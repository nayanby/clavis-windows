"""Original Cardiac Imaging and Hemodynamics chapter."""
from qbank_authoring import question,ref,finalize
R=ref('ASE 2025 Right Heart and Pulmonary Hypertension Recommendations','https://doi.org/10.1016/j.echo.2025.01.006')
D=ref('ASE 2025 LV Diastolic Function and HFpEF Recommendations','https://www.asecho.org/wp-content/uploads/2025/07/Left-Ventricular-Diastolic-Function.pdf')
V=ref('2025 ESC/EACTS Valvular Heart Disease Guideline','https://doi.org/10.1093/eurheartj/ehaf194')
C=ref('2023 ESC Cardiomyopathies Guideline','https://doi.org/10.1093/eurheartj/ehad194')
S=ref('SCCT 2021 Coronary CTA Expert Consensus','https://pmc.ncbi.nlm.nih.gov/articles/PMC8713482/')
P=ref('2025 ESC Myocarditis and Pericarditis Guideline','https://doi.org/10.1093/eurheartj/ehaf192')
rows=[]
def q(*args,**kwargs):rows.append(question(*args,**kwargs))

q('A peak Doppler velocity of 4 m/s is measured across a discrete stenotic valve. Using the simplified Bernoulli equation and negligible proximal velocity, what is the peak instantaneous gradient?',
 '64 mm Hg',[
 ('16 mm Hg','This squares velocity but omits the factor of four.'),
 ('32 mm Hg','This does not apply 4v² correctly.'),
 ('4 mm Hg','Velocity itself is not the pressure gradient.')],
 'Convert velocity to a pressure difference',
 '**The simplified equation is delta P = 4v².**',
 ['At 4 m/s the estimate is 4 × 16 = 64 mm Hg.', 'It assumes negligible proximal velocity and appropriate Doppler alignment.'],
 '**A peak instantaneous Doppler gradient is not the same as a catheter peak-to-peak gradient.**',
 ['The two measurements compare pressure at different moments and should not be treated as interchangeable.', 'Pressure recovery and serial obstructions can further affect interpretation.'],
 [['Velocity','4 m/s'],['Equation','4 × velocity squared'],['Peak instantaneous gradient','64 mm Hg']], [V])
q('Measured oxygen consumption is 250 mL/min. Arterial oxygen content is 20 mL/dL and mixed venous content is 15 mL/dL. What is Fick cardiac output?',
 '5 L/min',[
 ('0.5 L/min','This mishandles the content unit conversion.'),
 ('50 L/min','This treats the per-deciliter difference as a per-liter difference.'),
 ('12.5 L/min','This is not oxygen consumption divided by the arteriovenous content difference.')],
 'Use oxygen content with consistent units',
 '**Cardiac output equals oxygen consumption divided by arterial-minus-mixed-venous oxygen content.**',
 ['The difference is 5 mL/dL, or 50 mL/L.', '250 mL/min divided by 50 mL/L equals 5 L/min.'],
 '**Measured and assumed oxygen consumption are not equivalent in every patient.**',
 ['Assumed consumption can introduce error in unusual body size or metabolic states.', 'Sampling and shunts can also affect the calculation.'],
 [['Oxygen consumption','250 mL/min'],['Content difference','50 mL/L'],['Output','5 L/min']], [R])
q('Mean arterial pressure is 90 mm Hg, right atrial pressure 10 mm Hg and cardiac output 4 L/min. What is systemic vascular resistance in dyn·s·cm⁻5?',
 '1600',[
 ('20','This is the resistance in Wood-unit-style pressure/flow units before multiplication by 80.'),
 ('1800','This omits the right atrial pressure subtraction.'),
 ('800','This does not use the stated pressure difference and output correctly.')],
 'Systemic resistance uses the systemic pressure drop',
 '**SVR = 80 × (MAP minus RAP)/CO in conventional cgs units.**',
 ['The pressure difference is 80 mm Hg.', '80/4 = 20; multiplying by 80 gives 1600.'],
 '**Interpret resistance with flow and perfusion.**',
 ['A high resistance can be compensatory during low output.', 'The number alone does not identify a specific shock cause.'],
 [['Pressure drop','90 minus 10 = 80'],['Flow','4 L/min'],['SVR','1600 dyn·s·cm⁻5']], [R])
