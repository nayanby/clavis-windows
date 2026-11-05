"""Original 52-question Arrhythmias and Electrophysiology chapter."""
import json
from qbank_authoring import ROOT, question, ref, finalize
AF=ref('2023 ACC/AHA/ACCP/HRS Atrial Fibrillation Guideline','https://doi.org/10.1161/CIR.0000000000001193')
EAF=ref('2024 ESC Atrial Fibrillation Guideline','https://doi.org/10.1093/eurheartj/ehae176')
VA=ref('2022 ESC Ventricular Arrhythmias and Sudden Cardiac Death Guideline','https://doi.org/10.1093/eurheartj/ehac262')
SVT=ref('2019 ESC Supraventricular Tachycardia Guideline','https://doi.org/10.1093/eurheartj/ehz467')
BRADY=ref('2018 ACC/AHA/HRS Bradycardia and Cardiac Conduction Delay Guideline','https://doi.org/10.1161/CIR.0000000000000628')
ALS=ref('2025 AHA Guidelines: Adult Advanced Life Support','https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-advanced-life-support')
rows=json.loads((ROOT/'drafts/Cardiology/03. Arrhythmias and Electrophysiology/arrhythmias-draft.json').read_text(encoding='utf-8'))['questions'][:1]
def q(*args,**kwargs):rows.append(question(*args,**kwargs))

q('A patient has a regular broad-complex tachycardia at 190/min, a palpable pulse, blood pressure 65/40 mm Hg and altered consciousness. What is the immediate treatment?',
 'Synchronized electrical cardioversion',[
 ('An intravenous adenosine trial before arranging a shock','A diagnostic drug trial must not delay cardioversion in unstable tachycardia.'),
 ('A slow amiodarone infusion as the first and only immediate intervention','An infusion is not the preferred immediate response to profound instability with a pulse.'),
 ('Unsynchronized defibrillation as the routine choice for this organized rhythm','With an organized monomorphic rhythm and a pulse, synchronize if possible to avoid a vulnerable-period shock; inability to synchronize in critical deterioration changes the practical approach.')],
 'Stability determines the initial tachycardia intervention',
 '**Unstable tachycardia with a pulse generally requires prompt synchronized cardioversion.**',
 ['Hypotension, altered mental status, ischemic discomfort or acute HF can indicate instability attributable to the rhythm.', 'Sedation is appropriate when feasible but must not delay a lifesaving shock.'],
 '**Treat the hemodynamic emergency before pursuing a detailed rhythm mechanism.**',
 ['A regular broad-complex rhythm in an adult should be approached as VT when uncertain.', 'If the rhythm becomes pulseless or polymorphic such that synchronization is unreliable, use the appropriate defibrillation pathway.'],
 [['Organized unstable tachycardia with pulse','Synchronized cardioversion'],['VF or pulseless VT','Defibrillation plus CPR'],['Stable regular tachycardia','Time for targeted diagnostic and drug treatment']], [ALS,VA], 'clinical_scenario')
q('A collapsed unresponsive patient has no pulse and ventricular fibrillation on the monitor. Which action is appropriate?',
 'Immediate unsynchronized defibrillation with high-quality CPR',[
 ('Synchronized cardioversion after waiting for an R-wave marker','VF has no organized R wave for reliable synchronization.'),
 ('Adenosine followed by pulse reassessment before CPR','Adenosine does not terminate VF and must not delay defibrillation and CPR.'),
 ('Transcutaneous pacing as the first electrical treatment','Pacing is not the treatment for VF.')],
 'VF is a shockable cardiac arrest rhythm',
 '**Defibrillation interrupts disorganized ventricular activity while CPR supports perfusion.**',
 ['Minimize interruptions in compressions and deliver a shock promptly when indicated.', 'Resume CPR immediately after the shock according to the arrest algorithm rather than waiting for prolonged rhythm observation.'],
 '**Continue the full resuscitation pathway.**',
 ['Provide appropriate airway and vascular access management, medications at their indicated time and assessment of reversible causes.', 'A synchronized setting should not prevent delivery of a required unsynchronized shock in VF.'],
 [['VF/pulseless VT','Shockable arrest pathway'],['PEA/asystole','CPR and reversible-cause pathway; no shock for the nonshockable rhythm'],['Tachycardia with pulse','Assess stability and synchronization needs']], [ALS], 'clinical_scenario')
q('A patient with prior MI has a well-tolerated sustained monomorphic broad-complex tachycardia. Blood pressure is 122/76 mm Hg, QT is not prolonged, and there is no severe HF. Which intravenous drug is appropriate among these choices?',
 'Procainamide',[
 ('Verapamil','Empirical verapamil in undifferentiated broad-complex tachycardia can cause severe deterioration, especially in scar-related VT.'),
 ('Diltiazem','AV nodal blockade is not appropriate empirical treatment for likely ventricular tachycardia.'),
 ('Digoxin','Digoxin does not provide acute termination of sustained scar-related VT.')],
 'Stable monomorphic VT permits controlled treatment',
 '**Treat a broad-complex tachycardia as VT when the diagnosis is uncertain, particularly with structural heart disease.**',
 ['Procainamide can be used for selected tolerated monomorphic VT, with blood pressure and QRS monitoring.', 'Avoid it in settings such as prolonged QT or severe HF; electrical cardioversion is also a valid strategy.'],
 '**Stability allows assessment but does not make the rhythm benign.**',
 ['Correct electrolyte abnormalities, evaluate ischemia and prepare for deterioration.', 'Do not extrapolate the use of verapamil in a proven fascicular VT to an undifferentiated post-MI wide-complex rhythm.'],
 [['Tolerated monomorphic VT','Selected antiarrhythmic or cardioversion'],['Unstable VT with pulse','Urgent synchronized cardioversion'],['Uncertain wide-complex mechanism','Avoid empirical AV nodal CCB treatment']], [VA,ALS], 'clinical_scenario')
q('Which finding during a regular broad-complex tachycardia most strongly supports ventricular tachycardia?',
 'Atrial activity marching independently through the ventricular rhythm',[
 ('A ventricular rate of 160/min','Both ventricular and supraventricular tachycardias can occur at this rate.'),
 ('QRS duration of 130 ms without other information','QRS widening can result from aberrant conduction as well as VT.'),
 ('Preserved blood pressure throughout the episode','Hemodynamic tolerance does not exclude VT.')],
 'AV dissociation supports ventricular origin',
 '**Independent atrial and ventricular activation indicates that the atrium is not driving each ventricular complex.**',
 ['AV dissociation is a strong clue to VT in a broad-complex tachycardia.', 'It may be difficult to see on a standard tracing; absence of a visible dissociated P wave does not exclude VT.'],
 '**Do not use stability as a rhythm diagnosis.**',
 ['A tolerated VT can still deteriorate and requires appropriate assessment.', 'Clinical history, morphology and other features such as capture or fusion beats strengthen interpretation.'],
 [['AV dissociation','Strong support for VT'],['Broad QRS alone','Not specific'],['Normal blood pressure','Does not exclude VT']], [VA])
q('During sustained broad-complex tachycardia, an occasional near-normal QRS appears after a sinus P wave, while another beat has morphology intermediate between the normal and tachycardia complexes. What do these represent?',
 'Capture and fusion beats supporting ventricular tachycardia',[
 ('Two forms of atrial flutter conduction that prove supraventricular tachycardia','These descriptions concern ventricular capture and combined ventricular activation, not flutter-wave conduction alone.'),
 ('Electrical alternans diagnostic of tamponade','Alternating QRS amplitude in tamponade is a different phenomenon.'),
 ('A delta wave proving every broad complex is orthodromic AVRT','A delta wave is a sinus pre-excitation feature and does not explain capture and fusion during this rhythm.')],
 'Capture and fusion reveal competing ventricular activation',
 '**A capture beat occurs when a conducted supraventricular impulse activates the ventricles during VT.**',
 ['A fusion beat reflects combined activation from the VT focus and a conducted impulse.', 'These events are possible when atrial and ventricular activity are not obligatorily linked.'],
 '**They provide specific mechanistic clues in a difficult wide-complex tracing.**',
 ['A single rhythm strip may not show them; their absence is not a rule-out test.', 'Correlate morphology with the baseline ECG and clinical substrate.'],
 [['Capture beat','Near-normal conducted ventricular complex during VT'],['Fusion beat','Hybrid complex from two activation wavefronts'],['Clinical meaning','Supports ventricular origin']], [VA])
q('A stable patient has an abrupt-onset regular narrow-complex tachycardia at 180/min without pre-excitation or severe symptoms. Which initial maneuver can terminate an AV-node-dependent re-entry circuit?',
 'A modified Valsalva maneuver',[
 ('Forceful ocular pressure','Ocular pressure is not an appropriate vagal maneuver because of potential harm.'),
 ('Unsynchronized defibrillation','This is not the initial treatment for a stable organized narrow-complex tachycardia.'),
 ('A prolonged amiodarone infusion before any bedside maneuver','A simple vagal maneuver is an appropriate initial step in the stated stable rhythm.')],
 'Transiently increasing AV nodal refractoriness',
 '**Vagal maneuvers may interrupt AVNRT or orthodromic AVRT by affecting AV nodal conduction.**',
 ['A modified Valsalva with postural adjustment is an effective nonpharmacological option.', 'Continuous ECG monitoring helps document termination or reveal the underlying atrial rhythm.'],
 '**Confirm stability and rhythm regularity before following the stable SVT pathway.**',
 ['If maneuvers fail, adenosine is appropriate for suitable regular narrow-complex rhythms.', 'Atrial flutter or atrial tachycardia may persist despite transient AV block because the AV node is not essential to the atrial circuit.'],
 [['AV-node-dependent SVT','May terminate with vagal maneuver'],['Atrial flutter','AV slowing may reveal atrial activity'],['Hemodynamic instability','Electrical treatment takes priority']], [SVT], 'clinical_scenario')
