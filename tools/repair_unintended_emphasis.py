"""Undo automatic Subtle Emphasis conversions using pre-palette run evidence."""
import argparse
from collections import Counter
from copy import copy, deepcopy
from difflib import SequenceMatcher
import hashlib
import io
import json
from pathlib import Path
import re
import shutil
import time
from zipfile import ZipFile
from lxml import etree as E
from apply_clinical_template import NS, W, signature, list_signature, serialize, sha, order_properties

PROPERTIES = {'b', 'bCs', 'i', 'iCs', 'u', 'strike', 'dstrike', 'caps', 'smallCaps', 'color', 'highlight', 'shd'}


def text(node):
    return ''.join(node.xpath('.//w:t/text()', namespaces=NS))


def propval(node):
    return node.get(f'{{{W}}}val', '') if node is not None else ''


def original_properties(run, styles):
    result = {}
    def inherit(sid, seen):
        if not sid or sid in seen or sid not in styles:
            return
        seen.add(sid)
        style = styles[sid]
        inherit(propval(style.find('w:basedOn', NS)), seen)
        props = style.find('w:rPr', NS)
        if props is not None:
            result.update({E.QName(n).localname: deepcopy(n) for n in props if E.QName(n).localname in PROPERTIES})
    props = run.find('w:rPr', NS)
    if props is not None:
        inherit(propval(props.find('w:rStyle', NS)), set())
        result.update({E.QName(n).localname: deepcopy(n) for n in props if E.QName(n).localname in PROPERTIES})
    return result


def stage(data, output):
    backup = next((data / 'backups').glob('style-palette-before-edit-*.zip'))
    reports = []
    with ZipFile(backup) as historical:
        global_paragraphs = {}
        for name in historical.namelist():
            if not name.endswith('.docx'):
                continue
            with ZipFile(io.BytesIO(historical.read(name))) as z:
                doc = E.fromstring(z.read('word/document.xml'))
                definitions = {s.get(f'{{{W}}}styleId'): s for s in E.fromstring(z.read('word/styles.xml')).findall('w:style', NS)}
                for paragraph in doc.findall('.//w:p', NS):
                    key = text(paragraph)
                    if not key.strip():
                        continue
                    global_paragraphs[key] = None if key in global_paragraphs else (paragraph, definitions)
        for source in sorted((data / 'files').rglob('*.docx')):
            relative = source.relative_to(data / 'files')
            if source.name.startswith('~$') or any(p.startswith(('_', '.')) for p in relative.parts[:-1]):
                continue
            original_hash = sha(source)
            old = None
            old_styles = {}
            if relative.as_posix() in historical.namelist():
                with ZipFile(io.BytesIO(historical.read(relative.as_posix()))) as z:
                    old = E.fromstring(z.read('word/document.xml'))
                    old_styles = {s.get(f'{{{W}}}styleId'): s for s in E.fromstring(z.read('word/styles.xml')).findall('w:style', NS)}
            with ZipFile(source) as z:
                root = E.fromstring(z.read('word/document.xml'))
                styles = E.fromstring(z.read('word/styles.xml'))
                numbering = E.fromstring(z.read('word/numbering.xml')) if 'word/numbering.xml' in z.namelist() else E.Element(f'{{{W}}}numbering')
                before = signature(root)
                lists = list_signature(root, styles, numbering)
                paragraphs = root.findall('.//w:p', NS)
                matches = {}
                if old is not None:
                    old_ps = old.findall('.//w:p', NS)
                    for block in SequenceMatcher(None, [text(p) for p in old_ps], [text(p) for p in paragraphs], autojunk=False).get_matching_blocks():
                        for i in range(block.size):
                            a, b = old_ps[block.a+i].findall('.//w:r', NS), paragraphs[block.b+i].findall('.//w:r', NS)
                            for runs in SequenceMatcher(None, [text(r) for r in a], [text(r) for r in b], autojunk=False).get_matching_blocks():
                                for j in range(runs.size):
                                    matches[b[runs.b+j]] = (a[runs.a+j], old_styles)
                # Chapters have also been renamed and redistributed since the backup.
                # Unique, identical paragraphs supply evidence across those moves.
                for p in paragraphs:
                    reference = global_paragraphs.get(text(p))
                    if reference is None:
                        continue
                    old_p, definitions = reference
                    a, b = old_p.findall('.//w:r', NS), p.findall('.//w:r', NS)
                    if [text(r) for r in a] == [text(r) for r in b]:
                        for previous, current in zip(a, b):
                            matches.setdefault(current, (previous, definitions))
                counts = Counter()
                for p in paragraphs:
                    sid = propval(p.find('w:pPr/w:pStyle', NS))
                    heading = bool(re.search(r'heading|boldside', sid, re.I)) or sid == 'Title'
                    for run in p.findall('.//w:r', NS):
                        props = run.find('w:rPr', NS)
                        if props is None:
                            continue
                        style = props.find('w:rStyle', NS)
                        if propval(style) != 'SubtleEmphasis':
                            continue
                        if heading:
                            props.remove(style)
                            counts['headingRuns'] += 1
                        elif run in matches:
                            previous, previous_styles = matches[run]
                            previous_sid = propval(previous.find('w:rPr/w:rStyle', NS))
                            # Keep deliberate emphasis styles and hyperlink formatting.
                            if re.search(r'subtleemphasis|hyperlink', previous_sid, re.I):
                                counts['deliberatePreserved'] += 1
                                continue
                            props.remove(style)
                            restored = original_properties(previous, previous_styles)
                            for n in list(props):
                                if E.QName(n).localname in PROPERTIES:
                                    props.remove(n)
                            for n in restored.values():
                                props.append(n)
                            counts['restoredRuns'] += 1
                        else:
                            counts['unmatchedPreserved'] += 1
                changed = bool(counts['headingRuns'] or counts['restoredRuns'])
                if changed:
                    order_properties(root)
                    assert signature(root) == before
                    assert list_signature(root, styles, numbering) == lists
                    destination = output / relative
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    replacement = serialize(root)
                    with ZipFile(destination, 'w') as out:
                        out.comment = z.comment
                        for info in z.infolist():
                            out.writestr(copy(info), replacement if info.filename == 'word/document.xml' else z.read(info.filename))
                    with ZipFile(destination) as out:
                        assert out.testzip() is None
                        for name in z.namelist():
                            if name != 'word/document.xml':
                                assert out.read(name) == z.read(name)
                        assert out.read('word/document.xml') == replacement
                reports.append(dict(file=relative.as_posix(), before=original_hash, changed=changed, counts=dict(counts),
                                    staged=sha(output / relative) if changed else None))
    output.mkdir(parents=True, exist_ok=True)
    (output / 'report.json').write_text(json.dumps(reports, indent=2), encoding='utf-8')
    return reports


