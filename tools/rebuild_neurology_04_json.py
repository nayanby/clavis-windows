"""Coverage-driven headache and cranial neuralgia chapter; original educational MCQs."""
from pathlib import Path
import json
from qbank_json_chapters import question as Q, save, ROOT

R={
 'MWO':('ICHD-3: Migraine without aura','https://ichd-3.org/1-migraine/1-1-migraine-without-aura/'),
 'AURA':('ICHD-3: Migraine with aura','https://ichd-3.org/1-migraine/1-2-migraine-with-aura/'),
 'BRAIN':('ICHD-3: Migraine with brainstem aura','https://ichd-3.org/1-migraine/1-2-migraine-with-aura/1-2-2-migraine-with-brainstem-aura/'),
 'HEMI':('GeneReviews: Familial hemiplegic migraine','https://www.ncbi.nlm.nih.gov/books/NBK1388/'),
 'VEST':('ICHD-3 appendix: Vestibular migraine','https://ichd-3.org/appendix/a1-migraine/a1-6-episodic-syndromes-that-may-be-associated-with-migraine/a1-6-6-vestibular-migraine/'),
 'RET':('ICHD-3: Retinal migraine','https://ichd-3.org/1-migraine/1-2-migraine-with-aura/1-2-4-retinal-migraine/'),
 'STATUS':('ICHD-3: Status migrainosus','https://ichd-3.org/1-migraine/1-4-complications-of-migraine/1-4-1-status-migrainosus/'),
 'NICE':('NICE CG150: Headaches in over 12s, recommendations','https://www.nice.org.uk/guidance/cg150/chapter/Recommendations'),
 'AHS':('AHS position statement: CGRP therapies as first-line migraine prevention, 2024','https://doi.org/10.1111/head.14692'),
 'UBRO':('DailyMed: Ubrogepant prescribing information','https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=fd9f9458-fd96-4688-be3f-f77b3d1af6ab'),
 'LAS':('DailyMed: Lasmiditan prescribing information','https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aea3358c-ff41-4490-9e6d-c7bf7b3de13f'),
 'BOTOX':('DailyMed: OnabotulinumtoxinA, chronic migraine dosing','https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=33d066a9-34ff-4a1a-b38b-d10983df3300'),
 'MEC':('CDC US MEC 2024: Combined hormonal contraception and migraine','https://www.cdc.gov/contraception/hcp/usmec/combined-hormonal-contraceptives.html'),
 'CLUSTER':('ICHD-3: Cluster headache','https://ichd-3.org/3-trigeminal-autonomic-cephalalgias/3-1-cluster-headache/'),
 'EAN':('EAN cluster headache treatment guideline, 2023','https://doi.org/10.1111/ene.15956'),
 'DANISH':('Danish Headache Society reference programme, third edition, 2020','https://pmc.ncbi.nlm.nih.gov/articles/PMC8034101/'),
}
def S(h,main,*children):return(h,[(main,list(children))])
rows=[]
def add(*a,**kw):rows.append(Q(*a,**kw))

add('Migraine diagnosis and subtypes','Migraine Without Aura: Diagnostic Criteria',
 'An adult has six untreated attacks lasting 12–24 hours, with pulsating moderate-to-severe pain, worsening on climbing stairs, nausea and light sensitivity. Examination is normal between attacks. Which diagnosis best fits?',
 'Migraine without aura',[
 ('Episodic tension-type headache','Tension-type pain is more often pressing, less disabling and not aggravated by routine activity; nausea is also against its usual diagnostic pattern.'),
 ('Cluster headache','Cluster attacks are shorter, strictly unilateral orbital or temporal events with autonomic features or restlessness; the prolonged nausea-associated activity-aggravated attacks favor migraine.'),
 ('Paroxysmal hemicrania','This causes frequent much shorter unilateral autonomic attacks and requires an absolute indomethacin response; a 12–24-hour attack pattern does not fit.')],
 [S('Required Features','**ICHD-3 migraine without aura** requires at least five qualifying attacks lasting ==4–72 hours== untreated or unsuccessfully treated in adults.',
    'At least two pain features are required: unilateral location, pulsating quality, moderate or severe intensity, or aggravation by/avoidance of routine physical activity.',
    'During headache there must be nausea/vomiting or both photophobia and phonophobia. No better diagnosis should explain the presentation; unilateral pain is therefore not individually mandatory.'),
  S('Clinical Interpretation','**Diagnosis is clinical** when the pattern is typical and no secondary red flags are present.',
    'A headache diary records frequency, duration, associated features and acute-drug days. Fewer than five otherwise qualifying attacks can support probable migraine rather than a definite full-criteria diagnosis.',
    'Assess disability and acute-treatment response as well as frequency when planning prevention. New neurological deficits, a major pattern change or systemic illness require reassessment even in someone with a prior migraine diagnosis.')],['MWO','NICE'])

add('Migraine diagnosis and subtypes','Typical Migraine Aura',
 'Recurrent events begin with a shimmering visual arc that expands over 10 minutes, followed by tingling spreading from hand to face. Each symptom resolves within 40 minutes and headache follows. Which feature most strongly favors migraine aura over a typical TIA pattern?',
 'Gradual positive symptoms occurring in succession',[
 ('The presence of any sensory symptom','Both ischemia and migraine can produce sensory symptoms; the tempo, quality and sequential evolution are more informative than the sensory modality alone.'),
 ('Complete reversibility by itself','TIA is also transient and reversible by definition, so recovery alone cannot distinguish it from aura.'),
 ('Headache after the event by itself','Headache can accompany vascular events, and aura can occur without headache. A subsequent headache supports context but is not independently diagnostic.')],
 [S('Aura Framework','**Migraine with aura** requires at least two attacks of fully reversible qualifying neurological symptoms and at least three of six temporal or phenomenological features.',
    'The six features are gradual spread over at least 5 minutes, symptoms in succession, each individual symptom lasting 5–60 minutes, at least one unilateral symptom, at least one positive symptom, and headache accompanying or following within 60 minutes.',
    'Visual, sensory and speech/language symptoms are typical. Different sequential symptoms may make the total episode longer than one hour; motor aura has a different permitted duration.'),
  S('Differential Diagnosis','**Gradual spreading positive phenomena** favor aura but are not an absolute exclusion of ischemia or seizures.',
    'A first, atypical, abrupt or persistent deficit still merits urgent evaluation. Focal seizures are often briefer and highly stereotyped, while a typical TIA more often produces abrupt negative symptoms.',
    'Confirm whether a visual symptom is truly monocular or a homonymous hemifield phenomenon, because the diagnostic implications differ substantially.')],['AURA'])

add('Migraine diagnosis and subtypes','Migraine With Brainstem Aura',
 'Which fully reversible symptom combination can satisfy the additional brainstem-aura requirement when the remaining migraine-with-aura criteria are met?',
 'Dysarthria and true vertigo, without motor weakness or retinal symptoms',[
 ('Aphasia and unilateral arm weakness','Motor weakness places an otherwise qualifying migraine in the hemiplegic category; aphasia is a language symptom and is not interchangeable with brainstem dysarthria.'),
 ('Monocular visual loss and tinnitus','Retinal symptoms exclude the brainstem-aura subtype, and vascular causes of transient monocular loss require assessment.'),
 ('Lightheadedness and blurred vision alone','Nonspecific dizziness is not necessarily true vertigo, and blurred vision is not equivalent to diplopia; these descriptions alone do not establish two qualifying brainstem symptoms.')],
 [S('Subtype Criteria','**Brainstem aura** requires at least two fully reversible brainstem symptoms and no motor or retinal symptoms.',
    'Qualifying features include dysarthria, vertigo, tinnitus, hypacusis, diplopia, ataxia not attributable to sensory loss, and decreased level of consciousness. The overall migraine-with-aura requirements also apply.',
    'Dysarthria differs from aphasia; vertigo differs from nonspecific dizziness; diplopia differs from nonspecific blurred vision. Precise symptom description prevents overdiagnosis.'),
  S('Important Exclusions','**New posterior-circulation symptoms** must not be presumed migrainous merely because headache is present.',
    'Consider ischemia, dissection, seizures, drug effects and other brainstem processes, especially with abrupt onset, vascular risks or persistent findings. “Basilar migraine” is an older term that can misleadingly imply demonstrated basilar-artery pathology.',
    'Motor weakness redirects classification toward hemiplegic migraine after appropriate exclusion of acute vascular disease; it should not simply be added to the brainstem-aura checklist.')],['BRAIN','AURA'],style='direct')

add('Migraine diagnosis and subtypes','Familial Hemiplegic Migraine Genetics',
 'An adolescent has recurrent migraine aura with fully reversible unilateral weakness; a parent has similar attacks. Which gene–protein association is characteristic of familial hemiplegic migraine type 1?',
 'CACNA1A: P/Q-type voltage-gated calcium channel',[
 ('ATP1A2: neuronal voltage-gated sodium channel','ATP1A2 is a genuine hemiplegic-migraine gene, but encodes the alpha-2 subunit of Na+/K+-ATPase, not the sodium channel proposed.'),
 ('SCN1A: Na+/K+-ATPase alpha-2 subunit','SCN1A is associated with type 3 and encodes a voltage-gated sodium channel; the protein assignment here belongs to ATP1A2.'),
 ('KCNQ2: P/Q-type voltage-gated calcium channel','KCNQ2 encodes a potassium-channel subunit associated with important epilepsy phenotypes; it is not the classic type-1 hemiplegic migraine calcium-channel gene.')],
 [S('Phenotype and Inheritance','**Hemiplegic migraine** includes fully reversible motor weakness together with reversible visual, sensory or speech/language aura.',
    'A first- or second-degree relative with qualifying hemiplegic migraine supports the familial form. A similar phenotype without that family history is classified as sporadic, and a pathogenic variant is not found in every patient.',
    'CACNA1A, ATP1A2 and SCN1A are the classical type 1, 2 and 3 associations; broader genetic evaluation may be appropriate for selected atypical or severe phenotypes.'),
  S('Diagnostic Limits','**A genetic association does not excuse acute stroke assessment** when weakness is new, abrupt or atypical.',
    'Motor symptoms often last longer than typical visual or sensory aura and can persist up to 72 hours or occasionally longer. Associated ataxia or other neurological features may suggest a particular channelopathy.',
    'Genetic testing should be clinically interpreted and paired with counseling; variants of uncertain significance do not independently confirm the diagnosis or establish treatment efficacy.')],['HEMI','AURA'],table=(['Classic subtype','Gene','Protein'],[['Type 1','CACNA1A','P/Q-type calcium channel'],['Type 2','ATP1A2','Na+/K+-ATPase alpha-2'],['Type 3','SCN1A','Voltage-gated sodium channel']]))

