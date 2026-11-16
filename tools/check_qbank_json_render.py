"""Render a bank's own offline explanation HTML/CSS in isolated headless Chrome."""
import argparse
import hashlib
import html
import json
from pathlib import Path
import re
import subprocess
import tempfile

CHECK = r"""
<script>
const failures=[];
const check=(v,label)=>{if(!v)failures.push(label)};
const css=e=>getComputedStyle(e);
for(const q of document.querySelectorAll('article')){
 const h2=q.querySelector('h2'),h3=q.querySelector('h3');
 check(css(q).fontFamily.startsWith('Arial'),'Arial: '+q.id);
 check(css(q).fontSize==='17px','body size: '+q.id);
 check(css(h2).fontSize==='18px'&&css(h2).color==='rgb(111, 61, 93)'&&css(h2).backgroundColor==='rgb(231, 225, 228)','title: '+q.id);
 check(css(h3).fontSize==='17px'&&css(h3).color==='rgb(35, 61, 107)'&&css(h3).backgroundColor==='rgba(0, 0, 0, 0)','subheading: '+q.id);
 for(const e of q.querySelectorAll('strong'))check(css(e).fontSize==='17px'&&css(e).color==='rgb(35, 61, 107)','bold: '+q.id);
 for(const e of q.querySelectorAll('p'))check(css(e).marginBottom==='8px','paragraph: '+q.id);
 for(const e of q.querySelectorAll('mark'))check(css(e).backgroundColor==='rgb(255, 242, 179)','highlight: '+q.id);
 for(const e of q.querySelectorAll('th'))check(css(e).backgroundColor==='rgb(111, 61, 93)'&&css(e).color==='rgb(255, 255, 255)','table header: '+q.id);
 for(const e of q.querySelectorAll('.table-wrap'))check(css(e).overflowX==='auto','table scroll: '+q.id);
}
check(document.documentElement.scrollWidth<=innerWidth+1,'page overflow');
document.getElementById('render-report').textContent=JSON.stringify({status:failures.length?'failed':'passed',questions:document.querySelectorAll('article').length,viewport:innerWidth,failures});
</script>
"""


def main():
    ap=argparse.ArgumentParser();ap.add_argument('bank');args=ap.parse_args()
    source=Path(args.bank).resolve();bank=json.loads(source.read_text(encoding='utf-8'))
    root=Path(__file__).resolve().parents[1]
    out=root/'outputs'/'qbank-render'/f"cardiology-{bank['chapterOrder']:02}"
    out.mkdir(parents=True,exist_ok=True)
    markup=''.join('<article id="'+q['id']+'"><p>'+html.escape(q['question'])+'</p>'+q['explanationHtml']+'</article>' for q in bank['questions'])
    page=out/'explanations.html'
    page.write_text('<!doctype html><html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>'+bank['explanationCss']+'body{margin:16px;line-height:1.45}article{max-width:1100px;margin:0 auto 32px}#render-report{display:none}</style><body>'+markup+'<pre id="render-report"></pre>'+CHECK+'</body></html>',encoding='utf-8')
    chrome=Path('C:/Program Files/Google/Chrome/Application/chrome.exe')
    results=[]
    with tempfile.TemporaryDirectory(prefix='qbank-render-',dir=out,ignore_cleanup_errors=True) as tmp:
        assert Path(tmp).resolve().parent==out.resolve()
        for width in [1200,540]:
            screenshot=out/f'preview-{width}.png'
            command=[str(chrome),'--headless=new','--disable-gpu','--no-first-run','--no-default-browser-check',f'--user-data-dir={tmp}/profile-{width}',f'--window-size={width},1000','--hide-scrollbars','--force-device-scale-factor=1','--virtual-time-budget=1000',f'--screenshot={screenshot}','--dump-dom',page.as_uri()]
            result=subprocess.run(command,capture_output=True,encoding='utf-8',timeout=45)
            match=re.search(r'<pre id="render-report">(.*?)</pre>',result.stdout,re.S)
            assert match,(result.returncode,result.stderr[-1000:])
            report=json.loads(html.unescape(match.group(1)));assert report['status']=='passed',report
            assert report['viewport']<=width,'Browser minimum layout width exceeds screenshot width'
            assert report['questions']==len(bank['questions'])
            assert screenshot.is_file()
            report['screenshot']=str(screenshot);results.append(report)
    audit=dict(status='passed',scope='Bank-provided offline HTML and CSS, not application theme overrides',bankSha256=hashlib.sha256(source.read_bytes()).hexdigest(),results=results)
    (out/'render-report.json').write_text(json.dumps(audit,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(audit,indent=2))


if __name__=='__main__':main()
