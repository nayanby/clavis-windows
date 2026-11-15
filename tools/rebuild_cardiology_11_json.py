"""Original hypertension chapter; incomplete drafts are not installed."""
import json,re
from qbank_json_chapters import question as Q,save,ROOT
DOC='11. Systemic Hypertension and Hypertensive Emergencies'
R={
 'AHA2025':('AHA/ACC high blood pressure guideline, 2025','https://doi.org/10.1161/CIR.0000000000001356'),
 'ESC2024':('ESC elevated blood pressure and hypertension guideline, 2024','https://doi.org/10.1093/eurheartj/ehae178'),
 'PA2025':('Endocrine Society primary aldosteronism guideline, 2025','https://www.endocrine.org/clinical-practice-guidelines/primary-aldosteronism-2'),
 'BEDMED':('BedMed randomized medication-timing trial, 2025','https://doi.org/10.1001/jama.2025.4390')}
R['AMLODIPINE']=('Amlodipine prescribing information, DailyMed','https://www.dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=1080fcea-a5da-499d-a855-690c13559071')
R['DASH']=('NHLBI DASH eating plan','https://www.nhlbi.nih.gov/health/dash-eating-plan')
R['SODIUM']=('WHO sodium reduction recommendations','https://www.who.int/news-room/fact-sheets/detail/sodium-reduction')
R['SSASS']=('SSaSS: salt substitution and cardiovascular outcomes, 2021','https://doi.org/10.1056/NEJMoa2105675')
SECTIONS=[
 ('Measurement classification and blood-pressure phenotypes',[
  'Apply the AHA 2025 systolic-or-diastolic category using confirmed average pressure',
  'Distinguish ESC 2024 elevated pressure from AHA stage-one hypertension',
  'Correct measurement conditions before interpreting a nonstandard office reading',
  'Recognize undercuffing as a cause of falsely elevated pressure and apparent resistance',
  'Use framework-specific home and ambulatory thresholds rather than transferring an office cutoff',
  'Recognize untreated white-coat hypertension and plan surveillance without reflex escalation',
  'Recognize masked hypertension despite apparently reassuring office readings',
  'Diagnose orthostatic hypotension using timed postural measurements',
  'Identify nocturnal hypertension and nondipping with appropriate limitations']),
 ('Risk assessment treatment thresholds and targets',[
  'Initiate treatment at the AHA 2025 lower threshold in an appropriate high-risk patient',
  'Apply the three-to-six-month lifestyle trial and subsequent drug decision in lower-risk AHA stage-one disease',
  'Apply the ESC elevated-pressure treatment pathway using risk and repeat confirmation',
  'Use the AHA general treatment target while recognizing individual tolerability',
  'Apply the ESC systolic target with orthostatic frailty and age-related exceptions',
  'Evaluate hypertension-mediated organ damage and baseline renal metabolic and cardiovascular risk']),
 ('Lifestyle and reversible contributors',[
  'Choose a sustainable weight and DASH-style dietary intervention',
  'Translate sodium reduction into a clinically meaningful intake target',
  'Select potassium enrichment only after assessing kidney function and hyperkalemia risk',
  'Address exercise alcohol sleep and relevant medication or substance contributors']),
 ('Initial drug selection and adverse effects',[
  'Choose initial combination treatment in appropriate stage-two hypertension',
  'Use complementary first-line classes rather than dual renin-angiotensin blockade',
  'Select beta-blockade according to a compelling cardiovascular indication',
  'Prefer an ACE inhibitor or ARB in an appropriate albuminuric CKD phenotype',
  'Interpret chlorthalidone efficacy and toxicity in advanced CKD without assuming thiazides cannot work',
  'Recognize thiazide-associated hyponatremia hypokalemia and hyperuricemia',
  'Manage dihydropyridine edema according to its hemodynamic mechanism',
  'Reassess a major creatinine rise or hyperkalemia after renin-angiotensin blockade']),
 ('Resistant hypertension',[
  'Confirm true resistance using adherence adequate doses and out-of-office pressure',
  'Optimize the diuretic and foundational triple regimen before adding drugs',
  'Apply the PATHWAY-2 evidence for fourth-line spironolactone in a suitable patient',
  'Choose an MRA alternative or monitoring plan according to renal and endocrine adverse effects',
  'Recognize clonidine withdrawal and other treatment-related rebound problems',
  'Place renal denervation within a selected shared-decision pathway without claiming proven event reduction']),
 ('Secondary hypertension',[
  'Apply the 2025 Endocrine Society broader primary-aldosteronism screening approach',
  'Interpret aldosterone renin and the ratio with potassium medications and assay-specific thresholds',
  'Choose confirmatory testing or a justified exception for a strong aldosterone phenotype',
  'Use adrenal venous sampling rather than CT appearance alone for appropriate surgical lateralization',
  'Choose unilateral adrenalectomy versus MRA treatment for confirmed primary aldosteronism',
  'Distinguish routine atherosclerotic renal-artery stenosis from recurrent flash-pulmonary-edema presentations',
  'Recognize renal fibromuscular dysplasia and its revascularization strategy',
  'Evaluate obstructive sleep apnea without assuming CPAP replaces all antihypertensive therapy',
  'Sequence alpha and beta blockade in a catecholamine-secreting tumor',
  'Distinguish Liddle syndrome from aldosterone-mediated low-renin hypertension',
  'Recognize coarctation through arm-leg and pulse findings']),
 ('Hypertensive emergencies and severe asymptomatic pressure',[
  'Define emergency through acute organ injury rather than a pressure number alone',
  'Use the usual controlled initial BP reduction sequence when no disease-specific exception applies',
  'Choose a titratable IV agent according to organ involvement and contraindications',
  'Evaluate malignant hypertension-associated microangiopathy without overlooking a competing TMA',
  'Avoid unnecessary rapid IV lowering in severe asymptomatic hypertension']),
 ('Disease-specific emergency treatment',[
  'Use anti-impulse sequencing and targets in acute aortic syndromes',
  'Treat hypertensive acute pulmonary edema with appropriate vasodilation and respiratory support',
  'Select pressure treatment in acute coronary ischemia without compromising coronary perfusion',
  'Apply an appropriate intracerebral-hemorrhage pressure strategy to the stated severity range',
  'Apply ischemic-stroke pressure thresholds according to reperfusion eligibility',
  'Treat a catecholamine or stimulant-associated hypertensive crisis with appropriate sequencing',
  'Treat persistent severe pregnancy hypertension and distinguish magnesium seizure prophylaxis',
  'Choose ongoing pregnancy-compatible therapy and avoid fetotoxic renin-angiotensin agents']),
 ('Landmark treatment-target trials',[
  'Interpret SPRINT eligibility benefits and adverse effects without extrapolating to excluded diabetes or stroke',
  'Distinguish the ACCORD-BP primary outcome from its stroke result',
  'Apply BPROAD evidence in type-two diabetes without confusing it with ACCORD',
  'Interpret STEP blood-pressure targets and population limitations',
  'Apply HYVET to selected adults aged eighty or older without withholding all treatment solely for age'])]
rows=[]
def S(h,t,*children):return h,[(t,list(children))]
def add(*a,**k):rows.append(Q(*a,**k))

