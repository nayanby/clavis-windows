"""Original decision-mapped coronary disease, ACS and MI question bank."""
import json
from qbank_json_chapters import question as Q,save,ROOT
R={
 'MI':('Joint ESC/ACC/AHA/WHF Fifth Universal Definition of MI, 2026','https://pmc.ncbi.nlm.nih.gov/articles/PMC13523810/'),
 'ACS':('ACC/AHA/ACEP/NAEMSP/SCAI ACS guideline, 2025','https://doi.org/10.1016/j.jacc.2024.11.009'),
}
rows=[]
def S(h,main,*children):return h,[(main,list(children))]
def add(*a,**kw):rows.append(Q(*a,**kw))

add('ACS diagnosis and myocardial infarction classification','Acute Injury Requires a Mechanistic Diagnosis',
 'A patient with systemic illness has a clear rise and fall in high-sensitivity troponin, with at least one value above the assay’s sex-specific 99th percentile. No ischemic or acute coronary evidence is established yet. What is the best-supported current label?',
 'Acute myocardial injury',[
 ('Primary myocardial infarction','Primary infarction requires an appropriate spontaneous ischemic or acute coronary presentation; the troponin pattern alone does not establish that mechanism.'),
 ('Secondary myocardial infarction','Another acute illness can produce secondary infarction, but a trigger and acute injury alone are insufficient; establish ischemia and the required supporting assessment.'),
 ('Chronic myocardial injury','Chronic injury is an elevated persistent pattern rather than the clear acute rise and fall supplied in this question.')],
 [S('Establish the Biomarker Pattern First','**A rise and/or fall with a value above the sex-specific 99th percentile supports acute myocardial injury.** Use the actual assay and sampling context.',
    'The supported label should precede any more specific mechanism assignment. An acute illness can coexist with coronary disease, so neither automatic infarction labeling nor automatic dismissal is appropriate.',
    'A laboratory boundary does not independently determine the next procedure or antithrombotic prescription.'),
  S('Connect Further Assessment to the Clinical Question','**Evaluate symptoms, ECG, hemodynamics and appropriate imaging.** The urgency depends on the evolving presentation, including whether an acute coronary process is plausible.',
    'Treat the underlying illness and instability while clarifying cardiac involvement. Consider whether additional testing will change care and whether its procedural burden is acceptable.',
    'Record the measured values, time course and relevant clinical findings rather than relying on a nonspecific positive-troponin description. If evidence changes, revise the diagnosis transparently. A nonspecific injury label does not mean the finding is harmless, and a more specific infarction label should not be used merely to make the record appear decisive. Communication should separate what is established from what remains under evaluation so subsequent clinicians do not inherit an unsupported assumption about coronary thrombosis.')],['MI','ACS'])

add('ACS diagnosis and myocardial infarction classification','Primary MI Includes Acute Coronary Pathologies Beyond Atherothrombosis',
 'A patient develops spontaneous ischemic chest pain, dynamic ischemic ECG changes and acute troponin elevation. Angiography identifies spontaneous coronary artery dissection as the culprit, without a preceding cardiac procedure or an alternative acute illness. Under the 2026 clinical classification, which category applies?',
 'Primary myocardial infarction',[
 ('Secondary myocardial infarction','Secondary infarction is considered when another acute condition creates the supply–demand mismatch; here the presentation arises from a primary acute coronary pathology itself.'),
 ('Procedure-related myocardial infarction','This category concerns infarction complicating a cardiac procedure in the applicable time frame; angiography performed to diagnose an already-present spontaneous event does not make it procedure-related.'),
 ('Acute nonischemic myocardial injury','The case supplies ischemic findings and a culprit acute coronary pathology, so a nonischemic injury label fails to account for the demonstrated mechanism.')],
 [S('Classify the Clinical Setting and Then the Cause','**The 2026 primary category includes spontaneous acute coronary pathology**, not only plaque-associated thrombosis. The identified SCAD mechanism fits that setting.',
    'Keep the clinical category, ECG presentation and coronary etiology distinct. A category name does not by itself determine whether PCI is beneficial for the specific culprit process.',
    'Historical type numbering may appear in older trials and examination sources; label its year rather than assuming a one-to-one translation without reviewing the mechanism.'),
  S('Avoid Classification Errors Created by the Investigation','**A diagnostic procedure does not retroactively become the cause of an event that preceded it.** Establish the temporal sequence clearly.',
    'Review symptoms, biomarker timing and imaging together. Document the culprit mechanism when demonstrated instead of stopping at an undifferentiated MI label.',
    'Care remains guided by hemodynamic stability, ongoing ischemia and the specific coronary pathology. In a patient with SCAD, a standard plaque-rupture intervention strategy should not be adopted simply because both events fall under a broad primary category. Explain the diagnosis and its implications using the actual findings. The reason for specificity is to guide a suitable treatment and follow-up plan, not to replace immediate stabilization with a terminology exercise.')],['MI','ACS'])

add('ACS diagnosis and myocardial infarction classification','Secondary MI Requires More Than a Supply–Demand Trigger',
 'During severe anemia, a patient develops ischemic discomfort, new ST depression and an acute troponin rise. Imaging shows a new regional abnormality in an ischemic distribution. Coronary assessment identifies obstructive CAD without an acute culprit pathology. Under the 2026 definition, which diagnosis is supported?',
 'Secondary myocardial infarction',[
 ('Primary myocardial infarction','Primary MI remains an important alternative during acute illness, but this case establishes a mismatch trigger and obstructive disease without an acute coronary culprit.'),
 ('Acute myocardial injury without established infarction','That label is appropriate while infarction remains unconfirmed, but the stem adds ischemic findings and the objective features supporting secondary MI.'),
 ('Chronic myocardial injury with incidental CAD','A clear acute troponin change, new ischemic ECG findings and a new regional abnormality do not fit an unchanged chronic injury pattern.')],
 [S('Confirm the Ischemic Mechanism','**The 2026 secondary category addresses infarction triggered by another acute condition causing supply–demand mismatch.** The stated anemia is the trigger, not proof by itself.',
    'Here, ischemic evidence and the objective assessment support the diagnosis. If an acute coronary culprit had instead been found, primary MI would need consideration.',
    'The presence of an illness should therefore neither automatically create nor automatically exclude an infarction diagnosis.'),
  S('Treat the Trigger and the Demonstrated Substrate','**Correct the anemia and assess ongoing ischemia and hemodynamic stability.** Investigate and control its cause, including bleeding when relevant.',
    'Subsequent coronary and ventricular treatment follows the demonstrated disease and the individual benefit–risk balance rather than a reflex plaque-rupture regimen.',
    'Document which findings confirmed infarction and which condition triggered it. When additional imaging is not feasible or appropriate, communicate the limits of diagnostic certainty rather than implying that every necessary test was performed. A historical type-2 label may appear in older literature, but its use should be dated because the current confirmation framework is more specific. The classification helps distinguish the treatment problem: managing an acute trigger and clinically important coronary substrate differs from assuming a new coronary thrombosis solely from an elevated troponin.')],['MI','ACS'])

add('ACS diagnosis and myocardial infarction classification','Procedure-Related MI Within the 2026 Time Window',
 'Five days after elective PCI, a patient develops acute chest pain, new ischemic ECG changes and a new troponin rise. Angiography shows thrombosis of the recently treated segment, and echo shows a corresponding new regional wall-motion abnormality. Under the 2026 clinical classification, which category applies?',
 'Procedure-related myocardial infarction',[
 ('Primary myocardial infarction unrelated to the recent procedure','The 2026 framework places an infarction caused by a coronary complication within 30 days of a cardiac procedure in the procedure-related category; the documented early stent event fits that context.'),
 ('Secondary myocardial infarction from a systemic demand trigger','No alternative systemic mismatch trigger explains the event; angiography instead identifies a coronary complication of the recent intervention.'),
 ('Expected post-PCI myocardial injury without infarction','Routine injury after an intervention does not explain this new ischemic episode with a demonstrated coronary complication and corresponding new ventricular abnormality.')],
 [S('Use the Clinical Time Window and Causal Evidence','**The 2026 definition applies a 30-day window to infarction caused by a cardiac procedural complication.** The diagnosis is not established merely because troponin is elevated after a procedure.',
    'Confirmation requires a demonstrated coronary complication or new ischemic regional dysfunction/loss of viable myocardium. Both are required when the complication occurs during the procedure or the procedure is performed in acute MI. This day-five case supplies both, beyond an expected biomarker leak.',
    'The framework differs from older PCI/CABG-specific type numbering and should be identified by year when teaching or comparing studies.'),
  S('Preserve the Sequence of Events','**Distinguish a complication of treatment from the original condition that prompted treatment.** Baseline biomarkers, intervening recovery and the new episode matter.',
    'Review antiplatelet exposure, adherence, procedural findings and other contributors while arranging urgent management of the demonstrated complication.',
    'Immediately after a procedure, the 2026 framework describes a likely diagnosis when biomarkers increase from baseline and continue rising at six hours after intervention, for example above five times URL, or at twenty-four hours after surgery, for example above thirty-five times URL. These are context-dependent examples supporting suspicion, not standalone confirmation thresholds. Apply the coronary and ventricular confirmation requirements as well. This differs from importing historical PCI/CABG type-number thresholds into the new framework. Record the culprit, timing and regional consequence while treating recurrent occlusion urgently.')],['MI','MI2026SLIDES','ACS'])

R.update({
 'ESCACS':('ESC ACS guideline, 2023','https://doi.org/10.1093/eurheartj/ehad191'),
 'CHESTPATH':('ACC emergency chest-pain evaluation consensus pathway, 2022','https://doi.org/10.1016/j.jacc.2022.08.750'),
})

add('ACS diagnosis and myocardial infarction classification','Serial High-Sensitivity Troponin in an Early Presenter',
 'A stable patient presents 45 minutes after ischemic-sounding chest pain began. The ECG has no persistent ST elevation. Initial hs-cTn is below the 99th percentile but does not meet a validated assay-specific very-low rule-out threshold. Which next approach is appropriate?',
 'Use the validated assay-specific serial pathway with repeat ECG and clinical reassessment',[
 ('Exclude MI because the initial value is below the 99th percentile','The diagnostic injury boundary is not itself a single-sample early rule-out criterion; troponin can still rise after a very recent symptom onset.'),
 ('Apply a numeric rule-out cutoff from a different hs-cTn assay','Different assays have different validated concentrations and change thresholds; a cutoff cannot be transferred merely because both tests are called high sensitivity.'),
 ('Diagnose unstable angina immediately from the normal first sample','Unstable angina remains possible, but an early first sample cannot establish the absence of evolving injury; complete the appropriate serial assessment.')],
 [S('Use the Correct Algorithm for the Actual Assay','**Validated 0/1-hour or 0/2-hour pathways combine baseline concentration and change**, together with the clinical and ECG findings.',
    'The zero time refers to the initial sample. A very early presentation and a value below the 99th percentile do not automatically satisfy a single-sample discharge rule.',
    'Use the laboratory’s validated assay-specific concentrations and deltas rather than a universal number.'),
  S('Preserve Clinical Reassessment','**Repeat assessment when pain persists, recurs or the clinical picture changes.** A biomarker pathway does not override an indication for immediate invasive evaluation.',
    'An observation-zone result requires further assessment rather than forced assignment to rule-in or rule-out. Consider repeat sampling and targeted testing according to risk.',
    'Describe the actual time course so later clinicians can distinguish an early nondiagnostic sample from a completed negative pathway. Rule-out of infarction does not exclude every cause of ischemic symptoms or every dangerous alternative diagnosis. Similarly, a rule-in biomarker pattern identifies a high-probability injury presentation that still requires clinical interpretation of the cause. The aim is a validated diagnostic sequence, with disposition based on the integrated evidence rather than one apparently reassuring laboratory result.')],['ESCACS','CHESTPATH'])

add('ACS diagnosis and myocardial infarction classification','Unstable Angina After Adequate Serial Testing',
 'A patient has recurrent rest discomfort with transient ischemic ST depression. Appropriately timed serial hs-cTn values remain below the assay’s injury threshold without a significant rise. The ischemic presentation remains clinically convincing. Which diagnosis is most appropriate?',
 'Unstable angina',[
 ('NSTEMI established by the dynamic ECG alone','Dynamic ischemic changes are important, but an infarction diagnosis requires acute myocardial injury; the stem specifies adequate serial testing without that evidence.'),
 ('Chronic stable angina','Stable angina is a reproducible chronic pattern, typically related to exertion; recurrent rest symptoms with dynamic ischemic changes indicate an unstable presentation.'),
 ('Nonischemic chest pain established by the negative troponins','Negative injury testing does not establish a nonischemic mechanism when transient ischemic ECG changes and the clinical presentation remain convincing.')],
 [S('Separate Ischemia From Demonstrable Injury','**Unstable angina describes an unstable ischemic presentation without established acute myocardial injury.** Sensitive assays have reclassified many older unstable-angina cases as infarction.',
    'That change in frequency does not eliminate unstable angina. Adequate timing and serial testing matter before using the label.',
    'The early single negative sample in a new presentation is a different scenario from the completed assessment stated here.'),
  S('Manage the Risk Rather Than the Biomarker Label Alone','**Persistent or recurrent ischemia and instability influence the urgency of care.** A negative troponin does not justify dismissal of dynamic ischemic findings.',
    'Review the ECG during and after symptoms, assess hemodynamics and investigate according to the ACS risk pathway. Alternative causes of symptoms and ST changes must also be considered.',
    'Treatment depends on the suspected mechanism, bleeding risk and invasive plan rather than an assumption that every troponin-negative patient has trivial disease. Document why the presentation remains ischemic and whether symptoms have resolved. If the pattern is instead chronic and exertional, or adequate evaluation identifies a noncoronary explanation, revise the diagnosis. A precise unstable-angina label requires positive clinical reasoning, not simply the absence of a biomarker elevation.')],['ESCACS','ACS'])

R['AORTA']=('ACC/AHA aortic disease guideline, 2022','https://pmc.ncbi.nlm.nih.gov/articles/PMC9876736/')
R['CMR2026']=('EACVI/ESC clinical consensus on CMR implementation, 2026','https://doi.org/10.1093/eurheartj/ehag678')

add('ACS diagnosis and myocardial infarction classification','MINOCA Is a Working Diagnosis Requiring Further Evaluation',
 'A patient has acute troponin elevation and a possible ischemic presentation. Angiography shows no stenosis ≥50%, and no mechanism has been established. Under the 2026 definition, which next approach is most appropriate?',
 'Treat MINOCA as a myocardial-injury working diagnosis and investigate the cause, including appropriately timed CMR',[
 ('Assign myocarditis as the final diagnosis and arrange follow-up echocardiography','Myocarditis is a plausible cause of injury with nonobstructive coronaries, but the angiogram alone cannot establish it; tissue characterization and the clinical differential remain necessary.'),
 ('Assign coronary vasospasm as the mechanism and start a definitive vasospasm regimen','Vasospasm is a genuine coronary alternative, but nonobstructive anatomy does not demonstrate it; targeted functional evaluation may be needed after other causes are assessed.'),
 ('Assign occult plaque disruption and prescribe a fixed long-term ACS regimen','Plaque disruption can be missed on angiography and may warrant selected intravascular imaging, but the working label alone does not establish this mechanism or its definitive treatment.')],
 [S('Use the Updated Working Terminology','**The Fifth Universal Definition expands MINOCA as myocardial injury with nonobstructive coronary arteries.** Its purpose is to preserve diagnostic uncertainty until the mechanism is established.',
    'The term is not a final confirmation of infarction and does not mean that angiography has proved normal coronary physiology.',
    'Label older infarction-based terminology by year when interpreting historical trials and guidelines.'),
  S('Select Tests That Can Establish the Cause','**CMR can distinguish ischemic from several nonischemic injury patterns.** The 2026 document favors early assessment, ideally within two weeks when feasible.',
    'Intravascular imaging or coronary functional testing can address selected unresolved coronary mechanisms. Review noncardiac causes when the presentation warrants them.',
    'Select testing to resolve the actual differential and change treatment. An ischemic scar pattern supports infarction but does not independently identify plaque disruption, embolism or spasm. A normal study does not establish a specific coronary mechanism or exclude every small or transient injury. Interpret tissue characterization alongside symptom timing, ECG and coronary findings. The 2026 CMR consensus describes myocarditis assessment using both an edema-sensitive T2 marker and an injury-sensitive T1 marker; late enhancement alone is not the complete framework.')],['MI','ESCACS','CMR2026'],
 table=(['CMR finding','Interpretation','Limitation'],[
 ['Subendocardial or transmural LGE in a coronary territory','Ischemic injury pattern','Does not establish the coronary mechanism'],
 ['Subepicardial or midwall LGE with edema','Supports a nonischemic inflammatory process','Integrate T1/T2 markers and clinical findings'],
 ['No diagnostic scar or edema pattern','No tissue mechanism established by this scan','Timing and lesion size affect sensitivity']]))

add('ACS diagnosis and myocardial infarction classification','Acute Aortic Syndrome Can Present With Myocardial Ischemia',
 'A hemodynamically stable patient has abrupt severe chest pain maximal at onset, an interarm pulse difference and a new diastolic murmur. ECG shows ischemic changes. Which investigation should be prioritized before committing to an antithrombotic or fibrinolytic ACS pathway?',
 'Urgent CT angiography directed at suspected acute aortic syndrome',[
 ('Serial troponin testing as the principal discriminator','Troponin can identify myocardial injury but cannot exclude aortic dissection or establish whether coronary ischemia is due to aortic involvement.'),
 ('D-dimer as a stand-alone exclusion test','A low D-dimer can contribute in selected low-probability pathways, but this high-risk presentation requires definitive imaging rather than biomarker exclusion alone.'),
 ('Immediate coronary-only angiography without assessing the aorta','Coronary assessment may become necessary, but the abrupt pain, pulse discrepancy and new regurgitant murmur require urgent evaluation of the suspected aortic emergency.')],
 [S('Recognize the Competing Emergency','**Acute aortic disease can cause coronary malperfusion and ischemic ECG changes.** Those findings do not establish primary coronary atherothrombosis as the cause.',
    'Abrupt maximal pain, pulse or pressure differences and a new aortic regurgitation murmur raise concern in the stated presentation.',
    'A normal chest radiograph would not adequately exclude the diagnosis.'),
  S('Match Imaging to Stability and Availability','**CT is recommended as initial diagnostic imaging for suspected acute aortic syndrome in suitable patients.** TEE or MRI can be alternatives according to circumstances.',
    'If instability makes transport unsafe, bedside assessment and specialist coordination may favor another rapid imaging route. Begin appropriate monitoring and urgent aortic-team involvement.',
    'Fibrinolysis or indiscriminate anticoagulation can be dangerous when dissection is the actual mechanism, so resolve this specific high-risk differential promptly rather than waiting for a complete biomarker series. This is not a reason to delay reperfusion in every typical coronary presentation; the stem supplies substantial aortic red flags. Document the reasoning and proceed rapidly with definitive care once the anatomy is known. The purpose of recognizing the mimic is to choose the correct emergency pathway, not simply add another diagnosis to a list.')],['AORTA','ACS'])

add('ECG localization and urgent coronary occlusion recognition','Lead-Specific ST-Elevation Thresholds',
 'A 35-year-old man with ongoing ischemic chest discomfort has new J-point elevation confined to V2 and V3, without LVH or bundle branch block. Which minimum elevation in both leads meets the standard age- and sex-specific threshold?',
 '2.5 mm',[
 ('1.0 mm','One millimeter is the standard threshold in other qualifying leads, but V2–V3 require the specified age- and sex-specific threshold.'),
 ('1.5 mm','One and a half millimeters is the V2–V3 threshold for women, not a man younger than forty.'),
 ('2.0 mm','Two millimeters is the V2–V3 threshold for men aged forty or older; the stated patient is thirty-five.')],
 [S('Apply the Correct Lead and Patient Category','**In V2–V3, men younger than forty require at least 2.5 mm**, compared with 2 mm in older men and 1.5 mm in women.',
    'Use the J-point and contiguous leads. The ordinary 1-mm threshold for other leads must not replace the V2–V3 qualification.',
    'The standard framework assumes the absence of confounding LVH or bundle branch block, as specified in this stem.'),
  S('Use the ECG to Direct Timely Clinical Assessment','**Thresholds support a working reperfusion diagnosis in the appropriate presentation**, not a complete etiologic diagnosis from voltage alone.',
    'Evaluate symptom timing, prior tracings and reciprocal or evolving changes. Some acute occlusions do not display conventional qualifying elevation, and some nonischemic conditions do.',
    'Do not wait for biomarkers to become positive when the presentation warrants emergency reperfusion assessment. Conversely, an isolated voltage criterion should be interpreted with its clinical context and the possibility of repolarization variants or other causes. Correct electrode placement and calibration matter when measurements sit near a boundary. The teaching point is a precise standard criterion, while the bedside decision remains an integrated assessment of possible acute coronary occlusion.')],['MI','ESCACS'],style='direct',table=(['Lead group','Standard J-point threshold'],[
 ['V2–V3, men <40 years','≥2.5 mm'],['V2–V3, men ≥40 years','≥2.0 mm'],
 ['V2–V3, women','≥1.5 mm'],['Other standard leads','≥1 mm in the required contiguous distribution']]))

