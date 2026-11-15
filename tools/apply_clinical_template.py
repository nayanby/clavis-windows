"""Apply the retained Clinical Notes Templatex formatting to main subject DOCX files.

Preserve source text and relationship-backed objects. Template sample content is
never imported. Stage and verify all files before a separately invoked install.
"""
from __future__ import annotations

import argparse
from collections import Counter
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import posixpath
import re
import shutil
import time
from zipfile import ZipFile

from lxml import etree as E
from ensure_introduction_h1 import has_opening_h1

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = Path(r'C:\Users\ANT-PC\OneDrive\Cortex Windows\data')
DEFAULT_TEMPLATE = Path(r'C:\Users\ANT-PC\OneDrive\Clinical Notes Formatter\Clinical Notes Templatex.dotx')
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
R = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
PKG = 'http://schemas.openxmlformats.org/package/2006/relationships'
CT = 'http://schemas.openxmlformats.org/package/2006/content-types'
NS = {'w': W, 'r': R}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    with ZipFile(path) as z:
        assert z.testzip() is None, path
        assert len(z.namelist()) == len(set(z.namelist())), path
        return {n: z.read(n) for n in z.namelist()}


def xml(data):
    return E.fromstring(data)


def serialize(node):
    return E.tostring(node, encoding='UTF-8', xml_declaration=True, standalone=True)


def local(node):
    return E.QName(node).localname


def val(node, key='val', default=''):
    return node.get(f'{{{W}}}{key}', default) if node is not None else default


def key(value):
    return re.sub(r'[^a-z0-9]', '', value.casefold())


def remove(parent, names):
    for child in list(parent):
        if local(child) in names:
            parent.remove(child)


def child(parent, name):
    found = parent.find(f'{{{W}}}{name}')
    if found is None:
        found = E.Element(f'{{{W}}}{name}')
        if name in {'pPr', 'rPr', 'tblPr', 'trPr', 'tcPr'}:
            parent.insert(0, found)
        else:
            parent.append(found)
    return found


PROPERTY_ORDER = {
    'pPr': 'pStyle keepNext keepLines pageBreakBefore framePr widowControl numPr suppressLineNumbers pBdr shd tabs suppressAutoHyphens kinsoku wordWrap overflowPunct topLinePunct autoSpaceDE autoSpaceDN bidi adjustRightInd snapToGrid spacing ind contextualSpacing mirrorIndents suppressOverlap jc textDirection textAlignment textboxTightWrap outlineLvl divId cnfStyle rPr sectPr pPrChange',
    'numPr': 'ilvl numId numberingChange ins',
    'tblPr': 'tblStyle tblpPr tblOverlap bidiVisual tblStyleRowBandSize tblStyleColBandSize tblW jc tblCellSpacing tblInd tblBorders shd tblLayout tblCellMar tblLook tblCaption tblDescription tblPrChange',
    'trPr': 'cnfStyle divId gridBefore gridAfter wBefore wAfter cantSplit trHeight tblHeader tblCellSpacing jc hidden ins del trPrChange',
    'tcPr': 'cnfStyle tcW gridSpan hMerge vMerge tcBorders shd noWrap tcMar textDirection tcFitText vAlign hideMark headers cellIns cellDel cellMerge tcPrChange',
    'sectPr': 'headerReference footerReference footnotePr endnotePr type pgSz pgMar paperSrc pgBorders lnNumType pgNumType cols formProt vAlign noEndnote titlePg textDirection bidi rtlGutter docGrid printerSettings sectPrChange',
    'lvl': 'start numFmt lvlRestart pStyle isLgl suff lvlText lvlPicBulletId legacy lvlJc pPr rPr',
}


def order_properties(root):
    for node in root.iter():
        if E.QName(node).namespace != W or local(node) not in PROPERTY_ORDER:
            continue
        positions = {name: i for i, name in enumerate(PROPERTY_ORDER[local(node)].split())}
        node[:] = sorted(node, key=lambda n: positions.get(local(n), len(positions)))


