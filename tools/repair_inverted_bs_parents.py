"""Promote uppercase BS3 parents above their explicitly lettered children."""
import argparse
from copy import copy
import json
import re
import time
from zipfile import ZipFile
from apply_clinical_template import DEFAULT_DATA, ROOT, NS, W, read, xml, val, serialize, signature, list_signature, sha, order_properties
from audit_document_headings import RANK


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--install-staged',action='store_true');args=parser.parse_args()
    output=ROOT/'build/inverted-bs-parents';output.mkdir(parents=True,exist_ok=True)
    if args.install_staged:
        from repair_unintended_emphasis import install
        install(DEFAULT_DATA,output)
        return
    reports=[]
    for source in sorted((DEFAULT_DATA/'files').rglob('*.docx')):
        relative=source.relative_to(DEFAULT_DATA/'files')
        if source.name.startswith('~$') or re.search(r'\bold\b',source.stem,re.I) or any(p.startswith(('_','.')) for p in relative.parts[:-1]):continue
        data=read(source);d=xml(data['word/document.xml']);s=xml(data['word/styles.xml'])
        n=xml(data.get('word/numbering.xml',f'<w:numbering xmlns:w="{W}"/>'.encode()))
        ps=d.findall('.//w:p',NS);before=signature(d);lists=list_signature(d,s,n)
        rows=[]
        for i,p in enumerate(ps):
            if p.xpath('ancestor::w:tc|ancestor::w:txbxContent',namespaces=NS):continue
            sid=val(p.find('w:pPr/w:pStyle',NS));t=''.join(p.xpath('.//w:t/text()',namespaces=NS)).strip()
            if sid in RANK:rows.append((i,sid,t))
        changes=[]
        for pos,(i,sid,t) in enumerate(rows[:-1]):
            if sid!='Boldside3' or not t.isupper():continue
            if re.match(r'^[A-Z][.)]\s',t) and not re.match(r'^[IVXLCDM]+[.)]\s',t):continue
            j,child,childtext=rows[pos+1]
            if child not in ('boldside2','Boldside3') or not re.match(r'^A[.)]\s',childtext):continue
            p=ps[i];props=p.find('w:pPr',NS)
            props.find('w:pStyle',NS).set(f'{{{W}}}val','BoldSide1')
            for tag in ('spacing','ind','tabs','shd','pBdr','outlineLvl'):
                for node in props.findall('w:'+tag,NS):props.remove(node)
            # Let BS1 supply its colour, case and weight, retaining other run data.
            for run in p.findall('.//w:r',NS):
                rpr=run.find('w:rPr',NS)
                if rpr is not None:
                    for tag in ('rStyle','color','b','bCs','sz','szCs','caps'):
                        for node in rpr.findall('w:'+tag,NS):rpr.remove(node)
            changes.append(dict(index=i,text=t,before=sid,after='BoldSide1',firstChild=childtext))
        if not changes:continue
        order_properties(d);assert signature(d)==before;assert list_signature(d,s,n)==lists
        destination=output/relative;destination.parent.mkdir(parents=True,exist_ok=True)
        with ZipFile(source) as z,ZipFile(destination,'w') as out:
            out.comment=z.comment
            for info in z.infolist():out.writestr(copy(info),serialize(d) if info.filename=='word/document.xml' else z.read(info.filename))
        verified=read(destination)
        assert all(verified[k]==v for k,v in data.items() if k!='word/document.xml')
        reports.append(dict(file=relative.as_posix(),before=sha(source),staged=sha(destination),changed=True,changes=changes))
        print(json.dumps(dict(file=relative.as_posix(),changes=changes)),flush=True)
    (output/'report.json').write_text(json.dumps(reports,indent=2),encoding='utf-8')
    print(json.dumps(dict(files=len(reports),parents=sum(len(r['changes']) for r in reports))))


if __name__=='__main__':main()
