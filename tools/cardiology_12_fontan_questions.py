"""Fontan physiological decisions; expanded sequentially."""
from qbank_json_chapters import question as Q
REFERENCES={
 'FONTAN_PH':('AHA scientific statement: pulmonary hypertension in congenital heart disease, 2023','https://doi.org/10.1161/HHF.0000000000000080'),
 'FONTAN_STRESS':('Fontan pressure-flow profiling during stress and vasodilation, 2025','https://doi.org/10.1152/ajpheart.00105.2025'),
 'AAT_CLEARANCE':('Mayo Clinic Laboratories: alpha-1-antitrypsin clearance, feces and serum','https://www.mayocliniclabs.com/api/sitecore/TestCatalog/DownloadTestCatalog?testId=604982'),
 'FONTAN_KOREA':('Korean Fontan clinical practice consensus, 2025','https://doi.org/10.4070/kcj.2025.0455'),
}
TOPIC='Fontan and single-ventricle circulation'
def S(heading,lead,*details):return heading,[(lead,list(details))]
rows=[Q(TOPIC,'Pulmonary Flow and Preload Limitation in Fontan Circulation',
 'An adult with an extracardiac Fontan has worsening exercise intolerance despite preserved systemic ventricular ejection fraction and no important AV-valve regurgitation. The conduit and branch pulmonary arteries are unobstructed. Pulmonary vascular resistance has increased, while ventricular filling pressure is unchanged. Which mechanism most directly reduces systemic output?',
 'Reduced passive pulmonary flow limits systemic ventricular preload',[
 ('Increased pulmonary resistance directly increases systemic ventricular systolic afterload','Systemic arterial resistance and outflow obstruction directly determine systemic ventricular ejection load. Pulmonary resistance lies upstream of ventricular filling in a Fontan circulation and primarily limits delivery of preload, although the entire circulation remains coupled.'),
 ('Reduced ventricular compliance impairs filling at an elevated diastolic pressure','Diastolic dysfunction can reduce Fontan output by increasing downstream filling pressure and reducing the transpulmonary driving gradient. Here filling pressure is unchanged and the identified change is higher pulmonary vascular resistance, which limits upstream delivery of preload.'),
 ('Reduced sinus-node responsiveness limits augmentation of cardiac output','Sinus-node dysfunction and chronotropic limitation can reduce exercise output after Fontan surgery. No abnormal heart-rate response is supplied, whereas the rise in pulmonary resistance directly explains restricted filling despite a preserved ejection fraction.')],
 [('Pressure-Flow Relationship',[
  ('**The Fontan pathway connects systemic venous return to the pulmonary arteries without an intervening ventricle.** Flow through the lungs depends on a limited upstream-to-downstream pressure gradient and low resistance.',[
   'Conceptually, pulmonary flow depends on the difference between Fontan and pulmonary venous pressures divided by pulmonary vascular resistance. Increased resistance can reduce flow or require a higher upstream venous pressure to sustain it.',
   'The resulting reduction in pulmonary venous return limits systemic ventricular end-diastolic volume and stroke volume. A normal ejection fraction therefore does not establish normal cardiac output or exclude Fontan circulatory failure.'])]),
  ('Clinical Assessment and Treatment Implications',[
  ('**Assess the entire circuit when exercise capacity declines.** Ventricular systolic performance is only one component of the evaluation.',[
   'Look for pathway or branch-artery obstruction, elevated ventricular filling pressure, AV-valve regurgitation, arrhythmia, collateral flow and pulmonary vascular limitation. Catheter assessment can define pressures and flow when noninvasive studies do not explain deterioration.',
   'Venous congestion and inadequate ventricular filling may coexist. Diuresis can relieve congestion but excessive volume removal can further reduce output; treatment requires attention to the individual pressure and flow profile.',
   'Pulmonary vasodilators may improve exercise performance in selected patients without elevated ventricular end-diastolic pressure, but heterogeneous trial results do not support treating every Fontan patient identically. A mechanical pathway stenosis requires its own assessment rather than an assumption that vasodilator treatment will correct it. Exercise evaluation and serial clinical measurements help detect physiological deterioration that resting systolic imaging can miss.'])])],
 ['ACHD2025','FONTAN_PH','FONTAN_STRESS'])]

