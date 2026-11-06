"""Dense Cardiomyopathies revision pearls; short factual bullets and selective comparisons."""
import json
from pathlib import Path
from lxml import html
from create_qbank_topic_notes import DEST,page

BODY=Path(__file__).with_name('cardiomyopathy_dense_body.html').read_text(encoding='utf-8')


def make():
    doc=html.fragment_fromstring(BODY,create_parent='div')
    ids=doc.xpath('.//section/@id');assert len(ids)==len(set(ids))==12
    assert not doc.xpath('.//h1|.//script|.//iframe')
    assert all(link[1:] in ids for link in doc.xpath('.//nav//a/@href'))
    tables=doc.xpath('.//table');assert len(tables)==2
    for table in tables:
        count=len(table.xpath('./thead/tr/th'))
        assert all(len(row.xpath('./td'))==count for row in table.xpath('./tbody/tr'))
    coverage=['hcm','hcm','hcm','hcm','hcm','hcm','hcm','assessment','dcm','dcm','dcm','arrhythmogenic',
        'arrhythmogenic','restriction','restriction','amyloid','amyloid','amyloid','storage','storage',
        'myocarditis','myocarditis','sarcoid','sarcoid','takotsubo','takotsubo','storage','storage','cmr','family',
        'dcm','arrhythmogenic','family','family','myocarditis','family','assessment']
    assert len(coverage)==37 and all(key in ids for key in coverage)
    target=DEST/'Cardiology/Cardiomyopathies.html';target.parent.mkdir(parents=True,exist_ok=True)
    rendered=page('Cardiomyopathies',BODY).replace('<h1>Cardiomyopathies</h1>','',1)
    rendered=rendered.replace('</style>','table{display:table;width:100%}@media(max-width:650px){table{display:block;overflow-x:auto}}</style>')
    target.write_text(rendered,encoding='utf-8')
    sources=[
      'https://academic.oup.com/eurheartj/article/44/37/3503/7246608',
      'https://www.jacc.org/doi/10.1016/j.jacc.2024.02.014',
      'https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=669c936b-3ee6-4e36-8a22-79dd11b1255b',
      'https://www.jacc.org/doi/10.1016/j.jacc.2022.11.022',
      'https://academic.oup.com/eurheartj/article/46/40/3952/8234483',
      'https://academic.oup.com/eurheartj/article/46/43/4462/8234487',
      'https://www.acc.org/Latest-in-Cardiology/ten-points-to-remember/2024/04/22/13/10/diagnosis-and-management-of-cs',
      'https://www.acc.org/latest-in-cardiology/ten-points-to-remember/2020/03/30/12/17/takotsubo-syndrome',
    ]
    target.with_suffix('.review.json').write_text(json.dumps(dict(module='Cardiomyopathies',status='authored',
      sourceCheckedAt='2026-11-07',independentClinicianReview=False,visibleReferences=False,visibleTitle=False,
      writingStyle='Dense revision pearls; short factual bullets; essential comparisons only',
      groups=12,tables=2,questionCoverage={str(i):key for i,key in enumerate(coverage,1)},checkedSources=sources),indent=2),encoding='utf-8')
    manifest=DEST/'authored-notes.json';authored=json.loads(manifest.read_text(encoding='utf-8')) if manifest.exists() else {}
    authored['Cardiology/Cardiomyopathies']=dict(file=str(target),sections=12,tables=2,references=0,
      words=len(doc.text_content().split()),status='authored_source_checked',chapterOrder=6,writingStyle='dense-pearls')
    manifest.write_text(json.dumps(authored,indent=2),encoding='utf-8')
    print(target);print(f'12 sections; 2 comparison tables; {len(doc.text_content().split())} words; 37 concepts mapped')


if __name__=='__main__':make()
