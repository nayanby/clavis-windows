"""HTML and Word Pearls beside Qbank, with subject browsing and explicit Word export."""
from pathlib import Path
import re
import os
import time
import zipfile
from functools import lru_cache
from . import study_packs

NOTE_SUFFIXES={'.docx','.html','.htm'}


def resolve(root: Path, relative: str) -> Path | None:
    root=root.resolve()
    if not relative or '\\' in relative or any(p.startswith(('.', '~$')) for p in relative.split('/')):
        return None
    try:
        target=(root/relative).resolve()
    except (ValueError,OSError):
        return None
    if not target.is_relative_to(root) or target.suffix.lower() not in NOTE_SUFFIXES or not target.is_file():
        return None
    return target


def catalog(data_root: Path) -> dict:
    root=(data_root/'Pearls').resolve()
    if not root.is_dir():return {'subjects':[]}
    orders={}
    for bank in study_packs.read_quizzes(data_root/'study-data'):
        if bank.get('navigationGroup')!='general':continue
        for label in (bank.get('document'),bank.get('headingText')):
            key=(bank.get('folder'),re.sub(r'\W','',str(label)).lower())
            orders[key]=bank.get('chapterOrder') or 9999
    subjects=[]
    for folder in sorted(root.iterdir(),key=lambda p:p.name.casefold()):
        if not folder.is_dir() or folder.name.startswith(('.','_')):continue
        topics={}
        for path in sorted(folder.rglob('*')):
            if path.suffix.lower() not in NOTE_SUFFIXES or path.stem.lower()=='index' or path.stem.endswith('layout-check'):continue
            relative=path.relative_to(root).as_posix()
            if resolve(root,relative) is None:continue
            label=re.sub(r'^\d+[. _-]+','',path.stem)
            order=study_packs._quiz_number(path.stem) or orders.get((folder.name,re.sub(r'\W','',label).lower()),9999)
            key=path.relative_to(folder).with_suffix('').as_posix().casefold()
            format='word' if path.suffix.lower()=='.docx' else 'html'
            if key not in topics or format=='html':
                topics[key]={'id':relative,'label':label,'order':order,'format':format}
        topics=sorted(topics.values(),key=lambda t:(t['order'],t['label'].casefold()))
        if topics:subjects.append({'name':folder.name,'topics':topics})
    return {'subjects':subjects}


@lru_cache(maxsize=16)
def _converted_html(source: str) -> bytes:
    from .pearls_word import to_docx
    return to_docx(source)[0]


def word_document(path: Path) -> bytes:
    if path.suffix.lower()=='.docx':return path.read_bytes()
    if path.stat().st_size>10*1024*1024:raise ValueError('This HTML note is too large to convert.')
    return _converted_html(path.read_text(encoding='utf-8-sig'))


def save_word(root: Path,relative: str) -> dict:
    source=resolve(root,relative)
    if source is None or source.suffix.lower() not in {'.html','.htm'}:
        raise ValueError('Choose an HTML Pearl to save as Word.')
    content=word_document(source)
    destination=source.with_suffix('.docx')
    root=root.resolve()
    if not destination.resolve().is_relative_to(root):raise ValueError('Invalid Word destination.')
    if destination.is_file():
        previous=destination.read_bytes()
        if previous==content:return {'saved':True,'path':destination.relative_to(root).as_posix()}
        backup=root/'_backups'/f'word-before-html-export-{time.time_ns()}.zip'
        backup.parent.mkdir(parents=True,exist_ok=True)
        with zipfile.ZipFile(backup,'x',zipfile.ZIP_DEFLATED) as archive:
            archive.writestr(destination.relative_to(root).as_posix(),previous)
        with zipfile.ZipFile(backup) as archive:
            if archive.read(destination.relative_to(root).as_posix())!=previous:raise OSError('Could not verify Word backup.')
    temporary=destination.with_name(f'.{destination.name}.{time.time_ns()}.tmp')
    try:
        temporary.write_bytes(content)
        try:
            os.replace(temporary,destination)
        except PermissionError:
            # Some OneDrive-managed folders permit writes but deny replacement.
            # The verified ZIP above retains the old file if writing is interrupted.
            if not destination.is_file():raise
            try:
                destination.write_bytes(content)
            except OSError:
                destination.write_bytes(previous)
                raise
        if destination.read_bytes()!=content:raise OSError('Could not verify the saved Word file.')
    finally:temporary.unlink(missing_ok=True)
    return {'saved':True,'path':destination.relative_to(root).as_posix()}


