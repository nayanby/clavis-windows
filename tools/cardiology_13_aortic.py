"""Original concise aortic questions; primary-source review precedes release."""
from qbank_json_chapters import question
REFERENCES={'aorta':('ACC/AHA Aortic Disease Guideline, 2022','https://doi.org/10.1161/CIR.0000000000001106'),
 'esc':('ESC Peripheral Arterial and Aortic Diseases Guideline, 2024','https://doi.org/10.1093/eurheartj/ehae179')}
rows=[]
def B(t,*children):return (t,list(children))
def Q(title,stem,answer,others,sections,table=None,ordered=(),flow=None,refs=('aorta',),calculation=False):
 r=question('Aortic diseases',title,stem,answer,others,sections,list(refs),table=table,calculation=calculation)
 r['explanationStyle']='concise_structured';r['orderedSections']=list(ordered)
 if flow:r['flow']=flow
 rows.append(r)

Q('Anatomical Classification of Aortic Dissection',
 'CTA shows an entry tear distal to the left subclavian artery, with retrograde extension into the ascending aorta. Which classification and initial definitive pathway are appropriate?',
 'Stanford A; emergency open aortic repair',[
 ('Stanford B; anti-impulse therapy and surveillance','This fits disease sparing the ascending aorta without complications; retrograde ascending involvement changes the Stanford category.'),
 ('Stanford B; urgent descending-aortic TEVAR','TEVAR is commonly used for complicated descending dissection; an entry tear there does not negate ascending involvement.'),
 ('Stanford A; planned elective repair after stabilization','Elective repair suits selected stable chronic disease; acute ascending dissection carries immediate rupture, regurgitation and tamponade risks.')],
 [('Classify the Extent',[B('**Stanford depends on ascending involvement, not the entry-tear site.**', 'Any ascending involvement is A; B spares the ascending aorta. Isolated arch disease may require more detailed contemporary classification.')]),
 ('Clinical Consequence',[B('**Urgent surgical assessment and anti-impulse treatment proceed together.**','Medical stabilization is a bridge to repair, not a reason to defer an operable acute type A lesion.'),B('**DeBakey describes origin and propagation.**','I originates in the ascending aorta and extends beyond it; II is confined to ascending; III originates in descending.')])],
 table=(['DeBakey III subtype','Extent'],[['IIIa','Descending thoracic, above diaphragm'],['IIIb','Extends below diaphragm']]))

Q('Dynamic and Static Malperfusion',
 'In type B dissection, renal hypoperfusion varies with pressure. CTA shows compression of the aortic true lumen across the renal ostium without a flap extending into the renal artery. What mechanism predominates?',
 'Dynamic branch-vessel obstruction',[
 ('Static branch-vessel obstruction','Static obstruction results from dissection entering the branch with fixed stenosis or thrombosis; that branch extension is absent here.'),
 ('Renal artery thromboembolism','An embolus creates a branch filling defect and generally fixed occlusion; ostial obstruction varying with true-lumen compression suggests a flap mechanism.'),
 ('Atheroembolic renal disease','Cholesterol emboli affect small vessels, often with skin signs after instrumentation; this is major-ostial perfusion compromise.')],
 [('Mechanism',[B('**Dynamic:** false-lumen pressure compresses the true lumen and obstructs a branch origin.', 'Severity can change with the pressure relationship between lumina.'),B('**Static:** the dissection propagates into the branch, producing fixed narrowing or thrombosis.')]),
 ('Treatment Implications',[B('**Malperfusion makes type B dissection complicated.**','Urgent aortic-team treatment is needed; proximal tear coverage may restore true-lumen flow.'),B('**Persistent branch obstruction may need fenestration or branch stenting.**','Monitor lactate, urine output, abdominal findings and limb perfusion; imaging anatomy alone does not quantify organ injury.')])])

