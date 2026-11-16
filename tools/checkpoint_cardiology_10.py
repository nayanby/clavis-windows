"""Record local editing progress without installing or publishing a draft."""
import json,statistics
from qbank_json_chapters import ROOT,validate
bank_path=ROOT/'Cardiology/10. Infective Endocarditis.json'
bank=json.loads(bank_path.read_text(encoding='utf-8'))
audit=bank_path.parent/'audit'
compact=[q for q in bank['questions'] if q.get('explanationStyle')=='concise_structured']
remaining=[q['id'] for q in bank['questions'] if q.get('explanationStyle')!='concise_structured']
report=dict(chapter=10,status='local_draft_in_progress',installed=False,
 authoredQuestions=len(bank['questions']),conciseExplanations=len(compact),
 remainingConciseExplanations=len(bank['questions'])-len(compact),
 conciseQuestionIds=[q['id'] for q in compact],validation=validate(bank),
 workflow='One consolidated chapter pass: source coverage, targeted verification, concise editing, then one validation/render/release cycle. Reuse documented source checks unless a changed claim or unresolved issue requires rechecking.',
 sourceReview='Existing source-review record retained; October 2026 correction remains unread. No completed medical release review claimed.',
 nextWork=('Continue concise editing from '+remaining[0]+'; ' if remaining else '')+'Resolve the specific treatment claims affected by the outstanding correction review and compare source-document coverage before release.',
 targetedChecks=[
  dict(url='https://www.cdc.gov/q-fever/hcp/clinical-guidance/index.html',finding='Adult endocarditis doxycycline 100 mg every 12 hours plus hydroxychloroquine 200 mg every 8 hours for at least 18 months rechecked.'),
  dict(url='https://www.idsociety.org/practice-guideline/vancomycin/',finding='AUC24 400–600 at MIC 1 mg/L, early exposure assessment and limitations of trough-only monitoring rechecked.'),
  dict(url='https://www.iscvid.org/wp-content/uploads/2026/09/2026-AHA-IE-Dx-Tx-Management-DeSimone-Circulation-Sept-8-2026.pdf',finding='September text confirms ceftriaxone monotherapy consensus for penicillin-intermediate VGS/S. gallolyticus, no gentamicin for staphylococcal PVE, unresolved rifampin consensus and postoperative duration wording. This does not verify the unread October correction.')],
 draftPolicy='Local only until reviewed installation.',
 answerPositionChange=dict(questionId='cardiology-rebuild-10-001',reason='Moved the same correct answer from A to B in an unpublished question to balance the 66-question set after transfer; medical answer unchanged.'))
(audit/'chapter-10-authoring-progress.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
revisions_path=audit/'reviewed-question-revisions.json'
if revisions_path.exists():
 revisions=json.loads(revisions_path.read_text(encoding='utf-8'))
 for r in revisions['revisions']:
  if r['questionId']=='cardiology-rebuild-10-001':
   r['reason']='Condensed teaching into structured bullets. Same medical answer moved from A to B in this unpublished question; options and distractor indices reordered to balance the transferred chapter.'
 revisions_path.write_text(json.dumps(revisions,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:report[k] for k in ('authoredQuestions','conciseExplanations','remainingConciseExplanations','validation')}))
