"""Foundational ACHD physiological reasoning."""
from qbank_json_chapters import question as Q
REFERENCES={}
def S(h,t,*details):return h,[(t,list(details))]
TOPIC='Foundations and physiological classification'
rows=[Q(TOPIC,'Chamber Loading in Congenital Left-to-Right Shunts',
 'Which pairing correctly describes the dominant chamber volume-loading pattern of an uncomplicated significant left-to-right shunt before advanced pulmonary vascular disease develops?',
 'ASD: right atrium and RV; VSD: left atrium and LV',[
 ('ASD: left atrium and LV; VSD: right atrium and RV','This reverses the usual diagnostic pattern. Atrial shunting increases right-sided filling, whereas pulmonary recirculation from a ventricular shunt returns to the left atrium and ventricle.'),
 ('ASD: right atrium and RV; VSD: isolated RV pressure loading without left-heart volume loading','The ASD component is correct, and a large VSD can transmit pressure to the RV and pulmonary artery. However, a significant left-to-right VSD also increases pulmonary venous return and left-heart volume load; pressure transmission does not remove that effect.'),
 ('ASD: isolated RV pressure loading; VSD: left atrium and LV','The VSD component is correct. In an uncomplicated ASD without advanced pulmonary vascular disease, increased RV filling volume is the primary load; isolated pressure overload suggests another or additional mechanism.')],
 [S('Follow the Recirculating Blood',
  '**The level of the communication determines where excess flow re-enters the circuit.** In an ASD, pulmonary venous blood reaching the left atrium can cross into the right atrium and increase RV filling.',
  'In a VSD, left ventricular output diverted to the pulmonary circuit returns through the pulmonary veins to the left atrium and LV. Left-heart enlargement therefore helps quantify the physiological consequence of the ventricular shunt.',
  'A PDA also increases pulmonary venous return and left-heart volume loading. Anomalous pulmonary venous connection instead directs oxygenated venous blood into the systemic venous circuit, producing a right-sided volume burden.'),
  S('Separate Pressure From Flow',
  '**Pressure transmission and excess flow are related but distinct.** A large nonrestrictive VSD may produce high RV and PA pressures, while a restrictive defect maintains a substantial LV-to-RV systolic gradient.',
  'High pulmonary pressure does not by itself prove high pulmonary vascular resistance. Interpret pressure together with flow and downstream filling pressure. Conversely, advanced pulmonary vascular disease may reduce the left-to-right shunt and alter the expected chamber pattern.',
  'Valvar pulmonary stenosis produces RV pressure loading without a primary recirculating left-to-right shunt. Pulmonary regurgitation can cause RV volume loading without an ASD. Chamber enlargement narrows the physiological differential but does not establish the anatomical diagnosis alone.'),
  S('Apply the Pattern to Imaging',
  '**Match chamber size to the suspected lesion and quantify the actual flow.** Unexpected findings should prompt review for additional valve disease, anomalous veins, obstruction or pulmonary vascular disease.',
  'Echocardiography maps the communication and estimates pressures; CMR can quantify volumes and Qp/Qs when needed. Symptoms, attributable chamber enlargement and pulmonary vascular status influence intervention assessment. Do not select closure solely from a chamber label or assume that a small anatomical defect must have a large physiological effect.')],
 ['ACHD2025','ESC2020'],style='direct')]

