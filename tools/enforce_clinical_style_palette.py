"""Restrict editable subject-note text to the user's pictured template palette."""
import argparse
from collections import Counter
from copy import deepcopy
import json
from pathlib import Path
import re
import shutil
import time
from zipfile import ZipFile
from lxml import etree as E

from apply_clinical_template import (
    ROOT, DEFAULT_DATA, DEFAULT_TEMPLATE, W, NS, Template, read, sha, xml,
    serialize, local, val, child, remove, signature, list_signature,
    preserve_source_list_properties, order_properties,
)
from ensure_introduction_h1 import has_opening_h1

PARAGRAPH = {
    'Normal', 'Heading1', 'Heading2', 'Heading3', 'Heading4', 'Title',
    'BoldSide1', 'boldside2', 'Boldside3', 'boldside4', 'image',
    'level1', 'level2', 'level3',
}
CHARACTER = {'SubtleEmphasis', 'Emphasis'}
ALLOWED = PARAGRAPH | CHARACTER
BY_KEY = {re.sub(r'[^a-z0-9]', '', s.casefold()): s for s in ALLOWED}
PREFIX = re.compile(r'^(?:(?:n|import|chapter|gi|imp)\d+(?:_\d+)*_?)+', re.I)
BLUE = {'294C7B', '28467C', '28467C', '28446C', '0563C1', '0000FF', '1F4D78', '2F5496'}
NEUTRAL = {'', 'AUTO', '000000', '262626', 'FFFFFF'}


def canonical(value):
    value = PREFIX.sub('', value or '')
    return re.sub(r'[^a-z0-9]', '', value.casefold())


def inherited(styles, sid, prop, seen=None):
    seen = set(seen or ())
    if not sid or sid not in styles or sid in seen:
        return None
    seen.add(sid)
    style = styles[sid]
    node = style.find(prop, NS)
    if node is not None:
        return node
    return inherited(styles, val(style.find('w:basedOn', NS)), prop, seen)


def outline(paragraph, styles, sid):
    node = paragraph.find('w:pPr/w:outlineLvl', NS)
    if node is None:
        node = inherited(styles, sid, 'w:pPr/w:outlineLvl')
    return val(node)


def choose_paragraph(paragraph, styles):
    sid = val(paragraph.find('w:pPr/w:pStyle', NS)) or 'Normal'
    style = styles.get(sid)
    labels = [canonical(sid), canonical(val(style.find('w:name', NS))) if style is not None else '']
    level = outline(paragraph, styles, sid)
    # Native outline semantics take priority over legacy style aliases.
    if level.isdigit() and int(level) < 9:
        return f'Heading{int(level)+1}' if int(level) < 4 else 'Boldside3', level
    for label in labels:
        if label in BY_KEY and BY_KEY[label] in PARAGRAPH:
            target = BY_KEY[label]
            # Select the existing list depth while retaining explicit numId/ilvl.
            if target.startswith('level'):
                if val(paragraph.find('w:pPr/w:numPr/w:numId', NS)) == '0':
                    return 'Normal', level
                ilvl = val(paragraph.find('w:pPr/w:numPr/w:ilvl', NS)) or '0'
                return f'level{min(int(ilvl), 2)+1}', level
            return target, level
    if any('caption' in label or label.startswith('image') for label in labels):
        return 'image', level
    if any('subtitle' in label for label in labels):
        return 'Boldside3', level
    number_id = val(paragraph.find('w:pPr/w:numPr/w:numId', NS))
    if number_id and number_id != '0':
        ilvl = val(paragraph.find('w:pPr/w:numPr/w:ilvl', NS)) or '0'
        return f'level{min(int(ilvl), 2)+1}', level
    return 'Normal', level


def true(node):
    return node is not None and val(node).casefold() not in {'0', 'false', 'off', 'none'}


def character_role(run, styles):
    props = run.find('w:rPr', NS)
    if props is None:
        return None
    sid = val(props.find('w:rStyle', NS))
    style = styles.get(sid)
    labels = [canonical(sid), canonical(val(style.find('w:name', NS))) if style is not None else '']
    if any('subtleemphasis' in label or 'hyperlink' in label for label in labels):
        return 'SubtleEmphasis'
    if any(label == 'emphasis' or 'intenseemphasis' in label for label in labels):
        return 'Emphasis'
    return None


