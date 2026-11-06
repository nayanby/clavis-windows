"""Consumer Cortex study navigation adapted to the desktop DOM."""

STUDY_BRIDGE_JS = r"""
window.cnlGenerateTopicQuiz = async function(keyword, count, depth) {
  if(!aiGetActiveKey('quiz'))throw new Error('Save your quiz API key in AI Settings first.');
  const prompt=aiBuildEditablePrompt('quiz',{count:Number(count)||8,depth})+'\n\nTOPIC: '+keyword+'\nCreate original questions using established clinical knowledge about this topic. There are no supplied notes for this topic-based request. Do not invent precise criteria, drug doses or citations when uncertain.';
  const data=await aiCallSelectedProvider(prompt,QUIZ_SCHEMA,'quiz');
  if(!Array.isArray(data.questions)||!data.questions.length)throw new Error('No questions were generated.');
  const row={folder:'AI Practice',document:keyword,headingText:'Practice: '+keyword,
    questions:data.questions,madeAt:Date.now()};
  const res=await fetch('/api/saved-quiz',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(row)});
  if(!res.ok)throw new Error('Could not save the generated quiz.');
  return {...row,studyLabel:keyword};
};
window.cnlStartLibraryCards = function(entries, label) {
  const lib = aiGetFlashcardLibrary();
  const cards = [];
  entries.forEach(entry => {
    if (!entry.key) return;
    lib[entry.key] = entry;
    (entry.data?.cards || []).forEach(card => cards.push({
      ...card, _libraryEntryKey:entry.key,
      _sourceDocument:entry.documentName, _sourceFolder:entry.folderName
    }));
  });
  aiSetFlashcardLibrary(lib);
  aiFlashcardReviewMode = 'due';
  aiFlashcardSession = null;
  aiRenderFlashcards({cards,aggregateRange:'all',aggregateLabel:label}, {
    preserve:false, saved:true, descriptor:{scopeKey:'library-review',scopeLabel:label}
  });
  aiFlashcardSession.aggregateRange = 'all';
};
const cnlOriginalPersistCards=aiPersistCurrentFlashcardSession;
window.cnlSetLibraryFlashSession=entry=>{if(aiFlashcardSession)aiFlashcardSession.libraryEntry=entry;};
aiPersistCurrentFlashcardSession=async function(){
  if(aiFlashcardSession?.libraryEntry){
    const session=aiFlashcardSession;
    const entry={...session.libraryEntry,data:session.data,savedAt:new Date().toISOString()};
    const lib=aiGetFlashcardLibrary();
    const empty=!entry.data.cards.length;
    if(empty)delete lib[entry.key];else lib[entry.key]=entry;
    aiSetFlashcardLibrary(lib);
    const scopeKey=entry.scope?.scopeKey || entry.scopeKey || entry.key.split('::').slice(1).join('::');
    const doc=entry.doc || (entry.folderName+'/'+String(entry.documentName||'Note').replace(/\.docx$/i,'')+'.docx');
    const payload=empty ? {op:'delete',doc,documentKey:entry.documentKey||entry.recordKey||entry.key.split('::')[0],
      scope:entry.storageScope||'flashcards-'+scopeKey} : {kind:'flashcards',decks:[entry]};
    const res=await fetch(empty?'/api/poster':'/api/study-pack',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload)});
    if(!res.ok)throw new Error('Could not save flashcard review progress.');
    session.saved=true;
    return;
  }
  await cnlOriginalPersistCards();
  if(!aiFlashcardSession?.aggregateRange)return;
  const keys=new Set(aiFlashcardSession.data.cards.map(card=>card._libraryEntryKey));
  const lib=aiGetFlashcardLibrary();
  const decks=Array.from(keys,key=>lib[key]).filter(Boolean);
  try{
    const res=await fetch('/api/study-pack',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({kind:'flashcards',decks})});
    if(!res.ok)throw new Error('Could not save flashcard review progress.');
  }catch(error){console.warn(error);window.cnlToast?.('Review saved locally; could not sync the deck file.');}
};
"""

