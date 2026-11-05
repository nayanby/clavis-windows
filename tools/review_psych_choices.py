"""Explicit author revision of Psychiatry distractors before installation."""
import json
from qbank_authoring import ROOT,finalize

def review():
    banks={b['chapterOrder']:b for p in (ROOT/'completed/Psychiatry').glob('*/*/questions.json') for b in [json.loads(p.read_text(encoding='utf-8'))]};edits=[]
    def change(ch,n,needle,choices):
        item=banks[ch]['questions'][n-1];assert needle.casefold() in item['question'].casefold(),(ch,n)
        indices=[i for i in range(4) if i!=item['correctIndex']];assert len(choices)==3
        for i,(option,reason) in zip(indices,choices):item['options'][i]=option
        item['explanationTeaching']['otherOptions']=[dict(optionIndex=i,explanation=reason) for i,(_,reason) in zip(indices,choices)]
        item['optionReview']='Author-revised distractor plausibility; no independent clinician review';edits.append(item['id'])
    change(1,18,'lithium',[
      ('Selective prevention of depression with no established antimanic effect','Lithium also has established antimanic and maintenance efficacy.'),
      ('Rapid rescue of severe agitation within minutes as its principal use','Its role differs from immediate sedative rescue medication.'),
      ('Maintenance only after at least five failed antipsychotic regimens','Lithium need not be reserved to that late sequence.')])
    change(1,19,'baseline',[
      ('Serum lithium levels alone, with organ tests only after symptoms develop','Kidney, thyroid and calcium monitoring are also necessary.'),
      ('Liver enzymes and platelet counts as the complete primary monitoring set','These do not replace the kidney/endocrine assessment central to lithium.'),
      ('Annual ECG alone with no serial blood levels','A cardiac assessment may be relevant but cannot substitute for exposure and organ monitoring.')])
    change(2,13,'first episode',[
      ('Antipsychotic treatment alone with psychosocial care deferred until all symptoms resolve','Psychological, family and functional support are part of early care.'),
      ('CBT alone as the routine preferred complete treatment for established first-episode psychosis','Guidance recommends offering antipsychotic treatment with psychological interventions, with shared decisions and review if medication is declined.'),
      ('Routine initiation of two antipsychotics to prevent treatment resistance','Routine polypharmacy is not the recommended initial strategy.')])
    change(2,14,'two adequate',[
      ('Add a second nonclozapine antipsychotic as the routine next step','This should not displace indicated clozapine assessment.'),
      ('Require four further nonclozapine switches before discussing clozapine','That can delay an effective treatment without a guideline requirement.'),
      ('Treat persistent psychosis with antidepressant augmentation alone','This does not provide the indicated treatment-resistant psychosis strategy.')])
    change(2,18,'troponin',[
      ('Benign titration-related sinus tachycardia','This is common, but fever, chest symptoms and elevated troponin require urgent myocarditis assessment.'),
      ('Orthostatic hypotension alone','It does not adequately explain the inflammatory myocardial-injury pattern.'),
      ('Panic-related chest discomfort as the complete explanation','An elevated troponin and treatment context cannot be dismissed as panic.')])
    change(2,23,'restlessness',[
      ('Worsening psychotic agitation requiring automatic dose escalation','The dose-linked inner urge to move is characteristic of akathisia.'),
      ('Drug-induced parkinsonism','Bradykinesia and rigidity differ from the urge to move.'),
      ('Restless legs syndrome','This more often has a leg-predominant evening/rest pattern rather than the described generalized dose-related syndrome.')])
    change(3,11,'long-term',[
      ('Maintenance benzodiazepine monotherapy as the default long-term plan','Dependence and long-term outcome concerns make this unsuitable as routine preferred care.'),
      ('Propranolol alone to treat the entire syndrome','Reducing some autonomic symptoms does not provide the core evidence-based panic treatment.'),
      ('General supportive counseling without panic-focused or medication treatment despite persistent impairment','Support is helpful, but structured evidence-based treatment should be offered.')])
    change(3,14,'cannot tolerate',[
      ('Quetiapine as a routine primary-care GAD next step','Antipsychotic treatment is not the corresponding routine NICE primary-care recommendation.'),
      ('Long-term diazepam as the standard maintenance replacement','Long-term dependence and safety concerns limit this approach.'),
      ('Propranolol as a full treatment of persistent cognitive worry','It does not adequately treat the entire GAD syndrome.')])
    change(4,10,'acamprosate',[
      ('Hepatic oxidative metabolism as its main route of elimination','Acamprosate is not substantially hepatically metabolized.'),
      ('Current opioid exposure as an automatic receptor-antagonist contraindication','This is a naltrexone concern, not acamprosate pharmacology.'),
      ('A requirement for ECG monitoring because of a characteristic QT-prolonging effect','Renal suitability is the more relevant issue asked here.')])
    change(4,14,'receptor',[
      ('Full mu-opioid receptor agonism','This describes methadone more closely.'),
      ('Competitive mu-opioid receptor antagonism without agonist activity','This describes naltrexone rather than buprenorphine.'),
      ('Alpha-2 adrenergic agonism','Clonidine/lofexidine use this mechanism for selected withdrawal symptoms.')])
    change(4,15,'too soon',[
      ('A reduction in opioid concentration caused by immediate renal elimination','Precipitated withdrawal is a receptor-displacement phenomenon rather than sudden drug removal.'),
      ('Naloxone in every prescribed formulation is systemically active to the same extent as IV naloxone','Buprenorphine itself can precipitate withdrawal through high-affinity partial agonism.'),
      ('An immune hypersensitivity reaction that can be prevented with an antihistamine','The mechanism is pharmacological and requires an appropriate initiation strategy.')])
    change(4,20,'psychosocial',[
      ('CBT alone should always replace contingency management','CBT can be helpful, but contingency management has particularly strong evidence as a core component.'),
      ('Withdrawal management without an ongoing psychosocial plan','Detoxification alone does not address continuing relapse risk.'),
      ('Medication-only care as a universally established first-line strategy','Selected off-label treatments have roles, but no universal medication-only approach replaces the core psychosocial intervention.')])
    change(4,22,'varenicline',[
      ('Norepinephrine/dopamine reuptake inhibition','This is bupropion’s relevant mechanism.'),
      ('Full nicotinic agonist delivery that replaces smoking nicotine','This describes nicotine replacement more closely than varenicline’s partial agonism.'),
      ('Muscarinic acetylcholine receptor antagonism','Varenicline targets nicotinic rather than muscarinic receptors.')])
    change(5,2,'brief tool',[
      ('MoCA','This assesses cognition more broadly and is not the specified rapid delirium tool.'),
      ('MMSE','It can detect cognitive impairment but is not the recommended general-setting delirium assessment in this guidance.'),
      ('CAM-ICU as the specified routine general-setting choice instead','NICE specifies CAM-ICU/ICDSC for critical care or postoperative recovery; 4AT is the named general-setting option.')])
    change(5,7,'not threatening',[
      ('Give haloperidol routinely to shorten delirium in every case','It is not routine disease-modifying treatment for all delirium.'),
      ('Use a benzodiazepine as the default treatment for all delirium distress','It can worsen nonwithdrawal delirium and respiratory risk.'),
      ('Use physical restraint before trying communication and environmental measures','This can worsen distress and harm; a proportionate indication is required.')])
    change(6,3,'pair',[
      ('Sertraline and fluoxetine as the pair with the same dose-dependent regulatory warning','Their QT profiles are not identical to citalopram/escitalopram.'),
      ('Mirtazapine and bupropion as the equivalent specifically warned pair','These have different primary adverse-effect and regulatory profiles.'),
      ('Vortioxetine and agomelatine as the pair with the same QT dose restrictions','These are not the corresponding named pair.')])
    change(6,4,'appetite',[
      ('Bupropion','Its generally activating profile and appetite effects are less aligned with this symptom-targeting question.'),
      ('Fluoxetine','It is effective for depression but does not share the same usual sedating/appetite-increasing profile.'),
      ('Reboxetine','Its noradrenergic profile is less suited to the specifically requested sleep/appetite profile.')])
    change(6,5,'contraindication',[
      ('Obesity without an eating-disorder history','Obesity alone is not the named seizure-risk contraindication.'),
      ('Stable generalized anxiety disorder','Anxiety may affect tolerability but is not the same formal contraindication.'),
      ('A history of SSRI-related sexual dysfunction','This can be a reason to consider alternatives such as bupropion when otherwise suitable.')])
    change(6,6,'tyramine',[
      ('Inhibition of norepinephrine synthesis causing compensatory hypertension','The reaction involves increased catecholamine availability/release, not reduced synthesis.'),
      ('Tyramine-induced serotonin depletion as the primary pressor pathway','The characteristic dietary pressor reaction is mainly adrenergic.'),
      ('An IgE-mediated food reaction as the required mechanism','This is a pharmacological interaction rather than a required allergy.')])
    change(6,12,'tardive',[
      ('Anticholinergic drugs as the preferred targeted TD treatment','These treat some other extrapyramidal syndromes and can worsen TD.'),
      ('Increasing the causative dopamine blocker as a durable cure','This may mask movement temporarily without resolving the syndrome.'),
      ('Levodopa as routine TD treatment','This is not the established targeted treatment and can worsen psychiatric or movement problems.')])
    slugs={1:'psych-mood',2:'psych-psychosis',3:'psych-anxiety',4:'psych-substance',5:'psych-neuropsychiatry',6:'psych-emergencies'}
    for order,b in sorted(banks.items()):finalize('Psychiatry',order,b['document'],slugs[order],b['questions'],b['targetQuestions'])
    (ROOT/'psychiatry-author-choice-review.json').write_text(json.dumps(dict(revisedQuestions=len(edits),ids=edits,review='Author revision; no independent clinician review'),indent=2),encoding='utf-8')
    print('Explicit distractor revisions:',len(edits))

if __name__=='__main__':review()
