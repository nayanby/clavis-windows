"""Move fever syndromes and chapters after nine into one tenth Word document."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from copy import deepcopy
from collections import Counter
import hashlib,shutil,sys,time
from lxml import etree as E
from arrange_rheumatology_word import merge_parts,W,SOURCE

stage=Path(__file__).resolve().parents[1]/'build/rheumatology-others'
stage.mkdir(parents=True,exist_ok=True)
parts=stage/'parts';parts.mkdir(exist_ok=True)
files=sorted(SOURCE.glob('*.docx'))
assert len(files)==16
first=files[0]
with ZipFile(first) as z:package={n:z.read(n) for n in z.namelist()}
root=E.fromstring(package['word/document.xml']);body=root.find(f'{{{W}}}body')
ns={'w':W}
texts=[''.join(n.xpath('.//w:t/text()',namespaces=ns)) for n in body]
start=next(i for i,t in enumerate(texts) if t.startswith('AUTOINFLAMMATORY FEVER SYNDROMES'))
end=next(i for i,t in enumerate(texts) if t.startswith('CONNECTIVE TISSUE DISORDERS (CTDS)'))
# The preceding empty paragraph is the inserted page break at each boundary.
if not texts[start-1].strip():start-=1
if not texts[end-1].strip():end-=1
def split(dest,keep):
 r=deepcopy(root);b=r.find(f'{{{W}}}body')
 for i,n in enumerate(list(b)):
  if n.tag!=f'{{{W}}}sectPr' and not keep(i):b.remove(n)
 data=dict(package);data['word/document.xml']=E.tostring(r,xml_declaration=True,encoding='UTF-8',standalone=True)
 with ZipFile(dest,'w',ZIP_DEFLATED) as z:
  for name,content in data.items():z.writestr(name,content)
newfirst=stage/'01. Autoimmunity, Immunological Tests & Immunodeficiency.docx'
split(newfirst,lambda i:not start<=i<end)
split(parts/'0.docx',lambda i:start<=i<end)
for i,p in enumerate(files[9:],1):shutil.copyfile(p,parts/f'{i}.docx')
others=stage/'10. Others.docx'
merge_parts(parts,others)
def inspect(paths):
 text=Counter();tables=0;images=Counter()
 for p in paths:
  with ZipFile(p) as z:
   assert z.testzip() is None
   r=E.fromstring(z.read('word/document.xml'))
   text.update(r.xpath('//w:body//w:t/text()',namespaces=ns))
   tables+=len(r.xpath('//w:body//w:tbl',namespaces=ns))
   rels={n.get('Id'):n for n in E.fromstring(z.read('word/_rels/document.xml.rels'))}
   for node in r.iter():
    for k,v in node.attrib.items():
     if E.QName(k).namespace=='http://schemas.openxmlformats.org/officeDocument/2006/relationships':
      rel=rels[v]
      if rel.get('Type').endswith('/image'):
       import posixpath
       images[hashlib.sha256(z.read(posixpath.normpath(posixpath.join('word',rel.get('Target'))))).hexdigest()]+=1
 return text,tables,images
expected=inspect(files)
assert expected==inspect([newfirst,*files[1:9],others])
print('Verified all text, tables and image references preserved across 10 documents.')
if '--install' in sys.argv:
 backup=SOURCE.parent.parent/'backups'/('rheumatology-before-others-'+time.strftime('%Y%m%d-%H%M%S')+'.zip')
 changed=[first,*files[9:]]
 with ZipFile(backup,'x',ZIP_DEFLATED) as z:
  for p in changed:z.write(p,p.name)
 with ZipFile(backup) as z:
  for p in changed:assert z.read(p.name)==p.read_bytes()
 for p in (newfirst,others):
  target=SOURCE/p.name;assert not target.exists();shutil.copyfile(p,target)
  assert target.read_bytes()==p.read_bytes()
 for p in changed:
  assert p.parent.resolve()==SOURCE.resolve();p.unlink()
 assert len(list(SOURCE.glob('*.docx')))==10
 assert inspect(SOURCE.glob('*.docx'))==expected
 print('Installed 10. Others.docx; updated chapter 01; backup:',backup)
