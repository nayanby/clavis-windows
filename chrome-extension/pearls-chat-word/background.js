async function openExporter(tab, request = {}) {
  if (!tab.id) return;
  const url = new URL(chrome.runtime.getURL('exporter.html'));
  url.searchParams.set('tab', String(tab.id));
  if (request.mode === 'all' || request.mode === 'single') url.searchParams.set('mode', request.mode);
  if (request.jobId) url.searchParams.set('job', String(request.jobId).slice(0,100));
  if (request.mode === 'single') {
    url.searchParams.set('index', String(Math.max(0, Number(request.index) || 0)));
    if (request.id) url.searchParams.set('responseId', String(request.id).slice(0, 300));
    if (request.fingerprint) url.searchParams.set('fingerprint', String(request.fingerprint));
  }
  await chrome.tabs.create({ url: url.href, active: false });
}
chrome.action.onClicked.addListener(async tab => {
  try {
    if (!['chatgpt.com','chat.openai.com','claude.ai','gemini.google.com'].includes(new URL(tab.url).hostname)) throw Error('Open a ChatGPT, Claude or Gemini conversation.');
    await chrome.scripting.executeScript({target:{tabId:tab.id},files:['capture.js','page-toolbar.js']});
    await chrome.scripting.executeScript({target:{tabId:tab.id},func:()=>globalThis.PearlsToolbar.toggleOverlay()});
    await chrome.action.setBadgeText({tabId:tab.id,text:''});
    await chrome.action.setTitle({tabId:tab.id,title:'Show Word download toolbar'});
  } catch(error) {
    await chrome.action.setBadgeText({tabId:tab.id,text:'!'});
    await chrome.action.setTitle({tabId:tab.id,title:error.message});
  }
});
chrome.runtime.onMessage.addListener((request, sender, reply) => {
  if (request?.type === 'PEARLS_EXPORT_PROGRESS') {
    try {
      const source = new URL(sender.url);
      const own = new URL(chrome.runtime.getURL('exporter.html'));
      if (source.protocol !== own.protocol || source.host !== own.host || source.pathname !== own.pathname) return;
      if (!request.jobId || source.searchParams.get('job') !== request.jobId) return;
      const tabId = Number(source.searchParams.get('tab'));
      if (!Number.isInteger(tabId) || tabId <= 0) return;
      const phase = ['preparing','collecting','formatting','packaging','saving','complete','error'].includes(request.phase) ? request.phase : 'preparing';
      chrome.tabs.sendMessage(tabId, {type:'PEARLS_EXPORT_PROGRESS',jobId:request.jobId,phase,text:String(request.text||'').slice(0,300),percent:Number.isFinite(request.percent)?Math.max(0,Math.min(100,request.percent)):null})
        .then(()=>{
          reply({ok:true});
          if(phase==='complete'&&sender.tab?.id)chrome.tabs.remove?.(sender.tab.id).catch(()=>{});
        },()=>reply({ok:false}));
      return true;
    } catch { return; }
  }
  if (request?.type !== 'PEARLS_OPEN_EXPORT') return;
  const host = (() => { try { return new URL(sender.url).hostname; } catch { return ''; } })();
  if (!sender.tab || !['chatgpt.com','chat.openai.com','claude.ai','gemini.google.com'].includes(host)) return;
  openExporter(sender.tab, request).then(() => reply({ ok: true }), error => reply({ error: error.message }));
  return true;
});
