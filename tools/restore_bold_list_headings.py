"""Restore short bold subsection labels stored as Normal numbered paragraphs."""
import argparse
from collections import defaultdict
from copy import copy
import json
import re
import shutil
from zipfile import ZipFile
from apply_clinical_template import DEFAULT_DATA, ROOT, NS, W, read, xml, val, serialize, signature, list_signature, sha, order_properties
from audit_document_headings import bold


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--install-staged', action='store_true')
    args = parser.parse_args()
    folder = DEFAULT_DATA / 'files'
    output = ROOT / 'build/restore-bs3'
    output.mkdir(parents=True, exist_ok=True)
    if args.install_staged:
        from repair_unintended_emphasis import install
        reports = json.loads((output / 'report.json').read_text(encoding='utf-8'))
        for r in reports:
            r.update(changed=True, staged=r['after'])
        (output / 'report.json').write_text(json.dumps(reports, indent=2), encoding='utf-8')
        install(DEFAULT_DATA, output)
        print(json.dumps(dict(installed=len(reports), headings=sum(len(r['headings']) for r in reports))))
        return
    reports = []
    for source in sorted(folder.rglob('*.docx')):
        relative = source.relative_to(folder)
        if source.name.startswith('~$') or any(p.startswith(('_', '.')) for p in relative.parts[:-1]):
            continue
        data = read(source)
        d = xml(data['word/document.xml'])
        s = xml(data['word/styles.xml'])
        n = xml(data.get('word/numbering.xml', f'<w:numbering xmlns:w="{W}"/>'.encode()))
        defs = {val(x, 'styleId'): x for x in s.findall('w:style', NS)}
        if 'Boldside3' not in defs:
            continue
        ps = d.findall('.//w:p', NS)
        lists = list_signature(d, s, n)
        content = signature(d)
        groups = defaultdict(list)
        for i, (p, listing) in enumerate(zip(ps, lists)):
            text = ''.join(p.xpath('.//w:t/text()', namespaces=NS)).strip()
            if val(p.find('w:pPr/w:pStyle', NS)) not in ('', 'Normal'):
                continue
            if not listing or listing[0] != 'decimal' or not bold(p, defs):
                continue
            if p.xpath('ancestor::w:tc|ancestor::w:txbxContent|.//w:drawing|.//w:fldSimple', namespaces=NS):
                continue
            if not text or len(text) > 100 or len(text.split()) > 10 or re.search(r'[.!?;:=<>→⚬]', text):
                continue
            # A subsection has explanatory bullet content immediately below it.
            following = next((j for j in range(i+1, len(ps)) if ''.join(ps[j].xpath('.//w:t/text()', namespaces=NS)).strip()), None)
            if following is None or not lists[following] or lists[following][0] != 'bullet':
                continue
            groups[listing[-1]].append((i, text))
        targets = [item for group in groups.values() if len(group) >= 2 for item in group]
        if not targets:
            continue
        for i, text in targets:
            p = ps[i]
            props = p.find('w:pPr', NS)
            style = props.find('w:pStyle', NS)
            if style is None:
                from lxml import etree as E
                style = E.Element(f'{{{W}}}pStyle'); props.insert(0, style)
            style.set(f'{{{W}}}val', 'Boldside3')
            # BS3 inherits ListParagraph in the template: explicitly cancel lists.
            num = props.find('w:numPr', NS)
            for child in list(num): num.remove(child)
            from lxml import etree as E
            E.SubElement(num, f'{{{W}}}numId', {f'{{{W}}}val': '0'})
            for tag in ('spacing', 'ind', 'tabs'):
                for node in props.findall('w:'+tag, NS): props.remove(node)
        order_properties(d)
        assert signature(d) == content
        after = list_signature(d, s, n)
        expected = list(lists)
        for i, _ in targets: expected[i] = None
        assert after == expected
        destination = output / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        with ZipFile(source) as z, ZipFile(destination, 'w') as out:
            out.comment = z.comment
            for info in z.infolist():
                out.writestr(copy(info), serialize(d) if info.filename == 'word/document.xml' else z.read(info.filename))
        verified = read(destination)
        assert all(verified[k] == v for k, v in data.items() if k != 'word/document.xml')
        reports.append(dict(file=relative.as_posix(), before=sha(source), after=sha(destination), headings=targets))
        print(json.dumps(dict(file=relative.as_posix(), headings=targets)), flush=True)
    (output / 'report.json').write_text(json.dumps(reports, indent=2), encoding='utf-8')
    print(json.dumps(dict(files=len(reports), headings=sum(len(r['headings']) for r in reports))))


if __name__ == '__main__': main()
