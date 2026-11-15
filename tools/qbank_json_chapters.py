"""Common serializer, validation and additive installation for new JSON chapters."""
import argparse, collections, copy, hashlib, json, random, re, sys, time, zipfile
from html import escape
from html.parser import HTMLParser
from pathlib import Path

REPO=Path(__file__).resolve().parents[1]
ROOT=REPO/'Qbank Rebuild'
DATA=Path('C:/Users/ANT-PC/OneDrive/Cortex Windows/data')
SUBJECTS=['Neurology','Cardiology','Rheumatology','Endocrine','Nephrology','Critical Care','Infectious disease','GI & pancreas','Hepatology','Oncology','Research Methodology & Biostatistics']

def rich(s):
    s=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',escape(s))
    return re.sub(r'==(.+?)==',r'<mark>\1</mark>',s)

def question(topic,title,stem,answer,others,sections,refs,table=None,style='clinical_scenario',calculation=False):
    return dict(topic=topic,title=title,question=stem,answer=answer,others=others,sections=sections,refs=refs,table=table,style=style,calculation=calculation)

def validate(bank):
    rows=bank['questions'];assert len(rows)==bank['targetQuestions'] and rows
    assert len({q['id'] for q in rows})==len(rows)
    assert len({q['question'] for q in rows})==len(rows)
    counts=collections.Counter(q['correctIndex'] for q in rows)
    assert max(counts.get(i,0) for i in range(4))-min(counts.get(i,0) for i in range(4))<=1
    for q in rows:
        assert len(q['options'])==len(set(q['options']))==4
        assert isinstance(q['correctIndex'],int) and 0<=q['correctIndex']<4
        d=q['explanationTeaching'];assert len(d['sections'])>=2
        if not q.get('calculation'):
            assert {x['optionIndex'] for x in d['otherOptions']}==set(range(4))-{q['correctIndex']}
            assert all(len(x['explanation'].split())>=10 for x in d['otherOptions'])
        assert q['references'] and all(x['url'].startswith('https://') for x in q['references'])
        assert len(q['explanation'].split())>=180,(q['id'],len(q['explanation'].split()))
        assert '<h2>' in q['explanationHtml'] and '<strong>' in q['explanationHtml']
        # Parse and balance all generated HTML, including nested lists and table wrappers.
        class Check(HTMLParser):
            def __init__(self):super().__init__();self.stack=[]
            def handle_starttag(self,t,a):self.stack.append(t)
            def handle_endtag(self,t):assert self.stack.pop()==t,(q['id'],t)
        check=Check();check.feed(q['explanationHtml']);assert not check.stack
    return dict(questions=len(rows),answerDistribution={chr(65+i):counts[i] for i in range(4)},
        minimumExplanationWords=min(len(q['explanation'].split()) for q in rows),
        distractorRationales=sum(len(q['explanationTeaching']['otherOptions']) for q in rows),
        questionStyles=dict(collections.Counter(q.get('questionStyle','unspecified') for q in rows)),status='passed')

