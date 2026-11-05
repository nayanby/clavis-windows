"""Original Adult Congenital Heart Disease chapter."""
from qbank_authoring import question, ref, finalize
A=ref('2025 ACC/AHA/HRS/ISACHD/SCAI Adult Congenital Heart Disease Guideline','https://doi.org/10.1161/CIR.0000000000001402')
E=ref('2020 ESC Adult Congenital Heart Disease Guideline','https://doi.org/10.1093/eurheartj/ehaa554')
P=ref('2022 ESC/ERS Pulmonary Hypertension Guideline','https://doi.org/10.1093/eurheartj/ehac237')
rows=[]
def q(*args,**kwargs):rows.append(question(*args,**kwargs))

q('An adult has a fixed wide split second heart sound, a pulmonary flow murmur and right atrial and RV enlargement. Which lesion is most likely?',
 'Atrial septal defect with a significant left-to-right shunt',[
 ('Small restrictive VSD without chamber overload','A small VSD more typically produces a harsh localized systolic murmur and does not explain the classic right-sided volume pattern.'),
 ('Isolated severe aortic regurgitation','AR primarily produces LV volume loading and a diastolic murmur.'),
 ('Uncomplicated mitral prolapse','A click-MR pattern does not explain fixed splitting with RV volume overload.')],
 'ASD produces right-sided volume loading',
 '**A significant atrial left-to-right shunt increases RV and pulmonary flow.**',
 ['The murmur is often a flow murmur across the pulmonary valve rather than flow across the atrial defect itself.', 'Right-sided volume and altered respiratory variation contribute to the fixed split S2.'],
 '**Define the anatomy and consequences rather than treating the murmur alone.**',
 ['Assess defect type, pulmonary venous connections, RV size and pulmonary pressure.', 'An ASD can remain unrecognized until adulthood with dyspnea or atrial arrhythmia.'],
 [['ASD','RA/RV volume overload'],['Small restrictive VSD','High-velocity localized systolic murmur'],['AR','Predominant LV volume overload']], [A,E], 'clinical_scenario')
q('A secundum ASD has Qp:Qs 1.8, RV dilation, PVR 1.6 Wood units and suitable device rims. There is no important LV disease. What is the appropriate management direction?',
 'Evaluate for transcatheter ASD closure',[
 ('Observe indefinitely because symptoms are mild','Significant RV volume loading can justify closure even when symptoms are limited.'),
 ('Treat with diuretics as a permanent substitute for closing the shunt','Diuresis does not remove the atrial communication.'),
 ('Avoid closure solely because the patient is an adult','Age alone does not prohibit closure when hemodynamics and anatomy are suitable.')],
 'Shunt consequence and pulmonary vascular status guide closure',
 '**A significant left-to-right shunt with RV dilation and low PVR supports closure.**',
 ['Secundum anatomy with adequate rims often permits a device approach.', 'Assess associated lesions and left-sided filling pressures before proceeding.'],
 '**Closure decisions change in PAH or significant LV disease.**',
 ['The communication can serve a decompressive role in those settings.', 'Do not generalize a low-PVR case to Eisenmenger physiology.'],
 [['Significant shunt, RV dilation, low PVR','Closure generally appropriate'],['Suitable secundum rims','Potential device closure'],['Severe pulmonary vascular or LV disease','Specialized reassessment']], [A], 'clinical_scenario')
q('Which associated lesion should be actively sought with a superior sinus venosus ASD?',
 'Partial anomalous pulmonary venous connection, often involving right-sided veins',[
 ('A cleft left AV valve as the characteristic association','That is more characteristic of an AV septal/primum defect.'),
 ('Isolated bicuspid aortic valve as the defining companion lesion','It does not define the sinus venosus pulmonary venous anatomy.'),
 ('A patent ductus as an obligatory part of the defect','PDA is not an obligatory sinus venosus component.')],
 'An atrial shunt may be part of a pulmonary venous connection abnormality',
 '**Sinus venosus defects often coexist with anomalous pulmonary venous drainage.**',
 ['The combined lesions increase right-sided volume load.', 'Standard TTE may not define all connections.'],
 '**Use TOE and cross-sectional imaging when anatomy is incomplete.**',
 ['CMR or CT can map pulmonary veins and quantify flow.', 'Repair planning differs from a routine isolated secundum device closure.'],
 [['Secundum ASD','Central septal defect; often device suitable'],['Sinus venosus defect','Assess anomalous pulmonary veins'],['Primum defect','Assess AV valve anatomy']], [A,E])
q('A primum atrial septal defect is found in an adult with MR. Which anatomical issue is particularly relevant?',
 'An associated left AV valve cleft or zone of apposition abnormality',[
 ('A mandatory calcific aortic stenosis mechanism','That is not the defining associated lesion.'),
 ('A prosthetic pulmonary valve','A prosthetic valve is not an intrinsic part of primum anatomy.'),
 ('An isolated pulmonary vein stenosis as the obligatory MR cause','The AV valve abnormality is the key association.')],
 'Primum defects belong to the AV septal defect spectrum',
 '**The atrial communication and AV valve abnormalities arise from a shared developmental anatomy.**',
 ['Regurgitation can be an important part of the clinical burden.', 'Conduction-system anatomy also differs from an isolated secundum defect.'],
 '**Plan a complete repair rather than closing only an atrial hole.**',
 ['Valve function and associated ventricular or outflow lesions require assessment.', 'A routine secundum occluder pathway is not the usual treatment of a primum defect.'],
 [['Primum/AV septal defect','AV valve involvement'],['Secundum defect','Different septal anatomy'],['Management','Address shunt and valve consequences']], [A,E])
