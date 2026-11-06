"""Restore the user's saved Qbanks into document/heading folders, beside General."""
import argparse
import copy
import json
import sys
import time
import zipfile
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(REPO/'src'))
from cnl_desktop import study_packs, paths


def source_banks(source):
    rows = {}
    copies = 0
    for file in sorted(source.rglob('*.json')):
        row = json.loads(file.read_text(encoding='utf-8-sig'))
        if not isinstance(row,dict) or not isinstance(row.get('questions'),list) or not row['questions']:
            continue
        identity = study_packs._quiz_row_id(row)
        if not identity:
            raise ValueError(f'Missing quiz identity: {file}')
        if identity in rows:
            if rows[identity]['questions'] != row['questions']:
                raise ValueError(f'Conflicting source copies: {file}')
            copies += 1
            continue
        rows[identity] = copy.deepcopy(row)
    if not rows:
        raise ValueError('No saved Qbanks in source directory')
    return rows,copies


def restore(source, data, apply=False):
    rows,copies = source_banks(source)
    study = data.resolve()/'study-data'
    root = paths.quizzes_dir(data.resolve()).resolve()
    before = {p:p.read_bytes() for p in study_packs._quiz_record_files(study)}
    existing = {}
    for p,raw in before.items():
        row = json.loads(raw)
        identity = study_packs._quiz_row_id(row)
        if p.relative_to(root).parts[1] == 'General':
            if identity in rows:
                raise ValueError('Source identity collides with General; keeping both libraries untouched')
        else:
            existing[identity] = p
    report = dict(banks=len(rows),questions=sum(len(r['questions']) for r in rows.values()),
                  duplicateCopiesSkipped=copies,subjects=dict(Counter(r['folder'] for r in rows.values())))
    if not apply:
        return report
    backup = root/'backups'/f'before-legacy-restore-{time.time_ns()}.zip'
    backup.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(backup,'x',zipfile.ZIP_DEFLATED) as archive:
        for p,raw in before.items():
            archive.writestr(p.relative_to(root).as_posix(),raw)
    with zipfile.ZipFile(backup) as archive:
        assert all(archive.read(p.relative_to(root).as_posix())==raw for p,raw in before.items())
    written = []
    groups = {}
    for identity,row in rows.items():
        groups.setdefault((row['folder'],row['document']),[]).append((identity,row))
    try:
        for (subject,document),topics in sorted(groups.items()):
            for number,(identity,row) in enumerate(sorted(topics,key=lambda t:(t[1].get('headingIndex',0),t[1]['headingText'])),1):
                row['chapterOrder'] = study_packs._quiz_number(document) or 1
                row['topicOrder'] = number
                row.pop('navigationGroup',None)
                destination = study_packs._quiz_record_path(study,row,existing)
                assert destination.resolve().is_relative_to(root)
                assert len(destination.relative_to(root).parts)==4
                row['chapterOrder'] = study_packs._quiz_number(destination.parent.parent.name) or 1
                row['topicOrder'] = study_packs._quiz_number(destination.parent.name) or 1
                written.append(destination)
                study_packs._write_json(destination,row)
                assert json.loads(destination.read_text(encoding='utf-8'))==row
        actual = {study_packs._quiz_row_id(r):r for r in study_packs.read_quizzes(study)}
        assert all(actual[identity]['questions']==row['questions'] for identity,row in rows.items())
        assert all(p.read_bytes()==raw for p,raw in before.items() if p not in written)
    except Exception:
        for p in written:
            if p not in before:
                p.unlink(missing_ok=True)
        for p,raw in before.items():
            p.parent.mkdir(parents=True,exist_ok=True)
            p.write_bytes(raw)
        raise
    report.update(backup=str(backup),preservedExistingBanks=len(before),paths=[str(p) for p in written])
    out = REPO/'build/legacy-qbank-restore'
    out.mkdir(parents=True,exist_ok=True)
    (out/'restore-report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    return {k:v for k,v in report.items() if k!='paths'}


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--source',type=Path,default=Path('D:/Qbank/saved'))
    parser.add_argument('--data',type=Path,default=Path('C:/Users/ANT-PC/OneDrive/Cortex Windows/data'))
    parser.add_argument('--apply',action='store_true')
    args=parser.parse_args()
    print(json.dumps(restore(args.source,args.data,args.apply),indent=2))
