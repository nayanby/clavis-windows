const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {chromium}=require(process.env.PEARLS_PLAYWRIGHT||'playwright');
(async()=>{const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});try{
const page=await browser.newPage(),root=path.resolve(__dirname,'..');
await page.goto('about:blank');
for(const file of ['vendor/jszip.min.js','capture.js','word-export.js'])await page.addScriptTag({path:path.join(root,file)});
const result=await page.evaluate(async({template,profile})=>{
 const div=document.createElement('div');div.innerHTML='<p><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>URR</mi><mo>=</mo><mfrac><mrow><mtext>Pre-HD urea</mtext><mo>−</mo><mtext>Post-HD urea</mtext></mrow><mtext>Pre-HD urea</mtext></mfrac><mo>×</mo><mn>100</mn></mrow><annotation encoding="application/x-tex">DO NOT DUPLICATE</annotation></semantics></math></span><span aria-hidden="true">DUPLICATE</span></span></p>';
 document.body.append(div);const blocks=PearlsCapture.blocks(div);
 blocks.push({type:'paragraph',runs:[{math:true,text:String.raw`\mathrm{URR}=\frac{\text{Pre-HD urea}-\text{Post-HD urea}}{\text{Pre-HD urea}}\times100`}]});
 blocks.push({type:'paragraph',runs:[{math:true,text:String.raw`p^2+2pq+q^2=1; x_{ij}; \sqrt{q}`}]});
 const doc=await PearlsWord.create({messages:[{role:'assistant',blocks}]},{single:true,title:'Equation regression',templateBytes:new Uint8Array(template),profile});
 const zip=await JSZip.loadAsync(doc.bytes);return {bytes:[...doc.bytes],xml:await zip.file('word/document.xml').async('string')};
},{template:[...fs.readFileSync(path.join(root,'template/base.docx'))],profile:JSON.parse(fs.readFileSync(path.join(root,'template/profile.json')))});
const xml=result.xml;assert.equal((xml.match(/<m:f>/g)||[]).length,2);assert(xml.includes('<m:sSup>'));assert(xml.includes('<m:sSub>'));assert(xml.includes('<m:rad>'));assert(!xml.includes('DUPLICATE'));assert(!xml.includes('\\frac'));assert(!xml.includes('\\mathrm'));
const out=path.resolve(root,'../../build/chat-word-qa');fs.mkdirSync(out,{recursive:true});fs.writeFileSync(path.join(out,'equations.docx'),Buffer.from(result.bytes));console.log('PASS: capture and Word export: URR fractions, MathML, TeX fallback, scripts and root');
}finally{await browser.close();}})().catch(e=>{console.error(e);process.exit(1)});
