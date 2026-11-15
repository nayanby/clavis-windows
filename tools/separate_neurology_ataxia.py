"""Split Ataxia from Movement Disorders and insert it as Neurology chapter eight."""
import argparse
from collections import Counter
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import re
import shutil
import time
from zipfile import ZipFile

from docx import Document
from lxml import etree as E
from word_chapter_distribution import read_package, write_slice, inspect, W, NS, ROOT, DEFAULT_DATA
from ensure_introduction_h1 import has_opening_h1
from enforce_clinical_style_palette import PARAGRAPH, CHARACTER

SOURCE_NAME = '7. Movement Disorders & Cerebellar Ataxias.docx'
MOVEMENT_NAME = '7. Movement Disorders.docx'
ATAXIA_NAME = '8. Ataxia.docx'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def text(node):
    return ''.join(node.xpath('.//w:t/text()', namespaces=NS)).strip()


def run(data, output, install=False):
    subject = (data / 'files/Neurology').resolve()
    source = subject / SOURCE_NAME
    originals = sorted(subject.glob('*.docx'))
    originals = [p for p in originals if not p.name.startswith('~$')]
    hashes = {p: sha(p) for p in originals}
    assert len(originals) == 14, 'Expected the current fourteen Neurology chapters'
    package = read_package(source)
    root = E.fromstring(package['word/document.xml'])
    body = root.find('w:body', NS)
    split = next(i for i, n in enumerate(body) if text(n).casefold() == 'ataxia'
                 and n.find('w:pPr/w:pStyle', NS) is not None
                 and n.find('w:pPr/w:pStyle', NS).get(f'{{{W}}}val') == 'Heading1')
    end = len(body) - 1
    assert body[end].tag == f'{{{W}}}sectPr'
    title = next(n for n in body[:split] if n.find('w:pPr/w:pStyle', NS) is not None
                 and n.find('w:pPr/w:pStyle', NS).get(f'{{{W}}}val') == 'Title')
    old_title = text(title)
    assert old_title == 'Movement Disorders & Cerebellar Ataxias'
    title_nodes = title.xpath('.//w:t', namespaces=NS)
    for i, n in enumerate(title_nodes):
        n.text = 'Movement Disorders' if i == 0 else ''
    edited_package = dict(package)
    edited_package['word/document.xml'] = E.tostring(root, encoding='UTF-8', xml_declaration=True, standalone=True)
    output.mkdir(parents=True, exist_ok=True)
    movement = output / MOVEMENT_NAME; ataxia = output / ATAXIA_NAME
    write_slice(edited_package, [(0, split)], movement)
    write_slice(package, [(split, end)], ataxia)
    combined = Counter(); tables = 0; images = Counter()
    for path, expected in [(movement, list(body[:split])), (ataxia, list(body[split:end]))]:
        data_after = read_package(path)
        assert all(data_after[n] == b for n, b in package.items() if n != 'word/document.xml')
        result_body = E.fromstring(data_after['word/document.xml']).find('w:body', NS)
        assert len(result_body) == len(expected) + 1
        for actual, original in zip(list(result_body)[:-1], expected):
            assert E.tostring(actual, method='c14n') == E.tostring(original, method='c14n')
        assert has_opening_h1(path)
        assert {n.get(f'{{{W}}}val') for n in result_body.findall('.//w:pPr/w:pStyle', NS)} <= PARAGRAPH
        assert {n.get(f'{{{W}}}val') for n in result_body.findall('.//w:rPr/w:rStyle', NS)} <= CHARACTER
        content, count, media = inspect(path)
        combined.update(content); tables += count; images.update(media)
        assert len(Document(path).paragraphs) > 0
    expected_text = Counter(root.xpath('//w:body//w:t/text()', namespaces=NS))
    expected_text += Counter()  # Ignore empty text nodes left by the title edit.
    assert +combined == expected_text
    _, before_tables, before_images = inspect(source)
    assert tables == before_tables and images == before_images
    renames = []
    for p in originals:
        match = re.match(r'^(\d+)\. (.+)\.docx$', p.name)
        assert match, p
        number = int(match.group(1))
        if number >= 8:
            renames.append((p, subject / f'{number + 1}. {match.group(2)}.docx'))
    targets = [subject / MOVEMENT_NAME, subject / ATAXIA_NAME, *(b for a, b in renames)]
    assert len(targets) == len(set(targets))
    assert not any(p.exists() for p in targets), 'A destination chapter already exists'
    report = {'movementChapter': MOVEMENT_NAME, 'newChapter': ATAXIA_NAME,
              'laterChaptersRenumbered': [{'old': a.name, 'new': b.name} for a, b in renames],
              'splitBodyElement': split, 'tableCountPreserved': tables,
              'imageReferencesPreserved': sum(images.values()), 'sourceContentPreserved': True,
              'stylesAndAllOtherPackagePartsPreserved': True,
              'visualQA': 'Not completed: LibreOffice renderer is unavailable.'}
    print(json.dumps(report, ensure_ascii=False, indent=2), flush=True)
    if install:
        affected = [source, *(a for a, b in renames)]
        for path in affected:
            assert path.resolve().is_relative_to(subject)
            assert sha(path) == hashes[path], 'Concurrent edit detected'
            try:
                with path.open('r+b'):
                    pass
            except PermissionError as exc:
                raise PermissionError(f'Close this Word document before continuing: {path}') from exc
        backup = data / 'backups' / f'neurology-before-ataxia-split-{time.time_ns()}.zip'
        backup.parent.mkdir(parents=True, exist_ok=True)
        with ZipFile(backup, 'x') as z:
            z.writestr('ataxia-split-manifest.json', json.dumps(report, ensure_ascii=False, indent=2))
            for path in affected:
                z.write(path, path.name)
        with ZipFile(backup) as z:
            for path in affected:
                assert hashlib.sha256(z.read(path.name)).hexdigest() == hashes[path]
        moved, written = [], []
        retired = False
        try:
            for path in (movement, ataxia):
                target = subject / path.name
                shutil.copyfile(path, target); written.append(target)
                assert sha(target) == sha(path)
            for old, new in renames:
                assert old.resolve().is_relative_to(subject) and new.resolve().is_relative_to(subject)
                assert sha(old) == hashes[old]
                old.rename(new); moved.append((old, new))
                assert sha(new) == hashes[old]
            assert sha(source) == hashes[source]
            source.unlink(); retired = True
            for path in originals:
                if path not in affected:
                    assert sha(path) == hashes[path]
            current = [p for p in subject.glob('*.docx') if not p.name.startswith('~$')]
            assert len(current) == 15
            assert {int(p.name.split('.', 1)[0]) for p in current} == set(range(1, 16))
            assert all(has_opening_h1(subject / n) for n in [MOVEMENT_NAME, ATAXIA_NAME])
        except Exception:
            for old, new in reversed(moved):
                new.rename(old)
            for path in written:
                assert path.resolve().is_relative_to(subject); path.unlink()
            if retired:
                with ZipFile(backup) as z:
                    source.write_bytes(z.read(source.name))
            raise
        report.update(installed=True, backup=str(backup), totalNeurologyChapters=15)
        print(f'Installed Ataxia chapter 8; Neurology now has 15 chapters. Backup: {backup}', flush=True)
    (output / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=Path, default=DEFAULT_DATA)
    parser.add_argument('--output', type=Path, default=ROOT / 'build/neurology-ataxia-split')
    parser.add_argument('--install', action='store_true')
    args = parser.parse_args()
    run(args.data.resolve(), args.output.resolve(), args.install)
