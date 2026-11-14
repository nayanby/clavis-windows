"""Original chapter 2: coherent progression from ischemia to hemorrhage and CVT."""
from qbank_json_chapters import question as Q, save

R={
 'AIS':('AHA/ASA acute ischemic stroke guideline, 2026','https://doi.org/10.1161/STR.0000000000000513'),
 'IVT':('Canadian Stroke Best Practices: Acute Ischemic Stroke Treatment','https://www.strokebestpractices.ca/recommendations/acute-stroke-management/acute-ischemic-stroke-treatment'),
 'BP':('Neurocritical Care Society ENLS: Acute Ischemic Stroke Protocol, version 6.0','https://www.neurocriticalcare.org/Portals/0/ENLS%205.0/ENLS%206.0/Protocol%20V6_0_Acute%20Ischemic%20Stroke.pdf'),
 'ED':('Canadian Stroke Best Practices: Emergency Department Evaluation and Management','https://www.strokebestpractices.ca/recommendations/acute-stroke-management/emergency-department-evaluation-and-management'),
 'CAR':('Canadian Stroke Best Practices: Extracranial Carotid Disease and Intracranial Atherosclerosis','https://www.strokebestpractices.ca/recommendations/secondary-prevention-of-stroke/management-of-extracranial-carotid-disease-and-intracranial-atherosclerosis'),
 'ICH':('AHA/ASA spontaneous intracerebral hemorrhage guideline, 2022','https://doi.org/10.1161/STR.0000000000000407'),
 'ICHC':('Canadian Stroke Best Practices: Emergency Management of Intracerebral Hemorrhage','https://www.strokebestpractices.ca/recommendations/management-of-intracerebral-hemorrhage/emergency-management-of-intracerebral-hemorrhage'),
 'SAH':('AHA/ASA aneurysmal subarachnoid hemorrhage guideline, 2023','https://doi.org/10.1161/STR.0000000000000436'),
 'NICE':('NICE NG228: Aneurysmal Subarachnoid Haemorrhage, recommendations, 2022','https://www.nice.org.uk/guidance/ng228/chapter/Recommendations'),
 'CVT':('Canadian Stroke Best Practice Recommendations: Cerebral Venous Thrombosis, 2024','https://doi.org/10.1017/cjn.2024.269'),
 'ELAN':('ELAN: Early versus Later Anticoagulation for Stroke with Atrial Fibrillation, NEJM 2023','https://doi.org/10.1056/NEJMoa2303048'),
 'SELECT':('SELECT2: Trial of Endovascular Thrombectomy for Large Ischemic Strokes, NEJM 2023','https://doi.org/10.1056/NEJMoa2214403'),
 'BAOCHE':('BAOCHE: Thrombectomy 6 to 24 Hours after Basilar-Artery Occlusion, NEJM 2022','https://doi.org/10.1056/NEJMoa2207576'),
 'WAKE':('WAKE-UP: MRI-Guided Thrombolysis for Stroke with Unknown Time of Onset, NEJM 2018','https://doi.org/10.1056/NEJMoa1804355'),
 'POINT':('POINT: Clopidogrel and Aspirin in Acute Ischemic Stroke and High-Risk TIA, NEJM 2018','https://doi.org/10.1056/NEJMoa1800410'),
 'LOCAL':('California Northstate University: Neurology Clerkship Handbook, localization appendix, 2024–2025','https://medicine.cnsu.edu/PDFs/clerkships/Neurology_Clerkship_Handbook_2_24_25.pdf'),
}
def S(heading,main,*children):return (heading,[(main,list(children))])
rows=[]
def add(*a,**kw):rows.append(Q(*a,**kw))

add('Ischemic stroke: definitions and mechanisms','Tissue-Based Diagnosis of TIA',
 'A patient has 25 minutes of left arm weakness that resolves completely. MRI shows a small acute diffusion-restricted right precentral lesion. Which diagnosis is most appropriate?',
 'Acute ischemic stroke with transient symptoms',[
 ('Transient ischemic attack','TIA requires transient ischemic dysfunction without acute infarction; complete clinical recovery does not negate the tissue evidence in this case.'),
 ('Migraine aura without infarction','Gradually spreading positive symptoms may suggest aura, but a matching acute vascular lesion and abrupt negative motor symptom support cerebral infarction.'),
 ('Focal seizure with postictal weakness','This is plausible after witnessed motor activity or impaired awareness, but the described episode and anatomically congruent infarct favor an ischemic event.')],
 [S('Diagnostic Definition','**Acute infarction** determines the tissue-based distinction between ischemic stroke and TIA, even when symptoms last less than an hour.',
    'Diffusion restriction with low ADC supports cytotoxic edema, but restricted diffusion is not uniquely ischemic; interpret the pattern, timing and clinical history together.',
    'Conversely, a normal early MRI does not exclude TIA or a small posterior-circulation infarct; diagnosis remains clinical when imaging is negative.'),
  S('Early Evaluation','**Transient recovery** does not remove the need for urgent vascular and cardiac assessment.',
    'Assess extracranial and intracranial vessels, ECG and rhythm monitoring, glucose and vascular risks. The mechanism guides antiplatelet treatment, anticoagulation or carotid intervention.',
    'Clinical risk scores supplement assessment but should not delay evaluation of recurrent events, carotid stenosis or atrial fibrillation.')],['ED','LOCAL'])

add('Ischemic stroke: definitions and mechanisms','Lacunar Versus Cortical Infarction',
 'Which finding most strongly argues against classifying a hemispheric stroke as a pure motor lacunar syndrome?',
 'Aphasia',[
 ('Weakness involving face, arm and leg','A small internal-capsular or pontine motor-pathway lesion can affect all three; this distribution alone is compatible with a lacunar syndrome.'),
 ('An extensor plantar response','This indicates corticospinal dysfunction and can occur in either lacunar or larger cortical-subcortical infarction, so it is not discriminatory.'),
 ('Absence of sensory loss','A pure motor lacunar syndrome has no required sensory deficit; sensory sparing therefore supports rather than contradicts the clinical label.')],
 [S('Clinical Syndromes','**Aphasia** is a cortical-network sign that is not part of the classic pure motor lacunar syndrome.',
    'Typical lacunar presentations include pure motor, pure sensory, sensorimotor, ataxic hemiparesis and dysarthria–clumsy hand syndromes. Small subcortical infarcts are often caused by penetrating-artery disease.',
    'Neglect, a homonymous field defect, gaze preference or aphasia suggests cortical or larger network involvement and should prompt assessment for large-artery or embolic disease.'),
  S('Etiological Limitations','**A clinical lacunar pattern** does not prove intrinsic small-vessel pathology.',
    'Embolism and branch atheromatous disease can produce small deep lesions. Use MRI distribution, vascular imaging and appropriate cardiac investigations to establish the likely mechanism.',
    'A strategically located thalamic lesion can disturb language, illustrating that a cortical-type sign identifies a network rather than proving a superficial cortical infarct.')],['LOCAL','ED'],style='direct')

add('Ischemic stroke: initial imaging','Imaging Before Reperfusion',
 'A woman develops disabling aphasia 70 minutes ago. Glucose is normal, and there is no trauma or anticoagulant use. Which imaging study should be obtained immediately to exclude intracranial bleeding?',
 'Noncontrast head CT',[
 ('CT perfusion alone','Perfusion maps estimate flow and tissue status but are not a substitute for the structural hemorrhage assessment; advanced perfusion is not routinely required in an otherwise eligible early-window patient.'),
 ('Gadolinium-enhanced brain MRI','MRI may be used in capable workflows, but contrast enhancement is unnecessary for emergency hemorrhage exclusion and can add delay in this straightforward early presentation.'),
 ('Carotid duplex ultrasonography','Useful for extracranial carotid stenosis, but it neither excludes intracranial hemorrhage nor adequately assesses intracranial occlusion for urgent reperfusion.')],
 [S('Immediate Imaging','**Noncontrast CT** rapidly identifies intracranial blood and major structural mimics, allowing an urgent reperfusion decision.',
    'Early ischemic CT may be normal; a normal scan does not refute an ischemic syndrome. Look for early loss of gray–white differentiation, sulcal effacement and a hyperdense artery.',
    'Rapid MRI with hemorrhage-sensitive sequences is an alternative when immediately available without delaying treatment; gadolinium is not a prerequisite.'),
  S('Vascular Assessment','**CTA of head and neck** identifies a treatable large-vessel occlusion and should be integrated into an efficient pathway.',
    'Do not delay otherwise eligible early-window intravenous thrombolysis merely to obtain perfusion imaging. Thrombectomy selection requires vascular occlusion assessment, while late or unknown-onset treatment may require additional tissue-based selection.',
    'In parallel establish last known well, deficit severity and disability, medications, blood pressure and glucose.')],['ED','IVT'])

add('Ischemic stroke: initial imaging','Diffusion–FLAIR Mismatch',
 'A patient wakes with disabling hemiparesis. MRI shows a matching DWI-bright, ADC-low lesion without marked corresponding FLAIR hyperintensity. What does this imaging pattern primarily support?',
 'An imaging-selected early tissue state despite unknown clock onset',[
 ('Proof that onset occurred within exactly 4.5 hours','Mismatch is a probabilistic tissue marker; its biological variability prevents exact retrospective determination of onset time in an individual.'),
 ('Proof that the affected tissue has fully reperfused','DWI–FLAIR mismatch compares tissue signal evolution, not vessel patency; arterial imaging is required to identify occlusion or reperfusion.'),
 ('A venous rather than arterial mechanism','Venous infarction may also alter diffusion, but mismatch itself does not establish a venous etiology; lesion distribution and venography answer that question.')],
 [S('MRI Selection','**DWI–FLAIR mismatch** can identify selected unknown-onset strokes for thrombolysis under an appropriate protocol.',
    'DWI detects water-motion restriction associated with acute cellular injury, whereas a clear FLAIR change commonly develops later. A small acute lesion with absent marked FLAIR change suggests relatively recent injury.',
    'WAKE-UP tested MRI-selected alteplase and demonstrated improved functional outcome; its entry criteria and bleeding risk still matter.'),
  S('Limits of Interpretation','**Tissue-based eligibility** supplements rather than replaces the full contraindication review.',
    'Exclude hemorrhage, major established injury and alternative diagnoses, and assess blood pressure, anticoagulants and other bleeding risks. A mismatch is not an instruction to lyse every patient who wakes with symptoms.',
    'Perfusion-core mismatch is a different construct: it estimates potentially salvageable tissue relative to an infarct core, rather than contrasting DWI with FLAIR evolution.')],['WAKE','IVT'])

