const fs=require('node:fs/promises'),path=require('node:path');
function folderName(value){let name=String(value||'Untitled book').normalize('NFC').replace(/[<>:"/\\|?*\x00-\x1f]/g,' ').replace(/\s+/g,' ').replace(/[. ]+$/g,'').trim().slice(0,140);if(!name)name='Untitled book';if(/^(con|prn|aux|nul|com[1-9]|lpt[1-9])(\.|$)/i.test(name))name='Book '+name;return name;}
async function uniqueFolder(root,title){await fs.mkdir(root,{recursive:true});const name=folderName(title);for(let n=1;n<10000;n++){const dir=path.join(root,name+(n===1?'':` (${n})`));try{await fs.mkdir(dir);return dir;}catch(e){if(e.code!=='EEXIST')throw e;}}throw Error('Too many books with this name.');}
function inside(file,dir){const rel=path.relative(path.resolve(dir),path.resolve(file));return rel===''||(!rel.startsWith('..'+path.sep)&&rel!=='..'&&!path.isAbsolute(rel));}
function commonFolder(files){if(!files.length)return null;let root=path.dirname(files[0]);while(files.some(f=>!inside(f,root))){const parent=path.dirname(root);if(parent===root)break;root=parent;}return root;}
async function organizeBook(book,booksFolder){
  const files=[...(book.path?[book.path]:[]),...(book.tracks||[]).map(t=>t.path).filter(Boolean),...(book.cover?[book.cover]:[])];
  if(!files.length||files.every(f=>inside(f,booksFolder)))return book;
  const primary=[...(book.path?[book.path]:[]),...(book.tracks||[]).map(t=>t.path).filter(Boolean)];
  const dest=await uniqueFolder(booksFolder,book.title);const sourceRoot=commonFolder(primary);const moved=new Map(),targets=new Set();
  async function copy(file){if(!file)return file;if(moved.has(file))return moved.get(file);let relative=sourceRoot&&inside(file,sourceRoot)?path.relative(sourceRoot,file):path.basename(file);if(sourceRoot&&/^[a-f0-9]{24}$/i.test(path.basename(sourceRoot)))relative=relative.replace(/^\d{4}[/\\]/,'');let target=path.join(dest,relative);if(!inside(target,dest))throw Error('Invalid book file path');for(let n=2;targets.has(target.toLowerCase());n++){const ext=path.extname(relative);target=path.join(dest,path.dirname(relative),path.basename(relative,ext)+` (${n})`+ext);}targets.add(target.toLowerCase());await fs.mkdir(path.dirname(target),{recursive:true});await fs.copyFile(file,target);moved.set(file,target);return target;}
  if(book.path)book.path=await copy(book.path);for(const track of book.tracks||[])if(track.path)track.path=await copy(track.path);if(book.cover)book.cover=await copy(book.cover);book.source=dest;return book;
}
async function migrateStorage(store,dataFolder){
  const booksFolder=path.join(dataFolder,'Books'),oldFiles=new Set();await fs.mkdir(booksFolder,{recursive:true});
  const rebase=(file,from,to)=>typeof file==='string'&&inside(file,from)?path.join(to,path.relative(from,file)):file;
  for(const job of store.downloads||[]){if(!job.dir||!inside(job.dir,path.join(dataFolder,'Downloads')))continue;try{await fs.access(job.dir);}catch{continue;}const previous=job.dir,target=await uniqueFolder(booksFolder,job.title||'Audiobook');await fs.rmdir(target);await fs.rename(previous,target);job.dir=target;for(const b of store.books){for(const key of ['path','cover','source'])if(b[key])b[key]=rebase(b[key],previous,target);for(const t of b.tracks||[])if(t.path)t.path=rebase(t.path,previous,target);}}
  for(const b of store.books){const previous=[b.path,b.cover,...(b.tracks||[]).map(t=>t.path)].filter(Boolean);try{const copy=structuredClone(b);await organizeBook(copy,booksFolder);Object.assign(b,copy);delete b.storageError;for(const old of previous)if((inside(old,path.join(dataFolder,'Library'))||inside(old,path.join(dataFolder,'Downloads')))&&![b.path,b.cover,...(b.tracks||[]).map(t=>t.path)].includes(old))oldFiles.add(old);}catch(e){b.storageError='Could not migrate files: '+e.message;}}
  return [...oldFiles];
}
async function removeMigratedFiles(files,dataFolder){for(const file of files){if(!inside(file,path.join(dataFolder,'Library'))&&!inside(file,path.join(dataFolder,'Downloads')))continue;await fs.unlink(file).catch(()=>{});let dir=path.dirname(file);while(dir!==dataFolder&&inside(dir,dataFolder)){try{await fs.rmdir(dir);}catch{break;}dir=path.dirname(dir);}}}
module.exports={folderName,uniqueFolder,inside,commonFolder,organizeBook,migrateStorage,removeMigratedFiles};
