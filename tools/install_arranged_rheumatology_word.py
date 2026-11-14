"""Verify rearranged Word content, back up originals, and install on request."""
import sys,json,hashlib,shutil,time
from collections import Counter
from zipfile import ZipFile,ZIP_DEFLATED
from pathlib import Path
from lxml import etree as E
from arrange_rheumatology_word import SOURCE,OUT,W

def inspect(path):
 with ZipFile(path) as z:
  assert z.testzip() is None
  root=E.fromstring(z.read('word/document.xml'))
  ns={'w':W}
  texts=Counter(root.xpath('//w:body//w:t/text()',namespaces=ns))
  tables=len(root.xpath('//w:body//w:tbl',namespaces=ns))
  images=Counter()
  rels=E.fromstring(z.read('word/_rels/document.xml.rels'))
  rels={n.get('Id'):n for n in rels}
  for n in root.iter():
   for k,v in n.attrib.items():
    if E.QName(k).namespace=='http://schemas.openxmlformats.org/officeDocument/2006/relationships':
     assert v in rels,(path,v)
     r=rels[v]
     if r.get('Type').endswith('/image'):
      import posixpath
      target=posixpath.normpath(posixpath.join('word',r.get('Target')))
      images[hashlib.sha256(z.read(target)).hexdigest()]+=1
  return texts,tables,images

def total(files):
 text=Counter();tables=0;images=Counter()
 for p in files:
  t,c,i=inspect(p);text.update(t);tables+=c;images.update(i)
 return text,tables,images

original=sorted(SOURCE.glob('*.docx')); arranged=sorted(OUT.glob('*.docx'))
assert len(original)==5 and len(arranged)==16
before=total(original);after=total(arranged)
assert before==after,'Text/table/image preservation failed'
report={'chapters':16,'textRuns':sum(before[0].values()),'tables':before[1],'imageReferences':sum(before[2].values()),'preservation':'passed','visualQA':'Unavailable: Word automation stalled; LibreOffice is not installed'}
if '--install' in sys.argv:
 backup=SOURCE.parent.parent/'backups'/('rheumatology-word-arrangement-'+time.strftime('%Y%m%d-%H%M%S')+'.zip')
 backup.parent.mkdir(parents=True,exist_ok=True)
 with ZipFile(backup,'x',ZIP_DEFLATED) as z:
  for p in original:z.write(p,p.name)
 with ZipFile(backup) as z:
  for p in original:assert z.read(p.name)==p.read_bytes()
 for p in arranged:
  target=SOURCE/p.name
  assert not target.exists(),target
  shutil.copyfile(p,target)
  assert target.read_bytes()==p.read_bytes()
 for p in original:
  assert p.parent.resolve()==SOURCE.resolve()
  p.unlink()
 assert total(sorted(SOURCE.glob('*.docx')))==before
 report['backup']=str(backup)
reportpath=OUT/'verification.json'
reportpath.write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