add('Ischemic stroke: intravenous thrombolysis','Thrombolysis for Mild but Disabling Stroke',
 'A teacher presents 90 minutes after onset of severe isolated aphasia, NIHSS 3. CT excludes bleeding, and all other thrombolysis eligibility criteria are met. Which approach is best?',
 'Offer intravenous thrombolysis because the deficit is disabling',[
 ('Use the NIHSS score alone to exclude thrombolysis','NIHSS can underestimate the functional importance of language, hand or gait deficits. A low score is not synonymous with a nondisabling event.'),
 ('Wait for spontaneous improvement before deciding','Delaying an otherwise eligible disabling stroke sacrifices time-dependent benefit; improvement must remove the disabling deficit to change this reasoning.'),
 ('Choose aspirin–clopidogrel in place of reperfusion solely because NIHSS is 3','Short-course DAPT is appropriate for selected minor nondisabling noncardioembolic events, but is not an equivalent substitute for reperfusion in this disabling early-window stroke.')],
 [S('Disability Assessment','**Functional impact** determines whether a numerically mild deficit is disabling.',
    'Assess whether the persisting deficit would prevent basic daily activities or return to usual work. Aphasia, dominant-hand dysfunction and inability to walk may be disabling despite a low total NIHSS.',
    'The same score can describe very different clinical consequences. Document the actual deficit and its impact rather than relying on a numerical cut-off alone.'),
  S('Treatment Choice','**Eligible early-window patients** with disabling ischemic deficits should receive prompt thrombolytic consideration.',
    'The standard window is up to 4.5 hours from onset or last known well; selected unknown or later-onset patients require additional imaging criteria. Check bleeding risk and blood pressure before treatment.',
    'For genuinely nondisabling minor ischemic events, antiplatelet-based strategies often apply; that distinction is clinical and does not follow automatically from NIHSS ≤5.')],['IVT','AIS'])

add('Ischemic stroke: intravenous thrombolysis','Tenecteplase Stroke Dose',
 'A 72-kg patient with disabling ischemic stroke is selected for tenecteplase. Which regimen is appropriate for stroke?',
 '18 mg as a single intravenous bolus',[
 ('28.8 mg as a single intravenous bolus','This is 0.4 mg/kg, a higher stroke-trial dose without an acceptable benefit–risk advantage; it is not the recommended 0.25-mg/kg regimen.'),
 ('18 mg over a 60-minute intravenous infusion','The quantity corresponds to the stroke dose, but tenecteplase is given as a single bolus; a prolonged infusion confuses its administration with alteplase.'),
 ('64.8 mg with a bolus followed by a 60-minute infusion','This is an alteplase-style 0.9-mg/kg regimen. The agents are not dose interchangeable despite both activating plasminogen.')],
 [S('Dose and Administration','**Tenecteplase** for acute ischemic stroke is given at ==0.25 mg/kg, maximum 25 mg== as a single IV bolus.',
    'For 72 kg, 0.25 × 72 = 18 mg. Verify actual body weight, drug concentration and the stroke-specific order before preparing the dose.',
    'The 2026 AHA/ASA guideline accepts tenecteplase or alteplase in eligible adults within 4.5 hours. The 0.4-mg/kg tenecteplase dose is not recommended.'),
  S('Safety and Comparison','**Alteplase** uses 0.9 mg/kg, maximum 90 mg, with 10% as an initial bolus and the rest infused over 60 minutes.',
    'Both agents require hemorrhage exclusion, blood-pressure control and assessment of anticoagulants and other bleeding risks. The single-bolus convenience does not remove post-treatment neurological and pressure monitoring.',
    'Avoid confusing myocardial-infarction tenecteplase dosing with the smaller stroke regimen. Acute neurological worsening after either agent requires urgent hemorrhage evaluation.')],['AIS','IVT'],style='direct')

add('Ischemic stroke: intravenous thrombolysis','Blood Pressure Around Thrombolysis',
 'A patient otherwise eligible for IV thrombolysis has persistent BP 198/114 mmHg. Which plan best balances eligibility and hemorrhage risk?',
 'Lower BP below 185/110 before treatment and maintain below 180/105 for 24 hours',[
 ('Use 220/120 as the pretreatment threshold','This threshold concerns selected patients not undergoing reperfusion and without another hypertensive emergency; it is too permissive before thrombolysis.'),
 ('Lower systolic pressure to 110 before treatment and maintain below 120','Excessive reduction may compromise perfusion, and these targets are not the established thrombolysis thresholds; controlled lowering is the aim.'),
 ('Proceed at the current BP and lower it only if bleeding develops','Persistently elevated pretreatment pressure increases hemorrhagic risk; eligibility requires that pressure be controlled before the thrombolytic is administered.')],
 [S('Treatment Thresholds','**Before IV thrombolysis**, achieve BP below ==185/110 mmHg== using a titratable regimen; maintain below ==180/105 mmHg for 24 hours== after initiation.',
    'Suitable agents include IV labetalol or a nicardipine infusion according to local protocol. Recheck frequently and avoid abrupt fluctuations or hypotension.',
    'If pressure cannot be controlled and maintained safely, IV thrombolysis should not proceed on the assumption that later treatment will correct the risk.'),
  S('Why Context Matters','**Nonreperfusion stroke** has a different pressure strategy because elevated systemic pressure may sustain penumbral flow.',
    'Aortic dissection, acute coronary syndromes, pulmonary edema and other hypertensive emergencies create separate indications for treatment. Do not transfer an ICH pressure target to an ischemic stroke automatically.',
    'Intensive pressure reduction after successful reperfusion has not consistently improved outcomes and can be harmful at very low targets; follow the specific reperfusion protocol.')],['BP'])

add('Ischemic stroke: intravenous thrombolysis','Recent Direct Oral Anticoagulant Exposure',
 'A patient with disabling stroke took apixaban 3 hours ago. Renal function is normal. Noncontrast CT is negative and INR is 1.0; a calibrated drug assay is unavailable. What is the most appropriate interpretation?',
 'A normal INR does not establish thrombolysis safety after recent apixaban',[
 ('The INR confirms negligible apixaban effect','INR is standardized for vitamin K antagonists and may remain normal at clinically important apixaban concentrations; it cannot clear the patient for lysis.'),
 ('A normal aPTT would establish eligibility','Routine aPTT is also insensitive to therapeutic factor-Xa inhibitor activity; a normal value cannot exclude meaningful apixaban exposure.'),
 ('The oral anticoagulant excludes mechanical thrombectomy as well','Recent anticoagulant exposure affects bleeding-risk decisions for IV lysis but is not by itself a reason to deny thrombectomy for an eligible large-vessel occlusion.')],
 [S('Coagulation Interpretation','**Recent factor-Xa inhibitor ingestion** may leave substantial anticoagulant effect despite normal routine clotting tests.',
    'Timing, adherence, renal function and an appropriately calibrated drug-specific anti-Xa concentration are more relevant than INR. A normal INR is reassuring for neither apixaban nor rivaroxaban.',
    'Conventional protocols generally withhold IV thrombolysis after recent DOAC ingestion unless a validated testing pathway demonstrates sufficiently low activity; exact assay cut-offs vary by protocol and evidence is evolving.'),
  S('Reperfusion Pathway','**Urgent vessel imaging** remains important because thrombectomy may be available.',
    'Assess for a treatable large-vessel occlusion and transfer efficiently when needed. Reversal followed by thrombolysis is not a uniform strategy across DOACs; factor-Xa inhibitor reversal solely to facilitate lysis is not established routine care.',
    'For dabigatran, specialized protocols may consider idarucizumab before lysis, but that cannot be extrapolated to apixaban.')],['IVT','AIS'])

add('Ischemic stroke: thrombectomy','Bridging Thrombolysis Before Thrombectomy',
 'A previously independent patient arrives 2 hours after onset with an M1 occlusion. CT shows a small infarct, and both IV thrombolysis and thrombectomy criteria are met. Which strategy is most appropriate?',
 'Give eligible IV thrombolysis promptly while arranging immediate thrombectomy',[
 ('Wait for clinical response to IV thrombolysis before activating thrombectomy','Large-vessel recanalization is uncertain and waiting delays effective reperfusion; both pathways should proceed without a response-observation delay.'),
 ('Withhold IV thrombolysis because thrombectomy is planned','Direct-to-thrombectomy strategies have been studied, but planned EVT alone does not automatically remove standard IV treatment eligibility in this early presentation.'),
 ('Give IV thrombolysis and repeat angiography after several hours before transfer','This delays access to thrombectomy in a documented proximal occlusion. Transfer decisions should be based on immediate vessel imaging and clinical eligibility.')],
 [S('Parallel Reperfusion','**Bridging treatment** combines eligible intravenous thrombolysis with rapid endovascular therapy rather than making the treatments sequential alternatives.',
    'The IV drug can be started while the interventional team or transfer is activated. Do not wait for the infusion to finish or for neurological improvement before proceeding toward EVT.',
    'Conversely, thrombectomy should not be delayed by nonessential tests or prolonged attempts to overcome a clear thrombolysis contraindication.'),
  S('Eligibility Review','**A proximal occlusion** plus a disabling deficit warrants rapid specialist evaluation.',
    'Assess baseline function, time, established infarct burden, hemorrhage and vascular access. The strongest evidence concerns selected proximal anterior-circulation and basilar occlusions; treatment should follow current site-specific criteria.',
    'Patients ineligible for IV thrombolysis can still be eligible for EVT. A contraindication to one reperfusion method is not automatically a contraindication to the other.')],['IVT','AIS'])

add('Ischemic stroke: thrombectomy','Large-Core Thrombectomy Evidence',
 'A previously independent 66-year-old has an ICA terminus occlusion, NIHSS 21 and ASPECTS 4, 5 hours after last known well. There is no hemorrhage. Which statement is most appropriate?',
 'Low ASPECTS alone should not exclude urgent thrombectomy evaluation',[
 ('ASPECTS below 6 establishes futility for thrombectomy','Large-core trials have overturned an absolute exclusion based on this historical threshold; benefit depends on selection rather than that cut-off alone.'),
 ('Intravenous thrombolysis alone is the preferred reperfusion method at 5 hours without additional imaging selection','The patient is outside the standard 4.5-hour IV window; selected later IV treatment requires appropriate imaging, and a proximal occlusion still warrants EVT assessment.'),
 ('Thrombectomy benefits only patients with a core below 50 mL','SELECT2 included large cores, using ASPECTS 3–5 or core volume at least 50 mL; the stated restriction misrepresents the evidence.')],
 [S('Trial Findings','**SELECT2 and other large-core trials** demonstrated improved disability outcomes with EVT in selected patients previously considered poor candidates.',
    'SELECT2 studied proximal anterior-circulation occlusions within 24 hours and used ASPECTS 3–5 or a large imaging-derived core as qualifying features. Benefit does not mean that functional independence is common in every large-core subgroup.',
    'Evidence is strongest within the actual trial and guideline populations; extreme infarct volumes, major swelling, severe baseline disability and other exclusions require individualized assessment.'),
  S('Application','**ASPECTS is a severity estimate**, not a stand-alone declaration of irreversibility or futility.',
    'Immediately review imaging, time, baseline status and goals with the stroke intervention team. A modern pathway should not deny consultation solely because ASPECTS is 4.',
    'Communicate that thrombectomy may shift the distribution of disability even when the chance of complete independence remains limited.')],['SELECT','AIS'])

