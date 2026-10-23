"""Native Python/WebView2 entry point; no Electron or Node runtime."""
import ctypes
import json
import logging
import mimetypes
import os
from pathlib import Path
import re
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import unquote, urlparse

ROOT=Path(getattr(sys,'_MEIPASS',Path(__file__).resolve().parents[1]))
APP=Path(sys.executable).parent if getattr(sys,'frozen',False) else ROOT
if (ROOT/'python_vendor').is_dir(): sys.path.insert(0,str(ROOT/'python_vendor'))
sys.path.insert(0,str(Path(__file__).parent))
from core import Services, fetch, inside
from identity import APP_ID, window_identity

BRIDGE="""(()=>{
const ready=new Promise(resolve=>{if(window.pywebview?.api)resolve();else window.addEventListener('pywebviewready',resolve,{once:true});});
const call=async(method,...args)=>{await ready;const r=await window.pywebview.api.invoke(method,args);if(!r.ok)throw new Error(r.error);return r.value;};
const names=['load','importFiles','importFolder','updateBook','removeBook','deleteBook','settings','feeds','feedAdd','feedRefresh','feedRemove','article','playEpisode','getInk','saveInk','getTranscript','saveTranscript','prepareAudio','chapterScanStart','chapterScanRead','chapterScanCancel','applySpokenChapters','openURL','openFiles','saveNote','deleteNote','exportNote','exportDrawing','downloads','downloadAdd','downloadAction','kindleDetect','kindleScan','kindleImport','kindleExport','kindleExportFolder','kindleDeleteDeviceBook','kindleCover','updateBookMetadata'];
const api=Object.fromEntries(names.map(name=>[name,(...args)=>call(name,...args)]));
api.onDownloads=fn=>{let active=true,busy=false;const poll=async()=>{if(busy||!active)return;busy=true;try{const data=await api.downloads();if(active)fn(data);}catch(e){console.warn(e);}finally{busy=false;}};const timer=setInterval(poll,1500);return()=>{active=false;clearInterval(timer);};};
Object.defineProperty(window,'clavis',{value:Object.freeze(api),writable:false});
})();"""

class Server(ThreadingHTTPServer):
    daemon_threads=True
    def __init__(self,services):
        self.services=services; super().__init__(('127.0.0.1',0),Handler)