q('An older patient with ASD, hypertension and a stiff LV develops a marked rise in left atrial pressure during temporary balloon occlusion. Why does this matter?',
 'Complete closure could precipitate pulmonary congestion by removing an atrial decompression pathway',[
 ('The pressure rise proves closure is harmless','The response identifies a potential adverse filling-pressure consequence.'),
 ('The test measures only coronary flow and has no atrial relevance','The occlusion specifically tests the hemodynamic effect of removing the shunt.'),
 ('Every such patient must receive the same fully closed device without further discussion','Fenestration or no closure may be considered after individualized assessment.')],
 'An ASD can mask impaired LV filling reserve',
 '**Removing the communication can increase left-sided filling pressure in a noncompliant LV.**',
 ['Hypertension and age-related diastolic dysfunction are relevant clues.', 'The shunt benefit and the filling-pressure risk must be balanced.'],
 '**Use an ACHD and structural Heart Team decision.**',
 ['Consider treatment of loading conditions and the possible role of fenestration or deferral.', 'Do not apply low-risk young-patient closure criteria without assessing the older patient\'s physiology.'],
 [['Low PVR with compliant LV','Often tolerates closure'],['Marked LA pressure rise on occlusion','Warns of pulmonary congestion risk'],['Options','Individualized complete, fenestrated or no closure']], [A,E], 'clinical_scenario')
q('Under the 2025 ACC/AHA ACHD guideline, an ASD patient initially has PVR 6.2 Wood units, Qp:Qs 1.9 and RV dilation. After targeted PAH treatment, repeat catheterization shows PVR 3.8 Wood units with a persistent significant left-to-right shunt and no important LV disease. What is appropriate?',
 'Expert-center reassessment for closure because a selected treat-and-repair strategy may now be beneficial',[
 ('Close the defect without repeat hemodynamic review because any vasodilator response guarantees safety','Repeat complete assessment is essential; treatment response is not a universal safety guarantee.'),
 ('Declare closure permanently impossible solely from the initial PVR value','The updated guideline allows selected patients whose PVR falls below 5 after therapy to be considered.'),
 ('Apply the same strategy to established irreversible Eisenmenger shunt reversal','That physiology is not equivalent and routine closure can be dangerous.')],
 'Pulmonary vascular treatment can change selected ASD decisions',
 '**The 2025 framework permits consideration in selected initially high-PVR patients after a documented fall below 5 Wood units.**',
 ['A persistent significant left-to-right shunt and absence of major LV disease are important.', 'The initial range and the full hemodynamic response must match the studied recommendation context.'],
 '**Treat-and-repair is a specialized strategy.**',
 ['Confirm stability, pulmonary flow, pressure and wedge measurements.', 'Do not extrapolate to progressive PAH with cyanosis or irreversible shunt reversal.'],
 [['Selected fall in PVR with persistent L-R shunt','May permit closure assessment'],['Persistent severe pulmonary vascular disease','Closure may be harmful'],['Eisenmenger physiology','Different contraindicating context']], [A], 'clinical_scenario')
q('Why can a small restrictive VSD produce a louder systolic murmur than a very large nonrestrictive VSD?',
 'A large pressure gradient across the small defect produces high-velocity turbulent flow',[
 ('Murmur loudness always rises in direct proportion to anatomical defect size','The pressure gradient and flow characteristics matter, so this direct rule is unreliable.'),
 ('Small VSDs necessarily cause the largest pulmonary flow','A small restrictive defect often limits shunt volume.'),
 ('Large defects have no pressure communication','A nonrestrictive defect allows substantial ventricular pressure communication.')],
 'A loud murmur is not a direct defect-size measure',
 '**Restriction preserves a substantial LV-to-RV pressure difference.**',
 ['High velocity can produce a prominent murmur despite a small shunt.', 'A large defect with high RV pressure may have a less dramatic gradient and murmur.'],
 '**Assess shunt volume, chambers and pulmonary vascular disease directly.**',
 ['Echo and selected catheterization define the consequences.', 'A softening murmur can reflect changed hemodynamics rather than spontaneous improvement.'],
 [['Small restrictive VSD','High velocity, potentially loud murmur'],['Large nonrestrictive VSD','Greater pressure communication'],['Severity assessment','More than auscultatory intensity']], [A,E])
