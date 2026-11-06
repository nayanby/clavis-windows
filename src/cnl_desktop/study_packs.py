"""The library-wide JSON packs shared with the Android app.

Flashcard and quiz packs live in their own data folders; older copies under
study-data are read and merged for compatibility. Reading activity remains under
study-data. These packs are the shared copies OneDrive can carry to the tablet:

  flashcards.json     every deck, keyed the way the phone's library is
  Qbank/<subject>/<NN. chapter>/<NN. topic>/*.json one quiz per file
  performance.json    finished quiz attempts as a flat list of runs
  activity-log.json   heading read/review logs

A write here never replaces data the other app filled: decks, quizzes, runs
and logs are merged by identity so a tablet-only row survives a desktop save.
A missing pack is the normal empty library, not an error.
"""

from __future__ import annotations

import json
import hashlib
import logging
import os
import re
import tempfile
import threading
import time
import zipfile
from datetime import datetime, timezone
from pathlib import Path

from . import paths

log = logging.getLogger("cnl_desktop.study_packs")

FLASH_FILE = "flashcards.json"
FLASH_PROGRESS_FILE = "flashcard-progress.json"
QUIZ_FILE = "quizzes.json"
PERFORMANCE_FILE = "performance.json"
ACTIVITY_FILE = "activity-log.json"

FLASHCARD_SCOPE_PREFIX = "flashcards-"

_LOCK = threading.RLock()
_UNSAFE = re.compile(r"[^a-z0-9]+")
_MAX_QUIZ_QUESTIONS = 200
_MAX_TITLE = 120


def _now_ms() -> int:
    return int(datetime.now().timestamp() * 1000)


def _saved_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def _fold(value: str) -> str:
    """Letters and digits only, so a stray comma or .docx is not a new heading."""
    return _UNSAFE.sub("", str(value or "").casefold())


def _pack_path(study_root: Path, name: str) -> Path:
    root = Path(study_root).resolve()
    if name == FLASH_FILE:
        root = paths.flashcards_dir(root.parent)
    elif name == QUIZ_FILE:
        root = paths.quizzes_dir(root.parent)
    elif name == PERFORMANCE_FILE:
        root = paths.performance_dir(root.parent)
    elif name == FLASH_PROGRESS_FILE:
        root = paths.performance_dir(root.parent)
    return root / name


def _read_json(path: Path):
    if not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        log.exception("corrupt study pack: %s", path)
        return None