STUDY_NAV_JS = r"""
cnlOpenSavedQuiz=function(row,options={}){
  if(!row?.questions?.length)return;
  const mount=cnlStudyMountFor('cnlQuizPage');
  mount?.querySelector(':scope > .folder-btn')?.remove();
  cnlMountStudyResult(mount);window.aiSetInterfaceMode?.('quiz');
  window.cnlRenderSavedQbank(row,{...options,onExit:options.onExit||(()=>{
    cnlRestoreStudyResult();cnlStudyMountFor('cnlQuizPage')?.replaceChildren();cnlStudyRender(cnlStudyQuiz);
  })});
};
const cnlStudyStyle=document.createElement('style');
cnlStudyStyle.textContent=`
.cnl-study-setup{display:grid;gap:12px;margin:0 0 14px}
.cnl-study-setup[hidden],.cnl-tab-list[hidden]{display:none!important}
.cnl-study-bar{display:flex;align-items:center;gap:8px;padding-bottom:10px;border-bottom:1px solid #d9e1ec}
.cnl-study-path{flex:1 1 auto;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font:700 20px/1.2 "Averia Serif Libre",serif;color:var(--cnl-ink,#292664)}
.cnl-study-fields{display:flex;gap:8px;flex-wrap:wrap}
.cnl-study-field{display:grid;gap:6px;flex:0 1 220px;color:#516781;font:600 11px/1.1 system-ui,-apple-system,"Segoe UI",sans-serif;letter-spacing:.04em;text-transform:uppercase}
.cnl-study-select{padding:8px 10px;border:1px solid #b9c7db;border-radius:9px;background:#fff;color:#23354f;font:400 13px/1.2 system-ui,-apple-system,"Segoe UI",sans-serif;width:100%}
.cnl-study-actions{display:flex;gap:8px;flex-wrap:wrap;margin:0}
.cnl-study-actions .folder-btn{flex:0 1 auto;margin:0}
.cnl-study-mount>.folder-btn{margin-bottom:14px}
/* The mist wash Deep Dive's own subject and chapter cards carry, restated here
   rather than inherited: those rules hang off #subjectGrid and #subjectScreen,
   which these pages do not use. */
#cnlFlashPage .subject-card,#cnlFlashPage .chapter-card,
#cnlQuizPage .subject-card,#cnlQuizPage .chapter-card{
  background:color-mix(in srgb,var(--cnl-mist,#b5ccf1) 20%,#fff)!important;
}
#cnlFlashPage .subject-card:hover,#cnlFlashPage .chapter-card:hover,
#cnlQuizPage .subject-card:hover,#cnlQuizPage .chapter-card:hover{
  background:color-mix(in srgb,var(--cnl-mist,#b5ccf1) 34%,#fff)!important;
}
/* The desktop sheet hides .chapter-meta outright, which is right on Deep Dive -
   there the line repeats the heading count already in the reader - but here it
   is the one number that says whether a chapter has cards or questions yet. So
   it is put back on these two pages only. */
#cnlFlashPage .chapter-meta,#cnlQuizPage .chapter-meta{display:block!important}
`;
document.head.appendChild(cnlStudyStyle);

/* Quiz and flashcards are browsed the way Deep Dive browses notes: subjects,
   then the chapters inside one, then the Heading 1s inside a chapter. A saved
   deck or quiz hangs off the heading it was made from, matched the way the
   server matches it - folder, note and heading text with everything but letters
   and digits folded away - so the row is the same row the reader would find. */

function cnlFoldHeading(value) {
  return String(value || '').toLowerCase().replace(/[^a-z0-9]+/g, '');
}

const cnlStudyNav = {
  flash: { subject: '', chapter: '', chapterLabel: '' },
  quiz: { subject: '', chapter: '', chapterLabel: '', count: '8', depth: 'standard' }
};

function cnlStudyStem(record) {
  return String(record.fileName || record.displayName || '').replace(/\.docx$/i, '');
}

function cnlStudyKey(folder, doc, label) {
  return [folder, doc, label].map(cnlFoldHeading).join('\u241f');
}

function cnlStudyOrdinal(label) {
  const match=String(label||'').match(/^\s*(\d+|[IVXLCDM]+)[. _-]+/i);
  if(!match)return Number.MAX_SAFE_INTEGER;
  if(/^\d+$/.test(match[1]))return Number(match[1]);
  const roman={I:1,V:5,X:10,L:50,C:100,D:500,M:1000};
  const chars=match[1].toUpperCase().split('');
  return chars.reduce((sum,c,i)=>sum+(roman[c]<(roman[chars[i+1]]||0)?-roman[c]:roman[c]),0);
}

async function cnlStudySaved(kind) {
  const rows = [];
  const push = (folder, doc, label, item) => {
    const clean = String(label || '').trim();
    if (!clean) return;
    const row = {
      folder: String(folder || 'Unfiled') || 'Unfiled',
      doc: String(doc || ''), label: clean,
      key: cnlStudyKey(folder, doc, clean), item
    };
    if (!rows.some(other => other.key === row.key)) rows.push(row);
  };
  if (kind === 'flashcards') {
    const by = await cnlFlashDecksByFolder();
    Object.keys(by).forEach(folder => (by[folder].entries || []).forEach(entry =>
      push(entry.folderName || folder, entry.documentName, entry.scopeLabel, entry)));
    return { rows };
  }
  let pack;
  try{[pack]=await Promise.all([cnlFetchStudyPack('quizzes'),window.cnlQbank.load()]);}
  catch(error){cnlToast(error.message);return null;}
  if (!pack) return null;
  (pack.quizzes || []).forEach(row => {
    if ((row.questions || []).length) push(row.folder, row.document, row.headingText, row);
  });
  return { rows };
}

function cnlStudyTree(saved, savedOnly = false) {
  const folders = new Map();
  const folderNode = name => {
    let node = folders.get(name);
    if (!node) { node = { name, chapters: [] }; folders.set(name, node); }
    return node;
  };

  cnlH1LibraryRecords().forEach(record => {
    const name = String(record.folderName || 'Unfiled') || 'Unfiled';
    const stem = cnlStudyStem(record);
    const label = String(record.displayName || stem);
    const chapter = {
      record, folder: name, label, docKey: cnlFoldHeading(stem),
      keys: new Set([cnlFoldHeading(stem), cnlFoldHeading(label)]),
      heads: [], others: []
    };
    (Array.isArray(record.headings) ? record.headings : []).forEach(head => {
      const text = String((head && head.text) || '').trim();
      if (!text || Number(head && head.level) !== 1) return;
      if (!chapter.heads.some(other => other.label === text)) chapter.heads.push({ label: text, row: null });
    });
    folderNode(name).chapters.push(chapter);
  });

  // A saved item whose note has left the library - renamed, moved, deleted -
  // still gets a chapter of its own rather than vanishing from the browser.
  saved.rows.forEach(row => {
    const folder = folderNode(row.folder);
    let chapter = folder.chapters.find(node => node.keys.has(cnlFoldHeading(row.doc)));
    if (!chapter) {
      chapter = {
        record: null, folder: row.folder, label: row.doc || 'Note',
        docKey: cnlFoldHeading(row.doc), keys: new Set([cnlFoldHeading(row.doc)]),
        heads: [], others: []
      };
      folder.chapters.push(chapter);
    }
    const head = chapter.heads.find(node =>
      !node.row && cnlFoldHeading(node.label) === cnlFoldHeading(row.label));
    if (head) head.row = row; else chapter.others.push(row);
    if (Number.isFinite(row.item.chapterOrder)) chapter.order = row.item.chapterOrder;
  });

  let list = Array.from(folders.values());
  if (savedOnly) {
    list.forEach(folder => {
      folder.chapters.forEach(chapter => {
        chapter.heads = chapter.heads.filter(head => head.row);
      });
      folder.chapters = folder.chapters.filter(chapter =>
        chapter.heads.length || chapter.others.length);
    });
    list = list.filter(folder => folder.chapters.length);
  }
  list.forEach(folder => folder.chapters.sort((a, b) =>
    (a.order ?? cnlStudyOrdinal(a.label)) - (b.order ?? cnlStudyOrdinal(b.label))
      || a.label.localeCompare(b.label, undefined, {numeric:true})));
  return list.sort((a, b) => a.name.localeCompare(b.name));
}

function cnlStudyCover(chapter) {
  const have = chapter.heads.filter(head => head.row).length + chapter.others.length;
  return { have, total: Math.max(chapter.heads.length, have) };
}

function cnlStudyQbankTree(saved) {
  const general = saved.rows.filter(row => row.item.navigationGroup === 'general');
  const tree = cnlStudyTree({rows: saved.rows.filter(row => row.item.navigationGroup !== 'general')});
  general.forEach(row => {
    if (!tree.some(group => group.name === row.folder)) tree.push({name:row.folder,chapters:[]});
  });
  tree.forEach(group => {
    group.chapters.forEach(chapter => {
      chapter.heads = chapter.heads.filter(head => head.row);
    });
    const rows = general.filter(row => row.folder === group.name);
    group.chapters.unshift({folder:group.name,label:'General',docKey:'__general__',
      record:null,heads:[],others:rows,isGeneral:true,order:0});
  });
  return tree.sort((a,b) => a.name.localeCompare(b.name));
}

function cnlStudyGroupOf(tree, nav) {
  return tree.find(folder => folder.name === nav.subject) || null;
}

function cnlStudyChapterOf(group, nav) {
  return group && group.chapters.find(chapter => chapter.docKey === nav.chapter) || null;
}

function cnlStudyButton(host, label, action, primary) {
  const button = document.createElement('button');
  button.type = 'button';
  button.className = 'folder-btn' + (primary ? ' primary' : '');
  button.textContent = label;
  button.addEventListener('click', action);
  host.appendChild(button);
  return button;
}

function cnlStudyField(host, label, values, selected, onChange) {
  const wrap = document.createElement('label');
  wrap.className = 'cnl-study-field';
  const text = document.createElement('span');
  text.textContent = label;
  const select = document.createElement('select');
  select.className = 'cnl-study-select';
  values.forEach(pair => {
    const option = document.createElement('option');
    option.value = pair[0];
    option.textContent = pair[1];
    option.selected = pair[0] === selected;
    select.appendChild(option);
  });
  select.addEventListener('change', () => onChange(select.value));
  wrap.append(text, select);
  host.appendChild(wrap);
  return select;
}

// The deck or quiz opens in the page's own mount, below the list it came from,
// and the list is put back exactly as it was when that mount is left.
function cnlStudyOpen(spec, run) {
  const page = cnl$('#' + spec.pageId);
  const mount = cnlStudyMountFor(spec.pageId);
  if (!page || !mount) return;
  mount.replaceChildren();
  cnlStudyButton(mount, 'Back to ' + spec.root, () => {
    cnlRestoreStudyResult();
    mount.replaceChildren();
    cnlStudyRender(spec);
  });
  page.querySelector('.cnl-study-setup').hidden = true;
  page.querySelector('.cnl-tab-list').hidden = true;
  cnlMountStudyResult(mount);
  run();
}

function cnlStudyKeyName(spec) {
  return window.aiProviderLabel?.(spec.aiKind) || spec.keyName;
}

function cnlStudyHasKey(spec) {
  if (typeof window.aiGetActiveKey === 'function' && window.aiGetActiveKey(spec.aiKind)) return true;
  cnlToast('Save your ' + cnlStudyKeyName(spec) + ' API key in AI Settings first.');
  return false;
}

async function cnlStudyCreate(spec, chapter, headingLabel) {
  if (!chapter || !chapter.record) {
    cnlToast('That note is not in the library any more.');
    return;
  }
  if (!cnlStudyHasKey(spec)) return;
  await cnlRunLibraryH1(spec.aiKind, record => record === chapter.record,
    spec.options ? spec.options() : null, headingLabel);
  cnlStudyRender(spec);
}

async function cnlStudyRunNotes(spec, selection, title, message) {
  if (!cnlStudyHasKey(spec)) return;
  if (!await cnlAskConfirm(title, message, 'Create')) return;
  await cnlRunLibraryH1(spec.aiKind, selection, spec.options ? spec.options() : null);
  cnlStudyRender(spec);
}

async function cnlStudyRender(spec) {
  const page = cnl$('#' + spec.pageId);
  if (!page) return;
  const nav = cnlStudyNav[spec.nav];
  const setup = page.querySelector('.cnl-study-setup');
  const list = page.querySelector('.cnl-tab-list');
  if (!setup || !list) return;
  cnlRestoreStudyResult();
  cnlStudyMountFor(spec.pageId)?.replaceChildren();
  setup.hidden = false;
  list.hidden = false;
  setup.textContent = '';
  list.textContent = '';

  const saved = await spec.load();
  if (!saved) {
    cnlListHint(list, 'Could not load your saved ' + spec.plural + '. Reopen this tab to try again.');
    return;
  }
  const tree = spec.nav === 'quiz' ? cnlStudyQbankTree(saved) : cnlStudyTree(saved);
  const level = nav.chapter ? 2 : nav.subject ? 1 : 0;
  const group = level ? cnlStudyGroupOf(tree, nav) : null;
  const chapter = level === 2 ? cnlStudyChapterOf(group, nav) : null;
  // A subject or chapter can leave the library between paints, so a selection
  // that no longer resolves steps back a level rather than showing nothing.
  if (level && !group) { nav.subject = ''; nav.chapter = ''; return cnlStudyRender(spec); }
  if (level === 2 && !chapter) { nav.chapter = ''; return cnlStudyRender(spec); }

  // The breadcrumb appears only once there is somewhere to go back to. On the
  // subject grid the tab's own heading already names the level, so a bar here
  // would repeat it and add a rule for nothing.
  if (level) {
    const bar = document.createElement('div');
    bar.className = 'cnl-study-bar';
    const back = document.createElement('button');
    back.type = 'button';
    back.className = 'icon-btn';
    back.title = 'Back';
    back.textContent = '\u2190';
    back.addEventListener('click', () => {
      if(spec.nav==='quiz'&&nav.bookmarks){
        if(nav.bookmarks.bank){nav.bookmarks.bank='';nav.bookmarks.bankLabel='';}
        else if(nav.bookmarks.chapter){nav.bookmarks.chapter='';nav.bookmarks.chapterLabel='';}
        else nav.bookmarks=null;
      }else if (level === 2) nav.chapter = ''; else nav.subject = '';
      cnlStudyRender(spec);
    });
    bar.appendChild(back);
    const path = document.createElement('div');
    path.className = 'cnl-study-path';
    path.textContent = [spec.root, nav.subject, nav.chapter && nav.chapterLabel]
      .filter(Boolean).join('  \u203a  ');
    bar.appendChild(path);
    setup.appendChild(bar);
  }

  if(spec.nav==='quiz'&&nav.bookmarks){
    const path=setup.querySelector('.cnl-study-path');
    if(path)path.textContent=[spec.root,nav.subject,'Bookmarks',nav.bookmarks.chapterLabel,nav.bookmarks.bankLabel].filter(Boolean).join(' › ');
    cnlStudyPaintBookmarks(list,group,spec);return;
  }

  if (spec.fields && !(spec.nav==='quiz'&&chapter?.isGeneral)) {
    const fields = document.createElement('div');
    fields.className = 'cnl-study-fields';
    spec.fields(fields, nav);
    if (fields.children.length) setup.appendChild(fields);
  }

  const actions = document.createElement('div');
  actions.className = 'cnl-study-actions';
  spec.actions(actions, { level, nav, tree, group, chapter, spec });
  if (actions.children.length) setup.appendChild(actions);

  if (level === 0) cnlStudyPaintSubjects(list, tree, spec);
  else if (level === 1) cnlStudyPaintChapters(list, group, spec);
  else if (chapter.isGeneral) cnlStudyPaintQuizModules(list, {chapters:[chapter]}, spec);
  else cnlStudyPaintHeadings(list, chapter, spec);
}

function cnlStudyPaintSubjects(host, tree, spec) {
  if (!tree.length) {
    cnlListHint(host, spec.nav === 'quiz'
      ? 'No Qbank modules yet. Import HTML or create a quiz from a topic.'
      : 'Nothing is in the library yet. Add notes in Deep Dive first.');
    return;
  }
  const grid = document.createElement('div');
  grid.className = 'subject-grid';
  tree.forEach(group => {
    const tally = group.chapters.reduce((sum, chapter) => {
      const cover = cnlStudyCover(chapter);
      sum.have += cover.have;
      sum.total += cover.total;
      return sum;
    }, { have: 0, total: 0 });

    const card = document.createElement('article');
    card.className = 'subject-card';
    const inner = document.createElement('div');
    const icon = document.createElement('div');
    icon.className = 'subject-icon';
    icon.textContent = subjectInitial(group.name);
    const name = document.createElement('div');
    name.className = 'subject-name';
    name.textContent = group.name;
    const count = document.createElement('div');
    count.className = 'subject-count';
    count.textContent = spec.nav === 'quiz'
      ? cnlCount(cnlStudyQuizModules(group).length, 'module')
      : cnlCount(group.chapters.length, 'chapter')
        + (tally.total ? ' \u00b7 ' + tally.have + '/' + tally.total + ' ' + spec.short : '');
    inner.append(icon, name, count);
    card.appendChild(inner);
    card.addEventListener('click', () => {
      const nav = cnlStudyNav[spec.nav];
      nav.subject = group.name;
      if(spec.nav==='quiz')nav.bookmarks=null;
      nav.chapter = '';
      nav.chapterLabel = '';
      cnlStudyRender(spec);
    });
    grid.appendChild(card);
  });
  host.appendChild(grid);
}

function cnlStudyPaintChapters(host, group, spec) {
  if(spec.nav==='quiz'){
    const modules=cnlStudyQuizModules(group),count=modules.reduce((n,{row})=>n+window.cnlQbank.marked(row.item).length,0);
    const tile=cnlStudyRow('★ Bookmarks',cnlCount(count,'bookmarked question'),()=>{
      cnlStudyNav.quiz.bookmarks={chapter:'',bank:''};cnlStudyRender(spec);
    });tile.classList.add('cnl-qbank-bookmarks-tile');host.append(tile);
  }
  if (!group.chapters.length) {
    cnlListHint(host, 'No notes in this subject yet.');
    return;
  }
  const grid = document.createElement('div');
  grid.className = 'chapter-grid';
  group.chapters.forEach((chapter, index) => {
    const cover = cnlStudyCover(chapter);
    const card = document.createElement('article');
    card.className = 'chapter-card';
    const number = document.createElement('div');
    number.className = 'chapter-number';
    const order=chapter.order ?? cnlStudyOrdinal(chapter.label);
    number.textContent = chapter.isGeneral ? '' : 'Chapter ' + (order===Number.MAX_SAFE_INTEGER ? index+1 : order);
    const name = document.createElement('div');
    name.className = 'chapter-name';
    name.textContent = chapter.label.replace(/^\s*(?:\d+|[IVXLCDM]+)[. _-]+/i,'');
    const meta = document.createElement('div');
    meta.className = 'chapter-meta';
    meta.textContent = chapter.isGeneral ? cnlCount(chapter.others.length,'module')
      : (cover.total ? cover.have + '/' + cover.total + ' ' + spec.short : 'nothing saved yet')
      + (chapter.record ? '' : ' \u00b7 note is not in the library');
    card.append(number, name, meta);
    if (!chapter.isGeneral) cnlLibraryNumberRow(card,order===Number.MAX_SAFE_INTEGER ? index + 1 : order,name);
    card.addEventListener('click', () => {
      const nav = cnlStudyNav[spec.nav];
      nav.chapter = chapter.docKey;
      nav.chapterLabel = chapter.label;
      cnlStudyRender(spec);
    });
    grid.appendChild(card);
  });
  host.appendChild(grid);
}

function cnlStudyQuizModules(group) {
  const modules = [];
  (group.chapters || []).forEach(chapter => {
    const rows = [...chapter.heads.filter(head => head.row).map(head => head.row), ...chapter.others];
    rows.forEach(row => {
      if ((row.item.questions || []).length) modules.push({chapter, row});
    });
  });
  return modules.sort((a,b) =>
    (a.row.item.chapterOrder ?? cnlStudyOrdinal(a.chapter.label))
      - (b.row.item.chapterOrder ?? cnlStudyOrdinal(b.chapter.label))
    || (a.row.item.topicOrder ?? 1) - (b.row.item.topicOrder ?? 1)
    || a.row.label.localeCompare(b.row.label, undefined, {numeric:true}));
}

function cnlStudyPaintQuizModules(host, group, spec) {
  const modules = cnlStudyQuizModules(group);
  if (!modules.length) {
    cnlListHint(host, 'No Qbank modules in this subject yet.');
    return;
  }
  const grid = document.createElement('div');
  grid.className = 'chapter-grid';
  modules.forEach(({chapter,row},index) => {
    const card = document.createElement('article');
    card.className = 'chapter-card';
    const name = document.createElement('div');
    name.className = 'chapter-name';
    name.textContent = row.label.replace(/^\s*(?:\d+|[IVXLCDM]+)[. _-]+/i,'');
    const meta = document.createElement('div');
    meta.className = 'chapter-meta';
    meta.textContent = cnlCount(row.item.questions.length, 'question');
    card.append(name,meta);
    // Ordering comes from numbered chapter/topic folders; the displayed module
    // number is sequential even when a note has more than one saved bank.
    cnlLibraryNumberRow(card,index+1,name);
    window.cnlQbank.decorate(card,row.item,options=>cnlStudyOpen(spec,()=>cnlOpenSavedQuiz(row.item,options)),()=>cnlStudyRender(spec));
    grid.appendChild(card);
  });
  host.appendChild(grid);
}

function cnlStudyPaintHeadings(host, chapter, spec) {
  const rows = [];
  const topics=chapter.heads.map((head,index)=>({label:head.label,row:head.row,index}));
  chapter.others.forEach(row=>topics.push({label:row.label,row,index:topics.length}));
  const numbered=topics.some(topic=>Number.isFinite(topic.row?.item.topicOrder));
  const rank=topic=>topic.row?.item.topicOrder ?? (numbered ? Number.MAX_SAFE_INTEGER : topic.index+1);
  topics.sort((a,b)=>rank(a)-rank(b)||a.index-b.index);
  topics.forEach(topic=>{
    const order=topic.row?.item.topicOrder;
    const label=order ? String(order).padStart(2,'0')+'. '+topic.label : topic.label;
    rows.push(topic.row ? spec.savedRow(chapter,label,topic.row)
      : cnlStudyRow(label,spec.missingDetail,()=>cnlStudyCreate(spec,chapter,topic.label)));
  });
  if (!rows.length) {
    cnlListHint(host, spec.nav === 'quiz' ? 'No saved quizzes in this document yet.'
      : 'This note has no headings listed yet. The button above works through the whole note, or open it in Deep Dive first.');
    return;
  }
  rows.forEach((row,index) => {
    const label=row.querySelector('b');
    const match=label?.textContent.match(/^\s*(\d+)[. _-]+/);
    cnlLibraryNumberRow(row,match ? Number(match[1]) : index + 1,label);
    host.appendChild(row);
  });
}

function cnlStudyPaintBookmarks(host, group, spec){
  const nav=cnlStudyNav.quiz.bookmarks,Q=window.cnlQbank,chapters=new Map();
  cnlStudyQuizModules(group).forEach(({row})=>{
    const indices=Q.marked(row.item);if(!indices.length)return;
    const key=JSON.stringify([row.item.navigationGroup||'legacy',row.item.document||'']);
    if(!chapters.has(key))chapters.set(key,{key,label:row.item.document||row.label,banks:[]});
    chapters.get(key).banks.push({row,indices});
  });
  if(!chapters.size){cnlListHint(host,'No bookmarked questions in this subject yet.');return;}
  const selected=chapters.get(nav.chapter);
  if(nav.chapter&&!selected){nav.chapter='';nav.chapterLabel='';nav.bank='';nav.bankLabel='';cnlStudyRender(spec);return;}
  if(!selected){
    chapters.forEach(chapter=>host.append(cnlStudyRow(chapter.label,
      cnlCount(chapter.banks.reduce((n,bank)=>n+bank.indices.length,0),'bookmarked question'),()=>{
        nav.chapter=chapter.key;nav.chapterLabel=chapter.label;cnlStudyRender(spec);
      })));
    return;
  }
  const bank=selected.banks.find(bank=>bank.row.key===nav.bank);
  if(nav.bank&&!bank){nav.bank='';nav.bankLabel='';cnlStudyRender(spec);return;}
  if(!bank){
    selected.banks.forEach(bank=>host.append(cnlStudyRow(bank.row.label,cnlCount(bank.indices.length,'bookmarked question'),()=>{
      nav.bank=bank.row.key;nav.bankLabel=bank.row.label;cnlStudyRender(spec);
    })));
    return;
  }
  const attempt=Q.attempt(bank.row.item);
  bank.indices.forEach(index=>{
    const question=bank.row.item.questions[index],answer=attempt?.answers[index];
    const detail=answer==null?'Your answer: Not answered':answer===-1?'Reviewed as recall':'Your answer: '+String.fromCharCode(65+answer)+'. '+question.options[answer];
    host.append(cnlStudyRow((index+1)+'. '+question.question,detail,()=>{
      cnlStudyOpen(spec,()=>cnlOpenSavedQuiz(bank.row.item,{review:true,bookmarksOnly:true,questionIndices:[index]}));
    }));
  });
}

function cnlStudyFlashEntries(tree, subject) {
  const entries = [];
  tree.forEach(group => {
    if (subject && group.name !== subject) return;
    group.chapters.forEach(chapter => {
      chapter.heads.forEach(head => head.row && entries.push(head.row.item));
      chapter.others.forEach(row => entries.push(row.item));
    });
  });
  return entries;
}

function cnlStudyCardsDue(cards) {
  const now = Date.now();
  return cards.filter(card => {
    const review = card && card.review;
    return !review || review.state === 'new' || !(Number(review.due) > 0) || Number(review.due) <= now;
  }).length;
}

const cnlStudyFlash = {
  nav: 'flash',
  pageId: 'cnlFlashPage',
  root: 'Flashcards',
  plural: 'decks',
  short: 'headings with cards',
  aiKind: 'flashcards',
  keyName: 'flashcard',
  missingDetail: 'No cards yet \u00b7 makes them from this heading',
  load: () => cnlStudySaved('flashcards'),
  savedRow(chapter, label, row) {
    const cards = (row.item.data && row.item.data.cards) || [];
    return cnlStudyRow(label,
      cnlCount(cards.length, 'card') + ' \u00b7 ' + cnlStudyCardsDue(cards) + ' due',
      () => cnlStudyOpen(cnlStudyFlash, () => cnlOpenFlashDeck(row.item)));
  },
  actions(host, state) {
    const review = (buttonLabel, deckLabel, entries) => cnlStudyButton(host, buttonLabel, () => {
      if (!entries.length) {
        cnlToast('No saved flashcards' + (deckLabel ? ' in ' + deckLabel : ' anywhere') + ' yet.');
        return;
      }
      cnlStudyOpen(cnlStudyFlash, () => {
        window.aiSetInterfaceMode?.('flashcards');
        window.cnlStartLibraryCards(entries, deckLabel || 'All subjects');
      });
    }, true);

    if (state.level === 0) {
      review('Review due cards', '', cnlStudyFlashEntries(state.tree));
      cnlStudyButton(host, 'Flashcard settings', () => cnlOpenFsrsPanel());
      return;
    }
    if (state.level === 1) {
      review('Review due in ' + state.group.name, state.group.name,
        cnlStudyFlashEntries(state.tree, state.group.name));
      return;
    }
    if (state.chapter.record) {
      cnlStudyButton(host, 'Make cards for every heading in this note', () => cnlStudyRunNotes(
        cnlStudyFlash,
        record => record === state.chapter.record,
        'Flashcards for ' + state.chapter.label,
        'Make flashcards for every Heading 1 in \u201c' + state.chapter.label
          + '\u201d that has none yet? How many cards a section gets follows from its own length.'
      ), true);
    }
  }
};

function cnlStudyChapterQuestions(chapter) {
  const rows = chapter.heads.filter(head => head.row).map(head => head.row).concat(chapter.others);
  const seen = new Set();
  const questions = [];
  rows.forEach(row => (row.item.questions || []).forEach((question, index) => {
    const id = question.sourceId || JSON.stringify([question.question, question.options]);
    if (seen.has(id)) return;
    seen.add(id);
    questions.push(window.cnlSetQuizOrigin({
      ...question,
      chapter: question.chapter || row.label,
      subject: question.subject || row.folder,
      exam: String(question.exam || row.item.exam || '').trim()
    }, row.item, index));
  }));
  return questions;
}

function cnlStudySample(questions, count) {
  const copy = questions.slice();
  for (let i = copy.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy.slice(0, Number(count) || 8);
}

const cnlStudyQuiz = {
  nav: 'quiz',
  pageId: 'cnlQuizPage',
  root: 'Qbank',
  plural: 'quizzes',
  short: 'headings with quizzes',
  aiKind: 'quiz',
  keyName: 'quiz',
  missingDetail: 'No quiz yet \u00b7 writes one from this heading',
  load: () => cnlStudySaved('quizzes'),
  options: () => ({ count: cnlStudyNav.quiz.count, depth: cnlStudyNav.quiz.depth }),
  fields(host, nav) {
    cnlStudyField(host, 'Questions per new quiz', [['5', '5'], ['8', '8'], ['12', '12'], ['20', '20']],
      nav.count, value => { nav.count = value; });
    cnlStudyField(host, 'New quiz depth', [['basic', 'Basic'], ['standard', 'Standard'],
      ['advanced', 'Advanced'], ['ini_ss', 'INI-SS']], nav.depth, value => { nav.depth = value; });
  },
  savedRow(chapter, label, row) {
    const questions = row.item.questions || [];
    const exams = Array.from(new Set(questions.map(question =>
      String(question.exam || row.item.exam || '').trim()))).filter(Boolean);
    const tile=document.createElement('article');tile.className='cnl-study-row';
    const content=document.createElement('div'),name=document.createElement('b'),detail=document.createElement('small');
    name.textContent=label;detail.textContent=questions.length+' questions'+(exams.length?' · '+exams.join(' / '):'');content.append(name,detail);tile.append(content);
    window.cnlQbank.decorate(tile,row.item,options=>cnlStudyOpen(cnlStudyQuiz,()=>cnlOpenSavedQuiz(row.item,options)),()=>cnlStudyRender(cnlStudyQuiz));
    return tile;
  },
  actions(host, state) {
    const nav = state.nav;
    if (state.level === 0) {
      cnlStudyButton(host, 'Convert to JSON', () => window.cnlConvertQbankHtml());
      cnlStudyButton(host, 'Import HTML Qbank', () => window.cnlImportQbankHtml(() => cnlStudyRender(cnlStudyQuiz)));
      cnlStudyButton(host, 'Create a quiz from a topic', async () => {
        if (!cnlStudyHasKey(cnlStudyQuiz)) return;
        const keyword = String(window.prompt('What should the quiz be about?') || '').trim();
        if (!keyword) return;
        const button = host.lastElementChild;
        button.disabled = true;
        button.textContent = 'Creating quiz\u2026';
        try {
          const row = await window.cnlGenerateTopicQuiz(keyword, nav.count, nav.depth);
          cnlStudyOpen(cnlStudyQuiz, () => cnlOpenSavedQuiz(row));
        } catch (err) {
          cnlToast(err.message || 'Could not create that quiz.');
        } finally {
          button.disabled = false;
          button.textContent = 'Create a quiz from a topic';
        }
      }, true);
      return;
    }
    if (state.level === 1) {
      cnlStudyButton(host, 'Write quizzes for every heading in ' + state.group.name, () => cnlStudyRunNotes(
        cnlStudyQuiz,
        record => String(record.folderName || 'Unfiled') === state.group.name,
        'Quizzes for ' + state.group.name,
        'Write a quiz for every Heading 1 in \u201c' + state.group.name
          + '\u201d that has none yet? The quizzes are kept, so you can take them later without spending the key again.'
      ), true);
      return;
    }
    if (state.chapter.isGeneral) return;
    if (state.chapter.record) {
      cnlStudyButton(host, 'Write a quiz for every heading in this note', () => cnlStudyRunNotes(
        cnlStudyQuiz,
        record => record === state.chapter.record,
        'Quizzes for ' + state.chapter.label,
        'Write a quiz for every Heading 1 in \u201c' + state.chapter.label
          + '\u201d that has none yet? The quizzes are kept, so you can take them later without spending the key again.'
      ));
    }
  }
};

async function cnlPaintFlashPage() {
  await cnlStudyRender(cnlStudyFlash);
}

async function cnlPaintQuizPage() {
  await cnlStudyRender(cnlStudyQuiz);
};
"""