add(SECTIONS[0][0],'AHA Blood-Pressure Categories and Isolated Diastolic Elevation',
 'An untreated adult has a properly measured average office BP of 128/84 mmHg on repeated visits. Under AHA/ACC 2025 classification, which category applies?',
 'Stage 1 hypertension',[
 ('Normal blood pressure','Normal AHA pressure requires systolic below 120 and diastolic below 80 mmHg. The patient does not meet either combined normal condition, and the diastolic result specifically reaches the stage-one range.'),
 ('Elevated blood pressure','AHA elevated pressure means systolic 120–129 with diastolic below 80 mmHg. The systolic value fits that interval but the diastolic value moves the classification to the higher category.'),
 ('Stage 2 hypertension','Stage two requires systolic at least 140 or diastolic at least 90 mmHg. The supplied repeated average reaches neither threshold; the stage-one diastolic elevation should not be overstaged.')],
 [S('Use the Higher Systolic or Diastolic Category','**AHA classification uses either component when the systolic and diastolic categories differ.** The patient has isolated diastolic elevation into the stage-one range despite a systolic value below 130 mmHg.',
    'Normal and elevated categories use combined conditions. Hypertension stages can be reached by the systolic or the diastolic component, so reading only the top number can misclassify the patient.',
    'The question supplies a repeated standardized average. One rushed or technically poor reading would require confirmation rather than automatically establishing the chronic category.'),
  S('Separate Classification From the Treatment Decision','**Stage 1 is a pressure category, not an automatic instruction to give the same drugs to every patient.** Assess clinical CVD, diabetes, CKD and estimated cardiovascular risk and address lifestyle.',
    'AHA 2025 uses a PREVENT ten-year CVD risk threshold of 7.5% for a relevant higher-risk treatment pathway. Lower-risk persistent stage-one pressure is reassessed after a three-to-six-month lifestyle trial before the subsequent medication decision.',
    'Use home or ambulatory measurements when appropriate to identify a white-coat or masked pattern. Review organ damage, age, tolerability and patient circumstances before selecting therapy. A classification label also does not establish a hypertensive emergency: acute target-organ injury is a separate requirement. When comparing sources, specify the society and year because ESC uses a different elevated-pressure category while retaining an office hypertension threshold of 140/90 mmHg. The numerical finding is therefore interpreted within a named framework rather than treated as a universal terminology rule.')],['AHA2025','ESC2024'],
 table=(['AHA/ACC 2025 category','Standardized office average'],[['Normal','SBP <120 AND DBP <80 mmHg'],['Elevated','SBP 120–129 AND DBP <80 mmHg'],['Stage 1','SBP 130–139 OR DBP 80–89 mmHg'],['Stage 2','SBP ≥140 OR DBP ≥90 mmHg']] ),style='direct')

add(SECTIONS[0][0],'ESC Elevated Pressure Versus AHA Stage One',
 'A confirmed standardized office BP is 132/82 mmHg. Which pairing correctly names the AHA/ACC 2025 and ESC 2024 categories?',
 'AHA stage 1 hypertension; ESC elevated blood pressure',[
 ('AHA elevated blood pressure; ESC hypertension','AHA elevated pressure requires diastolic below 80 and systolic below 130. ESC hypertension begins at 140 systolic or 90 diastolic, so neither part of this pairing matches the supplied average.'),
 ('AHA stage 1 hypertension; ESC hypertension','The AHA component is correct. The ESC component incorrectly transfers the American diagnostic threshold to the European framework, where 132/82 remains in the elevated category.'),
 ('AHA stage 2 hypertension; ESC elevated blood pressure','The ESC component is correct. AHA stage two requires a higher systolic or diastolic threshold than supplied, so the American classification is overstated.')],
 [S('Name the Diagnostic Framework','**AHA and ESC use different category boundaries and terminology.** A patient can therefore have stage-one hypertension in one framework and elevated pressure in the other without any disagreement about the measured number.',
    'AHA 2025 defines stage one at systolic 130–139 or diastolic 80–89 mmHg. ESC 2024 retains hypertension at systolic at least 140 or diastolic at least 90 mmHg.',
    'ESC elevated BP includes systolic 120–139 or diastolic 70–89 mmHg when the hypertension boundary is not reached. Non-elevated ESC pressure requires both systolic below 120 and diastolic below 70 mmHg.'),
  S('Do Not Turn Different Names Into Opposite Care Plans','**Both frameworks use risk, confirmation and tolerability when deciding treatment.** An ESC elevated label does not mean that pharmacological treatment is excluded in a high-risk patient.',
    'Diagnostic thresholds, thresholds to start a drug and on-treatment targets are distinct concepts. A treatment target below the diagnostic hypertension threshold is not a contradiction.',
    'Review out-of-office pressure, clinical CVD, diabetes, kidney disease and organ damage before interpreting what the category means for care. A low-risk younger patient and an older patient with established CVD can require different next steps at the same office average. Explain the named framework when communicating a diagnosis or comparing examination answers. Do not combine a US category with a European treatment cutoff and present the result as a single unqualified guideline. The best answer here is a terminology comparison based on verified averages, not a decision about immediate drug number, a BP target or an emergency.')],['AHA2025','ESC2024'],
 table=(['Framework','How 132/82 mmHg is classified','Office hypertension boundary'],[['AHA/ACC 2025','Stage 1 hypertension','SBP ≥130 OR DBP ≥80 mmHg'],['ESC 2024','Elevated blood pressure','SBP ≥140 OR DBP ≥90 mmHg']] ),style='direct')

add(SECTIONS[0][0],'Standardizing a Nonstandard Office Reading',
 'A patient arrives immediately after climbing stairs, drinks coffee and has BP measured while talking with the arm unsupported. The reading is 156/94 mmHg without acute symptoms or organ injury. Which immediate measurement plan is most appropriate?',
 'Repeat after appropriate preparation and seated rest with a supported arm and correct upper-arm cuff',[
 ('Use the highest of three immediate post-exertional readings to set the chronic category','Repeated readings are valuable when obtained properly. Selecting the maximum from the same nonstandard post-exertional conditions preserves measurement bias rather than establishing a reliable chronic average.'),
 ('Use a wrist reading with the hand resting below heart level','A validated wrist device can be useful when upper-arm measurement is unsuitable, but positioning is critical. A wrist below heart level introduces hydrostatic error and does not correct the supplied technique problem.'),
 ('Use the first standing measurement as the replacement for resting office BP','Standing measurements are appropriate for postural symptoms and orthostatic assessment. They answer a different physiological question and should not replace a properly prepared resting office reading.')],
 [S('Correct Preparation and Position Before Interpreting the Number','**A technically poor reading can overestimate usual pressure and lead to unnecessary treatment.** Allow quiet seated rest and use a validated device with a cuff matched to the upper arm.',
    'Avoid smoking, caffeine and exercise for at least thirty minutes before a planned resting measurement when feasible. Empty the bladder, support the back and arm and keep the feet flat with legs uncrossed.',
    'Rest quietly for at least five minutes and position the supported cuff at heart level. Do not talk during rest or measurement. Take repeated readings at appropriate intervals and use their average rather than selecting the highest value.'),
  S('Confirm the Phenotype Without Ignoring an Emergency','**The next step depends on the clinical context as well as measurement quality.** This stem explicitly excludes acute organ injury, so a chronic diagnosis or escalation should not be built on the nonstandard observation alone.',
    'If a patient instead has concerning chest pain, neurological findings, pulmonary edema or another acute syndrome, assessment and treatment must proceed promptly while measurements are verified.',
    'Measure both arms initially and investigate a persistent meaningful difference, generally using the higher-reading arm for subsequent management. Home or ambulatory monitoring can help confirm usual pressure after the office technique is corrected. A repeated high reading under proper conditions deserves follow-up even if the first one was flawed. Conversely, attributing every elevation to anxiety without checking is also inappropriate. The purpose of standardization is to obtain a usable physiological estimate, not to find a lower number by choosing a different limb, posture or device until the result appears reassuring.')],['AHA2025','ESC2024'])

