import sys,re,json
from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from apply_clinical_template import NS,W,list_signature
from enforce_clinical_style_palette import choose_paragraph
ROOT=Path(r'C:/Users/ANT-PC/OneDrive/Cortex Windows/data/files')
RANK={'Heading1':0,'Heading2':1,'Heading3':2,'Heading4':3,'BoldSide1':4,'boldside2':5,'Boldside3':6,'boldside4':7}
def text(p):return ''.join(p.xpath('.//w:t/text()',namespaces=NS)).strip()
def sid(p):return p.xpath('string(w:pPr/w:pStyle/@w:val)',namespaces=NS)
def bold(p,styles):
 def inherited(style,seen=None):
  seen=set(seen or ())
  if not style or style in seen or style not in styles:return None
  seen.add(style);s=styles[style];n=s.find('w:rPr/w:b',NS)
  if n is not None:return n.get('{'+W+'}val','true') not in ('0','false','off')
  return inherited(s.xpath('string(w:basedOn/@w:val)',namespaces=NS),seen)
 default=inherited(sid(p));total=0;strong=0
 for r in p.findall('.//w:r',NS):
  t=text(r)
  if not t:continue
  n=r.find('w:rPr/w:b',NS)
  b=(n.get('{'+W+'}val','true') not in ('0','false','off')) if n is not None else inherited(r.xpath('string(w:rPr/w:rStyle/@w:val)',namespaces=NS))
  if b is None:b=default
  total+=len(t);strong+=len(t) if b else 0
 return bool(total and strong/total>.95)
def scan(path):
 with ZipFile(path) as z:
  root=E.fromstring(z.read('word/document.xml'));styles=E.fromstring(z.read('word/styles.xml'));numbering=E.fromstring(z.read('word/numbering.xml')) if 'word/numbering.xml' in z.namelist() else E.Element('{'+W+'}numbering')
 definitions={s.get('{'+W+'}styleId'):s for s in styles.findall('w:style',NS)}
 ps=root.findall('.//w:p',NS);lists=list_signature(root,styles,numbering);rows=[]
 for i,p in enumerate(ps):
  if p.xpath('ancestor::w:tc|ancestor::w:txbxContent',namespaces=NS):continue
  t=text(p)
  if not t:continue
  semantic=choose_paragraph(p,definitions)[0]
  rows.append(dict(i=i,text=t,style=semantic if semantic in RANK else sid(p),listing=lists[i],bold=bold(p,definitions)))
 candidates=[]
 for pos,row in enumerate(rows):
  t=row['text']
  p=ps[row['i']]
  if p.xpath('.//w:hyperlink|.//w:fldSimple|.//w:drawing|.//w:pict|.//m:oMath',namespaces={**NS,'m':'http://schemas.openxmlformats.org/officeDocument/2006/math'}):continue
  if re.search(r'MD/DNB|GENERAL MEDICINE|\bPAGE\s+\d|\|\s*\d',t,re.I):continue
  if t.isupper() and len(t.split())==1 and t not in {'MANAGEMENT','TREATMENT','DIAGNOSIS','INVESTIGATIONS','COMPLICATIONS','PROGNOSIS','EPIDEMIOLOGY','PATHOPHYSIOLOGY','ETIOLOGY','DEFINITION','CLASSIFICATION','PREVENTION','THERAPY'}:continue
  if row['style'] in RANK or row['style'] in ('Title','image') or row['listing'] is not None:continue
  if len(t)>155 or len(t.split())>18 or re.search(r'[.!?;]$',t) or re.match(r'^(?:fig(?:ure)?|table|source|reference|note)\b',t,re.I):continue
  if re.search(r'[=<>→]|\d\s*(?:mg|mm|cm|ml|kg|%|mmHg)\b',t,re.I):continue
  following=rows[pos+1] if pos+1<len(rows) else None
  if following is None:continue
  prior=next((r for r in reversed(rows[:pos]) if r['style'] in RANK),None)
  if prior and re.search(r'references|bibliograph|further reading',prior['text'],re.I):continue
  major=t.isupper() and following['style'] in RANK and RANK[following['style']]>0
  if not row['bold'] and not major:continue
  numbered=bool(re.match(r'^\d+[.)]\s+\S',t))
  letter=bool(re.match(r'^[A-Z][.)]\s+\S',t))
  if major or ((numbered or letter or (len(t.split())>=2)) and following['listing'] is not None):
   candidates.append(dict(**row,major=major,preceding=prior and [prior['style'],prior['text']],following=[following['style'],following['text'][:90]]))
 return root,styles,numbering,ps,rows,candidates
if __name__=='__main__':
 report=[]
 for path in sorted(ROOT.rglob('*.docx')):
  if path.name.startswith('~$') or any(p.startswith(('_','.')) for p in path.relative_to(ROOT).parts[:-1]):continue
  *_,candidates=scan(path)
  if candidates:report.append(dict(file=path.relative_to(ROOT).as_posix(),candidates=candidates))
 Path('build/missing-heading-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
 print('Files',len(report),'Candidates',sum(len(x['candidates']) for x in report))
 for row in report[:12]:
  print(row['file'])
  for c in row['candidates'][:7]:print(c['i'],c['text'],c['major'],c['preceding'])
