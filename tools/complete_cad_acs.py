"""Complete the original CAD/ACS chapter without executing the eight-item seed writer."""
import ast, json, html, re, random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / 'build/topic-based-qbank-replacement'
seed = Path(__file__).with_name('create_cad_batch_01.py')
tree = ast.parse(seed.read_text(encoding='utf-8'))
for function in tree.body:
    if isinstance(function, ast.FunctionDef) and function.name in ('rich', 'render'):
        exec(compile(ast.Module(body=[function], type_ignores=[]), str(seed), 'exec'))
path = ROOT / 'drafts/Cardiology/01. Coronary Artery Disease and Acute Coronary Syndromes/cad-acs-draft.json'
bank = json.loads(path.read_text(encoding='utf-8'))
rows = bank['questions'][:8]
def ref(label, url): return dict(label=label, url=url)
ACS = ref('2025 ACC/AHA/ACEP/NAEMSP/SCAI Guideline for Acute Coronary Syndromes', 'https://doi.org/10.1016/j.jacc.2024.11.009')
ESC = ref('2023 ESC Guidelines for Acute Coronary Syndromes', 'https://doi.org/10.1093/eurheartj/ehad191')
CCD = ref('2023 AHA/ACC Multisociety Guideline for Chronic Coronary Disease', 'https://doi.org/10.1016/j.jacc.2023.04.003')
CCS = ref('2024 ESC Guidelines for Chronic Coronary Syndromes', 'https://doi.org/10.1093/eurheartj/ehae177')
MI = ref('Fourth Universal Definition of Myocardial Infarction (2018)', 'https://doi.org/10.1016/j.jacc.2018.08.1038')
MECH = ref('AHA Scientific Statement: Mechanical Complications of Acute Myocardial Infarction (2021)', 'https://doi.org/10.1161/CIR.0000000000000985')
LVT = ref('AHA Scientific Statement: Management of Patients at Risk for and With Left Ventricular Thrombus (2022)', 'https://doi.org/10.1161/CIR.0000000000001092')
SCAD = ref('AHA Scientific Statement: Spontaneous Coronary Artery Dissection (2018)', 'https://doi.org/10.1161/CIR.0000000000000564')
TTS = ref('International Expert Consensus Document on Takotsubo Syndrome, Part I (2018)', 'https://doi.org/10.1093/eurheartj/ehy076')
ISCHEMIA = ref('ISCHEMIA: Initial Invasive or Conservative Strategy for Stable Coronary Disease (2020)', 'https://doi.org/10.1056/NEJMoa1915922')

def q(stem, correct, distractors, title, principle, details, application, clinical, comparison, refs, style='direct'):
    """Each distractor is authored alongside its rationale before answer-position balancing."""
    rows.append(dict(question=stem, options=[correct]+[x[0] for x in distractors], correctIndex=0,
        questionStyle=style, explanationTeaching=dict(title=title, sections=[
            dict(heading='Diagnostic or treatment principle', bullets=[dict(text=principle, children=details)]),
            dict(heading='Applying the principle', bullets=[dict(text=application, children=clinical)])],
            tables=[dict(title='Key distinctions',headers=['Finding or strategy','Interpretation'],rows=comparison)],
            otherOptions=[dict(optionIndex=i+1,explanation=x[1]) for i,x in enumerate(distractors)]), references=refs))

q('Which finding is required, in addition to an acute rise or fall of cardiac troponin with at least one value above the 99th-percentile upper reference limit, to diagnose acute myocardial infarction?',
 'Evidence of acute myocardial ischemia',[
 ('Any abnormality on echocardiography','Chronic ventricular hypertrophy or an old regional abnormality does not establish acute ischemia.'),
 ('Angiographic coronary stenosis of at least 70% in every case','MI can occur with nonobstructive coronaries; an arbitrary stenosis threshold is not a universal requirement.'),
 ('Simultaneous elevation of creatine kinase-MB','An additional biomarker is not required when cardiac troponin is available and appropriate criteria are satisfied.')],
 'Myocardial injury is not synonymous with infarction',
 '**Acute myocardial injury becomes myocardial infarction only when there is evidence of acute ischemia.**',
 ['A troponin rise or fall identifies an acute process; a persistently elevated concentration can reflect chronic injury.', 'Qualifying ischemic evidence includes symptoms, new ischemic ECG changes, pathological Q waves, new ischemic-pattern loss of viable myocardium or a coronary thrombus in the appropriate setting.'],
 '**Interpret the biomarker together with the clinical syndrome.**',
 ['Sepsis, myocarditis, renal disease and tachyarrhythmia can produce myocardial injury without necessarily meeting MI criteria.', 'Neither a normal angiogram nor a negative CK-MB alone excludes MI when the relevant troponin and ischemia criteria are met.'],
 [['Acute troponin change without ischemia','Acute myocardial injury'],['Acute troponin change with ischemic evidence','Acute myocardial infarction']], [MI])
q('During severe gastrointestinal bleeding, a patient develops hemoglobin 5.6 g/dL, sustained sinus tachycardia, ischemic chest pain, new ST depression and a rise and fall in troponin. Angiography shows no acute coronary thrombus. Which classification best fits the infarction mechanism?',
 'Type 2 myocardial infarction caused by oxygen supply-demand imbalance',[
 ('Type 1 myocardial infarction caused by acute plaque thrombosis','The stem identifies a major extracoronary supply-demand trigger without evidence of acute atherothrombosis.'),
 ('Chronic myocardial injury because anemia is present','The dynamic biomarker pattern and new ischemic symptoms and ECG changes establish an acute ischemic event.'),
 ('Type 4a myocardial infarction related to PCI','Type 4a MI requires a PCI-related context, which is absent here.')],
 'Type 2 MI requires ischemia and a supply-demand mechanism',
 '**Severe anemia reduces oxygen delivery while tachycardia increases demand and shortens diastolic coronary perfusion time.**',
 ['An acute troponin change plus ischemic symptoms and ECG changes supports MI rather than isolated injury.', 'Type 2 MI reflects an ischemic imbalance without acute coronary atherothrombosis; background coronary disease may still be present.'],
 '**Address the precipitating imbalance and assess the underlying coronary context.**',
 ['Control bleeding, restore adequate oxygen delivery and manage hemodynamic stress according to the individual clinical situation.', 'A type 2 label does not automatically justify the same antithrombotic regimen as plaque-rupture ACS, especially during active bleeding.'],
 [['Type 1 MI','Acute coronary atherothrombosis'],['Type 2 MI','Ischemic supply-demand imbalance without acute atherothrombosis'],['Acute nonischemic injury','Dynamic troponin without ischemic evidence']], [MI], 'clinical_scenario')
q('An emergency department adopts a high-sensitivity troponin 0/1-hour rule-out algorithm. Which approach to the baseline concentration and change over one hour is correct?',
 'Use thresholds validated for the particular assay, together with symptoms, timing and ECG findings',[
 ('Apply the same numerical cutoffs to all manufacturers\' assays','Assays differ in analytic characteristics and validated concentration and delta thresholds.'),
 ('Rule out MI whenever the initial result is below the 99th percentile','Very early presentation can precede a detectable rise; one result is not universally sufficient.'),
 ('Use a fixed percentage rise alone regardless of the baseline value','Validated rapid algorithms commonly use assay-specific absolute changes and concentration cutoffs, not an isolated universal percentage.')],
 'High-sensitivity troponin algorithms are assay specific',
 '**A rapid troponin pathway is a validated clinical algorithm, not a universal numerical formula.**',
 ['Baseline concentrations and short-interval absolute changes depend on the assay used.', 'Early presenters, ongoing symptoms and patients in an observation zone require additional assessment and often further sampling.'],
 '**A biomarker rule-out must not override a diagnostic ischemic ECG or persistent clinical concern.**',
 ['Know the local assay, sampling interval and rule-in, rule-out and observation thresholds.', 'A rule-in result indicates a high probability of acute injury but still requires determining whether the mechanism is ischemic.'],
 [['Rule-out zone with reassuring clinical assessment','Consider discharge through a validated pathway'],['Observation zone or ongoing suspicion','Continue evaluation and serial testing']], [ESC])
