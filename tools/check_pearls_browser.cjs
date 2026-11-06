/* Exercise the real packaged app in a throwaway headless browser and data folder. */
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {spawn}=require('node:child_process');
const root=path.resolve(__dirname,'..'),work=path.join(root,'build','pearls-browser-qa');
const packageRoot=path.join(root,'dist','Clinical Notes Library');
const data=path.join(work,'data'),port=8976,debugPort=9227;
fs.mkdirSync(data,{recursive:true});
fs.cpSync(path.join(root,'build','pearls-word'),path.join(data,'Pearls'),{recursive:true,filter:p=>!p.endsWith('.json')});
const app=spawn(path.join(packageRoot,'Clinical Notes Library.exe'),['--server-only','--port',String(port),'--data-dir',data],{cwd:packageRoot,windowsHide:true,stdio:'ignore'});
let chrome,ws;
const pause=ms=>new Promise(r=>setTimeout(r,ms));
async function until(run,label){for(let i=0;i<160;i++){try{const value=await run();if(value)return value;}catch{}await pause(150);}throw Error('Timed out: '+label);}
(async()=>{
 await until(async()=> (await fetch(`http://127.0.0.1:${port}/api/pearls`)).ok,'app startup');
 const catalog=await (await fetch(`http://127.0.0.1:${port}/api/pearls`)).json();
 assert.equal(catalog.subjects.length,4);assert.equal(catalog.subjects.flatMap(s=>s.topics).length,42);
 const first=catalog.subjects[0].topics[0];
 const word=await fetch(`http://127.0.0.1:${port}/api/pearls/document?id=${encodeURIComponent(first.id)}`);
 assert.ok(word.headers.get('content-type').includes('wordprocessingml'));
 assert.equal(Buffer.from(await word.arrayBuffer()).subarray(0,2).toString(),'PK');
 assert.equal((await fetch(`http://127.0.0.1:${port}/api/pearls/document?id=../outside.docx`)).status,404);
 chrome=spawn('C:/Program Files/Google/Chrome/Application/chrome.exe',[
  '--headless=new','--disable-gpu','--no-first-run','--no-default-browser-check',
  '--remote-debugging-port='+debugPort,'--user-data-dir='+path.join(work,'profile'),
  '--window-size=1200,1000','about:blank'],{windowsHide:true,stdio:'ignore'});
 const tab=await until(async()=> (await (await fetch(`http://127.0.0.1:${debugPort}/json/list`)).json()).find(t=>t.type==='page'),'Chrome');
 ws=new WebSocket(tab.webSocketDebuggerUrl);await new Promise((r,j)=>{ws.onopen=r;ws.onerror=j;});
 let sequence=0;const waiting=new Map(),errors=[];
 ws.onmessage=event=>{const msg=JSON.parse(event.data);if(msg.id){const pending=waiting.get(msg.id);waiting.delete(msg.id);if(msg.error)pending.reject(msg.error);else pending.resolve(msg.result);}if(msg.method==='Runtime.exceptionThrown')errors.push(msg.params.exceptionDetails.text);};
 const send=(method,params={})=>new Promise((resolve,reject)=>{const id=++sequence;waiting.set(id,{resolve,reject});ws.send(JSON.stringify({id,method,params}));});
 const evaluate=async expression=>{const result=await send('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true});if(result.exceptionDetails)throw Error(JSON.stringify(result.exceptionDetails));return result.result.value;};
 const screenshot=async name=>{const shot=await send('Page.captureScreenshot',{format:'png'});fs.writeFileSync(path.join(work,name+'.png'),Buffer.from(shot.data,'base64'));};
 await send('Runtime.enable');await send('Page.enable');await send('Page.navigate',{url:`http://127.0.0.1:${port}/`});
 await until(()=>evaluate("!!document.querySelector('#cnlTabBar [data-cnl-tab=pearls]')"),'Pearls tab');
 await evaluate("document.querySelector('#cnlTabBar [data-cnl-tab=pearls]').click()");
 await until(()=>evaluate("document.querySelectorAll('#cnlPearlsPage .subject-card').length===4"),'subjects');
 await screenshot('subjects');
 await evaluate("Array.from(document.querySelectorAll('#cnlPearlsPage .subject-card')).find(b=>b.textContent.includes('Nephrology')).click()");
 await until(()=>evaluate("document.querySelectorAll('#cnlPearlsPage .cnl-pearls-topic').length===10"),'topics');
 await screenshot('topics');
 await evaluate("Array.from(document.querySelectorAll('#cnlPearlsPage .cnl-pearls-topic')).find(b=>b.textContent.includes('Acid Base')).click()");
 await until(()=>evaluate("!!document.querySelector('#cnlPearlsViewerFrame')?.contentDocument?.querySelector('body.view-reader #paper .doc-root')"),'separate Pearls reader');
 const inReader=expression=>evaluate("(()=>{const document=window.document.querySelector('#cnlPearlsViewerFrame').contentDocument;"+expression+"})()");
 assert.equal(await evaluate("document.body.classList.contains('view-reader')"),false,'Main Notes reader is untouched');
 assert.equal(await inReader("return document.querySelectorAll('#paper [data-style-name=Title]').length"),0,'Opening titles are removed');
 assert.ok(await inReader("return document.querySelectorAll('#paper table').length>0"),'Native Notes tables render');
 assert.ok(await inReader("return !!document.querySelector('#cnlReaderBottomPill')"),'Notes bottom pill is duplicated');
 assert.ok(await inReader("return !!document.querySelector('#cnlTypeBtn')"),'Notes typography controls are duplicated');
 await screenshot('acid-base');
 await inReader("document.querySelector('#cnlReaderBottomPill button[aria-label=\"Next heading\"]').click()");
 await inReader("document.querySelector('#cnlOutlineBtn').click()");
 await until(()=>inReader("return document.querySelectorAll('#toc .cnl-scoped-outline-row').length>0"),'native Notes outline');
 await screenshot('outline');
 const firstHeading=await inReader("return document.querySelector('#paper .doc-p.h1').textContent.trim()");
 await inReader("const rows=Array.from(document.querySelectorAll('#toc .cnl-scoped-outline-row'));rows[rows.length-1].click()");
 await screenshot('heading-navigation');
 await inReader("document.querySelector('#headerBackBtn').click()");
 await until(()=>evaluate("!document.querySelector('#cnlPearlsViewerFrame')&&document.querySelectorAll('#cnlPearlsPage .cnl-pearls-topic').length===10"),'back to Pearls topics');
 assert.equal(await evaluate("document.body.classList.contains('view-reader')"),false,'Closing Pearls leaves the main reader untouched');
 await evaluate("Array.from(document.querySelectorAll('#cnlPearlsPage .cnl-pearls-topic')).find(b=>b.textContent.includes('Acid Base')).click()");
 await until(()=>evaluate("!!document.querySelector('#cnlPearlsViewerFrame')?.contentDocument?.querySelector('body.view-reader #paper .doc-root')"),'reopen independent viewer');
 await inReader("document.querySelector('#headerHomeBtn').click()");
 await until(()=>evaluate("!document.querySelector('#cnlPearlsViewerFrame')&&document.body.dataset.cnlTab==='home'"),'Home returns to app Home');
 assert.equal(errors.length,0,'Browser has no uncaught exceptions: '+errors.join('; '));
 console.log('PASS: 4 subjects / 42 title-free Word topics; isolated Pearls viewer duplicates Notes toolbar, outline and bottom pill; heading navigation and Back; main Notes state preserved; download and containment.');
})().catch(err=>{console.error(err);process.exitCode=1;}).finally(()=>{ws?.close();chrome?.kill();app.kill();});
