const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {chromium}=require('playwright');
(async()=>{const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});try{
const page=await browser.newPage(),root=path.resolve(__dirname,'..');
await page.setContent('<svg xmlns="http://www.w3.org/2000/svg" width="600" height="400"><rect width="600" height="400" fill="white"/><text x="40" y="80" font-size="24">Sharp diagnostic algorithm</text><path d="M80 100V280" stroke="black"/></svg>');
for(const file of ['vendor/html2canvas-page.min.js','vendor/jszip.min.js','word-export.js'])await page.addScriptTag({path:path.join(root,file)});
const r=await page.evaluate(async({template,profile})=>{const img=await __pearlsPageRendererV1(document.querySelector('svg'));const bitmap=await createImageBitmap(await(await fetch(img.data)).blob());const result={width:bitmap.width,height:bitmap.height};bitmap.close();const doc=await PearlsWord.create({messages:[{role:'assistant',blocks:[{type:'image',...img}]}],warnings:[]},{single:true,title:'Quality',templateBytes:new Uint8Array(template),profile});const z=await JSZip.loadAsync(doc.bytes);result.xml=await z.file('word/document.xml').async('string');return result;},{template:[...fs.readFileSync(path.join(root,'template/base.docx'))],profile:JSON.parse(fs.readFileSync(path.join(root,'template/profile.json')))});
assert.equal(r.width,2400);assert.equal(r.height,1600);assert(r.xml.includes('cy="2160000"'));assert(r.xml.includes('cx="3240000"'));console.log('PASS: 4x SVG pixels and proportional 6 cm DOCX image');
}finally{await browser.close();}})().catch(e=>{console.error(e);process.exit(1)});