add('Migraine diagnosis and subtypes','Vestibular Migraine',
 'A patient with a migraine history has eight moderate-to-severe vertigo episodes lasting 20 minutes to 6 hours. Five include photophobia and phonophobia or a characteristic migraine headache. No better vestibular cause is found. Which diagnosis fits best?',
 'Vestibular migraine',[
 ('Definite Ménière disease','Ménière disease requires its characteristic auditory and audiometric context; migraine-linked recurrent vestibular episodes without documented fluctuating low-frequency hearing loss favor vestibular migraine here.'),
 ('Benign paroxysmal positional vertigo','BPPV produces brief position-triggered attacks with characteristic positional nystagmus, rather than the described prolonged spontaneous episodes associated with migrainous features.'),
 ('Vestibular neuritis','This usually causes a single acute sustained vestibular syndrome lasting days, not recurring separated episodes with migraine associations over time.')],
 [S('Diagnostic Requirements','**Vestibular migraine** requires at least five episodes of moderate or severe vestibular symptoms lasting ==5 minutes to 72 hours==.',
    'There must be a current or previous migraine history and migrainous features during at least half of the vestibular episodes: a qualifying migraine headache, photophobia with phonophobia, or visual aura.',
    'Symptoms should not be better explained by another headache or vestibular disorder. Headache need not accompany every vertigo episode.'),
  S('Practical Assessment','**History and vestibular examination** distinguish recurrent syndromes more reliably than an isolated normal MRI.',
    'Review positional triggers, hearing changes, tinnitus, duration, neurological symptoms and orthostatic symptoms. Audiometry is important when Ménière disease is suspected, and both disorders can coexist.',
    'A new acute continuous vestibular syndrome, severe gait failure or focal signs requires assessment for posterior-circulation ischemia. A prior migraine label should not automatically classify every episode of dizziness.')],['VEST'])

add('Migraine diagnosis and subtypes','Retinal Migraine Is a Diagnosis of Exclusion',
 'A 58-year-old smoker describes a first episode of a dark curtain over one eye lasting 12 minutes, followed by headache. Which approach is most appropriate?',
 'Urgently evaluate retinal ischemia and other causes of transient monocular visual loss',[
 ('Diagnose retinal migraine from the subsequent headache alone','Retinal migraine is rare and requires exclusion of other causes of amaurosis fugax; a first negative monocular event in a vascular-risk patient cannot be assigned from headache timing alone.'),
 ('Classify the event as typical binocular visual aura without clarifying laterality','Patients can misdescribe a hemifield defect as monocular, but a truly monocular curtain suggests the retina or optic nerve and requires specific evaluation.'),
 ('Defer vascular assessment until a permanent field defect develops','Transient retinal ischemia is itself a warning event. Waiting for irreversible loss forfeits an opportunity to identify treatable carotid, cardiac or inflammatory disease.')],
 [S('Visual Localization','**True monocular visual loss** localizes anterior to the chiasm and requires a retinal or optic-nerve differential.',
    'Ask whether the patient covered each eye during the episode and use a drawing or field description if needed. Typical cortical visual aura often affects corresponding visual fields of both eyes.',
    'Assess retinal embolism, carotid or cardiac sources and, in an appropriate older patient, giant-cell arteritis. Sudden negative visual loss differs from a slowly expanding scintillating cortical phenomenon.'),
  S('Retinal Migraine Criteria','**Retinal migraine** involves repeated fully reversible monocular phenomena with an appropriate aura-like time course after exclusion of other causes.',
    'ICHD-3 requires confirmation of monocular involvement and at least two features among gradual spread over at least 5 minutes, duration 5–60 minutes, and headache accompanying or following within 60 minutes.',
    'A subsequent headache does not exclude ischemia. Diagnostic caution matters because the rare migraine label and retinal TIA imply different prevention and follow-up strategies.')],['RET'])

add('Migraine diagnosis and subtypes','Status Migrainosus',
 'A patient with established migraine has an otherwise typical but continuously disabling attack for 90 hours. There is no secondary cause or medication-overuse pattern. Which complication best fits?',
 'Status migrainosus',[
 ('Chronic migraine','Chronic migraine is defined by headache-day frequency over more than three months; one prolonged attack does not establish that longitudinal pattern.'),
 ('Persistent aura without infarction','This refers to prolonged aura symptoms, typically at least a week with no infarction, rather than a 90-hour disabling headache without persistent aura.'),
 ('New daily persistent headache','NDPH requires a clearly remembered onset with headache becoming continuous and unremitting within 24 hours and persisting over three months; this established migraine attack has a different context and duration.')],
 [S('Definition','**Status migrainosus** is a debilitating migraine attack lasting ==more than 72 hours== in a patient with migraine, typical of prior attacks except duration and severity.',
    'Remissions of up to 12 hours due to sleep or medication are allowed in the classification. Exclude a secondary cause and assess whether medication-overuse headache better explains the presentation.',
    'When the pattern fulfills medication-overuse headache criteria, ICHD-3 directs coding the overuse disorder and relevant migraine rather than automatically adding status migrainosus.'),
  S('Management Priorities','**Reassess diagnosis and hydration**, especially with vomiting, dehydration or a changed examination.',
    'Use a clinician-supervised nonoral rescue strategy when oral treatment has failed, considering an antiemetic and an appropriate NSAID, migraine-specific agent or other specialist rescue. Avoid routine opioid escalation.',
    'There is no single universally proven rescue regimen for every status episode. Screen for contraindications, repeated acute-drug exposure and preventive needs while investigating any new red flags.')],['STATUS','NICE'])

add('Acute migraine therapy','Combining a Triptan With an NSAID',
 'Oral sumatriptan gives partial relief of an established migraine, but pain recurs later. The patient has no cardiovascular, gastrointestinal or renal contraindication. Which strategy is supported for future attacks?',
 'Use an oral triptan with an NSAID such as naproxen',[
 ('Add a second different triptan simultaneously to the first','Combining different triptans within the restricted interval is not the standard strategy; a triptan–NSAID combination targets complementary mechanisms without that same-class exposure.'),
 ('Use a long-acting opioid instead of optimizing migraine-specific therapy','Opioids are not preferred routine migraine treatment and introduce dependence and medication-overuse risk when evidence-based migraine strategies remain available.'),
 ('Replace acute treatment with a one-time dose of a preventive CGRP antibody','Preventive antibodies are not immediate attack-abortion drugs; a preventive plan may be needed, but it does not replace an effective acute rescue regimen.')],
 [S('Rationale and Dosing','**A triptan–NSAID combination** can improve sustained relief when a triptan alone is inadequate or recurrence occurs.',
    'A common adult regimen uses sumatriptan 50–100 mg orally with naproxen 500 mg; available fixed combinations and local labels differ. Treat early in the headache phase when appropriate rather than repeatedly waiting for maximal pain.',
    'NICE supports an oral triptan with an NSAID, or with paracetamol when more suitable, while considering patient preference and risks.'),
  S('Safety and Follow-Up','**Triptans activate 5-HT1B/1D receptors** and require assessment of cardiovascular and cerebrovascular contraindications.',
    'Check the NSAID’s renal, ulcer, bleeding and pregnancy risks. Respect product-specific repeat-dose limits and intervals and avoid triptan–ergot or different-triptan stacking within prohibited periods.',
    'Track acute-treatment days and disability. Frequent recurrence may justify a different triptan, nonoral formulation or preventive treatment rather than increasing acute exposure indefinitely.')],['NICE'])

add('Acute migraine therapy','Nonoral Treatment for Vomiting',
 'A patient with established migraine vomits early in each severe attack and cannot retain tablets. There are no triptan contraindications. Which listed option best addresses the delivery problem?',
 'Subcutaneous sumatriptan',[
 ('Oral sumatriptan with an extra glass of water','Oral treatment remains vulnerable to vomiting and delayed gastric absorption; changing the amount of water does not solve the stated route limitation.'),
 ('Orally disintegrating rizatriptan as proof that gastrointestinal absorption is bypassed','A dissolving tablet improves swallowing convenience but most drug is still absorbed through the gastrointestinal tract; it is not equivalent to injection for persistent vomiting.'),
 ('Oral delayed-release naproxen as the fastest available rescue','Delayed-release oral delivery is poorly matched to rapid severe symptoms with vomiting and does not bypass unreliable gastrointestinal uptake.')],
 [S('Route Selection','**Subcutaneous sumatriptan** provides rapid migraine-specific delivery without dependence on gastric retention.',
    'A usual adult dose is ==6 mg subcutaneously==; lower-dose products exist. Product instructions commonly permit a repeat after at least one hour, with a usual maximum of 12 mg in 24 hours for the 6-mg regimen.',
    'An intranasal migraine-specific drug or nonoral NSAID/antiemetic may be alternatives depending on availability and clinical setting.'),
  S('Treatment Context','**Vomiting and migraine-related gastric stasis** can make an otherwise appropriate oral agent appear ineffective.',
    'Assess hydration and use an antiemetic when appropriate; metoclopramide or prochlorperazine can have their own contraindications and extrapyramidal adverse effects. Recurrent severe vomiting also warrants diagnostic review if the pattern changes.',
    'A nonoral route does not remove triptan vascular contraindications, interaction restrictions or daily dose limits. Review preventive needs when severe attacks are frequent rather than repeatedly escalating injections alone.')],['NICE','DANISH'])

add('Acute migraine therapy','Acute Migraine With Coronary Disease',
 'A patient with stable established coronary artery disease needs an acute migraine-specific oral option. Which listed agent avoids the direct vasoconstrictor mechanism of triptans and ergots?',
 'Ubrogepant',[
 ('Sumatriptan','Sumatriptan acts at 5-HT1B/1D receptors and has vascular contraindications in established coronary disease; oral delivery does not remove that concern.'),
 ('Rizatriptan','This is another triptan with the same relevant vascular limitation; choosing a different member does not make a coronary contraindication disappear.'),
 ('Dihydroergotamine','Ergot pharmacology can produce vasoconstriction and is not the nonvasoconstrictive alternative requested for this coronary-disease context.')],
 [S('Mechanism and Regimen','**Ubrogepant** is a small-molecule CGRP-receptor antagonist for acute migraine treatment.',
    'The labeled adult oral dose is ==50 or 100 mg==; a second dose may be taken at least 2 hours later when permitted, up to 200 mg in 24 hours. It is not the same as the preventive antibody dosing schedule.',
    'Gepants lack the direct 5-HT1B vasoconstrictor mechanism that limits triptans; this does not mean every vascular condition or interaction has been studied without uncertainty.'),
  S('Contraindications and Monitoring','**CYP3A4 interactions** and renal or hepatic function affect safe prescribing.',
    'Strong CYP3A4 inhibitors are contraindicated with ubrogepant, and strong inducers should be avoided. Dose or repeat-dose restrictions apply with certain moderate inhibitors and organ impairment.',
    'Recognize hypersensitivity and current warnings including hypertension or Raynaud-related symptoms. A nonvasoconstrictive mechanism should not be described as freedom from all cardiovascular monitoring or from medication-specific precautions.')],['UBRO'])

