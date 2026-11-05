"""Map every authored infection question exactly once to numbered topical chapters."""
import copy,json,random
from collections import Counter
from qbank_authoring import ROOT,render,validate

def prepare():
    source={b['chapterOrder']:b for p in (ROOT/'completed/Infectious disease').glob('*/*/questions.json') for b in [json.loads(p.read_text(encoding='utf-8'))]}
    assert len(source)==13 and sum(len(b['questions']) for b in source.values())==404
    specs=[(1,'I. Pyrexia of unknown origin',1,None,None),(2,'II. Sepsis',2,None,None),
      (3,'III. HIV AIDS',3,None,None),(4,'IV. Tuberculosis',4,None,None),
      (5,'V. Leprosy',13,None,None),(6,'VI. UTI and urosepsis',7,list(range(14)),'Urinary Tract Infection and Urosepsis'),
      (7,'VII. Tetanus',6,[30,31],'Tetanus'),(11,'XI. Fungal infections comprehensive',9,None,None),
      (12,'XII. Mosquito borne disease',8,list(range(22))+[38,39,40],'Mosquito-borne Infections'),
      (13,'XIII. Typhoid',8,list(range(32,38)),'Typhoid and Enteric Fever'),
      (14,'XIV. Infective Endocarditis and Bacteremia',5,None,None),
      (15,'XV. Respiratory and CNS Infections',6,list(range(30)),'Respiratory and CNS Infections'),
      (16,'XVI. Intraabdominal Infections',7,list(range(14,28)),'Intraabdominal Infections'),
      (17,'XVII. Other Tropical Infections',8,list(range(22,32))+[41,42,43],'Scrub Typhus, Leptospirosis and Other Tropical Infections'),
      (18,'XVIII. Parasitic Infections',10,None,None),(19,'XIX. Antimicrobial Resistance and Safety',11,None,None),
      (20,'XX. Vaccination and Postexposure Prophylaxis',12,None,None)]
    seen=set();distribution=Counter();report=[]
    for order,doc,index,selection,title in specs:
        original=source[index];bank=copy.deepcopy(original)
        if selection is not None:bank['questions']=[bank['questions'][i] for i in selection]
        n=len(bank['questions']);counts=[n//4]*4
        for i in sorted(range(4),key=lambda j:(distribution[j],j))[:n%4]:counts[i]+=1
        positions=[i for i,count in enumerate(counts) for _ in range(count)]
        random.Random(903000+order).shuffle(positions)
        for item,pos in zip(bank['questions'],positions):
            assert item['id'] not in seen;seen.add(item['id'])
            old=item['correctIndex'];answer=item['options'][old]
            item['options'][old],item['options'][pos]=item['options'][pos],item['options'][old]
            for other in item['explanationTeaching']['otherOptions']:
                if other['optionIndex']==pos:other['optionIndex']=old
                elif other['optionIndex']==old:other['optionIndex']=pos
            item['correctIndex']=pos;item['explanationTeaching']['otherOptions'].sort(key=lambda a:a['optionIndex'])
            assert item['options'][pos]==answer;render(item);distribution[pos]+=1
        bank.update(document=doc,headingText=title or original['headingText'],chapterOrder=order,topicOrder=1,sourceAuthoredChapter=original['document'],targetQuestions=n)
        validate(bank)
        dest=ROOT/'install-ready/Infectious disease'/f'{order:02}. {doc.split(". ",1)[1]}'/f'01. {bank["headingText"]}'
        dest.mkdir(parents=True,exist_ok=True)
        (dest/'questions.json').write_text(json.dumps(bank,ensure_ascii=False,indent=2),encoding='utf-8')
        report.append(dict(document=doc,topic=bank['headingText'],questions=n,sourceChapter=index))
    assert len(seen)==404 and seen=={q['id'] for b in source.values() for q in b['questions']}
    assert all(distribution[i]==101 for i in range(4)),distribution
    (ROOT/'infectious-mapping-report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(dict(questions=len(seen),chapters=len(report),answerDistribution=dict(distribution))))

if __name__=='__main__':prepare()
