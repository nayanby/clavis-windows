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
    files=['manifest.json','background.js','capture.js','page-toolbar.js','exporter.html','exporter.css','exporter.js','word-export.js','README.md','THIRD_PARTY_NOTICES.txt','artifact.md','template/base.docx','template/profile.json','vendor/jszip.min.js']
    files += ['vendor/html2canvas.min.js','vendor/html2canvas.LICENSE.txt']
    files += [f'icons/{size}.png' for size in (16,32,48,128)]
    manifest=json.loads((SOURCE/'manifest.json').read_text())
    assert manifest['manifest_version']==3
    assert '<all_urls>' not in manifest.get('host_permissions',[])
    assert not any(p in manifest['permissions'] for p in ('cookies','history','debugger','nativeMessaging'))
    for script in manifest['content_scripts']:
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
