"""Original sequential valvular disease bank with reviewed decision coverage."""
import json
from qbank_json_chapters import question as Q, save, ROOT

DOC='Chapter_03_Valvular_Heart_Diseases'
R={'VHD2025':('ESC/EACTS valvular heart disease guideline, 2025','https://doi.org/10.1093/eurheartj/ehaf194')}
rows=[]
def S(h,main,*children): return h,[(main,list(children))]
def add(*args,**kwargs): rows.append(Q(*args,**kwargs))

add('Aortic stenosis','Concordant High-Gradient Aortic Stenosis',
 'A patient with exertional dyspnea has a heavily restricted calcific aortic valve. Carefully acquired echocardiography shows Vmax 4.4 m/s, mean gradient 46 mmHg and valve area 0.8 cm². LVEF is 58% and stroke-volume index 39 mL/m². Which classification best fits?',
 'Severe high-gradient aortic stenosis',[
 ('Moderate aortic stenosis with preserved ventricular function','Preserved EF does not downgrade concordant severe valve obstruction; moderate disease does not account for all three severe hemodynamic measurements supplied here.'),
 ('Paradoxical low-flow low-gradient severe aortic stenosis','This phenotype has preserved EF but reduced indexed stroke volume and a mean gradient below 40 mmHg; neither the flow nor gradient in this case meets that pattern.'),
 ('Classical low-flow low-gradient severe aortic stenosis','Classical low-flow low-gradient disease has reduced EF with low flow and a gradient below 40 mmHg; this patient instead has preserved EF and concordantly high velocity and gradient.')],
 [S('Hemodynamic Severity','**The measurements are concordant for severe high-gradient obstruction.** Velocity, mean gradient and valve area should be interpreted together rather than choosing one reassuring ventricular measurement.',
    'The 2025 ESC/EACTS framework uses Vmax at least 4.0 m/s, mean gradient at least 40 mmHg and valve area at most 1.0 cm² for this concordant severe pattern.',
    'Preserved EF describes ventricular systolic performance; it does not imply that the valve lesion is moderate or that symptoms can be ignored.'),
  S('Clinical Assessment and Intervention','**Establish whether symptoms are attributable to the valve and assess intervention suitability.** Exertional dyspnea can also arise from lung disease, anemia, coronary disease or other cardiac abnormalities.',
    'Confirm Doppler alignment, LVOT measurements, blood pressure and rhythm when findings conflict. This case is intentionally concordant and does not require a low-flow confirmation pathway.',
    'A symptomatic severe lesion warrants prompt valve-team evaluation. The choice of surgical or transcatheter replacement depends on anatomy, age, life expectancy, procedural risk and lifetime valve planning. Preserved EF is not a reason to defer assessment until irreversible ventricular damage appears.')],['VHD2025'])

add('Aortic stenosis','Classical Low-Flow Low-Gradient Aortic Stenosis',
 'A patient with heart failure has a restricted calcific aortic valve, valve area 0.75 cm², mean gradient 28 mmHg, stroke-volume index 27 mL/m² and LVEF 32%. Measurements remain discordant after technical review. Which additional test most directly assesses whether the small valve area represents true severe rather than pseudo-severe obstruction?',
 'Low-dose dobutamine stress echocardiography',[
 ('Exercise treadmill ECG without valve imaging','Exercise testing can clarify symptoms in selected apparently asymptomatic valve patients, but it does not provide the flow-dependent valve measurements needed to resolve this reduced-EF discordance.'),
 ('Repeat resting valve-area calculation after diuresis as the definitive severity test','Optimization and repeat measurements can improve interpretation, but persistent discordance requires integrated testing; a small resting calculated area alone cannot reliably distinguish true from pseudo-severe obstruction.'),
 ('Transesophageal leaflet planimetry as the sole determinant of severity','TEE can clarify valve morphology and selected anatomical measurements, but calcific shadowing and anatomical-versus-effective area differences limit a sole-planimetry decision; dynamic assessment directly addresses the low-flow question.')],
 [S('Low-Flow Physiology','**Reduced forward flow can produce a deceptively low gradient across a severely obstructed valve.** Conversely, a poorly contracting ventricle may fail to open a moderately diseased valve fully, producing an apparently small area.',
    'The reduced EF and low indexed stroke volume identify the classical low-flow phenotype. This is different from preserved-EF paradoxical low-flow disease.',
    'Review LVOT size and velocity sampling, multiple Doppler windows, pressure and rhythm before attributing disagreement to complex valve physiology.'),
  S('Dynamic Confirmation','**Low-dose dobutamine increases flow while valve area and gradient are remeasured.** A persistently restricted area with a rising severe gradient supports fixed severe obstruction; appreciable opening with flow favors pseudo-severe disease.',
    'Inadequate flow augmentation can leave the test indeterminate. Projected valve area and CT valve calcium assessment can supply complementary information; lack of flow reserve is not synonymous with absence of severe stenosis.',
    'Integrate the test with symptoms, valve morphology, myocardial disease and procedural suitability. True severe obstruction may warrant valve replacement, whereas pseudo-severe findings redirect attention toward ventricular therapy and surveillance. Do not select intervention from the resting valve area alone or deny assessment solely because the initial gradient is below the conventional severe boundary.')],['VHD2025'])

R['ASIMAGING']=('EACVI/ASE focused aortic stenosis echocardiography update, 2017','https://www.asecho.org/wp-content/uploads/2017/04/2017ValveStenosisGuideline.pdf')

add('Aortic stenosis','True Severe Obstruction During Flow Augmentation',
 'A patient with LVEF 30% has resting valve area 0.72 cm² and mean aortic gradient 25 mmHg. During technically satisfactory low-dose dobutamine testing, stroke volume increases by 28%, mean gradient reaches 44 mmHg and valve area remains 0.76 cm². Which interpretation is best?',
 'True severe aortic stenosis with demonstrable flow reserve',[
 ('Pseudo-severe aortic stenosis with demonstrable flow reserve','Pseudo-severe disease shows greater valve opening with restored flow; the persistently small area and newly severe gradient support fixed severe obstruction instead.'),
 ('True severe aortic stenosis without demonstrable flow reserve','The valve behavior supports severe stenosis, but the 28% stroke-volume increase exceeds the conventional 20% flow-reserve boundary.'),
 ('Indeterminate stenosis because a stress gradient cannot establish severity','Some dobutamine studies remain indeterminate, but adequate flow augmentation with this concordant small area and high gradient supplies a coherent true-severe pattern.')],
 [S('Valve Response to Increased Flow','**A fixed severely narrowed valve remains restricted as forward flow increases.** The rising gradient in this case unmasks obstruction that was underestimated by the resting gradient.',
    'Pseudo-severe obstruction behaves differently: improved ventricular output allows greater leaflet opening and the calculated area increases beyond the severe range.',
    'Review the area and gradient at each stage. A gradient increase alone, without the accompanying area and flow response, is less informative.'),
  S('Flow Reserve and Treatment Assessment','**Flow reserve describes an increase in stroke volume, not merely a faster pulse or higher EF.** Here the 28% rise satisfies the conventional ≥20% definition.',
    'A low-dose valve protocol differs from an ischemia-provocation stress study. EACVI/ASE guidance describes starting at 2.5–5 micrograms/kg/min and increasing every 3–5 minutes, generally up to 10–20 micrograms/kg/min, with appropriate monitoring and stopping criteria.',
    'A symptomatic patient with confirmed severe obstruction needs valve-team assessment rather than medical treatment alone for the gradient. Conversely, lack of flow reserve in another patient would not automatically prove pseudo-severe disease or eliminate potential intervention benefit. Integrate myocardial disease, anatomy and procedural suitability with the valve assessment.')],['VHD2025','ASIMAGING'])

add('Aortic stenosis','Inconclusive Dobutamine Testing Without Flow Reserve',
 'A symptomatic patient with LVEF 28%, valve area 0.8 cm² and mean gradient 24 mmHg undergoes low-dose dobutamine testing. Stroke volume increases by only 6%; gradient reaches 27 mmHg and valve area is 0.82 cm². Which next approach is most appropriate?',
 'Use integrated assessment with CT aortic-valve calcium scoring to clarify severity',[
 ('Classify pseudo-severe disease from the failure to reach a 40-mmHg gradient','Without adequate flow augmentation, a persistently low gradient does not demonstrate that the valve would open normally at higher flow; the test has not established pseudo-severe disease.'),
 ('Classify true severe disease from the unchanged valve area alone','An unchanged small area during minimal flow change remains ambiguous; the ventricle has not generated a sufficient dynamic challenge to distinguish fixed from flow-dependent restriction.'),
 ('Calculate projected valve area and use it as the definitive result despite minimal flow change','Projected area can help with an adequate measurable flow response, but extrapolation from a tiny change is unstable and should not be treated as definitive in this study.')],
 [S('Recognize an Indeterminate Dynamic Test','**The absence of flow reserve is a limitation of the test, not a diagnosis of valve severity.** A 6% stroke-volume change does not meaningfully normalize the low-flow state.',
    'Recheck acquisition quality and potential causes of limited response. Persistent myocardial dysfunction can coexist with either severe or less-than-severe valve disease.',
    'Do not convert failure to reach a numerical gradient into proof that valve replacement cannot help.'),
  S('Complementary Imaging and Projected Area','**CT valve calcium assessment provides information that is less dependent on the instantaneous forward flow.** Interpret sex-specific values with valve morphology and the clinical presentation.',
    'Projected valve area estimates opening at a standardized transvalvular flow rate of 250 mL/s. It uses the relationship between area and flow during testing; it is not simply the resting area relabeled.',
    'The 2025 ESC algorithm identifies projected area as useful with intermediate stroke-volume augmentation of 10–20%. Very limited augmentation makes extrapolation less dependable, favoring complementary imaging rather than forced classification. Calcium scoring also has limitations, particularly predominantly fibrotic disease and some bicuspid valves. The final decision combines symptoms, ventricular function, technical review and convergent valve evidence; no-flow-reserve status alone should not become a permanent refusal of intervention assessment.')],['VHD2025','ASIMAGING'])

add('Aortic stenosis','Paradoxical Low Flow Despite Preserved Ejection Fraction',
 'A hypertensive older patient with exertional dyspnea has a small concentrically remodeled LV, LVEF 62%, aortic valve area 0.8 cm², mean gradient 29 mmHg and stroke-volume index 28 mL/m². Which interpretation best guides further assessment?',
 'A preserved-EF low-flow low-gradient phenotype requiring integrated severity confirmation',[
 ('Normal-flow low-gradient stenosis because EF exceeds fifty percent','EF is the fraction of end-diastolic volume ejected, not indexed forward stroke volume; the measured 28 mL/m² establishes low flow despite preserved EF.'),
 ('Classical low-flow low-gradient stenosis from reduced systolic EF','Classical low-flow low-gradient disease has reduced EF; this case instead demonstrates the preserved-EF phenotype and requires assessment of its distinct contributors.'),
 ('Concordant severe stenosis established by the calculated area','An area below 1 cm² raises concern, but the low gradient is discordant; measurement review, blood-pressure assessment and complementary evidence are needed before assigning confirmed severity.')],
 [S('Ejection Fraction Versus Forward Flow','**A small ventricle can eject a normal fraction while delivering a low absolute stroke volume.** Concentric remodeling, impaired filling and reduced longitudinal performance can coexist with preserved EF.',
    'Other contributors include atrial fibrillation, associated mitral disease or RV dysfunction. The low-flow label should describe measured forward output rather than be inferred from EF alone.',
    'In the ESC 2025 framework, preserved-EF low-flow low-gradient AS has EF ≥50%, indexed stroke volume ≤35 mL/m², mean gradient <40 mmHg and area ≤1 cm².'),
  S('Confirm the Lesion Before Selecting Intervention','**Review technical validity and control important loading abnormalities.** Check LVOT measurement, Doppler windows, rhythm and blood pressure; hypertension can complicate interpretation.',
    'CT valve calcium scoring can provide complementary evidence when severity remains uncertain. Assess symptoms and alternative explanations such as HFpEF or pulmonary disease.',
    'This phenotype is not proof that the valve is harmless, nor sufficient evidence for intervention from one calculated area. Integrate valve morphology, ventricular findings and convergent measurements. A symptomatic patient with confirmed severe obstruction should receive valve-team assessment; a less-than-severe lesion requires management of the actual cause of symptoms and appropriate surveillance.')],['VHD2025','ASIMAGING'])

add('Aortic stenosis','Sex-Specific CT Calcium Assessment in Discordant Stenosis',
 'A woman has persistent discordant low-gradient aortic stenosis after expert echocardiographic review. Noncontrast CT gives an aortic-valve calcium score of 1850 Agatston units. Which interpretation is best supported by ESC 2025 guidance?',
 'The calcium burden strongly supports severe stenosis using female thresholds',[
 ('Severe stenosis is unlikely because the score is below two thousand','The commonly cited 2000-unit threshold applies to men; applying it to this woman ignores lower female thresholds and underestimates the significance of her valve calcium burden.'),
 ('The score is indeterminate because a threshold above three thousand applies to both sexes','A value above 3000 is a highly specific male threshold, not a sex-neutral requirement; the corresponding female highly specific threshold is lower.'),
 ('The score establishes high-gradient stenosis regardless of Doppler measurements','Calcium scoring supports anatomical severity but does not measure the transvalvular gradient; low flow can coexist with extensive calcification and a low measured gradient.')],
 [S('Use a Valve-Specific Calcium Score','**Noncontrast CT quantifies calcification of the aortic valve.** This is different from coronary calcium scoring and from contrast CT planning of an intervention.',
    'Apply sex-specific thresholds. The same numerical calcium burden does not carry identical severity implications in men and women.',
    'This woman’s score exceeds the highly specific female boundary, adding strong evidence to the integrated assessment without changing the measured hemodynamic phenotype.'),
  S('Limits of Anatomical Confirmation','**Calcium supports severity but does not establish symptom attribution or the preferred procedure.** Assess the complete valve and ventricular findings and consider competing causes of dyspnea.',
    'Predominantly fibrotic stenosis, some bicuspid valves and certain associated disorders can produce important obstruction without the expected calcium burden. A low score should therefore be interpreted with morphology rather than as an infallible exclusion.',
    'Review acquisition and scoring quality. If evidence converges on severe symptomatic obstruction, proceed to valve-team assessment; if it remains inconsistent, resolve the uncertainty before selecting replacement. A calcium score does not itself supply a coronary anatomical assessment or settle transcatheter versus surgical suitability.')],['VHD2025'],
 table=(['ESC 2025 calcium interpretation','Men: Agatston units','Women: Agatston units'],[
 ['Supports severe AS','>2000','>1200'],
 ['Highly specific for severe AS','>3000','>1600'],
 ['Severe AS unlikely','<1600','<800']]))

add('Aortic stenosis','Normal-Flow Low-Gradient Discordance',
 'A patient with a restricted aortic valve has LVEF 60%, stroke-volume index 42 mL/m², valve area 0.95 cm² and mean gradient 27 mmHg. There are no definite valve-related symptoms. Which interpretation is most appropriate?',
 'Normal-flow low-gradient discordance, often representing moderate disease, requiring integrated review',[
 ('Paradoxical low-flow severe stenosis because the area is below one square centimeter','Paradoxical low flow requires reduced indexed stroke volume, which is absent here; the area boundary cannot replace the measured flow criterion.'),
 ('Concordant severe high-gradient stenosis because the area is below one square centimeter','Concordant high-gradient severity requires a qualifying velocity/gradient pattern; the measured mean gradient is below the severe boundary and must be reconciled.'),
 ('Pseudo-severe stenosis conclusively demonstrated by the preserved EF','Pseudo-severe disease is not established by EF; it describes flow-dependent restriction demonstrated through appropriate integrated or dynamic assessment, not a normal EF alone.')],
 [S('Recognize the Discordant Phenotype','**The indexed stroke volume is normal while valve area and gradient disagree.** Do not force the case into a low-flow category merely because the area is small.',
    'The ESC 2025 guideline notes that patients with this normal-flow low-gradient pattern usually have moderate stenosis. This is a population tendency, not proof in every individual.',
    'Measurement error, body size, flow rate and the relationship between anatomical area and gradient can contribute to disagreement.'),
  S('Resolve Uncertainty and Arrange Surveillance','**Review image acquisition and the clinical context before assigning severity.** Reassess LVOT dimensions, pulsed Doppler placement and the highest reliable transvalvular velocity from multiple windows.',
    'Verify rhythm, blood pressure and whether the reported forward stroke volume is credible. CT calcium assessment or other targeted imaging can help when uncertainty is clinically consequential.',
    'An asymptomatic discordant study does not justify automatic valve replacement from area alone. Follow the confirmed severity with clinical and echocardiographic surveillance, and reassess promptly if symptoms develop. Conversely, new convincing valve-related symptoms or convergent severe anatomical evidence should trigger renewed specialist evaluation rather than dismissal based on the usual moderate-disease association.')],['VHD2025','ASIMAGING'])

add('Aortic stenosis','Symptomatic Severe Stenosis Despite Preserved EF',
 'A 74-year-old with confirmed severe high-gradient aortic stenosis develops exertional angina and near-syncope. LVEF is 61%. There is no major competing illness limiting expected survival or functional recovery. Which next management plan is best?',
 'Prompt Heart Valve Team assessment for valve replacement',[
 ('Optimize antianginal treatment and defer intervention until EF declines','Medical treatment can address comorbidity and symptoms but does not relieve fixed severe obstruction; preserved EF does not remove the intervention indication in attributable symptomatic severe disease.'),
 ('Perform an exercise test before accepting the reported symptoms as an intervention trigger','Exercise testing is useful for apparently asymptomatic patients; provoking symptoms in an already symptomatic severe lesion adds risk and is not required to validate this presentation.'),
 ('Use balloon aortic valvotomy as the planned durable treatment','Balloon valvotomy can bridge selected unstable patients or specific urgent situations, but restenosis and limited durability make it unsuitable as the usual definitive plan when valve replacement is feasible.')],
 [S('Indication for Intervention','**Symptoms attributable to confirmed severe aortic stenosis warrant valve replacement assessment even when EF is preserved.** Angina, exertional syncope or presyncope, and dyspnea are clinically important presentations.',
    'Confirm symptom attribution and severity while assessing coronary disease, arrhythmia and other possible contributors. The stem provides an established severe high-gradient lesion rather than unresolved low-gradient discordance.',
    'A normal EF does not measure all myocardial consequences of pressure overload and should not be used as a prerequisite for waiting until ventricular damage develops.'),
  S('Selecting the Definitive Approach','**The valve team selects surgery or a transcatheter procedure through individualized assessment.** Consider valve and vascular anatomy, associated coronary or aortic disease, frailty, life expectancy, procedural risk and patient preference.',
    'Temporary improvement with diuresis or other supportive treatment does not establish resolution of the obstruction. Treat decompensation while coordinating definitive care rather than substituting indefinite medical observation.',
    'Intervention should offer a reasonable prospect of survival or functional benefit; major irreversible comorbidity may change that balance. When appropriate, explain recovery, prosthesis implications, follow-up and lifetime reintervention considerations. The decision to intervene and the choice of procedure are related but distinct questions: this patient meets a clinical indication without the vignette supplying every fact needed to select TAVI or surgery.')],['VHD2025'])

add('Aortic stenosis','Exercise Assessment of Apparently Asymptomatic Severe Disease',
 'An independently mobile patient with severe high-gradient aortic stenosis and LVEF 58% reports no symptoms, but has progressively curtailed daily activity. There is no contraindication to supervised testing. Which assessment best clarifies whether the patient is truly asymptomatic?',
 'A supervised symptom-limited exercise test with ECG and blood-pressure monitoring',[
 ('A pharmacological perfusion study as the principal test of symptom status','Perfusion testing can answer a coronary ischemia question in selected patients, but does not reproduce ordinary exertion to assess valve-related exercise symptoms and hemodynamic tolerance.'),
 ('A low-dose dobutamine study to distinguish true severe from pseudo-severe stenosis','Dobutamine is valuable for selected discordant low-flow studies; this lesion is already concordant severe high-gradient disease, so the unresolved issue is actual exertional tolerance.'),
 ('Resting CT valve calcium scoring to determine whether exertional symptoms are present','Calcium assessment can corroborate anatomical severity when measurements disagree, but cannot establish the patient’s functional symptom status during activity.')],
 [S('Unmasking Symptoms','**Self-reported absence of symptoms can reflect avoidance of exertion.** A supervised exercise test can reveal dyspnea, angina, presyncope or impaired exercise tolerance that the patient does not encounter in a restricted routine.',
    'Assess symptoms, achieved workload, ECG and blood-pressure response together. The ESC 2025 discussion identifies a blood-pressure fall exceeding 20 mmHg as hemodynamic intolerance.',
    'Testing belongs in a suitable monitored environment with an experienced team and appropriate stopping criteria. It should not be transferred to a patient already known to have symptomatic severe stenosis.'),
  S('Using the Result','**Symptoms elicited during appropriate exercise assessment change the apparent asymptomatic classification.** The result informs intervention discussion rather than serving as an isolated numerical pass/fail label.',
    'If the patient remains genuinely asymptomatic, assess ventricular function, progression, biomarkers and suitability for an early-intervention strategy under current guidance. Preserved EF and a normal exercise response do not mean follow-up can cease.',
    'For surveillance, educate the patient about new symptoms and arrange clinical and echocardiographic reassessment, commonly at least every six months for severe disease under ESC guidance. An earlier review is needed for new symptoms. Physical limitations that prevent useful exercise testing require another individualized assessment; inability to test is not evidence that the patient has normal exercise tolerance.')],['VHD2025'])