Q('Aortic Dissection Detection Risk Score',
 'A patient with Marfan syndrome has abrupt, severe tearing chest pain, equal pulses and normal blood pressure, with no new murmur or neurological deficit. What is the ADD-RS?',
 '2', [('1','One point would apply if only one risk category were present; this patient has both a predisposing condition and high-risk pain.'),('3','Three requires a high-risk examination category as well; the supplied examination does not provide one.'),('4','ADD-RS is capped at three categories; multiple pain descriptors do not each contribute a separate point.')],
 [('Scoring',[B('**Count positive categories, not individual features.**','Marfan syndrome gives 1 for predisposition; abrupt/severe/tearing pain collectively gives 1; examination gives 0.')]),
 ('Use in Diagnosis',[B('**A high-risk presentation requires definitive imaging.**','D-dimer is an adjunct in selected low-probability pathways, not a replacement for CTA in this case.'),B('**A normal ECG or chest radiograph does not exclude dissection.**','Intramural hematoma, limited disease or thrombosed false lumen can complicate biomarker interpretation.')])],
 table=(['Category','Examples; maximum 1 point each'],[['Predisposition','Heritable aortopathy, family history, known aneurysm, recent aortic manipulation'],['Pain','Abrupt onset, severe intensity, ripping/tearing quality'],['Examination','Pulse/BP differential, painful neurological deficit or new AR, shock']]))

Q('Imaging an Unstable Suspected Aortic Dissection',
 'A patient with suspected proximal dissection has shock and cannot safely leave the resuscitation area. An experienced echocardiographer is immediately available. Which test best provides rapid definitive proximal-aortic information?',
 'Bedside transesophageal echocardiography',[
 ('Contrast-enhanced whole-aorta CT','CTA is preferred in most stable patients and maps branch anatomy; unsafe transfer makes bedside TEE the immediate choice.'),
 ('Aortic magnetic resonance angiography','MRI offers comprehensive imaging without ionizing radiation but is impractical for an unstable patient requiring active resuscitation.'),
 ('Transthoracic echocardiography alone','TTE quickly assesses effusion and regurgitation but incompletely visualizes the thoracic aorta; a negative result cannot exclude dissection.')],
 [('Immediate Information',[B('**TEE assesses proximal flap, AR, tamponade and ventricular function.**','It can be performed bedside or in theatre while surgical management is organized.')]),
 ('Limitations and Complementary Imaging',[B('**A negative study is not universally definitive.**','Distal ascending/arch blind regions and operator dependence matter; persistent suspicion requires further assessment.'),B('**CTA maps the entire aorta and branches when feasible.**','ECG gating reduces proximal motion artifact; MRI is useful for selected stable patients and follow-up.'),B('**Avoid delaying emergency repair** merely to obtain every imaging modality when diagnosis and operative need are established.')])])

Q('Anti-Impulse Therapy in Acute Aortic Syndrome',
 'A hypertensive patient with uncomplicated acute type B dissection has HR 112/min and BP 186/104 mmHg, with preserved perfusion and no beta-blocker contraindication. What is the best initial pharmacological sequence?',
 'IV esmolol, then add nicardipine if pressure remains high',[
 ('IV nicardipine, then add esmolol after pressure normalizes','Nicardipine is useful after rate control; vasodilation first can provoke reflex tachycardia and increase aortic impulse.'),
 ('IV nitroprusside followed by oral metoprolol','Nitroprusside is an adjunct after adequate rate control; oral beta-blockade does not provide the initial rapid titration needed here.'),
 ('Oral labetalol followed by oral amlodipine','Oral drugs suit longer-term control; the acute hypertensive tachycardic emergency requires titratable IV treatment and invasive monitoring.')],
 [('Treatment Sequence',[B('**Analgesia and arterial-line monitoring; initiate IV beta-blockade.**','Esmolol: 500 micrograms/kg over 1 minute, then 50 micrograms/kg/min; titrate to response, commonly up to 200 micrograms/kg/min.'),B('**Add IV vasodilator if needed after rate control.**','Nicardipine 5 mg/hour; increase 2.5 mg/hour every 5–15 minutes, maximum 15 mg/hour.')]),
 ('Targets and Safety',[B('**2022 ACC/AHA:** HR 60–80/min; SBP <120 mmHg or the lowest pressure maintaining organ perfusion.'),B('**Monitor bradycardia, AV block, bronchospasm and hypoperfusion.**','Shock, major malperfusion or acute severe AR requires individualized hemodynamic management rather than automatic target chasing.')])],ordered=['Treatment Sequence'],flow=['Control pain and impulse','Reassess perfusion','Add vasodilator if required'])

