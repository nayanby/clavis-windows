"""Compact cyanotic, transposition and Fontan teaching notes."""
def B(label,*details):return ('**'+label+'**',list(details))
edits={
26:dict(sections=[
 ('Eisenmenger Physiology',[
  B('Longstanding large shunt → pulmonary arteriolar remodeling → high PVR → bidirectional/right-to-left flow.',
    'Earlier overcirculation and the causal large VSD distinguish this from coincidental-defect PAH.'),
  B('2022 ESC/ERS precapillary PH: mPAP >20 mmHg, PAWP ≤15 mmHg, PVR >2 Wood units.',
    'These hemodynamics alone do not establish Eisenmenger syndrome.'),
  B('PVR = (mPAP − PAWP)/Qp; use mmHg and L/min.',
    'In shunts, pulmonary flow Qp is not interchangeable with systemic flow Qs.')]),
 ('Clinical Consequences',[
  B('Do not close the established Eisenmenger pressure-relief pathway: RV failure may follow.'),
  B('ACHD/PH care: targeted therapy, exercise/functional assessment, iron and renal monitoring.',
    'Assess bleeding, arrhythmia, embolism and infection; pregnancy risk is very high.',
    'Exclude air meticulously from IV lines because systemic embolization is possible.')])],reasons=[
 'Coincidental small defects do not explain the arteriopathy. This large longstanding VSD caused prior overcirculation and subsequent reversal.',
 'Post-correction PAH requires prior repair; this defect remains open and carries desaturated systemic flow.',
 'Prevalent systemic-to-pulmonary shunts retain net left-to-right flow. Qp/Qs 0.8 with cyanosis instead supports Eisenmenger physiology.']),
27:dict(sections=[
 ('Adaptive Erythrocytosis',[
  B('Higher hemoglobin compensates for reduced saturation and helps maintain oxygen content.',
    'Hematocrit 68% without symptoms or iron deficiency is not a phlebotomy indication.')]),
 ('If Hyperviscosity Symptoms Occur',[
  B('Assess hydration and iron indices; correct reversible abnormalities.'),
  B('Exclude alternative causes of headache, dizziness or fatigue.',
    'Severe headache, fever or focal deficits require urgent assessment for stroke/brain abscess.'),
  B('Consider expert isovolumic phlebotomy only for persistent important symptoms, usually Hct >65%, after correction.'),
  B('Monitor saturation, symptoms, CBC and iron stores.',
    'Repeated venesection can impair oxygen delivery and cause iron deficiency.')])],orderedSections=['If Hyperviscosity Symptoms Occur'],reasons=[
 'Hct >65% is relevant only with persistent significant hyperviscosity after hydration and iron correction; the supplied patient is asymptomatic.',
 'Polycythemia vera is clonal with different treatment targets; applying its hematocrit target to hypoxemic adaptation can impair oxygen transport.',
 'Aspirin has separate vascular indications, but elevated red-cell mass alone does not establish benefit and cyanotic patients may bleed.']),
28:dict(sections=[
 ('Iron Deficiency Despite High Hemoglobin',[
  B('Ferritin 7 micrograms/L + transferrin saturation 8% confirms depleted iron stores.',
    'Microcytosis supports deficiency; high hemoglobin does not exclude it in chronic hypoxemia.'),
  B('Interpret hemoglobin relative to saturation; inflammation can complicate ferritin interpretation.')]),
 ('Replace and Reassess',[
  B('Look for dietary deficiency, menstrual/GI loss and prior phlebotomy.'),
  B('Choose oral or IV iron according to severity and tolerance.',
    'A small prospective study used ferrous fumarate up to 200 mg three times daily for 3 months.',
    'This is iron-salt mass, not elemental iron, and not a mandatory starting regimen.'),
  B('Repeat CBC, iron indices and symptoms; assess excessive erythrocytosis or adverse effects.',
    'Persistent microcytosis after repletion may require a hemoglobinopathy evaluation.')])],orderedSections=['Replace and Reassess'],reasons=[
 'Hemoglobin rises adaptively in hypoxemia; low ferritin and transferrin saturation still demonstrate treatable iron deficiency.',
 'Venesection removes additional iron and red cells. Its narrow hyperviscosity indication does not apply to this iron-deficient presentation.',
 'Thalassemia can coexist, but proven iron depletion already warrants treatment; investigate residual unexplained microcytosis after repletion.']),
29:dict(sections=[
 ('Trial Interpretation',[
  B('BREATHE-5: 54 WHO-FC III patients; bosentan versus placebo for 16 weeks.',
    'PVR improved; systemic saturation safety was preserved; walking distance also improved.'),
  B('MAESTRO: 226 patients; macitentan did not meet primary 6-minute-walk superiority.',
    'Exploratory signals do not convert a negative primary endpoint into proven efficacy or mortality benefit.')]),
 ('Drug Use and Escalation',[
  B('Bosentan blocks ETA and ETB: >40-kg adult, 62.5 mg twice daily for 4 weeks, then 125 mg twice daily.',
    'LFTs before treatment and monthly; monitor Hb, edema and interactions.',
    'Pregnancy contraindicated; contraception during treatment and for 1 month afterward; hormonal contraceptive efficacy may fall.'),
  B('2025: persistent symptoms/worsening exercise on monotherapy with LVEF >40% → ERA + PDE5 inhibitor.',
    'Sildenafil commonly 20 mg three times daily; avoid nitrates and riociguat.'),
  B('Selected advanced disease: specialist prostacyclin therapy.',
    'IV epoprostenol labeled start 2 ng/kg/min; initial increments 2 ng/kg/min at ≥15-minute intervals under monitoring.',
    'Monitor BP, oxygenation, flushing, headache, jaw pain and diarrhea; abrupt interruption risks rebound PH.',
    'Plan infusion backup, infection prevention and meticulous air exclusion.'),
  B('Refractory high-risk disease: assess lung transplant plus defect repair versus heart–lung transplantation.',
    'Choice depends on anatomy, ventricular function and other organs; not equivalent to isolated shunt closure.')])],orderedSections=['Drug Use and Escalation'],reasons=[
 'MAESTRO did not demonstrate primary walking-distance superiority; biomarker or subgroup signals must retain their exploratory status.',
 'BREATHE-5 compared bosentan with placebo, not sildenafil; it cannot establish head-to-head superiority over PDE5 inhibition.',
 'MAESTRO studied short-term exercise capacity, not mortality as its primary endpoint; a survival claim is unsupported.']),
30:dict(sections=[
 ('Thrombosis and Bleeding Coexist',[
  B('Cyanotic CHD combines stasis/vascular dilation with platelet and coagulation abnormalities.',
    'Organized in-situ PA thrombus is not automatically equivalent to acute embolism.'),
  B('2025: no routine oral anticoagulation solely for Eisenmenger syndrome.')]),
 ('When an Independent Indication Exists',[
  B('Reassess for atrial arrhythmia, proven thromboembolism, mechanical valve or another indication.'),
  B('Review bleeding, platelets, renal/hepatic function and drug interactions.',
    'Mechanical valves require a vitamin K antagonist, not a DOAC.'),
  B('Significant active hemoptysis: urgent assessment, stabilization and selected antithrombotic interruption/reversal.'),
  B('With markedly high hematocrit, ask the laboratory about citrate adjustment for coagulation samples.')])],orderedSections=['When an Independent Indication Exists'],reasons=[
 'Warfarin may treat an independent indication, but routine Eisenmenger thromboprophylaxis lacks sufficient benefit against the bleeding risk.',
 'Avoiding INR monitoring is convenient but does not create an indication; a DOAC still requires appropriate risk and organ-function assessment.',
 'Aspirin treats specific arterial conditions; it is not a proven low-intensity substitute for routine cyanotic-CHD anticoagulation.']),
31:dict(sections=[
 ('Diagnostic Anatomy',[
  B('Indexed displacement = 18/1.8 = 10 mm/m²; ≥8 mm/m² supports adult Ebstein anomaly.',
    'Measure septal tricuspid hinge relative to anterior mitral insertion in the four-chamber view.'),
  B('Displaced valve creates atrialized proximal RV and a functional distal RV.',
    'Assess leaflet morphology, TR and effective RV output; total chamber size can mislead.')]),
 ('Associated Lesions and Intervention',[
  B('Look for ASD/PFO-related cyanosis and accessory pathways; CMR quantifies functional RV anatomy.'),
  B('2025: ≥moderate TR with HF, worsening exercise capacity or progressive RV dysfunction → surgery.',
    'Selected asymptomatic cases: progressive RV enlargement, atrial desaturation, recurrent arrhythmia or paradoxical embolism also support intervention.'),
  B('Cone reconstruction preserves native valve tissue when suitable.',
    'Do not close an atrial outlet without assessing RV filling tolerance.')])],reasons=[
 'Dysplasia causes malformed leaflets and TR without the characteristic indexed apical displacement demonstrated in this case.',
 'Atrial functional TR follows annular/right-atrial dilation; it does not explain congenital displacement of the septal hinge point.',
 'Ventricular functional TR reflects tethering from RV remodeling; the valve attachment itself is not characteristically displaced as supplied.']),
32:dict(sections=[
 ('Why Asymptomatic Pre-excitation Matters',[
  B('Ebstein anomaly can have multiple or rapidly conducting accessory pathways.',
    'They support AVRT; pre-excited AF may produce dangerous ventricular rates.'),
  B('2025: EP study is recommended for symptomatic arrhythmia or asymptomatic ventricular pre-excitation.')]),
 ('Coordinate With Tricuspid Surgery',[
  B('Map pathway number and conduction risk before surgery when appropriate.'),
  B('Ablate high-risk or multiple pathways using congenital EP expertise.',
    'Valve repair may make later catheter access more difficult.'),
  B('For unstable tachyarrhythmia, use synchronized cardioversion.',
    'Avoid isolated AV-nodal blockade in irregular pre-excited tachycardia.'),
  B('Successful ablation does not treat severe TR; continue structural care.')])],orderedSections=['Coordinate With Tricuspid Surgery'],reasons=[
 'Monitoring can capture episodes but cannot fully assess antegrade conduction risk or exclude multiple pathways in manifest pre-excitation.',
 'Repair can impede later access; absence of palpitations does not remove the rationale for preoperative pathway assessment.',
 'AV-nodal blockers treat selected regular SVTs but do not eliminate pathways and can be hazardous during pre-excited AF.']),
33:dict(sections=[
 ('Atrial-Switch Circulation',[
  B('Mustard/Senning baffles send caval blood to the mitral valve and subpulmonary LV.',
    'Pulmonary venous blood enters the systemic RV and aorta.'),
  B('Baffle leak permits desaturated venous blood into the systemic circuit.',
    'Exercise-related pressure changes may reveal a leak not obvious at rest.')]),
 ('Investigate and Manage',[
  B('Map baffle patency and integrity: contrast echo, CMR and selected TEE/catheterization.',
    'Arm injection can miss an inferior baffle leak; select the injection site for the anatomy.'),
  B('Assess symptomatic leak closure with congenital expertise and hemodynamic review.'),
  B('Before transvenous leads, assess obstruction and systemic embolic risk.'),
  B('Continue surveillance for systemic RV failure, TR, atrial arrhythmia and sinus-node disease.')])],orderedSections=['Investigate and Manage'],reasons=[
 'Baffle stenosis restricts preload and causes congestion, but without admixture it does not directly explain arterial desaturation.',
 'Systemic TR can reduce output but does not create venous-to-arterial mixing; important new regurgitation is also excluded.',
 'Chronotropic incompetence limits exercise output through heart-rate response, usually without this marked reproducible oxygen-saturation fall.']),
34:dict(sections=[
 ('Arterial-Switch Complications',[
  B('Great arteries are switched and coronaries reimplanted; the LV becomes systemic.',
    'Late ostial narrowing or proximal kinking can cause ischemia despite young age.'),
  B('New exertional symptoms or regional dysfunction warrant coronary evaluation.')]),
 ('Select the Investigation',[
  B('Coronary CTA maps transferred ostia, proximal course and great-vessel relationships.'),
  B('Functional perfusion testing or invasive angiography may clarify significance or persistent unexplained symptoms.',
    'A normal anatomical study does not exclude every dynamic abnormality.'),
  B('This stable case asks anatomy; unstable/ACS presentations need urgent clinical treatment.'),
  B('Long-term follow-up also assesses neoaortic root/valve and neopulmonary/branch PA stenosis.')])],orderedSections=['Select the Investigation'],reasons=[
 'Stress CMR assesses perfusion/ischemia, whereas this question asks directly for reimplanted coronary ostial and proximal anatomy.',
 'Stress echo detects inducible wall-motion changes but does not usually map the surgically transferred coronary origins.',
 'Exercise ECG can link symptoms and ischemic electrical changes; it cannot show ostial narrowing or the proximal coronary course.']),
35:dict(sections=[
 ('Double Discordance',[
  B('AV discordance + ventriculoarterial discordance restores circulation in series.',
    'Systemic venous blood → morphological LV → PA.',
    'Pulmonary venous blood → morphological tricuspid valve/RV → aorta.'),
  B('Identify morphology, not side: moderator band and coarse trabeculations indicate RV.')]),
 ('Adult Complications',[
  B('Systemic RV dysfunction and systemic TR can reinforce each other.',
    '2025: symptomatic severe TR with normal/mildly impaired systemic RV function → surgical valve replacement.'),
  B('Abnormal conduction anatomy causes spontaneous AV block.',
    'Symptomatic complete block needs urgent rhythm/pacing assessment; plan activation to limit dyssynchrony.'),
  B('Assess associated VSD, pulmonary obstruction and Ebstein-like tricuspid anatomy.',
    'Corrected describes flow sequence, not normal anatomy or freedom from surveillance.')])],reasons=[
 'Mitral/LV is the usual systemic pump and follows arterial switch with AV concordance; double discordance leaves the RV systemic.',
 'Left-sided location does not make this chamber an LV; its moderator band and trabeculation identify a morphological RV.',
 'AV-valve identity follows morphological ventricular connection; the supplied systemic RV has a tricuspid, not mitral, inlet.']),
36:dict(sections=[
 ('Passive Pulmonary Flow',[
  B('Fontan connects caval return to the pulmonary arteries without a subpulmonary ventricle.'),
  B('Qp depends on (Fontan pressure − pulmonary venous pressure)/PVR.',
    'Higher PVR reduces flow or requires more upstream venous pressure.',
    'Less pulmonary return → less systemic ventricular preload and stroke volume; EF can remain normal.')]),
 ('Assess the Whole Circuit',[
  B('Check pathway/branch PA obstruction, filling pressure, AV-valve disease, rhythm and collaterals.'),
  B('Use catheterization when unexplained deterioration needs pressure/flow assessment.'),
  B('Treat congestion cautiously: excessive diuresis further reduces preload.'),
  B('Selected pulmonary vasodilators may help without elevated ventricular filling pressure.',
    'They do not correct mechanical pathway obstruction; response is not uniform.')])],
 flow=['PVR ↑','Passive pulmonary flow ↓','Ventricular preload ↓','Stroke volume ↓ despite preserved EF'],reasons=[
 'Systemic arterial resistance directly determines systemic ejection afterload; pulmonary resistance chiefly limits upstream filling in Fontan physiology.',
 'Diastolic stiffness can limit output through high downstream filling pressure, but that pressure is unchanged in this case.',
 'Sinus-node dysfunction can impair exercise output, but no abnormal rate response is supplied; increased PVR directly explains reduced preload.']),
37:dict(sections=[
 ('Confirm Intestinal Protein Loss',[
  B('Timed fecal alpha-1-antitrypsin clearance uses contemporaneous stool and serum measurements.',
    'Mayo reference ≤27 mL/24 h; diarrhea may raise values and requires qualified interpretation.',
    'GI bleeding can confound results; gastric acid limits assessment of gastric protein loss.'),
  B('PLE: low albumin, edema ± diarrhea, immunoglobulin/lymphocyte loss.',
    'Exclude renal loss, nutrition and hepatic dysfunction; normal INR does not exclude FALD.')]),
 ('Fontan and Lymphatic Management',[
  B('Assess pathway obstruction, PVR, ventricular filling, AV-valve disease and rhythm.'),
  B('Support nutrition and fluid balance; correct reversible hemodynamic lesions.',
    'Albumin provides temporary support, not correction of ongoing leakage.'),
  B('Selected patients need lymphatic imaging/intervention or transplant assessment.')]),
 ('Plastic Bronchitis',[
  B('Abnormal pulmonary lymphatic flow causes branching bronchial casts and possible airway obstruction.',
    'Urgent airway assessment ± bronchoscopic removal; dynamic MR lymphangiography can guide targeted intervention.',
    'Preserved EF does not exclude either lymphatic complication.')])],orderedSections=['Fontan and Lymphatic Management'],reasons=[
 'Calprotectin indicates intestinal inflammation and supports IBD assessment; it does not quantify intestinal plasma-protein clearance.',
 'Elastase evaluates pancreatic insufficiency, with dilutional pitfalls in watery stool; it does not directly demonstrate protein-losing enteropathy.',
 'Fecal fat documents fat malabsorption, not plasma-protein leakage; it cannot directly confirm the suspected Fontan complication.']),
38:dict(sections=[
 ('Fontan Thromboembolic Risk',[
  B('Venous stasis, abnormal pathways and sustained atrial arrhythmia add risk beyond CHA2DS2-VASc.'),
  B('A 20-minute documented flutter episode establishes a sustained arrhythmia history.',
    'Return to sinus rhythm does not remove that history or the Fontan substrate.')]),
 ('Long-Term Strategy',[
  B('Initiate oral anticoagulation after agent and bleeding-risk assessment.'),
  B('Review renal/hepatic function, prior bleeding, anatomy, drugs and adherence.',
    'Do not infer agent equivalence from convenience; comparative Fontan evidence remains limited.'),
  B('Lower-risk Fontan adults without high-risk features may receive aspirin or anticoagulation.',
    'Prior thrombus, embolism, atriopulmonary Fontan or sustained atrial arrhythmia changes the decision.'),
  B('Continue rhythm surveillance and evaluate hemodynamic contributors.')])],orderedSections=['Long-Term Strategy'],reasons=[
 'Aspirin can suit lower-risk Fontan prophylaxis, but sustained flutter is a high-risk feature missed by a conventional zero stroke score.',
 'The documented sustained episode already establishes the relevant risk; waiting for recurrence is not required by this pathway.',
 'Episode-only treatment ignores persistent Fontan stasis and arrhythmia history; anticoagulation is not limited to detected flutter periods.']),
39:dict(sections=[
 ('Cirrhosis and HCC Surveillance',[
  B('FALD reflects chronic venous congestion and altered perfusion; quiet liver enzymes do not exclude advanced disease.'),
  B('Confirmed cirrhosis: surveillance at least every 6 months.',
    'EASL-ERN: experienced ultrasound with AFP adjunct; normal AFP does not exclude HCC.',
    'Poor visualization or suspicious nodules require appropriate multiphase CT/MRI.')]),
 ('Interpret Results in Fontan Context',[
  B('Elastography reflects congestion plus fibrosis; ordinary fibrosis cutoffs may misclassify FALD.'),
  B('Assess platelets, spleen, varices, ascites and serial imaging.',
    'Regenerative nodules can be benign; indeterminate lesions may need targeted biopsy.'),
  B('Coordinate hepatology and ACHD care; review circuit pressures and transplant implications.',
    'Routine repeat biopsy is not a substitute for tumor surveillance.')])]),
40:dict(sections=[
 ('Why Flutter Destabilizes Fontan Flow',[
  B('Loss of effective atrial rhythm impairs filling even after the ventricular rate slows.',
    'AV-valve disease, relaxation abnormalities and pulmonary venous flow changes may amplify the effect.')]),
 ('Restore Rhythm and Assess the Circuit',[
  B('2025: timely cardioversion for new atrial flutter/AF.',
    'Stable patients need thrombus assessment, anticoagulation and selected imaging; short reported duration does not eliminate risk.'),
  B('Instability: urgent synchronized cardioversion; do not wait for an elective anticoagulation interval.'),
  B('Plan sedation/ventilation to preserve preload and low PVR.',
    'Avoid excessive airway pressure, hypoxemia and acidosis.'),
  B('Search for obstruction/thrombosis, AV-valve disease and ventricular/filling abnormalities.',
    'Consider congenital EP ablation, recurrence monitoring and advanced Fontan assessment if deterioration persists.')])],orderedSections=['Restore Rhythm and Assess the Circuit'],reasons=[
 'Rate slowing can stabilize initially, but persistent Fontan symptoms require timely rhythm restoration and evaluation rather than routine delayed review.',
 'Diuresis helps congestion but can reduce preload; the arrhythmia itself needs treatment instead of waiting for full decongestion.',
 'Vasodilators help selected pulmonary vascular limitation; they do not replace treatment of new flutter and require filling-pressure assessment.']),
}
