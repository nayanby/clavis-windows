"""Render every staged cardiology explanation in real Chromium without jsdom."""
import argparse,json,re,subprocess,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
TEST=r'''
const output=document.getElementById('result'),host=document.getElementById('host');
const check=(ok,label)=>{if(!ok)throw Error(label)};
try{
 const answers=[0,0,0,0],stems=new Set(),ids=new Set();let count=0;
 for(const bank of BANKS){
  check(bank.questions.length===bank.targetQuestions,'chapter quota');
  for(const q of bank.questions){
   check(!stems.has(q.question),'duplicate stem');stems.add(q.question);
   check(!ids.has(q.id),'duplicate ID');ids.add(q.id);
   window.cnlRenderQbankExplanation(host,q,true);
   check(host.querySelector('.cnl-qbank-answer').textContent.includes(q.options[q.correctIndex]),q.id+' answer');
   const rich=host.querySelector('.cnl-notes-explanation');
   check(rich.querySelector('li > ul'),q.id+' nesting');
   check(rich.querySelector('table th')&&rich.querySelector('table td'),q.id+' table');
   check(rich.querySelector('h2')&&rich.querySelector('h3')&&rich.querySelector('strong'),q.id+' formatting');
   check(!host.querySelector('script,iframe,img,[onclick]'),q.id+' inert');
   const refs=host.lastElementChild;
   check(refs.classList.contains('cnl-qbank-references'),q.id+' references last');
   check(refs.querySelectorAll('ol > li > a').length===new Set(q.references.map(r=>new URL(r.url).href)).size,q.id+' reference count');
   const heading=[...rich.querySelectorAll('h3')].find(x=>x.textContent==='Other Options');
   check(heading?.nextElementSibling.children.length===3,q.id+' three distractors');
   for(const a of q.explanationTeaching.otherOptions)check(a.optionIndex!==q.correctIndex&&rich.textContent.includes(q.options[a.optionIndex]),q.id+' distractor mapping');
   answers[q.correctIndex]++;count++;
  }
 }
 check(count===EXPECTED&&answers.every(n=>n===EXPECTED/4),'subject balance');
 output.textContent=JSON.stringify({result:'PASS',questions:count,answerDistribution:answers,realChromiumRenderer:true,referencesLast:true,tablesAndNestedBullets:true,distractorMapping:true});
}catch(e){output.textContent='FAIL: '+e.stack;}
host.replaceChildren();
'''
def main():
 parser=argparse.ArgumentParser();parser.add_argument('--subject',default='Cardiology');parser.add_argument('--expected',type=int,default=416);parser.add_argument('--directory',type=Path);args=parser.parse_args()
 directory=args.directory or ROOT/'build/topic-based-qbank-replacement/completed'/args.subject
 banks=[json.loads(p.read_text(encoding='utf-8')) for p in sorted(directory.glob('*/*/questions.json'))]
 scripts=''.join('<script>'+ (ROOT/'assets/vendor'/name).read_text(encoding='utf-8')+'</script>' for name in ['study-rich-text.js','qbank-explanations.js'])
 data=json.dumps(banks,ensure_ascii=True).replace('<','\\u003c')
 with tempfile.TemporaryDirectory(prefix='cnl-qbank-render-',ignore_cleanup_errors=True) as tmp:
  page=Path(tmp)/'check.html';page.write_text('<!doctype html><meta charset="utf-8"><pre id="result"></pre><div id="host"></div>'+scripts+'<script>const EXPECTED='+str(args.expected)+';const BANKS='+data+';'+TEST+'</script>',encoding='utf-8')
  cmd=['C:/Program Files/Google/Chrome/Application/chrome.exe','--headless=new','--disable-gpu','--no-first-run','--disable-extensions','--user-data-dir='+str(Path(tmp)/'profile'),'--dump-dom',page.as_uri()]
  r=subprocess.run(cmd,capture_output=True,encoding='utf-8',errors='replace',timeout=45)
  match=re.search(r'<pre id="result">(.*?)</pre>',r.stdout,re.S)
  result=match[1] if match else 'FAIL: no browser result '+r.stderr[-1000:]
  print(result)
  if not result.startswith('{"result":"PASS"'):return 1
  slug=re.sub(r'[^a-z0-9]+','-',args.subject.lower()).strip('-')
  out=ROOT/'build/topic-based-qbank-replacement'/(slug+'-renderer-validation.json');out.write_text(result,encoding='utf-8')
 return 0
if __name__=='__main__':raise SystemExit(main())
