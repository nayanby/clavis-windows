"""Import the user's A1 Quick Style set without resaving clinical document content."""
import argparse,copy,hashlib,io,json,os,re,time
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
from lxml import etree as E
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main';N={'w':W}
def q(k):return '{'+W+'}'+k
def sha(b):return hashlib.sha256(b).hexdigest()
def xml(e):return E.tostring(e,xml_declaration=True,encoding='UTF-8',standalone=True)
def norm(s):return re.sub(r'[^a-z0-9]','',re.sub(r'^chapter\d+(?:_\d+)?_','',s,flags=re.I).lower())
def package(z,changes):
 out=io.BytesIO()
 with ZipFile(out,'w',ZIP_DEFLATED) as dest:
  for info in z.infolist():dest.writestr(copy.copy(info),changes.get(info.filename,z.read(info.filename)))
  for name,value in changes.items():
   if name not in z.namelist():dest.writestr(name,value)
 return out.getvalue()
def apply(raw,template):
 ts=E.fromstring(template['word/styles.xml']);tn=E.fromstring(template['word/numbering.xml'])
 with ZipFile(io.BytesIO(raw)) as z:
  s=E.fromstring(z.read('word/styles.xml'));numbering=E.fromstring(z.read('word/numbering.xml')) if 'word/numbering.xml' in z.namelist() else E.Element(q('numbering'),nsmap={'w':W})
  existing={x.get(q('styleId')):x for x in s.findall('w:style',N)}
  # Source list identifiers are retained. Imported style lists get distinct IDs.
  num_offset=max([int(x.get(q('numId'))) for x in numbering.findall('w:num',N)]+[0])+1
  abs_offset=max([int(x.get(q('abstractNumId'))) for x in numbering.findall('w:abstractNum',N)]+[0])+1
  nums={x.get(q('numId')):str(num_offset+i) for i,x in enumerate(tn.findall('w:num',N))}
  abstracts={x.get(q('abstractNumId')):str(abs_offset+i) for i,x in enumerate(tn.findall('w:abstractNum',N))}
  for original in tn.findall('w:abstractNum',N):
   node=copy.deepcopy(original);node.set(q('abstractNumId'),abstracts[original.get(q('abstractNumId'))]);first_num=numbering.find('w:num',N);numbering.insert(list(numbering).index(first_num) if first_num is not None else len(numbering),node)
  for original in tn.findall('w:num',N):
   node=copy.deepcopy(original);node.set(q('numId'),nums[original.get(q('numId'))]);ref=node.find('w:abstractNumId',N);ref.set(q('val'),abstracts[ref.get(q('val'))]);numbering.append(node)
  template_styles={x.get(q('styleId')):x for x in ts.findall('w:style',N)}
  byname={norm(x.find('w:name',N).get(q('val'))):x for x in template_styles.values() if x.find('w:name',N) is not None and not x.get(q('styleId'),'').lower().startswith('chapter')}
  def clone_style(original,sid=None,name=None):
   node=copy.deepcopy(original)
   if sid:node.set(q('styleId'),sid)
   if name is not None:node.find('w:name',N).set(q('val'),name)
   # Keep headings attached to their first paragraph when the source style omits pagination controls.
   if node.get(q('type'))=='paragraph' and re.search(r'heading[1-9]|boldside[1-4]',norm(node.get(q('styleId'),''))):
    pp=node.find('w:pPr',N)
    if pp is None:pp=E.Element(q('pPr'));rp=node.find('w:rPr',N);node.insert(list(node).index(rp) if rp is not None else len(node),pp)
    if pp.find('w:keepNext',N) is None:pp.insert(0,E.Element(q('keepNext')))
   for ref in node.findall('.//w:numId',N):
    val=ref.get(q('val'))
    if val in nums:ref.set(q('val'),nums[val])
   return node
  # Update original aliases too, so merged-chapter headings retain their levels.
  for sid,old in existing.items():
   name=old.find('w:name',N);target=template_styles.get(sid)
   if target is None:target=byname.get(norm(name.get(q('val')) if name is not None else sid))
   if target is not None:s.replace(old,clone_style(target,sid,name.get(q('val')) if name is not None else None))
  for sid,node in template_styles.items():
   if sid not in existing:s.append(clone_style(node))
  for tag in ['docDefaults','latentStyles']:
   old=s.find('w:'+tag,N);new=ts.find('w:'+tag,N)
   if old is not None:s.remove(old)
   if new is not None:s.insert(0 if tag=='docDefaults' else (1 if s.find('w:docDefaults',N) is not None else 0),copy.deepcopy(new))
  changes={'word/styles.xml':xml(s),'word/numbering.xml':xml(numbering)}
  if 'word/theme/theme1.xml' in z.namelist():changes['word/theme/theme1.xml']=template['word/theme/theme1.xml']
  if 'word/numbering.xml' not in z.namelist():
   relns='http://schemas.openxmlformats.org/package/2006/relationships';ctns='http://schemas.openxmlformats.org/package/2006/content-types'
   rel=E.fromstring(z.read('word/_rels/document.xml.rels'));entry=E.SubElement(rel,'{'+relns+'}Relationship');entry.set('Id','rIdPearlsA1Numbering');entry.set('Type',W.replace('wordprocessingml/2006/main','officeDocument/2006/relationships/numbering'));entry.set('Target','numbering.xml');changes['word/_rels/document.xml.rels']=xml(rel)
   ct=E.fromstring(z.read('[Content_Types].xml'));entry=E.SubElement(ct,'{'+ctns+'}Override');entry.set('PartName','/word/numbering.xml');entry.set('ContentType','application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml');changes['[Content_Types].xml']=xml(ct)
  result=package(z,changes)
  with ZipFile(io.BytesIO(result)) as check:
   assert check.read('word/document.xml')==z.read('word/document.xml')
   for name in z.namelist():
    if name not in changes:assert check.read(name)==z.read(name),name
  return result

