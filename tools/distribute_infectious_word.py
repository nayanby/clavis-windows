"""Redistribute existing Infectious Disease Word material; retain native content."""
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import shutil
import time
from zipfile import ZipFile,ZIP_DEFLATED
from docx import Document
from lxml import etree as E
from word_chapter_distribution import read_package,body_for,write_slice,merge,make_unique_drawing_ids,inspect,totals,digest,W,NS

DATA=Path(r'C:/Users/ANT-PC/OneDrive/Cortex Windows/data')
SUBJECT='Infectious disease'
OUT=Path(__file__).resolve().parents[1]/'build/infectious-distributed'
TITLES={1:'Fever & Pyrexia of Unknown Origin',2:'Antimicrobial Therapy',
3:'Gram-Positive Bacterial Infections',4:'Gram-Negative Bacterial Infections',
5:'Anaerobic, Atypical, Spirochetal & Non-Vector Zoonotic Infections',6:'Mycobacterial Infections',
7:'Vector-Borne Diseases',8:'DNA Viral Infections',9:'Non-Vector-Borne RNA Viral Infections & Viral Hemorrhagic Fevers',
10:'HIV Infection & Retrovirology',11:'Major Infectious Syndromes',12:'Fungal Infections',
13:'Non-Vector-Borne Parasitic & Helminthic Infections',14:'Infections in Special Hosts & Infection Control'}
# Source chapter, inclusive start/exclusive end of complete top-level body nodes.
MAP={
1:[(1,0,454)],2:[(15,0,958)],
3:[(2,184,272),(8,699,714)],
4:[(2,387,400),(8,0,231),(8,623,695),(9,132,194),(9,359,371),(9,376,383),(11,974,1083)],
5:[(5,743,825),(6,208,279),(8,231,298),(8,714,738),(9,194,333),(9,371,376),(9,411,447),(10,385,447),(11,579,710)],
6:[(4,0,815),(5,205,297),(10,510,835)],
7:[(11,0,579),(11,710,974),(11,1159,1222),(5,182,186),(13,133,245),(13,509,551)],
8:[(5,116,182),(5,186,205),(6,413,415),(9,342,359)],
9:[(5,636,743),(6,279,413),(6,415,418),(8,758,802),(11,1083,1159),(11,1222,1253)],
10:[(3,0,1680)],
11:[(5,0,116),(5,395,485),(5,566,636),(6,0,208),(6,418,651),(7,0,430),
    (8,298,623),(8,695,699),(8,738,758),(9,0,132),(9,333,342),(9,383,388),(9,447,950),(10,0,385),(10,447,510)],
12:[(12,0,1356),(5,297,395)],
13:[(13,0,133),(13,245,509),(13,551,635),(5,485,566),(9,388,411)],
14:[(14,0,1019),(2,335,387),(2,400,425)],
15:[(16,0,361),(2,0,184),(2,272,335)]}
CRITICAL=Path('Critical Care/2. Sepsis, Septic Shock & Multiorgan Dysfunction.docx')
# These complete organism sections lose their former parent during redistribution.
# Promote their existing heading without adding title/Introduction paragraphs.
PROMOTE={2:[387],5:[182],8:[699,705,714,719],9:[342,359,371,376],
         11:[1159,1171,1180,1187,1205,1214]}


