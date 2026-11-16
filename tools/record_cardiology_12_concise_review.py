"""Record consolidated explanation review without releasing draft content."""
import hashlib,json,subprocess
from pathlib import Path
from qbank_json_chapters import validate
ROOT=Path(__file__).resolve().parents[1]
BANK=ROOT/'Qbank Rebuild/Cardiology/12. Adult Congenital Heart Diseases.json'
bank=json.loads(BANK.read_text(encoding='utf-8'))
prior=json.loads(subprocess.check_output(['git','show','HEAD:Qbank Rebuild/Cardiology/12. Adult Congenital Heart Diseases.json'],cwd=ROOT).decode('utf-8'))
def words(b):
 return sum(len(x['text'].split())+sum(len(c.split()) for c in x['children']) for q in b['questions'] for s in q['explanationTeaching']['sections'] for x in s['bullets'])
assert len(bank['questions'])==55
assert all(q.get('explanationStyle')=='concise_structured' for q in bank['questions'])
for q in bank['questions']:
 old=next(x for x in prior['questions'] if x['id']==q['id'])
 for key in ['question','options','correctIndex','references']:assert q[key]==old[key],(q['id'],key)
audit=BANK.parent/'audit'
p=audit/'chapter-12-editorial-review.json';d=json.loads(p.read_text(encoding='utf-8'))
d['bankSha256']=hashlib.sha256(BANK.read_bytes()).hexdigest()
d['conciseRewrite']=dict(status='complete',completedQuestionIds=[q['id'] for q in bank['questions']],totalChapterQuestions=55,teachingBulletWordsBeforeThisBatch=words(prior),teachingBulletWordsAfter=words(bank),preserved='All stems, options, answer positions and references retained.',validation=validate(bank),next='App display integration and final release review before installation.')
d['remaining']=['Verify app rendering of concise bullets, ordered lists, tables and decision flows.','Seal release review, install with runtime readback, then commit and push.']
render=json.loads((ROOT/'outputs/qbank-render/cardiology-12/render-report.json').read_text(encoding='utf-8'))
assert render['bankSha256']==d['bankSha256']
(audit/'chapter-12-render-review.json').write_text(json.dumps(render,indent=2),encoding='utf-8')
d['renderReview']=dict(status='offline_html_css_passed',report='chapter-12-render-review.json',limitation='App theme integration remains to be verified.')
p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(d['conciseRewrite']))
