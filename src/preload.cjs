const {contextBridge,ipcRenderer}=require('electron');
const invoke=(name,...args)=>ipcRenderer.invoke(name,...args);
contextBridge.exposeInMainWorld('clavis',{
  load:()=>invoke('state:load'), importFiles:kind=>invoke('library:import',kind), importFolder:()=>invoke('library:folder'),
  updateBook:(id,patch)=>invoke('library:update',id,patch),removeBook:id=>invoke('library:remove',id),deleteBook:id=>invoke('library:delete',id),
  settings:patch=>invoke('settings:update',patch),feeds:()=>invoke('feeds:list'),feedAdd:(kind,url)=>invoke('feeds:add',kind,url),
  feedRefresh:id=>invoke('feeds:refresh',id),feedRemove:id=>invoke('feeds:remove',id),article:url=>invoke('article:read',url),playEpisode:(feed,id)=>invoke('feeds:play',feed,id),
  getInk:id=>invoke('reader:ink',id),saveInk:(id,ink)=>invoke('reader:save-ink',id,ink),
  getTranscript:id=>invoke('audio:transcript',id),saveTranscript:(id,data)=>invoke('audio:save-transcript',id,data),
  prepareAudio:(id,force=false)=>invoke('audio:prepare',id,force),
  chapterScanStart:id=>invoke('audio:scan-start',id),chapterScanRead:id=>invoke('audio:scan-read',id),chapterScanCancel:id=>invoke('audio:scan-cancel',id),applySpokenChapters:(id,markers)=>invoke('audio:apply-spoken',id,markers),
  openURL:url=>invoke('system:open',url),openFiles:()=>invoke('system:files'),
  saveNote:note=>invoke('notes:save',note),deleteNote:id=>invoke('notes:delete',id),exportNote:id=>invoke('notes:export',id),exportDrawing:(id,png)=>invoke('notes:export-drawing',id,png),
  downloads:()=>invoke('downloads:list'),downloadAdd:url=>invoke('downloads:add',url),downloadAction:(id,action)=>invoke('downloads:action',id,action),
  onDownloads:fn=>{const handler=(_,data)=>fn(data);ipcRenderer.on('downloads:changed',handler);return()=>ipcRenderer.removeListener('downloads:changed',handler);}
});
