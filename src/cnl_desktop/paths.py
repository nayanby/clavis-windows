"""Filesystem layout resolution.

Three locations, and deciding which one a thing belongs in is the whole job:
bundled read-only assets ship inside the PyInstaller payload; ``data/`` lives next
to the .exe so the user can see and edit their notes in Explorer; and per-machine
state that must never be synced - the WebView2 profile - lives under
%LOCALAPPDATA%, because ``data/`` is normally inside OneDrive.
"""

from __future__ import annotations

import logging
import os
import re
import sys
from pathlib import Path

APP_NAME = "Clinical Notes Library"
BUNDLE_ID = "ClinicalNotesDesktop"

# Created inside the data tree on startup. Three names are deliberately absent:
# "app-profile", because the WebView2 profile lives outside the data tree entirely
# - see _local_root() - and "listen" and "speech", for the same reason - see
# listen_dir() and speech_dir().
DATA_SUBDIRS = (
    "files",
    "study-data",
    "Snapshots",
    "flashcards",
    "Qbank",
    "Pearls",
    "performance",
    "exports",
    "trash",
    "PDFs",
    "Notebooks",
    "paper",
    "ink",
)

# The phone exports its snapshots as one JSON file and the user drops it in by
# hand, so the folder is a shared location rather than a private one: the desktop
# reads the rows the phone wrote and appends its own to the same file.
SNAPSHOTS_DIRNAME = "Snapshots"
SNAPSHOTS_PACK_NAME = "phone_snapshots.json"

# The only two subject folders the app may write into. The HTML app hardcodes these
# same names when it saves an AI-generated note, so the two sides must not drift
# apart. My Notes is where a newly generated note goes; AI Notes is the earlier
# destination and stays writable because live libraries already hold notes there
# that the app can still rename or delete.
MY_NOTES_SUBJECT = "My Notes"
AI_NOTES_SUBJECT = "AI Notes"

log = logging.getLogger(BUNDLE_ID)


def is_frozen() -> bool:
    return bool(getattr(sys, "frozen", False))


def resource_root() -> Path:
    """Read-only assets bundled with the app."""
    if is_frozen():
        # PyInstaller onedir: sys._MEIPASS is the _internal folder.
        return Path(sys._MEIPASS) / "assets"
    return Path(__file__).resolve().parents[2] / "assets"


def app_root() -> Path:
    """Folder the user considers "the app" - holds the .exe and data/."""
    if is_frozen():
        # Never __file__ or _MEIPASS: both point inside _internal.
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parents[2]


def _probe_writable(candidate: Path) -> bool:
    try:
        candidate.mkdir(parents=True, exist_ok=True)
        token = candidate / ".write-probe"
        token.write_text("ok", encoding="utf-8")
        token.unlink()
        return True
    except OSError:
        return False


def _local_root() -> Path:
    """Per-machine state, deliberately kept out of the data tree.

    The data tree normally lives inside OneDrive, which offers no way to exclude a
    single subfolder from upload and follows junctions through to their target, so
    the only reliable way to keep WebView2's profile off the cloud is to not put it
    in the synced folder at all. That matters because the profile holds whatever the
    page writes to localStorage - an AI API key among it - in plaintext.
    """
    base = os.environ.get("LOCALAPPDATA")
    if not base:
        base = str(Path.home() / "AppData" / "Local")
    return Path(base) / BUNDLE_ID


def _fallback_root() -> Path:
    return _local_root() / "data"


def data_dir() -> Path:
    """Library next to the exe — on the OneDrive Cortex Windows install, that
    is ``OneDrive\\Cortex Windows\\data``.
    """
    primary = app_root() / "data"
    if _probe_writable(primary):
        return primary
    cache = _fallback_root()
    if _probe_writable(cache):
        return cache
    primary.mkdir(parents=True, exist_ok=True)
    return primary


def ensure_data_tree(root: Path | None = None) -> Path:
    root = root or data_dir()
    _adopt_legacy_qbank(root)
    for name in DATA_SUBDIRS:
        (root / name).mkdir(parents=True, exist_ok=True)
    return root


