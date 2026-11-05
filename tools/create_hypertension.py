"""Original Hypertension chapter, with guideline systems stated explicitly."""
from qbank_authoring import question,ref,finalize
E=ref('2024 ESC Elevated Blood Pressure and Hypertension Guideline','https://doi.org/10.1093/eurheartj/ehae178')
A=ref('2025 AHA/ACC High Blood Pressure Guideline','https://doi.org/10.1161/CIR.0000000000001356')
PA=ref('Endocrine Society 2025 Primary Aldosteronism Guideline','https://www.endocrine.org/clinical-practice-guidelines/primary-aldosteronism-2')
PHEO=ref('Endocrine Society Pheochromocytoma and Paraganglioma Guideline','https://doi.org/10.1210/jc.2014-1498')
rows=[]
def q(*args,**kwargs):rows.append(question(*args,**kwargs))

q('A patient with a large arm has unexpectedly high office BP measured with a small cuff. What is the likely measurement effect?',
 'The undersized cuff can overestimate BP',[
 ('An undersized cuff reliably underestimates BP','The usual miscuffing effect is falsely high pressure.'),
 ('Cuff size has no effect if a digital device is used','Automated measurement still requires a validated device and suitable cuff.'),
 ('The result proves resistant hypertension','Technique must be checked before assigning a disease category.')],
 'Correct technique precedes diagnosis',
 '**Use a validated device and a cuff appropriate to arm circumference.**',
 ['Support the arm at heart level after a rest period.', 'Avoid talking and account for recent exercise, caffeine or smoking.'],
 '**Confirm a persistent elevation with appropriate repeat measurements.**',
 ['A single technically flawed value should not trigger a resistant-hypertension label.', 'Out-of-office readings help characterize the usual pressure burden.'],
 [['Small cuff','Can falsely elevate BP'],['Correct cuff and position','Improves accuracy'],['Diagnosis','Requires reliable repeated assessment']], [A,E], 'clinical_scenario')
q('Office BP is repeatedly elevated, but validated home and ambulatory averages are normal. Which phenotype is present?',
 'White-coat hypertension',[
 ('Masked hypertension','Masked hypertension has normal office readings with high out-of-office pressure.'),
 ('Sustained hypertension','Sustained hypertension is elevated in both settings.'),
 ('Orthostatic hypotension','That concerns a postural pressure fall rather than this setting-dependent pattern.')],
 'The setting can change the measured phenotype',
 '**White-coat hypertension requires a discordance between office and usual out-of-office pressure.**',
 ['Confirm reliable devices and sampling.', 'Treatment status distinguishes white-coat hypertension from a white-coat effect during therapy.'],
 '**Continue risk assessment and follow-up.**',
 ['The phenotype can progress to sustained hypertension.', 'Lifestyle and cardiovascular risk management remain relevant even when medication is not immediately indicated.'],
 [['Office high, home normal','White-coat phenotype'],['Office normal, home high','Masked phenotype'],['Both high','Sustained hypertension']], [A,E])
q('A patient with LV hypertrophy has normal clinic readings but consistently elevated daytime ambulatory BP. What is the diagnosis?',
 'Masked hypertension',[
 ('White-coat hypertension','That has the opposite office-outside pattern.'),
 ('Normotension established by one clinic reading','Out-of-office elevation can represent clinically important pressure exposure.'),
 ('Isolated postural hypotension','No postural fall is described.')],
 'A normal office pressure may miss the usual burden',
 '**Masked hypertension is elevated outside the clinic despite normal office readings.**',
 ['Target-organ changes can be a clue prompting ambulatory assessment.', 'Work, sleep and activity patterns may influence the exposure.'],
 '**Treat the confirmed phenotype and overall risk.**',
 ['Check measurement quality and secondary contributors.', 'Do not ignore reliable ambulatory findings because the clinic value is reassuring.'],
 [['Office normal, ambulatory high','Masked hypertension'],['Target-organ injury','Supports investigating hidden exposure'],['Follow-up','Use reliable out-of-office monitoring']], [A,E], 'clinical_scenario')
