"""Validate all module notes, rebuild the index and package the complete collection."""
import json,zipfile
from pathlib import Path
from urllib.parse import quote
from html import escape
from lxml import html
from create_qbank_topic_notes import DEST,page
from import_replacement_html_archives import OUT

def finalize():
    manifest=json.loads((OUT/'staging-report.json').read_text(encoding='utf-8'))
    banks=[json.loads(Path(p).read_text(encoding='utf-8')) for p in manifest['stagedFiles']]
    assert len(banks)==42
    records={};sections=0;tables=0;referencecount=0
    for bank in banks:
        key=bank['folder']+'/'+bank['headingText'];p=DEST/(key+'.html');assert p.is_file(),p
        doc=html.parse(str(p));text=doc.getroot().text_content()
        assert 'Source-derived draft' not in text and 'Topic revision notes extracted' not in text,key
        assert doc.xpath('//h1') and not doc.xpath('//script|//iframe|//object'),key
        ids=doc.xpath('//*[@id]/@id');assert len(ids)==len(set(ids)),key
        assert all(a[1:] in ids for a in doc.xpath('//a[starts-with(@href,"#")]/@href')),key
        ts=doc.xpath('//table');assert ts,key
        for t in ts:
            n=len(t.xpath('./thead/tr/th'));assert n>=2
            assert all(len(r.xpath('./td'))==n for r in t.xpath('./tbody/tr')),key
        refs=doc.xpath('//*[@id="references"]/ol/li')
        # The earlier acid–base note already has reference anchors; identify its final section.
        if not refs:refs=doc.xpath('//section[h2="References"]/ol/li')
        assert refs and all(r.xpath('./a[starts-with(@href,"https://")]') for r in refs),key
        count=len(text.split());assert count>=200,(key,count)
        ss=len(doc.xpath('//main/section'))-1;sections+=ss;tables+=len(ts);referencecount+=len(refs)
        records[key]=dict(file=str(p),sections=ss,tables=len(ts),references=len(refs),words=count,status='authored_source_checked',chapterOrder=bank['chapterOrder'])
    assert len(records)==42
    (DEST/'authored-notes.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
    body='<p>42 modules · Cardiology, GI &amp; pancreas, liver and nephrology</p><p><a href="Example%20-%20Achalasia.html">Achalasia example</a></p>'
    for subject in ['Cardiology','GI & pancreas','Liver','Nephrology']:
        chosen=sorted([b for b in banks if b['folder']==subject],key=lambda b:(b['chapterOrder'],b.get('topicOrder',1),b['headingText']))
        body+='<section><h2>'+escape(subject)+'</h2><ol>'+''.join('<li><a href="'+quote(b['folder']+'/'+b['headingText']+'.html')+'">'+escape(b['headingText'])+'</a></li>' for b in chosen)+'</ol></section>'
    (DEST/'index.html').write_text(page('High-yield clinical notes',body),encoding='utf-8')
    index=html.parse(str(DEST/'index.html'))
    from urllib.parse import unquote
    assert all((DEST/unquote(u)).is_file() for u in index.xpath('//a/@href'))
    package=DEST.parent/'High Yield Clinical Notes - Complete.zip'
    files=[DEST/'index.html',DEST/'Example - Achalasia.html']+[Path(r['file']) for r in records.values()]
    with zipfile.ZipFile(package,'w',zipfile.ZIP_DEFLATED) as z:
        for p in files:z.write(p,p.relative_to(DEST).as_posix())
    with zipfile.ZipFile(package) as z:
        assert len(z.namelist())==44 and z.testzip() is None
        assert all(z.read(p.relative_to(DEST).as_posix())==p.read_bytes() for p in files)
    report=dict(result='PASS',modules=42,sourceQuestions=manifest['questions'],subjects=4,clinicalSections=sections,tables=tables,referenceEntries=referencecount,
      internalLinks=True,indexLinks=True,allModulesAuthored=True,independentClinicianReview=False,zipVerified=True,package=str(package))
    (DEST/'completion-report.json').write_text(json.dumps(report,indent=2),encoding='utf-8');print(json.dumps(report,indent=2))

if __name__=='__main__':finalize()