q('A patient has cardiac output 4.5 L/min and body surface area 1.8 m². What is cardiac index?',
 '2.5 L/min/m²',[
 ('8.1 L/min/m²','This multiplies rather than divides by body surface area.'),
 ('1.8 L/min/m²','This repeats the body surface area rather than indexing output.'),
 ('4.5 L/min/m²','This fails to index the measured output.')],
 'Indexing adjusts flow for body size',
 '**Cardiac index equals cardiac output divided by body surface area.**',
 ['Here 4.5/1.8 = 2.5.', 'Body-size indexing is useful but can be misleading at extreme body habitus.'],
 '**Use perfusion as well as a threshold.**',
 ['Lactate, urine output and examination help determine whether flow is adequate.', 'A single index does not by itself define the entire shock phenotype.'],
 [['Cardiac output','Total flow per minute'],['Cardiac index','Flow normalized to surface area'],['Clinical interpretation','Combine with perfusion']], [R])
q('A patient with sudden pulmonary edema has very large V waves on the pulmonary wedge tracing. Which valve lesion is an important possibility?',
 'Acute severe mitral regurgitation',[
 ('Isolated severe TR','TR more directly produces prominent right atrial systolic V waves.'),
 ('Pure pulmonary valve stenosis','That does not directly generate large left atrial systolic waves.'),
 ('Aortic coarctation as the specific explanation','The waveform reflects left atrial filling pressure events rather than diagnosing coarctation.')],
 'A wedge tracing can reflect left atrial pressure events',
 '**Systolic regurgitant filling of the LA can generate large V waves.**',
 ['A noncompliant atrium can also create prominent waves, so the finding is not perfectly specific.', 'Echo establishes the valve mechanism and severity.'],
 '**Do not equate a waveform with a complete anatomical diagnosis.**',
 ['Review timing, catheter position and the clinical syndrome.', 'Acutely severe MR can be dangerous despite a soft murmur.'],
 [['Large wedge V wave','Consider MR or low LA compliance'],['Large RA V wave','Consider TR'],['Confirmation','Echo and integrated hemodynamics']], [V,R], 'clinical_scenario')
q('A right atrial pressure tracing shows prominent systolic V waves in a patient with a pulsatile liver. Which lesion best fits?',
 'Severe tricuspid regurgitation',[
 ('Isolated severe MR','MR generates left atrial/wedge rather than primary RA regurgitant V waves.'),
 ('Mitral stenosis as a direct RA systolic regurgitant lesion','MS acts on left atrial filling pressure through a different mechanism.'),
 ('A small restrictive ASD without other disease','That does not directly explain systolic regurgitant venous waves.')],
 'Waveform location matters',
 '**TR returns ventricular systolic flow into the RA.**',
 ['The pressure wave can propagate into the systemic veins and liver.', 'Rhythm and compliance can modify the tracing.'],
 '**Assess RV function and the cause of TR.**',
 ['Functional dilation, lead interaction and primary leaflet disease need different strategies.', 'A waveform supports physiology while imaging defines anatomy.'],
 [['RA systolic wave','Right-sided regurgitant physiology'],['Wedge systolic wave','Left atrial physiology'],['Imaging','Defines mechanism']], [R,V], 'clinical_scenario')
q('Which right atrial waveform finding is more characteristic of classic constriction than tamponade?',
 'A rapid prominent y descent from brisk early ventricular filling',[
 ('A markedly blunted y descent as the defining constriction feature','Blunted early filling is more typical of tamponade.'),
 ('No relation between atrial emptying and ventricular filling','The y descent reflects atrial emptying during early ventricular filling.'),
 ('A systolic V wave as a specific proof of constriction','V-wave prominence is not uniquely diagnostic and may reflect TR.')],
 'Both disorders constrain filling at different phases',
 '**Constriction permits rapid early filling before abrupt restraint.**',
 ['Tamponade can limit filling throughout diastole and blunt the y descent.', 'Respiratory ventricular interaction provides additional discrimination.'],
 '**Use the pattern within the full hemodynamic context.**',
 ['Volume, rhythm and mixed disease can modify waveforms.', 'Echo and pericardial imaging are essential complements.'],
 [['Constriction','Prominent y descent'],['Tamponade','Blunted y descent'],['Interpretation','Not one waveform alone']], [P,R])