R['EARLYTAVR']=('EARLY TAVR randomized trial, 2024 online/2025 print','https://doi.org/10.1056/NEJMoa2405880')

add('Aortic stenosis','Interpreting EARLY TAVR Without Overstating Mortality Benefit',
 'Which interpretation of the EARLY TAVR randomized trial is most accurate when discussing intervention with an asymptomatic older patient with severe aortic stenosis and preserved EF?',
 'Early TAVR reduced the composite of death, stroke or unplanned cardiovascular hospitalization compared with surveillance',[
 ('Early TAVR established an isolated all-cause mortality benefit as its primary finding','The primary endpoint was a composite. Death occurred in 8.4% versus 9.2%; the significant composite result cannot be relabeled as a demonstrated isolated mortality benefit.'),
 ('The comparison established TAVR superiority over surgical valve replacement','The randomized comparator was clinical surveillance, not surgery; the trial does not directly determine which replacement approach is superior.'),
 ('The comparison established benefit of TAVR in moderate aortic stenosis with reduced EF','This is a different disease-severity and ventricular-function question; EARLY TAVR studied asymptomatic severe disease rather than that moderate-AS population.')],
 [S('Population, Comparator and Endpoint','**EARLY TAVR randomized 901 patients with asymptomatic severe aortic stenosis to early TAVR or clinical surveillance.** It addressed timing of intervention, not a direct comparison with surgery.',
    'The primary composite occurred in 26.8% versus 45.3%, hazard ratio 0.50 with 95% confidence interval 0.40–0.63. Interpretation must retain the endpoint components.',
    'Unplanned cardiovascular hospitalization occurred in 20.9% versus 41.7%; stroke in 4.2% versus 6.7%; death in 8.4% versus 9.2%. These component figures should not be presented as if each independently established the same statistical conclusion.'),
  S('Clinical Application','**An early-intervention discussion should consider trial eligibility and lifetime treatment consequences.** Asymptomatic status, stenosis severity, ventricular function, anatomy and procedural suitability matter.',
    'Clinical surveillance is active care with symptom education, repeat assessment and later intervention when indicated. It is not permanent refusal of replacement.',
    'The findings support reconsidering timing in appropriate severe disease, while leaving procedure selection to individualized Heart Team assessment. They do not establish benefit in every younger patient, every anatomy or every less-than-severe lesion. Explain potential procedural harms and later prosthesis-related decisions alongside the composite benefit. A qualified discussion is more useful than converting a trial result into a universal instruction to implant immediately.')],['EARLYTAVR','VHD2025'],style='direct')

add('Aortic stenosis','Choosing Surgical Replacement in a Younger Low-Risk Patient',
 'A 62-year-old with symptomatic severe calcific aortic stenosis has low surgical risk and a long expected lifespan. Both surgery and transfemoral TAVI appear technically feasible. Under the 2025 ESC/EACTS framework, which planning approach is preferred?',
 'Favor surgical replacement while discussing prosthesis choice and lifetime valve management',[
 ('Favor TAVI because technical transfemoral feasibility settles the modality decision','Feasible access is necessary for transfemoral TAVI but does not settle age, durability, coronary access and lifetime reintervention concerns in a younger low-risk patient.'),
 ('Favor TAVI because a low operative-risk score identifies the strongest transcatheter indication','Low-risk TAVI trials inform shared decisions, but a low operative-risk score alone does not override the named ESC preference for SAVR below seventy years when surgical risk is low.'),
 ('Defer the modality discussion until the patient reaches seventy years','Age informs procedure selection rather than postponing treatment of symptomatic severe disease; delay leaves an established valve indication untreated without a compensating clinical reason.')],
 [S('Age, Risk and Lifetime Planning','**ESC 2025 favors SAVR for patients younger than seventy years when surgical risk is low.** The threshold belongs to the stated framework and is not an isolated universal age law.',
    'A long expected lifespan raises questions about prosthesis durability, future valve-in-valve feasibility, coronary access and the consequences of later explantation.',
    'Surgical replacement also permits individualized mechanical-versus-biological prosthesis selection; the patient must understand the implications of lifelong anticoagulation if a mechanical valve is chosen.'),
  S('Shared Decision With the Heart Team','**Technical eligibility for both procedures does not make them interchangeable in every patient.** Review valve anatomy, coronary and aortic disease, frailty, access, anticipated recovery and preferences.',
    'A different balance may favor TAVI in an older patient or one with increased operative risk. Associated disease requiring surgery can favor a combined surgical approach.',
    'Discuss the tradeoffs without promising identical lifetime outcomes from short- or intermediate-term comparisons. A procedural-risk score is one input and does not capture every anatomical or long-term issue. Document why the selected strategy suits this patient and what later interventions may be possible. The symptomatic indication establishes the need for replacement assessment; it does not remove the need to select the appropriate procedure and prosthesis.')],['VHD2025'])

add('Aortic stenosis','Balloon Valvotomy as a Selected Bridge',
 'A patient has cardiogenic shock from confirmed severe calcific aortic stenosis. The valve team concludes that definitive replacement cannot be performed immediately, but remains feasible after stabilization. There is no important aortic regurgitation. How should balloon aortic valvotomy be considered?',
 'As a selected temporary bridge to definitive valve replacement',[
 ('As definitive treatment if the immediate gradient and blood pressure improve','Immediate improvement can be valuable, but recoil and restenosis limit durability in calcific adult disease; a successful bridge does not remove the planned definitive valve assessment.'),
 ('As a mandatory preliminary procedure before subsequent TAVI','Balloon treatment can help selected unstable patients, but it is not a required separate preliminary admission for every TAVI candidate; direct definitive treatment may be preferable when feasible.'),
 ('As a reason to defer replacement planning until severe symptoms recur','Recurrent symptoms can indicate loss of the temporary benefit; delaying planning until deterioration forfeits the purpose of stabilizing the patient for definitive intervention.')],
 [S('Bridging Indication','**Balloon valvotomy may provide temporary relief of obstruction in selected unstable patients.** ESC 2025 permits consideration as a bridge to SAVR or TAVI, including selected urgent high-risk noncardiac surgical situations.',
    'Selection requires a valve team because urgent definitive replacement may be possible and preferable in some centers. The stem specifies that it cannot currently be performed.',
    'An explicit destination and reassessment plan distinguish bridging care from an unintended permanent postponement.'),
  S('Benefits, Limits and Procedural Risk','**Improved forward flow can create an opportunity for stabilization, but the calcific lesion remains.** Assess blood pressure, perfusion, congestion and renal function after treatment.',
    'Potential complications include vascular injury, bleeding, stroke, tamponade and important new aortic regurgitation. Existing significant regurgitation can make balloon treatment especially problematic.',
    'Continue multidisciplinary shock care and reassess suitability for replacement as the patient recovers. If severe irreversible comorbidity makes meaningful recovery unlikely, clarify goals and whether an intervention offers useful benefit. Balloon treatment is not disease-modifying medical therapy and should not be represented as equivalent in durability to a prosthetic replacement. Its value in this question is a carefully selected temporary step with a defined subsequent plan.')],['VHD2025'])

R['REGURG']=('ASE recommendations for noninvasive evaluation of native valvular regurgitation, 2017','https://www.asecho.org/wp-content/uploads/2025/04/2017VavularRegurgitationGuideline.pdf')
R['ACCVALVE']=('ACC/AHA valvular heart disease guideline, 2020','https://doi.org/10.1161/CIR.0000000000000923')

add('Aortic regurgitation','Integrated Assessment of Chronic Aortic Regurgitation',
 'A patient with chronic native aortic regurgitation has vena contracta 0.75 cm, regurgitant volume 72 mL/beat, regurgitant fraction 56% and effective regurgitant orifice area 0.36 cm². Holodiastolic descending aortic flow reversal and LV enlargement are present. Which conclusion is best supported?',
 'Concordant multiparametric evidence of severe chronic aortic regurgitation',[
 ('Moderate regurgitation because the LV remains compensated','Ventricular compensation describes the response to loading, not a reason to downgrade multiple concordant severe regurgitant measurements; LV size and EF additionally guide timing of intervention.'),
 ('Indeterminate severity until pressure half-time is measured','Pressure half-time is a supportive, load-dependent parameter rather than a compulsory gatekeeper; the supplied independent quantitative and flow findings already converge.'),
 ('Severe regurgitation established solely by the visible color jet length','Color jet appearance depends on settings, driving pressure and eccentricity; severity is supported here by the integrated measurements, not by an isolated visual length criterion.')],
 [S('Concordant Quantitative Evidence','**Chronic regurgitant severity should be graded using multiple complementary findings.** The measurements in this stem all lie in the severe range.',
    'Confirm the valve mechanism, jet direction, acquisition quality and the consistency of volumetric calculations. Eccentric or multiple jets can limit individual methods.',
    'Assess LV volumes and function and measure the aortic root and ascending aorta. The ventricular response and associated aortic disease influence management in addition to leak severity.'),
  S('Limitations and Further Assessment','**Pressure half-time depends on ventricular compliance and aortic–ventricular pressure equalization.** A short value can support severe disease but should not override the full study.',
    'When echo measurements conflict or windows are poor, CMR can quantify regurgitant flow and ventricular volumes. TEE can clarify leaflet abnormalities or unresolved mechanisms.',
    'The immediate next management decision depends on symptoms, EF, indexed ventricular dimensions and aortic anatomy. Severe regurgitation is not synonymous with immediate surgery in every asymptomatic patient, but it requires structured specialist follow-up and timely intervention assessment. Acute severe regurgitation is a different physiological setting and may lack the LV enlargement expected with chronic volume loading.')],['REGURG','ACCVALVE','VHD2025'],
 table=(['Severe chronic native AR marker','Common guideline boundary'],[
 ['Vena contracta','>0.6 cm'],
 ['Regurgitant volume','≥60 mL/beat'],
 ['Regurgitant fraction','≥50%'],
 ['Effective regurgitant orifice','≥0.30 cm²'],
 ['Descending aortic Doppler','Holodiastolic flow reversal supports severity']]))

add('Aortic regurgitation','Acute Severe Regurgitation Without Ventricular Dilatation',
 'A patient with aortic-valve endocarditis abruptly develops pulmonary edema and hypotension. Echocardiography shows leaflet perforation, severe aortic regurgitation, premature mitral closure and a nondilated LV. Which management approach is most appropriate?',
 'Urgent surgical evaluation with concurrent stabilization and antimicrobial treatment',[
 ('Treat the infection and defer surgery until chronic LV dilatation develops','Acutely elevated filling pressure can cause collapse before the LV has time to dilate; waiting for chronic remodeling ignores the urgent hemodynamic indication.'),
 ('Use intra-aortic balloon counterpulsation as the preferred bridge','Balloon inflation increases diastolic aortic pressure and can worsen important aortic regurgitation; it is not the appropriate default support strategy for this lesion.'),
 ('Initiate beta blockade as the principal treatment for the compensatory tachycardia','Slowing the heart can lengthen diastolic regurgitant time and impair compensation in acute severe AR; the priority is urgent valve care and perfusion support, not reflex rate suppression.')],
 [S('Acute Volume Loading','**An unadapted LV cannot accommodate a sudden large regurgitant volume without a marked pressure rise.** Pulmonary edema and low forward output can therefore occur with normal chamber dimensions.',
    'Early aortic–ventricular pressure equalization may shorten the murmur and produce premature mitral closure. Absence of a wide pulse pressure or long diastolic murmur does not exclude a severe acute lesion.',
    'Endocarditis-related destruction and acute aortic root disease are important causes. Define the mechanism promptly with TTE and TEE when needed.'),
  S('Stabilization and Definitive Treatment','**Acute severe AR with hemodynamic compromise requires urgent surgical coordination.** Start appropriate infection treatment and obtain cultures without delaying resuscitation or necessary intervention.',
    'Provide respiratory and circulatory support. Vasodilator afterload reduction can be useful if pressure permits; shock requires individualized vasoactive support. These are bridges, not repairs of a perforated leaflet.',
    'Do not apply chronic asymptomatic LV-dimension thresholds to this emergency. Mechanical-support selection must account for the regurgitant lesion: increased aortic diastolic pressure or LV afterload can worsen physiology. Reassess perfusion and congestion continuously while the valve and endocarditis teams plan definitive care. A temporary clinical improvement does not remove the structural indication or justify waiting for completion of an antibiotic course.')],['VHD2025','ACCVALVE'])

add('Aortic regurgitation','Ventricular Dysfunction as a Surgical Trigger in Chronic AR',
 'An asymptomatic patient has confirmed severe chronic aortic regurgitation. LVEF has fallen to 48% without another cause; LV end-systolic diameter is 47 mm. Surgical risk is acceptable. Under ESC 2025 guidance, what is the appropriate plan?',
 'Refer for aortic valve surgery based on LV systolic dysfunction',[
 ('Continue surveillance until end-systolic diameter exceeds fifty millimeters','The dimension and EF triggers are alternatives; crossing the EF threshold already supports surgery even though the absolute diameter is below fifty millimeters.'),
 ('Continue surveillance until exertional symptoms are documented','Symptoms are an important intervention trigger, but their absence does not negate established LV dysfunction from severe chronic regurgitation.'),
 ('Use vasodilator therapy and reassess after EF falls below thirty-five percent','Treat hypertension and other indications, but the HFrEF threshold of thirty-five percent is not the surgical threshold for severe AR; waiting risks less reversible ventricular injury.')],
 [S('Independent Intervention Triggers','**Severe AR can warrant surgery before symptoms appear when ventricular function or size crosses the applicable boundary.** EF 48% satisfies the ESC established systolic-dysfunction trigger.',
    'Confirm severity, measurement quality and the absence of another dominant explanation for reduced EF. Serial change helps interpret borderline values but should not be used to disregard clear dysfunction.',
    'Assess aortic root and ascending aortic dimensions because associated aortopathy can independently influence the operation.'),
  S('Attribute Thresholds to Their Guideline','**ESC and ACC/AHA frameworks use different EF boundaries and recommendation categories.** Do not merge them into a single undated cutoff.',
    'ESC 2025 identifies EF ≤50%, LVESD >50 mm or indexed LVESD >25 mm/m² as established asymptomatic severe-AR surgical triggers. Selected low-risk patients may be considered earlier using additional evidence of ventricular change.',
    'The ACC/AHA 2020 framework uses EF ≤55% when no other cause explains dysfunction. A lower-risk earlier-surgery discussion is not the same recommendation as an established trigger. Explain the rationale for intervening before advanced remodeling, document the measurement framework and coordinate a valve-center review rather than waiting for a heart-failure drug threshold.')],['VHD2025','ACCVALVE'],
 table=(['Framework for asymptomatic severe AR','LV criterion','Interpretation'],[
 ['ESC 2025 established triggers','EF ≤50%; or LVESD >50 mm; or LVESDi >25 mm/m²','Surgery recommended when appropriate'],
 ['ESC 2025 selected low-risk earlier discussion','EF ≤55%; or LVESDi >22 mm/m²; or LVESVi >45 mL/m²','Earlier intervention considered in context; distinct from established triggers'],
 ['ACC/AHA 2020 EF trigger','EF ≤55% without another cause','Guideline-specific systolic-dysfunction indication']]))

add('Aortic regurgitation','Indexed Ventricular Size in a Small Adult',
 'An asymptomatic small adult has severe chronic aortic regurgitation, LVEF 60%, LV end-systolic diameter 44 mm and body surface area 1.5 m². Measurements are reproducible and surgical risk is acceptable. Under ESC 2025 guidance, which interpretation is appropriate?',
 'The indexed end-systolic diameter exceeds the established surgical trigger',[
 ('The ventricular size trigger is absent because absolute diameter is below fifty millimeters','The absolute boundary is not the only criterion: indexing identifies important enlargement in small adults, whose ventricular dimensions can be clinically abnormal below fifty millimeters.'),
 ('The indexed diameter remains below the established trigger because EF is normal','Indexed diameter and EF are independent measurements; preserved EF neither changes the calculation nor cancels the size-based intervention criterion.'),
 ('Only an earlier discretionary intervention discussion is supported by these dimensions','The calculated 29.3 mm/m² exceeds the established 25-mm/m² boundary, not merely the lower threshold used for selected low-risk earlier discussions.')],
 [S('Index the Measurement Correctly','**LVESDi equals LV end-systolic diameter divided by body surface area.** Here, 44 mm ÷ 1.5 m² = ==29.3 mm/m²==.',
    'The ESC 2025 established severe-AR trigger is LVESDi >25 mm/m². This patient crosses it despite LVESD below fifty millimeters and preserved EF.',
    'Report the units and measurement method. Do not divide by height, confuse end-systolic with end-diastolic diameter, or substitute an indexed volume boundary.'),
  S('Interpret Size With Clinical Evidence','**Body size matters when interpreting chronic volume-overload remodeling.** A single unindexed cutoff can delay recognition in a small adult.',
    'Confirm severe regurgitation and reproducible ventricular measurement, evaluate exercise symptoms where appropriate, and review serial function and dimensions. CMR can clarify ventricular volumes or regurgitant severity when echo is uncertain.',
    'Refer for valve-center surgical assessment with the full anatomical and clinical record. Indexing is not a replacement for assessing symptoms, EF, aortic disease and operative suitability. Likewise, an apparently reassuring symptom history does not negate an established ventricular criterion. Explain that the intention is to intervene before advanced, potentially less reversible myocardial dysfunction, rather than wait for an absolute diameter derived without regard to body size.')],['VHD2025'])

add('Aortic regurgitation','Addressing Aortic Disease During Valve Surgery',
 'A low-risk patient is scheduled for surgery for symptomatic severe aortic regurgitation. Cross-sectional imaging confirms a maximal ascending aortic diameter of 48 mm. Under ESC 2025 guidance, what should the surgical plan include?',
 'Assessment for concomitant replacement of the enlarged ascending aorta',[
 ('Isolated valve surgery with aortic intervention deferred until fifty-five millimeters','An isolated aortopathy threshold should not be copied into a patient already undergoing valve surgery; concomitant replacement can be considered at a lower diameter with low predicted surgical risk.'),
 ('Isolated valve surgery with aortic replacement considered only if subsequent rapid growth occurs','Rapid growth is an important aortopathy risk feature, but the opportunity for concomitant replacement at the specified size should be assessed during the already indicated operation rather than reserved solely for documented future growth.'),
 ('Plan a root replacement instead of evaluating the tubular ascending segment','Root replacement is relevant to root pathology; a tubular ascending measurement does not establish root enlargement. The operation should address the demonstrated segment and valve mechanism.')],
 [S('Concomitant Aortic Assessment','**Valve disease and aortic disease require a combined anatomical plan.** The root and tubular ascending segment are different structures and should be measured and described separately.',
    'ESC 2025 advises considering concomitant root or ascending replacement at maximal diameter ≥45 mm when a valve operation is indicated and predicted surgical risk is low.',
    'This is not a universal isolated-aorta threshold. Etiology, genetic disease, growth, body size, family history and operative circumstances influence aortic decisions.'),
  S('Repair, Replacement and Valve Preservation','**Choose the operation according to the mechanism and the involved aortic segment.** Root enlargement with suitable pliable cusps may allow valve-sparing root replacement at an experienced center.',
    'Calcification, cusp destruction or an unlikely durable repair may favor valve replacement. A tubular ascending graft and an operation on the root are not interchangeable labels.',
    'Review CT or CMR alongside echocardiographic valve assessment and discuss durability, prosthesis implications and reintervention. A successful isolated correction of regurgitation does not remove untreated aortic risk. Conversely, a forty-eight-millimeter ascending measurement does not by itself prove that every part of the root must be replaced. The clinical value of the threshold is to prompt an integrated surgical decision rather than two disconnected treatment plans.')],['VHD2025'])

