"""Run the actual Firefox add-on in a fresh, isolated WebDriver profile."""
import json
import base64
from zipfile import ZipFile
from lxml import etree as E
import os
from pathlib import Path
import socket
import subprocess
import time
import ssl
import threading
from http.server import HTTPServer,BaseHTTPRequestHandler
from datetime import datetime,timedelta,timezone
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes,serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from urllib.request import Request, urlopen
from urllib.error import HTTPError

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'build/firefox-integration'
OUT.mkdir(parents=True,exist_ok=True)

def main():
    assert (OUT/'geckodriver.exe').is_file(), 'Place Mozilla geckodriver in build/firefox-integration/geckodriver.exe'
    fixture=(ROOT/'chrome-extension/pearls-chat-word/tests/fixtures/chatgpt.html').read_text(encoding='utf-8')
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            data=fixture.encode();self.send_response(200);self.send_header('Content-Type','text/html; charset=utf-8');self.send_header('Content-Length',str(len(data)));self.end_headers();self.wfile.write(data)
        def log_message(self,*args):pass
    key=rsa.generate_private_key(public_exponent=65537,key_size=2048)
    name=x509.Name([x509.NameAttribute(NameOID.COMMON_NAME,'chatgpt.com')]);now=datetime.now(timezone.utc)
    cert=x509.CertificateBuilder().subject_name(name).issuer_name(name).public_key(key.public_key()).serial_number(x509.random_serial_number()).not_valid_before(now-timedelta(days=1)).not_valid_after(now+timedelta(days=1)).add_extension(x509.SubjectAlternativeName([x509.DNSName('chatgpt.com')]),False).sign(key,hashes.SHA256())
    cert_path=OUT/'test-certificate.pem';key_path=OUT/'test-key.pem'
    cert_path.write_bytes(cert.public_bytes(serialization.Encoding.PEM));key_path.write_bytes(key.private_bytes(serialization.Encoding.PEM,serialization.PrivateFormat.PKCS8,serialization.NoEncryption()))
    server=HTTPServer(('127.0.0.1',0),Handler);tls=ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER);tls.load_cert_chain(cert_path,key_path);server.socket=tls.wrap_socket(server.socket,server_side=True)
    threading.Thread(target=server.serve_forever,daemon=True).start()
    fixture_url=f'https://chatgpt.com:{server.server_port}/c/test-fixture'
    with socket.socket() as sock:
        sock.bind(('127.0.0.1',0));port=sock.getsockname()[1]
    log=(OUT/'geckodriver.log').open('w',encoding='utf-8')
    environment=dict(os.environ,MOZ_REMOTE_ALLOW_SYSTEM_ACCESS='1')
    proc=subprocess.Popen([str(OUT/'geckodriver.exe'),'--port',str(port),'--allow-system-access'],stdout=log,stderr=log,creationflags=subprocess.CREATE_NO_WINDOW,env=environment)
    base=f'http://127.0.0.1:{port}'
    session=None
    def request(method,path,data=None):
        raw=None if data is None else json.dumps(data).encode()
        try:
            with urlopen(Request(base+path,data=raw,method=method,headers={'Content-Type':'application/json'}),timeout=100) as response:result=json.load(response)
        except HTTPError as error:
            raise RuntimeError(error.read().decode()) from error
        value=result.get('value')
        if isinstance(value,dict) and value.get('error'):raise RuntimeError(json.dumps(value))
        return value
    try:
        for _ in range(80):
            try:request('GET','/status');break
            except Exception:time.sleep(.2)
        value=request('POST','/session',{'capabilities':{'alwaysMatch':{'browserName':'firefox','acceptInsecureCerts':True,'pageLoadStrategy':'eager','moz:firefoxOptions':{'binary':'C:/Program Files/Mozilla Firefox/firefox.exe','args':['-headless'],'prefs':{'browser.shell.checkDefaultBrowser':False,'browser.tabs.warnOnClose':False,'network.dns.localDomains':'chatgpt.com','network.trr.mode':5,'network.proxy.type':0}}}}})
        session=value['sessionId'];prefix='/session/'+session
        def command(method,path,data=None):return request(method,prefix+path,data)
        def js(script,args=None):return command('POST','/execute/sync',{'script':script,'args':args or []})
        def context(name):command('POST','/moz/context',{'context':name})
        print('Firefox',value['capabilities']['browserVersion'],flush=True)
        command('POST','/window/rect',{'width':1200,'height':900})
        command('POST','/timeouts',{'pageLoad':15000,'script':60000})
        addon=command('POST','/moz/addon/install',{'path':str(ROOT/'outputs/pearls-chat-word/firefox/Pearls Chat to Word Firefox.xpi'),'temporary':True})
        print('Installed isolated add-on',addon,flush=True)
        try:command('POST','/url',{'url':fixture_url})
        except Exception as error:print('Page load:',str(error)[:180],flush=True)
        print('Source URL',command('GET','/url'),flush=True)
        context('chrome')
        uuid=js("return JSON.parse(Services.prefs.getStringPref('extensions.webextensions.uuids'))[arguments[0]];",[addon])
        print('Extension uuid available',bool(uuid),flush=True)
        # Execute the real background API from its own extension page. No API mocks.
        context('content')
        command('POST','/window/new',{'type':'tab'})
        handles=command('GET','/window/handles');command('POST','/window',{'handle':handles[-1]})
        command('POST','/url',{'url':f'moz-extension://{uuid}/exporter.html'})
        script=(ROOT/'chrome-extension/pearls-chat-word/tests/firefox-integration.js').read_text(encoding='utf-8')
        result=command('POST','/execute/async',{'script':script,'args':[fixture]})
        docx=result.pop('docx',None)
        for i,image in enumerate(result.get('images',[])):
            png=image.pop('png',None)
            if png:(OUT/f'actual-image-{i+1}.png').write_bytes(base64.b64decode(png.split(',')[1]))
        print(json.dumps(result,ensure_ascii=True),flush=True)
        (OUT/'actual-firefox-result.json').write_text(json.dumps(result,indent=2))
        assert not result.get('error'),result.get('error')
        assert len(result['images'])==4 and all(image['data'] for image in result['images']), 'Firefox capture is incomplete'
        assert not result['warnings'],result['warnings']
        assert docx,'No Word bytes returned'
        path=OUT/'actual-firefox-export.docx';path.write_bytes(base64.b64decode(docx))
        with ZipFile(path) as package:
            xml=E.fromstring(package.read('word/document.xml'))
            assert len([name for name in package.namelist() if name.startswith('word/media/') and not name.endswith('/')])==4
            extents=xml.xpath('//*[local-name()="inline"]/*[local-name()="extent"]')
            assert len(extents)==4 and all(extent.get('cy')=='1440000' for extent in extents)
            assert b'Diagram capture failed' not in package.read('word/document.xml')
        print('PASS actual Firefox: image + HTML diagram + tall diagram + SVG embedded in Word at 4 cm without activeTab grant',flush=True)

    finally:
        if session:
            try:request('DELETE','/session/'+session)
            except Exception:pass
        proc.terminate();log.close();server.shutdown();server.server_close();key_path.unlink(missing_ok=True);cert_path.unlink(missing_ok=True)

if __name__=='__main__':main()
