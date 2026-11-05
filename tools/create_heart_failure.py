"""Original topic-based Heart Failure chapter, authored directly in ChatGPT."""
from qbank_authoring import question, ref, finalize

HF=ref('2022 AHA/ACC/HFSA Guideline for the Management of Heart Failure','https://doi.org/10.1161/CIR.0000000000001063')
ESC=ref('2026 ESC Guidelines for the Management of Heart Failure','https://doi.org/10.1093/eurheartj/ehag100')
ECDP=ref('2024 ACC Expert Consensus Decision Pathway for Treatment of HFrEF','https://doi.org/10.1016/j.jacc.2023.12.024')
UPDATE=ref('2023 Focused Update of ESC Heart Failure Guidelines','https://doi.org/10.1093/eurheartj/ehad195')
ADVOR=ref('ADVOR: Acetazolamide in Acute Decompensated Heart Failure with Volume Overload','https://doi.org/10.1056/NEJMoa2203094')
FINE=ref('FINEARTS-HF: Finerenone in Heart Failure with Mildly Reduced or Preserved Ejection Fraction','https://doi.org/10.1056/NEJMoa2407107')
SUMMIT=ref('SUMMIT: Tirzepatide for Heart Failure with Preserved Ejection Fraction and Obesity','https://doi.org/10.1056/NEJMoa2410027')
rows=[]
def q(*args,**kwargs):rows.append(question(*args,**kwargs))

q('A symptomatic patient has LVEF 45% and objective evidence of increased LV filling pressure. Which ejection-fraction category best describes the heart failure?',
 'Heart failure with mildly reduced ejection fraction',[
 ('Heart failure with reduced ejection fraction','The conventional HFrEF category is LVEF 40% or less, not 45%.'),
 ('Heart failure with preserved ejection fraction','HFpEF generally requires LVEF at least 50% plus the relevant syndrome and objective evidence.'),
 ('Asymptomatic stage B disease solely because EF exceeds 40%','The patient is symptomatic; stage and EF phenotype are different classification axes.')],
 'Classifying HF by ejection fraction',
 '**An LVEF of 41-49% falls within HF with mildly reduced EF when the clinical HF syndrome is established.**',
 ['EF is a phenotype, not the entire diagnosis; symptoms and objective cardiac abnormalities matter.', 'For EF above 40%, evidence of elevated filling pressure supports the diagnosis and helps distinguish HF from noncardiac dyspnea.'],
 '**Do not confuse HF stage, symptom class and EF category.**',
 ['Stage C denotes current or previous symptomatic HF, while NYHA class describes functional limitation.', 'Measurement variability and change over time require reviewing prior studies rather than treating one percentage as immutable.'],
 [['LVEF at most 40%','HFrEF'],['LVEF 41-49%','HFmrEF'],['LVEF at least 50%','HFpEF when diagnostic criteria are met']], [HF,ESC], 'clinical_scenario')
q('Which finding best supports HFpEF in a patient with exertional dyspnea and LVEF 60% when resting investigations are inconclusive?',
 'Abnormally elevated left-sided filling pressure during exercise',[
 ('A preserved EF by itself','Normal EF does not establish HF; many patients with noncardiac dyspnea have preserved EF.'),
 ('Normal resting ECG as proof of diastolic heart failure','A normal ECG cannot establish elevated filling pressure or the HF syndrome.'),
 ('A small rise in heart rate during ordinary walking alone','Chronotropic responses are nonspecific and do not independently prove HFpEF.')],
 'Preserved EF does not mean normal filling physiology',
 '**HFpEF requires a compatible syndrome and objective evidence of cardiac dysfunction or raised filling pressure.**',
 ['Some patients have normal filling pressure at rest but a pathological rise with exercise.', 'Exercise echocardiography or invasive exercise hemodynamics can resolve selected intermediate-probability cases.'],
 '**Use testing to answer the unresolved physiological question.**',
 ['Assess competing explanations such as lung disease, anemia, obesity and deconditioning.', 'Left atrial enlargement, diastolic indices and natriuretic peptides contribute to probability but are interpreted in context.'],
 [['Preserved EF alone','Insufficient for HFpEF diagnosis'],['Raised exercise filling pressure with compatible symptoms','Supports HFpEF'],['Alternative noncardiac cause','Requires separate evaluation']], [HF,ESC])
q('An obese patient with exertional dyspnea and suspected HFpEF has a low-normal NT-proBNP. Which interpretation is most appropriate?',
 'Obesity can lower natriuretic peptide concentrations, so the result does not completely exclude HFpEF',[
 ('HFpEF is impossible whenever NT-proBNP is within the laboratory range','Natriuretic peptide sensitivity is imperfect, especially in obesity.'),
 ('Obesity invariably causes a markedly elevated NT-proBNP','The usual modifying effect is lower peptide concentrations for a given clinical burden.'),
 ('The result proves that filling pressures are normal during exercise','A resting biomarker is not a direct measurement of exercise filling pressure.')],
 'Natriuretic peptides require clinical context',
 '**A low peptide concentration reduces HF probability but is not an absolute exclusion in every phenotype.**',
 ['Obesity can suppress circulating BNP and NT-proBNP concentrations.', 'AF, increasing age and kidney dysfunction may raise peptide concentrations, creating different interpretive problems.'],
 '**Persistent clinical suspicion justifies appropriate cardiac assessment.**',
 ['Use echocardiography and, when needed, exercise-based evaluation in an inconclusive HFpEF presentation.', 'Do not diagnose HF solely from symptoms either: the low result should prompt careful reassessment of both cardiac and noncardiac causes.'],
 [['Obesity','May lower BNP and NT-proBNP'],['AF or CKD','May elevate concentrations'],['Uncertain HFpEF','Integrate imaging and selected functional testing']], [HF,ESC], 'clinical_scenario')
q('Soon after sacubitril/valsartan initiation, a stable patient has a modest BNP rise but a fall in NT-proBNP. Which mechanism best explains this pattern?',
 'Neprilysin inhibition affects BNP handling, whereas NT-proBNP is not a neprilysin substrate',[
 ('Sacubitril directly increases myocardial necrosis','An isolated BNP rise in this context does not establish myocardial necrosis.'),
 ('NT-proBNP is the peptide directly degraded by neprilysin','NT-proBNP is not the relevant neprilysin substrate.'),
 ('The two tests must move identically or one is analytically invalid','Drug effects and peptide biology can produce discordant short-term changes.')],
 'Interpreting biomarkers during ARNI treatment',
 '**Sacubitril inhibits neprilysin, altering degradation of biologically active peptides including BNP.**',
 ['BNP can rise early even as wall stress improves.', 'NT-proBNP is not a neprilysin substrate and often better reflects the change in myocardial stress soon after ARNI initiation.'],
 '**Treat the patient and interpret trends within the treatment context.**',
 ['Symptoms, weight, examination and renal function remain essential when assessing congestion.', 'BNP retains prognostic information; the drug effect does not make every later BNP rise meaningless.'],
 [['BNP after starting ARNI','May be influenced by neprilysin inhibition'],['NT-proBNP','Not directly degraded by neprilysin'],['Clinical deterioration','Requires assessment regardless of peptide explanation']], [HF,ECDP], 'clinical_scenario')
q('A patient with dilated cardiomyopathy improves from LVEF 28% to 55% on HFrEF therapy and is asymptomatic. What is the preferred approach to disease-modifying treatment?',
 'Continue guideline-directed therapy to reduce relapse risk',[
 ('Stop all HF drugs because EF has normalized','Improvement often represents remission rather than permanent cure; withdrawal can lead to relapse.'),
 ('Continue only a loop diuretic irrespective of volume status','Diuretics control congestion but do not replace disease-modifying treatment.'),
 ('Replace the regimen with aspirin alone','Aspirin is not a substitute for treatment of the underlying cardiomyopathy and has no universal HF indication.')],
 'HF with improved EF usually represents remission',
 '**Recovered ventricular function does not establish that the substrate for HF has disappeared.**',
 ['Continue the disease-modifying HFrEF regimen in HF with improved EF when tolerated.', 'Diuretic requirements can be reassessed according to congestion, separately from the neurohormonal and disease-modifying drugs.'],
 '**Explain relapse prevention when reviewing long-term adherence.**',
 ['Improvement is often the result of the therapy that the patient now wishes to stop.', 'A new treatment-limiting adverse effect merits individual adjustment, not a blanket assumption that all therapy is unnecessary.'],
 [['Improved EF on therapy','Continue disease-modifying treatment'],['No residual congestion','Reassess diuretic dose'],['Treatment intolerance','Adjust the specific regimen with monitoring']], [HF,ECDP], 'clinical_scenario')