rows.append(Q(TOPIC,'Confirming Protein-Losing Enteropathy After Fontan Palliation',
 'A 27-year-old with Fontan circulation develops edema, loose stools and serum albumin 2.1 g/dL. Urinary protein excretion is 120 mg/day, INR is 1.1 without anticoagulation, and there is no gastrointestinal bleeding. Which test most directly establishes excessive intestinal protein loss?',
 'Timed fecal alpha-1-antitrypsin clearance with a contemporaneous serum level',[
 ('Fecal calprotectin concentration','Calprotectin assesses intestinal inflammation and can support investigation of inflammatory bowel disease. It does not quantify plasma protein clearance into the intestine, which is the immediate diagnostic question in this Fontan patient.'),
 ('Fecal pancreatic elastase concentration','Elastase helps evaluate exocrine pancreatic insufficiency in a patient with maldigestion or steatorrhea. A low result can also be misleading in watery stool; it does not directly establish enteric plasma protein loss.'),
 ('Quantitative fecal fat excretion','Fecal fat can document fat malabsorption and may assist a broader nutritional assessment. It measures loss of fat rather than plasma proteins, so it cannot directly confirm the suspected protein-losing enteropathy.')],
 [('Mechanism and Differential Diagnosis',[
  ('**Fontan-associated protein-losing enteropathy reflects intestinal protein leakage in a circulation with abnormal venous and lymphatic pressures.** Edema and hypoalbuminemia are typical, but diarrhea is not obligatory.',[
   'Assess renal protein loss, hepatic synthetic impairment, nutritional intake and other intestinal disease. The small urinary protein loss in this vignette is insufficient to explain the profound hypoalbuminemia. A normal INR does not exclude Fontan-associated liver disease, and more than one mechanism may coexist.',
   'Loss may include immunoglobulins and lymphocytes as well as albumin. Review nutritional status, infection risk and fluid balance rather than interpreting albumin as an isolated liver test.'])]),
  ('Test Collection and Interpretation',[
  ('**Alpha-1-antitrypsin clearance combines a timed stool collection with a serum concentration obtained during collection.** It accounts for circulating concentration and stool output better than an isolated random fecal concentration.',[
   'Mayo lists a reference clearance of 27 mL/24 hours or less. Interpret against the performing laboratory and stool consistency: diarrhea can increase clearance, and a higher threshold is used in some Fontan definitions. Do not apply a single cutoff without those qualifications.',
   'Gastrointestinal bleeding can contribute protein to stool. Acid degradation also limits assessment of predominantly gastric protein loss; a negative test does not resolve every possible protein-losing disorder.'])]),
  ('Evaluate the Failing Fontan Circuit',[
  ('**Confirmation should trigger assessment for reversible hemodynamic and lymphatic contributors.** Preserved ventricular ejection fraction does not exclude an important Fontan circulation problem.',[
   'Evaluate pathway obstruction, pulmonary resistance, ventricular filling pressure, AV-valve regurgitation and rhythm. Catheterization and specialist lymphatic imaging may be appropriate according to the findings.',
   'Management combines nutritional support and careful fluid treatment with correction of identified lesions. Selected patients require targeted lymphatic interventions or advanced heart-failure and transplant assessment. Albumin infusion can provide temporary support in selected circumstances but does not by itself correct the cause of continuing intestinal loss.'])]),
  ('Related Lymphatic Complication: Plastic Bronchitis',[
  ('**Abnormal lymphatic flow can also produce branching bronchial casts.** Cough, expectoration of casts, hypoxemia or airway obstruction suggest plastic bronchitis rather than intestinal protein loss.',[
   'Airway compromise requires urgent respiratory assessment and, when needed, bronchoscopic cast removal. Dynamic contrast MR lymphangiography can identify abnormal pulmonary lymphatic perfusion and help plan selected lymphatic intervention at an experienced center.',
   'Assess Fontan pressures, pathway patency and ventricular filling in parallel. A preserved ejection fraction does not exclude either lymphatic complication. Targeted treatment is anatomy-dependent; recurrent casts should not be managed as uncomplicated asthma or infection without evaluating the Fontan and lymphatic systems.'])])],
 ['ACHD2025','AAT_CLEARANCE','FONTAN_KOREA']))

