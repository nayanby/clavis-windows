"""Original initial atrial-shunt questions for the source-matched ACHD chapter."""
from qbank_json_chapters import question as Q

REFERENCES = {
 'ACHD2025': ('ACC/AHA multisociety ACHD guideline, 2025', 'https://doi.org/10.1016/j.jacc.2025.09.006'),
 'ESC2020': ('ESC adult congenital heart disease guideline, 2020', 'https://doi.org/10.1093/eurheartj/ehaa554'),
 'ASE_ASD': ('ASE/SCAI echocardiographic assessment of ASD and PFO, 2015', 'https://www.asecho.org/wp-content/uploads/2025/04/2015_ASD-PFO.pdf'),
 'ASD_CLINICAL': ('Merck Manual Professional: atrial septal defect', 'https://www.merckmanuals.com/professional/pediatrics/congenital-cardiovascular-anomalies/atrial-septal-defect-asd'),
 'AUSCULTATION': ('Merck Manual Professional: cardiac auscultation', 'https://www.merckmanuals.com/professional/cardiovascular-disorders/approach-to-the-cardiac-patient/cardiac-auscultation'),
}
TOPIC='Atrial septal defects and atrioventricular septal anatomy'
rows=[]

def S(h,t,*children):return h,[(t,list(children))]
def add(*args,**kwargs):rows.append(Q(*args,**kwargs))

add(TOPIC,'Atrial Shunting and the Pulmonary Flow Murmur',
 'An adult with a secundum ASD has RV enlargement, wide fixed splitting of S2 and a grade 2/6 midsystolic murmur at the upper left sternal border. Doppler shows no pulmonary valve stenosis. What principally generates this murmur?',
 'Increased systolic flow across the pulmonary valve',[
 ('High-velocity systolic flow through the atrial defect','A ventricular septal jet can produce a prominent systolic murmur because of its pressure gradient. The atrial communication usually has a much smaller pressure difference; the characteristic ASD ejection murmur is generated downstream by increased pulmonary flow.'),
 ('Systolic regurgitation through the tricuspid valve','Significant tricuspid regurgitation can accompany right-heart dilatation and produces its own usually holosystolic lower-sternal murmur. It does not explain the supplied pulmonary-area ejection murmur with no stated important regurgitation.'),
 ('Dynamic systolic obstruction in the RV outflow tract','Dynamic or fixed RV outflow obstruction can create an ejection murmur and RV pressure loading. The supplied ASD produces a volume-loaded RV and the evaluation excludes pulmonary stenosis; increased flow is the appropriate mechanism here.')],
 [S('Flow and Sound Generation',
   '**The murmur of an uncomplicated ASD is usually a pulmonary flow murmur, not the sound of the interatrial jet.** Recirculated left-to-right flow increases RV stroke volume and pulmonary valve flow.',
   'A large shunt may also cause a tricuspid diastolic flow rumble. Its presence reflects increased inflow and should not automatically be labeled tricuspid stenosis.',
   'Persistent RV loading delays pulmonary closure; changes in systemic venous return and interatrial shunting buffer respiratory variation, producing relatively fixed S2 splitting. A fixed split is a useful clue, but congenital anatomy and hemodynamic significance require imaging.'),
  S('Clinical Assessment',
   '**Establish anatomy, right-heart volume load and pulmonary vascular status before choosing treatment.** TTE is the initial examination; additional transesophageal or cross-sectional imaging is selected when rims, pulmonary veins or RV measurements remain uncertain.',
   'A soft murmur does not imply a small defect. Conversely, a prominent ejection murmur can be caused by valvar stenosis or another high-flow state. Integrate Doppler velocity, valve morphology and chamber loading rather than using loudness as a shunt measurement.',
   'Adults may present with reduced exercise capacity or atrial arrhythmias after years of right atrial enlargement. A suitable significant shunt can merit closure before advanced symptoms, provided pulmonary vascular disease and left-heart filling problems do not make closure hazardous. Do not infer a device indication from auscultation alone. Marked pulmonary hypertension or advanced RV dysfunction can change the usual examination, including the intensity and splitting of S2.')],
 ['ASD_CLINICAL','AUSCULTATION','ESC2020'])