q('Which regimen contains the four foundational disease-modifying drug classes for eligible patients with HFrEF?',
 'ARNI or ACE inhibitor/ARB, an evidence-based beta blocker, an MRA and an SGLT2 inhibitor',[
 ('Loop diuretic, digoxin, nitrate and aspirin','These drugs do not constitute the four foundational disease-modifying HFrEF classes.'),
 ('ACE inhibitor plus ARB plus ARNI plus beta blocker','Combining these overlapping renin-angiotensin pathway drugs is inappropriate and increases adverse effects.'),
 ('Beta blocker, verapamil, diltiazem and digoxin','Multiple rate-slowing drugs are not the foundational regimen, and non-DHP CCBs can worsen systolic HF.')],
 'The four pillars of HFrEF treatment',
 '**Use complementary drug classes that modify different pathways rather than stacking drugs from the same pathway.**',
 ['Renin-angiotensin pathway inhibition, evidence-based beta blockade, mineralocorticoid receptor blockade and SGLT2 inhibition form the core regimen.', 'An ARNI is generally preferred when appropriate; ACE inhibitor or ARB is an alternative when the ARNI cannot be used.'],
 '**Congestion management and selected add-on treatments remain important but serve different roles.**',
 ['Loop diuretics relieve fluid overload and help achieve stability for other treatment.', 'Individual contraindications, renal function, potassium, pressure and tolerability guide initiation and titration.'],
 [['Foundational therapies','Improve important HF outcomes'],['Loop diuretics','Relieve congestion'],['Selected add-ons','Address residual indications after core therapy']], [HF,ECDP])
q('A stable, newly diagnosed HFrEF patient is eligible for all four foundational drug classes. Which implementation strategy best reflects the 2024 ACC consensus pathway?',
 'Start low doses of the complementary classes early and titrate promptly as tolerated rather than completing one drug before adding the next',[
 ('Reach the maximal beta-blocker dose before considering any other class','A serial one-drug-at-a-time approach can delay exposure to other effective therapies for months.'),
 ('Delay all disease-modifying drugs until EF is rechecked six months later','The initial diagnosis is the time to establish effective therapy, not to defer it without a contraindication.'),
 ('Use only a loop diuretic until the patient has been admitted twice','Waiting for recurrent deterioration misses a major opportunity for prevention.')],
 'Early exposure to complementary HFrEF therapies',
 '**Benefit begins before every drug reaches its target dose.**',
 ['Early introduction of the four classes can provide complementary protection.', 'The ACC pathway supports rapid initiation and titration toward maximally tolerated doses, when feasible within about three months.'],
 '**Sequence is individualized to physiology rather than a rigid universal order.**',
 ['Volume status, pressure, heart rate, potassium and kidney function determine what can be started safely.', 'Use frequent reassessment to address adverse effects and avoid leaving a patient indefinitely on starter doses.'],
 [['Eligible stable patient','Introduce complementary low-dose therapies early'],['Congestion or shock','Stabilize and tailor timing'],['Follow-up','Titrate and monitor tolerance']], [ECDP], 'clinical_scenario')
q('A symptomatic HFrEF patient is being considered for spironolactone under the 2022 AHA/ACC/HFSA guideline. Which baseline values satisfy the usual initiation criteria?',
 'eGFR 42 mL/min/1.73 m² and potassium 4.6 mmol/L',[
 ('eGFR 22 mL/min/1.73 m² and potassium 4.6 mmol/L','This eGFR is below the usual greater-than-30 threshold for initiating a steroidal MRA in the specified guideline.'),
 ('eGFR 42 mL/min/1.73 m² and potassium 5.5 mmol/L','This baseline potassium is too high for routine initiation.'),
 ('eGFR 28 mL/min/1.73 m² and potassium 5.3 mmol/L','Both renal function and potassium are unfavorable for routine initiation under these criteria.')],
 'MRA eligibility and monitoring in HFrEF',
 '**The specified guideline recommends initiation when eGFR is greater than 30 and potassium is below 5.0.**',
 ['Spironolactone and eplerenone reduce morbidity and mortality in eligible symptomatic HFrEF.', 'Their potassium-retaining effect requires baseline and repeat monitoring after initiation and dose changes.'],
 '**A suitable baseline does not guarantee continued safety.**',
 ['Reassess during intercurrent illness, renal deterioration or changes in interacting drugs.', 'Avoid unnecessary potassium supplementation and review NSAIDs or other contributors to hyperkalemia.'],
 [['Adequate eGFR and K below 5.0','Potential candidate with monitoring'],['Hyperkalemia or severe renal impairment','Correct contributors and reassess eligibility']], [HF])
q('A patient is switching from enalapril to sacubitril/valsartan. What minimum interval is required after the last ACE inhibitor dose?',
 'At least 36 hours',[
 ('No interval if the first ARNI dose is low','Dose reduction does not remove the angioedema risk from overlapping ACE and neprilysin inhibition.'),
 ('Six hours','This is shorter than the required ACE inhibitor washout.'),
 ('Two hours after the next meal','Food timing does not determine the necessary washout interval.')],
 'ACE inhibitor washout before ARNI',
 '**A 36-hour washout reduces the risk of angioedema from overlapping ACE and neprilysin inhibition.**',
 ['Both pathways influence bradykinin metabolism.', 'Do not administer an ACE inhibitor together with sacubitril/valsartan.'],
 '**Check the actual last dose rather than the intended prescription change date.**',
 ['The same 36-hour separation is relevant when switching back from ARNI to an ACE inhibitor.', 'An ARB does not require this ACE-specific washout, but sacubitril/valsartan already contains an ARB and should not be combined with another.'],
 [['ACE inhibitor to ARNI','At least 36-hour separation'],['ARNI plus ACE inhibitor','Do not combine'],['ARNI plus another ARB','Avoid duplicate ARB treatment']], [HF,ECDP], 'clinical_scenario')
q('A patient with HFrEF previously developed unequivocal ACE inhibitor-associated angioedema. Which statement about sacubitril/valsartan is correct?',
 'It should not be used in this patient because of the angioedema history',[
 ('It is safe after a 36-hour washout irrespective of prior angioedema','The washout addresses overlap; it does not negate a contraindicating angioedema history.'),
 ('It becomes safe if combined with an ACE inhibitor','Combining the drugs increases risk and is contraindicated.'),
 ('A prophylactic antihistamine reliably removes the risk','Antihistamine prophylaxis does not make bradykinin-mediated angioedema risk acceptable.')],
 'Washout and prior angioedema are different safety questions',
 '**An appropriate washout does not override a history of ACE inhibitor-related angioedema.**',
 ['Review the nature of the previous reaction and relevant drug history.', 'ARNI is not appropriate in this documented setting; an alternative HF regimen must be selected.'],
 '**Preserve other tolerated disease-modifying therapies.**',
 ['Assess ARB use or hydralazine-isosorbide dinitrate according to the individual risk profile and guideline context.', 'Do not abandon beta blockade, MRA or SGLT2 treatment solely because ARNI cannot be used.'],
 [['Recent ACE inhibitor use without prior angioedema','Washout required before ARNI'],['Documented ACE inhibitor-related angioedema','Avoid ARNI']], [HF], 'clinical_scenario')
q('A beta-blocker-naive patient is admitted with pulmonary edema, cold extremities and cardiogenic shock requiring intravenous inotropic support. When should a disease-modifying beta blocker generally be initiated?',
 'After stabilization and resolution of shock, when perfusion and volume status permit',[
 ('Immediately at a high dose to counter the tachycardia','Acute negative inotropy can worsen shock and low output.'),
 ('Only after a second shock admission','A second admission is not required; treatment should begin once it can be tolerated safely.'),
 ('Never, because any history of decompensation permanently contraindicates beta blockers','Stable HFrEF patients commonly benefit from evidence-based beta blockers after recovery.')],
 'Beta blockers improve chronic outcomes but can worsen active shock',
 '**Initiate beta blockade in a clinically stable state rather than during ongoing inotrope-dependent hypoperfusion.**',
 ['The immediate priorities are perfusion, precipitant treatment and relief of congestion.', 'Use evidence-based agents such as carvedilol, bisoprolol or sustained-release metoprolol succinate once suitable.'],
 '**Distinguish starting treatment from managing a patient already taking it.**',
 ['Continuation or temporary adjustment of an existing beta blocker depends on shock, bradycardia and other clinical factors.', 'After stabilization, begin at a low dose and titrate with monitoring rather than omitting the class indefinitely.'],
 [['Active shock on inotrope','Do not newly initiate beta blockade'],['Stable, adequately perfused recovery','Start low-dose evidence-based therapy']], [HF,ECDP], 'clinical_scenario')
