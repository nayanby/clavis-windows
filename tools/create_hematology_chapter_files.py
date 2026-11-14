"""Create the twelve requested title-only Hematology Word chapter files."""
from pathlib import Path
import sys
from zipfile import ZipFile, ZIP_DEFLATED
from xml.etree import ElementTree as E

ROOT = Path(__file__).resolve().parents[1]
DEST = Path(r'C:\Users\ANT-PC\OneDrive\Cortex Windows\data\files\Hematology')
TEMPLATE = next((ROOT / 'data/files/Research Methodology & Biostatistics').glob('01.*.docx'))
TITLES = [
    'Approach to Anemia, RBC Indices & Iron Disorders',
    'Megaloblastic & Other Macrocytic Anemias',
    'Hemolytic Anemias & Hemoglobin Disorders',
    'Bone-Marrow Failure, Aplastic Anemia & MDS',
    'Myeloproliferative Neoplasms',
    'Acute Leukemias',
    'Chronic Lymphoid Leukemias & Related Disorders',
    'Lymphomas',
    'Plasma-Cell Disorders & Amyloidosis',
    'Platelets, Bleeding Disorders & Coagulation',
    'Thrombosis, Thrombophilia & Anticoagulants',
    'Transfusion Medicine, Hematologic Emergencies & Stem-Cell Transplantation',
]
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
E.register_namespace('w', W)


def main():
    output = DEST if '--install' in sys.argv else ROOT / 'build/hematology-chapter-files'
    output.mkdir(parents=True, exist_ok=True)
    with ZipFile(TEMPLATE) as z:
        package = {name: z.read(name) for name in z.namelist()}
    targets = [output / f'{i:02}. {title}.docx' for i, title in enumerate(TITLES, 1)]
    assert all(not path.exists() for path in targets), 'A requested chapter already exists'
    for path in targets:
        root = E.fromstring(package['word/document.xml'])
        body = root.find(f'{{{W}}}body')
        for node in list(body):
            if node.tag != f'{{{W}}}sectPr':
                body.remove(node)
        paragraph = E.Element(f'{{{W}}}p')
        props = E.SubElement(paragraph, f'{{{W}}}pPr')
        E.SubElement(props, f'{{{W}}}pStyle', {f'{{{W}}}val': 'Title'})
        run = E.SubElement(paragraph, f'{{{W}}}r')
        E.SubElement(run, f'{{{W}}}t').text = path.stem
        body.insert(0, paragraph)
        with ZipFile(path, 'x', ZIP_DEFLATED) as z:
            for member, content in package.items():
                z.writestr(member, E.tostring(root, encoding='utf-8', xml_declaration=True)
                           if member == 'word/document.xml' else content)
        with ZipFile(path) as z:
            assert z.testzip() is None
            assert ''.join(E.fromstring(z.read('word/document.xml')).itertext()) == path.stem
        print(path.name)


if __name__ == '__main__':
    main()