add('Acute migraine therapy','Lasmiditan and Driving',
 'A patient uses lasmiditan for migraine and feels subjectively normal after two hours. What minimum post-dose driving restriction should be explained under the product labeling?',
 'At least 8 hours after each dose',[
 ('Only until headache pain resolves','Driving impairment is a drug effect that can persist independently of pain relief; headache resolution does not establish safe psychomotor performance.'),
 ('Two hours, provided the patient does not feel sleepy','Subjective alertness does not reliably exclude the impairment demonstrated in driving studies; the label specifies a longer minimum interval.'),
 ('Four hours if no alcohol was taken','Avoiding alcohol is sensible but does not replace the eight-hour restriction; the label does not provide a four-hour exception based on alcohol abstinence.')],
 [S('Mechanism and Precaution','**Lasmiditan** is a 5-HT1F receptor agonist, distinct from the vasoconstrictor 5-HT1B/1D triptan mechanism.',
    'It can cause dizziness, sedation and impaired driving. Advise no driving or operating machinery for ==at least 8 hours after each dose==, even if the patient believes alertness has returned.',
    'A person unable to comply with that interval should choose a different appropriate acute strategy rather than assume that a small dose abolishes the restriction.'),
  S('Dosing and Interactions','**The adult dose** is 50, 100 or 200 mg orally as selected, with no more than one dose in 24 hours under the label.',
    'CNS depressants may add impairment, and serotonergic co-medication warrants attention to serotonin-syndrome risk. The medication is an acute treatment rather than routine daily prevention.',
    'Contrast gepants, which target the CGRP receptor, with this serotonergic agent. Both expand nontriptan options, but their adverse effects, interactions and repeat-dose rules are not interchangeable.')],['LAS'],style='direct')

add('Migraine prevention and counseling','Comorbidity-Based Selection of Prevention',
 'A woman beyond childbearing potential has frequent disabling migraine, obesity and asthma. She has no stone history or cognitive complaints and wants an oral preventive. Which listed option best fits these comorbidities?',
 'Topiramate',[
 ('Propranolol','It is an effective migraine preventive but nonselective beta blockade can worsen asthma, making it less attractive in this specific comparison.'),
 ('Sodium valproate','It can prevent migraine but often causes weight gain and has important reproductive and systemic risks; the obesity concern favors the alternative offered.'),
 ('Amitriptyline','It can be useful when insomnia or another indication favors it, but weight gain and sedation can conflict with this patient’s priorities.')],
 [S('Choosing an Oral Preventive','**Topiramate** can reduce migraine frequency and often promotes weight loss, making it a reasonable offered option here.',
    'Start low, commonly 25 mg at night, and titrate gradually; a common target is ==50 mg twice daily== if effective and tolerated. The individual may benefit at a lower dose.',
    'Asthma, weight, sleep, mood, cardiac disease, pregnancy potential and patient preference should influence preventive selection rather than using the same first drug for everyone.'),
  S('Adverse Effects and Follow-Up','**Paresthesia, cognitive slowing and word-finding difficulty** can limit topiramate even when headaches improve.',
    'Assess bicarbonate, renal risk and history of nephrolithiasis; carbonic-anhydrase inhibition can produce non-anion-gap acidosis and stones. Acute painful blurred vision can signal secondary angle closure.',
    'Pregnancy carries fetal risks and jurisdiction-specific prevention requirements. The stem removes childbearing potential, but that does not erase the need to counsel other patients. Reassess benefit and tolerability after an adequate titrated trial using a headache diary.')],['NICE','DANISH'])

add('Migraine prevention and counseling','Amitriptyline With Sleep Disturbance',
 'An adult with migraine needs prevention and has troublesome insomnia. There is no obesity, urinary retention, glaucoma, conduction disease or overdose risk. Which listed preventive may address both concerns?',
 'Amitriptyline at a low bedtime starting dose',[
 ('Topiramate solely for its sedative effect','Topiramate is effective prevention but is not selected principally as a sleep treatment and may cause cognitive or sensory adverse effects; it does not match the stated dual target as well.'),
 ('Propranolol as a specific treatment for insomnia','Propranolol can prevent migraine but does not specifically treat insomnia and can disturb sleep in some patients; another comorbidity might instead favor it.'),
 ('Candesartan as a primary hypnotic','Candesartan can be useful for migraine and hypertension, but it is not a hypnotic; its blood-pressure effect would matter more if hypertension were the target comorbidity.')],
 [S('Dual-Purpose Selection','**Amitriptyline** is an oral preventive option when its sedating properties are useful rather than problematic.',
    'A common starting dose is ==10 mg at night==, gradually increased according to benefit and tolerance, often within a low-dose range of 10–50 mg nightly for headache prevention. This differs from an automatic antidepressant-dose prescription.',
    'Sleep hygiene and assessment of the cause of insomnia remain appropriate; a drug that causes drowsiness does not treat every sleep disorder.'),
  S('Safety Screening','**Anticholinergic and cardiac effects** guide suitability.',
    'Dry mouth, constipation, urinary retention, weight gain and orthostatic symptoms can occur. Use caution with conduction disease, relevant glaucoma, interacting drugs and substantial overdose risk, and consider ECG assessment when clinically indicated.',
    'Assess headache days, function and adverse effects after titration. If insomnia improves but migraine remains disabling, reconsider the preventive plan rather than escalating indefinitely on the assumption that more sedation means better migraine control.')],['NICE','DANISH'])

add('Migraine prevention and counseling','CGRP Therapies as a First-Line Option',
 'Which statement accurately reflects the American Headache Society 2024 position on CGRP-targeting migraine prevention?',
 'It can be a first-line option without a requirement to fail other preventive classes first',[
 ('It requires failure of at least two oral classes as a universal clinical prerequisite','That reflects older positioning or some reimbursement rules, rather than the AHS 2024 clinical position statement.'),
 ('It is recommended only for chronic migraine after botulinum toxin failure','CGRP therapies have evidence in episodic as well as chronic migraine; a mandatory prior botulinum trial is not the stated universal clinical requirement.'),
 ('It replaces assessment of migraine frequency, disability and patient preference','First-line status expands choice but does not eliminate individualized indication, safety, access and preference assessment.')],
 [S('Updated Position','**AHS 2024** considers CGRP-targeting treatments alongside established first-line migraine preventives without requiring previous class failures.',
    'The category includes ligand- or receptor-targeting antibodies and preventive gepants with their specific indications. An acute-only gepant should not be assumed to have the same preventive authorization.',
    'A clinical position statement is different from a payer’s step-therapy rule or a national cost-effectiveness pathway; those may still impose access criteria.'),
  S('Individualized Prevention','**Shared selection** weighs burden, likely benefit, adverse effects, interactions, administration route, pregnancy plans and affordability.',
    'Oral agents remain reasonable when a comorbidity favors them or cost and preference make them suitable. First-line status does not mean every patient must receive the newest drug.',
    'Use baseline headache and migraine-day records and functional goals to assess response. Review adverse effects and current product guidance rather than extrapolating safety across every agent or special population.')],['AHS'],style='direct')

add('Migraine prevention and counseling','CGRP Receptor Versus Ligand Antibodies',
 'Which preventive monoclonal antibody targets the CGRP receptor rather than the CGRP ligand?',
 'Erenumab',[
 ('Fremanezumab','Fremanezumab binds the CGRP ligand. It shares the broad therapeutic pathway but not erenumab’s receptor-directed target.'),
 ('Galcanezumab','Galcanezumab binds the ligand, not the receptor. Its dosing and some indications also differ, so the products are not automatically interchangeable.'),
 ('Eptinezumab','Eptinezumab is an IV ligand-binding antibody; its route distinguishes it further, but it is not the receptor-targeting antibody requested.')],
 [S('Mechanistic Comparison','**Erenumab** blocks the CGRP receptor; fremanezumab, galcanezumab and eptinezumab bind the peptide ligand.',
    'Both strategies interfere with CGRP signaling involved in migraine. Erenumab is administered subcutaneously, commonly ==70 mg monthly==, with 140 mg monthly used in selected patients according to labeling.',
    'These antibodies are prevention therapies, not substitutes for an immediate acute rescue dose during an attack.'),
  S('Safety and Selection','**Constipation** is a notable erenumab adverse effect and can occasionally be serious.',
    'Review bowel history, interacting constipating drugs and symptoms of obstruction. Hypertension and Raynaud-related symptoms are relevant current warnings, so assess vascular symptoms and pressure rather than assuming the pathway is risk free.',
    'Hypersensitivity, pregnancy uncertainty and long biological persistence affect counseling. A patient intolerant of one product may have other options, but changing receptor to ligand targeting does not guarantee either efficacy or absence of shared pathway-related risks.')],['AHS'],table=(['Agent','Target','Route'],[['Erenumab','CGRP receptor','Subcutaneous'],['Fremanezumab','CGRP ligand','Subcutaneous'],['Galcanezumab','CGRP ligand','Subcutaneous'],['Eptinezumab','CGRP ligand','Intravenous']]),style='direct')

add('Migraine prevention and counseling','OnabotulinumtoxinA for Chronic Migraine',
 'A patient with chronic migraine is selected for onabotulinumtoxinA. Which regimen matches the standard fixed-site labeled protocol?',
 '155 units across 31 head and neck sites, repeated every 12 weeks',[
 ('155 units across 31 sites every 4 weeks','The dose and sites resemble the protocol, but a four-week routine interval is not the standard chronic-migraine retreatment schedule.'),
 ('50 units confined to the forehead every 12 weeks','A forehead-only cosmetic-style approach does not reproduce the validated multi-muscle chronic-migraine injection pattern or total dose.'),
 ('300 units intramuscularly at one temporal site every 12 weeks','Units must be distributed according to the protocol; concentrating a different total at one site is neither the labeled regimen nor equivalent treatment.')],
 [S('Protocol and Population','**OnabotulinumtoxinA** has established preventive use in chronic migraine, rather than routine extrapolation to every episodic headache.',
    'The labeled fixed-site regimen is ==155 units in 31 sites every 12 weeks== across specified head and neck muscles. PREEMPT-derived practice in some settings uses an additional follow-the-pain component up to 195 units in 39 sites.',
    'Product units are formulation-specific and should not be converted one-for-one to another botulinum toxin preparation.'),
  S('Monitoring and Response','**Neck pain, focal weakness and ptosis** are relevant adverse effects; injection technique and anatomical targeting matter.',
    'Assess baseline headache burden, medication overuse, functional goals and response across an adequate supervised trial. One incompletely observed cycle should not automatically establish failure.',
    'Avoid injection through local infection and review neuromuscular disease and interacting drugs that can enhance weakness. A planned preventive procedure still needs a separate acute-treatment plan for breakthrough attacks.')],['BOTOX','NICE'],style='direct')

