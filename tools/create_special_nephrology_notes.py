from create_core_nephrology_notes import *
PKD=('KDIGO ADPKD guideline, 2025','https://kdigo.org/guidelines/autosomal-dominant-polycystic-kidney-disease-adpkd/kdigo-2025-adpkd-guideline/')
STONE=('EAU urolithiasis guideline','https://uroweb.org/guidelines/urolithiasis/chapter/guidelines')
TX=('KDIGO kidney transplant recipient guideline','https://kdigo.org/guidelines/transplant-recipient/')

def tubular():
 write('Nephrology','Tubulointerstitial Cystic Kidney Diseases',[
 S('Tubulointerstitial injury',T('Condition|Clues|Key management','''Acute interstitial nephritis|AKI after drug exposure or systemic disease; pyuria may occur|Stop cause; selected biopsy and corticosteroid treatment after infection/other causes are assessed
 Chronic interstitial disease|Concentrating defect, modest proteinuria, progressive CKD|Identify drugs/toxins, reflux/obstruction or inherited causes
 Analgesic-associated injury|Chronic exposure, papillary injury and CKD pattern|Stop exposure and assess complications
 Lithium nephropathy|Nephrogenic DI and possible chronic tubulointerstitial disease|Drug/psychiatric review, hydration safety and selected treatment
 Light-chain proximal disease|Fanconi pattern; monoclonal protein concern|Hematological and renal assessment''')+U('''The fever–rash–eosinophilia triad is often absent in AIN. Urine eosinophils are not a definitive diagnostic test.
 Proton-pump inhibitors, antibiotics and NSAIDs are important drug groups; NSAID-associated disease may include substantial proteinuria.
 Tubular proteinuria may be missed by an albumin-focused dipstick.''')),
 S('Inherited tubular syndromes',T('Syndrome|Physiology|Discriminating clue','''Bartter|Loop-like salt wasting|Hypokalemic alkalosis, high renin/aldosterone, usually normal/low BP; urinary calcium often increased
 Gitelman|Thiazide-like salt wasting|Hypokalemic alkalosis, hypomagnesemia and low urine calcium
 Liddle|ENaC gain of function|Hypertension, hypokalemic alkalosis, low renin/aldosterone; ENaC-directed treatment
 Apparent mineralocorticoid excess|Impaired cortisol inactivation or relevant exposure|Low-renin/low-aldosterone hypertension; licorice is an acquired mimic
 Fanconi syndrome|Generalized proximal losses|Normoglycemic glycosuria, phosphate/urate/bicarbonate loss''')),
 S('ADPKD: kidney and systemic disease',U('''Autosomal-dominant cystic disease: assess family history, age-appropriate imaging and selected genetic testing. Negative family history does not exclude a new variant or unrecognized family disease.
 Risk assessment uses kidney size/imaging class, eGFR trajectory and other factors; cyst count alone does not establish rapid progression.
 Tolvaptan is for selected adults at risk of rapid progression with adequate kidney function, not all cystic disease. KDIGO 2025 supports eligible initiation at eGFR ≥25; monitor liver tests, aquaresis, sodium and access to water.
 Flank pain: consider cyst hemorrhage, infection and stones. Fever with focal pain requires infection assessment; cyst penetration influences antibiotic selection.
 Extrarenal disease includes liver cysts, intracranial aneurysms and selected cardiac/aortic findings. Intracranial screening is targeted by history/risk and shared decision, not automatic annual imaging for everyone.''')),
 S('Other cystic disease and pitfalls',T('Pattern|Distinction','''Simple cyst|Typical benign imaging; complex features require characterization
 Acquired cystic kidney disease|Advanced CKD/dialysis context; increased renal-tumor risk
 Autosomal-dominant tubulointerstitial disease|Often bland urine, progressive CKD and family pattern; cysts may be few or absent
 Medullary sponge kidney|Collecting-duct ectasia with stones/hematuria/infection risk
 Complex renal cyst / solid component|Use appropriate imaging classification and urological assessment; not every cyst is ADPKD'''))],[PKD,AKI])