REFERENCES['AP2025']=('AHA: 2025 ACHD anatomic and physiological classification','https://professional.heart.org/en/science-news/2025-adult-congenital-heart-disease-anatomic-and-physiological-classification-system')
rows.append(Q(TOPIC,'Anatomical Complexity and Physiological Stage',
 'An adult with repaired tetralogy of Fallot without pulmonary atresia is now NYHA class II, with moderate pulmonary regurgitation. Four months ago the patient required hospitalization for heart failure. Which 2025 ACHD anatomic-physiological classification applies?',
 'II-D',[
 ('II-C','TOF without pulmonary atresia has moderate anatomical complexity, and moderate valve dysfunction is a stage C feature. However, the heart-failure admission within 12 months establishes stage D despite the current improvement in functional class.'),
 ('III-C','Great anatomical complexity includes TOF with pulmonary atresia and other complex circulations, not the supplied form of repaired TOF. This option also underestimates physiology by ignoring the recent heart-failure hospitalization.'),
 ('III-D','Stage D correctly reflects the recent admission. Anatomical category III would fit, for example, pulmonary atresia or Fontan physiology; heart failure alone does not move ordinary repaired TOF from category II to III.')],
 [S('Two Complementary Axes',
  '**Anatomical complexity and current physiological burden answer different questions.** The anatomical categories are I, simple; II, moderate complexity; and III, great complexity. Physiological stages range from A to D.',
  'Anatomy describes the congenital lesion and circulation. Physiology reflects current sequelae and clinical status and can change over time. Repair does not automatically reclassify every lesion as anatomically simple or establish physiological stage A.'),
  S('Use the Current Criteria',
  '**The 2025 framework refines the physiological criteria.** Review symptoms, ventricular and valve function, shunts, pulmonary vascular disease, oxygenation, rhythm and recent clinical events rather than relying on a single reassuring measurement.',
  'Stage A describes a patient without relevant symptoms or sequelae, with normal exercise capacity and pulmonary pressure and no sustained arrhythmia. Increasing stages incorporate clinically important abnormalities; recent heart-failure hospitalization and recurrent hemodynamically significant or refractory arrhythmia are stage D features in the updated framework.',
  'The time window and severity qualifications matter. Heart-failure hospitalization within the preceding 12 months places this patient in D even after symptomatic improvement. Use the highest applicable physiological stage; neither current NYHA II nor preserved function on one measurement cancels a qualifying recent event.'),
  S('Apply Classification to Care',
  '**The combined classification helps determine surveillance and specialist resource needs.** Patients with the same anatomical diagnosis may require different visit intervals, investigations and procedural planning because their physiological stages differ.',
  'Reassess stage when status changes, and investigate the cause rather than merely changing a label. The framework supports judgment; it does not replace lesion-specific management or evaluation of acquired disease.',
  'A small incidental congenital defect does not account for every later symptom. Conditions such as coronary disease, renal dysfunction or acquired valve disease need assessment under their own relevant guidance. Record the anatomical diagnosis and current physiological findings explicitly so the classification remains interpretable.')],
 ['ACHD2025','AP2025'],table=(['Stage','2025 physiological criteria'],[
 ('A','Asymptomatic; no anatomical/hemodynamic sequelae or sustained arrhythmia; normal exercise capacity and pulmonary pressure.'),
 ('B','Mild ventricular enlargement/dysfunction or native valve disease; normally functioning prosthetic valve; insignificant shunt; stable arrhythmia without treatment change for 12 months; pacemaker/ICD without ICD therapy for 12 months.'),
 ('C','BNP/NT-proBNP ≥2× upper normal limit; significant shunt; resting saturation 86–92%; at least moderate valve disease or ventricular dysfunction; low-risk PAH; sustained/high-burden tachyarrhythmia needing drugs, ablation, cardioversion or ICD therapy within 12 months.'),
 ('D','Heart-failure admission or endocarditis within 12 months; Eisenmenger syndrome; NYHA III/IV; recurrent hemodynamically important/refractory arrhythmia; resting saturation ≤85%; intermediate/high-risk PAH.')])))

rows.append(Q('Other important congenital lesions','Adult ALCAPA and Restoration of Coronary Supply',
 'An asymptomatic 30-year-old is found to have the left coronary artery originating from the pulmonary artery. There are extensive right-to-left coronary collaterals and retrograde flow into the pulmonary artery. LV ejection fraction is 58%. Which strategy is most appropriate?',
 'Refer for surgical restoration of a two-coronary system',[
 ('Observe until LV ejection fraction falls because collateral supply is currently adequate','Collateral development explains survival into adulthood but does not eliminate ischemic or sudden-death risk. Preserved ejection fraction is not a reason to defer the recommended repair of ALCAPA until myocardial damage develops.'),
 ('Use a negative stress study as the criterion for avoiding repair','Stress imaging can help assess ischemia and myocardial consequences. A negative result does not reliably establish long-term safety in ALCAPA, and the surgical recommendation is not contingent on demonstrating inducible ischemia.'),
 ('Close the pulmonary origin alone and retain collateral-dependent single-coronary supply','Eliminating runoff can be part of reconstruction, but ligation alone leaves the left coronary territory dependent on collateral supply. The operative objective is a reliable two-coronary circulation, with the technique chosen for the anatomy.')],
 [S('Why Adult Survival Does Not Establish Safety',
  '**ALCAPA connects the left coronary circulation to the pulmonary artery rather than the aorta.** After pulmonary pressure falls, adequate antegrade systemic-pressure coronary perfusion is lost.',
  'Adults who survive commonly have extensive collaterals from the right coronary artery. Blood can pass through these channels into the left coronary system and run off into the low-pressure pulmonary artery. This creates a coronary steal pathway and can leave myocardium vulnerable despite a normal resting ejection fraction.',
  'Clinical manifestations include ischemia, ventricular dysfunction, mitral regurgitation and arrhythmia. Mitral regurgitation may reflect ischemic papillary dysfunction or ventricular remodeling rather than a primary congenital leaflet abnormality.'),
  S('Define Anatomy and Myocardial Consequences',
  '**Cross-sectional coronary imaging establishes the origin and course.** Echocardiography evaluates ventricular and valve function and may demonstrate an enlarged right coronary artery or abnormal flow.',
  'CMR can assess ventricular function and scar; functional ischemia testing provides additional information but should not be used as a stand-alone guarantee against future events. Coronary anatomy, collateral pathways and myocardial viability inform the repair plan.'),
  S('Surgical Goal and Follow-Up',
  '**Current ACHD guidance recommends surgery for adults with ALCAPA.** Restore a two-coronary system, usually by reimplantation when anatomically feasible or another suitable reconstructive approach.',
  'The precise operation depends on the distance and relationship of the anomalous origin to the aorta and surrounding structures. Closing the pulmonary origin without securing an adequate independent left-coronary supply is not the general objective.',
  'Assess associated mitral disease and ventricular injury during planning. After repair, follow coronary patency, ventricular recovery, residual mitral regurgitation and arrhythmias. Established scar may persist even when perfusion improves, so successful reconstruction does not remove the need for surveillance.')],
 ['ACHD2025','ESC2020']))
