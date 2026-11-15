"""Original decision-mapped neurocritical care chapter."""
import json
from qbank_json_chapters import question as Q,save,ROOT
R={
 'COMA':('NCS ENLS version 6: approach to coma','https://www.neurocriticalcare.org/Portals/0/ENLS%205.0/ENLS%206.0/Protocol%20V6_0_Approach%20to%20the%20Patient%20With%20Coma.pdf'),
 'AHA':('AHA 2025 special circumstances of resuscitation','https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-and-pediatric-special-circumstances-of-resuscitation'),
 'BLS':('AHA 2025 adult basic life support','https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'),
}
def S(h,main,*children):return(h,[(main,list(children))])
rows=[]
def add(*a,**kw):rows.append(Q(*a,**kw))

add('Coma and acute consciousness assessment','Immediate Stabilization in Undifferentiated Coma',
 'An unresponsive adult arrives with shallow breathing and no reliable history. A pulse is present. Which initial approach is most appropriate?',
 'Support airway and ventilation, assess circulation and check bedside glucose while evaluating reversible causes',[
 ('Obtain emergency CT before intervening so the examination remains unaltered','CT is often urgent, but an unprotected airway, inadequate ventilation or hypoglycemia requires immediate treatment rather than waiting for imaging.'),
 ('Give a sedative reversal combination before evaluating breathing and glucose','Selected antidotes have specific indications, but an indiscriminate reversal strategy does not replace physiologic stabilization and can introduce harm.'),
 ('Complete a detailed neurologic localization before deciding on respiratory support','A focused examination is useful in parallel, but inadequate ventilation cannot wait for a complete localization or history.')],
 [S('Correct Physiologic Threats in Parallel','**Coma assessment begins with airway, breathing and circulation**, with cervical protection when trauma is possible. Check pulse, oxygenation and ventilation directly.',
    'Obtain bedside glucose promptly and correct hypoglycemia. Consider relevant toxidromes, temperature abnormalities and seizures while arranging the broader workup.',
    'A pulse does not establish adequate ventilation, and normal oxygen saturation on supplemental oxygen does not exclude hypercapnia.'),
  S('Investigate Without Delaying Stabilization','**Perform a focused neurologic assessment during resuscitation**, documenting pupils, motor responses, focal findings and evidence of trauma.',
    'Select urgent CT and vascular imaging when structural disease or basilar occlusion is plausible, and obtain targeted laboratory, toxicologic and infection studies according to context.',
    'Review medicines and prehospital interventions because sedation and paralysis can alter the examination. A diagnostic label should follow the integrated evidence rather than a single Glasgow Coma Scale total. Serial assessment is essential: successful correction of one reversible contributor does not exclude a concurrent structural lesion, and an initially nondiagnostic scan does not remove the need to reassess persistent impaired consciousness.')],['COMA','BLS'])

add('Coma and acute consciousness assessment','Ventilation During Suspected Opioid Toxicity',
 'A patient with suspected opioid exposure is unresponsive, breathing four times per minute and has a definite pulse. Which immediate strategy is most appropriate?',
 'Provide assisted ventilation and administer naloxone, then monitor for recurrent respiratory depression',[
 ('Give naloxone and wait for awakening before assisting breathing','Naloxone can reverse opioid effects, but its onset and response are not guaranteed; severe hypoventilation requires immediate ventilatory support.'),
 ('Give oxygen alone and use saturation as the endpoint of treatment','Oxygen can mask inadequate ventilation; the patient requires effective breaths and reassessment of carbon dioxide clearance and airway protection.'),
 ('Begin chest compressions solely because the patient is unconscious','Compressions are required for cardiac arrest, but this patient has a definite pulse and respiratory failure; ventilation and opioid reversal are the immediate priorities.')],
 [S('Treat Respiratory Failure Rather Than Chasing Wakefulness','**Opioid toxicity can progress from respiratory depression to hypoxic cardiac arrest.** AHA guidance prioritizes breaths or bag-mask ventilation when a pulse is present but breathing is inadequate.',
    'Administer an appropriate naloxone preparation by an available validated route and titrate or repeat according to the clinical response and product/local protocol.',
    'The immediate goal is adequate ventilation and airway safety, not necessarily complete abrupt awakening. Severe dependence can increase withdrawal-related complications after reversal.'),
  S('Reassess After the Initial Response','**Naloxone can wear off before the opioid effect resolves.** Monitor breathing, consciousness and hemodynamics and consider repeat dosing or an infusion through the appropriate toxicology pathway.',
    'Review long-acting agents, coingestants, aspiration, hypoglycemia and other causes when response is incomplete. Pinpoint pupils support but do not independently prove the mechanism.',
    'If cardiac arrest develops, provide standard high-quality CPR and indicated advanced care; naloxone must not delay proven resuscitation measures. After stabilization, arrange an observation and discharge plan that reflects the exposure and recurrence risk, with overdose prevention and treatment linkage where relevant. A transient response is not sufficient reason to leave a recently hypoventilating patient unmonitored.')],['AHA','BLS','COMA'])

R.update({
 'ASAM':('ASAM alcohol-withdrawal guideline: thiamine and glucose, 2020','https://doi.org/10.1097/ADM.0000000000000668'),
 'EEG':('ACNS continuous EEG consensus: indications, 2015','https://pmc.ncbi.nlm.nih.gov/articles/PMC4435533/'),
 'EEG21':('ACNS standardized critical-care EEG terminology, 2021','https://doi.org/10.1097/WNP.0000000000000806'),
})

add('Coma and acute consciousness assessment','Hypoglycemia and Thiamine Risk',
 'A malnourished patient is unconscious with bedside glucose 32 mg/dL. Parenteral glucose is immediately available, but thiamine is being obtained. Which action is most appropriate?',
 'Correct hypoglycemia immediately and administer parenteral thiamine promptly without delaying glucose',[
 ('Withhold glucose until thiamine has been administered','Thiamine should be provided promptly in at-risk patients, but treatment of severe symptomatic hypoglycemia should not be delayed while it is obtained.'),
 ('Give thiamine alone and reassess glucose after consciousness improves','Thiamine treats deficiency risk but does not immediately correct the severe glucose deficit threatening cerebral function.'),
 ('Obtain laboratory confirmation before treating the low bedside value','Laboratory testing can clarify uncertain readings, but a profoundly low bedside result with coma warrants immediate treatment and follow-up measurement.')],
 [S('Treat the Immediate Energy Failure','**Severe hypoglycemia can cause seizures, focal findings or coma.** Give an appropriate IV glucose preparation promptly and recheck the response.',
    'Use a locally standardized concentration and dose and monitor access safety, because concentrated solutions can injure tissue if extravasated.',
    'Assess the cause, including insulin or secretagogue exposure, poor intake, alcohol, organ failure or endocrine disease. Recurrent hypoglycemia may require continuing support rather than a single bolus.'),
  S('Replace Thiamine Without Creating a Treatment Delay','**Malnutrition and alcohol-related risk warrant prompt parenteral thiamine.** ASAM permits glucose and thiamine in either order or concurrently to avoid delaying necessary care.',
    'Prevention dosing is not the same as treatment of suspected Wernicke encephalopathy, which may require a higher parenteral regimen. Choose the regimen for the actual clinical indication.',
    'Review magnesium and other nutritional deficits and monitor for refeeding problems when feeding resumes. If consciousness does not recover as expected, continue investigation for seizures, structural disease or another contributor. Neither a low glucose nor nutritional risk proves that every finding has one mechanism, but both warrant timely correction while the differential remains open.')],['COMA','ASAM'])

add('Coma and acute consciousness assessment','New Anisocoria in Deteriorating Consciousness',
 'An acutely deteriorating patient develops a newly dilated poorly reactive pupil and asymmetric motor responses. Which response is most appropriate?',
 'Treat as a structural intracranial emergency while stabilizing physiology and obtaining urgent imaging and specialist assessment',[
 ('Assume a sedative effect and wait for drug clearance before imaging','Medicines can alter the examination, but new asymmetric pupillary and motor findings require urgent structural assessment rather than an observation-only drug explanation.'),
 ('Perform LP first to measure the intracranial pressure','A possible mass-related pressure gradient makes LP unsafe until appropriate structural assessment; manometry is not the immediate test for suspected herniation.'),
 ('Use the pupil finding alone to declare irreversible brainstem failure','An abnormal pupil can arise from reversible compression, ocular causes or drugs; it does not establish irreversible failure or meet death-determination criteria.')],
 [S('Recognize a Warning Pattern, Not a Final Diagnosis','**New anisocoria with declining consciousness and focal motor findings raises concern for mass effect or brainstem involvement.** The complete clinical pattern determines urgency.',
    'Review baseline pupils, ocular trauma, prior surgery and topical or systemic medicines, but do not let that review delay stabilization of a threatened patient.',
    'Pupil size alone is not a reliable single-lesion diagnosis. Serial examination and imaging are needed to identify hemorrhage, mass lesion, hydrocephalus or another mechanism.'),
  S('Stabilize and Identify the Treatable Cause','**Support oxygenation, ventilation and circulation and arrange emergency neuroimaging**, with immediate neurosurgical or neurovascular involvement as appropriate.',
    'When impending herniation is clinically suspected, initiate appropriate temporizing measures while arranging definitive treatment; do not wait passively for a report.',
    'Avoid unsafe LP and unnecessary delays for prolonged examination. Record the timing and progression of findings and relevant treatments. A transient response to a rescue measure does not remove the need for definitive evaluation, and a grave examination at one time point should not be substituted for a properly conducted prognostic or death-determination process.')],['COMA'])

add('Coma and acute consciousness assessment','Oculocephalic Testing and Cervical Safety',
 'A comatose patient is brought after an unwitnessed fall. Cervical injury has not been excluded. Which examination approach is most appropriate?',
 'Avoid head-turning oculocephalic testing until cervical safety is established and assess other safe brainstem components',[
 ('Perform rapid head rotation because coma makes the response more informative','The maneuver can assess selected brainstem pathways, but its diagnostic value does not override the risk of movement in a potentially injured cervical spine.'),
 ('Record all brainstem reflexes as absent because one maneuver cannot be performed','Untestable is not equivalent to absent; document the limitation and use appropriate safe assessments rather than inventing a complete examination.'),
 ('Infer a normal oculocephalic response from a preserved pupillary light reflex','These assess different pathways; one preserved reflex does not establish the result of another unperformed maneuver.')],
 [S('Assess Pathways Without Adding Injury','**Brainstem examination includes distinct pupillary, corneal, ocular-motor and bulbar components.** Each has limitations and contraindications that must be considered.',
    'Oculocephalic testing involves head movement and should not be used when cervical instability remains a concern.',
    'Ocular trauma, prior surgery and ear pathology can also limit selected reflex tests. Use appropriate technique and expert advice rather than force an unsafe maneuver.'),
  S('Document Confounding and Untestable Findings','**Record what was observed, what was not tested and why.** Sedatives, neuromuscular blockers and local injury can alter or obscure responses.',
    'Other safe clinical findings, imaging and selected investigations contribute to acute localization. A missing test should not be converted into an assumed negative result.',
    'Death-by-neurologic-criteria assessment has a formal prerequisite and completion framework separate from a routine coma examination. Do not use one untestable reflex as sufficient reason to declare death or bypass confounder evaluation. Repeat the examination when conditions change and communicate the limitations so that later clinicians do not mistake an incomplete entry for demonstrated brainstem areflexia.')],['COMA'])

add('Coma and acute consciousness assessment','Persistent Impairment After Convulsions Stop',
 'Visible convulsions have stopped after treatment, but the patient remains unexpectedly unresponsive with intermittent subtle facial movements. Which investigation has immediate value?',
 'Urgent EEG, with continuous monitoring when ongoing nonconvulsive seizures remain a concern',[
 ('Wait for all sedative effects to disappear before considering EEG','Sedation can contribute to nonawakening, but also conceals seizures; unexplained persistent impairment after convulsions warrants EEG assessment without an indefinite wait.'),
 ('Use absence of limb convulsions to exclude continuing seizure activity','Electrographic seizures can persist without major motor activity, particularly after treatment or neuromuscular blockade.'),
 ('Use serum lactate normalization as the principal test of seizure cessation','Lactate reflects several physiologic processes and can normalize despite nonconvulsive activity; it cannot replace EEG for this question.')],
 [S('Motor Cessation Does Not Guarantee Electrographic Control','**Nonconvulsive seizures or status can contribute to persistent impaired consciousness after a convulsive episode.** Postictal effects, drugs and structural or metabolic injury are competing explanations.',
    'EEG distinguishes some of these possibilities and helps characterize subtle events. Continuous monitoring can be needed because a short recording samples only part of the course.',
    'Clinical and EEG correlation matters; not every facial movement is a seizure and not every abnormal background pattern requires anesthetic suppression.'),
  S('Use Findings to Direct Treatment','**ACNS supports early continuous EEG in selected patients with persistent altered mental status after clinical seizures.** Duration depends on findings, risk and treatment response.',
    'Treat confirmed seizures and status under an appropriate protocol and investigate the precipitating cause. Interpret rhythmic or periodic patterns with standardized criteria and clinical context.',
    'Do not equate nonspecific slowing or isolated periodic activity automatically with definite status. Sedative treatment can itself reduce arousal and complicate assessment, so document dose changes and objective response. EEG monitoring is a diagnostic and treatment tool, not a standalone determination of prognosis or death.')],['EEG','EEG21','COMA'])

R.update({
 'DOC':('EAN guideline on coma and disorders of consciousness, 2020','https://doi.org/10.1111/ene.14151'),
 'ICP':('NCS ENLS version 6: intracranial hypertension and herniation','https://www.neurocriticalcare.org/Portals/0/ENLS%205.0/ENLS%206.0/Protocol%20V6_0_Intracranial%20Hypertension%20and%20Herniation.pdf'),
 'EDEMA':('NCS acute cerebral edema guideline, 2020','https://pmc.ncbi.nlm.nih.gov/articles/PMC7272487/'),
})

add('Coma and acute consciousness assessment','Locked-In Syndrome Can Mimic Unresponsiveness',
 'A patient is quadriplegic and unable to speak after an acute brainstem event. Repeated examination shows reliable upward gaze and blinking to verbal commands. Which interpretation is most appropriate?',
 'Preserved awareness with a locked-in motor-output syndrome',[
 ('Coma because no limb response or speech is present','Coma implies impaired wakefulness and awareness; reproducible command-following through eye responses demonstrates a channel of purposeful behavior despite severe motor impairment.'),
 ('Unresponsive wakefulness syndrome because the eyes can open','Eye opening alone can occur without demonstrated awareness, but reproducible responses to commands provide evidence beyond wakefulness.'),
 ('A reflex ocular response that cannot support any inference about awareness','Spontaneous or stimulus-driven movements can be reflexive, but consistent appropriately directed responses to commands require assessment as purposeful behavior rather than dismissal.')],
 [S('Look for a Preserved Communication Channel','**Classical locked-in syndrome combines quadriplegia and anarthria with preserved consciousness**, often with useful vertical eye movement or blinking.',
    'Ventral pontine injury is a classic mechanism, but the extent of injury and available responses vary. Incomplete and total forms can differ from the classical examination.',
    'Test repeated simple commands and establish reliable yes/no signals while accounting for hearing, vision, fatigue and sedation.'),
  S('Avoid Equating Motor Silence With Absent Awareness','**Assess comprehension through the available output channel.** A low motor or verbal score cannot independently establish unconsciousness in a patient unable to move or speak.',
    'Acute brainstem vascular disease requires urgent imaging and mechanism-specific treatment assessment. Support ventilation, swallowing and other affected functions.',
    'Provide communication aids and rehabilitation and address pain and distress even when bedside interaction is difficult. Do not infer an individual quality-of-life preference or prognosis from the motor deficit alone. Document reproducible responses so that other clinicians do not mistake the patient for persistently comatose and so that treatment discussions can involve the patient whenever possible.')],['DOC','COMA'])

add('Coma and acute consciousness assessment','A GCS Total Does Not Remove Sedation Confounding',
 'An intubated patient has received sedatives and a neuromuscular blocker. No limb movement is observed. Which documentation and interpretation is most appropriate?',
 'Record the examination components and drug confounders and reassess when clinically safe',[
 ('Use the absent movement as definitive evidence of severe motor-pathway injury','Neuromuscular blockade can abolish visible movement without proving central motor failure; the medication context prevents that inference.'),
 ('Assign a low total score and use it alone to determine prognosis','A total score obscures untestable and confounded components and cannot alone establish outcome or justify a death determination.'),
 ('Stop all sedation immediately regardless of intracranial or respiratory instability','A sedation interruption can help selected assessments, but must be safe; abrupt withdrawal can worsen physiology and should follow an individualized plan.')],
 [S('Describe What Was Actually Measured','**Standardized serial examinations are useful only when their limitations are explicit.** Record eye, verbal and motor components and explain intubation or other barriers.',
    'Document sedative dose and timing, renal/hepatic dysfunction and neuromuscular blockade. Drug accumulation can outlast a nominal dosing interval.',
    'A pharmacologically absent motor response is not equivalent to a demonstrated destructive lesion or a permanent prognosis.'),
  S('Reassess Alongside Objective Clinical Data','**Plan safe repeat assessment**, integrating brainstem findings, imaging, laboratory results and EEG where relevant.',
    'A wake-up examination is not automatically safe during uncontrolled ICP, severe hypoxemia or another unstable condition; weigh information value against risk.',
    'Check for reversible metabolic and temperature confounders and assess for seizures when nonawakening is unexplained. Separate immediate severity assessment, longer-term prognostication and formal death determination: each answers a different question and has different prerequisites. Clear documentation prevents a later clinician from treating a confounded one-time score as proof of irreversible neurologic failure.')],['COMA','DOC'])

