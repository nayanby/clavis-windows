"""Seal Chapter 14 after source review and measured rendering checks."""
import hashlib,json
from qbank_json_chapters import ROOT,DATA,REPO,validate
from redistribute_cardiology_qbank import digest

def read(p):return json.loads(p.read_text(encoding='utf-8'))
def write(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

path=ROOT/'Cardiology/14. Advanced ECG Interpretation and Electrophysiology.json'
bank=read(path);audit=path.parent/'audit'
assert len(bank['questions'])==80 and all(q.get('explanationStyle')=='concise_structured' for q in bank['questions'])
before=hashlib.sha256(path.read_bytes()).hexdigest()
for label,folder in [('offline',''),('app','app')]:
 report=read(REPO/'outputs/qbank-render/cardiology-14'/folder/'render-report.json')
 assert report['status']=='passed' and report['bankSha256']==before
 assert all(r['questions']==80 and not r['failures'] for r in report['results'])
 write(audit/f'chapter-14-{label}-render-review.json',report)
progress=read(audit/'chapter-14-authoring-progress.json')
assert progress['sourceDocumentSha256']==hashlib.sha256((DATA/'files/Cardiology'/bank['sourceDocument']).read_bytes()).hexdigest()
sections=['Technical validity, intervals and rate/rhythm','Axis and conduction','Chamber/QRS morphology','Ischemia/infarction','Arrhythmia patterns','Electrolytes, drugs and channelopathies','Other diseases, pacing and mimics','Integrated reporting','Approach to tachyarrhythmia','Syncope evaluation and treatment']
findings=progress['sourceFindings']+[
 'All remaining source spans read in focused batches, including 185–349, 585–617, 618–938, 1109–1129 and 1226–1474; source review is complete for the chapter.',
 'Forty-five transferred explanations manually condensed into topic-specific nested bullets, retaining tables and individualized distractor reasons. IDs and correct answer slots are stable.',
 'Two numerical questions independently checked: 60/(24*0.020)=125/min and 400/(0.512**(1/3))=500 ms.',
 'Syncope timing, symptom-reproducing carotid sinus syndrome, POTS exclusions, infrequent-event monitoring and selected reflex pacing are separated from broad positive-test labels.',
 'Canadian POTS guideline DOI and publication details confirmed against PubMed 32145864; threshold distinguishes adults from ages 12–19.',
 'VT versus SVT mechanisms, adenosine response limitations, pre-excited AF, acquired versus congenital long QT, pacing capture/sensing and PMT circuits retained in concise teaching notes.',
 'All 80 explanations passed offline and actual app-renderer checks at two widths; narrow app screenshot visually inspected.'
]
for q in bank['questions']:
 if q['id'].startswith('cardiology-rebuild-14-'):q['reviewStatus']='source_checked_not_independently_clinician_reviewed'
validation=validate(bank)
progress.update(status='author_review_complete',sourceReadStatus='Completed with focused reads replacing truncated outputs.',sourceSectionsPending=[],reviewedSourceRanges=sections,sourceFindings=findings,validation=validation,nextWork='Install sealed chapter and verify runtime readback.')
write(audit/'chapter-14-authoring-progress.json',progress)
coverage=read(audit/'chapter-14-coverage.json');coverage.update(status='reviewed_ready_to_install',countPolicy='80 distinct decisions: 45 retained IDs and 35 additions for uncovered source topics; not official examination weightage.',remainingDecisions=[])
write(audit/'chapter-14-coverage.json',coverage)
write(audit/'chapter-14-editorial-review.json',dict(status='author_review_passed',questionCount=80,questionIds=[q['id'] for q in bank['questions']],sourceSectionsRead=sections,findings=findings,independentClinicianReview=False,validation=validation))
from cardiology_14_foundations import REFERENCES
from cardiology_14_pacing_syncope import REFERENCES as additional
refs=dict(REFERENCES);refs.update(additional)
write(audit/'chapter-14-source-review.json',dict(status='reviewed_ready_to_install',sourceDocumentSha256=progress['sourceDocumentSha256'],sourceSectionsRead=sections,corrections=progress['sourceFindings'],references=[dict(label=l,url=u) for l,u in refs.values()],checks=dict(finalClinicalReview='author_review_passed',transferredExplanationCompaction='passed',rendering='passed_offline_and_app_two_widths'),releaseReview=dict(status='passed',installed=False,report='chapter-14-release-review.json'),editorialReviewProgress=dict(status='passed',nextWork='Install and verify runtime readback.')))
release=dict(chapterNumber=14,document=bank['document'],status='passed',installed=False,reviewedAt='2026-11-16',reviewedQuestionsSha256=digest(bank['questions']),sourceDocumentSha256=progress['sourceDocumentSha256'],questionCount=80,coverageAudit='chapter-14-coverage.json',sourceReview='chapter-14-source-review.json',editorialReview='chapter-14-editorial-review.json',validation=validation,checks=dict(continuousTopicOrder='passed',individualDistractorExplanations='passed_except_two_calculations',stableIdsAndAnswerSlots='passed',rendering='passed_offline_and_app_two_widths'),limitations=['Full Harrison text was not accessed.','Author source review is not independent clinician peer review.'])
write(audit/'chapter-14-release-review.json',release)
bank.update(status='reviewed_ready_to_install',sourceNote='Concise original educational explanations with author source review against the source document and named primary guidance. Full Harrison text not accessed; no independent clinician peer review claimed.')
write(path,bank)
print(json.dumps(validation,indent=2))