PEARLS_CSS=r"""
body.view-home[data-cnl-tab="pearls"] #cnlTabBar{display:flex}
body[data-cnl-tab="pearls"] #cnlPearlsPage{display:block}
body[data-cnl-tab="pearls"] #homeScreen{display:none!important}
#cnlPearlsPage .cnl-pearls-bar{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin-bottom:16px;position:sticky;top:0;z-index:2;background:#f5f4fa;padding:6px 0}
#cnlPearlsPage .cnl-pearls-path{font:700 18px/1.3 "Averia Serif Libre",serif;flex:1}
#cnlPearlsPage .cnl-pearls-topics{display:grid;gap:8px}
#cnlPearlsPage .cnl-pearls-topic{width:100%;display:flex;align-items:center;gap:14px;text-align:left;
 padding:10px 12px;min-height:54px;border:1px solid #d6def1;border-radius:12px;
 background:linear-gradient(110deg,#f2f5fc,#eaf0fa);color:#292664;cursor:pointer;font:700 17px/1.25 "Averia Serif Libre",serif}
#cnlPearlsPage .cnl-pearls-number{display:grid;place-items:center;flex:0 0 32px;height:32px;background:#d9e2f3;border-radius:8px}
.cnl-pearls-format{display:inline-block;padding:3px 7px;border-radius:6px;background:#e0e9f7;color:#28467c;font:700 11px/1.2 system-ui,sans-serif}
#cnlPearlsViewerFrame{position:fixed;inset:0;width:100vw;height:100vh;border:0;z-index:2147480000;background:#f5f4fa}
body.cnl-pearls-viewer #cnlTabBar{display:none!important}
body.cnl-pearls-viewer #paper .cnl-pearl-card{display:block;background:#fff;border:1px solid #d8dfef;border-radius:14px;padding:18px 20px;margin:0 0 18px;min-width:0;box-sizing:border-box}
body.cnl-pearls-viewer #paper .cnl-pearl-card>.doc-block.h1:first-child{margin-top:0!important}
.cnl-pearls-loading{position:fixed;inset:0;z-index:2147480001;display:grid;place-content:center;gap:12px;background:#f5f4fa;color:#292664;font:18px "Averia Serif Libre",serif}

"""

