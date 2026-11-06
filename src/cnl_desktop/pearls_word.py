"""Convert authored Pearls HTML to editable Word, preserving text and structure."""
import copy
import re
import io
from lxml import html
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

SUB=dict(zip('₀₁₂₃₄₅₆₇₈₉₊₋','0123456789+-'))
SUP=dict(zip('⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻','0123456789+-'))


def canonical(text):
    return re.sub(r'\s+','', ''.join(SUB.get(c,SUP.get(c,c)) for c in text))


class Converter:
    def __init__(self):
        self.doc=Document()
        self.num=200
        sec=self.doc.sections[0]
        sec.page_width=Inches(8.27);sec.page_height=Inches(11.69)
        sec.top_margin=sec.bottom_margin=Inches(.6)
        sec.left_margin=sec.right_margin=Inches(.65)
        normal=self.doc.styles['Normal']
        normal.font.name='Averia Serif Libre';normal.font.size=Pt(11.5)
        normal.font.color.rgb=RGBColor.from_string('242348')
        normal.paragraph_format.line_spacing=1.2
        normal.paragraph_format.space_after=Pt(6)
        normal.paragraph_format.widow_control=True
        for name,size,color in [('Title',23,'000000'),('Heading 1',15,'242348'),
                                ('Heading 2',12.5,'24568C'),('Heading 3',11.5,'24568C')]:
            style=self.doc.styles[name]
            style.font.name='Averia Serif Libre';style.font.size=Pt(size)
            style.font.bold=True;style.font.color.rgb=RGBColor.from_string(color)
            style.paragraph_format.keep_with_next=True
            style.paragraph_format.space_before=Pt(12)
            style.paragraph_format.space_after=Pt(6)
            if name=='Heading 1':
                shading=OxmlElement('w:shd');shading.set(qn('w:fill'),'F8DFEB')
                style.element.get_or_add_pPr().append(shading)
        self.doc.core_properties.author=''
        self.doc.core_properties.last_modified_by=''
        for style in self.doc.styles:
            for border in list(style.element.iter(qn('w:pBdr'))):border.getparent().remove(border)

    def text(self,p,text,bold=False,italic=False,script=None):
        if not text:return
        parts=[]
        for c in text:
            mode='subscript' if c in SUB else 'superscript' if c in SUP else script
            c=SUB.get(c,SUP.get(c,c))
            if parts and parts[-1][0]==mode:parts[-1][1]+=c
            else:parts.append([mode,c])
        for mode,part in parts:
            run=p.add_run(part)
            if bold:run.bold=True
            if italic:run.italic=True
            if mode: setattr(run.font,mode,True)

    def inline(self,p,node,bold=False,italic=False,script=None):
        bold=bold or node.tag in ('strong','b')
        italic=italic or node.tag in ('em','i')
        script={'sup':'superscript','sub':'subscript'}.get(node.tag,script)
        self.text(p,node.text,bold,italic,script)
        for child in node:
            if child.tag=='br':p.add_run().add_break()
            elif child.tag not in ('ul','ol','table'):self.inline(p,child,bold,italic,script)
            self.text(p,child.tail,bold,italic,script)

    def numbering(self,ordered):
        self.num+=1
        abstract=OxmlElement('w:abstractNum');abstract.set(qn('w:abstractNumId'),str(self.num))
        for depth in range(3):
            lvl=OxmlElement('w:lvl');lvl.set(qn('w:ilvl'),str(depth))
            for tag,value in [('start','1'),('numFmt','decimal' if ordered else 'bullet'),
                              ('lvlText',f'%{depth+1}.' if ordered else ('•' if depth==0 else '○'))]:
                item=OxmlElement('w:'+tag);item.set(qn('w:val'),value);lvl.append(item)
            pp=OxmlElement('w:pPr');indent=OxmlElement('w:ind')
            indent.set(qn('w:left'),str(300+depth*260));indent.set(qn('w:hanging'),'220')
            pp.append(indent);lvl.append(pp);abstract.append(lvl)
        numbering=self.doc.part.numbering_part.element
        # OOXML requires every abstractNum before every concrete num. Word can
        # silently substitute its default bullet format when they are interleaved.
        first_num=numbering.find(qn('w:num'))
        numbering.insert(list(numbering).index(first_num) if first_num is not None else len(numbering),abstract)
        num=OxmlElement('w:num');num.set(qn('w:numId'),str(self.num))
        aid=OxmlElement('w:abstractNumId');aid.set(qn('w:val'),str(self.num));num.append(aid)
        override=OxmlElement('w:lvlOverride');override.set(qn('w:ilvl'),'0')
        start=OxmlElement('w:startOverride');start.set(qn('w:val'),'1');override.append(start);num.append(override)
        numbering.append(num)
        return self.num

    def listing(self,parent,node,depth=0):
        number=self.numbering(node.tag=='ol')
        for item in node:
            if item.tag!='li':continue
            p=parent.add_paragraph();self.inline(p,item)
            p.paragraph_format.space_after=Pt(3)
            np=OxmlElement('w:numPr')
            for tag,value in [('ilvl',str(min(depth,2))),('numId',str(number))]:
                element=OxmlElement('w:'+tag);element.set(qn('w:val'),value);np.append(element)
            p._p.get_or_add_pPr().append(np)
            for nested in item:
                if nested.tag in ('ul','ol'):self.listing(parent,nested,depth+1)

    def table(self,parent,node):
        rows=node.xpath('./tr|./thead/tr|./tbody/tr|./tfoot/tr')
        if not rows:return
        count=max(sum(int(c.get('colspan',1)) for c in row if c.tag in ('td','th')) for row in rows)
        table=parent.add_table(rows=len(rows),cols=count)
        table.autofit=False;table.style='Table Grid'
        lengths=[8]*count
        for row in rows:
            for i,cell in enumerate(row):
                if i<count:lengths[i]=max(lengths[i],min(100,len(cell.text_content())))
        weights=[max(18,min(75,n)) for n in lengths];widths=[6.97*n/sum(weights) for n in weights]
        if count>=3 and widths[0]<1.45:
            remaining=6.97-1.45
            scale=remaining/sum(widths[1:])
            widths=[1.45,*[width*scale for width in widths[1:]]]
        for col,width in zip(table.columns,widths):col.width=Inches(width)
        for i,(row,tr) in enumerate(zip(table.rows,rows)):
            keep=OxmlElement('w:cantSplit');row._tr.get_or_add_trPr().append(keep)
            cells=[c for c in tr if c.tag in ('td','th')]
            header=any(c.tag=='th' for c in cells)
            if header:
                repeat=OxmlElement('w:tblHeader');row._tr.get_or_add_trPr().append(repeat)
            column=0
            for source in cells:
                span=int(source.get('colspan',1))
                cell=row.cells[column]
                if span>1:cell=cell.merge(row.cells[column+span-1])
                cell.width=Inches(sum(widths[column:column+span]));column+=span
                cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
                p=cell.paragraphs[0];self.inline(p,source,bold=header)
                p.paragraph_format.space_after=Pt(3);p.paragraph_format.line_spacing=1.1
                for run in p.runs:run.font.size=Pt(10)
                props=cell._tc.get_or_add_tcPr()
                margins=OxmlElement('w:tcMar')
                for edge in ('top','bottom','left','right'):
                    part=OxmlElement('w:'+edge);part.set(qn('w:w'),'90');part.set(qn('w:type'),'dxa');margins.append(part)
                props.append(margins)
                if header:
                    fill=OxmlElement('w:shd');fill.set(qn('w:fill'),'ECF1FA');props.append(fill)
        border=OxmlElement('w:tblBorders')
        for edge in ('top','bottom','left','right','insideH','insideV'):
            side=OxmlElement('w:'+edge)
            for key,val in [('val','single'),('sz','4'),('color','D9D9D9')]:side.set(qn('w:'+key),val)
            border.append(side)
        table._tbl.tblPr.append(border)
        parent.add_paragraph().paragraph_format.space_after=Pt(3)

    def blocks(self,parent,node):
        if node.tag in ('style','script','nav'):return
        if node.tag in ('ul','ol'):self.listing(parent,node);return
        if node.tag=='table':self.table(parent,node);return
        if node.tag in ('h1','h2','h3','h4','p','summary'):
            style={'h1':'Title','h2':'Heading 1','h3':'Heading 2','h4':'Heading 3','summary':'Heading 2'}.get(node.tag)
            p=parent.add_paragraph(style=style);self.inline(p,node);return
        if node.text and node.text.strip():
            self.text(parent.add_paragraph(),node.text)
        for child in node:
            self.blocks(parent,child)
            if child.tail and child.tail.strip():self.text(parent.add_paragraph(),child.tail)