q('A patient with an outlet VSD develops progressive AR. Which mechanism should be considered?',
 'Aortic cusp prolapse into the defect',[
 ('Mandatory primary rheumatic fusion as the only cause','The VSD location can directly affect cusp support.'),
 ('Pulmonary vein obstruction as the direct cusp mechanism','That does not explain prolapse into an outlet defect.'),
 ('A small VSD can never have a valve complication','Even a modest shunt can be associated with important AR.')],
 'VSD anatomy can threaten aortic valve competence',
 '**Loss of support and flow effects near an outlet defect can promote cusp prolapse.**',
 ['The resulting AR may become the main reason for intervention.', 'Shunt magnitude alone does not capture this complication.'],
 '**Follow valve morphology and regurgitation over time.**',
 ['Discuss closure and valve treatment when clinically indicated.', 'Do not reassure solely because ventricular volume overload is limited.'],
 [['Outlet VSD','Assess aortic cusp relationship'],['Progressive AR','Can alter intervention timing'],['Small shunt','Does not exclude valve harm']], [A,E], 'clinical_scenario')
q('During catheterization, systemic arterial saturation is 98%, mixed venous saturation 68%, pulmonary venous saturation 98% and pulmonary arterial saturation 88%. Assuming comparable oxygen-content factors, what is Qp:Qs?',
 '3.0',[
 ('0.33','This is the inverse of the correct flow ratio.'),
 ('1.0','The large pulmonary arterial oxygen step-up indicates a substantial left-to-right shunt.'),
 ('1.5','Using the given Fick differences yields 30 divided by 10, not 1.5.')],
 'Apply the oxygen-content form of the Fick principle',
 '**Qp:Qs equals systemic arteriovenous oxygen difference divided by pulmonary venous-arterial oxygen difference.**',
 ['Here the simplified ratio is (98-68)/(98-88) = 30/10 = 3.', 'Actual catheterization interpretation uses oxygen content and appropriate samples, particularly when inspired oxygen or hemoglobin issues matter.'],
 '**Confirm that the sampled saturations represent the relevant mixed streams.**',
 ['Streaming, anomalous connections and assumptions about pulmonary venous saturation can create error.', 'Flow ratio and pulmonary vascular resistance answer different questions.'],
 [['Systemic difference','98 minus 68 = 30'],['Pulmonary difference','98 minus 88 = 10'],['Qp:Qs','30 divided by 10 = 3']], [A,E])
q('An adult with a large PDA and advanced pulmonary vascular disease has lower-limb cyanosis with relatively preserved right-hand saturation. What explains the distribution?',
 'Right-to-left ductal flow enters the descending aorta distal to the upper-body branches',[
 ('Atrial right-to-left shunting must selectively spare the right hand','An atrial shunt generally mixes blood before systemic distribution.'),
 ('A small restrictive VSD necessarily creates isolated lower-limb cyanosis','That is not the characteristic ductal differential pattern.'),
 ('The pattern proves the pulmonary pressure is normal','Shunt reversal through a PDA can reflect severe pulmonary vascular disease.')],
 'Differential cyanosis localizes the shunt entry',
 '**A ductal communication joins the pulmonary artery to the descending aorta.**',
 ['With shunt reversal, desaturated blood can preferentially reach the lower body.', 'Measure saturations in appropriate upper and lower extremities.'],
 '**Do not close an irreversible Eisenmenger-type ductus reflexively.**',
 ['Specialized hemodynamic and PAH assessment is essential.', 'The same anatomical lesion can have very different management before and after severe vascular remodeling.'],
 [['Usual PDA','Left-to-right aortic-to-pulmonary flow'],['Reversed PDA','Desaturated flow to descending aorta'],['Clinical clue','Lower-body differential cyanosis']], [A,E,P], 'clinical_scenario')
q('Why is routine closure of the original shunt contraindicated in established irreversible Eisenmenger physiology?',
 'The communication can decompress the high-pressure right-sided circulation, and closure can precipitate RV failure',[
 ('Cyanosis means the defect has already closed spontaneously','Cyanosis reflects right-to-left or bidirectional flow, not spontaneous closure.'),
 ('Closing any shunt immediately reverses all pulmonary vascular remodeling','Advanced remodeling is not reliably reversible in this way.'),
 ('The only problem is a cosmetic saturation change','Eisenmenger physiology is a major cardiopulmonary vascular disease.')],
 'A shunt can change from cause to essential pressure relief',
 '**Advanced pulmonary vascular resistance can reverse the initial left-to-right shunt.**',
 ['The RV then faces a high-resistance circulation.', 'Eliminating the outlet can cause severe hemodynamic deterioration.'],
 '**Use PAH and ACHD expertise for management.**',
 ['Targeted therapy, complication prevention and selected advanced options are individualized.', 'Do not extrapolate selected treat-and-repair ASD cases to irreversible cyanotic shunt reversal.'],
 [['Early significant L-R shunt','Closure may prevent complications'],['Irreversible Eisenmenger reversal','Do not routinely close'],['Management','Specialized PAH/ACHD pathway']], [A,E,P])