add(SECTIONS[0][0],'Undercuffing and Apparent Resistant Hypertension',
 'An adult with a large upper-arm circumference has high office BP on three medicines. The clinic has been using a standard cuff visibly too small for the arm. Which action is most appropriate before labeling true resistant hypertension?',
 'Repeat measurement with a validated device and an appropriately sized cuff',[
 ('Add spironolactone on the basis of the current office average','Spironolactone is useful in suitable true resistant hypertension. The supplied cuff mismatch creates a remediable measurement bias that must be corrected before adding a fourth drug.'),
 ('Perform ambulatory monitoring using the same undersized cuff','ABPM helps identify white-coat effects and usual pressure. It still requires correct cuff sizing; moving the same measurement error outside the clinic does not make the estimate valid.'),
 ('Begin renal-artery imaging as the first explanation for resistance','Renovascular assessment is appropriate with a compatible phenotype and selected indications. It should not precede correction of a known technical cause of apparent resistance in the supplied stable case.')],
 [S('Match the Inflatable Bladder to Arm Circumference','**A cuff that is too small generally overestimates pressure.** Undercuffing is particularly relevant in obesity and can create an apparent need for additional drugs.',
    'ESC 2024 describes a bladder length of roughly 75%–100% and width of 35%–50% of arm circumference. Follow the validated device’s specified circumference range rather than assuming every standard cuff fits.',
    'A cuff that is too large can bias the result in the opposite direction. Conical arms and very large circumferences may need a validated alternative cuff or approach rather than improvising with an unsuitable device.'),
  S('Exclude Pseudoresistance Before Escalation','**True resistant hypertension requires reliable pressure assessment as well as an adequate treatment regimen.** Confirm out-of-office pressure, adherence, doses and diuretic suitability after correcting technique.',
    'Review interfering agents, sodium intake, sleep apnea and secondary causes according to the phenotype. The existence of one measurement error does not prove that the patient has no hypertension.',
    'Arrange repeat measurements and a clear follow-up plan and monitor for hypotension if apparent resistance resolves while several drugs are already being taken. Device validation and cuff size are separate requirements: a validated monitor used with an incompatible cuff can still mislead. Conversely, a normal pressure obtained with an oversized cuff does not establish control. The case tests a common correctable source of classification and treatment error. Appropriate technical reassessment comes before an MRA prescription or an invasive or expensive secondary-cause pathway, while any genuine acute organ-injury symptoms would require prompt evaluation on their own merits.')],['AHA2025','ESC2024'])

add(SECTIONS[0][0],'ESC Home and Ambulatory Diagnostic Thresholds',
 'Under ESC 2024, which out-of-office average reaches the diagnostic threshold for hypertension?',
 'A 24-hour ambulatory average of 130/80 mmHg',[
 ('A home average of 130/80 mmHg','That average is relevant to some American threshold mappings and to elevated-pressure risk assessment. ESC uses a home diagnostic hypertension threshold of at least 135 systolic or 85 diastolic mmHg.'),
 ('An awake ambulatory average of 130/80 mmHg','Awake ambulatory pressure is assessed separately from the full 24-hour average. ESC’s daytime hypertension threshold is at least 135 systolic or 85 diastolic mmHg, so this lower awake average does not meet it.'),
 ('A sleep ambulatory average of 110/65 mmHg','Sleep pressure has a lower threshold than daytime pressure. ESC uses at least 120 systolic or 70 diastolic mmHg for nocturnal hypertension; 110/65 belongs to a different lower reference mapping.')],
 [S('Use the Threshold for the Setting Being Measured','**Office, home, awake, sleep and full-day averages are not interchangeable.** Sleep values normally lower the twenty-four-hour average, so its diagnostic boundary differs from the daytime boundary.',
    'Under ESC, office hypertension begins at 140/90 mmHg, home and daytime ambulatory hypertension at 135/85 mmHg, the twenty-four-hour average at 130/80 mmHg and nighttime hypertension at 120/70 mmHg.',
    'Either a systolic or a diastolic component at or above its threshold is sufficient for that setting. A slash in a compact table does not mean that both values must be elevated simultaneously.'),
  S('Review Recording Quality and the Named Framework','**A usable ABPM study needs an appropriate cuff, enough valid readings and accurate wake–sleep information.** A single isolated peak is not the same as an elevated time-period average.',
    'Use a diary to interpret sleep, work, exercise, symptoms and medication timing. Assess whether disturbed sleep or measurement artifacts could affect interpretation.',
    'Home monitoring is valuable for repeated resting values but usually does not characterize sleep pressure. ABPM is useful when a white-coat or masked phenotype or a nocturnal problem is suspected. American guidance also maps out-of-office values to its lower office threshold; do not silently substitute those mappings into the ESC diagnostic table. Confirmation, cardiovascular risk and organ damage determine the clinical plan after the phenotype is identified. The question names ESC and the monitoring interval so the numerical answer is defensible rather than dependent on an unstated society or on a single nonrepresentative reading.')],['ESC2024','AHA2025'],
 table=(['ESC 2024 setting','Hypertension if SBP or DBP reaches'],[['Office','140 or 90 mmHg'],['Home average','135 or 85 mmHg'],['Awake ABPM average','135 or 85 mmHg'],['24-hour ABPM average','130 or 80 mmHg'],['Sleep ABPM average','120 or 70 mmHg']] ),style='direct')

add(SECTIONS[0][0],'Untreated White-Coat Hypertension',
 'An untreated adult has repeated standardized office readings around 148/92 mmHg. Reliable home and ambulatory averages are below the corresponding ESC diagnostic thresholds. Which BP phenotype is present?',
 'White-coat hypertension',[
 ('Masked hypertension','Masked hypertension is the reverse discordance: office pressure is below the diagnostic threshold while home or ambulatory pressure is elevated. This patient’s excess is in the office setting.'),
 ('Sustained hypertension','Sustained hypertension requires elevated pressure both in the office and in the relevant out-of-office setting. The supplied reliable home and ambulatory findings do not meet that pattern.'),
 ('White-coat uncontrolled hypertension','This term describes a treated patient whose office readings suggest poor control while out-of-office pressure is controlled. The stem specifies no treatment, so white-coat hypertension is the appropriate untreated phenotype.')],
 [S('Define the Discordance in the Correct Treatment Setting','**White-coat hypertension is an untreated office-high, out-of-office-below-threshold pattern.** Correct technique and a reliable home or ambulatory study are needed before assigning it.',
    'Under ESC 2024, an office average of at least 140 systolic or 90 diastolic mmHg is compared with home or awake ambulatory 135/85 mmHg and twenty-four-hour ambulatory 130/80 mmHg boundaries.',
    'A lower out-of-office result is not automatically normal if it still exceeds the relevant threshold. Review the actual average and setting rather than merely noting that it is lower than the clinic value.'),
  S('Plan Risk Assessment and Surveillance','**White-coat hypertension should not trigger reflex drug escalation from the office number alone.** Assess overall cardiovascular risk, kidney disease and hypertension-mediated organ damage.',
    'Provide appropriate lifestyle measures and repeat out-of-office assessment over time. Some patients progress to sustained hypertension, and the phenotype is not a guarantee of lifelong low risk.',
    'Drug treatment is individualized when risk or organ damage changes the balance; do not turn the label into an absolute prohibition on medication. In a treated patient, adding medicines solely to normalize an office reading can cause hypotension at home. Conversely, a convincing history of high readings outside the clinic deserves investigation even if one home series was reassuring. ABPM can clarify nighttime pressure that ordinary home monitoring may miss. Document whether the patient is untreated or treated so the terminology and action are consistent. The key interpretation combines the two measurement environments with treatment status rather than equating an office-high result with established sustained disease.')],['ESC2024','AHA2025'])

add(SECTIONS[0][0],'Masked Hypertension Despite Reassuring Office Values',
 'An untreated adult has repeated office BP around 126/76 mmHg but validated home averages of 146/92 mmHg and an awake ambulatory average of 143/89 mmHg. What is the most appropriate interpretation?',
 'Masked hypertension requiring cardiovascular-risk and treatment assessment',[
 ('White-coat hypertension requiring office-only follow-up','White-coat hypertension has elevated office pressure with lower out-of-office values. The supplied pattern is opposite, and office-only follow-up would continue to miss the actual pressure burden.'),
 ('Normotension because repeated office measurements are below 140/90 mmHg','A below-threshold office average does not negate reliable elevated out-of-office pressure. Home and ambulatory evidence must be incorporated into diagnosis and care.'),
 ('Transient home-measurement artifact without a hypertension phenotype','Technique and device artifacts are genuine causes of discordant readings and must be checked. Here validated home measurements are corroborated by ABPM, making a measurement-only dismissal less defensible.')],
 [S('Identify the Hidden Pressure Burden','**Masked hypertension means office pressure is below the diagnostic boundary while the appropriate out-of-office average is elevated.** It can explain organ damage that appears disproportionate to clinic readings.',
    'The home and awake ambulatory averages in the stem exceed the ESC 135/85 mmHg threshold. They also exceed relevant American hypertension mappings, so the basic interpretation is not dependent on a borderline framework difference.',
    'In a treated patient the analogous phenomenon is masked uncontrolled hypertension: the clinic appears controlled while pressure elsewhere remains high.'),
  S('Confirm Quality and Act on Risk','**Reliable out-of-office hypertension deserves management rather than reassurance from the clinic number alone.** Review measurement technique, cuff size, medication or substance exposure, work and sleep patterns and relevant symptoms.',
    'Assess kidney function, albuminuria, ECG and other indicated markers of organ damage and cardiovascular risk. Select lifestyle and drug treatment using the confirmed phenotype, comorbidities and applicable guideline.',
    'ABPM can identify nocturnal hypertension or a work-related pattern not captured by occasional home readings. Do not infer that anxiety at home is the cause without evaluating the record, particularly when two methods agree. Conversely, an isolated unvalidated watch reading should not establish masked hypertension. Explain how and when to monitor and arrange follow-up for treatment response and adverse effects. A patient whose office pressure is already modest may need careful out-of-office titration to avoid excessive lowering during other periods. The objective is durable control of the patient’s real pressure exposure, not normalization of a clinic measure that was already reassuring.')],['ESC2024','AHA2025'])

