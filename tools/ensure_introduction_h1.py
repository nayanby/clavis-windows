"""Prepend Introduction as native Heading 1 when a subject DOCX lacks an opening H1.

Retain every existing body element and every unrelated package member unchanged.
Empty .docx placeholders become valid Word documents with Introduction only.
"""
import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import re
import shutil
import time
from zipfile import ZipFile

from docx import Document
from docx.shared import RGBColor
from lxml import etree as E

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = Path(r'C:\Users\ANT-PC\OneDrive\Cortex Windows\data')
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
NS = {'w': W}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def first_content(body):
    for node in body:
        text = ''.join(node.xpath('.//w:t/text()', namespaces=NS)).strip()
        visible = node.xpath('.//w:drawing | .//w:pict | .//w:object | self::w:tbl', namespaces=NS)
        if text or visible:
            return node
    return None


def is_h1(node, styles):
    if node is None or node.tag != f'{{{W}}}p':
        return False
    pr = node.find('w:pPr', NS)
    if pr is None:
        return False
    level = pr.find('w:outlineLvl', NS)
    if level is not None:
        return level.get(f'{{{W}}}val') == '0'
    ps = pr.find('w:pStyle', NS)
    sid = ps.get(f'{{{W}}}val') if ps is not None else ''
    stylemap = {n.get(f'{{{W}}}styleId'): n for n in styles.findall('w:style', NS)}
    visited = set()
    while sid and sid not in visited:
        visited.add(sid)
        style = stylemap.get(sid)
        if style is None:
            return False
        level = style.find('w:pPr/w:outlineLvl', NS)
        if level is not None:
            return level.get(f'{{{W}}}val') == '0'
        name = style.find('w:name', NS)
        if re.search(r'heading\s*1$', sid, re.I) or (
                name is not None and re.search(r'heading\s*1$', name.get(f'{{{W}}}val', ''), re.I)):
            return True
        base = style.find('w:basedOn', NS)
        sid = base.get(f'{{{W}}}val') if base is not None else ''
    return False


def introduction():
    paragraph = E.Element(f'{{{W}}}p')
    pr = E.SubElement(paragraph, f'{{{W}}}pPr')
    E.SubElement(pr, f'{{{W}}}pStyle', {f'{{{W}}}val': 'Heading1'})
    E.SubElement(pr, f'{{{W}}}keepNext')
    E.SubElement(pr, f'{{{W}}}outlineLvl', {f'{{{W}}}val': '0'})
    run = E.SubElement(paragraph, f'{{{W}}}r')
    props = E.SubElement(run, f'{{{W}}}rPr')
    E.SubElement(props, f'{{{W}}}color', {f'{{{W}}}val': '000000'})
    E.SubElement(run, f'{{{W}}}t').text = 'Introduction'
    return paragraph


def ensure_style(styles):
    if styles.xpath('./w:style[@w:styleId="Heading1"]', namespaces=NS):
        return False
    style = E.SubElement(styles, f'{{{W}}}style', {f'{{{W}}}type': 'paragraph', f'{{{W}}}styleId': 'Heading1'})
    E.SubElement(style, f'{{{W}}}name', {f'{{{W}}}val': 'heading 1'})
    if styles.xpath('./w:style[@w:styleId="Normal"]', namespaces=NS):
        E.SubElement(style, f'{{{W}}}basedOn', {f'{{{W}}}val': 'Normal'})
        E.SubElement(style, f'{{{W}}}next', {f'{{{W}}}val': 'Normal'})
    E.SubElement(style, f'{{{W}}}qFormat')
    pr = E.SubElement(style, f'{{{W}}}pPr')
    E.SubElement(pr, f'{{{W}}}keepNext')
    E.SubElement(pr, f'{{{W}}}outlineLvl', {f'{{{W}}}val': '0'})
    props = E.SubElement(style, f'{{{W}}}rPr')
    E.SubElement(props, f'{{{W}}}b')
    E.SubElement(props, f'{{{W}}}sz', {f'{{{W}}}val': '28'})
    E.SubElement(props, f'{{{W}}}color', {f'{{{W}}}val': '000000'})
    return True


def package(path):
    with ZipFile(path) as z:
        assert z.testzip() is None
        return {n: z.read(n) for n in z.namelist()}


def has_opening_h1(path):
    data = package(path)
    root = E.fromstring(data['word/document.xml'])
    styles = E.fromstring(data['word/styles.xml'])
    return is_h1(first_content(root.find('w:body', NS)), styles)


