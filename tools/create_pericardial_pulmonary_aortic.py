"""Original combined pericardial, pulmonary vascular and aortic chapter."""
import json
from qbank_authoring import ROOT,question,ref,finalize
PER=ref('2025 ESC Myocarditis and Pericarditis Guideline','https://doi.org/10.1093/eurheartj/ehaf192')
PH=ref('2022 ESC/ERS Pulmonary Hypertension Guideline','https://doi.org/10.1093/eurheartj/ehac237')
AO=ref('2022 ACC/AHA Aortic Disease Guideline','https://doi.org/10.1016/j.jacc.2022.08.004')
rows=json.loads((ROOT/'drafts/Cardiology/08. Pericardial Disease/pericardial-draft.json').read_text(encoding='utf-8'))['questions'][:1]
def q(*args,**kwargs):rows.append(question(*args,**kwargs))
q('A patient has sharp chest pain improved by sitting forward, a friction rub and diffuse concave ST elevation with PR depression. Which diagnosis is most likely?',
 'Acute pericarditis',[
 ('A focal inferior occlusive MI','The distributed ECG and positional pleuritic syndrome favor pericardial inflammation, although ischemia must be assessed when uncertain.'),
 ('Isolated stable angina','Stable angina does not explain the rub and characteristic diffuse inflammatory ECG changes.'),
 ('Uncomplicated chronic constriction without active inflammation','The acute pain and ECG syndrome indicates active pericardial inflammation rather than a purely chronic filling disorder.')],
 'Recognize a pericardial inflammatory syndrome',
 '**Typical pain, a rub and compatible ECG changes support acute pericarditis.**',
 ['An effusion can be present but is not required.', 'Troponin elevation or ventricular abnormalities raise the possibility of associated myocarditis.'],
 '**Assess cause and risk before choosing outpatient care.**',
 ['Fever, a large effusion, tamponade, a subacute course or poor treatment response require closer evaluation.', 'Do not dismiss a possible ACS from ECG shape alone when clinical features are concerning.'],
 [['Pericarditis','Pleuritic positional pain, rub, diffuse changes'],['Focal MI','Territorial ischemic pattern and reciprocal changes'],['Myocardial involvement','Assess troponin and function']], [PER], 'clinical_scenario')
q('Which ECG pattern is more supportive of acute pericarditis than a single-territory STEMI?',
 'Widespread ST elevation with PR depression and reciprocal PR elevation in aVR',[
 ('Inferior ST elevation with reciprocal lateral ST depression','That distribution raises concern for a territorial occlusive infarction.'),
 ('Persistent localized Q waves with matching scar','That supports a prior infarct pattern rather than defining active pericarditis.'),
 ('A delta wave with a short PR','That is ventricular pre-excitation rather than a pericarditis pattern.')],
 'Distributed inflammation differs from a focal arterial territory',
 '**Pericardial and superficial atrial inflammation can produce widespread ST and PR changes.**',
 ['Not every case follows a textbook sequence of ECG stages.', 'Localized postoperative or infarct-associated inflammation can be atypical.'],
 '**Use the ECG within the clinical syndrome.**',
 ['Persistent ischemic symptoms or territorial reciprocal changes require urgent coronary assessment.', 'Echo and biomarkers help identify effusion and myocardial involvement.'],
 [['Diffuse ST/PR changes','Supports pericarditis'],['Territorial reciprocal pattern','Consider acute coronary occlusion'],['Normal ECG','Does not independently exclude pericarditis']], [PER])
q('A patient with recent MI has pleuritic pain and a rub but also recurrent pressure-like discomfort and a new dynamic territorial ST change. What is the correct approach?',
 'Reassess for recurrent ischemia rather than attributing every symptom to pericarditis',[
 ('A rub excludes concurrent coronary ischemia','Different processes can coexist.'),
 ('A persistently elevated post-MI troponin alone proves reinfarction','New biomarker dynamics and ischemic evidence must be interpreted in context.'),
 ('Pericardial pain makes all further ECG assessment unnecessary','A changing territorial pattern is clinically important.')],
 'Avoid diagnostic anchoring after a recent infarct',
 '**An inflammatory clue does not exclude a new ischemic event.**',
 ['Compare serial ECGs and biomarker changes with the recent baseline.', 'Assess hemodynamics and ventricular function when complications are possible.'],
 '**Treat the most urgent plausible process while resolving uncertainty.**',
 ['Recurrent coronary occlusion may require immediate invasive assessment.', 'The pericarditis diagnosis should be supported rather than used to explain every later symptom automatically.'],
 [['Positional pleuritic pain and rub','Supports pericarditis'],['New territorial dynamic ischemia','Requires coronary reassessment'],['Recent baseline troponin elevation','Not sufficient alone for reinfarction']], [PER], 'clinical_scenario')
q('A low-risk patient has uncomplicated idiopathic acute pericarditis without contraindications to first-line therapy. Which regimen is generally appropriate?',
 'Aspirin or an NSAID plus colchicine, with appropriate gastroprotection',[
 ('High-dose corticosteroid alone as the default for every first episode','Steroids are not the routine first choice and can promote dependence or recurrence.'),
 ('Anticoagulation as the principal anti-inflammatory treatment','Anticoagulation does not treat pericardial inflammation.'),
 ('Colchicine as an antibacterial substitute in purulent pericarditis','A bacterial cause requires antimicrobial and drainage management, not this idiopathic regimen.')],
 'Treat inflammation and reduce recurrence',
 '**An aspirin/NSAID-based course with colchicine is standard first-line care in an appropriate patient.**',
 ['Drug selection and dose depend on comorbidity, renal function, bleeding risk and interactions.', 'Tapering follows clinical and inflammatory improvement rather than an arbitrary short exposure.'],
 '**Confirm that the patient fits an uncomplicated phenotype.**',
 ['A specific infectious, autoimmune or malignant cause changes treatment.', 'Provide activity advice, symptom review and a plan for recurrence or deterioration.'],
 [['Aspirin/NSAID','Anti-inflammatory symptom control'],['Colchicine','Reduces recurrent disease'],['Specific cause','Requires additional targeted care']], [PER])
