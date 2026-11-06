"""Import only the fifteen explicitly supplied Neurology HTML modules as JSON."""
import argparse, copy, hashlib, json, re, sys, time, zipfile
from pathlib import Path
from lxml import html
from import_replacement_html_archives import REPO, DATA, INSTALL, extract, convert, clean, rich
from cnl_desktop import study_packs, paths

OUT=REPO/'build/neurology-modules-20261106'
DOWNLOADS=Path('C:/Users/ANT-PC/Downloads')
SPECS=[
 ('NEET_SS_Neurology_Chapter_01_Cerebrovascular_Diseases_45_Interactive.html','Cerebrovascular Diseases',45),
 ('Neurology_Chapter_02_Epilepsy_40_MCQs_REUPLOAD.html','Epilepsy',40),
 ('NEET_SS_Neurology_Chapter_03_Headache_Disorders_25_Interactive.html','Headache Disorders',25),
 ('NEET_SS_Neurology_Chapter_04_Demyelinating_Disorders_35_Interactive.html','Demyelinating Disorders',35),
 ('NEET_SS_Neurology_Chapter_05_Movement_Disorders_35_Interactive.html','Movement Disorders',35),
 ('NEET_SS_Neurology_Chapter_06_Neuromuscular_Junction_Disorders_25_Interactive.html','Neuromuscular Junction Disorders',25),
 ('NEET_SS_Neurology_Chapter_07_Peripheral_Neuropathy_35_Interactive.html','Peripheral Neuropathy',35),
 ('NEET_SS_Neurology_Chapter_08_Motor_Neuron_Muscle_Diseases_35_Interactive.html','Motor Neuron and Muscle Diseases',35),
 ('NEET_SS_Neurology_Chapter_09_Dementia_Cognitive_Disorders_30_Interactive.html','Dementia and Cognitive Disorders',30),
 ('NEET_SS_Neurology_Chapter_10_CNS_Infections_38_Interactive.html','CNS Infections',38),
 ('NEET_SS_Neurology_Chapter_11_Neuroimmunology_Inflammatory_Disorders_25_Interactive.html','Neuroimmunology and Inflammatory Disorders',25),
 ('NEET_SS_Neurology_Chapter_12_Spinal_Cord_Disorders_25_Interactive.html','Spinal Cord Disorders',25),
 ('NEET_SS_Neurology_Chapter_13_Neuroanatomy_Clinical_Localization_35_Interactive.html','Neuroanatomy and Clinical Localization',35),
 ('NEET_SS_Neurology_Chapter_14_Neurodiagnostics_30_Interactive.html','Neurodiagnostics',30),
 ('NEET_SS_Neurology_Chapter_15_Neurocritical_Care_30_Interactive.html','Neurocritical Care',30),
]

def stage():
 OUT.mkdir(parents=True,exist_ok=True)
 banks=[];files=[]
 for order,(name,title,count) in enumerate(SPECS,1):
  raw=(DOWNLOADS/name).read_bytes();digest=hashlib.sha256(raw).hexdigest()
  items=extract(raw.decode('utf-8-sig'));assert len(items)==count,(name,len(items))
  qs=[]
  for i,item in enumerate(items,1):
   base=copy.deepcopy(item)
   reviews=[base.pop(k) for k in ['other','others','wrongs'] if base.get(k)]
   q=convert(base,digest,i)
   # Some supplied files use stale numeric distractor indexes after shuffling.
   # Preserve their explanations without assigning them to a different option.
   reasons=[]
   for review in reviews:
    entries=list(review.values()) if isinstance(review,dict) else review if isinstance(review,list) else [review]
    for entry in entries:
     if isinstance(entry,str):reasons.append(rich(entry))
     elif isinstance(entry,list) and len(entry)==2 and isinstance(entry[0],int):reasons.append(rich(entry[1]))
     elif isinstance(entry,dict):
      label=entry.get('option','');reason=entry.get('reason',entry.get('why',''))
      reasons.append(('<strong>'+rich(label)+':</strong> ' if label else '')+rich(reason))
     else:raise ValueError((name,i,entry))
   assert reasons,(name,i,'Missing distractor explanation')
   q['explanationHtml']=clean(q['explanationHtml']+'<h3>Other Options</h3><ul>'+''.join('<li>'+r+'</li>' for r in reasons)+'</ul>')
   q['sourceQuestion']=copy.deepcopy(item)
   # These HTML schemas also carry a separate clinical pearl. Keep it visible,
   # while retaining the exact original object in sourceQuestion for audit.
   if item.get('pearl'):
    q['explanationHtml']=clean(q['explanationHtml']+'<h3>Key point</h3><p>'+rich(item['pearl'])+'</p>')
   q['explanation']=html.fragment_fromstring(q['explanationHtml'],create_parent='div').text_content().strip()
   if item.get('topic'):
    q['topic']=re.sub(r'^\s*NEET[\s-]*SS\s*[·:–-]?\s*','',str(item['topic']),flags=re.I)
   dom=html.fragment_fromstring(q['explanationHtml'],create_parent='div')
   assert not dom.xpath('.//script|.//iframe|.//*[@onclick or @onload]')
   assert 'Other Options' in dom.text_content(),(name,i,'Missing distractor review')
   assert q['sourceQuestion']==item
   qs.append(q)
  bank=dict(folder='Neurology',document=title,headingText=title,chapterOrder=order,topicOrder=1,
            headingIndex=0,questions=qs,sourceFile=name,sourceSha256=digest,madeAt=int(time.time()*1000))
  label=study_packs._quiz_component(title)
  dest=OUT/'staged'/'Neurology'/f'{order:02}. {label}'/f'01. {label}'/'questions.json'
  dest.parent.mkdir(parents=True,exist_ok=True)
  dest.write_text(json.dumps(bank,ensure_ascii=False,indent=2),encoding='utf-8')
  files.append(str(dest));banks.append(bank)
 assert sum(len(b['questions']) for b in banks)==488
 (OUT/'staging-report.json').write_text(json.dumps(dict(banks=15,questions=488,stagedFiles=files,
   modules=[dict(title=b['headingText'],order=b['chapterOrder'],questions=len(b['questions'])) for b in banks]),indent=2),encoding='utf-8')
 print('Validated 15 Neurology modules / 488 questions; answers, rich explanations, distractors and pearls preserved.')
 return banks,files

