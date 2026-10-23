const {test}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs/promises'),path=require('node:path'),os=require('node:os');
const {scanFolder,kindFor,progressPatch,atomicWrite}=require('../src/library.cjs');
const {privateAddress,publicURL}=require('../src/network.cjs');
test('imports nested audio, combines discs, sorts chapter numbers, skips unrelated files',async()=>{
  const dir=await fs.mkdtemp(path.join(os.tmpdir(),'clavis-test-'));
  try{
    for(const sub of ['Book A/CD 1','Book A/CD 2','Book B'])await fs.mkdir(path.join(dir,sub),{recursive:true});
    for(const file of ['Book A/CD 1/Chapter 10.mp3','Book A/CD 1/Chapter 2.mp3','Book A/CD 2/Chapter 1.mp3','Book A/cover.jpg','Book B/Book.m4b','Book B/readme.txt'])await fs.writeFile(path.join(dir,file),'');
    const books=await scanFolder(dir);assert.equal(books.length,2);assert.equal(books[0].tracks.length,3);assert.match(books[0].tracks[0].path,/Chapter 2/);assert.match(books[0].cover,/cover.jpg$/);assert.equal(books[1].tracks.length,1);
  }finally{await fs.rm(dir,{recursive:true,force:true});}
});
test('progress changes cannot replace imported paths or identifiers',()=>{
  const p=progressPatch({path:'C:\\Windows\\secret',id:'other',position:42,cfi:'epubcfi(/6/2)',speed:1.5,page:-9,bookmarks:[{name:'hello',path:'secret'}]});
  assert.equal(p.path,undefined);assert.equal(p.id,undefined);assert.equal(p.page,undefined);assert.equal(p.position,42);assert.equal(p.bookmarks[0].path,undefined);
});
test('kind matching is case insensitive and rejects executable files',()=>{assert.equal(kindFor('Book.EPUB'),'EPUB');assert.equal(kindFor('Book.M4B'),'Audio');assert.equal(kindFor('book.exe'),null);});
test('atomic library replacement persists valid data',async()=>{const dir=await fs.mkdtemp(path.join(os.tmpdir(),'clavis-store-'));try{const file=path.join(dir,'library.json');await atomicWrite(file,{books:[1]});await atomicWrite(file,{books:[2]});assert.deepEqual(JSON.parse(await fs.readFile(file,'utf8')),{books:[2]});}finally{await fs.rm(dir,{recursive:true,force:true});}});
test('network guard rejects loopback, LAN, link-local and mapped IPv6 addresses',async()=>{for(const ip of ['127.0.0.1','10.1.2.3','172.16.4.2','192.168.1.1','169.254.169.254','::1','fd00::1','::ffff:127.0.0.1'])assert.equal(privateAddress(ip),true,ip);assert.equal(privateAddress('8.8.8.8'),false);await assert.rejects(()=>publicURL('https://127.0.0.1/'));await assert.rejects(()=>publicURL('file:///C:/Windows/win.ini'));});
