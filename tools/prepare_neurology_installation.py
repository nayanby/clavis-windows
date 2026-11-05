"""Map all 548 original Neurology questions to the existing 17 note chapters."""
import copy,json,random
from qbank_authoring import ROOT,render,validate

def prepare():
    source={b['chapterOrder']:b for p in (ROOT/'completed/Neurology').glob('*/*/questions.json')
        for b in [json.loads(p.read_text(encoding='utf-8'))]}
    assert len(source)==16 and sum(len(b['questions']) for b in source.values())==548
    specs=[
        (1,'I. Clinical examination','Clinical Localization and Neurodiagnostics',16,None),
        (2,'II. Neuropathy basics','Neuropathy Assessment and Focal Disorders',6,list(range(22,44))),
        (3,'III. Polyneuropathy','Inflammatory and Immune Neuropathies',6,list(range(22))),
        (4,'IV. Neuromuscular junction disorders','Neuromuscular Junction Disorders',7,None),
        (5,'V. Myopathy','Myopathies',8,None),
        (6,'VI. Motor neuron disease','Motor Neuron Disease',9,None),
        (7,'VII. Spinal cord disorders','Spinal Cord Disorders',10,None),
        (8,'VIII. Movement disorders','Other Movement Disorders',3,list(range(22,44))),
        (9,'IX. Ataxia','Ataxia and Cerebellar Disorders',12,None),
        (10,'X. Parkinsonism and dementia','Parkinson Disease',3,list(range(22))),
        (10,'X. Parkinsonism and dementia','Dementia and Cognitive Disorders',4,None),
        (11,'XI. Demyelinating disease and neuroimmunology','Demyelination and Neuroimmunology',5,None),
        (12,'XII. Headache','Headache and Facial Pain',11,None),
        (13,'XIII. Stroke','Stroke and Cerebrovascular Disease',1,None),
        (15,'XV. Seizure and epilepsy','Seizures and Epilepsy',2,None),
        (16,'XVI. Sleep medicine','Sleep Disorders',14,None),
        (17,'XVII. Infections','CNS Infections',13,None),
        (18,'XVIII. Extra topics','Neurocritical Care and Coma',15,None)]
    seen=set();offset=0;topics={};result=[]
    for order,doc,title,src,indexes in specs:
        bank=source[src];indexes=indexes if indexes is not None else range(len(bank['questions']))
        questions=copy.deepcopy([bank['questions'][i] for i in indexes])
        positions=[i%4 for i in range(offset,offset+len(questions))]
        random.Random(87000+offset).shuffle(positions);offset+=len(questions)
        for q,pos in zip(questions,positions):
            assert q['id'] not in seen;seen.add(q['id'])
            old=q['correctIndex'];answer=q['options'][old]
            q['options'][old],q['options'][pos]=q['options'][pos],q['options'][old]
            for a in q['explanationTeaching']['otherOptions']:
                if a['optionIndex']==pos:a['optionIndex']=old
                elif a['optionIndex']==old:a['optionIndex']=pos
            q['correctIndex']=pos;q['explanationTeaching']['otherOptions'].sort(key=lambda a:a['optionIndex'])
            assert q['options'][pos]==answer;render(q)
        topics[order]=topics.get(order,0)+1
        row=dict(folder='Neurology',document=doc,headingText=title,chapterOrder=order,topicOrder=topics[order],
            targetQuestions=len(questions),questions=questions,sourceAuthoredChapter=bank['document'])
        report=validate(row)
        directory=ROOT/'install-ready/Neurology'/f'{order:02}. {doc.split(". ",1)[1]}'/f'{topics[order]:02}. {title}'
        directory.mkdir(parents=True,exist_ok=True)
        (directory/'questions.json').write_text(json.dumps(row,ensure_ascii=False,indent=2),encoding='utf-8')
        result.append(dict(document=doc,topic=title,questions=len(questions),distribution=report['answerDistribution']))
    assert offset==len(seen)==548 and len(topics)==17 and len(result)==18
    assert seen=={q['id'] for b in source.values() for q in b['questions']}
    (ROOT/'neurology-mapping-report.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(dict(questions=offset,uniqueIds=len(seen),topicFiles=len(result),chapters=len(topics))))

if __name__=='__main__':prepare()