q('Under the 2024 ESC classification, which confirmed office BP meets the hypertension threshold?',
 '146/92 mm Hg',[
 ('128/76 mm Hg','This is below the ESC hypertension threshold, although elevated-BP categories and treatment risk assessment differ.'),
 ('134/84 mm Hg','This is below the ESC office diagnostic threshold of 140/90.'),
 ('138/86 mm Hg','This also falls below that threshold.')],
 'State the guideline before applying a category',
 '**The 2024 ESC office hypertension threshold remains at least 140/90 mm Hg.**',
 ['The guideline also recognizes an elevated-BP category below this level.', 'US categories use different labels and thresholds.'],
 '**Diagnosis thresholds and treatment targets are different concepts.**',
 ['A high-risk person can merit treatment below a categorical hypertension threshold.', 'Confirm pressure with reliable repeat or out-of-office measurements.'],
 [['ESC diagnostic threshold','Office BP at least 140/90'],['Treatment threshold','Can depend on risk'],['On-treatment target','Separate recommendation']], [E])
q('What on-treatment systolic target does the 2024 ESC guideline generally recommend for most adults when well tolerated?',
 '120-129 mm Hg',[
 ('150-159 mm Hg for every adult','That is not the general current target.'),
 ('Below 100 mm Hg irrespective of symptoms','Excessive lowering without regard to tolerability is not recommended.'),
 ('Exactly the same target without exceptions for severe frailty or orthostatic symptoms','The guideline allows individualization in such settings.')],
 'Tolerability is part of the target',
 '**The general ESC target is a systolic range of 120-129 when treatment is tolerated.**',
 ['Symptoms, orthostatic pressure and frailty can justify a more individualized approach.', 'Out-of-office confirmation helps avoid overtreating a clinic-only elevation.'],
 '**A target is not a command to ignore adverse effects.**',
 ['Review dizziness, falls, kidney function and electrolytes.', 'Use shared decisions and accurate measurement when intensifying therapy.'],
 [['Most suitable treated adults','Aim 120-129 systolic'],['Intolerance or important frailty','Individualize'],['Monitoring','Symptoms and biochemical safety']], [E])
q('Under the 2025 AHA/ACC guideline, a patient has confirmed BP 134/84 mm Hg and PREVENT 10-year CVD risk 10%. What is appropriate?',
 'Add BP-lowering medication to lifestyle measures if the patient is otherwise suitable',[
 ('Wait until BP reaches 180/110 regardless of risk','The guideline uses lower risk-based treatment thresholds.'),
 ('Use the older 10% ASCVD threshold as the only current rule','The updated framework uses PREVENT and a 7.5% risk threshold in this context.'),
 ('Ignore risk because BP is below 140/90','Selected higher-risk patients merit treatment at at least 130/80.')],
 'Treatment can be risk based below 140/90',
 '**The 2025 US framework recommends medication at at least 130/80 in selected higher-risk adults.**',
 ['PREVENT risk at least 7.5% is one qualifying context.', 'Clinical CVD, diabetes, CKD or prior stroke also affect the decision.'],
 '**Confirm the pressure and individual suitability.**',
 ['Continue lifestyle treatment and monitor response.', 'Do not mix the diagnostic labels or risk equations from different guideline systems.'],
 [['BP at least 140/90','Broad medication threshold'],['BP at least 130/80 with qualifying risk','Medication plus lifestyle'],['Low-risk persistent elevation','Lifestyle and time-based reassessment']], [A], 'clinical_scenario')
q('A patient needs initial combination therapy for uncomplicated hypertension. Which combination uses complementary recommended first-line classes?',
 'An ARB plus a dihydropyridine calcium channel blocker',[
 ('An ACE inhibitor plus an ARB','Dual RAS blockade increases adverse effects without being the routine combination strategy.'),
 ('Verapamil plus a beta blocker in every patient','Combined nodal suppression is not the routine uncomplicated-hypertension default.'),
 ('Two different ACE inhibitors','This duplicates a mechanism rather than combining complementary classes.')],
 'Combine complementary mechanisms',
 '**RAS blockade can be combined with a CCB or a suitable thiazide-type diuretic.**',
 ['Single-pill combinations can improve adherence.', 'Comorbidity, electrolytes, renal function and pregnancy potential affect selection.'],
 '**Avoid harmful duplication.**',
 ['ACE inhibitor plus ARB is not standard hypertension combination care.', 'Use beta blockers when an appropriate indication or selected context exists.'],
 [['RAS blocker plus CCB/diuretic','Complementary approach'],['ACE inhibitor plus ARB','Avoid routine dual blockade'],['Choice','Individualize to comorbidity']], [A,E])
