"""Add four source-gap decisions while preserving all existing questions."""
import copy,json
from qbank_json_chapters import ROOT,question,save,validate
from cardiology_10_compact_diagnosis import B
path=ROOT/'Cardiology/10. Infective Endocarditis.json'
bank=json.loads(path.read_text(encoding='utf-8'))
assert bank['status']!='installed_verified'
refs={
 'adhesion':('Experimental study of S. aureus adhesion to damaged and inflamed valves','https://doi.org/10.1093/eurheartj/ehz175'),
 'duke':('Duke–ISCVID diagnostic criteria, 2023','https://doi.org/10.1093/cid/ciad271'),
 'asper':('IDSA aspergillosis guideline, 2016','https://www.idsociety.org/practice-guideline/aspergillosis/'),
 'esc':('ESC endocarditis guideline, 2023','https://doi.org/10.1093/eurheartj/ehad193')}
new=[]
def Q(topic,title,stem,answer,others,sections,ref,**extras):
 r=question(topic,title,stem,answer,others,sections,ref);r.update(explanationStyle='concise_structured',**extras);new.append(r)
Q('Clinical suspicion and blood-culture strategy','Vegetation Formation and Previously Normal Valves',
 'A patient with a previously normal echocardiogram develops S. aureus bacteremia and destructive mitral IE. Which mechanism best explains why the earlier normal valve study does not exclude this diagnosis?',
 'S. aureus can adhere to activated endothelium and infect valves without known structural disease',[
 ('A pre-existing rheumatic lesion is required but was missed by the earlier study','Valve damage increases susceptibility, but S. aureus can infect previously normal valves; occult rheumatic disease is not required.'),
 ('Circulating immune complexes initiate every vegetation before bacteria attach','Immune complexes help explain some extracardiac injury; they are not the obligatory initiating mechanism of bacterial valve colonization.'),
 ('An infected venous thrombus must cross an intracardiac shunt to seed the mitral valve','A shunt can permit paradoxical embolism, but bloodstream bacteria can seed left-sided valves without a venous thrombus crossing a shunt.')],
 [('Adhesion and Growth',[B('**Endothelial injury exposes matrix and promotes platelet–fibrin deposition.**','Microbial adhesins support attachment; organisms then proliferate within a protective vegetation.'),B('**S. aureus also exploits activated/inflamed endothelium.**','A previously normal anatomical study does not establish resistance to infection.')]),
 ('Clinical Consequences',[B('**Vegetation growth can cause destruction and embolization.**','Perforation or chordal injury causes regurgitation; extension can produce abscess or conduction disease.'),B('**Assess current bacteremia and anatomy.**','Prior normal imaging does not replace present cultures, echocardiography or source assessment.')])],['adhesion'],
 flow=['Endothelial injury or activation','Microbial adhesion','Platelet–fibrin vegetation growth','Destruction, extension or embolization'])
Q('Diagnostic criteria','Peripheral Signs and Their Diagnostic Domains',
 'During evaluation for IE, a patient has tender fingertip nodules and painless erythematous macules on the soles. Which classification of these findings matches Duke–ISCVID 2023?',
 'Osler nodes are immunological phenomena; Janeway lesions are vascular phenomena',[
 ('Osler nodes are vascular phenomena; Janeway lesions are immunological phenomena','This reverses their diagnostic categories; tenderness helps identify Osler nodes, whereas painless palm/sole lesions suggest Janeway lesions.'),
 ('Both findings count separately within the immunological domain','Osler nodes belong to that domain, but Janeway lesions are vascular; multiple findings within one domain are not separate minor criteria.'),
 ('Both findings count separately within the vascular domain','Janeway lesions are vascular, but Osler nodes are immunological; the criteria count domains rather than each individual skin lesion.')],
 [('Recognize the Findings',[B('**Osler nodes:** tender fingertip/toe-pad nodules.','Count as immunological evidence alongside Roth spots, rheumatoid factor or qualifying immune-complex GN.'),B('**Janeway lesions:** painless hemorrhagic/erythematous palm or sole lesions.','Count as vascular evidence, as do qualifying embolic manifestations.')]),
 ('Avoid Overclassification',[B('**Roth spots are pale-centered retinal hemorrhages; splinter hemorrhages are subungual.**','Both have other causes; isolated splinter hemorrhages are not a listed standalone Duke minor criterion.'),B('**Clinical signs support, but do not replace, microbiology and imaging.**','Count each applicable domain once and interpret the whole illness.')])],['duke'],style='clinical_scenario')
