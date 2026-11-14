"""Preserve source Word content while distributing it into numbered chapters."""
from __future__ import annotations

import argparse
from collections import Counter
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import posixpath
import shutil
import time
from zipfile import ZipFile, ZIP_DEFLATED

from docx import Document
from docx.opc.packuri import PackURI
from lxml import etree as E

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = Path(r'C:\Users\ANT-PC\OneDrive\Cortex Windows\data')
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
R = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
NS = {'w': W, 'r': R}
def read_package(path):
    with ZipFile(path) as z:
        assert z.testzip() is None
        return {name: z.read(name) for name in z.namelist()}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def body_for(package):
    return E.fromstring(package['word/document.xml']).find(f'{{{W}}}body')


def write_slice(package, slices, dest):
    root = E.fromstring(package['word/document.xml'])
    body = root.find(f'{{{W}}}body')
    original = list(body)
    section = deepcopy(body.find(f'{{{W}}}sectPr'))
    for n in original:
        body.remove(n)
    for start, end in slices:
        for n in original[start:end]:
            assert n.tag != f'{{{W}}}sectPr'
            body.append(deepcopy(n))
    if section is not None:
        body.append(section)
    content = dict(package)
    content['word/document.xml'] = E.tostring(root, encoding='UTF-8', xml_declaration=True, standalone=True)
    with ZipFile(dest, 'w', ZIP_DEFLATED) as z:
        for name, data in content.items():
            z.writestr(name, data)


def merge(target, incoming, prefix):
    """Import a source body together with its styles, lists and relationships."""
    for part in incoming.part.package.parts:
        name = str(part.partname)
        # Relink all potentially imported resources, not only raster images.
        if name.startswith('/word/') and name != '/word/document.xml':
            folder, leaf = name.rsplit('/', 1)
            part._partname = PackURI(folder + '/' + prefix + leaf)

    stylemap = {s.style_id: prefix + s.style_id for s in incoming.styles}
    numbering = target.part.numbering_part.element
    source_numbering = incoming.part.numbering_part.element
    numbermaps = {}
    for kind, attr in [('abstractNum', 'abstractNumId'), ('num', 'numId')]:
        used = [int(n.get(f'{{{W}}}{attr}')) for n in numbering.findall(f'{{{W}}}{kind}')]
        offset = max(used, default=0) + 1
        numbermaps[kind] = {
            n.get(f'{{{W}}}{attr}'): str(offset + i)
            for i, n in enumerate(source_numbering.findall(f'{{{W}}}{kind}'))
        }

    def remap(node):
        for ref in node.iter():
            if ref.tag in {f'{{{W}}}{t}' for t in ('pStyle', 'rStyle', 'tblStyle', 'basedOn', 'next', 'link', 'styleLink', 'numStyleLink')}:
                val = ref.get(f'{{{W}}}val')
                if val in stylemap:
                    ref.set(f'{{{W}}}val', stylemap[val])
            if ref.tag in (f'{{{W}}}numId', f'{{{W}}}abstractNumId'):
                kind = 'num' if ref.tag == f'{{{W}}}numId' else 'abstractNum'
                val = ref.get(f'{{{W}}}val')
                if val in numbermaps[kind]:
                    ref.set(f'{{{W}}}val', numbermaps[kind][val])
            for key, value in list(ref.attrib.items()):
                if E.QName(key).namespace == R:
                    rel = incoming.part.rels[value]
                    ref.set(key, target.part.relate_to(
                        rel.target_ref if rel.is_external else rel.target_part,
                        rel.reltype, rel.is_external))
        return node

    for style in incoming.styles:
        node = deepcopy(style.element)
        node.set(f'{{{W}}}styleId', stylemap[style.style_id])
        # Prevent multiple competing default paragraph/character styles.
        node.attrib.pop(f'{{{W}}}default', None)
        name = node.find(f'{{{W}}}name')
        if name is not None:
            name.set(f'{{{W}}}val', prefix + name.get(f'{{{W}}}val', ''))
        target.styles.element.append(remap(node))
    for original in source_numbering:
        kind = E.QName(original).localname
        if kind not in numbermaps:
            continue
        n = deepcopy(original)
        attr = 'abstractNumId' if kind == 'abstractNum' else 'numId'
        n.set(f'{{{W}}}{attr}', numbermaps[kind][n.get(f'{{{W}}}{attr}')])
        # Distinct abstract-list identities avoid accidental list joining.
        nsid = n.find(f'{{{W}}}nsid')
        if nsid is not None:
            nsid.set(f'{{{W}}}val', hashlib.sha256((prefix + E.tostring(n).hex()).encode()).hexdigest()[:8].upper())
        numbering.append(remap(n))
    target.add_page_break()
    for original in incoming.element.body:
        if original.tag != f'{{{W}}}sectPr':
            target.element.body.insert(len(target.element.body) - 1, remap(deepcopy(original)))