def stones():
 write('Nephrology','Nephrolithiasis Obstructive Uropathy',[
 S('Acute colic: identify the emergency',U('''Assess pain, fever, renal function, pregnancy, solitary kidney and urine findings. Noncontrast CT is highly sensitive; ultrasound is preferred first in pregnancy and other radiation-sensitive settings.
 Infected obstruction or obstructed anuric system: urgent drainage by stent or nephrostomy plus antibiotics/support. Definitive stone removal is usually deferred until infection is controlled.
 Refractory pain, worsening renal function and high-risk anatomy also require urgent urological review.
 Hematuria may be absent. Hydronephrosis may be limited early or in selected forms of obstruction.''')),
 S('Stone types and prevention',T('Stone|Clues|Prevention / treatment distinction','''Calcium oxalate|Common; associated with hypercalciuria, hyperoxaluria or low citrate|Adequate normal dietary calcium with meals, sodium reduction, fluids; selected thiazide/citrate by metabolic findings
 Calcium phosphate|Higher urine pH; consider distal RTA|Treat cause; avoid indiscriminate excessive alkalinization
 Uric acid|Low urine pH; often radiolucent on plain film but visible on CT|Urine alkalinization is central; selected urate-lowering treatment
 Struvite|Urease-positive infection; possible staghorn calculus|Infection control and appropriate complete stone management; antibiotics alone may not eradicate the nidus
 Cystine|Inherited cystinuria; hexagonal crystals|High fluid intake, sodium management, alkalinization and selected thiol drugs''')),
 S('Metabolic evaluation and procedure selection',U('''Analyze a retrieved stone. Recurrent/high-risk disease often warrants 24-hour urine evaluation after the acute phase.
 Increase urine volume; prevention targets commonly aim above ~2–2.5 L/day, adjusted for clinical circumstances. Do not force excessive fluids during obstructed acute colic.
 Avoid a blanket low-calcium diet for calcium stones: lower gut calcium binding can increase oxalate absorption.
 Choose shock-wave lithotripsy, ureteroscopy or percutaneous treatment by size, site, composition, anatomy and patient factors.
 Alpha-blocker expulsive therapy has a selected role, especially suitable distal ureteric stones; it does not replace drainage of an infected obstruction.''')),
 S('Obstructive uropathy and post-obstructive diuresis',T('Problem|Key point','''Bilateral obstruction / solitary functioning kidney|Can cause severe AKI and hyperkalemia; decompress promptly when indicated
 Bladder outflow obstruction|Check retention/catheter; assess upper tracts and cause
 Post-obstructive diuresis|Monitor urine output, BP, sodium, potassium and magnesium after relief
 Fluid replacement|Match clinical volume/electrolyte needs; avoid unmonitored replacement of every milliliter
 Persistent dysfunction|Assess duration, infection and residual obstruction; drainage does not guarantee complete recovery'''))],[STONE,AKI])

def dialysis():
 write('Nephrology','Dialysis RRT',[
 S('Indications and modality',T('Decision|Principle','''Urgent dialysis|Refractory dangerous hyperkalemia/acidosis, pulmonary edema/overload, uremic complications or selected dialyzable poisoning
 Intermittent hemodialysis|Rapid small-solute clearance; hemodynamic tolerance matters
 Continuous kidney replacement|Slower continuous fluid/solute control; useful in selected unstable or neurological patients
 Peritoneal dialysis|Peritoneal exchange; home-based option with different access and infection issues
 Conservative kidney care|Active symptom and supportive management; appropriate option for selected patients''')+U('''Do not initiate chronic dialysis from one eGFR number without symptoms, complications and planning.
 Diffusion clears small solutes down a gradient; convection removes solute with filtered water. Ultrafiltration rate and solute clearance are separate prescriptions.''')),
 S('Adequacy and access',T('Measure / access|Interpretation','''URR|100 × (predialysis urea − postdialysis urea)/predialysis urea
 Single-pool Kt/V|K × time / urea distribution volume; sampling/recirculation affect results
 Thrice-weekly HD with little residual function|Common minimum delivered spKt/V 1.2, prescribed target around 1.4; schedules and residual function alter targets
 AV fistula/graft|Access choice individualized; assess maturation, stenosis, thrombosis, infection and ischemic steal
 Dialysis catheter|Immediate access but infection/thrombosis risk; avoid unnecessary prolonged exposure''')+U('''Adequate urea clearance does not prove adequate volume, nutrition, potassium or symptom control.
 High venous pressures, poor flows or recirculation can indicate access dysfunction. Preserve vascular access during admissions and procedures.''')),
 S('Complications grouped by mechanism',T('Problem|Recognition / action','''Intradialytic hypotension|Assess ultrafiltration, dry weight, cardiac disease, infection and medicines; do not treat every episode with an unchanged prescription
 Disequilibrium syndrome|Neurological deterioration after rapid solute change, especially initial high-urea treatments; prevention by a gentler initial prescription
 Hemolysis / air embolism / severe dialyzer reaction|Dialysis emergency; stop exposure and follow the specific circuit/patient safety protocol
 Citrate accumulation in continuous therapy|Systemic hypocalcemia, rising calcium needs and total/ionized calcium ratio; assess acid–base and citrate metabolism
 Anticoagulation|Bleeding/HIT risks versus circuit clotting; modality-specific selection''')),
 S('PD peritonitis',U('''Consider with cloudy effluent or abdominal pain. Diagnosis usually needs at least 2: compatible symptoms/cloudiness; effluent WBC >100/µL after ≥2-hour dwell with >50% neutrophils; positive culture.
 Obtain appropriate effluent testing/cultures and begin timely empiric coverage according to local protocol; intraperitoneal delivery is often preferred when suitable.
 Fungal, refractory or selected relapsing infections may require catheter removal. Do not assume a negative culture means no peritonitis.
 Distinguish exit-site/tunnel infection and noninfectious cloudy effluent. Preserve residual kidney function and reassess the dialysis plan after complications.'''))],[AKI,('NKF hemodialysis adequacy overview','https://www.kidney.org/kidney-topics/hemodialysis'),('ISPD peritonitis guideline, 2022','https://doi.org/10.1177/08968608221080586')])