add('Migraine prevention and counseling','Migraine Aura and Estrogen-Containing Contraception',
 'A 29-year-old with confirmed migraine with aura seeks contraception. Under CDC US MEC 2024, which approach is most appropriate?',
 'Choose a suitable progestin-only or nonhormonal method rather than combined hormonal contraception',[
 ('Use a combined pill because age below 35 removes the aura-related concern','The aura-related combined-hormonal category is not removed by young age; age and smoking are additional risk considerations rather than a waiver.'),
 ('Use a combined vaginal ring because nonoral estrogen avoids the classification','The combined hormonal category includes pills, patches and rings; changing delivery route does not remove the aura-related recommendation.'),
 ('Use a combined patch because no headache occurs during most auras','Aura can occur without headache, and the classification depends on accurately identified aura history rather than whether every aura is painful.')],
 [S('Eligibility Framework','**Migraine with aura** is category ==4== for combined hormonal contraception under US MEC 2024, indicating an unacceptable health risk.',
    'Accurate aura identification matters; nonspecific blurred vision or premonitory fatigue should not automatically be labeled aura. A new or markedly changed headache pattern needs evaluation.',
    'Without aura, the combined-hormonal assessment differs and additional stroke-risk factors affect suitability.'),
  S('Alternative Selection','**Progestin-only and nonhormonal methods** provide alternatives without the same estrogen-related classification.',
    'Select the specific method after reviewing the patient’s other medical conditions, preference, bleeding goals and interacting medicines. Enzyme-inducing drugs can alter the effectiveness of some hormonal methods.',
    'Explain that the recommendation concerns prevention of serious vascular harm rather than a claim that all hormones worsen headaches. Menstrual migraine management and contraception should be coordinated, but improved headache control does not override the aura-related eligibility category.')],['MEC'])

add('Chronic headache and medication overuse','Chronic Migraine Thresholds',
 'For 5 months, a patient with established migraine has 18 headache days each month. Nine have migraine features; the rest feel like mild bilateral pressure. There is no medication overuse or secondary cause. What is the best classification?',
 'Chronic migraine',[
 ('Frequent episodic migraine because only nine days are migrainous','Chronic migraine counts total headache days, including tension-type-like days, provided the required subset has migraine features; the remaining pressure days do not make it episodic.'),
 ('Chronic tension-type headache as the sole diagnosis','The sufficient number of migraine-feature days favors chronic migraine under ICHD-3 rather than assigning only a tension-type label.'),
 ('Status migrainosus','Status is a single debilitating prolonged attack over 72 hours; this longitudinal high-frequency pattern is a different classification problem.')],
 [S('Diagnostic Thresholds','**Chronic migraine** requires headache on ==at least 15 days/month for more than 3 months== in an appropriate migraine-history context.',
    'On at least ==8 days/month== there must be qualifying migraine features or another permitted migraine-specific criterion, including attacks the patient recognizes as migraine that are relieved by a triptan or ergot.',
    'Not every headache day must look classically migrainous, and the phenotype may vary within or between days.'),
  S('Diary and Co-Diagnosis','**A daily record** is particularly useful for distinguishing total headache days, migraine days and acute-drug days.',
    'Evaluate overuse and secondary causes. If medication-overuse headache criteria are also met, ICHD-3 permits both diagnoses; improvement after withdrawal can clarify the ongoing frequency pattern.',
    'Prevention and acute-treatment limits should address the full burden and disability. Do not equate a high number of tablets with a high number of medication-use days, because overuse classification is based on days of exposure.')],['NICE'])

add('Chronic headache and medication overuse','Medication-Overuse Headache Thresholds',
 'A patient with pre-existing migraine now has 22 headache days per month and uses sumatriptan on 12 days each month for 4 months. Which interpretation is correct?',
 'The exposure meets the triptan-overuse threshold in a medication-overuse headache assessment',[
 ('The threshold is not reached until triptan use occurs on 15 days per month','The 15-day threshold applies to simple nonopioid analgesics, not the usual 10-day triptan threshold.'),
 ('Only the number of tablets matters, not the number of treatment days','Overuse criteria are defined using treatment days per month. Repeated doses on the same day and doses on separate days have different counting implications.'),
 ('Medication-overuse headache cannot be diagnosed until improvement after withdrawal is proven','ICHD-3 does not require waiting for a successful withdrawal response to diagnose a qualifying current pattern; reassessment after withdrawal remains useful.')],
 [S('Class-Specific Exposure','**MOH** requires headache on at least 15 days/month in a person with a pre-existing headache disorder and regular overuse for more than three months.',
    'Triptans, ergots, opioids and combination analgesics generally use a ==10 or more days/month== threshold. Simple analgesics such as paracetamol or NSAIDs generally use ==15 or more days/month==.',
    'Multiple acute classes can create a combined-overuse pattern even when a single drug’s use is below its own separate threshold; assess the complete medication history.'),
  S('Treatment Implications','**Explain the cycle and plan withdrawal or reduction**, together with an appropriate preventive strategy.',
    'Temporary worsening can occur. The withdrawal method depends on the drug: opioid or barbiturate dependence requires a different plan from uncomplicated triptan overuse.',
    'The diagnostic thresholds are not a promise of safety just below the cut-off. Individual susceptibility varies, so practical acute-use counseling and follow-up should begin before chronic daily headache develops.')],['NICE'],table=(['Acute medication class','Typical overuse threshold','Duration'],[['Triptan, ergot, opioid, combination analgesic','≥10 days/month','>3 months'],['Paracetamol or NSAID class','≥15 days/month','>3 months']]))

add('Chronic headache and medication overuse','Withdrawal Strategy in Medication Overuse',
 'A patient with uncomplicated triptan-overuse headache wants to stop the overused drug. There is no opioid or barbiturate use, major psychiatric instability or previous failed withdrawal. Which plan is most appropriate?',
 'A planned abrupt triptan withdrawal with support and preventive treatment as appropriate',[
 ('Use a long-acting opioid to replace the triptan every day','This transfers the patient to another high-risk acute-drug class and introduces dependence rather than correcting the overuse pattern.'),
 ('Continue the same triptan frequency until preventive therapy guarantees complete relief','Prevention can begin alongside withdrawal, but waiting for guaranteed freedom from headache can indefinitely preserve the overuse cycle.'),
 ('Require inpatient detoxification for every uncomplicated triptan-overuse case','Admission is appropriate for selected complex or high-risk cases, but most uncomplicated triptan withdrawal can be managed with a structured outpatient plan.')],
 [S('Uncomplicated Withdrawal','**Abrupt cessation** is commonly used for triptan and simple-analgesic overuse, with clear preparation and follow-up.',
    'Explain that headache, nausea or other withdrawal symptoms may worsen temporarily before improving. Provide practical support and a limited alternative rescue plan when needed without recreating daily acute exposure.',
    'Preventive therapy for the underlying migraine can be started or optimized during the withdrawal strategy rather than omitted until the entire process is complete.'),
  S('When the Plan Changes','**Opioids, barbiturates and sedative dependence** may require gradual reduction, monitoring and specialist or inpatient care.',
    'Comorbidity, major psychiatric illness, other chronic pain, prior failures or a safety concern can also justify referral or a more intensive setting. Do not apply the abrupt-triptan rule indiscriminately to dependence-forming drugs.',
    'Use a diary and early review to assess adherence, persistent headache burden and relapse risk. Education should avoid blame: the treatment plan must make repeated overuse less necessary as well as ask the patient to stop it.')],['NICE','DANISH'])

add('Chronic headache and medication overuse','Chronic Tension-Type Headache',
 'A patient has gradually evolved bilateral pressing headache on 20 days/month for 6 months. It is mild to moderate, not aggravated by activity, with no vomiting and only occasional phonophobia. There are no migraine-feature days or secondary red flags. What is most likely?',
 'Chronic tension-type headache',[
 ('Chronic migraine','Chronic migraine requires a sufficient subset of migraine-feature days or other qualifying migraine criteria; these are absent in the described longitudinal history.'),
 ('New daily persistent headache','NDPH begins on a clearly remembered day and becomes continuous within 24 hours; this patient’s frequency increased gradually.'),
 ('Hemicrania continua','This is a strictly unilateral continuous headache with exacerbations and an absolute indomethacin response; bilateral pressing pain without that pattern is different.')],
 [S('Clinical Pattern','**Chronic tension-type headache** occurs on at least 15 days/month for more than three months, lasting hours to days or continuously.',
    'At least two characteristics include bilateral location, pressing/tightening quality, mild-to-moderate intensity and no aggravation by routine activity. There is no more than one of photophobia, phonophobia or mild nausea, and no moderate/severe nausea or vomiting.',
    'A remembered abrupt daily onset instead raises NDPH, while enough migraine-feature days changes classification toward chronic migraine.'),
  S('Management','**Prevention and nonpharmacological care** reduce the need for frequent analgesics.',
    'Amitriptyline can be used, commonly starting at 10 mg at bedtime and titrating according to response and tolerability; assess anticholinergic, orthostatic and cardiac risks. Sleep, stress, physical activity and relevant musculoskeletal factors also deserve attention.',
    'Limit acute analgesic exposure and assess overuse. The term tension-type does not prove that a headache is caused solely by stress, posture or muscle contraction; new red flags still require evaluation.')],['DANISH','NICE'])

add('Trigeminal autonomic cephalalgias','Cluster Headache Attack Pattern',
 'A patient has repeated strictly unilateral orbital attacks lasting 60 minutes, twice daily for several weeks, with tearing, nasal congestion and pacing during pain. Which diagnosis best fits?',
 'Cluster headache',[
 ('Migraine without aura','Migraine usually lasts longer and patients often avoid movement; brief repeated orbital attacks with marked restlessness and ipsilateral autonomic signs favor cluster.'),
 ('Paroxysmal hemicrania','Its attacks typically last 2–30 minutes and occur more than five times daily, with an absolute indomethacin response; the hour-long twice-daily pattern is more typical of cluster.'),
 ('SUNCT','SUNCT attacks are much shorter, usually seconds to minutes within the 1–600-second framework; a continuous hour-long attack is outside its characteristic range.')],
 [S('Diagnostic Framework','**Cluster headache** requires at least five severe or very severe unilateral orbital, supraorbital or temporal attacks lasting ==15–180 minutes== untreated.',
    'There must be ipsilateral cranial autonomic features or restlessness/agitation, with frequency usually from one every other day to eight daily during active periods. Tearing, conjunctival injection, nasal symptoms, eyelid edema, sweating, miosis or ptosis may occur.',
    'The pattern must not be better explained by another disorder; the characteristic syndrome is more than unilateral pain plus a watery eye.'),
  S('Clinical Assessment','**Circadian timing and clustering** support recognition, while restlessness helps distinguish many attacks from migraine.',
    'Migraine can also produce autonomic symptoms, so duration and longitudinal pattern matter. Evaluate a first or atypical TAC presentation for secondary causes with appropriate imaging and examination.',
    'Acute treatment and prevention are separate needs: rapid oxygen or an appropriate rapid triptan can stop attacks, while preventive therapy reduces recurrence through the bout.')],['CLUSTER','EAN'])