def install(data, output):
    reports = json.loads((output / 'report.json').read_text(encoding='utf-8'))
    changed = [r for r in reports if r['changed']]
    backup = data / 'backups' / ('emphasis-repair-' + str(time.time_ns()) + '.zip')
    for r in changed:
        source = data / 'files' / r['file']
        assert sha(source) == r['before'], source
        assert sha(output / r['file']) == r['staged']
        with source.open('r+b'):
            pass
    with ZipFile(backup, 'x') as z:
        for r in changed:
            z.write(data / 'files' / r['file'], r['file'])
    with ZipFile(backup) as z:
        for r in changed:
            assert hashlib.sha256(z.read(r['file'])).hexdigest() == r['before']
    written = []
    try:
        for r in changed:
            source = data / 'files' / r['file']
            assert sha(source) == r['before']
            written.append(r)
            shutil.copyfile(output / r['file'], source)
            assert sha(source) == r['staged']
    except Exception:
        with ZipFile(backup) as z:
            for r in written:
                (data / 'files' / r['file']).write_bytes(z.read(r['file']))
        raise
    print('Backup:', backup)
    return reports


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--install-staged', action='store_true')
    args = parser.parse_args()
    data = Path(r'C:/Users/ANT-PC/OneDrive/Cortex Windows/data')
    output = Path(__file__).resolve().parents[1] / 'build/emphasis-repair'
    reports = install(data, output) if args.install_staged else stage(data, output)
    totals = Counter()
    for r in reports:
        totals.update(r['counts'])
    print(json.dumps(dict(filesChecked=len(reports), filesChanged=sum(r['changed'] for r in reports), counts=dict(totals)), indent=2))