add(TOPIC,'Primum Communication and the Left Atrioventricular Valve',
 'A 42-year-old with an interatrial left-to-right shunt has RV volume loading, PR 240 ms and a superior leftward QRS axis. Echocardiography also shows regurgitation through an abnormal left AV valve. Which defect best fits this combination?',
 'Ostium primum defect in a partial AV septal defect',[
 ('Ostium secundum defect at the fossa ovalis','Secundum defects are the common fossa-ovalis lesions and can produce RV volume overload and incomplete right bundle-branch block. The superior axis and associated left AV-valve abnormality instead point to AV septal anatomy.'),
 ('Superior sinus venosus interatrial communication','A superior sinus venosus communication is associated particularly with anomalous right pulmonary venous drainage near the SVC. It can cause right-heart enlargement but does not characteristically explain the combined conduction-axis and left AV-valve findings.'),
 ('Unroofed coronary sinus communication','Unroofing of the coronary sinus may coexist with a persistent left SVC and produce an unusual interatrial shunt. Defining coronary venous anatomy is important in that lesion; the supplied AV-valve and superior-axis combination is more typical of a primum defect.')],
 [S('Anatomy and Electrical Clues',
   '**A primum communication is part of an atrioventricular septal defect, not simply a low fossa-ovalis hole.** The common AV junction and abnormal left AV-valve anatomy determine investigation and repair.',
   'The leftward or superior QRS axis is a useful contrast with the common right-axis/incomplete-RBBB pattern of a secundum ASD. PR prolongation may accompany the conduction anatomy but is not sufficient alone to classify the defect.',
   'Regurgitation may involve the zone of apposition of the left AV-valve leaflets, often described clinically as a cleft. Assess the valve, ventricular components of the septal defect and any associated obstruction rather than considering only the atrial communication.'),
  S('Investigation and Treatment Implications',
   '**Detailed echocardiography must define both the shunt and the AV-valve lesion.** TEE or other imaging is selected when the initial study does not resolve the repair anatomy or pulmonary venous connections.',
   'An indicated partial AVSD repair is generally surgical and can address the left AV valve together with the septal communication. A conventional double-disc secundum device does not correct AV septal anatomy or associated valve dysfunction.',
   'Evaluate pulmonary pressure and resistance, ventricular size/function, exercise capacity and arrhythmias. Catheterization is appropriate when pulmonary vascular status is uncertain. Repair decisions balance the volume load and valve disease against operative and hemodynamic risk. Even after successful repair, residual AV-valve regurgitation, arrhythmia and conduction disease justify individualized follow-up; apparent closure of the atrial opening does not remove those associated risks.')],
 ['ASE_ASD','ESC2020'],
 table=(['Communication','Important associated anatomy'],[
  ['Secundum','Fossa ovalis; assess device rims and pulmonary veins'],
  ['Primum / partial AVSD','AV junction and left AV-valve abnormality'],
  ['Sinus venosus','Caval–pulmonary venous junction; frequently anomalous pulmonary venous connection'],
  ['Unroofed coronary sinus','Coronary sinus roof; assess persistent left SVC'],
 ]))

