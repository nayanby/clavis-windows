import {readingWidth,readingTheme,readingFontCSS,themeCSS,markSentences} from './reading-layout.mjs';
import {illustration,illustrateEmptyStates,dialogArt} from './illustrations.js';
import {uiIcons as clavisIcons,transportIcon} from './ui-icons.js';
import ePub from 'epubjs';
import DOMPurify from 'dompurify';
import * as pdfjs from 'pdfjs-dist/build/pdf.mjs';
import {effects,transcribe,stopTranscription,finishTranscription,scanRecognizer} from './audio-tools.js';
import {spokenHeadings} from './spoken-headings.mjs';
import {trackStart,trackDuration,relativePosition,listeningProgress} from './playback.mjs';
pdfjs.GlobalWorkerOptions.workerSrc=new URL('./pdf.worker.mjs',location.href).href;
const api=window.clavis,$=id=>document.getElementById(id);
const categories=[
  ['EPUB','EPUB Books','Read at your own pace','home_epub.png','▤'],
  ['PDF','PDF Books','Read and annotate PDFs','home_pdf.png','▧'],
  ['Audio','Audio Books','Listen to your library','home_audiobooks.png','♬'],
  ['Kindle','Kindle','Sync your e-reader','home_epub.png','◈'],
  ['News','News','Your latest RSS stories','home_news.png','▥'],
  ['Podcasts','Podcasts','Listen to your shows','home_podcasts.png','◉'],
  ['Journals','Articles','Follow publications','home_articles.png','▱'],
  ['Journalling','Journalling','Type or write your thoughts','home_journals.png','✎']
];
let state={books:[],settings:{},notes:[]},feeds=[],directory=[],route='Home',query='',activeFeed=null,current=null,chapter=0,playerContext='Audio',reader=null,readerGeneration=0,toastTimer,sleepTimer,saveTimer,noteTimer,activeNote=null,downloadState=[];
let kindleDevice=null,kindleBooks=[],kindleScanning=false;
const kindleArtCache=new Map(),pdfThumbCache=new Map();
let ink={},inkTool='navigate',inkColor='#7971ae',inkWidth=3;
let transcriptVisible=false,transcriptData={},transcriptStatus='',equalizer=[0,0,0,0,0],voiceGain=1;
let audioLoading=false,audioGeneration=0,seekDragging=false,lastSeek=null,advancing=false;
const activeTrack=()=>current?.tracks?.[chapter];
const audioDuration=()=>trackDuration(activeTrack(),audio.duration);
const audioPosition=()=>relativePosition(activeTrack(),audio.currentTime,audio.duration);
const FEED_KINDS=['News','Podcasts','Journals'];
const FEED_TOPIC_WORDS={
  Medical:['health','medicin','clinical','patient','disease','cancer','hospital','surgery','vaccine','diabet','cardio','mental health','psychiatr','public health'],
  Technology:['software','computer','digital','artificial intelligence','cyber','android','linux','internet','technology','machine learning'],
  Science:['science','scientist','research','discovery','experiment'],
  Environment:['climate','environment','warming','ecolog','biodiversity','conservation','pollution','renewable','sustainab'],
  Business:['business','econom','finance','market','trade','investment','inflation'],
  Politics:['politic','election','government','parliament','congress','democra','policy'],
  India:['india','indian','delhi','mumbai','bengaluru','chennai'],
  World:['international','global','world','diploma'],
  Culture:['culture','artists','literature','music','cinema','history','museum'],
  Education:['education','school','teaching','student','learning','university'],
  'Social sciences':['sociolog','psycholog','society','inequality','humanities','social'],
  Engineering:['engineering','robot','manufactur','materials','infrastructure'],
  Mathematics:['mathematic','statistics','algorithm','geometry'],
  Physics:['physics','quantum','particle','relativity'],
  Chemistry:['chemistry','chemical','molecule','catalys'],
  Biology:['biology','genom','genetic','organism','microb','plant','protein'],
  Space:['space','astronom','planet','galaxy','cosmos','nasa','telescope']
};
let feedActivity={},feedView={},feedBrowseTopic='',feedPosts=[],feedRefreshingIds=new Set(),feedRefreshKind=null,feedRefreshQueue=new Map(),feedRedrawTimer=null,postObserver=null;
const FEED_TOPICS=Object.keys(FEED_TOPIC_WORDS);
const feedLocks=new Map(),postBodies=new Map();
let postDrag=null;
const feedLabel=kind=>kind==='Journals'?'Articles':kind;
const feedTab=kind=>feedView[kind]||'popular';
const feedTopics=kind=>state.settings?.feedTopics?.[kind]||[];
const feedOrder=kind=>state.settings?.feedOrder?.[kind]||'latest';
const feedKey=item=>item.audio||item.link||item.id;
const feedDateValue=value=>{const stamp=Date.parse(value||'');return Number.isFinite(stamp)?stamp:0;};
const feedWhen=value=>{const stamp=Date.parse(value||'');return Number.isFinite(stamp)?new Date(stamp).toLocaleString(undefined,{day:'numeric',month:'short',year:'numeric',hour:'numeric',minute:'2-digit'}):'';};
function feedStatus(feed){
  if(!feed)return '';
  if(feedRefreshingIds.has(feed.id))return 'Fetching latest stories…';
  if(feed.refreshError)return feed.entries?.length?'Saved stories · '+feed.refreshError:feed.refreshError;
  return feed.updated?'Updated '+new Date(feed.updated).toLocaleString():'Not fetched yet';
}
function feedTopicMatch(feed,item){
  const selected=feedTopics(feed.kind);
  if(!selected.length||feed.kind==='Podcasts')return true;
  const text=(plain(item.title)+' '+(item.summary||plain(item.content))).toLowerCase();
  return selected.some(topic=>(feed.tags||[]).includes(topic)||(FEED_TOPIC_WORDS[topic]||[]).some(word=>text.includes(word)));
}
function feedSourceMatches(feed){
  const selected=feedTopics(feed.kind);
  if(!selected.length||feed.kind==='Podcasts')return true;
  return (feed.tags||[]).some(tag=>selected.includes(tag))||(feed.entries||[]).some(item=>feedTopicMatch(feed,item));
}
function feedStream(kind){
  const seen=new Set(),rows=[];
  for(const feed of feeds){
    if(feed.kind!==kind)continue;
    let position=0;
    for(const item of feed.entries||[]){
      if(kind==='Podcasts'&&!item.audio)continue;
      if(!feedTopicMatch(feed,item))continue;
      const key=feedKey(item)||feed.url+item.title;
      if(seen.has(key))continue;
      seen.add(key);rows.push({feed,item,position:position++,opens:feedActivity[key]||0,time:feedDateValue(item.date)});
    }
  }
  if(feedOrder(kind)==='latest'&&kind!=='Podcasts')rows.sort((a,b)=>b.time-a.time||a.position-b.position);
  else rows.sort((a,b)=>b.opens-a.opens||a.position-b.position);
  return rows.slice(0,150);
}
function scheduleFeedRedraw(){
  if(feedRedrawTimer||!FEED_KINDS.includes(route))return;
  feedRedrawTimer=setTimeout(()=>{
    feedRedrawTimer=null;
    if(!FEED_KINDS.includes(route))return;
    if(document.querySelector('.post-reading'))return;
    const top=$('main').scrollTop;
    renderFeeds();
    $('main').scrollTop=top;
  },350);
}
function redrawFeeds(){scheduleFeedRedraw();}
async function fetchLatestFeed(id,notify=false){
  if(feedLocks.has(id))return feedLocks.get(id);
  const work=(async()=>{
    feedRefreshingIds.add(id);scheduleFeedRedraw();
    try{
      const fresh=await api.feedRefresh(id);
      const at=feeds.findIndex(f=>f.id===id);
      if(at>=0)feeds[at]=fresh;
      if(notify)toast('Latest stories fetched.');
      return fresh;
    }catch(e){
      const feed=feeds.find(f=>f.id===id);
      if(feed)feed.refreshError=e.message;
      if(notify)toast('Could not refresh '+(feed?.title||'this source')+': '+e.message);
    }finally{
      feedRefreshingIds.delete(id);feedLocks.delete(id);scheduleFeedRedraw();
    }
  })();
  feedLocks.set(id,work);return work;
}
async function refreshCategory(kind,{force=false}={}){
  if(!feeds.some(f=>f.kind===kind))return;
  if(feedRefreshKind){feedRefreshQueue.set(kind,force||feedRefreshQueue.get(kind)===true);return;}
  const targets=feeds.filter(f=>f.kind===kind);
  if(!force){
    const latest=Math.max(0,...targets.map(f=>Number(f.lastAttempt)||0));
    if(Date.now()-latest<30*60*1000&&targets.some(f=>(f.entries||[]).length))return;
  }
  feedRefreshKind=kind;scheduleFeedRedraw();
  const ids=targets.map(f=>f.id);let next=0;
  await Promise.all(Array.from({length:Math.min(5,ids.length)},async()=>{while(next<ids.length)await fetchLatestFeed(ids[next++]);}));
  feedRefreshKind=null;scheduleFeedRedraw();
  const queued=[...feedRefreshQueue.entries()][0];
  if(queued){feedRefreshQueue.delete(queued[0]);await refreshCategory(queued[0],{force:queued[1]});}
}
function applyFeedPayload(data){
  if(!data)return;
  if(Array.isArray(data.feeds))feeds=data.feeds;
  if(Array.isArray(data.directory))directory=data.directory;
  if(data.activity)feedActivity=data.activity;
}
function openFeed(id){activeFeed=id;feedView[route]='mine';query='';$('search').value='';renderFeeds();const feed=feeds.find(f=>f.id===id);if(feed&&!(feed.entries||[]).length)void fetchLatestFeed(id);}
const audio=$('audio');
audio.crossOrigin='anonymous';
const listenAudio=$('listen-audio');
let listening=null;
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const plain=s=>new DOMParser().parseFromString(s||'','text/html').body.textContent||'';
const short=(s,n=180)=>s.length>n?s.slice(0,n)+'…':s;
const art=kind=>'../assets/'+(categories.find(c=>c[0]===kind)?.[3]||'home_audiobooks.png');
const time=n=>{if(!Number.isFinite(n)||n<0)return '0:00';const h=Math.floor(n/3600),m=Math.floor(n/60)%60,s=Math.floor(n%60);return h?`${h}:${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`:`${m}:${String(s).padStart(2,'0')}`;};
const date=s=>{const d=new Date(s);return Number.isNaN(+d)?'':d.toLocaleDateString(undefined,{day:'numeric',month:'short',year:'numeric'});};
function toast(text){$('toast').textContent=String(text).replace(/^Error invoking remote method '[^']+': (Error: )?/,'');$('toast').classList.add('show');clearTimeout(toastTimer);toastTimer=setTimeout(()=>$('toast').classList.remove('show'),5500);}
const run=fn=>(...args)=>Promise.resolve().then(()=>fn(...args)).catch(e=>toast(e.message));
function on(id,event,fn){$(id)?.addEventListener(event,run(fn));}
function modal(title,html,setup){$('dialog-title').textContent=title;$('dialog-art').innerHTML=dialogArt(title);$('dialog-content').innerHTML=html;if(!$('dialog').open)$('dialog').showModal();setup?.();}
function closeModal(){$('dialog').close();}
function safeHTML(html){return DOMPurify.sanitize(html,{FORBID_TAGS:['script','style','iframe','object','embed','form','input','button','audio','video','svg','math'],FORBID_ATTR:['style','srcset'],ADD_ATTR:['target']});}
function applyTheme(){const dark=state.settings.theme==='dark'||(state.settings.theme==='system'&&matchMedia('(prefers-color-scheme: dark)').matches);document.body.classList.toggle('dark',dark);}
async function settings(patch){state.settings=await api.settings(patch);applyTheme();return state.settings;}
async function updateBook(b,patch){Object.assign(b,patch);const saved=await api.updateBook(b.id,patch);const i=state.books.findIndex(x=>x.id===b.id);if(i>=0)state.books[i]=saved;if(current?.id===b.id)Object.assign(current,saved);return saved;}
function cover(b,cls='book-cover'){return `<img class="${cls}" src="${esc(artURL(b.cover)||art(b.kind))}" alt="" loading="lazy">`;}
function bookRow(b){return `<div class="book-row"><button class="book-open" data-open="${b.id}">${cover(b)}<span class="grow"><strong>${esc(b.title)}</strong><small>${esc(b.kind==='Audio'?`${b.tracks?.length||1} chapters · Chapter ${(b.chapter||0)+1}`:b.kind==='Podcast'?b.author:b.kind+' book')}${b.progress?` · ${Math.round(b.progress)}%`:''}</small><span class="progress"><span style="width:${Math.min(100,b.progress||0)}%"></span></span></span></button><button class="subtle" data-book-menu="${b.id}" aria-label="Options for ${esc(b.title)}">•••</button></div>`;}
function renderNavigation(){document.querySelectorAll('[data-icon]').forEach(el=>el.innerHTML=clavisIcons[el.dataset.icon]||'');
  $('navigation').innerHTML=`<button data-route="Home" class="${route==='Home'?'active':''}"><span class="nav-icon">${clavisIcons.Home}</span>Home</button><p class="nav-label">YOUR LIBRARY</p>`+categories.map(([kind,title,,,symbol])=>`<button data-route="${kind}" class="${route===kind?'active':''}"><span class="nav-icon">${clavisIcons[kind]}</span>${title}</button>`).join('');
  document.querySelectorAll('.sidebar-bottom [data-route]').forEach(b=>b.classList.toggle('active',b.dataset.route===route));
}
async function cleanupReader(){if(listening)await closeListen();readerGeneration++;if(reader){reader.epub?.destroy();reader.pdf?.destroy();reader.observer?.disconnect();reader=null;}document.body.classList.remove('reading');}
async function navigate(next){await persistAudio();await flushNote();if(reader)await cleanupReader();route=next;activeFeed=null;feedBrowseTopic='';query='';$('search').value='';$('search').placeholder=['News','Podcasts','Journals'].includes(route)?'Search sources and stories':'Search your library';render();$('main').scrollTop=0;window.scrollTo(0,0);if(['News','Podcasts','Journals'].includes(next))void refreshCategory(next);}
function render(){document.body.classList.toggle('playing',route==='Player');renderNavigation();$('heading').textContent=route==='Home'?'Clavis':route==='Kindle'?'Kindle':categories.find(c=>c[0]===route)?.[1]||route;$('eyebrow').textContent=route==='Home'?'YOUR PERSONAL LIBRARY':route==='Player'?'NOW PLAYING':route==='Kindle'?'KINDLE LIBRARY':'CLAVIS FOR WINDOWS';$('import').hidden=!['Home','EPUB','PDF','Audio','Kindle'].includes(route);$('search').hidden=['Player','Reader','Settings','Journalling','Downloads'].includes(route);renderMini();
  if(route==='Home')renderHome();else if(['EPUB','PDF','Audio'].includes(route))renderLibrary();else if(['News','Podcasts','Journals'].includes(route))renderFeeds();else if(route==='Player')renderPlayer();else if(route==='Settings')renderSettings();else if(route==='Journalling')renderNotes();else if(route==='Downloads')renderDownloads();else if(route==='Kindle')renderKindle();
}
function renderHome(){const recent=state.books.filter(b=>b.lastActive&&b.kind!=='Podcast').sort((a,b)=>b.lastActive-a.lastActive).slice(0,4);$('main').innerHTML=`<div class="intro"><div class="intro-copy">${illustration('library','intro-art')}<div><h2>A little space for your next chapter.</h2><p>Everything you read and listen to, together.</p></div></div><span class="pill">${state.books.filter(b=>b.kind!=='Podcast').length} books in your library</span></div><div class="home-grid">${categories.map(([kind,title,description,image])=>`<button class="home-card" data-route="${kind}"><img src="../assets/${image}" alt=""><strong>${title}</strong><small>${description}</small></button>`).join('')}</div><div class="section-head"><h2>Continue reading</h2><span class="muted">Pick up where you left off</span></div>${recent.length?recent.map(bookRow).join(''):'<div class="empty"><h3>Your next chapter starts here.</h3><p>Import a book or audiobook to make this space your own.</p><button class="primary" data-action="import">＋ Import your first book</button></div>'}`;}
function renderLibrary(){const books=state.books.filter(b=>(b.kind===route||(route==='EPUB'&&b.kind==='Kindle'))&&b.title.toLowerCase().includes(query.toLowerCase()));$('main').innerHTML=`<div class="toolbar"><span class="muted">${books.length} ${books.length===1?'book':'books'}</span><div class="row">${route==='Audio'?'<button data-action="folder">＋ Import audiobook folder</button>':''}<button data-action="import">＋ Import files</button></div></div>${books.length?books.map(bookRow).join(''):`<div class="empty">${illustration(query?'search':'library','empty-art')}<h2>${query?'No matching books':'Your shelf is waiting'}</h2><p>${query?'Try a different title.':route==='Audio'?'Import a book folder, a whole library folder, or audio files.':`Import a ${route} book from your computer.`}</p>${query?'':'<button class="primary" data-action="import">＋ Import a book</button>'}</div>`}`;}
async function importFiles(){modal('Import books',`<p class="muted">Files are copied into the app’s Data / Books folder. Your originals stay untouched.</p><div class="stack"><button id="import-docs">▤ Choose ${route==='Home'?'EPUB, PDF or audio':route} files</button><button id="import-folder">♬ Choose an audiobook folder</button></div>`,()=>{on('import-docs','click',async()=>{closeModal();const s=await api.importFiles(['EPUB','PDF','Audio'].includes(route)?route:'All');if(s){state=s;render();toast('Books added to your library.');}});on('import-folder','click',importFolder);});}
async function importFolder(){closeModal();toast('Choose an audiobook folder. Subfolders and disc folders are included.');const s=await api.importFolder();if(s){state=s;render();toast('Audiobook folder scan complete.');}}
function bookMenu(id){const b=state.books.find(b=>b.id===id);const isKindle=b.kind==='Kindle';modal(b.title,`<div class="stack"><button id="book-open">Open book</button>${isKindle?`<button id="book-edit">Edit details…</button>`:''}<button id="book-remove">Remove from library · keep files</button><button id="book-delete" class="danger">Move book files to Recycle Bin…</button></div>`,()=>{on('book-open','click',()=>{closeModal();return openBook(id);});if(isKindle)on('book-edit','click',()=>{closeModal();libraryMetadataDialog(id);});on('book-remove','click',async()=>{if(current?.id===id){audio.pause();current=null;audio.removeAttribute('src');}state=await api.removeBook(id);closeModal();await navigate(route==='Reader'?'Home':route);});on('book-delete','click',async()=>{const s=await api.deleteBook(id);if(s){if(current?.id===id){audio.pause();current=null;}state=s;closeModal();await navigate('Home');}});});}
async function openBook(id){const b=state.books.find(b=>b.id===id);if(!b)return;await flushNote();if(b.kind==='Audio'||b.kind==='Podcast'){if(reader)await cleanupReader();await startBook(b,false);route='Player';render();}else{let book=b;if(book.kind==='Kindle'){try{toast('Preparing this Kindle book for reading…');const updated=await api.kindleConvert(book.id);const i=state.books.findIndex(x=>x.id===book.id);if(i>=0)state.books[i]=updated;book=updated;}catch(e){toast(e.message);return;}}await openReader(book);}}
async function startBook(b,autoplay=true,index,position){
  if(listening)await closeListen();
  await persistAudio();const generation=++audioGeneration;audioLoading=true;audio.pause();stopTranscription();transcriptVisible=false;
  try{
    if(b.kind==='Audio'&&!b.chaptersVersion){b=await api.prepareAudio(b.id);const i=state.books.findIndex(x=>x.id===b.id);if(i>=0)state.books[i]=b;}
    if(generation!==audioGeneration)return;
    current=b;chapter=Math.max(0,Math.min(Math.floor(index??b.chapter??0),(b.tracks?.length||1)-1));const track=b.tracks[chapter];if(!track)throw Error('This book has no audio tracks.');
    const resume=position??b.position??0;transcriptData=await api.getTranscript(b.id);playerContext=b.kind==='Podcast'?'Podcast':'Audio';
    if(audio.src!==track.url||audio.readyState<1){await new Promise((resolve,reject)=>{let timer;const clean=()=>{clearTimeout(timer);audio.removeEventListener('loadedmetadata',ready);audio.removeEventListener('error',failed);};const ready=()=>{clean();resolve();};const failed=()=>{clean();reject(Error('This audio file could not be opened.'));};audio.addEventListener('loadedmetadata',ready);audio.addEventListener('error',failed);timer=setTimeout(()=>{clean();reject(Error('Audio metadata timed out.'));},30000);audio.src=track.url;audio.load();});}
    if(generation!==audioGeneration)return;audio.playbackRate=b.speed||state.settings.speed||1;audio.volume=state.settings.volume??.8;
    audio.currentTime=trackStart(track)+Math.max(0,Math.min(resume,Math.max(0,audioDuration()-.01)));audioLoading=false;
    await updateBook(b,{chapter,position:audioPosition(),progress:listeningProgress(b.tracks,chapter,audioPosition(),audio.duration),speed:audio.playbackRate});
    if(autoplay)await audio.play();renderMini();if(route==='Player')renderPlayer();setMediaSession();
  }finally{if(generation===audioGeneration)audioLoading=false;}
}
function setMediaSession(){if(!current||!('mediaSession'in navigator))return;navigator.mediaSession.metadata=new MediaMetadata({title:current.title,artist:current.author||'Clavis',album:current.kind==='Podcast'?'Podcast':'Audiobook'});for(const [name,fn]of Object.entries({play:()=>audio.play(),pause:()=>audio.pause(),seekbackward:()=>skip(-1),seekforward:()=>skip(1),previoustrack:()=>changeChapter(-1),nexttrack:()=>changeChapter(1),seekto:d=>seekTo(d.seekTime)}))try{navigator.mediaSession.setActionHandler(name,run(fn));}catch{}}
function renderPlayerExtras(){document.body.classList.toggle('player-text-visible',transcriptVisible);if(!current||!document.querySelector('.player-options'))return;document.querySelector('.player-options').insertAdjacentHTML('beforeend',`<button id="equalizer">Equalizer</button>${current.kind==='Audio'?`<button id="transcript-toggle">${transcriptVisible?'Hide':'Show'} live text</button>`:''}`);on('equalizer','click',equalizerDialog);on('transcript-toggle','click',toggleTranscript);if(transcriptVisible)document.querySelector('.player').insertAdjacentHTML('afterend',`<section class="transcript"><div class="row spread"><h2>Live text</h2><small id="transcript-status">${esc(transcriptStatus)}</small></div><div id="transcript-text">${transcriptMarkup()}</div></section>`);}
function transcriptMarkup(){return (transcriptData[chapter]||[]).map(s=>`<p><small>${time(s.position)}</small> ${esc(s.text)}</p>`).join('')||'<p class="muted">Press Play to begin. Finalized passages appear here as the narration is recognized.</p>';}
async function toggleTranscript(){transcriptVisible=!transcriptVisible;if(!transcriptVisible){stopTranscription();renderPlayer();return;}transcriptStatus='Starting offline recognition…';renderPlayer();const bookId=current.id,trackIndex=chapter;try{await transcribe(audio,bookId+':'+chapter,text=>{if(current?.id!==bookId||chapter!==trackIndex)return;(transcriptData[trackIndex]||=[]).push({position:audioPosition(),text});if($('transcript-text'))$('transcript-text').innerHTML=transcriptMarkup();run(()=>api.saveTranscript(bookId,transcriptData))();},status=>{transcriptStatus=status;if($('transcript-status'))$('transcript-status').textContent=status;});}catch(e){transcriptStatus='Speech model could not start: '+e.message;if($('transcript-status'))$('transcript-status').textContent=transcriptStatus;toast(transcriptStatus);}}
function equalizerDialog(target=audio){modal('Audio settings',`<p class="muted">Shape narration with a five-band equalizer and voice gain.</p>${[100,350,1000,3500,10000].map((hz,i)=>`<label for="eq-${i}">${hz>=1000?hz/1000+' kHz':hz+' Hz'}</label><input id="eq-${i}" type="range" min="-12" max="12" step="1" value="${equalizer[i]}">`).join('')}<label for="voice-gain">Voice gain</label><input id="voice-gain" type="range" min=".5" max="2" step=".1" value="${voiceGain}"><div class="row"><button id="apply-eq" class="primary">Apply</button><button id="reset-eq">Reset</button></div>`,()=>{on('apply-eq','click',async()=>{equalizer=equalizer.map((_,i)=>Number($('eq-'+i).value));voiceGain=Number($('voice-gain').value);await effects(target,equalizer,voiceGain,target!==audio);closeModal();});on('reset-eq','click',async()=>{equalizer=[0,0,0,0,0];voiceGain=1;await effects(target,equalizer,voiceGain,target!==audio);closeModal();});});}
async function persistAudio(){if(current&&audio.src&&!audioLoading){clearTimeout(saveTimer);saveTimer=null;const b=current;await updateBook(b,{chapter,position:audioPosition(),progress:listeningProgress(b.tracks,chapter,audioPosition(),audio.duration),speed:audio.playbackRate});}}
async function togglePlay(){if(!current)return toast('Open an audiobook or podcast first.');if(audioLoading)return;if(audio.paused){if(audioPosition()>=audioDuration()-.05)await seekTo(0,false);await audio.play();}else audio.pause();}
async function seekTo(position,remember=true){if(!current||audioLoading)return;if(remember)lastSeek={id:current.id,chapter,position:audioPosition()};const resumeText=transcriptVisible;stopTranscription();audio.currentTime=trackStart(activeTrack())+Math.max(0,Math.min(Number(position)||0,audioDuration()));updateTimes();await persistAudio();if(resumeText){transcriptVisible=false;await toggleTranscript();}}
async function undoSeek(){if(!lastSeek||lastSeek.id!==current?.id)return;const target=lastSeek;lastSeek=null;if(target.chapter===chapter)await seekTo(target.position,false);else await startBook(current,!audio.paused,target.chapter,target.position);}
async function skip(direction){if(!current||audioLoading)return;lastSeek={id:current.id,chapter,position:audioPosition()};const target=audioPosition()+direction*(state.settings.skip||30),duration=audioDuration(),playing=!audio.paused;if(target>=duration&&chapter+1<current.tracks.length)await startBook(current,playing,chapter+1,target-duration);else if(target<0&&chapter>0)await startBook(current,playing,chapter-1,0);else await seekTo(target,false);updateTimes();}
async function changeChapter(delta){if(!current||audioLoading)return;const i=chapter+delta;if(i<0||i>=current.tracks.length)return;await startBook(current,true,i,0);}
function updatePlayButtons(){document.querySelectorAll('[data-action="play"]').forEach(b=>{b.innerHTML=transportIcon(audio.paused?'play':'pause');b.setAttribute('aria-label',audio.paused?'Play':'Pause');});}
function offerSpokenScan(){modal('Detect spoken chapters',`<p>No embedded chapter markers were found. Clavis can scan English narration for spoken headings such as “Chapter one”.</p><p class="notice">This runs offline and may take a long time for a full audiobook. Detection is approximate. Review the results before applying them.</p><div class="row"><button id="begin-chapter-scan" class="primary">Scan narration</button><button id="skip-chapter-scan">Keep file chapters</button></div>`,()=>{on('skip-chapter-scan','click',closeModal);on('begin-chapter-scan','click',scanSpokenChapters);});}
async function scanSpokenChapters(){
  const b=current;await persistAudio();audio.pause();stopTranscription();let scan,recognizer,cancelled=false;const markers=[],seen=new Map();let carry=[],fileIndex=0;
  modal('Scanning spoken chapter headings','<p id="scan-status" class="muted">Loading bundled English speech model…</p><progress id="scan-progress" max="100" value="0" style="width:100%"></progress><p id="scan-found">No headings found yet.</p><button id="cancel-chapter-scan">Cancel scan</button>');
  const cancel=()=>{cancelled=true;recognizer?.remove();if(scan)run(()=>api.chapterScanCancel(scan.id))();};$('dialog').addEventListener('close',cancel,{once:true});on('cancel-chapter-scan','click',closeModal);
  function results(result){const words=result?.result||[];const combined=[...carry,...words];for(const h of spokenHeadings(combined)){const previous=seen.get(fileIndex+':'+h.title);if(previous!=null&&Math.abs(previous-h.start)<12)continue;seen.set(fileIndex+':'+h.title,h.start);markers.push({...h,fileIndex});}carry=combined.slice(-5);if($('scan-found'))$('scan-found').textContent=markers.length+' candidate headings found.';}
  try{scan=await api.chapterScanStart(b.id);const total=scan.files.reduce((n,f)=>n+f.duration,0);let finishedSeconds=0;recognizer=await scanRecognizer(results);while(!cancelled){const chunk=await api.chapterScanRead(scan.id);if(chunk.done)break;if(chunk.fileDone){await recognizer.finish();recognizer.remove();recognizer=null;finishedSeconds+=scan.files[fileIndex]?.duration||chunk.seconds;fileIndex++;carry=[];if(fileIndex<scan.files.length)recognizer=await scanRecognizer(results);continue;}fileIndex=chunk.fileIndex;await recognizer.accept(chunk.pcm);if(cancelled)break;if($('scan-status'))$('scan-status').textContent='Scanning file '+(fileIndex+1)+' of '+scan.files.length+' · '+time(chunk.seconds);if($('scan-progress'))$('scan-progress').value=total?Math.min(100,(finishedSeconds+chunk.seconds)/total*100):0;}
    if(cancelled)return;recognizer?.remove();recognizer=null;await api.chapterScanCancel(scan.id);$('dialog').removeEventListener('close',cancel);markers.sort((a,b)=>a.fileIndex-b.fileIndex||a.start-b.start);
    modal('Review detected chapters',`<p class="notice">${markers.length} candidate headings. Uncheck any spoken references that are not real chapter starts.</p><div class="directory">${markers.map((m,i)=>`<label class="row"><input type="checkbox" data-scan-marker="${i}" checked style="width:auto">${esc(m.title)} · File ${m.fileIndex+1} · ${time(m.start)}</label>`).join('')||'<p class="muted">No spoken chapter headings were recognized. Your current chapters are unchanged.</p>'}</div><div class="row"><button id="apply-chapter-results" class="primary" ${markers.length?'':'disabled'}>Apply selected chapters</button><button id="discard-chapter-results">Keep current chapters</button></div>`,()=>{on('discard-chapter-results','click',closeModal);on('apply-chapter-results','click',async()=>{const chosen=[...document.querySelectorAll('[data-scan-marker]:checked')].map(el=>markers[Number(el.dataset.scanMarker)]);if(!chosen.length)return toast('Select at least one chapter.');const updated=await api.applySpokenChapters(b.id,chosen);state.books=state.books.map(x=>x.id===b.id?updated:x);closeModal();await startBook(updated,false,updated.chapter,updated.position);toast('Detected chapters saved.');});});
  }catch(e){if(!cancelled){$('dialog').removeEventListener('close',cancel);modal('Chapter scan could not finish',`<p>${esc(e.message)}</p><p class="muted">Existing chapters have been kept.</p>`);}}
  finally{recognizer?.remove();if(scan)await api.chapterScanCancel(scan.id);$('dialog').removeEventListener('close',cancel);}
}
function bindPlayerSeek(){const slider=$('player-seek');if(!slider)return;slider.addEventListener('pointerdown',()=>{seekDragging=true;});slider.addEventListener('input',()=>{const value=Number(slider.value)/1000*audioDuration();if($('elapsed'))$('elapsed').textContent=time(value);if(!seekDragging)run(()=>seekTo(value))();});slider.addEventListener('change',()=>{const value=Number(slider.value)/1000*audioDuration();seekDragging=false;run(()=>seekTo(value))();});slider.addEventListener('pointercancel',()=>{seekDragging=false;updateTimes();});}
async function detectChapters(){if(!current||current.kind!=='Audio')return;await persistAudio();const playing=!audio.paused;audioLoading=true;audio.pause();try{toast('Reading embedded chapter markers…');const updated=await api.prepareAudio(current.id,true);state.books=state.books.map(b=>b.id===updated.id?updated:b);current=updated;await startBook(updated,playing,updated.chapter,updated.position);const embedded=updated.tracks.filter(t=>t.embedded).length;if(embedded)toast(embedded+' embedded chapters detected.');else offerSpokenScan();}finally{audioLoading=false;}}

function renderMini(){const mini=$('mini');mini.hidden=!current||route==='Player'||route==='Reader';if(!current)return;mini.innerHTML=`${cover(current,'mini-cover')}<button class="mini-title" data-action="show-player"><strong>${esc(current.title)}</strong><small id="mini-detail">${esc(current.tracks?.[chapter]?.title||'')} · ${time(audioPosition())}</small></button><button class="subtle" data-action="skip-back" aria-label="Rewind">${transportIcon('back',state.settings.skip)}</button><button class="mini-play" data-action="play" aria-label="${audio.paused?'Play':'Pause'}">${transportIcon(audio.paused?'play':'pause')}</button><button class="subtle" data-action="skip-forward" aria-label="Forward">${transportIcon('forward',state.settings.skip)}</button>`;}
function renderPlayer(){document.body.classList.add('playing');document.body.classList.remove('player-text-visible');if(!current){$('main').innerHTML='<div class="empty"><h2>Nothing playing yet</h2><p>Open a book from Audio Books or an episode from Podcasts.</p><button data-route="Audio">Open audiobook library</button></div>';return;}$('main').innerHTML=`<div class="row spread"><button data-route="${current.kind==='Podcast'?'Podcasts':'Audio'}">‹ Back to library</button><span class="pill">${current.kind==='Podcast'?'PODCAST':'AUDIOBOOK'}</span></div><div class="player">${cover(current,'player-art')}<div><p class="muted">${esc(current.author||'YOUR AUDIO LIBRARY')}</p><h2>${esc(current.title)}</h2><p class="player-meta">${esc(current.tracks[chapter]?.title||'')} · ${chapter+1} / ${current.tracks.length}</p><input id="player-seek" type="range" min="0" max="1000" value="0" aria-label="Playback position"><div class="time"><span id="elapsed">${time(audioPosition())}</span><span id="duration">${time(audioDuration())}</span></div><div class="transport"><button data-action="previous" aria-label="Previous chapter" ${chapter===0?'disabled':''}>${transportIcon('previous')}</button><button data-action="skip-back" aria-label="Rewind ${state.settings.skip||30} seconds">${transportIcon('back',state.settings.skip)}</button><button class="play" data-action="play" aria-label="${audio.paused?'Play':'Pause'}">${transportIcon(audio.paused?'play':'pause')}</button><button data-action="skip-forward" aria-label="Forward ${state.settings.skip||30} seconds">${transportIcon('forward',state.settings.skip)}</button><button data-action="next" aria-label="Next chapter" ${chapter===current.tracks.length-1?'disabled':''}>${transportIcon('next')}</button></div><div class="player-options"><button data-action="speed">${audio.playbackRate}× Speed</button><button data-action="sleep">◷ ${sleepTimer?'Timer on':'Sleep timer'}</button><button data-action="audio-bookmarks">⚑ Bookmarks</button></div><label class="volume">Volume <input id="volume" type="range" min="0" max="1" step=".01" value="${audio.volume}" aria-label="Volume"></label></div></div><div class="chapters"><div class="row spread"><h2>Chapters</h2><div class="row"><button data-action="undo-seek">Undo seek</button>${current.kind==='Audio'?'<button data-action="detect-chapters">Detect chapters</button>':''}<button data-action="add-audio-bookmark">＋ Bookmark this moment</button></div></div><div class="chapter-list">${current.tracks.map((t,i)=>`<button class="chapter-row ${i===chapter?'active':''}" data-chapter="${i}"><span>${i+1}. ${esc(t.title)}</span><small>${i===chapter?'Now selected':t.duration?time(t.duration):''}</small></button>`).join('')}</div></div>`;bindPlayerSeek();on('volume','input',async()=>{audio.volume=Number($('volume').value);await settings({volume:audio.volume});});updateTimes();renderPlayerExtras();}
function updateTimes(){if(current&&audioDuration()>0&&navigator.mediaSession)try{navigator.mediaSession.setPositionState({duration:audioDuration(),playbackRate:audio.playbackRate,position:Math.min(audioDuration(),audioPosition())});}catch{}if($('elapsed'))$('elapsed').textContent=time(audioPosition());if($('duration'))$('duration').textContent=time(audioDuration());if($('player-seek')&&!seekDragging)$('player-seek').value=audioDuration()?audioPosition()/audioDuration()*1000:0;if($('mini-detail')&&current)$('mini-detail').textContent=(current.tracks[chapter]?.title||'')+' · '+time(audioPosition());}

function speedDialog(){modal('Playback speed',`<div class="stack">${[.5,.75,1,1.25,1.5,1.75,2,2.5,3].map(n=>`<button data-rate="${n}">${n}×${n===1?' · Normal':''}</button>`).join('')}</div>`,()=>{$('dialog-content').querySelectorAll('[data-rate]').forEach(b=>b.onclick=run(async()=>{audio.playbackRate=Number(b.dataset.rate);await settings({speed:audio.playbackRate});await persistAudio();closeModal();renderPlayer();}));});}
function sleepDialog(){modal('Sleep timer','<p class="muted">Pause playback after a set time or at the end of this chapter.</p><div class="stack"><button data-minutes="15">15 minutes</button><button data-minutes="30">30 minutes</button><button data-minutes="60">60 minutes</button><button id="end-chapter">End of chapter</button><button id="cancel-sleep">Turn off timer</button></div>',()=>{document.querySelectorAll('[data-minutes]').forEach(b=>b.onclick=()=>{clearTimeout(sleepTimer);audio.dataset.sleepEnd='';sleepTimer=setTimeout(()=>{audio.pause();sleepTimer=null;toast('Sleep timer finished.');renderPlayer();},Number(b.dataset.minutes)*60000);closeModal();renderPlayer();toast(`Sleep timer: ${b.dataset.minutes} minutes.`);});on('end-chapter','click',()=>{clearTimeout(sleepTimer);sleepTimer=null;audio.dataset.sleepEnd='yes';closeModal();toast('Playback will stop at the end of this chapter.');});on('cancel-sleep','click',()=>{clearTimeout(sleepTimer);sleepTimer=null;audio.dataset.sleepEnd='';closeModal();renderPlayer();});});}
function addAudioBookmark(){modal('Bookmark this moment',`<p class="muted">Chapter ${chapter+1} · ${time(audioPosition())}</p><input id="bookmark-name" placeholder="Bookmark name" maxlength="200"><div class="row"><button id="save-bookmark" class="primary">Save bookmark</button></div>`,()=>on('save-bookmark','click',async()=>{await updateBook(current,{bookmarks:[...(current.bookmarks||[]),{name:$('bookmark-name').value||`Chapter ${chapter+1} · ${time(audioPosition())}`,chapter,position:audioPosition()}]});closeModal();toast('Bookmark saved.');}));}
function audioBookmarks(){if(!current)return;modal('Audio bookmarks',`<div class="stack">${(current.bookmarks||[]).map((b,i)=>`<div class="row"><button class="grow" data-jump-bookmark="${i}">${esc(b.name)} · ${time(b.position)}</button><button data-remove-bookmark="${i}" aria-label="Delete bookmark">✕</button></div>`).join('')||'<p class="muted">Save a moment to find it again.</p>'}<button id="new-bookmark">＋ Bookmark current position</button></div>`,()=>{on('new-bookmark','click',addAudioBookmark);document.querySelectorAll('[data-jump-bookmark]').forEach(b=>b.onclick=run(async()=>{const mark=current.bookmarks[Number(b.dataset.jumpBookmark)];await startBook(current,true,mark.chapter,mark.position);closeModal();if(route==='Player')renderPlayer();}));document.querySelectorAll('[data-remove-bookmark]').forEach(b=>b.onclick=run(async()=>{await updateBook(current,{bookmarks:current.bookmarks.filter((_,i)=>i!==Number(b.dataset.removeBookmark))});audioBookmarks();}));});}
const artURL=value=>String(value||'').replace(/^http:\/\//,'https://');
function sourceArt(source){
  const image=source.image?artURL(source.image):'';
  const initials=esc(plain(source.title).split(/\s+/).slice(0,3).map(word=>word[0]).join(''));
  return image?`<img class="source-art" src="${esc(image)}" alt="" loading="lazy" referrerpolicy="no-referrer">`:`<span class="source-art source-placeholder"><span class="source-initials">${initials}</span></span>`;
}
function feedHtml(raw){
  const box=document.createElement('div');box.innerHTML=safeHTML(raw||'');
  box.querySelectorAll('script,style,img,picture,figure,video,audio,iframe,svg,form,button,input,aside,nav,footer,header').forEach(el=>el.remove());
  box.querySelectorAll('a').forEach(link=>{if(!link.textContent.trim())link.remove();});
  box.querySelectorAll('p,div,section').forEach(el=>{if(!el.textContent.trim()&&!el.querySelector('img,table,ul,ol'))el.remove();});
  return box.innerHTML.trim();
}
function postCover(row){
  const image=artURL(row.item.image||row.feed.image);
  return image?`<img src="${esc(image)}" alt="" loading="lazy" referrerpolicy="no-referrer">`:`<div class="post-cover-fallback"><strong>${esc(plain(row.item.title))}</strong></div>`;
}
function postCredit(row){return [row.item.author?'By '+plain(row.item.author):'',row.item.rights||''].filter(Boolean).join(' · ');}
function postCard(row,index){
  const when=feedWhen(row.item.date);
  const credit=postCredit(row);
  const plainPost=!(row.item.image||row.feed.image);
  return `<article class="post${plainPost?' post-no-image':''}" data-post="${index}" data-title-in-cover="${plainPost?'1':''}" data-key="${esc(feedKey(row.item))}"><div class="post-meta"><span class="post-source">${esc(row.feed.title)}</span>${when?`<time>${esc(when)}</time>`:''}</div><div class="post-pages" data-pages><div class="post-cover" data-cover>${postCover(row)}</div><div class="post-text" data-text hidden><div class="post-flow" data-flow></div></div></div><h2 class="post-title"${plainPost?' hidden':''}>${esc(plain(row.item.title))}</h2><div class="post-nav"><button data-slide="-1" aria-label="Previous story slide" disabled>‹</button><span data-count>Loading story…</span><button data-slide="1" aria-label="Next story slide" disabled>›</button></div><p class="post-status" data-status></p><button class="post-credits" data-credits>${esc(credit||'Source credits')}</button><div class="post-actions"><button data-listen>♪ Listen</button>${row.item.link?'<button data-web>Open website ↗</button>':''}</div></article>`;
}
function renderPostStream(rows){
  feedPosts=rows;
  return `<div class="post-stream">${rows.map((row,index)=>postCard(row,index)).join('')}</div>`;
}
function renderEpisodeStream(rows){
  feedPosts=rows;
  return `<div class="episode-stream">${rows.map(row=>{
    const when=feedWhen(row.item.date),duration=row.item.duration?time(row.item.duration):'';
    const image=artURL(row.item.image||row.feed.image);
    return `<button class="episode-row" data-play-feed="${esc(row.feed.id)}" data-play-item="${esc(row.item.id)}">${image?`<img class="episode-art" src="${esc(image)}" alt="" loading="lazy" referrerpolicy="no-referrer">`:`<span class="episode-art source-placeholder"><span class="source-initials">${esc(plain(row.feed.title).split(/\s+/).slice(0,2).map(word=>word[0]).join(''))}</span></span>`}<span class="episode-copy"><small>${esc(row.feed.title)}${when?' · '+esc(when):''}${duration?' · '+duration:''}</small><strong>${esc(plain(row.item.title))}</strong><span>${esc(short(plain(row.item.summary||row.item.content),180))}</span></span><span class="episode-play" aria-hidden="true">▶</span></button>`;
  }).join('')}</div>`;
}
function feedTabs(kind){
  const tabs=[['popular','Popular'],['mine',kind==='Podcasts'?'My podcasts':'My list'],['browse','Browse']];
  return `<div class="feed-tabs">${tabs.map(([key,label])=>`<button data-feed-tab="${key}" class="${feedTab(kind)===key?'active':''}">${label}</button>`).join('')}</div>`;
}
function feedControls(kind,count){
  const topics=feedTopics(kind);
  const topicLabel=!topics.length?'All topics':topics.length===1?topics[0]:topics.length+' selected';
  const refreshing=feedRefreshKind===kind;
  return `<div class="feed-controls">${['News','Journals'].includes(kind)?`<button data-topics>Topics · ${esc(topicLabel)}</button><button data-order>${feedOrder(kind)==='latest'?'Latest first':'Popular first'}</button>`:''}<button data-refresh-kind ${refreshing?'disabled':''}>${refreshing?'Refreshing…':'↻ Refresh'}</button><button data-custom-feed>＋ RSS address</button></div><p class="feed-note">${count} ${kind==='Podcasts'?'episodes':'stories'} from ${feeds.filter(f=>f.kind===kind).length} sources · saved stories stay available offline</p>`;
}
function renderMyList(kind){
  const term=query.toLowerCase();
  const list=feeds.filter(f=>f.kind===kind&&feedSourceMatches(f)&&(!term||f.title.toLowerCase().includes(term)||(f.entries||[]).some(item=>item.title.toLowerCase().includes(term))));
  if(!list.length)return `<div class="empty">${illustration('feeds','empty-art')}<h2>${feeds.some(f=>f.kind===kind)?'No sources match these topics':'Follow your favourite '+feedLabel(kind).toLowerCase()}</h2><p>Browse the ${feedLabel(kind).toLowerCase()} directory or add an RSS address.</p><button class="primary" data-feed-tab="browse">Browse sources</button></div>`;
  return `<div class="source-list">${list.map(feed=>{const latest=(feed.entries||[])[0];return `<div class="source-row" data-feed-open="${esc(feed.id)}" role="button" tabindex="0">${sourceArt(feed)}<div class="source-copy"><strong>${esc(plain(feed.title))}</strong><small>${(feed.entries||[]).length} ${kind==='Podcasts'?'episodes':'articles'}${feed.refreshError?' · saved stories':''}</small>${latest?`<span>${esc(plain(latest.title))}</span>`:''}</div><button class="source-remove" data-remove-feed="${esc(feed.id)}" aria-label="Remove ${esc(plain(feed.title))}">✕</button></div>`;}).join('')}</div>`;
}
function renderBrowse(kind){
  const term=query.toLowerCase();
  const sources=directory.filter(source=>source.kind===kind&&(!term||(source.title+' '+(source.tags||[]).join(' ')).toLowerCase().includes(term))&&(!feedBrowseTopic||(source.tags||[]).includes(feedBrowseTopic)));
  return `<div class="browse-tags"><button data-browse-topic="" class="${feedBrowseTopic?'':'active'}">All topics</button>${FEED_TOPICS.map(topic=>`<button data-browse-topic="${esc(topic)}" class="${feedBrowseTopic===topic?'active':''}">${esc(topic)}</button>`).join('')}</div><p class="feed-note">${sources.length} ${feedLabel(kind).toLowerCase()} sources · follow as many as you like</p><div class="browse-list">${sources.map(source=>{const image=source.image?artURL(source.image):'';const followed=feeds.some(feed=>feed.kind===kind&&feed.url===source.url);return `<div class="browse-row">${image?`<img class="source-art" src="${esc(image)}" alt="" loading="lazy" referrerpolicy="no-referrer">`:`<span class="source-art source-placeholder"><span class="source-initials">${esc(source.title.split(/\s+/).slice(0,2).map(word=>word[0]).join(''))}</span></span>`}<div class="browse-copy"><strong>${esc(source.title)}</strong><small>${esc((source.tags||[]).join(' · '))}${source.artist?' · '+esc(source.artist):''}</small></div><button class="${followed?'':'primary'}" data-subscribe="${esc(source.url)}" data-subscribe-kind="${kind}">${followed?'Open':'＋ Follow'}</button></div>`;}).join('')||'<div class="empty"><h3>No matching sources</h3><p>Try another publisher, topic or website name.</p></div>'}</div>`;
}
function renderFeedSource(feed){
  const rows=(feed.entries||[]).map((item,index)=>({feed,item,position:index,opens:feedActivity[feedKey(item)]||0,time:feedDateValue(item.date)}));
  const filtered=query?rows.filter(row=>(row.item.title+' '+(row.item.summary||row.item.content)).toLowerCase().includes(query.toLowerCase())):rows;
  return `<div class="source-head"><button data-feed-back>‹ ${esc(feed.kind==='Podcasts'?'My podcasts':'My list')}</button><div class="source-identity">${sourceArt(feed)}<div><h2>${esc(plain(feed.title))}</h2><small>${esc(feedStatus(feed))}</small></div></div><div class="feed-controls"><button data-refresh="${esc(feed.id)}" ${feedRefreshingIds.has(feed.id)?'disabled':''}>${feedRefreshingIds.has(feed.id)?'Refreshing…':'↻ Refresh'}</button><button data-remove-feed="${esc(feed.id)}">Remove</button></div>${feed.refreshError?`<p class="notice">Saved stories are shown. ${esc(feed.refreshError)}</p>`:''}</div>`+(filtered.length?(feed.kind==='Podcasts'?renderEpisodeStream(filtered):renderPostStream(filtered)):`<div class="empty"><h3>No ${feed.kind==='Podcasts'?'episodes':'stories'} yet</h3><p>Refresh this source to check for updates.</p></div>`);
}
function renderFeeds(){
  if(!FEED_KINDS.includes(route))return;
  const kind=route;
  if(activeFeed){const feed=feeds.find(f=>f.id===activeFeed);if(feed&&feed.kind===kind){$('main').innerHTML=renderFeedSource(feed);if(kind!=='Podcasts')observePosts();return;}activeFeed=null;}
  const tab=feedTab(kind);
  if(tab==='browse'){$('main').innerHTML=feedTabs(kind)+renderBrowse(kind);return;}
  if(tab==='mine'){$('main').innerHTML=feedTabs(kind)+renderMyList(kind);return;}
  const rows=feedStream(kind);
  const filtered=query?rows.filter(row=>(row.item.title+' '+(row.item.summary||row.item.content)+' '+row.feed.title).toLowerCase().includes(query.toLowerCase())):rows;
  const refreshing=feeds.filter(f=>f.kind===kind&&feedRefreshingIds.has(f.id)).length;
  const body=filtered.length?(kind==='Podcasts'?renderEpisodeStream(filtered):renderPostStream(filtered)):`<div class="empty">${illustration('feeds','empty-art')}<h2>${refreshing||feedRefreshKind===kind?'Fetching the latest stories…':query?'No matching stories':'No entries yet'}</h2><p>${refreshing||feedRefreshKind===kind?'Publishers are being checked in the background. Saved stories stay available offline.':query?'Try a different search.':'Refresh your sources or browse the directory to follow more.'}</p><button data-refresh-kind>↻ Refresh sources</button></div>`;
  $('main').innerHTML=feedTabs(kind)+feedControls(kind,filtered.length)+body;
  if(kind!=='Podcasts'&&filtered.length)observePosts();
}
function observePosts(){
  postObserver?.disconnect();
  // the page scrolls in the window, so the viewport is the only useful root: main spans the whole stream
  postObserver=new IntersectionObserver(entries=>{for(const entry of entries)if(entry.isIntersecting){postObserver.unobserve(entry.target);void hydratePost(entry.target);}},{root:null,rootMargin:'900px 0px'});
  document.querySelectorAll('.post').forEach(post=>postObserver.observe(post));
}
async function hydratePost(post){
  const row=feedPosts[Number(post.dataset.post)];if(!row)return;
  const key=post.dataset.key||feedKey(row.item);
  const known=postBodies.get(key);
  if(known&&!known.loading){paintPost(post,known);return;}
  if(known?.loading)return;
  const record={loading:true,loaded:false,html:'',body:'',status:'',image:''};postBodies.set(key,record);
  let html=feedHtml(row.item.content),body=plain(html),status='';
  if(!row.item.link)status='Feed text · no publisher link';
  else if(row.feed.contentMode!=='full-feed'||body.length<400){
    const line=post.querySelector('[data-status]');if(line)line.textContent='Loading the full story…';
    try{
      const article=await api.article(row.item.link);
      if(article.availability==='publisher-blocked')status='Publisher access required · Open website to read the story';
      else if((article.characters||0)>=120&&article.content){html=feedHtml(article.content);body=plain(html);status=article.preview?'Publisher preview · Open website for access':'';record.image=article.image||'';}
      else status='Feed text · open the website for the full story';
    }catch(e){status='Feed text · the full story may be on the website';}
  }
  if(!body.trim())status=status||'This feed has no article text. Open the website to read the story.';
  record.html=html;record.body=body;record.status=status;record.loading=false;record.loaded=true;
  const target=post.isConnected?post:postFor(key);
  if(target)paintPost(target,record);
}
function paintPost(post,record){
  const flow=post.querySelector('[data-flow]');if(!flow)return;
  flow.innerHTML=record.html||'<p class="muted">This feed has no article text. Use Open website to read the story.</p>';
  const status=post.querySelector('[data-status]');if(status)status.textContent=record.status||'';
  if(record.image){
    const cover=post.querySelector('[data-cover]'),image=cover?.querySelector('img');
    if(image)image.src=artURL(record.image);
    else if(cover){
      cover.innerHTML=`<img src="${esc(artURL(record.image))}" alt="" loading="lazy" referrerpolicy="no-referrer">`;
      post.classList.remove('post-no-image');post.dataset.titleInCover='';
      const title=post.querySelector('.post-title');if(title)title.hidden=post.dataset.slide>0;
    }
  }
  requestAnimationFrame(()=>paginatePost(post));
}
function paginatePost(post){
  const pages=post.querySelector('[data-pages]'),text=post.querySelector('[data-text]'),flow=post.querySelector('[data-flow]');
  if(!pages||!text||!flow)return;
  if(post.classList.contains('post-no-image'))post.classList.add('post-paginating');
  text.hidden=false;
  const style=getComputedStyle(text);
  const width=flow.clientWidth,height=text.clientHeight-parseFloat(style.paddingTop||0)-parseFloat(style.paddingBottom||0);
  if(width<40||height<40)return;
  flow.style.columnWidth=width+'px';flow.style.height=height+'px';
  const gap=parseFloat(getComputedStyle(flow).columnGap)||36;
  const total=Math.max(1,Math.round((flow.scrollWidth+gap)/(width+gap)));
  // Re-measuring must not snap a reader back to the cover when the story finishes hydrating.
  const wanted=Math.min(Number(post.dataset.slide||0),total);
  post.dataset.pages=String(total);post.dataset.slide=String(wanted);
  if(!wanted)flow.style.transform='translateX(0)';
  post.classList.remove('post-paginating');
  updatePost(post);
}
function updatePost(post){
  const total=1+Number(post.dataset.pages||1),slide=Math.max(0,Math.min(total-1,Number(post.dataset.slide||0)));
  post.dataset.slide=String(slide);
  const cover=post.querySelector('[data-cover]'),text=post.querySelector('[data-text]');
  if(cover)cover.hidden=slide!==0;
  if(text)text.hidden=slide===0;
  const count=post.querySelector('[data-count]');if(count)count.textContent=`${slide+1} / ${total}${slide===0?' · Use the arrows or drag to read':''}`;
  const previous=post.querySelector('[data-slide="-1"]'),next=post.querySelector('[data-slide="1"]');
  if(previous)previous.disabled=slide<=0;if(next)next.disabled=slide>=total-1;
  post.classList.toggle('post-reading',slide>0);
  const title=post.querySelector('.post-title');if(title)title.hidden=slide>0||post.dataset.titleInCover==='1';
  if(slide>0){const flow=post.querySelector('[data-flow]'),gap=parseFloat(getComputedStyle(flow).columnGap)||36;flow.style.transform=`translateX(calc(${-(slide-1)} * (100% + ${gap}px)))`;}
  if(slide>0&&!post.dataset.opened){post.dataset.opened='1';markFeedOpened(post.dataset.key);}
}
function slidePost(post,delta){
  const total=1+Number(post.dataset.pages||1);
  post.dataset.slide=String(Math.max(0,Math.min(total-1,Number(post.dataset.slide||0)+delta)));
  updatePost(post);
  // the card changes height when it opens, so centre it after the layout settles
  requestAnimationFrame(()=>centerPost(post));
}
function centerPost(post){
  if(!post.isConnected)return;
  const box=post.getBoundingClientRect(),margin=16,mini=$('mini');
  // the floating player covers the foot of the page, so the usable view stops above it
  const view=window.innerHeight-(mini&&mini.hidden===false?mini.getBoundingClientRect().height+margin*2:0);
  if(box.top>=margin&&box.bottom<=view-margin)return;
  // explicit window maths: scrollIntoView walks every nested scroller and overshoots when the stream re-renders mid-scroll
  const offset=box.height+margin*2<=view?(view-box.height)/2:margin;
  window.scrollTo({top:window.scrollY+box.top-offset,behavior:'smooth'});
}
function markFeedOpened(key){
  if(!key)return;
  void api.feedOpened(key).then(activity=>{if(activity)feedActivity=activity;}).catch(()=>{});
}
function postFor(key){return document.querySelector(`.post[data-key="${CSS.escape(key)}"]`);}
function feedCredits(row){
  const lines=[plain(row.item.title),row.item.author?'By '+plain(row.item.author):'',row.feed.title,row.item.link,row.item.rights].filter(Boolean);
  modal('Source credits',`<div class="stack">${lines.map(line=>`<p>${esc(line)}</p>`).join('')}<div class="row">${row.item.link?'<button id="credit-website">Open website ↗</button>':''}${row.feed.policy?'<button id="credit-terms">Source terms ↗</button>':''}</div></div>`,()=>{
    if(row.item.link)on('credit-website','click',()=>api.openURL(row.item.link));
    if(row.feed.policy)on('credit-terms','click',()=>api.openURL(row.feed.policy));
  });
}
async function listenPost(row){
  const state=postBodies.get(feedKey(row.item));
  const body=state?.body||plain(row.item.content)||plain(row.item.summary);
  await listenArticle(row.feed,row.item,body);
  markFeedOpened(feedKey(row.item));
}
async function playEpisode(feedId,itemId){
  await persistAudio();if(listening)await closeListen();
  const feed=feeds.find(f=>f.id===feedId),item=feed?.entries.find(entry=>entry.id===itemId);
  const book=await api.playEpisode(feedId,itemId);
  const at=state.books.findIndex(entry=>entry.id===book.id);
  if(at<0)state.books.push(book);else state.books[at]=book;
  markFeedOpened(item?feedKey(item):itemId);
  await startBook(book,true);route='Player';render();
}
async function subscribeSource(url,kind){
  const existing=feeds.find(feed=>feed.kind===kind&&feed.url===url);
  if(existing){openFeed(existing.id);return;}
  const button=document.querySelector(`[data-subscribe="${CSS.escape(url)}"]`);
  if(button){button.disabled=true;button.textContent='Adding…';}
  try{
    const source=directory.find(item=>item.kind===kind&&item.url===url);
    applyFeedPayload(await api.feedAdd(kind,url));
    feedView[kind]='mine';renderFeeds();toast((source?.title||'Source')+' added to '+feedLabel(kind)+'.');
  }catch(e){
    if(button){button.disabled=false;button.textContent='＋ Follow';}
    toast('Could not add this source: '+e.message);
  }
}
function feedAddDialog(){
  const kind=route;
  modal('Add an RSS feed',`<p class="muted">Add a public RSS or Atom address to ${esc(feedLabel(kind))}.</p><label for="feed-url">Feed address</label><input id="feed-url" type="url" placeholder="https://example.com/feed.xml"><div class="row"><button id="subscribe" class="primary">Add feed</button><span id="feed-add-status" class="muted"></span></div>`,()=>on('subscribe','click',async()=>{
    $('subscribe').disabled=true;$('feed-add-status').textContent='Fetching feed…';
    try{applyFeedPayload(await api.feedAdd(kind,$('feed-url').value.trim()));closeModal();feedView[kind]='mine';renderFeeds();toast('Feed added.');}
    catch(e){$('feed-add-status').textContent=e.message;if($('subscribe'))$('subscribe').disabled=false;}
  }));
}
function feedTopicsDialog(){
  const kind=route;
  if(!['News','Journals'].includes(kind))return;
  const chosen=new Set(feedTopics(kind));
  modal('Choose topics',`<p class="muted">Topics filter publishers and individual stories. Stories stay saved either way.</p><div class="topic-grid">${FEED_TOPICS.map(topic=>`<label class="topic-choice"><input type="checkbox" value="${esc(topic)}" ${chosen.has(topic)?'checked':''}> ${esc(topic)}</label>`).join('')}</div><div class="row"><button id="topics-apply" class="primary">Apply</button><button id="topics-all">All topics</button></div>`,()=>{
    on('topics-apply','click',run(async()=>{
      const selected=[...$('dialog-content').querySelectorAll('input[type=checkbox]:checked')].map(input=>input.value);
      state.settings=await api.settings({feedTopics:{...(state.settings.feedTopics||{}),[kind]:selected}});
      closeModal();renderFeeds();
    }));
    on('topics-all','click',run(async()=>{
      state.settings=await api.settings({feedTopics:{...(state.settings.feedTopics||{}),[kind]:[]}});
      closeModal();renderFeeds();
    }));
  });
}
async function toggleFeedOrder(){
  const kind=route;if(!['News','Journals'].includes(kind))return;
  const next=feedOrder(kind)==='latest'?'popular':'latest';
  state.settings=await api.settings({feedOrder:{...(state.settings.feedOrder||{}),[kind]:next}});
  renderFeeds();toast(next==='latest'?'Latest stories first.':'Most opened stories first.');
}
function confirmRemoveFeed(id){
  const feed=feeds.find(f=>f.id===id);if(!feed)return;
  modal(feed.kind==='Podcasts'?'Remove podcast?':'Remove from My list?',`<p>${esc(plain(feed.title))}</p><p class="muted">Saved stories for this source are removed. Podcast playback positions are kept.</p><div class="row"><button id="confirm-unsubscribe" class="danger">Remove</button><button id="keep-subscription">Cancel</button></div>`,()=>{
    on('keep-subscription','click',closeModal);
    on('confirm-unsubscribe','click',run(async()=>{applyFeedPayload(await api.feedRemove(id));if(activeFeed===id)activeFeed=null;closeModal();renderFeeds();}));
  });
}
async function refreshFeed(id){return fetchLatestFeed(id,true);}
function renderSettings(){$('main').innerHTML=`<div class="settings"><div class="surface-heading">${illustration('settings','surface-art')}<div><h2>Make yourself at home.</h2><p class="muted">Reading and playback preferences are saved on this computer.</p></div></div><div class="setting"><div><h3>Appearance</h3><p>A quiet space, day or night.</p></div><select id="theme"><option value="system">Follow Windows</option><option value="light">Light</option><option value="dark">Dark</option></select></div><div class="setting"><div><h3>Skip interval</h3><p>Rewind and forward buttons.</p></div><select id="skip-setting">${[5,10,15,30,60,120].map(n=>`<option value="${n}">${n} seconds</option>`).join('')}</select></div><div class="setting"><div><h3>EPUB font size</h3><p>Applied to your reflowable books.</p></div><input id="font-setting" type="number" min="10" max="40" value="${state.settings.fontSize||19}" aria-label="EPUB font size"></div><div class="setting"><div><h3>Downloads</h3><p>Imports and downloads share Data / Books in named folders.</p></div><button data-action="files">Open folder ↗</button></div><div class="setting"><div><h3>Clavis for Windows</h3><p>Python desktop edition 0.2.5 · Based on your Clavis Android project.</p></div></div><p class="notice" style="margin-top:25px">This first desktop build includes local books, playback, PDF ink, EPUB highlights, feeds, typed journals and magnet transfers. EPUB and PDF books can be read aloud offline from the current chapter or page with the built-in Kitten voice. Journals also support handwriting. Embedded chapters and reviewed offline spoken-heading scans are supported.</p></div>`;$('theme').value=state.settings.theme||'system';$('skip-setting').value=state.settings.skip||30;on('theme','change',()=>settings({theme:$('theme').value}));on('skip-setting','change',()=>settings({skip:Number($('skip-setting').value)}));on('font-setting','change',()=>settings({fontSize:Number($('font-setting').value)}));}
function renderNotes(){renderNotesContent();journalDrawingControls();}
function renderNotesContent(){const n=state.notes.find(n=>n.id===activeNote);$('main').innerHTML=`<div class="toolbar"><span class="muted">A place for your thoughts.</span><button class="primary" data-action="new-note">＋ New journal entry</button></div><div class="note-layout"><div class="note-list">${state.notes.map(n=>`<button data-note="${n.id}"><strong>${esc(n.title)}</strong><br><small>${date(n.updated)}</small></button>`).join('')||'<p class="muted">No entries yet.</p>'}</div><div>${n?`<div class="note-editor"><input id="note-title" value="${esc(n.title)}" placeholder="Entry title" aria-label="Entry title"><textarea id="note-text" placeholder="Start writing…" aria-label="Journal entry">${esc(n.text)}</textarea><div class="row spread"><small id="note-status">Saved on this computer</small><div class="row"><button id="note-export">Export text</button><button id="note-delete" class="danger">Delete entry</button></div></div></div>`:'<div class="empty"><img class="ui-illustration empty-art" src="../assets/pastel/bookmarks.png" alt=""><h2>Leave a little room to reflect.</h2><p>Create an entry and start writing.</p></div>'}</div></div>`;if(n){const changed=()=>{n.title=$('note-title').value;n.text=$('note-text').value;$('note-status').textContent='Saving…';clearTimeout(noteTimer);noteTimer=setTimeout(run(async()=>{await api.saveNote(n);if($('note-status'))$('note-status').textContent='Saved on this computer';}),600);};on('note-title','input',changed);on('note-text','input',changed);on('note-export','click',async()=>{await flushNote();if(await api.exportNote(n.id))toast('Entry exported.');});on('note-delete','click',()=>modal('Delete journal entry?',`<p>Delete “${esc(n.title)}” permanently?</p><div class="row"><button id="confirm-delete-note" class="danger">Delete entry</button><button id="keep-note">Keep entry</button></div>`,()=>{on('keep-note','click',closeModal);on('confirm-delete-note','click',async()=>{clearTimeout(noteTimer);state.notes=await api.deleteNote(n.id);activeNote=null;closeModal();renderNotes();});}));}}
async function flushNote(){clearTimeout(noteTimer);const n=state.notes.find(n=>n.id===activeNote);if(n&&route==='Journalling')await api.saveNote(n);}
function journalDrawingControls(){const n=state.notes.find(n=>n.id===activeNote);if(!n||!document.querySelector('.note-editor'))return;const editor=document.querySelector('.note-editor');editor.insertAdjacentHTML('beforeend','<div class="row"><button id="journal-draw-toggle">✎ Open handwriting page</button></div><div id="journal-drawing" hidden><div class="row wrap"><select id="journal-tool" aria-label="Handwriting tool"><option value="pen">Pen</option><option value="highlight">Highlighter</option><option value="underline">Straight underline</option></select><input id="journal-color" type="color" value="#292664" aria-label="Handwriting color"><button id="journal-undo">Undo stroke</button><button id="journal-export">Export drawing</button></div><canvas id="journal-canvas" width="1000" height="1300" aria-label="Handwriting page"></canvas></div>');
  const canvas=$('journal-canvas'),ctx=canvas.getContext('2d');n.drawing||=[];
  const draw=preview=>{ctx.fillStyle='#fff';ctx.fillRect(0,0,1000,1300);ctx.strokeStyle='#e5e8f0';ctx.lineWidth=1;ctx.beginPath();for(let y=60;y<1300;y+=40){ctx.moveTo(30,y);ctx.lineTo(970,y);}ctx.stroke();for(const s of [...n.drawing,...(preview?[preview]:[])]){ctx.strokeStyle=s.color;ctx.lineWidth=s.tool==='highlight'?22:3;ctx.globalAlpha=s.tool==='highlight'?.3:1;ctx.lineCap='round';ctx.lineJoin='round';ctx.beginPath();const points=s.tool==='underline'&&s.points.length>1?[s.points[0],s.points.at(-1)]:s.points;points.forEach((p,i)=>{if(!i)ctx.moveTo(p[0]*1000,p[1]*1300);else ctx.lineTo(p[0]*1000,p[1]*1300);});ctx.stroke();}ctx.globalAlpha=1;};draw();
  let stroke;const point=e=>{const box=canvas.getBoundingClientRect();return [(e.clientX-box.left)/box.width,(e.clientY-box.top)/box.height];};canvas.onpointerdown=e=>{e.preventDefault();canvas.setPointerCapture(e.pointerId);stroke={tool:$('journal-tool').value,color:$('journal-color').value,points:[point(e)]};};canvas.onpointermove=e=>{if(stroke){stroke.points.push(point(e));draw(stroke);}};canvas.onpointerup=run(async()=>{if(stroke){n.drawing.push(stroke);stroke=null;draw();await api.saveNote(n);}});on('journal-draw-toggle','click',()=>{$('journal-drawing').hidden=!$('journal-drawing').hidden;});on('journal-undo','click',async()=>{n.drawing.pop();draw();await api.saveNote(n);});on('journal-export','click',async()=>{await api.saveNote(n);if(await api.exportDrawing(n.id,canvas.toDataURL('image/png')))toast('Handwriting exported.');});
}
async function newNote(){await flushNote();const n=await api.saveNote({title:'Untitled entry',text:''});state.notes.unshift(n);activeNote=n.id;renderNotes();$('note-title')?.focus();}
function renderDownloads(){$('main').innerHTML=`<div class="toolbar"><span class="muted">Audiobooks and documents · BitTorrent magnets</span><button class="primary" data-action="add-download">＋ Add magnet link</button></div><p class="notice">Completed books import automatically. Files are kept in the app’s Data / Books folder. Transfer speed depends on available peers; a link may wait for seeders.</p><div id="download-list">${downloadState.length?downloadState.map(j=>`<div class="download"><div class="download-heading">${illustration('downloads')}<h3>${esc(j.title)}</h3><span class="pill">${esc(j.status)}</span></div><div class="progress"><span style="width:${j.progress*100}%"></span></div><div class="row spread"><small>${(j.progress*100).toFixed(1)}% · ${(j.speed/1024).toFixed(0)} KB/s · ${j.peers} peers${j.error?' · '+esc(j.error):''}</small><div class="row">${j.status==='Complete'?`<button data-download-action="open" data-id="${j.id}">Open folder</button>`:`<button data-download-action="${j.status==='Paused'||j.status==='Error'?'resume':'pause'}" data-id="${j.id}">${j.status==='Paused'||j.status==='Error'?'Resume':'Pause'}</button>`}<button data-download-action="remove" data-id="${j.id}">Remove · keep files</button></div></div></div>`).join(''):'<div class="empty"><h2>Your downloads will appear here.</h2><p>Paste a magnet link to add a transfer.</p></div>'}</div>`;}
function addDownload(){modal('Add a download','<label for="magnet">Magnet link</label><textarea id="magnet" rows="4" placeholder="magnet:?xt=urn:btih:…"></textarea><div class="row"><button id="start-download" class="primary">Start download</button></div>',()=>on('start-download','click',async()=>{downloadState=await api.downloadAdd($('magnet').value);closeModal();renderDownloads();}));}

async function openReader(b){
  await cleanupReader();document.body.classList.remove('playing');route='Reader';renderNavigation();document.body.classList.add('reading');$('heading').textContent=b.title;$('eyebrow').textContent=b.kind+' READER';$('import').hidden=true;$('search').hidden=true;renderMini();
  const generation=readerGeneration;
  $('main').innerHTML=`<div class="reader-shell"><div class="reader-toolbar"><button id="reader-back">‹ Library</button><div class="reader-tools"><label class="reader-width-control">Width <input id="reader-width" type="range" min="8" max="60" step="0.1" aria-label="Reader width in centimetres"><output id="reader-width-value"></output></label><label class="reader-width-control">Height <input id="reader-height" type="range" min="6" max="60" step="0.1" aria-label="Reader height in centimetres"><output id="reader-height-value"></output></label><input id="reader-find" class="reader-find" type="search" placeholder="Search book" aria-label="Search book"><button id="reader-search">Find</button><button id="reader-bookmark" aria-label="Bookmark current page">⚑ Bookmark</button><button id="reader-marks">Bookmarks</button>${b.kind==='EPUB'?'<button id="reader-type">Aa</button><button id="reader-highlight">Highlight selection</button>':'<button id="ink-toggle">✎ Pen</button><select id="ink-kind" aria-label="Drawing tool"><option value="pen">Pen</option><option value="highlight">Highlighter</option><option value="underline">Underliner</option></select><input id="ink-color" class="ink-color" type="color" value="#7971ae" aria-label="Ink color"><button id="ink-undo">Undo</button><button id="pdf-zoom-out" aria-label="Zoom out">−</button><button id="pdf-zoom-in" aria-label="Zoom in">＋</button>'}</div></div><div class="reader-canvas"><button id="reader-previous" class="reader-page-side" aria-label="Previous page">‹</button><div class="reader-stage" id="reader-stage"><div class="loading">Opening ${b.kind}…</div></div><button id="reader-next" class="reader-page-side" aria-label="Next page">›</button></div><div class="reader-footer"><div class="row"><button id="reader-listen" class="listen-pill">♪ Listen</button><button id="reader-outline">☷ Outline</button></div><div class="row"><span id="reader-position" class="muted"></span><button id="reader-jump">Go to…</button></div><span class="muted" id="reader-percent"></span></div></div>`;
  reader={book:b,page:Math.floor(b.page)||1,selected:null,generation};
  bindReadingWidth();$('reader-stage').addEventListener('wheel',()=>{if(listening)listening.holdUntil=Date.now()+8000;},{passive:true});
  on('reader-back','click',()=>navigate(b.kind));on('reader-bookmark','click',readerBookmark);on('reader-marks','click',readerBookmarks);on('reader-outline','click',readerOutline);on('reader-search','click',readerSearch);on('reader-find','keydown',e=>{if(e.key==='Enter')return readerSearch();});on('reader-jump','click',readerJump);on('reader-previous','click',()=>readerMove(-1));on('reader-next','click',()=>readerMove(1));on('reader-listen','click',listenFromReader);  try{
    const response=await fetch(b.url);if(!response.ok)throw Error('The source file could not be opened.');const bytes=new Uint8Array(await response.arrayBuffer());if(generation!==readerGeneration)return;
    if(b.kind==='PDF')await openPDF(bytes,generation);else await openEPUB(bytes,generation);
  }catch(e){if(generation===readerGeneration){$('reader-stage').innerHTML=`<div class="empty"><h2>This book could not be opened.</h2><p>${esc(e.message)}</p><p>Check that the file is still in its original location and available offline.</p></div>`;toast(e.message);}}
}
function applyReadingWidth(){
  const width=readingWidth(state.settings.readerWidth),height=Math.max(6,Math.min(60,Number(state.settings.readerHeight)||17));
  document.querySelector('.reader-shell')?.style.setProperty('--reading-height',height+'cm');
  if($('reader-height'))$('reader-height').value=height;
  if($('reader-height-value'))$('reader-height-value').textContent=height.toFixed(1)+' cm';
  document.querySelector('.reader-shell')?.style.setProperty('--reading-width',width+'cm');
  const panel=$('listen-panel');
  if(panel){panel.style.setProperty('--reading-width',width+'cm');panel.style.setProperty('--listen-size',(state.settings.fontSize||19)+'px');panel.style.setProperty('--listen-leading',state.settings.lineHeight||1.7);panel.style.setProperty('--listen-margin',(state.settings.margin??32)+'px');}
  if($('reader-width-value'))$('reader-width-value').textContent=width.toFixed(1)+' cm';
  if($('reader-width'))$('reader-width').value=width;
}
function bindReadingWidth(){
  applyReadingWidth();
  on('reader-height','input',()=>{state.settings.readerHeight=Number($('reader-height').value);applyReadingWidth();requestAnimationFrame(()=>reader?.rendition?.resize());});
  on('reader-height','change',async()=>{state.settings=await api.settings({readerHeight:Number($('reader-height').value)});applyReadingWidth();});
  on('reader-width','input',()=>{state.settings.readerWidth=readingWidth($('reader-width').value);applyReadingWidth();requestAnimationFrame(()=>reader?.rendition?.resize());});
  on('reader-width','change',async()=>{state.settings=await api.settings({readerWidth:readingWidth($('reader-width').value)});applyReadingWidth();});
}
function decorateReaderNarration(contents){
  const s=listening;if(!s||!reader?.listenSections)return;
  const chapterIndex=reader.listenSections.findIndex(item=>item.index===contents.sectionIndex);
  const chapter=s.doc.chapters[chapterIndex];if(!chapter)return;
  const doc=contents.document,win=doc.defaultView;
  if(!doc.getElementById('clavis-narration-style')){
    const style=doc.createElement('style');style.id='clavis-narration-style';
    const rgb=document.body.classList.contains('dark')?'221,223,243':'41,38,100';
    style.textContent='::highlight(clavis-listen-muted){color:rgba('+rgb+',.5);background-color:transparent}::highlight(clavis-listen-spoken){color:rgb('+rgb+');background-color:transparent}';
    doc.head.append(style);
  }
  const all=doc.createRange();all.selectNodeContents(doc.body);
  const muted=new win.Highlight(all);muted.priority=0;
  win.CSS.highlights.set('clavis-listen-muted',muted);
  s.groups=markSentences(doc.body,s.doc.text,chapter,true);
  s.contents=contents;s.contentChapter=chapterIndex;
  if(chapterIndex===s.chapter){s.sentenceEls=s.groups;s.lastSentence=-1;updateListenHighlight(false);}
}
function renderFormattedListen(index,chapter){
  const s=listening,section=reader?.listenSections?.[index];
  if(!s||!section||reader.book.kind!=='EPUB')return;
  s.rendition=reader.rendition;
  const contents=s.rendition.getContents().find(item=>item.sectionIndex===section.index);
  if(contents){decorateReaderNarration(contents);return;}
  s.displaying=true;
  s.rendition.display(section.href).then(()=>{
    if(listening!==s||s.chapter!==index)return;
    s.displaying=false;
    const contents=s.rendition.getContents().find(item=>item.sectionIndex===section.index);
    if(contents)decorateReaderNarration(contents);
    updateListenHighlight(true);
  }).catch(error=>{s.displaying=false;setListenStatus(error.message);});
}
function followListenPage(group){
  const s=listening;if(!s?.rendition||s.displaying||!s.contents||!group?.length)return;
  if(s.contentChapter!==s.chapter){renderFormattedListen(s.chapter,s.doc.chapters[s.chapter]);return;}
  const range=group[0];if(!range.startContainer.isConnected)return;
  const rect=range.getBoundingClientRect(),frame=range.startContainer.ownerDocument.defaultView.frameElement.getBoundingClientRect(),stage=$('reader-stage').getBoundingClientRect();
  if(rect.left+frame.left>=stage.left&&rect.left+frame.left<stage.right)return;
  const target=range.cloneRange();target.collapse(true);
  const cfi=s.contents.cfiFromRange(target);
  s.displaying=true;s.rendition.display(cfi).finally(()=>{if(listening===s)s.displaying=false;}).catch(error=>setListenStatus(error.message));
}
async function currentNarrationPosition(doc,target){
  if(!reader?.rendition)return doc.position||0;
  const location=reader.rendition.currentLocation()||reader.location;
  if(!location?.start.cfi)return doc.position||0;
  let range=await reader.rendition.getRange(typeof target==='string'&&target.startsWith('epubcfi(')?target:location.start.cfi);
  if(typeof target==='string'&&target.includes('#')){
    const contents=reader.rendition.getContents().find(item=>item.sectionIndex===location.start.index);
    const anchor=contents?.document.getElementById(decodeURIComponent(target.slice(target.indexOf('#')+1)));
    if(anchor){range=anchor.ownerDocument.createRange();range.setStartBefore(anchor);range.collapse(true);}
  }
  if(!range)return doc.position||0;
  const prefix=range.startContainer.ownerDocument.createRange();prefix.selectNodeContents(range.startContainer.ownerDocument.body);prefix.setEnd(range.startContainer,range.startOffset);
  const significant=text=>Array.from(text.replace(/\u00ad/g,'').replace(/-\r?\n/g,'')).filter(char=>! /\s/u.test(char));
  const count=significant(prefix.toString()).length;
  const index=reader.listenSections.findIndex(item=>item.index===location.start.index);
  const chapter=doc.chapters[index];if(!chapter)return doc.position||0;
  let seen=0,position=chapter.start;
  for(const char of Array.from(doc.text).slice(position,chapter.end)){if(seen>=count)break;if(significant(char).length)seen++;position++;}
  return position;
}
async function openEPUB(bytes,generation){
  $('reader-stage').innerHTML='<div id="epub-host" class="epub-host"></div>';
  const book=ePub(bytes.buffer);reader.epub=book;
  const rendition=book.renderTo('epub-host',{width:'100%',height:'100%',spread:'none',flow:'paginated',allowScriptedContent:false});reader.rendition=rendition;
  rendition.themes.default(readingTheme(state.settings,document.body.classList.contains('dark')));
  rendition.on('relocated',location=>{if(generation!==readerGeneration)return;reader.location=location;const percent=book.locations.length()?book.locations.percentageFromCfi(location.start.cfi)*100:Math.min(99,location.start.index/Math.max(1,book.spine.length)*100);$('reader-position').textContent=`Section ${location.start.index+1} of ${book.spine.length}`;$('reader-percent').textContent=Math.round(percent)+'%';clearTimeout(reader.saveTimer);reader.saveTimer=setTimeout(run(()=>updateBook(reader.book,{cfi:location.start.cfi,progress:percent})),400);});
  rendition.on('selected',(cfiRange,contents)=>{if(generation!==readerGeneration)return;reader.selected=cfiRange;reader.selectionText=contents.window.getSelection()?.toString()||'';toast('Text selected. Choose Highlight selection to save it.');});
  rendition.hooks.content.register(contents=>{const hold=()=>{if(listening)listening.holdUntil=Date.now()+8000;};contents.document.addEventListener('wheel',hold,{passive:true});contents.document.addEventListener('pointerdown',hold);if(listening)requestAnimationFrame(()=>decorateReaderNarration(contents));const fontStyle=contents.document.createElement('style');fontStyle.textContent=readingFontCSS(new URL('../assets/',location.href).href);contents.document.head.append(fontStyle);contents.document.addEventListener('keydown',e=>{if(e.key==='ArrowRight'){e.preventDefault();run(()=>readerMove(1))();}if(e.key==='ArrowLeft'){e.preventDefault();run(()=>readerMove(-1))();}});contents.document.addEventListener('click',e=>{const a=e.target.closest('a');if(a&&/^https?:/.test(a.href)){e.preventDefault();run(()=>api.openURL(a.href))();}});});
  await rendition.display(reader.book.cfi||undefined);if(generation!==readerGeneration)return;
  reader.outline=(await book.loaded.navigation).toc;
  for(const cfi of reader.book.highlights||[])try{rendition.annotations.highlight(cfi,{},null,'saved-highlight',{'fill':'#e7c36b','fill-opacity':'.4'});}catch{}
  on('reader-type','click',typeDialog);on('reader-highlight','click',async()=>{if(!reader.selected)return toast('Select some book text first.');const cfi=reader.selected;rendition.annotations.highlight(cfi,{},null,'saved-highlight',{'fill':'#e7c36b','fill-opacity':'.4'});await updateBook(reader.book,{highlights:[...(reader.book.highlights||[]),cfi]});reader.selected=null;toast('Highlight saved.');});
  book.locations.generate(1800).then(()=>{if(generation===readerGeneration&&reader.location)$('reader-percent').textContent=Math.round(book.locations.percentageFromCfi(reader.location.start.cfi)*100)+'%';}).catch(()=>{});
}
function typeDialog(){modal('Reading appearance',`<label for="reader-font">Font size <span id="reader-font-value">${state.settings.fontSize||19}</span> px</label><input id="reader-font" type="range" min="10" max="40" step="1" value="${state.settings.fontSize||19}"><label for="reader-leading">Line spacing</label><input id="reader-leading" type="range" min="1" max="2.5" step=".1" value="${state.settings.lineHeight||1.7}"><label for="reader-margin">Margins</label><input id="reader-margin" type="range" min="0" max="100" step="4" value="${state.settings.margin??32}"><div class="row"><button id="apply-type" class="primary">Apply</button></div>`,()=>{on('reader-font','input',()=>{$('reader-font-value').textContent=$('reader-font').value;});on('apply-type','click',async()=>{await settings({fontSize:Number($('reader-font').value),lineHeight:Number($('reader-leading').value),margin:Number($('reader-margin').value)});closeModal();const theme=readingTheme(state.settings,document.body.classList.contains('dark'));reader.rendition.themes.default(theme);for(const contents of reader.rendition.getContents()){let style=contents.document.getElementById('clavis-reader-appearance');if(!style){style=contents.document.createElement('style');style.id='clavis-reader-appearance';contents.document.head.append(style);}style.textContent=themeCSS(theme);}reader.rendition.resize();applyReadingWidth();});});}
async function openPDF(bytes,generation){
  const pdf=await pdfjs.getDocument({data:bytes,isEvalSupported:false,cMapUrl:new URL('./cmaps/',location.href).href,cMapPacked:true,standardFontDataUrl:new URL('./standard_fonts/',location.href).href,wasmUrl:new URL('./wasm/',location.href).href}).promise;
  if(generation!==readerGeneration){await pdf.destroy();return;}
  reader.pdf=pdf;reader.zoom=1;reader.rendered=new Set();reader.rendering=new Set();reader.ink=await api.getInk(reader.book.id);ink=reader.ink;inkTool='navigate';reader.outline=await pdf.getOutline()||[];
  const first=await pdf.getPage(1);reader.baseViewport=first.getViewport({scale:1});
  $('reader-stage').innerHTML='<div id="pdf-pages" class="pdf-pages"></div>';
  const maxWidth=$('reader-stage').clientWidth-45;
  reader.scale=Math.min(1.4,maxWidth/reader.baseViewport.width);
  const viewport=first.getViewport({scale:reader.scale});
  $('pdf-pages').innerHTML=Array.from({length:pdf.numPages},(_,i)=>`<div class="pdf-page" data-page="${i+1}" style="width:${viewport.width}px;height:${viewport.height}px"><canvas class="paper"></canvas><canvas class="ink"></canvas></div>`).join('');
  const observer=new IntersectionObserver(entries=>{for(const entry of entries)if(entry.isIntersecting)run(()=>renderPDFPage(Number(entry.target.dataset.page),generation))();},{root:$('reader-stage'),rootMargin:'500px'});reader.observer=observer;document.querySelectorAll('.pdf-page').forEach(el=>observer.observe(el));
  $('reader-stage').addEventListener('scroll',()=>{if(!reader||generation!==readerGeneration)return;const top=$('reader-stage').getBoundingClientRect().top;let nearest=null,dist=Infinity;for(const el of document.querySelectorAll('.pdf-page')){const d=Math.abs(el.getBoundingClientRect().top-top);if(d<dist){nearest=Number(el.dataset.page);dist=d;}}if(nearest){reader.page=nearest;pdfPosition();clearTimeout(reader.saveTimer);const b=reader.book;reader.saveTimer=setTimeout(run(()=>updateBook(b,{page:nearest,progress:nearest/pdf.numPages*100})),500);}},{passive:true});
  on('ink-toggle','click',()=>{inkTool=inkTool==='navigate'?$('ink-kind').value:'navigate';$('ink-toggle').textContent=inkTool==='navigate'?'✎ Pen':'✓ Drawing';document.querySelectorAll('.pdf-page').forEach(el=>el.classList.toggle('inking',inkTool!=='navigate'));});
  on('ink-kind','change',()=>{if(inkTool!=='navigate')inkTool=$('ink-kind').value;});on('ink-color','input',()=>{inkColor=$('ink-color').value;});on('ink-undo','click',async()=>{const list=ink[reader.page]||[];list.pop();drawInk(reader.page);await api.saveInk(reader.book.id,ink);});on('pdf-zoom-in','click',()=>zoomPDF(1.2));on('pdf-zoom-out','click',()=>zoomPDF(1/1.2));
  reader.page=Math.max(1,Math.min(pdf.numPages,reader.page));await renderPDFPage(reader.page,generation);pdfGo(reader.page);pdfPosition();
}
async function renderPDFPage(n,generation){
  const r=reader;if(!r||generation!==readerGeneration||r.rendered.has(n)||r.rendering.has(n))return;r.rendering.add(n);
  try{const page=await r.pdf.getPage(n);if(generation!==readerGeneration)return;const viewport=page.getViewport({scale:r.scale}),el=document.querySelector(`.pdf-page[data-page="${n}"]`);if(!el)return;el.style.width=viewport.width+'px';el.style.height=viewport.height+'px';const canvas=el.querySelector('.paper'),overlay=el.querySelector('.ink'),dpr=Math.min(devicePixelRatio||1,2);canvas.width=Math.round(viewport.width*dpr);canvas.height=Math.round(viewport.height*dpr);canvas.style.width=viewport.width+'px';canvas.style.height=viewport.height+'px';overlay.width=canvas.width;overlay.height=canvas.height;overlay.style.width=canvas.style.width;overlay.style.height=canvas.style.height;await page.render({canvasContext:canvas.getContext('2d'),viewport,transform:dpr!==1?[dpr,0,0,dpr,0,0]:undefined}).promise;if(generation!==readerGeneration)return;r.rendered.add(n);drawInk(n);bindInk(overlay,n);el.classList.toggle('inking',inkTool!=='navigate');
  }finally{r.rendering.delete(n);}
}
function drawInk(n,preview){const canvas=document.querySelector(`.pdf-page[data-page="${n}"] .ink`);if(!canvas)return;const ctx=canvas.getContext('2d');ctx.clearRect(0,0,canvas.width,canvas.height);for(const stroke of [...(ink[n]||[]),...(preview?[preview]:[])]){if(!stroke.points.length)continue;ctx.beginPath();ctx.lineCap='round';ctx.lineJoin='round';ctx.strokeStyle=stroke.color;ctx.globalAlpha=stroke.tool==='highlight'?.3:1;ctx.lineWidth=(stroke.width||3)*(canvas.width/600);const points=stroke.tool==='underline'&&stroke.points.length>1?[stroke.points[0],stroke.points.at(-1)]:stroke.points;points.forEach((p,i)=>{const x=p[0]*canvas.width,y=p[1]*canvas.height;if(!i)ctx.moveTo(x,y);else ctx.lineTo(x,y);});ctx.stroke();}ctx.globalAlpha=1;}
function bindInk(canvas,n){let stroke=null;const point=e=>{const rect=canvas.getBoundingClientRect();return [(e.clientX-rect.left)/rect.width,(e.clientY-rect.top)/rect.height];};canvas.onpointerdown=e=>{if(inkTool==='navigate')return;e.preventDefault();canvas.setPointerCapture(e.pointerId);stroke={tool:inkTool,color:inkColor,width:inkTool==='highlight'?18:inkWidth,points:[point(e)]};};canvas.onpointermove=e=>{if(!stroke)return;stroke.points.push(point(e));drawInk(n,stroke);};const finish=run(async()=>{if(!stroke)return;(ink[n]||=[]).push(stroke);stroke=null;drawInk(n);await api.saveInk(reader.book.id,ink);});canvas.onpointerup=finish;canvas.onpointercancel=finish;}
function pdfPosition(){if(!reader?.pdf)return;$('reader-position').textContent=`Page ${reader.page} of ${reader.pdf.numPages}`;$('reader-percent').textContent=Math.round(reader.page/reader.pdf.numPages*100)+'%';}
function pdfGo(n){if(!reader?.pdf)return;reader.page=Math.max(1,Math.min(reader.pdf.numPages,Math.floor(n)));document.querySelector(`.pdf-page[data-page="${reader.page}"]`)?.scrollIntoView({block:'start'});pdfPosition();if(listening&&!listening.syncing)run(syncListenToReader)();run(()=>updateBook(reader.book,{page:reader.page,progress:reader.page/reader.pdf.numPages*100}))();}
async function zoomPDF(factor){if(!reader?.pdf)return;reader.scale=Math.min(4,Math.max(.3,reader.scale*factor));reader.rendered.clear();const n=reader.page;for(const el of document.querySelectorAll('.pdf-page')){el.style.width=reader.baseViewport.width*reader.scale+'px';el.style.height=reader.baseViewport.height*reader.scale+'px';}pdfGo(n);await renderPDFPage(n,readerGeneration);for(const el of document.querySelectorAll('.pdf-page')){const rect=el.getBoundingClientRect();if(rect.bottom>0&&rect.top<innerHeight+500)await renderPDFPage(Number(el.dataset.page),readerGeneration);}}
async function readerMove(delta){
  if(reader?.pdf)pdfGo(reader.page+delta);
  else if(reader?.rendition){await (delta>0?reader.rendition.next():reader.rendition.prev());await syncListenToReader();}
}
async function readerDisplay(target){await reader.rendition.display(target);await syncListenToReader(target);}
async function syncListenToReader(target){
  const s=listening;if(!s||s.syncing||s.displaying)return;
  s.syncing=true;
  try{
    const position=reader?.pdf?s.doc.chapters.find(item=>item.label==='Page '+reader.page)?.start:await currentNarrationPosition(s.doc,target);
    if(listening!==s||position==null)return;
    const playing=s.intent;s.holdUntil=Date.now()+500;
    await listenSeek(position,playing);
    const chapter=s.doc.chapters[listenChapterIndex(position)];s.followedSentence=chapter.sentences.findIndex(([a,b])=>position>=a&&position<b);
  }finally{s.syncing=false;}
}
async function readerBookmark(){if(!reader)return;const r=reader,mark={name:r.pdf?`Page ${r.page}`:`Section ${(r.location?.start.index||0)+1}`,page:r.page,cfi:r.location?.start.cfi||''};await updateBook(r.book,{bookmarks:[...(r.book.bookmarks||[]),mark]});toast('Reading bookmark saved.');}
function readerBookmarks(){if(!reader)return;modal('Reading bookmarks',`<div class="stack">${(reader.book.bookmarks||[]).map((b,i)=>`<div class="row"><button class="grow" data-reading-mark="${i}">${esc(b.name)}</button><button data-reading-remove="${i}" aria-label="Delete bookmark">✕</button></div>`).join('')||'<p class="muted">Bookmark a page to return to it.</p>'}</div>`,()=>{document.querySelectorAll('[data-reading-mark]').forEach(el=>el.onclick=run(async()=>{const b=reader.book.bookmarks[Number(el.dataset.readingMark)];closeModal();if(reader.pdf)pdfGo(b.page);else await readerDisplay(b.cfi);}));document.querySelectorAll('[data-reading-remove]').forEach(el=>el.onclick=run(async()=>{await updateBook(reader.book,{bookmarks:reader.book.bookmarks.filter((_,i)=>i!==Number(el.dataset.readingRemove))});readerBookmarks();}));});}
function readerOutline(){if(!reader)return;const flat=[];function flatten(list,depth=0){for(const item of list){flat.push({...item,depth});flatten(item.items||item.subitems||[],depth+1);}}flatten(reader.outline||[]);modal('Outline',`<div class="outline">${flat.map((t,i)=>`<button data-outline="${i}" style="padding-left:${15+t.depth*16}px">${esc(t.label||t.title||'Section')}</button>`).join('')||'<p class="muted">This book has no table of contents.</p>'}</div>`,()=>{document.querySelectorAll('[data-outline]').forEach(el=>el.onclick=run(async()=>{const item=flat[Number(el.dataset.outline)];closeModal();if(reader.pdf){const dest=typeof item.dest==='string'?await reader.pdf.getDestination(item.dest):item.dest;if(dest){const n=typeof dest[0]==='number'?dest[0]+1:await reader.pdf.getPageIndex(dest[0])+1;pdfGo(n);}}else await readerDisplay(item.href);}));});}
function readerJump(){if(!reader)return;const pdf=!!reader.pdf;modal(pdf?'Go to page':'Go to reading position',`<label for="jump-position">${pdf?'Page number':'Percentage (0–100)'}</label><input id="jump-position" type="number" min="${pdf?1:0}" max="${pdf?reader.pdf.numPages:100}" value="${pdf?reader.page:Math.round(reader.book.progress||0)}"><div class="row"><button id="jump-confirm" class="primary">Go</button></div>`,()=>on('jump-confirm','click',async()=>{const n=Number($('jump-position').value);closeModal();if(pdf)pdfGo(n);else if(reader.epub.locations.length())await reader.rendition.display(reader.epub.locations.cfiFromPercentage(Math.max(0,Math.min(1,n/100))));else toast('Book positions are still being indexed. Try again shortly.');}));}
async function readerSearch(){if(!reader)return;const term=$('reader-find').value.trim();if(!term)return;const r=reader,generation=readerGeneration;modal('Search book','<p class="muted" id="search-progress">Searching…</p><div id="book-search-results" class="stack"></div>');const results=[];
  if(r.pdf){for(let n=1;n<=r.pdf.numPages;n++){if(generation!==readerGeneration||!$('dialog').open)return;const p=await r.pdf.getPage(n),text=(await p.getTextContent()).items.map(x=>x.str).join(' '),at=text.toLowerCase().indexOf(term.toLowerCase());if(at>=0)results.push({label:`Page ${n} · ${text.slice(Math.max(0,at-50),at+100)}`,page:n});if(results.length>=100)break;if(n%20===0)$('search-progress').textContent=`Searching page ${n} of ${r.pdf.numPages}…`;}}
  else{for(const section of r.epub.spine.spineItems){if(generation!==readerGeneration||!$('dialog').open)return;await section.load(r.epub.load.bind(r.epub));for(const found of section.find(term))results.push({label:found.excerpt,cfi:found.cfi});section.unload();if(results.length>=100)break;}}
  if(generation!==readerGeneration||!$('dialog').open||!$('book-search-results'))return;$('search-progress').textContent=`${results.length}${results.length>=100?'+':''} matches`;$('book-search-results').innerHTML=results.slice(0,100).map((r,i)=>`<button data-search-result="${i}">${esc(r.label)}</button>`).join('');document.querySelectorAll('[data-search-result]').forEach(el=>el.onclick=run(async()=>{const found=results[Number(el.dataset.searchResult)];closeModal();if(r.pdf)pdfGo(found.page);else await readerDisplay(found.cfi);}));
}
// ---- Listen: offline narration for EPUB and PDF books ----
const MAX_LISTEN_TEXT=7.5*1024*1024;
let listenVoiceTimer=null;

function setListenStatus(text){const el=$('listen-status');if(el)el.textContent=text||'';}
function listenChapterIndex(position){const chapters=listening.doc.chapters;let index=0;for(let i=0;i<chapters.length;i++){if(chapters[i].start<=position)index=i;else break;}return index;}
function listenRangeAt(position){
  const chapters=listening.doc.chapters;let current=null;
  for(const chapter of chapters){if(position<chapter.start)break;current=chapter;if(position<=chapter.end)break;}
  if(current){const passages=current.passages||[];const found=passages.find(([a,b])=>position>=a&&position<b)||passages.find(([a])=>a>=position);if(found)return found;}
  const later=chapters.find(chapter=>chapter.start>position);
  return later?.passages?.[0]||null;
}
function renderListenChapter(force=false){
  const s=listening;if(!s)return;
  const index=listenChapterIndex(s.position);
  const chapter=s.doc.chapters[index];
  if(!chapter)return;
  if(force||s.chapter!==index){if(reader?.book.kind==='EPUB'){s.chapter=index;s.lastSentence=-1;s.followedSentence=-1;const label=$('listen-chapter-label');if(label)label.textContent=chapter.label;renderFormattedListen(index,chapter);return;}const text=s.doc.text;let at=chapter.start,html='';for(const [start,finish] of chapter.sentences){if(start>at)html+=esc(text.slice(at,start));html+=`<span class="listen-sentence">${esc(text.slice(start,finish))}</span>`;at=finish;}if(at<chapter.end)html+=esc(text.slice(at,chapter.end));$('listen-text').innerHTML=html;s.sentenceEls=[...$('listen-text').querySelectorAll('.listen-sentence')].map(el=>[el]);renderFormattedListen(index,chapter);s.lastSentence=-1;s.followedSentence=-1;s.chapter=index;const label=$('listen-chapter-label');if(label)label.textContent=chapter.label;const stage=$('listen-stage');if(stage)stage.scrollTop=0;force=true;}
  updateListenHighlight(force);
}
function updateListenHighlight(force=false){
  const s=listening;if(!s)return;const chapter=s.doc.chapters[s.chapter];if(!chapter)return;
  const index=chapter.sentences.findIndex(([a,b])=>s.position>=a&&s.position<b);
  if(index<0)return;
  if(s.rendition){const win=s.contents?.document.defaultView;if(win){const active=new win.Highlight(...(s.sentenceEls[index]||[]));active.priority=1;win.CSS.highlights.set('clavis-listen-spoken',active);}s.lastSentence=index;if(!s.intent)s.followedSentence=index;}
  else if(index!==s.lastSentence){s.sentenceEls[s.lastSentence]?.forEach(el=>el.classList.remove('active'));s.sentenceEls[index]?.forEach(el=>el.classList.add('active'));s.lastSentence=index;}
  if(force){if(s.rendition){if(s.intent)followListenPage(s.sentenceEls[index]);}else s.sentenceEls[index]?.[0]?.scrollIntoView({block:'center'});}
  else if(s.follow&&!listenAudio.paused&&Date.now()>=s.holdUntil&&index!==s.followedSentence){s.followedSentence=index;if(s.rendition)followListenPage(s.sentenceEls[index]);else s.sentenceEls[index]?.[0]?.scrollIntoView({block:'center',behavior:'smooth'});}
}
function renderListenDock(){
  const s=listening;if(!s)return;
  const chapter=s.doc.chapters[s.chapter];const total=s.doc.text.length||1;
  const location=$('listen-location');if(location)location.textContent=chapter?.label||'';
  const percent=$('listen-percent');if(percent)percent.textContent=Math.round(s.position/total*100)+'%';
  if($('listen-volume'))$('listen-volume').value=Math.round((state.settings.volume??.8)*100);
  const bar=$('listen-progress');if(bar&&!s.dragging)bar.value=Math.round(s.position/total*1000);
  const play=$('listen-play');if(play){play.innerHTML=transportIcon(listenAudio.paused?'play':'pause');play.setAttribute('aria-label',listenAudio.paused?'Play narration':'Pause narration');}
  const previous=$('listen-prev');if(previous)previous.disabled=s.chapter<=0;
  const next=$('listen-next');if(next)next.disabled=s.chapter>=s.doc.chapters.length-1;
}
function renderListenVoice(){
  const s=listening;if(!s)return;const voice=s.voice||{};
  const button=$('listen-download');if(button)button.hidden=!!(voice.installed||voice.downloading);
  if(voice.downloading)setListenStatus(`Downloading the offline voice… ${voice.progress||0}%`);
}
function watchListenVoice(){
  clearTimeout(listenVoiceTimer);
  const check=async()=>{
    if(!listening)return;let voice;
    try{voice=await api.listenVoice();}catch{return;}
    if(!listening)return;
    const wasInstalled=listening.voice?.installed;
    listening.voice=voice;renderListenVoice();
    if(voice.downloading){listenVoiceTimer=setTimeout(check,1200);return;}
    if(voice.installed&&!wasInstalled)setListenStatus('Offline voice ready.');
  };
  listenVoiceTimer=setTimeout(check,500);
}
async function downloadListenVoice(){
  if(!listening)return;
  listening.voice=await api.listenVoiceDownload();
  renderListenVoice();watchListenVoice();
}
function queueListenSave(){
  const s=listening;if(!s||s.saveTimer)return;
  s.saveTimer=setTimeout(()=>{s.saveTimer=null;if(listening===s)api.listenSave(s.doc.id,s.position).catch(()=>{});},2000);
}
async function listenChunkAt(position){
  const range=listenRangeAt(position);
  if(!range)return null;
  const prefetch=listening.prefetch;
  if(prefetch&&prefetch.range[0]===range[0]&&prefetch.range[1]===range[1]){
    listening.prefetch=null;
    try{return await prefetch.promise;}catch{return api.listenSpeak(listening.doc.id,range[0],range[1],listening.rate,listening.speaker);}
  }
  return api.listenSpeak(listening.doc.id,range[0],range[1],listening.rate,listening.speaker);
}
function listenPrefetch(chunk){
  const s=listening;if(!s)return;
  const range=listenRangeAt(chunk.end);
  if(!range)return;
  const promise=api.listenSpeak(s.doc.id,range[0],range[1],s.rate,s.speaker);
  promise.catch(()=>{});
  s.prefetch={range,promise};
}
function stopListenAudio(){
  const s=listening;if(!s)return;
  s.gen++;s.chunk=null;s.prefetch=null;
  listenAudio.pause();listenAudio.removeAttribute('src');listenAudio.load();
  setListenStatus('');
}
async function listenPlay(){
  const s=listening;if(!s)return;
  if(!s.voice?.installed){setListenStatus('Download the offline voice once to listen.');renderListenVoice();return;}
  if(!audio.paused)audio.pause();
  s.intent=true;
  if(s.position>=s.doc.text.length){s.position=0;renderListenChapter(true);}
  const generation=++s.gen;
  setListenStatus('Preparing speech…');renderListenDock();
  try{
    const chunk=await listenChunkAt(s.position);
    if(listening!==s||generation!==s.gen)return;
    if(!chunk){finishListen();return;}
    s.chunk=chunk;
    listenAudio.src=chunk.url;listenAudio.volume=state.settings.volume??.8;
    await listenAudio.play();
    if(generation===s.gen)setListenStatus('');
    listenPrefetch(chunk);
  }catch(e){
    if(listening===s&&generation===s.gen){
      if(e.name==='NotAllowedError')setListenStatus('Press Play to begin.');
      else{setListenStatus(e.message);toast(e.message);}
    }
  }finally{
    if(listening===s&&generation===s.gen)renderListenDock();
  }
}
function listenPause(){
  const s=listening;if(!s)return;
  s.intent=false;
  if(listenAudio.paused)return;
  const chunk=s.chunk;
  if(chunk&&Number.isFinite(listenAudio.duration)&&listenAudio.duration>0){const fraction=Math.min(1,listenAudio.currentTime/listenAudio.duration);s.position=Math.min(chunk.end,chunk.start+Math.round((chunk.end-chunk.start)*fraction));}
  listenAudio.pause();
  queueListenSave();renderListenChapter();renderListenDock();
}
async function toggleListenPlay(){
  if(!listening)return;
  if(listenAudio.paused)await listenPlay();else listenPause();
}
async function listenSeek(position,autoplay){
  const s=listening;if(!s)return;
  const target=Math.max(0,Math.min(s.doc.text.length,Math.round(position)));
  const chunk=s.chunk;
  if(chunk&&target>=chunk.start&&target<chunk.end&&listenAudio.src&&listenAudio.readyState>0){
    listenAudio.pause();
    const duration=Number.isFinite(listenAudio.duration)&&listenAudio.duration>0?listenAudio.duration:chunk.seconds||0;
    if(duration)listenAudio.currentTime=Math.min(duration-.05,Math.max(0,(target-chunk.start)/(chunk.end-chunk.start)*duration));
    s.position=target;renderListenChapter();renderListenDock();queueListenSave();
    if(autoplay)await listenAudio.play().catch(()=>{});
    return;
  }
  stopListenAudio();
  s.position=target;renderListenChapter();renderListenDock();queueListenSave();
  if(autoplay)await listenPlay();
}
async function listenSkip(words){
  const s=listening;if(!s)return;
  const playing=s.intent;
  const result=await api.listenPosition(s.doc.id,s.position,words);
  if(listening!==s)return;
  await listenSeek(result.position,playing);
}
function listenTick(){
  const s=listening;if(!s||!s.chunk||listenAudio.paused)return;
  const chunk=s.chunk;
  if(!Number.isFinite(listenAudio.duration)||listenAudio.duration<=0)return;
  const fraction=Math.min(1,listenAudio.currentTime/listenAudio.duration);
  s.position=Math.min(chunk.end,chunk.start+Math.round((chunk.end-chunk.start)*fraction));
  renderListenChapter();renderListenDock();queueListenSave();
}
function finishListen(){
  const s=listening;if(!s)return;
  s.intent=false;
  s.position=s.doc.text.length;s.chunk=null;
  listenAudio.pause();listenAudio.removeAttribute('src');
  setListenStatus('Finished · Play to listen again.');
  renderListenChapter();renderListenDock();queueListenSave();
}
async function listenEnded(){
  const s=listening;if(!s||!s.chunk)return;
  const chunk=s.chunk;
  s.position=chunk.end;s.chunk=null;queueListenSave();
  if(s.stopAfterChapter&&listenChapterIndex(chunk.end)!==listenChapterIndex(chunk.start)){s.stopAfterChapter=false;s.sleepLabel='';setListenStatus('Stopped at the end of the chapter.');renderListenChapter();renderListenDock();return;}
  if(chunk.end>=s.doc.text.length||!listenRangeAt(chunk.end)){finishListen();return;}
  await listenPlay();
}
async function restartListen(){
  const s=listening;if(!s)return;
  const playing=s.intent;
  stopListenAudio();renderListenChapter();renderListenDock();
  if(playing)await listenPlay();
}
async function setListenRate(rate){
  if(!listening)return;
  listening.rate=Math.max(.5,Math.min(2.5,rate));
  state.settings=await api.settings({listenRate:listening.rate});
  toast(`Narration speed: ${listening.rate}×.`);
  await restartListen();
}
async function setListenSpeaker(id){
  if(!listening)return;
  listening.speaker=[0,1,2].includes(id)?id:1;
  state.settings=await api.settings({listenSpeaker:listening.speaker});
  toast(`Narrator: ${listening.speaker===1?'Original voice':listening.speaker===2?'Deep male voice':'Hugo, male voice'}.`);
  await restartListen();
}
async function toggleListenFollow(){
  if(!listening)return;
  listening.follow=!listening.follow;listening.holdUntil=0;
  state.settings=await api.settings({listenFollow:listening.follow});
  toast(`Follow spoken text ${listening.follow?'on':'off'}.`);
}
function setListenSleep(minutes,atChapter=false){
  const s=listening;if(!s)return;
  clearTimeout(s.sleepTimer);s.sleepTimer=null;
  s.stopAfterChapter=atChapter;
  s.sleepLabel=atChapter?'end of chapter':minutes?`${minutes} min`:'';
  if(minutes)s.sleepTimer=setTimeout(()=>{if(!listening)return;listenPause();setListenStatus('Sleep timer finished.');listening.sleepLabel='';},minutes*60000);
  toast(atChapter?'Listening stops at the end of this chapter.':minutes?`Sleep timer: ${minutes} minutes.`:'Sleep timer off.');
}
function bindListenProgress(){
  const slider=$('listen-progress');if(!(slider instanceof HTMLInputElement))return;
  const stage=$('listen-stage');
  if(stage&&!stage.dataset.listenBound){stage.dataset.listenBound='1';const hold=()=>{if(listening)listening.holdUntil=Date.now()+8000;};stage.addEventListener('wheel',hold,{passive:true});stage.addEventListener('pointerdown',hold);}
  slider.addEventListener('pointerdown',()=>{if(!listening)return;listening.dragging=true;listening.resumeAfterSeek=listening.intent;listenAudio.pause();});
  slider.addEventListener('input',()=>{
    if(!listening)return;
    const chapter=listening.doc.chapters[listenChapterIndex(Number(slider.value)/1000*listening.doc.text.length)];
    const location=$('listen-location');if(location&&chapter)location.textContent=chapter.label;
    const percent=$('listen-percent');if(percent)percent.textContent=Math.round(Number(slider.value)/10)+'%';
  });
  slider.addEventListener('change',run(async()=>{
    if(!listening)return;
    const resume=listening.resumeAfterSeek;listening.dragging=false;
    await listenSeek(Number(slider.value)/1000*listening.doc.text.length,resume);
  }));
}
function listenSpeedDialog(){
  const rates=[.5,.75,.8,.9,1,1.25,1.5,1.75,2,2.5];
  modal('Narration speed',`<div class="stack">${rates.map(n=>`<button data-listen-rate="${n}"${n===listening.rate?' class="primary"':''}>${n}×${n===1?' · Normal':''}</button>`).join('')}</div>`,()=>{$('dialog-content').querySelectorAll('[data-listen-rate]').forEach(button=>button.onclick=run(async()=>{closeModal();await setListenRate(Number(button.dataset.listenRate));}));});
}
function listenSleepDialog(){
  modal('Sleep timer',`<div class="stack"><button data-listen-sleep="15">15 minutes</button><button data-listen-sleep="30">30 minutes</button><button data-listen-sleep="60">60 minutes</button><button id="listen-sleep-chapter">End of chapter</button><button id="listen-sleep-off">Turn off timer</button></div>`,()=>{
    document.querySelectorAll('[data-listen-sleep]').forEach(button=>button.onclick=()=>{closeModal();setListenSleep(Number(button.dataset.listenSleep));});
    on('listen-sleep-chapter','click',()=>{closeModal();setListenSleep(0,true);});
    on('listen-sleep-off','click',()=>{closeModal();setListenSleep(0);});
  });
}
function listenVoiceDialog(){
  const s=listening;if(!s)return;const voice=s.voice||{};
  const speakers=voice.speakers||[{id:1,label:'Original voice'},{id:0,label:'Hugo · male'},{id:2,label:'Deep male'}];
  modal('Narrator voice',`<p class="muted">The neural voice runs on this computer. The first use downloads 44 MB once.</p><div class="stack">${speakers.map(speaker=>`<button data-listen-speaker="${speaker.id}"${speaker.id===s.speaker?' class="primary"':''}>${esc(speaker.label)}</button>`).join('')}${voice.installed?'':`<button id="listen-voice-get" class="primary">${voice.downloading?`Downloading… ${voice.progress||0}%`:'Download offline voice · 44 MB'}</button>`}</div>`,()=>{
    document.querySelectorAll('[data-listen-speaker]').forEach(button=>button.onclick=run(async()=>{closeModal();await setListenSpeaker(Number(button.dataset.listenSpeaker));}));
    on('listen-voice-get','click',async()=>{closeModal();await downloadListenVoice();});
  });
}
function listenSettingsDialog(){
  if(!listening)return;
  const sleep=listening.sleepLabel?' · '+listening.sleepLabel:'';
  modal('Listen settings',`<div class="stack"><button data-listen-setting="speed">Speed · ${listening.rate}×</button><button data-listen-setting="sleep">Sleep timer${sleep}</button><button data-listen-setting="follow">Follow spoken text · ${listening.follow?'On':'Off'}</button>${reader?.rendition?'<button data-listen-setting="appearance">Text and spacing</button>':''}<button data-listen-setting="effects">Equalizer &amp; voice gain</button><button data-listen-setting="voice">Narrator voice · ${listening.speaker===1?'Original':listening.speaker===2?'Deep male':'Hugo · male'}</button><button data-listen-setting="stop">Stop listening</button></div>`,()=>{
    $('dialog-content').querySelectorAll('[data-listen-setting]').forEach(button=>button.onclick=()=>{
      const choice=button.dataset.listenSetting;
      if(choice==='speed')listenSpeedDialog();
      else if(choice==='sleep')listenSleepDialog();
      else if(choice==='follow'){closeModal();return toggleListenFollow();}
      else if(choice==='appearance'){closeModal();typeDialog();}
      else if(choice==='effects'){closeModal();equalizerDialog(listenAudio);}
      else if(choice==='voice')listenVoiceDialog();
      else{closeModal();return closeListen();}
    });
  });
}
async function collectEPUBText(from,note,cancelled){
  const book=reader?.epub;
  if(!book)throw Error('Open the book again to prepare listening.');
  const labels=new Map(),base=new Map();
  const flatten=list=>{for(const item of list||[]){if(item.href){const href=String(item.href).split('#')[0].replace(/^\.\//,'');if(!labels.has(href))labels.set(href,item.label||'');base.set(href.split('/').pop(),item.label||'');}flatten(item.subitems||item.items||[]);}};
  flatten(reader.outline||[]);
  const chapters=[];let size=0;reader.listenSections=[];
  for(let index=Math.max(0,from);index<book.spine.length;index++){
    if(cancelled())return [];
    note(`Reading section ${index+1} of ${book.spine.length}…`);
    const section=book.spine.get(index);
    if(!section)continue;
    const doc=await book.load(section.href);
    if(!doc?.body)continue;
    let text='';
    const clone=doc.body.cloneNode(true);
    clone.querySelectorAll('script,style,noscript,svg').forEach(el=>el.remove());
    clone.querySelectorAll('br').forEach(el=>el.replaceWith('\n'));
    clone.querySelectorAll('p,h1,h2,h3,h4,h5,h6,li,blockquote,pre,div,section,article,tr,figcaption').forEach(el=>el.append('\n\n'));
    text=clone.textContent||'';
    if(!text.trim())continue;
    const href=String(section.href||'').split('#')[0].replace(/^\.\//,'');
    reader.listenSections.push({index:section.index,href:section.href});
    chapters.push({label:labels.get(href)||base.get(href.split('/').pop())||`Section ${index+1}`,text});
    size+=text.length;
    if(size>MAX_LISTEN_TEXT)break;
  }
  return chapters;
}
async function collectPDFText(from,note,cancelled){
  const pdf=reader?.pdf;
  if(!pdf)throw Error('Open the PDF again to prepare listening.');
  const chapters=[];let size=0,skipped=0;
  for(let page=Math.max(1,from);page<=pdf.numPages;page++){
    if(cancelled())return {chapters:[],skipped:0};
    note(`Reading page ${page} of ${pdf.numPages}…`);
    const item=await pdf.getPage(page);
    let content;
    try{content=await item.getTextContent();}
    finally{item.cleanup();}
    let text='';
    for(const part of content.items){if(typeof part.str!=='string')continue;text+=part.str+(part.hasEOL?'\n':' ');}
    if(!text.trim()){skipped++;continue;}
    chapters.push({label:`Page ${page}`,text});
    size+=text.length;
    if(size>MAX_LISTEN_TEXT)break;
  }
  return {chapters,skipped};
}
async function listenFromReader(){
  const book=reader?.book;
  if(!book)return;
  if(!['EPUB','PDF'].includes(book.kind))return toast('Listening is available for EPUB and PDF books.');
  const from=book.kind==='PDF'?Math.max(1,reader.page||1):Math.max(0,reader.location?.start.index||0);
  let cancelled=false;
  const onClose=()=>{cancelled=true;};
  $('dialog').addEventListener('close',onClose,{once:true});
  modal('Preparing reading',`<p class="muted" id="listen-prep">Collecting text from this ${book.kind==='PDF'?'page':'chapter'}…</p><div class="row"><button id="listen-prep-cancel">Cancel</button></div>`,()=>on('listen-prep-cancel','click',()=>{cancelled=true;closeModal();}));
  const note=text=>{if($('listen-prep'))$('listen-prep').textContent=text;};
  try{
    let chapters=[],skipped=0;
    if(book.kind==='PDF')({chapters,skipped}=await collectPDFText(1,note,()=>cancelled));
    else chapters=await collectEPUBText(0,note,()=>cancelled);
    if(cancelled)return;
    if(!chapters.length)throw Error(book.kind==='PDF'?'No selectable text from this page. Scanned PDFs need OCR before listening.':'No readable text from this chapter onward.');
    note('Preparing the offline reading…');
    const doc=await api.listenPrepare({bookId:book.id,key:`book:${book.id}:${book.kind==='PDF'?'pdf':'epub'}:all`,title:book.title,chapters});
    if(cancelled)return;
    $('dialog').removeEventListener('close',onClose);
    closeModal();
    if(book.kind==='EPUB')doc.position=await currentNarrationPosition(doc);else doc.position=doc.chapters.find(item=>item.label==='Page '+from)?.start||0;
    openListen(doc,{note:skipped?`${skipped} page${skipped===1?'':'s'} without selectable text skipped.`:''});
  }catch(e){
    $('dialog').removeEventListener('close',onClose);
    if(!cancelled&&$('dialog').open)modal('Listen',`<p>${esc(e.message)}</p>`);
  }
}
async function listenArticle(feed,item,text){
  const body=String(text||'').trim();
  if(!body)return toast('Wait for the story to load, then listen.');
  try{
    const doc=await api.listenPrepare({bookId:'feed:'+item.id,key:'article:'+(item.link||feed.url+':'+item.id),title:plain(item.title)||feed.title,chapters:[{label:feed.title,text:body}]});
    openListen(doc);
  }catch(e){toast(e.message);}
}
function openListen(doc,options={}){
  const panel=$('listen-panel');
  if(!panel)return;
  const epub=reader?.book.kind==='EPUB';
  listening={doc,position:Math.max(0,Math.min(doc.text.length,doc.position||0)),chapter:-1,chunk:null,prefetch:null,gen:0,intent:false,rate:state.settings.listenRate||1,speaker:state.settings.listenSpeaker??1,follow:state.settings.listenFollow!==false,holdUntil:0,sleepTimer:null,sleepLabel:'',stopAfterChapter:false,dragging:false,resumeAfterSeek:false,saveTimer:null,voice:doc.voice||{installed:false},lastSentence:-1,followedSentence:-1,sentenceEls:[]};
  document.body.classList.add('listening');panel.hidden=false;panel.classList.toggle('paginated-listen',epub);for(const id of ['listen-page-prev','listen-page-next','listen-page-label'])$(id).hidden=!epub;applyReadingWidth();
  if(!audio.paused)audio.pause();
  renderListenChapter(true);renderListenDock();renderListenVoice();
  if(options.note)toast(options.note);
  setListenStatus(options.note||'');
  if(!listening.voice.installed){setListenStatus('Download the offline voice once to listen.');watchListenVoice();}
  else void listenPlay();
}
function bindListenPanel(){
  on('listen-back','click',()=>closeListen());
  on('listen-page-prev','click',()=>{if(listening?.rendition){listening.holdUntil=Date.now()+8000;return listening.rendition.prev();}});
  on('listen-page-next','click',()=>{if(listening?.rendition){listening.holdUntil=Date.now()+8000;return listening.rendition.next();}});
  on('listen-settings','click',listenSettingsDialog);
  on('listen-back30','click',()=>listenSkip(-30));
  on('listen-forward30','click',()=>listenSkip(30));
  on('listen-play','click',toggleListenPlay);
  on('listen-download','click',downloadListenVoice);
  bindListenProgress();
  on('listen-volume','input',()=>{const volume=Number($('listen-volume').value)/100;state.settings.volume=volume;listenAudio.volume=volume;});
  on('listen-volume','change',async()=>{state.settings=await api.settings({volume:Number($('listen-volume').value)/100});});
}
async function closeListen(){
  const s=listening;if(!s)return;
  listening=null;s.gen++;
  for(const contents of reader?.rendition?.getContents()||[]){contents.window.CSS.highlights.delete('clavis-listen-muted');contents.window.CSS.highlights.delete('clavis-listen-spoken');contents.document.getElementById('clavis-narration-style')?.remove();}
  clearTimeout(s.sleepTimer);clearTimeout(s.saveTimer);clearTimeout(listenVoiceTimer);
  listenAudio.pause();listenAudio.removeAttribute('src');
  document.body.classList.remove('listening');
  const panel=$('listen-panel');if(panel){panel.hidden=true;panel.classList.remove('paginated-listen');}
  if($('listen-chapter-label'))$('listen-chapter-label').textContent='';
  if($('listen-location'))$('listen-location').textContent='';
  try{await api.listenSave(s.doc.id,s.position);}catch{}
  renderMini();
}
listenAudio.addEventListener('timeupdate',listenTick);
listenAudio.addEventListener('ended',()=>run(listenEnded)());
listenAudio.addEventListener('play',renderListenDock);
listenAudio.addEventListener('pause',renderListenDock);

async function kindleDetect(){
  const result=await api.kindleDetect();
  kindleDevice=result.connected?result.device:null;
  return result;
}
async function kindleScan(){
  if(!kindleDevice)return;
  kindleScanning=true;
  renderKindle();
  try{
    const result=await api.kindleScan(kindleDevice);
    kindleBooks=result.books||[];
  }catch(e){toast(e.message);}
  finally{kindleScanning=false;renderKindle();}
}
async function importDeviceBooks(ids){
  if(!ids.length)return toast('Select at least one book to import.');
  try{
    const s=await api.kindleImport(ids);
    if(s){state=s;kindleBooks=kindleBooks.filter(b=>!ids.includes(b.id));toast(ids.length+' book(s) imported to library.');render();}
  }catch(e){toast(e.message);}
}
function kindleImportSelected(){
  return importDeviceBooks([...document.querySelectorAll('[data-device-select]:checked')].map(el=>el.dataset.deviceSelect));
}
function kindleMenu(id){
  const b=kindleBooks.find(x=>x.id===id);
  if(!b)return;
  const editable=String(b.format||'').toUpperCase()!=='KFX';
  const details=editable?'<button id="device-edit">Edit details…</button><button id="device-online">Download details…</button>':'';
  modal(b.title,`<div class="stack"><button id="device-import">Import to library</button>${details}<button id="device-remove" class="danger">Remove from Kindle…</button></div>`,()=>{
    on('device-import','click',()=>{closeModal();importDeviceBooks([id]);});
    if(editable){
      on('device-edit','click',()=>{closeModal();editDeviceMetadata(id);});
      on('device-online','click',()=>{closeModal();openMetadataLookup(b,candidate=>editDeviceMetadata(id,candidate));});
    }
    on('device-remove','click',async()=>{
      closeModal();
      try{
        const s=await api.kindleDeleteDeviceBook(id);
        if(s){kindleBooks=s.books||[];toast('Removed from Kindle (Recycle Bin).');renderKindle();}
      }catch(e){toast(e.message);}
    });
  });
}
function libraryMetadataDialog(id){return editBookMetadata(id);}
function kindleBookRow(b){
  const known=kindleArtCache.get('dev:'+b.path)||art(b.format==='PDF'?'PDF':'EPUB');
  return `<div class="book-row"><img class="book-cover" data-device-art="${b.id}" src="${esc(known)}" alt="" style="width:55px;height:66px;object-fit:contain;border-radius:7px;background:var(--soft);padding:5px"><span class="grow"><strong>${esc(b.title)}</strong><small>${esc(b.author||'Unknown author')}${b.format?' · '+esc(b.format):''}${b.drm?' · DRM':''}</small></span><label class="row" style="gap:6px"><input type="checkbox" data-device-select="${b.id}" style="width:auto">Select</label><button class="subtle" data-kindle-menu="${b.id}" aria-label="Options for ${esc(b.title)}">•••</button></div>`;
}
function libBookRow(b){
  const fmt=b.kind==='Kindle'?(b.kindleFormat||'MOBI').toUpperCase():b.kind==='PDF'?'PDF':'EPUB';
  const needsConvert=b.kind==='EPUB'?' · → AZW3':'';
  const known=b.cover||kindleArtCache.get('lib:'+b.id)||art(b.kind);
  return `<div class="book-row"><img class="book-cover" data-lib-art="${b.id}" src="${esc(known)}" alt="" style="width:55px;height:66px;object-fit:contain;border-radius:7px;background:var(--soft);padding:5px"><span class="grow"><strong>${esc(b.title)}</strong><small>${esc(b.author||'Unknown author')}${fmt?' · '+esc(fmt):''}${needsConvert}</small></span><label class="row" style="gap:6px"><input type="checkbox" data-lib-select="${b.id}" style="width:auto">Select</label><button class="subtle" data-lib-menu="${b.id}" aria-label="Options for ${esc(b.title)}">•••</button></div>`;
}
async function pdfThumbnail(url,width=96){
  if(!url)return null;
  const key=url+'|'+width;
  if(!pdfThumbCache.has(key)){
    pdfThumbCache.set(key,(async()=>{
      try{
        const probe=await fetch(url,{method:'HEAD'}).catch(()=>null);
        const size=Number(probe?.headers.get('content-length')||0);
        if(size>80*1024*1024)return null;
        const response=await fetch(url);
        if(!response.ok)return null;
        const bytes=new Uint8Array(await response.arrayBuffer());
        const doc=await pdfjs.getDocument({data:bytes,isEvalSupported:false}).promise;
        try{
          const page=await doc.getPage(1),base=page.getViewport({scale:1});
          if(!base.width)return null;
          const view=page.getViewport({scale:width/base.width});
          const canvas=document.createElement('canvas');
          canvas.width=Math.max(1,Math.round(view.width));
          canvas.height=Math.max(1,Math.round(view.height));
          await page.render({canvasContext:canvas.getContext('2d'),viewport:view}).promise;
          return canvas.toDataURL('image/jpeg',.7);
        }finally{doc.destroy();}
      }catch{return null;}
    })());
  }
  return pdfThumbCache.get(key);
}
function libraryMatch(b){
  const wanted=String(b.title||'').toLowerCase().replace(/[^a-z0-9]+/g,' ').trim();
  return state.books.find(x=>{
    if(!['EPUB','Kindle','PDF'].includes(x.kind))return false;
    if(b.asin&&x.asin===b.asin)return true;
    if(!wanted)return false;
    const title=String(x.title||'').toLowerCase().replace(/[^a-z0-9]+/g,' ').trim();
    if(!title)return false;
    return title===wanted||(wanted.length>6&&title.length>6&&(title.includes(wanted)||wanted.includes(title)));
  })||null;
}
async function kindleLibraryArt(book){
  if(book.cover)return book.cover;
  const cached=kindleArtCache.get('lib:'+book.id);
  if(cached)return cached;
  let src=null;
  if(book.kind==='PDF'&&book.url)src=await pdfThumbnail(book.url);
  if(!src)src=await api.bookCover(book.id).catch(()=>null);
  if(src)kindleArtCache.set('lib:'+book.id,src);
  return src;
}
async function loadKindleArtwork(){
  const queue=[];
  document.querySelectorAll('[data-lib-art]').forEach(img=>{
    const book=state.books.find(x=>x.id===img.dataset.libArt);
    if(!book||book.cover)return;
    queue.push(async()=>{const src=await kindleLibraryArt(book);if(src&&img.isConnected)img.src=src;});
  });
  document.querySelectorAll('[data-device-art]').forEach(img=>{
    const book=kindleBooks.find(x=>x.id===img.dataset.deviceArt);
    if(!book)return;
    const cached=kindleArtCache.get('dev:'+book.path);
    if(cached){img.src=cached;return;}
    queue.push(async()=>{
      let src=null;
      if(book.hasCover)src=await api.kindleCover(book.path).catch(()=>null);
      if(!src&&String(book.format).toUpperCase()==='PDF'){
        const url=await api.kindleMediaUrl(book.path).catch(()=>null);
        src=await pdfThumbnail(url);
      }
      if(!src){const library=libraryMatch(book);if(library)src=await kindleLibraryArt(library);}
      if(src){kindleArtCache.set('dev:'+book.path,src);if(img.isConnected)img.src=src;}
    });
  });
  const workers=Array.from({length:3},async()=>{while(queue.length)await queue.shift()();});
  await Promise.all(workers);
}
function bookDraft(b){
  return {title:b.title||'',author:b.author||'',series:b.series||'',seriesIndex:b.seriesIndex??'',publisher:b.publisher||'',published:b.published||'',isbn:b.isbn||'',subject:b.subject||'',description:b.description||'',cover:b.cover||'',coverData:null};
}
function seedFields(seed){
  return Object.fromEntries(Object.entries(seed||{}).filter(([,value])=>value!==undefined&&value!==null));
}
function readEditor(draft){
  draft.title=$('me-title').value.trim();
  draft.author=$('me-author').value.trim();
  draft.series=$('me-series').value.trim();
  draft.seriesIndex=$('me-series-index').value;
  draft.publisher=$('me-publisher').value.trim();
  draft.published=$('me-published').value.trim();
  draft.isbn=$('me-isbn').value.trim();
  draft.subject=$('me-subject').value.trim();
  draft.description=$('me-description').value.trim();
  return draft;
}
function editMetadataDialog(draft,save){
  const preview=draft.coverData||draft.cover||art('EPUB');
  modal('Edit book details',`<div class="meta-editor"><div class="meta-cover"><img id="me-cover" src="${esc(preview)}" alt=""><button id="me-cover-pick">Choose cover…</button></div><div class="meta-fields"><label for="me-title">Title</label><input id="me-title" value="${esc(draft.title)}"><label for="me-author">Author(s)</label><input id="me-author" value="${esc(draft.author)}"><div class="meta-pair"><div><label for="me-series">Series</label><input id="me-series" value="${esc(draft.series)}"></div><div><label for="me-series-index">Number</label><input id="me-series-index" type="number" min="0" step="0.1" value="${draft.seriesIndex??''}"></div></div><div class="meta-pair"><div><label for="me-publisher">Publisher</label><input id="me-publisher" value="${esc(draft.publisher)}"></div><div><label for="me-published">Published</label><input id="me-published" value="${esc(draft.published)}"></div></div><label for="me-isbn">ISBN</label><input id="me-isbn" value="${esc(draft.isbn)}"><label for="me-subject">Tags</label><input id="me-subject" value="${esc(draft.subject)}"><label for="me-description">Description</label><textarea id="me-description" rows="5">${esc(draft.description)}</textarea></div></div><div class="row meta-actions"><button id="me-online">Download metadata…</button><span class="grow"></span><button id="me-save" class="primary">Save</button><button id="me-cancel">Cancel</button></div>`,()=>{
    on('me-cover-pick','click',()=>{
      const input=document.createElement('input');
      input.type='file';input.accept='image/jpeg,image/png,image/webp';
      input.onchange=()=>{
        const file=input.files[0];if(!file)return;
        const reader=new FileReader();
        reader.onload=()=>{draft.coverData=reader.result;draft.cover=reader.result;$('me-cover').src=reader.result;};
        reader.readAsDataURL(file);
      };
      input.click();
    });
    on('me-cancel','click',closeModal);
    on('me-online','click',()=>{
      readEditor(draft);
      openMetadataLookup(draft,candidate=>{
        Object.assign(draft,{title:candidate.title,author:candidate.author,publisher:candidate.publisher,published:candidate.published,isbn:candidate.isbn,subject:candidate.subject,description:candidate.description});
        if(candidate.series){draft.series=candidate.series;draft.seriesIndex=candidate.seriesIndex??draft.seriesIndex;}
        if(candidate.coverData){draft.coverData=candidate.coverData;draft.cover=candidate.coverData;}
        editMetadataDialog(draft,save);
      });
    });
    on('me-save','click',async()=>{
      readEditor(draft);
      if(!draft.title)return toast('A title is required.');
      const patch={title:draft.title,author:draft.author,series:draft.series,publisher:draft.publisher,published:draft.published,isbn:draft.isbn,subject:draft.subject,description:draft.description};
      if(draft.seriesIndex!=='')patch.seriesIndex=Number(draft.seriesIndex);
      if(draft.coverData)patch.cover=draft.coverData;
      const button=$('me-save');button.disabled=true;
      try{await save(patch);closeModal();}
      catch(e){button.disabled=false;toast(e.message);}
    });
  });
}
async function editBookMetadata(id,seed){
  const book=state.books.find(x=>x.id===id);
  if(!book)return;
  const draft=Object.assign(bookDraft(book),seedFields(seed));
  editMetadataDialog(draft,async patch=>{
    const updated=await api.updateBookMetadata(book.id,patch);
    const index=state.books.findIndex(x=>x.id===book.id);
    if(index>=0)state.books[index]=updated;
    if(current?.id===book.id)Object.assign(current,updated);
    if(patch.cover)kindleArtCache.set('lib:'+book.id,patch.cover);
    renderKindle();toast('Book details saved.');
  });
}
function editDeviceMetadata(id,seed){
  const book=kindleBooks.find(x=>x.id===id);
  if(!book)return;
  const draft=Object.assign(bookDraft(book),{cover:kindleArtCache.get('dev:'+book.path)||''},seedFields(seed));
  editMetadataDialog(draft,async patch=>{
    const result=await api.kindleUpdateMetadata(book.path,patch);
    if(result){kindleBooks=result.books||kindleBooks;kindleArtCache.delete('dev:'+book.path);if(patch.cover)kindleArtCache.set('dev:'+book.path,patch.cover);renderKindle();toast('Details saved to the Kindle.');}
  });
}
async function useCandidate(candidate,apply){
  let cover=candidate.coverData||null;
  if(!cover&&candidate.coverUrl){
    cover=await api.metadataCover(candidate.coverUrl).catch(()=>null);
  }
  apply({title:candidate.title||'',author:candidate.author||'',publisher:candidate.publisher||'',published:candidate.published||'',isbn:candidate.isbn||'',subject:candidate.subject||'',description:candidate.description||'',coverData:cover,cover:cover||candidate.coverThumb||''});
}
function openMetadataLookup(seed,onPick){
  let title=String(seed.title||'').trim();
  const author=String(seed.author||'').trim();
  const last=author.split(/[\s,]+/).filter(Boolean).pop();
  if(last&&title.toLowerCase().includes(last.toLowerCase()))title=title.replace(/\s+[-–—]\s+.*$/,'').trim();
  const initial=[title,author].filter(Boolean).join(' ')||seed.isbn||'';
  modal('Download book details',`<p class="muted">Search Open Library, Internet Archive and Crossref, then review the result before saving.</p><div class="row"><input id="ml-query" class="grow" value="${esc(initial)}" placeholder="Title, author or ISBN"><button id="ml-search" class="primary">Search</button></div><div id="ml-results" class="meta-results"><p class="muted">Searching…</p></div>`,()=>{
    const search=async()=>{
      const query=$('ml-query').value.trim();
      if(!query)return;
      $('ml-results').innerHTML='<p class="muted">Searching Open Library, Internet Archive and Crossref…</p>';
      try{
        const results=await api.metadataLookup(query);
        if(!$('ml-results'))return;
        if(!results.length){$('ml-results').innerHTML='<p class="muted">No matches. Try the title and author, or paste the ISBN.</p>';return;}
        $('ml-results').innerHTML=results.map((c,i)=>`<button class="meta-result" data-meta="${i}">${c.coverThumb?`<img src="${c.coverThumb}" alt="">`:`<img src="${art('EPUB')}" alt="">`}<span class="grow"><strong>${esc(c.title)}</strong><small>${esc([c.author,(c.published||'').slice(0,10),c.publisher].filter(Boolean).join(' · ')||'Unknown author')}</small><small class="muted">${esc([c.source,c.isbn].filter(Boolean).join(' · '))}</small></span></button>`).join('');
        document.querySelectorAll('[data-meta]').forEach(el=>el.addEventListener('click',run(async()=>{
          el.disabled=true;
          await useCandidate(results[Number(el.dataset.meta)],candidate=>{closeModal();onPick(candidate);});
        })));
      }catch(e){if($('ml-results'))$('ml-results').innerHTML=`<p class="notice">${esc(e.message)}</p>`;}
    };
    on('ml-search','click',search);
    $('ml-query').addEventListener('keydown',e=>{if(e.key==='Enter')search();});
    if(initial)search();
  });
}
function openLibraryMenu(id){
  const book=state.books.find(x=>x.id===id);
  if(!book)return;
  modal(book.title,`<div class="stack"><button id="lib-open">Open book</button><button id="lib-edit">Edit details…</button><button id="lib-online">Download details…</button><button id="lib-send">Send to Kindle</button></div>`,()=>{
    on('lib-open','click',()=>{closeModal();return openBook(id);});
    on('lib-edit','click',()=>{closeModal();editBookMetadata(id);});
    on('lib-online','click',()=>{closeModal();openMetadataLookup(book,candidate=>editBookMetadata(id,candidate));});
    on('lib-send','click',async()=>{closeModal();await sendBooks([id]);});
  });
}
async function sendBooks(ids){
  if(!ids.length)return toast('Select at least one book to send.');
  if(!kindleDevice)return toast('No Kindle device detected.');
  try{
    const result=await api.kindleExport(ids,kindleDevice);
    document.querySelectorAll('[data-lib-select]').forEach(el=>{if(ids.includes(el.dataset.libSelect))el.checked=false;});
    const parts=[];
    if(result.copied?.length)parts.push(result.copied.length+' sent');
    if(result.skipped?.length)parts.push(result.skipped.length+' skipped');
    if(result.errors?.length)parts.push(result.errors.length+' failed');
    toast(parts.join(', ')||'Export complete.');
    if(result.skipped?.length||result.errors?.length){
      const details=[...(result.skipped||[]).map(s=>s.title+': '+s.reason),...(result.errors||[]).map(e=>e.title+': '+e.reason)];
      if(details.length)console.warn('Export details:',details);
    }
    await kindleScan();
  }catch(e){toast(e.message);}
}
function kindleExportSelected(){
  return sendBooks([...document.querySelectorAll('[data-lib-select]:checked')].map(el=>el.dataset.libSelect));
}
function syncKindleSelectAll(){
  for(const [all,rows] of [['kindle-all-lib','[data-lib-select]'],['kindle-all-device','[data-device-select]']]){
    const box=$(all);
    if(!box)continue;
    const items=[...document.querySelectorAll(rows)];
    box.checked=items.length>0&&items.every(el=>el.checked);
  }
}
function kindlePdfDialog(){
  const pdfs=state.books.filter(b=>b.kind==='PDF');
  const body=(pdfs.length
    ?'<div class="stack">'+pdfs.map(b=>'<button data-send-pdf="'+b.id+'"><strong>'+esc(b.title)+'</strong><small style="display:block;margin-top:3px">'+esc(b.author||'Unknown author')+'</small></button>').join('')+'</div>'
    :'<p class="muted">No PDF books in your library yet.</p>')
    +'<div class="stack" style="margin-top:12px"><button id="kindle-pdf-browse" class="primary">Choose PDF files from your computer…</button></div>';
  modal('Send a PDF to Kindle',body,()=>{
    on('kindle-pdf-browse','click',async()=>{
      closeModal();
      try{
        const res=await api.kindleAddPDF(kindleDevice);
        if(!res)return;
        if(res.state)state=res.state;
        const result=res.result||{};
        if(result.copied?.length)toast(result.copied.length+' PDF(s) added to your library and sent to Kindle.');
        else toast((result.skipped?.[0]||result.errors?.[0])?.reason||'The PDF could not be sent.');
        await kindleScan();
      }catch(e){toast(e.message);}
    });
    document.querySelectorAll('[data-send-pdf]').forEach(el=>el.onclick=run(async()=>{
      el.disabled=true;
      const result=await api.kindleExport([el.dataset.sendPdf],kindleDevice);
      closeModal();
      if(result.copied?.length){toast('PDF sent to Kindle.');await kindleScan();}
      else toast((result.skipped?.[0]||result.errors?.[0])?.reason||'The PDF could not be sent.');
    }));
  });
}
function kindleDeleteSelected(){
  const ids=[...document.querySelectorAll('[data-device-select]:checked')].map(el=>el.dataset.deviceSelect);
  if(!ids.length)return toast('Select at least one book to remove.');
  modal('Remove from Kindle?',`<p>Move ${ids.length} selected file(s) to the Recycle Bin? They will no longer appear on the device.</p><div class="row"><button id="confirm-device-delete" class="danger">Remove ${ids.length} file(s)</button><button id="cancel-device-delete">Cancel</button></div>`,()=>{
    on('cancel-device-delete','click',closeModal);
    on('confirm-device-delete','click',async()=>{
      closeModal();
      try{
        const s=await api.kindleDeleteDeviceBooks(ids);
        if(s){kindleBooks=s.books||[];toast(ids.length+' file(s) removed from Kindle (Recycle Bin).');renderKindle();}
      }catch(e){toast(e.message);}
    });
  });
}
function renderKindle(){
  if(!kindleDevice){
    $('main').innerHTML=`<div class="empty"><h2>Connect your Kindle</h2><p>Plug in your Kindle via USB to browse, import, and export books.</p><div class="row" style="justify-content:center;margin-top:16px"><button id="kindle-refresh" class="primary">Detect Kindle</button></div></div>`;
    on('kindle-refresh','click',async()=>{
      const result=await kindleDetect();
      if(result.connected){kindleDevice=result.device;await kindleScan();}
      else toast('No Kindle device found. Make sure it is connected via USB.');
    });
    return;
  }
  const exportable=state.books.filter(b=>['EPUB','Kindle','PDF'].includes(b.kind));
  const libBody=exportable.length
    ?exportable.map(libBookRow).join('')
    :'<p class="muted" style="padding:20px;text-align:center">No exportable books in library.<br>Import Kindle books or add EPUB files.</p>';
  const deviceBody=kindleBooks.length
    ?kindleBooks.map(kindleBookRow).join('')
    :'<p class="muted" style="padding:20px;text-align:center">No books found on device.</p>';
  const columns='<div class="kindle-two-col">'
    +'<div class="kindle-col"><div class="kindle-col-head"><h3>Clavis Library</h3><span class="muted">'+exportable.length+' book(s)</span></div><div class="kindle-col-tools"><label><input type="checkbox" id="kindle-all-lib">Select all</label></div><div class="kindle-col-body">'+libBody+'</div></div>'
    +'<div class="kindle-col-mid"><button id="kindle-to-device" class="primary" title="Send selected books to Kindle">→</button><button id="kindle-to-library" title="Import selected books to library">←</button></div>'
    +'<div class="kindle-col"><div class="kindle-col-head"><h3>On Kindle</h3><span class="muted">'+kindleBooks.length+' book(s)</span></div><div class="kindle-col-tools"><label><input type="checkbox" id="kindle-all-device">Select all</label><button id="kindle-add-pdf" title="Send a PDF from your library">＋ PDF</button><button id="kindle-delete-selected" class="danger">Delete</button></div><div class="kindle-col-body">'+deviceBody+'</div></div>'
    +'</div>';
  const toolbar='<div class="toolbar"><span class="muted">Kindle at '+esc(kindleDevice)+'</span><div class="row"><button id="kindle-rescan">↻ Rescan</button><button id="kindle-disconnect">Disconnect</button></div></div>';
  const body=kindleScanning?'<div class="loading">Scanning your Kindle…</div>':columns;
  $('main').innerHTML=toolbar+body;
  on('kindle-rescan','click',kindleScan);
  on('kindle-disconnect','click',()=>{kindleDevice=null;kindleBooks=[];renderKindle();});
  on('kindle-to-device','click',kindleExportSelected);
  on('kindle-to-library','click',kindleImportSelected);
  on('kindle-all-lib','change',()=>{const on_=$('kindle-all-lib').checked;document.querySelectorAll('[data-lib-select]').forEach(el=>el.checked=on_);});
  on('kindle-all-device','change',()=>{const on_=$('kindle-all-device').checked;document.querySelectorAll('[data-device-select]').forEach(el=>el.checked=on_);});
  document.querySelectorAll('[data-device-select],[data-lib-select]').forEach(el=>el.addEventListener('change',syncKindleSelectAll));
  on('kindle-add-pdf','click',kindlePdfDialog);
  on('kindle-delete-selected','click',kindleDeleteSelected);
  void loadKindleArtwork();
}

const actions={'undo-seek':undoSeek,'detect-chapters':detectChapters,import:importFiles,folder:importFolder,play:togglePlay,'skip-back':()=>skip(-1),'skip-forward':()=>skip(1),previous:()=>changeChapter(-1),next:()=>changeChapter(1),speed:speedDialog,sleep:sleepDialog,'add-audio-bookmark':addAudioBookmark,'audio-bookmarks':audioBookmarks,'show-player':async()=>{if(reader)await cleanupReader();route='Player';render();},files:()=>api.openFiles(),'new-note':newNote,'add-download':addDownload};
function postRowFor(el){const post=el.closest('.post');return post?feedPosts[Number(post.dataset.post)]:null;}
document.addEventListener('click',run(async e=>{
  const el=e.target.closest('button,[data-feed-open]');if(!el||el.disabled)return;const d=el.dataset;
  if(d.removeFeed){confirmRemoveFeed(d.removeFeed);return;}
  if(d.subscribe){await subscribeSource(d.subscribe,d.subscribeKind||route);return;}
  if(d.playFeed){await playEpisode(d.playFeed,d.playItem);return;}
  if(d.feedOpen){openFeed(d.feedOpen);return;}
  if(d.feedTab){activeFeed=null;feedBrowseTopic='';query='';$('search').value='';feedView[route]=d.feedTab;renderFeeds();$('main').scrollTop=0;return;}
  if(d.browseTopic!==undefined){feedBrowseTopic=d.browseTopic;renderFeeds();return;}
  if(d.slide!==undefined){const post=el.closest('.post');if(post)slidePost(post,Number(d.slide));return;}
  if(d.credits!==undefined){const row=postRowFor(el);if(row)feedCredits(row);return;}
  if(d.listen!==undefined){const row=postRowFor(el);if(row)await listenPost(row);return;}
  if(d.web!==undefined){const row=postRowFor(el);if(row?.item.link)await api.openURL(row.item.link);return;}
  if(d.feedBack!==undefined){activeFeed=null;renderFeeds();$('main').scrollTop=0;return;}
  if(d.refresh){await refreshFeed(d.refresh);return;}
  if(d.refreshKind!==undefined){await refreshCategory(route,{force:true});return;}
  if(d.customFeed!==undefined){feedAddDialog();return;}
  if(d.topics!==undefined){feedTopicsDialog();return;}
  if(d.order!==undefined){await toggleFeedOrder();return;}
  if(d.route)return navigate(d.route);if(d.action)return actions[d.action]?.();if(d.open)return openBook(d.open);if(d.bookMenu)return bookMenu(d.bookMenu);if(d.kindleMenu)return kindleMenu(d.kindleMenu);if(d.libMenu)return openLibraryMenu(d.libMenu);if(d.chapter!==undefined){await startBook(current,true,Number(d.chapter),0);return renderPlayer();}if(d.external)return api.openURL(d.external);if(d.note){await flushNote();activeNote=d.note;renderNotes();return;}if(d.downloadAction){downloadState=await api.downloadAction(d.id,d.downloadAction);if(Array.isArray(downloadState))renderDownloads();return;}
}));
document.addEventListener('keydown',e=>{const row=e.target.closest?.('.source-row[data-feed-open]');if(row&&(e.key==='Enter'||e.key===' ')){e.preventDefault();openFeed(row.dataset.feedOpen);}});
document.addEventListener('pointerdown',e=>{const pages=e.target.closest?.('.post-pages');if(!pages||e.button!==0||e.target.closest('.post-flow'))return;postDrag={pages,x:e.clientX,y:e.clientY,pointer:e.pointerId};});
document.addEventListener('pointerup',e=>{const drag=postDrag;postDrag=null;if(!drag||drag.pointer!==e.pointerId)return;const dx=e.clientX-drag.x,dy=e.clientY-drag.y;if(Math.abs(dx)<48||Math.abs(dx)<Math.abs(dy)*1.2)return;const selection=window.getSelection();if(selection&&!selection.isCollapsed)return;const post=drag.pages.closest('.post');if(post)slidePost(post,dx<0?1:-1);});
document.addEventListener('pointercancel',()=>{postDrag=null;});
document.addEventListener('click',e=>{const a=e.target.closest('.article-content a');if(a){e.preventDefault();run(()=>api.openURL(a.href))();}});
document.addEventListener('error',e=>{if(e.target instanceof HTMLImageElement){e.target.removeAttribute('src');e.target.style.visibility='hidden';}},true);
on('dialog-close','click',closeModal);on('import','click',importFiles);on('files','click',()=>api.openFiles());on('search','input',()=>{query=$('search').value;render();});bindListenPanel();
async function completeAudioChapter(){if(!current||audioLoading||advancing)return;advancing=true;try{finishTranscription();const autoplay=audio.dataset.sleepEnd!=='yes';audio.dataset.sleepEnd='';await persistAudio();if(chapter+1<current.tracks.length)await startBook(current,autoplay,chapter+1,0);else{audio.pause();await updateBook(current,{progress:100,position:0});toast('You’ve reached the end.');}}finally{advancing=false;}}
audio.addEventListener('timeupdate',()=>{if(audioLoading)return;updateTimes();if(!audio.paused&&Number.isFinite(activeTrack()?.end)&&audio.currentTime>=activeTrack().end-.025){run(completeAudioChapter)();return;}if(!saveTimer)saveTimer=setTimeout(run(async()=>{saveTimer=null;await persistAudio();}),5000);});
audio.addEventListener('play',()=>{renderMini();updatePlayButtons();});audio.addEventListener('pause',()=>{if(audioLoading)return;renderMini();updatePlayButtons();run(persistAudio)();});
audio.addEventListener('ended',run(completeAudioChapter));
audio.addEventListener('error',()=>toast('This audio could not be played. Check the file or connection; try MP3, M4A, M4B, WAV, OGG or FLAC.'));
document.addEventListener('keydown',run(async e=>{if($('dialog').open||e.target.closest('input,textarea,select,[contenteditable]'))return;if(listening){if(e.code==='Space'){e.preventDefault();await toggleListenPlay();}return;}if(reader){if(e.key==='ArrowRight'){e.preventDefault();await readerMove(1);}if(e.key==='ArrowLeft'){e.preventDefault();await readerMove(-1);}}else if(e.code==='Space'&&current){e.preventDefault();await togglePlay();}}));
setInterval(()=>{if(current&&!audioLoading&&!audio.paused&&Number.isFinite(activeTrack()?.end)&&audio.currentTime>=activeTrack().end)run(completeAudioChapter)();},100);
window.addEventListener('beforeunload',()=>{run(persistAudio)();run(flushNote)();if(listening)api.listenSave(listening.doc.id,listening.position).catch(()=>{});});
matchMedia('(prefers-color-scheme: dark)').addEventListener('change',applyTheme);
api.onDownloads(jobs=>{downloadState=jobs;if(route==='Downloads'&&!$('dialog').open)renderDownloads();});
async function boot(){state=await api.load();applyFeedPayload(await api.feeds());downloadState=await api.downloads();applyTheme();render();if(FEED_KINDS.includes(route))void refreshCategory(route);const recent=state.books.filter(b=>['Audio','Podcast'].includes(b.kind)&&b.lastActive).sort((a,b)=>b.lastActive-a.lastActive)[0];if(recent)await startBook(recent,false);}
run(boot)();

Object.defineProperty(window,'clavisTransport',{value:Object.freeze({state:()=>({ready:!!current?.tracks?.length&&!audioLoading,playing:!audio.paused,skip:state.settings.skip||30}),command:async action=>{if(!current||audioLoading)return;if(action==='play')await togglePlay();else if(action==='back')await skip(-1);else if(action==='forward')await skip(1);}})});

illustrateEmptyStates(()=>route);

// MARKER_TEST_12345
