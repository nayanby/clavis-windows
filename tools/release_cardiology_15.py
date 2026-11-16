"""Seal the completed Chapter 15 author review and measured layout evidence."""
import hashlib,json,statistics
from qbank_json_chapters import ROOT,DATA,REPO,validate
from redistribute_cardiology_qbank import digest
from rebuild_cardiology_15_json import DOC,GROUPS
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def write(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
path=ROOT/'Cardiology'/(DOC+'.json');bank=read(path);audit=path.parent/'audit'
assert len(bank['questions'])==128
assert all(q.get('explanationStyle')=='concise_structured' for q in bank['questions'])
before=hashlib.sha256(path.read_bytes()).hexdigest()
for label,folder in [('offline',''),('app','app')]:
 report=read(REPO/'outputs/qbank-render/cardiology-15'/folder/'render-report.json')
 assert report['status']=='passed' and report['bankSha256']==before
 assert all(r['questions']==128 and not r['failures'] for r in report['results'])
 write(audit/f'chapter-15-{label}-render-review.json',report)
progress=read(audit/'chapter-15-authoring-progress.json')
assert progress['sourceDocumentSha256']==hashlib.sha256((DATA/'files/Cardiology'/bank['sourceDocument']).read_bytes()).hexdigest()
sections=['Antiplatelets, anticoagulants and fibrinolytics','Antiarrhythmic and antianginal drugs','Lipid drugs','Inotropes, chronotropes, vasopressors and vasodilators']
findings=[
 'All 1232 source paragraphs read in contiguous batches; 93 transferred decisions retained and 35 source-gap decisions added.',
 'All 93 retained explanations manually condensed to topic-specific nested bullets. Tables, references and three individualized distractor rationales retained; original IDs, stems, options and answer slots unchanged.',
 'Final answer positions A32/B32/C32/D32; continuous subject groups separate antiplatelet, anticoagulant, fibrinolytic, rhythm, angina, HF, disease-specific, lipid, vasoactive and structural-trial decisions.',
 'Cangrelor transition differentiates clopidogrel/prasugrel from ticagrelor timing. CYP2C19 result interpretation does not imply mandatory universal genotyping.',
 'Age and renal enoxaparin adjustments are combined. Tirofiban renal adjustment changes infusion while preserving the loading dose.',
 'Acute VTE apixaban dosing is kept separate from AF dose reduction and extended secondary prevention. Fondaparinux prophylactic/ACS doses are distinguished from weight-tier VTE treatment.',
 'HIT treatment starts from clinical probability, preserves nonheparin anticoagulation, and defers VKA until platelet recovery. Acute VTE VKA overlap is not the same question as perioperative bridging.',
 'Reversal differentiates VKA factor replacement plus vitamin K, specific dabigatran binding, partial LMWH neutralization and nonspecific Xa-inhibitor hemostatic support. FDA December 2025 Andexxa US availability/safety change verified.',
 'Normal PT/INR/aPTT do not exclude apixaban. Calibrated anti-Xa testing is interpreted with timing and urgency, not as a universal procedural safety threshold.',
 'Mechanical-valve targets are explicitly anchored to ACC/AHA 2020; reduced INR in On-X aortic valves is not evidence for apixaban substitution. Rheumatic MS and triple-positive APS remain distinct high-risk contexts.',
 'Dronedarone permanent-AF restriction, dofetilide interactions, sotalol renal/QT risk, nitrate tolerance and nicorandil/trimetazidine adverse effects retained.',
 '2026 finerenone HF label and September 2026 mavacamten interruption threshold rechecked in FDA sources; indication-specific dose and monitoring frameworks preserved.',
 'Trial notes distinguish populations, randomized comparators and composite versus individual endpoints, including DIGIT-HF, preserved-EF post-MI beta-blocker meta-analysis, ADVENT, VANISH2, ALONE-AF and OCEAN.',
 'Lipid questions distinguish siRNA from antibodies, clinical-outcome evidence from LDL lowering, formulation-specific EPA evidence, renal fenofibrate dosing, bempedoic interactions and ANGPTL3 inhibition.',
 '2026 SSC vasoactive questions specify predominant vasodilation versus low-output cardiac dysfunction. Pressure response is not equated with restored flow or survival benefit.',
 'Milrinone accumulation, angiotensin-II thrombosis precautions, nitroprusside thiocyanate toxicity, epinephrine aerobic lactate and clevidipine formulation restrictions cover major monitoring decisions.',
 'Offline and actual-app rendering passed at desktop and narrow widths; narrow app screenshot visually inspected.'
]
for q in bank['questions']:
 if q['id'].startswith('cardiology-rebuild-15-'):q['reviewStatus']='source_checked_not_independently_clinician_reviewed'
validation=validate(bank)
progress.update(status='author_review_complete',newDraftQuestions=35,integratedCanonicalQuestions=128,transferredConciseCompleted=93,transferredConciseRemaining=0,remainingCoverage=[],sourceFindings=findings,validation=validation,nextWork='Install sealed chapter and verify runtime readback.')
write(audit/'chapter-15-authoring-progress.json',progress)
coverage=read(audit/'chapter-15-coverage.json');coverage.update(status='reviewed_ready_to_install',authoredQuestions=128,newDraftQuestions=35,remainingCoverage=[],remainingDecisions=[],countPolicy='128 high-yield decisions: 93 retained plus 35 source-gap additions; count follows source breadth and avoids duplicating other chapter decisions, not official examination weightage.')
write(audit/'chapter-15-coverage.json',coverage)
lengths=[len(q['explanation'].split()) for q in bank['questions']]
write(audit/'chapter-15-editorial-review.json',dict(status='author_review_passed',questionCount=128,questionIds=[q['id'] for q in bank['questions']],findings=findings,sourceSectionsRead=sections,independentClinicianReview=False,validation=validation,explanationWordCounts=dict(minimum=min(lengths),median=statistics.median(lengths),maximum=max(lengths))))
refs={r['url']:r for q in bank['questions'] for r in q['references']}
write(audit/'chapter-15-source-review.json',dict(status='reviewed_ready_to_install',sourceDocumentSha256=progress['sourceDocumentSha256'],sourceSectionsRead=sections,corrections=findings,references=list(refs.values()),checks=dict(finalClinicalReview='author_review_passed',transferredExplanationCompaction='passed',rendering='passed_offline_and_app_two_widths'),releaseReview=dict(status='passed',installed=False,report='chapter-15-release-review.json'),editorialReviewProgress=dict(status='passed',nextWork='Install and verify runtime readback.')))
release=dict(chapterNumber=15,document=bank['document'],status='passed',installed=False,reviewedAt='2026-11-16',reviewedQuestionsSha256=digest(bank['questions']),sourceDocumentSha256=progress['sourceDocumentSha256'],questionCount=128,coverageAudit='chapter-15-coverage.json',sourceReview='chapter-15-source-review.json',editorialReview='chapter-15-editorial-review.json',validation=validation,checks=dict(continuousTopicOrder='passed',individualDistractorExplanations='passed',stableIdsAndAnswerSlots='passed',rendering='passed_offline_and_app_two_widths'),limitations=['Full Harrison text was not accessed.','Author source review is not independent clinician peer review.','Named regulatory and guideline frameworks can differ by jurisdiction.'])
write(audit/'chapter-15-release-review.json',release)
snapshot=read(audit/'chapter-15-new-question-draft.json');snapshot.update(status='superseded_authoring_snapshot',supersededBy=path.name);write(audit/'chapter-15-new-question-draft.json',snapshot)
bank.update(status='reviewed_ready_to_install',sourceNote='Concise original educational explanations with author source review of the source document and named primary guidance/trials. Full Harrison text not accessed; no independent clinician peer review claimed.')
write(path,bank)
print(json.dumps(validation,indent=2))