add('Intracranial pressure and traumatic brain injury','Impending Herniation Requires Parallel Rescue and Definitive Planning',
 'A patient with a known intracranial mass abruptly loses consciousness and develops a dilating pupil. Which response is most appropriate?',
 'Begin immediate physiologic and ICP rescue measures while arranging urgent definitive neurosurgical evaluation',[
 ('Wait for a repeat scan before beginning any stabilization or ICP rescue','Imaging is important, but clinically suspected herniation is a time-critical emergency requiring treatment while the cause and intervention are assessed.'),
 ('Use repeated LP to lower pressure before calling neurosurgery','A mass-related pressure gradient can make lumbar drainage dangerous; this is not the appropriate decompression route for a suspected herniation syndrome.'),
 ('Treat the pupil change as proof of irreversible injury and limit further assessment','Acute compression can be treatable; one severe examination does not establish irreversibility or substitute for appropriate rescue and diagnostic evaluation.')],
 [S('Recognize a Time-Critical Brain Emergency','**Herniation syndromes require immediate recognition and treatment.** Acute deterioration with pupillary and motor changes can indicate a dangerous compartment pressure gradient.',
    'Support airway, oxygenation, ventilation and circulation and urgently involve neurosurgery or the relevant neurocritical team.',
    'Use emergency imaging as soon as feasible without allowing transport or test sequencing to delay essential stabilization.'),
  S('Temporize While Treating the Cause','**Position appropriately, relieve venous outflow obstruction and give indicated hyperosmolar rescue** under an emergency protocol.',
    'Brief controlled hyperventilation can be a bridge in a herniation emergency, but sustained indiscriminate hypocapnia can reduce cerebral blood flow and cause harm.',
    'Definitive treatment can include evacuation, resection, CSF diversion or decompression according to anatomy. An improved pupil after rescue is not proof that the underlying threat has resolved. Continue monitoring and reassessment and avoid unsafe LP. Rescue choices must account for blood pressure, sodium, kidney function and the actual lesion rather than using one fixed intervention for every deteriorating neurologic patient.')],['ICP','EDEMA'])

add('Intracranial pressure and traumatic brain injury','Optimize Venous Drainage Without Sacrificing Perfusion',
 'A patient with intracranial hypertension is lying flat with the neck rotated and a constrictive tube tie. Which bedside adjustment is appropriate while definitive treatment proceeds?',
 'Elevate the head around 30 degrees and maintain neutral neck alignment while ensuring safe perfusion and spinal precautions',[
 ('Raise the head to 90 degrees without reassessing blood pressure','Head elevation can reduce ICP, but excessive elevation or systemic hypotension can impair perfusion; position must be individualized and monitored.'),
 ('Remove all cervical protection immediately to maximize venous drainage','A poorly fitted device can obstruct outflow, but possible spinal instability still needs protection; adjust safely rather than abandoning precautions.'),
 ('Rotate the neck further to improve access and assess ICP later','Neck rotation or compression can impair jugular drainage; access arrangements should preserve neutral alignment where feasible.')],
 [S('Reduce Avoidable Venous Outflow Resistance','**Head elevation near 30 degrees and neutral alignment are useful adjuncts to ICP control.** Avoid unnecessary neck flexion, rotation and constrictive ties.',
    'Check the fit of collars and airway devices while maintaining required cervical protection. A simple device adjustment can reduce an avoidable contributor without changing the underlying lesion.',
    'Use appropriate analgesia and control coughing, agitation or ventilator dyssynchrony where these worsen pressure, while avoiding unmonitored oversedation.'),
  S('Keep the Whole Perfusion System in View','**A lower ICP is not beneficial if systemic pressure or oxygen delivery becomes inadequate.** Reassess hemodynamics and clinical status after position changes.',
    'When using an ICP monitor or arterial transducer, apply the relevant leveling/reference protocol so that a changed position does not create a misleading number.',
    'Correct hypoxemia, fever and other contributors alongside lesion-specific treatment. Positioning is supportive rather than definitive therapy for a compressive mass or obstructed CSF pathway. If deterioration continues, escalate promptly rather than repeating simple bedside measures indefinitely; treatment goals combine pressure control with adequate cerebral perfusion and safe management of associated injuries.')],['ICP','EDEMA'])

R['BTFTBI']=('Brain Trauma Foundation: severe TBI fourth-edition recommendations','https://braintrauma.org/coma/guidelines/severe-tbi-4th-edition')
R['ACSTBI']=('ACS best practices: traumatic brain injury, 2024','https://www.facs.org/media/vgfgjpfk/best-practices-guidelines-traumatic-brain-injury.pdf')
R['PHARM']=('ENLS pharmacotherapy protocol: hyperosmolar agents','https://www.neurocriticalcare.org/Portals/0/ENLS%205.0/ENLS%205.0%20Protocol%20-%20Pharm.pdf')

add('Intracranial pressure and traumatic brain injury','Hyperosmolar Rescue and Toxicity Monitoring',
 'A patient needs urgent hyperosmolar treatment for an ICP crisis. Which prescribing principle is most appropriate?',
 'Select hypertonic saline or mannitol using hemodynamics and renal/electrolyte status, with reassessment after the bolus',[
 ('Repeat mannitol on a fixed schedule without reviewing volume status','Mannitol can lower ICP but can also cause diuresis, hypovolemia and renal injury; repeat dosing needs response and safety reassessment.'),
 ('Use a high sodium target as proof that hypertonic treatment is effective','Serum sodium is a safety and physiologic measure, not proof of clinical efficacy; deliberately chasing severe hypernatremia can add renal and other risks.'),
 ('Treat the initial ICP response as a substitute for definitive lesion treatment','A bolus can buy time, but does not remove a compressive hematoma or other structural cause requiring intervention.')],
 [S('Use an Appropriate Emergency Regimen','**Hyperosmolar agents can reduce ICP but require patient-specific selection.** An example mannitol rescue dose is ==0.5–1 g/kg IV==, with monitoring for hypotension and diuresis.',
    'Hypertonic saline comes in markedly different concentrations. A commonly used concentrated rescue preparation is 23.4% saline, with an ENLS example of 0.5 mL/kg up to 30 mL; use the relevant access and administration protocol.',
    'Never interchange concentration and volume without checking the actual prescription. Hemodynamic instability, existing hypernatremia and renal impairment affect the choice.'),
  S('Monitor the Response and the Cost','**Follow clinical/ICP response, volume status, sodium, chloride and renal function.** Mannitol assessment also uses an appropriate measure of osmotic burden.',
    'NCS advises avoiding severe hypernatremia and hyperchloremia; its suggested upper safety ranges are not treatment targets and rest on low-certainty evidence.',
    'No universal bolus or serum target guarantees neurologic recovery. Reassess recurrent crises for a reversible structural cause and coordinate definitive neurosurgical care. Avoid an automatic cycle of repeat osmotic doses when the pressure remains high, kidney function worsens or perfusion falls; escalation requires a broader reassessment of physiology and anatomy.')],['EDEMA','ICP','PHARM'])

add('Intracranial pressure and traumatic brain injury','Hyperventilation as a Short Rescue Bridge',
 'A ventilated patient develops a clinical herniation syndrome while urgent definitive treatment is arranged. Which ventilation approach is most appropriate?',
 'Consider brief controlled hyperventilation, commonly toward PaCO2 30–35 mmHg, while treating the cause',[
 ('Maintain PaCO2 at 20–25 mmHg for the next several days to prevent recurrence','Prolonged prophylactic marked hypocapnia can reduce cerebral blood flow and cause ischemia; it is not the recommended preventive strategy.'),
 ('Avoid any transient ventilation change because hyperventilation can never lower ICP','CO2 reduction can rapidly reduce cerebral blood volume and pressure, so a brief rescue bridge has a role despite its perfusion risks.'),
 ('Use a fixed respiratory rate without confirming carbon dioxide response','The same rate does not produce the same PaCO2 in every patient; capnography and blood gases help avoid excessive or inadequate ventilation.')],
 [S('Recognize Both the Benefit and Hazard','**Hypocapnia causes cerebral vasoconstriction**, which can reduce ICP quickly but also reduce cerebral blood flow.',
    'A short rescue course toward ==PaCO2 30–35 mmHg== can be used during impending herniation while hyperosmolar and definitive treatment are organized.',
    'This differs from routine prolonged prophylactic hyperventilation. The Brain Trauma Foundation advises against prolonged prophylactic PaCO2 at or below 25 mmHg.'),
  S('Use Monitoring and a Clear Exit Plan','**Measure the physiologic response rather than prescribing a rate alone.** End-tidal CO2 can guide adjustments, but the arterial gradient varies and blood gases may be needed.',
    'Avoid hypotension and hypoxemia and reassess perfusion, especially early after TBI when ischemic vulnerability is important.',
    'Return to an appropriate ventilation strategy as rescue and definitive treatment take effect. Persistent need for hypocapnia signals unresolved intracranial danger rather than a successful long-term solution. Document the indication and duration, and do not treat a lower pressure number as adequate evidence of preserved tissue oxygen delivery.')],['ICP','BTFTBI','ACSTBI'])

add('Intracranial pressure and traumatic brain injury','ICP and CPP Targets in Severe TBI',
 'Which monitored-treatment framework best reflects Brain Trauma Foundation guidance for severe adult TBI?',
 'Treat ICP above 22 mmHg and generally target CPP 60–70 mmHg, integrating the clinical and imaging context',[
 ('Treat ICP above 10 mmHg and target CPP above 90 mmHg in every patient','These targets are not the recommended severe-TBI framework and can drive unnecessary therapy and excessive fluid or vasopressor exposure.'),
 ('Use normal systemic MAP as proof that CPP is adequate without considering ICP','CPP depends on the relationship between arterial pressure and ICP; a superficially acceptable MAP can coexist with inadequate perfusion when ICP is high.'),
 ('Use the same fixed target regardless of autoregulation, examination or CT findings','Thresholds guide care but do not eliminate the need to interpret pressure burden, autoregulation and the structural clinical picture.')],
 [S('Use the Recommended Ranges With Context','**BTF recommends treatment of ICP above ==22 mmHg==**, because higher values are associated with increased mortality. Interpret this with the examination and CT findings.',
    'The usual CPP target is ==60–70 mmHg==. Which part of that range is best may depend on autoregulation and patient-specific physiology.',
    'CPP is commonly approximated as MAP minus ICP, with correct transducer reference and measurement technique essential for interpretation.'),
  S('Avoid Creating Harm While Chasing a Number','**Correct systemic hypotension and treat intracranial causes together.** Raising MAP alone is not the entire strategy when a mass lesion or obstruction drives ICP.',
    'Excessive fluids or pressors to force high CPP can add pulmonary and systemic complications. Assess oxygenation, ventilation, temperature, sedation and surgical options.',
    'A single artifact or transient pressure spike should not be interpreted without waveform and clinical review. Conversely, sustained or recurrent elevation requires action even if one later measurement improves. These targets apply to the specified severe-TBI setting and should not be copied without qualification to every cause of cerebral edema or every age group.')],['BTFTBI','ACSTBI'],style='direct')

add('Intracranial pressure and traumatic brain injury','Deterioration With a Traumatic Extra-Axial Hematoma',
 'After head trauma, a patient develops worsening consciousness and a new focal deficit. CT shows a substantial extra-axial hematoma with mass effect. Which next action is most appropriate?',
 'Urgent neurosurgical evaluation for evacuation while stabilizing airway, perfusion and intracranial pressure',[
 ('Observe until a fixed pupil develops before seeking operative assessment','A fixed pupil is not a prerequisite for a dangerous hematoma; progressive neurologic decline and mass effect already require urgent surgical assessment.'),
 ('Use hyperosmolar boluses as the definitive treatment plan','Osmotic treatment can bridge an emergency, but does not remove the clot or replace evaluation for evacuation of a surgically actionable lesion.'),
 ('Perform LP to measure the pressure before deciding whether the hematoma matters','A mass-related pressure gradient can make LP unsafe; the clinical deterioration and CT already establish the need for urgent structural assessment.')],
 [S('Recognize Progression Rather Than Waiting for a Complete Syndrome','**Traumatic epidural or subdural hematoma can cause rapid secondary deterioration.** A lucid interval may occur in some epidural cases but is not required.',
    'Assess the neurologic trajectory, pupillary changes, hematoma burden, shift and associated injuries with urgent neurosurgical review.',
    'Specific operative thresholds depend on the hematoma type and clinical context; do not apply one universal thickness or volume rule to every extra-axial collection.'),
  S('Bridge to Definitive Structural Treatment','**Support airway, oxygenation and perfusion while arranging indicated evacuation.** Treat herniation physiology without delaying the operative pathway.',
    'Review anticoagulants, coagulopathy and other trauma-related bleeding and coordinate reversal or blood-product care as appropriate.',
    'Repeat imaging is useful when the examination worsens or another complication is suspected, but should not create avoidable delay when an actionable lesion is already demonstrated. Continue serial examination after treatment and assess recurrent deterioration for rebleeding, swelling, seizures or systemic injury. Early severe findings are an emergency-treatment signal, not a standalone permanent prognostic conclusion.')],['ACSTBI','ICP','COMA'])

R.update({
 'DC':('BTF decompressive craniectomy recommendations update, 2020','https://pmc.ncbi.nlm.nih.gov/articles/PMC7426189/'),
 'POSTAHA':('AHA post-cardiac-arrest care guideline, 2025','https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/post-cardiac-arrest-care'),
 'POSTERC':('ERC-ESICM post-resuscitation care guideline, 2025','https://www.resus.org.uk/professional-library/2025-resuscitation-guidelines/post-resuscitation-care-guidelines'),
})

add('Intracranial pressure and traumatic brain injury','CSF Diversion and Decompression Address Different Problems',
 'A severe-TBI patient has refractory intracranial hypertension despite first-tier care. Which principle best guides consideration of ventricular drainage or decompressive craniectomy?',
 'Select the intervention from anatomy, pressure mechanism, prior therapy and expected outcomes rather than treating all procedures as interchangeable',[
 ('Use ventricular drainage as definitive treatment for any large compressive hematoma','Drainage can reduce CSF-related pressure but does not evacuate a mass lesion; a compressive hematoma needs its own surgical assessment.'),
 ('Use decompressive craniectomy whenever one ICP reading exceeds the treatment threshold','Decompression decisions depend on sustained refractory burden, imaging and treatment context, not one isolated value or artifact.'),
 ('Interpret any post-procedure ICP reduction as proof of favorable functional recovery','Pressure control is important, but lower ICP does not by itself establish survival with a favorable outcome; trial and patient-level results need separate interpretation.')],
 [S('Match the Procedure to the Mechanism','**Ventricular CSF drainage can reduce ICP when an appropriate ventricular target and indication exist.** Evacuation treats a mass lesion; decompression increases available intracranial space.',
    'These interventions can coexist in a plan but do not answer identical anatomic questions. Review imaging, clinical trajectory and response to earlier treatments.',
    'Catheter placement and drainage require infection, hemorrhage and overdrainage precautions and specialist monitoring.'),
  S('Discuss Outcomes Beyond the Pressure Trace','**BTF updated secondary decompression recommendations distinguish early and late refractory ICP trial settings.** Late refractory decompression has stronger support for improving mortality and favorable outcomes than the early DECRA-type setting.',
    'Either setting can show reduced ICP and ICU duration without that effect translating automatically into the same functional benefit.',
    'Counsel about the distribution of possible disability and recovery, not merely whether the operation lowers pressure. Primary decompression during mass-lesion evacuation is a different question from secondary decompression for refractory diffuse swelling. Decisions need expert review and patient-centered goals rather than a universal procedural sequence copied from one trial population.')],['DC','ACSTBI','ICP'])

add('Intracranial pressure and traumatic brain injury','Corticosteroids Are Not TBI Edema Treatment',
 'A patient has severe TBI with diffuse swelling. Which corticosteroid strategy is appropriate for treatment of the brain injury itself?',
 'Do not use high-dose corticosteroids to treat the TBI or improve its outcome',[
 ('Use high-dose methylprednisolone because all cerebral edema is steroid-responsive','Steroids help selected tumor-associated edema and inflammatory disorders, but severe TBI evidence shows harm rather than a general edema benefit.'),
 ('Use dexamethasone routinely whenever traumatic ICP rises','Dexamethasone is appropriate for selected vasogenic tumor edema, but routine treatment of traumatic intracranial hypertension is not supported.'),
 ('Use an empirical steroid response to decide whether decompression is needed','A response trial is not a safe substitute for treating traumatic pressure and structural causes; steroids do not define the need for indicated neurosurgical intervention.')],
 [S('Mechanism Determines Whether Steroids Help','**BTF advises against corticosteroids for improving severe-TBI outcome or reducing ICP.** High-dose methylprednisolone was associated with increased mortality.',
    'Do not transfer tumor-edema or immune-disease treatment to trauma merely because the CT report describes swelling.',
    'This recommendation concerns treatment of TBI itself; a separate valid indication, such as adrenal replacement, must be assessed on its own merits.'),
  S('Use Supported Pressure and Supportive Strategies','**Prevent hypoxemia and hypotension and treat the actual intracranial problem.** Positioning, appropriate sedation, hyperosmolar rescue and selected drainage or surgery have defined roles.',
    'Monitor ICP and perfusion in the appropriate patient and reassess an unexpectedly worsening course for hematoma expansion, seizures or systemic complications.',
    'Steroid risks include hyperglycemia, infection, myopathy and other complications, but the reason to avoid routine TBI use is not theoretical toxicity alone: outcome evidence demonstrated harm. Document the indication if a steroid is nevertheless prescribed for another condition so that later clinicians do not mistake it for recommended traumatic-edema therapy.')],['BTFTBI','ACSTBI'],style='direct')

