"""Retire the remaining pre-replacement Cardiology/GI banks after verified backup."""
import argparse,hashlib,json,sys,time,zipfile
from collections import Counter
from pathlib import Path
from qbank_authoring import ROOT
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from cnl_desktop import study_packs

def remove(data,write=False):
    root=(data/'Qbank').resolve();study=data/'study-data'
    plan=json.loads((ROOT/'topic-map.json').read_text(encoding='utf-8'))
    ids={q['id'] for s in plan['subjects'] for c in s['chapters']
         for q in json.loads((ROOT/c['completedFile']).read_text(encoding='utf-8'))['questions']}
    assert len(ids)==4456
    before={p:p.read_bytes() for p in study_packs._quiz_record_files(study)}
    retired={};counts=Counter();bankcounts=Counter()
    for p,body in before.items():
        bank=json.loads(body);questions=bank.get('questions',[])
        if not isinstance(questions,list) or not questions:continue
        assert all(isinstance(q,dict) for q in questions),p
        old=[q for q in questions if q.get('id') not in ids]
        if not old:continue
        assert bank.get('folder') in {'Cardiology','GI & pancreas'},p
        assert len(old)==len(questions),'Mixed old/new bank requires a separate migration'
        assert p.resolve().is_relative_to(root) and len(p.relative_to(root).parts)==4,p
        retired[p]=body;counts[bank['folder']]+=len(old);bankcounts[bank['folder']]+=1
    assert dict(counts)=={'Cardiology':628,'GI & pancreas':66},counts
    assert dict(bankcounts)=={'Cardiology':39,'GI & pancreas':7},bankcounts
    report=dict(mode='remove' if write else 'dry_run',removedQuestions=sum(counts.values()),removedBanks=len(retired),
      questionsBySubject=dict(counts),banksBySubject=dict(bankcounts),paths=[str(p) for p in retired])
    if not write:print(json.dumps(report,indent=2));return
    backup=root/'backups'/f'remaining-old-banks-{time.time_ns()}.zip';backup.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(backup,'x',zipfile.ZIP_DEFLATED) as z:
        for p,body in retired.items():z.writestr(p.relative_to(root).as_posix(),body)
    with zipfile.ZipFile(backup) as z:
        assert len(z.namelist())==len(retired)
        assert all(z.read(p.relative_to(root).as_posix())==body for p,body in retired.items())
    deleted=[]
    try:
        assert all(p.read_bytes()==body for p,body in before.items()),'Concurrent bank edit'
        for p,body in retired.items():
            assert p.resolve().is_relative_to(root) and p.read_bytes()==body
            p.unlink();deleted.append(p)
        assert all(p.read_bytes()==body for p,body in before.items() if p not in retired)
        active=study_packs.read_quizzes(study);seen=Counter()
        for bank in active:
            questions=bank.get('questions',[])
            if not isinstance(questions,list):continue
            for q in questions:
                assert isinstance(q,dict) and q.get('id') in ids,'Old question still active'
                seen[q['id']]+=1
        assert set(seen)==ids and all(n==1 for n in seen.values()),'New questions changed or missing'
    except Exception:
        for p in deleted:p.write_bytes(retired[p])
        raise
    report.update(backup=str(backup),backupVerified=True,readback='passed',activeQuestions=sum(seen.values()),
      preservedFileHashes={str(p):hashlib.sha256(body).hexdigest() for p,body in before.items() if p not in retired})
    (ROOT/'remaining-old-banks-removal-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k not in {'paths','preservedFileHashes'}},indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--remove',action='store_true');p.add_argument('--data',type=Path,default=Path('C:/Users/ANT-PC/OneDrive/Cortex Windows/data'))
    a=p.parse_args();remove(a.data.resolve(),a.remove)
