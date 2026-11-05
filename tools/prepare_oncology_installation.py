"""Map 208 original Oncology questions into seven numbered chapters, retaining the Basics note identity."""
import copy,json
from collections import Counter
from qbank_authoring import ROOT,validate

def prepare():
    source={b['chapterOrder']:b for p in (ROOT/'completed/Oncology').glob('*/*/questions.json') for b in [json.loads(p.read_text(encoding='utf-8'))]}
    assert set(source)==set(range(1,8)) and sum(len(b['questions']) for b in source.values())==208
    numerals=['I','II','III','IV','V','VI','VII'];seen=set();counts=Counter();report=[]
    for order,original in sorted(source.items()):
        bank=copy.deepcopy(original);doc='Basics' if order==1 else f'{numerals[order-1]}. {original["document"]}'
        bank.update(document=doc,chapterOrder=order,topicOrder=1,sourceAuthoredChapter=original['document'])
        validate(bank)
        for item in bank['questions']:
            assert item['id'] not in seen;seen.add(item['id']);counts[item['correctIndex']]+=1
        dest=ROOT/'install-ready/Oncology'/f'{order:02}. {doc.split(". ",1)[-1]}'/f'01. {bank["headingText"]}'
        dest.mkdir(parents=True,exist_ok=True);(dest/'questions.json').write_text(json.dumps(bank,ensure_ascii=False,indent=2),encoding='utf-8')
        report.append(dict(document=doc,topic=bank['headingText'],questions=len(bank['questions']),sourceChapter=order))
    assert len(seen)==208 and all(counts[i]==52 for i in range(4))
    assert seen=={q['id'] for b in source.values() for q in b['questions']}
    (ROOT/'oncology-mapping-report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(dict(questions=len(seen),numberedChapters=7,topicFiles=7,answerDistribution=dict(counts))))

if __name__=='__main__':prepare()