add('ECG localization and urgent coronary occlusion recognition','Posterior Infarction Hidden in Anterior Reciprocal Changes',
 'A patient with ongoing ischemic discomfort has horizontal ST depression in V1–V3 with prominent anterior R waves. No conventional ST-elevation territory is apparent. Which additional lead set most directly evaluates the suspected missed infarct?',
 'Posterior leads V7–V9',[
 ('Right-sided leads V3R–V4R','Right-sided leads assess RV involvement, particularly with inferior infarction; they do not directly test the posterior territory suggested by anterior reciprocal depression.'),
 ('Repeat limb leads with emphasis on aVR','Limb leads can clarify other ischemic patterns, but the described anterior reciprocal changes specifically call for posterior recording rather than aVR-focused assessment.'),
 ('Repeat standard V1–V3 after moving them superiorly','High right-precordial placement has other uses, but does not substitute for posterior leads in evaluating the suspected posterior injury pattern.')],
 [S('Interpret the Reciprocal View','**Posterior injury may appear as ST depression in anterior leads**, often with a prominent R wave as the reciprocal counterpart of a posterior Q-wave pattern.',
    'Posterior V7–V9 recordings directly sample the suspected territory. The ESC 2023 supplementary ECG framework identifies elevation of at least 0.5 mm in V7–V9 as supporting posterior STEMI in the compatible clinical setting; standard anterior-lead thresholds should not be substituted for this posterior criterion.',
    'Prominent anterior R waves have other causes, so the acute symptoms and ST pattern are necessary context rather than proof from R-wave height alone.'),
  S('Act on the Integrated Occlusion Assessment','**A standard twelve-lead ECG can miss a posterior elevation pattern.** Additional leads should be acquired promptly while urgent coronary assessment proceeds.',
    'Posterior infarction may accompany inferior or lateral involvement; do not force an isolated territory when the full tracing shows more extensive injury.',
    'Serial ECGs, symptoms and hemodynamics remain important. A nondiagnostic initial biomarker does not remove concern during an early ongoing ischemic presentation. Distinguish this pattern from diffuse subendocardial ischemia and other causes of anterior depression using the full ECG and clinical evidence. Record electrode placement and acquisition time so the posterior tracing can be compared correctly. The useful next test is the lead set that resolves the suspected blind spot, not a delay for unrelated investigations.')],['MI','ESCACS'])

R['SGARBOSSA']=('Smith et al. modified Sgarbossa derivation study, 2012','https://pubmed.ncbi.nlm.nih.gov/22939607/')

add('ECG localization and urgent coronary occlusion recognition','Right Ventricular Involvement in Inferior Infarction',
 'A patient with inferior ST elevation develops hypotension, elevated jugular venous pressure and relatively clear lungs. Which additional ECG recording most directly evaluates the suspected accompanying chamber involvement?',
 'Right precordial leads V3R and V4R',[
 ('Posterior leads V7–V9','Posterior leads evaluate posterior injury and are useful with compatible reciprocal changes, but the hemodynamic pattern here specifically raises concern for RV involvement.'),
 ('Repeat standard V5 and V6 at the same positions','Lateral leads may show additional infarct extension, but do not replace right-sided leads for evaluating the suspected RV territory.'),
 ('High right-precordial V1 and V2 recordings','High right-precordial placement can clarify selected electrical patterns, but the appropriate infarction assessment is a standard right-sided lead recording rather than a superior shift.')],
 [S('Localize the Hemodynamic Problem','**Inferior infarction can involve the RV**, producing impaired forward delivery, venous congestion and hypotension without prominent pulmonary edema.',
    'ESC guidance recommends right precordial recording in suspected inferior STEMI. Elevation in V3R–V4R supports ongoing RV ischemia.',
    'The examination pattern is suggestive rather than exclusive; assess other causes of hypotension and obtain appropriate echo when useful.'),
  S('Support Perfusion While Arranging Reperfusion','**Avoid reflex preload reduction in a hypotensive patient with suspected RV involvement.** Evaluate nitrate exposure, filling, rhythm and perfusion before treatment.',
    'Fluid may help selected underfilled patients but should be titrated with reassessment; indiscriminate large-volume loading can worsen RV dilation and congestion.',
    'Treat important bradycardia or AV dyssynchrony and maintain an urgent coronary reperfusion strategy. Clear lungs do not prove that every hypotensive patient needs fluid, just as venous distension does not independently establish the infarct territory. Record right-sided leads promptly because changes can evolve. The purpose of the additional tracing is to clarify a management-relevant extension of the infarct, not delay definitive care while seeking a perfect localization label.')],['ESCACS','ACS'])

add('ECG localization and urgent coronary occlusion recognition','Proportionally Excessive Discordance in LBBB',
 'A patient with established LBBB has persistent ischemic discomfort. A predominantly negative QRS lead has an S-wave depth of 8 mm and discordant J-point elevation of 3 mm. Which interpretation is appropriate?',
 'The discordance meets the proportional modified Sgarbossa criterion and supports urgent occlusion assessment',[
 ('The finding falls below the excessive-discordance threshold because elevation is under 5 mm','Five millimeters is the original absolute discordance boundary; the modified criterion instead identifies disproportionate elevation relative to S-wave depth, which this lead satisfies.'),
 ('The finding falls below the proportional threshold because ST/S is less than positive 0.25','The signed ratio uses a negative S-wave amplitude and is compared with minus 0.25 or lower; alternatively compare positive magnitudes, where 37.5 percent exceeds twenty-five percent.'),
 ('The finding requires at least 5 mm elevation as well as a qualifying ST/S ratio','The modified proportional criterion requires at least one millimeter of discordant elevation, not a second five-millimeter requirement; three millimeters satisfies the amplitude component.')],
 [S('Use the Sign Convention Correctly','**With an S wave recorded as −8 mm, the ST/S ratio is 3/−8 = −0.375.** This is at or below the −0.25 proportional boundary.',
    'Equivalently, elevation is 37.5% of the S-wave magnitude, exceeding a quarter. The elevation also exceeds the minimum 1 mm used in the modified criterion.',
    'This replaces the older fixed excessive-discordance threshold; it does not mean every expected discordant ST segment is abnormal.'),
  S('Modified Sgarbossa Criteria','**The modified rule is positive when any one of three components is present:** concordant ST elevation at least 1 mm in a lead with a positive QRS; concordant ST depression at least 1 mm in V1, V2 or V3; or discordant elevation at least 1 mm with signed ST/S ratio at most −0.25.',
    'Check baseline, calibration and lead quality. A negative criterion does not exclude occlusion in a patient with compelling ongoing ischemia.',
    'Use urgent specialist assessment and appropriate reperfusion planning when the integrated picture is concerning. Do not delay necessary care while waiting for a biomarker rise, and do not infer that a positive criterion identifies the exact culprit artery. The original study supports improved detection with proportional assessment, but no ECG rule is perfectly sensitive or specific. Document the measured elevation, S-wave depth and clinical context so the interpretation can be reviewed rather than reduced to LBBB-positive or LBBB-negative.')],['SGARBOSSA','ESCACS'])

R['DEWINTER']=('de Winter et al. original acute LAD occlusion ECG report, 2008','https://doi.org/10.1056/NEJMc0804737')

add('ECG localization and urgent coronary occlusion recognition','de Winter Pattern During Ongoing Ischemic Pain',
 'A patient has persistent crushing chest discomfort. ECG shows upsloping J-point depression across the precordial leads merging into tall symmetric T waves, without conventional anterior ST elevation. Potassium is normal. Which action is most appropriate?',
 'Arrange emergency coronary occlusion assessment and reperfusion planning',[
 ('Use serial troponin results to decide whether to activate the emergency invasive pathway','Serial biomarkers are appropriate in many stable suspected ACS presentations, but persistent ischemia with this occlusion-suggestive pattern warrants escalation before biochemical confirmation.'),
 ('Plan inpatient angiography within twenty-four hours after initial medical stabilization','An early inpatient approach suits selected stable high-risk NSTE-ACS, but ongoing pain with an occlusion-suggestive ECG requires more immediate assessment than that planned interval.'),
 ('Repeat ECGs until conventional anterior elevation appears before activating the pathway','Serial ECGs help identify evolving ischemia and should continue during care, but waiting for conventional elevation can delay reperfusion when the current pattern already suggests occlusion.')],
 [S('Recognize Occlusion Without Conventional Elevation','**The de Winter pattern combines precordial upsloping depression with prominent symmetric T waves.** It was described in acute LAD occlusion.',
    'Interpret the pattern with the ongoing symptoms, prior tracing and the full ECG. It is not simply a large T wave or an isolated numerical amplitude criterion.',
    'Hyperacute ischemic T waves and evolving occlusion patterns may change over time; obtain serial recordings without delaying escalation.'),
  S('Do Not Wait for a More Familiar Pattern','**Persistent ischemia with an occlusion-suggestive ECG requires urgent coronary assessment.** Biomarker negativity early after symptom onset does not remove this concern.',
    'Check important mimics such as electrolyte abnormalities in parallel, but do not use a pending test as a reason to postpone necessary care.',
    'The pattern is associated with LAD disease but should not be presented as a perfectly specific map of the culprit in every patient. Definitive anatomy and treatment follow the emergency assessment. Communicate the concern clearly to the receiving team rather than describing the ECG merely as nonspecific ST depression. A working occlusion diagnosis is meant to accelerate an appropriate reperfusion pathway, not to require that every feature of a textbook image be present before action.')],['DEWINTER','MI','ACS'])

add('ECG localization and urgent coronary occlusion recognition','Diffuse ST Depression With aVR Elevation',
 'During ongoing chest discomfort, a patient has horizontal ST depression in multiple inferolateral leads with ST elevation in aVR. Which interpretation is most appropriate?',
 'A high-risk global ischemic pattern that requires clinical assessment without uniquely identifying left-main occlusion',[
 ('Acute left-main coronary thrombosis established from the ECG','Left-main disease is an important possibility, but this appearance does not distinguish acute thrombosis from severe multivessel disease or global supply–demand ischemia without further assessment.'),
 ('Severe three-vessel coronary disease established from the ECG','Multivessel disease can cause this pattern, but angiographic anatomy cannot be determined definitively from the ECG; an acute left-main process and systemic mismatch remain alternatives.'),
 ('Secondary ischemia from a systemic supply–demand trigger established from the ECG','Severe anemia, hypoxemia or hemodynamic stress can produce global ischemia, but the tracing alone does not establish such a trigger or exclude a primary acute coronary process.')],
 [S('Describe the Ischemic Pattern Before the Anatomy','**Widespread ST depression with aVR elevation can reflect global subendocardial ischemia.** Left-main or multivessel coronary disease belongs in the differential.',
    'The same appearance can occur during severe supply–demand imbalance and other presentations. The ECG does not independently establish acute left-main thrombosis.',
    'Evaluate symptoms, blood pressure, rhythm, oxygenation and the extent and evolution of changes.'),
  S('Let Instability and Persistent Ischemia Determine Urgency','**Hemodynamic compromise or refractory symptoms require urgent escalation.** A high-risk pattern should not be placed in a low-risk pathway merely because regional elevation is absent.',
    'Treat a reversible trigger when present while reassessing whether an acute primary coronary process remains plausible. Persistent changes after correction warrant continued concern.',
    'Use the full clinical evidence to plan invasive assessment and antithrombotic treatment, considering important alternative emergencies and bleeding risk. A precise handover distinguishes the observed ECG from an unconfirmed anatomic diagnosis. Avoid the opposite errors of overcalling one specific lesion and underreacting to a potentially extensive ischemic burden. Serial comparison can clarify evolution, but observation should not delay intervention when the patient is unstable.')],['ESCACS','MI','ACS'])

R['MYOPERI']=('ESC myocarditis and pericarditis guideline, 2025','https://doi.org/10.1093/eurheartj/ehaf192')

add('ECG localization and urgent coronary occlusion recognition','Recurrent Transient ST Elevation Is Not a Reassuring Resolution',
 'A patient has repeated episodes of ischemic discomfort with transient ST elevation that resolves between attacks. Pain and ECG changes recur despite initial treatment. Under the 2023 ESC ACS framework, which approach is appropriate?',
 'Immediate invasive assessment for recurrent ischemia with dynamic ECG changes',[
 ('Arrange early inpatient angiography within twenty-four hours after serial biomarker assessment','An early inpatient strategy suits stable high-risk features, but recurrent ischemia despite treatment with repeated dynamic changes supports immediate assessment without waiting for biomarker confirmation.'),
 ('Continue medical treatment and reserve angiography for persistent ST elevation','Persistent elevation identifies a familiar emergency pathway, but repeated transient elevation during refractory ischemia is itself a very-high-risk feature; waiting for persistence can delay indicated intervention.'),
 ('Begin a calcium antagonist trial and defer angiography until the symptom response is assessed','Calcium antagonists are appropriate for established vasospastic angina, but reversibility alone does not establish spasm; a treatment trial should not postpone assessment of this recurrent unstable presentation.')],
 [S('Distinguish Resolved High-Risk Features From Ongoing Instability','**Recurrent or refractory ischemia and repeated dynamic ECG changes support an immediate invasive strategy.** A normalized tracing between attacks does not erase the clinical sequence.',
    'A stable patient after one resolved transient episode has a different risk context from this patient with recurrence despite treatment.',
    'Document ECGs during symptoms and after resolution rather than using only the latest apparently improved tracing.'),
  S('Escalate While Continuing Monitored Care','**Continue rhythm and hemodynamic monitoring and urgent cardiology coordination.** Reassess the mechanism and treatment response while arranging definitive evaluation.',
    'Troponin adds information about injury but does not need to become positive before persistent high-risk ischemia is addressed.',
    'The distinction between immediate and early assessment depends on the current clinical state, not simply an isolated score or an ECG label. If a vasomotor mechanism is eventually established, tailor treatment accordingly; do not presume it from nitrate response or transient changes alone. Communicate recurrent episodes clearly at handover so that an asymptomatic interval is not mistaken for a low-risk presentation. The purpose of serial evaluation is to detect this evolving risk and act on it, rather than collect additional normal intervals while ischemia continues.')],['ESCACS','ACS'])

add('ECG localization and urgent coronary occlusion recognition','Pericarditis Versus a Territorial Coronary Pattern',
 'A patient has sharp pleuritic chest pain relieved by leaning forward, a friction rub, widespread ST elevation and PR depression. There is no territorial reciprocal depression apart from expected changes in aVR. Which diagnosis best fits the integrated presentation?',
 'Acute pericarditis',[
 ('Acute territorial coronary occlusion','Coronary occlusion remains an important alternative in chest pain, but the positional pleuritic symptoms, rub and widespread PR/ST pattern favor pericardial inflammation rather than one coronary territory.'),
 ('Benign early repolarization','Early repolarization can cause widespread elevation, but does not explain a new friction rub and the stated inflammatory pain pattern as well as acute pericarditis.'),
 ('A persistent post-infarct ventricular aneurysm pattern','An aneurysm can produce persistent regional ST elevation after an infarct, usually with supporting history and Q-wave or imaging evidence; it does not match the acute widespread inflammatory pattern here.')],
 [S('Integrate the Symptoms and Examination With the ECG','**Widespread elevation with PR depression supports pericarditis in the appropriate inflammatory presentation.** The rub and positional pleuritic pain provide independent clinical evidence.',
    'ST shape alone is insufficient: concavity does not reliably exclude coronary occlusion, and inflammatory disease can occasionally produce regional findings.',
    'Under ESC 2025, a definite clinical pericarditis diagnosis requires a compatible presentation with more than one additional criterion; one supports possible pericarditis. This stem supplies both a rub and characteristic ECG changes. These are separate criteria; PR depression and widespread elevation are components of the same ECG category, not two independent categories.'),
  S('Assess Extent and Complications','**Obtain appropriate echocardiography, inflammatory markers and myocardial-injury assessment.** Effusion, ventricular dysfunction or elevated troponin can change the evaluation.',
    'Consider myocardial involvement and important alternative causes when the presentation is atypical or severe. A pericarditis diagnosis does not imply that coronary disease cannot coexist.',
    'If coronary occlusion remains plausible, resolve it urgently. Assess tamponade, significant effusion, myocardial involvement and secondary causes before disposition. Elevated troponin suggests associated myocardial injury rather than providing an additional pericarditis biomarker criterion. Treatment and follow-up depend on this full assessment, not ST morphology alone.')],['MYOPERI','MI'],
 table=(['Additional pericarditis criterion: ESC 2025','Finding'],[
 ['Examination','Pericardial friction rub'],
 ['ECG','PR depression or widespread ST elevation'],
 ['Inflammatory biomarker','Raised CRP'],
 ['Echocardiography','New or worsening pericardial effusion'],
 ['CMR','Pericardial edema or late gadolinium enhancement']]))

add('STEMI reperfusion and post-lysis management','Timely Primary PCI in a Transfer Patient',
 'A patient presents to a non-PCI hospital two hours after STEMI symptoms began. Transfer can achieve first device activation 105 minutes after first medical contact. There is no reason that transport is unsafe. Under the 2025 ACC/AHA framework, which reperfusion strategy is preferred?',
 'Immediate transfer for primary PCI',[
 ('Immediate fibrinolysis because the expected interval exceeds ninety minutes','Ninety minutes is the system goal for direct presentation, while the transfer framework allows a goal up to 120 minutes; the stated 105-minute interval supports primary PCI.'),
 ('Fibrinolysis followed by primary PCI on arrival regardless of reperfusion response','A pharmaco-invasive pathway is appropriate when timely primary PCI is unavailable, but routine lysis before an already timely PCI adds risk without being the preferred strategy here.'),
 ('Antithrombotic stabilization with elective angiography after symptoms settle','An eligible early STEMI requires urgent reperfusion, not a plan to await spontaneous symptom resolution before elective coronary assessment.')],
 [S('Use the Correct Clock and Presentation Pathway','**The 2025 ACC/AHA transfer goal is first-medical-contact to device activation within 120 minutes.** The direct-presentation goal is within ninety minutes.',
    'This patient’s anticipated 105-minute transfer pathway fits the stated primary PCI goal. Begin activation and transfer promptly rather than using the goal as permission for avoidable delay.',
    'Keep total symptom duration separate from the system interval; both inform the clinical context.'),
  S('Coordinate Treatment During Transfer','**Provide monitored ACS care and the appropriate antithrombotic plan while arranging PCI.** Screen for shock, bleeding and important alternative emergencies.',
    'Communicate the ECG, symptom onset and actual expected device time with the receiving team. A nominal transport time is not the same as an achievable reperfusion time.',
    'If the plan becomes delayed, reassess the strategy rather than assuming the original estimate remains true. Primary PCI and a pharmaco-invasive pathway are distinct strategies; giving a lytic simply because the ambulance is leaving for a PCI center is not an equivalent default. The preference is timely effective reperfusion with the least justified treatment burden, guided by the named system and patient eligibility.')],['ACS'])

add('STEMI reperfusion and post-lysis management','Fibrinolysis When Timely Primary PCI Is Unavailable',
 'A patient presents two hours after clear STEMI onset. Predicted diagnosis-to-wire-crossing time is 190 minutes despite an organized transfer plan. There is no fibrinolytic contraindication and treatment can be given promptly. Under 2023 ESC guidance, which strategy is appropriate?',
 'Prompt fibrinolysis followed by immediate transfer into a pharmaco-invasive pathway',[
 ('Transfer for primary PCI without fibrinolysis at the predicted 190-minute delay','Direct primary PCI is preferred when timely or when lysis is unsuitable, but this eligible early presenter exceeds the ESC 120-minute diagnosis-to-reperfusion threshold.'),
 ('Give fibrinolysis and arrange transfer only if reperfusion fails','Failure requires rescue PCI, but success also requires immediate transfer and planned early angiography; making transfer conditional on failure omits the successful-lysis pathway.'),
 ('Give fibrinolysis and transfer for immediate routine PCI regardless of the reperfusion response','Immediate rescue PCI is appropriate after failed lysis or instability; after successful uncomplicated lysis, routine angiography is planned at 2–24 hours rather than using an automatic immediate facilitated-PCI strategy.')],
 [S('Apply the ESC Reperfusion Threshold','**When PCI-mediated reperfusion cannot be achieved within 120 minutes of STEMI diagnosis, eligible patients within twelve hours of onset should receive fibrinolysis.** This case is well within the symptom window.',
    'ESC targets prompt lytic administration, within ten minutes of diagnosis, when that strategy is selected and the contraindication screen is complete.',
    'The named diagnosis-to-wire clock differs in wording from the ACC/AHA first-medical-contact-to-device framework; report the clock explicitly.'),
  S('Treat Lysis as the Beginning of an Invasive Pathway','**Transfer immediately to a PCI-capable center after treatment.** Monitor symptoms, ST resolution, rhythm, hemodynamics and bleeding.',
    'Failed reperfusion requires rescue assessment; successful lysis still leads to a planned early invasive strategy rather than discharge from the initial facility.',
    'Select the lytic and concomitant antithrombotics using age, weight, renal function and the current protocol. Fibrinolysis is not an indiscriminate treatment for all troponin-positive ACS or all ST depression. Verify the reperfusion diagnosis and contraindications while avoiding unnecessary delay. The decision reflects the balance between the benefit of earlier reperfusion and the bleeding risk, not a claim that lysis and PCI are interchangeable in every setting.')],['ESCACS','ACS'])

R['TNK']=('TNKase FDA prescribing information, 2025: indication-specific dosing','https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/103909s5197lbl.pdf')