add(SECTIONS[0][0],'Timed Assessment of Orthostatic Hypotension',
 'After five minutes supine rest, an older adult has BP 158/84 mmHg. At one minute after standing it is 132/76 mmHg with lightheadedness, and at three minutes it is 134/76 mmHg. Which interpretation is most appropriate?',
 'Orthostatic hypotension based on the sustained systolic fall',[
 ('No orthostatic hypotension because standing systolic pressure remains above 120 mmHg','The usual definition is based on the fall from baseline, not a requirement to reach an absolute systolic value below 120. The supplied symptomatic systolic decrease exceeds the standard threshold.'),
 ('No orthostatic hypotension because diastolic pressure fell by less than 10 mmHg','A qualifying systolic or diastolic fall can establish the usual definition. Both components do not need to cross their thresholds simultaneously.'),
 ('Postural orthostatic tachycardia syndrome based on symptoms alone','POTS requires an appropriate sustained heart-rate response and clinical context without the defining orthostatic hypotension. No heart-rate criterion is supplied, while a clear BP fall is documented.')],
 [S('Measure the Change at Defined Time Points','**Orthostatic hypotension is usually a sustained fall of at least 20 mmHg systolic or 10 mmHg diastolic within three minutes of standing.** Symptoms support clinical significance but are not required in every case.',
    'Obtain a resting baseline after about five minutes and repeat at one and three minutes after standing. The patient’s systolic fall is 26 mmHg at one minute and 24 mmHg at three minutes.',
    'A higher systolic threshold is used in some autonomic settings with marked supine hypertension. This question uses the standard guideline definition rather than silently applying a different specialist convention.'),
  S('Manage Coexisting Hypertension and Postural Symptoms Together','**Orthostatic hypotension does not mean that every antihypertensive must be stopped.** Assess volume status, anemia, autonomic disease, heart rate and drug effects, including alpha-blockers and other vasodilating or sedating medicines.',
    'Review falls, meals, dehydration and the timing of symptoms. Supine hypertension can coexist with impaired standing tolerance, making a single seated target insufficient for the full management problem.',
    'Correct reversible contributors and individualize the pressure target and regimen. Avoid rapid escalation from the supine value without considering symptomatic standing measurements, but also avoid abandoning cardiovascular-risk treatment without reassessment. Delayed symptoms may require longer standing or specialist evaluation beyond a normal initial three-minute test. A patient with a convincing postural history therefore deserves further assessment if the standard test is negative. The present measurements are already diagnostic under the stated rule and demonstrate why a modest absolute standing systolic pressure can coexist with clinically important orthostatic hypotension.')],['ESC2024','AHA2025'])

add(SECTIONS[0][0],'Nocturnal Hypertension and a Nondipping Pattern',
 'A reliable ABPM study shows an awake average of 138/84 mmHg and a sleep average of 132/78 mmHg. Which interpretation best fits ESC 2024?',
 'Nocturnal hypertension with a reduced nighttime dip',[
 ('Normal nocturnal pressure because it is lower than the awake average','A nighttime value can be lower than daytime yet still exceed the sleep hypertension threshold. The supplied 132/78 is above the ESC 120/70 mmHg nighttime boundary.'),
 ('An extreme-dipping pattern with a normal sleep pressure','Extreme dipping means a much larger relative nighttime reduction, generally more than 20%. The systolic decrease here is only about 4%, and the sleep average remains elevated.'),
 ('A reverse-dipping pattern because the sleep average exceeds the nocturnal threshold','Reverse dipping refers to sleep pressure higher than awake pressure, not merely pressure above the nighttime hypertension cutoff. The patient’s sleep value is lower than the awake value.')],
 [S('Distinguish the Absolute Sleep Level From the Relative Dip','**Nocturnal hypertension and nondipping are related but different classifications.** One uses an absolute nighttime average and the other compares nighttime with daytime pressure.',
    'ESC nocturnal hypertension begins at sleep systolic at least 120 or diastolic at least 70 mmHg. Here both components exceed the threshold.',
    'A usual nighttime fall is around 10%–20%. The systolic fall from 138 to 132 is approximately 4%, supporting reduced dipping. A reverse dip means nighttime pressure rises above daytime, while an extreme dip is greater than 20%.'),
  S('Interpret the Pattern Without Prescribing a Universal Bedtime Rule','**Review sleep quality, the diary and possible contributors such as OSA, CKD, diabetes-related autonomic disease and salt sensitivity.** Cuff-related sleep disruption can affect the apparent pattern.',
    'Nocturnal hypertension carries prognostic information, but the finding does not automatically establish a particular secondary diagnosis. Choose investigations from the wider clinical phenotype.',
    'Optimize adequate around-the-clock treatment and adherence. ESC does not endorse routine bedtime dosing of all BP drugs as an established event-prevention strategy. The 2025 BedMed trial also did not show a reduction in death or major cardiovascular events from bedtime rather than morning administration in its primary-care population. This does not mean that timing is irrelevant to every individual’s symptoms or pressure control; it means that a favorable monitoring pattern must not be converted into a universal proven-outcome claim. Reassess actual pressure exposure and tolerability after a patient-specific change and avoid nocturnal hypotension, falls or impractical dosing schedules. The best interpretation names both the elevated sleep average and the small relative decline.')],['ESC2024','BEDMED'])

add(SECTIONS[1][0],'Risk-Based Drug Initiation in Stage 1 Hypertension',
 'A 58-year-old has confirmed office and home BP averages of 134/84 mmHg. There is no clinical CVD, diabetes or CKD. The PREVENT 10-year CVD risk is 8.2%. Under AHA/ACC 2025 guidance, what is the best next step?',
 'Begin antihypertensive medication with lifestyle treatment',[
 ('Use lifestyle treatment alone for six months before considering medication','A three-to-six-month lifestyle-first approach applies to otherwise lower-risk stage-one hypertension. This patient crosses the current PREVENT risk threshold, making pharmacological treatment appropriate alongside lifestyle changes.'),
 ('Defer medication until the average BP reaches 140/90 mmHg','That pressure is a medication-initiation threshold regardless of estimated risk, but it is not the only threshold. Confirmed stage-one pressure with sufficiently high cardiovascular risk supports earlier treatment.'),
 ('Repeat annual risk assessment without active BP treatment','Periodic risk reassessment is appropriate during follow-up, including for patients below treatment thresholds. Here the combination of confirmed pressure and present risk already justifies active treatment rather than annual observation alone.')],
 [S('Treatment Eligibility','**AHA/ACC 2025 links the lower medication threshold to cardiovascular risk.** At average BP at least 130/80 mmHg, drug treatment is recommended in adults with clinical cardiovascular disease, previous stroke, diabetes, CKD, or a PREVENT ten-year CVD risk of at least 7.5%.',
    'The supplied 8.2% risk crosses that boundary. Confirmation with reliable measurements has already addressed the possibility that an isolated office reading is driving the decision.',
    'PREVENT estimates broader cardiovascular risk; its percentage should not be substituted directly into an older pooled-cohort ASCVD treatment algorithm with a different cutoff.'),
  S('Treatment and Follow-Up','**Combine a suitable first-line drug with lifestyle measures and monitor the response.** An ACE inhibitor or ARB, a long-acting dihydropyridine calcium-channel blocker, or a thiazide-type diuretic may be appropriate according to comorbidities, kidney function, electrolytes and tolerance.',
    'For example, the usual adult amlodipine starting dose is 5 mg once daily, titrated to a maximum of 10 mg daily. A 2.5 mg starting dose is appropriate in selected small, frail, elderly or hepatically impaired adults. Assess ankle edema and orthostatic symptoms during titration.',
    'The general American goal is below 130/80 mmHg, with individual considerations for pregnancy, institutional care or limited lifespan. Review adherence, home averages and adverse effects during titration. Check creatinine and potassium when selecting renin–angiotensin system blockade and electrolytes when using a diuretic. A ten-year risk score does not identify a secondary cause, determine a specific drug, or establish hypertensive emergency. Those are separate clinical decisions. The examination distinction is between a risk-based threshold to start treatment and the subsequently chosen pressure target; neither should be inferred from the stage label alone.')],['AHA2025','AMLODIPINE'],
 table=(['Clinical setting in AHA/ACC 2025','Medication initiation'],[['Average BP ≥140/90 mmHg','Medication plus lifestyle regardless of estimated risk'],['Average BP ≥130/80 with CVD, stroke, DM, CKD or PREVENT risk ≥7.5%','Medication plus lifestyle'],['Average BP ≥130/80 with PREVENT risk <7.5%, without the listed high-risk conditions','Initial lifestyle trial; add medication if persistent after 3–6 months']]))

