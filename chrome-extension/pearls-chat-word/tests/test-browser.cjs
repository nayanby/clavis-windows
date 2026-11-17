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
  const browser = await chromium.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe', headless: true, args: ['--disable-background-networking', '--no-first-run'] });
  try {
    const page = await browser.newPage();
    const errors = []; page.on('pageerror', error => errors.push(error.message));
    await page.route('**/*', route => route.fulfill({ contentType: 'text/html', body: fs.readFileSync(path.join(__dirname, 'fixtures/chatgpt.html'), 'utf8') }));
    await page.goto('https://chatgpt.com/c/test-fixture');
    await page.addScriptTag({ path: path.join(root, 'capture.js') });
    const chat = await page.evaluate(() => PearlsCapture.snapshot());
    assert.equal(chat.messages.length, 6);
    assert.equal(chat.messages.filter(m => m.role === 'assistant').length, 3);
    await page.evaluate(() => { globalThis.toolbarRequests=[]; globalThis.chrome={runtime:{sendMessage:async value=>{toolbarRequests.push(value);return {ok:true};}}}; });
    await page.addScriptTag({ path: path.join(root, 'page-toolbar.js') });
    assert.equal(await page.locator('[data-pearls-toolbar="chat"]').count(), 1);
    assert.equal(await page.locator('[data-pearls-toolbar="response"]').count(), 3);
    await page.evaluate(() => PearlsToolbar.render());
    assert.equal(await page.locator('[data-pearls-toolbar="response"]').count(), 3);
    await page.locator('[data-pearls-toolbar="response"]').first().getByRole('button').click();
    assert.equal(await page.evaluate(() => toolbarRequests[0].mode), 'single');
    assert.equal(await page.evaluate(() => toolbarRequests[0].id), 'a1');
    await page.locator('[data-pearls-toolbar="chat"]').getByRole('button',{name:'Download entire chat',exact:true}).click();
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
    assert.equal(await page.evaluate(() => {
      const a = { role: 'assistant', id: 'a', blocks: [] }, b = { role: 'user', id: 'b', blocks: [] }, c = { role: 'assistant', id: 'c', blocks: [] };
      return PearlsCapture.merge([a,b],[b,c]).map(x => x.id).join(',');
    }), 'a,b,c');
    assert.equal(await page.evaluate(() => { try { PearlsCapture.merge([{id:'a'}],[{id:'z'}]); return false; } catch { return true; } }), true);
    await page.addScriptTag({ path: path.join(root, 'vendor/jszip.min.js') });
    await page.addScriptTag({ path: path.join(root, 'word-export.js') });
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
        return { bytes: [...doc.bytes], xml, numbers, paragraphs, warnings: doc.warnings };
      }, { chat, messages, single, includePrompts, template, profile });
      assert(result.xml.includes('Bone marrow'));
      assert(result.xml.includes('Sole Subsection'));
      assert(!result.paragraphs.includes('A. Sole Subsection'));
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
      assert.equal(await page.locator('[data-pearls-toolbar="response"]').count(),1);
      assert.equal(await page.locator('[data-pearls-toolbar="chat"]').count(),1);
    }
    // Exercise the exporter controller and automatic toolbar download path.
    const exporter = await browser.newPage({viewport:{width:1100,height:950}});
    exporter.on('pageerror',error=>errors.push(error.message));
    await exporter.addInitScript(data => {
      globalThis.mockDownloads=[];
      globalThis.chrome={
        runtime:{getURL:file=>location.origin+'/'+file},
        scripting:{executeScript:async options=> {
          if(options.files)return [];
          const value=structuredClone(data);
          if(options.args[0]==='single')value.messages=[value.messages.filter(m=>m.role==='assistant')[options.args[1]]];
          return [{result:{value}}];
        }},
        downloads:{download:async options=>{const bytes=[...new Uint8Array(await(await fetch(options.url)).arrayBuffer())];mockDownloads.push({...options,bytes});return mockDownloads.length;},onChanged:{addListener(){},removeListener(){}}}
      };
    },chat);
    await exporter.route('**/*',route=>{
      const name=new URL(route.request().url()).pathname.slice(1)||'exporter.html';
      const file=path.join(root,name);
      const types={'.html':'text/html','.js':'text/javascript','.css':'text/css','.json':'application/json','.png':'image/png','.docx':'application/vnd.openxmlformats-officedocument.wordprocessingml.document'};
      if(!file.startsWith(root+path.sep)||!fs.existsSync(file))return route.fulfill({status:404,body:''});
      return route.fulfill({contentType:types[path.extname(file)]||'application/octet-stream',headers:{'Content-Security-Policy':"script-src 'self'; object-src 'none'"},body:fs.readFileSync(file)});
    });
    await exporter.goto('https://pearls.test/exporter.html?tab=42&mode=single&responseId=a1&index=0');
    await exporter.waitForFunction(()=>mockDownloads.length===1);
    assert.equal(await exporter.locator('#response').inputValue(),'0');
    assert.equal(await exporter.evaluate(()=>mockDownloads[0].filename),'Immunology Pearls - Response 1.docx');
    const uiDoc=await exporter.evaluate(()=>mockDownloads[0].bytes);
    fs.writeFileSync(path.join(output,'toolbar-response.docx'),Buffer.from(uiDoc));
    await exporter.screenshot({path:path.join(output,'exporter-ui.png'),fullPage:true});
    await exporter.goto('https://pearls.test/exporter.html?tab=42&mode=all');
    await exporter.waitForFunction(()=>mockDownloads.length===1);
    assert.equal(await exporter.evaluate(()=>mockDownloads[0].filename),'Immunology Pearls.docx');
    await exporter.close();
    assert.deepEqual(errors, []);
    console.log('PASS: automatic response/chat toolbars, click targets, all three adapters, full-chat traversal, repeated turns, response-only export, headings, equations, nested/restarted lists, image packaging, merged tables and escaping.');
    console.log('QA documents: ' + output);
  } finally { await browser.close(); }
}
run().catch(error => { console.error(error); process.exitCode = 1; });
