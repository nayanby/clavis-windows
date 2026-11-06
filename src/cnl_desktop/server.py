"""Local HTTP server the app already knows how to talk to.

Only explicit routes are served. This deliberately does not subclass
SimpleHTTPRequestHandler with a directory argument, which would expose the whole
application tree (including the WebView2 profile, where API keys live) over HTTP.

Logging never touches stdout/stderr: in a --windowed PyInstaller build both are
None, so a single stray write raises AttributeError on every request.
"""

from __future__ import annotations

import base64
import json
import logging
import math
import mimetypes
import time
import threading
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from . import (
    ai_notes,
    html_transform,
    ink,
    library,
    listen,
    paper,
    pearls,
    paths,
    pdf_engine,
    posters,
    render,
    speech,
    study_packs,
)

log = logging.getLogger("cnl_desktop.server")

DOCX_MIME = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
MASTER_NAME = "Clinical Notes Library"

VENDOR_MIME = {
    ".js": "application/javascript; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".woff2": "font/woff2",
    ".ttf": "font/ttf",
    ".ico": "image/x-icon",
    ".svg": "image/svg+xml; charset=utf-8",
}

ICON_MIME = {
    ".png": "image/png",
    ".svg": "image/svg+xml; charset=utf-8",
}

# Kept as documentation; every response sets Content-Type explicitly so the
# Windows registry cannot influence it.
mimetypes.add_type(DOCX_MIME, ".docx")

# A layout record is a handful of numbers per note, so these caps sit far above
# anything a real note needs. They exist to bound what one POST can write to disk
# and to keep a clamped column width inside a range the reader can still render.
_MAX_LAYOUT_TABLES = 200
_MAX_LAYOUT_COLUMNS = 40
_MAX_LAYOUT_MOVES = 500
_MIN_COLUMN_PX = 20
_MAX_COLUMN_PX = 4000
_MAX_LAYOUT_INDEX = 100000
_SNAP_PULLING = False


def _pull_snapshots_later() -> None:
    """Fill in missing snapshot files after the first catalog paint."""
    global _SNAP_PULLING
    if _SNAP_PULLING:
        return

    def run() -> None:
        global _SNAP_PULLING
        _SNAP_PULLING = True
        try:
            log.info("snapshots stay in the local data folder")
        finally:
            _SNAP_PULLING = False

    threading.Thread(target=run, daemon=True, name="cnl-snap-pull").start()


def _layout_index(value) -> int | None:
    """Coerce one document-order index, or None if it is not a usable one."""
    try:
        number = int(value)
    except (TypeError, ValueError):
        return None
    return number if 0 <= number <= _MAX_LAYOUT_INDEX else None


def _clean_layout(payload) -> dict:
    """Reduce a posted layout to exactly what the reader knows how to apply.

    Anything unrecognised is dropped rather than rejected: the record is the
    user's own reading preference, and losing one malformed entry is better than
    failing the whole save.
    """
    if not isinstance(payload, dict):
        return {}
    cleaned: dict = {}

    columns = payload.get("columns")
    if isinstance(columns, dict):
        widths_by_table: dict = {}
        for raw_table, raw_widths in columns.items():
            table = _layout_index(raw_table)
            if table is None or not isinstance(raw_widths, list):
                continue
            widths = []
            for raw_width in raw_widths[:_MAX_LAYOUT_COLUMNS]:
                try:
                    px = round(float(raw_width))
                except (TypeError, ValueError):
                    continue
                widths.append(min(max(px, _MIN_COLUMN_PX), _MAX_COLUMN_PX))
            if widths:
                widths_by_table[str(table)] = widths
            if len(widths_by_table) >= _MAX_LAYOUT_TABLES:
                break
        if widths_by_table:
            cleaned["columns"] = widths_by_table

    moves = payload.get("images")
    if isinstance(moves, list):
        image_moves = []
        for entry in moves[:_MAX_LAYOUT_MOVES]:
            if not isinstance(entry, dict):
                continue
            image = _layout_index(entry.get("image"))
            before = _layout_index(entry.get("before"))
            if image is None or before is None:
                continue
            image_moves.append({"image": image, "before": before})
        if image_moves:
            cleaned["images"] = image_moves

    return cleaned


# The one type preference the client cannot compute for itself is the face. Beside it
# the reader keeps three scales, which are controls again; the poster's own three are
# still baked into the client at the values the app was being read at, so nothing
# offers them and nothing posts them.
_VIEW_FONTS = ("averia", "inter", "averia-serif", "averia-sans", "noto-serif", "lato", "open-sans", "aptos")

# What a record saved while those three were controls still carries. Dropping them on
# the way through a save is what stops them being merged forward forever, which is the
# same treatment the two reading-mode keys already get.
_RETIRED_SCALE_KEYS = (
    "posterText",
    "posterSpace",
    "posterLine",
)

# The reader's three scales as the same five-rung ladders the client offers: two steps
# either side of the value each was baked at, 5% a step for text size and 10% for the
# two spacings. Built from the default and the step rather than written out, so the
# server's ends cannot drift away from the client's middle.
# Consumer TypeSettings ladders: millipoints, sixteenths, and paragraph permille.
_READER_SCALES = {
    "textScale": tuple(range(-1500,1501,250)),
    "lineScale": tuple(range(16,33)),
    "paraScale": (1000,1300,1600,1900,2200),
}

# The scheduler's five live settings, as the same five menus the client offers. They
# are choices rather than ranges: unlike a percentage, a retention or an interval the
# menu never listed moves every deck in the library in a way nothing on screen would
# have predicted, so an unlisted value is dropped and the stored one kept.
_FSRS_RETENTION = (0.9, 0.91, 0.92)
_FSRS_NEW_PER_DAY = (20.0, 30.0, 40.0)
_FSRS_MAX_INTERVAL = (90.0, 180.0, 365.0)
_FSRS_RELEARNING = (5.0, 10.0, 20.0, 30.0)
_FSRS_MAX_REVIEWS = (100.0, 200.0, 500.0, 9999.0)
_FSRS_FIELDS = (
    ("desiredRetention", _FSRS_RETENTION),
    ("newCardsPerDay", _FSRS_NEW_PER_DAY),
    ("maxIntervalDays", _FSRS_MAX_INTERVAL),
    ("relearningMinutes", _FSRS_RELEARNING),
    ("maxReviewsPerDay", _FSRS_MAX_REVIEWS),
)