q('Which treatment pattern can increase the risk of recurrent pericarditis?',
 'Unnecessary high-dose corticosteroids followed by rapid tapering',[
 ('Appropriate colchicine use with a tolerated anti-inflammatory regimen','Colchicine reduces recurrence in suitable patients.'),
 ('A gradual individualized taper after remission','That is more consistent with preventing relapse than a rapid unplanned withdrawal.'),
 ('Correction of an identified specific cause','Treating the cause is generally appropriate.')],
 'Steroid exposure and tapering can influence disease course',
 '**Corticosteroids have selected indications but are not a harmless default.**',
 ['High doses and fast tapering can promote relapse or dependence.', 'Exclude an untreated infectious cause before immunosuppression when relevant.'],
 '**When steroids are necessary, use a planned regimen.**',
 ['Follow symptoms and inflammatory activity during taper.', 'Maintain appropriate colchicine and address the underlying cause when possible.'],
 [['Selected steroid indication','Use the lowest appropriate planned regimen'],['High-dose/rapid taper','Recurrence concern'],['Colchicine','Important recurrence-prevention role']], [PER])
q('A patient has inflammatory recurrent pericarditis with colchicine resistance, steroid dependence and persistently elevated CRP after exclusion of infection. Which targeted pathway has evidence?',
 'IL-1 inhibition with an agent such as anakinra or rilonacept',[
 ('Routine TNF stimulation','That is not the evidence-supported anti-inflammatory strategy.'),
 ('A direct thrombin inhibitor to suppress CRP','Anticoagulation is not the targeted inflammatory mechanism.'),
 ('Escalating corticosteroids indefinitely without a steroid-sparing assessment','Dependence and recurrence justify reassessing the treatment pathway.')],
 'Refractory inflammatory pericarditis can be IL-1 mediated',
 '**Anti-IL-1 treatment has evidence in selected recurrent inflammatory disease.**',
 ['The phenotype, prior treatment response and exclusion of infection matter.', 'CMR evidence can help establish inflammation when systemic markers are not decisive.'],
 '**Use a specialist steroid-sparing plan.**',
 ['Screen for relevant infection and monitor according to the agent.', 'Do not apply the same strategy to every noninflammatory effusion or unexplained chest pain.'],
 [['Inflammatory steroid-dependent recurrence','Consider IL-1 pathway therapy'],['Noninflammatory effusion','Different evaluation'],['Treatment planning','Cause and safety assessment']], [PER], 'clinical_scenario')
q('Which acute pericarditis presentation favors hospital assessment rather than routine low-risk outpatient treatment?',
 'High fever with a large effusion and a subacute course',[
 ('Typical pain improving promptly with first-line treatment and no effusion','That is more consistent with a low-risk presentation after appropriate assessment.'),
 ('A normal temperature and stable hemodynamics without adverse features','Those findings do not define the high-risk pattern.'),
 ('A brief self-limited episode with no recurrence or concerning cause','That alone does not establish a hospital-level risk feature.')],
 'Identify features suggesting complications or a specific cause',
 '**Fever, large effusion, tamponade, subacute onset and poor response warrant closer evaluation.**',
 ['Immunosuppression, trauma, anticoagulation and myocardial involvement can add concern.', 'The purpose is to identify etiology and complications rather than merely control pain.'],
 '**Escalate according to the whole presentation.**',
 ['Obtain echo and directed investigations.', 'A large effusion does not automatically equal tamponade, but it changes follow-up and diagnostic needs.'],
 [['Low-risk uncomplicated pattern','May be managed as outpatient'],['Adverse features','Hospital and etiological assessment'],['Hemodynamic compromise','Urgent drainage pathway']], [PER])
q('What is pulsus paradoxus in the conventional bedside definition?',
 'An inspiratory fall in systolic arterial pressure greater than 10 mm Hg',[
 ('An inspiratory rise in systolic pressure greater than 10 mm Hg','The conventional finding is an excessive fall, not rise.'),
 ('Alternation of strong and weak beats without a respiratory relationship','That describes pulsus alternans.'),
 ('A fixed difference between right and left arm pressure','That is a different vascular finding.')],
 'Respiratory ventricular interaction can reduce inspiratory LV output',
 '**Tamponade exaggerates the normal inspiratory fall in systolic pressure.**',
 ['Limited total cardiac volume increases ventricular interdependence.', 'The sign is not unique to tamponade and can occur with severe obstructive respiratory disease.'],
 '**Absence does not exclude tamponade in every setting.**',
 ['Atrial septal communication, severe AR and other hemodynamic conditions can modify the sign.', 'Use examination, echo and clinical perfusion together.'],
 [['Pulsus paradoxus','Respiratory systolic fall greater than 10 mm Hg'],['Pulsus alternans','Beat-to-beat amplitude alternation'],['Tamponade diagnosis','Integrated clinical and echo assessment']], [PER])
q('A patient with a large pericardial effusion has hypotension, oliguria and echo evidence of tamponade. What is the definitive immediate management direction?',
 'Urgent pericardial drainage with appropriate procedural expertise',[
 ('High-dose diuresis as the principal definitive treatment','Reducing preload can worsen tamponade and does not remove the external constraint.'),
 ('Wait for anti-inflammatory drugs to shrink the effusion despite shock','Hemodynamic compromise requires urgent decompression.'),
 ('Exercise testing to confirm the severity','This is inappropriate in an unstable patient.')],
 'Tamponade is a hemodynamic emergency',
 '**Fluid under pressure impairs filling and forward output.**',
 ['Drainage method depends on cause, fluid characteristics and local expertise.', 'Purulent, traumatic or loculated collections may need a surgical approach.'],
 '**Support perfusion while arranging definitive relief.**',
 ['Avoid unnecessary preload reduction and use ventilatory support carefully.', 'Investigate the cause after immediate stabilization rather than delaying drainage for nonessential testing.'],
 [['Effusion without compromise','Cause and monitoring pathway'],['Tamponade with shock','Urgent drainage'],['Loculated/purulent or traumatic disease','May need surgical management']], [PER], 'clinical_scenario')
