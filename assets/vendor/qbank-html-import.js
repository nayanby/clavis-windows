/* Extract saved HTML without running its scripts or sending it to an AI service. */
(() => {
  'use strict';
  const text=node=>String(node?.textContent||'').replace(/\u00a0/g,' ').trim();
  const answerPrefix=/^(?:correct\s+answer|correct\s+option|answer|ans|key)\s*(?::|[.\-–]|\bis\b)\s*/i;
  const escape=value=>String(value??'').replace(/[&<>"']/g,ch=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));
  const rich=value=>escape(value).replace(/\*\*([^]*?)\*\*/g,'<strong>$1</strong>');
  function block(value){
    if(value===undefined||value===null||value==='')return '';
    if(typeof value!=='object')return '<p>'+rich(value)+'</p>';
    if(!Array.isArray(value)){
      if(value.headers && value.rows)return table(value);
      if(value.title && (value.points||value.bullets||value.content))return '<h3>'+rich(value.title)+'</h3>'+block(value.points||value.bullets||value.content);
      return Object.entries(value).map(([key,part])=>['table','deep_table'].includes(key)?table(part):'<h3>'+rich(key)+'</h3>'+block(part)).join('');
    }
    if(value.length===2 && typeof value[0]==='string' && Array.isArray(value[1]))return '<h3>'+rich(value[0])+'</h3>'+block(value[1]);
    if(value.every(part=>typeof part==='string'))return '<ul>'+value.map(part=>'<li>'+rich(part)+'</li>').join('')+'</ul>';
    return value.map(part=>block(part)).join('');
  }
  function table(value){
    if(!value)return '';
    let caption='',headers,rows;
    if(!Array.isArray(value)){headers=value.headers||[];rows=value.rows||[];}
    else if(typeof value[0]==='string' && Array.isArray(value[1]) && Array.isArray(value[2])){[caption,headers,rows]=value;}
    else [headers,...rows]=value;
    if(!Array.isArray(headers)||!Array.isArray(rows))return block(value);
    if(rows.length===1 && Array.isArray(rows[0]?.[0]))rows=rows[0];
    return (caption?'<h3>'+rich(caption)+'</h3>':'')+'<table><thead><tr>'+headers.map(cell=>'<th>'+rich(cell)+'</th>').join('')+'</tr></thead><tbody>'+rows.map(row=>'<tr>'+(Array.isArray(row)?row:[row]).map(cell=>'<td>'+rich(cell)+'</td>').join('')+'</tr>').join('')+'</tbody></table>';
  }
  function explanationHtml(item){
    if(item.explanationHtml||item.exHtml||item.explanation_html)return item.explanationHtml||item.exHtml||item.explanation_html;
    let result='';
    for(const key of ['title','heading','focus'])if(item[key])result+='<h2>'+rich(item[key])+'</h2>';
    for(const key of ['lead','why','reason','sections','points','blocks','b','notes','note','detail','deep','expl','ex','formula','clinical','explain','explanation','rationale']){
      const value=item[key];if(!value)continue;
      result+=typeof value==='string' && /<\/?(?:p|h[1-4]|table|ul|ol|div|strong|b|br)\b/i.test(value)?value:block(value);
    }
    for(const key of ['table','deep_table'])result+=table(item[key]);
    if(item.rich){result+=block(item.rich.points)+table(item.rich.table);}
    if(item.notes_html)result+=item.notes_html;
    for(const key of ['distractors','other','others','wrongs']){
      if(!item[key])continue;
      const value=item[key];
      if(Array.isArray(value))result+='<h3>Other Options</h3><ul>'+value.map(part=>{
        if(Array.isArray(part)&&part.length===2&&Number.isInteger(part[0]))return '<li>'+rich(part[1])+'</li>';
        if(part && typeof part==='object'&&!Array.isArray(part))return '<li>'+((part.label||part.option)?'<strong>'+rich(part.label||part.option)+':</strong> ':'')+rich(part.why||part.reason||part.explanation||'')+'</li>';
        return '<li>'+rich(part)+'</li>';
      }).join('')+'</ul>';
      else result+='<h3>Other Options</h3>'+block(value);
    }
    if(item.pearl)result+='<h3>Key point</h3>'+block(item.pearl);
    if(item.references)result+='<h3>References</h3>'+block(item.references);
    return result;
  }
  function answerIndex(answer,options){
    const value=String(answer||'').replace(answerPrefix,'').trim();
    const match=value.match(/^\(?([A-H])\)?(?:\s*[.):\-–]\s*|\s+|$)/i);
    if(match && !/^[A-H]\s*[,/&+]\s*[A-H]/i.test(value)){
      const index=match[1].toUpperCase().charCodeAt(0)-65;
      if(index<options.length)return index;
    }
    return options.findIndex(option=>option.toLowerCase()===value.toLowerCase());
  }
  function normalise(item){
    const question=String(item.question||item.stem||item.q||item.text||'').trim();
    let options=item.options||item.choices||item.opts||item.o||[];
    if(options && !Array.isArray(options) && typeof options==='object')options=Object.values(options);
    options=Array.isArray(options)?options.map(value=>String(typeof value==='object' ? value?.text||value?.label||'' : value).trim()):[];
    const answer=item.correctIndex??item.correct??item.answer??item.a??item.key??item.correctAnswer;
    let correctIndex=Number.isInteger(answer)?answer:answerIndex(answer??'',options);
    if(correctIndex<0 || correctIndex>=options.length || options.length<2 || item.answerReviewRequired)correctIndex=-1;
    if(!question)return null;
    const cleaned=window.cnlCleanExplanationHtml(explanationHtml(item));const html=cleaned.innerHTML;
    return {question,options,correctIndex,answerReviewRequired:correctIndex<0,
      answerText:String(item.answerText||item.correctAnswer||item.answer||''),
      explanation:cleaned.textContent.trim(),explanationHtml:html,
      sourceQuestion:item,
      ...(item.explanationDetail?.version===1?{explanationDetail:item.explanationDetail}:{}),
      reviewNote:correctIndex<0?'Imported answer needs review. Use Edit question to set the correct answer.':''};
  }
  function parse(html){
    const doc=new DOMParser().parseFromString(String(html),'text/html');
    let questions=[];
    function embedded(value){
      if(Array.isArray(value))for(const item of value)embedded(item);
      else if(value && typeof value==='object'){
        if((value.question||value.stem||value.q) && (value.options||value.choices||value.opts||value.o)){
          const row=normalise(value);if(row)questions.push(row);
        }else for(const key of ['questions','quizzes','items','data'])if(value[key])embedded(value[key]);
      }
    }
    doc.querySelectorAll('script[type="application/json"],script[type="application/ld+json"]').forEach(script=>{
      try{embedded(JSON.parse(script.textContent));}catch{}
    });
    // Read JSON-compatible array literals from interactive banks, never eval scripts.
    if(!questions.length)for(const script of doc.querySelectorAll('script:not([src])')){
      const source=script.textContent;
      for(const match of source.matchAll(/(?:const|let|var)\s+\w+\s*=\s*([\[{])/g)){
        let depth=0,quoted=false,escaped=false,end=match.index+match[0].length-1;
        const start=end;
        for(;end<source.length;end++){
          const ch=source[end];
          if(quoted){if(escaped)escaped=false;else if(ch==='\\')escaped=true;else if(ch==='"')quoted=false;continue;}
          if(ch==='"'){quoted=true;continue;}
          if(ch==='['||ch==='{')depth++;else if(ch===']'||ch==='}')if(--depth===0){end++;break;}
        }
        try{embedded(JSON.parse(source.slice(start,end)));}catch{}
      }
    }
    if(!questions.length){
      for(const section of doc.querySelectorAll('section[id^="q"]')){
        const inputs=[...section.querySelectorAll('input[type="radio"]')];
        const stem=section.querySelector('h2,h3,.stem');const explanation=section.querySelector('[id^="ans"],.explanation');
        const key=inputs[0]?.getAttribute('onchange')?.match(/check\(\s*\d+\s*,\s*(\d+)\s*\)/);
        if(stem && inputs.length && explanation && key){
          questions.push(normalise({question:text(stem).replace(/^Q\d+[.)]\s*/i,''),
            options:inputs.map(input=>text(input.closest('label')||input.parentElement).replace(/^[A-H][.)]\s*/i,'')),
            correctIndex:Number(key[1]),explanationHtml:explanation.innerHTML}));
        }
      }
    }
    if(!questions.length){
      const cards=[...doc.querySelectorAll('.question-card,.question-item,.quiz-question,.mcq,[data-question]')]
        .filter(card=>!card.parentElement?.closest('.question-card,.question-item,.quiz-question,.mcq,[data-question]'));
      for(const card of cards){
        const stem=card.querySelector('.question-text,.question-stem,.stem,.question,h2,h3,h4');
        const optionNodes=[...card.querySelectorAll('.option,.answer-option,.choice,.options li,.choices li')]
          .filter(option=>!option.parentElement?.closest('.option,.answer-option,.choice'));
        if(!stem || !optionNodes.length)continue;
        const options=optionNodes.map(option=>text(option).replace(/^\(?[A-H]\)?[.):\-]\s*/i,''));
        const explanation=card.querySelector('.explanation,.rationale,.solution');
        const answer=card.querySelector('.answer-key,.correct-answer,[data-answer]');
        let correctIndex=optionNodes.findIndex(option=>option.matches('.correct,.is-correct,[data-correct="true"]'));
        const explicit=card.getAttribute('data-correct-index');
        if(explicit!==null && /^\d+$/.test(explicit))correctIndex=Number(explicit);
        if(correctIndex<0)correctIndex=answerIndex(text(answer),options);
        const row=normalise({question:text(stem).replace(/^(?:question|q)\s*\d+\s*[.):\-]?\s*/i,''),
          options,correctIndex,answerText:text(answer),explanation:text(explanation),
          explanationHtml:explanation?.innerHTML||''});
        if(row)questions.push(row);
      }
    }
    if(!questions.length){
      doc.querySelectorAll('script,style,noscript,nav,header,footer').forEach(node=>node.remove());
      // Flatten wrappers, keeping paragraphs/headings and whole tables as ordered blocks.
      const blocks=[];
      function walk(node){
        if(node.nodeType===3){if(text(node))blocks.push({text:text(node),html:''});return;}
        if(node.nodeType!==1)return;
        if(node.matches('p,h1,h2,h3,h4,h5,h6,li,table,pre')){
          const lines=node.innerHTML.split(/<br\s*\/?>/i);
          if(lines.length>1 && node.localName!=='table')for(const line of lines){
            const temp=new DOMParser().parseFromString(line,'text/html');blocks.push({text:text(temp.body),html:line});
          }else blocks.push({text:text(node),html:node.outerHTML});
        }else for(const child of node.childNodes)walk(child);
      }
      walk(doc.body);
      let current=null,explaining=false;
      const finish=()=>{if(current){const row=normalise(current);if(row)questions.push(row);}current=null;explaining=false;};
      for(const [blockIndex,block] of blocks.entries()){
        const line=block.text;
        const start=line.match(/^(?:(?:question|q)\s*\d+\s*[.):\-]?|\d+\s*[.)])\s*(.*)$/i);
        // Numbered items inside an explanation are kept as explanation content.
        const explicit=/^(?:question|q)\s*\d+/i.test(line);
        const following=[];
        for(const item of blocks.slice(blockIndex+1,blockIndex+13)){
          if(/^(?:(?:question|q)\s*\d+|\d+\s*[.)])/i.test(item.text))break;
          following.push(item.text);
        }
        const hasOptions=following.some(value=>/^\(?A\)?[.):\-]\s*\S/i.test(value)) &&
          following.some(value=>/^\(?B\)?[.):\-]\s*\S/i.test(value));
        if(start && (explicit || !explaining || hasOptions)){
          finish();current={question:start[1],options:[],answer:'',explanation:'',explanationHtml:''};continue;
        }
        if(!current)continue;
        if(answerPrefix.test(line)){
          current.answer=line.replace(answerPrefix,'');continue;
        }
        if(/^(?:explanation|rationale|solution)\s*[:.\-–]?/i.test(line)){
          explaining=true;
          const remainder=line.replace(/^(?:explanation|rationale|solution)\s*[:.\-–]?\s*/i,'');
          if(remainder){current.explanation+=remainder+'\n';
            const p=document.createElement('p');p.textContent=remainder;current.explanationHtml+=p.outerHTML;}
          continue;
        }
        const option=line.match(/^\(?([A-H])(?:[.):\-])\s*(.+)$/i);
        if(option && !explaining && option[1].toUpperCase().charCodeAt(0)-65===current.options.length){
          current.options.push(option[2].trim());continue;
        }
        if(explaining || current.answer){
          explaining=true;current.explanation+=line+'\n';current.explanationHtml+=block.html||'';
        }else if(!current.options.length)current.question+=(current.question?'\n':'')+line;
        else current.options[current.options.length-1]+='\n'+line;
      }
      finish();
    }
    const seen=new Set();
    return questions.filter(row=>{
      const key=JSON.stringify([row.question,row.options]);if(seen.has(key))return false;
      seen.add(key);return true;
    });
  }
  window.cnlParseQbankHtml=parse;

  window.cnlConvertQbankHtml=async()=>{
    const api=window.pywebview?.api;
    if(!api?.choose_qbank_html){window.alert('Open the installed desktop app to select HTML files and save JSON beside them.');return;}
    if(window.cnlConvertingHtml)return;
    window.cnlConvertingHtml=true;
    const dialog=document.createElement('dialog');dialog.className='cnl-study-editor';
    const heading=document.createElement('h2');heading.textContent='Convert to JSON';
    const status=document.createElement('p');status.setAttribute('role','status');status.textContent='Select one or more HTML files…';
    const list=document.createElement('div');const close=document.createElement('button');close.className='folder-btn';close.textContent='Close';close.disabled=true;
    close.onclick=()=>dialog.close();dialog.onclose=()=>dialog.remove();
    dialog.addEventListener('cancel',event=>{if(window.cnlConvertingHtml)event.preventDefault();});
    dialog.append(heading,status,list,close);document.body.append(dialog);dialog.showModal();
    try{
      const selection=await api.choose_qbank_html();if(selection.error)throw Error(selection.error);
      if(!selection.files?.length){dialog.close();return;}
      let saved=0;
      for(const [index,file] of selection.files.entries()){
        status.textContent='Converting '+(index+1)+' of '+selection.files.length+'…';
        const row=document.createElement('p');list.append(row);
        try{
          if(file.error)throw Error(file.error);
          const questions=parse(file.html);
          if(!questions.length)throw Error('No questions found. No JSON was written.');
          const result=await api.save_qbank_json(file.token,questions);
          if(result.error)throw Error(result.error);
          saved++;row.textContent=file.name+': '+result.count+' questions saved to '+result.path+
            (result.review?' — '+result.review+' answers need review.':'')+(result.backup?' Previous JSON backed up.':'');
        }catch(error){row.textContent=file.name+': '+error.message;}
      }
      status.textContent='Saved '+saved+' of '+selection.files.length+' files. Each JSON is inside a folder named after its HTML file.';
    }catch(error){status.textContent=error.message;}
    finally{window.cnlConvertingHtml=false;close.disabled=false;}
  };

  window.cnlImportQbankHtml=async refresh=>{
    const picker=document.createElement('input');picker.type='file';picker.accept='.html,.htm,text/html';
    picker.addEventListener('change',async()=>{
      const file=picker.files?.[0];if(!file)return;
      if(file.size>10*1024*1024){window.alert('Choose an HTML file smaller than 10 MB.');return;}
      let questions;
      try{questions=parse(await file.text());}catch(error){window.alert('Could not read this HTML: '+error.message);return;}
      if(!questions.length){window.alert('No questions found. Use question cards, embedded JSON, or numbered questions with A/B/C/D options and Answer / Explanation labels.');return;}
      const dialog=document.createElement('dialog');dialog.className='cnl-study-editor';dialog.setAttribute('aria-label','Import HTML Qbank');
      const form=document.createElement('form');const title=document.createElement('h2');title.textContent='Import HTML Qbank';
      const summary=document.createElement('p');const ungraded=questions.filter(q=>q.answerReviewRequired).length;
      summary.textContent=questions.length+' questions extracted. '+ungraded+' answers need manual review. Preview the extraction before importing.';
      const field=(label,value)=>{const wrap=document.createElement('label');wrap.textContent=label;
        const input=document.createElement('input');input.value=value;input.required=true;input.maxLength=100;wrap.append(input);form.append(wrap);return input;};
      form.append(title,summary);const folder=field('Subject','HTML Imports');
      const name=field('Chapter / bank name',file.name.replace(/\.html?$/i,''));
      const preview=document.createElement('div');preview.className='cnl-html-preview';
      questions.forEach((question,index)=>{
        const item=document.createElement('details');const heading=document.createElement('summary');
        heading.textContent=(index+1)+'. '+question.question;item.append(heading);
        const options=document.createElement('ol');options.type='A';question.options.forEach(value=>{const li=document.createElement('li');li.textContent=value;options.append(li);});
        const answer=document.createElement('p');answer.textContent=question.answerReviewRequired?'Answer needs review':
          'Correct answer: '+String.fromCharCode(65+question.correctIndex);
        const explanation=document.createElement('div');
        window.cnlRenderQbankExplanation(explanation,question,!question.answerReviewRequired);
        item.append(options,answer,explanation);preview.append(item);
      });
      form.append(preview);const error=document.createElement('p');error.setAttribute('role','alert');form.append(error);
      const actions=document.createElement('div');actions.className='cnl-study-editor-actions';
      const button=(label,type='button')=>{const b=document.createElement('button');b.type=type;b.className='folder-btn';b.textContent=label;actions.append(b);return b;};
      const cancel=button('Cancel');const download=button('Download JSON');const save=button('Import to Qbank','submit');save.classList.add('primary');
      const rows=documentName=>Array.from({length:Math.ceil(questions.length/200)},(_,index)=>({folder:folder.value.trim(),document:documentName,
        headingText:questions.length>200?'HTML import · Part '+(index+1):'HTML import',headingIndex:index,
        questions:questions.slice(index*200,index*200+200),madeAt:Date.now()}));
      download.addEventListener('click',()=>{
        const url=URL.createObjectURL(new Blob([JSON.stringify({version:1,quizzes:rows(name.value.trim()||'Imported HTML')},null,2)],{type:'application/json'}));
        const link=document.createElement('a');link.href=url;link.download=(name.value.trim()||'Qbank')+'.json';link.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
      });
      cancel.addEventListener('click',()=>dialog.close());dialog.addEventListener('close',()=>dialog.remove());
      let busy=false,completed=0,destination=null;
      dialog.addEventListener('cancel',event=>{if(busy)event.preventDefault();});
      form.addEventListener('submit',async event=>{
        event.preventDefault();if(busy)return;
        if(!folder.value.trim()||!name.value.trim()){error.textContent='Enter a subject and bank name.';return;}
        busy=true;save.disabled=cancel.disabled=download.disabled=folder.disabled=name.disabled=true;error.textContent='';
        try{
          if(!destination){
            const response=await fetch('/api/study-pack?kind=quizzes',{cache:'no-store'});
            if(!response.ok && response.status!==404)throw Error('Could not check existing banks. Try again.');
            const pack=response.ok?await response.json():{quizzes:[]};
            const fold=value=>String(value||'').toLowerCase().replace(/[^a-z0-9]+/g,'');
            const noteFold=value=>fold(String(value||'').replace(/\.docx$/i,'').replace(/^\d+[\s._-]*/,''));
            const occupied=new Set((pack.quizzes||[]).filter(row=>fold(row.folder)===fold(folder.value.trim())).map(row=>noteFold(row.document)));
            destination=name.value.trim();let suffix=2;
            while(occupied.has(noteFold(destination)))destination=name.value.trim()+' ('+(suffix++)+')';
          }
          const banks=rows(destination);
          for(;completed<banks.length;completed++){
            save.textContent='Importing '+(completed+1)+' / '+banks.length+'…';
            const response=await fetch('/api/saved-quiz',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(banks[completed])});
            if(!response.ok)throw Error('Could not save part '+(completed+1)+'. Click Import to retry the remaining parts.');
          }
          await refresh();dialog.close();
          window.alert('Imported '+questions.length+' questions into '+folder.value.trim()+' / '+destination+'. JSON saved in topic folders under data\\Qbank.');
        }catch(err){error.textContent=err.message+(completed?' '+completed+' parts already saved.':'');}
        finally{busy=false;save.disabled=cancel.disabled=download.disabled=false;
          if(!destination)folder.disabled=name.disabled=false;save.textContent='Import to Qbank';}
      });
      form.append(actions);dialog.append(form);document.body.append(dialog);dialog.showModal();
    });
    picker.click();
  };
})();