add('Trigeminal autonomic cephalalgias','Episodic Versus Chronic Cluster Headache',
 'Qualifying cluster attacks have continued for 18 months, with the longest remission lasting 6 weeks. Which subtype is most appropriate?',
 'Chronic cluster headache',[
 ('Episodic cluster headache','Episodic cluster requires qualifying bouts separated by remissions of at least three months; six weeks does not meet that remission criterion.'),
 ('Chronic paroxysmal hemicrania','The episodic/chronic time course does not change an established cluster attack phenotype into paroxysmal hemicrania, which has different attack duration, frequency and indomethacin criteria.'),
 ('Chronic migraine','Frequent headache alone does not establish chronic migraine when the recurring attacks fulfill the cluster phenotype; headache type and remission pattern must both be considered.')],
 [S('Current Remission Cut-Off','**Chronic cluster headache** has attacks for at least one year without remission or with remissions lasting less than ==3 months==.',
    'Episodic cluster has at least two bouts lasting 7 days to one year when untreated, separated by pain-free remissions of at least three months. Older references using a one-month remission threshold should not be applied to current ICHD-3 classification.',
    'A six-week gap therefore does not make this 18-month pattern episodic.'),
  S('Why the Distinction Matters','**Treatment duration and evidence** can differ between episodic and chronic disease.',
    'Patients with chronic attacks may need sustained prevention and more frequent reassessment of adverse effects, whereas a bout-limited plan may be suitable in episodic disease. Some newer preventive evidence is subtype specific.',
    'Keep an attack diary and reassess subtype over time. A change in pain character, new persistent neurological signs or a marked change in the established pattern still warrants secondary-cause evaluation rather than attribution to chronicity alone.')],['CLUSTER','EAN'])

add('Trigeminal autonomic cephalalgias','Oxygen Delivery for Acute Cluster Headache',
 'Which oxygen prescription best matches guideline-supported acute cluster-headache treatment?',
 '100% oxygen through a nonrebreather mask at at least 12 L/min for about 15–20 minutes',[
 ('Oxygen at 2 L/min through nasal cannulae for 20 minutes','This low-flow approach is used in some oxygenation settings but does not deliver the high inspired concentration and flow recommended for cluster attack abortion.'),
 ('A 40% Venturi mask at its usual controlled-oxygen flow','A controlled lower inspired concentration can be appropriate in other respiratory contexts, but it is not equivalent to the recommended high-concentration cluster regimen.'),
 ('Oxygen at 6 L/min through a simple face mask','A simple mask at this flow provides less reliable high inspired oxygen than an adequately supplied nonrebreather and does not reproduce the guideline regimen.')],
 [S('Rapid Attack Treatment','**High-flow 100% oxygen** is a first-line acute option for cluster headache.',
    'Use a nonrebreather mask with reservoir and a flow of ==at least 12 L/min==, often 12–15 L/min, for approximately 15–20 minutes at attack onset. The reservoir should remain adequately supplied during inspiration.',
    'Low-flow nasal cannulae do not provide an equivalent treatment. Access to appropriate equipment matters as much as writing the word oxygen on the prescription.'),
  S('Alternatives and Safety','**Subcutaneous sumatriptan 6 mg** is another effective rapid option when vascular and other contraindications are absent.',
    'Intranasal triptans may help when injection is unsuitable; oral drugs are often too slow for short cluster attacks. Oxygen is particularly useful when triptans are unsuitable or attacks exceed permitted triptan frequency.',
    'Provide oxygen fire-safety counseling and assess relevant respiratory disease. Acute oxygen does not prevent the next attack, so frequent bouts require a separate preventive and transitional plan.')],['EAN'],style='direct')

add('Trigeminal autonomic cephalalgias','Verapamil and ECG Monitoring',
 'A patient starts verapamil for frequent cluster attacks. Which monitoring plan is most important during dose escalation?',
 'Baseline and interval ECG assessment for PR prolongation or AV block',[
 ('Serum verapamil concentration as the main safety guide','Routine drug-level targeting does not replace assessment of conduction, pulse, pressure and clinical response during headache-related verapamil titration.'),
 ('QTc assessment alone without reviewing the PR interval','The principal relevant verapamil issue is AV nodal conduction delay; examining only QTc can miss the effect being monitored.'),
 ('A baseline echocardiogram as the only follow-up test','Structural assessment may be useful when indicated, but it does not detect evolving drug-induced PR prolongation or AV block during subsequent dose increases.')],
 [S('Preventive Role','**Verapamil** is the usual first-choice cluster preventive, with dose selected by response and tolerability.',
    'A common starting total is ==240 mg/day==, often in divided doses, with specialist-guided increases as needed. Some patients require substantially higher doses than in routine cardiovascular use.',
    'The schedule and formulation vary; do not treat a single maximum dose or titration interval as universal across all patients and services.'),
  S('Conduction and Other Risks','**ECG monitoring** is essential because PR prolongation, bradycardia and AV block can develop, including after escalation.',
    'Obtain a baseline ECG and repeat according to the titration protocol and symptoms. Review other AV-nodal-slowing drugs, heart failure risk, hypotension and constipation.',
    'A short transitional treatment may reduce attacks while a safe preventive dose is reached. Rapid unsupervised escalation is not justified by severe pain; safety monitoring and prompt access to acute treatment should proceed together.')],['EAN','DANISH'])

add('Trigeminal autonomic cephalalgias','Transitional Treatment During a Cluster Bout',
 'Cluster attacks occur several times daily while verapamil is being cautiously titrated. Which listed strategy is most suitable for short-term transitional treatment?',
 'A brief supervised corticosteroid course while preventive therapy is established',[
 ('Lithium as an immediate attack-abortive drug','Lithium can be considered for prevention in selected cases, particularly chronic cluster, but it is not an immediate short-term abortive substitute for a bridging plan.'),
 ('Topiramate alone with no additional short-term strategy','Topiramate can be a preventive alternative, but titration and onset do not reliably provide the rapid bridge needed during the current intense bout.'),
 ('Melatonin as a guaranteed rapid bridge for all patients','Melatonin may have a role in selected preventive plans, but evidence and onset do not justify presenting it as a universally effective rapid transitional strategy.')],
 [S('Purpose of Bridging','**Transitional therapy** reduces attack burden during the interval before a preventive reaches an effective tolerated dose.',
    'A short oral corticosteroid regimen can be used with an appropriate taper; guideline and local regimens differ, commonly using a high initial dose over several days rather than indefinite low-dose therapy.',
    'Greater occipital nerve blockade with steroid is another specialist transitional option; it is not offered as a distractor here because it may also be reasonable.'),
  S('Avoiding Chronic Steroid Exposure','**Steroids are a bridge**, not the preferred sustained solution for chronic cluster attacks.',
    'Review diabetes, infection, blood pressure, mood, bone and gastrointestinal risks. Repeated courses require particular caution, and relapse during taper should prompt preventive reassessment rather than automatic permanent corticosteroids.',
    'Continue access to rapid oxygen or an appropriate triptan and document attack frequency. A successful bridge does not remove the need for ECG-guided verapamil titration or another durable preventive plan.')],['EAN','DANISH'])

add('Trigeminal autonomic cephalalgias','Paroxysmal Hemicrania',
 'A patient has 15 strictly unilateral orbital attacks daily, each lasting 8–12 minutes with tearing. An adequate supervised indomethacin trial completely prevents them. Which diagnosis is most likely?',
 'Paroxysmal hemicrania',[
 ('Cluster headache','Cluster attacks are usually longer and less frequent; an absolute indomethacin response with the 2–30-minute high-frequency pattern favors paroxysmal hemicrania.'),
 ('SUNCT','SUNCT can be frequent and autonomic but typically lasts seconds to at most 600 seconds and is not defined by an absolute indomethacin response.'),
 ('Hemicrania continua','Hemicrania continua has continuous unilateral background pain with exacerbations; this patient has discrete short attacks rather than a continuously painful baseline.')],
 [S('Diagnostic Pattern','**Paroxysmal hemicrania** requires at least 20 severe unilateral orbital, supraorbital or temporal attacks lasting ==2–30 minutes==.',
    'Attacks usually occur more than five daily, have ipsilateral autonomic features or restlessness/agitation, and are prevented absolutely by therapeutic indomethacin. A partial NSAID response is insufficient for the defining criterion.',
    'Frequency can vary during a minority of the course, so the overall active pattern matters.'),
  S('Indomethacin Trial','**An adequate trial** must be both safe and sufficient to judge responsiveness.',
    'ICHD-3 notes adult oral diagnostic doses of at least 150 mg/day, increasing if necessary to 225 mg/day; clinical practice often titrates upward from a lower starting dose for tolerance under supervision.',
    'Assess renal function, ulcer or bleeding risk, cardiovascular risk and gastroprotection needs. Seek the lowest effective maintenance dose after confirmation, and evaluate secondary mimics when the presentation is new or atypical; a medication response alone does not exclude structural disease.')],['DANISH'])

add('Trigeminal autonomic cephalalgias','SUNCT and SUNA',
 'A patient has dozens of unilateral orbital stabs lasting 20–80 seconds, with prominent ipsilateral conjunctival injection and tearing during each event. Which syndrome best fits?',
 'SUNCT',[
 ('SUNA with neither conjunctival injection nor tearing','SUNA is the related category when only one or neither of those two features is present, with another qualifying autonomic feature; both are prominent in this stem.'),
 ('Paroxysmal hemicrania','Its attacks are generally longer, lasting 2–30 minutes, and require complete indomethacin prevention. Seconds-long neuralgiform attacks suggest SUNCT here.'),
 ('Cluster headache','Cluster attacks usually last 15–180 minutes. Severe orbital pain and tearing alone do not overcome this large difference in duration.')],
 [S('Attack Criteria','**Short-lasting unilateral neuralgiform headache attacks** last ==1–600 seconds==, with moderate or severe trigeminal-distribution pain and cranial autonomic features.',
    'At least 20 attacks and usually at least one daily during the active period are required. The pain can occur as single stabs, grouped stabs or a saw-tooth pattern.',
    'SUNCT has both conjunctival injection and tearing. SUNA has only one or neither, provided the broader required autonomic criteria are met.'),
  S('Differential and Evaluation','**Trigeminal neuralgia** can overlap in brevity and triggers, but the prominent autonomic syndrome and refractory-period pattern can help distinguish them.',
    'Obtain appropriate MRI assessment for secondary mimics, including relevant posterior-fossa or sellar disease when clinically suggested. A normal examination does not prove a primary headache syndrome.',
    'Lamotrigine is commonly used preventively in specialist practice; evidence is smaller than for common migraine treatments. Short attacks are often over before an oral abortive could work, making preventive and selected supervised bridge strategies more important.')],['DANISH'])