add(SECTIONS[1][0],'Persistent Lower-Risk Stage 1 Hypertension',
 'A 46-year-old without CVD, stroke, diabetes or CKD has PREVENT 10-year CVD risk of 4%. After six months of documented diet, exercise and weight reduction, validated home and standardized office averages remain 134/82 mmHg. Under AHA/ACC 2025, which strategy is best?',
 'Add an antihypertensive drug while continuing lifestyle measures',[
 ('Continue lifestyle treatment alone until the estimated risk exceeds 7.5%','The risk threshold determines the initial pathway, but persistent stage-one pressure after a completed three-to-six-month lifestyle trial supports adding medication even when ten-year risk remains below 7.5%.'),
 ('Defer treatment changes until office BP reaches 140/90 mmHg','Waiting for stage two was a common interpretation of earlier low-risk management. The 2025 American recommendation specifically addresses persistent lower-risk stage-one pressure after lifestyle intervention.'),
 ('Obtain ABPM before any treatment change despite concordant validated readings','ABPM is useful for discordant readings, suspected nocturnal hypertension or uncertain measurement quality. The stem already establishes persistent hypertension with reliable concordant measurements, so an additional mandatory confirmation step should not delay the indicated decision.')],
 [S('Treatment Threshold After Lifestyle Intervention','**Lower ten-year risk changes initial timing rather than excluding later drug treatment.** AHA/ACC 2025 recommends starting medication when average BP remains at least 130/80 mmHg after a three-to-six-month lifestyle trial in otherwise lower-risk adults.',
    'The patient has completed the trial and remains above threshold on two reliable measurement methods. Continuing to repeat an unchanged lifestyle-only plan indefinitely would miss the specified escalation point.',
    'A low short-term risk estimate can coexist with substantial cumulative lifetime exposure to high pressure. Conversely, a very young patient outside a risk equation’s validated age range should not be assigned a fabricated PREVENT percentage.'),
  S('Long-Term Management','**Continue the successful lifestyle changes when adding medication.** Their benefits extend beyond the small remaining pressure difference and may reduce the dose burden needed for durable control.',
    'Use a complementary first-line drug selected from the patient’s clinical profile; do not infer that every stage-one patient needs immediate two-drug initiation. The preferred two-agent American starting strategy specifically concerns stage-two hypertension.',
    'Monitor home pressure, postural symptoms and drug-specific adverse effects, and aim for the usual American target below 130/80 mmHg when appropriate. Reassess cardiovascular and renal risk over time because diabetes, CKD or overt vascular disease may subsequently alter priorities. Confirm adherence and measurement quality before labeling inadequate response as resistance. Severe acute symptoms or organ injury would require a different assessment, but a stable average of 134/82 is a chronic prevention problem rather than an indication for rapid intravenous lowering. This question tests the completed lifestyle trial and the current recommendation, not failure of a named antihypertensive drug.')],['AHA2025'])

add(SECTIONS[1][0],'ESC Treatment of Elevated Blood Pressure at High Risk',
 'A 64-year-old with established coronary disease has confirmed BP of 134/82 mmHg after three months of lifestyle intervention. There is no symptomatic orthostatic hypotension, major frailty or limited life expectancy. Under ESC 2024, what is the most appropriate BP strategy?',
 'Start BP-lowering medication despite the elevated-BP category',[
 ('Continue lifestyle treatment alone until office BP reaches 140/90 mmHg','ESC retains 140/90 as the diagnostic hypertension boundary, but high-risk adults with persistent pressure at least 130/80 after lifestyle treatment can benefit from medication below that boundary.'),
 ('Delay medication until a new SCORE2 estimate confirms risk above 10%','An appropriate risk score can guide decisions in apparently healthy adults. Established coronary disease already identifies a high-risk clinical condition, so a screening risk estimate is not required to rediscover that risk.'),
 ('Start medication only if ambulatory monitoring shows nocturnal hypertension','Nocturnal hypertension may provide additional information, particularly with OSA or discordant measurements. It is not an additional eligibility requirement once persistent elevated BP and an established high-risk condition are present.')],
 [S('Cardiovascular Risk and Treatment Eligibility','**ESC diagnostic categories and drug-treatment thresholds are separate.** In 2024, office hypertension remains at least 140/90 mmHg, while elevated BP includes values below that boundary that may still justify treatment in sufficiently high-risk adults.',
    'Established cardiovascular disease, clinically significant CKD, diabetes, familial hypercholesterolemia or hypertension-mediated organ damage can identify a high-risk condition. Estimated ten-year risk and appropriate risk modifiers guide decisions in adults without these established conditions.',
    'For an eligible high-risk adult with confirmed BP at least 130/80 mmHg after three months of lifestyle intervention, pharmacological BP lowering is recommended. This patient’s coronary disease and persistent pressure meet that pathway.'),
  S('Targets and Drug Selection','**ESC generally recommends an on-treatment systolic target of 120–129 mmHg when well tolerated.** A diastolic range of 70–79 mmHg is considered alongside the systolic goal and the individual clinical setting.',
    'Select treatment according to coronary symptoms, ventricular function, kidney function and other indications. An ACE inhibitor or ARB may fit the vascular-risk profile; a beta blocker may additionally be appropriate for angina or another specific cardiac indication rather than solely because the patient has an elevated pressure category.',
    'Check standing pressure and symptoms during titration. More lenient goals can be appropriate with symptomatic orthostasis, age at least 85 years, significant frailty or limited predicted lifespan. Coronary perfusion, treatment tolerance and the achieved diastolic pressure deserve attention, particularly in an older patient with stiff arteries. The diagnosis has not been renamed hypertension merely because a drug is started: risk-based intervention can occur within the elevated-BP category. State the guideline framework explicitly to avoid confusing this pathway with the American stage-one terminology.')],['ESC2024'])