q('A patient has ongoing ischemic chest pain, horizontal ST depression in V1-V3 and tall R waves in these leads. The standard ECG does not show anterior ST elevation. Which additional leads are most useful to detect the suspected occlusion pattern?',
 'Posterior leads V7-V9',[
 ('Right-sided V3R-V4R only','Right-sided leads assess right ventricular involvement, particularly with inferior infarction, rather than directly recording the posterior LV wall.'),
 ('A repeat tracing using only the limb leads','Limb leads may add information but do not replace direct posterior recordings for this pattern.'),
 ('Lewis leads to accentuate atrial activity','Lewis leads are intended to clarify atrial activity, not posterior myocardial injury.')],
 'Recognizing posterior coronary occlusion',
 '**Anterior ST depression can be the reciprocal image of posterior ST elevation.**',
 ['Tall anterior R waves and compatible ischemic symptoms strengthen suspicion of posterior infarction.', 'V7-V9 record posterior electrical activity and can reveal otherwise missed ST elevation; apply the appropriate lead-specific criteria.'],
 '**A nondiagnostic standard 12-lead tracing does not exclude an occlusive infarction.**',
 ['Obtain posterior leads promptly when the pattern is suggestive.', 'Continue urgent ACS assessment and reperfusion evaluation rather than waiting for a large troponin rise.'],
 [['V7-V9','Posterior LV assessment'],['V3R-V4R','Right ventricular assessment'],['Serial standard ECGs','Detect dynamic ischemic evolution']], [ESC,ACS], 'clinical_scenario')
q('A patient with inferior STEMI is hypotensive, has elevated jugular venous pressure and clear lung fields. Which additional ECG lead is most useful to support right ventricular infarction?',
 'V4R',[
 ('V8','V8 assesses the posterior LV wall and is not the preferred right ventricular lead.'),
 ('V9','V9 is another posterior lead, useful for posterior rather than isolated right ventricular assessment.'),
 ('A single repeat V6 recording','A lateral LV lead does not directly assess the suspected right ventricular injury.')],
 'Right ventricular infarction with inferior STEMI',
 '**Hypotension, systemic venous congestion and relatively clear lungs suggest impaired right ventricular output.**',
 ['Right-sided ST elevation, particularly in V4R, supports right ventricular involvement.', 'The pattern is commonly associated with a proximal right coronary culprit, although anatomy varies.'],
 '**Recognize preload sensitivity while pursuing urgent reperfusion.**',
 ['Avoid reflex nitrate administration in a hypotensive patient with suspected RV infarction.', 'Volume and hemodynamic management require reassessment: fluid is not unlimited therapy, especially if LV dysfunction coexists.'],
 [['V4R ST elevation','Supports RV infarction'],['Clear lungs with raised JVP and hypotension','Suggests predominant right-sided pump failure']], [ESC,ACS], 'clinical_scenario')
q('A patient has abrupt tearing chest pain radiating to the back, unequal arm pulses, a new early diastolic murmur and inferior ST elevation. What is the most appropriate immediate diagnostic priority before fibrinolysis?',
 'Urgently evaluate for acute aortic dissection with coronary involvement',[
 ('Assume uncomplicated inferior STEMI and give fibrinolysis immediately','Dissection can obstruct a coronary ostium; fibrinolysis can cause catastrophic bleeding in this setting.'),
 ('Exclude MI solely because the pain radiates to the back','The patient may have genuine coronary ischemia caused by the dissection; the pain pattern does not exclude myocardial involvement.'),
 ('Wait for a second troponin before considering aortic imaging','A biomarker delay does not address a potentially fatal aortic emergency with characteristic clinical signs.')],
 'Aortic dissection can produce an ischemic ECG',
 '**ST elevation does not exclude an acute aortic syndrome.**',
 ['A proximal dissection may compromise coronary perfusion and produce true myocardial ischemia.', 'Pulse asymmetry and new aortic regurgitation substantially change the interpretation of the chest-pain presentation.'],
 '**Suspected dissection is a contraindication to fibrinolysis.**',
 ['Obtain urgent definitive aortic imaging appropriate to stability and local availability, such as CT angiography or bedside transesophageal echocardiography.', 'Mobilize aortic surgical expertise when proximal dissection is suspected; avoid an automatic thrombolysis pathway.'],
 [['Uncomplicated occlusive STEMI','Prompt coronary reperfusion pathway'],['ST elevation with strong dissection features','Urgent aortic evaluation and surgical pathway']], [ESC,ACS], 'clinical_scenario')
q('A comfortable patient with ACS has an oxygen saturation of 97% on room air and no respiratory distress. Which oxygen strategy is appropriate?',
 'Do not give routine supplemental oxygen solely because ACS is present',[
 ('Give high-flow oxygen to all ACS patients for the first 24 hours','Routine oxygen in a nonhypoxemic patient has not shown the expected clinical benefit and is not recommended.'),
 ('Titrate oxygen to a saturation of 100% in every patient','A universal 100% target encourages unnecessary hyperoxia.'),
 ('Withhold oxygen even if clinically significant hypoxemia develops','The absence of an initial indication does not prevent later oxygen treatment when hypoxemia occurs.')],
 'Oxygen treats hypoxemia, not the ACS label',
 '**Routine oxygen is not recommended when arterial oxygen saturation is already adequate.**',
 ['Assess saturation and respiratory status rather than automatically prescribing oxygen for chest pain.', 'Supplemental oxygen is indicated in ACS with hypoxemia, commonly defined as saturation below 90%, while accounting for the clinical context.'],
 '**Reassess if pulmonary edema, shock or respiratory compromise develops.**',
 ['This patient has neither a low saturation nor respiratory distress.', 'Normal saturation does not replace assessment of perfusion, ventilation or the need for reperfusion.'],
 [['Normoxemia without distress','No routine oxygen'],['Hypoxemia or respiratory failure','Provide appropriate oxygen and respiratory support']], [ACS,ESC], 'clinical_scenario')
q('A patient with ischemic chest pain and blood pressure 138/82 mm Hg took tadalafil 18 hours earlier. Which antianginal decision is appropriate?',
 'Avoid nitrate administration because tadalafil was taken within the preceding 48 hours',[
 ('Give sublingual nitroglycerin because blood pressure is currently normal','A normal baseline pressure does not prevent a profound nitrate-PDE5 inhibitor interaction.'),
 ('Use intravenous nitroglycerin because it avoids the interaction','The interaction is pharmacodynamic and applies to intravenous as well as sublingual nitrates.'),
 ('Give a nitrate after a small fluid bolus to neutralize tadalafil','Volume loading does not neutralize PDE5 inhibition or make nitrate use safe.')],
 'Nitrates and PDE5 inhibition',
 '**Combining nitrates with recent PDE5 inhibition can cause severe hypotension through excess cyclic GMP signaling.**',
 ['Tadalafil has a longer interaction window: avoid nitrates within 48 hours of its use.', 'Sildenafil and vardenafil generally require at least a 24-hour separation; additional clinical factors may prolong drug effects.'],
 '**Medication history is part of the immediate chest-pain assessment.**',
 ['Select other appropriate ACS therapies while arranging definitive ischemia management.', 'Changing the nitrate route or giving fluid does not remove the interaction.'],
 [['Recent sildenafil or vardenafil','Avoid nitrates within 24 hours'],['Recent tadalafil','Avoid nitrates within 48 hours']], [ACS,ESC], 'clinical_scenario')
