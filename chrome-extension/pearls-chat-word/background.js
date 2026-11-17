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
    await chrome.scripting.executeScript({target:{tabId:tab.id},files:['vendor/html2canvas.min.js','capture.js','page-toolbar.js']});
    await chrome.scripting.executeScript({target:{tabId:tab.id},func:()=>globalThis.PearlsToolbar.toggleOverlay()});
    await chrome.action.setBadgeText({tabId:tab.id,text:''});
    await chrome.action.setTitle({tabId:tab.id,title:'Show Word download toolbar'});
  } catch(error) {
    await chrome.action.setBadgeText({tabId:tab.id,text:'!'});
    await chrome.action.setTitle({tabId:tab.id,title:error.message});
  }
});
chrome.runtime.onMessage.addListener((request, sender, reply) => {
  if(request?.type==='PEARLS_CROP_VISUAL'){
    (async()=>{
      const source=new URL(sender.url);
      if(!sender.tab?.id||!['chatgpt.com','chat.openai.com','claude.ai','gemini.google.com'].includes(source.hostname)||source.protocol!=='https:')throw Error('Unsupported capture source.');
      if(!chrome.runtime.getBrowserInfo)throw Error('Native crop is available in Firefox only.');
      const r=request.rect;
      if(!r||!['x','y','width','height'].every(key=>Number.isFinite(r[key]))||r.x<0||r.y<0||r.width<1||r.height<1||r.width>8000||r.height>8000||r.width*r.height>16000000)throw Error('Invalid crop bounds.');
      const tab=await chrome.tabs.get(sender.tab.id);
      if(!tab.active||tab.url!==sender.url)throw Error('Keep the source chat active while exporting diagrams.');
      const data=await chrome.tabs.captureVisibleTab(tab.windowId,{format:'png'});
      const after=await chrome.tabs.get(sender.tab.id);
      if(!after.active||after.url!==sender.url)throw Error('The source tab changed during capture.');
      reply({data});
    })().catch(error=>reply({error:error.message}));
    return true;
  }
  if (request?.type === 'PEARLS_FETCH_IMAGE') {
    try {
      const source = new URL(sender.url), url = new URL(request.url);
      if (!sender.tab || !['chatgpt.com','chat.openai.com','claude.ai','gemini.google.com'].includes(source.hostname)) return;
      const allowed = ['chatgpt.com','chat.openai.com','images.openai.com','claude.ai','gemini.google.com','oaiusercontent.com','googleusercontent.com'];
      if (url.protocol !== 'https:' || url.port || !allowed.some(host=>url.hostname===host||url.hostname.endsWith('.'+host))) return reply({error:'Image host is not supported.'});
      (async()=>{
        const response=await fetch(url.href,{credentials:'omit',redirect:'error',signal:AbortSignal.timeout(15000)});
        if(!response.ok || !/^image\/(png|jpeg|gif|webp|svg\+xml)(;|$)/i.test(response.headers.get('content-type')||'')) throw Error('Image unavailable or unsupported.');
        if(Number(response.headers.get('content-length'))>8000000) throw Error('Image exceeds 8 MB.');
        const reader=response.body.getReader();const chunks=[];let length=0;
        try { while(true){const {done,value}=await reader.read();if(done)break;length+=value.length;if(length>8000000)throw Error('Image exceeds 8 MB.');chunks.push(value);} } finally {await reader.cancel();}
        const bytes=new Uint8Array(length);let offset=0;for(const chunk of chunks){bytes.set(chunk,offset);offset+=chunk.length;}
        let binary='';for(let i=0;i<bytes.length;i+=32768)binary+=String.fromCharCode(...bytes.subarray(i,i+32768));
        reply({data:'data:'+response.headers.get('content-type').split(';')[0]+';base64,'+btoa(binary)});
      })().catch(error=>reply({error:error.message}));
      return true;
    } catch { reply({error:'Invalid image request.'});return; }
  }
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