Q('Organism-directed antimicrobial therapy','Aspergillus Prosthetic-Valve Endocarditis',
 'A prosthetic-valve patient has recurrent systemic emboli and a large vegetation with repeatedly negative pre-antibiotic blood cultures. Excised embolic tissue shows invasive septate hyphae, and culture identifies Aspergillus fumigatus. Which management is most appropriate?',
 'Begin systemic voriconazole or lipid amphotericin B and arrange early valve-surgery assessment',[
 ('Begin fluconazole and reserve surgery for persistent positive blood cultures','Fluconazole lacks useful Aspergillus activity, and blood cultures are often negative; waiting for persistent positivity delays appropriate source control.'),
 ('Use an uncomplicated invasive-pulmonary-aspergillosis course without valve intervention','Pulmonary treatment-duration rules do not establish adequate therapy for an infected prosthesis with embolization; valve surgery and prolonged treatment require separate assessment.'),
 ('Use valve surgery alone because removal of the vegetation eliminates the fungal focus','Surgery reduces infected tissue but does not treat residual or disseminated infection; systemic antifungal therapy remains necessary.')],
 [('Diagnosis and Initial Care',[B('**Aspergillus IE often has negative blood cultures.**','Tissue histology plus culture/molecular identification is valuable; a biomarker alone cannot localize infection to a valve.'),B('**IDSA recommends early surgery plus voriconazole or lipid amphotericin B.**','Adult IV voriconazole commonly starts at 6 mg/kg every 12 hours for two doses, then 4 mg/kg every 12 hours; individualize exposure and route.')]),
 ('Monitoring and Relapse',[B('**Monitor voriconazole levels, liver tests, QT and interactions.**','Lipid amphotericin requires renal/electrolyte monitoring.'),B('**Consider lifelong antifungal therapy after valve replacement.**','This is individualized guidance supported by limited evidence, reflecting late relapse risk; do not apply a short candidemia course.')])],['asper'])
Q('Complications and prognosis','Risk Assessment After Bloodstream Clearance',
 'Blood cultures clear in a patient with prosthetic-valve IE, but severe regurgitation, periannular extension and worsening renal function remain. Which interpretation is most appropriate?',
 'Microbiological improvement does not remove the high risk from structural and organ complications',[
 ('Culture clearance removes the need for inpatient risk assessment if the patient is afebrile','Clearance is favorable but does not resolve severe valve dysfunction, invasive anatomy or renal injury; these findings still need urgent integrated assessment.'),
 ('The organism alone determines prognosis once repeat cultures are negative','Pathogen matters, but hemodynamics, prosthetic involvement, extension, neurological injury and organ dysfunction independently influence risk and treatment.'),
 ('Declining inflammatory markers can substitute for follow-up imaging of the valve','Markers track inflammation imperfectly and cannot show whether regurgitation or periannular destruction has resolved; anatomical reassessment remains necessary.')],
 [('Integrate Risk Domains',[B('**Assess host, pathogen, anatomy and organ function together.**','HF, prosthetic involvement, invasive infection, persistent bacteremia, renal failure and neurological complications are adverse features.'),B('**Reassess dynamically.**','One improved variable does not negate deterioration in another domain.')]),
 ('Link Risk to Action',[B('**Escalate Endocarditis Team and surgical assessment when indicated.**','Use imaging, perfusion, rhythm, renal trends and microbiology to define the unresolved problem.'),B('**Avoid a universal individual mortality estimate from cohort averages.**','Counsel according to recoverability, complications and treatment options; continue follow-up after discharge.')])],['esc'])
existing=[q for q in bank['questions'] if q['id'].startswith('cardiology-rebuild-10-') and int(q['id'].split('-')[-1])<=65]
assert len(existing)==65
existing.sort(key=lambda q:q['id'])
rows=[]
for q in existing:
 keys=[]
 for ref in q['references']:
  key='ref'+str(len(refs));refs[key]=(ref['label'],ref['url']);keys.append(key)
 rows.append(question(q['topic'],q['explanationTeaching']['title'],q['question'],q['options'][q['correctIndex']],[(q['options'][o['optionIndex']],o['explanation']) for o in q['explanationTeaching']['otherOptions']],[],keys))
rows+=new
transfer=[q for q in bank['questions'] if q['id']=='cardiology-rebuild-05-048']
assert len(transfer)==1
save('Cardiology',10,bank['document'],rows,refs,bank['sourceNote'],preserved_questions=existing,additional_preserved_questions=transfer)
out=json.loads(path.read_text(encoding='utf-8'))
for k in ('sourceDocument','redistribution'):out[k]=copy.deepcopy(bank[k])
out['status']='local_draft_in_progress'
byid={q['id']:q for q in out['questions']}
ordered=[]
for q in bank['questions']:
 if q['id'].startswith('cardiology-rebuild-10-') and int(q['id'].split('-')[-1])>65:continue
 if q['id']=='cardiology-rebuild-10-001':ordered.append(byid['cardiology-rebuild-10-066'])
 ordered.append(byid[q['id']])
 for after,newid in [('006','067'),('034','068'),('061','069')]:
  if q['id']=='cardiology-rebuild-10-'+after:ordered.append(byid['cardiology-rebuild-10-'+newid])
assert len(ordered)==70
out['questions']=ordered
report=validate(out)
path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report))