q('A cyanotic Eisenmenger patient has hematocrit 67% but no hyperviscosity symptoms. What is the appropriate phlebotomy principle?',
 'Do not perform routine phlebotomy solely to normalize the hematocrit',[
 ('Phlebotomize weekly until hematocrit is within the normal noncyanotic range','This can cause iron deficiency and impair oxygen delivery.'),
 ('Assume secondary erythrocytosis is identical to polycythemia vera','It is an adaptive response to chronic hypoxemia with a different treatment context.'),
 ('Use aspirin automatically to neutralize every hematocrit-related risk','Antiplatelet treatment has its own bleeding-risk considerations and is not universal therapy for cyanosis.')],
 'Secondary erythrocytosis supports oxygen carrying capacity',
 '**A high hematocrit alone is not a routine venesection indication in cyanotic CHD.**',
 ['Assess hydration, iron status and symptoms.', 'Selected severe hyperviscosity requires expert evaluation rather than a numerical normalization target.'],
 '**Avoid causing iron-deficient microcytosis.**',
 ['Iron deficiency can worsen exercise capacity and complicate viscosity and oxygen-delivery physiology.', 'Investigate bleeding, nutrition and other contributors when deficiency is present.'],
 [['Adaptive erythrocytosis','Not routinely treated to normal hematocrit'],['Dehydration or iron deficiency','Identify and correct appropriately'],['True symptomatic hyperviscosity','Specialist individualized management']], [A,E], 'clinical_scenario')
q('Which congenital-disease physiology carries particularly high maternal risk in pregnancy?',
 'Pulmonary arterial hypertension with Eisenmenger physiology',[
 ('A completely repaired uncomplicated small ASD with normal pressures','This generally has a different risk profile.'),
 ('An isolated tiny restrictive VSD with normal ventricular function and no PAH','This is not the same high-risk circulation.'),
 ('A successfully treated mild pulmonary stenosis with normal RV function','That does not carry the characteristic PAH pregnancy risk.')],
 'Pregnancy can overwhelm a pulmonary vascular circulation',
 '**PAH and cyanotic shunt physiology confer major maternal and fetal risk.**',
 ['Changes in volume, resistance and the postpartum period can destabilize the RV.', 'Preconception counseling is essential.'],
 '**Use a specialized pregnancy and ACHD team.**',
 ['Discuss contraception, risk and options in a patient-centered manner.', 'If pregnancy occurs, medication and delivery planning need expert coordination rather than routine low-risk obstetric care.'],
 [['Eisenmenger/PAH','Very high pregnancy risk'],['Simple repaired lesion without sequelae','Different risk category'],['Planning','Preconception and multidisciplinary assessment']], [A,E,P])
q('Why are meticulous intravenous air precautions important in a cyanotic congenital patient with right-to-left shunting?',
 'Venous air can bypass the pulmonary filter and embolize into the systemic circulation',[
 ('The shunt guarantees that all air will remain in the lungs','Right-to-left passage can bypass that filter.'),
 ('The concern applies only to patients with high LDL','The mechanism is anatomical, not lipid dependent.'),
 ('Air filtering replaces all infection and thrombosis precautions','It addresses one preventable hazard and does not replace other care.')],
 'Right-to-left shunts permit paradoxical embolization',
 '**Material introduced into the venous circulation may reach systemic arteries.**',
 ['Air and thrombus can have neurological or other organ consequences.', 'Use careful line preparation and appropriate air-elimination practices.'],
 '**Apply anatomy-aware care across procedures.**',
 ['Communicate the shunt to anesthesia and other teams.', 'Avoid assuming routine venous access has the same risk profile as in a person without a shunt.'],
 [['Normal pulmonary passage','Filters many venous embolic materials'],['Right-to-left shunt','Allows systemic passage'],['Prevention','Meticulous venous line and air precautions']], [A,E])
q('Years after transannular-patch repair of tetralogy of Fallot, a patient develops progressive RV dilation. Which residual lesion is a common driver?',
 'Chronic pulmonary regurgitation',[
 ('Isolated severe MR as an obligatory result of the patch','The usual patch-related lesion concerns the RV outflow and pulmonary valve.'),
 ('Aortic coarctation as the defining repair complication','That is not the characteristic transannular-patch consequence.'),
 ('A normal RV with no volume burden','Progressive dilation requires assessment and is not simply a normal finding.')],
 'Relieving childhood RV outflow obstruction can create later volume overload',
 '**A transannular patch can leave important pulmonary valve incompetence.**',
 ['Repeated regurgitant volume loads the RV.', 'Residual obstruction, TR and ventricular scar can coexist.'],
 '**Follow adults with repaired TOF longitudinally.**',
 ['Assess symptoms, exercise capacity, rhythm and biventricular size and function.', 'Anatomical repair does not mean the lifelong disease is cured.'],
 [['Residual PR','RV volume loading'],['Residual outflow obstruction','RV pressure loading'],['Long-term care','Function, rhythm and reintervention assessment']], [A,E], 'clinical_scenario')
q('Which imaging method is particularly useful for serial RV volumes and pulmonary regurgitant fraction after TOF repair?',
 'Cardiac magnetic resonance',[
 ('A resting ECG alone','ECG provides electrical information but does not quantify regurgitant fraction or RV volumes.'),
 ('A coronary calcium score alone','That addresses a different question.'),
 ('A chest radiograph as an equivalent quantitative substitute','Radiography cannot supply the same ventricular and flow measurements.')],
 'CMR quantifies the repaired right-sided circulation',
 '**RV geometry and regurgitant flow can be difficult to quantify fully by echo alone.**',
 ['CMR provides reproducible chamber and flow assessment.', 'Echo remains important for routine hemodynamics and valve review.'],
 '**Use serial trends rather than one isolated volume threshold.**',
 ['Symptoms, exercise performance, RV function, obstruction and arrhythmia all influence pulmonary valve replacement timing.', 'Historical indexed-volume thresholds are decision aids, not the entire contemporary algorithm.'],
 [['CMR','RV volumes and regurgitant fraction'],['Echo','Valve and pressure assessment'],['Timing decisions','Integrate serial functional and clinical findings']], [A,E])

