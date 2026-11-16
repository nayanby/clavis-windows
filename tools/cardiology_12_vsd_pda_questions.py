"""Ventricular and ductal shunts: sequential original adult CHD questions."""
from qbank_json_chapters import question as Q

REFERENCES={
 'VSD_MERCK': ('Merck Manual Professional: ventricular septal defect', 'https://www.merckmanuals.com/professional/pediatrics/congenital-cardiovascular-anomalies/ventricular-septal-defect-vsd'),
 'VSD_REVIEW': ('Diagnosis and Management of Ventricular Septal Defects, 2024', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11607469/'),
 'VSD_ACC': ('ACC clinical practice algorithm for VSD follow-up, updated 2026', 'https://www.acc.org/latest-in-cardiology/articles/2023/05/30/10/47/clinical-practice-algorithm-for-the-follow-up-of-unrepaired-and-repaired-ventricular-septal-defects'),
 'PDA_MERCK': ('Merck Manual Professional: patent ductus arteriosus', 'https://www.merckmanuals.com/professional/pediatrics/congenital-cardiovascular-anomalies/patent-ductus-arteriosus-pda'),
}
VSD='Ventricular septal defects'
PDA='Patent ductus arteriosus'
rows=[]

def S(h,t,*children):return h,[(t,list(children))]
def add(*args,**kwargs):rows.append(Q(*args,**kwargs))

add(VSD,'Restrictive VSD: Doppler Gradient Versus RV Pressure',
 'An adult has a left-to-right restrictive VSD with peak Doppler velocity 4.5 m/s. Simultaneous systolic systemic BP is 125 mmHg. There is no LV outflow or aortic obstruction. Using the simplified Bernoulli equation, what is the estimated RV systolic pressure?',
 '44 mmHg',[('81 mmHg',''),('125 mmHg',''),('206 mmHg','')],
 [S('Calculation',
   '**The measured VSD jet estimates the LV-to-RV pressure difference, not RV pressure itself.** The simplified Bernoulli equation is ΔP = 4v² when velocity is expressed in metres per second.',
   'Substitution: ΔP = 4 × (4.5)² = 4 × 20.25 = 81 mmHg. With no LV outflow obstruction, LV systolic pressure is approximated by systemic systolic pressure, 125 mmHg.',
   'Because flow is left to right, RV systolic pressure = LV systolic pressure − ΔP = 125 − 81 = 44 mmHg. Adding the gradient would reverse the direction implied by the measured jet.'),
  S('Interpretation and Limitations',
   '**A high-velocity restrictive jet can coexist with a loud murmur and a relatively small shunt.** Pressure restriction and volume restriction are related but not identical; ventricular size and flow quantify the volume burden.',
   'Doppler alignment and correct identification of the jet matter. If LV outflow obstruction is present, systemic pressure underestimates LV systolic pressure and cannot be substituted without accounting for the obstruction.',
   'An RV pressure estimate is not a pulmonary vascular resistance measurement. Pulmonary artery pressure can be inferred from RV systolic pressure only when there is no significant RV outflow or pulmonary valve obstruction. PVR additionally requires pulmonary pressure, left atrial/wedge pressure and pulmonary flow. Do not label a restrictive VSD as hemodynamically insignificant or diagnose pulmonary vascular disease from this calculation alone.')],
 ['VSD_REVIEW','ESC2020'],calculation=True)

add(VSD,'Aortic Cusp Prolapse in a Small VSD',
 'An adult has a small outlet VSD with Qp:Qs 1.2. Serial echocardiograms show aortic cusp prolapse with regurgitation progressing from mild to moderate. PVR is low. Which approach is most appropriate?',
 'Seek ACHD surgical review of VSD closure and valve preservation',[
  ('Continue surveillance until Qp:Qs reaches at least 1.5','A shunt-based threshold is useful for assessing volume overload but does not encompass the separate problem of progressive VSD-related aortic regurgitation. Waiting only for the flow ratio to rise can allow further valve injury.'),
  ('Plan VSD device closure without a strategy for the aortic valve','A catheter approach can be suitable for selected defect anatomy. An outlet lesion with cusp prolapse and evolving regurgitation requires explicit valve assessment; proximity to the aortic valve can make an isolated device plan unsuitable.'),
  ('Plan isolated aortic valve replacement while leaving the VSD open','Valve replacement may be appropriate for severe irreparable valve disease, but moderate regurgitation from cusp prolapse warrants assessment of valve preservation and correction of the responsible congenital lesion rather than default isolated replacement.')],
 [S('Anatomical Complication',
   '**An outlet or some perimembranous VSDs can lose support beneath an aortic cusp.** Cusp prolapse may create or worsen regurgitation even when the ventricular shunt is small.',
   'A smaller apparent shunt is not necessarily reassuring if prolapsing tissue is partly restricting the defect. Evaluate the aortic valve directly, including mechanism and progression of regurgitation, rather than following Qp:Qs alone.',
   'A new diastolic murmur, widening pulse pressure or evolving LV enlargement can accompany clinically important regurgitation. The absence of symptoms does not negate documented structural progression.'),
  S('Repair Assessment',
   '**Refer for ACHD surgical assessment when VSD-related aortic regurgitation is progressive.** The plan can address the defect and preserve or repair the valve when feasible; the required valve procedure depends on its actual damage.',
   'A standard device strategy must account for proximity to the aortic cusps and the conduction axis. Closing a hole while leaving important cusp distortion unaddressed may not solve the problem.',
   'Assess LV size and function, other lesions and pulmonary vascular status before intervention. Discuss residual regurgitation and long-term valve surveillance after repair. A small uncomplicated muscular VSD without valve disease or volume loading is a different setting in which observation can be appropriate. This question tests an associated-lesion indication rather than a rule that all restrictive defects should be closed.')],
 ['VSD_MERCK','VSD_REVIEW','ACHD2025'])

add(VSD,'VSD Closure: Left-Heart Volume Load and Lesion-Specific Risk',
 'Which adult VSD profile provides the strongest hemodynamic indication for closure evaluation? All have PVR 1.3 Wood units, no hypoxemia, and no aortic-regurgitation or endocarditis indication.',
 'Qp:Qs 1.8 with progressive LV dilatation attributable to the VSD',[
  ('Qp:Qs 1.2 with normal LV size and stable systolic function','This describes a small volume-restrictive shunt without chamber loading. Surveillance can be appropriate in the absence of a separate complication; it does not match the stronger flow-plus-volume-load indication.'),
  ('Qp:Qs 1.8 with normal LV size and no serial enlargement','The ratio suggests important flow, but the supplied profile lacks the important or progressive LV dilatation specified in the favorable hemodynamic closure pathway. Confirm the flow and chamber assessment rather than treating one number as the whole indication.'),
  ('Qp:Qs 1.2 with LV dilatation attributed to primary cardiomyopathy','LV enlargement must be related to the congenital shunt to support this indication. A small shunt does not automatically explain a cardiomyopathic LV, and closure should not be expected to reverse the unrelated myocardial disease.')],
 [S('Volume Recirculation',
   '**A VSD increases pulmonary venous return to the LA and LV.** This differs from the characteristic RA/RV volume loading of a significant atrial-level shunt.',
   'In the favorable low-PVR setting, Qp:Qs at least 1.5 with important or progressive LV dilatation supports closure evaluation under the current ACHD framework. The selected profile has both flow and chamber-loading evidence.',
   'Do not use murmur intensity, anatomical diameter or preserved LVEF alone to classify the burden. Confirm that LV enlargement is attributable to the VSD rather than a competing valve or myocardial disease.'),
  S('Procedure and Additional Indications',
   '**Choose surgical or selected transcatheter treatment according to anatomy and associated lesions.** Consider aortic and tricuspid valves, conduction risk, RV outflow obstruction and any need for combined repair.',
   'Progressive VSD-related aortic regurgitation is a separate reason to consider repair. A recent history of infective endocarditis involving the VSD may also support closure after infection assessment and control; prevention of a first episode alone is not a closure indication.',
   'Raised PVR changes the decision, and a treatment response in VSD-associated PAH must not be given the same certainty as the ASD treat-and-repair pathway. Eisenmenger physiology is a nonclosure setting. Following any repair, assess residual shunt, ventricular remodeling, valve function, pulmonary pressure and conduction disease. A technically closed defect does not eliminate the need for an appropriate follow-up plan.')],
 ['ACHD2025','ESC2020','VSD_ACC'],style='direct')

add(VSD,'VSD With PAH: Uncertain Benefit After a Treatment Response',
 'A patient with a VSD has Qp:Qs 1.7 and no hypoxemia. PVR decreases from 6.5 to 4.4 Wood units with PAH therapy. Which statement best reflects the lesion-specific 2025 ACC/AHA recommendation?',
 'The usefulness of VSD closure remains uncertain and requires specialist assessment',[
  ('The response establishes the same routine closure indication as uncomplicated low-PVR VSD','A treatment-responsive higher-resistance presentation is not equivalent to a VSD with no PAH and favorable baseline physiology. The guideline identifies uncertainty for this treated VSD subgroup rather than a routine low-risk indication.'),
  ('The ASD treat-and-repair recommendation can be directly transferred to the VSD','Both lesions can produce pulmonary overcirculation, but their pressure loading, ventricular effects and evidence bases differ. The current guideline gives more cautious wording for a VSD in this resistance range after treatment.'),
  ('The fall below 5 Wood units establishes that PAH treatment can stop after closure','An improved PVR does not demonstrate cure of pulmonary vascular disease. Continued specialist PAH treatment and surveillance may remain necessary regardless of whether a selected intervention is eventually chosen.')],
 [S('Guideline Interpretation',
   '**For VSD with significant shunting, PVR initially 5 to less than 8 Wood units and no hypoxemia, the 2025 guideline describes closure usefulness as uncertain even if therapy lowers PVR below 5.** This is not the same wording as the selected ASD pathway.',
   'The question supplies a treatment response but does not convert limited evidence into a proven outcome benefit. Reassess invasive hemodynamics, ventricular function, clinical risk and the anatomy with congenital and PH specialists.',
   'Avoid a binary rule that every PVR above a single cutoff mandates repair or that every treatment responder has irreversible disease. Neither a favorable short-term pressure response nor a large shunt answers the whole risk question.'),
  S('Treatment and Follow-Up',
   '**The initial priority remains accurate PAH characterization and risk-directed therapy.** Review resting and exercise oxygenation, shunt direction, symptoms and evidence of RV failure before discussing intervention.',
   'Selected expert-center discussions may include a fenestrated approach, but procedural feasibility and published small series are not proof that this strategy improves long-term survival in every VSD patient.',
   'If intervention is deferred, continue specialist follow-up and indicated PAH therapy rather than treating nonclosure as absence of care. If intervention is chosen after individualized review, maintain surveillance for RV failure, persistent PAH and residual shunt. Established Eisenmenger physiology remains a different and hazardous closure setting. Communicate the uncertainty explicitly; a patient should not be promised that closure removes the pulmonary vascular disease or medication burden.')],
 ['ACHD2025','ESC2020'])

add(VSD,'Perimembranous VSD and the AV Conduction Axis',
 'When planning device closure of a perimembranous VSD, which adjacent structure most directly explains the concern about complete AV block?',
 'The AV conduction axis near the posteroinferior defect margin',[
  ('The distal right bundle branch after bundle bifurcation','A distal right-bundle lesion can produce right bundle-branch block. It does not by itself interrupt conduction to both ventricles; the high-grade AV-block concern relates to the more proximal AV conduction axis near the defect.'),
  ('The left anterior fascicle in the anterosuperior LV septum','Injury to this fascicle can cause a leftward or superior QRS axis with left anterior fascicular block. An isolated fascicular lesion does not explain the principal complete-AV-block risk at the perimembranous closure site.'),
  ('The left posterior fascicle in the inferoposterior LV septum','An isolated posterior fascicular lesion affects intraventricular activation and axis. It is not the main adjacent proximal conduction structure responsible for the known AV-block concern with perimembranous device closure.')],
 [S('Anatomy and Procedural Choice',
   '**The AV conduction axis runs close to the posteroinferior border of a typical perimembranous VSD.** Device pressure, local injury or subsequent tissue reaction can therefore impair AV conduction.',
   'Location matters: muscular, inlet, outlet and perimembranous defects do not share identical relationships to valves and conduction tissue. Detailed imaging and a baseline ECG inform procedural planning.',
   'Device sizing and design, tissue margins, aortic-valve proximity and associated lesions affect suitability. A high procedural success rate for one defect type should not be generalized to another anatomy.'),
  S('Monitoring and Late Complications',
   '**Assess conduction both immediately and during follow-up.** New PR prolongation, bundle-branch changes, syncope or bradycardia after repair deserves evaluation; conduction disease may not be limited to the procedure day.',
   'Hemodynamically significant high-grade block requires prompt rhythm monitoring and appropriate temporary or permanent pacing assessment. The need for pacing depends on persistence, timing and clinical circumstances, not simply on the presence of a VSD device.',
   'Surgery remains appropriate when the anatomy or associated aortic-valve disease favors it. Even a small residual shunt needs assessment in context, including hemolysis, infection risk and ventricular loading. Do not promise that choosing a catheter procedure removes surgical or electrophysiological risk. This anatomical concern is one reason perimembranous closure requires expertise and cannot be selected only from the shunt ratio.')],
 ['VSD_REVIEW','ACHD2025'],style='direct')

add(PDA,'Ductal Runoff and Left-Heart Volume Loading',
 'An adult with a substantial left-to-right PDA has bounding pulses and a continuous infraclavicular murmur. Which chamber-loading pattern is most characteristic of the shunt itself?',
 'Left atrial and left ventricular volume loading',[
  ('Right atrial and right ventricular volume loading','This is the characteristic primary pattern for a substantial atrial-level shunt. A PDA returns excess pulmonary flow through the pulmonary veins to the left heart; RV pressure effects can develop if pulmonary hypertension supervenes.'),
  ('Isolated right ventricular pressure loading with normal pulmonary flow','Isolated RV pressure loading suggests an obstructive or pulmonary vascular process rather than uncomplicated high-flow left-to-right ductal physiology. PDA can eventually cause PAH, but that is not the initial loading pattern described.'),
  ('Isolated left atrial pressure loading without LV volume recirculation','A mitral inflow obstruction can primarily raise LA pressure. With a PDA, the increased pulmonary venous return passes through the LA into the LV, so LV volume recirculation is central to the shunt physiology.')],
 [S('Pressure Gradient and Flow',
   '**A PDA connects the descending aorta to the pulmonary arterial circulation.** When systemic pressure exceeds pulmonary pressure throughout the cycle, flow persists in systole and diastole and can generate a continuous murmur.',
   'Aortic diastolic runoff contributes to widened pulse pressure and bounding pulses. Pulmonary overcirculation increases pulmonary venous return, producing LA and LV volume loading.',
   'A continuous murmur is not guaranteed in advanced pulmonary vascular disease: a reduced diastolic aortopulmonary gradient can attenuate its diastolic component. Murmur intensity alone is not a reliable measure of defect severity.'),
  S('Assessment and Competing Diagnoses',
   '**TTE should identify the ductal flow and assess the left-heart burden and pulmonary pressures.** CT or CMR can clarify adult anatomy when echocardiography is incomplete or procedural planning needs more detail.',
   'Distinguish PDA from an aortopulmonary window, coronary fistula, systemic arteriovenous fistula and other causes of continuous flow. The entry site, chamber-loading pattern and vascular anatomy are more discriminating than the descriptive word machinery.',
   'Catheterization is selected when pulmonary vascular disease or closure tolerance is uncertain. A suitable significant PDA with favorable pulmonary vascular physiology is often closed by catheter; advanced right-to-left ductal flow requires a different assessment. Follow ventricular remodeling and residual flow after intervention. The left-sided volume pattern links the clinical pulse findings to the actual recirculating flow rather than assuming that every systemic-to-pulmonary shunt first enlarges the right atrium.')],
 ['PDA_MERCK','ESC2020','ACHD2025'])

add(PDA,'Differential Cyanosis in Ductal Pulmonary Vascular Disease',
 'An adult has oxygen saturations of 97% in both hands and 83% in the feet, with toe clubbing but no finger clubbing. Arterial anatomy is otherwise usual. Which lesion with right-to-left flow best explains this pattern?',
 'Patent ductus arteriosus with advanced pulmonary vascular disease',[
  ('Atrial septal defect with advanced pulmonary vascular disease','Atrial-level right-to-left flow mixes with blood entering the systemic ventricle and generally desaturates upper and lower extremities. It does not selectively enter the descending aorta distal to the arm vessels.'),
  ('Ventricular septal defect with advanced pulmonary vascular disease','Ventricular right-to-left flow enters the systemic outflow before it supplies the arch vessels. Generalized rather than isolated lower-body cyanosis is the expected pattern in otherwise usual anatomy.'),
  ('Tetralogy of Fallot with severe RV outflow obstruction','Right-to-left flow across the VSD in TOF reaches the overriding aorta and systemic arterial tree. It causes systemic cyanosis, not the characteristic ductal lower-body desaturation with normally oxygenated hands.')],
 [S('Site of Desaturated Blood Entry',
   '**Right-to-left ductal flow can introduce desaturated pulmonary arterial blood into the descending aorta beyond the usual left subclavian origin.** The arch vessels supplying both hands can therefore receive better-oxygenated blood.',
   'Measure upper- and lower-extremity saturations when evaluating suspected ductal PAH. The persistent distribution of cyanosis and clubbing reflects the anatomical entry site rather than a local foot perfusion problem.',
   'Unusual arch anatomy, reversed connections or additional lesions can change the expected distribution; do not apply this pattern without considering the actual anatomy.'),
  S('Investigation and Closure Risk',
   '**Investigate ductal direction and pulmonary vascular physiology before contemplating closure.** Echo, appropriate cross-sectional imaging and specialist catheter assessment define the lesion and its consequences.',
   'A ductus that serves as an outlet in established Eisenmenger physiology must not be treated as an uncomplicated left-to-right PDA suitable for routine device occlusion. Abrupt removal of that outlet can worsen RV failure.',
   'Invasive oximetry and flow estimates require care because saturation may vary within the pulmonary artery and aorta. Use representative sampling and consider complementary flow assessment rather than assuming that a single arterial sample describes the entire systemic circuit. Management includes specialist PAH care and assessment of iron status, bleeding/thrombotic risk and exercise tolerance. The diagnostic value of the hand–foot difference is localization; it does not alone quantify resistance or prove that intervention will be tolerated.')],
 ['PDA_MERCK','ESC2020','ACHD2025'])

add(PDA,'Adult PDA: Selecting Definitive Closure',
 'A 33-year-old has a PDA with progressive LA/LV enlargement and a net left-to-right shunt. PVR is 1.2 Wood units. Ductal anatomy is suitable for a closure device and there is no associated indication for cardiac surgery. Which definitive approach is preferred?',
 'Transcatheter PDA device closure',[
  ('Surgical ligation through a thoracotomy','Ligation is an established treatment and remains useful when device anatomy is unsuitable or other clinical factors favor surgery. In this suitable adult lesion, the catheter approach generally avoids the additional morbidity of a surgical exposure.'),
  ('Surgical ductal division with open repair','Open repair can address anatomy unsuitable for catheter treatment or associated surgical disease. It is not the preferred initial approach when a device-suitable isolated PDA can be treated percutaneously.'),
  ('Surveillance without intervention until LV systolic function falls','Surveillance is appropriate for selected small or clinically insignificant lesions. Progressive left-heart enlargement attributable to a substantial shunt supports closure assessment before established LV systolic dysfunction develops.')],
 [S('Indication and Anatomical Suitability',
   '**Left-heart enlargement attributable to a PDA with favorable pulmonary vascular physiology supports closure.** The supplied progressive chamber load and low PVR make this different from an incidental tiny duct or advanced pulmonary vascular disease.',
   'The 2025 ACHD guideline generally prefers percutaneous closure when technically feasible. Measure ductal morphology, size, adjacent vessels and potential obstruction risk; adult calcification or unusual anatomy may alter the strategy.',
   'A Qp:Qs value alone is not the whole indication. Establish the direction of shunting, its chamber effect and whether pulmonary vascular disease changes the risk.'),
  S('Procedure, Monitoring and Higher-PVR Cases',
   '**Follow for residual flow, device position, hemolysis and adjacent aortic or pulmonary artery obstruction.** Review ventricular size and function as the chronic recirculating load resolves.',
   'For a PDA with PAH, expert assessment may include test occlusion. Symptoms, rising pulmonary pressure or falling aortic pressure during a selected test can signal intolerance; there is no single universally validated pass/fail rule.',
   'The 2025 pathway allows consideration of closure in selected net left-to-right PDA with PVR in the 2–5 Wood unit range in consultation with PH specialists. This must not be generalized to established right-to-left ductal Eisenmenger physiology. Surgery remains a valuable alternative for unsuitable anatomy, but merely being an adult does not make open treatment mandatory. Maintain follow-up and procedure-specific preventive care rather than assuming that successful occlusion eliminates every later risk.')],
 ['ACHD2025','ESC2020','PDA_MERCK'])

rows[2]['table']=(['Shunt level','Usual primary volume-loaded chambers','Interpretation clue'],[
 ['ASD','RA and RV','Pulmonary flow murmur; assess atrial and pulmonary venous anatomy'],
 ['VSD','LA and LV','Jet velocity measures an LV–RV pressure difference, not shunt volume'],
 ['PDA','LA and LV','Continuous flow requires a persistent aortopulmonary gradient'],
])
