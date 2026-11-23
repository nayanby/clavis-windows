const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {chromium}=require('playwright');
(async()=>{const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});try{
const page=await browser.newPage({viewport:{width:1100,height:720}}),root=path.resolve(__dirname,'..');await page.goto('about:blank');
await page.setContent('<style>body{margin:0;padding:130px 30px 500px;font:18px Arial}.flow{width:620px;height:1540px;box-sizing:border-box;background:#142335;color:white;padding:28px;display:flex;flex-direction:column;justify-content:space-between}.card{border:1px solid #a4c7e9;border-radius:12px;background:#274561;padding:24px}.arrow{text-align:center;font-size:46px}</style><main id="fixture"><p>OUTSIDE BEFORE</p><div class="flow"><div class="card"><h3>Clinical features</h3><p>Raynaud phenomenon, arthritis and rash</p></div><div class="arrow">↓</div><div class="card"><h3>ANA by HEp-2 IIF</h3><div style="display:grid;grid-template-columns:1fr 1fr;gap:20px"><div>ANA positive</div><div>ANA negative</div></div></div><div class="arrow">↓</div><div class="card"><h3>Integrate clinical findings</h3><p>END OF COMPLETE DIAGRAM</p></div></div><p>OUTSIDE AFTER</p></main>');
let requests=0;
await page.exposeFunction('nativeScreenshot',async()=>{requests++;return {data:'data:image/png;base64,'+(await page.screenshot()).toString('base64')};});
for(const file of ['vendor/jszip.min.js','capture.js','word-export.js'])await page.addScriptTag({path:path.join(root,file)});
const result=await page.evaluate(async({template,profile})=>{
 globalThis.chrome={runtime:{sendMessage:async request=>{if(request.type!=='PEARLS_CROP_VISUAL')throw Error('Only real screenshots allowed');return nativeScreenshot();}}};
 globalThis.html2canvas=()=>{throw Error('HTML rasterizer must not be used');};
 const fixture=document.querySelector('#fixture'),original=fixture.innerHTML,x=scrollX,y=scrollY;
 const blocks=PearlsCapture.blocks(fixture),data=await PearlsCapture.resolveImages({messages:[{role:'assistant',blocks}],warnings:[]});
 const image=data.messages[0].blocks.find(b=>b.type==='image');if(!image?.data)throw Error(JSON.stringify(data.warnings));
 const bitmap=await createImageBitmap(await(await fetch(image.data)).blob()),canvas=document.createElement('canvas');canvas.width=bitmap.width;canvas.height=bitmap.height;const ctx=canvas.getContext('2d');ctx.drawImage(bitmap,0,0);bitmap.close();
 const doc=await PearlsWord.create(data,{single:true,title:'Complete flowchart',templateBytes:new Uint8Array(template),profile});const zip=await JSZip.loadAsync(doc.bytes);
 return {restored:fixture.innerHTML===original&&scrollX===x&&scrollY===y,types:blocks.map(b=>b.type),width:canvas.width,height:canvas.height,top:[...ctx.getImageData(5,5,1,1).data],bottom:[...ctx.getImageData(5,canvas.height-5,1,1).data],png:image.data.split(',')[1],bytes:[...doc.bytes],media:Object.keys(zip.files).filter(n=>n.startsWith('word/media/')&&!n.endsWith('/')),xml:await zip.file('word/document.xml').async('string')};
},{template:[...fs.readFileSync(path.join(root,'template/base.docx'))],profile:JSON.parse(fs.readFileSync(path.join(root,'template/profile.json')))});
assert.deepEqual(result.types,['paragraph','image','paragraph']);assert(result.restored);assert(requests>=3);assert.equal(result.width,620);assert.equal(result.height,1540);assert.deepEqual(result.top,[20,35,53,255]);assert.deepEqual(result.bottom,[20,35,53,255]);assert.equal(result.media.length,1);assert(!/<w:t[^>]*>[^<]*ANA positive/.test(result.xml));assert(result.xml.includes('OUTSIDE BEFORE'));assert(result.xml.includes('OUTSIDE AFTER'));
const out=path.resolve(root,'../../build/chat-word-qa');fs.mkdirSync(out,{recursive:true});fs.writeFileSync(path.join(out,'chrome-flowchart.png'),Buffer.from(result.png,'base64'));fs.writeFileSync(path.join(out,'chrome-flowchart.docx'),Buffer.from(result.bytes));console.log('PASS: full dark flowchart captured as ONE PNG using '+requests+' real Chrome screenshots; text/cards/arrows retained; source scroll and DOM restored; one Word image embedded');
}finally{await browser.close();}})().catch(e=>{console.error(e);process.exit(1)});



