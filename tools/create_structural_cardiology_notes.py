from create_remaining_cardiology_notes import *
CMP=('ESC cardiomyopathy guideline, 2023','https://academic.oup.com/eurheartj/article/44/37/3503/7246608')
ACHD=('AHA/ACC adult congenital heart disease guideline, 2025','https://doi.org/10.1161/CIR.0000000000001402')
PH=('ESC/ERS pulmonary hypertension guideline, 2022','https://academic.oup.com/eurheartj/article/43/38/3618/6673929')
AORTA=('ACC/AHA aortic disease guideline, 2022','https://doi.org/10.1016/j.jacc.2022.08.004')

def valves():
 write('Cardiology','Valvular',[
 S('Stenotic lesions: compare severity and intervention',T('Lesion|Typical findings|Key decision','''Aortic stenosis|Ejection systolic murmur radiating to carotids; delayed carotid pulse|Severe high-gradient: Vmax ≥4 m/s or mean gradient ≥40 mmHg; valve area usually ≤1.0 cm²
 Low-flow/low-gradient AS|Small valve area with lower gradient|Check stroke volume and measurement error; dobutamine stress or CT calcium can distinguish true severe from pseudo-severe disease
 Rheumatic mitral stenosis|Opening snap, apical diastolic rumble; AF and pulmonary hypertension|Clinically significant area ≤1.5 cm²; balloon commissurotomy for suitable anatomy without LA thrombus or more than mild MR
 Tricuspid stenosis|Raised JVP with large a waves; inspiratory increase in diastolic murmur|Usually associated with rheumatic left-sided disease''')+U('''Symptomatic severe AS usually requires valve replacement. Selected asymptomatic patients also benefit from intervention; do not wait for symptoms in every severe lesion.
 TAVI versus surgery: age, life expectancy, anatomy, transfemoral access, valve/aortic disease and future procedures; do not decide from age alone.
 AF with significant rheumatic MS: vitamin K antagonist rather than a DOAC.''')),
 S('Regurgitant lesions',T('Lesion|Recognition|Treatment distinction','''Primary MR|Leaflet/chordal disease: prolapse, flail, rheumatic or infective destruction|Repair preferred when durable; symptoms or early LV dysfunction trigger intervention
 Secondary MR|LV/LA remodeling with relatively intact leaflets|Optimize HF therapy/CRT first; selected transcatheter or surgical intervention
 Aortic regurgitation|Early diastolic murmur, wide pulse pressure in chronic severe disease|Symptoms, LV size/function and aortic disease guide surgery
 Tricuspid regurgitation|Inspiratory pansystolic murmur, large cv waves, systemic congestion|Treat cause/congestion; intervene before irreversible RV/end-organ damage in suitable patients''')+U('''Primary severe MR: LVEF ≤60% or LV end-systolic diameter ≥40 mm are established warning thresholds; preserved-looking EF can already represent dysfunction. The 2025 ESC guideline adds earlier-intervention considerations in selected patients.
 Acute severe MR/AR can cause shock without a loud murmur or dilated ventricle; urgent echo and intervention are required.
 AR and MR severity requires integrated Doppler, anatomy and ventricular response; jet area alone is insufficient.''')),
 S('Prosthetic valves and endocarditis',T('Situation|High-yield rule','''Mechanical valve|Lifelong vitamin K antagonist; INR target depends on valve and risk factors. DOACs are not substitutes.
 Bioprosthetic valve|Antithrombotic strategy depends on position, time since implantation and AF/other indications.
 Prosthetic obstruction|Consider thrombosis, pannus, degeneration and patient–prosthesis mismatch; use echo and selected CT/fluoroscopy.
 Suspected infective endocarditis|Blood cultures before antibiotics when this does not delay urgent care; TTE then TEE when indicated.
 High-risk dental prophylaxis|Selected patients such as prosthetic valves or previous endocarditis; not every murmur requires prophylaxis.''')+U('''New regurgitation with fever or emboli requires endocarditis assessment. A negative initial echo does not exclude early infection.
 Diuretics improve congestion but do not correct severe mechanical valve disease.
 Mitral valve prolapse click moves earlier with reduced LV volume and later with increased filling.'''))],[VHD,('ESC endocarditis guideline, 2023','https://doi.org/10.1093/eurheartj/ehad193')])

