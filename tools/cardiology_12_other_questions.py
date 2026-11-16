"""Additional congenital lesions with physiology-based decisions."""
from qbank_json_chapters import question as Q
REFERENCES={}
def S(h,t,*details):return h,[(t,list(details))]
rows=[Q('Other important congenital lesions','Small Isolated Anomalous Pulmonary Venous Shunt',
 'CMR in an asymptomatic adult shows one right upper pulmonary vein draining to the SVC, an intact atrial septum, Qp/Qs 1.2 and a mildly enlarged RV with normal function. Pulmonary pressure is normal and serial measurements are stable. Which strategy is best supported?',
 'Continue congenital cardiology surveillance without repair at present',[
 ('Refer for surgical redirection based on the anomalous connection alone','Surgical redirection is appropriate for selected hemodynamically important anomalous drainage. The anatomical finding alone does not establish benefit when the shunt is small, RV enlargement is mild and function and clinical status are stable.'),
 ('Plan covered-stent correction using the sinus venosus ASD pathway','Selected superior sinus venosus defects with suitable venous anatomy may undergo specialized covered-stent correction. This isolated anomalous vein with an intact septum is not the same lesion, and its small physiological burden does not justify applying that pathway.'),
 ('Perform invasive hemodynamic assessment before deciding whether any observation is acceptable','Catheterization is useful for suspected pulmonary hypertension, uncertain hemodynamics or discordant noninvasive findings. Clear concordant CMR data, normal pressure estimates and stable mild RV enlargement do not require an invasive study merely to justify surveillance.')],
 [S('Anatomy Does Not Establish an Intervention Indication',
  '**An anomalous pulmonary vein returns oxygenated blood to the systemic venous circuit.** This creates recirculation through the right heart and lungs even when the atrial septum is intact.',
  'The number and size of anomalous veins, and the lung territory they drain, influence flow burden. Unlike an ASD, the communication is not an atrial opening whose shunt is chiefly determined by relative ventricular diastolic compliance.',
  'The 2025 ACHD guideline advises against surgical repair when Qp/Qs is below 1.5 and the RV is normal to mildly enlarged, because benefit has not been demonstrated. This patient fits that qualified recommendation; it is not a rule that every anomalous vein should remain untreated.'),
  S('Surveillance and Reassessment',
  '**Follow symptoms, exercise capacity, RV size and function, and pulmonary hemodynamics.** CMR can map the veins and quantify flow and chamber volumes; CT provides detailed anatomy when CMR is unsuitable.',
  'Worsening exercise limitation, progressive RV enlargement or dysfunction, a larger shunt or suspected pulmonary vascular disease changes the assessment. Significant attributable volume loading may warrant repair after congenital surgical review.',
  'Repair planning must define the entire venous pathway and associated defects. Potential postoperative problems include pulmonary venous or systemic venous obstruction and rhythm complications, depending on the reconstruction. These risks reinforce the need for a demonstrable physiological indication rather than intervention based solely on an unusual image.',
  'An intact atrial septum excludes the assumed ASD closure target but does not exclude a left-to-right shunt from anomalous drainage. Conversely, an unexplained enlarged RV should prompt a search for anomalous veins even when routine echocardiography does not show an ASD.')],
 ['ACHD2025','ESC2020'])]

