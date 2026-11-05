"""Map 11 authored chapters to the existing 14 numbered note chapters without duplicate questions."""
import copy,json,random
from qbank_authoring import ROOT,render,validate
DEST=ROOT/'install-ready/Liver'

def prepare():
    source={b['chapterOrder']:b for p in (ROOT/'completed/Liver').glob('*/*/questions.json')
        for b in [json.loads(p.read_text(encoding='utf-8'))]}
    assert len(source)==11
    # Selected original-question indexes form disjoint complete partitions.
    lft=[0,1,2,3,11,12,13,14,15,16,17,19]
    specs=[
        (1,'I. LFT interpretation','Liver Test Interpretation',1,lft),
        (2,'II. Hyperbilirubinemia','Hyperbilirubinemia and Jaundice',1,[i for i in range(20) if i not in lft]),
        (3,'III. Viral hepatitis','Viral Hepatitis',2,None),
        (4,'IV. AUD and ALD','Alcohol-associated Liver Disease',3,None),
        (5,'V. MASLD, Autoimmune hepatitis & Metabolic Liver Diseases','MASLD and Metabolic Liver Disease',4,None),
        (5,'V. MASLD, Autoimmune hepatitis & Metabolic Liver Diseases','Autoimmune Hepatitis',5,list(range(12))),
        (12,'XII. Biliary disease','Cholestatic Disease',5,list(range(12,32))),
        (7,'VII. Portal hypertension','Portal Hypertension and Variceal Bleeding',6,list(range(12))),
        (6,'VI. CLD and cirrhosis','Cirrhosis and Its Complications',6,list(range(12,36))),
        (10,'X. Acute liver failure','Acute Liver Failure',7,list(range(13))),
        (9,'IX. Drug induced liver injury','Drug-induced Liver Injury',7,list(range(13,28))),
        (8,'VIII. Budd Chiari syndrome','Hepatic Vascular Disorders',8,None),
        (11,'XI. Liver abscess','Liver Abscess and Hydatid Disease',9,None),
        (13,'XIII. Hepatocellular carcinoma','Liver Tumors and Transplantation',10,None),
        (14,'XIV. Liver diseased in pregnancy','Liver Disease in Pregnancy',11,None)]
    result=[];offset=0;seen=set();topic_order={}
    for order,doc,title,source_order,indexes in specs:
        bank=source[source_order];indexes=indexes if indexes is not None else range(len(bank['questions']))
        questions=copy.deepcopy([bank['questions'][i] for i in indexes])
        positions=[i%4 for i in range(offset,offset+len(questions))]
        random.Random(72000+offset).shuffle(positions);offset+=len(questions)
        for q,pos in zip(questions,positions):
            assert q['id'] not in seen;seen.add(q['id'])
            old=q['correctIndex'];answer=q['options'][old]
            q['options'][old],q['options'][pos]=q['options'][pos],q['options'][old]
            for a in q['explanationTeaching']['otherOptions']:
                if a['optionIndex']==pos:a['optionIndex']=old
                elif a['optionIndex']==old:a['optionIndex']=pos
            q['correctIndex']=pos;q['explanationTeaching']['otherOptions'].sort(key=lambda a:a['optionIndex'])
            assert q['options'][pos]==answer;render(q)
        topic_order[order]=topic_order.get(order,0)+1
        row=dict(folder='Liver',document=doc,headingText=title,chapterOrder=order,topicOrder=topic_order[order],
            targetQuestions=len(questions),questions=questions,sourceAuthoredChapter=bank['document'])
        report=validate(row)
        directory=DEST/f'{order:02}. {doc.split(". ",1)[1]}'/f'{topic_order[order]:02}. {title}'
        directory.mkdir(parents=True,exist_ok=True)
        (directory/'questions.json').write_text(json.dumps(row,ensure_ascii=False,indent=2),encoding='utf-8')
        result.append(dict(document=doc,topic=title,questions=len(questions),distribution=report['answerDistribution']))
    assert offset==276 and len(seen)==276
    assert seen=={q['id'] for b in source.values() for q in b['questions']}
    print(json.dumps(dict(questions=offset,uniqueIds=len(seen),topicFiles=len(result),chapters=len(topic_order),mapping=result),indent=2))

if __name__=='__main__':prepare()