add('STEMI reperfusion and post-lysis management','Prior Intracranial Hemorrhage and STEMI Fibrinolysis',
 'An otherwise eligible early STEMI patient cannot receive timely primary PCI. Which history is an absolute contraindication to fibrinolysis under the 2025 ACC/AHA ACS framework?',
 'A spontaneous intracranial hemorrhage six years earlier',[
 ('An ischemic stroke five years earlier without residual deficit','A remote ischemic stroke requires careful assessment and is a relative contraindication in the stated framework; it is not equivalent to any previous intracranial hemorrhage.'),
 ('Current pregnancy without active bleeding','Pregnancy is an important relative bleeding-risk consideration, but is not classified as the same absolute prohibition as the supplied prior intracranial hemorrhage.'),
 ('Prolonged resuscitation with possible chest-wall trauma','Traumatic or prolonged CPR increases bleeding concern and requires assessment, but is a relative consideration rather than the particular absolute history asked for here.')],
 [S('Distinguish Absolute From Relative Contraindications','**Any prior intracranial hemorrhage is an absolute contraindication in this STEMI framework.** A long interval does not convert it into a low-risk remote ischemic stroke history.',
    'Other critical exclusions include active important bleeding and suspected aortic dissection. Review the complete current checklist rather than asking only about one neurologic event.',
    'Remote ischemic stroke, pregnancy and traumatic resuscitation require individualized assessment of relative risk and alternatives.'),
  S('Choose a Reperfusion Pathway That Remains Available','**A contraindication to lysis does not remove the need for reperfusion assessment.** Arrange urgent PCI-capable transfer and specialist coordination.',
    'Confirm the stroke type from records when uncertainty can be resolved rapidly; do not assume every past event was ischemic or use an unreliable description to override risk.',
    'Assess blood pressure, medicines, recent surgery, trauma and bleeding in parallel. The table summarizes the 2025 ACC/AHA STEMI framework, whose time windows differ from some other guidance. Its acute ischemic stroke exception concerns a separate indication and specialist eligibility assessment; it is not blanket permission to give the STEMI lytic regimen in concurrent stroke. Document the contraindication and alternative reperfusion plan clearly.')],['ACS','ESCACS'],
 table=(['Clinical feature','Absolute exclusion in ACC/AHA 2025','Relative concern in the same framework'],[
 ['Intracranial disease','Any prior ICH; cerebral vascular lesion; malignant intracranial neoplasm','Other known intracranial pathology; dementia'],
 ['Prior ischemic stroke','Within 3 months, with the guideline’s acute-stroke exception','More than 3 months earlier'],
 ['Head injury or neurosurgery','Significant closed-head/facial trauma within 3 months; intracranial/intraspinal surgery within 2 months','Assess other trauma according to site and severity'],
 ['Blood pressure','SBP >180 or DBP >110 mmHg unresponsive to treatment','Same elevation at presentation before treatment; chronic severe poor control'],
 ['Bleeding or aortic disease','Active bleeding/bleeding diathesis excluding menses; suspected dissection','Internal bleeding within 2–4 weeks; active peptic ulcer; oral anticoagulant treatment'],
 ['Recent procedures','Intracranial/intraspinal surgery as above','Major surgery within 3 weeks; noncompressible vascular puncture'],
 ['Other relative concerns','Assess all absolute exclusions first','Traumatic/prolonged CPR >10 minutes; pregnancy']]))

add('STEMI reperfusion and post-lysis management','Weight-Based Tenecteplase for STEMI',
 'A 62-year-old weighing 84 kg is selected for fibrinolysis for STEMI. Using the standard adult STEMI weight-tier regimen without an older-patient dose reduction, what is the tenecteplase dose?',
 '45 mg as a single IV bolus',[
 ('40 mg as a single IV bolus','Forty milligrams is the standard STEMI tier for weight at least 70 but below 80 kg; this patient weighs 84 kg.'),
 ('50 mg as a single IV bolus','Fifty milligrams is the standard maximum tier for weight at least 90 kg, rather than the 80-to-below-90-kg tier supplied here.'),
 ('25 mg as a single IV bolus','Twenty-five milligrams is not the standard full-dose STEMI tier for this patient; it can arise in a different indication or an explicitly modified regimen.')],
 [S('Use the Indication-Specific Weight Table','**The standard STEMI tenecteplase regimen uses weight tiers rather than one fixed dose for all adults.** At 84 kg, the applicable tier is ==45 mg==.',
    'Check the vial, reconstituted concentration and delivery instructions. A dose stated in milligrams should not be converted to milliliters without confirming the preparation.',
    'Do not substitute an acute ischemic stroke regimen merely because the drug name is the same.'),
  S('Complete the Fibrinolysis Prescription','**The lytic is only one component of treatment.** Appropriate antiplatelet and anticoagulant therapy, monitoring and immediate transfer are also required.',
    'The ESC 2023 fibrinolysis recommendation advises considering half-dose tenecteplase in patients older than seventy-five years. Thus an otherwise eligible older patient in the 80-to-below-90-kg tier would receive 22.5 mg under that modified regimen, rather than the standard 45 mg. The sixty-two-year-old in this stem is outside that age modification. Keep the guideline age wording and local protocol explicit rather than confusing this reduction with a stroke dose.',
    'Review contraindications, weight reliability, recent antithrombotic exposure and bleeding risk before administration. Observe for neurologic symptoms and other bleeding after treatment. A correct numerical dose does not establish that the patient was eligible for fibrinolysis or that reperfusion succeeded. Assess the subsequent ECG and clinical response and use the rescue or planned angiographic pathway as appropriate. Keep indication and protocol visible in the prescription to prevent confusion between different tenecteplase uses.')],['TNK','ACS','ESCACS'],style='direct',table=(['Body weight','Standard STEMI dose'],[
 ['<60 kg','30 mg'],['60 to <70 kg','35 mg'],['70 to <80 kg','40 mg'],['80 to <90 kg','45 mg'],['≥90 kg','50 mg']]))

add('STEMI reperfusion and post-lysis management','Clopidogrel at the Time of STEMI Fibrinolysis',
 'A 68-year-old is receiving STEMI fibrinolysis and aspirin. There is no P2Y12 contraindication. Which oral P2Y12 regimen matches the 2025 ACC/AHA recommendation at fibrinolytic administration?',
 'Clopidogrel 300 mg loading, then 75 mg daily',[
 ('Clopidogrel 75 mg daily without a loading dose','A no-loading regimen is used in older fibrinolysis patients; the sixty-eight-year-old in this question is clearly within the loading-dose group.'),
 ('Ticagrelor 180 mg loading, then 90 mg twice daily','Ticagrelor has an important role in ACS, particularly PCI pathways, but is not the recommended initial oral P2Y12 regimen given concurrently with fibrinolysis here.'),
 ('Prasugrel 60 mg loading, then 10 mg daily','Prasugrel is used in selected PCI-treated ACS patients after appropriate assessment, rather than as the standard P2Y12 adjunct at fibrinolytic administration.')],
 [S('Use the Reperfusion-Specific Regimen','**Clopidogrel is the recommended oral P2Y12 adjunct at fibrinolysis in the stated framework.** At age below seventy-five, use ==300 mg loading followed by 75 mg daily==.',
    'The 2025 ACC/AHA narrative uses age at least seventy-five for the no-load 75 mg regimen, whereas its Table 7 uses older than seventy-five; ESC 2023 also uses older than seventy-five. Thus the exact seventy-fifth-year boundary is not internally consistent across these presentations. Follow the applicable local protocol at that boundary; this sixty-eight-year-old case is unambiguous and does not test the discrepancy.',
    'Do not transfer a primary-PCI preference for another P2Y12 agent directly into the initial lysis prescription.'),
  S('Complete and Reconcile Concomitant Treatment','**Aspirin and a suitable parenteral anticoagulant are also part of the pathway.** Select and dose the anticoagulant using age, weight and renal function.',
    'For example, the cited enoxaparin lysis regimen below age seventy-five with adequate renal function begins with 30 mg IV, then 1 mg/kg subcutaneously every twelve hours, with the first two doses capped at 100 mg.',
    'That example must not be copied to older patients or severe renal impairment without adjustment. Record all pretransfer doses and times so the receiving PCI team avoids duplication. Monitor for bleeding and assess reperfusion while arranging transfer. Later switching or procedural loading decisions depend on elapsed time, previous exposure and the invasive plan; the initial clopidogrel choice does not supply permission for an unplanned extra load of another agent.')],['ACS','ESCACS'])

add('STEMI reperfusion and post-lysis management','Failed Fibrinolysis Requires Rescue Assessment',
 'Ninety minutes after fibrinolysis, a patient still has ischemic chest pain and only 20% resolution of the initial ST elevation. Which next strategy is appropriate?',
 'Immediate angiography with rescue PCI when indicated',[
 ('Give a second fibrinolytic dose and reassess after another ninety minutes','Repeat lysis is not the recommended rescue strategy for failed reperfusion; urgent angiography addresses persistent occlusion and avoids delaying effective treatment.'),
 ('Wait for routine angiography in the two-to-twenty-four-hour window','That planned early window applies after successful lysis in a stable patient, whereas persistent pain and poor ST resolution indicate failure requiring immediate assessment.'),
 ('Continue medical treatment and repeat the ECG at three hours before deciding on rescue','Later reassessment can be useful when initial findings are equivocal, but persistent ischemic pain with only twenty-percent ST resolution at ninety minutes already supports failed reperfusion and should prompt immediate rescue assessment.')],
 [S('Assess Reperfusion at the Appropriate Time','**ST resolution below 50% at sixty to ninety minutes supports failed fibrinolysis.** Persistent pain strengthens the concern in this case.',
    'Hemodynamic or electrical instability, worsening ischemia or evidence of reocclusion can also require immediate angiography rather than waiting for a scheduled reassessment.',
    'A transient rhythm change or partial symptom improvement does not override ongoing concerning evidence.'),
  S('Separate Rescue PCI From Planned Early Angiography','**Rescue PCI addresses failure or renewed occlusion.** Successful fibrinolysis still requires transfer and early angiography, but it is a different clinical pathway.',
    'Communicate the lytic agent, timing, antiplatelets, anticoagulants and subsequent ECG response to the receiving team.',
    'Continue monitoring and evaluate bleeding while urgent transport and catheterization are coordinated. Repeat fibrinolysis is discouraged in this setting rather than treated as an interchangeable second attempt. Do not await enzyme completion, a further routine ward review or proof of an unfavorable outcome before acting. The decision follows the current reperfusion evidence and patient stability, with angiography determining the anatomy and appropriate intervention.')],['ESCACS','ACS'])

add('STEMI reperfusion and post-lysis management','Angiography After Apparently Successful Fibrinolysis',
 'After fibrinolysis, a stable patient has resolution of pain and 70% ST-segment resolution at ninety minutes. Under the 2023 ESC pharmaco-invasive pathway, which plan is appropriate?',
 'Transfer and routine angiography within two to twenty-four hours of the lytic bolus',[
 ('Transfer and schedule angiography forty-eight to seventy-two hours after the bolus','A later inpatient schedule can be considered in other clinical settings, but it misses the recommended two-to-twenty-four-hour routine invasive window after successful fibrinolysis.'),
 ('Transfer and use recurrent ischemia to determine whether angiography is needed','An ischemia-guided selective strategy is used in selected other presentations, but successful lysis still requires routine early angiographic assessment under this pharmaco-invasive framework.'),
 ('Transfer for immediate rescue angiography on the basis of residual ST elevation','Immediate rescue is appropriate for failed lysis, recurrent ischemia or instability; seventy-percent resolution with relief of pain and stability does not meet that stated failure pattern.')],
 [S('Recognize Success Without Ending the Pathway','**Pain relief and substantial ST resolution support successful reperfusion**, but do not prove a normal culprit artery or eliminate recurrence risk.',
    'In the ESC framework, routine angiography follows within ==2–24 hours from the lytic bolus==, with PCI if required.',
    'Transfer to the PCI-capable center begins promptly; it is not postponed until the intended catheterization time.'),
  S('Escalate if the Clinical State Changes','**Recurrent ischemia, failed reperfusion or instability moves the patient into an immediate rescue pathway.** Do not retain a routine schedule when the indication changes.',
    'Continue ECG, rhythm, hemodynamic and bleeding surveillance. Reconcile all antiplatelet and anticoagulant doses before the procedure.',
    'The planned early strategy differs from routine facilitated immediate PCI after giving lysis to a patient who could already receive timely primary PCI. Describe the indication and timing clearly to avoid confusing those pathways. A reperfusion arrhythmia is supportive information, not a reason to stop monitoring or omit angiography. The clinical sequence remains lytic selection, transfer, response assessment and the appropriate invasive step, with treatment adjusted to the patient’s evolving condition.')],['ESCACS','ACS'])

add('STEMI reperfusion and post-lysis management','Late Presentation With a Stable Completed Infarct',
 'Four days after a completed infarct, a patient is stable and asymptomatic without ongoing ischemia, severe acute heart failure or life-threatening arrhythmia. Angiography shows a persistently occluded infarct-related artery. Which principle is appropriate?',
 'Do not perform routine PCI solely to reopen the completed-infarct artery in this stable setting',[
 ('Perform routine infarct-artery PCI during the current admission','Routine late opening has not improved the expected clinical outcomes in the stable completed-infarct population; ongoing ischemia or another independent indication would change the assessment.'),
 ('Schedule infarct-artery PCI after four weeks of medical stabilization','Staged PCI is useful for selected residual significant disease, but delaying this procedure does not create an indication to open a stable completed-infarct artery solely for patency.'),
 ('Perform elective infarct-artery PCI if any residual viability is detected','Viability can inform selected complex assessments, but residual viable tissue alone is not an automatic indication for routine late opening; symptoms, ischemic burden, anatomy and clinical context remain relevant.')],
 [S('Distinguish a Completed Infarct From Ongoing Salvageable Ischemia','**Routine PCI beyond forty-eight hours is not supported solely to open an occluded infarct artery in an asymptomatic stable patient.** This is a clinical-population qualification, not a prohibition on every late intervention.',
    'Ongoing angina, shock, severe acute heart failure or dangerous arrhythmias require a different urgent assessment even when symptom onset was delayed.',
    'Avoid treating the calendar alone as the decision rule; the current clinical state determines whether an active indication remains.'),
  S('Continue Comprehensive Post-Infarct Care','**Assess ventricular function, complications and secondary prevention needs.** Lack of a routine late-opening indication does not mean that treatment or follow-up is complete.',
    'OAT tested routine PCI versus medical therapy in selected stable patients with persistent infarct-artery occlusion three to twenty-eight days after MI. Routine opening did not reduce its composite of death, reinfarction or NYHA class IV heart failure.',
    'Other coronary lesions, recurrent symptoms or a separate revascularization indication require their own assessment. Residual viability was present in many patients assessed in an OAT ancillary study, so this evidence is not simply a comparison restricted to completely nonviable infarcts. Medical therapy, rehabilitation and risk-factor care remain essential. Document whether ongoing ischemia exists. If the condition changes, reassess rather than retaining a conclusion derived from an earlier stable presentation.')],['ACS','ESCACS','OAT'])

add('NSTE-ACS risk and invasive strategy','Electrical Instability in NSTE-ACS',
 'A patient with NSTE-ACS develops sustained ventricular tachycardia requiring cardioversion, with continued ischemic discomfort afterward. There is no persistent diagnostic ST elevation. Which invasive strategy is appropriate?',
 'Immediate angiography with intent to revascularize if indicated',[
 ('Early angiography within twenty-four hours after routine ward stabilization','A within-day strategy is appropriate for selected stable high-risk patients, but the life-threatening electrical instability and continuing ischemia warrant immediate assessment.'),
 ('A selective strategy after predischarge stress imaging','Stress-based selection is inappropriate during ongoing ischemia with sustained VT; the patient has an urgent invasive indication.'),
 ('An inpatient angiogram after forty-eight to seventy-two hours of rhythm observation','A delayed inpatient approach may be selected in stable patients with different risk profiles, but sustained VT with continuing ischemia requires immediate invasive assessment rather than observation for recurrence.')],
 [S('Recognize Very-High-Risk Features Without Requiring STEMI','**Electrical instability with ongoing ischemia supports an immediate invasive strategy.** A conventional ST-elevation pattern is not required for every coronary emergency.',
    'Resuscitate the arrhythmia and correct reversible contributors while the coronary pathway is activated. Treatment and investigation proceed together.',
    'Hemodynamic instability or refractory ischemia are other reasons not to wait for a routine early slot.'),
  S('Use the Patient’s Current State to Set Urgency','**Risk scores and biomarker timing do not override active instability.** The clinical event supplies an actionable risk feature.',
    'Continue monitoring, defibrillation capability and appropriate ACS treatment during transfer or catheterization preparation.',
    'Angiography identifies the coronary anatomy; revascularization depends on the findings and feasibility. Do not assume every ventricular arrhythmia has a coronary cause, but do not dismiss the demonstrated ischemic context because the ECG lacks persistent elevation. Document the rhythm, treatment and post-cardioversion symptoms so the receiving team understands why this is an immediate rather than simply an early investigation. A subsequently normal rhythm does not erase the significance of the event that prompted escalation.')],['ACS','ESCACS'])

add('NSTE-ACS risk and invasive strategy','Stable High-Risk NSTE-ACS and Early Angiography',
 'A stabilized patient with confirmed NSTEMI is pain-free, without heart failure or electrical instability, and has a GRACE score of 156. Under the 2023 ESC framework, which timing approach is appropriate?',
 'An inpatient invasive strategy with angiography within twenty-four hours considered',[
 ('Emergency angiography solely because GRACE exceeds 140','A score above 140 supports high risk and consideration of early angiography, but does not by itself create the same immediate indication as shock, refractory ischemia or electrical instability.'),
 ('Outpatient angiography after noninvasive stress testing','Confirmed NSTEMI with this risk profile supports an inpatient invasive approach rather than routine outpatient stress-based triage.'),
 ('A selective invasive strategy based on a negative predischarge stress test','Selective testing may guide care in appropriately assessed lower-risk presentations, but established NSTEMI with GRACE 156 supports an inpatient invasive strategy even while symptoms are controlled.')],
 [S('Separate the Invasive Plan From Its Exact Timing','**An inpatient invasive strategy is appropriate in confirmed NSTEMI.** In the 2023 ESC framework, high-risk findings such as GRACE above 140 support considering angiography within twenty-four hours.',
    'This is distinct from an immediate strategy for very-high-risk clinical instability. The stem explicitly describes a stabilized patient.',
    'The wording and recommendation strength should be attributed to the named guideline rather than presented as an identical rule across every source and year.'),
  S('Reassess While Awaiting the Procedure','**New refractory pain, shock, acute ischemic heart failure or dangerous arrhythmia changes the urgency.** A planned early slot is not a reason to wait through deterioration.',
    'Review bleeding risk, renal function, comorbidity and the antithrombotic plan alongside ischemic risk.',
    'Trials of early versus delayed angiography vary in eligibility and actual timing; do not infer identical mortality benefit for all risk groups. The ESC 2023 table distinguishes an inpatient invasive strategy from the recommendation to consider an early procedure. Continue monitored reassessment because new very-high-risk findings supersede the planned timetable.')],['ESCACS','ACS'],
 table=(['ESC 2023 group','Qualifying findings','Invasive approach'],[
 ['Very high risk','Hemodynamic instability/shock; refractory or recurrent pain despite treatment; life-threatening arrhythmia; mechanical complication; ACS-related HF; recurrent dynamic ST/T changes, especially intermittent elevation','Immediate invasive strategy'],
 ['High risk','Confirmed NSTEMI; GRACE >140; dynamic ST/T changes; transient ST elevation','Inpatient invasive strategy; angiography within 24 hours should be considered'],
 ['No very-high/high-risk criteria','Assess residual clinical suspicion, comorbidity and test findings','Individualize inpatient assessment or selective invasive evaluation']]))

add('NSTE-ACS risk and invasive strategy','An Admission Risk Score Does Not Override New Instability',
 'An NSTE-ACS patient had a GRACE score below 140 at admission. Several hours later, refractory pain and new hypotension develop. Which interpretation should guide care?',
 'The new clinical instability requires immediate reassessment and invasive escalation despite the earlier score',[
 ('Recalculate GRACE and use the updated category to select the angiography time','Recalculation may document changing risk, but current refractory ischemia and hypotension already justify immediate escalation; the updated score is not a prerequisite.'),
 ('Obtain the next scheduled troponin to confirm recurrent injury before escalating','Serial troponin helps characterize injury, but hemodynamic deterioration and refractory pain require urgent action even before another biomarker change is demonstrated.'),
 ('Intensify anti-ischemic therapy and retain the early inpatient angiography slot','Medical stabilization proceeds alongside urgent assessment; retaining a nonemergency slot underweights the new instability and may delay treatment of ongoing coronary compromise.')],
 [S('Use Risk Prediction for Its Intended Purpose','**GRACE estimates clinical risk from defined patient variables.** It helps stratify patients but is not a guarantee of a stable future course.',
    'Age, hemodynamics, renal function, heart failure severity, arrest, ECG and biomarker information contribute in the relevant score version.',
    'Use a validated calculator and the correct version rather than reconstructing a score from an incomplete list or mixing models for different outcomes.'),
  S('Reassess the Evolving Patient','**New refractory ischemia and hypotension change the clinical pathway.** Stabilize, investigate complications and coordinate urgent invasive assessment.',
    'Do not wait for another laboratory value or an updated score to cross a threshold when the urgent indication is already present.',
    'Document the change from the admission state and communicate it clearly to the receiving team. Risk scores summarize selected evidence; they do not encode every dangerous complication or remove the need for serial examination. Conversely, a high predicted risk in a stable patient is not the same as the immediate clinical emergency described here. Keep the reason for urgency tied to the actual deterioration so later clinicians do not mistake it for an elective timing preference.')],['ACS','ESCACS'])

