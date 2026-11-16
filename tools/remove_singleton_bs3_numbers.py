"""Unnumber a lone BS3 beneath BS2 without altering body-list numbering."""
import argparse
from collections import defaultdict
from copy import copy
import json
from pathlib import Path
import re
from zipfile import ZipFile
from lxml import etree as E
from apply_clinical_template import NS,W,sha,serialize,list_signature,order_properties
from enforce_clinical_style_palette import choose_paragraph
from repair_unintended_emphasis import install as install_verified_packages

DATA=Path(r'C:/Users/ANT-PC/OneDrive/Cortex Windows/data')
OUT=Path(__file__).resolve().parents[1]/'build/singleton-bs3'


def stage():
    reports=[]
    for source in sorted((DATA/'files').rglob('*.docx')):
        relative=source.relative_to(DATA/'files')
        if source.name.startswith('~$') or any(p.startswith(('_','.')) for p in relative.parts[:-1]):continue
        original_hash=sha(source)
        with ZipFile(source) as z:
            root=E.fromstring(z.read('word/document.xml'));styles=E.fromstring(z.read('word/styles.xml'))
            numbering=E.fromstring(z.read('word/numbering.xml')) if 'word/numbering.xml' in z.namelist() else E.Element('{'+W+'}numbering')
            definitions={s.get('{'+W+'}styleId'):s for s in styles.findall('w:style',NS)}
            paragraphs=root.findall('.//w:p',NS);lists=list_signature(root,styles,numbering)
            groups=defaultdict(list);parent=None
            for i,p in enumerate(paragraphs):
                if p.xpath('ancestor::w:tc|ancestor::w:txbxContent',namespaces=NS):continue
                role=choose_paragraph(p,definitions)[0]
                if role=='boldside2':parent=i
                elif role=='Boldside3':
                    if parent is not None:groups[parent].append(i)
                elif role.startswith('Heading') or role in ('BoldSide1','Title'):parent=None
            original_lists=lists[:];changes=[]
            for children in groups.values():
                if len(children)!=1:continue
                i=children[0];p=paragraphs[i];text=''.join(p.xpath('.//w:t/text()',namespaces=NS))
                match=re.match(r'^\s*\d{1,3}[.)]\s+',text)
                if match:
                    remaining=len(match.group())
                    for node in p.findall('.//w:t',NS):
                        old=node.text or '';take=min(len(old),remaining);node.text=old[take:];remaining-=take
                        if not remaining:break
                    assert not remaining
                automatic=bool(lists[i] and lists[i][0]=='decimal')
                if automatic:
                    props=p.find('w:pPr',NS)
                    if props is None:props=E.Element('{'+W+'}pPr');p.insert(0,props)
                    num=props.find('w:numPr',NS)
                    if num is None:num=E.SubElement(props,'{'+W+'}numPr')
                    for n in list(num):num.remove(n)
                    E.SubElement(num,'{'+W+'}numId',{'{'+W+'}val':'0'})
                    original_lists[i]=None
                if match or automatic:
                    changes.append(dict(index=i,before=text,after=''.join(p.xpath('.//w:t/text()',namespaces=NS)),automatic=automatic))
            if changes:
                order_properties(root)
                assert list_signature(root,styles,numbering)==original_lists
                # Verify every text node except the documented heading prefixes.
                before=E.fromstring(z.read('word/document.xml'));old_ps=before.findall('.//w:p',NS)
                changed={c['index']:c for c in changes}
                for i,(old,new) in enumerate(zip(old_ps,paragraphs)):
                    a=''.join(old.xpath('.//w:t/text()',namespaces=NS));b=''.join(new.xpath('.//w:t/text()',namespaces=NS))
                    assert b==(changed[i]['after'] if i in changed else a)
                destination=OUT/relative;destination.parent.mkdir(parents=True,exist_ok=True)
                replacement=serialize(root)
                with ZipFile(destination,'w') as out:
                    out.comment=z.comment
                    for info in z.infolist():out.writestr(copy(info),replacement if info.filename=='word/document.xml' else z.read(info.filename))
                with ZipFile(destination) as out:
                    assert out.testzip() is None
                    for name in z.namelist():assert out.read(name)==(replacement if name=='word/document.xml' else z.read(name))
            reports.append(dict(file=relative.as_posix(),before=original_hash,changed=bool(changes),changes=changes,staged=sha(OUT/relative) if changes else None))
    OUT.mkdir(parents=True,exist_ok=True);(OUT/'report.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2),encoding='utf-8')
    return reports


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--install-staged',action='store_true');args=parser.parse_args()
    reports=install_verified_packages(DATA,OUT) if args.install_staged else stage()
    print(json.dumps(dict(filesChecked=len(reports),filesChanged=sum(r['changed'] for r in reports),headingsUnnumbered=sum(len(r['changes']) for r in reports)),indent=2))
