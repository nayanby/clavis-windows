"""Verify real exported OOXML packages, including heading/list separation."""
from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
from docx import Document
import posixpath
from io import BytesIO
from PIL import Image

ROOT=Path(__file__).resolve().parents[3]
NS={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
W=NS['w']
R='http://schemas.openxmlformats.org/package/2006/relationships'
for path in sorted((ROOT/'build/chat-word-qa').glob('*.docx')):
    with ZipFile(path) as z:
        assert z.testzip() is None
        for name in z.namelist():
            if name.endswith(('.xml','.rels')):E.fromstring(z.read(name))
        d=E.fromstring(z.read('word/document.xml'));s=E.fromstring(z.read('word/styles.xml'));n=E.fromstring(z.read('word/numbering.xml'))
        types=z.read('[Content_Types].xml')
        assert b'wordprocessingml.document.main+xml' in types
        assert b'template.main+xml' not in types
        for style in s.findall('w:style',NS):assert style.find('w:pPr/w:numPr',NS) is None
        bs3=s.find('w:style[@w:styleId="Boldside3"]/w:basedOn',NS)
        assert bs3.get('{'+W+'}val')=='Normal'
        headings=0
        for p in d.findall('.//w:p',NS):
            sid=p.find('w:pPr/w:pStyle',NS)
            if sid is not None and sid.get('{'+W+'}val') in ('Heading1','Heading2','Heading3','Heading4','BoldSide1','boldside2','Boldside3'):
                headings+=1;assert p.find('w:pPr/w:numPr',NS) is None
        assert headings>=5
        # Native body lists still have actual nonzero numbering references.
        num_ids={x.get('{'+W+'}numId') for x in n.findall('w:num',NS)}
        for num in d.findall('.//w:numPr/w:numId',NS):assert num.get('{'+W+'}val') in num_ids
        seen_num=False
        for child in n:
            if E.QName(child).localname=='num':seen_num=True
            if E.QName(child).localname=='abstractNum':assert not seen_num
        for p in d.findall('.//w:tc//w:p',NS):
            for run in p.findall('w:r',NS):
                if run.find('w:t',NS) is not None:
                    assert run.find('w:rPr/w:sz',NS).get('{'+W+'}val')=='19'
        for rel in E.fromstring(z.read('word/_rels/document.xml.rels')):
            if rel.get('TargetMode')=='External':continue
            assert posixpath.normpath('word/'+rel.get('Target')) in z.namelist()
        assert z.namelist().count('word/media/image1.png')==1
        Image.open(BytesIO(z.read('word/media/image1.png'))).verify()
        assert d.find('.//w:tbl/w:tr/w:trPr/w:tblHeader',NS) is not None
    opened=Document(path)
    assert len(opened.tables)==1
    print('PASS',path.name,'headings:',headings,'paragraphs:',len(opened.paragraphs),'native tables:',len(opened.tables))