q('Which history is a contraindication to prasugrel in a patient undergoing PCI for ACS?',
 'Previous ischemic stroke or transient ischemic attack',[
 ('Previous uncomplicated PCI','Prior PCI alone is not a contraindication to prasugrel.'),
 ('Diabetes mellitus without bleeding','Diabetes increases ischemic risk and does not itself prohibit prasugrel.'),
 ('A remote myocardial infarction without cerebrovascular disease','A previous MI alone is not the contraindication being tested.')],
 'Prasugrel and cerebrovascular history',
 '**A prior stroke or TIA is a contraindication to prasugrel.**',
 ['This restriction reflects the unfavorable bleeding and net clinical risk in patients with cerebrovascular history.', 'Ask specifically about transient focal neurological events as well as a documented completed stroke.'],
 '**Choice of a P2Y12 inhibitor depends on more than antiplatelet potency.**',
 ['Alternative agents must be selected according to bleeding risk, concurrent anticoagulation, contraindications and treatment strategy.', 'Older age and low body weight also affect prasugrel selection and dosing, but do not replace the absolute cerebrovascular-history restriction.'],
 [['Previous stroke or TIA','Do not use prasugrel'],['Diabetes or previous PCI alone','Assess overall risk; not an automatic contraindication']], [ESC,ACS])
q('A patient with atrial fibrillation requiring long-term oral anticoagulation undergoes PCI for ACS. After the initial period of triple therapy, which strategy generally reduces bleeding while retaining antithrombotic protection under the 2025 ACC/AHA guideline?',
 'Discontinue aspirin after 1-4 weeks and continue the oral anticoagulant plus a P2Y12 inhibitor, preferably clopidogrel',[
 ('Continue aspirin, clopidogrel and full-dose anticoagulation indefinitely','Indefinite triple therapy exposes the patient to substantial bleeding and is not the default strategy.'),
 ('Stop anticoagulation and continue DAPT alone for the first year','DAPT does not replace anticoagulation for prevention of AF-related embolic stroke.'),
 ('Stop both antiplatelet agents immediately after PCI and use anticoagulation alone in every patient','Early stent-related protection ordinarily still requires antiplatelet therapy; this blanket approach ignores the immediate PCI context.')],
 'Combining anticoagulation with antiplatelets after PCI',
 '**Limit the duration of triple therapy when oral anticoagulation is required.**',
 ['The 2025 ACC/AHA ACS guideline recommends aspirin discontinuation after 1-4 weeks with continuation of an anticoagulant and P2Y12 inhibitor, preferably clopidogrel.', 'The exact early duration is individualized to bleeding risk, stent thrombosis risk and procedural features.'],
 '**Preserve the treatment for each underlying indication while reducing unnecessary overlap.**',
 ['Anticoagulation addresses AF-related embolic risk; the P2Y12 inhibitor supports protection after recent PCI.', 'Reassess the long-term regimen after the post-PCI period rather than assuming dual therapy must continue indefinitely.'],
 [['Initial selected post-PCI period','Short triple-therapy course'],['After early aspirin withdrawal','Anticoagulant plus P2Y12 inhibitor'],['Later stable phase','Reassess need for continuing antiplatelet therapy']], [ACS], 'clinical_scenario')
q('A patient with NSTE-ACS is scheduled for coronary angiography within 12 hours. Coronary anatomy is unknown. According to the 2023 ESC guideline, which statement about routine oral P2Y12 inhibitor pretreatment is correct?',
 'Routine pretreatment before the anatomy is known is not recommended when an early invasive strategy is planned',[
 ('Every patient must receive prasugrel before angiography','Routine pretreatment is not required in this setting, and prasugrel requires attention to anatomy, PCI intent and contraindications.'),
 ('Pretreatment is necessary because it cannot increase surgical bleeding','Platelet inhibition can increase bleeding and complicate urgent CABG if surgical anatomy is found.'),
 ('No P2Y12 inhibitor should be used even after PCI is selected','Avoiding routine pretreatment does not mean withholding indicated antiplatelet treatment once the invasive plan is established.')],
 'Timing P2Y12 treatment in early invasive NSTE-ACS',
 '**Pretreatment means giving a P2Y12 inhibitor before coronary anatomy is established.**',
 ['For NSTE-ACS with an early invasive strategy, routine pretreatment is not recommended by the ESC.', 'Potential bleeding, an alternative diagnosis and a possible need for CABG must be weighed against ischemic benefit.'],
 '**The timing recommendation is specific to the clinical pathway.**',
 ['Give appropriate antithrombotic treatment once anatomy and the revascularization strategy are established.', 'A delayed invasive strategy or a different ACS presentation requires its own risk assessment; do not universalize this rule to every patient.'],
 [['Unknown anatomy, early NSTE-ACS angiography','No routine P2Y12 pretreatment'],['PCI selected after angiography','Administer the appropriate P2Y12 regimen']], [ESC])
q('For ACS PCI performed by an experienced operator when either access site is technically suitable, which arterial access is preferred to reduce bleeding and vascular complications?',
 'Radial access',[
 ('Femoral access in every patient','Femoral access remains necessary in selected situations but is not the preferred routine approach when radial access is suitable.'),
 ('Brachial cutdown as the routine first choice','A surgical brachial approach is not the routine evidence-based default for ACS PCI.'),
 ('No arterial access until troponin normalizes','Waiting for troponin normalization is inappropriate when PCI is indicated.')],
 'Radial access in ACS intervention',
 '**Radial access is preferred for suitable ACS PCI because it reduces access-related harm.**',
 ['The radial artery is superficial and readily compressible, supporting bleeding reduction.', 'Guidelines also recognize favorable clinical outcomes, including a mortality benefit in the ACS evidence base.'],
 '**Access choice still depends on procedural needs and operator expertise.**',
 ['Large-bore support, failed radial access and other anatomical considerations may justify femoral access.', 'When femoral access is needed, careful puncture technique and bleeding-avoidance measures remain important.'],
 [['Routine suitable ACS PCI','Prefer radial access'],['Large-bore support or unsuitable radial anatomy','Select an appropriate alternative']], [ACS])
q('During PCI of a complex calcified left main bifurcation lesion, which adjunct can assess vessel size, stent expansion and edge complications more directly than angiography alone?',
 'Intravascular ultrasound or optical coherence tomography',[
 ('A repeat resting ECG alone','An ECG assesses electrical effects of ischemia but does not measure stent expansion or vessel dimensions.'),
 ('A higher angiographic contrast volume without intracoronary imaging','Additional contrast views may help anatomy but do not provide the same cross-sectional assessment.'),
 ('A postprocedural troponin measurement as a substitute for imaging','A biomarker may detect injury after it occurs but cannot guide immediate stent optimization.')],
 'Intracoronary imaging for complex PCI',
 '**IVUS and OCT provide cross-sectional information that complements the angiographic lumen silhouette.**',
 ['They can characterize lesion dimensions and identify underexpansion, malapposition and edge problems.', 'Imaging guidance is recommended for complex lesions in the 2025 ACS guideline; technique selection depends on anatomy and procedural constraints.'],
 '**Imaging guides how to perform PCI; coronary physiology helps decide whether a stenosis is flow limiting.**',
 ['IVUS is particularly useful in left main assessment and can be used without the contrast clearance required by conventional OCT.', 'Imaging does not remove the need for good lesion preparation, appropriate antithrombotic treatment or clinical judgment.'],
 [['IVUS/OCT','Lesion and stent morphology'],['FFR/iFR','Physiological significance of a stenosis'],['Angiography','Overall lumen and coronary anatomy']], [ACS], 'clinical_scenario')
