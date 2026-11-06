const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');
class Element {
 constructor(tag){this.tag=tag;this.children=[];this.events={};this.className='';this.textContent='';this.dataset={};}
 append(...nodes){this.children.push(...nodes);}
 appendChild(node){this.append(node);return node;}
 addEventListener(type,fn){this.events[type]=fn;}
 querySelector(selector){return this.querySelectorAll(selector)[0]||null;}
 querySelectorAll(selector){return this.children.flatMap(c=>[...(selector[0]==='.'?c.className.split(' ').includes(selector.slice(1)):c.tag===selector)?[c]:[],...c.querySelectorAll(selector)]);}
 click(){this.events.click?.();}
}
const source=fs.readFileSync('src/cnl_desktop/study_navigation.py','utf8').split('STUDY_NAV_JS = r"""')[1].split('"""')[0];
const records=[{folderName:'Neurology',fileName:'02. Existing note',displayName:'02. Existing note',headings:[{level:1,text:'Available'},{level:1,text:'Empty heading'}]},
 {folderName:'Neurology',fileName:'01. Other note',displayName:'01. Other note',headings:[{level:1,text:'No quiz'}]}];
let opened=null;
const context={window:{},document:{head:new Element('head'),createElement:t=>new Element(t)},
 cnlH1LibraryRecords:()=>records,cnlCount:(n,label)=>n+' '+label+(n===1?'':'s'),
 cnlLibraryNumberRow:(card,n)=>card.dataset.number=String(n),cnlOpenSavedQuiz:item=>opened=item};
vm.createContext(context);vm.runInContext(source,context);
context.cnlStudyOpen=(_spec,run)=>run();context.cnlStudyRender=()=>{};
const item={chapterOrder:2,topicOrder:1,questions:[{question:'Saved question'}]};
const general={navigationGroup:'general',chapterOrder:1,topicOrder:1,questions:[{},{}]};
const saved={rows:[{folder:'Neurology',doc:'02. Existing note',label:'Available',item},
 {folder:'Neurology',doc:'Imported module',label:'Cerebrovascular Diseases',item:general}]};
const full=context.cnlStudyTree(saved);
assert.equal(full[0].chapters.find(c=>c.label==='02. Existing note').heads.length,2,'Flashcard/library navigation preserves missing headings');
const tree=context.cnlStudyQbankTree(saved),group=tree[0];
assert.equal(group.chapters[0].label,'General');
assert.equal(group.chapters.length,3,'General precedes both legacy document folders');
assert.equal(group.chapters[1].label,'01. Other note');
assert.equal(group.chapters[1].heads.length,0,'Empty quiz headings are hidden');
assert.equal(group.chapters[2].heads.length,1);
assert.equal(group.chapters[0].others[0].item,general);
const host=new Element('div');
context.cnlStudyPaintChapters(host,group,{nav:'quiz'});
assert.equal(host.querySelectorAll('.chapter-card').length,3);
assert.equal(host.querySelector('.chapter-name').textContent,'General');
host.querySelector('.chapter-card').click();
assert.equal(vm.runInContext('cnlStudyNav.quiz.chapter',context),'__general__');
const modules=new Element('div');
context.cnlStudyPaintQuizModules(modules,{chapters:[group.chapters[0]]},{nav:'quiz'});
assert.equal(modules.querySelector('.chapter-name').textContent,'Cerebrovascular Diseases');
assert.equal(modules.querySelector('.chapter-meta').textContent,'2 questions');
modules.querySelector('.chapter-card').click();assert.equal(opened,general);
const headings=new Element('div');
context.cnlStudyPaintHeadings(headings,group.chapters[2],{nav:'quiz',savedRow:(_c,label,row)=>{
 const e=new Element('div'),b=new Element('b');b.textContent=label;e.append(b);e.addEventListener('click',()=>opened=row.item);return e;}});
assert.equal(headings.children.length,1);
headings.children[0].click();assert.equal(opened,item);
console.log('PASS: General first, imported modules inside it, legacy documents ordered below, only saved headings, direct quiz opening, other navigation preserved.');