add('Post-cardiac-arrest neurologic care','Deliberate Temperature Control After ROSC',
 'An adult remains unable to follow commands after ROSC. Which temperature strategy best reflects the 2025 AHA guidance?',
 'Use a deliberate temperature-control strategy within 32–37.5°C rather than permitting uncontrolled fever',[
 ('Cool every patient to 32°C because deeper cooling is universally superior','Guidance supports a selected controlled range; trials do not establish that the lowest target is superior for every patient or rhythm.'),
 ('Allow fever unless convulsive seizures develop','Fever prevention is part of care for the unresponsive post-arrest patient and should not depend on the appearance of a convulsion.'),
 ('Use rapid large-volume ice-cold IV fluid infusion as the routine cooling method','Rapid cold-fluid loading is not the preferred routine strategy and can create hemodynamic or pulmonary complications; method and target require a controlled protocol.')],
 [S('Choose a Controlled Strategy and Prevent Fever','**AHA 2025 recommends a deliberate target between ==32°C and 37.5°C==** for adults unresponsive to verbal commands after ROSC.',
    'The guideline supports maintaining temperature control for at least 36 hours. ERC-ESICM emphasizes active fever prevention at or below 37.5°C; recommendations should be attributed rather than merged into a single rigid protocol.',
    'The optimal temperature for every subgroup and the ideal overall duration remain uncertain. Do not portray routine deep cooling as a proven universal requirement.'),
  S('Account for Treatment Effects on Assessment','**Monitor temperature with a reliable core measurement**, manage shivering and coordinate sedation, circulation and electrolyte care.',
    'Rewarming and sedative clearance affect the timing of a reliable neurologic assessment. Persistent coma during treatment does not independently establish a poor prognosis.',
    'Avoid uncontrolled fever during and after the initial intervention and reassess systemic complications. A chosen target is part of a broader post-arrest plan that includes cause identification, oxygenation, perfusion and seizure assessment. Temperature control does not replace delayed multimodal prognostication or justify an early irreversible conclusion from a drug-confounded examination.')],['POSTAHA','POSTERC'])

add('Post-cardiac-arrest neurologic care','Oxygen, Carbon Dioxide and Perfusion After ROSC',
 'A ventilated adult has ROSC and reliable arterial blood gases. Which physiologic approach best reflects the 2025 AHA post-arrest framework?',
 'Titrate oxygen to avoid hypoxemia and hyperoxemia, aim for normocapnia and maintain at least MAP 65 mmHg',[
 ('Maintain maximal FiO2 indefinitely because hyperoxemia cannot be harmful','High oxygen may be needed until reliable measurements are available, but thereafter titration avoids unnecessary hyperoxemia while preventing hypoxemia.'),
 ('Use routine marked hypocapnia to prevent cerebral edema in all survivors','Excessive CO2 reduction can impair cerebral blood flow; routine prophylactic hyperventilation is not the post-arrest normocapnic strategy.'),
 ('Accept MAP below 60 mmHg if the pulse and urine output are initially present','A pulse does not establish adequate perfusion, and hypotension should be avoided; the AHA framework uses at least 65 mmHg with individualized assessment.')],
 [S('Use Measured Physiologic Targets','**AHA 2025 suggests SpO2 ==90–98%== or PaO2 ==60–105 mmHg== after reliable measurement is available**, avoiding both hypoxemia and unnecessary hyperoxemia.',
    'The usual PaCO2 target is ==35–45 mmHg==, with individualization for relevant acid-base or pulmonary conditions. End-tidal values may not equal arterial CO2 after arrest.',
    'Maintain ==MAP at least 65 mmHg== and evaluate cardiac function, vasodilation and the arrest cause. Selected patients need a different individualized perfusion plan.'),
  S('Interpret Ranges Within the Guideline Used','**ERC-ESICM uses a narrower oxygenation target, commonly SpO2 94–98%.** This illustrates why a question should identify its guideline rather than imply that every published range is identical.',
    'Review blood gases, perfusion markers and the clinical response rather than treating an isolated monitor value as the entire resuscitation endpoint.',
    'Avoid overventilation, fluid overload and excessive vasopressor exposure while correcting threats. Normocapnia and stable pressure support cerebral recovery, but none of these values independently predicts outcome. Continue appropriate coronary, structural and toxicologic evaluation and reassess organ dysfunction as the post-arrest syndrome evolves.')],['POSTAHA','POSTERC'],style='direct')

R['PROG']=('NCS neuroprognostication in comatose cardiac-arrest survivors, 2023','https://pmc.ncbi.nlm.nih.gov/articles/PMC10241762/')

add('Post-cardiac-arrest neurologic care','Post-Arrest Myoclonus Needs EEG Context',
 'A patient develops generalized jerks after ROSC while remaining unresponsive. Which next approach is most appropriate?',
 'Obtain EEG to characterize the movements and background and treat confirmed seizures rather than infer outcome from jerks alone',[
 ('Declare a uniformly poor prognosis from early myoclonus without EEG','Early jerks have heterogeneous mechanisms and outcomes; the clinical sign alone does not supply a reliable individualized prognosis.'),
 ('Suppress every jerk with deep anesthesia irrespective of EEG findings','Treatment of electroclinical seizures differs from suppressing nonepileptic myoclonus; unnecessary deep sedation can add harm and confound examination.'),
 ('Exclude seizures because some jerks occur without a visible EEG correlate','Some myoclonus lacks a correlate, but other events can be epileptic; appropriate recording and expert interpretation are required rather than a general exclusion.')],
 [S('Classify the Electroclinical Pattern','**Post-arrest myoclonus can accompany seizures, abnormal backgrounds or no time-locked EEG correlate.** EEG helps distinguish these situations and assess continuing seizure activity.',
    'Treat diagnosed seizures or status under an appropriate protocol. Do not equate every rhythmic or periodic EEG abnormality with definite status without standardized interpretation.',
    'AHA 2025 does not recommend treatment simply to suppress myoclonus without an EEG correlate. Separate symptom-specific exceptional concerns from an assumed neuroprotective benefit.'),
  S('Keep Treatment and Prognosis Distinct','**The background, timing and confounders matter to prognostic interpretation.** A motor sign without EEG is not an adequate basis for irreversible decisions.',
    'Sedatives and neuromuscular blockade can obscure clinical activity and alter the recording. Document exposures and use continued monitoring when appropriate.',
    'Assess hypoxic injury and other causes alongside the seizure question. A patient with jerks can have uncertain recovery potential, and controlling movements does not establish either favorable or unfavorable outcome. Integrate the later examination, electrophysiology and imaging within the appropriate delayed multimodal framework rather than allowing an early bedside label to determine subsequent care.')],['POSTAHA','EEG21','PROG'])

add('Post-cardiac-arrest neurologic care','Timing of Prognostic Synthesis After Rewarming',
 'A comatose cardiac-arrest survivor has completed hypothermic temperature control and has just been rewarmed. Sedatives may still be active. Which approach best reflects NCS 2023 guidance?',
 'Defer prognostic synthesis for at least 72 hours after rewarming and ensure relevant confounders are excluded',[
 ('Use 72 hours from the original arrest as sufficient regardless of rewarming or drug clearance','The timing anchor differs when hypothermia was used, and sedative or metabolic confounding can require additional delay before a reliable assessment.'),
 ('Infer poor outcome because commands are not followed immediately after rewarming','Delayed awakening can occur and ongoing drug effects complicate examination; immediate nonawakening does not independently establish poor recovery potential.'),
 ('Wait 72 hours and then use the motor score alone as the definitive predictor','Timing is necessary but not sufficient; the motor response alone is not a reliable basis for the required multimodal prognostic conclusion.')],
 [S('Use the Correct Time Anchor','**NCS recommends waiting at least 72 hours after ROSC when hypothermia was not used**, and at least ==72 hours after rewarming== when it was used.',
    'Some tests can be acquired earlier at their validated times, but the overall prognostic synthesis must account for examination readiness and the full evidence.',
    'Persistence of coma beyond that interval does not by itself establish a poor long-term outcome.'),
  S('Clear Confounders Rather Than Following the Clock Alone','**Review sedation, paralysis, temperature, seizures and metabolic or organ dysfunction.** Drug clearance varies with dose, infusion duration and renal or hepatic function.',
    'Use multiple modalities and the broader clinical context. Distinguish prognosis from preexisting illness and nonneurologic treatment limitations.',
    'If predictors are absent, conflicting or confounded, communicate uncertainty and consider longer observation consistent with the patient’s goals. A scheduled time point should not become an automatic withdrawal deadline. Document which findings are usable and which remain uninterpretable so that an early confounded examination is not carried forward as proof of permanent injury.')],['PROG','POSTAHA'])

add('Post-cardiac-arrest neurologic care','Use Validated Predictors in a Multimodal Assessment',
 'A cardiac-arrest survivor remains comatose at an appropriate unconfounded assessment time. Which test finding has strong prognostic value under NCS 2023 when technically valid and integrated with the overall assessment?',
 'Bilateral absence of cortical N20 responses on appropriately performed SSEP at least 48 hours after ROSC',[
 ('An absent or extensor motor response alone at 72 hours','Motor findings help characterize severity but are not sufficiently reliable alone to establish poor functional outcome in the NCS framework.'),
 ('Early myoclonus within 48 hours without EEG assessment','The sign has heterogeneous mechanisms and is not a reliable stand-alone poor-outcome predictor without appropriate electrophysiologic context.'),
 ('A single NSE value interpreted using one universal cutoff','NSE thresholds vary with assay and confounding such as hemolysis; a single universal value is not a reliable stand-alone predictor in this framework.')],
 [S('Check Timing, Technique and Biological Plausibility','**Bilaterally absent N20 responses at 48 hours or later can be a reliable poor-outcome predictor**, provided peripheral and cervical responses and recording quality support interpretation.',
    'Severe hypothermia, artifact and technical failure can invalidate an apparent absence. Obtain expert interpretation rather than accepting an uninterpretable trace as a positive predictor.',
    'Bilateral absent pupillary light responses at 72 hours or later can also be reliable when confounders and measurement limitations are excluded.'),
  S('Combine Independent Modalities','**Diffuse CT injury, appropriate MRI diffusion patterns and late suppressed or burst-suppressed EEG can contribute**, with their own timing and confounder requirements.',
    'MRI diffusion assessment is generally considered over days two to seven; seizures and other causes of restriction can alter interpretation. EEG requires exclusion of sedation and temperature effects.',
    'No test should be stripped from its clinical and technical conditions. Seek concordance and explain the uncertainty of indeterminate or conflicting results. Reliable predictors estimate functional outcome in a defined population; they are not equivalent to a diagnosis of death by neurologic criteria or proof that a particular intervention is ethically required.')],['PROG','POSTERC'],style='direct')

add('Post-cardiac-arrest neurologic care','An Indeterminate Prognosis Requires Honest Follow-Up',
 'At a properly timed review, a comatose arrest survivor has no reliable poor-outcome predictor and several equivocal studies. The family asks whether nonawakening proves permanent unconsciousness. Which response is most appropriate?',
 'Explain that recovery likelihood and timing remain uncertain and discuss continued observation and reassessment in the context of the patient’s goals',[
 ('State that coma beyond 72 hours establishes permanent unconsciousness','The recommended assessment interval is not a universal awakening deadline; persistent coma alone does not establish permanent loss of consciousness.'),
 ('Promise meaningful recovery because poor-outcome predictors are absent','Absence of a reliable poor-outcome predictor leaves uncertainty; it does not guarantee a favorable outcome or a particular recovery timetable.'),
 ('Repeat one biomarker until a threshold supplies an unequivocal decision','Repeated measurements can help selected questions, but a threshold cannot replace multimodal interpretation or remove assay and biologic uncertainty.')],
 [S('Describe What the Evidence Can and Cannot Say','**An indeterminate assessment is a legitimate conclusion.** Explain the findings, confounders, possible recovery trajectories and remaining questions in understandable language.',
    'Distinguish survival, awakening, functional independence and acceptable quality of life rather than treating them as one endpoint.',
    'Discuss preexisting function and systemic illness separately from the neurologic prognosis. The patient’s values guide decisions but do not change the measured certainty of a test.'),
  S('Plan Reassessment and Support','**NCS supports extended observation for recovery when prognosis remains indeterminate and this is consistent with goals of care.** Define a review plan rather than making a vague promise.',
    'Continue appropriate organ support, complication prevention and assessment for reversible barriers to awakening. Seek expert review when results conflict.',
    'Avoid self-fulfilling interpretation in which early withdrawal determines the apparent accuracy of an early pessimistic prediction. Neither automatic indefinite treatment nor automatic withdrawal follows from uncertainty alone. Shared decisions require clear communication, time for questions and documentation of the patient’s priorities and the limits of current evidence.')],['PROG','POSTAHA'])

R['BD']=('AAN/AAP/CNS/SCCM BD/DNC consensus guideline, 2023','https://pmc.ncbi.nlm.nih.gov/articles/PMC10791061/')

add('Brain death clinical prerequisites and examination','Death Determination Is Not a Disability Prognosis',
 'A patient has devastating brain injury and a very poor expected functional outcome. Some brainstem reflexes remain present. Which interpretation is correct?',
 'Poor prognosis does not establish death by neurologic criteria; preserved brainstem function is incompatible with that determination',[
 ('A sufficiently poor prognosis permits death certification without completing the clinical prerequisites','Prognostic counseling and death determination answer different questions; expected disability cannot replace the required demonstration of permanent loss of relevant brain function.'),
 ('Dependence on mechanical ventilation is sufficient evidence of neurologic death','Ventilator dependence can occur with many reversible or nonfatal neurologic conditions and does not establish the necessary clinical findings.'),
 ('An unfavorable imaging appearance overrides the preserved brainstem reflex','Imaging helps identify the mechanism and extent, but cannot negate observed brain-mediated function or justify certification contrary to the clinical framework.')],
 [S('Keep the Concepts Separate','**Coma, severe disability and death by neurologic criteria are distinct states.** A patient can have a devastating prognosis while retaining functions incompatible with death determination.',
    'The 2023 US consensus framework requires a known permanent catastrophic injury, exclusion of confounders and the specified clinical findings, including apnea assessment when appropriate.',
    'A preserved brainstem reflex or other brain-mediated activity is not an inconvenience to be bypassed with another test.'),
  S('Use the Applicable Clinical and Legal Framework','**Certification must follow the governing jurisdiction and authorized protocol.** US BD/DNC guidance informs these questions where stated but does not replace Indian legal requirements.',
    'Goals-of-care discussions may be appropriate for a living patient with severe injury, but they should not be framed as an already completed death determination.',
    'Explain the distinction clearly to family and staff. Do not equate the absence of a meaningful recovery prospect, a low GCS or a decision not to escalate treatment with neurologic death. A formal process requires documented prerequisites and examination rather than a global impression of futility or an anticipated donation pathway.')],['BD','PROG'])

add('Brain death clinical prerequisites and examination','A Known Catastrophic Mechanism Is Required',
 'An unresponsive apneic patient has no elicitable brainstem responses, but the cause is unknown and intoxication remains possible. Which next step is appropriate under the 2023 US BD/DNC guideline?',
 'Continue diagnostic evaluation and exclude mimics before undertaking a death-determination examination',[
 ('Proceed because the bedside appearance supplies the missing injury mechanism','A reversible mimic can produce profound areflexic coma; the examination appearance does not independently establish a permanent catastrophic brain injury.'),
 ('Use an ancillary test immediately to bypass the unknown cause','Ancillary tests do not replace the prerequisite of an identified qualifying mechanism or remove unresolved drug confounding.'),
 ('Use apnea alone as proof that the loss of function is permanent','Apnea can occur with intoxication or other reversible disease and cannot establish permanence without the required etiologic and confounder assessment.')],
 [S('Establish Etiology and Permanence','**The 2023 guideline requires a catastrophic permanent brain injury caused by an identified mechanism known to lead to BD/DNC.** The history, examination, imaging and laboratory data must be coherent.',
    'An unexplained combination of coma, apnea and absent reflexes requires further investigation, including toxicologic or metabolic causes when plausible.',
    'Observation and timing depend on the mechanism, interventions and relevant guideline requirements; a severe appearance alone does not create an adequate waiting period or diagnosis.'),
  S('Do Not Use Tests to Circumvent Prerequisites','**Ancillary studies have defined indications after appropriate clinical preparation.** They are not a shortcut for unexplained coma or an unexcluded intoxication.',
    'Review structural imaging for compatibility with the mechanism and assess for potentially reversible contributors. A mismatch should prompt expert review rather than forced certification.',
    'Document the causal assessment and reasons the injury is considered permanent. Local legal and institutional requirements also govern who can determine death and how findings are recorded. Preserve this distinction from prognostication: uncertainty about the cause must be resolved sufficiently for the death framework even when the patient is critically ill and the family needs timely communication.')],['BD','COMA'])