Q('Rate Control When Beta-Blockade Is Unsuitable',
 'A patient with acute type B dissection has active severe bronchospasm, HR 118/min and preserved LV systolic function, without shock or AV block. Which IV agent is the most appropriate alternative for initial rate control?',
 'Diltiazem',[
 ('Nicardipine','Nicardipine lowers pressure but does not reliably suppress heart rate; it is added once impulse control is established.'),
 ('Nitroprusside','Nitroprusside rapidly reduces afterload but may trigger reflex tachycardia; it does not replace initial rate control.'),
 ('Amiodarone','Amiodarone treats selected tachyarrhythmias; this sinus tachycardia needs impulse control rather than antiarrhythmic conversion.')],
 [('Alternative Strategy',[B('**IV non-dihydropyridine calcium-channel blockade** can substitute when beta-blockers are contraindicated or not tolerated.','Diltiazem or verapamil slows AV nodal conduction and reduces rate; titrate under continuous monitoring.')]),
 ('Patient Selection',[B('**Preserved ventricular function and adequate pressure matter.**','Avoid this strategy in decompensated systolic failure, significant AV block or hypotension.'),B('**Reassess pressure after rate control.**','Add a titratable vasodilator if needed; maintain organ perfusion and coordinate definitive aortic management.'),B('**This acute alternative does not imply chronic preference** for calcium-channel blockers in every inherited aortopathy.')])])

Q('Complicated Type B Aortic Dissection',
 'Despite analgesia and controlled HR/BP, a patient with acute type B dissection develops rising lactate, abdominal pain and reduced superior mesenteric artery perfusion. The anatomy is suitable for endovascular treatment. What is the best next strategy?',
 'Urgent TEVAR-based repair with assessment of residual branch malperfusion',[
 ('Continue anti-impulse therapy with repeat imaging in one week','Medical management is initial treatment for uncomplicated disease; evolving mesenteric ischemia demands urgent intervention rather than scheduled surveillance.'),
 ('Isolated superior mesenteric thrombolysis without aortic treatment','Thrombolysis treats selected thrombotic occlusions; flap-related malperfusion requires correcting aortic/branch anatomy and carries bleeding concerns.'),
 ('Routine open descending replacement as the preferred first procedure','Open repair remains important when endovascular treatment is unsuitable or fails; suitable complicated type B anatomy generally favors TEVAR.')],
 [('Recognize Complication',[B('**Malperfusion, rupture, extension, progressive enlargement, refractory pain or uncontrolled BP** require escalation.','Normal arm pressure does not establish visceral perfusion; monitor lactate and organ function.')]),
 ('Restore Flow',[B('**TEVAR covers the proximal tear** and expands the true lumen when anatomy permits.'),B('**Check branch vessels after aortic treatment.**','Static obstruction may persist and need fenestration or branch intervention; bowel viability may require surgical assessment.'),B('**Continue anti-impulse therapy and surveillance.**','Intervention does not remove every residual dissected segment or future aneurysm risk.')])])

Q('High-Risk Uncomplicated Type B Dissection',
 'A stable patient with acute type B dissection has no pain, rupture or organ malperfusion after treatment. CTA shows total aortic diameter 43 mm and false-lumen diameter 24 mm. Which statement best reflects the 2022 ACC/AHA approach?',
 'These are high-risk imaging features; selected pre-emptive endovascular management may be considered',[
 ('These measurements establish rupture and mandate immediate open repair','Rupture requires hemorrhage or other rupture evidence; enlargement markers alone identify risk, not established rupture.'),
 ('These measurements prove branch malperfusion and require branch stenting','Branch malperfusion depends on vascular and organ findings; the patient has no supplied perfusion deficit.'),
 ('These measurements have no role until chronic diameter reaches 55 mm','High-risk acute morphology can inform earlier multidisciplinary decisions; chronic aneurysm thresholds do not exhaust the acute assessment.')],
 [('Risk Features',[B('**Examples:** maximal aorta >40 mm; false lumen >20–22 mm; entry tear >10 mm.','Other findings include lesser-curvature entry, interval enlargement, bloody effusion or imaging-only malperfusion.')]),
 ('Qualified Intervention',[B('**Initially uncomplicated does not mean low long-term risk.**','Selected TEVAR can be considered after expert assessment; it is not mandatory for every uncomplicated case.'),B('**Balance remodeling benefit against procedural risk.**','Consider landing zones, connective-tissue disease, stroke/spinal injury risk and follow-up capacity; continue medical treatment whichever pathway is chosen.')])])