add('Aortic regurgitation','Treating Hypertension Without Replacing Valve Surveillance',
 'An asymptomatic patient with chronic moderate aortic regurgitation has repeated blood pressures around 164/86 mmHg, normal renal function and preserved LV systolic function. There is no current intervention indication. Which treatment principle is appropriate?',
 'Treat hypertension with an appropriate agent such as an ACE inhibitor or dihydropyridine calcium antagonist and continue valve surveillance',[
 ('Treat the blood pressure and reduce echocardiographic surveillance if readings normalize','Pressure control treats an added hemodynamic load but does not establish that the valve lesion has regressed; surveillance remains necessary even after hypertension improves.'),
 ('Use vasodilator therapy principally to postpone valve surgery even if later ventricular criteria appear','A vasodilator is justified for hypertension, but is not a proven substitute for surgery once severe-AR intervention criteria develop; indication and follow-up must remain explicit.'),
 ('Choose rate-slowing therapy primarily to reduce the duration of diastolic regurgitation','Rate slowing lengthens rather than shortens diastole. Beta blockers can treat separate indications, but this proposed AR-specific mechanism does not justify prioritizing them here.')],
 [S('Treat the Coexisting Hemodynamic Load','**Hypertension adds to the LV load imposed by regurgitation.** An ACE inhibitor, ARB or dihydropyridine calcium antagonist can be selected according to the patient’s clinical context.',
    'Titrate to blood-pressure response and tolerability. Assess renal function and potassium with renin–angiotensin inhibition and monitor edema or hypotension with vasodilating calcium antagonists.',
    'For example, amlodipine commonly begins at 5 mg once daily and can be increased to 10 mg daily; frailty or hepatic disease can require more cautious initiation.'),
  S('Keep Medical and Procedural Indications Distinct','**Blood-pressure control does not repair a structurally incompetent valve.** Continue assessment of symptoms, LV size and function and associated aortic disease.',
    'Do not prescribe prophylactic vasodilation to a normotensive patient as a proven method of postponing surgery. If established intervention criteria later appear, symptomatic improvement on medicines should not obscure them.',
    'Beta blockers are not a blanket lifelong prohibition in chronic AR: arrhythmia, ventricular dysfunction or associated aortic disease may create another indication. Their use should follow that actual clinical problem rather than an incorrect claim about shortening regurgitant exposure. Explain why treatment is being prescribed and arrange follow-up so improved pressure is not mistaken for resolution of the valve lesion.')],['VHD2025','ACCVALVE','AMLODIPINE'])

add('Aortic regurgitation','Combined Burden of Mixed Aortic Valve Disease',
 'A patient has moderate native aortic stenosis by valve-area assessment and moderate aortic regurgitation. Exertional dyspnea is attributable to the valve lesion after evaluation. Vmax is 4.2 m/s and mean gradient 43 mmHg, with reliable measurements and no alternative high-output cause. Under ESC 2025 guidance, what is appropriate?',
 'Refer for valve intervention assessment based on symptomatic mixed disease with a high-gradient burden',[
 ('Continue surveillance until either isolated valve lesion is independently graded severe','The combination can impose important pressure and volume loading even when individual lesion grades are moderate; the named guideline provides a specific intervention pathway for this mixed presentation.'),
 ('Attribute the gradient entirely to regurgitant flow and disregard it in management','AR increases systolic transvalvular flow and can raise gradients, but that is part of the combined burden; it does not make qualifying high gradients irrelevant in symptomatic mixed disease.'),
 ('Use balloon valvotomy as the preferred treatment for the mixed lesion','Balloon treatment does not correct regurgitation and can worsen it; mixed stenosis and regurgitation requires a replacement-oriented valve-team assessment rather than that default strategy.')],
 [S('Pressure and Volume Load Together','**Mixed aortic disease cannot be interpreted by considering each component in isolation.** Regurgitation increases forward systolic flow across the stenotic valve while also producing chronic volume loading.',
    'Confirm acquisition quality, valve morphology, regurgitant severity and ventricular response. Anemia or another high-output state can complicate the interpretation and should be assessed.',
    'The gradient describes the combined hemodynamic burden in this setting rather than serving as a pure anatomical measure of stenosis alone.'),
  S('Guideline-Specific Intervention Threshold','**ESC 2025 recommends intervention in symptomatic mixed moderate AS and moderate AR when mean gradient is ≥40 mmHg or Vmax ≥4.0 m/s.** This patient meets both hemodynamic boundaries.',
    'Confirm that symptoms are attributable and use Heart Team assessment to select the procedure. Valve anatomy, aortic dimensions and accompanying disease remain important.',
    'For asymptomatic mixed disease, the guideline also identifies Vmax ≥4.0 m/s with EF <50% not explained by another cardiac disorder as an intervention setting. Do not extend a recommendation based on these defined findings to every minor mixed lesion. Continue symptom education and serial ventricular assessment when intervention criteria are absent; combined loading may progress or be underestimated if follow-up focuses only on the word moderate.')],['VHD2025'])

R['STENOSIS']=('EAE/ASE echocardiographic assessment of valve stenosis, 2009','https://www.escardio.org/static-file/Escardio/Subspecialty/EACVI/education/echo-box/valvular/EAE-recommendations-valve-stenosis.pdf')

add('Mitral stenosis','Commissural Fusion Identifies the Rheumatic Mechanism',
 'A patient with mitral obstruction has doming of the anterior leaflet, restricted posterior leaflet motion, commissural fusion and subvalvular thickening. Which mechanism best explains these findings?',
 'Rheumatic mitral stenosis',[
 ('Degenerative stenosis from mitral annular calcification','Calcific degenerative obstruction typically arises from annular and basal leaflet disease without the characteristic commissural fusion; its procedural options differ from rheumatic commissural disease.'),
 ('Obstruction from a left atrial myxoma','A myxoma can intermittently obstruct inflow but is an intracavitary mass; it does not itself produce fused commissures and the described leaflet/subvalvular remodeling.'),
 ('Congenital parachute mitral valve','A parachute valve has abnormal chordal insertion toward a single papillary muscle; that congenital apparatus differs from the acquired fused-commissure pattern here.')],
 [S('Valve and Subvalvular Morphology','**Rheumatic injury can thicken leaflets, fuse commissures and shorten or fuse chordae.** The resulting funnel-like opening produces diastolic inflow obstruction.',
    'Commissural fusion is particularly important because balloon commissurotomy treats fused commissures. A small orifice caused by another mechanism does not imply the same response to balloon treatment.',
    'Assess mobility, calcification, commissural anatomy, subvalvular involvement and associated regurgitation rather than relying on one descriptive sign.'),
  S('Implications for Evaluation and Treatment','**Mechanism determines which severity measurements and interventions are appropriate.** In suitable rheumatic anatomy, planimetry and integrated hemodynamic assessment guide management.',
    'Degenerative annular calcification can create acoustic shadowing and a different orifice geometry, making straightforward planimetry less reliable. Such patients need a tailored multimodality assessment.',
    'For possible commissurotomy, assess symptoms, valve area, pulmonary pressure, regurgitation and left atrial thrombus before selecting treatment. Associated aortic or tricuspid disease and coronary surgical needs can favor a surgical approach. Finding rheumatic morphology does not by itself establish that every valve is balloon-suitable; severe calcification, significant MR or atrial thrombus can change the plan. The examination distinction is therefore both diagnostic and therapeutic.')],['VHD2025','STENOSIS'])

add('Mitral stenosis','A Low Resting Gradient Does Not Exclude Important Mitral Obstruction',
 'A patient with rheumatic mitral stenosis has a reproducible planimetered valve area of 1.2 cm². Mean transmitral gradient is 4 mmHg at a sinus rate of 48/min, with low forward flow. Which interpretation is most appropriate?',
 'Clinically significant mitral stenosis with a gradient reduced by the low-flow slow-rate state',[
 ('Mild stenosis because the mean gradient is below five millimeters of mercury','A low gradient can reflect reduced transmitral flow and prolonged diastolic filling time; it cannot independently overturn a technically valid small valve area.'),
 ('Severe measurement error established by the area–gradient disagreement','Discordance warrants technical review, but physiologic dependence on rate and flow can explain it without proving that the area measurement is wrong.'),
 ('Mild anatomical disease with an overestimated gradient from bradycardia','Bradycardia tends to prolong filling time and reduce rather than inflate the gradient at a given flow; this interpretation reverses the physiological effect and disregards the measured area.')],
 [S('Anatomical Area and Hemodynamic Consequences','**Mitral valve area and mean gradient answer related but different questions.** Planimetry estimates the orifice, while the gradient depends on flow and the time available for filling.',
    'A valve area ≤1.5 cm² defines clinically significant rheumatic MS in the intervention framework; ACC/AHA staging describes this range as severe. Older echo grading schemes may reserve the term severe for area <1.0 cm², so identify the framework.',
    'Tachycardia shortens diastole and commonly increases gradient. Bradycardia and low output can produce the opposite pattern even when the orifice remains important.'),
  S('Resolve the Clinical Discrepancy','**Record heart rate and rhythm with the reported gradient.** Check acquisition, average suitable beats when rhythm is irregular, and integrate pulmonary pressure and chamber changes.',
    'If symptoms and resting measurements disagree, supervised exercise echocardiography can assess functional capacity, gradient and pulmonary pressure responses in an appropriate patient.',
    'Intervention decisions require symptoms, morphology, thromboembolic risk, hemodynamic consequences and procedural suitability. Do not use one resting gradient as a universal clearance for exercise, pregnancy or surgery. Equally, a small measured area should be verified before treatment is chosen. The task is to reconcile anatomy with the physiological conditions under which the measurement was obtained.')],['VHD2025','ACCVALVE','STENOSIS'])

add('Mitral stenosis','Pressure Half-Time Immediately After Commissurotomy',
 'Immediately after balloon mitral commissurotomy, a pressure-half-time calculation suggests valve area 2.4 cm², but technically satisfactory planimetry gives 1.6 cm². The patient is stable. Which interpretation is most appropriate?',
 'Integrate planimetry, gradient, regurgitation and the clinical response because pressure half-time is unreliable immediately after the procedure',[
 ('Accept 2.4 cm² because Doppler-derived area is independent of chamber compliance','The empirical pressure-half-time relation depends on atrial and ventricular compliance and pressure conditions, which can change abruptly after commissurotomy.'),
 ('Diagnose early restenosis because planimetry is smaller than the pressure-half-time estimate','Disagreement between two immediate postprocedural methods does not demonstrate recurrent fusion or restenosis; it requires assessment of each method’s assumptions and technical validity.'),
 ('Repeat balloon inflation to make planimetry equal the pressure-half-time result','A numerical discrepancy alone is not an indication for further inflation; additional dilation can cause regurgitation or other injury and requires an integrated procedural assessment.')],
 [S('Principle and Assumptions','**The conventional relation is MVA in cm² = 220 ÷ pressure half-time in milliseconds.** It is empirical rather than a direct anatomical measurement.',
    'Pressure half-time reflects decay of the atrial–ventricular pressure difference. Altered chamber compliance, significant AR and other loading conditions can change that decay independently of valve area.',
    'Immediately after commissurotomy, abrupt hemodynamic changes can invalidate the usual relation. A mathematically correct calculation can therefore yield a misleading anatomical estimate.'),
  S('Assess the Procedural Result','**Combine anatomical opening with hemodynamics and complications.** Review commissural separation, planimetered area, mean gradient at the recorded heart rate, new MR and clinical status.',
    'Use appropriate 2D or 3D imaging and check the plane of the smallest orifice. Planimetry also has technical limitations and should not be accepted without image review.',
    'Do not pursue an idealized target by repeat inflation without considering leaflet injury or regurgitation. Arrange follow-up to document the sustained result once loading conditions stabilize. The useful distinction is between a method-dependent immediate discrepancy and evidence of a genuinely inadequate or complicated procedure; treatment must follow the latter assessment rather than a single derived number.')],['STENOSIS','VHD2025'])

add('Mitral stenosis','Exercise Hemodynamics When Resting Measurements Underestimate Symptoms',
 'A patient with rheumatic mitral stenosis has exertional dyspnea despite a resting valve area of 1.7 cm² and mean gradient 5 mmHg. Symptoms remain unexplained after basic evaluation. Which investigation most directly assesses the valve’s contribution during exertion?',
 'Exercise echocardiography measuring symptoms, transmitral gradient and pulmonary pressure',[
 ('Transesophageal three-dimensional planimetry at rest as the next functional test','TEE can clarify uncertain orifice anatomy or thrombus, but a resting anatomical measurement does not directly reproduce the exertional gradient and symptoms in this adequately imaged patient.'),
 ('Cardiopulmonary exercise testing without simultaneous valve hemodynamics','CPET can quantify limitation and suggest cardiac versus pulmonary contributors, but by itself does not measure the exercise transmitral gradient or pulmonary-pressure response needed to link symptoms to this lesion.'),
 ('Repeat pressure-half-time calculation at rest as the sole next assessment','Repeat acquisition can resolve technical error, but a resting calculation alone does not reproduce the exercise-related hemodynamic question when the resting study is already adequate.')],
 [S('Reproduce the Physiological Challenge','**Exercise increases transmitral flow and heart rate, potentially exposing an important gradient not apparent at rest.** Assess symptoms and workload alongside Doppler and pulmonary-pressure responses.',
    'Check baseline rhythm, rate and blood pressure and select a supervised protocol appropriate to functional capacity. Avoid attributing every exercise symptom to the valve without considering pulmonary disease, ischemia or deconditioning.',
    'If noninvasive findings remain unclear, invasive exercise hemodynamics can provide targeted clarification in a specialist setting.'),
  S('Interpret Thresholds in Their Clinical Framework','**ACC/AHA 2020 permits consideration of balloon commissurotomy in selected symptomatic rheumatic MS with area >1.5 cm² when exercise demonstrates significant obstruction.** The cited findings are mean mitral gradient >15 mmHg or pulmonary artery wedge pressure >25 mmHg.',
    'These are not interchangeable with a resting gradient threshold or a universal indication for every elevated exercise pulmonary pressure. Anatomy, MR, atrial thrombus and procedural expertise still determine suitability.',
    'The aim is to connect symptoms with demonstrable valve physiology. A positive assessment informs treatment discussion; it does not bypass morphological contraindications. Conversely, a genuinely reassuring valve response should prompt renewed investigation of alternative causes rather than an intervention based solely on the patient’s symptom report.')],['ACCVALVE','VHD2025','STENOSIS'])

add('Mitral stenosis','Selecting Balloon Commissurotomy for Favorable Rheumatic Anatomy',
 'A patient has persistent NYHA III symptoms from rheumatic mitral stenosis despite appropriate medical treatment. Valve area is 1.0 cm², with mobile leaflets, commissural fusion, limited calcification and only mild MR. TEE excludes LA thrombus. No other cardiac lesion requires surgery. Which intervention is preferred?',
 'Percutaneous balloon mitral commissurotomy at an experienced valve center',[
 ('Surgical mitral replacement as the initial procedure','Replacement is important when anatomy or associated disease makes commissurotomy unsuitable, but favorable commissural anatomy without a surgical co-indication supports the less invasive commissurotomy pathway here.'),
 ('Open surgical commissurotomy as the initial procedure','Surgical commissurotomy can preserve the valve when catheter treatment is unsuitable or another operation is needed; favorable balloon anatomy without a surgical co-indication supports percutaneous treatment first.'),
 ('Continued medical therapy without a procedural plan','Diuresis and rate control may reduce symptoms but do not remove fused commissures; persistent substantial symptoms with clinically severe suitable rheumatic MS support intervention.')],
 [S('Mechanism-Based Intervention','**Balloon commissurotomy separates fused commissures.** Its success depends on the mechanism and distribution of valve disease rather than valve area alone.',
    'Review leaflet mobility, thickening, calcification and subvalvular disease. Anatomy scores support assessment, but do not replace direct review of commissures or associated MR.',
    'A favorable total score cannot cancel a contraindication. Severe or bicommissural calcification and absent commissural fusion substantially change suitability.'),
  S('Eligibility and Safety Assessment','**Confirm important stenosis, a clinical indication and absence of major exclusions.** TEE is used to exclude LA thrombus before the procedure.',
    'More than mild MR is a contraindication in the ESC framework. Significant concomitant aortic or tricuspid disease requiring surgery, or coronary disease requiring bypass, can favor a surgical strategy.',
    'Explain risks including important MR, embolism, tamponade and an inadequate result. Reassess valve opening, gradient at the documented heart rate, residual regurgitation and symptoms afterward. Medical treatment for rate or volume control may still be necessary. Commissurotomy is an intervention on the mechanical obstruction, not a substitute for thromboembolic prevention or follow-up for recurrent disease.')],['VHD2025','ACCVALVE'])

add('Mitral stenosis','Left Atrial Appendage Thrombus Before Commissurotomy',
 'A stable patient with symptomatic rheumatic MS has otherwise favorable balloon anatomy. Preprocedural TEE identifies LA appendage thrombus. There is no urgent need for intervention, anticoagulation is feasible and surgery is undesirable. Which approach best matches ESC 2025 guidance?',
 'Defer commissurotomy, give appropriate anticoagulation and require repeat TEE confirmation of thrombus resolution before reconsideration',[
 ('Proceed after a procedural heparin bolus because the thrombus is confined to the appendage','A heparin bolus provides procedural anticoagulation but does not immediately dissolve an established appendage thrombus or remove the embolic hazard of instrumentation.'),
 ('Proceed after one month of anticoagulation without repeat imaging','A treatment interval does not prove resolution; the specified delayed pathway requires repeat TEE showing disappearance before commissurotomy is reconsidered.'),
 ('Exclude commissurotomy permanently even if later imaging confirms resolution','Active thrombus precludes the current procedure, but selected stable patients can be reconsidered after anticoagulation and documented resolution; an initial finding is not necessarily a lifelong exclusion.')],
 [S('Embolic Hazard and Immediate Decision','**LA thrombus is a contraindication to proceeding with commissurotomy while it remains present.** Appendage location does not by itself make catheter intervention safe.',
    'Assess rhythm, prior embolism, anticoagulant exposure and bleeding risk. TEE should establish thrombus location and distinguish it from spontaneous echo contrast or artifact.',
    'If clinical instability makes delay unsafe, the valve team must select another urgent plan rather than simply applying a stable outpatient pathway.'),
  S('Selected Delayed Reassessment','**ESC 2025 permits a reassessment pathway for selected appendage thrombus when surgery is contraindicated or intervention need is not urgent.** Appropriate oral anticoagulation can be given for 1–3 months, followed by repeat TEE.',
    'Reconsider commissurotomy only if imaging confirms resolution and the remaining suitability criteria are still met. Persistent thrombus requires further specialist planning.',
    'In rheumatic MS with AF, VKA anticoagulation with INR 2–3 is the established framework; DOAC convenience should not be assumed to establish equivalent protection. Document the monitoring plan and responsible reviewer. Resolution permits reassessment of the procedure, not automatic discontinuation of anticoagulation when AF or another continuing indication remains.')],['VHD2025','ACCVALVE'])

R['INVICTUS']=('INVICTUS randomized trial, 2022','https://doi.org/10.1056/NEJMoa2209051')
R['PREG2025']=('ESC cardiovascular disease and pregnancy guideline, 2025','https://doi.org/10.1093/eurheartj/ehaf193')

