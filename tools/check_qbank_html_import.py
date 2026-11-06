"""Browser regression checks for offline HTML question extraction."""
from pathlib import Path
import check_rich_explanation as browser

TEST=r"""
<script>
const report=document.createElement('pre');report.id='rich-test-result';document.body.append(report);
(async()=>{try{
  const check=(ok,message)=>{if(!ok)throw Error(message);};
  const parse=window.cnlParseQbankHtml;
  const interactive='<scr'+'ipt>window.executed=false; const QUIZ='+JSON.stringify([
    {stem:'Interactive question?',options:['First','Second','Third','Fourth'],correct:2,
      blocks:[['Mechanism',['**Bold fact**','Second fact']]],table:[['Feature','Value'],['Row','Cell']],
      distractors:[{label:'First',why:'Incorrect mechanism'}]}])+';window.executed=true;</scr'+'ipt>';
  const interactiveRows=parse(interactive);
  check(interactiveRows.length===1 && interactiveRows[0].correctIndex===2,'Interactive array and numeric correct field');
  check(interactiveRows[0].explanationHtml.includes('<strong>Bold fact</strong>'),'Structured explanation emphasis');
  check(interactiveRows[0].explanationHtml.includes('<table>') && interactiveRows[0].explanationHtml.includes('Other Options'),'Structured comparison and distractors');
  check(!window.executed,'Interactive scripts never execute');
  const numbered=`<h2>Question 1</h2><p>A patient has fever. What is the diagnosis?</p>
    <p>A. Malaria</p><p>B. Influenza</p><p>Answer: B</p><p>Explanation:</p>
    <h2>Mechanism</h2><p class=BS1>Key points</p><p>1. Keep this explanation point.</p>
    <table><tr><th>Finding</th><th>Cause</th></tr><tr><td>Fever</td><td>Infection</td></tr></table>
    <p>2. Which therapy?</p><p>(A) Treatment A</p><p>(B) Treatment B</p>
    <p>Correct answer: A</p><p>Explanation: Useful treatment.</p>
    <h3>Q3. Uncertain answer?</h3><p>A) First</p><p>B) Second</p>`;
  const rows=parse(numbered);
  check(rows.length===3,'All numbered questions extracted: '+rows.length);
  check(rows[0].question.includes('A patient'),'Question continuation preserved');
  check(rows[0].options[0]==='Malaria','Options extracted');
  check(rows[0].correctIndex===1,'Letter answer mapped');
  check(rows[0].explanationHtml.includes('<h2>Mechanism</h2>'),'Explanation heading preserved');
  check(rows[0].explanationHtml.includes('boldside1'),'BS style preserved');
  check(rows[0].explanationHtml.includes('<table>'),'Explanation table preserved');
  check(rows[0].explanation.includes('Keep this explanation point'),'Numbered explanation kept');
  check(rows[1].options[1]==='Treatment B','Parenthesized options extracted');
  check(rows[1].correctIndex===0,'Second question answer mapped');
  check(rows[2].correctIndex===-1 && rows[2].answerReviewRequired,'Unknown answer ungraded');
  const cards=parse(`<article class=question-card data-correct-index=1><h3>Card stem?</h3>
    <div class=option>A. Alpha</div><div class=option>B. Beta</div>
    <div class=explanation><h4>Reason</h4><table><tr><td>Cell</td></tr></table></div></article>`);
  check(cards.length===1 && cards[0].correctIndex===1,'Card layout extracted');
  check(cards[0].explanationHtml.includes('<h4>'),'Card explanation formatting preserved');
  const embedded='<scr'+'ipt type="application/json">'+JSON.stringify({questions:[
    {question:'JSON stem?',options:['A','B'],correctIndex:0,explanation:'Reason'},
    {question:'JSON stem?',options:['A','B'],correctIndex:0}]})+'</scr'+'ipt>';
  const json=parse(embedded);check(json.length===1 && json[0].correctIndex===0,'Embedded JSON and duplicates handled');
  const multi=parse('<p>Q1. Choose?</p><p>A. One</p><p>B. Two</p><p>Answer: A, B</p>');
  check(multi[0].answerReviewRequired,'Multiple answers require review');
  const hostile=parse('<p>Q1. Safe?</p><p>A. Yes</p><p>B. No</p><p>Answer: A</p><p>Explanation:</p><img src=x onerror="window.bad=true"><p onclick="bad()">Text</p>');
  check(!hostile[0].explanationHtml.includes('onclick') && !window.bad,'No executable imported markup');
  check(parse('<h1>Notes without questions</h1>').length===0,'No invented questions');
  const many=Array.from({length:201},(_,i)=>({question:'Imported '+i+'?',options:['One','Two'],correctIndex:0}));
  const importHtml='<scr'+'ipt type="application/json">'+JSON.stringify({questions:many})+'</scr'+'ipt>';
  const importFile={name:'Bank.html',size:importHtml.length,text:async()=>importHtml};
  const create=document.createElement.bind(document);
  document.createElement=(tag,...args)=>{
    const element=create(tag,...args);
    if(tag==='input')element.click=()=>{
      if(element.type==='file'){Object.defineProperty(element,'files',{value:[importFile]});element.dispatchEvent(new Event('change'));}
    };
    return element;
  };
  const posts=[];let failSecond=true,refreshes=0;
  window.alert=()=>{};
  window.fetch=async(url,options)=>{
    if(!options?.method)return {ok:true,json:async()=>({quizzes:[{folder:'HTML Imports',document:'Bank'}]})};
    const payload=JSON.parse(options.body);
    if(payload.headingIndex===1 && failSecond){failSecond=false;return {ok:false,status:503};}
    posts.push(payload);return {ok:true};
  };
  const wait=()=>new Promise(resolve=>setTimeout(resolve,20));
  window.cnlImportQbankHtml(async()=>{refreshes++;});
  for(let i=0;i<30 && !document.querySelector('dialog[open]');i++)await wait();
  const dialog=document.querySelector('dialog[open]');check(dialog,'Import preview opens');
  check(dialog.querySelectorAll('details').length===201,'Every question previewed');
  check(posts.length===0,'Preview does not write data');
  dialog.querySelector('form').requestSubmit();await wait();
  check(posts.length===1 && posts[0].questions.length===200,'First part saved without truncation');
  check(dialog.querySelector('[role=alert]').textContent.includes('part 2'),'Partial failure reported');
  dialog.querySelector('form').requestSubmit();await wait();
  check(posts.length===2 && posts[1].questions.length===1,'Retry saves only remaining questions');
  check(posts.every(row=>row.document==='Bank (2)'),'Existing bank not overwritten');
  check(refreshes===1 && !dialog.open,'Successful import refreshes Qbank');
  report.textContent='RICH_EXPLANATION_PASS';
}catch(error){report.textContent='HTML_IMPORT_FAIL: '+error.stack;}})();
</script>
"""

if __name__=='__main__':
    source=(Path(__file__).resolve().parents[1]/'assets/vendor/qbank-html-import.js').read_text(encoding='utf-8')
    browser.TEST='<script>'+source+'</script>'+TEST
    raise SystemExit(browser.main())