def clean_run_properties(props, role, table, header, diagram=False):
    # Keep language, direction, fields, revision metadata and super/subscript.
    keep = {'lang', 'rtl', 'cs', 'vertAlign', 'noProof', 'vanish', 'specVanish', 'ins', 'del', 'rPrChange',
            'b', 'bCs', 'i', 'iCs', 'u', 'strike', 'dstrike', 'caps', 'smallCaps', 'highlight', 'shd'}
    if role is None:
        keep.add('color')
    font = props.find('w:rFonts', NS)
    if font is not None and any(t in v.casefold() for v in font.attrib.values()
                                for t in ['symbol', 'wingdings', 'cambria math']):
        keep.add('rFonts')
    # Font size inside a diagram is part of its fixed drawing layout.
    if diagram:
        keep |= {'sz', 'szCs'}
    for item in list(props):
        if local(item) not in keep:
            props.remove(item)
    if role:
        node = E.Element(f'{{{W}}}rStyle', {f'{{{W}}}val': role}); props.insert(0, node)
    if table and not diagram:
        child(props, 'sz').set(f'{{{W}}}val', '19')
        child(props, 'szCs').set(f'{{{W}}}val', '19')
        if header:
            child(props, 'color').set(f'{{{W}}}val', 'FFFFFF')
            child(props, 'b').set(f'{{{W}}}val', 'true')


def normalize(source, destination, reference):
    before = read(source); after = dict(before)
    root = xml(before['word/document.xml']); styles_root = xml(before['word/styles.xml'])
    styles = {}
    for style in styles_root.findall('w:style', NS):
        styles.setdefault(val(style, 'styleId'), style)
    assert ALLOWED <= set(styles), source
    numbering = xml(before['word/numbering.xml'])
    original_signature = signature(root)
    original_lists = list_signature(root, styles_root, numbering)
    preserve_source_list_properties(root, styles_root)
    used_p, used_r = Counter(), Counter()
    for paragraph in root.findall('.//w:p', NS):
        target, old_outline = choose_paragraph(paragraph, styles)
        diagram = any(local(a) in {'txbxContent', 'textbox', 'txbx'} for a in paragraph.iterancestors())
        table = any(local(a) == 'tc' for a in paragraph.iterancestors())
        row = next((a for a in paragraph.iterancestors() if local(a) == 'tr'), None)
        header = table and row is not None and row.find('w:trPr/w:tblHeader', NS) is not None
        props = paragraph.find('w:pPr', NS)
        if props is None:
            props = E.Element(f'{{{W}}}pPr'); paragraph.insert(0, props)
        old_style = val(props.find('w:pStyle', NS)) or 'Normal'
        if not diagram:
            remove(props, {'spacing', 'ind', 'tabs', 'pBdr', 'shd', 'jc', 'contextualSpacing', 'rPr'})
        else:
            remove(props, {'rPr'})
        pstyle = props.find('w:pStyle', NS)
        if pstyle is None:
            pstyle = E.Element(f'{{{W}}}pStyle'); props.insert(0, pstyle)
        pstyle.set(f'{{{W}}}val', target)
        if old_outline.isdigit() and int(old_outline) < 9:
            child(props, 'outlineLvl').set(f'{{{W}}}val', old_outline)
        if table and not diagram:
            props.append(deepcopy(reference.table_spacing))
            mark = child(props, 'rPr')
            child(mark, 'sz').set(f'{{{W}}}val', '19')
        elif not diagram:
            prototype = reference.body.xpath('./w:p[w:pPr/w:pStyle/@w:val=$s]', namespaces=NS, s=target)
            if prototype:
                for extra in prototype[0].find('w:pPr', NS):
                    if local(extra) not in {'pStyle', 'numPr', 'rPr'}:
                        remove(props, {local(extra)}); props.append(deepcopy(extra))
            elif target == 'Normal':
                props.append(deepcopy(reference.body_spacing))
        styled_paragraph = target not in {'Normal', 'level1', 'level2', 'level3'}
        for run in paragraph.findall('.//w:r', NS):
            owner = next((a for a in run.iterancestors() if a.tag == f'{{{W}}}p'), None)
            if owner is not paragraph:
                continue
            role = None if styled_paragraph or header else character_role(run, styles)
            rpr = run.find('w:rPr', NS)
            if rpr is None:
                if not table and not role:
                    continue
                rpr = E.Element(f'{{{W}}}rPr'); run.insert(0, rpr)
            if rpr.find('w:rStyle', NS) is not None and val(rpr.find('w:rStyle', NS)).endswith(('FootnoteReference', 'EndnoteReference')):
                child(rpr, 'vertAlign').set(f'{{{W}}}val', 'superscript')
            if not role and not styled_paragraph:
                run_style = val(rpr.find('w:rStyle', NS))
                for name in ('b', 'bCs', 'i', 'iCs', 'u', 'strike', 'dstrike', 'caps', 'smallCaps', 'color', 'highlight', 'shd'):
                    if rpr.find(f'w:{name}', NS) is None:
                        source_property = inherited(styles, run_style, f'w:rPr/{name}')
                        if source_property is not None:
                            rpr.append(deepcopy(source_property))
            clean_run_properties(rpr, role, table, header, diagram)
            if role:
                used_r[role] += 1
        used_p[target] += 1
    # Keep native dependencies, but show only the pictured text styles in Quick Styles.
    for style in styles_root.findall('w:style', NS):
        sid = val(style, 'styleId')
        if sid in ALLOWED:
            remove(style, {'semiHidden', 'hidden'})
            if style.find('w:qFormat', NS) is None:
                node = E.Element(f'{{{W}}}qFormat')
                index = next((i for i, n in enumerate(style) if local(n) in {'pPr', 'rPr', 'tblPr', 'trPr', 'tcPr'}), len(style))
                style.insert(index, node)
        else:
            remove(style, {'qFormat'})
    order_properties(root)
    assert signature(root) == original_signature, source
    assert list_signature(root, styles_root, numbering) == original_lists, ('List structure changed', source)
    assert {val(n) for n in root.findall('.//w:pPr/w:pStyle', NS)} <= PARAGRAPH
    assert {val(n) for n in root.findall('.//w:rPr/w:rStyle', NS)} <= CHARACTER
    after['word/document.xml'] = serialize(root)
    after['word/styles.xml'] = serialize(styles_root)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(source) as old, ZipFile(destination, 'w') as new:
        new.comment = old.comment
        for info in old.infolist():
            new.writestr(info, after[info.filename])
    checked = read(destination)
    assert all(checked[n] == b for n, b in before.items() if n not in {'word/document.xml', 'word/styles.xml'})
    assert has_opening_h1(destination)
    return used_p, used_r