add('Mitral stenosis','Anticoagulant Selection in Rheumatic MS With AF',
 'A nonpregnant adult with rheumatic mitral stenosis, valve area 1.1 cm² and persistent AF needs long-term embolic prevention. There is no active bleeding and INR monitoring is feasible. Which strategy is best supported?',
 'A vitamin K antagonist adjusted to INR 2–3',[
 ('Rivaroxaban at the standard renal-adjusted AF dose','Standard AF dosing does not overcome the evidence limitation in rheumatic MS; INVICTUS favored VKA over rivaroxaban for its primary composite outcome.'),
 ('Apixaban at the standard age-, weight- and renal-adjusted AF dose','Apixaban is appropriate for many AF patients, but the general DOAC preference should not be transferred to clinically important rheumatic MS, which requires the established VKA strategy.'),
 ('Aspirin plus clopidogrel instead of oral anticoagulation','Dual antiplatelet therapy has coronary indications but does not provide equivalent prevention of atrial cardioembolic events in this high-risk valve-associated AF setting.')],
 [S('Valve-Specific Thromboembolic Risk','**Rheumatic mitral obstruction and AF promote atrial stasis and thrombus formation.** Anticoagulant selection must incorporate the valve lesion rather than rely only on a general AF risk score.',
    'The ESC 2025 MS section specifies VKA therapy with INR 2–3 for AF and advises avoiding DOACs with mitral valve area ≤2.0 cm² on current evidence. This case is well within the clinically important rheumatic range.',
    'Review bleeding, interactions, renal and hepatic disease, adherence and monitoring access. A fixed warfarin dose cannot replace INR-guided adjustment.'),
  S('Randomized Evidence and Monitoring','**INVICTUS compared rivaroxaban with adjusted VKA therapy in rheumatic heart disease-associated AF.** VKA produced fewer primary composite events without a significant increase in major bleeding.',
    'The composite included stroke, systemic embolism, MI and death from vascular or unknown causes. Its interpretation must retain that population and endpoint.',
    'Explain INR testing, dose changes, interactions and consistency of vitamin K intake. Investigate inadequate time in therapeutic range and address barriers rather than assuming any DOAC is an evidence-equivalent substitute. Rate control, rhythm management and relief of valve obstruction are separate decisions; none automatically removes an ongoing anticoagulation indication. Pregnancy requires a dedicated maternal–fetal anticoagulation plan and should not be managed by copying this nonpregnant prescription.')],['VHD2025','INVICTUS','ACCVALVE'])

add('Mitral stenosis','Persistent Mitral Stenosis Symptoms During Pregnancy',
 'At 24 weeks of pregnancy, a patient with rheumatic MS remains NYHA III despite appropriate diuresis and beta-1-selective rate control. SPAP is 62 mmHg. Valve area is 0.9 cm², anatomy is favorable for commissurotomy, MR is mild and TEE shows no LA thrombus. What is the preferred next assessment?',
 'Pregnancy Heart Team evaluation for percutaneous mitral commissurotomy',[
 ('Continue medical treatment with intervention scheduled only after delivery','That approach can suit controlled disease, but persistent NYHA III symptoms and SPAP >50 mmHg despite therapy support assessing intervention now rather than fixing a postpartum-only plan.'),
 ('Proceed directly to surgical replacement because severe MS excludes catheter treatment in pregnancy','Surgery during pregnancy has important fetal risk and is generally reserved for life-threatening situations when other options fail; suitable commissurotomy anatomy supports the percutaneous option.'),
 ('Plan delivery at twenty-four weeks before reassessing valve intervention','Delivery can become necessary in selected maternal or fetal emergencies, but it carries substantial prematurity consequences here; suitable catheter treatment offers a route to relieve obstruction while continuing pregnancy.')],
 [S('Why Pregnancy Exposes Obstruction','**Increased flow and heart rate raise the transmitral gradient and left atrial pressure.** An apparently stable lesion before pregnancy can become poorly tolerated as circulatory demands increase.',
    'Assess symptoms, congestion, rhythm, pulmonary pressure and fetal status. Use diuretics and appropriate beta-1-selective rate control when indicated, with individualized dosing and monitoring.',
    'Tachyarrhythmia, anemia or infection can worsen the hemodynamics and should be sought and treated alongside the valve assessment.'),
  S('Intervention After Medical Treatment','**ESC 2025 supports considering commissurotomy for severe symptoms or SPAP >50 mmHg despite medical therapy.** Favorable anatomy and exclusion of thrombus remain necessary.',
    'The valvular guideline favors performing it after the twentieth week when feasible. This timing preference does not justify delaying rescue of a deteriorating mother.',
    'Use an experienced Pregnancy Heart Team and valve center, minimize radiation and plan maternal and fetal monitoring. Surgery is considered when maternal survival is threatened and alternatives are unsuitable or unsuccessful. Follow-up must include delivery and postpartum planning because major volume shifts can precipitate decompensation. An intervention during pregnancy does not complete the need for longitudinal valve and reproductive counseling.')],['PREG2025','VHD2025'])

add('Mitral stenosis','Calcific Mitral Obstruction Requires a Different Intervention Strategy',
 'An older patient has limiting dyspnea despite medical treatment, severe mitral annular calcification extending into both leaflet bases and important inflow obstruction. There is no commissural fusion. Why is standard balloon commissurotomy unsuitable?',
 'The calcific obstruction lacks fused commissures that can be split by the procedure',[
 ('The elevated transmitral gradient by itself mandates surgical replacement','Gradient contributes prognostic information but depends on rate and flow; it does not independently establish an optimal intervention without integrated anatomy, ventricular and risk assessment.'),
 ('The absence of rheumatic disease makes all transcatheter mitral treatment ineffective','Standard commissurotomy is mechanistically unsuitable, but selected transcatheter replacement options can be considered after specialist assessment; they have substantial anatomical and procedural limitations.'),
 ('The patient’s age alone is an absolute contraindication to balloon treatment','Age influences procedural risk and expected benefit but is not the mechanism-specific reason; the key difference is annular/leaflet calcification without a splittable fused commissure.')],
 [S('Mechanism of Degenerative Obstruction','**Mitral annular calcification can extend into the leaflet bases and restrict inflow without commissural fusion.** The orifice differs from the funnel-like rheumatic lesion.',
    'Acoustic shadowing and irregular geometry can limit planimetry. Interpret gradients with heart rate, flow, MR and atrial/ventricular compliance.',
    'Treat congestion and relevant comorbidity while clarifying how much of the symptom burden is attributable to the valve.'),
  S('Specialist Procedural Assessment','**Surgery and transcatheter replacement are complex options requiring a valve center.** Heavy calcium can make surgical decalcification and reconstruction hazardous.',
    'For a transcatheter strategy, CT planning assesses anchoring, sealing and predicted LV outflow tract obstruction. Valve embolization, paravalvular leak and LVOT obstruction are important risks.',
    'Severe symptoms do not make an anatomically unsuitable intervention beneficial. Assess frailty, ventricular function, pulmonary pressure, associated disease and the prospect of functional recovery. Conversely, absence of commissural fusion should not be confused with absence of any treatable obstruction. The Heart Team must compare feasible procedures with optimized medical care and avoid claiming that outcomes of rheumatic balloon commissurotomy apply to calcific annular disease.')],['VHD2025','ACCVALVE'])

add('Mitral regurgitation','Atrial Versus Ventricular Secondary Mitral Regurgitation',
 'A patient with longstanding AF and HFpEF has severe MR, marked LA and mitral annular enlargement, preserved LVEF and no important LV enlargement. Leaflets show no prolapse, flail segment or major calcification. Which mechanism is most likely?',
 'Atrial secondary mitral regurgitation',[
 ('Ventricular secondary mitral regurgitation from ischemic tethering','Ventricular secondary MR typically involves LV remodeling and displacement of the papillary apparatus; the dominant atrial/annular remodeling without important LV enlargement favors the atrial phenotype.'),
 ('Primary degenerative mitral regurgitation','Primary degenerative MR arises from intrinsic leaflet or chordal disease, such as prolapse or flail; those structural abnormalities are absent in the supplied assessment.'),
 ('Rheumatic primary mitral regurgitation','Rheumatic valve disease can produce restricted leaflet motion and mixed stenosis/regurgitation, but does not best explain the annular/atrial remodeling pattern with otherwise unremarkable leaflets.')],
 [S('Identify the Dominant Remodeling Process','**Secondary MR results from altered geometry and closing/tethering forces rather than a primary leaflet lesion.** The atrial and ventricular forms differ in their dominant remodeling substrate.',
    'Chronic AF and HFpEF can accompany atrial and annular enlargement with inadequate leaflet coaptation despite preserved global LV systolic function.',
    'Ventricular secondary MR commonly accompanies dilated or ischemic cardiomyopathy with papillary displacement and systolic leaflet tethering. Mixed or advanced phenotypes can blur these distinctions.'),
  S('Consequences for Management','**Treat the underlying substrate and assess MR under representative loading conditions.** Congestion and hypertension can exaggerate functional regurgitation.',
    'Optimize appropriate HF treatment, volume status and rhythm/rate management before definitive procedural selection. Preserved EF does not make severe MR trivial or prove that all symptoms are nonvalvular.',
    'Review comprehensive echo anatomy, regurgitant severity, pulmonary pressure and right-sided consequences; CMR can help when measurements conflict. Persistent symptomatic severe MR warrants a mechanism-specific valve-team discussion. Evidence from ventricular-HFrEF trials should not automatically be applied to atrial MR with preserved EF. Primary leaflet repair decisions also require a different rationale from procedures aimed at annular remodeling or secondary coaptation failure.')],['VHD2025','REGURG'],
 table=(['MR category','Dominant substrate','Characteristic clue'],[
 ['Primary','Intrinsic leaflet/chordal disease','Prolapse, flail, destructive or rheumatic leaflet abnormality'],
 ['Ventricular secondary','LV remodeling and papillary displacement','Tethering with dilated or ischemic LV disease'],
 ['Atrial secondary','LA and annular remodeling','AF/HFpEF, preserved EF and relatively preserved LV geometry']]))

add('Mitral regurgitation','A Small Wall-Hugging Jet Can Conceal Severe MR',
 'A patient with posterior leaflet flail has a relatively small eccentric color jet tracking along the LA wall. Vena contracta is 0.8 cm, EROA 0.45 cm² and regurgitant volume 68 mL/beat. Which interpretation is most appropriate?',
 'Severe MR supported by integrated evidence despite the small displayed jet area',[
 ('Mild MR because the displayed jet occupies less than twenty percent of LA area','Jet area is particularly unreliable in eccentric wall-impinging regurgitation; energy loss along the wall can make a severe leak appear deceptively small.'),
 ('Moderate MR because eccentric direction invalidates every quantitative method','Eccentricity creates method-specific limitations, but does not automatically invalidate carefully acquired vena contracta or quantitative flow measurements; integrate their technical reliability.'),
 ('Unclassified MR until CMR replaces all echo measurements','CMR is valuable when echo is inconclusive or discordant, but is not mandatory before grading a technically sound study with concordant severe quantitative findings and flail anatomy.')],
 [S('Color Jet Area and the Coanda Effect','**An eccentric jet can adhere to the atrial wall and appear smaller than its regurgitant volume suggests.** Color settings, driving pressure and LA pressure further affect its appearance.',
    'Assess the mechanism and the narrow jet origin rather than using distal area alone. Flail anatomy is an important clue that the apparent small color area may be misleading.',
    'In acute MR, a high LA pressure and low systemic pressure may further reduce the visible jet despite major hemodynamic compromise.'),
  S('Integrated Quantification','**The supplied measurements converge on severe primary MR.** Check whether the jet is holosystolic, the vena contracta plane is correct and quantitative calculations are internally consistent.',
    'Single-frame PISA or vena contracta measurements can overstate the total burden of a brief late-systolic jet. Multiple jets, noncircular orifices and constrained flow convergence require additional care.',
    'Use pulmonary-vein flow, chamber response and other supportive findings when suitable. TEE clarifies complex anatomy; CMR can resolve uncertain regurgitant volume or ventricular response. Once severity is established, intervention depends on symptoms, LV function and dimensions, repairability and clinical risk rather than color-jet area alone.')],['REGURG','VHD2025'],
 table=(['Common severe primary-MR measurement','Boundary'],[
 ['Single-plane vena contracta width','≥0.7 cm'],
 ['EROA','≥0.40 cm²'],
 ['Regurgitant volume','≥60 mL/beat'],
 ['Regurgitant fraction','≥50%']]))

R['BSEMITRAL']=('British Society of Echocardiography mitral valve assessment guideline, 2021','https://pmc.ncbi.nlm.nih.gov/articles/PMC8495880/')

add('Mitral regurgitation','Systolic Restriction in the Carpentier Framework',
 'After an inferolateral infarct, mitral leaflets are structurally intact but tethered apically during systole by papillary displacement. Diastolic opening is preserved. Which Carpentier category describes the dysfunction?',
 'Type IIIb',[
 ('Type I','Type I denotes normal leaflet motion with another mechanism such as annular enlargement or perforation; this patient has restricted systolic excursion from tethering.'),
 ('Type II','Type II denotes excessive leaflet motion, including prolapse or flail; this patient’s leaflets are held below the coaptation plane rather than moving excessively into the atrium.'),
 ('Type IIIa','Type IIIa involves restriction during systole and diastole, often with rheumatic structural disease; preserved diastolic opening favors IIIb instead.')],
 [S('Classify Motion Rather Than Severity','**Carpentier classification describes leaflet dysfunction.** It is not an MR severity grade or a complete etiological diagnosis.',
    'The case supplies a ventricular mechanism with systolic restriction and preserved diastolic opening, corresponding to IIIb. Regional ischemic remodeling can create asymmetric tethering without a primary leaflet tear.',
    'Document which leaflet segments are affected, coaptation geometry and the ventricular substrate; a single class does not describe all repair-relevant anatomy.'),
  S('Connect Mechanism With Treatment','**Ventricular secondary MR requires treatment of the ventricular disease before isolated valve decisions are finalized.** Optimize indicated HF therapy, assess revascularization and resynchronization where appropriate.',
    'Reassess MR severity under stable loading conditions. Persistent symptomatic severe disease can warrant valve-team consideration of TEER or surgery according to anatomy and clinical eligibility.',
    'Do not apply prolapse-repair expectations to a tethered valve or assume that an intact leaflet means the regurgitation is benign. Mixed mechanisms can occur: a patient can have intrinsic leaflet disease and ventricular tethering together. Integrated imaging and a treatment plan addressing the actual substrate are more useful than assigning a classification label without its physiological context.')],['BSEMITRAL','VHD2025'],style='direct',
 table=(['Carpentier type','Motion','Typical mechanism'],[
 ['I','Normal','Annular dilation or leaflet perforation'],
 ['II','Excessive','Prolapse or flail'],
 ['IIIa','Restricted in systole and diastole','Rheumatic leaflet/subvalvular disease'],
 ['IIIb','Restricted primarily in systole','Ventricular remodeling with tethering']]))

add('Mitral regurgitation','Acute Chordal Rupture With Pulmonary Edema',
 'A previously stable patient with degenerative mitral disease develops abrupt pulmonary edema. Echo shows a new flail posterior leaflet from chordal rupture, severe MR, a nondilated LA and preserved EF. Blood pressure is 108/70 mmHg. Which plan is most appropriate?',
 'Stabilize respiratory and hemodynamic status while arranging urgent valve-team surgical assessment',[
 ('Treat with diuretics and await progressive LA enlargement before referral','An unadapted LA can develop very high pressure before dilating; chamber enlargement is not a prerequisite for urgent assessment of acute severe structural MR.'),
 ('Optimize chronic HFrEF treatment for three months before considering the valve','That sequence can apply to ventricular secondary MR, but it does not repair a ruptured chord or justify delaying assessment of acute severe primary MR.'),
 ('Use preserved EF to select outpatient reassessment after symptoms improve','EF can remain normal or hyperdynamic because blood ejects into the low-impedance LA; it does not establish adequate forward output or safety after acute structural failure.')],
 [S('Acute Left Atrial Pressure Rise','**A sudden regurgitant volume enters an atrium that has not adapted to chronic loading.** Pulmonary venous pressure can rise sharply, producing edema despite little chamber enlargement.',
    'A soft or short murmur and a small color jet do not exclude severe acute disease. Rapid pressure equalization and eccentric wall impingement can obscure familiar chronic signs.',
    'TEE can clarify the disrupted segment and repair anatomy if TTE is incomplete, while urgent coordination and stabilization proceed.'),
  S('Bridge to Definitive Valve Treatment','**Support oxygenation and treat congestion while selecting urgent definitive care.** The cause is primary structural failure rather than secondary ventricular tethering.',
    'Afterload reduction can improve forward flow when blood pressure permits, but hypotension requires a different individualized support strategy. Do not give a vasodilator simply because it is useful in a hypertensive MR presentation.',
    'At an experienced center, repair may be feasible for chordal rupture; replacement or selected transcatheter rescue may be required according to anatomy and operative risk. These options require specialist selection rather than an automatic equivalence claim. Temporary symptom improvement does not restore the ruptured apparatus. Document the cause, hemodynamic trajectory and repair assessment so the patient is not placed into a prolonged chronic-HF observation pathway.')],['VHD2025','REGURG','ACCVALVE'])

add('Mitral regurgitation','An EF of Fifty-Eight Percent Is Abnormal in Severe Primary MR',
 'An asymptomatic low-risk patient has confirmed severe chronic degenerative MR that is highly likely to be durably repaired. LVEF is 58%, LVESD 38 mm and LVESDi 19 mm/m². Which plan best matches ESC 2025 guidance?',
 'Refer for mitral surgery because the EF criterion for LV dysfunction is met',[
 ('Continue surveillance because EF exceeds fifty percent','The usual lower EF boundary used in other settings is not the MR intervention threshold; severe MR has an established dysfunction trigger at EF ≤60%.'),
 ('Wait until LVESD reaches forty millimeters because both EF and diameter criteria are required','The ventricular triggers are alternatives rather than a requirement to cross both. This patient already meets the EF criterion.'),
 ('Wait until pulmonary hypertension or AF develops despite the reduced EF','AF and pulmonary hypertension can affect earlier intervention timing, but their absence does not cancel an already established LV systolic trigger.')],
 [S('Load-Dependent Ejection Fraction','**Total EF includes regurgitant ejection into the LA as well as forward ejection into the aorta.** It can appear preserved while myocardial reserve and effective forward function deteriorate.',
    'For severe primary MR, an EF of 58% is not reassuring simply because it lies above a conventional general-cardiology threshold.',
    'Confirm the measurement, severity and mechanism. Serial imaging and CMR can help when values or chamber measurements are uncertain.'),
  S('Independent Ventricular Triggers','**ESC 2025 identifies LVEF ≤60%, LVESD ≥40 mm or LVESDi ≥20 mm/m² as LV criteria for intervention assessment in asymptomatic severe primary MR.** This patient qualifies through EF.',
    'Durable repair is preferred when feasible at an experienced center. Operative suitability, repair probability and patient preferences remain central.',
    'When no intervention criteria are met, genuinely asymptomatic severe MR requires active follow-up, typically clinical and echocardiographic review twice yearly under ESC guidance. New symptoms prompt earlier assessment. Do not wait for advanced conventional HFrEF or require every adverse marker to appear: the purpose of valve-specific boundaries is to identify myocardial consequences before they become less reversible.')],['VHD2025','ACCVALVE'])

add('Mitral regurgitation','Durable Repair for Localized Degenerative Disease',
 'A low-risk patient needs intervention for severe primary MR from isolated posterior leaflet prolapse. Expert assessment predicts a durable repair. Which operative strategy is preferred?',
 'Mitral valve repair at an experienced center',[
 ('Chordal-sparing mechanical mitral replacement','Mechanical replacement can be appropriate when a durable repair is unlikely, but entails lifelong VKA and prosthesis-related risks; it is not preferred over an expected durable repair of localized degenerative disease.'),
 ('Chordal-sparing bioprosthetic mitral replacement','Biological replacement is appropriate when replacement is needed and its tradeoffs suit the patient; tissue degeneration and prosthesis-related complications do not favor it over the feasible durable repair supplied here.'),
 ('Transcatheter mitral edge-to-edge repair','TEER is valuable in selected higher-risk primary MR, but lower invasiveness does not establish equivalent lifetime results to durable surgical repair in this low-risk patient.')],
 [S('Preserve the Native Apparatus When Durable','**Surgical repair is preferred for severe primary MR when a durable result is expected.** Localized posterior prolapse is often favorable, but the assessment must account for the actual segment, tissue and center expertise.',
    'Repair aims to restore coaptation while preserving the native subvalvular apparatus. It can avoid prosthesis-specific complications and the anticoagulation required by a mechanical replacement.',
    'Complex anterior or bileaflet disease, substantial calcification, rheumatic restriction or destructive disease can reduce repair feasibility or durability.'),
  S('Counseling and Follow-Up','**An expected durable repair is a clinical judgment, not a guarantee of freedom from recurrence.** Review residual MR, transmitral gradient and ventricular function after the procedure.',
    'If repair cannot achieve a satisfactory durable result, replacement may be appropriate. Prosthesis selection then requires a separate discussion of anticoagulation, bleeding risk, durability and future intervention.',
    'A minimally invasive surgical access route is distinct from a transcatheter repair strategy. Discuss recovery and procedural risks without conflating these methods. Continue follow-up for recurrent regurgitation, functional obstruction, arrhythmia and ventricular recovery. The preference is conditional on repair quality and durability, not a rule to retain a severely diseased valve regardless of the resulting function.')],['VHD2025','ACCVALVE'])