add(TOPIC,'Ventricular Compliance and Atrial Shunt Magnitude',
 'A woman with an unchanged unrepaired secundum ASD develops hypertension-associated LV hypertrophy over two decades. Her LVEF remains normal, but LV filling pressure rises and left-to-right shunting increases. Pulmonary vascular resistance remains low. Which change most directly explains the increased shunt?',
 'Reduced LV diastolic compliance',[
 ('Reduced RV diastolic compliance','A stiffer RV raises right-sided filling resistance and can reduce left-to-right flow or promote right-to-left flow in an appropriate pressure setting. It does not explain the supplied increase driven by higher left-heart filling pressure.'),
 ('Increased pulmonary vascular resistance','Progressive pulmonary vascular disease raises RV afterload and can ultimately reduce or reverse a systemic-to-pulmonary shunt. The stem documents low resistance, separating this process from the left-heart compliance change.'),
 ('Increased LV diastolic compliance','A more compliant LV accepts filling at a lower pressure and tends to reduce the pressure advantage favoring diversion to the right heart. The patient instead has LV hypertrophy, higher filling pressure and increased left-to-right flow.')],
 [S('Determinants of Atrial-Level Flow',
   '**An atrial-level shunt depends on relative ventricular filling properties as well as communication size.** The normally more compliant RV can receive blood diverted from the left atrium through a substantial defect.',
   'Acquired LV stiffness can increase left atrial pressure and augment left-to-right flow even when the anatomical defect has not enlarged. Preserved ejection fraction does not establish normal diastolic function.',
   'Increasing RV stiffness or pulmonary vascular resistance can move the physiology in the opposite direction. A single shunt ratio therefore does not describe all future behavior of an unrepaired lesion.'),
  S('Why Closure Requires Left-Heart Assessment',
   '**An ASD can partly decompress a high-pressure left atrium.** Eliminating that route in significant LV filling disease can raise left atrial pressure and precipitate congestion.',
   'Assess LV diastolic disease, AV-valve pathology, blood pressure and volume status before closure. In selected patients with suspected high filling pressure, invasive assessment and temporary balloon occlusion can clarify tolerance of closing the communication.',
   'Treat reversible left-heart contributors and use an ACHD team to consider complete closure, a fenestrated strategy or deferral according to the findings. Do not apply the uncomplicated low-PVR closure pathway without checking its left-heart qualifications. Conversely, mild age-related LV abnormalities do not by themselves prohibit intervention. The decision requires the actual pressure response and clinical balance rather than an age cutoff or the assumption that every large shunt must be fully closed.')],
 ['ESC2020','ACHD2025'])

add(TOPIC,'ASD Closure for Right-Ventricular Volume Overload',
 'An asymptomatic 38-year-old has an unrepaired secundum ASD, Qp:Qs 1.9 and definite RV dilatation. Catheterization shows PVR 1.6 Wood units and no significant LV filling disease. Imaging shows adequate rims. Which approach best fits the 2025 ACC/AHA ACHD recommendation?',
 'Refer for anatomically appropriate ASD closure',[
 ('Continue surveillance until exercise symptoms develop','Surveillance is suitable for a small shunt without important chamber loading or when intervention risk outweighs benefit. The guideline recommendation here is driven by significant left-to-right flow and RV dilation with favorable pulmonary and left-heart physiology, not by waiting for symptoms.'),
 ('Start PAH-targeted treatment before reconsidering closure','PAH treatment and reassessment can form part of selected specialist pathways with elevated pulmonary vascular resistance. PVR 1.6 Wood units does not identify that problem and does not justify introducing PAH drugs to prepare for uncomplicated closure.'),
 ('Use chronic diuretics to reduce the need for closure','Diuretics can relieve congestion or optimize volume status in selected patients. They do not remove the continuing right-heart volume burden of an otherwise suitable significant ASD and are not an equivalent definitive strategy in this asymptomatic favorable-risk case.')],
 [S('Named Guideline Criteria',
   '**The 2025 ACC/AHA pathway recommends closure for an unrepaired ASD with Qp:Qs at least 1.5 and RV dilatation when PVR is no more than 2 Wood units and significant LV disease is absent.** All those qualifications are supplied here.',
   'This is a lesion-specific recommendation. A shunt ratio alone does not establish suitability if the RV is not volume loaded, pulmonary vascular disease is substantial or closure would cause a problematic rise in left-heart filling pressure.',
   'Older ESC guidance uses different PVR categories, including below 3 Wood units for its straightforward pathway. Name the framework and year instead of merging thresholds into an unqualified universal rule.'),
  S('Anatomy, Procedure and Follow-Up',
   '**For a suitable secundum defect, transcatheter closure is generally the preferred approach.** Assess size, rims, adjacent structures, pulmonary venous connections and any other lesion needing surgery.',
   'Primum/AV septal anatomy and unsuitable secundum rims can require surgical repair. Sinus venosus anatomy needs specialist mapping and lesion-specific procedural assessment rather than a standard fossa-ovalis device assumption.',
   'Discuss procedural complications, residual shunt, device thrombus and atrial arrhythmia risk. ESC 2020 specifies antiplatelet treatment for at least six months after device closure, with aspirin at least 75 mg once daily; individualize for allergy, bleeding risk, other antithrombotic indications and device protocol. Follow-up imaging documents position, residual flow and right-heart remodeling. Closure does not automatically erase an established atrial arrhythmia substrate. The referral addresses an existing hemodynamic burden rather than promising that every future risk will disappear.')],
 ['ACHD2025','ESC2020','ASE_ASD'])