add('NSTE-ACS risk and invasive strategy','P2Y12 Pretreatment Before Early Angiography',
 'A stable NSTE-ACS patient has unknown coronary anatomy and angiography planned in four hours. Under the 2023 ESC approach, which P2Y12 strategy is appropriate?',
 'Defer routine oral P2Y12 loading until anatomy and the revascularization plan are known',[
 ('Give prasugrel 60 mg now, before transfer to the catheterization laboratory','Prasugrel is effective for eligible PCI patients after the treatment decision, but pretreatment before anatomy is known failed to improve ischemic outcomes and increased bleeding in ACCOAST.'),
 ('Give ticagrelor 180 mg now, before transfer to the catheterization laboratory','Ticagrelor is appropriate in eligible ACS treatment and may be considered upstream with substantially delayed angiography, but routine pretreatment is discouraged in this early-invasive unknown-anatomy setting.'),
 ('Give clopidogrel 600 mg now, before transfer to the catheterization laboratory','Clopidogrel can be selected when potent agents are unsuitable or in other defined pathways, but its lower potency does not remove bleeding or surgical concerns that favor deferral here.')],
 [S('Define Pretreatment Precisely','**Pretreatment means giving a P2Y12 inhibitor before coronary anatomy is known.** It is a timing decision, not a decision to omit appropriate eventual antiplatelet treatment.',
    'For planned early angiography within twenty-four hours in NSTE-ACS, the 2023 ESC guideline discourages routine pretreatment.',
    'Aspirin and appropriate anticoagulation are separate treatment decisions and are not automatically deferred with the oral P2Y12 load.'),
  S('Account for Delay and the Possible Treatment Path','**Anatomy may identify a surgical indication or another diagnosis**, so unnecessary early platelet inhibition can add harm without benefit.',
    'If angiography will be substantially delayed, a different individualized pretreatment decision may be appropriate after assessing bleeding risk; the 2025 ACC/AHA guidance permits consideration of upstream clopidogrel or ticagrelor when the delay exceeds twenty-four hours.',
    'Do not transfer the rule unchanged to STEMI or concurrent fibrinolysis. After anatomy is known, select the agent and timing according to PCI, surgery or medical management, comorbidity and contraindications. Record any doses already given during transfer so a deferred strategy does not become accidental duplicate loading when the patient reaches the catheterization laboratory.')],['ESCACS','ACS'])

add('NSTE-ACS risk and invasive strategy','Choosing CABG After Stabilized NSTE-ACS',
 'A surgically suitable patient with diabetes has stabilized after NSTEMI. Angiography shows complex three-vessel disease involving the LAD, with graftable distal vessels. No ongoing instability requires immediate culprit PCI. Which revascularization plan is best supported?',
 'Heart Team assessment favoring CABG after appropriate preparation',[
 ('Complete multivessel PCI during the index hospitalization','Multivessel PCI is appropriate in selected ACS anatomy or when surgery is unsuitable, but complex three-vessel LAD disease with diabetes favors CABG in this suitable surgical candidate.'),
 ('Culprit PCI followed by medical treatment of all remaining lesions as the definitive plan','Culprit-only initial PCI is particularly important in shock; this stable patient still needs an anatomy-based plan addressing prognostically important multivessel disease.'),
 ('Culprit PCI now followed by staged nonculprit PCI after discharge','Staged PCI is an effective strategy in suitable multivessel anatomy, but it does not address why this patient’s diabetes and complex graftable disease favor selecting CABG before committing to a complete PCI pathway.')],
 [S('Select the Method Using Anatomy and Patient Factors','**CABG may be preferred in NSTE-ACS with complex multivessel disease and diabetes involving the LAD.** An acute presentation does not make multivessel PCI the automatic best definitive strategy.',
    'Assess left-main involvement, lesion complexity, ventricular function, distal targets, frailty, renal disease, surgical risk and patient preferences.',
    'A Heart Team discussion is particularly useful when the optimal method is uncertain. A recommendation for surgery assumes feasible grafting and acceptable operative risk.'),
  S('Prepare Without Losing Control of Ischemic Risk','**Timing balances the current ischemic state with operative bleeding risk.** Review aspirin, oral P2Y12 exposure and anticoagulation with the surgical team.',
    'For elective CABG, the 2025 ACC/AHA ACS table specifies clopidogrel interruption for five days, prasugrel for seven days, and ticagrelor for three to five days. Urgent surgery has a different risk balance; seek at least twenty-four hours of interruption when feasible rather than applying elective intervals as an absolute barrier to life-saving surgery.',
    'Continue evidence-based ACS and secondary prevention treatment while planning revascularization. Explain expected benefits, procedural risks and the possibility of later intervention. PCI remains an important alternative when CABG is unsuitable or the anatomy supports a percutaneous approach. The answer is therefore a patient-specific surgical preference, not a claim that every diabetic patient with any coronary stenosis requires bypass surgery. Document the anatomical and clinical reasons for the selected strategy.')],['ACS','ESCACS'])

R['COMPLETE']=('COMPLETE randomized trial, 2019','https://doi.org/10.1056/NEJMoa1907775')
R['CULPRIT']=('CULPRIT-SHOCK randomized trial, 2017','https://doi.org/10.1056/NEJMoa1710261')

add('NSTE-ACS risk and invasive strategy','Complete Revascularization After Stable STEMI',
 'After successful culprit PCI for STEMI, a patient remains stable without shock. There are severe, PCI-suitable nonculprit stenoses. Using the 2023 ESC framework, which plan best addresses the remaining coronary disease?',
 'Plan complete revascularization during the index procedure or within forty-five days',[
 ('Restrict treatment permanently to the culprit lesion unless angina recurs','Culprit-only treatment is the initial strategy in shock, but stable STEMI with suitable significant multivessel disease benefits from a planned complete strategy even without recurrent angina.'),
 ('Use same-session nonculprit PCI rather than allowing a staged completion plan','Same-session treatment can be appropriate, but excluding staged completion overstates the timing evidence; anatomy, procedural burden and clinical status determine the sequence.'),
 ('Delay any nonculprit intervention for at least three months to establish chronic stability','A long mandatory delay is not the guideline strategy; suitable complete revascularization is planned during the index procedure or within forty-five days.')],
 [S('Apply the Stable-STEMI Evidence to the Correct Population','**Complete revascularization is recommended for suitable significant multivessel disease after STEMI without cardiogenic shock.** The 2023 ESC window is the index procedure or ==within forty-five days==.',
    'Select lesions using angiographic severity and clinical context. This does not mean stenting every visible irregularity or ignoring anatomy that favors surgery.',
    'Timing should account for renal function, contrast already used, procedural complexity and the patient’s condition. A staged strategy is an active treatment plan, not an unstructured deferral.'),
  S('Understand What COMPLETE Demonstrated','**COMPLETE compared planned nonculprit PCI with culprit-only management after successful culprit PCI.** At a median three years, cardiovascular death or new MI occurred in 7.8% versus 10.5%, respectively.',
    'The hazard ratio was 0.74; this composite result should not be relabeled as proof of an isolated mortality reduction.',
    'The trial supports treating important residual disease in the studied stable population. It does not establish that every lesion must be treated immediately or that the same strategy should be used during shock. Continue antithrombotic treatment, lipid lowering and rehabilitation regardless of procedural completeness. Document which lesions remain, their significance and the planned timing so the intended staged procedure is not lost after discharge.')],['ESCACS','ACS','COMPLETE'])

add('NSTE-ACS risk and invasive strategy','Initial PCI in Infarction With Cardiogenic Shock',
 'A patient with acute MI and cardiogenic shock has a clearly identified occluded culprit artery and severe nonculprit stenoses. Culprit PCI is feasible. What is the preferred initial PCI strategy?',
 'Treat the culprit vessel now and reassess nonculprit revascularization after stabilization',[
 ('Perform routine immediate PCI of the culprit and all severe nonculprit lesions','Complete PCI is beneficial in appropriate stable patients, but routine immediate multivessel PCI during shock increases harm compared with the culprit-only initial strategy.'),
 ('Treat the largest nonculprit territory before the identified culprit vessel','A large residual ischemic territory may matter later, but it does not supersede emergency reperfusion of the clearly identified infarct-related artery in this presentation.'),
 ('Defer coronary PCI until vasopressors have fully corrected the shock','Hemodynamic support is provided alongside emergency culprit revascularization; waiting for complete resolution leaves the ischemic cause untreated.')],
 [S('Revascularize the Culprit Without Routine Additional PCI','**Cardiogenic shock changes the initial multivessel strategy.** Emergency culprit revascularization is indicated, while routine nonculprit PCI during the same procedure is discouraged.',
    'This differs from the stable-STEMI recommendation for complete revascularization. Do not extrapolate a stable-population benefit into an unstable physiological setting.',
    'Provide shock support, assess ventricular function and look for mechanical complications concurrently. Anatomy unsuitable for PCI may require emergency surgical consideration.'),
  S('Interpret CULPRIT-SHOCK and Plan Subsequent Care','**CULPRIT-SHOCK allowed staged revascularization after initial culprit-only PCI.** It therefore tested the initial strategy, not permanent abandonment of other important lesions.',
    'At thirty days, death or renal-replacement therapy occurred in 45.9% with culprit-only PCI versus 55.4% with immediate multivessel PCI; relative risk 0.83.',
    'The endpoint was a composite, and the result does not mean that nonculprit disease is harmless or that every shock presentation has an easily identifiable culprit. After stabilization, reassess residual anatomy, symptoms, ventricular recovery, renal function and suitability for PCI or CABG. Avoid adding contrast and procedural complexity merely to achieve an angiographically complete result during the emergency. The initial priority is effective culprit treatment with coordinated support and a documented plan for reassessment.')],['ACS','ESCACS','CULPRIT'])

R['SCAD']=('AHA scientific statement on spontaneous coronary artery dissection, 2018','https://pmc.ncbi.nlm.nih.gov/articles/PMC5957087/')

add('NSTE-ACS risk and invasive strategy','Conservative Management of Stable SCAD',
 'Angiography confirms mid-distal LAD spontaneous coronary artery dissection in a patient whose pain has resolved. Distal flow is preserved, there is no left-main involvement, and hemodynamics and serial ECGs are stable. Which initial strategy is most appropriate?',
 'Monitored conservative management with reassessment for recurrent ischemia',[
 ('Immediate long-segment stenting to seal the entire dissection','PCI may be needed for ongoing ischemia with threatened myocardium and impaired flow, but routine long-segment stenting adds technical risk in a stable, well-perfused dissection.'),
 ('Immediate CABG for the dissected LAD','CABG is considered for selected high-risk anatomy or failed or unsuitable PCI with ongoing ischemia; LAD involvement alone does not justify surgery in this stable distal lesion.'),
 ('Repeat angiography with intravascular imaging before selecting conservative treatment','Intravascular imaging can clarify uncertain diagnoses when it changes management, but unnecessary instrumentation of an already established stable SCAD can propagate injury.')],
 [S('Allow Healing When Perfusion and Clinical Stability Permit','**Conservative management is generally preferred in stable SCAD with preserved distal flow and no ongoing ischemia.** Intramural hematoma and arterial-wall disruption differ from a straightforward plaque stenosis.',
    'Many lesions heal spontaneously. Hospital observation and serial assessment remain important because early extension or recurrent ischemia can occur.',
    'PCI can enter the false lumen, propagate hematoma or require extensive stenting. These procedural hazards explain why angiographic narrowing alone does not establish benefit from intervention.'),
  S('Identify the Exceptions and Individualize Medical Treatment','**Ongoing ischemia, impaired flow, hemodynamic instability or high-risk proximal anatomy prompts urgent specialist reassessment.** The procedure chosen depends on the anatomy and feasibility.',
    'The 2023 ESC recommendation limits PCI to SCAD with ongoing ischemic features, substantial myocardium at risk and reduced antegrade flow. Selected left-main or proximal multivessel disease may require CABG.',
    'Review antithrombotic treatment after the mechanism is established. The AHA statement advises considering discontinuation of systemic anticoagulation without another indication; antiplatelet strategy in conservatively managed SCAD has limited evidence and should not be presented as a universally proven regimen. Stented patients require appropriate stent-directed antiplatelet care. Assess ventricular function, provide individualized rehabilitation and arrange evaluation for associated arteriopathy, including fibromuscular dysplasia. Persistent or recurrent symptoms require clinical assessment rather than automatic attribution to either reinfarction or benign recovery.')],['ESCACS','SCAD'])

add('Antiplatelet anticoagulant and bleeding decisions','Aspirin Loading and Maintenance in ACS',
 'A patient with confirmed ACS can swallow and has no aspirin hypersensitivity or active bleeding. No loading dose has been given. Under the 2025 ACC/AHA guideline, which oral regimen is appropriate?',
 'Aspirin 162–325 mg initially, followed by 75–100 mg daily',[
 ('Aspirin 75–100 mg initially, followed by 75–100 mg daily','Low-dose aspirin is suitable maintenance treatment, but a larger initial loading dose is recommended to establish prompt platelet inhibition during ACS.'),
 ('Aspirin 162–325 mg initially, followed by 325 mg daily as the preferred maintenance dose','The initial loading range is appropriate, but prolonged full-dose aspirin is not the preferred maintenance strategy and adds bleeding burden without established superior ACS protection.'),
 ('Aspirin 75–100 mg initially, followed by 325 mg daily','This reverses the intended loading and maintenance approach: the acute phase requires a loading dose, while subsequent treatment generally uses low-dose aspirin.')],
 [S('Separate Rapid Platelet Inhibition From Maintenance','**Aspirin irreversibly inhibits platelet cyclooxygenase-1 and thromboxane production.** The 2025 ACC/AHA ACS regimen is an oral load of ==162–325 mg== followed by ==75–100 mg daily==.',
    'Use a nonenteric-coated preparation for prompt absorption; chewing the initial dose accelerates its effect when oral administration is suitable.',
    'A history of low-dose aspirin use does not automatically remove the guideline loading recommendation. Confirm what was actually administered during transfer to prevent undocumented duplicate doses.'),
  S('Integrate Aspirin With the Rest of ACS Treatment','**Aspirin and a P2Y12 inhibitor act at different platelet pathways.** The accompanying agent and treatment duration depend on reperfusion strategy, bleeding risk and other indications for anticoagulation.',
    'Active pathological bleeding or a serious hypersensitivity history requires an alternative specialist plan. Gastrointestinal risk should prompt assessment and appropriate gastroprotection rather than indiscriminate high-dose maintenance.',
    'Low-dose maintenance provides effective thromboxane suppression. Trials have not established superior clinical protection from maintaining the acute loading range, and some ACS comparisons showed more gastrointestinal or minor bleeding with higher doses. Reassess the regimen when bleeding occurs or oral anticoagulation is needed; the initial recommendation does not imply that aspirin must continue unchanged through every later combination strategy. Give clear discharge instructions distinguishing the loading dose already received from the ongoing daily dose.')],['ACS'],style='direct')

add('Antiplatelet anticoagulant and bleeding decisions','P2Y12 Selection After a Previous Ischemic Stroke',
 'A 62-year-old patient weighing 76 kg undergoes PCI for NSTEMI. There was an ischemic stroke five years earlier, without intracranial hemorrhage. Bleeding risk is not high, oral anticoagulation is unnecessary, and ticagrelor is tolerated and affordable. Which oral P2Y12 regimen is preferred among these choices?',
 'Ticagrelor 180 mg loading, then 90 mg twice daily',[
 ('Prasugrel 60 mg loading, then 10 mg daily','This is a standard prasugrel regimen in appropriately selected PCI patients, but any previous stroke or TIA makes prasugrel unsuitable because of adverse net clinical outcomes.'),
 ('Clopidogrel 600 mg loading, then 75 mg daily','Clopidogrel is a reasonable alternative when potent agents are unsuitable, bleeding risk is high or anticoagulation is required; the stated eligible PCI patient favors ticagrelor over clopidogrel.'),
 ('Ticagrelor 180 mg loading, then 60 mg twice daily','The 60 mg twice-daily dose is used in selected extended secondary prevention settings after the first year; it is not the standard initial ACS maintenance dose.')],
 [S('Distinguish Ischemic Stroke From Intracranial Hemorrhage','**Previous stroke or TIA excludes prasugrel**, irrespective of the reassuring age and weight in this vignette. Reducing the prasugrel dose does not remove that restriction.',
    'A remote ischemic stroke is not the same contraindication as previous intracranial hemorrhage for ticagrelor. Review the actual diagnosis rather than accepting an unspecified history of stroke.',
    'For an eligible ACS patient undergoing PCI, the 2025 ACC/AHA guideline favors ticagrelor or prasugrel over clopidogrel; the prior stroke directs selection away from prasugrel.'),
  S('Prescribe and Monitor the Selected Agent','**The initial ACS ticagrelor regimen is a 180 mg load followed by 90 mg twice daily.** Check prior loading during transfer before prescribing another dose.',
    'Monitor bleeding, dyspnea and clinically important bradyarrhythmia. Review strong CYP3A inhibitors or inducers and adherence to twice-daily treatment.',
    'Active pathological bleeding or previous intracranial hemorrhage precludes ticagrelor. Clopidogrel remains useful when the balance of bleeding, tolerability, drug interactions, cost or concurrent anticoagulation favors it. Prasugrel additionally requires caution in older or low-weight patients: its age and weight dose considerations apply only after contraindications are excluded. Combine the selected agent with low-dose aspirin initially unless a specific alternative strategy is indicated, and reassess duration as ischemic and bleeding risks evolve. The question concerns the initial post-PCI choice, not a universal commitment to unchanged dual therapy indefinitely.')],['ACS'])

add('Antiplatelet anticoagulant and bleeding decisions','Prasugrel Loading for Primary PCI',
 'A 58-year-old, 82-kg patient with STEMI is proceeding directly to primary PCI without fibrinolysis. Prasugrel has been selected after contraindication screening. No P2Y12 inhibitor has been administered. Which regimen is appropriate?',
 'Prasugrel 60 mg loading, followed by 10 mg daily',[
 ('Prasugrel 10 mg initially, followed by 10 mg daily','Ten milligrams is the usual maintenance dose in this age and weight group; using it alone initially omits the loading dose needed for prompt platelet inhibition.'),
 ('Prasugrel 60 mg loading, followed by 5 mg daily','Five-milligram maintenance is considered for low weight or older age with caution; neither dose-reduction feature is present in the stated patient.'),
 ('Prasugrel 30 mg loading, followed by 10 mg daily','Thirty milligrams is not the standard guideline prasugrel loading regimen for this eligible primary-PCI presentation; it should not be inferred by halving another regimen.')],
 [S('Match the Regimen to the Reperfusion Strategy','**For eligible ACS patients undergoing PCI, prasugrel is loaded at 60 mg orally.** In a patient younger than seventy-five years and weighing at least sixty kilograms, the usual maintenance dose is ==10 mg daily==.',
    'Exclude previous stroke or TIA and active pathological bleeding before prescribing. A contraindication cannot be corrected merely by reducing the dose.',
    'Age at least seventy-five years or body weight below sixty kilograms requires separate caution and dose consideration; do not apply these adjustments to every patient.'),
  S('Keep Primary PCI Distinct From Concurrent Fibrinolysis','**Prasugrel for primary PCI is not the standard oral adjunct administered with fibrinolysis.** Clopidogrel is used in the concurrent lytic pathway, with its own age-dependent loading approach.',
    'Later PCI after fibrinolysis is a separate decision involving elapsed time, age, previous treatment and the selected guideline. Avoid treating a subsequent switch as permission to use any potent agent at the lytic bolus.',
    'Check swallowing, absorption concerns and prior doses. Shock, vomiting or opioid exposure may delay oral drug effect; specialist intravenous antiplatelet treatment may be appropriate in selected circumstances. Continue bleeding surveillance and clear medication reconciliation through transfer. The choice among prasugrel, ticagrelor and clopidogrel depends on contraindications, reperfusion strategy and bleeding risk, while loading and maintenance are distinct prescribing steps. Do not mistake a correctly selected maintenance dose for adequate acute loading.')],['ACS'])

R['ENOX']=('Lovenox prescribing information, renal and geriatric STEMI dosing','https://www.dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=5017a927-2a24-4f27-89f9-27c805bf7d59')

