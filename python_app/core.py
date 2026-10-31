"""Clavis native services. All persistent data lives beside Clavis.exe."""
import base64
import calendar
import copy
import hashlib
import html as htmllib
import ipaddress
import json
import logging
import mimetypes
import os
from pathlib import Path
import re
import shutil
import socket
import subprocess
import threading
import time
import uuid
from urllib.parse import urljoin, urlparse, parse_qs
import webbrowser

import feedparser
import requests
from readability import Document

import bookart
import kindle
import listen
import metadata

AUDIO = {'.mp3', '.m4a', '.m4b', '.ogg', '.wav', '.flac', '.opus', '.aac'}
FEED_KINDS = ('News', 'Podcasts', 'Journals')
FEED_TOPICS = ['Medical','Technology','Science','Environment','Business','Politics','India','World','Culture','Education','Social sciences','Engineering','Mathematics','Physics','Chemistry','Biology','Space']
FEED_IMAGE_LOGO = re.compile(r'(logo|favicon|sprite|avatar|icon)[-_./]', re.I)
FEED_NON_IMAGE = re.compile(r'\.(mp3|m4a|m4b|ogg|oga|opus|wav|aac|flac|m3u8|pdf|epub|zip|html?)([?#]|$)', re.I)
FEED_FETCH_LIMIT = 8*1024*1024
FEED_CONTENT_LIMIT = 256*1024
def uid(value): return hashlib.sha256(str(value).lower().encode()).hexdigest()[:24]
def now(): return int(time.time()*1000)
def natural(value): return [int(x) if x.isdigit() else x.lower() for x in re.split(r'(\d+)',str(value))]
def name(value):
    result=re.sub(r'\s+', ' ', re.sub(r'[<>:"/\\|?*\x00-\x1f]', ' ',str(value))).strip(' .')[:140] or 'Untitled book'
    return 'Book '+result if re.match(r'^(con|prn|aux|nul|com[1-9]|lpt[1-9])(\.|$)',result,re.I) else result
def inside(file,folder): return Path(file).resolve().is_relative_to(Path(folder).resolve())
def atomic(file,value):
    file=Path(file); file.parent.mkdir(parents=True,exist_ok=True)
    tmp=file.with_suffix(file.suffix+'.tmp'); tmp.write_text(json.dumps(value,ensure_ascii=False,indent=2),encoding='utf-8')
    for attempt in range(6):
        try: os.replace(tmp,file); return
        except PermissionError:
            if attempt==5: raise
            time.sleep(.05*(attempt+1))

def public_url(url):
    parsed=urlparse(url)
    if parsed.scheme not in ('http','https') or not parsed.hostname or parsed.username or parsed.password:
        raise ValueError('Enter a public HTTP or HTTPS address.')
    for address in socket.getaddrinfo(parsed.hostname,parsed.port or (443 if parsed.scheme=='https' else 80),type=socket.SOCK_STREAM):
        if not ipaddress.ip_address(address[4][0]).is_global: raise ValueError('Private network addresses are not allowed.')
    return url

def fetch(url,stream=False,headers=None,max_bytes=12*1024*1024):
    # Podcast hosts such as podtrac chain six or more tracking redirects before the audio file.
    for _ in range(15):
        public_url(url)
        response=requests.get(url,headers={'User-Agent':'Clavis/0.2.0','Cache-Control':'no-cache','Pragma':'no-cache',**(headers or {})},timeout=(15,30),allow_redirects=False,stream=True)
        if response.status_code in (301,302,303,307,308):
            from urllib.parse import urljoin
            url=urljoin(url,response.headers['Location']); response.close(); continue
        response.raise_for_status()
        if stream: return response
        try:
            chunks=[]; size=0
            for chunk in response.iter_content(65536):
                size+=len(chunk)
                if size>max_bytes: raise ValueError('This page is too large.')
                chunks.append(chunk)
            return b''.join(chunks),response.url
        finally: response.close()
    raise ValueError('Too many redirects.')

def plain_text(value):
    text=re.sub(r'<(script|style)[^>]*>.*?</\1>',' ',value or '',flags=re.I|re.S)
    return re.sub(r'\s+',' ',htmllib.unescape(re.sub(r'<[^>]+>',' ',text))).strip()

def absolute_markup(value,base):
    def fix(match):
        try: target=urljoin(base,htmllib.unescape(match.group(2)).strip())
        except ValueError: return match.group(0)
        return f'{match.group(1)}="{target}"'
    return re.sub(r'(?i)\b(src|href)\s*=\s*["\']([^"\']+)["\']',fix,value or '')

def meta_content(raw,*names):
    for name in names:
        pattern=re.escape(name)
        for regex in (rf'<meta[^>]+(?:property|name)\s*=\s*["\']{pattern}["\'][^>]*?content\s*=\s*["\']([^"\']*)', rf'<meta[^>]+content\s*=\s*["\']([^"\']*)["\'][^>]*?(?:property|name)\s*=\s*["\']{pattern}["\']'):
            match=re.search(regex,raw,re.I)
            if match and match.group(1).strip(): return htmllib.unescape(match.group(1).strip())
    return ''

