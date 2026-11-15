"""Original spinal cord chapter with decision-based coverage."""
import json
from qbank_json_chapters import question as Q, save, ROOT

R={
 'ACR': ('ACR Appropriateness Criteria: Myelopathy, 2026 update', 'https://www.sciencedirect.com/science/article/abs/pii/S1546144026002930'),
 'NICE': ('NICE NG234: spinal metastases and metastatic spinal cord compression, 2023', 'https://www.nice.org.uk/guidance/ng234/chapter/recommendations'),
 'CES': ('WFNS recommendations: cauda equina and conus syndromes, 2024', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC10943478/'),
}
def S(h, main, *children): return(h,[(main,list(children))])
rows=[]
def add(*a,**kw): rows.append(Q(*a,**kw))

add('Assessment and urgent investigation','Exclude Compression Before Labeling Myelitis',
 'An adult develops progressive leg weakness, a thoracic sensory level and urinary difficulty over two days. Which investigation has priority in the initial etiologic assessment?',
 'Urgent spinal MRI to evaluate the cord and exclude a compressive lesion',[
 ('Lumbar puncture before spinal imaging','CSF helps investigate inflammatory and infectious causes, but should not delay exclusion of a surgically treatable compression in a newly evolving cord syndrome.'),
 ('Lower-limb nerve conduction studies as the first definitive test','Electrodiagnostics can assess peripheral mimics, but do not directly evaluate spinal canal compression and are not the priority with a sensory level and sphincter symptoms.'),
 ('Brain MRI alone before assessing the spine','Brain imaging can contribute to a demyelinating evaluation, but cannot adequately exclude the spinal structural emergency suggested by the current examination.')],
 [S('Localize Clinically, Then Identify the Cause','**A sensory level with bilateral weakness and sphincter disturbance** should prompt assessment for a spinal cord process. The syndrome does not by itself distinguish inflammation from compression, ischemia or other pathology.',
    'Document onset, rate of progression, pain, fever, cancer, infection, trauma and anticoagulant exposure. Assess respiratory involvement when the suspected level is high.',
    'The absence of one typical feature does not establish safety; sphincter symptoms or rapidly progressive weakness can be important even before all long-tract signs develop.'),
  S('MRI Before an Inflammatory Label','**Urgent MRI assesses both the cord and its surrounding structures.** Choose coverage and contrast according to the clinical level and suspected etiology, extending investigation when the examination or risk context suggests multilevel disease.',
    'Compression from tumor, infection, hematoma or degenerative disease requires its own urgent pathway. CSF and serologic testing follow an appropriately sequenced evaluation when a noncompressive cause remains likely.',
    'Do not initiate a prolonged myelitis treatment plan solely from bilateral weakness or a cord T2 signal description. Correlate the canal, lesion location and clinical tempo. Provide appropriate monitoring and specialist assessment while the cause is established; diagnostic testing should run alongside protection from falls, unsafe swallowing or other immediate complications.')],['ACR','NICE','CES'])

add('Assessment and urgent investigation','Acute Areflexia Does Not Exclude Cord Injury',
 'After sudden severe back pain, a patient develops bilateral leg paralysis, a clear sensory level and urinary retention. Tendon reflexes are initially absent. Which interpretation is most appropriate?',
 'Acute cord dysfunction remains possible despite the initial areflexia',[
 ('Areflexia localizes the syndrome to a peripheral polyneuropathy','Peripheral disease is a differential, but early severe cord dysfunction can also produce hypotonia and areflexia; the sensory level and sphincter findings demand urgent spinal evaluation.'),
 ('Areflexia establishes a cauda equina lesion rather than a cord lesion','Cauda equina disease can be areflexic, but the finding alone cannot exclude early cord dysfunction; the full distribution and imaging establish the level.'),
 ('Absent reflexes favor muscle disease as the complete explanation','Severe muscle disease can reduce reflex responses, but does not explain a clear sensory level with acute sphincter dysfunction; spinal pathology remains a priority.')],
 [S('Long-Tract Signs Evolve Over Time','**An acute severe spinal lesion can initially be flaccid and areflexic**, with later emergence of hyperreflexia and spasticity. The first reflex examination is not a permanent localization rule.',
    'Record sensory level, sacral function, motor distribution, pain and time course. Sudden onset raises vascular or hemorrhagic possibilities, while trauma or compression must also be considered.',
    'Peripheral and root disorders remain relevant, particularly when the examination lacks a convincing level; reassess rather than using one reflex sign to close the diagnosis.'),
  S('Avoid a Diagnostic Delay','**Urgent spinal imaging is warranted by the whole syndrome.** Do not wait for extensor plantar responses or brisk reflexes before investigating a potentially treatable cord emergency.',
    'Serial examination can clarify the level and evolution. MRI findings must be interpreted with timing; some intrinsic vascular lesions are initially subtle, whereas a compressive lesion requires a prompt etiologic response.',
    'Distinguish the neurologic term spinal shock from neurogenic hemodynamic shock: the former concerns depressed reflex/motor activity, while the latter involves circulatory consequences of sympathetic disruption. Assess blood pressure and perfusion directly; an areflexic examination does not itself establish the cause of hypotension or justify ignoring bleeding and other shock states.')],['ACR','CES'])

R.update({
 'INFIMG':('ACR Appropriateness Criteria: suspected spine infection','https://acsearch.acr.org/docs/3148734/Narrative/'),
 'APPROACH':('Continuum: clinical approach to myelopathy diagnosis, 2024','https://doi.org/10.1212/CON.0000000000001390'),
 'IDSA':('IDSA native vertebral osteomyelitis guideline, 2015','https://www.idsociety.org/practice-guideline/vertebral-osteomyelitis/'),
})

add('Assessment and urgent investigation','MRI When Spinal Infection Is Suspected',
 'A patient with diabetes has fever, worsening thoracic pain and new leg weakness. There is no MRI contraindication. Which imaging study best evaluates suspected epidural infection and its effect on the cord?',
 'Urgent spinal MRI without and with intravenous contrast, with coverage directed by the clinical findings',[
 ('Thoracic radiographs followed by repeat films if initially normal','Radiographs can show established bony changes but are insensitive to early infection and cannot adequately assess epidural tissue or cord compression in this neurologic emergency.'),
 ('Noncontrast CT alone as the definitive canal investigation','CT can clarify bone destruction and assist procedures, but MRI better evaluates epidural collections, cord and soft tissues when feasible.'),
 ('FDG-PET as the initial emergency cord assessment','PET can have selected roles in occult or complex infection, but is not the preferred immediate anatomical study for new neurologic deficits and possible epidural compression.')],
 [S('Image the Canal and the Infectious Extent','**MRI without and with contrast is usually appropriate for suspected spinal infection.** It assesses vertebrae, discs, epidural and paraspinal tissues and neural compression.',
    'Contrast can help characterize enhancement and collections. Noncontrast sequences remain informative; if contrast cannot be given, obtain an appropriate urgent study and radiology advice rather than abandoning imaging.',
    'Extent depends on the level, symptoms and suspicion of noncontiguous disease. Do not impose one limited region when the examination suggests additional pathology.'),
  S('Parallel Emergency Assessment','**Obtain cultures and urgent specialist review** while assessing sepsis and neurologic progression. Blood cultures should be collected before antibiotics when feasible without delaying necessary treatment in an unstable patient.',
    'New or progressive neurologic deficits can require urgent decompression and source control. The complete fever–back-pain–deficit triad is not required before considering infection.',
    'CT is valuable when MRI is unavailable or contraindicated and for bone/procedural questions, but its limitations must be understood. A normal radiograph or absence of extensive vertebral destruction does not exclude dangerous epidural disease. Do not use CSF sampling as the initial substitute for imaging a suspected compressive infectious process.')],['INFIMG','IDSA','ACR'])

add('Assessment and urgent investigation','A Lumbar Finding That Does Not Explain the Examination',
 'An adult has progressive gait stiffness, brisk knee reflexes, extensor plantar responses and a trunk sensory level. Lumbar MRI shows modest L4–L5 degenerative stenosis. Which next step best addresses the discordance?',
 'Reassess localization and obtain appropriate cervical/thoracic cord imaging',[
 ('Assign the lumbar stenosis as the cause and begin a lumbar-only treatment pathway','Degenerative lumbar findings are common and may explain root symptoms, but do not adequately account for a trunk level and bilateral upper-motor-neuron signs.'),
 ('Repeat lumbar imaging alone at a later routine interval','Repeat imaging is useful for evolving local disease or technical limitations, but restricting reassessment to the lumbar region leaves the clinical cord localization unexplained.'),
 ('Use lower-limb electrodiagnostics as the sole test to exclude cord disease','EMG/NCS can identify coexisting roots or peripheral nerve pathology but do not exclude a cervical or thoracic cord lesion suggested by the examination.')],
 [S('An Abnormal Scan Is Not Automatically Causal','**Match imaging to the neurologic syndrome.** Lumbar root compression may cause pain, focal weakness, sensory change and reduced reflexes, but cannot explain every long-tract pattern.',
    'A sensory level can be imperfectly reported and should be rechecked. Nevertheless, persistent upper-motor-neuron signs require consideration of pathology above the lumbosacral roots.',
    'Coexisting degenerative disease can produce mixed signs. Do not force all findings into the first visible abnormality or ignore a second lesion.'),
  S('Extend the Investigation Where the Evidence Points','**Image the relevant cord regions**, choosing broader coverage when localization is uncertain or multilevel disease is plausible. Review prior image quality and the actual report rather than assuming the cord was assessed.',
    'Consider structural compression, intrinsic inflammatory lesions, vascular disease and other causes according to tempo and risk factors. Brain evaluation may also be relevant if findings do not localize solely to the cord.',
    'Urgency follows progression and functional or sphincter compromise, not the apparent mildness of an incidental lumbar report. Explain that further evaluation addresses an unresolved clinical-radiologic mismatch; it does not imply that every degenerative finding is irrelevant or that symptoms are unexplained because one scan was nondiagnostic.')],['ACR','APPROACH'])

add('Assessment and urgent investigation','Tempo Before an Inflammatory Label',
 'A patient develops severe bilateral leg weakness reaching near-maximal severity within one hour. MRI excludes compression but shows an intrinsic cord lesion; CSF protein is mildly elevated with no pleocytosis. Which feature most strongly argues for prioritizing a vascular cause over routine presumed inflammatory myelitis?',
 'The hyperacute onset and rapid time to maximal deficit',[
 ('The isolated mild CSF protein increase','Protein elevation is nonspecific and can occur in several inflammatory and noninflammatory processes; it should not outweigh a strongly vascular clinical tempo.'),
 ('The presence of cord T2 hyperintensity','T2 signal reflects tissue abnormality rather than one mechanism; ischemia, inflammation, compression and other causes can produce it.'),
 ('The presence of urinary dysfunction','Sphincter involvement supports significant cord/conus pathway dysfunction but does not by itself distinguish vascular from inflammatory etiology.')],
 [S('Use Time to Nadir as a Diagnostic Clue','**Minutes-to-hours evolution raises vascular and hemorrhagic causes**, while days-to-weeks progression may fit inflammatory, infectious or other processes and a chronic course suggests another range of causes.',
    'These are probability shifts, not absolute cutoffs. Ask about aortic disease/procedures, severe hypotension, trauma and sudden pain while excluding structural compression.',
    'Reconstruct the onset carefully: a patient who first notices weakness on awakening may not have a reliably known time to nadir.'),
  S('Integrate Imaging and CSF Without Overcalling Either','**An intrinsic cord lesion is not synonymous with myelitis.** Review lesion distribution, diffusion, enhancement, adjacent structures and imaging timing with the clinical context.',
    'CSF cells, protein and immune markers can contribute, but a mild isolated protein increase is not proof of immune inflammation. Early MRI may also be insensitive to ischemia and require reassessment.',
    'Investigate and address perfusion or aortic causes when suspected while providing supportive care and specialist input. Do not delay treatment of a genuinely supported severe inflammatory attack, but avoid a steroid-response trial as the sole diagnostic method for a potentially vascular emergency. Reassessment of discordant data protects against prolonged treatment of a mistaken mechanism.')],['APPROACH','ACR'])

add('Assessment and urgent investigation','Lumbar Puncture After Structural Assessment',
 'MRI has excluded compression in a patient with suspected inflammatory myelopathy. CSF assessment is planned, but the patient took apixaban that morning. Which next step is most appropriate?',
 'Review anticoagulant timing, renal function and procedure safety before deciding when or whether to perform LP',[
 ('Proceed immediately because a normal INR excludes an apixaban effect','Routine INR does not reliably quantify apixaban anticoagulation; a normal result is not sufficient clearance for an invasive spinal procedure.'),
 ('Proceed immediately because an atraumatic needle eliminates bleeding risk','An atraumatic needle can reduce selected procedural complications but does not eliminate spinal bleeding risk from active anticoagulation.'),
 ('Permanently abandon CSF evaluation because any anticoagulant history prohibits LP','Anticoagulant exposure requires an individualized safety plan, not a permanent blanket prohibition; timing, indication, clearance and alternative information influence the decision.')],
 [S('Separate Diagnostic Value From Procedural Readiness','**CSF can help characterize inflammatory, infectious and neoplastic cord disease** once the structural and clinical context is understood. Its expected value must be balanced against procedural risk.',
    'Review platelet/coagulation concerns, relevant medicines, renal function, last dose and local procedural guidance. Standard clotting results do not uniformly exclude clinically relevant direct-oral-anticoagulant activity.',
    'Hold or modify anticoagulation only through an appropriate plan that considers thrombotic risk and the reason for treatment. Do not infer one safe interval for every agent, dose and clearance state.'),
  S('Do Not Let One Pending Test Freeze Urgent Care','**Coordinate neurology, procedural and anticoagulation expertise** when timing is uncertain. The safest diagnostic route may involve delay, an alternative test or a specialist reversal decision in exceptional circumstances.',
    'Collect blood-based tests and review MRI, clinical trajectory and potential infectious causes while arranging the procedure. CSF collection is not a prerequisite for every emergency treatment decision.',
    'Document what question CSF is intended to answer and interpret subsequent results in that context. A mildly raised protein or incidental immune marker is not a stand-alone etiologic diagnosis. Continue serial motor, sensory, sphincter and respiratory assessment while the workup proceeds rather than assuming that the absence of a completed LP makes deterioration unavoidable or unassessable.')],['APPROACH','ACR'])

R['LP']=('ABN periprocedural antithrombotic management for LP: 2026 summary update','https://pn.bmj.com/content/practneurol/early/2026/08/25/pn-2026-005351.full.pdf')
rows[-1]['refs'].append('LP')

R['NICEINIT']=('NICE NG234 visual summary: MSCC initial management','https://www.nice.org.uk/guidance/ng234/resources/metastatic-spinal-cord-compression-initial-assessment-and-management-pdf-13134700768')
R['NICETX']=('NICE NG234 visual summary: MSCC radiotherapy and invasive interventions','https://www.nice.org.uk/guidance/ng234/resources/metastatic-spinal-cord-compression-radiotherapy-and-invasive-interventions-pdf-13134700769')

add('Compressive and structural myelopathy','Recognize Metastatic Cord Compression Early',
 'A patient previously treated for breast cancer develops progressive nocturnal thoracic pain, difficulty walking and new leg weakness. Which pathway is most appropriate?',
 'Immediate MSCC emergency referral with urgent spinal imaging and neurologic/stability assessment',[
 ('A routine musculoskeletal back-pain pathway with reassessment after physiotherapy','Conservative care is appropriate for selected uncomplicated mechanical pain, but cancer history plus new gait/weakness findings requires an urgent compression pathway.'),
 ('Routine outpatient staging before deciding whether the neurologic symptoms need imaging','Staging informs cancer treatment but should not delay assessment of a potentially reversible neurologic emergency.'),
 ('Escalate analgesia and arrange imaging only if urinary retention develops','Analgesia is important, but retention is not a prerequisite for MSCC; waiting for it can permit further irreversible neurologic injury.')],
 [S('Pain Can Precede Major Neurologic Loss','**New or progressive spinal pain in a person with cancer** deserves attention, especially with night pain, movement-related pain, gait change, weakness or sensory symptoms.',
    'Bladder/bowel dysfunction and radicular pain can occur, but do not wait for a complete syndrome. A remote cancer history still matters in the current risk assessment.',
    'Perform and document a focused neurologic examination and assess possible instability. Severe movement-related pain can indicate a mechanical issue that requires protection during transfers.'),
  S('An Emergency Pathway Rather Than Sequential Routine Referral','**Contact the relevant MSCC service immediately** when compression is suspected with neurologic findings. Arrange urgent MRI, appropriate dexamethasone and specialist definitive planning.',
    'Immobilize without delay when symptoms or signs suggest instability, using appropriate clinical advice; avoid unnecessary prolonged immobilization once stability is assessed.',
    'Provide analgesia, pressure care and supportive assessment while investigating. A normal plain radiograph does not exclude epidural disease, and absence of established paraplegia does not reduce the urgency. The purpose of early action is to preserve function and control the structural/oncologic cause rather than merely document advanced loss.')],['NICE','NICEINIT','ACR'])

add('Compressive and structural myelopathy','MRI Timing in Suspected MSCC',
 'A patient with known malignancy has new neurologic signs suspicious for MSCC. Under NICE NG234, which MRI plan is appropriate?',
 'MRI as soon as possible and within 24 hours, including whole-spine sagittal assessment and targeted axial images',[
 ('MRI within one week limited to the painful vertebral level','A one-week pathway can apply to selected suspected spinal metastases without cord-compression features; neurologic signs require the more urgent MSCC pathway and appropriate broader coverage.'),
 ('MRI only after a positive isotope bone scan','Bone imaging can address other oncologic questions but cannot gate the urgent MRI required to assess neural compression.'),
 ('Lumbar MRI alone because leg weakness localizes all relevant pathology to the lumbar region','Leg weakness can result from thoracic or cervical disease, and metastatic lesions can be noncontiguous; a lumbar-only assumption risks missing the cause.')],
 [S('Time and Coverage Both Matter','**NICE NG234 specifies MRI as soon as possible, always within ==24 hours==**, for suspected MSCC with neurologic signs/symptoms. This is an outer time standard, not a reason to delay an available scan.',
    'Whole-spine sagittal T1 and/or STIR sequences assess metastatic involvement. Sagittal T2 sequences help show compression, the cord/cauda and intrinsic signal.',
    'Obtain supplementary axial images through significant abnormalities. A single sagittal sequence or a scan confined to the patient’s perceived pain level can be inadequate.'),
  S('Adapt Safely When MRI Cannot Be Done','**Discuss an urgent alternative imaging pathway** when MRI is contraindicated or cannot be obtained appropriately. CT may supply useful structural information, with specialist advice for further evaluation.',
    'Do not replace emergency neural imaging with routine radiographs or a bone scan. Coordinate transfer when needed without unnecessary movement in a potentially unstable spine.',
    'Continue neurologic monitoring, analgesia and appropriate steroid/stability measures while imaging is arranged. An imaging deadline and the subsequent treatment deadline concern different steps; completing MRI does not end the emergency pathway when compression is demonstrated.')],['NICE','NICEINIT','ACR'],style='direct')

add('Compressive and structural myelopathy','Dexamethasone in Neurologic MSCC',
 'An adult with a known solid tumor develops weakness and sensory findings strongly suggesting MSCC. Definitive treatment is being arranged. Which steroid regimen matches NICE NG234 initial guidance?',
 'Dexamethasone 16 mg orally or equivalent parenteral dose promptly, then 16 mg daily while awaiting surgery or radiotherapy',[
 ('Dexamethasone 4 mg once daily while awaiting routine outpatient reassessment','A lower symptom-control dose may have other palliative uses, but does not match the specified neurologic MSCC regimen or urgency.'),
 ('Prednisolone 5 mg daily until the MRI result is available','Low-dose maintenance prednisolone is used in other conditions, but is not equivalent to the guideline emergency dexamethasone regimen.'),
 ('Hydrocortisone replacement dosing without a dexamethasone-equivalent treatment course','Physiologic replacement addresses adrenal deficiency rather than the anti-edema regimen recommended for neurologic MSCC.')],
 [S('Give the Neurologic Emergency Regimen','**Offer ==16 mg dexamethasone== as soon as possible**, orally or as an equivalent parenteral dose. Continue ==16 mg daily== while awaiting surgery or radiotherapy under the NICE pathway.',
    'Steroids reduce edema-related effects but do not correct instability or replace decompression/radiotherapy. Treatment planning and monitoring must continue in parallel.',
    'Monitor glucose and provide appropriate gastric protection. Review infection, psychiatric and other steroid risks without allowing routine concerns to obscure a genuine neurologic emergency.'),
  S('Distinguish Diagnosis and Taper Questions','**If MSCC is excluded after steroids were started, discontinue the emergency course appropriately.** After surgery or initiation of radiotherapy, taper according to clinical course and the treatment plan.',
    'Suspected lymphoma or myeloma without neurologic signs requires hematology advice before steroids because diagnostic tissue and imaging can be altered. This caveat should not be turned into a blanket rule to withhold urgent care in neurologic compression.',
    'Known hematologic malignancy and other severe symptoms have specific specialist considerations. Document the indication and subsequent reduction plan rather than leaving a high emergency dose unreviewed indefinitely. Continued worsening requires reassessment of compression and definitive treatment, not simply repeated dose escalation.')],['NICE','NICEINIT'])

add('Compressive and structural myelopathy','Definitive MSCC Treatment Requires Stability Assessment',
 'MRI confirms metastatic epidural compression with progressive weakness and severe movement-related pain suggesting instability. The patient can undergo surgery. Which approach is most appropriate?',
 'Urgent multidisciplinary consideration of decompression and stabilization, followed by appropriate oncologic treatment',[
 ('Radiotherapy alone without surgical stability assessment','Radiotherapy is important in selected MSCC and after surgery, but does not mechanically stabilize an unstable spine; this patient’s pain and operability require surgical assessment.'),
 ('A prolonged steroid-only trial before discussing definitive treatment','Steroids are a bridge, not a substitute for treating ongoing compression or instability; progressive deficits should not wait for a prolonged trial.'),
 ('Systemic anticancer therapy alone before assessing the mechanical lesion','Systemic therapy may be important and some tumors are sensitive, but an unstable compressive lesion needs an urgent structural and neurologic treatment decision.')],
 [S('Neurology, Mechanics and Cancer Biology Interact','**Definitive planning considers compression, stability, neurologic trajectory, tumor factors and overall condition.** No single prognostic number should decide care in isolation.',
    'Use validated stability or prognostic tools as adjuncts to clinical and imaging assessment, not as automatic vetoes. Mechanical pain and instability can remain treatment targets even when neurologic recovery is uncertain.',
    'Arrange surgical intervention to halt or reverse decline as soon as appropriate; urgency reflects the speed of progression rather than an arbitrary wait for complete paralysis.'),
  S('Coordinate Surgery, Radiation and Support','**Decompression and stabilization can be considered when suitable**, with postoperative radiotherapy according to the multidisciplinary plan. Histology, previous radiation and systemic therapy options also matter.',
    'When surgery is unsuitable, NICE recommends urgent radiotherapy for appropriate MSCC patients, generally within 24 hours, with specified poor-prognosis or prolonged-complete-deficit exceptions.',
    'External support may be appropriate when instability cannot be treated surgically. Continue analgesia, bladder/bowel and skin care, rehabilitation and shared decisions about goals. A radiotherapy prescription does not replace reassessing severe mechanical pain or ensuring safe mobilization.')],['NICE','NICETX'])

R['ENLS']=('Neurocritical Care Society ENLS: spinal cord compression protocol','https://www.neurocriticalcare.org/Portals/0/ENLS%205.0/ENLS%205.0%20Protocol%20-%20SCC.pdf')

add('Compressive and structural myelopathy','Epidural Abscess Without the Full Triad',
 'A patient receiving hemodialysis has new focal severe thoracic pain and elevated inflammatory markers after recent Staphylococcus aureus bacteremia. Temperature is normal and strength is currently preserved. Which diagnosis must be actively investigated?',
 'Spinal infection with possible epidural abscess',[
 ('Uncomplicated mechanical back pain','Mechanical pain is common, but recent S. aureus bacteremia, dialysis exposure and focal severe pain substantially raise infection probability despite absent fever or deficit.'),
 ('Isolated diabetic distal symmetric polyneuropathy','A distal neuropathy can coexist, but does not explain new focal thoracic pain and inflammatory findings after bacteremia.'),
 ('A typical inflammatory demyelinating myelitis','Immune myelitis can produce cord symptoms, but the bloodstream infection and focal pain make a spinal infectious focus a more immediate concern.')],
 [S('Fever and Paralysis Are Not Prerequisites','**Epidural infection can precede neurologic deficits**, and the classic fever–back-pain–deficit triad has limited sensitivity. A normal temperature does not exclude dangerous disease.',
    'Recent bacteremia, spinal procedures, immunosuppression, diabetes and dialysis are important context. Examine tenderness, gait, strength, sensation and sphincter symptoms and repeat the examination if the course changes.',
    'Inflammatory markers are supportive but nonspecific. Their absence or presence should not be used alone to decide whether a high-risk patient needs imaging.'),
  S('Find the Source Before Neurologic Decline','**Obtain appropriate spinal MRI and microbiologic evaluation.** Blood cultures and review of prior isolates help connect the current syndrome to an organism and possible source.',
    'Assess vertebral/disc, epidural and paraspinal involvement. If new weakness, sphincter dysfunction or sepsis develops, escalate urgently for source control and antimicrobial treatment.',
    'A stable patient may permit a culture-directed diagnostic strategy, but the plan must include close neurologic monitoring and clear escalation. A documented bloodstream pathogen may alter the need for percutaneous biopsy in a concordant vertebral infection; do not repeat invasive sampling reflexively without considering existing microbiology and the treatment question.')],['IDSA','INFIMG','ENLS'])

add('Compressive and structural myelopathy','Epidural Infection With Progressive Weakness',
 'MRI shows a thoracic epidural abscess compressing the cord. Leg weakness is progressing and the patient is septic. Which approach is most appropriate?',
 'Urgent spine-surgical assessment/source control and empiric intravenous antibiotics, with cultures obtained promptly',[
 ('Withhold all antimicrobial therapy until a scheduled percutaneous biopsy is completed','Withholding can improve microbiologic yield in selected stable vertebral infection, but progressive deficits and sepsis require treatment and source-control assessment without that delay.'),
 ('Give corticosteroids as the principal treatment while awaiting interval imaging','Steroids have a defined role in selected malignant compression, but do not substitute for antimicrobials and source control in this septic compressive infection.'),
 ('Use an oral antibiotic trial and reserve surgical review for failure after several weeks','Selected stable infections can be treated medically, but progressive cord compromise and sepsis demand urgent specialist assessment rather than a prolonged outpatient trial.')],
 [S('Neurologic Deterioration Changes the Sequence','**Sepsis and progressive deficits require immediate treatment**, while pursuing microbiologic diagnosis in parallel. Obtain blood cultures promptly when this does not create a clinically significant delay.',
    'Urgent surgical review addresses decompression, drainage, tissue acquisition and any instability. The definitive operation depends on anatomy and patient factors rather than a universal procedure.',
    'IDSA native vertebral osteomyelitis guidance supports immediate antimicrobial therapy in unstable or progressive neurologic presentations; stable biopsy-first recommendations should not be misapplied to this emergency.'),
  S('Cover Likely Pathogens, Then Narrow','**Empiric therapy commonly covers MRSA, streptococci and relevant gram-negative bacilli**, tailored to host, exposures, prior organisms and local susceptibility. Vancomycin plus an appropriate cephalosporin such as cefepime is one cited framework.',
    'Use renal-adjusted dosing and contemporary drug monitoring; dialysis patients need a specific schedule. Narrow therapy when cultures and susceptibilities are available, with infectious-disease input on duration and source control.',
    'Follow neurologic function, hemodynamics, inflammatory trajectory and toxicity. Antibiotics do not mechanically decompress every abscess, while drainage alone does not treat bacteremia or associated osteomyelitis. Investigate the bloodstream source and other metastatic foci when clinically indicated.')],['IDSA','INFIMG','ENLS'])

add('Compressive and structural myelopathy','Acute Spinal Epidural Hematoma',
 'A patient taking an anticoagulant develops sudden severe cervical pain followed by rapidly progressive limb weakness. There is no fever. Which immediate diagnostic-treatment pathway is most appropriate?',
 'Emergency spinal imaging and spine-surgical review, with urgent assessment and reversal of relevant coagulopathy',[
 ('Lumbar puncture first to distinguish hemorrhage from inflammatory myelitis','LP does not adequately evaluate a compressive epidural collection and may add bleeding risk; urgent anatomical assessment is the priority.'),
 ('Empiric intravenous steroids with imaging only if weakness persists','Steroids do not replace diagnosis, anticoagulant management or decompression assessment for a possible rapidly expanding hematoma.'),
 ('Observation for anticoagulant clearance before arranging specialist imaging','Spontaneous improvement can influence selected management after diagnosis, but a rapidly progressive deficit cannot safely wait for unmonitored drug clearance.')],
 [S('Pain Followed by Deficit Is an Alarm Pattern','**Spinal epidural bleeding can rapidly compress the cord or cauda.** Anticoagulants, coagulopathy, procedures and trauma increase suspicion, but spontaneous cases can occur without a recognized risk factor.',
    'Assess motor, sensory, respiratory and sphincter function and hemodynamic status. The lesion level and pace determine immediate support needs.',
    'MRI is preferred for defining the collection, neural compression and associated pathology. If unavailable or contraindicated, obtain urgent specialist-directed alternative imaging rather than delaying assessment.'),
  S('Coordinate Reversal and Decompression Decisions','**Review the anticoagulant, dose, last exposure and renal function** and activate an appropriate reversal pathway for serious bleeding. Agent-specific protocols matter; a normal INR does not exclude all anticoagulant effects.',
    'Progressive neurologic compromise warrants urgent surgical evaluation for evacuation/decompression. Selected patients with minimal or rapidly improving deficits may be managed differently under close specialist observation.',
    'Do not turn a possible conservative option into a reason to delay consultation in worsening paralysis. Reassess serially and arrange rapid access to definitive care. The lack of fever favors neither safety nor a benign musculoskeletal diagnosis when severe pain is followed by objective neurologic loss.')],['ENLS','ACR','LP'])

R.update({
 'DCM':('AO Spine/CSRS degenerative cervical myelopathy management guideline, 2017','https://doi.org/10.1177/2192568217701914'),
 'DCM26':('AO Spine recommendations for mild DCM, 2026','https://doi.org/10.1177/21925682261492222'),
 'SYRINX':('NINDS: syringomyelia','https://www.ninds.nih.gov/health-information/disorders/syringomyelia'),
 'CHIARI':('CNS Chiari guideline: surgical interventions, 2023','https://www.cns.org/Assets/5067fa36-3af0-4909-9fc4-77aba32ff6ab/638297012466600000/cim-guideline-chap-3-final-pdf'),
 'PVR':('Postvoid residual in suspected CES: MRI-confirmed cases with PVR at or below 200 mL, 2022','https://pubmed.ncbi.nlm.nih.gov/35182176/'),
})

add('Compressive and structural myelopathy','Progressive Degenerative Cervical Myelopathy',
 'An adult has worsening hand dexterity and gait imbalance, pyramidal signs and concordant cervical cord compression. The mJOA score is 13. Which management best fits guideline-based care?',
 'Refer for surgical decompression assessment for moderate progressive DCM',[
 ('Use analgesics and routine physiotherapy without a surgical assessment','Nonoperative care can be considered in selected mild disease, but moderate clinical myelopathy with progression warrants surgical evaluation rather than pain treatment alone.'),
 ('Offer prophylactic surgery solely because cervical stenosis is visible','The current indication is symptomatic moderate progressive myelopathy, not an imaging-only prophylactic rule; nonmyelopathic compression requires a different discussion.'),
 ('Treat with corticosteroid immunotherapy before addressing the stenosis','Steroids are used for selected inflammatory causes, but do not correct concordant degenerative mechanical compression or replace its surgical assessment.')],
 [S('Severity Is Clinical, Not Just a Canal Measurement','**DCM combines compatible cord dysfunction with degenerative compression.** Hand clumsiness, gait impairment and long-tract signs should be correlated with imaging and competing diagnoses.',
    'The mJOA framework classifies ==15–17 as mild, 12–14 as moderate and 11 or less as severe==. The score supports rather than replaces functional assessment and consideration of progression.',
    'Cord T2 signal can inform the evaluation but is not required to make every clinically supported case important. Conversely, incidental stenosis does not establish symptomatic DCM.'),
  S('Match the Strategy to Severity and Course','**Guidelines recommend surgery for moderate/severe DCM**, while mild disease permits an individualized discussion of surgery or structured supervised nonoperative care with close follow-up.',
    'Deterioration during nonoperative management changes the balance toward surgery. The 2026 mild-DCM recommendations emphasize patient disability and symptoms alongside the score and acknowledge evidence limitations.',
    'Discuss goals as prevention of further injury and possible recovery, without guaranteeing reversal of established deficits. Nonmyelopathic compression without radiculopathy does not automatically warrant prophylactic surgery. Provide safety and rehabilitation advice while arranging assessment, and avoid allowing a generic neck-pain pathway to delay review of progressive cord dysfunction.')],['DCM','DCM26','ACR'])

add('Compressive and structural myelopathy','Treat the Cause of a Syrinx',
 'MRI identifies an enlarging cervical syrinx and Chiari I malformation in a patient with progressive hand weakness. Which approach is most appropriate?',
 'Neurosurgical assessment of the Chiari/CSF-flow abnormality and cause-directed treatment',[
 ('Direct syrinx shunting as the required first procedure in every case','Shunting has selected roles, but treatment commonly addresses the cause of disturbed CSF flow first; one procedure is not mandatory for all syringomyelia.'),
 ('Immune therapy for presumed demyelination based on the cavity alone','A syrinx is a structural fluid cavity, not itself evidence of inflammatory demyelination; the associated Chiari anatomy requires a different assessment.'),
 ('Symptom treatment without reassessment despite objective progression','Analgesia and rehabilitation matter, but enlargement with progressive weakness warrants etiologic neurosurgical evaluation rather than symptom-only observation.')],
 [S('The Cavity Is a Finding With Several Causes','**Syringomyelia can be associated with Chiari malformation, prior trauma, tumor or arachnoid disease.** Imaging should characterize the extent and investigate the relevant underlying cause.',
    'A central cord cavity can produce dissociated sensory findings and segmental weakness, but the clinical burden and progression vary. Localization does not by itself specify treatment.',
    'Review the craniocervical junction, cord and possible CSF obstruction. Selected additional imaging helps when the mechanism is unclear or another lesion is suspected.'),
  S('Progression Changes the Management Discussion','**Symptomatic progressive disease merits specialist evaluation.** In Chiari-associated cases, decompression aims to improve the craniocervical/CSF-flow problem, with technique individualized to anatomy and expertise.',
    'Not every incidental small cavity requires surgery. Observe appropriate stable cases with a clear clinical and imaging plan, rather than applying one radiologic size threshold to every patient.',
    'Explain that symptom improvement and syrinx shrinkage do not correlate perfectly, and established injury may persist. Follow strength, sensation, gait and function after treatment. Further procedures depend on clinical course and residual anatomy; do not treat a persistent image alone as automatic surgical failure or ignore new weakness because pain is controlled.')],['SYRINX','CHIARI','ACR'])

add('Conus medullaris and cauda equina emergencies','Incomplete Cauda Equina Syndrome',
 'A patient with severe lumbar pain develops altered perineal sensation, reduced awareness of bladder filling and difficulty initiating urination, but can still void voluntarily. Which interpretation is most appropriate?',
 'Possible incomplete CES requiring urgent investigation',[
 ('Uncomplicated radiculopathy because voluntary voiding is retained','Retention is not required for incomplete CES; new saddle and bladder-sensory changes require urgent assessment even while executive bladder control persists.'),
 ('Established painless-retention CES because any urinary symptom meets that category','Retention-stage CES implies loss of bladder control with retention, often overflow; the current history instead raises an earlier incomplete syndrome.'),
 ('A purely urologic disorder until bilateral paralysis develops','Urologic causes can coexist, but saddle change with a spinal pain syndrome requires prompt spinal evaluation rather than waiting for major motor loss.')],
 [S('Recognize Change Before Complete Retention','**CES can be incomplete**, with altered urinary sensation, poor stream, straining or loss of normal desire to void while some voluntary control remains.',
    'Ask directly about saddle sensation, bowel and sexual function, bladder awareness and the evolution of symptoms. Patients may not volunteer these details or use the term incontinence accurately.',
    'A classic bilateral sciatica or paralysis pattern is not mandatory. Individual bedside findings have limited sensitivity, so absence of one sign does not safely close the diagnosis.'),
  S('Do Not Wait for a Later Stage','**Arrange urgent lumbar MRI and specialist assessment** when compressive CES is suspected. Document the history, examination, onset and progression, and address bladder/analgesia needs in parallel.',
    'Postvoid residual can support assessment but must be interpreted with symptoms and examination. A low residual does not exclude incomplete CES.',
    'Disc disease is a common cause, but tumor, hematoma, infection and other lesions need consideration. Once compression is confirmed, urgent surgical decision making should aim to preserve remaining function. The distinction between incomplete and retention-stage disease informs prognosis and communication; it is not a reason to withhold an emergency pathway from either group.')],['CES','PVR'])

add('Conus medullaris and cauda equina emergencies','A Low PVR Does Not Exclude CES',
 'A patient with new saddle sensory change and altered urinary awareness has a postvoid residual of 90 mL. Which next step is most appropriate?',
 'Continue urgent CES assessment and MRI according to the clinical suspicion',[
 ('Exclude CES because the residual is below 200 mL','The 200-mL threshold can aid risk assessment but cannot exclude incomplete CES; MRI-confirmed cases requiring decompression can have lower residuals.'),
 ('Repeat the bladder scan days later before deciding whether spinal imaging is needed','Repeat scans can help follow bladder function, but should not delay urgent anatomical assessment when new sacral symptoms raise concern.'),
 ('Use urinary catheterization as the definitive diagnostic test for the spinal cause','Catheterization may treat retention and quantify output, but cannot establish or exclude the compressive lesion responsible for neurologic bladder symptoms.')],
 [S('Bladder Ultrasound Is an Adjunct','**A PVR of about ==200 mL or more== raises concern** in a compatible presentation and can improve risk stratification. It does not function as a universal binary diagnostic rule.',
    'Incomplete disease may preserve enough emptying to yield a low residual despite abnormal bladder sensation or sacral dysfunction. Measurement timing, baseline urologic disease and medicines also influence the result.',
    'Interpret the value with perineal symptoms, motor/sensory examination and the clinical course. Do not substitute a bladder number for assessment of the neurologic syndrome.'),
  S('Use MRI to Answer the Compression Question','**Urgent MRI remains the key anatomical investigation** when CES is suspected. Clinical concern can justify imaging despite a residual below the commonly quoted threshold.',
    'A high residual also has non-CES causes and should not independently assign a spinal diagnosis. Address retention when present while investigating the cause.',
    'The published low-PVR CES series is selected evidence and should not be used to derive population prevalence, but it demonstrates why a low value cannot safely exclude every case. Explain test limitations clearly and document a timely plan rather than reassuring a patient solely from one apparently favorable measurement.')],['CES','PVR'])

R['SCANNEG']=('Scan-negative CES: prospective cohort study','https://doi.org/10.1212/WNL.0000000000011154')

add('Conus medullaris and cauda equina emergencies','Urgent MRI and Decompression Assessment',
 'A patient develops progressive saddle numbness, leg weakness and new urinary dysfunction. MRI shows a large central lumbar disc prolapse compressing the cauda equina. Which next action is most appropriate?',
 'Urgent spine-surgical assessment for decompression as early as feasible',[
 ('Wait until 48 hours have elapsed because surgery before then is unnecessary','Timing studies use heterogeneous definitions and cannot turn a proposed upper window into permission to delay progressive compression.'),
 ('Use a prolonged oral steroid trial before seeking a surgical decision','Steroids do not remove a large compressive disc and are not a substitute for urgent decompression assessment in confirmed CES.'),
 ('Reassess after outpatient physiotherapy because some voluntary bladder control remains','Incomplete CES can retain bladder control, but remaining function is a reason for timely preservation rather than a justification for delaying care.')],
 [S('The Anatomical Cause Has Been Demonstrated','**Confirmed compressive CES requires an urgent specialist decision.** Large disc prolapse is common, but the treatment plan must account for the actual lesion and neurologic trajectory.',
    'Record symptom onset and progression carefully, including changes in bladder sensation versus established retention. Provide analgesia, bladder care and safe handling while definitive care is arranged.',
    'Neither normal leg power in one muscle group nor residual voluntary voiding excludes important sacral dysfunction.'),
  S('Interpret Timing Evidence Without Creating Delay','**WFNS recommends early decompression, preferably within 24 hours and within 48 hours where feasible**, while acknowledging limitations and inconsistency in the underlying timing literature.',
    'The practical aim is prompt treatment after diagnosis rather than waiting for a clock threshold. Delayed presentation does not automatically make surgery futile; assess ongoing compression and potential benefit individually.',
    'Discuss uncertain recovery of bladder, bowel, sexual and motor function without guaranteeing reversal. The severity and duration of injury influence outcome, but prognosis cannot be inferred from one time cutoff alone. Continue postoperative rehabilitation and urologic follow-up, because mechanical decompression and restoration of neurologic function are not identical events.')],['CES','PVR'])

add('Conus medullaris and cauda equina emergencies','Conus and Cauda Patterns Overlap',
 'A patient has acute saddle sensory loss and early bladder/bowel dysfunction, relatively symmetric leg findings and a mixture of brisk knee responses with reduced ankle reflexes. Which localization deserves particular consideration?',
 'Conus medullaris involvement, potentially with adjacent roots',[
 ('An isolated single lumbar radiculopathy','One root can cause focal pain, weakness and reflex change, but does not adequately explain bilateral sacral sensory and early sphincter dysfunction.'),
 ('A typical length-dependent distal polyneuropathy','DSP can reduce ankle reflexes and distal sensation, but does not characteristically produce this acute saddle/sphincter syndrome.'),
 ('A pure distal muscle disorder','Muscle disease does not explain saddle sensory loss and neurogenic sphincter dysfunction; preserved sensory pathways would be expected in an isolated myopathy.')],
 [S('Clinical Clues Are Probabilistic','**Conus lesions can produce early sacral dysfunction and mixed upper/lower motor neuron findings.** Adjacent root involvement can blur an idealized distinction from CES.',
    'Cauda lesions often have radicular pain, asymmetric weakness and reduced reflexes, but symmetry or pain patterns are not sufficiently reliable to assign every case without imaging.',
    'Examine perineal sensation, motor distribution, reflexes and sphincter function while asking about the tempo and associated back pain.'),
  S('Localize Without Delaying the Emergency Pathway','**Both suspected conus and cauda compression need urgent anatomical assessment.** The exact vertebral level of the conus varies, so imaging coverage should reflect the syndrome and not a rigid single-level assumption.',
    'MRI identifies disc, tumor, hemorrhage, infection or intrinsic pathology and guides definitive management. A mixed reflex pattern does not justify postponing investigation until the examination becomes textbook.',
    'Use localization to refine the search and prognosis, not to reduce urgency. Bladder ultrasound is adjunctive, and a low residual cannot exclude an incomplete sacral syndrome. Treat retention and immediate complications while seeking the cause; persistent or progressive findings with a nondiagnostic study require review of image coverage and competing diagnoses.')],['CES','APPROACH','ACR'],table=(['Feature','Conus tendency','Cauda tendency'],[
 ['Distribution','More symmetric sacral/leg findings','Often asymmetric root-pattern deficits'],
 ['Reflex pattern','Can mix UMN and LMN features','Predominantly LMN'],
 ['Sphincter symptoms','Can appear early','Variable; incomplete disease may still void'],
 ['Clinical implication','Urgent imaging; overlap limits bedside certainty','Urgent imaging; do not wait for complete retention']]))

add('Conus medullaris and cauda equina emergencies','After MRI Excludes Cauda Compression',
 'A patient has severe back pain and urinary difficulty, but a technically adequate lumbar MRI reviewed by specialists shows no cauda equina compression. Symptoms persist. What is the best next approach?',
 'Reassess neurologic and urologic causes, medicines and symptom mechanisms, with follow-up and renewed investigation if findings warrant',[
 ('Perform lumbar decompression despite no demonstrated surgical target','Surgery requires an appropriate structural indication; symptoms alone do not establish a compressive target after adequate imaging.'),
 ('End assessment because a negative lumbar scan proves that symptoms are fabricated','A negative scan excludes the assessed compression but does not invalidate symptoms or exclude urologic, medication-related, other neurologic or functional mechanisms.'),
 ('Assign permanent neurogenic bladder from CES solely on the initial symptoms','Urinary symptoms have several mechanisms, and the cause and prognosis need assessment rather than a permanent label unsupported by current anatomical evidence.')],
 [S('A Negative Compression Study Answers One Question','**Scan-negative suspected CES is common**, and a high-quality negative lumbar study changes the need for emergency lumbar decompression. It does not explain every symptom by itself.',
    'Review image coverage and the examination. A new sensory level, pyramidal findings or other discordance can justify investigation above the lumbar region or for a different neurologic process.',
    'Assess urinary retention, infection, preexisting bladder disease and medications such as opioids or anticholinergic agents. Treat immediate bladder needs while clarifying etiology.'),
  S('Give a Positive Plan Rather Than Dismissal','**Pain-related bladder changes and functional neurologic mechanisms can contribute** in selected patients, but should be assessed through a clinical framework rather than inferred as deception from a negative MRI.',
    'Use positive findings and appropriate specialist input when diagnosing a functional disorder. Explain the result, symptom-management strategy, medication review and follow-up in understandable terms.',
    'Provide return precautions for new or progressive weakness, saddle change or bladder/bowel deterioration, with prompt reassessment when indicated. An old negative scan does not exclude a new future lesion. Conversely, repeated imaging without a changed clinical question may not resolve persistent symptoms; rehabilitation, pain and urologic pathways can be important once dangerous compression is excluded.')],['SCANNEG','CES','APPROACH'])

R.update({
 'INFARCT':('Spontaneous spinal cord infarction: characteristics and proposed diagnostic criteria, 2019','https://doi.org/10.1001/jamaneurol.2018.2734'),
 'LESIONS':('Practical approach to spinal cord lesions, 2018','https://doi.org/10.1136/practneurol-2017-001845'),
 'AORTA':('ACC/AHA aortic disease guideline, 2022','https://doi.org/10.1016/j.jacc.2022.08.004'),
})

add('Vascular spinal cord disorders','Acute Spinal Cord Infarction',
 'During an episode of severe systemic hypotension, a patient develops abrupt paraplegia with pain/temperature loss and relative preservation of position sense. MRI excludes an epidural compressive lesion. Which diagnosis is most likely?',
 'Spinal cord ischemic infarction',[
 ('Acute inflammatory transverse myelitis','Myelitis can produce motor, sensory and sphincter deficits, but the abrupt onset during severe hypotension and selective vascular pattern more strongly suggest ischemia.'),
 ('Degenerative cervical myelopathy','Degenerative disease generally has a more chronic course with concordant mechanical compression; that context does not explain this abrupt hypoperfusion-associated syndrome.'),
 ('Vitamin B12-related myelopathy','B12 disease usually evolves subacutely with prominent posterior-column dysfunction, rather than this hyperacute hypoperfusion-linked pattern with relative position-sense preservation.')],
 [S('Recognize the Vascular Context','**Spinal infarction can follow systemic hypoperfusion, aortic disease or procedures**, and can also occur spontaneously through other vascular mechanisms.',
    'A sudden severe deficit supports the diagnosis, but the full classic anterior-cord pattern is not obligatory. Pain, weakness, sensory and sphincter findings depend on the territory and extent.',
    'Early flaccidity and areflexia can occur. They do not override a sensory level or the vascular time course and should not automatically redirect the diagnosis to peripheral neuropathy.'),
  S('Confirm and Address the Mechanism','**MRI assesses the cord and excludes urgent compression.** Diffusion restriction, a compatible axial pattern or adjacent vertebral-body infarction can strengthen confidence, while early studies can be nondiagnostic.',
    'Investigate hypotension, aortic pathology and other mechanisms according to the clinical context. Restore appropriate perfusion and oxygen delivery while excluding hemorrhage and other causes of shock.',
    'Evidence for routine cerebral-stroke-style thrombolysis or one universal antithrombotic regimen in spinal infarction is limited; treatment must follow the identified cause and specialist assessment. Provide bladder, skin, thrombosis and rehabilitation care. Do not presume that an intrinsic cord T2 lesion requires steroids merely because it is visible within the cord.')],['INFARCT','LESIONS','AORTA'])

add('Vascular spinal cord disorders','Early Negative MRI in Suspected Infarction',
 'A patient has abrupt severe myelopathy with a vascular context. MRI obtained two hours after onset excludes compression but shows no definite intrinsic lesion. Which next interpretation is most appropriate?',
 'Early negative cord imaging does not exclude infarction; arrange clinically directed repeat MRI with diffusion-sensitive assessment',[
 ('The normal scan establishes a functional diagnosis','A functional disorder requires a positive clinical framework; early imaging sensitivity is imperfect and cannot negate a compelling acute cord syndrome by itself.'),
 ('The normal scan excludes spinal disease and makes repeat imaging unnecessary','Some acute cord lesions, especially ischemic ones, are initially subtle or absent on routine sequences; persistence of objective findings warrants reassessment.'),
 ('The negative scan proves inflammatory disease because infarction is immediately visible','Both mechanisms require clinical/imaging integration, and infarction may be initially MRI-negative; the time course does not support this inference.')],
 [S('Imaging Sensitivity Changes With Time','**A normal early MRI can occur in spinal infarction.** In the cited spontaneous-infarction cohort, initial scans were normal in about one quarter of patients.',
    'Diffusion-weighted and ADC sequences can provide useful evidence but are technically more difficult in the cord than in the brain. Artifact and incomplete coverage also affect interpretation.',
    'Review the actual sequences, timing and clinical level with neuroradiology. Repeat imaging should address a defined unresolved question rather than mechanically repeating a limited study.'),
  S('Continue Clinical and Etiologic Assessment','**Persistent objective myelopathy remains clinically important** even before a clear intrinsic lesion appears. Continue serial examination and monitor sphincter, respiratory and hemodynamic status as appropriate.',
    'Investigate aortic or perfusion causes when indicated and maintain exclusion of evolving compression, inflammation and other mimics. CSF may contribute when the differential warrants and it is safe to obtain.',
    'Later T2 abnormalities or enhancement must still be interpreted with the vascular tempo; subacute enhancement does not retrospectively prove autoimmune myelitis. Communicate the provisional diagnosis and imaging limits clearly without offering a premature guarantee of either benignity or irreversible prognosis.')],['INFARCT','LESIONS','ACR'])

add('Vascular spinal cord disorders','Delayed Weakness After Aortic Repair',
 'A patient develops new paraparesis after thoracoabdominal aortic repair during a hypotensive episode. Which response best addresses a potentially reversible spinal-perfusion problem?',
 'Urgent aortic/critical-care assessment to optimize perfusion and oxygen delivery, with specialist consideration of CSF drainage',[
 ('Observe until the next day because delayed weakness cannot be related to the operation','Spinal ischemic dysfunction can appear after a delay; timely perfusion-directed measures can be important rather than dismissing the temporal association.'),
 ('Use high-dose corticosteroids as the principal treatment without reviewing perfusion','Steroids do not replace correction of hypotension, oxygen-delivery problems or procedure-related vascular compromise in this setting.'),
 ('Lower blood pressure further to protect the aortic repair regardless of the neurologic decline','Aortic management requires individualized targets, but worsening spinal hypoperfusion demands urgent coordinated reassessment rather than unqualified additional pressure reduction.')],
 [S('Spinal Perfusion Has Arterial and Intrathecal Components','**Spinal cord perfusion depends on systemic pressure relative to surrounding CSF pressure.** Hypotension, altered vascular supply and elevated intrathecal pressure can impair effective perfusion.',
    'The ACC/AHA 2022 aortic guideline recommends timely measures to optimize cord perfusion and reduce intrathecal pressure for delayed dysfunction after relevant aortic repair.',
    'Assessment includes bleeding, volume status, oxygenation, hemoglobin and the repair/vascular anatomy. New weakness should not be treated as a routine postoperative rehabilitation issue.'),
  S('Use a Specialist Rescue Pathway','**Optimize hemodynamics and oxygen delivery promptly**, with aortic-surgical and critical-care input. Vasopressor or volume decisions require the whole cardiac and vascular context.',
    'CSF drainage can improve the pressure gradient in selected peri-aortic cases but is an invasive procedure with bleeding and other risks. It should not be generalized to every spontaneous cord infarct or performed without an appropriate safety protocol.',
    'Image and investigate other causes when needed while avoiding unnecessary delay in rescue measures. Continue serial neurologic assessment, and arrange rehabilitation and prevention of secondary complications after stabilization. Distinguish this cause-specific perfusion strategy from an unsupported universal treatment for all acute myelopathies.')],['AORTA','INFARCT','ENLS'])

R.update({
 'DAVF':('Spinal dorsal intradural AV fistulas: imaging and management review, 2023','https://pmc.ncbi.nlm.nih.gov/articles/PMC10516273/'),
 'DAVFDELAY':('AJNR primary series: delayed diagnosis of spinal dural AV fistula, 2016','https://doi.org/10.3174/ajnr.A4504'),
 'DAVFSTEROID':('Prospective cohort: steroid-associated worsening in spinal dural AV fistula, 2020','https://pubmed.ncbi.nlm.nih.gov/31923124/'),
})

add('Vascular spinal cord disorders','Venous Congestive Myelopathy',
 'An older man has months of progressive gait impairment, patchy sensory symptoms and urinary dysfunction. MRI shows long-segment thoracic/conus edema with prominent serpiginous vessels along the cord surface. Which diagnosis best fits?',
 'Spinal dural arteriovenous fistula',[
 ('AQP4-associated inflammatory myelitis','NMOSD can cause longitudinally extensive lesions, but the progressive course and prominent perimedullary vessels particularly raise a vascular shunt and venous congestion.'),
 ('Degenerative lumbar canal stenosis','Lumbar degeneration can cause pain and root symptoms, but does not sufficiently explain long-segment cord edema with dilated surface vessels.'),
 ('Subacute combined degeneration','A metabolic posterior-column/corticospinal syndrome can impair gait, but the vascular surface findings and congestive imaging pattern point elsewhere.')],
 [S('A Treatable Cause of Progressive Cord Dysfunction','**A spinal dural AV fistula can arterialize venous drainage**, causing venous hypertension, congestion and impaired cord function rather than a simple arterial infarct.',
    'Symptoms may progress gradually, fluctuate or worsen with activity. Older men are a common demographic, but neither age nor sex is an absolute diagnostic requirement.',
    'Long-segment T2 edema, conus involvement and abnormal perimedullary vessels are important clues. A lesion can enhance, so enhancement alone does not establish inflammation.'),
  S('Confirm the Shunt and Plan Disconnection','**Refer for experienced spinal vascular assessment and angiographic confirmation.** MR angiography can help localization, but catheter angiography defines the relevant arterial supply and venous drainage.',
    'Definitive treatment uses an appropriate surgical or endovascular strategy to eliminate the shunt. Anatomy, completeness of closure and procedural risk determine the choice.',
    'Earlier diagnosis can prevent additional disability; established deficits may not fully reverse after successful treatment. Do not attribute all symptoms to coincident lumbar degeneration or assume that a long cord lesion is automatically immune myelitis. Monitor gait and sphincter function and provide rehabilitation alongside definitive vascular treatment.')],['DAVF','DAVFDELAY','APPROACH'])

add('Vascular spinal cord disorders','When a Negative Angiogram Needs Review',
 'MRI strongly suggests a spinal dural fistula, but an outside catheter angiogram is reported negative. The procedure record shows that several relevant arterial territories were not examined. What is the best next step?',
 'Expert review of the angiogram and targeted completion or repeat angiography as indicated',[
 ('Exclude a fistula because any negative angiogram is definitive','A technically complete, well-interpreted study is highly informative, but an incomplete arterial survey can miss a shunt and cannot support the same conclusion.'),
 ('Replace vascular investigation with serial CSF protein measurements','CSF findings are nonspecific in congestive myelopathy and cannot resolve an incomplete anatomical shunt investigation.'),
 ('Start indefinite immune treatment and use subjective response as the reference standard','Immune therapy response is not a substitute for completing a strongly indicated vascular evaluation; delayed fistula diagnosis can permit additional irreversible injury.')],
 [S('Diagnostic Accuracy Depends on the Procedure','**Spinal catheter angiography is the reference anatomical investigation**, but requires appropriate coverage, technique and interpretation. A negative report is not equivalent to proof that every relevant vessel was adequately assessed.',
    'Review the actual images and injected territories with an experienced neurovascular team. The fistula level need not match the most prominent cord edema.',
    'MR angiography can guide planning and reduce uncertainty about localization, but should not be treated as a universal replacement for definitive angiographic characterization.'),
  S('Resolve Discordance Rather Than Choosing One Test Blindly','**Persistent clinicoradiologic suspicion warrants expert reassessment.** The AJNR delayed-diagnosis series documents cases missed on incomplete or misinterpreted angiography.',
    'A repeat procedure has risks and should address the suspected technical or coverage limitation. The decision is individualized rather than a rule to repeat every negative study.',
    'Avoid prolonged diagnostic closure on nonspecific inflammatory markers when imaging suggests venous congestion. Continue monitoring strength, gait and sphincter function, and reconsider other causes if a high-quality complete evaluation remains negative. Explain both the reason for further testing and the limits of certainty without promising that one image guarantees the final diagnosis.')],['DAVFDELAY','DAVF','APPROACH'])

add('Vascular spinal cord disorders','Steroid Worsening as a Vascular Warning',
 'A patient treated for presumed myelitis has progressive symptoms over months and deteriorates abruptly during intravenous methylprednisolone. MRI review reveals long-segment edema and abnormal perimedullary flow voids. Which next action is most appropriate?',
 'Reassess for a spinal vascular shunt and urgently arrange expert vascular imaging review',[
 ('Escalate steroids solely because deterioration establishes steroid-resistant inflammation','Worsening does not establish an immune mechanism; the chronic course and flow voids require vascular reassessment before automatic escalation.'),
 ('Diagnose an adverse drug allergy as the full explanation of the neurologic change','Allergy needs compatible systemic evidence; new neurologic decline with vascular imaging clues is not sufficiently explained by that label.'),
 ('Use the cord enhancement as proof that angiography is unnecessary','Congestive vascular myelopathy can enhance, and enhancement cannot override abnormal surface vessels and a discordant clinical course.')],
 [S('Do Not Use a Treatment Trial as the Diagnostic Gold Standard','**Steroid-associated deterioration is described in spinal dural fistula**, including prospective cohort evidence. It is an important warning in a clinically and radiologically compatible presentation.',
    'The association does not mean that every post-steroid decline proves a fistula. Disease progression, infection, metabolic effects and other complications still require assessment.',
    'Long-segment lesions and CSF protein elevation can occur outside immune disease. Review the entire pattern rather than retaining a myelitis diagnosis because one supportive test was nonspecific.'),
  S('Find the Mechanism Before More Immune Escalation','**Venous hypertension and congestion can impair cord perfusion**, with abnormal perimedullary vessels providing a key clue. Arrange experienced neuroradiologic review and catheter angiography when indicated.',
    'Steroid-worsening studies are not randomized proof of every proposed mechanism or a precise individual risk. They support diagnostic caution rather than a blanket prohibition of steroids for genuinely established inflammatory attacks.',
    'Treat acute deterioration with appropriate monitoring and reconsider compression or other emergencies in parallel. Once a shunt is confirmed, definitive closure is the disease-directed approach. Avoid allowing the time spent on repeated immune courses to substitute for an unresolved vascular investigation, because delayed treatment can leave persistent motor and sphincter disability.')],['DAVFSTEROID','DAVFDELAY','DAVF'])

R.update({
 'TM':('Transverse Myelitis Consortium proposed diagnostic framework, 2002','https://doi.org/10.1212/WNL.59.4.499'),
 'NEMOS':('NEMOS revised recommendations, part II: attack treatment, 2023','https://doi.org/10.1007/s00415-023-11910-z'),
})

add('Inflammatory and infiltrative myelopathy','Establishing an Inflammatory Myelopathy',
 'A patient develops bilateral leg weakness, a sensory level and sphincter symptoms over five days. MRI excludes compression and shows an intrinsic cord lesion. Which next assessment best supports etiologic classification?',
 'Integrate CSF inflammation, brain/cord imaging and phenotype-directed infectious, immune and metabolic testing',[
 ('Classify the disease as idiopathic transverse myelitis from the T2 lesion alone','A T2 lesion is not etiologically specific; idiopathic classification requires appropriate exclusion of alternative causes and assessment for a defined inflammatory disorder.'),
 ('Use isolated CSF protein elevation as sufficient evidence of autoimmunity','Protein can rise in vascular, structural and other processes; inflammatory cells, immune markers, imaging and clinical context carry different diagnostic information.'),
 ('Assign spinal infarction solely because bladder dysfunction is present','Bladder involvement occurs in several cord disorders; the subacute course and wider investigation are needed to distinguish mechanisms.')],
 [S('A Syndrome Requires a Cause-Based Workup','**Acute transverse myelopathy is not automatically idiopathic immune myelitis.** A compatible bilateral cord syndrome and exclusion of extra-axial compression begin the evaluation.',
    'The classic 2002 idiopathic-TM framework includes progression to nadir over ==4 hours to 21 days== and evidence of inflammation through CSF or enhancement, with specified exclusions.',
    'These historical syndrome criteria are not a replacement for contemporary AQP4/MOG, MS, infectious and other etiologic frameworks. Some early tests may be nondiagnostic and need clinically justified reassessment.'),
  S('Select Tests From the Phenotype','**Review CSF cells, protein and appropriate immune/infectious studies**, alongside brain and spinal MRI. Serum antibody testing and systemic evaluation depend on the presentation and pretest probability.',
    'Consider vascular tempo, medication/toxic exposure, nutritional risk, systemic autoimmune disease and malignancy. A positive nonspecific blood antibody does not independently explain a cord lesion.',
    'Treat a convincingly severe inflammatory attack promptly once urgent mimics are reasonably addressed; do not wait unnecessarily for every send-out result. Simultaneously monitor respiratory, motor and sphincter function and prevent secondary complications. The final diagnosis should remain revisable when progression or subsequent results contradict the initial label.')],['TM','APPROACH','LESIONS'])

add('Inflammatory and infiltrative myelopathy','LETM Is a Pattern, Not One Diagnosis',
 'MRI shows a central cord lesion spanning five vertebral segments. Which interpretation is most appropriate before assigning NMOSD?',
 'The lesion is longitudinally extensive, but requires antibody, clinical and competing-cause assessment',[
 ('Lesion length alone is sufficient to diagnose AQP4-associated NMOSD','LETM is an important clue but also occurs in other inflammatory, vascular, infiltrative and structural processes; the disease-specific diagnostic framework still applies.'),
 ('A five-segment lesion excludes vascular shunt disease','Venous congestive myelopathy can produce long-segment edema, often with conus and perimedullary vascular clues; length does not exclude it.'),
 ('Central axial location establishes MOG-associated disease independently of serology','MOG disease can involve central gray matter or conus, but axial pattern alone is not specific enough to establish the antibody-associated diagnosis.')],
 [S('Describe the Image Before Naming the Disease','**LETM generally denotes a lesion spanning at least three contiguous vertebral segments.** Axial distribution, expansion, enhancement and associated surface vessels refine the differential.',
    'AQP4-associated NMOSD and MOG-associated disease are important causes, but sarcoid, infection, neoplasia and venous congestion can produce overlapping appearances.',
    'A lesion’s measured length also depends on timing and imaging technique. Shorter lesions do not exclude every antibody-associated disorder, especially after evolution or treatment.'),
  S('Combine Independent Lines of Evidence','**Use validated serum antibody assays and the clinical phenotype**, brain imaging and appropriate CSF/systemic studies. Optic, area-postrema and other characteristic features can inform the disease framework.',
    'A weak unexpected antibody result needs assay and pretest-probability review. An extensive lesion plus a nonspecific protein rise does not establish one mechanism.',
    'Inspect for compression and perimedullary flow voids, and review tempo before immune escalation. A hyperacute deficit suggests a different pathway from a relapsing inflammatory syndrome or a months-long progressive congestion. Choose acute and long-term treatment according to the best-supported etiology rather than prescribing indefinite disease-specific prevention from lesion length alone.')],['APPROACH','LESIONS','NEMOS'],style='direct')

add('Inflammatory and infiltrative myelopathy','Early Apheresis in a Severe Inflammatory Attack',
 'A patient with a well-supported severe antibody-associated inflammatory myelitis remains markedly paraparetic despite initial high-dose IV methylprednisolone. Compression and important infectious mimics have been addressed. Which next treatment should be considered promptly?',
 'Plasma exchange or appropriate apheresis escalation',[
 ('Wait several months for azathioprine alone to reverse the acute deficit','Azathioprine can have a selected long-term prevention role, but delayed immune effects do not substitute for acute rescue in a severe ongoing attack.'),
 ('Begin an MS-specific maintenance drug as the immediate rescue strategy','Disease-specific preventive agents are not interchangeable acute rescue, and an MS regimen can be inappropriate in other antibody-associated disorders.'),
 ('Continue repeated steroid courses indefinitely before considering rescue','Additional steroid decisions can be individualized, but severe inadequate response warrants early apheresis assessment rather than an automatic prolonged sequence that delays escalation.')],
 [S('Separate Attack Rescue From Relapse Prevention','**High-dose IV methylprednisolone is a common acute treatment**, typically ==1,000 mg/day for 3–5 days== in the cited NMOSD attack guidance.',
    'The regimen requires monitoring for glucose, BP, infection, psychiatric and other adverse effects. The cause of myelopathy must remain clinically concordant before treating an image as immune disease.',
    'A severe attack may justify early or concurrent apheresis in selected circumstances; treatment need not always wait for a rigid definition of steroid failure.'),
  S('Escalate With Attention to Timing and Risk','**NEMOS recommends early apheresis when steroid response is insufficient in the first days.** Plasma exchange or immunoadsorption is selected according to availability, expertise and patient factors.',
    'A common course uses about five exchanges, sometimes more according to severity and response. Assess vascular access, hemodynamics, calcium, coagulation and infection risks.',
    'Document motor, sensory, sphincter and respiratory outcomes. Longer-term prevention and steroid taper depend on the established disorder and are distinct from rescue. Reconsider the diagnosis when treatment response or imaging is discordant, especially with a progressive course or vascular clues, rather than assuming all nonresponse means more of the same immune mechanism.')],['NEMOS','APPROACH','TM'])

R.update({
 'SARCOID':('Neurosarcoidosis Consortium consensus diagnostic framework, 2018','https://doi.org/10.1001/jamaneurol.2018.2295'),
 'NSREVIEW':('Neurosarcoidosis: clinical diagnosis and treatment review, 2021','https://doi.org/10.1212/NXI.0000000000001084'),
 'LM':('EANO–ESMO leptomeningeal metastasis guideline, 2023','https://doi.org/10.1016/j.esmoop.2023.101624'),
 'PNS':('Updated diagnostic criteria for paraneoplastic neurologic syndromes, 2021','https://doi.org/10.1212/NXI.0000000000001014'),
})

add('Inflammatory and infiltrative myelopathy','Tissue Strategy in Suspected Neurosarcoidosis',
 'A patient has subacute myelopathy with dorsal subpial enhancement and mediastinal lymphadenopathy. Infection and malignancy remain in the differential. Which diagnostic strategy is most appropriate when feasible?',
 'Biopsy an accessible extraneural lesion and integrate pathology with the neurologic syndrome and exclusions',[
 ('Diagnose definite neurosarcoidosis from the enhancement pattern alone','The imaging pattern can be suggestive but is not specific enough for a definite diagnosis; consensus certainty depends on pathology and exclusion of alternatives.'),
 ('Use serum ACE alone as the decisive diagnostic test','ACE can be supportive in some contexts but lacks sufficient sensitivity and specificity to establish the cause of a cord lesion.'),
 ('Perform spinal cord biopsy first despite an accessible systemic target','Neural biopsy can provide definite evidence in selected cases, but its morbidity makes a safer accessible systemic site preferable when it can resolve the diagnostic question.')],
 [S('A Suggestive Pattern Still Needs Confirmation','**Sarcoid-associated myelopathy can be longitudinally extensive**, sometimes with dorsal subpial or central enhancement patterns. Systemic clues help direct investigation but do not exclude infection or neoplasia.',
    'Review pulmonary, nodal, skin, ocular and other manifestations. CSF can show inflammation, but no isolated CSF ACE or protein finding is a definitive test.',
    'Granulomatous pathology also requires an appropriate differential, including tuberculosis and other infection in the relevant epidemiologic context.'),
  S('Choose the Safest Informative Tissue','**The 2018 framework distinguishes possible, probable and definite neurosarcoidosis.** Compatible neurologic disease plus extraneural biopsy-confirmed sarcoidosis supports probable disease after appropriate exclusions.',
    'Neural tissue confirmation supports definite disease, but is not required in every clinically managed case. Select biopsy based on yield, accessibility and risk rather than pursuing the highest-risk site simply to upgrade a label.',
    'Treatment commonly begins with corticosteroids for significant active disease, with specialist steroid-sparing or biologic strategies when needed. Establish diagnostic confidence and screen relevant infections before prolonged immunosuppression. Follow objective neurologic and systemic response; improvement with steroids alone is not proof that every infiltrative lesion was sarcoid.')],['SARCOID','NSREVIEW','APPROACH'])

add('Inflammatory and infiltrative myelopathy','Negative First CSF Cytology in Suspected Cancer Involvement',
 'A patient with cancer develops multifocal radicular and myelopathic symptoms with suspicious leptomeningeal enhancement. The first CSF cytology is negative. Which approach is most appropriate?',
 'Integrate clinical/MRI findings and obtain a repeat optimized CSF sample when safe and indicated',[
 ('Exclude leptomeningeal disease because a single cytology result is negative','Cytology has imperfect sensitivity; a negative first sample does not exclude disease when the phenotype and imaging remain suspicious.'),
 ('Diagnose a paraneoplastic immune syndrome solely from the negative cytology','Paraneoplastic disease is a different mechanism and requires its own evidence; negative cytology alone does not distinguish it from direct malignant involvement.'),
 ('Start a spinal decompression procedure without demonstrating a compressive target','Surgery addresses appropriate structural lesions, not every cancer-associated cord/root syndrome; the actual anatomy and mechanism must guide treatment.')],
 [S('Cancer Can Affect the Cord Through Several Mechanisms','**Direct epidural, intramedullary or leptomeningeal involvement differs from paraneoplastic myelopathy.** Treatment-related, infectious, metabolic and vascular causes can also occur in a patient with cancer.',
    'Contrast MRI and a focused clinical examination help characterize the distribution. The presence of cancer does not make every new deficit metastatic, but should prevent premature diagnostic closure.',
    'CSF studies should answer a defined question, with cytology, flow cytometry or other tests selected for the suspected malignancy and context.'),
  S('Optimize Sampling and Reassess the Mechanism','**EANO–ESMO recommends one repeat optimized LP after initially negative or equivocal studies** when leptomeningeal disease remains suspected. Ensure adequate collection and prompt processing with the laboratory.',
    'Assess procedure safety, including anticoagulation and relevant structural findings. Sampling limitations can explain a negative result, but repeated testing should still have a clear rationale.',
    'Paraneoplastic myelopathy may show tract-predominant lesions and antibodies such as CRMP5 or amphiphysin; interpret these with phenotype, assay reliability and cancer assessment. Antibody positivity does not replace exclusion of direct tumor or infection. Coordinate oncologic and neurologic treatment urgently when function is threatened rather than waiting indefinitely for one perfect confirmatory test.')],['LM','PNS','APPROACH','LP'])

add('Inflammatory and infiltrative myelopathy','Nonresponse Should Reopen the Differential',
 'A patient labeled as having idiopathic myelitis has continued progression over six months despite repeated immune treatment. Imaging and CSF were never fully concordant with an acute inflammatory attack. What is the best next step?',
 'Reassess the original localization, tempo, imaging and alternative causes before further immune escalation',[
 ('Interpret all progression as proof of refractory autoimmunity','Treatment resistance can reflect an incorrect mechanism, fixed damage or complications; it does not independently validate the original immune diagnosis.'),
 ('Stop etiologic investigation because a long T2 lesion was previously demonstrated','Long-segment signal is not unique to inflammation; vascular, compressive, metabolic and infiltrative causes remain important when the course is discordant.'),
 ('Use a mild isolated CSF protein increase as the deciding evidence for indefinite immunotherapy','Protein elevation is nonspecific and should not outweigh a chronic progressive course with unresolved imaging/clinical mismatch.')],
 [S('Ask What the Initial Evidence Actually Established','**A provisional myelitis label needs longitudinal reassessment.** Review the examination, time to nadir, lesion morphology, contrast behavior, vascular structures and the quality of prior studies.',
    'Obtain the original images and laboratory results rather than relying only on a summary diagnosis. Repeated subjective improvement is different from reproducible objective recovery.',
    'A six-month progressive course can suggest venous congestion, compression, neoplasia, sarcoid or a metabolic/inherited process, although chronic immune disorders also exist.'),
  S('Change the Test Strategy When the Question Changes','**Target testing to the unresolved mechanism.** This may involve expert vascular review, additional structural imaging, nutritional/toxic studies, systemic evaluation or selected tissue assessment.',
    'Separate active treatable disease from established damage and treatment complications. More immunosuppression can add infection and metabolic harm without correcting a missed structural or vascular cause.',
    'Do not abandon care or assume functional symptoms solely because treatment failed. Provide rehabilitation, symptom and sphincter management while clarifying the diagnosis. Escalation remains appropriate when a supported immune mechanism and objective activity are demonstrated; the point is to re-establish that evidence rather than treating the historical label as immutable.')],['APPROACH','LESIONS','DAVFDELAY','SARCOID'])

R.update({
 'B12':('NICE NG239: B12 deficiency, including nitrous oxide exposure, 2024','https://www.nice.org.uk/guidance/ng239/chapter/Recommendations'),
 'COPPER':('Primary clinical series: copper deficiency myelopathy, 2004','https://doi.org/10.1212/01.WNL.0000132644.52613.FA'),
 'HIV':('DGN guideline: diagnosis and therapy of HIV-1-associated neurologic disorders, 2026','https://pmc.ncbi.nlm.nih.gov/articles/PMC13474671/'),
})

add('Metabolic, infectious and chronic myelopathies','Nitrous Oxide and Functional B12 Deficiency',
 'A patient using recreational nitrous oxide develops sensory ataxia, impaired position sense and pyramidal signs. Serum B12 is within range after recent supplementation. Which investigation best addresses the suspected mechanism?',
 'A functional marker such as serum MMA or plasma homocysteine, interpreted with relevant confounders',[
 ('Repeat total B12 alone and exclude deficiency if it remains normal','Nitrous oxide can inactivate B12 function despite apparently normal measured concentrations, especially after supplements; repeating total concentration alone misses that mechanism.'),
 ('Use a normal hemoglobin to exclude a nutritional cord disorder','Neurologic B12 disease can occur without anemia or macrocytosis, so a normal count cannot exclude this myeloneuropathic presentation.'),
 ('Use CSF oligoclonal bands as the primary test for the toxic exposure','OCBs can contribute to an immune differential, but do not directly investigate functional cobalamin impairment associated with nitrous oxide.')],
 [S('Measured Concentration and Function Can Diverge','**Nitrous oxide impairs cobalamin-dependent function**, producing a potentially treatable myeloneuropathy. Posterior-column sensory ataxia and corticospinal signs can coexist with peripheral nerve findings.',
    'Ask specifically about use, frequency and supplements. A normal serum B12 result does not eliminate functional impairment in this context.',
    'NICE NG239 recommends functional testing with homocysteine or MMA when recreational nitrous oxide is suspected. Renal dysfunction can elevate MMA, and folate or other factors can alter homocysteine.'),
  S('Stop Exposure and Treat Neurologic Disease Promptly','**Arrange prompt B12 replacement and cessation of nitrous oxide**, with support for sustained exposure reduction. Testing should not create a harmful delay when significant neurologic deficiency is suspected.',
    'Choose replacement route and regimen according to neurologic severity, absorption and local guidance. Supplements do not make ongoing nitrous oxide use safe.',
    'Assess gait, falls, sensation, sphincter function and coexisting nutritional causes. MRI may support a posterior-column pattern but is not required to be abnormal in every case. Recovery varies with duration and injury burden; laboratory correction does not guarantee immediate neurologic reversal. Reassess atypical progression for structural, vascular or other metabolic disease.')],['B12','APPROACH'])

add('Metabolic, infectious and chronic myelopathies','Copper Deficiency After Gastric Surgery',
 'A patient with prior gastric bypass develops spastic gait, loss of position sense and anemia/neutropenia despite adequate B12 replacement. There is frequent use of a zinc-containing supplement. Which tests are most appropriate?',
 'Serum copper, ceruloplasmin and zinc',[
 ('AChR and MuSK antibodies','These investigate autoimmune transmission disease, which does not explain the posterior-column and pyramidal syndrome with cytopenias and malabsorptive/exposure context.'),
 ('Anti-GM1 antibodies and motor conduction-block testing alone','MMN is a motor neuropathy and does not account for posterior-column dysfunction with this nutritional and hematologic pattern.'),
 ('CSF protein alone to establish inflammatory myelitis','Protein is nonspecific and cannot replace assessment of a plausible treatable nutritional cause; the gastric/zinc history is directly relevant.')],
 [S('A B12-Like Syndrome With a Different Deficiency','**Copper deficiency can cause myeloneuropathy** with sensory ataxia and spasticity, sometimes accompanied by anemia or neutropenia. It can mimic subacute combined degeneration.',
    'Risk factors include gastric surgery, malabsorption and excess zinc exposure. Review all supplements and other zinc sources rather than asking only about prescribed medicines.',
    'Low copper and ceruloplasmin support deficiency in the proper context; zinc measurement can reveal an important contributor but need not be high in every deficient patient.'),
  S('Correct the Cause and Monitor More Than Blood Counts','**Replace copper through an individualized nutritional plan** and remove excess zinc where relevant. Severity, absorption and adherence influence the route and replacement strategy.',
    'Investigate the cause of malabsorption and other deficiencies, including B12, rather than assuming one nutrient explains all abnormalities. Avoid interpreting low ceruloplasmin without the broader clinical and biochemical context.',
    'Hematologic recovery can precede or exceed neurologic recovery; established spinal injury may only stabilize or partially improve. Follow gait, proprioception, strength and laboratory indices. A normal MRI does not exclude the syndrome, and a lack of complete recovery does not by itself invalidate a well-supported deficiency diagnosis.')],['COPPER','B12','APPROACH'])

add('Metabolic, infectious and chronic myelopathies','HIV-Associated Vacuolar Myelopathy Is an Exclusion Diagnosis',
 'A person with advanced HIV has gradually progressive spastic paraparesis, posterior-column sensory impairment and urinary urgency. Which diagnostic approach is most appropriate before assigning vacuolar myelopathy?',
 'Exclude compression, opportunistic/infectious and nutritional causes through targeted imaging and laboratory/CSF assessment',[
 ('Diagnose vacuolar disease from HIV status and spasticity alone','HIV raises several competing risks, including treatable infection and malignancy; the association does not establish one cord mechanism.'),
 ('Use a normal spinal MRI to exclude all HIV-related neurologic disease','Vacuolar myelopathy may have normal imaging or atrophy, and other processes require phenotype-directed investigation; normal imaging is not an all-purpose exclusion.'),
 ('Use plasma CMV seropositivity as sufficient proof of CMV polyradiculomyelitis','Exposure serology is not proof of active neurologic CMV disease; the clinical pattern and appropriate CSF/pathogen assessment are needed.')],
 [S('Recognize the Pattern but Preserve the Differential','**HIV-associated vacuolar myelopathy** often produces a chronic spastic and sensory-ataxic syndrome with bladder dysfunction, especially in advanced disease.',
    'MRI may show thoracic-predominant atrophy or tract changes, but findings are not uniquely diagnostic. The absence of a compressive lesion answers only part of the evaluation.',
    'Assess B12 and other nutritional/metabolic causes, syphilis/HTLV risk and opportunistic infection or lymphoma according to immune status and presentation.'),
  S('A Different Tempo Can Signal Another Cause','**CMV polyradiculomyelitis can cause painful, rapidly progressive lower-motor-neuron/root disease** with retention in severe immunosuppression. Its investigation and treatment differ from assigning a chronic vacuolar syndrome.',
    'Use CSF studies and imaging selected for the actual clinical question, with attention to LP safety. Do not equate a positive blood exposure marker with proven central infection.',
    'Optimize antiretroviral care with an HIV specialist and treat identified alternatives. Provide gait, bladder, spasticity and rehabilitation support. There is no single confirmatory serum biomarker for vacuolar myelopathy; persistent discordance or progression requires reassessment rather than assuming all neurologic deterioration is an inevitable consequence of HIV.')],['HIV','APPROACH','B12'])

R.update({
 'HTLV':('HAM/TSP systematic review and consensus recommendations, 2019','https://pmc.ncbi.nlm.nih.gov/articles/PMC8101298/'),
 'TB':('Government of India INDEX-TB extrapulmonary tuberculosis guideline','https://tbcindia.mohfw.gov.in/wp-content/uploads/2023/05/5585665076Index-TB-Guidelines.pdf'),
 'HSP':('GeneReviews: uncomplicated hereditary spastic paraplegia, updated 2025','https://www.ncbi.nlm.nih.gov/books/NBK1509/'),
})

add('Metabolic, infectious and chronic myelopathies','HTLV-1-Associated Spastic Paraparesis',
 'An adult with epidemiologic HTLV-1 exposure risk has chronic progressive spastic paraparesis, early urinary urgency and little arm involvement. Structural compression has been excluded. Which targeted investigation is most relevant?',
 'HTLV-1 testing with appropriate confirmation and clinical/CSF evaluation',[
 ('AChR antibody testing as the primary explanation','MG produces motor fatigability rather than a spastic cord syndrome with urinary dysfunction; its antibodies do not address this epidemiologic and clinical pattern.'),
 ('PMP22 copy-number testing as the initial etiologic test','PMP22 disorders usually produce peripheral neuropathy patterns, not a primary chronic pyramidal/sphincter syndrome; inherited causes can be assessed if the broader workup supports them.'),
 ('A normal CK as sufficient exclusion of a neurologic cause','CK does not assess corticospinal tract disease; a normal muscle enzyme result cannot explain away objective spastic paraparesis.')],
 [S('A Chronic Inflammatory Cord Syndrome','**HAM/TSP is associated with HTLV-1 infection** and often presents with progressive leg spasticity, weakness and bladder dysfunction. Epidemiology and exposure history help select testing.',
    'Assess sensory symptoms, bowel/sexual function and the rate of decline. The phenotype overlaps with hereditary, degenerative, nutritional, vascular and other inflammatory causes.',
    'A positive screening antibody does not alone prove that HTLV-1 causes every neurologic symptom; confirm infection and integrate the syndrome and appropriate CSF/systemic findings.'),
  S('Assess Activity and Disability','**Management depends on progression and disease activity**, with specialist consideration of anti-inflammatory treatment in appropriate patients and explicit recognition that evidence is limited.',
    'Do not promise that antiviral therapy alone reliably reverses established HAM/TSP. Provide individualized spasticity, bladder, mobility and rehabilitation care.',
    'Review infection risks before immunosuppression and counsel about transmission through an appropriate service. Exclude treatable alternatives such as compression, B12/copper deficiency and other infections rather than assigning the diagnosis from geography alone. Longitudinal gait, strength and sphincter measurements help distinguish active deterioration from fixed disability and guide realistic treatment goals.')],['HTLV','HIV','APPROACH'])

add('Metabolic, infectious and chronic myelopathies','Spinal Tuberculosis With Neurologic Deterioration',
 'A patient has vertebral destruction, a paravertebral collection and progressive leg weakness. Spinal tuberculosis is suspected. Which approach is most appropriate?',
 'Urgent stability/compression assessment, tissue-based microbiology where feasible and specialist antituberculous/surgical planning',[
 ('Diagnose drug-sensitive TB from MRI alone and postpone neurologic reassessment','Imaging can strongly suggest TB but does not establish susceptibility or exclude competing disease; progressive weakness needs urgent structural and neurologic review.'),
 ('Treat every spinal TB case with immediate surgery regardless of anatomy or response','Many cases can be managed medically, while surgery has selected indications such as neurologic compromise, instability, deformity or diagnostic needs; decisions are individualized.'),
 ('Use corticosteroids alone until the collection resolves','Steroids do not provide definitive antimicrobial treatment or stabilization and are not an adequate sole strategy for destructive compressive spinal infection.')],
 [S('Confirm Organism and Assess Mechanical Consequences','**Spinal TB can destroy vertebrae and cause epidural or paravertebral disease**, leading to deformity, instability and neurologic compromise.',
    'Obtain tissue for appropriate molecular testing, culture/susceptibility and histology when feasible. Imaging appearance or granulomas alone do not identify every organism or resistance pattern.',
    'Consider pyogenic infection, malignancy and other granulomatous disease according to the context. Evaluate pulmonary or other sites and infection-control needs.'),
  S('Medical Therapy and Surgery Have Complementary Roles','**Use a multidrug antituberculous regimen through the relevant TB programme**, tailored to susceptibility, patient factors and local guidance. Do not assume a single duration applies to every extrapulmonary presentation.',
    'Progressive weakness, significant compression, instability or deformity warrants urgent spine-surgical assessment. An abscess on imaging is not by itself a universal mandate for one operation, but neurologic decline should not be observed casually.',
    'Monitor drug toxicity, adherence, objective function and structural recovery. Worsening can reflect resistance, mechanical injury, paradoxical inflammation or another diagnosis and needs reassessment. Provide pain, bladder, skin and rehabilitation support while protecting an unstable spine; antimicrobial therapy alone cannot immediately reverse every mechanical threat.')],['TB','IDSA','ACR'])

add('Metabolic, infectious and chronic myelopathies','Before Labeling Hereditary Spastic Paraplegia',
 'An adult has years of slowly progressive symmetric leg spasticity and a similarly affected parent. Which diagnostic strategy is best?',
 'Exclude relevant acquired/treatable causes and use phenotype- and pedigree-informed genetic testing',[
 ('Diagnose one specific HSP gene from the family history alone','A pedigree can suggest inheritance but does not uniquely identify a gene; HSP is genetically heterogeneous and different causes can share a similar pattern.'),
 ('Skip spinal imaging because familial disease excludes compression','An inherited predisposition or family history does not exclude a coexisting acquired lesion; structural evaluation is selected according to clinical context.'),
 ('Use a negative limited gene panel to exclude all hereditary disease','Panels differ in gene and variant-class coverage and cannot resolve every mechanism; an unrevealing result requires interpretation rather than absolute exclusion.')],
 [S('A Pattern With Many Genetic and Acquired Mimics','**HSP commonly produces progressive lower-limb pyramidal dysfunction**, with pure and complicated phenotypes. Additional neuropathy, ataxia, cognitive, visual or other features refine the differential.',
    'Review age at onset, progression, pedigree and exposures. Compression, vascular shunts, B12/copper deficiency, HTLV-1 and other causes can mimic parts of the syndrome.',
    'Selected inherited metabolic conditions can also be treatable, so a genetic-looking pattern should not end the search for actionable alternatives.'),
  S('Interpret Molecular Results With the Patient','**Choose genetic testing suited to the phenotype and possible inheritance**, including relevant variant classes. Counseling should precede predictive testing and address the limits of uncertain results.',
    'A variant of uncertain significance is not a definitive cause. Family segregation, phenotype and specialist interpretation may clarify it, while a negative result may reflect current assay limits.',
    'Provide rehabilitation, stretching, mobility and bladder/spasticity care according to function. Do not promise that symptomatic reduction of tone changes the underlying degeneration, and avoid excessive antispastic treatment that worsens useful strength. Reassess abrupt or disproportionate decline for a superimposed process rather than assuming all future disability follows the inherited disorder.')],['HSP','APPROACH','B12','COPPER'])

R.update({
 'TRAUMA':('NICE NG41: spinal injury initial assessment and imaging','https://www.nice.org.uk/guidance/ng41/chapter/Recommendations'),
 'MAP':('AO Spine/Praxis acute SCI hemodynamic guideline, 2024','https://doi.org/10.1177/21925682231202348'),
})

add('Acute cord injury and secondary complications','Neurologic Deficit Despite a Nondiagnostic Trauma CT',
 'After a fall, an adult has objective limb weakness and sensory abnormalities suggesting cervical cord injury. CT shows no fracture explaining the deficit. Which next step is appropriate?',
 'Maintain appropriate spinal precautions and obtain MRI with urgent specialist assessment',[
 ('Clear the spine solely because CT shows no explanatory fracture','CT assesses bone well but cannot exclude every cord, disc or ligament injury; persistent attributable neurologic deficits require further evaluation.'),
 ('Begin unrestricted mobilization and arrange outpatient EMG','Electrodiagnostics can answer later peripheral questions, but are not the immediate substitute for assessing a possible acute cord/soft-tissue injury.'),
 ('Wait for brisk reflexes before further spinal investigation','Acute cord dysfunction can initially be hypotonic and areflexic, so waiting for later long-tract signs can delay appropriate imaging and care.')],
 [S('Resuscitation and Protection Come First','**Manage airway, breathing and circulation with appropriate spinal alignment/protection.** Identify respiratory risk in high lesions and look for associated trauma and bleeding.',
    'Document motor and sensory findings, including sacral function when feasible, and repeat assessment after stabilization. Sedation, pain and other injuries can limit the first examination.',
    'Avoid hypotension and hypoxemia while arranging imaging and specialist review; diagnostic uncertainty does not justify unprotected handling of a potentially unstable injury.'),
  S('CT and MRI Answer Different Questions','**NICE NG41 recommends MRI after CT when a neurologic abnormality could be attributable to cord injury**, regardless of whether CT demonstrates it.',
    'MRI evaluates the cord, discs, ligaments and soft tissues and can clarify the compressive or intrinsic injury mechanism. A normal bony study is not a complete neurologic clearance.',
    'Coordinate trauma/spine services and definitive management according to anatomy, instability and overall condition. Do not delay essential resuscitation for a scan, but do not defer indicated MRI to a routine outpatient pathway either. Early specialist decisions and serial examination guide prognosis more reliably than one initial image or reflex sign.')],['TRAUMA','ACR','ENLS'])

add('Acute cord injury and secondary complications','Spinal Shock and Neurogenic Shock Are Different',
 'A patient with acute high thoracic trauma is hypotensive and bradycardic with flaccid areflexic legs. Which statement best distinguishes the relevant terms?',
 'Spinal shock describes depressed reflex activity; neurogenic shock describes hemodynamic failure from sympathetic disruption',[
 ('Spinal shock and neurogenic shock are interchangeable names for hypotension','They address different neurologic and circulatory consequences; the same patient may have both, but one term cannot replace assessment of the other.'),
 ('Areflexia establishes neurogenic shock as the cause of hypotension','Areflexia can accompany acute cord dysfunction but does not determine circulatory etiology; hemorrhage and other shock causes still require investigation.'),
 ('Bradycardia excludes concurrent traumatic hemorrhage','Relative bradycardia can support sympathetic disruption in context, but does not safely rule out bleeding or mixed shock in an injured patient.')],
 [S('Separate the Neurologic Examination From Perfusion','**Spinal shock is an acute depression of reflex and motor activity below a lesion.** It can temporarily mask later upper-motor-neuron signs.',
    'Neurogenic shock involves loss of sympathetic vascular support, commonly after cervical or high thoracic injury, with hypotension and often relative bradycardia.',
    'The neurologic and hemodynamic syndromes can coexist, but their presence and treatment must be assessed separately.'),
  S('Exclude More Than One Cause of Shock','**Trauma hypotension requires active assessment for hemorrhage and other threats.** A convincing cord lesion does not make blood loss impossible.',
    'Use the resuscitation context, examination, imaging and response to treatment to guide fluid, blood-product and vasopressor decisions. Avoid indiscriminate volume loading when vasodilation or cardiac factors dominate.',
    'Provide close hemodynamic and respiratory monitoring and specialist care. Assess perfusion targets individually under contemporary SCI guidance rather than equating a normal pulse rate with adequate cord blood flow. Serial neurologic examination helps characterize recovery from reflex suppression, while circulatory stabilization limits secondary injury; neither process guarantees complete neurologic recovery.')],['TRAUMA','MAP','ENLS'],style='direct')

add('Acute cord injury and secondary complications','Contemporary MAP Augmentation Guidance',
 'Which statement best reflects the 2024 AO Spine/Praxis hemodynamic guideline for acute traumatic spinal cord injury?',
 'Consider MAP augmentation with a lower limit around 75–80 mmHg and an upper active-augmentation limit around 90–95 mmHg for 3–7 days',[
 ('Maintain exactly 85–90 mmHg for exactly seven days as a high-certainty universal requirement','That narrow target reflects older guidance; the updated recommendation permits a broader individualized range and acknowledges very low certainty.'),
 ('Actively raise every patient above 100 mmHg for two weeks','The guideline does not endorse unlimited high-pressure augmentation or this fixed duration; excessive vasopressor exposure can create harm.'),
 ('Lower spontaneous MAP above 95 mmHg in every patient to meet the augmentation limit','The upper limit concerns active augmentation, not an instruction to lower every naturally higher pressure irrespective of the clinical context.')],
 [S('Avoid Hypoperfusion While Recognizing Uncertainty','**The 2024 guidance suggests MAP support for ==3–7 days==**, with a lower augmentation boundary of approximately ==75–80 mmHg== and not actively augmenting beyond about ==90–95 mmHg==.',
    'These are weak recommendations based on very-low-certainty evidence, not a precisely proven optimum for every injury. Clinical severity and associated illness influence the plan.',
    'Avoid or correct systemic hypotension promptly, while identifying bleeding, cardiac dysfunction and other contributors rather than assigning all low pressure to the cord.'),
  S('Individualize the Support and Its Risks','**Use monitored hemodynamic care**, weighing vasopressor-related arrhythmia/ischemia, fluid balance and the broader trauma physiology. One vasopressor is not established as universally superior by this guideline.',
    'The upper range refers to active pressure augmentation. It should not automatically trigger antihypertensive treatment when MAP is spontaneously higher.',
    'MAP is a practical surrogate rather than a direct measurement of every patient’s spinal perfusion. Surgical decompression, oxygen delivery and complication prevention remain important alongside blood-pressure support. Document the rationale, duration and reassessment plan rather than maintaining a pressor target indefinitely because it appeared in an older protocol.')],['MAP','TRAUMA'],style='direct')

R.update({
 'MPSS':('AO Spine guideline on methylprednisolone in acute SCI, 2017','https://pubmed.ncbi.nlm.nih.gov/29164025/'),
 'AD':('Consortium for Spinal Cord Medicine: autonomic dysfunction guideline, 2021','https://pmc.ncbi.nlm.nih.gov/articles/PMC8152175/'),
 'VTE':('Acute SCI anticoagulant thromboprophylaxis guideline, 2017','https://pmc.ncbi.nlm.nih.gov/articles/PMC5684841/'),
})

add('Acute cord injury and secondary complications','Steroids Are Not Universal Traumatic SCI Treatment',
 'An adult presents 12 hours after traumatic spinal cord injury. Which interpretation of methylprednisolone guidance is most accurate?',
 'Do not start a high-dose infusion for neuroprotection; late initiation is not supported',[
 ('Offer a 24-hour infusion using the early-treatment option','The 2017 AO Spine option applies to adults presenting within eight hours; this patient presents after that interval and does not meet that timing condition.'),
 ('Offer a 48-hour infusion to compensate for delayed presentation','The AO Spine guideline suggests against a 48-hour infusion; extending exposure does not establish benefit from late treatment and can add complications.'),
 ('Give the pulse regimen used for an inflammatory myelitis attack','Inflammatory myelitis can warrant high-dose corticosteroids, but traumatic tissue injury is a different mechanism and cannot inherit that indication without evidence.')],
 [S('Recommendations Depend on Mechanism and Timing','**Traumatic SCI is distinct from immune-mediated myelitis and malignant epidural compression.** Corticosteroid recommendations cannot be transferred between these conditions simply because each can cause weakness.',
    'NICE NG41 advises against methylprednisolone for neuroprotection after acute traumatic SCI. The 2017 AO Spine guideline permits a 24-hour infusion as a treatment option within eight hours, rather than a mandatory standard.',
    'That AO Spine recommendation does not support initiating the infusion after eight hours and suggests against a 48-hour course. The 12-hour presentation therefore lies outside its early-treatment option.'),
  S('Discuss Evidence Without Delaying Essential Care','**The timing subgroup and modest potential motor benefit have generated continuing disagreement.** An optional regimen in one guideline is not proof that every injured patient benefits.',
    'Assess infectious, gastrointestinal, metabolic and other complications when discussing corticosteroid exposure. Document the applicable guideline and uncertainty if an early-treatment option is considered.',
    'Prioritize resuscitation, avoidance of hypoxemia/hypotension, indicated decompression and stabilization, and prevention of secondary complications. Steroids do not replace these measures. Reconsider a different steroid indication only if the clinical evaluation establishes a separate condition, rather than prescribing empirically because the neurologic deficit is severe.')],['TRAUMA','MPSS'],style='direct')

add('Acute cord injury and secondary complications','Autonomic Dysreflexia From Bladder Obstruction',
 'A patient with chronic T4 SCI develops headache and facial sweating. BP is 190/110 mmHg, compared with a usual 100/65. The urinary catheter has stopped draining. What is the best immediate approach?',
 'Sit upright, monitor BP closely, address catheter obstruction and use a rapid short-acting antihypertensive as appropriate',[
 ('Lie flat, elevate the legs and give a fluid bolus','These measures can help symptomatic orthostatic hypotension, but this episode is severe hypertension with a likely noxious bladder trigger and can worsen with that approach.'),
 ('Give an oral long-acting antihypertensive and review catheter drainage later','Chronic hypertension can need sustained treatment, but dysreflexia requires rapid assessment and removal of its trigger; a long-acting drug can cause prolonged hypotension after relief.'),
 ('Treat the headache with analgesia and observe the next scheduled BP','Analgesia may be useful for another headache disorder, but severe acute hypertension in this setting needs immediate dysreflexia management and frequent reassessment.')],
 [S('Recognize a Rise From a Low Baseline','**Autonomic dysreflexia occurs particularly with lesions at or above T6.** Bladder distension or obstruction, bowel impaction and skin injury are common triggers below the lesion.',
    'A systolic rise exceeding about 20 mmHg above baseline in an adult can be significant; headache, sweating or flushing may accompany it, but symptoms can be limited.',
    'Sit the patient upright with legs lowered if possible, loosen constrictive items and measure BP/pulse every one to two minutes during the acute episode.'),
  S('Relieve the Trigger While Controlling Dangerous Pressure','**Inspect the urinary drainage system promptly**, correcting a kink or overfilled collection bag and arranging appropriate catheter assessment. Avoid forceful or unnecessarily provocative manipulation.',
    'At systolic BP of 150 mmHg or higher, consider a rapid-onset, short-duration antihypertensive while investigating the trigger. Check recent phosphodiesterase-5 inhibitor exposure before any nitrate because the combination can cause profound hypotension.',
    'If the bladder explanation is inadequate, evaluate bowel and skin causes with appropriate precautions. Continue monitoring after relief because BP can fall rapidly, particularly after medication. Persistent hypertension, neurologic symptoms or uncertainty requires emergency escalation; repeated episodes warrant an individualized prevention plan.')],['AD'])

add('Acute cord injury and secondary complications','Thromboprophylaxis Within a Secondary-Care Plan',
 'An adult with acute traumatic paraplegia remains immobile 48 hours after stabilization. The treating team finds no active bleeding or current procedural contraindication. Which VTE strategy is best supported?',
 'Begin prophylactic LMWH or fixed low-dose UFH promptly, with mechanical measures and reassessment',[
 ('Use mechanical prophylaxis alone until independent walking returns','Mechanical methods are useful when bleeding prevents anticoagulants, but prolonged immobility without a contraindication supports adding pharmacologic prophylaxis rather than waiting for walking.'),
 ('Begin therapeutic-dose anticoagulation to prevent a first thrombosis','Therapeutic dosing is used for established thrombosis or another specific indication; it adds bleeding exposure without being the recommended routine primary-prophylaxis strategy here.'),
 ('Insert a prophylactic vena cava filter instead of anticoagulant prophylaxis','A filter can have selected indications when acute VTE and contraindications coexist, but it is not the routine substitute for feasible prophylactic anticoagulation in this patient.')],
 [S('Balance Thrombosis Against Bleeding','**Acute SCI with immobility creates substantial VTE risk.** The 2017 guideline suggests prophylactic LMWH or fixed low-dose UFH and initiation within 72 hours of injury when possible.',
    'Coordinate timing with surgery, hemostasis, renal function and other injuries. A genuine bleeding contraindication warrants mechanical measures and repeated assessment of when anticoagulants can begin.',
    'Choose the prophylactic dose under the relevant trauma protocol, accounting for renal clearance and patient factors; adjusted therapeutic-dose UFH is not the recommended routine prevention approach.'),
  S('Prevent Disability Beyond the Initial Lesion','**Pair thromboprophylaxis with structured skin, bladder, bowel and rehabilitation care.** Pressure redistribution, skin inspection, safe repositioning and nutrition help prevent pressure injury.',
    'Maintain appropriate bladder drainage and plan longer-term management according to function, urodynamic risk and feasibility. Establish a bowel programme and educate about autonomic dysreflexia in susceptible lesions.',
    'Assess respiratory function, pain, spasticity, mood and practical rehabilitation goals. Reassess prophylaxis duration as mobility and bleeding risk evolve rather than stopping at an arbitrary discharge date. New swelling, unexplained hypoxemia or cardiopulmonary deterioration needs diagnostic evaluation; preventive treatment does not exclude breakthrough thrombosis.')],['VTE','TRAUMA','AD'])

# Editorial revisions: compare realistic competing pathways without giveaway wording.
def revise(title, answer=None, others=None, stem=None, table=None):
    r=next(r for r in rows if r['title']==title)
    if answer is not None:r['answer']=answer
    if others is not None:r['others']=others
    if stem is not None:r['question']=stem
    if table is not None:r['table']=table

revise('Dexamethasone in Neurologic MSCC',
 answer='Dexamethasone 16 mg promptly, then 16 mg daily pending definitive treatment',
 others=[
 ('Dexamethasone 4 mg promptly, then 4 mg daily pending definitive treatment','Lower dexamethasone doses may be used for other symptom-control indications, but 4 mg daily does not match NICE initial treatment for neurologic MSCC.'),
 ('Dexamethasone 96 mg promptly, then 96 mg daily pending definitive treatment','Very high-dose regimens have been studied historically, but NICE recommends 16 mg rather than this substantially greater exposure, with its increased toxicity concerns.'),
 ('Dexamethasone 16 mg once, with further dosing after radiotherapy starts','A prompt initial dose is appropriate, but NICE also recommends continuing 16 mg daily while awaiting definitive treatment; one dose leaves that interval untreated.')])
revise('Epidural Abscess Without the Full Triad',others=[
 ('Vertebral metastatic disease with epidural extension','Malignancy can cause focal pain and epidural compression, but recent S. aureus bacteremia and dialysis particularly raise hematogenous spinal infection requiring urgent investigation.'),
 ('An acute osteoporotic vertebral compression fracture','A fracture can produce focal pain, especially with skeletal fragility, but cannot adequately account for the bacteremia-associated inflammatory context without excluding infection.'),
 ('Thoracic disc herniation with an evolving myelopathy','A disc lesion can cause focal pain and later weakness, but the infection risk and inflammatory findings make an infectious epidural process the priority to exclude.')])
revise('Epidural Infection With Progressive Weakness',others=[
 ('Obtain percutaneous biopsy before starting antibiotics, then reassess surgical need','A stable patient without neurologic compromise may undergo microbiologic sampling before empiric therapy; sepsis and progressive deficits require prompt antimicrobial and surgical action.'),
 ('Start intravenous antibiotics and assess response before arranging surgical consultation','Antibiotic-only care can be selected for carefully monitored patients without an urgent operative indication, but progressive cord compression needs immediate surgical assessment.'),
 ('Drain the paraspinal component percutaneously and continue culture-directed antibiotics','Percutaneous drainage can control selected accessible collections, but a compressive epidural lesion with worsening weakness requires direct assessment of neural decompression and source control.')])
revise('Progressive Degenerative Cervical Myelopathy',others=[
 ('Offer supervised rehabilitation first, with surgery if neurologic deterioration develops','A supervised rehabilitation trial can be considered in selected mild DCM, but this patient already has progressive moderate disease, for which surgical assessment is recommended.'),
 ('Observe with serial examinations because the symptoms are not yet severely disabling','Observation may be appropriate for selected nonmyelopathic compression or carefully selected mild disease; progressive moderate myelopathy should not wait for severe dependence.'),
 ('Treat the radicular component with an epidural injection before reassessing gait','Selected radicular pain may respond to an injection, but treating pain does not address progressive cord dysfunction or replace decompression assessment.')],table=(['DCM category','mJOA score','Management framework'],[
 ['Mild','15–17','Surgery or supervised rehabilitation in selected patients; operate for deterioration'],
 ['Moderate','12–14','Recommend surgical intervention after appropriate assessment'],
 ['Severe','11 or less','Recommend surgical intervention after appropriate assessment']]))
revise('Treat the Cause of a Syrinx',others=[
 ('Primary syrinx shunting before addressing the craniocervical CSF-flow obstruction','A syrinx shunt has selected roles in persistent or otherwise unsuitable cases, but the associated Chiari and flow obstruction should guide the initial cause-directed surgical strategy.'),
 ('Serial MRI surveillance with symptom-directed treatment','Observation can suit stable or incidental cavities, but enlargement and objective progressive weakness warrant neurosurgical reassessment of the cause and treatment.'),
 ('Obtain CSF oligoclonal bands and begin a demyelinating treatment pathway','CSF testing can help an independently suspected inflammatory disorder, but a cavity with Chiari and progression does not itself establish immune-mediated myelitis.')])
revise('Incomplete Cauda Equina Syndrome',others=[
 ('Pain-associated urinary hesitation with lumbar radiculopathy','Severe pain can impair voiding, but new perineal sensory loss and altered bladder awareness require exclusion of CES before attributing the urinary symptoms to pain.'),
 ('CES with established painless urinary retention','Retention-stage CES entails loss of executive bladder control, often with painless retention and overflow; retained voluntary voiding fits an incomplete stage more closely.'),
 ('Medication-associated urinary retention accompanying sciatica','Opioids and anticholinergic drugs can cause retention, but they do not safely explain new saddle sensory changes; medication review must accompany urgent spinal assessment.')])
revise('A Low PVR Does Not Exclude CES',others=[
 ('Arrange expedited outpatient MRI because the residual suggests preserved emptying','Preserved emptying can lower concern in an otherwise reassuring evaluation, but a low residual cannot exclude incomplete CES when new saddle and urinary-awareness abnormalities are present.'),
 ('Repeat the bladder scan after analgesia before deciding on MRI','Repeat measurement may clarify pain- or medicine-related retention, but should not gate urgent imaging when the neurologic history remains suspicious for CES.'),
 ('Prioritize urologic testing for detrusor dysfunction before spinal imaging','Urologic assessment can help persistent bladder dysfunction after appropriate evaluation, but acute saddle sensory change requires exclusion of compressive spinal disease first.')])
revise('Urgent MRI and Decompression Assessment',others=[
 ('Use an epidural injection and reassess motor and bladder function','An injection can help selected uncomplicated radicular pain, but MRI-confirmed cauda compression with evolving sphincter and motor deficits needs a decompression decision.'),
 ('Begin a supervised conservative disc programme with frequent outpatient reviews','Conservative treatment is appropriate for many disc prolapses without CES; this combination of neurologic decline and compression requires urgent surgical assessment.'),
 ('Schedule decompression after completion of elective prehabilitation','Prehabilitation can benefit elective spine surgery, but should not delay emergency evaluation of progressive cauda equina dysfunction with an established compressive target.')])
revise('Conus and Cauda Patterns Overlap',others=[
 ('Predominantly cauda equina root compression','Cauda disease can cause saddle loss and sphincter dysfunction, but often has radicular pain, asymmetric lower-motor-neuron findings and reduced reflexes; mixed signs and symmetry suggest conus involvement.'),
 ('A higher thoracic cord lesion sparing the conus','Thoracic lesions can cause bilateral weakness and sphincter dysfunction, but preferential saddle symptoms with mixed sacral-root and long-tract signs direct attention toward the conus region.'),
 ('Bilateral lumbosacral plexus involvement','Plexopathy can cause painful weakness and reduced reflexes, but the early sacral autonomic pattern with brisk knee responses is less consistent with a purely peripheral plexus localization.')])
revise('After MRI Excludes Cauda Compression',others=[
 ('Arrange exploratory lumbar decompression on the clinical history','Surgery can treat a demonstrated compressive lesion, but without a corresponding target its harms are not justified; reassessment should seek another mechanism or missed localization.'),
 ('Assign a functional diagnosis from the negative scan and begin that pathway','Functional symptoms can coexist with pain and bladder disturbance, but diagnosis requires positive clinical assessment and exclusion of relevant alternatives rather than a negative scan alone.'),
 ('Treat as established neurogenic bladder from CES and end etiologic evaluation','Bladder protection and urology assessment may be needed, but the initial symptoms do not establish a compressive CES etiology after adequate negative imaging.')])
revise('Acute Spinal Cord Infarction',others=[
 ('Acute inflammatory transverse myelitis','Inflammatory disease can cause severe bilateral myelopathy, but an abrupt deficit during systemic hypotension with relative dorsal-column preservation more strongly supports ischemia.'),
 ('Spinal dural arteriovenous fistula with venous congestion','A fistula can cause a vascular myelopathy and occasional abrupt decline, but usually produces a progressive or fluctuating course with venous imaging clues rather than this acute low-flow syndrome.'),
 ('Intramedullary hemorrhage','Hemorrhage can cause hyperacute myelopathy, particularly with a vascular malformation or coagulopathy; blood-sensitive MRI and the clinical context distinguish it from a hypotension-related infarct.')])

revise('Early Negative MRI in Suspected Infarction',others=[
 ('Perform electrodiagnostics next and defer repeat cord imaging','Electrodiagnostics help peripheral or root localization, but an abrupt clinically convincing cord syndrome can precede visible ischemic MRI changes and needs directed reassessment.'),
 ('Begin immune treatment after interpreting the negative scan as early myelitis','Early inflammatory lesions may also be subtle, but a negative scan does not establish inflammation; the abrupt vascular context requires continued ischemic evaluation.'),
 ('Obtain CSF first and use its protein level to decide whether repeat MRI is needed','CSF may help the differential after safe assessment, but isolated protein is nonspecific and should not determine whether a clinically suspected infarct receives repeat imaging.')])
revise('Delayed Weakness After Aortic Repair',others=[
 ('Begin high-dose methylprednisolone for postoperative inflammatory cord edema','Immune-mediated myelitis can warrant steroid treatment, but postoperative hypotension-associated weakness requires urgent correction of perfusion threats rather than assuming inflammation.'),
 ('Maintain the current pressure target and obtain elective rehabilitation assessment','Rehabilitation is important after injury, but a new deficit after aortic repair may respond to urgent perfusion rescue and cannot await an elective pathway.'),
 ('Use anticoagulant thrombolysis under the standard cerebral-stroke protocol','Selected cerebral infarcts may be eligible for thrombolysis, but recent major aortic surgery and suspected spinal hypoperfusion require a different specialist evaluation and rescue strategy.')])
revise('When a Negative Angiogram Needs Review',others=[
 ('Accept the angiogram and proceed to an inflammatory-myelitis treatment pathway','An adequately performed negative study can change the differential, but omitted relevant territories limit exclusion of a fistula despite this suspicious MRI.'),
 ('Use repeat contrast MRI as the definitive test to exclude a shunt','MRI can strengthen or weaken suspicion and guide angiography, but cannot reliably exclude every fistula or replace completion of a technically incomplete catheter study.'),
 ('Obtain spinal cord tissue to distinguish congestion from inflammation','Biopsy has selected roles in unresolved infiltrative disease, but suspected vascular congestion with incomplete angiography should prompt expert vascular assessment before invasive cord sampling.')])
revise('Steroid Worsening as a Vascular Warning',others=[
 ('Escalate directly to apheresis for presumed steroid-refractory immune myelitis','Apheresis is appropriate for a well-supported severe inflammatory attack with inadequate response, but the chronic course and perimedullary vessels require reassessing a vascular shunt first.'),
 ('Proceed to cord biopsy for suspected infiltrative malignancy','Biopsy can help selected unresolved neoplastic lesions, but a vascular explanation should be investigated before sampling a cord with congestive imaging clues.'),
 ('Continue the planned steroid course and assess response with interval MRI','Interval monitoring can suit established inflammatory disease, but acute worsening with flow voids calls for urgent reconsideration rather than completing treatment on the original assumption.')])
revise('Establishing an Inflammatory Myelopathy',others=[
 ('Classify as idiopathic transverse myelitis after excluding compression','Idiopathic inflammatory myelitis is a diagnosis reached after relevant etiologic exclusions; excluding compression alone leaves infection, vascular, metabolic and specific immune causes unresolved.'),
 ('Classify as antibody-associated disease from lesion length and axial position','Lesion morphology helps select tests, but does not replace appropriate antibody testing and clinical criteria or exclude important mimics.'),
 ('Classify as MS-related disease from CSF oligoclonal bands','CSF-restricted bands can support MS in the right clinical and MRI setting, but are not specific enough to assign MS from an isolated cord syndrome without that assessment.')])
revise('LETM Is a Pattern, Not One Diagnosis',others=[
 ('Classify provisionally as AQP4-associated NMOSD from the longitudinal pattern','Longitudinally extensive lesions are characteristic of NMOSD, but the pattern occurs in other disorders; appropriate antibody, clinical and exclusion criteria are required.'),
 ('Classify provisionally as MOG-associated disease from central axial involvement','Central gray-matter involvement may support MOGAD in context, but is not diagnostic without the clinical and serologic framework and exclusion of alternatives.'),
 ('Classify provisionally as neurosarcoidosis from the segment count','Sarcoidosis can cause long lesions, especially with characteristic enhancement and systemic findings, but lesion length alone does not establish granulomatous disease.')])
revise('Early Apheresis in a Severe Inflammatory Attack',stem='A patient with established AQP4-IgG-positive NMOSD has a severe myelitis attack and remains markedly paraparetic despite initial high-dose IV methylprednisolone. Compression and important infectious mimics have been addressed. Which treatment should be considered promptly?',others=[
 ('Begin azathioprine as the main intervention for the current deficit','Azathioprine can be a relapse-prevention option in selected NMOSD settings, but its delayed immunosuppressive effect does not replace timely rescue of a severe acute attack.'),
 ('Start a maintenance biologic and assess the deficit at its next dosing visit','Targeted biologics can prevent subsequent NMOSD attacks, but prevention scheduling is not a substitute for acute apheresis escalation in a disabling poorly responsive attack.'),
 ('Complete an oral steroid taper before deciding whether to use apheresis','A taper can follow acute treatment, but waiting through it can delay rescue; severe attacks with insufficient response warrant prompt consideration of apheresis.')])
revise('Tissue Strategy in Suspected Neurosarcoidosis',others=[
 ('Use the cord enhancement and systemic imaging to assign definite disease','Imaging can strongly support sarcoidosis and identify biopsy targets, but definite neurosarcoidosis requires neural tissue evidence within the appropriate exclusion framework.'),
 ('Measure serum ACE and reserve biopsy for an elevated result','ACE can contribute to assessment but has insufficient sensitivity and specificity to gate tissue diagnosis or exclude competing infection and malignancy.'),
 ('Biopsy the enhancing spinal cord lesion as the initial tissue target','Neural biopsy can establish definite disease when necessary, but an accessible extraneural target can establish systemic pathology with less neurologic risk and support probable neurosarcoidosis.')])
revise('Negative First CSF Cytology in Suspected Cancer Involvement',others=[
 ('Observe with interval imaging before obtaining another CSF specimen','Surveillance may suit low-suspicion uncertain findings, but this clinical and imaging pattern warrants an optimized repeat sample because one negative cytology does not exclude disease.'),
 ('Prioritize a paraneoplastic antibody panel as the confirmatory investigation','Paraneoplastic immune syndromes are relevant cancer-associated mimics, but an antibody result does not replace evaluation of suspected direct leptomeningeal involvement.'),
 ('Biopsy the spinal leptomeninges before attempting another CSF collection','Biopsy can help selected unresolved cases, but a repeat optimized CSF examination is generally recommended after an initial negative or equivocal cytology when suspicion persists.')])
revise('Nonresponse Should Reopen the Differential',others=[
 ('Escalate to maintenance cyclophosphamide for treatment-resistant idiopathic myelitis','Potent immune escalation can be appropriate in selected confirmed inflammatory disorders, but the chronic discordant trajectory first requires reassessment of the diagnosis and mimics.'),
 ('Use repeat CSF protein measurements to determine the next immunotherapy','CSF trends can contribute to selected inflammatory assessments, but protein alone is nonspecific and cannot resolve whether this progressive syndrome is inflammatory.'),
 ('Proceed to spinal cord biopsy before reviewing prior imaging and vascular studies','Biopsy can answer selected persistent infiltrative questions, but careful reassessment of localization and less invasive diagnostic evidence should precede such a high-risk step.')])
revise('Nitrous Oxide and Functional B12 Deficiency',others=[
 ('Repeat total B12 after stopping supplementation and await the result','Total B12 can support other deficiency assessments, but nitrous oxide can impair functional activity despite a normal concentration and treatment should not wait for a washout.'),
 ('Measure serum folate as the principal marker of nitrous-induced cord injury','Folate status can affect homocysteine and anemia, but it does not directly assess the B12-dependent functional disturbance underlying nitrous-associated myeloneuropathy.'),
 ('Measure serum copper as the principal marker of nitrous-induced cord injury','Copper testing is valuable for a similar posterior-column syndrome, particularly after gastric surgery or zinc exposure, but does not address the nitrous-specific B12 mechanism.')])
revise('Copper Deficiency After Gastric Surgery',others=[
 ('Serum MMA, homocysteine and total B12','These help assess B12-related dysfunction and remain relevant if replacement adequacy is uncertain, but gastric surgery, zinc exposure and cytopenias specifically warrant copper assessment.'),
 ('Serum vitamin E and a fasting lipid profile','Vitamin E deficiency can cause ataxia and neuropathy in malabsorption, but the combined pyramidal/posterior-column syndrome with anemia and neutropenia particularly supports copper deficiency.'),
 ('Plasma very-long-chain fatty acids and adrenal function','These can investigate adrenomyeloneuropathy in an appropriate phenotype, but do not best explain the acquired gastric-surgery/zinc context with cytopenias.')],table=(['Cause','Useful clues','Targeted evaluation'],[
 ['B12 dysfunction','Posterior-column and pyramidal signs; anemia may be absent','B12 plus MMA/homocysteine as appropriate; interpret renal/folate confounding'],
 ['Nitrous oxide','Exposure; normal total B12 does not exclude functional injury','MMA or homocysteine; exposure history; stop use and treat'],
 ['Copper deficiency','Gastric surgery, zinc excess, anemia/neutropenia','Copper, ceruloplasmin and zinc; assess associated deficiencies']]))
revise('HTLV-1-Associated Spastic Paraparesis',others=[
 ('AQP4-IgG testing as the leading etiologic investigation','AQP4 testing is appropriate for a compatible inflammatory attack, but a chronic progressive exposure-associated spastic paraparesis with early bladder symptoms particularly warrants HTLV-1 evaluation.'),
 ('A hereditary spastic paraplegia panel as the leading etiologic investigation','Genetic testing can help a familial or otherwise suggestive chronic pyramidal syndrome, but an actionable infectious exposure should be assessed before assigning an inherited cause.'),
 ('CSF oligoclonal bands as the leading etiologic investigation','Bands can contribute to selected inflammatory evaluations but do not specifically diagnose the exposure-associated syndrome and cannot replace confirmatory HTLV-1 assessment.')])
revise('Spinal Tuberculosis With Neurologic Deterioration',others=[
 ('Begin empiric TB therapy and defer surgical assessment until the microbiology returns','Empiric treatment may be needed when suspicion is high, but progressive weakness and destructive disease require urgent assessment of compression and stability while tests proceed.'),
 ('Arrange elective biopsy and use analgesia until susceptibility results return','Tissue and susceptibility data are important, but an elective diagnostic sequence is unsuitable when neurologic deterioration may reflect an urgent mechanical threat.'),
 ('Plan abscess aspiration followed by antibiotics without stability assessment','Aspiration can aid diagnosis or drainage in selected cases, but does not alone resolve vertebral instability or the need to decompress threatened neural structures.')])
revise('Before Labeling Hereditary Spastic Paraplegia',others=[
 ('Test the most likely single HSP gene and end investigation if negative','Single-gene testing can be efficient for a known familial variant or strong specific phenotype, but heterogeneous HSP and acquired mimics require a broader context-dependent strategy here.'),
 ('Obtain a broad genetic panel before any assessment for acquired causes','Broad testing can assist molecular diagnosis, but it should not postpone clinically indicated imaging or evaluation of treatable acquired conditions that can mimic familial spasticity.'),
 ('Use clinical pedigree classification and reserve molecular testing for affected children','Clinical assessment is essential, but adult molecular diagnosis can inform counseling and management; testing should be chosen for the proband rather than deferred solely by age.')])

revise('Acute Areflexia Does Not Exclude Cord Injury',others=[
 ('An acute inflammatory polyradiculoneuropathy is the leading localization','GBS can cause areflexic paralysis and autonomic dysfunction, but sudden back pain, a clear sensory level and early retention prioritize a cord lesion despite absent reflexes.'),
 ('A cauda equina root lesion is the leading localization','Acute root compression can cause areflexia and retention, but a clear trunk sensory level favors cord involvement; areflexia alone cannot distinguish them.'),
 ('A bilateral lumbosacral plexopathy is the leading localization','Plexus disease can cause painful lower-motor-neuron weakness, but a sudden bilateral syndrome with a clear sensory level and retention requires urgent central structural assessment.')])
revise('MRI When Spinal Infection Is Suspected',others=[
 ('Urgent contrast-enhanced CT of the symptomatic spinal region','CT is useful for bone and selected alternative pathways when MRI cannot be performed, but feasible MRI better assesses epidural extent and neural compression.'),
 ('Urgent CT myelography of the symptomatic spinal region','CT myelography can answer selected canal questions when MRI is unsuitable, but is invasive and is not preferred over available MRI in suspected epidural infection.'),
 ('Urgent FDG-PET/CT to define the infectious focus','PET/CT can help selected occult or multifocal infection assessments, but does not replace the immediate MRI assessment of a threatened cord.')])
revise('A Lumbar Finding That Does Not Explain the Examination',others=[
 ('Obtain lumbar flexion-extension radiographs to assess dynamic stenosis','Dynamic lumbar studies can address selected instability questions, but do not explain the trunk sensory level or pyramidal signs and should not displace cord imaging.'),
 ('Obtain lower-limb EMG/NCS to characterize multilevel radiculopathy','Electrodiagnostics can define coexisting peripheral disease, but cannot adequately evaluate a cervical or thoracic lesion suggested by this examination.'),
 ('Obtain CT of the lumbar canal to refine operative planning','CT can clarify bony anatomy when lumbar surgery is contemplated, but refining an incidental lumbar finding does not resolve the discordant clinical localization.')])
revise('Lumbar Puncture After Structural Assessment',others=[
 ('Check INR and proceed if it is within the laboratory reference range','INR helps assess vitamin-K-antagonist effects and selected coagulation disorders, but cannot reliably exclude relevant apixaban activity after a morning dose.'),
 ('Omit the next apixaban dose and perform LP later the same afternoon','A brief omission may be inadequate; procedural timing depends on the drug, dose, clearance and relevant guidance rather than a single missed dose.'),
 ('Replace apixaban with therapeutic heparin and proceed with LP','Bridging is appropriate only in selected thrombotic situations and introduces its own bleeding and timing requirements; it does not automatically make immediate LP safe.')])
revise('Recognize Metastatic Cord Compression Early',others=[
 ('Arrange expedited outpatient cancer staging and review the spine with the results','Staging is important for cancer planning, but new weakness and walking difficulty require an immediate compression pathway rather than waiting for staging.'),
 ('Arrange a mechanical-back-pain pathway with supervised exercise and analgesia','That pathway can suit uncomplicated mechanical pain, but cancer history and evolving neurologic findings require urgent assessment of compression and stability.'),
 ('Arrange a radiculopathy pathway with selective root imaging and pain treatment','Root-focused care can suit isolated radicular symptoms, but this progressive gait and weakness presentation requires broader urgent assessment for cord compression.')])
revise('MRI Timing in Suspected MSCC',others=[
 ('MRI within one week, including whole-spine sagittal and targeted axial images','A one-week MRI standard applies to suspected spinal metastases without suspicion of MSCC; neurologic compression features require imaging as soon as possible within 24 hours.'),
 ('MRI within 24 hours, limited to the painful vertebral region','The urgency is appropriate, but pain location can miss noncontiguous lesions; NICE recommends whole-spine sagittal assessment with supplementary axial images through abnormalities.'),
 ('MRI within 72 hours, including whole-spine sagittal and targeted axial images','Broader coverage is appropriate, but a 72-hour schedule exceeds the NICE emergency imaging standard for suspected MSCC with neurologic findings.')])
revise('Acute Spinal Epidural Hematoma',others=[
 ('Obtain brain CT/angiography and prioritize a cerebral-stroke treatment pathway','Acute weakness can trigger stroke assessment, but severe cervical pain with rapidly progressive limb findings and anticoagulation requires urgent spinal evaluation for hemorrhagic compression.'),
 ('Obtain spinal MRI and begin an inflammatory-myelitis steroid pathway','MRI is essential, but a potential anticoagulant-associated compressive hematoma needs urgent surgical and hemostatic assessment rather than presuming inflammation.'),
 ('Withhold anticoagulation and observe neurologic recovery before imaging','Conservative monitoring can be selected after specialist evaluation in some stable or improving cases, but rapid progression requires emergency imaging and a decompression/reversal decision.')])
revise('HIV-Associated Vacuolar Myelopathy Is an Exclusion Diagnosis',others=[
 ('Use cord atrophy on MRI as the confirmatory finding','Atrophy can support chronic cord disease but is nonspecific; it does not exclude infections, nutritional disease or other treatable mechanisms in advanced HIV.'),
 ('Use plasma CMV serology as the confirmatory investigation','Seropositivity indicates exposure and does not establish CMV polyradiculomyelitis; a compatible syndrome and targeted CSF assessment are needed when that diagnosis is suspected.'),
 ('Use improvement after ART initiation as the etiologic diagnostic test','ART is essential HIV care and may influence neurologic outcomes, but waiting for a response cannot substitute for excluding urgent or treatable competing causes.')])
revise('Neurologic Deficit Despite a Nondiagnostic Trauma CT',others=[
 ('Obtain flexion-extension radiographs to exclude dynamic instability','Such studies address selected later stability questions, but acute attributable neurologic deficits after CT require MRI and specialist assessment rather than provocative clearance testing.'),
 ('Obtain CT myelography as the initial soft-tissue investigation','Myelography can be considered when MRI cannot be performed under specialist guidance, but does not take priority over feasible MRI for acute cord and ligament assessment.'),
 ('Arrange early EMG/NCS to distinguish cord from peripheral trauma','Electrodiagnostics may clarify associated peripheral injury later, but cannot replace urgent cord and soft-tissue imaging in this acute trauma presentation.')])
revise('Spinal Shock and Neurogenic Shock Are Different',others=[
 ('Spinal shock describes circulatory failure; neurogenic shock describes depressed reflexes','Both phenomena can follow severe cord injury, but this option reverses their accepted meanings and would misdirect neurologic versus circulatory assessment.'),
 ('Spinal shock requires bradycardia; neurogenic shock requires loss of sacral reflexes','Bradycardia can accompany sympathetic disruption and sacral reflex changes can accompany spinal shock, but these are assigned to the wrong syndromes and are not universal requirements.'),
 ('Spinal shock is a root-level syndrome; neurogenic shock is a long-tract syndrome','Root and long-tract localization helps neurologic diagnosis, but the shock terms distinguish depressed spinal reflex activity from circulatory sympathetic failure rather than these anatomical categories.')],table=(['Term','Main domain','Key implication'],[
 ['Spinal shock','Transiently depressed motor/reflex activity below injury','Initial areflexia does not exclude a cord lesion'],
 ['Neurogenic shock','Hypotension from sympathetic disruption, often relative bradycardia','Assess perfusion and exclude hemorrhage or mixed shock']]))
revise('Contemporary MAP Augmentation Guidance',answer='Consider a lower augmentation limit of 75–80 mmHg and an upper limit of 90–95 mmHg for 3–7 days',others=[
 ('Consider a lower augmentation limit of 85 mmHg and an upper limit of 90 mmHg for seven days','The narrow 85–90 mmHg target reflects older guidance; the 2024 update suggests broader boundaries and a three-to-seven-day duration with very-low-certainty evidence.'),
 ('Consider a lower augmentation limit of 65 mmHg and an upper limit of 70 mmHg for 3–7 days','MAP around 65 mmHg is used in some other shock contexts, but the SCI-specific guideline suggests a higher lower boundary to reduce spinal hypoperfusion risk.'),
 ('Consider a lower augmentation limit of 95 mmHg and an upper limit of 100 mmHg for 3–7 days','The 2024 recommendation does not support this higher active-augmentation range; extra pressor exposure may add harm without a proven neurologic advantage.')])

if __name__=='__main__':
    coverage=ROOT/'Neurology/11. Spinal Cord Disorders, Myelopathy & Cauda Equina Syndromes.coverage.json'
    c=json.loads(coverage.read_text(encoding='utf-8'))
    assert len(rows)==sum(s['questions'] for s in c['sections'])==c['plannedQuestions'],'Chapter incomplete; do not install'
    index=0
    for section in c['sections']:
        for decision in section['decisions']:
            assert rows[index]['topic']==section['section']
            rows[index]['coverageDecision']=decision
            index+=1
    save('Neurology',11,c['chapter'],rows,R,'Original postgraduate synthesis with source-based review. Full Harrison subscription text was not accessed; no independent clinician review is claimed.')
    c.update(status='authored_validated',authoredQuestions=len(rows))
    c['questionDecisions']=[dict(question=i+1,title=r['title'],decision=r['coverageDecision']) for i,r in enumerate(rows)]
    coverage.write_text(json.dumps(c,ensure_ascii=False,indent=2),encoding='utf-8')