add(SECTIONS[1][0],'AHA Blood-Pressure Treatment Target',
 'A nonpregnant 59-year-old receiving antihypertensive treatment has no frailty, orthostatic symptoms or limited life expectancy. Which office BP goal best matches the general AHA/ACC 2025 recommendation?',
 'Below 130/80 mmHg',[
 ('Below 140/90 mmHg','This remains an important diagnostic and drug-initiation boundary in several settings, and may be an individualized less intensive goal when tolerance is limited. It is above the general American treatment goal for the uncomplicated adult described.'),
 ('Below 120/70 mmHg','Some trials used an intensive systolic target below 120, but a trial target is not a universal paired systolic-and-diastolic goal for all treated adults. The American overarching recommendation is below 130/80.'),
 ('Systolic 130–139 and diastolic 80–89 mmHg','This range describes American stage-one hypertension rather than the usual desired treated pressure. It could represent an interim response or a tolerated compromise, but not the stated general target.')],
 [S('Treatment Target','**AHA/ACC 2025 recommends a general BP goal below 130/80 mmHg.** The goal refers to properly measured pressure and should be interpreted with the patient’s clinical circumstances rather than a single hurried reading.',
    'Treatment-initiation thresholds answer when to add drugs; a target answers what pressure to seek after treatment begins. A patient started at 148/92 and one started at 134/84 because of high risk may share the same general target.',
    'A trial comparing systolic targets does not automatically establish a diastolic target or validate the same intensity in every excluded population. Measurement technique, baseline comorbidity and adverse-event monitoring influence applicability.'),
  S('Monitoring and Individualization','**Assess benefit and tolerability together.** Use validated home readings and clinical review to detect persistent excess pressure, excessive lowering outside the office and inconsistent adherence.',
    'Ask about dizziness, presyncope and falls; measure standing pressure when indicated. Review creatinine, sodium and potassium according to the drugs used, especially after initiation or titration of a diuretic or renin–angiotensin system blocker.',
    'Institutional care, limited predicted lifespan and pregnancy require additional considerations. A target should support a safe longitudinal plan rather than trigger reflex dose escalation despite clinically important adverse effects. Conversely, the absence of symptoms does not justify accepting persistent above-target pressure without reviewing treatment. Standardize measurement before concluding that apparent resistance is real. When comparing American and European recommendations, specify that ESC 2024 usually expresses the systolic goal as a tolerated range of 120–129 mmHg. The American less-than notation and the ESC range should not be combined into a new invented universal target.')],['AHA2025','ESC2024'],style='direct')

add(SECTIONS[1][0],'Blood-Pressure Targets in Frailty and Orthostatic Hypotension',
 'An 88-year-old with moderate frailty takes three antihypertensives. Seated BP is 132/76 mmHg; standing BP is 106/64 mmHg with recurrent presyncope and a recent fall. Under ESC 2024, what is the best next step?',
 'Review reversible causes and treatment, then individualize a less intensive goal',[
 ('Intensify treatment to obtain a seated systolic pressure of 120–129 mmHg','That range is the usual ESC goal when well tolerated. This patient has symptomatic orthostasis, frailty and age above 85, which are explicit reasons to individualize rather than intensify toward the default range.'),
 ('Maintain the current regimen because the seated pressure is near target','A satisfactory seated value can conceal clinically important standing hypotension. Recurrent presyncope and a fall require assessment of volume status, other medicines and the antihypertensive regimen.'),
 ('Add midodrine while retaining all antihypertensive doses unchanged','A pressor may have a role in persistent symptomatic neurogenic orthostatic hypotension after appropriate assessment. Adding it before evaluating potentially reversible medication or volume contributors can create competing treatment effects and supine hypertension.')],
 [S('Clinical Assessment','**The treatment-limiting finding is symptomatic orthostatic hypotension, not chronological age alone.** The systolic drop is 26 mmHg and the diastolic drop is 12 mmHg, with presyncope and a fall.',
    'Check volume depletion, intercurrent illness, anemia and autonomic dysfunction. Review alpha blockers, nitrates, sedatives and other non-hypertension drugs as well as the antihypertensive regimen.',
    'Document a resting baseline and timed standing measurements. A posture-related pattern can coexist with supine or nocturnal hypertension, so home or ambulatory information may help guide changes.'),
  S('Treatment and Prognosis','**ESC 2024 allows a more lenient individualized target when the usual systolic range is not tolerated.** Symptomatic orthostasis, age at least 85, moderate-to-severe frailty and limited lifespan are important contexts for this decision.',
    'Correct reversible causes and consider reducing or changing the agent most likely to contribute, taking account of compelling indications such as heart failure or angina. Make a supervised, monitored adjustment rather than stopping all cardiovascular treatment abruptly.',
    'Reassess standing symptoms, falls and home pressure after each meaningful change. The goal is the lowest reasonably achievable pressure that is clinically tolerated, not a fixed higher target automatically assigned to every older adult. A robust older person with good tolerance may still benefit from sustained control. Conversely, a normal seated number is not sufficient evidence of safety in someone repeatedly falling on standing. If symptoms persist after appropriate changes, investigate neurogenic orthostasis and consider nonpharmacological measures and specialist treatment. Measures that increase salt or fluid require care when heart failure or CKD is present.')],['ESC2024'])

add(SECTIONS[1][0],'Baseline Evaluation and Hypertension-Mediated Organ Damage',
 'An asymptomatic 52-year-old has newly confirmed sustained hypertension of 152/94 mmHg, a normal examination and no specific secondary-cause clues. Which investigation panel best establishes baseline cardiovascular and renal status?',
 'Creatinine/eGFR, electrolytes, urine ACR, glycemia, lipids and ECG',[
 ('Renal-artery CT angiography, plasma metanephrines and adrenal MRI','These investigations answer selected secondary-cause questions. They are appropriate when renovascular disease or a catecholamine-secreting tumor is suspected, but broad anatomical and endocrine imaging does not replace baseline renal and cardiovascular assessment.'),
 ('Troponin, coronary CT angiography, stress imaging and echocardiography','These tests can be valuable for suspected ischemia, acute myocardial injury or structural disease. An asymptomatic patient without such clues does not require this ischemia-focused panel merely because chronic hypertension is newly diagnosed.'),
 ('Brain MRI, carotid ultrasonography, CT aortography and exercise testing','Neurologic, vascular and exercise investigations are chosen for specific clinical indications. Screening all these territories would not substitute for identifying renal impairment, albuminuria, dysglycemia, dyslipidemia and electrical evidence of cardiac disease.')],
 [S('Baseline Investigations','**Initial evaluation establishes risk, organ involvement and a safe starting point for treatment.** Kidney function and electrolytes influence drug selection and provide a comparator when creatinine, sodium or potassium changes after treatment.',
    'A spot urine albumin-to-creatinine ratio identifies albuminuria that may be missed by a simple dipstick. An abnormal result usually requires appropriate confirmation; albuminuria at least 30 mg/g is clinically relevant, and chronicity is needed before diagnosing CKD from a new finding.',
    'Assess fasting glucose or HbA1c and a lipid profile. Obtain a twelve-lead ECG to look for LV hypertrophy, rhythm abnormalities, previous infarction or conduction disease. The listed panel is the best among the options, not an assertion that it is the entire local baseline workup; urinalysis, blood count, calcium and other routine tests may also be appropriate.'),
  S('Organ Damage and Directed Testing','**Hypertension-mediated organ damage can change cardiovascular-risk assessment and the urgency of durable control.** Relevant findings include LV hypertrophy, albuminuria, reduced eGFR and established vascular or cerebrovascular disease.',
    'Echocardiography is useful when clinical findings, symptoms or ECG abnormalities suggest structural disease; it is not a replacement for the basic renal and metabolic assessment. A normal ECG does not exclude all hypertensive cardiac remodeling.',
    'Investigate secondary causes according to the phenotype and current screening recommendations. Abrupt onset, resistance, marked hypokalemia, characteristic spells or recurrent flash pulmonary edema can redirect testing. The 2025 Endocrine Society guidance also supports broader aldosterone/renin screening, conditional on implementation resources; that recommendation does not justify adrenal imaging before appropriate biochemical assessment. Baseline tests and selected secondary-cause investigations are complementary rather than mutually exclusive. Record renal function and potassium before ACE inhibition, ARB therapy or mineralocorticoid receptor antagonism and repeat them according to the chosen treatment.')],['AHA2025','ESC2024','PA2025'])