add('Ischemic stroke: thrombectomy','Basilar Artery Occlusion',
 'A previously independent patient becomes quadriparetic 10 hours after abrupt vertigo and diplopia. CTA shows basilar occlusion and imaging shows limited established posterior-circulation injury. What is the best next step?',
 'Urgent endovascular thrombectomy assessment',[
 ('Exclude intervention because more than 6 hours have elapsed','BAOCHE and subsequent guidance support treatment in selected basilar occlusions out to 24 hours; the older 6-hour boundary is not an absolute limit.'),
 ('Start a therapeutic heparin infusion as the sole reperfusion strategy','Anticoagulation does not reliably or promptly reopen an occluded basilar artery and should not replace evaluation for effective mechanical reperfusion.'),
 ('Observe because an initially low posterior-circulation NIHSS predicts recovery','Posterior-circulation disability may be underestimated by NIHSS, and current quadriparesis indicates a severe evolving syndrome requiring urgent treatment assessment.')],
 [S('Posterior-Circulation Reperfusion','**Basilar occlusion** can cause coma, quadriplegia, cranial nerve deficits or a locked-in syndrome.',
    'BAOCHE compared thrombectomy plus medical care with medical care alone in selected patients 6–24 hours after onset and found improved functional outcomes. Hemorrhagic and procedural risks remained.',
    'The 2026 AHA/ASA guideline recommends EVT within 24 hours for an appropriate severe basilar-occlusion population, including limited established injury and favorable baseline function.'),
  S('Selection and Monitoring','**CTA or MRA** confirms occlusion; clinical severity, time and posterior-circulation infarct burden guide selection.',
    'PC-ASPECTS evaluates posterior-fossa and related ischemic changes and is not interchangeable with anterior-circulation ASPECTS. Extensive bilateral brainstem injury substantially changes prognosis.',
    'Protect the airway and assess consciousness without delaying transfer. Preserved vertical eye movements and awareness in a quadriplegic patient may indicate a locked-in state rather than coma.')],['BAOCHE','AIS'])

add('Ischemic stroke: early complications','Post-Thrombolysis Antithrombotic Timing',
 'A clinically stable patient received alteplase 8 hours ago for ischemic stroke. There is no coronary stent or other competing urgent antithrombotic indication. When should routine aspirin usually be started?',
 'After the 24-hour follow-up scan excludes intracranial hemorrhage',[
 ('Immediately because baseline CT excluded bleeding','Baseline imaging precedes reperfusion and cannot exclude subsequent hemorrhagic transformation; immediate aspirin is not the usual post-lysis strategy.'),
 ('At 12 hours without repeat imaging if the deficit improves','Clinical improvement does not exclude asymptomatic hemorrhage. The usual 24-hour imaging safeguard is not replaced by an improving examination.'),
 ('At 7 days in every patient after thrombolysis','A universal week-long delay unnecessarily postpones prevention after a small uncomplicated infarct; longer delay may be appropriate for specific hemorrhagic complications.')],
 [S('Hemorrhagic Surveillance','**Routine antiplatelet therapy** is generally deferred until approximately 24 hours after IV thrombolysis and follow-up imaging has excluded hemorrhage.',
    'Avoid routine therapeutic anticoagulants during this interval as well. Specialized procedural or cardiac indications require individualized risk assessment rather than an automatic exception.',
    'New headache, vomiting, acute hypertension or neurological deterioration requires immediate examination and CT rather than waiting for scheduled surveillance imaging.'),
  S('Subsequent Prevention','**The stroke mechanism** determines the long-term antithrombotic approach.',
    'Antiplatelets suit most noncardioembolic events; atrial fibrillation generally requires anticoagulation once timing is judged safe. IV thrombolysis itself is not a reason for indefinite antiplatelet avoidance.',
    'If hemorrhagic transformation is present, distinguish small petechial changes from a space-occupying hematoma and individualize further therapy with the stroke team.')],['IVT','BP'])

add('Ischemic stroke: early complications','Malignant MCA Infarction',
 'A 49-year-old with a large MCA infarct develops declining consciousness and increasing midline shift at 30 hours despite initial supportive care. Which intervention warrants immediate discussion?',
 'Decompressive hemicraniectomy',[
 ('Corticosteroids for infarct-related edema','Steroids do not treat the cytotoxic swelling of ischemic infarction effectively and introduce hyperglycemic, infectious and gastrointestinal risks; tumor-related vasogenic edema is a different situation.'),
 ('Repeated mannitol as definitive treatment without surgical review','Hyperosmolar treatment can temporize raised pressure but does not replace time-sensitive decompression in an appropriate malignant hemispheric infarction.'),
 ('Delay surgery until a fixed dilated pupil appears','This waits for advanced herniation and can lose the window for benefit; declining consciousness from edema is already a major warning sign.')],
 [S('Pathophysiology','**Space-occupying hemispheric edema** can produce herniation during the first several days after a large infarction.',
    'Young patients may have less intracranial reserve, but age alone does not determine eligibility. Clinical decline, imaging burden and premorbid function should trigger early neurosurgical review.',
    'Exclude hemorrhagic transformation, seizures, hydrocephalus and metabolic causes when deterioration occurs; more than one mechanism may coexist.'),
  S('Surgical Decision','**Early hemicraniectomy with dural expansion**, commonly within 48 hours in trial-based pathways, reduces mortality in selected patients.',
    'Survival may include substantial disability, especially in older or more severely affected patients. Discuss likely functional states and the patient’s values with surrogates while arranging urgent care.',
    'Head positioning, airway care and short-term hyperosmolar rescue are bridges. The decision should precede irreversible herniation, not await it.')],['AIS','LOCAL'])

add('Ischemic stroke: secondary prevention','Short-Course Dual Antiplatelet Therapy',
 'A patient presents 8 hours after a nondisabling noncardioembolic minor stroke, NIHSS 2. CT excludes hemorrhage, no thrombolysis was given, and bleeding risk is low. Which regimen is best supported?',
 'Aspirin plus clopidogrel for 21 days, then antiplatelet monotherapy',[
 ('Aspirin plus clopidogrel indefinitely','The early prevention benefit is not a justification for chronic dual treatment in an uncomplicated minor stroke; cumulative major bleeding becomes a concern.'),
 ('Therapeutic rivaroxaban alone without a cardioembolic indication','Anticoagulation is appropriate for specific mechanisms such as AF, not empirically for this established noncardioembolic minor event.'),
 ('Aspirin plus prasugrel for 21 days','Prasugrel has important harm in patients with prior stroke or TIA and is not a substitute for the evidence-based aspirin–clopidogrel minor-stroke regimen.')],
 [S('Regimen','**Early short-course DAPT** reduces recurrent ischemic events in selected minor noncardioembolic stroke or high-risk TIA.',
    'Use aspirin loading, commonly 160–325 mg, and clopidogrel loading, 300–600 mg according to protocol, followed by aspirin 81 mg and clopidogrel 75 mg daily.',
    'For the usual uncomplicated minor-stroke indication, continue the combination for ==21 days==, then one antiplatelet. Screen for hemorrhage, bleeding risk and anticoagulation indications first.'),
  S('Duration and Exceptions','**CHANCE and POINT** established the early benefit; bleeding risk rises with longer exposure.',
    'Severe symptomatic intracranial stenosis or a recent stent can create a separate reason for a different duration. Such exceptions must be stated, rather than treating every stroke with prolonged DAPT.',
    'A low NIHSS with a disabling deficit still requires reperfusion consideration in the treatment window; DAPT eligibility does not automatically supersede that decision.')],['POINT','IVT'])

add('Ischemic stroke: secondary prevention','Symptomatic Carotid Stenosis',
 'A surgically fit 68-year-old man had a nondisabling right hemispheric ischemic stroke 4 days ago. CTA shows 80% NASCET right internal carotid stenosis with no complete occlusion. Which strategy is most appropriate?',
 'Early carotid endarterectomy plus intensive medical therapy',[
 ('Medical therapy alone because the symptoms have resolved','Resolution does not remove the early recurrence risk from a severe symptomatic ipsilateral lesion; a fit patient merits prompt revascularization assessment.'),
 ('Delay endarterectomy for 3 months after every minor stroke','For suitable stable nondisabling events, benefit is greatest with timely treatment, generally within 14 days; large infarction or hemorrhagic risk may justify delay individually.'),
 ('Carotid stenting as the preferred procedure for every patient','Stenting is useful when surgical anatomy or risk favors it, but procedure choice depends on age, anatomy and operator outcomes; it is not universally superior to endarterectomy.')],
 [S('Who Benefits','**Severe symptomatic ipsilateral carotid stenosis** is a treatable high-risk mechanism after TIA or nondisabling ischemic stroke.',
    'The 70–99% NASCET category has strong evidence for endarterectomy when perioperative risk is acceptable. Benefit for 50–69% stenosis is more selective and depends on patient features.',
    'Complete carotid occlusion is not managed with routine endarterectomy. Near-occlusion requires specialist interpretation rather than equating it automatically with conventional severe stenosis.'),
  S('Timing and Medical Therapy','**Early intervention**, ideally within 14 days in an appropriate stable patient, preserves the preventive benefit.',
    'Large disabling infarction, significant hemorrhagic transformation or unstable medical status can alter timing. Review brain imaging, event attribution and expected procedural risk before intervention.',
    'Antiplatelet therapy, intensive lipid lowering, pressure control, diabetes care and smoking cessation remain essential before and after revascularization; surgery is not a replacement for them.')],['CAR'])

add('Ischemic stroke: secondary prevention','Symptomatic Intracranial Atherosclerosis',
 'A patient has a recent nondisabling MCA-territory infarct caused by 80% intracranial M1 atherosclerotic stenosis. No prior intensive prevention has been attempted. What is the preferred initial strategy?',
 'Aggressive medical therapy with short-term DAPT and vascular risk control',[
 ('Immediate intracranial stenting as first-line treatment','Randomized evidence found important early procedural harm with initial stenting; recurrent events despite optimized treatment require specialist reassessment rather than automatic primary stenting.'),
 ('Warfarin instead of antiplatelet therapy for the stenosis','Warfarin is not superior for intracranial atherosclerotic disease and adds bleeding risk; use it only when another established indication exists.'),
 ('Extracranial–intracranial bypass as the default initial prevention','Bypass is not established routine first-line therapy for symptomatic intracranial atherosclerotic stenosis and exposes the patient to operative risk without the standard initial evidence base.')],
 [S('Medical Treatment','**Severe symptomatic intracranial stenosis** requires intensive antiplatelet and risk-factor treatment.',
    'The SAMMPRIS-style approach includes aspirin and clopidogrel for up to ==90 days== in suitable low-bleeding-risk patients, then a single agent, plus intensive lipid and blood-pressure management.',
    'This is a specific prolonged-DAPT indication and should not be generalized to an uncomplicated minor stroke, where the usual combination course is shorter.'),
  S('Procedural Evidence','**Initial medical management** is preferred over routine intracranial stenting.',
    'Confirm that the lesion is atherosclerotic and causally related; dissection, vasculitis and reversible vasoconstriction can mimic stenosis. Review recurrence mechanism and adherence before labeling medical failure.',
    'Selected refractory cases may need expert multidisciplinary consideration, but the existence of a technically accessible stenosis does not establish a benefit from immediate stenting.')],['CAR'])

