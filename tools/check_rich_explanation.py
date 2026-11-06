"""Offline Edge regression checks for Word explanation structure and paste handling."""
import re
import subprocess
import tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
TEST=r"""
<script>
const report=document.createElement('pre');report.id='rich-test-result';document.body.append(report);
try{
  const check=(ok,message)=>{if(!ok)throw Error(message);};
  const word=`<style>p.Custom{mso-style-name:"BS 2"}</style>
    <h1>Heading one</h1><p class=MsoHeading2>Heading two</p>
    <p style="mso-outline-level:3">Heading three</p><h4>Heading four</h4>
    <p class=BS1>Side one</p><p class=Custom>Side two</p><p class=BoldSide3>Side three</p>
    <p style="mso-list:l0 level1 lfo1"><span style="mso-list:Ignore">• </span>First</p>
    <p style="mso-list:l0 level2 lfo1"><span style="mso-list:Ignore">• </span>Nested</p>
    <p style="mso-list:l0 level1 lfo1"><span style="mso-list:Ignore">• </span>Second</p>
    <table onclick="bad()"><tr><th colspan=2>Header</th></tr><tr><td rowspan=2>A</td><td><b>B</b></td></tr>
    <tr><td>C</td></tr></table><p><span style="font-weight:bold">Bold</span></p>
    <img src=x onerror="bad()"><a href="javascript:bad()">Safe text</a>`;
  const clean=window.cnlCleanExplanationHtml(word);
  for(const tag of ['h1','h2','h3','h4'])check(clean.querySelector(tag),tag+' retained');
  for(const kind of ['boldside1','boldside2','boldside3'])check(clean.querySelector('.'+kind),kind+' retained');
  check(clean.querySelectorAll('ul>li').length===3,'Word list structure');
  check(clean.querySelector('ul>li>ul>li')?.textContent==='Nested','Nested Word list');
  check(clean.querySelector('th').colSpan===2,'Column merge');
  check(clean.querySelector('td').rowSpan===2,'Row merge');
  check(clean.querySelector('strong')?.textContent==='Bold','Word bold retained');
  check(!clean.querySelector('img,script,style,[onclick],[onerror],[href]'),'Only inert content retained');
  check(clean.textContent.includes('Safe text'),'Link text retained');
  check(window.cnlCleanExplanationHtml(clean.innerHTML).innerHTML===clean.innerHTML,'Stable after reload');
  const form=document.createElement('form');document.body.append(form);
  const field=window.cnlRichExplanationField(form,{explanation:'Old explanation'});
  const editor=form.querySelector('[contenteditable]');editor.focus();
  const range=document.createRange();range.selectNodeContents(editor);
  window.getSelection().removeAllRanges();window.getSelection().addRange(range);
  const clipboard=new DataTransfer();clipboard.setData('text/html',word);clipboard.setData('text/plain','Plain fallback');
  editor.dispatchEvent(new ClipboardEvent('paste',{clipboardData:clipboard,bubbles:true,cancelable:true}));
  const saved=field.read();check(saved.explanationHtml.includes('<h1>'),'Pasted HTML saved');
  check(saved.explanation.includes('Nested'),'Plain text fallback saved');
  const host=document.createElement('div');document.body.append(host);
  window.cnlRenderQbankExplanation(host,{...saved,options:['A','B'],correctIndex:0},true);
  check(host.querySelector('.cnl-notes-explanation h2'),'Heading rendered');
  check(host.querySelector('td[rowspan="2"]'),'Table rendered');
  const reopened=window.cnlRichExplanationField(form,saved);
  check(Object.keys(reopened.read()).length===0,'Unchanged explanation preserved');
  report.textContent='RICH_EXPLANATION_PASS';
}catch(error){report.textContent='RICH_EXPLANATION_FAIL: '+error.stack;}
</script>
"""

def main():
    edge=next(path for path in (
        Path(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'),
        Path(r'C:\Program Files\Microsoft\Edge\Application\msedge.exe')) if path.is_file())
    scripts=''.join('<script>'+ (ROOT/'assets/vendor'/name).read_text(encoding='utf-8')+'</script>'
                    for name in ['study-rich-text.js','qbank-explanations.js'])
    with tempfile.TemporaryDirectory(prefix='cnl-rich-') as tmp:
        target=Path(tmp)/'test.html'
        target.write_text('<!doctype html><meta charset="utf-8"><body>'+scripts+TEST+'</body>',encoding='utf-8')
        result=subprocess.run([str(edge),'--headless=new','--disable-gpu','--no-first-run',
            f'--user-data-dir={Path(tmp)/"profile"}','--virtual-time-budget=6000','--dump-dom',target.as_uri()],
            capture_output=True,encoding='utf-8',errors='replace',timeout=35)
        match=re.search(r'<pre id="rich-test-result">(.*?)</pre>',result.stdout,re.S)
        message=match.group(1) if match else result.stderr[-1500:] or 'No browser result.'
        print(message)
        return 0 if message=='RICH_EXPLANATION_PASS' else 1

if __name__=='__main__':
    raise SystemExit(main())