add('Mitral regurgitation','TEER for Symptomatic Primary MR at High Surgical Risk',
 'An older patient has persistent NYHA III symptoms from severe degenerative MR. The Heart Team judges surgical risk high, life expectancy and potential functional benefit reasonable, and TEE anatomy suitable for leaflet grasping without a high predicted residual gradient. Which option should be considered?',
 'Mitral transcatheter edge-to-edge repair',[
 ('Surgical repair based on degenerative mechanism without incorporating the assessed operative risk','Durable surgery is preferred in suitable primary MR, but the patient’s high surgical risk changes the balance; mechanism alone does not override an integrated procedural-risk assessment.'),
 ('Transcatheter mitral replacement before considering leaflet repair','Transcatheter replacement can be considered in selected complex patients, but has additional anatomical and procedural constraints; it is not the preferred first transcatheter strategy when primary MR anatomy is suitable for TEER.'),
 ('Medical treatment alone because high surgical risk excludes valve intervention','Medical care remains important, but high surgical risk does not exclude a feasible transcatheter option when symptoms, anatomy and expected benefit support it.')],
 [S('Clinical and Anatomical Selection','**TEER can be appropriate for selected symptomatic severe primary MR when surgery carries high risk.** It is not simply a default substitute for repair in every anatomically treatable patient.',
    'TEE assesses leaflet tissue, coaptation gap, jet location, calcification, baseline valve area and gradient. Successful reduction of MR must be balanced against the risk of iatrogenic mitral stenosis.',
    'Assess frailty, comorbidity, RV function and pulmonary vascular disease alongside operative-risk estimates and the patient’s goals.'),
  S('Expected Benefit and Surveillance','**The procedural objective is useful MR reduction with an acceptable residual gradient and meaningful clinical benefit.** A technically placed device is not sufficient proof of a successful clinical result.',
    'Discuss residual or recurrent MR, increased gradient and possible future procedures. Surgical treatment after failed TEER can be complex and may require replacement rather than repair.',
    'Continue appropriate diuretics, rhythm care and other indicated treatment while arranging follow-up. If nonvalvular illness dominates symptoms or limits recovery, procedural feasibility alone does not establish benefit. Conversely, symptoms should not be dismissed solely because open surgery is unfavorable. The Heart Team should document both anatomical suitability and why intervention is likely to improve the patient’s remaining functional life.')],['VHD2025','ACCVALVE'])

R['COAPT']=('COAPT randomized trial, 2018','https://doi.org/10.1056/NEJMoa1806640')
R['MITRAFR']=('MITRA-FR randomized trial, 2018','https://doi.org/10.1056/NEJMoa1805374')

add('Mitral regurgitation','Optimize Ventricular Treatment Before Selecting TEER',
 'A patient with newly diagnosed dilated cardiomyopathy, EF 30% and severe ventricular secondary MR has just started HF therapy. There is congestion, blood pressure is elevated and CRT eligibility has not been assessed. There is no acute structural rupture or shock. Which next strategy is appropriate?',
 'Optimize HF therapy, volume and blood pressure, assess CRT eligibility, then reassess MR for a procedural decision',[
 ('Proceed directly to TEER using the admission MR grade as the definitive indication','TEER can help selected patients with persistent important MR despite appropriate treatment, but an untreated congested hypertensive state may exaggerate severity and has not established residual disease after optimization.'),
 ('Arrange isolated surgical annuloplasty before reassessing the response to HF therapy','Annuloplasty can address selected secondary MR, especially in an appropriate surgical context, but initial loading and ventricular treatment have not been optimized; the admission MR grade does not establish an isolated operative indication.'),
 ('Defer valve reassessment until a future hospitalization proves recurrent HF','Optimization requires a planned reassessment, not waiting passively for another event; persistent symptoms and MR can justify intervention review without deliberately awaiting deterioration.')],
 [S('Treat the Ventricular Substrate','**Ventricular secondary MR reflects remodeling, tethering and altered closing forces.** The measured leak can change with loading conditions and ventricular treatment.',
    'Use tolerated guideline-directed HFrEF therapy, including an ARNI or appropriate renin–angiotensin alternative, an evidence-based beta blocker, an MRA and an SGLT2 inhibitor when indicated and safe.',
    'Treat congestion and hypertension, assess ischemic disease and determine whether CRT is indicated from EF, symptoms, rhythm, QRS morphology and duration.'),
  S('Reassess Residual MR and Clinical Need','**Evaluate secondary MR after optimization in a representative euvolemic, normotensive state.** Confirm residual severity, symptoms and ventricular dimensions rather than relying on the worst admission image.',
    'Persistent symptomatic severe disease with suitable anatomy may warrant TEER assessment. Associated coronary surgical needs or other lesions may favor a different strategy.',
    'Advanced ventricular or right-sided disease, severe pulmonary vascular disease and major comorbidity can limit procedural benefit. Document what treatment is tolerated and why target doses cannot be reached; optimization does not mean forcing unsafe medication doses. Establish a follow-up date so the treatment sequence leads to a timely decision rather than indefinite medical deferral.')],['VHD2025','COAPT','ACCVALVE'],
 table=(['ESC 2025 ventricular-SMR TEER outcome-selection domain','Criteria after optimized treatment'],[
 ['Clinical and anatomical','Suitable TEER anatomy; NYHA class ≥II with persistent severe ventricular SMR'],
 ['LV measurements','LVEF 20%–50%; LVESD ≤70 mm'],
 ['HF burden','≥1 HF hospitalization in the preceding year, or BNP ≥300 pg/mL, or NT-proBNP ≥1000 pg/mL'],
 ['Right-sided assessment','SPAP ≤70 mmHg; no severe RV dysfunction'],
 ['Competing treatment needs','No advanced/Stage D HF, CAD requiring revascularization, or severe aortic/tricuspid valve disease'],
 ['Myocardial substrate','No hypertrophic, restrictive or infiltrative cardiomyopathy']]))

add('Mitral regurgitation','COAPT and MITRA-FR Require Population-Specific Interpretation',
 'Which statement best reconciles the original COAPT and MITRA-FR randomized reports when considering TEER for ventricular secondary MR?',
 'COAPT showed benefit in its selected treated population, while MITRA-FR did not show benefit for its primary endpoint; eligibility and treatment context matter',[
 ('Both trials demonstrated equivalent reductions in all-cause mortality','The trials did not report identical results; COAPT showed lower mortality at twenty-four months, whereas MITRA-FR did not establish benefit for its twelve-month primary composite.'),
 ('MITRA-FR invalidates TEER for patients resembling the COAPT population','A neutral study in one population does not erase a positive randomized comparison with different selection and treatment context; assess applicability rather than selecting one trial name universally.'),
 ('COAPT establishes benefit whenever any MR accompanies reduced EF','COAPT eligibility included clinically important secondary MR despite maximally tolerated treatment and procedural suitability; it cannot justify TEER for every lesser leak or untreated cardiomyopathy.')],
 [S('Keep Endpoints and Time Horizons Distinct','**COAPT compared TEER plus maximally tolerated medical treatment with medical treatment alone in selected symptomatic secondary MR.** Its primary effectiveness endpoint concerned recurrent HF hospitalization.',
    'MITRA-FR used a twelve-month composite of death or unplanned HF hospitalization. A comparison of results must preserve the endpoint and follow-up rather than treating every reported percentage as the same event measure.',
    'Differences in MR definitions, ventricular remodeling, treatment optimization and procedural results can influence applicability; no single simplified proportion automatically explains every difference.'),
  S('Apply Evidence to a Specific Patient','**First establish persistent clinically important MR despite appropriate ventricular care.** Then assess anatomy, ventricular size/function, right-sided disease and expected benefit.',
    'A positive trial does not make technical device placement sufficient for clinical success. A neutral trial does not imply that treatment is futile in all secondary MR.',
    'Use current guideline selection criteria and Heart Team review rather than a blanket claim that one trial supersedes all others. Atrial secondary MR and primary degenerative MR are different populations and should not inherit ventricular trial conclusions without qualification.')],['COAPT','MITRAFR','VHD2025'],style='direct',
 table=(['Original report','Endpoint and horizon','TEER versus control'],[
 ['COAPT','Annualized HF hospitalizations through 24 months','35.8 versus 67.9 per 100 patient-years; HR 0.53'],
 ['COAPT','All-cause death by 24 months','29.1% versus 46.1%; HR 0.62'],
 ['MITRA-FR','Death or unplanned HF hospitalization at 12 months','54.6% versus 51.3%; no significant difference']]))

R['RESHAPE']=('RESHAPE-HF2 randomized trial, 2024','https://doi.org/10.1056/NEJMoa2314328')

add('Mitral regurgitation','RESHAPE-HF2 Adds Evidence Without Removing Patient Selection',
 'Which conclusion is justified by RESHAPE-HF2 when considering TEER in a patient with symptomatic HF and functional MR despite appropriate treatment?',
 'TEER reduced recurrent HF hospitalization or cardiovascular death in the studied population, supporting selection beyond a single historical trial profile',[
 ('The trial established that ventricular treatment can be omitted before TEER','The intervention was tested on a background of appropriate medical treatment; the result does not support replacing ventricular care with a valve device.'),
 ('The primary result proves an isolated mortality benefit for every severity of secondary MR','The primary result was a composite in a selected functional-MR population; neither isolated mortality superiority nor universal benefit across lesser lesions follows from it.'),
 ('The trial compared TEER with surgical mitral repair and established equivalent durability','The comparator was medical therapy rather than surgery, so the trial cannot establish direct procedural equivalence or lifetime durability versus surgical repair.')],
 [S('Trial Question and Primary Finding','**RESHAPE-HF2 studied transcatheter repair added to medical treatment for HF with functional MR.** It expanded randomized evidence but did not abolish the need to match a patient to the study context.',
    'At twenty-four months, recurrent HF hospitalization or cardiovascular death occurred at 37.0 versus 58.9 events per 100 patient-years, rate ratio 0.64 with 95% CI 0.48–0.85.',
    'These are event rates, not percentages of patients with an isolated fatal outcome. Repeat hospitalizations can contribute more than one event per patient.'),
  S('Current Procedural Decision','**Assess residual MR after tolerated HF therapy and appropriate CRT or revascularization assessment.** Confirm symptoms, anatomical suitability, ventricular status and anticipated benefit.',
    'The evidence should not be reduced to a single EROA-to-volume label that automatically grants or denies intervention. Different trials used different populations, protocols and endpoints.',
    'The ESC 2025 framework incorporates the evolving ventricular-SMR evidence into Heart Team selection. Discuss expected symptom and hospitalization benefit alongside residual MR, stenosis risk and competing illness. Primary degenerative MR and atrial secondary MR remain distinct treatment settings; this trial does not directly settle their procedural choices.')],['RESHAPE','VHD2025'],style='direct')

add('Mitral regurgitation','Persistent Atrial Secondary MR After Medical and Rhythm Assessment',
 'A patient with HFpEF and AF has symptomatic severe atrial secondary MR despite optimized volume and blood-pressure care and appropriate rhythm-control assessment. Surgery is judged unsuitable, but TEER anatomy is favorable and expected functional benefit is meaningful. Under ESC 2025 guidance, which approach is appropriate?',
 'Consider TEER through a Heart Team discussion using the atrial-MR evidence and its limitations',[
 ('Treat the patient as meeting a definitive COAPT mortality indication because the leak is secondary','COAPT studied ventricular secondary MR with HF and its own eligibility framework; the secondary label alone does not transfer that randomized mortality evidence to atrial MR.'),
 ('Exclude intervention because preserved EF rules out clinically consequential secondary MR','Atrial remodeling can produce severe symptomatic MR despite preserved EF; ventricular EF alone does not establish absence of a valve-related treatment opportunity.'),
 ('Proceed to surgical annuloplasty without incorporating the established surgical unsuitability','Annuloplasty can address the annular mechanism in suitable patients, but an anatomical rationale does not override the patient-specific assessment that surgery is unsuitable.')],
 [S('Treat the Atrial and HFpEF Substrate','**Atrial secondary MR is associated with annular and LA remodeling, often with AF and HFpEF.** It is different from ventricular tethering in dilated or ischemic cardiomyopathy.',
    'Optimize volume and pressure, provide indicated HFpEF treatment and evaluate appropriate rhythm management. The feasibility and potential benefit of rhythm restoration vary with atrial disease and clinical context.',
    'Reassess severity after treatment under stable loading conditions; an improvement in congestion does not necessarily correct advanced annular remodeling.'),
  S('Procedure Selection and Evidence Limits','**ESC 2025 permits considering TEER in symptomatic severe atrial SMR when surgery is unsuitable after medical and appropriate rhythm optimization.** This is a qualified recommendation, not an identical evidence base to ventricular-SMR trials.',
    'Assess leaflet grasping, coaptation, baseline area and predicted residual gradient. Large annular dimensions and limited coaptation can affect success.',
    'Surgical annuloplasty, sometimes combined with AF and associated tricuspid treatment, can be appropriate for eligible surgical patients. For this nonsurgical candidate, compare a feasible TEER result with continued medical treatment and the patient’s priorities. Discuss uncertainty about long-term prognostic benefit and arrange follow-up of MR, gradient, symptoms and HF events rather than promising a trial result from another phenotype.')],['VHD2025'])

add('Mitral regurgitation','Interpreting a Raised Gradient After Mitral Repair',
 'After mitral TEER, a patient has mild residual MR and a mean transmitral gradient of 8 mmHg during AF at 115/min. Congestion is present. Which interpretation and next assessment are most appropriate?',
 'Assess possible post-repair obstruction while reviewing rate, flow and loading, then repeat integrated valve assessment after stabilization',[
 ('Diagnose severe fixed mitral stenosis from the gradient alone and schedule replacement','A raised gradient deserves attention, but tachycardia and loading affect it; one value does not establish fixed severe anatomical obstruction or independently select replacement.'),
 ('Attribute symptoms to HF alone because residual MR is mild','Successful MR reduction does not exclude iatrogenic obstruction, persistent pulmonary hypertension or ventricular disease; the gradient and valve opening require assessment.'),
 ('Use a pressure-half-time valve area alone to exclude postprocedural obstruction','Pressure half-time depends on atrial and ventricular compliance and loading; post-repair orifice geometry and abnormal physiology limit a sole derived-area decision. Integrate anatomy, rate and Doppler findings instead.')],
 [S('Regurgitation and Obstruction Must Both Be Assessed','**A repair can reduce MR while creating an excessive inflow gradient.** The follow-up assessment must therefore evaluate both residual leak and the effective valve opening.',
    'Record heart rate, rhythm and loading with the gradient. Tachycardia shortens diastolic filling time; congestion and altered forward flow can modify the measured burden.',
    'Review the baseline study and procedural result, leaflet motion, device position and available anatomical assessment. A solitary Doppler number is insufficient to characterize the complete repair.'),
  S('Reassessment and Subsequent Care','**Treat the unstable physiological contributors and reassess clinically meaningful obstruction.** Persistent symptoms or a concerning result may require TEE, exercise assessment or other targeted evaluation.',
    'Consider recurrent MR, ventricular dysfunction, AF and pulmonary disease alongside the valve findings. Avoid deciding that every postprocedural symptom must arise from the device.',
    'ESC 2025 notes higher residual MR and increased transmitral gradients after TEER than after surgical repair and supports continued surveillance, generally yearly after TEER when stable. Symptoms or abnormal findings require earlier review. If important persistent dysfunction is established, a specialist team compares further transcatheter treatment, surgery and medical care; the choice depends on anatomy and the clinical trajectory, not on the desire to achieve a lower MR grade alone.')],['VHD2025','BSEMITRAL'])

R['LEADTR']=('EHRA/EAPCI statement on transvalvular leads and tricuspid interventions, 2025','https://pmc.ncbi.nlm.nih.gov/articles/PMC12077151/')

add('Tricuspid and pulmonary valve disease','Direct Device-Lead Interference With Tricuspid Closure',
 'A patient develops important TR after placement of a transvenous pacing lead. Three-dimensional imaging shows the lead impinging on the septal leaflet and preventing systolic coaptation. RV size is only mildly increased and pulmonary pressure is not significantly elevated. Which mechanism is best supported?',
 'Device lead-related TR from direct leaflet interference',[
 ('Ventricular secondary TR caused primarily by pulmonary hypertension','Pressure-related RV remodeling and tethering can cause secondary TR, but the supplied imaging directly demonstrates leaflet interference without important pulmonary hypertension.'),
 ('Atrial secondary TR from isolated annular dilation','Atrial secondary TR can accompany AF with RA and annular enlargement, but it does not account as directly for the demonstrated lead obstructing leaflet closure.'),
 ('Primary infectious leaflet destruction associated with the lead','Device infection can cause TR, but requires clinical and imaging evidence such as vegetation or destructive disease; mechanical impingement alone does not establish infection.')],
 [S('Distinguish Association From Causation','**A lead crossing the valve is not sufficient proof that it causes TR.** Direct imaging of leaflet impingement, adherence or another mechanical interaction supplies stronger causal evidence.',
    'Use comprehensive TTE and 3D TEE when needed to define lead–leaflet interaction, coaptation and the mechanism of the jet.',
    'Mixed disease is possible: a patient can have lead interference together with annular dilation or RV remodeling. Assess the full valve rather than assigning every leak in a paced patient to the lead.'),
  S('Plan Management With Device and Valve Specialists','**A mechanism-specific review is needed before extraction, repositioning or valve intervention.** Lead age, dependence on pacing, alternative pacing options and extraction hazards influence the plan.',
    'Extraction can relieve selected mechanical problems but can also injure the apparatus; do not assume it predictably cures established TR or advanced annular remodeling.',
    'Assess congestion, renal/hepatic consequences, RV function and procedural suitability. Medical diuresis can improve symptoms while the structural problem is evaluated. For transcatheter repair or replacement, lead position and future access require explicit planning. Infection, when suspected, creates a separate diagnostic and extraction pathway; it should not be inferred solely from the temporal association between implantation and regurgitation.')],['VHD2025','LEADTR'])

add('Tricuspid and pulmonary valve disease','Severe TR Despite a Low Jet Velocity',
 'A patient has a broad tricuspid coaptation defect, vena contracta 10 mm, dense triangular CW Doppler and hepatic-vein systolic flow reversal. Peak TR velocity is only 2.2 m/s. Which interpretation is best?',
 'Severe TR is supported; low velocity does not exclude a major regurgitant lesion',[
 ('Mild TR because peak velocity is below three meters per second','Jet velocity reflects the RV–RA pressure difference rather than regurgitant volume alone; rapid pressure equalization can yield low velocity despite severe leakage.'),
 ('Severe pulmonary hypertension established by the broad color jet','Jet size does not quantify pulmonary pressure. Severe TR can also limit the reliability of Doppler pressure estimates, requiring integrated assessment and sometimes catheterization.'),
 ('Moderate TR because hepatic-vein reversal is incompatible with a low gradient','Venous systolic reversal is supportive evidence of important regurgitation; it can coexist with a low ventricular–atrial gradient and must be interpreted with rhythm and other findings.')],
 [S('Pressure Difference Is Not Regurgitant Severity','**The Bernoulli-derived gradient describes the pressure difference driving the jet.** It does not directly measure the size of the regurgitant orifice or the volume leaking through it.',
    'A broad orifice and elevated RA pressure may permit rapid equalization, producing a dense early-peaking triangular signal at a relatively low velocity.',
    'Assess signal quality and alignment before interpreting velocity. A weak incomplete envelope is a different limitation from a genuinely low-gradient severe lesion.'),
  S('Integrated Right-Heart Assessment','**The coaptation defect, broad vena contracta and hepatic flow finding converge on severe TR.** Use multiple views and measurements rather than a velocity cutoff.',
    'Assess RA and RV dimensions, RV systolic function, IVC behavior and left-sided disease. TAPSE alone does not capture every aspect of RV performance, particularly under abnormal loading.',
    'Doppler pulmonary-pressure estimation can be misleading in advanced TR. ESC 2025 recommends right-heart catheterization in all intervention candidates to characterize hemodynamics, including pulmonary vascular resistance and occult precapillary PH. Venous flow is also influenced by AF and RA compliance; interpret it with the valve and chamber findings. Assess severity, cause and downstream effects together before selecting treatment.')],['VHD2025','REGURG'])