add('Ischemic stroke: secondary prevention','Atrial Fibrillation and Anticoagulation Timing',
 'A patient with a small AF-associated ischemic infarct has no hemorrhagic transformation and stable follow-up imaging. Which statement best reflects the ELAN evidence?',
 'Selected minor strokes can start a DOAC within 48 hours after individualized assessment',[
 ('All AF-associated infarcts require a 14-day anticoagulation delay','ELAN tested earlier initiation based on infarct size; a fixed delay overlooks differences between small and major infarcts and their hemorrhagic risk.'),
 ('Immediate full-dose heparin bridging is required before every DOAC','DOACs have rapid onset and do not require routine heparin bridging; early therapeutic heparin is not the regimen tested by ELAN.'),
 ('ELAN established that early anticoagulation is safe despite any intracranial hematoma','Trial selection and hemorrhage exclusions limit extrapolation; a space-occupying hemorrhage or unstable bleeding changes the decision substantially.')],
 [S('Trial Schedule','**ELAN** randomized imaging-defined AF-related ischemic strokes to earlier or later DOAC initiation.',
    'The early group started within ==48 hours== for minor or moderate infarction and on ==day 6–7== for major infarction. The later schedule was day 3–4, 6–7 and 12–14 respectively.',
    'The study did not establish a statistically certain superiority of early treatment for its primary composite; it supports the feasibility of earlier treatment in selected patients.'),
  S('Individualization','**Infarct size, hemorrhagic transformation and clinical stability** matter more than a single calendar rule.',
    'Review renal function, drug interactions, bleeding risks and appropriate dose criteria. Mechanical valves and clinically significant rheumatic mitral stenosis are separate anticoagulant-selection contexts in which DOAC extrapolation is inappropriate.',
    'Do not combine long-term antiplatelets with anticoagulation without a separate indication such as a recent coronary intervention, because bleeding risk increases.')],['ELAN','AIS'])

add('Ischemic stroke: secondary prevention','Embolic Stroke of Undetermined Source',
 'A patient has a nonlacunar cortical infarct. Adequate evaluation identifies no AF, high-risk cardiac source or ≥50% relevant arterial stenosis. Which long-term strategy is most appropriate in the absence of another indication?',
 'Antiplatelet therapy with continued etiologic assessment',[
 ('Empirical rivaroxaban because the infarct appears embolic','NAVIGATE ESUS did not demonstrate superior prevention over aspirin and increased major bleeding; an embolic imaging pattern alone is insufficient for anticoagulation.'),
 ('Empirical warfarin with INR 2–3 for every cryptogenic cortical infarct','Warfarin is justified for defined indications, not simply failure to find a source. This adds treatment burden and bleeding risk without an established mechanism-specific benefit.'),
 ('Indefinite aspirin plus clopidogrel for all ESUS','Chronic DAPT is not the standard solution for an unidentified embolic source; short-course treatment has specific acute indications and must not become an indefinite default.')],
 [S('Diagnostic Category','**ESUS** is a nonlacunar infarct without a major-risk cardiac source or relevant high-grade proximal arterial stenosis after an adequate minimum evaluation.',
    'It is a heterogeneous category, not proof of occult AF. Potential mechanisms include intermittent AF, nonstenotic atheroma, aortic disease and paradoxical embolism.',
    'Repeated or prolonged rhythm monitoring can reveal AF that was not present on the initial ECG, particularly when the clinical profile suggests an atrial source.'),
  S('Evidence-Based Prevention','**Empirical anticoagulation** has not replaced antiplatelets for unselected ESUS.',
    'NAVIGATE ESUS compared rivaroxaban with aspirin and found no overall stroke-prevention advantage with more major bleeding. A later discovery of AF or another definite indication changes treatment.',
    'Continue lipid, pressure and lifestyle management and complete targeted investigations rather than interpreting “undetermined” as a reason for maximum antithrombotic intensity.')],['ED'],style='clinical_scenario')

add('Ischemic stroke: secondary prevention','Patent Foramen Ovale and Stroke',
 'A 34-year-old has an embolic-appearing ischemic stroke. Prolonged rhythm assessment and arterial studies reveal no alternative source. A large PFO shunt with atrial septal aneurysm is found. What is the most appropriate next step?',
 'Discuss PFO closure after multidisciplinary confirmation of a likely PFO-associated stroke',[
 ('Close every incidentally detected PFO after any stroke','PFO is common and may be incidental. Small-vessel disease, AF or another clear cause can make closure inappropriate despite a positive bubble study.'),
 ('Prescribe lifelong anticoagulation solely because a PFO exists','Anticoagulation is appropriate for a separate indication such as venous thromboembolism or AF; PFO alone does not universally mandate lifelong anticoagulation.'),
 ('Exclude closure because a leg ultrasound shows no current DVT','A negative ultrasound does not rule out a prior transient venous source; closure selection depends on the total causal assessment rather than documented persistent DVT.')],
 [S('Causal Assessment','**PFO-associated stroke** requires more than an anatomical shunt.',
    'The strongest trial evidence concerns selected adults approximately ==18–60 years== old with an embolic-appearing otherwise unexplained infarct. Large shunt and atrial septal aneurysm increase the likelihood that the PFO is relevant.',
    'Exclude dissection, atherosclerosis, AF, small-vessel disease and other plausible sources; the extent of rhythm monitoring should fit the patient’s age and risk profile.'),
  S('Shared Decision','**Percutaneous closure** can reduce recurrence in an appropriately selected group, but adds procedural and atrial-arrhythmia risks.',
    'Discuss anticipated benefit, device complications, post-procedure antiplatelet therapy and the possibility of newly detected AF. Causal tools can assist but do not replace clinical review.',
    'If an independent reason for long-term anticoagulation exists, the incremental benefit and strategy for closure require separate assessment rather than direct extrapolation from antiplatelet-control trials.')],['ED'])

add('Ischemic stroke: uncommon mechanisms','Cervical Artery Dissection',
 'A 38-year-old develops unilateral neck pain after minor neck strain, partial ipsilateral Horner syndrome, and a transient contralateral arm deficit. Which investigation best evaluates the suspected arterial cause urgently?',
 'CTA of the head and neck',[
 ('Noncontrast head CT alone','This is important for hemorrhage exclusion but may be normal in cervical dissection and does not adequately assess the cervical arterial lumen or wall.'),
 ('Routine carotid duplex as the only test','Ultrasound may identify accessible abnormalities but can miss distal cervical disease and intramural hematoma; a negative study does not reliably exclude the suspected lesion.'),
 ('Electrodiagnostic testing of the cervical sympathetic chain','Horner syndrome helps localization, but nerve testing does not identify the arterial lumen, mural hematoma or stroke mechanism and would delay appropriate vascular imaging.')],
 [S('Clinical Recognition','**Painful partial Horner syndrome** with focal cerebral ischemia raises concern for internal carotid dissection.',
    'Ipsilateral headache or neck pain and pulsatile tinnitus may occur. Anhidrosis may be absent because the relevant sudomotor fibers travel largely with the external carotid circulation.',
    'Vertebral dissection more often causes posterior neck or occipital pain with posterior-circulation ischemia; trauma may be minor or absent.'),
  S('Imaging and Treatment','**CTA or MRA** evaluates luminal narrowing, tapering, an intimal flap or pseudoaneurysm; fat-suppressed MRI can demonstrate mural hematoma.',
    'Acute stroke reperfusion is assessed by the usual relevant criteria rather than rejected solely because dissection is suspected. Subsequent antithrombotic choice is individualized; neither antiplatelets nor anticoagulation are uniformly superior in every patient.',
    'Intracranial extension or subarachnoid bleeding changes the risk assessment. Avoid reducing the decision to a blanket anticoagulation rule for all dissections.')],['LOCAL','ED'])

add('Intracerebral hemorrhage: cause and imaging','Cerebral Amyloid Angiopathy',
 'A 77-year-old has recurrent spontaneous lobar hemorrhages. SWI shows multiple strictly lobar microbleeds and cortical superficial siderosis, with no deep microbleeds. Which cause is most likely?',
 'Cerebral amyloid angiopathy',[
 ('Hypertensive arteriolosclerosis','This more characteristically causes deep hemorrhage or microbleeds involving basal ganglia, thalamus, pons or deep cerebellum; the exclusively lobar and superficial pattern favors CAA.'),
 ('A solitary cerebral cavernous malformation','A cavernoma can cause recurrent focal bleeding with a characteristic mixed-signal lesion, but does not best explain diffuse strictly lobar microbleeds and superficial siderosis.'),
 ('A ruptured saccular aneurysm','Aneurysmal bleeding usually centers in basal cisterns or fissures; recurrent lobar hematomas with a distributed cortical microbleed pattern suggest small-vessel amyloid disease instead.')],
 [S('Vascular Pathology','**CAA** involves amyloid deposition in cortical and leptomeningeal vessels and predisposes to lobar bleeding.',
    'Hemorrhagic markers include lobar ICH, strictly lobar cerebral microbleeds, convexity SAH and cortical superficial siderosis. Susceptibility-weighted or T2*-GRE MRI is important for detecting these markers.',
    'Deep hemorrhagic lesions suggest a different or mixed small-vessel process and affect the application of MRI-based CAA criteria.'),
  S('Diagnostic Framework','**Boston criteria version 2.0** allow a probable diagnosis without biopsy in a compatible patient aged at least 50 years.',
    'A qualifying pattern includes at least two strictly lobar hemorrhagic lesions, or one such lesion plus a specified white-matter marker, without deep hemorrhagic lesions or a better cause. The full clinical and imaging requirements must be checked.',
    'Recurrent hemorrhage risk influences antithrombotic decisions, but management still requires weighing the competing ischemic indication. Do not label all lobar hemorrhage in an older person CAA without investigating alternatives.')],['ICH'])