def signature(root):
    body = root.find('w:body', NS)
    tags = Counter(local(n) for n in body.iter()
                   if local(n) in {'p', 'r', 'tbl', 'tr', 'tc', 'drawing', 'pict', 'object',
                                   'hyperlink', 'bookmarkStart', 'bookmarkEnd', 'footnoteReference',
                                   'endnoteReference', 'commentReference', 'sectPr', 'fldChar'})
    text = tuple((E.QName(n).namespace, local(n), n.text or '') for n in body.iter()
                 if local(n) in {'t', 'instrText', 'delText'})
    merges = tuple((local(n), tuple(sorted(n.attrib.items()))) for n in body.iter()
                   if local(n) in {'gridSpan', 'vMerge', 'hMerge'})
    links = tuple((k, v) for n in body.iter() if local(n) not in {'footerReference', 'headerReference'}
                  for k, v in n.attrib.items() if E.QName(k).namespace == R)
    return tags, text, merges, links


class Template:
    def __init__(self, path):
        self.path = path
        self.sha = sha(path)
        self.parts = read(path)
        self.styles = xml(self.parts['word/styles.xml'])
        self.stylemap = {val(n, 'styleId'): n for n in self.styles.findall('w:style', NS)}
        self.lookup = {}
        for sid, style in self.stylemap.items():
            for label in (sid, val(style.find('w:name', NS))):
                self.lookup.setdefault((val(style, 'type'), key(label)), sid)
        self.document = xml(self.parts['word/document.xml'])
        self.body = self.document.find('w:body', NS)
        self.section = self.body.find('w:sectPr', NS)
        self.numbering = xml(self.parts['word/numbering.xml'])
        self.bullet_levels = self.numbering.find('w:abstractNum', NS).findall('w:lvl', NS)
        self.example_table = self.body.find('w:tbl', NS)
        self.cell_margin = self.example_table.find('w:tr/w:tc/w:tcPr/w:tcMar', NS)
        self.body_spacing = self.body.xpath('./w:p[.//w:t="Body text."]/w:pPr/w:spacing', namespaces=NS)[0]
        self.table_spacing = self.example_table.find('w:tr/w:tc/w:p/w:pPr/w:spacing', NS)
        self.max_width = int(val(self.section.find('w:pgSz', NS), 'w')) - sum(
            int(val(self.section.find('w:pgMar', NS), side)) for side in ('left', 'right'))

    def map_styles(self, source):
        result = {}
        for style in source.findall('w:style', NS):
            sid = val(style, 'styleId')
            typ = val(style, 'type')
            labels = [sid, val(style.find('w:name', NS))]
            labels += [re.sub(r'^(?:(?:chapter|gi|import)\d+(?:_\d+)?_)+', '', label, flags=re.I) for label in labels]
            exact = next((label for label in labels if label in self.stylemap and val(self.stylemap[label], 'type') == typ), None)
            target = exact or next((self.lookup[(typ, key(label))] for label in labels if (typ, key(label)) in self.lookup), None)
            if target is None and typ == 'paragraph':
                outline = val(style.find('w:pPr/w:outlineLvl', NS))
                if outline.isdigit() and int(outline) < 9:
                    target = f'Heading{int(outline) + 1}'
                elif key(sid) in {'bodytext', 'body', 'bodytext2', 'bodytext3'}:
                    target = 'Normal'
            result[sid] = target or sid
        return result


def remap_style_refs(node, mapping):
    for ref in node.iter():
        if local(ref) in {'pStyle', 'rStyle', 'tblStyle', 'basedOn', 'next', 'link', 'styleLink', 'numStyleLink'}:
            value = val(ref)
            if value in mapping:
                ref.set(f'{{{W}}}val', mapping[value])