rows.append(Q(TOPIC,'Anticoagulation After Atrial Flutter in Fontan Circulation',
 'A 28-year-old man with an extracardiac Fontan has a documented 20-minute episode of atrial flutter and is now in sinus rhythm. He has no conventional CHA2DS2-VASc risk factors, previous thromboembolism or bleeding contraindication. Which long-term strategy is most appropriate?',
 'Initiate oral anticoagulation after individualized agent and bleeding-risk assessment',[
 ('Continue aspirin alone because the conventional stroke score is zero','Aspirin can be a prophylactic option for Fontan adults without high-risk features. Sustained atrial flutter places this patient in a higher-risk congenital group that is not adequately represented by a conventional acquired-AF score.'),
 ('Withhold antithrombotic therapy unless a second flutter episode occurs','Observation may be appropriate for selected incidental rhythm findings that do not establish a relevant sustained atrial arrhythmia. A documented 20-minute flutter episode already establishes the high-risk feature here; recurrence is not required.'),
 ('Use anticoagulation only during future documented flutter episodes','Time-limited anticoagulation is used for some transient indications and procedural situations. Fontan-associated stasis and the history of sustained atrial flutter persist as risk considerations after sinus rhythm returns; intermittent treatment based solely on detected episodes is not the recommended strategy.')],
 [('Congenital Risk Beyond Conventional Scores',[
  ('**Fontan circulation combines venous stasis, surgically altered pathways and abnormal flow with potential atrial arrhythmia.** Its thromboembolic risk cannot be inferred from age and acquired vascular comorbidities alone.',[
   'The 2025 ACHD guideline identifies sustained atrial flutter or fibrillation lasting more than 30 seconds, prior thrombus or thromboembolism, cerebrovascular events and atriopulmonary Fontan anatomy as high-risk features supporting anticoagulation unless contraindicated.',
   'Restoration of sinus rhythm does not erase the documented arrhythmia history. The extracardiac connection does not negate the risk added by this sustained episode.'])]),
  ('Choice of Therapy and Follow-Up',[
  ('**Separate the indication for anticoagulation from the choice of drug.** Review hepatic and renal function, bleeding history, interactions, adherence and the congenital anatomy with an experienced team.',[
   'Warfarin has extensive historical use. Contemporary data also include direct oral anticoagulants, but comparative evidence in Fontan adults remains limited; do not claim that one agent has proven universal superiority or that all DOAC use is categorically prohibited.',
   'For adults without the high-risk features and without bleeding contraindications, current guidance recommends prophylaxis with aspirin or anticoagulation. That lower-risk choice should not be transferred to the present patient. Conversely, adding aspirin to an anticoagulant requires its own indication because combined treatment increases bleeding exposure.',
   'Evaluate the arrhythmia substrate and Fontan hemodynamics as well as prescribing thromboprophylaxis. Rhythm recurrence can impair filling and output, and may signal pathway or ventricular deterioration. Monitoring should include treatment adherence, bleeding, organ function and recurrent rhythm symptoms. The purpose of long-term prevention is distinct from decisions about anticoagulation around an urgent or planned cardioversion.'])])],
 ['ACHD2025','FONTAN_KOREA']))

REFERENCES['FALD_EASL']=('EASL-ERN position paper on liver involvement in Fontan circulation, 2023','https://www.journal-of-hepatology.eu/article/S0168-8278%2823%2904992-9/fulltext')
rows.append(Q(TOPIC,'Liver Surveillance in Fontan-Associated Cirrhosis',
 'A 32-year-old, 28 years after Fontan completion, has hepatology-confirmed cirrhosis. Aminotransferases are near normal, ultrasound visualization is adequate and no focal lesion is present. Which surveillance strategy best addresses the risk of hepatocellular carcinoma?',
 'Liver ultrasound at six-month intervals, with AFP as an adjunct',[
 ('Annual aminotransferases, with liver imaging when enzymes rise','Annual laboratory assessment is part of Fontan organ surveillance, but aminotransferases may remain near normal despite advanced disease. Waiting for enzyme elevation can miss an asymptomatic hepatic tumor.'),
 ('Annual elastography, with imaging for a focal lesion only if stiffness increases','Elastography can contribute longitudinal information, but stiffness is affected by venous congestion and does not screen directly for focal malignancy. A stable stiffness value does not replace scheduled tumor surveillance.'),
 ('Scheduled repeat liver biopsy to detect early malignant transformation','Biopsy is useful for selected diagnostic or transplant-related questions and indeterminate lesions. Repeated nontargeted biopsy is not the routine method for detecting new focal HCC and exposes the patient to procedural risk and sampling limitations.')],
 [S('Surveillance Despite Quiet Biochemistry',
  '**Fontan-associated liver disease arises in the setting of chronic hepatic venous congestion and altered perfusion.** Fibrosis, cirrhosis and malignancy can develop without striking aminotransferase elevations.',
  'Confirmed cirrhosis supports surveillance at least every six months under current ACHD guidance. EASL-ERN describes six-monthly ultrasound by experienced personnel, with AFP as an adjunct. A normal AFP does not exclude a tumor.',
  'Use the surveillance plan appropriate to actual imaging quality and risk. Poor visualization or a suspicious lesion warrants specialist selection of cross-sectional imaging rather than repeated reliance on an inadequate ultrasound examination.'),
  S('Interpreting Stiffness and Nodules',
  '**Elastography measures a physical property influenced by both fibrosis and congestion.** A high value cannot be translated uncritically into a fibrosis stage using thresholds validated in an unrelated liver disease.',
  'Serial imaging, laboratory trends and signs of portal hypertension complement one another. Falling platelet count, splenomegaly, varices or ascites merit assessment; ascites can also reflect the underlying cardiac circulation.',
  'Fontan livers may contain benign regenerative nodules, so a new lesion requires expert characterization. Multiphase CT or MRI and selected biopsy may be needed when imaging remains indeterminate. Routine biopsy solely to track fibrosis is controversial and should have a clear potential to change management.'),
  S('Coordinated Follow-Up',
  '**Cardiology and hepatology should jointly interpret hepatic findings.** Assess the Fontan pathway, filling pressures, ventricular function and other contributors to venous congestion alongside liver disease.',
  'Annual organ-system laboratory assessment remains useful but complements rather than replaces tumor surveillance. Advanced disease may affect procedural planning, anticoagulation decisions and consideration of isolated cardiac versus combined heart-liver transplantation. Those decisions require assessment of the overall circulation and hepatic complications rather than a single stiffness measurement.')],
 ['ACHD2025','FALD_EASL']))