def _prefs_choice(value, allowed) -> str | None:
    """Return the value only if it is one of the known choices."""
    return str(value) if value in allowed else None


def _prefs_choice_number(value, allowed) -> int | float | None:
    """Return a posted number only if the menu actually offers it.

    Not clamped: these are choices rather than ranges, and clamping would quietly
    turn a posted 5000 reviews/day into the 9999 the client labels Unlimited.
    Returned as an int when whole, so four of the five land in the stored record as
    the counts they are rather than as 30.0.
    """
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if not math.isfinite(number) or number not in allowed:
        return None
    return int(number) if number.is_integer() else number


def _clean_prefs(payload) -> dict:
    """Reduce posted preferences to the values the reader and the scheduler use.

    Unrecognised keys are dropped rather than rejected, and the caller merges the
    result over what is already on disk, so one malformed field costs that field
    alone instead of resetting everything the user had chosen. Because that merge
    keeps stored keys, the caller is also what retires a key this build no longer
    reads: the two an older build wrote for a reading mode it did not have, and the
    poster's three scales, which are baked into the client instead.
    """
    if not isinstance(payload, dict):
        return {}
    cleaned: dict = {}
    if payload.get("typeLadderVersion") == 2:
        cleaned["typeLadderVersion"] = 2
    if payload.get("consumerViewerVersion") in (1, 2):
        cleaned["consumerViewerVersion"] = int(payload["consumerViewerVersion"])

    font = _prefs_choice(payload.get("font"), _VIEW_FONTS)
    if font:
        cleaned["font"] = font

    snapshot_font = _prefs_choice(payload.get("snapshotFont"), _VIEW_FONTS)
    if snapshot_font:
        cleaned["snapshotFont"] = snapshot_font
    scales = dict(_READER_SCALES)
    scales.update({"snapshot" + key[0].upper() + key[1:]: ladder
                   for key, ladder in _READER_SCALES.items()})
    for key, ladder in scales.items():
        number = _prefs_choice_number(payload.get(key), ladder)
        if number is not None:
            cleaned[key] = number

    fsrs = payload.get("fsrs")
    if isinstance(fsrs, dict):
        scheduler = {}
        for key, allowed in _FSRS_FIELDS:
            number = _prefs_choice_number(fsrs.get(key), allowed)
            if number is not None:
                scheduler[key] = number
        if scheduler:
            cleaned["fsrs"] = scheduler

    return cleaned


