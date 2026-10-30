import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'python_vendor'),str(ROOT/'python_app')]
from core import Services, inside, public_url
from host import Server
import listen
import requests

class BackendTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(dir=ROOT/'test-output'); self.data=Path(self.temp.name)/'Data'; self.s=Services(ROOT,self.data)
    def tearDown(self): self.s.close(); self.temp.cleanup()
    def test_import_chapters_and_resume(self):
        source=next((ROOT/'test-output').glob('audio-*/Chapter Test Book.m4b'))
        state=self.s.add([self.s.new_book(source)]); b=self.s.store['books'][0]
        self.assertTrue(source.is_file()); self.assertTrue(inside(b['tracks'][0]['path'],self.s.booksdir))
        self.assertGreater(len(b['tracks']),1)
        self.assertIn('chapter',b['tracks'][0]['title'].lower())
        b['chapter']=1; b['position']=.5; b['bookmarks']=[{'chapter':1,'position':.5,'name':'Resume'}]
        old_absolute=b['tracks'][1]['start']+.5
        self.s.metadata(b)
        self.assertAlmostEqual(b['tracks'][b['chapter']]['start']+b['position'],old_absolute)
        self.s.save(); self.assertEqual(json.loads(self.s.file.read_text(encoding='utf-8'))['books'][0]['position'],b['position'])
        scan=self.s.start_scan(b['id']); chunk=self.s.read_scan(scan['id'])
        self.assertGreater(len(chunk['pcm']),0); self.assertEqual(len(chunk['pcm'])%4,0); self.s.cancel_scan(scan['id'])
    def test_feed_newest_before_limit_and_refresh(self):
        import datetime
        base=datetime.datetime(2020,1,1,tzinfo=datetime.timezone.utc)
        items=''.join(f'<item><guid>{i}</guid><title>Story {i}</title><pubDate>{(base+datetime.timedelta(days=i)).strftime("%a, %d %b %Y %H:%M:%S GMT")}</pubDate></item>' for i in range(350))
        raw=f'<rss version="2.0"><channel><title>Live feed</title>{items}</channel></rss>'.encode()
        f={'id':'unitfeed','kind':'News','url':'https://example.com/rss'}; self.s.store['feeds']=[f]
        with patch('core.fetch',return_value=(raw,f['url'])): result=self.s.refresh(f['id'])
        self.assertEqual(len(result['entries']),300); self.assertEqual(result['entries'][0]['title'],'Story 349'); self.assertIsNone(result['refreshError'])
        with patch('core.fetch',side_effect=ValueError('Offline')):
            with self.assertRaises(ValueError): self.s.refresh(f['id'])
        self.assertEqual(f['refreshError'],'Offline'); self.assertEqual(len(f['entries']),300)
    def test_media_range_and_capability(self):
        import threading
        server=Server(self.s); self.s.origin=f'http://127.0.0.1:{server.server_port}'; threading.Thread(target=server.serve_forever,daemon=True).start()
        try:
            file=Path(self.temp.name)/'audio.wav'; file.write_bytes(bytes(range(256))*4); url=self.s.media_url(str(file))
            r=requests.get(url,headers={'Range':'bytes=100-199'},timeout=5); self.assertEqual(r.status_code,206); self.assertEqual(r.content,file.read_bytes()[100:200]); self.assertEqual(r.headers['Content-Range'],'bytes 100-199/1024')
            self.assertEqual(requests.get(self.s.origin+'/media/unknown',timeout=5).status_code,404)
            self.assertEqual(requests.get(self.s.origin+'/python_app/core.py',timeout=5).status_code,404)
            self.assertEqual(requests.get(url,headers={'Host':'attacker.example'},timeout=5).status_code,403)
        finally: server.shutdown(); server.server_close()
    def test_torrent_engine(self):
        import libtorrent as lt
        session=lt.session({'enable_dht':False,'enable_lsd':False,'enable_upnp':False,'enable_natpmp':False,'listen_interfaces':'127.0.0.1:0'})
        params=lt.parse_magnet_uri('magnet:?xt=urn:btih:'+'a'*40+'&dn=Actual+Book+Name'); params.save_path=str(self.s.folder('Actual Book Name'))
        h=session.add_torrent(params); self.assertEqual(h.status().errc.value(),0); self.assertTrue(h.is_valid()); h.pause(); session.remove_torrent(h)
    def test_private_urls_rejected(self):
        for url in ('http://127.0.0.1/a','file:///C:/Windows/win.ini','http://[::1]/'):
            with self.assertRaises(ValueError): public_url(url)
    def test_live_feeds_have_no_offline_entries(self):
        self.assertTrue(self.s.store['feeds'])
        self.assertTrue(all(not f['entries'] for f in self.s.store['feeds']))
        self.s.store['feeds'][0]['entries']=[{'title':'Fetched article'}]
        self.s.save()
        disk=json.loads(self.s.file.read_text(encoding='utf-8'))
        self.assertTrue(all('entries' not in f for f in disk['feeds']))
        self.assertEqual(self.s.store['feeds'][0]['entries'][0]['title'],'Fetched article')
    def test_publisher_rejection_is_explicit(self):
        response=requests.Response(); response.status_code=403
        error=requests.HTTPError('Forbidden',response=response)
        with patch('core.fetch',side_effect=error): result=self.s.dispatch('article','https://example.com/article')
        self.assertEqual(result['availability'],'publisher-blocked')
        self.assertEqual(result['status'],403)
        self.assertIsNone(result['content'])
    def test_narration_text_utilities(self):
        self.assertEqual(listen.spoken('Mr. Smith read Chapter IV.'),'Mister Smith read Chapter four.')
        self.assertEqual(listen.spoken('Book 12 begins.'),'Book twelve begins.')
        self.assertEqual(listen.clean('hyphen-\nated\ttabs\r\n\r\n\r\nend'),'hyphenated tabs\n\nend')
        text='Mr. Smith paid 1.50 dollars. He left.'
        ranges=listen.sentence_ranges(text,0,len(text))
        self.assertEqual(len(ranges),2)
        self.assertEqual(text[ranges[0][0]:ranges[0][1]],'Mr. Smith paid 1.50 dollars.')
        text='one two three four five'
        self.assertEqual(listen.skip_words(text,0,2),text.index('three'))
        self.assertEqual(listen.skip_words(text,0,-1),0)
        self.assertEqual(listen.skip_words(text,text.index('five'),-2),text.index('three'))
        self.assertEqual(listen.skip_words(text,len(text),9),len(text))
        self.assertEqual(listen.word_start(text,text.index('three')+2),text.index('three'))
    def test_narration_passages_cover_every_character(self):
        text='Alpha beta gamma delta. '*40
        sentences=listen.sentence_ranges(text,0,len(text))
        parts=listen.passages(text,sentences)
        self.assertLessEqual(parts[0][1]-parts[0][0],160)
        self.assertEqual(parts[0][0],sentences[0][0])
        self.assertEqual(parts[-1][1],sentences[-1][1])
        for (a,b),(c,d) in zip(parts,parts[1:]):
            self.assertGreaterEqual(c,b)
            self.assertEqual(text[b:c].strip(),'')
            self.assertLessEqual(d-c,600)
        wordy='word '*600
        long=listen.passages(wordy,[[0,len(wordy)-1]])
        self.assertGreater(len(long),1)
        self.assertTrue(all(0<=d-c<=listen.MAX_SPAN for c,d in long))
        self.assertEqual(''.join(wordy[c:d] for c,d in long).replace(' ',''),'word'*600)
    def test_narration_prepare_positions_and_resume(self):
        doc=self.s.listen.prepare({'bookId':'book1','key':'unit:book','title':' Unit  Book ','chapters':[{'label':'One','text':'Mr. Smith went home. Chapter IV begins here.\n\nHe slept.'},{'label':'Two','text':'Second chapter text.'}]})
        self.assertEqual(doc['title'],'Unit Book'); self.assertEqual(len(doc['chapters']),2)
        self.assertTrue(all(c['sentences'] and c['passages'] for c in doc['chapters']))
        self.assertFalse(doc['truncated']); self.assertFalse(doc['voice']['installed'])
        self.assertEqual(doc['chapters'][1]['start'],doc['chapters'][0]['end']+2)
        self.assertEqual(self.s.dispatch('listenPosition',doc['id'],0,1)['position'],doc['text'].index('Smith'))
        self.s.dispatch('listenSave',doc['id'],12)
        self.assertEqual(self.s.listen.resume()['position'],12)
        other=self.s.listen.prepare({'bookId':'book2','key':'unit:book:2','chapters':[{'text':'A different reading.'}]})
        self.assertNotEqual(other['id'],doc['id'])
        self.assertEqual(self.s.listen.resume()['id'],doc['id'])
        self.s.dispatch('listenSave',other['id'],3)
        self.assertEqual(self.s.listen.resume()['id'],other['id'])
        with self.assertRaises(ValueError): self.s.listen.prepare({'key':'unit:empty','chapters':[{'text':'   '}]})
        with self.assertRaises(ValueError): self.s.listen.load('../progress')
    def test_narration_speech_cache_and_voice_state(self):
        class Engine:
            def __init__(self): self.calls=0
            def generate(self,text,sid=0,speed=1.0):
                self.calls+=1
                class Result: samples=[.1,-.1]*2400
                return Result()
        doc=self.s.listen.prepare({'bookId':'book1','key':'unit:speech','chapters':[{'text':'A short chapter to read aloud. Second sentence follows.'}]})
        chapter=doc['chapters'][0]; start,end=chapter['sentences'][0]; engine=Engine()
        self.s.listen._load_engine=lambda:(engine,24000)
        first=self.s.dispatch('listenSpeak',doc['id'],start,end,1.0,1)
        self.assertEqual(engine.calls,1); self.assertGreater(first['seconds'],0)
        self.assertTrue(inside(self.s.media[first['url'].split('/media/')[1]],self.s.listen.audio))
        cached=self.s.dispatch('listenSpeak',doc['id'],start,end,1.0,1)
        self.assertEqual(engine.calls,1); self.assertEqual(cached['url'],first['url'])
        self.s.dispatch('listenSpeak',doc['id'],start,end,1.0,0)
        self.assertEqual(engine.calls,2)
        deep=self.s.dispatch('listenSpeak',doc['id'],start,end,1.0,2)
        self.assertEqual(engine.calls,3); self.assertNotEqual(deep['url'],first['url'])
        self.assertEqual(deep['speaker'],2)
        voice=self.s.listen.voice()
        self.assertEqual([s['id'] for s in voice['speakers']],[1,0,2])
        self.assertEqual(self.s.dispatch('settings',{'listenSpeaker':2})['listenSpeaker'],2)
        self.assertEqual(self.s.dispatch('settings',{'listenSpeaker':7})['listenSpeaker'],2)
        self.assertFalse(self.s.dispatch('listenVoice')['installed'])
        with patch('requests.get') as get, patch('listen.logging.exception'):
            class Response:
                headers={'content-length':'4'}
                def __enter__(self): return self
                def __exit__(self,*args): return False
                def raise_for_status(self): pass
                def iter_content(self,size): return iter([b'junk'])
            get.return_value=Response(); self.s.listen._download()
        self.assertTrue(self.s.listen.voice()['error'])
        self.assertFalse(self.s.listen.installed())

if __name__=='__main__': unittest.main(verbosity=2)
