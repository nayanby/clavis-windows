"""Integrate additions with stable transferred IDs; never installs a draft."""
import json
import qbank_json_chapters as common
from draft_cardiology_15_json import rows,REFERENCES,DOC
ROOT=common.ROOT
PREFIX='cardiology-rebuild-15-'
GROUPS=[
 ('Antiplatelets and ACS antithrombotics','02-033 02-034 02-035 02-028 02-038 02-039 02-040 02-041 02-066'),
 ('Anticoagulants and reversal','02-036 02-037 03-026 03-050 03-051 03-052 03-053 03-054 03-055 06-037 06-038 06-043 06-064'),
 ('Fibrinolytic regimens','02-020 02-021'),
 ('Antiarrhythmic selection and safety','06-011 06-012 06-020 06-046 06-053 06-054 06-055 06-056 06-057 06-061 07-012 07-013 07-014 07-015 07-024 07-025 07-033 07-037 07-049 07-051 07-056'),
 ('Antianginal therapy and coronary evidence','02-042 02-043 02-056 02-060 02-057 02-062 02-063'),
 ('Heart failure pharmacology and trials','04-010 04-011 04-012 04-013 04-014 04-016 04-017 04-018 04-020 04-021 04-022 04-023 04-024 04-025 04-028 04-029 04-030 04-031 04-046 04-050'),
 ('Cardiomyopathy and pericardial therapies','08-015 08-016 08-037 08-038 09-009 09-010 09-020 09-021 09-022 09-053'),
 ('Lipid pharmacology','02-054'),
 ('Vasoactive and shock therapies','05-028 05-030 05-034 04-058 04-060 04-061 04-062'),
 ('Structural intervention trials','03-010 03-037 03-038')]
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def write(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def sort_key(q):
 if q['id'].startswith(PREFIX):
  n=int(q['id'][-3:]);group=0 if n<=3 else 1 if n<=12 or n in (32,33) else 3 if n<=15 else 4 if n<=18 else 7 if n<=26 else 8
  return(group,100+n)
 return ORIGINAL_ORDER[q['id']]
ORIGINAL_ORDER={'cardiology-rebuild-'+qid:(g,i) for g,(_,ids) in enumerate(GROUPS) for i,qid in enumerate(ids.split())}
if __name__=='__main__':
 path=ROOT/'Cardiology'/(DOC+'.json');old=read(path)
 assert old['status']!='installed_verified'
 originals=[q for q in old['questions'] if not q['id'].startswith(PREFIX)]
 assert len(originals)==93 and set(ORIGINAL_ORDER)=={q['id'] for q in originals}
 for r in rows:
  r['sections']=[(h,[(common.highlight_medical_values(t),[common.highlight_medical_values(c) for c in children]) for t,children in bs]) for h,bs in r['sections']]
 fixed={q['id']:q['correctIndex'] for q in old['questions'] if q['id'].startswith(PREFIX)}
 common.save('Cardiology',15,DOC,rows,REFERENCES,'Integrated local draft; final release review pending.',additional_preserved_questions=originals,preserved_answer_indices=fixed)
 bank=read(path);bank['questions'].sort(key=sort_key)
 for q in bank['questions']:
  if q['id'].startswith(PREFIX):q.update(sourceCheckedAt='2026-11-16',reviewStatus='draft_pending_final_review')
 bank.update(status='draft_in_progress',sourceDocument=DOC+'.docx',redistribution=old['redistribution'])
 bank['redistribution'].update(newQuestionsAfterRedistribution=len(rows),draftQuestions=len(rows))
 write(path,bank)
 audit=path.parent/'audit';progress=read(audit/'chapter-15-authoring-progress.json')
 progress.update(integratedCanonicalQuestions=len(bank['questions']),newDraftIntegrated=True,validation=common.validate(bank),nextWork='Finish coverage-gap review and concise revision of 93 transferred explanations before final rendering and release.')
 write(audit/'chapter-15-authoring-progress.json',progress)
 write(audit/'chapter-15-coverage.json',dict(status='draft_in_progress',authoredQuestions=len(bank['questions']),existingQuestions=93,newDraftQuestions=len(rows),groups=[name for name,_ in GROUPS],countPolicy=progress['countPolicy'],newDecisions=[dict(questionId=PREFIX+f'{i:03}',title=r['title']) for i,r in enumerate(rows,1)],remainingCoverage=progress['remainingCoverage']))
 plan=read(ROOT/'progress.json');entry=next(e for e in plan['chapters'] if e['subject']=='Cardiology' and e['document']==DOC)
 entry.update(status='draft_in_progress',authoredQuestions=len(bank['questions']),installedQuestions=93,draftQuestions=len(rows),draftQuestionsWithheld=len(rows),coverageMap='Cardiology/audit/chapter-15-coverage.json',coverageStatus='review_pending')
 total=sum(len(read(p)['questions']) for p in path.parent.glob('*.json'));manifest=read(audit/'installation-report.json');withheld=total-manifest['installedQuestions']
 manifest['draftQuestionsWithheld']=withheld;write(audit/'installation-report.json',manifest)
 plan['cardiologyRedistribution'].update(currentAuthoredQuestions=total,currentDraftQuestionsNotInstalled=withheld);write(ROOT/'progress.json',plan)
 summary=read(ROOT/'validation-summary.json');summary.update(currentCardiologyAuthoredQuestions=total,currentCardiologyDraftQuestionsNotInstalled=withheld,nextChapter='Cardiology '+DOC);write(ROOT/'validation-summary.json',summary)
 print(json.dumps(progress['validation'],indent=2))