q('Why can a relatively small rapidly accumulating pericardial effusion cause tamponade while a much larger slowly accumulating effusion does not?',
 'The pericardial pressure-volume relationship depends on the rate of accumulation and capacity for stretch',[
 ('Tamponade depends only on the measured fluid volume','Volume alone is insufficient.'),
 ('Slow fluid never raises pressure regardless of amount','Large chronic effusions can still decompensate.'),
 ('A small effusion cannot affect cardiac filling','Rapid hemopericardium can cause critical compression.')],
 'Pressure, not volume alone, defines the constraint',
 '**A rapidly filled pericardial space reaches the steep pressure-volume range sooner.**',
 ['Slow accumulation permits some adaptation.', 'Baseline chamber pressures and pericardial properties also influence hemodynamic effects.'],
 '**Assess physiology rather than judging danger from the image size alone.**',
 ['Look at perfusion, chamber collapse and respiratory flow findings.', 'A changing clinical state can make a previously tolerated effusion dangerous.'],
 [['Rapid accumulation','High pressure at smaller volume'],['Slow accumulation','Greater accommodation possible'],['Tamponade','Clinical filling compromise']], [PER])
q('Which chamber-collapse timing is characteristic of pericardial tamponade physiology?',
 'Right atrial collapse during its low-pressure phase and RV free-wall collapse in early diastole',[
 ('RV collapse only during peak systolic pressure as the usual hallmark','The RV is more vulnerable when intracavitary pressure is low in early diastole.'),
 ('LA systolic expansion alone as definitive proof','That is not the standard chamber-collapse pattern.'),
 ('No relationship between chamber pressure and collapse','External pressure relative to intracavitary pressure is central.')],
 'External pressure compresses the lowest-pressure chamber phases first',
 '**Collapse depends on the relation between pericardial and chamber pressure.**',
 ['RA inversion and early-diastolic RV collapse support tamponade in the right context.', 'High right-sided pressures can reduce or eliminate these classic signs.'],
 '**An echo sign is not the whole clinical diagnosis.**',
 ['Assess IVC, respiratory Doppler variation and perfusion.', 'Do not drain solely from a borderline isolated sign without considering the full presentation.'],
 [['RA/RV low-pressure phases','Most vulnerable to compression'],['High pulmonary/right-sided pressure','Can mask typical collapse'],['Clinical tamponade','Requires integrated hemodynamic assessment']], [PER])
q('Which invasive finding alone is insufficient to distinguish constrictive pericarditis from restrictive cardiomyopathy?',
 'A ventricular dip-and-plateau diastolic pressure pattern',[
 ('Marked respiratory LV/RV systolic discordance','This is more discriminating for constriction in an appropriate recording.'),
 ('Clear dissociation of intrathoracic and intracardiac pressure transmission','This is a mechanistic feature favoring constriction.'),
 ('An integrated echo and CMR demonstration of a constrictive process','A convergent assessment is more informative than the isolated shared sign.')],
 'Some classic filling signs are shared',
 '**Rapid early filling followed by abrupt limitation can occur in both constriction and restriction.**',
 ['Similar diastolic pressure elevation is also not uniquely diagnostic.', 'Respiratory ventricular interaction is more useful for differentiation.'],
 '**Avoid overdiagnosis from a memorable waveform.**',
 ['Review simultaneous respiratory recordings and imaging.', 'Mixed pericardial and myocardial disease can complicate the pattern.'],
 [['Dip-and-plateau','Shared, less specific'],['Respiratory systolic discordance','Favors constriction'],['Respiratory concordance','Favors restriction']], [PER])
q('A patient has recent-onset constrictive physiology, elevated CRP and pericardial enhancement without advanced chronic features. Which possibility matters before assuming immediate permanent fibrotic constriction?',
 'Transient inflammatory constriction that may improve with appropriate anti-inflammatory treatment',[
 ('Every constrictive pattern is inevitably irreversible','Inflammatory forms can improve.'),
 ('A normal pericardial thickness excludes all constriction','Constriction can occur without striking thickening.'),
 ('The physiology proves an isolated coronary stenosis','The findings concern pericardial restraint, not a proven focal coronary lesion.')],
 'Constrictive physiology can have a reversible inflammatory component',
 '**Recent active inflammation can create temporary restraint.**',
 ['CRP and CMR help assess activity.', 'Advanced chronic calcific and fibrotic disease has a different likelihood of medical reversibility.'],
 '**Use monitored treatment and reassessment in a suitable stable patient.**',
 ['Persistent symptomatic chronic constriction may require pericardiectomy.', 'Do not delay definitive care indefinitely when the clinical course is worsening.'],
 [['Active recent inflammatory constriction','Potentially reversible'],['Chronic fibrotic symptomatic constriction','Assess pericardiectomy'],['Follow-up','Reassess physiology and response']], [PER], 'clinical_scenario')
q('After drainage of a pressurized pericardial effusion, right atrial pressure remains elevated and constrictive filling persists. Which syndrome is suggested?',
 'Effusive-constrictive pericarditis',[
 ('A fully resolved uncomplicated tamponade with normal filling','Persistent constrictive physiology contradicts complete hemodynamic resolution.'),
 ('Pure isolated acute MR','The post-drainage pericardial filling pattern points elsewhere.'),
 ('Aortic coarctation','That does not explain the relationship to effusion drainage.')],
 'Relieving fluid pressure can reveal a second constraint',
 '**An effusion and a constricting visceral pericardial process can coexist.**',
 ['The effusive component may mask the constrictive component initially.', 'Persistent elevated RA pressure requires consideration of other causes too, including RV dysfunction or severe TR.'],
 '**Reassess the entire hemodynamic picture after drainage.**',
 ['Echo, inflammation assessment and selected invasive data guide next steps.', 'Some inflammatory cases improve medically, while persistent disease can need surgery.'],
 [['Before drainage','Effusion-related compression'],['After drainage','Persistent constrictive physiology'],['Differential','Exclude other right-sided pressure causes']], [PER], 'clinical_scenario')
