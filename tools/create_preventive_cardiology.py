"""Original Preventive Cardiology and Dyslipidemia chapter."""
from qbank_authoring import question,ref,finalize
L=ref('2026 ACC/AHA Multisociety Dyslipidemia Guideline','https://doi.org/10.1161/CIR.0000000000001423')
P=ref('2019 ACC/AHA Primary Prevention Guideline','https://doi.org/10.1016/j.jacc.2019.03.010')
C=ref('2023 AHA/ACC Chronic Coronary Disease Guideline','https://doi.org/10.1016/j.jacc.2023.04.003')
rows=[]
def q(*args,**kwargs):rows.append(question(*args,**kwargs))

q('A patient has a previous MI and peripheral arterial disease. What is the appropriate role of a primary-prevention risk calculator in deciding whether lipid treatment is needed?',
 'It is not needed to establish the indication because the patient already has clinical ASCVD',[
 ('A low calculated primary-prevention score can cancel the secondary-prevention indication','Established disease has already defined a high-risk treatment context.'),
 ('Only age determines whether secondary prevention is appropriate','Disease, expected benefit, tolerance and preferences matter.'),
 ('A normal current LDL excludes any benefit from risk assessment and follow-up','Residual risk and treatment response still need review.')],
 'Primary and secondary prevention start from different premises',
 '**Clinical ASCVD establishes a secondary-prevention pathway.**',
 ['Risk calculators estimate future events in a specified prevention population.', 'They should not be used outside their validated setting to deny established-disease treatment.'],
 '**Assess residual modifiable risk rather than recalculating whether disease exists.**',
 ['Review lipids, smoking, pressure, diabetes, activity and adherence.', 'Treatment intensity is individualized within the secondary-prevention framework.'],
 [['No clinical ASCVD','Primary-prevention risk assessment'],['Prior MI/PAD','Secondary prevention'],['Follow-up','Treat residual risk and monitor response']], [L,C], 'clinical_scenario')
q('A patient after MI tolerates atorvastatin 80 mg daily. What is the foundation of the lipid regimen?',
 'Continue maximally tolerated high-intensity statin therapy and assess the need for additional LDL lowering',[
 ('Stop therapy when one LDL value becomes lower','The benefit depends on sustained treatment rather than a one-time result.'),
 ('Replace the statin routinely with niacin to raise HDL','HDL raising is not an equivalent established strategy.'),
 ('Use supplements instead of medication solely because symptoms are absent','Asymptomatic status does not remove secondary-prevention risk.')],
 'Sustained LDL exposure influences atherosclerotic risk',
 '**A high-intensity or maximally tolerated statin is foundational after ASCVD.**',
 ['Nonstatin treatment may be needed to reach the applicable goal.', 'Lifestyle treatment remains complementary.'],
 '**Review response and tolerability.**',
 ['Check adherence and secondary causes when LDL remains high.', 'Do not equate absence of angina with absence of atherosclerotic risk.'],
 [['Statin','Foundation of LDL lowering'],['Residual LDL above goal','Consider appropriate combination therapy'],['Lifestyle','Continues alongside medication']], [L,C], 'clinical_scenario')
q('Under the 2026 ACC/AHA dyslipidemia guideline, what LDL-C goal applies to a patient with clinical ASCVD at very high risk?',
 'Below 55 mg/dL',[
 ('Below 130 mg/dL','This is not the current very-high-risk secondary-prevention goal.'),
 ('Below 100 mg/dL','This is insufficient as the specified very-high-risk goal.'),
 ('Below 160 mg/dL','This is far above the recommended goal.')],
 'Current secondary-prevention goals reflect residual risk',
 '**The 2026 guideline uses LDL-C below 55 mg/dL for very-high-risk ASCVD.**',
 ['The corresponding non-HDL goal is also relevant.', 'Classification as very high risk depends on events and associated risk conditions.'],
 '**Escalate with treatments supported for the patient\'s context.**',
 ['Use tolerated statin therapy and appropriate nonstatin additions.', 'Specify the guideline year because older US thresholds and current European goals are not identical historical frameworks.'],
 [['Very-high-risk ASCVD','LDL-C goal below 55'],['Therapy','Maximally tolerated foundation plus selected add-on'],['Review','Risk category and achieved levels']], [L])