q('Which regimen should generally be optimized before labeling BP uncontrolled on a three-drug foundation as resistant hypertension?',
 'A RAS blocker, a long-acting dihydropyridine CCB and an appropriate thiazide/thiazide-like diuretic',[
 ('Three low doses without a diuretic and without adherence review','This does not establish an optimized resistant-hypertension phenotype.'),
 ('Aspirin, statin and nitrate','These are not the standard three-class BP foundation.'),
 ('An ACE inhibitor, ARB and a second ARB','Duplicated RAS blockade is not the recommended foundation.')],
 'Resistance is defined after an adequate regimen and confirmation',
 '**The usual three-class foundation includes an effective diuretic.**',
 ['Dose, renal function and the appropriateness of the diuretic matter.', 'Out-of-office pressure and adherence must also be assessed.'],
 '**Exclude pseudoresistance and secondary disease.**',
 ['Check technique, white-coat effect, missed doses and pressor drugs.', 'Different guideline labels can include controlled-on-four-drugs phenotypes, so specify the framework when needed.'],
 [['Optimized three-class therapy','Foundation for assessing resistance'],['Incorrect measurement/nonadherence','Pseudoresistance'],['Secondary disease','Requires directed assessment']], [E,A])
q('A patient appears resistant to four BP drugs but refill history suggests frequent missed doses. What is the most appropriate first response?',
 'Assess barriers and actual medication exposure before adding more drugs',[
 ('Add two more drugs without checking the regimen','This can increase burden without resolving the cause and risks hypotension if adherence improves.'),
 ('Assume the patient is intentionally noncooperative','Adherence barriers include cost, adverse effects, complexity and misunderstanding.'),
 ('Diagnose a rare endocrine tumor solely from the office pressure','Pseudoresistance must be assessed alongside appropriate secondary-cause evaluation.')],
 'Apparent resistance may reflect implementation rather than pharmacology',
 '**A nonjudgmental adherence assessment is part of resistant-hypertension care.**',
 ['Simplify the regimen and use fixed-dose combinations where suitable.', 'Confirm home pressure and technique.'],
 '**Avoid therapeutic escalation based on a prescription list alone.**',
 ['The recorded regimen may not equal the taken regimen.', 'Reassess after addressing access, tolerability and understanding.'],
 [['Prescription list','Intended exposure'],['Actual use','Determines physiological effect'],['Intervention','Address barriers and simplify']], [A,E], 'clinical_scenario')
q('A patient has confirmed resistant hypertension despite an optimized RAS blocker, CCB and thiazide-like diuretic. eGFR is 68 and potassium 4.1. Which fourth drug is commonly preferred?',
 'Spironolactone',[
 ('A second ARB','Duplicate RAS blockade is not the preferred next step.'),
 ('Digoxin','Digoxin is not routine treatment for resistant hypertension.'),
 ('Aspirin','Aspirin is not a BP-lowering fourth-line drug.')],
 'Mineralocorticoid blockade addresses a common resistant phenotype',
 '**Spironolactone is an evidence-supported add-on when renal function and potassium permit.**',
 ['Monitor potassium and kidney function after initiation and titration.', 'Endocrine adverse effects or contraindications may require alternatives.'],
 '**Continue the resistance work-up.**',
 ['Assess primary aldosteronism, sleep apnea and other relevant causes.', 'The fourth drug does not replace adherence and out-of-office confirmation.'],
 [['Suitable resistant hypertension','Consider spironolactone'],['High potassium/severe renal impairment','Safety concern'],['Follow-up','Biochemical and BP monitoring']], [E], 'clinical_scenario')
q('Which feature strongly supports assessing primary aldosteronism in a hypertensive patient?',
 'Resistant hypertension with spontaneous hypokalemia',[
 ('Normal potassium as definitive exclusion','Many patients with primary aldosteronism are normokalemic.'),
 ('A normal resting ECG as proof that endocrine hypertension is absent','An ECG does not exclude autonomous aldosterone production.'),
 ('A single mild headache as a specific diagnostic test','Headache is nonspecific.')],
 'Aldosterone excess is often missed by relying on potassium alone',
 '**Hypertension with hypokalemia is a strong clue, but normokalemia does not exclude disease.**',
 ['The 2025 Endocrine Society guideline supports broader screening than older narrow case-detection approaches.', 'Local feasibility and an appropriate testing protocol matter.'],
 '**Measure aldosterone and renin with attention to conditions.**',
 ['Correct hypokalemia and review interfering medication.', 'Interpret the ratio with the absolute aldosterone and renin rather than as an isolated number.'],
 [['Resistant BP plus low K','High-priority clue'],['Normal K','Does not rule out PA'],['Screen','Aldosterone, renin and their relationship']], [PA], 'clinical_scenario')