q('Which statement about pericardial thickness and constriction is correct?',
 'Normal thickness does not exclude constrictive physiology',[
 ('Every calcified pericardium necessarily causes clinical constriction','An anatomical abnormality does not establish its hemodynamic effect.'),
 ('Thickness alone fully determines the surgical indication','Symptoms and physiological consequences matter.'),
 ('CMR or CT anatomy can replace all functional assessment','Morphological and functional data are complementary.')],
 'Anatomy and physiology are not interchangeable',
 '**A pericardium can constrain filling without dramatic thickening.**',
 ['Calcification or thickening can also exist without severe functional constraint.', 'Echo and selected invasive assessment demonstrate ventricular interaction and filling effects.'],
 '**Use imaging methods for their complementary strengths.**',
 ['CT maps calcification and surgical anatomy.', 'CMR can assess inflammation, thickness and dynamic interaction.'],
 [['CT','Calcification and anatomy'],['CMR','Tissue activity and dynamic assessment'],['Echo/hemodynamics','Functional consequences']], [PER])

# Pulmonary vascular disease and aortic syndromes follow.
q('Which resting right-heart catheterization profile meets the 2022 definition of precapillary PH?',
 'Mean PA pressure 28 mm Hg, wedge pressure 10 mm Hg and PVR 4 Wood units',[
 ('Mean PA pressure 18 mm Hg, wedge 10 and PVR 1.5','The mean PA pressure is not above the PH threshold.'),
 ('Mean PA pressure 30 mm Hg, wedge 22 and PVR 1.5','The elevated wedge indicates postcapillary PH.'),
 ('Mean PA pressure 24 mm Hg, wedge 12 and PVR 1.5','PVR is not above 2 Wood units, so this does not meet the complete precapillary definition.')],
 'PH classification needs pressure, wedge and resistance',
 '**Precapillary PH requires mean PA pressure above 20, wedge at most 15 and PVR above 2.**',
 ['PAH is one cause of this profile, not a synonym for every precapillary case.', 'CTEPH and lung-associated PH must be distinguished.'],
 '**Confirm measurement quality and cause before therapy.**',
 ['Wedge accuracy and cardiac output method affect classification.', 'Echo estimates probability but does not replace definitive invasive characterization when indicated.'],
 [['Precapillary PH','mPAP above 20, PAWP at most 15, PVR above 2'],['Postcapillary PH','PAWP above 15'],['PAH','Precapillary phenotype with appropriate group 1 cause']], [PH])
q('Mean PA pressure is 42 mm Hg, wedge pressure 12 mm Hg and cardiac output 5 L/min. What is PVR?',
 '6 Wood units',[
 ('8.4 Wood units','This incorrectly divides mean PA pressure by output without subtracting wedge.'),
 ('10.8 Wood units','Adding wedge instead of subtracting it produces this error.'),
 ('2.4 Wood units','Dividing wedge alone by output does not calculate PVR.')],
 'Resistance uses the transpulmonary pressure difference',
 '**PVR equals (mean PA pressure minus wedge pressure) divided by cardiac output.**',
 ['Here (42-12)/5 = 6 Wood units.', 'Pressure and output measurements must be reliable and obtained in the relevant physiological state.'],
 '**A numerical PVR is not an etiology.**',
 ['Assess wedge, clinical disease and vascular imaging to determine PH group.', 'High resistance can arise from different disorders needing different treatment.'],
 [['Pressure difference','42 minus 12 = 30 mm Hg'],['Flow','5 L/min'],['Resistance','30/5 = 6 Wood units']], [PH])
q('A patient has unexplained precapillary PH. Which screening imaging test is particularly important to exclude chronic thromboembolic disease?',
 'Ventilation-perfusion lung scanning',[
 ('A normal chest radiograph alone','A radiograph cannot reliably exclude chronic perfusion obstruction.'),
 ('Coronary calcium scoring','That does not assess pulmonary perfusion defects.'),
 ('A single normal D-dimer as definitive exclusion','D-dimer does not rule out chronic organized thromboembolic disease.')],
 'CTEPH must be actively excluded',
 '**A V/Q scan is a sensitive screening tool for chronic mismatched perfusion defects.**',
 ['A normal perfusion scan strongly argues against CTEPH in the appropriate setting.', 'An abnormal scan requires anatomical and hemodynamic evaluation rather than diagnosing operability from the scan alone.'],
 '**Do not classify all precapillary disease as idiopathic PAH.**',
 ['CTEPH has potentially definitive mechanical treatment options.', 'Expert review includes CT angiography and selected pulmonary angiography.'],
 [['V/Q','Screening for chronic perfusion obstruction'],['CT/angiography','Defines anatomical lesions'],['RHC','Defines hemodynamic burden']], [PH])
q('A patient with HFpEF has mean PA pressure 34 mm Hg, wedge 24 mm Hg and PVR 1.7 Wood units. Which category fits?',
 'Isolated postcapillary PH',[
 ('Idiopathic PAH','The elevated wedge supports left-heart-related postcapillary disease.'),
 ('Combined post- and precapillary PH','The current PVR threshold for a precapillary component is above 2; this value does not meet it.'),
 ('No PH because EF is preserved','Preserved EF does not prevent raised left-sided filling pressure or PH.')],
 'High wedge pressure localizes an important upstream burden',
 '**Postcapillary PH has wedge pressure above 15 mm Hg.**',
 ['PVR at most 2 supports the isolated postcapillary category.', 'PVR above 2 would indicate a combined component in this framework.'],
 '**Treat the left-heart disease and congestion.**',
 ['Do not automatically prescribe a PAH regimen from the PA pressure alone.', 'When wedge measurement is uncertain or discordant, verify technique and clinical context.'],
 [['PAWP above 15, PVR at most 2','Isolated postcapillary PH'],['PAWP above 15, PVR above 2','Combined post/precapillary PH'],['PAWP at most 15 with high PVR','Precapillary profile']], [PH], 'clinical_scenario')