def cardiomyopathy():
 write('Cardiology','Cardiomyopathies',[
 S('Recognize the phenotype; then identify the cause',T('Pattern|Key clues|Important alternatives','''Dilated cardiomyopathy|LV dilation and systolic dysfunction|Ischemia, genetic disease, alcohol/drugs, tachycardia, myocarditis, endocrine causes
 Hypertrophic cardiomyopathy|Unexplained hypertrophy; dynamic obstruction may occur|Hypertension, aortic stenosis, athletic remodeling, amyloid/Fabry and other phenocopies
 Restrictive cardiomyopathy|Impaired filling, enlarged atria, often nondilated ventricles|Amyloidosis, fibrosis and storage disease; distinguish constriction
 Arrhythmogenic cardiomyopathy|Ventricular arrhythmias with RV/LV scar or dysfunction|Myocarditis, sarcoidosis and other inherited disease''')+U('''Obtain a three-generation pedigree when inherited disease is possible. Genetic counseling, targeted testing and family screening can change management.
 CMR defines chamber function, edema and scar pattern. A preserved EF does not exclude arrhythmic risk in a scarred/genetic cardiomyopathy.''')),
 S('Hypertrophic cardiomyopathy',T('Problem|Management / distinction','''LV outflow obstruction|Gradient ≥30 mmHg defines obstruction; ≥50 mmHg is important when considering symptom-directed advanced treatment
 Symptomatic obstructive HCM|Nonvasodilating beta blocker; verapamil/diltiazem in appropriate patients if unsuitable/ineffective
 Persistent symptoms|Selected myosin inhibitor, disopyramide or septal reduction at an experienced centre
 AF in HCM|Anticoagulate unless contraindicated; usual low CHA₂DS₂-based scores do not remove the indication
 Sudden-death prevention|Prior arrest/sustained VT and major risk markers guide ICD assessment; not every HCM patient needs an ICD''')+U('''Dehydration, vasodilation and reduced preload can worsen obstruction. Systolic anterior motion can cause MR.
 Myosin inhibitors can reduce EF and have important interactions/pregnancy precautions; follow product-specific monitoring.
 Do not label all LV hypertrophy sarcomeric HCM before assessing phenocopies.''')),
 S('Infiltrative and inflammatory disease',T('Disease|Discriminating clues|Action','''Cardiac amyloidosis|Thick walls, restrictive physiology; low voltage may be absent; strain apical sparing is supportive, not diagnostic|Screen serum free light chains plus serum/urine immunofixation; bone scintigraphy supports ATTR only with the required criteria and exclusion of a monoclonal process
 AL amyloidosis|Monoclonal light-chain disease|Urgent hematology-directed assessment; do not assume ATTR from a positive bone scan alone
 Fabry disease|LVH with renal/neurological features; low native T1 can be a clue|Enzyme/genetic assessment appropriate to sex and presentation
 Cardiac sarcoidosis|AV block, VT, patchy scar/inflammation|CMR/PET and selected biopsy; immunosuppression and rhythm/device management
 Myocarditis|Chest pain, troponin, arrhythmia or HF; CMR edema/nonischemic injury|Biopsy in selected high-risk cases where histology changes treatment''')),
 S('Cause-specific and long-term care',U('''Dilated disease: treat HF and the cause; suppress causal tachyarrhythmia, stop cardiotoxins and evaluate familial disease.
 Peripartum cardiomyopathy: pregnancy/postpartum timing plus LV dysfunction after excluding alternatives; drug selection must account for pregnancy/lactation and thrombotic risk.
 Exercise advice depends on phenotype, genotype, arrhythmias and activity intensity; blanket unrestricted endurance exercise is inappropriate in arrhythmogenic disease.
 Improvement in EF does not erase inherited risk or justify automatic withdrawal of HF treatment.'''))],[CMP,HCM,MYO])