add('Brain death clinical prerequisites and examination','Rewarming Before the US BD/DNC Examination',
 'A patient being considered for BD/DNC evaluation under the 2023 US guideline previously had a core temperature of 34°C and has just reached 36°C after rewarming. Which timing requirement applies?',
 'Wait at least 24 hours after rewarming to at least 36°C before evaluation, while meeting all other prerequisites',[
 ('Begin immediately because the temperature has crossed 36°C','The guideline adds a waiting period after rewarming when the core temperature was at or below 35.5°C; reaching the minimum temperature alone is insufficient.'),
 ('Wait six hours because that is the universal adult interval for every neurologic-death protocol','The Indian adult repeat-testing interval concerns a different jurisdiction and stage; it does not replace the specified US post-hypothermia prerequisite.'),
 ('Use an ancillary study immediately instead of the rewarming waiting period','An ancillary study should not be used to bypass hypothermia-related prerequisites or uncertainty about its effects on examination and drug clearance.')],
 [S('Apply the Stated Temperature Rule','**The 2023 US guideline requires core temperature at least 36°C.** If the patient’s temperature has been ==35.5°C or lower==, wait at least ==24 hours after rewarming to 36°C or higher== before evaluation.',
    'Hypothermia can suppress neurologic responses and delay elimination of sedatives. Both direct and indirect effects can remain relevant after a thermometer first shows normothermia.',
    'This is a guideline-specific safety requirement, not a statement that every confounder resolves exactly after 24 hours.'),
  S('Reassess the Remaining Prerequisites','**Review drugs, hemodynamics, metabolic state and the permanent injury mechanism** before proceeding after the waiting interval.',
    'A longer delay may be needed when clearance is impaired or other confounders remain. Do not equate completed rewarming with a completed death determination.',
    'Record the lowest relevant core temperature, time of rewarming and subsequent stability. Distinguish this interval from the separate testing schedule required under Indian certification law or from the timing of post-arrest prognostication. Each framework answers a different procedural question, and combining their numbers without attribution can produce an unsafe answer key.')],['BD'],style='direct')

add('Brain death clinical prerequisites and examination','Drug Clearance Is Not a Fixed Clock in Overdose',
 'A deeply comatose patient has possible sedative overdose, renal dysfunction and recent hypothermia. Five usual therapeutic half-lives have elapsed. Which conclusion is most appropriate before BD/DNC evaluation?',
 'Drug effect may still be unresolved; assess exposure, levels and prolonged clearance with toxicology expertise as needed',[
 ('Five published half-lives guarantee absence of confounding even after overdose','Therapeutic pharmacokinetics may not apply to overdose, prolonged infusions, hypothermia or organ dysfunction; a nominal interval is not a guarantee.'),
 ('A negative routine urine screen excludes all clinically important sedatives','Screening panels have limited drug coverage and detection characteristics and cannot exclude every CNS-depressant exposure.'),
 ('An absent motor response confirms drug clearance despite the risk factors','The motor examination is itself affected by drugs and blockade; it cannot independently establish that their confounding action has ended.')],
 [S('Interpret Pharmacokinetics in the Actual Patient','**Exclude CNS-depressant effects before a reliable neurologic-death examination.** Review dose, last exposure, infusion duration, metabolites and available quantitative levels.',
    'The guideline’s use of at least five half-lives when levels are unavailable requires appropriate assumptions and longer consideration with organ dysfunction, obesity, hypothermia or other clearance concerns.',
    'Overdose can create prolonged absorption or nonlinear elimination, so a standard reference half-life may underestimate the required time.'),
  S('Use Expert Assessment Rather Than a Screening Shortcut','**Seek toxicology or pharmacology input when intoxication is plausible.** A routine negative screen is not a comprehensive clearance certificate.',
    'Assess neuromuscular blockade separately because loss of visible movement can occur without the same CNS mechanism. Treat reversible toxic and metabolic disease while monitoring the trajectory.',
    'Do not use an ancillary study simply to bypass high sedative levels or unresolved intoxication. Document why the medication effect is considered excluded and which uncertainties remain. The absence of clinical improvement at one expected time point does not establish permanence, particularly when the measured examination could still be drug-confounded.')],['BD','COMA'])

add('Brain death clinical prerequisites and examination','Paralysis and Metabolic Confounding',
 'A patient being considered for BD/DNC evaluation has recently received rocuronium and has severe metabolic derangements. Which next step is appropriate?',
 'Exclude residual pharmacologic paralysis and correct relevant metabolic abnormalities before interpreting the examination',[
 ('Interpret absent movement as central failure because rocuronium is not a sedative','Rocuronium does not establish unconsciousness, but blocks motor output; its peripheral mechanism still invalidates an unqualified interpretation of absent movement.'),
 ('Use a normal pupillary response to confirm the motor examination is unconfounded','Pupil and skeletal muscle responses involve different mechanisms; a pupil finding does not exclude residual neuromuscular blockade.'),
 ('Perform apnea testing immediately because laboratory abnormalities do not affect breathing drive','Severe metabolic disturbances can cause reversible dysfunction and alter respiratory physiology; prerequisites must be addressed before a valid test.')],
 [S('Exclude More Than CNS Sedation','**Residual neuromuscular blockade can mimic absent motor and respiratory output.** Review administration, clearance and an appropriate peripheral neuromuscular assessment.',
    'The 2023 guideline permits train-of-four assessment or demonstration of deep tendon reflexes to help exclude pharmacologic paralysis. An absent reflex is not, by itself, proof that blockade has cleared.',
    'Do not infer preserved awareness or absent awareness from paralysis alone. This is a separate confounder from sedative intoxication.'),
  S('Correct Reversible Physiologic Abnormalities','**Assess severe electrolyte, glucose, acid-base and endocrine disturbances**, as well as organ dysfunction relevant to the overall interpretation.',
    'The guideline does not provide a universally validated laboratory boundary for every possible disorder. Clinical severity and the potential to explain the examination require expert assessment.',
    'If a relevant metabolic abnormality cannot be adequately corrected, a defined ancillary pathway may be required after the clinical examination is completed as far as possible and remains consistent. This does not permit bypassing hypothermia or high sedative levels. Document the unresolved issue and applicable protocol rather than treating any abnormal laboratory value as either harmless or an automatic substitute for clinical testing.')],['BD','COMA'])

add('Brain death clinical prerequisites and examination','Adult Blood Pressure Prerequisites in the 2023 US Guideline',
 'Which minimum blood-pressure framework applies to a usual adult BD/DNC evaluation under the 2023 US consensus guideline?',
 'Maintain systolic BP at least 100 mmHg and MAP at least 75 mmHg',[
 ('Maintain systolic BP at least 90 mmHg and MAP at least 65 mmHg','These values appear in other resuscitation contexts or older frameworks, but do not meet the stated 2023 adult BD/DNC thresholds.'),
 ('Maintain MAP at least 65 mmHg without a systolic threshold','A post-arrest perfusion target is not interchangeable with the adult BD/DNC prerequisite requiring both specified pressures in the usual setting.'),
 ('Maintain systolic BP at least 100 mmHg without considering MAP','Meeting one component does not replace the other requirement; both systolic and mean pressure matter under the stated adult guideline.')],
 [S('Prevent Hypotension From Confounding the Examination','**The 2023 US guideline requires adult SBP at least ==100 mmHg== and MAP at least ==75 mmHg==.** Use appropriate fluids and vasoactive support to achieve stable physiology.',
    'Consider the patient’s known chronic baseline when relevant. Special circulatory support settings require their own technical application rather than copying a cuff-pressure rule.',
    'Children use age-dependent thresholds; the adult numbers are not a pediatric default.'),
  S('Distinguish Prerequisites From Other ICU Targets','**A target used after ROSC or during another shock state does not automatically satisfy death-determination requirements.** The question specifies the guideline and procedural context.',
    'Confirm temperature, drug clearance, metabolic readiness and a qualifying injury mechanism as well; a satisfactory BP alone does not make the examination valid.',
    'Monitor hemodynamics during testing and respond to instability rather than accepting an inadequately perfused examination. Indian certification follows its own applicable requirements and authorized documentation. Clearly attribute numeric thresholds in teaching material so that a learner does not combine one jurisdiction’s blood-pressure rule with another framework’s testing interval and assume the result is a complete legal protocol.')],['BD'],style='direct')

add('Brain death clinical prerequisites and examination','An Untestable Reflex Requires a Defined Pathway',
 'During a 2023 US BD/DNC evaluation, cervical injury makes oculocephalic testing unsafe. Oculovestibular responses can be assessed safely and are absent bilaterally. All other criteria are satisfied. Which interpretation is appropriate?',
 'The guideline permits determination without ancillary testing solely for the untestable oculocephalic component in this specific situation',[
 ('The neck must be rotated despite injury to complete the examination','An unsafe maneuver should not be forced; the guideline provides a specific pathway using safely assessed bilateral oculovestibular responses.'),
 ('Every untestable component can be assumed absent if the remaining reflexes are absent','Untestable is not generally equivalent to absent; the stated oculocephalic exception should not be generalized to other incomplete components.'),
 ('A preserved corneal reflex can be ignored because the oculovestibular responses are absent','Any preserved brainstem reflex is incompatible with the determination; one absent reflex does not override a preserved response elsewhere.')],
 [S('Assess Each Required Component Safely','**The clinical examination evaluates unresponsiveness and the required brainstem responses.** Pupillary, corneal, ocular-motor, facial, gag and cough findings answer different pathway questions.',
    'Facial, orbital, ear or cervical injuries can prevent reliable assessment. Document the specific limitation rather than charting a complete set of absent reflexes.',
    'If oculocephalic testing is unsafe because of cervical or skull-base concerns, the 2023 guideline allows the stated exception when bilateral oculovestibular responses are assessable and absent and all other requirements are met.'),
  S('Do Not Generalize an Exception','**Other untestable or uninterpretable components may require ancillary assessment through the defined protocol.** The clinical examination should still be completed as far as safely possible.',
    'A preserved brain-mediated response prevents determination and cannot be bypassed by an ancillary result.',
    'Ensure adequate technique and relevant local-injury review before calling a reflex absent. This question concerns a specifically attributed US guideline exception; it should not be copied automatically into Indian statutory certification without checking the applicable requirements and institutional authorized procedure.')],['BD'])

add('Brain death clinical prerequisites and examination','Spinal Reflexes Can Persist',
 'During an otherwise consistent BD/DNC evaluation, a limb shows a stereotyped withdrawal-like movement after peripheral stimulation. Which next approach is most appropriate?',
 'Determine whether the movement is spinally or brain-mediated and seek ancillary assessment if the distinction remains uncertain',[
 ('Any limb movement establishes preserved cerebral consciousness','Spinally mediated reflexes can persist without cerebral function; movement must be characterized rather than automatically equated with awareness.'),
 ('Ignore every movement once the initial brainstem examination is absent','Some movements can be brain-mediated and incompatible with determination; uncertainty must be resolved rather than dismissed.'),
 ('Use neuromuscular blockade to remove the movement and complete certification','Paralyzing the patient conceals motor output and introduces a confounder; it does not establish the movement’s origin or make the examination valid.')],
 [S('Separate Spinal Activity From Brain Function','**Spinal reflex motor responses can occur despite findings consistent with BD/DNC.** Their presence does not automatically invalidate the process.',
    'Assess stimulus relationship, pattern and reproducibility with appropriate expertise. Purposeful or brain-mediated activity has a different implication and prevents the determination.',
    'Complex appearance alone is not a reliable shortcut; some spinally generated patterns can be striking.'),
  S('Resolve Uncertainty Transparently','**The 2023 guideline calls for ancillary testing when the origin of observed limb movement remains unclear.** Continue the clinical assessment as far as possible and meet the other prerequisites.',
    'Do not suppress the movement pharmacologically to make the examination easier. Record what was seen and why it is interpreted as spinal or uncertain.',
    'Explain anticipated reflex phenomena to family and staff without implying that all future movements are harmless. A new or poorly characterized finding deserves reassessment. The goal is a valid determination based on demonstrated loss of relevant brain function, not simply an appearance of complete stillness or a test chosen to support a predetermined conclusion.')],['BD'])

add('Apnea testing, ancillary studies and Indian certification','Preparation for a Safe Apnea Test',
 'An adult meets the other prerequisites for a 2023 US BD/DNC evaluation and has no chronic CO2 retention. Which apnea-test preparation is appropriate?',
 'Establish normal baseline PaCO2/pH, adequate oxygenation and stable hemodynamics before testing',[
 ('Begin from induced hypocapnia so the test can continue longer before CO2 becomes high','An artificially low baseline changes the required stimulus and interpretation; the guideline calls for appropriate baseline gases rather than prophylactic hyperventilation.'),
 ('Disconnect immediately without preoxygenation because desaturation is part of the test','Hypoxemia is a complication to prevent, not a diagnostic endpoint; the test assesses respiratory drive under an adequate hypercarbic/acidemic stimulus.'),
 ('Use end-tidal CO2 alone instead of arterial gases to establish the endpoint','End-tidal measurements do not reliably substitute for arterial PaCO2 and pH, particularly during apnea and abnormal pulmonary physiology.')],
 [S('Confirm Readiness Before Testing','**Without chronic CO2 retention, establish PaCO2 35–45 mmHg and pH 7.35–7.45** before the test under the 2023 US guideline.',
    'Preoxygenate with 100% oxygen for at least ten minutes, aiming for PaO2 above 200 mmHg, and ensure the patient is not hypovolemic, hypotensive or hypoxemic.',
    'Use an appropriate arterial sampling and monitoring plan, trained personnel and equipment to restore ventilation immediately if needed.'),
  S('Maintain Oxygenation While Observing Respiratory Effort','**Use a guideline-supported oxygenation method**, selected for the patient and available expertise. Avoid unrecognized ventilator autocycling or a technique that obscures genuine respiratory effort.',
    'Observe the chest and abdomen carefully and obtain arterial gases at appropriate times. The elapsed minutes alone do not establish a completed test.',
    'Chronic hypercapnia, ECMO and substantial pulmonary disease require specific technical consideration rather than a generic disconnection protocol. If safe performance is not possible, follow the defined ancillary pathway. Do not start an unsafe test simply to complete a form; adequate prerequisites and a clear stopping plan are part of a valid examination.')],['BD'],style='direct')

add('Apnea testing, ancillary studies and Indian certification','The US Apnea Endpoint Requires Both CO2 and pH Criteria',
 'In a 2023 US adult apnea test without chronic CO2 retention, no respiratory effort occurs. Which final arterial result meets the stated biochemical endpoint when baseline PaCO2 was 40 mmHg?',
 'PaCO2 62 mmHg with pH 7.25',[
 ('PaCO2 58 mmHg with pH 7.24','Although acidemia is present, PaCO2 has not reached 60 mmHg or risen at least 20 mmHg from the stated baseline.'),
 ('PaCO2 62 mmHg with pH 7.32','The CO2 conditions are met, but the 2023 US criterion also requires arterial pH below 7.30.'),
 ('PaCO2 60 mmHg with pH 7.30','The CO2 conditions are met, but a pH exactly 7.30 does not satisfy the specified less-than-7.30 requirement.')],
 [S('Apply Every Endpoint Condition','**With no respiratory effort, the 2023 US framework requires pH below 7.30 and PaCO2 at least 60 mmHg and at least 20 mmHg above baseline.** All conditions must be satisfied.',
    'From a baseline of 40, a final PaCO2 of 62 is a rise of 22 mmHg. Together with pH 7.25 it meets the biochemical stimulus described.',
    'Meeting these numbers does not complete the entire death determination if other prerequisites or examination components are unmet.'),
  S('Account for Chronic Hypercapnia','**Known chronic CO2 retention requires reference to the patient’s known chronic baseline**, not an assumed normal value created by ventilator settings.',
    'When chronic retention is suspected but its baseline is unknown, the guideline includes an ancillary requirement despite an otherwise compatible apnea result because adequacy of the stimulus remains uncertain.',
    'A genuine spontaneous breath prevents an apnea result consistent with BD/DNC regardless of gas values. Continue safety monitoring throughout and stop for defined instability. Attribute this endpoint to the specified US guideline; do not assume its exact pH and CO2 formulation automatically replaces the legally applicable Indian testing protocol.')],['BD'],style='direct')