q('What is a positive acute vasoreactivity response in appropriate idiopathic, heritable or drug-associated PAH?',
 'Mean PA pressure falls by at least 10 mm Hg to 40 mm Hg or less with unchanged or increased cardiac output',[
 ('Mean PA pressure falls by 5 mm Hg while output collapses','A fall caused by failing output is not the required response.'),
 ('Systolic systemic pressure rises regardless of PA pressure','The criterion concerns pulmonary hemodynamics and preserved output.'),
 ('Any oxygen saturation increase without pressure measurements','That does not establish the required vasoreactive phenotype.')],
 'Only a selected PAH subgroup is tested for CCB responsiveness',
 '**The response identifies potential candidates for high-dose CCB therapy.**',
 ['Testing uses a suitable short-acting pulmonary vasodilator in an expert setting.', 'The criterion is not a general screening rule for every PH group.'],
 '**Preserved output is essential to interpreting the pressure fall.**',
 ['A lower pressure from a lower flow can reflect deterioration.', 'Long-term response requires reassessment rather than assuming an acute result guarantees lasting success.'],
 [['Pressure response','Fall at least 10 to at most 40'],['Output','Unchanged or increased'],['Clinical role','Selected PAH CCB assessment']], [PH])
q('A patient with idiopathic PAH has a negative acute vasoreactivity test. What is the implication for high-dose CCB treatment?',
 'Do not prescribe high-dose CCB therapy as an empirical PAH regimen',[
 ('Every PAH patient benefits from the same high-dose CCB strategy','Nonresponders can deteriorate with systemic hypotension or negative inotropy.'),
 ('The test proves that no PAH treatment can work','It addresses CCB suitability, not all targeted therapies.'),
 ('Use verapamil automatically because it is the strongest general PAH drug','That is not an appropriate inference and can be hazardous.')],
 'Vasoreactivity is a treatment-selection test',
 '**Only a small selected group has sustained benefit from high-dose CCBs.**',
 ['A negative result directs care toward other PAH pathways.', 'PH due to left heart or lung disease is not managed by copying this algorithm.'],
 '**Use risk-based targeted therapy at a PH center.**',
 ['Evaluate functional class, exercise capacity, biomarkers and RV function.', 'Reassess treatment response and escalate as appropriate.'],
 [['Positive qualifying response','Potential CCB candidate'],['Negative response','Use other PAH strategies'],['Other PH groups','Cause-specific pathway']], [PH], 'clinical_scenario')
q('A treatment-naive patient has idiopathic PAH, no major cardiopulmonary comorbidity and low-to-intermediate risk. Which initial strategy is commonly recommended?',
 'Combination of an endothelin receptor antagonist and a PDE5 inhibitor',[
 ('A loop diuretic alone as equivalent disease-modifying therapy','Diuretics relieve congestion but do not replace targeted PAH treatment.'),
 ('Routine high-dose CCB despite a negative vasoreactivity test','That is not appropriate for a nonresponder.'),
 ('A PAH drug without identifying the PH group','Targeted treatment requires correct classification.')],
 'Complementary PAH pathways support initial combination therapy',
 '**Endothelin and nitric oxide-cGMP pathways can be targeted together in an appropriate patient.**',
 ['Comorbidity, risk and tolerability influence the regimen.', 'Higher-risk disease may require a prostacyclin-based strategy rather than oral dual therapy alone.'],
 '**Treat toward a low-risk profile with repeated assessment.**',
 ['Review symptoms, exercise performance, NT-proBNP and RV function.', 'A starting prescription is not the end of the treatment algorithm.'],
 [['Suitable low/intermediate-risk PAH','Often ERA plus PDE5 inhibitor'],['High-risk PAH','Consider parenteral prostacyclin strategy'],['Follow-up','Risk-based escalation']], [PH], 'clinical_scenario')
q('A newly diagnosed PAH patient has syncope, severe RV dysfunction, low cardiac output and a high-risk profile. Which treatment direction is appropriate?',
 'Urgent expert-center therapy including a parenteral prostacyclin-based strategy when suitable',[
 ('Wait six months on diuretics alone before reassessment','High-risk disease requires prompt escalation.'),
 ('Treat the PA pressure as benign because wedge is normal','A normal wedge does not make severe precapillary disease benign.'),
 ('Use high-dose beta blockade solely to lower a compensatory heart rate','Reflex suppression can worsen RV output and does not treat the pulmonary vascular burden.')],
 'High-risk PAH needs an intensive strategy',
 '**RV failure and low output predict a dangerous trajectory.**',
 ['Parenteral prostacyclin treatment is important in appropriate high-risk patients.', 'Combination treatment, supportive care and transplant evaluation may be needed.'],
 '**Avoid abrupt interruption of continuous prostacyclin.**',
 ['Interruption can cause severe rebound deterioration.', 'Patient education, infusion support and a reliable backup plan are part of treatment.'],
 [['High-risk RV failure','Urgent advanced PAH therapy'],['Continuous prostacyclin','Requires reliable delivery'],['Persistent risk','Assess transplant and escalation options']], [PH], 'clinical_scenario')
q('A patient has operable CTEPH with surgically accessible organized lesions. Which treatment can be definitive?',
 'Pulmonary endarterectomy at an expert center',[
 ('Repeated systemic fibrinolysis as routine chronic therapy','Organized chronic material is not managed like a fresh acute embolus with repeated lysis.'),
 ('Anticoagulation alone as equivalent removal of established obstruction','Anticoagulation is important but does not remove all organized lesions.'),
 ('Routine coronary bypass grafting','The target is the pulmonary arterial obstructive material.')],
 'CTEPH has a potentially curative mechanical pathway',
 '**Operability depends on anatomy, hemodynamics and expert surgical judgment.**',
 ['Balloon pulmonary angioplasty and medical therapy have important roles in selected inoperable or residual disease.', 'Lifelong anticoagulation is generally part of management.'],
 '**Do not label a patient inoperable without specialist review.**',
 ['An experienced multidisciplinary CTEPH team weighs accessible disease and microvascular burden.', 'Persistent PH after surgery needs reassessment rather than assuming the procedure failed in every respect.'],
 [['Accessible operable disease','Endarterectomy assessment'],['Inoperable/residual disease','BPA and/or targeted medical treatment'],['All pathways','Anticoagulation and expert follow-up']], [PH], 'clinical_scenario')