q('Four days after an inferior MI, a patient develops abrupt pulmonary edema and hypotension. Echocardiography shows a flail mitral leaflet with severe eccentric mitral regurgitation. Which complication is most likely?',
 'Papillary muscle rupture',[
 ('Ventricular septal rupture','A septal defect causes a left-to-right shunt and often a harsh systolic murmur; it does not explain a flail mitral leaflet.'),
 ('Left ventricular free-wall rupture','Free-wall rupture causes hemopericardium and tamponade rather than a flail leaflet with acute severe MR.'),
 ('Chronic true left ventricular aneurysm','A true aneurysm is a remodeled scarred ventricular segment, not the immediate cause of acute flail-leaflet MR.')],
 'Acute severe mitral regurgitation after infarction',
 '**Papillary muscle rupture is a life-threatening mechanical complication of MI.**',
 ['The posteromedial papillary muscle is particularly vulnerable because its arterial supply is usually less redundant than that of the anterolateral muscle.', 'A sudden regurgitant load raises left atrial and pulmonary venous pressure before the atrium can adapt, causing flash pulmonary edema.'],
 '**Urgent echocardiographic diagnosis and surgical evaluation are essential.**',
 ['A murmur can be soft in profound shock; its absence does not exclude severe acute MR.', 'Stabilization and selected mechanical support bridge to definitive treatment rather than replace repair or replacement.'],
 [['Papillary muscle rupture','Acute severe MR, flail leaflet, pulmonary edema'],['Septal rupture','New intracardiac left-to-right shunt'],['Free-wall rupture','Hemopericardium and tamponade']], [MECH], 'clinical_scenario')
q('A patient develops shock and a new harsh holosystolic murmur several days after MI. Right heart catheterization demonstrates a substantial oxygen-saturation step-up from the right atrium to the right ventricle. Which complication is most likely?',
 'Postinfarction ventricular septal rupture',[
 ('Acute papillary muscle rupture','Acute MR raises left atrial pressure but does not create an oxygen step-up within the right ventricle.'),
 ('Isolated right ventricular infarction','RV infarction causes pump failure, not a new left-to-right ventricular shunt.'),
 ('Left ventricular free-wall rupture into the pericardium','This causes tamponade rather than oxygenated blood entering the right ventricle.')],
 'Hemodynamics of postinfarction septal rupture',
 '**A ventricular septal defect allows oxygenated LV blood to enter the RV.**',
 ['The RV oxygen-saturation step-up localizes a left-to-right shunt at ventricular level.', 'The resulting pulmonary overcirculation and reduced forward systemic output can rapidly cause biventricular failure and shock.'],
 '**Confirm the defect with urgent echocardiography and involve a multidisciplinary mechanical-complication team.**',
 ['Defect size, shunt magnitude, tissue quality and shock severity influence repair timing and support.', 'Do not treat this as uncomplicated post-MI LV dysfunction or defer structural assessment because a culprit artery has already been opened.'],
 [['RA-to-RV oxygen step-up','Ventricular-level left-to-right shunt'],['Large left atrial V waves without RV step-up','Consider acute MR'],['Pericardial blood with tamponade','Consider free-wall rupture']], [MECH], 'clinical_scenario')
q('A patient collapses with pulseless electrical activity three days after MI. Bedside ultrasound shows a new large pericardial effusion with echogenic material and tamponade physiology. Which complication is most likely?',
 'Left ventricular free-wall rupture',[
 ('Acute ventricular septal rupture','A septal rupture produces an intracardiac shunt; it does not primarily cause a bloody pericardial effusion.'),
 ('Papillary muscle rupture','Papillary muscle rupture causes acute MR and pulmonary edema rather than hemopericardium.'),
 ('A stable chronic true ventricular aneurysm','The sudden hemopericardium and arrest suggest acute rupture, not stable scar remodeling.')],
 'Post-MI hemopericardium and tamponade',
 '**Free-wall rupture may cause rapid bleeding into the pericardial space and obstructive circulatory collapse.**',
 ['Pulseless electrical activity is a characteristic catastrophic presentation.', 'Echogenic pericardial material can represent clot; an effusion need not appear uniformly anechoic.'],
 '**This is an immediate resuscitation and cardiothoracic surgical emergency.**',
 ['Urgent bedside imaging can identify a potentially correctable mechanical cause during collapse.', 'Pericardial drainage, when used, is a carefully managed temporizing measure while definitive repair is arranged, not a reason to delay surgery.'],
 [['Free-wall rupture','Hemopericardium, tamponade, possible PEA'],['Papillary rupture','Acute severe MR'],['Septal rupture','Left-to-right ventricular shunt']], [MECH], 'clinical_scenario')
q('Which imaging feature most strongly favors a postinfarction left ventricular pseudoaneurysm over a true ventricular aneurysm?',
 'A contained ventricular rupture communicating through a relatively narrow neck',[
 ('A broad-based outpouching composed of scarred ventricular wall','This is more characteristic of a true aneurysm containing remodeled myocardial wall.'),
 ('Persistent ST elevation alone','Persistent ST elevation may accompany a true aneurysm and does not establish a pseudoaneurysm.'),
 ('Apical dyskinesia without information about wall continuity','Dyskinesia is not sufficient to distinguish the two structural entities.')],
 'True aneurysm versus pseudoaneurysm',
 '**A pseudoaneurysm is a contained rupture rather than a complete myocardial-wall outpouching.**',
 ['Its wall is formed largely by pericardium and thrombus rather than intact ventricular myocardium.', 'A narrow communication supports the diagnosis, but neck geometry alone should not replace multimodality assessment.'],
 '**Distinguishing the lesions changes urgency because a pseudoaneurysm carries rupture risk.**',
 ['Echocardiography, CT or CMR can define the neck, wall continuity and surrounding structures.', 'Management requires prompt specialist assessment; a benign interpretation based only on chronicity can be unsafe.'],
 [['True aneurysm','Scarred ventricular wall, usually broad connection'],['Pseudoaneurysm','Contained rupture, often narrow connection']], [MECH])
q('Two days after a transmural MI, a stable patient develops sharp pain worse with inspiration and improved by sitting forward. A pericardial friction rub is heard. Which explanation is most likely?',
 'Early infarct-associated pericarditis',[
 ('Dressler syndrome with its usual delayed immune-mediated presentation','Dressler syndrome classically appears after a latent interval of weeks rather than the immediate early postinfarction period.'),
 ('Reinfarction established solely by the pain description','Recurrent infarction requires assessment for new ischemia; positional pleuritic pain and a rub favor pericardial inflammation.'),
 ('Acute papillary muscle rupture','Papillary rupture presents with acute MR, pulmonary edema and often shock, not a stable friction-rub syndrome.')],
 'Early postinfarction pericardial inflammation',
 '**Inflammation overlying a transmural infarct can cause pericarditis within the first several days.**',
 ['Pleuritic positional pain and a friction rub favor pericardial involvement.', 'Recurrent ischemia, pulmonary embolism and mechanical complications remain important alternatives if the clinical course is atypical.'],
 '**Timing helps separate early infarct-associated inflammation from delayed post-cardiac injury syndrome.**',
 ['Use ECG, serial biomarkers and echocardiography as appropriate to assess competing diagnoses and an effusion.', 'Do not diagnose reinfarction from a single persistently elevated troponin after a recent MI.'],
 [['First days after transmural MI','Early infarct-associated pericarditis'],['Delayed inflammatory syndrome after a latent interval','Post-cardiac injury syndrome, including Dressler syndrome']], [ESC], 'clinical_scenario')
