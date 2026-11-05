"""Author plausibility pass for Clinical Examination; no independent clinical review."""
import json
from qbank_authoring import ROOT,finalize

def review():
    banks={b['chapterOrder']:b for p in (ROOT/'completed/Clinical Examination').glob('*/*/questions.json') for b in [json.loads(p.read_text(encoding='utf-8'))]};edits=[]
    def change(ch,n,needle,choices):
        item=banks[ch]['questions'][n-1];assert needle.casefold() in item['question'].casefold(),(ch,n)
        indices=[i for i in range(4) if i!=item['correctIndex']];assert len(choices)==3
        for i,(option,reason) in zip(indices,choices):item['options'][i]=option
        item['explanationTeaching']['otherOptions']=[dict(optionIndex=i,explanation=reason) for i,(_,reason) in zip(indices,choices)]
        item['optionReview']='Author-revised distractor plausibility; no independent clinician review';edits.append(item['id'])
    change(1,6,'Spoon',[
      ('Vitamin B12 deficiency','Macrocytic deficiency has other clues; spoon nails more classically prompt iron assessment.'),
      ('Chronic hypoxemic lung disease','This is more associated with selected clubbing contexts than koilonychia.'),
      ('Psoriasis','Pitting and other nail changes are more typical than the classic iron-associated spoon pattern.')])
    change(1,10,'generalized',[
      ('Multiple enlarged nodes within one cervical chain','This remains one regional basin.'),
      ('A single supraclavicular node with systemic symptoms','That is concerning but not generalized by distribution.'),
      ('Bilateral nodes within one contiguous regional drainage area only','The definition requires noncontiguous regions, not simply multiple nearby nodes.')])
    change(2,1,'jugular',[
      ('A single palpable upstroke with little respiratory change','This favors a carotid arterial pulse.'),
      ('A fixed visible neck swelling without cardiac-cycle variation','This is not a venous pulse waveform.'),
      ('A palpable thrill over a vessel independent of the venous column height','This suggests turbulent arterial flow rather than the characteristic jugular pulse.')])
    change(2,6,'constrictive',[
      ('A markedly blunted y descent','This more strongly supports uncomplicated tamponade.'),
      ('Isolated absence of the a wave during atrial fibrillation','That reflects rhythm rather than specifically separating constriction from tamponade.'),
      ('A large systolic cv wave with a pulsatile liver','This points more strongly to tricuspid regurgitation.')])
    change(2,7,'abdominal',[
      ('A brief venous rise that promptly returns despite continued pressure','A transient response can occur normally; persistence is the important distinction.'),
      ('A specific diagnosis of tricuspid stenosis','The maneuver is not specific to one valve lesion.'),
      ('A direct quantitative estimate of left-ventricular ejection fraction','It probes filling-pressure response rather than EF.')])
    change(2,8,'apical impulse',[
      ('Isolated RV pressure loading as the most direct explanation','A parasternal heave is more characteristic of an RV pressure load.'),
      ('A normal small LV inferred because the impulse is palpable','Palpability does not establish chamber size and displacement raises another question.'),
      ('Severe mitral stenosis uniquely established by the apical location','The finding is not specific for that lesion.')])
    change(2,19,'click',[
      ('Later in systole with a shorter murmur','This is more typical of increased LV volume during squatting.'),
      ('Unchanged because prolapse timing is independent of preload','MVP click timing characteristically changes with LV volume.'),
      ('Earlier only because standing necessarily increases systemic venous return','The timing may be earlier, but the stated mechanism is wrong: standing reduces filling.')])
    change(3,6,'spoken',[
      ('Bronchophony','This is increased clarity/loudness of transmitted speech rather than the specific vowel-quality change.'),
      ('Whispered pectoriloquy','This is unusually clear transmission of whispered speech.'),
      ('A pleural friction rub','This is a grating nonvocal respiratory sound.')])
    change(3,7,'neck',[
      ('Diffuse intrathoracic small-airway narrowing causing expiratory wheeze','The neck-centered inspiratory pattern favors an upper/central source.'),
      ('Pleural inflammation producing a friction rub','A rub has a different grating localized character.'),
      ('Parenchymal reopening producing fine crackles','Crackles are discontinuous and do not explain this high-pitched neck sound.')])
    change(3,12,'grating',[
      ('A pericardial friction rub','A cardiac-cycle rub may persist during breath holding.'),
      ('Coarse airway secretions','These often vary with cough and have a different sound quality.'),
      ('A transmitted cardiac murmur','This follows cardiac flow rather than disappearing solely with respiratory movement.')])
    change(3,16,'cycles',[
      ('Kussmaul breathing','This is sustained deep ventilation rather than a crescendo–decrescendo apnea cycle.'),
      ('Cluster/Biot breathing','This can be periodic but lacks the characteristic gradual waxing and waning pattern.'),
      ('Obstructive apneas with persistent inspiratory effort','The described central-apnea pattern lacks that ongoing obstructed effort.')])
    change(3,21,'segment',[
      ('Respiratory Hoover sign','This involves lower-rib mechanics in hyperinflation rather than a focal traumatic segment.'),
      ('Diaphragmatic abdominal paradox','This primarily concerns inward abdominal motion rather than a detached local chest-wall segment.'),
      ('Unilateral loss of expansion from a pleural effusion','That reduces movement but does not create the characteristic reverse movement of a flail segment.')])
    change(4,2,'nodular',[
      ('Cirrhosis confirmed by palpation alone','Nodularity is not sufficiently specific.'),
      ('Metastatic carcinoma confirmed without imaging or tissue context','It is a concern but not a definitive palpation diagnosis.'),
      ('Congestive hepatomegaly as the unique explanation','Congestion can enlarge the liver but does not uniquely explain the hard irregular pattern.')])
    change(4,6,'right lower',[
      ('Uncomplicated acute viral hepatitis as the usual cause','Hepatitis can affect the spleen but is less typical of this massive degree.'),
      ('Isolated immune thrombocytopenia as the expected explanation','Massive splenomegaly should prompt an alternative or additional diagnosis.'),
      ('Portal hypertension proved as the only possible cause','It is possible, but size alone does not establish it or exclude myeloproliferative/infectious causes.')])
    change(4,8,'midline',[
      ('To compress the aorta and stop all vascular pulsation','This is not the purpose of the maneuver.'),
      ('To increase superficial abdominal-wall transmission','The goal is to dampen that confounding route.'),
      ('To determine whether the fluid is a transudate','The maneuver cannot determine ascitic chemistry.')])
    change(4,15,'inspiratory arrest',[
      ('Psoas sign','This uses hip movement rather than subcostal inspiratory palpation.'),
      ('Courvoisier finding','This concerns a palpable nontender gallbladder in the jaundice context.'),
      ('Rovsing sign','This describes right-sided pain with left-sided abdominal pressure in the appropriate context.')])
    change(4,22,'suprapubic',[
      ('Use shifting dullness alone to confirm the focal swelling is ascites','The focal suprapubic/voiding pattern makes bladder assessment more directly informative.'),
      ('Diagnose a pelvic tumor before measuring retained urine','Retention is a common reversible mimic.'),
      ('Exclude retention because earlier dribbling proves complete emptying','Overflow can occur with substantial retained urine.')])
    change(5,4,'MRC',[
      ('2/5','This is movement with gravity eliminated.'),
      ('4/5','This includes movement against added resistance.'),
      ('1/5','This is a visible/palpable contraction without effective joint movement.')])
    change(5,13,'alternating',[
      ('Dysmetria','This is inaccurate range or endpoint rather than the specific alternating-movement sign.'),
      ('Intention tremor','This is an oscillation that increases toward a target.'),
      ('Apraxia','This is impaired learned action not adequately explained by basic motor/sensory deficits and requires a different assessment.')])
    change(5,20,'lower-facial',[
      ('An isolated right peripheral seventh-nerve palsy','This does not explain the associated arm pyramidal signs.'),
      ('A right pontine facial-nuclear/fascicular lesion as the best fit','That more often affects the ipsilateral whole face and can create crossed limb findings.'),
      ('Bilateral neuromuscular-junction weakness','The unilateral central pattern is more localizing here.')])
    slugs={1:'exam-general',2:'exam-cardiac',3:'exam-respiratory',4:'exam-abdominal',5:'exam-neurological',6:'exam-reasoning'}
    for order,b in sorted(banks.items()):finalize('Clinical Examination',order,b['document'],slugs[order],b['questions'],b['targetQuestions'])
    (ROOT/'clinical-examination-author-choice-review.json').write_text(json.dumps(dict(revisedQuestions=len(edits),ids=edits,review='Author revision; no independent clinician review'),indent=2),encoding='utf-8')
    print('Explicit distractor revisions:',len(edits))

if __name__=='__main__':review()