q('A patient with symptomatic HFrEF has no diabetes and an HbA1c of 5.5%. Which statement about dapagliflozin or empagliflozin is correct?',
 'SGLT2 inhibition can improve HF outcomes even without diabetes',[
 ('Treatment is indicated only if HbA1c exceeds 6.5%','The HF indication is not dependent on a diabetes diagnosis.'),
 ('The drug has no role unless insulin is already prescribed','Insulin use is not required for HF benefit.'),
 ('It can replace all other foundational HFrEF classes','SGLT2 inhibitors complement rather than replace the other tolerated foundational therapies.')],
 'SGLT2 inhibitors are HF drugs as well as glucose-lowering drugs',
 '**HF benefits extend to patients without type 2 diabetes.**',
 ['The clinical effects are not explained simply by lowering an elevated HbA1c.', 'Check the specific agent\'s renal criteria, volume status and contraindications before treatment.'],
 '**Provide practical counseling along with the prescription.**',
 ['Discuss genital infections, volume depletion and sick-day or perioperative withholding when appropriate.', 'Acute severe illness or prolonged fasting can increase ketoacidosis risk even when glucose is not markedly elevated.'],
 [['HFrEF with diabetes','Eligible for HF benefit if otherwise suitable'],['HFrEF without diabetes','Also eligible for HF benefit'],['Acute illness or fasting','Review temporary withholding and ketosis risk']], [HF,ESC])
q('Two weeks after starting an SGLT2 inhibitor, a stable euvolemic HFrEF patient has an eGFR change from 62 to 56 mL/min/1.73 m² without hypotension or other abnormalities. What is the most appropriate interpretation?',
 'A small early hemodynamic eGFR dip can occur; reassess clinically rather than automatically stopping treatment',[
 ('Any eGFR decline proves irreversible drug-induced tubular necrosis','A small early dip is not equivalent to structural acute kidney injury.'),
 ('Double the loop diuretic automatically','A euvolemic patient does not require additional diuresis solely because eGFR fell modestly.'),
 ('Ignore all future renal monitoring','An expected pattern does not eliminate the need to monitor for genuine injury or volume depletion.')],
 'Early renal changes during SGLT2 treatment',
 '**An initial modest eGFR reduction may reflect a change in glomerular hemodynamics.**',
 ['The long-term kidney trajectory can still be favorable.', 'A larger decline or accompanying hypotension, dehydration or illness warrants a more detailed evaluation.'],
 '**Assess volume and interacting treatment before changing therapy.**',
 ['Review diuretic dose, oral intake and nephrotoxic exposure.', 'In this stable example, monitoring is more appropriate than reflex permanent discontinuation.'],
 [['Small early dip, stable clinical state','Reassess and monitor'],['Progressive decline with hypovolemia or illness','Investigate and adjust treatment']], [ECDP,ESC], 'clinical_scenario')
q('Which statement most accurately describes loop diuretics in chronic heart failure?',
 'They relieve congestion and symptoms, while disease-modifying therapies provide the established foundational outcome benefits',[
 ('They replace the need for neurohormonal treatment once edema resolves','A patient can be euvolemic and still require disease-modifying therapy.'),
 ('The highest possible dose should be continued indefinitely regardless of volume status','Overdiuresis can cause hypotension, electrolyte disturbance and renal dysfunction.'),
 ('They should never be used in HFpEF','Congestion in HFpEF also requires appropriate diuretic treatment.')],
 'Decongestion and disease modification are complementary',
 '**Loop diuretics are central to treating fluid overload.**',
 ['They inhibit sodium reabsorption in the thick ascending limb and increase natriuresis.', 'Dose and route depend on congestion, kidney function, prior exposure and response.'],
 '**Aim for adequate decongestion with the lowest effective maintenance requirement.**',
 ['Track symptoms, weight, examination, electrolytes and renal function.', 'Do not assume symptom relief alone means the long-term HF substrate has been treated.'],
 [['Congestion','Loop diuretic adjusted to response'],['Long-term HFrEF risk','Foundational disease-modifying regimen'],['Euvolemia','Reassess maintenance dose']], [HF,ESC])
q('A volume-overloaded patient has an inadequate response to appropriately dosed intravenous loop diuretic despite adherence and exclusion of obstruction. Which strategy can overcome distal nephron sodium retention?',
 'Add a thiazide-type diuretic for sequential nephron blockade with close electrolyte and renal monitoring',[
 ('Add an NSAID to increase natriuresis','NSAIDs can impair renal perfusion and blunt the diuretic response.'),
 ('Stop all diuretics because resistance proves the edema is noncardiac','An inadequate response does not exclude cardiac congestion.'),
 ('Add potassium supplementation regardless of the serum concentration','Potassium replacement should follow measured need, not a blanket rule, particularly with interacting HF drugs.')],
 'Sequential nephron blockade',
 '**Chronic loop exposure can promote compensatory sodium reabsorption downstream.**',
 ['A thiazide-type agent such as metolazone can block a complementary nephron site.', 'Combination treatment increases the risk of hypokalemia, hyponatremia, volume depletion and renal deterioration.'],
 '**Confirm adequate loop delivery and assess response before escalating.**',
 ['Gut edema, renal impairment, sodium intake and NSAID exposure can contribute to poor response.', 'Use repeated clinical and laboratory review rather than leaving combination treatment unchanged without monitoring.'],
 [['Loop diuretic','Thick ascending limb blockade'],['Thiazide-type add-on','Distal sodium transport blockade'],['Combination','Greater natriuresis with greater electrolyte risk']], [HF,ESC], 'clinical_scenario')
q('What did the ADVOR trial primarily demonstrate about adding intravenous acetazolamide to standardized loop diuretic therapy in acute HF with volume overload?',
 'A higher rate of successful early decongestion',[
 ('A proven reduction in all-cause mortality as the primary finding','ADVOR was primarily a decongestion trial and did not establish a mortality benefit.'),
 ('Elimination of the need for loop diuretics','Acetazolamide was added to loop treatment rather than replacing it.'),
 ('A requirement to use acetazolamide chronically in every euvolemic HF patient','The acute volume-overload trial does not establish this blanket long-term indication.')],
 'Acetazolamide as an acute decongestive adjunct',
 '**Proximal tubular carbonic anhydrase inhibition complements loop diuresis.**',
 ['Acetazolamide increases proximal sodium and bicarbonate loss.', 'ADVOR showed more successful decongestion with the add-on strategy in the studied acute HF population.'],
 '**Do not convert a decongestion endpoint into an unsupported survival claim.**',
 ['Assess renal function, acid-base status and electrolytes when considering treatment.', 'Study eligibility and concomitant treatment matter when extrapolating to a different patient.'],
 [['ADVOR intervention','Acetazolamide plus standardized IV loop diuretic'],['Established primary benefit','Successful early decongestion'],['Not established by the trial','Universal chronic use or mortality benefit']], [ADVOR])
q('During intravenous diuresis for marked HF congestion, a patient loses edema and breathlessness, remains well perfused and has a creatinine rise from 1.2 to 1.4 mg/dL. JVP remains elevated. What is the best next interpretation?',
 'A modest creatinine rise during effective decongestion requires context and does not automatically mandate stopping diuresis',[
 ('Stop all decongestive treatment immediately regardless of residual congestion','Residual congestion carries risk, and a small creatinine rise must be interpreted alongside perfusion and response.'),
 ('Give intravenous saline solely to normalize the creatinine','Saline can worsen persistent volume overload and is not indicated by the number alone.'),
 ('Diagnose irreversible renal failure without further assessment','A small dynamic change during treatment does not establish irreversible failure.')],
 'Creatinine and congestion must be assessed together',
 '**Changes in filtration during diuresis do not always represent intrinsic structural kidney injury.**',
 ['Venous congestion itself can impair kidney function.', 'Blood pressure, perfusion, urine output, electrolyte changes and the magnitude and trajectory of creatinine inform the decision.'],
 '**Avoid both overdiuresis and premature acceptance of persistent congestion.**',
 ['The described improvement and preserved perfusion support continued individualized reassessment.', 'Hypotension, progressive oliguria or a substantial continuing renal decline would require a different evaluation.'],
 [['Modest rise with improving congestion and preserved perfusion','Monitor and individualize ongoing decongestion'],['Rise with shock or severe volume depletion','Investigate hypoperfusion and adjust treatment']], [HF,ECDP], 'clinical_scenario')