add('Intracerebral hemorrhage: cause and imaging','CTA Spot Sign',
 'CTA obtained shortly after a basal ganglia hemorrhage shows a small focus of contrast pooling within the hematoma, separate from an adjacent vessel. What is its principal prognostic implication?',
 'Increased risk of hematoma expansion',[
 ('Confirmation that an aneurysm caused the hemorrhage','An intrahaematomal spot represents contrast extravasation, not necessarily a structured aneurysmal sac communicating with an artery; the underlying cause requires separate evaluation.'),
 ('Evidence that the hematoma has stabilized','Contrast leakage suggests continuing bleeding risk, which is the opposite of a reliable stability marker.'),
 ('Proof of hemorrhagic brain metastasis','Tumors may bleed, but the acute spot sign is not a tumor-specific enhancement pattern; delayed structural imaging may be required when a mass is suspected.')],
 [S('Imaging Meaning','**A spot sign** is a marker of active or recent contrast extravasation within an acute hematoma.',
    'It predicts a higher probability of subsequent expansion and deterioration. Absence of a spot does not exclude expansion, and acquisition timing influences sensitivity.',
    'Other expansion predictors include early presentation, larger initial volume, anticoagulant exposure and certain noncontrast CT patterns; none replaces repeated clinical assessment.'),
  S('Clinical Response','**High-risk ICH** requires monitored stroke or neurocritical care, rapid correction of coagulopathy and smooth pressure control.',
    'Repeat CT is indicated for deterioration and is commonly used to assess early stability. A spot sign alone is not an instruction to give an unproven hemostatic treatment or operate on every supratentorial hematoma.',
    'CTA also evaluates macrovascular causes, especially in younger patients, unusual locations or unexplained hemorrhage. Interpret the extravasation marker separately from any identified aneurysm or arteriovenous malformation.')],['ICHC','ICH'])

add('Intracerebral hemorrhage: acute treatment','Blood Pressure in Mild-to-Moderate ICH',
 'A patient with a 12-mL spontaneous putaminal hemorrhage is alert and has SBP 182 mmHg. There is no planned immediate decompression. Under the AHA/ASA 2022 approach, which target is most appropriate?',
 'Aim for SBP about 140 and maintain approximately 130–150 mmHg',[
 ('Maintain SBP 180–200 to preserve the ischemic penumbra','This imports permissive-hypertension reasoning from nonreperfused ischemic stroke into a setting where ongoing bleeding and expansion are major concerns.'),
 ('Reduce SBP below 120 as quickly as possible','For the stated mild-to-moderate ICH population, excessive lowering, particularly below 130, can be harmful; lower is not automatically better.'),
 ('Allow SBP up to 220 until the 24-hour scan','In an otherwise suitable mild-to-moderate ICH with SBP 150–220, controlled early lowering is reasonable rather than deferring all intervention until the next day.')],
 [S('Target Population','**AHA/ASA 2022 guidance** supports smooth reduction toward ==140 mmHg== with maintenance around ==130–150 mmHg== in mild-to-moderate ICH presenting with SBP 150–220.',
    'Avoid treatment-associated SBP below 130 in this setting. Large or severe hemorrhage, pressure-dependent physiology and surgical decompression are populations in which the same intensive target is less well established.',
    'The recommendation is not a mandate to lower every hemorrhage to an identical value regardless of perfusion or comorbidity.'),
  S('Delivery and Monitoring','**Titratable intravenous agents** help achieve sustained control without large swings.',
    'Nicardipine or labetalol may be used according to local protocol with frequent pressure and neurological checks. Correct pain, agitation, urinary retention and other contributors while avoiding oversedation.',
    'Recheck renal function and watch for hypotension. A practical goal is stable controlled pressure, not an abrupt large reduction followed by rebound hypertension.')],['ICH','ICHC'])

add('Intracerebral hemorrhage: acute treatment','Warfarin-Associated ICH Reversal',
 'A patient taking warfarin has an acute intracerebral hemorrhage and INR 3.2. Four-factor PCC is immediately available. Which reversal strategy is preferred?',
 'Four-factor PCC plus intravenous vitamin K',[
 ('Intravenous vitamin K alone','Vitamin K restores factor synthesis over hours and cannot supply immediate clotting-factor replacement during an expanding life-threatening intracranial bleed.'),
 ('Fresh frozen plasma without vitamin K','Plasma supplies factors but is slower and more volume intensive than PCC when PCC is available; omitting vitamin K also permits rebound anticoagulation as infused factors decline.'),
 ('Protamine plus intravenous vitamin K','Protamine reverses heparin activity, not warfarin-related depletion of vitamin-K-dependent factors; it does not replace the urgent factor concentrate needed here.')],
 [S('Immediate Reversal','**Four-factor PCC** rapidly replaces factors II, VII, IX and X; **IV vitamin K** provides sustained reversal.',
    'Give vitamin K, commonly ==10 mg IV== by an appropriate controlled administration protocol, together with PCC. PCC dose follows the product, body weight and pretreatment INR.',
    'A typical labeled 4F-PCC schedule is 25 factor-IX units/kg for INR 2 to less than 4, 35 for INR 4–6 and 50 for INR above 6, subject to product-specific maximum doses.'),
  S('Verification and Alternatives','**Repeat INR and clinical imaging assessment** confirm whether reversal and hemorrhage control have been achieved.',
    'Stop warfarin immediately, identify the original anticoagulation indication and monitor for thrombotic complications. The future decision to restart anticoagulation is separate from emergency reversal.',
    'FFP is an alternative when PCC is unavailable, but thawing, infusion time and volume may delay correction. Vitamin K should accompany factor replacement to avoid later INR rebound.')],['ICH'])

add('Intracerebral hemorrhage: acute treatment','Dabigatran Reversal',
 'A patient taking dabigatran develops life-threatening intracerebral bleeding shortly after the latest dose. Which specific reversal regimen is most appropriate?',
 'Idarucizumab 5 g intravenously',[
 ('Andexanet alfa using the factor-Xa inhibitor schedule','Andexanet is designed for selected direct factor-Xa inhibitors and does not specifically bind dabigatran, which directly inhibits thrombin.'),
 ('Protamine 1 mg per 100 units of recent heparin exposure','This is a heparin-reversal approach and does not neutralize dabigatran; the units and dosing concept do not apply to the oral direct thrombin inhibitor.'),
 ('Vitamin K 10 mg intravenously','Vitamin K reverses impaired synthesis from warfarin, but dabigatran inhibits circulating thrombin directly; restoring vitamin-K-dependent synthesis does not remove its effect.')],
 [S('Specific Antidote','**Idarucizumab** is an antibody fragment that binds dabigatran and rapidly neutralizes its anticoagulant action.',
    'The usual dose is ==5 g IV==, supplied as two consecutive 2.5-g administrations according to the product instructions. Use is appropriate for life-threatening or uncontrolled bleeding or urgent procedures requiring reversal.',
    'This is drug-specific reversal; do not substitute an agent merely because it is labeled an anticoagulant antidote.'),
  S('Subsequent Assessment','**Renal function and rebound drug activity** are relevant because dabigatran is substantially renally cleared.',
    'Monitor clinical bleeding, repeat imaging and appropriate coagulation tests; thrombin-sensitive assays can help assess activity when available. Very large body stores or renal failure may produce later redistribution.',
    'Hemodialysis can remove dabigatran in selected circumstances when specific reversal is unavailable or insufficient, but it should not delay immediately available idarucizumab. Future anticoagulation timing requires a separate ischemic-versus-hemorrhagic risk review.')],['ICH'])

add('Intracerebral hemorrhage: acute treatment','Platelet Transfusion After Antiplatelet-Associated ICH',
 'A patient taking aspirin has spontaneous supratentorial ICH. Platelet count is normal, and emergency neurosurgery is not planned. What is the best approach to platelet transfusion?',
 'Do not give routine platelet transfusion solely for aspirin exposure',[
 ('Transfuse platelets to reverse aspirin in every spontaneous ICH','PATCH and guideline recommendations identify harm in the relevant nonsurgical setting; pharmacological platelet inhibition alone is not a universal transfusion indication.'),
 ('Transfuse only after a normal platelet-function result','A normal function result does not create a transfusion indication. Testing should not invert the evidence against routine transfusion in this context.'),
 ('Give platelets until the count exceeds 200 × 10⁹/L','An arbitrary supranormal count is not an established reversal target for a patient whose count is already normal and can expose the patient to transfusion harm.')],
 [S('Evidence','**Routine platelet transfusion** is potentially harmful in aspirin-associated spontaneous ICH when emergency surgery is not planned.',
    'PATCH compared platelet transfusion with standard care in antiplatelet-associated hemorrhage and found worse functional outcomes with transfusion. The result applies to the studied clinical context, not every bleeding disorder.',
    'A normal platelet count does not indicate normal platelet function, but impaired aspirin-related function still does not establish a net benefit from transfusion.'),
  S('Important Exceptions','**Emergency neurosurgery or substantial thrombocytopenia** requires a different hemostatic assessment.',
    'Selected aspirin-exposed patients requiring urgent surgery may be considered for platelets under specialist guidance. Low platelet counts from marrow disease or another cause need independent treatment thresholds.',
    'Desmopressin has uncertain outcome benefit in this setting and should not be described as a proven routine substitute. Address pressure control, coagulopathy from other drugs and hematoma surveillance simultaneously.')],['ICHC','ICH'])

add('Intracerebral hemorrhage: surgery','Cerebellar Hemorrhage With Hydrocephalus',
 'A patient with a 20-mL cerebellar hemorrhage becomes drowsy. CT shows fourth-ventricular compression, hydrocephalus and brainstem distortion. Which strategy is most appropriate?',
 'Urgent surgical hematoma evacuation with CSF diversion as indicated',[
 ('External ventricular drainage alone as the definitive plan','CSF drainage may be needed, but it does not remove posterior-fossa mass effect and can be inadequate or risky when the compressed compartment remains untreated.'),
 ('Medical observation until the hematoma reaches 30 mL','Current surgical indications include deterioration, brainstem compression, obstructive hydrocephalus or a cerebellar volume at least 15 mL; the proposed wait misses several existing indications.'),
 ('Corticosteroids followed by elective surgery after one week','Steroids do not reverse acute hematoma mass effect, and delay in a deteriorating patient risks fatal posterior-fossa compression.')],
 [S('Urgent Indications','**Posterior-fossa mass effect** can rapidly compromise the brainstem and CSF pathways.',
    'AHA/ASA 2022 supports immediate removal for cerebellar ICH with neurological deterioration, brainstem compression, obstructive hydrocephalus or volume ==at least 15 mL==, to reduce mortality.',
    'Any one of these features may be sufficient; this patient has several. Do not apply supratentorial-volume thresholds to the compact posterior fossa.'),
  S('Combined Management','**Evacuation and CSF management** are coordinated by neurosurgery with neurocritical support.',
    'Protect the airway, reverse anticoagulation and control pressure while preparing definitive treatment. EVD can treat hydrocephalus when indicated but is not a complete response to a space-occupying cerebellar hematoma.',
    'A neurologically stable patient with a small hemorrhage and no compression may be monitored closely, illustrating why location and physiology matter as much as a single size measurement.')],['ICH','ICHC'])