add('Trigeminal autonomic cephalalgias','Hemicrania Continua',
 'A patient has strictly left-sided continuous headache for 7 months, with severe exacerbations accompanied by tearing and agitation. Therapeutic indomethacin eliminates both background pain and exacerbations. What is most likely?',
 'Hemicrania continua',[
 ('Chronic cluster headache','Chronic cluster describes a remission pattern of cluster attacks; a continuously painful background with absolute indomethacin response is more characteristic of hemicrania continua.'),
 ('Paroxysmal hemicrania','This involves discrete 2–30-minute attacks rather than the defining continuous unilateral pain between exacerbations.'),
 ('Chronic tension-type headache','Bilateral pressing pain without this autonomic and indomethacin-responsive unilateral pattern is more typical; continuous duration alone does not identify tension-type disease.')],
 [S('Defining Features','**Hemicrania continua** is a persistent unilateral headache present for more than ==3 months==, with moderate or greater exacerbations and an absolute indomethacin response.',
    'During exacerbations there are ipsilateral cranial autonomic features or restlessness/agitation or aggravation by movement. Migrainous features can also occur and do not by themselves change the primary diagnosis.',
    'The background pain is crucial: patients may describe only severe flares unless specifically asked whether they are completely pain free between them.'),
  S('Diagnostic and Treatment Review','**Confirm a sufficient indomethacin trial** while assessing gastrointestinal, renal and cardiovascular safety.',
    'The diagnostic notes use an adequate adult therapeutic dose, potentially 150–225 mg/day, but supervised titration and the lowest effective maintenance regimen reduce unnecessary toxicity. Gastroprotection may be appropriate.',
    'MRI and other investigation depend on presentation and secondary concerns. An indomethacin response is diagnostically important but should not become a reason to ignore a new structural warning sign or unexplained neurological deficit.')],['DANISH'])

add('Cranial neuralgias','Trigeminal Neuralgia Phenotype',
 'Brushing the teeth triggers recurrent unilateral electric-shock pains in the cheek and jaw, lasting several seconds with pain-free intervals. Which diagnosis best fits?',
 'Trigeminal neuralgia',[
 ('Persistent idiopathic facial pain','This is more often daily prolonged poorly localized aching pain rather than brief severe electric shocks triggered within a specific trigeminal territory.'),
 ('Painful post-traumatic trigeminal neuropathy','This requires an appropriate nerve-injury context and often positive or negative sensory signs; continuous neuropathic pain is more prominent than the typical triggerable paroxysms here.'),
 ('Glossopharyngeal neuralgia','Pain typically involves the throat, tonsillar region, tongue base, ear or angle of the jaw and is triggered by swallowing or talking; the cheek and teeth-brushing distribution favors trigeminal involvement.')],
 [S('Clinical Criteria','**Trigeminal neuralgia** causes recurrent unilateral severe electric, shooting, stabbing or sharp pain within one or more trigeminal divisions.',
    'Individual paroxysms typically last a fraction of a second to ==2 minutes== and are precipitated by innocuous stimuli in the affected distribution. Some patients also have continuous background pain.',
    'A trigger zone and a short refractory period after an attack are helpful; dental disease must be assessed appropriately rather than inferred from facial location alone.'),
  S('Classification and Evaluation','**Classical, secondary and idiopathic forms** are distinguished after investigation.',
    'Classical disease involves neurovascular compression with morphological nerve changes, not merely any vessel contact. Secondary causes include multiple sclerosis or a structural lesion.',
    'MRI is part of the work-up because clinical features cannot exclude every secondary cause. Sensory loss, bilateral symptoms, younger presentation or another neurological sign increases concern and guides urgency, but their absence does not prove a primary form.')],['DANISH'])

add('Cranial neuralgias','MRI in Suspected Trigeminal Neuralgia',
 'A 33-year-old with triggerable facial shocks also has persistent facial numbness and episodes of diplopia. Which investigation is most appropriate to assess a secondary cause?',
 'Brain MRI with dedicated trigeminal and posterior-fossa assessment',[
 ('Dental panoramic imaging as the only investigation','Dental evaluation may identify an odontogenic cause, but does not assess demyelination, cerebellopontine-angle lesions or the trigeminal root explaining the additional neurological findings.'),
 ('Noncontrast sinus CT as the definitive test','Sinus imaging does not adequately assess the neural pathway or demyelinating disease suggested by numbness and diplopia.'),
 ('Carotid Doppler as a substitute for intracranial nerve imaging','Cervical vascular ultrasound does not establish the cause of trigeminal-root symptoms or evaluate associated brainstem disease.')],
 [S('Secondary-Cause Assessment','**MRI** evaluates multiple sclerosis, tumors, other structural lesions and neurovascular compression in suspected trigeminal neuralgia.',
    'Use high-resolution posterior-fossa/trigeminal sequences and appropriate whole-brain assessment; vascular and contrast sequences are selected according to the clinical question.',
    'Persistent sensory change and other neurological symptoms strengthen concern for secondary disease. Nevertheless, modern guideline work-up does not rely on the absence of red flags to exclude all secondary causes.'),
  S('Interpreting Neurovascular Contact','**A vessel touching the nerve** is common and does not by itself establish classical trigeminal neuralgia.',
    'Compression with morphological changes such as displacement, indentation or atrophy is more meaningful. Imaging findings must fit the painful side and clinical phenotype.',
    'If MRI is contraindicated, specialist alternatives may include trigeminal reflex testing and other tailored studies. A normal plain CT or a negative dental examination is not equivalent to a complete neural investigation.')],['DANISH'])

add('Cranial neuralgias','First-Choice Pharmacotherapy for Trigeminal Neuralgia',
 'A patient with classical trigeminal neuralgia requires an initial preventive medication. Which listed drug has the strongest first-choice guideline position?',
 'Carbamazepine',[
 ('Gabapentin','Gabapentin can be considered as an alternative or add-on, especially when first-choice agents are unsuitable, but it does not displace carbamazepine or oxcarbazepine as the usual initial choices.'),
 ('Baclofen','Baclofen can help selected patients, sometimes as add-on therapy, but its guideline position is not the same as the usual first-choice sodium-channel blockers.'),
 ('Lamotrigine','Lamotrigine can be used in selected refractory or intolerant cases and requires slow titration; it is not the preferred initial agent among these choices for a typical new case.')],
 [S('First-Line Options','**Carbamazepine or oxcarbazepine** are guideline-recommended first-choice medicines for trigeminal neuralgia.',
    'A common carbamazepine starting regimen is 100 mg once or twice daily, gradually titrated to response; many adults require 400–1200 mg/day in divided doses, with individual limits and tolerability considered.',
    'Oxcarbazepine is an alternative first-choice agent, commonly started at a low twice-daily dose and titrated. It is not offered as a distractor because it could also be a defensible answer.'),
  S('Monitoring and Escalation','**Check sodium, blood counts, hepatic risk and interactions** as clinically appropriate.',
    'Carbamazepine is an enzyme inducer and can cause hyponatremia, hematological toxicity and severe rash. Assess HLA-B*15:02 screening in genetically at-risk ancestry groups before first exposure; other hypersensitivity associations also matter.',
    'Oxcarbazepine also has substantial hyponatremia risk. If adequate treatment fails or adverse effects limit use, consider alternatives and surgical evaluation rather than repeated unsupervised dose escalation.')],['DANISH'],style='direct')

add('Cranial neuralgias','Microvascular Decompression',
 'A medically fit patient has classical trigeminal neuralgia with concordant arterial compression and morphological root changes. Adequate medication trials have failed or caused intolerable effects. Which procedure offers a nonablative nerve-preserving approach?',
 'Microvascular decompression',[
 ('Percutaneous radiofrequency lesioning','This can reduce pain through a destructive trigeminal procedure, but carries sensory loss and dysesthesia risk and is not the nonablative approach requested.'),
 ('Balloon compression of the trigeminal ganglion','Balloon compression is another percutaneous neuroablative option useful in selected patients, rather than decompression that preserves the nerve without an intended destructive lesion.'),
 ('Stereotactic radiosurgery','Radiosurgery can be appropriate for selected patients, often with delayed benefit, but works by a targeted radiation effect on the nerve rather than mechanically separating the offending artery.')],
 [S('Anatomical Rationale','**Microvascular decompression** separates the compressing vessel from the trigeminal root without intending to destroy sensory fibers.',
    'EAN guidance favors it as first-line surgery for suitable classical TN. Concordant compression with nerve morphological change is more relevant than nonspecific vessel contact alone.',
    'Selection includes medical fitness, expected benefit, prior procedures, anatomy and the patient’s preferences regarding recurrence and sensory risks.'),
  S('Trade-Offs and Alternatives','**Posterior-fossa surgery** has operative risks despite a favorable potential for durable pain relief.',
    'Discuss hearing impairment, CSF leak, neurological injury and other surgical complications. Percutaneous procedures or radiosurgery may be attractive when operative risk is higher or anatomy and preferences favor them.',
    'Neuroablative approaches can cause numbness and, rarely, troublesome deafferentation pain. No procedure should be described as guaranteed permanent cure, and recurrent pain warrants reassessment rather than automatic repetition of the same intervention.')],['DANISH'])

add('Cranial neuralgias','Glossopharyngeal Neuralgia With Syncope',
 'Brief severe shocks start in the tonsillar region and tongue base, radiating to the ear during swallowing. Some attacks cause bradycardia and syncope. Which diagnosis is most likely?',
 'Glossopharyngeal neuralgia',[
 ('Trigeminal neuralgia','Facial triggers and V2/V3 shocks are typical, but tongue-base/tonsillar pain with swallowing and vagal cardiovascular phenomena favors glossopharyngeal involvement.'),
 ('Temporomandibular joint disorder','Jaw-motion pain may overlap with eating-related symptoms, but joint pain is not typically a seconds-long pharyngeal-to-ear electric shock with reflex bradycardia.'),
 ('Eagle syndrome as an established diagnosis from symptoms alone','An elongated styloid process can cause regional pain and secondary neuralgic symptoms, but that structural cause requires demonstration; the clinical neuralgia syndrome is what the stem establishes.')],
 [S('Pain Distribution and Triggers','**Glossopharyngeal neuralgia** involves brief unilateral stabbing or electric pain in the posterior tongue, tonsillar fossa, pharynx, angle of the jaw or deep ear.',
    'Swallowing, coughing, yawning or talking may trigger attacks, which typically last seconds to about two minutes. Vagal connections can produce bradycardia, asystolic episodes or syncope in some patients.',
    'Distinguish a neuralgic attack from persistent inflammatory, malignant or mechanical throat pain.'),
  S('Investigation and Safety','**Syncope makes cardiac monitoring important** as well as neurological and structural assessment.',
    'Assess for a secondary head-and-neck or skull-base cause and neurovascular compression with appropriate imaging. Swallowing avoidance can lead to weight loss and dehydration, requiring active management.',
    'Carbamazepine or oxcarbazepine is often used, with specialist procedural options for refractory disease. Treating bradyarrhythmic risk and pain requires coordination; a pacemaker decision alone does not address the cause of neuralgic pain.')],['DANISH'])

