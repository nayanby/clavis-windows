"""Import user-supplied HTML data without executing scripts; replace the active library."""
import argparse,copy,hashlib,html,json,re,sys,time,zipfile
from collections import Counter
from pathlib import Path
import lxml.html as LH
REPO=Path(__file__).resolve().parents[1];OUT=REPO/'build/html-archive-replacement';OUT.mkdir(parents=True,exist_ok=True)
sys.path.insert(0,str(REPO/'src'))
from cnl_desktop import study_packs,paths
INSTALL=Path('C:/Users/ANT-PC/OneDrive/Cortex Windows');DATA=INSTALL/'data'
ARCHIVES=['Nephrology_Final_Chapters.zip','Final_Chapter_Versions_Only.zip']

def clean(value):
    root=LH.fragment_fromstring(str(value),create_parent='div')
    for node in list(root.iterdescendants()):
        if node.tag in {'script','style','iframe','object','input','button','img','svg'}:node.drop_tree();continue
        if node.tag not in {'p','div','section','span','h1','h2','h3','h4','strong','b','em','i','u','ul','ol','li','table','thead','tbody','tr','th','td','br','sub','sup','a'}:node.drop_tag();continue
        for key in list(node.attrib):
            if key!='href' or not node.get(key,'').startswith(('https://','http://')):del node.attrib[key]
    return (root.text or '')+''.join(LH.tostring(x,encoding='unicode') for x in root)
def rich(value):return re.sub(r'\*\*(.*?)\*\*',r'<strong>\1</strong>',html.escape(str(value)))

def block(value):
    if value is None or value==[] or value=='':return ''
    if isinstance(value,str):return '<p>'+rich(value)+'</p>'
    if isinstance(value,dict):
        return ''.join('<h3>'+rich(k)+'</h3>'+block(v) for k,v in value.items())
    assert isinstance(value,list),type(value)
    # Named section plus nested content, recursively preserving all levels.
    if len(value)==2 and isinstance(value[0],str) and isinstance(value[1],list):return '<h3>'+rich(value[0])+'</h3>'+block(value[1])
    if all(isinstance(x,str) for x in value):return '<ul>'+''.join('<li>'+rich(x)+'</li>' for x in value)+'</ul>'
    if value and all(isinstance(x,list) and len(x)==2 and isinstance(x[0],str) and isinstance(x[1],list) for x in value):
        return '<ul>'+''.join('<li><strong>'+rich(x[0])+'</strong>'+block(x[1])+'</li>' for x in value)+'</ul>'
    return ''.join(block(x) for x in value)

