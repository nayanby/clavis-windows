"""General ACHD management with lesion-specific risk."""
from qbank_json_chapters import question as Q
REFERENCES={'PREGNANCY2025':('ESC cardiovascular disease and pregnancy guideline, 2025','https://doi.org/10.1093/eurheartj/ehaf193')}
def S(h,t,*details):return h,[(t,list(details))]
TOPIC='General adult congenital management'
rows=[Q(TOPIC,'Pregnancy Counseling in Eisenmenger Syndrome',
 'A 26-year-old with Eisenmenger syndrome from a large VSD is considering pregnancy. She is in functional class II on PAH treatment and has preserved LV ejection fraction. Which preconception recommendation best reflects her cardiovascular risk?',
 'Advise against pregnancy because of very high risk and arrange multidisciplinary counseling and reliable contraception',[
 ('Consider pregnancy acceptable with routine obstetric follow-up because LV ejection fraction is preserved','Preserved systemic LV function is reassuring in some congenital lesions but does not remove severe pulmonary vascular disease, right-heart risk or cyanotic physiology. This patient needs specialist counseling rather than routine follow-up alone.'),
 ('Delay conception until symptoms improve to functional class I, then classify the pregnancy as low risk','Functional improvement is desirable but does not establish reversal of Eisenmenger physiology. A symptom-class change alone cannot reclassify this pulmonary vascular disorder as a low-risk pregnancy condition.'),
 ('Offer preconception VSD closure to remove the pregnancy risk','Closure is appropriate for selected shunts before irreversible pulmonary vascular disease develops. Established Eisenmenger physiology makes defect closure hazardous; it cannot be offered as a simple method of converting the patient to a safe pregnancy phenotype.')],
 [S('Risk Is Determined by Physiology',
  '**Eisenmenger syndrome remains a very high-risk pregnancy condition despite modest symptoms or preserved LV systolic function.** Pregnancy-related circulatory changes can exceed the reserve of the pulmonary circulation and right ventricle.',
  'Systemic vasodilation may worsen right-to-left shunting, while changes in volume and flow can precipitate right-heart failure. Thromboembolism and paradoxical embolism add risk. Delivery and the postpartum period require particular attention; successful progression through early pregnancy does not establish safety.',
  'The mWHO 2.0 framework places pulmonary arterial hypertension in class IV. Current guidance emphasizes transparent counseling about maternal and fetal risks, respect for patient decisions and involvement of a Pregnancy Heart Team with congenital and pulmonary-hypertension expertise.'),
  S('Contraception and Medication Review',
  '**Discuss effective contraception before an unintended pregnancy occurs.** Choose the method with the patient after reviewing thrombotic risk, bleeding, drug interactions and procedural tolerance.',
  'Estrogen-containing contraception should be avoided in cyanotic ACHD because of thromboembolic risk. Long-acting options can be considered with specialist counseling; the insertion setting may need planning when hemodynamic reserve is limited.',
  'Review PAH drugs before conception. Endothelin receptor antagonists carry fetal risk, and some can reduce hormonal contraceptive effectiveness. Medication adjustment requires specialist oversight rather than abrupt withdrawal of essential treatment.'),
  S('If Pregnancy Occurs',
  '**Arrange prompt expert review and shared decision-making.** Discuss all management options, including termination where appropriate, without delaying care or assuming the patient has chosen an option.',
  'If pregnancy continues, coordinated maternal-fetal, ACHD, pulmonary-hypertension and anesthesia care is required throughout pregnancy and postpartum. The team should plan surveillance, treatment and delivery in an experienced center. The availability of intensive monitoring does not eliminate the underlying risk.')],
 ['ACHD2025','PREGNANCY2025','BOSENTAN_LABEL'])]

