"""Original Acute and Chronic Pancreatitis questions; directly authored."""
from qbank_authoring import question, ref, finalize
AP=ref('ACG 2024 Acute Pancreatitis Guideline: official highlights','https://webfiles.gi.org/links/journals/AJG-Clinical-Guidelines-Highlights-Acute-Pancreatitis-2024-FINAL.pdf')
IAP=ref('International Association of Pancreatology Revised Guidelines 2025','https://doi.org/10.1016/j.pan.2025.04.020')
NEC=ref('AGA Clinical Practice Update: Management of Pancreatic Necrosis','https://gastro.org/clinical-guidance/management-of-pancreatic-necrosis/')
CP=ref('ACG 2020 Chronic Pancreatitis Guideline','https://doi.org/10.14309/ajg.0000000000000535')
EPI=ref('AGA 2023 Exocrine Pancreatic Insufficiency Clinical Practice Update','https://doi.org/10.1053/j.gastro.2023.07.007')
AIP=ref('International Consensus Diagnostic Criteria for Autoimmune Pancreatitis','https://pubmed.ncbi.nlm.nih.gov/21412117/')
NICE=ref('NICE NG104: Pancreatitis recommendations','https://www.nice.org.uk/guidance/ng104/chapter/recommendations')
rows=[]
def q(*args,**kwargs): rows.append(question(*args,**kwargs))

q('Which combination establishes acute pancreatitis without requiring diagnostic CT?',
 'Characteristic acute epigastric pain and serum lipase more than three times the upper reference limit',[
 ('Isolated lipase elevation of 1.5 times the upper limit without symptoms','A small isolated elevation is nonspecific and does not meet the biochemical threshold.'),
 ('Epigastric discomfort with normal enzymes and normal pancreatic imaging','Only a compatible symptom is present; another criterion is needed.'),
 ('Gallstones on ultrasound and mildly elevated bilirubin without pancreatic symptoms','These suggest biliary disease but do not themselves establish pancreatitis.')],
 'Diagnosis rests on two of three complementary findings',
 '**Compatible pain, pancreatic enzymes above three times normal, and characteristic imaging are the three diagnostic domains.**',
 ['Two domains are generally sufficient; all three are not required.', 'Delayed presentation and hypertriglyceridemia can complicate enzyme interpretation.'],
 '**Order imaging to answer a remaining clinical question.**',
 ['An uncertain diagnosis or an atypical course can justify cross-sectional imaging.', 'Enzyme height alone does not grade organ failure or necrosis.'],
 [['Typical pain plus diagnostic enzymes','Usually sufficient'],['Equivocal biochemical presentation','Imaging may establish the second criterion'],['Very high lipase','Not a severity category']], [AP,IAP])
q('A patient with definite acute pancreatitis is stable and improving during the first 24 hours. What is the best approach to contrast-enhanced CT?',
 'Reserve CT for diagnostic uncertainty or failure to improve rather than obtaining it routinely now',[
 ('Obtain CT immediately to assign a definitive necrosis burden in every case','Very early CT may underestimate evolving necrosis and adds little in an improving definite case.'),
 ('Schedule daily CT until the lipase normalizes','Serial enzyme normalization is not an indication for repeated radiation and contrast.'),
 ('Exclude CT permanently because pancreatitis is already diagnosed','New deterioration or suspected complications can make later CT important.')],
 'Timing determines the value of anatomical staging',
 '**Routine admission CT is unnecessary in an uncomplicated, clearly diagnosed presentation.**',
 ['Necrosis evolves over time and may be poorly delineated very early.', 'Failure to improve over roughly 48–72 hours or a new complication changes the imaging decision.'],
 '**Reassess the patient rather than following a fixed scanning schedule.**',
 ['Consider renal function and contrast suitability.', 'Suspected alternative emergencies may require immediate imaging despite early timing.'],
 [['Clear and improving disease','No routine early CT'],['Uncertain diagnosis','Targeted imaging'],['Persistent or worsening illness','Assess complications']], [AP], 'clinical_scenario')
q('A patient with acute pancreatitis has mild hypovolemia and a history of heart failure. Which fluid strategy is most appropriate?',
 'Use lactated Ringer solution with individualized, frequently reassessed resuscitation and close monitoring for overload',[
 ('Give a fixed aggressive bolus and high infusion rate regardless of examination','Unselected aggressive hydration increases overload risk and is particularly hazardous with limited cardiac reserve.'),
 ('Avoid all intravenous fluid until pancreatic enzymes fall','Untreated hypovolemia can worsen perfusion and kidney injury.'),
 ('Use hydroxyethyl starch as the preferred routine resuscitation fluid','Crystalloid is preferred; starch is not routine pancreatitis resuscitation.')],
 'Restore perfusion without creating a second organ problem',
 '**Early crystalloid resuscitation should respond to volume status, not a universal large-volume target.**',
 ['Follow hemodynamics, urine output, renal indices and signs of congestion.', 'Heart failure and renal impairment require additional caution and often a lower tolerance for empiric volume.'],
 '**Reassess within hours and adjust the rate.**',
 ['A falling perfusion deficit is useful; new hypoxemia or edema demands reassessment.', 'The moderate-fluid evidence does not mean undertreating shock.'],
 [['Hypovolemia','Careful correction'],['Adequate perfusion','Avoid unnecessary escalation'],['Cardiac/renal limitation','Closer monitoring and individualization']], [AP,IAP], 'clinical_scenario')
