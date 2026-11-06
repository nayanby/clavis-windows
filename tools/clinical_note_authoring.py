"""Shared layout for directly authored concise clinical module notes."""
import json,re
from html import escape
from lxml import html
from create_qbank_topic_notes import DEST,page
def T(headers,rows):
    return '<table><thead><tr>'+''.join('<th>'+escape(x)+'</th>' for x in headers.split('|'))+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+c.strip()+'</td>' for c in row.split('|'))+'</tr>' for row in rows.strip().splitlines())+'</tbody></table>'
def U(lines):return '<ul>'+''.join('<li>'+x.strip()+'</li>' for x in lines.strip().splitlines() if x.strip())+'</ul>'
def P(text):return '<p>'+text+'</p>'
def S(title,body):return (title,body)
def write(subject,title,sections,refs):
    nav='<nav><strong>Contents</strong><ol>'+''.join(f'<li><a href="#s{i}">{escape(t)}</a></li>' for i,(t,b) in enumerate(sections,1))+'<li><a href="#references">References</a></li></ol></nav>'
    body=nav+''.join(f'<section id="s{i}"><h2>{i} · {escape(t)}</h2>{b}</section>' for i,(t,b) in enumerate(sections,1))
    body+='<section id="references"><h2>References</h2><ol>'+''.join('<li><a href="'+escape(url,quote=True)+'">'+escape(label)+'</a></li>' for label,url in refs)+'</ol></section>'
    doc=html.fragment_fromstring(body,create_parent='div');assert doc.xpath('.//table') and len(refs)>=1
    assert all(len(row.xpath('./td'))==len(tab.xpath('./thead/tr/th')) for tab in doc.xpath('.//table') for row in tab.xpath('./tbody/tr'))
    dest=DEST/subject/(title+'.html');dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(page(title,body),encoding='utf-8')
    log=DEST/'authored-notes.json';records=json.loads(log.read_text(encoding='utf-8')) if log.exists() else {}
    records[subject+'/'+title]=dict(file=str(dest),sections=len(sections),tables=len(doc.xpath('.//table')),references=len(refs),words=len(doc.text_content().split()),status='authored_source_checked')
    log.write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8');print(subject+' / '+title+' completed')
