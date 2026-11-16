"""Ebstein anatomy and operation-specific transposition complications."""
from qbank_json_chapters import question as Q
REFERENCES={
 'CCS2022':('Canadian Cardiovascular Society ACHD intervention guideline, 2022','https://www.cachnet.org/wp-content/uploads/2023/11/CCS-2022-ACHD-Guideline.pdf'),
 'AHA_CPET':('AHA statement: cardiopulmonary exercise testing in congenital heart disease, 2025','https://pmc.ncbi.nlm.nih.gov/articles/PMC12074744/'),
}
def S(h,t,*children):return h,[(t,list(children))]
rows=[]
def add(*args,**kwargs):rows.append(Q(*args,**kwargs))

add('Ebstein anomaly','Indexed Tricuspid Displacement and Ebstein Anatomy',
 'A 25-year-old with severe tricuspid regurgitation has a septal tricuspid leaflet hinge point 18 mm apical to the anterior mitral leaflet insertion in the four-chamber view. Body surface area is 1.8 m². Which structural diagnosis is best supported?',
 'Ebstein anomaly',[
 ('Isolated tricuspid valve dysplasia without Ebstein displacement','Congenital dysplasia can cause severe regurgitation with thickened or poorly mobile leaflets. The supplied indexed apical displacement is 10 mm/m², supporting an Ebstein-type displaced attachment rather than an isolated normally inserted dysplastic valve.'),
 ('Atrial functional tricuspid regurgitation','Right atrial and annular dilation can cause functional regurgitation, often with atrial fibrillation. It does not explain marked congenital apical displacement of the septal leaflet attachment.'),
 ('Ventricular functional tricuspid regurgitation','RV remodeling and papillary displacement can tether leaflets and produce secondary regurgitation. Tethering of a normally attached valve should be distinguished from the measured apical hinge-point displacement of Ebstein anatomy.')],
 [S('Measurement and Functional Anatomy',
  '**Index the septal leaflet displacement to body surface area.** Here 18/1.8 = 10 mm/m²; an adult displacement of at least 8 mm/m² supports Ebstein anomaly in the appropriate imaging context.',
  'Measure the septal tricuspid hinge relative to the anterior mitral insertion in a suitable four-chamber view. A raw millimeter threshold without body-size indexing is not equivalent. Confirm leaflet morphology and attachment rather than inferring the diagnosis from regurgitation severity alone.',
  'The displaced valve divides the morphological RV into an atrialized proximal segment and a smaller functional distal RV. The right atrium can become markedly enlarged. Functional output depends on both valve competence and the remaining RV, not simply on the total apparent right-sided chamber size.'),
  S('Associated Findings and Management Assessment',
  '**Evaluate atrial communication, cyanosis and accessory pathways.** Elevated right atrial pressure can drive right-to-left passage through a PFO or ASD, while accessory pathways can cause reentrant tachycardia.',
  'Echocardiography defines valve anatomy and flow; CMR helps quantify functional RV anatomy and systolic performance when needed. Serial symptoms, objective exercise capacity, regurgitation and ventricular response guide specialist repair assessment.',
  'Cone reconstruction is an established valve-preserving approach in suitable anatomy. The 2025 guideline recommends surgery for at least moderate tricuspid regurgitation with heart failure, worsening exercise capacity or progressive RV systolic dysfunction. Thus, severe regurgitation is not an obligatory prerequisite when these consequences are present.',
  'In an asymptomatic patient with at least moderate regurgitation, progressive RV enlargement, right-to-left atrial desaturation, recurrent arrhythmia or paradoxical embolism can also support intervention. An atrial communication should not be closed in isolation without considering whether the right ventricle tolerates the additional filling load.')],
 ['ESC2020','CCS2022','ACHD2025'])