# Late repair physiology and less common congenital lesions follow.
q('An adult with repaired TOF develops sustained monomorphic VT. Which mechanism is particularly important?',
 'Macro-re-entry through anatomical isthmuses related to ventricular scars and patches',[
 ('AV nodal re-entry as the obligatory mechanism of every postoperative VT','AVNRT is supraventricular and is not the characteristic scar-related ventricular circuit.'),
 ('An accessory pathway is required for all ventricular arrhythmias','Scar re-entry does not require an AV accessory pathway.'),
 ('Pulmonary regurgitation excludes an electrical substrate','Hemodynamic lesions and scar-related arrhythmia can coexist.')],
 'Surgical survival creates a distinct adult arrhythmia substrate',
 '**Patches, incisions and valve boundaries can form channels for ventricular re-entry.**',
 ['Ventricular function and residual hemodynamic lesions modify risk.', 'Ablation can target defined anatomical isthmuses in appropriate patients.'],
 '**Assess arrhythmia and hemodynamics together.**',
 ['Review CMR, exercise capacity, QRS features and rhythm history.', 'ICD and ablation decisions are individualized rather than based solely on the childhood repair label.'],
 [['Repaired TOF VT','Often scar/isthmus re-entry'],['Residual valve disease','Contributes to ventricular burden'],['Management','ACHD and electrophysiology expertise']], [A,E], 'clinical_scenario')
q('A repaired TOF patient has severe PR, worsening exercise capacity and progressive RV dilation with declining RV function. Which next step is appropriate?',
 'ACHD Heart Team evaluation for pulmonary valve replacement and the associated arrhythmic substrate',[
 ('Wait for irreversible end-stage RV failure in every patient','Late intervention can reduce the chance of reverse remodeling.'),
 ('Treat only the oxygen saturation despite normal saturation','Normal saturation does not negate significant RV volume overload.'),
 ('Assume a childhood repair eliminates the need for reintervention','Late valve intervention is a common part of TOF care.')],
 'Pulmonary valve replacement timing uses the whole trajectory',
 '**Symptoms, serial RV enlargement and declining function are important intervention signals.**',
 ['CMR supports quantitative follow-up.', 'Residual obstruction, TR and anatomy determine surgical versus transcatheter options.'],
 '**Plan electrical management around the valve intervention.**',
 ['Scar-related VT risk may persist even when regurgitation improves.', 'Preprocedural EP assessment can matter in selected high-risk anatomy and rhythm histories.'],
 [['Progressive PR-related RV burden','Assess replacement before irreversible decline'],['Anatomical suitability','Guides transcatheter versus surgery'],['Arrhythmic risk','Needs separate integrated review']], [A,E], 'clinical_scenario')
q('An adult underwent a Mustard or Senning operation for d-transposition. Which ventricle supports the systemic circulation?',
 'The morphological right ventricle',[
 ('The morphological LV in the normal anatomical arrangement','An atrial switch redirects venous flow but does not perform an arterial switch.'),
 ('Neither ventricle because all flow is passive','That describes a different univentricular circulation concept.'),
 ('The RV only during exercise and the LV at rest','The systemic ventricular assignment does not alternate with activity.')],
 'An atrial switch redirects inflow rather than reconnecting the great arteries',
 '**The morphological RV remains the systemic pump.**',
 ['Systemic RV dysfunction and systemic AV valve regurgitation are important late issues.', 'Atrial arrhythmia, sinus-node disease and baffle problems also require surveillance.'],
 '**Identify the exact historical operation before interpreting adult physiology.**',
 ['Arterial-switch survivors have different coronary and outflow concerns.', 'Generic labels such as repaired transposition can hide major anatomical differences.'],
 [['Mustard/Senning','Systemic morphological RV'],['Arterial switch','Systemic morphological LV'],['Follow-up','Operation-specific complications']], [A,E])
q('A patient after an atrial-switch operation develops exertional desaturation and a suspected venous pathway abnormality. Which complication should be assessed?',
 'Baffle obstruction or leak',[
 ('A routine pulmonary valve leak as the only possible explanation','Atrial-switch venous pathways create specific obstruction and shunt risks.'),
 ('A normal coronary calcium score as definitive exclusion of the cause','Coronary calcium does not assess the baffle.'),
 ('A new ASD is impossible after any operation','A leak in the surgically created pathway can permit abnormal mixing.')],
 'Atrial baffles can obstruct or leak over time',
 '**Surgically redirected systemic and pulmonary venous pathways must remain unobstructed and separated.**',
 ['Obstruction can cause venous congestion or limit preload.', 'A leak can create shunting and desaturation depending on pressures and location.'],
 '**Use anatomy-specific imaging and hemodynamic assessment.**',
 ['Echo, CMR, CT and selected catheterization provide complementary information.', 'A baffle issue can also complicate transvenous device access.'],
 [['Baffle obstruction','Impaired venous pathway flow'],['Baffle leak','Potential abnormal mixing'],['Evaluation','ACHD imaging and selected catheterization']], [A,E], 'clinical_scenario')
