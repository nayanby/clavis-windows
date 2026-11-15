"""Standardize main subject Word filenames as N. Topic without editing DOCX bytes."""
import argparse
from collections import Counter
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import re
import time
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = Path(r'C:\Users\ANT-PC\OneDrive\Cortex Windows\data')
PREFIX = re.compile(r'^(?:(?:chapter|chaper|chap|ch)\.?[\s_.-]*)?(\d+|[IVXLCDM]+)[\s_.)-]+(.+)$', re.I)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def split_name(path):
    match = PREFIX.match(path.stem)
    number = None
    title = path.stem
    if match:
        token, title = match.groups()
        if token.isdecimal():
            number = int(token)
        else:
            values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
            value, last = 0, 0
            for char in reversed(token.upper()):
                current = values[char]
                value += -current if current < last else current
                last = current
            number = value
    title = re.sub(r'[_\s]+', ' ', title).strip()
    title = re.sub(r'\s+ORIGINAL$', '', title, flags=re.I).strip()
    assert title and (number is None or number > 0), path
    return number, title


def make_plan(files_root):
    rows = []
    for subject in sorted(files_root.iterdir(), key=lambda p: p.name.casefold()):
        if not subject.is_dir() or subject.name.startswith(('_', '.')):
            continue
        files = sorted((p for p in subject.glob('*.docx') if not p.name.startswith('~$')),
                       key=lambda p: p.name.casefold())
        parsed = [(p, *split_name(p)) for p in files]
        used = {n for p, n, t in parsed if n is not None}
        for path, number, title in parsed:
            if number is None:
                number = max(used, default=0) + 1
                used.add(number)
            target = subject / f'{number}. {title}{path.suffix.lower()}'
            assert path.resolve().is_relative_to(files_root.resolve())
            assert target.resolve().is_relative_to(files_root.resolve())
            rows.append({'old': path, 'new': target, 'subject': subject.name})
        targets = [str(r['new']).casefold() for r in rows if r['subject'] == subject.name]
        assert len(targets) == len(set(targets)), f'Filename collision in {subject.name}'
    old_paths = {str(r['old']).casefold() for r in rows}
    for row in rows:
        if row['new'].exists():
            assert str(row['new']).casefold() in old_paths, f'Destination exists: {row["new"]}'
    return rows


def catalog_update(data, rows):
    path = data / 'study-data/library_catalog.json'
    if not path.exists():
        return None, None, None, 0
    original = path.read_bytes()
    payload = json.loads(original)
    updated = deepcopy(payload)
    changes = {r['old'].relative_to(data / 'files').as_posix().casefold(): r for r in rows}
    count = 0
    for note in updated.get('notes', []):
        relative = str(note.get('path') or f'{note.get("subject", "")}/{note.get("fileName", "")}').replace('\\', '/').lstrip('/')
        if relative.lower().startswith('files/'):
            relative = relative[6:]
        row = changes.get(relative.casefold())
        if row is None or row['old'] == row['new']:
            continue
        note['path'] = row['new'].relative_to(data / 'files').as_posix()
        note['fileName'] = row['new'].name
        note['displayName'] = re.sub(r'^\d+\.\s*', '', row['new'].stem)
        if 'url' in note:
            from urllib.parse import quote
            note['url'] = '/files/' + '/'.join(quote(p) for p in row['new'].relative_to(data / 'files').parts)
        count += 1
    return path, original, updated, count


def main(data, install):
    root = data / 'files'
    rows = make_plan(root)
    changes = [r for r in rows if r['old'].name != r['new'].name]
    catalog, catalog_original, catalog_payload, catalog_count = catalog_update(data, rows)
    report = {'format': '1. Topic Name.docx', 'filesReviewed': len(rows),
              'filesRenamed': len(changes), 'subjectsChanged': dict(Counter(r['subject'] for r in changes)),
              'catalogEntriesUpdated': catalog_count,
              'changes': [{'old': str(r['old'].relative_to(root)), 'new': str(r['new'].relative_to(root))} for r in changes]}
    print(json.dumps({k: v for k, v in report.items() if k != 'changes'}, indent=2))
    if not install:
        for row in changes:
            print(f'{row["subject"]}: {row["old"].name} -> {row["new"].name}')
        return
    hashes = {r['old']: sha(r['old']) for r in rows}
    for row in changes:
        try:
            with row['old'].open('r+b'):
                pass
        except PermissionError as exc:
            raise PermissionError(f'Close the locked Word document: {row["old"]}') from exc
    backup = data / 'backups' / f'subject-filename-standardization-{time.time_ns()}.zip'
    backup.parent.mkdir(parents=True, exist_ok=True)
    manifest = {**report, 'originalHashes': {str(p.relative_to(root)): h for p, h in hashes.items()}}
    with ZipFile(backup, 'x', ZIP_DEFLATED) as z:
        z.writestr('rename-manifest.json', json.dumps(manifest, ensure_ascii=False, indent=2))
        if catalog_count:
            z.writestr('library_catalog.json', catalog_original)
    moved = []
    catalog_written = False
    try:
        for row in changes:
            assert sha(row['old']) == hashes[row['old']], 'Concurrent change'
            assert not row['new'].exists(), row['new']
            row['old'].rename(row['new'])
            moved.append(row)
        for row in rows:
            assert sha(row['new']) == hashes[row['old']], f'Content changed: {row["new"]}'
        if catalog_count:
            assert catalog.read_bytes() == catalog_original, 'Concurrent catalog update'
            catalog_written = True
            catalog.write_text(json.dumps(catalog_payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        assert not [r for r in make_plan(root) if r['old'].name != r['new'].name], 'Nonstandard filenames remain'
    except Exception:
        for row in reversed(moved):
            row['new'].rename(row['old'])
        if catalog_written and catalog.read_bytes() != catalog_original:
            catalog.write_bytes(catalog_original)
        raise
    report.update(installed=True, contentHashesPreserved=len(rows), backup=str(backup))
    destination = ROOT / 'build/subject-filename-standardization.json'
    destination.parent.mkdir(exist_ok=True)
    destination.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Renamed {len(changes)} files; verified {len(rows)} unchanged content hashes. Backup: {backup}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=Path, default=DEFAULT_DATA)
    parser.add_argument('--install', action='store_true')
    args = parser.parse_args()
    main(args.data.resolve(), args.install)