add('Cranial neuralgias','Occipital Neuralgia',
 'A patient has seconds-long shooting pain over the posterior scalp, allodynia with hair brushing and marked tenderness over the greater occipital nerve. Local-anesthetic nerve block temporarily abolishes the pain. Which diagnosis is supported?',
 'Occipital neuralgia',[
 ('Cervicogenic headache without neuralgia','Cervical structures can refer pain to the occiput, but paroxysmal shooting pain with nerve-distribution dysesthesia and focal tenderness supports a neuralgic phenotype.'),
 ('Chronic tension-type headache','Tension-type pain is generally pressing rather than brief stabbing neuralgic paroxysms, and the focal nerve-distribution allodynia is not its defining pattern.'),
 ('Primary stabbing headache','Primary stabs can be brief, but the reproducible nerve-territory tenderness, sensory features and block response suggest occipital neuralgia rather than an unlocalized primary stabbing syndrome.')],
 [S('Diagnostic Components','**Occipital neuralgia** affects the greater, lesser or third occipital nerve distribution and may be unilateral or bilateral.',
    'The characteristic pain is severe, shooting or stabbing, occurring in paroxysms lasting seconds to minutes, with dysesthesia or allodynia and nerve tenderness or trigger points.',
    'Temporary relief from an appropriate local-anesthetic nerve block is part of the ICHD-3 framework, but a block response alone is not specific because other headache disorders can also improve.'),
  S('Differential and Management','**Examine the cervical region and neurological system** and investigate a suspected structural or traumatic cause when indicated.',
    'Distinguish referred pain from upper cervical joints, muscular trigger points and migraine-related occipital tenderness. Trigeminocervical connections can allow anterior radiation, so an orbital component does not necessarily exclude occipital input.',
    'Treatment may include medication, physical measures and targeted blocks, with selected interventions for refractory cases. Explain sensory and procedural risks rather than assuming a positive block proves that permanent nerve destruction is appropriate.')],['DANISH'])

add('Secondary headache decisions','Giant-Cell Arteritis With Threatened Vision',
 'A 74-year-old has new temporal headache, jaw claudication and transient monocular visual loss, with raised inflammatory markers. Giant-cell arteritis is strongly suspected. Which principle is most important?',
 'Start urgent glucocorticoid treatment without waiting for confirmatory testing',[
 ('Wait for temporal artery biopsy before giving the first dose','Biopsy is important, but delaying treatment in a threatened-vision presentation can permit irreversible loss. Arrange confirmation promptly while treatment begins.'),
 ('Use a negative ESR alone to withhold treatment if repeat testing is normal','Inflammatory markers support assessment but are not perfectly sensitive; a compelling ischemic presentation cannot be dismissed by one normal value.'),
 ('Treat as uncomplicated migraine because visual loss was transient','Age, new headache, jaw claudication and visual ischemic symptoms are a high-risk secondary pattern; temporary recovery does not remove the risk.')],
 [S('Immediate Vision Protection','**Suspected GCA with visual ischemia** is an urgent treatment and ophthalmic assessment problem.',
    'ACR/VF guidance conditionally favors IV pulse glucocorticoids for threatened vision, commonly methylprednisolone 500–1000 mg/day for 3 days under specialist care. Patients without cranial ischemia often start high-dose oral therapy instead.',
    'The exact regimen depends on clinical severity and local guidance, but confirmation should not postpone protection against imminent visual loss.'),
  S('Confirmation and Follow-Up','**Temporal artery imaging or biopsy** establishes diagnostic support, with the preferred pathway depending on local expertise and guideline framework.',
    'Arrange testing promptly because treatment can reduce imaging sensitivity; a negative biopsy also requires interpretation in light of skip lesions and the overall probability. Assess large-vessel involvement and steroid toxicity.',
    'Monitor glucose, pressure, bone and infection risk, and discuss steroid-sparing treatment when appropriate. Do not infer that headache improvement alone proves GCA or that a resolved monocular event was harmless.')],['NICE'])

add('Secondary headache decisions','Idiopathic Intracranial Hypertension',
 'An obese young woman has papilledema, pulsatile tinnitus and transient visual obscurations. MRI and venography exclude a mass and venous thrombosis. Neurological examination is otherwise normal apart from a sixth-nerve palsy. Which finding supports IIH?',
 'Opening pressure above 25 cm CSF with normal CSF composition in a correctly performed LP',[
 ('Opening pressure 18 cm CSF with inflammatory pleocytosis','Neither a normal-range pressure nor inflammatory CSF establishes the usual IIH framework; infection or inflammation needs evaluation.'),
 ('A single high pressure measured while straining, without review of technique','Technique and clinical context matter. A falsely elevated measurement cannot substitute for a reliable opening pressure and full diagnostic assessment.'),
 ('Papilledema attributed to obesity without venous or structural evaluation','Obesity is a risk factor, not proof of idiopathic disease; mass lesions, venous thrombosis, medication effects and other causes must be excluded.')],
 [S('Diagnostic Framework','**Adult IIH** is supported by papilledema, appropriate neurological examination, suitable normal structural/venous imaging, normal CSF constituents and elevated opening pressure.',
    'A cut-off ==above 25 cm CSF== is used in the consensus framework. Measure in the lateral decubitus position with the patient relaxed, and interpret a borderline or discordant value in context rather than in isolation.',
    'Without papilledema, additional strict criteria apply; an incidental pressure or an empty-sella MRI finding alone is insufficient.'),
  S('Preserving Vision','**Assess acuity, formal fields and papilledema severity**, not just headache relief.',
    'Weight reduction is disease modifying. Acetazolamide commonly starts at 250–500 mg twice daily and is titrated to tolerance, monitoring renal function, electrolytes, acidosis and stone risk.',
    'Rapidly worsening vision requires urgent specialist pressure-lowering intervention rather than a prolonged trial of headache drugs or repeated unstructured LPs. Headache phenotype may also need migraine-directed care once vision and pressure are addressed.')],['NICE'])

add('Secondary headache decisions','Spontaneous Intracranial Hypotension',
 'A patient develops a new headache that worsens after standing and improves substantially when supine. There has been no dural procedure. Contrast MRI shows diffuse smooth pachymeningeal enhancement and brain sag. What is most likely?',
 'Spontaneous intracranial hypotension from spinal CSF leakage or a CSF–venous fistula',[
 ('Idiopathic intracranial hypertension','IIH generally has a raised-pressure and papilledema context; the marked orthostatic pattern with smooth dural enhancement and brain sag favors low CSF volume.'),
 ('Chronic migraine established solely by frequent headache','Frequent pain does not negate a new reproducible orthostatic syndrome or the characteristic imaging findings, which require a secondary-cause diagnosis.'),
 ('Leptomeningeal carcinomatosis as proven by any meningeal enhancement','Leptomeningeal and pachymeningeal patterns differ. Smooth diffuse dural enhancement with sag in this clinical setting is not proof of malignant leptomeningeal disease.')],
 [S('Low CSF Volume Syndrome','**SIH** can arise from a dural tear, leaking diverticulum or CSF–venous fistula.',
    'MRI clues include smooth pachymeningeal enhancement, venous engorgement, pituitary enlargement, subdural collections and downward brain displacement. A normal opening pressure does not exclude it, despite the traditional name.',
    'The postural quality can become less obvious over time, so ask about the initial pattern rather than only current symptoms.'),
  S('Investigation and Treatment','**Contrast brain MRI and whole-spine MRI** are recommended first-line investigations in the 2023 multidisciplinary pathway.',
    'Spine imaging may show an extradural collection and guide later myelography, but often does not localize the exact leak. LP should not be performed solely to prove low pressure when the diagnosis is otherwise supported.',
    'Early non-targeted epidural blood patch is a key treatment. Persistent cases may need dynamic CT or digital-subtraction myelography to target a leak or fistula; a fistula can exist without an extradural collection.')],['DANISH'])

add('Secondary headache decisions','Reversible Cerebral Vasoconstriction Syndrome',
 'A postpartum patient has recurrent thunderclap headaches over one week. Aneurysmal SAH is excluded. CTA shows multifocal segmental narrowing, and CSF is near normal. Which diagnosis is favored?',
 'Reversible cerebral vasoconstriction syndrome',[
 ('Primary angiitis of the CNS','PACNS more often has a subacute progressive course and inflammatory CSF or other supportive evidence. Angiographic beading alone is not specific, but the recurrent thunderclap postpartum phenotype favors RCVS.'),
 ('Migraine with typical aura','A recurrent maximal-at-onset thunderclap pattern with arterial narrowing is not explained by ordinary gradual typical aura, even if migraine history is present.'),
 ('Cervical artery dissection as established by intracranial beading alone','Dissection is important in the differential and may coexist, but requires appropriate arterial-wall or luminal evidence; diffuse intracranial segmental constriction in this context favors RCVS.')],
 [S('Clinical and Vascular Pattern','**RCVS** features recurrent thunderclap headache with reversible multifocal arterial constriction.',
    'Postpartum physiology and vasoactive exposures are recognized contexts. Angiography can be normal early, especially in the first week; a high-suspicion presentation may need follow-up imaging.',
    'Document resolution, usually within about 12 weeks, and monitor for convexity SAH, ischemic infarction, ICH or PRES. “Reversible” describes the vessel pattern, not a guarantee that brain injury cannot occur.'),
  S('Treatment Cautions','**Remove triggers and provide monitored supportive care** with careful pressure and neurological assessment.',
    'Calcium-channel blockers such as nimodipine are often used for headache symptoms, but robust evidence that they prevent stroke is lacking. Avoid assuming that improvement proves the diagnosis.',
    'Glucocorticoids are not routine RCVS treatment and have been associated with worse outcomes; distinguish it carefully from inflammatory vasculitis before starting an immunosuppressive pathway.')],['DANISH'])

add('Secondary headache decisions','Cough Headache and the Craniovertebral Junction',
 'A patient develops new short occipital headaches triggered only by coughing or straining. What is the most appropriate approach before labeling the disorder primary cough headache?',
 'Obtain appropriate brain and craniovertebral-junction MRI',[
 ('Diagnose primary cough headache from a normal funduscopic examination alone','A normal fundus does not exclude a Chiari malformation or other posterior-fossa structural cause of a Valsalva-triggered headache.'),
 ('Use an indomethacin response as sufficient proof of a primary disorder','A response can be useful therapeutically but is not a replacement for investigating a new cough-triggered secondary phenotype.'),
 ('Use cervical plain radiographs as a complete substitute for MRI','Radiographs do not evaluate cerebellar tonsils, CSF spaces or posterior-fossa masses adequately; the relevant structural question requires neural imaging.')],
 [S('Why Image','**Cough or Valsalva-triggered pain** can be secondary to a craniovertebral or posterior-fossa process.',
    'Chiari I malformation is an important cause. Other structural lesions or CSF-pressure disorders can produce similar symptoms, so a new phenotype warrants investigation even without limb weakness.',
    'MRI should assess the posterior fossa, foramen magnum and relevant spinal or CSF features according to the findings.'),
  S('Primary Diagnosis and Causation','**Primary cough headache** is considered after no better cause is found, not before structural assessment.',
    'It is brought on by coughing, straining or another Valsalva maneuver, begins suddenly and can last from seconds up to two hours under ICHD-3. A first thunderclap or atypical exertional episode also requires its appropriate emergency vascular evaluation.',
    'An incidental low tonsillar position is not automatically causal; symptoms, CSF physiology and imaging must fit. Treatment or neurosurgical referral should follow the demonstrated cause and functional impact rather than the imaging label alone.')],['NICE'])