def table(value):
    if not value:return ''
    caption=''
    if isinstance(value,dict):headers=value.get('headers',[]);rows=value.get('rows',[])
    elif isinstance(value[0],str):
        assert len(value)==3,value
        caption,headers,rows=value
        if rows and all(len(r)==len(headers)+1 for r in rows):headers=[caption,*headers];caption=''
    else:
        headers,*rows=value
        if len(rows)==1 and rows[0] and isinstance(rows[0][0],list):rows=rows[0]
    assert isinstance(headers,list) and all(isinstance(r,list) and len(r)==len(headers) for r in rows),(headers,rows)
    return ('<h3>'+rich(caption)+'</h3>' if caption else '')+'<table><thead><tr>'+''.join('<th>'+rich(x)+'</th>' for x in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+rich(x)+'</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table>'

def alternatives(value,options,answer):
    if not value:return ''
    if isinstance(value,str):return '<h3>Other Options</h3><p>'+rich(value)+'</p>'
    pairs=[]
    wrong=[i for i in range(len(options)) if i!=answer]
    if isinstance(value,dict):
        for key,reason in value.items():
            if str(key).isdigit():i=int(key);label=options[i];include=i!=answer
            else:label=str(key);include=label!=options[answer]
            if include and reason:pairs.append((label,reason))
    elif isinstance(value,list):
        for n,item in enumerate(value):
            if not item:continue
            if isinstance(item,str):
                i=n if len(value)==len(options) else wrong[n];pairs.append((options[i],item)) if i!=answer else None
            elif isinstance(item,list) and len(item)==2 and isinstance(item[0],int):
                i,reason=item
                if i!=answer:pairs.append((options[i],reason))
            elif isinstance(item,dict):
                label=item.get('option',item.get('label','Option'));reason=item.get('reason',item.get('why',item.get('explanation','')))
                pairs.append((label,reason))
            else:pairs.append(('Option',item))
    else:raise ValueError(type(value))
    return '<h3>Other Options</h3><ul>'+''.join('<li><strong>'+rich(a)+':</strong> '+(rich(b) if isinstance(b,str) else block(b))+'</li>' for a,b in pairs)+'</ul>'

def extract(text):
    doc=LH.fromstring(text)
    for script in doc.xpath('//script[@type="application/json"]'):
        v=json.loads(script.text or '')
        if isinstance(v,dict):v=v.get('questions',v.get('items'))
        if isinstance(v,list) and v:return v
    for m in re.finditer(r'(?:const|let|var)\s+\w+\s*=\s*(\[)',text):
        try:v,_=json.JSONDecoder().raw_decode(text[m.start(1):])
        except ValueError:continue
        if v and isinstance(v[0],dict) and any(k in v[0] for k in ['q','stem','question']):return v
    result=[]
    for section in doc.xpath('//section[starts-with(@id,"q")]'):
        headings=section.xpath('./h2');inputs=section.xpath('.//input[@type="radio"]');ex=section.xpath('.//div[starts-with(@id,"ans")]')
        if not headings or not inputs or not ex:continue
        key=re.search(r'check\(\s*\d+\s*,\s*(\d+)\s*\)',inputs[0].get('onchange',''));assert key is not None
        opts=[re.sub(r'^[A-D]\.\s*','',i.getparent().text_content().strip()) for i in inputs]
        result.append(dict(stem=re.sub(r'^Q\d+\.\s*','',headings[0].text_content()),options=opts,answer=int(key[1]),explanationHtml=LH.tostring(ex[0],encoding='unicode')))
    assert result,'No question data found';return result

def convert(item,digest,index):
    stem=item.get('stem',item.get('q',item.get('question')));opts=item.get('options',item.get('o',item.get('opts')))
    answer=next((item[k] for k in ['answer','a','correct','key','correctIndex'] if k in item),None)
    if isinstance(answer,str) and answer.upper() in ['A','B','C','D']:answer=ord(answer.upper())-65
    assert stem and isinstance(opts,list) and len(opts)==4 and type(answer)==int and 0<=answer<4,(stem,answer)
    assert len(set(opts))==4,stem
    parts=[]
    for key in ['title','heading','focus']:
        if item.get(key):parts.append('<h2>'+rich(item[key])+'</h2>')
    for key in ['lead','why','reason','sections','points','blocks','b','notes','note','detail','deep','expl','ex','formula','clinical']:
        value=item.get(key)
        if value is None:continue
        if key=='blocks' and isinstance(value,list):
            for v in value:
                if isinstance(v,dict) and 'title' in v:parts.append('<h3>'+rich(v['title'])+'</h3>'+block(v.get('points',[])))
                else:parts.append(block(v))
        elif key=='why' and isinstance(value,dict):parts.append(alternatives(value,opts,answer))
        else:parts.append(block(value))
    for key in ['table','deep_table']:parts.append(table(item.get(key)))
    for key in ['notes_html','explanationHtml']:
        if item.get(key):parts.append(clean(item[key]))
    if item.get('explanation'):parts.append(clean(item['explanation']) if isinstance(item['explanation'],str) else block(item['explanation']))
    if isinstance(item.get('rich'),dict):
        parts.append(block(item['rich'].get('points')));parts.append(table(item['rich'].get('table')))
    for key in ['other','others','wrongs']:parts.append(alternatives(item.get(key),opts,answer))
    explanation=clean(''.join(parts));plain=LH.fragment_fromstring(explanation,create_parent='div').text_content().strip()
    assert plain,(stem,'Missing explanation')
    return dict(id=f'html-{digest[:16]}-{index:03}',question=stem,options=opts,correctIndex=answer,
      explanation=plain,explanationHtml=explanation,sourceQuestion=copy.deepcopy(item),sourceId=digest+f'-{index}',
      authorship='Imported from user-supplied HTML; question and answer content preserved')

def identity(name):
    stem=Path(name).stem
    m=re.search(r'Chapter_(\d+)_(.*)',stem)
    if 'Cardiology/' in name:subject='Cardiology'
    elif 'Nephrology' in name:subject='Nephrology'
    elif any(x in Path(name).name for x in ['Hepatology','Liver','Cirrhosis','Biliary','HCC']):subject='Liver'
    else:subject='GI & pancreas'
    if m:order=int(m[1]);label=m[2]
    elif 'Esophageal' in name:order=1;label='Esophageal Disorders'
    elif 'HBV' in name:order=19;label='Hepatitis B Advanced'
    elif 'Hepatitis_C' in name:order=20;label='Hepatitis C Advanced'
    else:raise ValueError(name)
    label=re.split(r'_\d+(?:_|$)',label)[0].replace('_',' ')
    if 'Additional_Advanced_Modules' in name and 'Chapter_02' in name:order=2;label='Gastric and Duodenal Disorders Advanced'
    if 'Additional_Advanced_Modules' in name and 'Chapter_03' in name:order=3;label='Malabsorption Advanced'
    label={'AKI':'Acute Kidney Injury','CAD ACS':'CAD and ACS','GI NET':'Gastrointestinal Neuroendocrine Tumors'}.get(label,label)
    return subject,order,label

def stage():
    seen={};banks=[];duplicates=[];summary=[];excluded=[]
    for archive in ARCHIVES:
        with zipfile.ZipFile(Path('C:/Users/ANT-PC/Downloads')/archive) as z:
            for entry in z.infolist():
                if not entry.filename.lower().endswith('.html'):continue
                if re.search(r'Level_?2|Level_2',entry.filename,re.I):excluded.append(entry.filename);continue
                raw=z.read(entry);digest=hashlib.sha256(raw).hexdigest()
                if digest in seen:duplicates.append(dict(file=entry.filename,duplicateOf=seen[digest]));continue
                seen[digest]=entry.filename;items=extract(raw.decode('utf-8-sig'));subject,order,label=identity(entry.filename)
                qs=[convert(q,digest,i) for i,q in enumerate(items,1)]
                document=label;topic_order=1
                if label=='Gastric and Duodenal Disorders Advanced':document='Gastric Duodenal Disorders';topic_order=2
                if label=='Malabsorption Advanced':document='Small Intestine Malabsorption';topic_order=2
                bank=dict(folder=subject,document=document,headingText=label,chapterOrder=order,topicOrder=topic_order,headingIndex=0,questions=qs,
                  sourceArchive=archive,sourceFile=entry.filename,sourceSha256=digest,madeAt=int(time.time()*1000))
                banks.append(bank);summary.append(dict(subject=subject,chapter=order,title=label,questions=len(qs),source=entry.filename))
    assert len(banks)==40 and len(duplicates)==3 and len(excluded)==3
    # Final chapter ZIPs take priority; the broad archive also contains two
    # separate mixed collections, each with many earlier presentation variants.
    supplemental=['NEET_SS_GI_Pancreas_200_Interactive_Structured_Notes.html','NEET_SS_GI_Pancreas_50_Interactive_Expanded_Reviews.html']
    norm=lambda s:re.sub(r'\W+','',str(s).casefold())
    known={norm(q['question']) for bank in banks for q in bank['questions']};superseded=[]
    archive='All_Available_Chat_Files.zip'
    with zipfile.ZipFile(Path('C:/Users/ANT-PC/Downloads')/archive) as z:
        for entry in z.infolist():
            if not entry.filename.lower().endswith('.html'):continue
            if re.search(r'Level_?2|Level_2',entry.filename,re.I):excluded.append(entry.filename);continue
            raw=z.read(entry);digest=hashlib.sha256(raw).hexdigest()
            if digest in seen:duplicates.append(dict(file=entry.filename,duplicateOf=seen[digest]));continue
            if Path(entry.filename).name not in supplemental:
                superseded.append(entry.filename);continue
            label='Mixed GI Structured Review' if '_200_' in entry.filename else 'Mixed GI Expanded Review'
            items=extract(raw.decode('utf-8-sig'));qs=[]
            for i,item in enumerate(items,1):
                stem=norm(item.get('stem',item.get('q',item.get('question'))))
                if stem in known:continue
                qs.append(convert(item,digest,i));known.add(stem)
            assert qs and len(qs)<=200
            bank=dict(folder='GI & pancreas',document='Mixed GI Review',headingText=label,chapterOrder=21,topicOrder=len(banks)-39,headingIndex=0,questions=qs,sourceArchive=archive,sourceFile=entry.filename,sourceSha256=digest,madeAt=int(time.time()*1000))
            banks.append(bank);summary.append(dict(subject=bank['folder'],chapter=21,title=label,questions=len(qs),source=entry.filename))
    staged=[]
    for bank in banks:
        subject,order=bank['folder'],bank['chapterOrder'];label=study_packs._quiz_component(bank['document'])
        dest=OUT/'staged'/subject/f'{order:02}. {label}'/f'{bank["topicOrder"]:02}. {study_packs._quiz_component(bank["headingText"])}';dest.mkdir(parents=True,exist_ok=True)
        (dest/'questions.json').write_text(json.dumps(bank,ensure_ascii=False,indent=2),encoding='utf-8')
        staged.append(str(dest/'questions.json'))
    assert len(set(staged))==42
    report=dict(banks=len(banks),questions=sum(len(b['questions']) for b in banks),duplicates=duplicates,excludedLevel2=excluded,supersededVersions=superseded,chapters=summary,stagedFiles=staged)
    (OUT/'staging-report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k not in {'chapters','stagedFiles'}},indent=2));return banks

def install(banks):
    study=DATA/'study-data';root=(DATA/'Qbank').resolve();before={p:p.read_bytes() for p in study_packs._quiz_record_files(study)}
    extras=[study/'quizzes.json',root/'quizzes.json',INSTALL/'_internal/assets/ini_ss_neurology_quizzes.json',REPO/'assets/ini_ss_neurology_quizzes.json']
    replaced={**before,**{p:p.read_bytes() for p in extras if p.is_file()}}
    assert all(p.resolve().is_relative_to(INSTALL.resolve()) or p.resolve()==(REPO/'assets/ini_ss_neurology_quizzes.json').resolve() for p in replaced)
    backup=root/'backups'/f'all-qbanks-before-html-replacement-{time.time_ns()}.zip';backup.parent.mkdir(parents=True,exist_ok=True)
    names={p:('installed/'+p.relative_to(INSTALL).as_posix() if p.is_relative_to(INSTALL) else 'source-assets/'+p.name) for p in replaced}
    with zipfile.ZipFile(backup,'x',zipfile.ZIP_DEFLATED) as z:
        for p,body in replaced.items():z.writestr(names[p],body)
    with zipfile.ZipFile(backup) as z:assert all(z.read(names[p])==body for p,body in replaced.items())
    written=[]
    try:
        assert all(p.read_bytes()==body for p,body in replaced.items())
        for p in before:p.unlink()
        for p in extras:
            if p in replaced:p.write_text(json.dumps(dict(version=1,quizzes=[])),encoding='utf-8')
        for p in sorted(root.rglob('*'),key=lambda p:len(p.parts),reverse=True):
            if p.is_dir() and p.resolve().is_relative_to(root) and not p.is_relative_to(root/'backups'):
                try:p.rmdir()
                except OSError:pass
        for bank in banks:
            row=study_packs.upsert_saved_quiz(study,bank);assert row
            dest=study_packs._quiz_record_path(study,row);written.append(dest)
            assert json.loads(dest.read_text(encoding='utf-8'))['questions']==bank['questions']
        actual=study_packs.read_quizzes(study);expected={q['id']:q for b in banks for q in b['questions']}
        assert len(actual)==len(banks)
        found={q['id']:q for b in actual for q in b['questions']};assert found==expected
        # Verify the frozen app resource path too, not just the development loader.
        original=paths.resource_root
        try:
            paths.resource_root=lambda:INSTALL/'_internal/assets'
            assert {q['id'] for b in study_packs.read_quizzes(study) for q in b['questions']}==set(expected)
        finally:paths.resource_root=original
    except Exception:
        for p in written:
            if p not in replaced:p.unlink(missing_ok=True)
        for p,body in replaced.items():p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(body)
        raise
    report=dict(result='PASS',banks=len(banks),questions=len(expected),subjects=dict(Counter(b['folder'] for b in banks)),backup=str(backup),backupVerified=True,exactReadback=True,bundledLegacyBanksDisabled=True)
    (OUT/'installation-report.json').write_text(json.dumps(report,indent=2),encoding='utf-8');print(json.dumps(report,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--install',action='store_true');a=p.parse_args();banks=stage()
    if a.install:install(banks)
