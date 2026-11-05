"""Replace exactly the revised CAD/ACS chapter; retain all other bank bytes."""
import argparse,json,sys,time,zipfile
from pathlib import Path
from qbank_authoring import ROOT
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from cnl_desktop import study_packs

def install(write=False):
    study=Path('C:/Users/ANT-PC/OneDrive/Cortex Windows/data/study-data');root=study.parent/'Qbank'
    bank=json.loads((ROOT/'recreated-v2/Cardiology/01. CAD and ACS/questions.json').read_text(encoding='utf-8'))
    qs=bank['questions'];assert len(qs)==44 and all(q['qualityRevision']=='master-instructions-v2' for q in qs)
    ids={q['id'] for q in qs};assert len(ids)==44
    before={p:p.read_bytes() for p in study_packs._quiz_record_files(study)}
    candidates=[p for p,body in before.items() if isinstance((b:=json.loads(body)).get('questions'),list) and {q.get('id') for q in b['questions'] if isinstance(q,dict)}==ids]
    assert len(candidates)==1;p=candidates[0];old=json.loads(before[p]);assert old['folder']=='Cardiology' and p.resolve().is_relative_to(root.resolve())
    print('Target:',p,'questions:',len(qs))
    if not write:return
    backup=root/'backups'/f'cad-acs-before-quality-v2-{time.time_ns()}.zip'
    with zipfile.ZipFile(backup,'x',zipfile.ZIP_DEFLATED) as z:z.writestr(p.relative_to(root).as_posix(),before[p])
    with zipfile.ZipFile(backup) as z:assert z.read(p.relative_to(root).as_posix())==before[p]
    try:
        assert p.read_bytes()==before[p]
        study_packs.upsert_saved_quiz(study,{**old,'questions':qs,'madeAt':int(time.time()*1000)})
        assert json.loads(p.read_text(encoding='utf-8'))['questions']==qs
        assert all(f.read_bytes()==body for f,body in before.items() if f!=p)
        actual=[r for r in study_packs.read_quizzes(study) if study_packs._quiz_row_id(r)==study_packs._quiz_row_id(old)]
        assert len(actual)==1 and actual[0]['questions']==qs
    except Exception:p.write_bytes(before[p]);raise
    report=dict(chapter='CAD and ACS',questions=44,status='installed',backup=str(backup),backupVerified=True,exactReadback=True,otherBanksPreserved=len(before)-1)
    (ROOT/'recreated-v2/cad-acs-installation-report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report,indent=2))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--install',action='store_true');install(p.parse_args().install)