add('Intracerebral hemorrhage: prevention of complications','Venous Thromboembolism Prophylaxis in ICH',
 'A nonambulatory patient is admitted immediately after spontaneous ICH. There is no limb contraindication to compression. What should be started now for venous thrombosis prevention?',
 'Intermittent pneumatic compression',[
 ('Graduated compression stockings alone','Stockings alone have not shown adequate prophylactic effectiveness in this population and should not be considered equivalent to intermittent pneumatic compression.'),
 ('Immediate full-dose unfractionated heparin','Therapeutic anticoagulation is not prophylactic dosing and can worsen an acute unstable hematoma; a separate proven VTE indication requires its own risk assessment.'),
 ('No mechanical or pharmacologic prevention until walking resumes','Immobility raises VTE risk during the period before recovery; withholding feasible mechanical prevention loses an established early preventive measure.')],
 [S('Immediate Prevention','**Intermittent pneumatic compression** should begin on the day of ICH diagnosis in a suitable nonambulatory patient.',
    'Inspect skin and limb perfusion and ensure correct device use. Graduated stockings alone are not an equivalent evidence-based substitute.',
    'Early rehabilitation and mobilization plans should fit medical and neurological stability; indiscriminately forcing intense early activity is not the solution to VTE risk.'),
  S('Later Pharmacologic Prophylaxis','**Low-dose UFH or LMWH** may be considered after hemorrhage stability is assessed.',
    'AHA/ASA 2022 describes prophylactic initiation around ==24–48 hours== as potentially reasonable in selected patients; evidence certainty and international recommendations vary, so this is not an automatic instruction for every expanding bleed.',
    'Repeat imaging, coagulopathy, planned procedures and renal function influence timing and agent choice. A proven proximal DVT or PE is a treatment problem requiring a separate strategy, not merely a higher prophylactic dose.')],['ICH'])

add('Intracerebral hemorrhage: prevention of complications','Seizure Assessment After ICH',
 'A patient with lobar ICH has fluctuating consciousness unexplained by repeat CT, glucose or medications. No convulsion has been witnessed. Which next step is most appropriate?',
 'Continuous EEG monitoring for nonconvulsive seizures',[
 ('Attribute all fluctuation to the hematoma without further evaluation','Lobar injury increases seizure risk, and an unchanged CT does not exclude an electrical cause of unexplained altered awareness.'),
 ('Commit to indefinite antiseizure medication without attempting EEG assessment','Empirical urgent treatment may be appropriate if seizures are strongly suspected, but indefinite prophylaxis without evidence is not the standard response to an unexplained fluctuating examination.'),
 ('Use a normal 12-lead ECG to exclude nonconvulsive status','ECG assesses cardiac electrical activity, not cortical seizures. Rhythm assessment may identify another cause but cannot rule out nonconvulsive status epilepticus.')],
 [S('Electrical Causes of Deterioration','**Continuous EEG**, commonly for at least 24 hours when feasible, helps detect electrographic seizures in unexplained or fluctuating reduced consciousness.',
    'Nonconvulsive seizures may lack obvious motor signs. Simultaneously assess hemorrhage expansion, hydrocephalus, infection, metabolic abnormalities and sedating drugs.',
    'Treat clinical seizures and clinically relevant electrographic seizures; avoid assuming that every abnormal movement or EEG sharp wave establishes status epilepticus.'),
  S('Prophylaxis Versus Treatment','**Routine antiseizure prophylaxis without seizures** has not demonstrated a functional benefit in spontaneous ICH.',
    'The present question is about diagnosing a suspected complication, not screening every stable patient or prescribing indefinite medication to all lobar hemorrhages.',
    'If seizures are found, select an appropriate agent with attention to renal function, interactions and sedation, and reassess duration after the acute event according to seizure type and recurrence risk.')],['ICH','ICHC'])

add('Subarachnoid hemorrhage: diagnosis','Thunderclap Headache With a Late Negative CT',
 'A patient presents 18 hours after a sudden maximal-at-onset headache. Noncontrast CT is negative. Examination shows meningism but no papilledema or focal deficit, and lumbar puncture is judged safe. Under NICE NG228, what is the next diagnostic step?',
 'Lumbar puncture with assessment for CSF bilirubin',[
 ('Exclude SAH because the CT is negative','CT sensitivity declines with time, so a negative scan obtained beyond 6 hours cannot by itself dismiss a convincing clinical presentation.'),
 ('Diagnose migraine without further investigation','Migraine can cause severe headache, but an abrupt thunderclap onset with meningism requires exclusion of hemorrhage and other secondary causes first.'),
 ('Use a normal D-dimer to rule out aneurysmal bleeding','D-dimer is not a validated rule-out test for aneurysmal SAH; its use cannot replace time-appropriate imaging and CSF assessment.')],
 [S('Timing of Tests','**A negative CT obtained more than 6 hours after onset** requires further consideration when clinical suspicion persists.',
    'NICE NG228 advises considering lumbar puncture and allowing ==at least 12 hours from onset== for bilirubin formation. This patient is already beyond that interval.',
    'Where available, spectrophotometric bilirubin analysis supports interpretation. A decline in red-cell numbers across collection tubes alone does not securely exclude true SAH.'),
  S('Clinical Safeguards','**LP suitability** depends on examination, imaging, coagulation and the possibility of mass effect or obstructed CSF flow.',
    'Do not perform LP through an unsafe pressure gradient or uncorrected significant bleeding risk. Different health systems may use CT–CTA pathways after shared diagnostic assessment; the question specifies the NICE late-negative-CT pathway.',
    'Thunderclap differentials also include reversible cerebral vasoconstriction, dissection, CVT and pituitary apoplexy. Excluding aneurysmal hemorrhage does not automatically establish a primary headache.')],['NICE'])

add('Subarachnoid hemorrhage: diagnosis','Angiography After CT-Proven SAH',
 'CT shows diffuse basal cisternal SAH. CTA does not identify a source, but the distribution remains strongly suspicious for a ruptured aneurysm. What is the most appropriate next investigation?',
 'Catheter digital subtraction angiography',[
 ('Lumbar puncture to confirm that bleeding occurred','CT has already established subarachnoid blood. LP does not identify the bleeding aneurysm and adds risk without addressing the unresolved vascular question.'),
 ('Noncontrast CT only at six months','Delayed structural surveillance alone is insufficient when an acutely unsecured aneurysm remains plausible; an early missed source can rebleed.'),
 ('Carotid duplex to exclude an intracranial aneurysm','Duplex evaluates accessible cervical vessels but cannot exclude the intracranial arterial source suggested by basal cisternal blood.')],
 [S('Source Identification','**Catheter DSA** provides high-resolution vascular assessment when CTA is negative or inconclusive but an aneurysmal source remains suspected.',
    'Small aneurysms, complex anatomy, vasospasm or technical limitations may obscure an initial CTA finding. Blood distribution helps determine how strongly to pursue an occult source.',
    'A classic isolated perimesencephalic pattern has a different likelihood of aneurysm from diffuse basal cisternal or sylvian bleeding; protocols for repeat angiography therefore differ.'),
  S('Risk and Follow-Up','**Negative angiography** must be interpreted in the context of the hemorrhage pattern and image quality.',
    'Specialists may recommend repeat vascular imaging when the initial study is negative in a high-suspicion nonperimesencephalic case. DSA is invasive and carries procedural risks, so it should answer a defined diagnostic question.',
    'Continue monitored SAH care while the source is unresolved; do not treat a negative CTA as proof that rebleeding risk is absent.')],['SAH','NICE'])

add('Subarachnoid hemorrhage: securing the source','Timing of Ruptured Aneurysm Treatment',
 'A neurologically salvageable patient has aneurysmal SAH from an accessible ruptured anterior communicating artery aneurysm. What is the preferred general timing strategy for definitive aneurysm treatment?',
 'Secure the aneurysm as early as feasible, preferably within 24 hours',[
 ('Wait until the vasospasm period has ended in every patient','Leaving a ruptured aneurysm unsecured exposes the patient to early rebleeding; anticipated vasospasm is not a universal reason to defer treatment for weeks.'),
 ('Use nimodipine alone and reserve repair for a second bleed','Nimodipine improves outcomes related to delayed ischemia but does not mechanically secure an aneurysm; rebleeding can be catastrophic.'),
 ('Delay treatment until all subarachnoid blood has cleared on CT','Blood clearance is not a prerequisite for clipping or coiling and may take far longer than the high-risk rebleeding interval.')],
 [S('Early Rebleeding Prevention','**Definitive occlusion** of the ruptured aneurysm prevents further bleeding from that source.',
    'AHA/ASA 2023 favors treatment as early as feasible, preferably within ==24 hours==. Stabilization, imaging and access to an experienced neurovascular team should proceed promptly.',
    'Treatment modality depends on aneurysm anatomy, location, associated hematoma, patient factors and local expertise; neither coiling nor clipping is automatically best for every lesion.'),
  S('Before and After Occlusion','**Avoid hemodynamic extremes** and correct relevant coagulopathy while maintaining adequate cerebral perfusion.',
    'Pain control, antiemetic treatment, monitored care and management of hydrocephalus are important, but do not replace aneurysm occlusion. A single universal pre-occlusion pressure target is not supported for every patient.',
    'After the aneurysm is secured, continue surveillance for delayed cerebral ischemia, hydrocephalus, seizures and systemic complications; successful coiling does not conclude the acute illness.')],['SAH'])

add('Subarachnoid hemorrhage: medical treatment','Enteral Nimodipine',
 'Which regimen is standard for prevention of delayed cerebral ischemic complications after aneurysmal SAH in an adult who tolerates enteral treatment?',
 'Nimodipine 60 mg enterally every 4 hours for 21 days',[
 ('Nifedipine 30 mg enterally twice daily for 21 days','Another dihydropyridine is not interchangeable with nimodipine for the specific SAH outcome evidence; systemic antihypertensive activity does not establish the same indication.'),
 ('Nicardipine infusion as a direct replacement for enteral nimodipine','IV nicardipine can control pressure, but it is not an equivalent prophylactic regimen for the demonstrated outcome benefit of enteral nimodipine.'),
 ('Nimodipine 60 mg intravenously every 4 hours','The enteral preparation and dose must not be administered intravenously; route confusion can cause profound hypotension and fatal medication error.')],
 [S('Regimen and Benefit','**Enteral nimodipine**, usually ==60 mg every 4 hours for 21 days== from the hemorrhage, improves neurological outcome after aneurysmal SAH.',
    'Begin early when feasible. The clinical benefit should not be reduced to guaranteed prevention of angiographic vasospasm; macrovascular narrowing and delayed ischemic injury are related but not identical endpoints.',
    'Oral or feeding-tube administration is standard. Never inject an enteral capsule or solution; specialized IV formulations, where used, follow distinct specialist protocols and dosing.'),
  S('Monitoring','**Hypotension** can compromise cerebral perfusion and may require dose adjustment or a specialist-guided altered schedule.',
    'Monitor pressure and maintain euvolemia. Avoid unnecessary interruptions when treatment can be tolerated, but do not persist with a regimen causing dangerous hemodynamic instability.',
    'Nimodipine does not replace early aneurysm securing or assessment of new deficits. New weakness or confusion still requires evaluation for ischemia, rebleeding, hydrocephalus, seizures and metabolic complications.')],['SAH','NICE'],style='direct')

