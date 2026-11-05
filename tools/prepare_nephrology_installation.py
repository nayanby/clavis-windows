"""Map ten authored renal topics onto the five existing numbered note chapters."""
import copy,json
from qbank_authoring import ROOT,validate

def prepare():
    source={b['chapterOrder']:b for p in (ROOT/'completed/Nephrology').glob('*/*/questions.json')
        for b in [json.loads(p.read_text(encoding='utf-8'))]}
    assert len(source)==10 and sum(len(b['questions']) for b in source.values())==368
    specs=[(1,'I. Basics and AKI',[1,5]),(2,'II. CKD',[2,10]),(3,'III. Dialysis',[6]),
        (4,'IV. Electrolytes and metabolic interpretation',[7,8,9]),(5,'V. Glomerular disease',[3,4])]
    seen=set();report=[]
    for order,doc,chapters in specs:
        for topic_order,index in enumerate(chapters,1):
            original=source[index];bank=copy.deepcopy(original)
            bank.update(document=doc,chapterOrder=order,topicOrder=topic_order,sourceAuthoredChapter=original['document'])
            validate(bank)
            ids={q['id'] for q in bank['questions']};assert not ids&seen;seen|=ids
            dest=ROOT/'install-ready/Nephrology'/f'{order:02}. {doc.split(". ",1)[1]}'/f'{topic_order:02}. {bank["headingText"]}'
            dest.mkdir(parents=True,exist_ok=True)
            (dest/'questions.json').write_text(json.dumps(bank,ensure_ascii=False,indent=2),encoding='utf-8')
            report.append(dict(document=doc,topic=bank['headingText'],questions=len(bank['questions']),sourceChapter=index))
    assert len(seen)==368 and len(report)==10
    (ROOT/'nephrology-mapping-report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(dict(questions=len(seen),chapters=len(specs),topicFiles=len(report))))

if __name__=='__main__':prepare()