q('After a large anterior MI, contrast echocardiography shows an equivocal apical mass. Clinical concern for LV thrombus remains. Which investigation is most appropriate to clarify the finding?',
 'Cardiac magnetic resonance imaging with an appropriate thrombus-detection protocol',[
 ('A normal ECG as sufficient exclusion of thrombus','Electrical findings cannot exclude an intracavitary clot.'),
 ('Exercise ECG to distinguish thrombus from myocardium','Exercise testing assesses inducible ischemia and does not characterize an apical mass.'),
 ('Repeated troponin testing alone','Troponin describes myocardial injury, not whether an intracavitary thrombus is present.')],
 'CMR for uncertain LV thrombus',
 '**CMR is particularly useful when echocardiography remains nondiagnostic despite an ultrasound-enhancing agent.**',
 ['Akinetic infarcted myocardium produces stasis and a substrate for thrombus formation.', 'CMR offers tissue characterization and greater sensitivity for LV thrombus than routine echocardiography.'],
 '**Establish the diagnosis before assuming that every apical finding is clot.**',
 ['Confirmed thrombus affects anticoagulation decisions and requires balancing embolic risk against bleeding, particularly during antiplatelet therapy.', 'CMR is not mandatory for every post-MI patient; it is targeted here to a persisting diagnostic uncertainty.'],
 [['Definite thrombus on adequate imaging','Plan treatment and follow-up'],['Equivocal echo with persistent suspicion','Use CMR when feasible']], [LVT], 'clinical_scenario')
q('Which conduction pattern after MI is most suggestive of extensive infranodal injury and a higher-risk anterior infarction rather than transient AV nodal dysfunction?',
 'Complete AV block with a slow broad-QRS escape rhythm during anterior MI',[
 ('Wenckebach block with a narrow QRS during inferior MI','This more often reflects AV nodal involvement and may be transient, although monitoring remains necessary.'),
 ('Sinus bradycardia resolving after reperfusion of an inferior MI','This often reflects vagal or nodal mechanisms rather than extensive His-Purkinje destruction.'),
 ('Brief first-degree AV block with stable hemodynamics','An isolated PR prolongation does not imply the same high-risk infranodal substrate.')],
 'Localizing conduction disease after infarction',
 '**The infarct territory, QRS width and escape rhythm help localize AV block.**',
 ['Inferior MI more commonly produces AV nodal block with a narrow escape rhythm.', 'Anterior MI with broad-QRS complete block suggests His-Purkinje injury and a larger damaged myocardial territory.'],
 '**Assess perfusion and prepare pacing support when clinically indicated.**',
 ['Hemodynamic instability, an unreliable escape rhythm or persistent high-grade block increases urgency.', 'Reperfusion remains essential; localization is a guide to risk and management, not a reason to delay reperfusion.'],
 [['Inferior MI, narrow-QRS Wenckebach','Often AV nodal and potentially transient'],['Anterior MI, broad-QRS complete block','Suggests infranodal injury and greater risk']], [ESC,ACS])
q('A patient meets MI criteria but angiography shows no stenosis of 50% or greater. No clear alternative diagnosis is evident. Which statement about MINOCA is most accurate?',
 'It is a working diagnosis requiring investigation of the underlying mechanism, often including CMR',[
 ('It proves that the symptoms were noncardiac','Nonobstructive angiography does not negate myocardial injury or the established ischemic presentation.'),
 ('It mandates the same indefinite DAPT regimen for every mechanism','Treatment depends on the final mechanism; plaque disruption, spasm and nonischemic mimics are not therapeutically identical.'),
 ('It is established only when troponin remains normal','MI requires myocardial injury; a normal troponin is not the defining feature of MINOCA.')],
 'MINOCA requires a mechanism-based evaluation',
 '**MINOCA describes an initial angiographic-clinical problem, not a single disease.**',
 ['Possible ischemic mechanisms include plaque disruption, embolism, spasm, microvascular dysfunction and dissection.', 'CMR can identify an infarct pattern or reveal a nonischemic alternative such as myocarditis or Takotsubo syndrome; those alternatives change the final diagnosis.'],
 '**Treatment should follow the mechanism established by further assessment.**',
 ['Review the angiogram carefully and use intracoronary or functional testing when appropriate.', 'Do not discharge the patient with either a dismissive normal-coronaries label or an indiscriminate lifelong antithrombotic regimen.'],
 [['Initial nonobstructive angiogram with MI criteria','Working MINOCA diagnosis'],['CMR demonstrates myocarditis','Nonischemic alternative diagnosis'],['Coronary spasm identified','Mechanism-directed anti-spasm therapy']], [ESC], 'clinical_scenario')
q('A hemodynamically stable woman has angiographically confirmed spontaneous coronary artery dissection of a mid-distal vessel, preserved distal flow and no ongoing ischemia. What is the usual initial coronary management strategy?',
 'Conservative management with monitoring rather than routine PCI',[
 ('Stent the entire dissected segment in every patient','PCI can propagate dissection, enter the false lumen and require extensive stenting; it is not routine in this stable presentation.'),
 ('Administer fibrinolysis to dissolve the intramural hematoma','Fibrinolysis is not treatment for an arterial-wall hematoma and may worsen bleeding and dissection.'),
 ('Perform emergency CABG solely because any SCAD is present','CABG is reserved for selected high-risk anatomy or unsuccessful alternatives, not all stable distal SCAD.')],
 'Stable SCAD is often managed conservatively',
 '**SCAD is an arterial-wall disorder, and many stable lesions heal without intervention.**',
 ['An intramural hematoma or intimal disruption can compress the true lumen without the usual plaque-rupture mechanism.', 'Interventional treatment is technically challenging and may extend the lesion.'],
 '**Conservative care requires observation and reassessment rather than neglect.**',
 ['Ongoing ischemia, hemodynamic instability or high-risk proximal anatomy can require revascularization.', 'Assess associated arteriopathies and individualize medication and follow-up; avoid automatically copying every atherosclerotic ACS treatment.'],
 [['Stable SCAD, preserved flow, no ongoing ischemia','Conservative strategy usually favored'],['Ongoing ischemia or high-risk instability','Consider revascularization with expert input']], [SCAD], 'clinical_scenario')