def preserve_source_list_properties(document, source_styles):
    definitions = {}
    for style in source_styles.findall('w:style', NS):
        definitions.setdefault(val(style, 'styleId'), style)
    cache = {}

    def inherited(sid, visited=None):
        if sid in cache:
            return dict(cache[sid])
        visited = set(visited or ())
        if sid not in definitions or sid in visited:
            return {}
        visited.add(sid); style = definitions[sid]
        result = inherited(val(style.find('w:basedOn', NS)), visited)
        num = style.find('w:pPr/w:numPr', NS)
        if num is not None:
            result.update({local(n): val(n) for n in num if local(n) in {'ilvl', 'numId'}})
        cache[sid] = dict(result)
        return result

    for paragraph in document.findall('.//w:p', NS):
        props = paragraph.find('w:pPr', NS)
        if props is None:
            props = E.Element(f'{{{W}}}pPr'); paragraph.insert(0, props)
        effective = inherited(val(props.find('w:pStyle', NS)) or 'Normal')
        num = props.find('w:numPr', NS)
        if num is not None:
            effective.update({local(n): val(n) for n in num if local(n) in {'ilvl', 'numId'}})
        if num is None:
            num = E.SubElement(props, f'{{{W}}}numPr')
        number_id = effective.get('numId') or '0'
        child(num, 'numId').set(f'{{{W}}}val', number_id)
        if number_id != '0':
            child(num, 'ilvl').set(f'{{{W}}}val', effective.get('ilvl') or '0')


def list_signature(document, styles, numbering):
    definitions = {}
    for n in styles.findall('w:style', NS):
        definitions.setdefault(val(n, 'styleId'), n)
    numbers = {val(n, 'numId'): n for n in numbering.findall('w:num', NS)}
    abstracts = {val(n, 'abstractNumId'): n for n in numbering.findall('w:abstractNum', NS)}
    cache = {}

    def inherited(sid, seen=None):
        if sid in cache:
            return dict(cache[sid])
        seen = set(seen or ())
        if sid in seen or sid not in definitions:
            return {}
        seen.add(sid); style = definitions[sid]
        result = inherited(val(style.find('w:basedOn', NS)), seen)
        props = style.find('w:pPr/w:numPr', NS)
        if props is not None:
            result.update({local(n): val(n) for n in props if local(n) in {'ilvl', 'numId'}})
        cache[sid] = dict(result)
        return result

    result = []
    for paragraph in document.findall('.//w:p', NS):
        props = inherited(val(paragraph.find('w:pPr/w:pStyle', NS)) or 'Normal')
        direct = paragraph.find('w:pPr/w:numPr', NS)
        if direct is not None:
            props.update({local(n): val(n) for n in direct if local(n) in {'ilvl', 'numId'}})
        number_id = props.get('numId')
        if not number_id or number_id == '0':
            result.append(None); continue
        level = props.get('ilvl', '0')
        number = numbers.get(number_id)
        abstract = abstracts.get(val(number.find('w:abstractNumId', NS))) if number is not None else None
        definition = abstract.find(f'w:lvl[@w:ilvl="{level}"]', NS) if abstract is not None else None
        if definition is None:
            result.append(('unresolved', number_id, level)); continue
        fmt = val(definition.find('w:numFmt', NS))
        if fmt == 'bullet':
            result.append(('bullet', level))
        else:
            override = number.find(f'w:lvlOverride[@w:ilvl="{level}"]/w:startOverride', NS)
            start = val(override) or val(definition.find('w:start', NS))
            result.append((fmt, level, val(definition.find('w:lvlText', NS)), start, number_id))
    return result


def merge_numbering(source, reference, mapping):
    result = deepcopy(source)
    remap_style_refs(result, mapping)
    for level in result.findall('w:abstractNum/w:lvl', NS):
        if val(level.find('w:numFmt', NS)) != 'bullet' or level.find('w:lvlPicBulletId', NS) is not None:
            continue
        index = min(int(val(level, 'ilvl', '0')), len(reference.bullet_levels) - 1)
        target = reference.bullet_levels[index]
        for name in ('lvlText', 'pPr', 'rPr'):
            remove(level, {name})
            item = target.find(f'{{{W}}}{name}')
            if item is not None:
                level.append(deepcopy(item))
    abstract_offset = max((int(val(n, 'abstractNumId')) for n in result.findall('w:abstractNum', NS)), default=-1) + 1
    num_offset = max((int(val(n, 'numId')) for n in result.findall('w:num', NS)), default=0) + 1
    abstract_map, num_map = {}, {}
    for i, old in enumerate(reference.numbering.findall('w:abstractNum', NS)):
        new = deepcopy(old)
        abstract_map[val(old, 'abstractNumId')] = str(abstract_offset + i)
        new.set(f'{{{W}}}abstractNumId', str(abstract_offset + i))
        result.insert(len(result.findall('w:abstractNum', NS)), new)
    for i, old in enumerate(reference.numbering.findall('w:num', NS)):
        new = deepcopy(old)
        num_map[val(old, 'numId')] = str(num_offset + i)
        new.set(f'{{{W}}}numId', str(num_offset + i))
        abstract = new.find('w:abstractNumId', NS)
        abstract.set(f'{{{W}}}val', abstract_map[val(abstract)])
        result.append(new)
    return result, num_map