def congenital():
 write('Cardiology','Adult Congenital',[
 S('Shunts: anatomy and hemodynamics',T('Lesion|Typical clues|Key issue','''ASD|Fixed split S2; RV volume overload|Closure depends on shunt size, RV enlargement and pulmonary vascular resistance
 VSD|Pansystolic murmur at lower left sternal border|Small restrictive defects may be loud; large defects can cause pulmonary vascular disease
 PDA|Continuous murmur; differential cyanosis in advanced reversal|Closure requires assessment of pulmonary vascular disease
 AV septal defect|AV-valve regurgitation and shunt; association with trisomy 21|Residual shunt, valve disease and conduction problems persist in adults''')+U('''Qp/Qs estimates pulmonary-to-systemic flow; >1 indicates net left-to-right shunting. A ratio alone does not establish safe closure.
 Eisenmenger syndrome: advanced pulmonary vascular disease with reversed/bidirectional shunting and cyanosis. Do not close the defect as routine treatment.''')),
 S('Obstructive lesions and repaired disease',T('Condition|Recognition|Adult complication','''Coarctation|Upper-limb hypertension, arm–leg pressure difference, radiofemoral delay|Persistent hypertension, recoarctation, aneurysm; assess associated bicuspid aortic valve
 Bicuspid aortic valve|AS/AR with aortopathy|Image the aorta; assess first-degree relatives as indicated
 Repaired tetralogy of Fallot|Previous RV outflow repair|Pulmonary regurgitation, RV enlargement, ventricular arrhythmias; time pulmonary-valve intervention before irreversible damage
 Atrial-switch transposition / congenitally corrected transposition|Systemic morphological RV|Systemic RV failure, tricuspid regurgitation, arrhythmias/AV block
 Fontan circulation|Systemic venous flow to pulmonary arteries without a subpulmonary ventricle|Venous hypertension, liver disease, thrombosis, protein-losing enteropathy and arrhythmia''')),
 S('Cyanosis, stroke and pregnancy',U('''Chronic cyanosis: iron deficiency can coexist with secondary erythrocytosis. Routine phlebotomy is harmful; reserve for specific symptomatic hyperviscosity situations after correcting dehydration/iron deficiency.
 Right-to-left shunts permit paradoxical embolism; avoid air in intravenous lines and assess embolic sources.
 Pregnancy risk is lesion- and physiology-specific. Eisenmenger syndrome and severe pulmonary hypertension carry very high maternal risk and require preconception specialist counseling.
 Anticoagulation is individualized; cyanotic disease can carry both thrombotic and bleeding risk. Do not apply routine anticoagulation to every cyanotic patient.''')),
 S('Follow-up and pitfalls',U('''Anatomical repair is not cure: residual valve disease, ventricular dysfunction, arrhythmias and aortic complications require lifelong review.
 Use adult-congenital expertise for intervention, pregnancy, arrhythmia and complex imaging decisions.
 Endocarditis prophylaxis is restricted to specified high-risk lesions/prosthetic material and procedures.
 Do not infer pulmonary vascular reversibility from echo pressure estimates alone when closure is being considered; invasive assessment may be necessary.'''))],[ACHD,PH])

