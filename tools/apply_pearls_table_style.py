"""Install the reference Autoimmunity table design as a named library table style."""
import argparse, copy, hashlib, io, json, os
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from lxml import etree as E
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main';N={'w':W}
def q(name):return '{'+W+'}'+name
def el(name,**attrs):return E.Element(q(name),{q(k):v for k,v in attrs.items()})
def remove(parent,names):
 for c in list(parent):
  if E.QName(c).localname in names:parent.remove(c)
def add(parent,name,**attrs):
 remove(parent,[name]);c=el(name,**attrs);parent.append(c);return c
def digest(data):return hashlib.sha256(data).hexdigest()
def pack(z,changes):
 out=io.BytesIO()
 with ZipFile(out,'w',ZIP_DEFLATED) as dest:
  for info in z.infolist():dest.writestr(copy.copy(info),changes.get(info.filename,z.read(info.filename)))
 return out.getvalue()
def xml(root):return E.tostring(root,xml_declaration=True,encoding='UTF-8',standalone=True)
def semantic(d):
 # Include content, relationships, math, shapes and the exact grid/merge structure.
 return [(E.QName(x).localname, x.text,tuple(sorted(x.attrib.items()))) for x in d.iter() if E.QName(x).localname in {'t','instrText','delText','blip','imagedata','gridCol','gridSpan','vMerge','tcW','oMath','extent','br','tab','sym'}]
def transform(raw,style,p):
 with ZipFile(io.BytesIO(raw)) as z:
  d=E.fromstring(z.read('word/document.xml'));s=E.fromstring(z.read('word/styles.xml'));before=semantic(d)
  for st in s.findall("w:style[@w:styleId='PearlsTable']",N):s.remove(st)
  s.append(copy.deepcopy(style));tables=d.findall('.//w:tbl',N)
  for table in tables:
   pr=table.find('w:tblPr',N)
   if pr is None:pr=el('tblPr');table.insert(0,pr)
   remove(pr,['tblStyle','jc','tblBorders','shd','tblCellMar','tblStyleRowBandSize','tblStyleColBandSize','tblLook'])
   pr.insert(0,el('tblStyle',val='PearlsTable'))
   pr.append(el('tblLook',val='0220',firstRow='1',lastRow='0',firstColumn='0',lastColumn='0',noHBand='0',noVBand='1'))
   pr.append(copy.deepcopy(style.find('w:tblPr/w:tblBorders',N)))
   for ri,row in enumerate(table.findall('w:tr',N)):
    rp=row.find('w:trPr',N)
    if rp is not None:remove(rp,['cnfStyle'])
    if ri==0:
     if rp is None:rp=el('trPr');row.insert(0,rp)
     add(rp,'tblHeader')
    for cell in row.findall('w:tc',N):
     cp=cell.find('w:tcPr',N)
     if cp is not None:remove(cp,['shd','tcBorders','tcMar','cnfStyle'])
     else:cp=el('tcPr');cell.insert(0,cp)
     border=el('tcBorders')
     for side in ['top','left','bottom','right']:border.append(el(side,val='single',sz='4',space='0',color='D9D9D9'))
     cp.append(border);cp.append(el('shd',val='clear',color='auto',fill='E7E1E4' if ri==0 else ('F8F6F8' if ri%2 else 'FFFFFF')))
     # Only this table's cells; nested tables are processed independently.
     for para in cell.findall('w:p',N):
      pp=para.find('w:pPr',N)
      if pp is None:pp=el('pPr');para.insert(0,pp)
      remove(pp,['pStyle','shd','pBdr','spacing','cnfStyle','rPr'])
      pp.insert(0,el('pStyle',val='Normal'))
      pp.append(el('spacing',before='24',after='48',line='249',lineRule='auto'))
      for run in para.findall('.//w:r',N):
       rpr=run.find('w:rPr',N)
       if rpr is None:rpr=el('rPr');run.insert(0,rpr)
       remove(rpr,['rStyle','rFonts','sz','szCs','color','shd'])
       rpr.insert(0,el('rFonts',ascii='Averia Serif Libre',hAnsi='Averia Serif Libre',cs='Averia Serif Libre'))
       rpr.append(el('color',val='5C3A52' if ri==0 else '000000'));rpr.append(el('sz',val='19'));rpr.append(el('szCs',val='19'))
       if ri==0:add(rpr,'b');add(rpr,'bCs')
  assert semantic(d)==before, str(p)
  # WordprocessingML property order, including explicit overrides.
  orders={'rPr':'rStyle rFonts b bCs i iCs caps smallCaps strike dstrike outline shadow emboss imprint noProof snapToGrid vanish webHidden color spacing w kern position sz szCs highlight u effect bdr shd fitText vertAlign rtl cs em lang eastAsianLayout specVanish oMath rPrChange','tblPr':'tblStyle tblpPr tblOverlap bidiVisual tblStyleRowBandSize tblStyleColBandSize tblW jc tblCellSpacing tblInd tblBorders shd tblLayout tblCellMar tblLook tblCaption tblDescription tblPrChange','pPr':'pStyle keepNext keepLines pageBreakBefore framePr widowControl numPr suppressLineNumbers pBdr shd tabs suppressAutoHyphens kinsoku wordWrap overflowPunct topLinePunct autoSpaceDE autoSpaceDN bidi adjustRightInd snapToGrid spacing ind contextualSpacing mirrorIndents suppressOverlap jc textDirection textAlignment textboxTightWrap outlineLvl divId cnfStyle rPr sectPr pPrChange'}
  for name,order in orders.items():
   keys=order.split()
   for pr in d.findall('.//w:'+name,N):
    for c in sorted(list(pr),key=lambda c:keys.index(E.QName(c).localname) if E.QName(c).localname in keys else len(keys)):pr.append(c)
  new=pack(z,{'word/document.xml':xml(d),'word/styles.xml':xml(s)})
  with ZipFile(io.BytesIO(new)) as check:
   assert check.testzip() is None
   for name in z.namelist():
    if name not in {'word/document.xml','word/styles.xml'}:assert z.read(name)==check.read(name)
 return new,len(tables)