def styles_for(source, reference, mapping, template_nums):
    result = deepcopy(reference.styles)
    for n in result.xpath('.//w:numPr/w:numId', namespaces=NS):
        if val(n) in template_nums:
            n.set(f'{{{W}}}val', template_nums[val(n)])
    canonical = {val(n, 'styleId'): n for n in result.findall('w:style', NS)}
    seen = set(canonical)
    for old in source.findall('w:style', NS):
        sid = val(old, 'styleId')
        if sid in seen:
            continue
        target = mapping.get(sid, sid)
        if target in canonical:
            alias = deepcopy(canonical[target])
            alias.set(f'{{{W}}}styleId', sid)
            name = alias.find('w:name', NS)
            if name is not None:
                name.set(f'{{{W}}}val', val(old.find('w:name', NS)) or sid)
        else:
            alias = deepcopy(old)
            remap_style_refs(alias, mapping)
            rpr = alias.find('w:rPr', NS)
            if rpr is not None:
                remove(rpr, {'rFonts', 'sz', 'szCs'})
        alias.attrib.pop(f'{{{W}}}default', None)
        result.append(alias)
        seen.add(sid)
    return result


def format_runs(paragraph, heading, table_header, in_table):
    runs = [r for r in paragraph.findall('.//w:r', NS)
            if next((a for a in r.iterancestors() if a.tag == f'{{{W}}}p'), None) is paragraph]
    all_rpr = list(paragraph.xpath('./w:pPr/w:rPr', namespaces=NS))
    all_rpr.extend(r.find('w:rPr', NS) for r in runs if r.find('w:rPr', NS) is not None)
    for props in all_rpr:
        font = props.find('w:rFonts', NS)
        symbol = font is not None and any(token in v.casefold() for v in font.attrib.values()
                                        for token in ('symbol', 'wingdings', 'cambria math'))
        remove(props, {'sz', 'szCs'} | (set() if symbol else {'rFonts'}))
        if heading:
            remove(props, {'color', 'b', 'bCs', 'i', 'iCs', 'caps', 'smallCaps', 'shd', 'highlight', 'bdr', 'spacing', 'position'})
            if val(props.find('w:rStyle', NS)) not in {'FootnoteReference', 'EndnoteReference'}:
                remove(props, {'rStyle'})
    if in_table:
        for run in runs:
            props = run.find('w:rPr', NS)
            if props is None:
                props = E.Element(f'{{{W}}}rPr'); run.insert(0, props)
            child(props, 'sz').set(f'{{{W}}}val', '19')
            child(props, 'szCs').set(f'{{{W}}}val', '19')
            if table_header:
                remove(props, {'color', 'highlight', 'shd'})
                child(props, 'color').set(f'{{{W}}}val', 'FFFFFF')
                child(props, 'b')