def pericardial():
 write('Cardiology','Pericardial PH Aortic',[
 S('Pericarditis, effusion and tamponade',T('Condition|Key findings|Management','''Acute pericarditis|Pleuritic/positional pain, rub, diffuse ST/PR changes or new effusion|Anti-inflammatory therapy plus colchicine when appropriate; assess cause and high-risk features
 Tamponade|Hypotension, raised JVP, pulsus paradoxus; chamber collapse on echo|Urgent drainage when hemodynamically significant; do not wait for all classic signs
 Recurrent pericarditis|Recurrent inflammatory episodes|Colchicine and cause-directed therapy; selected steroid-sparing/IL-1-directed treatment for refractory disease
 Constrictive pericarditis|Ventricular interdependence, septal shift, expiratory hepatic-vein reversal; often preserved medial e′|Treat reversible inflammation when present; established symptomatic constriction may need pericardiectomy''')+U('''Effusion size does not determine tamponade alone; rate of accumulation and chamber pressures matter.
 Constriction versus restriction: respiratory LV/RV systolic pressure discordance favors constriction; myocardial restriction more often shows concordance. Pericardial calcification is not required.''')),
 S('Pulmonary hypertension: classify before treatment',T('Hemodynamic pattern|Right-heart catheterization','''PH|Mean pulmonary artery pressure >20 mmHg
 Precapillary PH|mPAP >20, wedge ≤15 mmHg, PVR >2 Wood units
 Isolated postcapillary PH|mPAP >20, wedge >15, PVR ≤2
 Combined post/precapillary PH|mPAP >20, wedge >15, PVR >2''')+U('''PVR = (mPAP − wedge pressure)/cardiac output. Elevated pressure alone does not establish pulmonary arterial hypertension.
 Groups: 1 PAH; 2 left-heart disease; 3 lung/hypoxia; 4 chronic thromboembolic disease; 5 multifactorial.
 V/Q scanning is important to exclude chronic thromboembolic disease. Right-heart catheterization confirms phenotype when treatment decisions require it.
 PAH-specific drugs are not routine treatment for group 2 or all group 3 PH. CTEPH requires assessment for endarterectomy, balloon angioplasty and selected medical therapy.''')),
 S('Aortic dissection and aneurysm',T('Condition|Immediate distinction','''Stanford type A|Ascending aorta involved: emergency surgical assessment
 Stanford type B|No ascending involvement: anti-impulse therapy if uncomplicated; complicated disease often requires endovascular/surgical treatment
 Acute aortic syndrome|Dissection, intramural hematoma or penetrating ulcer; assess with urgent appropriate aortic imaging
 Thoracic aneurysm|Intervention depends on segment, diameter, growth, genotype, body size and associated surgery''')+U('''Initial anti-impulse treatment commonly uses IV beta blockade, then vasodilator if needed; avoid reflex tachycardia. Correct shock or severe AR according to the cause.
 Pulse/BP asymmetry and tearing pain may be absent. D-dimer cannot independently exclude high-probability dissection.
 Sporadic root/ascending aneurysm: 5.5 cm is a common intervention threshold; selected expert-centre patients, rapid growth and heritable disease warrant earlier surgery.
 Confirmed growth ≥0.5 cm in one year or ≥0.3 cm/year over two consecutive years is a major warning in sporadic root/ascending disease.'''))],[MYO,PH,AORTA])