q('A patient presents with acute pulmonary edema and blood pressure 210/115 mm Hg. There is no shock, recent PDE5 inhibitor use or severe aortic stenosis. Alongside respiratory support and appropriate diuresis, which treatment addresses the prominent hemodynamic problem?',
 'A titratable intravenous vasodilator such as nitroglycerin',[
 ('Routine fluid boluses to raise preload','The presentation suggests high filling pressures and severe hypertension, not a need for reflex fluid loading.'),
 ('Immediate high-dose beta-blocker initiation despite respiratory instability','New aggressive beta blockade is not the immediate treatment for acute unstable pulmonary edema.'),
 ('Dobutamine solely because pulmonary edema is present','An inotrope is not routinely indicated in a severely hypertensive patient without hypoperfusion.')],
 'Hypertensive acute HF often involves fluid redistribution and excessive afterload',
 '**Vasodilation can rapidly reduce cardiac loading conditions when blood pressure permits.**',
 ['Nitroglycerin reduces venous tone and, at higher doses, arterial loading.', 'Monitor pressure and avoid precipitous hypotension or use in contraindicated settings.'],
 '**Treat oxygenation, congestion and the precipitating cause simultaneously.**',
 ['Noninvasive ventilatory support is appropriate when respiratory distress warrants it.', 'Investigate ischemia, medication interruption and other triggers rather than treating the blood pressure in isolation.'],
 [['Pulmonary edema with severe hypertension','Consider titratable vasodilation'],['HF with hypotensive hypoperfusion','Assess shock and perfusion support']], [HF,ESC], 'clinical_scenario')
q('A conscious, cooperative patient with cardiogenic pulmonary edema has severe respiratory distress and hypoxemia despite supplemental oxygen, with adequate blood pressure and no vomiting. Which escalation is appropriate?',
 'Noninvasive positive-pressure ventilation with close monitoring',[
 ('Sedation alone without ventilatory support','Sedation can impair airway protection and does not correct the underlying gas-exchange problem.'),
 ('High-flow oxygen indefinitely despite worsening fatigue','Escalating respiratory failure requires reassessment and may need positive-pressure support or intubation.'),
 ('Noninvasive ventilation even if the patient becomes unable to protect the airway','Loss of airway protection or other NIV contraindications requires a different airway strategy.')],
 'Positive pressure in acute cardiogenic pulmonary edema',
 '**NIV can improve oxygenation and reduce respiratory work in an appropriate patient.**',
 ['Positive intrathoracic pressure can also reduce cardiac preload and afterload.', 'Adequate cooperation and airway protection are essential; monitor hemodynamics because positive pressure can lower venous return.'],
 '**NIV is a monitored treatment trial, not a substitute for recognizing failure.**',
 ['Worsening mental status, refractory hypoxemia or exhaustion may require intubation.', 'Continue treatment of congestion and the cardiac precipitant during respiratory support.'],
 [['Cooperative patient with distress and adequate pressure','Consider NIV'],['Airway compromise or NIV failure','Evaluate invasive ventilation'],['Hypotension or RV-predominant failure','Use positive pressure with particular caution']], [ESC,HF], 'clinical_scenario')
q('A patient with acute HFrEF has cool extremities, oliguria, lactate elevation and persistent hypotension despite assessment and correction of reversible filling problems. What is the appropriate role of intravenous inotropic therapy?',
 'Short-term support may be used for low-output hypoperfusion while treating the cause and assessing advanced support',[
 ('Routine long-term use in every stable HFrEF patient','Chronic inotropic exposure is not routine outcome-improving therapy for stable HFrEF.'),
 ('Use solely to normalize EF in a warm, well-perfused patient','An EF value alone is not an indication for an inotrope.'),
 ('Replace urgent evaluation for ischemia or mechanical complications','Hemodynamic support must not delay treatment of a reversible cause of shock.')],
 'Inotropes are targeted perfusion support',
 '**Clinical hypoperfusion, not just a low EF, defines the need to consider inotropic support.**',
 ['Tachyarrhythmia, ischemia and increased myocardial oxygen demand are important treatment risks.', 'Agent selection depends on blood pressure, rhythm, kidney function and the overall shock phenotype; a vasopressor may also be required.'],
 '**Use support as a bridge to recovery, a definitive intervention or an advanced-therapy decision.**',
 ['Identify ACS, arrhythmia, infection and structural complications promptly.', 'Escalate to a shock team and selected temporary mechanical support when medical stabilization is inadequate.'],
 [['Cold hypoperfusion with hypotension','Consider targeted vasoactive support'],['Warm congestion without hypoperfusion','Decongestion rather than routine inotrope'],['Persistent shock','Assess reversible causes and advanced support']], [HF,ESC], 'clinical_scenario')
q('Which HF patient is most likely to benefit from invasive hemodynamic assessment rather than routine pulmonary artery catheterization of all admissions?',
 'A patient with persistent shock and uncertain filling pressures or cardiac output despite initial assessment',[
 ('Every stable euvolemic outpatient at each visit','Routine invasive monitoring is not recommended for clinically stable patients.'),
 ('Every patient with an isolated high BNP regardless of symptoms','A biomarker concentration alone is not a sufficient indication for pulmonary artery catheterization.'),
 ('An asymptomatic patient solely to confirm an already clear normal examination','The procedure should answer a meaningful unresolved clinical question.')],
 'Use invasive hemodynamics selectively',
 '**A pulmonary artery catheter can clarify uncertain physiology when the result will change treatment.**',
 ['Measurements can distinguish filling-pressure abnormalities, cardiac output and vascular resistance.', 'Persistent shock, complex right-sided failure and advanced-therapy assessment are examples of selected indications.'],
 '**Routine use in every HF admission is not supported.**',
 ['Balance the expected information against procedural risks and interpretation limitations.', 'Integrate invasive numbers with examination, echocardiography and the patient\'s trajectory.'],
 [['Clear stable congestion responding to treatment','Usually manage without routine catheterization'],['Shock with unresolved hemodynamics','Consider invasive assessment']], [HF,ESC])
q('A patient has confirmed symptomatic HFpEF without diabetes. Which medication class has strong randomized evidence for reducing HF events across preserved-EF populations?',
 'SGLT2 inhibitors such as empagliflozin or dapagliflozin',[
 ('Routine long-acting nitrates for every HFpEF patient','Nitrates have not demonstrated routine functional or outcome benefit in unselected HFpEF.'),
 ('Digoxin as mandatory mortality-reducing therapy for all HFpEF','A universal mortality benefit has not been established.'),
 ('Nonselective beta blockade solely because EF is preserved','Beta blockers may have separate indications but are not a universal HFpEF disease-modifying requirement.')],
 'SGLT2 benefit is not confined to HFrEF',
 '**SGLT2 inhibition reduces HF events in eligible HFpEF patients, including those without diabetes.**',
 ['The benefit is particularly clear for prevention of HF worsening and hospitalization.', 'Other therapies and comorbidity treatment remain important; the absence of diabetes does not remove the indication.'],
 '**Treat the phenotype and its associated burdens.**',
 ['Relieve congestion, control blood pressure and assess AF, obesity, ischemia and kidney disease.', 'Current ESC guidance also incorporates MRA therapy across EF, with appropriate renal and potassium assessment.'],
 [['SGLT2 inhibitor','Evidence-based reduction in HF events'],['Diuretic','Relieves congestion'],['Comorbidity treatment','Addresses important HFpEF drivers']], [UPDATE,ESC], 'clinical_scenario')

