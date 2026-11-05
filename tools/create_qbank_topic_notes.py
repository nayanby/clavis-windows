"""Create standalone topic-note HTML from imported explanations, with an authored achalasia example."""
import html,json,re
from collections import OrderedDict
from pathlib import Path
import lxml.html as LH
from import_replacement_html_archives import OUT,REPO,clean
DEST=REPO/'build/qbank-topic-notes'
CSS='''body{margin:0;background:#f5f4fa;color:#242348;font:17px/1.45 "Averia Serif Libre",Georgia,serif}main{max-width:940px;margin:auto;padding:32px 24px 80px}h1{font-size:30px}h2{font-size:19px;line-height:1.2;background:#f8dfeb;padding:12px;border-radius:9px;margin-top:28px}h3{font-size:17px;color:#24568c;line-height:1.2}p{margin:0 0 8px}section{background:white;border:1px solid #ddddec;border-radius:12px;padding:20px;margin:14px 0}table{width:100%;border-collapse:collapse;font-size:16px}th,td{border:1px solid #d6d9e6;padding:9px;text-align:left;vertical-align:top}th{background:#ecf1fa}li{margin:5px 0}a{color:#24568c}.meta{font:14px/1.5 Aptos,Arial,sans-serif;color:#676780}.key{border-left:4px solid #9679b3;padding:12px;background:#f4eff9}nav{background:#eeedf7;padding:14px;border-radius:10px}details{margin:10px 0}summary{cursor:pointer;font-weight:bold}@media(max-width:650px){main{padding:16px}table{display:block;overflow:auto}}@media print{body{background:white}main{max-width:none;padding:0}section{break-inside:avoid}nav{display:none}}'''
def page(title,body):return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(title)+'</title><style>'+CSS+'</style></head><body><main><h1>'+html.escape(title)+'</h1>'+body+'</main></body></html>'
def make():
    manifest=json.loads((OUT/'staging-report.json').read_text(encoding='utf-8'));links=[];topiccount=0
    for path in manifest['stagedFiles']:
        b=json.loads(Path(path).read_text(encoding='utf-8'));groups=OrderedDict()
        for q in b['questions']:
            source=q.get('sourceQuestion',{});label=source.get('topic') or source.get('focus') or source.get('title') or source.get('chapter') or b['headingText']
            groups.setdefault(str(label),[]).append(q)
        sections=[];outline=[]
        for i,(label,qs) in enumerate(groups.items(),1):
            topiccount+=1;outline.append(f'<li><a href="#t{i}">'+html.escape(label)+'</a></li>');chunks=[];seen=set()
            for q in qs:
                doc=LH.fragment_fromstring(q['explanationHtml'],create_parent='div')
                for p in list(doc.xpath('.//p')):
                    if re.match(r'^\s*(?:The )?correct (?:choice|answer)\s*(?:is|:)',p.text_content(),re.I):p.drop_tree()
                value=clean(''.join(LH.tostring(x,encoding='unicode') for x in doc))
                value=re.sub(r'NEET[\s–—-]*SS\s*(?:application)?\s*:?', 'Key application',value,flags=re.I)
                norm=re.sub(r'\W+','',LH.fragment_fromstring(value,create_parent='div').text_content()).lower()
                if norm in seen:continue
                seen.add(norm);chunks.append(value)
            sections.append(f'<section id="t{i}"><h2>'+html.escape(label)+'</h2>'+''.join(chunks)+'</section>')
        name=re.sub(r'[^\w -]','',b['headingText'])+'.html';dest=DEST/b['folder']/name;dest.parent.mkdir(parents=True,exist_ok=True)
        body='<p class="meta">Topic revision notes extracted from the supplied Qbank explanations. Source-derived draft; not independently medically reviewed.</p><nav><strong>Topics</strong><ol>'+''.join(outline)+'</ol></nav>'+''.join(sections)
        dest.write_text(page(b['headingText'],body),encoding='utf-8');links.append((b['folder'],b['headingText'],dest.relative_to(DEST).as_posix()))
    sample=DEST/'Example - Achalasia.html'
    sample.write_text(page('Achalasia · High-yield notes',SAMPLE),encoding='utf-8')
    index='<p class="meta">'+str(len(links))+' Qbank note files. The achalasia example is separately authored and reference-checked; other files preserve imported explanation content.</p><p><a href="Example%20-%20Achalasia.html">Open the achalasia example</a></p>'
    for subject in sorted({a for a,_,_ in links}):
        index+='<h2>'+html.escape(subject)+'</h2><ul>'+''.join('<li><a href="'+html.escape(url,quote=True)+'">'+html.escape(title)+'</a></li>' for s,title,url in links if s==subject)+'</ul>'
    (DEST/'index.html').write_text(page('Qbank topic notes',index),encoding='utf-8')
    for p in DEST.rglob('*.html'):
        doc=LH.parse(str(p));assert doc.xpath('//h1') and not doc.xpath('//script|//iframe|//object')
    print(json.dumps(dict(noteFiles=len(links),topicGroups=topiccount,sourceQuestions=manifest['questions'],example=str(sample),index=str(DEST/'index.html'))))

