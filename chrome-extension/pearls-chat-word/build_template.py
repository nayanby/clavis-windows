"""Create a content-free DOCX template and icons from the retained Word template."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from copy import deepcopy
import hashlib
import json
from lxml import etree as E
from PIL import Image, ImageDraw

HERE=Path(__file__).resolve().parent
SOURCE=Path('C:/Users/ANT-PC/OneDrive/Clinical Notes Formatter/Clinical Notes Templatex.dotx')
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
R='http://schemas.openxmlformats.org/officeDocument/2006/relationships'
NS={'w':W}
def serialize(node):return E.tostring(node,encoding='UTF-8',xml_declaration=True,standalone=True)
def tag(name):return '{'+W+'}'+name

def main():
    output=HERE/'template';output.mkdir(exist_ok=True)
    with ZipFile(SOURCE) as source:
        styles=E.fromstring(source.read('word/styles.xml'))
        original=E.fromstring(source.read('word/document.xml'))
        section=deepcopy(original.find('w:body/w:sectPr',NS))
        # Page geometry comes from the reference. Export documents have no sample footer.
        for name in ('footerReference','headerReference'):
            for node in section.findall('w:'+name,NS):section.remove(node)
        for element in styles.iter():
            for attr in list(element.attrib):
                if E.QName(attr).localname.startswith('rsid'):del element.attrib[attr]
        for node in list(styles.iter(tag('rsid'))):node.getparent().remove(node)
        for style in styles.findall('w:style',NS):
            # Native lists always get explicit numPr. No paragraph style supplies one.
            for node in style.findall('w:pPr/w:numPr',NS):node.getparent().remove(node)
            sid=style.get(tag('styleId'),'')
            if sid=='Boldside3':style.find('w:basedOn',NS).set(tag('val'),'Normal')
            if sid in {'Heading1','Heading2','Heading3','Heading4','BoldSide1','boldside2','Boldside3','boldside4'}:
                props=style.find('w:pPr',NS)
                if props is None:props=E.SubElement(style,tag('pPr'))
                if props.find('w:keepNext',NS) is None:props.insert(0,E.Element(tag('keepNext')))
        # Auxiliary roles never enter the medical-heading outline.
        for sid,name,extra in [('ChatRole','Chat speaker','<w:b/><w:color w:val="5C3A52"/>'),('ChatMetadata','Chat source','<w:color w:val="666666"/><w:sz w:val="18"/>'),('ChatCode','Chat code','<w:rFonts w:ascii="Consolas" w:hAnsi="Consolas"/><w:sz w:val="19"/>')]:
            node=E.fromstring(f'<w:style xmlns:w="{W}" w:type="paragraph" w:customStyle="1" w:styleId="{sid}"><w:name w:val="{name}"/><w:basedOn w:val="Normal"/><w:pPr><w:spacing w:before="80" w:after="60"/></w:pPr><w:rPr>{extra}</w:rPr></w:style>')
            styles.append(node)
        document=E.Element(tag('document'),nsmap={'w':W,'r':R});body=E.SubElement(document,tag('body'));body.append(E.Element(tag('p')));body.append(section)
        normal=styles.find('w:style[@w:styleId="Normal"]',NS)
        halfpoints=int(normal.find('w:rPr/w:sz',NS).get(tag('val')))
        page=section.find('w:pgSz',NS);margins=section.find('w:pgMar',NS)
        profile=dict(bodyHalfPoints=halfpoints,contentWidthTwips=int(page.get(tag('w')))-int(margins.get(tag('left')))-int(margins.get(tag('right'))),font='Averia Serif Libre',template='Clinical Notes Templatex',templateSHA256=hashlib.sha256(SOURCE.read_bytes()).hexdigest())
        types='''<?xml version="1.0" encoding="UTF-8"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Default Extension="png" ContentType="image/png"/>'''
        parts={'document':'application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml','styles':'application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml','numbering':'application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml','fontTable':'application/vnd.openxmlformats-officedocument.wordprocessingml.fontTable+xml','settings':'application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml'}
        for name,mime in parts.items():types+=f'<Override PartName="/word/{name}.xml" ContentType="{mime}"/>'
        types+='<Override PartName="/word/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/><Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/></Types>'
        relns='http://schemas.openxmlformats.org/package/2006/relationships'
        rootrels=f'<Relationships xmlns="{relns}"><Relationship Id="rId1" Type="{R}/officeDocument" Target="word/document.xml"/><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/></Relationships>'
        docrels=f'<Relationships xmlns="{relns}">'
        for i,(name,target) in enumerate([('styles','styles.xml'),('numbering','numbering.xml'),('fontTable','fontTable.xml'),('settings','settings.xml'),('theme','theme/theme1.xml')],1):docrels+=f'<Relationship Id="rId{i}" Type="{R}/{name}" Target="{target}"/>'
        docrels+='</Relationships>'
        with ZipFile(output/'base.docx','w',ZIP_DEFLATED) as z:
            for name,value in {'[Content_Types].xml':types,'_rels/.rels':rootrels,'word/document.xml':serialize(document),'word/styles.xml':serialize(styles),'word/numbering.xml':f'<w:numbering xmlns:w="{W}"/>','word/_rels/document.xml.rels':docrels,'word/settings.xml':f'<w:settings xmlns:w="{W}"><w:updateFields w:val="true"/></w:settings>','docProps/core.xml':'<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties"/>'}.items():z.writestr(name,value)
            for name in ('word/theme/theme1.xml','word/fontTable.xml'):z.writestr(name,source.read(name))
    (output/'profile.json').write_text(json.dumps(profile,indent=2),encoding='utf-8')
    icons=HERE/'icons';icons.mkdir(exist_ok=True)
    for size in (16,32,48,128):
        image=Image.new('RGBA',(256,256),(0,0,0,0));draw=ImageDraw.Draw(image)
        draw.rounded_rectangle((4,4,252,252),radius=52,fill='#6F3D5D')
        draw.rounded_rectangle((70,40,188,216),radius=12,fill='white')
        for y in (92,120,148,176):draw.rounded_rectangle((91,y,165,y+8),radius=4,fill='#294C7B')
        image.resize((size,size),Image.Resampling.LANCZOS).save(icons/f'{size}.png')
    (HERE/'artifact.md').write_text(f'''# Template contract

Reference: Clinical Notes Templatex.dotx. SHA-256: {profile['templateSHA256']}.
Retained source is unchanged. The bundled base.docx contains no example content or personal metadata.

Page: {page.get(tag('w'))} × {page.get(tag('h'))} twips; margins copied from reference.
Body: Averia Serif Libre, {halfpoints/2:g} pt. Tables: {halfpoints/2-1:g} pt.
Original named Heading1–4, BoldSide1, boldside2, Boldside3, level1–3 and emphasis styles retained.
BS3 inherits Normal. All style numPr removed; real body lists receive explicit numbering only.
Heading1 is white on plum; Heading2 plum on mauve; Heading3 navy on pale blue;
BoldSide1 uppercase plum with bottom rule; BS2 unshaded plum; BS3 unshaded navy.
Body bold runs use the template SubtleEmphasis navy. Selected source highlights are pastel yellow.
Lists: filled circle, hollow circle, square; nested ordered sequences remain native Word lists.
All abstract numbering definitions precede num instances. A fresh num instance restarts each list.
Only the document title uses H1. Roman sections use H2 and lettered subsections H3.
Source heading prefixes are preserved exactly; automatic heading numbering is disabled.
Tables: repeating header row, light borders, template colours, cell spans and native editable text.
Section geometry, style properties, theme and font table come from the retained reference.
Sample content, sample footer, editing identifiers and user metadata are excluded.
Images are embedded PNG when readable; otherwise a labelled source link and explicit warning remain.
Equations retain their LaTeX/text representation. No AI rewriting is performed.
Visual render gate is attempted with the bundled document renderer; report any unavailable renderer.
''',encoding='utf-8')
    print('Created sanitized Word template, profile, style contract and icons.')

if __name__=='__main__':main()