q('Adenosine is most appropriate for which stable tachycardia presentation?',
 'Regular narrow-complex tachycardia likely to involve an AV-node-dependent circuit',[
 ('Irregular pre-excited broad-complex tachycardia','AV nodal blockade is contraindicated in pre-excited AF.'),
 ('Polymorphic ventricular tachycardia with no pulse','This requires the shockable arrest pathway rather than an adenosine trial.'),
 ('Sinus tachycardia caused by major hemorrhage','Treat the hemorrhage and physiological cause; transient nodal blockade does not correct compensatory sinus tachycardia.')],
 'Match adenosine to the rhythm mechanism',
 '**Adenosine briefly blocks AV nodal conduction and can terminate AVNRT or orthodromic AVRT.**',
 ['Use rapid intravenous delivery with an appropriate flush and ECG recording.', 'Warn a conscious patient about the brief flushing, chest discomfort or sense of unease that can occur.'],
 '**Its short duration does not make it safe for every tachycardia.**',
 ['Avoid in pre-excited AF and assess bronchospasm, conduction disease and relevant interactions.', 'Transient slowing without termination can be diagnostically useful but does not imply every persistent rhythm needs repeat doses.'],
 [['Regular AV-node-dependent SVT','Potential therapeutic termination'],['Flutter or atrial tachycardia','May reveal atrial activity without termination'],['Pre-excited AF','Avoid AV nodal blockade']], [SVT,AF])
q('A regular narrow-complex tachycardia at 150/min persists after adenosine, but transient AV block reveals continuous atrial activity near 300/min with sawtooth inferior-lead waves. What is the rhythm?',
 'Atrial flutter with 2:1 AV conduction',[
 ('Typical AVNRT terminated by adenosine','The atrial rhythm continues through AV block rather than terminating with disruption of an AV-node-dependent circuit.'),
 ('Sinus tachycardia with first-degree AV block','Continuous flutter activity at approximately 300/min is not a sinus P-wave pattern.'),
 ('Ventricular tachycardia with capture beats','The described organized atrial flutter and narrow 2:1 ventricular response do not fit that mechanism.')],
 'Adenosine can expose rather than terminate a rhythm',
 '**Typical flutter is a macro-reentrant atrial rhythm whose circuit does not require the AV node.**',
 ['A 2:1 ventricular response often produces a rate close to 150/min.', 'Temporary AV block reveals hidden flutter waves while the atrial circuit continues.'],
 '**Recognition changes both acute and long-term planning.**',
 ['Consider appropriate rate or rhythm control and thromboembolic assessment.', 'Do not call a persistent atrial rhythm an adenosine-resistant AVNRT solely because the initial ventricular rate was regular.'],
 [['AVNRT','AV nodal block commonly terminates the circuit'],['Flutter','AV block reveals continuing atrial waves'],['2:1 flutter','Ventricular rate often near 150/min']], [SVT], 'clinical_scenario')
q('Which mechanism most commonly accounts for typical AV nodal re-entrant tachycardia?',
 'Antegrade slow-pathway conduction with retrograde fast-pathway conduction within an AV nodal re-entry circuit',[
 ('Antegrade conduction through an accessory AV pathway and retrograde conduction through the AV node','This describes an antidromic accessory-pathway circuit rather than typical AVNRT.'),
 ('A large right atrial circuit around the tricuspid annulus','That is the substrate of typical atrial flutter.'),
 ('Re-entry through a healed ventricular infarct scar','That mechanism produces scar-related ventricular tachycardia.')],
 'Dual AV nodal physiology creates a re-entry substrate',
 '**Typical AVNRT uses a slow antegrade and fast retrograde limb.**',
 ['Different conduction and refractory properties permit a premature atrial impulse to initiate re-entry.', 'Atrial and ventricular activation may be nearly simultaneous, hiding the P wave within or just after the QRS.'],
 '**Mechanism explains the response to AV nodal interventions.**',
 ['Vagal maneuvers and adenosine can interrupt the circuit.', 'Slow-pathway modification provides definitive treatment for selected recurrent symptomatic AVNRT.'],
 [['Typical AVNRT','Slow-fast AV nodal re-entry'],['Orthodromic AVRT','AV node antegrade, accessory pathway retrograde'],['Typical flutter','Macro-re-entry around tricuspid annulus']], [SVT])
q('Which conduction sequence defines orthodromic AV re-entrant tachycardia?',
 'Antegrade conduction through the AV node-His-Purkinje system and retrograde conduction through an accessory pathway',[
 ('Antegrade accessory-pathway conduction and retrograde AV nodal conduction','That is the usual antidromic direction.'),
 ('Re-entry confined to the AV nodal region without an accessory pathway','That is AVNRT rather than AVRT.'),
 ('Atrial fibrillation conducting only through an accessory pathway','Pre-excited AF is irregular and does not define the organized orthodromic circuit.')],
 'Orthodromic AVRT usually has a narrow QRS',
 '**Ventricular activation uses the normal His-Purkinje system in the antegrade direction.**',
 ['The accessory pathway provides the retrograde return limb.', 'A narrow QRS is usual unless bundle branch aberrancy coexists.'],
 '**The same accessory pathway can participate in different clinical rhythms.**',
 ['A patient with WPW can have regular orthodromic AVRT or dangerous irregular pre-excited AF.', 'The safety of AV nodal treatment depends on the active rhythm rather than the historical label alone.'],
 [['Orthodromic AVRT','AV node down, accessory pathway up'],['Antidromic AVRT','Accessory pathway down'],['Pre-excited AF','Irregular rapid pathway conduction']], [SVT])
q('A regular broad-complex tachycardia is proven at EP study to conduct antegradely down an accessory pathway and return retrogradely through the AV node. What is the mechanism?',
 'Antidromic AV re-entrant tachycardia',[
 ('Orthodromic AV re-entrant tachycardia','Orthodromic AVRT uses the AV node-His-Purkinje system antegradely.'),
 ('Typical slow-fast AVNRT','Typical AVNRT does not require an accessory AV pathway as a circuit limb.'),
 ('Pre-excited atrial fibrillation','Pre-excited AF is an irregular atrial rhythm rather than this organized re-entry circuit.')],
 'Antidromic activation begins outside the normal ventricular conduction sequence',
 '**Antegrade accessory-pathway conduction produces pre-excited ventricular activation and a broad QRS.**',
 ['The retrograde return can occur through the AV node or, in some circuits, another pathway.', 'Surface ECG differentiation from VT may be difficult.'],
 '**Mechanistic proof is different from an empirical emergency assumption.**',
 ['In an undifferentiated broad-complex tachycardia, prioritize stability and treat as VT when uncertain.', 'Recurrent symptomatic accessory-pathway tachycardia is assessed for ablation.'],
 [['Antidromic AVRT','Broad pre-excited ventricular activation'],['Orthodromic AVRT','Usually narrow normal-system activation'],['Uncertain broad-complex tachycardia','VT-oriented safety approach']], [SVT])
q('A patient has recurrent orthodromic AVRT but no delta wave on any sinus-rhythm ECG. Which accessory-pathway property best explains this?',
 'Retrograde-only conduction through a concealed accessory pathway',[
 ('Obligatory rapid antegrade conduction at rest','Antegrade pathway activation would tend to produce ventricular pre-excitation rather than explain its absence.'),
 ('An accessory pathway must be absent if there is no delta wave','A concealed pathway can support AVRT without antegrade pre-excitation.'),
 ('Continuous antegrade AV nodal block','This would not explain recurrent orthodromic AVRT using the normal antegrade conduction limb.')],
 'A concealed pathway can still complete a re-entry circuit',
 '**Absence of a delta wave does not exclude a retrogradely conducting accessory pathway.**',
 ['The normal AV node activates the ventricle during sinus rhythm.', 'During AVRT, the concealed pathway can return the impulse from ventricle to atrium.'],
 '**Separate pathway direction from pathway existence.**',
 ['EP testing can define conduction properties and the circuit.', 'A pathway that truly lacks antegrade conduction does not create the same rapid antegrade pre-excited AF mechanism as a manifest rapidly conducting pathway.'],
 [['Manifest pathway','Antegrade conduction can create delta wave'],['Concealed pathway','Retrograde-only conduction; no delta wave'],['Clinical consequence','Can still sustain orthodromic AVRT']], [SVT])