def format_paragraphs(document, reference, mapping, styles):
    for paragraph in document.findall('.//w:p', NS):
        if any(local(a) in {'txbxContent', 'textbox', 'txbx'} for a in paragraph.iterancestors()):
            continue
        props = paragraph.find('w:pPr', NS)
        if props is None:
            props = E.Element(f'{{{W}}}pPr'); paragraph.insert(0, props)
        pstyle = props.find('w:pStyle', NS)
        sid = val(pstyle) if pstyle is not None else 'Normal'
        sid = mapping.get(sid, sid)
        outline = val(props.find('w:outlineLvl', NS))
        if outline.isdigit() and int(outline) < 9:
            sid = f'Heading{int(outline) + 1}'
            if pstyle is None:
                pstyle = E.Element(f'{{{W}}}pStyle'); props.insert(0, pstyle)
        if pstyle is not None:
            pstyle.set(f'{{{W}}}val', sid)
        heading = bool(re.fullmatch(r'Heading[1-9]', sid) or sid.casefold().startswith('boldside') or sid == 'Title')
        in_table = any(local(a) == 'tc' for a in paragraph.iterancestors())
        row = next((a for a in paragraph.iterancestors() if local(a) == 'tr'), None)
        header = row is not None and (row.find('w:trPr/w:tblHeader', NS) is not None or row.getprevious() is None)
        if in_table:
            remove(props, {'cnfStyle'})
            if header:
                remove(props, {'shd', 'pBdr'})
        if heading:
            remove(props, {'spacing', 'ind', 'tabs', 'shd', 'pBdr', 'jc', 'contextualSpacing'})
            prototype = reference.body.xpath('./w:p[w:pPr/w:pStyle/@w:val=$s]', namespaces=NS, s=sid)
            if prototype:
                for extra in prototype[0].find('w:pPr', NS):
                    if local(extra) != 'pStyle':
                        remove(props, {local(extra)}); props.append(deepcopy(extra))
        else:
            remove(props, {'spacing'})
            props.append(deepcopy(reference.table_spacing if in_table else reference.body_spacing))
            definition = styles.xpath('./w:style[@w:styleId=$s]', namespaces=NS, s=sid)
            direct_list = props.find('w:numPr', NS)
            if direct_list is not None:
                is_list = val(direct_list.find('w:numId', NS)) not in {'', '0'}
            else:
                is_list = bool(definition and definition[0].find('w:pPr/w:numPr', NS) is not None)
            if is_list:
                remove(props, {'ind', 'tabs'})
        format_runs(paragraph, heading, header, in_table)


def format_tables(document, reference):
    for table in document.findall('.//w:tbl', NS):
        if any(local(a) in {'txbxContent', 'textbox', 'txbx'} for a in table.iterancestors()):
            continue
        props = table.find('w:tblPr', NS)
        if props is None:
            props = E.Element(f'{{{W}}}tblPr'); table.insert(0, props)
        remove(props, {'tblStyle', 'tblBorders', 'tblCellMar', 'shd', 'tblLook', 'tblInd', 'jc'})
        style = E.Element(f'{{{W}}}tblStyle', {f'{{{W}}}val': 'A1'}); props.insert(0, style)
        props.append(deepcopy(reference.example_table.find('w:tblPr/w:tblLook', NS)))
        props.append(deepcopy(reference.example_table.find('w:tblPr/w:tblInd', NS)))
        preferred = props.find('w:tblW', NS)
        if preferred is not None:
            if val(preferred, 'type') == 'dxa' and int(val(preferred, 'w', '0')) > reference.max_width:
                preferred.set(f'{{{W}}}w', str(reference.max_width))
            elif val(preferred, 'type') == 'pct' and int(val(preferred, 'w', '0')) > 5000:
                preferred.set(f'{{{W}}}w', '5000')
        grid = table.find('w:tblGrid', NS)
        total = sum(int(val(n, 'w', '0')) for n in grid) if grid is not None else 0
        ratio = min(1.0, reference.max_width / total) if total else 1.0
        if ratio < 1:
            used_width = 0
            for n in grid:
                new_width = max(1, round(int(val(n, 'w')) * ratio))
                if n is grid[-1]:
                    new_width = max(1, reference.max_width - used_width)
                used_width += new_width
                n.set(f'{{{W}}}w', str(new_width))
            width = props.find('w:tblW', NS)
            if width is not None and val(width, 'type') == 'dxa':
                width.set(f'{{{W}}}w', str(reference.max_width))
        for i, row in enumerate(table.findall('w:tr', NS)):
            rpr = row.find('w:trPr', NS)
            if rpr is not None:
                remove(rpr, {'cnfStyle'})
                for height in rpr.findall('w:trHeight', NS):
                    if val(height, 'hRule') == 'exact':
                        height.set(f'{{{W}}}hRule', 'atLeast')
            if i == 0:
                child(child(row, 'trPr'), 'tblHeader')
            for cell in row.findall('w:tc', NS):
                cpr = child(cell, 'tcPr')
                remove(cpr, {'shd', 'tcBorders', 'tcMar', 'cnfStyle'})
                cpr.append(deepcopy(reference.cell_margin))
                width = cpr.find('w:tcW', NS)
                if ratio < 1 and width is not None and val(width, 'type') == 'dxa':
                    width.set(f'{{{W}}}w', str(max(1, round(int(val(width, 'w', '0')) * ratio))))