def _adopt_legacy_qbank(root: Path) -> None:
    old, new = root / "quiz", root / "Qbank"
    if not old.is_dir():
        return
    try:
        if not new.exists():
            old.rename(new)
            return
        for item in sorted(old.rglob("*")):
            if item.is_file():
                target = new / item.relative_to(old)
                if not target.exists():
                    target.parent.mkdir(parents=True, exist_ok=True)
                    item.replace(target)
        for item in sorted(old.rglob("*"), reverse=True):
            if item.is_dir():
                item.rmdir()
        old.rmdir()
    except OSError:
        logging.getLogger(__name__).warning("could not move quiz folder to Qbank", exc_info=True)


def files_dir(root: Path | None = None) -> Path:
    return (root or data_dir()) / "files"


def study_dir(root: Path | None = None) -> Path:
    return (root or data_dir()) / "study-data"


def flashcards_dir(root: Path | None = None) -> Path:
    return (root or data_dir()) / "flashcards"


def flashcard_progress_dir(root: Path | None = None) -> Path:
    return performance_dir(root)


def quizzes_dir(root: Path | None = None) -> Path:
    return (root or data_dir()) / "Qbank"


def performance_dir(root: Path | None = None) -> Path:
    return (root or data_dir()) / "performance"


def exports_dir(root: Path | None = None) -> Path:
    return (root or data_dir()) / "exports"


def trash_dir(root: Path | None = None) -> Path:
    return (root or data_dir()) / "trash"


def snapshots_dir(root: Path | None = None) -> Path:
    """The folder shared with the phone's snapshot export."""
    return (root or data_dir()) / SNAPSHOTS_DIRNAME


def snapshots_pack(root: Path | None = None) -> Path:
    """The one file holding every snapshot, written by both apps.

    Not created on demand here: an absent pack is a library that has no phone
    rows yet, which is a normal state and not something to paper over with an
    empty file the user would then see in Explorer.
    """
    return snapshots_dir(root) / SNAPSHOTS_PACK_NAME


# The phone reduces a folder and a file name to these before joining them into a
# path, and the desktop has to reduce them the same way or the two apps would file
# the same note's snapshots under two different names. Kept apart from _safe() in
# posters.py on purpose: that one is this app's own containment rule and is free to
# change, while this is a format shared with another program.
_PATH_UNSAFE = re.compile(r"[\\/:*?\"<>|]")


def _component(value: str, fallback: str) -> str:
    """One path component, reduced to something NTFS will accept.

    The phone reduces a folder by its slashes alone and a file name by the whole
    set, because every folder it files under is a real directory whose name was
    already legal. Both halves get the whole set here instead. A real subject
    folder is a directory on this disk too, so the stricter rule cannot change one
    and the two apps still agree on where a note's snapshots live - but the doc
    reference reaches this function straight from the page, and a colon in it would
    otherwise reach mkdir and raise rather than be filed somewhere harmless.

    Trailing dots and spaces go for the same reason: Windows accepts them in a
    string and then silently resolves the path to a different name.
    """
    cleaned = _PATH_UNSAFE.sub("_", str(value or "")).strip(" .")
    return cleaned or fallback


def folder_key(value: str) -> str:
    """A subject folder's name as it is written into a snapshot path."""
    return _component(value, "Library")


def file_key(value: str) -> str:
    """A note's name as it is written into a snapshot path, without its extension."""
    return _component(value, "Document")


def snapshot_file(folder: str, document: str, root: Path | None = None) -> Path:
    """The one JSON file holding every snapshot of one note.

    A file per note rather than a single pack for the whole library, which is what
    the phone moved to: the pack is rewritten whole on every save, so one shared
    file meant a multi-megabyte write each time a heading was summarised, and two
    notes summarised at once raced for it. Paired with the DOCX by name so a note
    and its snapshots stay recognisable as a pair in Explorer.
    """
    stem = re.sub(r"\.docx$", "", str(document or ""), flags=re.I)
    return snapshots_dir(root) / folder_key(folder) / f"{file_key(stem)}.json"


def ink_dir(root: Path | None = None) -> Path:
    """Handwriting drawn over a note, a snapshot or a page of paper.

    Inside the data tree, unlike the phone, which keeps ink in the store it loses
    on uninstall. Ink is the one thing here nothing can regenerate - a summary can
    be asked for again and audio can be spoken again, but a margin note exists
    only because someone wrote it - so it belongs with the notes, where whatever
    backs the data folder up will take it too.
    """
    return (root or data_dir()) / "ink"