Q('Aortic Intramural Hematoma',
 'Noncontrast CT shows crescentic hyperattenuating thickening of the ascending aortic wall. Contrast imaging shows no opacified false lumen or visible intimal flap. Which diagnosis best fits?',
 'Type A intramural hematoma',[
 ('Penetrating atherosclerotic ulcer','An ulcer is a focal contrast-filled crater penetrating atherosclerotic intima; the supplied lesion is crescentic mural blood without that crater.'),
 ('Aortic pseudoaneurysm','Pseudoaneurysm is a contained wall disruption with an outpouching communicating with the lumen; no focal outpouching is described.'),
 ('Uncomplicated mural thrombus','Luminal thrombus lies within the intimal boundary and usually lacks the characteristic acute hyperattenuating intramural crescent.')],
 [('Imaging Pattern',[B('**Intramural blood without a perfused false lumen** can produce acute aortic syndrome.','Absence of a visible flap does not make the lesion benign; progression to dissection or rupture can occur.')]),
 ('Management by Location',[B('**Ascending involvement generally prompts urgent surgical management.**','Selected high-operative-risk type A cases without high-risk imaging may be managed expectantly in expert centers, not by routine outpatient observation.'),B('**Uncomplicated type B IMH can start with medical treatment.**','Complications or high-risk progression change the intervention threshold; noncontrast and contrast CT provide complementary information.')])])

Q('Surveillance After Aortic Dissection',
 'After successful proximal repair of type A dissection, a patient has a residual dissected descending aorta. Which CT/MRI schedule is recommended by the 2022 ACC/AHA guideline if findings remain stable?',
 'At 1, 6 and 12 months, then annually',[
 ('At 6 months, then every three years','Long intervals may suit selected small stable aneurysms; residual dissection requires earlier and continuing annual cross-sectional assessment.'),
 ('At 12 months, then only for recurrent symptoms','Aortic enlargement may be asymptomatic; symptom-driven imaging misses progressive residual disease after proximal repair.'),
 ('Every month for the first year, then every five years','Monthly imaging is not the standard stable follow-up schedule, and five-year intervals are too long for residual dissection.')],
 [('Why Follow-up Continues',[B('**Repair treats the immediate segment, not the entire aortopathy.**','Residual false-lumen flow, distal expansion and new aneurysm formation may require later intervention.')]),
 ('Long-Term Care',[B('**CT or MRI at 1, 6, 12 months and annually if stable.**','New symptoms or growth require earlier evaluation; compare consistent measurement planes and techniques.'),B('**Continue BP/heart-rate control**, commonly beta-blockade with additional agents as needed.'),B('**Assess familial disease and counsel activity.**','Screen relatives when appropriate; avoid intense isometric strain and individualize aerobic activity and pregnancy planning.')])])

Q('Family Screening in Thoracic Aortic Disease',
 'A 42-year-old has a root aneurysm and a father who died from aortic dissection. A multigene panel finds no pathogenic variant. What should be offered to first-degree relatives?',
 'Aortic imaging despite the negative genetic panel',[
 ('Imaging only if a relative develops hypertension','Hypertension raises risk but is not required for familial thoracic aortopathy; waiting for it can miss silent dilation.'),
 ('Cascade testing of a variant of uncertain significance as a definitive risk classifier','A VUS does not establish a disease-causing genotype and should not replace phenotype-based family imaging.'),
 ('No screening because the genetic panel excludes inherited disease','Current panels do not identify every causal variant; a negative result cannot negate the strongly suggestive family history.')],
 [('Genetic Evaluation',[B('**Young presentation, syndromic features or family history** support genetic counseling and testing.','A pathogenic/likely pathogenic variant enables targeted cascade testing; a VUS requires cautious interpretation.')]),
 ('Imaging Relatives',[B('**Screen first-degree relatives with TTE**, adding CT/MRI when the root or ascending aorta is incompletely seen.'),B('**Negative genetic testing does not exclude heritability.**','Determine repeat imaging from age, baseline dimensions and family events.'),B('**Recognize gene–phenotype patterns:** FBN1 in Marfan; TGFBR1/2 in Loeys–Dietz; COL3A1 in vascular Ehlers–Danlos; ACTA2 in nonsyndromic familial disease.')])])

