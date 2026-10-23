"""Explicit Windows taskbar identity, independent of Explorer's executable cache."""
import ctypes
from pathlib import Path
import uuid

APP_ID='com.clavis.reader.python.windows'

class GUID(ctypes.Structure):
    _fields_=[('data',ctypes.c_ubyte*16)]
    def __init__(self,value):
        super().__init__(); self.data[:]=uuid.UUID(value).bytes_le

class PROPERTYKEY(ctypes.Structure):
    _fields_=[('fmtid',GUID),('pid',ctypes.c_ulong)]

class VALUE(ctypes.Union):
    _fields_=[('string',ctypes.c_void_p),('padding',ctypes.c_byte*16)]

class PROPVARIANT(ctypes.Structure):
    _fields_=[('vt',ctypes.c_ushort),('reserved1',ctypes.c_ushort),('reserved2',ctypes.c_ushort),('reserved3',ctypes.c_ushort),('value',VALUE)]

def window_identity(hwnd,executable):
    """Set and read back Shell relaunch properties on the native window."""
    shell=ctypes.windll.shell32; store=ctypes.c_void_p()
    get=shell.SHGetPropertyStoreForWindow
    get.argtypes=[ctypes.c_void_p,ctypes.POINTER(GUID),ctypes.POINTER(ctypes.c_void_p)]; get.restype=ctypes.c_long
    result=get(ctypes.c_void_p(int(hwnd)),ctypes.byref(GUID('886D8EEB-8CF2-4446-8D02-CDBA1DBDCF99')),ctypes.byref(store))
    if result<0: raise OSError(f'Window property store: {result:#x}')
    executable=str(Path(executable).resolve())
    # Explorer may cache the previous Electron icon for an executable at the
    # same path. A separate ICO resource avoids that executable cache entry.
    icon=Path(executable).parent/'_internal/assets/clavis-taskbar.ico'
    if not icon.exists(): icon=Path(__file__).resolve().parents[1]/'assets/clavis-taskbar.ico'
    return set_properties(store,{2:f'"{executable}"',3:str(icon)+',0',4:'Clavis',5:APP_ID})

def shortcut_identity(path):
    store=ctypes.c_void_p(); get=ctypes.windll.shell32.SHGetPropertyStoreFromParsingName
    get.argtypes=[ctypes.c_wchar_p,ctypes.c_void_p,ctypes.c_ulong,ctypes.POINTER(GUID),ctypes.POINTER(ctypes.c_void_p)]; get.restype=ctypes.c_long
    result=get(str(Path(path).resolve()),None,2,ctypes.byref(GUID('886D8EEB-8CF2-4446-8D02-CDBA1DBDCF99')),ctypes.byref(store))
    if result<0: raise OSError(f'Shortcut property store: {result:#x}')
    return set_properties(store,{5:APP_ID})

def set_properties(store,values):
    table=ctypes.cast(store,ctypes.POINTER(ctypes.POINTER(ctypes.c_void_p))).contents
    set_value=ctypes.WINFUNCTYPE(ctypes.c_long,ctypes.c_void_p,ctypes.POINTER(PROPERTYKEY),ctypes.POINTER(PROPVARIANT))(table[6])
    get_value=ctypes.WINFUNCTYPE(ctypes.c_long,ctypes.c_void_p,ctypes.POINTER(PROPERTYKEY),ctypes.POINTER(PROPVARIANT))(table[5])
    commit=ctypes.WINFUNCTYPE(ctypes.c_long,ctypes.c_void_p)(table[7])
    release=ctypes.WINFUNCTYPE(ctypes.c_ulong,ctypes.c_void_p)(table[2])
    readback={}
    try:
        for pid,text in values.items():
            key=PROPERTYKEY(GUID('9F4C2855-9F79-4B39-A8D0-E1D42DE1D5F3'),pid)
            buffer=ctypes.create_unicode_buffer(text); variant=PROPVARIANT(); variant.vt=31; variant.value.string=ctypes.cast(buffer,ctypes.c_void_p).value
            result=set_value(store,ctypes.byref(key),ctypes.byref(variant))
            if result<0: raise OSError(f'Taskbar property {pid}: {result:#x}')
        result=commit(store)
        if result<0: raise OSError(f'Taskbar commit: {result:#x}')
        for pid in values:
            key=PROPERTYKEY(GUID('9F4C2855-9F79-4B39-A8D0-E1D42DE1D5F3'),pid); variant=PROPVARIANT()
            result=get_value(store,ctypes.byref(key),ctypes.byref(variant))
            if result<0: raise OSError(f'Read taskbar property {pid}: {result:#x}')
            try: readback[pid]=ctypes.wstring_at(variant.value.string) if variant.vt==31 else None
            finally: ctypes.windll.ole32.PropVariantClear(ctypes.byref(variant))
        if values!=readback: raise RuntimeError('Windows taskbar identity verification failed')
        return readback
    finally: release(store)
