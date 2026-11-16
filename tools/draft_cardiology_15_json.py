"""Keep Chapter 15 additions local until the full chapter is reviewed."""
import json,hashlib,collections
import qbank_json_chapters as common
from cardiology_15_antithrombotics import rows,REFERENCES
from cardiology_15_rhythm_angina import rows as rhythm_rows, REFERENCES as rhythm_references
rows.extend(rhythm_rows);REFERENCES.update(rhythm_references)
from cardiology_15_lipids import rows as lipid_rows, REFERENCES as lipid_references
from cardiology_15_vasoactive import rows as vaso_rows, REFERENCES as vaso_references
rows.extend(lipid_rows);REFERENCES.update(lipid_references)
rows.extend(vaso_rows);REFERENCES.update(vaso_references)
from cardiology_15_final_gaps import rows as final_rows, REFERENCES as final_references
rows.extend(final_rows);REFERENCES.update(final_references)
ROOT=common.ROOT
DOC='15. Cardiovascular Pharmacology Antithrombotic Therapy and Landmark Trials'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def write(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
if __name__=='__main__':
 out=common.REPO/'outputs/cardiology-15-authoring'
 template='01. Neuroanatomy, Clinical Localization & Neurological Examination.json'
 (out/'Neurology').mkdir(parents=True,exist_ok=True)
 (out/'Neurology'/template).write_bytes((ROOT/'Neurology'/template).read_bytes())
 common.ROOT=out
 for r in rows:
  r['sections']=[(h,[(common.highlight_medical_values(t),[common.highlight_medical_values(c) for c in children]) for t,children in bullets]) for h,bullets in r['sections']]
 dest=common.save('Cardiology',15,DOC,rows,REFERENCES,'Local additions only; 93 existing canonical questions remain unchanged. Final coverage, independent key checks and integration pending.')
 bank=read(dest);bank['status']='uninstalled_authoring_draft'
 for q in bank['questions']:q.update(reviewStatus='draft_pending_final_review',sourceCheckedAt='2026-11-16')
 write(dest,bank)
 audit=ROOT/'Cardiology/audit';write(audit/'chapter-15-new-question-draft.json',bank)
 original=read(ROOT/'Cardiology'/(DOC+'.json'))
 original['questions']=[q for q in original['questions'] if not q['id'].startswith('cardiology-rebuild-15-')]
 assert len(original['questions'])==93
 source=common.DATA/'files/Cardiology'/(DOC+'.docx')
 report=dict(status='in_progress',sourceDocumentSha256=hashlib.sha256(source.read_bytes()).hexdigest(),existingCanonicalQuestions=93,newDraftQuestions=len(rows),sourceReadStatus='Complete: all 1232 extracted paragraphs read in four contiguous batches.',reviewedSourceRanges=['0–299','300–610','611–925','926–1231'],sourceSectionsPending=[],
  countPolicy='Retain 93 valid transferred decisions and add questions for documented source gaps; final total determined by coverage and overlap review, not an arbitrary equal chapter quota.',
  existingAnswerDistribution=dict(collections.Counter(chr(65+q['correctIndex']) for q in original['questions'])),
  completedNewDecisions=[r['title'] for r in rows],
  remainingCoverage=['Antithrombotic initiation/bridging and selected special populations','Antiarrhythmic toxicity and monitoring gaps','Antianginal selection, tolerance and adverse effects','Lipid drug mechanisms, doses, interactions and outcome distinctions','Vasopressor/inotrope selection, adverse effects and monitoring','Concise manual review of 93 transferred explanations and existing trial claims'],
  sourceFindings=['FDA December 2025 Andexxa communication verified; do not present US availability as unchanged.','Apixaban AF reduction criteria must not be applied to acute VTE.','Tirofiban infusion is halved at CrCl ≤60, with unchanged bolus.','Source labels and country-specific regimens must remain explicit, especially DOACs and newer lipid agents.','2026 lipid guideline found in official JACC; further drug-specific verification remains before those questions are authored.'],
  validation=common.validate(bank),installedChanges=False,nextWork='Complete new pharmacology gap questions and concise review of retained questions, then integrate, render and install.')
 write(audit/'chapter-15-authoring-progress.json',report)
 plan=read(ROOT/'progress.json');plan['currentChapter']='Cardiology '+DOC
 entry=next(e for e in plan['chapters'] if e['subject']=='Cardiology' and e['document']==DOC)
 entry.update(authoringStatus='source_read_new_gap_questions_in_progress',additionalLocalDraftQuestions=len(rows),authoringProgress='Cardiology/audit/chapter-15-authoring-progress.json')
 write(ROOT/'progress.json',plan)
 print(json.dumps(report['validation'],indent=2))
