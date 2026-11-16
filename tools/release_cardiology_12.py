"""Seal the completed author review and rendering evidence for Chapter 12."""
import hashlib,json
from qbank_json_chapters import ROOT,DATA,REPO,validate
from redistribute_cardiology_qbank import digest

def read(p):return json.loads(p.read_text(encoding='utf-8'))
def write(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
path=ROOT/'Cardiology/12. Adult Congenital Heart Diseases.json';bank=read(path);audit=path.parent/'audit'
editor=read(audit/'chapter-12-editorial-review.json')
assert editor['conciseRewrite']['status']=='complete'
assert len(editor['sourceCoverageReview']['sectionsReadInFull'])==14
assert len(bank['questions'])==55 and all(q.get('explanationStyle')=='concise_structured' for q in bank['questions'])
render=read(REPO/'outputs/qbank-render/cardiology-12/app/render-report.json')
assert render['status']=='passed' and render['bankSha256']==hashlib.sha256(path.read_bytes()).hexdigest()
assert all(r['questions']==55 and not r['failures'] for r in render['results'])
write(audit/'chapter-12-app-render-review.json',render)
report=validate(bank)
release=dict(chapterNumber=12,document=bank['document'],status='passed',installed=False,reviewedAt='2026-11-16',
 reviewedQuestionsSha256=digest(bank['questions']),sourceDocumentSha256=hashlib.sha256((DATA/'files/Cardiology'/bank['sourceDocument']).read_bytes()).hexdigest(),
 questionCount=55,coverageAudit='chapter-12-coverage.json',sourceReview='chapter-12-source-review.json',editorialReview='chapter-12-editorial-review.json',validation=report,
 checks=dict(singleBestAnswerAuthorReview='passed',continuousTopicOrder='passed',individualDistractorExplanations='passed',sourceCoverageAndCurrentUpdates='passed_for_documented_scope',stableIdsAndAnswerSlots='passed',offlineRichTextAndRequiredStyles='passed_offline_and_app_renderer_at_two_widths'),
 limitations=['Full Harrison text was not accessed.','Author source verification is not independent clinician peer review.','Publisher-access limitations and the primary references used are documented in the source review.'])
write(audit/'chapter-12-release-review.json',release)
bank['status']='reviewed_ready_to_install'
bank['sourceNote']='Original educational synthesis with retained question identities; author source review completed against documented primary guidance. Full Harrison text not accessed; independent clinician review not claimed.'
write(path,bank)
editor.update(status='author_review_passed',bankSha256=hashlib.sha256(path.read_bytes()).hexdigest(),remaining=['Install sealed chapter and verify runtime readback; commit and push installed changes.'])
editor['reviewedScope']+=' Consolidated concise rewrite complete for all 55 explanations; offline and application-renderer checks passed at wide and narrow widths; narrow preview visually inspected.'
editor['sourceCoverageReview']['status']='all_14_source_sections_reviewed'
editor['renderReview']=dict(status='passed_offline_and_app_renderer',report='chapter-12-app-render-review.json',visualReview='Narrow preview inspected; title, nested bullets and table remain readable.')
write(audit/'chapter-12-editorial-review.json',editor)
p=audit/'chapter-12-source-review.json';source=read(p)
source.update(status='reviewed_ready_to_install',nextWork='Install sealed chapter and verify runtime readback.',releaseReview=dict(status='passed',installed=False,report='chapter-12-release-review.json'),editorialReviewProgress=dict(status='passed',nextWork='Install and verify runtime readback.'))
source['limitations']=['Four transferred IDs retained with hash-audited explanation revisions.','Author source review is not independent clinician peer review.','55 distinct decisions cover the documented source scope; not official examination weightage.']
write(p,source)
p=audit/'chapter-12-coverage.json';coverage=read(p);coverage['status']='reviewed_ready_to_install';coverage['countPolicy']='55 distinct high-yield decisions mapped to all 14 source sections and reviewed for overlap; not official examination weightage.';write(p,coverage)
print(json.dumps(release,indent=2))
