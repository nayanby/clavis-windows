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
let ink={},inkTool='navigate',inkColor='#7971ae',inkWidth=3;
let transcriptVisible=false,transcriptData={},transcriptStatus='',equalizer=[0,0,0,0,0],voiceGain=1;
let audioLoading=false,audioGeneration=0,seekDragging=false,lastSeek=null,advancing=false;
const activeTrack=()=>current?.tracks?.[chapter];
const audioDuration=()=>trackDuration(activeTrack(),audio.duration);
const audioPosition=()=>relativePosition(activeTrack(),audio.currentTime,audio.duration);
const refreshingFeeds=new Map();
let articleOpen=false;
function feedStatus(f){return refreshingFeeds.has(f.id)?'Fetching latest entries…':f.refreshError?'Refresh failed · retry to fetch live RSS':f.updated?'Updated '+new Date(f.updated).toLocaleString():'Not fetched yet · open to fetch live RSS';}
function redrawFeeds(){if(['News','Podcasts','Journals'].includes(route)&&!articleOpen)renderFeeds();}
async function fetchLatestFeed(id,notify=false){
  if(refreshingFeeds.has(id))return refreshingFeeds.get(id);
  const work=(async()=>{try{const fresh=await api.feedRefresh(id);feeds=feeds.map(f=>f.id===id?fresh:f);if(notify)toast('Latest entries fetched.');return fresh;}
    catch(e){feeds=feeds.map(f=>f.id===id?{...f,refreshError:e.message}:f);if(notify)toast('Could not refresh this source: '+e.message);}
    finally{refreshingFeeds.delete(id);redrawFeeds();}
  })();refreshingFeeds.set(id,work);redrawFeeds();return work;
}
async function refreshCategory(kind){const ids=feeds.filter(f=>f.kind===kind).map(f=>f.id);let next=0;await Promise.all(Array.from({length:Math.min(3,ids.length)},async()=>{while(next<ids.length)await fetchLatestFeed(ids[next++]);}));}
function openFeed(id){articleOpen=false;activeFeed=id;query='';$('search').value='';renderFeeds();void fetchLatestFeed(id);}
const audio=$('audio');
audio.crossOrigin='anonymous';
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
function cover(b,cls='book-cover'){return `<img class="${cls}" src="${esc(b.cover||art(b.kind))}" alt="" loading="lazy">`;}
function bookRow(b){return `<div class="book-row"><button class="book-open" data-open="${b.id}">${cover(b)}<span class="grow"><strong>${esc(b.title)}</strong><small>${esc(b.kind==='Audio'?`${b.tracks?.length||1} chapters · Chapter ${(b.chapter||0)+1}`:b.kind==='Podcast'?b.author:b.kind+' book')}${b.progress?` · ${Math.round(b.progress)}%`:''}</small><span class="progress"><span style="width:${Math.min(100,b.progress||0)}%"></span></span></span></button><button class="subtle" data-book-menu="${b.id}" aria-label="Options for ${esc(b.title)}">•••</button></div>`;}
function renderNavigation(){document.querySelectorAll('[data-icon]').forEach(el=>el.innerHTML=clavisIcons[el.dataset.icon]||'');
  $('navigation').innerHTML=`<button data-route="Home" class="${route==='Home'?'active':''}"><span class="nav-icon">${clavisIcons.Home}</span>Home</button><p class="nav-label">YOUR LIBRARY</p>`+categories.map(([kind,title,,,symbol])=>`<button data-route="${kind}" class="${route===kind?'active':''}"><span class="nav-icon">${clavisIcons[kind]}</span>${title}</button>`).join('');
  document.querySelectorAll('.sidebar-bottom [data-route]').forEach(b=>b.classList.toggle('active',b.dataset.route===route));
}
async function cleanupReader(){readerGeneration++;if(reader){reader.epub?.destroy();reader.pdf?.destroy();reader.observer?.disconnect();reader=null;}document.body.classList.remove('reading');}
async function navigate(next){await persistAudio();await flushNote();if(reader)await cleanupReader();route=next;activeFeed=null;articleOpen=false;query='';$('search').value='';$('search').placeholder=['News','Podcasts','Journals'].includes(route)?'Search sources and stories':'Search your library';render();$('main').scrollTop=0;window.scrollTo(0,0);if(['News','Podcasts','Journals'].includes(next))void refreshCategory(next);}
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
function equalizerDialog(){modal('Audio settings',`<p class="muted">Shape narration with a five-band equalizer and voice gain.</p>${[100,350,1000,3500,10000].map((hz,i)=>`<label for="eq-${i}">${hz>=1000?hz/1000+' kHz':hz+' Hz'}</label><input id="eq-${i}" type="range" min="-12" max="12" step="1" value="${equalizer[i]}">`).join('')}<label for="voice-gain">Voice gain</label><input id="voice-gain" type="range" min=".5" max="2" step=".1" value="${voiceGain}"><div class="row"><button id="apply-eq" class="primary">Apply</button><button id="reset-eq">Reset</button></div>`,()=>{on('apply-eq','click',async()=>{equalizer=equalizer.map((_,i)=>Number($('eq-'+i).value));voiceGain=Number($('voice-gain').value);await effects(audio,equalizer,voiceGain);closeModal();});on('reset-eq','click',async()=>{equalizer=[0,0,0,0,0];voiceGain=1;await effects(audio,equalizer,voiceGain);closeModal();});});}
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
function sourceArt(f){return f.image?`<img class="source-art" src="${esc(f.image)}" alt="" loading="lazy">`:`<span class="source-art source-placeholder">${illustration('feeds')}<span class="source-initials">${esc(f.title.split(/\s+/).slice(0,3).map(w=>w[0]).join(''))}</span></span>`;}
function renderFeeds(){if(activeFeed){const f=feeds.find(f=>f.id===activeFeed);if(!f){activeFeed=null;return renderFeeds();}const entries=f.entries.filter(e=>(e.title+' '+plain(e.content)).toLowerCase().includes(query.toLowerCase()));$('main').innerHTML=`<div class="toolbar"><button data-action="sources-back">‹ All sources</button><div class="row"><span class="muted">${esc(feedStatus(f))}</span><button data-refresh="${f.id}" ${refreshingFeeds.has(f.id)?'disabled':''}>↻ Refresh</button><button data-remove-feed="${f.id}">Unsubscribe</button></div></div><div class="row" style="margin-bottom:25px">${sourceArt(f)}<div><h2 style="margin:0 0 7px">${esc(f.title)}</h2><span class="muted">${f.entries.length} stories${f.kind==='Podcasts'?' and episodes':''}</span>${f.refreshError?`<p class="notice">Could not fetch the RSS feed: ${esc(f.refreshError)}. Use Refresh to fetch this RSS source again.</p>`:''}</div></div>${entries.map(e=>`<div class="entry">${e.image?sourceArt({image:e.image,title:e.title}):''}<div class="entry-copy"><small>${esc(date(e.date))}${e.duration?' · '+esc(e.duration):''}</small><h3>${esc(e.title)}</h3><p>${esc(short(plain(e.content),200))}</p><div class="row">${e.audio?`<button class="primary" data-episode="${e.id}">▶ Listen</button>`:''}<button data-article="${e.id}">Read ${e.audio?'show notes':'article'} →</button>${e.enclosure?.url&&e.enclosure?.type?.includes('pdf')?`<button data-external="${esc(e.enclosure.url)}">Open PDF ↗</button>`:''}</div></div></div>`).join('')||'<div class="empty"><h3>No matching stories</h3></div>'}`;return;}
  const matching=feeds.filter(f=>f.kind===route&&(f.title.toLowerCase().includes(query.toLowerCase())||f.entries.some(e=>e.title.toLowerCase().includes(query.toLowerCase()))));$('main').innerHTML=`<div class="toolbar"><span class="muted">${matching.length} subscriptions · RSS & Atom</span><div class="row"><button data-action="feed-add">＋ RSS address</button><button class="primary" data-action="browse-sources">Browse sources</button></div></div><p class="notice">Latest entries are fetched automatically when you open this section or a source. Only live RSS content is shown for the current session.</p><div class="source-grid">${matching.map(f=>`<button class="source-card" data-feed="${f.id}">${sourceArt(f)}<span><h3>${esc(f.title)}</h3><small>${f.entries.length} ${f.kind==='Podcasts'?'episodes':'stories'}<br>${esc(feedStatus(f))}</small></span></button>`).join('')}</div>${matching.length?'':'<div class="empty"><h2>Your reading list, your interests.</h2><p>Add an RSS address or browse the source directory.</p><button data-action="browse-sources">Browse sources</button></div>'}`;
}
function feedAdd(){modal('Subscribe with RSS',`<p class="muted">Add a public RSS or Atom feed to ${route==='Journals'?'Articles':route}.</p><label for="feed-url">Feed address</label><input id="feed-url" type="url" placeholder="https://example.com/feed.xml"><div class="row"><button id="subscribe" class="primary">Subscribe</button><span id="feed-status" class="muted"></span></div>`,()=>on('subscribe','click',async()=>{$('subscribe').disabled=true;$('feed-status').textContent='Fetching feed…';try{feeds=await api.feedAdd(route,$('feed-url').value.trim());closeModal();renderFeeds();toast('Source added.');}finally{if($('subscribe'))$('subscribe').disabled=false;}}));}
function browseSources(){const list=directory.filter(f=>f.kind===route);modal('Browse sources',`<input id="directory-search" type="search" placeholder="Find a source"><div id="directory-list" class="directory"></div><div class="row"><button id="custom-feed">＋ Add another RSS address</button></div>`,()=>{const draw=()=>{$('directory-list').innerHTML=list.filter(f=>f.title.toLowerCase().includes($('directory-search').value.toLowerCase())).map(f=>`<button data-subscribe="${esc(f.url)}"><strong>${esc(f.title)}</strong><small>${feeds.some(s=>s.url===f.url&&s.kind===route)?'Subscribed · open to read':'＋ Subscribe'}</small></button>`).join('');$('directory-list').querySelectorAll('[data-subscribe]').forEach(b=>b.onclick=run(async()=>{const existing=feeds.find(f=>f.url===b.dataset.subscribe&&f.kind===route);if(existing){closeModal();openFeed(existing.id);return;}b.disabled=true;b.textContent='Fetching feed…';try{feeds=await api.feedAdd(route,b.dataset.subscribe);draw();toast('Subscribed.');}finally{b.disabled=false;}}));};draw();on('directory-search','input',draw);on('custom-feed','click',feedAdd);});}
async function refreshFeed(id){return fetchLatestFeed(id,true);}
async function playEpisode(id){const b=await api.playEpisode(activeFeed,id);const i=state.books.findIndex(x=>x.id===b.id);if(i<0)state.books.push(b);else state.books[i]=b;await startBook(b,true);route='Player';render();}
async function readArticle(id){
  const f=feeds.find(f=>f.id===activeFeed),e=f?.entries.find(x=>x.id===id);if(!e)return;
  articleOpen=true;const back=activeFeed;let live=true;
  const show=(title,content,status='',publisherAction=false)=>{
    $('main').innerHTML=`<div class="toolbar"><button id="article-back">‹ Back to ${esc(f.title)}</button><button id="article-website" ${e.link?'':'disabled'}>Website ↗</button></div><article class="article"><small>${esc(f.title)} · ${esc(date(e.date))}</small><h1>${esc(title)}</h1>${status?`<p class="notice">${esc(status)}</p>`:''}<div class="article-content">${safeHTML(content||'')}</div>${publisherAction&&e.link?'<p><button id="article-publisher" class="primary">Open publisher website ↗</button></p>':''}</article>`;
    on('article-back','click',()=>{live=false;articleOpen=false;activeFeed=back;renderFeeds();});
    on('article-website','click',()=>api.openURL(e.link));
    if(publisherAction&&e.link)on('article-publisher','click',()=>api.openURL(e.link));
  };
  const visible=()=>live&&activeFeed===back&&['News','Journals','Podcasts'].includes(route);
  show(e.title,e.content,'Fetching article from publisher…');
  if(!e.link)return show(e.title,e.content,'This RSS entry does not include an article link.');
  try{
    const article=await api.article(e.link);if(!visible())return;
    if(article.availability==='publisher-blocked')show(e.title,e.content,`RSS preview only. The publisher refused automated access to the article (HTTP ${article.status}). Open the publisher website to read it; access may require signing in or a subscription.`,true);
    else show(article.title||e.title,article.content);
  }catch(error){if(visible())show(e.title,e.content,'RSS preview only. The article could not be loaded from the publisher. '+error.message,true);}
}
function renderSettings(){$('main').innerHTML=`<div class="settings"><div class="surface-heading">${illustration('settings','surface-art')}<div><h2>Make yourself at home.</h2><p class="muted">Reading and playback preferences are saved on this computer.</p></div></div><div class="setting"><div><h3>Appearance</h3><p>A quiet space, day or night.</p></div><select id="theme"><option value="system">Follow Windows</option><option value="light">Light</option><option value="dark">Dark</option></select></div><div class="setting"><div><h3>Skip interval</h3><p>Rewind and forward buttons.</p></div><select id="skip-setting">${[5,10,15,30,60,120].map(n=>`<option value="${n}">${n} seconds</option>`).join('')}</select></div><div class="setting"><div><h3>EPUB font size</h3><p>Applied to your reflowable books.</p></div><input id="font-setting" type="number" min="10" max="40" value="${state.settings.fontSize||19}" aria-label="EPUB font size"></div><div class="setting"><div><h3>Downloads</h3><p>Imports and downloads share Data / Books in named folders.</p></div><button data-action="files">Open folder ↗</button></div><div class="setting"><div><h3>Clavis for Windows</h3><p>Python desktop edition 0.2.5 · Based on your Clavis Android project.</p></div></div><p class="notice" style="margin-top:25px">This first desktop build includes local books, playback, PDF ink, EPUB highlights, feeds, typed journals and magnet transfers. Offline English live text and audio equalizer are included. Journals also support handwriting. Embedded chapters and reviewed offline spoken-heading scans are supported.</p></div>`;$('theme').value=state.settings.theme||'system';$('skip-setting').value=state.settings.skip||30;on('theme','change',()=>settings({theme:$('theme').value}));on('skip-setting','change',()=>settings({skip:Number($('skip-setting').value)}));on('font-setting','change',()=>settings({fontSize:Number($('font-setting').value)}));}
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
  $('main').innerHTML=`<div class="reader-shell"><div class="reader-toolbar"><button id="reader-back">‹ Library</button><div class="reader-tools"><input id="reader-find" class="reader-find" type="search" placeholder="Search book" aria-label="Search book"><button id="reader-search">Find</button><button id="reader-bookmark" aria-label="Bookmark current page">⚑ Bookmark</button><button id="reader-marks">Bookmarks</button>${b.kind==='EPUB'?'<button id="reader-type">Aa</button><button id="reader-highlight">Highlight selection</button>':'<button id="ink-toggle">✎ Pen</button><select id="ink-kind" aria-label="Drawing tool"><option value="pen">Pen</option><option value="highlight">Highlighter</option><option value="underline">Underliner</option></select><input id="ink-color" class="ink-color" type="color" value="#7971ae" aria-label="Ink color"><button id="ink-undo">Undo</button><button id="pdf-zoom-out" aria-label="Zoom out">−</button><button id="pdf-zoom-in" aria-label="Zoom in">＋</button>'}</div></div><div class="reader-stage" id="reader-stage"><div class="loading">Opening ${b.kind}…</div></div><div class="reader-footer"><button id="reader-outline">☷ Outline</button><div class="row"><button id="reader-previous">‹ Previous</button><span id="reader-position" class="muted"></span><button id="reader-next">Next ›</button><button id="reader-jump">Go to…</button></div><span class="muted" id="reader-percent"></span></div></div>`;
  reader={book:b,page:Math.floor(b.page)||1,selected:null,generation};
  on('reader-back','click',()=>navigate(b.kind));on('reader-bookmark','click',readerBookmark);on('reader-marks','click',readerBookmarks);on('reader-outline','click',readerOutline);on('reader-search','click',readerSearch);on('reader-find','keydown',e=>{if(e.key==='Enter')return readerSearch();});on('reader-jump','click',readerJump);on('reader-previous','click',()=>readerMove(-1));on('reader-next','click',()=>readerMove(1));
  try{
    const response=await fetch(b.url);if(!response.ok)throw Error('The source file could not be opened.');const bytes=new Uint8Array(await response.arrayBuffer());if(generation!==readerGeneration)return;
    if(b.kind==='PDF')await openPDF(bytes,generation);else await openEPUB(bytes,generation);
  }catch(e){if(generation===readerGeneration){$('reader-stage').innerHTML=`<div class="empty"><h2>This book could not be opened.</h2><p>${esc(e.message)}</p><p>Check that the file is still in its original location and available offline.</p></div>`;toast(e.message);}}
}
async function openEPUB(bytes,generation){
  $('reader-stage').innerHTML='<div id="epub-host" class="epub-host"></div>';
  const book=ePub(bytes.buffer);reader.epub=book;
  const rendition=book.renderTo('epub-host',{width:'100%',height:'100%',spread:'none',flow:'paginated',allowScriptedContent:false});reader.rendition=rendition;
  rendition.themes.default({'body':{'color':document.body.classList.contains('dark')?'#dddff3':'#292664','background':document.body.classList.contains('dark')?'#252632':'#ffffff','font-family':'Georgia, serif','font-size':`${state.settings.fontSize||19}px`,'line-height':`${state.settings.lineHeight||1.7}`,'padding':`${state.settings.margin??32}px !important`},'p':{'line-height':`${state.settings.lineHeight||1.7} !important`}});
  rendition.on('relocated',location=>{if(generation!==readerGeneration)return;reader.location=location;const percent=book.locations.length()?book.locations.percentageFromCfi(location.start.cfi)*100:Math.min(99,location.start.index/Math.max(1,book.spine.length)*100);$('reader-position').textContent=`Section ${location.start.index+1} of ${book.spine.length}`;$('reader-percent').textContent=Math.round(percent)+'%';clearTimeout(reader.saveTimer);reader.saveTimer=setTimeout(run(()=>updateBook(reader.book,{cfi:location.start.cfi,progress:percent})),400);});
  rendition.on('selected',(cfiRange,contents)=>{if(generation!==readerGeneration)return;reader.selected=cfiRange;reader.selectionText=contents.window.getSelection()?.toString()||'';toast('Text selected. Choose Highlight selection to save it.');});
  rendition.hooks.content.register(contents=>{contents.document.addEventListener('keydown',e=>{if(e.key==='ArrowRight')run(()=>rendition.next())();if(e.key==='ArrowLeft')run(()=>rendition.prev())();});contents.document.addEventListener('click',e=>{const a=e.target.closest('a');if(a&&/^https?:/.test(a.href)){e.preventDefault();run(()=>api.openURL(a.href))();}});});
  await rendition.display(reader.book.cfi||undefined);if(generation!==readerGeneration)return;
  reader.outline=(await book.loaded.navigation).toc;
  for(const cfi of reader.book.highlights||[])try{rendition.annotations.highlight(cfi,{},null,'saved-highlight',{'fill':'#e7c36b','fill-opacity':'.4'});}catch{}
  on('reader-type','click',typeDialog);on('reader-highlight','click',async()=>{if(!reader.selected)return toast('Select some book text first.');const cfi=reader.selected;rendition.annotations.highlight(cfi,{},null,'saved-highlight',{'fill':'#e7c36b','fill-opacity':'.4'});await updateBook(reader.book,{highlights:[...(reader.book.highlights||[]),cfi]});reader.selected=null;toast('Highlight saved.');});
  book.locations.generate(1800).then(()=>{if(generation===readerGeneration&&reader.location)$('reader-percent').textContent=Math.round(book.locations.percentageFromCfi(reader.location.start.cfi)*100)+'%';}).catch(()=>{});
}
function typeDialog(){modal('Reading appearance',`<label for="reader-font">Font size <span id="reader-font-value">${state.settings.fontSize||19}</span> px</label><input id="reader-font" type="range" min="10" max="40" step="1" value="${state.settings.fontSize||19}"><label for="reader-leading">Line spacing</label><input id="reader-leading" type="range" min="1" max="2.5" step=".1" value="${state.settings.lineHeight||1.7}"><label for="reader-margin">Margins</label><input id="reader-margin" type="range" min="0" max="100" step="4" value="${state.settings.margin??32}"><div class="row"><button id="apply-type" class="primary">Apply</button></div>`,()=>{on('reader-font','input',()=>{$('reader-font-value').textContent=$('reader-font').value;});on('apply-type','click',async()=>{const cfi=reader.location?.start.cfi;await settings({fontSize:Number($('reader-font').value),lineHeight:Number($('reader-leading').value),margin:Number($('reader-margin').value)});const b=reader.book;if(cfi)b.cfi=cfi;closeModal();await openReader(b);});});}
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
function pdfGo(n){if(!reader?.pdf)return;reader.page=Math.max(1,Math.min(reader.pdf.numPages,Math.floor(n)));document.querySelector(`.pdf-page[data-page="${reader.page}"]`)?.scrollIntoView({block:'start'});pdfPosition();run(()=>updateBook(reader.book,{page:reader.page,progress:reader.page/reader.pdf.numPages*100}))();}
async function zoomPDF(factor){if(!reader?.pdf)return;reader.scale=Math.min(4,Math.max(.3,reader.scale*factor));reader.rendered.clear();const n=reader.page;for(const el of document.querySelectorAll('.pdf-page')){el.style.width=reader.baseViewport.width*reader.scale+'px';el.style.height=reader.baseViewport.height*reader.scale+'px';}pdfGo(n);await renderPDFPage(n,readerGeneration);for(const el of document.querySelectorAll('.pdf-page')){const rect=el.getBoundingClientRect();if(rect.bottom>0&&rect.top<innerHeight+500)await renderPDFPage(Number(el.dataset.page),readerGeneration);}}
async function readerMove(delta){if(reader?.pdf)pdfGo(reader.page+delta);else if(reader?.rendition)await (delta>0?reader.rendition.next():reader.rendition.prev());}
async function readerBookmark(){if(!reader)return;const r=reader,mark={name:r.pdf?`Page ${r.page}`:`Section ${(r.location?.start.index||0)+1}`,page:r.page,cfi:r.location?.start.cfi||''};await updateBook(r.book,{bookmarks:[...(r.book.bookmarks||[]),mark]});toast('Reading bookmark saved.');}
function readerBookmarks(){if(!reader)return;modal('Reading bookmarks',`<div class="stack">${(reader.book.bookmarks||[]).map((b,i)=>`<div class="row"><button class="grow" data-reading-mark="${i}">${esc(b.name)}</button><button data-reading-remove="${i}" aria-label="Delete bookmark">✕</button></div>`).join('')||'<p class="muted">Bookmark a page to return to it.</p>'}</div>`,()=>{document.querySelectorAll('[data-reading-mark]').forEach(el=>el.onclick=run(async()=>{const b=reader.book.bookmarks[Number(el.dataset.readingMark)];closeModal();if(reader.pdf)pdfGo(b.page);else await reader.rendition.display(b.cfi);}));document.querySelectorAll('[data-reading-remove]').forEach(el=>el.onclick=run(async()=>{await updateBook(reader.book,{bookmarks:reader.book.bookmarks.filter((_,i)=>i!==Number(el.dataset.readingRemove))});readerBookmarks();}));});}
function readerOutline(){if(!reader)return;const flat=[];function flatten(list,depth=0){for(const item of list){flat.push({...item,depth});flatten(item.items||item.subitems||[],depth+1);}}flatten(reader.outline||[]);modal('Outline',`<div class="outline">${flat.map((t,i)=>`<button data-outline="${i}" style="padding-left:${15+t.depth*16}px">${esc(t.label||t.title||'Section')}</button>`).join('')||'<p class="muted">This book has no table of contents.</p>'}</div>`,()=>{document.querySelectorAll('[data-outline]').forEach(el=>el.onclick=run(async()=>{const item=flat[Number(el.dataset.outline)];closeModal();if(reader.pdf){const dest=typeof item.dest==='string'?await reader.pdf.getDestination(item.dest):item.dest;if(dest){const n=typeof dest[0]==='number'?dest[0]+1:await reader.pdf.getPageIndex(dest[0])+1;pdfGo(n);}}else await reader.rendition.display(item.href);}));});}
function readerJump(){if(!reader)return;const pdf=!!reader.pdf;modal(pdf?'Go to page':'Go to reading position',`<label for="jump-position">${pdf?'Page number':'Percentage (0–100)'}</label><input id="jump-position" type="number" min="${pdf?1:0}" max="${pdf?reader.pdf.numPages:100}" value="${pdf?reader.page:Math.round(reader.book.progress||0)}"><div class="row"><button id="jump-confirm" class="primary">Go</button></div>`,()=>on('jump-confirm','click',async()=>{const n=Number($('jump-position').value);closeModal();if(pdf)pdfGo(n);else if(reader.epub.locations.length())await reader.rendition.display(reader.epub.locations.cfiFromPercentage(Math.max(0,Math.min(1,n/100))));else toast('Book positions are still being indexed. Try again shortly.');}));}
async function readerSearch(){if(!reader)return;const term=$('reader-find').value.trim();if(!term)return;const r=reader,generation=readerGeneration;modal('Search book','<p class="muted" id="search-progress">Searching…</p><div id="book-search-results" class="stack"></div>');const results=[];
  if(r.pdf){for(let n=1;n<=r.pdf.numPages;n++){if(generation!==readerGeneration||!$('dialog').open)return;const p=await r.pdf.getPage(n),text=(await p.getTextContent()).items.map(x=>x.str).join(' '),at=text.toLowerCase().indexOf(term.toLowerCase());if(at>=0)results.push({label:`Page ${n} · ${text.slice(Math.max(0,at-50),at+100)}`,page:n});if(results.length>=100)break;if(n%20===0)$('search-progress').textContent=`Searching page ${n} of ${r.pdf.numPages}…`;}}
  else{for(const section of r.epub.spine.spineItems){if(generation!==readerGeneration||!$('dialog').open)return;await section.load(r.epub.load.bind(r.epub));for(const found of section.find(term))results.push({label:found.excerpt,cfi:found.cfi});section.unload();if(results.length>=100)break;}}
  if(generation!==readerGeneration||!$('dialog').open||!$('book-search-results'))return;$('search-progress').textContent=`${results.length}${results.length>=100?'+':''} matches`;$('book-search-results').innerHTML=results.slice(0,100).map((r,i)=>`<button data-search-result="${i}">${esc(r.label)}</button>`).join('');document.querySelectorAll('[data-search-result]').forEach(el=>el.onclick=run(async()=>{const found=results[Number(el.dataset.searchResult)];closeModal();if(r.pdf)pdfGo(found.page);else await r.rendition.display(found.cfi);}));
}
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
function loadKindleCover(path,imgEl){
  api.kindleCover(path).then(dataUri=>{
    if(dataUri&&imgEl)imgEl.src=dataUri;
  }).catch(()=>{});
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
  modal(b.title,`<div class="stack"><button id="device-import">Import to library</button><button id="device-remove" class="danger">Remove from Kindle…</button></div>`,()=>{
    on('device-import','click',()=>{closeModal();importDeviceBooks([id]);});
    on('device-remove','click',async()=>{
      closeModal();
      try{
        const s=await api.kindleDeleteDeviceBook(id);
        if(s){kindleBooks=s.books||[];toast('Removed from Kindle (Recycle Bin).');renderKindle();}
      }catch(e){toast(e.message);}
    });
  });
}
function libraryMetadataDialog(id){
  const b=state.books.find(x=>x.id===id);
  if(!b)return;
  modal('Edit book details',`<label for="lm-title">Title</label><input id="lm-title" value="${esc(b.title)}"><label for="lm-author">Author</label><input id="lm-author" value="${esc(b.author||'')}">${b.kind==='Kindle'?`<label for="lm-series">Series</label><input id="lm-series" value="${esc(b.series||'')}"><label for="lm-series-index">Series number</label><input id="lm-series-index" type="number" min="0" step="0.1" value="${b.seriesIndex||''}">`:''}<div class="row" style="margin-top:16px"><div><small class="muted">Cover image</small><br><img id="lm-cover-preview" src="${esc(b.cover||art(b.kind))}" style="width:60px;height:72px;object-fit:contain;border-radius:6px;border:1px solid var(--line);margin-top:6px"></div></div><div class="row"><button id="lm-change-cover">Change cover…</button></div><div class="row"><button id="lm-save" class="primary">Save</button><button id="lm-cancel">Cancel</button></div>`,()=>{
    let coverDataUri=null;
    on('lm-change-cover','click',async()=>{
      const input=document.createElement('input');
      input.type='file';input.accept='image/jpeg,image/png,image/webp';
      input.onchange=()=>{
        const file=input.files[0];if(!file)return;
        const reader=new FileReader();
        reader.onload=()=>{coverDataUri=reader.result;$('lm-cover-preview').src=reader.result;};
        reader.readAsDataURL(file);
      };
      input.click();
    });
    on('lm-cancel','click',closeModal);
    on('lm-save','click',async()=>{
      const patch={title:$('lm-title').value,author:$('lm-author').value};
      if(b.kind==='Kindle'){
        patch.series=$('lm-series')?.value||'';
        const idx=$('lm-series-index')?.value;
        if(idx!=='')patch.seriesIndex=Number(idx);
      }
      if(coverDataUri)patch.cover=coverDataUri;
      try{
        const updated=await api.updateBookMetadata(b.id,patch);
        const i=state.books.findIndex(x=>x.id===b.id);
        if(i>=0)state.books[i]=updated;
        if(current?.id===b.id)Object.assign(current,updated);
        closeModal();render();toast('Book details updated.');
      }catch(e){toast(e.message);}
    });
  });
}
function kindleBookRow(b){
  return `<div class="book-row"><img class="book-cover" data-device-cover="${esc(b.path)}" src="${art('EPUB')}" alt="" style="width:55px;height:66px;object-fit:contain;border-radius:7px;background:var(--soft);padding:5px"><span class="grow"><strong>${esc(b.title)}</strong><small>${esc(b.author||'Unknown author')}${b.format?' · '+esc(b.format):''}${b.drm?' · DRM':''}</small></span><label class="row" style="gap:6px"><input type="checkbox" data-device-select="${b.id}" style="width:auto">Select</label><button class="subtle" data-kindle-menu="${b.id}" aria-label="Options for ${esc(b.title)}">•••</button></div>`;
}
function libBookRow(b){
  const fmt=b.kind==='Kindle'?(b.kindleFormat||'MOBI').toUpperCase():b.kind==='PDF'?'PDF':'EPUB';
  const needsConvert=b.kind==='EPUB'?' · → AZW3':'';
  return `<div class="book-row"><img class="book-cover" src="${esc(b.cover||art(b.kind))}" alt="" style="width:55px;height:66px;object-fit:contain;border-radius:7px;background:var(--soft);padding:5px"><span class="grow"><strong>${esc(b.title)}</strong><small>${esc(b.author||'Unknown author')}${fmt?' · '+esc(fmt):''}${needsConvert}</small></span><label class="row" style="gap:6px"><input type="checkbox" data-lib-select="${b.id}" style="width:auto">Select</label></div>`;
}
async function kindleExportSelected(){
  const ids=[...document.querySelectorAll('[data-lib-select]:checked')].map(el=>el.dataset.libSelect);
  if(!ids.length)return toast('Select at least one book to send.');
  if(!kindleDevice)return toast('No Kindle device detected.');
  try{
    const result=await api.kindleExport(ids,kindleDevice);
    document.querySelectorAll('[data-lib-select]').forEach(el=>el.checked=false);
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
  const body=pdfs.length
    ?'<div class="stack">'+pdfs.map(b=>'<button data-send-pdf="'+b.id+'"><strong>'+esc(b.title)+'</strong><small>'+esc(b.author||'Unknown author')+'</small></button>').join('')+'</div>'
    :'<p class="muted">No PDF books in your library yet.</p>';
  modal('Send a PDF to Kindle',body,()=>{
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
  document.querySelectorAll('[data-device-cover]').forEach(img=>loadKindleCover(img.dataset.deviceCover,img));
}

const actions={'undo-seek':undoSeek,'detect-chapters':detectChapters,import:importFiles,folder:importFolder,play:togglePlay,'skip-back':()=>skip(-1),'skip-forward':()=>skip(1),previous:()=>changeChapter(-1),next:()=>changeChapter(1),speed:speedDialog,sleep:sleepDialog,'add-audio-bookmark':addAudioBookmark,'audio-bookmarks':audioBookmarks,'show-player':async()=>{if(reader)await cleanupReader();route='Player';render();},'sources-back':()=>{articleOpen=false;activeFeed=null;renderFeeds();},'feed-add':feedAdd,'browse-sources':browseSources,files:()=>api.openFiles(),'new-note':newNote,'add-download':addDownload};
document.addEventListener('click',run(async e=>{const el=e.target.closest('button');if(!el||el.disabled)return;const d=el.dataset;if(d.route)return navigate(d.route);if(d.action)return actions[d.action]?.();if(d.open)return openBook(d.open);if(d.bookMenu)return bookMenu(d.bookMenu);if(d.kindleMenu)return kindleMenu(d.kindleMenu);if(d.chapter!==undefined){await startBook(current,true,Number(d.chapter),0);return renderPlayer();}if(d.feed)return openFeed(d.feed);if(d.refresh)return refreshFeed(d.refresh);if(d.removeFeed){modal('Unsubscribe?',`<p>Remove this source and its saved feed entries?</p><div class="row"><button id="confirm-unsubscribe">Unsubscribe</button><button id="keep-subscription">Keep source</button></div>`,()=>{on('keep-subscription','click',closeModal);on('confirm-unsubscribe','click',async()=>{feeds=await api.feedRemove(d.removeFeed);activeFeed=null;closeModal();renderFeeds();});});return;}if(d.episode)return playEpisode(d.episode);if(d.article)return readArticle(d.article);if(d.external)return api.openURL(d.external);if(d.note){await flushNote();activeNote=d.note;renderNotes();return;}if(d.downloadAction){downloadState=await api.downloadAction(d.id,d.downloadAction);if(Array.isArray(downloadState))renderDownloads();return;}}));
document.addEventListener('click',e=>{const a=e.target.closest('.article-content a');if(a){e.preventDefault();run(()=>api.openURL(a.href))();}});
document.addEventListener('error',e=>{if(e.target instanceof HTMLImageElement){e.target.removeAttribute('src');e.target.style.visibility='hidden';}},true);
on('dialog-close','click',closeModal);on('import','click',importFiles);on('files','click',()=>api.openFiles());on('search','input',()=>{query=$('search').value;render();});
async function completeAudioChapter(){if(!current||audioLoading||advancing)return;advancing=true;try{finishTranscription();const autoplay=audio.dataset.sleepEnd!=='yes';audio.dataset.sleepEnd='';await persistAudio();if(chapter+1<current.tracks.length)await startBook(current,autoplay,chapter+1,0);else{audio.pause();await updateBook(current,{progress:100,position:0});toast('You’ve reached the end.');}}finally{advancing=false;}}
audio.addEventListener('timeupdate',()=>{if(audioLoading)return;updateTimes();if(!audio.paused&&Number.isFinite(activeTrack()?.end)&&audio.currentTime>=activeTrack().end-.025){run(completeAudioChapter)();return;}if(!saveTimer)saveTimer=setTimeout(run(async()=>{saveTimer=null;await persistAudio();}),5000);});
audio.addEventListener('play',()=>{renderMini();updatePlayButtons();});audio.addEventListener('pause',()=>{if(audioLoading)return;renderMini();updatePlayButtons();run(persistAudio)();});
audio.addEventListener('ended',run(completeAudioChapter));
audio.addEventListener('error',()=>toast('This audio could not be played. Check the file or connection; try MP3, M4A, M4B, WAV, OGG or FLAC.'));
document.addEventListener('keydown',run(async e=>{if($('dialog').open||e.target.closest('input,textarea,select,[contenteditable]'))return;if(reader){if(e.key==='ArrowRight'){e.preventDefault();await readerMove(1);}if(e.key==='ArrowLeft'){e.preventDefault();await readerMove(-1);}}else if(e.code==='Space'&&current){e.preventDefault();await togglePlay();}}));
setInterval(()=>{if(current&&!audioLoading&&!audio.paused&&Number.isFinite(activeTrack()?.end)&&audio.currentTime>=activeTrack().end)run(completeAudioChapter)();},100);
window.addEventListener('beforeunload',()=>{run(persistAudio)();run(flushNote)();});
matchMedia('(prefers-color-scheme: dark)').addEventListener('change',applyTheme);
api.onDownloads(jobs=>{downloadState=jobs;if(route==='Downloads'&&!$('dialog').open)renderDownloads();});
async function boot(){state=await api.load();const f=await api.feeds();feeds=f.feeds;directory=f.directory;downloadState=await api.downloads();applyTheme();render();void (async()=>{for(const kind of ['News','Podcasts','Journals'])await refreshCategory(kind);})();const recent=state.books.filter(b=>['Audio','Podcast'].includes(b.kind)&&b.lastActive).sort((a,b)=>b.lastActive-a.lastActive)[0];if(recent)await startBook(recent,false);}
run(boot)();

Object.defineProperty(window,'clavisTransport',{value:Object.freeze({state:()=>({ready:!!current?.tracks?.length&&!audioLoading,playing:!audio.paused,skip:state.settings.skip||30}),command:async action=>{if(!current||audioLoading)return;if(action==='play')await togglePlay();else if(action==='back')await skip(-1);else if(action==='forward')await skip(1);}})});

illustrateEmptyStates(()=>route);

// MARKER_TEST_12345
