"""Integrate Chapter 14 locally, preserving 45 transferred IDs and answer slots."""
import hashlib,json
from qbank_json_chapters import ROOT,DATA,save,validate,highlight_medical_values
from cardiology_14_foundations import rows,REFERENCES
from cardiology_14_pacing_syncope import rows as additional,REFERENCES as additional_refs
rows.extend(additional);REFERENCES.update(additional_refs)
DOC='14. Advanced ECG Interpretation and Electrophysiology';PREFIX='cardiology-rebuild-14-'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def write(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def order(q):
 qid=q['id']
 if qid.startswith(PREFIX):
  n=int(qid[-3:])
  if n<=12:return(0,n)
  if n==21:return(2,25)
  if n in [13,14,15,16,20,35]:return(5,{35:0,13:1,14:2,15:3,16:4,20:5}[n])
  if n==22:return(4,50)
  if 17<=n<=19:return(6,n)
  return(7,n)
 if qid=='cardiology-rebuild-01-019':return(1,0)
 origin=int(qid.split('-')[-2]);n=int(qid[-3:])
 return({2:2,5:1,6:3,7:4,8:4,9:2}[origin],n+100 if origin in [8,9] else n)

if __name__=='__main__':
 path=ROOT/'Cardiology'/(DOC+'.json');old=read(path)
 assert old['status']!='installed_verified'
 originals=[q for q in old['questions'] if not q['id'].startswith(PREFIX)]
 assert len(originals)==45 and len(rows)==35
 for r in rows:
  r['sections']=[(h,[(highlight_medical_values(t),[highlight_medical_values(c) for c in children]) for t,children in bullets]) for h,bullets in r['sections']]
  if r['title']=='Pathological Q Waves in the 2026 Universal Definition':r['style']='direct'
 fixed={q['id']:q['correctIndex'] for q in old['questions'] if q['id'].startswith(PREFIX)}
 save('Cardiology',14,DOC,rows,REFERENCES,'Integrated local draft: full source review and concise revision of transferred explanations pending; not installed. Full Harrison text not accessed.',preserved_answer_indices=fixed,additional_preserved_questions=originals)
 bank=read(path);bank['questions'].sort(key=order)
 for q in bank['questions']:
  if q['id'].startswith(PREFIX):q.update(sourceCheckedAt='2026-11-16',reviewStatus='draft_pending_final_source_review')
 bank.update(status='draft_in_progress',plannedQuestions=80,sourceDocument=DOC+'.docx',redistribution=old['redistribution'])
 bank['redistribution'].update(newQuestionsAfterRedistribution=35,draftQuestions=35);write(path,bank)
 audit=path.parent/'audit'
 progress=read(audit/'chapter-14-authoring-progress.json')
 progress.update(newDraftQuestions=35,integratedCanonicalQuestions=80,newDraftIntegrated=True,plannedNewDecisionsRemaining=[],validation=validate(bank),nextWork='Complete remaining source read, concise review of 45 transferred explanations and consolidated final clinical/layout review before release.')
 progress['sourceFindings'].extend(['Classical OH occurs WITHIN three minutes, not only after three minutes.','Source statement that seizure loss of consciousness usually lasts over five minutes is misleading; the new explanation distinguishes typical brief convulsions from postictal impairment.','CSM hypersensitivity is distinguished from symptom-reproducing carotid sinus syndrome.'])
 write(audit/'chapter-14-authoring-progress.json',progress)
 write(audit/'chapter-14-coverage.json',dict(status='draft_in_progress',plannedQuestions=80,authoredQuestions=80,existingQuestions=45,newDraftQuestions=35,countPolicy='45 retained decisions plus 35 uncovered decisions, provisional until complete source/overlap review; not official examination weightage.',groups=['Technical validity, axis, intervals and morphology','AV conduction and pauses','Ischemic and pericardial patterns','Supraventricular mechanisms','Ventricular mechanisms and inherited electrical patterns','Metabolic, toxic and temperature effects','Device ECGs','Syncope and autonomic assessment'],newDecisions=[dict(questionId=PREFIX+f'{i:03}',title=r['title']) for i,r in enumerate(rows,1)]))
 plan=read(ROOT/'progress.json');entry=next(e for e in plan['chapters'] if e['subject']=='Cardiology' and e['document']==DOC)
 entry.update(status='draft_in_progress',authoredQuestions=80,plannedQuestions=80,installedQuestions=45,draftQuestions=35,draftQuestionsWithheld=35,coverageMap='Cardiology/audit/chapter-14-coverage.json',coverageStatus='review_pending')
 total=sum(len(read(p)['questions']) for p in path.parent.glob('*.json'));manifest=read(audit/'installation-report.json');withheld=total-manifest['installedQuestions'];manifest['draftQuestionsWithheld']=withheld;write(audit/'installation-report.json',manifest)
 plan['currentChapter']='Cardiology '+DOC;plan['cardiologyRedistribution'].update(currentAuthoredQuestions=total,currentDraftQuestionsNotInstalled=withheld);write(ROOT/'progress.json',plan)
 summary=read(ROOT/'validation-summary.json');summary.update(currentCardiologyAuthoredQuestions=total,currentCardiologyDraftQuestionsNotInstalled=withheld,nextChapter='Cardiology '+DOC);write(ROOT/'validation-summary.json',summary)
 print(json.dumps(dict(authored=80,installedUnchanged=45,newDrafts=35,validation=validate(bank)),indent=2))
