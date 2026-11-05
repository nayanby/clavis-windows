"""Disjointly map 328 original hematology questions to eleven existing note chapters."""
import copy,json,random
from collections import Counter
from qbank_authoring import ROOT,render,validate

def prepare():
    source={b['chapterOrder']:b for p in (ROOT/'completed/Hematology').glob('*/*/questions.json')
        for b in [json.loads(p.read_text(encoding='utf-8'))]}
    assert len(source)==10 and sum(len(b['questions']) for b in source.values())==328
    specs=[(1,'I. Hemat basics',1,list(range(22)),'Approach to Anemia and Iron Deficiency'),
        (2,'II. Hypoproliferative anemia',2,None,None),(3,'III. Hemolytic anemia',3,None,None),
        (4,'IV. Pancytopenia',4,None,None),(5,'V. Plasma cell',7,None,None),
        (6,'VI. WBCs',5,None,'Myeloid Neoplasms and Marrow Dysplasia'),(6,'VI. WBCs',6,None,None),
        (7,'VII. Coagulation disorders',9,list(range(16)),'Coagulation and Bleeding Disorders'),
        (8,'VIII. Platelet disorders',8,None,None),
        (9,'IX. Diseases of metabolism',1,list(range(22,28)),'Hemochromatosis and Iron Overload'),
        (10,'X. Quesions',10,None,None),
        (11,'XI. VTE detailed',9,list(range(16,32)),'Venous Thromboembolism and Thrombophilia')]
    seen=set();topics={};report=[];distribution=Counter()
    for order,doc,index,selection,title in specs:
        original=source[index];bank=copy.deepcopy(original)
        if selection is not None:bank['questions']=[bank['questions'][i] for i in selection]
        n=len(bank['questions']);counts=[n//4]*4
        # Balance the 22+6 split together to preserve whole-subject answer balance.
        extra={1:[0,1],9:[2,3]}.get(order,[])
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
        dest=ROOT/'install-ready/Hematology'/f'{order:02}. {doc.split(". ",1)[1]}'/f'{topics[order]:02}. {bank["headingText"]}'
        dest.mkdir(parents=True,exist_ok=True)
        (dest/'questions.json').write_text(json.dumps(bank,ensure_ascii=False,indent=2),encoding='utf-8')
        report.append(dict(document=doc,topic=bank['headingText'],questions=n,sourceChapter=index))
    assert len(seen)==328 and len(report)==12 and len(topics)==11
    assert seen=={q['id'] for b in source.values() for q in b['questions']}
    assert all(distribution[i]==82 for i in range(4)),distribution
    (ROOT/'hematology-mapping-report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(dict(questions=len(seen),chapters=len(topics),topicFiles=len(report),answerDistribution=dict(distribution))))

if __name__=='__main__':prepare()