q('In mild acute pancreatitis, pain and nausea are improving and the patient is hungry. Lipase remains elevated. What feeding plan is appropriate?',
 'Begin oral low-fat solid food as tolerated without waiting for lipase normalization',[
 ('Keep the patient fasting until lipase is normal on two tests','Enzyme normalization is not required to restart tolerated feeding.'),
 ('Start parenteral nutrition because oral intake stimulates the pancreas','The enteral route is preferred when feasible.'),
 ('Require several days of clear liquids before any solid food','A mandatory liquid-to-solid ladder is unnecessary in suitable mild disease.')],
 'Clinical tolerance guides early feeding',
 '**Early oral intake is appropriate in mild disease when vomiting and ileus do not prevent it.**',
 ['A low-fat solid diet can be the initial diet.', 'If oral feeding is not possible in more severe disease, enteral tube nutrition is usually favored over parenteral nutrition.'],
 '**Do not use persistent enzyme elevation as a fasting order.**',
 ['Nutrition limits catabolism and supports the intestinal barrier.', 'Recurrent intolerance requires reassessment of disease and feeding route.'],
 [['Mild and tolerating food','Early oral diet'],['Unable to eat but gut usable','Enteral tube feeding'],['Enteral route impossible/inadequate','Consider parenteral supplementation']], [AP,IAP], 'clinical_scenario')
q('CT shows pancreatic necrosis in a stable patient without fever, bacteremia, gas in the collection or another infection. What is the antibiotic recommendation?',
 'Do not prescribe antibiotics solely to prevent infection of sterile necrosis',[
 ('Use a carbapenem in every patient with necrosis','Necrosis alone is not evidence of bacterial infection.'),
 ('Give routine antifungal prophylaxis with broad-spectrum antibiotics','Routine prophylactic antifungal treatment is not recommended.'),
 ('Treat all early leukocytosis as proof of infected necrosis','Sterile inflammation can produce leukocytosis and fever.')],
 'Separate sterile inflammatory injury from infection',
 '**Prophylactic antimicrobials do not replace supportive care for sterile necrosis.**',
 ['Search for a real infection when the clinical course changes.', 'Pneumonia, cholangitis, urinary infection or catheter infection still warrant treatment on their own merits.'],
 '**Use antimicrobials when infection is demonstrated or strongly suspected.**',
 ['Gas, bacteremia, sepsis or clinical deterioration can support infected necrosis.', 'Choice should account for penetration, cultures, resistance and organ function.'],
 [['Sterile necrosis','No routine prophylaxis'],['Strongly suspected infection','Therapeutic antibiotics'],['Extra-pancreatic infection','Treat the identified source']], [AP,NEC])
q('Three weeks after necrotizing pancreatitis, a patient develops sepsis and new gas within a necrotic collection without a prior intervention. Which interpretation is best?',
 'Infected pancreatic necrosis is strongly suspected and should prompt antibiotics and multidisciplinary source-control planning',[
 ('Gas is a routine feature of every sterile necrotic collection','Gas is an important infection clue, although fistulation is another possible cause.'),
 ('Treatment must wait for a positive fine-needle aspiration in every case','Strong clinical and imaging evidence can support treatment without routine FNA.'),
 ('A normal serum amylase would exclude infected necrosis','Enzyme concentration does not exclude a late infectious complication.')],
 'The late course can be more informative than enzyme levels',
 '**Sepsis plus gas in an uninstrumented necrotic collection makes infection a major concern.**',
 ['Blood cultures and evaluation for competing infection sources are useful.', 'Routine diagnostic FNA is unnecessary when the overall evidence is convincing.'],
 '**Timing and method of intervention depend on stability and anatomy.**',
 ['A stable responder may benefit from delayed intervention.', 'Uncontrolled sepsis can require earlier drainage; waiting four weeks is not an absolute rule.'],
 [['Gas with sepsis','Strong infection signal'],['Early isolated inflammatory markers','Can be sterile'],['Clinical instability despite treatment','Reconsider urgent drainage']], [NEC,IAP], 'clinical_scenario')
q('A patient with infected necrosis improves on antibiotics and organ support at day 18. There is no obstruction or other urgent indication. What intervention timing is generally preferred?',
 'Delay debridement toward four weeks when clinically tolerated so the collection can organize',[
 ('Perform immediate open necrosectomy merely because infection was diagnosed','Early open debridement can impose avoidable morbidity in a stabilizing patient.'),
 ('Avoid any future intervention even if sepsis recurs','Clinical failure or symptomatic necrosis can require source control.'),
 ('Use the serum lipase concentration alone to determine debridement timing','Lipase is not a timing marker for maturation or source-control need.')],
 'Organization makes intervention more controlled',
 '**A mature boundary helps separate viable tissue from necrosis and facilitates less invasive access.**',
 ['Delay is preferred only while the patient can tolerate it.', 'Earlier drainage may be needed for persistent sepsis or progressive organ failure.'],
 '**Review the course with endoscopy, radiology and surgery together.**',
 ['The best route depends on location, extension and expertise.', 'Debridement and initial drainage are distinct decisions.'],
 [['Stable response','Prefer delayed intervention'],['Failure despite medical treatment','Earlier drainage may be necessary'],['Mature accessible collection','More intervention options']], [NEC,IAP], 'clinical_scenario')
