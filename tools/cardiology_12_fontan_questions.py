"""Fontan physiological decisions; expanded sequentially."""
from qbank_json_chapters import question as Q
REFERENCES={
 'FONTAN_PH':('AHA scientific statement: pulmonary hypertension in congenital heart disease, 2023','https://doi.org/10.1161/HHF.0000000000000080'),
 'FONTAN_STRESS':('Fontan pressure-flow profiling during stress and vasodilation, 2025','https://doi.org/10.1152/ajpheart.00105.2025'),
 'AAT_CLEARANCE':('Mayo Clinic Laboratories: alpha-1-antitrypsin clearance, feces and serum','https://www.mayocliniclabs.com/api/sitecore/TestCatalog/DownloadTestCatalog?testId=604982'),
 'FONTAN_KOREA':('Korean Fontan clinical practice consensus, 2025','https://doi.org/10.4070/kcj.2025.0455'),
}
TOPIC='Fontan and single-ventricle circulation'
rows=[Q(TOPIC,'Pulmonary Flow and Preload Limitation in Fontan Circulation',
 'An adult with an extracardiac Fontan has worsening exercise intolerance despite preserved systemic ventricular ejection fraction and no important AV-valve regurgitation. The conduit and branch pulmonary arteries are unobstructed. Pulmonary vascular resistance has increased, while ventricular filling pressure is unchanged. Which mechanism most directly reduces systemic output?',
 'Reduced passive pulmonary flow limits systemic ventricular preload',[
 ('Increased pulmonary resistance directly increases systemic ventricular systolic afterload','Systemic arterial resistance and outflow obstruction directly determine systemic ventricular ejection load. Pulmonary resistance lies upstream of ventricular filling in a Fontan circulation and primarily limits delivery of preload, although the entire circulation remains coupled.'),
 ('Increased pulmonary resistance produces failure of the subpulmonary ventricular pump','This explains an important mechanism in a biventricular circulation with pulmonary vascular disease. A completed Fontan has no functioning subpulmonary ventricular pump between caval return and the pulmonary arteries.'),
 ('Preserved ejection fraction ensures preserved stroke volume, so chronotropic limitation must explain the symptoms','Chronotropic limitation is a real Fontan problem but is not established here. Ejection fraction is a proportion; an underfilled ventricle can eject a normal fraction while delivering a reduced absolute stroke volume.')],
 [('Pressure-Flow Relationship',[
  ('**The Fontan pathway connects systemic venous return to the pulmonary arteries without an intervening ventricle.** Flow through the lungs depends on a limited upstream-to-downstream pressure gradient and low resistance.',[
   'Conceptually, pulmonary flow depends on the difference between Fontan and pulmonary venous pressures divided by pulmonary vascular resistance. Increased resistance can reduce flow or require a higher upstream venous pressure to sustain it.',
   'The resulting reduction in pulmonary venous return limits systemic ventricular end-diastolic volume and stroke volume. A normal ejection fraction therefore does not establish normal cardiac output or exclude Fontan circulatory failure.'])]),
  ('Clinical Assessment and Treatment Implications',[
  ('**Assess the entire circuit when exercise capacity declines.** Ventricular systolic performance is only one component of the evaluation.',[
   'Look for pathway or branch-artery obstruction, elevated ventricular filling pressure, AV-valve regurgitation, arrhythmia, collateral flow and pulmonary vascular limitation. Catheter assessment can define pressures and flow when noninvasive studies do not explain deterioration.',
   'Venous congestion and inadequate ventricular filling may coexist. Diuresis can relieve congestion but excessive volume removal can further reduce output; treatment requires attention to the individual pressure and flow profile.',
   'Pulmonary vasodilators may improve exercise performance in selected patients without elevated ventricular end-diastolic pressure, but heterogeneous trial results do not support treating every Fontan patient identically. A mechanical pathway stenosis requires its own assessment rather than an assumption that vasodilator treatment will correct it. Exercise evaluation and serial clinical measurements help detect physiological deterioration that resting systolic imaging can miss.'])])],
 ['ACHD2025','FONTAN_PH','FONTAN_STRESS'])]

rows.append(Q(TOPIC,'Confirming Protein-Losing Enteropathy After Fontan Palliation',
 'A 27-year-old with Fontan circulation develops edema, loose stools and serum albumin 2.1 g/dL. Urinary protein excretion is 120 mg/day, INR is 1.1 without anticoagulation, and there is no gastrointestinal bleeding. Which test most directly establishes excessive intestinal protein loss?',
 'Timed fecal alpha-1-antitrypsin clearance with a contemporaneous serum level',[
 ('Fecal calprotectin concentration','Calprotectin assesses intestinal inflammation and can support investigation of inflammatory bowel disease. It does not quantify plasma protein clearance into the intestine, which is the immediate diagnostic question in this Fontan patient.'),
 ('Fecal pancreatic elastase concentration','Elastase helps evaluate exocrine pancreatic insufficiency in a patient with maldigestion or steatorrhea. A low result can also be misleading in watery stool; it does not directly establish enteric plasma protein loss.'),
 ('Quantitative fecal fat excretion','Fecal fat can document fat malabsorption and may assist a broader nutritional assessment. It measures loss of fat rather than plasma proteins, so it cannot directly confirm the suspected protein-losing enteropathy.')],
 [('Mechanism and Differential Diagnosis',[
  ('**Fontan-associated protein-losing enteropathy reflects intestinal protein leakage in a circulation with abnormal venous and lymphatic pressures.** Edema and hypoalbuminemia are typical, but diarrhea is not obligatory.',[
   'Assess renal protein loss, hepatic synthetic impairment, nutritional intake and other intestinal disease. The small urinary protein loss in this vignette is insufficient to explain the profound hypoalbuminemia. A normal INR does not exclude Fontan-associated liver disease, and more than one mechanism may coexist.',
   'Loss may include immunoglobulins and lymphocytes as well as albumin. Review nutritional status, infection risk and fluid balance rather than interpreting albumin as an isolated liver test.'])]),
  ('Test Collection and Interpretation',[
  ('**Alpha-1-antitrypsin clearance combines a timed stool collection with a serum concentration obtained during collection.** It accounts for circulating concentration and stool output better than an isolated random fecal concentration.',[
   'Mayo lists a reference clearance of 27 mL/24 hours or less. Interpret against the performing laboratory and stool consistency: diarrhea can increase clearance, and a higher threshold is used in some Fontan definitions. Do not apply a single cutoff without those qualifications.',
   'Gastrointestinal bleeding can contribute protein to stool. Acid degradation also limits assessment of predominantly gastric protein loss; a negative test does not resolve every possible protein-losing disorder.'])]),
  ('Evaluate the Failing Fontan Circuit',[
  ('**Confirmation should trigger assessment for reversible hemodynamic and lymphatic contributors.** Preserved ventricular ejection fraction does not exclude an important Fontan circulation problem.',[
   'Evaluate pathway obstruction, pulmonary resistance, ventricular filling pressure, AV-valve regurgitation and rhythm. Catheterization and specialist lymphatic imaging may be appropriate according to the findings.',
   'Management combines nutritional support and careful fluid treatment with correction of identified lesions. Selected patients require targeted lymphatic interventions or advanced heart-failure and transplant assessment. Albumin infusion can provide temporary support in selected circumstances but does not by itself correct the cause of continuing intestinal loss.'])])],
 ['ACHD2025','AAT_CLEARANCE','FONTAN_KOREA']))