def _write_json(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    body = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
    fd, tmp_name = tempfile.mkstemp(dir=str(path.parent), prefix=".tmp-", suffix=".json")
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(body)
            handle.flush()
            os.fsync(handle.fileno())
        for attempt in range(8):
            try:
                os.replace(tmp_name, path)
                break
            except PermissionError:
                if attempt == 7:
                    raise
                time.sleep(0.2 * (attempt + 1))
    except BaseException:
        for attempt in range(5):
            try:
                os.unlink(tmp_name)
                break
            except FileNotFoundError:
                break
            except PermissionError:
                if attempt == 4:
                    log.warning("could not remove temporary study pack %s", tmp_name, exc_info=True)
                else:
                    time.sleep(0.2 * (attempt + 1))
            except OSError:
                log.warning("could not remove temporary study pack %s", tmp_name, exc_info=True)
                break
        raise


def _load(study_root: Path, name: str) -> dict:
    payload = _read_json(_pack_path(study_root, name))
    return payload if isinstance(payload, dict) else {}


def _legacy_load(study_root: Path, name: str) -> dict:
    payload = _read_json(Path(study_root).resolve() / name)
    return payload if isinstance(payload, dict) else {}


def _save(study_root: Path, name: str, payload: dict) -> None:
    _write_json(_pack_path(study_root, name), payload)


def _merge_rows(legacy: list, current: list, key) -> list[dict]:
    merged: dict[str, dict] = {}
    unkeyed: list[dict] = []
    for row in [*legacy, *current]:
        if not isinstance(row, dict):
            continue
        ident = key(row)
        if ident:
            merged[ident] = row
        else:
            unkeyed.append(row)
    return [*merged.values(), *unkeyed]


def _flash_deck_key(deck: dict) -> str:
    key = str(deck.get("key") or "").strip()
    if key:
        return key
    scope = str(deck.get("storageScope") or "")
    document_key = str(deck.get("documentKey") or deck.get("recordKey") or "")
    return flash_key(document_key, scope) if document_key and scope else ""


def _review_stamp(review: dict) -> int:
    try:
        return int(review.get("lastReviewed") or 0)
    except (TypeError, ValueError):
        return 0


def _merge_progress(target: dict, incoming: dict) -> None:
    for deck_key, cards in incoming.items():
        if not isinstance(cards, dict):
            continue
        stored = target.setdefault(str(deck_key), {})
        for card_id, review in cards.items():
            if not card_id or not isinstance(review, dict):
                continue
            current = stored.get(str(card_id))
            if not isinstance(current, dict) or _review_stamp(review) >= _review_stamp(current):
                stored[str(card_id)] = review


def _progress_from_deck(deck: dict) -> dict[str, dict]:
    key = _flash_deck_key(deck)
    data = deck.get("data") if isinstance(deck.get("data"), dict) else {}
    cards = data.get("cards")
    progress: dict[str, dict] = {}
    if not key or not isinstance(cards, list):
        return progress
    for card in cards:
        if not isinstance(card, dict):
            continue
        card_id = str(card.get("id") or "").strip()
        review = card.get("review")
        if card_id and isinstance(review, dict):
            progress[card_id] = review
    return {key: progress} if progress else {}


def _without_progress(deck: dict) -> dict:
    stored = dict(deck)
    data = stored.get("data")
    if not isinstance(data, dict):
        return stored
    clean_data = dict(data)
    cards = clean_data.get("cards")
    if isinstance(cards, list):
        clean_data["cards"] = [
            {key: value for key, value in card.items() if key != "review"}
            if isinstance(card, dict)
            else card
            for card in cards
        ]
    stored["data"] = clean_data
    return stored


def _read_flash_progress(study_root: Path) -> dict[str, dict]:
    payload = _load(study_root, FLASH_PROGRESS_FILE)
    decks = payload.get("decks")
    if not isinstance(decks, dict):
        return {}
    return {
        str(deck_key): {
            str(card_id): review
            for card_id, review in cards.items()
            if isinstance(review, dict)
        }
        for deck_key, cards in decks.items()
        if isinstance(cards, dict)
    }


def _save_flash_progress(study_root: Path, progress: dict[str, dict]) -> None:
    _save(study_root, FLASH_PROGRESS_FILE, {"version": 1, "decks": progress})


def _with_flash_progress(deck: dict, progress: dict[str, dict]) -> dict:
    stored = dict(deck)
    key = _flash_deck_key(stored)
    data = stored.get("data")
    if not key or not isinstance(data, dict) or not isinstance(data.get("cards"), list):
        return stored
    cards = []
    deck_progress = progress.get(key, {})
    for card in data["cards"]:
        if not isinstance(card, dict):
            cards.append(card)
            continue
        enriched = dict(card)
        card_id = str(enriched.get("id") or "").strip()
        review = deck_progress.get(card_id) if card_id else None
        if not isinstance(review, dict):
            review = card.get("review")
        if isinstance(review, dict):
            enriched["review"] = review
        cards.append(enriched)
    enriched_data = dict(data)
    enriched_data["cards"] = cards
    stored["data"] = enriched_data
    return stored


def strip_flash_progress(payload: dict) -> dict:
    return _without_progress(payload)


def apply_flash_progress(
    study_root: Path, doc: str, document_key: str, scope: str, payload: dict
) -> dict:
    deck = dict(payload)
    deck["key"] = flash_key(document_key, scope)
    progress = _read_flash_progress(study_root)
    embedded = _progress_from_deck(deck)
    if embedded:
        _merge_progress(progress, embedded)
        _save_flash_progress(study_root, progress)
    return _with_flash_progress(_without_progress(deck), progress)


def _doc_parts(doc: str) -> tuple[str, str]:
    parts = [p for p in re.split(r"[\\/]+", str(doc or "")) if p not in ("", ".", "..")]
    if not parts:
        return "", ""
    name = re.sub(r"\.docx$", "", parts[-1], flags=re.I)
    folder = parts[-2] if len(parts) > 1 else ""
    return folder, name


def heading_scope(scope: str) -> str:
    scope = str(scope or "").strip()
    if scope.startswith(FLASHCARD_SCOPE_PREFIX):
        return scope[len(FLASHCARD_SCOPE_PREFIX) :]
    return scope


def flash_key(document_key: str, scope: str) -> str:
    return f"{str(document_key or '').strip()}::{heading_scope(scope)}"


def is_flash_scope(scope: str) -> bool:
    return str(scope or "").startswith(FLASHCARD_SCOPE_PREFIX)


# ---- flashcards.json ---------------------------------------------------------

def _flash_context(deck: dict) -> tuple:
    return (_fold(deck.get('folderName', '')), _note_fold(deck.get('documentName', '')),
            heading_scope(deck.get('storageScope') or deck.get('scopeKey') or (deck.get('scope') or {}).get('scopeKey', '')))


def _flash_record_files(study_root: Path) -> list[Path]:
    root = paths.flashcards_dir(Path(study_root).resolve().parent).resolve()
    return [path for path in sorted(root.glob('*/*/*/*.json'))
            if path.relative_to(root).parts[0].lower() != 'backups' and path.resolve().is_relative_to(root)]


def _flash_record_rows(study_root: Path) -> list[tuple[Path, dict]]:
    result = []
    for path in _flash_record_files(study_root):
        deck = _read_json(path)
        if isinstance(deck, dict) and _flash_deck_key(deck) and isinstance(deck.get('data', {}).get('cards'), list):
            deck['chapterOrder'] = _quiz_number(path.parent.parent.name) or 1
            deck['topicOrder'] = _quiz_number(path.parent.name) or 1
            result.append((path, deck))
    return result


def flash_record_path(study_root: Path, deck: dict, existing: dict | None = None) -> Path:
    root = paths.flashcards_dir(Path(study_root).resolve().parent)
    row = {'folder': deck.get('folderName'), 'document': deck.get('documentName'),
           'headingText': deck.get('scopeLabel') or (deck.get('scope') or {}).get('scopeLabel') or deck.get('scopeKey') or 'Cards',
           'chapterOrder': deck.get('chapterOrder'), 'topicOrder': deck.get('topicOrder')}
    return _numbered_record_path(root, row, _flash_deck_key(deck), existing)


def _persist_flash_decks(study_root: Path, decks: list) -> None:
    existing = {_flash_deck_key(deck): path for path, deck in _flash_record_rows(study_root)}
    for deck in decks:
        target = flash_record_path(study_root, deck, existing)
        stored = _without_progress(deck)
        stored['chapterOrder'] = _quiz_number(target.parent.parent.name) or 1
        stored['topicOrder'] = _quiz_number(target.parent.name) or 1
        if _read_json(target) != stored:
            _write_json(target, stored)
        deck['chapterOrder'] = stored['chapterOrder']
        deck['topicOrder'] = stored['topicOrder']
    # Retain the phone-compatible aggregate alongside the individual deck files.
    _save(study_root, FLASH_FILE, {'version': 1, 'decks': [_without_progress(deck) for deck in decks]})


def flash_deck_for_ref(study_root: Path, doc: str, document_key: str, scope: str) -> dict | None:
    folder, name = _doc_parts(doc)
    wanted = flash_key(document_key, scope)
    context = (_fold(folder), _note_fold(name), heading_scope(scope))
    for deck in read_flash_decks(study_root):
        if _flash_deck_key(deck) == wanted or _flash_context(deck) == context:
            return deck
    return None


def _payload_from_deck(deck: dict) -> dict:
    data = deck.get("data") if isinstance(deck.get("data"), dict) else {"cards": []}
    scope = deck.get("scope") if isinstance(deck.get("scope"), dict) else {}
    return {
        "kind": "flashcards",
        "data": data,
        "scope": scope,
        "savedAt": deck.get("savedAt") or _saved_now(),
        "documentKey": str(deck.get("documentKey") or deck.get("recordKey") or ""),
    }


def _deck_from_poster(doc: str, document_key: str, scope: str, payload: dict) -> dict:
    folder, name = _doc_parts(doc)
    data = payload.get("data") if isinstance(payload.get("data"), dict) else {"cards": []}
    scope_obj = payload.get("scope") if isinstance(payload.get("scope"), dict) else {}
    heading = heading_scope(scope)
    if not scope_obj:
        scope_obj = {"scopeKey": heading, "scopeLabel": heading}
    return {
        "key": flash_key(document_key, scope),
        "recordKey": str(document_key or ""),
        "folderName": folder,
        "documentName": name,
        "scopeLabel": str(scope_obj.get("scopeLabel") or heading),
        "data": data,
        "kind": "flashcards",
        "scope": scope_obj,
        "savedAt": payload.get("savedAt") or _saved_now(),
        "documentKey": str(payload.get("documentKey") or document_key or ""),
        "doc": str(doc or ""),
        "storageScope": str(scope or ""),
    }


def read_flash_decks(study_root: Path) -> list[dict]:
    legacy = _legacy_load(study_root, FLASH_FILE).get("decks")
    current = _load(study_root, FLASH_FILE).get("decks")
    rows = _merge_rows(
        legacy if isinstance(legacy, list) else [],
        current if isinstance(current, list) else [],
        lambda deck: str(deck.get("key") or ""),
    )
    rows = _merge_rows(rows, [deck for _, deck in _flash_record_rows(study_root)], _flash_deck_key)
    progress = _read_flash_progress(study_root)
    for deck in rows:
        _merge_progress(progress, _progress_from_deck(deck))
    return [_with_flash_progress(_without_progress(deck), progress) for deck in rows]


def upsert_flash_deck(
    study_root: Path, doc: str, document_key: str, scope: str, payload: dict
) -> None:
    if not is_flash_scope(scope):
        return
    if not isinstance(payload, dict):
        return
    cards = (payload.get("data") or {}).get("cards") if isinstance(payload.get("data"), dict) else None
    if not isinstance(cards, list) or not cards:
        return

    deck = _deck_from_poster(doc, document_key, scope, payload)
    key = deck["key"]
    with _LOCK:
        decks = read_flash_decks(study_root)
        previous = next((row for row in decks if _flash_context(row) == _flash_context(deck)), None)
        if previous:
            deck['key'] = previous['key']
            key = deck['key']
        progress = _read_flash_progress(study_root)
        for stored_deck in decks:
            _merge_progress(progress, _progress_from_deck(stored_deck))
        _merge_progress(progress, _progress_from_deck(deck))
        _save_flash_progress(study_root, progress)
        deck = _without_progress(deck)
        decks = [d for d in decks if str(d.get("key") or "") != key]
        decks.append(_with_flash_progress(deck, progress))
        decks = [_without_progress(row) for row in decks]
        _persist_flash_decks(study_root, decks)


def merge_flash_decks(study_root: Path, incoming: list) -> int:
    """Fold page or tablet decks into flashcards.json by key. Returns how many were new."""
    if not isinstance(incoming, list) or not incoming:
        return 0
    with _LOCK:
        decks = read_flash_decks(study_root)
        progress = _read_flash_progress(study_root)
        for stored_deck in decks:
            _merge_progress(progress, _progress_from_deck(stored_deck))
        by_key = {
            str(deck.get("key") or ""): deck
            for deck in decks
            if str(deck.get("key") or "")
        }
        added = 0
        for deck in incoming:
            if not isinstance(deck, dict):
                continue
            _merge_progress(progress, _progress_from_deck(deck))
            deck = _without_progress(deck)
            key = str(deck.get("key") or "")
            data = deck.get("data") if isinstance(deck.get("data"), dict) else {}
            cards = data.get("cards")
            if not key or not isinstance(cards, list) or not cards:
                continue
            if key not in by_key:
                added += 1
            by_key[key] = deck
        _save_flash_progress(study_root, progress)
        _persist_flash_decks(study_root, list(by_key.values()))
    return added


def drop_flash_deck(study_root: Path, document_key: str, scope: str, deck_key: str | None = None) -> None:
    if not is_flash_scope(scope):
        return
    key = deck_key or flash_key(document_key, scope)
    with _LOCK:
        for path, deck in _flash_record_rows(study_root):
            if _flash_deck_key(deck) == key:
                path.unlink()
        decks = [d for d in read_flash_decks(study_root) if str(d.get("key") or "") != key]
        legacy_path = Path(study_root).resolve() / FLASH_FILE
        current_path = _pack_path(study_root, FLASH_FILE)
        if current_path.is_file() or decks:
            _save(
                study_root,
                FLASH_FILE,
                {"version": 1, "decks": [_without_progress(deck) for deck in decks]},
            )
        legacy = _legacy_load(study_root, FLASH_FILE)
        if legacy_path.is_file() and isinstance(legacy.get("decks"), list):
            legacy["decks"] = [
                deck for deck in legacy["decks"]
                if not isinstance(deck, dict) or str(deck.get("key") or "") != key
            ]
            _write_json(legacy_path, legacy)
        progress = _read_flash_progress(study_root)
        progress.pop(key, None)
        _save_flash_progress(study_root, progress)


def find_flash_payload(
    study_root: Path, doc: str, document_key: str, scope: str
) -> dict | None:
    if not is_flash_scope(scope):
        return None
    want_key = flash_key(document_key, scope)
    heading = heading_scope(scope)
    folder, name = _doc_parts(doc)
    for deck in read_flash_decks(study_root):
        if str(deck.get("key") or "") == want_key:
            return _payload_from_deck(deck)
        stored_scope = str(deck.get("storageScope") or "")
        stored_key = str(deck.get("documentKey") or deck.get("recordKey") or "")
        if stored_scope == scope and stored_key and stored_key == str(document_key or ""):
            return _payload_from_deck(deck)
        if (
            _fold(str(deck.get("folderName") or "")) == _fold(folder)
            and _fold(str(deck.get("documentName") or "")) == _fold(name)
            and heading_scope(stored_scope or str((deck.get("scope") or {}).get("scopeKey") or ""))
            == heading
        ):
            return _payload_from_deck(deck)
    return None


def migrate_flashcard_folders(study_root: Path) -> int:
    """Preserve packs, legacy note decks and scheduler state in numbered deck folders."""
    from . import posters
    with _LOCK:
        study_root = Path(study_root).resolve()
        root = paths.flashcards_dir(study_root.parent).resolve()
        decks = read_flash_decks(study_root)
        by_key = {_flash_deck_key(deck): deck for deck in decks}
        by_context = {_flash_context(deck): deck for deck in decks}
        progress = _read_flash_progress(study_root)
        lookup = {}
        for note in (study_root.parent / 'files').glob('*/*.docx'):
            doc = note.relative_to(study_root.parent / 'files').as_posix()
            resolved = posters._study_dirs(root, doc)
            if resolved:
                lookup[tuple(resolved[1])] = doc
        sources = []
        for store in (study_root, root):
            for path in sorted(store.rglob('*.poster.json')):
                relative = path.relative_to(store)
                if relative.parts[0].lower() == 'backups' or not path.resolve().is_relative_to(store):
                    continue
                payload = _read_json(path)
                if not isinstance(payload, dict) or not isinstance(payload.get('data'), dict) or not isinstance(payload['data'].get('cards'), list):
                    if store == root and '__flashcards-' in path.name:
                        sources.append(path)
                    continue
                if not payload['data']['cards']:
                    continue
                scope_obj = payload.get('scope') or {}
                scope = str(scope_obj.get('scopeKey') or '')
                if not scope:
                    match = re.search(r'__(flashcards-.+)\.poster\.json$', path.name)
                    if not match:
                        continue
                    scope = heading_scope(match[1])
                scope = FLASHCARD_SCOPE_PREFIX + heading_scope(scope)
                known_doc = lookup.get(tuple(relative.parts[:-1]))
                doc = known_doc or '/'.join(relative.parts[:-1]) + '.docx'
                document_key = str(payload.get('documentKey') or path.name.split('__', 1)[0])
                deck = _deck_from_poster(doc, document_key, scope, payload)
                context = _flash_context(deck)
                sources.append(path)
                if context in by_context:
                    deck['key'] = by_context[context]['key']
                elif not known_doc:
                    # Keep retired/backup-note decks recoverable without reviving deleted subjects.
                    continue
                else:
                    by_key[deck['key']] = deck
                    by_context[context] = deck
                _merge_progress(progress, _progress_from_deck(deck))
                alias = flash_key(document_key, scope)
                if alias in progress:
                    _merge_progress(progress, {deck['key']: progress[alias]})
        decks = list(by_key.values())
        groups = {}
        for deck in decks:
            groups.setdefault((deck.get('folderName', ''), deck.get('documentName', '')), []).append(deck)
            _merge_progress(progress, _progress_from_deck(deck))
        for (_, document), topics in sorted(groups.items()):
            used = {deck.get('topicOrder') for deck in topics if deck.get('topicOrder')}
            number = 1
            for deck in sorted(topics, key=lambda row: (int((row.get('scope') or {}).get('headingIndex') or 0), str(row.get('scopeLabel', '')).casefold())):
                if not deck.get('topicOrder'):
                    while number in used:
                        number += 1
                    deck['topicOrder'] = number
                    used.add(number)
                if not deck.get('chapterOrder') and _quiz_number(document):
                    deck['chapterOrder'] = _quiz_number(document)
        if sources:
            backup = root / 'backups' / f'numbered-folders-{time.time_ns()}.zip'
            backup.parent.mkdir(parents=True, exist_ok=True)
            originals = {f'{"study-data" if path.is_relative_to(study_root) else "flashcards"}/{path.relative_to(study_root if path.is_relative_to(study_root) else root).as_posix()}': path.read_bytes()
                         for path in sources}
            for path in (_pack_path(study_root, FLASH_FILE), _pack_path(study_root, FLASH_PROGRESS_FILE)):
                if path.is_file():
                    originals[path.relative_to(study_root.parent).as_posix()] = path.read_bytes()
            with zipfile.ZipFile(backup, 'x', zipfile.ZIP_DEFLATED) as archive:
                for name, body in originals.items():
                    archive.writestr(name, body)
            with zipfile.ZipFile(backup) as archive:
                if any(archive.read(name) != body for name, body in originals.items()):
                    raise OSError('Could not verify the flashcard migration backup.')
        _save_flash_progress(study_root, progress)
        _persist_flash_decks(study_root, decks)
        actual = {_flash_deck_key(deck): deck for _, deck in _flash_record_rows(study_root)}
        for deck in decks:
            if _without_progress(actual.get(deck['key'], {})).get('data') != _without_progress(deck).get('data'):
                raise OSError('Could not verify migrated flashcard content.')
        for path in sources:
            if not (path.resolve().is_relative_to(root) or path.resolve().is_relative_to(study_root)):
                raise OSError('Flashcard source escaped its data folder.')
            path.unlink()
        for path in sources:
            base = root if path.is_relative_to(root) else study_root
            parent = path.parent
            while parent != base and parent.resolve().is_relative_to(base):
                try:
                    parent.rmdir()  # Remove only empty legacy directories, never their contents.
                except OSError:
                    break
                parent = parent.parent
        return len(decks)


# ---- saved quizzes -----------------------------------------------------------


def _quiz_id(folder: str, document: str, heading: str) -> str:
    return "|".join((_fold(folder), _note_fold(document), _fold(heading)))


def _quiz_row_id(row: dict) -> str:
    folder = str(row.get("folder") or "")
    document = str(row.get("document") or "")
    heading = str(row.get("headingText") or "")
    if not any((folder.strip(), document.strip(), heading.strip())):
        return ""
    return _quiz_id(folder, document, heading)


def _note_fold(value: str) -> str:
    """A note's name the way both apps would list it, minus numbering and .docx."""
    stem = re.sub(r"\.docx$", "", str(value or ""), flags=re.I)
    stem = re.sub(r"^\d+[\s._-]*", "", stem)
    return _fold(stem.replace("_", " "))


def _quiz_component(value: str) -> str:
    name = re.sub(r'[<>:"/\\|?*\x00-\x1f]', '-', str(value or 'Untitled'))
    name = re.sub(r'\s+', ' ', name).strip(' .')[:40].rstrip(' .') or 'Untitled'
    if (name.lower() in {'saved', 'backups'} or name.startswith('.')
            or re.fullmatch(r'(?:con|prn|aux|nul|com[1-9]|lpt[1-9])(?:\..*)?', name, re.I)):
        name = '_' + name
    return name


def _quiz_number(value: str) -> int | None:
    match = re.match(r'^\s*(\d+|[IVXLCDM]+)[. _-]+', str(value), re.I)
    if not match:
        return None
    token = match[1].upper()
    if token.isdigit():
        return int(token) or None
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return sum(-roman[c] if i + 1 < len(token) and roman[c] < roman[token[i+1]] else roman[c]
               for i, c in enumerate(token))


def _quiz_label(value: str) -> str:
    return re.sub(r'^\s*(?:\d+|[IVXLCDM]+)[. _-]+', '', str(value), flags=re.I)


def _quiz_record_path(study_root: Path, row: dict, existing: dict | None = None) -> Path:
    root = paths.quizzes_dir(Path(study_root).resolve().parent).resolve()
    identity = _quiz_row_id(row)
    return _numbered_record_path(root, row, identity, existing)


def _numbered_record_path(root: Path, row: dict, identity: str, existing: dict | None = None) -> Path:
    root = root.resolve()
    digest = hashlib.sha256(identity.encode("utf-8")).hexdigest()
    # Keep folders the user has renumbered. Identity stays independent of ordering.
    matches = [existing[identity]] if existing is not None and identity in existing else (
        [*root.glob(f'*/*/*/{digest}.json'), *root.glob(f'*/General/*/*/{digest}.json')]
        if existing is None else [])
    for match in matches:
        if match.resolve().is_relative_to(root) and len(match.relative_to(root).parts) in (4, 5):
            return match
    # General banks use readable filenames. Resolve by stored identity so edits
    # preserve migrated paths and never create a second hashed copy.
    if existing is None and 'questions' in row:
        for match in root.glob('*/General/*/*.json'):
            if match.resolve().is_relative_to(root):
                payload = _read_json(match)
                if isinstance(payload, dict) and _quiz_row_id(payload) == identity:
                    return match
    subject = root / _quiz_component(row.get('folder') or 'Unfiled')
    if row.get('navigationGroup') == 'general':
        subject = subject / 'General'
    chapter_label = _quiz_component(_quiz_label(row.get('document') or 'Note'))
    chapter_number = row.get('chapterOrder') or _quiz_number(row.get('document') or '')
    chapter = next((p for p in sorted(subject.glob('*')) if p.is_dir()
                    and re.match(r'^\d+[. _-]', p.name)
                    and _quiz_label(p.name).casefold() == chapter_label.casefold()), None)
    if chapter is None:
        used = {_quiz_number(p.name) for p in subject.glob('*') if p.is_dir()}
        if not chapter_number:
            chapter_number = max((n for n in used if n), default=0) + 1
        chapter = subject / f'{int(chapter_number):02}. {chapter_label}'
    if row.get('navigationGroup') == 'general':
        destination = chapter / (_quiz_component(_quiz_label(row.get('headingText') or row.get('document') or 'Questions')) + '.json')
        if destination.exists() and _quiz_row_id(_read_json(destination) or {}) != identity:
            destination = chapter / (destination.stem + ' ' + digest[:8] + '.json')
        if not destination.resolve().is_relative_to(root):
            raise ValueError('Quiz chapter folder escaped Qbank.')
        return destination
    topic_label = _quiz_component(row.get('headingText') or 'Untitled')
    topic = next((p for p in sorted(chapter.glob('*')) if p.is_dir()
                  and ((p / f'{digest}.json').is_file() or
                       (_quiz_label(p.name).casefold() == topic_label.casefold() and not any(p.glob('*.json'))))), None)
    if topic is None:
        topic_number = row.get('topicOrder')
        if not isinstance(topic_number, int) or topic_number <= 0:
            used = [_quiz_number(p.name) for p in chapter.glob('*') if p.is_dir()]
            topic_number = max((n for n in used if n), default=0) + 1
        topic = chapter / f'{topic_number:02}. {topic_label}'
        while topic.exists():
            topic_number += 1
            topic = chapter / f'{topic_number:02}. {topic_label}'
    destination = topic / f"{digest}.json"
    if not destination.resolve().is_relative_to(root.resolve()):
        raise ValueError('Quiz topic folder escaped Qbank.')
    return destination


def _quiz_record_files(study_root: Path) -> list[Path]:
    root = paths.quizzes_dir(Path(study_root).resolve().parent).resolve()
    if not root.is_dir():
        return []
    candidates = [path for path in root.rglob('*.json')
                  if (len(path.relative_to(root).parts) in (2, 4)
                      or (len(path.relative_to(root).parts) == 5 and path.relative_to(root).parts[1] == 'General'))
                  and path.relative_to(root).parts[0].lower() != 'backups']
    return sorted((path for path in candidates if path.resolve().is_relative_to(root)),
                  key=lambda p: (len(p.relative_to(root).parts), str(p)))


def _read_quiz_records(study_root: Path) -> list[dict]:
    rows = []
    root = paths.quizzes_dir(Path(study_root).resolve().parent).resolve()
    for path in _quiz_record_files(study_root):
        payload = _read_json(path)
        if isinstance(payload, dict) and _quiz_row_id(payload):
            parts = path.relative_to(root).parts
            if len(parts) in (4, 5) and parts[1] == 'General':
                payload['navigationGroup'] = 'general'
                if len(parts) == 4:
                    payload['chapterOrder'] = _quiz_number(parts[2]) or 1
                    payload['topicOrder'] = payload.get('topicOrder') or 1
                    rows.append(payload)
                    continue
                parts = (parts[0], *parts[2:])
            if len(parts) == 4:
                payload['chapterOrder'] = _quiz_number(parts[1]) or 1
                payload['topicOrder'] = _quiz_number(parts[2]) or 1
            rows.append(payload)
    return rows


def read_quizzes(study_root: Path) -> list[dict]:
    bundled = _read_json(paths.resource_root() / "ini_ss_neurology_quizzes.json")
    built_in = bundled.get("quizzes", []) if isinstance(bundled, dict) else []
    legacy = _legacy_load(study_root, QUIZ_FILE).get("quizzes")
    current = _load(study_root, QUIZ_FILE).get("quizzes")
    return _merge_rows(
        [
            *built_in,
            *(legacy if isinstance(legacy, list) else []),
            *(current if isinstance(current, list) else []),
        ],
        _read_quiz_records(study_root),
        _quiz_row_id,
    )


def migrate_saved_quizzes(study_root: Path) -> int:
    """Migrate quiz packs and flat records to topic folders, verifying before cleanup."""
    with _LOCK:
        sources = [(path, _read_json(path)) for path in _quiz_record_files(study_root)]
        rows = read_quizzes(study_root)
        groups = {}
        for row in rows:
            groups.setdefault((row.get('folder', ''), row.get('document', '')), []).append(row)
        for (subject, document), topics in sorted(groups.items()):
            used = {row.get('topicOrder') for row in topics if row.get('topicOrder')}
            next_number = 1
            for row in sorted(topics, key=lambda r: (r.get('headingIndex', 0), str(r.get('headingText', '')).casefold())):
                if not row.get('topicOrder'):
                    while next_number in used:
                        next_number += 1
                    row['topicOrder'] = next_number
                    used.add(next_number)
                if not row.get('chapterOrder') and _quiz_number(document):
                    row['chapterOrder'] = _quiz_number(document)
        root = paths.quizzes_dir(Path(study_root).resolve().parent).resolve()
        existing = {_quiz_row_id(payload): path for path, payload in sources
                    if isinstance(payload, dict) and len(path.relative_to(root).parts) in (4, 5)}
        destinations = []
        for row in rows:
            destination = _quiz_record_path(study_root, row, existing)
            flat_general = len(destination.relative_to(root).parts) == 4 and destination.relative_to(root).parts[1] == 'General'
            row['chapterOrder'] = _quiz_number(destination.parent.name if flat_general else destination.parent.parent.name) or 1
            row['topicOrder'] = (row.get('topicOrder') or 1) if flat_general else (_quiz_number(destination.parent.name) or 1)
            if not destination.is_file() or _read_json(destination) != row:
                _write_json(destination, row)
            destinations.append((destination, row))
        if any(_read_json(path) != row for path, row in destinations):
            raise OSError("Could not verify all saved-quiz files; keeping the source pack.")

        canonical = {_quiz_row_id(row): path.resolve() for path, row in destinations}
        obsolete = [path for path, payload in sources if isinstance(payload, dict)
                    and _quiz_row_id(payload) in canonical
                    and path.resolve() != canonical[_quiz_row_id(payload)]]
        if obsolete:
            root = paths.quizzes_dir(Path(study_root).resolve().parent).resolve()
            backup = root / 'backups' / f'topic-folders-{time.time_ns()}.zip'
            backup.parent.mkdir(parents=True, exist_ok=True)
            with zipfile.ZipFile(backup, 'x', zipfile.ZIP_DEFLATED) as archive:
                for path in obsolete:
                    archive.write(path, path.relative_to(root).as_posix())
            with zipfile.ZipFile(backup) as archive:
                if any(archive.read(path.relative_to(root).as_posix()) != path.read_bytes() for path in obsolete):
                    raise OSError('Could not verify the topic-folder migration backup.')
            for path in obsolete:
                if not path.resolve().is_relative_to(root):
                    raise OSError('Quiz source escaped the Qbank folder.')
                path.unlink()

        for source in (
            Path(study_root).resolve() / QUIZ_FILE,
            _pack_path(study_root, QUIZ_FILE),
        ):
            if source.is_file():
                source.unlink()
        return len(destinations)


def find_saved_quiz(
    study_root: Path, folder: str, document: str, heading: str
) -> dict | None:
    wanted = _quiz_id(folder, document, heading)
    if not wanted.strip("|"):
        return None
    for row in read_quizzes(study_root):
        if _quiz_id(str(row.get("folder") or ""), str(row.get("document") or ""), str(row.get("headingText") or "")) == wanted:
            questions = row.get("questions")
            if isinstance(questions, list) and questions:
                return row
    return None


def upsert_saved_quiz(study_root: Path, row: dict) -> dict | None:
    folder = str(row.get("folder") or "").strip()
    document = str(row.get("document") or "").strip()
    heading = str(row.get("headingText") or "").strip()
    questions = row.get("questions")
    if not heading or not isinstance(questions, list) or not questions:
        return None
    if len(questions) > _MAX_QUIZ_QUESTIONS:
        questions = questions[:_MAX_QUIZ_QUESTIONS]

    index = row.get("headingIndex")
    heading_index = index if isinstance(index, int) and not isinstance(index, bool) and index >= 0 else 0
    made = row.get("madeAt")
    made_at = int(made) if isinstance(made, int) and made > 0 else _now_ms()

    stored = {
        "folder": folder,
        "document": re.sub(r"\.docx$", "", document, flags=re.I),
        "headingIndex": heading_index,
        "headingText": heading[:_MAX_TITLE],
        "questions": questions,
        "madeAt": made_at,
    }
    with _LOCK:
        destination = _quiz_record_path(study_root, {**stored, 'chapterOrder': row.get('chapterOrder'),
            'topicOrder': row.get('topicOrder'), 'navigationGroup': row.get('navigationGroup')})
        if 'General' == destination.relative_to(paths.quizzes_dir(Path(study_root).resolve().parent).resolve()).parts[1]:
            stored['navigationGroup'] = 'general'
        flat_general = len(destination.relative_to(paths.quizzes_dir(Path(study_root).resolve().parent)).parts) == 4 and stored.get('navigationGroup') == 'general'
        stored['chapterOrder'] = _quiz_number(destination.parent.name if flat_general else destination.parent.parent.name) or 1
        stored['topicOrder'] = (row.get('topicOrder') or 1) if flat_general else (_quiz_number(destination.parent.name) or 1)
        _write_json(destination, stored)
        for source in (
            Path(study_root).resolve() / QUIZ_FILE,
            _pack_path(study_root, QUIZ_FILE),
        ):
            payload = _read_json(source)
            if not isinstance(payload, dict) or not isinstance(payload.get("quizzes"), list):
                continue
            identity = _quiz_row_id(stored)
            remaining = [
                item
                for item in payload["quizzes"]
                if not isinstance(item, dict) or _quiz_row_id(item) != identity
            ]
            if remaining:
                payload["quizzes"] = remaining
                _write_json(source, payload)
            else:
                source.unlink(missing_ok=True)
    return stored


# ---- performance.json --------------------------------------------------------


def _run_id(ran_at, correct, total, label: str) -> str:
    return f"{int(ran_at)}|{int(correct)}|{int(total)}|{label}"


def _run_row_id(row: dict) -> str:
    try:
        ran_at = int(row.get("ranAt") or 0)
        correct = int(row.get("correct") or 0)
        total = int(row.get("total") or 0)
    except (TypeError, ValueError):
        return ""
    if ran_at < 1 or total < 1 or correct < 0 or correct > total:
        return ""
    return _run_id(ran_at, correct, total, str(row.get("label") or ""))


def read_runs(study_root: Path) -> list[dict]:
    legacy = _legacy_load(study_root, PERFORMANCE_FILE).get("runs")
    current = _load(study_root, PERFORMANCE_FILE).get("runs")
    rows = _merge_rows(
        legacy if isinstance(legacy, list) else [],
        current if isinstance(current, list) else [],
        _run_row_id,
    )
    out = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        try:
            ran_at = int(row.get("ranAt") or 0)
            correct = int(row.get("correct") or 0)
            total = int(row.get("total") or 0)
        except (TypeError, ValueError):
            continue
        if total < 1 or correct < 0 or correct > total:
            continue
        out.append(
            {
                "ranAt": ran_at,
                "correct": correct,
                "total": total,
                "label": str(row.get("label") or ""),
            }
        )
    return out


def append_run(
    study_root: Path, ran_at: int, correct: int, total: int, label: str
) -> None:
    label = str(label or "").strip()[:_MAX_TITLE]
    ident = _run_id(ran_at, correct, total, label)
    with _LOCK:
        runs = read_runs(study_root)
        if any(_run_id(r["ranAt"], r["correct"], r["total"], r["label"]) == ident for r in runs):
            return
        runs.append(
            {"ranAt": int(ran_at), "correct": int(correct), "total": int(total), "label": label}
        )
        _save(study_root, PERFORMANCE_FILE, {"version": 1, "runs": runs})


# ---- activity-log.json -------------------------------------------------------


def _activity_id(doc: str, document_key: str) -> str:
    key = str(document_key or "").strip()
    if key:
        return f"key:{key}"
    return f"doc:{_fold(doc)}"


def read_activity_logs(study_root: Path) -> list[dict]:
    pack = _load(study_root, ACTIVITY_FILE)
    logs = pack.get("logs")
    rows = [r for r in logs if isinstance(r, dict)] if isinstance(logs, list) else []
    if rows:
        return rows
    payload = pack.get("payload")
    if isinstance(payload, dict):
        return [
            {
                "key": str(pack.get("key") or ""),
                "savedAt": pack.get("savedAt"),
                "payload": payload,
                "doc": "",
                "documentKey": str(payload.get("documentKey") or ""),
            }
        ]
    return []


def upsert_activity(
    study_root: Path, doc: str, document_key: str, payload: dict, key: str = ""
) -> None:
    if not isinstance(payload, dict):
        return
    ident = _activity_id(doc, document_key)
    row = {
        "key": key or f"{document_key}::heading-activity-log",
        "savedAt": payload.get("updatedAt") or payload.get("savedAt") or _saved_now(),
        "payload": payload,
        "doc": str(doc or ""),
        "documentKey": str(document_key or payload.get("documentKey") or ""),
    }
    with _LOCK:
        logs = [
            item
            for item in read_activity_logs(study_root)
            if _activity_id(str(item.get("doc") or ""), str(item.get("documentKey") or "")) != ident
        ]
        logs.append(row)
        _save(
            study_root,
            ACTIVITY_FILE,
            {
                "version": 1,
                "key": row["key"],
                "savedAt": row["savedAt"],
                "payload": payload,
                "logs": logs,
            },
        )


def drop_activity(study_root: Path, doc: str, document_key: str) -> None:
    ident = _activity_id(doc, document_key)
    with _LOCK:
        logs = [
            item
            for item in read_activity_logs(study_root)
            if _activity_id(str(item.get("doc") or ""), str(item.get("documentKey") or "")) != ident
        ]
        path = _pack_path(study_root, ACTIVITY_FILE)
        if not path.is_file() and not logs:
            return
        latest = logs[-1] if logs else None
        _save(
            study_root,
            ACTIVITY_FILE,
            {
                "version": 1,
                "key": (latest or {}).get("key") or "library::heading-activity-log",
                "savedAt": (latest or {}).get("savedAt") or _saved_now(),
                "payload": (latest or {}).get("payload") or {},
                "logs": logs,
            },
        )


def find_activity(study_root: Path, doc: str, document_key: str) -> dict | None:
    ident = _activity_id(doc, document_key)
    folder, name = _doc_parts(doc)
    for item in read_activity_logs(study_root):
        if _activity_id(str(item.get("doc") or ""), str(item.get("documentKey") or "")) == ident:
            payload = item.get("payload")
            return payload if isinstance(payload, dict) else None
        payload = item.get("payload") if isinstance(item.get("payload"), dict) else {}
        if document_key and str(payload.get("documentKey") or item.get("documentKey") or "") == str(document_key):
            return payload
        item_folder, item_name = _doc_parts(str(item.get("doc") or ""))
        if folder and name and _fold(item_folder) == _fold(folder) and _fold(item_name) == _fold(name):
            return payload if isinstance(payload, dict) else None
    return None