def ink_file(folder: str, document: str, scope: str, root: Path | None = None) -> Path:
    """The one file holding the ink drawn on one surface of one note.

    Laid out like a snapshot file and for the same reason: paired with the DOCX by
    name, so a note and everything drawn on it stay recognisable as a pair in
    Explorer. The scope is part of the file name rather than a folder of its own,
    because a note has only a handful of surfaces and a folder per note per surface
    would be mostly empty directories.
    """
    stem = re.sub(r"\.docx$", "", str(document or ""), flags=re.I)
    return ink_dir(root) / folder_key(folder) / f"{file_key(stem)}__{file_key(scope)}.json"


def pdfs_dir(root: Path | None = None) -> Path:
    """Imported PDFs, either loose or grouped into a folder of their own."""
    return (root or data_dir()) / "PDFs"


def notebooks_dir(root: Path | None = None) -> Path:
    """One folder per notebook, holding its pages and their embedded images."""
    return (root or data_dir()) / "Notebooks"


def paper_dir(root: Path | None = None) -> Path:
    """The indexes listing what is in PDFs and Notebooks, and in what order."""
    return (root or data_dir()) / "paper"


def listen_dir() -> Path:
    """Spoken audio, kept out of the data tree for the reason the profile is.

    Machine-local rather than synced because it is regenerable: a note read aloud
    is tens of megabytes of audio that can be made again from the note itself, and
    the data tree is normally inside OneDrive. Created on demand so a library that
    is never listened to never grows the folder.
    """
    path = _local_root() / "listen"
    path.mkdir(parents=True, exist_ok=True)
    return path


def speech_dir() -> Path:
    """The offline voice and the WAVs it has spoken, likewise machine-local.

    The voice is a 44 MB model that can be fetched again, and the clips beside it
    are regenerated from the notes, so neither belongs in the synced data tree.
    """
    path = _local_root() / "speech"
    path.mkdir(parents=True, exist_ok=True)
    return path


def my_notes_dir(root: Path | None = None) -> Path:
    """Where a newly generated AI note is saved. Created on demand so the first
    save works on a fresh install."""
    path = files_dir(root) / MY_NOTES_SUBJECT
    path.mkdir(parents=True, exist_ok=True)
    return path


def ai_notes_dir(root: Path | None = None) -> Path:
    """The earlier destination for generated notes, still writable so notes already
    saved there can be renamed or deleted. Created on demand."""
    path = files_dir(root) / AI_NOTES_SUBJECT
    path.mkdir(parents=True, exist_ok=True)
    return path


def profile_dir() -> Path:
    """WebView2's user-data folder. Machine-local; _local_root() says why it is not
    inside the data tree. Created on demand so a first run has somewhere to land."""
    path = _local_root() / "app-profile"
    path.mkdir(parents=True, exist_ok=True)
    return path


def extra_profile_dir(pid: int) -> Path:
    """A throwaway WebView2 folder for a second window of the same library.

    WebView2 locks ``app-profile`` exclusively, so another process cannot share it.
    This sits beside that folder, not inside it, and is named for the process that
    owns it so two extra windows cannot collide.
    """
    path = _local_root() / "app-profile-windows" / str(int(pid))
    path.mkdir(parents=True, exist_ok=True)
    return path


def port_file(root: Path | None = None) -> Path:
    """Records the ephemeral port so the running app can be inspected."""
    return (root or data_dir()) / "runtime-port.txt"


def setup_logging(root: Path | None = None) -> Path:
    """Log to a file only.

    In a --windowed build sys.stdout and sys.stderr are None, so any handler
    that writes to a stream - including logging's default lastResort - raises
    on emit. A FileHandler is the only safe sink.

    The log stays in the data tree even though the profile left it: it holds no
    secrets, it is the thing a user sends when something goes wrong, and keying it
    to ``root`` means a --data-dir test run cannot write into the log of the copy
    the user actually runs.
    """
    path = (root or data_dir()) / "cnl-desktop.log"
    path.parent.mkdir(parents=True, exist_ok=True)

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    for handler in list(root_logger.handlers):
        root_logger.removeHandler(handler)

    try:
        handler = logging.FileHandler(path, encoding="utf-8")
    except OSError:
        path = path.with_name(f"cnl-desktop-{os.getpid()}.log")
        handler = logging.FileHandler(path, encoding="utf-8")
    handler.setFormatter(
        logging.Formatter("%(asctime)s %(levelname)-7s %(name)s: %(message)s")
    )
    root_logger.addHandler(handler)
    return path