q('Under the 2026 ACC/AHA framework, which LDL-C goal is generally used for clinical ASCVD that is not classified as very high risk?',
 'Below 70 mg/dL',[
 ('Below 160 mg/dL','That is not an appropriate secondary-prevention goal.'),
 ('Below 130 mg/dL','This is above the specified goal.'),
 ('No goal because only pretreatment LDL matters','Achieved levels and ongoing exposure matter.')],
 'Risk category helps define treatment intensity',
 '**The guideline distinguishes very-high-risk from other clinical ASCVD.**',
 ['The conventional goal for the latter is below 70 mg/dL.', 'Other patient factors can support a more intensive individualized strategy.'],
 '**Use goals to guide a sustained plan.**',
 ['Review adherence, tolerance and the need for combination therapy.', 'Do not confuse a treatment goal with the diagnostic threshold for hypercholesterolemia.'],
 [['ASCVD not very high risk','Generally LDL-C below 70'],['Very-high-risk ASCVD','Below 55'],['Treatment review','Response and tolerability']], [L])
q('A 38-year-old has repeated untreated LDL-C 224 mg/dL after secondary causes are assessed. What is the appropriate principle?',
 'Treat severe hypercholesterolemia and assess for familial disease without relying on a low short-term risk score',[
 ('Defer treatment solely because age lowers the 10-year estimate','Lifetime exposure can be substantial despite low short-term risk.'),
 ('Require a previous MI before any lipid treatment','Prevention should not wait for an event.'),
 ('Assume that normal triglycerides exclude inherited LDL disease','FH commonly presents with predominantly LDL elevation.')],
 'Severe LDL elevation carries cumulative lifetime risk',
 '**An LDL-C at least 190 mg/dL prompts a severe-hypercholesterolemia pathway.**',
 ['Evaluate hypothyroidism, nephrotic disease and other secondary contributors.', 'Family history and physical findings can support FH assessment.'],
 '**Act before clinical atherosclerosis develops.**',
 ['Use appropriate intensive LDL lowering and family evaluation.', 'A short-term calculator does not fully capture a young person\'s cumulative exposure.'],
 [['Marked LDL elevation','Important even at young age'],['Secondary causes','Assess before assigning etiology'],['Lifetime exposure','Key prevention rationale']], [L], 'clinical_scenario')
q('Which finding most strongly supports heterozygous familial hypercholesterolemia in a patient with markedly elevated untreated LDL-C?',
 'Tendon xanthomas with a family history of premature ASCVD',[
 ('An isolated low HDL level after an acute illness','That is nonspecific and does not define FH.'),
 ('A single nonfasting triglyceride elevation after alcohol use','That points to a different lipid disturbance.'),
 ('Normal LDL in all untreated measurements','That does not fit the usual severe LDL phenotype.')],
 'FH assessment combines lipid, physical and familial evidence',
 '**Tendon xanthomas are a strong clue in the appropriate LDL phenotype.**',
 ['Premature family coronary disease adds support.', 'Absence of xanthomas does not exclude FH.'],
 '**Consider genetic confirmation and family screening.**',
 ['A negative panel does not exclude every clinical FH phenotype.', 'Treat the LDL burden while the etiological evaluation proceeds.'],
 [['Tendon xanthoma','Strong physical clue'],['Premature family ASCVD','Supports inherited risk'],['No xanthoma','Does not rule out FH']], [L])
q('A pathogenic LDLR variant confirms FH in a patient. What is an appropriate next preventive action?',
 'Offer cascade testing and lipid assessment to relatives with genetic counseling',[
 ('Wait until relatives have angina before assessing them','Early identification can prevent cumulative LDL exposure.'),
 ('Test only unrelated household members','Biological relatives are the relevant inherited-risk group.'),
 ('Assume every relative is affected without testing or clinical assessment','Inheritance creates risk, not certainty for each person.')],
 'An FH diagnosis can prevent events beyond the index patient',
 '**Cascade evaluation identifies relatives who may benefit from early treatment.**',
 ['Use the known familial variant when appropriate.', 'Lipid screening remains useful within the family assessment.'],
 '**Counsel clearly about inheritance and uncertainty.**',
 ['Differentiate a pathogenic variant from a VUS.', 'Age-appropriate management and follow-up are needed for affected younger relatives.'],
 [['Index diagnosis','Triggers family opportunity'],['Cascade testing','Uses established familial finding'],['Prevention','Earlier reduction in lifetime LDL exposure']], [L], 'clinical_scenario')