def add_relationship(rels, kind, target, external=False):
    base, i = 'rIdClinicalTemplate', 1
    used = {n.get('Id') for n in rels}
    while base + str(i) in used:
        i += 1
    rid = base + str(i)
    attrs = {'Id': rid, 'Type': R + '/' + kind, 'Target': target}
    if external:
        attrs['TargetMode'] = 'External'
    E.SubElement(rels, f'{{{PKG}}}Relationship', attrs)
    return rid


def fit_images(document, reference):
    wp = 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'
    a = 'http://schemas.openxmlformats.org/drawingml/2006/main'
    maximum = reference.max_width * 635
    for extent in document.findall(f'.//{{{wp}}}extent'):
        width, height = int(extent.get('cx')), int(extent.get('cy'))
        if width <= maximum:
            continue
        ratio = maximum / width
        extent.set('cx', str(maximum)); extent.set('cy', str(round(height * ratio)))
        for shape_extent in extent.getparent().findall(f'.//{{{a}}}xfrm/{{{a}}}ext'):
            if shape_extent.get('cx') == str(width) and shape_extent.get('cy') == str(height):
                shape_extent.set('cx', str(maximum)); shape_extent.set('cy', str(round(height * ratio)))
    v = 'urn:schemas-microsoft-com:vml'
    max_points = reference.max_width / 20
    for shape in document.findall(f'.//{{{v}}}shape'):
        if shape.find(f'{{{v}}}imagedata') is None:
            continue
        style = shape.get('style', '')
        width = re.search(r'(?:^|;)width:([\d.]+)pt', style)
        height = re.search(r'(?:^|;)height:([\d.]+)pt', style)
        if width and height and float(width.group(1)) > max_points:
            ratio = max_points / float(width.group(1))
            style = re.sub(r'((?:^|;)width:)[\d.]+pt', lambda m: m.group(1) + f'{max_points:.3f}pt', style)
            style = re.sub(r'((?:^|;)height:)[\d.]+pt', lambda m: m.group(1) + f'{float(height.group(1)) * ratio:.3f}pt', style)
            shape.set('style', style)