class Handler(BaseHTTPRequestHandler):
    protocol_version='HTTP/1.1'
    def log_message(self,*args): pass
    def do_HEAD(self): self.serve(True)
    def do_GET(self): self.serve(False)
    def output(self,raw,mime,head=False,status=200):
        self.send_response(status); self.send_header('Content-Type',mime); self.send_header('Content-Length',str(len(raw))); self.send_header('X-Content-Type-Options','nosniff'); self.send_header('Cache-Control','no-store'); self.end_headers()
        if not head: self.wfile.write(raw)
    def serve(self,head):
        try:
            s=self.server.services
            if self.headers.get('Host')!=urlparse(s.origin).netloc: return self.output(b'Forbidden','text/plain',head,403)
            path=unquote(urlparse(self.path).path)
            if path=='/python-bridge.js': return self.output(BRIDGE.encode(),'application/javascript',head)
            if path.startswith('/media/'):
                file=s.media.get(path[7:])
                if not file: return self.output(b'Not found','text/plain',head,404)
                if file.startswith(('https://','http://')):
                    headers={k:self.headers[k] for k in ('Range','If-Range') if k in self.headers}
                    with fetch(file,stream=True,headers=headers) as r:
                        self.send_response(r.status_code)
                        for k in ('Content-Type','Content-Length','Content-Range','Accept-Ranges'):
                            if k in r.headers: self.send_header(k,r.headers[k])
                        self.send_header('Connection','close'); self.end_headers(); self.close_connection=True
                        if not head:
                            for chunk in r.iter_content(65536): self.wfile.write(chunk)
                    return
                return self.local(Path(file),head)
            relative=path.lstrip('/'); file=ROOT/relative
            if relative.split('/')[0] not in ('ui','assets') or not inside(file,ROOT) or not file.is_file(): return self.output(b'Not found','text/plain',head,404)
            if relative=='ui/index.html':
                raw=file.read_text(encoding='utf-8').replace('<script type="module"','<script src="/python-bridge.js"></script><script type="module"')
                return self.output(raw.encode(),'text/html; charset=utf-8',head)
            return self.local(file,head,worker=relative=='ui/vosk-worker.js')
        except (BrokenPipeError,ConnectionResetError,ConnectionAbortedError): pass
        except Exception:
            logging.exception('HTTP')
            try: self.output(b'Unable to open this resource.','text/plain',head,500)
            except OSError: pass
    def local(self,file,head,worker=False):
        if not file.is_file(): return self.output(b'Not found','text/plain',head,404)
        size=file.stat().st_size; start=0; end=size-1; status=200
        value=self.headers.get('Range')
        if value:
            match=re.fullmatch(r'bytes=(\d*)-(\d*)',value)
            if not match or not any(match.groups()): return self.output(b'Invalid range','text/plain',head,416)
            if match[1]: start=int(match[1]); end=min(int(match[2]),end) if match[2] else end
            else: start=max(0,size-int(match[2]))
            if start>=size or end<start:
                self.send_response(416); self.send_header('Content-Range',f'bytes */{size}'); self.send_header('Content-Length','0'); self.end_headers(); return
            status=206
        length=max(0,end-start+1); self.send_response(status)
        mime={'.js':'application/javascript','.mjs':'application/javascript','.wasm':'application/wasm','.epub':'application/epub+zip','.m4b':'audio/mp4','.gz':'application/gzip'}.get(file.suffix.lower(),mimetypes.guess_type(file)[0] or 'application/octet-stream')
        self.send_header('Content-Type',mime); self.send_header('Content-Length',str(length)); self.send_header('Accept-Ranges','bytes'); self.send_header('X-Content-Type-Options','nosniff')
        if status==206: self.send_header('Content-Range',f'bytes {start}-{end}/{size}')
        if worker: self.send_header('Content-Security-Policy',"default-src 'none'; script-src 'self' 'unsafe-eval' 'wasm-unsafe-eval'; connect-src 'self'; worker-src 'none'")
        self.end_headers()
        if not head:
            with file.open('rb') as stream:
                stream.seek(start)
                while length:
                    chunk=stream.read(min(262144,length))
                    if not chunk: break
                    self.wfile.write(chunk); length-=len(chunk)

class Bridge:
    def __init__(self,services): self._services=services
    def invoke(self,method,args): return self._services.invoke(method,args)