q('What does the 2026 ACC/AHA guideline recommend about Lp(a) measurement in adults?',
 'Measure it at least once in adult life to refine inherited ASCVD risk',[
 ('Never measure it unless triglycerides exceed 1000','Lp(a) is a separate risk marker.'),
 ('Measure it only as a substitute for every LDL test','It does not replace the standard lipid profile.'),
 ('A high Lp(a) proves that conventional risk factors no longer matter','Other modifiable risk remains important.')],
 'Lp(a) adds information not captured by routine LDL alone',
 '**Lp(a) is largely genetically determined and can refine lifetime risk.**',
 ['Use the reported units carefully; mass and molar units are not interchangeable through one universal conversion.', 'A high result supports more careful management of overall atherosclerotic risk.'],
 '**Avoid promising an unverified treatment effect.**',
 ['Current care includes aggressive control of modifiable risks.', 'Specific Lp(a)-lowering therapies and outcome evidence must be assessed using current approvals and trial results.'],
 [['Lp(a)','Inherited risk refinement'],['LDL/non-HDL','Still central treatment measures'],['High result','Intensify comprehensive prevention as appropriate']], [L])
q('A patient with diabetes and high triglycerides reaches the LDL-C goal but may have residual atherogenic particle burden. Which measure can add useful information?',
 'Apolipoprotein B',[
 ('Troponin as a direct count of atherogenic particles','Troponin measures myocardial injury.'),
 ('BNP as the definitive lipoprotein particle measure','BNP relates to cardiac wall stress.'),
 ('INR as a lipid residual-risk marker','INR assesses a coagulation pathway, not particle burden.')],
 'Cholesterol content and particle number can be discordant',
 '**ApoB reflects the number of atherogenic lipoprotein particles.**',
 ['Discordance is particularly relevant with high triglycerides and cardiometabolic disease.', 'Non-HDL cholesterol also captures cholesterol carried by multiple atherogenic particles.'],
 '**Use the result to refine a clinical question.**',
 ['The 2026 framework supports selected apoB assessment for residual or discordant risk.', 'It complements rather than erases LDL and other risk information.'],
 [['LDL-C','Cholesterol within LDL'],['Non-HDL-C','Cholesterol in atherogenic particles'],['ApoB','Atherogenic particle burden']], [L], 'clinical_scenario')
q('A patient with diabetes asks whether CAC score 0 means statin treatment is automatically unnecessary. What is the best response?',
 'CAC 0 does not override all treatment indications or high-risk exceptions',[
 ('CAC 0 guarantees no coronary plaque and no future events','Noncalcified plaque and future risk remain possible.'),
 ('Every person with CAC 0 must stop lipid medication','Risk and established indications still matter.'),
 ('CAC directly measures all LDL exposure since birth','It measures calcified plaque burden, not cumulative lipids directly.')],
 'The power of zero has defined limits',
 '**CAC can refine uncertain primary-prevention decisions but is not an absolute veto on treatment.**',
 ['Diabetes, severe LDL elevation, smoking and strong family risk can change interpretation.', 'Clinical ASCVD is a separate secondary-prevention context.'],
 '**Use CAC only when the result can change a suitable decision.**',
 ['Discuss the patient\'s baseline risk and the limitations.', 'Do not order a scan simply to justify stopping clearly indicated treatment.'],
 [['Selected uncertain risk','CAC may reclassify'],['Strong treatment indication','Zero does not automatically negate it'],['CAC 0','Low calcified burden, not zero lifetime risk']], [L], 'clinical_scenario')
