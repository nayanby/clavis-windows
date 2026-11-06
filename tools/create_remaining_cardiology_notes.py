"""Directly authored Cardiology modules, grouped by mechanism and clinical decisions."""
from clinical_note_authoring import *
HF=('ACC HFrEF treatment pathway, 2024','https://doi.org/10.1016/j.jacc.2023.12.024')
AF=('ESC atrial fibrillation guideline, 2024','https://academic.oup.com/eurheartj/article/45/36/3314/7738779')
VA=('ESC ventricular arrhythmia guideline, 2022','https://academic.oup.com/eurheartj/article/43/40/3997/6675633')
VHD=('ESC/EACTS valvular heart disease guideline, 2025','https://academic.oup.com/eurheartj/article/46/44/4635/8234488')
MYO=('ESC myocarditis/pericarditis guideline, 2025','https://doi.org/10.1093/eurheartj/ehaf192')
HCM=('AHA/ACC hypertrophic cardiomyopathy guideline, 2024','https://doi.org/10.1016/j.jacc.2024.02.014')
LIP=('ACC/AHA dyslipidemia guideline, 2026','https://doi.org/10.1161/CIR.0000000000001423')
HT=('AHA/ACC high blood pressure guideline, 2025','https://doi.org/10.1161/CIR.0000000000001356')

def heart_failure():
 write('Cardiology','Heart Failure',[
 S('Classification and diagnosis',T('Category|LVEF|Required distinction','''HFrEF|≤40%|Reduced systolic function
 HFmrEF|41–49%|Symptoms/signs plus evidence supporting HF
 HFpEF|≥50%|Symptoms/signs plus objective evidence of raised filling pressure or structural/functional abnormality
 HF with improved EF|Previous ≤40%, subsequently >40%|Continue disease-modifying treatment; improvement is not cure''')+U('''Assess congestion, perfusion, precipitant and cause: ischemia, hypertension, valve disease, arrhythmia, myocarditis, toxins or inherited disease.
 Natriuretic peptides support diagnosis; obesity can lower values, while AF and CKD can raise them. A preserved EF does not exclude HF.
 Echocardiography: EF, chamber size, valves, RV function and estimated pressures. Use CMR when tissue diagnosis or accurate ventricular assessment is needed.''')),
 S('HFrEF drugs: the four pillars',T('Class|Benefit / role|Key precautions','''ARNI; ACE inhibitor/ARB if unsuitable|Disease modification|BP, potassium, renal function; 36-hour gap between ACE inhibitor and sacubitril/valsartan; avoid in pregnancy and relevant angioedema history
 Evidence-based beta blocker|Carvedilol, bisoprolol or metoprolol succinate|Start/titrate when stable; do not newly escalate in shock
 Mineralocorticoid antagonist|Spironolactone/eplerenone|Hyperkalemia; usual initiation requires eGFR >30 and K <5.0 mmol/L
 SGLT2 inhibitor|Dapagliflozin/empagliflozin; benefit does not require diabetes|Volume status, genital infection and ketoacidosis risk; hold during major acute illness/fasting as appropriate''')+U('''Introduce all four classes promptly at tolerated doses; do not wait for maximal dosing of one before adding the others.
 Loop diuretics relieve congestion; they do not replace the four pillars.
 Selected additions: ivabradine for eligible sinus-rhythm patients with persistent tachycardia; hydralazine–nitrate in specified settings; digoxin for selected symptomatic/rate-control indications. Monitor renal function and toxicity.''')),
 S('Acute decompensation',T('Pattern|Immediate treatment emphasis','''Congested, adequately perfused|IV loop diuretic; monitor urine output, weight, renal function and electrolytes
 Pulmonary edema with high BP|Noninvasive ventilation when indicated; IV vasodilator if BP permits; diuresis
 Cardiogenic shock|Urgent cause correction, monitored vasoactive support, selected mechanical support and revascularization when ischemic
 Isolated RV failure|Identify cause; avoid reflex large-volume loading or aggressive preload reduction''')+U('''Look for ACS, infection, uncontrolled BP, AF, pulmonary embolism, nonadherence, renal deterioration and offending drugs.
 Reassess response to diuresis. A small creatinine increase during effective decongestion is not an automatic reason to leave severe congestion untreated.
 Before discharge: oral regimen, four-pillar plan, electrolyte/renal review, education and early follow-up.''')),
 S('HFpEF, devices and advanced HF',U('''HFpEF/HFmrEF: SGLT2 inhibition, diuretics for congestion, and treatment of hypertension, AF, ischemia, obesity and other causes; do not apply every HFrEF drug indication indiscriminately.
 Primary-prevention ICD: selected patients with persistently low EF despite adequate treatment and meaningful expected survival; observe post-MI and treatment waiting periods.
 CRT: strongest standard indication is symptomatic HFrEF with LVEF ≤35%, sinus rhythm, LBBB and QRS ≥150 ms despite treatment; other groups require specific criteria.
 Persistent NYHA III–IV symptoms, repeated admissions, low output or intolerance of therapy: evaluate for advanced-HF care, transplant/LVAD eligibility and concurrent palliative support.'''))],[HF,('ESC HF focused update, 2023','https://doi.org/10.1093/eurheartj/ehad195')])