Q('Screening for Abdominal Aortic Aneurysm',
 'A 67-year-old man with a 30-pack-year smoking history, now abstinent, has no abdominal symptoms and no prior aortic imaging. What screening test is appropriate?',
 'One-time abdominal aortic ultrasound',[
 ('Contrast abdominal CT as the initial screening test','CTA is valuable for symptomatic disease and repair planning; ultrasound provides screening without contrast or radiation.'),
 ('Abdominal MRI every year beginning now','MRI can characterize aortic disease but is unnecessary as repeated screening in an otherwise eligible unscreened asymptomatic patient.'),
 ('No screening after smoking cessation','Ever-smoking remains an eligibility factor; cessation improves risk but does not erase the accumulated aneurysm risk.')],
 [('Eligibility',[B('**Men aged ≥65 who have ever smoked** are a standard ACC/AHA screening group.','Family history also informs screening; other organizations specify different age windows and selective eligibility.')]),
 ('Interpret and Act',[B('**AAA is conventionally diameter ≥3.0 cm.**','Document maximal diameter with a consistent measurement convention; body size and morphology can modify clinical interpretation.'),B('**Ultrasound is first-line for screening and surveillance.**','Use CT when ultrasound is inadequate or detailed anatomy is needed.'),B('**Screening is preventive, not an emergency pathway.**','Pain, shock or suspected rupture requires immediate clinical/vascular assessment rather than routine screening scheduling.')])])

Q('Sex-Specific AAA Surveillance',
 'An asymptomatic woman has a stable fusiform infrarenal AAA measuring 4.6 cm, with no rapid growth. Under the 2022 ACC/AHA framework, what is the usual ultrasound surveillance interval?',
 'Every 6 months',[
 ('Every 3 years','Three-year surveillance applies to uncomplicated 3.0–3.9 cm AAA; this lesion is substantially closer to the female repair threshold.'),
 ('Every 12 months','Annual imaging applies to women with 4.0–4.4 cm AAA; women at 4.5 cm or greater need shorter surveillance.'),
 ('Every 24 months','Two-year intervals are not the recommended schedule for a woman with a 4.6 cm AAA approaching intervention size.')],
 [('Surveillance',[B('**Sex-specific intervals reflect different rupture risks at a given diameter.**','This 4.6 cm aneurysm falls in the six-month group, not the male 4.0–4.9 cm annual group.')]),
 ('Change the Plan When Needed',[B('**New attributable pain or rapid enlargement** triggers earlier evaluation, regardless of the scheduled interval.'),B('**Use reproducible measurements.**','Small differences between modalities or planes may reflect technique; confirm clinically important growth.'),B('**Treat vascular risk:** smoking cessation, BP control and atherosclerotic risk reduction; these do not replace surveillance.')])],
 table=(['Diameter','Interval'],[['3.0–3.9 cm, either sex','3 years'],['Men 4.0–4.9; women 4.0–4.4 cm','1 year'],['Men ≥5.0; women ≥4.5 cm','6 months']]))

Q('Elective AAA Repair Thresholds',
 'An otherwise fit woman has an asymptomatic fusiform infrarenal AAA measuring 5.1 cm on reproducible imaging. Under 2022 ACC/AHA guidance, which is the best next step?',
 'Refer for elective repair assessment now',[
 ('Continue surveillance until the diameter reaches 5.5 cm','The usual male threshold is 5.5 cm; applying it unchanged to women overlooks the recommended female threshold of 5.0 cm.'),
 ('Defer repair assessment until growth reaches 0.5 cm in six months','Rapid growth is an additional reason for intervention, not a prerequisite after the sex-specific diameter threshold is reached.'),
 ('Proceed directly to emergency repair without anatomical planning','Emergency intervention applies to rupture or unstable symptomatic disease; this stable elective case needs anatomical and operative assessment.')],
 [('When to Repair',[B('**2022 ACC/AHA: ≥5.5 cm in men; ≥5.0 cm in women.**','Symptoms attributable to the aneurysm, rapid growth or unstable morphology can justify earlier repair.')]),
 ('Choose the Procedure',[B('**CTA defines neck, visceral branches and iliac access.**','EVAR suitability depends on seal zones and device anatomy, not diameter alone.'),B('**EVAR reduces early invasiveness but requires lifelong surveillance.**','Open repair may provide better durability for selected fit patients or unsuitable endovascular anatomy.'),B('**Discuss life expectancy and operative risk** before committing to either strategy.')])])

