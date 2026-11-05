"""Explicit author distractor revision; not an independent clinician review."""
import json
from qbank_authoring import ROOT,finalize

def review():
    banks={b['chapterOrder']:b for p in (ROOT/'completed/Critical Care and Toxicology').glob('*/*/questions.json') for b in [json.loads(p.read_text(encoding='utf-8'))]}
    edits=[]
    def change(ch,n,needle,choices):
        item=banks[ch]['questions'][n-1];assert needle.casefold() in item['question'].casefold(),(ch,n)
        indices=[i for i in range(4) if i!=item['correctIndex']];assert len(choices)==3
        for i,(option,reason) in zip(indices,choices):item['options'][i]=option
        item['explanationTeaching']['otherOptions']=[dict(optionIndex=i,explanation=reason) for i,(_,reason) in zip(indices,choices)]
        item['optionReview']='Author-revised distractor plausibility; no independent clinician review'
        edits.append(item['id'])
    change(1,1,'118/72',[
      ('Persistent isolated hypovolemia is established by lactate alone','Lactate and organ dysfunction indicate a problem but do not uniquely establish the mechanism.'),
      ('Macrovascular pressure recovery establishes adequate microcirculatory perfusion','Pressure and tissue perfusion can dissociate.'),
      ('An elevated lactate proves that additional fluid will improve perfusion','Lactate does not establish fluid responsiveness or fluid tolerance.')])
    change(1,7,'ScvO2',[
      ('The high saturation proves that all tissues receive adequate oxygen','Venous blood can remain highly saturated despite regional maldistribution or impaired extraction.'),
      ('The saturation alone proves that cardiac output is excessively high','It reflects delivery, consumption and extraction, not cardiac output alone.'),
      ('The result identifies occult hemorrhage as the primary mechanism','Hemorrhage more often lowers delivery; the value does not specifically identify it.')])
    change(1,8,'epinephrine',[
      ('New tissue hypoperfusion is the only possible mechanism','Epinephrine can increase lactate through beta-2-related glycolytic effects even with improving perfusion.'),
      ('A rise necessarily proves an inadequate norepinephrine dose','Lactate alone cannot define the appropriate pressor dose.'),
      ('Hepatic failure is established by the temporal lactate rise','Reduced clearance is a differential but is not established by this association.')])
    change(1,10,'imaging',[
      ('CT pulmonary angiography before any bedside hemodynamic assessment','CT may be important for selected suspected causes but is not the general first rapid bedside characterization tool.'),
      ('Cardiac MRI as the initial study during unstable shock','MRI is usually impractical for immediate shock characterization.'),
      ('A chest radiograph as the definitive assessment of ventricular function','It can show associated findings but does not replace bedside cardiac functional assessment.')])
    change(1,11,'PEEP',[
      ('The distended IVC proves that no fluid could ever increase stroke volume','Venous appearance under positive pressure is not a definitive response test.'),
      ('The IVC establishes the exact transmural right-atrial pressure','Intrathoracic pressure affects measured venous dimensions and pressure relationships.'),
      ('The IVC alone establishes primary RV pump failure','Positive-pressure effects and other loading conditions can produce distension.')])
    change(1,24,'low SVR',[
      ('Pure vasoplegic shock with preserved pump function','The depressed output and LV dysfunction indicate an additional cardiac component.'),
      ('Pure LV cardiogenic shock with no vascular component','The low SVR indicates concurrent vasoplegia.'),
      ('Primary obstructive shock from pericardial tamponade','No obstructive findings are provided; the described abnormalities support mixed vascular and pump failure.')])
    change(1,29,'central access',[
      ('Delay the pressor until a central catheter is placed, using repeated fluids meanwhile','This can prolong hypotension and cause unnecessary fluid loading.'),
      ('Give norepinephrine only as intermittent peripheral boluses','A controlled infusion with an appropriate protocol is the intended approach.'),
      ('Use any peripheral cannula without site surveillance if the dose is low','Extravasation risk still requires suitable access and close monitoring.')])
    change(2,12,'pressure-control',[
      ('Improved compliance at unchanged resistance is the most likely explanation','Improved compliance would generally increase, rather than lower, delivered volume at the same pressure.'),
      ('A fixed pressure guarantees a fixed tidal volume irrespective of mechanics','Delivered volume remains dependent on mechanics, timing, effort and leaks.'),
      ('The lower tidal volume alone proves reduced patient CO2 production','Ventilator volume is not a direct measurement of metabolic CO2 production.')])
    change(2,21,'double-triggers',[
      ('The two breaths necessarily preserve the intended low delivered tidal volume','Breath stacking can produce a much larger effective volume.'),
      ('It proves that every patient should receive a higher routine tidal volume','Address drive, timing, flow and other causes rather than abandoning protective goals indiscriminately.'),
      ('It is diagnostic of an endotracheal cuff leak','A leak can cause other problems, but consecutive triggered breaths indicate a different interaction.')])
    change(2,24,'suddenly',[
      ('Assume worsening ARDS and increase PEEP before checking the airway/circuit','Displacement, obstruction, pneumothorax and equipment failure need immediate assessment.'),
      ('Increase sedation alone without checking tube patency','Sedation does not correct a displaced or blocked tube.'),
      ('Order CT before evaluating bedside reversible causes','Immediate airway and equipment checks cannot wait for transport imaging.')])
    change(2,28,'weak cough',[
      ('The SBT result alone proves the patient is ready for immediate extubation','The trial assesses ventilatory capacity, not all airway-protection requirements.'),
      ('The finding proves permanent ventilator dependence','Airway and secretion problems may improve or be addressed.'),
      ('A normal cuff-leak test would eliminate the aspiration risk','The cuff-leak test assesses stridor risk rather than cough and airway protection.')])
    change(2,34,'against continuing',[
      ('A pH of 7.28 in a cooperative COPD patient with a protected airway','This is a common indication for closely monitored bilevel NIV.'),
      ('Persistent but improving tachypnea during the first monitored treatment period','A responding patient may continue NIV with close reassessment.'),
      ('A mask leak that corrects with interface adjustment','A correctable interface problem alone is not the strongest reason to secure the airway.')])
    change(3,5,'citrate',[
      ('Citrate net overload with preserved metabolism and alkalosis','This is distinct from accumulation with a rising calcium gap and deteriorating systemic ionized calcium.'),
      ('Isolated calcium under-replacement without citrate accumulation','This can lower ionized calcium but does not as well explain the rising total-to-ionized ratio and full trend.'),
      ('Primary respiratory alkalosis lowering ionized calcium','It can alter calcium binding but is a poorer explanation for the combined protocol/metabolic pattern.')])
    change(3,9,'hypertonic saline',[
      ('Serum sodium alone without chloride, renal or volume assessment','Sodium is important but does not capture all relevant toxicity and physiological effects.'),
      ('ICP alone without systemic laboratory monitoring','A useful ICP response does not exclude electrolyte or renal complications.'),
      ('Serum osmolality alone as a substitute for clinical and renal reassessment','An isolated osmotic value does not provide a complete safety assessment.')])
    change(3,12,'visible convulsions',[
      ('Lumbar puncture before assessing persistent electrical seizure activity','CSF may be indicated for a cause, but EEG directly assesses the concern raised by unexplained postconvulsive coma.'),
      ('Repeat serum CK as the definitive test for ongoing seizures','CK can reflect prior muscle activity but cannot exclude electrographic status.'),
      ('A normal head CT as sufficient evidence against ongoing seizures','CT does not exclude nonconvulsive status epilepticus.')])
    change(3,16,'III',[
      ('Continue noninvasive airway observation despite loss of protection','Severe encephalopathy creates major aspiration and airway risk.'),
      ('Delay transplant-center discussion until spontaneous breathing fails','Referral should precede terminal deterioration.'),
      ('Use falling aminotransferases alone to defer escalation','Falling enzymes can coexist with worsening synthetic failure and loss of viable hepatocytes.')])
    change(3,21,'drawn back',[
      ('Differential hypoxemia from native LV ejection during femoral VA-ECMO','That is a VA-specific mixing problem, not immediate VV return-to-drainage flow.'),
      ('Oxygenator membrane thrombosis','This can impair oxygen transfer but differs from the stated circuit flow path.'),
      ('Increased systemic oxygen extraction alone','The observed return blood entering the drainage cannula defines recirculation.')])
    change(3,23,'24 mmHg',[
      ('Intra-abdominal hypertension without compartment syndrome','New organ dysfunction with sustained pressure above twenty supports the compartment syndrome.'),
      ('Isolated intrinsic AKI unrelated to abdominal pressure','The combined pressure, ventilation and renal pattern suggests a pressure-mediated systemic syndrome.'),
      ('Acute colonic pseudo-obstruction established by the pressure measurement alone','The pressure measurement does not define the underlying abdominal cause.')])
    change(3,28,'malnourished',[
      ('Critical illness myopathy as the primary explanation','It may coexist but does not explain the abrupt feeding-linked phosphate shift as well.'),
      ('Primary hyperparathyroidism','This can lower phosphate but does not fit the acute nutritional trigger and syndrome.'),
      ('Respiratory alkalosis as the sole established cause','It can shift phosphate, but the feeding relationship and broader deficits favor refeeding syndrome.')])
    change(3,32,'D-dimer',[
      ('Immune thrombotic thrombocytopenic purpura','TTP is a TMA; prominent PT prolongation and consumption in sepsis favor DIC.'),
      ('Heparin-induced thrombocytopenia alone','HIT can cause thrombosis but does not typically explain this broad factor-consumption pattern.'),
      ('Immune thrombocytopenia','ITP does not generally cause prolonged PT and low fibrinogen.')])
    change(3,38,'quiet',[
      ('Major depression established by reduced activity alone','Fluctuating attention is more characteristic of delirium.'),
      ('Coma','The patient has adequate arousal for attention testing.'),
      ('Dementia as established from the acute examination','An acute fluctuating course requires delirium assessment even if baseline cognitive disease is possible.')])
    change(3,40,'memory',[
      ('Isolated critical illness polyneuropathy as the complete explanation','Neuropathy does not account for the cognitive and psychological domains.'),
      ('Post-traumatic stress disorder alone','Trauma symptoms can coexist, but the combined syndrome includes physical and cognitive impairment.'),
      ('Persistent delirium as established by memory complaints alone','Delirium requires an appropriate acute attention/awareness pattern; recovery needs are broader.')])
    change(7,30,'ataxic',[
      ('Remain at the same altitude with acetazolamide alone','Severe neurological altitude illness requires urgent descent/oxygen rather than relying on acclimatization medication.'),
      ('Treat as uncomplicated AMS with analgesia and planned ascent the next morning','Ataxia and confusion indicate an emergency rather than uncomplicated AMS.'),
      ('Use nifedipine alone without arranging descent','Nifedipine is a selected HAPE adjunct, not definitive HACE treatment.')])
    # Replace an overly broad numeric distractor with clinically used alternative targets.
    change(8,13,'SpO2',[
      ('94–98% as the exact range stated by AHA 2025','This is used by some other guidance; the explicitly asked AHA range is ninety to ninety-eight.'),
      ('88–92% as the routine target for every postarrest adult','This is not the universal AHA postarrest range; individual chronic respiratory considerations require separate assessment.'),
      ('99–100% regardless of the arterial oxygen tension','This can encourage unnecessary hyperoxemia.')])
    slugs={1:'critical-shock',2:'critical-ventilation',3:'critical-organ-support',4:'critical-electrolytes',5:'critical-poisoning',6:'critical-envenomation',7:'critical-environment',8:'critical-resuscitation'}
    for order,bank in sorted(banks.items()):finalize('Critical Care and Toxicology',order,bank['document'],slugs[order],bank['questions'],bank['targetQuestions'])
    (ROOT/'critical-care-author-choice-review.json').write_text(json.dumps(dict(revisedQuestions=len(edits),ids=edits,review='Author plausibility revision; not independent clinical review'),indent=2),encoding='utf-8')
    print('Explicit distractor revisions:',len(edits))

if __name__=='__main__':review()
