"""Local serialization and structural checks for directly authored original Qbanks."""
import ast
from collections import Counter
from html import escape
from html.parser import HTMLParser
import json
from pathlib import Path
import random
import re

ROOT = Path(__file__).resolve().parents[1] / 'build/topic-based-qbank-replacement'

def ref(label, url):
    return dict(label=label, url=url)

def rich(text):
    return re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', escape(text))

def question(stem, correct, distractors, title, principle, details, application, clinical, comparison, refs, style='direct'):
    return dict(question=stem, options=[correct]+[x[0] for x in distractors], correctIndex=0,
        questionStyle=style, explanationTeaching=dict(title=title, sections=[
            dict(heading='Diagnostic or treatment principle',bullets=[dict(text=principle,children=details)]),
            dict(heading='Applying the principle',bullets=[dict(text=application,children=clinical)])],
            tables=[dict(title='Key distinctions',headers=['Finding or strategy','Interpretation'],rows=comparison)],
            otherOptions=[dict(optionIndex=i+1,explanation=x[1]) for i,x in enumerate(distractors)]),references=refs)

def render(q):
    d=q['explanationTeaching']; parts=['<h2>'+rich(d['title'])+'</h2>']; plain=[d['title']]
    for sec in d['sections']:
        parts.append('<h3>'+rich(sec['heading'])+'</h3><ul>'); plain.append(sec['heading'])
        for b in sec['bullets']:
            parts.append('<li>'+rich(b['text'])+'<ul>'+''.join('<li>'+rich(t)+'</li>' for t in b['children'])+'</ul></li>')
            plain.extend([b['text'],*b['children']])
        parts.append('</ul>')
    for t in d['tables']:
        parts.append('<h3>'+rich(t['title'])+'</h3><table><thead><tr>'+''.join('<th>'+rich(h)+'</th>' for h in t['headers'])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+rich(x)+'</td>' for x in row)+'</tr>' for row in t['rows'])+'</tbody></table>')
        plain.extend([t['title'],*[' | '.join(row) for row in t['rows']]])
    parts.append('<h3>Other Options</h3><ul>')
    for a in d['otherOptions']:
        option=q['options'][a['optionIndex']]
        parts.append('<li><strong>'+rich(option)+':</strong> '+rich(a['explanation'])+'</li>')
        plain.append(option+': '+a['explanation'])
    parts.append('</ul>')
    q['explanationHtml']=''.join(parts)
    # HTML reference lists are appended by the app; plain exports carry them at the end too.
    plain+=['References']+[f"{i}. {r['label']} — {r['url']}" for i,r in enumerate(q['references'],1)]
    q['explanation']='\n\n'.join(plain)

class BalancedHTML(HTMLParser):
    def __init__(self): super().__init__(); self.stack=[]
    def handle_starttag(self,tag,attrs):
        assert tag in {'h2','h3','ul','li','strong','table','thead','tbody','tr','th','td'}, tag
        assert not attrs, (tag,attrs)
        self.stack.append(tag)
    def handle_endtag(self,tag): assert self.stack.pop()==tag, tag