q('An adult after an arterial-switch operation for d-transposition develops exertional chest discomfort. Which operation-specific issue is important to assess?',
 'Coronary ostial or proximal coronary complications after coronary reimplantation',[
 ('A systemic morphological RV as the obligatory arterial-switch anatomy','That is characteristic of an atrial switch, not the usual arterial switch.'),
 ('A Fontan pathway as the normal repair','An arterial switch is not a Fontan procedure.'),
 ('Coronary anatomy is irrelevant because the operation occurred in infancy','Reimplanted coronaries can have important late issues.')],
 'Arterial switch restores great-artery relationships and transfers the coronaries',
 '**Coronary reimplantation creates a distinct long-term surveillance concern.**',
 ['Neo-aortic root/valve disease and pulmonary arterial obstruction are other late issues.', 'Symptoms can require targeted coronary and ischemia assessment.'],
 '**Match imaging to the operation and the clinical question.**',
 ['Do not interpret the patient as if a Mustard or Senning repair had been performed.', 'Cross-sectional coronary anatomy can be important when conventional assessment is incomplete.'],
 [['Arterial switch','Coronary transfer and neo-aortic surveillance'],['Atrial switch','Baffle and systemic RV surveillance'],['New ischemic symptoms','Targeted coronary assessment']], [A,E], 'clinical_scenario')
q('What defines congenitally corrected transposition of the great arteries?',
 'Both AV and ventriculoarterial discordance',[
 ('AV concordance with ventriculoarterial discordance alone','That is the basic arrangement in d-transposition rather than double discordance.'),
 ('A single ventricle with passive pulmonary flow as the defining anatomy','That describes a different circulation.'),
 ('An isolated interatrial communication without ventricular discordance','That is not corrected transposition.')],
 'Double discordance can produce physiologically connected circulations',
 '**Systemic venous blood reaches the pulmonary artery and pulmonary venous blood reaches the aorta despite morphological discordance.**',
 ['The morphological RV commonly supports the systemic circulation.', 'Associated VSD, outflow obstruction, systemic AV valve disease and conduction block are important.'],
 '**Corrected does not mean a normal long-term heart.**',
 ['Systemic RV and tricuspid valve function need surveillance.', 'Conduction-system anatomy can predispose to AV block.'],
 [['ccTGA','AV plus ventriculoarterial discordance'],['Systemic pump','Often morphological RV'],['Late issues','Systemic RV, AV valve and conduction disease']], [A,E])
q('What is the central hemodynamic feature of a Fontan circulation?',
 'Systemic venous blood reaches the pulmonary arteries without a subpulmonary ventricle',[
 ('Two normal ventricles pump in parallel with no venous pressure cost','Fontan flow is a surgically constructed passive pulmonary pathway.'),
 ('Pulmonary flow is independent of pulmonary vascular resistance','PVR is a major determinant of forward flow.'),
 ('The circulation produces normal preload reserve at every exercise level','Limited preload augmentation contributes to exercise limitation.')],
 'Fontan flow depends on a low-resistance pulmonary pathway',
 '**Venous pressure drives blood through the lungs to fill the systemic ventricle.**',
 ['Elevated PVR, pathway obstruction or high ventricular filling pressure can reduce output.', 'Chronic systemic venous hypertension has extracardiac consequences.'],
 '**Assess the whole pathway when the circulation fails.**',
 ['Valve dysfunction, arrhythmia, lymphatic disease and ventricular dysfunction can all matter.', 'A normal systemic EF alone does not establish a healthy Fontan circulation.'],
 [['No subpulmonary pump','Passive pulmonary flow'],['PVR/pathway obstruction','Limits preload and output'],['Chronic venous pressure','Drives organ and lymphatic complications']], [A,E])
q('Why do adults with a Fontan circulation require liver surveillance?',
 'Chronic venous congestion and altered flow can cause fibrosis and other Fontan-associated liver disease',[
 ('A normal EF excludes hepatic complications','Hepatic burden can develop independently of a severely reduced systemic EF.'),
 ('Only alcohol exposure can cause liver fibrosis in these patients','Fontan hemodynamics themselves are an important cause.'),
 ('Normal transaminases reliably exclude all significant fibrosis','Routine laboratory values may not capture the full structural disease.')],
 'Fontan disease is multisystem disease',
 '**Sustained elevated venous pressure can injure the liver over time.**',
 ['Fibrosis, portal-hypertension features and focal lesions may require specialist assessment.', 'Surveillance uses an integrated clinical, laboratory and imaging approach.'],
 '**Coordinate congenital and hepatology care.**',
 ['Assess circulation quality and potentially correctable pathway problems.', 'Advanced disease can affect heart-only versus combined-organ transplant planning.'],
 [['Chronic venous congestion','Hepatic fibrosis risk'],['Normal enzymes','Do not fully exclude structural disease'],['Advanced assessment','ACHD and liver expertise']], [A,E])
