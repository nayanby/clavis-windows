const {JSDOM}=require('jsdom');
function parseXML(xml){
  const dom=new JSDOM(xml,{contentType:'text/xml'});
  try{
    const doc=dom.window.document;
    const all=Array.from(doc.getElementsByTagName('*'));
    const child=(el,name)=>Array.from(el?.children||[]).find(x=>x.localName===name);
    const text=(el,name)=>child(el,name)?.textContent?.trim()||'';
    const header=all.find(x=>x.localName==='channel')||doc.documentElement;
    const link=el=>{const links=Array.from(el.children).filter(x=>x.localName==='link');const selected=links.find(x=>x.getAttribute('rel')==='alternate')||links.find(x=>!x.getAttribute('rel'));return selected?.getAttribute('href')||selected?.textContent?.trim()||'';};
    const items=all.filter(x=>x.localName==='item'||x.localName==='entry').map(el=>{
      const enc=child(el,'enclosure')||Array.from(el.children).find(x=>x.localName==='link'&&x.getAttribute('rel')==='enclosure');
      const image=Array.from(el.children).find(x=>['thumbnail','image'].includes(x.localName)&& (x.hasAttribute('url')||x.hasAttribute('href')))||Array.from(el.children).find(x=>x.localName==='content'&&x.hasAttribute('url')&&(!x.hasAttribute('type')||x.getAttribute('type').startsWith('image/')));
      const content=child(el,'encoded')||child(el,'content')||child(el,'description')||child(el,'summary');
      return {title:text(el,'title'),guid:text(el,'guid')||text(el,'id'),link:link(el),isoDate:text(el,'pubDate')||text(el,'published')||text(el,'updated')||text(el,'date')||text(el,'publicationDate')||text(el,'coverDate'),content:content?.textContent||'',enclosure:enc?{url:enc.getAttribute('url')||enc.getAttribute('href'),type:enc.getAttribute('type'),length:enc.getAttribute('length')}:undefined,itunes:{image:image?.getAttribute('url')||image?.getAttribute('href')||'',duration:text(el,'duration')}};
    });
    items.sort((a,b)=>(Date.parse(b.isoDate)||0)-(Date.parse(a.isoDate)||0));
    if(!['rss','RDF','feed'].includes(doc.documentElement.localName))throw Error('This address does not contain an RSS or Atom feed.');
    const image=child(header,'image');
    return {title:text(header,'title'),description:text(header,'description')||text(header,'subtitle'),image:{url:text(image,'url')||image?.getAttribute('href')||text(header,'logo')||''},items:items.slice(0,300)};
  }finally{dom.window.close();}
}
module.exports={parseXML};