q('Which EP finding indicates a higher-risk accessory pathway capable of rapid antegrade conduction during AF?',
 'A shortest pre-excited RR interval of 220 ms during AF',[
 ('A shortest pre-excited RR interval of 420 ms during AF','A longer interval suggests less rapid antegrade pathway conduction than the high-risk finding.'),
 ('A prolonged AV nodal Wenckebach cycle length alone','AV nodal properties do not directly measure the rapid antegrade capacity of the accessory pathway.'),
 ('Absence of palpitations as definitive proof of low risk','Symptoms alone do not reliably characterize pathway conduction risk.')],
 'Rapid antegrade pathway conduction is the key danger',
 '**A very short pre-excited RR interval during AF indicates that rapid atrial activity can reach the ventricles.**',
 ['An interval at or below about 250 ms is a recognized high-risk feature.', 'Other pathway properties and inducible rhythms contribute to the full EP risk assessment.'],
 '**Risk stratification informs discussion of ablation.**',
 ['Patient occupation, activity, preferences and pathway location also matter.', 'Ablation benefits must be weighed against procedural risks, particularly for pathways near the normal conduction system.'],
 [['Short pre-excited RR interval','Rapid antegrade conduction; higher risk'],['Retrograde-only pathway','Cannot provide antegrade pre-excitation'],['Asymptomatic status','Does not independently prove safety']], [SVT])
q('In a patient with recurrent symptomatic typical AVNRT who chooses catheter ablation, which target is generally modified?',
 'The slow AV nodal pathway region',[
 ('The compact AV node as the intended routine target','Intentional destruction of the compact AV node would create unnecessary AV block.'),
 ('The cavotricuspid isthmus','That is the standard target for typical right atrial flutter.'),
 ('The pulmonary vein antra','Pulmonary vein isolation is an AF ablation strategy, not the usual AVNRT target.')],
 'Slow-pathway modification treats typical AVNRT',
 '**Ablation aims to interrupt the re-entry substrate while preserving normal AV conduction.**',
 ['The slow-pathway region is targeted rather than deliberately destroying the compact AV node.', 'AV block is an important procedural risk to discuss, even though the intended approach is conduction preserving.'],
 '**Match the ablation site to the mechanism.**',
 ['A similar complaint of palpitations can arise from different circuits needing different targets.', 'Confirm the mechanism during EP assessment before delivering lesions.'],
 [['AVNRT','Slow-pathway modification'],['Typical flutter','Cavotricuspid isthmus ablation'],['AF','Pulmonary vein isolation-based strategy']], [SVT])
q('What is the standard ablation target for typical counterclockwise right atrial flutter?',
 'The cavotricuspid isthmus with confirmation of bidirectional block',[
 ('The AV node as the atrial flutter circuit itself','AV nodal ablation controls ventricular conduction but does not eliminate the atrial macro-re-entry circuit.'),
 ('An isolated left superior pulmonary vein in every case','Typical right atrial flutter is not a pulmonary-vein-dependent circuit.'),
 ('The slow AV nodal pathway','That target is appropriate for typical AVNRT, not the flutter macro-circuit.')],
 'Typical flutter is an anatomically defined macro-re-entry',
 '**The cavotricuspid isthmus is a critical limb of the typical flutter circuit.**',
 ['Ablation across the isthmus interrupts the circuit.', 'Bidirectional conduction block is an important procedural endpoint rather than relying only on transient termination.'],
 '**Successful flutter ablation does not eliminate future AF risk.**',
 ['Assess stroke prevention using the relevant risk and rhythm history.', 'Atypical atrial flutter can use different circuits and may require detailed mapping rather than the same empirical target.'],
 [['Typical right atrial flutter','CTI-dependent circuit'],['Atypical flutter','May require other mapped targets'],['After ablation','Reassess AF and thromboembolic risk']], [SVT,AF])
q('An older patient with severe COPD has an irregular narrow-complex tachycardia at 125/min. There are at least three distinct P-wave morphologies, variable PR intervals and an isoelectric baseline between P waves. What is the diagnosis?',
 'Multifocal atrial tachycardia',[
 ('Atrial fibrillation','AF lacks the organized discrete P waves with multiple clearly identifiable morphologies described here.'),
 ('Typical atrial flutter with fixed 2:1 conduction','That rhythm has organized flutter activity and a regular ventricular response when conduction is fixed.'),
 ('Sinus tachycardia with a single atrial focus','Sinus tachycardia generally has a consistent P-wave morphology.')],
 'MAT is an organized but multifocal atrial rhythm',
 '**Three or more P-wave morphologies with an atrial rate above 100/min support MAT.**',
 ['Variable atrial activation and AV conduction produce an irregular ventricular rhythm.', 'Pulmonary disease, hypoxemia, electrolyte disturbances and adrenergic stress are common associations.'],
 '**Treat the precipitating illness and correct reversible contributors.**',
 ['Do not assume every irregular rhythm is AF or automatically apply an AF cardioversion strategy.', 'Rate-control choices must account for lung disease, ventricular function and hemodynamics.'],
 [['MAT','Distinct multiple P morphologies and isoelectric intervals'],['AF','No consistent discrete P waves'],['Flutter','Organized repetitive atrial waves']], [SVT], 'clinical_scenario')
q('A patient with AF and rapid ventricular response has LVEF 25% and acute decompensated HF. Which intravenous rate-control drug should generally be avoided because of negative inotropy?',
 'Diltiazem',[
 ('Digoxin','Digoxin can be considered in selected decompensated HFrEF patients, although onset and toxicity considerations limit it.'),
 ('Amiodarone in a selected critically ill patient','IV amiodarone may be considered when other approaches are unsuitable, with attention to cardioversion and thromboembolic risk.'),
 ('Intravenous magnesium as an adjunct to selected rate-control treatment','Magnesium can be a useful adjunct in appropriate AF treatment; it does not share diltiazem\'s negative-inotropic contraindication.')],
 'Rate control depends on ventricular function',
 '**Non-dihydropyridine CCBs can worsen moderate or severe LV systolic dysfunction.**',
 ['Diltiazem and verapamil combine AV nodal slowing with negative inotropy.', 'Their usefulness in preserved ventricular function does not make them appropriate in decompensated HFrEF.'],
 '**Assess whether the arrhythmia is causing instability.**',
 ['If AF is responsible for shock or severe instability, urgent electrical cardioversion may be required.', 'Otherwise select rate or rhythm treatment according to pressure, congestion, anticoagulation and the clinical setting.'],
 [['Preserved LV function and stable AF','Non-DHP CCB may be an option'],['Moderate/severe systolic dysfunction','Avoid IV diltiazem/verapamil'],['Unstable AF','Urgent cardioversion assessment']], [AF,EAF], 'clinical_scenario')
q('Why may digoxin alone provide inadequate ventricular rate control during exertion in a patient with AF?',
 'Its predominantly vagotonic AV nodal effect is less effective during increased sympathetic activity',[
 ('It has no effect on AV nodal conduction at rest','Digoxin can slow AV nodal conduction, particularly in resting conditions.'),
 ('It blocks only accessory-pathway antegrade conduction','Digoxin is not an accessory-pathway protective drug and is contraindicated in pre-excited AF.'),
 ('Its therapeutic action requires exercise-induced sodium depletion','That is not the mechanism of its rate-control action.')],
 'Resting rate control may not equal activity rate control',
 '**Digoxin\'s AV nodal slowing depends in part on vagal effects.**',
 ['Sympathetic activation during exercise can overcome adequate resting control.', 'Assess symptoms and ventricular rate during relevant daily activities, not only on a resting clinic ECG.'],
 '**Choose additional treatment according to ventricular function and tolerance.**',
 ['A beta blocker or another suitable strategy may be required.', 'Kidney function, potassium and interactions constrain digoxin dosing; increasing the dose indiscriminately risks toxicity.'],
 [['Resting AF','Digoxin may provide useful slowing'],['Exertion or adrenergic stress','Control can be less reliable'],['Dose escalation','Requires toxicity assessment']], [AF,EAF])
q('Under the 2024 ESC AF guideline, a 68-year-old patient with hypertension has CHA2DS2-VA score 2. What is the recommended stroke-prevention approach if no contraindication exists?',
 'Oral anticoagulation is recommended',[
 ('Aspirin alone is an equivalent alternative','Antiplatelet treatment is not an equivalent substitute for indicated anticoagulation in AF.'),
 ('Anticoagulation is withheld unless a stroke has already occurred','Primary stroke prevention should not wait for an embolic event.'),
 ('The score is zero because sex is not included','Removing sex from CHA2DS2-VA does not remove the age 65-74 or hypertension points.')],
 'Applying the ESC CHA2DS2-VA framework',
 '**Age 65-74 contributes one point and hypertension contributes one point.**',
 ['The 2024 ESC framework recommends anticoagulation at CHA2DS2-VA at least 2 and consideration at score 1.', 'This score omits sex, whereas other guideline systems may use CHA2DS2-VASc or estimated annual risk.'],
 '**Specify the risk tool rather than mixing thresholds from different systems.**',
 ['Reassess risk as age and comorbidities change.', 'Drug choice requires checking valve status, renal function, interactions and bleeding factors.'],
 [['CHA2DS2-VA 0','Usually low risk'],['Score 1','Consider anticoagulation'],['Score at least 2','Anticoagulation recommended']], [EAF], 'clinical_scenario')
