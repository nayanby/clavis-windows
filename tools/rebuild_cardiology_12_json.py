"""Additive, source-matched ACHD authoring; incomplete additions stay uninstalled."""
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET

from qbank_json_chapters import ROOT, DATA, save, validate, highlight_medical_values
from cardiology_12_asd_questions import rows, REFERENCES
from cardiology_12_asd_advanced import rows as advanced_asd_rows, REFERENCES as advanced_asd_references
rows.extend(advanced_asd_rows)
REFERENCES.update(advanced_asd_references)
from cardiology_12_vsd_pda_questions import rows as vsd_pda_rows, REFERENCES as vsd_pda_references
rows.extend(vsd_pda_rows)
REFERENCES.update(vsd_pda_references)
from cardiology_12_obstruction_questions import rows as obstruction_rows, REFERENCES as obstruction_references
rows.extend(obstruction_rows)
REFERENCES.update(obstruction_references)
from cardiology_12_tof_questions import rows as tof_rows, REFERENCES as tof_references
rows.extend(tof_rows)
REFERENCES.update(tof_references)
from cardiology_12_eisenmenger_questions import rows as eisenmenger_rows, REFERENCES as eisenmenger_references
rows.extend(eisenmenger_rows)
REFERENCES.update(eisenmenger_references)
from cardiology_12_ebstein_tga_questions import rows as ebstein_tga_rows, REFERENCES as ebstein_tga_references
rows.extend(ebstein_tga_rows)
REFERENCES.update(ebstein_tga_references)

DOC='12. Adult Congenital Heart Diseases'
PREFIX='cardiology-rebuild-12-'
SECTIONS=[
 ('Foundations and physiological classification',[
  'Classify anatomical complexity separately from physiological stage',
  'Calculate Qp/Qs from an appropriately sampled oximetry run',
  'Distinguish pressure loading from shunt-related chamber volume loading',
  'Choose expert surveillance using physiological sequelae after repair']),
 ('Atrial septal defects and atrioventricular septal anatomy',[
  'Explain the pulmonary flow murmur and fixed S2 splitting',
  'Recognize partial AV septal anatomy from axis conduction and AV-valve findings',
  'Interpret relative ventricular compliance and atrial shunt magnitude',
  'Map sinus venosus communications and anomalous pulmonary venous connections',
  'Use CMR for reproducible RV volumes and pulmonary-systemic flow assessment',
  'Apply the 2025 uncomplicated ASD closure recommendation with its PVR and LV qualifications',
  'Assess elevated PVR without assuming every large ASD should be closed',
  'Assess left-heart filling tolerance before an appropriate selected closure strategy']),
 ('Ventricular septal defects',[
  'Distinguish restrictive from nonrestrictive VSD physiology',
  'Recognize aortic cusp prolapse and regurgitation associated with a VSD',
  'Select closure according to LV loading shunt magnitude and pulmonary vascular status',
  'Distinguish uncertain VSD treat-and-repair benefit from the ASD recommendation',
  'Recognize residual shunt and conduction complications after repair']),
 ('Patent ductus arteriosus',[
  'Interpret the continuous murmur and systemic-to-pulmonary runoff',
  'Recognize differential cyanosis and its ductal physiology',
  'Select adult PDA closure according to left-heart load and pulmonary resistance']),
 ('Coarctation after diagnosis and repair',[
  'Select arch imaging for residual obstruction aneurysm and collateral anatomy',
  'Interpret gradients with collateral flow and reduced cardiac output',
  'Choose an appropriate intervention for an anatomically suitable adult lesion',
  'Interpret postrepair Doppler gradients and monitor persistent or exercise-related hypertension']),
 ('Congenital valve and outflow obstruction',[
  'Choose balloon treatment for a suitable symptomatic doming pulmonary valve',
  'Differentiate valvar subvalvar and supravalvar RV outflow obstruction',
  'Assess congenital aortic valve disease with associated aortopathy and family risk']),
 ('Tetralogy of Fallot and repaired RV outflow physiology',[
  'Interpret unrepaired TOF physiology and determinants of cyanosis',
  'Apply current pulmonary-valve replacement assessment in repaired TOF',
  'Identify arrhythmia substrates and appropriate sudden-death risk assessment',
  'Evaluate anatomy and coronary safety before transcatheter pulmonary valve treatment',
  'Investigate declining exercise capacity with residual obstruction or regurgitation']),
 ('Eisenmenger syndrome and cyanotic physiology',[
  'Recognize irreversible pulmonary vascular disease and unsafe defect closure',
  'Distinguish adaptive erythrocytosis from an indication for phlebotomy',
  'Assess iron deficiency and hyperviscosity symptoms in cyanotic disease',
  'Select and monitor appropriate PAH-directed treatment using the relevant evidence',
  'Assess hemoptysis thrombosis and anticoagulation without routine blanket treatment']),
 ('Ebstein anomaly',[
  'Interpret indexed tricuspid displacement and atrialized RV anatomy',
  'Recognize the relevance of accessory pathways and arrhythmia assessment']),
 ('Transposition and systemic right ventricle',[
  'Investigate systemic RV and baffle complications after an atrial switch',
  'Investigate coronary and great-artery complications after an arterial switch',
  'Recognize AV block and systemic AV-valve disease in congenitally corrected TGA']),
 ('Fontan and single-ventricle circulation',[
  'Explain passive pulmonary flow and sensitivity to pulmonary resistance',
  'Investigate failing Fontan and protein-losing enteropathy',
  'Individualize thromboprophylaxis and evaluation of thromboembolism',
  'Apply current liver surveillance and interpret congestive liver findings',
  'Assess exercise limitation arrhythmia and procedural hemodynamic risk']),
 ('Other important congenital lesions',[
  'Distinguish isolated anomalous pulmonary venous drainage from an ASD',
  'Recognize cor triatriatum and differentiate it from mitral inflow disease',
  'Assess anomalous aortic coronary origin and an ischemia-risk phenotype']),
 ('General adult congenital management',[
  'Plan pregnancy and contraception using lesion-specific physiological risk',
  'Select endocarditis prophylaxis according to the actual high-risk indication',
  'Individualize activity and objective exercise assessment',
  'Use specialist multidisciplinary planning for noncardiac procedures',
  'Plan lifelong follow-up after repair without relying only on anatomical labels']),
]