q('A Fontan patient develops edema, diarrhea and severe hypoalbuminemia without nephrotic protein loss or severe hepatic synthetic failure. Which complication should be considered?',
 'Protein-losing enteropathy',[
 ('Isolated iron-deficiency anemia as the full explanation','That does not account for severe enteric protein loss and hypoalbuminemia.'),
 ('A small asymptomatic ASD as the obligatory cause','The Fontan lymphatic and hemodynamic context is more relevant.'),
 ('Physiological pregnancy-related hemodilution in every Fontan patient','That does not fit the stated clinical context.')],
 'Fontan venous and lymphatic dysfunction can cause enteric protein loss',
 '**Protein-losing enteropathy is a serious late Fontan complication.**',
 ['Assess intestinal loss and exclude renal, hepatic and nutritional alternatives.', 'Lymphatic abnormalities and adverse hemodynamics can contribute.'],
 '**Investigate the circulation rather than treating albumin as an isolated laboratory target.**',
 ['Evaluate obstruction, pressures, rhythm and ventricular or valve function.', 'Specialist lymphatic and advanced-HF options may be needed in refractory disease.'],
 [['Fontan plus hypoalbuminemia/edema','Consider enteric protein loss'],['Renal or hepatic cause','Must also be assessed'],['Management','Hemodynamic and lymphatic evaluation']], [A,E], 'clinical_scenario')
q('Why can a sustained atrial tachyarrhythmia be poorly tolerated in a Fontan patient even when the ventricular rate is not extremely high?',
 'Loss of coordinated atrial contribution and altered filling can markedly reduce an already preload-limited circulation',[
 ('Fontan output is independent of rhythm','Rhythm can have a major hemodynamic effect.'),
 ('Atrial arrhythmia proves that the pulmonary pathway has normal pressure','The rhythm does not establish normal hemodynamics.'),
 ('The systemic ventricle is irrelevant to Fontan flow','Ventricular filling and output remain essential.')],
 'A modest rhythm disturbance can destabilize a limited circulation',
 '**Fontan physiology has restricted preload reserve and depends on efficient filling.**',
 ['Atrial dilation and surgical scars create arrhythmia substrates.', 'Thromboembolic risk and the need for anticoagulation assessment are also important.'],
 '**Seek prompt ACHD and electrophysiology input.**',
 ['Assess stability and the need for rhythm restoration.', 'Review pathway obstruction and other causes of deterioration rather than treating the rate in isolation.'],
 [['Atrial rhythm loss','Can reduce filling and output'],['Surgical substrate','Promotes atrial re-entry'],['Management','Rhythm plus hemodynamic assessment']], [A,E], 'clinical_scenario')
q('A young adult has upper-limb hypertension, diminished femoral pulses and delayed femoral upstroke relative to the radial pulse. Which lesion is most likely?',
 'Aortic coarctation',[
 ('Isolated secundum ASD','ASD does not usually create this upper-lower body pressure and pulse discrepancy.'),
 ('Uncomplicated pulmonary stenosis','A pulmonary valve lesion does not obstruct systemic flow to the lower body.'),
 ('Mitral prolapse','This does not explain radiofemoral delay.')],
 'Coarctation obstructs systemic aortic flow',
 '**Upper-body pressure can be high while lower-extremity perfusion is delayed.**',
 ['Measure arm and leg pressures and assess collateral flow.', 'A bicuspid aortic valve and aortic disease can coexist.'],
 '**Use cross-sectional aortic imaging.**',
 ['CMR or CT defines location, extent, collateral vessels and associated aneurysm.', 'A low measured gradient does not always exclude important obstruction when collaterals or reduced output alter flow.'],
 [['Clinical clue','Arm hypertension and radiofemoral delay'],['Imaging','Entire thoracic aorta and associated anatomy'],['Associated disease','Bicuspid valve and aortopathy']], [A,E], 'clinical_scenario')
q('An adult had successful coarctation repair in childhood and now has hypertension despite no major recurrent obstruction. Which statement is correct?',
 'Persistent vascular dysfunction and hypertension can remain, so lifelong pressure and aortic follow-up are needed',[
 ('A successful childhood repair eliminates all future cardiovascular risk','Residual vascular and aortic risks persist.'),
 ('Every later high pressure proves the stent or repair has completely occluded','Recurrent obstruction must be assessed, but it is not the only explanation.'),
 ('A normal office reading eliminates the need for exercise or ambulatory assessment when suspicion remains','Masked or exercise-related hypertension can be relevant.')],
 'Repair corrects a narrowing but not every vascular consequence',
 '**Persistent or recurrent hypertension is common after coarctation treatment.**',
 ['Assess residual obstruction, vascular stiffness and associated aortopathy.', 'Aneurysm or repair-site problems require imaging surveillance.'],
 '**Continue lifelong ACHD care.**',
 ['Use appropriate pressure treatment and out-of-office assessment.', 'Plan CMR or CT follow-up according to anatomy and prior intervention.'],
 [['After repair','Residual hypertension can persist'],['Imaging surveillance','Detects recurrent narrowing or aneurysm'],['Risk management','Lifelong rather than discharge as cured']], [A,E], 'clinical_scenario')