# The second half covers current HFpEF evidence, add-on therapy, devices and advanced HF.
q('Which statement reflects an important change in the 2026 ESC HF guideline compared with older EF-restricted treatment frameworks?',
 'MRA therapy is recommended for eligible symptomatic HF patients across the EF spectrum, with renal and potassium precautions',[
 ('MRAs are now contraindicated whenever EF is at least 50%','The updated ESC framework extends rather than prohibits MRA use across EF.'),
 ('SGLT2 inhibitors should be stopped if EF improves above 40%','The updated framework supports their use across EF, not withdrawal at this boundary.'),
 ('Every HF drug has identical mortality evidence at every EF','Drug recommendations and composite-endpoint benefits do not imply identical mortality evidence in all phenotypes.')],
 'Current HF guidance extends beyond an HFrEF-only model',
 '**The 2026 ESC guideline recommends MRAs and SGLT2 inhibitors for symptomatic HF across LVEF categories when appropriate.**',
 ['This reflects evidence accumulated in mildly reduced and preserved EF populations.', 'The MRA evidence base differs by phenotype: steroidal MRAs have established HFrEF evidence, while finerenone contributes important higher-EF data.'],
 '**A broad recommendation still requires individual eligibility checks.**',
 ['Assess potassium, kidney function, interactions and the evidence for the selected agent.', 'Do not claim that each drug independently reduces all-cause mortality in every EF group merely because a composite HF endpoint improves.'],
 [['Older HFrEF evidence','Strong steroidal MRA morbidity and mortality evidence'],['Higher-EF evidence','Includes finerenone and composite HF-event benefit'],['All eligible patients','Require safety assessment and monitoring']], [ESC,FINE])
q('What was the principal outcome finding of FINEARTS-HF in patients with LVEF at least 40%?',
 'Finerenone reduced the composite rate of total worsening HF events and cardiovascular death',[
 ('Finerenone proved a significant reduction in every mortality endpoint separately','A positive composite does not prove that each component or all-cause mortality is independently reduced.'),
 ('Finerenone eliminated hyperkalemia risk because it is nonsteroidal','Nonsteroidal structure does not eliminate potassium retention or the need for monitoring.'),
 ('The trial tested finerenone as an emergency inotrope in shock','The trial studied chronic HF outcomes, not acute inotropic support.')],
 'Interpreting finerenone evidence accurately',
 '**FINEARTS-HF supports finerenone in a higher-EF HF population through reduction of a composite HF outcome.**',
 ['The endpoint combined total worsening HF events with cardiovascular death.', 'Avoid interpreting a composite result as proof of a statistically significant effect on every component separately.'],
 '**The mechanism remains mineralocorticoid receptor antagonism.**',
 ['Renal function and potassium influence suitability and follow-up.', 'Do not combine multiple MRAs indiscriminately; adding finerenone to spironolactone is not the intervention established by this trial.'],
 [['Studied phenotype','HF with mildly reduced or preserved EF'],['Established trial finding','Reduced composite total worsening HF events and CV death'],['Safety issue','Hyperkalemia monitoring remains necessary']], [FINE,ESC])
q('An obese patient with confirmed HFpEF remains limited despite appropriate HF care. Which statement best reflects evidence from SUMMIT and the 2026 ESC update?',
 'Tirzepatide can be considered for the obesity-related HFpEF phenotype, with benefits in health status and worsening HF outcomes',[
 ('Tirzepatide replaces diuretics even during acute pulmonary edema','Obesity-directed therapy is not an emergency decongestive substitute.'),
 ('The evidence establishes treatment for every form of HF regardless of body size or EF','The trial population and recommendation are phenotype specific.'),
 ('Weight reduction has no role once HFpEF is diagnosed','Obesity is an important treatable contributor to HFpEF symptoms and physiology.')],
 'Treating the obesity-HFpEF phenotype',
 '**Obesity-directed incretin therapy has evidence beyond weight loss alone in selected HFpEF populations.**',
 ['SUMMIT found a lower risk of cardiovascular death or worsening HF and improved health status with tirzepatide in HFpEF with obesity.', 'The 2026 ESC guideline includes consideration of semaglutide or tirzepatide for preserved-EF HF with obesity.'],
 '**Integrate phenotype treatment with ongoing HF care.**',
 ['Assess nutritional status, tolerability, contraindications and access while preserving muscle and functional capacity.', 'Continue appropriate congestion and comorbidity management; the trial does not establish a replacement for all HF medications.'],
 [['HFpEF with obesity','Evidence-supported phenotype for incretin-based consideration'],['Acute pulmonary edema','Immediate respiratory and decongestive treatment'],['Nonobese or different HF phenotype','Do not assume identical trial evidence']], [SUMMIT,ESC], 'clinical_scenario')
q('A symptomatic HFrEF patient has hemoglobin 12.8 g/dL, ferritin 72 ng/mL and transferrin saturation 16%. Which statement about iron treatment is most appropriate?',
 'Iron deficiency can be present without marked anemia, and intravenous iron may improve symptoms and reduce HF hospitalization in eligible patients',[
 ('Iron deficiency is excluded because hemoglobin is not severely low','Hemoglobin and iron availability measure different problems; iron deficiency can occur without substantial anemia.'),
 ('Oral iron has equivalent proven HF benefits to intravenous iron in all patients','The major HF outcome and functional evidence is for specific intravenous formulations, not equivalence of all oral preparations.'),
 ('Intravenous iron guarantees a reduction in all-cause mortality','The evidence supports symptom, functional and HF-event benefits rather than this universal mortality guarantee.')],
 'Iron deficiency is a separate therapeutic target',
 '**Assess iron stores and availability rather than using hemoglobin alone.**',
 ['The conventional HF trial definition includes ferritin below 100 ng/mL, or ferritin 100-299 with TSAT below 20%.', 'Ferritin is an acute-phase reactant; TSAT adds information about iron available to tissues.'],
 '**Use the evidence-supported intravenous formulation in an eligible symptomatic patient.**',
 ['Ferric carboxymaltose and ferric derisomaltose have HF-specific evidence.', 'Investigate the cause of deficiency and monitor response rather than treating an unexplained deficiency indefinitely.'],
 [['Normal or mildly low hemoglobin with low iron indices','Iron deficiency may still be important'],['IV iron in eligible symptomatic HF','Can improve symptoms and reduce HF hospitalization'],['Oral iron','Does not have equivalent established HF evidence']], [UPDATE,ESC], 'clinical_scenario')
q('A stable patient with LVEF 30% has NYHA II symptoms despite GDMT, including the maximally tolerated beta blocker. Sinus rhythm persists at 82/min. Which additional treatment specifically targets the sinus-node If current?',
 'Ivabradine',[
 ('Digoxin','Digoxin has different electrophysiological and inotropic actions; it does not selectively inhibit the sinus-node If current.'),
 ('Verapamil','Verapamil is a non-DHP CCB and is not an appropriate substitute in systolic HF.'),
 ('Amiodarone solely to lower an otherwise normal sinus rhythm','Antiarrhythmic toxicity is not justified as routine sinus-rate treatment in this setting.')],
 'Selecting ivabradine for the correct rhythm and phenotype',
 '**Ivabradine slows sinus-node firing without beta-receptor blockade.**',
 ['The 2022 guideline supports selected symptomatic stable HFrEF patients with EF at most 35%, sinus rhythm and resting rate at least 70 despite maximally tolerated beta blockade.', 'It is not effective as a ventricular rate-control strategy in AF because the sinus node is not driving that rhythm.'],
 '**Optimize foundational treatment before using a selected add-on.**',
 ['Confirm adherence and exclude reversible causes of tachycardia such as infection, anemia or congestion.', 'Monitor for bradycardia and AF; do not assume a low starting beta-blocker dose is already maximally tolerated without assessment.'],
 [['Sinus rhythm with qualifying persistent tachycardia','Potential ivabradine candidate'],['Atrial fibrillation','Not an If-based ventricular rate-control indication']], [HF], 'clinical_scenario')
q('A self-identified Black patient has persistent NYHA III HFrEF symptoms despite appropriate foundational therapy. Which add-on regimen has evidence in this clinical context?',
 'Hydralazine plus isosorbide dinitrate',[
 ('Hydralazine alone as an equivalent tested substitute','The evidence-based HF regimen is the combination, not a claim of equivalence for hydralazine monotherapy.'),
 ('Isosorbide mononitrate plus sildenafil','A nitrate-PDE5 inhibitor combination can cause severe hypotension and is not the evidence-based regimen.'),
 ('A second ACE inhibitor added to an ARNI','Overlapping ACE and neprilysin inhibition is contraindicated and does not represent additive foundational therapy.')],
 'Hydralazine-isosorbide dinitrate in selected HFrEF',
 '**The combination provides complementary arterial and venous vasodilation.**',
 ['It has evidence as add-on treatment in self-identified Black patients with persistent NYHA III-IV HFrEF on appropriate therapy.', 'It can also be considered in selected patients unable to receive renin-angiotensin pathway inhibitors because of intolerance or contraindication.'],
 '**Preserve tolerated foundational therapy and monitor treatment burden.**',
 ['Headache, hypotension, dosing frequency and hydralazine-related adverse effects can limit adherence.', 'The trial-defined population guides this recommendation; self-identified race should not be treated as a complete biological explanation of HF.'],
 [['Persistent symptomatic eligible HFrEF','Consider the combination as an add-on'],['RAS inhibitor cannot be used','Selected alternative vasodilator pathway'],['Nitrate treatment','Avoid PDE5 inhibitor interaction']], [HF], 'clinical_scenario')
