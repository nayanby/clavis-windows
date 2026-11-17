const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const { chromium } = require('playwright');
const root = path.resolve(__dirname, '..');
const output = path.resolve(root, '../../build/chat-word-qa');
async function run() {
  const executable=process.env.PEARLS_TEST_BROWSER || chromium.executablePath();
  if(!fs.existsSync(executable)) {
    console.log('SKIP installed-extension smoke test: provide PEARLS_TEST_BROWSER pointing to Chromium or Chrome for Testing with unpacked-extension support. Fixture and exporter tests run separately.');
    return;
  }
  const context = await chromium.launchPersistentContext(path.join(output, 'extension-test-profile'), {
    executablePath: executable,
    headless: true, acceptDownloads: true, downloadsPath: path.join(output,'downloads'),
    ignoreDefaultArgs: ['--disable-extensions'],
    args: ['--disable-extensions-except=' + root, '--load-extension=' + root, '--no-first-run', '--disable-background-networking']
  });
  try {
    const worker = context.serviceWorkers()[0] || await context.waitForEvent('serviceworker', {timeout:15000});
    assert(worker.url().endsWith('/background.js'));
    const page = await context.newPage();
    const fixture = fs.readFileSync(path.join(__dirname, 'fixtures/chatgpt.html'), 'utf8');
    await context.route('https://chatgpt.com/**', route => route.fulfill({contentType:'text/html',body:fixture}));
    await page.goto('https://chatgpt.com/c/test-extension-fixture');
    assert.equal(await page.locator('[data-pearls-toolbar]').count(),0);
    const testTabId=await worker.evaluate(async()=>{const tabs=await chrome.tabs.query({});return tabs.find(tab=>tab.url?.includes('/c/test-extension-fixture')).id;});
    await worker.evaluate(async id=>{await chrome.scripting.executeScript({target:{tabId:id},files:['vendor/html2canvas.min.js','capture.js','page-toolbar.js']});},testTabId);
    await page.locator('[data-pearls-toolbar="chat"]').waitFor();
    assert.equal(await page.locator('[data-pearls-toolbar="response"]').count(),0);
    await page.screenshot({path:path.join(output,'chat-toolbars.png'),fullPage:true});
    const opened = context.waitForEvent('page');
    await page.locator('[data-pearls-toolbar="chat"]').getByRole('button',{name:'Download response',exact:true}).click();
    const exporter = await opened;
    await exporter.waitForLoadState('domcontentloaded');
    await exporter.waitForFunction(() => !document.getElementById('status').textContent.includes('Connecting') && document.getElementById('source').textContent.includes('ChatGPT'));
    await exporter.screenshot({path:path.join(output,'extension-exporter.png'),fullPage:true});
    await exporter.waitForFunction(() => /saved|prepared|cancelled|interrupted|Could|Error|failed/i.test(document.getElementById('status').textContent), {timeout:15000});
    const state = await exporter.locator('#status').innerText();
    assert(!/error|failed|could not|cannot|denied/i.test(state),state);
    const downloads = await worker.evaluate(() => chrome.downloads.search({limit:5,orderBy:['-startTime']}));
    const generated = downloads.find(item => item.byExtensionId === new URL(worker.url()).hostname);
    assert(generated,'No download was created by the extension.');
    assert(downloads.some(item => /Response 1\.docx$/.test(item.filename)),JSON.stringify(downloads.map(x=>x.filename)));
    console.log('PASS: installed MV3 extension, automatic toolbars, service-worker messaging, real tab capture and response download.');
    console.log('Exporter status: ' + state);
  } finally { await context.close(); }
}
run().catch(error=>{console.error(error);process.exitCode=1;});