def main():
    data=Path(os.environ.get('CLAVIS_DATA_DIR',str(APP/'Data'))); (data/'Logs').mkdir(parents=True,exist_ok=True)
    logging.basicConfig(filename=str(data/'Logs/python.log'),level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
    # A separate mutex per portable installation protects the library from concurrent writers.
    import hashlib
    kernel=ctypes.windll.kernel32; kernel.CreateMutexW.restype=ctypes.c_void_p
    mutex=kernel.CreateMutexW(None,False,'Local\\ClavisPython'+hashlib.sha256(str(data.resolve()).lower().encode()).hexdigest()[:24])
    if kernel.GetLastError()==183:
        ctypes.windll.user32.MessageBoxW(None,'Clavis is already open.','Clavis',64); return
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(APP_ID)
    import webview
    services=Services(ROOT,data); server=Server(services); services.origin=f'http://127.0.0.1:{server.server_port}'
    threading.Thread(target=server.serve_forever,daemon=True).start()
    debug_port=os.environ.get('CLAVIS_DEBUG_PORT')
    if debug_port: webview.settings['REMOTE_DEBUGGING_PORT']=int(debug_port)
    webview.settings['OPEN_EXTERNAL_LINKS_IN_BROWSER']=True
    webview.settings['ALLOW_FILE_URLS']=False
    # pywebview uses Windows logical pixels, matching the screen working area below.
    import clr
    clr.AddReference('System.Windows.Forms')
    from System.Windows.Forms import Screen
    area=Screen.PrimaryScreen.WorkingArea; width=round(area.Width*.7); height=round(area.Height*.7)
    window=webview.create_window('Clavis',services.origin+'/ui/index.html',js_api=Bridge(services),width=width,height=height,x=area.X+round((area.Width-width)/2),y=area.Y+round((area.Height-height)/2),min_size=(560,360),background_color='#FAF9FD',text_select=True)
    services.window=window
    def loaded():
        from System import Action
        def configure():
            native=window.native; native.Text='Clavis'; native.webview.ZoomFactor=.8
            identity=window_identity(native.Handle.ToInt64(),sys.executable)
            logging.info('Verified taskbar identity: %s',identity)
            if not hasattr(window,'_clavis_taskbar'):
                from taskbar import TaskbarControls
                window._clavis_taskbar=TaskbarControls(window,ROOT)
            native.webview.CoreWebView2.Settings.IsZoomControlEnabled=False
            def navigation(sender,args):
                if str(args.Uri)!=services.origin+'/ui/index.html': args.Cancel=True
            native.webview.CoreWebView2.NavigationStarting+=navigation
            # Retain event delegate for the window lifetime.
            window._clavis_navigation=navigation
        window.native.Invoke(Action(configure))
    window.events.loaded+=loaded
    def smoke():
        if not os.environ.get('CLAVIS_SMOKE'): return
        import time
        result={'ok':False}
        try:
            if not window.events.loaded.wait(45): raise RuntimeError('Window did not load within 45 seconds')
            time.sleep(2)
            result['page']=window.evaluate_js("({title:document.title,url:location.href,text:document.body.innerText.slice(0,1400),api:!!window.clavis})")
            if not result['page']['api']: raise RuntimeError('Bridge is missing')
            event=threading.Event(); values=[]
            window.evaluate_js("window.clavis.load().then(s=>({books:s.books.length,theme:s.settings.theme}));",lambda value:(values.append(value),event.set()))
            if not event.wait(20): raise RuntimeError('Native bridge did not respond')
            result['state']=values[0]
            import ssl
            context=ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            result['tls']={'contextCreated':True,'certificateVerification':context.verify_mode==ssl.CERT_REQUIRED}
            if os.environ.get('CLAVIS_NETWORK_TEST'):
                from core import fetch
                raw,url=fetch(os.environ['CLAVIS_NETWORK_TEST'],max_bytes=64*1024*1024)
                parsed=services.parse_feed({'id':'network-verification','url':url,'kind':'News'},raw)
                result['network']={'url':url,'title':parsed['title'],'entries':len(parsed['entries']),'newestDate':parsed['entries'][0]['date'] if parsed['entries'] else None}
            if os.environ.get('CLAVIS_VERIFY'):
                from verify import verify
                result['verification']=verify(window,services,data)
            result['ok']=True
        except Exception as e:
            result['error']=str(e); logging.exception('Smoke test')
        finally:
            (data/'smoke.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
            window.destroy()
    try:
        webview.start(smoke,gui='edgechromium',private_mode=False,storage_path=str(data/'SessionPython'),icon=str(ROOT/'assets/icon.ico'))
    finally:
        services.close(); server.shutdown(); server.server_close(); kernel.CloseHandle(ctypes.c_void_p(mutex))

if __name__=='__main__':
    try: main()
    except Exception as e:
        logging.exception('Startup')
        ctypes.windll.user32.MessageBoxW(None,f'Clavis could not start.\n\n{e}\n\nDetails: {APP / "Data/Logs/python.log"}','Clavis',16)
        raise