rows.append(Q('Other important congenital lesions','Localizing Obstruction in Cor Triatriatum Sinister',
 'An adult with exertional dyspnea has a left atrial membrane on TEE. All pulmonary veins enter the chamber upstream of it; the left atrial appendage and a normally opening mitral valve lie downstream. Doppler localizes acceleration to a small membrane opening. Which diagnosis best explains the obstruction?',
 'Cor triatriatum sinister',[
 ('Supramitral ring','A supramitral ring produces obstruction close to the mitral valve, typically below the left atrial appendage. The supplied appendage lies downstream of the membrane with the mitral valve, supporting cor triatriatum anatomy instead.'),
 ('Congenital valvar mitral stenosis','Congenital mitral stenosis involves the valve apparatus and may accompany other left-sided obstructive lesions. Here the valve opens normally and the flow acceleration is localized to a separate atrial membrane.'),
 ('Pulmonary vein stenosis','Pulmonary vein stenosis obstructs one or more venous entry pathways and can cause pulmonary venous hypertension. The observed obstructing structure instead separates the pulmonary venous chamber from the appendage-containing distal atrium.')],
 [S('Use the Appendage as an Anatomical Landmark',
  '**Cor triatriatum sinister partitions the left atrium into a proximal pulmonary venous chamber and a distal chamber containing the appendage and mitral valve.** The size and number of membrane openings determine the physiological obstruction.',
  'A restrictive opening can mimic mitral stenosis by raising upstream pulmonary venous pressure despite a normal valve. A nonrestrictive membrane may be discovered incidentally in an adult without a clinically important gradient.',
  'The relationship to the appendage helps distinguish a supramitral ring, but the entire membrane, valve apparatus and pulmonary venous anatomy should be mapped. Do not diagnose valvar stenosis from pulmonary congestion or a diastolic flow disturbance alone.'),
  S('Assess Physiology and Associated Lesions',
  '**Echocardiography defines the membrane and localizes flow acceleration.** TEE and three-dimensional imaging can clarify anatomy; CMR or CT can assess pulmonary veins and associated congenital lesions when needed.',
  'Interpret gradients with flow, heart rate and symptoms. Pulmonary hypertension or discordant noninvasive findings may justify invasive assessment. Symptoms after prior repair require consideration of residual obstruction and associated pulmonary vein disease.'),
  S('Treatment According to Obstruction',
  '**Symptoms attributable to membrane obstruction warrant surgical resection under current ACHD guidance.** The aim is to relieve pulmonary venous hypertension rather than intervene on a normally opening mitral valve.',
  'Severe obstruction can also justify surgical assessment in an asymptomatic adult. Conversely, a reassuring nonobstructive lesion can be followed without automatic surgery. Evaluate associated defects, atrial arrhythmia and ventricular or valve disease as part of the same decision.',
  'Diuretics may temporarily relieve congestion but do not remove the membrane. Long-term follow-up after treatment considers residual lesions, pulmonary venous abnormalities and recurrent symptoms; anatomical repair does not eliminate every associated congenital problem.')],
 ['ACHD2025','ESC2020']))

rows.append(Q('Other important congenital lesions','Ischemic Anomalous Aortic Coronary Origin',
 'A 24-year-old has exertional chest pain and presyncope. Coronary CT shows the left coronary artery arising from the right sinus with a slit-like ostium and proximal intramural segment. Stress imaging demonstrates ischemia in its territory, without atherosclerotic disease. Which management strategy is most appropriate?',
 'Refer for congenital coronary surgical repair assessment',[
 ('Use antianginal medication with imaging surveillance as the definitive strategy','Medication and surveillance can be considered in selected patients whose risk and anatomy do not justify intervention, or when intervention is unsuitable. Attributable symptoms and demonstrated ischemia in this high-risk anatomical pattern support surgical treatment assessment.'),
 ('Proceed directly to coronary stenting as for an atherosclerotic ostial lesion','PCI treats many acquired coronary stenoses and may have selected roles in congenital anomalies. This young patient has an intramural congenital origin abnormality, not an ordinary plaque lesion; anatomical surgical correction requires specialist consideration rather than automatic ostial stenting.'),
 ('Implant a prophylactic ICD before addressing the coronary anomaly','An ICD is appropriate for selected patients with established arrhythmic indications, including some secondary-prevention settings. It does not correct the ischemic substrate, and the supplied history does not establish a standalone device indication in place of coronary repair.')],
 [S('Combine Anatomy With Attributable Ischemia',
  '**Anomalous origin alone is not a complete risk description.** The ostial shape, takeoff angle, proximal narrowing and intramural or other course influence the potential for compromised perfusion.',
  'The left coronary arising from the opposite sinus with an intramural segment is particularly concerning when exertional symptoms and territorial ischemia agree. This combination supports a causal relationship rather than incidental discovery of a benign anatomical variant.',
  'CT angiography usually provides detailed definition of origin and proximal course. Functional testing adds evidence about ischemia; a negative test in another patient does not automatically neutralize every high-risk anatomical feature.'),
  S('Select an Anatomical Repair',
  '**Current ACHD guidance recommends surgery for symptomatic AAOCA or ischemia attributable to the anomalous artery.** The operation must be selected from the actual coronary and aortic-root anatomy.',
  'Unroofing may address a suitable intramural segment; reimplantation or another reconstruction may be preferred in other configurations. The relationship to an aortic commissure and potential valve injury matter. Avoid treating every interarterial or intramural variant with an identical operation.',
  'Restrict strenuous exertion pending specialist assessment in this symptomatic ischemic presentation. Review ventricular function, scar and arrhythmias, and coordinate postoperative reassessment before decisions about return to sport.'),
  S('Limits of Generalization',
  '**Asymptomatic anomalies require a separate risk discussion.** A retroaortic circumflex course, for example, does not carry the same implications as the supplied left-coronary phenotype.',
  'Surgical outcome assessment includes residual ischemia, recurrent symptoms, coronary patency and aortic regurgitation. Repair should not be presented as a guarantee against every future event. Conversely, an ICD or antianginal prescription does not remove a mechanically compromised coronary origin; those treatments answer different clinical questions.')],
 ['ACHD2025','ESC2020']))