Q('Rapid Growth of a Sporadic Ascending Aneurysm',
 'A sporadic ascending aneurysm measures 4.7, 5.0 and 5.3 cm on standardized gated CT examinations exactly one year apart. There is no heritable syndrome. Under 2022 ACC/AHA guidance, what does this establish?',
 'A growth-rate indication for surgery despite diameter below 5.5 cm',[
 ('Surveillance only because growth is below 0.5 cm in the latest year','The alternative criterion is at least 0.3 cm/year in two consecutive years; both annual increments meet it.'),
 ('A growth indication only if the patient also has a bicuspid valve','The two-year 0.3 cm/year criterion applies to sporadic root/ascending aneurysms; BAV is not required.'),
 ('A diagnosis of acute dissection based on enlargement alone','Serial growth increases risk but does not prove a dissection flap or acute aortic syndrome.')],
 [('Confirm Growth',[B('**Sporadic root/ascending rapid growth:** ≥0.5 cm in one year OR ≥0.3 cm/year for two consecutive years.','Use comparable tomographic measurements; apparent growth from technique changes is not equivalent evidence.')]),
 ('Operative Assessment',[B('**Surgery is indicated when confirmed rapid growth meets this framework.**','Symptoms attributable to the aneurysm or diameter ≥5.5 cm are separate indications.'),B('**Selected patients may undergo repair at ≥5.0 cm** in experienced multidisciplinary aortic centers.'),B('**Heritable disease and BAV use additional risk-specific criteria** rather than applying every sporadic threshold unchanged.')])])

Q('Marfan Aortic Root Intervention',
 'A patient with Marfan syndrome has a 4.7 cm aortic root and a first-degree relative who dissected at a small diameter. Which 2022 ACC/AHA approach is most appropriate?',
 'Discuss root replacement now at an experienced aortic center',[
 ('Wait until 5.5 cm because this is an asymptomatic aneurysm','The general sporadic threshold is too high for Marfan aortopathy, particularly with a high-risk family history.'),
 ('Wait until 5.0 cm regardless of family history','Five centimeters is the usual Marfan threshold without added risk; high-risk features support considering repair from 4.5 cm.'),
 ('Use thoracic endografting as the preferred definitive root treatment','Root replacement is generally open surgery; routine TEVAR does not provide a durable solution for the root and valve apparatus.')],
 [('Thresholds',[B('**Marfan root replacement:** recommended at ≥5.0 cm; reasonable at ≥4.5 cm with high-risk features.','Family dissection, rapid growth and adverse root/aortic morphology inform individualized decisions.')]),
 ('Treatment Before and After Repair',[B('**Beta-blocker or ARB at maximally tolerated doses** slows dilation; combination therapy may be reasonable.'),B('**Continue lifelong imaging.**','Root replacement does not eliminate distal disease; screen relatives and plan pregnancy before conception.'),B('**Valve-sparing versus composite root replacement** depends on valve anatomy, expertise and patient preferences.')])])

Q('Loeys–Dietz Aortopathy',
 'A young adult has arterial tortuosity, hypertelorism, a bifid uvula and a pathogenic TGFBR2 variant. The aortic root is 4.3 cm. Which principle should guide the repair discussion?',
 'Use genotype- and phenotype-specific thresholds that may be below 5.0 cm',[
 ('Apply the sporadic 5.5 cm threshold without modification','Sporadic thresholds do not account for dissection at smaller dimensions in heritable TGF-beta-pathway aortopathy.'),
 ('Use the Marfan 5.0 cm threshold for every TGFBR2 carrier','Risk differs by gene, phenotype and family history; a single universal Marfan threshold can delay needed assessment.'),
 ('Base intervention solely on a normal exercise stress test','Stress testing evaluates functional ischemia or exercise response, not the mechanical dissection risk of a fragile aortic wall.')],
 [('Recognize the Syndrome',[B('**Loeys–Dietz:** TGF-beta signaling-pathway disease with aneurysm/tortuosity and variable craniofacial features.','Absence of a classic external phenotype does not exclude genetically confirmed disease.')]),
 ('Individualize Risk',[B('**Gene, sex/body size, growth, family events and severe extra-aortic features** influence intervention.','Some TGFBR1/2 patients warrant discussion around 4.0–4.5 cm; the exact threshold requires the applicable risk table.'),B('**Image beyond the root.**','Head-to-pelvis arterial assessment detects extra-aortic aneurysms and tortuosity; continue periodic surveillance and family evaluation.')])])

