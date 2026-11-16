"""Compact teaching notes for ventricular/ductal shunts and outflow lesions."""
def B(label,*details):return ('**'+label+'**',list(details))

edits={
8:dict(sections=[
 ('Calculate RV Pressure',[
  B('VSD gradient = 4v² = 4 × 4.5² = 81 mmHg.'),
  B('No LV outflow obstruction: LV systolic pressure ≈ systemic pressure = 125 mmHg.'),
  B('Left-to-right jet: RV systolic pressure = 125 − 81 = 44 mmHg.')]),
 ('Interpretation and Limits',[
  B('The jet measures a pressure difference, not shunt volume.',
    'A restrictive defect can produce a loud high-velocity murmur despite limited volume overload.'),
  B('Check Doppler alignment and the systemic-pressure measurement.',
    'LV outflow obstruction invalidates simple substitution of systemic BP for LV pressure.'),
  B('RV pressure approximates PA pressure only without RV outflow obstruction.',
    'PVR requires pulmonary flow and mean PA/wedge pressures; this calculation cannot diagnose pulmonary vascular disease.')])],
 orderedSections=['Calculate RV Pressure']),
9:dict(sections=[
 ('Cusp Prolapse Despite a Small Shunt',[
  B('Outlet and some perimembranous VSDs undermine aortic cusp support.',
    'Prolapse may partly restrict the defect while worsening aortic regurgitation.'),
  B('2025 indication: progressive moderate or greater VSD-related AR supports closure assessment.',
    'Qp:Qs below 1.5 does not cancel this separate valve indication.')]),
 ('Repair Planning',[
  B('Define cusp injury, AR progression, LV size/function and pulmonary vascular status.'),
  B('Seek congenital surgical review for defect closure and valve preservation/repair.',
    'Choose the valve procedure according to actual damage; device proximity can threaten the cusp or conduction axis.'),
  B('Follow residual AR and ventricular response after repair.')])],
 orderedSections=['Repair Planning'],reasons=[
 'A flow threshold guides volume-overload decisions. Progressive VSD-related aortic regurgitation is an independent reason for repair assessment.',
 'Device closure suits selected anatomy. Outlet cusp prolapse requires explicit valve assessment, making an isolated device plan unsuitable.',
 'Replacement may suit severe irreparable valve disease. Moderate progressive cusp-prolapse AR favors assessment of valve preservation and the causal VSD.']),
10:dict(sections=[
 ('Hemodynamic Closure Indication',[
  B('Low PVR + Qp:Qs ≥1.5 + important/progressive LV dilation attributable to the VSD.',
    'Excess pulmonary flow returns to the LA/LV; ASD instead primarily volume-loads the RA/RV.'),
  B('Confirm attribution: exclude primary cardiomyopathy or valve disease.',
    'Murmur intensity, diameter and preserved EF do not quantify shunt burden.')]),
 ('Additional Indications and Procedure',[
  B('Progressive VSD-related AR and selected recent VSD-associated endocarditis may justify closure.',
    'Preventing a first IE episode alone is not an indication.'),
  B('Select surgery or catheter closure from anatomy, valve involvement and conduction risk.'),
  B('Elevated PVR requires a separate pathway; Eisenmenger physiology precludes closure.',
    'Follow residual shunt, ventricular remodeling, valves and AV conduction.')])],reasons=[
 'Qp:Qs 1.2 with a normal LV describes a small volume-restrictive lesion; observation fits unless another complication develops.',
 'A ratio of 1.8 warrants confirmation, but absent LV loading does not meet the specified flow-plus-chamber criterion.',
 'Cardiomyopathic dilation is not attributable to this small shunt; closure should not be expected to reverse primary myocardial disease.']),
11:dict(sections=[
 ('2025 VSD Treat-and-Repair Recommendation',[
  B('Qp:Qs ≥1.5; initial PVR 5–8 Wood units; no hypoxemia; treated PVR <5.',
    'Even with this response, usefulness of VSD closure remains uncertain.'),
  B('Do not transfer the more favorable selected-ASD recommendation to VSD.',
    'Different pressure loading and evidence bases matter.')]),
 ('Specialist Decision',[
  B('Repeat invasive flow/resistance assessment; review ventricular function, oxygenation and anatomy.'),
  B('Continue risk-directed PAH therapy and surveillance.',
    'A lower resistance does not prove cure or justify stopping treatment.'),
  B('Consider intervention only after individualized ACHD/PH discussion.',
    'Small series or fenestration feasibility do not prove universal survival benefit; established Eisenmenger remains a nonclosure setting.')])],
 orderedSections=['Specialist Decision'],reasons=[
 'A treated high-PVR presentation is not equivalent to uncomplicated low-PVR VSD; the guideline explicitly retains uncertainty.',
 'ASD and VSD share excess pulmonary flow but differ in pressure loading and treatment evidence; their recommendations are not interchangeable.',
 'A PVR response is not proof of resolved arteriopathy; persistent PAH can require treatment after any selected closure.']),
12:dict(sections=[
 ('AV Conduction Anatomy',[
  B('The AV conduction axis lies near the posteroinferior margin of a typical perimembranous VSD.',
    'Device compression, injury or later tissue reaction may produce complete AV block.'),
  B('Risk depends on defect type, tissue margins, device design/sizing and valve proximity.')]),
 ('Procedure and Monitoring',[
  B('Map valves and defect anatomy; obtain a baseline ECG.'),
  B('Choose surgery when associated aortic-valve disease or anatomy favors repair.'),
  B('Monitor immediate and delayed conduction changes.',
    'New PR prolongation, bundle-branch change, syncope or bradycardia requires assessment.',
    'Significant high-grade block needs rhythm monitoring and temporary/permanent pacing assessment according to persistence and clinical status.'),
  B('Also assess residual shunt, hemolysis, infection risk and ventricular load.')])],
 orderedSections=['Procedure and Monitoring'],reasons=[
 'Isolated distal right-bundle injury causes RBBB, not interruption of conduction to both ventricles through the proximal AV axis.',
 'Left anterior fascicular injury changes axis and intraventricular activation; it does not explain the principal complete-AV-block risk.',
 'Isolated posterior fascicular injury affects activation/axis. The adjacent proximal AV conduction axis is the relevant complete-block hazard.']),
13:dict(sections=[
 ('Ductal Recirculation',[
  B('Aorta → pulmonary artery → lungs → LA/LV: primary left-heart volume loading.',
    'Diastolic runoff produces bounding pulses and widened pulse pressure.'),
  B('Continuous murmur requires an aortopulmonary gradient in systole and diastole.',
    'Advanced pulmonary vascular disease can reduce its diastolic component.')]),
 ('Investigation and Treatment',[
  B('TTE: ductal flow, LA/LV size and pulmonary pressure.',
    'CT/CMR clarifies complex adult anatomy; catheterization assesses uncertain PVR/closure tolerance.'),
  B('Suitable significant left-to-right PDA with favorable PVR: catheter closure.',
    'Right-to-left Eisenmenger physiology requires nonclosure and specialist PAH care.'),
  B('Differentiate coronary fistula, aortopulmonary window and systemic AV fistula by entry site and chamber load.')])],
 flow=['Aortic runoff','Pulmonary flow ↑','Pulmonary venous return ↑','LA/LV volume load ↑'],reasons=[
 'RA/RV volume loading is typical of an atrial-level shunt. A PDA primarily recirculates blood through the LA/LV.',
 'Isolated RV pressure overload suggests obstruction or pulmonary vascular disease; uncomplicated PDA initially increases pulmonary flow and LV volume.',
 'Mitral inflow obstruction primarily raises LA pressure. PDA flow passes through the LA into the LV, creating volume recirculation.']),
14:dict(sections=[
 ('Differential Cyanosis',[
  B('Right-to-left PDA flow enters the descending aorta beyond the usual left subclavian origin.',
    'Hands remain better oxygenated; feet develop desaturation and clubbing.'),
  B('Measure both upper- and lower-limb saturation.',
    'Unusual arch anatomy or additional connections can alter the distribution.')]),
 ('Assess Before Considering Closure',[
  B('Define ductal direction, pulmonary resistance and ventricular function with imaging and selected catheterization.'),
  B('Established ductal Eisenmenger: do not close the pressure-relief pathway.',
    'Abrupt removal can worsen RV failure.'),
  B('Sample oximetry carefully: PA and aortic saturation may vary by site.',
    'The hand–foot difference localizes entry; it does not quantify PVR or demonstrate closure tolerance.'),
  B('Provide PAH care and assess iron, bleeding/thrombosis and exercise status.')])],
 orderedSections=['Assess Before Considering Closure'],reasons=[
 'Atrial right-to-left flow mixes before systemic ejection, usually desaturating both upper and lower limbs rather than only the feet.',
 'Ventricular shunting reaches the aorta before the arch branches; generalized cyanosis is expected in otherwise usual anatomy.',
 'TOF shunting enters the overriding aorta and systemic circulation broadly; it does not selectively desaturate the postductal lower body.']),
15:dict(sections=[
 ('When and How to Close',[
  B('Attributable progressive LA/LV enlargement + net left-to-right flow + favorable PVR supports closure.'),
  B('Prefer percutaneous closure when technically feasible.',
    'Assess morphology, calcification, adjacent vessels and device-related obstruction risk.',
    'Surgery suits unsuitable catheter anatomy or associated surgical lesions.')]),
 ('After Closure and Higher-PVR Cases',[
  B('Monitor residual flow, hemolysis, device position and adjacent PA/aortic obstruction.'),
  B('Follow LV size/function as recirculating volume falls.'),
  B('Selected left-to-right PDA with PVR 2–5 Wood units: discuss with PH experts.',
    'Test occlusion may help; symptoms, rising PA pressure or falling aortic pressure suggest intolerance.',
    'No universal test-occlusion cutoff; do not extrapolate to right-to-left Eisenmenger physiology.')])],
 orderedSections=['After Closure and Higher-PVR Cases'],reasons=[
 'Surgical ligation is established for unsuitable device anatomy. A suitable isolated adult PDA generally favors the less invasive catheter approach.',
 'Open division treats difficult ductal or associated surgical anatomy; those features are absent in this device-suitable isolated lesion.',
 'Observation suits insignificant shunts. Progressive attributable left-heart enlargement supports closure before established LV systolic dysfunction develops.']),
16:dict(sections=[
 ('Image the Aorta, Not Only the Gradient',[
  B('CMR maps arch geometry, repair site, collaterals and aneurysm without radiation.',
    'CTA is an alternative; stent artifact or integrity assessment may favor CT.'),
  B('A normal Doppler gradient does not exclude repair-site aneurysm.',
    'Assess root/ascending aorta and associated bicuspid valve disease.')]),
 ('Lifelong Surveillance',[
  B('Check arm/leg BP, LV remodeling, valves and symptoms.',
    'Ambulatory BP or exercise testing can reveal masked pressure burden.'),
  B('ESC 2024: CT/CMR every 3–5 years, adjusted for anatomy and prior findings.',
    'Residual narrowing, dilation or new symptoms require earlier evaluation.'),
  B('2025: brain MR/CT angiographic aneurysm screening may be considered.',
    'Individualize by age, hypertension and preferences; thoracic imaging does not screen the brain.')])],reasons=[
 'TTE assesses valves and flow, but repeated Doppler cannot resolve the already poorly visualized repair wall and arch anatomy.',
 'TEE visualizes selected thoracic segments but has blind spots; it is less comprehensive for this arch, repair-site and collateral survey.',
 'Abdominal/renal duplex assesses distal flow and selected hypertension causes; it cannot adequately survey the thoracic repair site.']),
17:dict(sections=[
 ('Why a Low Gradient Can Mislead',[
  B('Collaterals bypass the narrowing and reduce measured pressure drop.',
    'Low cardiac output or severe aortic stenosis can also attenuate the gradient.'),
  B('Isthmus ratio = 7/20 = 0.35: substantial anatomical narrowing.',
    'A ratio below 0.5 is a conventional major-narrowing marker, not an isolated intervention command.')]),
 ('Integrated Assessment',[
  B('Combine hypertension, LV load, symptoms, cross-sectional anatomy and stated gradient type.',
    'Doppler maximum instantaneous and catheter peak-to-peak values are not interchangeable.'),
  B('Radiofemoral delay and inferior rib notching reflect chronic obstruction/collaterals.',
    'Notching typically involves ribs 3–8; pre/poststenotic contours can form a figure-of-3 sign.'),
  B('Severe anatomy with consequences merits ACHD repair assessment despite a 12-mmHg gradient.')])],reasons=[
 'Gradient depends on flow; extensive collaterals can conceal severe anatomical narrowing despite a low catheter measurement.',
 'Maximum instantaneous Doppler and catheter peak-to-peak gradients measure different pressure relationships and cannot be substituted directly.',
 'Collaterals can also reduce arm–leg BP difference; this does not exclude coarctation-related hypertension when severe anatomy is present.']),
18:dict(sections=[
 ('Select the Repair',[
  B('Hypertension + significant obstruction + suitable landing zones/access favors adult stent repair.',
    'ESC 2020: stenting is first choice in many ACHD centers for suitable native/recurrent lesions.',
    'Covered stents are often preferred; anatomy determines device selection.'),
  B('Map arch, branch vessels, aneurysms, collaterals and access arteries.')]),
 ('Risks and Follow-Up',[
  B('Discuss aortic injury/aneurysm, migration/fracture, access complications and reintervention.'),
  B('Surgery remains appropriate for complex arch disease, unsuitable landing zones or combined lesions.'),
  B('Repair does not guarantee normal BP: continue treatment and imaging.',
    '2025 US guidance permits surgical or transcatheter repair by experts and targets systolic BP <130 mmHg, adjusted for tolerance.')])],reasons=[
 'Balloon dilation has selected roles, including stent redilation; native adult lesions generally benefit from stent support against recoil.',
 'Interposition grafting is a valid surgical option for unsuitable catheter anatomy; the supplied landing zones and access favor stenting.',
 'Ascending-to-descending bypass can treat complex arch disease. It is not the usual first repair for this discrete stent-suitable lesion.']),
19:dict(sections=[
 ('Doppler Versus Catheter Measurement',[
  B('Doppler mean systolic gradient best approximates catheter peak-to-peak gradient in the 2025 framework.'),
  B('Catheter peak-to-peak compares separate systolic peaks; Doppler maximum uses an instantaneous difference.',
    'The relationship is empirical; values are not identical in every patient.')]),
 ('Avoid Misclassification After Repair',[
  B('High Doppler gradient without narrowing: consider compliance and pressure recovery.'),
  B('Low gradient despite narrowing: consider collaterals or low output.'),
  B('Correlate with CT/CMR anatomy, LV function, arm/leg BP and symptoms.',
    'Account for proximal velocity and Doppler alignment; state the measured index.',
    'Do not select reintervention from a single peak velocity; continue aneurysm and hypertension surveillance.')])],reasons=[
 'Maximum instantaneous gradient can exceed peak-to-peak pressure difference; it is not the closest named Doppler approximation.',
 'Proximal-velocity correction reduces one error but leaves a maximum instantaneous index, distinct from the catheter peak-to-peak measurement.',
 'A diastolic flow tail supports obstruction, but its peak gradient is not the systolic index used for this approximation.']),
20:dict(sections=[
 ('Localize the Pressure Step',[
  B('Proximal RV 78 → distal RV 26 → PA 24 mmHg: obstruction is within the RV.',
    'Double-chambered RV has obstructing muscle bundles, often with a perimembranous VSD.'),
  B('Define whether the VSD enters the high- or low-pressure compartment.',
    'TTE may miss the full partition; CMR/CT and selected catheterization clarify anatomy.')]),
 ('Treatment',[
  B('Symptomatic moderate-or-greater DCRV obstruction: surgical muscle-bundle repair.',
    'Assess associated VSD, valves, ventricular function and arrhythmia.'),
  B('Balloon pulmonary valvuloplasty does not remove muscular intracavitary obstruction.'),
  B('Severe asymptomatic obstruction also merits expert review.',
    'Follow residual/recurrent obstruction and RV remodeling; high proximal RV pressure is not automatically PAH.')])],reasons=[
 'Valvar PS creates a distal-RV-to-PA step. Here those pressures nearly match; the major step is proximal within the RV.',
 'Supravalvar stenosis is beyond the valve and raises upstream outflow pressure; it does not explain the intracavitary partition.',
 'Branch PA stenosis requires main-to-branch pressure/anatomical assessment. It does not primarily divide the RV into two pressure chambers.']),
21:dict(sections=[
 ('Family Screening',[
  B('2022 ACC/AHA: first-degree relatives need TTE when BAV coexists with aortic dilation.',
    'Assess valve morphology/function, root and ascending aorta.',
    'Aortopathy may occur with a tricuspid valve; normal examination is insufficient.'),
  B('Incomplete TTE visualization: complete imaging with CT or MRI.')]),
 ('Proband: Aortic Intervention Thresholds',[
  B('4.6 cm alone does not mandate isolated replacement; assess growth and risk.',
    'Rapid BAV growth: ≥0.3 cm in one year.',
    'Risk modifiers: family dissection, coarctation, root phenotype and body size.'),
  B('2022 ACC/AHA: operate at 5.5 cm; selected earlier surgery at 5.0–5.4 cm with additional risk.',
    'Area/height ≥10 cm²/m can support intervention.',
    '≥4.5 cm may justify concomitant replacement during aortic valve surgery; it is not a universal isolated-surgery threshold.')])],reasons=[
 'ECG and BP can identify other problems but cannot exclude bicuspid morphology or silent aortic enlargement.',
 'CTA is useful when echo is incomplete or specific anatomy requires it; TTE is the initial family-screening test.',
 'Genetic testing helps selected heritable disease, but many BAV families lack an identified variant; imaging cannot be restricted to carriers.']),
22:dict(sections=[
 ('Unrepaired TOF Hemodynamics',[
  B('Large VSD + RV outflow obstruction permit competing pulmonary and systemic ejection routes.'),
  B('Lower SVR makes systemic ejection easier: right-to-left shunt increases and saturation falls.',
    'The obstruction need not change; raising SVR can reduce shunting in an appropriate acute setting.')]),
 ('Anatomy and Clinical Implications',[
  B('Four components: malalignment VSD, RV outflow obstruction, overriding aorta and RV hypertrophy.'),
  B('Murmur usually comes from outflow obstruction, not the large low-gradient VSD.',
    'A quieter murmur during deterioration may mean less pulmonary flow.'),
  B('Assess oxygenation, vascular tone, hydration and filling during acute deterioration.',
    'Seek congenital expertise and definitive anatomical assessment; repaired-TOF scar/regurgitation physiology differs.')])],
 flow=['Systemic resistance ↓','RV-to-aorta ejection favored','Right-to-left flow ↑','Systemic saturation ↓'],reasons=[
 'Restrictive defects produce pressure-gradient-limited jets. This large nonrestrictive TOF VSD permits pressure communication and systemic diversion.',
 'Systemic arteriolar dilation does not remove fixed valvar or muscular RV outflow obstruction; pulmonary flow need not increase.',
 'Less RV-to-aorta diversion would improve saturation. With obstruction, lower SVR instead favors more desaturated systemic ejection.']),
23:dict(sections=[
 ('Scar-Related Macroreentry',[
  B('Patches, scars and valve annuli form fixed circuit boundaries; slow-conducting isthmuses sustain monomorphic VT.',
    'A key isthmus lies between the pulmonary annulus and VSD patch.'),
  B('Risk assessment integrates clinical VT/syncope, CMR scar and ventricular function.',
    'QRS ≥180 ms is a historical marker, not a stand-alone ICD rule.')]),
 ('Coordinated Treatment',[
  B('Congenital EP mapping identifies the critical isthmus for ablation.'),
  B('Assess residual pulmonary valve dysfunction and ventricular loading concurrently.'),
  B('Individualize ICD treatment from presentation, reversible causes and overall risk.',
    'Selected tolerated VT may have an ablation-led pathway in expert care.',
    'Successful ablation or valve replacement does not eliminate every future arrhythmic risk.')])],
 orderedSections=['Coordinated Treatment'],reasons=[
 'Triggered activity underlies idiopathic RVOT VT, often without scar; the supplied repaired-TOF substrate favors anatomical macroreentry.',
 'Bundle-branch reentry occurs with selected His–Purkinje disease; postrepair RBBB alone does not establish it as the dominant circuit.',
 'Focal automatic rhythms occur in other contexts but do not explain the common patch/isthmus-related sustained reentrant substrate.']),
24:dict(sections=[
 ('Native-RVOT Device Fit',[
  B('2025 guideline: cardiac CT for native-RVOT transcatheter pulmonary-valve suitability.',
    'Self-expanding device planning needs three-dimensional geometry across the cardiac cycle.'),
  B('Map landing zone, pulmonary arteries and coronary relationships.',
    'CMR already quantifies regurgitation, RV volumes and function; it answers complementary questions.')]),
 ('Coronary Safety and Procedure Selection',[
  B('RVOT expansion may compress an adjacent coronary artery.'),
  B('Selected balloon-expandable procedures use balloon testing with simultaneous coronary angiography.',
    'Device-specific assessment remains essential; no generic distance/test guarantees safety.'),
  B('Unsuitable landing anatomy, compression risk or associated surgical lesions may favor surgery.',
    'Discuss durability, endocarditis, residual obstruction/regurgitation and follow-up.')])],reasons=[
 'CMR angiography provides anatomy and flow without radiation, but CT supplies the recommended cycle-dependent self-expanding native-RVOT fit dataset.',
 'Three-dimensional TEE aids valve/procedural imaging; the anterior RVOT and full coronary relationships are less consistently characterized than by CT.',
 'Catheter angiography and balloon testing complement procedural safety assessment; they do not replace preprocedural CT self-expanding device-fit analysis.']),
25:dict(sections=[
 ('Pressure Load Despite Little Regurgitation',[
  B('RV/systemic systolic pressure = 90/120 = 0.75, exceeding two-thirds systemic.',
    'Low regurgitant fraction does not negate important obstructive dysfunction.'),
  B('Normal distal PA pressure localizes the pressure load to the RV outflow pathway.',
    'High RV pressure is not PAH when intervening obstruction is present.')]),
 ('Intervention Assessment',[
  B('Map valvar, muscular, conduit or branch-artery obstruction and its severity.'),
  B('Assess ventricular function, TR, rhythm and objective exercise change.'),
  B('Select catheter relief, valve intervention or surgery according to anatomy.',
    'Symptoms with important obstruction do not require waiting for severe PR or RV volume progression.'),
  B('Follow residual gradient, new PR and RV response; scar-related rhythm risk persists.')])],
 orderedSections=['Intervention Assessment'],reasons=[
 'Serial CMR suits uncertain stable indications. Symptoms and major pressure loading already warrant intervention assessment without proving further volume enlargement.',
 'Vasodilator testing addresses selected pulmonary vascular disease. Normal distal PA pressure and an RVOT pressure step identify mechanical obstruction here.',
 'Medication can optimize congestion but cannot relieve a fixed lesion; it should not impose a prerequisite delay before anatomical assessment.']),
}