q('Which statement best describes digoxin in symptomatic HFrEF despite appropriate therapy?',
 'It may reduce HF hospitalization in selected patients, but a mortality benefit has not been established',[
 ('It is a foundational mortality-reducing substitute for an SGLT2 inhibitor','Digoxin is a selected add-on, not a replacement for a foundational class.'),
 ('Renal function has little effect on toxicity risk','Renal clearance, age, interactions and electrolyte abnormalities influence toxicity.'),
 ('Higher serum levels are always better for long-term outcomes','Digoxin has a narrow therapeutic window; excessive concentrations can cause serious arrhythmias.')],
 'Digoxin has a limited, specific role',
 '**Use digoxin for selected persistent symptoms or other appropriate indications with a clear monitoring plan.**',
 ['The main HF evidence supports reduced hospitalization rather than improved survival.', 'Inhibition of Na/K ATPase and vagotonic effects contribute to its actions.'],
 '**Dose conservatively and review toxicity risks.**',
 ['Kidney impairment, hypokalemia and interacting drugs increase risk.', 'Nausea, visual symptoms, bradyarrhythmia and ventricular arrhythmia may indicate toxicity; interpret a level at an appropriate interval after dosing.'],
 [['Potential benefit','Fewer HF hospitalizations in selected patients'],['Major limitation','Narrow therapeutic window'],['Monitoring','Kidney function, electrolytes, interactions and selected levels']], [HF])
q('A patient with LVEF 28% has a recent worsening-HF hospitalization despite GDMT and is now stable. Which statement about vericiguat is correct?',
 'It is a soluble guanylate cyclase stimulator that may be considered in selected high-risk patients after worsening HF',[
 ('It is a loop diuretic that replaces congestion assessment','Vericiguat works through nitric oxide-sGC signaling, not loop sodium transport.'),
 ('It must replace all four foundational drug classes','It is a selected additional therapy rather than a replacement for tolerated foundational treatment.'),
 ('It is first-line treatment for every patient with isolated hypertension','Its HF use concerns a selected worsening-HFrEF population, not routine isolated hypertension.')],
 'An add-on for selected recently worsening HFrEF',
 '**Vericiguat stimulates soluble guanylate cyclase and enhances cyclic GMP signaling.**',
 ['Evidence relates to selected symptomatic patients with reduced EF and recent worsening HF.', 'The 2022 guideline gives a selective role rather than a universal mandate.'],
 '**Address foundational treatment and the cause of deterioration first.**',
 ['Check adherence, congestion, ischemia, arrhythmia and other triggers.', 'Blood pressure, drug interactions and pregnancy considerations affect suitability; do not combine indiscriminately with PDE5 inhibitors.'],
 [['Foundational therapies not optimized','Prioritize eligible core treatment'],['Recent worsening despite therapy','Consider selected add-ons such as vericiguat'],['Persistent advanced deterioration','Assess advanced HF referral']], [HF], 'clinical_scenario')
q('A patient with ischemic cardiomyopathy has LVEF 30%, NYHA II symptoms and persistent dysfunction despite more than three months of GDMT. MI occurred one year earlier, and meaningful survival beyond one year is expected. Which device primarily addresses sudden arrhythmic death risk?',
 'An implantable cardioverter-defibrillator for primary prevention',[
 ('A standard single-chamber pacemaker solely because EF is low','A conventional pacemaker does not provide defibrillation for malignant ventricular tachyarrhythmias.'),
 ('No device can be considered unless cardiac arrest has already occurred','Primary prevention does not require a previous arrest when guideline criteria are met.'),
 ('An ICD solely to reverse all mechanical dyssynchrony','An ICD treats dangerous arrhythmias; resynchronization requires a CRT strategy and relevant conduction criteria.')],
 'Primary-prevention ICD selection',
 '**Persistent severe LV dysfunction can identify a population at risk of sudden arrhythmic death.**',
 ['For the stated ischemic, symptomatic patient, an EF at most 35% despite chronic GDMT supports ICD consideration.', 'Timing after MI and treatment optimization matter, as does an expectation of meaningful survival beyond one year.'],
 '**Balance arrhythmic benefit against competing mortality and patient goals.**',
 ['Advanced noncardiac disease or severe frailty may reduce net benefit.', 'Discuss shocks, complications and future deactivation preferences as part of an informed device decision.'],
 [['ICD','Prevents selected arrhythmic deaths'],['CRT','Resynchronizes selected dyssynchronous ventricles'],['Conventional pacemaker','Treats selected bradycardia indications']], [HF], 'clinical_scenario')
q('Ten days after an uncomplicated MI, a patient has LVEF 30% but no sustained ventricular arrhythmia. What is the appropriate approach to a primary-prevention ICD?',
 'Optimize treatment and reassess after the required post-MI waiting period rather than implanting solely for the early EF value',[
 ('Implant immediately in every patient with EF below 35%','Early post-MI EF alone does not satisfy the standard primary-prevention timing criteria.'),
 ('Exclude ICD treatment permanently because no arrest occurred','Primary prevention may become appropriate if dysfunction persists after the waiting and treatment period.'),
 ('Use a standard pacemaker as an equivalent substitute','A standard pacemaker cannot deliver the same ventricular defibrillation protection.')],
 'Early post-MI dysfunction may improve',
 '**Routine primary-prevention ICD implantation is deferred until at least 40 days after MI, with treatment and recovery reassessment.**',
 ['Revascularization and GDMT may improve EF, so the early measurement is not necessarily the final substrate.', 'Additional reassessment intervals apply after revascularization and during medical optimization.'],
 '**Primary and secondary prevention follow different reasoning.**',
 ['A sustained ventricular arrhythmia requires evaluation of timing, reversible causes and a secondary-prevention pathway.', 'The stem specifies no sustained arrhythmia and asks about implantation based only on early low EF.'],
 [['Early low EF after MI without qualifying arrhythmia','Optimize and reassess'],['Persistently qualifying dysfunction later','Consider primary-prevention ICD'],['Sustained VT/VF','Assess a distinct arrhythmia indication']], [HF], 'clinical_scenario')
q('A patient has LVEF 28%, sinus rhythm, LBBB with QRS 168 ms and persistent NYHA III symptoms despite GDMT. Which intervention is particularly supported by this electrical pattern?',
 'Cardiac resynchronization therapy',[
 ('CRT solely because the PR interval is normal','The indication concerns ventricular dyssynchrony and HF phenotype, not a normal PR interval.'),
 ('A standard RV-only pacemaker as the preferred resynchronization treatment','RV-only pacing does not reproduce biventricular resynchronization and may worsen dyssynchrony in susceptible patients.'),
 ('No device because only QRS durations above 200 ms qualify','A QRS of 168 ms with LBBB falls within the strongest conventional CRT evidence group.')],
 'LBBB and a wide QRS identify a strong CRT phenotype',
 '**CRT can improve ventricular coordination, symptoms and outcomes in selected HFrEF.**',
 ['The strongest conventional indication includes EF at most 35%, sinus rhythm, LBBB and QRS at least 150 ms despite GDMT.', 'The expected benefit varies with QRS duration and morphology; all wide QRS patterns are not equivalent.'],
 '**Evaluate the complete device strategy.**',
 ['Assess the need for defibrillation capability separately and consider procedural feasibility and goals.', 'CRT complements foundational treatment and does not eliminate the need for follow-up or medication.'],
 [['LBBB with QRS at least 150 ms and qualifying HFrEF','Strong CRT evidence'],['Narrow QRS without another pacing indication','No routine CRT for HF alone'],['Non-LBBB patterns','More selective assessment']], [HF,ESC], 'clinical_scenario')
