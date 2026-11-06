"""Flatten General modules and replace hash filenames without changing JSON bytes."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import time
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from cnl_desktop.study_packs import _quiz_component, _quiz_label


def migrate(root: Path, apply=False):
    root = root.resolve(strict=True)
    if root.name.casefold() != 'qbank':
        raise ValueError('Specify the Qbank directory.')
    plan = []
    targets = set()
    for source in sorted(root.glob('*/General/*/*/*.json')):
        if not source.resolve().is_relative_to(root):
            raise ValueError('Source escapes Qbank.')
        raw = source.read_bytes()
        bank = json.loads(raw)
        if not isinstance(bank.get('questions'), list):
            raise ValueError(f'Not a bank: {source}')
        label = _quiz_component(_quiz_label(bank.get('headingText') or bank.get('document') or source.parent.name))
        destination = source.parent.parent / (label + '.json')
        if destination.exists() or str(destination).casefold() in targets:
            raise ValueError(f'Destination collision: {destination}')
        targets.add(str(destination).casefold())
        plan.append((source, destination, raw))
    report = {'files': len(plan), 'questions': sum(len(json.loads(raw)['questions']) for _, _, raw in plan),
        'changes': [{'from': str(a.relative_to(root)), 'to': str(b.relative_to(root))} for a, b, _ in plan]}
    if not apply or not plan:
        return report
    backup = root / 'backups' / f'general-before-readable-{time.time_ns()}.zip'
    backup.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(backup, 'x', zipfile.ZIP_DEFLATED) as archive:
        for source, _, raw in plan:
            archive.writestr(source.relative_to(root).as_posix(), raw)
    with zipfile.ZipFile(backup) as archive:
        for source, _, raw in plan:
            if archive.read(source.relative_to(root).as_posix()) != raw:
                raise OSError('Backup verification failed.')
    for source, destination, raw in plan:
        if source.read_bytes() != raw:
            raise OSError('Source changed during migration.')
        # Copy, verify, then remove only the verified source file.
        with destination.open('xb') as output:
            output.write(raw)
        if hashlib.sha256(destination.read_bytes()).digest() != hashlib.sha256(raw).digest():
            raise OSError('Destination verification failed.')
        source.unlink()
        if not any(source.parent.iterdir()):
            source.parent.rmdir()
    report['backup'] = str(backup)
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', type=Path)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    print(json.dumps(migrate(args.root, args.apply), indent=2))