PEARLS_JS=r"""
const cnlPearlsNav={subject:'',topic:'',request:0};

function cnlPearlsChoose(subject,topic=''){
  cnlPearlsNav.subject=subject;cnlPearlsNav.topic=topic;cnlPaintPearlsPage();
}

async function cnlPaintPearlsPage(){
  const page=cnl$('#cnlPearlsPage');if(!page)return;
  const request=++cnlPearlsNav.request;
  const host=page.querySelector('.cnl-tab-list');
  host.replaceChildren();cnlListHint(host,'Loading Pearls…');
  try{
    const response=await fetch('/api/pearls');
    if(!response.ok)throw new Error('Could not load Pearls.');
    const pack=await response.json();if(request!==cnlPearlsNav.request)return;
    host.replaceChildren();
    const subject=pack.subjects.find(s=>s.name===cnlPearlsNav.subject);
    if(cnlPearlsNav.subject&&!subject){cnlPearlsNav.subject='';cnlPearlsNav.topic='';}
    if(!subject){
      if(!pack.subjects.length){cnlListHint(host,'No Pearls yet. Add Word notes to subject folders inside Pearls.');return;}
      const grid=document.createElement('div');grid.className='subject-grid';
      pack.subjects.forEach(s=>{
        const card=document.createElement('button');card.type='button';card.className='subject-card';
        const inner=document.createElement('div');
        const icon=document.createElement('div');icon.className='subject-icon';icon.textContent=subjectInitial(s.name);
        const name=document.createElement('div');name.className='subject-name';name.textContent=s.name;
        const count=document.createElement('div');count.className='subject-count';count.textContent=cnlCount(s.topics.length,'topic');
        inner.append(icon,name,count);card.append(inner);card.addEventListener('click',()=>cnlPearlsChoose(s.name));grid.append(card);
      });host.append(grid);return;
    }
    let topic=subject.topics.find(t=>t.id===cnlPearlsNav.topic);
    if(!topic)cnlPearlsNav.topic='';
    const bar=document.createElement('div');bar.className='cnl-pearls-bar';
    const back=cnlStudyButton(bar,topic?'Back to topics':'Back to subjects',()=>cnlPearlsChoose(topic?subject.name:''));
    const path=document.createElement('div');path.className='cnl-pearls-path';
    path.textContent=['Pearls',subject.name,topic?.label].filter(Boolean).join(' › ');bar.append(path);host.append(bar);
    if(!topic){
      const list=document.createElement('div');list.className='cnl-pearls-topics';
      subject.topics.forEach((t,index)=>{
        const button=document.createElement('button');button.type='button';button.className='cnl-pearls-topic';
        const number=document.createElement('span');number.className='cnl-pearls-number';number.textContent=String(index+1);
        const name=document.createElement('span');name.textContent=t.label;name.style.flex='1';
        const format=document.createElement('span');format.className='cnl-pearls-format';format.textContent=t.format==='html'?'HTML':'WORD';
        button.append(number,name,format);button.addEventListener('click',()=>cnlPearlsChoose(subject.name,t.id));list.append(button);
      });host.append(list);return;
    }
    cnlOpenPearlsViewer(topic,subject);

  }catch(error){
    if(request!==cnlPearlsNav.request)return;
    cnlListHint(host,error.message||'Could not load Pearls.');
    cnlStudyButton(host,'Try again',()=>cnlPaintPearlsPage());
    cnlStudyButton(host,'Back to subjects',()=>cnlPearlsChoose(''));
  }
}

function cnlInstallPearls(){
  const tabs=cnl$('#cnlTabBar');if(!tabs||cnl$('#cnlPearlsPage'))return;
  const tab=document.createElement('button');tab.type='button';tab.className='cnl-tab';tab.dataset.cnlTab='pearls';
  const icon=document.createElement('span');icon.className='cnl-tab-icon';icon.innerHTML=cnlPngIcon('book');
  const label=document.createElement('span');label.textContent='Pearls';tab.append(icon,label);
  tab.addEventListener('click',()=>cnlSetTab('pearls'));tabs.append(tab);
  const drawer=cnl$('#cnlDrawer');
  if(drawer){
    const row=document.createElement('button');row.type='button';row.className='cnl-drawer-row';
    const mark=document.createElement('span');mark.innerHTML=cnlPngIcon('book');row.append(mark,document.createTextNode('Pearls'));
    row.addEventListener('click',()=>cnlSetTab('pearls'));drawer.insertBefore(row,drawer.children[4]||null);
  }
  const page=document.createElement('section');page.id='cnlPearlsPage';page.className='cnl-tab-page';
  const heading=document.createElement('h2');heading.textContent='Pearls';
  const list=document.createElement('div');list.className='cnl-tab-list';page.append(heading,list);document.body.append(page);
  const original=cnlSetTab;
  cnlSetTab=function(tab){original(tab);if(tab==='pearls')cnlPaintPearlsPage();};
}
"""


