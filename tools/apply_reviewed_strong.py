"""Apply explicitly reviewed Strong-style ranges while preserving DOCX content."""
import copy,io,json
from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main';N={'w':W};Q=lambda v:'{'+W+'}'+v

def apply_spans(raw,choices):
 with ZipFile(io.BytesIO(raw)) as z:
  d=E.fromstring(z.read('word/document.xml'));paragraphs=d.findall('.//w:p',N);before=''.join(d.xpath('//w:t/text()',namespaces=N));marked=0
  for choice in choices:
   p=paragraphs[choice['paragraph']];text=''.join(p.xpath('.//w:t/text()',namespaces=N));ranges=[]
   for phrase in choice['spans']:
    start=text.find(phrase)
    if start<0:raise ValueError(f"Paragraph {choice['paragraph']}: missing {phrase!r}")
    ranges.append((start,start+len(phrase)));marked+=1
   offset=0
   for run in list(p.findall('.//w:r',N)):
    text_nodes=run.findall('w:t',N);length=sum(len(t.text or '') for t in text_nodes);start=offset;offset+=length
    if not length or not any(a<offset and b>start for a,b in ranges):continue
    parent=run.getparent();index=parent.index(run);parent.remove(run);cursor=start
    original_pr=run.find('w:rPr',N)
    def append_piece(child,selected=False):
     nonlocal index
     piece=E.Element(Q('r'),dict(run.attrib));pr=copy.deepcopy(original_pr) if original_pr is not None else E.Element(Q('rPr'))
     if selected:
      for c in list(pr):
       if E.QName(c).localname in {'rStyle','color','shd','highlight','b','bCs'}:pr.remove(c)
      st=E.Element(Q('rStyle'));st.set(Q('val'),'Strong');pr.insert(0,st)
     if len(pr):piece.append(pr)
     piece.append(child);parent.insert(index,piece);index+=1
    for child in run:
     if child.tag==Q('rPr'):continue
     if child.tag!=Q('t'):append_piece(copy.deepcopy(child));continue
     value=child.text or '';cuts={0,len(value)}
     for a,b in ranges:
      if a<cursor+len(value) and b>cursor:cuts.update([max(0,a-cursor),min(len(value),b-cursor)])
     boundaries=sorted(cuts)
     for lo,hi in zip(boundaries,boundaries[1:]):
      if hi==lo:continue
      selected=any(a<=cursor+lo and b>=cursor+hi for a,b in ranges)
      t=copy.deepcopy(child);t.set('{http://www.w3.org/XML/1998/namespace}space','preserve');t.text=value[lo:hi];append_piece(t,selected)
     cursor+=len(value)
  assert ''.join(d.xpath('//w:t/text()',namespaces=N))==before
  out=io.BytesIO()
  with ZipFile(out,'w') as dest:
   for info in z.infolist():dest.writestr(copy.copy(info),E.tostring(d,xml_declaration=True,encoding='UTF-8',standalone=True) if info.filename=='word/document.xml' else z.read(info.filename))
  result=out.getvalue()
  with ZipFile(io.BytesIO(result)) as check:
   for name in z.namelist():
    if name!='word/document.xml':assert check.read(name)==z.read(name)
  return result,marked

if __name__=='__main__':
 import argparse
 a=argparse.ArgumentParser();a.add_argument('document',type=Path);a.add_argument('review',type=Path);args=a.parse_args();data,count=apply_spans(args.document.read_bytes(),json.loads(args.review.read_text(encoding='utf-8')));args.document.write_bytes(data);print('Applied Strong to',count,'reviewed exam-point spans')
