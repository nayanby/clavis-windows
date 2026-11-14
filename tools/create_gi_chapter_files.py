"""Create title-only GI chapter Word files while retaining existing sources."""
from pathlib import Path
import sys
from zipfile import ZipFile, ZIP_DEFLATED
from xml.etree import ElementTree as E

ROOT=Path(__file__).resolve().parents[1]
DEST=Path(r'C:\Users\ANT-PC\OneDrive\Cortex Windows\data\files\GI & pancreas')
TEMPLATE=next((ROOT/'data/files/Research Methodology & Biostatistics').glob('01.*.docx'))
TITLES=[
 'Esophageal Disorders & GERD',
 'Gastritis, Peptic Ulcer Disease & H. pylori',
 'Upper & Lower Gastrointestinal Bleeding',
 'Malabsorption, Celiac Disease & Chronic Diarrhea',
 'Inflammatory Bowel Disease',
 'Functional GI & Motility Disorders',
 'Acute & Chronic Pancreatitis',
 'Pancreatic Cystic Lesions & Neoplasms',
 'Biliary Tract Disorders & Cholangitis',
 'GI Polyps, NETs & GI Malignancies',
 'GI Endoscopy, Imaging & Miscellaneous Disorders',
]
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
E.register_namespace('w',W)

def main():
 output=DEST if '--install' in sys.argv else ROOT/'build/gi-chapter-files'
 output.mkdir(parents=True,exist_ok=True)
 with ZipFile(TEMPLATE) as z:package={n:z.read(n) for n in z.namelist()}
 for i,title in enumerate(TITLES,1):
  name=f'{i:02}. {title}'
  root=E.fromstring(package['word/document.xml']);body=root.find(f'{{{W}}}body')
  for n in list(body):
   if n.tag!=f'{{{W}}}sectPr':body.remove(n)
  p=E.Element(f'{{{W}}}p');pr=E.SubElement(p,f'{{{W}}}pPr')
  E.SubElement(pr,f'{{{W}}}pStyle',{f'{{{W}}}val':'Title'})
  run=E.SubElement(p,f'{{{W}}}r');E.SubElement(run,f'{{{W}}}t').text=name
  body.insert(0,p)
  path=output/(name+'.docx')
  assert not path.exists(),path
  with ZipFile(path,'x',ZIP_DEFLATED) as z:
   for member,data in package.items():
    z.writestr(member,E.tostring(root,encoding='utf-8',xml_declaration=True) if member=='word/document.xml' else data)
  with ZipFile(path) as z:
   assert z.testzip() is None
   assert ''.join(E.fromstring(z.read('word/document.xml')).itertext())==name
  print(path.name)

if __name__=='__main__':main()