q('What is the principle of a step-up approach to infected pancreatic necrosis?',
 'Begin with appropriate drainage and escalate to minimally invasive necrosectomy if response is inadequate',[
 ('Begin with open necrosectomy in every patient, then add drainage','That reverses the less invasive escalation principle.'),
 ('Perform endoscopic necrosectomy before evaluating collection anatomy','Access and safety must be established before selecting an intervention.'),
 ('Continue antibiotics indefinitely regardless of uncontrolled sepsis','Failure of medical treatment requires source-control reassessment.')],
 'Escalate only as much as needed for source control',
 '**Drainage alone can be sufficient for some patients.**',
 ['Endoscopic or percutaneous access is chosen according to location and condition.', 'Residual infected debris and persistent illness can justify further debridement.'],
 '**Plan access with the whole disease distribution in mind.**',
 ['Deep extension may require complementary routes.', 'Expertise and patient stability matter as much as the label of the procedure.'],
 [['First invasive step','Drainage when appropriate'],['Persistent infected debris','Escalate debridement'],['Complex anatomy','Combined multidisciplinary strategy']], [NEC,IAP])
q('Six weeks after necrotizing pancreatitis, MRI shows an encapsulated collection containing fluid and substantial nonliquid debris. What is the correct term?',
 'Walled-off necrosis',[
 ('Pancreatic pseudocyst','A true pseudocyst is predominantly fluid without necrotic debris and usually follows interstitial pancreatitis.'),
 ('Acute peripancreatic fluid collection','This is an early, non-encapsulated fluid collection associated with interstitial pancreatitis.'),
 ('Acute necrotic collection','This describes necrotic material before a mature encapsulating wall has developed.')],
 'Classify by contents, wall and time',
 '**Necrotic debris distinguishes walled-off necrosis from a pseudocyst.**',
 ['A mature wall usually develops after about four weeks.', 'MRI or EUS can help define debris when CT is less clear.'],
 '**The distinction affects drainage planning.**',
 ['A debris-rich collection may need more than simple fluid drainage.', 'Collection size alone does not determine the need for intervention.'],
 [['Pseudocyst','Mature wall, fluid predominates'],['Walled-off necrosis','Mature wall, necrotic contents'],['Acute necrotic collection','Immature necrotic collection']], [IAP,NEC], 'clinical_scenario')
q('Acute biliary pancreatitis is complicated by fever, jaundice, hypotension and evidence of common bile duct obstruction. What is the appropriate biliary intervention?',
 'Urgent ERCP for drainage of associated cholangitis, alongside resuscitation and antibiotics',[
 ('Delay all biliary drainage until a pancreatic collection matures','The four-week necrosis principle does not apply to infected obstructed bile ducts.'),
 ('Perform elective MRCP weeks later as the only action','Noninvasive imaging should not delay necessary drainage in convincing cholangitis.'),
 ('Perform cholecystectomy first as the sole method of draining the duct','Gallbladder removal does not reliably relieve the infected duct obstruction.')],
 'Treat the concurrent source of biliary sepsis',
 '**Cholangitis is a specific indication for urgent ERCP in biliary pancreatitis.**',
 ['Drainage is generally sought within 24 hours, adjusted to severity and immediate stabilization.', 'Antibiotics and hemodynamic support accompany source control.'],
 '**Separate duct drainage from prevention of future gallstone events.**',
 ['Cholecystectomy planning follows disease severity and recovery.', 'ERCP is not automatically indicated in every gallstone-related episode.'],
 [['Pancreatitis plus cholangitis','Urgent duct drainage'],['No cholangitis or ongoing obstruction','Supportive pathway, selective duct assessment'],['Later recurrence prevention','Gallbladder management']], [AP,IAP], 'clinical_scenario')
q('A patient with gallstone pancreatitis has improving liver tests, no fever or jaundice, no duct dilatation and no evidence of retained duct stones. What is the role of early ERCP?',
 'Routine early ERCP is not indicated; use selective duct evaluation if suspicion persists',[
 ('All biliary pancreatitis requires ERCP within 24 hours','This disregards cholangitis and obstruction criteria.'),
 ('Diagnostic ERCP is preferred to EUS or MRCP for low-to-intermediate residual stone suspicion','EUS and MRCP can avoid unnecessary invasive ERCP.'),
 ('ERCP replaces the need to consider cholecystectomy in an operable patient','A retained gallbladder can still cause future events.')],
 'The benefit depends on an actionable duct problem',
 '**A passed stone can trigger pancreatitis without leaving persistent obstruction.**',
 ['Improving biochemical and imaging findings reduce the case for urgent intervention.', 'ERCP carries its own risks and should usually have a therapeutic purpose.'],
 '**Escalate if new evidence changes the assessment.**',
 ['Cholangitis or persistent biliary obstruction changes management.', 'EUS or MRCP is useful when a retained stone remains uncertain.'],
 [['No cholangitis/ongoing obstruction','No routine early ERCP'],['Uncertain retained stone','EUS or MRCP'],['Infected obstruction','Therapeutic ERCP']], [AP,IAP], 'clinical_scenario')