q('What does Kussmaul sign describe?',
 'An inspiratory rise or failure of the expected fall in JVP',[
 ('An inspiratory systolic pressure fall greater than 10 mm Hg','That is pulsus paradoxus.'),
 ('A delayed femoral pulse compared with the radial pulse','That is radiofemoral delay.'),
 ('Alternating strong and weak arterial beats','That is pulsus alternans.')],
 'The venous response to inspiration can reveal limited RV filling',
 '**Normally inspiration promotes right-sided venous return with a fall in RA pressure.**',
 ['A restricted right-sided filling response can produce Kussmaul sign.', 'Constriction, restriction and RV infarction are possible contexts.'],
 '**The sign is not a single-disease diagnosis.**',
 ['Assess RV function, valves and pericardial physiology.', 'Distinguish it from the arterial respiratory sign of pulsus paradoxus.'],
 [['Kussmaul','Inspiratory JVP rise or failed fall'],['Pulsus paradoxus','Excess inspiratory systolic fall'],['Meaning','Limited right-sided filling accommodation']], [R,P])
q('A saturation run shows a reproducible oxygen step-up from the venae cavae to the right atrium. Which shunt level is suggested?',
 'An atrial-level left-to-right shunt',[
 ('An isolated ventricular-level shunt as the only possible level','A VSD first raises oxygen content at the RV level.'),
 ('An isolated ductal shunt as the expected first RA step-up','A PDA typically produces a pulmonary arterial-level step-up.'),
 ('A right-to-left shunt as the explanation of increased RA oxygen','The oxygenated entry into the RA indicates left-to-right mixing at that level.')],
 'Localize the first reproducible oxygen increase',
 '**Oxygenated blood entering the RA suggests an ASD or an associated venous connection abnormality.**',
 ['Use appropriate high and low caval and atrial samples.', 'Streaming and anomalous pulmonary veins can complicate interpretation.'],
 '**Confirm the anatomy with imaging.**',
 ['A step-up helps localize but does not identify the exact defect type.', 'Qp:Qs and PVR then quantify different hemodynamic consequences.'],
 [['RA step-up','Atrial-level entry'],['RV step-up','Ventricular-level entry'],['PA step-up','Ductal or other arterial-level entry']], [R], 'clinical_scenario')
q('Which pattern on a saturation run most strongly suggests a VSD?',
 'A first significant step-up from the RA to the RV',[
 ('A first step-up from systemic veins to RA','That suggests atrial-level mixing.'),
 ('A first step-up from RV to PA without an RV increase','That suggests a more distal arterial-level source.'),
 ('Uniform systemic desaturation without a right-sided step-up as a specific VSD proof','That does not localize a left-to-right ventricular shunt.')],
 'Ventricular communication introduces oxygenated blood at RV level',
 '**The LV-to-RV pathway raises RV oxygen content compared with the RA.**',
 ['Sample multiple RV locations when needed because mixing can be uneven.', 'Acquired post-MI septal rupture and congenital VSD share this shunt-level principle.'],
 '**Interpret the size and direction separately.**',
 ['Defect anatomy, pressure gradient and PVR determine the clinical burden.', 'A saturation step-up does not alone establish that closure is safe.'],
 [['RA to RV step-up','Ventricular shunt'],['Shunt quantity','Qp:Qs'],['Closure safety','Includes pulmonary vascular and anatomical assessment']], [R], 'clinical_scenario')
