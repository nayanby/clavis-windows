"""Build Chapter 13 locally; only the sealed-release installer writes runtime data."""
import hashlib,json
from pathlib import Path
from qbank_json_chapters import ROOT,DATA,save,validate,highlight_medical_values
from cardiology_13_aortic import rows,REFERENCES

DOC='13. Aortic Diseases and Peripheral Vascular Diseases'
PREFIX='cardiology-rebuild-13-'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def write(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

if __name__=='__main__':
 source=ROOT/'Cardiology'/(DOC+'.json');existing=read(source)
 assert existing['status']!='installed_verified','Do not overwrite a released chapter with draft authoring'
 originals=[q for q in existing['questions'] if not q['id'].startswith(PREFIX)]
 assert len(originals)==3
 pad=Path(__file__).with_name('cardiology_13_pad.py')
 if pad.exists():
  from cardiology_13_pad import rows as pad_rows,REFERENCES as pad_refs
  rows.extend(pad_rows);REFERENCES.update(pad_refs)
 for r in rows:
  r['sections']=[(h,[(highlight_medical_values(t),[highlight_medical_values(c) for c in children]) for t,children in bullets]) for h,bullets in r['sections']]
  if r['title'] in {'BEST-CLI and Suitable Vein Conduit','BASIL-2 and Infrapopliteal Revascularization'}:r['style']='direct'
 fixed={q['id']:q['correctIndex'] for q in existing['questions'] if q['id'].startswith(PREFIX)}
 save('Cardiology',13,DOC,rows,REFERENCES,'Local authoring draft; final clinical, source-coverage and rendering review pending. Full Harrison text not accessed.',preserved_answer_indices=fixed,additional_preserved_questions=originals)
 bank=read(source)
 order={q['id']:i*10 for i,q in enumerate(bank['questions'],1) if q['id'].startswith(PREFIX)}
 order.update({'cardiology-rebuild-02-008':35,'cardiology-rebuild-09-042':65,'cardiology-rebuild-03-017':155})
 bank['questions'].sort(key=lambda q:order[q['id']])
 for q in bank['questions']:
  if q['id'].startswith(PREFIX):q['reviewStatus']='draft_pending_final_source_review';q['sourceCheckedAt']='2026-11-16'
 bank.update(status='draft_in_progress',plannedQuestions=48,sourceDocument=DOC+'.docx',redistribution=existing['redistribution'])
 bank['redistribution'].update(newQuestionsAfterRedistribution=len(rows),draftQuestions=len(rows))
 write(source,bank)
 audit=source.parent/'audit'
 write(audit/'chapter-13-coverage.json',dict(status='draft_in_progress',plannedQuestions=48,authoredQuestions=len(bank['questions']),installedQuestions=3,
  countPolicy='45 new distinct decisions plus 3 transferred questions; provisional until consolidated source-coverage and duplication review, not official examination weightage.',
  sections=[dict(section='Acute aortic syndromes',newQuestions=10,transferredQuestions=2),dict(section='Aortic aneurysms',newQuestions=12,transferredQuestions=1),dict(section='Chronic peripheral arterial disease',plannedNewQuestions=16),dict(section='Acute limb ischemia',plannedNewQuestions=7)],
  authoredDecisions=[dict(questionId=PREFIX+f'{i:03}',title=r['title']) for i,r in enumerate(rows,1)],
  remainingDecisions=['ABI calculation','Exercise ABI','Noncompressible ABI and TBI','CLTI perfusion assessment','Anatomical localization','Vascular versus neurogenic claudication','Lipid lowering','Single antiplatelet therapy','Dual-pathway inhibition','Postprocedural DAPT','Cilostazol','Structured exercise','Claudication revascularization','WIfI','BEST-CLI','BASIL-2','ALI viability classification','Initial anticoagulation','Immediately threatened limb','Irreversible ischemia','Reperfusion compartment syndrome','Catheter thrombolysis selection','Embolic versus thrombotic occlusion']))
 write(audit/'chapter-13-source-review.json',dict(status='in_progress',sourceDocumentSha256=hashlib.sha256((DATA/'files/Cardiology'/(DOC+'.docx')).read_bytes()).hexdigest(),
  sourceSectionsRead=['I. Aortic dissection','II. Aortic aneurysm','III. Peripheral arterial disease','IV. Acute limb ischemia'],
  corrections=['2022 ACC/AHA AAS heart-rate target is 60–80/min, not an unqualified ≤60/min.','Cilostazol dose reduction includes strong OR moderate CYP3A4 inhibitors and CYP2C19 inhibitors; label verification available.','Exercise ABI fall thresholds vary by protocol and should not be presented as universally definitive.'],
  references=[dict(label=x[0],url=x[1]) for x in REFERENCES.values()],
  checks=dict(aorticQuestionStructure='22 new questions authored with four options and individual distractor rationales',finalClinicalReview='pending',transferredExplanationCompaction='pending',rendering='pending'),
  nextWork='Finish PAD and ALI authoring in one content pass; then perform the consolidated full-chapter review and installation checks.'))
 plan=read(ROOT/'progress.json');entry=next(x for x in plan['chapters'] if x['subject']=='Cardiology' and x['document']==DOC)
 entry.update(status='draft_in_progress',authoredQuestions=len(bank['questions']),plannedQuestions=48,installedQuestions=3,draftQuestions=len(rows),draftQuestionsWithheld=len(rows),coverageMap='Cardiology/audit/chapter-13-coverage.json',coverageStatus='incomplete_draft')
 total=sum(len(read(p)['questions']) for p in source.parent.glob('*.json'));manifest=read(audit/'installation-report.json');remaining=total-manifest['installedQuestions']
 manifest['draftQuestionsWithheld']=remaining;write(audit/'installation-report.json',manifest)
 plan['currentChapter']='Cardiology '+DOC;plan['cardiologyRedistribution'].update(currentAuthoredQuestions=total,currentDraftQuestionsNotInstalled=remaining);write(ROOT/'progress.json',plan)
 summary=read(ROOT/'validation-summary.json');summary.update(currentCardiologyAuthoredQuestions=total,currentCardiologyDraftQuestionsNotInstalled=remaining,nextChapter='Cardiology '+DOC);write(ROOT/'validation-summary.json',summary)
 print(json.dumps(validate(bank),indent=2))
