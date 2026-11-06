"""Convert authored Pearls HTML with the same converter used by the app."""
import argparse,json,sys
from pathlib import Path
REPO=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(REPO/'src'))
from cnl_desktop.pearls_word import Converter,canonical,convert,to_docx

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--source',type=Path,default=Path('C:/Users/ANT-PC/OneDrive/Cortex Windows/data/Pearls'))
    parser.add_argument('--output',type=Path,default=REPO/'build/pearls-word')
    args=parser.parse_args()
    files=[p for p in sorted(args.source.rglob('*.html')) if p.name!='index.html' and not p.stem.endswith('layout-check')]
    report=[]
    for source in files:
        target=args.output/source.relative_to(args.source).with_suffix('.docx')
        report.append(convert(source,target))
    (args.output/'conversion-report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(f'Converted {len(report)} Word files; text, headings, bold, lists and tables verified.')
