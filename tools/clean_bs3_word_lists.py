"""Make Word BS3 headings independent of list styles and no-list markers."""
from copy import copy
import json
from zipfile import ZipFile
from apply_clinical_template import DEFAULT_DATA, ROOT, NS, W, read, xml, val, serialize, signature, list_signature, sha, order_properties


def main():
    output=ROOT/'build/portable-bs3';output.mkdir(parents=True,exist_ok=True)
    reports=[]
    for source in sorted((DEFAULT_DATA/'files').rglob('*.docx')):
        relative=source.relative_to(DEFAULT_DATA/'files')
        if source.name.startswith('~$') or ' old' in source.stem.lower() or any(p.startswith(('_','.')) for p in relative.parts[:-1]):continue
        data=read(source);d=xml(data['word/document.xml']);s=xml(data['word/styles.xml'])
        n=xml(data.get('word/numbering.xml',f'<w:numbering xmlns:w="{W}"/>'.encode()))
        ps=d.findall('.//w:p',NS)
        headings=[p for p in ps if val(p.find('w:pPr/w:pStyle',NS))=='Boldside3']
        if not headings:continue
        styles={val(x,'styleId'):x for x in s.findall('w:style',NS)}
        style=styles.get('Boldside3')
        if style is None:continue
        content=signature(d);lists=list_signature(d,s,n);changes=[]
        base=style.find('w:basedOn',NS)
        # Explicit BS3 font/colour/spacing stay intact; eliminate list inheritance.
        if base is not None and val(base)!='Normal':
            changes.append(dict(style='Boldside3',before=val(base),after='Normal'))
            base.set(f'{{{W}}}val','Normal')
        for node in style.findall('w:pPr/w:numPr',NS):
            node.getparent().remove(node)
            changes.append(dict(style='Boldside3',removedStyleNumbering=True))
        for p in headings:
            num=p.find('w:pPr/w:numPr',NS)
            if num is not None and val(num.find('w:numId',NS))=='0':
                # Do not silently discard numbering revision records.
                if any(x.tag not in (f'{{{W}}}numId',f'{{{W}}}ilvl') for x in num):continue
                num.getparent().remove(num)
                changes.append(dict(text=''.join(p.xpath('.//w:t/text()',namespaces=NS)),removedNoListMarker=True))
        if not changes:continue
        order_properties(d);order_properties(s)
        assert signature(d)==content
        assert list_signature(d,s,n)==lists,source
        destination=output/relative;destination.parent.mkdir(parents=True,exist_ok=True)
        replacements={'word/document.xml':serialize(d),'word/styles.xml':serialize(s)}
        with ZipFile(source) as z,ZipFile(destination,'w') as out:
            out.comment=z.comment
            for info in z.infolist():out.writestr(copy(info),replacements.get(info.filename,z.read(info.filename)))
        verified=read(destination)
        assert all(verified[k]==v for k,v in data.items() if k not in replacements)
        reports.append(dict(file=relative.as_posix(),before=sha(source),staged=sha(destination),changed=True,changes=changes))
    (output/'report.json').write_text(json.dumps(reports,indent=2),encoding='utf-8')
    print(json.dumps(dict(files=len(reports),headingsCleaned=sum(sum(bool(c.get('removedNoListMarker')) for c in r['changes']) for r in reports))))


if __name__=='__main__':main()
