"""Map all 136 Psychiatry questions; preserve the existing psychotic chapter identity."""
import copy,json
from collections import Counter
from qbank_authoring import ROOT,validate

def prepare():
    source={b['chapterOrder']:b for p in (ROOT/'completed/Psychiatry').glob('*/*/questions.json') for b in [json.loads(p.read_text(encoding='utf-8'))]}
    assert set(source)==set(range(1,7)) and sum(len(b['questions']) for b in source.values())==136
    specs=[(1,'I. Psychotic disorders',2),(2,'II. Mood Disorders',1),
      (3,'III. Anxiety, Trauma and Obsessive-compulsive Disorders',3),(4,'IV. Substance-use Disorders',4),
      (5,'V. Delirium and Neuropsychiatry',5),(6,'VI. Psychopharmacology and Psychiatric Emergencies',6)]
    seen=set();counts=Counter();report=[]
    for order,doc,index in specs:
        bank=copy.deepcopy(source[index]);bank.update(document=doc,chapterOrder=order,topicOrder=1,sourceAuthoredChapter=source[index]['document'])
        validate(bank)
        for item in bank['questions']:
            assert item['id'] not in seen;seen.add(item['id']);counts[item['correctIndex']]+=1
        dest=ROOT/'install-ready/Psychiatry'/f'{order:02}. {doc.split(". ",1)[1]}'/f'01. {bank["headingText"]}'
        dest.mkdir(parents=True,exist_ok=True);(dest/'questions.json').write_text(json.dumps(bank,ensure_ascii=False,indent=2),encoding='utf-8')
        report.append(dict(document=doc,topic=bank['headingText'],questions=len(bank['questions']),sourceChapter=index))
    assert len(seen)==136 and all(counts[i]==34 for i in range(4))
    assert seen=={q['id'] for b in source.values() for q in b['questions']}
    (ROOT/'psychiatry-mapping-report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(dict(questions=len(seen),numberedChapters=6,topicFiles=6,answerDistribution=dict(counts))))

if __name__=='__main__':prepare()