def arrhythmias():
 write('Cardiology','Arrhythmias Electrophysiology',[
 S('First decision: rhythm and stability',T('Rhythm|Initial approach','''Unstable tachycardia with pulse|Synchronized cardioversion; polymorphic VT or inability to synchronize requires defibrillation
 VF/pulseless VT|Defibrillation and resuscitation
 Regular narrow-complex tachycardia, stable|Vagal maneuver, then adenosine when appropriate
 Regular wide-complex tachycardia|Treat as VT until shown otherwise, especially with structural disease
 Irregular wide-complex tachycardia|Consider AF with pre-excitation or polymorphic VT; avoid reflex AV-nodal blockade''')+U('''AV dissociation, capture/fusion beats and concordance support VT. Hemodynamic stability does not exclude VT.
 Adenosine may expose flutter waves without terminating flutter. Avoid it in an irregular wide-complex rhythm.''')),
 S('Antiarrhythmic drugs: one comparison',T('Class / agents|Main action / use|Major trap','''IA: procainamide, quinidine, disopyramide|Sodium blockade + repolarization prolongation|QT prolongation/torsades; disopyramide anticholinergic and negative-inotropic effects
 IB: lidocaine, mexiletine|Ventricular arrhythmias in selected settings|Neurological toxicity; not routine AF treatment
 IC: flecainide, propafenone|Selected atrial rhythm control|Avoid with previous MI/significant structural disease; AV-nodal protection may be needed to prevent 1:1 flutter
 II: beta blockers|AV-nodal slowing; adrenergic arrhythmias|Bradycardia, AV block; caution in decompensated HF
 III: amiodarone|Atrial/ventricular rhythm control|Thyroid, pulmonary, hepatic, ocular and interaction toxicity; bradycardia
 III: sotalol, dofetilide|Selected rhythm control|Renal dosing, QT monitoring and torsades risk
 IV: verapamil, diltiazem|AV-nodal slowing|Avoid in HFrEF, pre-excited AF and undiagnosed wide-complex tachycardia
 Adenosine / digoxin|Transient AV block / vagal AV slowing|Adenosine: transient effect; digoxin: renal accumulation, interactions and toxicity''')),
 S('AF: stroke prevention, rate and rhythm',U('''Anticoagulation follows thromboembolic risk, not whether AF is paroxysmal or sinus rhythm has been restored. ESC 2024: CHA₂DS₂-VA ≥2 generally warrants anticoagulation; consider at 1.
 DOACs preferred when eligible; mechanical valves and moderate-to-severe mitral stenosis require a vitamin K antagonist. Aspirin is not equivalent stroke prevention.
 Rate control: beta blocker or appropriate calcium-channel blocker; digoxin in selected patients. Avoid verapamil/diltiazem with reduced EF.
 Unstable AF: electrical cardioversion without delaying for prolonged anticoagulation preparation; start anticoagulation as soon as safe.
 Elective cardioversion: ESC 2024 uses AF >24 hours to trigger ≥3 weeks therapeutic anticoagulation or transesophageal-echo exclusion of thrombus. Usually continue ≥4 weeks afterward; longer treatment follows stroke risk.
 Rhythm control includes cardioversion, selected antiarrhythmics and catheter ablation. Early rhythm control and ablation have defined roles; recurrent symptoms are not the only consideration.''')),
 S('Pre-excitation, torsades and bradycardia',T('Problem|Key management','''Pre-excited AF|Avoid beta blockers, diltiazem/verapamil, digoxin, adenosine and IV amiodarone; use cardioversion or an appropriate accessory-pathway-active drug under specialist monitoring
 Torsades with prolonged QT|Stop QT-prolonging drugs; correct K/Mg; IV magnesium; defibrillate if unstable; selected pacing for pause-dependent recurrence
 Acquired symptomatic bradycardia|Treat reversible causes; atropine in appropriate cases; pacing/chronotropic support if ineffective
 Mobitz II, high-grade or complete AV block|Assess urgent pacing; persistent nonreversible disease generally warrants permanent pacing
 Sinus-node dysfunction|Symptom–rhythm correlation matters; no single heart-rate cutoff establishes a pacing indication''')+U('''Long-QT and Brugada syndromes require syndrome-specific drug precautions and sudden-death assessment.
 QTc formulas are rate dependent; Bazett often overcorrects at high heart rates. QT prolongation plus low potassium and multiple interacting drugs is a preventable torsades setting.
 Frequent ectopy can cause cardiomyopathy; do not call all PVCs harmless without burden and structural assessment.'''))],[AF,VA,('ESC pacing guideline, 2021','https://doi.org/10.1093/eurheartj/ehab364')])

