"""Move the four subjects' current banks under General, preserving quiz content."""
import argparse
import json
import sys
import time
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / 'src'))
from cnl_desktop import study_packs, paths

SUBJECTS = {'Nephrology', 'Cardiology', 'GI & pancreas', 'Neurology'}


def organize(data: Path, apply=False):
    study = data.resolve() / 'study-data'
    root = paths.quizzes_dir(data.resolve()).resolve()
    originals = {p: p.read_bytes() for p in study_packs._quiz_record_files(study)}
    moves = []
    for source, raw in originals.items():
        row = json.loads(raw)
        parts = source.relative_to(root).parts
        if row.get('folder') not in SUBJECTS or len(parts) != 4:
            continue
        destination = root / parts[0] / 'General' / Path(*parts[1:])
        assert destination.resolve().is_relative_to(root)
        if destination.exists():
            raise ValueError(f'Existing General destination: {destination}')
        row['navigationGroup'] = 'general'
        moves.append((source, destination, row))
    report = dict(modules=len(moves), questions=sum(len(r['questions']) for _, _, r in moves),
                  subjects={s:sum(1 for _,_,r in moves if r['folder']==s) for s in sorted(SUBJECTS)})
    if not apply or not moves:
        return report
    backup = root / 'backups' / f'general-folders-{time.time_ns()}.zip'
    backup.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(backup, 'x', zipfile.ZIP_DEFLATED) as archive:
        for source, _, _ in moves:
            archive.writestr(source.relative_to(root).as_posix(), originals[source])
    with zipfile.ZipFile(backup) as archive:
        assert all(archive.read(p.relative_to(root).as_posix()) == originals[p] for p,_,_ in moves)
    try:
        for _, destination, row in moves:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(json.dumps(row, ensure_ascii=False, indent=2), encoding='utf-8')
            assert json.loads(destination.read_text(encoding='utf-8')) == row
        # Remove a source only after every destination has been verified.
        for source, _, _ in moves:
            source.unlink()
        actual = study_packs.read_quizzes(study)
        by_id = {study_packs._quiz_row_id(r):r for r in actual}
        for _, _, row in moves:
            loaded = by_id[study_packs._quiz_row_id(row)]
            assert loaded['navigationGroup'] == 'general'
            assert loaded['questions'] == row['questions']
        moved = {p for p,_,_ in moves}
        assert all(p.read_bytes()==raw for p,raw in originals.items() if p not in moved)
    except Exception:
        for source, destination, _ in moves:
            source.parent.mkdir(parents=True, exist_ok=True)
            source.write_bytes(originals[source])
            destination.unlink(missing_ok=True)
        raise
    for source, _, _ in moves:
        for directory in (source.parent, source.parent.parent):
            if directory.exists() and not any(directory.iterdir()):
                try:
                    directory.rmdir()
                except OSError:
                    # OneDrive can keep an empty directory open after the move.
                    # It contains no active quizzes and does not appear in Qbank.
                    report.setdefault('retainedEmptyFolders', []).append(str(directory))
    report['backup'] = str(backup)
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=Path, default=Path('C:/Users/ANT-PC/OneDrive/Cortex Windows/data'))
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    print(json.dumps(organize(args.data,args.apply),indent=2))