q('An operable patient is recovering from mild gallstone pancreatitis without necrosis or a persistent collection. When should cholecystectomy generally occur?',
 'During the same admission, preferably before discharge',[
 ('After six months in every patient','Delay leaves a period of recurrent biliary risk without a routine benefit in mild disease.'),
 ('Only after a second episode of pancreatitis','Recurrence need not occur before preventive treatment.'),
 ('Never if the presumed culprit stone has passed','A remaining gallbladder remains a source of stones.')],
 'Treat the source during recovery from mild disease',
 '**Same-admission cholecystectomy reduces recurrent gallstone-related events in suitable mild cases.**',
 ['This differs from severe necrotizing disease with ongoing inflammation or collections.', 'Surgical risk and duct-stone management still require individualized assessment.'],
 '**Do not generalize severe-disease delays to uncomplicated mild disease.**',
 ['Document severity and clinical recovery.', 'If surgery is unsuitable, an alternative prevention strategy needs specialist discussion.'],
 [['Mild uncomplicated biliary pancreatitis','Same admission when fit'],['Severe disease/collections','Individualized delay'],['Inoperable patient','Alternative strategy assessment']], [AP,IAP], 'clinical_scenario')
q('Under the revised Atlanta framework, what defines severe acute pancreatitis?',
 'Organ failure persisting for more than 48 hours',[
 ('Any lipase value above ten times normal','Enzyme magnitude does not define the severity category.'),
 ('A local fluid collection without organ failure','Local complications alone generally make disease moderately severe, not necessarily severe.'),
 ('A transient creatinine rise that resolves within 24 hours as the only complication','Transient organ failure is distinguished from persistent failure.')],
 'Severity is anchored to organ dysfunction and duration',
 '**Persistent respiratory, cardiovascular or renal organ failure is the defining severe-disease feature.**',
 ['Moderately severe disease includes transient organ failure or local/systemic complications without persistent failure.', 'Mild disease has neither organ failure nor local or systemic complications.'],
 '**Use serial assessment because severity evolves.**',
 ['A reassuring admission assessment does not exclude later deterioration.', 'An anatomical collection and physiological failure convey different information.'],
 [['Mild','No organ failure or complications'],['Moderately severe','Transient failure or complications'],['Severe','Persistent organ failure >48 hours']], [IAP])
q('A patient with severe pancreatitis develops a tense abdomen, oliguria and worsening ventilation. Bladder pressure is sustained at 25 mmHg. What is the best interpretation?',
 'Abdominal compartment syndrome because intra-abdominal pressure exceeds 20 mmHg with new organ dysfunction',[
 ('Intra-abdominal hypertension without compartment syndrome because oliguria is irrelevant','New organ dysfunction is central to the syndrome.'),
 ('A pressure threshold that proves infected necrosis','Raised pressure does not itself diagnose infection.'),
 ('An indication to intensify fluid loading without reassessment','Additional volume may worsen edema and pressure in an already overloaded patient.')],
 'Pressure becomes a syndrome when it compromises organs',
 '**Abdominal compartment syndrome combines sustained high intra-abdominal pressure with new organ dysfunction.**',
 ['Measure pressure in a standardized way and assess the trend.', 'Pancreatic inflammation, ileus, collections and fluid accumulation may contribute.'],
 '**Use prompt multidisciplinary pressure-reduction measures.**',
 ['Gastric or colonic decompression, drainage and careful fluid balance may help selected patients.', 'Refractory life-threatening dysfunction can require surgical decompression.'],
 [['Pressure ≥12 mmHg','Intra-abdominal hypertension'],['Pressure >20 plus new organ dysfunction','Compartment syndrome'],['Refractory dysfunction','Urgent escalation']], [IAP], 'clinical_scenario')
q('Which triglyceride result most strongly supports hypertriglyceridemia as the cause of acute pancreatitis when no gallstone or alcohol explanation is found?',
 'A level above 1,000 mg/dL obtained early in the presentation',[
 ('A level of 180 mg/dL obtained after a meal','Mild elevation alone is not convincing evidence of this etiology.'),
 ('A normal level several days after fasting as definitive exclusion of a previously severe elevation','Triglycerides can fall during fasting and treatment, so timing matters.'),
 ('Any detectable triglyceride concentration','Triglycerides are normally present and require contextual interpretation.')],
 'Very high triglycerides provide a causal clue',
 '**An early level above 1,000 mg/dL is particularly suggestive in the right setting.**',
 ['Check diabetes control, alcohol exposure, medicines and genetic susceptibility.', 'A delayed sample may underestimate the initiating concentration.'],
 '**Treat pancreatitis and the metabolic driver together.**',
 ['Correct hyperglycemia and other precipitating factors.', 'Long-term recurrence prevention requires substantial triglyceride reduction and dietary/metabolic management.'],
 [['Very severe early elevation','Supports causation'],['Mild elevation','Often nonspecific'],['Late post-fasting sample','May miss the peak']], [AP,IAP])
q('A patient develops acute pancreatitis three weeks after starting azathioprine. Gallstones, alcohol and marked hypertriglyceridemia are excluded. What is the most appropriate medication decision?',
 'Withdraw azathioprine as a plausible cause and avoid routine rechallenge',[
 ('Increase azathioprine because the reaction must be dose-dependent','Thiopurine pancreatitis is generally an idiosyncratic adverse reaction.'),
 ('Continue it unchanged until recurrent pancreatitis proves causality','A deliberate recurrence is not required for a reasonable adverse-drug assessment.'),
 ('Label every future abdominal pain episode as pancreatitis without diagnostic criteria','The suspected cause does not remove the need to establish the syndrome.')],
 'Drug causality requires chronology and competing-cause assessment',
 '**A recognized offending drug with a compatible interval is an important etiological clue.**',
 ['Avoid attributing pancreatitis to a drug before examining common alternatives.', 'Document the adverse reaction and coordinate an alternative treatment for the underlying condition.'],
 '**A rechallenge is usually unnecessary and may be harmful.**',
 ['Resolution after withdrawal supports but does not independently prove causality.', 'Future therapy depends on the disease indication and the type of reaction.'],
 [['Compatible exposure plus excluded common causes','Raises drug causality'],['Routine rechallenge','Usually avoid'],['Future treatment','Choose an alternative with the treating team']], [IAP], 'clinical_scenario')