add('Secondary headache decisions','Red Flags That Change Imaging Decisions',
 'A patient with treated breast cancer develops a progressive new headache and intermittent vomiting over three weeks. Neurological examination is currently normal. Which approach is most appropriate?',
 'Investigate promptly with brain imaging, usually MRI with and without contrast when feasible',[
 ('Defer imaging until a persistent focal deficit appears','A normal current examination does not remove the significance of cancer history and progressive new symptoms; metastatic or other intracranial disease can present before focal signs.'),
 ('Classify migraine solely because nausea or vomiting is present','Nausea and vomiting are not migraine-specific and can accompany raised pressure or a mass. The new progressive cancer-context pattern requires secondary assessment.'),
 ('Perform sinus radiographs as the primary intracranial assessment','Sinus radiographs do not address metastasis, hydrocephalus or other intracranial causes and should not divert the investigation prompted by this red-flag history.')],
 [S('High-Risk Context','**Cancer or immunocompromise** lowers the threshold for imaging a new or changed headache.',
    'Other concerning features include thunderclap onset, fever, a focal deficit, papilledema, a progressive pattern, onset after age 50, pregnancy or puerperium, positional dependence and Valsalva precipitation.',
    'The urgency and modality depend on the suspected cause. An acutely deteriorating patient may need immediate CT rather than waiting for a preferred outpatient MRI.'),
  S('Choosing the Test','**MRI with and without contrast** is useful for many neoplastic, inflammatory and posterior-fossa questions when safe and available.',
    'Vascular studies, venography or CSF evaluation may be needed for a different suspected mechanism. Review renal function, contrast suitability and LP safety where relevant.',
    'In contrast, stable typical migraine with a normal examination and no red flags often does not require imaging solely for reassurance. The decision follows the current risk pattern, not the intensity of pain alone or a blanket scan-every-headache rule.')],['NICE'])

add('Secondary headache decisions','Post-Dural-Puncture Headache and Blood Patch',
 'Two days after a documented accidental dural puncture, a patient has a disabling postural headache that persists despite appropriate conservative measures. Examination is reassuring and there is no infection or coagulopathy. Which treatment should be considered?',
 'Therapeutic epidural blood patch',[
 ('Continue caffeine alone indefinitely despite major functional limitation','Caffeine may provide temporary symptomatic relief but does not reliably seal the leak; persistent disabling symptoms justify reassessment and discussion of definitive treatment.'),
 ('A prophylactic blood patch as though no headache had developed','This is now symptomatic treatment, not prophylaxis. Routine prophylactic patching after every puncture has a different and insufficient evidence base.'),
 ('Repeated lumbar punctures to document progressively lower pressure','Additional punctures can worsen leakage and are not required to establish a typical documented post-puncture syndrome or decide on a therapeutic patch.')],
 [S('Recognition and Reassessment','**PDPH** typically begins within five days of dural puncture and often worsens upright with relief supine.',
    'Consider neck symptoms or auditory changes, but do not attribute every postpartum or postprocedural headache to the puncture. Focal signs, fever, seizures, a nonpostural change or unusual persistence require investigation for alternatives such as CVT, preeclampsia or subdural bleeding.',
    'The treatment decision depends on disability and the clinical context, not solely a fixed number of days.'),
  S('Therapeutic Patch','**Autologous epidural blood** can seal the leak and restore CSF-pressure support.',
    'A commonly recommended volume is approximately ==15–20 mL==, stopping earlier for significant pain or other limiting symptoms, under an appropriate sterile anesthetic protocol. Confirm relevant coagulation and infection safety.',
    'Explain incomplete response, recurrence and procedural risks. A second patch may be considered after reassessing other causes; repeated failure or a changing phenotype warrants further imaging and specialist review rather than automatic serial patching.')],['DANISH'])

R.update({
 'EREN':('FDA erenumab prescribing information, 2025','https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/761077s026lbl.pdf'),
 'CM':('ICHD-3: Chronic migraine','https://ichd-3.org/1-migraine/1-3-chronic-migraine/'),
 'MOH':('ICHD-3: Triptan-overuse headache','https://ichd-3.org/8-headache-attributed-to-a-substance-or-its-withdrawal/8-2-medication-overuse-headache-moh/8-2-2-triptan-overuse-headache/'),
 'TTH':('ICHD-3: Chronic tension-type headache','https://ichd-3.org/2-tension-type-headache/2-3-chronic-tension-type-headache/'),
 'EPCL':('ICHD-3: Episodic cluster headache','https://ichd-3.org/3-trigeminal-autonomic-cephalalgias/3-1-cluster-headache/3-1-1-episodic-cluster-headache/'),
 'PH':('ICHD-3: Paroxysmal hemicrania','https://ichd-3.org/3-trigeminal-autonomic-cephalalgias/3-2-paroxysmal-hemicrania/'),
 'SUN':('ICHD-3: Short-lasting unilateral neuralgiform headache attacks','https://ichd-3.org/3-trigeminal-autonomic-cephalalgias/3-3-short-lasting-unilateral-neuralgiform-headache-attacks/'),
 'HC':('ICHD-3: Hemicrania continua','https://ichd-3.org/3-trigeminal-autonomic-cephalalgias/3-4-hemicrania-continua/'),
 'TN':('EAN trigeminal neuralgia guideline, 2019','https://doi.org/10.1111/ene.13950'),
 'TNICHD':('ICHD-3: Trigeminal neuralgia','https://ichd-3.org/13-painful-cranial-neuropathies-and-other-facial-pains/13-1-trigeminal-neuralgia/'),
 'GLOSS':('ICHD-3: Glossopharyngeal neuralgia','https://ichd-3.org/13-painful-cranial-neuropathies-and-other-facial-pains/13-2-glossopharyngeal-neuralgia/13-2-1-glossopharyngeal-neuralgia/'),
 'OCC':('ICHD-3: Occipital neuralgia','https://ichd-3.org/13-painful-cranial-neuropathies-and-other-facial-pains/13-4-occipital-neuralgia/'),
 'GCA':('ACR/Vasculitis Foundation GCA guideline, 2021','https://doi.org/10.1002/art.41774'),
 'IIH':('IIH consensus management guidelines, 2018','https://doi.org/10.1136/jnnp-2017-317440'),
 'SIH':('Multidisciplinary SIH consensus guideline, 2023','https://pmc.ncbi.nlm.nih.gov/articles/PMC10511987/'),
 'RCVS':('ICHD-3: Acute headache attributed to RCVS','https://ichd-3.org/6-headache-attributed-to-cranial-or-cervical-vascular-disorder/6-7-headache-attributed-to-other-acute-intracranial-arterial-disorder/6-7-3-headache-attributed-to-reversible-cerebral-vasoconstriction-syndrome-rcvs/6-7-3-1-headache-probably-attributed-to-reversible-cerebral-vasoconstriction-syndrome-rcvs/'),
 'COUGH':('ICHD-3: Primary cough headache','https://ichd-3.org/other-primary-headache-disorders/4-1-primary-cough-headache/'),
 'ACR':('ACR Headache Appropriateness Criteria: red-flag headache','https://acsearch.acr.org/list/GetAppendix?TopicId=140&TopicName=Headache'),
 'PDPH':('ASRA/multisociety post-dural-puncture headache guideline summary, 2024','https://asra.com/the-asra-family/special-interest-groups/neuromodulation-sig/neuromodulation-sig-article-item/asra-news/2024/11/06/collaborative-excellence-the-multi-society-post-dural-puncture-headache-guidelines'),
})
for n,key in {15:'EREN',18:'CM',19:'MOH',21:'TTH',23:'EPCL',27:'PH',28:'SUN',29:'HC',30:'TNICHD',31:'TN',32:'TN',33:'TN',34:'GLOSS',35:'OCC',36:'GCA',37:'IIH',38:'SIH',39:'RCVS',40:'COUGH',41:'ACR',42:'PDPH'}.items():rows[n-1]['refs'].append(key)

rows[15]['others']=[
 ('155 units across 31 sites every 4 weeks','The fixed-site total is recognizable, but routine four-week retreatment is not the labeled chronic-migraine interval and adds unnecessary exposure.'),
 ('195 units across 39 sites every 12 weeks','This is a real PREEMPT-derived fixed-site plus follow-the-pain regimen in appropriate settings, but the question asks specifically for the standard labeled 155-unit fixed-site protocol.'),
 ('100 units across 20 sites every 12 weeks','Lower-dose or different-site approaches have been explored, but this is not the labeled fixed-site protocol on which the requested regimen is based.')]
rows[30]['others']=[
 ('Noncontrast head CT','This may detect major acute pathology but has limited sensitivity for demyelination and subtle trigeminal-root or posterior-fossa lesions in this young patient with additional neurological symptoms.'),
 ('Head and neck CT angiography alone','CTA can answer a vascular question, but it does not provide the demyelination-sensitive and fine neural assessment required to investigate this suspected secondary neuralgia.'),
 ('Contrast-enhanced head CT','Contrast CT can identify some mass lesions when MRI is unavailable, but MRI is preferred for the brainstem, demyelinating disease and detailed trigeminal anatomy when it can be obtained.')]
rows[40]['question']='A patient with breast cancer has a progressive new headache and intermittent vomiting for three weeks but is clinically stable with a normal examination. All modalities are available and contrast is safe. Which study is preferred for detecting small intracranial metastases?'
rows[40]['answer']='Brain MRI with and without intravenous contrast'
rows[40]['others']=[
 ('Noncontrast head CT','CT can be useful immediately in an unstable patient or for hemorrhage, but is less sensitive for small metastases than contrast MRI in this stable patient.'),
 ('Contrast-enhanced head CT','This is a reasonable alternative when MRI cannot be performed, but contrast MRI generally detects small lesions and posterior-fossa disease more sensitively when both are available.'),
 ('Brain MRI without contrast only','Noncontrast MRI can demonstrate many abnormalities, but contrast adds sensitivity and characterization for small metastases when there is no contraindication.')]

if __name__=='__main__':
    coverage=ROOT/'Neurology/04. Headache Disorders & Cranial Neuralgias.coverage.json'
    c=json.loads(coverage.read_text(encoding='utf-8'))
    assert len(rows)==sum(s['questions'] for s in c['sections'])==42
    index=0
    for section in c['sections']:
        assert len(section['decisions'])==section['questions']
        for decision in section['decisions']:
            assert rows[index]['topic']==section['section'],(index,rows[index]['topic'])
            rows[index]['coverageDecision']=decision
            index+=1
    save('Neurology',4,'04. Headache Disorders & Cranial Neuralgias',rows,R,
      'Original postgraduate educational synthesis with a documented 42-decision coverage map. Classification checked against ICHD-3; treatment-sensitive details checked against named specialty guidance and product labels. AHS positioning, reimbursement rules and national prescribing restrictions can differ and are distinguished where relevant. Full Harrison’s subscription text was not accessed. No independent clinician validation is claimed.')
    c['status']='authored_validated';c['authoredQuestions']=len(rows)
    c['questionDecisions']=[dict(question=i+1,title=r['title'],decision=r['coverageDecision']) for i,r in enumerate(rows)]
    coverage.write_text(json.dumps(c,ensure_ascii=False,indent=2),encoding='utf-8')
