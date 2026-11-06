/* Saved Qbank attempts: original order, explicit persistence, independent bookmarks. */
(() => {
 'use strict';
 const Q=window.cnlQbank={banks:{},active:null};let queue=Promise.resolve();
 const el=(tag,text,cls)=>{const node=document.createElement(tag);if(text!=null)node.textContent=text;if(cls)node.className=cls;return node;};
 const button=(host,label,run,primary=false)=>{const b=el('button',label,'folder-btn'+(primary?' primary':''));b.type='button';b.onclick=run;host.append(b);return b;};
 const error=message=>window.cnlToast?.(message)||console.warn(message);
 Q.key=row=>JSON.stringify([row.folder||'',row.document||'',row.headingText||'']);
 Q.questionKey=(row,index)=>String(row.questions[index]?.id||row.questions[index]?.sourceId||'index:'+index);
 Q.signature=row=>{let hash=2166136261;const value=JSON.stringify((row.questions||[]).map(q=>[q.question,q.options,q.correctIndex,q.answerReviewRequired]));for(let i=0;i<value.length;i++){hash^=value.charCodeAt(i);hash=Math.imul(hash,16777619);}return 'v1:'+row.questions.length+':'+(hash>>>0).toString(16);};
 Q.entry=row=>Q.banks[Q.key(row)]||{bookmarks:[],attempt:null};
 Q.attempt=row=>{const attempt=Q.entry(row).attempt;return attempt?.signature===Q.signature(row)?attempt:null;};
 Q.marked=row=>{const marks=new Set(Q.entry(row).bookmarks||[]);return row.questions.map((_,i)=>i).filter(i=>marks.has(Q.questionKey(row,i)));};
 Q.load=async()=>{await queue;const response=await fetch('/api/qbank-progress',{cache:'no-store'});if(!response.ok)throw Error('Could not load Qbank progress. Try again.');const data=await response.json();Q.banks=data.banks||{};return data;};
 Q.send=(row,payload)=>{
   const work=queue.then(async()=>{const response=await fetch('/api/qbank-progress',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({bank:Q.key(row),...payload})});
     const data=await response.json();if(!response.ok)throw Error(data.error||'Could not save Qbank progress.');Q.banks[Q.key(row)]=data.entry;return data;});
   queue=work.catch(()=>{});return work;
 };
 Q.confirmRetry=(row,after)=>{
   const dialog=el('dialog',null,'cnl-study-editor');dialog.setAttribute('aria-label','Retry Qbank');
   dialog.append(el('h2','Retry Qbank'),el('p','Reset this bank’s answers, paused progress and result? Your bookmarks will be kept.'));
   const actions=el('div',null,'cnl-study-editor-actions');button(actions,'Cancel',()=>dialog.close());
   const retry=button(actions,'Retry',async()=>{retry.disabled=true;try{await Q.send(row,{op:'retry'});dialog.close();after?.();}catch(e){error(e.message);retry.disabled=false;}},true);
   dialog.append(actions);dialog.onclose=()=>dialog.remove();document.body.append(dialog);dialog.showModal();
 };
 Q.decorate=(tile,row,open,refresh)=>{
   tile.dataset.qbankTile=Q.key(row);const attempt=Q.attempt(row);
   if(attempt){
     const status=el('p',attempt.status==='submitted'?`Result: ${attempt.score} / ${attempt.total}${attempt.total?' · '+Math.round(100*attempt.score/attempt.total)+'%':''}`:`Paused · ${attempt.answers.filter(a=>a!==null).length} / ${row.questions.length} answered`,'cnl-qbank-status');tile.append(status);
     if(attempt.status==='submitted')button(tile,'Review',event=>{event.stopPropagation();open({review:true});}).classList.add('cnl-qbank-review-button');
   }
   tile.tabIndex=0;tile.setAttribute('role','button');tile.setAttribute('aria-description','Open Qbank. Long press or right click to retry.');
   let timer=null,suppress=0,start=null;
   const cancel=()=>{clearTimeout(timer);timer=null;};
   const retry=()=>{cancel();suppress=Date.now()+1500;Q.confirmRetry(row,refresh);};
   tile.addEventListener('pointerdown',event=>{if(event.button!==0||event.target.closest('button'))return;start=[event.clientX,event.clientY];timer=setTimeout(retry,650);});
   tile.addEventListener('pointermove',event=>{if(start&&Math.hypot(event.clientX-start[0],event.clientY-start[1])>10)cancel();});
   for(const name of ['pointerup','pointercancel','pointerleave'])tile.addEventListener(name,cancel);
   tile.addEventListener('contextmenu',event=>{event.preventDefault();retry();});
   tile.addEventListener('click',event=>{if(Date.now()<suppress){event.preventDefault();event.stopImmediatePropagation();return;}if(event.target.closest('button'))return;open({review:attempt?.status==='submitted'});});
   tile.addEventListener('keydown',event=>{if(event.target!==tile)return;if(event.key==='Enter'||event.key===' '){event.preventDefault();open({review:attempt?.status==='submitted'});}if(event.key==='ContextMenu'||(event.shiftKey&&event.key==='F10')){event.preventDefault();retry();}});
 };
 const gradable=q=>!q.answerReviewRequired&&Number.isInteger(q.correctIndex)&&q.correctIndex>=0&&q.correctIndex<(q.options||[]).length;
 function markButton(host,row,index){
   const b=button(host,'',async()=>{b.disabled=true;try{const marked=!(Q.entry(row).bookmarks||[]).includes(Q.questionKey(row,index));await Q.send(row,{op:'bookmark',question:Q.questionKey(row,index),marked});paint();}catch(e){error(e.message);}finally{b.disabled=false;}});
   const paint=()=>{const marked=(Q.entry(row).bookmarks||[]).includes(Q.questionKey(row,index));b.textContent=marked?'★ Bookmarked':'☆ Bookmark';b.setAttribute('aria-pressed',String(marked));};paint();return b;
 }
 Q.leave=callback=>{
   const session=Q.active;if(!session||session.review||!session.dirty){Q.active=null;callback();return;}
   const dialog=el('dialog',null,'cnl-study-editor');dialog.setAttribute('aria-label','Leave Qbank');
   dialog.append(el('h2','Leave Qbank'),el('p','Pause to save your answers and position, or exit without saving changes to this attempt. Bookmarks are kept.'));
   const actions=el('div',null,'cnl-study-editor-actions');button(actions,'Continue solving',()=>dialog.close());
   button(actions,'Exit without saving',()=>{Q.active=null;dialog.close();callback();});
   const pause=button(actions,'Pause and save',async()=>{pause.disabled=true;try{await session.save('paused');Q.active=null;dialog.close();callback();}catch(e){error(e.message);pause.disabled=false;}},true);
   dialog.append(actions);dialog.onclose=()=>dialog.remove();document.body.append(dialog);dialog.showModal();
 };
 document.addEventListener('click',event=>{
   if(!Q.active||event.defaultPrevented)return;
   const target=event.target.closest?.('#cnlTabBar .cnl-tab,.cnl-drawer-row,#headerBackBtn,#headerHomeBtn,#cnlQuizPage .cnl-study-mount > .folder-btn');
   if(!target)return;
   if(Q.active.saving){event.preventDefault();event.stopImmediatePropagation();error('Saving Qbank progress…');return;}
   if(Q.active.review||!Q.active.dirty){Q.active=null;return;}
   event.preventDefault();event.stopImmediatePropagation();Q.leave(()=>target.click());
 },true);
 window.addEventListener('beforeunload',event=>{if(Q.active?.dirty){event.preventDefault();event.returnValue='';}});
 window.cnlRenderSavedQbank=async(row,options={})=>{
   const area=document.getElementById('aiResultArea');if(!area)return;
   const attempt=Q.attempt(row),questions=row.questions,signature=Q.signature(row);
   const session={row,review:!!options.review||attempt?.status==='submitted',dirty:false,
     answers:attempt?[...attempt.answers]:questions.map(()=>null),index:attempt?.index||0,
     id:attempt?.id||crypto.randomUUID(),signature};
   Q.active=session;
   const wrap=el('div',null,'ai-quiz cnl-qbank-session');area.replaceChildren(wrap);
   const exit=()=>{Q.active=null;options.onExit?.();};
   const result=()=>({score:questions.reduce((sum,q,i)=>sum+(gradable(q)&&session.answers[i]===q.correctIndex?1:0),0),total:questions.filter(gradable).length});
   session.save=async status=>{if(session.saving)throw Error('Saving Qbank progress…');session.saving=true;wrap.inert=true;const stats=result();let saved;
     try{saved=await Q.send(row,{op:'attempt',attempt:{id:session.id,signature:session.signature,answers:[...session.answers],index:session.index,status,...stats}});session.dirty=false;}
     finally{session.saving=false;wrap.inert=false;}
     if(status==='submitted'&&saved.newSubmission&&stats.total)fetch('/api/study-attempt',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({correct:stats.score,total:stats.total,label:[row.folder,row.document,row.headingText].join(' · ')})}).catch(()=>{});
     return saved;
   };
   function renderQuestionCard(index,review){
     const q=questions[index],chosen=session.answers[index],card=el('section',null,review?'cnl-qbank-review-card':'cnl-qbank-question-card');
     const tools=el('div',null,'cnl-qbank-tools');tools.append(el('span','Question '+(index+1)+' of '+questions.length));markButton(tools,row,index);card.append(tools);
     card.append(el('div',q.question,'ai-quiz-question'));
     if(review)card.append(el('p',chosen===null?'Your answer: Not answered':chosen===-1?'Reviewed as recall':'Your answer: '+String.fromCharCode(65+chosen)+'. '+q.options[chosen],'cnl-qbank-your-answer'));
     const opts=el('div',null,'ai-quiz-options');
     (q.options||[]).forEach((text,i)=>{const b=el('button',String.fromCharCode(65+i)+'. '+text,'ai-quiz-opt');b.type='button';b.dataset.optionIndex=String(i);b.disabled=review||chosen!==null||!gradable(q);
       if(chosen!==null||review){if(gradable(q)&&i===q.correctIndex)b.classList.add('correct');else if(i===chosen)b.classList.add('incorrect');if(i===chosen)b.dataset.candidateAnswer='true';}
       b.onclick=()=>{if(session.answers[index]!==null)return;session.answers[index]=i;session.dirty=true;render();};opts.append(b);});card.append(opts);
     if(review||chosen!==null){const explanation=el('div',null,'ai-quiz-explain');window.cnlRenderQbankExplanation(explanation,q,gradable(q));card.append(explanation);}
     if(!review&&!gradable(q)&&chosen===null)button(card,'Show answer and mark reviewed',()=>{session.answers[index]=-1;session.dirty=true;render();});
     if(!review)window.cnlAddSavedQuizEditor?.(card,q,row,index,()=>{session.signature=Q.signature(row);session.answers[index]=null;session.id=crypto.randomUUID();session.dirty=true;render();});
     return card;
   }
   function review(){
     wrap.replaceChildren();const toolbar=el('div',null,'cnl-qbank-tools');button(toolbar,options.bookmarksOnly?'Back to bookmarks':'Back to Qbank',exit);wrap.append(toolbar);
     const stored=Q.attempt(row);
     if(stored?.status==='submitted'&&!options.bookmarksOnly)wrap.append(el('h2',`Result: ${stored.score} / ${stored.total}`));
     (options.questionIndices||questions.map((_,i)=>i)).forEach(i=>wrap.append(renderQuestionCard(i,true)));
     requestAnimationFrame(()=>wrap.scrollIntoView({block:'start',behavior:'instant'}));
   }
   function final(){
     wrap.replaceChildren();session.review=true;const stats=result();wrap.append(el('h2',`Result: ${stats.score} / ${stats.total}`,'ai-quiz-final-score'));
     wrap.append(el('p',stats.total?Math.round(100*stats.score/stats.total)+'% correct':'Recall review complete'));
     button(wrap,'Review answers',review,true);button(wrap,'Back to Qbank',exit);
     requestAnimationFrame(()=>wrap.scrollIntoView({block:'start',behavior:'instant'}));
   }
   function render(){
     wrap.replaceChildren();const actions=el('div',null,'cnl-qbank-tools');
     const pause=button(actions,'Pause',async()=>{pause.disabled=true;try{await session.save('paused');exit();}catch(e){error(e.message);pause.disabled=false;}});
     button(actions,'Exit without saving',()=>{if(!session.saving)exit();});wrap.append(actions,renderQuestionCard(session.index,false));
     const nav=el('div',null,'ai-quiz-nav');const previous=button(nav,'Previous',()=>{session.index--;session.dirty=true;render();});previous.disabled=session.index===0;
     if(session.index<questions.length-1){const next=button(nav,'Next',()=>{session.index++;session.dirty=true;render();},true);next.disabled=session.answers[session.index]===null;}
     else{const submit=button(nav,'Submit',async()=>{submit.disabled=true;try{await session.save('submitted');final();}catch(e){error(e.message);submit.disabled=false;}},true);submit.disabled=session.answers.some(answer=>answer===null);}
     wrap.append(nav);
     requestAnimationFrame(()=>wrap.scrollIntoView({block:'start',behavior:'instant'}));
   }
   if(session.review)review();else render();
 };
 const style=el('style');style.textContent=`
 .cnl-qbank-tools{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:14px}.cnl-qbank-tools>span{flex:1}
 .cnl-qbank-status{font:600 14px/1.4 system-ui,sans-serif;color:#365c80;margin:8px 0}
 body #cnlQuizPage [data-qbank-tile]>.cnl-qbank-status{grid-column:2;grid-row:2!important;margin:0!important;padding:3px 0!important;border:0;background:transparent;font:600 14px/1.4 system-ui,sans-serif!important;text-transform:none!important}
 body #cnlQuizPage [data-qbank-tile]>.cnl-qbank-review-button{grid-column:2;grid-row:3!important;justify-self:start;width:auto!important;min-width:90px!important;max-width:100%;padding:7px 14px!important;margin:4px 0 0!important;display:inline-flex;justify-content:center;font:600 13px/1.4 system-ui,sans-serif;text-transform:none}
 .cnl-qbank-session{scroll-margin-top:70px}
 .cnl-qbank-review-card{padding:20px;border:1px solid #d6def1;border-radius:14px;background:#fff;margin:16px 0}
 .cnl-qbank-your-answer{font-weight:700}.cnl-qbank-session .ai-quiz-explain{display:block!important;max-height:none!important;overflow:visible!important}
 .cnl-qbank-session .ai-quiz-opt[data-candidate-answer]{box-shadow:inset 0 0 0 2px #775374}
 article.cnl-study-row{cursor:pointer;text-align:left}.cnl-qbank-session [disabled]{cursor:default}
 `;document.head.append(style);
})();