add('Antiplatelet anticoagulant and bleeding decisions','Enoxaparin When Age and Renal Adjustments Intersect',
 'A 78-year-old patient receiving fibrinolysis for eligible STEMI weighs 70 kg and has a creatinine clearance of 24 mL/min. Enoxaparin is selected under its labeled STEMI regimen. Which initial schedule is appropriate?',
 'No intravenous bolus; 70 mg subcutaneously every twenty-four hours',[
 ('No intravenous bolus; 52.5 mg subcutaneously every twelve hours','This applies the older-patient 0.75 mg/kg twice-daily regimen without making the additional severe-renal-impairment adjustment required at this creatinine clearance.'),
 ('A 30 mg intravenous bolus; 70 mg subcutaneously every twenty-four hours','The once-daily renal adjustment is appropriate, but the initial intravenous bolus is omitted in STEMI patients at least seventy-five years old.'),
 ('No intravenous bolus; 70 mg subcutaneously every twelve hours','This preserves excessive dosing frequency for a creatinine clearance below thirty; omitting the bolus alone does not address renal accumulation.')],
 [S('Apply Both Adjustments to the Correct Indication','**The labeled STEMI regimen for age at least seventy-five years with creatinine clearance below thirty is 1 mg/kg subcutaneously once daily, without an intravenous bolus.** For seventy kilograms, this is ==70 mg every twenty-four hours==.',
    'Without severe renal impairment, the older-patient STEMI regimen is 0.75 mg/kg every twelve hours without a bolus, with a seventy-five-milligram cap on each of the first two subcutaneous doses.',
    'Do not simply combine the older-patient dose with the usual twelve-hour frequency when severe renal impairment is present. The renal table supplies the appropriate combined regimen.'),
  S('Monitor Accumulation and Coordinate Subsequent Procedures','**Enoxaparin potentiates antithrombin-mediated factor Xa inhibition and has clinically important renal clearance.** Review weight, calculated creatinine clearance, blood count, platelets and bleeding before dosing.',
    'Avoid using an indexed eGFR number interchangeably with the creatinine-clearance dosing criterion without assessing the patient and the estimation method.',
    'Monitor changing renal function and overt or occult bleeding. Unfractionated heparin may be selected in some patients when rapid titration or reversibility is advantageous; that choice does not alter the labeled enoxaparin answer requested here. If PCI follows, document the exact last dose and time so procedural anticoagulation is selected safely. Prior heparin-induced thrombocytopenia or active major bleeding requires a different plan. Antiplatelet therapy and fibrinolytic age adjustments are separate decisions and must also be checked rather than inferred from the anticoagulant prescription.')],['ENOX','ACS'],table=(['STEMI fibrinolysis setting','Enoxaparin regimen','Initial qualification'],[
 ['Age <75; CrCl ≥30 mL/min','30 mg IV, then 1 mg/kg SC every 12 h','First two SC doses maximum 100 mg each'],
 ['Age ≥75; CrCl ≥30 mL/min','0.75 mg/kg SC every 12 h','No IV bolus; first two SC doses maximum 75 mg each'],
 ['Age <75; CrCl <30 mL/min: labeled STEMI regimen','30 mg IV plus 1 mg/kg SC, then 1 mg/kg SC every 24 h','Renal adjustment changes SC frequency; initial IV bolus retained in this age group'],
 ['Age ≥75; CrCl <30 mL/min','1 mg/kg SC every 24 h','No IV bolus'],
 ['UFH alternative: ACC/AHA 2025','60 units/kg IV then 12 units/kg/hour','Bolus maximum 4000 units; initial infusion maximum 1000 units/hour; adjust to therapeutic aPTT']]))

R['FUTURA']=('FUTURA/OASIS-8 randomized trial, 2010','https://doi.org/10.1001/jama.2010.1320')

add('Antiplatelet anticoagulant and bleeding decisions','PCI After Upstream Fondaparinux',
 'A patient with NSTE-ACS received fondaparinux while awaiting delayed angiography. Renal function is adequate and there is no heparin-induced thrombocytopenia. Angiography now identifies a lesion requiring PCI. Which anticoagulation step is appropriate?',
 'Administer a procedural intravenous UFH bolus in addition to the prior fondaparinux',[
 ('Proceed with fondaparinux as the sole procedural anticoagulant','Fondaparinux is useful upstream in selected NSTE-ACS patients, but alone it does not provide adequate catheter-related thrombotic protection during PCI.'),
 ('Give an additional subcutaneous fondaparinux dose immediately before PCI','Repeating the upstream drug does not replace the recommended procedural UFH bolus and may increase bleeding without addressing the relevant procedural limitation.'),
 ('Start a ward-dose UFH infusion and postpone the procedural bolus until after PCI','A UFH infusion is useful in selected upstream ACS pathways, but this patient now requires procedural anticoagulation; postponing the bolus leaves the catheterization phase inadequately covered.')],
 [S('Recognize the Transition From Upstream Treatment to PCI','**Fondaparinux requires additional UFH when a treated NSTE-ACS patient proceeds to PCI.** The 2023 ESC guideline specifies a full-dose procedural bolus because guiding-catheter thrombosis is a concern.',
    'Fondaparinux indirectly inhibits factor Xa through antithrombin. Its upstream efficacy does not establish that it can be used alone for every invasive procedure.',
    'The principle is deliberate procedural supplementation, not indiscriminate switching among anticoagulants throughout admission.'),
  S('Coordinate the Procedural Prescription','**Use the catheterization protocol and activated clotting-time assessment where appropriate.** Account for body weight, other anticoagulants, bleeding risk and planned glycoprotein IIb/IIIa use.',
    'The FUTURA/OASIS-8 standard-dose strategy used UFH 85 units/kg, reduced to 60 units/kg with a glycoprotein IIb/IIIa inhibitor; distinguish this trial protocol from a universal unqualified dose for all PCI situations.',
    'Record the timing of prior fondaparinux and communicate it to the procedural team. Check renal function and contraindications before the upstream prescription and reassess if the clinical state changes. Antiplatelet treatment remains a separate component of PCI care. After an uncomplicated procedure, continued parenteral anticoagulation requires a specific indication rather than automatic continuation of every drug administered before catheterization. The key decision is to preserve appropriate upstream treatment while adding the anticoagulant coverage required for the invasive phase.')],['ESCACS','FUTURA'])

add('Antiplatelet anticoagulant and bleeding decisions','DAPT Duration After ACS Is a Risk-Based Prescription',
 'An ACS patient has undergone uncomplicated PCI and is preparing for discharge on aspirin plus ticagrelor. There is no high bleeding risk or oral anticoagulation indication. What is the default duration framework under the 2025 ACC/AHA guideline?',
 'Plan at least twelve months of DAPT, with reassessment if the risk balance changes',[
 ('Plan one month of DAPT followed by aspirin alone','An abbreviated strategy can be appropriate in selected high-bleeding-risk patients, but it is not the default for this stated lower-bleeding-risk ACS presentation.'),
 ('Plan six months of DAPT followed by aspirin alone','Six-month courses apply in selected coronary contexts and individualized bleeding-risk strategies, but the named lower-bleeding-risk ACS default remains at least one year.'),
 ('Plan thirty-six months of DAPT from discharge','Extended treatment can benefit selected prior-MI patients with favorable ischemic-to-bleeding balance, but it requires reassessment and is not the default duration for every ACS patient.')],
 [S('Begin With the ACS Default and Reassess','**The 2025 ACC/AHA default is aspirin plus an oral P2Y12 inhibitor for at least twelve months in ACS without high bleeding risk.** This addresses recurrent ischemic events as well as stent thrombosis.',
    'Record bleeding history, anemia, renal dysfunction, concomitant drugs and anticipated procedures. Risk changes during follow-up, so the discharge plan needs explicit review.',
    'A minimum default is not a command to continue both agents through major bleeding, nor proof that every patient benefits from extension beyond one year.'),
  S('Distinguish Evidence-Based Bleeding Reduction Strategies','**Selected patients can transition to a different regimen without abandoning antiplatelet protection.** The agent retained and the timing matter.',
    'For patients who have tolerated ticagrelor-based DAPT, the 2025 guideline supports ticagrelor monotherapy at least one month after PCI to reduce bleeding. This means withdrawing aspirin while continuing ticagrelor, not stopping both agents.',
    'In high-bleeding-risk ACS PCI patients, single antiplatelet therapy after one month may be reasonable under the named framework. These strategies are not interchangeable with immediate aspirin withdrawal at the procedure, unguided early switching or a universal one-month course. Use a proton pump inhibitor when gastrointestinal bleeding risk warrants it. Explain adherence and the need to consult the treating team before interruption, especially early after stenting. A new anticoagulation indication requires its own combination strategy rather than simply adding another drug to unchanged DAPT.')],['ACS'])

add('Antiplatelet anticoagulant and bleeding decisions','Antithrombotic Therapy When AF Coexists With ACS PCI',
 'A patient with atrial fibrillation requiring long-term anticoagulation has uncomplicated PCI for ACS. There is no mechanical valve, significant mitral stenosis or exceptionally high stent-thrombosis risk. Under the 2025 ACC/AHA framework, which planned sequence is preferred?',
 'Brief triple therapy, then stop aspirin at one to four weeks and continue anticoagulation plus clopidogrel',[
 ('Continue anticoagulation, aspirin and clopidogrel together for twelve months','Prolonged triple therapy adds substantial bleeding risk; the usual strategy limits aspirin exposure while retaining anticoagulation and a P2Y12 inhibitor.'),
 ('Stop anticoagulation after PCI and use aspirin plus clopidogrel for twelve months','DAPT protects against coronary events but does not replace indicated anticoagulation for AF-related cardioembolic stroke prevention.'),
 ('Stop clopidogrel at one week and continue anticoagulation plus aspirin','The recommended early aspirin-withdrawal strategy retains a P2Y12 inhibitor, preferably clopidogrel; aspirin is not the usual agent retained in its place.')],
 [S('Treat Two Thrombotic Indications With the Fewest Necessary Agents','**AF-related embolic prevention and post-PCI platelet inhibition have distinct indications.** Neither DAPT nor anticoagulation alone automatically supplies all early post-ACS protection.',
    'The 2025 ACC/AHA guideline recommends stopping aspirin after ==one to four weeks== of triple therapy, continuing an oral anticoagulant plus a P2Y12 inhibitor, preferably clopidogrel.',
    'Choose the exact aspirin stop date according to bleeding and stent-thrombosis risks. The stated uncomplicated case does not supply a reason for prolonged triple therapy.'),
  S('Preserve Appropriate Anticoagulation and Follow-Up','**For eligible AF patients, a DOAC is generally preferred over a vitamin K antagonist.** Use the indicated stroke-prevention dose with its validated renal, age, weight and interaction adjustments.',
    'Do not substitute the low vascular-prevention rivaroxaban dose for therapeutic AF anticoagulation. Mechanical valves and significant mitral stenosis require a separate anticoagulant assessment.',
    'Reassess hemoglobin, renal function, adherence and gastrointestinal protection. Explain which drug stops and on what date: vague instructions to reduce blood thinners can cause the wrong agent to be withdrawn. The duration of subsequent anticoagulant-plus-clopidogrel treatment is individualized, commonly through the first post-ACS year, followed by reassessment for anticoagulant monotherapy. Recurrent ischemia, bleeding or repeat intervention can change that plan. Different society frameworks use somewhat different default early aspirin windows, so attribute the one-to-four-week interval to the named guideline rather than presenting it as an identical universal rule.')],['ACS'])

R['GIBLEED']=('BSG/ESGE antithrombotic and endoscopy guideline update, 2021','https://pmc.ncbi.nlm.nih.gov/articles/PMC8390296/')

add('Antiplatelet anticoagulant and bleeding decisions','Major Gastrointestinal Bleeding Soon After Coronary Stenting',
 'Ten days after ACS stenting, a patient on aspirin and clopidogrel develops a major upper gastrointestinal bleed. Resuscitation is underway and endoscopic hemostasis is being arranged. Which antiplatelet principle is most appropriate?',
 'Coordinate urgently with interventional cardiology, preserve aspirin if feasible, and minimize any necessary P2Y12 interruption',[
 ('Withhold both antiplatelets until a repeat endoscopy documents ulcer healing','Temporary interruption may be necessary in uncontrolled life-threatening hemorrhage, but requiring complete ulcer healing before resumption creates excessive early stent risk; coordinate the shortest necessary interruption after source control.'),
 ('Stop clopidogrel for two weeks while continuing aspirin and treating the bleeding source','Preserving aspirin can be appropriate, but a predetermined two-week P2Y12 interruption is longer than the named guideline framework for a still-indicated recent-stent agent; plan early reassessment and reinstatement.'),
 ('Stop aspirin permanently and continue clopidogrel alone as the immediate default','P2Y12 monotherapy is used in selected planned post-PCI strategies, but this acute major-bleeding presentation ten days after stenting requires coordinated hemostasis and individualized interruption rather than automatic permanent aspirin withdrawal.')],
 [S('Control Hemorrhage While Recognizing Very Early Stent Risk','**Resuscitation and source control proceed urgently.** Recent coronary stenting makes antiplatelet interruption hazardous, so involve the interventional cardiologist at the same time as the endoscopy team.',
    'The BSG/ESGE 2021 framework favors continuing DAPT when possible in patients with coronary stents. If major hemorrhage requires P2Y12 interruption, continue aspirin if feasible.',
    'This is not an instruction to continue every agent through uncontrolled life-threatening bleeding. Severity, hemostatic success and the coronary anatomy determine the immediate individualized plan.'),
  S('Write an Explicit Restart and Prevention Plan','**If still indicated, reinstate the P2Y12 inhibitor within five days under the named guidance.** This is a maximum interruption framework, not a reason to wait five days after secure hemostasis when earlier resumption is appropriate.',
    'Assess the endoscopic lesion, recurrent bleeding risk, hemoglobin trend and coronary risk with both teams. Use appropriate proton pump inhibitor treatment and address ulcer causes.',
    'Record the last doses, the reason for interruption, which agent continues and the intended reassessment time. A temporary hold without a restart owner can become an unintended permanent withdrawal. Heparin bridging does not replace the antiplatelet mechanism needed for a recent stent. Once stabilized, review whether the longer-term regimen can be adjusted to reduce bleeding while maintaining coronary protection. The decision is a coordinated treatment sequence rather than choosing hemorrhage or thrombosis as the only relevant danger.')],['GIBLEED','ACS'])

add('Early infarct care and mechanical electrical complications','Recent Tadalafil Exposure During ACS',
 'An ACS patient has continuing ischemic discomfort, blood pressure 138/82 mm Hg and oxygen saturation 97% on room air. Tadalafil was taken eighteen hours earlier. Which immediate supportive-treatment plan is appropriate while definitive ACS care proceeds?',
 'Withhold nitrates and reassess pain and perfusion while expediting indicated coronary treatment',[
 ('Give sublingual nitroglycerin because the current blood pressure is normal','Normal baseline pressure does not remove the nitrate–PDE5 inhibitor interaction; tadalafil exposure within forty-eight hours makes nitrate-associated hypotension a serious concern.'),
 ('Use intravenous nitroglycerin because titration avoids the oral drug interaction','The interaction is pharmacodynamic and persists with intravenous nitrate delivery; changing the route does not remove excessive cyclic-GMP-mediated vasodilation.'),
 ('Give high-flow oxygen as the principal anti-ischemic treatment at the stated saturation','Supplemental oxygen treats hypoxemia, but routine use at this normal saturation has no established benefit and does not substitute for addressing continuing coronary ischemia.')],
 [S('Screen for Vasodilator Interactions Before Giving Nitrates','**Nitrates increase cyclic GMP, while PDE5 inhibition reduces its breakdown.** Combined exposure can produce profound hypotension despite an initially reassuring blood pressure.',
    'The 2025 ACC/AHA ACS framework avoids nitrates within ==forty-eight hours of tadalafil==, twenty-four hours of sildenafil or vardenafil, and twelve hours of avanafil.',
    'Also assess suspected right ventricular infarction, systolic pressure below ninety or a fall greater than thirty millimeters of mercury from baseline. Nitrate eligibility requires more than the absence of one contraindication.'),
  S('Treat Persistent Ischemia Without Relying on Symptom Suppression','**Continuing ischemic discomfort requires reassessment of ECG, hemodynamics and the invasive or reperfusion plan.** Analgesia must not delay treatment of the cause.',
    'At oxygen saturation below ninety percent, give oxygen to correct hypoxemia; routine supplemental oxygen is not recommended for the normally saturated patient described here.',
    'Opioids may be considered selectively for severe pain unresponsive to other suitable measures, but can cause hypotension, respiratory depression and delayed absorption of oral P2Y12 drugs. Relief of pain does not prove reperfusion. When nitrates are otherwise suitable, sublingual nitroglycerin is commonly 0.3–0.4 mg every five minutes for up to three doses, with monitoring and further treatment based on response. Those usual doses remain inappropriate during the tadalafil interaction window. Record the drug and time of exposure explicitly so another clinician does not inadvertently administer a nitrate during transfer.')],['ACS'])

add('Early infarct care and mechanical electrical complications','Defer Early Beta Blockade During Low Output',
 'After anterior MI, a patient has heart rate 112/min, blood pressure 92/64 mm Hg, cool extremities and pulmonary congestion. No beta blocker has been administered. Which approach is appropriate?',
 'Defer beta-blocker initiation, treat the unstable state, and reassess after stabilization',[
 ('Give intravenous metoprolol promptly to correct the tachycardia','Intravenous beta blockade can worsen low output or precipitate shock; tachycardia in this setting may be compensatory rather than an isolated treatment target.'),
 ('Start low-dose oral metoprolol now with close blood-pressure monitoring','Low-dose oral initiation is appropriate after contraindications resolve, but the current low-output features and acute congestion make even cautious immediate initiation unsuitable.'),
 ('Start carvedilol now to obtain its longer-term ventricular-remodeling benefit','Carvedilol benefits selected stable reduced-EF patients, but negative inotropy and vasodilation can worsen this acute hypoperfused state; long-term benefit does not remove the need for stabilization.')],
 [S('Recognize Compensatory Tachycardia and Shock Risk','**Acute heart failure and low-output features are reasons to defer initiation of beta blockade.** A fast pulse does not establish that reducing it immediately will improve cardiac output.',
    'Assess perfusion, congestion, ventricular function, ongoing ischemia and mechanical complications. Provide appropriate stabilization and coronary treatment.',
    'Negative inotropy and reduced chronotropic support can worsen an already compromised circulation. Intravenous dosing does not bypass this physiological risk.'),
  S('Reassess Eligibility After the Acute Contraindication Resolves','**The 2025 ACC/AHA guideline recommends early oral beta blockers in ACS without contraindications.** Begin at a low dose with cautious titration when blood pressure, perfusion and heart rate permit.',
    'Other barriers include severe bradycardia, advanced AV block without pacing, active bronchospasm and marked PR prolongation. The traditional PR threshold is 0.24 seconds, equivalent to 240 milliseconds.',
    'Reassess initially ineligible patients rather than documenting a permanent class prohibition. Stabilized reduced-EF heart failure is different from the acute low-output state in this stem and supports an evidence-based beta blocker when tolerated. Monitor blood pressure, pulse, congestion and conduction after initiation. The appropriate drug and titration depend on ventricular function and comorbidity. Avoid conflating this acute safety decision with the separate question of indefinite beta-blocker treatment after an uncomplicated preserved-EF infarct. The indication, timing and duration each require their own assessment.')],['ACS'])

R['HF2022']=('AHA/ACC/HFSA heart failure guideline, 2022','https://doi.org/10.1016/j.jacc.2021.12.012')
R['CCS2021']=('Canadian Cardiovascular Society HFrEF guideline, 2021: standard therapies','https://ccs.ca/guideline/2021-heart-failure-reduced-ef/chapter-2-standard-therapies/')

R['EPLER']=('Eplerenone prescribing information: post-MI dosing and monitoring','https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9b66a393-8af1-42bc-9673-89fe471147ee')
R['PARADISE']=('PARADISE-MI randomized trial, 2021','https://doi.org/10.1056/NEJMoa2104508')

add('Early infarct care and mechanical electrical complications','Mineralocorticoid Antagonism After MI With Diabetes',
 'A stabilized patient five days after MI has LVEF 38% and diabetes, without current pulmonary congestion. Blood pressure is 118/72 mm Hg, eGFR 62 mL/min/1.73 m² and potassium 4.3 mmol/L. An ACE inhibitor and appropriate beta blocker are tolerated. Which additional treatment is supported?',
 'Add eplerenone with potassium and renal-function monitoring',[
 ('Withhold an MRA because heart-failure symptoms are absent today','Post-MI diabetes with LVEF at most forty percent supports MRA treatment even without current HF symptoms, provided renal function and potassium permit.'),
 ('Replace the ACE inhibitor with eplerenone rather than combining them','An MRA complements tolerated renin–angiotensin inhibition in eligible patients; it is not a routine substitute for the ACE inhibitor solely to avoid combination treatment.'),
 ('Replace the ACE inhibitor with sacubitril–valsartan as the preferred post-MI addition','Sacubitril–valsartan has an established role in appropriate symptomatic HFrEF, but PARADISE-MI did not demonstrate significant superiority over ramipril for its primary endpoint after acute MI; it does not replace the specific additional MRA indication here.')],
 [S('Use the Post-Infarct Eligibility Framework','**After MI, LVEF at most forty percent with heart failure or diabetes supports mineralocorticoid receptor antagonism when safe.** Absence of congestion at this examination does not exclude the diabetic patient described here.',
    'Eplerenone blocks aldosterone-mediated sodium retention and adverse remodeling. Its benefit is additional to other indicated post-infarct therapy.',
    'Assess hemodynamic stability and review renal function, potassium and interacting drugs before initiation rather than selecting treatment from EF alone.'),
  S('Initiate Safely and Recheck Laboratory Results','**Under the 2022 AHA/ACC/HFSA safety framework, initiate an MRA when eGFR is greater than thirty and potassium below 5.0.** The question’s values satisfy these boundaries.',
    'With adequate renal function, start eplerenone at ==25 mg daily== and titrate toward ==50 mg daily==, preferably within four weeks if tolerated. Reduced renal function can require a lower starting schedule.',
    'Measure potassium before treatment, within the first week and one month after initiation or dose adjustment, then periodically. Review renal function alongside potassium and recheck during dehydration, acute illness or interacting-drug changes. Avoid unnecessary potassium supplements and review NSAIDs and other potassium-raising medicines. Strong CYP3A inhibitors are contraindicated with eplerenone; moderate inhibitors can require dose limitation. Continue indicated ACE inhibitor or ARB therapy with monitoring rather than combining an ACE inhibitor and ARB. Persistent hyperkalemia requires dose adjustment or withdrawal according to the treatment protocol.')],['ACS','HF2022','CCS2021','EPLER','PARADISE'])