def validate(bank):
    rows=bank['questions']; target=bank['targetQuestions']; stems=set(); ids=set()
    assert len(rows)==target, (len(rows),target)
    counts=Counter(q['correctIndex'] for q in rows)
    assert all(target//4<=counts[i]<=(target+3)//4 for i in range(4)),counts
    for q in rows:
        assert q['question'].strip() and q['question'] not in stems
        stems.add(q['question']); assert q['id'] not in ids; ids.add(q['id'])
        assert len(q['options'])==len(set(q['options']))==4
        d=q['explanationTeaching']
        assert len(d['otherOptions'])==3
        assert {a['optionIndex'] for a in d['otherOptions']}==set(range(4))-{q['correctIndex']}
        assert all(a['explanation'].strip() for a in d['otherOptions'])
        assert len(d['sections'])>=2 and all(s['bullets'] for s in d['sections'])
        assert all(b['children'] for s in d['sections'] for b in s['bullets'])
        assert d['tables'] and all(t['rows'] and all(len(r)==len(t['headers']) for r in t['rows']) for t in d['tables'])
        assert q['references'] and all(r['url'].startswith('https://') and r['label'] for r in q['references'])
        assert '<strong>' in q['explanationHtml'] and '<table>' in q['explanationHtml']
        p=BalancedHTML(); p.feed(q['explanationHtml']); assert not p.stack
        assert q['questionStyle'] in {'direct','clinical_scenario'}
    return dict(questions=len(rows), answerDistribution={chr(65+i):sum(q['correctIndex']==i for q in rows) for i in range(4)},
        questionStyles=dict(Counter(q['questionStyle'] for q in rows)),
        explanationsWithNestedBullets=len(rows),explanationsWithTables=len(rows),distractorRationales=len(rows)*3,
        referencesAtEnd=True,uniqueStems=len(stems),structuralValidation='passed',
        clinicalReview='Source-checked original educational content; no independent clinician review recorded')

def finalize(subject, order, topic, slug, rows, target):
    assert len(rows)==target
    answers=[q['options'][q['correctIndex']] for q in rows]
    targets=list(range(4))*(target//4); random.Random(614000+order).shuffle(targets)
    for i,(q,pos) in enumerate(zip(rows,targets),1):
        old=q['correctIndex']
        if old!=pos:
            q['options'][old],q['options'][pos]=q['options'][pos],q['options'][old]
            for a in q['explanationTeaching']['otherOptions']:
                if a['optionIndex']==pos:a['optionIndex']=old
                elif a['optionIndex']==old:a['optionIndex']=pos
        q['correctIndex']=pos
        q['explanationTeaching']['otherOptions'].sort(key=lambda a:a['optionIndex'])
        assert q['options'][pos]==answers[i-1]
        q.update(id=f'{slug}-{i:03}',authorship='Original ChatGPT-authored topic-based question; not an authenticated examination PYQ',
            reviewStatus='authored_source_checked',sourceCheckedAt='2026-11-05')
        render(q)
    bank=dict(folder=subject,document=topic,headingText=topic,chapterOrder=order,topicOrder=1,targetQuestions=target,status='chapter_authored',questions=rows)
    report=validate(bank)
    chapter=f'{order:02}. {topic}'
    dest=ROOT/'completed'/subject/chapter/('01. '+topic)/'questions.json'
    dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(json.dumps(bank,ensure_ascii=False,indent=2),encoding='utf-8')
    dest.with_name('validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    preview=['<!doctype html><html><head><meta charset="utf-8"><title>'+escape(topic)+'</title><style>body{max-width:980px;margin:32px auto;padding:0 20px;color:#232350;background:#f7f7fb;font:17px/1.37 Georgia,serif}article{background:white;padding:24px;margin:24px 0;border:1px solid #ddd;border-radius:12px}.stem{font:700 20px/26px Aptos,Arial,sans-serif}.options{font:16px/22px Aptos,Arial,sans-serif}h2{font-size:19px;line-height:1.2;background:#f9dfe9;padding:8px}h3{font-size:17px;line-height:1.2;color:#214c90}p{margin:0 0 8px}table{border-collapse:collapse;width:100%;font-size:16px}th,td{border:1px solid #ccc;padding:8px;text-align:left}li{margin:4px 0}nav{position:sticky;top:0;background:#f7f7fb;padding:8px}</style></head><body><h1>'+escape(topic)+'</h1><p>Original educational questions. '+str(target)+' questions. Answers and explanations follow each question.</p>']
    for i,q in enumerate(rows,1):
        preview+=['<article id="q'+str(i)+'"><p class="stem">'+str(i)+'. '+escape(q['question'])+'</p><ol type="A" class="options">'+''.join('<li>'+escape(o)+'</li>' for o in q['options'])+'</ol><p><strong>Correct answer: '+chr(65+q['correctIndex'])+'</strong></p>'+q['explanationHtml']+'<h3>References</h3><ol>'+''.join('<li><a href="'+escape(r['url'],quote=True)+'">'+escape(r['label'])+'</a></li>' for r in q['references'])+'</ol></article>']
    preview+=['</body></html>']; dest.with_name('review.html').write_text(''.join(preview),encoding='utf-8')
    planpath=ROOT/'topic-map.json';plan=json.loads(planpath.read_text(encoding='utf-8'))
    for s in plan['subjects']:
        for c in s['chapters']:
            if s['subject']==subject and c['chapterOrder']==order:
                c.update(status='chapter_authored',draftQuestionCount=target,completedQuestionCount=target,completedFile=str(dest.relative_to(ROOT)))
    plan['progress']=dict(plan.get('progress',{}),completedChapters=sum(c.get('status')=='chapter_authored' for s in plan['subjects'] for c in s['chapters']),
        completedQuestions=sum(c.get('completedQuestionCount',0) for s in plan['subjects'] for c in s['chapters']),
        plannedQuestions=sum(s['targetQuestions'] for s in plan['subjects']))
    plan['progress'].setdefault('activeNewProjectBanksReplaced',0)
    planpath.write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(dict(subject=subject,chapter=topic,file=str(dest),**report),indent=2))
    return bank

if __name__=='__main__':
    for path in sorted((ROOT/'completed').rglob('questions.json')):
        bank=json.loads(path.read_text(encoding='utf-8'))
        for q in bank['questions']:render(q)
        report=validate(bank)
        path.write_text(json.dumps(bank,ensure_ascii=False,indent=2),encoding='utf-8')
        path.with_name('validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
        print(path,report['structuralValidation'])
