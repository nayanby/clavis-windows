/* Render trusted structure as DOM text, never executable explanation HTML. */
(() => {
  'use strict';
  const isAnswerLine=text=>/^\s*correct\s+answer\s*[:\uFF1A\u2014\u2013-]/i.test(String(text||''));
  function node(tag,text,className) {
    const el=document.createElement(tag);
    if(text!=null)el.textContent=String(text);
    if(className)el.className=className;
    return el;
  }
  function inline(parent,text) {
    // Only emphasis is interpreted. Tags and other input remain ordinary text.
    String(text||'').split(/(\*\*[^*]+\*\*)/g).forEach(part=>{
      if(part.startsWith('**')&&part.endsWith('**'))parent.append(node('strong',part.slice(2,-2)));
      else parent.append(document.createTextNode(part));
    });
  }
  function table(parent,data) {
    if(!Array.isArray(data?.headers)||!Array.isArray(data?.rows))return;
    const box=node('div',null,'cnl-qbank-table-scroll');
    const el=node('table');
    const head=node('tr');
    data.headers.forEach(label=>head.append(node('th',label)));
    const thead=node('thead');thead.append(head);el.append(thead);
    const body=node('tbody');
    data.rows.forEach(row=>{
      if(!Array.isArray(row))return;
      const tr=node('tr');
      data.headers.forEach((_,i)=>{const td=node('td');inline(td,row[i]||'');tr.append(td);});
      body.append(tr);
    });
    el.append(body);box.append(el);parent.append(box);
  }
  window.cnlRenderQbankExplanation=(host,question,gradable)=>{
    host.replaceChildren();
    host.classList.add('cnl-qbank-explanation');
    const paper=document.getElementById('paper');
    if(paper)host.style.setProperty('--cnl-qbank-font',getComputedStyle(paper).getPropertyValue('--cnl-note-body-font')||'"Lato"');
    const detail=question.explanationDetail;
    if(!gradable)host.append(node('p',[question.answerText,question.reviewNote].filter(Boolean).join(' — '),'cnl-qbank-review'));
    if(question.explanationHtml){
      if(gradable)host.append(node('p','Correct answer: '+String.fromCharCode(65+question.correctIndex)+'. '+question.options[question.correctIndex],'cnl-qbank-answer'));
      const rich=node('div',null,'cnl-notes-explanation');
      rich.append(...window.cnlCleanExplanationHtml(question.explanationHtml).childNodes);
      if(gradable)rich.querySelectorAll('p').forEach(p=>{if(isAnswerLine(p.textContent))p.remove();});
      host.append(rich);
    }else if(detail?.version===1){
      if(detail.answer)host.append(node('p',detail.answer,'cnl-qbank-answer'));
      (detail.sections||[]).forEach(section=>{
        (section.paragraphs||[]).forEach(text=>{const p=node('p');inline(p,text);host.append(p);});
        if(section.bullets?.length){const ul=node('ul');section.bullets.forEach(text=>{const li=node('li');inline(li,text);ul.append(li);});host.append(ul);}
        if(section.table)table(host,section.table);
      });
      if(detail.alternatives)table(host,detail.alternatives);
      if(detail.takeaway){const p=node('p');inline(p,detail.takeaway);host.append(p);}
    }else{
      if(gradable)host.append(node('p','Correct answer: '+String.fromCharCode(65+question.correctIndex)+'. '+question.options[question.correctIndex],'cnl-qbank-answer'));
      // Unrewritten entries remain readable and are never labelled as rewritten.
      String(question.explanation||'').split(/\n\s*\n/).filter(text=>text.trim()&&(!gradable||!isAnswerLine(text))).forEach(text=>{const p=node('p');inline(p,text);host.append(p);});
    }
    // Rich HTML and plain explanations can carry the same verified reference list.
    const sources=[...(Array.isArray(question.references)?question.references:[]),...(Array.isArray(detail?.sources)?detail.sources:[])];
    if(sources.length){
      const refs=node('div',null,'cnl-qbank-references');
      refs.append(node('h3','References'));
      const list=node('ol');const seen=new Set();
      sources.forEach(source=>{
        try{
          const url=new URL(source.url);if(url.protocol!=='https:'||seen.has(url.href))return;seen.add(url.href);
          const a=node('a',source.label||url.hostname);a.href=url.href;a.target='_blank';a.rel='noopener noreferrer';const item=node('li');item.append(a);list.append(item);
        }catch{}
      });
      if(list.children.length){refs.append(list);host.append(refs);}
      if(list.children.length)host.querySelectorAll('.cnl-notes-explanation').forEach(rich=>{
        rich.querySelectorAll('h1,h2,h3,h4,p').forEach(heading=>{
          if(!/^references\s*:?\s*$/i.test(heading.textContent))return;
          const section=[];let next=heading.nextElementSibling;
          while(next&&!/^H[1-4]$/.test(next.tagName)){section.push(next);next=next.nextElementSibling;}
          if(section.length&&!section.some(part=>part.querySelector('a[href]'))){section.forEach(part=>part.remove());heading.remove();}
        });
      });
    }
  };
})();
