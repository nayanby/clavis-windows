"""Remove opening Title paragraphs and the synthetic Introduction preceding them."""
import argparse
from copy import copy
import hashlib
import json
from pathlib import Path
import shutil
import time
from zipfile import ZipFile
from lxml import etree as E

NS = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def clean(source, destination):
    with ZipFile(source) as z:
        data = z.read('word/document.xml')
        root = E.fromstring(data)
        body = root.find('w:body', NS)
        opening = []
        for node in body:
            text = ''.join(node.xpath('.//w:t/text()', namespaces=NS)).strip()
            if not text:
                if node.xpath('.//w:drawing|.//w:pict|self::w:tbl', namespaces=NS):
                    break
                continue
            opening.append(node)
            if len(opening) == 3:
                break
        removed = []
        for i, node in enumerate(opening):
            style = node.xpath('string(w:pPr/w:pStyle/@w:val)', namespaces=NS)
            if style.casefold() != 'title' or i > 1:
                continue
            if i == 1:
                if ''.join(opening[0].xpath('.//w:t/text()', namespaces=NS)).strip() != 'Introduction':
                    continue
                removed.append(opening[0])
            removed.append(node)
            break
        if not removed:
            return None
        for node in removed:
            assert not node.xpath('.//w:drawing|.//w:pict|.//w:object|.//w:sectPr', namespaces=NS)
            body.remove(node)
        expected = E.tostring(root, method='c14n')
        replacement = E.tostring(root, encoding='UTF-8', xml_declaration=True, standalone=True)
        destination.parent.mkdir(parents=True, exist_ok=True)
        with ZipFile(destination, 'w') as out:
            out.comment = z.comment
            for info in z.infolist():
                out.writestr(copy(info), replacement if info.filename == 'word/document.xml' else z.read(info.filename))
        with ZipFile(destination) as out:
            assert out.testzip() is None
            assert out.namelist() == z.namelist()
            for name in z.namelist():
                if name != 'word/document.xml':
                    assert out.read(name) == z.read(name)
            assert E.tostring(E.fromstring(out.read('word/document.xml')), method='c14n') == expected
        return [''.join(n.xpath('.//w:t/text()', namespaces=NS)) for n in removed]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=Path, default=Path(r'C:/Users/ANT-PC/OneDrive/Cortex Windows/data'))
    parser.add_argument('--install', action='store_true')
    args = parser.parse_args()
    files = args.data / 'files'
    output = Path(__file__).resolve().parents[1] / 'build/remove-opening-titles'
    changes = []
    for source in sorted(files.glob('*/*.docx')):
        if source.name.startswith('~$'):
            continue
        relative = source.relative_to(files)
        before = digest(source)
        removed = clean(source, output / relative)
        if removed:
            changes.append({'file': str(relative), 'sha256': before, 'removed': removed})
    if args.install and changes:
        backup = args.data / 'backups' / ('opening-titles-' + str(time.time_ns()) + '.zip')
        with ZipFile(backup, 'x') as z:
            for row in changes:
                source = files / row['file']
                assert digest(source) == row['sha256'], source
                with source.open('r+b'):
                    pass
                z.write(source, row['file'])
        for row in changes:
            source = files / row['file']
            assert digest(source) == row['sha256'], source
            shutil.copyfile(output / row['file'], source)
            assert digest(source) == digest(output / row['file'])
        print('Backup:', backup)
    output.mkdir(parents=True, exist_ok=True)
    (output / 'report.json').write_text(json.dumps(changes, ensure_ascii=False, indent=2), encoding='utf-8')
    print('Changed files:', len(changes), 'Installed:', args.install)


if __name__ == '__main__':
    main()