q('A mechanically ventilated patient has a wedge pressure measured during substantial positive intrathoracic pressure. Which interpretation is important?',
 'The measured pressure includes surrounding pressure effects and may not equal the transmural LV filling pressure',[
 ('Every measured wedge is automatically the true transmural preload regardless of ventilation','Intrathoracic pressure changes the relationship.'),
 ('Positive pressure makes all catheter values zero','It alters interpretation rather than eliminating measurements.'),
 ('A fixed subtraction from PEEP is perfectly accurate in every patient','Transmission varies, so a universal correction can mislead.')],
 'Pressure relative to atmosphere differs from pressure across a chamber wall',
 '**Transmural pressure depends on intracavitary minus surrounding pressure.**',
 ['Respiratory timing and PEEP affect interpretation.', 'A technically correct wedge tracing still needs physiological context.'],
 '**Assess the full perfusion and volume picture.**',
 ['Use waveform quality, ventilation, echo and clinical response.', 'Avoid large treatment changes from one uncontextualized number.'],
 [['Measured wedge','Referenced to external zero'],['Transmural filling pressure','Accounts for surrounding pressure'],['Ventilation','Can alter the relationship']], [R])
q('Why is an appropriate dependent zone-3 position desirable for wedge-pressure interpretation?',
 'Pulmonary venous and capillary pressure should exceed alveolar pressure so the measurement reflects downstream vascular pressure',[
 ('Alveolar pressure should dominate the occluded vessel in every case','That can prevent the reading from representing left atrial pressure.'),
 ('Catheter position is irrelevant once the balloon is inflated','Position and waveform are important.'),
 ('A wedge is a direct aortic pressure measurement','It estimates a downstream pulmonary venous/left atrial pressure under suitable conditions.')],
 'A wedge measurement relies on a continuous vascular fluid column',
 '**Alveolar pressure can distort a reading outside suitable physiological conditions.**',
 ['Confirm a proper waveform and avoid over-wedging.', 'Mitral and pulmonary venous disease can also alter the relationship to LV end-diastolic pressure.'],
 '**Do not treat PAWP and LVEDP as identical in every disease.**',
 ['Large MR V waves and mitral stenosis are important examples.', 'Use the measurement appropriate to the clinical question.'],
 [['Suitable wedge conditions','Supports LA pressure estimation'],['Alveolar pressure dominance','Can distort interpretation'],['PAWP versus LVEDP','May differ in valve disease']], [R])

# Noninvasive imaging interpretation completes the chapter.
q('Which statement about E/e-prime in diastolic assessment is most accurate?',
 'It is one contributor to estimating filling pressure and should be interpreted with other measures and the clinical setting',[
 ('A single E/e-prime value is a direct invasive pressure in mm Hg','It is a dimensionless ratio, not a direct pressure measurement.'),
 ('It is equally reliable without qualification in all mitral valve disease','Valve and annular disease can limit interpretation.'),
 ('A normal value excludes every exercise-only HFpEF presentation','Resting indices can miss exertional pressure abnormalities.')],
 'Diastolic function is a multiparameter assessment',
 '**Transmitral flow and annular relaxation reflect related but different physiology.**',
 ['Use E/e-prime with relaxation velocities, atrial findings, pulmonary pressure information and other appropriate variables.', 'Special populations require modified approaches.'],
 '**Do not turn an algorithm component into a universal stand-alone test.**',
 ['Loading, rhythm and valve pathology affect performance.', 'Selected discordant cases need stress or invasive assessment.'],
 [['E/e-prime','Supportive filling-pressure index'],['Mitral/rhythm abnormalities','Can limit usual interpretation'],['Uncertain HFpEF','May need dynamic testing']], [D])
q('Peak TR velocity is 3 m/s and estimated RA pressure is 8 mm Hg. There is no RV outflow or pulmonary valve obstruction. What is estimated pulmonary systolic pressure?',
 '44 mm Hg',[
 ('36 mm Hg','This gives the RV-RA gradient but omits estimated RA pressure.'),
 ('17 mm Hg','Adding velocity rather than 4v² is incorrect.'),
 ('80 mm Hg','This is not the stated Doppler calculation.')],
 'Estimate RV pressure from the TR jet',
 '**RV systolic pressure is approximately 4v² plus RA pressure.**',
 ['Here 4 × 9 + 8 = 44.', 'Without outflow obstruction, RV systolic pressure approximates pulmonary artery systolic pressure.'],
 '**Recognize uncertainty in both terms.**',
 ['Poor alignment, an incomplete envelope and severe TR can affect the velocity estimate.', 'RA pressure estimation is also imperfect, so echo assigns probability rather than replacing RHC when needed.'],
 [['TR gradient','36 mm Hg'],['Estimated RAP','8 mm Hg'],['Estimated PASP','44 mm Hg if no outflow obstruction']], [R])