Q('Repair of a Descending Thoracic Aneurysm',
 'A 73-year-old with a degenerative 5.8 cm descending thoracic aneurysm has suitable landing zones and access, with no Marfan, Loeys–Dietz or vascular Ehlers–Danlos syndrome. Which approach is generally favored under ACC/AHA guidance?',
 'TEVAR rather than open repair when intervention is appropriate',[
 ('Open repair is preferred solely because the diameter exceeds 5.5 cm','Diameter establishes the usual repair threshold but does not itself favor open surgery over anatomically suitable TEVAR.'),
 ('Surveillance until 6.5 cm because the aneurysm is asymptomatic','The usual descending thoracic threshold is 5.5 cm; asymptomatic status does not mandate waiting to 6.5 cm.'),
 ('Medical therapy alone because endovascular repair lacks any role in degenerative disease','Degenerative descending aneurysm is a principal TEVAR setting; medical treatment accompanies rather than universally replaces indicated repair.')],
 [('Selection',[B('**Descending TAA repair is generally recommended at ≥5.5 cm.**','Symptoms, rapid growth or other rupture-risk features may lower the threshold; high operative risk may raise it.')]),
 ('Procedural Planning',[B('**TEVAR is favored over open repair in suitable anatomy without the named heritable syndromes.**','Assess access, seal zones, left-subclavian coverage and spinal-cord perfusion risk.'),B('**Open repair remains important** for unsuitable anatomy and selected durable-repair needs.'),B('**Thoracoabdominal disease uses different thresholds:** usually ≥6.0 cm; ≥5.5 cm may be reasonable in experienced centers.')])])

Q('Infective Aortic Aneurysm',
 'A patient with Salmonella bacteremia has persistent back pain and a new irregular saccular aortic lesion with surrounding inflammatory tissue. Which treatment strategy is most appropriate?',
 'Culture-directed prolonged IV antibiotics plus urgent aortic repair assessment',[
 ('Short-course oral antibiotics followed by routine annual surveillance','A superficial infection may need a short course, but infected aortic tissue risks rupture and usually requires prolonged therapy and source control.'),
 ('High-dose glucocorticoids for presumed sterile inflammatory aneurysm','Sterile periaortitis can require immunosuppression; bacteremia and an evolving saccular lesion favor infection, which steroids could worsen.'),
 ('Elective repair only after the usual fusiform diameter threshold is reached','Degenerative size thresholds do not safely govern infected aneurysms; infection can cause rapid wall destruction and rupture at smaller sizes.')],
 [('Diagnosis',[B('**Infective aortitis/aneurysm:** bacteremia plus compatible wall or periaortic changes.','Salmonella and S. aureus are important causes; obtain cultures and assess other infectious foci.')]),
 ('Management',[B('**Antibiotics and aortic source control are coordinated.**','Prolonged IV therapy is generally at least six weeks, individualized by organism, repair and persistent infection.'),B('**Repair timing and technique depend on instability and anatomy.**','Open debridement/reconstruction or selected endovascular bridging/treatment needs expert discussion; infection surveillance remains essential.'),B('**“Mycotic” does not mean fungal**; most such aneurysms are bacterial.')])])

Q('Type I Endoleak',
 'After EVAR, arterial-phase CTA shows contrast entering the aneurysm sac alongside the proximal graft attachment. Which interpretation and action are most appropriate?',
 'Type Ia endoleak; prompt correction of the proximal seal',[
 ('Type II endoleak; surveillance if the sac is stable','Type II reflects retrograde collateral filling, not direct inflow at the graft attachment site described here.'),
 ('Type IV endoleak; expect spontaneous resolution of graft porosity','Type IV arises through porous graft material, usually early; a discrete proximal attachment leak indicates failed seal.'),
 ('Type V endoleak; investigate occult sac pressurization','Type V is sac expansion without a demonstrable leak; visible direct proximal inflow establishes another mechanism.')],
 [('Why It Matters',[B('**Attachment-site leaks transmit systemic pressure to the sac.**','Type Ia is proximal, Ib distal; prompt repair is needed because successful graft deployment has not excluded the aneurysm.')]),
 ('Comparison and Follow-up',[B('**Type II:** retrograde lumbar/IMA flow; stable sacs can be observed, enlargement prompts reassessment/intervention.'),B('**Type III:** component separation or fabric failure; also a high-pressure leak requiring correction.'),B('**Type IV:** porosity; **type V:** endotension without identified leak.','Surveillance assesses sac size, migration and graft integrity, not merely the presence of contrast.')])])