add('Tricuspid and pulmonary valve disease','Refer Severe TR Before Advanced Organ Damage',
 'A patient with isolated severe TR has recurrent edema despite diuretics and progressive RV enlargement. There is no severe RV dysfunction, severe pulmonary vascular disease or advanced irreversible hepatic/renal failure. Which next step is most appropriate?',
 'Early specialist valve-team assessment for intervention suitability while optimizing congestion',[
 ('Increase diuretics and defer referral until advanced liver dysfunction establishes severity','Advanced organ dysfunction increases risk and can reduce recoverability; waiting for that stage may lose a useful intervention opportunity rather than establish a desirable prerequisite.'),
 ('Refer only if pulmonary pressure rises substantially on surveillance','Pulmonary hypertension can affect suitability but is not a prerequisite for treating severe symptomatic TR; increasing afterload can instead reduce RV recoverability and procedural benefit.'),
 ('Refer only after a predefined maximal diuretic dose has been reached','Persistent congestion warrants optimization and referral together; renal function, pressure and tolerability determine diuretic dosing, and there is no universal maximum-dose gate before structural assessment.')],
 [S('Identify Progressive Right-Sided Disease','**Recurrent congestion and RV enlargement indicate clinically important consequences of TR.** Medical relief of edema does not establish that the structural problem has resolved.',
    'Track functional capacity, escalating diuretic requirements, renal and hepatic trends, RV size/function and rhythm. Evaluate the cause and associated left-sided disease.',
    'A late presentation with severe irreversible RV or organ dysfunction can have a different benefit–risk balance from this earlier potentially recoverable stage.'),
  S('Assess Recoverability and Procedure Choice','**ESC 2025 emphasizes multidisciplinary assessment of mechanism, disease stage, procedural risk and likelihood of recovery.** Referral should precede an assumption that every advanced consequence must appear.',
    'Repairability, leaflet tethering, annular dimensions, coaptation gap and device leads influence the feasible technique. ESC 2025 recommends right-heart catheterization in intervention candidates to assess filling pressures, pulmonary hemodynamics and vascular resistance.',
    'Compare surgery, transcatheter options and medical care using the patient’s anatomy and goals. Do not promise isolated mortality benefit from symptom or quality-of-life evidence. Explain expected reduction of congestion, procedural hazards and uncertainty, and arrange continued monitoring regardless of the selected strategy. Early assessment means making a timely informed decision, not performing an intervention without testing whether meaningful recovery is likely.')],['VHD2025'])

add('Tricuspid and pulmonary valve disease','Severe TR at the Time of Left-Sided Valve Surgery',
 'A patient undergoing surgery for severe mitral disease also has severe secondary TR with annular dilation. RV function remains adequate and the tricuspid valve is repairable. Which operative plan is best supported?',
 'Concomitant tricuspid repair during the planned left-sided operation',[
 ('Treat the mitral lesion alone and defer TR treatment until right-sided HF develops','Secondary TR may persist or progress after correction of left-sided disease; severe TR at the time of surgery supports concomitant treatment rather than deliberately awaiting late failure.'),
 ('Replace the tricuspid valve because secondary mechanism excludes durable repair','Secondary annular disease can be repairable, and replacement is not mandated by the mechanism alone; repair is preferred when the anatomy permits a satisfactory durable result.'),
 ('Plan isolated transcatheter TR treatment immediately after recovery from mitral surgery','Transcatheter treatment can be useful in selected high-risk patients, but it does not replace the established opportunity for concomitant repair during an already indicated operation in this suitable candidate.')],
 [S('Treat Both Important Lesions','**Severe TR should be addressed when left-sided valve surgery is performed in an appropriate surgical candidate.** Correction of the left-sided lesion does not reliably reverse established annular dilation and leaflet malcoaptation.',
    'Assess the TR mechanism, annulus, leaflet tethering, RV function and pulmonary pressures before the operation.',
    'Repair is favored when feasible. Marked tethering, severe structural damage or an inadequate expected repair may require another strategy.'),
  S('Balance Benefit With Concomitant Risk','**A combined procedure can prevent progression and a later high-risk isolated reoperation.** It still requires assessment of operative burden and the likelihood of right-sided recovery.',
    'Annuloplasty can increase conduction-system injury and pacemaker risk; that tradeoff should be discussed rather than treating additional repair as risk-free.',
    'Less-than-severe TR requires a more individualized indication based on grade, annular size, progression risk and current guidance. Do not transfer the severe-TR recommendation unchanged to every trivial leak. After surgery, monitor residual TR, RV performance, congestion and rhythm. The planned repair should be part of a comprehensive valve operation, not an assumption that right-sided disease is clinically irrelevant once the mitral lesion is corrected.')],['VHD2025'])

R['TRILUMINATE']=('TRILUMINATE Pivotal randomized trial, 2023','https://doi.org/10.1056/NEJMoa2300525')

add('Tricuspid and pulmonary valve disease','Selecting Transcatheter Treatment for Persistent Symptomatic TR',
 'An older patient has severe symptomatic TR despite optimized medical care. Surgical risk is high. RV function is not severely impaired, there is no precapillary pulmonary hypertension and valve anatomy appears suitable for transcatheter repair. Which counseling approach is most accurate?',
 'Consider transcatheter intervention with emphasis on expected symptom and quality-of-life benefit and patient-specific procedural risks',[
 ('Defer transcatheter referral until severe RV dysfunction proves progression','Severe RV dysfunction can reduce the chance of recovery and change eligibility; it is a potential limitation rather than a prerequisite for considering treatment in symptomatic severe TR.'),
 ('Promise a one-year mortality reduction based on the original TRILUMINATE hierarchical result','The original hierarchical advantage was driven predominantly by quality-of-life improvement; it did not establish a separate one-year mortality benefit.'),
 ('Choose the procedure from TR grade without further RV or pulmonary assessment','Severe TR is not sufficient to establish procedural benefit; advanced RV dysfunction and precapillary pulmonary hypertension can materially change suitability and recovery.')],
 [S('Clinical and Anatomical Eligibility','**ESC 2025 supports consideration of transcatheter therapy in selected high-risk patients with symptomatic severe TR despite treatment.** The absence of severe RV dysfunction and precapillary pulmonary hypertension is important.',
    'Assess coaptation gap, jet location, tethering, leaflet tissue and interaction with device leads. Repair and replacement have different anatomical requirements and complication profiles.',
    'Confirm that valve-related congestion is a meaningful contributor to disability and that recovery is plausible. Right-heart catheterization is recommended in intervention candidates rather than relying exclusively on a Doppler pulmonary-pressure estimate.'),
  S('Interpret the Trial Benefit Precisely','**TRILUMINATE Pivotal used a hierarchical endpoint including death or tricuspid surgery, HF hospitalization and health-status improvement.** Its positive one-year result primarily reflected better quality of life.',
    'The win ratio was 1.48; it is not a mortality hazard ratio and should not be presented as a forty-eight-percent survival gain.',
    'Discuss residual TR, bleeding, vascular injury, device-related complications and future treatment needs. Continue medical care and follow-up after intervention. Later trial reports and newer replacement evidence should be interpreted separately by endpoint and duration rather than silently substituted for the original one-year result. A worthwhile symptomatic benefit need not be exaggerated into a proven isolated survival effect.')],['VHD2025','TRILUMINATE'])

add('Tricuspid and pulmonary valve disease','Rheumatic Tricuspid Stenosis in Multivalve Disease',
 'A patient with rheumatic mitral disease has marked systemic venous congestion, prominent jugular a waves and a low-pitched inspiratory diastolic murmur at the lower sternal border. Echo shows restricted tricuspid opening and a mean diastolic gradient of 7 mmHg at 70/min. Which additional lesion is best supported?',
 'Severe tricuspid stenosis',[
 ('Isolated severe tricuspid regurgitation','TR can cause venous congestion but produces systolic regurgitant flow and prominent systolic venous waves; it does not explain the demonstrated diastolic inflow obstruction.'),
 ('Constrictive pericarditis without valve obstruction','Constriction can cause right-sided congestion and respiratory filling abnormalities, but does not account for the directly demonstrated restricted tricuspid orifice and sustained diastolic valve gradient.'),
 ('Isolated precapillary pulmonary hypertension','Pulmonary vascular disease can cause RV pressure overload and secondary TR, but does not itself produce the stated anatomical tricuspid inflow obstruction.')],
 [S('Recognize Right-Sided Inflow Obstruction','**Tricuspid stenosis raises RA pressure and limits RV filling.** Rheumatic disease often accompanies mitral or other valve involvement rather than occurring alone.',
    'The ESC 2025 framework identifies a mean diastolic gradient >5 mmHg at a normal heart rate as severe TS. Flow and rhythm still influence the gradient.',
    'Assess leaflet thickening, commissural fusion, associated TR and the full multivalve burden. An inspiratory increase in a diastolic right-sided murmur supports localization but does not replace imaging.'),
  S('Treat the Combined Disease','**Diuresis can relieve congestion but does not reverse valve fusion.** Evaluate symptoms, severity, RV performance and whether another valve already requires surgery.',
    'A combined operation may be appropriate when severe TS accompanies a surgical left-sided lesion. Selected catheter commissurotomy depends on anatomy and the risk of worsening associated regurgitation.',
    'If replacement is necessary, prosthesis choice must consider the high thrombogenicity of a low-pressure right-sided position. The ESC discussion generally favors a biological prosthesis in this setting. Assess hepatic and renal congestion and functional recovery when planning intervention. Do not assume that treating mitral disease alone will remove a fixed right-sided inflow lesion.')],['VHD2025','STENOSIS'])

R['ACHD2025']=('ACC/AHA adult congenital heart disease guideline, 2025','https://doi.org/10.1161/CIR.0000000000001402')

add('Tricuspid and pulmonary valve disease','Balloon Treatment of Suitable Valvular Pulmonary Stenosis',
 'An adult with isolated doming pulmonary valve stenosis has progressive exertional limitation, peak Doppler velocity 4.5 m/s and RV pressure loading. The valve is suitable for balloon treatment, with no important pulmonary regurgitation or subvalvular obstruction. Which intervention is preferred?',
 'Balloon pulmonary valvuloplasty',[
 ('Surgical pulmonary valve replacement as the first procedure','Surgery is appropriate for unsuitable anatomy, failed balloon treatment or important associated lesions, but a suitable isolated doming valve generally favors balloon valvuloplasty.'),
 ('Surgical pulmonary valvotomy as the initial procedure','Surgical relief is relevant when anatomy is unsuitable for catheter treatment or associated lesions require operation; favorable isolated doming valvular stenosis generally supports balloon treatment first.'),
 ('Surveillance until severe RV systolic failure develops','Symptoms and severe valvular obstruction already support intervention; waiting for advanced ventricular damage is not a necessary prerequisite.')],
 [S('Localize and Grade the Obstruction','**Valvular, subvalvular and pulmonary artery obstruction require different treatment plans.** This stem specifically supplies a favorable doming valve.',
    'The Doppler peak instantaneous gradient is approximately 4 × 4.5² = 81 mmHg. It is not interchangeable with an invasive peak-to-peak gradient.',
    'ACC/AHA grading uses peak velocity <3 m/s for mild disease, 3–4 m/s for moderate disease and >4 m/s for severe disease, corresponding to peak gradients <36, 36–64 and >64 mmHg.'),
  S('Treatment and Long-Term Assessment','**The 2025 adult congenital guideline recommends balloon valvuloplasty for symptomatic moderate or severe valvular PS with favorable anatomy.** An ACHD team should assess associated anatomy and RV consequences.',
    'Dysplastic valves, unsuitable anatomy, important regurgitation or failure of catheter treatment can shift the plan toward surgery.',
    'After relief, monitor residual obstruction, pulmonary regurgitation, RV size/function and exercise capacity. Important late regurgitation may require CMR quantification and a replacement discussion; a low residual gradient does not prove that lifelong follow-up is unnecessary. Decisions about chronic pulmonary regurgitation must incorporate its cause, symptoms and RV response rather than copy a stenosis gradient threshold.')],['ACHD2025','STENOSIS'])

add('Tricuspid and pulmonary valve disease','Pulmonary Regurgitation After Repaired Tetralogy Requires RV Assessment',
 'An asymptomatic adult with repaired tetralogy of Fallot has moderate-to-severe pulmonary regurgitation. CMR shows RV end-systolic volume index 92 mL/m² and RVEF 43%; serial exercise testing shows declining capacity. Under the 2025 ACC/AHA ACHD framework, which approach is appropriate?',
 'Refer to an ACHD valve team to assess pulmonary valve replacement despite absent reported symptoms',[
 ('Continue surveillance until the patient reports exertional symptoms','Symptom-only surveillance can overlook reduced self-selected activity; objective decline and the supplied RV markers already support replacement assessment in the named repaired-tetralogy framework.'),
 ('Defer referral until RV end-diastolic volume exceeds three times LV volume','The named criterion is RV end-diastolic volume at least twice LV volume, not three times; moreover, the other qualifying markers already support assessment without requiring every listed criterion.'),
 ('Defer referral until RVEF falls below thirty-five percent','The specified 2025 marker is RVEF at or below 46% as part of the combined framework; waiting for a conventional advanced dysfunction boundary overlooks the existing adverse findings.')],
 [S('Quantify Regurgitation and Ventricular Consequences','**Chronic pulmonary regurgitation after tetralogy repair can cause progressive RV dilation and dysfunction before symptoms are recognized.** CMR quantifies regurgitant burden and ventricular volumes; serial exercise testing can reveal functional deterioration.',
    'The 2025 ACC/AHA ACHD guideline considers replacement reasonable in asymptomatic repaired tetralogy with moderate or greater pulmonary valve dysfunction and at least two specified adverse markers.',
    'This patient has RVESVi above 80 mL/m², RVEF at or below 46%, and declining exercise capacity. These concordant findings support specialist replacement assessment rather than symptom-only surveillance.'),
  S('Use Anatomy-Specific Criteria','**Other listed markers include RV end-diastolic volume at least twice LV end-diastolic volume and LVEF at or below 50%.** Do not substitute an older isolated RVEDVi threshold for the complete named 2025 framework.',
    'Select surgical or transcatheter replacement using RV outflow anatomy, coronary relationships, associated lesions and device suitability. Imaging and congenital expertise are essential before choosing a procedure.',
    'Assess arrhythmias, residual obstruction, branch pulmonary arteries and other causes of reduced exercise performance. These criteria belong to repaired tetralogy; they should not automatically be transferred to isolated regurgitation following treatment of pulmonary stenosis or to every RV–PA conduit. Replacement can improve loading conditions but does not eliminate lifelong congenital follow-up or all arrhythmic risk.')],['ACHD2025'])

add('Prosthetic valves','Prosthesis Choice Requires a Feasible Anticoagulation Plan',
 'A patient requires surgical valve replacement. Recurrent major bleeding and an inability to maintain safe long-term VKA treatment are established despite specialist assessment. Which prosthesis-selection principle is most appropriate?',
 'Favor a bioprosthesis after discussing durability, early antithrombotic care and future intervention',[
 ('Favor a mechanical prosthesis and use a DOAC instead of VKA','Mechanical valves require an established VKA strategy; substituting a DOAC is not an evidence-supported solution to inability to maintain VKA treatment.'),
 ('Favor a mechanical prosthesis and use antiplatelet treatment alone','Antiplatelet therapy alone does not provide adequate protection against mechanical prosthetic thrombosis and embolism.'),
 ('Favor a bioprosthesis because it guarantees that no anticoagulation will be needed','A tissue valve avoids the mechanical valve’s obligatory lifelong VKA requirement, but early postoperative treatment or another indication such as AF may still require anticoagulation.')],
 [S('Durability and Treatment Burden','**Prosthesis selection is a shared lifetime-care decision.** Mechanical durability must be weighed against bleeding, thrombosis, monitoring, reproductive plans and treatment feasibility.',
    'A bioprosthesis may be preferable when safe VKA therapy is not feasible. That advantage must be balanced against structural degeneration and the potential need for reintervention.',
    'Age informs the discussion but does not override an established anticoagulation problem or the patient’s informed preferences.'),
  S('Plan Beyond the Initial Operation','**A tissue valve does not mean freedom from every antithrombotic indication.** Position, surgical versus transcatheter implantation, early postoperative period and independent embolic risks affect treatment.',
    'Discuss expected follow-up and possible future surgery or valve-in-valve treatment. Small prostheses, coronary anatomy and access can limit later transcatheter options.',
    'Record the reason for the prosthesis choice and the intended medication plan. An unsupported low-anticoagulation regimen should not be used to make an otherwise unsuitable mechanical valve appear feasible. Conversely, describe bioprosthetic durability honestly rather than promising that future treatment will be simple or unnecessary. The appropriate choice connects the device to a treatment and surveillance plan that this patient can safely sustain.')],['VHD2025','ACCVALVE'])

add('Prosthetic valves','Standard INR Target for a Low-Risk Mechanical Aortic Valve',
 'A patient has a current-generation bileaflet mechanical aortic valve, sinus rhythm, normal LV systolic function and no prior embolism or hypercoagulable condition. No device-specific reduced-INR protocol is being used. Which standard VKA target is appropriate?',
 'Target INR 2.5, with therapeutic range 2.0–3.0',[
 ('Target INR 3.0, with therapeutic range 2.5–3.5','A higher target applies to mechanical mitral valves or selected aortic valves with additional risk or older prosthesis characteristics; those features are not supplied here.'),
 ('Target INR 1.75, with therapeutic range 1.5–2.0','This is not the general bileaflet aortic standard; reduced-intensity regimens require specific device, timing and protocol eligibility.'),
 ('Target INR 3.5, with therapeutic range 3.0–4.0','Still higher intensity may apply to particular thrombogenic devices or risk settings, but exposes this low-risk current-generation aortic patient to unnecessary anticoagulation intensity.')],
 [S('Match Target to Valve and Patient','**Mechanical-valve anticoagulation depends on position, prosthesis characteristics and thromboembolic risk.** A single INR target should not be copied to all mechanical devices.',
    'ESC 2025 lists a target of 2.5 with range 2–3 for a current-generation bileaflet or single-tilting aortic valve without additional prothrombotic factors.',
    'Confirm the actual implanted device and relevant history. A patient’s recollection of a metal valve is not enough to select a regimen.'),
  S('Maintain Stable Anticoagulation','**The target is the center of a therapeutic range, not an instruction to accept repeated values at its edge.** Monitor INR and investigate variability, interactions, illness and adherence.',
    'Higher intensity is not automatically safer: bleeding increases while unnecessary escalation may not improve protection. Conversely, repeated subtherapeutic values require prompt assessment.',
    'Do not substitute a DOAC for VKA or add aspirin without an applicable indication and bleeding review. A separate lower-INR protocol cannot be generalized from one valve design to all bileaflet valves. Provide a clear monitoring and interruption plan, including when urgent review is needed for bleeding, embolic symptoms or suspected prosthetic dysfunction.')],['VHD2025','ACCVALVE'])

add('Prosthetic valves','Mechanical Mitral Position Requires a Different INR Target',
 'A patient with a current-generation mechanical mitral prosthesis has no previous embolism and no active bleeding. Which standard long-term VKA target follows the ACC/AHA 2020 framework?',
 'Target INR 3.0, with therapeutic range 2.5–3.5',[
 ('Target INR 2.5, with therapeutic range 2.0–3.0','This is the standard low-risk current-generation mechanical aortic target; mitral position has a different thrombogenic setting and should not inherit that lower target.'),
 ('Target INR 1.75, with therapeutic range 1.5–2.0','The selected On-X aortic reduced-intensity pathway is not the standard regimen for a mechanical mitral prosthesis.'),
 ('Target INR 4.0, with therapeutic range 3.5–4.0','Escalation may be considered after selected embolic events despite therapeutic anticoagulation, but it is not the baseline target for the uncomplicated patient described here.')],
 [S('Position and Thromboembolic Risk','**Mechanical mitral valves require more intensive standard anticoagulation than uncomplicated current-generation aortic devices.** Confirm the actual position and prosthesis before prescribing.',
    'The ACC/AHA 2020 baseline target is INR 3.0, with range 2.5–3.5. Absence of prior embolism does not convert the valve to the lower aortic pathway.',
    'Other device types, additional prothrombotic factors and recurrent embolism can require a separate assessment; identify the framework rather than applying one number to all situations.'),
  S('Safe Long-Term Management','**Maintain VKA therapy with a feasible monitoring plan.** Review adherence, interacting medications, dietary changes, illness and time in therapeutic range.',
    'Aspirin is not an automatic substitute for anticoagulation. Addition for another vascular indication or embolism despite therapeutic treatment requires explicit bleeding-risk assessment.',
    'Before invasive procedures, assess both thromboembolic and bleeding risks; a mechanical mitral valve is not equivalent to a low-risk bileaflet aortic valve. Symptoms of obstruction, embolism or significant bleeding require urgent evaluation. Raising INR intensity without investigating poor control or a suspected prosthetic problem can expose the patient to harm without addressing the cause. Provide a written target, monitoring schedule and contact plan.')],['ACCVALVE','VHD2025'])