q('A primary-prevention patient has CAC 240 Agatston units after an uncertain treatment discussion. What does this finding generally support?',
 'Initiating or intensifying appropriate statin-based LDL lowering',[
 ('Deferring all prevention because there is no angina','Subclinical plaque can be important before symptoms.'),
 ('Immediate PCI solely from the calcium score','CAC does not identify a specific flow-limiting lesion for intervention.'),
 ('A diagnosis of acute MI from calcium alone','Calcium burden does not establish acute myocardial injury.')],
 'CAC identifies established subclinical atherosclerotic burden',
 '**A score above 100 materially strengthens the case for lipid-lowering prevention.**',
 ['The 2026 framework uses burden to guide intensity.', 'Age, percentile and other risk factors remain relevant.'],
 '**Do not confuse risk imaging with an ischemia procedure indication.**',
 ['Treat risk and investigate symptoms separately if present.', 'Lifestyle and blood pressure care remain necessary.'],
 [['CAC at least 100','Supports statin treatment'],['CAC alone','Not a PCI indication'],['Prevention','Addresses future event risk']], [L], 'clinical_scenario')
q('A patient reports muscle aches on one statin with normal CK and no objective weakness. What is an appropriate next strategy?',
 'Assess alternative causes and interactions, then consider a supervised rechallenge or a different tolerated statin regimen',[
 ('Declare permanent intolerance to every statin from one exposure','One episode does not establish inability to tolerate all regimens.'),
 ('Ignore symptoms because normal CK proves they are imaginary','Symptoms deserve assessment even when CK is normal.'),
 ('Stop all lipid prevention permanently','Alternative dosing and nonstatin therapy can preserve prevention.')],
 'SAMS assessment should preserve effective prevention where possible',
 '**Evaluate timing, dose, thyroid disease, exercise and interacting medication.**',
 ['Symptoms can be pharmacological, unrelated or influenced by expectation.', 'Normal CK does not invalidate symptoms but makes severe muscle necrosis less likely.'],
 '**Find a tolerable effective regimen.**',
 ['A lower dose, different statin or selected dosing schedule can be considered.', 'Add nonstatin treatment according to residual LDL and risk.'],
 [['Initial symptoms','Assess rather than dismiss'],['Rechallenge','Can clarify tolerance'],['Persistent limitation','Use a suitable combination or alternative']], [L], 'clinical_scenario')

# Residual lipid risk and comprehensive prevention complete the subject.
q('A patient has new LDL elevation, fatigue, constipation and muscle symptoms during lipid therapy. Which reversible condition should be assessed?',
 'Hypothyroidism',[
 ('FH proven solely by the new LDL value','Secondary causes should be evaluated, particularly with a compatible systemic syndrome.'),
 ('A primary platelet disorder as the usual cause of LDL elevation','That does not fit the thyroid-like symptom cluster.'),
 ('A normal CK as exclusion of all endocrine disease','CK does not rule out hypothyroidism.')],
 'Secondary disease can worsen both lipids and treatment tolerance',
 '**Hypothyroidism can raise LDL and contribute to myalgia.**',
 ['Review thyroid function along with medication and other secondary causes.', 'Nephrotic disease, cholestasis and other disorders can also alter lipids.'],
 '**Treat the cause while reassessing the preventive regimen.**',
 ['Do not label a sudden change as inherited disease without context.', 'Repeat the lipid and symptom assessment after appropriate treatment.'],
 [['Thyroid symptoms plus LDL rise','Check thyroid function'],['Secondary cause found','Treat and reassess'],['Residual ASCVD risk','Continue appropriate prevention']], [L], 'clinical_scenario')
q('A patient has persistent proximal weakness and markedly elevated CK despite stopping a statin. Anti-HMGCR antibodies are positive. Which diagnosis is most likely?',
 'Immune-mediated necrotizing myopathy',[
 ('Simple self-limited statin myalgia as the complete explanation','Persistent objective weakness and high CK after withdrawal suggest a different process.'),
 ('A nocebo effect established by all muscle symptoms','The objective biochemical and antibody findings require immune-myopathy assessment.'),
 ('An isolated benign LDL fluctuation','That does not explain muscle necrosis findings.')],
 'Persistent weakness after drug withdrawal is a warning',
 '**Anti-HMGCR-associated disease can continue after the initiating statin is removed.**',
 ['Specialist neurological or rheumatological assessment is needed.', 'Biopsy and other evaluation may help define disease and alternatives.'],
 '**Do not manage this as an ordinary rechallenge case.**',
 ['Immunotherapy may be required according to severity.', 'Plan alternative lipid reduction around the patient\'s cardiovascular risk.'],
 [['Routine myalgia','Often improves after adjustment or withdrawal'],['Persistent high CK and weakness','Consider immune myopathy'],['Anti-HMGCR','Supports the specific immune phenotype']], [L], 'clinical_scenario')