def main():
 a=argparse.ArgumentParser();a.add_argument('--publish',action='store_true');args=a.parse_args()
 root=Path(r'C:/Users/ANT-PC/OneDrive/Cortex Windows/data/files');out=Path('outputs/library-table-style-light');out.mkdir(parents=True,exist_ok=True)
 ref=root/'Rheumatology/1. Autoimmunity, Immunological Tests & Immunodeficiency.docx'
 if args.publish:
  report=json.loads((out/'report.json').read_text());done=[];locked=[]
  for rec in report['documents']:
   p=Path(rec['path']);stage=out/'documents'/p.relative_to(root)
   if digest(p.read_bytes())==rec['after']:done.append(str(p));continue
   if digest(p.read_bytes())!=rec['before']:locked.append('Changed since staging: '+str(p));continue
   temp=p.with_name('.pearls-table-style.tmp')
   try:
    temp.write_bytes(stage.read_bytes());os.replace(temp,p);assert digest(p.read_bytes())==rec['after'];done.append(str(p))
   except PermissionError:locked.append(str(p));temp.unlink(missing_ok=True)
  (out/'publication.json').write_text(json.dumps({'updated':done,'locked':locked},indent=2));print('UPDATED',len(done),'LOCKED',len(locked));return
 style=E.fromstring((Path(__file__).resolve().parents[1]/'assets/word/PearlsTable.xml').read_bytes())
 (out/'PearlsTable.xml').write_bytes(xml(style))
 report={'reference':str(ref),'style':'Pearls Table','documents':[],'tables':0}
 backup=out/'before.zip'
 with ZipFile(backup,'x',ZIP_DEFLATED) as backups:
  for p in sorted(root.rglob('*.docx')):
   if p.name.startswith('~$'):continue
   raw=p.read_bytes();backups.writestr(p.relative_to(root).as_posix(),raw)
   new,table_count=transform(raw,style,p)
   target=out/'documents'/p.relative_to(root);target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(new)
   report['documents'].append({'path':str(p),'tables':table_count,'before':digest(raw),'after':digest(new)});report['tables']+=table_count
 (out/'report.json').write_text(json.dumps(report,indent=2));print('STAGED',len(report['documents']),'TABLES',report['tables'])
if __name__=='__main__':main()