REFERENCES['AHA_IE_CARD']=('AHA prevention of infective endocarditis wallet card','https://www.heart.org/-/media/files/health-topics/infective-endocarditis/infective-endocarditis-wallet-card.pdf')
rows.append(Q(TOPIC,'Dental Prophylaxis After Congenital Defect Repair',
 'Four adults are scheduled for dental extraction involving gingival manipulation. None has previous endocarditis or a prosthetic valve. Under AHA prevention guidance, which congenital finding supports antibiotic prophylaxis?',
 'A residual VSD jet adjacent to a prosthetic patch placed five years ago',[
 ('A completely closed secundum ASD device placed five years ago with no residual defect','A remote, completely repaired defect without residual shunt or another high-risk condition does not supply the ongoing indication described here. The crucial distinction is the residual defect adjacent to prosthetic material.'),
 ('An isolated bicuspid aortic valve with mild regurgitation','Bicuspid valve disease carries endocarditis risk, but an unoperated native bicuspid valve alone is not among the AHA highest-risk indications for dental antibiotic prophylaxis.'),
 ('A small unrepaired acyanotic muscular VSD without prior endocarditis','An unrepaired acyanotic VSD can predispose to infection, but it does not by itself meet the listed AHA high-risk prophylaxis categories. Unrepaired cyanotic CHD and residual defects adjacent to prosthetic repair material are different categories.')],
 [S('Identify Both the Cardiac and Procedural Indication',
  '**A residual shunt at or adjacent to a prosthetic patch or device is a qualifying repaired-CHD finding.** The elapsed time since repair does not remove that continuing anatomical indication.',
  'The dental procedure must also be relevant: gingival manipulation, work around the periapical region or oral mucosal perforation qualifies. A cardiac diagnosis alone does not mean antibiotics are needed before every dental contact.',
  'Other major AHA high-risk categories include previous IE, prosthetic cardiac valves or valve-repair material, unrepaired cyanotic CHD and transplant-associated structural valvular disease. Increased lifetime infection risk and eligibility for procedural prophylaxis are related but not identical concepts.'),
  S('Regimen and Allergy Assessment',
  '**For an eligible adult able to take oral medication without penicillin allergy, use amoxicillin 2 g once 30–60 minutes before the procedure.** Prophylaxis is a single procedural dose rather than a routine multi-day treatment course.',
  'Review the exact allergy history and current medications before selecting an alternative. The AHA no longer recommends clindamycin for dental prophylaxis. Cephalosporins should not be used in patients with penicillin-associated anaphylaxis, angioedema or urticaria.',
  'If infection is already suspected, diagnostic cultures and an appropriate treatment plan take precedence over simply applying a prophylaxis regimen. A dose intended to prevent dental bacteremia is not adequate therapy for established endocarditis.'),
  S('Long-Term Prevention',
  '**Good oral hygiene and regular dental care remain central.** A prophylactic dose cannot compensate for untreated dental disease or replace prompt assessment of unexplained fever.',
  'Document the repaired anatomy, residual findings and prophylaxis indication so the dentist and cardiologist use the same information. Reassess when anatomy changes. The question uses AHA dental guidance; recommendations for other procedures or other guideline systems should be identified explicitly rather than assumed to be interchangeable.')],
 ['AHA_IE_CARD','ACHD2025']))

