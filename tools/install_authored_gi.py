"""Back up and replace the GI clinical banks; preserve separate basic-science banks."""
import argparse,hashlib,json,sys,time,zipfile
from pathlib import Path
from qbank_authoring import ROOT,validate
REPO=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(REPO/'src'))
from cnl_desktop import study_packs
SUBJECT='GI & pancreas'
DOCUMENTS={1:'II. Esophageal disorders',2:'III. Stomach',3:'V. Malabsorption syndromes',
    4:'IV. IBD',5:'VII. Other intestinal disorders',6:'VI. Pancreas',7:'VI. Pancreas',
    8:'VII. Other intestinal disorders',9:'VII. Other intestinal disorders',
    10:'VII. Other intestinal disorders',11:'V. Malabsorption syndromes'}

def install(data,write=False):
    study=data/'study-data';root=(data/'Qbank').resolve()
    before={p:p.read_bytes() for p in study_packs._quiz_record_files(study)}
    active=[(p,json.loads(b)) for p,b in before.items()]
    banks=[json.loads(p.read_text(encoding='utf-8')) for p in sorted((ROOT/'completed'/SUBJECT).glob('*/*/questions.json'))]
    assert len(banks)==11 and sum(len(b['questions']) for b in banks)==300
    # The prior clinical banks overlap the replacement chapters. Basic anatomy/physiology
    # is outside this replacement plan and is retained to avoid dropping unique coverage.
    replaced={p:r for p,r in active if r.get('folder')==SUBJECT and r.get('document') in set(DOCUMENTS.values())}
    assert replaced,'No prior clinical GI banks found'
    assert all(p.resolve().is_relative_to(root) for p in replaced)
    existing_ids={study_packs._quiz_row_id(r) for p,r in active}
    for row in study_packs.read_quizzes(study):
        if row.get('folder')==SUBJECT:
            assert study_packs._quiz_row_id(row) in existing_ids,'Unmigrated legacy GI bank requires review'
    targets=[]
    next_topic={doc:max((study_packs._quiz_number(p.parent.name) or 0 for p,r in active
        if r.get('folder')==SUBJECT and r.get('document')==doc),default=0)+1 for doc in set(DOCUMENTS.values())}
    for b in banks:
        validate(b)
        doc=DOCUMENTS[b['chapterOrder']]
        matches=[(p,r) for p,r in replaced.items() if r['document']==doc and r['headingText']==b['headingText']]
        assert len(matches)<=1
        if matches:
            p,old=matches[0];row={**old,'questions':b['questions'],'madeAt':int(time.time()*1000)}
        else:
            row=dict(folder=SUBJECT,document=doc,headingText=b['headingText'],headingIndex=0,
                questions=b['questions'],madeAt=int(time.time()*1000),topicOrder=next_topic[doc])
            next_topic[doc]+=1
            p=study_packs._quiz_record_path(study,row)
            assert p not in before,'New bank path collides with an unrelated bank'
        assert p.resolve().is_relative_to(root) and len(p.relative_to(root).parts)==4
        targets.append((p,row,b))
    destination_paths={p for p,_,_ in targets}
    assert len(destination_paths)==11
    retired=set(replaced)-destination_paths
    report=dict(mode='install' if write else 'dry_run',subject=SUBJECT,newBanks=11,newQuestions=300,
        replacedOldBanks=len(replaced),replacedOldQuestions=sum(len(r['questions']) for r in replaced.values()),
        retiredOverlappingBanks=len(retired),untouchedBanks=len(before)-len(replaced),
        paths=[str(p) for p,_,_ in targets],retiredPaths=[str(p) for p in sorted(retired)],
        policy='Replace old clinical GI banks; preserve basic-science GI coverage and every other subject; preserve existing numbered note/chapter links')
    if not write:print(json.dumps(report,indent=2));return
    backup=root/'backups'/f'gi-original-replacement-{time.time_ns()}.zip'
    backup.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(backup,'x',zipfile.ZIP_DEFLATED) as z:
        for p in replaced:z.writestr(p.relative_to(root).as_posix(),before[p])
    with zipfile.ZipFile(backup) as z:
        assert all(z.read(p.relative_to(root).as_posix())==before[p] for p in replaced)
    written=set()
    try:
        assert all(p.read_bytes()==before[p] for p in replaced),'Concurrent edit detected'
        for p,row,b in targets:
            stored=study_packs.upsert_saved_quiz(study,row);written.add(p)
            assert stored and study_packs._quiz_record_path(study,stored)==p
            assert json.loads(p.read_text(encoding='utf-8'))['questions']==b['questions']
        for p in retired:
            assert p.resolve().is_relative_to(root) and p.read_bytes()==before[p]
            p.unlink()  # Individual verified files only; backup was verified before mutation.
        assert all(p.read_bytes()==body for p,body in before.items() if p not in replaced)
        readback=study_packs.read_quizzes(study)
        for p,row,b in targets:
            found=[r for r in readback if study_packs._quiz_row_id(r)==study_packs._quiz_row_id(row)]
            assert len(found)==1 and found[0]['questions']==b['questions']
        retired_ids={study_packs._quiz_row_id(replaced[p]) for p in retired}
        assert not any(study_packs._quiz_row_id(r) in retired_ids for r in readback)
    except Exception:
        for p in written-set(before):
            assert p.resolve().is_relative_to(root);p.unlink(missing_ok=True)
        for p in replaced:p.write_bytes(before[p])
        raise
    report.update(backup=str(backup),backupVerified=True,readback='passed',
        hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p,_,_ in targets})
    (ROOT/'gi-installation-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    path=ROOT/'topic-map.json';plan=json.loads(path.read_text(encoding='utf-8'))
    for s in plan['subjects']:
        if s['subject']==SUBJECT:
            s.update(status='installed',installedQuestions=300)
            for c in s['chapters']:c['installed']=True
    plan['progress']['installedQuestions']=sum(s.get('installedQuestions',0) for s in plan['subjects'])
    plan['progress']['activeNewProjectBanksReplaced']=sum(sum(bool(c.get('installed')) for c in s['chapters']) for s in plan['subjects'])
    path.write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(report,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--install',action='store_true');p.add_argument('--data',type=Path,default=Path('C:/Users/ANT-PC/OneDrive/Cortex Windows/data'))
    a=p.parse_args();install(a.data.resolve(),a.install)