add('Apnea testing, ancillary studies and Indian certification','Stop an Unsafe Apnea Test',
 'During an apnea test under the 2023 US protocol, oxygen saturation progressively falls below 85% before an adequate endpoint gas is documented. Which next action is appropriate?',
 'Abort the test, restore oxygenation/ventilation and reassess a safe repeat or ancillary pathway',[
 ('Continue until ten minutes have elapsed because a shorter test is invalid','A planned duration does not override instability; the endpoint depends on physiology and observed effort, not completing a fixed interval despite danger.'),
 ('Call the test positive because desaturation prevented breathing','Hypoxemia is not the required respiratory-drive stimulus and an incomplete unsafe test cannot be converted into a completed compatible result.'),
 ('Certify from the preceding absent reflexes without addressing the incomplete test','The apnea component must be completed or handled through an appropriate authorized alternative; an incomplete result is not assumed absent.')],
 [S('Recognize Mandatory Safety Limits','**Progressive desaturation below 85% requires stopping under the 2023 US guideline.** Hypotension despite support or an unstable arrhythmia also requires interruption.',
    'If feasible, obtain an arterial sample before restoring ventilation to determine whether the biochemical endpoint had already been reached, without delaying rescue.',
    'A spontaneous breath is a different stopping reason: it demonstrates respiratory drive and is incompatible with the required apnea finding.'),
  S('Do Not Convert an Incomplete Test Into a Diagnosis','**Restore stable physiology and identify why the test became unsafe.** Oxygenation technique, pulmonary disease and hemodynamics may permit a safer repeat after correction.',
    'When testing cannot be safely completed, use the guideline’s defined ancillary approach and complete the clinical evaluation as far as possible.',
    'Record the reason for stopping, observed respiratory activity and available gases. Do not invent endpoint values or assume that a severe initial injury makes missing data irrelevant. The safety and validity of the procedure are linked; preventing a test-related arrest is not an obstacle to correct determination but a requirement of responsible assessment.')],['BD'])

add('Apnea testing, ancillary studies and Indian certification','Ancillary Testing Has Indications and Limits',
 'A patient meets BD/DNC prerequisites, but severe facial injury prevents reliable assessment of required brainstem components. Which principle is appropriate under the 2023 US guideline?',
 'Complete the clinical examination as far as safely possible and use an accepted ancillary study for the unresolved required components',[
 ('Use ancillary testing routinely in every patient regardless of a complete interpretable examination','Ancillary studies are reserved for specified limitations or uncertainties, rather than being mandatory confirmatory tests after every complete valid clinical determination.'),
 ('Use an ancillary study to bypass high sedative levels','Unresolved major CNS drug effects are a prerequisite problem and should not be bypassed by ancillary testing under this guideline.'),
 ('Accept an ancillary result despite a preserved brainstem reflex','Observed brain-mediated function prevents the determination; an ancillary result cannot override a finding that is incompatible with BD/DNC.')],
 [S('Use Ancillary Studies for a Defined Unresolved Question','**An examination or apnea test that cannot be completed or interpreted can justify ancillary testing.** Examples include relevant anatomic injury, unsafe apnea testing or uncertain movement origin.',
    'Certain uncorrectable metabolic abnormalities have a defined role in this pathway. The specific oculocephalic exception discussed in the guideline should not be generalized to every missing component.',
    'Perform and document the safe clinical portions first and ensure findings are otherwise consistent with the determination.'),
  S('Preserve the Prerequisite Framework','**Ancillary tests do not replace establishing the catastrophic permanent mechanism or excluding hypothermia and high sedative effects.** They are not a shortcut for an inconvenient examination.',
    'Choose a modality accepted by the stated guideline and interpreted by qualified personnel with an adequate technical study. A nondiagnostic result does not establish death.',
    'Local law and authorized institutional protocols determine applicability. If clinical findings show consciousness, a brainstem reflex or spontaneous breathing, stop the determination rather than seeking another test to negate it. Clearly document the indication, limitations and interpretation so that the study answers the actual unresolved question.')],['BD'])

add('Apnea testing, ancillary studies and Indian certification','Selecting an Accepted Adult Ancillary Perfusion Study',
 'An adult meets BD/DNC prerequisites, but apnea testing remains unsafe despite optimization. Under the 2023 US consensus guideline, which available investigation is accepted for this ancillary indication?',
 'Technically adequate transcranial Doppler ultrasonography interpreted by an experienced examiner',[
 ('CT angiography using the local stroke acquisition protocol','CTA evaluates arterial anatomy and stroke occlusion, but the 2023 US guideline does not accept it as a BD/DNC ancillary test because validation is insufficient.'),
 ('MR angiography with diffusion-weighted brain imaging','MRI and MRA can characterize injury and vessels, but are not accepted ancillary modalities in this guideline because adequate validation is lacking.'),
 ('Continuous EEG reviewed for electrocerebral inactivity','EEG is valuable for seizures and cortical activity, but does not establish loss of brainstem function and is not accepted for this ancillary indication.')],
 [S('Match the Modality to the Stated Guideline','**Accepted adult modalities include conventional four-vessel catheter angiography, radionuclide perfusion imaging and transcranial Doppler.** Availability alone does not establish diagnostic validity.',
    'TCD requires characteristic circulatory-arrest waveforms; failure to obtain a signal through an inadequate acoustic window is not equivalent to demonstrating arrested flow.',
    'The pediatric distinction matters: the guideline accepts TCD in adults, not children. Each modality requires appropriate acquisition and expert interpretation.'),
  S('Document the Unresolved Clinical Component','**Record why ancillary testing is necessary and complete the safe examination components first.** A nondiagnostic study requires reassessment, rather than a declaration based on presumed severity.',
    'Confirm that prerequisites remain satisfied at the time of investigation. Ancillary testing cannot override observed brain-mediated function or bypass unresolved sedative effects.',
    'Specify jurisdiction when teaching this selection: a modality accepted elsewhere is not automatically accepted under this guideline. In clinical practice, use the legally applicable institutional pathway and retain the technical report with the determination record. The ordering clinician should communicate the precise diagnostic question to the interpreting specialist; a routine vascular study obtained for a different indication may not answer it.')],['BD'])

add('Apnea testing, ancillary studies and Indian certification','Electrical Silence Does Not Establish Brainstem Failure',
 'An ICU patient has electrocerebral inactivity on a technically adequate EEG. Under the 2023 US BD/DNC guideline, which interpretation is most appropriate?',
 'The EEG finding does not substitute for the required brainstem and respiratory assessment',[
 ('The EEG finding completes the determination if motor responses are absent','Absent motor responses can reflect several mechanisms, and EEG does not test the entire brainstem or replace the prerequisites and required assessment.'),
 ('Adding somatosensory evoked potentials makes EEG an accepted ancillary combination','Evoked potentials examine restricted pathways; adding them does not provide the comprehensive brainstem assessment required for an accepted ancillary determination.'),
 ('The EEG finding eliminates the need to review sedative exposure','CNS depressants can alter electrophysiology as well as the clinical examination, so drug effects remain a prerequisite issue requiring independent evaluation.')],
 [S('Understand What the Recording Samples','**Scalp EEG primarily evaluates cerebral cortical electrical activity.** Electrical silence does not establish absence of every brainstem function.',
    'The 2023 US guideline therefore does not accept EEG, auditory evoked potentials or somatosensory evoked potentials as ancillary tests for this purpose.',
    'This restriction concerns death determination, not the usefulness of EEG for seizures, encephalopathy or selected prognostic questions.'),
  S('Keep Diagnostic Questions Separate','**An investigation must answer the clinical question being asked.** A technically excellent recording can still be unsuitable for a different diagnostic purpose.',
    'Record the indication, relevant medicines, temperature and physiologic conditions when interpreting electrophysiology. Describe the observed finding without extending it beyond the test’s domain.',
    'If a required clinical component cannot be assessed safely, establish the indication for an accepted ancillary modality rather than relabeling a previously obtained EEG. Communicate clearly with families: lack of detectable cortical activity on one recording is not, by itself, a complete declaration of death. Conversely, a test obtained for seizure monitoring should be interpreted according to its own clinical purpose, with appropriate attention to artifact and technical adequacy.')],['BD'])

R['FORM10']=('Government of India: Form 10, certification of brain-stem death','https://www.notto.mohfw.gov.in/WriteReadData/Portal/images/FORM10.pdf')

add('Apnea testing, ancillary studies and Indian certification','Adult Repeat Examination in Indian Form 10',
 'Under the adult minimum interval explicitly specified in Indian Form 10, when may the second brain-stem death examination follow the first?',
 'At least six hours later',[
 ('At least two hours later','Two hours does not meet the minimum adult interval printed in Form 10, even if both examinations are otherwise technically adequate.'),
 ('At least twelve hours later','A longer observation may be clinically appropriate, but twelve hours is not the minimum adult interval specified by this form.'),
 ('At least twenty-four hours later','Twenty-four hours may arise in other age-specific or clinical protocols, but it is not the stated adult minimum in Indian Form 10.')],
 [S('Identify the Jurisdiction Before Applying an Interval','**Indian Form 10 specifies at least six hours between adult examinations.** Both assessments require valid clinical conditions; elapsed time cannot correct an invalid examination.',
    'Document the actual dates and times, examination findings, applicable prerequisites and the identity of the examining board.',
    'Do not import a different country’s adult examination rule simply because its clinical guideline is more familiar.'),
  S('Use the Interval as One Part of Certification','**An observation interval is not an independent diagnostic test.** The underlying cause, exclusion of reversible confounders and required clinical assessment remain essential.',
    'If sedation, hypothermia, hemodynamic instability or another unresolved factor prevents valid testing, address that factor rather than scheduling a second invalid examination.',
    'Separate the timing of the examinations from subsequent administrative tasks and any discussion of donation. A family’s decision about donation cannot shorten the required assessment. Similarly, a transfer between hospitals does not justify reconstructing undocumented findings from memory: obtain the original records and follow the authorized local process. Numerical examination questions should name the governing form or guideline because superficially similar questions may have different answers across jurisdictions.')],['FORM10'],style='direct')

add('Apnea testing, ancillary studies and Indian certification','Indian Brain-Stem Death Certifying Board',
 'Which group corresponds to the four positions listed for signatures on Indian Form 10, before considering its authorized substitution provision?',
 'Hospital medical administrator, authorized specialist, neurologist/neurosurgeon and treating medical officer',[
 ('Hospital medical administrator, transplant coordinator, neurologist/neurosurgeon and treating medical officer','The coordinator supports communication and logistics, but does not replace the authorized specialist position listed for medical certification on Form 10.'),
 ('Hospital medical administrator, authorized specialist, neurologist/neurosurgeon and recipient surgeon','The listed fourth position is the medical officer treating the patient; a recipient surgeon is not a substitute merely because transplantation is being considered.'),
 ('Hospital medical administrator, authorized specialist, anesthetist and treating medical officer','An anesthetist may participate through the specified substitution pathway, but this list omits the neurologist/neurosurgeon position asked for before substitution.')],
 [S('Recognize the Listed Positions','**Form 10 lists the administrator, authorized specialist, neurologist/neurosurgeon and treating medical officer.** Its panel and substitution notes must also be followed.',
    'The authorized specialist and neurologist/neurosurgeon positions are co-opted from a hospital-nominated panel approved by the Appropriate Authority.',
    'When neurologic specialists are unavailable, the form provides a nomination pathway involving a surgeon or physician and an anesthetist or intensivist; it is not unrestricted replacement by any available doctor.'),
  S('Verify Authority Before Beginning the Process','**Check the current approved panel and applicable institutional implementation.** Clinical expertise and legal authorization are related requirements but are not interchangeable.',
    'The administrator should resolve availability and authorized substitution through the prescribed pathway. Do not invent an informal board because a transplant deadline is approaching.',
    'Each examiner’s findings and signatures must be attributable and accurately timed. A coordinator may help assemble documentation and support the family, but administrative assistance does not transfer medical certification responsibility. Keep the assessment independent of organ allocation and the recipient’s condition. When teaching a board-composition question, specify whether it asks for the printed positions or an authorized alternative; otherwise more than one reasonable arrangement may appear defensible.')],['FORM10'],style='direct')

add('Apnea testing, ancillary studies and Indian certification','Pediatric Intervals Require an Age-Specific Protocol',
 'A team proposes automatically using the adult six-hour minimum for every child because it appears on Indian Form 10. Which response best reflects the form’s pediatric qualification?',
 'Use the longer age-appropriate interval determined by the certifying experts and the applicable pediatric protocol',[
 ('Use six hours for all ages once the injury is structural','A structural mechanism does not remove the form’s pediatric qualification or the need for an age-appropriate certification pathway.'),
 ('Use the adult interval whenever an ancillary study is available','Availability of a test does not independently waive age-related examination requirements or establish authorization to shorten observation.'),
 ('Use a single examination once the family agrees to donation','Donation consent does not substitute for valid death determination or eliminate the required repeat assessment and observation.')],
 [S('Read the Pediatric Qualification Explicitly','**Form 10 calls for increased intervals in children and infants according to the BSD experts’ opinion.** It does not provide one universal pediatric numeric interval.',
    'Its age categories include children aged 6–12 years, those aged 1–5 years and infants. Apply the current authorized pediatric pathway to the actual age and circumstances.',
    'Do not silently replace this wording with a foreign society guideline and describe the imported numbers as the text of Indian law.'),
  S('Distinguish a Legal Form From a Clinical Recommendation','**Document which recommendation and institutional protocol support the chosen interval.** When requirements differ, resolve the applicable process before certification.',
    'Prematurity, very young age, injury mechanism and unresolved confounders require particular attention from experienced pediatric clinicians.',
    'A longer observation period cannot compensate for an uncertain diagnosis or an uninterpretable examination. Explain to the family why repeated assessment is necessary and what remains to be established. Avoid giving a promised declaration time before prerequisites are met. For examination preparation, retain both the adult minimum and the explicit pediatric qualification; memorizing one number for every age creates a clinically important error even when the adult answer itself is correct.')],['FORM10'])

R.update({
 'DONOR':('ISCCM position statement: management of potential organ donor, 2024','https://pmc.ncbi.nlm.nih.gov/articles/PMC11369920/'),
 'WE':('UK clinical alcohol-treatment guidance: Wernicke encephalopathy treatment','https://www.gov.uk/guidance/clinical-guidelines-for-alcohol-treatment/16-alcohol-care-in-acute-hospitals'),
 'PRES':('Triplett et al. PRES diagnosis and management, Practical Neurology 2022','https://doi.org/10.1136/practneurol-2021-003194'),
})

add('Apnea testing, ancillary studies and Indian certification','Certification and Donation Are Separate Decisions',
 'The family of an Indian ICU patient undergoing brain-stem death assessment declines organ donation. Which approach to the medical assessment is appropriate?',
 'Complete the clinically indicated, legally valid assessment and documentation independently of the donation decision',[
 ('Postpone the assessment until donation consent is obtained','Donation authorization concerns organ retrieval; it does not determine whether the clinical evidence fulfills the requirements for death certification.'),
 ('Shorten repeat testing because organ retrieval will not occur','The absence of a retrieval plan does not change the validity requirements or permit omission of the required clinical assessments.'),
 ('Ask the transplant coordinator to replace the certifying board','The coordinator can support communication and documentation, but medical determination remains the responsibility of the authorized certifying clinicians.')],
 [S('Maintain Independent Medical Determination','**Certification depends on the prescribed clinical findings and authorized process.** A donation preference cannot supply missing examination findings or negate valid ones.',
    'Record the cause, exclusion of confounders, prerequisites, examination and apnea-test findings, dates, times and required signatures accurately.',
    'Use the applicable Indian form and institutional pathway. Unresolved components must be addressed through an authorized process rather than hidden in a completed checklist.'),
  S('Explain the Findings With Care','**Families need a clear account of what has been assessed and what it means.** Avoid using donation language as the explanation for the medical diagnosis.',
    'Allow questions, check understanding and distinguish ongoing ventilator-supported circulation from recovery of brain function. Describe uncertainty honestly if the determination is incomplete.',
    'Donation requires its own appropriate authorization and coordination. Family support remains necessary regardless of the decision. A coordinator can assist with logistics and communication while the certifying team retains responsibility for findings and records. Do not promise recipients or organ availability before the relevant processes are complete. Accurate documentation should allow another authorized clinician to reconstruct the sequence from contemporaneous evidence, without relying on informal recollection or assumptions about why assessment was initiated.')],['FORM10','DONOR'])

add('Other high-yield neurocritical and behavioral syndromes','Wernicke Encephalopathy Without the Complete Triad',
 'A malnourished adult with prolonged heavy alcohol use develops confusion and a broad-based gait. Eye movements are normal. Glucose has been corrected, but symptoms persist. Which next approach is most appropriate?',
 'Treat suspected Wernicke encephalopathy promptly with parenteral thiamine while evaluating competing causes',[
 ('Use oral thiamine alone while awaiting the appearance of ophthalmoplegia','Oral replacement may be appropriate after acute treatment or for selected prophylaxis, but suspected symptomatic disease requires prompt parenteral treatment without waiting for the full triad.'),
 ('Obtain MRI confirmation before administering thiamine','MRI may support the diagnosis and investigate alternatives, but a normal or delayed scan cannot safely exclude the condition or justify postponing treatment.'),
 ('Treat as alcohol withdrawal alone and reassess after sedation','Withdrawal can coexist, but sedation does not correct thiamine deficiency and may obscure persistent neurologic abnormalities requiring specific treatment.')],
 [S('Recognize an Incomplete Clinical Presentation','**Confusion, gait ataxia and ocular abnormalities need not all be present.** Malnutrition and compatible neurologic findings warrant a low threshold for treatment.',
    'Consider dietary deficiency, eye signs, cerebellar dysfunction and altered mental state or memory impairment together; the complete classic triad is an insensitive requirement.',
    'MRI can support the diagnosis but does not replace clinical judgment. Check for infection, withdrawal, intoxication, structural disease and metabolic contributors in parallel.'),
  S('Separate Treatment From Prophylaxis','**Suspected symptomatic Wernicke encephalopathy requires parenteral therapy.** UK guidance recommends ==thiamine 300–500 mg IV three times daily for 3–5 days==, with daily review.',
    'If still symptomatic after five days, that guidance uses 300–500 mg IV once daily for a further 3–5 days and while improvement continues. Regimens differ between authorities; state the regimen being used.',
    'Correct magnesium deficiency and nutritional deficits, monitor the response and follow parenteral-administration precautions. Do not delay emergency glucose for hypoglycemia while arranging thiamine. Prevention doses are not interchangeable with treatment of established neurologic disease. After the acute course, provide ongoing supplementation and nutritional and alcohol-use care; residual memory impairment may persist despite improvement in eye signs or gait.')],['WE','ASAM'])

