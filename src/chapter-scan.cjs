const {spawn}=require('node:child_process');
const crypto=require('node:crypto');
class ChapterScans{
  constructor(executable){this.executable=executable;this.sessions=new Map();}
  start(book){const files=[...new Set(book.tracks.map(t=>t.path).filter(Boolean))];if(!files.length)throw Error('No local audio files to scan.');const id=crypto.randomUUID(),session={id,bookId:book.id,files,index:0,decoder:null,error:'',samples:0};this.sessions.set(id,session);return {id,files:files.map((file,i)=>({index:i,title:book.tracks.find(t=>t.path===file)?.title||'Audio',duration:Math.max(...book.tracks.filter(t=>t.path===file).map(t=>t.end||t.duration||0))}))};}
  async read(id){const s=this.sessions.get(id);if(!s)throw Error('Chapter scan cancelled.');if(s.reading)throw Error('A scan chunk is already being read.');s.reading=true;try{
    if(s.index>=s.files.length)return {done:true};
    if(!s.decoder){const child=spawn(this.executable,['-nostdin','-hide_banner','-loglevel','error','-i',s.files[s.index],'-vn','-ac','1','-ar','16000','-f','f32le','pipe:1'],{windowsHide:true,stdio:['ignore','pipe','pipe']});s.decoder=child;s.iterator=child.stdout[Symbol.asyncIterator]();s.error='';s.samples=0;s.tail=Buffer.alloc(0);child.stderr.on('data',b=>{s.error=(s.error+b.toString()).slice(-4000);});s.exit=new Promise((resolve,reject)=>{child.once('error',reject);child.once('close',code=>code===0?resolve():reject(Error(s.error||'Audio decoder stopped.')));});s.exit.catch(()=>{});}
    const result=await s.iterator.next();if(result.done){await s.exit;const index=s.index;s.index++;s.decoder=null;return {fileDone:true,fileIndex:index,seconds:s.samples/16000};}
    const buffer=Buffer.concat([s.tail,result.value]),length=buffer.length-buffer.length%4;s.tail=buffer.subarray(length);s.samples+=length/4;return {fileIndex:s.index,pcm:new Uint8Array(buffer.subarray(0,length)),seconds:s.samples/16000};
  }finally{s.reading=false;}}
  cancel(id){const s=this.sessions.get(id);if(s){s.decoder?.kill();this.sessions.delete(id);}}
  close(){for(const id of this.sessions.keys())this.cancel(id);}
}
module.exports={ChapterScans};