q('A patient with permanent AF and a CRT device has persistent HF symptoms and only 78% effective biventricular pacing because of rapid conducted beats. What is the key management principle?',
 'Achieve near-complete effective biventricular pacing, considering AV node ablation if adequate control cannot otherwise be obtained',[
 ('Accept any pacing percentage above 50% as fully effective CRT','Suboptimal effective pacing can substantially reduce CRT benefit.'),
 ('Use ivabradine to control the ventricular rate in permanent AF','Ivabradine acts at the sinus node and is not a ventricular rate-control solution for AF.'),
 ('Stop CRT permanently without assessing the cause of low pacing','The correct first step is to address why effective resynchronization is inadequate.')],
 'CRT requires delivery of effective resynchronization',
 '**AF can compete with pacing and reduce effective biventricular capture.**',
 ['A high device-reported pacing count may still overestimate effective resynchronization if fusion or pseudofusion occurs.', 'Rate control, rhythm strategy and selected AV node ablation can improve pacing delivery.'],
 '**Choose an intervention based on the reason for lost capture.**',
 ['Review device programming, arrhythmia burden, ventricular ectopy and lead function.', 'AV node ablation creates pacing dependence and requires careful counseling and an appropriate device plan.'],
 [['High effective biventricular capture','Supports CRT benefit'],['AF with inadequate capture','Optimize rate or rhythm strategy'],['Persistent inadequate delivery','Consider AV node ablation in selected patients']], [HF,ESC], 'clinical_scenario')
q('A patient with HFrEF remains symptomatic with severe secondary MR despite optimized GDMT and appropriate CRT assessment. LVEF is 35%, LV end-systolic diameter 62 mm and pulmonary artery systolic pressure 55 mm Hg. Mitral anatomy is suitable. Which next step is appropriate?',
 'Heart Team evaluation for transcatheter edge-to-edge repair',[
 ('Treat the MR immediately before any HF therapy is attempted','Secondary MR can improve with ventricular treatment, so optimization precedes a residual-MR intervention decision.'),
 ('Exclude intervention because any reduced EF prohibits TEER','Selected reduced-EF patients are the population in which TEER benefit has been demonstrated.'),
 ('Assume valve intervention is unnecessary because MR is secondary','Persistent severe secondary MR can remain an important treatment target in selected symptomatic patients.')],
 'Residual secondary MR after HF optimization',
 '**Secondary MR reflects ventricular or atrial disease, so the underlying HF treatment is foundational.**',
 ['Selected patients with severe residual MR and suitable anatomy can benefit from TEER.', 'The stated measurements are within commonly used COAPT-like selection ranges, but full anatomical and clinical assessment is still necessary.'],
 '**Use a multidisciplinary decision rather than a single EF cutoff.**',
 ['Consider ventricular size, pulmonary pressure, RV function, comorbidity and competing advanced-HF needs.', 'Do not confuse this chronic secondary-MR pathway with emergency papillary muscle rupture after MI.'],
 [['Secondary MR before GDMT optimization','Treat the HF substrate first'],['Persistent severe MR in an eligible symptomatic patient','Assess TEER'],['Advanced irreversible ventricular disease','Assess the broader advanced-HF strategy']], [HF,ref('2020 ACC/AHA Valvular Heart Disease Guideline','https://doi.org/10.1161/CIR.0000000000000923')], 'clinical_scenario')
q('A patient with HFrEF develops persistent AF, worsening symptoms and a decline in EF despite appropriate HF therapy and attempted rate control. Which statement about catheter ablation is most accurate?',
 'In appropriately selected HFrEF patients, AF ablation can improve symptoms and ventricular function and may improve clinical outcomes',[
 ('Ablation is contraindicated in every patient with reduced EF','Reduced EF is not a blanket contraindication; selected patients can benefit.'),
 ('Successful ablation automatically removes every indication for anticoagulation','Anticoagulation decisions depend on thromboembolic risk and guideline context, not apparent rhythm success alone.'),
 ('AF can never cause or worsen ventricular dysfunction','Tachycardia and rhythm-related mechanisms can contribute to an arrhythmia-induced cardiomyopathy.')],
 'AF may be both a consequence and a driver of HF',
 '**Consider a rhythm-control strategy when AF contributes to symptoms or ventricular deterioration.**',
 ['Catheter ablation can reduce AF burden and permit reverse remodeling in selected HFrEF patients.', 'Selection considers AF duration, atrial size, comorbidity, procedural risk and likelihood of maintaining rhythm.'],
 '**Continue treating the associated HF and stroke risk.**',
 ['Reassess ventricular function after successful rhythm treatment.', 'Do not stop anticoagulation solely because an ablation appears successful when ongoing risk-based treatment is indicated.'],
 [['AF contributing to HFrEF','Consider appropriate rhythm-control assessment'],['After successful ablation','Reassess EF and symptoms'],['Stroke prevention','Continue risk-based decisions']], [HF,ref('2023 ACC/AHA/ACCP/HRS Atrial Fibrillation Guideline','https://doi.org/10.1161/CIR.0000000000001193')], 'clinical_scenario')
q('What was the key safety finding of SERVE-HF when the studied adaptive servo-ventilation strategy was used in systolic HF with predominant central sleep apnea?',
 'Cardiovascular and all-cause mortality increased despite effective suppression of central apnea',[
 ('A clear mortality reduction proved that all sleep-disordered breathing should receive the same device','The trial found increased mortality, and treatment cannot be generalized across apnea types and devices.'),
 ('Central apnea was not improved, so no physiological effect occurred','The concern was that physiological control of apnea did not translate into clinical safety.'),
 ('The findings prove that CPAP for every patient with obstructive apnea is harmful','SERVE-HF studied a particular ASV approach in predominant central apnea, not all CPAP treatment for obstructive apnea.')],
 'A surrogate improvement can coexist with clinical harm',
 '**Suppressing an abnormal physiological signal does not guarantee better survival.**',
 ['SERVE-HF enrolled systolic HF with predominant central sleep apnea and found increased mortality with the studied ASV strategy.', 'This is a trial-specific safety lesson; current device selection requires attention to apnea type, ventricular phenotype and contemporary evidence.'],
 '**Diagnose the sleep disorder before prescribing ventilatory treatment.**',
 ['Obstructive and central apnea have different mechanisms and evidence bases.', 'Do not extrapolate a single trial to every PAP mode or assume a lower apnea index automatically means a safer treatment.'],
 [['SERVE-HF population','Systolic HF with predominant central apnea'],['Physiological effect','Central apnea suppressed'],['Clinical finding','Increased mortality with studied ASV']], [ref('SERVE-HF: Adaptive Servo-Ventilation for Central Sleep Apnea in Systolic Heart Failure','https://doi.org/10.1056/NEJMoa1506459')])
q('A patient with stable HFrEF and LVEF 25% is in sinus rhythm with no LV thrombus, prior embolism, venous thromboembolism or other anticoagulation indication. Which antithrombotic statement is correct?',
 'Low EF alone does not justify routine oral anticoagulation',[
 ('Every patient with EF below 30% requires indefinite warfarin','A low EF alone does not establish a favorable net benefit from routine anticoagulation.'),
 ('Aspirin must be used in every nonischemic cardiomyopathy','Antiplatelet therapy requires its own indication and is not universally prescribed for nonischemic HF.'),
 ('Anticoagulation should never be used if AF subsequently develops','A later valid indication, such as risk-qualified AF, changes the treatment decision.')],
 'Treat a thromboembolic indication rather than an EF number',
 '**Routine anticoagulation is not recommended for chronic HFrEF in sinus rhythm without another indication.**',
 ['Bleeding risk offsets an indiscriminate attempt to reduce embolic events.', 'AF, demonstrated intracardiac thrombus, previous embolism or venous thrombosis can provide separate reasons for treatment.'],
 '**Reassess when the clinical context changes.**',
 ['An ischemic cause of HF may justify antiplatelet therapy for coronary disease, which is a different question.', 'Review new arrhythmia, imaging evidence of thrombus and bleeding risk during follow-up.'],
 [['Low EF alone in sinus rhythm','No routine anticoagulation'],['AF or LV thrombus','Assess the specific anticoagulation indication'],['Coronary disease','Assess separate antiplatelet needs']], [HF])
