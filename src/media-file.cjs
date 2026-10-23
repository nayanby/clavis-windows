const fs=require('node:fs/promises');
const {createReadStream}=require('node:fs');
const {Readable}=require('node:stream');
const path=require('node:path');
const types={'.mp3':'audio/mpeg','.m4a':'audio/mp4','.m4b':'audio/mp4','.mp4':'audio/mp4','.wav':'audio/wav','.flac':'audio/flac','.ogg':'audio/ogg','.opus':'audio/ogg','.aac':'audio/aac','.pdf':'application/pdf','.epub':'application/epub+zip','.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.webp':'image/webp'};
function byteRange(value,size){
  if(!value)return null;
  const m=/^bytes=(\d*)-(\d*)$/.exec(value.trim());
  if(!m||(!m[1]&&!m[2])||size===0)return false;
  let start,end;
  if(!m[1]){const length=Number(m[2]);if(!Number.isSafeInteger(length)||length<=0)return false;start=Math.max(0,size-length);end=size-1;}
  else{start=Number(m[1]);end=m[2]?Math.min(Number(m[2]),size-1):size-1;}
  return Number.isSafeInteger(start)&&Number.isSafeInteger(end)&&start>=0&&start<size&&end>=start?{start,end}:false;
}
async function serveFile(file,request){
  let stat;try{stat=await fs.stat(file);}catch{return new Response('File unavailable',{status:404});}
  if(!stat.isFile())return new Response('Not a file',{status:404});
  const headers=new Headers({'Content-Type':types[path.extname(file).toLowerCase()]||'application/octet-stream','Accept-Ranges':'bytes','Access-Control-Allow-Origin':'*','Access-Control-Expose-Headers':'Content-Range, Content-Length, Accept-Ranges'});
  const range=byteRange(request.headers.get('range'),stat.size);
  if(range===false){headers.set('Content-Range',`bytes */${stat.size}`);return new Response(null,{status:416,headers});}
  const start=range?.start||0,end=range?.end??stat.size-1;
  headers.set('Content-Length',String(Math.max(0,end-start+1)));
  if(range)headers.set('Content-Range',`bytes ${start}-${end}/${stat.size}`);
  const body=request.method==='HEAD'||!stat.size?null:Readable.toWeb(createReadStream(file,{start,end}));
  return new Response(body,{status:range?206:200,headers});
}
module.exports={byteRange,serveFile};