q('After major emotional stress, a postmenopausal woman develops chest pain and troponin elevation. Angiography shows no culprit obstruction. Imaging shows apical and midventricular akinesia extending beyond a single coronary distribution with basal hyperkinesis. Which diagnosis is most likely?',
 'Takotsubo syndrome',[
 ('A single distal LAD occlusion as the only explanation','The broad circumferential pattern extends beyond a usual single-vessel territory, and angiography shows no culprit obstruction.'),
 ('Chronic true LV aneurysm','A chronic scar aneurysm does not explain the acute stress-associated, multi-territory dysfunction pattern.'),
 ('Isolated right ventricular infarction','The described abnormality is a characteristic LV pattern rather than isolated RV dysfunction.')],
 'Recognizing a stress cardiomyopathy pattern',
 '**Takotsubo syndrome causes transient regional ventricular dysfunction, commonly extending beyond one epicardial vascular territory.**',
 ['A physical or emotional trigger is common but is not obligatory.', 'The syndrome can mimic ACS with pain, ECG changes and troponin elevation; a stress trigger alone is not diagnostic.'],
 '**Confirm the pattern and exclude competing conditions rather than assuming benign disease.**',
 ['CMR can help assess myocarditis or infarction, and follow-up imaging documents recovery.', 'Shock, LV outflow obstruction, arrhythmia and apical thrombus are clinically important possible complications.'],
 [['Typical Takotsubo pattern','Transient dysfunction beyond one vessel territory'],['Territorial infarction','Ischemic pattern matching the affected coronary supply'],['Myocarditis','Alternative inflammatory injury assessed with CMR and context']], [TTS], 'clinical_scenario')
q('A patient has recurrent rest angina with transient ST elevation. Angiography excludes flow-limiting fixed disease, and provocative testing confirms epicardial coronary spasm. Which drug class is the mainstay of preventive antianginal therapy?',
 'Calcium channel blockers',[
 ('Nonselective beta blockers as the preferred sole therapy','Nonselective beta blockade may worsen vasospasm and is not the mainstay of treatment for this mechanism.'),
 ('Fibrinolytics taken during each brief episode','Fibrinolysis does not treat recurrent vasomotor constriction and creates unnecessary bleeding risk.'),
 ('Digoxin as first-line coronary vasodilator treatment','Digoxin is not a primary coronary antispasm drug.')],
 'Mechanism-directed treatment of vasospastic angina',
 '**Calcium channel blockers reduce coronary smooth-muscle contraction and are central to preventing vasospastic episodes.**',
 ['Nitrates can relieve episodes and may be added for persistent symptoms when appropriate.', 'Smoking cessation and avoidance of provoking drugs are important parts of treatment.'],
 '**Match treatment to a vasomotor mechanism rather than a fixed stenosis model.**',
 ['An unobstructed angiogram does not exclude clinically important coronary ischemia.', 'Select the CCB and dose according to heart rate, ventricular function, blood pressure and tolerance.'],
 [['Epicardial coronary spasm','CCB-based anti-spasm treatment'],['Fixed obstructive disease','Risk reduction, antianginals and selected revascularization']], [CCS], 'clinical_scenario')
q('A patient with exertional angina has no obstructive coronary disease, an FFR of 0.93, reduced coronary flow reserve and elevated microvascular resistance. Which mechanism best explains the findings?',
 'Coronary microvascular dysfunction',[
 ('A physiologically significant focal epicardial stenosis demonstrated by the FFR','An FFR of 0.93 does not identify a flow-limiting focal epicardial lesion.'),
 ('Normal coronary physiology because angiography is nonobstructive','Angiography does not directly assess the microcirculation; abnormal flow reserve and resistance are meaningful.'),
 ('Epicardial spasm conclusively established by reduced flow reserve alone','Spasm requires appropriate vasoreactivity evidence; reduced flow reserve alone does not prove epicardial spasm.')],
 'Ischemia can arise below the angiographic resolution scale',
 '**Microvascular disease can limit coronary flow even when major epicardial arteries are not obstructed.**',
 ['Reduced coronary flow reserve reflects impaired flow augmentation, while elevated microvascular resistance supports a microvascular abnormality.', 'Interpret these measurements using the validated technique and its thresholds rather than one universal value for every modality.'],
 '**A normal epicardial pressure ratio does not establish a normal microcirculation.**',
 ['Functional testing can distinguish structural microvascular dysfunction, vasospasm and mixed mechanisms.', 'Tailored antianginal treatment and cardiovascular risk-factor management follow the identified endotype.'],
 [['FFR/iFR','Assess epicardial stenosis physiology'],['Flow reserve and microvascular resistance','Assess coronary flow and microvascular function'],['Acetylcholine testing','Assesses vasomotor responses']], [CCS], 'clinical_scenario')
q('During assessment of an intermediate stable coronary stenosis, FFR measured during adequate hyperemia is 0.76. Which interpretation is most appropriate?',
 'The lesion meets the usual physiological threshold for hemodynamic significance',[
 ('It is physiologically insignificant because FFR is below 0.80','The standard direction is the reverse: lower FFR indicates a greater pressure loss.'),
 ('It proves that PCI will reduce mortality in every stable patient','Physiological significance informs revascularization decisions but does not establish a universal survival benefit.'),
 ('It measures coronary calcium burden rather than pressure loss','FFR is a pressure-derived physiological index, not a calcium score.')],
 'Interpreting fractional flow reserve',
 '**An FFR of 0.80 or less is the commonly used threshold for a hemodynamically significant epicardial stenosis.**',
 ['FFR compares distal coronary pressure with aortic pressure during adequate hyperemia.', 'Pressure-wire quality, drift, serial lesions and the clinical setting influence interpretation.'],
 '**Use physiology within a complete revascularization decision.**',
 ['Symptoms, ischemic burden, anatomy and medical treatment still matter.', 'A positive physiological result does not mean every patient has an identical prognosis or requires the same procedure.'],
 [['FFR at or below 0.80','Supports hemodynamic significance'],['FFR above 0.80','Often supports deferral in an appropriate stable setting']], [CCS])
q('Which statement correctly describes the instantaneous wave-free ratio used for intermediate coronary stenoses?',
 'It is a resting pressure-derived index; 0.89 or less is the usual ischemic threshold',[
 ('It requires maximal adenosine hyperemia and uses a cutoff of 0.80','That description corresponds to FFR rather than iFR.'),
 ('It is a calcium score calculated from CT','iFR is an invasive pressure-wire measurement, not a CT calcium score.'),
 ('A higher value always indicates a more severe flow-limiting lesion','As with other pressure ratios, a lower value generally indicates a greater pressure loss.')],
 'iFR and FFR answer related questions using different conditions',
 '**iFR measures a resting diastolic pressure ratio without requiring adenosine-induced hyperemia.**',
 ['The usual decision threshold is iFR 0.89 or less.', 'FFR uses a hyperemic measurement with a threshold of 0.80 or less; the numerical cutoffs cannot be interchanged.'],
 '**Interpret a threshold alongside symptoms and technical quality.**',
 ['Discordance between indices or borderline values may require further assessment.', 'Neither index is a direct measure of plaque vulnerability or future plaque rupture risk.'],
 [['FFR','Hyperemic pressure ratio; threshold 0.80'],['iFR','Resting diastolic pressure ratio; threshold 0.89']], [CCS])
q('A patient with significant left main disease has a high-complexity distal bifurcation lesion and diffuse multivessel disease. Surgical risk is acceptable. Which revascularization recommendation is generally most appropriate?',
 'Heart Team assessment with CABG favored for the complex anatomy',[
 ('PCI is always preferable because it avoids sternotomy','Procedural invasiveness alone does not outweigh the implications of complex left main and multivessel anatomy.'),
 ('Defer all revascularization because symptoms improve with nitrates','Symptom improvement does not remove the prognostic implications of significant left main disease.'),
 ('Treat only the easiest distal lesion before discussing the left main','Revascularization should be planned around the high-risk anatomy rather than opportunistic treatment of a convenient lesion.')],
 'Complex left main disease requires an anatomical strategy',
 '**CABG is generally favored over PCI when significant left main disease has high anatomical complexity and surgery is suitable.**',
 ['The comparison depends on the likelihood of complete and durable revascularization.', 'A Heart Team weighs coronary complexity, comorbidity, operative risk and patient preferences.'],
 '**Do not extrapolate stable low-risk trial conclusions to significant left main disease.**',
 ['PCI remains an option for selected less complex anatomy or when surgical suitability is limited.', 'The stem establishes complex anatomy and acceptable operative risk, making CABG the generally preferred recommendation.'],
 [['Complex left main plus diffuse multivessel disease','CABG generally favored if suitable'],['Selected lower-complexity left main disease','Individualized CABG versus PCI discussion']], [CCD,CCS], 'clinical_scenario')