q('A stable euvolemic HF patient asks whether exercise should be avoided to protect the weak heart. Which advice is most appropriate?',
 'Offer an individualized exercise or cardiac rehabilitation program appropriate to clinical stability and capacity',[
 ('Prescribe permanent bed rest because any exercise accelerates HF','Prolonged inactivity worsens deconditioning and is not routine chronic HF care.'),
 ('Recommend maximal unsupervised exertion regardless of symptoms','Exercise intensity requires individual assessment and progression.'),
 ('Use exercise as a reason to stop disease-modifying medication','Exercise complements rather than replaces medical treatment.')],
 'Exercise is part of stable HF management',
 '**Appropriate training can improve functional capacity, symptoms and quality of life.**',
 ['The prescription should account for baseline function, frailty, arrhythmia, ischemia and comorbidity.', 'Acute decompensation is a reason to stabilize before training, not a permanent prohibition.'],
 '**Build a sustainable program with symptom education.**',
 ['Discuss warning signs, gradual progression and adherence.', 'Nutrition and resistance training may help preserve muscle, particularly in older or obese patients undergoing weight reduction.'],
 [['Stable compensated HF','Individualized activity and rehabilitation'],['Acute unstable HF','Stabilize before exercise progression'],['Long-term care','Combine activity with preventive and HF therapy']], [HF,ESC], 'clinical_scenario')
q('Which pattern should prompt timely advanced-HF referral rather than repeated routine outpatient escalation alone?',
 'Recurrent HF admissions with worsening end-organ function and inability to tolerate disease-modifying therapy',[
 ('A single mildly elevated BNP in an asymptomatic stable patient','This alone does not establish advanced HF or a need for transplant evaluation.'),
 ('Improving symptoms and EF on a well-tolerated regimen','Improvement is reassuring rather than the deterioration pattern in question.'),
 ('Stable mild ankle edema that resolves with a small diuretic adjustment','An isolated easily corrected symptom does not carry the same advanced-HF signal.')],
 'Recognize the trajectory before irreversible deterioration',
 '**Advanced HF is identified by persistent severe disease and repeated deterioration despite appropriate treatment.**',
 ['Recurrent admissions, refractory congestion, low output and progressive renal or hepatic dysfunction are important warning signs.', 'Intolerance of previously tolerated treatment may reflect diminishing hemodynamic reserve.'],
 '**Refer while options can still be assessed.**',
 ['An advanced team can evaluate transplant, LVAD, investigational strategies and integrated palliative support.', 'Referral is an assessment step, not a promise of eligibility or a commitment to a device.'],
 [['Recurrent admissions and end-organ decline','Advanced-HF referral signal'],['Refractory symptoms despite optimized treatment','Assess advanced options'],['Irreversible competing disease','Clarify goals and appropriate supportive care']], [HF,ESC])
q('During a maximal cardiopulmonary exercise test, a patient with advanced HF on a beta blocker has peak oxygen consumption 10.5 mL/kg/min. Which interpretation is most appropriate?',
 'The result supports severe functional limitation and transplant evaluation when integrated with the full assessment',[
 ('The value alone automatically guarantees transplant listing','Listing requires a multidimensional assessment, not a single exercise number.'),
 ('Any value above 5 mL/kg/min excludes advanced HF','This cutoff is not the relevant standard; 10.5 is markedly reduced.'),
 ('Peak oxygen consumption is unrelated to prognosis','CPET provides important functional and prognostic information in advanced HF.')],
 'CPET contributes to advanced-HF risk assessment',
 '**A low peak VO2 can support advanced-therapy evaluation when effort and measurement quality are adequate.**',
 ['ISHLT guidance commonly uses peak VO2 at most 12 mL/kg/min on beta blockade as supportive evidence; a higher threshold may be used off beta blockers.', 'Percent predicted VO2, ventilatory efficiency, effort, age and body composition also influence interpretation.'],
 '**Use the test as part of a comprehensive decision.**',
 ['Assess hemodynamics, end-organ function, frailty, comorbidity and psychosocial suitability.', 'Obesity can complicate weight-indexed values, and a submaximal study may require alternative interpretive measures.'],
 [['Peak VO2','Functional and prognostic measure'],['Low value with adequate effort','Supports advanced-HF assessment'],['Listing decision','Requires comprehensive eligibility evaluation']], [ref('ISHLT Guidelines for Evaluation and Care of Cardiac Transplant Candidates (2024)','https://www.ishlt.org/docs/default-source/standards-guidelines/2024_guideline_careofhtxcandidates.pdf'),ESC], 'clinical_scenario')
q('Why is severe right ventricular failure an important concern before implanting an isolated durable LV assist device?',
 'The RV must still deliver blood through the lungs to fill the LVAD-supported circulation',[
 ('An LVAD directly replaces both ventricles in every patient','An isolated LVAD supports left-sided output and does not directly provide right-sided pumping.'),
 ('Right-sided function has no effect on LVAD flow','Inadequate RV output can limit LV filling and device flow.'),
 ('LVAD implantation removes the need to assess pulmonary vascular load','Pulmonary vascular resistance and RV reserve influence postoperative risk.')],
 'Isolated LV support depends on a functioning right-sided circulation',
 '**An LVAD unloads the LV but does not eliminate the RV\'s work.**',
 ['Increasing systemic flow can increase venous return that the RV must handle.', 'Severe RV dysfunction can lead to postoperative congestion, low LVAD preload and low output.'],
 '**Assess biventricular physiology before choosing the support strategy.**',
 ['Integrate RV imaging, venous pressures, pulmonary vascular load and end-organ function.', 'Selected patients need additional right-sided support or a different advanced-therapy plan.'],
 [['Isolated LV dysfunction with adequate RV reserve','May suit LVAD support'],['Severe RV failure','High risk with isolated LVAD'],['Support planning','Requires biventricular assessment']], [HF,ESC])
q('A patient with advanced HF is considering an LVAD. Which statement about palliative care is correct?',
 'Palliative care can be integrated alongside disease-directed and advanced therapies',[
 ('It can begin only after every HF treatment has been stopped','Palliative care is not restricted to withdrawal of treatment.'),
 ('Accepting palliative support automatically excludes transplant evaluation','Supportive care and advanced-therapy evaluation can occur together.'),
 ('It concerns only analgesia during the last hours of life','It also addresses symptoms, communication, caregiver burden and decisions throughout serious illness.')],
 'Palliative support is concurrent comprehensive care',
 '**The aim is to improve quality of life and align treatment with patient goals.**',
 ['HF symptoms and uncertainty can create substantial patient and caregiver burden.', 'Shared decisions about devices, hospitalization, resuscitation and future treatment changes benefit from early discussion.'],
 '**Concurrent care does not imply abandonment of effective therapy.**',
 ['Continue disease-directed treatment when it fits the patient\'s goals and expected benefit.', 'Document preferences and revisit them as illness and treatment options change.'],
 [['Disease-directed treatment','Targets cardiac disease and prognosis'],['Palliative care','Targets symptoms, communication and goal alignment'],['Integrated approach','Can include both simultaneously']], [HF,ESC], 'clinical_scenario')
q('After hospitalization for acute HF, a patient is stable and ready for discharge. Which plan best addresses the high-risk transition period?',
 'Arrange early follow-up with medication review, congestion assessment and planned renal and electrolyte monitoring',[
 ('Defer review for six months because symptoms improved in hospital','Early relapse and medication-related problems are common after discharge.'),
 ('Give a weight diary without a medication or escalation plan','Monitoring is more useful when linked to clear actions and access to clinical advice.'),
 ('Avoid all medication titration until another admission occurs','The post-discharge period is an opportunity to optimize treatment with close follow-up.')],
 'The discharge plan is part of HF treatment',
 '**A successful discharge links inpatient stabilization to early outpatient reassessment.**',
 ['Review volume status, symptoms, adherence, blood pressure and tolerability soon after discharge.', 'Kidney function and potassium monitoring are particularly important after diuretic, RAS-pathway or MRA changes.'],
 '**Provide an actionable self-management plan.**',
 ['Explain daily weights, warning symptoms, medication access and whom to contact for deterioration.', 'Use early review to introduce or titrate eligible therapies rather than accepting therapeutic inertia.'],
 [['Before discharge','Reconcile medication and assess residual congestion'],['Early follow-up','Review symptoms, function and laboratories'],['Deterioration plan','Clear contact and escalation instructions']], [HF,ECDP,ESC], 'clinical_scenario')

if __name__=='__main__':
    finalize('Cardiology',2,'Heart Failure','cardiology-heart-failure',rows,44)