q('Which histological pattern most strongly supports type 1 autoimmune pancreatitis?',
 'Lymphoplasmacytic inflammation, storiform fibrosis and obliterative phlebitis with IgG4-positive plasma cells',[
 ('Granulocytic epithelial lesions as the defining IgG4-independent pattern','That pattern favors type 2 autoimmune pancreatitis.'),
 ('Infiltrating atypical malignant glands with desmoplasia','That suggests ductal adenocarcinoma rather than autoimmune pancreatitis.'),
 ('Isolated acinar necrosis without the characteristic fibroinflammatory pattern','This is not the defining histological constellation of type 1 disease.')],
 'Type 1 is the pancreatic form of IgG4-related disease',
 '**Diagnosis integrates histology with imaging, serology and other-organ involvement.**',
 ['Biliary, salivary or retroperitoneal involvement may provide supporting evidence.', 'Serum IgG4 elevation alone is insufficient and can occur in other conditions.'],
 '**Interpret the whole pattern rather than one stain.**',
 ['A focal mass still requires careful exclusion of cancer.', 'A steroid response is supportive only in an appropriate diagnostic pathway.'],
 [['Type 1','Lymphoplasmacytic sclerosing/IgG4-related'],['Type 2','Duct-centric granulocytic epithelial injury'],['Cancer concern','Dedicated exclusion work-up']], [AIP])
q('A young adult with ulcerative colitis has autoimmune pancreatitis with granulocytic epithelial lesions and normal serum IgG4. Which subtype is most likely?',
 'Type 2 autoimmune pancreatitis',[
 ('Type 1 autoimmune pancreatitis solely because all autoimmune pancreatitis is IgG4-related','Type 2 is distinct and usually lacks the IgG4-related systemic phenotype.'),
 ('Hereditary PRSS1 pancreatitis because ulcerative colitis is diagnostic of it','IBD is associated with type 2 AIP, not a diagnostic marker for PRSS1 disease.'),
 ('Alcohol-related chronic pancreatitis because the serum IgG4 is normal','Normal IgG4 does not exclude type 2 AIP or establish an alcohol cause.')],
 'Normal IgG4 does not rule out autoimmune pancreatitis',
 '**Type 2 is characterized by duct-centric neutrophilic epithelial injury and an association with IBD.**',
 ['Pancreatic histology is often important for secure classification.', 'The clinical phenotype differs from systemic IgG4-related disease.'],
 '**Distinguish subtype from generic steroid responsiveness.**',
 ['Imaging findings can overlap between subtypes.', 'Other causes and malignancy must still be considered when appropriate.'],
 [['Type 2','Granulocytic epithelial lesions, IBD association'],['Type 1','IgG4-related systemic pattern'],['Normal IgG4','Compatible with type 2']], [AIP], 'clinical_scenario')
q('A focal pancreatic head mass and obstructive jaundice raise the possibility of autoimmune pancreatitis. What is the safest diagnostic principle before a steroid trial?',
 'Undertake an appropriate malignancy assessment, including EUS-guided tissue sampling when indicated',[
 ('Use steroid response alone as the initial test for every pancreatic mass','A response can mislead and delay cancer diagnosis.'),
 ('Treat a mildly raised IgG4 as definitive proof against cancer','Serum IgG4 is not sufficiently specific in isolation.'),
 ('Exclude pancreatic cancer because the patient has no severe pain','Pancreatic malignancy can be painless.')],
 'A reversible inflammatory hypothesis must not obscure cancer',
 '**A steroid trial is a specialist diagnostic step after a suitable cancer work-up.**',
 ['Assess pancreatic and duct imaging, other-organ disease, serology and tissue in combination.', 'Sampling quality and residual suspicion determine whether further evaluation is needed.'],
 '**Judge response objectively and promptly.**',
 ['Imaging and biochemical change should fit the expected disease pattern.', 'Failure to respond or persisting focal concern demands diagnostic reassessment.'],
 [['Isolated IgG4 elevation','Supportive, not definitive'],['Focal mass','Exclude malignancy appropriately'],['Steroid response','Optional contextual diagnostic evidence']], [AIP], 'clinical_scenario')
q('Which initial imaging strategy is generally appropriate for suspected chronic pancreatitis?',
 'Pancreatic CT or MRI, with EUS or secretin-enhanced MRCP considered when uncertainty remains',[
 ('Diagnostic ERCP as the routine first test in all patients','ERCP is invasive and usually reserved for a therapeutic indication.'),
 ('Serum lipase alone to demonstrate irreversible chronic structural disease','Enzymes may be normal and do not adequately define chronic morphology.'),
 ('A normal transabdominal ultrasound as definitive exclusion of early disease','Ultrasound has limited sensitivity, particularly for subtle or early disease.')],
 'Start with noninvasive structural assessment',
 '**Calcification, ductal distortion and atrophy can support established chronic pancreatitis.**',
 ['No single minor imaging feature establishes every early case.', 'EUS findings must be interpreted with symptoms, exposures and pretest probability.'],
 '**Investigate an alternative diagnosis when the pattern is atypical.**',
 ['Weight loss or a focal duct cutoff may require a cancer-focused evaluation.', 'Functional assessment is a separate question from morphological diagnosis.'],
 [['CT/MRI','First-line cross-sectional assessment'],['Persistent uncertainty','EUS or selected secretin MRCP'],['ERCP','Usually therapeutic']], [CP])
