"""Atrial-shunt mapping and qualified closure decisions for adult CHD."""
from qbank_json_chapters import question as Q

TOPIC='Atrial septal defects and atrioventricular septal anatomy'
REFERENCES={
 'SV_REGISTRY': ('Covered-stent sinus venosus correction: international registry, 2025', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11913232/'),
 'ASD_TREAT_REPAIR': ('Treat-and-repair strategy for ASD with PAH: multicentre cohort', 'https://doi.org/10.1136/heartjnl-2021-319096'),
 'ASD_BALLOON': ('Balloon occlusion versus actual ASD closure hemodynamics, 2023', 'https://pubmed.ncbi.nlm.nih.gov/36640419/'),
 'SILDENAFIL_LABEL': ('Sildenafil PAH prescribing information, FDA, 2025', 'https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/203109s019lbl.pdf'),
 'MACITENTAN_LABEL': ('Macitentan prescribing information, DailyMed', 'https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a654726e-f12f-4b03-8bfe-727f26761dce'),
}

def S(h,t,*children):return h,[(t,list(children))]

rows=[Q(
 TOPIC,'Caval Oximetry and Anomalous Pulmonary Venous Drainage',
 'Repeated stable catheter samples on room air show upper SVC saturation 66%, lower SVC near the cavoatrial junction 82%, IVC 68%, RA 80%, RV 81% and PA 81%. TTE shows RV enlargement but no clear fossa-ovalis defect. Which connection most directly explains the earliest saturation step-up?',
 'A right pulmonary vein draining into the SVC',[
  ('A fossa-ovalis communication between the atria','A secundum ASD introduces oxygenated blood at atrial level and can enlarge the RV. A reproducible step-up already within the SVC, above the atrium, directs attention to anomalous pulmonary venous entry rather than assuming an isolated fossa-ovalis lesion.'),
  ('A perimembranous communication between the ventricles','A left-to-right VSD classically introduces oxygenated blood at ventricular level. It does not explain why the lower SVC is substantially more oxygenated than the upper SVC before blood reaches the RA or RV.'),
  ('A persistent connection from descending aorta to pulmonary artery','A PDA introduces oxygenated blood into the pulmonary arterial circulation. It can produce pulmonary overcirculation but would not account for the earliest reproducible step-up within the SVC.')],
 [S('Localizing the Entry of Oxygenated Blood',
   '**The sampling level of the first reliable step-up helps localize a shunt.** Oxygenated pulmonary venous blood entering the SVC can produce a caval increase that is already present before the blood reaches the atrium.',
   'Confirm catheter position and repeat samples because streaming, incomplete mixing and timing can mislead. A contaminated lower-SVC sample should not be accepted as representative pre-shunt mixed venous blood for an oxygen-based flow calculation.',
   'Superior sinus venosus anatomy is frequently associated with anomalous right pulmonary venous drainage. The oximetry result identifies a suspected connection; it does not by itself prove an associated atrial communication or map every pulmonary vein.'),
  S('Anatomical Mapping and Repair',
   '**Define the pulmonary veins and cavoatrial anatomy with appropriate TEE and cross-sectional imaging.** A normal-looking fossa ovalis does not exclude a superior sinus venosus communication or isolated partial anomalous pulmonary venous connection.',
   'CMR can assess flow and RV volume as well as anatomy; CT provides detailed spatial definition when useful for procedural planning. Assess all pulmonary venous connections and any high-draining accessory vein rather than stopping after the first anomaly is found.',
   'Surgery remains an established repair for suitable significant lesions. Selected superior sinus venosus defects can instead be treated with a covered SVC stent that separates systemic venous flow from pulmonary venous return. Specialist imaging and test-balloon interrogation must show unobstructed redirection toward the LA. The evidence includes nonrandomized registry experience, so technical success in selected anatomy must not be generalized to every sinus venosus defect. Consider pulmonary venous obstruction, SVC obstruction, residual shunt and other associated lesions when choosing and following the repair.')],
 ['ASE_ASD','ACHD2025','SV_REGISTRY']),
 Q(TOPIC,'ASD With PAH: Response to Therapy and Closure Reassessment',
 'An adult has an unrepaired ASD with RV dilatation and Qp:Qs 1.9. PVR falls from 6.7 to 4.3 Wood units after targeted PAH therapy; wedge pressure is 10 mmHg, resting saturation 97%, and no significant LV disease is present. Which interpretation best fits the 2025 ACC/AHA framework?',
 'Closure can be considered by the ACHD/PH team with ongoing PAH follow-up',[
  ('Closure assessment should wait until PVR reaches 2 Wood units or less','That is the uncomplicated low-resistance pathway, not a universal requirement for every patient with ASD and PAH. The 2025 guideline also permits a specialist treat-and-reassess pathway when PVR initially 5–8 Wood units falls below 5 with therapy.'),
  ('Closure should be paired with planned discontinuation of PAH therapy','Successful shunt closure does not establish resolution of pulmonary vascular disease. Long-term PAH treatment and surveillance may still be needed; medication withdrawal is not a consequence that should be promised as part of this referral.'),
  ('The baseline PVR establishes Eisenmenger physiology and favors nonclosure','Eisenmenger syndrome requires the relevant advanced pulmonary vascular and bidirectional/right-to-left shunt physiology, not an elevated PVR number alone. The supplied net left-to-right shunt, normal resting saturation and treatment response do not establish it.')],
 [S('Qualified Treat-and-Reassess Pathway',
   '**Initial PVR 5–8 Wood units is not equivalent to an uncomplicated closure indication or an automatic diagnosis of Eisenmenger syndrome.** In the named 2025 pathway, reduction below 5 with targeted therapy can make closure beneficial in selected patients with significant shunting, RV dilatation and no important LV disease.',
   'Repeat invasive hemodynamics and review functional status, RV function, oxygenation and anatomy with ACHD and PH specialists. Do not use an improved echocardiographic pressure estimate as a substitute for the resistance assessment needed for this decision.',
   'Treat-and-repair cohorts provide supportive medium-term evidence but involve selected responders and do not establish universal reversibility or a guaranteed survival benefit. Complete versus fenestrated repair is individualized; a residual controlled outlet may be desirable in selected higher-risk physiology.'),
  S('PAH Treatment and Monitoring',
   '**PAH drugs are selected by risk and phenotype; shunt closure does not replace specialist medical care.** A PDE-5 inhibitor and an endothelin-receptor antagonist are common oral treatment classes in eligible patients.',
   'Examples of labeled adult doses are sildenafil 20 mg three times daily and macitentan 10 mg once daily. These examples do not prescribe an identical combination for every ASD patient. Sildenafil must not be combined with organic nitrates or riociguat; monitor pressure and symptomatic adverse effects.',
   'Macitentan is contraindicated in pregnancy. Assess pregnancy status, contraception, hemoglobin, liver status and fluid retention according to its label and clinical context. Reassess treatment response and adverse effects after any intervention. Persistent pulmonary vascular disease may remain clinically important even if the atrial volume load improves. Avoid defect closure in established Eisenmenger physiology, where eliminating the outlet can precipitate RV failure.')],
 ['ACHD2025','ASD_TREAT_REPAIR','SILDENAFIL_LABEL','MACITENTAN_LABEL']),
 Q(TOPIC,'High Left-Heart Filling Pressure Before ASD Closure',
 'A 70-year-old with a large secundum ASD, RV volume overload and Qp:Qs 2.0 has longstanding hypertension and LV hypertrophy. LVEF is 62%, PVR 1.4 Wood units, wedge pressure 24 mmHg and LVEDP 26 mmHg at rest. Which strategy best addresses the main closure hazard?',
 'Optimize left-heart filling pressure and reassess the closure strategy',[
  ('Proceed with standard complete transcatheter ASD closure','Complete device closure is suitable for many significant secundum defects with favorable pulmonary and left-heart physiology. Here resting left-heart filling pressures are markedly elevated, and removing the atrial decompression route can worsen congestion despite low PVR.'),
  ('Choose complete surgical patch closure instead of device closure','Surgery is appropriate for unsuitable device anatomy or associated surgical lesions. A complete patch still abolishes the same decompression route; changing the procedural access alone does not remove the left-heart filling-pressure problem.'),
  ('Start PAH-targeted vasodilation before planning complete closure','Targeted PAH treatment is relevant to precapillary pulmonary vascular disease. This patient has low PVR with high wedge and LV end-diastolic pressures, so the principal issue is left-heart filling disease rather than an indication to lower pulmonary vascular resistance.')],
 [S('Why Low PVR Does Not Establish Closure Safety',
   '**Significant LV filling disease is a separate qualification from pulmonary vascular resistance.** An ASD can allow high-pressure left atrial blood to escape to the right heart; complete closure removes that route and may produce pulmonary congestion.',
   'Preserved LVEF does not exclude impaired relaxation, increased chamber stiffness or HFpEF. The resting wedge pressure and LVEDP supplied here provide direct evidence that the uncomplicated ASD closure pathway cannot simply be applied.',
   'Reassess blood pressure, volume status, ischemia, AV-valve disease and other contributors to high filling pressure. Optimize treatable causes before deciding whether the benefit of reducing right-heart volume load outweighs the left-heart risk.'),
  S('Individualized Assessment and Balloon-Test Limitations',
   '**Discuss complete closure, selected fenestrated repair or nonclosure with an experienced ACHD team after optimization.** These are physiological choices, not a rule that every older patient must remain unrepaired.',
   'The 2025 guideline states that balloon test occlusion may be reasonable, a Class 2b recommendation. It is not a validated stand-alone prediction rule. Retrospective data show that the temporary balloon can overestimate the wedge-pressure increase after actual device closure.',
   'In a 42-patient study, some patients with a substantial wedge rise during balloon occlusion did not have the same rise after device closure. That observation limits interpretation of the test; it does not prove that a patient with markedly elevated resting LV filling pressures is safe for immediate complete closure. Integrate the baseline findings, symptoms, response to treatment and procedural measurements. Maintain individualized follow-up for congestion, residual shunt, RV remodeling and arrhythmia after the selected strategy.')],
 ['ACHD2025','ESC2020','ASD_BALLOON']),
]