rows.append(Q(TOPIC,'Objective Functional Assessment Before Exercise Advice',
 'A stable adult with repaired congenital heart disease reports no limitation but has gradually stopped climbing stairs and cycling. Resting echocardiography is unchanged. The patient can exercise and has no acute illness or test contraindication. Which investigation best quantifies integrated exercise capacity and guides individualized activity advice?',
 'Cardiopulmonary exercise testing with gas exchange, ECG and oxygen saturation monitoring',[
 ('A six-minute walk test as the definitive physiological assessment','Walking distance is useful in established PAH or when reliable CPET cannot be performed. It provides a more limited assessment and does not measure the full gas-exchange and ventilatory response available in this exercise-capable patient.'),
 ('Ambulatory ECG monitoring during usual daily activity','Ambulatory monitoring can identify intermittent arrhythmia and relate it to symptoms. It does not measure oxygen uptake, ventilatory efficiency or exercise capacity under a standardized graded workload.'),
 ('Repeat resting CMR ventricular volumes as the sole basis for exercise clearance','CMR provides important anatomy and ventricular measurements when indicated. Resting volumes alone cannot quantify integrated exertional performance or exclude exercise-related desaturation, chronotropic limitation or arrhythmia.')],
 [S('Recognize Adaptation to Functional Limitation',
  '**Self-reported absence of symptoms can conceal progressive restriction of activity.** A person may avoid demanding tasks rather than describe breathlessness during them.',
  'CPET measures the response to a controlled increasing workload and permits comparison with prior performance. The result integrates cardiovascular delivery, pulmonary gas exchange, peripheral conditioning and effort; it should not be reduced to a single resting imaging measurement.'),
  S('Interpret the Pattern, Not One Number',
  '**Review peak oxygen uptake, ventilatory efficiency, heart-rate response, blood pressure, oxygen saturation and rhythm together.** Interpret values with the congenital anatomy, repair, medication and test quality.',
  'Reduced peak oxygen uptake can reflect cardiac limitation, deconditioning or inadequate effort. A reduced heart-rate response may relate to sinus-node disease, pacing or medication. Exertional desaturation requires assessment of shunting or pulmonary disease rather than a blanket diagnosis of poor fitness.',
  'Serial change is most informative when protocol, effort and clinical conditions are comparable. A concerning trajectory should trigger evaluation for residual hemodynamic lesions, valve dysfunction or arrhythmia. CPET complements anatomical assessment; it does not identify every structural cause by itself.'),
  S('Translate Findings Into Activity Advice',
  '**Encourage appropriate activity using an individualized prescription.** Consider ventricular function, pulmonary pressure, aortic dimensions, arrhythmic risk and cyanosis along with the exercise findings.',
  'Stable patients may benefit from progressive aerobic training and selected resistance exercise. The intensity and supervision should match the lesion and physiological risk; competitive sport requires a more specific assessment than ordinary daily activity.',
  'Severe obstruction, significant aortopathy, uncontrolled arrhythmia or other high-risk findings can alter the plan. Conversely, a congenital diagnosis alone does not justify lifelong inactivity. When CPET is unsafe or cannot yield reliable information, use an appropriate alternative such as a six-minute walk test and interpret its narrower scope explicitly.')],
 ['ACHD2025','AHA_CPET']))

REFERENCES['ACHD_ANESTHESIA']=('ESC and partner societies: anesthesia for ACHD noncardiac surgery, 2026','https://academic.oup.com/ehjvshd/article/2/1/xwaf005/8539866')
rows.append(Q(TOPIC,'Planning Noncardiac Surgery in Fontan Circulation',
 'A clinically stable 31-year-old with Fontan circulation is scheduled for elective laparoscopic abdominal surgery. Ventricular ejection fraction is preserved, but there is mild cyanosis and Fontan-associated liver disease. Which preoperative approach is most appropriate?',
 'Arrange ACHD and anesthesia planning of physiology, procedure location and postoperative support',[
 ('Use the standard acquired-heart-disease risk score as the sole cardiac assessment','General risk tools can contribute information about comorbidity and the operation. They do not adequately encode Fontan preload dependence, venous pathways, cyanosis and organ complications, so they cannot replace congenital assessment.'),
 ('Obtain a normal resting echocardiogram and proceed without further congenital review','Echocardiography is useful, but preserved ventricular systolic function does not establish normal Fontan hemodynamics or exclude extracardiac risk. The surgical and anesthetic effects on the entire circuit require planning.'),
 ('Perform routine coronary angiography before determining whether surgery is feasible','Coronary angiography is appropriate for specific coronary indications. In this patient the major known issues concern Fontan physiology, cyanosis and liver disease; an invasive coronary study is not a universal preoperative requirement.')],
 [S('Evaluate the Patient and the Planned Procedure',
  '**Risk depends on congenital anatomy, current physiology, organ complications and the operation itself.** A childhood procedure described as successful does not make the adult circulation equivalent to a normal biventricular heart.',
  'Review operative records, functional status, rhythm, ventricular and AV-valve function, oxygen saturation, venous pathway patency and relevant imaging. Assess hepatic and renal function, blood count, coagulation and current antithrombotic treatment.',
  'An ACHD cardiologist should help determine the appropriate center, additional investigations, optimization and postoperative observation. Elective procedures allow coordinated planning; urgent procedures require rapid risk assessment without delaying necessary treatment for tests unlikely to change immediate care.'),
  S('Anticipate Fontan Hemodynamic Vulnerability',
  '**Pulmonary flow depends on systemic venous pressure and low resistance without a subpulmonary pump.** Positive-pressure ventilation, pneumoperitoneum and positioning may alter venous return and pulmonary flow.',
  'Avoid hypoxemia, hypercapnia, acidosis and substantial hypovolemia. Balance fluid administration against venous congestion rather than using either unrestricted loading or aggressive depletion. Ventilation and insufflation strategies require individualized discussion with the surgical and anesthesia teams.',
  'Residual right-to-left communication increases concern about paradoxical air embolism. Meticulous line preparation and appropriate air precautions matter. Abnormal venous anatomy may also affect vascular access and interpretation of pressure measurements.'),
  S('Plan Recovery as Well as Induction',
  '**Postoperative pain, hypoventilation, bleeding, arrhythmia and fluid shifts can destabilize the circulation.** Decide monitoring intensity and escalation resources before the procedure.',
  'Anticoagulant interruption and resumption require assessment of the actual indication, procedure bleeding risk and organ function. A blanket rule for every Fontan patient is inappropriate. The plan should identify who will manage postoperative congenital or rhythm problems and when reassessment is needed.',
  'Specialist involvement does not imply every operation requires the same invasive monitoring or intensive-care admission. It permits a proportionate plan based on anatomy, physiology and the anticipated stresses of the procedure.')],
 ['ACHD2025','ACHD_ANESTHESIA']))