q('A patient with AF has moderate-to-severe rheumatic mitral stenosis and an indication for anticoagulation. Which oral treatment is preferred?',
 'A vitamin K antagonist such as warfarin',[
 ('Rivaroxaban as the default regardless of valve disease','The usual DOAC preference does not apply to moderate-to-severe rheumatic mitral stenosis.'),
 ('Apixaban solely because the INR is inconvenient','Monitoring convenience does not override the evidence and guideline recommendation in rheumatic stenosis.'),
 ('Aspirin plus clopidogrel instead of anticoagulation','DAPT is not equivalent embolic protection in this setting.')],
 'Rheumatic mitral stenosis changes anticoagulant selection',
 '**Warfarin is preferred over a DOAC in AF with moderate-to-severe rheumatic mitral stenosis.**',
 ['This is a specific exception to the broad DOAC preference in many other AF patients.', 'The high thromboembolic risk reflects atrial disease and stasis, not merely the usual risk score.'],
 '**Confirm valve severity and plan reliable anticoagulation follow-up.**',
 ['Review INR control, adherence, interactions and bleeding risk.', 'Do not use a generic nonvalvular-AF label without checking the actual valve lesion.'],
 [['AF without rheumatic MS or mechanical valve','DOAC often preferred when suitable'],['Moderate/severe rheumatic MS with AF','Vitamin K antagonist preferred']], [AF,EAF], 'clinical_scenario')
q('Which anticoagulant principle applies to a patient with a mechanical prosthetic valve and AF?',
 'Use a vitamin K antagonist with a valve-specific INR target',[
 ('Use dabigatran because it avoids INR testing','DOACs are not appropriate substitutes for warfarin in mechanical valves.'),
 ('Use a reduced-dose factor Xa inhibitor whenever bleeding risk is high','An unvalidated DOAC dose does not provide an evidence-based mechanical-valve regimen.'),
 ('Use antiplatelet monotherapy because AF is not continuous','The mechanical valve itself creates an anticoagulation indication irrespective of AF burden.')],
 'Mechanical valves require a distinct anticoagulation pathway',
 '**Vitamin K antagonist treatment remains standard for mechanical prosthetic valves.**',
 ['The INR target depends on valve type, position and risk factors.', 'The presence or absence of AF episodes does not remove the valve-related indication.'],
 '**Do not generalize the convenience of DOACs to excluded valve populations.**',
 ['Coordinate interruption and bridging decisions with the valve-specific risk assessment.', 'Assess bleeding causes while preserving effective valve thrombosis prevention.'],
 [['Mechanical prosthesis','VKA with appropriate target'],['Bioprosthesis or valve repair','Different, context-dependent pathway'],['AF alone','Risk-based anticoagulant assessment']], [AF,EAF])
q('An older patient with AF is prescribed a DOAC. Which principle best reduces preventable stroke from inappropriate underdosing?',
 'Use the labeled dose and reduce it only when the agent-specific renal, age, weight or interaction criteria are met',[
 ('Halve every DOAC dose once a patient reaches 70 years','Dose-reduction rules are not identical across agents and do not follow this universal age cutoff.'),
 ('Reduce all doses whenever HAS-BLED is elevated','A bleeding score is not a validated replacement for the labeled dose criteria.'),
 ('Choose a dose from eGFR alone without checking the product\'s renal method','Many DOAC dosing criteria rely on creatinine clearance calculated using the specified approach; the full label must be applied.')],
 'Correct dosing is part of effective stroke prevention',
 '**Unjustified dose reduction can compromise protection without delivering the assumed safety benefit.**',
 ['Check the actual DOAC, renal function calculation, weight, age and interacting drugs.', 'Reassess dosing as kidney function and medication exposure change.'],
 '**A high bleeding risk should prompt risk-factor correction, not automatic off-label dosing.**',
 ['Control blood pressure, avoid unnecessary antiplatelets or NSAIDs and investigate bleeding sources.', 'Use an alternative appropriate regimen if the labeled drug is unsuitable rather than inventing a dose.'],
 [['Meets labeled reduction criteria','Use the specified reduced dose'],['Does not meet reduction criteria','Use the appropriate standard dose'],['Changing kidney function','Repeat dose assessment']], [AF,EAF], 'clinical_scenario')
q('A patient has AF with a clear anticoagulation indication and an elevated bleeding-risk score. There is no active major bleeding. How should the score be used?',
 'Identify modifiable bleeding factors and the need for closer follow-up rather than automatically deny anticoagulation',[
 ('Treat the score as an absolute contraindication to all anticoagulants','A bleeding score alone should not negate a strong stroke-prevention indication.'),
 ('Substitute aspirin because it has no bleeding risk','Aspirin also causes bleeding and is less effective than anticoagulation for indicated AF stroke prevention.'),
 ('Ignore the score and continue unnecessary NSAIDs and antiplatelets','Modifiable contributors should be addressed to improve treatment safety.')],
 'Bleeding assessment should improve treatment safety',
 '**Stroke and bleeding risks often share factors, so a high score can identify patients who still have substantial anticoagulation benefit.**',
 ['Review pressure control, renal and liver function, prior bleeding, alcohol and interacting medication.', 'Correct avoidable factors and arrange appropriate monitoring.'],
 '**Separate a risk marker from an active contraindication.**',
 ['Ongoing major bleeding or another specific contraindication requires individualized management.', 'Shared decisions should describe the expected stroke benefit and bleeding risk in the actual patient.'],
 [['Elevated score without active contraindication','Modify risks and monitor'],['Active major bleeding','Urgent individualized management'],['Unnecessary antiplatelet or NSAID','Review and discontinue when appropriate']], [AF,EAF])

# Remaining items cover cardioversion, rhythm drugs, inherited syndromes and bradycardia.
q('A stable patient has AF of definite 36-hour duration and has not received anticoagulation. Under the 2024 ESC approach, what is appropriate before elective cardioversion?',
 'Provide at least three weeks of therapeutic anticoagulation or use a TOE-guided strategy to exclude intracardiac thrombus',[
 ('Cardiovert without anticoagulation assessment because duration is below 48 hours','The 2024 ESC safety threshold is more conservative: AF longer than 24 hours requires the stated precautions.'),
 ('Use aspirin for one day as equivalent preparation','Antiplatelet therapy is not equivalent to therapeutic anticoagulation for this purpose.'),
 ('Use a normal transthoracic echo as sufficient exclusion of left atrial appendage thrombus','A routine transthoracic study does not reliably exclude appendage thrombus.')],
 'Specify the guideline when applying a cardioversion time threshold',
 '**The 2024 ESC guideline uses an AF duration greater than 24 hours for this elective-cardioversion safety precaution.**',
 ['At least three weeks of therapeutic anticoagulation is one pathway.', 'TOE can support an earlier strategy when thrombus is excluded and appropriate anticoagulation is established.'],
 '**Stable elective treatment differs from emergency cardioversion for instability.**',
 ['Do not delay lifesaving cardioversion in an unstable patient while waiting weeks for anticoagulation.', 'Post-cardioversion anticoagulation and long-term stroke prevention remain separate decisions after the preparation step.'],
 [['Stable AF longer than 24 hours under ESC 2024','Anticoagulation or TOE-guided preparation'],['Hemodynamic instability due to AF','Urgent cardioversion'],['After cardioversion','Continue appropriate anticoagulation']], [EAF], 'clinical_scenario')
q('TOE before planned AF cardioversion shows a left atrial appendage thrombus. What is the appropriate strategy?',
 'Defer elective cardioversion, establish or optimize therapeutic anticoagulation and repeat assessment after an appropriate treatment interval',[
 ('Proceed because the shock will dissolve the thrombus','Electrical cardioversion does not dissolve thrombus and may expose the patient to embolic risk.'),
 ('Use pharmacological cardioversion because it avoids the same embolic concern','Restoring rhythm pharmacologically also carries embolic considerations.'),
 ('Add aspirin and cardiovert later the same day','Aspirin does not provide adequate treatment of an established appendage thrombus before elective cardioversion.')],
 'Visible appendage thrombus changes the elective rhythm plan',
 '**An established intracardiac thrombus is a reason to defer elective cardioversion.**',
 ['Investigate adherence, anticoagulant dose, interactions and other reasons for thrombus despite treatment.', 'Repeat imaging after an appropriate period of effective anticoagulation assesses resolution.'],
 '**Do not substitute one cardioversion method for another to bypass the risk.**',
 ['Both electrical and pharmacological rhythm restoration require thromboembolic safety planning.', 'Anticoagulant choice depends on valve status, renal function and the individual context.'],
 [['No thrombus with appropriate preparation','Proceed according to a safe pathway'],['Appendage thrombus present','Defer elective cardioversion and treat'],['Persistent thrombus','Reassess treatment and repeat specialist evaluation']], [AF,EAF], 'clinical_scenario')