add(SECTIONS[2][0],'DASH Eating Pattern and Weight Management',
 'Which dietary pattern best matches the DASH intervention recommended for an overweight adult with uncomplicated hypertension and preserved kidney function?',
 'Vegetables, fruit, whole grains, low-fat dairy, legumes and limited saturated fat',[
 ('Vegetables, fruit, whole grains, full-fat dairy and liberal coconut oil','Several components overlap with DASH, but the pattern should limit saturated fat. Substituting full-fat dairy and liberal coconut oil does not reproduce the recommended low-fat dairy and fat-quality emphasis.'),
 ('Vegetables, lean meat, refined grains and avoidance of dairy and legumes','A diet can include some favorable foods without matching DASH. Refined grains and routine exclusion of low-fat dairy and legumes remove important elements of the studied eating pattern without a stated clinical reason.'),
 ('Whole grains, low-fat dairy, fruit drinks and regular processed-meat servings','Whole grains and low-fat dairy fit, but fruit drinks may supply added sugar and regular processed-meat intake can add substantial sodium. These substitutions do not reproduce the overall DASH pattern; a product containing fruit is not nutritionally equivalent to whole fruit.')],
 [S('Dietary Composition','**DASH emphasizes an overall eating pattern rather than a single supplement.** It combines vegetables, fruit, whole grains, low-fat or fat-free dairy, legumes, nuts and appropriate lean protein while limiting saturated fat and sugar-sweetened foods.',
    'At a reference intake of 2000 kcal/day, NHLBI examples include four to five daily servings each of vegetables and fruit and two to three servings of low-fat or fat-free dairy. Calorie and portion needs vary; these are not a mandatory energy prescription for every adult.',
    'Sodium reduction complements the dietary pattern. Neither a label such as low carbohydrate nor adding one potassium-rich food establishes that the entire diet follows DASH.'),
  S('Weight Management and Monitoring','**For an overweight patient, add a sustainable calorie deficit and physical activity rather than assuming food quality alone guarantees weight loss.** Set a feasible initial weight goal and review waist size, weight trajectory, home BP and medication tolerance.',
    'DASH can be used with an energy intake that maintains weight or with an energy-restricted plan. Diet quality and weight reduction are related but distinct interventions, so the clinical benefit should not be attributed exclusively to one mechanism.',
    'Use accessible local foods, portion guidance and repeated follow-up rather than a rigid short-term list that the patient cannot maintain. Favor unsalted nuts and minimally processed foods when sodium intake is high. Milk alternatives or other substitutions may be needed for intolerance, but they should preserve nutritional adequacy. Assess renal function and potassium before unrestricted potassium enrichment in a patient with CKD or potassium-retaining medicines. Continue indicated antihypertensive medication while assessing the diet’s effect; as BP falls, titration may be needed to avoid symptomatic hypotension. The appropriate dietary plan is a sustained component of cardiovascular prevention, not an acute treatment for severe hypertension with organ injury.')],['DASH','AHA2025'],style='direct')

add(SECTIONS[2][0],'Dietary Sodium and Salt Are Different Quantities',
 'A patient with hypertension is advised to follow the WHO adult sodium target of less than 2 g/day. Which practical instruction correctly translates this into approximate total salt intake?',
 'Keep total salt intake below about 5 g/day, including salt already in foods',[
 ('Keep total salt intake below about 2 g/day, including salt already in foods','Two grams of salt contains only about 0.8 g of sodium. A lower intake may be chosen in some circumstances, but it is not the equivalent of the stated two-gram sodium threshold.'),
 ('Keep total salt intake below about 8 g/day, including salt already in foods','Eight grams of salt contains approximately 3.2 g of sodium. This remains above the specified sodium target despite possibly representing a reduction from a very high baseline.'),
 ('Keep total salt intake below about 10 g/day, including salt already in foods','Ten grams of salt contains about 4 g of sodium, roughly twice the stated sodium limit. Confusing a salt weight with its sodium content can materially weaken the intended intervention.')],
 [S('Sodium-to-Salt Conversion','**Table salt is sodium chloride; its weight is not the weight of sodium alone.** Sodium constitutes approximately 40% of sodium chloride by mass.',
    'Sodium in grams multiplied by about 2.5 gives grams of salt. Thus 2 g sodium corresponds to approximately 5 g salt. Conversely, 1 g salt contains about 400 mg sodium.',
    'WHO recommends less than 2000 mg sodium daily for adults. The limit refers to the total diet, not only salt added at the table. Sodium-containing additives can contribute even when a food is not conspicuously salty.'),
  S('Dietary Implementation','**Identify the patient’s major sources before choosing the intervention.** Packaged snacks, sauces, pickles, processed meats, restaurant meals and cooking salt may contribute differently in different households.',
    'Read sodium per serving and the actual number of servings consumed. A package describing a small serving can underestimate the intake if the whole package is eaten. Use herbs, spices and less processed foods to maintain palatability while reducing sodium.',
    'A dietary sodium target does not mean that the serum sodium concentration should be lowered. Serum sodium chiefly reflects water balance; a normal value neither proves nor disproves excessive dietary sodium. Moderate sustained reduction can support BP control and drug responsiveness, but clinical response varies. Avoid extreme advice that compromises nutrition or ignores volume status in vulnerable patients. If a potassium-enriched salt substitute is considered, assess kidney function, serum potassium and medicines that impair potassium excretion. When medications remain indicated, sodium reduction is complementary rather than a reason to postpone them indefinitely. Explain the unit conversion explicitly because sodium and salt figures on different labels otherwise appear contradictory.')],['SODIUM'],
 table=(['Substance or conversion','Approximate amount'],[['1 g table salt','400 mg sodium'],['2 g sodium','5 g table salt'],['WHO adult sodium recommendation','<2000 mg sodium/day; approximately <5 g salt/day']]),calculation=True)

add(SECTIONS[2][0],'Potassium-Enriched Salt Substitutes in CKD',
 'A 65-year-old with hypertension and previous ischemic stroke has eGFR 24 mL/min/1.73 m² and potassium 5.4 mmol/L while taking losartan. They cite SSaSS to support potassium-enriched cooking salt. Which trial feature is the strongest reason the reported safety cannot be directly applied to this patient?',
 'Exclusion of participants with serious kidney disease or substantial hyperkalemia risk',[
 ('Randomization of villages rather than randomization of individual participants','Cluster randomization affects trial design, contamination and statistical analysis. It does not by itself invalidate a properly analyzed result or explain the particular renal and potassium safety gap in this patient.'),
 ('Enrollment of older high-risk adults or people with previous stroke','This eligibility profile limits extrapolation to young low-risk primary prevention. The patient is older and has previous stroke, so these features support rather than undermine population similarity on that dimension.'),
 ('Use of a combined sodium-reduction and potassium-enrichment intervention','The mixture makes it difficult to attribute benefit exclusively to either electrolyte change. That mechanistic limitation is distinct from whether the trial establishes safety in advanced CKD with existing hyperkalemia.')],
 [S('Potassium Handling and Drug Interactions','**Reduced renal potassium excretion changes the safety of dietary potassium enrichment.** Advanced CKD and renin–angiotensin system blockade can combine to produce clinically important hyperkalemia.',
    'The patient already has potassium of 5.4 mmol/L. Verify the result when appropriate, review the trend, other medicines and clinical context, and manage the hyperkalemia rather than introducing another potassium source.',
    'ACE inhibitors, ARBs, mineralocorticoid receptor antagonists and other potassium-sparing drugs deserve attention. A dietary product can deliver a pharmacologically relevant potassium load even though it is sold as a healthier cooking ingredient.'),
  S('Evidence and Clinical Application','**Salt-substitution trial benefits should be applied to patients with a comparable safety profile.** SSaSS compared a mixture containing 75% sodium chloride and 25% potassium chloride with usual salt and found fewer strokes and major cardiovascular events in its studied population.',
    'The trial excluded people reporting serious kidney disease or using medicines expected to substantially increase potassium. Absence of a significant hyperkalemia signal in the eligible trial population does not establish safety in this patient with advanced CKD and existing hyperkalemia.',
    'Reduce sodium by changing processed-food intake, portion selection, sauces and cooking practices while maintaining nutrition. Individualize dietary potassium advice with the renal team; restriction should not be prescribed indiscriminately to every person with a CKD label. Reassess whether losartan remains indicated and can be safely continued after addressing potassium and other contributors. A potassium binder or drug adjustment may be appropriate, but neither is a blanket license to start an unrestricted potassium salt substitute. The key distinction is between sodium reduction, which remains a useful goal, and the particular potassium-containing method proposed to achieve it.')],['SSASS','AHA2025','ESC2024'])

