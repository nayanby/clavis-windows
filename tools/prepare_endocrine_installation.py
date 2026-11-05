"""Map all 380 original Endocrine questions to ten existing numbered note chapters."""
import copy,json,random
from qbank_authoring import ROOT,render,validate

def prepare():
    source={b['chapterOrder']:b for p in (ROOT/'completed/Endocrine').glob('*/*/questions.json')
        for b in [json.loads(p.read_text(encoding='utf-8'))]}
    assert len(source)==11 and sum(len(b['questions']) for b in source.values())==380
    specs=[(1,'I. Basics',11,None,None),(2,'II. Diabetes mellitus',1,None,None),
        (2,'II. Diabetes mellitus',2,None,None),(2,'II. Diabetes mellitus',3,None,None),
        (3,'III. Pituitary',4,None,None),(4,'IV. Thyroid gland',5,None,None),
        (5,'V. Adrenal',6,None,None),(6,'VI. Calcium metabolism',7,None,None),
        (7,'VII. Disorders of intermediary metabolism',8,list(range(16,24)),'Metabolic Liver Disease and Lipodystrophy'),
        (8,'VIII. Dyslipidemia',9,None,None),
        (9,'IX. Obesity',8,list(range(16)),'Obesity Treatment and Bariatric Care'),
        (10,'X. PCOS',10,None,None)]
    seen=set();topics={};report=[]
    for order,doc,index,selection,title in specs:
        original=source[index];bank=copy.deepcopy(original)
        if selection is not None:bank['questions']=[bank['questions'][i] for i in selection]
        positions=list(range(4))*(len(bank['questions'])//4)
        assert len(positions)==len(bank['questions'])
        random.Random(901000+order+index).shuffle(positions)
        for item,pos in zip(bank['questions'],positions):
            assert item['id'] not in seen;seen.add(item['id'])
            old=item['correctIndex'];answer=item['options'][old]
            item['options'][old],item['options'][pos]=item['options'][pos],item['options'][old]
            for other in item['explanationTeaching']['otherOptions']:
                if other['optionIndex']==pos:other['optionIndex']=old
                elif other['optionIndex']==old:other['optionIndex']=pos
            item['correctIndex']=pos;item['explanationTeaching']['otherOptions'].sort(key=lambda a:a['optionIndex'])
            assert item['options'][pos]==answer;render(item)
        topics[order]=topics.get(order,0)+1
        bank.update(document=doc,headingText=title or original['headingText'],chapterOrder=order,
            topicOrder=topics[order],sourceAuthoredChapter=original['document'],targetQuestions=len(bank['questions']))
        validate(bank)
        dest=ROOT/'install-ready/Endocrine'/f'{order:02}. {doc.split(". ",1)[1]}'/f'{topics[order]:02}. {bank["headingText"]}'
        dest.mkdir(parents=True,exist_ok=True)
        (dest/'questions.json').write_text(json.dumps(bank,ensure_ascii=False,indent=2),encoding='utf-8')
        report.append(dict(document=doc,topic=bank['headingText'],questions=len(bank['questions']),sourceChapter=index))
    assert len(seen)==380 and len(report)==12 and len(topics)==10
    assert seen=={q['id'] for b in source.values() for q in b['questions']}
    (ROOT/'endocrine-mapping-report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(dict(questions=len(seen),chapters=len(topics),topicFiles=len(report))))

if __name__=='__main__':prepare()
