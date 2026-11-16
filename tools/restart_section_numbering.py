"""Restart reused body-list numbering at independent heading/cell boundaries."""
import argparse
from collections import Counter
from copy import copy, deepcopy
import hashlib
import json
from pathlib import Path
import shutil
import time
from zipfile import ZipFile
from lxml import etree as E
from apply_clinical_template import NS, W, list_signature, signature, serialize, sha, order_properties
from enforce_clinical_style_palette import choose_paragraph

ROOT=Path(r'C:/Users/ANT-PC/OneDrive/Cortex Windows/data/files')
OUT=Path(__file__).resolve().parents[1]/'build/section-numbering'
def tag(name):return '{'+W+'}'+name
def value(node):return node.get(tag('val'),'') if node is not None else ''


def stage():
    reports=[]
    for path in sorted(ROOT.rglob('*.docx')):
        rel=path.relative_to(ROOT)
        if path.name.startswith('~$') or any(p.startswith(('_','.')) for p in rel.parts[:-1]):continue
        before_hash=sha(path)
        with ZipFile(path) as z:
            if 'word/numbering.xml' not in z.namelist():
                reports.append(dict(file=rel.as_posix(),before=before_hash,changes=[],staged=None));continue
            root=E.fromstring(z.read('word/document.xml'));styles=E.fromstring(z.read('word/styles.xml'));numbers=E.fromstring(z.read('word/numbering.xml'))
            definitions={s.get(tag('styleId')):s for s in styles.findall('w:style',NS)}
            ps=root.findall('.//w:p',NS);lists=list_signature(root,styles,numbers);body_signature=signature(root)
            nums={n.get(tag('numId')):n for n in numbers.findall('w:num',NS)}
            next_id=max([int(n) for n in nums if n.isdigit()]+[0])+1
            # The shallowest level of each numbering instance is its section list.
            top={}
            for listing in lists:
                if listing and listing[0] not in {'bullet','unresolved'}:
                    top[listing[-1]]=min(top.get(listing[-1],99),int(listing[1]))
            used=set();contexts={};sections={None:(-1,'Document start')};changes=[]
            for index,(p,listing) in enumerate(zip(ps,lists)):
                cell=next((a for a in p.iterancestors() if a.tag==tag('tc')),None)
                role=choose_paragraph(p,definitions)[0]
                if role.startswith('Heading') or role.lower().startswith('boldside') or role=='Title':
                    sections[cell]=(index,''.join(p.xpath('.//w:t/text()',namespaces=NS)).strip())
                    if listing and listing[0] not in {'bullet','unresolved'}:used.add(listing[-1])
                    continue
                if not listing or listing[0] in {'bullet','unresolved'}:continue
                fmt,level,_,start,num_id=listing
                section,section_text=sections.get(cell,sections[None])
                key=(num_id,section,cell)
                if key not in contexts:
                    if int(level)!=top[num_id]:continue
                    target=num_id
                    if num_id in used or str(start)!='1':
                        target=str(next_id);next_id+=1
                        clone=deepcopy(nums[num_id]);clone.set(tag('numId'),target)
                        override=clone.find(f'w:lvlOverride[@w:ilvl="{level}"]',NS)
                        if override is None:override=E.SubElement(clone,tag('lvlOverride'),{tag('ilvl'):level})
                        restart=override.find('w:startOverride',NS)
                        if restart is None:restart=E.Element(tag('startOverride'));override.insert(0,restart)
                        restart.set(tag('val'),'1');numbers.append(clone)
                        changes.append(dict(index=index,section=section_text,firstText=''.join(p.xpath('.//w:t/text()',namespaces=NS))[:180],fromNum=num_id,toNum=target,level=level))
                    used.add(num_id);contexts[key]=target
                target=contexts[key]
                if target==num_id:continue
                props=p.find('w:pPr',NS)
                if props is None:props=E.Element(tag('pPr'));p.insert(0,props)
                num=props.find('w:numPr',NS)
                if num is None:num=E.SubElement(props,tag('numPr'))
                for name,val in [('numId',target),('ilvl',level)]:
                    node=num.find('w:'+name,NS)
                    if node is None:node=E.SubElement(num,tag(name))
                    node.set(tag('val'),val)
            if changes:
                order_properties(root)
                assert signature(root)==body_signature
                after_lists=list_signature(root,styles,numbers)
                for old,new in zip(lists,after_lists):
                    if old is None or old[0] in {'bullet','unresolved'}:assert old==new
                    else:assert old[:3]==new[:3]
                dest=OUT/rel;dest.parent.mkdir(parents=True,exist_ok=True)
                replacements={'word/document.xml':serialize(root),'word/numbering.xml':serialize(numbers)}
                with ZipFile(dest,'w') as out:
                    out.comment=z.comment
                    for info in z.infolist():out.writestr(copy(info),replacements.get(info.filename,z.read(info.filename)))
                with ZipFile(dest) as out:
                    assert out.testzip() is None
                    for name in z.namelist():assert out.read(name)==replacements.get(name,z.read(name))
            reports.append(dict(file=rel.as_posix(),before=before_hash,changes=changes,staged=sha(OUT/rel) if changes else None))
    OUT.mkdir(parents=True,exist_ok=True);(OUT/'report.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2),encoding='utf-8')
    return reports


def install():
    reports=json.loads((OUT/'report.json').read_text(encoding='utf-8'));changed=[];locked=[]
    for row in reports:
        if not row['changes'] or sha(ROOT/row['file'])==row['staged']:continue
        assert sha(ROOT/row['file'])==row['before'],row['file'];assert sha(OUT/row['file'])==row['staged']
        try:
            with (ROOT/row['file']).open('r+b'):pass
        except PermissionError:locked.append(row['file']);continue
        changed.append(row)
    print('Installing',len(changed),'Locked:',locked,flush=True)
    if not changed:return reports
    backup=ROOT.parent/'backups'/('numbering-restarts-'+str(time.time_ns())+'.zip')
    with ZipFile(backup,'x') as z:
        for row in changed:z.write(ROOT/row['file'],row['file'])
    with ZipFile(backup) as z:
        for row in changed:assert hashlib.sha256(z.read(row['file'])).hexdigest()==row['before']
    written=[]
    try:
        for row in changed:
            assert sha(ROOT/row['file'])==row['before'];written.append(row)
            shutil.copyfile(OUT/row['file'],ROOT/row['file']);assert sha(ROOT/row['file'])==row['staged']
    except Exception:
        with ZipFile(backup) as z:
            for row in written:(ROOT/row['file']).write_bytes(z.read(row['file']))
        raise
    print('Backup:',backup)
    return reports


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--install-staged',action='store_true');args=parser.parse_args()
    rows=install() if args.install_staged else stage()
    print(json.dumps(dict(filesChecked=len(rows),filesChanged=sum(bool(r['changes']) for r in rows),listsRestarted=sum(len(r['changes']) for r in rows)),indent=2))
