"""Record source coverage after reading all 214 extracted source paragraphs."""
import hashlib,json
from qbank_json_chapters import ROOT,DATA
bank_path=ROOT/'Cardiology/10. Infective Endocarditis.json'
b=json.loads(bank_path.read_text(encoding='utf-8'))
source=DATA/'files/Cardiology'/b['sourceDocument']
groups=[
 ('Overview, predisposition and pathogenesis',[2,45],['001','007','008','017','018','020','021','022','033','034','036','056','062']),
 ('Clinical manifestations',[46,59],['001','006','044','045','047','049','050','051','052','053','056']),
 ('Diagnostic sampling and imaging',[60,77],['002','003','004','012','013','014','015','016']),
 ('Duke–ISCVID criteria',[78,106],['005','006','007','008','009','010','011']),
 ('Culture-negative infection',[107,111],['017','018','019','020','021','022','023']),
 ('Medical management',[112,144],list(map(lambda n:f'{n:03}',range(24,44)))),
 ('Surgery and neurological complications',[145,161],['044','045','046','047','048','049','050','051','055']),
 ('Complications and prognosis',[162,171],['014','016','044','045','046','049','050','051','052','053','056']),
 ('Prevention and follow-up',[172,194],['062','063','064','065']),
 ('Clinical distinctions',[195,214],['004','045','046','047','055','062','065'])]
gaps=[
 dict(topic='Vegetation pathogenesis and previously normal valves',sourceParagraphs=[11,17],decision='Distinguish endothelial-injury/platelet–fibrin adhesion sequence from S. aureus capacity to infect previously normal valves.'),
 dict(topic='Peripheral clinical signs',sourceParagraphs=[51,56],decision='Differentiate Janeway vascular lesions, Osler immune manifestations, Roth spots and nonspecific splinter hemorrhages.'),
 dict(topic='Aspergillus endocarditis',sourceParagraphs=[43,44],decision='Recognize culture-negative fungal prosthetic infection with embolic disease; tissue diagnosis and antifungal plus surgical strategy.'),
 dict(topic='Prognostic assessment',sourceParagraphs=[169,171],decision='Integrate HF, invasive infection, persistent bacteremia and renal/neurological injury rather than equating culture clearance with low risk.')]
report=dict(chapter=10,status='source_coverage_review_in_progress',sourceDocument=b['sourceDocument'],sourceDocumentSha256=hashlib.sha256(source.read_bytes()).hexdigest(),sourceParagraphsRead=214,
 authoredQuestions=len(b['questions']),conciseExplanations=sum(q.get('explanationStyle')=='concise_structured' for q in b['questions']),
 coverage=[dict(section=s,sourceParagraphRange=p,questionIds=['cardiology-rebuild-10-'+i for i in ids]) for s,p,ids in groups],remainingDecisions=gaps,
 sourceCorrections=['Duke fever criterion is >38°C; do not copy the source ≥38°C wording.','Body-lice/housing exposure points to B. quintana; distinguish cat/flea-associated B. henselae.','Microbial rankings vary by cohort and acquisition; avoid universal frequency claims.','Keep AHA and ESC nondental prophylaxis and postoperative-duration approaches explicitly named.'],
 remainingReleaseWork=['Author and source-check the four uncovered decisions without duplicating existing questions.','Resolve or explicitly rewrite uncertain treatment claims after the inaccessible October 2026 AHA correction.','Review final answer balance and distractors, render once in offline and app contexts, then seal/install/read back/commit/push.'])
newids=['cardiology-rebuild-10-'+str(n).zfill(3) for n in range(66,70)]
if set(newids)<={q['id'] for q in b['questions']}:
 report['status']='source_coverage_mapped_pending_release'
 report['resolvedGaps']=[dict(**gap,questionId=qid) for gap,qid in zip(gaps,newids)]
 report['remainingDecisions']=[]
 report['remainingReleaseWork']=report['remainingReleaseWork'][1:]
(bank_path.parent/'audit/chapter-10-coverage.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'sourceParagraphsRead':214,'mappedQuestions':len(b['questions']),'remainingDecisions':len(report['remainingDecisions'])}))
