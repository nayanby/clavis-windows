"""Split existing Rheumatology sources without rewriting their OOXML content."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from copy import deepcopy
import json
from lxml import etree as E
from docx import Document

SOURCE = Path(r'C:\Users\ANT-PC\OneDrive\Cortex Windows\data\files\Rheumatology')
OUT = Path(__file__).resolve().parents[1] / 'build/rheumatology-arranged'
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
files = sorted(SOURCE.glob('*.docx'))
assert len(files) == 5
packages = [dict((n, z.read(n)) for n in z.namelist()) for p in files for z in [ZipFile(p)]]
bodies = [E.fromstring(p['word/document.xml']).find(f'{{{W}}}body') for p in packages]
specs = [
 ('01. Autoimmunity, Immunological Tests, Autoinflammatory Diseases & Immunodeficiency', [(2,0,867),(1,573,870),(3,0,70)]),
 ('02. Rheumatoid Arthritis', [(0,0,361)]),
 ('03. Spondyloarthritis & Psoriatic Arthritis', [(0,618,1354)]),
 ('04. Systemic Lupus Erythematosus & Antiphospholipid Syndrome', [(3,70,320),(3,659,815)]),
 ('05. Systemic Sclerosis, Sjögren Syndrome & Overlap Syndromes', [(3,456,659),(3,815,None)]),
 ('06. Idiopathic Inflammatory Myopathies', [(3,320,456)]),
 ('07. Large-, Medium- & Small-Vessel Vasculitis', [(4,0,None)]),
 ('08. Crystal Arthropathies & Osteoarthritis', [(0,1354,None)]),
 ('09. Biologics', [(2,867,None)]),
 ('10. Juvenile Idiopathic Arthritis', [(0,361,618)]),
 ('11. Sarcoidosis', [(1,0,210)]),
 ('12. IgG4-Related Disease', [(1,210,342)]),
 ('13. Hemophagocytic Lymphohistiocytosis', [(1,342,573)]),
 ('14. Fibromyalgia', [(1,870,973)]),
 ('15. Cytokine Release Syndrome', [(1,973,1063)]),
 ('16. Relapsing Polychondritis', [(1,1063,None)]),
]

def nodes(s,a,b):
 return [n for n in list(bodies[s])[a:b] if n.tag != f'{{{W}}}sectPr']

def write(path, slices):
 s=slices[0][0]; package=dict(packages[s]); root=E.fromstring(package['word/document.xml']); body=root.find(f'{{{W}}}body')
 section=deepcopy(body.find(f'{{{W}}}sectPr'))
 for n in list(body): body.remove(n)
 for source,a,b in slices:
  assert source==s
  for n in nodes(source,a,b): body.append(deepcopy(n))
 if section is not None: body.append(section)
 package['word/document.xml']=E.tostring(root,xml_declaration=True,encoding='UTF-8',standalone=True)
 with ZipFile(path,'w',ZIP_DEFLATED) as z:
  for name,data in package.items(): z.writestr(name,data)

def main():
 OUT.mkdir(parents=True,exist_ok=True)
 coverage=[[] for _ in files]
 report=[]
 for name,slices in specs:
  for s,a,b in slices: coverage[s].extend(range(a,b if b is not None else len(bodies[s])-1))
  if len({s for s,a,b in slices})==1: write(OUT/(name+'.docx'),slices)
  else:
   parts=OUT/'parts'; parts.mkdir(exist_ok=True)
   for i,part in enumerate(slices): write(parts/f'{i}.docx',[part])
   merge_parts(parts, OUT/(name+'.docx'))
  report.append({'chapter':name,'sources':[{'file':files[s].name,'start':a,'end':b} for s,a,b in slices]})
 for i,indices in enumerate(coverage):
  expected=[j for j,n in enumerate(bodies[i]) if n.tag!=f'{{{W}}}sectPr']
  assert sorted(indices)==expected,files[i]
 (OUT/'mapping.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
 print('All source body elements mapped exactly once into 16 chapters.')

def merge_parts(parts, target):
 doc=Document(parts/'0.docx')
 for index in (1,2):
  other=Document(parts/f'{index}.docx')
  prefix=f'import{index}_'
  stylemap={s.style_id:prefix+s.style_id for s in other.styles}
  for style in other.styles:
   node=deepcopy(style.element)
   node.set(f'{{{W}}}styleId',stylemap[style.style_id])
   for ref in node.iter():
    if ref.tag in [f'{{{W}}}{t}' for t in ('basedOn','next','link')]:
     value=ref.get(f'{{{W}}}val')
     if value in stylemap:ref.set(f'{{{W}}}val',stylemap[value])
   doc.styles.element.append(node)
  numbering=doc.part.numbering_part.element
  incoming=other.part.numbering_part.element
  maps={}
  for kind,attr in [('abstractNum','abstractNumId'),('num','numId')]:
   used=[int(n.get(f'{{{W}}}{attr}')) for n in numbering.findall(f'{{{W}}}{kind}')]
   offset=max(used,default=0)+1
   maps[kind]={n.get(f'{{{W}}}{attr}'):str(offset+i) for i,n in enumerate(incoming.findall(f'{{{W}}}{kind}'))}
  for n in incoming:
   kind=E.QName(n).localname
   if kind not in maps:continue
   n=deepcopy(n);attr='abstractNumId' if kind=='abstractNum' else 'numId'
   n.set(f'{{{W}}}{attr}',maps[kind][n.get(f'{{{W}}}{attr}')])
   for ref in n.iter():
    if ref.tag==f'{{{W}}}abstractNumId':ref.set(f'{{{W}}}val',maps['abstractNum'][ref.get(f'{{{W}}}val')])
    if ref.tag in [f'{{{W}}}{t}' for t in ('pStyle','styleLink','numStyleLink')]:
     val=ref.get(f'{{{W}}}val')
     if val in stylemap:ref.set(f'{{{W}}}val',stylemap[val])
   numbering.append(n)
  doc.add_page_break()
  for original in other.element.body:
   if original.tag==f'{{{W}}}sectPr':continue
   n=deepcopy(original)
   for ref in n.iter():
    if ref.tag in [f'{{{W}}}{t}' for t in ('pStyle','rStyle','tblStyle')]:
     val=ref.get(f'{{{W}}}val')
     if val in stylemap:ref.set(f'{{{W}}}val',stylemap[val])
    if ref.tag==f'{{{W}}}numId':
     val=ref.get(f'{{{W}}}val')
     if val in maps['num']:ref.set(f'{{{W}}}val',maps['num'][val])
    for key,value in list(ref.attrib.items()):
     if E.QName(key).namespace=='http://schemas.openxmlformats.org/officeDocument/2006/relationships':
      rel=other.part.rels[value]
      ref.set(key,doc.part.relate_to(rel.target_ref if rel.is_external else rel.target_part,rel.reltype,rel.is_external))
   doc.element.body.insert(len(doc.element.body)-1,n)
 doc.save(target)

if __name__=='__main__':main()