def apply(banks,files):
 study=DATA/'study-data';root=(DATA/'Qbank').resolve()
 before={p:p.read_bytes() for p in study_packs._quiz_record_files(study)}
 wanted={study_packs._quiz_row_id(b) for b in banks}
 replaced={p:v for p,v in before.items() if study_packs._quiz_row_id(json.loads(v)) in wanted}
 assert all(p.resolve().is_relative_to(root) for p in replaced)
 backup=root/'backups'/f'neurology-modules-{time.time_ns()}.zip'
 backup.parent.mkdir(parents=True,exist_ok=True)
 with zipfile.ZipFile(backup,'x',zipfile.ZIP_DEFLATED) as z:
  for p,v in replaced.items():z.writestr(p.relative_to(root).as_posix(),v)
  z.writestr('manifest.json',json.dumps(dict(replacedFiles=[str(p) for p in replaced],addedModules=15)))
 with zipfile.ZipFile(backup) as z:
  assert all(z.read(p.relative_to(root).as_posix())==v for p,v in replaced.items())
 written=[]
 try:
  for b in banks:
   row=study_packs.upsert_saved_quiz(study,b);assert row
   p=study_packs._quiz_record_path(study,row);written.append(p)
   assert json.loads(p.read_text(encoding='utf-8'))['questions']==b['questions']
  assert all(p.read_bytes()==v for p,v in before.items() if p not in replaced)
  actual=study_packs.read_quizzes(study)
  imported=[r for r in actual if study_packs._quiz_row_id(r) in wanted]
  assert len(imported)==15 and sum(len(r['questions']) for r in imported)==488
  original=paths.resource_root
  try:
   paths.resource_root=lambda:INSTALL/'_internal/assets'
   loaded=study_packs.read_quizzes(study)
   assert sum(len(r['questions']) for r in loaded if study_packs._quiz_row_id(r) in wanted)==488
  finally:paths.resource_root=original
 except Exception:
  for p in written:
   if p not in before:p.unlink(missing_ok=True)
  for p,v in replaced.items():p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(v)
  raise
 report=dict(result='PASS',modules=15,questions=488,replacedModules=len(replaced),
             preservedModules=len(before)-len(replaced),backup=str(backup),paths=[str(p) for p in written])
 (OUT/'import-report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
 # Extend the source manifest for subsequent topic-note work without regenerating
 # or replacing any previously authored HTML notes.
 manifest=REPO/'build/html-archive-replacement/staging-report.json'
 m=json.loads(manifest.read_text(encoding='utf-8'))
 keep=[]
 for f in m['stagedFiles']:
  existing=json.loads(Path(f).read_text(encoding='utf-8'))
  if study_packs._quiz_row_id(existing) not in wanted:keep.append(f)
 m['stagedFiles']=keep+files;m['banks']=len(m['stagedFiles'])
 m['questions']=sum(len(json.loads(Path(f).read_text(encoding='utf-8'))['questions']) for f in m['stagedFiles'])
 manifest.write_text(json.dumps(m,indent=2),encoding='utf-8')
 print(json.dumps({k:v for k,v in report.items() if k!='paths'},indent=2))

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--apply',action='store_true');args=parser.parse_args()
 banks,files=stage()
 if args.apply:apply(banks,files)