PEARLS_VIEWER_JS=r"""
window.cnlBuildPearlCards=function(root){
  if(!document.body.classList.contains('cnl-pearls-viewer')||!root||root.querySelector(':scope > .cnl-pearl-card'))return;
  let card=null;
  for(const child of [...root.children]){
    if(child.matches('.cnl-ink-wash,.cnl-ink-pen,.cnl-layout-grip'))continue;
    const head=child.matches('.doc-p.h1')?child:child.querySelector('.doc-p.h1');
    if(head){
      card=document.createElement('section');card.className='cnl-pearl-card';
      card.setAttribute('aria-label',head.dataset.headingText||head.textContent.trim());
      root.insertBefore(card,child);
    }
    if(card)card.append(child);
  }
};
function cnlClosePearlsViewer(){
  const frame=cnl$('#cnlPearlsViewerFrame');
  if(frame)frame.remove();
  cnlPearlsNav.topic='';
  cnlPaintPearlsPage();
}

function cnlOpenPearlsViewer(topic,subject){
  cnl$('#cnlPearlsViewerFrame')?.remove();
  const frame=document.createElement('iframe');
  frame.id='cnlPearlsViewerFrame';frame.title='Pearls viewer — '+topic.label;
  const query=new URLSearchParams({id:topic.id,subject:subject.name,label:topic.label});
  frame.src='/pearls/viewer?'+query;
  document.body.append(frame);
}

window.addEventListener('message',event=>{
  const frame=cnl$('#cnlPearlsViewerFrame');
  if(event.origin!==location.origin||event.source!==frame?.contentWindow)return;
  if(event.data?.type==='cnl-pearls-close'){
    if(event.data.home===true){frame.remove();cnlPearlsNav.topic='';cnlHeaderGoHome();}
    else cnlClosePearlsViewer();
  }
});

async function cnlBootPearlsViewer(){
  if(location.pathname!=='/pearls/viewer')return;
  document.body.classList.add('cnl-pearls-viewer');
  const loading=document.createElement('div');loading.className='cnl-pearls-loading';loading.textContent='Opening Pearl…';document.body.append(loading);
  const close=(home=false)=>{
    if(window.parent!==window)window.parent.postMessage({type:'cnl-pearls-close',home:home===true},location.origin);
    else location.href='/';
  };
  // Capture at window level before the Notes copy's header handlers, so Back
  // returns to Pearls without touching the main Notes reader's document or scope.
  window.addEventListener('click',event=>{
    if(!event.target.closest?.('#headerBackBtn,#headerHomeBtn'))return;
    event.preventDefault();event.stopImmediatePropagation();close(!!event.target.closest('#headerHomeBtn'));
  },true);
  try{
    await window.cnlPearlsLibraryBoot;
    const params=new URLSearchParams(location.search),id=params.get('id')||'';
    const response=await fetch('/api/pearls/document?id='+encodeURIComponent(id));
    if(!response.ok)throw new Error('Could not open this Pearl.');
    const sourceName=id.split('/').pop(),isHtml=/\.html?$/i.test(sourceName);
    const name=sourceName.replace(/\.html?$/i,'.docx'),subject=params.get('subject')||id.split('/')[0];
    const label=params.get('label')||sourceName.replace(/\.(docx|html?)$/i,'');
    const blob=new File([await response.blob()],name,{type:'application/vnd.openxmlformats-officedocument.wordprocessingml.document'});
    const key='pearls:'+id;
    const record={pendingKey:key,id:key,key,folderName:'Pearls · '+subject,displayName:label,fileName:name,
      mimeType:blob.type,blob,file:blob,headings:[],serverPath:'/api/pearls/document?id='+encodeURIComponent(id),
      serverRelativePath:'Pearls - '+subject+'/'+name,serverFresh:true};
    pendingDocuments.push(record);
    currentSubject=record.folderName;currentReaderDocKey=key;
    await openPendingDocument(key);
    setAppView('reader');renderReaderSidebar(record);
    const back=cnl$('#headerBackBtn');if(back){back.hidden=false;back.disabled=false;back.title='Back to Pearls';back.setAttribute('aria-label','Back to Pearls');}
    if(isHtml){
      const actions=cnl$('.reader-header-actions');
      const format=document.createElement('span');format.className='cnl-pearls-format';format.textContent='HTML';
      const save=document.createElement('button');save.type='button';save.className='icon-btn reader-only';save.id='cnlPearlsSaveWord';
      save.title='Save as Word';save.setAttribute('aria-label','Save as Word');
      save.innerHTML='<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M14 3H5v18h14V8zM14 3v5h5M7 12l2 6 3-6 3 6 2-6"/></svg>';
      save.addEventListener('click',async()=>{
        save.disabled=true;
        try{
          const result=await fetch('/api/pearls/save-word',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({id})});
          const data=await result.json();if(!result.ok)throw new Error(data.error||'Could not save Word file.');
          cnlToast('Saved Word file: Pearls/'+data.path);
        }catch(error){cnlToast(error.message||'Could not save Word file.');}
        finally{save.disabled=false;}
      });
      actions?.prepend(format,save);
    }
    document.title=label+' — Pearls';
    loading.remove();
  }catch(error){
    loading.textContent=error.message||'Could not open this Pearl.';
    cnlStudyButton(loading,'Back to Pearls',close);
  }
}
if(location.pathname==='/pearls/viewer'){
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',cnlBootPearlsViewer,{once:true});
  else setTimeout(cnlBootPearlsViewer,0);
}
"""


def viewer_html(app_html: str) -> str:
    """An isolated copy of the Notes viewer, with its own document and UI state."""
    anchor='loadServerLibrary().catch(err=>{'
    if app_html.count(anchor)!=1:
        raise ValueError('Could not locate Notes library bootstrap for the Pearls viewer copy')
    return app_html.replace(anchor,'window.cnlPearlsLibraryBoot = '+anchor,1)