R['MECH']=('AHA scientific statement on mechanical complications of MI, 2021','https://pmc.ncbi.nlm.nih.gov/articles/PMC9364424/')

add('Early infarct care and mechanical electrical complications','Papillary Muscle Rupture After Inferior MI',
 'Three days after inferior MI, a patient abruptly develops pulmonary edema and shock. A soft apical systolic murmur is heard. Echocardiography shows a flail mitral leaflet with a mobile attached subvalvular structure and severe eccentric regurgitation; no septal shunt is present. What is the most likely diagnosis?',
 'Papillary muscle rupture causing acute severe mitral regurgitation',[
 ('Ischemic leaflet tethering from ventricular remodeling','Functional ischemic MR results from altered ventricular geometry and leaflet restriction; an acutely flail leaflet with an attached disrupted subvalvular structure supports rupture instead.'),
 ('Post-infarct ventricular septal rupture','Septal rupture produces an interventricular left-to-right shunt, often with a harsh parasternal murmur; imaging here demonstrates mitral apparatus disruption without that shunt.'),
 ('Dynamic outflow obstruction with systolic anterior mitral motion','Dynamic obstruction can cause shock and MR, but echocardiography would show systolic anterior motion and an outflow gradient rather than a flail apparatus from rupture.')],
 [S('Recognize Acute Structural Mitral Failure','**Papillary muscle rupture causes abrupt severe MR, pulmonary edema and circulatory collapse.** The posteromedial muscle is particularly vulnerable because its arterial supply is usually less redundant.',
    'A loud murmur is not required: rapid left ventricular–atrial pressure equalization can make the murmur short or soft despite catastrophic regurgitation.',
    'Transthoracic echocardiography is urgent. Use transesophageal imaging when the mechanism or severity is inadequately defined, without allowing additional imaging to delay necessary stabilization and surgical coordination.'),
  S('Stabilize as a Bridge to Definitive Treatment','**Activate cardiac surgery and the shock team immediately.** Acute rupture is a surgical emergency, commonly requiring mitral replacement; selected partial ruptures may be repairable.',
    'Support oxygenation and perfusion. Afterload reduction may help when pressure permits, while hypotension requires individualized vasoactive and mechanical-support decisions.',
    'Temporary mechanical support may bridge a selected patient to surgery, but is not definitive treatment for the disrupted valve apparatus. Transcatheter edge-to-edge repair is a specialized alternative in selected prohibitive-risk patients rather than a universal replacement for surgery. Distinguish structural rupture from functional ischemic MR because their mechanisms and procedural decisions differ. Reassess coronary anatomy and the need for concomitant revascularization with the surgical team. Do not attribute sudden post-infarct edema solely to infarct size when the clinical course suggests a mechanical event.')],['MECH','ACS'])

add('Early infarct care and mechanical electrical complications','Shunt Physiology in Post-Infarct Septal Rupture',
 'Four days after MI, a patient develops hypotension and a new harsh left parasternal systolic murmur with a thrill. Oxygen saturation rises from 61% in the right atrium to 82% in the right ventricle. Which complication best explains these findings?',
 'Ventricular septal rupture with left-to-right shunting',[
 ('Papillary muscle rupture with acute mitral regurgitation','Acute MR causes pulmonary venous hypertension and edema, but does not directly introduce oxygenated LV blood into the right ventricle to produce the stated step-up.'),
 ('Left ventricular free-wall rupture with tamponade','Free-wall rupture causes hemopericardium and impaired filling, often with collapse or PEA; it does not produce a ventricular-level oxygen saturation step-up.'),
 ('Isolated right ventricular infarction','RV infarction can cause hypotension and elevated venous pressure, but does not create a new LV-to-RV shunt with a harsh thrill-producing murmur.')],
 [S('Localize the Abnormal Flow','**A new ventricular-level oxygen saturation step-up indicates entry of oxygenated blood into the right ventricle.** In this post-infarct setting, the murmur and hemodynamic deterioration strongly support septal rupture.',
    'The left-to-right shunt increases pulmonary flow and RV volume burden while reducing effective systemic output. Infarct-related dysfunction can compound the shock.',
    'Urgent echocardiography with color Doppler defines the defect, shunt, ventricular function and associated valve or pericardial abnormalities. Catheter data can support physiology but must not delay an already urgent diagnosis.'),
  S('Coordinate Closure and Stabilization','**Activate cardiac surgery and the shock team promptly.** Definitive treatment generally requires closure; medical support alone does not repair the structural defect.',
    'Refractory shock or pulmonary edema requires urgent intervention. In selected stabilized patients, timing can be individualized to balance ongoing shunt risk against friable infarct tissue.',
    'Do not claim that all patients must wait a fixed number of weeks: apparent advantages of delayed surgery in observational cohorts are affected by survival and selection bias. Temporary mechanical support may provide a bridge in selected patients, with device choice guided by shunt physiology and ventricular function. Percutaneous closure is an option in selected anatomy, residual defects or patients unsuitable for surgery, requiring specialist assessment. Communicate whether instability is persistent or controlled, because that distinction determines whether a bridging strategy is feasible. The oxygen step-up identifies the mechanism; the patient’s trajectory determines urgency.')],['MECH','ACS'],table=(['Complication','Key physiology','Urgent imaging clue'],[
 ['Septal rupture','LV-to-RV shunt; ventricular oxygen step-up','Color Doppler flow across disrupted septum'],
 ['Papillary muscle rupture','Acute MR; pulmonary venous hypertension','Flail mitral apparatus and severe often eccentric MR'],
 ['Free-wall rupture','Hemopericardium; tamponade; possible PEA','Pericardial blood/clot with compressive physiology']]))

R['TAMP']=('ESC position statement on urgent tamponade management, 2014','https://doi.org/10.1093/eurheartj/ehu217')

add('Early infarct care and mechanical electrical complications','Free-Wall Rupture With Hemopericardium',
 'Five days after MI, a patient suddenly collapses with pulseless electrical activity. During resuscitation, bedside echocardiography shows a new echodense pericardial collection with chamber compression. What is the most likely complication?',
 'Ventricular free-wall rupture causing hemopericardium and tamponade',[
 ('Ventricular septal rupture causing an acute intracardiac shunt','Septal rupture can produce shock, but its defining imaging feature is interventricular flow rather than a new compressive pericardial blood collection.'),
 ('Papillary muscle rupture causing acute mitral regurgitation','Acute MR causes pulmonary edema and shock with mitral apparatus disruption; it does not account for the newly demonstrated hemopericardium.'),
 ('Isolated recurrent infarction causing primary pump failure','Reinfarction can cause collapse, but the new pericardial collection and compression identify an additional mechanical explanation requiring immediate treatment.')],
 [S('Recognize a Mechanical Cause of Pulseless Electrical Activity','**Post-infarct free-wall rupture can rapidly fill the pericardium with blood and cause tamponade.** The resulting obstruction to filling can produce PEA despite electrical activity.',
    'Bedside echocardiography may show pericardial fluid or clot and compressive physiology; direct visualization of the tear is not necessary to trigger urgent concern.',
    'Continue resuscitation while activating cardiac surgery. An echodense collection may contain clot, so the absence of a large simple fluid pocket does not exclude hemopericardium.'),
  S('Prioritize Definitive Repair and Individualized Rescue','**Suspected free-wall rupture with tamponade requires emergency surgical management.** Drainage alone does not repair the bleeding ventricular wall.',
    'If surgery cannot be reached immediately and the patient cannot survive without decompression, controlled limited drainage may be used by an experienced team as a bridge. Rapid complete decompression can aggravate bleeding.',
    'Avoid treating this as an uncomplicated inflammatory effusion or delaying surgery to obtain elective cross-sectional imaging in a collapsing patient. Selected temporary circulatory support may assist rescue, although tamponade can limit venous drainage and device flow. A contained rupture can later form a pseudoaneurysm, whose wall lacks normal full-thickness myocardium and requires separate specialist assessment. Do not infer safety from temporary hemodynamic improvement: the structural lesion remains. Communicate the post-infarct timing, arrest rhythm and bedside findings immediately so transfer and definitive treatment proceed together.')],['MECH','TAMP','ACS'])

R['ALS2025']=('AHA adult advanced life support guideline, 2025','https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-advanced-life-support/')
R['ARREST2025']=('AHA adult cardiac arrest algorithm, 2025','https://cpr.heart.org/-/media/CPR-Files/CPR-Guidelines-Files/2025-Algorithms/Algorithm-ACLS-CA-250527.pdf')

add('Early infarct care and mechanical electrical complications','Early VF Requires Resuscitation and Trigger Assessment',
 'Six hours after STEMI, a monitored patient suddenly becomes unresponsive and pulseless. The monitor shows ventricular fibrillation and a defibrillator is immediately available. Which action has priority?',
 'Deliver prompt unsynchronized defibrillation with high-quality CPR and the cardiac-arrest pathway',[
 ('Give intravenous amiodarone before the first shock','Amiodarone may be considered for shock-refractory VF, but administering it first must not delay prompt defibrillation of a witnessed shockable arrest.'),
 ('Perform synchronized cardioversion after establishing a stable synchronization marker','Synchronization is used for selected organized tachyarrhythmias with a pulse; VF has no reliable QRS target and requires unsynchronized defibrillation.'),
 ('Correct potassium before attempting electrical treatment','Electrolyte abnormalities require correction during resuscitation, but laboratory confirmation or replacement must not delay the first shock for VF.')],
 [S('Treat the Arrest Before Classifying Its Long-Term Implications','**VF is a shockable cardiac-arrest rhythm.** Provide prompt defibrillation and high-quality CPR with minimal interruption, following the current resuscitation algorithm.',
    'In the AHA 2025 shockable pathway, epinephrine begins during CPR after the second shock; amiodarone or lidocaine is considered after the third. Resume CPR immediately after each shock for two minutes before rhythm reassessment, minimizing pauses. Drug preparation must not delay defibrillation.',
    'Assess reversible causes during resuscitation, including hypoxia, electrolyte disturbance and coronary ischemia, without prolonged pauses for testing.'),
  S('Reassess Ischemia and Recurrence After Circulation Returns','**Early timing does not make a ventricular arrhythmia harmless.** Evaluate reperfusion, recurrent occlusion, hemodynamics, ventricular function, potassium, magnesium and drug-related proarrhythmia.',
    'Recurrent malignant arrhythmias may require antiarrhythmic therapy and sympathetic control when hemodynamically suitable, alongside treatment of the ischemic substrate.',
    'A transient early infarct-related arrhythmia does not by itself establish an immediate permanent ICD indication. Later sustained VT/VF or an event without a reversible explanation requires secondary-prevention assessment. Distinguish VF from nonsustained VT and tolerated reperfusion rhythms; routine prophylactic antiarrhythmics are not justified merely by an infarct diagnosis.')],['ALS2025','ARREST2025','ESCACS','ACS'],
 table=(['AHA 2025 adult VF/pVT arrest intervention','Dose or delivery','Qualification'],[
 ['Biphasic defibrillation','Manufacturer recommendation, e.g. 120–200 J initially; maximum available if unknown','Subsequent shocks equivalent or higher energy as appropriate'],
 ['Epinephrine IV/IO','1 mg every 3–5 minutes','After initial defibrillation attempts in the shockable pathway'],
 ['Amiodarone IV/IO','300 mg bolus, then 150 mg if needed','For shock-refractory VF/pVT'],
 ['CPR','100–120 compressions/min; adult depth at least 5 cm, avoiding >6 cm','Full recoil, minimal interruption and appropriate ventilation']]))

R['PACE']=('ESC cardiac pacing and CRT guideline, 2021','https://doi.org/10.1093/eurheartj/ehab364')

add('Early infarct care and mechanical electrical complications','Transient AV Block After Inferior Infarction',
 'During inferior STEMI, complete AV block occurs with a narrow-complex escape at 48/min and preserved perfusion. After successful reperfusion, normal AV conduction returns and remains stable without bundle-branch block. What is the appropriate pacing approach?',
 'Continue monitored reassessment without automatic permanent pacemaker implantation',[
 ('Schedule permanent pacing on day five based on the documented complete block','A five-day assessment interval can apply to unresolved infarct-related block, but the previous rhythm alone does not create a device indication after stable recovery.'),
 ('Insert a transvenous temporary pacemaker during the post-reperfusion observation period','Temporary pacing is appropriate for refractory symptomatic bradycardia or hemodynamic compromise, but adds invasive risk without a current indication when conduction and perfusion have recovered.'),
 ('Schedule permanent pacing on day ten even if normal conduction is maintained','Ten days is an upper observation boundary for unresolved block in the ESC discussion, not a scheduled device indication for a patient whose conduction has recovered.')],
 [S('Infer the Likely Level of Block Without Treating It as Certain','**AV block accompanying inferior MI is commonly nodal or supra-Hisian and can resolve after reperfusion.** A narrow escape supports this mechanism but does not replace assessment of symptoms and stability.',
    'Anterior MI with new intraventricular conduction disease more often indicates infra-Hisian injury, an unreliable wide escape and a larger infarct burden.',
    'Review drugs, electrolytes and recurrent ischemia. Avoid unnecessary AV-nodal suppression while clinically important block is present.'),
  S('Separate Temporary Support From Permanent Device Indication','**Refractory symptoms or hemodynamic compromise can require temporary pacing.** Atropine may help vagally mediated or nodal block, but should not delay pacing when ineffective in an unstable patient.',
    'ESC 2021 describes individualized observation for persistent block, commonly five to ten days; if it has not resolved within ten days, permanent pacing should be performed. Earlier consideration depends on factors including unsuccessful or late reperfusion, anterior MI, preceding bifascicular/AV block and progression. This waiting framework concerns unresolved block, not the recovered conduction in this stem.',
    'Assess escape reliability and clinical deterioration throughout observation; temporary support can be needed while recovery is awaited. When a permanent device is indicated, ventricular function and anticipated pacing burden influence selection of conventional pacing, resynchronization or an ICD-capable system. Stable recovery after reperfusion supports monitored reassessment rather than implantation based solely on the earlier complete-block tracing.')],['PACE','ACS'])

R['LVT']=('AHA scientific statement on left ventricular thrombus, 2022','https://doi.org/10.1161/CIR.0000000000001092')

add('Post-infarct recovery and secondary prevention','Confirmed LV Thrombus After Anterior MI',
 'After anterior MI and PCI, contrast echocardiography confirms an apical LV thrombus. The patient has no active bleeding. Under the AHA 2022 statement, which management framework is appropriate?',
 'Begin oral anticoagulation, typically for three months, with repeat imaging and a coordinated antiplatelet plan',[
 ('Continue DAPT alone and repeat imaging at three months','DAPT is important after coronary stenting but does not replace indicated anticoagulation for confirmed LV thrombus; waiting for surveillance imaging leaves systemic embolic risk untreated.'),
 ('Prescribe indefinite anticoagulation without planned repeat imaging','Persistent thrombus or another indication can justify prolonged anticoagulation, but duration should be reassessed using resolution, ventricular recovery and bleeding rather than prescribed indefinitely without imaging.'),
 ('Give anticoagulation for one week and stop when symptoms resolve','A short symptomatic course is not an adequate treatment framework for confirmed LV thrombus; embolic risk and thrombus resolution cannot be inferred from relief of infarct symptoms.')],
 [S('Treat Confirmed Thrombus Rather Than Inferring Protection From DAPT','**Post-MI LV thrombus generally warrants oral anticoagulation.** The AHA 2022 statement describes a typical duration of ==three months==, followed by reassessment rather than an automatic stop regardless of findings.',
    'Apical akinesis, endocardial injury and blood stasis after a large anterior infarct promote thrombus formation. Embolism can occur without warning symptoms.',
    'Warfarin is an established option; the statement considers a DOAC a reasonable alternative on available evidence. Select the drug and dose using renal function, interactions, adherence and the patient’s other indications.'),
  S('Use Imaging and Bleeding Risk to Guide the Next Decision','**Repeat imaging assesses resolution and ventricular recovery.** Contrast echocardiography improves apical definition, while CMR is useful when echocardiography is inconclusive or clinical suspicion remains high.',
    'Persistent thrombus requires assessment of morphology, anticoagulant exposure and adherence before deciding whether to extend or change therapy.',
    'Coordinate the coronary antiplatelet regimen because adding anticoagulation to DAPT increases bleeding. Avoid leaving three agents unchanged indefinitely without an explicit indication and review date. Document the planned imaging modality, timing and clinician responsible for reviewing the result. Prophylactic anticoagulation for apical akinesis without demonstrated thrombus is a different, less certain decision and should not be equated with treatment of confirmed thrombus. The evidence-based duration framework must remain linked to the actual imaging and clinical course.')],['LVT','ACS'])

add('Post-infarct recovery and secondary prevention','Delayed Inflammatory Pericarditis After MI',
 'Three weeks after MI, a patient develops fever, pleuritic positional chest pain, a pericardial rub, elevated CRP and a small pleuropericardial effusion. There is no new troponin rise, territorial ECG evolution or echocardiographic evidence of rupture. Which diagnosis is most likely?',
 'Dressler syndrome within the post-cardiac injury syndrome spectrum',[
 ('Early infarct-associated pericarditis from adjacent myocardial necrosis','Early pericarditis usually occurs in the first days after infarction; the delayed inflammatory pleuropericardial presentation favors the immune-mediated syndrome.'),
 ('Recurrent myocardial infarction','Reinfarction requires renewed ischemic assessment and supporting acute injury evidence; the stated pain pattern, rub and inflammatory effusions without new ischemic findings favor pericarditis.'),
 ('Contained ventricular free-wall rupture','A contained rupture can present subacutely and must be excluded, but structural disruption or a pseudoaneurysmal cavity rather than this inflammatory syndrome would support that diagnosis.')],
 [S('Use Timing Together With Inflammatory Evidence','**Dressler syndrome is delayed post-MI pericarditis within the post-cardiac injury syndrome spectrum.** Timing varies; a latency of weeks and pleuropericardial inflammation support an immune-mediated process.',
    'Early infarct-associated pericarditis occurs in the first days and reflects local injury. Timing alone is insufficient without compatible symptoms, examination and investigations.',
    'Assess ECG, serial troponin when appropriate, inflammatory markers and echocardiography. New hypotension, a substantial effusion or an atypical course requires renewed evaluation for rupture, tamponade or another cause.'),
  S('Treat Inflammation Without Overlooking Coronary Therapy','**The 2025 ESC guideline favors high-dose aspirin as the anti-inflammatory agent after MI**, with colchicine when suitable. Coordinate the prescription with the existing antiplatelet regimen and bleeding risk.',
    'The 2025 ACC/AHA ACS dosing table lists aspirin 500–1000 mg every six to eight hours until improvement and colchicine 0.5–0.6 mg once or twice daily for three months. Use once-daily colchicine below seventy kilograms, with further renal, hepatic and interaction adjustments. Provide gastroprotection and coordinate high-dose aspirin with the existing antiplatelet regimen; these anti-inflammatory doses differ from routine maintenance aspirin.',
    'The guideline describes a short five-to-seven-day aspirin course with colchicine as reasonable for early post-MI pericarditis; delayed inflammatory disease requires duration and tapering guided by response. Corticosteroids are not routine first-line treatment when aspirin and colchicine are suitable. Reassess symptoms, CRP and effusion, and investigate alternative diagnoses if improvement is inadequate. A new post-infarct pain episode must first be evaluated rather than labeled Dressler syndrome simply because several weeks have elapsed.')],['MYOPERI','ACS'])

add('Post-infarct recovery and secondary prevention','Contained Rupture Versus True Ventricular Aneurysm',
 'After an inferior MI, imaging shows an inferolateral ventricular outpouching with an abrupt myocardial discontinuity and a narrow communication. The sac wall consists of adherent pericardial tissue rather than a continuous myocardial scar. Which diagnosis is most likely?',
 'Left ventricular pseudoaneurysm',[
 ('True post-infarct ventricular aneurysm','A true aneurysm represents expansion of scarred ventricular wall with myocardial continuity, usually with a broader transition; the described contained wall disruption favors pseudoaneurysm.'),
 ('Congenital muscular ventricular diverticulum','A muscular diverticulum contains myocardial tissue and typically contracts with the ventricle; it does not explain the acquired post-infarct wall discontinuity and pericardial sac.'),
 ('Loculated pericardial effusion without ventricular rupture','A loculated effusion lies outside the ventricle without the demonstrated communication through disrupted ventricular myocardium into an outpouching.')],
 [S('Identify the Wall Composition and Communication','**A pseudoaneurysm is a contained ventricular rupture.** Pericardium, adhesions and thrombotic material contain the sac rather than an intact myocardial wall.',
    'A narrow neck and inferior or lateral location are useful clues, but neck geometry alone is not an infallible diagnostic rule.',
    'Echocardiography evaluates flow and ventricular function; CMR or cardiac CT can clarify wall continuity and surrounding tissue when the patient is stable enough for further imaging.'),
  S('Connect the Diagnosis to Management Urgency','**Pseudoaneurysm requires prompt surgical or structural-heart assessment because rupture risk differs from that of a mature true aneurysm.** Instability or evidence of ongoing rupture requires emergency treatment.',
    'An incidentally identified chronic lesion after remote MI may permit urgent planned assessment rather than immediate emergency surgery. Anatomy, symptoms, expansion and operative risk inform the decision.',
    'True aneurysms more often cause chronic heart failure, ventricular arrhythmia or thrombus-related embolism. Their management includes appropriate ventricular therapy and anticoagulation when indicated; surgery is reserved for selected refractory complications or associated operative indications. Do not prescribe automatic surgery for every stable true aneurysm, or reassurance for a pseudoaneurysm simply because the rupture is currently contained. Document whether the wall contains myocardial scar, the communication, sac dimensions, thrombus and interval change. Those findings provide a stronger basis for decision-making than the nonspecific word aneurysm alone.')],['MECH'])