def add_heading(source, destination):
    if source.stat().st_size == 0:
        doc = Document()
        p = doc.add_paragraph('Introduction', style='Heading 1')
        p.runs[0].font.color.rgb = RGBColor(0, 0, 0)
        doc.save(destination)
        assert has_opening_h1(destination)
        return 'emptyPlaceholder'
    data = package(source)
    root = E.fromstring(data['word/document.xml'])
    styles = E.fromstring(data['word/styles.xml'])
    body = root.find('w:body', NS)
    if is_h1(first_content(body), styles):
        return None
    original_root = deepcopy(root)
    body.insert(0, introduction())
    replacement = {'word/document.xml': E.tostring(root, encoding='UTF-8', xml_declaration=True, standalone=True)}
    if ensure_style(styles):
        replacement['word/styles.xml'] = E.tostring(styles, encoding='UTF-8', xml_declaration=True, standalone=True)
    with ZipFile(source) as old, ZipFile(destination, 'w') as new:
        new.comment = old.comment
        for info in old.infolist():
            new.writestr(info, replacement.get(info.filename, data[info.filename]))
    after = package(destination)
    assert set(after) == set(data)
    assert all(after[n] == b for n, b in data.items() if n not in replacement)
    checked_root = E.fromstring(after['word/document.xml'])
    checked_body = checked_root.find('w:body', NS)
    assert ''.join(checked_body[0].xpath('.//w:t/text()', namespaces=NS)) == 'Introduction'
    assert is_h1(checked_body[0], E.fromstring(after['word/styles.xml']))
    checked_body.remove(checked_body[0])
    assert E.tostring(checked_root, method='c14n') == E.tostring(original_root, method='c14n'), source
    return 'prependedIntroduction'


def run(data, output, install):
    files_root = data / 'files'
    files = sorted(p for subject in files_root.iterdir()
                   if subject.is_dir() and not subject.name.startswith(('_', '.'))
                   for p in subject.glob('*.docx') if not p.name.startswith('~$'))
    output.mkdir(parents=True, exist_ok=True)
    changed, unchanged, hashes = [], [], {}
    for source in files:
        relative = source.relative_to(files_root)
        hashes[source] = sha(source)
        destination = output / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        action = add_heading(source, destination)
        if action:
            changed.append((source, destination, action))
        else:
            unchanged.append(source)
    report = {'filesChecked': len(files), 'introductionAdded': len(changed),
              'alreadyStartsWithH1': len(unchanged),
              'emptyPlaceholdersRepaired': [str(p.relative_to(files_root)) for p, _, a in changed if a == 'emptyPlaceholder'],
              'changedFiles': [str(p.relative_to(files_root)) for p, _, _ in changed],
              'originalBodyAndOtherPackageMembersPreserved': True,
              'visualQA': 'Not completed: LibreOffice renderer is unavailable.'}
    print(json.dumps({k: v for k, v in report.items() if k != 'changedFiles'}, indent=2), flush=True)
    if install:
        for source, _, _ in changed:
            assert source.resolve().is_relative_to(files_root.resolve())
            assert sha(source) == hashes[source], f'Concurrent change: {source}'
            try:
                with source.open('r+b'):
                    pass
            except PermissionError as exc:
                raise PermissionError(f'Close this Word document before continuing: {source}') from exc
        backup = data / 'backups' / f'introduction-h1-before-edit-{time.time_ns()}.zip'
        backup.parent.mkdir(parents=True, exist_ok=True)
        with ZipFile(backup, 'x') as z:
            for source, _, _ in changed:
                z.write(source, source.relative_to(files_root).as_posix())
        with ZipFile(backup) as z:
            for source, _, _ in changed:
                assert hashlib.sha256(z.read(source.relative_to(files_root).as_posix())).hexdigest() == hashes[source]
        written = []
        try:
            for source, destination, _ in changed:
                assert sha(source) == hashes[source], f'Concurrent change: {source}'
                written.append(source)
                shutil.copyfile(destination, source)
                assert sha(source) == sha(destination)
            for source in unchanged:
                assert sha(source) == hashes[source]
            assert all(has_opening_h1(p) for p in files)
        except Exception:
            with ZipFile(backup) as z:
                for source in written:
                    source.write_bytes(z.read(source.relative_to(files_root).as_posix()))
            raise
        report.update(installed=True, backup=str(backup), allFilesStartWithH1=True)
        print(f'Installed {len(changed)} changes; verified all {len(files)} files start with H1.', flush=True)
    (output / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=Path, default=DEFAULT_DATA)
    parser.add_argument('--output', type=Path, default=ROOT / 'build/introduction-h1')
    parser.add_argument('--install', action='store_true')
    args = parser.parse_args()
    run(args.data.resolve(), args.output.resolve(), args.install)