q('A patient has stable coronary disease, moderate-to-severe inducible ischemia, preserved LV function and controlled symptoms. Significant left main disease has been excluded. Which conclusion best reflects the ISCHEMIA trial?',
 'An initial invasive strategy did not reduce the primary ischemic composite outcome compared with an initial conservative strategy over the main trial follow-up',[
 ('Every patient with moderate ischemia requires immediate PCI to improve survival','The trial did not establish this universal survival indication.'),
 ('Revascularization cannot improve angina in any stable patient','Symptom benefit is a separate issue, especially in patients with frequent angina.'),
 ('The results apply without qualification to acute MI and significant left main disease','The trial addressed selected stable disease and should not be extrapolated to excluded high-risk or acute presentations.')],
 'What ISCHEMIA does and does not establish',
 '**A positive ischemia test is not, by itself, proof that routine immediate intervention improves major outcomes in every stable patient.**',
 ['The main trial found no reduction in its primary outcome with an initial invasive approach over a median 3.2 years.', 'An initial conservative strategy included guideline-directed therapy and angiography when clinically necessary; it did not prohibit later revascularization.'],
 '**Separate prognostic indications from symptom-relief indications and trial exclusions.**',
 ['Persistent lifestyle-limiting angina can still justify revascularization.', 'Significant left main disease, acute coronary syndromes and important LV dysfunction require their own evidence-based assessment.'],
 [['Stable selected disease with controlled symptoms','Initial medical strategy can be appropriate'],['Persistent limiting symptoms despite therapy','Consider revascularization for symptom relief'],['Significant left main or acute MI','Use the relevant high-risk pathway']], [ISCHEMIA,CCD])
q('A patient has lifestyle-limiting angina despite maximally tolerated antianginal therapy and a significant coronary stenosis suitable for intervention. Which is a well-established reason to offer revascularization?',
 'Improvement of angina and functional status',[
 ('A guaranteed survival benefit from any PCI in stable disease','Survival benefit depends on disease pattern and treatment context; it is not guaranteed by every stable PCI.'),
 ('Elimination of the need for lipid-lowering treatment','Revascularization does not treat the systemic atherosclerotic process or remove secondary-prevention indications.'),
 ('Prevention of every future infarction regardless of plaque location','Treating one stenosis cannot guarantee prevention of all future coronary events.')],
 'Symptom relief is a valid revascularization goal',
 '**Revascularization can improve symptoms when significant disease causes angina despite appropriate medical treatment.**',
 ['Confirm that the symptoms and lesion are plausibly related and that the anatomy is suitable.', 'Choose PCI or CABG according to anatomical complexity, ventricular function, comorbidity and preferences.'],
 '**Describe the expected benefit accurately during shared decision-making.**',
 ['Explain symptom benefit separately from any prognostic indication.', 'Continue antithrombotic treatment when indicated, lipid reduction, exercise and other secondary prevention after the procedure.'],
 [['Persistent limiting angina despite therapy','Revascularization may improve symptoms'],['Systemic atherosclerotic risk','Requires continuing preventive treatment']], [CCD,CCS], 'clinical_scenario')
q('A patient remains symptomatic with stable angina despite tolerated therapy. Heart rate is 52/min and blood pressure is 98/62 mm Hg, limiting further beta-blocker, CCB or nitrate titration. QT interval and renal and hepatic function are acceptable, and there are no relevant drug interactions. Which add-on drug is most suitable?',
 'Ranolazine',[
 ('Increase the beta blocker substantially','Further heart-rate reduction is poorly suited to the stated bradycardia.'),
 ('Add verapamil to the beta blocker','This combination can worsen bradycardia, AV conduction and hypotension.'),
 ('Use ivabradine to avoid any additional heart-rate reduction','Ivabradine lowers heart rate and is not a solution to pre-existing bradycardia.')],
 'Antianginal selection when heart rate and pressure limit therapy',
 '**Ranolazine can reduce angina without substantial lowering of heart rate or blood pressure.**',
 ['Its antianginal action is associated with inhibition of the late inward sodium current and reduced downstream calcium loading.', 'QT prolongation, interactions and renal or hepatic disease must be considered before prescribing.'],
 '**Choose an add-on that fits the hemodynamic constraints.**',
 ['The stem explicitly removes the major ranolazine selection concerns and highlights low heart rate and pressure.', 'It is a symptom-control drug; do not promise that it substitutes for risk reduction or confers a universal survival benefit.'],
 [['Low HR limits beta blockade or non-DHP CCB','Avoid further rate suppression'],['Low BP limits vasodilators','Consider an agent with little hemodynamic effect'],['Ranolazine','Check QT and interaction profile']], [CCD,CCS], 'clinical_scenario')
q('Three years after an uncomplicated MI, a patient has LVEF 60%, no angina, no arrhythmia and controlled blood pressure. What is the most accurate statement about continuing a beta blocker solely to improve prognosis under the 2023 chronic coronary disease guideline?',
 'Its ongoing indication can be reassessed rather than assuming a lifelong outcome benefit in every such patient',[
 ('It must be stopped abruptly in every patient after one year','Reassessment is not a mandate for abrupt withdrawal, which can provoke rebound symptoms.'),
 ('Lifelong mortality benefit is established irrespective of EF or other indications','The guideline does not support such an unconditional outcome claim.'),
 ('Beta blockers are contraindicated after any MI once EF normalizes','They may remain appropriate for angina, arrhythmia, hypertension or other indications.')],
 'Reassessing long-term beta blockade',
 '**The chronic indication depends on LV function, time from MI and other clinical needs.**',
 ['The 2023 guideline supports reassessing treatment beyond one year when LVEF is above 50% and there is no angina, arrhythmia or uncontrolled hypertension.', 'Evidence for remote uncomplicated MI with preserved EF differs from the established benefit in systolic HF.'],
 '**Individualize continuation or gradual withdrawal rather than applying an abrupt universal stop rule.**',
 ['Confirm whether another indication exists and monitor symptoms if treatment changes.', 'This question concerns the specified guideline recommendation, not a claim that every later trial has identical findings.'],
 [['Reduced EF or another active indication','Continue appropriate evidence-based therapy'],['Remote uncomplicated MI with preserved EF and no other indication','Reassess the need for ongoing beta blockade']], [CCD])
