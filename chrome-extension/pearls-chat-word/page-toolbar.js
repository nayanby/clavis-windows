/* Small on-page controls; content and native chat controls are never replaced. */
(() => {
  if (globalThis.PearlsToolbar) return;
  // Reloading an unpacked extension invalidates old listeners but can leave its
  // DOM behind. Remove those disabled controls before mounting the fresh ones.
  document.querySelectorAll('[data-pearls-toolbar]').forEach(host=>host.remove());
  const controls = new WeakMap();
  const jobs = new Map();
  let top = null, scheduled = false, overlay = false;
  const style = `:host{display:flex!important;flex-direction:column!important;align-items:flex-end!important;clear:both!important;box-sizing:border-box!important;width:100%!important;margin:10px 0 12px!important;color-scheme:light!important}
    :host([hidden]){display:none!important}
    :host([data-placement="top"]){position:fixed!important;top:96px!important;right:28px!important;z-index:2147483600!important;width:max-content!important;margin:0!important}
    :host([data-placement="response"]){position:absolute!important;width:max-content!important;margin:0!important}
    :host([data-placement="overlay"]){position:fixed!important;top:96px!important;right:28px!important;left:auto!important;width:max-content!important;max-width:calc(100vw - 24px)!important;z-index:2147483600!important;margin:0!important;padding:0!important}
    *{box-sizing:border-box}.bar{display:flex;align-items:center;gap:3px;border:1px solid #e1e5eb;border-radius:16px;background:#fffffffa;padding:6px 9px;font:12px/1.4 system-ui,-apple-system,"Segoe UI",sans-serif;color:#929292}
    :host([data-placement="overlay"]) .bar{box-shadow:0 4px 18px #171b2610}
    :host([data-placement="response"]) .bar{background:transparent;border-color:transparent;padding:2px 4px}
    .identity{display:none}button{display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;width:38px;height:38px;border:0;border-radius:9px;background:transparent;color:#9a9a9a;padding:6px;cursor:pointer}
    button:hover{background:#f2f3f6;color:#6f3d5d}button:disabled{opacity:.4;cursor:default}button:focus-visible{outline:2px solid #3b82f6;outline-offset:1px}svg{width:25px;height:28px;display:block}
    .button-label{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap}.error{color:#a22340;font:11px/1.5 system-ui;margin-top:5px;max-width:280px}
    .progress{width:230px;max-width:calc(100vw - 32px);margin-top:7px;padding:10px 12px;border:1px solid #e1e5eb;border-radius:10px;background:white;box-shadow:0 3px 12px #171b260a;font:11px/1.5 system-ui;color:#65536b;text-align:left}.progress[hidden]{display:none}.progress-label{overflow-wrap:anywhere}progress{display:block;width:100%;height:5px;margin-top:7px;border:0;border-radius:8px;overflow:hidden;accent-color:#6f3d5d}progress::-webkit-progress-bar{background:#eee9f0;border-radius:8px}progress::-webkit-progress-value{background:#6f3d5d;border-radius:8px}.progress[data-phase="complete"]{color:#237348}.progress[data-phase="complete"] progress::-webkit-progress-value{background:#34865c}.progress[data-phase="error"]{color:#a22340}
    @media(max-width:600px){:host([data-placement="overlay"]){top:76px!important;right:12px!important}}`;
  const fingerprint = text => {
    let hash = 2166136261;
    for (const char of String(text)) { hash ^= char.codePointAt(0); hash = Math.imul(hash, 16777619); }
    return (hash >>> 0).toString(16);
  };
  function visibleResponse() {
    const entries = globalThis.PearlsCapture.responseTargets();
    const choices = entries.map((entry,index)=>{
      const rect=entry.node.getBoundingClientRect();
      return {entry,index,visible:Math.max(0,Math.min(rect.bottom,innerHeight)-Math.max(rect.top,65))};
    });
    return choices.filter(choice=>choice.visible>0).sort((a,b)=>b.visible-a.visible)[0] || choices.at(-1);
  }
  function icon(button,whole=false){
    const label=document.createElement('span');label.className='button-label';label.textContent=whole?'Download entire chat':'Download response';
    button.setAttribute('aria-label',label.textContent);button.title=label.textContent;
    const ns='http://www.w3.org/2000/svg',svg=document.createElementNS(ns,'svg');svg.setAttribute('viewBox','0 0 28 30');svg.setAttribute('aria-hidden','true');
    const add=(name,attrs)=>{const node=document.createElementNS(ns,name);for(const [key,value]of Object.entries(attrs))node.setAttribute(key,value);svg.append(node);return node;};
    if(whole)add('path',{d:'M3 20V4a2 2 0 0 1 2-2h11',fill:'none',stroke:'currentColor','stroke-width':'1.8','stroke-linecap':'round'});
    add('path',{d:'M9 5h9l6 6v15a2 2 0 0 1-2 2H9a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2Z',fill:'none',stroke:'currentColor','stroke-width':'2','stroke-linejoin':'round'});
    add('path',{d:'M18 5v7h6',fill:'none',stroke:'currentColor','stroke-width':'2','stroke-linejoin':'round'});
    add('path',{d:'m10 17 2 7 3-6 3 6 2-7',fill:'none',stroke:'currentColor','stroke-width':'1.9','stroke-linecap':'round','stroke-linejoin':'round'});
    button.replaceChildren(svg,label);
  }
  function updateProgress(jobId,update){
    const control=jobs.get(jobId);if(!control)return;
    control.progress.hidden=false;
    control.progress.dataset.phase=update.phase;
    control.progressLabel.textContent=update.text || 'Preparing Word file…';
    control.progressBar.hidden=update.phase==='error';
    if(Number.isFinite(update.percent))control.progressBar.value=update.percent;
    else control.progressBar.removeAttribute('value');
    if(update.phase==='complete'||update.phase==='error'){jobs.delete(jobId);render();}
  }
  function create(whole = false) {
    const host = document.createElement('div');
    host.setAttribute('data-pearls-ignore', 'true');
    host.setAttribute('data-pearls-toolbar', whole ? 'chat' : 'response');
    host.setAttribute('data-placement', whole ? 'top' : 'response');
    const shadow = host.attachShadow({ mode: 'open' });
    const css = document.createElement('style'); css.textContent = style;
    const bar = document.createElement('div'); bar.className = 'bar';
    const label = document.createElement('div'); label.className = 'identity';
    const brand = document.createElement('span'); brand.className = 'brand'; brand.textContent = 'Pearls · Word';
    const hint = document.createElement('span'); hint.className = 'hint'; hint.textContent = 'Clinical Notes template';
    label.append(brand, hint);
    const button = document.createElement('button'); button.type = 'button'; button.textContent = whole ? 'Download entire chat' : 'Download response';
    icon(button,whole);
    const responseButton = whole ? document.createElement('button') : null;
    if(responseButton){responseButton.type='button';icon(responseButton);bar.append(label,responseButton,button);}
    else bar.append(label,button);
    const error = document.createElement('div'); error.className = 'error'; error.setAttribute('role','status');
    const progress=document.createElement('div');progress.className='progress';progress.hidden=true;progress.setAttribute('role','status');progress.setAttribute('aria-live','polite');
    const progressLabel=document.createElement('div');progressLabel.className='progress-label';
    const progressBar=document.createElement('progress');progressBar.max=100;progressBar.setAttribute('aria-label','Word export progress');
    progress.append(progressLabel,progressBar);
    shadow.append(css, bar, progress, error);
    const control = { host, button, responseButton, error, progress, progressLabel, progressBar, index: 0, entry: null };
    async function send(event,isWhole,clicked) {
      if (!event.isTrusted) return;
      if(jobs.size)return;
      error.textContent = ''; clicked.disabled = true;
      const jobId=crypto.randomUUID();jobs.set(jobId,control);
      updateProgress(jobId,{phase:'preparing',text:'Preparing Word download…'});render();
      try {
        const target = whole && !isWhole ? visibleResponse() : {entry:control.entry,index:control.index};
        if(!isWhole&&!target?.entry)throw Error('No completed response is available yet.');
        const preview = isWhole ? '' : (target.entry.root.innerText?.trim().slice(0,240) || target.entry.root.textContent.trim().slice(0,240));
        const reply = await chrome.runtime.sendMessage({ type: 'PEARLS_OPEN_EXPORT', jobId, mode: isWhole ? 'all' : 'single', index: target?.index||0, id: target?.entry?.id || null, fingerprint: fingerprint(preview) });
        if (reply?.error) throw Error(reply.error);
      } catch (cause) { updateProgress(jobId,{phase:'error',text:cause.message || 'Reload this chat after updating the extension.'}); }
    }
    button.addEventListener('click',event=>send(event,whole,button));
    if(responseButton)responseButton.addEventListener('click',event=>send(event,false,responseButton));
    return control;
  }
  function render() {
    scheduled = false;
    const reader = globalThis.PearlsCapture;
    if (!reader) return;
    let entries;
    try { entries = reader.responseTargets(); } catch { return; }
    if (!entries.length && !overlay) { if (top) top.host.hidden = true; return; }
    if (!top?.host.isConnected) {
      top = create(true);
      document.body.append(top.host);
    }
    top.host.hidden = false;
    const destination=document.body;
    if(top.host.parentElement!==destination)destination.prepend(top.host);
    if(top.host.getAttribute('data-placement')!==(overlay?'overlay':'top'))top.host.setAttribute('data-placement',overlay?'overlay':'top');
    for(const [key,value]of Object.entries({position:'fixed',top:'96px',right:'28px',width:'max-content','z-index':'2147483600'}))top.host.style.setProperty(key,value,'important');
    const streaming = reader.isGenerating();
    top.button.disabled = streaming || !entries.length || jobs.size>0;
    top.responseButton.disabled = streaming || !entries.length || jobs.size>0;
    if(!entries.length&&!jobs.size){
      top.emptyHint=true;top.progress.hidden=false;top.progress.dataset.phase='preparing';top.progressLabel.textContent='No responses found. Open a conversation or refresh the chat.';top.progressBar.hidden=true;
    }else if(top.emptyHint){top.emptyHint=false;top.progress.hidden=true;top.progressBar.hidden=false;}
    entries.forEach((entry,index) => {
      let control = controls.get(entry.node);
      if (!control?.host.isConnected) { control = create(); document.body.append(control.host); controls.set(entry.node, control); }
      const rect=entry.node.getBoundingClientRect();
      for(const [key,value]of Object.entries({position:'absolute',top:(rect.bottom+scrollY)+'px',left:'auto',right:Math.max(8,innerWidth-rect.right-scrollX)+'px',width:'max-content',margin:'0','z-index':'100'}))control.host.style.setProperty(key,value,'important');
      control.index = index; control.entry = entry;
      control.button.disabled = streaming || jobs.size>0;
    });
  }
  function schedule() { if (!scheduled) { scheduled = true; setTimeout(render, 300); } }
  const observer = new MutationObserver(schedule);
  document.addEventListener('scroll',schedule,{passive:true,capture:true});
  observer.observe(document.documentElement, { childList: true, subtree: true, attributes: true, attributeFilter: ['data-is-streaming','aria-busy'] });
  function toggleOverlay(){overlay=!overlay;render();if(overlay)top?.responseButton.focus({preventScroll:true});}
  globalThis.chrome?.runtime?.onMessage?.addListener(message=>{
    if(message?.type==='PEARLS_EXPORT_PROGRESS')updateProgress(message.jobId,message);
  });
  globalThis.PearlsToolbar = { render, fingerprint, toggleOverlay, updateProgress };
  render();
})();