q('A patient has fasting triglycerides 1450 mg/dL. Which immediate preventive priority accompanies ASCVD risk management?',
 'Reduce severe triglyceride elevation to lower pancreatitis risk',[
 ('Focus only on raising HDL and ignore the triglyceride level','Severe elevation has an acute pancreatitis concern.'),
 ('Treat the value as equivalent to a mildly high LDL','The short-term risk and dietary approach differ.'),
 ('Begin unrestricted alcohol intake to improve HDL','Alcohol can worsen triglycerides and pancreatitis risk.')],
 'Severe hypertriglyceridemia creates a second prevention target',
 '**At very high levels, pancreatitis risk becomes clinically important.**',
 ['Use an appropriate very-low-fat nutritional strategy and address secondary causes.', 'Fibrate or prescription triglyceride-lowering therapy may be indicated according to the full assessment.'],
 '**Treat the metabolic driver as well as the number.**',
 ['Assess uncontrolled diabetes, alcohol, drugs and inherited susceptibility.', 'Abdominal pain or vomiting requires evaluation for active pancreatitis.'],
 [['Very high triglycerides','Pancreatitis prevention'],['ASCVD risk','Still assess and treat'],['Secondary contributors','Must be corrected']], [L], 'clinical_scenario')
q('Which change can substantially improve secondary hypertriglyceridemia?',
 'Control poorly controlled diabetes and stop excess alcohol exposure',[
 ('Treat only an incidental normal LDL value','That does not address the triglyceride drivers.'),
 ('Increase refined carbohydrate and alcohol intake','Those exposures can worsen triglycerides.'),
 ('Ignore new medications because they cannot affect lipids','Several drugs can contribute.')],
 'Triglycerides are sensitive to metabolic and exposure changes',
 '**Glycemic dysregulation and alcohol are common reversible contributors.**',
 ['Review weight, diet, kidney disease, thyroid function and medications.', 'A genetic tendency can coexist with secondary triggers.'],
 '**Use a staged response assessment.**',
 ['Severe elevations may need medication and urgent dietary action at the same time.', 'Repeat fasting measurements when clinically appropriate rather than assuming one value defines the lifetime phenotype.'],
 [['Diabetes/alcohol','Important reversible drivers'],['Genetic predisposition','May amplify the response'],['Management','Cause correction plus severity-based therapy']], [L])
q('A laboratory uses the traditional Friedewald equation when triglycerides are 620 mg/dL. Which interpretation is appropriate?',
 'The calculated LDL-C is unreliable; use a suitable alternative assessment',[
 ('The traditional equation is equally accurate at every triglyceride level','Its assumptions fail with substantial triglyceride elevation.'),
 ('A low calculated LDL proves low atherogenic particle burden','A calculation artifact can falsely reassure.'),
 ('Triglycerides alone determine every LDL treatment decision','Non-HDL, apoB, a validated alternative or direct measurement can add information.')],
 'A calculated result depends on its assumptions',
 '**Traditional Friedewald LDL is not valid at triglycerides at least 400 mg/dL.**',
 ['Modern equations have different validated ranges and should not be conflated with the traditional method.', 'Check which method the laboratory used.'],
 '**Use an appropriate measure of residual risk.**',
 ['Non-HDL cholesterol and apoB can be helpful in high-triglyceride states.', 'Address the severe triglyceride elevation as well.'],
 [['Traditional Friedewald','Unreliable at high TG'],['Modern alternative/direct test','Method-specific validation'],['Non-HDL/apoB','Useful complementary measures']], [L])