SAMPLE='''<p class="meta">Gastroenterology → Esophageal disorders → Motility · Reference-checked 6 November 2026</p>
<p class="key"><strong>Core idea:</strong> Impaired esophagogastric junction relaxation plus absent normal peristalsis. Treatment reduces outflow resistance; it does not restore normal inhibitory neurons.</p>
<nav><a href="#recognize">Recognition</a> · <a href="#diagnose">Diagnosis</a> · <a href="#classify">Classification</a> · <a href="#treat">Treatment</a> · <a href="#traps">Pitfalls</a></nav>
<section id="recognize"><h2>Recognize the pattern</h2><ul><li><strong>Dysphagia to liquids and solids</strong>, often with regurgitation of retained food.<ul><li>Chest discomfort, nocturnal cough and weight loss can accompany it.</li><li>Marked weight loss or a short, rapidly progressive course—especially in an older patient—raises concern for pseudoachalasia.</li></ul></li></ul></section>
<section id="diagnose"><h2>Establish the diagnosis</h2><ul><li><strong>Upper endoscopy:</strong> assess for a mechanical lesion or malignant mimic.<ul><li>Retained saliva/food and a tight junction support suspicion; early disease can look less striking.</li></ul></li><li><strong>High-resolution manometry:</strong> defines the motor pattern.<ul><li>Interpret the integrated relaxation pressure (IRP) against the equipment- and position-specific normal range.</li></ul></li><li><strong>Timed barium esophagram or FLIP:</strong> provide supportive evidence when the manometric diagnosis is inconclusive.</li></ul></section>
<section id="classify"><h2>Chicago Classification v4.0</h2><table><thead><tr><th>Pattern</th><th>Key findings</th><th>Recall cue</th></tr></thead><tbody><tr><td>Type I</td><td>Abnormal median IRP; 100% failed peristalsis; no qualifying panesophageal pressurization</td><td>Failed, without pressure column</td></tr><tr><td>Type II</td><td>Abnormal median IRP; 100% failed peristalsis; panesophageal pressurization in ≥20% of swallows</td><td>Whole-esophagus pressure column</td></tr><tr><td>Type III</td><td>Abnormal median IRP; premature/spastic contractions in ≥20% of swallows; no normal peristalsis</td><td>Spastic pattern</td></tr><tr><td>Absent contractility</td><td>Normal median IRP in supine and upright positions; 100% failed peristalsis</td><td>Normal relaxation separates the pattern</td></tr></tbody></table><p><strong>Borderline IRP:</strong> do not dismiss possible achalasia solely on a near-normal value; integrate symptoms and supportive testing.</p></section>
<section id="treat"><h2>Choose treatment by subtype and fitness</h2><ul><li><strong>Types I/II:</strong> pneumatic dilation, laparoscopic Heller myotomy and POEM are established options.<ul><li>Choice depends on expertise, anatomy, durability, reflux risk and patient preference.</li></ul></li><li><strong>Type III:</strong> a tailored, sufficiently long myotomy addresses the spastic segment; POEM is particularly useful for this purpose.</li><li><strong>Unable to undergo definitive therapy:</strong> botulinum toxin can provide symptom relief, usually with limited durability.</li><li><strong>After treatment:</strong> assess persistent/recurrent symptoms and reflux; symptom relief alone does not settle the mechanism of recurrence.</li></ul></section>
<section id="traps"><h2>High-yield pitfalls</h2><ul><li><strong>EGJ outflow obstruction is not automatically achalasia:</strong> preserved peristalsis and the full diagnostic context matter.</li><li><strong>Type II threshold:</strong> qualifying pressurization in at least one fifth of swallows.</li><li><strong>Type III:</strong> premature contractions plus absent normal peristalsis; an isolated spastic swallow is insufficient.</li><li><strong>Reflux trade-off:</strong> discuss reflux after myotomy, particularly POEM, and plan appropriate management.</li></ul></section>
<section><h2>References</h2><ol><li><a href="https://pmc.ncbi.nlm.nih.gov/articles/8034247/">Yadlapati et al. Chicago Classification v4.0, 2021.</a></li><li><a href="https://gi.org/guideline/diagnosis-and-management-of-achalasia/">ACG Clinical Guideline: Diagnosis and Management of Achalasia.</a></li><li><a href="https://www.asge.org/docs/default-source/guidelines/asge-guideline-on-the-management-of-achalasia-2020-february-gie.pdf">ASGE Guideline on the Management of Achalasia, 2020.</a></li></ol></section>'''
if __name__=='__main__':make()
