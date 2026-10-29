const {test}=require('node:test');
const assert=require('node:assert/strict');
const {JSDOM}=require('jsdom');

test('reading width is capped and both views share Averia typography',async()=>{
  const {readingWidth,readingTheme,readingFontCSS}=await import('../src/reading-layout.mjs');
  assert.equal(readingWidth(undefined),20);
  assert.equal(readingWidth(30),20);
  assert.equal(readingWidth(2),8);
  assert.equal(readingWidth(14.5),14.5);
  assert.match(readingTheme({fontSize:24,lineHeight:2,margin:12}).body['font-family'],/Averia/);
  assert.equal(readingTheme({fontSize:24}).body['font-size'],'24px');
  assert.match(readingFontCSS('https://local/assets/'),/averia_serif_libre_bold_italic.ttf/);
});

test('narration highlights across formatting without flattening headings, emphasis or lists',async()=>{
  const {markSentences}=await import('../src/reading-layout.mjs');
  const {document}=new JSDOM('<body><h1>Chapter I</h1><p>Hello <em>beautiful</em> world.</p><ul><li>Next sentence.</li></ul></body>').window;
  const text='Chapter I\n\nHello beautiful world.\n\nNext sentence.';
  const groups=markSentences(document.body,text,{start:0,end:text.length,sentences:[[0,9],[11,33],[35,text.length]]});
  assert.equal(groups.length,3);
  assert.equal(groups[1].map(el=>el.textContent).join(''),'Hellobeautifulworld.');
  assert.equal(document.querySelector('em').textContent,'beautiful');
  assert.equal(document.querySelector('h1').textContent,'Chapter I');
  assert.equal(document.querySelectorAll('li').length,1);
});

test('highlight mapping handles soft hyphens, wrapped words and Unicode offsets',async()=>{
  const {markSentences}=await import('../src/reading-layout.mjs');
  const {document}=new JSDOM('<body><p>A\u00ad word split-\nword 😀.</p></body>').window;
  const text='A word splitword 😀.';
  const groups=markSentences(document.body,text,{start:0,end:Array.from(text).length,sentences:[[0,Array.from(text).length]]});
  assert.equal(groups.length,1);
  assert.equal(groups[0].length,1);
  assert.equal(document.body.textContent,'A\u00ad word split-\nword 😀.');
});
