/* Small on-page controls; content and native chat controls are never replaced. */
(() => {
  if (globalThis.PearlsToolbar) return;
  const controls = new WeakMap();
  let top = null, scheduled = false, overlay = false;
  const style = `:host{display:block!important;clear:both!important;box-sizing:border-box!important;margin:12px 0 18px!important;color-scheme:light!important}
    :host([hidden]){display:none!important}:host([data-placement="top"]){position:sticky!important;top:0!important;z-index:100!important;margin:0 0 14px!important;padding-top:8px!important}
    :host([data-placement="overlay"]){position:fixed!important;top:14px!important;left:50%!important;transform:translateX(-50%)!important;width:max-content!important;max-width:calc(100vw - 24px)!important;z-index:2147483600!important;margin:0!important;padding:0!important}
    :host([data-placement="overlay"]) .identity{display:none}:host([data-placement="overlay"]) .bar{gap:8px;padding:8px;box-shadow:0 8px 35px #2c163236}:host([data-placement="overlay"]) button{padding:11px 15px}
    *{box-sizing:border-box}.bar{display:flex;align-items:center;justify-content:space-between;gap:16px;border:1px solid #ded4df;border-radius:10px;background:#faf7fa;padding:9px 12px;font:12px/1.4 system-ui,-apple-system,"Segoe UI",sans-serif;color:#654f65}
    .brand{font-weight:700;letter-spacing:.035em}.hint{margin-left:8px;color:#807580;font-size:11px}button{display:inline-flex;align-items:center;gap:7px;flex-shrink:0;border:0;border-radius:7px;background:#6f3d5d;color:white;padding:9px 12px;font:600 12px/1.2 system-ui;cursor:pointer}button:hover{background:#57304a}button:disabled{opacity:.5;cursor:default}button:focus-visible{outline:3px solid #93b9de;outline-offset:2px}.error{color:#a22340;font-size:11px;margin-top:5px}@media(max-width:600px){.hint{display:none}.bar{gap:8px;padding:8px}.brand{font-size:11px}:host([data-placement="top"]) .identity{display:none}:host([data-placement="overlay"]) button{padding:9px 10px;font-size:11px}}`;
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
    const responseButton = whole ? document.createElement('button') : null;
    if(responseButton){responseButton.type='button';responseButton.textContent='Download response';responseButton.title='Download the response currently in view';bar.append(label,responseButton,button);}
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