q('Which biochemical pattern supports primary rather than secondary hyperaldosteronism?',
 'Inappropriately high aldosterone with suppressed renin',[
 ('High aldosterone with markedly increased renin from renal hypoperfusion','That suggests secondary RAS activation.'),
 ('Low aldosterone with low renin during licorice exposure','That suggests a nonaldosterone mineralocorticoid mechanism.'),
 ('High renin with low aldosterone after RAS blockade as proof of PA','Medication effects can create a different pattern and confound interpretation.')],
 'Primary aldosteronism is renin-independent production',
 '**Aldosterone remains inappropriate despite renin suppression.**',
 ['Assay type and units determine ratio thresholds.', 'A very low renin denominator alone can inflate a ratio when aldosterone is not meaningfully elevated.'],
 '**Interpret biochemical evidence before imaging.**',
 ['Adrenal nodules are common and do not prove functional laterality.', 'Subtyping and confirmatory assessment follow the clinical and biochemical context.'],
 [['Primary aldosteronism','High/inappropriate aldosterone, suppressed renin'],['Secondary activation','Aldosterone and renin both raised'],['Apparent mineralocorticoid excess','Often both suppressed']], [PA])
q('Why must spironolactone exposure be reviewed when interpreting an aldosterone-renin screen?',
 'Mineralocorticoid blockade can raise renin and alter the ratio, potentially obscuring the expected pattern',[
 ('It has no effect on the RAS under any circumstance','It changes the feedback and volume context.'),
 ('It directly measures aldosterone in the laboratory','It is a drug exposure, not an assay.'),
 ('Its presence proves unilateral adrenal disease','Medication use cannot localize the source.')],
 'Screening conditions affect the result',
 '**MRAs and several other antihypertensives can alter renin and aldosterone interpretation.**',
 ['Beta blockers can suppress renin, while RAS blockers and diuretics can raise it.', 'Hypokalemia can suppress aldosterone and should be corrected when possible.'],
 '**Use a safe individualized testing strategy.**',
 ['Do not withdraw essential treatment recklessly in severe hypertension.', 'A specialist can choose medication substitution or interpret results under a minimal-withdrawal approach.'],
 [['MRA exposure','Can raise renin and change ARR'],['Low potassium','Can lower aldosterone'],['Testing plan','Balance validity and BP safety']], [PA])
q('A patient with confirmed PA wants adrenal surgery. CT shows a small left adrenal nodule. Why may adrenal venous sampling still be needed?',
 'Anatomical nodules do not reliably identify which adrenal is secreting excess aldosterone',[
 ('Every visible nodule is necessarily the functional source','Nonfunctioning incidental nodules are common.'),
 ('AVS measures coronary flow reserve','It assesses adrenal hormone lateralization.'),
 ('A normal contralateral CT excludes bilateral functional disease','Bilateral secretion can exist without visible bilateral nodules.')],
 'Function and anatomy need not match',
 '**AVS helps distinguish unilateral from bilateral aldosterone production in appropriate surgical candidates.**',
 ['Technical expertise and correct interpretation are important.', 'Selected young patients with a highly convincing phenotype may fit an exception, but this is not a universal CT-only rule.'],
 '**Choose treatment based on subtype and suitability.**',
 ['Unilateral disease may be treated surgically.', 'Bilateral disease or a nonsurgical preference generally leads to medical mineralocorticoid blockade.'],
 [['CT','Anatomical assessment'],['AVS','Functional lateralization'],['Treatment','Subtype and patient preference dependent']], [PA], 'clinical_scenario')