q('A statin-treated patient has low HDL-C but otherwise appropriate LDL management. Why is niacin not routinely added solely to raise HDL?',
 'Raising the HDL number with niacin has not established the expected incremental cardiovascular benefit and adds adverse effects',[
 ('HDL concentration is a validated treatment target for every drug regardless of outcomes','A biomarker association does not guarantee benefit from pharmacologically changing it.'),
 ('Niacin has no metabolic or tolerability adverse effects','Flushing, glycemic, hepatic and other effects can matter.'),
 ('A low HDL automatically means the statin should be stopped','LDL-focused treatment remains appropriate when indicated.')],
 'Treat outcomes rather than an attractive surrogate',
 '**An inverse association between HDL and risk does not prove that every HDL-raising intervention reduces events.**',
 ['Major add-on trials did not establish a routine event benefit from niacin on contemporary statin treatment.', 'Adverse effects and treatment burden remain relevant.'],
 '**Address the broader metabolic risk profile.**',
 ['Exercise, smoking cessation, weight and diabetes care can improve health without chasing an HDL target.', 'Continue evidence-supported LDL lowering.'],
 [['Low HDL','Risk marker'],['Niacin add-on','No routine incremental event benefit'],['Prevention','Evidence-supported comprehensive care']], [L])
q('Which patient most closely resembles the population in whom icosapent ethyl demonstrated cardiovascular outcome benefit?',
 'A high-risk statin-treated patient with persistent moderate triglyceride elevation',[
 ('Any healthy young person taking an arbitrary mixed fish-oil supplement','The formulation, dose and risk population are not equivalent.'),
 ('A patient stopping all statins to use dietary fish oil alone','The relevant evidence was not a statin-replacement strategy.'),
 ('Every patient with isolated low HDL and normal triglycerides','That is not the defining trial population.')],
 'A positive trial has a defined intervention and population',
 '**REDUCE-IT studied purified EPA in selected high-risk patients on statin therapy.**',
 ['The result cannot be generalized to all omega-3 products.', 'Eligibility includes the risk and lipid context.'],
 '**Discuss net benefit and safety.**',
 ['Review AF history, bleeding risk and concurrent antithrombotics.', 'Continue diet, statin treatment and management of secondary triglyceride contributors.'],
 [['Studied setting','High risk, statin treated, elevated TG'],['Product','Specific purified EPA regimen'],['Not equivalent','All supplements or statin withdrawal']], [L,ref('REDUCE-IT: Cardiovascular Risk Reduction with Icosapent Ethyl','https://doi.org/10.1056/NEJMoa1812792')])
q('A 76-year-old without clinical ASCVD asks to start aspirin solely for primary prevention. Which recommendation is most appropriate?',
 'Do not start aspirin routinely; bleeding risk generally outweighs routine primary-prevention benefit in this age group',[
 ('Start it in every adult above 70 because age removes bleeding concern','Age increases rather than removes bleeding risk.'),
 ('Use aspirin as an equivalent substitute for indicated lipid treatment','The mechanisms and benefit-risk profiles differ.'),
 ('Apply this advice to automatically stop aspirin after a recent coronary stent','Secondary prevention and recent PCI are different contexts.')],
 'Aspirin primary prevention is selective',
 '**Routine primary-prevention aspirin is not recommended above age 70 in the ACC/AHA framework.**',
 ['Bleeding history, CKD and interacting medication further affect risk.', 'This does not negate established secondary-prevention indications.'],
 '**Prioritize interventions with a clearer net benefit.**',
 ['Treat pressure, lipids, smoking and physical inactivity.', 'Review an existing prescription in its actual clinical context before changing it.'],
 [['Older primary prevention','No routine aspirin'],['Established ASCVD/PCI','Different indication'],['Risk reduction','Comprehensive evidence-based care']], [P], 'clinical_scenario')
q('A smoker with coronary disease is ready to quit. Which approach offers more effective support than advice alone?',
 'Behavioral support plus an appropriate evidence-based cessation medication',[
 ('Delay help until another coronary event demonstrates motivation','Treatment should be offered now.'),
 ('Assume nicotine dependence is corrected by one warning','Dependence often requires structured repeated support.'),
 ('Recommend continued smoking if it helps control weight','Smoking remains a major cardiovascular hazard.')],
 'Treat tobacco dependence as a modifiable disease',
 '**Counseling and pharmacotherapy can improve cessation success.**',
 ['Varenicline, nicotine replacement or bupropion may be appropriate depending on the patient.', 'Review contraindications, preferences and previous attempts.'],
 '**Arrange follow-up rather than a one-time instruction.**',
 ['Plan for cravings, relapse and household exposure.', 'Weight concerns can be addressed while preserving the priority of cessation.'],
 [['Behavioral support','Builds skills and follow-up'],['Medication','Addresses dependence when suitable'],['Relapse','Opportunity to adjust treatment']], [P,C], 'clinical_scenario')