def save(subject,number,document,rows,refs,source_note,preserved_questions=None,preserved_answer_indices=None):
    positions=[i%4 for i in range(len(rows))];random.Random(2026111500+number).shuffle(positions)
    slug=re.sub('[^a-z0-9]+','-',subject.lower())
    preserved={q['id']:q for q in (preserved_questions or [])}
    fixed=dict(preserved_answer_indices or {})
    assert all(isinstance(i,int) and 0<=i<4 for i in fixed.values())
    assert all(k not in fixed or fixed[k]==q['correctIndex'] for k,q in preserved.items())
    fixed.update({k:q['correctIndex'] for k,q in preserved.items()})
    if fixed:
        ids=[f'{slug}-rebuild-{number:02}-{i:03}' for i in range(1,len(rows)+1)]
        assert set(fixed)<=set(ids),'Preserved questions must belong to this chapter'
        target=collections.Counter(i%4 for i in range(len(rows)))
        used=collections.Counter(fixed.values())
        assert all(used[i]<=target[i] for i in range(4)),'Cannot preserve keys with balanced final counts'
        remaining=[i for i in range(4) for _ in range(target[i]-used[i])]
        random.Random(2026111500+number).shuffle(remaining)
        positions=[fixed[k] if k in fixed else remaining.pop() for k in ids]
    qs=[]
    for i,(r,pos) in enumerate(zip(rows,positions),1):
        existing=preserved.get(f'{slug}-rebuild-{number:02}-{i:03}')
        if existing:
            assert existing['question']==r['question'],'Preserving a question with a changed stem'
            assert existing['options'][existing['correctIndex']]==r['answer'],'Preserving a question with a changed answer'
            assert set(existing['options'])=={r['answer'],*(o for o,_ in r['others'])},'Preserving a question with changed options'
            qs.append(copy.deepcopy(existing));continue
        options=[r['answer']]+[x[0] for x in r['others']];assert len(options)==4
        options[0],options[pos]=options[pos],options[0]
        reasons=dict(r['others']);other=[dict(optionIndex=j,explanation=reasons[o]) for j,o in enumerate(options) if j!=pos]
        sections=[];html=['<h2>'+escape(r['title'])+'</h2><p><strong>Correct answer: '+chr(65+pos)+' — '+escape(r['answer'])+'</strong></p>']
        plain=[r['title'],'Correct answer: '+r['answer']]
        for heading,bullets in r['sections']:
            html.append('<h3>'+escape(heading)+'</h3><ul>');bs=[];plain.append(heading)
            for text,children in bullets:
                html.append('<li>'+rich(text))
                if children:html.append('<ul>'+''.join('<li>'+rich(x)+'</li>' for x in children)+'</ul>')
                html.append('</li>');bs.append(dict(text=text,children=children));plain.extend([text,*children])
            html.append('</ul>');sections.append(dict(heading=heading,bullets=bs))
        tables=[]
        if r['table']:
            headers,values=r['table'];tables=[dict(headers=headers,rows=values)]
            html.append('<div class="table-wrap"><table><thead><tr>'+''.join('<th>'+rich(x)+'</th>' for x in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+rich(x)+'</td>' for x in line)+'</tr>' for line in values)+'</tbody></table></div>')
            plain.extend([' | '.join(headers),*[' | '.join(line) for line in values]])
        if not r['calculation']:
            html.append('<h3>Other Options</h3><ul>'+''.join('<li><strong>'+chr(65+a['optionIndex'])+' — '+escape(options[a['optionIndex']])+':</strong> '+rich(a['explanation'])+'</li>' for a in other)+'</ul>')
            plain.extend([options[a['optionIndex']]+': '+a['explanation'] for a in other])
        else:other=[]
        references=[dict(label=refs[k][0],url=refs[k][1]) for k in r['refs']]
        html.append('<h3>References</h3><ul>'+''.join('<li><a href="'+x['url']+'">'+escape(x['label'])+'</a></li>' for x in references)+'</ul>')
        plain.extend([x['label']+' — '+x['url'] for x in references])
        slug=re.sub('[^a-z0-9]+','-',subject.lower())
        qs.append(dict(id=f'{slug}-rebuild-{number:02}-{i:03}',topic=r['topic'],question=r['question'],options=options,correctIndex=pos,
          questionStyle=r['style'],calculation=r['calculation'],explanation='\n\n'.join(plain),explanationHtml=''.join(html),
          explanationTeaching=dict(title=r['title'],sections=sections,tables=tables,otherOptions=other),references=references,
          sourceCheckedAt='2026-11-15',reviewStatus='source_checked_not_independently_clinician_reviewed'))
        if r.get('coverageDecision'):qs[-1]['coverageDecision']=r['coverageDecision']
    first=json.loads((ROOT/'Neurology/01. Neuroanatomy, Clinical Localization & Neurological Examination.json').read_text(encoding='utf-8'))
    bank=dict(schemaVersion=1,folder=subject,subject=subject,chapterOrder=number,topicOrder=1,headingIndex=0,document=document,
      headingText=re.sub(r'^\d+[. ]+','',document),targetQuestions=len(qs),status='chapter_authored',
      authorship='Original educational MCQs; not authenticated NEET-SS past questions',sourceNote=source_note,
      explanationCss=first['explanationCss'],questions=qs)
    report=validate(bank);dest=ROOT/subject/(document+'.json');dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(bank,ensure_ascii=False,indent=2),encoding='utf-8')
    update_plan(subject,number,document,dest,report)
    print(json.dumps(dict(file=str(dest),**report),indent=2));return dest