q('A patient with AF of two weeks\' duration undergoes successful TOE-guided electrical cardioversion after thrombus is excluded and anticoagulation is started. Which statement about the following four weeks is correct?',
 'Continue therapeutic anticoagulation for at least four weeks, with longer treatment determined by ongoing stroke risk',[
 ('Stop anticoagulation the next day because sinus rhythm is documented','Atrial mechanical recovery and thromboembolic risk do not normalize immediately after electrical rhythm restoration.'),
 ('TOE exclusion of thrombus removes the need for all post-cardioversion anticoagulation','A negative preprocedure TOE does not eliminate subsequent risk from atrial stunning or new thrombus.'),
 ('Replace anticoagulation with aspirin for four weeks','Aspirin is not equivalent post-cardioversion protection.')],
 'Atrial electrical and mechanical recovery are not simultaneous',
 '**Post-cardioversion anticoagulation covers a period of persisting thromboembolic vulnerability.**',
 ['The usual minimum is four weeks in this prolonged-AF presentation.', 'TOE addresses existing thrombus at one point in time; it does not prevent thrombus forming during subsequent atrial dysfunction.'],
 '**Long-term treatment follows risk rather than apparent procedural success.**',
 ['Reassess the indication beyond four weeks using the appropriate stroke-risk framework.', 'A negative monitor or absence of palpitations alone does not prove that future AF or embolic risk is absent.'],
 [['Preprocedure TOE','Assesses existing thrombus'],['First four weeks after prolonged-AF cardioversion','Continue therapeutic anticoagulation'],['Beyond this period','Use ongoing thromboembolic risk']], [AF,EAF], 'clinical_scenario')
q('A patient with a continuing risk-based anticoagulation indication has apparently successful AF ablation and no symptomatic recurrence. What is the appropriate long-term principle?',
 'Base continued anticoagulation on thromboembolic risk rather than apparent ablation success alone',[
 ('Stop all anticoagulation immediately after ablation','Ablation itself requires a protected postprocedural period, and longer treatment may remain indicated.'),
 ('Use symptom absence as a reliable exclusion of all AF','Recurrences can be silent, and stroke risk is not determined solely by reported symptoms.'),
 ('Switch every patient to aspirin once the access site heals','Aspirin is not an equivalent substitute for indicated AF anticoagulation.')],
 'Rhythm control and stroke prevention are complementary',
 '**Successful rhythm treatment does not automatically erase a stroke-prevention indication.**',
 ['Clinical risk factors may persist even when AF burden falls.', 'Silent recurrence and atrial disease complicate reliance on symptoms alone.'],
 '**Reassess treatment using the applicable guideline and the individual risk profile.**',
 ['Keep the immediate post-ablation anticoagulation requirement distinct from the long-term decision.', 'Discuss bleeding risks and alternatives when a genuine contraindication arises rather than using procedural success as the sole reason to stop.'],
 [['Ablation goal','Reduce AF burden and symptoms'],['Anticoagulation goal','Prevent thromboembolism'],['Long-term decision','Guided by risk and clinical context']], [AF,EAF])
q('Which finding from EAST-AFNET 4 is most relevant to a patient with recently diagnosed AF and cardiovascular risk factors?',
 'An early rhythm-control strategy reduced a composite of cardiovascular death, stroke and hospitalization for HF or ACS compared with usual care',[
 ('Benefit was demonstrated only when every participant underwent immediate ablation','Most early rhythm-control treatment initially used antiarrhythmic drugs rather than mandatory immediate ablation.'),
 ('Early rhythm control eliminated the need for anticoagulation','Stroke prevention remained part of appropriate care.'),
 ('The trial proved that symptom control is the only possible benefit of rhythm treatment','The trial addressed important cardiovascular outcomes in a selected early-AF population.')],
 'Timing can matter in a rhythm-control strategy',
 '**Early rhythm control is more than rescuing symptoms after years of persistent AF.**',
 ['The trial enrolled patients with AF diagnosed within one year and relevant cardiovascular conditions or risk.', 'The intervention was a strategy using drugs, cardioversion and selected ablation, not a single mandatory procedure.'],
 '**Apply the evidence to the studied clinical context.**',
 ['Balance expected benefit with drug toxicity, procedural risk and preferences.', 'Continue anticoagulation and comorbidity treatment when indicated.'],
 [['Early rhythm-control strategy','Selected cardiovascular outcome benefit'],['Specific treatment method','Individualized; not ablation in every patient'],['Stroke prevention','Continues according to risk']], [ref('EAST-AFNET 4: Early Rhythm-Control Therapy in Patients with Atrial Fibrillation','https://doi.org/10.1056/NEJMoa2019422'),EAF])
q('A patient with prior MI and ventricular scar asks for flecainide to prevent recurrent AF. What is the appropriate response?',
 'Avoid flecainide because previous MI or significant ventricular scar creates a proarrhythmic risk',[
 ('Prescribe it because class Ic drugs are preferred after infarction','Class Ic sodium-channel blockade is unsuitable in this scar-related substrate.'),
 ('Use it safely if aspirin is added','Aspirin does not neutralize ventricular proarrhythmia.'),
 ('Use it without checking EF because only the atria are affected','Flecainide affects ventricular conduction and requires structural and functional assessment.')],
 'Structural substrate determines class Ic safety',
 '**Flecainide is an option only in appropriately selected patients without prior MI or significant structural scar.**',
 ['Sodium-channel blockade slows conduction and can promote re-entry in diseased ventricular tissue.', 'The concern is not removed by a currently stable coronary symptom pattern.'],
 '**Select rhythm treatment around the patient\'s substrate.**',
 ['Assess ventricular function, ischemic history, conduction disease and drug interactions.', 'Consider another suitable antiarrhythmic or ablation strategy according to the full clinical context.'],
 [['No significant structural disease','Class Ic may be suitable'],['Prior MI or ventricular scar','Avoid flecainide/propafenone'],['Alternative strategy','Individualize drug or ablation choice']], [AF,EAF], 'clinical_scenario')
q('Why is an AV nodal blocking drug often co-prescribed with flecainide for AF in an otherwise suitable patient?',
 'To reduce the risk of rapid 1:1 AV conduction if AF organizes into atrial flutter',[
 ('To prevent all flecainide-related QRS widening','AV nodal blockade does not eliminate sodium-channel-mediated ventricular conduction slowing.'),
 ('To make flecainide safe after a large ventricular infarction','The structural-heart-disease restriction remains.'),
 ('To provide stroke prevention equivalent to an anticoagulant','Rate-slowing medication does not replace indicated anticoagulation.')],
 'Class Ic treatment can alter the atrial rhythm without safely limiting ventricular conduction',
 '**Flecainide can organize AF into a slower atrial flutter that conducts rapidly through the AV node.**',
 ['A suitable AV nodal blocker reduces the risk of dangerous 1:1 ventricular conduction.', 'Drug choice must account for blood pressure, heart rate and ventricular function.'],
 '**The combination does not bypass other contraindications.**',
 ['Check the absence of significant MI-related or structural ventricular disease.', 'A pill-in-the-pocket approach should first be evaluated in a monitored setting in a suitable patient.'],
 [['Class Ic alone','Possible organized flutter with rapid conduction'],['Appropriate AV nodal co-treatment','Reduces 1:1 conduction risk'],['Stroke prevention','Remains a separate risk-based decision']], [AF])
q('What is required when initiating dofetilide for AF under its standard monitored initiation protocol?',
 'Inpatient ECG monitoring with QT and creatinine-clearance-based dosing for at least three days',[
 ('An outpatient first dose without renal assessment because the drug is purely atrial','Dofetilide can cause ventricular torsades, and renal function affects exposure.'),
 ('A fixed maximal dose regardless of QT or kidney function','Dose selection and continuation depend on renal clearance and QT response.'),
 ('Routine co-prescription of another QT-prolonging antiarrhythmic','Additive repolarization effects can increase torsades risk.')],
 'Dofetilide initiation is a safety protocol',
 '**IKr blockade can prolong QT and trigger torsades de pointes.**',
 ['Renal clearance determines exposure and dose selection.', 'Check baseline QT, potassium, magnesium and contraindicated interactions, with continuous monitoring and repeat ECGs during loading.'],
 '**The monitored period addresses early proarrhythmic risk.**',
 ['The standard protocol requires at least three days and appropriate observation after conversion when relevant.', 'Ongoing follow-up still includes renal function, electrolytes and QT assessment.'],
 [['QT prolongation','Signals repolarization-related risk'],['Reduced creatinine clearance','Requires labeled dose adjustment or exclusion'],['Initiation/reinitiation','Monitored inpatient protocol']], [AF,ref('Tikosyn prescribing information: initiation and renal/QT dosing','https://labeling.pfizer.com/showlabeling.aspx?id=639')])
q('Which patient should not receive dronedarone for AF rhythm maintenance?',
 'A patient hospitalized for decompensated HFrEF two weeks earlier with persistent NYHA III symptoms',[
 ('A stable patient with paroxysmal AF and preserved ventricular function after full suitability assessment','Dronedarone can be an option in selected patients without recent decompensation or severe LV dysfunction.'),
 ('A patient without structural disease who has undergone evaluation for drug interactions','Absence of structural disease is not itself a contraindication.'),
 ('A stable patient in sinus rhythm whose AF rhythm-control indication remains appropriate','The stated feature is not the high-risk contraindication tested here.')],
 'Dronedarone safety depends on HF and rhythm context',
 '**Recent decompensated HF or advanced symptomatic HF creates an important harm signal.**',
 ['The ACC/AHA guideline advises against dronedarone in NYHA III-IV HF or decompensation within the previous four weeks.', 'Permanent AF is another important context in which the drug is unsuitable.'],
 '**Do not extrapolate its use in selected stable AF patients to an unstable HF population.**',
 ['Assess the current rhythm, EF, recent admissions and interactions.', 'Choose another rhythm-control or ablation strategy when appropriate.'],
 [['Selected stable paroxysmal/persistent AF','May be considered after suitability review'],['Recent decompensated or advanced HF','Do not use'],['Permanent AF','Unsuitable rhythm context']], [AF], 'clinical_scenario')
