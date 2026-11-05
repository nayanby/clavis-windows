"""Disjointly map 348 original respiratory questions to fifteen existing note chapters."""
import copy,json,random
from collections import Counter
from qbank_authoring import ROOT,render,validate

def prepare():
    source={b['chapterOrder']:b for p in (ROOT/'completed/Respiratory system').glob('*/*/questions.json')
        for b in [json.loads(p.read_text(encoding='utf-8'))]}
    assert len(source)==12 and sum(len(b['questions']) for b in source.values())==348
    specs=[(1,'I. COPD',2,None,None),(2,'II. Astham',1,None,None),
        (3,'III. ILD',3,None,None),
        (4,'IV. Pneumonia',4,list(range(23))+[31],'Pneumonia and Opportunistic Infections'),
        (4,'IV. Pneumonia',5,None,None),
        (5,'V. ARDS',8,list(range(18,36)),'ARDS'),
        (6,'VI. Aspergillosis',4,list(range(23,31)),'Aspergillus and Other Fungal Lung Syndromes'),
        (7,'VII. Respiratory failure',8,list(range(18)),'Respiratory Failure and Ventilatory Support'),
        (8,'VIII. Pleural disesae',6,list(range(22)),'Pleural Fluid, Infection and Malignancy'),
        (9,'IX. Pneumothorax',6,list(range(22,32)),'Pneumothorax'),
        (10,'X. Pulmonary hypertension',7,None,'Pulmonary Embolism and Pulmonary Hypertension'),
        (11,'XI. Bronchiectasis',9,None,None),(12,'XII. OSA and OHS',10,None,None),
        (13,'XIII. Pulmonary nodule',11,list(range(8)),'Pulmonary Nodules and Screening'),
        (14,'XIV. PFT',12,None,None),
        (15,'XV. Lung cancer',11,list(range(8,24)),'Lung Cancer')]
    seen=set();topics={};report=[];distribution=Counter()
    for order,doc,index,selection,title in specs:
        original=source[index];bank=copy.deepcopy(original)
        if selection is not None:bank['questions']=[bank['questions'][i] for i in selection]
        n=len(bank['questions']);counts=[n//4]*4
        # Balance partial banks together: 18+18 and 22+10 retain exact chapter-wide balance.
        extra={5:[0,1],7:[2,3],8:[0,1],9:[2,3]}.get(order,[])
        assert len(extra)==n%4
        for i in extra:counts[i]+=1
        positions=[i for i,count in enumerate(counts) for _ in range(count)]
        random.Random(902000+order+index).shuffle(positions)
        for item,pos in zip(bank['questions'],positions):
            assert item['id'] not in seen;seen.add(item['id'])
            old=item['correctIndex'];answer=item['options'][old]
            item['options'][old],item['options'][pos]=item['options'][pos],item['options'][old]
            for other in item['explanationTeaching']['otherOptions']:
                if other['optionIndex']==pos:other['optionIndex']=old
                elif other['optionIndex']==old:other['optionIndex']=pos
            item['correctIndex']=pos;item['explanationTeaching']['otherOptions'].sort(key=lambda a:a['optionIndex'])
            assert item['options'][pos]==answer;render(item);distribution[pos]+=1
        topics[order]=topics.get(order,0)+1
        bank.update(document=doc,headingText=title or original['headingText'],chapterOrder=order,
            topicOrder=topics[order],sourceAuthoredChapter=original['document'],targetQuestions=n)
        validate(bank)
        dest=ROOT/'install-ready/Respiratory system'/f'{order:02}. {doc.split(". ",1)[1]}'/f'{topics[order]:02}. {bank["headingText"]}'
        dest.mkdir(parents=True,exist_ok=True)
        (dest/'questions.json').write_text(json.dumps(bank,ensure_ascii=False,indent=2),encoding='utf-8')
        report.append(dict(document=doc,topic=bank['headingText'],questions=n,sourceChapter=index))
    assert len(seen)==348 and len(report)==16 and len(topics)==15
    assert seen=={q['id'] for b in source.values() for q in b['questions']}
    assert all(distribution[i]==87 for i in range(4)),distribution
    (ROOT/'respiratory-mapping-report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(dict(questions=len(seen),chapters=len(topics),topicFiles=len(report),answerDistribution=dict(distribution))))

if __name__=='__main__':prepare()