ASSIGNMENTS={
 'cardiology-rebuild-01-015':(0,1),
 PREFIX+'001':(1,0), PREFIX+'002':(1,1), PREFIX+'003':(1,2),
 'cardiology-rebuild-01-048':(1,4), PREFIX+'004':(1,5),
 PREFIX+'005':(1,3), PREFIX+'006':(1,6), PREFIX+'007':(1,7),
 PREFIX+'008':(2,0), PREFIX+'009':(2,1), PREFIX+'010':(2,2), PREFIX+'011':(2,3), PREFIX+'012':(2,4),
 PREFIX+'013':(3,0), PREFIX+'014':(3,1), PREFIX+'015':(3,2),
 PREFIX+'016':(4,0), PREFIX+'017':(4,1), PREFIX+'018':(4,2), PREFIX+'019':(4,3),
 PREFIX+'020':(5,1), PREFIX+'021':(5,2),
 PREFIX+'022':(6,0), PREFIX+'023':(6,2), PREFIX+'024':(6,3), PREFIX+'025':(6,4),
 PREFIX+'026':(7,0), PREFIX+'027':(7,1), PREFIX+'028':(7,2), PREFIX+'029':(7,3), PREFIX+'030':(7,4),
 PREFIX+'031':(8,0), PREFIX+'032':(8,1), PREFIX+'033':(9,0), PREFIX+'034':(9,1), PREFIX+'035':(9,2),
 'cardiology-rebuild-03-047':(5,0), 'cardiology-rebuild-03-048':(6,1),
}


def write(p,value):p.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')