class AppServer(ThreadingHTTPServer):
    """Threaded because the app fans out many parallel poster requests.

    block_on_close is inherited as True, which joins handler threads on shutdown
    and can hang exit while keep-alive sockets are still open.
    """

    daemon_threads = True
    block_on_close = False
    allow_reuse_address = True

    # socketserver defaults the listen backlog to 5. The app fans out one
    # /api/poster request per heading with Promise.all, so bursts of 50+
    # simultaneous connections are normal and anything past the backlog is
    # refused or reset. Queue them in the kernel instead.
    request_queue_size = 256

    def __init__(self, data_root: Path, host: str = "127.0.0.1", port: int = 0):
        self.data_root = Path(data_root)
        self.files_root = paths.files_dir(self.data_root)
        self.study_root = paths.study_dir(self.data_root)
        self.resource_root = paths.resource_root()
        self._html_cache: str | None = None

        paths.ensure_data_tree(self.data_root)
        self._catalog_lock = threading.Lock()
        self._library_catalog = library.read_saved_catalog(self.data_root)
        if self._library_catalog is None:
            self._library_catalog = library.scan_library(self.files_root, MASTER_NAME, headings=False)
        try:
            migrated = study_packs.migrate_saved_quizzes(self.study_root)
            if migrated:
                log.info("split %d saved quizzes into individual files", migrated)
        except Exception:
            log.exception("could not split saved quizzes into individual files")
        try:
            migrated = study_packs.migrate_flashcard_folders(self.study_root)
            log.info("flashcard numbered folders ready: %d decks", migrated)
        except Exception:
            log.exception("could not migrate flashcard folders")
        try:
            paper.adopt_pdfs(self.data_root)
        except Exception:
            log.exception("could not take new PDFs onto the shelf")

        # Once at startup rather than on the route that lists snapshots: the home
        # screen waits on that route, and a pack holding a whole library would make
        # the first paint wait on a migration. Never fatal - a library whose pack
        # cannot be read still opens, it just opens without the rows inside it.
        try:
            posters.import_legacy_pack(self.study_root, self.files_root)
        except Exception:
            log.exception("could not import the snapshot pack")
        try:
            count = posters.migrate_snapshot_folders(self.study_root)
            log.info("snapshot numbered folders ready: %d snapshots", count)
        except Exception:
            log.exception("could not migrate snapshot folders")

        super().__init__((host, port), Handler)
        threading.Thread(target=self._refresh_catalog_background, daemon=True,
                         name="cnl-catalog-refresh").start()

    def refresh_catalog(self) -> dict:
        with self._catalog_lock:
            payload = library.scan_library(self.files_root, MASTER_NAME)
            library.save_catalog(self.data_root, payload)
            self._library_catalog = payload
            return payload

    def _refresh_catalog_background(self) -> None:
        try:
            self.refresh_catalog()
        except Exception:
            log.exception("could not refresh saved library catalog; keeping previous catalog")

    @property
    def port(self) -> int:
        return self.server_address[1]

    def app_html(self) -> str:
        if self._html_cache is None:
            log.info("rendering app page")
            raw = (self.resource_root / "app.html").read_text(encoding="utf-8")
            self._html_cache = html_transform.transform_html(raw)
            log.info("app page ready: %d characters", len(self._html_cache))
        return self._html_cache


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    server_version = "ClinicalNotesDesktop/1.0"

    # Silence the default stderr access log entirely.
    def log_message(self, fmt, *args):
        log.debug("%s - %s", self.address_string(), fmt % args)

    def log_error(self, fmt, *args):
        log.warning("%s - %s", self.address_string(), fmt % args)

    @property
    def app(self) -> AppServer:
        return self.server  # type: ignore[return-value]

    def end_headers(self):
        # Notes are edited in Word while the app is open; never serve a stale copy.
        self.send_header("Cache-Control", "no-store, max-age=0")
        self.send_header("X-Content-Type-Options", "nosniff")
        super().end_headers()

    # ---- response helpers -------------------------------------------------

    def _send(self, status: int, body: bytes, content_type: str) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        # HTTP/1.1 keep-alive depends on an accurate length on every response.
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def _send_json(self, status: int, payload) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self._send(status, body, "application/json; charset=utf-8")

    def _send_file(self, path: Path, content_type: str) -> None:
        try:
            body = path.read_bytes()
        except OSError:
            log.warning("could not read %s", path)
            self._send_json(404, {"error": "File not found."})
            return
        self._send(200, body, content_type)

    # ---- routing ----------------------------------------------------------

    def do_GET(self) -> None:  # noqa: N802
        parsed = urllib.parse.urlparse(self.path)
        route = parsed.path
        query = urllib.parse.parse_qs(parsed.query)

        try:
            if route in ("/", "/index.html", "/app.html"):
                self._serve_app()
            elif route == "/api/library":
                self._serve_library()
            elif route == "/api/pearls":
                self._send_json(200, pearls.catalog(self.app.data_root))
            elif route == "/api/pearls/document":
                target = pearls.resolve(self.app.data_root / 'Pearls', (query.get('id') or [''])[0])
                if target is None:
                    self._send_json(404, {'error': 'Pearl not found.'})
                else:
                    self._send_file(target, DOCX_MIME)
            elif route == "/api/posters":
                self._serve_posters()
            elif route == "/api/h1-coverage":
                self._serve_h1_coverage()
            elif route == "/api/refresh":
                self._serve_refresh()
            elif route == "/api/performance":
                self._serve_performance()
            elif route.startswith("/files/"):
                self._serve_docx(route[len("/files/") :])
            elif route == "/api/poster":
                self._serve_poster_get(query)
            elif route == "/api/saved-quiz":
                self._serve_saved_quiz_get(query)
            elif route == "/api/study-pack":
                self._serve_study_pack_get(query)
            elif route == "/api/layout":
                self._serve_layout_get(query)
            elif route == "/api/ink":
                self._serve_ink_get(query)
            elif route == "/api/listen":
                self._serve_listen_get(query)
            elif route == "/api/listen/clip":
                self._serve_listen_clip(query)
            elif route == "/api/speech/status":
                self._send_json(200, speech.status())
            elif route == "/api/speech/clip":
                self._serve_speech_clip(query)
            elif route == "/api/pdfs":
                self._serve_pdf_list()
            elif route == "/api/paper":
                self._serve_paper_list()
            elif route == "/api/paper/outline":
                self._serve_paper_outline_get(query)
            elif route == "/api/pdf/outline":
                self._serve_pdf_outline(query)
            elif route == "/api/pdf/page":
                self._serve_pdf_page(query)
            elif route == "/api/prefs":
                self._serve_prefs_get()
            elif route == "/app.ico":
                self._serve_icon()
            elif route.startswith("/local-fonts/"):
                self._serve_local_font(route)
            elif route.startswith("/vendor/"):
                self._serve_vendor(route)
            elif route.startswith("/icons/"):
                self._serve_icon_asset(route)
            else:
                self._send_json(404, {"error": f"No such endpoint: {route}"})
        except html_transform.TransformError as err:
            log.error("HTML rewrite failed: %s", err)
            self._send_json(500, {"error": str(err)})
        except (listen.ListenError, paper.PaperError, pdf_engine.PdfError, speech.SpeechError) as err:
            # Wording written for the user, same as the POST routes treat theirs.
            self._send_json(400, {"error": str(err)})
        except Exception:  # keep one bad request from killing the thread
            log.exception("unhandled error on GET %s", self.path)
            self._send_json(500, {"error": "Internal server error."})

    def do_HEAD(self) -> None:  # noqa: N802
        self.do_GET()

    def do_POST(self) -> None:  # noqa: N802
        parsed = urllib.parse.urlparse(self.path)
        try:
            if parsed.path == "/api/poster":
                self._serve_poster_post()
            elif parsed.path == "/api/saved-quiz":
                self._serve_saved_quiz_post()
            elif parsed.path == "/api/study-attempt":
                self._serve_study_attempt()
            elif parsed.path == "/api/study-pack":
                self._serve_study_pack_post()
            elif parsed.path == "/api/layout":
                self._serve_layout_post()
            elif parsed.path == "/api/ink":
                self._serve_ink_post()
            elif parsed.path == "/api/paper":
                self._serve_paper_post()
            elif parsed.path == "/api/listen":
                self._serve_listen_post()
            elif parsed.path == "/api/speech":
                self._serve_speech_post()
            elif parsed.path == "/api/pdf/import":
                self._serve_pdf_import()
            elif parsed.path == "/api/prefs":
                self._serve_prefs_post()
            elif parsed.path == "/api/ai-note":
                self._serve_ai_note_post()
            elif parsed.path == "/api/export":
                self._serve_export_post()
            else:
                self._send_json(404, {"error": f"No such endpoint: {parsed.path}"})
        except (
            ai_notes.AiNotesError,
            ink.InkError,
            listen.ListenError,
            paper.PaperError,
            pdf_engine.PdfError,
            posters.PosterError,
            render.RenderError,
            speech.SpeechError,
        ) as err:
            # These carry wording written for the user, not a stack trace.
            self._send_json(400, {"error": str(err)})
        except Exception:
            log.exception("unhandled error on POST %s", self.path)
            self._send_json(500, {"error": "Internal server error."})

    # ---- handlers ---------------------------------------------------------

    def _serve_app(self) -> None:
        html = self.app.app_html()
        self._send(200, html.encode("utf-8"), "text/html; charset=utf-8")

    def _serve_library(self) -> None:
        payload = self.app._library_catalog
        log.info("library catalog: %d document(s)", len(payload["documents"]))
        self._send_json(200, payload)

    def _serve_refresh(self) -> None:
        """Force-pull the shared catalog the way Master's pull-to-refresh does."""
        notes = self.app.refresh_catalog()["documents"]
        paper.refresh_from_master(self.app.data_root)
        pdfs = paper.list_pdfs(self.app.data_root, refresh=True)
        notebooks = paper.list_notebooks(self.app.data_root, refresh=True)
        log.info(
            "local refresh: %d note(s), %d PDF(s), %d notebook(s)",
            len(notes),
            len(pdfs),
            len(notebooks),
        )
        self._send_json(
            200,
            {
                "pulled": [],
                "notes": len(notes),
                "pdfs": len(pdfs),
                "notebooks": len(notebooks),
            },
        )

    def _serve_h1_coverage(self) -> None:
        """How many Heading 1s already have flashcards, quizzes and snapshots."""
        payload = library.scan_h1_coverage(self.app.files_root, self.app.study_root)
        log.info(
            "coverage H1/H2 flash %d/%d + %d/%d quiz %d/%d + %d/%d snapshot %d/%d + %d/%d",
            payload.get("flashH1", payload.get("flash", 0)),
            payload.get("h1", payload.get("total", 0)),
            payload.get("flashH2", 0),
            payload.get("h2", 0),
            payload.get("quizH1", payload.get("quiz", 0)),
            payload.get("h1", payload.get("total", 0)),
            payload.get("quizH2", 0),
            payload.get("h2", 0),
            payload.get("snapshotH1", payload.get("snapshot", 0)),
            payload.get("h1", payload.get("total", 0)),
            payload.get("snapshotH2", 0),
            payload.get("h2", 0),
        )
        self._send_json(200, payload)

    def _serve_posters(self) -> None:
        """List every saved poster, grouped the way the library is.

        Derived from a library scan rather than a walk of study-data so each
        poster carries the exact doc string the app saved it under and can be
        reopened with it. The home screen waits on this, so it is served fresh
        but never caches: a poster saved a moment ago has to show up.
        """
        try:
            posters.import_legacy_pack(self.app.study_root, self.app.files_root)
        except Exception:
            log.exception("could not import the phone snapshot pack")
        documents = library.scan_library(self.app.files_root, MASTER_NAME)["documents"]
        payload = posters.scan_posters(self.app.study_root, documents)
        _pull_snapshots_later()
        log.info(
            "poster scan: %d subject(s), %d read and %d reviewed today",
            len(payload["subjects"]),
            payload["today"]["read"],
            payload["today"]["reviewed"],
        )
        self._send_json(200, payload)

    def _serve_performance(self) -> None:
        """Quiz and flashcard results across the whole library.

        Scanned fresh on every call for the same reason the poster listing does: the
        Performance tab is what a user opens after finishing a quiz, so it has to show
        the attempt that was written a moment ago rather than one from launch.
        """
        documents = library.scan_library(self.app.files_root, MASTER_NAME)["documents"]
        payload = posters.scan_performance(self.app.study_root, documents)
        log.info(
            "performance scan: %d quiz attempt(s) over %d note(s), %d deck(s), %d card(s)",
            payload["quiz"]["attempts"],
            payload["quiz"]["notes"],
            payload["flashcards"]["deckCount"],
            payload["flashcards"]["cards"],
        )
        self._send_json(200, payload)

    def _serve_docx(self, relative: str) -> None:
        target = library.resolve_docx(self.app.files_root, relative)
        if target is None:
            self._send_json(403, {"error": "Forbidden."})
            return
        self._send_file(target, DOCX_MIME)

    def _poster_key(self, params: dict):
        return (
            (params.get("doc") or "").strip(),
            (params.get("documentKey") or "").strip(),
            (params.get("scope") or "").strip(),
        )

    def _serve_poster_get(self, query: dict) -> None:
        doc, key, scope = self._poster_key(
            {k: v[0] if v else "" for k, v in query.items()}
        )
        if not doc:
            self._send_json(400, {"error": "Missing 'doc' parameter."})
            return

        payload = posters.read_poster(self.app.study_root, doc, key, scope)
        if payload is None:
            # 404 means "nothing saved yet" to the app; it is not a failure.
            self._send_json(404, {"error": "Not found."})
            return
        self._send_json(200, payload)

    def _serve_ink_get(self, query: dict) -> None:
        params = {k: v[0] if v else "" for k, v in query.items()}
        doc = (params.get("doc") or "").strip()
        if not doc:
            self._send_json(400, {"error": "Missing 'doc' parameter."})
            return

        payload = ink.read_ink(self.app.data_root, doc, params.get("scope"))
        if payload is None:
            # 404 means "nothing drawn yet" to the app; it is not a failure.
            self._send_json(404, {"error": "Not found."})
            return
        self._send_json(200, payload)

    def _serve_ink_post(self) -> None:
        # A page of dense handwriting runs to a few hundred kilobytes, and the
        # module's own caps decide what survives being parsed. This is only the
        # gate before the parse, so it is generous rather than exact.
        body = self._read_json(24 * 1024 * 1024)
        if body is None:
            return

        doc = str(body.get("doc") or "").strip()
        if not doc:
            self._send_json(400, {"error": "Missing 'doc'."})
            return

        scope = body.get("scope")
        if body.get("clear"):
            ink.delete_ink(self.app.data_root, doc, scope)
            self._send_json(200, {"ok": True, "strokes": 0})
            return

        document = ink.clean_document(body.get("ink"))
        path = ink.write_ink(self.app.data_root, doc, scope, document)
        if path is None:
            self._send_json(400, {"error": "Could not tell which note that ink belongs to."})
            return

        self._send_json(200, {"ok": True, "strokes": len(document["strokes"])})

    def _serve_listen_get(self, query: dict) -> None:
        """What has already been written and spoken for one section.

        Answered before the app asks for anything expensive, so a chapter listened
        to yesterday starts playing without another AI call or another trip to a
        voice service. The script comes back in full rather than as a flag: the app
        needs the text to follow along with, and it is the same few kilobytes it
        would have to fetch separately anyway.
        """
        params = {k: v[0] if v else "" for k, v in query.items()}
        key = (params.get("key") or "").strip()
        if not key:
            self._send_json(400, {"error": "Missing 'key' parameter."})
            return

        self._send_json(200, listen.describe(key, params.get("voice")))

    def _serve_listen_clip(self, query: dict) -> None:
        """One clip of speech, played straight out of the cache.

        Served as audio rather than wrapped in JSON so the page can hand the URL to
        an <audio> element and let the browser stream and seek it. Cached hard for
        the same reason a rendered PDF page is: a clip is the same bytes every time
        until the script behind it changes, and changing it clears the folder.
        """
        params = {k: v[0] if v else "" for k, v in query.items()}
        key = (params.get("key") or "").strip()
        if not key:
            self._send_json(400, {"error": "Missing 'key' parameter."})
            return

        path = listen.find_clip(key, params.get("voice"), params.get("index") or 0)
        if path is None:
            # 404 means "not spoken yet" to the app; it is not a failure.
            self._send_json(404, {"error": "Not found."})
            return

        try:
            body = path.read_bytes()
        except OSError:
            log.warning("could not read clip %s", path)
            self._send_json(404, {"error": "Not found."})
            return

        self.send_response(200)
        self.send_header("Content-Type", listen.content_type(path.suffix))
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Accept-Ranges", "none")
        self.send_header("Cache-Control", "private, max-age=3600")
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def _serve_listen_post(self) -> None:
        """Store a script, store a clip, or throw a section's audio away.

        Three actions on one route because all three are the same cache seen from
        different sides, and the app does them in sequence for a single chapter.

        The synthesis is not here. The page holds the API keys and makes both the
        script call and the voice call itself, the way it already makes every other
        AI call, and hands the result here to be kept.
        """
        # A clip arrives base64'd inside the JSON, so the gate has to clear the
        # module's own 32MB clip cap plus a third for the encoding.
        body = self._read_json(48 * 1024 * 1024)
        if body is None:
            return

        key = str(body.get("key") or "").strip()
        if not key:
            self._send_json(400, {"error": "Missing 'key'."})
            return

        voice = body.get("voice")

        if body.get("clear"):
            # Without a voice this takes the script too, which is what the app
            # wants when the note behind it was edited and the reading is stale.
            gone = listen.clear(key, voice if not body.get("all") else None)
            self._send_json(200, {"ok": True, "removed": gone})
            return

        if "script" in body:
            script = body.get("script")
            listen.write_script(key, script)
            chunks = listen.segment(script)
            self._send_json(
                200,
                {
                    "ok": True,
                    "chunks": chunks,
                    "digest": listen.script_digest(script),
                    "gapMs": listen.SECTION_GAP_MS,
                },
            )
            return

        if "audio" in body:
            try:
                audio = base64.b64decode(str(body.get("audio") or ""), validate=True)
            except (ValueError, TypeError):
                self._send_json(400, {"error": "That clip was not readable audio."})
                return

            listen.write_clip(
                key,
                voice,
                body.get("index") or 0,
                audio,
                body.get("format") or "mp3",
            )
            self._send_json(200, {"ok": True, "bytes": len(audio)})
            return

        self._send_json(400, {"error": "Nothing to do: send a script, a clip, or clear."})

    def _serve_speech_clip(self, query: dict) -> None:
        """One synthesised sentence, played straight from the clip cache."""
        params = {k: v[0] if v else "" for k, v in query.items()}
        path = speech.clip_path(params.get("name"))
        self._send_file(path, "audio/wav")

    def _serve_speech_post(self) -> None:
        """Start the voice download, or speak one sentence.

        Synthesis runs here rather than in the page: the voice is a local model,
        not a web service, so the page neither holds a key nor sees the samples.
        """
        body = self._read_json(64 * 1024)
        if body is None:
            return

        op = str(body.get("op") or "speak")
        if op == "download":
            self._send_json(200, speech.download())
            return

        if op != "speak":
            self._send_json(400, {"error": f"Unknown speech operation: {op}"})
            return

        clip = speech.speak(body.get("text"), body.get("rate"), body.get("speaker"))
        clip["url"] = "/api/speech/clip?name=" + urllib.parse.quote(clip["name"])
        self._send_json(200, clip)

    def _serve_pdf_import(self) -> None:
        """Take a PDF the user picked in the file dialog onto the shelf.

        A route of its own rather than another action on /api/paper, because that
        route's body cap is sized for index edits of a few kilobytes and a textbook
        is three orders of magnitude past it.
        """
        # A PDF arrives base64'd inside the JSON, so the gate has to clear the
        # module's own 512MB ceiling plus a third for the encoding.
        body = self._read_json(700 * 1024 * 1024)
        if body is None:
            return

        try:
            blob = base64.b64decode(str(body.get("base64") or ""), validate=True)
        except (ValueError, TypeError):
            self._send_json(400, {"error": "That file could not be read."})
            return

        row = paper.import_pdf(
            self.app.data_root, body.get("name"), blob, body.get("folder")
        )
        self._send_json(200, {"pdf": row})

    def _serve_pdf_list(self) -> None:
        found = pdf_engine.list_pdfs(self.app.data_root)
        log.info("PDF scan: %d file(s)", len(found))
        self._send_json(200, {"pdfs": found})

    def _serve_paper_list(self) -> None:
        """Everything the paper screens list: the PDF shelf and the notebooks.

        One route for both because the two are shown side by side and neither is
        useful without the folder list, so three requests would only mean three
        chances for the screen to paint half of itself.
        """
        root = self.app.data_root
        paper.pull_paper_indexes(root)
        paper.adopt_pdfs(root)
        self._send_json(
            200,
            {
                "pdfs": paper.list_pdfs(root),
                "folders": paper.list_pdf_folders(root),
                "notebooks": paper.list_notebooks(root),
            },
        )

    def _serve_paper_outline_get(self, query: dict) -> None:
        params = {k: v[0] if v else "" for k, v in query.items()}
        key = (params.get("key") or "").strip()
        if not key:
            self._send_json(400, {"error": "Missing 'key' parameter."})
            return
        self._send_json(200, {"outline": paper.read_outline(self.app.data_root, key)})

    def _serve_paper_post(self) -> None:
        """Every change to the shelf and the notebooks, told apart by 'action'.

        One route rather than nine, because they all rewrite one of the same small
        indexes and each would otherwise be four lines of dispatch for one call.
        """
        body = self._read_json(1 * 1024 * 1024)
        if body is None:
            return

        root = self.app.data_root
        action = str(body.get("action") or "").strip()
        item_id = body.get("id")

        if action == "rename-pdf":
            self._send_json(200, {"pdf": paper.rename_pdf(root, item_id, body.get("name"))})
        elif action == "move-pdf":
            self._send_json(200, {"pdf": paper.move_pdf(root, item_id, body.get("folder"))})
        elif action == "delete-pdf":
            self._send_json(200, {"pdf": paper.delete_pdf(root, item_id)})
        elif action == "create-folder":
            self._send_json(200, {"folder": paper.create_pdf_folder(root, body.get("name"))})
        elif action == "create-notebook":
            notebook = paper.create_notebook(root, body.get("name"), bool(body.get("ruled", True)))
            self._send_json(200, {"notebook": notebook})
        elif action == "rename-notebook":
            self._send_json(200, {"notebook": paper.rename_notebook(root, item_id, body.get("name"))})
        elif action == "add-page":
            self._send_json(200, {"notebook": paper.add_notebook_page(root, item_id)})
        elif action == "set-pages":
            self._send_json(200, {"notebook": paper.set_notebook_pages(root, item_id, body.get("pages"))})
        elif action == "delete-notebook":
            self._send_json(200, {"notebook": paper.delete_notebook(root, item_id)})
        elif action == "outline":
            rows = paper.write_outline(root, body.get("key"), body.get("outline"))
            self._send_json(200, {"outline": rows})
        else:
            self._send_json(400, {"error": f"Unknown action: {action or '(none)'}"})

    def _pdf_at(self, query: dict) -> Path:
        """The PDF one request names, or a refusal the user can read."""
        params = {k: v[0] if v else "" for k, v in query.items()}
        return pdf_engine.resolve(self.app.data_root, params.get("doc"))

    def _serve_pdf_outline(self, query: dict) -> None:
        """A PDF's bookmarks and how many pages it has.

        The two together because the view needs both before it can draw anything,
        and asking for them separately would open the document twice.
        """
        path = self._pdf_at(query)
        self._send_json(
            200,
            {
                "pages": pdf_engine.page_count(path),
                "outline": pdf_engine.outline(path),
            },
        )

    def _serve_pdf_page(self, query: dict) -> None:
        """One page drawn to a PNG.

        The page's shape rides back in a header rather than in the body, because the
        body is the image: the view needs the aspect to size the row it is about to
        put the image in, and reading it off the decoded image would mean waiting
        for the decode. Cached hard - a page of a PDF that has not changed is the
        same pixels every time, and the view asks for the same page whenever it
        scrolls back to it.
        """
        params = {k: v[0] if v else "" for k, v in query.items()}
        path = pdf_engine.resolve(self.app.data_root, params.get("doc"))

        png, aspect = pdf_engine.render_page(
            path,
            params.get("page") or 0,
            params.get("width") or 0,
            params.get("quality") or 1.0,
        )

        self.send_response(200)
        self.send_header("Content-Type", "image/png")
        self.send_header("Content-Length", str(len(png)))
        self.send_header("X-Page-Aspect", f"{aspect:.6f}")
        self.send_header("Cache-Control", "private, max-age=3600")
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(png)

    def _read_json(self, limit: int):
        """Parse a JSON request body, or send the 400 and return None."""
        try:
            length = int(self.headers.get("Content-Length") or 0)
        except ValueError:
            length = 0
        if length <= 0 or length > limit:
            self._send_json(400, {"error": "Missing or oversized request body."})
            return None

        raw = self.rfile.read(length)
        try:
            return json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, ValueError):
            self._send_json(400, {"error": "Request body is not valid JSON."})
            return None

    def _serve_poster_post(self) -> None:
        body = self._read_json(64 * 1024 * 1024)
        if body is None:
            return

        # No op field means save. The poster body is what makes a request a save,
        # and it carries no op, so the operation is read here rather than required.
        op = str(body.get("op") or "save")
        if op == "rename":
            self._serve_poster_rename(body)
            return
        if op == "delete":
            self._serve_poster_delete(body)
            return
        if op == "quiz":
            self._serve_quiz_record(body)
            return
        if op != "save":
            self._send_json(400, {"error": f"Unknown snapshot operation: {op}"})
            return

        doc = str(body.get("doc") or "")
        key = str(body.get("documentKey") or "")
        scope = str(body.get("scope") or "")
        if "poster" not in body:
            self._send_json(400, {"error": "Missing 'poster' field."})
            return

        saved = posters.write_poster(self.app.study_root, doc, key, scope, body["poster"])
        if saved is None:
            self._send_json(400, {"error": "Could not resolve a storage path for that document."})
            return

        # A snapshot lands in the shared pack and every other record under
        # study-data, so the location is named rather than made relative to a
        # tree the file may not be in.
        try:
            where = saved.relative_to(self.app.study_root).as_posix()
        except ValueError:
            where = saved.parent.name

        log.info("saved study data: %s", saved.name)
        self._send_json(200, {"saved": True, "path": where})

    def _poster_ref(self, body: dict) -> tuple[str, str, str]:
        """The triple that identifies one saved poster, as the listing reports it."""
        return (
            str(body.get("doc") or "").strip(),
            str(body.get("documentKey") or "").strip(),
            str(body.get("scope") or "").strip(),
        )

    def _serve_poster_rename(self, body: dict) -> None:
        doc, key, scope = self._poster_ref(body)
        if not doc:
            self._send_json(400, {"error": "Missing 'doc' field."})
            return

        title = str(body.get("title") or "")
        renamed = posters.rename_poster(self.app.study_root, doc, key, scope, title)
        if renamed is None:
            self._send_json(400, {"error": "Could not resolve a storage path for that document."})
            return

        self._send_json(200, {"renamed": True, "title": title.strip()})

    def _serve_poster_delete(self, body: dict) -> None:
        doc, key, scope = self._poster_ref(body)
        if not doc:
            self._send_json(400, {"error": "Missing 'doc' field."})
            return

        moved = posters.delete_poster(
            self.app.study_root, paths.trash_dir(self.app.data_root), doc, key, scope
        )
        if moved is None:
            self._send_json(400, {"error": "Could not resolve a storage path for that document."})
            return

        self._send_json(200, {"deleted": True, "trash": moved.name})

    def _serve_quiz_record(self, body: dict) -> None:
        """Append one finished quiz to the note's result record.

        Shares /api/poster rather than getting a route of its own because the
        containment that makes doc and documentKey safe to turn into a path already
        lives here, and a second route would need a second copy of it.

        No scope is read from the request. There is one quiz record per note and its
        name is fixed in the store, so this op cannot be aimed at any other file in
        the tree however the request is written - which is why the two components it
        does take are the only thing the boundary has to hold.
        """
        doc = str(body.get("doc") or "").strip()
        key = str(body.get("documentKey") or "").strip()
        if not doc:
            self._send_json(400, {"error": "Missing 'doc' field."})
            return

        saved = posters.record_quiz_result(self.app.study_root, doc, key, body.get("attempt"))
        if saved is None:
            self._send_json(400, {"error": "Could not resolve a storage path for that document."})
            return

        self._send_json(
            200,
            {"recorded": True, "path": saved.relative_to(self.app.data_root).as_posix()},
        )

    def _serve_saved_quiz_get(self, query: dict) -> None:
        """The ready-made quiz the phone wrote for one heading, if there is one."""
        params = {k: v[0] if v else "" for k, v in query.items()}
        row = study_packs.find_saved_quiz(
            self.app.study_root,
            str(params.get("folder") or ""),
            str(params.get("document") or ""),
            str(params.get("heading") or params.get("headingText") or ""),
        )
        if row is None:
            self._send_json(404, {"error": "Not found."})
            return
        self._send_json(200, row)

    def _serve_saved_quiz_post(self) -> None:
        """Keep one generated quiz in the shared pack so the tablet can take it."""
        body = self._read_json(4 * 1024 * 1024)
        if body is None:
            return
        saved = study_packs.upsert_saved_quiz(self.app.study_root, body)
        if saved is None:
            self._send_json(400, {"error": "A saved quiz needs a heading and questions."})
            return
        self._send_json(200, {"saved": True, "quiz": saved})

    def _study_pack_payload(self, kind: str, incoming_decks=None):
        """The JSON Master imports from Storage, or None when that pack is empty."""
        name = str(kind or "").strip().lower()
        if name in ("flashcards", "flash"):
            if incoming_decks:
                study_packs.merge_flash_decks(self.app.study_root, incoming_decks)
            decks = study_packs.read_flash_decks(self.app.study_root)
            if not decks:
                return None
            return {"version": 1, "decks": decks}
        if name in ("quizzes", "quiz"):
            quizzes = study_packs.read_quizzes(self.app.study_root)
            if not quizzes:
                return None
            return {"version": 1, "quizzes": quizzes}
        if name in ("snapshots", "posters"):
            pack = posters.export_phone_pack(self.app.study_root)
            if not pack.get("posters"):
                return None
            return pack
        return False

    def _serve_study_pack_get(self, query: dict) -> None:
        """Download one of the three packs Master can import from Storage."""
        params = {k: v[0] if v else "" for k, v in query.items()}
        payload = self._study_pack_payload(str(params.get("kind") or ""))
        if payload is False:
            self._send_json(400, {"error": "kind must be flashcards, quizzes or snapshots."})
            return
        if payload is None:
            self._send_json(404, {"error": "Not found."})
            return
        self._send_json(200, payload)

    def _serve_study_attempt(self) -> None:
        body = self._read_json(16384)
        if body is None:
            return
        correct, total = body.get("correct"), body.get("total")
        if (type(correct) is not int or type(total) is not int
                or total < 1 or total > 10000 or not 0 <= correct <= total):
            self._send_json(400, {"error": "Invalid quiz result."})
            return
        study_packs.append_run(self.app.study_root, int(time.time() * 1000),
                               correct, total, str(body.get("label") or "Qbank"))
        self._send_json(200, {"saved": True})

    def _serve_study_pack_post(self) -> None:
        """Build a share pack, folding in any decks the page still holds."""
        body = self._read_json(32 * 1024 * 1024)
        if body is None:
            return
        kind = str(body.get("kind") or "")
        incoming = body.get("decks") if isinstance(body.get("decks"), list) else None
        payload = self._study_pack_payload(kind, incoming)
        if payload is False:
            self._send_json(400, {"error": "kind must be flashcards, quizzes or snapshots."})
            return
        if payload is None:
            self._send_json(404, {"error": "Not found."})
            return
        self._send_json(200, payload)

    def _serve_layout_get(self, query: dict) -> None:
        params = {k: v[0] if v else "" for k, v in query.items()}
        doc = str(params.get("doc") or "").strip()
        key = str(params.get("documentKey") or "").strip()
        if not doc:
            self._send_json(400, {"error": "Missing 'doc' parameter."})
            return

        payload = posters.read_layout(self.app.study_root, doc, key)
        if payload is None:
            # As for posters: 404 means "nothing saved yet", not a failure.
            self._send_json(404, {"error": "Not found."})
            return
        self._send_json(200, payload)

    def _serve_layout_post(self) -> None:
        # A layout record is column widths and image moves, so it is tiny; the
        # poster route's 64 MiB allowance is for embedded images and would let one
        # request write an unbounded file here.
        body = self._read_json(1024 * 1024)
        if body is None:
            return

        doc = str(body.get("doc") or "").strip()
        key = str(body.get("documentKey") or "").strip()
        if not doc:
            self._send_json(400, {"error": "Missing 'doc' field."})
            return
        if "layout" not in body:
            self._send_json(400, {"error": "Missing 'layout' field."})
            return

        layout = _clean_layout(body["layout"])
        saved = posters.write_layout(self.app.study_root, doc, key, layout)
        if saved is None:
            self._send_json(400, {"error": "Could not resolve a storage path for that document."})
            return

        log.info("saved note layout: %s", saved.name)
        self._send_json(200, {"saved": True, "layout": layout})

    def _serve_prefs_get(self) -> None:
        payload = posters.read_prefs(self.app.study_root)
        if payload is None:
            # 404 means "nothing chosen yet", so the client keeps its own defaults.
            self._send_json(404, {"error": "Not found."})
            return
        self._send_json(200, payload)

    def _serve_prefs_post(self) -> None:
        # One short string and a five-key nested record; the layout route's 1 MiB is
        # generous enough and nothing here needs more.
        body = self._read_json(1024 * 1024)
        if body is None:
            return
        if "prefs" not in body:
            self._send_json(400, {"error": "Missing 'prefs' field."})
            return

        stored = posters.read_prefs(self.app.study_root)
        merged = dict(stored) if isinstance(stored, dict) else {}
        # Keys nothing reads any more: two from when the reader still had modes, and
        # the poster's three scales from when they were controls. Dropping them here is
        # what stops them being merged forward forever.
        merged.pop("mode", None)
        merged.pop("fonts", None)
        for key in _RETIRED_SCALE_KEYS:
            merged.pop(key, None)

        cleaned = _clean_prefs(body["prefs"])
        # fsrs is the one nested record, so the shallow update below would replace
        # all five settings whenever one of them posted badly. Merging it here keeps
        # the promise the flat keys already make: one bad field costs that field.
        if isinstance(merged.get("fsrs"), dict) and isinstance(cleaned.get("fsrs"), dict):
            cleaned["fsrs"] = {**merged["fsrs"], **cleaned["fsrs"]}
        merged.update(cleaned)
        saved = posters.write_prefs(self.app.study_root, merged)

        log.info("saved preferences: %s", saved.name)
        self._send_json(200, {"saved": True, "prefs": merged})

    def _decode_docx(self, body: dict):
        """Validate an uploaded .docx payload, or send the 400 and return None."""
        try:
            blob = base64.b64decode(str(body.get("base64") or ""), validate=True)
        except ValueError:
            self._send_json(400, {"error": "Payload is not valid base64."})
            return None
        if not blob.startswith(b"PK\x03\x04"):
            self._send_json(400, {"error": "Payload is not a .docx container."})
            return None
        return blob

    def _serve_ai_note_post(self) -> None:
        """Save, rename or delete inside one of the two writable note folders.

        This is the only route that can write into the notes tree. Which folder it
        may write to is decided here from a fixed allow-list, never from a path in
        the request, and every file name goes through ai_notes, which sanitises and
        containment-checks it, so the rest of data\\files stays read-only.
        """
        body = self._read_json(64 * 1024 * 1024)
        if body is None:
            return

        op = str(body.get("op") or "").strip().lower()

        # Matched case-insensitively because the library scanner reports a subject
        # with the casing it happens to have on disk, and Windows folders are
        # case-insensitive: a library whose folder reads "AI notes" has to resolve
        # to the same root as one spelled "AI Notes".
        writable = {
            paths.MY_NOTES_SUBJECT.lower(): paths.my_notes_dir,
            paths.AI_NOTES_SUBJECT.lower(): paths.ai_notes_dir,
        }
        wanted = str(body.get("folder") or "").strip().lower()
        make_root = writable.get(wanted or paths.MY_NOTES_SUBJECT.lower())
        if make_root is None:
            self._send_json(400, {"error": "That folder is not writable."})
            return

        note_root = make_root(self.app.data_root)
        trash_root = paths.trash_dir(self.app.data_root)

        if op == "save":
            blob = self._decode_docx(body)
            if blob is None:
                return
            saved = ai_notes.save_note(note_root, str(body.get("name") or ""), blob)
            self._send_json(200, {"saved": True, "name": saved.name, "folder": note_root.name})
        elif op == "rename":
            renamed = ai_notes.rename_note(
                note_root, str(body.get("name") or ""), str(body.get("newName") or "")
            )
            self._send_json(200, {"renamed": True, "name": renamed.name})
        elif op == "delete":
            moved = ai_notes.delete_note(note_root, trash_root, str(body.get("name") or ""))
            self._send_json(200, {"deleted": True, "movedTo": moved.name})
        elif op == "delete-folder":
            count = ai_notes.delete_folder(note_root, trash_root)
            self._send_json(200, {"deleted": count})
        else:
            self._send_json(400, {"error": "Unknown or missing 'op'."})

    def _serve_export_post(self) -> None:
        """Render posted HTML to a PDF or a PNG with headless Edge.

        The HTML comes from our own page (a poster or a note already on screen)
        and is rendered from a temp file, so nothing here is written into data.
        """
        body = self._read_json(32 * 1024 * 1024)
        if body is None:
            return

        html = str(body.get("html") or "")
        want = str(body.get("format") or "").strip().lower()

        if want == "pdf":
            self._send(200, render.to_pdf(html, body.get("outline")), "application/pdf")
        elif want == "png":
            png = render.to_png(
                html, body.get("width"), body.get("height"), body.get("scale") or 2
            )
            self._send(200, png, "image/png")
        else:
            self._send_json(400, {"error": "format must be 'pdf' or 'png'."})

    def _serve_icon(self) -> None:
        icon = self.app.resource_root / "app.ico"
        if not icon.is_file():
            self._send_json(404, {"error": "Icon not bundled."})
            return
        self._send_file(icon, "image/x-icon")

    def _serve_local_font(self, route: str) -> None:
        from .local_fonts import aptos_font
        names = {"/local-fonts/aptos-" + style + ".ttf": style
                 for style in ("regular", "bold", "italic", "bold-italic")}
        style = names.get(route)
        target = aptos_font(style) if style else None
        if target is None:
            self._send_json(404, {"error": "Local font unavailable."})
            return
        self._send(200, target.read_bytes(), "font/ttf")

    def _serve_vendor(self, route: str) -> None:
        relative = urllib.parse.unquote(route[len("/vendor/") :])
        vendor_root = (self.app.resource_root / "vendor").resolve()
        target = (vendor_root / relative).resolve()

        if not target.is_relative_to(vendor_root) or not target.is_file():
            self._send_json(404, {"error": "No such asset."})
            return

        suffix = target.suffix.lower()
        content_type = VENDOR_MIME.get(suffix, "application/octet-stream")

        # Every vendored stylesheet is verbatim Google Fonts CSS still pointing at
        # fonts.gstatic.com; rewrite them the same way the HTML is rewritten.
        if suffix == ".css":
            css = html_transform.transform_font_css(target.read_text(encoding="utf-8"))
            self._send(200, css.encode("utf-8"), content_type)
            return

        self._send_file(target, content_type)

    def _serve_icon_asset(self, route: str) -> None:
        relative = urllib.parse.unquote(route[len("/icons/") :])
        icons_root = (self.app.resource_root / "icons").resolve()
        target = (icons_root / relative).resolve()

        if not target.is_relative_to(icons_root) or not target.is_file():
            self._send_json(404, {"error": "No such icon."})
            return

        suffix = target.suffix.lower()
        content_type = ICON_MIME.get(suffix, "application/octet-stream")
        self._send_file(target, content_type)

def start_server(data_root: Path | None = None, port: int = 0) -> AppServer:
    """Bind a loopback port and return the unstarted server.

    ``port=0`` lets the OS choose, which is what the packaged app wants; pass a
    number to hold a fixed address for browser-based verification.
    """
    return AppServer(data_root or paths.data_dir(), port=port)