def apply_one(source, target, reference):
    before = read(source); after = dict(before)
    root = xml(before['word/document.xml'])
    if not root.findall('.//w:sectPr', NS):
        root.find('w:body', NS).append(deepcopy(reference.section))
    original_signature = signature(root)
    original_styles = xml(before['word/styles.xml'])
    mapping = reference.map_styles(original_styles)
    numbering = xml(before['word/numbering.xml']) if 'word/numbering.xml' in before else E.Element(f'{{{W}}}numbering')
    original_lists = list_signature(root, original_styles, numbering)
    preserve_source_list_properties(root, original_styles)
    numbering, nums = merge_numbering(numbering, reference, mapping)
    styles = styles_for(original_styles, reference, mapping, nums)
    remap_style_refs(root, mapping)
    format_tables(root, reference)
    format_paragraphs(root, reference, mapping, styles)
    fit_images(root, reference)
    rels = xml(before['word/_rels/document.xml.rels'])
    footer_name = 'word/clinicalTemplateFooter.xml'
    assert footer_name not in before, 'Already formatted by this operation'
    footer_rid = add_relationship(rels, 'footer', 'clinicalTemplateFooter.xml')
    for section in root.findall('.//w:sectPr', NS):
        remove(section, {'pgSz', 'pgMar', 'cols', 'docGrid', 'footerReference', 'titlePg'})
        section.insert(0, E.Element(f'{{{W}}}footerReference', {f'{{{W}}}type': 'default', f'{{{R}}}id': footer_rid}))
        for name in ('pgSz', 'pgMar', 'cols', 'docGrid'):
            node = reference.section.find(f'{{{W}}}{name}')
            if node is not None:
                section.append(deepcopy(node))
    settings = xml(before['word/settings.xml']) if 'word/settings.xml' in before else E.Element(f'{{{W}}}settings', nsmap={'w': W, 'r': R})
    remove(settings, {'attachedTemplate', 'linkStyles', 'updateFields', 'evenAndOddHeaders'})
    settings_rels_name = 'word/_rels/settings.xml.rels'
    settings_rels = xml(before[settings_rels_name]) if settings_rels_name in before else E.Element(f'{{{PKG}}}Relationships', nsmap={None: PKG})
    template_rid = add_relationship(settings_rels, 'attachedTemplate', reference.path.as_uri(), True)
    E.SubElement(settings, f'{{{W}}}attachedTemplate', {f'{{{R}}}id': template_rid})
    # Styles are already applied. Keep Word from remapping preserved list IDs
    # through an automatic style update on a later document open.
    E.SubElement(settings, f'{{{W}}}linkStyles', {f'{{{W}}}val': 'false'})
    E.SubElement(settings, f'{{{W}}}updateFields', {f'{{{W}}}val': 'true'})
    order_properties(root)
    order_properties(styles)
    order_properties(numbering)
    content_types = xml(before['[Content_Types].xml'])
    E.SubElement(content_types, f'{{{CT}}}Override', {
        'PartName': '/' + footer_name,
        'ContentType': 'application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml'})
    if 'word/settings.xml' not in before:
        add_relationship(rels, 'settings', 'settings.xml')
        E.SubElement(content_types, f'{{{CT}}}Override', {'PartName': '/word/settings.xml',
            'ContentType': 'application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml'})
    if 'word/numbering.xml' not in before:
        add_relationship(rels, 'numbering', 'numbering.xml')
        E.SubElement(content_types, f'{{{CT}}}Override', {'PartName': '/word/numbering.xml',
            'ContentType': 'application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml'})
    after.update({'word/document.xml': serialize(root), 'word/styles.xml': serialize(styles),
                  'word/numbering.xml': serialize(numbering), 'word/settings.xml': serialize(settings),
                  'word/_rels/document.xml.rels': serialize(rels), settings_rels_name: serialize(settings_rels),
                  '[Content_Types].xml': serialize(content_types), footer_name: reference.parts['word/footer1.xml']})
    themes = [name for name in before if re.fullmatch(r'word/theme/theme\d+\.xml', name)]
    for name in themes:
        after[name] = reference.parts['word/theme/theme1.xml']
    if not themes:
        after['word/theme/theme1.xml'] = reference.parts['word/theme/theme1.xml']
        add_relationship(rels, 'theme', 'theme/theme1.xml')
        E.SubElement(content_types, f'{{{CT}}}Override', {'PartName': '/word/theme/theme1.xml',
            'ContentType': 'application/vnd.openxmlformats-officedocument.theme+xml'})
    if 'word/fontTable.xml' in before:
        fonts = xml(before['word/fontTable.xml']); names = {val(n, 'name') for n in fonts}
        for font in xml(reference.parts['word/fontTable.xml']):
            if val(font, 'name') not in names:
                fonts.append(deepcopy(font))
        after['word/fontTable.xml'] = serialize(fonts)
    else:
        after['word/fontTable.xml'] = reference.parts['word/fontTable.xml']
        add_relationship(rels, 'fontTable', 'fontTable.xml')
        E.SubElement(content_types, f'{{{CT}}}Override', {'PartName': '/word/fontTable.xml',
            'ContentType': 'application/vnd.openxmlformats-officedocument.wordprocessingml.fontTable+xml'})
    after['word/_rels/document.xml.rels'] = serialize(rels)
    after['[Content_Types].xml'] = serialize(content_types)
    assert signature(root) == original_signature, f'Content/structure loss: {source}'
    actual_lists = list_signature(root, styles, numbering)
    assert original_lists == actual_lists, ('List numbering/nesting changed', source,
        [(a, b) for a, b in zip(original_lists, actual_lists) if a != b][:3])
    for name, data in before.items():
        if name.startswith(('word/media/', 'word/embeddings/', 'word/charts/', 'word/diagrams/', 'customXml/')):
            assert after[name] == data, name
    for name, data in after.items():
        if name.endswith('.rels'):
            directory = posixpath.dirname(posixpath.dirname(name))
            for rel in xml(data):
                if rel.get('TargetMode') != 'External':
                    resolved = posixpath.normpath(posixpath.join(directory, rel.get('Target'))).lstrip('/')
                    assert resolved in after, (source, name, resolved)
    ids = [val(n, 'styleId') for n in styles.findall('w:style', NS)]
    assert len(ids) == len(set(ids))
    for n in root.xpath('//w:pStyle | //w:rStyle | //w:tblStyle', namespaces=NS):
        assert val(n) in ids, (source, val(n))
    target.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(source) as old, ZipFile(target, 'w') as new:
        new.comment = old.comment
        for info in old.infolist():
            new.writestr(info, after.pop(info.filename))
        for name, data in after.items():
            new.writestr(name, data)
    assert has_opening_h1(target), source
    assert sha(reference.path) == reference.sha
    return {'paragraphs': original_signature[0]['p'], 'tables': original_signature[0]['tbl'],
            'mediaParts': sum(n.startswith('word/media/') for n in before)}


