"""Repair duplicate heading prefixes and heading-styled labels in an older export."""
import argparse
from collections import defaultdict
from copy import copy
from pathlib import Path
import re
from zipfile import ZipFile
from lxml import etree as E
from apply_clinical_template import W,NS,read,xml,val,serialize,list_signature
from audit_document_headings import RANK

def text(p):return ''.join(p.xpath('.//w:t/text()',namespaces=NS))
def roman_value(token):
    values={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000};total=0;prior=0
    for char in reversed(token.upper()):
        value=values[char];total+=-value if value<prior else value;prior=max(prior,value)
    return total
def roman_label(value):
    result=''
    for number,token in [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]:
        count,value=divmod(value,number);result+=token*count
    return result
def replace_prefix(p,length,replacement):
    nodes=p.findall('.//w:t',NS);remaining=length
    for node in nodes:
        old=node.text or '';take=min(len(old),remaining);node.text=old[take:];remaining-=take
        if not remaining:break
    assert not remaining
    nodes[0].text=replacement+(nodes[0].text or '')

def main():
    parser=argparse.ArgumentParser();parser.add_argument('source',type=Path);parser.add_argument('destination',type=Path);parser.add_argument('--normalize-heading-levels',action='store_true');args=parser.parse_args()
    assert args.source.resolve()!=args.destination.resolve()
    data=read(args.source);d=xml(data['word/document.xml']);s=xml(data['word/styles.xml']);n=xml(data['word/numbering.xml'])
    lists=list_signature(d,s,n);ps=d.findall('.//w:p',NS);before=[text(p) for p in ps]
    groups=defaultdict(list);stack=[];table_labels=0;prefixes=0;expected={}
    for i,p in enumerate(ps):
        style=p.find('w:pPr/w:pStyle',NS);sid=val(style)
        if p.xpath('ancestor::w:tc',namespaces=NS):
            if sid in RANK:
                style.set('{'+W+'}val','Normal')
                for keep in p.findall('w:pPr/w:keepNext',NS):keep.getparent().remove(keep)
                for run in p.findall('w:r',NS):
                    props=run.find('w:rPr',NS)
                    if props is None:props=E.Element('{'+W+'}rPr');run.insert(0,props)
                    if props.find('w:rStyle',NS) is None:
                        props.insert(0,E.Element('{'+W+'}rStyle',{'{'+W+'}val':'SubtleEmphasis'}))
                table_labels+=1
            continue
        if sid not in RANK:continue
        rank=RANK[sid]
        while stack and stack[-1][1]>=rank:stack.pop()
        groups[(stack[-1][0] if stack else None,rank)].append(i);stack.append((i,rank))
    for indices in groups.values():
        for i in indices:
            match=re.match(r'^\s*[A-Za-z][.)]\s+(?=(?:[IVXLCDM]+|\d+(?:\.\d+)*)[.)]\s+)',text(ps[i]),re.I)
            if match:
                replace_prefix(ps[i],len(match.group()),'');expected[i]=text(ps[i]);prefixes+=1
        # The older exporter stripped single-character Roman I/V/X before
        # adding letters. Restore them only when multiple surviving Roman
        # siblings prove the original sequence and their exact positions.
        hints=[]
        for position,i in enumerate(indices):
            match=re.match(r'^\s*([IVXLCDM]+)[.)]\s+',text(ps[i]),re.I)
            if match:hints.append((position,roman_value(match.group(1))))
        if len(hints)>=2 and all(value==position+1 for position,value in hints):
            for position,i in enumerate(indices):
                match=re.match(r'^\s*([A-Z])[.)]\s+',text(ps[i]))
                if match and match.group(1)==chr(65+position) and match.group(1)!=roman_label(position+1):
                    replace_prefix(ps[i],len(match.group()),roman_label(position+1)+'. ');expected[i]=text(ps[i]);prefixes+=1
    level_changes=0;new_title=None;removed_title=None;removed_spacers=[]
    if args.normalize_heading_levels:
        body=d.find('w:body',NS)
        headings=[p for p in ps if not p.xpath('ancestor::w:tc',namespaces=NS) and val(p.find('w:pPr/w:pStyle',NS)) in RANK]
        if len(headings)>1 and val(headings[0].find('w:pPr/w:pStyle',NS))=='Heading1' and val(headings[1].find('w:pPr/w:pStyle',NS))=='Heading2' and not re.match(r'^\s*(?:[IVXLCDM]+|[A-Z]|\d+)[.)]\s+',text(headings[1]),re.I):
            removed_title=headings[0];new_title=headings[1]
            body.remove(removed_title);body.insert(0,new_title)
            new_title.find('w:pPr/w:pStyle',NS).set('{'+W+'}val','Heading1');level_changes+=1
        for p in headings:
            if p is removed_title or p is new_title:continue
            style=p.find('w:pPr/w:pStyle',NS);sid=val(style);t=text(p)
            target=None
            if sid=='Heading3' and re.match(r'^\s*[IVXLCDM]+[.)]\s+',t,re.I):target='Heading2'
            elif sid in ('BoldSide1','boldside2','Boldside3') and re.match(r'^\s*[A-Z][.)]\s+',t):target='Heading3'
            elif sid in ('boldside2','Boldside3') and re.match(r'^\s*\d+[.)]\s+',t):target='Heading4'
            if target and target!=sid:style.set('{'+W+'}val',target);level_changes+=1
        assert len(d.findall('.//w:pPr/w:pStyle[@w:val="Heading1"]',NS))==1
        for p in list(body.findall('w:p',NS)):
            previous=p.getprevious()
            if previous is not None and previous.tag=='{'+W+'}tbl' and len(p)==0:
                removed_spacers.append(p);body.remove(p)
    after_lists=list_signature(d,s,n)
    if removed_title is not None or removed_spacers:
        assert after_lists==[listing for p,listing in zip(ps,lists) if p is not removed_title and p not in removed_spacers]
    else:assert after_lists==lists
    for i,p in enumerate(ps):assert text(p)==expected.get(i,before[i])
    args.destination.parent.mkdir(parents=True,exist_ok=True)
    replacements={'word/document.xml':serialize(d)}
    if new_title is not None and 'docProps/core.xml' in data:
        core=xml(data['docProps/core.xml']);title=core.find('{http://purl.org/dc/elements/1.1/}title')
        if title is not None:title.text=text(new_title)
        replacements['docProps/core.xml']=serialize(core)
    with ZipFile(args.source) as z,ZipFile(args.destination,'w') as out:
        out.comment=z.comment
        for info in z.infolist():out.writestr(copy(info),replacements.get(info.filename,z.read(info.filename)))
    verified=read(args.destination)
    assert all(verified[k]==v for k,v in data.items() if k not in replacements)
    print('Corrected heading prefixes:',prefixes,'table labels:',table_labels,'heading levels:',level_changes,'file:',args.destination)

if __name__=='__main__':main()