def main():
 a=argparse.ArgumentParser();a.add_argument('--publish',action='store_true');args=a.parse_args()
 root=Path(r'C:/Users/ANT-PC/OneDrive/Cortex Windows/data/files');out=Path('outputs/a1-library-style');out.mkdir(parents=True,exist_ok=True);manifest=out/'manifest.json'
 if args.publish:
  report=json.loads(manifest.read_text());done=[];locked=list(report.get('locked',[]))
  for rec in report['documents']:
   p=Path(rec['path']);new=out/'documents'/p.relative_to(root)
   try:
    data=p.read_bytes()
    if sha(data)==rec['after']:done.append(str(p));continue
    if sha(data)!=rec['before']:locked.append('Changed since staging: '+str(p));continue
    tmp=p.with_name('.a1-quickstyle.tmp');tmp.write_bytes(new.read_bytes());os.replace(tmp,p);assert sha(p.read_bytes())==rec['after'];done.append(str(p))
   except PermissionError:locked.append(str(p))
  (out/'publication.json').write_text(json.dumps({'updated':done,'locked':locked},indent=2));print('PUBLISHED',len(done),'PENDING',locked);return
 template_path=Path(r'C:/Users/ANT-PC/AppData/Roaming/Microsoft/QuickStyles/A1.dotx')
 with ZipFile(template_path) as z:template={name:z.read(name) for name in z.namelist()}
 report={'template':str(template_path),'template_sha256':sha(template_path.read_bytes()),'documents':[],'locked':[]}
 (out/'A1.dotx').write_bytes(template_path.read_bytes())
 with ZipFile(out/'before.zip','x',ZIP_DEFLATED) as backups:
  for p in sorted(root.rglob('*.docx')):
   if p.name.startswith('~$'):continue
   try:raw=p.read_bytes()
   except PermissionError:report['locked'].append(str(p));continue
   backups.writestr(p.relative_to(root).as_posix(),raw);new=apply(raw,template);target=out/'documents'/p.relative_to(root);target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(new);report['documents'].append({'path':str(p),'before':sha(raw),'after':sha(new)})
 manifest.write_text(json.dumps(report,indent=2));print('STAGED',len(report['documents']),'LOCKED',report['locked'])
if __name__=='__main__':main()

