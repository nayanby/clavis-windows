"""Focused drug safety decisions for Chapter 15."""
from qbank_json_chapters import question
REFERENCES={
 'dron':('Dronedarone US prescribing information','https://products.sanofi.us/Multaq/multaq.pdf'),
 'dof':('Dofetilide US prescribing information','https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=02438044-d6a3-49e9-a1ac-3aad21ef2c8c'),
 'sot':('Sotalol US prescribing information','https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/205108s003lbl.pdf'),
 'nit':('Nitroglycerin patch prescribing information','https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=4f85d2e0-2e37-fcd1-276d-5a6466554289'),
 'nico':('MHRA nicorandil ulceration warning','https://www.gov.uk/drug-safety-update/nicorandil-risk-of-gastrointestinal-ulceration'),
 'trim':('EMA trimetazidine referral and restrictions','https://www.ema.europa.eu/en/medicines/human/referrals/trimetazidine')}
rows=[]
def B(t,*c):return(t,list(c))
def Q(title,stem,answer,others,sections,ref,style='clinical_scenario'):
 r=question('Antiarrhythmic and antianginal safety',title,stem,answer,others,sections,[ref],style=style)
 r['explanationStyle']='concise_structured';rows.append(r)

Q('Dronedarone in Permanent AF','A patient taking dronedarone for recurrent AF now has sustained AF, and patient and team decide that no further restoration of sinus rhythm will be attempted. EF is 55%. What is the best medication decision?',
 'Discontinue dronedarone and use an appropriate rate-control strategy',[
 ('Continue dronedarone because preserved EF removes the major restriction','Permanent AF is itself a contraindication; preserved EF does not remove the excess adverse cardiovascular risk in this setting.'),
 ('Increase dronedarone to improve ventricular rate control','Dose escalation does not make permanent-AF treatment appropriate; the drug is not a substitute for a suitable rate-control plan.'),
 ('Reduce dronedarone to once daily while accepting AF','A lower off-label schedule does not establish safety in permanent AF and is not the recommended response to this change in rhythm strategy.')],
 [('Rhythm Strategy Determines Eligibility',[B('**Permanent AF means that restoration is no longer pursued.**','Dronedarone is used in suitable patients in sinus rhythm with a history of paroxysmal or persistent AF; it is not continued for accepted permanent AF.')]),
 ('Safety and Follow-up',[B('**Also avoid recent decompensated symptomatic HF or NYHA IV HF under US labeling.**','The standard eligible-patient regimen is 400 mg twice daily with meals; review QT, liver function and interactions.'),B('**Stroke prevention remains risk-based**, independent of stopping the antiarrhythmic.')])],'dron')

Q('Dofetilide–Hydrochlorothiazide Interaction','Which antihypertensive is specifically contraindicated with dofetilide under US labeling because the combination increases exposure and QT prolongation?',
 'Hydrochlorothiazide',[
 ('Amlodipine','This dihydropyridine is not the labeled dofetilide interaction in the question; blood-pressure effects still require routine clinical assessment.'),
 ('Losartan','Losartan does not share the specified hydrochlorothiazide interaction; kidney function and potassium remain relevant to overall antiarrhythmic safety.'),
 ('Lisinopril','ACE inhibition is not the specific contraindicated interaction; renal deterioration or electrolyte changes still warrant review in a dofetilide-treated patient.')],
 [('Interaction Screening',[B('**Hydrochlorothiazide is contraindicated, including combination tablets.**','The interaction is more than a generic warning about diuretic-associated potassium loss.')]),
 ('Safe Initiation',[B('**Review all drugs before monitored initiation.**','Other prohibited combinations include verapamil, trimethoprim and cimetidine; use the current label for the complete list.'),B('**Dose by CrCl and QT response**, with inpatient ECG monitoring for at least three days.','Correct potassium/magnesium and reassess after renal changes; an initially acceptable QT does not remove interaction risk.')])],'dof',style='direct')

Q('Sotalol Accumulation and QT Prolongation','A patient taking sotalol develops acute kidney injury. Heart rate is 52/min, narrow-QRS QTc is 525 ms, and potassium is normal. Which action is most appropriate?',
 'Withhold further dosing and urgently reassess QT, renal dosing and rhythm',[
 ('Continue the same regimen because potassium is normal','Normal potassium does not prevent concentration-dependent torsades; renal accumulation and bradycardia materially increase risk.'),
 ('Increase the dose to prevent breakthrough ventricular arrhythmia','Additional exposure can intensify repolarization delay; prolonged QT is a toxicity warning, not an indication for escalation.'),
 ('Add a second beta blocker while retaining the sotalol dose','Further slowing may worsen pause-related proarrhythmia and does not correct excessive sotalol exposure during kidney injury.')],
 [('Mechanism of Risk',[B('**Sotalol combines beta blockade with delayed repolarization.**','Renal elimination requires an appropriate dosing interval; bradycardia and interacting QT-prolonging drugs increase risk.')]),
 ('Monitoring and Adjustment',[B('**QT ≥500 ms requires dose reduction, interval extension or discontinuation under labeling.**','In this acute deterioration, withhold and obtain monitored specialist reassessment rather than an automatic outpatient adjustment.'),B('**Recheck magnesium, potassium, creatinine and ECG.**','Reinitiation requires the appropriate monitored protocol; manage sustained ventricular arrhythmia immediately.')])],'sot')

