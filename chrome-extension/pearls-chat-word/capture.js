/* Read rendered chat content only. Never execute, click or submit chat content. */
(() => {
  const VERSION='1.0.28';
  if (globalThis.PearlsCapture?.version===VERSION) return;
  const SKIP = 'button,script,style,noscript,textarea,input,select,nav,[role="button"],[data-pearls-ignore],.sr-only,[aria-hidden="true"]';
  const clean = value => String(value || '').replace(/\u00a0/g, ' ');
  const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
  function citation(element) {
    if (element.matches('[data-citation],[data-citation-index],[data-testid*="citation"],.citation,.citation-marker,.citation-container')) return true;
    if (element.tagName !== 'A' || element.querySelector('img')) return false;
    const label = element.textContent.trim();
    // Source chips can be plain links after the site has flattened its markup.
    return element.matches('[data-testid="webpage-citation-pill"],a[role="doc-biblioref"]')
      || /^(?:\[?\d+\]?|CDC(?: Stacks)?|WHO|NIH|PubMed|NCBI|NICE|FDA|NHS)(?:\s*\+\d+)?$/i.test(label)
      || /^(?:https?:\/\/|www\.)\S+$/i.test(label);
  }
  function site() {
    const host = location.hostname;
    if (host === 'chatgpt.com' || host === 'chat.openai.com') return 'chatgpt';
    if (host === 'claude.ai') return 'claude';
    if (host === 'gemini.google.com') return 'gemini';
    throw Error('Open a ChatGPT, Claude or Gemini conversation and click the extension icon there.');
  }
  function hidden(element) {
    return citation(element) || element.matches(SKIP) || element.hidden || element.closest('[hidden],[aria-hidden="true"]')
      || (element.matches('[data-markdown-copy="exclude"]')&&!element.querySelector('img,svg,canvas')&&!isDiagram(element));
  }
  function arrowText(label) {
    const match = /^([←↑→↓↔↕↖↗↘↙⇐⇑⇒⇓⇔⇕⟵⟶⟷⬅⬆⬇➡])[\uFE0E\uFE0F]?$/.exec(label.trim());
    const glyph = match?.[1] || '';
    return ({ '⬅': '←', '⬆': '↑', '⬇': '↓', '➡': '→' })[glyph] || glyph;
  }
  function arrowGlyph(element) {
    const label = element.getAttribute('alt') || element.getAttribute('aria-label') || element.querySelector('title')?.textContent || '';
    const source = (element.getAttribute('src') || '').split(/[?#]/)[0];
    const directions = { down: '↓', up: '↑', left: '←', right: '→' };
    const named = /(?:^|[\s/_-])(?:arrow|chevron)[-_ ](down|up|left|right)(?=$|[.\s_-])/i.exec(`${label} ${element.getAttribute('class') || ''} ${source}`);
    const emoji = /\/(2190|2191|2192|2193|2b05|2b06|2b07|27a1)(?:-fe0f)?\.(?:svg|png|webp)$/i.exec(source);
    return arrowText(label) || (named ? directions[named[1].toLowerCase()] : '') || (emoji ? arrowText(String.fromCodePoint(parseInt(emoji[1], 16))) : '');
  }
  function inlines(node, format = {}) {
    if (node.nodeType === Node.TEXT_NODE) return [{ text: clean(node.nodeValue), ...format }];
    if (node.nodeType !== Node.ELEMENT_NODE || hidden(node)) return [];
    const tag = node.tagName.toLowerCase();
    const arrow = node.matches('img,svg') && arrowGlyph(node);
    if (arrow) return [{ text: arrow, ...format }];
    if (tag === 'br') return [{ text: '\n', ...format }];
    if (tag === 'img') return [{ text: node.alt || '[Image]', ...format }];
    // KaTeX duplicates its visible and accessible representations. Preserve LaTeX once.
    if (node.matches('.katex,.MathJax,mjx-container,math')) {
      const latex = node.querySelector('annotation[encoding="application/x-tex"]')?.textContent;
      return [{ text: latex || node.getAttribute('aria-label') || node.textContent, ...format, math: true, mathml: (node.matches('math') ? node : node.querySelector('math'))?.outerHTML }];
    }
    const next = { ...format };
    if (tag === 'strong' || tag === 'b') next.bold = true;
    if (tag === 'em' || tag === 'i') next.italic = true;
    if (tag === 'u') next.underline = true;
    if (tag === 'del' || tag === 's') next.strike = true;
    if (tag === 'code') next.code = true;
    if (tag === 'mark') next.highlight = true;
    if (tag === 'sub') next.sub = true;
    if (tag === 'sup') next.sup = true;
    // Keep substantive linked prose as plain text, without exporting hyperlinks.
    return [...node.childNodes].flatMap(child => inlines(child, next));
  }
  const textOf = runs => runs.map(run => run.text).join('');
  const diagramIds=new WeakMap(),diagramRenders=new Map();
  let diagramSequence=0,lastScreenshotAt=0;
  async function tiledVisual(node,runtime) {
    const positions=[];
    for(let parent=node.parentElement;parent;parent=parent.parentElement)positions.push([parent,parent.scrollLeft,parent.scrollTop]);
    const originalX=scrollX,originalY=scrollY;
    const controls=[...document.querySelectorAll('[data-pearls-toolbar]')].map(el=>[el,el.style.visibility]);
    const initial=node.getBoundingClientRect(),canvas=document.createElement('canvas');
    if(initial.width*initial.height>16000000)return null;
    const nextFrame=()=>new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve)));
    let scale=0;
    function visible(){
      const rect=node.getBoundingClientRect();
      const clip={left:Math.max(0,rect.left),top:Math.max(90,rect.top),right:Math.min(innerWidth,rect.right),bottom:Math.min(innerHeight-8,rect.bottom)};
      for(const [parent]of positions){const css=getComputedStyle(parent),r=parent.getBoundingClientRect();if(/auto|scroll|hidden|clip/.test(css.overflowX)){clip.left=Math.max(clip.left,r.left);clip.right=Math.min(clip.right,r.right);}if(/auto|scroll|hidden|clip/.test(css.overflowY)){clip.top=Math.max(clip.top,r.top);clip.bottom=Math.min(clip.bottom,r.bottom);}}
      return {rect,clip};
    }
    try{
      for(const [el]of controls)el.style.visibility='hidden';
      let y=0,tiles=0;
      while(y<initial.height-1){
        let x=0,rowBottom=Infinity;
        while(x<initial.width-1){
          if(++tiles>80)throw Error('Diagram exceeds the screenshot tile limit');
          node.scrollIntoView({block:'start',inline:'start',behavior:'instant'});
          for(const [parent]of positions){const css=getComputedStyle(parent),r=parent.getBoundingClientRect(),n=node.getBoundingClientRect();if(/auto|scroll/.test(css.overflowY))parent.scrollTop+=n.top+y-Math.max(100,r.top+8);if(/auto|scroll/.test(css.overflowX))parent.scrollLeft+=n.left+x-Math.max(8,r.left+8);}
          let n=node.getBoundingClientRect();scrollTo({left:scrollX+n.left+x-8,top:scrollY+n.top+y-100,behavior:'instant'});
          await nextFrame();
          const {rect,clip}=visible();
          const left=Math.max(x,clip.left-rect.left),top=Math.max(y,clip.top-rect.top),right=Math.min(initial.width,clip.right-rect.left),bottom=Math.min(initial.height,clip.bottom-rect.top);
          if(left>x+1||top>y+1||right<=x+1||bottom<=y+1)return null;
          // Chrome permits at most two visible-tab captures per second.
          await sleep(Math.max(0,550-(Date.now()-lastScreenshotAt)));
          const response=await runtime.sendMessage({type:'PEARLS_CROP_VISUAL',rect:{x:rect.left+left,y:rect.top+top,width:right-left,height:bottom-top},viewport:{width:innerWidth,height:innerHeight}});lastScreenshotAt=Date.now();
          if(!response?.data?.startsWith('data:image/png;base64,'))throw Error(response?.error||'Screenshot unavailable');
          const bitmap=await createImageBitmap(await(await fetch(response.data)).blob());
          try{const sx=bitmap.width/innerWidth,sy=bitmap.height/innerHeight;if(!scale){scale=sx;canvas.width=Math.round(initial.width*scale);canvas.height=Math.round(initial.height*scale);}canvas.getContext('2d').drawImage(bitmap,(rect.left+left)*sx,(rect.top+top)*sy,(right-left)*sx,(bottom-top)*sy,left*scale,top*scale,(right-left)*scale,(bottom-top)*scale);}finally{bitmap.close();}
          rowBottom=Math.min(rowBottom,bottom);x=right;
        }
        y=rowBottom;
      }
      return {data:canvas.toDataURL('image/png'),width:initial.width,height:initial.height};
    }finally{for(const [parent,x,y]of positions){parent.scrollLeft=x;parent.scrollTop=y;}scrollTo({left:originalX,top:originalY,behavior:'instant'});for(const [el,value]of controls)el.style.visibility=value;}
  }
  async function firefoxCrop(node) {
    const runtime=(globalThis.browser||globalThis.chrome)?.runtime;
    if(!runtime?.sendMessage||!node?.isConnected)return null;
    const initial=node.getBoundingClientRect();
    // Taller/wider diagrams need the full-element renderer instead of a clipped viewport.
    if(initial.width>innerWidth-16||initial.height>innerHeight-110)return tiledVisual(node,runtime);
    const positions=[];
    for(let parent=node.parentElement;parent;parent=parent.parentElement)positions.push([parent,parent.scrollLeft,parent.scrollTop]);
    const originalX=scrollX,originalY=scrollY;
    const controls=[...document.querySelectorAll('[data-pearls-toolbar]')].map(el=>[el,el.style.getPropertyValue('visibility'),el.style.getPropertyPriority('visibility')]);
    try {
      node.scrollIntoView({block:'center',inline:'nearest',behavior:'instant'});
      for(const [el]of controls)el.style.setProperty('visibility','hidden','important');
      await new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve)));
      const rect=node.getBoundingClientRect();
      if(rect.left<0||rect.top<0||rect.right>innerWidth||rect.bottom>innerHeight)return tiledVisual(node,runtime);
      // Ancestor scroll panes can clip an otherwise viewport-sized diagram.
      for(const [parent]of positions){const css=getComputedStyle(parent),r=parent.getBoundingClientRect();if(/auto|scroll|hidden|clip/.test(css.overflowX+' '+css.overflowY)&&(rect.left<r.left||rect.right>r.right||rect.top<r.top||rect.bottom>r.bottom))return tiledVisual(node,runtime);}
      await sleep(Math.max(0,550-(Date.now()-lastScreenshotAt)));
      const response=await runtime.sendMessage({type:'PEARLS_CROP_VISUAL',rect:{x:rect.left,y:rect.top,width:rect.width,height:rect.height},viewport:{width:innerWidth,height:innerHeight}});
      lastScreenshotAt=Date.now();
      if(!response?.data?.startsWith('data:image/png;base64,'))throw Error(response?.error||'Firefox did not return screenshot data');
      const bitmap=await createImageBitmap(await (await fetch(response.data)).blob());
      try{
        const scaleX=bitmap.width/innerWidth,scaleY=bitmap.height/innerHeight;
        const x=Math.round(rect.left*scaleX),y=Math.round(rect.top*scaleY);
        const width=Math.min(bitmap.width-x,Math.round(rect.width*scaleX)),height=Math.min(bitmap.height-y,Math.round(rect.height*scaleY));
        if(width<1||height<1)throw Error('The screenshot crop is outside the viewport');
        const canvas=document.createElement('canvas');canvas.width=width;canvas.height=height;
        canvas.getContext('2d').drawImage(bitmap,x,y,width,height,0,0,width,height);
        return {data:canvas.toDataURL('image/png'),width:rect.width,height:rect.height};
      }finally{bitmap.close();}
    }
    finally{
      for(const [el,value,priority]of controls){if(value)el.style.setProperty('visibility',value,priority);else el.style.removeProperty('visibility');}
      for(const [parent,x,y]of positions){parent.scrollLeft=x;parent.scrollTop=y;}
      scrollTo({left:originalX,top:originalY,behavior:'instant'});
    }
  }
  async function renderDiagram(node){
    let nativeError='';
    const runtime=(globalThis.browser||globalThis.chrome)?.runtime;
    if(runtime){
      const attribute='data-pearls-render-key',previous=node.getAttribute(attribute);
      try{
        const key='pearls-'+crypto.randomUUID();
        node.setAttribute(attribute,key);
        const response=await runtime.sendMessage({type:'PEARLS_RENDER_DIAGRAM',key});
        if(!response?.data)throw Error(response?.error||'Page renderer returned no image');
        return response;
      }catch(error){nativeError+=(nativeError?'; ':'')+error.message;}
      finally{if(previous===null)node.removeAttribute(attribute);else node.setAttribute(attribute,previous);}
    }
    if(node.matches('svg')){
      const clone=node.cloneNode(true),originals=[node,...node.querySelectorAll('*')],copies=[clone,...clone.querySelectorAll('*')];
      const properties=['fill','stroke','stroke-width','color','font-family','font-size','font-style','font-weight','text-anchor','dominant-baseline','letter-spacing','visibility'];
      for(let i=0;i<originals.length;i++){const css=getComputedStyle(originals[i]);for(const property of properties)copies[i].style.setProperty(property,css.getPropertyValue(property));}
      for(const script of clone.querySelectorAll('script'))script.remove();
      const rect=node.getBoundingClientRect();clone.setAttribute('xmlns','http://www.w3.org/2000/svg');clone.setAttribute('width',rect.width);clone.setAttribute('height',rect.height);
      const img=new Image();img.src='data:image/svg+xml;charset=utf-8,'+encodeURIComponent(new XMLSerializer().serializeToString(clone));await img.decode();
      const canvas=document.createElement('canvas');canvas.width=Math.round(rect.width*4);canvas.height=Math.round(rect.height*4);const ctx=canvas.getContext('2d');ctx.fillStyle='#ffffff';ctx.fillRect(0,0,canvas.width,canvas.height);ctx.drawImage(img,0,0,canvas.width,canvas.height);
      return {data:canvas.toDataURL('image/png'),width:canvas.width,height:canvas.height};
    }
    if(!globalThis.html2canvas){const crop=await firefoxCrop(node);if(crop)return crop;return null;}
    try{
      const canvas=await globalThis.html2canvas(node,{backgroundColor:'#ffffff',scale:Math.min(4,Math.sqrt(32000000/Math.max(1,node.getBoundingClientRect().width*node.getBoundingClientRect().height))),logging:false,useCORS:true,onclone:normalizeDiagramColors,ignoreElements:el=>el.matches('[data-pearls-ignore],button')});
      return {data:canvas.toDataURL('image/png'),width:canvas.width,height:canvas.height};
    }catch(error){try{const crop=await firefoxCrop(node);if(crop)return crop;}catch(cropError){nativeError+='; '+cropError.message;}throw Error((nativeError?'Firefox screenshot: '+nativeError+'; ':'')+'diagram renderer: '+error.message);}
  }
  function normalizeDiagramColors(doc) {
    const canvas=doc.createElement('canvas');canvas.width=canvas.height=1;
    const ctx=canvas.getContext('2d',{willReadFrequently:true});
    const modern=/(?:oklch|oklab|lch|lab|color)\(/i;
    for(const el of doc.querySelectorAll('*')){
      const css=doc.defaultView.getComputedStyle(el);
      for(const property of ['color','background-color','border-top-color','border-right-color','border-bottom-color','border-left-color','outline-color','text-decoration-color']){
        const value=css.getPropertyValue(property);
        if(!modern.test(value))continue;
        ctx.clearRect(0,0,1,1);ctx.fillStyle=value;ctx.fillRect(0,0,1,1);
        const [r,g,b,a]=ctx.getImageData(0,0,1,1).data;
        el.style.setProperty(property,`rgba(${r},${g},${b},${a/255})`,'important');
      }
      for(const property of ['box-shadow','text-shadow'])if(modern.test(css.getPropertyValue(property)))el.style.setProperty(property,'none','important');
    }
  }
  function isDiagram(node) {
    if(!node.matches('div,section,figure,[role="img"]'))return false;
    const explicit=node.matches('[role="img"],[data-diagram],[data-testid*="diagram"],[data-d-component*="diagram"],[data-d-component*="chart"],[data-d-component*="flow"],[data-d-component*="smart"],[data-d-component*="punnett"],.mermaid,.flowchart,.smartart');
    if(!explicit&&node.querySelector('table,ul,ol,pre'))return false;
    // Photo galleries and their loading skeletons are not SmartArt diagrams.
    const pictures = [...node.querySelectorAll('img')];
    if((!explicit&&(node.querySelector('picture')||pictures.some(img=>!arrowGlyph(img))))||(!node.textContent.trim()&&!node.querySelector('svg,canvas,img')))return false;
    const rect=node.getBoundingClientRect();
    if(rect.width<100||rect.height<60||node.textContent.length>4500)return false;
    if(explicit)return true;
    const style=getComputedStyle(node);
    const cards=[...node.querySelectorAll('div,section')].filter(el=>{const css=getComputedStyle(el),r=el.getBoundingClientRect();return r.width>60&&r.height>24&&el.textContent.trim()&&(parseFloat(css.borderTopWidth)>0||(!['transparent','rgba(0, 0, 0, 0)'].includes(css.backgroundColor)));});
    const arrows=/[↓↑→←↘↙⇓⇒⟶]/.test(node.textContent)||pictures.some(arrowGlyph)||!!node.querySelector('svg path,svg line,svg polygon');
    if(arrows&&cards.length>=2&&node.children.length<=14&&!node.querySelector('h1,h2')&&!node.matches('.markdown,.prose,[data-message-author-role]'))return true;
    if([...node.querySelectorAll('h1,h2,h3,h4')].some(el=>!/^\s*\d+(?:\.\d+)?\s*%\s*$/.test(el.textContent)))return false;
    const grid=[node,...node.querySelectorAll('div')].find(el=>{
      const css=getComputedStyle(el);
      const grid=/^(inline-)?grid$/.test(css.display)&&el.children.length>=2&&css.gridTemplateColumns.split(' ').length>=2;
      const flex=/^(inline-)?flex$/.test(css.display)&&el.children.length>=2
        && [...el.children].filter(child=>/%/.test(child.textContent)&&child.textContent.trim().length<150).length>=2;
      return grid||flex;
    });
    if(!grid)return false;
    // Prefer the complete diagram wrapper, including legend/outcome cards.
    // Many SmartArt wrappers have no visible border, unlike the inner grid.
    if(grid===node || (parseFloat(style.borderRadius)>0&&parseFloat(style.borderTopWidth)>0))return true;
    const branch=[...node.children].find(child=>child===grid||child.contains(grid));
    const siblings=[...node.children].filter(child=>child!==branch&&!hidden(child));
    return siblings.length>0 && siblings.every(child=>child.textContent.trim().length<=450)
      && ![...node.querySelectorAll('p')].some(p=>p.textContent.trim().length>140)
      && siblings.some(child=>/%/.test(child.textContent)||/legend|outcome|unaffected|carrier|affected/i.test(child.textContent));
  }
  function diagram(node) {
    let id=diagramIds.get(node);
    if(!id){
      id='diagram-'+(++diagramSequence);diagramIds.set(node,id);
      // Scanning must remain read-only: clone/rasterize only during export.
      diagramRenders.set(id,{node});
    }
    const rect=node.getBoundingClientRect();
    return {type:'image',diagramId:id,alt:node.getAttribute('aria-label')||'Diagram: '+node.textContent.trim().replace(/\s+/g,' ').slice(0,160),width:rect.width,height:rect.height};
  }
  function branchingFlowcharts(parent) {
    const groups = new Map();
    const children = [...parent.childNodes].filter(node => node.nodeType === Node.ELEMENT_NODE ? !node.matches('br,[data-pearls-ignore]') : node.textContent.trim());
    const element = node => node?.nodeType === Node.ELEMENT_NODE;
    const step = node => element(node) && node.textContent.trim().length > 0 && node.textContent.trim().length <= 240
      && !node.querySelector('img,svg,canvas,table,ul,ol,pre') && !arrowText(node.textContent);
    const arrow = node => {
      if (!element(node)) return false;
      if (arrowText(node.textContent)) return true;
      const icon = node.matches('img,svg') ? node : node.querySelector('img,svg');
      if (!icon || node.textContent.trim()) return false;
      const { width, height } = icon.getBoundingClientRect();
      return !!arrowGlyph(icon) || (width >= 8 && height >= 8 && width <= 80 && height <= 80 && width / height >= 0.5 && width / height <= 2);
    };
    const lanes = node => element(node) && [node, ...node.querySelectorAll('div,section,figure,td,tr')].some(row => {
      const cards = [...row.children].filter(child => child.textContent.trim()).map(child => child.getBoundingClientRect())
        .filter(rect => rect.width >= 60 && rect.height >= 16);
      return cards.length >= 2 && cards.length <= 5 && cards.some((a, index) => cards.slice(index + 1).some(b =>
        Math.abs(a.top - b.top) <= 12 && (a.right <= b.left + 2 || b.right <= a.left + 2)));
    });
    const fork = node => {
      if (!element(node)) return false;
      const visuals = node.matches('svg,img,canvas') ? [node] : [...node.querySelectorAll('svg,img,canvas')];
      if (visuals.some(visual => {
        const { width, height } = visual.getBoundingClientRect();
        return width >= 85 && height > 0 && height <= 100 && width >= height * 2.5
          && (visual.matches('svg') ? !!visual.querySelector('path,line,polyline,polygon') : height <= 65);
      })) return true;
      return [node, ...node.querySelectorAll('div,span')].some(line => {
        if (line.textContent.trim()) return false;
        const { width, height } = line.getBoundingClientRect();
        const style = getComputedStyle(line);
        return width >= 100 && height <= 50 && width >= height * 2
          && ((parseFloat(style.borderTopWidth) > 0 && (parseFloat(style.borderLeftWidth) > 0 || parseFloat(style.borderRightWidth) > 0))
            || (height <= 4 && !['transparent', 'rgba(0, 0, 0, 0)'].includes(style.backgroundColor)));
      });
    };
    for (let index = 0; index < children.length; index++) {
      if (!element(children[index])) continue;
      const layout = children[index];
      const splitBranch = fork(layout) && lanes(children[index + 1]);
      const wrappedBranch = lanes(layout) && [...layout.children].some(child => fork(child) && !lanes(child));
      if (!splitBranch && !wrappedBranch) continue;
      const hasLabel = splitBranch && !!layout.textContent.trim();
      if (!hasLabel && !step(children[index - 1])) continue;
      let start = hasLabel ? index : index - 1, end = index + Number(splitBranch);
      while (step(children[start - 2]) && arrow(children[start - 1])) start -= 2;
      while (arrow(children[end + 1]) && step(children[end + 2])) end += 2;
      const nodes = children.slice(start, end + 1);
      groups.set(nodes[0], nodes);
      index = end;
    }
    return groups;
  }
  async function renderDiagramGroup(nodes) {
    const parent = nodes[0].parentElement;
    if (!parent || nodes.some(node => node.parentElement !== parent)) return null;
    const wrapper = document.createElement('div');
    const css = getComputedStyle(parent);
    const layout = ['display', 'flex-direction', 'align-items', 'justify-items', 'grid-template-columns', 'gap'];
    for (const property of layout) wrapper.style.setProperty(property, css.getPropertyValue(property));
    const clones = nodes.map(node => node.cloneNode(true));
    nodes.forEach((node, index) => {
      const canvases = node.matches('canvas') ? [node] : [...node.querySelectorAll('canvas')];
      const clone = clones[index];
      const copies = clone.matches('canvas') ? [clone] : [...clone.querySelectorAll('canvas')];
      canvases.forEach((canvas, position) => {
        if (canvas.width && canvas.height) copies[position].getContext('2d')?.drawImage(canvas, 0, 0);
      });
    });
    wrapper.append(...clones);
    nodes.at(-1).after(wrapper);
    try {
      await Promise.allSettled([...wrapper.querySelectorAll('img')].map(img => {
        img.loading = 'eager';
        return img.decode();
      }));
      try {
        const screenshot = await firefoxCrop(wrapper);
        if (screenshot) return screenshot;
      } catch { /* Fall back to the whole-element renderer. */ }
      return await renderDiagram(wrapper);
    } finally {
      wrapper.remove();
    }
  }
  function imagePlaceholder(node){
    if(!node.matches('div,section,figure')||node.textContent.trim()||node.querySelector('img,picture,svg,canvas,table'))return false;
    const css=getComputedStyle(node),children=[...node.children];
    return /grid|flex/.test(css.display)&&children.length>=2&&children.length<=8&&children.every(child=>{
      const r=child.getBoundingClientRect(),s=getComputedStyle(child);
      return r.width>=70&&r.height>=70&&(parseFloat(s.borderRadius)>0||s.backgroundColor!=='rgba(0, 0, 0, 0)');
    });
  }
  async function prepareVisuals(index=null){
    let targets=entries(site());
    if(index!==null)targets=targets.filter(entry=>entry.role==='assistant').slice(Number(index),Number(index)+1);
    const positions=new Map(),originalX=scrollX,originalY=scrollY,deadline=Date.now()+18000;
    const remember=node=>{for(let p=node.parentElement;p;p=p.parentElement)if(!positions.has(p))positions.set(p,[p.scrollLeft,p.scrollTop]);};
    async function reveal(node){
      remember(node);node.scrollIntoView({block:'center',inline:'nearest',behavior:'instant'});
      await new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve)));
      await sleep(100);
    }
    try{
      for(const entry of targets){
        const galleries=[...entry.node.querySelectorAll('div,section,figure')].filter(imagePlaceholder);
        for(const gallery of galleries){
          if(Date.now()>=deadline)break;
          await reveal(gallery);
          while(gallery.isConnected&&imagePlaceholder(gallery)&&Date.now()<deadline)await sleep(120);
        }
        for(const img of entry.node.querySelectorAll('img')){
          if(Date.now()>=deadline)break;
          if(/\/s2\/favicons|\/favicon/i.test(img.currentSrc||img.src))continue;
          await reveal(img);
          while(!img.complete&&Date.now()<deadline)await sleep(120);
        }
      }
    }finally{
      for(const [node,[x,y]]of positions){node.scrollLeft=x;node.scrollTop=y;}
      scrollTo({left:originalX,top:originalY,behavior:'instant'});
    }
  }
  function blocks(parent) {
    const output = [];
    const groups = branchingFlowcharts(parent);
    const grouped = new Set();
    let pending = [];
    function flush() {
      if (textOf(pending).trim()) output.push({ type: 'paragraph', runs: pending });
      pending = [];
    }
    for (const node of parent.childNodes) {
      if (grouped.has(node)) continue;
      const group = groups.get(node);
      if (group) {
        flush();
        group.forEach(member => grouped.add(member));
        const item = diagram(node);
        diagramRenders.set(item.diagramId, { nodes: group });
        output.push({ ...item, fullHeight: true, alt: group.map(member => member.textContent.trim()).filter(Boolean).join(' ') });
        continue;
      }
      if (node.nodeType === Node.TEXT_NODE) { if (node.textContent.trim()) pending.push(...inlines(node)); continue; }
      if (node.nodeType !== Node.ELEMENT_NODE) continue;
      // Generated pictures are often wrapped in a preview button/link.
      if (node.matches('button,[role="button"]') && !node.closest('[data-pearls-ignore],[hidden],[aria-hidden="true"]')) {
        flush();
        for (const img of node.querySelectorAll('img')) if (!hidden(img)) {
          const arrow = arrowGlyph(img);
          output.push(arrow ? { type: 'paragraph', runs: [{ text: arrow }] } : image(img));
        }
        continue;
      }
      if (hidden(node)) continue;
      const tag = node.tagName.toLowerCase();
      if(imagePlaceholder(node)){flush();output.push({type:'image',pending:true,alt:'Image gallery is still loading'});continue;}
      if(isDiagram(node)){flush();output.push(diagram(node));continue;}
      if (/^h[1-6]$/.test(tag)) { flush(); output.push({ type: 'heading', level: Number(tag[1]), runs: inlines(node) }); }
      else if (tag === 'p') {
        flush();
        const pictures = [...node.querySelectorAll(node.textContent.trim() ? 'img' : 'img,svg')].filter(img => !arrowGlyph(img));
        if (pictures.length && !node.textContent.trim() && ![...node.querySelectorAll('img,svg')].some(arrowGlyph)) {
          for (const img of pictures) output.push(img.matches('svg') ? diagram(img) : image(img));
          continue;
        }
        const runs = inlines(node);
        const words = runs.filter(run => run.text.trim());
        const text = textOf(runs).trim();
        const heading = !node.closest('li') && words.length && words.every(run => run.bold) && text.length < 100 && text.split(/\s+/).length <= 12 && !/[.!?;:]$/.test(text);
        if (text) output.push({ type: heading ? 'heading' : 'paragraph', ...(heading ? { level: 6, inferred: true } : {}), runs });
        // Inline image positions are preserved as image paragraphs after the caption text.
        for (const img of pictures) output.push(img.matches('svg') ? diagram(img) : image(img));
      }
      else if (tag === 'ul' || tag === 'ol') {
        flush();
        output.push({ type: 'list', ordered: tag === 'ol', start: Number(node.getAttribute('start')) || 1,
          format: node.getAttribute('type') || '1', items: [...node.children].filter(child => child.tagName === 'LI').map(li => ({ value: li.hasAttribute('value') ? Number(li.getAttribute('value')) : null, blocks: blocks(li) })) });
      }
      else if (tag === 'table') {
        flush();
        output.push({ type: 'table', rows: [...node.rows].map(row => ({ cells: [...row.cells].map(cell => ({ header: cell.tagName === 'TH', colspan: cell.colSpan || 1, rowspan: cell.rowSpan || 1, blocks: blocks(cell) })) })) });
      }
      else if (tag === 'pre') { flush(); output.push({ type: 'code', text: clean((node.querySelector('code') || node).textContent) }); }
      else if (tag === 'blockquote') { flush(); output.push({ type: 'quote', blocks: blocks(node) }); }
      else if ((tag === 'img' || tag === 'svg') && arrowGlyph(node)) pending.push(...inlines(node));
      else if (tag === 'img') { flush(); output.push(image(node)); }
      else if (tag === 'canvas') {
        flush();try{output.push({type:'image',data:node.toDataURL('image/png'),alt:node.getAttribute('aria-label')||'Diagram',width:node.width,height:node.height});}
        catch{output.push({type:'image',alt:'Diagram could not be read'});}
      }
      else if (tag === 'svg') {
        flush();
        output.push(diagram(node));
      }
      else if (tag === 'hr') { flush(); output.push({ type: 'rule' }); }
      else if (/^(div|section|article|main|figure|figcaption|details|summary|dl|dt|dd|li)$/.test(tag)) { flush(); output.push(...blocks(node)); }
      else if ([...node.querySelectorAll('img')].some(img => !arrowGlyph(img))) { flush(); output.push(...blocks(node)); }
      else pending.push(...inlines(node));
    }
    flush(); return output;
  }
  function image(img) {
    let elementId=diagramIds.get(img);
    if(!elementId){elementId='picture-'+(++diagramSequence);diagramIds.set(img,elementId);diagramRenders.set(elementId,{node:img});}
    const lazy=img.getAttribute('data-src')||img.getAttribute('data-original');
    const src=/^data:/i.test(img.currentSrc||img.src)&&/^https?:/i.test(lazy||'')?lazy:img.currentSrc||img.src;
    return { type: 'image',elementId, src, alt: img.alt || 'Image', width: img.naturalWidth || img.width || 640, height: img.naturalHeight || img.height || 480 };
  }
  function renderFlowchart(rows) {
    const canvas = document.createElement('canvas');
    const context = canvas.getContext('2d');
    const font = '20px Arial, sans-serif';
    context.font = font;
    const width = Math.min(660, Math.max(180, ...rows.map(row => context.measureText(row).width + 48)));
    const lines = rows.flatMap(row => {
      const arrow = arrowText(row);
      if (arrow) return [{ text: arrow, arrow: true }];
      const wrapped = [];
      let line = '';
      for (const word of row.split(/\s+/)) {
        const next = line ? `${line} ${word}` : word;
        if (line && context.measureText(next).width > width - 48) {
          wrapped.push({ text: line });
          line = word;
        } else line = next;
      }
      wrapped.push({ text: line });
      return wrapped;
    });
    const height = 32 + lines.reduce((sum, line) => sum + (line.arrow ? 36 : 28), 0);
    const scale = Math.min(3, 8192 / height);
    canvas.width = Math.ceil(width * scale);
    canvas.height = Math.ceil(height * scale);
    context.scale(scale, scale);
    context.fillStyle = '#ffffff';
    context.fillRect(0, 0, width, height);
    context.fillStyle = '#17212e';
    context.textAlign = 'center';
    context.textBaseline = 'middle';
    let y = 16;
    for (const line of lines) {
      const lineHeight = line.arrow ? 36 : 28;
      context.font = line.arrow ? '28px Arial, sans-serif' : font;
      context.fillText(line.text, width / 2, y + lineHeight / 2, width - 48);
      y += lineHeight;
    }
    return { data: canvas.toDataURL('image/png'), width, height };
  }
  function combineFlowcharts(items) {
    const label = block => block?.runs ? textOf(block.runs).trim() : '';
    const isStep = text => text && !arrowText(text) && text.length <= 240 && !text.includes('\n');
    const imageBlock = rows => ({ type: 'image', flowchart: rows, alt: rows.join(' ') });
    const iconSignature = block => {
      const entry = diagramRenders.get(block?.diagramId || block?.elementId);
      const node = entry?.node;
      if (!node?.matches('img,svg') || node.getAttribute('alt') || node.getAttribute('aria-label') || node.textContent.trim()) return '';
      const { width, height } = node.getBoundingClientRect();
      if (width < 8 || height < 8 || width > 64 || height > 64 || width / height < 0.5 || width / height > 2) return '';
      return node.matches('img') ? block.src || '' : node.innerHTML;
    };
    const output = [];
    for (let index = 0; index < items.length;) {
      const first = label(items[index]);
      const lines = first.split(/\n/).map(line => line.trim()).filter(Boolean);
      if (lines.length >= 3 && lines.length % 2 === 1 && lines.every((line, position) => position % 2 ? arrowText(line) : isStep(line))) {
        output.push(imageBlock(lines));
        index++;
        continue;
      }
      let end = index;
      let repeatedIcon = '';
      let inferredArrows = 0;
      if (isStep(first)) {
        while (isStep(label(items[end + 2]))) {
          const connector = items[end + 1];
          if (!arrowText(label(connector))) {
            const signature = iconSignature(connector);
            if (!signature || (repeatedIcon && signature !== repeatedIcon)) break;
            repeatedIcon = signature;
            inferredArrows++;
          }
          end += 2;
        }
      }
      if (inferredArrows === 1) {
        end = index;
        while (arrowText(label(items[end + 1])) && isStep(label(items[end + 2]))) end += 2;
      }
      if (end > index) output.push(imageBlock(items.slice(index, end + 1).map((item, offset) => offset % 2 ? arrowText(label(item)) || '↓' : label(item))));
      else output.push(items[index]);
      index = end + 1;
    }
    return output;
  }
  function contentImages(items) {
    return items.filter(item => {
      if (item.type === 'image' && /(?:\/s2\/favicons|\/favicon(?:V2)?(?:[?.\/]|$))/i.test(item.src || '')) return false;
      if(item.blocks)item.blocks=contentImages(item.blocks);
      for(const entry of item.items||[])entry.blocks=contentImages(entry.blocks);
      for(const row of item.rows||[])for(const cell of row.cells)cell.blocks=contentImages(cell.blocks);
      return true;
    });
  }
  function entries(provider) {
    let candidates = [];
    if (provider === 'chatgpt') {
      // ChatGPT's newer Work UI uses search units and response-body attributes
      // instead of data-message-author-role. Support both DOM generations.
      const selector='[data-message-author-role="user"],[data-message-author-role="assistant"],[data-chatgpt-search-unit-key],[data-response-body],[data-markdown-text-style="assistant-message"],[data-turn="user"],[data-turn="assistant"]';
      candidates = [...document.querySelectorAll(selector)].map(node => {
        const key=node.getAttribute('data-chatgpt-search-unit-key')||'';
        const role=node.getAttribute('data-message-author-role') || node.getAttribute('data-turn') || /:(user|assistant)$/.exec(key)?.[1] || (node.matches('[data-response-body],[data-markdown-text-style="assistant-message"]')?'assistant':null);
        const root=node.querySelector('[data-response-body],[data-markdown-text-style="assistant-message"],.markdown,.prose,[class*="whitespace-pre-wrap"]')||node;
        return {node,role,root,id:node.getAttribute('data-message-id')||root.getAttribute('data-response-body')||node.getAttribute('data-response-body')||node.getAttribute('data-chatgpt-search-message-ids')?.trim().split(/\s+/)[0]||node.closest('[data-message-id]')?.getAttribute('data-message-id')||key||node.closest('article[data-testid]')?.getAttribute('data-testid')};
      }).filter(entry=>entry.role==='user'||entry.role==='assistant');
    } else if (provider === 'claude') {
      candidates = [...document.querySelectorAll('[data-testid="user-message"],[data-testid="assistant-message"],.font-claude-response')].map(node => ({
        node, root: node.querySelector('.standard-markdown,.markdown,.prose') || node,
        role: node.matches('[data-testid="user-message"]') ? 'user' : 'assistant',
        id: node.closest('[data-message-id]')?.getAttribute('data-message-id') || node.getAttribute('data-message-id')
      }));
    } else if (provider === 'gemini') {
      candidates = [...document.querySelectorAll('user-query,model-response')].map(node => ({
        node, root: node.querySelector('.model-response-text,.query-text,.markdown') || node,
        role: node.tagName.toLowerCase() === 'user-query' ? 'user' : 'assistant',
        id: node.getAttribute('data-message-id') || node.getAttribute('id')
      }));
    }
    // Retain only outermost message candidates; nested adapter matches are duplicates.
    return candidates.filter(item => !candidates.some(other => other !== item && other.node.contains(item.node))).filter(item => !item.node.closest('[hidden],[aria-hidden="true"]'));
  }
  function isStreaming(provider) {
    const selectors = {
      chatgpt: '[data-testid="stop-button"],button[aria-label="Stop generating"]',
      claude: '[data-is-streaming="true"],button[aria-label="Stop response"],button[aria-label="Stop generating"]',
      gemini: 'button[aria-label="Stop response"],button[aria-label="Stop generating"],.stop-button:not([hidden])'
    };
    return [...document.querySelectorAll(selectors[provider])].some(node => node.getClientRects().length && !node.closest('[hidden],[aria-hidden="true"]'));
  }
  function snapshot(provider = site()) {
    if (isStreaming(provider)) throw Error('The response is still being generated. Wait for it to finish, then refresh.');
    const messages = entries(provider).map((entry, index) => ({
      id: entry.id || null, role: entry.role, blocks: responseBlocks(entry.node),
      preview: entry.root.innerText?.trim().slice(0, 240) || entry.root.textContent.trim().slice(0, 240), index
    })).filter(message => message.blocks.length);
    if (!messages.length) throw Error('No chat messages were found. Open a conversation and let it finish loading. The site may also have changed its page layout.');
    const warnings = entries(provider).some(entry => entry.root.querySelector('video,iframe')) ? ['This response contains video or an embedded frame. Its interactive content is not included in the Word file.'] : [];
    return { provider, title: document.title.replace(/\s*[-–|]\s*(ChatGPT|Claude|Gemini).*$/i, '').trim(), url: location.href, messages, warnings };
  }
  function responseBlocks(node) {
    return contentImages(combineFlowcharts(blocks(node)));
  }
  function scroller(provider) {
    const first = entries(provider)[0]?.node;
    for (let node = first?.parentElement; node; node = node.parentElement) {
      const style = getComputedStyle(node);
      if (/(auto|scroll)/.test(style.overflowY) && node.scrollHeight > node.clientHeight + 80) return node;
    }
    return document.scrollingElement;
  }
  const messageKey = message => message.id ? message.role + ':' + message.id : message.role + ':' + JSON.stringify(message.blocks, (key, value) => {
    if (value?.flowchart) return { type: value.type, flowchart: value.flowchart };
    return value;
  });
  // Sequence overlap, rather than a Set of text, preserves repeated identical turns.
  function merge(left, right) {
    if (!left.length) return right.slice();
    if (!right.length) return left;
    const a = left.map(messageKey), b = right.map(messageKey);
    const contained = a.findIndex((_, index) => b.every((key, j) => a[index + j] === key));
    if (contained >= 0) return left;
    let overlap = Math.min(a.length, b.length);
    while (overlap > 0 && !a.slice(-overlap).every((key, j) => key === b[j])) overlap--;
    if (!overlap) {
      // Without an overlapping turn we cannot prove chronology for a virtualized page.
      throw Error('The page replaced its messages while scrolling. Export stopped to avoid an incomplete chat. Zoom out or expand the conversation history, then retry.');
    }
    return left.concat(right.slice(overlap));
  }
  async function conversation(onProgress = () => {}) {
    const provider = site(), container = scroller(provider), originalTop = container.scrollTop;
    let collected = [], topReached = false, bottomReached = false;
    try {
      // Let the site's own history loading run; no hidden endpoints or credentials.
      for (let i = 0; i < 100; i++) {
        container.scrollTop = 0;
        await sleep(350);
        const before = JSON.stringify(snapshot(provider).messages.map(messageKey));
        await sleep(400);
        const after = JSON.stringify(snapshot(provider).messages.map(messageKey));
        if (container.scrollTop <= 2 && before === after && i >= 2) { topReached = true; break; }
      }
      if (!topReached) throw Error('The start of the chat could not be reached. Expand earlier messages in the chat and retry.');
      let result;
      for (let i = 0; i < 250; i++) {
        await prepareVisuals();
        result = await resolveImages(snapshot(provider),true);
        collected = merge(collected, result.messages);
        onProgress({messages:collected.length});
        if (JSON.stringify(collected).length > 18000000) throw Error('This chat is too large for one export. Export individual responses instead.');
        const atBottom = container.scrollTop + container.clientHeight >= container.scrollHeight - 5;
        if (atBottom) {
          await sleep(600);
          const final = await resolveImages(snapshot(provider),true);
          collected = merge(collected, final.messages);
          if (container.scrollTop + container.clientHeight >= container.scrollHeight - 5) { bottomReached = true; break; }
        }
        container.scrollTop += Math.max(200, container.clientHeight * 0.6);
        await sleep(220);
      }
      if (!bottomReached) throw Error('The full chat could not be traversed. Export stopped instead of saving a partial conversation.');
      result.messages = collected;
      result.warnings.push('Exports the active conversation branch and history the site exposes in its page. Collapsed content, separate artifacts/canvases and alternative response branches are not included.');
      return result;
    } finally { container.scrollTop = originalTop; }
  }
  async function resolveImages(result,diagramsOnly=false) {
    const cache = new Map();
    async function walk(items) {
      for (const item of items || []) {
        if (item.type === 'image') {
          try {
            if(item.data)continue;
            if(item.flowchart){Object.assign(item,renderFlowchart(item.flowchart));continue;}
            if(diagramsOnly&&!item.diagramId)continue;
            if(item.pending)throw Error('Images are still loading in the chat. Wait for the photographs to appear, then export again.');
            if(item.diagramId){
              const entry=diagramRenders.get(item.diagramId);
              const rendered = entry?.nodes ? await renderDiagramGroup(entry.nodes) : entry ? await renderDiagram(entry.node) : null;
              if(!rendered)throw Error('Diagram rendering failed');
              Object.assign(item,rendered);continue;
            }
            if (!cache.has(item.src)) cache.set(item.src, (async () => {
              const url = new URL(item.src, location.href);
              if (!/^(https?:|data:|blob:)$/.test(url.protocol)) throw Error('Unsupported image URL');
              let blob;
              try {
                const response = await fetch(url.href, { credentials: 'same-origin', signal: AbortSignal.timeout(15000) });
                if (!response.ok) throw Error('Image unavailable');
                blob = await response.blob();
              } catch(error) {
                // Extension fetch can read provider image CDNs that deny page CORS.
                const runtime=(globalThis.browser||globalThis.chrome)?.runtime;
                if (url.protocol !== 'https:' || !runtime?.sendMessage) throw error;
                const resolved = await runtime.sendMessage({type:'PEARLS_FETCH_IMAGE',url:url.href});
                if (!resolved?.data) throw Error(resolved?.error || 'Image unavailable');
                blob = await (await fetch(resolved.data)).blob();
              }
              if (!/^image\/(png|jpeg|gif|webp|svg\+xml)/i.test(blob.type) || blob.size > 8000000) throw Error('Image format or size unsupported');
              // Chromium cannot decode SVG blobs with createImageBitmap reliably.
              let bitmap;
              if(blob.type.startsWith('image/svg+xml')){
                const src=URL.createObjectURL(blob),img=new Image();
                try{img.src=src;await img.decode();bitmap=img;}finally{URL.revokeObjectURL(src);}
              }else bitmap=await createImageBitmap(blob);
              const scale = Math.min(1, 4096 / Math.max(bitmap.width, bitmap.height));
              const canvas = document.createElement('canvas'); canvas.width = Math.max(1, Math.round(bitmap.width * scale)); canvas.height = Math.max(1, Math.round(bitmap.height * scale));
              canvas.getContext('2d').drawImage(bitmap, 0, 0, canvas.width, canvas.height); bitmap.close?.();
              return canvas.toDataURL('image/png');
            })());
            item.data = await cache.get(item.src);
          } catch(error) {
            let crop=null;
            try{crop=item.elementId?await firefoxCrop(diagramRenders.get(item.elementId)?.node):null;}catch(cropError){error=cropError;}
            if(crop)Object.assign(item,crop);
            else {item.captureError=error.message;result.warnings.push('An image could not be embedded: ' + item.alt + '. '+error.message);}
          }
        }
        if (item.blocks) await walk(item.blocks);
        for (const entry of item.items || []) await walk(entry.blocks);
        for (const row of item.rows || []) for (const cell of row.cells) await walk(cell.blocks);
      }
    }
    for (const message of result.messages) await walk(message.blocks);
    result.warnings = [...new Set(result.warnings)];
    return result;
  }
  globalThis.PearlsCapture = { version:VERSION, snapshot, conversation, resolveImages, prepareVisuals, merge, blocks, combineFlowcharts, responseBlocks,
    responseTargets: () => entries(site()).filter(entry => entry.role === 'assistant'),
    isGenerating: () => isStreaming(site())
  };
})();
