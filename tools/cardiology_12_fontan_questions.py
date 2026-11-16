"""Fontan physiological decisions; expanded sequentially."""
from qbank_json_chapters import question as Q
REFERENCES={
 'FONTAN_PH':('AHA scientific statement: pulmonary hypertension in congenital heart disease, 2023','https://doi.org/10.1161/HHF.0000000000000080'),
 'FONTAN_STRESS':('Fontan pressure-flow profiling during stress and vasodilation, 2025','https://doi.org/10.1152/ajpheart.00105.2025'),
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