add('Subarachnoid hemorrhage: delayed complications','Delayed Cerebral Ischemia',
 'On day 7 after a secured aneurysmal SAH, a patient develops new aphasia. CT shows no new bleed or hydrocephalus; glucose and sodium are normal. Vascular studies support vasospasm. Which strategy is most appropriate?',
 'Maintain euvolemia and consider induced hypertension for symptomatic DCI with specialist monitoring',[
 ('Prophylactic hypervolemia with hemodilution in all SAH patients','Routine triple-H prophylaxis lacks established benefit and can cause pulmonary or cardiac complications; targeted treatment of symptomatic ischemia is a different intervention.'),
 ('Stop nimodipine and observe until the arterial narrowing resolves','Observation alone risks infarction. Nimodipine is generally continued when tolerated while the cause and treatment of neurological decline are addressed.'),
 ('Lower SBP below 100 to reduce the vasospasm','Hypotension can further reduce flow through narrowed vessels and is not a treatment for symptomatic delayed cerebral ischemia.')],
 [S('Diagnosis','**DCI** is clinical deterioration or infarction after SAH not explained by another cause.',
    'It commonly occurs during the days after the initial bleed, often around days 4–14. Exclude rebleeding, hydrocephalus, seizures, infection, hypoxemia and metabolic abnormalities before attributing a deficit to vasospasm.',
    'Transcranial Doppler, CTA and perfusion imaging can support assessment, but angiographic narrowing alone is not synonymous with clinically significant DCI.'),
  S('Treatment Escalation','**Euvolemia and adequate perfusion** are central; induced hypertension may help selected symptomatic patients once the aneurysm is secured.',
    'Assess cardiac function, pulmonary status and pressure response. Severe or refractory symptoms may prompt intra-arterial vasodilators or balloon angioplasty under an experienced team.',
    'Avoid routine prophylactic hemodynamic augmentation and hypervolemia. Continue enteral nimodipine as tolerated and evaluate the clinical response rather than treating a Doppler velocity in isolation.')],['SAH'])

add('Subarachnoid hemorrhage: delayed complications','Acute Hydrocephalus After SAH',
 'Twelve hours after aneurysmal SAH, a patient becomes progressively drowsy. CT shows enlarged ventricles and transependymal CSF flow without a larger hematoma. Which intervention directly addresses the likely cause?',
 'Urgent CSF diversion, commonly external ventricular drainage',[
 ('Increase nimodipine dosing to reverse ventricular enlargement','Nimodipine targets delayed ischemic outcome risk; it does not remove an acute CSF obstruction or drain the ventricles.'),
 ('Perform a large-volume lumbar puncture without assessing the CSF-flow pattern','Lumbar drainage can be appropriate in selected communicating patterns, but indiscriminate LP with obstructive hydrocephalus can create a dangerous pressure gradient.'),
 ('Defer drainage until the patient has persistent coma for 24 hours','Progressive symptomatic hydrocephalus requires urgent treatment; waiting for prolonged coma risks secondary injury and herniation.')],
 [S('Mechanism','**Subarachnoid or intraventricular blood** can obstruct CSF flow or impair resorption, causing acute hydrocephalus.',
    'Declining awareness, headache, vomiting and ventricular enlargement support the diagnosis. Acute neurological worsening after SAH also requires evaluation for rebleeding, seizures and other causes.',
    'Transependymal flow indicates pressure-related CSF movement into periventricular white matter and supports clinically important ventricular pressure.'),
  S('Drainage Strategy','**Urgent CSF diversion** is recommended for symptomatic acute hydrocephalus.',
    'EVD is commonly used, especially with obstructive patterns or intraventricular blood. Drainage rate and pressure are controlled by the neurocritical and neurosurgical team; an unsecured aneurysm requires coordinated management rather than automatic denial of necessary CSF diversion.',
    'Monitor for catheter infection, blockage and overdrainage. Persistent symptomatic communicating hydrocephalus after the acute period may need a permanent shunt after appropriate assessment.')],['SAH'])

add('Subarachnoid hemorrhage: delayed complications','Hyponatremia With Salt Loss After SAH',
 'After aneurysmal SAH, sodium falls to 122 mmol/L with high urine sodium, polyuria, negative fluid balance and evidence of intravascular depletion. Which strategy best fits the immediate clinical problem?',
 'Replace volume and sodium while closely monitoring sodium correction',[
 ('Restrict fluids as the sole treatment for every neurocritical hyponatremia','Fluid restriction can worsen hypovolemia and cerebral perfusion in this patient; SIADH and salt-loss states require distinction rather than a universal restriction rule.'),
 ('Give hypotonic maintenance fluid to match all urine output','Replacing sodium-rich losses with hypotonic fluid can aggravate hyponatremia; both the volume deficit and sodium content need assessment.'),
 ('Use a vasopressin antagonist before correcting volume depletion','Aquaresis can worsen intravascular depletion and cause rapid sodium shifts; it is not the appropriate initial response to this hypovolemic presentation.')],
 [S('Differential Diagnosis','**Natriuresis with hypovolemia** after SAH favors a salt-loss phenotype, although volume assessment is difficult and mixed mechanisms occur.',
    'SIADH can also produce concentrated urine and high urine sodium, so urine sodium alone does not distinguish it. Assess fluid balance, weight, hemodynamics, kidney function and alternative endocrine or drug causes.',
    'Maintaining cerebral perfusion and avoiding hypovolemia are especially important during the period of DCI risk.'),
  S('Sodium and Volume Treatment','**Isotonic replacement** addresses depletion; hypertonic saline is used when neurological symptoms or severity require it under a monitored protocol.',
    'Mineralocorticoids may help persistent natriuresis in selected patients. Monitor potassium, pressure, pulmonary status and urine output if used.',
    'Check sodium frequently and avoid overly rapid correction, with limits individualized to chronicity and osmotic-demylination risk. A sudden water diuresis can accelerate correction even after the initial sodium dose has stopped.')],['SAH'])

add('Cerebral venous thrombosis: diagnosis','Venography Despite Normal CT and D-Dimer',
 'A woman 2 weeks postpartum develops progressive headache, papilledema and a focal seizure. Noncontrast CT is unrevealing and D-dimer is normal. Which next investigation is most appropriate?',
 'CT venography or MRI with appropriate MR venography',[
 ('No further vascular imaging because D-dimer is normal','A normal D-dimer does not reliably exclude CVT, especially with subacute symptoms or limited thrombus burden; the clinical probability here is high.'),
 ('Carotid duplex alone','Cervical arterial ultrasound does not evaluate the intracranial venous sinuses or cortical veins responsible for the suspected syndrome.'),
 ('Lumbar puncture alone to confirm idiopathic intracranial hypertension','Raised pressure may be secondary to venous thrombosis, and the postpartum seizure raises concern for a structural vascular cause; exclude CVT before assigning an idiopathic label.')],
 [S('Diagnostic Suspicion','**Headache, raised intracranial pressure and seizures** in a prothrombotic setting should prompt venous imaging.',
    'CVT may cause a normal early noncontrast CT, hemorrhagic lesions outside arterial territories, or bilateral thalamic abnormalities with deep venous involvement. Neither a normal plain scan nor a normal D-dimer safely excludes it.',
    'Pregnancy and puerperium, estrogen exposure, infection, malignancy and thrombophilia are important contexts, but absence of a known risk factor does not rule it out.'),
  S('Imaging Choice','**Parenchymal imaging plus venography** demonstrates both thrombosis and its complications.',
    'CTV or contrast-enhanced MRV is suitable for major sinus assessment. MRI susceptibility sequences and appropriate venous techniques help evaluate suspected isolated cortical-vein disease.',
    'Flow artifacts and normal anatomic asymmetry can mimic occlusion. A negative or equivocal study must be reconciled with clinical probability and reviewed with neuroradiology when needed.')],['CVT'])

add('Cerebral venous thrombosis: acute treatment','Anticoagulation in Hemorrhagic Venous Infarction',
 'Venography confirms superior sagittal sinus thrombosis with a small stable hemorrhagic venous infarct. Platelet count and renal function are normal, and no emergency procedure is planned. Which initial treatment is preferred?',
 'Therapeutic-dose low-molecular-weight heparin',[
 ('Withhold all anticoagulation until the venous hemorrhage completely disappears','Hemorrhage from venous congestion is not the same as primary spontaneous ICH; delaying treatment can permit thrombus propagation and worsening congestion.'),
 ('Aspirin alone as equivalent antithrombotic treatment','Antiplatelets do not replace therapeutic anticoagulation for confirmed symptomatic CVT; the thrombotic mechanism and treatment evidence differ from noncardioembolic arterial stroke.'),
 ('Immediate catheter thrombolysis as routine first-line therapy','Endovascular therapy is considered selectively for deterioration or failure in expert centers; it is not the standard initial treatment for this stable case.')],
 [S('Why Anticoagulate','**Venous outflow obstruction** raises venous pressure and can produce edema, infarction and secondary hemorrhage.',
    'Therapeutic anticoagulation prevents extension and facilitates recanalization despite a small stable venous hemorrhage. A common enoxaparin treatment regimen is ==1 mg/kg subcutaneously every 12 hours== when renal function and other factors permit.',
    'LMWH is generally preferred in a stable patient. Intravenous UFH may be favored with severe renal dysfunction, an anticipated urgent procedure or a need for rapid reversibility.'),
  S('Exceptions and Monitoring','**Large expanding bleeding or imminent surgery** requires individualized specialist coordination.',
    'Assess platelets, kidney function, bleeding and neurological status. Suspected heparin-induced thrombocytopenia requires a nonheparin strategy rather than switching between UFH and LMWH.',
    'Treat seizures and intracranial-pressure complications concurrently. Anticoagulation is not a substitute for urgent decompression if malignant mass effect develops.')],['CVT'])