add('Other high-yield neurocritical and behavioral syndromes','Posterior Reversible Encephalopathy Syndrome',
 'A renal transplant recipient receiving tacrolimus develops headache, seizures and blurred vision with marked hypertension. MRI shows bilateral parieto-occipital subcortical FLAIR hyperintensity with increased ADC. Which diagnosis best integrates the findings?',
 'Posterior reversible encephalopathy syndrome',[
 ('Bilateral posterior cerebral artery infarction','PCA infarction can cause visual loss, but acute cytotoxic ischemia typically restricts diffusion and follows an arterial distribution rather than the stated vasogenic edema pattern.'),
 ('Progressive multifocal leukoencephalopathy','Immunosuppression raises this possibility, but its usually progressive focal course and asymmetric white-matter injury fit less well than an acute hypertensive seizure syndrome.'),
 ('Cerebral venous sinus thrombosis','Venous thrombosis can produce seizures and edema and requires venous imaging when suspected, but this clinical trigger and symmetric posterior vasogenic pattern favor PRES.')],
 [S('Interpret the Clinicoradiographic Pattern','**PRES combines acute neurologic symptoms with predominantly vasogenic edema.** Increased ADC supports extracellular edema; restricted diffusion can indicate superimposed injury.',
    'Hypertension, renal dysfunction, eclampsia and endothelial-toxic medicines are important settings. Posterior predominance is characteristic but neither exclusive nor mandatory.',
    'Hemorrhage, infarction and persistent deficits can occur; the word reversible does not guarantee a benign outcome.'),
  S('Treat the Precipitant and Immediate Complications','**Control seizures and reduce severe blood pressure with monitored, titratable treatment.** Avoid abrupt excessive lowering that compromises cerebral perfusion.',
    'Review tacrolimus exposure, drug interactions, renal function and the immunosuppression plan with the transplant team rather than stopping essential therapy without a replacement strategy.',
    'Evaluate atypical findings for arterial or venous ischemia, infection and other competing diagnoses. Repeat clinical assessment and follow-up imaging can document the evolution. A normal early CT does not exclude the MRI-defined syndrome. In a patient with persistent impaired awareness after convulsions, obtain EEG to assess ongoing seizures. Recovery and the duration of antiseizure treatment depend on the injury and clinical course, rather than an assumption that every patient needs indefinite therapy.')],['PRES'])

R.update({
 'SEROTONIN':('Austin Clinical Toxicology Service: serotonin toxicity guideline','https://www.austin.org.au/Assets/Files/Serotonin%20Toxicity%20Guidelines.March2024.pdf'),
 'BAP':('BAP evidence-based consensus guideline on catatonia, 2023','https://pmc.ncbi.nlm.nih.gov/articles/PMC10101189/'),
 'SEROTONIN2':('Chiew and Isbister: management of serotonin toxicity, 2024','https://doi.org/10.1111/bcp.16152'),
})

add('Other high-yield neurocritical and behavioral syndromes','Serotonin Toxicity and Neuromuscular Excitation',
 'Hours after linezolid is added to sertraline, a patient becomes agitated and diaphoretic, with diarrhea, temperature 39.2°C, ocular clonus and brisk leg reflexes. Which diagnosis is most likely?',
 'Serotonin toxicity',[
 ('Neuroleptic malignant syndrome','NMS usually follows dopamine blockade or withdrawal of dopaminergic therapy and favors generalized rigidity; the rapid serotonergic interaction with clonus and hyperreflexia is more characteristic of serotonin toxicity.'),
 ('Antimuscarinic toxicity','Antimuscarinic poisoning can cause agitation, hyperthermia and mydriasis, but typically produces dry skin and reduced bowel activity rather than diaphoresis, diarrhea and clonus.'),
 ('Malignant catatonia','Malignant catatonia combines catatonic signs with systemic instability and may precede drug exposure; this abrupt interaction-related neuromuscular excitation is more consistent with serotonin toxicity.')],
 [S('Integrate Exposure With the Examination','**Clonus and hyperreflexia are major discriminators in a compatible serotonergic exposure.** Review recent starts, dose escalation, interactions and overdose rather than considering each prescription separately.',
    'With serotonergic exposure, Hunter patterns include spontaneous clonus; inducible or ocular clonus with agitation or diaphoresis; tremor with hyperreflexia; or hypertonia with temperature above 38°C and ocular or inducible clonus.',
    'Severe rigidity can mask clonus. Do not dismiss a critically ill patient because a complete textbook pattern is difficult to elicit.'),
  S('Reduce Muscle Activity and Prevent Organ Injury','**Stop serotonergic contributors and provide monitored supportive care.** Benzodiazepines, active cooling, fluids and management of complications are central.',
    'Severe hyperthermia with rigidity may require airway control, ventilation and nondepolarizing paralysis. Antipyretics do not address heat generated by excessive muscular activity.',
    'Cyproheptadine is an enteral adjunct, not a substitute for resuscitation; Austin guidance uses 12 mg initially then 2 mg every two hours until response. Evidence for outcome benefit is limited. Discuss severe cases with toxicology, monitor CK, renal function and electrolytes, and assess coingestants. Reintroduction of psychiatric therapy requires review of the interaction, washout and clinical recovery rather than immediate resumption of the previous combination.')],['SEROTONIN','SEROTONIN2'])

add('Other high-yield neurocritical and behavioral syndromes','Neuroleptic Malignant Syndrome Requires Withdrawal and Support',
 'Three days after a substantial haloperidol dose increase, a patient develops confusion, temperature 40.3°C, generalized rigidity, autonomic instability and CK 18000 U/L. There is no clonus. Which immediate management strategy is most appropriate?',
 'Stop dopamine-blocking drugs and begin intensive supportive care with cooling and complication monitoring',[
 ('Continue haloperidol and add cyproheptadine as the principal treatment','Cyproheptadine is sometimes used for serotonin toxicity; continuing the likely dopamine-blocking trigger would sustain the suspected NMS mechanism.'),
 ('Use bromocriptine as the sole intervention on the ward','A dopamine agonist may be considered with specialist input, but it cannot replace resuscitation, cooling and monitoring in this severe systemic presentation.'),
 ('Give antipyretics and observe before changing the antipsychotic','Antipyretics alone do not adequately treat muscle-related hyperthermia or remove the suspected trigger; delay risks renal injury and further deterioration.')],
 [S('Recognize a Drug-Associated Systemic Emergency','**NMS is associated with dopamine antagonism and can also follow abrupt withdrawal of dopaminergic treatment.** Medication chronology and examination help distinguish it from other hyperthermic syndromes.',
    'Raised CK supports muscle injury but is neither specific nor mandatory. Check electrolytes, renal function, urine output and complications of rhabdomyolysis.',
    'Investigate infection, seizures, heat illness and other mimics when indicated; a suspected medicine reaction does not exclude a concurrent illness.'),
  S('Escalate According to Severity','**Withdrawal of the trigger and intensive supportive treatment are foundational.** Address airway safety, temperature, circulating volume and organ dysfunction promptly.',
    'BAP guidance supports specialist consideration of lorazepam, dopamine agonists or dantrolene according to severity; ECT can be relevant for persistent severe disease or catatonic features. These are not interchangeable mandatory antidotes.',
    'Evidence is largely observational. Drug choice must consider contraindications and organ function, with close clinical monitoring. Prevent aspiration, thrombosis and pressure injury while immobility persists. After recovery, reassess whether an antipsychotic remains necessary, allow an appropriate recovery interval and use a cautious specialist-supervised strategy if restarting. Record the reaction and avoid recreating the same rapid escalation and dehydration risks.')],['BAP'])

add('Other high-yield neurocritical and behavioral syndromes','Malignant Catatonia and Early ECT Planning',
 'Before receiving any antipsychotic, a patient develops mutism, posturing, negativism and episodic excitement, followed by fever and marked autonomic instability. Infection and metabolic assessment is underway. Which treatment pathway is most appropriate?',
 'Begin monitored lorazepam treatment and urgently arrange specialist ECT assessment while treating systemic complications',[
 ('Escalate a potent dopamine antagonist to suppress the motor behavior','Antipsychotics can worsen catatonic syndromes and precipitate NMS; prominent catatonic signs with malignant physiology require a different urgent pathway.'),
 ('Wait for antibody results before treating the catatonic syndrome','Autoimmune encephalitis is an important possible cause, but etiologic testing should proceed alongside treatment rather than delaying intervention for a life-threatening syndrome.'),
 ('Manage as serotonin toxicity using cyproheptadine alone','The history lacks the characteristic serotonergic trigger and excitation pattern, while prominent antecedent catatonia requires benzodiazepine and ECT consideration with systemic support.')],
 [S('Recognize Malignant Physiology in Catatonia','**Fever and autonomic instability accompanying catatonic motor and behavioral signs indicate a medical emergency.** Catatonia may occur with psychiatric, neurologic or systemic disease.',
    'Assess for encephalitis, seizures, medication effects or withdrawal and metabolic illness. The chronology before dopamine blockade helps distinguish the presentation from typical drug-triggered NMS, although overlap exists.',
    'Support hydration, nutrition, airway safety and renal function; immobility also requires thrombosis and pressure-injury prevention.'),
  S('Treat While Investigating the Cause','**Lorazepam and ECT are key treatments, with urgent ECT planning in malignant disease.** A monitored 1–2 mg IV lorazepam challenge can support assessment, but a negative response does not exclude catatonia.',
    'BAP guidance recommends ECT if response to lorazepam is partial or absent within 48–72 hours; rapid deterioration warrants urgent escalation rather than waiting for the full interval.',
    'Further benzodiazepine dosing requires individualized titration and respiratory monitoring. Coordinate psychiatry, neurology, anesthesia and critical care early, including capacity and consent processes under applicable law. Treat an identified underlying cause in parallel. The evidence base includes substantial observational experience rather than large definitive trials, so communicate anticipated benefit and risks honestly while avoiding delay in a potentially fatal syndrome.')],['BAP'])

R.update({
 'ICUAW':('ATS clinical practice guideline: diagnosis of ICU-acquired weakness','https://www.thoracic.org/statements/resources/cc/ICUAW_cpg.pdf'),
 'DOCAAN':('AAN/ACRM/NIDILRR disorders of consciousness guideline, 2018','https://doi.org/10.1212/WNL.0000000000005926'),
 'FND':('Australian health-professional recommendations for functional neurological disorder, 2025','https://neurologyopen.bmj.com/content/7/1/e000970'),
})

add('Other high-yield neurocritical and behavioral syndromes','ICU-Acquired Weakness After Critical Illness',
 'After two weeks of sepsis and ventilation, a patient is awake, follows commands and has symmetric flaccid limb weakness with difficulty weaning. Sensory nerve action potentials and motor response amplitudes are reduced without a demyelinating pattern. Which mechanism best fits?',
 'Critical illness polyneuropathy',[
 ('Critical illness myopathy alone','Myopathy can cause similar weakness and weaning failure, but sensory responses are generally preserved; reduced sensory amplitudes favor an axonal neuropathic component.'),
 ('Residual neuromuscular blockade','Drug-related blockade can impair movement and ventilation, but does not explain the described axonal sensory response abnormalities; assess drug exposure and neuromuscular transmission separately.'),
 ('Persistent hypoxic coma','This patient is awake and follows commands, so impaired consciousness cannot explain the motor deficit; peripheral weakness must be distinguished from failure to awaken.')],
 [S('Localize Weakness Separately From Consciousness','**ICU-acquired weakness may reflect polyneuropathy, myopathy or both.** A patient can understand commands yet lack the motor strength to demonstrate a normal examination.',
    'Assess strength when cooperation is adequate. The MRC sum evaluates six bilateral muscle groups, each scored 0–5, for a total of 60; a score below 48 commonly defines significant ICU-acquired weakness.',
    'Sedation, delirium, pain and poor cooperation limit manual testing. Review electrolytes, medication effects and other neurologic causes before attributing weakness to critical illness.'),
  S('Use Electrophysiology for the Relevant Distinction','**Reduced sensory and motor amplitudes support axonal polyneuropathy.** Preserved sensory responses with myopathic findings support myopathy, although overlap is common.',
    'Nerve conduction studies, needle EMG and sometimes direct muscle stimulation help clarify the mechanism when the result will inform care.',
    'Treat the underlying critical illness, optimize nutrition and mobilization as tolerated, and plan respiratory and functional rehabilitation. A label of ICU-acquired weakness does not eliminate the need to investigate atypical asymmetry, cranial findings, a sensory level or evolving weakness. Prognosis depends on the injury, comorbidity and rehabilitation trajectory. Avoid interpreting an inability to lift the limbs as evidence of absent awareness, particularly during discussions of recovery and goals of care.')],['ICUAW'])

add('Other high-yield neurocritical and behavioral syndromes','Minimally Conscious State Requires Reproducible Evidence',
 'Six weeks after severe brain injury, a patient has sleep–wake cycles. Across repeated standardized examinations, the patient reproducibly follows a simple command on some trials, although performance fluctuates. Which classification best fits?',
 'Minimally conscious state',[
 ('Unresponsive wakefulness syndrome','This syndrome includes wakefulness without behavioral evidence of awareness; reproducible command following provides evidence beyond reflexive wakefulness.'),
 ('Coma','Coma lacks wakefulness as well as awareness; established sleep–wake cycles and intermittent command following are inconsistent with ongoing coma.'),
 ('Emergence from minimally conscious state','Emergence requires reliable functional communication or functional object use; intermittent simple command following establishes awareness but not that higher threshold.')],
 [S('Separate Arousal From Awareness','**Minimally conscious state includes definite but limited evidence of awareness.** Responses may fluctuate, so repeat standardized assessment rather than relying on one brief encounter.',
    'Unresponsive wakefulness syndrome has eye opening and sleep–wake cycles without demonstrated awareness. Coma lacks wakefulness; neither term is synonymous with death by neurologic criteria.',
    'Functional communication or appropriate functional object use supports emergence from minimally conscious state, which is a separate threshold from occasional command following.'),
  S('Optimize the Opportunity to Demonstrate Awareness','**Use a validated instrument such as the Coma Recovery Scale–Revised and address confounders.** Sedatives, sleep disruption, seizures and systemic illness can lower performance.',
    'Motor, visual, auditory and language limitations can hide awareness. Adapt the examination, assess serially and involve clinicians experienced in disorders of consciousness.',
    'Explain the distinction between current diagnostic category and individual prognosis to the family. Continue pain assessment, rehabilitation and prevention of immobility complications. Specialist testing may be considered when behavior and other evidence are discordant, but an isolated test should not be stretched beyond its validated interpretation. Document which response was observed, its reproducibility and the conditions of testing so that apparent changes can be evaluated rather than inferred from inconsistent labels.')],['DOCAAN','DOC'])

add('Other high-yield neurocritical and behavioral syndromes','Functional Weakness Requires Positive Clinical Evidence',
 'A patient with recurrent leg weakness has a normal appropriate structural workup. On repeated examination, weak voluntary hip extension returns during contralateral hip flexion against resistance. Which interpretation is most appropriate?',
 'A positive Hoover sign supports functional weakness when integrated with the complete examination',[
 ('Normal imaging by itself establishes functional weakness','Normal imaging may exclude selected structural lesions, but does not independently provide the positive clinical evidence required for a functional diagnosis.'),
 ('The finding proves deliberate symptom fabrication','A positive functional sign identifies an inconsistency in motor performance, not intention; functional symptoms are not equivalent to malingering.'),
 ('The finding excludes coexisting neurologic disease','Functional symptoms can coexist with structural or other neurologic disorders, so new red flags and discordant findings still require assessment.')],
 [S('Make a Positive Clinical Diagnosis','**Hoover sign demonstrates a discrepancy between voluntary and automatic hip extension.** Interpret it in the context of pain, comprehension and the rest of the examination.',
    'Other presentations require their own appropriate positive signs; one motor sign is not a universal test for every functional symptom.',
    'A psychiatric history, stressor or normal scan is insufficient by itself. Symptoms can be disabling and involuntary even when their mechanism differs from a structural lesion.'),
  S('Explain the Finding and Address the Actual Disability','**Show how the examination supports the diagnosis and offer a treatment plan.** Use clear, respectful language that validates symptoms and describes potential for improvement.',
    'Specialist physiotherapy can retrain movement; psychological treatment and management of pain, fatigue or psychiatric comorbidity may be useful according to the individual presentation.',
    'Keep acute red flags in view: a new focal syndrome, altered consciousness, sphincter dysfunction or a changed examination may warrant renewed investigation. A previous functional diagnosis must not become a reason to dismiss a later illness. Avoid repeated nondirected testing once the diagnosis is well supported, while providing follow-up and an explanation of when reassessment is appropriate. Rehabilitation goals should focus on restoring function and confidence rather than requiring the patient to accept a psychological cause as a prerequisite for care.')],['FND'])

