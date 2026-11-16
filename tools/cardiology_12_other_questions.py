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
