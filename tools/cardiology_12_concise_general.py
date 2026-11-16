"""Compact other-lesion, general-care and foundation notes."""
def B(label,*details):return ('**'+label+'**',list(details))
edits={
41:dict(sections=[
 ('Isolated Anomalous Pulmonary Venous Drainage',[
  B('Oxygenated pulmonary venous blood enters systemic veins, recirculating through RA/RV despite an intact atrial septum.',
    'Shunt burden depends on the number, size and lung territory of anomalous veins.'),
  B('2025: Qp/Qs <1.5 with normal/mildly enlarged RV → no surgical repair indication.')]),
 ('Surveillance and Related Anatomy',[
  B('Track symptoms, RV size/function and pulmonary pressures; CMR quantifies flow and maps veins.',
    'CT is an anatomical alternative; deterioration or significant volume loading prompts repair reassessment.'),
  B('Scimitar: right pulmonary vein usually drains to IVC.',
    'Curved right-border vein may accompany right-lung hypoplasia and abnormal systemic arterial supply.'),
  B('Repair can cause pulmonary/systemic venous obstruction or rhythm complications; establish benefit first.')])],reasons=[
 'Surgical redirection treats significant attributable loading, not every anatomical anomaly; this small stable shunt has no demonstrated repair benefit.',
 'Covered-stent correction applies to selected sinus venosus anatomy; an isolated anomalous vein with intact septum is a different target.',
 'Catheterization resolves suspected PAH or discordant hemodynamics. Clear stable CMR findings do not require invasion merely to justify observation.']),
42:dict(sections=[
 ('Appendage Landmark',[
  B('Cor triatriatum: proximal chamber receives pulmonary veins; distal chamber contains LAA and mitral valve.',
    'Small membrane openings obstruct pulmonary venous return and mimic mitral stenosis.'),
  B('Supramitral ring usually lies below the LAA, close to the valve.')]),
 ('Assess and Treat',[
  B('Echo/TEE: define membrane openings, gradient and valve anatomy.',
    'CT/CMR maps associated pulmonary veins and congenital lesions.'),
  B('Interpret gradients with flow, heart rate and symptoms; catheterize selected uncertain cases.'),
  B('Attributable symptomatic obstruction → surgical membrane resection.',
    'Severe asymptomatic obstruction merits expert assessment; nonobstructive incidental membranes may be observed.'),
  B('Diuretics relieve congestion temporarily; follow residual obstruction, pulmonary veins and rhythm.')])],orderedSections=['Assess and Treat'],reasons=[
 'A supramitral ring usually lies below the appendage; here the appendage is downstream with the mitral valve.',
 'Valvar stenosis involves the mitral apparatus; the supplied normally opening valve and separate membrane localize obstruction elsewhere.',
 'Pulmonary vein stenosis obstructs venous entry, not a membrane dividing pulmonary venous and appendage-containing atrial chambers.']),
43:dict(sections=[
 ('High-Risk Coronary Phenotype',[
  B('Opposite-sinus left coronary origin + slit-like ostium/intramural course + attributable ischemia warrants surgical assessment.',
    'CT defines origin/course; stress imaging tests functional consequence.'),
  B('A negative stress test does not automatically neutralize high-risk anatomy in another patient.')]),
 ('Repair and Follow-Up',[
  B('Select unroofing, reimplantation or another reconstruction from actual anatomy.',
    'Consider aortic commissural relationships and valve-injury risk.'),
  B('Restrict strenuous exertion pending assessment of this symptomatic ischemic presentation.'),
  B('Assess ventricular function, scar and arrhythmias; reassess before return to sport.',
    'Follow patency, residual ischemia and AR; repair is not a guarantee against every event.'),
  B('Asymptomatic or benign-course variants require separate assessment.')])],orderedSections=['Repair and Follow-Up'],reasons=[
 'Medication/surveillance can suit selected lower-risk or inoperable patients; attributable ischemia with this anatomy supports surgical correction.',
 'PCI treats acquired stenosis and selected anomalies; this intramural congenital origin needs anatomical surgical consideration, not automatic plaque-style stenting.',
 'An ICD treats established arrhythmic risk but does not relieve coronary compromise; this history does not supply a device indication instead of repair.']),
44:dict(sections=[
 ('Pregnancy Risk Is Not Symptom Class',[
  B('Eisenmenger/PAH → mWHO 2.0 class IV, despite functional class II or preserved LVEF.',
    'Pregnancy can worsen right-to-left shunting, RV failure, hypoxemia and embolic risk.',
    'Delivery and postpartum remain hazardous even after an uneventful early pregnancy.')]),
 ('Counseling and Management',[
  B('Pregnancy Heart Team: explain maternal/fetal risks, advise avoidance and discuss reliable contraception.'),
  B('Avoid estrogen-containing contraception in cyanotic CHD; individualize long-acting methods and insertion setting.'),
  B('Review PAH drugs: ERAs carry fetal risk; bosentan may reduce hormonal contraceptive efficacy.',
    'Do not abruptly stop essential therapy without specialist planning.'),
  B('If pregnant: prompt shared discussion of all options, including termination.',
    'If continuing, coordinate maternal-fetal, ACHD, PH and anesthesia care through postpartum.')])],orderedSections=['Counseling and Management'],reasons=[
 'Class II represents substantially lower risk. Mild symptoms and preserved LV function do not remove Eisenmenger pulmonary vascular hazards.',
 'II–III is an intermediate category, not an average of reassuring LV function and severe pulmonary vascular disease.',
 'Class III is high risk, but Eisenmenger belongs in the exceptionally high-risk class IV despite improved functional status.']),
45:dict(sections=[
 ('Who Needs Dental Prophylaxis?',[
  B('Residual shunt adjacent to prosthetic patch/device qualifies, including years after repair.'),
  B('Other high-risk groups: prior IE, prosthetic valves/repair material, unrepaired cyanotic CHD and transplant structural valvular disease.'),
  B('Relevant procedure: gingival manipulation, periapical work or mucosal perforation.')]),
 ('Adult Regimen and Prevention',[
  B('Amoxicillin 2 g orally once, 30–60 minutes before the procedure.',
    'Prophylaxis is not a multi-day course or treatment for established IE.'),
  B('Check allergy: clindamycin is no longer recommended by AHA.',
    'Avoid cephalosporins after penicillin-associated anaphylaxis, angioedema or urticaria.'),
  B('Maintain oral hygiene and regular dental care; evaluate unexplained fever.',
    'Suspected IE requires cultures and treatment assessment; document the actual prophylaxis indication.')])],reasons=[
 'A remote completely closed ASD without residual defect lacks this continuing high-risk anatomical indication; adjacent residual flow changes eligibility.',
 'Native bicuspid valve disease increases IE risk but alone is not an AHA highest-risk indication for dental prophylaxis.',
 'An unrepaired acyanotic muscular VSD alone does not qualify; unrepaired cyanotic disease and adjacent prosthetic residual defects are different categories.']),
46:dict(sections=[
 ('Why CPET?',[
  B('Patients may reduce activity and report no symptoms despite deteriorating capacity.'),
  B('CPET integrates cardiac delivery, ventilation, gas exchange, conditioning and effort.')]),
 ('Interpret and Prescribe Activity',[
  B('Review peak VO2, ventilatory efficiency, heart-rate/BP response, saturation and rhythm.'),
  B('Interpret low peak VO2 with effort and conditioning; assess chronotropic limitation and exercise desaturation.'),
  B('Compare serial tests using similar protocols and clinical conditions.'),
  B('Tailor exercise to ventricular function, PA pressure, aorta, rhythm risk and cyanosis.',
    'Encourage appropriate activity; severe obstruction, aortopathy or uncontrolled arrhythmia changes intensity/supervision.',
    'Use alternatives such as 6-minute walk when CPET is unsafe or unreliable.')])],orderedSections=['Interpret and Prescribe Activity'],reasons=[
 'Six-minute walk is useful in PAH or when CPET is impractical, but provides less complete gas-exchange and ventilatory assessment.',
 'Ambulatory ECG detects intermittent rhythm problems but does not quantify standardized oxygen uptake or integrated exercise capacity.',
 'CMR defines resting anatomy, volumes and flows; it cannot replace graded assessment of exertional physiology and rhythm.']),
47:dict(sections=[
 ('Preoperative ACHD Assessment',[
  B('Combine anatomy, current physiology, organ disease and procedural stress; preserved EF alone is insufficient.'),
  B('Review rhythm, oxygenation, venous pathways, ventricular/AV-valve function, liver/renal status and antithrombotics.'),
  B('ACHD/anesthesia team selects location, investigations, optimization and postoperative resources.')]),
 ('Fontan Anesthesia Priorities',[
  B('Protect venous return and low PVR during ventilation, pneumoperitoneum and positioning.'),
  B('Avoid hypoxemia, hypercapnia, acidosis and marked hypovolemia.',
    'Balance fluid against congestion; neither unrestricted loading nor aggressive depletion is appropriate.'),
  B('Use meticulous air precautions when right-to-left pathways exist; plan unusual venous access.'),
  B('Plan pain control, rhythm monitoring, fluid shifts and individualized anticoagulant interruption/resumption.',
    'Monitoring intensity depends on risk, not a universal ICU rule.')])],orderedSections=['Fontan Anesthesia Priorities'],reasons=[
 'RCRI adds acquired-disease risk information but does not adequately encode Fontan pathways, cyanosis or venous-pressure-related organ complications.',
 'CPET measures reserve but cannot independently plan for pneumoperitoneum, ventilation or hepatic bleeding risks; multidisciplinary integration is required.',
 'Catheterization addresses specific pressure/obstruction questions, not a mandatory test for every stable Fontan patient before surgery.']),
48:dict(sections=[
 ('Why Lifelong Review?',[
  B('TOF repair leaves risks of pulmonary valve dysfunction, residual obstruction, RV remodeling and scar arrhythmia.',
    'Self-limited activity can conceal deterioration; symptoms alone are insufficient surveillance.')]),
 ('Routine and Triggered Follow-Up',[
  B('2025 physiological stages A/B: ACHD visits every 12–24 months.'),
  B('Normal ventricular function and no more than mild PR: CMR every 3–5 years.',
    'Do not confuse imaging intervals with clinical visit intervals.'),
  B('Earlier review for palpitations, syncope, desaturation, exercise decline or changing imaging.',
    'Select rhythm monitoring, CPET and imaging according to the concern.'),
  B('Address exercise, reproductive health, procedures and acquired risk; preserve repair records.',
    'Intervals are lesion-specific and become closer with physiological deterioration.')])],reasons=[
 'A five-year CMR interval may fit stable TOF, but it should not replace the recommended 12–24-month clinical review.',
 'Shared cardiology care helps access, but symptom-only CMR may miss RV remodeling; planned congenital and objective surveillance remains needed.',
 'Annual CMR can suit significant residual disease, but stable normal-function/mild-PR physiology does not justify that intensity automatically.']),
49:dict(sections=[
 ('Follow the Recirculating Blood',[
  B('ASD: LA → RA/RV; primary right-heart volume load.'),
  B('VSD/PDA: excess pulmonary flow returns to LA/LV; primary left-heart volume load.'),
  B('Anomalous pulmonary venous drainage enters systemic veins and volume-loads the right heart.')]),
 ('Separate Pressure and Volume',[
  B('A large VSD can transmit systemic pressure while also increasing pulmonary flow.',
    'A restrictive jet retains a pressure gradient; pressure does not quantify volume or PVR.'),
  B('Pulmonary stenosis causes RV pressure loading; pulmonary regurgitation causes RV volume loading without an ASD.'),
  B('Advanced pulmonary vascular disease can reduce shunting and alter chamber patterns.',
    'Confirm anatomy/flow by echo and selected CMR; attribute chamber enlargement before intervention.')])],reasons=[
 'This reverses the usual pattern: ASD loads RA/RV, whereas VSD pulmonary recirculation returns excess volume to LA/LV.',
 'Large VSD can transmit RV pressure, but significant left-to-right flow also increases LA/LV filling; it is not isolated RV pressure loading.',
 'Uncomplicated ASD predominantly increases RV filling volume; isolated RV pressure overload suggests another or additional mechanism.']),
50:dict(sections=[
 ('Two Independent Axes',[
  B('Anatomy: I simple, II moderate complexity, III great complexity.',
    'TOF without pulmonary atresia is II; TOF with pulmonary atresia is III.'),
  B('Physiology: A–D; use the highest applicable stage.',
    'Repair does not automatically make anatomy simple or physiology normal.')]),
 ('Apply the 2025 Time Window',[
  B('Heart-failure admission within 12 months establishes stage D.',
    'This admission was 4 months ago: II-D despite current NYHA II.',
    'Current moderate PR alone would be a C feature; clinical improvement does not erase the recent D event.'),
  B('Reassess physiology over time to guide surveillance and procedural planning.',
    'Record the qualifying findings; symptoms, EF or anatomical labels alone are incomplete.')])],reasons=[
 'Anatomical II is correct; moderate PR is a C feature, but the recent heart-failure admission establishes the higher stage D.',
 'Ordinary repaired TOF is anatomical II, not III; this option also overlooks the stage-D admission within 12 months.',
 'Stage D is correct, but heart failure changes physiology rather than anatomical category; TOF without pulmonary atresia remains II.']),
51:dict(sections=[
 ('Why Collaterals Do Not Establish Safety',[
  B('ALCAPA: left coronary arises from PA; RCA collaterals permit adult survival.',
    'Retrograde runoff into low-pressure PA creates steal; preserved resting EF does not eliminate ischemic/SCD risk.'),
  B('Manifestations include LV dysfunction, arrhythmia and ischemic/functional MR.')]),
 ('Restore a Two-Coronary Circulation',[
  B('Map coronary anatomy and collaterals with cross-sectional imaging; assess LV, MR and scar.'),
  B('Current guidance recommends surgical repair, including asymptomatic adults.',
    'Reimplantation when feasible or another anatomical reconstruction supplies the left coronary territory.'),
  B('Negative stress testing is not a criterion for avoiding recommended repair.'),
  B('Follow patency, ventricular recovery, MR and arrhythmias.',
    'Existing scar may persist after perfusion is restored.')])],orderedSections=['Restore a Two-Coronary Circulation'],reasons=[
 'Collaterals explain survival but do not abolish ischemia/SCD risk; waiting for falling EF delays the recommended anatomical repair.',
 'Stress studies assess functional consequences but cannot guarantee long-term safety; surgery is not conditional on a positive test.',
 'Ligation alone removes runoff but leaves collateral-dependent supply; the usual objective is a reliable two-coronary system.']),
}
