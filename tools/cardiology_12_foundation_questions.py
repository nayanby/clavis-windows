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