def stage(data, output, template):
    reference = Template(template); root = data / 'files'
    files = sorted(p for folder in root.iterdir() if folder.is_dir() and not folder.name.startswith(('_', '.'))
                   for p in folder.glob('*.docx') if not p.name.startswith('~$'))
    output.mkdir(parents=True, exist_ok=True)
    report = {'template': str(template), 'templateHash': reference.sha, 'files': [],
              'visualQA': 'Unavailable: LibreOffice renderer is not installed.',
              'allowedParagraphStyles': sorted(PARAGRAPH), 'allowedCharacterStyles': sorted(CHARACTER)}
    ps, rs = Counter(), Counter()
    for i, source in enumerate(files, 1):
        relative = source.relative_to(root); original = sha(source)
        target = output / 'documents' / relative
        a, b = normalize(source, target, reference); ps.update(a); rs.update(b)
        assert sha(source) == original, ('Concurrent edit', source)
        report['files'].append({'path': relative.as_posix(), 'originalHash': original, 'formattedHash': sha(target)})
        if i % 20 == 0 or i == len(files):
            print(f'Palette normalized and verified {i}/{len(files)} files.', flush=True)
    report.update(filesChecked=len(files), paragraphStylesUsed=dict(ps), characterStylesUsed=dict(rs),
                  originalContentListsAndMediaPreserved=True)
    (output / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k != 'files'}, indent=2), flush=True)


def install(data, output):
    report_path = output / 'report.json'; report = json.loads(report_path.read_text(encoding='utf-8'))
    assert sha(Path(report['template'])) == report['templateHash']
    root = (data / 'files').resolve()
    for row in report['files']:
        source = root / row['path']; staged = output / 'documents' / row['path']
        assert source.resolve().is_relative_to(root)
        assert sha(source) == row['originalHash'], ('Source changed', source)
        assert sha(staged) == row['formattedHash']
        try:
            with source.open('r+b'):
                pass
        except PermissionError as exc:
            raise PermissionError(f'Close this Word document: {source}') from exc
    backup = data / 'backups' / f'style-palette-before-edit-{time.time_ns()}.zip'
    backup.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(backup, 'x') as z:
        z.writestr('style-palette-manifest.json', json.dumps(report, ensure_ascii=False, indent=2))
        for row in report['files']:
            z.write(root / row['path'], row['path'])
    with ZipFile(backup) as z:
        import hashlib
        for row in report['files']:
            assert hashlib.sha256(z.read(row['path'])).hexdigest() == row['originalHash']
    written = []
    try:
        for row in report['files']:
            source = root / row['path']; staged = output / 'documents' / row['path']
            assert sha(source) == row['originalHash']
            written.append(row); shutil.copyfile(staged, source)
            assert sha(source) == row['formattedHash']
        assert all(has_opening_h1(root / row['path']) for row in report['files'])
    except Exception:
        with ZipFile(backup) as z:
            for row in written:
                (root / row['path']).write_bytes(z.read(row['path']))
        raise
    report.update(installed=True, backup=str(backup), allFilesStartWithH1=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Applied pictured style palette to {len(report["files"])} documents. Backup: {backup}', flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=Path, default=DEFAULT_DATA)
    parser.add_argument('--template', type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument('--output', type=Path, default=ROOT / 'build/clinical-style-palette')
    parser.add_argument('--install', action='store_true')
    args = parser.parse_args()
    if args.install:
        install(args.data.resolve(), args.output.resolve())
    else:
        stage(args.data.resolve(), args.output.resolve(), args.template.resolve())