rows.append(Q(TOPIC,'Lifelong Surveillance After Tetralogy Repair',
 'A 23-year-old with repaired TOF feels well and asks to stop cardiology follow-up. Current assessment shows normal ventricular function, mild pulmonary regurgitation and no significant residual obstruction. Which follow-up strategy is best supported?',
 'Continue periodic ACHD review with testing intervals tailored to current physiology',[
 ('Schedule the next ACHD visit in five years with earlier review for symptoms','Long intervals can suit selected uncomplicated restrictive defects, and CMR intervals may be several years in stable TOF. However, the 2025 routine ACHD clinical interval for repaired TOF stages A and B is 12–24 months; a five-year imaging interval should not be substituted for clinical review.'),
 ('Arrange annual general cardiology review and obtain CMR only if symptoms appear','Shared cardiology care is useful, but symptom-triggered CMR alone can miss progressive RV remodeling. Congenital expertise and planned objective surveillance remain appropriate even when self-reported function is preserved.'),
 ('Arrange annual ACHD visits with annual CMR irrespective of serial findings','Annual assessment and more frequent CMR can be appropriate with important residual lesions or deterioration. In the supplied stable phenotype, annual CMR is more intensive than the qualified 3–5-year routine interval and should be justified by a specific clinical question.')],
 [S('Repair Changes the Disease Trajectory',
  '**Repair relieves the original cyanotic and obstructive physiology but leaves a circulation requiring longitudinal assessment.** Pulmonary valve dysfunction, residual obstruction, ventricular remodeling and surgical scar can have later consequences.',
  'Patients may adapt to slowly declining exercise capacity. Waiting for overt symptoms can miss a period when objective changes already warrant closer review or intervention assessment. Preserve operative records and ensure a planned transition from pediatric to adult congenital care.'),
  S('Choose the Test and Interval for the Question',
  '**Clinical assessment, ECG and imaging provide complementary information.** Echocardiography assesses valve and outflow findings; CMR quantifies RV volumes, function and pulmonary flow when required.',
  'The 2025 guideline lists ACHD visits every 12–24 months for repaired-TOF physiological stages A and B. In patients with normal ventricular function and no more than mild pulmonary regurgitation, CMR can be obtained every 3–5 years. These are qualified routine intervals, not instructions to defer evaluation of new symptoms.',
  'Palpitations, syncope, new desaturation, declining exercise capacity or changing imaging findings warrant earlier assessment and selected rhythm or exercise testing. More advanced physiological stages require closer follow-up.'),
  S('Maintain a Broader Adult Care Plan',
  '**Surveillance also addresses exercise, reproductive health, procedural planning and acquired cardiovascular risks.** The congenital diagnosis should remain visible to clinicians treating otherwise unrelated conditions.',
  'Explain what changes should prompt contact and provide a clear follow-up schedule. Shared care can improve access, but responsibility for congenital surveillance should be explicit. Neither the word repaired nor an isolated normal ejection fraction proves that all future risk has disappeared.',
  'The same principle applies across ACHD, but the schedule is lesion-specific. Do not copy the TOF interval to every repaired ASD, systemic RV or Fontan circulation; use the actual anatomy and current physiological burden.')],
 ['ACHD2025','ESC2020']))
