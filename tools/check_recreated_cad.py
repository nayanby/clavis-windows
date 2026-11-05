"""Check the revised chapter with the app's actual explanation renderer."""
import json,re,subprocess,tempfile
from pathlib import Path
from check_authored_qbank import TEST,ROOT

bank=json.loads((ROOT/'build/topic-based-qbank-replacement/recreated-v2/Cardiology/01. CAD and ACS/questions.json').read_text(encoding='utf-8'))
test=TEST.replace("check(rich.querySelector('table th')&&rich.querySelector('table td'),q.id+' table');","if(rich.querySelector('table'))check(rich.querySelector('table th')&&rich.querySelector('table td'),q.id+' table');")
test=test.replace("rich.querySelector('h2')&&rich.querySelector('h3')&&rich.querySelector('strong')","rich.querySelector('h3')&&rich.querySelector('strong')")
scripts=''.join('<script>'+(ROOT/'assets/vendor'/n).read_text(encoding='utf-8')+'</script>' for n in ['study-rich-text.js','qbank-explanations.js'])
with tempfile.TemporaryDirectory(prefix='cnl-quality-v2-',ignore_cleanup_errors=True) as tmp:
    p=Path(tmp)/'check.html';p.write_text('<meta charset="utf-8"><pre id="result"></pre><div id="host"></div>'+scripts+'<script>const EXPECTED=44;const BANKS='+json.dumps([bank],ensure_ascii=True)+';'+test+'</script>',encoding='utf-8')
    r=subprocess.run(['C:/Program Files/Google/Chrome/Application/chrome.exe','--headless=new','--disable-gpu','--no-first-run','--disable-extensions','--user-data-dir='+str(Path(tmp)/'profile'),'--dump-dom',p.as_uri()],capture_output=True,encoding='utf-8',errors='replace',timeout=45)
    match=re.search(r'<pre id="result">(.*?)</pre>',r.stdout,re.S);assert match,r.stderr[-500:]
    report=json.loads(match[1]);assert report['result']=='PASS';report['tables']='Selected comparison questions only'
    print(json.dumps(report));(ROOT/'build/topic-based-qbank-replacement/recreated-v2/cad-renderer-report.json').write_text(json.dumps(report),encoding='utf-8')