def update_plan(subject,number,document,dest,report):
    path=ROOT/'progress.json'
    plan=json.loads(path.read_text(encoding='utf-8')) if path.exists() else dict(subjectOrder=SUBJECTS,delivery='JSON only; one chapter at a time',chapters=[])
    key=(subject,document)
    row=next((x for x in plan['chapters'] if (x['subject'],x['document'])==key),None)
    if row is None:row=dict(subject=subject,chapter=number,document=document);plan['chapters'].append(row)
    row.update(status='authored_validated',file=dest.relative_to(ROOT).as_posix(),validation=report)
    path.write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')

def install(source,data=DATA):
    sys.path.insert(0,str(REPO/'src'));from cnl_desktop import study_packs
    bank=json.loads(source.read_text(encoding='utf-8'));report=validate(bank)
    root=(data/'Qbank').resolve();study=data/'study-data'
    before={p:p.read_bytes() for p in study_packs._quiz_record_files(study)}
    dest=study_packs._quiz_record_path(study,bank)
    # Empty historical folders can have old chapter numbers; enforce the new sequence.
    chapter=dest.parent.parent
    label=re.sub(r'^\d+[. _-]+','',chapter.name)
    dest=chapter.with_name(f"{bank['chapterOrder']:02}. {label}")/dest.parent.name/dest.name
    assert dest.resolve().is_relative_to(root) and not any(p.is_symlink() or p.is_junction() for p in root.rglob('*'))
    identity=study_packs._quiz_row_id(bank)
    duplicates=[p for p,b in before.items() if study_packs._quiz_row_id(json.loads(b))==identity]
    assert len(duplicates)<=1,'Duplicate chapter identity'
    previous=duplicates[0] if duplicates else None
    if previous:
        backup=data/'qbank-reset-backups'/f'chapter-update-{time.time_ns()}.zip';backup.parent.mkdir(parents=True,exist_ok=True)
        with zipfile.ZipFile(backup,'x',zipfile.ZIP_DEFLATED) as z:z.writestr(previous.relative_to(root).as_posix(),before[previous])
        with zipfile.ZipFile(backup) as z:assert z.read(previous.relative_to(root).as_posix())==before[previous]
    dest.parent.mkdir(parents=True,exist_ok=True)
    try:
        assert all(p.read_bytes()==b for p,b in before.items()),'Concurrent change'
        study_packs._write_json(dest,bank)
        assert json.loads(dest.read_text(encoding='utf-8'))==bank
        if previous and previous!=dest:previous.unlink()
        assert all(p.read_bytes()==b for p,b in before.items() if p not in {dest,previous}),'Another chapter changed'
        old=study_packs.paths.resource_root
        try:
            study_packs.paths.resource_root=lambda:data.parent/'_internal/assets'
            loaded=study_packs.read_quizzes(study)
        finally:study_packs.paths.resource_root=old
        found=[x for x in loaded if study_packs._quiz_row_id(x)==identity]
        assert len(found)==1 and found[0]['questions']==bank['questions'] and found[0]['chapterOrder']==bank['chapterOrder']
    except BaseException:
        if dest in before:dest.write_bytes(before[dest])
        else:dest.unlink(missing_ok=True)
        if previous and previous!=dest:previous.write_bytes(before[previous])
        raise
    path=ROOT/'progress.json';plan=json.loads(path.read_text(encoding='utf-8'))
    row=next(x for x in plan['chapters'] if x['subject']==bank['folder'] and x['document']==bank['document'])
    row.update(status='installed_verified',installedSha256=hashlib.sha256(dest.read_bytes()).hexdigest())
    # Reconcile completed banks against runtime readback, including the initial chapter.
    for other in plan['chapters']:
        sourcefile=ROOT/other.get('file','__pending__')
        if sourcefile.is_file():
            sourcebank=json.loads(sourcefile.read_text(encoding='utf-8'))
            matches=[x for x in loaded if study_packs._quiz_row_id(x)==study_packs._quiz_row_id(sourcebank)]
            if len(matches)==1 and matches[0]['questions']==sourcebank['questions']:other['status']='installed_verified'
    pending=next((x for x in plan['chapters'] if x['status']=='pending'),None)
    plan['currentChapter']=(pending['subject']+' '+pending['document']) if pending else 'All planned chapters installed'
    path.write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(dict(installed=str(dest),preservedOtherBanks=len(before)-bool(previous),**report),indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source',type=Path);p.add_argument('--install',action='store_true');a=p.parse_args()
    if a.install:install(a.source)
    else:print(json.dumps(validate(json.loads(a.source.read_text(encoding='utf-8'))),indent=2))
