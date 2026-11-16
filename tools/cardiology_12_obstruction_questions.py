"""Coarctation, RV outflow localization and BAV family assessment."""
from qbank_json_chapters import question as Q

REFERENCES={
 'AORTA2022': ('ACC/AHA aortic disease guideline, 2022', 'https://doi.org/10.1161/CIR.0000000000001106'),
 'ESC_AORTA2024': ('ESC peripheral arterial and aortic diseases guideline, 2024', 'https://academic.oup.com/eurheartj/article/45/36/3538/7738955'),
 'COA_LVH': ('Persistent hypertension and LV hypertrophy after adult coarctation repair', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC8363521/'),
 'COA_TEAM': ('Heart-team management of adult coarctation', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC8807410/'),
 'COA_DIASTOLIC': ('LV diastolic function and exertional symptoms in adult coarctation', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC7041882/'),
 'DCRV_CASE': ('Double density sign in double-chambered RV, 2025', 'https://doi.org/10.1016/j.jaccas.2025.103529'),
 'BAV_AATS': ('AATS consensus on BAV-related aortopathy', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6413866/'),
}
COA='Coarctation after diagnosis and repair'
OUTFLOW='Congenital valve and outflow obstruction'
rows=[]

def S(h,t,*children):return h,[(t,list(children))]
def add(*args,**kwargs):rows.append(Q(*args,**kwargs))

add(COA,'Thoracic Aortic Surveillance After Coarctation Repair',
 'A 34-year-old had surgical coarctation repair in childhood. TTE shows preserved LV function and no large residual gradient, but the repair site is incompletely visualized. There has been no cross-sectional aortic imaging for many years. Which study most comprehensively assesses the repair segment, arch and collateral anatomy?',
 'CMR angiography of the thoracic aorta including the repair site',[
  ('TTE with repeated suprasternal Doppler sweeps alone','TTE is useful for LV function, associated valve disease and flow assessment. The stated acoustic limitation leaves important aortic wall and repair-site anatomy unresolved, so repeating Doppler alone does not complete aneurysm and arch surveillance.'),
  ('TEE limited to the descending thoracic aorta','TEE can provide valuable information about accessible thoracic aortic segments. It has anatomical blind spots and does not offer the same comprehensive noninvasive arch, repair-site and collateral survey in this stable follow-up setting.'),
  ('Duplex ultrasound of the abdominal aorta and renal arteries','Abdominal and renal duplex can evaluate distal flow or selected renal causes of hypertension. It does not adequately examine the childhood thoracic repair site for focal aneurysm, pseudoaneurysm or arch abnormalities.')],
 [S('What a Normal Gradient Does Not Exclude',
   '**Repair-site aneurysm and other aortic complications can be present without a large resting obstruction gradient.** Surveillance must assess the vessel wall and surrounding anatomy, not only systolic flow velocity.',
   'CMR defines arch geometry, the repair segment, residual narrowing and collateral vessels without radiation. CTA is an appropriate alternative when CMR is unsuitable or CT provides a better answer to the particular anatomical question.',
   'The imaging plan should also consider the aortic root and ascending aorta and associated bicuspid valve disease. With a prior stent, artifact and the need to assess the lumen or stent integrity may favor CT.'),
  S('Long-Term Follow-Up',
   '**Adults require continued assessment after apparently successful anatomical repair.** Check upper- and lower-extremity BP, LV remodeling, valve function and symptoms, and select imaging intervals from the current anatomy and prior findings.',
   'ESC 2024 recommends aortic CT/CMR every three to five years, adapted to clinical status and previous imaging. Residual stenosis, aortic dilation, repair technique, growth and image quality can require earlier assessment; a normal TTE is not a reason to stop surveillance. Acute pain or pulse changes require assessment outside the routine schedule.',
   'Hypertension may persist after relief of the obstruction. Ambulatory monitoring and exercise testing can reveal pressure burdens missed by a resting office reading. Detecting a high BP does not automatically prove recoarctation, just as a normal resting gradient does not rule out an aneurysm. Structural surveillance and physiological follow-up answer complementary questions.')],
 ['ACHD2025','AORTA2022','ESC2020','ESC_AORTA2024'])

add(COA,'Severe Coarctation With a Modest Measured Gradient',
 'An adult has arm BP 166/92 mmHg, leg BP 154/86 mmHg and an invasive coarctation peak-to-peak gradient of 12 mmHg. CTA shows a 7-mm isthmus, a 20-mm descending aorta at the diaphragm and extensive intercostal collaterals. Which interpretation is most appropriate?',
 'Important obstruction remains possible because collateral flow can reduce the measured gradient',[
  ('The catheter gradient establishes that the anatomical narrowing is minor','A gradient is flow dependent. Extensive collateral pathways can bypass a severely narrowed segment; the low value must therefore be interpreted with anatomy, hypertension and ventricular consequences rather than used to dismiss them.'),
  ('The maximum instantaneous Doppler gradient can replace the catheter value directly','Doppler maximum instantaneous and catheter peak-to-peak gradients are different measurements. They should not be substituted numerically without understanding the flow profile and pressure recovery.'),
  ('The modest arm–leg pressure difference makes hypertension unrelated to coarctation','A small limb pressure difference can also occur with collateral flow or other hemodynamic modifiers. It does not establish an unrelated cause when severe anatomical narrowing and proximal hypertension are documented.')],
 [S('Anatomy and Bypass Flow',
   '**Extensive collaterals can reduce flow through the narrowed isthmus and attenuate the pressure drop measured across it.** The case therefore needs integrated ACHD assessment rather than a single-gradient exclusion rule.',
   'The aortic isthmus ratio is the minimum isthmus diameter divided by the descending aortic diameter at the diaphragm. Here it is 7/20 = 0.35, supporting substantial anatomical narrowing.',
   'Low LV output or associated severe aortic stenosis can also reduce measured coarctation gradients. Assess ventricular function, valve lesions, collateral flow and measurement conditions before judging severity.'),
  S('Intervention Assessment',
   '**The 2025 ACHD framework accepts physiological and anatomical evidence when evaluating significant coarctation.** Its table includes gradients above 20 mmHg as important findings while explicitly qualifying situations in which gradients are lower.',
   'Expert consensus has commonly used an isthmus ratio below 0.5 as a marker of major narrowing, while newer observational analyses support assessment at less extreme narrowing. A ratio is not a universal standalone command to intervene.',
   'Review hypertension, LV hypertrophy, symptoms, repair options and procedural risk with a congenital aortic team. Severe anatomy with compatible consequences can justify intervention assessment despite the supplied 12-mmHg gradient. Conversely, an isolated high velocity with a widely patent repaired aorta may have a different explanation. Specify the named guideline and measurement method rather than treating all values labeled gradient as interchangeable.')],
 ['ACHD2025','COA_TEAM','COA_DIASTOLIC'],
 table=(['Assessment','2025 significance finding or case calculation','Qualification'],[
  ['Arm–leg systolic BP difference','Above 20 mmHg','Collateral flow can attenuate the difference'],
  ['Invasive peak-to-peak gradient','Above 20 mmHg','Flow and loading conditions affect the value'],
  ['Doppler mean systolic gradient','Above 20 mmHg','Do not substitute the maximum instantaneous value'],
  ['Isthmus / diaphragm-level descending aorta','7/20 = 0.35 in this case','Anatomical severity complements physiological assessment'],
 ]))

add(COA,'Adult Native Coarctation: Choosing a Repair Approach',
 'A 28-year-old with hypertension has discrete native coarctation, an invasive peak-to-peak gradient of 32 mmHg and suitable landing zones and arterial access. There is no extensive arch hypoplasia or associated lesion requiring surgery. Under the ESC adult congenital approach, which repair is generally preferred when technically feasible?',
 'Endovascular stent repair of the narrowed segment',[
  ('Balloon angioplasty without stent support','Balloon treatment has roles in selected contexts, including redilatation of a previously stented segment. For a suitable native adult coarctation, stent support better addresses recoil and is generally preferred to balloon angioplasty alone.'),
  ('Surgical interposition graft repair','An interposition graft is an established adult surgical option and can be appropriate for anatomy unsuitable for a catheter approach. The supplied discrete lesion, landing zones and access favor the less invasive stent pathway.'),
  ('Surgical ascending-to-descending aortic bypass','Bypass can be valuable for complex arch anatomy or other difficult surgical situations. It is not usually the preferred initial repair of an isolated discrete lesion that is suitable for stenting.')],
 [S('Indication and Procedural Planning',
   '**Hypertension with a clearly significant coarctation warrants repair assessment.** This patient has a favorable anatomical target and a substantial invasive gradient, without the modifiers that complicate a borderline measurement.',
   'ESC 2020 describes stenting as the first-choice approach in many adult congenital centers for suitable native or recurrent coarctation. Covered stents are often preferred to reduce aortic wall complications, but device choice remains anatomical and procedural.',
   'Assess the arch, head-and-neck branches, collateral vessels, aortic wall, any aneurysm and access-vessel size. A label of adult coarctation does not establish that every lesion can safely accept the same device.'),
  S('Benefits, Risks and Surveillance',
   '**Repair relieves the obstruction but does not guarantee normalization of BP.** Vascular stiffness, endothelial dysfunction and established ventricular remodeling can persist.',
   'Discuss aortic wall injury, aneurysm, access complications, stent migration or fracture, residual gradient and possible later reintervention. Appropriate follow-up includes cross-sectional imaging and BP assessment.',
   'Surgery remains important for extensive arch disease, unsuitable landing zones, complex associated pathology or a need for combined repair. The 2025 US guideline permits surgical or transcatheter repair by ACHD experts rather than mandating one device. Continue BP treatment after repair; that guideline targets systolic BP below 130 mmHg, individualized for tolerance. Persistent hypertension does not by itself establish procedural failure.')],
 ['ESC2020','ACHD2025','COA_LVH'])

add(COA,'Coarctation: Doppler and Catheter Gradients',
 'For coarctation assessment, which Doppler-derived quantity best approximates the catheterization-derived peak-to-peak systolic gradient according to the 2025 ACHD guideline?',
 'The Doppler mean systolic gradient',[
  ('The uncorrected maximum instantaneous systolic gradient','The maximum instantaneous gradient compares simultaneous velocities and can exceed the invasive peak-to-peak value. It is useful in assessment but should not be treated as its numerically identical replacement.'),
  ('The proximal-velocity-corrected maximum instantaneous gradient','Correcting for proximal velocity addresses one source of Doppler error. The result remains a maximum instantaneous index, with a different relationship and threshold from the catheter peak-to-peak measurement.'),
  ('The maximum gradient derived from the diastolic flow tail','Persistent diastolic forward flow can support significant coarctation. A peak diastolic estimate is not the systolic Doppler index used for the closest approximation of the invasive peak-to-peak gradient.')],
 [S('Why the Measurements Differ',
   '**An invasive peak-to-peak gradient compares proximal and distal systolic pressure peaks, which need not occur simultaneously.** Doppler maximum instantaneous gradients use the largest simultaneous velocity-derived difference.',
   'The 2025 guideline identifies the Doppler mean coarctation gradient as the best approximation among these Doppler-derived indices. That is an empirical relationship, not proof that any two measurements are identical in every patient.',
   'Flow, collaterals, pressure recovery, proximal velocity, Doppler alignment and the repaired aorta’s compliance can change the relationship. A report must state whether its value is mean, maximum instantaneous, corrected or invasive.'),
  S('Interpretation After Repair',
   '**An elevated postrepair Doppler gradient can occur without a fixed recurrent narrowing.** Poor arterial compliance and pressure recovery are important reasons to integrate the velocity with cross-sectional anatomy and clinical findings.',
   'Conversely, a modest resting gradient does not exclude important narrowing if collaterals or low output attenuate the pressure drop. Review arch dimensions, ventricular function, limb pressures and symptoms.',
   'Do not recommend repeat stenting from a single peak velocity alone. Determine whether there is an anatomical target and meaningful residual pressure burden. Continue surveillance for aortic complications and persistent hypertension even when no new intervention is required. Resting office measurements can miss hypertension; selected ambulatory and exercise assessment can refine physiological follow-up. The objective is agreement between the anatomy, the stated hemodynamic measurement and the patient’s consequences, not selection of the largest reported number.')],
 ['ACHD2025','AORTA2022','COA_DIASTOLIC'],style='direct')

add(OUTFLOW,'Intracavitary RV Pressure Step and Double-Chambered RV',
 'An adult with a small perimembranous VSD has exertional limitation. Catheter pullback shows PA systolic pressure 24 mmHg, distal RV systolic pressure 26 mmHg and proximal RV systolic pressure 78 mmHg. The pulmonary valve is structurally normal. Which obstruction best fits the pressure distribution?',
 'Intracavitary obstruction from a double-chambered right ventricle',[
  ('Valvar pulmonary stenosis','Valvar obstruction produces a major pressure step between the RV outflow and pulmonary artery. Here the distal RV and PA systolic pressures are similar, while the large step lies within the RV.'),
  ('Supravalvar main pulmonary artery stenosis','Supravalvar obstruction is beyond the pulmonary valve and produces an outflow-to-distal-PA pressure difference. It does not explain the supplied high proximal RV pressure with a relatively low distal RV pressure.'),
  ('Peripheral branch pulmonary artery stenosis','Branch stenosis requires assessment of main and branch PA pressures and the branch anatomy. It would not primarily partition the RV itself into a high-pressure proximal and low-pressure distal compartment.')],
 [S('Localizing the Obstruction',
   '**Double-chambered RV results from obstructing muscle bundles dividing the ventricle into pressure compartments.** The major step in this case is between proximal and distal RV, not across the pulmonary valve.',
   'A perimembranous VSD is a recognized association. Its connection to the high- or low-pressure compartment can alter the apparent jet and shunt physiology, so define the full anatomy before VSD repair.',
   'TTE may miss the complete intraventricular partition. CMR, or CT when appropriate, can define the anatomy; catheterization helps clarify severity when symptoms or RV dysfunction need hemodynamic explanation.'),
  S('Treatment Implications',
   '**Symptomatic moderate or greater DCRV obstruction is a surgical muscle-bundle repair problem.** The 2025 guideline recommends repair for otherwise unexplained heart-failure symptoms, cyanosis or exercise limitation in that setting.',
   'Standard pulmonary balloon valvuloplasty treats suitable valvar stenosis and does not remove a muscular intracavitary partition. The normal valve and small distal-RV-to-PA pressure difference make that distinction important here.',
   'Assess associated VSD, valve disease, RV function and arrhythmia before repair. Follow for residual or recurrent obstruction, ventricular remodeling and other associated congenital lesions afterward. An asymptomatic severe lesion also merits expert assessment under current guidance; symptoms alone are not the only marker of future risk. Avoid interpreting the high proximal RV pressure automatically as pulmonary hypertension when the distal RV and PA pressures are low.')],
 ['ACHD2025','DCRV_CASE','VSD_REVIEW'])

add(OUTFLOW,'Bicuspid Valve Aortopathy and First-Degree Relatives',
 'A 41-year-old has a bicuspid aortic valve and a 4.6-cm ascending aorta. His asymptomatic first-degree relatives have normal cardiac examinations. Which initial family-screening strategy best follows the 2022 ACC/AHA aortic guideline?',
 'TTE to assess the valve, aortic root and ascending aorta',[
  ('Resting ECG and ambulatory BP without structural imaging','Electrical and BP assessment can identify other cardiovascular issues but cannot exclude bicuspid valve anatomy or aortic enlargement. A normal examination or ECG is not a substitute for the indicated structural screen.'),
  ('Thoracic CTA as the first test for every relative','CT is useful when echo cannot assess the valve or thoracic aorta adequately and for selected anatomical questions. TTE is the appropriate initial family-screening test rather than exposing every relative to CT by default.'),
  ('Genetic testing first, with imaging restricted to variant carriers','Genetic evaluation is useful in selected heritable aortic-disease settings. Many BAV families do not have an identified pathogenic variant; a negative or uninformative genetic result does not remove the indication for screening imaging.')],
 [S('What the Family Screen Must Include',
   '**BAV and thoracic aortic enlargement can cluster in families and may be clinically silent.** The 2022 guideline recommends first-degree-relative TTE screening when the proband has BAV with a dilated root or ascending aorta.',
   'Assess both valve morphology/function and aortic dimensions. A relative may have aortic dilation even if the valve is tricuspid; looking only for a murmur or counting cusps is incomplete.',
   'If TTE does not visualize the relevant aorta accurately or completely, CT or MRI is indicated to complete the assessment. An affected relative can lead to further family evaluation; normal imaging does not establish one fixed lifelong re-screening interval for every family.'),
  S('Proband Surveillance and Intervention Context',
   '**The 4.6-cm aorta requires follow-up and risk assessment, not automatic isolated aortic replacement from its diameter alone.** Evaluate growth, family history, coarctation, root phenotype, body size and valve indications. The named ACC/AHA framework defines growth of at least 0.3 cm in one year as rapid in BAV.',
   'Within the named 2022 ACC/AHA framework, BAV aortic surgery is recommended at 5.5 cm; selected earlier intervention is reasonable at 5.0–5.4 cm with additional risk, or with a cross-sectional aortic area-to-height ratio at least 10 cm²/m. A diameter of at least 4.5 cm can support concomitant replacement when aortic valve surgery is already being performed.',
   'Use reproducible serial measurements and review symptoms, BP and valve function. The concomitant-surgery threshold must not be mistaken for a universal isolated-operation threshold. Family imaging, the proband’s surveillance and the timing of intervention are related but separate decisions; finding a heritable risk does not mean every family member needs the same test schedule or operation.')],
 ['AORTA2022','BAV_AATS'])
