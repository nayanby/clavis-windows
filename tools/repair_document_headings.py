"""Repair clear standalone headings and promote conflicting parent/sibling groups."""
from collections import Counter, defaultdict
from copy import copy
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import time
from zipfile import ZipFile
from lxml import etree as E
from audit_document_headings import ROOT, RANK, scan, text
from apply_clinical_template import NS, W, signature, list_signature, serialize, order_properties, sha

BY_RANK = {v: k for k, v in RANK.items()}
OUTPUT = Path(__file__).resolve().parents[1] / 'build/heading-repair'


def plan(rows, candidates):
    semantic = {r['i']: r['style'] for r in rows if r['style'] in RANK}
    targets = {}
    headings = [r for r in rows if r['i'] in semantic]
    # A letter I between H and J belongs to the same sibling group, not Roman I.
    for pos, row in enumerate(headings[1:-1], 1):
        if re.match(r'^I[.)]\s', row['text']) and re.match(r'^H[.)]\s', headings[pos-1]['text']) and re.match(r'^J[.)]\s', headings[pos+1]['text']):
            semantic[row['i']] = semantic[headings[pos-1]['i']]
            targets[row['i']] = semantic[row['i']]
    stack = []
    group = {}
    members = defaultdict(list)
    parent = {}
    for row in rows:
        index = row['i']
        if index not in semantic:
            continue
        rank = RANK[semantic[index]]
        while stack and RANK[semantic[stack[-1]]] >= rank:
            stack.pop()
        parent[index] = stack[-1] if stack else None
        group[index] = (parent[index], rank)
        members[group[index]].append(index)
        stack.append(index)
    promoted = set()

    def promote(index, child_rank):
        rank = RANK[targets.get(index, semantic[index])]
        if rank < child_rank:
            return
        new_rank = max(0, child_rank-1)
        key = group[index]
        if (key, new_rank) in promoted:
            return
        promoted.add((key, new_rank))
        for sibling in members[key]:
            targets[sibling] = BY_RANK[new_rank]
        ancestor = parent[index]
        if ancestor is not None:
            promote(ancestor, new_rank)

    candidate_by_id = {c['i']: c for c in candidates}
    for pos, row in enumerate(rows):
        index = row['i']
        if index not in candidate_by_id:
            continue
        candidate = candidate_by_id[index]
        following = rows[pos+1] if pos+1 < len(rows) else None
        major = candidate['major']
        child_heading = following if following and following['style'] in RANK else None
        if row['text'].isupper() and not re.match(r'^\d+[.)]', row['text']) and child_heading is None:
            child_heading = next((r for r in rows[pos+1:pos+16] if r['style'] in RANK), None)
            if child_heading and re.match(r'^[A-HJ-Z][.)]\s', child_heading['text']):
                major = True
        if major and child_heading:
            rank = RANK[child_heading['style']]
            targets[index] = 'Heading1' if rank == 4 else ('BoldSide1' if rank >= 5 else BY_RANK[max(0, rank-1)])
            continue
        targets[index] = 'Boldside3'
        # Existing numbered BS3 headings are siblings, not the new heading's parent.
        preceding = next((r for r in reversed(rows[:pos]) if r['i'] in semantic and not re.match(r'^\d+[.)]\s', r['text'])), None)
        if preceding:
            promote(preceding['i'], RANK['Boldside3'])
    return targets


def stage(only=None, previous=None):
    reports = [r for r in (previous or []) if r['file'] not in (only or set())]
    for source in sorted(ROOT.rglob('*.docx')):
        relative = source.relative_to(ROOT)
        if only is not None and relative.as_posix() not in only:
            continue
        if source.name.startswith('~$') or any(p.startswith(('_','.')) for p in relative.parts[:-1]):
            continue
        original_hash = sha(source)
        root, styles, numbering, paragraphs, rows, candidates = scan(source)
        targets = plan(rows, candidates)
        changes = []
        before = signature(root)
        lists = list_signature(root, styles, numbering)
        definitions = {s.get(f'{{{W}}}styleId'): s for s in styles.findall('w:style', NS)}
        for index, target in targets.items():
            p = paragraphs[index]
            assert not p.xpath('ancestor::w:tc|ancestor::w:txbxContent', namespaces=NS)
            assert lists[index] is None
            assert target in definitions, (source, target)
            props = p.find('w:pPr', NS)
            if props is None:
                props = E.Element(f'{{{W}}}pPr'); p.insert(0, props)
            sid = props.find('w:pStyle', NS)
            old = sid.get(f'{{{W}}}val', '') if sid is not None else ''
            if old == target:
                continue
            if sid is None:
                sid = E.Element(f'{{{W}}}pStyle'); props.insert(0, sid)
            sid.set(f'{{{W}}}val', target)
            # Inherit the requested heading design rather than old body formatting.
            for name in ('spacing','ind','tabs','outlineLvl','pBdr','shd','jc'):
                for n in props.findall('w:'+name, NS): props.remove(n)
            num = props.find('w:numPr', NS)
            if num is None: num = E.SubElement(props, f'{{{W}}}numPr')
            for n in list(num): num.remove(n)
            E.SubElement(num, f'{{{W}}}numId', {f'{{{W}}}val':'0'})
            for run in p.findall('.//w:r', NS):
                rpr = run.find('w:rPr', NS)
                if rpr is None: continue
                for name in ('rStyle','rFonts','sz','szCs','b','bCs','i','iCs','u','caps','smallCaps','color','shd','highlight'):
                    for n in rpr.findall('w:'+name, NS): rpr.remove(n)
            changes.append(dict(index=index,text=text(p),before=old,after=target))
        if changes:
            order_properties(root)
            assert signature(root) == before
            assert list_signature(root, styles, numbering) == lists
            destination = OUTPUT / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            replacement = serialize(root)
            with ZipFile(source) as z, ZipFile(destination,'w') as out:
                out.comment = z.comment
                for info in z.infolist():
                    out.writestr(copy(info), replacement if info.filename=='word/document.xml' else z.read(info.filename))
            with ZipFile(source) as z, ZipFile(destination) as out:
                assert out.testzip() is None
                assert out.read('word/document.xml') == replacement
                for name in z.namelist():
                    if name!='word/document.xml': assert z.read(name)==out.read(name)
        reports.append(dict(file=relative.as_posix(),before=original_hash,changes=changes,staged=sha(OUTPUT/relative) if changes else None))
    OUTPUT.mkdir(parents=True, exist_ok=True)
    (OUTPUT/'report.json').write_text(json.dumps(reports, ensure_ascii=False,indent=2),encoding='utf-8')
    return reports