rows.append(Q(TOPIC,'New Atrial Flutter and Fontan Hemodynamic Deterioration',
 'An adult with Fontan circulation develops new atrial flutter and worsening exercise intolerance. After initial rate slowing, blood pressure is maintained, but venous congestion and fatigue persist. Which strategy best addresses the risk of progressive Fontan failure?',
 'Plan timely rhythm restoration with thrombus assessment and anticoagulation, while evaluating the Fontan circuit',[
 ('Continue rate control alone and reassess ventricular function at routine follow-up','Rate slowing can provide initial stabilization, but loss of effective atrial rhythm can impair Fontan filling even with an acceptable ventricular rate. Persistent symptoms warrant timely rhythm restoration and hemodynamic evaluation rather than routine delayed review.'),
 ('Escalate diuresis first and defer rhythm restoration until congestion has resolved','Careful diuresis may help congestion, but excessive preload reduction can worsen output. The atrial arrhythmia itself may be driving the deterioration and should not be left untreated while waiting for complete decongestion.'),
 ('Start pulmonary vasodilator treatment and reserve cardioversion for failure of that therapy','Selected Fontan patients with pulmonary vascular limitation may benefit from vasodilators after physiological assessment. This does not substitute for treating a new atrial arrhythmia, and unmeasured filling pressures may alter the suitability of vasodilator therapy.')],
 [S('Why Rate Control May Be Insufficient',
  '**Effective atrial rhythm supports filling in a circulation already limited by passive pulmonary flow.** Flutter can impair atrioventricular coordination and reduce output even after the ventricular rate has slowed.',
  'Loss of atrial contribution, pulmonary venous flow disturbance and shortened or ineffective filling can interact with AV-valve regurgitation and abnormal ventricular relaxation. Symptoms may therefore be disproportionate to the apparent rate or resting ejection fraction.'),
  S('Rhythm Restoration and Procedural Planning',
  '**The 2025 ACHD guideline recommends timely cardioversion for new atrial flutter or fibrillation in Fontan adults.** Pharmacological or electrical restoration is selected according to rhythm, stability and specialist assessment.',
  'In a stable patient, assess thrombus risk, anticoagulation and the need for imaging before cardioversion. Do not assume a short reported duration excludes thrombus in this complex circulation. If the rhythm causes hemodynamic instability, urgent synchronized electrical cardioversion takes priority and should not be delayed for an elective anticoagulation interval.',
  'Sedation and ventilation require attention to venous return, preload and pulmonary resistance. Excessive airway pressures, hypoxemia or acidosis can compromise passive pulmonary flow. Plan with clinicians familiar with the anatomy and circulation rather than treating procedural preparation as routine.'),
  S('Search for a Hemodynamic Trigger',
  '**New or worsening atrial tachyarrhythmia should prompt imaging and catheter assessment when indicated.** Consider pathway obstruction or thrombosis, AV-valve disease, ventricular dysfunction and elevated filling pressure.',
  'Long-term management may include congenital EP evaluation and ablation, recurrence monitoring and appropriate anticoagulation. Correcting a contributory lesion and maintaining an effective rhythm are complementary goals. Persistent Fontan failure despite treatment warrants advanced specialist assessment, including transplantation evaluation when appropriate.')],
 ['ACHD2025','FONTAN_KOREA']))
