# Build with the workspace Python dependencies on PYTHONPATH.
from PyInstaller.utils.hooks import collect_all
from pathlib import Path
import ssl
datas=[]; binaries=[]; hidden=[]
for package in ('webview','pythonnet','clr_loader','libtorrent','readability'):
    d,b,h=collect_all(package); datas+=d; binaries+=b; hidden+=h
datas += [('ui','ui'),('assets/rss/catalog.json','assets/rss'),('licenses','licenses'),('README-Python.md','.'),('node_modules/ffmpeg-static/ffmpeg.exe.LICENSE','licenses'),('node_modules/ffmpeg-static/ffmpeg.exe.README','licenses')]
# Bundle interface assets, but never the saved RSS XML/article snapshots.
datas += [(str(p),'assets') for p in Path('assets').iterdir() if p.is_file()]
datas += [('assets/pastel','assets/pastel')]
# This Python runtime loads an additional CA policy file when creating any TLS
# context. It must remain next to the frozen ssl module, including in releases.
runtime_ca=Path(ssl.__file__).with_name('codex-rejected-cas.pem')
if runtime_ca.exists(): datas.append((str(runtime_ca),'.'))
binaries += [('node_modules/ffmpeg-static/ffmpeg.exe','.')]
a=Analysis(['python_app/host.py'],pathex=['python_app','python_vendor'],binaries=binaries,datas=datas,hiddenimports=hidden+['webview.platforms.winforms','webview.platforms.edgechromium','clr','mutagen.mp3','mutagen.mp4','mutagen.flac','mutagen.wave','mutagen.oggvorbis','mutagen.oggopus','mutagen.aac','send2trash.win.modern'],hookspath=[],excludes=['PySide6','PyQt6','PyQt5','PySide2','tkinter','matplotlib','pandas','numpy','scipy','IPython','pytest'],noarchive=False)
pyz=PYZ(a.pure)
exe=EXE(pyz,a.scripts,[],exclude_binaries=True,name='Clavis',debug=False,bootloader_ignore_signals=False,strip=False,upx=False,console=False,icon='assets/icon.ico',version='python_app/version.txt')
coll=COLLECT(exe,a.binaries,a.datas,strip=False,upx=False,name='Clavis')