def stage():
    folder=DATA/'files'/SUBJECT
    sources={int(p.name.split('.')[0]):p for p in folder.glob('*.docx') if not p.name.startswith('~$')}
    assert len(sources)==15 and set(sources)==set(range(1,16))
    sources[16]=DATA/'files'/CRITICAL
    packages={n:read_package(p) for n,p in sources.items()}
    for n,indices in PROMOTE.items():
        doc=E.fromstring(packages[n]['word/document.xml']);body=doc.find('w:body',NS)
        for index in indices:
            paragraph=body[index];props=paragraph.find('w:pPr',NS)
            if props is None:props=E.Element('{'+W+'}pPr');paragraph.insert(0,props)
            style=props.find('w:pStyle',NS)
            if style is None:style=E.Element('{'+W+'}pStyle');props.insert(0,style)
            style.set('{'+W+'}val','Heading1')
            for name in ('outlineLvl','spacing','ind','pBdr','shd'):
                for item in props.findall('w:'+name,NS):props.remove(item)
            for run in paragraph.findall('.//w:rPr',NS):
                for item in list(run):
                    if E.QName(item).localname in {'rStyle','rFonts','sz','szCs','color','b','bCs','i','iCs'}:run.remove(item)
        packages[n]['word/document.xml']=E.tostring(doc,encoding='UTF-8',xml_declaration=True,standalone=True)
    covered=defaultdict(list)
    for ranges in MAP.values():
        for n,a,b in ranges:covered[n].extend(range(a,b))
    # This entire older sepsis block is already present in Critical Care.
    covered[2].extend(range(425,787))
    for n,package in packages.items():
        body=body_for(package)
        assert sorted(covered[n])==[i for i,p in enumerate(body) if p.tag!='{'+W+'}sectPr'],('Coverage mismatch',sources[n])
        assert not body.xpath('.//w:footnoteReference|.//w:endnoteReference|.//w:commentReference',namespaces=NS)
    OUT.mkdir(parents=True,exist_ok=True)
    duplicate=OUT/'duplicate-sepsis-evidence.docx'
    write_slice(packages[2],[(425,787)],duplicate)
    assert totals([duplicate])==totals([sources[16]]),'Existing sepsis content differs; cannot consolidate automatically'
    report={'sources':{str(p.relative_to(DATA/'files')).replace('\\','/'):digest(p) for p in sources.values()},'outputs':[],
            'exactDuplicateSepsisBlock':{'source':sources[2].name,'start':425,'end':787,'alreadyIn':CRITICAL.as_posix()},
            'contentGaps':'Only existing material is redistributed. Organisms without standalone source notes are not newly authored.',
            'sepsisMovedToCriticalCare':True}
    output_paths=[]
    for number,ranges in MAP.items():
        target=CRITICAL if number==15 else Path(SUBJECT)/f'{number}. {TITLES[number]}.docx'
        dest=OUT/target;dest.parent.mkdir(parents=True,exist_ok=True)
        grouped={}
        for n,a,b in ranges:grouped.setdefault(n,[]).append((a,b))
        parts=[];partdir=OUT/'parts'/str(number);partdir.mkdir(parents=True,exist_ok=True)
        for n,slices in grouped.items():
            part=partdir/f'{n}.docx';write_slice(packages[n],slices,part);parts.append(part)
        if len(parts)==1:
            shutil.copyfile(parts[0],dest)
        else:
            doc=Document(parts[0])
            for i,part in enumerate(parts[1:],1):merge(doc,Document(part),f'chapter{number}_{i}_')
            make_unique_drawing_ids(doc);doc.save(dest)
        details=inspect(dest);output_paths.append(dest)
        report['outputs'].append(dict(file=target.as_posix(),sha256=digest(dest),words=sum(len(t.split())*c for t,c in details[0].items()),tables=details[1],images=sum(details[2].values()),ranges=ranges))
        print(target.name,report['outputs'][-1]['words'],'words',flush=True)
    before=totals(sources.values());after=totals(output_paths);dupe=totals([duplicate])
    assert after[0]==before[0]-dupe[0],'Text lost or duplicated'
    assert after[1]==before[1]-dupe[1],'Table count mismatch'
    assert after[2]==before[2]-dupe[2],'Image hash/reference mismatch'
    report['verification']=dict(allSourceBodyElementsAssignedOnceExceptVerifiedDuplicate=True,textPreserved=True,tablesPreserved=True,imageHashesPreserved=True,relationshipsAndStylesValidated=True)
    (OUT/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    return report


def install():
    report=json.loads((OUT/'report.json').read_text(encoding='utf-8'));files=DATA/'files'
    source_paths={files/name:hash_ for name,hash_ in report['sources'].items()}
    destinations={files/r['file'] for r in report['outputs']}
    for p,hash_ in source_paths.items():
        assert digest(p)==hash_,('Concurrent edit',p)
        with p.open('r+b'):pass
    for row in report['outputs']:
        target=files/row['file']
        assert target in source_paths or not target.exists(),('Destination collision',target)
        assert digest(OUT/row['file'])==row['sha256']
    backup=DATA/'backups'/('infectious-redistribution-'+str(time.time_ns())+'.zip')
    with ZipFile(backup,'x',ZIP_DEFLATED) as z:
        for p in source_paths:z.write(p,p.relative_to(files).as_posix())
    with ZipFile(backup) as z:
        for p,hash_ in source_paths.items():assert hashlib.sha256(z.read(p.relative_to(files).as_posix())).hexdigest()==hash_
    written=[]
    try:
        for row in report['outputs']:
            target=files/row['file'];assert target.resolve().is_relative_to(files.resolve())
            if target in source_paths:assert digest(target)==source_paths[target]
            written.append(target);shutil.copyfile(OUT/row['file'],target);assert digest(target)==row['sha256']
        for p,hash_ in source_paths.items():
            if p in destinations:continue
            assert p.parent.resolve()==(files/SUBJECT).resolve() and digest(p)==hash_
            p.unlink()
    except Exception:
        for p in written:
            if p not in source_paths:p.unlink(missing_ok=True)
        with ZipFile(backup) as z:
            for p in source_paths:p.write_bytes(z.read(p.relative_to(files).as_posix()))
        raise
    report.update(installed=True,backup=str(backup))
    (OUT/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print('Installed 14 Infectious Disease chapters and updated Critical Care sepsis. Backup:',backup)
    return report


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--install-staged',action='store_true');args=parser.parse_args()
    report=install() if args.install_staged else stage()
    print(json.dumps(report['verification'],indent=2))