q('A patient with chronic pancreatitis takes all pancreatic enzyme capsules at bedtime but still has postprandial steatorrhea. What is the most useful administration correction?',
 'Take enzymes during meals and snacks, distributing the dose through the meal when appropriate',[
 ('Take the entire daily dose on an empty stomach each morning','Enzymes need to mix with food to aid digestion.'),
 ('Use enzymes only on days with abdominal pain','Their principal indication here is maldigestion, not episodic analgesia.'),
 ('Stop enzymes whenever a meal contains fat','Fat-containing meals increase the need for effective lipase delivery.')],
 'Replacement works only when enzyme and food meet',
 '**Meal-associated administration is a central part of effective PERT.**',
 ['Check actual dose, timing and adherence before declaring treatment failure.', 'Dose escalation or acid suppression may be considered in selected inadequate responders after assessment.'],
 '**Follow nutritional response as well as stool symptoms.**',
 ['Weight, muscle status and fat-soluble vitamins help assess adequacy.', 'Persistent symptoms can also arise from SIBO, celiac disease or another coexisting disorder.'],
 [['With food','Promotes mixing and digestion'],['Remote from meals','Poor matching to nutrient delivery'],['Persistent symptoms','Review timing, dose and alternatives']], [EPI], 'clinical_scenario')
q('According to the AGA 2023 practice update, what is a reasonable initial adult PERT dose for established exocrine pancreatic insufficiency?',
 'At least 40,000 USP lipase units during each main meal and about half with snacks, then adjust',[
 ('4,000 USP lipase units once daily irrespective of meals','This is usually far below an appropriate adult meal dose and is mistimed.'),
 ('40,000 amylase units weekly as the dosing target','PERT is conventionally titrated in lipase units and taken with food.'),
 ('A fixed dose for all patients with no adjustment for intake or response','Requirements vary with meal size, fat content and residual pancreatic function.')],
 'Specify the enzyme, unit and timing',
 '**Lipase units per eating occasion are the practical starting framework.**',
 ['A starting dose is not a guarantee of adequate replacement.', 'Severe insufficiency or altered surgical anatomy may require higher individualized doses.'],
 '**Titrate against a combination of clinical and nutritional outcomes.**',
 ['Assess steatorrhea, weight and nutritional deficiencies.', 'Do not solve maldigestion by unnecessary severe dietary fat restriction alone.'],
 [['Main meal','At least 40,000 USP lipase units initially'],['Snack','About half the meal dose initially'],['Follow-up','Individualize dose and nutrition']], [EPI])
q('Which statement best describes pancreatic enzyme replacement as a treatment for pain in chronic pancreatitis?',
 'It treats exocrine insufficiency but should not be prescribed solely as a reliably effective analgesic strategy',[
 ('It reliably reverses ductal obstruction and eliminates the need for drainage','Enzymes do not mechanically decompress an obstructed duct.'),
 ('Its lack of reliable analgesic benefit means it should be withheld in steatorrhea','Maldigestion is a separate, established indication.'),
 ('Pain relief is the only meaningful marker of adequate enzyme replacement','Nutritional response and maldigestion are the relevant targets.')],
 'Keep the treatment indication clear',
 '**The evidence for routine enzyme therapy specifically to relieve pancreatic pain is inadequate.**',
 ['Pain can reflect inflammation, ductal pressure, neuropathic mechanisms or a complication.', 'Assess exocrine insufficiency independently and replace enzymes when indicated.'],
 '**A persistent pain syndrome needs its own evaluation.**',
 ['Consider pseudocyst, obstruction and malignancy where clinically appropriate.', 'Analgesic, behavioral, endoscopic and surgical options depend on the mechanism.'],
 [['Exocrine insufficiency','PERT indicated'],['Pain alone','PERT is not dependable analgesia'],['Obstructed duct or complication','Consider targeted intervention']], [CP])
q('Why can insulin-treated pancreatogenic diabetes be particularly prone to hypoglycemia?',
 'Pancreatic damage can impair glucagon counterregulation as well as insulin secretion',[
 ('The disease always causes isolated insulin resistance with normal islet reserve','Islet destruction is central in many pancreatogenic cases.'),
 ('Loss of glucagon necessarily protects against insulin-induced hypoglycemia','Glucagon normally helps restore glucose during hypoglycemia.'),
 ('Exocrine insufficiency guarantees uniform nutrient absorption','Maldigestion and variable intake can further destabilize glucose control.')],
 'Type 3c diabetes is more than beta-cell loss',
 '**Combined endocrine deficits, nutritional variability and impaired digestion complicate treatment.**',
 ['Insulin may be necessary as insulin reserve falls.', 'Alcohol exposure, poor intake and malabsorption can add hypoglycemia risk.'],
 '**Integrate diabetes and nutritional management.**',
 ['Optimize indicated PERT and meal consistency.', 'Use individualized glucose monitoring and hypoglycemia education rather than assuming a typical type 2 phenotype.'],
 [['Insulin deficiency','Hyperglycemia'],['Impaired glucagon response','Reduced hypoglycemia defense'],['Maldigestion/variable intake','Further glycemic variability']], [NICE,CP])
