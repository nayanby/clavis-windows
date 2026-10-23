"""Opt-in integration checks against the actual WebView2 window."""
import base64
import json
from pathlib import Path
import threading
import time

def verify(window,services,data):
    def js(script):
        complete=threading.Event(); values=[]
        window.evaluate_js('(async()=>{try{return {ok:true,value:await ('+script+')}}catch(e){return {ok:false,error:e.stack||String(e)}}})()',lambda value:(values.append(value),complete.set()))
        if not complete.wait(45): raise AssertionError('JavaScript operation timed out: '+script[:100])
        result=values[0]
        if not result.get('ok'): raise AssertionError(result.get('error'))
        return result.get('value')
    def wait(expression):
        for _ in range(150):
            result=window.evaluate_js(expression)
            if result: return result
            time.sleep(.1)
        raise AssertionError('Timed out: '+expression)
    def click(selector): js('document.querySelector('+json.dumps(selector)+').click()')
    def cdp(method,params):
        from System import Func,Object
        task=window.native.Invoke(Func[Object](lambda:window.native.webview.CoreWebView2.CallDevToolsProtocolMethodAsync(method,json.dumps(params))))
        return json.loads(task.GetAwaiter().GetResult())
    def picture(name):
        result=cdp('Page.captureScreenshot',{'format':'png'}); (data/(name+'.png')).write_bytes(base64.b64decode(result['data']))
    results={}
    cdp('Runtime.enable',{})
    js("(()=>{window.__errors=[];addEventListener('error',e=>__errors.push(e.message));addEventListener('unhandledrejection',e=>__errors.push(String(e.reason)));})()")
    assert js('document.querySelectorAll(".home-card").length')==7
    picture('python-home')
    from System import Func,Double
    zoom=window.native.Invoke(Func[Double](lambda:window.native.webview.ZoomFactor))
    results['native']={'zoom':zoom,'width':window.width,'height':window.height,'title':window.title}
    assert abs(results['native']['zoom']-.8)<.001
    # The same public API and native file dialog path used by the Import buttons.
    sources=[services.root/'test-output'/f for f in ('test.epub','test.pdf','test.wav')]
    if not all(p.exists() for p in sources): return {'native':results['native'],'basic':True}
    original=window.create_file_dialog; window.create_file_dialog=lambda *a,**k:tuple(str(p) for p in sources)
    try: state=js('window.clavis.importFiles("All")')
    finally: window.create_file_dialog=original
    assert len(state['books'])>=3
    js('location.reload()'); wait('document.querySelectorAll(".home-card").length===7')
    click('nav [data-route="EPUB"]'); click('[data-open]')
    wait('document.querySelector("#epub-host iframe")?.contentDocument?.body?.innerText.includes("Welcome to the Clavis")')
    click('#reader-bookmark'); picture('python-epub'); click('#reader-back')
    click('nav [data-route="PDF"]'); click('[data-open]'); wait('document.querySelector(".paper")?.width>0')
    click('#reader-bookmark'); click('#reader-next'); wait('document.querySelector("#reader-position")?.innerText.includes("Page 2")'); picture('python-pdf'); click('#reader-back')
    click('nav [data-route="Audio"]'); click('[data-open]'); wait('document.querySelector("#duration")?.innerText.includes("0:04")')
    # Real pointer events through WebView2 allow playback with a user activation.
    xy=js('(()=>{const r=document.querySelector(".transport [data-action=play]").getBoundingClientRect();return {x:r.x+r.width/2,y:r.y+r.height/2}})()')
    cdp('Input.dispatchMouseEvent',{'type':'mousePressed','button':'left','clickCount':1,**xy})
    cdp('Input.dispatchMouseEvent',{'type':'mouseReleased','button':'left','clickCount':1,**xy})
    wait('!document.querySelector("audio").paused')
    js('document.querySelector("audio").pause()')
    js('(()=>{const s=document.querySelector("#player-seek");s.value=500;s.dispatchEvent(new Event("input",{bubbles:true}));s.dispatchEvent(new Event("change",{bubbles:true}));})()')
    wait('document.querySelector("audio").currentTime>1.5')
    # Route the same WM_COMMAND notification Windows sends for thumbnail clicks.
    import ctypes
    from ctypes import wintypes
    send=ctypes.windll.user32.SendMessageW
    send.argtypes=[wintypes.HWND,wintypes.UINT,ctypes.c_size_t,ctypes.c_ssize_t]; send.restype=ctypes.c_ssize_t
    def thumb(id): send(window.native.Handle.ToInt64(),0x111,(0x1800<<16)|id,0)
    assert window._clavis_taskbar.added
    window.minimize(); time.sleep(.3)
    thumb(4101); wait('document.querySelector("audio").currentTime<.1')
    thumb(4103); wait('document.querySelector("audio").currentTime>3.9')
    thumb(4102); wait('!document.querySelector("audio").paused')
    for _ in range(30):
        if window._clavis_taskbar.previous==(True,True,30): break
        time.sleep(.05)
    assert window._clavis_taskbar.previous==(True,True,30), 'Taskbar did not change to Pause'
    thumb(4102); wait('document.querySelector("audio").paused')
    window.restore(); time.sleep(.2)
    results['taskbar']={'backward':True,'forward':True,'playPause':True,'whileMinimized':True,'pauseIcon':True}
    click('[data-action="add-audio-bookmark"]'); js('document.querySelector("#bookmark-name").value="Python bookmark"'); click('#save-bookmark')
    wait('!document.querySelector("#dialog").open'); picture('python-player')
    if __import__('os').environ.get('CLAVIS_ICON_VERIFY'):
        assert js('document.querySelectorAll(".transport button svg").length')==5
        assert js('document.querySelectorAll("#sidebar .nav-icon svg").length')==11
        for name,action in [('bookmarks','audio-bookmarks'),('sleep','sleep'),('speed','speed')]:
            click('[data-action="'+action+'"]'); wait('document.querySelector("#dialog").open')
            wait('document.querySelector(".dialog-art")?.naturalWidth>0')
            boxes=js('(()=>{const r=id=>{const b=document.getElementById(id).getBoundingClientRect();return {left:b.left,right:b.right,center:b.top+b.height/2}};return {title:r("dialog-title"),art:r("dialog-art"),close:r("dialog-close")};})()')
            assert boxes['title']['right']<boxes['art']['left']
            assert boxes['art']['right']<boxes['close']['left']
            assert abs(boxes['title']['center']-boxes['close']['center'])<1
            assert abs(boxes['art']['center']-boxes['close']['center'])<1
            picture('aligned-'+name); click('#dialog-close')
        results['iconsAndDialogs']={'transportSVG':5,'sidebarSVG':11,'alignedDialogs':['bookmarks','sleep','speed']}
    assert js('document.documentElement.scrollHeight<=innerHeight+2'), 'Player scrolls outside window'
    click('nav [data-route="Home"]')
    if __import__('os').environ.get('CLAVIS_PASTEL_VERIFY'):
        # Check both themes and all shared illustration placements in the real UI.
        wait('document.querySelectorAll(".home-card").length===7')
        assert js('document.querySelectorAll(".home-card img[src*=home_]").length')==7
        click('#import'); wait('document.querySelector(".dialog-art")?.naturalWidth>0'); picture('pastel-import'); click('#dialog-close')
        click('#sidebar [data-route="Settings"]')
        wait('document.querySelector("#theme")')
        js('(()=>{const t=document.querySelector("#theme");t.value="light";t.dispatchEvent(new Event("change",{bubbles:true}));})()')
        wait('!document.body.classList.contains("dark")'); wait('document.querySelector(".surface-art")?.naturalWidth>0'); picture('pastel-settings-light')
        click('nav [data-route="Home"]'); wait('document.querySelectorAll(".home-card").length===7'); picture('pastel-home-light')
        click('nav [data-route="News"]'); wait('document.querySelector(".source-card")'); picture('pastel-feeds-light')
        click('#sidebar [data-route="Downloads"]'); wait('document.querySelector(".empty-art")?.naturalWidth>0'); picture('pastel-downloads-light')
        click('nav [data-route="EPUB"]')
        wait('document.querySelector("#heading")?.innerText.includes("EPUB")')
        js('(()=>{const t=document.querySelector("#search");t.value="missing-book-12345";t.dispatchEvent(new Event("input",{bubbles:true}));})()')
        wait('document.querySelector(".empty-art")?.src.includes("search.png")'); picture('pastel-search-light')
        assets=js('Promise.all(["library","downloads","feeds","settings","search","bookmarks"].map(name=>new Promise((resolve,reject)=>{const img=new Image();img.onload=()=>resolve({name,width:img.naturalWidth});img.onerror=()=>reject(Error("Missing illustration: "+name));img.src="../assets/pastel/"+name+".png";})))')
        assert all(a['width']>0 for a in assets)
        results['illustrations']={'originalHomeIcons':7,'assets':assets,'themes':['dark','light'],'dialogs':True}
        click('nav [data-route="Home"]')
    note=js('window.clavis.saveNote({title:"Python verification",text:"Saved by the native Python backend",drawing:[]})')
    assert note['title']=='Python verification'
    state=js('window.clavis.load()')
    assert any(b.get('bookmarks') for b in state['books'] if b['kind']=='EPUB')
    assert any(b.get('bookmarks') for b in state['books'] if b['kind']=='PDF')
    assert any(any(m['name']=='Python bookmark' for m in b.get('bookmarks',[])) for b in state['books'] if b['kind']=='Audio')
    # A narrow window must scroll the sidebar without moving the document.
    window.resize(700,400); time.sleep(.8)
    dimensions=js('(()=>{const s=document.querySelector(".sidebar-scroll");s.scrollTop=10000;return {client:s.clientHeight,scroll:s.scrollHeight,top:s.scrollTop}})()')
    assert dimensions['scroll']>dimensions['client'] and dimensions['top']>0
    picture('python-sidebar-small')
    results.update(imports=True,epub=True,pdf=True,audioPlayback=True,seek=True,bookmarks=True,notes=True,sidebar=dimensions)
    errors=js('window.__errors||[]')
    if errors: raise AssertionError(errors)
    results['errors']=errors
    return results