q('A patient taking a QT-prolonging drug develops recurrent self-terminating polymorphic VT with a twisting QRS axis, QTc 560 ms and potassium 3.0 mmol/L. The patient currently has a pulse and is between episodes. Which treatment is appropriate immediately?',
 'Intravenous magnesium, withdrawal of the culprit drug and potassium correction',[
 ('Additional sotalol to suppress the episodes','Sotalol prolongs repolarization and can worsen torsades.'),
 ('A class Ic drug without electrolyte correction','This does not address the acquired long-QT mechanism or the reversible electrolyte trigger.'),
 ('Verapamil as treatment for all polymorphic VT','This is not the treatment of acquired long-QT torsades.')],
 'Treat the substrate for acquired torsades',
 '**Long QT, hypokalemia and a QT-prolonging drug strongly support torsades de pointes.**',
 ['Give magnesium even when the measured serum magnesium is not low.', 'Remove offending medication and correct potassium and other reversible contributors.'],
 '**Electrical treatment depends on the immediate rhythm and perfusion.**',
 ['Sustained unstable polymorphic VT or a pulseless episode requires prompt unsynchronized shock.', 'Recurrent pause-dependent episodes may require increasing the heart rate with pacing or a selected strategy after specialist assessment.'],
 [['Acquired long-QT torsades','Magnesium and correction of causes'],['Unstable sustained polymorphic VT','Immediate defibrillation'],['Recurrent pause dependence','Consider rate acceleration']], [VA,ALS], 'clinical_scenario')
q('After withdrawal of a culprit drug and electrolyte correction, a patient continues to have acquired pause-dependent torsades initiated after long bradycardic pauses. Which intervention can suppress the pause trigger?',
 'Temporary overdrive pacing',[
 ('Further slowing the sinus rate with a beta blocker as the immediate universal strategy','Additional bradycardia can worsen this acquired pause-dependent mechanism; congenital long-QT beta-blocker treatment is a different setting.'),
 ('Giving another QT-prolonging class III drug','This may worsen the repolarization abnormality.'),
 ('Waiting for the QT to normalize despite recurrent unstable episodes','Persistent dangerous recurrence requires active treatment and monitoring.')],
 'Avoid long pauses in acquired torsades',
 '**Increasing heart rate can reduce pause-dependent initiation when magnesium and cause correction are insufficient.**',
 ['Temporary pacing provides a controlled way to prevent long cycles.', 'Isoproterenol can have a selected role in acquired bradycardia-related torsades but is not a general treatment for congenital LQTS or ischemia.'],
 '**Identify the mechanism before choosing a chronotropic intervention.**',
 ['Review AV block, sinus-node suppression and interacting medication.', 'Continue monitoring and correction while the drug effect and QT abnormality resolve.'],
 [['Acquired pause-dependent torsades','Prevent long pauses'],['Congenital LQTS','Different long-term preventive strategy'],['Ischemic polymorphic VT without long QT','Evaluate ischemia and a different mechanism']], [VA,ALS], 'clinical_scenario')
q('A teenager with a prolonged QT interval has syncope while swimming. Which genotype-trigger association is most characteristic?',
 'LQT1 associated with KCNQ1 and exercise-related events',[
 ('LQT2 associated with KCNH2 and auditory startle','This is a genuine association, but swimming and exertion more strongly suggest LQT1.'),
 ('LQT3 associated with SCN5A and rest or sleep events','This association is more characteristic of events at low heart rates or during sleep.'),
 ('Brugada syndrome associated with a type 1 right-precordial pattern','Brugada is a different electrical syndrome and does not explain the characteristic prolonged-QT exercise association.')],
 'Triggers can suggest an LQTS subtype',
 '**Exercise, especially swimming, is a characteristic trigger in LQT1.**',
 ['KCNQ1 abnormalities affect the slow delayed rectifier potassium current.', 'Trigger associations guide suspicion but do not replace a full phenotype, family history and genetic interpretation.'],
 '**Reduce arrhythmic risk with syndrome-specific specialist care.**',
 ['Nonselective beta blockers such as nadolol or propranolol are important preventive therapies in appropriate congenital LQTS.', 'Avoid QT-prolonging drugs, correct electrolytes and individualize activity advice and family assessment.'],
 [['LQT1/KCNQ1','Exercise and swimming'],['LQT2/KCNH2','Auditory startle or emotion'],['LQT3/SCN5A','Rest or sleep association']], [VA], 'clinical_scenario')
q('Which congenital long-QT association is most characteristic of syncope triggered by a sudden alarm?',
 'LQT2 with KCNH2-related repolarization abnormality',[
 ('LQT1 with KCNQ1 as the strongest auditory-startle association','LQT1 is more characteristically exercise related, particularly swimming.'),
 ('LQT3 with SCN5A as the typical alarm-trigger phenotype','LQT3 events are more associated with rest or sleep.'),
 ('CPVT with a normal QT as a definition of LQT2','CPVT is a different syndrome and does not define an LQTS subtype.')],
 'Auditory startle is a useful LQT2 clue',
 '**KCNH2-related LQT2 affects the rapid delayed rectifier potassium current.**',
 ['Abrupt auditory stimuli and emotion are recognized event associations.', 'T-wave morphology, repeated QT assessment and the family phenotype can provide additional clues.'],
 '**Associations are probabilistic rather than absolute diagnostic rules.**',
 ['Do not assign a pathogenic genotype solely from one trigger.', 'Provide appropriate preventive treatment, drug avoidance and family evaluation based on the complete assessment.'],
 [['LQT2','KCNH2; auditory startle association'],['LQT1','KCNQ1; exercise association'],['LQT3','SCN5A; rest/sleep association']], [VA])
q('Which molecular mechanism is characteristic of classic LQT3?',
 'Gain of persistent late inward sodium current due to selected SCN5A variants',[
 ('Loss of IKs from KCNQ1 variants','This mechanism is characteristic of LQT1.'),
 ('Loss of IKr from KCNH2 variants','This mechanism is characteristic of LQT2.'),
 ('Catecholamine-induced calcium leak with a normal resting QT as the defining mechanism','That describes the usual CPVT framework rather than classic LQT3.')],
 'The same ion-channel gene can have different clinical phenotypes',
 '**LQT3 often results from increased late sodium current that prolongs repolarization.**',
 ['Events may occur at rest or during sleep.', 'Other SCN5A variants can cause different phenotypes, including Brugada syndrome or conduction disease; the gene name alone does not define the effect.'],
 '**Use variant and phenotype interpretation to guide specialist treatment.**',
 ['Selected genotype-directed therapies require demonstrated suitability, not indiscriminate use of a sodium-channel blocker.', 'QT, symptoms, family history and response to treatment contribute to risk assessment.'],
 [['SCN5A gain of late sodium current','Classic LQT3 mechanism'],['KCNQ1 loss of IKs','LQT1'],['KCNH2 loss of IKr','LQT2']], [VA])
q('A febrile young man with unexplained syncope has coved ST elevation of at least 2 mm followed by negative T waves in V1-V2 placed in high right-precordial positions. Which diagnosis should be considered?',
 'Brugada syndrome with a type 1 ECG pattern',[
 ('Typical acute pericarditis solely from these two leads','Pericarditis usually has a different distributed ECG and clinical pattern; a coved right-precordial type 1 pattern suggests Brugada evaluation.'),
 ('LQT1 established by a delta wave','LQT1 is a repolarization syndrome; a delta wave is a pre-excitation feature and is not described here.'),
 ('Typical CTI-dependent atrial flutter','Flutter is an atrial rhythm with repetitive atrial waves, not this ventricular repolarization pattern.')],
 'Recognize a type 1 Brugada pattern',
 '**Coved right-precordial ST elevation with T-wave inversion is the characteristic type 1 pattern.**',
 ['Fever can unmask the phenotype and increase arrhythmic risk.', 'Exclude mimics and integrate symptoms, family history and specialist assessment before final syndrome classification.'],
 '**Treat fever and avoid provoking drugs.**',
 ['Arrhythmic syncope, documented VT/VF and spontaneous type 1 pattern influence risk assessment.', 'A saddleback pattern alone has a different diagnostic status and should not be automatically equated with a definite type 1 phenotype.'],
 [['Type 1 pattern','Coved ST elevation with negative T wave'],['Fever','Potential unmasking and triggering factor'],['Prior VF or likely arrhythmic syncope','Important risk information']], [VA], 'clinical_scenario')