# Editorial replacements keep the source rationale with each competing option.
def revise(number, *, stem=None, answer=None, others=None):
    r=rows[number-1]
    if stem is not None:r['question']=stem
    if answer is not None:r['answer']=answer
    if others is not None:r['others']=others

revise(1,answer='Assisted ventilation with immediate bedside glucose and circulatory assessment',others=[
 ('Emergency noncontrast CT followed by CT angiography','Urgent imaging is appropriate for structural coma and basilar occlusion, but the stated shallow breathing requires stabilization before transport to the scanner.'),
 ('IV naloxone titration with targeted toxicology sampling','Naloxone is appropriate when opioid toxicity is suspected, but an undifferentiated patient still needs immediate ventilatory support and glucose assessment rather than antidote-centered evaluation.'),
 ('Urgent EEG with an IV antiseizure loading dose','EEG and antiseizure therapy are appropriate for suspected ongoing seizures, but there is no stated seizure evidence and inadequate ventilation takes immediate priority.')])
revise(2,answer='Bag-mask ventilation with naloxone titrated to adequate breathing',others=[
 ('Naloxone titration with supplemental oxygen by face mask','This may suffice in milder depression with adequate ventilation, but four breaths per minute requires assisted ventilation while the antidote takes effect.'),
 ('Flumazenil administration with bag-mask ventilation','Flumazenil reverses selected benzodiazepine effects but does not reverse opioids; unknown coingestion and dependence also increase seizure risk, while naloxone matches this suspected exposure.'),
 ('Immediate intubation with sedation and subsequent naloxone','Intubation is appropriate if bag-mask ventilation fails or airway protection remains inadequate, but a ventilatable opioid exposure should receive immediate assisted breaths and reversal without first delaying for induction.')])
revise(3,answer='Give IV glucose now and parenteral thiamine as soon as available',others=[
 ('Give parenteral thiamine first, followed by IV glucose','Thiamine should be prompt in a malnourished patient, but delaying immediately available glucose in severe symptomatic hypoglycemia risks ongoing brain injury.'),
 ('Give IM glucagon now, followed by thiamine and IV glucose','Glucagon is useful when IV access or glucose is unavailable, but immediate IV glucose is available here and depleted hepatic glycogen can reduce glucagon efficacy.'),
 ('Start a glucose-containing maintenance infusion and repeat the bedside value','An infusion can prevent recurrence after initial correction, but this profound symptomatic low glucose requires prompt rescue rather than maintenance-rate replacement alone.')])
revise(4,answer='Stabilize airway and perfusion, start herniation rescue and obtain urgent CT/neurosurgical assessment',others=[
 ('Obtain urgent MRI with diffusion imaging before selecting pressure treatment','MRI can characterize ischemia and brainstem injury, but acute deterioration with new anisocoria demands rapid stabilization and a fast structural assessment rather than delayed rescue.'),
 ('Load an IV antiseizure drug and obtain EEG before structural imaging','Seizures can cause impaired awareness and focal findings, but a newly dilated poorly reactive pupil with deterioration requires immediate evaluation for mass effect even if seizures coexist.'),
 ('Give a targeted sedative antagonist and reassess before neuroimaging','Reversal may help a documented medication effect, but new asymmetry and pupillary deterioration cannot safely be attributed to sedation without addressing a structural emergency.')])
revise(5,answer='Assess pupils, corneal responses and other safe components while preserving cervical alignment',others=[
 ('Perform the oculocephalic maneuver with a smaller range of neck rotation','A reduced rotation does not establish safety when cervical injury is unexcluded; the maneuver should wait until appropriate clearance.'),
 ('Use the absent vestibulo-ocular response as the primary localization sign','Vestibular testing can be useful under suitable conditions, but no response has been established here; assess contraindications and technical adequacy rather than assuming a finding.'),
 ('Defer the entire brainstem examination until cervical imaging is reported','Head rotation should be deferred, but pupils and other safe components provide immediate information without requiring cervical movement.')])
revise(6,answer='Urgent EEG, continuing monitoring if nonconvulsive seizures remain a concern',others=[
 ('Urgent noncontrast CT to assess a postictal structural complication','CT is appropriate for new focal findings, trauma or concern for hemorrhage, but does not determine whether the subtle movements and persistent impairment represent ongoing electrical seizures.'),
 ('Serum antiseizure drug concentration to assess adequacy of treatment','Levels can identify inadequate exposure for selected agents, but neither therapeutic nor low concentrations establish whether electrographic seizures are continuing now.'),
 ('Repeat lactate, blood gas and metabolic profile to assess seizure resolution','These tests identify contributors and physiologic consequences, but normalization does not exclude nonconvulsive seizures and cannot replace EEG for this question.')])
revise(10,stem='A patient with intracranial hypertension has stable systemic pressure but is lying flat with the neck rotated and a constrictive tube tie. Which initial positioning adjustment is most appropriate?',
 answer='Head elevation near 30 degrees with neutral neck alignment and repeat perfusion assessment',others=[
 ('Head elevation near 60 degrees with neutral neck alignment','Greater elevation may be individualized with pressure monitoring, but can reduce cerebral perfusion; approximately 30 degrees is the usual initial compromise rather than immediate steep elevation.'),
 ('Flat supine positioning with neutral neck alignment','Neutral alignment helps venous outflow, but remaining flat misses the additional usual benefit of modest elevation when blood pressure is stable; flat positioning may be needed with perfusion concerns.'),
 ('Reverse Trendelenburg near 15 degrees with the neck left rotated','Whole-bed tilt can be useful with spinal precautions, but persistent rotation and a constrictive tie can still obstruct venous drainage and should be addressed.')])
revise(12,answer='Brief controlled ventilation toward PaCO2 30–35 mmHg as a bridge',others=[
 ('Sustained controlled ventilation toward PaCO2 25–30 mmHg during the next day','More pronounced and prolonged hypocapnia can reduce cerebral blood flow and cause ischemia; rescue hyperventilation is a short bridge while the underlying cause is treated.'),
 ('Maintain PaCO2 40–45 mmHg while awaiting definitive treatment','Normocapnia is usually appropriate outside a crisis, but temporary controlled hypocapnia can provide a bridge during active herniation while definitive rescue is mobilized.'),
 ('Permit PaCO2 45–50 mmHg to reduce ventilator-associated injury','Permissive hypercapnia may be used in selected pulmonary strategies, but CO2-related cerebral vasodilation can worsen an active intracranial pressure crisis.')])
revise(13,answer='Treat ICP above 22 mmHg; generally target CPP 60–70 mmHg',others=[
 ('Treat ICP above 20 mmHg; generally target CPP 50–60 mmHg','An ICP threshold near 20 appears in older approaches, but the current BTF threshold is above 22 and the usual CPP range is 60–70 rather than 50–60.'),
 ('Treat ICP above 25 mmHg; generally target CPP 60–70 mmHg','The CPP range matches the guideline, but waiting for 25 rather than treating above 22 does not reflect the specified monitored-treatment threshold.'),
 ('Treat ICP above 22 mmHg; generally target CPP 80–90 mmHg','The ICP threshold matches, but routinely pursuing CPP above 70 with aggressive fluids and pressors can increase respiratory complications; targets require clinical individualization.')])

revise(7,answer='Classic locked-in syndrome',others=[
 ('Akinetic mutism','Akinetic mutism causes markedly reduced initiation with preserved wakefulness, but the combination of quadriplegia, anarthria and reliable vertical eye communication after a brainstem event favors locked-in syndrome.'),
 ('Minimally conscious state','This category implies limited and fluctuating evidence of awareness; reliable command-based communication through preserved eye movements instead supports intact awareness with impaired motor output.'),
 ('Unresponsive wakefulness syndrome','Eye opening can occur in this syndrome, but reliable eye responses to commands demonstrate awareness and are incompatible with an unresponsive wakefulness classification.')])
revise(8,answer='Record testable components and medication limitations; repeat when confounding is safely reduced',others=[
 ('Record the observed low GCS total as the admission neurologic baseline','A baseline score is useful when components are assessable, but paralysis and intubation prevent valid interpretation of an apparently low total as intrinsic neurologic severity.'),
 ('Use the motor component as the principal prognostic measure','Motor responses can inform assessment in an unconfounded patient, but recent neuromuscular blockade directly suppresses the response being interpreted here.'),
 ('Perform an immediate complete sedation interruption to obtain a score','A sedation interruption may permit examination when safe, but timing requires assessment of respiratory and intracranial stability and does not immediately remove residual neuromuscular blockade.')])
revise(9,answer='Hyperosmolar rescue and physiologic stabilization with urgent neurosurgical planning',others=[
 ('Dexamethasone with repeat examination after the initial clinical response','Dexamethasone is useful for selected tumor-associated vasogenic edema, but its effect is not an adequate immediate rescue for abrupt clinical herniation.'),
 ('Hyperosmolar rescue followed by serial imaging to assess the need for referral','A bolus may temporize the crisis, but improvement does not remove the need for immediate neurosurgical assessment of a mass causing acute deterioration.'),
 ('Controlled hyperventilation as the principal treatment pending scheduled imaging','Brief hypocapnia may serve as an emergency bridge, but pressure rescue and urgent definitive planning must proceed rather than relying on ventilation alone.')])
revise(11,stem='During a severe-TBI ICP crisis, a patient has persistent borderline hypotension despite resuscitation, sodium 140 mmol/L and no evidence of volume overload. Which hyperosmolar approach is most appropriate?',
 answer='A monitored hypertonic saline bolus with continued hemodynamic resuscitation',others=[
 ('A mannitol bolus followed by repeat volume and renal assessment','Mannitol lowers ICP and can be appropriate in a hemodynamically stable patient, but its osmotic diuresis may worsen this patient’s borderline perfusion; hypertonic saline is generally favored in this context.'),
 ('A continuous hypertonic saline infusion without an initial rescue bolus','An infusion may be used in selected monitored protocols, but it does not provide the same immediate rescue as a bolus during an acute ICP crisis.'),
 ('A loop-diuretic bolus followed by fluid restriction','Diuresis can be useful for systemic fluid overload, but this patient has no volume overload and needs perfusion-preserving ICP rescue rather than further intravascular depletion.')])
revise(14,answer='Urgent neurosurgical assessment for evacuation with parallel physiologic stabilization',others=[
 ('Hyperosmolar treatment followed by interval CT before operative referral','Hyperosmolar therapy can bridge to surgery, but neurologic deterioration with a substantial compressive hematoma requires immediate operative assessment even if the bolus improves the examination.'),
 ('ICP-monitor placement to establish a sustained pressure threshold before evacuation','An ICP monitor helps selected severe-TBI management, but a deteriorating patient with a demonstrated surgical mass should not wait for pressure documentation before evacuation assessment.'),
 ('Antiseizure loading followed by EEG before deciding on hematoma evacuation','Seizure treatment may be required when seizures coexist, but it does not address the established mass effect and should not delay neurosurgical action.')])
revise(15,stem='After severe TBI, ICP remains elevated despite optimized first-tier care. CT shows enlarging ventricles without an evacuable mass; ventricular catheter placement is feasible. Which next intervention most directly addresses the demonstrated pressure mechanism?',
 answer='External ventricular drainage with controlled CSF diversion',others=[
 ('Secondary decompressive craniectomy as the initial procedure','Decompression can be considered for selected refractory ICP patterns, but feasible CSF diversion directly addresses the demonstrated ventricular enlargement before assuming decompression is the next operation.'),
 ('Repeated lumbar CSF drainage as the initial procedure','Lumbar drainage has selected specialist indications, but ventricular obstruction or dangerous pressure gradients must be excluded; an external ventricular route directly treats the ventricular problem described.'),
 ('High-dose barbiturate coma before assessing CSF diversion','Barbiturates are an option for selected refractory pressure with hemodynamic monitoring, but do not directly relieve the demonstrated CSF accumulation when ventricular drainage is feasible.')])
revise(16,answer='No corticosteroid course for the traumatic brain injury itself',others=[
 ('High-dose methylprednisolone followed by an IV maintenance infusion','This strategy was tested in major TBI research and increased mortality; it should not be extrapolated from anti-inflammatory treatment of other conditions.'),
 ('Dexamethasone followed by taper according to the ICP response','Dexamethasone can reduce selected tumor-associated vasogenic edema, but benefit in that mechanism does not establish benefit for traumatic brain injury.'),
 ('Hydrocortisone titrated to the severity of traumatic cerebral edema','Hydrocortisone may be indicated for adrenal insufficiency or selected shock contexts, but traumatic edema itself is not a corticosteroid indication.')])
revise(17,answer='Protocolized temperature control within 32–37.5°C for at least 36 hours',others=[
 ('Protocolized temperature control within 32–37.5°C for 12 hours','The temperature range fits the 2025 AHA framework, but the recommended duration is at least 36 hours for patients remaining unresponsive to verbal commands.'),
 ('Protocolized cooling to 32–34°C for 24 hours in every unresponsive survivor','Hypothermia is one possible strategy, but the current AHA framework permits a wider range and does not establish universal superiority of deeper cooling.'),
 ('Fever treatment beginning only when temperature reaches 39°C','Temperature management should deliberately prevent uncontrolled fever; waiting for marked hyperthermia does not meet the specified post-arrest control strategy.')])
revise(18,answer='SpO2 90–98%, PaCO2 35–45 mmHg and MAP at least 65 mmHg',others=[
 ('SpO2 94–98%, PaCO2 25–30 mmHg and MAP at least 65 mmHg','The saturation and pressure targets are reasonable in some contexts, but routine marked hypocapnia reduces cerebral blood flow and is outside the AHA normocapnic target.'),
 ('SpO2 90–98%, PaCO2 45–55 mmHg and MAP at least 65 mmHg','The oxygen and pressure framework fits, but deliberate mild hypercapnia is not the general AHA target; use normocapnia unless the individual physiology requires modification.'),
 ('SpO2 90–98%, PaCO2 35–45 mmHg and MAP at least 55 mmHg','The oxygen and ventilation targets fit, but the pressure threshold is too low for the recommended minimum MAP of 65 mmHg after ROSC.')])
revise(19,answer='Obtain EEG and treat electroclinical or electrographic seizures when identified',others=[
 ('Give an antiseizure loading dose and assess success from disappearance of jerks','Treatment is appropriate for confirmed or strongly suspected seizures, but disappearance of motor activity does not establish electrographic cessation and some post-arrest jerks have no ictal correlate.'),
 ('Begin anesthetic suppression of the movements before EEG characterization','Anesthetic treatment is appropriate for refractory status, but routine suppression of myoclonus without an EEG correlate is not recommended and can obscure assessment.'),
 ('Classify the movements as nonictal myoclonus from bedside appearance','Some jerks are nonictal, but clinical appearance cannot reliably establish their relationship to cortical electrical activity; EEG is needed to characterize this presentation.')])

revise(20,answer='At least 72 hours after rewarming, with sedative and other confounders excluded',others=[
 ('At least 72 hours after ROSC, with sedative and other confounders excluded','This is the NCS timing framework when hypothermia has not been used; after hypothermic treatment, the interval is measured from rewarming.'),
 ('At least 48 hours after rewarming, with sedative and other confounders excluded','Some individual investigations have earlier validated acquisition times, but comprehensive prognostic synthesis after hypothermia is deferred for at least 72 hours after rewarming.'),
 ('At least 24 hours after sedative cessation, once temperature is normal','Drug clearance varies with exposure, organ function and temperature; a fixed 24-hour medication interval neither establishes clearance nor replaces the post-rewarming timing requirement.')])
revise(22,answer='Explain the uncertainty and consider extended observation aligned with the patient’s goals',others=[
 ('Recommend withdrawal because persistent coma itself indicates a poor neurologic outcome','Persistent coma warrants careful assessment, but in the absence of reliable predictors it does not establish irreversible unconsciousness or independently justify a confident neurologic prognosis.'),
 ('Recommend rehabilitation on the expectation of a favorable neurologic recovery','Rehabilitation planning may be appropriate, but absence of reliable poor-outcome predictors is not positive proof of favorable recovery and cannot justify that promise.'),
 ('Obtain a further NSE measurement as the decisive arbiter of recovery potential','Serial biomarkers can contribute to a broader assessment, but no universally reliable isolated NSE threshold resolves the stated multimodal uncertainty.')])
revise(24,answer='Investigate the cause and exclude intoxication before beginning formal death determination',others=[
 ('Obtain a cerebral perfusion study as the next step toward certification','Perfusion studies have defined ancillary indications after prerequisites are met; they do not replace establishing the cause of this unexplained coma.'),
 ('Begin apnea testing after normalizing oxygenation and blood pressure','Safe physiologic preparation is necessary, but it is insufficient while the permanent catastrophic mechanism remains unknown and a reversible toxic cause is plausible.'),
 ('Repeat the clinical examination after a six-hour observation interval','Repeated observation can document change, but elapsed time alone does not establish mechanism or exclude intoxication; further diagnostic evaluation remains necessary.')])