add('Post-infarct recovery and secondary prevention','Reassess EF Before Primary-Prevention ICD Implantation',
 'Ten days after MI and successful PCI, a stable patient has LVEF 28%. There has been no sustained VT or VF, and ventricular therapy has just been initiated. Which device strategy is appropriate?',
 'Optimize medical therapy and reassess EF after the post-MI and post-revascularization recovery intervals',[
 ('Implant a primary-prevention ICD before discharge using the current EF','A severely reduced early EF identifies risk but can improve; routine primary-prevention implantation during the first forty days after MI has not improved overall prognosis.'),
 ('Recheck EF at six weeks and implant then if it remains twenty-eight percent','Six weeks exceeds the post-MI interval, but recent revascularization and newly initiated therapy also require recovery and reassessment; that date is too early for the routine pathway described here.'),
 ('Continue medical therapy and reserve device assessment for a future sustained VT episode','Secondary prevention follows an arrhythmic event, but eligible persistent ventricular dysfunction can justify primary-prevention assessment without waiting for sustained VT or VF.')],
 [S('Distinguish Early Risk From a Proven Device Indication','**Primary-prevention ICD implantation is not routinely performed within forty days after MI.** An early low EF may reflect stunning and evolving remodeling as well as permanent injury.',
    'The 2022 AHA/ACC/HFSA framework supports EF reassessment beyond forty days after MI and beyond ninety days after revascularization or medical optimization when determining device candidacy.',
    'The patient has no separate secondary-prevention arrhythmic indication. Do not apply the primary-prevention waiting framework mechanically to every survivor of sustained VT or VF without evaluating reversibility.'),
  S('Assess Persistent Eligibility and Competing Risks','**Later candidacy requires persistent ventricular dysfunction despite appropriate therapy and a meaningful survival expectation exceeding one year.** Symptoms and EF thresholds matter.',
    'In the named framework, ischemic disease with EF at most thirty-five percent and NYHA II–III symptoms supports an ICD when other criteria are satisfied; selected NYHA I post-MI patients qualify at EF at most thirty percent.',
    'Repeat ventricular imaging and review treatment tolerance, comorbidity and patient preferences. Assess QRS morphology and duration if resynchronization may be relevant. A wearable defibrillator is a separate individualized bridging decision, not an automatic proven substitute for every patient awaiting reassessment. Explain the recovery plan and arrange a definite review so appropriate delay does not become indefinite omission of device assessment. The purpose is to select patients with a persistent, evidence-supported benefit rather than implant from a single acute-phase measurement.')],['HF2022','ACS'])

add('Post-infarct recovery and secondary prevention','Nonstatin Escalation After ACS',
 'Six weeks after ACS, a patient taking maximally tolerated atorvastatin 80 mg daily has LDL-C 86 mg/dL with confirmed adherence. Triglycerides are 130 mg/dL. Under the 2025 ACC/AHA ACS framework, which next step is appropriate?',
 'Add an evidence-based nonstatin LDL-lowering agent while continuing the tolerated statin',[
 ('Continue the same regimen because LDL-C is already below 100 mg/dL','A threshold of one hundred does not reflect the named post-ACS escalation framework; LDL-C at least seventy on maximal statin treatment supports adding a nonstatin.'),
 ('Replace atorvastatin with a moderate-intensity statin before considering combination therapy','Dose reduction is appropriate for intolerance or another specific reason, but the patient tolerates high-intensity treatment and needs additional LDL lowering.'),
 ('Add a fibrate as the preferred response to the residual LDL elevation','Fibrates have selected triglyceride-related uses, but the stated normal triglycerides and residual LDL burden favor an LDL-directed outcome-supported nonstatin.')],
 [S('Use the Named Guideline’s Escalation Threshold','**The 2025 ACC/AHA ACS guideline recommends adding a nonstatin when LDL-C remains at least seventy mg/dL on maximally tolerated statin therapy.** At fifty-five to sixty-nine, addition is reasonable.',
    'High-intensity statin treatment remains the foundation when tolerated. A numerically improved LDL does not establish that residual risk has been adequately addressed.',
    'Reassess adherence, drug access, interactions and secondary causes before labeling treatment failure. The six-week measurement is within the recommended four-to-eight-week follow-up interval.'),
  S('Select Additional Therapy According to Required Reduction','**Ezetimibe and PCSK9 monoclonal antibodies are established options with cardiovascular outcome evidence.** Selection depends on the magnitude of lowering needed, prior therapy, tolerance and access.',
    'Ezetimibe is commonly prescribed at ten milligrams daily. A PCSK9 antibody can provide a larger additional reduction when the remaining LDL burden warrants it.',
    'Distinguish an escalation threshold from a treatment goal. The 2026 ACC/AHA dyslipidemia guideline recommends LDL-C below 55 mg/dL and non-HDL-C below 85 mg/dL for very-high-risk secondary prevention; ASCVD patients outside that category generally have an LDL-C goal below 70 mg/dL, with further intensification toward below 55 reasonable in selected patients. Continue lifestyle treatment and reassess response. Avoid reducing a tolerated statin merely because combination treatment achieves a low LDL. Explain the additional agent and arrange a documented follow-up lipid measurement.')],['ACS','LIPID2026','ESCACS'],table=(['Framework','Value','Meaning'],[
 ['ACC/AHA ACS 2025','LDL-C ≥70 mg/dL on maximal tolerated statin','Add a nonstatin'],
 ['ACC/AHA ACS 2025','LDL-C 55–69 mg/dL on maximal tolerated statin','Nonstatin addition is reasonable'],
 ['ACC/AHA dyslipidemia 2026: very-high-risk ASCVD','LDL-C <55; non-HDL-C <85 mg/dL','Secondary-prevention treatment goals'],
 ['ACC/AHA ACS 2025','4–8 weeks','Reassess lipid profile after discharge'],
 ['ESC ACS 2023','LDL-C <55 mg/dL and ≥50% reduction from baseline','Post-ACS treatment goals'],
 ['ESC ACS 2023','4–6 weeks after treatment adjustment','Reassess response; add ezetimibe then PCSK9 inhibitor if goals remain unmet']]))

add('Post-infarct recovery and secondary prevention','Rehabilitation Referral Before ACS Discharge',
 'A stable patient is ready for discharge after ACS PCI. The nearest center-based rehabilitation program is difficult to reach. Which discharge approach is most appropriate?',
 'Arrange comprehensive rehabilitation referral now and assess a suitable home-based or hybrid program',[
 ('Reassess rehabilitation referral at the six-week clinic visit after initial recovery','Later review can refine training and barriers, but referral before discharge improves the opportunity to connect eligible patients with recovery services; stability does not require a six-week delay in referral.'),
 ('Provide a walking plan and written prevention advice as the complete discharge program','Walking and written advice can support recovery, but do not supply the assessment, graduated training, medication support and psychosocial components of comprehensive rehabilitation.'),
 ('Refer to the distant center-based program without assessing alternative delivery','Center-based rehabilitation is effective when accessible, but an unaddressed travel barrier can prevent participation; suitable home-based or hybrid delivery should be assessed rather than relying on an impractical referral.')],
 [S('Prescribe a Comprehensive Recovery Program','**Refer eligible ACS patients to cardiac rehabilitation before discharge.** The program combines graduated exercise, risk-factor management, medication support, nutrition and psychosocial care.',
    'Assess ventricular function, residual ischemia, rhythm problems and functional capacity to determine suitable training and supervision.',
    'A successful PCI does not remove the need for prevention and recovery support. The treatment target includes function, adherence and recurrent-event risk, not merely the treated lesion.'),
  S('Address Access and Tobacco Use Explicitly','**Home-based or hybrid rehabilitation can improve access for selected patients.** Selection still requires assessment; evidence and safety should not be assumed identical for every high-risk presentation.',
    'Ask about transport, cost, work, caregiving and digital access. Give a concrete contact and appointment plan rather than a generic instruction to exercise.',
    'For tobacco use, combine behavioral support with appropriate cessation pharmacotherapy after reviewing contraindications and patient preferences. Address secondhand exposure and arrange follow-up for relapse rather than treating a single bedside warning as a complete intervention. Provide individualized advice on activity progression, return to work and recognition of recurrent ischemic symptoms. Medication access and adherence should be reviewed alongside rehabilitation enrollment. A referral alone is not evidence that the patient attended, so follow-up should confirm participation and address barriers. The appropriate response to travel difficulty is a feasible supervised recovery pathway, not omission of care.')],['ACS'])

R['BBIPD']=('Individual-patient meta-analysis of beta blockers after MI with normal EF, 2025','https://doi.org/10.1056/NEJMoa2512686')
R['ABYSS']=('ABYSS beta-blocker interruption trial, 2024','https://doi.org/10.1056/NEJMoa2404204')

add('Post-infarct recovery and secondary prevention','Long-Term Beta Blockers With Preserved EF',
 'A clinician reviews contemporary randomized evidence for routine long-term beta blockers after an uncomplicated MI in patients with LVEF at least 50% and no other beta-blocker indication. Which interpretation is best supported by the 2025 individual-patient meta-analysis?',
 'Routine treatment did not reduce the composite of death, MI or heart failure in the preserved-EF population studied',[
 ('Routine treatment established a mortality benefit equivalent to that in reduced-EF heart failure','Benefit in reduced-EF HF cannot be transferred to normal-EF post-MI patients; the contemporary pooled preserved-EF evidence did not demonstrate that claimed benefit.'),
 ('The findings support avoiding beta blockers during the acute admission as well as follow-up','The analysis concerns long-term treatment in a selected EF population, not an instruction to abandon acute use when indicated or treatment for another condition.'),
 ('The findings establish noninferiority of withdrawal in patients already receiving long-term treatment','Initiation-versus-no-treatment evidence does not establish universal withdrawal safety; ABYSS addressed interruption separately and did not demonstrate noninferiority of interruption.')],
 [S('Specify the EF Group and Clinical Question','**The 2025 individual-patient meta-analysis pooled contemporary trials in post-MI patients with LVEF at least fifty percent.** Routine beta blockers did not lower the composite of all-cause death, MI or heart failure.',
    'This result should not be extended unchanged to EF forty to forty-nine percent, established HF, symptomatic angina, arrhythmia or another independent indication.',
    'Distinguish long-term event prevention from the acute hemodynamic and antiarrhythmic decisions made during the infarct admission.'),
  S('Separate Treatment Initiation From Withdrawal','**ABYSS studied interruption versus continuation in patients already receiving long-term beta blockers.** Failure to demonstrate noninferiority of interruption prevents a blanket claim that withdrawal is equivalent.',
    'Trials differ in EF entry criteria, endpoints and time since MI. A broad statement that all modern trials prove the same result obscures those clinically important differences.',
    'Review ventricular function, blood pressure, angina, rhythm, adverse effects and the original indication before changing an established prescription. If discontinuation is selected, use a supervised taper rather than an automatic abrupt stop. Continue proven secondary prevention irrespective of the beta-blocker decision. Explain that absence of demonstrated routine benefit in one population is not evidence that the drug has no role in coronary care. The appropriate conclusion is indication-based prescribing informed by the patient’s EF and clinical context, with separate attention to the risks of changing established treatment.')],['BBIPD','ABYSS','ACS'],style='direct')

R['MINT']=('MINT randomized transfusion trial, 2023','https://doi.org/10.1056/NEJMoa2307983')

add('Post-infarct recovery and secondary prevention','Transfusion Strategy in ACS With Anemia',
 'A patient with ACS has hemoglobin 8.4 g/dL without active bleeding. The team is reviewing the 2025 ACC/AHA recommendation and MINT evidence. Which interpretation is most appropriate?',
 'A liberal transfusion strategy toward hemoglobin around ten may be reasonable, with individualized benefit–risk assessment',[
 ('A seven-gram threshold remains the preferred ACS default because restrictive trials in other inpatients apply directly','Restrictive thresholds are supported in several other settings, but ACS-specific evidence and the named recommendation warrant separate interpretation rather than direct extrapolation.'),
 ('MINT proved a statistically significant reduction in its primary endpoint with liberal transfusion','The primary comparison favored liberal treatment numerically but did not reach conventional statistical significance; overstating certainty misrepresents the trial.'),
 ('The nonsignificant MINT result establishes equivalent safety of restrictive and liberal strategies','A superiority comparison with P=0.07 does not establish equivalence; its confidence interval still permits clinically important harm from the restrictive strategy.')],
 [S('Read the Trial Result Without Converting Uncertainty Into Equivalence','**MINT compared restrictive and liberal transfusion strategies in MI with hemoglobin below ten.** Thirty-day death or MI occurred in 16.9% versus 14.5%, respectively.',
    'The modeled relative risk for restrictive versus liberal treatment was 1.15, with a ninety-five-percent confidence interval of 0.99–1.34 and P=0.07.',
    'This did not establish statistical superiority of the liberal strategy, but clinically important harm from a restrictive strategy could not be excluded. A nonsignificant result does not prove the strategies equivalent.'),
  S('Apply the Recommendation to the Actual Patient','**The 2025 ACC/AHA ACS guideline states that transfusion to achieve hemoglobin at least ten may be reasonable in ACS with anemia.** This is a qualified recommendation rather than a universal mandate.',
    'Consider continuing ischemia, symptoms, anemia trajectory, heart failure, renal function and transfusion-associated circulatory overload. Reassess after each transfusion step according to clinical practice.',
    'Investigate the cause of anemia and distinguish this nonbleeding presentation from active major hemorrhage, where resuscitation and source control have their own urgency. Review antithrombotic exposure and occult blood loss. Do not replace the measured clinical course with a single threshold detached from context, and do not extrapolate these ACS findings to every stable medical inpatient. Explain the expected benefit and uncertainty while monitoring for adverse transfusion effects. The question tests appropriate interpretation and individualized management, not certainty that one hemoglobin target is optimal for every patient.')],['MINT','ACS'])

R['CCD']=('AHA/ACC chronic coronary disease guideline, 2023','https://doi.org/10.1016/j.jacc.2023.04.003')
R['CCS2024']=('ESC chronic coronary syndromes guideline, 2024','https://doi.org/10.1093/eurheartj/ehae177')

add('Chronic coronary disease angina and landmark evidence','Antianginal Selection With Bradycardia and Hypertension',
 'A patient with stable exertional angina has sinus rate 49/min, blood pressure 158/86 mm Hg and LVEF 60%. There is no recent MI or other indication for rate slowing. Which initial antianginal is best suited among these choices?',
 'Amlodipine',[
 ('Metoprolol','Metoprolol reduces angina through rate and contractility effects and is useful when tachycardia or another indication exists; this patient already has substantial resting bradycardia.'),
 ('Diltiazem','Diltiazem can treat angina and hypertension, but its nodal effects may further slow the heart rate; a dihydropyridine better matches the current physiology.'),
 ('Verapamil','Verapamil is an antianginal rate-slowing calcium antagonist, but resting bradycardia makes its chronotropic and conduction effects less suitable here.')],
 [S('Match the Drug to Heart Rate and Blood Pressure','**Amlodipine provides arterial vasodilation without clinically important direct sinus or AV-nodal suppression.** It can address both angina and the elevated pressure in this patient.',
    'Beta blockers and nondihydropyridine calcium antagonists are useful antianginals in appropriate patients, but their rate-slowing effects matter when the resting pulse is already low.',
    'Evaluate symptomatic bradycardia, conduction disease and medication causes separately. Choosing an antianginal does not remove the need to understand an unexpectedly slow pulse.'),
  S('Separate Symptom Control From Prognostic Therapy','**Antianginal treatment is individualized according to hemodynamics, ventricular function and comorbidity.** No single first-line drug is optimal for every stable coronary presentation.',
    'Amlodipine commonly starts at ==5 mg once daily==, with lower initiation in selected frail patients and titration to ==10 mg once daily== according to response. Monitor edema, dizziness and hypotension.',
    'Avoid casually combining a beta blocker with verapamil or diltiazem because bradycardia and AV block can be amplified. Nondihydropyridines are also unsuitable in significant systolic dysfunction. If blood pressure were low as well as heart rate, a hemodynamically neutral option such as ranolazine might be more attractive after interaction screening. Continue lipid lowering and other indicated secondary prevention independently of symptom treatment. Persistent lifestyle-limiting angina despite suitable therapy warrants reassessment of ischemia and anatomy rather than unstructured escalation of drugs that worsen the patient’s physiological constraints.')],['CCD','CCS2024'])

R['RAN']=('Ranolazine extended-release prescribing information','https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a624dc7f-921d-4554-a813-f72dca0133c3')
R['RANUK']=('Ranexa UK Summary of Product Characteristics','https://www.medicines.org.uk/emc/product/6442/smpc')

add('Chronic coronary disease angina and landmark evidence','Ranolazine With Concurrent Diltiazem',
 'A patient with chronic angina is taking diltiazem. Ranolazine extended release is being considered after review of renal function, ECG and other drugs. Under the US prescribing information, what is the maximum ranolazine dose while diltiazem continues?',
 '500 mg twice daily',[
 ('1000 mg twice daily','This is the usual maximum without a relevant interacting inhibitor, but diltiazem increases ranolazine exposure and lowers the permitted maximum.'),
 ('750 mg twice daily','Seven hundred fifty milligrams twice daily is a usual maximum in some European product information, but the question specifies the US prescribing information and its diltiazem interaction ceiling.'),
 ('375 mg twice daily','Three hundred seventy-five milligrams twice daily is a starting dose in some European formulations; it is not the specified US maximum during moderate CYP3A inhibition.')],
 [S('Identify the Pharmacokinetic Interaction','**Diltiazem is a moderate CYP3A inhibitor and increases ranolazine exposure.** The US prescribing information limits ranolazine to ==500 mg twice daily== during this combination.',
    'The ordinary extended-release regimen starts at five hundred milligrams twice daily and may increase to one thousand twice daily when suitable; the interacting-drug limit overrides that usual ceiling.',
    'Strong CYP3A inhibitors and CYP3A inducers are contraindicated combinations rather than situations managed simply by the same dose cap.'),
  S('Screen Beyond Heart Rate and Blood Pressure','**Ranolazine inhibits late inward sodium current and can improve angina with relatively little effect on resting pulse or pressure.** Hemodynamic neutrality does not imply freedom from important adverse effects.',
    'It can prolong QT in an exposure-dependent manner. Review baseline QT, other QT-prolonging medicines, electrolytes, renal function and liver disease; liver cirrhosis is a labeled contraindication.',
    'Dizziness, constipation and nausea can limit treatment. Monitor renal function, particularly with impairment or an acute illness, and review interactions involving other substrates as well as inhibitors. Extended-release tablets should be taken according to the formulation instructions rather than crushed or converted into an improvised dosing schedule. The drug treats chronic symptoms and does not replace acute reperfusion, antiplatelet treatment or lipid lowering when those are indicated. If angina remains limiting at the safe tolerated dose, reassess the regimen and coronary mechanism rather than exceeding an interaction-based ceiling.')],['RAN','RANUK','CCS2024'],style='direct')

add('Chronic coronary disease angina and landmark evidence','Symptom-Driven Revascularization in Stable Coronary Disease',
 'A patient with stable coronary disease has lifestyle-limiting angina despite tolerated guideline-directed therapy. A significant focal stenosis matches the ischemic territory and is suitable for PCI. LVEF is normal and left-main disease is absent. What is the best explanation for offering PCI?',
 'PCI is recommended to improve persistent symptoms, without promising a universal survival benefit in this setting',[
 ('PCI is offered primarily for an established survival advantage in this focal normal-EF presentation','Prognostic benefit depends on anatomy and clinical population; this focal stable lesion with normal EF supports symptom-directed intervention without an established universal survival claim.'),
 ('PCI should await development of LV dysfunction before symptoms justify intervention','LV dysfunction can affect prognostic indications, but is not required for symptom-directed revascularization when significant suitable disease causes lifestyle-limiting angina despite treatment.'),
 ('PCI should be reserved for a future ACS because symptoms alone do not justify it','Emergency reperfusion is a separate indication; selected stable patients already qualify for symptom-relieving revascularization without waiting for infarction or instability.')],
 [S('Define the Intended Benefit Before Recommending a Procedure','**Revascularization is recommended for lifestyle-limiting angina despite appropriate therapy when significant disease is amenable to treatment.** Symptom relief and improved daily function are meaningful outcomes.',
    'Confirm that the lesion is clinically relevant rather than assuming every angiographic narrowing causes the reported symptoms.',
    'Discuss procedural risks, bleeding and antiplatelet requirements, expected symptom benefit and the possibility of persistent symptoms from another mechanism.'),
  S('Keep Prognostic Indications Population-Specific','**Selected anatomy and ventricular dysfunction can create a separate survival indication**, particularly when CABG is appropriate for significant left-main disease or multivessel disease with severe LV dysfunction.',
    'Do not transfer CABG survival evidence automatically to PCI or extend stable-disease trial results to excluded high-risk anatomy.',
    'A Heart Team assessment is useful for complex multivessel disease or uncertainty about the preferred method. Continue lipid lowering, lifestyle treatment and other indicated prevention after intervention. If symptoms improve, reassess the need for antianginal drugs individually rather than assuming all coronary medicines can stop. The decision should reflect the patient’s symptom burden and preferences alongside anatomy and clinical risk. Accurate counseling neither dismisses symptom-directed PCI nor promises that treating one stable lesion necessarily prolongs life in every patient.')],['CCD','CCS2024'])

