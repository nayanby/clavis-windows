"""Seal the consolidated author/source review and measured render evidence."""
import hashlib,json
from qbank_json_chapters import ROOT,DATA,REPO,validate
from redistribute_cardiology_qbank import digest
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def write(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
path=ROOT/'Cardiology/13. Aortic Diseases and Peripheral Vascular Diseases.json';bank=read(path);audit=path.parent/'audit'
assert len(bank['questions'])==48
assert all(q.get('explanationStyle')=='concise_structured' for q in bank['questions'])
before=hashlib.sha256(path.read_bytes()).hexdigest()
for label,folder in [('offline',''),('app','app')]:
 report=read(REPO/'outputs/qbank-render/cardiology-13'/folder/'render-report.json')
 assert report['status']=='passed' and report['bankSha256']==before
 assert all(r['questions']==48 and not r['failures'] for r in report['results'])
 write(audit/f'chapter-13-{label}-render-review.json',report)
source=read(audit/'chapter-13-source-review.json')
assert len(source['sourceSectionsRead'])==4
assert source['sourceDocumentSha256']==hashlib.sha256((DATA/'files/Cardiology'/bank['sourceDocument']).read_bytes()).hexdigest()
for q in bank['questions']:
 if q['id'].startswith('cardiology-rebuild-13-'):q['reviewStatus']='source_checked_not_independently_clinician_reviewed'
validation=validate(bank)
coverage=read(audit/'chapter-13-coverage.json');coverage.update(status='reviewed_ready_to_install',remainingDecisions=[],countPolicy='48 distinct decisions: 45 newly authored and 3 retained IDs, covering the four source sections with additional trial evidence; not official examination weightage.')
write(audit/'chapter-13-coverage.json',coverage)
findings=[
 'Anatomical classification uses ascending involvement, not entry-tear site. Dynamic/static branch obstruction and urgent complicated-type-B treatment are distinguished.',
 'Acute aortic syndrome target HR is explicitly 60–80/min under 2022 ACC/AHA; SBP target is qualified by organ perfusion. Beta-blockade precedes vasodilation; diltiazem alternative excludes systolic failure, shock and AV block.',
 'High-risk uncomplicated type B morphology supports selected TEVAR consideration, not a claim of established rupture or mandatory intervention.',
 'IMH location, family imaging despite negative panels, dissection surveillance, sex-specific AAA surveillance/repair, sporadic growth criteria and inherited-aortopathy thresholds reviewed.',
 'BAV and Marfan thresholds are kept distinct from sporadic disease and the transferred ESC 2025 concomitant-valve-surgery threshold. Root and tubular ascending operations are not treated as interchangeable.',
 'Infected/symptomatic aneurysms do not require reaching ordinary degenerative size thresholds; endoleak I/III direct pressurization is separated from collateral II and occult V.',
 'ABI calculation independently checked: 105/150=0.70. Exercise ABI, TBI and local perfusion assessment are selected by the clinical context, not ordered interchangeably.',
 'CLTI requires clinical tissue threat plus PAD; toe pressure <30 and WIfI grades are interpreted with wound and infection findings.',
 'PAD lipid threshold is explicitly the named 2024 ACC/AHA framework. Clopidogrel, dual-pathway inhibition, time-limited DAPT and full-dose AF anticoagulation are distinguished.',
 'Cilostazol interaction dose includes moderate CYP3A4 inhibitors; heart-failure contraindication and meal timing are retained. Walking prescription specifies active time and program duration.',
 'BEST-CLI cohort-1 composite result is not portrayed as isolated mortality benefit. BASIL-2 endpoint/population and mortality-driven direction are explicit; neither trial is a universal procedural mandate.',
 'ALI Rutherford categories use neurological/Doppler findings rather than duration alone. ESVS UFH bolus/infusion guidance replaces an unsupported universal infusion rate.',
 'IIb prioritizes rapid reperfusion; III avoids reperfusing nonviable tissue. Compartment syndrome can occur with audible arterial signals. Selected IIa catheter lysis requires bleeding review and reassessment.',
 'All three transferred explanations condensed with stable IDs and answer slots. Two option sets shortened to remove giveaway wording; audit hashes identify the changes.',
 'All 48 generated explanation documents passed offline and actual-app-renderer checks at two viewport widths; narrow app preview visually inspected.'
]
editor=dict(status='author_review_passed',questionCount=48,sourceSectionsRead=source['sourceSectionsRead'],questionIds=[q['id'] for q in bank['questions']],findings=findings,independentClinicianReview=False,validation=validation,remaining=['Install sealed chapter and verify runtime readback, then commit and push.'])
write(audit/'chapter-13-editorial-review.json',editor)
revisions=read(audit/'reviewed-question-revisions.json')
for r in revisions['revisions']:
 if r['questionId'] in {'cardiology-rebuild-02-008','cardiology-rebuild-03-017','cardiology-rebuild-09-042'}:
  r['reason']='Condensed explanations into concise teaching bullets; retained question ID, stem and correct answer position.'+(' Shortened distractor option wording without changing the clinical answer.' if 'options' in r['changedFields'] else '')
write(audit/'reviewed-question-revisions.json',revisions)
release=dict(chapterNumber=13,document=bank['document'],status='passed',installed=False,reviewedAt='2026-11-16',reviewedQuestionsSha256=digest(bank['questions']),sourceDocumentSha256=source['sourceDocumentSha256'],questionCount=48,coverageAudit='chapter-13-coverage.json',sourceReview='chapter-13-source-review.json',editorialReview='chapter-13-editorial-review.json',validation=validation,
 checks=dict(singleBestAnswerAuthorReview='passed',continuousTopicOrder='passed',individualDistractorExplanations='passed',sourceCoverageAndCurrentUpdates='passed_for_documented_scope',stableIdsAndAnswerSlots='passed',offlineRichTextAndRequiredStyles='passed_offline_and_app_renderer_at_two_widths'),
 limitations=['Full Harrison text was not accessed.','Verification is author source review, not independent clinician peer review.','Named guideline frameworks are explicit; treatment selection remains individualized.'])
write(audit/'chapter-13-release-review.json',release)
source.update(status='reviewed_ready_to_install',checks=dict(finalClinicalReview='author_review_passed',transferredExplanationCompaction='passed',rendering='passed_offline_and_app_two_widths'),nextWork='Install sealed chapter and verify runtime readback.',releaseReview=dict(status='passed',installed=False,report='chapter-13-release-review.json'),editorialReviewProgress=dict(status='passed',nextWork='Install and verify runtime readback.'))
source['corrections'].append('ESVS ALI heparin dosing specifies 5,000 IU or 70–100 IU/kg bolus followed by monitored titrated infusion; no universal infusion rate is asserted.')
write(audit/'chapter-13-source-review.json',source)
bank['status']='reviewed_ready_to_install';bank['sourceNote']='Original concise educational questions with author review of the source document and named primary guidelines/trials. Full Harrison text not accessed; no independent clinician peer review claimed.'
write(path,bank)
print(json.dumps(release,indent=2))