def install():
    reports=json.loads((OUTPUT/'report.json').read_text(encoding='utf-8'))
    changed=[]
    locked=[]
    for r in (r for r in reports if r['changes']):
        if sha(ROOT/r['file'])==r['staged']:
            continue
        assert sha(ROOT/r['file'])==r['before'],r['file']
        assert sha(OUTPUT/r['file'])==r['staged'],r['file']
        try:
            with (ROOT/r['file']).open('r+b'):pass
        except PermissionError:
            locked.append(r['file'])
            continue
        changed.append(r)
    print('Installing:',len(changed),'Locked:',locked,flush=True)
    (OUTPUT/'pending.json').write_text(json.dumps(locked,indent=2),encoding='utf-8')
    if not changed:
        return reports
    backup=ROOT.parent/'backups'/('heading-hierarchy-'+str(time.time_ns())+'.zip')
    with ZipFile(backup,'x') as z:
        for r in changed:z.write(ROOT/r['file'],r['file'])
    with ZipFile(backup) as z:
        for r in changed:assert hashlib.sha256(z.read(r['file'])).hexdigest()==r['before']
    written=[]
    try:
        for r in changed:
            assert sha(ROOT/r['file'])==r['before']
            written.append(r)
            shutil.copyfile(OUTPUT/r['file'],ROOT/r['file'])
            assert sha(ROOT/r['file'])==r['staged']
    except Exception:
        with ZipFile(backup) as z:
            for r in written:(ROOT/r['file']).write_bytes(z.read(r['file']))
        raise
    print('Backup:',backup)
    return reports


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--install-staged',action='store_true');parser.add_argument('--refresh-filtered',action='store_true');args=parser.parse_args()
    if args.refresh_filtered:
        previous=json.loads((OUTPUT/'report.json').read_text(encoding='utf-8'))
        dirty=set()
        for report in previous:
            if not report['changes']:continue
            with ZipFile(ROOT/report['file']) as z:
                ps=E.fromstring(z.read('word/document.xml')).findall('.//w:p',NS)
            for change in report['changes']:
                if re.search(r'heading[1-4]$|boldside[1-4]$',change['before'],re.I):continue
                t=change['text'];p=ps[change['index']]
                excluded=bool(p.xpath('.//w:hyperlink|.//w:fldSimple|.//w:drawing|.//w:pict|.//m:oMath',namespaces={**NS,'m':'http://schemas.openxmlformats.org/officeDocument/2006/math'}))
                excluded|=bool(re.search(r'MD/DNB|GENERAL MEDICINE|\bPAGE\s+\d|\|\s*\d',t,re.I))
                excluded|=t.isupper() and len(t.split())==1 and t not in {'MANAGEMENT','TREATMENT','DIAGNOSIS','INVESTIGATIONS','COMPLICATIONS','PROGNOSIS','EPIDEMIOLOGY','PATHOPHYSIOLOGY','ETIOLOGY','DEFINITION','CLASSIFICATION','PREVENTION','THERAPY'}
                if excluded:dirty.add(report['file'])
        print('Refreshing filtered files:',len(dirty),flush=True)
        reports=stage(dirty,previous)
    else:
        reports=install() if args.install_staged else stage()
    print(json.dumps(dict(filesChecked=len(reports),filesChanged=sum(bool(r['changes']) for r in reports),changes=dict(Counter(c['after'] for r in reports for c in r['changes']))),indent=2))
