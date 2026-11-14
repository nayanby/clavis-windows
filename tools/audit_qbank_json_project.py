"""Read-only runtime comparison plus a portable, honest project progress summary."""
import collections,hashlib,json,sys
from qbank_json_chapters import REPO,ROOT,DATA,validate
sys.path.insert(0,str(REPO/'src'))
from cnl_desktop import study_packs

def main():
    path=ROOT/'progress.json';plan=json.loads(path.read_text(encoding='utf-8'))
    old=study_packs.paths.resource_root
    try:
        study_packs.paths.resource_root=lambda:DATA.parent/'_internal/assets'
        active=study_packs.read_quizzes(DATA/'study-data')
    finally:study_packs.paths.resource_root=old
    actual={study_packs._quiz_row_id(b):b for b in active}
    assert len(actual)==len(active),'Duplicate runtime identity'
    complete=[];expected=set()
    for row in plan['chapters']:
        if row['status']=='pending':continue
        source=ROOT/row['file'];bank=json.loads(source.read_text(encoding='utf-8'))
        validate(bank);identity=study_packs._quiz_row_id(bank);expected.add(identity)
        assert identity in actual,(row['document'],'Missing installed bank')
        loaded=actual[identity]
        assert loaded['questions']==bank['questions'],(row['document'],'Runtime questions differ')
        assert loaded['chapterOrder']==bank['chapterOrder'],(row['document'],'Chapter order differs')
        coverage=source.with_name(source.stem+'.coverage.json')
        if coverage.exists():
            c=json.loads(coverage.read_text(encoding='utf-8'))
            assert len(c['questionDecisions'])==len(bank['questions'])
            assert len({q['coverageDecision'] for q in bank['questions']})==len(bank['questions'])
            assert [q['coverageDecision'] for q in bank['questions']]==[x['decision'] for x in c['questionDecisions']]
            assert [q['explanationTeaching']['title'] for q in bank['questions']]==[x['title'] for x in c['questionDecisions']]
            c['status']='installed_verified';coverage.write_text(json.dumps(c,ensure_ascii=False,indent=2),encoding='utf-8')
            row['coverageMap']=coverage.relative_to(ROOT).as_posix();row['coverageReview']='mapped_and_cross_checked'
        else:row['coverageReview']='retrospective_audit_required'
        row['status']='installed_verified';row['installedSha256']=hashlib.sha256(source.read_bytes()).hexdigest()
        complete.append(row)
    assert set(actual)==expected,'Unexpected active bank outside the new project'
    report=dict(projectStatus='in_progress',plannedChapters=len(plan['chapters']),installedChapters=len(complete),
      installedQuestions=sum(len(b['questions']) for b in active),
      structurallyValidated=True,runtimeSourceComparison='passed',
      mappedChapters=sum(x['coverageReview']=='mapped_and_cross_checked' for x in complete),
      retrospectiveCoverageAudit=[x['subject']+' / '+x['document'] for x in complete if x['coverageReview']=='retrospective_audit_required'],
      independentClinicianReview='not_recorded',
      nextChapter=plan['currentChapter'],
      countPolicy=plan['questionCountPolicy'])
    path.write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
    (ROOT/'validation-summary.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
