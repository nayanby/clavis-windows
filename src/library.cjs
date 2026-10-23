const fs = require('node:fs/promises');
const path = require('node:path');
const crypto = require('node:crypto');
const AUDIO = new Set(['.mp3', '.m4a', '.m4b', '.ogg', '.wav', '.flac', '.opus', '.aac']);
const natural = (a,b) => a.localeCompare(b, undefined, { numeric:true, sensitivity:'base' });
const idFor = p => crypto.createHash('sha256').update(path.resolve(p).toLowerCase()).digest('hex').slice(0,24);
const titleFor = p => path.basename(p, path.extname(p)).replace(/[_]/g, ' ');
function kindFor(p) { const e=path.extname(p).toLowerCase(); return AUDIO.has(e)?'Audio':e==='.epub'?'EPUB':e==='.pdf'?'PDF':null; }
async function scanFolder(root) {
  const groups = new Map(); let count = 0;
  async function walk(dir, depth=0) {
    if(depth>20) throw Error('Folder nesting is too deep. Select a smaller folder.');
    const files=await fs.readdir(dir,{withFileTypes:true});
    for(const f of files) {
      if(++count>50000) throw Error('This folder is too large. Select a smaller audiobook folder.');
      const p=path.join(dir,f.name);
      if(f.isDirectory() && !f.name.startsWith('.')) await walk(p,depth+1);
      else if(f.isFile() && AUDIO.has(path.extname(p).toLowerCase())) {
        const group=/^(cd|disc|disk)[\s_-]*\d+$/i.test(path.basename(dir))?path.dirname(dir):dir;
        if(!groups.has(group))groups.set(group,[]);groups.get(group).push(p);
      }
    }
  }
  await walk(root);
  const books=[];
  for(const [dir, tracks] of groups) {
    tracks.sort(natural);
    const covers=(await fs.readdir(dir)).filter(f=>/\.(jpg|jpeg|png|webp)$/i.test(f));
    covers.sort((a,b)=>Number(!/^(cover|folder|front)\./i.test(a))-Number(!/^(cover|folder|front)\./i.test(b)));
    books.push({id:idFor(dir),kind:'Audio',title:path.basename(dir),source:dir,tracks:tracks.map(p=>({path:p,title:titleFor(p)})),cover:covers[0]?path.join(dir,covers[0]):null,chapter:0,position:0,progress:0,bookmarks:[],lastActive:0});
  }
  return books.sort((a,b)=>natural(a.title,b.title));
}
function progressPatch(p) {
  const out={};
  for(const key of ['position','progress','chapter','page','speed']) if(Number.isFinite(p[key]) && p[key]>=0) out[key]=p[key];
  if(typeof p.cfi==='string'&&p.cfi.length<4096)out.cfi=p.cfi;
  if(Array.isArray(p.highlights))out.highlights=p.highlights.slice(0,2000).filter(x=>typeof x==='string'&&x.length<4096);
  if(Array.isArray(p.bookmarks))out.bookmarks=p.bookmarks.slice(0,1000).map(b=>({name:String(b.name||'Bookmark').slice(0,200),chapter:Math.max(0,Math.floor(Number(b.chapter)||0)),position:Math.max(0,Number(b.position)||0),page:Math.max(1,Math.floor(Number(b.page)||1)),cfi:String(b.cfi||'').slice(0,4096)}));
  out.lastActive=Date.now();return out;
}
async function atomicWrite(file,value) {
  await fs.mkdir(path.dirname(file),{recursive:true});
  await fs.writeFile(file+'.tmp',JSON.stringify(value,null,2));
  for(let attempt=0;;attempt++){
    try{await fs.rename(file+'.tmp',file);break;}
    catch(e){if(!['EPERM','EBUSY','EACCES'].includes(e.code)||attempt>=5)throw e;await new Promise(r=>setTimeout(r,50*(attempt+1)));}
  }
}
module.exports={AUDIO,natural,idFor,titleFor,kindFor,scanFolder,progressPatch,atomicWrite};