def to_docx(source):
    """Build a Word document in memory; HTML scripts and navigation are omitted."""
    tree=html.fromstring(source,parser=html.HTMLParser(no_network=True))
    main=tree if tree.tag=='main' else tree.find('.//main')
    if main is None:main=tree if tree.tag=='body' else tree.find('.//body')
    if main is None:main=tree
    main=copy.deepcopy(main)
    for nav in main.xpath('.//nav|.//script|.//style|.//iframe|.//object'):nav.drop_tree()
    for title in main.xpath('./h1[1]'):title.drop_tree()
    for references in main.xpath('.//section[@id="references"]'):references.drop_tree()
    builder=Converter();builder.blocks(builder.doc,main)
    expected=canonical(main.text_content())
    actual=canonical(''.join(builder.doc.element.body.xpath('.//w:t/text()')))
    if actual!=expected:raise ValueError('This HTML contains a structure that could not be preserved in Word.')
    output=io.BytesIO();builder.doc.save(output)
    check=Document(io.BytesIO(output.getvalue()))
    if canonical(''.join(check.element.body.xpath('.//w:t/text()')))!=expected:
        raise ValueError('Could not verify the converted note.')
    return output.getvalue(),dict(tables=len(check.tables),paragraphs=len(check.paragraphs))


def convert(source,destination):
    data,stats=to_docx(source.read_text(encoding='utf-8-sig'))
    destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_bytes(data)
    return dict(file=str(destination),source=str(source),**stats)