# Secondary causes, acute presentations and special populations follow.
q('A patient has paroxysmal hypertension, headache, sweating and palpitations. Which biochemical test is appropriate for pheochromocytoma assessment?',
 'Plasma free metanephrines or urinary fractionated metanephrines',[
 ('Aldosterone-renin ratio as the specific catecholamine test','ARR evaluates aldosterone physiology, not catecholamine metabolism.'),
 ('Urinary 5-HIAA as the routine first test for this tumor','5-HIAA is used for selected serotonin-secreting neuroendocrine syndromes.'),
 ('Serum cortisol alone as a definitive exclusion test','Cortisol does not exclude a catecholamine-producing tumor.')],
 'Metanephrines integrate catecholamine production',
 '**Free or fractionated metanephrines are preferred biochemical screening tests.**',
 ['Sampling conditions, posture, stress and interfering drugs can affect results.', 'Borderline elevations require interpretation rather than automatic tumor diagnosis.'],
 '**Localize after appropriate biochemical assessment.**',
 ['Adrenal or extra-adrenal imaging follows the clinical context.', 'Severe suggestive episodes require timely specialist care.'],
 [['Metanephrines','Catecholamine tumor assessment'],['ARR','Primary aldosteronism assessment'],['5-HIAA','Selected serotonin-secreting disease']], [PHEO], 'clinical_scenario')
q('Before elective surgery for a catecholamine-secreting pheochromocytoma, what is the usual adrenergic blockade sequence?',
 'Establish alpha blockade before adding beta blockade when needed',[
 ('Start a beta blocker alone first','Unopposed alpha-mediated vasoconstriction can precipitate severe hypertension.'),
 ('Use a loop diuretic to create profound volume depletion','Patients may be volume contracted; preparation requires careful volume assessment rather than deliberate depletion.'),
 ('Omit all preparation once the tumor is localized','Localization does not eliminate perioperative catecholamine risk.')],
 'Control vasoconstriction before isolated beta suppression',
 '**Alpha blockade is the usual initial adrenergic preparation.**',
 ['Beta blockade can then address persistent tachycardia when appropriate.', 'Salt and fluid planning depend on cardiac and renal status.'],
 '**Use an experienced perioperative team.**',
 ['Tumor manipulation can release catecholamines.', 'Blood pressure can fall substantially after resection, so postoperative monitoring is important.'],
 [['Alpha first','Reduces vasoconstrictor effect'],['Beta added later','Selected rate control'],['Perioperative care','Anticipate pressure swings']], [PHEO])
q('A patient has recurrent flash pulmonary edema, resistant hypertension and a marked creatinine rise after ACE inhibition. Which secondary cause should be considered?',
 'Hemodynamically important renovascular disease',[
 ('Uncomplicated isolated white-coat effect as the full explanation','The pulmonary edema and renal response warrant a secondary physiological assessment.'),
 ('Pheochromocytoma established by low renin alone','The provided pattern is more suggestive of renovascular disease than that biochemical claim.'),
 ('A small incidental adrenal cyst as proof of PA','An incidental cyst does not establish autonomous aldosterone production.')],
 'Renal perfusion can link pressure, kidney function and congestion',
 '**Bilateral severe disease or a lesion in a solitary functioning kidney can create this high-risk pattern.**',
 ['Atherosclerotic disease and fibromuscular dysplasia have different populations and anatomy.', 'The ACE-related change requires assessment of other contributors such as dehydration or NSAIDs.'],
 '**Investigate selectively and distinguish diagnosis from intervention.**',
 ['Not every anatomical stenosis benefits from revascularization.', 'Recurrent flash edema and other high-risk presentations merit specialist evaluation.'],
 [['Renal artery lesion','Can activate RAS and impair pressure control'],['ACE-related large GFR fall','Suggests perfusion dependence in context'],['Revascularization','Selected indication, not every stenosis']], [A,E], 'clinical_scenario')
q('A patient with resistant hypertension snores loudly, has witnessed apneas and daytime sleepiness. Which associated condition should be assessed?',
 'Obstructive sleep apnea',[
 ('Central hypothyroidism solely from snoring','The breathing history points to obstructive sleep-disordered breathing.'),
 ('Primary aldosteronism excluded by obesity','Obesity does not exclude PA; multiple contributors can coexist.'),
 ('White-coat hypertension established by nocturnal symptoms','That diagnosis requires a specific office-out-of-office BP pattern.')],
 'Sleep-disordered breathing can sustain sympathetic pressure load',
 '**OSA is common in resistant hypertension.**',
 ['Intermittent hypoxemia and sleep fragmentation contribute to sympathetic activation.', 'Appropriate sleep testing confirms the diagnosis.'],
 '**Treat the sleep disorder and the broader cardiovascular risk.**',
 ['Weight management and indicated airway therapy can help, but BP medication may still be needed.', 'Continue assessment of adherence, salt, alcohol and other secondary causes.'],
 [['Snoring/apneas/sleepiness','OSA clues'],['Testing','Appropriate sleep study'],['Management','Sleep treatment plus BP and risk care']], [A,E], 'clinical_scenario')