def hypertension():
 write('Cardiology','Hypertension',[
 S('Confirm the diagnosis',T('Pattern|Definition / action','''Persistent hypertension|Standardized repeated office readings; confirm with home/ambulatory measurement when appropriate
 White-coat hypertension|Office high, out-of-office normal
 Masked hypertension|Office normal, out-of-office high
 Resistant hypertension|Uncontrolled despite an appropriate three-drug regimen including a diuretic, or controlled with ≥4 drugs; exclude nonadherence and measurement error''')+U('''Use a validated device, correct cuff, supported back/arm and rest before measurement. Check both arms initially.
 US 2025: hypertension begins at ≥130/80 mmHg; ESC office diagnostic threshold remains ≥140/90. Do not mix diagnostic thresholds and treatment targets.
 US treatment goal is generally <130/80; individualize for frailty, symptoms, pregnancy and limited life expectancy.''')),
 S('Drug selection and secondary causes',T('Situation|Preferred direction / clue','''Uncomplicated hypertension|ACE inhibitor/ARB, long-acting dihydropyridine CCB or thiazide-like diuretic; combinations often required
 Albuminuric CKD|ACE inhibitor/ARB when tolerated; monitor K/creatinine
 Resistant hypertension|Optimize diuretic, assess sodium intake/OSA/secondary causes; spironolactone in eligible patients
 Primary aldosteronism|Resistant hypertension, spontaneous/diuretic-associated hypokalemia or adrenal context; screen appropriately even if K is normal
 Renovascular disease|Abrupt worsening, recurrent flash pulmonary edema or marked creatinine rise with RAAS blockade
 Pheochromocytoma|Paroxysmal headache, sweating/palpitations; appropriate metanephrines; alpha blockade before beta blockade when required
 Drug-related hypertension|NSAIDs, stimulants, steroids, oral contraceptives, calcineurin inhibitors and selected cancer drugs''')),
 S('Hypertensive emergency',T('Presentation|Principle','''Severe BP + acute target-organ damage|Monitored IV treatment; pressure alone does not define the emergency
 Most emergencies|Controlled initial reduction, commonly ≤20–25% mean arterial pressure in the first hour; avoid sudden normalization
 Aortic dissection|More rapid anti-impulse treatment
 Ischemic stroke / intracranial hemorrhage|Use stroke-specific thresholds; do not apply the generic reduction rule
 Preeclampsia/eclampsia|Obstetric emergency pathway and appropriate magnesium/antihypertensive treatment''')+U('''Severe asymptomatic hypertension usually needs assessment and adjustment of oral treatment, not rapid IV lowering.
 Lifestyle: sodium reduction, weight control, exercise, moderation of alcohol and treatment of sleep apnea.
 US 2025 recommends medication at ≥140/90 for all eligible adults and at ≥130/80 for selected high-risk groups; lower-risk persistent elevation after lifestyle treatment also requires reassessment.'''))],[HT,('ESC elevated BP/hypertension guideline, 2024','https://doi.org/10.1093/eurheartj/ehae178')])

def imaging():
 write('Cardiology','Imaging Hemodynamics',[
 S('Choose the test for the question',T('Test|Best uses|Limitation','''TTE|Ventricular/valve function, effusion, pressure estimates|Image quality and loading conditions affect results
 TEE|Prosthetic valves, endocarditis, LA appendage thrombus, selected aortic disease|Semi-invasive; assess esophageal/procedural risk
 CMR|Volumes/EF, scar, edema, infiltrative disease, shunts|Availability, device safety and contrast-related considerations
 Coronary CT angiography|Anatomical exclusion/assessment of CAD in selected patients|Heavy calcium can overestimate stenosis; contrast/heart-rate issues
 Stress echo / nuclear / stress CMR|Inducible ischemia and functional significance|Modality-specific artifacts; ischemia is not equivalent to a universal PCI indication
 Invasive angiography / physiology|Coronary anatomy and lesion-specific significance|Invasive risks; anatomical severity and physiological significance differ''')),
 S('Core hemodynamic formulas',T('Quantity|Formula / threshold','''Cardiac output|Heart rate × stroke volume
 Cardiac index|Cardiac output / body surface area
 Fick cardiac output|Oxygen consumption / arteriovenous oxygen-content difference; use consistent units
 PVR|Mean PA pressure − wedge pressure, divided by cardiac output; Wood units
 SVR|Mean arterial pressure − right atrial pressure, divided by cardiac output; multiply by 80 for dyn·s·cm⁻⁵
 Simplified Bernoulli gradient|4v², with velocity in m/s and gradient in mmHg
 FFR / iFR|≤0.80 / ≤0.89 commonly denotes significant lesion physiology
 Qp/Qs|Pulmonary/systemic flow; oxygen-saturation step-ups help localize left-to-right shunts''')),
 S('Waveforms and interpretation',T('Finding|Meaning / caveat','''Large wedge v wave|May reflect MR or reduced LA compliance; not uniquely severe MR
 Giant RA a waves|AV dissociation, tricuspid obstruction or impaired RV filling; absent a waves in AF
 Kussmaul sign|Inspiratory JVP rise; RV filling limitation, constriction or restriction
 Wedge pressure|Estimates LA pressure under appropriate conditions; is not identical to LVEDP in every disease
 Tamponade|Pressure equalization and respiratory effects; clinical/echo integration required
 Constriction|Ventricular interdependence and respiratory pressure discordance''')+U('''Check zeroing, leveling, respiratory phase and waveform quality before interpreting catheter pressures.
 Doppler gradients are flow dependent. Low flow can hide severe stenosis; high flow can exaggerate gradients.
 LVEF is load dependent; normal EF does not exclude HF or early myocardial dysfunction.
 Late gadolinium enhancement indicates myocardial injury/scar pattern; it does not alone prove active inflammation.'''))],[PH,VHD,CMP,('ESC chronic coronary syndromes guideline, 2024','https://doi.org/10.1093/eurheartj/ehae177')])