q('A 7-cm mature pancreatic pseudocyst is incidentally found after pancreatitis. The patient has no pain, infection, bleeding or gastric/biliary obstruction. What is the best management principle?',
 'Assess and follow clinically; size alone is not an automatic indication for drainage',[
 ('Drain every collection exceeding 6 cm solely on that measurement','The historical size rule is not sufficient by itself.'),
 ('Operate on every collection persisting beyond six weeks regardless of symptoms','Persistence alone does not mandate an operation.'),
 ('Ignore all future symptoms because an asymptomatic pseudocyst can never cause complications','New symptoms or complications require reassessment.')],
 'Intervene for a clinical reason rather than a size slogan',
 '**Symptoms, infection, bleeding and obstruction are major drivers of intervention.**',
 ['Confirm that the lesion is truly post-inflammatory rather than a cystic neoplasm.', 'Duct anatomy and local expertise influence the route if drainage becomes necessary.'],
 '**Use follow-up to identify a changing risk-benefit balance.**',
 ['New early satiety, vomiting, jaundice or pain can be relevant.', 'Suspected vascular bleeding must be assessed before cyst drainage.'],
 [['Asymptomatic uncomplicated pseudocyst','Observation may be appropriate'],['Obstruction/infection/pain','Consider intervention'],['Bleeding concern','Assess vascular source first']], [IAP,NICE], 'clinical_scenario')
q('A patient with chronic pancreatitis develops a sudden hemoglobin fall and bleeding into a pseudocyst. Arterial-phase CT shows a splenic artery pseudoaneurysm. What is the preferred immediate management direction when feasible?',
 'Urgent interventional radiology assessment for angiographic embolization with resuscitation',[
 ('Routine transgastric cyst drainage before addressing the artery','Draining a collection with an untreated pseudoaneurysm can precipitate catastrophic bleeding.'),
 ('PERT dose escalation as the definitive hemostatic treatment','Enzymes do not close an arterial defect.'),
 ('Observation until the pseudocyst reaches a particular size threshold','Active vascular bleeding requires urgent action.')],
 'The vascular lesion determines the immediate priority',
 '**Pancreatic inflammation can erode an adjacent artery and form a pseudoaneurysm.**',
 ['Bleeding may be intracystic, gastrointestinal or intraperitoneal.', 'CTA and angiography define and potentially treat the source.'],
 '**Stabilize and obtain definitive hemostasis before elective collection treatment.**',
 ['Endovascular treatment is often preferred when anatomy and resources permit.', 'Uncontrolled bleeding or unsuitable anatomy may require surgery.'],
 [['Pseudoaneurysm','Arterial wall injury'],['Feasible endovascular access','Embolization pathway'],['Uncontrolled hemorrhage','Urgent surgical backup']], [NICE,IAP], 'clinical_scenario')
q('After mid-body pancreatic necrosis, a patient has recurrent fluid collections despite drainage. MRCP shows a viable upstream tail disconnected from the downstream duct. What mechanism best explains recurrence?',
 'Continued secretion from a disconnected viable pancreatic segment',[
 ('A simple communicating pseudocyst that must resolve after one aspiration','A disconnected remnant can maintain leakage or recurrent collections.'),
 ('Complete absence of pancreatic secretion from all viable tissue','The viable isolated segment can continue to secrete.'),
 ('A gallbladder stone as proof that no pancreatic duct problem exists','Biliary disease does not exclude a post-necrotic duct disruption.')],
 'Disconnected duct syndrome can sustain a leak',
 '**Necrosis can interrupt the main duct while leaving functioning pancreas upstream.**',
 ['Recurrent collections, external fistula or pancreatic ascites may follow.', 'Duct imaging and collection anatomy guide specialist planning.'],
 '**A single drainage procedure may not solve the underlying anatomy.**',
 ['Long-term internal drainage or surgery may be considered according to anatomy and fitness.', 'Management should be individualized by an experienced pancreatic team.'],
 [['Viable disconnected remnant','Ongoing secretion'],['Repeated recurrence','Look for duct disruption'],['Definitive plan','Anatomy-based endoscopic/surgical assessment']], [NEC,IAP], 'clinical_scenario')
q('A patient with chronic pancreatitis has isolated fundal gastric varices, splenomegaly, a patent portal vein and no cirrhosis. Which vascular complication is most likely?',
 'Splenic vein thrombosis causing left-sided portal hypertension',[
 ('Isolated hepatic vein thrombosis as the usual explanation','Budd–Chiari syndrome produces a different hepatic outflow phenotype.'),
 ('Splenic artery stenosis as the usual cause of venous gastric collaterals','The key lesion here is venous outflow obstruction.'),
 ('Inferior vena cava thrombosis without hepatic or splenic venous involvement','This does not explain the characteristic localized gastric collateral pattern.')],
 'Regional venous obstruction can mimic a portal-hypertensive complication',
 '**The splenic vein lies close to the pancreas and can thrombose during pancreatic disease.**',
 ['Short gastric collateral pathways can generate isolated gastric varices.', 'Normal liver structure and patent main portal flow support a regional mechanism.'],
 '**Define the anatomy before choosing treatment.**',
 ['Bleeding risk, acuity and extent affect the plan.', 'Do not assume that every gastric varix is caused by cirrhosis.'],
 [['Splenic vein obstruction','Left-sided portal hypertension'],['Fundal gastric varices','Characteristic collateral pattern'],['Main portal vein and liver','May remain normal']], [CP,IAP], 'clinical_scenario')