def pharmacology():
 write('Cardiology','Pharmacology',[
 S('Antianginal and antihypertensive drugs',T('Class|Useful effects|Important adverse effects / exclusions','''Beta blockers|Lower heart rate, BP and oxygen demand|Bradycardia/AV block; avoid abrupt withdrawal; do not use alone for vasospastic angina
 Dihydropyridine CCB|Arterial dilation: hypertension/angina|Ankle edema, headache, flushing
 Verapamil/diltiazem|AV-nodal slowing and antianginal action|Bradycardia, AV block, negative inotropy; avoid in HFrEF and pre-excited AF
 Nitrates|Venodilation; angina relief|Hypotension, headache, tolerance; avoid with recent PDE5 inhibitor and preload-dependent RV infarction
 Ranolazine|Antianginal with limited HR/BP effect|QT prolongation and interactions
 ACE inhibitor/ARB|Hypertension, proteinuric CKD and selected cardiovascular protection|Hyperkalemia/creatinine rise; avoid pregnancy; ACE inhibitor cough/angioedema''')+U('''Do not combine an ACE inhibitor with an ARB routinely. Stop ACE inhibition ≥36 hours before sacubitril/valsartan.
 A rise in creatinine after RAAS blockade requires assessment of volume status, drugs and renovascular disease; it is not automatically intrinsic nephrotoxicity.''')),
 S('Diuretics and mineralocorticoid antagonists',T('Class|Site / effect|Typical laboratory pattern','''Loop|Thick ascending limb; potent natriuresis|Hypokalemic metabolic alkalosis; hypomagnesemia; ototoxicity in risk settings
 Thiazide/thiazide-like|Distal convoluted tubule|Hyponatremia, hypokalemia, hyperuricemia; reduced urine calcium
 Spironolactone/eplerenone|Mineralocorticoid antagonism|Hyperkalemia; spironolactone can cause gynecomastia
 Amiloride|ENaC blockade|Hyperkalemia; useful in selected ENaC-related states''')+P('Diuretic choice depends on indication and kidney function. Combine loop and distal blockade only with electrolyte/renal surveillance.')),
 S('Antiplatelets and anticoagulants',T('Group|Mechanism / key use|Safety distinction','''Aspirin|Irreversible platelet COX inhibition|GI bleeding; not an AF anticoagulant substitute
 P2Y₁₂ inhibitors|Clopidogrel, prasugrel, ticagrelor|Prasugrel contraindicated after stroke/TIA; ticagrelor can cause dyspnea
 UFH|Antithrombin-mediated anticoagulation|aPTT/anti-Xa monitoring by protocol; HIT risk; protamine reversal
 LMWH|Predominantly anti-Xa activity|Renal accumulation; protamine only partially reverses
 Warfarin|Vitamin K antagonist|INR monitoring, interactions, teratogenicity; required for mechanical valves
 DOACs|Direct thrombin or factor Xa inhibition|Renal function/interactions matter; not for mechanical valves''')+U('''Bleeding treatment is agent-, timing- and severity-specific; antiplatelet and anticoagulant reversal are different problems.
 Suspected HIT: stop all heparin and use an appropriate nonheparin anticoagulant when indicated; platelet count can remain numerically normal despite a >50% fall.''')),
 S('Drugs requiring focused toxicity monitoring',T('Drug|Key toxicity / interaction','''Digoxin|Nausea, visual/neuro symptoms and arrhythmias; renal accumulation; hypokalemia increases toxicity; severe poisoning may need digoxin-specific Fab
 Amiodarone|Thyroid, liver, pulmonary and ocular toxicity; increases exposure to selected drugs including warfarin/digoxin
 Statins|Muscle symptoms and rare rhabdomyolysis; interactions vary by agent
 SGLT2 inhibitors|Genital infection, volume depletion, euglycemic ketoacidosis; benefits extend beyond diabetes
 Myosin inhibitors|Systolic dysfunction and drug interactions; structured LVEF monitoring''')+P('Keep antiarrhythmic classification and rhythm-specific selection in the Arrhythmias module; this section consolidates toxicity and interactions.'))],[HF,AF,VA,LIP])

if __name__=='__main__':
 heart_failure();arrhythmias();pharmacology()
