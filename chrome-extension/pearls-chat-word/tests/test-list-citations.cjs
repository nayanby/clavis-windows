const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {chromium}=require('playwright');
(async()=>{const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});try{
const page=await browser.newPage(),root=path.resolve(__dirname,'..');await page.goto('about:blank');
for(const file of ['vendor/jszip.min.js','capture.js','word-export.js'])await page.addScriptTag({path:path.join(root,file)});
const result=await page.evaluate(async({template,profile})=>{
 const div=document.createElement('div');div.innerHTML='<h3>B. Chelation</h3><ol><li><p><strong>Succimer (DMSA)</strong></p><ul><li><p>Retain clinical prose. <a href="https://cdc.gov/test">CDC</a></p></li><li><p><a href="https://stacks.cdc.gov/test">CDC Stacks</a></p><p>Retain follow-up text.</p></li></ul></li><li><h4>Severe poisoning or encephalopathy</h4><ul><li><p>Retain important linked <a href="https://example.org/details">clinical details</a> and <span data-testid="webpage-citation-pill">CDC +2</span>.</p></li></ul></li></ol>';
 document.body.append(div);const blocks=PearlsCapture.blocks(div);
 const doc=await PearlsWord.create({url:'https://chatgpt.com/c/test',messages:[{role:'assistant',blocks}]},{single:true,title:'List regression',templateBytes:new Uint8Array(template),profile});
 const zip=await JSZip.loadAsync(doc.bytes),xml=await zip.file('word/document.xml').async('string');
 const parsed=new DOMParser().parseFromString(xml,'application/xml'),ns='http://schemas.openxmlformats.org/wordprocessingml/2006/main';
 return {bytes:[...doc.bytes],blocks,xml,paragraphs:[...parsed.getElementsByTagNameNS(ns,'p')].map(p=>({text:p.textContent,numbered:!!p.getElementsByTagNameNS(ns,'numPr').length,style:p.getElementsByTagNameNS(ns,'pStyle')[0]?.getAttributeNS(ns,'val')}))};
},{template:[...fs.readFileSync(path.join(root,'template/base.docx'))],profile:JSON.parse(fs.readFileSync(path.join(root,'template/profile.json')))});
assert(!JSON.stringify(result.blocks).includes('CDC'));assert(!result.xml.includes('w:hyperlink'));assert(!result.xml.includes('Source conversation'));
for(const label of ['Succimer (DMSA)','Severe poisoning or encephalopathy'])assert(result.paragraphs.some(p=>p.text===label&&p.numbered),label);
assert(!result.paragraphs.some(p=>p.numbered&&!p.text.trim()),'No empty numbered paragraphs');assert(result.xml.includes('clinical details'));assert(result.xml.includes('Retain follow-up text.'));
const out=path.resolve(root,'../../build/chat-word-qa');fs.mkdirSync(out,{recursive:true});fs.writeFileSync(path.join(out,'list-citations.docx'),Buffer.from(result.bytes));console.log('PASS: numbered bold labels and headings stay with markers; citation chips, source labels and hyperlinks omitted; clinical prose and nested lists retained');
}finally{await browser.close();}})().catch(e=>{console.error(e);process.exit(1)});
