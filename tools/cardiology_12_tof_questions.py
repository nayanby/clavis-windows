"""TOF physiology, scar arrhythmia and RVOT intervention planning."""
from qbank_json_chapters import question as Q

REFERENCES={
 'TOF_MERCK': ('Merck Manual Professional: tetralogy of Fallot', 'https://www.merckmanuals.com/professional/pediatrics/congenital-cardiovascular-anomalies/tetralogy-of-fallot'),
 'TOF_ARRHYTHMIA': ('AHA scientific statement: arrhythmias in repaired TOF, 2022', 'https://doi.org/10.1161/HAE.0000000000000084'),
 'TOF_ISTHMUS': ('Anatomical substrates and ablation in repaired congenital heart disease', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5013179/'),
 'TPVR_CORONARY': ('Coronary compression during transcatheter pulmonary valve assessment: multicentre experience', 'https://pubmed.ncbi.nlm.nih.gov/24065444/'),
 'TPVR_CT': ('SCCT/CHSS/SCAI white paper on CT guidance of RVOT intervention, 2023', 'https://doi.org/10.1016/j.jcct.2023.06.005'),
}
TOPIC='Tetralogy of Fallot and repaired RV outflow physiology'
rows=[]
def S(h,t,*children):return h,[(t,list(children))]
def add(*args,**kwargs):rows.append(Q(*args,**kwargs))

add(TOPIC,'Systemic Resistance and Right-to-Left Flow in Unrepaired TOF',
 'An adult with unrepaired TOF and a large nonrestrictive VSD becomes more cyanotic after systemic vasodilation. RV outflow obstruction has not changed. Which hemodynamic change best explains the desaturation?',
 'Lower systemic resistance favors right-to-left flow through the VSD',[
  ('Lower systemic resistance increases the LV-to-RV gradient across a restrictive VSD','A small restrictive VSD behaves primarily as a pressure-gradient-limited jet. The supplied large nonrestrictive TOF defect permits pressure communication; lowering systemic afterload favors systemic ejection of desaturated RV blood rather than increasing a restrictive left-to-right jet.'),
  ('Lower systemic resistance directly relieves the fixed RV outflow obstruction','Systemic arteriolar dilation does not remove infundibular or valvar pulmonary obstruction. Even if ventricular loading changes, it cannot be assumed to increase pulmonary flow by mechanically relieving the lesion.'),
  ('Lower systemic resistance reduces the proportion of RV output entering the aorta','That direction would tend to improve systemic oxygenation. With substantial pulmonary outflow obstruction and a large VSD, a lower systemic resistance instead makes the systemic route relatively easier for RV ejection.')],
 [S('Competing Outflow Routes',
   '**The pulmonary and systemic outflow pathways compete in the presence of a large TOF VSD.** Significant RV outflow obstruction directs desaturated blood toward the overriding aorta.',
   'A fall in systemic vascular resistance can increase right-to-left flow without any change in the anatomical obstruction. Conversely, raising systemic resistance can reduce this diversion in an appropriate acute setting.',
   'The four defining components are a malalignment VSD, RV outflow obstruction, overriding aorta and RV hypertrophy. The degree of outflow obstruction and the resistance balance matter more for cyanosis than merely counting those components.'),
  S('Clinical Implications',
   '**Avoid assuming that a systemic vasodilator must improve oxygenation in every cyanotic patient.** Volume status, vascular tone, ventricular filling and the exact congenital connections determine the response.',
   'Hypotension, dehydration or an acute hypercyanotic episode requires prompt assessment of airway, oxygenation and hemodynamics with congenital expertise. A persistent unrepaired lesion merits full anatomical and physiological evaluation rather than symptom treatment alone.',
   'The murmur in uncomplicated TOF usually arises from outflow obstruction, not the large low-gradient VSD. Reduced murmur intensity during deterioration can reflect less pulmonary flow rather than improvement. Repaired TOF has a different balance of residual obstruction, pulmonary regurgitation and surgical scar; this unrepaired-shunt mechanism should not be transferred automatically to every postrepair episode of desaturation.')],
 ['TOF_MERCK','ESC2020'])

add(TOPIC,'Monomorphic VT After TOF Repair',
 'A 39-year-old with repaired TOF and an old RVOT patch has sustained monomorphic VT. CMR shows fibrosis near the patch and ventricular septal repair. Which mechanism most commonly explains this arrhythmia substrate?',
 'Macroreentry through slow-conducting anatomical isthmuses',[
  ('cAMP-mediated triggered activity in an otherwise structurally normal RVOT','Triggered idiopathic RVOT VT is a genuine mechanism and can occur without surgical scar. The repaired congenital substrate here instead favors scar- and anatomy-related slow-conduction circuits.'),
  ('Bundle-branch reentry using the His–Purkinje system as the principal circuit','Bundle-branch reentry occurs in selected patients with conduction disease and ventricular pathology. A postrepair RBBB alone does not establish that mechanism; anatomical isthmuses around patches and valve boundaries are the dominant substrate in repaired TOF.'),
  ('Enhanced automaticity from a single normal Purkinje focus','Automatic focal ventricular rhythms are possible in other settings. They do not explain the common stable macroreentrant substrate created by congenital anatomy, surgical boundaries and progressive fibrosis in repaired TOF.')],
 [S('Anatomical Substrate',
   '**Patches, valve annuli and surgical scars create nonconducting boundaries around potential VT isthmuses.** Progressive fibrosis and slow conduction can allow a macroreentrant circuit.',
   'A clinically important example lies between the pulmonary annulus and the VSD patch. The available pathways depend on the original anatomy and repair, so ablation planning needs the operative history and electroanatomical assessment.',
   'CMR scar, ventricular function, clinical VT and electrophysiological findings contribute to risk assessment. A historical QRS duration threshold of 180 ms is a risk marker, not an isolated rule deciding every patient’s ICD treatment.'),
  S('Management Implications',
   '**Congenital electrophysiology assessment integrates arrhythmia treatment with residual hemodynamic disease.** Ablation can target the critical slow-conducting isthmus; evaluate pulmonary valve dysfunction and ventricular loading at the same time.',
   'ICD decisions depend on the presenting event, ventricular function, reversible causes and the contemporary risk assessment. Successful ablation or pulmonary valve replacement must not be assumed to eliminate every future ventricular arrhythmia risk.',
   'Selected well-tolerated VT presentations may have individualized ablation and device pathways in expert care. Do not apply an automatic device rule from the presence of a long QRS alone. Conversely, syncope, sustained VT or resuscitated arrest should not be dismissed as the expected RBBB of repaired TOF. Long-term follow-up addresses both the electrical substrate and the changing ventricular physiology.')],
 ['TOF_ARRHYTHMIA','TOF_ISTHMUS','ACHD2025'])

add(TOPIC,'Cardiac CT Before Native-RVOT Transcatheter Pulmonary Valve Treatment',
 'A patient with repaired TOF and a native patched RVOT is being screened for a self-expanding transcatheter pulmonary valve. CMR has quantified pulmonary regurgitation and RV volumes. Which additional examination best supplies the recommended three-dimensional, cardiac-cycle-dependent device-fit assessment?',
 'Cardiac CT defining RVOT geometry and coronary relationships',[
  ('Contrast-enhanced CMR angiography of the RVOT and pulmonary arteries','CMR supplies valuable anatomy, flow and ventricular function without radiation. For the specified self-expanding native-RVOT device-fit assessment, ECG-gated CT is the recommended method for detailed geometry through the cardiac cycle and coronary relationships.'),
  ('Three-dimensional transesophageal echocardiography of the pulmonary outflow','TEE provides useful valve and procedural information. The anterior RVOT and its complete relationship to branch arteries and coronaries are not consistently characterized sufficiently for the requested device-fit analysis; CT provides the relevant volumetric dataset.'),
  ('Catheter RVOT angiography with balloon sizing and coronary angiography','Catheter angiography and selected balloon testing are important for procedural assessment, particularly balloon-expandable pathways and coronary-compression testing. They complement rather than replace the recommended preprocedural CT fit analysis for a self-expanding valve in a native patched RVOT.')],
 [S('Procedure-Specific Anatomy',
   '**The 2025 guideline recommends cardiac CT for repaired TOF with native RVOT anatomy when transcatheter pulmonary valve treatment is being considered.** The purpose is anatomical suitability, not replacement of the preceding CMR functional assessment.',
   'Define the intended landing zone, its dimensions and shape, pulmonary artery anatomy and the coronary course relative to the outflow tract. A favorable regurgitant fraction or RV volume does not by itself establish that a device can be implanted safely.',
   'CT planning and device selection are anatomy specific. A native patched RVOT and an RV-to-PA conduit do not have identical dimensions, mechanical constraints or procedural approaches.'),
  S('Coronary Compression and Alternative Repair',
   '**Expansion within the RVOT can compress a neighboring coronary artery.** The consequence can be acute ischemia, so coronary proximity is a central safety issue rather than an incidental imaging finding.',
   'Selected balloon-expandable conduit or RVOT procedures use test balloon inflation with simultaneous coronary angiography to assess compression. Apply the appropriate device-specific pathway; neither a generic negative test nor a simple coronary-distance estimate guarantees safety for every device.',
   'Demonstrated compression risk or unsuitable landing anatomy can favor surgical or another tailored approach. Assess associated lesions that may also need repair, and discuss valve durability, endocarditis, residual obstruction/regurgitation and follow-up. CT provides the device-fit dataset; complementary functional and invasive assessments remain relevant to the complete procedural decision.')],
 ['ACHD2025','TPVR_CORONARY','TPVR_CT'])

add(TOPIC,'Pressure-Loaded RV After TOF Repair',
 'An adult with repaired TOF has worsening exercise tolerance. CMR pulmonary regurgitant fraction is 12%, but imaging shows substantial RVOT obstruction. RV systolic pressure is 90 mmHg while systemic systolic pressure is 120 mmHg; distal PA pressure is not elevated. Which next approach is most appropriate?',
 'Refer for assessment of relief of the residual RVOT obstruction',[
  ('Repeat CMR after an interval to establish progressive RV volume enlargement','Serial CMR is useful in stable patients whose intervention indication remains uncertain, particularly with regurgitant volume loading. This patient already has worsening exercise tolerance and important obstructive pressure loading; documented volume progression is not a prerequisite for intervention assessment.'),
  ('Undertake pulmonary vasodilator testing to guide PAH-directed treatment','Invasive pulmonary vascular assessment can be appropriate when elevated distal pulmonary pressure and resistance suggest PAH. Here the high pressure is proximal to the RVOT obstruction and distal PA pressure is not elevated; testing a presumed pulmonary arteriopathy does not address the demonstrated mechanical load.'),
  ('Begin medical treatment for RV failure and reassess the obstruction after optimization','Medical optimization can support a patient with congestion or other ventricular failure contributors. It does not relieve a fixed outflow lesion, and the supplied presentation does not justify postponing anatomical intervention assessment for a mandatory drug trial.')],
 [S('Pressure Versus Volume Loading',
   '**Residual RVOT obstruction can create important pulmonary valve/outflow dysfunction despite little regurgitation.** Here RV pressure is 90/120 = 0.75 of systemic, exceeding two-thirds systemic pressure.',
   'Distinguish valvar, subvalvar, conduit and branch pulmonary arterial obstruction. Define where the pressure drop occurs and whether another lesion contributes to exercise limitation.',
   'A high RV pressure is not automatically pulmonary hypertension: obstruction between the RV and PA can generate the difference. Interpret tricuspid-regurgitation-derived RV pressure estimates within the known outflow anatomy.'),
  S('Intervention Assessment and Follow-Up',
   '**Symptoms with important residual obstruction warrant specialist repair assessment rather than waiting for severe regurgitation or advanced ventricular dilation.** The procedure depends on the actual level and anatomy of the lesion.',
   'Options may include catheter relief or valve intervention for a suitable target, while complex muscular, patched or associated lesions may favor surgery. CMR, CT, Doppler and selected catheter measurements answer complementary functional and anatomical questions.',
   'Review RV and LV function, tricuspid regurgitation, arrhythmias and objective exercise measurements. A fall in exercise capacity can result from multiple residual lesions, so intervention planning should not use a single number in isolation. After treatment, follow residual gradients, new or persisting regurgitation and ventricular response. Relief of the mechanical load does not remove the established scar-related arrhythmia substrate.')],
 ['ACHD2025','ESC2020'])