revise(25,answer='At least 24 hours after rewarming to at least 36°C',others=[
 ('Immediately after rewarming to at least 36°C','A current temperature at or above 36 is necessary, but the documented prior temperature at or below 35.5 triggers the additional 24-hour waiting requirement.'),
 ('At least six hours after rewarming to at least 36°C','Six hours is relevant to the adult repeat-testing minimum in Indian Form 10, but is not the post-hypothermia waiting interval specified in this US guideline.'),
 ('At least twelve hours after rewarming to at least 36°C','Twelve hours appears in other age-specific or protocol contexts, but does not satisfy the specified US 24-hour wait after this degree of hypothermia.')])
revise(26,answer='Assess prolonged clearance using exposure history, relevant levels and toxicology input',others=[
 ('Proceed after five standard half-lives if a routine urine drug screen is negative','Five half-lives may inform assessment under suitable conditions, but overdose, organ dysfunction and hypothermia can prolong clearance; routine screening also misses relevant exposures.'),
 ('Proceed after normalization of creatinine and a repeat absent examination','Renal recovery helps clearance of some drugs, but does not establish that all active parent drugs and metabolites have cleared or exclude other pharmacokinetic problems.'),
 ('Obtain a cerebral perfusion ancillary study to resolve the drug confounder','Ancillary testing does not provide an authorized shortcut around unresolved high sedative effects under this guideline; the pharmacologic prerequisite must be addressed.')])
revise(27,answer='Document recovery from neuromuscular blockade and correct significant metabolic abnormalities',others=[
 ('Confirm rocuronium discontinuation and proceed after one usual dosing interval','A dosing interval is not a measure of recovery; organ dysfunction and accumulated exposure can prolong paralysis and require objective exclusion.'),
 ('Confirm absent motor responses and use a perfusion study to resolve both confounders','Ancillary testing may have a role in selected uncorrectable metabolic abnormalities, but absent movement during possible residual paralysis is not interpretable evidence of central failure.'),
 ('Correct the metabolic abnormalities and use pupil size to exclude residual paralysis','Metabolic correction is necessary, but pupillary appearance does not establish neuromuscular transmission recovery; use the guideline’s appropriate examination or monitoring method.')])
revise(29,answer='Proceed without ancillary testing required solely for the untestable oculocephalic maneuver',others=[
 ('Obtain an ancillary study because every oculocephalic limitation requires one','Ancillary testing is required for specified unresolved components, but this guideline provides the stated exception when bilateral oculovestibular responses are assessable and absent and other requirements are met.'),
 ('Defer determination until the cervical injury permits oculocephalic testing','Delay may be necessary if required assessment remains unresolved, but the specific safe oculovestibular alternative makes cervical recovery unnecessary solely for this component.'),
 ('Repeat oculocephalic testing with cervical stabilization by an assistant','Manual stabilization does not make head rotation safe in the stated injury, and the guideline already supplies an appropriate alternative in this scenario.')])
revise(30,answer='Establish whether the movement is spinal; use ancillary assessment if its origin remains uncertain',others=[
 ('Classify the movement as a spinal reflex from its stereotyped appearance','Spinal reflexes can persist, but stereotypy alone does not resolve uncertainty about the origin; careful assessment and sometimes ancillary testing are required.'),
 ('Stop the determination because any withdrawal demonstrates brain-mediated activity','Brain-mediated responses preclude determination, but spinally generated limb movements can occur without brain function; their origin must be distinguished.'),
 ('Repeat the examination after sedation reduces the movement','Sedation would introduce a confounder rather than establish whether the original movement was spinal or brain-mediated; clarify the observed finding without masking it.')])
revise(31,answer='PaCO2 35–45 mmHg, pH 7.35–7.45 and preoxygenation to PaO2 above 200 mmHg',others=[
 ('PaCO2 25–30 mmHg, pH 7.45–7.50 and preoxygenation to PaO2 above 200 mmHg','Induced hypocapnia and alkalemia create an inappropriate starting point in a patient without chronic retention; the preparation specifies normal baseline arterial gases.'),
 ('PaCO2 35–45 mmHg, pH 7.35–7.45 and preoxygenation to PaO2 above 100 mmHg','The baseline gases fit, but the specified preoxygenation target is PaO2 above 200 after at least ten minutes of 100% oxygen, not merely above 100.'),
 ('PaCO2 45–55 mmHg, pH 7.30–7.35 and preoxygenation to PaO2 above 200 mmHg','A chronic hypercapnic patient requires an individualized baseline framework, but this patient has no chronic retention and should begin from the normal baseline range.')])
revise(33,answer='Stop, restore oxygenation and reassess a safe repeat or ancillary study',others=[
 ('Increase oxygen delivery and continue apnea until the scheduled blood gas','Oxygen-delivery methods can be optimized before a safe repeat, but progressive saturation below the guideline’s stopping limit requires interruption rather than extending the current test.'),
 ('End testing and use the most recent gas irrespective of its CO2 and pH','A gas obtained before rescue can be useful, but only an adequate endpoint establishes the result; the stem explicitly states that no adequate endpoint has been documented.'),
 ('Restore ventilation and restart immediately using the same oxygenation method','A repeat may be appropriate after stabilization, but the cause of desaturation and a safer technique must be addressed before exposing the patient to the same unresolved risk.')])

rows[12]['table']=(['Severe adult TBI parameter','BTF framework','Qualification'],[
 ['ICP treatment threshold','Above 22 mmHg','Interpret with examination and CT'],
 ['Usual CPP target','60–70 mmHg','Individualize for autoregulation and physiology'],
 ['CPP calculation','MAP minus ICP','Use consistent pressure-reference technique'],
 ['Higher CPP','Avoid aggressive routine pursuit above 70 mmHg','Pressors/fluids can increase respiratory complications']])
rows[31]['table']=(['2023 US apnea-test condition','Required finding'],[
 ['Observed respiratory effort','Absent'],['Arterial pH','Below 7.30'],
 ['Final PaCO2','At least 60 mmHg'],['Rise in PaCO2','At least 20 mmHg above appropriate baseline'],
 ['Suspected chronic retention, baseline unknown','Additional ancillary requirement despite otherwise compatible result']])
rows[46]['table']=(['State','Wakefulness','Behavioral evidence of awareness'],[
 ['Coma','Absent','Absent'],['Unresponsive wakefulness syndrome','Present','Not demonstrated'],
 ['Minimally conscious state','Present','Definite but limited; may fluctuate'],
 ['Emergence from minimally conscious state','Present','Functional communication or functional object use'],
 ['Classic locked-in syndrome','Present','Preserved; demonstrated through suitable communication']])

revise(34,answer='Complete safely assessable components and obtain an accepted ancillary study',others=[
 ('Repeat the clinical examination after six hours and certify if the remaining components are unchanged','Repeat assessment can establish consistency, but passage of time does not resolve the required brainstem components that facial injury prevents assessing.'),
 ('Use a technically adequate EEG as confirmation of the otherwise compatible examination','EEG can characterize cortical activity, but it is not accepted as an ancillary BD/DNC study under this guideline because it does not establish brainstem failure.'),
 ('Use an adequate apnea test to substitute for the inaccessible brainstem reflexes','Apnea testing assesses respiratory drive, not every required cranial reflex; a completed apnea component does not eliminate the ancillary indication created by the remaining untestable components.')])
revise(36,answer='It does not establish brainstem failure or replace the required assessment',others=[
 ('It can serve as the ancillary study when the apnea test is unsafe','This was accepted in some older frameworks, but the 2023 US guideline does not accept EEG for this purpose because it does not assess brainstem function.'),
 ('It becomes an accepted ancillary study if auditory evoked potentials are also absent','Adding tests of restricted pathways does not overcome the incomplete assessment of the entire brainstem; this combination is not accepted by the stated guideline.'),
 ('It can substitute for serial clinical assessment once hypothermia is excluded','Excluding hypothermia addresses one prerequisite, but does not convert a cortical electrical recording into the required comprehensive clinical or accepted ancillary determination.')])
revise(39,answer='Increase the interval according to the BSD experts and applicable pediatric protocol',others=[
 ('Use the adult six-hour minimum for children older than one year','The form explicitly includes pediatric age categories in its increased-interval qualification; the adult minimum cannot simply be extended to every child above one year.'),
 ('Use twelve hours for every child because Form 10 specifies that fixed pediatric interval','A twelve-hour interval appears in some clinical recommendations, but Form 10 itself does not specify one fixed numeric interval for all pediatric ages.'),
 ('Use twenty-four hours for every infant because Form 10 specifies that fixed infant interval','Longer age-specific observation may be recommended in a pediatric protocol, but the form’s own wording leaves increased intervals to the experts rather than stating this universal infant number.')])
revise(41,answer='Begin treatment-dose IV thiamine while investigating other causes',others=[
 ('Begin oral thiamine replacement with nutritional rehabilitation','Oral replacement is useful after acute therapy or in selected prevention settings, but suspected symptomatic Wernicke encephalopathy requires prompt parenteral treatment.'),
 ('Begin prevention-dose parenteral thiamine during alcohol-withdrawal treatment','Prevention is appropriate in at-risk patients without compatible neurologic disease, but this patient’s persistent confusion and ataxia warrant a treatment regimen.'),
 ('Obtain brain MRI and then select parenteral treatment according to the result','MRI can support diagnosis and identify alternatives, but sensitivity is insufficient to exclude Wernicke encephalopathy and imaging should not delay empirical treatment.')])
revise(44,answer='Withdraw dopamine blockers and provide intensive cooling, fluids and organ monitoring',others=[
 ('Withdraw dopamine blockers and prioritize enteral cyproheptadine treatment','Trigger withdrawal is appropriate, but cyproheptadine targets serotonin toxicity and is not the principal treatment for this dopamine-blockade-associated syndrome.'),
 ('Withdraw dopamine blockers and use bromocriptine before arranging intensive support','Bromocriptine may be considered as a specialist adjunct, but the severe hyperthermia and rhabdomyolysis require immediate systemic support rather than waiting for a drug response.'),
 ('Withdraw dopamine blockers and use antipyretics before deciding on active cooling','Withdrawal is necessary, but antipyretics do not adequately address muscle-related heat production; severe hyperthermia requires prompt active cooling and organ support.')])
revise(45,answer='Monitored lorazepam and urgent ECT assessment with systemic support',others=[
 ('Monitored lorazepam with ECT assessment deferred until a week-long trial is complete','Lorazepam is appropriate, but malignant physiology requires early ECT planning and escalation within 48–72 hours for inadequate response, or sooner with deterioration.'),
 ('High-dose antipsychotic treatment with intensive temperature control','Antipsychotics may be used for selected psychiatric syndromes, but can worsen catatonia and precipitate NMS; systemic cooling does not remove that risk.'),
 ('Immunotherapy first, with catatonia-specific treatment after antibody confirmation','Autoimmune encephalitis must be considered and may need parallel treatment, but antibody testing should not delay treatment of the immediately dangerous catatonic syndrome.')])
revise(46,others=[
 ('Critical illness myopathy','Myopathy can produce symmetric weakness and weaning failure, but sensory responses are generally preserved; reduced sensory amplitudes favor an axonal neuropathic component here.'),
 ('Acute inflammatory demyelinating polyneuropathy','AIDP can cause flaccid weakness and respiratory failure, but typically shows demyelinating electrophysiologic features; the stated axonal pattern after prolonged sepsis favors critical illness polyneuropathy.'),
 ('Myasthenic crisis','Myasthenia can impair ventilation and limb strength, but sensory nerve responses remain normal and neuromuscular transmission studies, rather than an axonal sensory pattern, support that diagnosis.')])

R['NALOXONE']=('Naloxone injection prescribing information: adult opioid overdose','https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=201fdedf-1736-4e52-9d7d-de14292547fd')
rows[1]['sections'].append(S('Dose and Repeat According to Response',
 '**Adult overdose labeling permits 0.4–2 mg IV initially**, repeated every 2–3 minutes if the respiratory response is inadequate. Product concentrations and routes differ; check the preparation.',
 'Continue assisted ventilation during dosing. Titrated smaller increments may be used in monitored settings to restore ventilation while limiting abrupt withdrawal; do not under-resuscitate severe respiratory failure.',
 'Recurrent depression requires repeat treatment and consideration of a monitored infusion because the opioid may outlast naloxone.'))
rows[1]['refs'].append('NALOXONE')
rows[10]['table']=(['Rescue option','Example ENLS dose','Principal monitoring'],[
 ['Mannitol','0.5–1 g/kg IV bolus','Volume status, BP, renal function and osmotic burden'],
 ['23.4% saline','0.5 mL/kg, maximum 30 mL','Sodium, chloride, renal function; concentration-specific access protocol'],
 ['After either bolus','Reassess before repeat treatment','ICP response, perfusion and definitive lesion plan']])
rows[34]['table']=(['Modality','2023 US ancillary status'],[
 ['Conventional four-vessel catheter angiography','Accepted'],['Radionuclide perfusion imaging','Accepted with appropriate technique'],
 ['Transcranial Doppler','Accepted in adults; not accepted in children'],['EEG, AEP or SEP','Not accepted'],
 ['CTA; MRI/MRA','Not accepted']])

revise(23,stem='After catastrophic brain injury, an adult remains unresponsive and ventilator-dependent with a very poor expected functional outcome. Corneal reflexes are reproducibly present. Which assessment is appropriate?',
 answer='Severe brain injury with preserved brainstem function; BD/DNC criteria are not met',others=[
 ('BD/DNC after a confirmatory cerebral perfusion study','Ancillary studies address specified unresolved components; a preserved brainstem reflex is evidence incompatible with the determination and cannot be overridden by imaging.'),
 ('BD/DNC after an apnea test documents no respiratory effort','Absent breathing is one necessary component, but it does not replace the requirement for absent brainstem reflexes; the corneal finding precludes determination.'),
 ('BD/DNC after a second examination confirms persistent coma','Persistent coma and a poor prognosis do not establish death; repeat assessment cannot convert preserved brainstem function into an absent reflex.')])
revise(40,answer='Continue the valid medical assessment and provide family support independently of donation authorization',others=[
 ('Defer certification while arranging another donation-counseling discussion','Further counseling may support an informed decision, but donation authorization does not determine whether clinically indicated death assessment should proceed.'),
 ('Use a non-donor certification pathway that omits repeat brainstem testing','The family’s retrieval preference does not create permission to omit the required examination or documentation in the stated certification process.'),
 ('Transfer responsibility for final certification to the donation coordinator','Coordinators may assist with logistics and communication, but the authorized medical board retains responsibility for the determination and its findings.')])
revise(48,stem='A patient has recurrent leg weakness and an appropriate structural evaluation. Repeated examination shows a convincing Hoover sign without new acute red flags. Which next management approach is most appropriate?',
 answer='Explain the positive clinical diagnosis and arrange functional motor rehabilitation',others=[
 ('Repeat brain and spinal MRI before discussing the diagnosis','Repeat imaging is warranted for new red flags or an inadequately evaluated localization, but indiscriminate repetition after an appropriate assessment delays a positive diagnosis and rehabilitation.'),
 ('Refer for psychological treatment without explaining the examination findings','Psychological care can help selected patients, but omitting the positive neurologic explanation leaves the diagnosis unsupported to the patient and neglects motor rehabilitation.'),
 ('Offer reassurance and discharge without a rehabilitation or follow-up plan','Reassurance is valuable, but functional weakness can cause substantial disability; a supported diagnosis, treatment pathway and appropriate follow-up are needed.')])
R['HYPO']=('JBDS: hospital management of hypoglycaemia in adults','https://www.diabetes.org.uk/sites/default/files/2023-03/JBDS%2001%20Hypo%20Guideline%20with%20qr%20code.pdf')
rows[2]['sections'].append(S('Use a Defined Glucose Rescue Regimen',
 '**A JBDS adult IV example supplies 20 g glucose:** 100 mL of 20% glucose or 200 mL of 10% glucose over 15 minutes. Follow the local emergency protocol and confirm IV patency.',
 'Recheck bedside glucose after 10 minutes and repeat treatment if still below 4.0 mmol/L, approximately 72 mg/dL. Do not give oral carbohydrate to an unconscious patient.',
 'If IV access is unavailable, 1 mg IM glucagon is an option, but malnutrition and depleted hepatic glycogen can limit the response. Continue monitoring and prevent recurrent hypoglycemia after rescue.'))
rows[2]['refs'].append('HYPO')
R['BTFTBI']=(R['BTFTBI'][0],'https://braintrauma.org/coma/guidelines/severe-tbi')

if __name__=='__main__':
    coverage=ROOT/'Neurology/14. Neurocritical Care, Coma, Brain Death & Miscellaneous Neurology.coverage.json'
    c=json.loads(coverage.read_text(encoding='utf-8'))
    assert len(rows)==c['plannedQuestions']==sum(s['questions'] for s in c['sections']),'Incomplete chapter; do not install'
    index=0
    for section in c['sections']:
        for decision in section['decisions']:
            assert rows[index]['topic']==section['section']
            rows[index]['coverageDecision']=decision
            index+=1
    save('Neurology',14,c['chapter'],rows,R,'Original source-based postgraduate synthesis; full Harrison subscription text not accessed; independent clinician review not claimed. Brain-death recommendations are labeled by jurisdiction.')
    c.update(status='authored_validated',authoredQuestions=len(rows))
    c['questionDecisions']=[dict(question=i+1,title=r['title'],decision=r['coverageDecision']) for i,r in enumerate(rows)]
    coverage.write_text(json.dumps(c,ensure_ascii=False,indent=2),encoding='utf-8')
