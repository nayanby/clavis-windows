"""Arrange Critical Care into ten sequential chapters after removing the blank slot."""
import argparse
import hashlib
import json
from pathlib import Path
import time
from zipfile import ZipFile

from standardize_subject_filenames import catalog_update

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = Path(r'C:\Users\ANT-PC\OneDrive\Cortex Windows\data')
CHAPTERS = [
    ('2. Hemodynamic Monitoring, Fluid Therapy & Shock.docx',
     '1. Hemodynamic Monitoring, Fluid Therapy & Shock.docx'),
    ('3. Sepsis, Septic Shock & Multiorgan Dysfunction.docx',
     '2. Sepsis, Septic Shock & Multiorgan Dysfunction.docx'),
    ('4. Mechanical Ventilation & Respiratory Support.docx',
     '3. Respiratory Failure, Mechanical Ventilation & Respiratory Support.docx'),
    ('5. Cardiopulmonary Resuscitation & Post-Cardiac Arrest Care.docx',
     '4. Cardiopulmonary Resuscitation & Post-Cardiac Arrest Care.docx'),
    ('7. Sedation, Analgesia, Delirium & ECMO.docx',
     '5. Sedation, Analgesia, Delirium & ECMO.docx'),
    ('8. General Toxicology, Toxidromes, Decontamination & Antidotes.docx',
     '6. General Toxicology, Toxidromes, Decontamination & Antidotes.docx'),
    ('9. Drug Poisoning, Toxic Alcohols, Chemical & Heavy Metal Toxicity.docx',
     '7. Drug Poisoning, Toxic Alcohols, Chemical & Heavy Metal Toxicity.docx'),
    ('10. Pesticide Poisoning, Envenomation & Biological Toxins.docx',
     '8. Pesticide Poisoning, Envenomation & Biological Toxins.docx'),
    ('11. Thermal, Electrical & Radiation Emergencies.docx',
     '9. Heat, Cold, Electrical & Radiation Injuries.docx'),
    ('12. Asphyxial & Environmental Emergencies.docx',
     '10. Hanging, Strangulation, Drowning, Altitude & Diving Emergencies.docx'),
]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(data, install):
    folder = (data / 'files/Critical Care').resolve()
    pairs = [(folder / old, folder / new) for old, new in CHAPTERS]
    current = [p for p in folder.glob('*.docx') if not p.name.startswith('~$')]
    assert set(current) == {a for a, b in pairs}, 'Critical Care file set changed'
    for old, new in pairs:
        assert old.resolve().is_relative_to(folder) and new.resolve().is_relative_to(folder)
        assert not new.exists(), f'Destination already exists: {new}'
    hashes = {a: sha(a) for a, b in pairs}
    rows = [{'old': a, 'new': b, 'subject': 'Critical Care'} for a, b in pairs]
    catalog, original_catalog, updated_catalog, catalog_count = catalog_update(data, rows)
    report = {'chapters': [{'old': a.name, 'new': b.name} for a, b in pairs],
              'totalChapters': 10, 'blankChapterSlotRemoved': True,
              'catalogEntriesUpdated': catalog_count, 'documentContentsUnchanged': True}
    print(json.dumps(report, ensure_ascii=False, indent=2), flush=True)
    if install:
        for old, new in pairs:
            assert sha(old) == hashes[old], 'Concurrent edit'
            try:
                with old.open('r+b'):
                    pass
            except PermissionError as exc:
                raise PermissionError(f'Close this Word document: {old}') from exc
        backup = data / 'backups' / f'critical-care-before-chapter-order-{time.time_ns()}.zip'
        backup.parent.mkdir(parents=True, exist_ok=True)
        with ZipFile(backup, 'x') as z:
            z.writestr('chapter-order-manifest.json', json.dumps(report, ensure_ascii=False, indent=2))
            for old, new in pairs:
                z.write(old, old.name)
            if catalog_count:
                z.writestr('library_catalog.json', original_catalog)
        with ZipFile(backup) as z:
            for old, new in pairs:
                assert hashlib.sha256(z.read(old.name)).hexdigest() == hashes[old]
        moved = []; catalog_written = False
        try:
            for old, new in pairs:
                assert sha(old) == hashes[old]
                old.rename(new); moved.append((old, new))
                assert sha(new) == hashes[old], 'Document content changed'
            if catalog_count:
                assert catalog.read_bytes() == original_catalog, 'Concurrent catalog edit'
                catalog_written = True
                catalog.write_text(json.dumps(updated_catalog, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
            actual = [p for p in folder.glob('*.docx') if not p.name.startswith('~$')]
            assert len(actual) == 10
            assert {int(p.name.split('.', 1)[0]) for p in actual} == set(range(1, 11))
        except Exception:
            for old, new in reversed(moved):
                new.rename(old)
            if catalog_written:
                catalog.write_bytes(original_catalog)
            raise
        report.update(installed=True, backup=str(backup), contentHashesPreserved=10)
        print(f'Installed ten sequential Critical Care chapters. Backup: {backup}', flush=True)
    output = ROOT / 'build/critical-care-chapter-order.json'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=Path, default=DEFAULT_DATA)
    parser.add_argument('--install', action='store_true')
    args = parser.parse_args()
    run(args.data.resolve(), args.install)