add('Cerebral venous thrombosis: follow-up','Duration of Anticoagulation After Provoked CVT',
 'A woman completes acute treatment for CVT associated with isolated estrogen-containing contraception. The estrogen is stopped, and no persistent thrombophilia or prior VTE is found. Which primary treatment duration best fits 2024 Canadian guidance?',
 'At least 3–6 months, followed by reassessment',[
 ('Stop after 7 days if the headache resolves','Symptom improvement does not establish adequate treatment of the cerebral and systemic thrombotic risk; a brief symptomatic course is insufficient.'),
 ('Continue lifelong in every estrogen-associated first episode','Indefinite therapy is considered for persistent major risks or recurrence; a removed major transient factor does not automatically justify lifelong anticoagulation.'),
 ('Stop only when every venous sinus is fully recanalized','Recanalization informs follow-up but is not the sole determinant of treatment duration; persistent imaging abnormality does not uniformly mandate indefinite anticoagulation.')],
 [S('Risk-Based Duration','**A major transient provoking factor** supports a finite course, commonly at least ==3–6 months== for a first CVT.',
    'A first unprovoked event commonly receives 6–12 months. Recurrent CVT or VTE, active cancer and high-risk thrombophilia may favor indefinite treatment after bleeding-risk assessment.',
    'These are clinical risk categories, not guarantees of identical treatment length for every patient. Patient preferences, bleeding, renal function and ongoing exposures matter.'),
  S('Follow-Up and Agent Choice','**Repeat venous imaging**, often around 3–6 months, provides a reference for recanalization and future symptoms.',
    'DOACs or warfarin may be appropriate after the acute phase in selected nonpregnant patients; triple-positive antiphospholipid syndrome favors a vitamin K antagonist. Pregnancy and breastfeeding require specific drug selection.',
    'Avoid resuming estrogen-containing contraception without specialist assessment. Persistent headache alone does not prove recurrent thrombosis, but new focal signs or seizures warrant urgent reevaluation.')],['CVT'])

add('Cerebral venous thrombosis: rescue treatment','Malignant Mass Effect in CVT',
 'Despite therapeutic anticoagulation, a patient with extensive CVT develops declining consciousness, a large edematous hemorrhagic venous infarct and midline shift with impending herniation. Which intervention is most immediately relevant?',
 'Urgent decompressive neurosurgical evaluation',[
 ('Continue anticoagulation alone and wait 48 hours for recanalization','Anticoagulation treats propagation but cannot reliably reverse a lethal pressure crisis quickly enough; impending herniation requires immediate rescue assessment.'),
 ('Escalate to dual antiplatelet therapy as the primary rescue','Platelet inhibition does not address the acute venous outflow obstruction or space-occupying lesion and adds bleeding risk without the required decompression.'),
 ('Perform lumbar puncture to remove a large CSF volume','A mass lesion with midline shift creates a dangerous pressure gradient; lumbar puncture can precipitate herniation and is not appropriate decompression here.')],
 [S('Life-Threatening Deterioration','**Malignant venous edema or hemorrhagic infarction** can cause herniation despite correct anticoagulant treatment.',
    'Declining consciousness, pupillary changes and progressive shift require emergency neurocritical and neurosurgical management. Secure airway and cerebral perfusion and use temporizing intracranial-pressure measures while definitive decisions are made.',
    'Decompressive hemicraniectomy can be lifesaving when a large parenchymal lesion produces malignant mass effect. The presence of venous hemorrhage is not by itself a reason to declare surgery futile.'),
  S('Other Rescue Options','**Endovascular venous treatment** may be considered for selected deteriorating patients at expert centers.',
    'It is not established routine first-line therapy, and the mechanism of deterioration matters: restoring flow and relieving an immediately dangerous compartment are different objectives.',
    'Anticoagulant interruption, reversal and restart around surgery require multidisciplinary coordination. Do not replace this individualized plan with either automatic permanent cessation or continued full-dose treatment through every procedure.')],['CVT'])

R.update({
 'NAV':('NAVIGATE ESUS: Rivaroxaban for Stroke Prevention after Embolic Stroke of Undetermined Source, NEJM 2018','https://doi.org/10.1056/NEJMoa1802686'),
 'PFO':('SCAI Guidelines for the Management of Patent Foramen Ovale, 2022','https://pmc.ncbi.nlm.nih.gov/articles/PMC11307505/'),
 'CAA':('Boston criteria version 2.0: multicentre MRI-neuropathology diagnostic accuracy study, 2022','https://pmc.ncbi.nlm.nih.gov/articles/PMC9389452/'),
 'PRA':('EMA: Praxbind product information','https://www.ema.europa.eu/en/documents/product-information/praxbind-epar-product-information_en.pdf'),
 'PATCH':('PATCH randomized trial: platelet transfusion after antiplatelet-associated ICH, Lancet 2016','https://pubmed.ncbi.nlm.nih.gov/27178479/'),
 'CVTDX':('Canadian Stroke Best Practices: Diagnosis and Initial Assessment of CVT, 2024','https://www.strokebestpractices.ca/recommendations/cerebral-venous-thrombosis/1-diagnosis-and-initial-clinical-assessment-of-symptomatic-cerebral-venous-thrombosis'),
 'CVTAC':('Canadian Stroke Best Practices: Acute Treatment of Symptomatic CVT, 2024','https://www.strokebestpractices.ca/recommendations/cerebral-venous-thrombosis/2-acute-treatment-of-symptomatic-cerebral-venous-thrombosis'),
 'CVTPOST':('Canadian Stroke Best Practices: Post-Acute Management of CVT, 2024','https://www.strokebestpractices.ca/recommendations/cerebral-venous-thrombosis/3-post-acute-management-of-cerebral-venous-thrombosis-and-person-centered-care'),
 'DAPT':('Canadian Stroke Best Practices: Antiplatelet Therapy for Ischemic Stroke and TIA','https://www.strokebestpractices.ca/recommendations/secondary-prevention-of-stroke/antiplatelet-therapy-for-ischemic-stroke-and-transient-ischemic-attack'),
 'NIMO':('SIAARTI consensus on aneurysmal SAH early management, part 2, 2022','https://doi.org/10.1186/s44158-022-00049-4'),
})
# Specific evidence accompanies the exact decision being tested.
for index,key in {14:'DAPT',18:'NAV',19:'PFO',21:'CAA',25:'PRA',26:'PATCH',33:'NIMO',37:'CVTDX',38:'CVTAC',39:'CVTPOST',40:'CVTAC'}.items():
    rows[index-1]['refs'].append(key)

rows[13]['table']=(['Indication','Common combination duration','After combination'],[
 ['Minor noncardioembolic stroke/high-risk TIA','Aspirin + clopidogrel for 21 days','Single antiplatelet'],
 ['Severe symptomatic intracranial stenosis','Selected patients: up to 90 days','Single antiplatelet plus intensive risk control'],
 ['AF-associated ischemic stroke','Not a replacement for anticoagulation','Anticoagulation when appropriate and safe']])
rows[23]['table']=(['Warfarin INR','Typical 4F-PCC factor-IX dose','Additional therapy'],[
 ['2 to <4','25 units/kg; product maximum 2500 units','IV vitamin K, commonly 10 mg'],
 ['4–6','35 units/kg; product maximum 3500 units','IV vitamin K, commonly 10 mg'],
 ['>6','50 units/kg; product maximum 5000 units','IV vitamin K, commonly 10 mg']])
rows[38]['table']=(['CVT risk context','Common primary course','Important qualification'],[
 ['Major transient factor removed','At least 3–6 months','Reassess recurrence and bleeding risk'],
 ['First unprovoked episode','6–12 months','Individualize subsequent prevention'],
 ['Recurrent VTE/CVT or major persistent risk','Consider indefinite','Review benefit–risk periodically']])

# Keep the alternatives within the same clinical decision, including timing and test scope.
rows[25]['others']=[
 ('Give one apheresis platelet unit on admission','This attempts to replace aspirin-inhibited platelets and may be considered in selected emergency-surgery contexts, but PATCH supports harm rather than benefit in the stated nonsurgical setting.'),
 ('Give platelets only if platelet-function testing confirms aspirin inhibition','Laboratory confirmation can describe drug effect, but has not established a net outcome benefit from platelet transfusion in a normal-count nonsurgical spontaneous ICH.'),
 ('Give platelets if the next scan shows expansion despite stable platelet count','Expansion requires urgent reassessment of pressure, coagulation and surgical options; it does not by itself reverse the evidence against aspirin-driven transfusion without a procedural or count-based indication.')]
rows[28]['others'][2]=('Obtain only a brief routine EEG and stop electrical monitoring if it is unrevealing','A short recording can identify ongoing seizures but may miss intermittent events. Persistent unexplained fluctuating consciousness supports extended recording even when an initial sample is negative.')
rows[29]['others'][2]=('Repeat noncontrast CT in 24 hours instead of CSF testing','A repeat scan can reassess new clinical deterioration, but waiting for another plain CT is not the NICE diagnostic completion strategy for a convincing late-presenting thunderclap with an initially negative scan.')
rows[30]['others']=[
 ('Time-of-flight MRA alone without further vascular assessment','MRA can be useful for selected aneurysm investigations, but a negative CTA with diffuse aneurysmal-pattern SAH warrants higher-resolution catheter evaluation rather than relying solely on another limited noninvasive test.'),
 ('Repeat CTA only after six weeks of observation','Delayed imaging can reveal an initially occult lesion, but deferring all immediate definitive vascular investigation leaves a potentially unsecured ruptured aneurysm during the high-risk early period.'),
 ('Contrast-enhanced structural brain MRI without angiography','MRI can investigate alternative causes of hemorrhage or an associated mass, but does not replace detailed arterial assessment for a suspected occult ruptured aneurysm in this bleeding pattern.')]
rows[31]['others']=[
 ('Plan treatment on day 3–7 after an observation period','Deferral may be necessary for individual medical or logistical reasons, but deliberate observation in a treatable salvageable patient leaves avoidable rebleeding exposure compared with the preferred early strategy.'),
 ('Plan treatment after day 14 when vasospasm risk has declined','Historically delayed strategies sought to avoid operating during vasospasm, but an unsecured ruptured aneurysm can rebleed while waiting; modern guidance favors early occlusion.'),
 ('Wait until follow-up CT shows complete clearance of subarachnoid blood','Blood clearance may help interpret some follow-up studies, but is not a requirement for aneurysm occlusion and could delay effective rebleeding prevention by weeks.')]
rows[32]['others'][2]=('Nimodipine 30 mg enterally every 4 hours for 7 days','Dose modification may be needed for hypotension, but a reduced total daily dose and a 7-day course are not the standard tolerated regimen through the main delayed-ischemia risk period.')
rows[36]['others'][1]=('Arterial CTA alone without a venous phase','Arterial imaging is appropriate for dissection or arterial occlusion, but a routine arterial-phase study does not reliably exclude sinus or cortical venous thrombosis; request dedicated venous assessment.')
R['DAPT']=(R['DAPT'][0],'https://www.strokebestpractices.ca/en/recommendations/secondary-prevention-of-stroke/anti-platelet-therapy-in-ischemic-stroke-and-tia/')

if __name__=='__main__':
    assert len(rows)==40,len(rows)
    save('Neurology',2,'02. Cerebrovascular Diseases',rows,R,
      'Original postgraduate educational synthesis. Decision-sensitive recommendations checked against cited AHA/ASA guidance (ischemic stroke 2026, ICH 2022, aneurysmal SAH 2023), Canadian CVT guidance 2024 and named primary trials. Some recommendations differ between societies; the question states the framework where necessary. Full Harrison’s subscription text was not accessed, and no independent clinician review is recorded.')
