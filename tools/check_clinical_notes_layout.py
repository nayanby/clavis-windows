"""Render every completed module at desktop and mobile widths in Chromium."""
import json,re,subprocess,tempfile
from pathlib import Path
from create_qbank_topic_notes import DEST,CSS
records=json.loads((DEST/'authored-notes.json').read_text(encoding='utf-8'))
docs=[dict(key=k,source=Path(r['file']).read_text(encoding='utf-8')) for k,r in records.items()]
test=r'''
const result=document.querySelector('#result'),host=document.querySelector('#host');let checked=0;
const check=(x,m)=>{if(!x)throw Error(m)};
try{for(const item of DOCS){
 const original=new DOMParser().parseFromString(item.source,'text/html');
 const source=original.querySelector('main');check(source,item.key+' main');
 host.innerHTML=source.outerHTML;
 const main=host.querySelector('main');
 check(main.textContent===source.textContent,item.key+' text');
 check(main.querySelectorAll('table').length===source.querySelectorAll('table').length,item.key+' tables');
 check(!main.querySelector('script,iframe,object'),item.key+' inert');
 for(const a of main.querySelectorAll('a[href^="#"]'))check(main.querySelector('[id="'+a.hash.slice(1)+'"]'),item.key+' anchor');
 for(const width of [1100,390]){
  host.style.width=width+'px';
  const overflow=main.scrollWidth-main.clientWidth;
  check(overflow<=2,item.key+' horizontal overflow '+width+' '+overflow);
 }
 checked++;
}result.textContent=JSON.stringify({result:'PASS',modules:checked,desktopAndMobileWidths:true,textAndTablesPreserved:true,internalNavigation:true});}
catch(e){result.textContent='FAIL: '+e.stack}host.replaceChildren();
'''
with tempfile.TemporaryDirectory(prefix='cnl-clinical-note-qa-',ignore_cleanup_errors=True) as tmp:
    p=Path(tmp)/'check.html'
    p.write_text('<meta charset="utf-8"><style>'+CSS+'#host{max-width:100%}</style><pre id="result"></pre><div id="host"></div><script>const DOCS='+json.dumps(docs,ensure_ascii=True).replace('<','\\u003c')+';'+test+'</script>',encoding='utf-8')
    r=subprocess.run(['C:/Program Files/Google/Chrome/Application/chrome.exe','--headless=new','--disable-gpu','--no-first-run','--disable-extensions','--user-data-dir='+str(Path(tmp)/'profile'),'--window-size=1200,1000','--dump-dom',p.as_uri()],capture_output=True,encoding='utf-8',errors='replace',timeout=60)
    m=re.search(r'<pre id="result">(.*?)</pre>',r.stdout,re.S);assert m,r.stderr[-500:]
    print(m[1]);result=json.loads(m[1]);assert result['result']=='PASS' and result['modules']==42
    (DEST/'layout-validation.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
