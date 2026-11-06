"""Read-only Pearls shelf stored beside Qbank, with subject and topic browsing."""
from pathlib import Path
import re
from . import study_packs


def resolve(root: Path, relative: str) -> Path | None:
    root=root.resolve()
    if not relative or '\\' in relative or any(p.startswith(('.', '~$')) for p in relative.split('/')):
        return None
    try:
        target=(root/relative).resolve()
    except (ValueError,OSError):
        return None
    if not target.is_relative_to(root) or target.suffix.lower()!='.docx' or not target.is_file():
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
        topics=[]
        for path in folder.rglob('*.docx'):
            relative=path.relative_to(root).as_posix()
            if resolve(root,relative) is None:continue
            label=re.sub(r'^\d+[. _-]+','',path.stem)
            order=study_packs._quiz_number(path.stem) or orders.get((folder.name,re.sub(r'\W','',label).lower()),9999)
            topics.append({'id':relative,'label':label,'order':order})
        topics.sort(key=lambda t:(t['order'],t['label'].casefold()))
        if topics:subjects.append({'name':folder.name,'topics':topics})
    return {'subjects':subjects}


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
#cnlPearlsPage .cnl-pearls-document{padding:22px;background:#fff;border:1px solid #dce1ed;border-radius:14px;overflow-wrap:anywhere}
#cnlPearlsPage .cnl-pearls-document .doc-root{max-width:100%;padding:0}
#cnlPearlsPage .cnl-pearls-document .doc-block{padding:0!important;background:transparent!important;border:0!important}
#cnlPearlsPage .cnl-pearls-document .doc-p,#cnlPearlsPage .cnl-pearls-document .doc-p span{font-family:"Averia Serif Libre",Georgia,serif!important;font-size:17px!important;line-height:1.37!important}
#cnlPearlsPage .cnl-pearls-document .doc-p{margin:0 0 8px!important;text-align:left!important}
#cnlPearlsPage .cnl-pearls-document [data-style-name="Title"],#cnlPearlsPage .cnl-pearls-document [data-style-name="Title"] span{font-size:27px!important;line-height:1.2!important}
#cnlPearlsPage .cnl-pearls-document [data-style-name="Title"]{margin-bottom:18px!important}
#cnlPearlsPage .cnl-pearls-document .doc-p.h1{background:#f8dfeb!important;padding:10px!important;margin-top:22px!important;border-radius:8px;border:0!important}
#cnlPearlsPage .cnl-pearls-document .h1,#cnlPearlsPage .cnl-pearls-document .h1 span{font-size:19px!important;font-weight:700!important;line-height:1.2!important;color:#242348!important}
#cnlPearlsPage .cnl-pearls-document .doc-p:is(.h2,.h3,.h4){margin-top:16px!important;background:transparent!important;border:0!important}
#cnlPearlsPage .cnl-pearls-document :is(.h2,.h3,.h4),#cnlPearlsPage .cnl-pearls-document :is(.h2,.h3,.h4) span{font-size:17px!important;font-weight:700!important;line-height:1.2!important;color:#24568c!important}
#cnlPearlsPage .cnl-pearls-document table{max-width:100%;width:100%!important;table-layout:fixed;border-collapse:collapse;margin:12px 0!important}
#cnlPearlsPage .cnl-pearls-document td,#cnlPearlsPage .cnl-pearls-document th{overflow-wrap:anywhere;border:1px solid #d6d9e6!important;padding:9px!important}
#cnlPearlsPage .cnl-pearls-document td .doc-p,#cnlPearlsPage .cnl-pearls-document td .doc-p span{font-size:16px!important}
#cnlPearlsPage .cnl-pearls-document tr:first-child td{background:#ecf1fa!important}
#cnlPearlsPage .cnl-pearls-document .doc-p span[style*="vertical-align"]{font-size:.75em!important}
#cnlPearlsPage .cnl-pearls-document :is(.h1,.h2,.h3,.h4){scroll-margin-top:12px}
#cnlPearlsPage .cnl-pearls-outline{max-width:min(100%,360px);padding:8px;border:1px solid #cbd5e7;border-radius:8px;background:#fff;color:#292664}
#cnlPearlsPage .cnl-pearls-word{font-size:14px;color:#24568c}
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
        const name=document.createElement('span');name.textContent=t.label;
        button.append(number,name);button.addEventListener('click',()=>cnlPearlsChoose(subject.name,t.id));list.append(button);
      });host.append(list);return;
    }
    const url='/api/pearls/document?id='+encodeURIComponent(topic.id);
    const download=document.createElement('a');download.className='cnl-pearls-word';download.textContent='Save Word file';
    download.href=url;download.download=topic.id.split('/').pop();bar.append(download);
    const paper=document.createElement('article');paper.className='cnl-pearls-document';
    host.append(paper);cnlListHint(paper,'Opening note…');
    const file=await fetch(url);if(!file.ok)throw new Error('Could not open this Pearl.');
    const parser=new DocxPrototype(await file.blob());
    // Pearls retain their authored hierarchy, spacing and colours.
    parser.applyFixedPalette=()=>{};parser.applyCompactSpacing=()=>{};
    await parser.init();const root=await parser.render();
    if(request!==cnlPearlsNav.request)return;
    paper.replaceChildren(root);
    const headings=Array.from(root.querySelectorAll('[data-heading-level]'));
    if(headings.length){
      const outline=document.createElement('select');outline.className='cnl-pearls-outline';outline.setAttribute('aria-label','Jump to heading');
      const placeholder=document.createElement('option');placeholder.textContent='Jump to heading';placeholder.value='';outline.append(placeholder);
      headings.forEach((head,index)=>{
        const option=document.createElement('option');option.value=String(index);
        option.textContent=('  '.repeat(Math.max(0,Number(head.dataset.headingLevel)-1)))+head.textContent.trim();outline.append(option);
      });
      outline.addEventListener('change',()=>{if(outline.value!=='')headings[Number(outline.value)]?.scrollIntoView({block:'start'});});bar.append(outline);
    }
    page.scrollTop=0;
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
