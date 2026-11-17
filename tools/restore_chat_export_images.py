"""Embed recoverable image placeholders in an exported Word copy at 4 cm height."""
import argparse
from io import BytesIO
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from docx import Document
from docx.shared import Cm
from PIL import Image


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('source', type=Path)
    parser.add_argument('destination', type=Path)
    args = parser.parse_args()
    assert args.source.resolve() != args.destination.resolve(), 'Write a separate repaired copy.'
    doc = Document(args.source)
    embedded = removed = 0
    for paragraph in list(doc.paragraphs):
        for link in paragraph._p.xpath('./w:hyperlink'):
            if 'Source image' not in ''.join(link.itertext()):
                continue
            rid = link.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
            url = doc.part.rels[rid].target_ref
            parsed = urlparse(url)
            if '/s2/favicons' in parsed.path:
                paragraph._p.getparent().remove(paragraph._p)
                removed += 1
                break
            if parsed.scheme != 'https' or parsed.hostname != 'images.openai.com':
                continue
            with urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=30) as response:
                assert response.headers.get('Content-Type', '').startswith('image/')
                data = response.read(8000001)
            assert len(data) <= 8000000
            image = Image.open(BytesIO(data)).convert('RGB')
            png = BytesIO()
            image.save(png, format='PNG')
            png.seek(0)
            paragraph.clear().add_run().add_picture(png, height=Cm(4))
            embedded += 1
            break
    assert embedded, 'No recoverable image placeholders found.'
    args.destination.parent.mkdir(parents=True, exist_ok=True)
    doc.save(args.destination)
    print(f'Embedded {embedded} image(s) at 4 cm; removed {removed} citation favicons: {args.destination}')


if __name__ == '__main__':
    main()