q('A patient with Brugada syndrome survives a documented VF arrest without a reversible explanation. Which strategy provides the principal secondary-prevention protection?',
 'An implantable cardioverter-defibrillator',[
 ('Fever advice alone with no arrhythmia protection discussion','Trigger avoidance is important but insufficient as the sole response to a survived VF arrest.'),
 ('Routine class Ic treatment to normalize the ECG','Sodium-channel blockers can provoke the phenotype and are not routine chronic protective treatment.'),
 ('A standard pacemaker as equivalent VF protection','A standard pacemaker does not terminate VF.')],
 'A survived VF arrest establishes a high-risk Brugada phenotype',
 '**An ICD is the central secondary-prevention strategy when appropriate after VF.**',
 ['A shock-terminating device addresses recurrence of a potentially fatal ventricular arrhythmia.', 'Quinidine and specialist ablation have selected roles in recurrent events or special circumstances, not an automatic equivalence to ICD protection.'],
 '**Continue trigger management and family assessment.**',
 ['Treat fever promptly and review drugs to avoid.', 'Discuss device complications and follow-up, and evaluate relatives according to the inherited-disease pathway.'],
 [['Survived VF','Secondary-prevention ICD assessment'],['Fever or provoking medication','Avoid and treat triggers'],['Recurrent shocks/electrical storm','Specialist adjunctive treatment']], [VA], 'clinical_scenario')
q('A child has exertional syncope, a structurally normal heart and a normal resting QT. Exercise testing provokes alternating-axis bidirectional VT. Which diagnosis is most likely?',
 'Catecholaminergic polymorphic ventricular tachycardia',[
 ('LQT3','A normal resting QT and catecholamine-triggered bidirectional VT are more characteristic of CPVT than LQT3.'),
 ('Typical idiopathic AVNRT','AVNRT is an AV nodal supraventricular circuit and does not produce this exercise-induced ventricular pattern.'),
 ('Typical atrial flutter with aberrancy','The characteristic bidirectional VT response in this setting supports an inherited ventricular calcium-handling disorder.')],
 'A normal resting ECG does not exclude an inherited lethal arrhythmia',
 '**CPVT is characterized by adrenergically triggered ventricular arrhythmias in an otherwise often normal heart.**',
 ['Bidirectional or polymorphic VT may appear during exercise or emotional stress.', 'Abnormal intracellular calcium handling, commonly involving RYR2, underlies many cases.'],
 '**Use specialist prevention rather than reassurance from a normal resting QT.**',
 ['Nonselective beta blockade is central; activity counseling and family assessment are important.', 'Flecainide can be added when arrhythmias persist despite adequate beta blockade.'],
 [['CPVT','Exercise/emotion-triggered bidirectional or polymorphic VT'],['Resting ECG','May be normal'],['Initial prevention','Nonselective beta blocker and trigger management']], [VA], 'clinical_scenario')
q('A CPVT patient remains exercise-test positive for ventricular arrhythmia despite adherence to maximally tolerated nadolol. Which additional drug has evidence for reducing arrhythmic burden?',
 'Flecainide',[
 ('Digoxin','Digoxin is not a preventive CPVT treatment and can itself produce calcium-related arrhythmias in toxicity.'),
 ('Isoproterenol as chronic prophylaxis','Adrenergic stimulation can provoke CPVT rather than prevent it.'),
 ('A long-acting nitrate as the mechanism-specific antiarrhythmic','Nitrates do not address the inherited calcium-triggered ventricular arrhythmia mechanism.')],
 'Persistent CPVT can require combination prevention',
 '**Flecainide is an evidence-supported add-on when adequate beta blockade does not control CPVT.**',
 ['This is a syndrome-specific use and does not negate class Ic restrictions in ischemic ventricular scar.', 'Assess adherence, dose tolerance and exercise response before declaring treatment failure.'],
 '**Continue comprehensive inherited-arrhythmia care.**',
 ['Specialist escalation may include left cardiac sympathetic denervation or selected device decisions.', 'ICD-related adrenergic shocks can complicate CPVT management, so prevention of arrhythmia remains important even when a device is used.'],
 [['First-line prevention','Nonselective beta blockade'],['Residual exercise-induced arrhythmia','Consider flecainide add-on'],['Persistent high-risk disease','Specialist escalation']], [VA], 'clinical_scenario')
q('In arrhythmogenic right ventricular cardiomyopathy, a VT arising from the RV commonly has which QRS morphology?',
 'Left bundle branch block morphology',[
 ('Right bundle branch block morphology as an obligatory RV-origin feature','An RV-origin ventricular wavefront commonly gives an LBBB pattern; RBBB morphology more often suggests LV origin.'),
 ('A narrow QRS identical to normal sinus conduction in every episode','Ventricular origin generally alters activation and does not obligately preserve a normal narrow QRS.'),
 ('A delta wave as the defining criterion for ARVC','Delta waves reflect accessory-pathway pre-excitation, not an ARVC criterion.')],
 'VT morphology provides a clue to ventricular origin',
 '**Activation beginning in the RV often spreads toward the LV and produces an LBBB-like pattern.**',
 ['The frontal axis adds localization information; a superior axis can be a concerning pattern in the appropriate ARVC context.', 'LBBB morphology alone is not diagnostic of ARVC because idiopathic RV outflow tract VT can look similar.'],
 '**Use a complete cardiomyopathy assessment.**',
 ['CMR, ventricular structure and function, ECG abnormalities, family history and genetics contribute.', 'Avoid diagnosing ARVC solely from one VT morphology or an isolated borderline imaging finding.'],
 [['RV-origin VT','Often LBBB morphology'],['LV-origin VT','Often RBBB morphology'],['ARVC diagnosis','Requires integrated structural, electrical and familial evidence']], [VA])
q('A young adult with normal cardiac imaging has monomorphic VT showing LBBB morphology and an inferior axis. The rhythm is catecholamine sensitive. Which origin is most characteristic?',
 'Right ventricular outflow tract',[
 ('Left posterior fascicular re-entry','That classically produces an RBBB pattern with a superior/left axis rather than this typical RVOT pattern.'),
 ('Inferolateral LV infarct scar in a known ischemic heart','The stem lacks a scar substrate and describes the characteristic idiopathic outflow pattern.'),
 ('The AV nodal slow pathway','An AV nodal circuit is supraventricular and does not define this ventricular focus.')],
 'Typical idiopathic RVOT tachycardia',
 '**LBBB morphology with an inferior axis suggests activation from a superior right-sided ventricular site.**',
 ['RVOT tachycardia often involves catecholamine-sensitive triggered activity.', 'A normal initial echo is helpful but does not eliminate the need to assess for concealed structural disease when features are atypical.'],
 '**Differentiate an idiopathic focus from arrhythmogenic cardiomyopathy.**',
 ['Syncope, family history, multiple morphologies or abnormal imaging can change the evaluation.', 'Beta blockade, selected drug treatment or catheter ablation may be appropriate according to symptoms and burden.'],
 [['Typical RVOT VT','LBBB morphology, inferior axis'],['Posterior fascicular VT','RBBB morphology, left/superior axis'],['Atypical presentation','Evaluate structural disease']], [VA], 'clinical_scenario')
q('A structurally normal heart has a relatively narrow monomorphic VT with RBBB morphology and left-axis deviation. EP assessment confirms left posterior fascicular VT. Which drug sensitivity is characteristic?',
 'Verapamil sensitivity',[
 ('Digoxin sensitivity as the defining feature','Digoxin is not the characteristic treatment for this re-entrant fascicular rhythm.'),
 ('A requirement for fibrinolysis to terminate the circuit','An idiopathic fascicular circuit is not treated by coronary thrombolysis.'),
 ('A universal response to atropine as the primary mechanism','Atropine does not define treatment of this ventricular re-entry mechanism.')],
 'Fascicular VT is a specific exception to a broad-complex safety rule',
 '**Proven idiopathic fascicular VT can be verapamil sensitive.**',
 ['The circuit involves specialized conduction tissue and a calcium-dependent component.', 'The posterior fascicular form commonly has an RBBB pattern and left/superior axis.'],
 '**Do not generalize this exception to undifferentiated VT.**',
 ['Empirical verapamil can be dangerous in scar-related or uncertain broad-complex tachycardia.', 'Ablation offers an effective strategy for recurrent symptomatic proven fascicular VT.'],
 [['Proven fascicular VT','May respond to verapamil'],['Undifferentiated broad-complex rhythm','Avoid empirical AV nodal CCB therapy'],['Recurrent fascicular VT','Consider catheter ablation']], [VA], 'clinical_scenario')
q('A patient has an otherwise unexplained fall in LVEF to 38% and a 24-hour PVC burden of 24%, predominantly from one focus. Which possibility should be assessed?',
 'PVC-induced cardiomyopathy',[
 ('A high PVC burden can never affect ventricular function','Frequent ectopy can cause or worsen ventricular dysfunction.'),
 ('An EF decline proves that every PVC is a harmless consequence','The relationship can be causal in either direction and requires investigation.'),
 ('Anticoagulation alone will remove the ectopic focus','Anticoagulation does not suppress ventricular ectopy.')],
 'Frequent ectopy can be a reversible driver of cardiomyopathy',
 '**A substantial PVC burden with otherwise unexplained LV dysfunction raises suspicion of PVC-induced cardiomyopathy.**',
 ['Burden, morphology, duration and additional electrical features influence risk.', 'CMR and clinical evaluation help exclude an underlying scar or cardiomyopathy that is producing the PVCs.'],
 '**Improvement after effective suppression supports a causal contribution.**',
 ['Catheter ablation is an important option for appropriate frequent predominantly monomorphic PVCs causing cardiomyopathy.', 'Follow ventricular function and ectopic burden after treatment rather than assuming immediate complete recovery.'],
 [['High PVC burden plus unexplained low EF','Consider PVC-induced dysfunction'],['Scar or structural abnormality','May indicate underlying cardiomyopathy'],['After suppression','Reassess EF and burden']], [VA], 'clinical_scenario')
