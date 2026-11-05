"""Read-only end-to-end audit of the complete authored project and installed app data."""
import copy,hashlib,json,sys
from collections import Counter
from pathlib import Path
from qbank_authoring import ROOT,validate,render
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from cnl_desktop import study_packs

def canonical(question):
    item=copy.deepcopy(question);answer=item['options'][item['correctIndex']]
    reasons={item['options'][a['optionIndex']]:a['explanation'] for a in item['explanationTeaching']['otherOptions']}
    item['options']=sorted(item['options']);item['correctIndex']=item['options'].index(answer)
    item['explanationTeaching']['otherOptions']=[dict(optionIndex=i,explanation=reasons[o]) for i,o in enumerate(item['options']) if o!=answer]
    render(item);return item

def audit(data=Path('C:/Users/ANT-PC/OneDrive/Cortex Windows/data')):
    plan=json.loads((ROOT/'topic-map.json').read_text(encoding='utf-8'))
    assert len(plan['subjects'])==14
    expected={};subjectcounts=Counter();sourcebanks=[]
    for subject in plan['subjects']:
        name=subject['subject'];assert subject['status']=='installed',name
        for chapter in subject['chapters']:
            assert chapter['status']=='chapter_authored' and chapter['installed'],(name,chapter)
            p=ROOT/chapter['completedFile'];bank=json.loads(p.read_text(encoding='utf-8'));validate(bank);sourcebanks.append(bank)
            assert len(bank['questions'])==chapter['completedQuestionCount']==chapter['targetQuestions'],(name,chapter['chapterOrder'])
            for q in bank['questions']:
                assert q['id'] not in expected,q['id'];expected[q['id']]=q;subjectcounts[name]+=1
        assert subjectcounts[name]==subject['installedQuestions'],name
    assert len(expected)==4456 and len(sourcebanks)==142
    # Chapter splitting rebalances option positions. Verify semantic preservation,
    # then compare exact serialized questions against the final install-ready banks.
    for p in (ROOT/'install-ready').glob('*/*/*/questions.json'):
        bank=json.loads(p.read_text(encoding='utf-8'));validate(bank)
        for q in bank['questions']:
            assert q['id'] in expected and canonical(q)==canonical(expected[q['id']]),q['id']
            expected[q['id']]=q
    root=(data/'Qbank').resolve();physical=[];seen=Counter();hashes={};projectfiles=[];physicalcounts=Counter()
    for p in study_packs._quiz_record_files(data/'study-data'):
        body=p.read_bytes();bank=json.loads(body);physical.append(bank)
        items=bank.get('questions',[])
        if not isinstance(items,list):continue
        mine=[q for q in items if isinstance(q,dict) and q.get('id') in expected]
        if not mine:continue
        assert len(mine)==len(bank['questions']),'Project bank mixed with unrelated questions'
        assert p.resolve().is_relative_to(root) and len(p.relative_to(root).parts)==4,p
        assert study_packs._quiz_number(p.parent.name) is not None,p
        assert study_packs._quiz_number(p.parent.parent.name) is not None,p
        projectfiles.append(str(p));hashes[str(p)]=hashlib.sha256(body).hexdigest()
        for q in mine:
            assert q==expected[q['id']],q['id'];seen[q['id']]+=1;physicalcounts[bank['folder']]+=1
    assert set(seen)==set(expected) and all(n==1 for n in seen.values())
    assert physicalcounts==subjectcounts,(physicalcounts,subjectcounts)
    loaded=study_packs.read_quizzes(data/'study-data');readback=Counter()
    for bank in loaded:
        items=bank.get('questions',[])
        if not isinstance(items,list):continue
        for q in items:
            if not isinstance(q,dict):continue
            if q.get('id') in expected:
                assert q==expected[q['id']],q['id'];readback[q['id']]+=1
    assert readback==seen,'App loader dropped, changed or duplicated project questions'
    assert len(projectfiles)==plan['progress']['activeNewProjectBanksReplaced']==159
    assert plan['progress']['completedQuestions']==plan['progress']['plannedQuestions']==plan['progress']['installedQuestions']==4456
    report=dict(result='PASS',subjects=14,authoredChapters=len(sourcebanks),installedTopicFiles=len(projectfiles),
      authoredAndInstalledQuestions=len(expected),subjectQuestions=dict(subjectcounts),
      answerDistribution={chr(65+i):sum(q['correctIndex']==i for q in expected.values()) for i in range(4)},
      exactQuestionReadback=True,sourceContentPreservedAcrossOptionRebalancing=True,uniqueProjectIds=True,numberedChapterTopicPaths=True,
      explanationStructure='Validated nested bullets, tables, bold emphasis, distractor mappings and reference metadata',
      independentClinicianReview=False,unrelatedActiveBanks=len(physical)-len(projectfiles),
      appExecutable=str(data.parent/'Clinical Notes Library.exe'),qbankRoot=str(root),hashes=hashes)
    assert Path(report['appExecutable']).is_file()
    (ROOT/'complete-project-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='hashes'},indent=2))

if __name__=='__main__':audit()
