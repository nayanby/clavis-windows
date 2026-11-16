"""Install one sealed Cardiology chapter using its full source document name."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import time
import zipfile

from qbank_json_chapters import DATA, REPO, ROOT, validate
from redistribute_cardiology_qbank import digest


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')


def install(source, apply=False):
    sys.path.insert(0, str(REPO/'src'))
    from cnl_desktop import study_packs
    source=source.resolve()
    assert source.parent==ROOT/'Cardiology'
    bank=read(source)
    validation=validate(bank)
    number=bank['chapterOrder']
    audit=source.parent/'audit'
    release_path=audit/f'chapter-{number:02}-release-review.json'
    release=read(release_path)
    assert release['status']=='passed'
    assert release['reviewedQuestionsSha256']==digest(bank['questions'])
    assert release['document']==bank['document'] and release['questionCount']==len(bank['questions'])
    assert bank['status'] in {'reviewed_ready_to_install','installed_verified'}
    source_doc=DATA/'files/Cardiology'/(bank['document']+'.docx')
    assert hashlib.sha256(source_doc.read_bytes()).hexdigest()==release['sourceDocumentSha256']
    root=(DATA/'Qbank').resolve()
    study=DATA/'study-data'
    before={p:p.read_bytes() for p in study_packs._quiz_record_files(study)}
    identity=study_packs._quiz_row_id(bank)
    previous=[p for p,raw in before.items() if study_packs._quiz_row_id(json.loads(raw))==identity]
    assert len(previous)<=1
    dest=root/'Cardiology'/bank['document']/'Questions'/(hashlib.sha256(identity.encode()).hexdigest()[:20]+'.json')
    assert dest.resolve().is_relative_to(root)
    assert not dest.exists() or dest in previous
    assert all(not (p.is_symlink() or p.is_junction()) for p in [root,root/'Cardiology',dest.parent.parent,dest.parent])
    existing_ids={q['id'] for p,raw in before.items() if p not in previous
                  for q in json.loads(raw).get('questions',[])}
    assert not existing_ids & {q['id'] for q in bank['questions']},'An installed question is assigned to another chapter'
    manifest_path=audit/'installation-report.json'
    manifest=read(manifest_path)
    assert all(Path(p) in before for p in manifest['files'])
    if not apply:
        print(json.dumps(dict(ready=True,destination=str(dest),questions=len(bank['questions']),otherBanks=len(before)-len(previous)),indent=2))
        return
    backup=DATA/'qbank-reset-backups'/f'reviewed-cardiology-{number:02}-{time.time_ns()}.zip'
    backup.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(backup,'x',zipfile.ZIP_DEFLATED) as z:
        z.writestr('repository-bank.json',source.read_bytes())
        z.writestr('installation-report.json',manifest_path.read_bytes())
        for p in previous:z.writestr(p.relative_to(root).as_posix(),before[p])
    with zipfile.ZipFile(backup) as z:
        assert z.read('repository-bank.json')==source.read_bytes()
        for p in previous:assert z.read(p.relative_to(root).as_posix())==before[p]
    source_before=source.read_bytes()
    bank['status']='installed_verified'
    if 'redistribution' in bank:bank['redistribution']['draftQuestions']=0
    try:
        assert all(p.read_bytes()==raw for p,raw in before.items()),'Concurrent runtime modification'
        write(dest,bank)
        for p in previous:
            if p!=dest:p.unlink()
        old_resource=study_packs.paths.resource_root
        try:
            study_packs.paths.resource_root=lambda:DATA.parent/'_internal/assets'
            loaded=study_packs.read_quizzes(study)
        finally:study_packs.paths.resource_root=old_resource
        matches=[b for b in loaded if study_packs._quiz_row_id(b)==identity]
        assert len(matches)==1 and matches[0]['questions']==bank['questions']
        assert matches[0]['chapterOrder']==number and matches[0]['document']==bank['document']
        assert all(p.read_bytes()==raw for p,raw in before.items() if p not in previous)
        cardio=[b for b in loaded if b.get('folder')=='Cardiology']
        assert len({q['id'] for b in loaded for q in b['questions']})==sum(len(b['questions']) for b in loaded)
        write(source,bank)
    except BaseException:
        if dest in before:dest.write_bytes(before[dest])
        else:dest.unlink(missing_ok=True)
        for p in previous:
            p.parent.mkdir(parents=True,exist_ok=True)
            p.write_bytes(before[p])
        source.write_bytes(source_before)
        raise
    history=audit/'installation-history'
    if not (history/'redistribution-installation.json').exists():write(history/'redistribution-installation.json',manifest)
    files=[str(Path(p)) for p in manifest['files'] if Path(p) not in previous]+[str(dest)]
    authored=sum(len(read(p)['questions']) for p in source.parent.glob('*.json'))
    released=sorted(set(manifest.get('releasedChapterOrders',[]))|{number})
    manifest.update(status='passed',installedChapters=len(cardio),installedQuestions=sum(len(b['questions']) for b in cardio),
                    files=files,releasedChapterOrders=released,lastInstalledChapter=number,lastBackup=str(backup),
                    lastReadback='passed',lastInstalledAt='2026-11-16',note='Redistributed subsets plus individually reviewed full chapters; other chapters may still have incomplete coverage.')
    manifest['draftQuestionsWithheld']=authored-manifest['installedQuestions']
    write(manifest_path,manifest)
    release.update(installed=True,installedPath=str(dest),installedSha256=hashlib.sha256(dest.read_bytes()).hexdigest())
    write(release_path,release)
    coverage_path=audit/f'chapter-{number:02}-coverage.json'
    coverage=read(coverage_path);coverage['status']='installed_verified';write(coverage_path,coverage)
    review_path=audit/f'chapter-{number:02}-source-review.json'
    review=read(review_path);review.update(status='installed_verified',installed=True)
    review['releaseReview'].update(installed=True,runtimeReadback='passed')
    review['editorialReviewProgress']['nextWork']='Release review and runtime readback completed.'
    write(review_path,review)
    plan=read(ROOT/'progress.json')
    entry=next(x for x in plan['chapters'] if x['subject']=='Cardiology' and x['document']==bank['document'])
    entry.update(status='installed_verified',runtimeStatus='installed_reviewed_chapter',installedQuestions=len(bank['questions']),
                 draftQuestions=0,draftQuestionsWithheld=0,installedSha256=release['installedSha256'])
    plan['cardiologyRedistribution'].update(currentAuthoredQuestions=authored,currentDraftQuestionsNotInstalled=manifest['draftQuestionsWithheld'])
    next_entry=next((x for x in plan['chapters'] if x['subject']=='Cardiology' and x.get('chapter',0)>number and x.get('status')!='installed_verified'),None)
    next_label=('Cardiology '+next_entry['document']) if next_entry else 'Continue pending source-matched chapters'
    plan['currentChapter']=next_label
    write(ROOT/'progress.json',plan)
    summary=read(ROOT/'validation-summary.json')
    summary.update(installedChapters=len(loaded),installedQuestions=sum(len(b['questions']) for b in loaded),
                   currentCardiologyAuthoredQuestions=authored,currentCardiologyDraftQuestionsNotInstalled=manifest['draftQuestionsWithheld'],
                   runtimeSourceComparison='passed_current_banks_against_released_subsets_and_reviewed_chapters',nextChapter=next_label)
    write(ROOT/'validation-summary.json',summary)
    print(json.dumps(dict(installed=str(dest),cardiologyChapters=len(cardio),cardiologyQuestions=manifest['installedQuestions'],
                          totalBanks=len(loaded),totalQuestions=summary['installedQuestions'],otherBanksPreserved=len(before)-len(previous),validation=validation),indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('source',type=Path)
    parser.add_argument('--apply',action='store_true')
    args=parser.parse_args()
    install(args.source,args.apply)