class Services:
    def __init__(self,root,data):
        self.root=Path(root); self.data=Path(data); self.booksdir=self.data/'Books'
        self.booksdir.mkdir(parents=True,exist_ok=True)
        self.lock=threading.RLock(); self.tokens={}; self.media={}; self.origin=''; self.window=None
        self.scans={}; self.handles={}; self.torrent=None; self.stopping=threading.Event()
        self.kindle_device=None; self.kindle_books=[]
        self.ffmpeg=self.root/'ffmpeg.exe'
        if not self.ffmpeg.exists(): self.ffmpeg=self.root/'node_modules/ffmpeg-static/ffmpeg.exe'
        self.catalog=json.loads((self.root/'assets/rss/catalog.json').read_text(encoding='utf-8'))
        self.feedsdir=self.data/'feed-cache'; self.feedsdir.mkdir(parents=True,exist_ok=True)
        self.articledir=self.data/'articles'; self.articledir.mkdir(parents=True,exist_ok=True)
        self.activityfile=self.data/'feed-activity.json'
        try: self.activity=json.loads(self.activityfile.read_text(encoding='utf-8'))
        except (OSError,ValueError): self.activity={}
        self.file=self.data/'library.json'
        if self.file.exists():
            self.store=json.loads(self.file.read_text(encoding='utf-8-sig'))
            if not isinstance(self.store.get('books'),list) or not isinstance(self.store.get('feeds'),list): raise ValueError('Library is invalid. Your existing data has been preserved.')
        else:
            self.store={'books':[],'feeds':[],'notes':[],'downloads':[],'settings':{}}
        settings=self.store.setdefault('settings',{})
        for key,value in {'theme':'system','fontSize':19,'lineHeight':1.7,'margin':32,'skip':30,'volume':.8,'speed':1,'listenRate':1,'listenSpeaker':1,'listenFollow':True,'feedTopics':{},'feedOrder':{'News':'latest','Journals':'latest'}}.items(): settings.setdefault(key,value)
        self.store['directory']=self.catalog
        for key in ('notes','downloads'): self.store.setdefault(key,[])
        self.reconcile_feeds()
        old=self.store.get('dataRoot')
        if old and Path(old)!=self.data:
            def rebase(value): return str(self.data/Path(value).relative_to(old)) if value and inside(value,old) else value
            for book in self.store['books']:
                for key in ('path','source','cover'):
                    if book.get(key): book[key]=rebase(book[key])
                for track in book.get('tracks',[]):
                    if track.get('path'): track['path']=rebase(track['path'])
            for job in self.store['downloads']: job['dir']=rebase(job['dir'])
        self.store['dataRoot']=str(self.data)
        self.listen=listen.Narration(self.data/'listen',self.media_url)
        for job in self.store['downloads']:
            if job.get('status')!='Complete': job['status']='Paused'
        self.save()
        threading.Thread(target=self.download_loop,daemon=True).start()

    def save(self):
        with self.lock:
            snapshot={**self.store,'feeds':[{k:v for k,v in feed.items() if k not in ('entries','updated','lastAttempt','refreshError')} for feed in self.store['feeds']]}
            atomic(self.file,snapshot)
    def feed_cache_file(self,id): return self.feedsdir/(re.sub(r'[^0-9a-f]','',str(id))[:64]+'.json')
    def load_feed_cache(self,feed):
        try: data=json.loads(self.feed_cache_file(feed['id']).read_text(encoding='utf-8'))
        except (OSError,ValueError): return
        if isinstance(data,list): feed['entries']=data
        elif isinstance(data,dict):
            feed['entries']=data.get('entries') if isinstance(data.get('entries'),list) else []
            feed['updated']=data.get('updated') or feed.get('updated')
            feed['lastAttempt']=data.get('lastAttempt') or feed.get('lastAttempt')
            feed['refreshError']=data.get('refreshError')
    def save_feed_cache(self,feed):
        atomic(self.feed_cache_file(feed['id']),{'entries':feed.get('entries',[]),'updated':feed.get('updated'),'lastAttempt':feed.get('lastAttempt'),'refreshError':feed.get('refreshError')})
    def reconcile_feeds(self):
        active={(source.get('kind'),source.get('url')) for source in self.catalog}
        retired=set()
        for name in ('legacy-defaults-v1.json','legacy-defaults-v2.json'):
            try: rows=json.loads((self.root/'assets/rss'/name).read_text(encoding='utf-8'))
            except (OSError,ValueError): rows=[]
            for row in rows if isinstance(rows,list) else []:
                key=(row.get('kind'),row.get('url'))
                if key not in active: retired.add(key)
        try: legacy_podcasts=json.loads((self.root/'assets/rss/legacy-podcasts-v3.json').read_text(encoding='utf-8'))
        except (OSError,ValueError): legacy_podcasts=[]
        for url in legacy_podcasts if isinstance(legacy_podcasts,list) else []:
            if ('Podcasts',url) not in active: retired.add(('Podcasts',url))
        feeds=[feed for feed in self.store['feeds'] if (feed.get('kind'),feed.get('url')) not in retired]
        seeded=self.store.get('feedCatalog')=='clavis-plus-1'
        for source in self.catalog:
            feed=next((item for item in feeds if item.get('kind')==source['kind'] and item.get('url')==source['url']),None)
            if feed is None:
                if seeded or not source.get('preload'): continue
                feed={'id':uid(source['kind']+source['url']),'kind':source['kind'],'url':source['url']}
                feeds.append(feed)
            feed['title']=source.get('title') or feed.get('title') or 'Source'
            for key in ('tags','contentMode','policy','image','artist','website'):
                if source.get(key) is not None: feed[key]=source[key]
        for feed in feeds:
            feed.setdefault('tags',[]); feed.setdefault('contentMode','open-access'); feed.setdefault('policy','')
            feed.setdefault('entries',[]); feed.setdefault('updated',None); feed.setdefault('refreshError',None)
            if not feed.get('entries'): self.load_feed_cache(feed)
        self.store['feedCatalog']='clavis-plus-1'
        self.store['feeds']=feeds
    def feeds_payload(self):
        return {'feeds':copy.deepcopy(self.store['feeds']),'directory':copy.deepcopy(self.catalog),'activity':copy.deepcopy(self.activity)}
    def feed_opened(self,key):
        key=str(key or '')[:2048]
        if not key: return copy.deepcopy(self.activity)
        with self.lock:
            self.activity[key]=min(100000,int(self.activity.get(key,0))+1)
            atomic(self.activityfile,self.activity)
        return copy.deepcopy(self.activity)
    def article(self,url):
        public_url(url)
        path=self.articledir/(hashlib.sha256(url.encode('utf-8')).hexdigest()+'.json')
        saved=None
        try: saved=json.loads(path.read_text(encoding='utf-8'))
        except (OSError,ValueError): pass
        if saved and time.time()-float(saved.get('time',0) or 0)<6*3600: return saved
        try: raw,final=fetch(url,max_bytes=FEED_FETCH_LIMIT)
        except requests.HTTPError as error:
            status=error.response.status_code if error.response is not None else None
            if status in (401,403):
                return {'availability':'publisher-blocked','status':status,'url':url,'content':None}
            if saved: return saved
            raise
        except Exception:
            if saved: return saved
            raise
        text=raw.decode('utf-8',errors='replace')
        try:
            doc=Document(text,url=final)
            title=htmllib.unescape(doc.short_title() or doc.title() or '')[:600]
            content=absolute_markup(doc.summary(html_partial=True),final)
        except Exception:
            logging.exception('Article extraction %s',url)
            if saved: return saved
            raise ValueError('This story could not be read. Open the website to read it.')
        content=re.sub(r'(?is)<(script|style|iframe|form|button|input|svg|video|audio)[^>]*>.*?</\1>',' ',content)
        content=re.sub(r'(?is)<(script|style|iframe|form|button|input|svg|video|audio)[^>]*/?>',' ',content)
        characters=len(plain_text(content))
        if saved and characters<120: return saved
        image=meta_content(text,'og:image','twitter:image','twitter:image:src')
        if not image:
            match=re.search(r'<img[^>]+src=["\']([^"\']+)',content,re.I)
            image=match[1] if match else ''
        if image:
            try: image=urljoin(final,image)
            except ValueError: image=''
        result={'availability':'available','title':title,'content':content if characters>=120 else '','characters':characters,
                'byline':meta_content(text,'author','article:author','bylines','citation_author')[:300],
                'published':meta_content(text,'article:published_time','citation_publication_date','datePublished','date')[:80],
                'image':image[:2000] if image.startswith('https://') else '',
                'preview':'you have a preview view of this article' in text.lower(),
                'url':final,'time':int(time.time())}
        if characters>=120: atomic(path,result)
        return result
    def book(self,id):
        return next(b for b in self.store['books'] if b['id']==id)
    def media_url(self,path):
        if not path: return None
        with self.lock:
            if path not in self.tokens:
                token=uuid.uuid4().hex+uuid.uuid4().hex; self.tokens[path]=token; self.media[token]=path
            return self.origin+'/media/'+self.tokens[path]
    def view(self,book):
        b=copy.deepcopy(book)
        b.pop('source',None); b.pop('path',None)
        b['cover']=book.get('remoteCover') or self.media_url(book.get('cover'))
        if book.get('path'): b['url']=self.media_url(book['path'])
        if 'tracks' in b:
            for t in b['tracks']: t['url']=self.media_url(t.get('remote') or t.pop('path',None))
        return b
    def state(self): return {'books':[self.view(b) for b in self.store['books']],'settings':copy.deepcopy(self.store['settings']),'notes':copy.deepcopy(self.store['notes'])}
    def folder(self,title):
        title=name(title)
        for i in range(1,10000):
            p=self.booksdir/(title+(f' ({i})' if i>1 else ''))
            try: p.mkdir(); return p
            except FileExistsError: pass
        raise ValueError('Too many folders with the same title.')
    def organize(self,b):
        files=list(dict.fromkeys([p for p in [b.get('path'),b.get('cover'),*[t.get('path') for t in b.get('tracks',[])]] if p]))
        if not files or all(inside(p,self.booksdir) for p in files): return
        dest=self.folder(b['title']); primary=[b['path']] if b.get('path') else [t['path'] for t in b['tracks']]
        common=Path(os.path.commonpath([str(Path(p).parent) for p in primary])); mapped={}
        for file in files:
            source=Path(file); relative=source.relative_to(common) if inside(source,common) else Path(source.name)
            target=dest/relative; target.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(source,target); mapped[file]=str(target)
        for k in ('path','cover'):
            if b.get(k): b[k]=mapped[b[k]]
        for t in b.get('tracks',[]):
            if t.get('path'): t['path']=mapped[t['path']]
        b['source']=str(dest)
    def new_book(self,file):
        p=Path(file); suffix=p.suffix.lower()
        kind='Audio' if suffix in AUDIO else 'EPUB' if suffix=='.epub' else 'PDF' if suffix=='.pdf' else 'Kindle' if suffix in kindle.KINDLE_EXTS else None
        if not kind: return None
        b={'id':uid(str(p.resolve())),'title':p.stem.replace('_',' '),'kind':kind,'source':str(p),'position':0,'progress':0,'bookmarks':[],'lastActive':0}
        if kind=='Audio': b.update(tracks=[{'path':str(p),'title':b['title']}],chapter=0)
        else:
            b['path']=str(p)
            if kind=='Kindle':
                try:
                    meta=kindle.parse_book(str(p))
                    b['title']=meta['title'] or b['title']
                    if meta['author']: b['author']=meta['author']
                    b['kindleFormat']=meta['format']
                    if meta['drm']: b['kindleDrm']=True
                except Exception: logging.exception('Kindle metadata %s',p)
            elif kind=='PDF':
                try:
                    meta=kindle.pdf_metadata(str(p))
                    b['title']=meta.get('title') or b['title']
                    if meta.get('author'): b['author']=meta['author']
                    if meta.get('subject'): b['subject']=meta['subject']
                    if meta.get('publisher'): b['publisher']=meta['publisher']
                    if meta.get('isbn'): b['isbn']=meta['isbn']
                    if meta.get('published'): b['published']=meta['published']
                except Exception: logging.exception('PDF metadata %s',p)
        return b
    def scan_folder(self,folder):
        groups={}; docs=[]
        for p in sorted(Path(folder).rglob('*'),key=natural):
            if not p.is_file(): continue
            if p.suffix.lower() in AUDIO:
                parent=p.parent.parent if re.match(r'^(cd|disc|disk)[\s_-]*\d+$',p.parent.name,re.I) else p.parent
                groups.setdefault(parent,[]).append(p)
            elif p.suffix.lower() in ('.pdf','.epub') or p.suffix.lower() in kindle.KINDLE_EXTS: docs.append(self.new_book(p))
        for parent,files in groups.items():
            b=self.new_book(files[0]); b.update(id=uid(str(parent)),title=parent.name,source=str(parent),tracks=[{'path':str(p),'title':p.stem} for p in files])
            covers=sorted([p for p in parent.iterdir() if p.suffix.lower() in ('.jpg','.jpeg','.png','.webp')],key=lambda p:not re.match(r'^(cover|folder|front)\.',p.name,re.I))
            if covers: b['cover']=str(covers[0])
            docs.append(b)
        return docs
    def metadata(self,b):
        from mutagen import File
        old=b.get('tracks',[]); tracks=[]
        for file in dict.fromkeys(t['path'] for t in old if t.get('path')):
            try:
                m=File(file); duration=float(m.info.length) if m and m.info else 0
                basic=File(file,easy=True)
                if basic:
                    b['author']=(basic.get('artist') or [''])[0]
                    if len(set(t.get('path') for t in old))==1: b['title']=(basic.get('album') or basic.get('title') or [b['title']])[0]
                result=subprocess.run([str(self.ffmpeg),'-hide_banner','-i',file],capture_output=True,creationflags=0x08000000,timeout=30)
                text=result.stderr.decode('utf-8',errors='replace')
                match=re.search(r'Duration: (\d+):(\d+):([\d.]+)',text)
                if match: duration=int(match[1])*3600+int(match[2])*60+float(match[3])
                markers=[]
                for match in re.finditer(r'Chapter #[^\n]*?start ([\d.]+), end ([\d.]+)(.*?)(?=\n\s*Chapter #|\n\s*Stream #|\Z)',text,re.S):
                    title=re.search(r'\btitle\s*:\s*([^\r\n]+)',match[3],re.I)
                    markers.append({'path':file,'start':float(match[1]),'end':float(match[2]),'duration':float(match[2])-float(match[1]),'title':title[1].strip() if title else f'Chapter {len(markers)+1}','embedded':True})
                tracks.extend(markers or [{'path':file,'title':Path(file).stem,'duration':duration}])
                if not b.get('cover') and m:
                    picture=None
                    if getattr(m,'pictures',None): picture=m.pictures[0].data
                    elif getattr(m,'tags',None):
                        pics=m.tags.getall('APIC') if hasattr(m.tags,'getall') else m.tags.get('covr',[])
                        if pics: picture=getattr(pics[0],'data',pics[0])
                    if picture and len(picture)<10*1024*1024:
                        target=Path(file).parent/'cover.jpg'; target.write_bytes(bytes(picture)); b['cover']=str(target)
            except Exception:
                logging.exception('Audio metadata'); tracks.extend(t for t in old if t.get('path')==file)
        if tracks:
            self.remap(b,tracks); b['chaptersVersion']=1
        return b
    def remap(self,b,tracks):
        old=b.get('tracks',[])
        def convert(chapter,position):
            track=old[min(int(chapter or 0),len(old)-1)] if old else {}
            absolute=float(track.get('start',0))+float(position or 0)
            candidates=[(i,t) for i,t in enumerate(tracks) if t.get('path')==track.get('path')]
            selected=next(((i,t) for i,t in reversed(candidates) if float(t.get('start',0))<=absolute),candidates[0] if candidates else (0,tracks[0]))
            return {'chapter':selected[0],'position':max(0,absolute-float(selected[1].get('start',0)))}
        b.update(convert(b.get('chapter'),b.get('position')))
        for bookmark in b.get('bookmarks',[]): bookmark.update(convert(bookmark.get('chapter'),bookmark.get('position')))
        b['tracks']=tracks
    def add(self,items):
        for b in items:
            if not b or any(x['id']==b['id'] for x in self.store['books']): continue
            self.organize(b)
            if b['kind']=='Audio': self.metadata(b)
            self.store['books'].append(b)
        self.save(); return self.state()
    @staticmethod
    def entry_seconds(value):
        try:
            seconds=0
            for part in str(value or '').strip().split(':'): seconds=seconds*60+float(part)
            return max(0,int(seconds))
        except (TypeError,ValueError): return 0
    @staticmethod
    def usable_image(value):
        if not value: return False
        url=str(value.get('url','') if isinstance(value,dict) else value)
        kind=str(value.get('type','') if isinstance(value,dict) else '')
        if kind and not kind.startswith('image/'): return False
        return bool(url) and not FEED_NON_IMAGE.search(url)
    def parse_feed(self,f,raw):
        parsed=feedparser.parse(raw)
        if not parsed.entries and not parsed.feed.get('title'): raise ValueError('This address did not return an RSS or Atom feed.')
        base=f['url']
        def absolute(value):
            try: return urljoin(base,htmllib.unescape(str(value))) if value else ''
            except ValueError: return ''
        def pick_image(values):
            # WebView2's CSP only permits https images, and podcast feeds put audio files in media:content.
            def url_of(value): return value.get('url','') if isinstance(value,dict) else value
            candidates=[re.sub(r'^http://','https://',absolute(url_of(value))) for value in values if self.usable_image(value)]
            return next((value for value in candidates if not FEED_IMAGE_LOGO.search(value)),candidates[0] if candidates else '')
        entries=[]
        for i,e in enumerate(parsed.entries):
            content=next(iter(e.get('content',[])),{}).get('value') or e.get('summary','') or e.get('description','')
            content=str(content)
            link=absolute(e.get('link',''))
            if not link:
                alternative=next((x.get('href') for x in e.get('links',[]) if x.get('rel') in (None,'alternate') and x.get('type') in (None,'text/html') and x.get('href')),'')
                link=absolute(alternative)
            images=[]
            for key in ('media_content','media_thumbnail'):
                images.extend(item for item in e.get(key,[]) if isinstance(item,dict))
            images.append((e.get('image') or {}).get('href','') if isinstance(e.get('image'),dict) else '')
            image=pick_image(images)
            if not image:
                match=re.search(r'<img[^>]+src=["\']([^"\']+)',content,re.I)
                if match: image=pick_image([match[1]])
            audio=''; document=''
            for enclosure in e.get('enclosures',[]):
                url=absolute(enclosure.get('href','')); kind=str(enclosure.get('type',''))
                if not audio and (kind.startswith('audio/') or re.search(r'\.(mp3|m4a|m4b|ogg|opus|wav)(\?|$)',url,re.I)): audio=url
                elif not document and kind=='application/pdf': document=url
            stamp=e.get('published_parsed') or e.get('updated_parsed')
            date=time.strftime('%Y-%m-%dT%H:%M:%SZ',stamp) if stamp else str(e.get('published') or e.get('updated') or '')
            author=''
            if e.get('author_detail',{}).get('name'): author=e['author_detail']['name']
            elif e.get('authors'): author='; '.join(str(x.get('name','')) for x in e['authors'] if isinstance(x,dict) and x.get('name'))
            elif e.get('author'): author=str(e['author'])
            key=str(e.get('id') or link or e.get('title') or i)
            entries.append({'id':uid(f['id']+key),'feed':f['id'],'title':re.sub(r'\s+',' ',str(e.get('title') or 'Untitled'))[:1000],'link':link,'date':date,'content':content[:FEED_CONTENT_LIMIT],'summary':plain_text(content)[:600],'audio':audio,'document':document,'image':image,'duration':self.entry_seconds(e.get('itunes_duration','')),'author':author[:300],'rights':str(e.get('rights') or e.get('copyright') or '')[:300],'_date':calendar.timegm(stamp) if stamp else 0})
        entries.sort(key=lambda e:e['_date'],reverse=True)
        seen=set(); unique=[]
        for e in entries:
            if e['id'] in seen: continue
            seen.add(e['id']); unique.append(e)
        limit=50 if f.get('kind')=='Podcasts' else 20
        kept=[]; characters=0
        for e in unique:
            if kept and (len(kept)>=limit or characters+len(e['content'])+len(e['title'])>FEED_CONTENT_LIMIT): break
            kept.append(e); characters+=len(e['content'])+len(e['title'])
        for e in kept: e.pop('_date',None)
        feed_image=pick_image([(parsed.feed.get('image') or {}).get('href','') if isinstance(parsed.feed.get('image'),dict) else ''])
        for e in kept:
            if not e['image']: e['image']=feed_image
        return {**f,'title':f.get('title') or parsed.feed.get('title') or 'Source','image':feed_image or f.get('image',''),'description':str(parsed.feed.get('subtitle') or '')[:1000],'entries':kept,'updated':now(),'lastAttempt':now(),'refreshError':None}
    def refresh(self,id):
        f=next(f for f in self.store['feeds'] if f['id']==id)
        try:
            raw,_=fetch(f['url'],max_bytes=FEED_FETCH_LIMIT)
            fresh=self.parse_feed(f,raw)
            if not fresh['entries'] and f.get('entries'):
                fresh['entries']=f['entries']
                fresh['refreshError']='Publisher returned no entries; showing saved stories.'
            with self.lock:
                f.update(fresh)
                self.save_feed_cache(f); self.save()
            return copy.deepcopy(f)
        except Exception as e:
            f['lastAttempt']=now(); f['refreshError']=str(e) or type(e).__name__
            with self.lock: self.save_feed_cache(f); self.save()
            raise
    def cache(self,folder,id,value=None):
        self.book(id); file=self.data/folder/(id+'.json')
        if value is None: return json.loads(file.read_text(encoding='utf-8')) if file.exists() else {}
        if len(json.dumps(value))>12*1024*1024: raise ValueError('Cache limit reached.')
        atomic(file,value); return True
    def start_scan(self,id):
        b=self.book(id); files=list(dict.fromkeys(t['path'] for t in b.get('tracks',[]) if t.get('path')))
        if not files: raise ValueError('Choose a local audiobook to scan.')
        token=uuid.uuid4().hex; self.scans[token]={'files':files,'index':0,'decoder':None,'samples':0,'lock':threading.Lock()}
        return {'id':token,'files':[{'index':i,'title':Path(f).stem,'duration':max(t.get('end',t.get('duration',0)) for t in b['tracks'] if t.get('path')==f)} for i,f in enumerate(files)]}
    def read_scan(self,id):
        s=self.scans[id]
        with s['lock']:
            if s['index']>=len(s['files']): return {'done':True}
            if not s['decoder']:
                s['decoder']=subprocess.Popen([str(self.ffmpeg),'-nostdin','-hide_banner','-loglevel','error','-i',s['files'][s['index']],'-vn','-ac','1','-ar','16000','-f','f32le','pipe:1'],stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,creationflags=0x08000000)
                s['samples']=0
            raw=s['decoder'].stdout.read(65536)
            if raw:
                s['samples']+=len(raw)//4
                return {'fileIndex':s['index'],'pcm':list(raw),'seconds':s['samples']/16000}
            code=s['decoder'].wait(); s['decoder'].stdout.close(); s['decoder']=None
            if code: raise ValueError('Audio decoding failed.')
            result={'fileDone':True,'fileIndex':s['index'],'seconds':s['samples']/16000}; s['index']+=1; return result
    def cancel_scan(self,id):
        s=self.scans.pop(id,None)
        if s and s['decoder']: s['decoder'].kill(); s['decoder'].wait(); s['decoder'].stdout.close()
        return True
    def apply_chapters(self,id,markers):
        b=self.book(id); tracks=[]
        if len(markers)>3000: raise ValueError('Too many chapters.')
        for i,file in enumerate(dict.fromkeys(t['path'] for t in b['tracks'])):
            old=[t for t in b['tracks'] if t['path']==file]; duration=max(t.get('end',t.get('duration',0)) for t in old)
            raw=sorted([m for m in markers if m.get('fileIndex')==i and 0<=float(m['start'])<duration],key=lambda m:float(m['start']))
            unique=[]
            for m in raw:
                if not unique or float(m['start'])-float(unique[-1]['start'])>2: unique.append(m)
            if unique:
                if float(unique[0]['start'])>2: unique.insert(0,{'start':0,'title':'Opening'})
                for j,m in enumerate(unique):
                    end=float(unique[j+1]['start']) if j+1<len(unique) else duration; start=float(m['start'])
                    tracks.append({'path':file,'start':start,'end':end,'duration':end-start,'title':str(m.get('title','Chapter'))[:200],'spoken':True})
            else: tracks.extend(old)
        self.remap(b,tracks); b['chaptersVersion']=1; self.save(); return self.view(b)

    def downloads(self):
        out=[]
        with self.lock:
            for j in self.store['downloads']:
                h=self.handles.get(j['id']); s=h.status() if h and h.is_valid() else None
                out.append({'id':j['id'],'title':j['title'],'status':j['status'],'error':j.get('error'),'progress':1 if j['status']=='Complete' else s.progress if s else j.get('progress',0),'speed':s.download_rate if s else 0,'peers':s.num_peers if s else 0,'downloaded':s.total_done if s else 0,'total':s.total_wanted if s else 0})
        return out
    def start_torrent(self,j):
        import libtorrent as lt
        if not self.torrent: self.torrent=lt.session({'listen_interfaces':'0.0.0.0:6881','enable_dht':True,'enable_lsd':False,'enable_upnp':False,'enable_natpmp':False})
        params=lt.parse_magnet_uri(j['magnet']); params.save_path=j['dir']; params.flags &= ~lt.torrent_flags.paused; params.flags &= ~lt.torrent_flags.auto_managed
        self.handles[j['id']]=self.torrent.add_torrent(params); j['status']='Finding peers'
    def download_add(self,value):
        import libtorrent as lt
        magnet=str(value).strip().replace('&amp;','&'); lt.parse_magnet_uri(magnet)
        id=uid(magnet)
        if any(j['id']==id for j in self.store['downloads']): return self.downloads()
        title=parse_qs(urlparse(magnet).query).get('dn',['New download'])[0]
        j={'id':id,'magnet':magnet,'dir':str(self.folder(title)),'title':title,'status':'Finding peers'}
        with self.lock: self.store['downloads'].append(j); self.save()
        self.start_torrent(j); return self.downloads()
    def download_action(self,id,action):
        j=next(j for j in self.store['downloads'] if j['id']==id); h=self.handles.get(id)
        if action=='open': os.startfile(j['dir'])
        elif action=='pause':
            if h: h.pause()
            j['status']='Paused'
        elif action=='resume':
            if h: h.resume(); j['status']='Downloading'
            else: self.start_torrent(j)
        elif action=='remove':
            if h: self.torrent.remove_torrent(h); self.handles.pop(id,None)
            self.store['downloads'].remove(j)
        else: raise ValueError('Unknown download action.')
        self.save(); return self.downloads()
    def download_loop(self):
        while not self.stopping.wait(1.5):
            for j in list(self.store['downloads']):
                h=self.handles.get(j['id'])
                if not h or j['status'] in ('Paused','Complete','Error','Importing'): continue
                try:
                    s=h.status()
                    if s.errc.value(): raise ValueError(s.errc.message())
                    if s.has_metadata:
                        j['title']=s.name; j['status']='Downloading'; j['progress']=s.progress
                    if s.is_seeding:
                        j['status']='Importing'; h.pause(); self.torrent.remove_torrent(h); self.handles.pop(j['id'],None)
                        previous=Path(j['dir'])
                        if previous.name!=name(j['title']):
                            target=self.folder(j['title']); target.rmdir(); previous.rename(target); j['dir']=str(target)
                        with self.lock:
                            self.add(self.scan_folder(j['dir'])); j['status']='Complete'; self.save()
                except Exception as e:
                    logging.exception('Download'); j['status']='Error'; j['error']=str(e); self.save()

    def invoke(self,method,args):
        try:
            if not self.window or self.window.get_current_url()!=self.origin+'/ui/index.html': raise ValueError('Access denied')
            return {'ok':True,'value':self.dispatch(method,*args)}
        except Exception as e:
            logging.exception('API %s',method)
            return {'ok':False,'error':str(e) or type(e).__name__}
    def dispatch(self,method,*args):
        import webview
        if method=='load': return self.state()
        if method in ('importFiles','importFolder'):
            folder=method=='importFolder'; kind=args[0] if args else 'All'
            kindle_ext=';'.join('*'+e for e in sorted(kindle.KINDLE_EXTS))
            ext='*.epub' if kind=='EPUB' else '*.pdf' if kind=='PDF' else kindle_ext if kind=='Kindle' else ';'.join('*'+e for e in sorted(AUDIO)) if kind=='Audio' else '*.epub;*.pdf;'+kindle_ext+';'+';'.join('*'+e for e in sorted(AUDIO))
            selected=self.window.create_file_dialog(webview.FOLDER_DIALOG if folder else webview.OPEN_DIALOG,allow_multiple=not folder,file_types=(f'Books and audio ({ext})',))
            if not selected: return None
            with self.lock: return self.add(self.scan_folder(selected[0]) if folder else [self.new_book(p) for p in selected])
        if method=='updateBook':
            b=self.book(args[0]); patch=args[1]
            for k in ('position','progress','chapter','page','speed'):
                v=patch.get(k)
                if isinstance(v,(int,float)) and 0<=v<1e15: b[k]=v
            if isinstance(patch.get('cfi'),str): b['cfi']=patch['cfi'][:4096]
            if isinstance(patch.get('title'),str): b['title']=name(patch['title'])
            if isinstance(patch.get('author'),str): b['author']=patch['author'][:300]
            for k in ('highlights','bookmarks'):
                if isinstance(patch.get(k),list): b[k]=patch[k][:2000]
            b['lastActive']=now(); self.save(); return self.view(b)
        if method in ('removeBook','deleteBook'):
            b=self.book(args[0])
            if method=='deleteBook':
                if not self.window.create_confirmation_dialog('Move to Recycle Bin?',f'Move the files for {b["title"]} to the Recycle Bin?'): return None
                from send2trash import send2trash
                for p in set([t.get('path') for t in b.get('tracks',[])]+[b.get('path')]):
                    if p and inside(p,self.booksdir) and not any(x['id']!=b['id'] and (x.get('path')==p or any(t.get('path')==p for t in x.get('tracks',[]))) for x in self.store['books']): send2trash(p)
            self.store['books'].remove(b); self.save(); return self.state()
        if method=='settings':
            for k,(lo,hi) in {'readerHeight':(6,60),'readerWidth':(8,60),'fontSize':(10,40),'lineHeight':(1,3),'margin':(0,100),'skip':(5,120),'volume':(0,1),'speed':(.5,3),'listenRate':(.5,2.5)}.items():
                v=args[0].get(k)
                if isinstance(v,(int,float)): self.store['settings'][k]=max(lo,min(hi,v))
            if args[0].get('listenSpeaker') in (0,1,2): self.store['settings']['listenSpeaker']=int(args[0]['listenSpeaker'])
            if isinstance(args[0].get('listenFollow'),bool): self.store['settings']['listenFollow']=args[0]['listenFollow']
            if args[0].get('theme') in ('light','dark','system'): self.store['settings']['theme']=args[0]['theme']
            topics=args[0].get('feedTopics')
            if isinstance(topics,dict):
                selection=self.store['settings'].setdefault('feedTopics',{})
                for kind in ('News','Journals'):
                    if isinstance(topics.get(kind),list): selection[kind]=[topic for topic in dict.fromkeys(str(x) for x in topics[kind]) if topic in FEED_TOPICS]
            order=args[0].get('feedOrder')
            if isinstance(order,dict):
                current=self.store['settings'].setdefault('feedOrder',{})
                for kind in ('News','Journals'):
                    if order.get(kind) in ('latest','popular'): current[kind]=order[kind]
            self.save(); return self.store['settings']
        if method=='feeds': return self.feeds_payload()
        if method=='feedRefresh': return self.refresh(args[0])
        if method=='feedAdd':
            kind,url=args[0],str(args[1] if len(args)>1 else '').strip()
            if kind not in FEED_KINDS: raise ValueError('Invalid category.')
            public_url(url)
            if any(f['kind']==kind and f['url']==url for f in self.store['feeds']): return self.feeds_payload()
            source=next((item for item in self.catalog if item.get('kind')==kind and item.get('url')==url),None)
            raw,_=fetch(url,max_bytes=FEED_FETCH_LIMIT)
            feed=self.parse_feed({'id':uid(kind+url),'kind':kind,'url':url},raw)
            if source:
                feed['title']=source.get('title') or feed['title']
                for key in ('tags','contentMode','policy','image','artist','website'):
                    if source.get(key) is not None: feed[key]=source[key]
            with self.lock:
                feed.setdefault('tags',[]); feed.setdefault('contentMode','open-access'); feed.setdefault('policy','')
                self.store['feeds'].append(feed); self.save_feed_cache(feed); self.save()
            return self.feeds_payload()
        if method=='feedRemove':
            feed=next((f for f in self.store['feeds'] if f['id']==args[0]),None)
            if feed:
                self.store['feeds']=[f for f in self.store['feeds'] if f['id']!=args[0]]
                try: self.feed_cache_file(feed['id']).unlink()
                except OSError: pass
                self.save()
            return self.feeds_payload()
        if method=='feedOpened': return self.feed_opened(args[0])
        if method=='article': return self.article(args[0])
        if method=='playEpisode':
            f=next(f for f in self.store['feeds'] if f['id']==args[0]); e=next(e for e in f['entries'] if e['id']==args[1]); public_url(e['audio'])
            b=next((b for b in self.store['books'] if b['id']==e['id']),None)
            if b is None:
                b={'id':e['id'],'title':e['title'],'author':f['title'],'kind':'Podcast','remoteCover':e.get('image') or f.get('image'),'tracks':[{'remote':e['audio'],'title':e['title']}],'chapter':0,'position':0,'progress':0,'bookmarks':[],'lastActive':0}; self.store['books'].append(b); self.save()
            self.feed_opened(e.get('audio') or e.get('link') or e['id'])
            return self.view(b)
        if method=='getInk': return self.cache('ink',args[0])
        if method=='saveInk': return self.cache('ink',*args)
        if method=='getTranscript': return self.cache('transcripts',args[0])
        if method=='saveTranscript': return self.cache('transcripts',*args)
        if method=='prepareAudio':
            b=self.book(args[0])
            if b['kind']=='Audio' and (len(args)>1 and args[1] or not b.get('chaptersVersion')): self.metadata(b); self.save()
            return self.view(b)
        if method=='listenPrepare': return self.listen.prepare(args[0])
        if method=='listenResume': return self.listen.resume()
        if method=='listenPosition': return self.listen.position(*args)
        if method=='listenSpeak': return self.listen.speak(*args)
        if method=='listenSave': return self.listen.save_position(*args)
        if method=='listenVoice': return self.listen.voice()
        if method=='listenVoiceDownload': return self.listen.download()
        if method=='chapterScanStart': return self.start_scan(args[0])
        if method=='chapterScanRead': return self.read_scan(args[0])
        if method=='chapterScanCancel': return self.cancel_scan(args[0])
        if method=='applySpokenChapters': return self.apply_chapters(*args)
        if method=='openURL':
            if urlparse(args[0]).scheme not in ('http','https'): raise ValueError('Only web links can be opened.')
            webbrowser.open(args[0]); return True
        if method=='openFiles': os.startfile(str(self.booksdir)); return True
        if method=='saveNote':
            n=args[0]; note={'id':n.get('id') or uuid.uuid4().hex,'title':str(n.get('title') or 'Untitled')[:300],'text':str(n.get('text',''))[:2000000],'drawing':n.get('drawing',[]) if len(json.dumps(n.get('drawing',[])))<4000000 else [],'updated':now()}
            previous=next((i for i,x in enumerate(self.store['notes']) if x['id']==note['id']),None)
            if previous is None: self.store['notes'].insert(0,note)
            else: self.store['notes'][previous]=note
            self.save(); return note
        if method=='deleteNote':
            self.store['notes']=[n for n in self.store['notes'] if n['id']!=args[0]]; self.save(); return self.store['notes']
        if method in ('exportNote','exportDrawing'):
            n=next(n for n in self.store['notes'] if n['id']==args[0]); drawing=method=='exportDrawing'
            file=self.window.create_file_dialog(webview.SAVE_DIALOG,save_filename=name(n['title'])+('.png' if drawing else '.txt'))
            if not file: return False
            file=file[0] if isinstance(file,(tuple,list)) else file
            if drawing:
                if not args[1].startswith('data:image/png;base64,') or len(args[1])>12000000: raise ValueError('Invalid drawing.')
                Path(file).write_bytes(base64.b64decode(args[1].split(',',1)[1]))
            else: Path(file).write_text(n['title']+'\n\n'+n['text'],encoding='utf-8')
            return True
        if method=='downloads': return self.downloads()
        if method=='downloadAdd': return self.download_add(args[0])
        if method=='downloadAction': return self.download_action(*args)
        if method=='kindleDetect':
            device=kindle.detect_device()
            self.kindle_device=device
            return {'device':device,'connected':device is not None}
        if method=='kindleScan':
            device=args[0] if args else self.kindle_device
            if not device: raise ValueError('No Kindle device detected.')
            self.kindle_device=device
            self.kindle_books=kindle.scan_device(device)
            return {'device':device,'books':self.kindle_books}
        if method=='kindleImport':
            ids=args[0]
            if not ids: raise ValueError('Select at least one book to import.')
            return kindle.import_books(self,self.kindle_books,ids)
        if method=='kindleExport':
            ids=args[0]
            device=args[1] if len(args)>1 else self.kindle_device
            if not device:
                device=kindle.detect_device()
                if not device: raise ValueError('No Kindle device detected. Connect your Kindle and try again.')
            return kindle.export_to_device(self,ids,device)
        if method=='kindleDeleteDeviceBook':
            id=args[0]
            kindle.delete_device_book(self.kindle_books,id)
            self.kindle_books=[x for x in self.kindle_books if x['id']!=id]
            return {'device':self.kindle_device,'books':self.kindle_books}
        if method=='kindleDeleteDeviceBooks':
            ids=args[0]
            if not ids: raise ValueError('Select at least one book to remove.')
            for id in ids: kindle.delete_device_book(self.kindle_books,id)
            self.kindle_books=[x for x in self.kindle_books if x['id'] not in ids]
            return {'device':self.kindle_device,'books':self.kindle_books}
        if method=='kindleAddPDF':
            device=args[0] if args else self.kindle_device
            if not device: raise ValueError('No Kindle device detected.')
            selected=self.window.create_file_dialog(webview.OPEN_DIALOG,allow_multiple=True,file_types=('PDF books (*.pdf)',))
            if not selected: return None
            items=[b for b in (self.new_book(p) for p in selected) if b and b['kind']=='PDF']
            if not items: raise ValueError('Choose PDF files to send.')
            with self.lock: state=self.add(items)
            result=kindle.export_to_device(self,[b['id'] for b in items],device)
            return {'state':state,'result':result}
        if method=='kindleConvert':
            return kindle.convert_book(self,self.book(args[0]))
        if method=='kindleCover':
            path=args[0]
            if not any(b.get('path')==path for b in self.kindle_books): return None
            try: data,mime=kindle.book_cover(path)
            except Exception:
                logging.exception('Kindle cover %s',path)
                return None
            if not data: return None
            return f'data:{mime};base64,{base64.b64encode(data).decode()}'
        if method=='kindleMediaUrl':
            path=args[0]
            if not any(b.get('path')==path for b in self.kindle_books): raise ValueError('That file is not on the connected Kindle.')
            return self.media_url(path)
        if method=='kindleUpdateMetadata':
            path,patch=args[0],args[1]
            if not any(b.get('path')==path for b in self.kindle_books): raise ValueError('That file is not on the connected Kindle.')
            kindle.write_device_metadata(path,patch)
            self.kindle_books=kindle.scan_device(self.kindle_device)
            return {'device':self.kindle_device,'books':self.kindle_books}
        if method=='bookCover':
            b=self.book(args[0])
            cover=b.get('cover')
            if isinstance(cover,str) and cover.lower().startswith(('http://','https://')): return cover
            # Books can share a folder, so a generic cover.jpg would leak between them.
            if cover and Path(cover).is_file() and sum(1 for x in self.store['books'] if x.get('cover')==cover)>1:
                cover=None; b['cover']=None
            if not cover or not Path(cover).is_file():
                data,mime=bookart.for_book(b)
                if (not data or not mime) and Path(b.get('path') or '').suffix.lower() in kindle.PARSE_EXTS:
                    try: data,mime=kindle.book_cover(b['path'])
                    except Exception: logging.exception('Book cover %s',b.get('path'))
                if not data or not mime: return None
                source=b.get('path')
                folder=Path(source).parent if source else Path(b.get('source') or self.booksdir)
                ext={'image/png':'png','image/webp':'webp','image/gif':'gif'}.get(mime,'jpg')
                target=folder/f"cover-{b['id']}.{ext}"
                try:
                    target.write_bytes(data); b['cover']=str(target); self.save(); cover=str(target)
                except OSError:
                    return f'data:{mime};base64,{base64.b64encode(data).decode()}'
            try: data=Path(cover).read_bytes()
            except OSError: return None
            suffix=Path(cover).suffix.lower()
            mime='image/png' if suffix=='.png' else 'image/webp' if suffix=='.webp' else 'image/gif' if suffix=='.gif' else 'image/jpeg'
            return f'data:{mime};base64,{base64.b64encode(data).decode()}'
        if method=='metadataLookup':
            return metadata.search(str(args[0] or ''))
        if method=='metadataCover':
            data,mime=metadata.cover(str(args[0]))
            return f'data:{mime};base64,{base64.b64encode(data).decode()}'
        if method=='updateBookMetadata':
            b=self.book(args[0]); patch=args[1]
            if isinstance(patch.get('title'),str): b['title']=name(patch['title'])
            if isinstance(patch.get('author'),str): b['author']=patch['author'][:300]
            if isinstance(patch.get('series'),str): b['series']=patch['series'][:200]
            if isinstance(patch.get('seriesIndex'),(int,float)): b['seriesIndex']=patch['seriesIndex']
            if isinstance(patch.get('publisher'),str): b['publisher']=patch['publisher'][:300]
            if isinstance(patch.get('isbn'),str): b['isbn']=patch['isbn'][:100]
            if isinstance(patch.get('subject'),str): b['subject']=patch['subject'][:300]
            if isinstance(patch.get('published'),str): b['published']=patch['published'][:40]
            if isinstance(patch.get('description'),str): b['description']=patch['description'][:2000]
            if patch.get('cover'):
                raw=patch['cover']
                if raw.startswith('data:'):
                    header,b64=raw.split(',',1)
                    ext='png' if 'png' in header else 'jpg'
                    cover_dir=Path(b.get('source',self.booksdir))
                    cover_dir.mkdir(parents=True,exist_ok=True)
                    cover_path=cover_dir/f"cover-{b['id']}.{ext}"
                    cover_path.write_bytes(base64.b64decode(b64))
                    b['cover']=str(cover_path)
            self.save(); return self.view(b)
        raise ValueError('Unknown API method.')
    def close(self):
        self.stopping.set()
        for id in list(self.scans): self.cancel_scan(id)
        self.listen.close()
        if self.torrent: self.torrent.pause()
        self.save()
