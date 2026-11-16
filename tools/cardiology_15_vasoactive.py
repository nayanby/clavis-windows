"""Vasoactive pharmacology additions, with explicit current-guideline context."""
from qbank_json_chapters import question
REFERENCES={
 'ssc':('Surviving Sepsis Campaign, 2026','https://www.sccm.org/clinical-resources/guidelines/guidelines/surviving-sepsis-campaign-international-guidelines-for-management-of-sepsis-and-septic-shock-2026'),
 'mil':('Milrinone prescribing information','https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=0fdaee3c-2144-4ca7-9868-54d251f468c0'),
 'ang':('Angiotensin II prescribing information','https://giapreza-assets.s3.amazonaws.com/prescribing-information.pdf'),
 'nitro':('Sodium nitroprusside prescribing information','https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=820eadcb-1230-4b17-a652-e69b52b3c12f')}
rows=[]
def B(t,*c):return(t,list(c))
def Q(title,stem,answer,others,sections,refs,flow=None):
 r=question('Vasoactive pharmacology',title,stem,answer,others,sections,refs)
 r['explanationStyle']='concise_structured'
 if flow:r['flow']=flow
 rows.append(r)

Q('Vasopressin as an Adjunct','An adequately fluid-resuscitated adult with predominantly vasodilatory septic shock has an escalating norepinephrine requirement. There is no dominant low-output cardiac dysfunction. Under SSC 2026, which additional vasopressor is suggested at this stage?',
 'Vasopressin',[
 ('Terlipressin','Although another vasopressin-pathway drug, terlipressin is not interchangeable with vasopressin in this setting; SSC 2026 suggests against its use in septic shock.'),
 ('Dobutamine','Dobutamine targets cardiac dysfunction with persistent hypoperfusion; it can lower vascular resistance and is not the usual adjunct for isolated vasodilatory pressure failure.'),
 ('Levosimendan','This inodilator does not address the usual escalating-vasopressor pathway and may worsen hypotension; it is not recommended as a routine septic-shock adjunct.')],
 [('Different Receptor Pathway',[B('**Vasopressin adds nonadrenergic vasoconstriction.**','A common adjunctive infusion is 0.03 units/min, with ischemia and perfusion monitoring.')]),
 ('Escalation',[B('**Reassess volume responsiveness, source control and shock phenotype.**','Persistent inadequate pressure despite norepinephrine and vasopressin may justify epinephrine; a higher MAP alone does not prove restored tissue flow.')])],['ssc'],flow=['Norepinephrine requirement rises','Add vasopressin','Reassess perfusion','Consider epinephrine if pressure remains inadequate'])

Q('Milrinone During Renal Deterioration','A patient on milrinone for low-output HF develops acute kidney injury and increasing hypotension. Which pharmacological interpretation best guides reassessment?',
 'Reduced renal clearance can prolong exposure to an inodilator',[
 ('Kidney injury increases milrinone metabolism, requiring dose escalation','Renal impairment prolongs elimination rather than accelerating it; increasing the infusion may worsen hypotension and arrhythmia risk.'),
 ('Milrinone is purely a vasoconstrictor, so hypotension excludes a drug contribution','PDE3 inhibition produces both inotropy and vasodilation; hypotension is a recognized concentration-related adverse effect.'),
 ('Beta-blocker use prevents all milrinone effects until the blocker is withdrawn','Milrinone acts downstream through PDE3 inhibition rather than direct beta-receptor stimulation; beta blockade does not abolish its action.')],
 [('Mechanism and Clearance',[B('**PDE3 inhibition increases cAMP in myocardium and vessels.**','Contractility rises while vascular resistance falls; impaired renal elimination can extend exposure.')]),
 ('Immediate Review',[B('**Reassess the infusion, perfusion and rhythm**, with dose reduction or interruption as clinically required.'),B('**Correct the shock cause and select support by phenotype.**','Check preload and other vasodilators; an inotrope is not automatically beneficial when pressure or output deteriorates.')])],['mil'])