if __name__=='__main__':
    source=ROOT/'Cardiology'/(DOC+'.json')
    existing=json.loads(source.read_text(encoding='utf-8'))
    originals=[q for q in existing['questions'] if not q['id'].startswith(PREFIX)]
    assert {q['id'] for q in originals}=={k for k in ASSIGNMENTS if not k.startswith(PREFIX)}
    for i,row in enumerate(rows,1):
        a,b=ASSIGNMENTS[PREFIX+f'{i:03}']
        row['coverageDecision']=SECTIONS[a][1][b]
        row['sections']=[(h,[(highlight_medical_values(t),[highlight_medical_values(x) for x in children]) for t,children in bullets]) for h,bullets in row['sections']]
        if row['table']:
            headers,values=row['table']
            row['table']=(headers,[[highlight_medical_values(x) for x in line] for line in values])
    fixed={q['id']:q['correctIndex'] for q in existing['questions'] if q['id'].startswith(PREFIX)}
    save('Cardiology',12,DOC,rows,REFERENCES,
         'Original educational synthesis with preserved redistributed questions; incomplete additions remain uninstalled. Full Harrison text not accessed; independent clinician review not claimed.',
         preserved_answer_indices=fixed,additional_preserved_questions=originals)
    bank=json.loads(source.read_text(encoding='utf-8'))
    for q in bank['questions']:
        if q['id'].startswith(PREFIX):q['sourceCheckedAt']='2026-11-16'
    bank['questions'].sort(key=lambda q:ASSIGNMENTS[q['id']])
    planned=sum(len(ds) for _,ds in SECTIONS)
    bank.update(status='draft_in_progress',plannedQuestions=planned,sourceDocument=DOC+'.docx')
    bank['redistribution']=existing['redistribution']
    bank['redistribution'].update(newQuestionsAfterRedistribution=len(rows),draftQuestions=len(rows))
    write(source,bank)
    report=validate(bank)
    coverage=dict(subject='Cardiology',chapterNumber=12,chapter=DOC,status='draft_in_progress',
                  plannedQuestions=planned,authoredQuestions=len(bank['questions']),existingQuestionsPreserved=len(originals),newDraftQuestions=len(rows),
                  countPolicy='Provisional 55 distinct high-yield decisions selected from source topics; revise after detailed source, guideline and duplication review. Not official examination weightage.',
                  sections=[dict(section=t,plannedQuestions=len(ds),authoredQuestions=sum(ASSIGNMENTS[q['id']][0]==i for q in bank['questions']),decisions=ds) for i,(t,ds) in enumerate(SECTIONS)],
                  questionDecisions=[dict(questionId=q['id'],section=SECTIONS[ASSIGNMENTS[q['id']][0]][0],decision=SECTIONS[ASSIGNMENTS[q['id']][0]][1][ASSIGNMENTS[q['id']][1]]) for q in bank['questions']])
    audit=source.parent/'audit'
    write(audit/'chapter-12-coverage.json',coverage)
    doc=DATA/'files/Cardiology'/(DOC+'.docx')
    ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    with ZipFile(doc) as z:xml=ET.fromstring(z.read('word/document.xml'))
    headings=[]
    for p in xml.findall('.//w:p',ns):
        style=p.find('w:pPr/w:pStyle',ns)
        if style is not None and ('heading' in style.get('{'+ns['w']+'}val','').lower() or style.get('{'+ns['w']+'}val','').lower()=='boldside1'):
            headings.append(''.join(t.text or '' for t in p.findall('.//w:t',ns)))
    write(audit/'chapter-12-source-review.json',dict(chapter=12,document=DOC,status='draft_in_progress',installedNewQuestions=False,
          authoredQuestions=len(bank['questions']),plannedQuestions=planned,sourceDocumentSha256=hashlib.sha256(doc.read_bytes()).hexdigest(),sourceHeadings=headings,
          initialSourceFindings=['The source ASD PVR categories must not be attributed unqualified to the newer 2025 ACC/AHA framework.','The source statement that every sinus venosus lesion requires surgery needs qualification for selected modern transcatheter approaches.','Detailed current AP stages should be checked against the official 2025 classification, not the simplified source summary.','Balloon occlusion is Class 2b in 2025 and can overestimate the actual postclosure wedge-pressure response; question 003 and the new LV-filling assessment question include this limitation.'],
          reviewedNewQuestionIds=[PREFIX+f'{i:03}' for i in range(1,len(rows)+1)],sources=[dict(label=v[0],url=v[1]) for v in REFERENCES.values()],validation=report,
          subsectionChecks=[
           dict(section='Atrial shunts',questionIds=[PREFIX+f'{i:03}' for i in range(1,8)],status='authored_cases_source_checked',
                findings=['Caval step-up localizes anomalous venous entry; it does not alone prove an ASD.','Selected superior sinus venosus covered-stent repair requires mapping and unobstructed pulmonary venous redirection.','ASD PVR 5–8 falling below 5 with PAH treatment is a qualified specialist pathway, not a reason to promise cessation of PAH therapy.','High resting left-heart filling pressure is distinct from low-PVR eligibility; balloon-test predictive limits are explicit.']),
           dict(section='Ventricular shunts',questionIds=[PREFIX+f'{i:03}' for i in range(8,13)],status='authored_cases_source_checked',
                findings=['Independent calculation: 125 - 4*(4.5**2) = 44 mmHg RV systolic pressure under the stated assumptions.','Progressive VSD-related aortic regurgitation is a separate assessment indication despite a small shunt.','VSD volume-load closure evaluation requires attributable important/progressive LV enlargement as well as the flow assessment.','2025 VSD treat-and-repair usefulness is uncertain in the specified higher-PVR responder group; the ASD recommendation is not transferred.','Perimembranous closure has a proximal AV-conduction-axis risk distinct from an isolated fascicular lesion.']),
           dict(section='Ductal shunts',questionIds=[PREFIX+f'{i:03}' for i in range(13,16)],status='authored_cases_source_checked',
                findings=['Left-to-right ductal flow primarily volume-loads LA/LV; a continuous murmur depends on the pressure gradient.','Right-to-left ductal entry beyond the usual left subclavian artery explains differential cyanosis in usual anatomy.','A suitable isolated adult PDA with attributable left-heart enlargement and low PVR favors transcatheter closure; pulmonary vascular disease and test-occlusion limits are qualified.']),
           dict(section='Coarctation and congenital outflow lesions',questionIds=[PREFIX+f'{i:03}' for i in range(16,22)],status='authored_cases_source_checked',
                findings=['Postrepair cross-sectional surveillance covers aneurysm and arch anatomy even with a low resting gradient; ESC 2024 gives an adapted 3–5-year interval.','A 7/20 isthmus ratio is 0.35; collaterals can lower a catheter gradient despite important anatomy.','ESC stenting preference is qualified by adult anatomy; current US guidance permits surgical or catheter repair by ACHD experts.','Doppler mean and maximum instantaneous gradients are distinguished from invasive peak-to-peak measurements.','A proximal/distal RV pressure step with little distal-RV-to-PA step localizes intracavitary rather than valvar obstruction.','BAV with aortic dilation prompts first-degree-relative TTE; isolated and concomitant aortic operation thresholds are not conflated.'])],
          tetralogyChecks=['Systemic vascular resistance changes can alter unrepaired right-to-left flow despite unchanged RVOTO.','Scar-related macroreentry is distinguished from idiopathic RVOT triggered activity; a historical QRS marker is not a standalone ICD indication.','Native-RVOT transcatheter valve planning uses CT anatomy and coronary assessment, with device-specific compression evaluation.','RV pressure above two-thirds systemic with obstruction is distinguished from PAH and from regurgitant volume-loading criteria.'],
          eisenmengerChecks=['Four PAH-CHD groups are distinguished using causal anatomy, repair status and shunt direction.','An asymptomatic hematocrit above 65% is not sufficient for phlebotomy; persistent symptoms require hydration, iron and alternative-cause assessment.','Iron deficiency is established by depleted stores despite a high hemoglobin; the ferrous fumarate study dose is salt mass and not a universal starting prescription.','BREATHE-5 primary safety and efficacy endpoints are separated from MAESTRO negative primary exercise outcome; bosentan dual ETA/ETB blockade is independently confirmed.','Routine oral anticoagulation is distinguished from a separate indication and individualized bleeding assessment.'],
          ebsteinTranspositionChecks=['Septal hinge displacement is body-surface-area indexed: 18/1.8 = 10 mm/m², exceeding the adult 8 mm/m² criterion.','Manifest pre-excitation in Ebstein anomaly warrants EP assessment even without reported sustained tachycardia; preoperative access issues are explained.','Atrial-switch baffle leak is distinguished from isolated obstruction, systemic valve regurgitation and chronotropic limitation.','Post-arterial-switch ischemic symptoms prompt assessment of reimplanted coronary anatomy; functional tests answer a complementary question.','Double discordance is mapped to the systemic morphological RV and tricuspid valve, with spontaneous AV-block risk.'],
          nextWork='Continue with Fontan physiology; foundations, remaining congenital lesions, general management and final whole-chapter review also remain pending.',
          limitations=['Four transferred questions retained verbatim with their original IDs.','New content has author source checks, not independent clinician review.','The 55-question plan is provisional and does not establish completeness.']))
    pp=ROOT/'progress.json';plan=json.loads(pp.read_text(encoding='utf-8'))
    entry=next(e for e in plan['chapters'] if e['subject']=='Cardiology' and e['document']==DOC)
    entry.update(status='draft_in_progress',authoredQuestions=len(bank['questions']),plannedQuestions=planned,installedQuestions=4,draftQuestions=len(rows),draftQuestionsWithheld=len(rows),newQuestionsAfterRedistribution=len(rows),coverageMap='Cardiology/audit/chapter-12-coverage.json',coverageStatus='incomplete_draft',explanationStructureStatus='four_originals_preserved_new_questions_use_deep_explanations')
    plan['currentChapter']='Cardiology '+DOC
    total=sum(len(json.loads(p.read_text(encoding='utf-8'))['questions']) for p in source.parent.glob('*.json'))
    manifest_path=audit/'installation-report.json'
    manifest=json.loads(manifest_path.read_text(encoding='utf-8'))
    installed=manifest['installedQuestions']
    manifest['draftQuestionsWithheld']=total-installed
    write(manifest_path,manifest)
    plan['cardiologyRedistribution'].update(currentAuthoredQuestions=total,currentDraftQuestionsNotInstalled=total-installed)
    write(pp,plan)
    sp=ROOT/'validation-summary.json';summary=json.loads(sp.read_text(encoding='utf-8'));summary.update(currentCardiologyAuthoredQuestions=total,currentCardiologyDraftQuestionsNotInstalled=total-installed,nextChapter='Cardiology '+DOC);write(sp,summary)
    print(json.dumps(dict(chapter=DOC,planned=planned,authored=len(bank['questions']),installedUnchanged=4,newDrafts=len(rows),validation=report),indent=2))
