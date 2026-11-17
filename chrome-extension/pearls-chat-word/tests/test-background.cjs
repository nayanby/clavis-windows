const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm'),assert=require('node:assert/strict');
let action,message,toggles=0;const tabs=[],scripts=[],progress=[],closed=[];
const sandbox={URL,AbortSignal,Uint8Array,btoa,fetch:async()=>new Response(new Uint8Array([1,2,3]),{headers:{'content-type':'image/png'}}),PearlsToolbar:{toggleOverlay(){toggles++;}},chrome:{
  runtime:{getURL:file=>'chrome-extension://test/'+file,onMessage:{addListener:fn=>{message=fn;}}},
  tabs:{create:async tab=>{tabs.push(tab);},sendMessage:async(tabId,event)=>{progress.push({tabId,event});},remove:async id=>{closed.push(id);}},
  action:{onClicked:{addListener:fn=>{action=fn;}},setBadgeText:async()=>{},setTitle:async()=>{}},
  scripting:{executeScript:async options=>{scripts.push(options);if(options.func)await options.func();return [];}}
}};
vm.createContext(sandbox);vm.runInContext(fs.readFileSync(path.join(__dirname,'../background.js'),'utf8'),sandbox);
(async()=>{
  await action({id:7,url:'https://chatgpt.com/c/example'});
  assert.equal(toggles,1);assert.equal(tabs.length,0);assert.equal(scripts.length,2);
  const reply=await new Promise(resolve=>{
    const keepsChannel=message({type:'PEARLS_OPEN_EXPORT',jobId:'job-1',mode:'single',index:2,id:'response-id',fingerprint:'abcd'},{url:'https://chatgpt.com/c/example',tab:{id:7}},resolve);
    assert.equal(keepsChannel,true);
  });
  assert.equal(reply.ok,true);assert.equal(tabs.length,1);
  const opened=new URL(tabs[0].url);
  assert.equal(opened.searchParams.get('mode'),'single');assert.equal(opened.searchParams.get('responseId'),'response-id');
  assert.equal(opened.searchParams.get('index'),'2');
  assert.equal(tabs[0].active,false);assert.equal(opened.searchParams.get('job'),'job-1');
  await new Promise(resolve=>message({type:'PEARLS_EXPORT_PROGRESS',jobId:'job-1',phase:'complete',text:'Downloaded',percent:100},{url:opened.href,tab:{id:99}},resolve));
  assert.equal(progress[0].tabId,7);assert.equal(progress[0].event.percent,100);
  assert.deepEqual(closed,[99]);
  assert.equal(message({type:'PEARLS_EXPORT_PROGRESS',jobId:'job-1',phase:'complete'},{url:'https://chatgpt.com/c/example',tab:{id:7}},()=>{}),undefined);
  assert.equal(message({type:'PEARLS_OPEN_EXPORT',mode:'all'},{url:'https://chatgpt.com.evil.example/',tab:{id:8}},()=>{}),undefined);
  assert.equal(tabs.length,1);
  for(const host of ['images.oaiusercontent.com','images.openai.com']){
    const image=await new Promise(resolve=>message({type:'PEARLS_FETCH_IMAGE',url:'https://'+host+'/example.png'},{url:'https://chatgpt.com/c/example',tab:{id:7}},resolve));
    assert.equal(image.data,'data:image/png;base64,AQID');
  }
  const rejected=await new Promise(resolve=>message({type:'PEARLS_FETCH_IMAGE',url:'https://oaiusercontent.com.evil.example/a.png'},{url:'https://chatgpt.com/c/example',tab:{id:7}},resolve));
  assert(rejected.error);
  assert.equal(message({type:'PEARLS_FETCH_IMAGE',url:'https://images.oaiusercontent.com/a.png'},{url:'https://evil.example',tab:{id:7}},()=>{}),undefined);
  console.log('PASS: extension icon toggles two-button overlay without opening a tab; download actions open the correct exporter; unsupported origins rejected.');
})().catch(error=>{console.error(error);process.exitCode=1;});