q('Which dietary substitution is most consistent with cardiovascular risk reduction?',
 'Replace saturated fats with unsaturated fats within a minimally processed, plant-rich dietary pattern',[
 ('Replace saturated fat predominantly with refined sugars','That is not an equivalent healthy substitution.'),
 ('Add trans fats to raise the energy density of every meal','Industrial trans fats worsen cardiovascular risk.'),
 ('Use supplements to eliminate any need to consider dietary quality','Supplements do not replace an overall healthy pattern.')],
 'The replacement nutrient matters',
 '**A lower saturated-fat intake is most useful when the replacement improves dietary quality.**',
 ['Vegetables, whole grains, legumes, nuts and appropriate unsaturated oils support a heart-healthy pattern.', 'Sodium, energy intake and glycemic context also matter.'],
 '**Adapt the pattern to the person.**',
 ['Culture, affordability, kidney disease and nutritional status influence practical choices.', 'Avoid reducing advice to a single nutrient while ignoring the overall pattern.'],
 [['Favorable replacement','Unsaturated fats and high-quality foods'],['Poor replacement','Refined carbohydrates or trans fats'],['Plan','Sustainable individualized dietary pattern']], [P,C])
q('For a stable adult able to exercise, which weekly activity target is consistent with standard cardiovascular prevention recommendations?',
 'At least 150 minutes of moderate-intensity aerobic activity or an equivalent vigorous-intensity amount',[
 ('Ten minutes of sitting quietly as an equivalent aerobic dose','This does not provide the recommended activity exposure.'),
 ('Maximal exertion every day regardless of symptoms','Intensity should be safe and individualized.'),
 ('Complete inactivity once a statin is prescribed','Medication does not replace activity benefits.')],
 'Regular activity reduces risk and improves function',
 '**The standard target is at least 150 minutes moderate or 75 minutes vigorous activity weekly, with appropriate equivalents.**',
 ['Resistance work and reduced sedentary time add value.', 'Any increase from inactivity can help when the full target is not yet achievable.'],
 '**Tailor activity to disease and capacity.**',
 ['Unstable symptoms require assessment before progression.', 'Rehabilitation can provide a structured route after a cardiovascular event.'],
 [['Moderate aerobic activity','At least 150 min/week'],['Vigorous activity','At least 75 min/week when suitable'],['Starting from inactivity','Progress gradually']], [P,C])
q('What did SELECT demonstrate in adults with established cardiovascular disease and overweight or obesity without diabetes?',
 'Weekly semaglutide 2.4 mg reduced major adverse cardiovascular events compared with placebo',[
 ('Benefit required a pre-existing diabetes diagnosis','The trial specifically studied people without diabetes.'),
 ('It proved identical cardiovascular benefit for every weight-loss supplement','The evidence applies to a defined drug, dose and population.'),
 ('It replaced the need for all other secondary-prevention treatment','The intervention was added to standard care.')],
 'Obesity treatment can have disease-outcome evidence',
 '**SELECT extended cardiovascular outcome benefit to a selected nondiabetic secondary-prevention population.**',
 ['The primary composite included cardiovascular death, nonfatal MI and nonfatal stroke.', 'The result should not be generalized to all obesity drugs or all risk groups.'],
 '**Use treatment within comprehensive prevention.**',
 ['Assess eligibility, contraindications, tolerability and nutritional/functional goals.', 'Continue appropriate lipid, pressure, smoking and antithrombotic care.'],
 [['Population','Established CVD plus overweight/obesity without diabetes'],['Intervention','Semaglutide 2.4 mg weekly'],['Finding','Reduced MACE versus placebo']], [ref('SELECT: Semaglutide and Cardiovascular Outcomes in Obesity without Diabetes','https://doi.org/10.1056/NEJMoa2307563')])

if __name__=='__main__':
    finalize('Cardiology',11,'Preventive Cardiology and Dyslipidemia','cardiology-preventive',rows,24)
