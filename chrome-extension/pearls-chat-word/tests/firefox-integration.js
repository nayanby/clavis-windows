const fixture=arguments[0],done=arguments[arguments.length-1];
(async()=>{
  const tab=(await browser.tabs.query({})).find(tab=>tab.url?.startsWith('https://chatgpt.com:'));
  if(!tab)throw Error('No local fixture tab');
  await browser.tabs.update(tab.id,{active:true});
  await browser.scripting.executeScript({target:{tabId:tab.id},args:[fixture],func:html=>{window.stop();document.documentElement.innerHTML=html;}});
  await browser.scripting.executeScript({target:{tabId:tab.id},files:['vendor/html2canvas.min.js','capture.js']});
  const captured=await browser.scripting.executeScript({target:{tabId:tab.id},func:async()=>{
    const message=document.querySelector('[data-message-author-role="assistant"]');
    const chart=document.createElement('div');chart.setAttribute('data-diagram','');chart.setAttribute('aria-label','Complete inheritance chart');
    chart.style.cssText='width:600px;height:260px;background:#eef7ef;padding:20px;box-sizing:border-box';
    chart.innerHTML='<div style="display:grid;grid-template-columns:repeat(3,1fr);text-align:center"><div>AA</div><div>Aa</div><div>aa</div></div><div style="display:flex;justify-content:space-around;margin-top:130px"><span>25% noncarrier</span><span>50% carrier</span><span>25% affected</span></div>';
    message.append(chart);
    const tall=chart.cloneNode(true);tall.style.height='1100px';tall.setAttribute('aria-label','Tall complete chart');message.append(tall);
    const svg=document.createElementNS('http://www.w3.org/2000/svg','svg');svg.setAttribute('width','300');svg.setAttribute('height','120');svg.setAttribute('aria-label','SVG inheritance diagram');
    svg.innerHTML='<rect width="300" height="120" fill="#e3f1ec"/><text x="20" y="60" font-size="24">Aa × Aa</text>';message.append(svg);
    return await PearlsCapture.resolveImages(PearlsCapture.snapshot());
  }});
  if(captured[0]?.error)throw Error(captured[0].error.message);
  const data=captured[0].result;
  const images=data.messages.flatMap(message=>message.blocks).filter(block=>block.type==='image');
  const [template,profile]=await Promise.all([
    fetch(browser.runtime.getURL('template/base.docx')).then(response=>response.arrayBuffer()),
    fetch(browser.runtime.getURL('template/profile.json')).then(response=>response.json())
  ]);
  const document=await PearlsWord.create(data,{single:true,title:'Firefox Real Capture Verification',templateBytes:template,profile});
  let binary='';for(let i=0;i<document.bytes.length;i+=32768)binary+=String.fromCharCode(...document.bytes.subarray(i,i+32768));
  return {warnings:data.warnings,images:images.map(image=>({alt:image.alt,data:!!image.data,error:image.captureError,width:image.width,height:image.height,png:image.data})),docx:btoa(binary)};
})().then(done,error=>done({error:error.message}));
