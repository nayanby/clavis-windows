"""Remove only the opening title from Word Pearls and their paired HTML notes."""
import argparse
import copy
import io
import json
import time
import zipfile
from pathlib import Path
from lxml import etree, html

W={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}


def without_word_title(raw):
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        original=archive.read('word/document.xml')
        tree=etree.fromstring(original)
        body=tree.find('w:body',W)
        title=body.find('w:p',W)
        if title is None or not title.xpath('./w:pPr/w:pStyle[@w:val="Title"]',namespaces=W):
            return raw,False
        before=[etree.tostring(node) for node in body if node is not title]
        body.remove(title)
        assert [etree.tostring(node) for node in body]==before
        changed=etree.tostring(tree,xml_declaration=True,encoding='UTF-8',standalone=True)
        buffer=io.BytesIO()
        with zipfile.ZipFile(buffer,'w') as target:
            for info in archive.infolist():
                target.writestr(copy.copy(info),changed if info.filename=='word/document.xml' else archive.read(info.filename))
        output=buffer.getvalue()
        with zipfile.ZipFile(io.BytesIO(output)) as check:
            assert check.testzip() is None
            for name in archive.namelist():
                if name!='word/document.xml':assert check.read(name)==archive.read(name)
        return output,True


def remove(root,apply=False):
    root=root.resolve();changes={};titles=0
    for word in sorted(root.rglob('*.docx')):
        if any(part.startswith(('.', '_','~$')) for part in word.relative_to(root).parts):continue
        raw=word.read_bytes();updated,changed=without_word_title(raw)
        if changed:changes[word]=(raw,updated);titles+=1
        paired=word.with_suffix('.html')
        if paired.is_file():
            original=paired.read_bytes();tree=html.fromstring(original.decode('utf-8'))
            heading=tree.xpath('//main/h1[1]')
            if heading:
                heading[0].drop_tree()
                changes[paired]=(original,html.tostring(tree,encoding='utf-8',method='html',doctype='<!doctype html>'))
    report=dict(wordTitlesRemoved=titles,filesChanged=len(changes))
    if not apply or not changes:return report
    backup=root/'_backups'/f'before-title-removal-{time.time_ns()}.zip'
    backup.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(backup,'x',zipfile.ZIP_DEFLATED) as archive:
        for path,(raw,_) in changes.items():archive.writestr(path.relative_to(root).as_posix(),raw)
    with zipfile.ZipFile(backup) as archive:
        assert all(archive.read(path.relative_to(root).as_posix())==raw for path,(raw,_) in changes.items())
    try:
        for path,(_,updated) in changes.items():
            assert path.resolve().is_relative_to(root)
            path.write_bytes(updated)
            assert path.read_bytes()==updated
    except Exception:
        for path,(raw,_) in changes.items():path.write_bytes(raw)
        raise
    report['backup']=str(backup)
    return report


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--root',type=Path,default=Path('C:/Users/ANT-PC/OneDrive/Cortex Windows/data/Pearls'))
    parser.add_argument('--apply',action='store_true')
    args=parser.parse_args()
    print(json.dumps(remove(args.root,args.apply),indent=2))