add('Ebstein anomaly','Accessory-Pathway Assessment Before Tricuspid Repair',
 'An adult with Ebstein anomaly is being assessed for tricuspid valve surgery. The ECG shows ventricular pre-excitation, although the patient reports no sustained palpitation. Which additional step is best supported before the operation?',
 'Expert electrophysiological study to assess accessory pathways and potential ablation',[
 ('Ambulatory monitoring alone, reserving pathway assessment for documented sustained tachycardia','Ambulatory monitoring can document intermittent arrhythmia but does not reliably define antegrade accessory-pathway risk or exclude multiple pathways. Current guidance supports EP assessment for asymptomatic pre-excitation in Ebstein anomaly.'),
 ('Proceed with valve repair and defer pathway assessment until after surgery','Valve surgery may alter or impede catheter access to relevant right-sided substrates. The absence of reported sustained tachycardia does not remove the rationale for assessing manifest pre-excitation before repair.'),
 ('Begin an AV-nodal blocking drug as definitive management of the pre-excitation','AV-nodal blockers treat selected regular supraventricular rhythms but do not eliminate an accessory pathway. They can be hazardous in pre-excited AF, where conduction over the pathway may accelerate ventricular activation.')],
 [S('Risk Beyond Symptom Frequency',
  '**Ebstein anomaly is associated with accessory atrioventricular pathways, sometimes multiple.** A patient can have clinically important antegrade conduction without a reliable history of sustained palpitations.',
  'The pathway can support AV reentrant tachycardia. During atrial fibrillation, rapid antegrade conduction over a high-risk pathway can produce dangerous ventricular rates. A resting tracing identifies pre-excitation but does not provide the complete risk assessment.'),
  S('Sequence Assessment With Valve Treatment',
  '**The 2025 ACHD guideline recommends EP study for symptomatic arrhythmia or asymptomatic ventricular pre-excitation in Ebstein anomaly.** The aim is to identify substrates suitable for ablation, including multiple or high-risk pathways.',
  'High-risk accessory conduction or multiple pathways supports ablation. Before tricuspid surgery, an expert EP approach is useful because repair can make later access to pathways and other arrhythmia substrates more difficult. The precise ablation plan is based on mapping and conduction properties, not on an assumption that every delta wave has identical risk.',
  'Acute management still depends on rhythm and stability. Hemodynamic instability warrants synchronized cardioversion; irregular pre-excited tachycardia should not be treated with isolated AV-nodal blockade. Long-term successful pathway ablation does not correct severe tricuspid regurgitation, so structural and electrical treatment remain coordinated parts of the same care plan.')],
 ['ACHD2025','ESC2020'])

add('Transposition and systemic right ventricle','Exertional Desaturation After an Atrial Switch',
 'A 38-year-old underwent a Senning operation for d-TGA. Resting saturation is 96%, falling reproducibly to 84% on exercise. Systemic RV function is unchanged, with no important new valve regurgitation or pulmonary disease. Which residual lesion should be specifically sought?',
 'A baffle leak allowing systemic venous blood to reach the systemic arterial circuit',[
 ('Isolated systemic venous baffle stenosis without a leak','Baffle stenosis can restrict preload, cause venous congestion and reduce exercise output. Without a communication or another source of admixture, obstruction alone does not directly explain systemic arterial desaturation.'),
 ('Isolated systemic tricuspid regurgitation without a shunt','Systemic AV-valve regurgitation contributes to systemic RV failure and exercise intolerance. It does not directly mix desaturated venous blood into the arterial circuit, and no important new regurgitation is present here.'),
 ('Isolated chronotropic incompetence from sinus-node dysfunction','Sinus-node dysfunction is common after atrial switch and can limit cardiac output during exercise. It usually produces an inadequate heart-rate response rather than a reproducible arterial oxygen-saturation fall of this magnitude.')],
 [S('Follow the Surgically Redirected Blood',
  '**Mustard and Senning procedures redirect venous return within the atria.** The morphological RV still pumps to the aorta, and the morphological LV remains subpulmonary.',
  'The systemic venous baffle normally channels caval blood toward the mitral valve and LV. A leak can permit desaturated systemic venous blood to enter the pulmonary venous atrium, then the systemic RV and aorta. Pressure relationships during exercise can make desaturation more evident than at rest.'),
  S('Imaging and Intervention Assessment',
  '**Define both baffle integrity and patency.** Contrast echocardiography, CMR and selected transesophageal or catheter assessment answer complementary questions about communication, obstruction and flow.',
  'An arm injection can miss an inferior systemic venous baffle leak; injection site should match the anatomy being interrogated. CMR also assesses systemic RV volumes, function and associated lesions. A negative limited study should not be treated as proof that every baffle segment is normal.',
  'A symptomatic leak requires congenital specialist assessment for closure when appropriate, with evaluation of the hemodynamic consequences. Before transvenous device leads, assess leaks and obstruction because systemic embolic risk and venous access issues may alter the procedure. Lifelong review also looks for systemic RV failure, systemic tricuspid regurgitation, atrial tachyarrhythmia and sinus-node disease.')],
 ['ESC2020','ACHD2025','AHA_CPET'])

