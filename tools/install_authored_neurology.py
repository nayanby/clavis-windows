"""Install 548 original Neurology questions; retire records and bundled legacy rows safely."""
import argparse,hashlib,json,sys,time,zipfile
from pathlib import Path
from qbank_authoring import ROOT,validate
REPO=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(REPO/'src'))
from cnl_desktop import study_packs
SUBJECT='Neurology'

def install(data,write=False):
    root=(data/'Qbank').resolve();study=data/'study-data';app=data.parent
    before={p:p.read_bytes() for p in study_packs._quiz_record_files(study)}
    replaced={p:json.loads(b) for p,b in before.items() if json.loads(b).get('folder')==SUBJECT}
    banks=[json.loads(p.read_text(encoding='utf-8')) for p in sorted((ROOT/'install-ready/Neurology').glob('*/*/questions.json'))]
    assert len(banks)==18 and sum(len(b['questions']) for b in banks)==548
    assert len({b['document'] for b in banks})==17
    ids={q['id'] for b in banks for q in b['questions']};assert len(ids)==548
    notes={p.stem for p in (data/'files/Neurology').glob('*.docx')}
    assert {b['document'] for b in banks}==notes,'Note chapter mapping mismatch'
    targets=[]
    for bank in banks:
        validate(bank);row={**bank,'headingIndex':0,'madeAt':int(time.time()*1000)}
        p=study_packs._quiz_record_path(study,row)
        assert p.resolve().is_relative_to(root) and len(p.relative_to(root).parts)==4
        assert p not in before or p in replaced,'Unrelated path collision'
        targets.append((p,row))
    destinations={p for p,_ in targets};assert len(destinations)==18
    retired=set(replaced)-destinations
    # Both runtime and source bundle must be replaced, otherwise built-in recalls return.
    assets=[REPO/'assets/ini_ss_neurology_quizzes.json',app/'_internal/assets/ini_ss_neurology_quizzes.json']
    assert all(p.is_file() for p in assets)
    wrappers=[p for p in [study/'quizzes.json',root/'quizzes.json'] if p.is_file()]
    extras={p:p.read_bytes() for p in assets+wrappers}
    bundle=json.dumps(dict(version=2,authorship='Original topic-based educational Qbank; not authenticated PYQs',
        sourceCheckedAt='2026-11-05',quizzes=[r for _,r in targets]),ensure_ascii=False,indent=2).encode('utf-8')
    report=dict(mode='install' if write else 'dry_run',subject=SUBJECT,newQuestions=548,newBanks=18,numberedChapters=17,
        replacedOldBanks=len(replaced),replacedOldQuestions=sum(len(r['questions']) for r in replaced.values()),
        untouchedBanks=len(before)-len(replaced),retiredOldBanks=len(retired),bundledLegacyReplaced=True,
        paths=[str(p) for p,_ in targets])
    if not write:print(json.dumps(report,indent=2));return
    backup=root/'backups'/f'neurology-original-replacement-{time.time_ns()}.zip';backup.parent.mkdir(parents=True,exist_ok=True)
    labels={p:'records/'+p.relative_to(root).as_posix() for p in replaced}
    labels.update({p:f'extras/{i:02}-{p.name}' for i,p in enumerate(extras)})
    original={**{p:before[p] for p in replaced},**extras}
    with zipfile.ZipFile(backup,'x',zipfile.ZIP_DEFLATED) as z:
        for p,body in original.items():z.writestr(labels[p],body)
        z.writestr('restore-map.json',json.dumps({labels[p]:str(p) for p in original},indent=2))
    with zipfile.ZipFile(backup) as z:
        assert all(z.read(labels[p])==body for p,body in original.items())
    written=set()
    try:
        assert all(p.read_bytes()==body for p,body in original.items()),'Concurrent edit detected'
        for p in assets:p.write_bytes(bundle)
        for p in wrappers:
            payload=json.loads(extras[p]);rows=payload.get('quizzes',[])
            assert isinstance(rows,list)
            payload['quizzes']=[r for r in rows if not isinstance(r,dict) or r.get('folder')!=SUBJECT]
            study_packs._write_json(p,payload)
        for p,row in targets:
            stored=study_packs.upsert_saved_quiz(study,row);written.add(p)
            assert stored and study_packs._quiz_record_path(study,stored)==p
            assert json.loads(p.read_text(encoding='utf-8'))['questions']==row['questions']
        for p in retired:
            assert p.resolve().is_relative_to(root) and p.read_bytes()==before[p]
            p.unlink()  # Individually verified files only, after verified backup.
        assert all(p.read_bytes()==body for p,body in before.items() if p not in replaced)
        # Exercise the installed app's actual asset source, not only the repository bundle.
        previous=study_packs.paths.resource_root
        study_packs.paths.resource_root=lambda:app/'_internal/assets'
        try:actual=[r for r in study_packs.read_quizzes(study) if r.get('folder')==SUBJECT]
        finally:study_packs.paths.resource_root=previous
        assert len(actual)==18 and sum(len(r['questions']) for r in actual)==548
        assert {q['id'] for r in actual for q in r['questions']}==ids
        for _,row in targets:
            found=[r for r in actual if study_packs._quiz_row_id(r)==study_packs._quiz_row_id(row)]
            assert len(found)==1 and found[0]['questions']==row['questions']
        assert all(p.read_bytes()==bundle for p in assets)
    except Exception:
        for p in written-set(before):
            assert p.resolve().is_relative_to(root);p.unlink(missing_ok=True)
        for p,body in original.items():p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(body)
        raise
    report.update(backup=str(backup),backupVerified=True,readback='passed',unrelatedRecordsPreserved=True,
        bundleSha256=hashlib.sha256(bundle).hexdigest(),hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p,_ in targets})
    (ROOT/'neurology-installation-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    pp=ROOT/'topic-map.json';plan=json.loads(pp.read_text(encoding='utf-8'))
    for s in plan['subjects']:
        if s['subject']==SUBJECT:
            s.update(status='installed',installedQuestions=548,installedTopicFiles=18)
            for c in s['chapters']:c['installed']=True
    plan['progress']['installedQuestions']=sum(s.get('installedQuestions',0) for s in plan['subjects'])
    plan['progress']['activeNewProjectBanksReplaced']=sum(s.get('installedTopicFiles',sum(bool(c.get('installed')) for c in s['chapters'])) for s in plan['subjects'])
    pp.write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k not in {'paths','hashes'}},indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--install',action='store_true');p.add_argument('--data',type=Path,default=Path('C:/Users/ANT-PC/OneDrive/Cortex Windows/data'))
    a=p.parse_args();install(a.data.resolve(),a.install)