Q('Angiotensin II and Thrombosis','Angiotensin II is selected as rescue treatment for refractory distributive shock. Which accompanying safety measure is specifically emphasized in its prescribing information?',
 'Provide concurrent VTE prophylaxis unless contraindicated',[
 ('Start full-dose anticoagulation in every recipient','The warning supports prophylaxis, not universal therapeutic anticoagulation; full-dose treatment requires an appropriate indication and bleeding assessment.'),
 ('Withhold prophylaxis because the infusion is anticoagulant','Angiotensin II is a vasoconstrictor, not an anticoagulant; thromboembolic events are an important treatment concern.'),
 ('Use aspirin alone as equivalent prevention of ICU venous thrombosis','Antiplatelet therapy is not equivalent to the usual pharmacological VTE-prophylaxis strategy in this critically ill population.')],
 [('AT1-Receptor Vasoconstriction',[B('**Start at 20 ng/kg/min under the labeled protocol.**','Titrate to response; nanograms must not be confused with micrograms.')]),
 ('Monitor Beyond Pressure',[B('**Review thrombosis, limb perfusion and excessive vasoconstriction.**','Use the lowest effective rate and reassess the underlying shock; a pressure response does not establish a survival benefit or replace resuscitation.')])],['ang'])

Q('Thiocyanate Accumulation','A patient with severe renal impairment receives a prolonged nitroprusside infusion and develops tinnitus, confusion and hyperreflexia. Which accumulated metabolite is particularly implicated?',
 'Thiocyanate',[
 ('Cyanide','Cyanide toxicity more typically causes impaired cellular oxygen use and metabolic acidosis during high exposure; renal failure particularly impairs clearance of its thiocyanate metabolite.'),
 ('Methemoglobin','Methemoglobinemia impairs oxygen carriage and may cause cyanosis or a saturation gap; it does not best explain this renal-associated neurotoxic accumulation pattern.'),
 ('Nitric oxide','Nitric oxide mediates the desired rapid vasodilator effect; it is not the renally accumulating metabolite responsible for the characteristic neurological toxicity.')],
 [('Metabolic Distinction',[B('**Cyanide is converted to thiocyanate, which is renally cleared.**','Prolonged exposure with impaired renal function can produce neurotoxicity; multiple toxic effects may coexist.')]),
 ('Response',[B('**Stop nitroprusside and assess urgently.**','Review dose/duration, acid–base status and relevant levels; select an alternative BP agent and obtain toxicology/nephrology input for severe toxicity.')])],['nitro'])

Q('Inotropy Despite an Adequate MAP','An adult with septic shock has MAP 70 mmHg on norepinephrine after adequate fluid assessment, but persistent hypoperfusion with echocardiographic LV dysfunction and low output. Which SSC 2026 strategy is reasonable?',
 'Add dobutamine to norepinephrine, with response-guided reassessment',[
 ('Increase norepinephrine solely to drive MAP above 90 mmHg','Increasing afterload may not correct low output; a higher pressure target alone is not the recommended response to documented cardiac dysfunction and persistent hypoperfusion.'),
 ('Add a fixed course of levosimendan to every such patient','SSC does not support routine levosimendan for this phenotype; hypotension and lack of convincing benefit limit that strategy.'),
 ('Give repeated fluid boluses solely until lactate normalizes','Further fluid requires evidence of likely benefit; persistent lactate does not establish ongoing fluid responsiveness and indiscriminate loading can worsen congestion.')],
 [('Pressure Versus Flow',[B('**An acceptable MAP does not guarantee adequate cardiac output.**','Confirm the phenotype and exclude persistent hypovolemia or another reversible cause.')]),
 ('Trial and Reassess',[B('**Dobutamine plus norepinephrine or epinephrine alone** is suggested for persistent hypoperfusion with cardiac dysfunction.','Monitor perfusion, arrhythmia and hypotension; stop or adjust therapy when ineffective or harmful.')])],['ssc'])
