"""Install verified staged heading repairs, retaining locked documents for retry."""
import hashlib
import argparse
import json
import shutil
import time
from zipfile import ZipFile
from apply_clinical_template import DEFAULT_DATA, ROOT, sha


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--set', choices=('singleton-bs3','inverted-bs-parents'), default='singleton-bs3')
    args = parser.parse_args()
    output = ROOT / 'build' / args.set
    reports = json.loads((output / 'report.json').read_text(encoding='utf-8'))
    ready, locked, already = [], [], []
    for r in reports:
        if not r['changed']: continue
        source = DEFAULT_DATA / 'files' / r['file']
        current = sha(source)
        if current == r['staged']:
            already.append(r['file']); continue
        assert current == r['before'], source
        assert sha(output / r['file']) == r['staged']
        try:
            with source.open('r+b'): pass
        except PermissionError:
            locked.append(r['file']); continue
        ready.append(r)
    backup = DEFAULT_DATA / 'backups' / ('heading-restoration-' + str(time.time_ns()) + '.zip')
    if ready:
        with ZipFile(backup, 'x') as z:
            for r in ready: z.write(DEFAULT_DATA / 'files' / r['file'], r['file'])
        with ZipFile(backup) as z:
            assert z.testzip() is None
            for r in ready: assert hashlib.sha256(z.read(r['file'])).hexdigest() == r['before']
        written = []
        try:
            for r in ready:
                source = DEFAULT_DATA / 'files' / r['file']
                assert sha(source) == r['before']
                written.append(r)
                shutil.copyfile(output / r['file'], source)
                assert sha(source) == r['staged']
        except Exception:
            with ZipFile(backup) as z:
                for r in written: (DEFAULT_DATA / 'files' / r['file']).write_bytes(z.read(r['file']))
            raise
    result = dict(installed=len(ready), alreadyInstalled=len(already), locked=locked,
                  restoredBS3=sum(len(r.get('restoredBS3', [])) for r in ready),
                  headingsCorrected=sum(len(r['changes']) for r in ready),
                  backup=str(backup) if ready else None)
    (output / 'installation.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__': main()