q('A patient with ischemic scar has recurrent sustained monomorphic VT and ICD shocks despite appropriate amiodarone treatment. Which next strategy is supported?',
 'Refer for scar-related VT catheter ablation assessment',[
 ('Disable all ICD therapy without treating the recurrent VT','This removes protection without addressing the dangerous arrhythmia.'),
 ('Treat every appropriate shock as proof of device malfunction','Appropriate shocks can reflect a recurrent arrhythmic substrate rather than a faulty device.'),
 ('Increase an AV nodal CCB as the principal scar-VT treatment','AV nodal CCBs do not eliminate ventricular scar re-entry and can be harmful in systolic dysfunction.')],
 'Recurrent scar VT requires substrate-directed assessment',
 '**Catheter ablation can reduce recurrent VT and ICD therapies in appropriate patients.**',
 ['Scar channels can sustain re-entry that persists despite drug treatment.', 'Device interrogation distinguishes appropriate VT therapy from inappropriate shocks and informs programming.'],
 '**Review reversible triggers while planning definitive treatment.**',
 ['Evaluate ischemia, HF deterioration, electrolytes and adherence.', 'Electrical storm requires urgent multidisciplinary treatment, including sympathetic and hemodynamic management when appropriate.'],
 [['Appropriate recurrent ICD shocks','Assess the VT substrate and triggers'],['Inappropriate shocks','Assess sensing, supraventricular rhythms and programming'],['Drug-refractory scar VT','Consider ablation']], [VA], 'clinical_scenario')
q('A patient with possible sinus node dysfunction has intermittent dizziness. Which principle is central to a permanent pacemaker decision?',
 'Demonstrate a relationship between symptoms and bradycardia after addressing reversible causes',[
 ('A resting rate below 60/min mandates pacing in every adult','A numerical rate alone does not establish symptomatic sinus node disease.'),
 ('Any asymptomatic nocturnal pause requires immediate implantation','Sleep-related bradycardia can be physiological or associated with sleep apnea and is not an automatic pacing indication.'),
 ('A normal single clinic ECG excludes intermittent sinus pauses','Intermittent events may require ambulatory monitoring matched to symptom frequency.')],
 'Sinus node pacing is primarily a symptom-linked decision',
 '**There is no universal minimum heart rate or pause duration that alone mandates pacing in sinus node dysfunction.**',
 ['Correlate the rhythm with symptoms using suitable monitoring.', 'Review medication, thyroid disease, electrolyte abnormalities and sleep-related contributors.'],
 '**Distinguish sinus node disease from high-risk acquired AV block.**',
 ['Mobitz II or complete AV block may justify pacing without symptoms when nonreversible.', 'In sinus node disease, avoid implanting solely for an incidental asymptomatic low rate.'],
 [['Symptom-correlated sinus bradycardia','Potential pacing indication'],['Asymptomatic physiological bradycardia','Usually no pacing'],['Intermittent symptoms','Use appropriate rhythm monitoring']], [BRADY])
q('A patient has acquired Mobitz II AV block with no reversible or physiological cause. The patient denies syncope. What is the appropriate permanent pacing principle?',
 'Permanent pacing is recommended even without symptoms',[
 ('Wait for cardiac arrest because symptoms are absent','Mobitz II can progress unpredictably to more severe block; absence of symptoms does not remove the indication.'),
 ('Treat it as benign AV nodal Wenckebach in every case','Mobitz II is a distinct higher-risk pattern, often involving the His-Purkinje system.'),
 ('Use chronic atropine as an equivalent durable solution','Atropine is not an equivalent long-term treatment for established nonreversible high-risk AV block.')],
 'High-risk acquired AV block differs from sinus node dysfunction',
 '**Nonreversible Mobitz II, high-grade and complete AV block justify permanent pacing regardless of symptoms.**',
 ['The risk is progression and unreliable ventricular activation.', 'Confirm the ECG diagnosis and exclude medication, ischemic, metabolic, infectious and other reversible causes.'],
 '**Do not apply the symptom-only sinus node rule to this setting.**',
 ['Device mode and pacing strategy depend on atrial rhythm, ventricular function and anticipated pacing burden.', 'An ambiguous 2:1 block needs localization and assessment rather than automatic labeling as Mobitz II.'],
 [['Nonreversible Mobitz II','Pacing even if asymptomatic'],['Sinus node dysfunction','Usually needs symptom correlation'],['2:1 block','Requires further characterization']], [BRADY], 'clinical_scenario')
q('A healthy asymptomatic adult has progressive PR prolongation before a dropped QRS during sleep, a narrow QRS and normalization with activity. Which diagnosis is most likely?',
 'AV nodal Mobitz I block associated with increased vagal tone',[
 ('Mobitz II block established by any dropped beat','Mobitz II does not show the characteristic progressive PR prolongation described here.'),
 ('Complete AV block','Complete block has independent atrial and ventricular rhythms rather than this grouped Wenckebach pattern.'),
 ('Sinus arrest','During AV block, atrial impulses continue while ventricular conduction intermittently fails.')],
 'Pattern and context help localize AV block',
 '**Progressive PR prolongation followed by a nonconducted P wave is the classic Wenckebach sequence.**',
 ['A narrow QRS, sleep association and improvement with activity support AV nodal vagal physiology.', 'Not every Mobitz I pattern is automatically benign; symptoms, QRS width and suspected infranodal disease change assessment.'],
 '**Avoid unnecessary permanent pacing for an asymptomatic physiological finding.**',
 ['Review medication and sleep apnea when relevant.', 'Investigate syncope, daytime high-grade block or additional conduction disease rather than extending reassurance beyond the stated context.'],
 [['Mobitz I','Progressive PR prolongation before block'],['Mobitz II','Unexpected nonconducted P with otherwise fixed PR'],['Complete block','AV dissociation']], [BRADY], 'clinical_scenario')
q('A patient with recent tick exposure and compatible systemic symptoms develops rapidly fluctuating high-grade AV block due to Lyme carditis. Which pacing principle is appropriate?',
 'Treat the infection and use temporary pacing when needed while assessing recovery before permanent implantation',[
 ('Implant a permanent pacemaker immediately in every case without treating the cause','Lyme-associated block can recover with appropriate antimicrobial treatment.'),
 ('Withhold monitoring because all infection-related block is harmless','Rapid progression and severe block can be dangerous and require monitored care.'),
 ('Use an AV nodal blocker to stabilize conduction','Further AV nodal slowing can worsen bradycardia and is not treatment of Lyme carditis.')],
 'A reversible cause can change the permanent-device decision',
 '**Lyme carditis can cause high-grade AV block that improves with infection treatment.**',
 ['Monitor severe conduction disease and provide temporary support for symptomatic or unstable bradycardia.', 'Appropriate antibiotics address the cause rather than merely the electrical consequence.'],
 '**Reassess conduction recovery before committing to a permanent device.**',
 ['The immediate safety needs and the eventual long-term pacing decision are different questions.', 'Persistent block after adequate treatment warrants individualized reassessment.'],
 [['Acute high-grade Lyme block','Antimicrobial treatment and monitored support'],['Unstable bradycardia','Temporary pacing may be needed'],['After recovery assessment','Decide whether permanent pacing remains necessary']], [BRADY,ref('IDSA/AAN/ACR 2020 Guidelines for Lyme Disease: Lyme carditis','https://www.idsociety.org/practice-guideline/lyme-disease/')], 'clinical_scenario')
q('A pacemaker-dependent patient becomes dizzy. ECG shows regular pacing spikes that are not followed by QRS complexes. What is the device problem?',
 'Failure to capture',[
 ('Failure to sense as the only defining finding','Undersensing produces inappropriately timed pacing despite intrinsic beats; the key finding here is lack of myocardial depolarization after output.'),
 ('Failure to output','Output failure would show absent expected pacing spikes, rather than spikes without a subsequent QRS.'),
 ('Normal effective ventricular pacing','Effective ventricular capture should produce a ventricular depolarization after the pacing stimulus.')],
 'Separate sensing, output and capture',
 '**A pacing stimulus without the expected depolarization indicates loss of capture.**',
 ['Possible causes include lead displacement or failure, increased pacing threshold and metabolic abnormalities such as severe hyperkalemia.', 'Device interrogation and assessment of the patient\'s perfusion are urgent in a pacing-dependent patient.'],
 '**Provide immediate support while identifying the cause.**',
 ['Prepare external pacing or another emergency pacing strategy when clinically required.', 'A magnet does not reliably fix every capture problem; management depends on device type and the actual malfunction.'],
 [['No expected pacing spike','Consider output failure or inhibition'],['Spike without QRS','Failure to capture'],['Inappropriate spikes despite intrinsic beats','Consider undersensing']], [BRADY], 'clinical_scenario')

if __name__=='__main__':
    finalize('Cardiology',3,'Arrhythmias and Electrophysiology','cardiology-arrhythmias',rows,52)
