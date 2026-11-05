"""Verify every imported explanation in the installed app's Chromium renderer."""
import json,re,subprocess,tempfile
from pathlib import Path
from import_replacement_html_archives import OUT,REPO
manifest=json.loads((OUT/'staging-report.json').read_text(encoding='utf-8'))
banks=[json.loads(Path(p).read_text(encoding='utf-8')) for p in manifest['stagedFiles']]
assert len(banks)==manifest['banks'] and manifest['questions']==sum(len(b['questions']) for b in banks)
test=r'''
const check=(v,m)=>{if(!v)throw Error(m)};let count=0,tables=0,nested=0;const ids=new Set();
try{for(const bank of BANKS)for(const q of bank.questions){
 check(q.options.length===4&&Number.isInteger(q.correctIndex)&&q.correctIndex>=0&&q.correctIndex<4,q.id+' options');
 check(!ids.has(q.id),q.id+' duplicate');ids.add(q.id);
 window.cnlRenderQbankExplanation(host,q,true);
 const expected=new DOMParser().parseFromString(q.explanationHtml,'text/html');
 const actual=host.querySelector('.cnl-notes-explanation');check(actual,q.id+' explanation');
 const norm=x=>x.textContent.replace(/\s+/g,' ').trim();
 check(norm(actual)===norm(expected.body),q.id+' missing explanation text');
 check(actual.querySelectorAll('table').length===expected.querySelectorAll('table').length,q.id+' tables');
 check(!actual.querySelector('script,iframe,object,input,button,img,[onclick]'),q.id+' unsafe content');
 check(host.querySelector('.cnl-qbank-answer').textContent.includes(q.options[q.correctIndex]),q.id+' answer');
 tables+=actual.querySelectorAll('table').length;if(actual.querySelector('li ul'))nested++;count++;
 }check(count===EXPECTED,'count');result.textContent=JSON.stringify({result:'PASS',banks:BANKS.length,questions:count,preservedTables:tables,explanationsWithNestedLists:nested,exactExplanationText:true,answersVerified:true});
}catch(e){result.textContent='FAIL: '+e.stack}host.replaceChildren();
'''
scripts=''.join('<script>'+(REPO/'assets/vendor'/n).read_text(encoding='utf-8')+'</script>' for n in ['study-rich-text.js','qbank-explanations.js'])
with tempfile.TemporaryDirectory(prefix='cnl-html-import-qa-',ignore_cleanup_errors=True) as tmp:
    p=Path(tmp)/'check.html';p.write_text('<meta charset="utf-8"><pre id="result"></pre><div id="host"></div>'+scripts+'<script>const EXPECTED='+str(manifest['questions'])+';const BANKS='+json.dumps(banks,ensure_ascii=True).replace('<','\\u003c')+';'+test+'</script>',encoding='utf-8')
    r=subprocess.run(['C:/Program Files/Google/Chrome/Application/chrome.exe','--headless=new','--disable-gpu','--disable-extensions','--no-first-run','--user-data-dir='+str(Path(tmp)/'profile'),'--dump-dom',p.as_uri()],capture_output=True,encoding='utf-8',errors='replace',timeout=60)
    m=re.search(r'<pre id="result">(.*?)</pre>',r.stdout,re.S);assert m,r.stderr[-1000:]
    print(m[1]);report=json.loads(m[1]);assert report['result']=='PASS'
    (OUT/'renderer-report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
