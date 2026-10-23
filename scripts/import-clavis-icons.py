import json
from pathlib import Path
import xml.etree.ElementTree as ET
root=Path(r'C:\Users\ANT-PC\OneDrive\Documents\ChatGPT\Audiobook\Reson\app\src\main\res\drawable')
ns='{http://schemas.android.com/apk/res/android}'
names={'Home':'ic_home','EPUB':'ic_book','PDF':'ic_pdf','Audio':'ic_listen_audio','News':'ic_news','Podcasts':'ic_podcast','Downloads':'ic_download_books','Files':'ic_book','Settings':'ic_cursor'}
icons={}
for name,file in names.items():
    vector=ET.parse(root/(file+'.xml')).getroot()
    paths=[]
    for p in vector.findall('path'):
        attrs={'d':p.get(ns+'pathData'),'fill':'none' if 'transparent' in p.get(ns+'fillColor','') else 'currentColor'}
        for old,new in [('strokeColor','stroke'),('strokeWidth','stroke-width'),('strokeLineCap','stroke-linecap'),('strokeLineJoin','stroke-linejoin'),('fillType','fill-rule')]:
            if p.get(ns+old):attrs[new]='currentColor' if old=='strokeColor' else ('evenodd' if p.get(ns+old)=='evenOdd' else p.get(ns+old))
        paths.append('<path '+' '.join(f'{k}="{v}"' for k,v in attrs.items())+'/>')
    icons[name]='<svg viewBox="0 0 '+vector.get(ns+'viewportWidth','24')+' '+vector.get(ns+'viewportHeight','24')+'" aria-hidden="true">'+''.join(paths)+'</svg>'
icons['Journals']='<img src="../assets/home_articles.png" alt="">'
icons['Journalling']='<img src="../assets/home_journals.png" alt="">'
Path('src/icons.js').write_text('export const clavisIcons = '+json.dumps(icons)+';\n',encoding='utf-8')