Q('Preventing Nitrate Tolerance','A patient uses a nitroglycerin patch continuously for chronic effort angina and reports declining benefit without a new unstable symptom pattern. Which schedule best addresses pharmacological tolerance?',
 'A daily patch-on period of 12–14 hours followed by 10–12 hours off',[
 ('Replace the patch every 12 hours without any gap','Changing patches while maintaining continuous delivery does not provide the nitrate-free interval needed to limit tolerance.'),
 ('Increase patch strength while maintaining continuous exposure','Dose escalation alone often fails to overcome tolerance and increases headache or hypotension without restoring reliable benefit.'),
 ('Use the same patch for 48 hours before replacement','Extending wear does not create a controlled effective dosing schedule and does not address continuous-exposure tolerance appropriately.')],
 [('Intermittent Exposure',[B('**A nitrate-free interval restores responsiveness.**','Schedule coverage during usual exertional symptoms and plan the off-period individually.')]),
 ('Practical Care',[B('**A patch is prophylaxis, not acute rescue therapy.**','Ensure an appropriate short-acting rescue plan and reassess worsening or new rest symptoms urgently.'),B('**Monitor off-period symptoms and blood pressure.**','Other antianginal therapy may be needed; continuous exposure is not made effective merely by applying a fresh patch.')])],'nit')

Q('Nicorandil-Associated Ulceration','A patient taking nicorandil develops a persistent painful perianal ulcer. Evaluation excludes malignancy and infection, and drug causation is considered likely. Which medication strategy is most appropriate?',
 'Stop nicorandil and arrange alternative antianginal treatment',[
 ('Continue nicorandil and add acid suppression','Acid suppression may treat acid-related upper GI disease but does not remove nicorandil-associated mucosal injury, particularly at a perianal site.'),
 ('Continue nicorandil and treat with topical corticosteroids alone','Local anti-inflammatory therapy does not address the causal drug exposure; associated ulcers may persist until withdrawal.'),
 ('Halve nicorandil and continue until the ulcer closes','Dose reduction alone is not the recommended response to recognized drug-related ulceration, which can progress to serious complications.')],
 [('Recognize the Adverse Effect',[B('**Ulceration can involve oral, GI, perianal or cutaneous sites.**','It may occur after prolonged treatment and can cause fistula, perforation or bleeding.')]),
 ('Management',[B('**Withdrawal is central when the association is suspected.**','Assess the lesion and complications; review analgesics and other drugs that increase injury or bleeding risk.'),B('**Replace antianginal coverage according to heart rate, BP and ventricular function.**','Nicorandil’s potassium-channel and nitrate-like actions do not justify persisting with a serious adverse effect.')])],'nico')

Q('Trimetazidine and Movement Disorders','Which comorbidity specifically argues against using trimetazidine as an add-on for chronic angina?',
 'Parkinson disease with bradykinesia and rigidity',[
 ('Sinus bradycardia without conduction disease','Trimetazidine has little direct heart-rate effect and may be considered when further slowing is undesirable, provided other contraindications are absent.'),
 ('Low-normal blood pressure without hypoperfusion','Its limited hemodynamic effect can be useful when vasodilators are poorly tolerated; low-normal pressure is not the specific contraindication here.'),
 ('Well-controlled diabetes without renal impairment','Diabetes alone is not the motor-disorder contraindication; treatment still requires an appropriate angina indication and clinical review.')],
 [('Neurological Restriction',[B('**Trimetazidine can cause or worsen parkinsonian symptoms.**','Avoid in Parkinson disease, related movement disorders and severe renal impairment; withdraw if new motor symptoms emerge.')]),
 ('Clinical Role',[B('**Use only as an add-on for stable angina where approved.**','It does not treat an acute attack or establish a reduction in MI or mortality.'),B('**Reassess persistent neurological symptoms after withdrawal.**','A drug association does not exclude an independent neurological disorder requiring evaluation.')])],'trim',style='direct')
