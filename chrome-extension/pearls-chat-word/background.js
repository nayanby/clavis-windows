async function openExporter(tab, request = {}) {
  if (!tab.id) return;
  const url = new URL(chrome.runtime.getURL('exporter.html'));
  url.searchParams.set('tab', String(tab.id));
  if (request.mode === 'all' || request.mode === 'single') url.searchParams.set('mode', request.mode);
  if (request.mode === 'single') {
    url.searchParams.set('index', String(Math.max(0, Number(request.index) || 0)));
    if (request.id) url.searchParams.set('responseId', String(request.id).slice(0, 300));
    if (request.fingerprint) url.searchParams.set('fingerprint', String(request.fingerprint));
  }
  await chrome.tabs.create({ url: url.href });
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
  if (request?.type !== 'PEARLS_OPEN_EXPORT') return;
  const host = (() => { try { return new URL(sender.url).hostname; } catch { return ''; } })();
  if (!sender.tab || !['chatgpt.com','chat.openai.com','claude.ai','gemini.google.com'].includes(host)) return;
  openExporter(sender.tab, request).then(() => reply({ ok: true }), error => reply({ error: error.message }));
  return true;
});
