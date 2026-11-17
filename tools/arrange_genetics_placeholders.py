"""Replace Introduction-only Genetics placeholders with the six requested chapters."""
import argparse
from copy import copy,deepcopy
import hashlib
import json
from pathlib import Path
import shutil
import time
from zipfile import ZipFile
from lxml import etree as E

DATA=Path(r'C:/Users/ANT-PC/OneDrive/Cortex Windows/data')
FOLDER=DATA/'files/Genetics'
OUT=Path(__file__).resolve().parents[1]/'build/genetics-six-chapters'
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
NS={'w':W}
TITLES=['Inheritance','Molecular Genetics','Chromosomal Disorders','Metabolic & Mitochondrial',
        'Cancer & Pharmacogenomics','Prenatal & Therapeutics']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def stage():
    sources=sorted(p for p in FOLDER.glob('*.docx') if not p.name.startswith('~$'))
    assert len(sources)==10
    for p in sources:
        with ZipFile(p) as z:root=E.fromstring(z.read('word/document.xml'))
        assert root.xpath('//w:body//w:t/text()',namespaces=NS)==['Introduction'],p
        assert not root.xpath('//w:body//w:tbl|//w:body//w:drawing|//w:body//w:object',namespaces=NS),p
    OUT.mkdir(parents=True,exist_ok=True)
    report={'sources':{p.name:sha(p) for p in sources},'outputs':[],'sourceContent':'Introduction placeholders only'}
    with ZipFile(sources[0]) as z:
        root=E.fromstring(z.read('word/document.xml'));body=root.find('w:body',NS)
        section=deepcopy(body.find('w:sectPr',NS))
        for n in list(body):body.remove(n)
        p=E.SubElement(body,'{'+W+'}p');props=E.SubElement(p,'{'+W+'}pPr')
        E.SubElement(props,'{'+W+'}pStyle',{'{'+W+'}val':'Normal'})
        if section is not None:body.append(section)
        replacement=E.tostring(root,encoding='UTF-8',xml_declaration=True,standalone=True)
        for index,title in enumerate(TITLES,1):
            dest=OUT/f'{index}. {title}.docx'
            with ZipFile(dest,'w') as out:
                out.comment=z.comment
                for info in z.infolist():out.writestr(copy(info),replacement if info.filename=='word/document.xml' else z.read(info.filename))
            with ZipFile(dest) as out:
                assert out.testzip() is None
                assert not E.fromstring(out.read('word/document.xml')).xpath('//w:t',namespaces=NS)
            report['outputs'].append(dict(file=dest.name,sha256=sha(dest)))
    (OUT/'report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    return report


def install():
    report=json.loads((OUT/'report.json').read_text(encoding='utf-8'))
    for name,hash_ in report['sources'].items():
        p=FOLDER/name;assert sha(p)==hash_,p
        with p.open('r+b'):pass
    for row in report['outputs']:
        assert not (FOLDER/row['file']).exists(),'Unexpected destination collision'
        assert sha(OUT/row['file'])==row['sha256']
    backup=DATA/'backups'/('genetics-six-chapters-'+str(time.time_ns())+'.zip')
    with ZipFile(backup,'x') as z:
        for name in report['sources']:z.write(FOLDER/name,name)
    with ZipFile(backup) as z:
        for name,hash_ in report['sources'].items():assert hashlib.sha256(z.read(name)).hexdigest()==hash_
    written=[]
    try:
        for row in report['outputs']:
            target=FOLDER/row['file'];written.append(target)
            shutil.copyfile(OUT/row['file'],target);assert sha(target)==row['sha256']
        for name,hash_ in report['sources'].items():
            p=FOLDER/name;assert p.resolve().parent==FOLDER.resolve() and sha(p)==hash_;p.unlink()
    except Exception:
        for p in written:p.unlink(missing_ok=True)
        with ZipFile(backup) as z:
            for name in report['sources']:(FOLDER/name).write_bytes(z.read(name))
        raise
    report.update(installed=True,backup=str(backup))
    (OUT/'report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print('Installed six Genetics chapters. Backup:',backup)
    return report


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--install-staged',action='store_true');args=parser.parse_args()
    report=install() if args.install_staged else stage()
    print('\n'.join(r['file'] for r in report['outputs']))
