/* Safe, offline renderer for reviewed structured QBank explanations. */
(() => {
  if (window.cnlConciseQbankInstalled) return;
  const original = window.cnlRenderQbankExplanation;
  if (typeof original !== 'function') return;
  window.cnlConciseQbankInstalled = true;
  const style = document.createElement('style');
  style.textContent = `
  .cnl-qbank-explanation.cnl-qbank-concise{font-family:Arial,Helvetica,sans-serif!important;font-size:17px!important;line-height:1.45;color:#242424}
  .cnl-qbank-concise *{font-family:Arial,Helvetica,sans-serif!important;font-size:17px!important}
  .cnl-qbank-concise h2{font-size:18px!important;font-weight:bold;color:#6F3D5D!important;background:#E7E1E4!important;padding:8px;margin:4px 0 8px}
  .cnl-qbank-concise h3{color:#233D6B!important;background:transparent!important;border-bottom:1px solid #c6ccd6;margin:4px 0 6px;padding:0;font-weight:bold}
  .cnl-qbank-concise strong{color:#233D6B!important;font-weight:bold}
  .cnl-qbank-concise p{margin:0 0 8px}.cnl-qbank-concise ul,.cnl-qbank-concise ol{padding-left:24px;margin:4px 0 8px}
  .cnl-qbank-concise li{margin:3px 0}.cnl-qbank-concise li li{margin:2.83px 0}
  .cnl-qbank-concise mark{background:#FFF2B3;color:inherit;padding:0 2px}
  .cnl-qbank-concise .qbc-table{overflow-x:auto;max-width:100%;margin:8px 0}
  .cnl-qbank-concise table{border-collapse:collapse;width:100%}.cnl-qbank-concise th,.cnl-qbank-concise td{border:1px solid #ccd0d5;padding:6px;vertical-align:top}
  .cnl-qbank-concise th{background:#6F3D5D!important;color:white!important}.cnl-qbank-concise th strong{color:white!important}
  .cnl-qbank-concise tbody tr:nth-child(even){background:#f6f7f9}
  .cnl-qbank-concise .qbc-flow{display:flex;flex-wrap:wrap;gap:8px}.cnl-qbank-concise .qbc-flow li{flex:1 1 150px;border:1px solid #bbc4d3;border-radius:4px;padding:7px;margin-right:12px}
  .cnl-qbank-concise .qbc-flow li:not(:last-child)::after{content:' →';color:#233D6B;font-weight:bold}
  .cnl-qbank-concise a{overflow-wrap:anywhere}`;
  document.head.append(style);
  function el(tag, text) {
    const n = document.createElement(tag);
    if (text !== undefined) n.textContent = String(text);
    return n;
  }
  function inline(parent, value) {
    String(value ?? '').split(/(\*\*[^*]+\*\*|==[^=]+==)/g).forEach(part => {
      if (part.startsWith('**') && part.endsWith('**')) {
        const n=el('strong'); inline(n,part.slice(2,-2)); parent.append(n);
      } else if (part.startsWith('==') && part.endsWith('==')) {
        parent.append(el('mark',part.slice(2,-2)));
      } else parent.append(document.createTextNode(part));
    });
  }
  function list(parent, items, tag='ul') {
    const l=el(tag);
    items.forEach(item => {
      const li=el('li'); inline(li,typeof item==='string'?item:item.text);
      if (Array.isArray(item.children) && item.children.length) list(li,item.children);
      l.append(li);
    });
    parent.append(l); return l;
  }
  window.cnlRenderQbankExplanation = (host,q,gradable) => {
    host.classList.remove('cnl-qbank-concise');
    if (q.explanationStyle !== 'concise_structured' || !q.explanationTeaching?.sections) return original(host,q,gradable);
    const d=q.explanationTeaching; host.replaceChildren(); host.classList.add('cnl-qbank-explanation','cnl-qbank-concise');
    host.append(el('h2',d.title));
    if (gradable) {
      const p=el('p'); p.append(el('strong','Correct answer: '+String.fromCharCode(65+q.correctIndex)+' — '+q.options[q.correctIndex])); host.append(p);
    } else host.append(el('p',[q.answerText,q.reviewNote].filter(Boolean).join(' — ')));
    d.sections.forEach(s => {host.append(el('h3',s.heading));list(host,s.bullets,s.listType==='ol'?'ol':'ul');});
    if (d.flow?.length) {host.append(el('h3','Decision Pathway'));list(host,d.flow,'ol').classList.add('qbc-flow');}
    (d.tables||[]).forEach(t => {
      const box=el('div');box.className='qbc-table';const table=el('table');const head=el('thead');const hr=el('tr');
      t.headers.forEach(x=>{const th=el('th');inline(th,x);hr.append(th);});head.append(hr);table.append(head);
      const body=el('tbody');t.rows.forEach(row=>{const tr=el('tr');row.forEach(x=>{const td=el('td');inline(td,x);tr.append(td);});body.append(tr);});
      table.append(body);box.append(table);host.append(box);
    });
    if (!q.calculation && d.otherOptions?.length) {
      host.append(el('h3','Other Options'));
      list(host,d.otherOptions.map(a=>'**'+String.fromCharCode(65+a.optionIndex)+' — '+q.options[a.optionIndex]+':** '+a.explanation));
    }
    if (q.references?.length) {
      host.append(el('h3','References'));const ul=el('ul');const seen=new Set();
      q.references.forEach(r=>{try {const url=new URL(r.url);if(url.protocol!=='https:'||seen.has(url.href))return;seen.add(url.href);
        const a=el('a',r.label||url.hostname);a.href=url.href;a.target='_blank';a.rel='noopener noreferrer';const li=el('li');li.append(a);ul.append(li);
      } catch { /* Invalid references are not linked. */ }});host.append(ul);
    }
  };
})();
