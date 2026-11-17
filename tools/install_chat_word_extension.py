"""Update a known unpacked extension folder without touching unrelated files."""
import argparse
import json
from pathlib import Path
import time
from zipfile import ZipFile,ZIP_DEFLATED

ROOT=Path(__file__).resolve().parents[1]
def main():
    parser=argparse.ArgumentParser();parser.add_argument('target',type=Path);args=parser.parse_args()
    target=args.target.resolve();original=json.loads((target/'manifest.json').read_text(encoding='utf-8-sig'))
    assert original['name']=='Pearls Chat to Word'
    backup=ROOT/'build/extension-install-backups'/('pearls-'+str(time.time_ns())+'.zip');backup.parent.mkdir(parents=True,exist_ok=True)
    with ZipFile(ROOT/'outputs/pearls-chat-word/Pearls Chat to Word.zip') as z:
        assert z.testzip() is None
        names=[name for name in z.namelist() if not name.endswith('/')];assert len(names)==20
        updated=json.loads(z.read('Pearls Chat to Word/manifest.json'));assert updated['name']==original['name']
        planned=[]
        for name in names:
            assert name.startswith('Pearls Chat to Word/')
            relative=Path(name[len('Pearls Chat to Word/'):]);destination=(target/relative).resolve();assert destination.is_relative_to(target)
            planned.append((name,relative,destination,destination.exists()))
        with ZipFile(backup,'x',ZIP_DEFLATED) as b:
            for name,relative,destination,existed in planned:
                if existed:b.write(destination,relative.as_posix())
        written=[]
        try:
            for name,relative,destination,existed in planned:
                destination.parent.mkdir(parents=True,exist_ok=True);written.append((relative,destination,existed))
                destination.write_bytes(z.read(name));assert destination.read_bytes()==z.read(name)
        except Exception:
            with ZipFile(backup) as b:
                for relative,destination,existed in written:
                    if existed:destination.write_bytes(b.read(relative.as_posix()))
                    else:destination.unlink(missing_ok=True)
            raise
    print(json.dumps(dict(previousVersion=original['version'],installedFilesVersion=updated['version'],files=len(names),backup=str(backup))))

if __name__=='__main__':main()