q('BP becomes harder to control after frequent ibuprofen use for arthritis. Which mechanism contributes?',
 'Renal prostaglandin inhibition can promote sodium retention and blunt antihypertensive treatment',[
 ('Selective irreversible aldosterone receptor blockade','That is not the NSAID mechanism.'),
 ('Obligatory profound natriuresis','NSAIDs can cause retention rather than predictable sodium loss.'),
 ('Direct correction of all renal perfusion abnormalities','Renal perfusion can worsen, especially with other risk factors.')],
 'Medication exposure can cause apparent treatment resistance',
 '**NSAIDs can raise pressure and worsen fluid or renal problems.**',
 ['The combination with a diuretic and RAS blocker can increase kidney-injury risk.', 'Decongestants, stimulants and other drugs can also contribute to poor control.'],
 '**Review the indication and safer alternatives.**',
 ['Assess renal function, potassium, congestion and pain-control needs.', 'Do not add antihypertensives indefinitely without addressing a removable pressor exposure.'],
 [['NSAID','Prostaglandin inhibition and sodium retention'],['RAS blocker plus diuretic','Additional renal vulnerability'],['Medication review','Essential resistance assessment']], [A,E], 'clinical_scenario')
q('A patient consuming large amounts of licorice has hypertension, hypokalemia, suppressed renin and suppressed aldosterone. Which mechanism fits?',
 'Inhibition of 11-beta-HSD2 permits cortisol to activate mineralocorticoid receptors',[
 ('An aldosterone-producing adenoma with obligatory high aldosterone','The suppressed aldosterone argues against that direct mechanism.'),
 ('Renovascular secondary hyperaldosteronism','Renin and aldosterone would generally be activated rather than both suppressed.'),
 ('Pheochromocytoma as the defining explanation of low aldosterone','The exposure and mineralocorticoid pattern indicate a different pathway.')],
 'Mineralocorticoid activity need not come from aldosterone',
 '**Reduced conversion of cortisol to cortisone allows cortisol-mediated receptor activation.**',
 ['Sodium retention and potassium loss suppress the RAS.', 'Licorice exposure can mimic apparent mineralocorticoid excess.'],
 '**Identify and remove the exposure.**',
 ['Assess potassium, ECG and severity.', 'A persistent phenotype after withdrawal warrants evaluation for other low-renin low-aldosterone disorders.'],
 [['Primary aldosteronism','Aldosterone inappropriate/high'],['Licorice effect','Renin and aldosterone suppressed'],['Mechanism','Cortisol reaches mineralocorticoid receptor']], [E], 'clinical_scenario')
q('Which feature distinguishes hypertensive emergency from severe BP elevation without acute organ injury?',
 'New or worsening acute target-organ injury attributable to the pressure',[
 ('An isolated systolic value above 180 regardless of context','The number alone does not establish an emergency.'),
 ('A longstanding asymptomatic high reading as automatic proof of encephalopathy','Encephalopathy requires clinical evidence.'),
 ('A chronic stable retinal change alone as proof of new acute injury','Chronic damage and acute emergency are different contexts.')],
 'An emergency is a clinical organ-injury syndrome',
 '**Brain, heart, kidney, aorta and pregnancy-related injury can define urgent treatment needs.**',
 ['Assess symptoms, examination and directed testing.', 'The treatment drug and speed depend on the affected organ and disease.'],
 '**Avoid treating every high number with the same rapid IV regimen.**',
 ['Excessive reduction can impair perfusion in chronic hypertension.', 'Acute dissection and other special emergencies follow specific targets.'],
 [['Severe BP plus acute injury','Hypertensive emergency'],['Severe BP without acute injury','Different treatment pace'],['Organ involved','Determines pathway']], [A,E])