R['ISCBASE']=('ISCHEMIA randomized trial baseline population and exclusions, 2019','https://pmc.ncbi.nlm.nih.gov/articles/PMC6439551/')
R['ISCEXT']=('ISCHEMIA-EXTEND long-term survival report, 2026','https://doi.org/10.1001/jama.2026.20375')

add('Chronic coronary disease angina and landmark evidence','Applying ISCHEMIA Beyond Its Enrollment Population',
 'A stable patient has a seventy-percent unprotected left-main stenosis. A colleague cites ISCHEMIA as proof that an initial conservative strategy is equivalent for this anatomy. Which response is most appropriate?',
 'Significant unprotected left-main disease was excluded, so the trial cannot justify that extrapolation',[
 ('The overall neutral comparison supports medical therapy first for this left-main lesion','An overall result applies within the population and strategies studied; it cannot establish a conservative-first conclusion for significant left-main disease that the trial excluded.'),
 ('The conservative arm prohibited later angiography, limiting comparison with current practice','The conservative strategy allowed angiography and revascularization for clinical indications; the relevant limitation here is excluded anatomy rather than a permanent ban on invasive care.'),
 ('The lack of statistical significance establishes equivalence between strategies in stable CAD','Failure to demonstrate superiority does not establish formal equivalence, and neither interpretation can extend the randomized comparison to this excluded anatomical subgroup.')],
 [S('Check Eligibility Before Applying a Trial Result','**ISCHEMIA enrolled selected stable patients with moderate or severe ischemia.** Significant unprotected left-main disease was excluded, so its initial-strategy comparison does not settle management of this patient.',
    'Other major exclusions included EF below thirty-five percent, recent ACS, unacceptable angina despite maximally tolerated treatment and advanced kidney disease in the main trial.',
    'The parallel ISCHEMIA-CKD study addressed a different kidney-disease population and must not be silently substituted for the main trial.'),
  S('Distinguish Strategy, Symptoms and Prognosis','**An initial conservative strategy includes active medical treatment and later angiography when indicated.** It does not mean permanent prohibition of revascularization.',
    'The November 2026 ISCHEMIA-EXTEND report found no significant all-cause survival difference over a median nine-year follow-up. Estimated eleven-year mortality was 25.8% with initial invasion versus 26.9% with initial conservative management; adjusted hazard ratio 0.97, ninety-five-percent confidence interval 0.86–1.09. This survival analysis does not eliminate symptom benefits or extend eligibility to excluded patients.',
    'Significant left-main disease requires anatomy-based specialist assessment and consideration of revascularization, often through a Heart Team. The suitable method depends on complexity, operative risk and other patient factors. Do not use a nonsignificant overall trial comparison to claim formal equivalence in an excluded subgroup. Similarly, severe uncontrolled symptoms remain a clinical indication for reassessment even when a patient otherwise resembles trial participants. The central examination skill is external validity: identify who was randomized, which strategies were compared and which conclusion the data can actually support.')],['ISCBASE','ISCEXT','CCD'])

R['COURAGE']=('COURAGE randomized trial, 2007','https://doi.org/10.1056/NEJMoa070829')
R['FAME']=('FAME randomized trial, 2009','https://doi.org/10.1056/NEJMoa0807611')

add('Chronic coronary disease angina and landmark evidence','FAME and COURAGE Answer Different Questions',
 'Which statement correctly distinguishes the original FAME and COURAGE randomized trials?',
 'FAME compared physiological versus angiographic PCI guidance; COURAGE compared initial PCI plus medical therapy with medical therapy alone',[
 ('FAME compared PCI with medical therapy alone; COURAGE compared physiological with angiographic PCI guidance','These trial designs are reversed: original FAME studied how to select lesions during planned multivessel PCI, whereas COURAGE studied adding initial PCI to medical therapy.'),
 ('FAME compared FFR-selected PCI with medical therapy; COURAGE compared PCI with CABG','The first comparison resembles FAME 2 rather than original FAME; COURAGE compared adding PCI to medical therapy and did not randomize patients between PCI and CABG.'),
 ('FAME compared FFR-guided with angiographic PCI; COURAGE compared intensive with moderate lipid lowering','The FAME description is correct, but COURAGE randomized the initial PCI strategy on a background of optimal medical therapy, not statin intensity as its assigned intervention.')],
 [S('Identify the Randomized Comparison','**Original FAME tested FFR-guided versus angiography-guided multivessel PCI.** In the physiological arm, lesions were treated when FFR was at most 0.80.',
    'At one year, the composite of death, MI or repeat revascularization was 13.2% with FFR guidance versus 18.3% with angiographic guidance. This is a composite strategy result, not proof of isolated mortality benefit.',
    'Do not confuse original FAME with FAME 2, which addressed a different comparison involving FFR-selected PCI and medical therapy.'),
  S('Interpret Medical-Therapy Evidence Without Abandoning Symptom Care','**COURAGE compared initial PCI plus optimal medical therapy with optimal medical therapy alone in selected stable coronary disease.** It did not demonstrate a reduction in death or nonfatal MI from adding initial PCI.',
    'Medical therapy in both arms was active preventive and antianginal treatment. A conservative initial strategy did not prohibit later revascularization when clinically required.',
    'FFR reflects the pressure consequence of an epicardial lesion during hyperemia; it is not a test that excludes every microvascular or vasospastic mechanism of angina. Interpret borderline measurements and acute-infarct physiology with appropriate clinical caution. Use the trials to clarify whether a patient needs revascularization and, separately, which lesions should be treated. Their results do not negate symptom-directed intervention or anatomy-specific prognostic indications outside the studied comparison. Knowing the trial name is less useful than identifying its population, comparator and endpoint.')],['COURAGE','FAME','CCD'],style='direct')

R['AMLOD']=('Amlodipine prescribing information: chronic stable and vasospastic angina','https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=5a0b3dd4-91f5-4173-a992-e91b1cac6a18')

add('Chronic coronary disease angina and landmark evidence','Preventing Recurrent Epicardial Coronary Spasm',
 'A patient has recurrent nocturnal rest angina with transient ST elevation. Coronary functional testing confirms epicardial spasm without a flow-limiting fixed lesion. Heart rate is 76/min, blood pressure 132/78 mm Hg and EF is normal. Which preventive treatment is preferred?',
 'A calcium channel blocker titrated to suppress episodes',[
 ('A beta blocker alone as the principal antispasm treatment','Beta blockers are useful for demand-related angina and other indications, but are not the preferred treatment for isolated epicardial spasm and may aggravate vasoconstriction in susceptible patients.'),
 ('Ranolazine alone before attempting calcium channel blockade','Ranolazine can help selected chronic angina patients, but confirmed spasm has a more directly supported first-line calcium antagonist strategy.'),
 ('A long-acting nitrate as initial preventive monotherapy before calcium channel blockade','Long-acting nitrates can be added for recurrent spasm despite calcium antagonism or selected when alternatives are unsuitable, but calcium channel blockade is the preferred initial preventive approach in this eligible patient.')],
 [S('Treat Dynamic Vasoconstriction','**Calcium channel blockers are first-line preventive therapy for confirmed vasospastic angina.** They reduce coronary smooth-muscle contraction and help prevent recurrent ischemic episodes.',
    'Select a dihydropyridine or nondihydropyridine according to pulse, blood pressure, conduction and ventricular function. For example, amlodipine is prescribed at ==5–10 mg once daily== for vasospastic angina, starting at the lower end and titrating to response. Monitor pressure, edema and dizziness; hepatic impairment and frailty can warrant more cautious initiation.',
    'Short-acting nitrates relieve episodes when suitable. Long-acting nitrates can be added for recurrent symptoms, with dosing designed to limit tolerance and with PDE5 interaction screening.'),
  S('Address Triggers and Overlapping Coronary Disease','**Smoking cessation and avoidance of provoking vasoconstrictors are important.** Review cocaine or stimulant exposure and medicines that may precipitate spasm.',
    'Spasm can coexist with atherosclerosis or microvascular dysfunction, so preventive treatment and additional antianginal choices should reflect the demonstrated mechanisms.',
    'A nondiagnostic resting ECG between episodes does not exclude the condition. Persistent pain or prolonged ST elevation requires emergency assessment for occlusion and infarction. Refractory episodes, syncope or ventricular arrhythmia warrant specialist evaluation and treatment intensification. Suppression of pain does not eliminate every arrhythmic risk. Calcium antagonism is the initial preventive step, with adjuncts and follow-up based on response.')],['CCS2024','CCD','AMLOD'])

add('Chronic coronary disease angina and landmark evidence','Mechanism-Based Treatment of Microvascular Angina',
 'A patient has exertional angina and objective ischemia without obstructive epicardial disease. Coronary function testing shows Doppler-derived CFR 1.8 and IMR 32 units, without provoked spasm. Which management principle is appropriate?',
 'Treat the demonstrated microvascular dysfunction with individualized antianginal and risk-factor therapy',[
 ('Reassure that the absence of an obstructive angiographic lesion excludes a coronary cause','Angiography assesses epicardial anatomy but does not exclude functional microvascular disease; the physiological findings supply a coronary mechanism for ischemia.'),
 ('Select a vasospasm-directed regimen without using the resistance and provocation findings','Vasospasm and impaired microvascular vasodilator function can overlap but are distinct endotypes; the negative provocation and resistance findings should inform selection.'),
 ('Perform empiric PCI of the vessel with the lowest flow reserve despite no focal obstruction','Reduced flow reserve can arise from microvascular dysfunction and does not itself identify a stentable epicardial lesion; empiric PCI does not address this demonstrated mechanism.')],
 [S('Interpret the Functional Measurements Together','**Reduced coronary flow reserve and increased microvascular resistance support coronary microvascular dysfunction.** A nonobstructive angiogram does not make objective ischemia noncardiac.',
    'Flow reserve integrates resting and hyperemic flow. The 2024 ESC guideline identifies Doppler CFR below 2.5 as abnormal in nonobstructive disease; IMR at least 25 units indicates increased microvascular resistance. CFR thresholds vary with method and framework, commonly below 2.0–2.5, so report the technique instead of treating one cutoff as universal.',
    'Acetylcholine testing addresses spasm and endothelial responses; a different positive endotype can change the preferred treatment. Avoid assigning every patient the same mechanism from symptoms alone.'),
  S('Tailor Treatment to the Demonstrated Endotype','**Antianginal selection should account for the microvascular mechanism, heart rate, blood pressure and comorbidity.** Beta blockers, calcium antagonists or ranolazine may be useful in selected reduced-reserve or increased-resistance presentations.',
    'Calcium antagonists are preferred when epicardial or microvascular spasm is demonstrated. Overlapping endotypes may require combination treatment.',
    'Address hypertension, lipids, smoking, physical conditioning and metabolic risk; ACE inhibition or other treatment should be selected according to the clinical context. Symptom improvement does not establish an identical mortality effect for every endotype-directed drug. Reassess symptoms and tolerability, and consider additional noncoronary contributors without dismissing documented coronary dysfunction.')],['CCS2024','CCD'],
 table=(['Functional finding','2024 ESC interpretation','Clinical distinction'],[
 ['Doppler CFR <2.5','Impaired coronary vasodilator reserve','Assess epicardial disease and testing conditions'],
 ['IMR ≥25 units','Increased microvascular resistance','Supports a resistance abnormality despite nonobstructive anatomy'],
 ['Acetylcholine: usual symptoms + ischemic ECG + ≥90% epicardial narrowing','Epicardial coronary spasm','Calcium antagonists are preferred initial preventive therapy'],
 ['Acetylcholine: usual symptoms + ischemic ECG without ≥90% epicardial narrowing','Microvascular spasm','Distinguish from impaired reserve without provoked spasm']]))

R['MI2026SLIDES']=('ESC official Fifth Universal Definition diagnostic slides, 2026','https://dam-assets.escardio.org/download/b2e827b89baa11f1879e62eac143aa37')
R['OAT']=('Occluded Artery Trial, 2006','https://doi.org/10.1056/NEJMoa066139')
R['LIPID2026']=('ACC/AHA multisociety dyslipidemia guideline, 2026','https://doi.org/10.1016/j.jacc.2025.11.016')
R['COMPASS']=('COMPASS randomized trial, 2017','https://doi.org/10.1056/NEJMoa1709118')

add('Chronic coronary disease angina and landmark evidence','Selected Long-Term Dual-Pathway Inhibition',
 'A patient with stable coronary and peripheral arterial disease has high recurrent ischemic risk, low bleeding risk, adequate renal function and no indication for DAPT or therapeutic anticoagulation. Which regimen is an evidence-supported option for intensifying long-term prevention?',
 'Rivaroxaban 2.5 mg twice daily plus low-dose aspirin',[
 ('Rivaroxaban 20 mg daily plus low-dose aspirin','Therapeutic-dose rivaroxaban has other indications such as eligible AF stroke prevention; it is not the COMPASS low-dose combination strategy requested here.'),
 ('Rivaroxaban 5 mg twice daily without aspirin','This rivaroxaban-alone arm was studied in COMPASS but did not establish the same benefit as low-dose rivaroxaban plus aspirin; the successful combination cannot be replaced by this higher-dose monotherapy.'),
 ('Rivaroxaban 2.5 mg twice daily plus clopidogrel','Clopidogrel is appropriate in several coronary and peripheral-arterial contexts, but substituting it for aspirin does not reproduce the COMPASS randomized combination evidence tested by this question.')],
 [S('Select Patients Before Intensifying Antithrombotic Treatment','**Low-dose rivaroxaban plus aspirin is an option in selected high-ischemic-risk chronic coronary disease without high bleeding risk.** The 2023 AHA/ACC framework specifies no separate need for therapeutic DOAC dosing or DAPT.',
    'The vascular dose is ==2.5 mg twice daily== with low-dose aspirin. It must not be substituted for therapeutic anticoagulation when AF or venous thromboembolism requires it.',
    'Review bleeding history, renal and hepatic function, stroke history, interactions and adherence. Polyvascular disease increases ischemic risk but does not erase bleeding contraindications.'),
  S('Explain the COMPASS Benefit and Harm Together','**COMPASS showed fewer cardiovascular deaths, strokes or MIs with the combination than with aspirin alone.** Primary events occurred in 4.1% versus 5.4%, with hazard ratio 0.76.',
    'Major bleeding increased: 3.1% versus 1.9%, with hazard ratio 1.70. The result supports patient selection rather than universal intensification.',
    'Continue lipid lowering, smoking cessation, blood-pressure management and exercise-based care; antithrombotic escalation does not replace these interventions. Reassess the regimen if bleeding, renal deterioration or a new anticoagulation indication develops. Extended DAPT in selected prior-MI patients is a different strategy with its own evidence and eligibility, not a reason to combine every available agent. Discuss both expected ischemic benefit and bleeding burden so the chosen prescription reflects the individual patient’s risk and preferences.')],['COMPASS','CCD'])

R['ARCHBR']=('Academic Research Consortium high bleeding risk consensus, 2019','https://pmc.ncbi.nlm.nih.gov/articles/PMC6636810/')
R['STENT']=('SCAI expert consensus on in-stent restenosis and stent thrombosis, 2023','https://pmc.ncbi.nlm.nih.gov/articles/PMC11308135/')

add('Antiplatelet anticoagulant and bleeding decisions','Recognizing High Bleeding Risk Before PCI',
 'A 76-year-old man undergoing ACS PCI has eGFR 45 mL/min/1.73 m², hemoglobin 13.5 g/dL and normal platelets. He has no prior bleeding, stroke, malignancy or anticoagulation indication. Which ARC-HBR interpretation is correct?',
 'High bleeding risk is present because age and moderate CKD supply two minor criteria',[
 ('High bleeding risk is absent because no major criterion is present','One major criterion is sufficient but not necessary: two minor criteria also establish ARC-HBR, as in this combination of age and moderate CKD.'),
 ('High bleeding risk is present because moderate CKD is a major criterion','An eGFR of 30–59 is a minor criterion; severe CKD below 30 supplies the major renal criterion, so this reaches the right label through the wrong classification.'),
 ('High bleeding risk is absent because three minor criteria are required','The consensus threshold is two minor criteria, not three; waiting for another abnormality would underrecognize this patient’s bleeding risk.')],
 [S('Apply the Binary Consensus Framework','**ARC-HBR requires at least one major or two minor criteria at PCI.** It is not an additive point score in which every item has equal weight.',
    'Age at least 75 years and eGFR 30–59 each constitute a minor criterion. This patient has both, despite normal hemoglobin and no bleeding history.',
    'The conceptual one-year boundaries are BARC 3 or 5 bleeding risk at least 4%, or intracranial hemorrhage risk at least 1%; they do not predict an exact individual event probability.'),
  S('Translate Risk Into a Treatment Discussion','**High bleeding risk prompts individualized prevention of bleeding while preserving coronary protection.** It does not itself prohibit PCI or justify stopping both antiplatelets.',
    'The 2025 ACS guideline allows selected abbreviated antiplatelet strategies; timing, retained agent and ischemic risk must be specified. Treat reversible anemia, avoid unnecessary NSAIDs and assess gastrointestinal protection when appropriate.',
    'Recheck renal function and hemoglobin during follow-up. A patient may have both high ischemic and high bleeding risk, so neither label independently dictates the complete prescription.')],['ARCHBR','ACS'],
 table=(['Selected ARC-HBR feature','Minor criterion','Major criterion'],[
 ['Age','≥75 years','Age alone does not supply a major criterion'],
 ['Renal function','eGFR 30–59 mL/min/1.73 m²','eGFR <30 mL/min/1.73 m²'],
 ['Hemoglobin','Men 11–12.9; women 11–11.9 g/dL','<11 g/dL'],
 ['Baseline platelet count','No minor threshold in this framework','<100 × 10⁹/L']] ))
# Keep the new risk-assessment decision adjacent to DAPT duration rather than append it out of sequence.
rows.insert(37,rows.pop())

add('Chronic coronary disease angina and landmark evidence','Investigating the Mechanism of Coronary Stent Failure',
 'Nine months after drug-eluting stent implantation, a patient develops recurrent exertional angina despite antianginal treatment. Angiography shows focal severe in-stent restenosis with preserved flow and no acute thrombotic occlusion. Before selecting repeat PCI treatment, which assessment is most useful?',
 'Intracoronary IVUS or OCT to define underexpansion, tissue growth and other mechanisms',[
 ('Platelet-function testing to determine the cause of the focal narrowing','Selected platelet testing can address antiplatelet response, especially in thrombotic presentations, but does not distinguish mechanical underexpansion from neointimal tissue causing this restenosis.'),
 ('Repeat coronary calcium scoring to characterize the stented segment','Calcium scoring can inform atherosclerotic risk in other settings but cannot reliably identify the intrastent mechanism needed to plan this repeat intervention.'),
 ('Repeat exercise ECG to distinguish neointimal hyperplasia from underexpansion','Exercise testing can demonstrate ischemia in suitable patients but cannot identify the structural cause of a known focal intrastent lesion.')],
 [S('Identify the Structural Cause Before Reintervening','**IVUS or OCT helps establish the mechanism of stent failure.** The 2023 SCAI consensus emphasizes imaging because angiography alone provides incomplete information about the stent and surrounding tissue.',
    'Underexpansion, neointimal hyperplasia, neoatherosclerosis and fracture can require different lesion preparation and treatment. Placing another stent without addressing the cause can perpetuate failure.',
    'Select the imaging technique according to the anatomical question, renal function, contrast requirements and expertise. This is structural intravascular imaging, distinct from FFR assessment of physiological lesion significance.'),
  S('Separate Restenosis From Acute Thrombotic Failure','**Stent thrombosis usually presents as an ACS and requires urgent coronary assessment and reperfusion.** Once flow is restored, investigate mechanical and medication-related contributors.',
    'Restenosis commonly produces recurrent angina but can also present as ACS. Time since implantation and symptoms alone therefore cannot establish or exclude thrombosis.',
    'For symptomatic restenosis, image-guided correction and an appropriate drug-coated balloon or repeat drug-eluting stent strategy depend on mechanism, prior layers and anatomy. Recurrent diffuse failure can warrant Heart Team discussion of surgery. Review adherence and secondary prevention in parallel; increasing antiplatelet intensity alone does not correct fixed mechanical underexpansion.')],['STENT','CCS2024'])
rows.insert(57,rows.pop())

if __name__=='__main__':
    coverage=ROOT/'Cardiology/Chapter_02_Coronary_Artery_Disease_ACS_and_Myocardial_Infarction.coverage.json'
    c=json.loads(coverage.read_text(encoding='utf-8'))
    assert len(rows)==c['plannedQuestions']==sum(s['questions'] for s in c['sections']),'Incomplete chapter; do not install'
    index=0
    for section in c['sections']:
        for decision in section['decisions']:
            assert rows[index]['topic']==section['section']
            rows[index]['coverageDecision']=decision
            index+=1
    save('Cardiology',2,c['chapter'],rows,R,'Original educational synthesis; full Harrison subscription text not accessed; independent clinician review not claimed. MI classification explicitly dated to the 2026 Fifth Universal Definition.')
    c.update(status='authored_validated',authoredQuestions=len(rows))
    c['questionDecisions']=[dict(question=i+1,title=r['title'],decision=r['coverageDecision']) for i,r in enumerate(rows)]
    coverage.write_text(json.dumps(c,ensure_ascii=False,indent=2),encoding='utf-8')
