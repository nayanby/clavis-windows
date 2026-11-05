"""Install all new Psychiatry content after verified backup and numbered-chapter mapping."""
import argparse,hashlib,json,sys,time,zipfile
from pathlib import Path
from qbank_authoring import ROOT,validate
REPO=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(REPO/'src'))
from cnl_desktop import study_packs

def install(data,write=False):
    root=(data/'Qbank').resolve();study=data/'study-data'
    before={p:p.read_bytes() for p in study_packs._quiz_record_files(study)}
    replaced={p:json.loads(body) for p,body in before.items() if json.loads(body).get('folder')=='Psychiatry'}
    banks=[json.loads(p.read_text(encoding='utf-8')) for p in sorted((ROOT/'install-ready/Psychiatry').glob('*/*/questions.json'))]
    assert len(banks)==6 and sum(len(b['questions']) for b in banks)==136
    assert len({b['document'] for b in banks})==6
    ids={q['id'] for b in banks for q in b['questions']};assert len(ids)==136
    activeids={study_packs._quiz_row_id(json.loads(body)) for body in before.values()}
    assert all(study_packs._quiz_row_id(r) in activeids for r in study_packs.read_quizzes(study) if r.get('folder')=='Psychiatry'),'Unmigrated Psychiatry data'
    targets=[]
    for bank in banks:
        validate(bank)
        row={**bank,'headingIndex':0,'madeAt':int(time.time()*1000)}
        p=study_packs._quiz_record_path(study,row)
        assert p.resolve().is_relative_to(root) and len(p.relative_to(root).parts)==4
        assert p not in before or p in replaced,'Collision with unrelated bank'
        targets.append((p,row))
    destinations={p for p,_ in targets};assert len(destinations)==6
    retired=set(replaced)-destinations
    report=dict(mode='install' if write else 'dry_run',subject='Psychiatry',newQuestions=136,newBanks=6,numberedChapters=6,
        replacedOldBanks=len(replaced),replacedOldQuestions=sum(len(r['questions']) for r in replaced.values()),
        untouchedBanks=len(before)-len(replaced),retiredOldBanks=len(retired),paths=[str(p) for p,_ in targets])
    if not write:print(json.dumps(report,indent=2));return
    backup=root/'backups'/f'psychiatry-original-replacement-{time.time_ns()}.zip';backup.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(backup,'x',zipfile.ZIP_DEFLATED) as z:
        for p in replaced:z.writestr(p.relative_to(root).as_posix(),before[p])
    with zipfile.ZipFile(backup) as z:
        assert all(z.read(p.relative_to(root).as_posix())==before[p] for p in replaced)
    written=set()
    try:
        assert all(p.read_bytes()==before[p] for p in replaced),'Concurrent edit detected'
        for p,row in targets:
            stored=study_packs.upsert_saved_quiz(study,row);written.add(p)
            assert stored and study_packs._quiz_record_path(study,stored)==p
            assert json.loads(p.read_text(encoding='utf-8'))['questions']==row['questions']
        for p in retired:
            assert p.resolve().is_relative_to(root) and p.read_bytes()==before[p]
            p.unlink()
        assert all(p.read_bytes()==body for p,body in before.items() if p not in replaced)
        actual=[r for r in study_packs.read_quizzes(study) if r.get('folder')=='Psychiatry']
        assert len(actual)==6 and sum(len(r['questions']) for r in actual)==136
        assert {q['id'] for r in actual for q in r['questions']}==ids
        for _,row in targets:
            found=[r for r in actual if study_packs._quiz_row_id(r)==study_packs._quiz_row_id(row)]
            assert len(found)==1 and found[0]['questions']==row['questions']
    except Exception:
        for p in written-set(before):
            assert p.resolve().is_relative_to(root);p.unlink(missing_ok=True)
        for p in replaced:p.write_bytes(before[p])
        raise
    report.update(backup=str(backup),backupVerified=True,readback='passed',
        hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p,_ in targets})
    (ROOT/'psychiatry-installation-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    pp=ROOT/'topic-map.json';plan=json.loads(pp.read_text(encoding='utf-8'))
    for s in plan['subjects']:
        if s['subject']=='Psychiatry':
            s.update(status='installed',installedQuestions=136,installedTopicFiles=6)
            for c in s['chapters']:c['installed']=True
    plan['progress']['installedQuestions']=sum(s.get('installedQuestions',0) for s in plan['subjects'])
    plan['progress']['activeNewProjectBanksReplaced']=sum(s.get('installedTopicFiles',sum(bool(c.get('installed')) for c in s['chapters'])) for s in plan['subjects'])
    pp.write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(report,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--install',action='store_true');p.add_argument('--data',type=Path,default=Path('C:/Users/ANT-PC/OneDrive/Cortex Windows/data'))
    a=p.parse_args();install(a.data.resolve(),a.install)