add('Transposition and systemic right ventricle','Coronary Assessment After an Arterial Switch',
 'A stable 29-year-old who had an arterial switch for d-TGA develops exertional chest pressure with new regional LV dysfunction. TTE shows no major neoaortic valve lesion. Renal function is normal. Which targeted investigation most directly defines a surgically related coronary anatomical cause?',
 'Coronary CT angiography focused on the reimplanted coronary origins and proximal course',[
 ('Vasodilator stress CMR focused on myocardial perfusion','Stress CMR can assess inducible ischemia and may be needed to determine functional significance. A perfusion-focused study does not directly map the reimplanted ostia and proximal course as requested; a dedicated coronary CMR protocol is a different investigation.'),
 ('Exercise stress echocardiography focused on inducible wall-motion abnormalities','Stress echocardiography can identify a functional ischemic response. It does not usually define the transferred coronary origins and their proximal anatomical relation to reconstructed great vessels.'),
 ('Exercise ECG focused on reproducible ST-segment changes','Exercise ECG can relate symptoms to exertion and identify an ischemic electrical response. It does not show ostial narrowing or the proximal surgical coronary course, so it cannot directly resolve the anatomical question.')],
 [S('Repair Determines the Late Complication',
  '**An arterial switch moves the great arteries and transfers the coronary arteries to the neoaorta.** The LV becomes the systemic ventricle, unlike the systemic RV after an atrial switch.',
  'Late coronary ostial narrowing, kinking or another proximal abnormality can cause ischemia. New symptoms, ventricular dysfunction or ventricular arrhythmia should prompt focused evaluation rather than reassurance based on young age and a low atherosclerotic risk profile.'),
  S('Anatomical and Functional Evaluation',
  '**Current ACHD guidance supports coronary evaluation when symptoms suggest ischemia after arterial switch.** CT usually provides the initial focused anatomical assessment; dedicated CMR or invasive angiography can be appropriate depending on the question and patient.',
  'Anatomical imaging defines the origins, proximal course and relation to the reconstructed great vessels. Functional perfusion assessment or catheter investigation may still be needed if symptoms persist despite unrevealing cross-sectional findings, because dynamic obstruction or functional significance can remain uncertain.',
  'The stable vignette asks for a targeted anatomical test. An acute coronary syndrome or unstable presentation instead requires urgent clinical management. Ongoing surveillance also includes the neoaortic root and valve, neopulmonary outflow and branch pulmonary arteries. The Lecompte-related arterial relationships and coronary transfer make this a different follow-up problem from atrial baffle obstruction or leak.')],
 ['ACHD2025','ESC2020','AHA_CPET'])

add('Transposition and systemic right ventricle','Systemic AV-Valve Disease in Congenitally Corrected TGA',
 'An unoperated adult has AV discordance and ventriculoarterial discordance. The left-sided ventricle has coarse trabeculations and a moderator band, and ejects into the aorta. New complete AV block accompanies worsening systemic AV-valve regurgitation. Which valve and ventricle form the systemic pump?',
 'Morphological tricuspid valve and morphological right ventricle',[
 ('Morphological mitral valve and morphological left ventricle','That is the usual systemic pump and the expected arrangement after a successful arterial switch with AV concordance. Here double discordance routes pulmonary venous blood through a morphological RV to the aorta.'),
 ('Morphological tricuspid valve and morphological left ventricle','Identify the ventricle by its morphology rather than left-right position. The moderator band and coarse trabeculation support an RV, and the AV valve connected to it is morphologically tricuspid.'),
 ('Morphological mitral valve and morphological right ventricle','An AV valve is named by its morphological ventricular connection, not merely by which side of the chest it occupies. In the supplied concordance pattern of valve-to-ventricular morphology, the systemic RV has a tricuspid inlet.')],
 [S('Two Discordances Restore the Sequence',
  '**In ccTGA, AV and ventriculoarterial discordance occur together.** Systemic venous blood reaches the pulmonary artery through the morphological LV, while pulmonary venous blood reaches the aorta through the morphological RV.',
  'The circulation is therefore physiologically in series, even though its connections are abnormal. Use segmental anatomy and ventricular markers; a left-sided chamber is not necessarily an LV. Associated VSD, pulmonary obstruction and an Ebstein-like systemic tricuspid valve can modify presentation.'),
  S('Conduction, Valve and Ventricular Surveillance',
  '**The systemic RV and its tricuspid valve face chronic systemic loading.** Regurgitation and ventricular dysfunction can reinforce each other, making serial valve and ventricular assessment essential.',
  'Abnormal conduction-system anatomy predisposes to AV block, which can develop without surgery. Symptomatic complete block requires urgent rhythm assessment and pacing planning. Pacing route, ventricular activation and the risk of dyssynchrony require congenital EP expertise; a routine device approach may not suit the anatomy.',
  'For symptomatic adults with severe systemic tricuspid regurgitation and normal or mildly impaired systemic RV function, the 2025 guideline recommends surgical tricuspid valve replacement. This is distinct from the valve-preserving cone-repair approach often used in ordinary Ebstein anatomy. Assess valve intervention before advanced irreversible systemic RV dysfunction when possible.',
  'Do not assume that evidence and thresholds for an ordinary systemic LV transfer unchanged. Follow-up also evaluates associated defects, arrhythmias and exercise capacity; the word corrected describes the circulatory sequence, not anatomical normality or freedom from lifelong complications.')],
 ['ESC2020','ACHD2025'])