def add_title(doc, title):
    paragraph = E.Element(f'{{{W}}}p')
    pr = E.SubElement(paragraph, f'{{{W}}}pPr')
    E.SubElement(pr, f'{{{W}}}pStyle', {f'{{{W}}}val': 'Title'})
    E.SubElement(pr, f'{{{W}}}keepNext')
    run = E.SubElement(paragraph, f'{{{W}}}r')
    props = E.SubElement(run, f'{{{W}}}rPr')
    E.SubElement(props, f'{{{W}}}b')
    E.SubElement(props, f'{{{W}}}color', {f'{{{W}}}val': '000000'})
    E.SubElement(props, f'{{{W}}}sz', {f'{{{W}}}val': '32'})
    E.SubElement(run, f'{{{W}}}t').text = title
    doc.element.body.insert(0, paragraph)


def make_unique_drawing_ids(doc):
    count = 0
    for node in doc.element.iter():
        if E.QName(node).localname in ('docPr', 'cNvPr'):
            count += 1
            node.set('id', str(count))


def inspect(path):
    package = read_package(path)
    root = E.fromstring(package['word/document.xml'])
    text = Counter(root.xpath('//w:body//w:t/text()', namespaces=NS))
    tables = len(root.xpath('//w:body//w:tbl', namespaces=NS))
    rels = {r.get('Id'): r for r in E.fromstring(package['word/_rels/document.xml.rels'])}
    images = Counter()
    for n in root.iter():
        for key, value in n.attrib.items():
            if E.QName(key).namespace == R:
                assert value in rels, (path, value)
                rel = rels[value]
                if rel.get('Type').endswith('/image'):
                    target = posixpath.normpath(posixpath.join('word', rel.get('Target')))
                    images[hashlib.sha256(package[target]).hexdigest()] += 1
    # Check every internal OPC relationship resolves to an actual ZIP member.
    for name, data in package.items():
        if name.endswith('.rels'):
            directory = posixpath.dirname(posixpath.dirname(name))
            for rel in E.fromstring(data):
                if rel.get('TargetMode') == 'External':
                    continue
                resolved = posixpath.normpath(posixpath.join(directory, rel.get('Target'))).lstrip('/')
                assert resolved in package, (path, name, resolved)
    ids = [n.get(f'{{{W}}}styleId') for n in E.fromstring(package['word/styles.xml']) if n.tag == f'{{{W}}}style']
    assert len(ids) == len(set(ids)), 'Duplicate style IDs'
    style_ids = set(ids)
    for node in root.xpath('//w:pStyle | //w:rStyle | //w:tblStyle', namespaces=NS):
        assert node.get(f'{{{W}}}val') in style_ids, ('Missing Word style', path, node.get(f'{{{W}}}val'))
    numbering = E.fromstring(package['word/numbering.xml'])
    list_ids = {n.get(f'{{{W}}}numId') for n in numbering.findall(f'{{{W}}}num')}
    for node in root.xpath('//w:numId', namespaces=NS):
        assert node.get(f'{{{W}}}val') in list_ids | {'0'}, ('Missing list definition', path)
    return text, tables, images


def totals(paths):
    text, images = Counter(), Counter()
    tables = 0
    for path in paths:
        t, n, i = inspect(path)
        text.update(t)
        tables += n
        images.update(i)
    return text, tables, images