def transplant():
 write('Nephrology','Kidney Transplantation',[
 S('Before transplantation',T('Assessment|Purpose','''ABO and HLA / crossmatch|Identify immunological incompatibility and donor-specific antibody risk
 Donor and recipient evaluation|Kidney quality, infection, malignancy, cardiovascular and surgical risks
 Living donation|Donor safety and independent assessment; benefit does not justify coercion
 Vaccination / infection screening|Prepare before immunosuppression where feasible
 Recurrent disease risk|Some glomerular/systemic diseases can recur in the graft''')),
 S('Graft dysfunction: timing guides but does not diagnose',T('Cause|Clues / assessment','''Vascular thrombosis or major surgical problem|Early abrupt dysfunction; urgent Doppler/imaging and surgical review
 Obstruction / leak|Imaging and urological assessment; pain may be absent in a denervated graft
 Ischemic tubular injury / delayed graft function|Early dysfunction; exclude vascular/obstructive and immune causes
 T-cell-mediated rejection|Biopsy classification; treatment differs from antibody-mediated rejection
 Antibody-mediated rejection|Integrate biopsy, donor-specific antibodies and other criteria; no single test alone fits all cases
 Drug toxicity, infection, recurrent disease|Levels, virology, urine and selected biopsy; do not label every creatinine rise rejection''')),
 S('Immunosuppression: compare classes',T('Drug class|Role|Major toxicity / interaction','''Calcineurin inhibitor: tacrolimus/ciclosporin|Core maintenance component in many regimens|Nephrotoxicity, hypertension, metabolic/neurotoxicity; CYP interactions; monitor levels
 Antimetabolite: mycophenolate|Maintenance|GI/marrow toxicity, infection; teratogenicity
 Azathioprine|Selected alternative|Marrow/hepatic toxicity; major interaction with xanthine-oxidase inhibitors
 Corticosteroid|Induction/rejection and selected maintenance|Infection, diabetes, bone and metabolic toxicity
 mTOR inhibitor|Selected maintenance strategies|Proteinuria, dyslipidemia, mouth ulcers, wound-healing problems
 Belatacept|Selected calcineurin-sparing therapy|EBV status and PTLD risk; not interchangeable for every recipient''')+U('''Acute rejection treatment follows biopsy category and severity; empiric management must still exclude urgent surgical and infectious causes.
 Rifampicin can reduce calcineurin-inhibitor exposure; azoles/macrolides can increase it. Review every new medicine and herbal product.''')),
 S('Infection and long-term care',U('''CMV risk depends on donor/recipient serostatus and immunosuppression; prophylaxis or pre-emptive monitoring is protocol-specific. Viral syndrome and tissue-invasive disease are distinct.
 BK polyomavirus: screen by protocol; graft infection is not treated by indiscriminately increasing immunosuppression. Immunosuppression reduction requires balanced rejection-risk assessment.
 Pneumocystis prophylaxis and vaccination schedules matter; avoid live vaccines during significant immunosuppression.
 Monitor malignancy, cardiovascular risk, diabetes, bone disease, proteinuria and recurrent kidney disease.
 Pregnancy requires planned graft/medication review; mycophenolate is contraindicated and must be changed under specialist guidance.
 A drug trough within target does not exclude every toxicity, and an isolated low level does not prove rejection.'''))],[TX,('International BK polyomavirus consensus, 2024','https://doi.org/10.1097/TP.0000000000004976')])

if __name__=='__main__':tubular();stones();dialysis();transplant()
