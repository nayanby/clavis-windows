"""Package only distributable Chrome extension assets, excluding tests and user data."""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
import hashlib
import json

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'chrome-extension/pearls-chat-word'
OUTPUT=ROOT/'outputs/pearls-chat-word'

def main():
    OUTPUT.mkdir(parents=True,exist_ok=True)
    # Firefox forbids document.open() on the renderer's clone iframe from an
    # extension sandbox. Bundle a private page-world renderer for that fallback.
    capture=(SOURCE/'capture.js').read_text(encoding='utf-8')
    normalize=capture[capture.index('  function normalizeDiagramColors(doc)'):capture.index('  function isDiagram(node)')]
    library=(SOURCE/'vendor/html2canvas.min.js').read_text(encoding='utf-8')
    page_renderer="""(()=>{if(globalThis.__pearlsPageRendererV1)return;
const had=Object.prototype.hasOwnProperty.call(globalThis,'html2canvas'),previous=globalThis.html2canvas;
const define=undefined,module=undefined,exports=undefined;
"""+library+"""
const renderer=globalThis.html2canvas;
if(had)globalThis.html2canvas=previous;else delete globalThis.html2canvas;
"""+normalize+"""
Object.defineProperty(globalThis,'__pearlsPageRendererV1',{configurable:true,value:async node=>{
if(node.namespaceURI==='http://www.w3.org/2000/svg'){
const clone=node.cloneNode(true),originals=[node,...node.querySelectorAll('*')],copies=[clone,...clone.querySelectorAll('*')];
const properties=['color','fill','fill-opacity','fill-rule','stroke','stroke-width','stroke-opacity','stroke-linecap','stroke-linejoin','stroke-dasharray','opacity','font-family','font-size','font-style','font-weight','text-anchor','dominant-baseline','letter-spacing','visibility'];
for(let i=0;i<originals.length;i++){const style=getComputedStyle(originals[i]);for(const property of properties)copies[i].style.setProperty(property,style.getPropertyValue(property));}
for(const script of clone.querySelectorAll('script'))script.remove();
const rect=node.getBoundingClientRect(),width=Math.max(1,rect.width),height=Math.max(1,rect.height);
clone.setAttribute('xmlns','http://www.w3.org/2000/svg');clone.setAttribute('width',width);clone.setAttribute('height',height);
const image=new Image();image.src='data:image/svg+xml;charset=utf-8,'+encodeURIComponent(new XMLSerializer().serializeToString(clone));await image.decode();
const canvas=document.createElement('canvas');canvas.width=Math.round(width*2);canvas.height=Math.round(height*2);
const context=canvas.getContext('2d');context.fillStyle='#ffffff';context.fillRect(0,0,canvas.width,canvas.height);context.drawImage(image,0,0,canvas.width,canvas.height);
return {data:canvas.toDataURL('image/png'),width:canvas.width,height:canvas.height};
}
const canvas=await renderer(node,{backgroundColor:'#ffffff',scale:2,logging:false,useCORS:true,onclone:normalizeDiagramColors,ignoreElements:el=>el.matches('[data-pearls-ignore],button')});
return {data:canvas.toDataURL('image/png'),width:canvas.width,height:canvas.height};
}});
})();
"""
    (SOURCE/'vendor/html2canvas-page.min.js').write_text(page_renderer,encoding='utf-8')
    files=['manifest.json','background.js','capture.js','page-toolbar.js','exporter.html','exporter.css','exporter.js','word-export.js','README.md','THIRD_PARTY_NOTICES.txt','artifact.md','template/base.docx','template/profile.json','vendor/jszip.min.js']
    files += ['vendor/html2canvas.min.js','vendor/html2canvas-page.min.js','vendor/html2canvas.LICENSE.txt']
    files += [f'icons/{size}.png' for size in (16,32,48,128)]
    manifest=json.loads((SOURCE/'manifest.json').read_text())
    assert manifest['manifest_version']==3
    assert '<all_urls>' not in manifest.get('host_permissions',[])
    assert not any(p in manifest['permissions'] for p in ('cookies','history','debugger','nativeMessaging'))
    assert not manifest.get('content_scripts'), 'Chat pages must remain untouched until the extension icon is clicked'
    for script in manifest.get('content_scripts',[]):
        for name in script['js']:assert name in files
    for name in files:assert (SOURCE/name).is_file(),name
    target=OUTPUT/'Pearls Chat to Word.zip'
    with ZipFile(target,'w',ZIP_DEFLATED) as z:
        for name in files:z.write(SOURCE/name,'Pearls Chat to Word/'+name)
    with ZipFile(target) as z:
        assert z.testzip() is None
        for name in files:assert z.read('Pearls Chat to Word/'+name)==(SOURCE/name).read_bytes()
    report=dict(version=manifest['version'],files=len(files),sha256=hashlib.sha256(target.read_bytes()).hexdigest(),bytes=target.stat().st_size)
    (OUTPUT/'package-report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(target)
    print(json.dumps(report))

if __name__=='__main__':main()