q('Why should riociguat not be combined with sildenafil?',
 'Both increase cGMP signaling, creating a risk of excessive hypotension',[
 ('They neutralize each other and prevent all vasodilation','The concern is excessive combined effect, not cancellation.'),
 ('Riociguat is an anticoagulant that directly inhibits platelets','It stimulates soluble guanylate cyclase.'),
 ('Sildenafil stabilizes TTR and has no vascular action','Sildenafil inhibits PDE5 and has vascular effects.')],
 'Shared downstream signaling can create a dangerous combination',
 '**Riociguat stimulates sGC while sildenafil reduces cGMP breakdown.**',
 ['Combining these approaches is contraindicated because of hypotension risk.', 'Nitrates create a related important interaction concern.'],
 '**Use an appropriate specialist switching protocol when changing pathways.**',
 ['Do not overlap drugs casually while waiting for a new prescription.', 'Assess pressure, other vasodilators and the actual indication.'],
 [['Riociguat','Stimulates cGMP production'],['Sildenafil','Reduces cGMP breakdown'],['Combination','Excess hypotension risk']], [PH])
q('Which mechanism distinguishes sotatercept from traditional vasodilator-focused PAH drugs?',
 'It modulates activin-related signaling through an activin receptor type IIA ligand-trap approach',[
 ('It is a PDE5 inhibitor identical to sildenafil','Its signaling target is different.'),
 ('It directly dissolves chronic pulmonary emboli','It is not a fibrinolytic or mechanical CTEPH treatment.'),
 ('It provides oxygen by binding hemoglobin as a substitute gas carrier','It is not an oxygen-carrying blood substitute.')],
 'PAH treatment now includes vascular remodeling-related pathways',
 '**Sotatercept targets a signaling balance distinct from endothelin, nitric oxide and prostacyclin pathways.**',
 ['STELLAR demonstrated benefit when added to background therapy in a selected PAH population.', 'Hemoglobin rise, thrombocytopenia, bleeding and telangiectasia are important safety considerations.'],
 '**Use current eligibility and laboratory monitoring.**',
 ['It complements a carefully selected PAH regimen rather than replacing all background treatment.', 'Do not extrapolate the evidence to every PH group.'],
 [['Traditional pathways','Endothelin, NO-cGMP, prostacyclin'],['Sotatercept','Activin-signaling ligand trap'],['Monitoring','Hemoglobin and platelets among key checks']], [ref('STELLAR: Phase 3 Trial of Sotatercept for PAH','https://doi.org/10.1056/NEJMoa2213558')])
q('Which trial-supported treatment may be considered in selected PH associated with interstitial lung disease?',
 'Inhaled treprostinil',[
 ('Automatic use of every oral PAH drug in every ILD patient','Group 3 PH requires cause-specific selection; indiscriminate vasodilator use is not appropriate.'),
 ('Routine ambrisentan for all idiopathic pulmonary fibrosis','This is not the evidence-supported strategy.'),
 ('Fibrinolysis solely because pulmonary pressure is elevated','PH-ILD is not equivalent to an acute embolic event.')],
 'Group 3 PH cannot be managed by copying group 1 treatment wholesale',
 '**INCREASE supports inhaled treprostinil in a selected PH-ILD population.**',
 ['Treat the lung disease, hypoxemia and other contributors.', 'PH severity and referral-center assessment affect selection.'],
 '**Keep the indication specific.**',
 ['Results do not establish benefit for all pulmonary vasodilators in all chronic lung diseases.', 'Monitor exercise tolerance, oxygenation and adverse effects.'],
 [['PH-ILD','Selected inhaled treprostinil evidence'],['Other group 3 disease','Do not assume equivalent benefit'],['Foundational care','Lung disease and oxygenation management']], [PH,ref('INCREASE: Inhaled Treprostinil in Pulmonary Hypertension Due to Interstitial Lung Disease','https://doi.org/10.1056/NEJMoa2008470')])

# Aortic disease items complete the chapter.
q('An acute dissection involves the ascending aorta and extends into the descending segment. What is its Stanford classification and usual definitive pathway?',
 'Type A; emergency surgical evaluation',[
 ('Type B because the descending aorta is also involved','Any ascending involvement defines type A.'),
 ('Type B; routine outpatient pressure review only','This misclassifies a proximal surgical emergency.'),
 ('Type A; fibrinolysis as standard definitive treatment','Fibrinolysis is not treatment of dissection and can cause catastrophic bleeding.')],
 'Ascending involvement determines Stanford type A',
 '**The distal extent does not change a dissection with ascending involvement into type B.**',
 ['Tamponade, AR, coronary compromise and malperfusion are important complications.', 'Emergency aortic surgical care is usually required.'],
 '**Stabilize while arranging definitive treatment.**',
 ['Control impulse and pain while preserving organ perfusion.', 'Do not delay referral for unnecessary repeat imaging when the diagnosis and surgical need are already clear.'],
 [['Type A','Any ascending involvement'],['Type B','No ascending involvement'],['Acute type A','Emergency surgical pathway']], [AO], 'clinical_scenario')
q('A patient has acute type B dissection without rupture, malperfusion, persistent pain, uncontrolled hypertension or rapid expansion. What is the usual initial approach?',
 'Intensive medical anti-impulse treatment and close surveillance',[
 ('Emergency open ascending replacement solely because all dissections are type A','Type B lacks ascending involvement and has a different initial pathway.'),
 ('No monitoring once the first analgesic dose works','Early surveillance is essential.'),
 ('Systemic anticoagulation as a universal substitute for impulse control','Anticoagulation does not treat aortic wall stress and is not a universal dissection therapy.')],
 'Uncomplicated type B disease differs from proximal or complicated disease',
 '**Initial medical treatment targets shear stress, pressure and pain.**',
 ['Monitor for evolving malperfusion, rupture and persistent symptoms.', 'Selected high-risk anatomical features can affect discussion of earlier endovascular treatment.'],
 '**Classification is dynamic during the acute course.**',
 ['A new complication can change the intervention need.', 'Long-term imaging and pressure treatment remain necessary after discharge.'],
 [['Uncomplicated type B','Initial medical management'],['Complicated type B','Intervention assessment'],['Follow-up','Serial aortic imaging']], [AO], 'clinical_scenario')
