"""Final high-yield source gaps after the chapter-wide coverage review."""
from qbank_json_chapters import question
REFERENCES={
 'vka':('British guideline on oral anticoagulation with warfarin','https://www.gloshospitals.nhs.uk/media/documents/BCSH_Guidelines_for_Oral_Anticoagulation_with_Warfarin.pdf'),
 'aps':('EULAR antiphospholipid syndrome recommendations','https://pmc.ncbi.nlm.nih.gov/articles/PMC11034817/'),
 'epi':('FDA epinephrine clinical pharmacology review','https://www.accessdata.fda.gov/drugsatfda_docs/nda/2014/205029Orig1s000MedR.pdf'),
 'clev':('Clevidipine US prescribing information','https://www.dailymed.nlm.nih.gov/dailymed/getFile.cfm?setid=a6826aa3-fabb-4ff1-a7a3-cd4c34e3a330&type=pdf')}
rows=[]
def B(t,*c):return(t,list(c))
def Q(title,stem,answer,others,sections,ref):
 r=question('Additional pharmacological distinctions',title,stem,answer,others,sections,[ref]);r['explanationStyle']='concise_structured';rows.append(r)
Q('Warfarin Initiation for Acute VTE','A patient with acute proximal DVT is receiving therapeutic LMWH while warfarin is initiated. INR reaches 2.2 on day 3. There is no bleeding. Which transition principle applies?',
 'Continue overlap for at least 5 days and until INR is therapeutic for at least 24 hours',[
 ('Stop LMWH after the first INR above 2 regardless of treatment duration','Early INR elevation can precede adequate reduction of longer-lived factors, especially prothrombin; three days is insufficient overlap.'),
 ('Stop LMWH after 5 days regardless of INR','The duration and INR criteria must both be satisfied; a subtherapeutic INR after five days still leaves inadequate oral anticoagulation.'),
 ('Continue both drugs until the thrombus disappears on ultrasound','Imaging resolution is not the transition criterion; persistent residual thrombus does not mandate indefinite combined anticoagulation.')],
 [('Delayed Factor Depletion',[B('**Warfarin inhibits synthesis rather than neutralizing existing factors.**','An early INR response reflects shorter-lived factors and does not replace the minimum overlap period.')]),
 ('Practical Transition',[B('**Meet both time and INR requirements**, then continue the VTE-specific VKA plan.'),B('**Monitor interactions, adherence and bleeding.**','This acute VTE initiation rule is different from deciding whether perioperative bridging is needed in a stable long-term VKA user.')])],'vka')
Q('Anticoagulant Selection in Triple-Positive APS','A patient has established thrombotic antiphospholipid syndrome with persistent lupus anticoagulant, anticardiolipin and anti-β2-glycoprotein I antibodies. INR monitoring is feasible. Which oral strategy is preferred for long-term prevention?',
 'A vitamin K antagonist with an individualized INR target',[
 ('Rivaroxaban because predictable dosing removes APS-related risk','Triple-positive APS showed excess recurrent events with rivaroxaban; convenience does not establish efficacy in this high-risk thrombophilia.'),
 ('Apixaban because all Xa inhibitors are equivalent to VKAs in APS','Evidence from ordinary VTE or AF cannot establish equivalence in high-risk thrombotic APS; changing the Xa inhibitor does not resolve the concern.'),
 ('Low-dose aspirin alone after the initial anticoagulation course','Aspirin has roles in selected antibody-positive or combined-treatment settings, but alone is inadequate replacement for secondary anticoagulation in established thrombotic APS.')],
 [('Risk Profile',[B('**Triple positivity identifies a high-risk antibody pattern.**','VKA therapy is preferred; prior arterial versus venous events and recurrence influence the target and adjuncts.')]),
 ('Follow-up',[B('**Check adherence, INR quality and alternative causes if thrombosis recurs.**','Do not assume every positive antibody result is equivalent to persistent high-risk APS.'),B('**Avoid routine substitution with a DOAC merely to remove INR testing.**','Discuss feasible monitoring and individualized specialist alternatives when VKA truly cannot be used.')])],'aps')
Q('Epinephrine-Associated Lactate Rise','After epinephrine is added for shock, MAP, capillary refill and measured cardiac output improve, but lactate rises. Which interpretation is most appropriate?',
 'Adrenergic aerobic glycolysis may contribute; reassess perfusion and other causes',[
 ('The rise proves worsening tissue hypoxia and requires fluids until normalization','Lactate has multiple determinants; a drug-related metabolic contribution can coexist with improving flow, and unnecessary fluid can cause harm.'),
 ('The rise proves a harmless drug effect and removes the need for reassessment','The temporal association is not sufficient to exclude ongoing regional ischemia, impaired clearance or persistent shock.'),
 ('The rise proves inadequate oxygen saturation despite a normal arterial value','Arterial saturation alone neither explains lactate nor measures tissue oxygen utilization; this finding does not establish occult arterial hypoxemia.')],
 [('Metabolic Mechanism',[B('**Epinephrine can accelerate glycolysis despite adequate oxygen availability.**','Lactate may rise without a parallel deterioration in global perfusion.')]),
 ('Integrated Reassessment',[B('**Trend clinical perfusion, hemodynamics, organ function and dose.**','Evaluate regional ischemia, clearance and other triggers; lactate remains useful but is not a stand-alone fluid target.'),B('**Titrate vasoactive support to the patient’s response.**','Neither ignoring the rise nor reflexively escalating fluids is justified.')])],'epi')
Q('Clevidipine and the Lipid Vehicle','Which history is a labeled contraindication to IV clevidipine because of its formulation?',
 'A clinically important allergy to egg or soy products',[
 ('Stable stage 3 CKD without another contraindication','Clevidipine is metabolized by esterases; moderate renal dysfunction alone is not the lipid-emulsion allergy contraindication.'),
 ('Sinus bradycardia without high-grade AV block','The drug predominantly dilates arterioles rather than blocking the AV node; this does not identify the formulation-specific contraindication.'),
 ('Chronic hypertension treated previously with an ACE inhibitor','Prior ACE-inhibitor treatment is not a contraindication to the lipid vehicle; overall hemodynamics still guide IV treatment.')],
 [('Formulation-Specific Screening',[B('**The emulsion contains soybean oil and egg-derived phospholipids.**','Labeling also contraindicates defective lipid metabolism and severe aortic stenosis.')]),
 ('Titration and Monitoring',[B('**Start 1–2 mg/hour and titrate under continuous BP monitoring.**','Account for the lipid load and maintain aseptic handling.'),B('**Choose an alternative titratable agent when contraindicated.**','A short half-life does not negate a serious formulation risk.')])],'clev')
