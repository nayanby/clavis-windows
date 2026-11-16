"""Serialize new Chapter 14 questions locally until the full balanced set is ready."""
import json,hashlib
from pathlib import Path
import qbank_json_chapters as common
from cardiology_14_foundations import rows,REFERENCES
ROOT=common.ROOT
DOC='14. Advanced ECG Interpretation and Electrophysiology'
def write(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
if __name__=='__main__':
 out=common.REPO/'outputs/cardiology-14-authoring'
 template='01. Neuroanatomy, Clinical Localization & Neurological Examination.json'
 (out/'Neurology').mkdir(parents=True,exist_ok=True)
 (out/'Neurology'/template).write_bytes((ROOT/'Neurology'/template).read_bytes())
 common.ROOT=out
 for r in rows:
  r['sections']=[(h,[(common.highlight_medical_values(t),[common.highlight_medical_values(c) for c in children]) for t,children in bullets]) for h,bullets in r['sections']]
  if r['title']=='Pathological Q Waves in the 2026 Universal Definition':r['style']='direct'
 dest=common.save('Cardiology',14,DOC,rows,REFERENCES,'Local new-question draft only; existing 45 questions remain in the canonical bank. Final integration and review pending.')
 b=json.loads(dest.read_text(encoding='utf-8'));b['status']='uninstalled_authoring_draft'
 for q in b['questions']:q['reviewStatus']='draft_pending_final_source_review';q['sourceCheckedAt']='2026-11-16'
 audit=ROOT/'Cardiology/audit'
 write(audit/'chapter-14-new-question-draft.json',b)
 original=json.loads((ROOT/'Cardiology'/(DOC+'.json')).read_text(encoding='utf-8'))
 assert len(original['questions'])==45
 source=common.DATA/'files/Cardiology'/(DOC+'.docx')
 report=dict(status='in_progress',sourceDocumentSha256=hashlib.sha256(source.read_bytes()).hexdigest(),existingCanonicalQuestions=45,newDraftQuestions=len(rows),provisionalPlannedTotal=80,
  countPolicy='Retain 45 source-matched IDs and add approximately 35 uncovered high-yield decisions; revise after full source and duplicate review, not official examination weightage.',
  sourceReadStatus='Partial full-text review; initial whole-document output was truncated and is not counted as a full read.',
  reviewedSourceRanges=['ECG foundations and opening rhythm sections from initial output','Axis/conduction and chamber/QRS sections, paragraphs 350–584','Electrolytes/drugs/channelopathies and opening other-disease sections, paragraphs 939–1108'],
  sourceSectionsPending=['Remaining rate/rhythm text','Ischemia/infarction','Arrhythmias/emergency rhythms','Remaining pacing/mimics and integrated reporting','Approach to tachyarrhythmia','Syncope full section'],
  sourceFindings=['2026 Fifth Universal Definition and its classical Q-wave criteria independently confirmed in official JACC/AHA/ESC sources.','Preserved original answer positions are uneven (A8 B5 C12 D20); final 80-question integration permits A20 B20 C20 D20 without changing original keys.'],
  plannedNewDecisionsRemaining=['Therapeutic digoxin effect','Pacing failure to capture','Oversensing','Pacemaker-mediated tachycardia','Hypothermic J waves','Wellens pattern','Exercise-provoked CPVT interpretation','Convulsive syncope versus seizure','Classical orthostatic hypotension','POTS','Implantable loop recorder selection','Tilt-test interpretation','Carotid sinus syndrome','Reflex counterpressure maneuvers','Midodrine','Fludrocortisone safety','Pacing selected reflex syncope','Exertional versus postexercise syncope','Psychogenic pseudosyncope','Hyperkalemia despite a normal ECG'],
  validation=common.validate(b),nextWork='Read remaining source sections, author the remaining decisions, integrate all 80 questions, compact/review transferred explanations, then render and install.')
 write(audit/'chapter-14-authoring-progress.json',report)
 print(json.dumps(dict(newDraftQuestions=len(rows),existingCanonicalQuestions=45,installedChanges=False),indent=2))