Q('Type III Endoleak',
 'Three years after EVAR, CTA shows aneurysm sac expansion and contrast passing through a gap between modular graft components. What is the most appropriate diagnosis?',
 'Type III endoleak',[
 ('Type I endoleak','Type I is loss of proximal or distal attachment seal; the described defect lies between components rather than at a native-vessel seal.'),
 ('Type II endoleak','Type II comes from collateral backflow such as lumbar or inferior mesenteric arteries; a modular gap is a graft-integrity failure.'),
 ('Type V endoleak','Type V denotes enlargement without a visible source; this study demonstrates a specific high-pressure communication.')],
 [('Mechanism',[B('**Type IIIa:** component disconnection; **IIIb:** fabric disruption.','Both can directly pressurize the excluded sac and require prompt correction.')]),
 ('Management',[B('**Endovascular relining or component bridging** may restore graft integrity; open conversion is used when necessary.'),B('**Evaluate seal zones and the whole graft**, because more than one leak mechanism may coexist.'),B('**Late surveillance remains necessary.**','An initially satisfactory EVAR result does not exclude delayed migration, separation or sac expansion; compare serial measurements and images.')])])

Q('Symptomatic AAA Below the Elective Size Threshold',
 'A 70-year-old man has new persistent abdominal and back pain, a tender 4.8 cm infrarenal AAA and no alternative cause on CTA. There is no free rupture and he is stable. What is the best next step?',
 'Admit for urgent vascular repair assessment and monitored optimization',[
 ('Continue six-month ultrasound surveillance because diameter is below 5.5 cm','Size-based surveillance applies to asymptomatic stable aneurysms; new attributable pain changes the repair indication.'),
 ('Treat pain and reassess after a routine outpatient interval','Analgesia is supportive but does not remove the risk signaled by a newly symptomatic aneurysm; inpatient urgent evaluation is needed.'),
 ('Begin therapeutic anticoagulation for mural thrombus as the principal treatment','Mural thrombus is common within AAA; it is not by itself an indication for anticoagulation or an explanation permitting delayed repair assessment.')],
 [('Symptomatic Disease',[B('**Attributable pain or tenderness warrants repair evaluation irrespective of usual elective diameter.**','Exclude alternative diagnoses, contained rupture and infection; absence of free rupture does not establish benign disease.')]),
 ('Immediate Care',[B('**Monitor, control pain and BP, and involve the vascular team.**','Stable patients permit rapid anatomical planning and optimization; deterioration requires emergency intervention.'),B('**CTA defines anatomy and complications.**','Aneurysm-related embolization, fistulation or rapid growth can also justify intervention below standard fusiform thresholds.'),B('**Long-term care continues after repair:** tobacco cessation, cardiovascular prevention and procedure-specific surveillance.')])])

# Complete source frameworks within the existing decisions, avoiding duplicate MCQs.
rows[0]['sections'][0][1].append(B('**Timing:** hyperacute <24 hours; acute 1–14 days; subacute 15–90 days; chronic >90 days.','Anatomical involvement and complications determine immediate treatment; duration is a separate classification axis.'))
rows[14]['table']=(['Aortopathy (2022 ACC/AHA)','Selected repair criteria'],[
 ['Sporadic root/ascending','≥5.5 cm; ≥5.0 cm reasonable at experienced centers; confirmed rapid growth or attributable symptoms'],
 ['BAV root/ascending','≥5.5 cm; 5.0–5.4 cm with added dissection risk; ≥4.5 cm reasonable during surgical valve repair/replacement'],
 ['Marfan root','≥5.0 cm; ≥4.5 cm with added high-risk features'],
 ['Heritable disease/BAV growth','≥0.3 cm in one year is rapid growth; apply the relevant disease-specific framework']])
rows[21]['sections'][0][1].append(B('**Suspected rupture:** new abdominal/back pain with hypotension, sometimes a pulsatile mass.','The complete triad is often absent; unstable patients need immediate vascular resuscitation and repair planning, not delay for routine surveillance imaging.'))
