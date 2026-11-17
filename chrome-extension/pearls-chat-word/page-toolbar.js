/* Small on-page controls; content and native chat controls are never replaced. */
(() => {
  if (globalThis.PearlsToolbar) return;
  const controls = new WeakMap();
  let top = null, scheduled = false, overlay = false;
  const style = `:host{display:flex!important;flex-direction:column!important;align-items:flex-end!important;clear:both!important;box-sizing:border-box!important;width:100%!important;margin:10px 0 12px!important;color-scheme:light!important}
    :host([hidden]){display:none!important}
    :host([data-placement="top"]){position:sticky!important;top:8px!important;z-index:100!important;margin:0 0 12px!important;padding-top:8px!important}
    :host([data-placement="overlay"]){position:fixed!important;top:96px!important;right:28px!important;left:auto!important;width:max-content!important;max-width:calc(100vw - 24px)!important;z-index:2147483600!important;margin:0!important;padding:0!important}
    *{box-sizing:border-box}.bar{display:flex;align-items:center;gap:3px;border:1px solid #e1e5eb;border-radius:16px;background:#fffffffa;padding:6px 9px;font:12px/1.4 system-ui,-apple-system,"Segoe UI",sans-serif;color:#929292}
    :host([data-placement="overlay"]) .bar{box-shadow:0 4px 18px #171b2610}
    :host([data-placement="response"]) .bar{background:transparent;border-color:transparent;padding:2px 4px}
    .identity{display:none}button{display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;width:38px;height:38px;border:0;border-radius:9px;background:transparent;color:#9a9a9a;padding:6px;cursor:pointer}
    button:hover{background:#f2f3f6;color:#6f3d5d}button:disabled{opacity:.4;cursor:default}button:focus-visible{outline:2px solid #3b82f6;outline-offset:1px}svg{width:25px;height:28px;display:block}
    .button-label{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap}.error{color:#a22340;font:11px/1.5 system-ui;margin-top:5px;max-width:280px}
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
    shadow.append(css, bar, error);
    const control = { host, button, responseButton, error, index: 0, entry: null };
    async function send(event,isWhole,clicked) {
      if (!event.isTrusted) return;
      error.textContent = ''; clicked.disabled = true;
      try {
        const target = whole && !isWhole ? visibleResponse() : {entry:control.entry,index:control.index};
        if(!isWhole&&!target?.entry)throw Error('No completed response is available yet.');
        const preview = isWhole ? '' : (target.entry.root.innerText?.trim().slice(0,240) || target.entry.root.textContent.trim().slice(0,240));
        const reply = await chrome.runtime.sendMessage({ type: 'PEARLS_OPEN_EXPORT', mode: isWhole ? 'all' : 'single', index: target?.index||0, id: target?.entry?.id || null, fingerprint: fingerprint(preview) });
        if (reply?.error) throw Error(reply.error);
      } catch (cause) { error.textContent = cause.message || 'Reload this chat after updating the extension.'; }
      finally { clicked.disabled = false; }
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
      const main = document.querySelector('main,[role="main"]') || entries[0]?.node.parentElement || document.body;
      main.prepend(top.host);
    }
    top.host.hidden = false;
    if(top.host.getAttribute('data-placement')!==(overlay?'overlay':'top'))top.host.setAttribute('data-placement',overlay?'overlay':'top');
    const streaming = reader.isGenerating();
    top.button.disabled = streaming || !entries.length;
    top.responseButton.disabled = streaming || !entries.length;
    entries.forEach((entry,index) => {
      let control = controls.get(entry.node);
      if (!control?.host.isConnected) { control = create(); entry.node.append(control.host); controls.set(entry.node, control); }
      control.index = index; control.entry = entry;
      control.button.disabled = streaming;
    });
  }
  function schedule() { if (!scheduled) { scheduled = true; setTimeout(render, 300); } }
  const observer = new MutationObserver(schedule);
  observer.observe(document.documentElement, { childList: true, subtree: true, attributes: true, attributeFilter: ['data-is-streaming','aria-busy'] });
  function toggleOverlay(){overlay=!overlay;render();if(overlay)top?.responseButton.focus({preventScroll:true});}
  globalThis.PearlsToolbar = { render, fingerprint, toggleOverlay };
  render();
})();
