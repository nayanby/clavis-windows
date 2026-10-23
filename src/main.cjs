const {app,BrowserWindow,ipcMain,dialog,shell,protocol,net,screen}=require('electron');
app.setAppUserModelId('com.clavis.reader.windows');
const fs=require('node:fs/promises'),path=require('node:path'),crypto=require('node:crypto');
const fsSync=require('node:fs');
const {pathToFileURL}=require('node:url');
const Parser=require('rss-parser');
const {parseXML}=require('./feed.cjs');
const {JSDOM}=require('jsdom');
const {Readability}=require('@mozilla/readability');
const {idFor,titleFor,kindFor,scanFolder,progressPatch,atomicWrite}=require('./library.cjs');
const {request,publicURL}=require('./network.cjs');
const {serveFile}=require('./media-file.cjs');
const {discoverChapters,normalizeMarkers,remapPosition}=require('./chapters.cjs');
const {ChapterScans}=require('./chapter-scan.cjs');
const {organizeBook,uniqueFolder,folderName,migrateStorage,removeMigratedFiles}=require('./storage.cjs');
protocol.registerSchemesAsPrivileged(['clavis-media','clavis-app'].map(scheme=>({scheme,privileges:{standard:true,secure:true,supportFetchAPI:true,stream:true,corsEnabled:true}})));
const appFolder=app.isPackaged?path.dirname(process.execPath):path.resolve(__dirname,'..');
const dataFolder=process.env.CLAVIS_DATA_DIR?path.resolve(process.env.CLAVIS_DATA_DIR):path.join(appFolder,'Data');
const chapterScans=new ChapterScans(app.isPackaged?path.join(process.resourcesPath,'ffmpeg.exe'):path.resolve(__dirname,'../node_modules/ffmpeg-static/ffmpeg.exe'));
for(const sub of ['', 'Session','Logs','CrashDumps','Books'])fsSync.mkdirSync(path.join(dataFolder,sub),{recursive:true});
app.setPath('userData',dataFolder);
app.setPath('sessionData',path.join(dataFolder,'Session'));
app.setPath('crashDumps',path.join(dataFolder,'CrashDumps'));
app.setAppLogsPath(path.join(dataFolder,'Logs'));
let win,store,storeFile,saveQueue=Promise.resolve(),torrentClient;
const media=new Map(),tokens=new Map(),jobs=new Map();
const parser=new Parser({customFields:{item:[['media:content','media'],['media:thumbnail','thumbnail'],['content:encoded','contentEncoded']]}});
const feedKinds=new Set(['News','Podcasts','Journals']);
const assets=path.join(__dirname,'../assets');
function save(){const snapshot=structuredClone(store);saveQueue=saveQueue.catch(()=>{}).then(()=>atomicWrite(storeFile,snapshot));return saveQueue;}
function mediaURL(p){if(!p)return null;if(!tokens.has(p)){const t=crypto.randomBytes(24).toString('hex');tokens.set(p,t);media.set(t,p);}return `clavis-media://item/${tokens.get(p)}`;}
function bookView(b){return {...b,source:undefined,cover:b.remoteCover|| (b.cover?mediaURL(b.cover):null),url:b.path?mediaURL(b.path):undefined,path:undefined,tracks:b.tracks?.map(t=>({...t,path:undefined,url:mediaURL(t.remote||t.path)}))};}
function stateView(){return {books:store.books.map(bookView),settings:store.settings,notes:store.notes};}
function book(id){const b=store.books.find(b=>b.id===id);if(!b)throw Error('This book is no longer in the library.');return b;}
async function metadata(b){
  try{const found=await discoverChapters(b);Object.assign(b,found.book);const m=found.metadata;if(!m)return b;
    if(new Set(b.tracks.map(t=>t.path)).size===1&&m.common.title)b.title=m.common.album||m.common.title;
    b.author=m.common.artist||'';
    if(!b.cover&&m.common.picture?.[0]){const p=m.common.picture[0];if(p.data.length<10*1024*1024){const out=path.join(app.getPath('userData'),'covers',b.id+(p.format.includes('png')?'.png':'.jpg'));await fs.mkdir(path.dirname(out),{recursive:true});await fs.writeFile(out,p.data);b.cover=out;}}
  }catch{}return b;
}
async function addBooks(items){for(const b of items){if(store.books.some(x=>x.id===b.id))continue;await organizeBook(b,path.join(dataFolder,'Books'));if(b.kind==='Audio')await metadata(b);store.books.push(b);}await save();return stateView();}
function parseFeed(f,parsed){
  const entries=(parsed.items||[]).slice(0,300).map((e,i)=>({id:idFor(f.id+':'+(e.guid||e.link||i)),title:e.title||'Untitled',link:e.link||'',date:e.isoDate||e.pubDate||'',content:e.contentEncoded||e['content:encoded']||e.content||e.summary||e.contentSnippet||'',audio:e.enclosure?.url||'',enclosure:e.enclosure||null,image:e.itunes?.image||e.thumbnail?.$?.url||e.media?.$?.url||'',duration:e.itunes?.duration||''}));
  return {...f,title:parsed.title||f.title,image:parsed.itunes?.image||parsed.image?.url||'',description:parsed.description||'',entries,updated:Date.now()};
}
const feedRequests=new Map();
async function refreshFeed(f){const r=await request(f.url);const parsed=parseXML(r.text);const refreshed=parseFeed(f,parsed);refreshed.entries.sort((a,b)=>(Date.parse(b.date)||0)-(Date.parse(a.date)||0));return refreshed;}
async function refreshStoredFeed(id){
  if(feedRequests.has(id))return feedRequests.get(id);
  const work=(async()=>{const source=store.feeds.find(f=>f.id===id);if(!source)throw Error('Source not found');
    try{const fresh=await refreshFeed(source);const index=store.feeds.findIndex(f=>f.id===id);if(index>=0){store.feeds[index]={...fresh,lastAttempt:Date.now(),refreshError:null};await save();}return {...fresh,refreshError:null};}
    catch(e){const current=store.feeds.find(f=>f.id===id);if(current){current.lastAttempt=Date.now();current.refreshError=e.message;await save();}throw e;}
  })();feedRequests.set(id,work);try{return await work;}finally{feedRequests.delete(id);}
}
async function seed(){const catalog=JSON.parse(await fs.readFile(path.join(assets,'rss/catalog.json'),'utf8'));store.directory=catalog;for(const f of catalog.filter(f=>f.preload)){try{const raw=await fs.readFile(path.join(assets,f.asset),'utf8');const data=parseFeed({id:idFor(f.url),kind:f.kind,url:f.url,title:f.title},parseXML(raw));data.updated=null;store.feeds.push(data);}catch(e){console.warn('Cannot seed',f.title,e.message);}}}
function handle(name,fn){ipcMain.handle(name,async(e,...args)=>{if(!win||e.sender!==win.webContents||e.senderFrame!==win.webContents.mainFrame)throw Error('Access denied');return fn(...args);});}
function downloadsView(){return [...jobs.values()].map(j=>({id:j.id,title:j.title,status:j.status,error:j.error,progress:j.status==='Complete'?1:(j.torrent?.progress||j.progress||0),speed:j.torrent?.downloadSpeed||0,peers:j.torrent?.numPeers||0,downloaded:j.torrent?.downloaded||0,total:j.torrent?.length||0}));}
function broadcast(){if(win&&!win.isDestroyed())win.webContents.send('downloads:changed',downloadsView());}
async function client(){if(!torrentClient){const {default:WebTorrent}=await import('webtorrent');torrentClient=new WebTorrent({utp:false});torrentClient.on('error',e=>{for(const j of jobs.values())if(j.status==='Downloading'){j.status='Error';j.error=e.message;}broadcast();});}return torrentClient;}
async function startTorrent(j){const c=await client();return new Promise((resolve,reject)=>{const t=c.add(j.magnet,{path:j.dir},()=>{j.title=t.name;j.status='Downloading';broadcast();resolve();});j.torrent=t;t.on('error',e=>{j.status='Error';j.error=e.message;broadcast();reject(e);});t.on('done',async()=>{j.status='Importing';try{const files=t.files.map(f=>f.path);await new Promise(r=>t.destroy({destroyStore:false},r));j.torrent=null;j.progress=1;if(path.basename(j.dir)!==folderName(j.title)){const destination=await uniqueFolder(path.join(dataFolder,'Books'),j.title);await fs.rmdir(destination);await fs.rename(j.dir,destination);j.dir=destination;}const audio=await scanFolder(j.dir),docs=[];for(const f of files){const file=path.join(j.dir,f),kind=kindFor(file);if(kind&&kind!=='Audio')docs.push({id:idFor(file),title:titleFor(file),path:file,source:file,kind,position:0,progress:0,bookmarks:[],lastActive:0});}await addBooks([...audio,...docs]);j.status='Complete';}catch(e){j.status='Error';j.error=e.message;}await saveJobs();broadcast();});setTimeout(()=>resolve(),1000);});}
async function saveJobs(){store.downloads=[...jobs.values()].map(j=>({id:j.id,title:j.title,magnet:j.magnet,dir:j.dir,status:j.status}));await save();}
async function init(){
  storeFile=path.join(app.getPath('userData'),'library.json');
  try{store=JSON.parse(await fs.readFile(storeFile,'utf8'));if(!Array.isArray(store.books)||!Array.isArray(store.feeds))throw Error('Invalid library');}
  catch(e){if(e.code!=='ENOENT'){await fs.copyFile(storeFile,storeFile+'.recovery-'+Date.now()).catch(()=>{});}store={books:[],feeds:[],settings:{theme:'system',fontSize:19,lineHeight:1.7,margin:32,skip:30,volume:0.8,speed:1},notes:[],downloads:[]};await seed();await save();}
  store.notes||=[];store.downloads||=[];
  if(store.dataRoot&&store.dataRoot!==dataFolder){const previous=path.resolve(store.dataRoot)+path.sep;const rebase=p=>typeof p==='string'&&p.toLowerCase().startsWith(previous.toLowerCase())?path.join(dataFolder,path.relative(store.dataRoot,p)):p;for(const b of store.books){for(const key of ['path','source','cover'])if(b[key])b[key]=rebase(b[key]);for(const t of b.tracks||[])if(t.path)t.path=rebase(t.path);}for(const j of store.downloads)j.dir=rebase(j.dir);}
  store.dataRoot=dataFolder;const migrated=await migrateStorage(store,dataFolder);await save();await removeMigratedFiles(migrated,dataFolder);
  protocol.handle('clavis-app',async req=>{const u=new URL(req.url),rel=decodeURIComponent(u.pathname).replace(/^\/+/,''),root=path.resolve(__dirname,'..'),file=path.resolve(root,rel);if(u.hostname!=='desktop'||!['ui','assets'].includes(rel.split('/')[0])||!file.startsWith(root+path.sep))return new Response('Not found',{status:404});const response=await net.fetch(pathToFileURL(file).href);const headers=new Headers(response.headers);if(rel==='ui/vosk-worker.js')headers.set('Content-Security-Policy',"default-src 'none'; script-src 'self' 'unsafe-eval' 'wasm-unsafe-eval'; connect-src 'self' clavis-media:; worker-src 'none'");return new Response(response.body,{status:response.status,headers});});
  for(const j of store.downloads)jobs.set(j.id,{...j,status:j.status==='Complete'?'Complete':'Paused'});
  protocol.handle('clavis-media',async req=>{const u=new URL(req.url),file=media.get(u.pathname.slice(1));if(u.hostname!=='item'||!file)return new Response('Not found',{status:404});let response;if(/^https:/.test(file)){let remote=await publicURL(file);for(let n=0;n<6;n++){response=await net.fetch(remote.href,{headers:req.headers,redirect:'manual'});if(![301,302,303,307,308].includes(response.status))break;await response.body?.cancel();remote=await publicURL(new URL(response.headers.get('location'),remote));}}else return serveFile(file,req);const headers=new Headers(response.headers);headers.set('Access-Control-Allow-Origin','*');return new Response(response.body,{status:response.status,headers});});
  const displayArea=screen.getPrimaryDisplay().workArea;
  win=new BrowserWindow({width:Math.round(displayArea.width*.7),height:Math.round(displayArea.height*.7),minWidth:560,minHeight:360,fullscreen:false,maximizable:true,title:'Clavis',backgroundColor:'#FAF9FD',icon:path.join(assets,'icon.ico'),show:false,webPreferences:{zoomFactor:.8,preload:path.join(__dirname,'preload.cjs'),nodeIntegration:false,contextIsolation:true,sandbox:true,webSecurity:true,spellcheck:true}});
  win.removeMenu();win.once('ready-to-show',()=>win.show());
  win.on('closed',()=>chapterScans.close());
  win.webContents.setWindowOpenHandler(()=>({action:'deny'}));
  win.webContents.on('will-navigate',(e,url)=>{if(url!=='clavis-app://desktop/ui/index.html')e.preventDefault();});
  win.webContents.session.setPermissionRequestHandler((_,__,cb)=>cb(false));
  handle('state:load',stateView);
  handle('audio:prepare',async(id,force=false)=>{const b=book(id);if(b.kind!=='Audio')return bookView(b);if(force||!b.chaptersVersion){await metadata(b);await save();}return bookView(b);});
  handle('audio:scan-start',id=>{const b=book(id);if(b.kind!=='Audio')throw Error('Choose a local audiobook.');return chapterScans.start(b);});
  handle('audio:scan-read',id=>chapterScans.read(id));handle('audio:scan-cancel',id=>chapterScans.cancel(id));
  handle('audio:apply-spoken',async(id,markers)=>{const b=book(id),files=[...new Set(b.tracks.map(t=>t.path))],old=b.tracks,tracks=[];if(!Array.isArray(markers)||markers.length>3000)throw Error('Invalid chapter results');for(let i=0;i<files.length;i++){const file=files[i],existing=old.filter(t=>t.path===file),duration=Math.max(...existing.map(t=>t.end||t.duration||0));const raw=markers.filter(m=>m.fileIndex===i&&Number.isFinite(m.start)&&m.start>=0).map(m=>({start:m.start,title:String(m.title||'Chapter').slice(0,200)}));const normalized=normalizeMarkers(raw,duration);if(normalized.length)tracks.push(...normalized.map(m=>({...m,path:file,spoken:true})));else tracks.push(...existing);}const mapped=remapPosition(old,b.chapter,b.position,tracks);b.bookmarks=(b.bookmarks||[]).map(m=>({...m,...remapPosition(old,m.chapter,m.position,tracks)}));b.tracks=tracks;Object.assign(b,mapped);b.chaptersVersion=1;await save();return bookView(b);});
  handle('library:import',async kind=>{if(!['EPUB','PDF','Audio','All'].includes(kind))throw Error('Unsupported library');const extensions=kind==='EPUB'?['epub']:kind==='PDF'?['pdf']:kind==='Audio'?['mp3','m4a','m4b','ogg','wav','flac','opus','aac']:['epub','pdf','mp3','m4a','m4b','ogg','wav','flac','opus','aac'];const r=await dialog.showOpenDialog(win,{title:'Import into Clavis',properties:['openFile','multiSelections'],filters:[{name:'Books and audio',extensions}]});if(r.canceled)return null;const items=r.filePaths.filter(p=>kindFor(p)).map(p=>{const k=kindFor(p);return {id:idFor(p),title:titleFor(p),kind:k,...(k==='Audio'?{tracks:[{path:p,title:titleFor(p)}],chapter:0}:{path:p}),source:p,position:0,progress:0,bookmarks:[],lastActive:0};});return addBooks(items);});
  handle('library:folder',async()=>{const r=await dialog.showOpenDialog(win,{title:'Import an audiobook or library folder',properties:['openDirectory']});if(r.canceled)return null;return addBooks(await scanFolder(r.filePaths[0]));});
  handle('library:update',async(id,p)=>{const b=book(id);Object.assign(b,progressPatch(p));await save();return bookView(b);});
  handle('library:remove',async id=>{book(id);store.books=store.books.filter(b=>b.id!==id);await save();return stateView();});
  handle('library:delete',async id=>{const b=book(id);const r=await dialog.showMessageBox(win,{type:'warning',title:'Move book files to Recycle Bin?',message:`Move “${b.title}” to the Recycle Bin?`,detail:'Only its document or chapter files will be moved. Folders and shared files are kept.',buttons:['Cancel','Move to Recycle Bin'],defaultId:0,cancelId:0});if(r.response!==1)return null;const files=b.tracks?b.tracks.map(t=>t.path):[b.path];for(const file of new Set(files)){const shared=store.books.some(x=>x.id!==id&&(x.path===file||x.tracks?.some(t=>t.path===file)));if(!shared)await shell.trashItem(file);}store.books=store.books.filter(x=>x.id!==id);await save();return stateView();});
  handle('settings:update',async p=>{for(const k of ['fontSize','lineHeight','margin','skip','volume','speed'])if(Number.isFinite(p[k])){const limits={fontSize:[10,40],lineHeight:[1,3],margin:[0,100],skip:[5,120],volume:[0,1],speed:[.5,3]}[k];store.settings[k]=Math.max(limits[0],Math.min(limits[1],p[k]));}if(['light','dark','system'].includes(p.theme))store.settings.theme=p.theme;await save();return store.settings;});
  handle('feeds:list',()=>({feeds:store.feeds,directory:store.directory||[]}));
  handle('feeds:add',async(kind,url)=>{if(!feedKinds.has(kind))throw Error('Invalid feed category');await publicURL(url);if(store.feeds.some(f=>f.url===url&&f.kind===kind))return store.feeds;const f=await refreshFeed({id:idFor(kind+url),kind,url});store.feeds.push(f);await save();return store.feeds;});
  handle('feeds:refresh',refreshStoredFeed);
  handle('feeds:remove',async id=>{store.feeds=store.feeds.filter(f=>f.id!==id);await save();return store.feeds;});
  handle('feeds:play',async(feedId,entryId)=>{const f=store.feeds.find(f=>f.id===feedId),e=f?.entries.find(e=>e.id===entryId);if(!e?.audio)throw Error('This episode has no audio enclosure.');await publicURL(e.audio);let b=store.books.find(b=>b.id===e.id);if(!b){b={id:e.id,title:e.title,author:f.title,kind:'Podcast',remoteCover:e.image||f.image,tracks:[{remote:e.audio,title:e.title}],chapter:0,position:0,progress:0,bookmarks:[],lastActive:0};store.books.push(b);await save();}return bookView(b);});
  handle('reader:ink',async id=>{book(id);try{return JSON.parse(await fs.readFile(path.join(app.getPath('userData'),'ink',id+'.json'),'utf8'));}catch{return {};}});
  handle('reader:save-ink',async(id,ink)=>{book(id);const json=JSON.stringify(ink);if(json.length>8*1024*1024)throw Error('Annotation limit reached for this book.');await atomicWrite(path.join(app.getPath('userData'),'ink',id+'.json'),ink);return true;});
  handle('audio:transcript',async id=>{book(id);try{return JSON.parse(await fs.readFile(path.join(app.getPath('userData'),'transcripts',id+'.json'),'utf8'));}catch{return {};}});
  handle('audio:save-transcript',async(id,data)=>{book(id);if(JSON.stringify(data).length>12*1024*1024)throw Error('Transcript cache limit reached.');await atomicWrite(path.join(app.getPath('userData'),'transcripts',id+'.json'),data);return true;});
  handle('article:read',async url=>{const r=await request(url);const dom=new JSDOM(r.text,{url:r.url});try{const article=new Readability(dom.window.document).parse();if(!article)throw Error('No readable article found.');return {title:article.title,content:article.content,byline:article.byline,url:r.url};}finally{dom.window.close();}});
  handle('system:open',async url=>{const u=new URL(url);if(!['https:','http:'].includes(u.protocol))throw Error('Only web links can be opened');await shell.openExternal(u.href);});
  handle('system:files',async()=>shell.openPath(path.join(dataFolder,'Books')));
  handle('notes:save',async n=>{const note={id:typeof n.id==='string'?n.id:crypto.randomUUID(),title:String(n.title||'Untitled').slice(0,300),text:String(n.text||'').slice(0,2000000),drawing:Array.isArray(n.drawing)&&JSON.stringify(n.drawing).length<4000000?n.drawing:[],updated:Date.now()};const i=store.notes.findIndex(x=>x.id===note.id);if(i<0)store.notes.unshift(note);else store.notes[i]=note;await save();return note;});
  handle('notes:delete',async id=>{store.notes=store.notes.filter(n=>n.id!==id);await save();return store.notes;});
  handle('notes:export',async id=>{const n=store.notes.find(n=>n.id===id);if(!n)throw Error('Note not found');const r=await dialog.showSaveDialog(win,{defaultPath:n.title.replace(/[<>:"/\\|?*]/g,'_')+'.txt',filters:[{name:'Text',extensions:['txt']}]});if(!r.canceled)await fs.writeFile(r.filePath,n.title+'\n\n'+n.text);return !r.canceled;});
  handle('notes:export-drawing',async(id,png)=>{const n=store.notes.find(n=>n.id===id);if(!n)throw Error('Note not found');if(typeof png!=='string'||!png.startsWith('data:image/png;base64,')||png.length>12000000)throw Error('Invalid drawing');const r=await dialog.showSaveDialog(win,{defaultPath:n.title.replace(/[<>:"/\\|?*]/g,'_')+'.png',filters:[{name:'PNG image',extensions:['png']}]});if(!r.canceled)await fs.writeFile(r.filePath,Buffer.from(png.slice(22),'base64'));return !r.canceled;});
  handle('downloads:list',downloadsView);
  handle('downloads:add',async value=>{const magnet=String(value).trim().replace(/&amp;/g,'&');if(!/^magnet:\?/i.test(magnet)||!new URLSearchParams(magnet.slice(8)).getAll('xt').some(x=>/^urn:btih:([a-f0-9]{40}|[a-z2-7]{32})$/i.test(x)))throw Error('Paste a valid BitTorrent magnet link.');const id=idFor(magnet);if(jobs.has(id))return downloadsView();const dir=await uniqueFolder(path.join(dataFolder,'Books'),new URLSearchParams(magnet.slice(8)).get('dn')||'New download');const j={id,magnet,dir,title:new URLSearchParams(magnet.slice(8)).get('dn')||'Finding audiobook metadata…',status:'Finding peers'};jobs.set(id,j);await saveJobs();startTorrent(j).catch(e=>{j.status='Error';j.error=e.message;broadcast();});return downloadsView();});
  handle('downloads:action',async(id,action)=>{const j=jobs.get(id);if(!j)throw Error('Download not found');if(action==='open')return shell.openPath(j.dir);if(action==='pause'){j.torrent?.pause();j.status='Paused';}else if(action==='resume'){if(j.torrent){j.torrent.resume();j.status='Downloading';}else await startTorrent(j);}else if(action==='remove'){if(j.torrent)await new Promise(resolve=>j.torrent.destroy({destroyStore:false},resolve));jobs.delete(id);}await saveJobs();broadcast();return downloadsView();});
  await win.loadURL('clavis-app://desktop/ui/index.html');
  setInterval(broadcast,1500).unref();
}
app.whenReady().then(init).catch(e=>{dialog.showErrorBox('Clavis could not start',e.stack||e.message);app.quit();});
app.on('window-all-closed',()=>app.quit());
let quitting=false;app.on('before-quit',e=>{if(quitting)return;e.preventDefault();quitting=true;saveQueue.finally(()=>{if(torrentClient)torrentClient.destroy(()=>app.quit());else app.quit();});});