q('What is a key limitation of TAPSE as a measure of RV systolic function?',
 'It mainly reflects longitudinal annular motion and is load- and geometry-dependent',[
 ('It directly measures the complete RV ejection fraction independent of geometry','TAPSE is not a direct volumetric EF.'),
 ('It is a quantitative measure of LV scar transmurality','It measures tricuspid annular excursion.'),
 ('It cannot change after cardiac surgery despite altered mechanics','Surgery can change the relationship between annular motion and global RV performance.')],
 'The RV needs more than one functional measure',
 '**A one-dimensional longitudinal metric cannot represent every component of RV contraction.**',
 ['Use FAC, tissue velocity, strain and 3D or CMR measures when appropriate.', 'Severe TR and postoperative state can complicate interpretation.'],
 '**Assess function relative to pulmonary afterload.**',
 ['RV-pulmonary arterial coupling provides additional physiological context.', 'Symptoms and serial changes matter more than an isolated borderline number.'],
 [['TAPSE','Longitudinal annular excursion'],['Other measures','Complement global and regional assessment'],['Interpretation','Load and clinical context dependent']], [R])
q('During cancer therapy, GLS changes from -20% to -16% while EF remains preserved. What is the relative reduction in GLS magnitude?',
 '20%, a potentially important subclinical change',[
 ('4%, because only the absolute percentage-point difference matters','The absolute change is four points, but relative reduction is 4/20 = 20%.'),
 ('80%, because 16/20 equals the reduction','That is the remaining fraction, not the loss.'),
 ('No change because both values are negative','A less negative magnitude represents reduced longitudinal shortening.')],
 'Relative strain change differs from percentage-point change',
 '**The magnitude falls from 20 to 16, a 20% relative reduction.**',
 ['A relative GLS decline above 15% is an important cardio-oncology signal.', 'Technical consistency and loading conditions must be considered.'],
 '**Integrate the result with biomarkers, symptoms and EF.**',
 ['It can prompt closer review and cardioprotective planning.', 'Do not automatically stop every cancer treatment from one measurement without multidisciplinary assessment.'],
 [['Absolute change','4 percentage points'],['Relative decline','4/20 = 20%'],['Meaning','Potential subclinical dysfunction signal']], [ref('2022 ESC Cardio-Oncology Guideline','https://doi.org/10.1093/eurheartj/ehac244')], 'clinical_scenario')
q('A dysfunctional myocardial segment improves at low-dose dobutamine but deteriorates at higher doses. What is the classic interpretation?',
 'Viable myocardium with inducible ischemia, a biphasic response',[
 ('Complete transmural scar with no contractile reserve','Initial improvement demonstrates reserve.'),
 ('A normal segment with no ischemic response','High-dose deterioration is not a normal sustained response.'),
 ('An isolated pericardial effusion as the explanation','That does not account for the characteristic segmental biphasic response.')],
 'Low-dose reserve and high-dose demand answer different questions',
 '**Initial improvement suggests viable contractile tissue.**',
 ['Higher-dose stress can expose limited flow reserve.', 'The combined pattern supports viable but jeopardized myocardium.'],
 '**Use viability within a broader revascularization decision.**',
 ['Anatomy, symptoms, ventricular function and procedural risk still matter.', 'A viable segment does not guarantee a universal survival benefit from any intervention.'],
 [['Low dose improves','Contractile reserve'],['High dose worsens','Inducible ischemia'],['Biphasic pattern','Viable jeopardized tissue']], [ref('2024 ESC Chronic Coronary Syndromes Guideline','https://doi.org/10.1093/eurheartj/ehae177')])