def prevention():
 write('Cardiology','Prevention Dyslipidemia',[
 S('Risk and treatment goals',T('Setting|High-yield approach','''Established ASCVD|Secondary prevention; high-intensity/maximally tolerated statin and goal-directed additional treatment
 Very-high-risk ASCVD|2026 US LDL goal <55 mg/dL; non-HDL <85 mg/dL
 Other ASCVD|Generally LDL <70 mg/dL; selected patients may reasonably target <55
 LDL ≥190 mg/dL / familial hypercholesterolemia|Treat without relying on a low short-term risk score; assess family and secondary causes
 Primary prevention|2026 US guideline uses PREVENT-ASCVD rather than old pooled-cohort equations; incorporate risk enhancers and selected coronary calcium testing''')+U('''A low calculated 10-year risk in a young person does not erase severe lifelong LDL exposure.
 Measure lipoprotein(a) at least once in adulthood under current guidance; apoB can reveal residual particle-related risk, especially with high triglycerides or metabolic disease.
 Do not convert Lp(a) mg/dL to nmol/L with one universal conversion factor.''')),
 S('Lipid drugs: compare mechanisms and adverse effects',T('Class|Action|Key distinction','''Statin|HMG-CoA reductase inhibition|First-line outcome benefit; myopathy/interactions vary by agent
 Ezetimibe|Intestinal cholesterol absorption inhibition|Useful statin add-on; modest LDL reduction
 PCSK9 monoclonal antibody|Increased LDL-receptor recycling|Large LDL reduction and established outcome benefit in appropriate patients
 Inclisiran|RNA interference reducing PCSK9 production|Long dosing interval; do not assume identical outcome evidence to every PCSK9 therapy
 Bempedoic acid|ATP-citrate lyase inhibition|Option in selected patients including intolerance; hyperuricemia/gout and tendon warnings
 Fibrate|Triglyceride lowering|Useful in selected severe hypertriglyceridemia; renal dosing and statin interaction concerns
 Icosapent ethyl|Purified EPA|Outcome benefit in a defined high-risk, statin-treated population; not interchangeable with mixed OTC fish oil''')),
 S('Triglycerides, intolerance and prevention',U('''Triglycerides ≥500 mg/dL: evaluate secondary causes and pancreatitis risk, especially at much higher levels; alcohol, uncontrolled diabetes and medicines are important reversible causes.
 Statin symptoms: review timing, CK when indicated, hypothyroidism, interactions and alternative causes; rechallenge or use another regimen when safe rather than abandoning LDL lowering.
 Coronary calcium helps selected uncertain primary-prevention decisions; CAC=0 does not cancel every high-risk indication.
 Smoking cessation, BP control, exercise, diet and diabetes/weight management remain central. Aspirin is not routine primary prevention for every adult.
 Recheck lipids after starting/changing treatment; assess adherence before declaring drug failure.'''))],[LIP,HT])

if __name__=='__main__':
 valves();cardiomyopathy();congenital();pericardial();hypertension();imaging();prevention()
