"""Record the user's ordered scope, selecting canonical chapter sets without duplicates."""
import json,re
from qbank_json_chapters import ROOT,DATA,SUBJECTS,validate

def number(name):
    m=re.match(r'(?:Chapter_)?(\d+)',name,re.I)
    if m:return int(m[1])
    m=re.match(r'(?:CH|chapter)\s*(\d+)',name,re.I)
    if m:return int(m[1])
    roman={'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'VII':7,'VIII':8,'IX':9,'X':10,'XI':11,'XII':12,'XIII':13,'XIV':14}
    return roman.get(name.split('.')[0],1)

def main():
    existing=json.loads((ROOT/'progress.json').read_text(encoding='utf-8'))
    bykey={(x['subject'],x['document']):x for x in existing['chapters']}
    chapters=[]
    for subject in SUBJECTS:
        names=[p.stem for p in (DATA/'files'/subject).glob('*.docx')]
        if subject in {'Cardiology','Endocrine','Nephrology'}:names=[n for n in names if n.startswith('Chapter_')]
        if subject=='GI & pancreas':names=[n for n in names if re.match(r'^\d+[.]',n)]
        for name in sorted(names,key=lambda x:(number(x),x.casefold())):
            row=bykey.get((subject,name),dict(subject=subject,chapter=number(name),document=name,status='pending'))
            bank=ROOT/subject/(name+'.json')
            if bank.exists() and row['status']=='pending':
                b=json.loads(bank.read_text(encoding='utf-8'));row.update(status='authored_validated',file=bank.relative_to(ROOT).as_posix(),validation=validate(b))
            chapters.append(row)
    # Preserve any later explicitly added chapter rather than dropping it on refresh.
    keys={(x['subject'],x['document']) for x in chapters}
    chapters.extend(x for k,x in bykey.items() if k not in keys)
    plan=dict(subjectOrder=SUBJECTS,delivery='JSON only; one chapter at a time',
      defaultQuestions=30,broadChapterQuestions=40,
      selectionPolicy='Use canonical numbered sets. Exclude older overlapping Endocrine/GI sets, duplicate Biostatistics folder and unnamed placeholders. Oncology currently has one source chapter (Basics); expand its coverage explicitly if needed.',
      currentChapter='Neurology 02. Cerebrovascular Diseases',chapters=chapters)
    (ROOT/'progress.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(dict(plannedChapters=len(chapters),bySubject={s:sum(x['subject']==s for x in chapters) for s in SUBJECTS}),indent=2))

if __name__=='__main__':main()