q('An asymptomatic patient has repeated BP 190/112 mm Hg after several missed doses, with no evidence of acute target-organ injury. Which strategy is generally appropriate?',
 'Reinstitute or adjust oral treatment, address the cause and arrange timely follow-up',[
 ('Immediately normalize pressure with rapid IV boluses in every case','Rapid lowering without acute injury can cause harm.'),
 ('Ignore the pressure indefinitely because symptoms are absent','Severe sustained hypertension still requires treatment and follow-up.'),
 ('Use short-acting sublingual nifedipine for an uncontrolled abrupt fall','An unpredictable rapid reduction is not the appropriate routine strategy.')],
 'Absence of emergency changes the pace, not the need for care',
 '**Treat confirmed severe asymptomatic elevation with an appropriate oral and follow-up plan.**',
 ['Review adherence, pain, anxiety and pressor exposures.', 'Reassess for subtle organ injury if symptoms or findings suggest it.'],
 '**Avoid a reflex rapid-normalization target.**',
 ['Longstanding hypertension shifts autoregulatory tolerance.', 'Ensure medication access and a clear review plan.'],
 [['No acute organ injury','Oral adjustment and follow-up'],['Acute injury present','Monitored emergency pathway'],['Missed medication','Address access and adherence']], [A,E], 'clinical_scenario')
q('For many hypertensive emergencies without a condition-specific exception, why is mean arterial pressure initially reduced by only about 20-25% rather than immediately to normal?',
 'To reduce injury while avoiding ischemia from excessive loss of perfusion',[
 ('Normalizing pressure instantly is always safer','A large abrupt fall can compromise brain, coronary or renal perfusion.'),
 ('The kidneys require permanent severe hypertension','The goal is controlled lowering, not preserving dangerous pressure indefinitely.'),
 ('Every emergency must use the same schedule including dissection and stroke','Important organ-specific exceptions exist.')],
 'Controlled reduction respects altered autoregulation',
 '**Chronic hypertension can shift the pressure range supporting organ blood flow.**',
 ['Use titratable monitored treatment.', 'The initial reduction is followed by further controlled treatment as appropriate.'],
 '**Check for an exception before using a generic rule.**',
 ['Acute aortic syndrome, stroke and pregnancy-related emergencies need their own guidance.', 'Clinical response and organ perfusion are as important as the monitor number.'],
 [['General initial approach','Controlled partial reduction'],['Excessive fall','Ischemic risk'],['Specific emergency','Use its dedicated target']], [A,E])
q('A severely hypertensive patient has headache, confusion, visual symptoms and MRI showing posterior vasogenic edema. Which syndrome is most likely?',
 'Posterior reversible encephalopathy syndrome in the hypertensive context',[
 ('A definite territorial cerebral infarct from the edema distribution alone','Vasogenic posterior edema has a different typical mechanism, although competing diagnoses require assessment.'),
 ('An uncomplicated tension headache with no organ injury','Confusion and imaging abnormalities indicate more than an isolated headache.'),
 ('A normal adaptation to high BP that needs no treatment','The neurological syndrome requires urgent evaluation and controlled treatment.')],
 'Severe pressure can overwhelm cerebral autoregulation',
 '**Vasogenic edema can produce seizures, visual change and encephalopathy.**',
 ['PRES also occurs in other settings, including immune therapy, renal disease and eclampsia.', 'The term reversible does not guarantee no permanent injury.'],
 '**Use controlled pressure management and treat associated triggers.**',
 ['Evaluate seizures and other neurological emergencies.', 'Avoid an uncontrolled abrupt pressure fall.'],
 [['PRES','Vasogenic edema syndrome'],['Ischemic stroke','Different tissue injury and BP pathway'],['Management','Cause-specific monitored care']], [A,E], 'clinical_scenario')
q('Which statement about renal denervation in resistant hypertension is most accurate?',
 'It may be considered in selected patients after confirmation and shared decision-making, but does not replace foundational evaluation and treatment',[
 ('It is a guaranteed cure allowing every medication to be stopped','Responses vary and ongoing treatment may remain necessary.'),
 ('It should precede basic adherence and ambulatory BP assessment','Pseudoresistance must be excluded first.'),
 ('It proves that secondary endocrine causes can be ignored','Cause assessment remains important.')],
 'A procedure is a selected option, not a shortcut around diagnosis',
 '**Current guidance allows a limited role after careful selection.**',
 ['Anatomy, kidney function, BP phenotype and preferences matter.', 'Benefits and uncertainties should be explained honestly.'],
 '**Continue lifestyle and pharmacological management as indicated.**',
 ['Assess response with reliable out-of-office readings.', 'Do not promise universal medication independence or an outcome benefit beyond established evidence.'],
 [['Before procedure','Confirm true hypertension and regimen'],['Selection','Anatomy, renal status and preferences'],['After procedure','Continue response-based care']], [E,A])
