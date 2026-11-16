"""Seal the source-matched 70-question chapter after final content/layout review."""
import hashlib,json,statistics
from qbank_json_chapters import ROOT,DATA,REPO,validate
from redistribute_cardiology_qbank import digest
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def write(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
p=ROOT/'Cardiology/10. Infective Endocarditis.json';b=read(p);a=p.parent/'audit'
assert b['status']!='installed_verified' and len(b['questions'])==70
assert all(q.get('explanationStyle')=='concise_structured' for q in b['questions'])
for name,folder in [('offline',''),('app','app')]:
 r=read(REPO/'outputs/qbank-render/cardiology-10'/folder/'render-report.json')
 assert r['bankSha256']==hashlib.sha256(p.read_bytes()).hexdigest() and r['status']=='passed'
 assert all(x['questions']==70 and not x['failures'] for x in r['results'])
 write(a/f'chapter-10-{name}-render-review.json',r)
c=read(a/'chapter-10-coverage.json')
assert c['sourceParagraphsRead']==214 and not c['remainingDecisions']
assert c['sourceDocumentSha256']==hashlib.sha256((DATA/'files/Cardiology'/b['sourceDocument']).read_bytes()).hexdigest()
findings=[
 'All 214 source-document paragraphs reviewed; existing 66 decisions retained and four source-gap decisions added.',
 'All 70 explanations use concise topic-specific multilevel bullets; individual distractor reasons and useful comparison tables retained. Pathogenesis uses an ordered offline decision pathway.',
 'Question order follows diagnosis, organism treatment, transition/duration, surgery/complications, devices, prognosis and prevention. Transferred pocket-management decision moved beside pocket diagnosis.',
 'New decisions cover adhesion on previously normal valves, peripheral signs, Aspergillus endocarditis and multidomain prognosis. Primary guideline/study checks documented in references.',
 'Unretrieved October AHA correction is not represented as read. Version-dependent ceftriaxone question replaced by a drug-specific MIC decision explicitly grounded in SPILF–AEPEI 2025.',
 'Detailed 14-day postoperative minimum removed from the assessed material; postoperative question now tests residual DNA versus viable infection and individualized course completion, supported by accessible AHA summary and ESC principles.',
 'Gentamicin PVE decision retains the accessible AHA public recommendation; unverified assertion about rifampin consensus removed. ESC rifampin timing remains explicitly framework-specific.',
 'Enterococcal colorectal discussion now identifies observational evidence and its limits, rather than relying on the correction-linked statement.',
 'POET and DOTS retain population, phase and endpoint limits; EASE composite is distinguished from isolated mortality.',
 'Neurological surgical timing distinguishes selected nonhemorrhagic stroke from conditional delay after hemorrhage; emergency cardiac deterioration can alter timing.',
 'Final A18/B18/C17/D17 positions, 210 individual distractor rationales, all original IDs preserved. One unpublished answer position was reordered without changing its medical answer.',
 'Offline and app layout checks passed at desktop/narrow widths for every question; narrow app screenshot inspected.'
]
limitations=['Full Harrison text was not accessed.','Author source review is not independent clinician peer review.','October 2026 AHA correction text was inaccessible. Affected detailed claims were reframed against accessible primary guidance; the correction itself is not certified as reviewed.']
v=validate(b);lengths=[len(q['explanation'].split()) for q in b['questions']]
write(a/'chapter-10-editorial-review.json',dict(status='author_review_passed',questionCount=70,questionIds=[q['id'] for q in b['questions']],findings=findings,validation=v,independentClinicianReview=False,explanationWordCounts=dict(minimum=min(lengths),median=statistics.median(lengths),maximum=max(lengths))))
write(a/'chapter-10-source-review.json',dict(status='reviewed_ready_to_install',sourceDocumentSha256=c['sourceDocumentSha256'],sourceParagraphsRead=214,priorDetailedReview='source-reviews/10-source-review.json',findings=findings,limitations=limitations,references=list({r['url']:r for q in b['questions'] for r in q['references']}.values()),releaseReview=dict(status='passed',installed=False),editorialReviewProgress=dict(status='passed',nextWork='Install, read back, commit and push scoped chapter changes.')))
write(a/'chapter-10-release-review.json',dict(chapterNumber=10,document=b['document'],status='passed',installed=False,reviewedAt='2026-11-16',reviewedQuestionsSha256=digest(b['questions']),sourceDocumentSha256=c['sourceDocumentSha256'],questionCount=70,validation=v,limitations=limitations))
c.update(status='reviewed_ready_to_install',remainingReleaseWork=['Install, verify runtime readback, commit and push.']);write(a/'chapter-10-coverage.json',c)
progress=read(a/'chapter-10-authoring-progress.json');progress.update(status='author_review_complete',nextWork='Install, verify runtime readback, commit and push.',sourceReview='Author review complete with explicit inaccessible-correction limitation and independently sourced replacement decisions.',findings=findings);write(a/'chapter-10-authoring-progress.json',progress)
b['status']='reviewed_ready_to_install';b['sourceNote']='Original concise educational questions with author source review against the source document and cited primary guidance. Full Harrison text and independent clinician peer review are not claimed. See chapter-10-source-review.json for source/version limitations.';write(p,b)
print(json.dumps(v))