q('A high-risk patient has severe multivessel CAD but relatively uniform SPECT perfusion. Which limitation can produce a falsely reassuring relative perfusion image?',
 'Balanced reduction in perfusion across multiple territories',[
 ('A uniformly normal image proves all coronary flow reserve is normal','Relative imaging can miss a diffuse global reduction.'),
 ('Only single-vessel disease can ever cause an imaging limitation','The issue is specifically important with diffuse or multivessel disease.'),
 ('SPECT directly visualizes every coronary lumen','It assesses tracer distribution rather than directly imaging the lumen.')],
 'Relative perfusion needs a reference region',
 '**If all territories are similarly impaired, regional contrast can be reduced.**',
 ['Other findings such as transient dilation or stress functional change can add concern.', 'PET flow quantification or another method may address residual uncertainty in selected cases.'],
 '**Reconcile the test with pretest probability and symptoms.**',
 ['Do not dismiss a high-risk syndrome from one apparently uniform study.', 'Additional evaluation should answer the remaining clinical question.'],
 [['Relative perfusion','Compares territories'],['Balanced ischemia','Can reduce visible regional differences'],['Absolute flow assessment','Can add information']], [ref('2024 ESC Chronic Coronary Syndromes Guideline','https://doi.org/10.1093/eurheartj/ehae177')], 'clinical_scenario')
q('What is a major limitation of coronary CTA in a patient with very extensive coronary calcification?',
 'Calcium blooming can overestimate luminal stenosis and reduce interpretability',[
 ('Calcium makes every lumen easier to measure perfectly','Blooming can obscure the true lumen.'),
 ('CTA becomes a direct measure of every lesion\'s ischemic significance','Anatomy and physiological significance are different questions.'),
 ('A calcium score by itself identifies a precise culprit stenosis','It quantifies burden rather than defining every obstructive lesion.')],
 'An anatomical test has technical constraints',
 '**High-density calcium can appear larger and obscure adjacent lumen.**',
 ['Heart rate, motion, body size and contrast timing also affect quality.', 'A nondiagnostic segment should not be silently treated as normal.'],
 '**Select a complementary test when needed.**',
 ['Functional assessment or invasive angiography may be appropriate according to risk and symptoms.', 'A good-quality CTA can be particularly useful for excluding significant anatomical disease in suitable patients.'],
 [['Heavy calcium','Blooming and stenosis overestimation'],['Motion','Can reduce evaluability'],['Next test','Chosen by the unresolved question']], [S])
q('CMR shows near-transmural LGE in a chronically dysfunctional coronary-territory segment. What does this suggest about recovery after revascularization?',
 'A lower likelihood of meaningful regional contractile recovery than in a segment with little or no scar',[
 ('Guaranteed complete recovery because more scar means more reserve','Extensive replacement scar limits recovery.'),
 ('Proof that no revascularization indication can exist anywhere in the patient','Regional viability is only one component of the overall decision.'),
 ('A characteristic isolated atrial scar pattern','The finding is ventricular and territorial.')],
 'Scar extent influences regional recovery potential',
 '**Greater transmural replacement fibrosis leaves less functioning myocardium to recover.**',
 ['Low-scar dysfunctional tissue has a different potential for improvement.', 'Segmental recovery and patient-level prognosis are not identical endpoints.'],
 '**Integrate anatomy and clinical indications.**',
 ['Angina, left main disease or other territories may still influence treatment.', 'Do not turn one segment\'s LGE into a complete management decision.'],
 [['Little scar','Greater potential for recovery'],['Near-transmural scar','Lower recovery likelihood'],['Revascularization decision','Broader clinical and anatomical assessment']], [C])
