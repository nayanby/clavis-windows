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
 'Two adults have the same repaired congenital lesion. One has normal function and no significant sequelae; the other has recurrent hemodynamically important arrhythmia and recent heart-failure hospitalization. How should the ACHD anatomic-physiological framework represent this difference?',
 'Retain the lesion-based anatomical category while assigning different physiological stages',[
 ('Assign the same combined classification because the original lesion is identical','Anatomy is only one axis. Physiological status adds information about current clinical burden, so identical lesions do not require identical combined classifications or follow-up intensity.'),
 ('Move the patient with heart failure to a higher anatomical category','Heart failure changes physiological burden but does not itself change the underlying congenital anatomical diagnosis. Relabeling anatomical complexity would obscure the distinction the two-axis framework is designed to preserve.'),
 ('Classify both by current NYHA class alone and omit the anatomical category','Functional class contributes to assessment but does not encode the congenital connections, prior repair or all relevant physiological findings. Arrhythmia, ventricular disease, hypoxemia and recent events also matter.')],
 [S('Two Complementary Axes',
  '**Anatomical complexity and current physiological burden answer different questions.** The anatomical categories are I, simple; II, moderate complexity; and III, great complexity. Physiological stages range from A to D.',
  'Anatomy describes the congenital lesion and circulation. Physiology reflects current sequelae and clinical status and can change over time. Repair does not automatically reclassify every lesion as anatomically simple or establish physiological stage A.'),
  S('Use the Current Criteria',
  '**The 2025 framework refines the physiological criteria.** Review symptoms, ventricular and valve function, shunts, pulmonary vascular disease, oxygenation, rhythm and recent clinical events rather than relying on a single reassuring measurement.',
  'Stage A describes a patient without relevant symptoms or sequelae, with normal exercise capacity and pulmonary pressure and no sustained arrhythmia. Increasing stages incorporate clinically important abnormalities; recent heart-failure hospitalization and recurrent hemodynamically significant or refractory arrhythmia are stage D features in the updated framework.',
  'The time window and severity qualifications matter. For example, the updated criteria specify heart-failure hospitalization within the preceding 12 months. Do not substitute a vague lifetime history or copy an older staging table without checking the current definitions.'),
  S('Apply Classification to Care',
  '**The combined classification helps determine surveillance and specialist resource needs.** The two patients may require different visit intervals, investigations and procedural planning despite the same congenital diagnosis.',
  'Reassess stage when status changes, and investigate the cause rather than merely changing a label. The framework supports judgment; it does not replace lesion-specific management or evaluation of acquired disease.',
  'A small incidental congenital defect does not account for every later symptom. Conditions such as coronary disease, renal dysfunction or acquired valve disease need assessment under their own relevant guidance. Record the anatomical diagnosis and current physiological findings explicitly so the classification remains interpretable.')],
 ['ACHD2025','AP2025'],style='direct'))