add('Prosthetic valves','Device-Specific Reduced INR After On-X Aortic Replacement',
 'Four months after On-X mechanical aortic replacement, a patient has no thromboembolic risk factors and reliable monitoring. The team is considering the ACC/AHA 2020 reduced-intensity option. Which regimen matches that recommendation?',
 'VKA targeting INR 1.5–2.0 with aspirin 75–100 mg daily',[
 ('VKA targeting INR 1.5–2.0 without aspirin','The named reduced-intensity recommendation includes low-dose aspirin; omitting it does not reproduce that specified treatment strategy.'),
 ('VKA targeting INR 1.5–2.0 immediately after any bileaflet valve implantation','The recommendation is specific to selected On-X aortic valves and begins at least three months after surgery; neither the timing nor the broad device generalization is appropriate.'),
 ('Apixaban at its standard AF dose instead of VKA','Reduced INR is still a VKA strategy. It does not establish that a DOAC can safely replace warfarin in a mechanical valve.')],
 [S('Apply Every Eligibility Qualification','**ACC/AHA 2020 permits this lower-INR option for selected On-X aortic recipients without thromboembolic risk factors from at least three months after surgery.** It is a qualified option rather than the universal mechanical-valve standard.',
    'The regimen includes aspirin 75–100 mg daily. Assess aspirin tolerance and bleeding risk as part of the full combination rather than treating the lower INR as an isolated prescription.',
    'Do not extrapolate to mechanical mitral valves, other bileaflet designs or the immediate postoperative period.'),
  S('Monitoring and Evidence Interpretation','**A narrow lower range still requires reliable anticoagulation monitoring and adherence.** Reduced intensity does not mean the device is nonthrombogenic.',
    'Review the implanted model, time since surgery, embolic risk and local protocol. If eligibility changes, reassess the regimen rather than retaining it indefinitely from an old discharge instruction.',
    'Different guideline frameworks may phrase lower-intensity strategies differently, so attribute this question to ACC/AHA 2020. A lower target does not justify unmonitored treatment or anticoagulant substitution. Explain bleeding and thromboembolic symptoms and keep perioperative interruption decisions separate. The important prescribing skill is preserving all device, position, timing and accompanying-drug conditions attached to a special regimen.')],['ACCVALVE','VHD2025'])

R['PROACTXA']=('PROACT Xa randomized trial, 2023','https://doi.org/10.1056/EVIDoa2300067')
R['REALIGN']=('RE-ALIGN randomized study, 2013','https://doi.org/10.1056/NEJMoa1300615')

add('Prosthetic valves','PROACT Xa Does Not Support Apixaban Substitution',
 'A patient with an On-X mechanical aortic valve implanted two years ago asks to replace warfarin with apixaban because the valve has a lower-INR option. Which response is best supported?',
 'Continue an appropriate VKA regimen because the reduced-INR option does not establish apixaban safety in this valve',[
 ('Switch to apixaban because implantation was more than three months ago','PROACT Xa specifically included On-X aortic recipients at least three months after implantation and still did not establish apixaban noninferiority; elapsed time does not justify the switch.'),
 ('Switch to dabigatran because direct thrombin inhibition is established for mechanical valves','RE-ALIGN found excess thromboembolic and bleeding complications with dabigatran versus warfarin; its different mechanism does not supply a safe alternative.'),
 ('Switch to apixaban and add aspirin to reproduce the lower-INR protocol','The reduced-INR regimen is VKA-based; adding aspirin does not convert an unsupported mechanical-valve DOAC strategy into the studied warfarin regimen.')],
 [S('Separate Anticoagulant Intensity From Drug Class','**A lower warfarin INR target remains a VKA treatment strategy.** It is not evidence that the prosthesis can be protected with any oral anticoagulant.',
    'PROACT Xa compared apixaban with warfarin in On-X aortic recipients at least three months after surgery. It was stopped early for excess thromboembolic events with apixaban.',
    'Valve thrombosis or valve-related thromboembolism occurred at 4.2 versus 1.3 events per 100 patient-years. These are event rates rather than an individual two-year event probability.'),
  S('Trial Evidence and Practical Response','**RE-ALIGN also failed to support dabigatran in mechanical valves**, with excess thromboembolic and bleeding complications. General AF DOAC preferences cannot be transferred to this indication.',
    'Address monitoring burden through anticoagulation services, suitable home INR testing, interaction review and adherence support rather than an unsupported substitution.',
    'Reassess eligibility for any device-specific VKA intensity protocol using the actual valve, patient risk and guideline framework. Bioprosthetic-valve AF is a different population and should not be used as an argument for mechanical-valve DOAC treatment. Explain the evidence clearly and keep the medication plan explicit across healthcare transitions.')],['PROACTXA','REALIGN','VHD2025'])

add('Prosthetic valves','A Defined Early VKA Course After Surgical Bioprosthetic Replacement',
 'A patient in sinus rhythm has undergone surgical bioprosthetic mitral replacement. There is no independent lifelong anticoagulation indication and bleeding risk is low. The team selects the ACC/AHA 2020 early VKA option. Which plan matches it?',
 'VKA targeting INR 2.5 for three to six months, followed by reassessment',[
 ('VKA targeting INR 3.0 indefinitely because the prosthesis is mitral','That resembles a mechanical-mitral intensity and lifelong framework; a tissue prosthesis without another indication does not automatically require the same regimen.'),
 ('VKA targeting INR 1.5–2.0 with aspirin from discharge','The selected On-X aortic strategy does not apply to a new surgical mitral bioprosthesis; its device, intensity and timing conditions are different.'),
 ('VKA targeting INR 2.5 for six weeks, followed by reassessment','A six-week course is shorter than the specified ACC/AHA three-to-six-month option. Duration should follow the selected valve-specific framework rather than an assumed routine postoperative interval.')],
 [S('Early Risk Is Different From Lifelong Device Risk','**A bioprosthesis can require antithrombotic treatment during the early postoperative period without requiring lifelong VKA solely because of the device.** Position and implantation route matter.',
    'ACC/AHA 2020 considers VKA to INR 2.5 reasonable for three to six months after surgical bioprosthetic mitral replacement in appropriate patients.',
    'This question specifies selection of that option; it does not imply that every society or every patient has an identical mandatory regimen.'),
  S('Reassess Before Changing Treatment','**Review bleeding, rhythm, ventricular function and any new indication for anticoagulation.** AF, venous thromboembolism or valve thrombosis can change duration and drug selection.',
    'Document the intended INR range, review date and clinician responsible for the next decision. Do not let a time-limited postoperative prescription become indefinite through an undocumented handover.',
    'Antiplatelet treatment and any coronary indication require their own review to avoid unnecessary combination bleeding. Distinguish surgical mitral replacement from valve repair, surgical aortic replacement and TAVI when interpreting guidance. A tissue valve is neither a reason to omit all early antithrombotic care nor a reason to retain the lifelong mechanical-valve regimen.')],['ACCVALVE','VHD2025'])

add('Prosthetic valves','Interruption Without Bridging in a Low-Risk Mechanical Aortic Valve',
 'A patient with a bileaflet mechanical aortic valve needs elective surgery requiring VKA interruption. There is sinus rhythm, normal LV function, no previous embolism and no hypercoagulable condition. Under ACC/AHA 2020 guidance, which approach is appropriate?',
 'Temporary VKA interruption without routine heparin bridging, with a coordinated restart plan',[
 ('Therapeutic heparin bridging because the presence of any mechanical valve mandates it','Valve position and patient risk matter; uncomplicated bileaflet aortic valves are specifically distinguished from higher-risk mechanical settings in the named guideline.'),
 ('Temporary replacement of warfarin with a short-course DOAC','A DOAC is not a validated bridging substitute for mechanical-valve VKA interruption; rapid onset does not establish adequate protection for this indication.'),
 ('Continue VKA unchanged despite the established procedural need for interruption','Some minor procedures permit continuation, but the stem specifies a procedure requiring interruption; the low thromboembolic profile guides bridging rather than negating the procedural bleeding requirement.')],
 [S('Separate Interruption From Bridging','**The procedure determines whether anticoagulation must be interrupted; valve and patient factors inform the need for bridging.** These are related but distinct decisions.',
    'ACC/AHA 2020 recommends interruption without bridging for a bileaflet mechanical aortic valve without additional thromboembolic risk factors.',
    'Mechanical mitral position, an older-generation aortic device or added thromboembolic risk requires a different individualized assessment.'),
  S('Coordinate the Entire Perioperative Interval','**Write an explicit stop, INR-check and restart plan with the procedural and anticoagulation teams.** Timing depends on the intervention, bleeding risk, INR recovery and postoperative hemostasis.',
    'Minor procedures with controllable or inconsequential bleeding often permit VKA continuation; do not generalize the current interruption decision to routine dental or skin care.',
    'Avoid extending the period without anticoagulation through an unclear handover. Guidelines differ in some higher-risk bridging recommendations and evidence remains incomplete, so retain the named framework. Reassess if AF, embolism, ventricular dysfunction or another risk factor is identified. Neither automatic bridging nor automatic omission for every mechanical valve reflects the patient-specific balance tested here.')],['ACCVALVE','VHD2025'])

R['PROSTHIMG']=('ASE/SCMR/SCCT prosthetic valve imaging guideline, 2024','https://www.asecho.org/wp-content/uploads/2024/01/PIIS0894731723005333.pdf')

add('Prosthetic valves','Restricted Mechanical Leaflet Motion Does Not Identify the Cause',
 'A patient with a mechanical aortic valve has a new rise in gradient. Fluoroscopy confirms restricted occluder motion, but echo is limited by shadowing. The patient is stable. Which additional investigation most directly helps distinguish thrombus from pannus?',
 'ECG-gated cardiac CT with an appropriate prosthetic-valve protocol',[
 ('Repeat fluoroscopy as the sole test of tissue composition','Fluoroscopy demonstrates opening angles and restricted motion but cannot reliably establish whether the obstructing tissue is thrombus or pannus.'),
 ('Repeat transthoracic Doppler with dimensionless velocity index as the tissue-discrimination test','Doppler and the dimensionless index can corroborate obstruction and reduce dependence on LVOT diameter, but do not identify whether the obstructing tissue is fibrous pannus or thrombus.'),
 ('Invasive transvalvular pressure measurement as the tissue-discrimination test','An invasive gradient can quantify pressure burden in selected unresolved hemodynamic cases, but does not characterize obstructing tissue. Crossing a mechanical prosthesis also requires particular caution and is not the preferred anatomical discriminator.')],
 [S('Identify Obstruction and Its Mechanism','**A new gradient and restricted leaflet motion establish concern for prosthetic dysfunction, but not its cause.** Compare the current study with the postoperative baseline and assess flow state.',
    'Thrombus may be associated with interrupted or inadequate anticoagulation and a more abrupt course. Pannus is tissue ingrowth that can develop gradually; the processes can coexist.',
    'Timing and INR history are clues rather than substitutes for anatomical assessment. Infection and nonobstructive explanations for increased gradients must also be considered.'),
  S('Complementary Imaging','**Gated CT can assess occluder motion and characterize periprosthetic tissue.** TEE is also valuable, particularly for mitral prostheses and associated masses or regurgitation.',
    'Cine fluoroscopy is complementary for motion but does not determine tissue etiology. CT artifacts, contrast suitability and acquisition quality can limit interpretation.',
    'The distinction changes treatment: fibrinolysis cannot remove fibrous pannus, while selected thrombotic obstruction may be treated by a different urgent strategy. If instability develops, imaging must not delay lifesaving valve-team management. Do not apply a single CT attenuation number as an infallible rule without morphology, protocol and clinical context; the useful outcome is a defensible mechanism-based treatment plan.')],['PROSTHIMG','VHD2025'])

add('Prosthetic valves','Obstructive Mechanical Thrombosis With Shock and High Lytic Risk',
 'A patient with a mechanical mitral valve has confirmed obstructive thrombus, pulmonary edema and shock. Emergency cardiac surgery is available and operative risk is acceptable. There is a previous spontaneous intracranial hemorrhage. Under ESC 2025 guidance, which strategy is favored?',
 'Emergency valve-team surgical management with concurrent stabilization',[
 ('Systemic fibrinolysis as the default before discussing surgical treatment','Fibrinolysis can be appropriate in selected mechanical thrombosis, but critical illness with available surgery and a major intracranial bleeding history strongly favors the surgical pathway here.'),
 ('VKA dose adjustment alone followed by elective imaging in several weeks','Restoring anticoagulation is important, but dose adjustment alone does not provide adequate rescue for confirmed obstructive thrombosis causing shock.'),
 ('Intravenous UFH alone with reassessment after several days if INR becomes therapeutic','Heparin can be part of anticoagulant restoration and treatment in selected less acute thrombosis, but delaying definitive relief in shock from confirmed mechanical obstruction is inadequate when emergency surgery is feasible.')],
 [S('Treat the Hemodynamic Emergency','**Obstructive mechanical-valve thrombosis with shock requires urgent definitive assessment.** Provide respiratory and circulatory support while activating cardiac surgery and the valve team.',
    'Review TTE, TEE or CT confirmation and distinguish thrombus from pannus or mixed obstruction. Additional imaging must not impose an unsafe delay in a deteriorating patient.',
    'Subtherapeutic anticoagulation should be promptly addressed, but this is not a substitute for relieving life-threatening obstruction.'),
  S('Surgery Versus Fibrinolysis','**ESC 2025 retains surgery as the first-line option in critically ill patients while requiring individualized Heart Team choice.** Emergency surgery carries risk, but lysis also risks major bleeding and systemic embolism.',
    'Slow low-dose lytic infusion can reduce complications in selected settings; it does not erase a major contraindication or make every unstable patient a lysis candidate.',
    'Incorporate thrombus features, clinical state, surgical access, bleeding risk and local expertise. Less symptomatic or nonobstructive thrombosis follows a different assessment, often incorporating embolic history and thrombus size. After rescue, establish the cause and a sustainable anticoagulation plan. A history of poor INR control must be corrected without assuming it explains every concurrent structural abnormality.')],['VHD2025','ACCVALVE','PROSTHIMG'])

add('Prosthetic valves','Clinically Relevant Bioprosthetic Thrombosis Before Reintervention',
 'Eighteen months after bioprosthetic aortic replacement, a stable patient has a new gradient rise and exertional dyspnea. Gated CT and echo show leaflet thickening with reduced motion consistent with thrombus, without major calcific degeneration or infection. There is no major bleeding contraindication. Which initial strategy is appropriate?',
 'Therapeutic VKA anticoagulation with planned clinical and imaging reassessment',[
 ('Immediate valve-in-valve replacement without addressing the thrombotic mechanism','Reintervention can be needed for persistent dysfunction or instability, but a stable potentially reversible thrombotic lesion supports an anticoagulation-first assessment rather than automatic device replacement.'),
 ('Proceed directly to redo surgical replacement for presumed irreversible leaflet failure','Surgery can be necessary for irreversible degeneration, persistent dysfunction or instability; demonstrated potentially reversible thrombosis in a stable patient supports an initial anticoagulant trial.'),
 ('Treat with dual antiplatelet therapy and reassess leaflet motion','Dual antiplatelet treatment has coronary indications but does not replace the recommended anticoagulant strategy for clinically relevant bioprosthetic thrombosis; symptom and gradient follow-up remain necessary.')],
 [S('Distinguish Reversible Thrombus From Structural Failure','**A biological valve can develop thrombosis as well as degeneration.** New gradient elevation should be interpreted against the baseline study and current flow state.',
    'TEE or gated CT can assess leaflet thickening, motion and other causes of dysfunction. Infection, pannus, mismatch and regurgitation require consideration when findings suggest them.',
    'Clinically relevant obstruction with symptoms differs from incidental subclinical leaflet thickening without hemodynamic consequences.'),
  S('Anticoagulation and Follow-Up','**ESC 2025 identifies VKA as first-line treatment for clinically relevant biological-valve thrombosis in stable patients.** Acute progressive HF or instability can require urgent intervention or another rescue strategy.',
    'Document the intended anticoagulation regimen and repeat imaging plan, monitoring symptoms, gradients, leaflet motion and bleeding. A treatment response can support the thrombotic mechanism.',
    'Persistent dysfunction requires reassessment of adherence, anticoagulant exposure and alternative or mixed pathology before deciding on reintervention. Recurrence can justify considering extended anticoagulation, balanced against bleeding; it is not an automatic lifelong prescription for every patient with a tissue valve. Explain why the current problem calls for treatment beyond routine bioprosthetic follow-up.')],['VHD2025','ACCVALVE','PROSTHIMG'])

add('Prosthetic valves','Paravalvular Leak With Clinically Important Hemolysis',
 'A patient with a mechanical mitral prosthesis develops recurrent transfusion-dependent hemolysis. TEE identifies a discrete paravalvular leak with anatomy suitable for device closure; occluder motion is normal. Cultures and imaging do not support infection. Redo surgical risk is high. Which strategy is most appropriate?',
 'Expert Heart Team assessment for transcatheter paravalvular leak closure',[
 ('Escalate anticoagulation intensity as the principal treatment','Increasing anticoagulation can address selected thrombotic complications, but cannot seal a demonstrated paravalvular channel and may increase bleeding in an already anemic patient.'),
 ('Continue transfusion and iron replacement as the definitive strategy','Supportive treatment can bridge to intervention or serve patients in whom intervention is unsuitable; recurrent transfusion dependence from a treatable leak warrants assessment for correction.'),
 ('Proceed directly to redo replacement without assessing catheter closure','Redo surgery is important for infection, major dehiscence or unsuitable catheter anatomy; this high-risk patient has a discrete feasible leak and merits assessment of the less invasive option.')],
 [S('Confirm the Source of Hemolysis','**A paravalvular jet can mechanically damage erythrocytes even when the prosthetic occluder functions normally.** Evaluate anemia with reticulocytes, LDH, bilirubin, haptoglobin and a blood film, while excluding bleeding and other causes.',
    'TEE, often with three-dimensional imaging, defines the location, dimensions and relation of the channel to the prosthesis. Assess regurgitation, ventricular consequences and signs of dehiscence.',
    'Exclude prosthetic infection before selecting an elective closure strategy. New fever, bacteremia or unstable seating changes the diagnostic and therapeutic pathway.'),
  S('Select a Corrective Strategy','**ESC/EACTS 2025 supports transcatheter closure as an alternative for significant regurgitation or hemolysis when anatomy is feasible and expertise is available.** The decision integrates surgical risk, leak morphology and patient preference.',
    'Plan device placement to avoid mechanical leaflet interference. Residual narrow jets can perpetuate hemolysis, so technical success requires assessment of residual leakage as well as device stability.',
    'Surgery remains relevant for endocarditis, substantial dehiscence or anatomy unsuitable for effective catheter closure. Transfusion, iron replacement and selected medical measures support the patient but do not repair the channel. After intervention, reassess blood counts, hemolysis markers, symptoms and prosthetic function rather than assuming that a deployed device guarantees clinical resolution.')],['VHD2025','PROSTHIMG'])

add('Prosthetic valves','Valve-in-Valve Planning Requires Coronary and Hemodynamic Assessment',
 'A high-risk surgical patient has symptomatic structural degeneration of a small surgical aortic bioprosthesis. CT shows low coronary origins and narrow sinuses. Which approach best guides the choice between valve-in-valve treatment and redo surgery?',
 'Heart Team planning of coronary obstruction risk, residual gradients and future coronary access before selecting the intervention',[
 ('Select valve-in-valve solely because redo surgical risk is high','High surgical risk supports considering a catheter option but does not establish anatomical safety; coronary obstruction and severe residual mismatch may alter the plan.'),
 ('Select valve-in-valve solely from the labeled surgical prosthesis diameter','The label does not fully describe the true internal diameter, leaflet configuration or coronary relationships; these determine device feasibility and important complications.'),
 ('Exclude valve-in-valve solely because the original prosthesis is small','A small valve raises residual-gradient and mismatch concerns, but size alone is not an absolute exclusion; integrated assessment and available mitigation strategies determine suitability.')],
 [S('Establish the Mechanism of Failure','**Structural degeneration should be distinguished from thrombosis, infection and paravalvular dysfunction before committing to replacement.** Compare symptoms and hemodynamics with the baseline study and use complementary imaging when necessary.',
    'A failed biological valve may be treated by redo surgery or a transcatheter valve-in-valve procedure in selected patients. A mechanical prosthesis is not interchangeable with this scenario.',
    'Identify the original device model and true internal dimensions rather than relying only on a nominal label.'),
  S('Assess the Entire Reintervention Pathway','**CT planning examines displaced leaflet relationships to the coronary ostia and sinotubular junction.** Low origins and narrow root anatomy can increase obstruction or sinus-sequestration risk, requiring expert assessment.',
    'A second valve inside a small prosthesis can leave a high residual gradient or prosthesis–patient mismatch. Evaluate expected hemodynamics alongside procedural risk and symptom benefit.',
    'Future coronary access and the feasibility of subsequent interventions belong in the same lifetime plan. Selected protective or leaflet-modification strategies require specialist expertise and do not eliminate anatomical risk. Redo surgery may offer advantages when catheter anatomy or predicted hemodynamics are unfavorable despite increased operative risk. The final choice should state why the anticipated benefit outweighs the specific hazards in this patient.')],['VHD2025','PROSTHIMG'])