q('A pregnant patient needs treatment of severe hypertension. Which drug is an accepted acute option when clinically appropriate?',
 'Intravenous labetalol',[
 ('Enalapril during pregnancy as the routine first choice','ACE inhibitors are not appropriate in pregnancy.'),
 ('Valsartan during pregnancy as a safer ARB substitute','ARBs also have important fetal risk and are not the substitute.'),
 ('Aliskiren as a preferred pregnancy RAS blocker','Direct renin inhibition is not an accepted pregnancy alternative.')],
 'Pregnancy changes antihypertensive selection',
 '**Labetalol, hydralazine or immediate-release oral nifedipine are accepted acute options in suitable contexts.**',
 ['Choice depends on urgency, route, comorbidity and local obstetric protocol.', 'Assess preeclampsia and maternal organ injury.'],
 '**Do not copy a nonpregnant RAS-blocking regimen.**',
 ['Magnesium sulfate may be indicated for seizure prevention in preeclampsia but is not the same as the antihypertensive plan.', 'Maternal and fetal assessment and delivery decisions require obstetric expertise.'],
 [['Accepted acute options','Labetalol, hydralazine, oral nifedipine'],['ACE inhibitor/ARB','Avoid during pregnancy'],['Seizure prevention','Separate magnesium indication']], [A,E], 'clinical_scenario')
q('A hypertensive patient has CKD with significant albuminuria and no contraindication to RAS blockade. Which drug strategy is generally appropriate?',
 'An ACE inhibitor or ARB with renal and potassium monitoring',[
 ('An ACE inhibitor plus an ARB to maximize blockade routinely','Dual blockade increases adverse effects and is not the standard approach.'),
 ('Avoid all RAS treatment solely because CKD is present','Albuminuric CKD is an important indication when treatment is tolerated.'),
 ('Choose a drug without reviewing potassium or kidney function','Monitoring is central to safe treatment.')],
 'Albuminuria identifies a renal-protection opportunity',
 '**RAS blockade can reduce intraglomerular pressure and albuminuria in suitable CKD.**',
 ['Check creatinine and potassium after initiation or dose changes.', 'A substantial unexpected change requires assessment of volume, interactions and renovascular disease.'],
 '**Treat the whole kidney and cardiovascular risk profile.**',
 ['Appropriate SGLT2 therapy and other measures may have additional indications.', 'Do not combine an ACE inhibitor and ARB simply to chase a lower urine value.'],
 [['Albuminuric CKD','ACE inhibitor or ARB when suitable'],['Dual RAS blockade','Not routine'],['Monitoring','Creatinine, potassium and pressure']], [A,E], 'clinical_scenario')
q('An older treated patient has seated BP 126/72 but develops dizziness with a substantial standing BP fall. What is the appropriate next principle?',
 'Assess orthostatic symptoms, medication and volume status and individualize the target',[
 ('Add another drug solely to push seated systolic BP below 120','This ignores symptomatic intolerance.'),
 ('Use the seated reading as proof that falls cannot be pressure related','Standing physiology can differ substantially.'),
 ('Stop all cardiovascular therapy permanently without assessment','A targeted review is preferable to indiscriminate withdrawal.')],
 'A treatment target must be safe in the patient\'s daily posture',
 '**Symptomatic orthostatic hypotension requires a specific assessment.**',
 ['Measure pressure after an appropriate standing interval and review symptoms.', 'Diuretics, vasodilators, autonomic disease and dehydration can contribute.'],
 '**Balance long-term prevention against current harm.**',
 ['Adjust the responsible regimen and consider more individualized pressure goals.', 'A normal clinic seated value does not establish adequate cerebral perfusion during standing.'],
 [['Seated measurement','One part of assessment'],['Standing symptoms and fall','Potential treatment-limiting issue'],['Plan','Targeted adjustment and reassessment']], [A,E], 'clinical_scenario')

if __name__=='__main__':
    finalize('Cardiology',9,'Hypertension','cardiology-hypertension',rows,28)
