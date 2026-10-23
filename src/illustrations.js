// Generated illustrations complement the original Clavis icons; never replace
// navigation, transport icons, real book covers, or publisher artwork.
export const illustration=(name,cls='')=>`<img class="ui-illustration ${cls}" src="../assets/pastel/${name}.png" alt="" decoding="async">`;

export function illustrateEmptyStates(getRoute){
  const keys={Home:'library',EPUB:'library',PDF:'library',Audio:'library',Kindle:'library',Player:'bookmarks',News:'feeds',Journals:'feeds',Podcasts:'feeds',Journalling:'bookmarks',Downloads:'downloads',Settings:'settings'};
  let queued=false;
  const enhance=()=>{
    queued=false;
    document.querySelectorAll('#main .empty:not([data-illustrated]),#main .loading:not([data-illustrated])').forEach(el=>{
      el.dataset.illustrated='true';
      if(!el.querySelector('img'))el.insertAdjacentHTML('afterbegin',illustration(/matching|search|find/i.test(el.textContent)?'search':keys[getRoute()]||'library','empty-art'));
    });
  };
  const observer=new MutationObserver(()=>{if(!queued){queued=true;queueMicrotask(enhance);}});
  observer.observe(document.getElementById('main'),{subtree:true,childList:true});
  enhance();
}

export function dialogArt(title){
  const key=/bookmark|moment|journal|writing/i.test(title)?'bookmarks':/settings|equalizer|speed|sleep|audio settings/i.test(title)?'settings':/rss|source|article|subscription/i.test(title)?'feeds':/import|download|magnet|folder|kindle|export/i.test(title)?'downloads':/find|search/i.test(title)?'search':'library';
  return illustration(key,'dialog-art');
}