q('Which anatomical feature is characteristic of Ebstein anomaly?',
 'Apical displacement of the septal tricuspid leaflet with atrialization of part of the RV',[
 ('A bicommissural aortic valve without tricuspid abnormality','That describes a different congenital valve lesion.'),
 ('Fusion of mitral commissures as the defining lesion','That is a mitral stenosis mechanism, not Ebstein anatomy.'),
 ('An isolated persistent ductal communication','PDA does not define the tricuspid displacement.')],
 'Ebstein anomaly changes both the valve and functional RV',
 '**Abnormal tricuspid leaflet attachment creates an atrialized ventricular segment.**',
 ['TR and reduced effective RV function can be important.', 'ASD-related shunting and accessory pathways are common associated concerns.'],
 '**Assess anatomy, cyanosis and rhythm together.**',
 ['Intervention planning depends on symptoms, valve severity and RV reserve.', 'A palpitations presentation may require an accessory-pathway assessment as well as valve imaging.'],
 [['Ebstein anatomy','Displaced tricuspid leaflet'],['Hemodynamic effects','TR and altered RV function'],['Electrical association','Accessory pathways and tachyarrhythmia']], [A,E])
q('An adult has symptomatic severe valvular pulmonary stenosis with a doming valve and suitable anatomy, without major dysplasia or another surgical lesion. Which intervention is generally preferred?',
 'Balloon pulmonary valvuloplasty',[
 ('Mitral commissurotomy','That treats a different valve.'),
 ('Aortic TAVI as the standard isolated pulmonary treatment','This is not the usual intervention for a native doming pulmonary valve.'),
 ('Long-term diuresis as the only corrective treatment','Diuresis cannot open the stenotic valve.')],
 'Suitable valvular pulmonary obstruction is often balloon treatable',
 '**Commissural opening can relieve obstruction in an appropriate doming pulmonary valve.**',
 ['Dysplastic valves, subvalvular or supravalvular obstruction may need a different strategy.', 'Assess RV pressure, function, symptoms and associated lesions.'],
 '**Follow for residual stenosis and pulmonary regurgitation.**',
 ['A successful pressure result can still leave a later valve follow-up need.', 'Intervention choice should be anatomy specific rather than based only on the word stenosis.'],
 [['Doming valvular PS','Often balloon suitable'],['Dysplastic or nonvalvular obstruction','May need another strategy'],['After treatment','Monitor residual obstruction and PR']], [A,E], 'clinical_scenario')
q('An athlete has exertional syncope and an anomalous coronary arising from the opposite sinus with an intramural/interarterial course. What is the appropriate interpretation?',
 'The anatomy can be high risk and warrants specialized anatomical and ischemia assessment',[
 ('All coronary anomalies are harmless incidental variants','Risk depends on origin, course and functional consequences.'),
 ('A normal resting ECG excludes exercise-related coronary compromise','Resting electrical findings may be normal.'),
 ('The interarterial course is the same as a benign retroaortic course in every case','Different courses have different implications.')],
 'The course matters as much as the anomalous origin',
 '**An intramural or interarterial segment can create dynamic ischemic risk.**',
 ['Slit-like ostial anatomy and acute takeoff can add concern.', 'Symptoms and the specific coronary involved influence intervention decisions.'],
 '**Use ACHD and coronary expertise.**',
 ['CT angiography can define the proximal anatomy.', 'Activity advice and surgery assessment require the full risk profile rather than reassurance from a single normal test.'],
 [['Interarterial/intramural course','Potential higher-risk anatomy'],['Retroaortic or other course','Different risk profile'],['Exertional syncope','Important clinical warning']], [A,E], 'clinical_scenario')
q('An adult has pulmonary venous hypertension and a membrane dividing the left atrium, with obstruction proximal to an otherwise normal mitral valve. What is the diagnosis?',
 'Cor triatriatum sinister',[
 ('Rheumatic MS','The obstruction is from an atrial membrane rather than fused mitral leaflets.'),
 ('Ebstein anomaly','That concerns the tricuspid valve and right-sided anatomy.'),
 ('A small restrictive VSD','A ventricular septal defect does not create the left atrial membrane.')],
 'A supramitral membrane can mimic MS physiology',
 '**Cor triatriatum sinister divides the left atrium into chambers connected by a variable opening.**',
 ['A restrictive opening can obstruct pulmonary venous return.', 'Severity depends on the membrane and associated anatomy.'],
 '**Define the membrane before selecting treatment.**',
 ['TOE and cross-sectional imaging help map the orifice and pulmonary veins.', 'Mitral balloon treatment would not correct an obstructing atrial membrane.'],
 [['Cor triatriatum','Obstructive LA membrane'],['MS','Mitral leaflet obstruction'],['Assessment','Membrane orifice and associated connections']], [A,E], 'clinical_scenario')

if __name__=='__main__':
    finalize('Cardiology',7,'Adult Congenital Heart Disease','cardiology-adult-congenital',rows,32)
