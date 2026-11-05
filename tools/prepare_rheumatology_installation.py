"""Map 328 original rheumatology questions once into existing or new topical chapters."""
import copy,json
from collections import Counter
from qbank_authoring import ROOT,validate

def prepare():
    source={b['chapterOrder']:b for p in (ROOT/'completed/Rheumatology').glob('*/*/questions.json') for b in [json.loads(p.read_text(encoding='utf-8'))]}
    assert len(source)==10 and sum(len(b['questions']) for b in source.values())==328
    specs=[(1,'I. Articular and musculoskeletal',1),(1,'I. Articular and musculoskeletal',2),(1,'I. Articular and musculoskeletal',3),
      (2,'II. Autoinflammatory fever syndromes',8),(3,'III. Immunology and Biologics',10),
      (4,'IV. Connective tissue disorders',4),(4,'IV. Connective tissue disorders',5),(4,'IV. Connective tissue disorders',6),
      (5,'V. Vasculitic syndromes',7),(6,'VI. Sarcoidosis',9)]
    seen=set();topics={};report=[];counts=Counter()
    for order,doc,index in specs:
        bank=copy.deepcopy(source[index]);topics[order]=topics.get(order,0)+1
        bank.update(document=doc,chapterOrder=order,topicOrder=topics[order],sourceAuthoredChapter=source[index]['document'])
        validate(bank)
        for item in bank['questions']:
            assert item['id'] not in seen;seen.add(item['id']);counts[item['correctIndex']]+=1
        dest=ROOT/'install-ready/Rheumatology'/f'{order:02}. {doc.split(". ",1)[1]}'/f'{topics[order]:02}. {bank["headingText"]}'
        dest.mkdir(parents=True,exist_ok=True)
        (dest/'questions.json').write_text(json.dumps(bank,ensure_ascii=False,indent=2),encoding='utf-8')
        report.append(dict(document=doc,topic=bank['headingText'],questions=len(bank['questions']),sourceChapter=index))
    assert len(seen)==328 and len(topics)==6 and all(counts[i]==82 for i in range(4))
    assert seen=={q['id'] for b in source.values() for q in b['questions']}
    (ROOT/'rheumatology-mapping-report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(dict(questions=len(seen),numberedChapters=len(topics),topicFiles=len(report),answerDistribution=dict(counts))))

if __name__=='__main__':prepare()
