"""Remove redundant numId=0 markers without changing effective Word lists."""
import argparse
from copy import copy
import json
from pathlib import Path
import shutil
from zipfile import ZipFile
from apply_clinical_template import DEFAULT_DATA, ROOT, NS, W, read, xml, val, serialize, signature, list_signature, sha


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--install', action='store_true')
    parser.add_argument('--install-staged', action='store_true')
    args = parser.parse_args()
    folder = DEFAULT_DATA / 'files'
    output = ROOT / 'build/no-list-cleanup'
    output.mkdir(parents=True, exist_ok=True)
    report = json.loads((output / 'report.json').read_text(encoding='utf-8')) if args.install_staged else []
    if args.install_staged:
        args.install = True
        for item in report:
            assert sha(folder / item['file']) == item['before']
            assert sha(output / item['file']) == item['after']
    for source in ([] if args.install_staged else sorted(folder.rglob('*.docx'))):
        relative = source.relative_to(folder)
        if source.name.startswith('~$') or any(p.startswith(('_', '.')) for p in relative.parts[:-1]):
            continue
        data = read(source)
        root = xml(data['word/document.xml'])
        styles = xml(data['word/styles.xml'])
        numbering = xml(data.get('word/numbering.xml', f'<w:numbering xmlns:w="{W}"/>'.encode()))
        before = list_signature(root, styles, numbering)
        content = signature(root)
        definitions = {val(s, 'styleId'): s for s in styles.findall('w:style', NS)}
        changed = 0
        for p in root.findall('.//w:p', NS):
            num = p.find('w:pPr/w:numPr', NS)
            if num is None or val(num.find('w:numId', NS)) != '0':
                continue
            # A cancellation is necessary when a style supplies a list.
            sid = val(p.find('w:pPr/w:pStyle', NS)) or 'Normal'
            seen = set()
            inherited = None
            while sid in definitions and sid not in seen:
                seen.add(sid)
                style = definitions[sid]
                node = style.find('w:pPr/w:numPr/w:numId', NS)
                if node is not None:
                    inherited = val(node)
                    break
                sid = val(style.find('w:basedOn', NS))
            if inherited not in (None, '', '0'):
                continue
            # Do not discard revision metadata or any other numbering property.
            if any(E.tag not in (f'{{{W}}}numId', f'{{{W}}}ilvl') for E in num):
                continue
            num.getparent().remove(num)
            changed += 1
        assert signature(root) == content
        assert list_signature(root, styles, numbering) == before
        if not changed:
            continue
        destination = output / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        with ZipFile(source) as z, ZipFile(destination, 'w') as out:
            out.comment = z.comment
            for info in z.infolist():
                out.writestr(copy(info), serialize(root) if info.filename == 'word/document.xml' else z.read(info.filename))
        verified = read(destination)
        assert all(verified[k] == v for k, v in data.items() if k != 'word/document.xml')
        report.append(dict(file=relative.as_posix(), removed=changed, before=sha(source), after=sha(destination)))
    if args.install and report:
        backup = output / 'backup.zip'
        if backup.exists():
            raise RuntimeError('Backup already exists; retain it and inspect before reinstalling.')
        with ZipFile(backup, 'x') as z:
            for item in report:
                z.write(folder / item['file'], item['file'])
        written = []
        try:
            for item in report:
                source = folder / item['file']
                assert sha(source) == item['before']
                written.append(item)
                shutil.copyfile(output / item['file'], source)
                assert sha(source) == item['after']
        except Exception:
            with ZipFile(backup) as z:
                for item in written:
                    (folder / item['file']).write_bytes(z.read(item['file']))
            raise
    (output / 'report.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps(dict(files=len(report), redundantMarkersRemoved=sum(x['removed'] for x in report), installed=args.install)))


if __name__ == '__main__':
    main()