q('CMR gives LV stroke volume 110 mL and aortic forward stroke volume 70 mL. There is isolated MR with no other shunt or regurgitant confounder. What is MR regurgitant volume?',
 '40 mL per beat',[
 ('180 mL','Adding the volumes does not calculate regurgitation.'),
 ('70 mL','This is forward flow, not the difference.'),
 ('110 mL','This is total LV stroke volume.')],
 'Separate total ejected volume from forward systemic flow',
 '**MR volume can be estimated as LV total stroke volume minus aortic forward flow under the stated assumptions.**',
 ['110 minus 70 equals 40 mL.', 'Other valve lesions, shunts and phase-contrast errors can invalidate a simple calculation.'],
 '**Check internal consistency and quantify severity integratively.**',
 ['Review chamber contours and flow acquisition.', 'A numerical regurgitant volume is interpreted with fraction, symptoms and ventricular response.'],
 [['Total LV stroke volume','110 mL'],['Aortic forward volume','70 mL'],['Difference','40 mL MR volume']], [V])
q('CMR measures net pulmonary flow 120 mL/beat and net systemic aortic flow 80 mL/beat. What is Qp:Qs?',
 '1.5',[
 ('0.67','This is the inverse ratio.'),
 ('40','This is the absolute flow difference, not the ratio.'),
 ('2.5','This does not follow from the given flows.')],
 'Net great-vessel flows quantify a shunt',
 '**Qp:Qs equals pulmonary divided by systemic flow.**',
 ['120/80 = 1.5.', 'Use net flow and account for valve regurgitation, collateral pathways and measurement quality.'],
 '**A ratio does not establish closure safety.**',
 ['The defect anatomy, chamber effects and pulmonary vascular resistance matter.', 'Catheterization may be required when pulmonary pressure or resistance is uncertain.'],
 [['Pulmonary flow','120 mL/beat'],['Systemic flow','80 mL/beat'],['Ratio','1.5']], [R])
q('An early-phase cardiac CT shows an LAA filling defect that completely opacifies on a suitable delayed scan. What is the likely explanation?',
 'Slow contrast mixing rather than a persistent thrombus',[
 ('A fixed thrombus is proven because any early defect is diagnostic','Slow flow can mimic a clot in the early phase.'),
 ('The delayed scan is irrelevant to appendage assessment','Delayed imaging helps distinguish mixing from persistent material.'),
 ('The finding excludes every future thromboembolic risk','An imaging result at one time does not remove a clinical anticoagulation indication.')],
 'Timing can distinguish a flow artifact from material',
 '**Slow LAA flow can delay contrast filling.**',
 ['A defect that resolves on delayed imaging favors mixing.', 'Persistent or indeterminate findings require appropriate further assessment, often TOE.'],
 '**Use a validated protocol and the clinical context.**',
 ['Image quality and delay duration matter.', 'Do not stop indicated anticoagulation solely because no current thrombus is seen.'],
 [['Early defect resolves','Slow-flow explanation favored'],['Persistent defect','Thrombus assessment needed'],['Clinical risk','Separate from one negative image']], [S], 'clinical_scenario')
q('Routine echo poorly visualizes the LV apex and two adjacent endocardial segments in a patient with suspected apical thrombus. Which step can improve assessment?',
 'Use an appropriate ultrasound-enhancing agent, with CMR if the study remains uncertain',[
 ('Assume an unseen apex is normal','Nonvisualization is not a negative diagnostic result.'),
 ('Repeat only a resting ECG as equivalent thrombus imaging','Electrical recording cannot characterize an apical mass.'),
 ('Use a coronary calcium score to exclude all LV thrombus','That is not the appropriate thrombus test.')],
 'Image quality is part of diagnostic accuracy',
 '**Ultrasound enhancement can improve endocardial border and apical cavity definition.**',
 ['The purpose is to resolve a limitation, not add contrast to every examination.', 'Persistent uncertainty can justify CMR, which has strong thrombus-detection capability.'],
 '**Report what was and was not visualized.**',
 ['A limited negative study should not be presented as definitive exclusion.', 'The result can affect anticoagulation and embolic-risk decisions.'],
 [['Poor apex visualization','Improve acquisition and consider enhancement'],['Persistent uncertainty','Consider CMR'],['Report','State diagnostic limitations']], [ref('AHA 2022 LV Thrombus Scientific Statement','https://doi.org/10.1161/CIR.0000000000001092')], 'clinical_scenario')

if __name__=='__main__':
    finalize('Cardiology',10,'Cardiac Imaging and Hemodynamics','cardiology-imaging-hemodynamics',rows,24)