q('A type B dissection causes ongoing mesenteric malperfusion and persistent pain despite treatment. What is appropriate?',
 'Urgent aortic-team assessment for intervention, often TEVAR when anatomy is suitable',[
 ('Continue the same outpatient regimen because descending dissections never need intervention','Malperfusion makes the disease complicated.'),
 ('Treat only the lactate without addressing aortic flow','The organ ischemia mechanism requires urgent correction assessment.'),
 ('Fibrinolysis as the standard solution for a compressed true lumen','The lesion is a dissection-related flow problem, not a routine lysis indication.')],
 'Complications change type B management',
 '**Rupture, malperfusion, refractory pain and uncontrolled hypertension are important intervention signals.**',
 ['TEVAR can cover the entry tear and improve true-lumen perfusion in suitable anatomy.', 'Some branch-vessel or anatomical problems require additional approaches.'],
 '**Treat organ perfusion as an emergency.**',
 ['Assess bowel, kidney, limb and spinal circulation.', 'Aortic and vascular expertise determines the definitive strategy.'],
 [['Uncomplicated type B','Medical pathway'],['Malperfusion or rupture','Urgent intervention pathway'],['TEVAR suitability','Anatomy and disease context dependent']], [AO], 'clinical_scenario')
q('In acute aortic syndrome with hypertension and tachycardia, why is a titratable beta blocker generally given before a potent vasodilator when no contraindication exists?',
 'To reduce heart rate and contractile impulse and limit reflex tachycardia from vasodilation',[
 ('A vasodilator alone always suppresses sympathetic tachycardia','It can provoke reflex tachycardia.'),
 ('Beta blockade dissolves the intimal flap','The goal is impulse reduction, not flap dissolution.'),
 ('Heart rate has no effect on aortic wall stress','Rate and contractility are relevant components.')],
 'Anti-impulse therapy addresses more than systolic pressure',
 '**Reducing the force and frequency of ejection can lower aortic stress.**',
 ['IV beta blockade is a usual initial approach in an appropriate patient.', 'A vasodilator can then be added if pressure remains high.'],
 '**Preserve organ perfusion and account for contraindications.**',
 ['Shock, severe acute AR, bradycardia or other circumstances require individualized treatment.', 'Analgesia also helps reduce adrenergic drive.'],
 [['Beta blocker first when suitable','Rate and impulse control'],['Vasodilator added','Additional pressure control'],['Clinical constraints','Perfusion and specific lesion physiology']], [AO])
q('Under the 2022 ACC/AHA acute aortic syndrome framework, which hemodynamic target is appropriate when perfusion permits?',
 'Heart rate 60-80/min and systolic pressure below 120 mm Hg or the lowest pressure maintaining organ perfusion',[
 ('Heart rate above 120/min to maximize shear','This increases rather than reduces impulse.'),
 ('Systolic pressure below 70 mm Hg regardless of consciousness or urine output','Organ perfusion limits pressure reduction.'),
 ('Pressure reduction without attention to rate, pain or perfusion','The treatment is an integrated anti-impulse strategy.')],
 'Targets are constrained by perfusion',
 '**The objective is lower aortic stress without causing ischemic organ injury.**',
 ['Use monitored titration rather than a fixed large oral dose.', 'Assess neurological status, urine output and other perfusion markers.'],
 '**A target is not a reason to ignore a complication.**',
 ['Hypotension can indicate rupture, tamponade or severe AR.', 'Reassess the lesion when the clinical state changes.'],
 [['Rate','60-80/min in the specified framework'],['Pressure','Below 120 or lowest perfusing level'],['Monitoring','Organ perfusion and evolving complications']], [AO])
q('A stable patient has suspected acute aortic dissection. Which study usually provides rapid assessment of the full aorta and branch-vessel involvement?',
 'CT angiography with an appropriate acute-aortic protocol',[
 ('A normal chest radiograph as definitive exclusion','A radiograph cannot rule out dissection.'),
 ('Exercise ECG before anatomical imaging','Exercise is inappropriate in a suspected aortic emergency.'),
 ('Coronary calcium scoring without contrast as an equivalent study','That does not define the dissection lumen or branch perfusion.')],
 'Acute aortic imaging must define extent and complications',
 '**CTA is often the fastest comprehensive test in a stable patient.**',
 ['Assess the ascending aorta, distal extent and malperfusion.', 'Protocol quality matters, including motion control for the proximal aorta when feasible.'],
 '**Choose a different bedside approach when transport is unsafe.**',
 ['TOE can be valuable in an unstable patient.', 'A negative limited study should not close a high-probability case without considering its blind spots.'],
 [['Stable suspected dissection','CTA often first comprehensive study'],['Unstable/unsafe transport','Bedside TOE may be preferable'],['Plain radiograph','Cannot exclude dissection']], [AO], 'clinical_scenario')
q('An unstable patient has suspected proximal dissection with tamponade and cannot safely leave the resuscitation area. Which imaging option can rapidly clarify the proximal anatomy at bedside?',
 'Transesophageal echocardiography',[
 ('A delayed outpatient MRI appointment','This does not meet the emergency need.'),
 ('A screening abdominal ultrasound as complete thoracic assessment','It cannot define the full proximal thoracic lesion.'),
 ('A treadmill stress test','This is inappropriate and unsafe in the stated emergency.')],
 'Imaging choice depends on stability and access',
 '**TOE can assess the proximal aorta, AR and pericardial complications without transporting an unstable patient to CT.**',
 ['It requires suitable expertise and airway considerations.', 'Some aortic segments are less well visualized, so interpret the study\'s limits.'],
 '**Mobilize definitive care in parallel.**',
 ['Do not postpone surgical consultation while pursuing a perfect test sequence.', 'The clinical question is urgent anatomical confirmation and complication assessment.'],
 [['TOE','Bedside proximal and cardiac complication assessment'],['CTA','Comprehensive stable-patient anatomy'],['MRI','Useful selected setting, often less practical acutely']], [AO], 'clinical_scenario')