q('After ACS, a patient is adherent to maximally tolerated high-intensity statin therapy but LDL-C remains 86 mg/dL. Under the 2025 ACC/AHA ACS guideline, which lipid-lowering strategy is appropriate?',
 'Add a nonstatin LDL-lowering agent while continuing the maximally tolerated statin',[
 ('Stop the statin and use dietary advice alone','Established ACS requires intensive lipid reduction; lifestyle measures complement rather than replace effective medication.'),
 ('Continue unchanged because any LDL-C below 100 mg/dL is sufficient after ACS','The guideline recommends additional nonstatin therapy when LDL-C remains at least 70 mg/dL on maximally tolerated statin.'),
 ('Substitute a fibrate solely to raise HDL-C','The treatment priority here is further reduction of atherogenic LDL cholesterol, not an HDL-targeted substitution.')],
 'Residual LDL elevation after ACS',
 '**High-intensity or maximally tolerated statin therapy is the foundation, but residual LDL elevation often requires combination treatment.**',
 ['The 2025 ACC/AHA ACS guideline recommends a nonstatin agent when LDL-C remains at least 70 mg/dL on maximally tolerated statin.', 'Ezetimibe and PCSK9-directed therapies are options selected according to the needed reduction, risk, tolerance and access.'],
 '**Verify adherence and response before calling treatment ineffective.**',
 ['This stem establishes adherence, so repeating the same regimen without intensification misses the residual risk.', 'Targets and treatment thresholds differ across guideline systems; the question specifies the ACC/AHA ACS recommendation.'],
 [['Maximally tolerated statin with LDL-C at least 70 mg/dL after ACS','Add nonstatin LDL-lowering therapy'],['Statin intolerance','Use an individualized tolerated regimen and alternatives']], [ACS], 'clinical_scenario')
q('A patient with chronic coronary disease is clinically unchanged, exercises without new symptoms and has no decline in functional capacity. Which follow-up testing policy is recommended?',
 'Do not perform routine periodic ischemia or anatomical testing solely because another year has elapsed',[
 ('Perform invasive coronary angiography every year','Routine invasive surveillance without a clinical trigger exposes the patient to risk without an established benefit.'),
 ('Perform annual stress imaging regardless of symptoms','Routine periodic testing is not recommended simply for surveillance in clinically unchanged CCD.'),
 ('Avoid testing permanently even if new symptoms develop','New or worsening symptoms can create a valid indication for diagnostic reassessment.')],
 'Clinical change should drive repeat coronary testing',
 '**Routine periodic testing is not recommended in unchanged chronic coronary disease.**',
 ['New symptoms, a fall in exercise tolerance or a change in clinical status may justify reassessment.', 'The goal is to answer a clinical question rather than document the passage of time.'],
 '**Follow-up still includes active prevention and clinical review.**',
 ['Review symptoms, function, medication adherence, blood pressure, lipid response and lifestyle.', 'Avoid confusing absence of routine stress testing with absence of medical follow-up.'],
 [['Stable symptoms and function','Clinical follow-up and risk reduction'],['New angina or functional deterioration','Targeted diagnostic evaluation']], [CCD])
q('Before discharge after an uncomplicated MI, which intervention should be arranged as part of comprehensive secondary prevention, in addition to appropriate medications?',
 'Referral to a structured cardiac rehabilitation program',[
 ('Prolonged complete exercise avoidance for all survivors','Unnecessary inactivity promotes deconditioning; exercise should be prescribed according to stability and individual risk.'),
 ('Exercise advice alone without risk-factor or adherence support','Comprehensive rehabilitation includes more than a generic instruction to exercise.'),
 ('Stop preventive therapy once supervised exercise begins','Rehabilitation complements medical secondary prevention; it does not replace it.')],
 'Cardiac rehabilitation is comprehensive secondary prevention',
 '**Cardiac rehabilitation combines individualized exercise training with education and risk-factor management.**',
 ['Programs address functional recovery, smoking, nutrition, medication adherence and psychosocial needs.', 'Referral should be part of the discharge pathway after MI, with an accessible center-based or appropriate home-based model.'],
 '**Exercise prescription follows clinical stabilization and assessment.**',
 ['Activity intensity and progression depend on ventricular function, residual ischemia, arrhythmia risk and comorbidity.', 'Long-term adherence and preventive medication remain important after the supervised program ends.'],
 [['Acute unstable phase','Stabilize and assess risk'],['Stable recovery phase','Structured exercise and comprehensive rehabilitation'],['Long-term follow-up','Maintain activity and secondary prevention']], [ACS,CCD], 'clinical_scenario')
q('An ACS patient receiving DAPT has a prior peptic ulcer bleed and requires ongoing antiplatelet therapy after PCI. Which additional measure is recommended to reduce upper gastrointestinal bleeding risk?',
 'Prescribe an appropriate proton pump inhibitor',[
 ('Withhold all antiplatelet therapy solely because a remote ulcer bleed occurred','Abruptly abandoning indicated post-PCI treatment may create major thrombotic risk; manage bleeding risk within an individualized antithrombotic plan.'),
 ('Add a nonsteroidal anti-inflammatory drug for gastric protection','NSAIDs increase gastrointestinal bleeding risk and do not provide gastric protection.'),
 ('Use an antacid only because it provides equivalent evidence-based protection','Simple antacids are not an equivalent substitute for PPI gastroprotection in this high-risk context.')],
 'Gastroprotection during antithrombotic therapy',
 '**A PPI is recommended for ACS patients at risk of gastrointestinal bleeding while taking antiplatelet therapy.**',
 ['A previous ulcer bleed is an important risk marker.', 'Review additional bleeding contributors such as NSAIDs, anticoagulants and untreated ulcer disease; evaluate Helicobacter pylori where appropriate.'],
 '**Reduce bleeding risk while preserving necessary coronary protection.**',
 ['Individualize the antithrombotic regimen and PPI selection, including relevant interactions.', 'A PPI reduces upper GI risk but does not prevent every bleeding complication or eliminate the need for follow-up.'],
 [['Prior ulcer bleeding on antiplatelets','Provide PPI gastroprotection'],['Concurrent NSAID exposure','Avoid unnecessary use and reassess bleeding risk'],['Active bleeding','Urgent individualized bleeding and antithrombotic management']], [ACS], 'clinical_scenario')

assert len(rows) == 44, len(rows)
# Exact chapter balance with a reproducible noncyclic sequence; preserve every answer identity.
targets = list(range(4)) * 11
random.Random(604411).shuffle(targets)
for i, (item, target) in enumerate(zip(rows, targets), 1):
    old = item['correctIndex']
    if old != target:
        item['options'][old], item['options'][target] = item['options'][target], item['options'][old]
        for other in item['explanationTeaching']['otherOptions']:
            if other['optionIndex'] == target: other['optionIndex'] = old
            elif other['optionIndex'] == old: other['optionIndex'] = target
    item['correctIndex'] = target
    item['explanationTeaching']['otherOptions'].sort(key=lambda x:x['optionIndex'])
    item.update(id=f'cardiology-cad-acs-{i:03}',authorship='Original ChatGPT-authored topic-based question; not an authenticated examination PYQ',reviewStatus='authored_source_checked',sourceCheckedAt='2026-11-05')
    render(item)
bank.update(status='chapter_authored',questions=rows)
path.write_text(json.dumps(bank,ensure_ascii=False,indent=2),encoding='utf-8')
completed=ROOT/'completed/Cardiology/01. Coronary Artery Disease and Acute Coronary Syndromes/01. Coronary Artery Disease and Acute Coronary Syndromes/questions.json'
completed.parent.mkdir(parents=True,exist_ok=True)
completed.write_text(json.dumps(bank,ensure_ascii=False,indent=2),encoding='utf-8')
planpath=ROOT/'topic-map.json'
plan=json.loads(planpath.read_text(encoding='utf-8'))
for subject in plan['subjects']:
    for chapter in subject['chapters']:
        if subject['subject']=='Cardiology' and chapter['chapterOrder']==1:
            chapter.update(status='chapter_authored',draftQuestionCount=44,completedQuestionCount=44,completedFile=str(completed.relative_to(ROOT)))
planpath.write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(dict(chapter=bank['document'],questions=len(rows),answerDistribution={chr(65+i):targets.count(i) for i in range(4)},file=str(completed),activeBanksReplaced=0),indent=2))