add(SECTIONS[2][0],'Exercise and Reversible Contributors to Poor BP Control',
 'A 55-year-old with stable uncomplicated hypertension exercises little, drinks 180 g of alcohol weekly and uses ibuprofen most days for knee pain. Which plan best fits ESC 2024 lifestyle advice and contributor review?',
 'Build toward 150 minutes/week of moderate aerobic activity, reduce alcohol and review NSAID use',[
 ('Build toward 75 minutes/week of moderate aerobic activity, maintain alcohol and review NSAID use','Seventy-five minutes can be an alternative weekly target for vigorous activity, not the usual moderate-intensity target. The substantial alcohol intake also warrants reduction rather than being left unchanged.'),
 ('Build toward 150 minutes/week of moderate aerobic activity, maintain alcohol and continue scheduled ibuprofen','The exercise component is appropriate, but it does not neutralize alcohol-related pressure elevation or the potential renal and sodium-retaining effects of regular NSAID exposure.'),
 ('Build toward 75 minutes/week of vigorous activity, reduce alcohol and substitute scheduled naproxen','The exercise and alcohol components are reasonable. Naproxen may be selected for particular analgesic circumstances, but it remains an NSAID and does not remove the need to review drug-related BP elevation and kidney risk.')],
 [S('Physical Activity and Alcohol','**A practical ESC aerobic goal is at least 150 minutes of moderate activity weekly or 75 minutes of vigorous activity.** Add suitable low-to-moderate intensity resistance exercise on two to three days per week.',
    'Progress gradually from the patient’s current activity and joint limitations; walking, cycling or other tolerable activities can be selected. Unstable cardiovascular symptoms or severe uncontrolled disease require assessment before vigorous training.',
    'Alcohol intake of 180 g/week exceeds the ESC upper limit of about 100 g/week of pure alcohol. Counsel reduction, explain local drink sizes and avoid treating the upper limit as a recommended intake. Assess dependence and withdrawal risk when planning reduction in a heavy drinker.'),
  S('Medication and Sleep Review','**Regular NSAIDs can worsen BP control through renal prostaglandin inhibition and sodium retention.** They can also blunt antihypertensive responses and increase kidney risk, especially with a diuretic plus ACE inhibitor or ARB.',
    'Review whether ibuprofen can be reduced or replaced with a clinically appropriate pain strategy; do not assume that another nonselective oral NSAID removes the class effect. Check kidney function and electrolytes when the exposure and regimen warrant it.',
    'Ask about sympathomimetic decongestants, stimulants, glucocorticoids, liquorice-containing products and other relevant exposures. Screen for OSA when snoring, witnessed apneas, daytime sleepiness or resistant hypertension suggests it. Sleep treatment and exercise complement indicated medicines rather than automatically replacing them. A diary of home BP and exposure changes can help assess response. Labeling hypertension resistant before assessing adherence, out-of-office measurements and these reversible factors risks unnecessary escalation. Avoid advising an abrupt unsupervised alcohol withdrawal if there is a history suggesting physiological dependence.')],['ESC2024','AHA2025'])

from cardiology_11_drug_questions import rows as drug_rows, REFERENCES as drug_references
rows.extend(drug_rows)
R.update(drug_references)
from cardiology_11_secondary_questions import rows as secondary_rows, REFERENCES as secondary_references
rows.extend(secondary_rows)
R.update(secondary_references)
from cardiology_11_emergency_questions import rows as emergency_rows, REFERENCES as emergency_references
rows.extend(emergency_rows)
R.update(emergency_references)
from cardiology_11_trial_questions import rows as trial_rows, REFERENCES as trial_references
rows.extend(trial_rows)
R.update(trial_references)

def highlight_values(text):
    return re.sub(r'(?<![\w.])(?:[<>≤≥]\s*)?\d+(?:\.\d+)?(?:[–−-]\d+(?:\.\d+)?)?(?:/\d+(?:[–−-]\d+)?)?\s*(?:mmHg|mg/kg/min|mg/kg/day|mg/kg|mg/hour|mg/h|mg/min|mg/g|mg/dL|mg|g/hour|g/h|g/day|g/week|g|mmol/L|nmol/L|ng/mL/h|ng/dL|µg/kg/min|µg/kg|µg/min|µg/dL|mU/L|mOsm/kg|mL/min/1\.73 m²|mL/min|%)(?!\w)',lambda m:'=='+m.group(0)+'==',text)

if __name__=='__main__':
    existing_path=ROOT/'Cardiology'/(DOC+'.json')
    existing=json.loads(existing_path.read_text(encoding='utf-8')) if existing_path.exists() else None
    decisions=[(t,d)for t,items in SECTIONS for d in items]
    assert len(rows)<=len(decisions)
    for r,(t,d)in zip(rows,decisions):assert r['topic']==t;r['coverageDecision']=d
    for r in rows:
        r['sections']=[(h,[(highlight_values(t),[highlight_values(x)for x in kids])for t,kids in bs])for h,bs in r['sections']]
        if r['table']:
            hs,vs=r['table'];r['table']=(hs,[[highlight_values(x)for x in line]for line in vs])
    # Keep the original nine redistributed questions verbatim. Later draft
    # explanations remain editable while retaining their existing answer slots.
    preserved=[q for q in existing['questions'] if int(q['id'].split('-')[-1])<=9] if existing else []
    answer_indices={q['id']:q['correctIndex'] for q in existing['questions']} if existing else {}
    p=save('Cardiology',11,DOC,rows,R,'Original educational synthesis; incomplete draft, not for installation. Full Harrison text not accessed; independent clinician review not claimed.',preserved_questions=preserved,preserved_answer_indices=answer_indices)
    chapter_status='draft_awaiting_final_review' if len(rows)==len(decisions) else 'draft_in_progress'
    b=json.loads(p.read_text(encoding='utf-8'));b.update(status=chapter_status,plannedQuestions=len(decisions),sourceDocument=DOC+'.docx')
    if existing and 'redistribution' in existing:
        b['redistribution']=existing['redistribution']
        b['redistribution'].update(draftQuestions=len(rows),newQuestionsAfterRedistribution=len(rows)-9)
    p.write_text(json.dumps(b,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    c=dict(subject='Cardiology',chapterNumber=11,chapter=DOC,status=chapter_status,countPolicy='Provisional coverage-driven distinct decisions; not official examination weights.',plannedQuestions=len(decisions),authoredQuestions=len(rows),sections=[dict(section=t,questions=len(items),authoredQuestions=sum(r['topic']==t for r in rows),decisions=items)for t,items in SECTIONS],questionDecisions=[dict(questionId=q['id'],title=q['explanationTeaching']['title'],section=q['topic'],decision=q['coverageDecision'])for q in b['questions']])
    (p.parent/'audit/chapter-11-coverage.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    pp=ROOT/'progress.json';plan=json.loads(pp.read_text(encoding='utf-8'));entry=next(x for x in plan['chapters']if x['subject']=='Cardiology'and x['document']==DOC);entry.update(status=chapter_status,authoredQuestions=len(rows),plannedQuestions=len(decisions),draftQuestions=len(rows),draftQuestionsWithheld=len(rows),newQuestionsAfterRedistribution=len(rows)-9,coverageMap='Cardiology/audit/chapter-11-coverage.json');plan['currentChapter']='Cardiology '+DOC;pp.write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    cardio=[json.loads(f.read_text(encoding='utf-8'))for f in p.parent.glob('*.json')]
    total=sum(len(bank.get('questions',[]))for bank in cardio)
    installed=json.loads((p.parent/'audit/installation-report.json').read_text(encoding='utf-8'))['installedQuestions']
    plan['cardiologyRedistribution'].update(currentAuthoredQuestions=total,currentDraftQuestionsNotInstalled=total-installed)
    pp.write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    summary_path=ROOT/'validation-summary.json';summary=json.loads(summary_path.read_text(encoding='utf-8'))
    summary.update(currentCardiologyAuthoredQuestions=total,currentCardiologyDraftQuestionsNotInstalled=total-installed,nextChapter='Cardiology '+DOC)
    summary_path.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
