"""Restore Normal on non-list paragraphs incorrectly retaining list styles."""
import argparse
from collections import Counter
from copy import copy, deepcopy
import json
from pathlib import Path
import re
import shutil
import time
from zipfile import ZipFile
from lxml import etree as E
from apply_clinical_template import NS, W, list_signature, sha, serialize, signature


def repair(source, destination):
    with ZipFile(source) as z:
        root = E.fromstring(z.read('word/document.xml'))
        styles = E.fromstring(z.read('word/styles.xml'))
        numbers = E.fromstring(z.read('word/numbering.xml')) if 'word/numbering.xml' in z.namelist() else E.Element(f'{{{W}}}numbering')
        before = signature(root)
        original = deepcopy(root)
        lists = list_signature(root, styles, numbers)
        changes = Counter()
        expected = []
        paragraphs = root.findall('.//w:p', NS)
        for index, (paragraph, listing) in enumerate(zip(paragraphs, lists)):
            style = paragraph.find('w:pPr/w:pStyle', NS)
            sid = style.get(f'{{{W}}}val', '') if style is not None else ''
            if listing is not None or not re.search(r'level|list', sid, re.I):
                continue
            style.set(f'{{{W}}}val', 'Normal')
            # Explicit cancellation also prevents inherited list formatting.
            props = paragraph.find('w:pPr', NS)
            num = props.find('w:numPr', NS)
            if num is None:
                num = E.SubElement(props, f'{{{W}}}numPr')
            for item in list(num):
                num.remove(item)
            E.SubElement(num, f'{{{W}}}numId', {f'{{{W}}}val': '0'})
            for name in ('ind', 'tabs'):
                item = props.find('w:' + name, NS)
                if item is not None:
                    props.remove(item)
            expected.append(index)
            changes['table' if paragraph.xpath('ancestor::w:tc', namespaces=NS) else 'body'] += 1
        assert signature(root) == before
        assert list_signature(root, styles, numbers) == lists
        # Every unaffected paragraph, including every actual list, is identical.
        old_paragraphs = original.findall('.//w:p', NS)
        for index, paragraph in enumerate(paragraphs):
            if index not in expected:
                assert E.tostring(paragraph, method='c14n') == E.tostring(old_paragraphs[index], method='c14n')
        result = {'paragraphs': len(lists), 'actualLists': sum(x is not None for x in lists),
                  'actualTableLists': sum(l is not None and bool(p.xpath('ancestor::w:tc', namespaces=NS)) for p, l in zip(paragraphs, lists)),
                  'repaired': dict(changes)}
        if not changes:
            return result
        destination.parent.mkdir(parents=True, exist_ok=True)
        with ZipFile(destination, 'w') as out:
            out.comment = z.comment
            for info in z.infolist():
                out.writestr(copy(info), serialize(root) if info.filename == 'word/document.xml' else z.read(info.filename))
        with ZipFile(destination) as out:
            assert out.testzip() is None
            for name in z.namelist():
                if name != 'word/document.xml':
                    assert z.read(name) == out.read(name)
            assert E.tostring(E.fromstring(out.read('word/document.xml')), method='c14n') == E.tostring(root, method='c14n')
        return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--install', action='store_true')
    parser.add_argument('--install-staged', action='store_true')
    parser.add_argument('--data', type=Path, default=Path(r'C:/Users/ANT-PC/OneDrive/Cortex Windows/data'))
    args = parser.parse_args()
    files = args.data / 'files'
    out = Path(__file__).resolve().parents[1] / 'build/document-list-repair'
    reports = []
    if args.install_staged:
        reports = json.loads((out / 'report.json').read_text(encoding='utf-8'))['files']
        args.install = True
        for r in reports:
            assert sha(files / r['file']) == r['sha256'], r['file']
    for source in ([] if args.install_staged else sorted(files.rglob('*.docx'))):
        relative = source.relative_to(files)
        if source.name.startswith('~$') or any(p.startswith(('_', '.')) for p in relative.parts[:-1]):
            continue
        original_hash = sha(source)
        result = repair(source, out / relative)
        reports.append(dict(file=str(relative), sha256=original_hash, **result))
    changed = [r for r in reports if r['repaired']]
    backup = None
    if args.install and changed:
        backup = args.data / 'backups' / ('document-list-styles-' + str(time.time_ns()) + '.zip')
        with ZipFile(backup, 'x') as z:
            for r in changed:
                source = files / r['file']
                assert sha(source) == r['sha256'], source
                with source.open('r+b'):
                    pass
                z.write(source, r['file'])
        with ZipFile(backup) as z:
            import hashlib
            for r in changed:
                assert hashlib.sha256(z.read(Path(r['file']).as_posix())).hexdigest() == r['sha256']
        written = []
        try:
            for r in changed:
                source = files / r['file']
                assert sha(source) == r['sha256'], source
                written.append(r)
                shutil.copyfile(out / r['file'], source)
                assert sha(source) == sha(out / r['file'])
        except Exception:
            with ZipFile(backup) as z:
                for r in written:
                    (files / r['file']).write_bytes(z.read(Path(r['file']).as_posix()))
            raise
    summary = {'filesChecked': len(reports), 'subjects': len({Path(r['file']).parts[0] for r in reports}),
               'filesRepaired': len(changed), 'paragraphsRepaired': sum(sum(r['repaired'].values()) for r in reports),
               'actualListParagraphsPreserved': sum(r['actualLists'] for r in reports),
               'actualTableListsPreserved': sum(r['actualTableLists'] for r in reports),
               'installed': args.install, 'backup': str(backup) if backup else None}
    out.mkdir(parents=True, exist_ok=True)
    (out / 'report.json').write_text(json.dumps(dict(summary=summary, files=reports), indent=2), encoding='utf-8')
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