q('CT shows crescentic high-attenuation thickening of the aortic wall without a clearly flowing false lumen. Which acute aortic syndrome is suggested?',
 'Intramural hematoma',[
 ('A simple uncomplicated atherosclerotic plaque as the only possibility','Acute crescentic wall blood is a different finding.'),
 ('An isolated pericardial cyst','The abnormality is within the aortic wall.'),
 ('A routine PDA','A ductal connection does not explain this wall appearance.')],
 'Acute aortic disease need not show a classic double lumen',
 '**Intramural hematoma involves hemorrhage within the aortic wall.**',
 ['A clear intimal flap or patent false lumen may not be visible.', 'It can progress to dissection or rupture.'],
 '**Location and complications guide management.**',
 ['Ascending involvement and adverse features require urgent aortic-team assessment.', 'Serial imaging tracks progression in a medically managed case.'],
 [['Classic dissection','Intimal flap with true/false lumen'],['Intramural hematoma','Wall hemorrhage without obvious flowing false lumen'],['Management','Location and complication dependent']], [AO])
q('A focal atherosclerotic ulcer penetrates through the aortic intima into the media. What is this lesion?',
 'Penetrating atherosclerotic ulcer',[
 ('A congenital sinus venosus ASD','That is an atrial/pulmonary venous abnormality.'),
 ('A purely mucosal esophageal ulcer','The described lesion is in the aortic wall.'),
 ('A stable nonpenetrating plaque by definition','Penetration into the media is the defining distinction.')],
 'An atherosclerotic plaque can initiate acute wall injury',
 '**Penetrating aortic ulcer can coexist with intramural hematoma.**',
 ['Symptoms, depth, size, growth and rupture features influence risk.', 'Older patients with diffuse atherosclerosis are a common clinical context.'],
 '**Use an aortic-specific surveillance or intervention plan.**',
 ['An incidental stable lesion and a painful complicated ulcer are not managed identically.', 'Control cardiovascular risk and blood pressure while assessing the local lesion.'],
 [['Penetrating ulcer','Atherosclerotic intimal lesion into media'],['Associated hematoma','Can signal additional wall injury'],['Decision','Symptoms and adverse anatomical features']], [AO])
q('Under the 2022 ACC/AHA framework, a patient with Marfan syndrome has an aortic root diameter 5.1 cm. What is the appropriate direction?',
 'Evaluate for prophylactic aortic root surgery at an experienced center',[
 ('Wait until 6.5 cm in every patient','Marfan thresholds are lower because of inherited aortic risk.'),
 ('Treat root size as irrelevant if the patient has no pain','Prophylactic intervention aims to prevent an acute event.'),
 ('Use a coronary stent to stabilize the root','A coronary stent does not repair root aneurysm.')],
 'Inherited aortopathy uses lower prophylactic thresholds',
 '**Aortic root surgery is recommended around 5.0 cm in Marfan syndrome in the specified guideline.**',
 ['A lower threshold can be appropriate with high-risk features such as rapid growth or family dissection.', 'Body size, valve status and pregnancy planning can influence the discussion.'],
 '**Use longitudinal measurements and consistent technique.**',
 ['Confirm dimensions and growth with appropriate imaging.', 'Medical therapy and surveillance remain important before and after intervention.'],
 [['Marfan root at least 5.0 cm','Prophylactic surgery assessment'],['High-risk features','May justify earlier intervention'],['No symptoms','Does not eliminate aneurysm risk']], [AO], 'clinical_scenario')
q('A patient with bicuspid aortic valve is being evaluated for an ascending aneurysm. Which factor can lower the intervention threshold from the default size-based approach?',
 'Rapid aortic growth or a family history of dissection',[
 ('A normal current oxygen saturation','That does not define inherited aortic risk.'),
 ('A soft murmur as proof of no aortic risk','Murmur intensity does not quantify the aneurysm.'),
 ('A normal resting troponin as proof that the aorta is stable','Troponin does not establish aortic stability.')],
 'Diameter is central but not the sole aortopathy variable',
 '**Bicuspid-associated aortic decisions include growth, family history, phenotype and planned valve surgery.**',
 ['The 2022 guideline uses a default 5.5-cm recommendation with selected earlier pathways.', 'Concomitant valve surgery can justify addressing a smaller dilated ascending aorta in an appropriate patient.'],
 '**Plan the valve and aorta together.**',
 ['Assess the root and ascending segment, valve function and family history.', 'Use serial imaging rather than one measurement without context.'],
 [['Default diameter framework','Modified by risk and context'],['Rapid growth/family dissection','Important adverse features'],['Planned valve surgery','Can change concomitant aortic decision']], [AO])
q('Under the 2022 ACC/AHA framework, an asymptomatic man has an infrarenal AAA measuring 5.7 cm and acceptable procedural suitability. What is appropriate?',
 'Evaluate for aneurysm repair',[
 ('Continue ultrasound indefinitely because repair is never considered before rupture','Elective repair aims to prevent rupture when size and risk justify it.'),
 ('Apply the same size threshold as every inherited thoracic aneurysm','Aortic segment, sex and etiology have different thresholds.'),
 ('Use aspirin as a method to shrink the aneurysm immediately','Risk reduction does not replace repair assessment of an aneurysm meeting criteria.')],
 'AAA repair balances rupture risk against procedural risk',
 '**The conventional ACC/AHA repair threshold is at least 5.5 cm in men and 5.0 cm in women.**',
 ['Symptoms attributable to the aneurysm and rapid growth can alter timing.', 'EVAR versus open surgery depends on anatomy, risk and lifetime surveillance considerations.'],
 '**Continue cardiovascular prevention and follow-up.**',
 ['Smoking cessation and pressure management remain important.', 'Endovascular repair requires surveillance for endoleak and other device-related issues.'],
 [['Asymptomatic men','Repair assessment at least 5.5 cm'],['Asymptomatic women','Repair assessment at least 5.0 cm'],['Symptoms/rapid growth','Can justify earlier evaluation']], [AO], 'clinical_scenario')

if __name__=='__main__':
    finalize('Cardiology',8,'Pericardial Disease, Pulmonary Hypertension and Aortic Disease','cardiology-pericardial-pulmonary-aortic',rows,40)
