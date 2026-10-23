const fs=require('node:fs/promises');
async function neroChapters(file){
  const handle=await fs.open(file,'r');const out=[];
  try{
    const {size}=await handle.stat();
    const read=async(at,n)=>{const b=Buffer.alloc(n);const r=await handle.read(b,0,n,at);if(r.bytesRead!==n)throw Error('Truncated chapter metadata');return b;};
    async function atoms(from,end,depth=0){if(depth>6)return;let count=0;for(let at=from;at+8<=end&&count++<100000;){const h=await read(at,8);let length=h.readUInt32BE(0),header=8;const type=h.toString('latin1',4,8);if(length===1){if(at+16>end)return;const big=(await read(at+8,8)).readBigUInt64BE();if(big>BigInt(Number.MAX_SAFE_INTEGER))return;length=Number(big);header=16;}if(length===0)length=end-at;if(length<header||at+length>end)return;
      if(type==='moov'||type==='udta')await atoms(at+header,at+length,depth+1);
      else if(type==='chpl'&&length-header<=1024*1024){const b=await read(at+header,length-header);let p=b[0]===1?8:4;if(p<b.length){const count=b[p++];for(let i=0;i<count&&p+9<=b.length;i++){const start=Number(b.readBigUInt64BE(p))/10000000;p+=8;const n=b[p++];if(p+n>b.length)break;out.push({start,title:b.toString('utf8',p,p+n)});p+=n;}}}
      at+=length;
    }}
    await atoms(0,size);return out;
  }finally{await handle.close();}
}
function normalizeMarkers(raw,duration){
  const markers=new Map();
  for(const m of raw||[]){const start=m.sampleOffset!=null&&m.sampleRate?m.sampleOffset/m.sampleRate:m.start/(m.timeScale||1);if(Number.isFinite(start)&&start>=0&&(!Number.isFinite(duration)||start<duration))markers.set(start,{start,title:String(m.title||'Chapter')});}
  const sorted=[...markers.values()].sort((a,b)=>a.start-b.start);
  if(sorted.length&&sorted[0].start>2)sorted.unshift({start:0,title:'Opening'});else if(sorted.length)sorted[0].start=0;
  return sorted.map((m,i)=>({...m,end:sorted[i+1]?.start??duration,duration:(sorted[i+1]?.start??duration)-m.start}));
}
function remapPosition(oldTracks,oldChapter,position,tracks){const old=oldTracks[Math.min(oldChapter||0,oldTracks.length-1)];if(!old)return {chapter:0,position:0};const absolute=(old.start||0)+(position||0);let index=tracks.findIndex(t=>t.path===old.path&&(t.start||0)<=absolute&&(!Number.isFinite(t.end)||absolute<t.end));if(index<0)index=tracks.findIndex(t=>t.path===old.path);if(index<0)index=0;return {chapter:index,position:Math.max(0,absolute-(tracks[index]?.start||0))};}
async function discoverChapters(book){
  const {parseFile}=await import('music-metadata');const files=[...new Set(book.tracks.map(t=>t.path).filter(Boolean))],tracks=[];let firstMetadata;
  for(const file of files){const old=book.tracks.find(t=>t.path===file);let m;try{m=await parseFile(file,{duration:true,includeChapters:true});}catch{tracks.push({...old});continue;}firstMetadata||=m;
    let raw=m.format.chapters||[];if(!raw.length)try{raw=await neroChapters(file);}catch{}
    const sampleRate=m.format.sampleRate;const normalized=normalizeMarkers(raw.map(x=>({...x,sampleRate})),m.format.duration);
    if(normalized.length)tracks.push(...normalized.map(c=>({path:file,title:c.title,start:c.start,end:c.end,duration:c.duration,embedded:true})));
    else if(book.tracks.some(t=>t.path===file&&t.spoken))tracks.push(...book.tracks.filter(t=>t.path===file));
    else tracks.push({path:file,title:old.title,start:0,duration:m.format.duration});
  }
  if(!tracks.length)return {book,metadata:firstMetadata};
  const mapped=remapPosition(book.tracks,book.chapter,book.position,tracks);
  const bookmarks=(book.bookmarks||[]).map(mark=>({...mark,...remapPosition(book.tracks,mark.chapter,mark.position,tracks)}));
  return {book:{...book,tracks,...mapped,bookmarks,chaptersVersion:1},metadata:firstMetadata};
}
module.exports={neroChapters,normalizeMarkers,remapPosition,discoverChapters};
