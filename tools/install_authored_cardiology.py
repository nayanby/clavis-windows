"""Replace the 11 matched topic banks only after full-subject validation and verified backup."""
import argparse,hashlib,json,sys,time,zipfile
from pathlib import Path
from qbank_authoring import ROOT,validate
REPO=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(REPO/'src'))
from cnl_desktop import study_packs

def install(data,write=False):
    study=data/'study-data';active_root=(data/'Qbank').resolve()
    paths=study_packs._quiz_record_files(study)
    before={p:p.read_bytes() for p in paths}
    active=[(p,json.loads(b)) for p,b in before.items()]
    banks=[json.loads(p.read_text(encoding='utf-8')) for p in sorted((ROOT/'completed/Cardiology').glob('*/*/questions.json'))]
    assert len(banks)==11 and sum(len(b['questions']) for b in banks)==416
    targets=[]
    for bank in banks:
        validate(bank)
        matches=[(p,r) for p,r in active if r.get('folder')=='Cardiology' and r.get('headingText')==bank['headingText']]
        assert len(matches)==1,(bank['headingText'],len(matches))
        p,old=matches[0]
        assert p.resolve().is_relative_to(active_root)
        # Preserve the existing subject/chapter/topic identity and user folder numbering.
        row={**old,'questions':bank['questions'],'madeAt':int(time.time()*1000)}
        targets.append((p,old,row,bank))
    replaced_paths={p for p,_,_,_ in targets}
    report=dict(mode='install' if write else 'dry_run',subject='Cardiology',banks=11,newQuestions=416,
        replacedQuestions=sum(len(old['questions']) for _,old,_,_ in targets),
        untouchedBanks=len(before)-len(targets),
        paths=[str(p) for p,_,_,_ in targets],
        preservation='Existing note links and numbered subject/chapter/topic folders retained; unmatched banks unchanged')
    if not write:print(json.dumps(report,indent=2));return
    backup=active_root/'backups'/f'cardiology-original-replacement-{time.time_ns()}.zip'
    backup.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(backup,'x',zipfile.ZIP_DEFLATED) as z:
        for p in replaced_paths:z.writestr(p.relative_to(active_root).as_posix(),before[p])
    with zipfile.ZipFile(backup) as z:
        assert all(z.read(p.relative_to(active_root).as_posix())==before[p] for p in replaced_paths)
    try:
        # Detect concurrent edits between initial read and replacement.
        assert all(p.read_bytes()==before[p] for p in replaced_paths),'Concurrent bank edit detected'
        for p,old,row,bank in targets:
            stored=study_packs.upsert_saved_quiz(study,row)
            assert stored and study_packs._quiz_record_path(study,stored)==p
            assert json.loads(p.read_text(encoding='utf-8'))['questions']==bank['questions']
        assert all(p.read_bytes()==b for p,b in before.items() if p not in replaced_paths)
        readback=study_packs.read_quizzes(study)
        for p,old,row,bank in targets:
            matches=[r for r in readback if study_packs._quiz_row_id(r)==study_packs._quiz_row_id(old)]
            assert len(matches)==1 and matches[0]['questions']==bank['questions']
    except Exception:
        for p in replaced_paths:p.write_bytes(before[p])
        raise
    report.update(backup=str(backup),readback='passed',backupVerified=True,
        hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in replaced_paths})
    (ROOT/'cardiology-installation-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    planpath=ROOT/'topic-map.json';plan=json.loads(planpath.read_text(encoding='utf-8'))
    for subject in plan['subjects']:
        if subject['subject']=='Cardiology':
            subject.update(status='installed',installedQuestions=416)
            for chapter in subject['chapters']:chapter['installed']=True
    plan['progress']['activeNewProjectBanksReplaced']=11
    plan['progress']['installedQuestions']=416
    planpath.write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(report,indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--install',action='store_true');parser.add_argument('--data',type=Path,default=Path('C:/Users/ANT-PC/OneDrive/Cortex Windows/data'))
    args=parser.parse_args();install(args.data.resolve(),args.install)
