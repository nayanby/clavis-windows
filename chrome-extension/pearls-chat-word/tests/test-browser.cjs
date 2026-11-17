const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const { chromium } = require('playwright');
const root = path.resolve(__dirname, '..');
const output = path.resolve(root, '../..', 'build/chat-word-qa');
fs.mkdirSync(output, { recursive: true });
const template = [...fs.readFileSync(path.join(root, 'template/base.docx'))];
const profile = JSON.parse(fs.readFileSync(path.join(root, 'template/profile.json')));
async function run() {
  const executable=process.env.PEARLS_FIXTURE_BROWSER||'C:/Program Files/Google/Chrome/Application/chrome.exe';
  const browser = await chromium.launch({ executablePath:executable, headless: true, timeout:15000,args: ['--disable-background-networking', '--no-first-run'] });
  try {
    const page = await browser.newPage();
    const errors = []; page.on('pageerror', error => errors.push(error.message));page.on('console',msg=>{if(msg.text().startsWith('Pearls native crop:')||msg.text().startsWith('Crop test capture:'))console.log(msg.text());});
    await page.route('**/*', route => route.fulfill({ contentType: 'text/html', body: fs.readFileSync(path.join(__dirname, 'fixtures/chatgpt.html'), 'utf8') }));
    await page.goto('https://chatgpt.com/c/test-fixture');
    await page.addScriptTag({ path: path.join(root, 'vendor/html2canvas.min.js') });
    await page.addScriptTag({ path: path.join(root, 'capture.js') });
    const chat = await page.evaluate(() => PearlsCapture.snapshot());
    assert.equal(chat.messages.length, 6);
    assert.equal(chat.messages.filter(m => m.role === 'assistant').length, 3);
    await page.evaluate(() => { globalThis.toolbarRequests=[];globalThis.autoCompleteJobs=true;globalThis.chrome={runtime:{onMessage:{addListener:fn=>{globalThis.progressListener=fn;}},sendMessage:async value=>{toolbarRequests.push(value);if(autoCompleteJobs)queueMicrotask(()=>PearlsToolbar.updateProgress(value.jobId,{phase:'complete',text:'Downloaded',percent:100}));return {ok:true};}}}; });
    await page.evaluate(()=>{const stale=document.createElement('div');stale.setAttribute('data-pearls-toolbar','chat');stale.id='stale-extension-toolbar';document.body.append(stale);});
    await page.addScriptTag({ path: path.join(root, 'page-toolbar.js') });
    assert.equal(await page.locator('#stale-extension-toolbar').count(),0);
    assert.equal(await page.locator('[data-pearls-toolbar="chat"]').count(), 1);
    assert.equal(await page.locator('[data-pearls-toolbar="response"]').count(), 0);
    assert.equal(await page.locator('main [data-pearls-toolbar], [data-message-author-role] [data-pearls-toolbar]').count(),0,'Controls must not be inserted into chat-owned content');
    await page.evaluate(() => PearlsToolbar.render());
    assert.equal(await page.locator('[data-pearls-toolbar="response"]').count(), 0);
    await page.locator('[data-pearls-toolbar="chat"]').getByRole('button',{name:'Download response',exact:true}).click({timeout:8000});
    assert.equal(await page.evaluate(() => toolbarRequests[0].mode), 'single');
    assert.equal(await page.evaluate(() => toolbarRequests[0].id), 'a1');
    await page.locator('[data-pearls-toolbar="chat"]').getByRole('button',{name:'Download entire chat',exact:true}).click({timeout:5000});
    assert.equal(await page.evaluate(() => toolbarRequests[1].mode), 'all');
    await page.evaluate(()=>{scrollTo(0,0);PearlsToolbar.toggleOverlay();});
    const floating=page.locator('[data-pearls-toolbar="chat"][data-placement="overlay"]');
    assert.equal(await floating.getByRole('button').count(),2);
    assert.equal(await floating.evaluate(el=>getComputedStyle(el).position),'fixed');
    await floating.screenshot({path:path.join(output,'two-button-toolbar.png')});
    await floating.getByRole('button',{name:'Download response',exact:true}).click();
    assert.equal(await page.evaluate(()=>toolbarRequests[2].mode),'single');
    assert.equal(await page.evaluate(()=>toolbarRequests[2].id),'a1');
    await page.evaluate(()=>PearlsToolbar.toggleOverlay());
    assert.equal(await page.locator('[data-placement="overlay"]').count(),0);
    await page.evaluate(()=>{autoCompleteJobs=false;PearlsToolbar.toggleOverlay();});
    await floating.getByRole('button',{name:'Download response',exact:true}).click();
    const jobId=await page.evaluate(()=>toolbarRequests.at(-1).jobId);
    assert.equal(await floating.getByRole('progressbar').count(),1);
    assert.equal(await floating.getByRole('button',{name:'Download response',exact:true}).isDisabled(),true);
    await page.evaluate(jobId=>progressListener({type:'PEARLS_EXPORT_PROGRESS',jobId,phase:'packaging',text:'Creating Word file · 42%',percent:42}),jobId);
    assert.equal(await floating.getByRole('progressbar').getAttribute('value'),'42');
    await floating.screenshot({path:path.join(output,'toolbar-progress.png')});
    await page.evaluate(jobId=>progressListener({type:'PEARLS_EXPORT_PROGRESS',jobId,phase:'complete',text:'Downloaded · Immunology.docx',percent:100}),jobId);
    assert.equal(await floating.getByRole('button',{name:'Download response',exact:true}).isDisabled(),false);
    await floating.getByRole('button',{name:'Download response',exact:true}).click();
    await page.evaluate(()=>progressListener({type:'PEARLS_EXPORT_PROGRESS',jobId:toolbarRequests.at(-1).jobId,phase:'error',text:'The download was cancelled.'}));
    assert.equal(await floating.getByRole('button',{name:'Download response',exact:true}).isDisabled(),false);
    assert.equal(await floating.locator('.progress-label').textContent(),'The download was cancelled.');
    await page.evaluate(()=>{autoCompleteJobs=true;PearlsToolbar.toggleOverlay();});
    const withToolbars = await page.evaluate(() => PearlsCapture.snapshot());
    assert.equal(JSON.stringify(withToolbars), JSON.stringify(chat));
    const captured = JSON.stringify(chat);
    assert(!captured.includes('PRIVATE SIDEBAR'));
    assert(!captured.includes('Copy response toolbar'));
    assert(!captured.includes('duplicate equation'));
    assert(captured.includes('x^2 + y^2'));
    const full = await page.evaluate(() => PearlsCapture.conversation());
    assert.equal(full.messages.length, 6);
    assert.equal(full.messages.filter(m => m.preview === 'Repeated answer.').length, 2);
    const resolved=await page.evaluate(()=>PearlsCapture.resolveImages(PearlsCapture.snapshot()));
    assert(resolved.messages[1].blocks.find(block=>block.type==='image').data.startsWith('data:image/png;base64,'));
    Object.assign(chat,resolved);
    // Generated images nested in preview controls and links must be real media.
    const imageCases=await page.evaluate(async()=>{
      const src=document.querySelector('img[alt="Example diagram"]').src;
      const fixture=document.createElement('div');
      fixture.innerHTML=`<button><img alt="Generated picture" src="${src}" width="2" height="2"></button><p><a href="#"><img alt="Linked picture" src="${src}" width="2" height="2"></a></p>`;
      const captured=PearlsCapture.blocks(fixture);
      const result=await PearlsCapture.resolveImages({messages:[{blocks:captured}],warnings:[]});
      const fetchOriginal=globalThis.fetch,sendOriginal=chrome.runtime.sendMessage,browserOriginal=globalThis.browser;
      let relayed=false;
      globalThis.fetch=(url,...args)=>String(url).startsWith('https://images.oaiusercontent.com/')?Promise.reject(Error('CORS')):fetchOriginal(url,...args);
      chrome.runtime.sendMessage=async request=>{relayed=request.type==='PEARLS_FETCH_IMAGE';return {data:src};};
      globalThis.browser={runtime:{sendMessage:chrome.runtime.sendMessage}};
      try {
        const fallback=await PearlsCapture.resolveImages({messages:[{blocks:[{type:'image',src:'https://images.oaiusercontent.com/test.png',alt:'CDN picture'}]}],warnings:[]});
        return {types:captured.map(b=>b.type),data:result.messages[0].blocks.every(b=>b.data?.startsWith('data:image/png;base64,')),relayed,fallback:!!fallback.messages[0].blocks[0].data};
      } finally {globalThis.fetch=fetchOriginal;chrome.runtime.sendMessage=sendOriginal;globalThis.browser=browserOriginal;}
    });
    assert.deepEqual(imageCases.types,['image','image']);assert(imageCases.data&&imageCases.relayed&&imageCases.fallback);
    assert(await page.evaluate(()=>{
      const icon=document.createElement('img');icon.src='https://www.google.com/s2/favicons?domain=example.org&sz=32';
      document.querySelector('[data-message-author-role="assistant"] .markdown').append(icon);
      try{return !JSON.stringify(PearlsCapture.snapshot()).includes('/s2/favicons');}finally{icon.remove();}
    }));
    assert.equal(await page.evaluate(() => {
      const a = { role: 'assistant', id: 'a', blocks: [] }, b = { role: 'user', id: 'b', blocks: [] }, c = { role: 'assistant', id: 'c', blocks: [] };
      return PearlsCapture.merge([a,b],[b,c]).map(x => x.id).join(',');
    }), 'a,b,c');
    assert.equal(await page.evaluate(() => { try { PearlsCapture.merge([{id:'a'}],[{id:'z'}]); return false; } catch { return true; } }), true);
    await page.addScriptTag({ path: path.join(root, 'vendor/jszip.min.js') });
    await page.addScriptTag({ path: path.join(root, 'word-export.js') });
    const visual=await page.evaluate(async({template,profile})=>{
      const fixture=document.createElement('div');fixture.style.cssText='width:780px;background:white;padding:12px;font:20px Arial';
      fixture.innerHTML='<p>Carrier parents: Aa × Aa</p><div style="padding:20px"><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:6px;text-align:center"><div>×</div><div>A</div><div>a</div><div>A</div><div style="background:oklch(96% 0.03 160);padding:20px;border-radius:8px">AA</div><div style="background:#f5eddf;padding:20px;border-radius:8px">Aa</div><div>a</div><div style="background:#f5eddf;padding:20px;border-radius:8px">Aa</div><div style="background:#f7e6e8;padding:20px;border-radius:8px">aa</div></div><div style="display:flex;justify-content:space-around;padding-top:20px"><div><h3>25%</h3><div>Unaffected noncarrier</div></div><div><h3>50%</h3><div>Unaffected carrier</div></div><div><h3>25%</h3><div>Affected</div></div></div></div><p>p^2+2pq+q^2=1</p><p><span class="katex"><annotation encoding="application/x-tex">x_{ij} + q^{2}</annotation></span></p><svg xmlns="http://www.w3.org/2000/svg" width="300" height="100"><rect width="300" height="100" fill="#e3f1ec"/><text x="20" y="55" font-size="24">SVG Diagram</text></svg>';
      document.body.append(fixture);
      fixture.children[1].setAttribute('data-markdown-copy','exclude');
      try{
        const original=fixture.innerHTML;
        let rasterCalls=0;const rasterOriginal=globalThis.html2canvas;
        globalThis.html2canvas=(...args)=>{rasterCalls++;return rasterOriginal(...args);};
        let captured;
        try{captured=PearlsCapture.blocks(fixture);if(rasterCalls!==0)throw Error('Preview scan started diagram rendering');}
        finally{globalThis.html2canvas=rasterOriginal;}
        if(fixture.innerHTML!==original)throw Error('Scan changed the original diagram');
        const data=await PearlsCapture.resolveImages({messages:[{role:'assistant',blocks:captured}],warnings:[]});
        if(fixture.innerHTML!==original)throw Error('Export changed the original diagram');
        const images=data.messages[0].blocks.filter(b=>b.type==='image');
        if(!images[0]?.alt.includes('Unaffected noncarrier')||!images[0]?.alt.includes('Affected'))throw Error('Diagram legend was not included in the captured image');
        if(images.length!==2||images.some(b=>!b.data))throw Error('Diagram rasterization failed: '+JSON.stringify(data.warnings));
        const doc=await PearlsWord.create(data,{single:true,title:'Inheritance Diagram',templateBytes:new Uint8Array(template),profile});
        const zip=await JSZip.loadAsync(doc.bytes),xml=await zip.file('word/document.xml').async('string');
        return {bytes:[...doc.bytes],png:images[0].data.split(',')[1],xml,types:data.messages[0].blocks.map(b=>b.type)};
      }finally{fixture.remove();}
    },{template,profile});
    assert.deepEqual(visual.types,['paragraph','image','paragraph','paragraph','image']);
    assert(visual.xml.includes('w:val="superscript"')&&visual.xml.includes('w:val="subscript"'));
    assert(!visual.xml.includes('p^2')&&!visual.xml.includes('q^{2}')&&!visual.xml.includes('x_{ij}'));
    assert.equal((visual.xml.match(/cy="1440000"/g)||[]).length,4);
    fs.writeFileSync(path.join(output,'diagram-example.docx'),Buffer.from(visual.bytes));
    fs.writeFileSync(path.join(output,'diagram-example.png'),Buffer.from(visual.png,'base64'));
    await page.exposeFunction('pearlsTestCrop',async request=>{
      const bytes=await page.screenshot();
      return {data:'data:image/png;base64,'+bytes.toString('base64')};
    });
    const nativeCrop=await page.evaluate(async()=>{
      const savedBrowser=globalThis.browser,savedRaster=globalThis.html2canvas;
      let requests=0,rasterCalls=0;
      const fixture=document.createElement('div');fixture.style.cssText='width:650px;margin:20px';
      fixture.innerHTML='<p>OUTSIDE BEFORE</p><div data-diagram aria-label="Complete inheritance chart" style="height:250px;background:#eef7ef;padding:15px;box-sizing:border-box"><div style="display:flex;justify-content:space-around"><span>AA</span><span>Aa</span><span>aa</span></div><div style="display:flex;justify-content:space-around;margin-top:130px"><span>25% noncarrier</span><span>50% carrier</span><span>25% affected</span></div></div><p>OUTSIDE AFTER</p>';
      document.body.append(fixture);
      const initialScroll=scrollY,original=fixture.innerHTML;
      globalThis.browser={runtime:{getBrowserInfo:async()=>({name:'Firefox'}),sendMessage:async request=>{requests++;try{return await pearlsTestCrop(request);}catch(error){console.error("Crop test capture:",error.message);throw error;}}}};
      globalThis.html2canvas=(...args)=>{rasterCalls++;return savedRaster(...args);};
      try{
        const data=await PearlsCapture.resolveImages({messages:[{blocks:PearlsCapture.blocks(fixture)}],warnings:[]});
        const image=data.messages[0].blocks.find(b=>b.type==='image');
        return {requests,rasterCalls,width:image.width,height:image.height,png:image.data?.split(',')[1],restored:scrollY===initialScroll&&fixture.innerHTML===original,types:data.messages[0].blocks.map(b=>b.type)};
      }finally{fixture.remove();globalThis.browser=savedBrowser;globalThis.html2canvas=savedRaster;}
    });
    assert.equal(nativeCrop.requests,1);assert.equal(nativeCrop.rasterCalls,0);assert(nativeCrop.restored);
    assert.equal(nativeCrop.width,650);assert.equal(nativeCrop.height,250);assert.deepEqual(nativeCrop.types,['paragraph','image','paragraph']);
    fs.writeFileSync(path.join(output,'firefox-native-crop.png'),Buffer.from(nativeCrop.png,'base64'));
    assert(await page.evaluate(async()=>{
      const message=document.querySelector('[data-message-author-role="assistant"]');
      const visual=document.createElement('div');
      visual.setAttribute('data-markdown-copy','exclude');
      visual.style.cssText='display:flex;width:700px;gap:10px';
      visual.innerHTML='<div style="padding:30px;background:#e3f1ec">AA — 25%</div><div style="padding:30px;background:#f5eddf">Aa — 50%</div><div style="padding:30px;background:#f7e6e8">aa — 25%</div>';
      // A visual sibling outside .markdown was lost by the old reader.
      message.append(visual);
      try{
        const data=await PearlsCapture.resolveImages(PearlsCapture.snapshot());
        const block=data.messages.find(m=>m.id==='a1').blocks.find(b=>b.diagramId);
        return !!block?.data&&block.alt.includes('AA')&&block.alt.includes('50%');
      }finally{visual.remove();}
    }));
    const headingCases=await page.evaluate(async({template,profile})=>{
      const h=(level,text)=>({type:'heading',level,runs:[{text}]});
      const cases=[
        [h(1,'Main'),h(2,'I. Classification'),h(2,'II. Predominantly Antibody Deficiencies')],
        [h(1,'Main'),h(2,'1. First'),h(2,'2. Second')],
        [h(1,'Main'),h(2,'First'),h(2,'Second')],
      ];
      const results=[];
      for(const blocks of cases){
        const doc=await PearlsWord.create({messages:[{role:'assistant',blocks}]},{single:true,title:'Heading checks',templateBytes:new Uint8Array(template),profile});
        const zip=await JSZip.loadAsync(doc.bytes);const parsed=new DOMParser().parseFromString(await zip.file('word/document.xml').async('string'),'application/xml');
        results.push([...parsed.getElementsByTagNameNS('http://schemas.openxmlformats.org/wordprocessingml/2006/main','p')].map(p=>p.textContent));
      }
      return results;
    },{template,profile});
    assert(headingCases[0].includes('I. Classification'));
    assert(headingCases[0].includes('II. Predominantly Antibody Deficiencies'));
    assert(!headingCases[0].some(text=>/^[A-Z]\. [IVX]+\./.test(text)));
    assert(headingCases[1].includes('1. First'));assert(headingCases[1].includes('2. Second'));
    assert(headingCases[2].includes('First'));assert(headingCases[2].includes('Second'));
    assert(!headingCases[2].includes('A. First'));
    const hierarchy=await page.evaluate(async({template,profile})=>{
      const h=(level,text)=>({type:'heading',level,runs:[{text}]});
      const doc=await PearlsWord.create({messages:[{role:'assistant',blocks:[h(1,'Major Immunodeficiency Syndromes'),h(2,'I. Classification'),h(3,'A. Functional Classification'),h(2,'II. Predominantly Antibody Deficiencies'),h(3,'A. Bruton Disease')]}]},{single:true,title:'Major Immunodeficiency Syndromes',templateBytes:new Uint8Array(template),profile});
      const zip=await JSZip.loadAsync(doc.bytes);const parsed=new DOMParser().parseFromString(await zip.file('word/document.xml').async('string'),'application/xml');
      const ns='http://schemas.openxmlformats.org/wordprocessingml/2006/main';
      return [...parsed.getElementsByTagNameNS(ns,'p')].map(p=>({text:p.textContent,style:p.getElementsByTagNameNS(ns,'pStyle')[0]?.getAttributeNS(ns,'val')}));
    },{template,profile});
    assert.equal(hierarchy.filter(p=>p.style==='Heading1').length,1);
    assert.equal(hierarchy.find(p=>p.text==='Major Immunodeficiency Syndromes').style,'Heading1');
    assert.equal(hierarchy.find(p=>p.text==='I. Classification').style,'Heading2');
    assert.equal(hierarchy.find(p=>p.text==='II. Predominantly Antibody Deficiencies').style,'Heading2');
    assert.equal(hierarchy.find(p=>p.text==='A. Functional Classification').style,'Heading3');
    for (const [name, messages, single, includePrompts] of [
      ['full-chat', chat.messages, false, true],
      ['single-response', [chat.messages[1]], true, false],
      ['responses-only', chat.messages, false, false],
    ]) {
      const result = await page.evaluate(async ({ chat, messages, single, includePrompts, template, profile }) => {
        const doc = await PearlsWord.create({ ...chat, messages }, { title: 'Immunology Pearls', single, includePrompts, templateBytes: new Uint8Array(template), profile });
        const zip = await JSZip.loadAsync(doc.bytes);
        const xml = await zip.file('word/document.xml').async('string');
        const numbers = await zip.file('word/numbering.xml').async('string');
        const parsed = new DOMParser().parseFromString(xml, 'application/xml');
        const paragraphs = [...parsed.getElementsByTagNameNS('http://schemas.openxmlformats.org/wordprocessingml/2006/main','p')].map(p => p.textContent);
        for(const cell of parsed.getElementsByTagNameNS('http://schemas.openxmlformats.org/wordprocessingml/2006/main','tc')){
          for(const style of cell.getElementsByTagNameNS('http://schemas.openxmlformats.org/wordprocessingml/2006/main','pStyle')){
            if(/Heading|BoldSide|boldside/i.test(style.getAttributeNS('http://schemas.openxmlformats.org/wordprocessingml/2006/main','val')))throw Error('A table label was exported as an outline heading.');
          }
        }
        return { bytes: [...doc.bytes], xml, numbers, paragraphs, warnings: doc.warnings };
      }, { chat, messages, single, includePrompts, template, profile });
      assert(result.xml.includes('Bone marrow'));
      assert(result.xml.includes('Sole Subsection'));
      assert(result.paragraphs.includes('A. Sole Subsection'));
      assert(result.paragraphs.includes('A. IgG'), JSON.stringify(result.paragraphs));
      assert(result.paragraphs.includes('B. IgM'));
      assert(!result.xml.includes('numId w:val="0"'));
      assert(result.xml.includes('w:vMerge'));
      assert(result.xml.includes('w:gridSpan'));
      assert(result.numbers.indexOf('<w:num ') > result.numbers.lastIndexOf('</w:abstractNum>'));
      assert(!result.xml.includes('PRIVATE SIDEBAR'));
      if (!includePrompts) assert(!result.xml.includes('Explain immunoglobulins'));
      fs.writeFileSync(path.join(output, name + '.docx'), Buffer.from(result.bytes));
    }
    // The new ChatGPT Work markup must not silently produce disabled controls.
    await page.unroute('**/*');await page.route('**/*',route=>route.fulfill({contentType:'text/html',body:fs.readFileSync(path.join(__dirname,'fixtures/chatgpt-work.html'),'utf8')}));
    await page.goto('https://chatgpt.com/c/work-fixture');await page.addScriptTag({path:path.join(root,'capture.js')});
    const work=await page.evaluate(()=>PearlsCapture.snapshot());
    assert.equal(work.messages.length,4);assert.equal(work.messages[1].id,'work-a1');assert.equal(work.messages[1].role,'assistant');
    assert.equal(work.messages[1].blocks.filter(block=>block.type==='table').length,1);
    assert(!JSON.stringify(work).includes('Copy response'));
    await page.addScriptTag({path:path.join(root,'page-toolbar.js')});
    assert.equal(await page.locator('[data-pearls-toolbar="response"]').count(),0);
    await page.evaluate(()=>PearlsToolbar.toggleOverlay());
    const workToolbar=page.locator('[data-pearls-toolbar="chat"]');
    assert.equal(await workToolbar.getByRole('button',{name:'Download response',exact:true}).isEnabled(),true);
    assert.equal(await workToolbar.evaluate(el=>el.parentElement===document.body),true);
    // Adapters are exercised against local synthetic pages, not live user chats.
    for (const [provider, url, fixture] of [
      ['claude','https://claude.ai/chat/test', '<div data-testid="user-message">Question</div><div data-testid="assistant-message"><div class="font-claude-response"><div class="standard-markdown"><h2>Claude heading</h2><p>Answer.</p></div></div></div>'],
      ['gemini','https://gemini.google.com/app/test','<user-query><div class="query-text">Question</div></user-query><model-response><div class="model-response-text"><h2>Gemini heading</h2><p>Answer.</p></div></model-response>'],
    ]) {
      await page.unroute('**/*'); await page.route('**/*', route => route.fulfill({contentType:'text/html',body:fixture}));
      await page.goto(url); await page.addScriptTag({ path: path.join(root, 'capture.js') });
      const data = await page.evaluate(() => PearlsCapture.snapshot());
      assert.equal(data.provider, provider); assert.equal(data.messages.length, 2);
      assert.equal(data.messages[1].role, 'assistant');
      await page.addScriptTag({path:path.join(root,'page-toolbar.js')});
      assert.equal(await page.locator('[data-pearls-toolbar="response"]').count(),0);
      assert.equal(await page.locator('[data-pearls-toolbar="chat"]').count(),1);
    }
    // Exercise the exporter controller and automatic toolbar download path.
    const exporter = await browser.newPage({viewport:{width:1100,height:950}});
    exporter.on('pageerror',error=>errors.push(error.message));
    await exporter.addInitScript(data => {
      globalThis.mockDownloads=[];
      globalThis.progressEvents=[];
      globalThis.chrome={
        runtime:{getURL:file=>location.origin+'/'+file,sendMessage:async event=>{progressEvents.push(event);return {ok:true};}},
        scripting:{executeScript:async options=> {
          if(options.files)return [];
          const value=structuredClone(data);
          if(options.args[0]==='single')value.messages=[value.messages.filter(m=>m.role==='assistant')[options.args[1]]];
          return [{result:{value}}];
        }},
        downloads:{download:async options=>{const bytes=[...new Uint8Array(await(await fetch(options.url)).arrayBuffer())];mockDownloads.push({...options,bytes});return mockDownloads.length;},search:async options=>[{id:options.id,state:'complete'}],onChanged:{addListener(){},removeListener(){}}}
      };
    },chat);
    await exporter.route('**/*',route=>{
      const name=new URL(route.request().url()).pathname.slice(1)||'exporter.html';
      const file=path.join(root,name);
      const types={'.html':'text/html','.js':'text/javascript','.css':'text/css','.json':'application/json','.png':'image/png','.docx':'application/vnd.openxmlformats-officedocument.wordprocessingml.document'};
      if(!file.startsWith(root+path.sep)||!fs.existsSync(file))return route.fulfill({status:404,body:''});
      return route.fulfill({contentType:types[path.extname(file)]||'application/octet-stream',headers:{'Content-Security-Policy':"script-src 'self'; object-src 'none'"},body:fs.readFileSync(file)});
    });
    await exporter.goto('https://pearls.test/exporter.html?tab=42&mode=single&responseId=a1&index=0&job=ui-job');
    await exporter.waitForFunction(()=>mockDownloads.length===1);
    await exporter.waitForFunction(()=>progressEvents.some(event=>event.phase==='complete'));
    assert.equal(await exporter.evaluate(()=>progressEvents.some(event=>event.phase==='packaging'&&event.percent===100)),true);
    assert.equal(await exporter.locator('#response').inputValue(),'0');
    assert.equal(await exporter.evaluate(()=>mockDownloads[0].filename),'Immunoglobulin Classes - Response 1.docx');
    const uiDoc=await exporter.evaluate(()=>mockDownloads[0].bytes);
    fs.writeFileSync(path.join(output,'toolbar-response.docx'),Buffer.from(uiDoc));
    await exporter.screenshot({path:path.join(output,'exporter-ui.png'),fullPage:true});
    await exporter.goto('https://pearls.test/exporter.html?tab=42&mode=all&job=ui-all-job');
    await exporter.waitForFunction(()=>mockDownloads.length===1);
    assert.equal(await exporter.evaluate(()=>mockDownloads[0].filename),'Immunology Pearls.docx');
    await exporter.close();
    assert.deepEqual(errors, []);
    console.log('PASS: automatic response/chat toolbars, click targets, all three adapters, full-chat traversal, repeated turns, response-only export, headings, equations, nested/restarted lists, image packaging, merged tables and escaping.');
    console.log('QA documents: ' + output);
  } catch(error){console.error(error);throw error;} finally { await browser.close(); }
}
run().catch(error => { console.error(error); process.exitCode = 1; });