add('Special clinical settings','Mechanical Valve Pregnancy Requires Monitored Therapeutic Anticoagulation',
 'A woman with a mechanical mitral valve is planning pregnancy. Her usual warfarin requirement is 7 mg daily. After counseling she chooses the ACC/AHA 2020 first-trimester LMWH pathway. Which prescription principle is essential?',
 'Therapeutic twice-daily LMWH adjusted using serial peak anti-Xa measurements',[
 ('Once-daily prophylactic LMWH adjusted only to body weight','Prophylactic dosing is used for selected venous thrombosis prevention indications; it does not provide the specified therapeutic mechanical-valve protection.'),
 ('Therapeutic twice-daily LMWH without laboratory surveillance','A therapeutic starting dose alone does not ensure sustained adequate exposure during pregnancy; the mechanical-valve pathway requires anti-Xa-guided adjustment.'),
 ('Therapeutic twice-daily LMWH adjusted to the activated partial thromboplastin time','aPTT is used to guide intravenous UFH in relevant protocols, but does not reliably quantify LMWH exposure; this pathway requires anti-Xa-based surveillance and dose adjustment.')],
 [S('Balance Maternal and Fetal Risks','**A mechanical valve requires effective anticoagulation throughout pregnancy.** Maternal valve thrombosis can be catastrophic, while VKA exposure carries fetal risks that depend partly on dose and gestational timing.',
    'The usual warfarin dose matters: more than 5 mg daily places this patient outside the commonly described low-dose warfarin category. Discuss options before conception through a Pregnancy Heart Team.',
    'LMWH does not cross the placenta, but inadequate dosing or interrupted treatment can expose the mother to valve thrombosis. A prescription is safe only when administration and monitoring are feasible.'),
  S('Named ACC/AHA Monitoring Framework','**ACC/AHA 2020 specifies twice-daily dose-adjusted LMWH with a peak anti-Xa target of 0.8–1.2 U/mL measured four to six hours after dosing.** Regular measurement and specialist adjustment are essential rather than optional reassurance.',
    'Use a therapeutic weight-based starting regimen under the local specialist protocol, then adjust for measured exposure, renal function and evolving pregnancy physiology. Do not substitute a prophylactic dose.',
    'Plan subsequent trimester treatment and delivery transitions in advance; the first-trimester choice is not the entire pregnancy plan. New dyspnea, embolic symptoms or altered valve sounds require urgent assessment. Current ESC guidance emphasizes individualized risk-based anti-Xa targets; preserve the named guideline attribution rather than presenting one target as universal across all valve positions and societies.')],['ACCVALVE','PREG2025'])

add('Special clinical settings','Mitral Stenosis Should Be Addressed Before Pregnancy',
 'A woman planning pregnancy has rheumatic mitral stenosis with valve area 1.2 cm². She reports no limitation during ordinary daily activity. There is commissural fusion, favorable balloon anatomy, mild MR and no left atrial thrombus. Under ESC 2025 pregnancy guidance, which plan is best?',
 'Recommend preconception valve intervention, with balloon commissurotomy assessment',[
 ('Defer valve assessment until symptoms develop during pregnancy','Pregnancy increases flow and heart rate, which can unmask clinically important stenosis; the preconception recommendation is not restricted to women already symptomatic at rest.'),
 ('Start a diuretic and regard symptom control as adequate preconception correction','Diuretics can reduce congestion when present but do not relieve fixed commissural obstruction or replace indicated preconception intervention.'),
 ('Recommend mechanical replacement as the initial procedure despite favorable balloon anatomy','Replacement is appropriate for unsuitable anatomy, important associated regurgitation or other surgical indications; a favorable rheumatic valve supports assessing commissurotomy first.')],
 [S('Pregnancy Changes the Consequences of Obstruction','**A restricted mitral orifice limits accommodation of the increased circulatory demands of pregnancy.** Tachycardia shortens diastolic filling time and can increase left atrial and pulmonary venous pressure.',
    'An apparently asymptomatic patient may have curtailed activity or unrecognized exercise intolerance. Assess functional capacity, rhythm, pulmonary pressure and associated valve disease before conception.',
    'ESC 2025 recommends intervention before pregnancy when mitral valve area is less than 1.5 cm². The 1.2 cm² measurement therefore has management implications despite reassuring ordinary activity.'),
  S('Choose the Procedure From Anatomy','**Percutaneous balloon commissurotomy is particularly relevant when rheumatic commissural fusion is favorable.** Review leaflet mobility, calcification, subvalvular disease and commissural morphology.',
    'Exclude left atrial thrombus and more than mild MR before the procedure. Severe unfavorable calcification, absent fusion or another lesion requiring surgery can redirect treatment.',
    'Reassess residual valve area, MR, symptoms and pulmonary pressure after treatment before advising on pregnancy risk. If replacement is unavoidable, discuss durability and anticoagulation consequences with the Pregnancy Heart Team. Successful intervention reduces an important hemodynamic hazard but does not eliminate the need for individualized pregnancy follow-up, particularly when pulmonary hypertension, AF or residual multivalve disease remains.')],['PREG2025','VHD2025'])

R['PERIOP2024']=('AHA/ACC perioperative cardiovascular guideline, 2024','https://doi.org/10.1161/CIR.0000000000001285')
R['AHAPROPH']=('AHA prevention of infective endocarditis wallet card, 2024','https://www.heart.org/-/media/Files/Health-Topics/Infective-Endocarditis/Infective-Endocarditis-Wallet-Card.pdf')
R['IE2023']=('ESC endocarditis guideline, 2023','https://doi.org/10.1093/eurheartj/ehad193')

add('Special clinical settings','Symptomatic Severe Aortic Stenosis Before Elective Surgery',
 'A patient awaiting elective major abdominal surgery reports exertional syncope. Echo confirms severe high-gradient aortic stenosis. The abdominal operation can safely be deferred and the patient is a candidate for valve replacement. Which sequence is most appropriate?',
 'Defer the abdominal operation for valve-team assessment and indicated aortic valve intervention',[
 ('Proceed with the abdominal operation using an arterial line as the principal risk-reduction measure','Invasive monitoring supports necessary surgery but does not relieve symptomatic fixed outflow obstruction; a deferrable operation permits treatment of the underlying valve indication first.'),
 ('Give diuretics until the gradient falls, then proceed without reassessing the valve','Diuresis can treat congestion but does not reverse calcific obstruction; a lower flow-dependent gradient after treatment is not proof that severe stenosis has resolved.'),
 ('Perform balloon valvuloplasty as the definitive replacement strategy before surgery','Balloon dilation can bridge selected urgent circumstances when definitive replacement is not feasible; it is not the preferred durable substitute in a suitable patient whose operation can wait.')],
 [S('Establish Urgency and Valve Indication','**Exertional syncope with confirmed severe AS constitutes symptomatic disease requiring valve assessment.** Determine whether the noncardiac procedure is elective, time-sensitive or emergent before choosing a sequence.',
    'A deferrable major operation allows the established valve indication to be addressed first. Evaluate coronary disease, ventricular function and procedural suitability as part of the replacement plan.',
    'The 2024 AHA/ACC perioperative guideline supports evaluation for indicated intervention before elective noncardiac surgery. This is different from automatically replacing every asymptomatic valve before any procedure.'),
  S('Coordinate Perioperative Care','**Valve replacement modality depends on anatomy, age, lifetime planning and operative risk.** Agree the timing of subsequent surgery and antithrombotic management with the procedural teams.',
    'If noncardiac surgery cannot wait, multidisciplinary planning weighs valve intervention, selected balloon bridging and proceeding with appropriate monitoring. Maintain preload, vascular tone and rhythm as clinically appropriate.',
    'Monitoring detects deterioration but does not itself remove the obstruction. Avoid treating preserved EF as reassurance against the risk of symptomatic severe disease. Conversely, selected asymptomatic patients with preserved function undergoing low-risk procedures may follow a different pathway. The decision in this stem follows both a clear valve indication and the ability to defer the abdominal operation.')],['PERIOP2024','VHD2025'])

add('Special clinical settings','Dental Endocarditis Prophylaxis After Valve Replacement',
 'An adult with a transcatheter aortic prosthesis is scheduled for dental extraction. There is no penicillin allergy, oral medication can be taken and there is no active infection. Which regimen is the standard first-line AHA oral prophylaxis choice?',
 'Amoxicillin 2 g orally once, 30–60 minutes before extraction',[
 ('Amoxicillin 500 mg orally once, 30–60 minutes before extraction','The agent and timing are compatible with prophylaxis, but the specified adult single dose is 2 g; an ordinary smaller treatment dose does not match the regimen.'),
 ('Amoxicillin 2 g orally daily for five days starting after extraction','Prophylaxis uses a preprocedure single dose rather than an empiric postoperative treatment course; active infection would require a separate therapeutic assessment.'),
 ('Azithromycin 500 mg orally once as the preferred first choice','Azithromycin is an oral alternative in appropriate penicillin-allergic patients; absent allergy and with oral access, amoxicillin is the standard choice tested here.')],
 [S('Identify Both Patient and Procedure','**A transcatheter valve is a prosthetic cardiac valve for dental prophylaxis decisions.** Extraction involves tissue manipulation qualifying for prophylaxis in this high-risk group.',
    'Other AHA high-risk groups include prosthetic valve-repair material, previous IE, unrepaired cyanotic congenital disease or repaired disease with residual shunt/regurgitation adjacent to prosthetic material, and a transplant with regurgitation from a structurally abnormal valve. A native murmur alone does not establish eligibility.',
    'Dental radiographs or appliance adjustment alone do not carry the same indication. Ongoing oral care remains central because a single prescription cannot prevent all endocarditis.'),
  S('Prescribe the Correct Single Dose','**Give amoxicillin 2 g orally 30–60 minutes beforehand in an adult able to take it without allergy.** This is prevention, not treatment of an established infection.',
    'The AHA card lists oral allergy alternatives including cephalexin 2 g, azithromycin or clarithromycin 500 mg, or doxycycline 100 mg. Avoid cephalosporins after penicillin-associated anaphylaxis, angioedema or urticaria.',
    'Clindamycin is no longer recommended for dental prophylaxis. Under the AHA framework, an uninfected routine colonoscopy or TEE does not acquire an antibiotic indication solely from the prosthesis. If fever or bacteremia suggests infection, obtain appropriate cultures before antibiotics when clinically safe and investigate endocarditis rather than prescribing a prophylactic course.')],['AHAPROPH','IE2023'])

R['ENETS2022']=('ENETS carcinoid syndrome and heart disease guidance, 2022','https://pmc.ncbi.nlm.nih.gov/articles/PMC9539661/')

add('Special clinical settings','Nonbacterial Thrombotic Endocarditis in a Hypercoagulable Setting',
 'A patient with metastatic pancreatic adenocarcinoma has cerebral and splenic emboli. TEE shows small mitral vegetations without destructive valve changes. Multiple cultures obtained before antibiotics remain negative and there is no fever. Which diagnosis best integrates the findings, while prompting exclusion of culture-negative infection?',
 'Malignancy-associated nonbacterial thrombotic endocarditis',[
 ('Blood culture-negative infective endocarditis','Fastidious infection or prior antimicrobial exposure can produce negative cultures and embolic vegetations; investigate when appropriate, but the untreated repeatedly culture-negative, noninflammatory presentation and advanced adenocarcinoma favor a sterile thrombotic process.'),
 ('Papillary fibroelastoma with systemic embolization','A fibroelastoma can embolize and mimic a vegetation, but usually appears as a discrete stalked valvular tumor rather than the small vegetations in a strongly hypercoagulable cancer setting.'),
 ('Lambl excrescences as the principal embolic source','Filamentous strands at closure lines may be incidental and their embolic significance can be uncertain; they do not explain this cancer-associated vegetative and multiterritory embolic pattern as well.')],
 [S('Sterile Vegetations and Systemic Embolism','**Nonbacterial thrombotic endocarditis consists of sterile platelet–fibrin deposits associated with systemic prothrombotic disease.** Advanced malignancy, particularly adenocarcinoma, is an important setting.',
    'Mitral and aortic involvement can present through emboli rather than a loud murmur or severe valve destruction. TEE improves assessment when transthoracic imaging is unrevealing.',
    'Libman–Sacks disease is associated with SLE and antiphospholipid antibodies. Its inflammatory and autoimmune context differs from malignancy-associated marantic disease, although both belong in the noninfective differential.'),
  S('Exclude Infection and Treat the Underlying Driver','**Negative routine cultures alone cannot prove that a vegetation is sterile.** Review prior antibiotics, exposures and clinical evidence for fastidious infection, directing serology or molecular testing accordingly.',
    'Evaluate anticoagulation after assessing embolic burden, cerebral hemorrhage and bleeding risk. UFH or LMWH are commonly used in cancer-associated disease; anticoagulant selection in antiphospholipid syndrome requires its own assessment.',
    'Treat the malignancy or autoimmune disorder driving thrombosis and reassess recurrent embolism and valve function. Do not assume DOAC efficacy is established for this indication or initiate anticoagulation solely because an infective vegetation exists. Severe dysfunction or recurrent embolism despite treatment may require surgical discussion, but prognosis, cancer trajectory and operative suitability determine whether intervention offers meaningful benefit.')],['IE2023'])

add('Special clinical settings','Carcinoid Fibrosis of the Right-Sided Valves',
 'A patient with a serotonin-secreting intestinal neuroendocrine tumor and liver metastases develops edema and ascites. Echo shows thickened, retracted tricuspid leaflets with poor coaptation and restricted pulmonary cusps. Which mechanism most plausibly explains the combined valve pattern?',
 'Carcinoid-associated endocardial fibrosis affecting predominantly the right-sided valves',[
 ('Atrial functional tricuspid regurgitation from chronic AF','Atrial enlargement can dilate the tricuspid annulus, but does not explain the characteristic fixed leaflet retraction together with pulmonary cusp involvement.'),
 ('Rheumatic multivalve disease with commissural fusion','Rheumatic pathology can restrict leaflets and involve several valves, but usually has a left-sided pattern and commissural/subvalvular changes rather than this tumor-associated right-sided fibrotic pattern.'),
 ('Pulmonary hypertension causing secondary tricuspid regurgitation','Pressure overload can produce RV remodeling and functional TR, but does not itself account for the primary fibrotic pulmonary and tricuspid leaflet abnormalities described.')],
 [S('Recognize Primary Leaflet Disease','**Carcinoid heart disease produces plaque-like fibrosis with thickening, retraction and fixation of valve tissue.** Tricuspid regurgitation is prominent; stenosis and pulmonary regurgitation or stenosis can coexist.',
    'Assess both right-sided valves and RV size and function. The consequences include systemic venous congestion and progressive right HF rather than an isolated Doppler abnormality.',
    'Pulmonary metabolism of vasoactive mediators usually limits left-sided exposure. Left-sided involvement warrants consideration of an intracardiac shunt, a pulmonary primary or unusually high mediator exposure.'),
  S('Integrate Cardiac and Tumor Management','**Evaluate hormonal activity, tumor burden and cardiac consequences together.** Serial echocardiography, NT-proBNP and appropriately collected 5-HIAA measurements contribute different information.',
    'Somatostatin analogue-based hormonal control and tumor-directed treatment require a neuroendocrine multidisciplinary team. They do not reliably reverse established severe fibrotic valve deformity.',
    'Diuretics relieve congestion with careful attention to renal function and preload. Symptomatic severe valve disease warrants expert surgical assessment in the context of expected oncological survival. Periprocedural planning must address carcinoid crisis risk and specialist hormonal management. Biological replacements are generally favored when surgery is selected, considering bleeding, anticipated procedures and right-sided mechanical thrombosis risk. Follow-up must track both prosthetic function and ongoing mediator activity.')],['ENETS2022'])

add('Special clinical settings','Staged Transcatheter Treatment of Aortic and Secondary Mitral Disease',
 'An older high-surgical-risk patient has symptomatic severe aortic stenosis and severe ventricular secondary MR. There is no primary mitral leaflet lesion. The Heart Team selects a transcatheter strategy and considers both valves treatable. Which sequence is generally preferred?',
 'Treat the aortic stenosis first, then reassess MR and symptoms before deciding on mitral intervention',[
 ('Treat the mitral regurgitation first while leaving severe aortic obstruction untreated','Selected anatomies can require individualized sequencing, but the generally preferred staged strategy addresses the downstream aortic lesion first and avoids committing to mitral repair before assessing its response.'),
 ('Schedule aortic replacement and mitral TEER during the same session','Combined treatment may be appropriate selectively, but in this secondary mechanism the generally preferred staged strategy permits reassessment of MR after relief of aortic obstruction.'),
 ('Schedule mitral TEER at a fixed interval after TAVI without reassessing residual MR','A later date alone does not make the sequence appropriately staged; reassessment may identify improvement, a persisting indication or a different dominant cause of symptoms.')],
 [S('Account for Interacting Hemodynamics','**Multiple valve lesions alter flow and loading conditions across each other.** A gradient or regurgitant measurement obtained in isolation may misrepresent the combined disease burden.',
    'Severe AS increases LV pressure load, while ventricular secondary MR reflects remodeling and tethering rather than a primary leaflet defect. Relief of aortic obstruction can change MR severity.',
    'Improvement is possible but not guaranteed. Persistent myocardial disease, annular dilation or tethering can leave clinically important regurgitation despite a successful aortic procedure.'),
  S('Reassess Before the Next Intervention','**ESC/EACTS 2025 generally favors a staged transcatheter sequence beginning with the aortic lesion, followed as needed by mitral and tricuspid treatment.** Anatomy and the mechanism of each lesion can justify exceptions.',
    'After aortic treatment, reassess symptoms, volume status, ventricular function, MR severity and guideline-directed HF therapy. Consider TEER only if residual disease and patient characteristics support benefit.',
    'The surgical pathway differs: when open surgery is selected, concomitant significant valve disease may warrant combined treatment. A Heart Valve Centre should integrate lesion severity, cumulative procedural risk, expected recovery and patient goals. Do not promise that secondary MR will resolve, or expose the patient to an unnecessary second procedure before its continuing indication is established.')],['VHD2025'])

R['AMLODIPINE']=('DailyMed amlodipine prescribing information, adult dosing','https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=5a0b3dd4-91f5-4173-a992-e91b1cac6a18')

if __name__=='__main__':
    cp=ROOT/'Cardiology'/(DOC+'.coverage.json')
    coverage=json.loads(cp.read_text(encoding='utf-8'))
    decisions=[(s['section'],d) for s in coverage['sections'] for d in s['decisions']]
    assert len(rows)==len(decisions)==coverage['plannedQuestions']
    assert len({d for _,d in decisions})==len(decisions)
    for row,(topic,decision) in zip(rows,decisions):
        assert row['topic']==topic
        row['coverageDecision']=decision
    dest=save('Cardiology',3,DOC,rows,R,'Original educational synthesis with primary-guideline source checks and chapter editorial review. Full Harrison subscription text not accessed; independent clinician review not claimed.')
    bank=json.loads(dest.read_text(encoding='utf-8'))
    bank['status']='chapter_authored'
    bank['plannedQuestions']=coverage['plannedQuestions']
    dest.write_text(json.dumps(bank,ensure_ascii=False,indent=2),encoding='utf-8')
    coverage.update(status='authored_validated',authoredQuestions=len(rows))
    coverage['questionDecisions']=[dict(question=i,title=r['title'],decision=r['coverageDecision'],section=r['topic']) for i,r in enumerate(rows,1)]
    cp.write_text(json.dumps(coverage,ensure_ascii=False,indent=2),encoding='utf-8')
    pp=ROOT/'progress.json';progress=json.loads(pp.read_text(encoding='utf-8'))
    entry=next(x for x in progress['chapters'] if x['subject']=='Cardiology' and x['document']==DOC)
    entry.update(status='authored_validated',plannedQuestions=coverage['plannedQuestions'],authoredQuestions=len(rows))
    pp.write_text(json.dumps(progress,ensure_ascii=False,indent=2),encoding='utf-8')