def run(data, output, subject, sources, chapters, install=False, content_gaps=None):
    source = data / 'files' / subject
    originals = [source / name for name in sources]
    placeholders = [source / f'{i:02}. {title}.docx' for i, (title, _) in enumerate(chapters, 1)]
    before_hashes = {p: digest(p) for p in [*originals, *placeholders]}
    packages = [read_package(p) for p in originals]
    bodies = [body_for(package) for package in packages]
    coverage = [[] for _ in originals]
    for _, ranges in chapters:
        for src, start, end in ranges:
            coverage[src].extend(range(start, end))
    for i, body in enumerate(bodies):
        expected = [j for j, n in enumerate(body) if n.tag != f'{{{W}}}sectPr']
        assert sorted(coverage[i]) == expected, ('Incomplete or duplicate source mapping', sources[i])
        assert not body.xpath('.//w:footnoteReference | .//w:endnoteReference | .//w:commentReference', namespaces=NS)

    output.mkdir(parents=True, exist_ok=True)
    report = {'sourceFiles': len(originals), 'chapters': [], 'sourceHashes': {p.name: h for p, h in before_hashes.items()},
              'contentGaps': content_gaps or [],
              'visualQA': 'Not completed: render_docx.py could not find LibreOffice soffice.exe.'}
    outputs = []
    for number, (title, ranges) in enumerate(chapters, 1):
        work = output / 'parts' / f'{number:02}'
        work.mkdir(parents=True, exist_ok=True)
        grouped = {}
        for src, start, end in ranges:
            grouped.setdefault(src, []).append((start, end))
        partfiles = []
        for index, (src, slices) in enumerate(grouped.items()):
            part = work / f'{index}.docx'
            write_slice(packages[src], slices, part)
            partfiles.append(part)
        doc = Document(partfiles[0])
        for index, part in enumerate(partfiles[1:], 1):
            merge(doc, Document(part), f'chapter{number}_{index}_')
        fulltitle = f'{number:02}. {title}'
        add_title(doc, fulltitle)
        make_unique_drawing_ids(doc)
        dest = output / (fulltitle + '.docx')
        doc.save(dest)
        outputs.append(dest)
        text, tables, images = inspect(dest)
        report['chapters'].append({'file': dest.name, 'tables': tables, 'imageReferences': sum(images.values()),
            'sourceBodyElements': len([i for s, a, b in ranges for i in range(a, b)]),
            'wordCount': sum(len(t.split()) * n for t, n in text.items()),
            'ranges': [{'source': sources[s], 'start': a, 'end': b} for s, a, b in ranges]})
        print(f'{dest.name}: {report["chapters"][-1]["wordCount"]} words', flush=True)

    before = totals(originals)
    after = totals(outputs)
    aftertext = after[0].copy()
    for i, (title, _) in enumerate(chapters, 1):
        aftertext.subtract({f'{i:02}. {title}': 1})
    assert +aftertext == before[0] and not -aftertext, 'Text preservation failed'
    assert after[1:] == before[1:], 'Table/image preservation failed'
    report['verification'] = {'sourceBodyElementsAssignedExactlyOnce': True,
        'textRuns': sum(before[0].values()), 'tables': before[1], 'imageReferences': sum(before[2].values()),
        'allContentPreserved': True, 'allPackageRelationshipsResolved': True}
    if install:
        assert all(digest(p) == h for p, h in before_hashes.items()), 'Concurrent edit detected'
        # Detect open Word documents before changing any of the files.
        for path in before_hashes:
            try:
                with path.open('r+b'):
                    pass
            except PermissionError as exc:
                raise PermissionError(f'Close the locked document before installing: {path.name}') from exc
        backup = data / 'backups' / f'{subject.lower().replace(" ", "-")}-word-before-distribution-{time.time_ns()}.zip'
        backup.parent.mkdir(parents=True, exist_ok=True)
        with ZipFile(backup, 'x', ZIP_DEFLATED) as z:
            for p in before_hashes:
                z.write(p, p.name)
        with ZipFile(backup) as z:
            for p in before_hashes:
                assert hashlib.sha256(z.read(p.name)).hexdigest() == before_hashes[p]
        retired = []
        try:
            for out, target in zip(outputs, placeholders):
                assert out.name == target.name and target.parent.resolve() == source.resolve()
                shutil.copyfile(out, target)
                assert digest(out) == digest(target)
            for p in originals:
                assert p.parent.resolve() == source.resolve() and digest(p) == before_hashes[p]
                p.unlink()
                retired.append(p)
            installed = totals(placeholders)
            assert installed == after
        except Exception:
            with ZipFile(backup) as z:
                for p in before_hashes:
                    if not p.exists() or digest(p) != before_hashes[p]:
                        p.write_bytes(z.read(p.name))
            raise
        report.update(installed=True, backup=str(backup), installedFiles=[str(p) for p in placeholders])
    (output / 'distribution-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(report['verification']), flush=True)
    if install:
        print(f'Installed all {len(chapters)} chapters. Backup: {backup}', flush=True)