def stage(data, output, template_path):
    reference = Template(template_path)
    root = data / 'files'
    files = sorted(p for subject in root.iterdir() if subject.is_dir() and not subject.name.startswith(('_', '.'))
                   for p in subject.glob('*.docx') if not p.name.startswith('~$'))
    output.mkdir(parents=True, exist_ok=True)
    report = {'template': str(template_path), 'templateHash': reference.sha, 'files': [],
              'visualQA': 'Unavailable: LibreOffice soffice.exe is not installed.'}
    for index, source in enumerate(files, 1):
        relative = source.relative_to(root)
        original_hash = sha(source)
        target = output / 'documents' / relative
        counts = apply_one(source, target, reference)
        assert sha(source) == original_hash, f'Concurrent source edit: {source}'
        report['files'].append({'path': relative.as_posix(), 'originalHash': original_hash,
                                'formattedHash': sha(target), **counts})
        if index % 20 == 0 or index == len(files):
            print(f'Formatted and verified {index}/{len(files)} files.', flush=True)
    report['filesFormatted'] = len(files)
    report['preservation'] = 'All body text in order, table structure, merges, object counts, media bytes and links verified.'
    (output / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({k: v for k, v in report.items() if k != 'files'}, indent=2), flush=True)


def install(data, output):
    report_path = output / 'report.json'
    report = json.loads(report_path.read_text(encoding='utf-8'))
    assert sha(Path(report['template'])) == report['templateHash']
    root = (data / 'files').resolve()
    for row in report['files']:
        source = root / row['path']; staged = output / 'documents' / row['path']
        assert source.resolve().is_relative_to(root)
        assert sha(source) == row['originalHash'], f'Source changed after preparation: {source}'
        assert sha(staged) == row['formattedHash'], f'Staged file changed: {staged}'
        try:
            with source.open('r+b'):
                pass
        except PermissionError as exc:
            raise PermissionError(f'Close this Word document before installing: {source}') from exc
    backup = data / 'backups' / f'clinical-template-before-application-{time.time_ns()}.zip'
    backup.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(backup, 'x') as z:
        z.writestr('template-application-manifest.json', json.dumps(report, ensure_ascii=False, indent=2))
        for row in report['files']:
            z.write(root / row['path'], row['path'])
    with ZipFile(backup) as z:
        for row in report['files']:
            assert hashlib.sha256(z.read(row['path'])).hexdigest() == row['originalHash']
    written = []
    try:
        for row in report['files']:
            source = root / row['path']; staged = output / 'documents' / row['path']
            assert sha(source) == row['originalHash'], f'Concurrent edit: {source}'
            written.append(row)
            shutil.copyfile(staged, source)
            assert sha(source) == row['formattedHash']
        assert all(has_opening_h1(root / row['path']) for row in report['files'])
    except Exception:
        with ZipFile(backup) as z:
            for row in written:
                (root / row['path']).write_bytes(z.read(row['path']))
        raise
    report.update(installed=True, backup=str(backup), allFilesStartWithH1=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Applied template to {len(report["files"])} documents. Verified backup: {backup}', flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=Path, default=DEFAULT_DATA)
    parser.add_argument('--template', type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument('--output', type=Path, default=ROOT / 'build/clinical-template-application')
    parser.add_argument('--install', action='store_true')
    args = parser.parse_args()
    if args.install:
        install(args.data.resolve(), args.output.resolve())
    else:
        stage(args.data.resolve(), args.output.resolve(), args.template.resolve())
