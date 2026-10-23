"""Windows thumbnail toolbar connected to the renderer's audio transport."""
import ctypes
from ctypes import wintypes
import json
import logging
from pathlib import Path
from identity import GUID

class THUMBBUTTON(ctypes.Structure):
    _fields_=[('mask',wintypes.DWORD),('id',wintypes.UINT),('bitmap',wintypes.UINT),('icon',wintypes.HICON),('tip',wintypes.WCHAR*260),('flags',wintypes.DWORD)]

class TaskbarControls:
    IDS=(4101,4102,4103)
    def __init__(self,window,root):
        from System import Action
        from System.Threading.Tasks import Task,TaskScheduler
        from System import String
        from System.Windows.Forms import Timer
        self.window=window; self.native=window.native; self.hwnd=self.native.Handle.ToInt64()
        self.pointer=ctypes.c_void_p(); self.added=False; self.pending=False; self.closed=False; self.previous=None
        self.scheduler=TaskScheduler.FromCurrentSynchronizationContext()
        self.continuation=Action[Task[String]](self.received)
        result=ctypes.windll.ole32.CoCreateInstance(ctypes.byref(GUID('56FDF344-FD6D-11D0-958A-006097C9A090')),None,1,ctypes.byref(GUID('EA1AFB91-9E28-4B86-90E9-9E9F8A5EEFAF')),ctypes.byref(self.pointer))
        if result<0: raise OSError(f'Taskbar COM initialization failed: {result:#x}')
        table=ctypes.cast(self.pointer,ctypes.POINTER(ctypes.POINTER(ctypes.c_void_p))).contents
        self.release=ctypes.WINFUNCTYPE(ctypes.c_ulong,ctypes.c_void_p)(table[2])
        initialize=ctypes.WINFUNCTYPE(ctypes.c_long,ctypes.c_void_p)(table[3])
        self.add_buttons=ctypes.WINFUNCTYPE(ctypes.c_long,ctypes.c_void_p,wintypes.HWND,wintypes.UINT,ctypes.POINTER(THUMBBUTTON))(table[15])
        self.update_buttons=ctypes.WINFUNCTYPE(ctypes.c_long,ctypes.c_void_p,wintypes.HWND,wintypes.UINT,ctypes.POINTER(THUMBBUTTON))(table[16])
        result=initialize(self.pointer)
        if result<0: raise OSError(f'Taskbar initialization failed: {result:#x}')
        load=ctypes.windll.user32.LoadImageW; load.argtypes=[wintypes.HINSTANCE,wintypes.LPCWSTR,wintypes.UINT,ctypes.c_int,ctypes.c_int,wintypes.UINT]; load.restype=wintypes.HANDLE
        self.icons={key:load(None,str(Path(root)/'assets'/f'taskbar-{key}.ico'),1,24,24,0x10) for key in ('back','play','pause','forward')}
        if not all(self.icons.values()): raise OSError('Taskbar icon is missing')
        self.created=ctypes.windll.user32.RegisterWindowMessageW('TaskbarButtonCreated')
        self.callback_type=ctypes.WINFUNCTYPE(ctypes.c_ssize_t,wintypes.HWND,wintypes.UINT,ctypes.c_size_t,ctypes.c_ssize_t,ctypes.c_size_t,ctypes.c_size_t)
        self.callback=self.callback_type(self.message)
        self.subclass=ctypes.windll.comctl32.SetWindowSubclass
        self.subclass.argtypes=[wintypes.HWND,self.callback_type,ctypes.c_size_t,ctypes.c_size_t]
        self.remove=ctypes.windll.comctl32.RemoveWindowSubclass
        self.remove.argtypes=[wintypes.HWND,self.callback_type,ctypes.c_size_t]
        self.default=ctypes.windll.comctl32.DefSubclassProc
        self.default.argtypes=[wintypes.HWND,wintypes.UINT,ctypes.c_size_t,ctypes.c_ssize_t]; self.default.restype=ctypes.c_ssize_t
        if not self.subclass(self.hwnd,self.callback,1,0): raise OSError('Could not attach taskbar controls')
        self.timer=Timer(); self.timer.Interval=500; self.timer.Tick+=self.poll
        self.update({'ready':False}); self.timer.Start()
        self.native.FormClosed+=self.on_closed

    def message(self,hwnd,message,wparam,lparam,subclass_id,reference):
        try:
            if message==self.created: self.added=False; self.previous=None
            if message==0x111 and ((wparam>>16)&0xffff)==0x1800 and (wparam&0xffff) in self.IDS:
                action=dict(zip(self.IDS,('back','play','forward')))[wparam&0xffff]
                expression=f'window.clavisTransport?.command({json.dumps(action)})'
                self.native.webview.CoreWebView2.CallDevToolsProtocolMethodAsync('Runtime.evaluate',json.dumps({'expression':expression,'userGesture':True,'awaitPromise':True}))
                return 0
        except Exception: logging.exception('Taskbar command')
        return self.default(hwnd,message,wparam,lparam)

    def poll(self,*args):
        if self.closed or self.pending: return
        self.pending=True
        try:
            self.native.webview.ExecuteScriptAsync('window.clavisTransport ? window.clavisTransport.state() : ({ready:false})').ContinueWith(self.continuation,self.scheduler)
        except Exception: self.pending=False; logging.exception('Taskbar state')

    def received(self,task):
        self.pending=False
        if self.closed: return
        try: self.update(json.loads(task.Result))
        except Exception: logging.exception('Taskbar state update')

    def update(self,state):
        ready=bool(state.get('ready')); playing=bool(state.get('playing')); skip=max(5,min(120,int(state.get('skip') or 30)))
        current=(ready,playing,skip)
        if self.added and current==self.previous: return
        buttons=(THUMBBUTTON*3)()
        for index,(key,tip) in enumerate((('back',f'Seek backward {skip} seconds'),('pause' if playing else 'play','Pause' if playing else 'Play'),('forward',f'Seek forward {skip} seconds'))):
            buttons[index].mask=2|4|8; buttons[index].id=self.IDS[index]; buttons[index].icon=self.icons[key]; buttons[index].tip=tip; buttons[index].flags=0 if ready else 1
        method=self.update_buttons if self.added else self.add_buttons
        result=method(self.pointer,self.hwnd,3,buttons)
        if result<0:
            if self.previous!=('error',result): logging.warning('Taskbar buttons HRESULT: %#x',result)
            self.previous=('error',result); return
        if not self.added: logging.info('Taskbar preview controls added: backward, play/pause, forward')
        self.added=True; self.previous=current

    def on_closed(self,*args):
        self.closed=True; self.timer.Stop(); self.timer.Dispose(); self.remove(self.hwnd,self.callback,1)
        self.release(self.pointer)
        destroy=ctypes.windll.user32.DestroyIcon; destroy.argtypes=[wintypes.HICON]
        for icon in self.icons.values(): destroy(icon)
