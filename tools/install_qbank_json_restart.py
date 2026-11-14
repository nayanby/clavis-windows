"""Explicit user-requested all-subject reset; verified backup and rollback."""
import argparse, json, sys, time, zipfile, hashlib
from pathlib import Path

REPO=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(REPO/'src'))
from cnl_desktop import study_packs

def install(data,write=False):
    data=data.resolve();root=(data/'Qbank').resolve()
    assert root.parent==data and root.name=='Qbank' and root.is_dir()
    source=REPO/'Qbank Rebuild/Neurology/01. Neuroanatomy, Clinical Localization & Neurological Examination.json'
    bank=json.loads(source.read_text(encoding='utf-8'))
    assert len(bank['questions'])==30 and bank['chapterOrder']==1
    files=list(root.rglob('*'))
    assert not any(p.is_symlink() or p.is_junction() for p in files),'Do not traverse redirected paths'
    originals={p:p.read_bytes() for p in files if p.is_file()}
    assert all(p.resolve().is_relative_to(root) for p in originals)
    extras=[data/'study-data/quizzes.json',data/'quizzes.json',
        REPO/'assets/ini_ss_neurology_quizzes.json',
        REPO/'dist/Clinical Notes Library/_internal/assets/ini_ss_neurology_quizzes.json',
        data.parent/'_internal/assets/ini_ss_neurology_quizzes.json']
    extras={p:p.read_bytes() for p in extras if p.is_file()}
    assert all(not json.loads(body).get('quizzes') for body in extras.values()), 'Nonempty fallback requires separate authorization; leave untouched'
    # Determine destination using the application's own identity and path rules.
    destination=study_packs._quiz_record_path(data/'study-data',bank)
    assert destination.resolve().is_relative_to(root)
    report=dict(mode='install' if write else 'dry_run',oldFolderFiles=len(originals),legacySources=len(extras),
                newBanks=1,newQuestions=30,destination=str(destination))
    if not write:print(json.dumps(report,indent=2));return
    backup=data/'qbank-reset-backups'/f'before-neurology-restart-{time.time_ns()}.zip'
    backup.parent.mkdir(parents=True,exist_ok=True)
    alloriginal=originals
    names={p:f'original/{i:04}-{p.name}' for i,p in enumerate(alloriginal)}
    with zipfile.ZipFile(backup,'x',zipfile.ZIP_DEFLATED) as z:
        for p,body in alloriginal.items():z.writestr(names[p],body)
        z.writestr('restore-map.json',json.dumps({names[p]:str(p) for p in alloriginal},indent=2))
    with zipfile.ZipFile(backup) as z:
        assert all(z.read(names[p])==body for p,body in alloriginal.items())
    changed=[]
    try:
        assert all(p.read_bytes()==b for p,b in alloriginal.items()),'Concurrent modification'
        # Fallbacks were verified empty; never modify files outside Qbank.
        assert all(p.read_bytes()==b for p,b in extras.items())
        for p in originals:
            assert p.resolve().is_relative_to(root)
            p.unlink();changed.append(p)
        for p in sorted((p for p in files if p.is_dir()),key=lambda p:len(p.parts),reverse=True):
            assert p.resolve().is_relative_to(root)
            if not any(p.iterdir()):
                try:p.rmdir()
                except PermissionError:pass  # OneDrive may retain an empty folder; no old bank remains.
        destination=study_packs._quiz_record_path(data/'study-data',bank)
        destination.parent.mkdir(parents=True,exist_ok=True)
        destination.write_bytes(source.read_bytes())
        assert json.loads(destination.read_text(encoding='utf-8'))==bank
        assert list(root.rglob('*.json'))==[destination]
        old_resource=study_packs.paths.resource_root
        for assetdir in {REPO/'assets',data.parent/'_internal/assets'}:
            study_packs.paths.resource_root=lambda a=assetdir:a
            actual=study_packs.read_quizzes(data/'study-data')
            assert len(actual)==1 and actual[0]['questions']==bank['questions'], 'Old bank remains active'
        study_packs.paths.resource_root=old_resource
    except BaseException:
        if 'old_resource' in locals():study_packs.paths.resource_root=old_resource
        if destination not in alloriginal:destination.unlink(missing_ok=True)
        for p,b in alloriginal.items():p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
        raise
    report.update(backup=str(backup),backupVerified=True,activeReadback='passed',sha256=hashlib.sha256(destination.read_bytes()).hexdigest())
    # Installation paths and the user's private backup remain local, not in Git.
    (data/'qbank-reset-backups/latest-reset-report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--data',type=Path,default=Path('C:/Users/ANT-PC/OneDrive/Cortex Windows/data'))
    p.add_argument('--install',action='store_true');a=p.parse_args();install(a.data,a.install)