q('Recurrent pancreatitis beginning in childhood occurs across three generations. Which gene is classically associated with autosomal dominant hereditary pancreatitis?',
 'PRSS1',[
 ('APC','APC is associated primarily with familial adenomatous polyposis.'),
 ('PKD1','PKD1 is associated with autosomal dominant polycystic kidney disease.'),
 ('HFE','HFE is associated with hereditary iron overload, not the classical hereditary pancreatitis syndrome.')],
 'A young familial pattern warrants genetic evaluation',
 '**PRSS1 encodes cationic trypsinogen, linking susceptibility to dysregulated intrapancreatic protease activity.**',
 ['Other genes can modify risk or contribute to recurrent pancreatitis.', 'A specialist genetic assessment includes counseling and careful phenotype interpretation.'],
 '**A positive result has implications beyond naming the cause.**',
 ['Discuss smoking avoidance and the associated long-term cancer risk.', 'Do not apply a single inheritance model to every pancreatitis-associated variant.'],
 [['PRSS1','Classical autosomal dominant hereditary pancreatitis'],['SPINK1/CFTR and others','May contribute through other risk patterns'],['Early recurrent disease','Consider specialist genetics']], [CP])
q('How should a heterozygous CFTR variant be interpreted in an adult with recurrent otherwise unexplained pancreatitis?',
 'It may contribute to susceptibility, but interpretation requires variant classification, phenotype and other risk factors',[
 ('Every heterozygous CFTR variant proves classical cystic fibrosis','Carrier status and disease-causing combinations require more careful interpretation.'),
 ('CFTR has no role in pancreatic duct physiology','CFTR affects ductal fluid and bicarbonate transport.'),
 ('A CFTR finding makes evaluation for gallstones and alcohol unnecessary','A genetic contribution does not exclude additional causes.')],
 'Genetic susceptibility is not always a complete diagnosis',
 '**Altered ductal secretion can predispose to pancreatic injury in selected CFTR-related phenotypes.**',
 ['Some variants are benign or of uncertain significance.', 'Functional testing and genetics input may be needed in the appropriate phenotype.'],
 '**Integrate genetic and acquired factors.**',
 ['Avoid both dismissing a relevant finding and overcalling a carrier result.', 'Counseling should use the actual variant and clinical context.'],
 [['Pathogenic variant plus compatible phenotype','Potential etiological contribution'],['Uncertain variant','Not proof of causation'],['Acquired risks','Still assess']], [CP])
q('A patient with stable chronic pancreatitis develops new progressive weight loss, worsening diabetes and a focal pancreatic duct cutoff. What is the best next principle?',
 'Reassess promptly for pancreatic malignancy with dedicated imaging and appropriate EUS-guided evaluation',[
 ('Attribute every new symptom to established chronic pancreatitis','A change in pattern can indicate a superimposed malignancy or complication.'),
 ('Exclude malignancy because pancreatic calcification is present','Chronic pancreatitis and pancreatic cancer can coexist.'),
 ('Use a normal CA 19-9 as a definitive rule-out test','CA 19-9 lacks the sensitivity and specificity to exclude cancer on its own.')],
 'A changed trajectory deserves a new diagnosis search',
 '**Chronic inflammation does not immunize a patient against cancer.**',
 ['New focal obstruction and progressive constitutional change are concerning.', 'Dedicated cross-sectional imaging and tissue evaluation are selected according to the findings.'],
 '**Interpret negative tests in light of residual suspicion.**',
 ['Chronic pancreatitis can make imaging and sampling more difficult.', 'Persisting concern can justify repeat expert assessment rather than false reassurance.'],
 [['Stable chronic pattern','Routine disease management'],['New focal/progressive change','Investigate malignancy or complication'],['Normal tumor marker','Does not exclude cancer']], [CP,NICE], 'clinical_scenario')
q('A fit patient has painful obstructive chronic pancreatitis with a dilated main duct and persistent symptoms despite appropriate medical care. What management discussion is warranted?',
 'Multidisciplinary assessment of duct decompression, including a surgical option rather than indefinite serial medical escalation alone',[
 ('PERT alone will reliably remove the mechanical obstruction','Enzymes treat maldigestion and do not decompress the duct.'),
 ('Surgery is never considered until pancreatic endocrine function is completely lost','This is not a required threshold for pain-directed intervention.'),
 ('Long-term opioids must be exhausted before any pancreatic team assessment','Structural disease can merit earlier targeted evaluation.')],
 'Mechanical obstruction can require mechanical treatment',
 '**The duct anatomy, stones, inflammatory head mass and operative fitness determine the intervention.**',
 ['Endoscopic therapy can be useful in selected anatomy.', 'Surgery can provide durable benefit in appropriate obstructive disease and should be discussed rather than indefinitely deferred.'],
 '**Use shared selection based on the actual anatomical problem.**',
 ['Pain may have more than one mechanism, so decompression is not a universal cure.', 'Continue nutritional, diabetes, alcohol and smoking management alongside intervention planning.'],
 [['Dilated obstructed duct','Consider decompression strategy'],['Focal inflammatory head disease','May alter the operation'],['No correctable structural target','Assess other pain mechanisms']], [CP,NICE], 'clinical_scenario')

if __name__=='__main__':
    finalize('GI & pancreas',6,'Acute and Chronic Pancreatitis','gi-pancreatitis',rows,32)
