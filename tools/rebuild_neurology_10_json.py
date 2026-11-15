"""Original NMJ and muscle chapter; serialize only after mapped coverage is complete."""
import json
import re
from qbank_json_chapters import question as Q, save, ROOT

R = {
 'MG': ('AAPM&R: myasthenia gravis, updated 2024', 'https://now.aapmr.org/myasthenia-gravis/'),
 'CONS': ('International consensus guidance for MG: 2020 update, published 2021', 'https://doi.org/10.1212/WNL.0000000000011124'),
 'SYND': ('Guideline for management of myasthenic syndromes, 2023', 'https://doi.org/10.1177/17562864231213240'),
 'EDX': ('AANEM practice parameter: RNS and single-fiber EMG in suspected MG/LEMS', 'https://www.aanem.org/docs/default-source/documents/aanem/practice/guidelines/myastheniagravis_reaffirmed.pdf'),
 'CMS': ('GeneReviews: congenital myasthenic syndromes overview', 'https://www.ncbi.nlm.nih.gov/books/NBK1168/'),
}

def S(h, main, *children): return (h, [(main, list(children))])
rows = []
def add(*a, **kw): rows.append(Q(*a, **kw))

add('Myasthenia gravis: recognition and diagnosis', 'Objective Fatigability in Myasthenia Gravis',
 'A woman has intermittent diplopia and ptosis that worsen during prolonged reading. Sustained upgaze increases the ptosis; pupils, sensation and tendon reflexes are normal. Which diagnosis best fits?',
 'Autoimmune myasthenia gravis', [
 ('Thyroid-associated orbitopathy', 'Orbitopathy can cause diplopia through restrictive extraocular disease, often with lid retraction or proptosis; fluctuating fatigable ptosis with this examination is more characteristic of MG.'),
 ('Chronic progressive external ophthalmoplegia', 'Mitochondrial ophthalmoplegia can produce ptosis and ocular weakness, but usually progresses slowly with relatively fixed limitation rather than clear activity-related fluctuation.'),
 ('An isolated third-nerve palsy', 'A third-nerve lesion can cause ptosis and diplopia, sometimes with pupil involvement; a consistent nerve-pattern deficit rather than fluctuating fatigability would be expected.')],
 [S('Transmission Failure Rather Than General Fatigue', '**MG causes fluctuating objective skeletal-muscle weakness**, particularly ocular, bulbar, neck and proximal limb weakness. Repeated activity can reveal a decrement in performance, with improvement after rest.',
    'General tiredness alone is insufficient. Demonstrate a reproducible pattern and ask about chewing, speech, swallowing, head control and breathing as well as limb activity.',
    'Pupillary responses and sensation are generally preserved. Prominent autonomic symptoms or areflexia should broaden the differential to presynaptic disease and other mimics.'),
  S('Confirm and Determine Extent', '**Serology and appropriately selected electrophysiology** support a compatible phenotype. Ocular-only disease can have negative standard antibody and routine stimulation results, so one negative test is not an automatic exclusion.',
    'Assess for generalization and airway risk at the first encounter. Severe dysphagia, weak cough or respiratory decline needs urgent evaluation rather than a routine outpatient diagnostic sequence.',
    'Evaluate thymic disease after autoimmune MG is established. Symptomatic acetylcholinesterase inhibition and immune treatment have different roles; response to a drug trial alone should not replace diagnostic concordance. Fixed ophthalmoplegia, restrictive eye movements or a focal cranial-nerve pattern warrant targeted assessment for competing pathology.')], ['MG','CONS'])

add('Myasthenia gravis: recognition and diagnosis', 'Antibody Testing After a Negative AChR Assay',
 'An adult has convincing fatigable bulbar and neck weakness. Standard AChR antibodies are negative. Which antibody assay is most appropriate next in the usual autoimmune MG evaluation?',
 'MuSK antibodies', [
 ('P/Q-type voltage-gated calcium-channel antibodies', 'These support LEMS in a compatible proximal, autonomic and reflex-facilitation phenotype; they are not the usual next autoimmune MG assay for prominent fatigable bulbar-neck weakness.'),
 ('Anti-GQ1b IgG', 'GQ1b testing is relevant to acute ophthalmoplegic/ataxic GBS-spectrum disease, especially with areflexia; it does not investigate the most likely MG subgroup here.'),
 ('Anti-HMGCR antibodies', 'HMGCR antibodies identify an immune necrotizing myopathy context, usually with persistent proximal weakness and substantial CK elevation, not primarily fatigable bulbar transmission failure.')],
 [S('A Phenotype-Directed Sequence', '**AChR antibodies are the commonest autoimmune MG marker.** If the standard assay is negative and clinical suspicion persists, test MuSK, especially in prominent bulbar, neck or respiratory disease.',
    'A negative result does not establish absence of autoimmunity. Specialist testing can include clustered-AChR cell-based assays and selected LRP4 evaluation, interpreted according to assay validation and the clinical setting.',
    'Avoid treating every weak antibody signal as diagnostic. False positives and unrelated antibodies become more consequential when the clinical pretest probability is low.'),
  S('Seronegative Is a Test Description', '**Seronegative MG requires the same clinical discipline** as seropositive disease. Targeted RNS or jitter testing can support impaired neuromuscular transmission, while reassessment should exclude myopathy, motor neuron disease and structural causes.',
    'Early-onset, familial or atypical persistent disease can suggest a congenital myasthenic syndrome even when recognized in adulthood. Genetic syndromes need subtype-directed treatment rather than automatic immune escalation.',
    'Antibody subgroup helps guide later therapy, but the clinical severity determines urgency. Do not delay airway assessment or rescue treatment for a convincing severe exacerbation while awaiting a specialized assay. Antibody concentration alone is not a reliable substitute for serial strength, bulbar and respiratory assessment.')], ['MG','SYND','CMS'])

add('Myasthenia gravis: recognition and diagnosis', 'MuSK Antibodies and Receptor Clustering',
 'Which mechanism most closely characterizes the commonly IgG4-mediated MuSK-associated form of MG?',
 'Disruption of agrin–LRP4–MuSK signaling and AChR clustering', [
 ('Complement-mediated destruction by antibodies binding the AChR as the principal process', 'Complement-fixing AChR antibodies can damage the postsynaptic membrane in AChR MG; MuSK IgG4 disease primarily interferes with receptor-clustering signaling.'),
 ('Antibody-mediated reduction of presynaptic calcium entry', 'Presynaptic P/Q-type calcium-channel autoimmunity is characteristic of LEMS and reduces acetylcholine release; it is not the MuSK receptor-clustering mechanism.'),
 ('Genetically reduced acetylcholinesterase anchoring at the end plate', 'COLQ-related congenital disease can impair acetylcholinesterase anchoring and alter transmission, but is an inherited syndrome rather than MuSK autoantibody disease.')],
 [S('Postsynaptic Organization', '**MuSK coordinates postsynaptic specialization** through the agrin–LRP4 signaling pathway. Interference reduces effective clustering and stability of AChRs, compromising the safety margin of transmission.',
    'The predominance of IgG4 helps explain why complement-mediated injury is not the same central mechanism as in common AChR-antibody disease. Antibody specificity therefore has therapeutic as well as diagnostic importance.',
    'Clinical presentations often emphasize facial, bulbar, neck and respiratory muscles, sometimes with less prominent limb weakness. This is a tendency rather than a requirement for every patient.'),
  S('Clinical Consequences', '**Pyridostigmine may be less effective or less well tolerated** in MuSK MG, so a poor symptomatic response should prompt clinical reassessment rather than dismissal of a supported diagnosis.',
    'Rituximab is an early consideration after an unsatisfactory response to initial immunotherapy under international consensus guidance. The evidence and indications for targeted therapies must be checked for the relevant antibody subgroup.',
    'Thymectomy evidence from nonthymomatous AChR-positive generalized MG should not be transferred automatically to MuSK disease. A thymic mass still needs its own assessment. In severe bulbar disease, secretion handling and ventilatory reserve require attention even when limb strength appears relatively preserved.')], ['MG','CONS','SYND'], style='direct')

add('Myasthenia gravis: recognition and diagnosis', 'Low-Frequency Repetitive Nerve Stimulation',
 'In a patient with fatigable weakness, technically adequate stimulation at 3 Hz produces a reproducible 14% fall in CMAP amplitude between the first and fourth responses. Which interpretation is best?',
 'Abnormal decrement supporting a neuromuscular transmission disorder in the clinical context', [
 ('A normal physiological reduction requiring no further NMJ evaluation', 'A reproducible decrement above the conventional 10% threshold is abnormal under the usual protocol, provided technique, temperature and waveform stability are satisfactory.'),
 ('A result that specifically distinguishes autoimmune MG from every presynaptic syndrome', 'Low-frequency decrement can occur in MG and LEMS and in other settings; postexercise increment, phenotype and serology address the underlying disorder.'),
 ('A motor conduction-block criterion establishing acquired demyelinating neuropathy', 'RNS compares successive responses during repeated stimulation at one site, whereas a demyelinating block assessment compares appropriate proximal and distal nerve stimulation.')],
 [S('Measure Failure Across Repeated Stimuli', '**Low-frequency RNS**, commonly at 2–3 Hz, tests the stability of neuromuscular transmission. A conventional abnormal result is a reproducible decrement of at least about ==10%== under the specified laboratory protocol.',
    'Maintain adequate temperature, immobilization and supramaximal stimulation. Movement, changing activation and unstable baseline recording can produce misleading amplitude changes.',
    'Test clinically involved muscles. Facial or proximal recordings can improve yield when distal hand recordings are normal, particularly in an ocular-bulbar presentation.'),
  S('Interpret Sensitivity and Specificity', '**A positive decrement supports transmission failure rather than a unique etiology.** Combine the result with clinical findings, antibody tests and relevant postexercise testing.',
    'Sensitivity is lower in restricted ocular disease, and an unrevealing limited study does not exclude MG. Targeted jitter testing may be appropriate when suspicion remains high.',
    'A normal routine sensory study is expected in an isolated NMJ disorder, but coexisting neuropathy can complicate the overall electrodiagnostic picture. Document medications and laboratory instructions; do not independently stop essential therapy in a patient at respiratory risk simply to improve test yield.')], ['EDX','MG'], style='direct')

R.update({
 'SFEMG': ('Washington University Neuromuscular: MG diagnostic tests', 'https://neuromuscular.wustl.edu/mtime/mgdx.html'),
 'MGFA': ('MGFA provider manual: clinical classification', 'https://myasthenia.org/wp-content/uploads/Portals/0/Provider%20Manual_ibook%20version.pdf'),
 'ABN25': ('ABN autoimmune MG management guideline, 2025 update', 'https://doi.org/10.1136/pn-2025-004655'),
})

add('Myasthenia gravis: recognition and diagnosis', 'Jitter Testing After Nondiagnostic RNS',
 'A patient has repeatedly documented fatigable ptosis and diplopia, negative standard AChR/MuSK assays and normal routine distal-hand RNS. Which test is most useful next to assess neuromuscular transmission?',
 'Jitter testing in an appropriately selected clinically involved facial muscle', [
 ('Routine needle EMG of a distal leg muscle alone', 'Conventional needle EMG helps identify neurogenic or myopathic mimics, but does not have the same targeted sensitivity for transmission failure in a restricted ocular presentation.'),
 ('Repeat sensory conduction studies in the symptomatic distribution', 'Sensory studies help assess peripheral nerve disease, but an isolated postsynaptic NMJ disorder generally preserves sensory responses and requires a transmission-focused test.'),
 ('High-frequency stimulation of an unaffected distal hand muscle as the sole next test', 'High-frequency or postexercise testing is useful for presynaptic disease; the persistent ocular suspicion after a limited normal study is better addressed by appropriately selected jitter testing.')],
 [S('Measure Variability in Transmission', '**Single-fiber EMG or validated concentric-needle jitter testing** measures variation in the timing of muscle-fiber responses. Increased jitter and blocking support impaired neuromuscular transmission.',
    'Use muscle- and technique-specific reference values. Stimulated and voluntary recordings have different protocols, so a single universal microsecond cutoff should not be applied to every method.',
    'Test selection matters: a normal distal-hand study can be less informative when the clinical disorder is predominantly ocular. Temperature, activation stability, sampling and recent treatment influence interpretation.'),
  S('Sensitive Does Not Mean Etiologically Specific', '**Abnormal jitter does not independently diagnose autoimmune MG.** Reinnervation, some myopathies, presynaptic disease and botulinum toxin exposure can produce abnormalities.',
    'Interpret the conventional EMG and clinical pattern alongside jitter, antibody assays and history. An isolated borderline result in a patient with nonspecific fatigue has a different meaning from a marked abnormality in reproducible ocular fatigability.',
    'A technically adequate normal study in an appropriately weak muscle lowers the probability of transmission failure, but does not justify an absolute exclusion from an inadequately sampled or treated case. Confirm the diagnosis before committing a seronegative patient to prolonged immune treatment, and reassess structural, mitochondrial or congenital alternatives when the pattern remains discordant.')], ['EDX','SFEMG','MG'])

add('Myasthenia gravis: recognition and diagnosis', 'Ice-Pack Testing for Ptosis',
 'An adult has fluctuating unilateral ptosis with normal pupils. After an ice pack is applied to the closed eyelid for two minutes, the lid position improves objectively by 3 mm. Which interpretation is most appropriate?',
 'The result supports ocular MG but requires integration with the examination and confirmatory assessment', [
 ('The result establishes the antibody subgroup and removes the need for serology', 'Cooling may improve myasthenic ptosis, but cannot identify AChR, MuSK or another antibody subgroup or provide the same information as validated serology.'),
 ('The result favors a fixed aponeurotic ptosis over impaired transmission', 'Aponeurotic ptosis is an important structural differential, but clear reversible improvement after cooling is more supportive of a myasthenic mechanism in this clinical context.'),
 ('The result establishes that the disease is permanently restricted to ocular muscles', 'A positive ocular bedside test addresses the current ptosis, not the future risk of generalization; bulbar, limb and respiratory assessment remains necessary.')],
 [S('A Practical Supportive Bedside Test', '**Cooling can transiently improve myasthenic ptosis.** Measure lid position before and after a standardized short application, protecting skin and avoiding pressure on the globe.',
    'A commonly used positive criterion is improvement of about ==2 mm or more==, but protocols and baseline severity affect performance. Document an objective change rather than a vague impression.',
    'The test is most useful when ptosis is present. Its interpretation is less straightforward for isolated diplopia, and a negative result does not exclude all ocular MG.'),
  S('Keep the Differential and Disease Extent in View', '**Fatigability, pupil examination and ocular-movement pattern** help distinguish MG from cranial neuropathy, restrictive orbitopathy and fixed muscle or eyelid disease.',
    'Pain, anisocoria, an acute focal nerve pattern or other concerning signs require appropriate urgent investigation. A bedside test must not distract from an aneurysmal or other structural emergency.',
    'Use antibody testing and selected electrophysiology according to the overall probability. Ask about swallowing, chewing, speech, neck and limb function and breathing. Ocular symptoms can precede generalization; neither a positive ice test nor a normal limb examination predicts permanent ocular restriction.')], ['MG','SFEMG'])

add('Myasthenia gravis: recognition and diagnosis', 'Thymic Imaging in Autoimmune MG',
 'A 45-year-old with newly confirmed AChR-positive generalized MG has no chest symptoms and a normal chest radiograph. Which investigation should assess associated thymic disease?',
 'Cross-sectional thoracic imaging with CT, or MRI when appropriate', [
 ('Repeat chest radiography in one year if symptoms develop', 'Radiography can show a large mediastinal lesion but cannot reliably exclude thymoma; absence of chest symptoms does not remove the need for adequate thymic assessment.'),
 ('Whole-body FDG-PET as the routine initial thymic screening test', 'PET may help selected tumor evaluation, but is not the usual first-line screening replacement for anatomical thoracic CT or MRI in confirmed MG.'),
 ('AChR antibody-titer surveillance to determine whether imaging is needed', 'Antibody levels can inform the autoimmune context but do not reliably exclude a thymic tumor; imaging is not contingent on a particular titer trajectory.')],
 [S('Look for a Clinically Silent Thymoma', '**Thymoma may be asymptomatic**, so a normal chest history and radiograph are insufficient to exclude it. Thoracic CT is commonly used; MRI is an alternative or problem-solving study when appropriate.',
    'Imaging assesses a mediastinal mass and helps distinguish other thymic appearances. Thymic hyperplasia and thymoma have different implications and should not be treated as synonymous.',
    'Thyroid and other autoimmune associations can also be relevant, but their evaluation does not replace investigation of the thymus.'),
  S('Separate Oncologic and Immunologic Indications', '**A thymoma requires multidisciplinary tumor assessment**, with surgery when indicated by resectability and the patient’s clinical condition. Stabilize significant MG before an elective operation.',
    'The immunologic benefit of thymectomy in selected nonthymomatous AChR-positive generalized disease is a separate evidence-based indication. Its age, phenotype and timing considerations should not be confused with treating a tumor.',
    'Thymectomy is not an immediate rescue for crisis, and improvement in autoimmune disease can be delayed. Continue appropriate perioperative medication, respiratory planning and follow-up. Antibody subgroup, comorbidity and operative risk inform decisions when no tumor is present; do not assume that every seronegative or MuSK-positive patient gains the same benefit.')], ['CONS','SYND','MG'])

add('Myasthenia gravis: recognition and diagnosis', 'MGFA Clinical Class and Bulbar Severity',
 'A patient with MG has severe dysphagia requiring a feeding tube and predominantly bulbar weakness, but has not required intubation. Which MGFA clinical class best fits?',
 'Class IVb', [
 ('Class IIIb', 'Class IIIb denotes moderate generalized disease with predominantly oropharyngeal/respiratory involvement; severe bulbar disease requiring tube feeding without intubation belongs to IVb.'),
 ('Class IVa', 'Class IVa denotes severe generalized disease with predominantly limb or axial involvement; the severe bulbar predominance here places the patient in the b subclass.'),
 ('Class V', 'Class V is defined by intubation outside routine postoperative management in the standard MGFA clinical classification; a feeding tube without intubation is specifically IVb.')],
 [S('Classify Distribution and Severity', '**MGFA clinical classes** describe current clinical severity and distribution. Ocular weakness can accompany generalized classes, and the worst affected nonocular domain determines the generalized category.',
    'The a subclasses emphasize limb/axial involvement, whereas b subclasses emphasize oropharyngeal/respiratory involvement. Assess function directly rather than inferring severity from antibody concentration.',
    'Feeding-tube dependence without intubation is specifically included in IVb. Routine postoperative intubation does not, by itself, change the clinical class to V.'),
  S('Do Not Confuse a Class With a Treatment Goal', '**Clinical class is different from postintervention status**, minimal manifestations or remission. The MG-ADL and other scales serve complementary longitudinal purposes and are not interchangeable labels.',
    'A patient can deteriorate urgently within a class. Weak cough, secretion difficulty or falling ventilatory reserve needs action before an intubation-based category is reached.',
    'Document bulbar, respiratory, axial and limb findings with serial functional measures. Clinical response and medication adverse effects guide treatment adjustment; a class number alone does not specify one mandatory drug or determine whether the patient can safely remain outside monitored care.')], ['MGFA','CONS'], style='direct',
 table=(['Class','Clinical framework'],[
 ['I','Ocular weakness only; eye closure weakness may occur'],
 ['II','Mild generalized weakness; a limb/axial, b bulbar/respiratory predominance'],
 ['III','Moderate generalized weakness; a/b distribution subclasses'],
 ['IV','Severe generalized weakness; a/b subclasses; feeding tube without intubation is IVb'],
 ['V','Intubation, except routine postoperative management']]))

R['PYR'] = ('MESTINON pyridostigmine prescribing information', 'https://www.dailymed.nlm.nih.gov/dailymed/getFile.cfm?setid=a851795e-b7a8-40c3-9922-5e79d3eb4d92&type=pdf')

add('Myasthenia gravis: long-term treatment', 'Pyridostigmine Is Symptomatic Therapy',
 'An adult with newly diagnosed mild generalized MG has no significant bulbar or respiratory involvement. Which medicine is used for rapid symptomatic improvement by reversible acetylcholinesterase inhibition?',
 'Pyridostigmine', [
 ('Amifampridine', 'Amifampridine increases presynaptic acetylcholine release through potassium-channel blockade and is a principal symptomatic treatment for LEMS, not the acetylcholinesterase inhibitor requested here.'),
 ('Prednisolone', 'Prednisolone provides immune treatment for MG with a slower clinical course and possible initial worsening; its action is not reversible acetylcholinesterase inhibition.'),
 ('Azathioprine', 'Azathioprine is a delayed-onset steroid-sparing immunosuppressant used in selected MG patients; it does not provide the rapid synaptic symptomatic effect described.')],
 [S('Increase Acetylcholine Availability', '**Pyridostigmine prolongs acetylcholine action** at the NMJ and can improve strength within a dose interval. It treats symptoms rather than eliminating the autoimmune process.',
    'A common adult starting approach is ==30 mg three or four times daily==, titrated to benefit and tolerability. Individualize timing to activities and meals; a rigid escalating dose is not a substitute for reassessing disease control.',
    'Patients with significant bulbar or respiratory weakness require urgent severity-directed care. Increasing oral symptomatic medication alone does not treat an impending crisis.'),
  S('Recognize Cholinergic Adverse Effects', '**Diarrhea, abdominal cramps, salivation, sweating and bradycardia** reflect muscarinic effects; excessive exposure can also cause fasciculation and weakness.',
    'Mechanical intestinal or urinary obstruction is a contraindication. Use caution with asthma and clinically important bradyarrhythmia; renal impairment can require lower individualized doses.',
    'Review dose-related symptoms and objective strength before assuming every decline is autoimmune worsening. Persistent functional weakness despite tolerated dosing warrants immune-treatment assessment. MuSK-associated disease can respond less well or tolerate treatment poorly. Antimuscarinic symptom treatment does not remove nicotinic toxicity or justify continued excessive dosing; the overall clinical and respiratory state remains the priority.')], ['PYR','ABN25','CONS'], style='direct')

add('Myasthenia gravis: long-term treatment', 'Functionally Limiting Ocular MG',
 'A patient with confirmed ocular MG has persistent disabling diplopia despite an adequate tolerated pyridostigmine trial. There is no respiratory or bulbar involvement. Which immune-treatment approach is generally recommended initially?',
 'Introduce corticosteroid therapy with an individualized low-dose escalation and monitoring plan', [
 ('Begin maintenance plasma exchange as the usual initial outpatient immune strategy', 'Exchange provides rapid short-term treatment for selected severe exacerbations and refractory situations, but is not the usual initial immune strategy for stable isolated ocular symptoms.'),
 ('Begin azathioprine alone and expect ocular improvement within several days', 'Azathioprine can be a steroid-sparing option when needed, but its delayed onset makes it unsuitable for an expectation of rapid response over days.'),
 ('Begin complement inhibition as the usual initial treatment for isolated ocular MG', 'Complement-directed agents have specific generalized-MG indications and safety requirements; those data do not establish them as routine first-line treatment for isolated ocular disease.')],
 [S('Treat Functional Limitation', '**Troublesome ptosis or ophthalmoparesis despite acetylcholinesterase inhibition** can justify immunotherapy. International consensus recommends corticosteroids as the initial immune agent in this setting.',
    'Assess the effect on reading, mobility, work and driving rather than treating an antibody titer. Reconsider the diagnosis when eye movements are fixed or restrictive, or the clinical response is discordant.',
    'A low starting dose with gradual escalation may improve tolerability and reduce early worsening risk in a stable outpatient. The optimal schedule is individualized rather than a single universally proven regimen.'),
  S('Balance Benefit and Toxicity', '**Use the lowest effective exposure** and monitor glucose, BP, weight, mood, infection and bone risk. Significant bulbar or respiratory disease changes the setting and may require rapid rescue therapy.',
    'If steroids are contraindicated, poorly tolerated or insufficient, consider an appropriate steroid-sparing agent with counseling about delayed onset and laboratory monitoring.',
    'Support diplopia temporarily with selected occlusion or optical measures where appropriate, and reassess for generalization. Established symptomatic benefit and immune control are different outcomes. Evidence for ocular therapy includes small trials and consensus; do not claim that corticosteroids guarantee prevention of future generalization in every patient.')], ['CONS','ABN25','MG'])

R.update({
 'CONS16': ('International consensus guidance for MG, 2016: short-term rescue and steroid precautions', 'https://doi.org/10.1212/WNL.0000000000002790'),
 'MGTX': ('MGTX randomized trial of thymectomy, 2016', 'https://doi.org/10.1056/NEJMoa1602489'),
 'AZA': ('US IMURAN prescribing information, 2024', 'https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/016324s040lbl.pdf'),
 'CPIC': ('CPIC thiopurine dosing by TPMT/NUDT15 genotype: 2025 update', 'https://doi.org/10.1002/cpt.70209'),
 'MAL25': ('Malaysian Society of Neurosciences MG consensus statement, 2025', 'https://www.neuro.org.my/assets/guideline/Myasthenia%20Gravis%20%28MG%29%20Physician%20Booklet_A5_68pp_VER3_3mm_REV2.pdf'),
})

add('Myasthenia gravis: long-term treatment', 'Corticosteroid Initiation in Significant Bulbar MG',
 'An untreated patient with generalized MG has marked dysphagia, a weak cough and declining respiratory reserve. Long-term corticosteroid therapy is planned. Which approach best addresses the early treatment risk?',
 'Admit for airway monitoring and rapid IVIG or exchange therapy, introducing steroids with an appropriate monitored plan', [
 ('Start a full oral steroid dose at home and reassess after two weeks', 'High-dose steroids can transiently worsen MG, and this patient already has airway-related features; outpatient delayed reassessment is unsuitable despite the long-term indication.'),
 ('Start azathioprine alone and defer rapid treatment until its effect is evident', 'Azathioprine can reduce long-term steroid requirements but acts over months; it cannot protect a patient with evolving bulbar and respiratory weakness during that interval.'),
 ('Use gradual outpatient steroid escalation with pyridostigmine as the sole bridge', 'Gradual escalation can be suitable for stable milder disease, but does not provide sufficient monitoring or rapid immune treatment for the supplied high-risk presentation.')],
 [S('Initial Worsening Is Clinically Important', '**Corticosteroids can transiently exacerbate myasthenic weakness**, particularly when substantial bulbar or generalized disease is present. This risk does not negate their long-term immune benefit.',
    'Assess secretion handling, swallowing, cough and ventilation before choosing the starting setting and regimen. A normal oxygen saturation does not establish adequate ventilatory reserve.',
    'Stable mild disease may be treated through gradual outpatient escalation, whereas severe or rapidly evolving bulbar/respiratory involvement needs a monitored inpatient approach.'),
  S('Bridge the Delay in Immune Control', '**IVIG or plasma exchange provides a faster short-term effect** and may be given before or alongside carefully timed steroid introduction. In selected high-risk cases, allow rescue therapy to begin working before escalating steroids.',
    'Choice depends on hemodynamics, access, renal and thrombotic risks, infection and local expertise. Intubation decisions remain clinical and should not wait for an immunotherapy response.',
    'Plan the longer course with objective functional assessment and steroid toxicity prevention. Glucose, BP, mood, bone and infection risks require monitoring. Neither a brief improvement after pyridostigmine nor initiation of a steroid-sparing agent removes the need for serial bulbar and respiratory review during early treatment.')], ['CONS16','ABN25','MAL25'])

add('Myasthenia gravis: long-term treatment', 'Azathioprine and Pharmacogenetic Safety',
 'A patient starting azathioprine for steroid-dependent MG has normal TPMT and NUDT15 results. Which monitoring plan remains appropriate?',
 'Serial CBC with platelets and liver tests, with closer checks during initiation and dose changes', [
 ('Liver tests alone because normal genotypes exclude marrow toxicity', 'Normal tested alleles reduce some inherited risk but do not exclude myelosuppression, drug interactions or acquired toxicity; CBC monitoring is still essential.'),
 ('CBC only after fever, bruising or oral ulceration develops', 'These symptoms require prompt assessment, but asymptomatic cytopenia can develop first; scheduled laboratory surveillance should not wait for clinical toxicity.'),
 ('Thiopurine metabolite levels as a substitute for blood counts', 'Metabolite measurements can answer selected adherence or toxicity questions, but do not replace CBC and organ-safety monitoring during azathioprine therapy.')],
 [S('Delayed Steroid-Sparing Benefit', '**Azathioprine is a thiopurine immunosuppressant** used in selected MG patients needing longer-term steroid reduction. Clinical benefit commonly takes months, so it is not rescue treatment for crisis.',
    'A common adult approach begins at 50 mg/day and titrates toward approximately ==2–3 mg/kg/day== if appropriate and tolerated. Adjust to the patient, pharmacogenetic result, interactions and laboratory trends.',
    'Obtain baseline CBC, liver and renal assessment and use TPMT/NUDT15 information according to local practice. Reduced activity can require substantial dose adjustment or an alternative agent.'),
  S('Genotyping Does Not Replace Surveillance', '**Monitor marrow and hepatic toxicity even with normal tested genotypes.** The US label describes CBC checks weekly during month one, twice monthly during months two and three, then monthly or more often when clinically needed.',
    'Check the local specialty protocol for liver-test timing and subsequent stable monitoring. Explain infection precautions and the importance of reporting bruising, fever or other toxicity symptoms.',
    'Allopurinol and febuxostat inhibit a pathway of thiopurine inactivation and can cause serious toxicity with usual azathioprine dosing. Reconcile medications before initiation and dose changes; any deliberate combination requires specialist dose management rather than an automatic standard regimen. Review long-term malignancy/skin risks and reproductive plans in shared decisions.')], ['AZA','CPIC','MAL25'], style='direct')

add('Myasthenia gravis: long-term treatment', 'Thymectomy Evidence in Nonthymomatous MG',
 'A 32-year-old has AChR-positive generalized MG of two years duration, no thymoma and persistent immunotherapy requirements. Which statement best describes the rationale for thymectomy?',
 'It can improve longer-term disease control and reduce prednisone requirements in this evidence-supported population', [
 ('It is mainly an immediate rescue treatment for severe weakness', 'Surgery does not substitute for IVIG or exchange during crisis; its autoimmune benefit develops over time, and significant weakness should be stabilized before an elective procedure.'),
 ('It is indicated only if imaging demonstrates a thymoma', 'Thymoma is a separate oncologic indication; randomized evidence also supports an immune benefit in selected nonthymomatous AChR-positive generalized disease.'),
 ('Its benefit is equally established for isolated ocular, MuSK-positive and AChR-positive generalized disease', 'These groups were not interchangeable in MGTX; extrapolation to ocular or MuSK disease cannot be presented as the same randomized evidence.')],
 [S('What MGTX Tested', '**MGTX compared thymectomy plus prednisone with prednisone alone** in nonthymomatous AChR-positive generalized MG. Its enrolled population was aged 18–65 years, with disease duration under five years and MGFA II–IV disease.',
    'The study demonstrated improved clinical measures and reduced steroid requirements over follow-up. It did not test surgery as an acute rescue, nor establish benefit for every antibody subgroup or phenotype.',
    'Distinguish trial eligibility from the strength of a recommendation for an individual age group. The 2020 international update particularly supported early consideration in ages 18–50.'),
  S('Apply Evidence to an Elective Decision', '**The 2025 ABN update recommends early thymectomy below 50 years in AChR MG and consideration at 50–65**, integrating comorbidity, disease course and patient preference.',
    'Assess operative and respiratory risk and optimize MG before surgery. Discuss surgical approach and expertise without assuming every minimally invasive technique has identical randomized comparative evidence.',
    'A thymoma requires tumor-directed multidisciplinary assessment regardless of whether the patient matches the nonthymomatous trial population. Continue postoperative clinical and medication review; thymectomy does not guarantee remission or allow immediate unmonitored withdrawal of immune treatment.')], ['MGTX','CONS','ABN25'])

R['RTX'] = ('US rituximab biosimilar prescribing information: HBV and infection precautions, 2026', 'https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/761140s005lbl.pdf')

add('Myasthenia gravis: long-term treatment', 'Early Rituximab Consideration in MuSK MG',
 'A patient with MuSK-positive generalized MG continues to have important bulbar weakness despite initial corticosteroid treatment and tolerates pyridostigmine poorly. After stabilization, which longer-term strategy has particular consensus support for this subgroup?',
 'Consider rituximab early with appropriate infection and immunoglobulin assessment', [
 ('Increase pyridostigmine until adverse muscarinic effects define the dose limit', 'Symptomatic titration can help selected MG patients, but MuSK disease often tolerates it poorly; persisting bulbar disease needs immune control rather than escalating through toxicity.'),
 ('Proceed to nonthymomatous thymectomy as the preferred subgroup-specific intervention', 'The strongest randomized nonthymomatous thymectomy evidence concerns AChR-positive generalized disease, not a comparable established benefit in MuSK MG.'),
 ('Choose terminal complement inhibition because MuSK antibodies principally cause complement injury', 'Complement inhibitors have antibody-specific evidence and indications; predominant MuSK IgG4 biology does not justify selecting them through an AChR-style complement-injury assumption.')],
 [S('A Subgroup-Specific Immune Strategy', '**Rituximab depletes CD20-positive B cells**, reducing an important source of ongoing antibody-producing immune activity. It is not an acetylcholinesterase inhibitor or an immediate substitute for airway support.',
    'The 2020 international update supports early consideration in MuSK MG with an unsatisfactory response to initial immunotherapy; later specialty guidance also emphasizes its early role in this phenotype.',
    'The evidence base includes observational experience and differs from the randomized evidence for some newer therapies. Do not describe a guaranteed response, identical benefit across all antibody groups or a universal licensed MG indication.'),
  S('Screen and Follow Beyond the Infusion', '**Assess hepatitis B with HBsAg and anti-HBc**, baseline immunoglobulins, infection history, vaccination needs and relevant laboratory data. Prior resolved HBV infection can still confer reactivation risk.',
    'Coordinate antiviral prevention and follow-up with an experienced service when indicated. Monitor infusion reactions, infections and clinically meaningful hypogammaglobulinemia; vaccination planning is best addressed before B-cell depletion where feasible.',
    'Specialist regimens vary, including 1 g IV on days 1 and 15 or alternative schedules; follow the selected protocol rather than assuming one schedule applies to every autoimmune condition. Assess objective bulbar, respiratory and functional outcomes over time, and provide rapid rescue separately when severe weakness cannot wait for longer-term immune control.')], ['CONS','SYND','RTX'])

R.update({
 'C5': ('US ULTOMIRIS/ravulizumab prescribing information, 2026', 'https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/761108s046lbl.pdf'),
 'MEN': ('CDC clinical guidance: meningococcal risk during complement inhibition, 2026', 'https://www.cdc.gov/meningococcal/hcp/clinical-guidance/complement-inhibitor.html'),
 'ROZ': ('US RYSTIGGO/rozanolixizumab prescribing information', 'https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/761286s007lbl.pdf'),
})

add('Myasthenia gravis: long-term treatment', 'Meningococcal Risk With C5 Inhibition',
 'An adult with AChR-positive generalized MG is scheduled to begin ravulizumab. Treatment can safely wait while preventive measures are arranged. Which plan is most appropriate?',
 'Update MenACWY and MenB vaccination before treatment and counsel about persistent infection risk', [
 ('Give MenACWY alone because serogroup B coverage is unnecessary during complement inhibition', 'Both vaccine categories are recommended for complement-inhibitor recipients; protection from MenACWY does not cover all relevant meningococcal risks.'),
 ('Use antibiotic prophylaxis as a replacement for vaccination throughout therapy', 'Antibiotics may reduce risk and are required in some urgent-start circumstances, but do not replace the recommended vaccine strategy and do not eliminate breakthrough infection.'),
 ('Complete vaccination and then manage subsequent meningococcal symptoms as ordinary low-risk illness', 'Vaccination is important but incompletely protective during terminal complement blockade; compatible symptoms still require urgent assessment even after full vaccination.')],
 [S('Mechanism Creates a Specific Infection Risk', '**Ravulizumab blocks terminal complement C5**, reducing an important effector mechanism in AChR-antibody MG. The same blockade impairs defense against invasive meningococcal infection.',
    'The 2026 US MG indication is adult AChR-positive generalized disease. Do not transfer this indication automatically to isolated ocular or MuSK-positive disease.',
    'Meningococcal illness can develop despite vaccination or prophylaxis. Explain fever, headache, neck stiffness, rash and systemic illness as reasons for immediate medical assessment rather than reassurance from a vaccine history.'),
  S('Vaccination and Urgent-Start Planning', '**Complete or update MenACWY and MenB vaccination ideally at least two weeks before treatment**, following the current risk-based schedule and boosters.',
    'If delaying treatment is clinically unsafe, follow the product label for prompt vaccination and antibacterial prophylaxis. Additional prophylaxis during ongoing treatment can be considered according to specialist and local guidance.',
    'Check for unresolved serious meningococcal infection before initiation and maintain a clear emergency pathway. Assess clinical response, infection and other adverse effects over time. Complement inhibition is disease-directed treatment, but acute airway support and rapid rescue decisions remain separate; an evolving crisis must not wait for elective preventive scheduling.')], ['C5','MEN'])

add('Myasthenia gravis: long-term treatment', 'FcRn Blockade and IgG Recycling',
 'Which mechanism explains the effect of FcRn blockers such as rozanolixizumab in autoimmune generalized MG?',
 'Reduced recycling and increased degradation of circulating IgG', [
 ('Depletion of CD20-positive B cells', 'This describes rituximab and related B-cell therapies; FcRn blockade alters IgG handling rather than directly depleting CD20-positive cells.'),
 ('Inhibition of cleavage of complement C5', 'Terminal complement inhibitors act downstream on complement-mediated injury; their mechanism and meningococcal precautions differ from FcRn-mediated IgG reduction.'),
 ('Inhibition of acetylcholinesterase at the motor end plate', 'Pyridostigmine provides symptomatic synaptic benefit by slowing acetylcholine breakdown; it does not lower pathogenic IgG through altered recycling.')],
 [S('Lower IgG Through a Salvage Pathway', '**FcRn normally rescues IgG from intracellular degradation.** Blocking this receptor lowers circulating IgG, including pathogenic autoantibodies, without directly correcting every cause of weakness.',
    'The mechanism differs from B-cell depletion, terminal complement blockade and symptomatic acetylcholinesterase inhibition. Drugs sharing an MG indication are therefore not interchangeable in mechanism or monitoring.',
    'Antibody subgroup, indication, route and treatment-cycle schedule are product specific. Evidence for one FcRn drug cannot automatically be used as the approved indication or exact regimen of another.'),
  S('Infection, Vaccines and Treatment Assessment', '**Assess active infection and vaccination needs** before treatment. Because IgG falls transiently, live vaccines are generally not recommended during the treatment period specified by the product instructions.',
    'Monitor hypersensitivity, infection and relevant formulation-specific adverse effects. Rozanolixizumab commonly causes headache, and aseptic meningitis is an important recognized warning; a severe headache still requires clinical evaluation for competing causes.',
    'Use objective symptoms and function to determine response and subsequent treatment planning. A biochemical IgG decline is not itself proof that every symptom is myasthenic or that the patient has achieved remission. Concomitant immune therapies and immunoglobulin exposure require specialist coordination rather than unplanned stacking of treatments with overlapping effects.')], ['ROZ','SYND'], style='direct')

add('Myasthenia gravis: long-term treatment', 'Rozanolixizumab Indication and Cycle',
 'An 82-kg adult with MuSK-positive generalized MG is prescribed rozanolixizumab under its US label. Which regimen matches the cited prescribing information?',
 '560 mg by subcutaneous infusion once weekly for six weeks', [
 ('420 mg by subcutaneous infusion once weekly for six weeks', 'This dose corresponds to the under-50-kg weight band in the cited label; the 82-kg patient belongs to the 50-to-under-100-kg group.'),
 ('840 mg by subcutaneous infusion once weekly for six weeks', 'This dose corresponds to patients weighing at least 100 kg, rather than the supplied 82-kg weight.'),
 ('560 mg by subcutaneous infusion once weekly for four weeks', 'The weight-band dose is correct, but the labeled rozanolixizumab cycle contains six weekly doses; a different FcRn product’s cycle should not be copied.')],
 [S('Read the Antibody and Weight Requirements', '**The cited US RYSTIGGO label includes adult generalized MG with AChR or MuSK antibodies.** This is a product-specific indication rather than a statement that every targeted MG drug covers both groups.',
    'The 82-kg patient falls in the ==50 to under 100 kg== band and receives ==560 mg weekly for six weeks==. Administration is by subcutaneous infusion using the specified equipment and preparation procedure.',
    'The label’s other bands are 420 mg below 50 kg and 840 mg at 100 kg or above. Do not substitute an infusion dose from a different weight group or convert the regimen to an unrelated fixed four-dose cycle.'),
  S('Plan Subsequent Cycles Clinically', '**Further cycles depend on clinical evaluation.** In the cited label, the safety of starting another cycle sooner than 63 days after the previous cycle began has not been established.',
    'Review infection and age-appropriate immunizations before a new cycle, with attention to the live-vaccine restriction during treatment. Monitor headache, hypersensitivity and possible aseptic meningitis.',
    'Assess MG symptoms, function and respiratory/bulbar status rather than scheduling repeat cycles from the antibody titer alone. The US label defines the example here; local approval, availability and instructions must be checked separately. A routine outpatient cycle is not a substitute for airway management in an acute crisis.')], ['ROZ','SYND'], style='direct')

R.update({
 'PREG': ('AGG recommendations for MG in pregnancy, 2021', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC8654508/'),
 'EMERG': ('MGFA emergency management guidance', 'https://myasthenia.org/understanding-mg/learn-more-about-mg-treatments/mg-brochures/emergency-management-for-first-responders/'),
 'CRISIS': ('Specialty review: myasthenic crisis, 2023', 'https://doi.org/10.1002/mus.27832'),
})

add('Myasthenia gravis: long-term treatment', 'Transient Neonatal Myasthenia',
 'A term infant develops hypotonia, a weak cry and poor sucking during the first two days after birth. The mother has autoimmune MG that was clinically well controlled during pregnancy. Which mechanism best explains the suspected neonatal syndrome?',
 'Transplacental transfer of maternal pathogenic IgG', [
 ('Inheritance of the mother’s acquired postsynaptic autoimmune defect as a Mendelian trait', 'Autoimmune MG is not transmitted as the same Mendelian defect; inherited congenital myasthenic syndromes instead arise from specific genetic abnormalities of transmission.'),
 ('Persistent direct neuromuscular blockade from maternal oral pyridostigmine as the usual mechanism', 'Medication exposure belongs in neonatal assessment, but transient neonatal MG principally reflects transferred maternal antibodies rather than this being the usual pyridostigmine toxicity mechanism.'),
 ('Primary neonatal production of pathogenic antibodies requiring permanent immunosuppression', 'The typical syndrome follows passive maternal antibody transfer and resolves as those antibodies clear; persistent disease should prompt reassessment for other neonatal or genetic causes.')],
 [S('Passive Autoimmunity Can Occur Despite Maternal Control', '**Maternal IgG crosses the placenta** and can temporarily impair neonatal neuromuscular transmission. Good maternal symptom control does not exclude neonatal weakness.',
    'Poor feeding, weak cry, hypotonia and respiratory difficulty require prompt neonatal assessment. Evaluate sepsis, metabolic disease, central illness and congenital neuromuscular disorders as competing or additional causes.',
    'Provide feeding and respiratory support as needed; selected infants receive specialist-directed acetylcholinesterase inhibition. The usual course improves over weeks as maternal antibodies disappear.'),
  S('Plan Pregnancy and Delivery Prospectively', '**Coordinate neurology, obstetrics, anesthesia and neonatal care.** Review medications before conception, maintain disease control and arrange neonatal observation after delivery.',
    'Oral pyridostigmine and appropriately selected corticosteroid treatment can be used under supervision. Mycophenolate and methotrexate are incompatible with pregnancy; withdrawal, substitution and contraception/washout planning require a specialist plan rather than abrupt unmonitored cessation.',
    'Magnesium sulfate can significantly worsen transmission in MG and should not be used as an automatic obstetric default; severe preeclampsia/eclampsia needs urgent individualized multidisciplinary management. Vaginal delivery is often feasible, with support if skeletal-muscle fatigue limits the second stage. Monitor maternal symptoms postpartum as well as during gestation.')], ['CONS16','PREG','CMS'])

add('Myasthenic crisis and treatment hazards', 'Recognizing Impending Myasthenic Crisis',
 'A patient with MG and a respiratory infection reports little change in limb strength but now cannot finish sentences, coughs weakly and repeatedly chokes on saliva. Oxygen saturation is 98% on room air. What is the best next step?',
 'Urgent monitored assessment of airway protection and ventilation with ICU-level escalation as indicated', [
 ('Increase oral pyridostigmine and arrange routine outpatient review', 'Dose adjustment can help stable symptoms, but weak cough and secretion difficulty indicate potential airway compromise that cannot safely await routine follow-up.'),
 ('Treat the infection and use pulse oximetry alone to determine whether weakness requires escalation', 'Infection treatment is essential, but oxygen saturation may remain normal despite failing ventilation or airway protection; the bulbar findings require parallel urgent assessment.'),
 ('Start a delayed-onset steroid-sparing agent as the immediate solution to the bulbar decline', 'Long-term immunotherapy may be needed, but an agent acting over months does not address the current respiratory and aspiration risk.')],
 [S('Bulbar Failure Can Precede Obvious Desaturation', '**Impending crisis is a clinical trajectory**, not a pulse-oximetry threshold. Inability to manage saliva, weak cough, dysarthria and progressive breathlessness can signal danger before severe hypoxemia.',
    'Assess swallowing, secretion clearance, work of breathing, neck strength and ability to speak. Serial respiratory mechanics complement this examination rather than replacing it.',
    'Limited limb weakness does not establish safety. Bulbar and respiratory muscles can be disproportionately affected, particularly in some antibody phenotypes.'),
  S('Protect the Airway While Treating the Trigger', '**Arrange monitored care and an anticipatory airway plan**, with neurology, critical care and experienced airway input. Avoid oral intake when swallowing is unsafe and manage aspiration and secretions.',
    'Look for infection, medication changes, missed therapy, surgery or other precipitating stress. Treat the cause while planning rapid MG therapy such as IVIG or exchange when indicated.',
    'Noninvasive ventilation is suitable only in selected patients who can protect the airway and clear secretions, with close monitoring and rapid access to intubation. Do not let a trial delay intubation in worsening bulbar failure. Completion of a diagnostic test or the onset of an immune-treatment effect must not become a prerequisite for life-saving respiratory support.')], ['EMERG','CRISIS','CONS16'])

add('Myasthenic crisis and treatment hazards', 'Respiratory Mechanics and Airway Timing',
 'During monitored treatment of MG, vital capacity falls from 28 to 17 mL/kg over four hours. The patient develops paradoxical breathing and cannot clear secretions; oxygen saturation remains 97%. Which respiratory strategy is most appropriate?',
 'Arrange timely endotracheal intubation rather than waiting for desaturation or exhaustion', [
 ('Continue observation until pulse oximetry demonstrates substantial hypoxemia', 'Hypoxemia can be late in neuromuscular ventilatory failure; the rapid decline and secretion failure already indicate an unsafe trajectory.'),
 ('Use ward-based noninvasive ventilation despite ineffective secretion clearance', 'Noninvasive support can help selected patients with preserved airway protection, but substantial secretion and bulbar failure make this proposed setting and strategy unsuitable.'),
 ('Repeat spirometry after rescue immunotherapy is completed before making the airway decision', 'Serial mechanics are useful, but treatment takes time to act and an unsafe airway cannot wait for an entire rescue course or another confirmatory measurement.')],
 [S('Use Numbers as Warning Signals', '**VC around or below 20 mL/kg** and inspiratory pressure weaker than about −30 cm H2O are concerning in the appropriate setting. A less negative inspiratory pressure means weaker force.',
    'These are warning values rather than mandatory universal intubation cutoffs. Bulbar dysfunction, poor seal, effort and measurement technique affect reliability.',
    'Trend, work of breathing, cough, aspiration risk and blood gases determine urgency. Hypercapnia can indicate advanced ventilatory compromise and should not be awaited before acting.'),
  S('Avoid an Emergency Airway After Exhaustion', '**Rapidly declining reserve with failed secretion clearance** favors elective controlled airway management over delayed rescue after collapse. In this stem, clinical deterioration independently reinforces the concerning VC.',
    'Selected nonhypercapnic patients with effective airway protection may benefit from closely supervised noninvasive support; frequent reassessment and an intubation plan remain essential.',
    'Ventilation supports the patient while immune treatment takes effect. Provide aspiration management, infection treatment, nutrition, thrombosis prevention and rehabilitation as appropriate. Extubation later requires improvement in cough, secretion handling and overall respiratory performance, not merely one satisfactory VC measurement.')], ['CRISIS','EMERG','MAL25'])

add('Myasthenic crisis and treatment hazards', 'Rapid Immune Therapy in Severe Exacerbation',
 'An adult with severe generalized MG has been stabilized in monitored care for bulbar and respiratory deterioration. Which statement best describes the established rapid immune-treatment options?',
 'IVIG or plasma exchange may be used, selected according to urgency, risks and feasibility', [
 ('Azathioprine and mycophenolate are equivalent substitutes for rapid rescue', 'Both can serve longer-term steroid-sparing roles, but their delayed onset makes them unsuitable replacements for a rapid treatment during severe exacerbation.'),
 ('Thymectomy should precede rapid immune treatment to correct the cause immediately', 'Thymectomy may improve selected long-term disease control or treat thymoma, but elective surgery requires stabilization and is not an immediate crisis rescue.'),
 ('A standard IVIG course should routinely be followed immediately by exchange in every case', 'Sequential treatment is not a universal default and exchange can remove infused immunoglobulin; assess response and individual circumstances before changing modalities.')],
 [S('Choose a Short-Term Bridge', '**IVIG and plasma exchange are established short-term therapies** for significant generalized exacerbation, crisis and selected perioperative or steroid-initiation situations.',
    'A common IVIG rescue course totals ==2 g/kg over 2–5 days==, although dose selection and local guidance vary. Assess thrombotic, renal, hemolytic and volume-related risks.',
    'Exchange commonly uses approximately four to five procedures, with the exact schedule individualized. Consider access, hemodynamic tolerance, anticoagulation, calcium and infection risks.'),
  S('Match the Modality to the Patient', '**Exchange may act faster and can be particularly useful in MuSK disease**, but this does not mean one modality is always best for every patient. Availability and comorbidity materially affect the choice.',
    'Continue respiratory and bulbar support independently of immune-treatment completion. Failure to improve immediately should prompt review of timing, complications, diagnosis and adequacy rather than automatic repetitive courses.',
    'Introduce or adjust sustained immune therapy with attention to initial steroid worsening. Rapid therapy is a bridge and does not by itself establish a long-term maintenance plan. Document objective strength, swallowing, ventilation and functional response so later decisions rest on clinical benefit rather than an assumed pharmacologic effect.')], ['CONS16','CRISIS','MAL25'])

R['CAUTION'] = ('MGFA cautionary drugs: strength of evidence and clinical context', 'https://myasthenia.org/living-with-mg/mg-emergency-preparedness/cautionary-drugs/')

add('Myasthenic crisis and treatment hazards', 'Fluoroquinolones and MG Worsening',
 'Which antibiotic carries a specific US boxed warning about exacerbating myasthenia gravis and should generally be avoided in a patient with known MG when an effective safer alternative is available?',
 'Ciprofloxacin', [
 ('Amoxicillin–clavulanate', 'This can be an appropriate infection-directed option and lacks the fluoroquinolone-specific boxed MG warning; selection still depends on allergy, organism and local susceptibility.'),
 ('Cefuroxime', 'A cephalosporin may be appropriate for selected infections and does not share the fluoroquinolone boxed MG warning; the infection site and microbiology remain essential.'),
 ('Doxycycline', 'Doxycycline can be selected for suitable infections and does not carry the fluoroquinolone-specific boxed MG warning; no antibiotic choice should be made without considering indication and individual tolerability.')],
 [S('Medication Review During Deterioration', '**Fluoroquinolones can impair neuromuscular transmission** and have a boxed warning for exacerbation in known MG. Review newly introduced drugs whenever weakness worsens.',
    'Macrolides, aminoglycosides and intravenous magnesium are other important caution categories, although the evidence, risk and clinical necessity differ among exposures.',
    'Sedatives, opioids and drugs with neuromuscular-blocking effects can further compromise ventilation or airway safety in a weak patient. The medication list should include nonprescription products and recent procedures.'),
  S('Treat Infection Without Creating Another Hazard', '**Infection itself can precipitate exacerbation or crisis.** Avoid delaying necessary antimicrobial treatment while debating medication risk; choose an effective lower-risk agent when feasible.',
    'Base therapy on the infection source, culture, severity, allergies, renal function and local resistance. A caution list is not proof that every reported association is an absolute contraindication.',
    'If a higher-risk drug is essential and alternatives are unsuitable, use an informed specialist plan with appropriate monitoring. Document timing, objective weakness and competing triggers rather than assuming causality from coincidence alone. New dysphagia, weak cough or respiratory decline requires urgent clinical assessment, not simply discontinuing a drug and waiting at home.')], ['CAUTION','EMERG'], style='direct')

add('Myasthenic crisis and treatment hazards', 'Pyridostigmine During Intubated Crisis',
 'A patient intubated for myasthenic crisis is receiving IVIG and has copious airway secretions while taking regular pyridostigmine. Which medication adjustment is generally appropriate during this phase?',
 'Temporarily withhold or substantially reduce pyridostigmine with specialist review, then reintroduce as recovery permits', [
 ('Increase pyridostigmine to clear the secretions and replace the need for IVIG', 'Pyridostigmine increases cholinergic secretions and does not replace immune rescue; escalation can worsen airway-management burden and toxicity.'),
 ('Continue the unchanged dose because stopping briefly causes irreversible loss of immune control', 'Pyridostigmine is symptomatic rather than immune therapy; in intubated crisis its secretion effects can justify temporary interruption without implying irreversible autoimmune deterioration.'),
 ('Discontinue all long-term MG therapy permanently once mechanical ventilation is started', 'Ventilation supports acute physiology but does not cure MG; longer-term treatment must be individualized and resumed or adjusted according to recovery and disease control.')],
 [S('Separate Symptom Treatment From Rescue', '**Acetylcholinesterase inhibitors increase acetylcholine and secretions.** During intubated crisis, temporary reduction or withholding commonly simplifies secretion management and avoids dose-related cholinergic effects.',
    'This does not mean pyridostigmine caused every crisis. Infection, inadequate disease control and other triggers remain important, and airway support plus rapid immune treatment continue.',
    'Consult the neuromuscular and intensive-care teams rather than applying an unqualified medication-stop rule to every nonintubated patient with mild symptoms.'),
  S('Reintroduce According to Clinical Recovery', '**Restart symptomatic treatment when strength and airway function improve**, often near the extubation period, using an individualized dose and assessment of secretion burden.',
    'Extubation readiness depends on cough, secretion handling, bulbar function, respiratory performance and the broader clinical course. Neither a pyridostigmine dose nor a single lung-volume measurement establishes readiness.',
    'Monitor bradycardia, diarrhea, abdominal cramps, fasciculation and excess salivation when restarting or titrating. Renal impairment can increase exposure and may require adjustment. A new decline after dosing should trigger reassessment for both toxicity and ongoing disease; routine intravenous diagnostic challenge is not necessary to resolve every uncertain episode.')], ['CRISIS','EMERG','PYR'])

add('Myasthenic crisis and treatment hazards', 'Cholinergic Toxicity After Dose Escalation',
 'After repeatedly increasing pyridostigmine, a patient develops worsening weakness accompanied by marked salivation, diarrhea, abdominal cramps, miosis, fasciculation and bradycardia. Which explanation is most likely?',
 'Excess acetylcholinesterase inhibition causing cholinergic toxicity', [
 ('Isolated autoimmune MG exacerbation', 'Autoimmune worsening can cause weakness and respiratory compromise, but the clustered muscarinic signs and fasciculation after dose escalation strongly suggest an additional toxic cholinergic mechanism.'),
 ('Steroid-induced myopathy', 'Steroid myopathy usually causes relatively painless proximal weakness without this acute secretory, gastrointestinal, pupillary and bradycardic syndrome linked to pyridostigmine escalation.'),
 ('Lambert-Eaton myasthenic syndrome', 'LEMS can cause proximal weakness and autonomic symptoms, but often dry mouth rather than cholinergic excess, and does not explain this dose-linked muscarinic cluster.')],
 [S('Muscarinic and Nicotinic Effects Coexist', '**Excess acetylcholine can paradoxically worsen strength** while producing muscarinic salivation, bronchial secretions, diarrhea, cramping, miosis and bradycardia.',
    'Fasciculation and weakness reflect nicotinic effects. Weakness alone cannot distinguish toxicity from MG activity; exposure history and the accompanying findings are crucial.',
    'Cholinergic crisis is uncommon in modern routine MG care, but clinically important toxicity must still be considered after excess dosing or impaired clearance.'),
  S('Stabilize Before Assigning the Entire Cause', '**Assess airway and ventilation urgently**, with monitored supportive care and withholding the offending exposure. Review renal function, dosing errors, overlapping preparations and other causes of deterioration.',
    'Atropine can treat significant muscarinic manifestations under appropriate supervision, but does not reverse nicotinic weakness. Clearing secretions pharmacologically does not establish restoration of respiratory muscle function.',
    'Do not give additional pyridostigmine reflexively or use a hazardous edrophonium challenge as the routine arbiter in respiratory distress. Autoimmune exacerbation or infection can coexist, so continue clinical reassessment and treat the supported underlying processes. Reintroduce an appropriate symptomatic regimen only after stabilization and a clear medication plan.')], ['PYR','CRISIS','MAL25'])

R.update({
 'LEMS': ('Lambert-Eaton myasthenic syndrome: diagnostic and cancer-screening review, 2018/2019', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6690495/'),
 'AMI': ('US FIRDAPSE/amifampridine prescribing information, revised July 2025', 'https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/208078s015lbl.pdf'),
 'CMSTX': ('Targeted therapies for congenital myasthenic syndromes: systematic review, 2019', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6436731/'),
})

add('Lambert-Eaton and congenital myasthenic syndromes', 'Presynaptic Facilitation in LEMS',
 'An older smoker has proximal leg weakness, dry mouth and depressed reflexes that briefly improve after contraction. Baseline CMAP is low and increases by 160% immediately after brief maximal exercise. Which diagnosis best fits?',
 'Lambert-Eaton myasthenic syndrome', [
 ('AChR-positive generalized myasthenia gravis', 'MG can cause proximal weakness and low-frequency decrement, but autonomic symptoms, depressed facilitating reflexes and a large postexercise increment favor presynaptic LEMS.'),
 ('Motor-predominant CIDP', 'CIDP can produce weakness and areflexia, but requires an appropriate demyelinating pattern rather than this striking exercise-related increment and autonomic phenotype.'),
 ('Inclusion body myositis', 'IBM can cause quadriceps weakness in older adults, but usually has a chronic characteristic muscle pattern without this presynaptic electrodiagnostic facilitation or autonomic syndrome.')],
 [S('Reduced Release With Exercise-Related Compensation', '**LEMS commonly involves antibodies to presynaptic P/Q-type calcium channels**, reducing acetylcholine release. Calcium accumulation during activation can transiently improve release and strength.',
    'Typical clues are proximal weakness, autonomic symptoms such as dry mouth and reduced tendon reflexes that facilitate after activation. Ocular and bulbar symptoms can occur, so their presence does not automatically establish MG.',
    'Electrodiagnostics combine low baseline motor responses, possible low-frequency decrement and substantial postexercise or high-frequency increment. Interpret percentages together with the actual baseline response and recording quality.'),
  S('Thresholds and Next Decisions', '**An increment exceeding 100% is the classic highly supportive pattern**; a threshold around 60% can improve sensitivity under validated protocols. A technically sound 160% increment fits either approach.',
    'Brief maximal exercise and immediate recording matter; delayed sampling can miss facilitation. Calcium-channel antibodies support a concordant syndrome but should not replace clinical and electrophysiological interpretation.',
    'Assess for associated small-cell lung cancer and provide symptomatic treatment, commonly amifampridine when suitable. Autoimmune nonparaneoplastic disease also occurs. Address mobility, falls and autonomic symptoms while the cancer investigation proceeds rather than treating this as an isolated laboratory finding.')], ['LEMS','EDX','SYND'])

add('Lambert-Eaton and congenital myasthenic syndromes', 'Cancer Surveillance After Negative Initial LEMS Imaging',
 'A 61-year-old smoker has confirmed LEMS. Initial thoracic CT shows no malignancy. Which next approach is most appropriate?',
 'Continue risk-directed cancer evaluation and scheduled surveillance rather than closing the cancer search', [
 ('Reclassify the syndrome as nonparaneoplastic permanently on the basis of the negative CT', 'Cancer can become detectable after neurologic onset; one negative study does not permanently establish nonparaneoplastic LEMS, particularly in a higher-risk smoker.'),
 ('Use the calcium-channel antibody concentration alone to determine whether imaging should be repeated', 'Antibody results support the syndrome but do not reliably exclude an occult tumor or replace risk- and time-directed imaging surveillance.'),
 ('Treat presumed small-cell lung cancer with chemotherapy before tissue or radiologic confirmation', 'Cancer treatment can improve paraneoplastic disease, but empirical chemotherapy is not justified solely by LEMS without an established malignancy and oncologic assessment.')],
 [S('Neurologic Disease May Precede Cancer Detection', '**Small-cell lung cancer is the key associated malignancy.** Age, smoking history, weight loss and other clinical features modify risk, but do not replace a proper initial evaluation.',
    'Thoracic CT is central to the search. Additional imaging, including FDG-PET in selected circumstances, depends on residual suspicion and specialist evaluation.',
    'A negative result is a time-specific observation, not proof that cancer will never emerge. Explain the surveillance plan clearly so follow-up is not lost after symptomatic improvement.'),
  S('A Scheduled, Risk-Adjusted Search', '**Common specialty recommendations repeat screening every 3–6 months for at least two years**, with the exact duration and intensity individualized to risk and findings.',
    'Reassess sooner for new systemic or respiratory symptoms, weight loss or suspicious imaging. Risk scores can help organize surveillance but should not override concerning clinical evidence.',
    'If cancer is identified, coordinate tissue diagnosis, staging and oncologic treatment with neurologic care. Continue symptomatic and, where needed, immune treatment for LEMS; improvement in strength does not establish absence of cancer. Support smoking cessation and function while avoiding unnecessary invasive procedures without a clinical indication.')], ['LEMS','SYND'])

add('Lambert-Eaton and congenital myasthenic syndromes', 'Amifampridine and Seizure History',
 'An adult with LEMS is being considered for amifampridine. Which history is a contraindication under the cited US FIRDAPSE label?',
 'A prior seizure disorder', [
 ('Stable mild renal impairment', 'Renal impairment requires a lower initial dose and careful titration under the label; it is not the same categorical contraindication as a history of seizures.'),
 ('Known NAT2 poor-metabolizer status', 'Poor metabolism increases exposure and supports the lowest recommended starting dose with monitoring, rather than automatically prohibiting use.'),
 ('Paresthesias after an earlier dose', 'Paresthesias are a recognized adverse effect that may affect tolerability and titration; they are not equivalent to the label’s seizure-history contraindication.')],
 [S('Increase Presynaptic Release', '**Amifampridine blocks potassium channels**, prolonging presynaptic depolarization and improving acetylcholine release. It provides symptomatic benefit in LEMS rather than treating an underlying malignancy.',
    'The July 2025 US adult starting range is ==15–30 mg/day in 3–5 divided doses==. Titrate total daily dose by 5 mg every 3–4 days according to response and tolerability.',
    'The cited adult limits are ==20 mg per dose== and ==100 mg/day==. Product and jurisdiction matter; older or non-US schedules should not be silently substituted for the specified label.'),
  S('Assess Exposure and Seizure Risk', '**A seizure history is a contraindication**, and seizures can also occur without prior epilepsy. Review medicines that lower seizure threshold and reassess promptly if a seizure occurs.',
    'Renal or hepatic impairment and known NAT2 poor metabolism call for the lowest recommended initial daily dose. Follow specific renal guidance; the label does not provide an end-stage renal disease regimen.',
    'Monitor adverse effects and practical strength/function. Pyridostigmine may be an adjunct in selected patients but adds cholinergic adverse-effect considerations. Treat associated cancer where present, and consider specialist immune therapy when symptomatic measures are insufficient; increasing the release-enhancing drug through toxicity is not a substitute for revisiting the whole disease strategy.')], ['AMI','SYND','LEMS'], style='direct')

add('Lambert-Eaton and congenital myasthenic syndromes', 'Genotype-Directed Congenital Myasthenia Treatment',
 'A young adult has lifelong exertional limb-girdle weakness, negative autoimmune MG antibodies and biallelic pathogenic DOK7 variants. Pyridostigmine worsened symptoms. Which approach best fits this diagnosis?',
 'Use specialist genotype-directed therapy, often salbutamol or ephedrine, rather than automatic autoimmune MG escalation', [
 ('Escalate pyridostigmine because every congenital transmission defect benefits from more acetylcholine', 'Response depends on the molecular defect; DOK7, COLQ and slow-channel syndromes can worsen with acetylcholinesterase inhibitors rather than improving through dose escalation.'),
 ('Start long-term corticosteroids because negative antibodies establish seronegative autoimmune MG', 'Negative antibodies alone do not establish autoimmune MG, and confirmed DOK7 disease identifies an inherited transmission defect without a routine immunosuppressive indication.'),
 ('Offer nonthymomatous thymectomy using the AChR-positive MGTX rationale', 'MGTX addressed acquired AChR-positive generalized autoimmune disease; its evidence does not justify thymectomy for genetically confirmed congenital myasthenia.')],
 [S('Inherited Transmission Disease Can Present Late', '**Congenital myasthenic syndromes** arise from diverse genetic defects of presynaptic, synaptic or postsynaptic transmission. Recognition in adulthood does not exclude an inherited disorder.',
    'Early symptoms, family history, episodic apnea or an atypical limb-girdle phenotype can provide clues. Inheritance varies by subtype, so counseling should follow the actual molecular diagnosis.',
    'Electrophysiology may show transmission failure, but that does not establish autoimmunity. Interpret a genetic result for pathogenicity and phenotype rather than treating every uncertain variant as a diagnosis.'),
  S('The Same Symptomatic Drug Can Help or Harm', '**DOK7-associated disease often benefits from beta-adrenergic agonist therapy** under specialist supervision. Salbutamol or ephedrine is chosen with attention to cardiac status, adverse effects and local availability.',
    'Acetylcholinesterase inhibitors can worsen DOK7, COLQ-related endplate enzyme deficiency and slow-channel disease. Other genotypes may respond well, illustrating why one inherited-NMJ regimen cannot be generalized.',
    'Assess respiratory, swallowing, mobility and orthopedic needs directly. Treatment evidence is often based on small series rather than large trials, and response may take time. Genetic counseling, family evaluation and an emergency plan for decompensation complement medication; immunotherapy is not added merely because the symptoms resemble MG.')], ['CMS','CMSTX','SYND'])

R.update({
 'MYOPAT': ('Continuum: a pattern-recognition approach to myopathy', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC10564046/'),
 'MYOEMG': ('Electrodiagnostic evaluation of myopathies', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC4435557/'),
 'HYPERCK': ('EAN 2024 guideline on oligo/asymptomatic hyperCKemia, published 2026', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC12860458/'),
 'RHABDO': ('AAST rhabdomyolysis clinical consensus document, 2022', 'https://tsaco.bmj.com/content/7/1/e000836'),
})

add('Approach to muscle disease', 'Normal CK Does Not Exclude Myopathy',
 'An adult has objectively progressive symmetric hip and shoulder weakness, preserved sensation and no clear fatigability. CK is normal on two occasions. Which interpretation is best?',
 'A muscle disorder remains possible; investigate according to the phenotype and exposures', [
 ('The weakness is most likely nonneurologic because CK is repeatedly normal', 'A normal injury marker does not negate demonstrated weakness; selected endocrine, toxic, structural and inherited muscle disorders may have normal or modest CK.'),
 ('The normal CK establishes a neuromuscular junction disorder', 'NMJ disease often has normal CK, but requires a compatible fatigable distribution and transmission evidence; normal CK alone does not establish that localization.'),
 ('The normal CK establishes motor neuron disease over a muscle disorder', 'Motor neuron disease is assessed through its distribution, upper/lower motor neuron findings and electrophysiology; CK cannot independently distinguish it from all myopathies.')],
 [S('A Marker of Injury Rather Than a Strength Meter', '**CK reflects muscle membrane injury and enzyme release**, not the amount of weakness in a simple linear relationship. Some severe weakness occurs without substantial CK elevation.',
    'Steroid myopathy, selected endocrine disorders, congenital myopathies and mitochondrial disease can have normal or modest values. Advanced loss of muscle bulk may also change the amount released.',
    'Conversely, exercise, seizures, trauma and injections can raise CK without a primary chronic myopathy. Interpret the reference range and timing rather than treating one numerical result as a diagnosis.'),
  S('Localize Before Selecting the Next Test', '**Describe distribution, tempo and associated features**: proximal versus distal, symmetric versus asymmetric, ocular/bulbar involvement, sensory signs, reflexes and exertional or fasting triggers.',
    'Review glucocorticoids, other myotoxic drugs, thyroid function, electrolytes, family history and systemic features. Use electrodiagnostics, targeted laboratory studies, muscle imaging or genetic assessment when indicated.',
    'Normal CK and even a normal EMG do not exclude every muscle disorder. A highly specific inherited phenotype may warrant molecular testing, while suspected inflammation may need antibody, imaging and tissue integration. Progressive respiratory or swallowing weakness requires direct assessment regardless of enzyme results.')], ['MYOPAT','MYOEMG'])

add('Approach to muscle disease', 'Myopathic Recruitment on Needle EMG',
 'In weak proximal muscles, needle EMG shows short-duration, low-amplitude motor units with early recruitment. Sensory responses are preserved. Which interpretation is most appropriate?',
 'A myopathic motor-unit pattern that requires etiologic correlation', [
 ('Chronic neurogenic remodeling as the main pattern', 'Chronic reinnervation typically produces larger, longer-duration units with reduced recruitment; this early recruitment of small short units more strongly favors myopathy.'),
 ('An electrophysiologic diagnosis of autoimmune myositis specifically', 'The motor-unit pattern can occur in inflammatory, inherited, toxic and other myopathies; it localizes dysfunction but does not uniquely identify immune inflammation.'),
 ('An electrophysiologic diagnosis of postsynaptic MG specifically', 'MG is assessed by transmission studies such as RNS and jitter in context; a conventional myopathic unit pattern alone does not establish its autoimmune postsynaptic cause.')],
 [S('Fewer Functioning Fibers Within a Motor Unit', '**Loss or dysfunction of muscle fibers** can produce smaller, shorter motor-unit potentials. Recruitment occurs early because more units are needed to generate the requested force.',
    'Sample an appropriate distribution and consider activation, disease stage and technical factors. Not every short unit is pathological, and end-stage or mixed disease can yield more complex patterns.',
    'Fibrillation potentials and positive sharp waves indicate membrane irritability but are not unique to denervation or immune myositis. Some dystrophic, necrotizing and toxic processes are also irritable.'),
  S('Use EMG to Refine, Not Replace, the Diagnosis', '**Integrate CK, clinical distribution, exposures and systemic findings.** Sensory preservation supports a muscle/NMJ localization but does not distinguish those categories on its own.',
    'Electrodiagnostics can identify a superimposed neuropathy, motor neuron disorder or transmission defect and can help choose a biopsy site when tissue is needed.',
    'Selected myopathies have a normal or nondiagnostic EMG, particularly with limited sampling or fiber-selective pathology. A negative study should be weighed against the phenotype. When planning biopsy, avoid sampling recently needled tissue because procedure-related injury can obscure interpretation; use an appropriate contralateral muscle when disease symmetry permits.')], ['MYOEMG','MYOPAT'], style='direct')

add('Approach to muscle disease', 'Selecting a Muscle Biopsy Site',
 'A patient with suspected inflammatory myopathy needs muscle biopsy. MRI shows one moderately weak thigh muscle with edema and preserved bulk, while another is severely atrophic with extensive fatty replacement. Which site is preferable?',
 'The affected, moderately weak muscle with preserved tissue, avoiding recent needle injury', [
 ('The most severely atrophic muscle because it must contain the greatest diagnostic inflammation', 'End-stage fatty replacement can leave little interpretable tissue and nonspecific damage; the weakest muscle is not automatically the highest-yield site.'),
 ('An entirely normal distant muscle regardless of the clinical or imaging distribution', 'Some disorders are patchy; a clinically and radiologically uninvolved site can miss pathology, so selection should reflect the suspected disease distribution.'),
 ('The exact area needled during yesterday’s EMG because irritability confirms the target', 'EMG can guide selection, but recent needle injury can produce artifacts; choose an appropriate unaffected-by-needle region or contralateral equivalent when feasible.')],
 [S('Aim for Active, Interpretable Tissue', '**Biopsy yield depends on selecting representative muscle**, often moderately weak and affected on imaging or examination, rather than normal tissue or end-stage destruction.',
    'MRI can map edema, atrophy and fatty replacement and reveal a useful distribution. Edema is not specific for immune inflammation and may also follow exertion, denervation or injury.',
    'Use the clinical question to determine whether tissue is needed at all. A secure genetic or antibody-defined diagnosis may change the value of biopsy, whereas unexplained disease may still require histology.'),
  S('Plan the Procedure With the Laboratory', '**Coordinate tissue handling and requested studies** before sampling. Histochemistry, immunostaining, biochemical or ultrastructural studies may require appropriate fresh/frozen material rather than routine fixation alone.',
    'Avoid recent EMG sites and discuss treatment exposure, disease duration and distribution with the pathologist. Symmetric disease may allow biopsy of the contralateral counterpart to an electrodiagnostically abnormal muscle.',
    'Interpret the report with the clinical phenotype and other tests. A nonspecific or negative sample does not automatically exclude a patchy inflammatory, metabolic or inherited disorder. Reassessment should identify whether sampling, timing or an alternative diagnosis explains discordance rather than simply repeating an invasive procedure without a new rationale.')], ['MYOEMG','MYOPAT','HYPERCK'])

add('Approach to muscle disease', 'Rechecking Incidental HyperCKemia',
 'An asymptomatic adult has CK twice the laboratory upper limit the day after an unusually strenuous gym session. Examination is normal. What is the most appropriate initial approach?',
 'Repeat CK after a rest interval and review exercise, drugs and systemic contributors', [
 ('Proceed directly to muscle biopsy before repeating the measurement', 'Biopsy can help selected persistent unexplained cases, but transient exercise-related elevation should first be reassessed and common nonneuromuscular causes excluded.'),
 ('Start corticosteroids for presumed subclinical autoimmune myositis', 'CK elevation alone after exertion does not establish inflammation; empiric immune treatment could create harm and obscure the subsequent diagnostic assessment.'),
 ('Assign a muscular dystrophy diagnosis from the CK value alone', 'Inherited disorders can cause asymptomatic hyperCKemia, but a single exercise-associated result is not sufficient to identify a dystrophy or its genetic cause.')],
 [S('Establish That the Finding Persists', '**CK varies with activity and reference population.** Repeat after avoiding strenuous activity, commonly for about seven days, unless symptoms or the clinical context require more immediate evaluation.',
    'Review medications, supplements, trauma, injections, seizures, thyroid status and other systemic causes. Ask about weakness, cramps, exertional intolerance, pigmenturia and family history.',
    'Dark urine, severe pain, rapidly progressive weakness or metabolic instability is not an incidental-asymptomatic pathway and requires prompt assessment.'),
  S('Use a Modern Stepwise Workup', '**Persistent unexplained elevation deserves phenotype-directed investigation.** The EAN 2024 guideline, published in 2026, recommends investigating persistent oligo/asymptomatic CK above about 1.5 times an appropriate ULN.',
    'The pathway includes exclusion of neurogenic and nonneuromuscular causes, electrodiagnostics, targeted metabolic evaluation and appropriate muscle imaging/genetic testing; it does not mandate biopsy first in every patient.',
    'Molecular testing can precede biopsy in suspected inherited disease. Tissue remains useful when genetics is uninformative or inflammatory/metabolic pathology is suspected. Explain that a variant of uncertain significance is not a confirmed cause. Interpret the threshold with validated laboratory and demographic context rather than attaching a diagnosis to any value outside one generic range.')], ['HYPERCK','MYOPAT'])

add('Approach to muscle disease', 'Initial Rhabdomyolysis Management',
 'After a crush injury, an adult has dark urine, CK 24,000 U/L and rising potassium. There is no pulmonary edema or initial anuria. Which strategy best fits initial management?',
 'Prompt individualized crystalloid resuscitation with ECG, electrolyte, urine-output and renal monitoring', [
 ('Routine bicarbonate and mannitol for every patient as the main kidney-protection strategy', 'Routine alkalinization or mannitol has not demonstrated the required preventive benefit; resuscitation and complication monitoring remain the foundation, with separate indications handled individually.'),
 ('Prophylactic dialysis based on the CK value before standard indications develop', 'CK helps describe injury burden but is not alone a dialysis indication; refractory hyperkalemia, acidosis, overload and other established clinical indications guide renal replacement.'),
 ('Restrict fluid until the CK concentration reaches its peak', 'Waiting for peak CK can delay effective correction of hypovolemia and renal perfusion; fluids should be guided by current physiology and overload risk rather than that delayed laboratory milestone.')],
 [S('Treat Immediate Physiology', '**Rhabdomyolysis releases muscle contents** and can cause AKI, hyperkalemia, acidosis and calcium/phosphate abnormalities. ECG and urgent potassium management are priorities when hyperkalemia is significant.',
    'Start crystalloid according to perfusion, losses and cardiac/renal reserve. The AAST 2022 consensus gives approximately ==400 mL/hour== as a possible adult starting rate, then titrates rather than prescribing one fixed rate for all patients.',
    'Suggested urine-output targets are approximately ==1–3 mL/kg/hour==, up to about 300 mL/hour, where achievable safely. Persistent anuria is a reason to reassess, not to force escalating fluid into overload.'),
  S('Monitor Complications and the Cause', '**Follow urine output, renal function, electrolytes and clinical volume status.** Serial CK helps establish the trajectory, but treatment decisions should not depend on CK alone.',
    'Routine bicarbonate, mannitol or loop diuretics solely to prevent AKI is not recommended by the cited consensus. Renal replacement treats standard complications rather than serving as automatic prophylaxis for a high enzyme result.',
    'Assess compartment syndrome and the initiating trauma, drug, heat, seizure or metabolic cause. Early hypocalcemia often does not need replacement unless symptomatic or required for cardiac stabilization in hyperkalemia; later calcium changes also require follow-up. Recurrent or disproportionate exertional episodes warrant investigation for an underlying muscle disorder after stabilization.')], ['RHABDO','MYOPAT'])

R.update({
 'BSR': ('British Society for Rheumatology inflammatory myopathy management guideline, 2022', 'https://doi.org/10.1093/rheumatology/keac115'),
 'DMENMC': ('239th ENMC workshop: classification of dermatomyositis', 'https://www.enmc.org/wp-content/uploads/2024/05/Full-report-WS-239.pdf'),
 'IMACS': ('IMACS international myositis-associated cancer screening guideline, 2023', 'https://doi.org/10.1038/s41584-023-01045-w'),
 'ASENMC': ('273rd ENMC workshop: antisynthetase syndrome classification, 2024 report', 'https://www.enmc.org/wp-content/uploads/2024/12/Full-report-WS-273.pdf'),
 'ILD': ('ACR/CHEST systemic autoimmune rheumatic disease ILD treatment guideline, 2023', 'https://doi.org/10.1002/art.42861'),
 'ERSILD': ('ERS/EULAR connective tissue disease ILD clinical practice guideline, 2026', 'https://doi.org/10.1183/13993003.02533-2024'),
})

add('Inflammatory and immune muscle disease', 'Recognizing Dermatomyositis',
 'A patient has subacute proximal weakness, violaceous eyelid discoloration and papules over the extensor MCP/PIP joints. Muscle biopsy shows perifascicular atrophy. Which diagnosis best fits?',
 'Dermatomyositis', [
 ('Antisynthetase syndrome', 'Antisynthetase disease can overlap with myositis and skin findings, especially mechanic’s hands, but the characteristic heliotrope/Gottron distribution and perifascicular pattern strongly support DM.'),
 ('Immune-mediated necrotizing myopathy', 'IMNM often causes severe proximal weakness and marked CK elevation with necrosis/regeneration, but usually lacks this characteristic DM rash and predominant perifascicular pattern.'),
 ('Inclusion body myositis', 'IBM commonly causes slowly progressive finger-flexor and quadriceps weakness with a different biopsy pattern; the subacute proximal-rash presentation is less consistent.')],
 [S('Integrate Skin, Muscle and Histology', '**Gottron papules and heliotrope change** are important DM clues. Photo-distributed erythema, periungual abnormalities and scalp disease can provide additional support.',
    'Muscle involvement is variable: clinically amyopathic or hypomyopathic disease can have little weakness or CK elevation. A normal enzyme result does not exclude the systemic implications of the cutaneous phenotype.',
    'Perifascicular atrophy and appropriate myxovirus-resistance protein A staining support muscle pathology in context, but individual findings have imperfect sensitivity and vary by antibody subgroup.'),
  S('Antibodies Organize Risk Rather Than Replace Examination', '**Anti-Mi-2 is associated with classic cutaneous-muscle DM**, while TIF1-gamma and NXP2 inform cancer-risk assessment, MDA5 highlights lung risk and SAE can accompany prominent skin/bulbar disease.',
    'Interpret assay strength and phenotype together. A positive panel does not independently establish every associated complication or justify treating an asymptomatic test result as proven organ disease.',
    'Assess swallowing, lung and cardiac symptoms and perform risk-directed cancer evaluation. Treatment generally combines glucocorticoids with an appropriate steroid-sparing strategy, rehabilitation and skin care; organ severity determines urgency. Differentiate DM from inherited or toxic myopathy before prolonged immunosuppression, and follow objective strength and function rather than CK alone.')], ['DMENMC','BSR','IMACS'])

add('Inflammatory and immune muscle disease', 'Risk-Stratified Cancer Screening in Myositis',
 'A 57-year-old with newly diagnosed dermatomyositis has anti-TIF1-gamma antibodies and no known cancer. Which approach best reflects IMACS 2023 guidance?',
 'Classify the patient as high risk and arrange guideline-directed enhanced assessment alongside routine age/sex-appropriate screening', [
 ('Use only routine population screening because no tumor symptoms are present', 'Cancer can be occult, and this patient has multiple high-risk factors within the IMACS framework; lack of symptoms does not justify omitting the recommended additional assessment.'),
 ('Use antibody titer surveillance instead of imaging and clinical screening', 'The antibody informs risk but is not a validated replacement for cancer evaluation; a falling titer cannot exclude an occult malignancy.'),
 ('Assign the same intensive screening schedule to every inflammatory myopathy subtype indefinitely', 'IMACS stratifies subtype, antibody and clinical features and focuses recommendations on the relevant disease-onset window; uniform indefinite enhanced screening ignores the risk framework.')],
 [S('Risk Is Relative to the Myositis Population', '**Dermatomyositis, anti-TIF1-gamma and onset after age 40** are high-risk factors in the IMACS framework. Two or more high-risk factors place an adult in the high-risk group.',
    'Other high-risk features include anti-NXP2, persistent high disease activity, moderate/severe dysphagia and cutaneous necrosis or ulceration. Antibody associations have differing evidence strength and must be interpreted accordingly.',
    'These strata compare risk within adult IIM; a standard-risk category does not mean absence of cancer risk or permission to omit routine population screening.'),
  S('Match the Evaluation to the Framework', '**Basic and enhanced assessment supplement country-specific screening.** Enhanced evaluation can include cross-sectional neck, thoracic, abdominal and pelvic imaging and appropriate sex-specific tests, avoiding redundant procedures.',
    'Investigate red flags such as weight loss, smoking-related concern, unexplained fever or night sweats regardless of a nominal category. If initial high-risk evaluation is unrevealing, specialist-directed additional testing and follow-up may be appropriate.',
    'Discuss benefits, incidental findings, radiation and local cancer epidemiology. A positive myositis antibody does not diagnose cancer, and screening is not a reason to withhold necessary treatment of dangerous muscle or lung disease. Reassess the plan as clinical features evolve rather than applying a tumor-marker-only shortcut.')], ['IMACS','BSR'])

add('Inflammatory and immune muscle disease', 'Antisynthetase Disease Beyond the Muscle',
 'A patient has proximal weakness, inflammatory arthritis, fissured hyperkeratotic fingertips and anti-Jo-1 antibodies. CK improves after initial therapy, but exertional dyspnea persists. Which assessment is most important next?',
 'Evaluate interstitial lung disease with HRCT and pulmonary function testing including gas transfer', [
 ('Use normalization of CK to conclude that the dyspnea is unrelated to the autoimmune syndrome', 'Muscle enzyme response does not establish pulmonary control; antisynthetase-associated ILD can persist or progress independently of muscle activity.'),
 ('Evaluate only maximal inspiratory pressure because dyspnea in myositis is entirely respiratory-muscle weakness', 'Respiratory muscle testing can be useful, but the syndrome carries substantial parenchymal lung risk that requires imaging and pulmonary physiology assessment.'),
 ('Obtain a screening chest radiograph and exclude ILD if it is normal', 'Radiography can miss early or clinically important ILD; HRCT is more sensitive and is appropriate in this high-risk symptomatic phenotype.')],
 [S('An Incomplete Triad Is Still Possible', '**Antisynthetase antibodies target aminoacyl-tRNA synthetases**, with Jo-1 the best-known example. Myositis, arthritis and ILD can appear at different times and need not all be present initially.',
    'Mechanic’s hands, Raynaud phenomenon and fever can provide clues. Non-Jo-1 phenotypes may be lung dominant, so lack of marked weakness does not exclude the syndrome.',
    'Interpret the antibody in clinical context and avoid classifying every positive assay as disease. Characterize lung involvement directly rather than estimating it from the CK.'),
  S('Assess Pulmonary Severity and Competing Causes', '**HRCT and PFTs, including FVC and DLCO**, help define parenchymal involvement and functional impairment. Consider oxygenation, exercise limitation and the pace of deterioration.',
    'Respiratory-muscle weakness, infection, aspiration, cardiac disease and pulmonary vascular disease can also contribute. A low FVC alone cannot distinguish restrictive ILD from weak respiratory muscles.',
    'Coordinate rheumatology/neurology and pulmonary care. Immunosuppressive selection depends on lung and muscle severity, toxicity and response; steroid monotherapy can be inadequate for significant ILD. Monitor symptoms, imaging and physiology as appropriate, with urgent reassessment for rapid decline rather than waiting for a scheduled enzyme check.')], ['ASENMC','ERSILD','ILD','BSR'])

add('Inflammatory and immune muscle disease', 'Anti-MDA5 and Rapidly Progressive ILD',
 'A patient with cutaneous dermatomyositis, minimal weakness and anti-MDA5 antibodies develops rapidly worsening hypoxemia and new diffuse interstitial abnormalities over days. Which approach is most appropriate?',
 'Urgent multidisciplinary RP-ILD evaluation and upfront combination immune therapy while assessing infection and transplant needs', [
 ('Defer escalation until CK becomes substantially elevated', 'Anti-MDA5 disease can be clinically amyopathic; little muscle injury does not imply low pulmonary risk or justify delaying treatment of rapid respiratory deterioration.'),
 ('Use a low-dose single immunosuppressant and await a prolonged outpatient response', 'A slowly evolving stable phenotype may permit staged treatment, but rapidly progressive ILD warrants urgent care and guideline-supported combination rather than routine delayed monotherapy.'),
 ('Use antifibrotic monotherapy as the sole initial treatment of the acute immune lung syndrome', 'Antifibrotic therapy has selected roles in fibrosing ILD, but does not replace prompt immunomodulation and supportive care for this rapidly progressive inflammatory presentation.')],
 [S('A Dangerous Muscle–Lung Disconnect', '**Anti-MDA5-associated disease can have severe lung involvement with little muscle weakness or CK elevation.** Cutaneous ulceration and palmar lesions may provide additional clues, but are not required in every case.',
    'Rapidly rising oxygen requirements and new HRCT abnormalities are urgent. Assess infection, aspiration, edema, drug toxicity and other competing processes in parallel rather than assuming that every opacity is autoimmune.',
    'Ferritin and other laboratory trends can inform severity, but no isolated biomarker should replace oxygenation, imaging, clinical trajectory or organ assessment.'),
  S('Combination Treatment With Evidence Qualifications', '**ACR/CHEST guidance conditionally favors upfront triple combination therapy for confirmed or suspected MDA5 RP-ILD over monotherapy.** This is a low-certainty, specialist-directed strategy, not one universally proven drug trio.',
    'Regimens commonly combine glucocorticoids with selected agents such as a calcineurin inhibitor and cyclophosphamide, or other guideline-listed options according to patient factors and expertise.',
    'Monitor infection, cytopenias, kidney/liver toxicity and other treatment risks, with appropriate preventive measures. Arrange early lung-transplant referral when suitable rather than waiting until all treatment options have failed. Oxygen and ventilatory support address current physiology while therapy is selected; urgent lung care must not depend on the onset of overt myositis.')], ['ILD','ERSILD','BSR'])

R.update({
 'IMNM': ('224th ENMC workshop: immune-mediated necrotizing myopathy classification', 'https://www.nmd-journal.com/article/S0960-8966(17)31207-5/abstract'),
 'IMNMDX': ('Myositis Association: diagnosis of immune-mediated necrotizing myopathy', 'https://www.myositis.org/about-myositis/diagnosis/diagnostic-criteria/diagnostic-criteria-for-necrotizing-myopathy/'),
 'IBM': ('272nd ENMC workshop: revised IBM criteria, 2024', 'https://www.enmc.org/wp-content/uploads/2024/05/272th-ENMC-International-workshop-10-Years-of-progress-revision.pdf'),
 'IBMCARE': ('AAPM&R: hereditary and sporadic inclusion body myositis', 'https://now.aapmr.org/hereditary-and-sporadic-inclusion-body-myositis/'),
 'PRODERM': ('ProDERM randomized trial of IVIG in adult dermatomyositis, 2022', 'https://doi.org/10.1056/NEJMoa2117912'),
})

add('Inflammatory and immune muscle disease', 'Persistent Weakness After Statin Withdrawal',
 'A patient has progressive proximal weakness and CK 9,800 U/L that remains markedly elevated eight weeks after statin withdrawal. Anti-HMGCR antibodies are strongly positive in the appropriate phenotype. Which diagnosis best fits?',
 'Anti-HMGCR immune-mediated necrotizing myopathy', [
 ('Self-limited statin-associated muscle symptoms', 'Ordinary toxic symptoms generally improve after withdrawal; persistent substantial CK elevation and progressive objective weakness with concordant HMGCR antibodies suggest immune disease.'),
 ('Glucocorticoid myopathy', 'Steroid myopathy usually has normal or only modest CK and lacks this antibody association; a relevant steroid exposure would also be needed to support it.'),
 ('Inclusion body myositis', 'IBM more often evolves slowly with finger-flexor and knee-extensor involvement, while the severe subacute proximal phenotype and HMGCR serology favor IMNM.')],
 [S('An Immune Process Can Outlast the Exposure', '**Anti-HMGCR IMNM** often causes substantial proximal weakness and CK elevation. Statin exposure is a recognized association but is not required, particularly in younger patients.',
    'The principal serologic groups include anti-HMGCR, anti-SRP and seronegative IMNM. Anti-SRP disease can be particularly severe; subgroup identification helps clinical interpretation and specialist treatment planning.',
    'Biopsy typically shows necrosis and regeneration with relatively sparse inflammation, but the pattern is not unique to one cause. In a convincing antibody-positive clinical setting, biopsy may not always be necessary; uncertainty or discordance can still justify tissue evaluation.'),
  S('Treat Ongoing Disease Rather Than Withdrawal Alone', '**Stop the implicated statin and arrange specialist immune treatment** when active IMNM is established. Withdrawal alone is often insufficient, and early combination treatment may be needed to prevent irreversible damage.',
    'Glucocorticoids and steroid-sparing therapy are commonly used; IVIG is particularly useful in selected anti-HMGCR disease, while other approaches are individualized by subgroup, severity and response.',
    'Monitor objective strength, swallowing, respiratory function when relevant, CK and medication toxicity. Interpret antibody results in context rather than using a low-probability screening signal as proof. Coordinate a future lipid-lowering strategy that avoids unplanned re-exposure and addresses cardiovascular risk alongside the muscle disorder.')], ['IMNM','IMNMDX','BSR'])

add('Inflammatory and immune muscle disease', 'Inclusion Body Myositis Pattern',
 'A 68-year-old has four years of slowly progressive asymmetric weakness, falls from knee buckling and difficulty gripping keys. Deep finger flexors and knee extensors are disproportionately weak; sensation is preserved. Which diagnosis best fits?',
 'Sporadic inclusion body myositis', [
 ('Typical dermatomyositis', 'DM more often presents subacutely with symmetric proximal weakness and characteristic skin disease; the prolonged asymmetric finger-flexor/knee-extensor pattern favors IBM.'),
 ('Anti-HMGCR necrotizing myopathy', 'HMGCR disease often causes marked CK elevation and more generalized proximal weakness; the distinctive chronic selective distribution is less characteristic.'),
 ('Multifocal motor neuropathy', 'MMN can cause asymmetric weakness without sensory loss, but follows named motor-nerve territories with supportive conduction findings rather than this characteristic selective muscle pattern.')],
 [S('Recognize Selective Weakness', '**Deep finger-flexor and knee-extensor weakness**, often asymmetric, is a major IBM clue in an older adult. Dysphagia can be important and may not parallel limb disability.',
    'CK is often normal to moderately elevated. EMG can contain mixed-looking units and irritability, so a neurogenic-appearing component should not automatically redirect the diagnosis to motor neuron disease.',
    'Biopsy and the full clinicopathologic framework establish confidence. Endomysial inflammation, rimmed vacuoles, protein aggregates and mitochondrial changes contribute, but not every feature is present in every sample.'),
  S('Avoid Repeated Ineffective Immune Escalation', '**Routine immunosuppression has not demonstrated the sustained benefit expected in many other immune myopathies.** Inflammation in tissue alone does not justify indefinite escalation without functional benefit.',
    'Assess swallowing and aspiration, falls, mobility, hand function, nutrition and respiratory symptoms. Rehabilitation, assistive devices and appropriate exercise support quality of life and independence.',
    'Anti-cN1A antibodies can support the diagnosis but have imperfect sensitivity and specificity and do not replace the phenotype and tissue assessment. The 2024 ENMC framework updates older criteria; do not demand an outdated relative-strength comparison as an absolute prerequisite. Discuss clinical trials where suitable while being clear about the limits of established disease-modifying treatment.')], ['IBM','IBMCARE','MYOEMG'])

add('Inflammatory and immune muscle disease', 'Initial Immune Treatment and Objective Follow-up',
 'An adult has confirmed active non-IBM inflammatory myopathy with disabling proximal weakness but no immediate respiratory, swallowing or rapidly progressive lung emergency. Which general initial strategy is most appropriate?',
 'Glucocorticoid induction with an individualized steroid-sparing plan, rehabilitation and objective monitoring', [
 ('Long-term pyridostigmine as the principal disease-modifying treatment', 'Pyridostigmine is useful for transmission disorders, not established treatment of inflammatory muscle injury; a muscle diagnosis requires a different disease-directed strategy.'),
 ('Exercise alone until severe atrophy develops before introducing immune treatment', 'Exercise is beneficial when tailored to the patient, but does not replace immune control of disabling active inflammation; waiting for atrophy risks fixed damage.'),
 ('Fixed high-dose glucocorticoids indefinitely, adjusted only by CK', 'Steroids are useful for induction but require a toxicity-conscious taper and wider assessment; CK alone does not distinguish all active disease, damage and treatment-related weakness.')],
 [S('Induce Control and Limit Cumulative Toxicity', '**Glucocorticoids are standard induction treatment** for many active non-IBM inflammatory myopathies, with choice modified by subtype and organ severity. BSR 2022 describes adult oral prednisolone approximately ==0.5–1 mg/kg/day==, commonly 40–60 mg/day.',
    'Severe disease may require intravenous therapy or additional rapid measures. A stable outpatient regimen should not be transferred to dangerous dysphagia, respiratory weakness or rapidly progressive ILD.',
    'Agents such as methotrexate, azathioprine or mycophenolate are selected according to phenotype, organ involvement, reproductive plans, contraindications and monitoring needs; no single agent suits every patient.'),
  S('Measure More Than Muscle Enzymes', '**Follow strength, function and extramuscular disease**, alongside CK and toxicity measures. Persistent weakness can reflect active inflammation, fixed damage, deconditioning, steroid myopathy or another diagnosis.',
    'Provide supervised rehabilitation and appropriate exercise rather than prolonged indiscriminate inactivity. Assess nutrition, bone protection, infection risk, vaccination and drug-specific laboratory surveillance.',
    'Escalate for a documented inadequate response after checking diagnosis, adherence, exposure and organ status. IVIG, rituximab or other therapies have selected roles, with evidence varying by subtype. An isolated enzyme change should not automatically trigger high-risk treatment or conceal worsening swallowing, lung disease or daily function.')], ['BSR','ILD','MYOPAT'])

add('Inflammatory and immune muscle disease', 'What ProDERM Established',
 'Which statement accurately summarizes the ProDERM randomized trial in adults with active dermatomyositis?',
 'IVIG 2 g/kg every four weeks improved the composite response rate at week 16 versus placebo', [
 ('IVIG was tested primarily against rituximab to establish comparative superiority', 'ProDERM used a placebo-controlled randomized phase, not a head-to-head rituximab comparison; its results cannot rank those agents directly.'),
 ('The trial demonstrated the same benefit in inclusion body myositis', 'The trial population had adult DM; extrapolating its response to IBM ignores distinct disease biology and evidence.'),
 ('The main result established normalization of CK as a sufficient treatment endpoint', 'The response was defined through a composite improvement score rather than CK normalization alone; functional and other disease domains matter.')],
 [S('Trial Population, Regimen and Endpoint', '**ProDERM was a phase 3 placebo-controlled study of adult active DM.** During the 16-week randomized phase, patients received IVIG ==2 g/kg every four weeks== or placebo.',
    'The primary response used at least minimal improvement on the Total Improvement Score, not an isolated laboratory threshold. Response occurred in approximately 79% versus 44% at week 16.',
    'The study supports an IVIG role in this population, but does not establish universal response, cure, or superiority to every other immune strategy.'),
  S('Benefit Must Be Balanced Against Infusion Risk', '**Thromboembolic events were an important safety finding.** Assess thrombosis, renal, volume, hemolysis and infusion-related risks before treatment and monitor according to the product and patient.',
    'Consider dose administration over appropriate days and infusion-rate precautions. New headache, chest pain, focal neurologic symptoms or renal deterioration requires assessment rather than automatic attribution to benign infusion discomfort.',
    'Use objective clinical response to decide ongoing treatment and the broader steroid-sparing plan. A positive DM trial does not justify IVIG for an unsupported inflammatory diagnosis or every chronic weakness syndrome. The duration, background treatment and selected trial population define what can reasonably be inferred from the result.')], ['PRODERM','BSR'], style='direct')

R.update({
 'DMD': ('GeneReviews: dystrophinopathies, updated 2026', 'https://www.ncbi.nlm.nih.gov/books/NBK1119/'),
 'FSHD': ('GeneReviews: facioscapulohumeral muscular dystrophy', 'https://www.ncbi.nlm.nih.gov/books/NBK1443/'),
 'FSHDTEST': ('Best-practice genetic diagnostics of FSHD: updated guidance, 2024', 'https://doi.org/10.1111/cge.14533'),
 'LGMD': ('AAN/AANEM limb-girdle and distal dystrophy guideline, 2014', 'https://www.aanem.org/docs/default-source/documents/lgmd_guideline-pdf.pdf'),
 'DM1': ('GeneReviews: myotonic dystrophy type 1', 'https://www.ncbi.nlm.nih.gov/books/NBK1165/'),
 'DMANES': ('Myotonic Dystrophy Foundation: anesthesia guidelines', 'https://myotonic.org/resources/anesthesia-guidelines/'),
})

add('Inherited and mitochondrial muscle disease', 'Cardiac Risk in a Female DMD Variant Carrier',
 'A woman is found to carry her son’s pathogenic DMD variant. She has no weakness, dyspnea or cardiac symptoms. Which management is appropriate?',
 'Arrange baseline cardiac assessment and ongoing surveillance despite absent skeletal symptoms', [
 ('Defer cardiac evaluation until clinically significant limb weakness appears', 'Cardiac involvement can occur without substantial skeletal disease in a heterozygous woman, so limb symptoms are not an adequate trigger for surveillance.'),
 ('Use a normal CK as sufficient evidence to stop cardiac follow-up', 'CK reflects skeletal-muscle injury imperfectly and cannot exclude dystrophin-related cardiomyopathy; cardiac assessment requires its own clinical and imaging pathway.'),
 ('Limit care to reproductive counseling because heterozygous women cannot develop organ disease', 'Genetic counseling is important, but heterozygous women can manifest skeletal and cardiac disease and need clinical assessment as well as reproductive discussion.')],
 [S('A Spectrum Rather Than a Male-Only Disorder', '**Dystrophinopathies include Duchenne, Becker and predominantly cardiac presentations.** Severity and age at onset vary, and women with a pathogenic variant can also develop clinically important disease.',
    'Duchenne usually presents earlier with more severe progressive weakness; Becker often retains more dystrophin function and has a later course, but cardiac disease can be disproportionate to limb disability.',
    'Molecular testing should detect the relevant DMD variant type, including deletion/duplication when appropriate. A negative generic sequencing result is not equivalent to exclusion of all copy-number changes.'),
  S('Surveillance Follows Organ Risk', '**Evaluate the heart independently of reported muscle strength**, using cardiology assessment, ECG and appropriate imaging with periodic follow-up. Tailor intervals to age, findings and current specialty recommendations.',
    'Affected patients also need respiratory, swallowing, rehabilitation, contracture, nutritional and bone assessment according to phenotype. Cardiac and respiratory decline may be clinically silent before advanced disease.',
    'Offer counseling and cascade testing for the established familial variant. Discuss pregnancy with cardiac review where relevant. Genotype-specific and gene-directed treatments have changing eligibility and safety requirements; do not infer candidacy solely from the Duchenne label or substitute an emerging therapy for multidisciplinary surveillance.')], ['DMD','LGMD'])

add('Inherited and mitochondrial muscle disease', 'FSHD Requires the Right Molecular Test',
 'A young adult has asymmetric scapular winging, weak eye closure, difficulty whistling and relatively preserved deltoid strength. Routine exome sequencing is unrevealing. Which next test most directly addresses the suspected disorder?',
 'Specialized D4Z4 repeat-array and permissive-haplotype assessment for FSHD', [
 ('Repeat DMPK CTG-expansion testing', 'DMPK testing evaluates DM1, usually suggested by myotonia and multisystem features; the facial-scapular asymmetric pattern here more strongly suggests FSHD.'),
 ('PMP22 copy-number analysis', 'PMP22 dosage testing addresses CMT1A/HNPP peripheral neuropathies; it does not directly evaluate this selective facial-scapular muscular dystrophy phenotype.'),
 ('AChR antibody testing as the definitive next molecular test', 'AChR serology evaluates autoimmune transmission disease, not an inherited molecular defect; the fixed selective weakness and scapular pattern need an appropriate genetic strategy.')],
 [S('Recognize the Selective Distribution', '**FSHD commonly affects facial, scapular-stabilizing and upper-arm muscles**, often asymmetrically. Abdominal weakness and foot dorsiflexor involvement may add diagnostic clues.',
    'Sensory loss is not a defining feature, and fixed weakness differs from the fluctuating fatigability of MG. Phenotypic variability and reduced penetrance can obscure family history.',
    'CK may be normal or mildly elevated. Neither CK nor routine EMG provides the repeat-array and epigenetic information needed for a molecular diagnosis.'),
  S('Repeat Structure and Haplotype Matter', '**FSHD1 involves a pathogenic D4Z4 contraction on a permissive chromosome-4 background.** A routine exome may not resolve the repeat architecture, so an unrevealing result does not exclude FSHD.',
    'If contraction testing is negative despite a convincing phenotype, specialized assessment can include methylation and FSHD2-related testing. Interpret repeat size, haplotype and epigenetic findings through an experienced laboratory.',
    'Provide genetic counseling, rehabilitation and assessment for respiratory compromise when indicated. Selected patients also need hearing or retinal evaluation according to phenotype and guidance. Do not assume one inheritance pattern or one simple sequence variant explains every molecular subtype; testing limitations should be explicit before declaring the case genetically negative.')], ['FSHD','FSHDTEST'])

add('Inherited and mitochondrial muscle disease', 'A Limb-Girdle Pattern Is Not One Genetic Diagnosis',
 'An adult has progressive pelvic and shoulder-girdle weakness, elevated CK and no skin rash or sensory loss. Several relatives have unexplained muscle disease. Which diagnostic approach is best?',
 'Use phenotype, pedigree and associated organ findings to guide a suitably designed genetic evaluation', [
 ('Assign one specific recessive dystrophy from the proximal distribution alone', 'Many genetic and acquired disorders cause a limb-girdle pattern; distribution alone cannot identify the gene or establish recessive inheritance.'),
 ('Classify the disease as autoimmune myositis because CK is elevated', 'Dystrophies and metabolic or toxic disorders can raise CK; objective evidence and clinical context are needed before assigning an immune mechanism.'),
 ('Use a negative family history in one branch to exclude an inherited disorder', 'Recessive disease, reduced penetrance, new variants and limited pedigree information can conceal inheritance; the broader family and phenotype need assessment.')],
 [S('Describe the Phenotype Precisely', '**Limb-girdle weakness is a pattern shared by many disorders.** Record age at onset, progression, scapular features, contractures, calf changes, distal involvement and exercise-related symptoms.',
    'Pedigree and associated cardiac, respiratory or other systemic disease refine the differential. Consider dystrophinopathy, FSHD, Pompe disease and acquired myopathies when the pattern suggests them.',
    'Modern nomenclature and gene associations evolve; a historical LGMD number should not replace molecular confirmation. Ensure testing includes relevant copy-number or other variant classes when needed.'),
  S('Test and Protect Organs in Parallel', '**Use appropriate panels or broader molecular assessment** when a single highly characteristic diagnosis is not established. Interpret uncertain variants through segregation, phenotype and other supporting data.',
    'Muscle MRI, protein studies or biopsy can help when genetics is uninformative or an acquired/metabolic process remains possible. A negative panel only excludes what the assay can reliably detect.',
    'Assess cardiac and respiratory risk before the gene is fully resolved when the phenotype warrants it. Symptoms can underestimate conduction disease or ventilatory impairment. Provide rehabilitation, safe exercise advice, contracture care and counseling while avoiding prolonged empirical immunosuppression based only on CK and proximal weakness.')], ['LGMD','DMD','FSHDTEST'])

add('Inherited and mitochondrial muscle disease', 'DM1: Myotonia Is Only One Part of the Risk',
 'A patient with grip myotonia, distal weakness and early cataracts has a pathogenic DMPK expansion. Before elective surgery, which issue most needs coordinated assessment beyond the limb examination?',
 'Cardiac conduction disease and respiratory/anesthetic vulnerability', [
 ('Only the degree of grip myotonia because it predicts all perioperative risk', 'Myotonia is clinically relevant, but does not capture conduction abnormalities, hypoventilation, aspiration or sedative sensitivity in this multisystem disease.'),
 ('Only the CK because a normal value excludes clinically important muscle disease', 'CK can be modest or normal and does not quantify cardiac or respiratory risk; molecularly established DM1 requires organ-directed assessment.'),
 ('Only the cataract severity because surgery eliminates the main systemic risk', 'Cataracts are part of the phenotype, but treating them does not remove the underlying conduction, respiratory, endocrine and muscle disease.')],
 [S('A Multisystem Repeat-Expansion Disorder', '**DM1 results from an expanded CTG repeat in DMPK** and is autosomal dominant. Myotonia, distal/facial weakness, cataracts and systemic manifestations can occur in varying combinations.',
    'Repeat instability contributes to anticipation, but one blood repeat measurement does not precisely predict every organ outcome. Targeted expansion testing is needed; routine sequence analysis alone can miss the mechanism.',
    'Congenital disease is a particular counseling concern, often through maternal transmission. Mildly affected relatives may remain unrecognized until a child or another family member is diagnosed.'),
  S('Assess Silent Cardiorespiratory Disease', '**Cardiac conduction defects and arrhythmias can occur without prominent symptoms.** Arrange ECG and appropriate cardiology surveillance, with further testing according to findings.',
    'Evaluate respiratory muscle weakness, sleep-disordered breathing, swallowing and aspiration risk. Sedatives, opioids and anesthesia can expose limited reserve; use a disease-informed perioperative and postoperative plan.',
    'Avoid assuming that an uneventful prior anesthetic guarantees safety. Monitor endocrine and metabolic features and provide rehabilitation and genetic counseling. Symptomatic antimyotonic treatment does not correct all multisystem risk and requires cardiac consideration; reducing stiffness is not equivalent to eliminating arrhythmia or respiratory vulnerability.')], ['DM1','DMANES'])

R.update({
 'DM2': ('GeneReviews: myotonic dystrophy type 2', 'https://www.ncbi.nlm.nih.gov/books/NBK1466/'),
 'CPEO': ('GeneReviews: single large-scale mitochondrial DNA deletion syndromes', 'https://www.ncbi.nlm.nih.gov/books/NBK1203/'),
 'OPMD': ('GeneReviews: oculopharyngeal muscular dystrophy', 'https://www.ncbi.nlm.nih.gov/books/NBK1126/'),
 'POLG': ('GeneReviews: POLG-related disorders', 'https://www.ncbi.nlm.nih.gov/books/NBK26471/'),
 'MITOSEIZ': ('InterERNs consensus on seizure management in primary mitochondrial disease, 2024', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11235721/'),
})

add('Inherited and mitochondrial muscle disease', 'DM2 and Repeat-Expansion Testing',
 'An adult has proximal weakness, prominent muscle pain, mild myotonia and early cataracts. DMPK expansion testing is negative. Which molecular test most directly evaluates the suspected alternative myotonic dystrophy?',
 'CNBP CCTG-repeat expansion testing', [
 ('PABPN1 repeat analysis', 'PABPN1-related OPMD usually emphasizes later-onset ptosis and dysphagia rather than this myotonic, painful proximal phenotype with cataracts.'),
 ('D4Z4 repeat and haplotype analysis', 'This addresses FSHD, typically suggested by selective facial-scapular weakness and asymmetry rather than myotonia and the multisystem dystrophic pattern here.'),
 ('CLCN1 sequence analysis alone', 'CLCN1 disease can cause nondystrophic myotonia, but progressive proximal weakness and early cataracts raise a multisystem myotonic dystrophy requiring expansion testing.')],
 [S('A Proximal and Painful Myotonic Phenotype', '**DM2 is associated with a CCTG expansion in CNBP** and usually follows autosomal dominant inheritance. Proximal or axial weakness and myalgia may be more conspicuous than clinical myotonia.',
    'DM1 more often emphasizes distal/facial weakness and has a recognized congenital phenotype. These are useful tendencies, not absolute clinical rules for every individual.',
    'Cataracts, metabolic abnormalities, cardiac involvement and other systemic features help distinguish dystrophic disease from isolated channel-related stiffness.'),
  S('Use a Test That Can Detect the Mechanism', '**A negative DMPK result does not exclude DM2.** Request a validated CNBP expansion assay; routine exome sequence analysis may not resolve the repeat adequately.',
    'Interpret a molecular result with the phenotype and family history. Muscle biopsy can show overlapping features and is not a reliable substitute for distinguishing DM1 from DM2 genetically.',
    'Assess cardiac conduction and function, respiratory/sleep symptoms, swallowing and endocrine status according to the patient. Manage pain, mobility and myotonia while accounting for drug and cardiac risks. Anesthesia requires a disease-informed plan even when myotonia is mild; a less severe limb phenotype does not establish absence of multisystem risk. Offer genetic counseling without applying DM1 repeat-size predictions indiscriminately to DM2.')], ['DM2','DM1','DMANES'])

add('Inherited and mitochondrial muscle disease', 'Progressive External Ophthalmoplegia and Tissue Testing',
 'A patient has years of slowly progressive bilateral ptosis and fixed external ophthalmoplegia, hearing impairment and exercise intolerance. MG evaluation is unrevealing. Blood testing for a mitochondrial DNA deletion is negative. Which interpretation is best?',
 'Mitochondrial disease remains possible; specialized tissue-aware mtDNA and nuclear-gene evaluation may be needed', [
 ('A negative blood deletion assay excludes all mitochondrial causes of ophthalmoplegia', 'Heteroplasmy and tissue distribution can limit blood sensitivity, and nuclear-gene causes also exist; one negative assay does not exclude the full category.'),
 ('The negative blood result establishes seronegative autoimmune MG', 'Seronegative MG requires a compatible transmission phenotype and evidence; fixed slowly progressive ophthalmoplegia with multisystem clues should prompt a broader evaluation.'),
 ('The ophthalmoplegia establishes a single mtDNA deletion with purely maternal transmission', 'CPEO can arise from several mtDNA or nuclear mechanisms, and a single deletion is often sporadic; phenotype alone cannot assign one mutation or inheritance pattern.')],
 [S('Look Beyond the Ocular Muscles', '**CPEO is a phenotype rather than one molecular diagnosis.** Ptosis and relatively fixed progressive extraocular weakness can accompany exercise intolerance, hearing loss and other mitochondrial manifestations.',
    'Ask about neuropathy, ataxia, pigmentary retinal change, endocrine features and cardiac symptoms. Conduction disease can be clinically important in deletion-associated multisystem syndromes.',
    'Distinguish a slowly progressive myopathic ocular pattern from fluctuating MG, restrictive orbitopathy and focal cranial neuropathy. Normal CK or lactate does not exclude every mitochondrial presentation.'),
  S('Match the Specimen to the Question', '**mtDNA heteroplasmy varies among tissues.** Depending on age, phenotype and suspected variant, urine or muscle testing can add information not captured in blood.',
    'Specialist molecular evaluation may need deletion analysis, sequencing and assessment of nuclear genes involved in mtDNA maintenance. A biopsy, when indicated, should be coordinated for the appropriate histochemical and molecular studies.',
    'Assess cardiac, respiratory, swallowing, endocrine and hearing needs while testing proceeds. Genetic counseling follows the established molecular mechanism; maternal inheritance is not an adequate blanket explanation for nuclear mitochondrial disorders or every large deletion. Avoid declaring a molecular diagnosis from ragged-red fibers alone or excluding disease from one negative blood result.')], ['CPEO','POLG','MYOEMG'])

add('Inherited and mitochondrial muscle disease', 'Oculopharyngeal Muscular Dystrophy and Aspiration',
 'A 56-year-old has slowly progressive bilateral ptosis and dysphagia. His father and paternal aunt had similar late-onset symptoms. There is little day-to-day fluctuation and sensation is normal. Which diagnosis is most likely?',
 'PABPN1-related oculopharyngeal muscular dystrophy', [
 ('MuSK-positive myasthenia gravis', 'MuSK MG can cause severe bulbar weakness, but the fixed late-onset familial ptosis-dysphagia pattern without clear fluctuation more strongly suggests OPMD.'),
 ('Myotonic dystrophy type 1', 'DM1 can cause facial and bulbar weakness but often adds myotonia, distal weakness, cataracts and other systemic clues; this selective familial oculopharyngeal course favors OPMD.'),
 ('Sporadic inclusion body myositis', 'IBM can cause dysphagia in this age range, but characteristic finger-flexor and knee-extensor weakness would be expected; the familial ptosis-led pattern suggests another disorder.')],
 [S('A Late-Onset Inherited Oculopharyngeal Pattern', '**OPMD is commonly associated with a pathogenic PABPN1 repeat expansion.** Ptosis and dysphagia often dominate early, with proximal limb weakness appearing in some patients.',
    'Autosomal dominant transmission is common, although other inheritance contexts exist. Molecular confirmation should use an assay appropriate to the repeat mechanism and family findings.',
    'The clinical pattern distinguishes it from an acquired fluctuating NMJ syndrome, but evaluate uncertain or atypical findings rather than assuming every familial swallowing problem has the same cause.'),
  S('Swallowing Function Drives Important Morbidity', '**Assess aspiration, nutritional intake and weight**, using speech/swallow expertise and instrumental evaluation when indicated. A patient may adapt eating habits and underreport severity.',
    'Diet texture, compensatory strategies and nutritional support are individualized. Selected cricopharyngeal interventions can improve symptoms, but require specialist selection and do not eliminate the progressive muscle disorder.',
    'Evaluate respiratory status and sleep-related symptoms according to phenotype, and plan ptosis procedures with attention to ocular protection. Genetic counseling and family assessment accompany rehabilitation. Do not delay aspiration management while awaiting a genetic result, and do not substitute repeated immune escalation for care of a confirmed inherited dystrophy.')], ['OPMD','LGMD','CMS'])

add('Inherited and mitochondrial muscle disease', 'Valproate Risk in POLG Disease',
 'An adult with molecularly confirmed POLG-related mitochondrial disease develops epilepsy. Which antiseizure drug should be avoided because of the specific risk of severe hepatic toxicity?',
 'Valproate', [
 ('Levetiracetam', 'Levetiracetam is a possible seizure-type-appropriate option in mitochondrial epilepsy and does not share the specific POLG-associated valproate contraindication; renal and behavioral factors still matter.'),
 ('Lamotrigine', 'Lamotrigine may be used in suitable epilepsy contexts with careful titration and seizure-type review; it does not carry the same POLG-specific hepatic prohibition as valproate.'),
 ('Lacosamide', 'Lacosamide can be considered for appropriate focal epilepsy with cardiac and other patient-specific precautions, but is not the drug with the characteristic POLG-related liver-failure risk.')],
 [S('A Genotype-Specific Medication Hazard', '**Valproate can precipitate severe or fatal hepatic dysfunction in POLG-related disease.** Its avoidance is a specific high-yield implication of identifying the molecular cause.',
    'POLG is a nuclear gene involved in mitochondrial DNA maintenance. Its phenotypes can include epilepsy, ataxia, neuropathy and ophthalmoplegia; not every patient has the same syndrome or organ burden.',
    'The precaution should not be diluted to routine enzyme monitoring as if standard-dose valproate were safe once tests are normal.'),
  S('Treat Seizures Without Overgeneralizing Mitochondrial Risk', '**Select an alternative by seizure type, organ function and interactions**, with specialist input. Acute status epilepticus still needs prompt treatment and escalation, avoiding valproate in confirmed POLG disease.',
    'The 2024 InterERNs consensus distinguishes this contraindication from non-POLG mitochondrial disorders, where choices depend on the individual context. It does not prohibit every standard antiseizure medicine solely because a disorder is mitochondrial.',
    'Counsel about inheritance using the established nuclear-gene mechanism rather than assuming maternal transmission. Review liver, cardiac, respiratory and nutritional issues and avoid catabolic stress where possible. Coordinate medication and procedure planning across specialties; symptom-directed care and genetic diagnosis should inform one another rather than leaving important safety information confined to a laboratory report.')], ['POLG','MITOSEIZ'], style='direct')

R.update({
 'POMPE': ('GeneReviews: Pompe disease', 'https://www.ncbi.nlm.nih.gov/books/NBK1261/'),
 'POMPEPATH': ('MetabERN clinical pathway for Pompe disease, 2024', 'https://doi.org/10.1186/s13023-024-03373-w'),
 'MCARDLE': ('GeneReviews: glycogen storage disease type V', 'https://www.ncbi.nlm.nih.gov/books/NBK1344/'),
 'GSDGUIDE': ('International clinical practice guideline for GSD V and VII, 2021', 'https://www.nmd-journal.com/article/S0960-8966(21)00687-8/fulltext'),
 'CPT2': ('GeneReviews: carnitine palmitoyltransferase II deficiency', 'https://www.ncbi.nlm.nih.gov/books/NBK1253/'),
 'METAB': ('Continuum: metabolic myopathies', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC10563931/'),
})

add('Metabolic myopathies and muscle channelopathies', 'Late-Onset Pompe Disease',
 'An adult has progressive limb-girdle and axial weakness with early diaphragmatic involvement and a marked fall in supine FVC. Sensation is normal and CK is moderately elevated. Which targeted investigation is most appropriate for a treatable metabolic cause?',
 'Acid alpha-glucosidase activity screening followed by appropriate biochemical and GAA genetic confirmation', [
 ('PYGM testing as the first phenotype-directed test', 'PYGM-related McArdle disease usually emphasizes early exercise cramps and second wind rather than this progressive axial-respiratory phenotype.'),
 ('CPT2 testing as the first phenotype-directed test', 'Myopathic CPT II deficiency typically causes episodic exertional or fasting-related rhabdomyolysis with relative interepisode recovery, rather than this characteristic progressive respiratory weakness.'),
 ('Anti-HMGCR testing as the sole metabolic confirmation', 'HMGCR antibodies investigate immune necrotizing myopathy, not a metabolic enzyme defect; they cannot confirm Pompe disease or replace appropriate enzyme/genetic evaluation.')],
 [S('Respiratory Weakness Can Be Disproportionate', '**Late-onset Pompe disease is a GAA-related lysosomal glycogen disorder.** Limb-girdle and axial weakness can coexist with diaphragmatic dysfunction before profound loss of ambulation.',
    'Evaluate sitting and supine respiratory function, sleep-related hypoventilation, cough and swallowing. A patient’s preserved ability to walk does not establish adequate ventilatory reserve.',
    'CK and EMG can be variably abnormal. A generic muscular dystrophy label should not prevent testing for this treatable alternative when the distribution and respiratory involvement fit.'),
  S('Confirm Before Disease-Specific Treatment', '**Dried-blood-spot GAA testing can be an initial screen**, followed by confirmation through appropriate enzymology and molecular assessment. Pseudodeficiency and sample quality can complicate a low screening result.',
    'Biallelic pathogenic GAA variants and concordant deficient enzyme activity establish confidence; an isolated variant of uncertain significance or one low screening value should not be overinterpreted.',
    'Refer for disease-specific enzyme-replacement assessment and multidisciplinary respiratory/rehabilitation care. Product selection, eligibility, infusion reactions and antibody issues require specialist review. Treatment can slow or improve aspects of disease but does not eliminate the need for ventilatory support when indicated; do not delay that support while awaiting molecular completion.')], ['POMPE','POMPEPATH','MYOPAT'])

add('Metabolic myopathies and muscle channelopathies', 'McArdle Disease and Second Wind',
 'A young adult develops muscle cramps and marked fatigue during the first minutes of exercise. After slowing or briefly resting, activity becomes easier; occasional dark urine follows intense exertion. Which disorder best fits?',
 'Muscle glycogen phosphorylase deficiency due to PYGM variants', [
 ('Muscle phosphofructokinase deficiency due to PFKM variants', 'Tarui disease also causes exercise intolerance, but does not share the typical McArdle second-wind response and may include hemolysis; carbohydrate strategy also differs.'),
 ('Carnitine palmitoyltransferase II deficiency', 'CPT II disease is more associated with prolonged exercise, fasting, illness or cold-triggered rhabdomyolysis than the early exercise limitation with characteristic second wind.'),
 ('Acid alpha-glucosidase deficiency', 'Pompe disease commonly causes progressive limb-girdle/axial and respiratory weakness rather than the early-exercise cramp and second-wind pattern described.')],
 [S('Blocked Muscle Glycogen Use', '**McArdle disease is GSD V**, usually caused by biallelic PYGM variants. Failure to access muscle glycogen limits early exercise energy supply.',
    'The second-wind phenomenon reflects improved tolerance as circulating fuels become more available. It is a useful clinical clue, but severe pain should not be pushed through to demonstrate it.',
    'Rhabdomyolysis and myoglobinuria can occur, with AKI risk. Resting CK is often elevated; molecular confirmation is preferable to unnecessary hazardous provocation.'),
  S('Plan Activity Rather Than Avoid All Exercise', '**Gradual aerobic conditioning and recognition of early warning symptoms** can improve function. Avoid sudden intense or sustained isometric effort that provokes severe pain or contracture.',
    'Selected pre-exercise carbohydrate intake can improve tolerance under an individualized dietary plan. Do not transfer this advice automatically to GSD VII, where a different metabolic block changes the response.',
    'If a forearm exercise test is needed, use an appropriate nonischemic protocol in experienced hands; ischemic testing can provoke injury. Manage dark urine or severe pain as possible rhabdomyolysis rather than routine postexercise soreness. Provide education, genetic counseling and a safe activity plan that balances fitness, weight and injury prevention.')], ['MCARDLE','GSDGUIDE','METAB'])

add('Metabolic myopathies and muscle channelopathies', 'CPT II Deficiency and Prolonged Exercise',
 'An adult has recurrent myalgia and pigmenturia after prolonged hiking, especially when fasting or unwell. Strength and CK are nearly normal between episodes, and there is no second-wind history. Which inherited defect is most likely?',
 'CPT II deficiency', [
 ('McArdle disease', 'McArdle disease more typically causes symptoms early in exercise with second wind and often persistently elevated CK; prolonged fasting-related episodes fit fatty-acid oxidation disease better.'),
 ('Late-onset Pompe disease', 'Pompe usually presents with progressive limb-girdle/axial and respiratory weakness, not predominantly episodic rhabdomyolysis with near-normal intervals.'),
 ('Primary hypokalemic periodic paralysis', 'Periodic paralysis causes episodic weakness associated with potassium shifts, but recurrent exertional myoglobinuria and muscle breakdown indicate a metabolic muscle-injury process instead.')],
 [S('Long-Chain Fuel Use During Stress', '**The myopathic form of CPT II deficiency** impairs long-chain fatty-acid use and often manifests during prolonged exercise, fasting, illness or cold exposure.',
    'Interepisode examination and CK can be normal, so one normal outpatient measurement does not exclude the diagnosis. Ask specifically about triggers, duration and pigmenturia.',
    'Acylcarnitine profiles can support the evaluation, often with long-chain abnormalities, but results depend on clinical state. Molecular CPT2 testing or appropriate enzyme studies provides confirmation.'),
  S('Prevent Catabolism and Treat Acute Injury', '**Avoid prolonged fasting and unplanned exhausting exertion**, with specialist nutritional and sick-day guidance. Maintain adequate energy intake during illness and procedures.',
    'Acute rhabdomyolysis needs prompt assessment of potassium, renal function, hydration and urine output. A genetic explanation does not reduce the urgency of dangerous electrolyte or kidney complications.',
    'Specialist long-term dietary or metabolic therapies are selected to the disorder and patient; generic high-fat exercise advice is inappropriate. Offer counseling and family assessment, and review anesthetic/procedural planning. Recurrent episodes merit etiologic evaluation even when the initial event had a plausible environmental trigger, because trigger avoidance alone may leave an inherited susceptibility unrecognized.')], ['CPT2','METAB','RHABDO'])

R.update({
 'HYPOPP': ('GeneReviews: hypokalemic periodic paralysis', 'https://www.ncbi.nlm.nih.gov/books/NBK1338/'),
 'PPREV': ('Review of diagnosis and treatment of periodic paralysis, 2018', 'https://periodicparalysis.org/wp-content/uploads/2022/09/Statland-Dx-and-Rx-of-PP-Muscle-Nerve-2018-1.pdf'),
 'HYPERPP': ('GeneReviews: hyperkalemic periodic paralysis', 'https://www.ncbi.nlm.nih.gov/books/NBK1496/'),
 'TPP': ('Changing management guidelines in thyrotoxic hypokalemic periodic paralysis, 2018', 'https://pubmed.ncbi.nlm.nih.gov/29871829/'),
 'NDM': ('Guidelines on presentation and management of nondystrophic myotonias, 2020', 'https://doi.org/10.1002/mus.26887'),
 'MEX': ('EMA NaMuscla product information: mexiletine base dosing and cardiac precautions', 'https://www.ema.europa.eu/en/documents/product-information/namuscla-epar-product-information_en.pdf'),
})

add('Metabolic myopathies and muscle channelopathies', 'Potassium During Familial Hypokalemic Paralysis',
 'A patient with confirmed familial hypokalemic periodic paralysis develops typical limb weakness after a carbohydrate-rich meal. Potassium is 2.6 mmol/L, swallowing is safe and there is no arrhythmia or respiratory weakness. Which initial strategy is appropriate?',
 'Cautious oral potassium chloride with serial potassium and clinical/ECG assessment', [
 ('Calculate a large total-body potassium deficit and replace it rapidly without reassessment', 'The low extracellular potassium mainly reflects redistribution in a typical attack, so a depletion-based large replacement can cause overshoot when the shift reverses.'),
 ('Give glucose-rich intravenous fluid as the principal attack treatment', 'Carbohydrate-related insulin release can promote intracellular potassium shift and worsen a hypokalemic attack; this is not the appropriate rescue for the stated physiology.'),
 ('Use potassium restriction and a thiazide as immediate attack treatment', 'Potassium restriction and selected diuretics can have a role in hyperkalemic periodic paralysis, but do not address this confirmed hypokalemic attack.')],
 [S('A Shift Is Different From a Depleted Store', '**Familial hypoPP commonly involves CACNA1S or SCN4A channel dysfunction**, with attacks after carbohydrate loads or rest following exercise. Sensation and consciousness are generally preserved.',
    'Measure potassium during weakness and assess ECG, breathing and swallowing. Exclude renal/GI losses, thyroid disease and other secondary causes when the presentation is not already securely characterized.',
    'Low potassium contributes to membrane inexcitability, but total-body potassium is not usually depleted in a classic redistribution attack. This changes the safety of replacement.'),
  S('Titrate Rather Than Replace an Assumed Deficit', '**Oral KCl is preferred when the patient is stable and can swallow.** One expert-review approach uses ==0.2–0.4 mEq/kg== increments with reassessment; the exact protocol and repeat dosing require supervised monitoring.',
    'Severe arrhythmia, unsafe swallowing or respiratory involvement may require monitored intravenous treatment and higher-level care. Avoid glucose-containing rescue fluids that intensify the potassium shift.',
    'Watch for rebound hyperkalemia as strength returns. Long-term trigger modification and preventive medication are individualized by genotype, response and adverse effects; some sodium-channel variants respond poorly to acetazolamide. Do not use hazardous potassium/glucose provocation routinely to reproduce an attack when safer clinical, electrophysiologic and molecular evidence is available.')], ['HYPOPP','PPREV'])

add('Metabolic myopathies and muscle channelopathies', 'Thyrotoxic Periodic Paralysis',
 'A man develops acute flaccid weakness after a large meal. Potassium is 2.1 mmol/L, urinary potassium excretion is low, TSH is suppressed and free T4 is elevated. Which management principle is most appropriate?',
 'Use monitored cautious potassium replacement, appropriate nonselective beta-blockade and definitive treatment of thyrotoxicosis', [
 ('Treat a large chronic potassium deficit and continue high-dose potassium after strength normalizes', 'Typical thyrotoxic paralysis is mainly redistribution; continued replacement after the shift reverses increases rebound hyperkalemia risk rather than treating a proven chronic deficit.'),
 ('Use acetazolamide as the principal definitive treatment without correcting thyrotoxicosis', 'Preventive strategies for familial hypoPP should not be copied automatically to TPP; restoring euthyroidism is central to preventing recurrence.'),
 ('Use potassium alone and defer thyroid treatment until a further attack occurs', 'Potassium can help acute weakness, but untreated thyrotoxicosis leaves the mechanism and recurrence risk active; endocrine treatment is part of the initial overall plan.')],
 [S('Look for Thyrotoxicosis Even When Signs Are Subtle', '**TPP combines thyrotoxicosis with episodic weakness and intracellular potassium shift.** Overt tremor, weight loss or goiter may be less conspicuous than expected.',
    'Low urinary potassium and the clinical context support redistribution rather than renal wasting. Evaluate magnesium, phosphate, ECG and competing causes of acute paralysis.',
    'Carbohydrate loads and adrenergic stimuli can trigger attacks, but a family history is not required. Do not label every young patient with hypokalemic weakness as having a primary inherited channelopathy.'),
  S('Reverse the Shift and Prevent Recurrence', '**Nonselective beta-blockade can counter the adrenergic mechanism**, provided bradycardia, asthma, decompensated cardiac disease and other contraindications are considered.',
    'Potassium is given cautiously with frequent checks and ECG monitoring according to severity. The cited review highlights greater rebound risk with larger replacement amounts, especially above about 50 mEq; this is not a universal safe/unsafe cutoff for every patient.',
    'Treat the cause of thyrotoxicosis and maintain a prevention plan until euthyroid. Large potassium loads are not a substitute for that treatment. Acute respiratory compromise or arrhythmia requires urgent monitored care, and recovery of limb strength does not end electrolyte surveillance because overshoot can follow clinical improvement.')], ['TPP','PPREV'])

add('Metabolic myopathies and muscle channelopathies', 'Hyperkalemic Periodic Paralysis',
 'A teenager has short attacks of weakness after rest following exercise or potassium-rich meals, sometimes with myotonia. Potassium rises during an attack and is normal between episodes. Which gene is most characteristically implicated?',
 'SCN4A', [
 ('CACNA1S', 'CACNA1S is a major familial hypoPP gene; the potassium-sensitive hyperkalemic/myotonic phenotype more characteristically implicates the skeletal muscle sodium channel.'),
 ('CLCN1', 'CLCN1 causes myotonia congenita with characteristic stiffness and warm-up, rather than the usual sodium-channel hyperkalemic periodic-paralysis phenotype.'),
 ('DMPK', 'DMPK CTG expansion causes multisystem DM1, not this characteristic childhood-onset potassium-sensitive episodic paralysis syndrome.')],
 [S('An Episodic Sodium-Channel Phenotype', '**SCN4A-related hyperPP** can combine transient flaccid weakness and myotonia. Triggers include potassium-rich foods, fasting, cold and rest after exercise.',
    'Potassium may be high or rise substantially from baseline during an attack, but not every captured sample is frankly hyperkalemic. Timing matters, and normal interepisode potassium does not exclude disease.',
    'Use history, appropriate exercise electrophysiology and molecular confirmation rather than dangerous provocation. Respiratory, swallowing or severe cardiac findings require urgent assessment even if many prior attacks were mild.'),
  S('Do Not Apply the HypoPP Rescue Plan', '**Avoid unsupervised potassium supplementation.** Mild activity or carbohydrate at attack onset can help selected hyperPP patients, in contrast to the carbohydrate trigger in hypoPP.',
    'Selected beta-agonist therapy and preventive measures are specialist directed. Significant hyperkalemia or ECG abnormalities require standard monitored hyperkalemia treatment according to severity.',
    'Long-term care includes avoiding fasting and personal triggers and considering preventive medication such as an appropriate diuretic or carbonic-anhydrase inhibitor. Individualize to genotype, attack burden and electrolyte effects. The serum potassium result guides acute safety, but the full channelopathy phenotype and genetic mechanism determine counseling and the longer-term plan.')], ['HYPERPP','PPREV','NDM'])

add('Metabolic myopathies and muscle channelopathies', 'Nondystrophic Myotonia and Mexiletine Safety',
 'An adult with genetically confirmed CLCN1-related myotonia has disabling stiffness that improves with repeated movement and no myotonic-dystrophy phenotype. Mexiletine is being considered. Which assessment is essential before starting?',
 'Cardiac evaluation including ECG, with review of electrolytes and interacting medicines', [
 ('CK alone to determine whether conduction monitoring is necessary', 'CK does not screen for cardiac conduction abnormalities or proarrhythmic drug risk; a normal value cannot replace cardiac assessment before mexiletine.'),
 ('AChR antibody testing to establish eligibility for sodium-channel blockade', 'AChR antibodies concern autoimmune MG and do not determine mexiletine safety or confirm this genetically established muscle channelopathy.'),
 ('Muscle biopsy to exclude every dystrophic process before any symptomatic treatment', 'Biopsy is not automatically needed after a concordant molecular diagnosis, whereas cardiac and medication safety review directly affects use of this antiarrhythmic agent.')],
 [S('Distinguish Stiffness From Multisystem Dystrophy', '**CLCN1 myotonia congenita** often shows warm-up, while SCN4A phenotypes may include cold sensitivity or paradoxical worsening with activity. Clinical patterns overlap and require molecular interpretation.',
    'Electrical myotonia supports muscle hyperexcitability but is not uniquely diagnostic. Cataracts, progressive weakness and systemic features should prompt consideration of DM1/DM2 and other causes.',
    'Mexiletine reduces sodium-channel excitability and has controlled-trial evidence for symptomatic nondystrophic myotonia. It does not correct the underlying genetic defect.'),
  S('Use the Product-Specific Dose and Cardiac Plan', '**Check ECG, cardiac history, electrolytes and interactions**, with specialist cardiology input for abnormalities and ongoing monitoring according to the selected product.',
    'The EMA NaMuscla regimen starts at ==167 mg mexiletine base daily==, with weekly-or-longer response-guided steps to approximately 333 mg and then 500 mg/day. Base and hydrochloride amounts differ, so do not interchange numbers without checking the formulation.',
    'Monitor gastrointestinal and neurologic adverse effects as well as cardiac safety. Other agents, including lamotrigine, have selected evidence and different precautions. Provide trigger and anesthesia counseling, particularly avoidance of provoking neuromuscular blockers, and judge benefit by daily stiffness and function rather than EMG discharges alone.')], ['NDM','MEX','DM1'])

R.update({
 'TOX': ('AAPM&R: toxic myopathy', 'https://now.aapmr.org/toxic-myopathy/'),
 'COLCH': ('US colchicine prescribing information: neuromuscular toxicity and interactions', 'https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/204820Orig1s004lbl.pdf'),
 'CIM': ('AAPM&R: critical illness myopathy', 'https://now.aapmr.org/critical-illness-myopathy/'),
 'SITC': ('SITC checkpoint-inhibitor adverse-event guideline, 2021', 'https://jitc.bmj.com/content/9/6/e002435'),
})

add('Toxic and critical illness muscle disorders', 'Glucocorticoid Myopathy Versus Active Myositis',
 'A patient treated for inflammatory myopathy develops gradual painless hip-girdle weakness after months of high-dose prednisone. CK has normalized, skin disease is quiet and EMG shows little irritability. Which explanation should be specifically considered before increasing steroids?',
 'Glucocorticoid-induced myopathy', [
 ('Active inflammatory myopathy established by weakness alone', 'Relapse remains possible, but weakness can reflect toxicity or damage; quiet associated disease and low enzyme/EMG activity require reassessment before reflex escalation.'),
 ('Pyridostigmine-induced cholinergic toxicity', 'That diagnosis requires relevant exposure and often muscarinic or fasciculatory findings; this chronic painless proximal pattern during glucocorticoid therapy is different.'),
 ('Inclusion body myositis established by any steroid nonresponse', 'IBM requires a concordant selective pattern and clinicopathologic assessment; nonresponse alone does not establish it, particularly when medication toxicity fits the timing.')],
 [S('A Noninflammatory Treatment Complication', '**Chronic steroid myopathy** typically causes painless proximal weakness, often pelvic-girdle predominant, with normal or modest CK. Fiber atrophy rather than active immune injury is central.',
    'Routine EMG can be normal or show relatively little irritability. These findings support the differential but do not exclude all concurrent active myositis.',
    'Review cumulative exposure, nutrition, inactivity, electrolyte/endocrine factors and other myotoxic medicines. A muscle enzyme result is not a stand-alone activity assessment.'),
  S('Reassess Disease Activity Before Escalating', '**Compare objective strength and function with the prior course**, skin/organ activity, imaging and other relevant data. Distinguish toxicity, fixed damage, deconditioning and ongoing inflammation.',
    'When steroid myopathy is likely, coordinate gradual reduction to the lowest effective exposure and a suitable steroid-sparing plan. Do not abruptly stop prolonged therapy or neglect the original disease.',
    'Provide graded resistance/aerobic rehabilitation and nutritional support appropriate to the patient. Recovery can take time and may be limited by coexisting muscle injury. New bulbar, respiratory or rapidly progressive findings deserve direct urgent assessment rather than automatic attribution to a chronic drug effect.')], ['TOX','BSR','MYOEMG'])

add('Toxic and critical illness muscle disorders', 'Colchicine Neuromyopathy and Drug Interaction',
 'An older patient with chronic kidney disease takes colchicine for gout. Soon after clarithromycin is added, proximal weakness, myalgia and CK elevation develop, with distal sensory findings. Which mechanism is most relevant?',
 'Increased colchicine exposure from inhibited drug handling, causing toxic neuromyopathy', [
 ('A new autoimmune necrotizing myopathy proved by the CK rise', 'IMNM is a consideration in persistent severe muscle disease, but CK elevation alone does not prove it; the renal and interaction context directly raises colchicine toxicity.'),
 ('A benign gout-related pain syndrome without muscle injury', 'Gout causes joint inflammation, not an adequate explanation for proximal weakness, CK elevation and sensory abnormalities after this high-risk drug combination.'),
 ('Typical chronic uremic neuropathy as the sole explanation of the abrupt change', 'Uremic neuropathy can coexist, but the new proximal muscle syndrome after a recognized interaction requires urgent toxic-drug assessment rather than attribution to baseline renal disease.')],
 [S('Microtubule Toxicity Can Affect Muscle and Nerve', '**Colchicine can cause myopathy, neuropathy and rhabdomyolysis**, including during therapeutic dosing when clearance or interacting medicines increase exposure.',
    'Clarithromycin inhibits CYP3A4 and P-glycoprotein pathways involved in colchicine handling. Renal impairment further increases concern for serious or fatal toxicity.',
    'Review the exact product label: colchicine with strong relevant inhibitors in renal or hepatic impairment can be contraindicated, not merely a routine combination needing casual observation.'),
  S('Stop the Exposure and Assess Systemic Harm', '**Urgently withhold implicated therapy and obtain expert medication review.** Evaluate CK, renal/liver function, electrolytes, blood counts and clinical evidence of multiorgan toxicity.',
    'GI symptoms, cytopenias and other systemic findings may accompany neuromuscular injury. Assess respiratory or swallowing involvement and manage rhabdomyolysis complications when present.',
    'Replace the interacting antimicrobial and reconsider gout treatment through an appropriate clinical plan. Recovery after drug withdrawal supports the interpretation, but persistent or atypical weakness requires reassessment for coexisting disease. Do not escalate immune treatment solely because CK is high, and do not assume that normal earlier dosing history makes a newly interacting regimen safe.')], ['COLCH','TOX','RHABDO'])

add('Toxic and critical illness muscle disorders', 'Critical Illness Myopathy Versus Polyneuropathy',
 'After prolonged sepsis and ventilation, a patient has diffuse weakness and difficulty weaning. CMAPs are low, sensory responses are relatively preserved, and needle EMG shows small short motor units with early recruitment. Which process is most strongly supported?',
 'Critical illness myopathy', [
 ('Critical illness polyneuropathy as an isolated process', 'An isolated axonal polyneuropathy more often reduces sensory as well as motor amplitudes; preserved SNAPs and myopathic recruitment favor a muscle component here.'),
 ('Typical acquired demyelinating polyneuropathy', 'Demyelinating disease requires appropriate timing, conduction and clinical evidence; low amplitudes alone in this critical-illness setting do not establish it.'),
 ('Postsynaptic autoimmune MG', 'MG can impair weaning, but requires compatible transmission evidence and phenotype; these conventional EMG findings in sepsis more directly support critical illness muscle disease.')],
 [S('ICU-Acquired Weakness Has Several Mechanisms', '**CIM affects limb and respiratory muscles** and commonly appears during severe systemic illness. CIP is an axonal nerve disorder, and mixed neuromyopathy is frequent.',
    'Sedation, delirium, edema, temperature and limited cooperation complicate bedside and electrodiagnostic assessment. Weakness should not be assigned to one mechanism merely from prolonged ventilation.',
    'Relative sensory preservation supports CIM, while reduced SNAPs can support CIP or coexisting neuropathy. Technical quality and baseline disease must be considered.'),
  S('Use Testing to Resolve a Clinical Question', '**Myopathic units and reduced muscle excitability** can support CIM; direct muscle stimulation has a selected role when distinguishing nerve from muscle failure in difficult cases.',
    'CK may be normal or elevated and is not a reliable sole discriminator. Exclude electrolyte abnormalities, drug effects, residual blockade, focal nerve injury and preexisting neuromuscular disease.',
    'Treat the underlying illness, optimize safe mobilization and rehabilitation, address nutrition and minimize avoidable contributors. No routine immunotherapy reverses every ICU-acquired weakness syndrome. Weaning decisions need respiratory and airway assessment in addition to limb power, and recovery can be prolonged; communicate realistic uncertainty rather than promising resolution when sepsis clears.')], ['CIM','MYOEMG','TOX'])

add('Toxic and critical illness muscle disorders', 'Checkpoint-Inhibitor Neuromuscular–Cardiac Overlap',
 'Soon after checkpoint-inhibitor treatment, a patient develops ptosis, dysphagia and proximal weakness with CK and troponin elevation. Which next approach is most appropriate?',
 'Hold the checkpoint inhibitor and urgently assess MG, myositis and myocarditis together in monitored multidisciplinary care', [
 ('Treat presumed isolated MG as an outpatient because ocular symptoms identify the whole syndrome', 'Ocular symptoms do not exclude concurrent myositis or myocarditis; troponin and CK abnormalities plus bulbar weakness demand broader urgent assessment.'),
 ('Continue cancer immunotherapy while awaiting muscle biopsy before any escalation', 'Tissue can help selected uncertain cases, but should not delay evaluation and treatment of potentially fatal cardiac and respiratory toxicity.'),
 ('Attribute troponin elevation to skeletal-muscle injury and omit cardiac evaluation', 'Assay and clinical context require interpretation, but possible myocarditis cannot be dismissed in this high-risk exposure-associated syndrome; ECG and cardiac assessment are necessary.')],
 [S('Look for All Three Disorders', '**Checkpoint-inhibitor MG, myositis and myocarditis can overlap**, with rapid deterioration and substantial mortality risk. Suspicion of one should prompt evaluation for the others.',
    'Assess bulbar/respiratory function, CK, ECG, troponin and appropriate cardiac testing, with neurology, cardiology, oncology and critical-care input. Antibody negativity does not by itself exclude the syndrome.',
    'Other causes of weakness or troponin elevation remain possible, but the exposure and pattern justify urgent monitored investigation rather than sequential outpatient exclusion.'),
  S('Coordinate Urgent Treatment', '**Withhold the suspected checkpoint inhibitor and treat according to organ severity.** Cardiac and respiratory support cannot wait for every confirmatory test.',
    'High-dose glucocorticoids are often needed for severe immune toxicity; when MG is present, anticipate possible initial worsening and coordinate rapid IVIG or exchange with respiratory monitoring.',
    'Myocarditis may require immediate intensive immune treatment and additional specialist therapy if refractory, while the neuromuscular component has its own assessment and rescue needs. The optimal regimen is individualized because controlled evidence is limited. Rechallenge is a high-stakes oncology decision, not an automatic consequence of a falling CK. Continue objective cardiac, swallowing and respiratory follow-up throughout recovery.')], ['SITC','CONS','CRISIS'])

# Review changes are matched by title so later insertions cannot shift them.
def revise(title, *, stem=None, answer=None, others=None):
    matches = [r for r in rows if r['title'] == title]
    assert len(matches) == 1, title
    row = matches[0]
    if stem is not None: row['question'] = stem
    if answer is not None: row['answer'] = answer
    if others is not None: row['others'] = others

revise('Low-Frequency Repetitive Nerve Stimulation',
 stem='In the conventional low-frequency RNS protocol for suspected MG, approximately what reproducible first-to-fourth/fifth CMAP decrement is commonly considered abnormal after technical artifacts are excluded?',
 answer='At least 10%', others=[
 ('At least 3%', 'Small response variation can occur from measurement and technical factors; three percent is below the conventional decrement threshold specified in this question.'),
 ('At least 20%', 'A decrement this large is abnormal, but requiring it would miss responses between the conventional threshold and twenty percent; the question asks the threshold, not a more severe example.'),
 ('At least 30%', 'Thirty percent is used in selected motor conduction-block frameworks with other qualifications, not as the conventional low-frequency NMJ decrement threshold.')])
revise('Jitter Testing After Nondiagnostic RNS', others=[
 ('Conventional needle EMG of clinically involved facial and proximal muscles', 'Conventional EMG helps identify myopathic or neurogenic mimics, but targeted jitter is more sensitive for transmission instability when routine stimulation has been unrevealing.'),
 ('Blink-reflex studies with facial motor conduction', 'These can investigate selected brainstem, trigeminal or facial pathway disorders; they do not provide the same assessment of endplate timing variability in suspected ocular MG.'),
 ('Postexercise increment testing in distal hand muscles', 'Postexercise testing is useful when presynaptic LEMS is suspected; a targeted facial jitter study more directly addresses this persistent ocular postsynaptic suspicion.')])
revise('Ice-Pack Testing for Ptosis',
 answer='It increases the likelihood of ocular MG in this clinical context', others=[
 ('It increases the likelihood of aponeurotic ptosis', 'Aponeurotic disease causes structural lid elevation failure, whereas an objective transient improvement after cooling in fluctuating ptosis is more supportive of impaired transmission.'),
 ('It increases the likelihood of mitochondrial external ophthalmoplegia', 'Mitochondrial ophthalmoplegia can produce ptosis but usually has a slowly progressive fixed course; this dynamic bedside response more strongly supports the myasthenic differential.'),
 ('It increases the likelihood of restrictive thyroid orbitopathy', 'Thyroid orbitopathy can cause diplopia and lid abnormalities, but mechanical restriction is not the expected explanation for the stated reversible fatigable ptosis response.')])
revise('Thymic Imaging in Autoimmune MG', others=[
 ('Chest radiography with interval reassessment', 'Radiography can reveal a large mass but is insufficient to exclude clinically silent thymoma; cross-sectional imaging is the appropriate anatomical evaluation.'),
 ('Whole-body FDG-PET as the initial screening study', 'PET has selected tumor-assessment roles but is not the usual first-line substitute for anatomical thymic CT or MRI in this setting.'),
 ('Striational-antibody profiling before deciding whether to image', 'Striational antibodies can accompany thymoma-associated or late-onset MG, but cannot reliably replace anatomical assessment or safely gate imaging on their result.')])
revise('Functionally Limiting Ocular MG', others=[
 ('Begin regularly scheduled IVIG maintenance', 'IVIG can be useful in selected severe or refractory MG, but is not the usual first immune step for stable isolated ocular disease inadequately controlled symptomatically.'),
 ('Begin azathioprine monotherapy', 'Azathioprine may be selected when steroids are contraindicated or poorly tolerated, but corticosteroids are the generally recommended initial immune agent in the stated uncomplicated context.'),
 ('Refer for nonthymomatous thymectomy as the initial immune intervention', 'Surgery can be considered in selected contexts, but the strongest randomized evidence is in generalized AChR-positive disease; it is not the routine initial immune approach for this ocular presentation.')])
revise('Corticosteroid Initiation in Significant Bulbar MG', others=[
 ('Admit for monitoring and begin rapid high-dose corticosteroid induction without short-term rescue', 'Steroids may be introduced under monitoring, but significant bulbar and declining respiratory reserve make rapid IVIG/exchange and attention to initial steroid worsening particularly appropriate.'),
 ('Begin azathioprine with a gradual outpatient prednisone escalation', 'This can be part of longer-term treatment for stable disease, but delayed drug onset and the supplied airway-related findings make an outpatient plan unsuitable now.'),
 ('Increase pyridostigmine with a brief monitored observation period', 'Symptomatic adjustment can help mild weakness, but cannot provide sufficient immune control for this high-risk trajectory and may increase secretion burden.')])
revise('Azathioprine and Pharmacogenetic Safety', others=[
 ('Serial liver tests with symptom-triggered blood counts', 'Liver monitoring is important, but cytopenias can precede symptoms; normal tested genotypes do not make scheduled CBC surveillance unnecessary.'),
 ('Serial thiopurine metabolites with symptom-triggered blood counts', 'Metabolites answer selected exposure questions, but cannot substitute for direct scheduled monitoring of blood counts and hepatic toxicity.'),
 ('CBC and liver tests only after the first six months of treatment', 'Stable long-term intervals may be extended under local protocols, but early initiation and titration need closer checks because serious toxicity can develop before six months.')])
revise('Thymectomy Evidence in Nonthymomatous MG',
 stem='Which outcome is supported by MGTX for a patient matching its nonthymomatous AChR-positive generalized MG population?',
 answer='Improved clinical control with reduced prednisone requirements versus prednisone alone', others=[
 ('Superiority to rituximab as initial steroid-sparing therapy', 'MGTX compared thymectomy plus prednisone with prednisone alone, not rituximab; its results cannot establish that active-treatment comparison.'),
 ('Equivalent benefit across AChR-positive and MuSK-positive subgroups', 'The trial addressed AChR-positive generalized disease; MuSK patients were not an equivalent randomized subgroup from which to infer the same benefit.'),
 ('Rapid prevention of intubation during an established crisis', 'MGTX studied longer-term outcomes rather than crisis rescue; acute airway and rapid immune treatment decisions must precede elective surgical considerations.')])
revise('Early Rituximab Consideration in MuSK MG',
 answer='Rituximab', others=[
 ('Nonthymomatous thymectomy', 'Thymectomy has specific tumor and AChR-generalized evidence-based roles, but does not have the same supported immune benefit in MuSK disease.'),
 ('Ravulizumab', 'Ravulizumab blocks C5 and has an adult AChR-positive generalized MG indication; predominant MuSK IgG4 biology and subgroup evidence make this a different therapeutic context.'),
 ('Azathioprine alone with no bridging plan', 'Azathioprine is a legitimate steroid-sparing option in MG, but its delayed onset is a limitation in persistent important bulbar disease; early rituximab has particular consensus support in MuSK MG.')])
revise('Meningococcal Risk With C5 Inhibition', others=[
 ('Update MenACWY vaccination and use routine boosters', 'MenACWY vaccination is necessary, but alone leaves out the recommended MenB component for complement-inhibitor recipients.'),
 ('Update MenB vaccination and use routine boosters', 'MenB vaccination is necessary, but alone does not cover the other serogroups addressed by MenACWY; both categories are recommended.'),
 ('Use antibacterial prophylaxis with vaccination deferred until treatment completion', 'Urgent-start prophylaxis can be needed when treatment cannot wait, but does not justify postponing indicated vaccines until the entire course ends when preventive planning is feasible.')])
revise('Transient Neonatal Myasthenia', others=[
 ('An inherited congenital myasthenic syndrome', 'CMS can cause neonatal hypotonia and feeding/respiratory weakness, but maternal autoimmune MG strongly raises passive antibody-mediated neonatal disease; persistence or atypical findings warrants genetic reassessment.'),
 ('A congenital structural myopathy', 'Congenital myopathy is an important neonatal weakness differential, but the maternal autoimmune history and early transient-transmission context particularly support transferred antibodies.'),
 ('A congenital myotonic dystrophy mechanism', 'Congenital DM1 can cause severe neonatal hypotonia, but usually reflects maternal DMPK disease rather than maternal autoimmune MG; it has a different inherited mechanism and course.')])

def comparison(title, headers, body):
    matches = [r for r in rows if r['title'] == title]
    assert len(matches) == 1
    matches[0]['table'] = (headers, body)

comparison('MuSK Antibodies and Receptor Clustering',
 ['Target','Relevant mechanism','Clinical implication'],[
 ['AChR','Postsynaptic receptor loss/blockade and complement-mediated injury','AChR-specific evidence for thymectomy and selected C5 inhibitors'],
 ['MuSK','Disrupted clustering signaling; often IgG4','Bulbar/neck phenotype and early rituximab consideration'],
 ['P/Q-type VGCC','Reduced presynaptic calcium-dependent release','LEMS phenotype, facilitation and cancer evaluation']])
comparison('Presynaptic Facilitation in LEMS',
 ['Feature','MG','LEMS'],[
 ['Common weakness emphasis','Ocular/bulbar, neck and proximal limbs','Proximal legs often prominent'],
 ['Reflexes','Usually preserved','Often reduced with postactivation facilitation'],
 ['Autonomic clues','Not a defining feature','Dry mouth and other autonomic symptoms'],
 ['Electrophysiology','Low-frequency decrement; increased jitter','Low resting CMAP; large postexercise increment'],
 ['Common antibody target','AChR or MuSK','P/Q-type calcium channel']])
comparison('Recognizing Dermatomyositis',
 ['Antibody','High-yield associated pattern','Qualification'],[
 ['Mi-2','Classic cutaneous-muscle phenotype','Phenotype association does not establish every complication'],
 ['TIF1-gamma','Cancer-risk assessment','A risk marker, not a cancer diagnosis'],
 ['NXP2','Included in IMACS high-risk factors','Association evidence differs across cohorts'],
 ['MDA5','Amyopathic/hypomyopathic disease and RP-ILD risk','Low CK cannot establish lung safety'],
 ['SAE','Prominent skin disease; possible bulbar involvement','Interpret assay and phenotype together']])
comparison('DM2 and Repeat-Expansion Testing',
 ['Feature','DM1','DM2'],[
 ['Gene/repeat','DMPK CTG','CNBP CCTG'],
 ['Common weakness emphasis','Distal and facial','Proximal/axial; pain may be prominent'],
 ['Myotonia','Often clinically evident','May be mild or less conspicuous'],
 ['Shared concerns','Cardiac, respiratory, cataract, endocrine and anesthesia assessment','Cardiac, respiratory, cataract, endocrine and anesthesia assessment'],
 ['Testing','Validated DMPK expansion assay','Validated CNBP expansion assay']])
comparison('McArdle Disease and Second Wind',
 ['Disorder','Typical trigger or course','Diagnostic direction'],[
 ['McArdle / GSD V','Early exercise cramps; second wind','PYGM-related muscle glycogen phosphorylase deficiency'],
 ['CPT II deficiency','Prolonged exercise, fasting or illness; episodic rhabdomyolysis','CPT2 testing / appropriate enzymology'],
 ['Late-onset Pompe','Progressive axial/limb-girdle and respiratory weakness','GAA activity with biochemical/genetic confirmation'],
 ['Tarui / GSD VII','Exercise intolerance; different response to carbohydrate','PFKM-related phosphofructokinase deficiency']])
comparison('Critical Illness Myopathy Versus Polyneuropathy',
 ['Finding','CIM','CIP'],[
 ['Primary localization','Muscle','Axonal peripheral nerve'],
 ['CMAP amplitude','Often reduced','Often reduced'],
 ['SNAP amplitude','Relatively preserved in isolated CIM','Often reduced'],
 ['Needle EMG','Myopathic units when voluntary assessment is possible','Neurogenic findings in appropriate distribution'],
 ['Clinical caution','Mixed CIM/CIP is common; technique and baseline disease matter','Mixed CIM/CIP is common; technique and baseline disease matter']])

revise('Recognizing Impending Myasthenic Crisis',
 answer='Urgent monitored airway/ventilation assessment and critical-care escalation', others=[
 ('Ward admission for antibiotics with intermittent saturation checks', 'Antibiotics address the trigger, but intermittent saturation monitoring alone does not capture rapidly evolving ventilatory or secretion failure; higher-acuity airway assessment is warranted.'),
 ('A trial of increased oral pyridostigmine before deciding the monitoring setting', 'Symptomatic adjustment can help stable weakness, but choking on saliva and weak cough require urgent airway assessment before waiting to judge an oral drug response.'),
 ('Outpatient prednisone escalation with early telephone review', 'This approach can fit stable disease under a planned protocol, but significant bulbar and respiratory warning features require monitored assessment and possible rescue therapy now.')])
revise('Respiratory Mechanics and Airway Timing',
 answer='Timely endotracheal intubation with continued immune and supportive treatment', others=[
 ('A closely observed noninvasive ventilation trial as the first airway strategy', 'Noninvasive support can be appropriate when airway protection and secretion clearance are effective; their failure here, with rapidly declining reserve, favors intubation.'),
 ('High-flow nasal oxygen with serial saturation-guided escalation', 'High-flow oxygen can help selected hypoxemic disorders, but does not reliably correct neuromuscular ventilation failure or protect this secretion-compromised airway.'),
 ('A short delay for another respiratory-mechanics measurement before intervention', 'Repeating a questionable isolated measurement is reasonable, but the reproducible rapid decline plus paradoxical breathing and secretion failure already supplies independent evidence to act.')])
revise('Rapid Immune Therapy in Severe Exacerbation',
 stem='An adult stabilized in monitored care for severe MG deterioration has no contraindication to either rapid immune modality. Which is an established IVIG rescue regimen?',
 answer='A total of 2 g/kg divided over 2–5 days', others=[
 ('A total of 0.4 g/kg given once, then reassess next month', 'A low single maintenance-style exposure does not match the commonly used full rescue course for severe MG; assess total dose rather than confusing a daily component with the complete regimen.'),
 ('A total of 1 g/kg every three weeks as a fixed induction schedule', 'This resembles a commonly used immunoglobulin maintenance framework in another immune neuropathy context rather than the standard full MG rescue course specified.'),
 ('A total of 2 g/kg administered as a single rapid bolus', 'The total amount resembles the rescue course, but IVIG requires controlled infusion and division according to product and patient risks, not a rapid bolus.')])
revise('Pyridostigmine During Intubated Crisis',
 answer='Temporarily withhold or reduce pyridostigmine, with planned reassessment before reintroduction', others=[
 ('Continue the same dose and add an antimuscarinic for secretions', 'An antimuscarinic can manage selected side effects in stable patients, but the intubated crisis setting warrants reconsidering pyridostigmine itself rather than automatically masking excess secretions.'),
 ('Increase pyridostigmine as the main strategy to accelerate ventilator liberation', 'Symptomatic benefit may help later recovery, but escalation during a secretion-heavy intubated phase can worsen cholinergic burden and does not replace immune rescue.'),
 ('Substitute continuous intravenous pyridostigmine during the intubated period', 'Intravenous cholinesterase inhibition has selected specialist uses but adds secretion and arrhythmic concerns and is not the routine solution to this presentation.')])
revise('Cancer Surveillance After Negative Initial LEMS Imaging',
 answer='Repeat risk-directed screening at approximately 3–6-month intervals for at least two years', others=[
 ('Discharge from cancer surveillance after the negative initial CT', 'One negative study can occur before a tumor becomes detectable; higher-risk LEMS warrants a scheduled surveillance pathway rather than closure.'),
 ('Repeat screening only if new chest symptoms develop', 'Symptoms should trigger earlier investigation, but scheduled screening is important because small-cell lung cancer may remain clinically silent while becoming detectable.'),
 ('Defer repeat screening until five years after the initial CT', 'A long interval misses the period when an occult associated tumor may emerge after neurologic presentation; early risk-directed follow-up is more appropriate.')])
revise('Genotype-Directed Congenital Myasthenia Treatment',
 answer='Salbutamol or ephedrine through a specialist genotype-directed plan', others=[
 ('Pyridostigmine dose escalation', 'Pyridostigmine benefits several CMS subtypes, but DOK7 disease can fail to respond or worsen; the confirmed genotype and prior deterioration argue against escalation.'),
 ('Fluoxetine or quinidine as slow-channel-directed treatment', 'These agents have selected roles in slow-channel CMS under specialist monitoring, but that channel-kinetic mechanism is not established by DOK7 variants.'),
 ('Corticosteroid induction followed by azathioprine', 'This is an autoimmune-MG strategy rather than standard therapy for a confirmed inherited DOK7 transmission defect; seronegativity alone should not redirect the molecular diagnosis.')])
revise('Normal CK Does Not Exclude Myopathy',
 stem='Which disorder can cause progressive proximal muscle weakness despite repeatedly normal CK?',
 answer='Chronic glucocorticoid myopathy', others=[
 ('Active anti-HMGCR necrotizing myopathy', 'Active HMGCR IMNM usually produces substantial CK elevation with proximal weakness; normal values make it less characteristic than chronic steroid myopathy in this comparison.'),
 ('Duchenne muscular dystrophy early in the symptomatic course', 'Early symptomatic Duchenne disease generally has marked CK elevation; chronic glucocorticoid myopathy is a more characteristic normal-CK proximal disorder.'),
 ('Acute rhabdomyolysis after peak enzyme release', 'Rhabdomyolysis typically causes a substantial CK rise after muscle injury; repeatedly normal CK is not its expected biochemical pattern at the stated stage.')])
revise('Myopathic Recruitment on Needle EMG',
 answer='A myopathic motor-unit pattern', others=[
 ('Chronic neurogenic motor-unit remodeling', 'Chronic reinnervation more commonly produces larger, longer-duration units and reduced recruitment; small short units with early recruitment point toward muscle-fiber dysfunction.'),
 ('Reduced recruitment from an acute motor axonal lesion', 'Acute axonal loss reduces the number of available motor units, whereas this early recruitment of small units better fits a myopathic pattern.'),
 ('Reduced central activation without peripheral motor-unit change', 'Poor central activation may limit recruitment, but does not by itself explain the characteristic small short units with early recruitment described.')])
revise('Selecting a Muscle Biopsy Site', others=[
 ('The severely atrophic muscle with maximal fatty replacement', 'A severely affected site may seem attractive, but end-stage destruction can yield nonspecific tissue with too little viable muscle for useful interpretation.'),
 ('A clinically strong muscle without MRI abnormalities', 'A less affected muscle may be appropriate in some diffuse disorders, but an entirely normal site can miss patchy disease when a representative moderately affected site is available.'),
 ('The recently needled portion of the moderately weak muscle', 'EMG can identify an involved target, but biopsy directly through recent needle injury can introduce artifacts; use an appropriate nonneedled site or contralateral counterpart.')])
revise('Rechecking Incidental HyperCKemia', others=[
 ('Obtain muscle MRI and a broad genetic panel immediately', 'MRI and genetics can be useful for persistent unexplained hyperCKemia, but a single postexercise result should first be confirmed after rest and common contributors reviewed.'),
 ('Obtain needle EMG and proceed to biopsy if it is irritable', 'Electrodiagnostics and selected biopsy have later roles, but exercise can transiently raise CK and cause misleading findings; confirm persistence before this invasive sequence.'),
 ('Stop follow-up because a normal examination excludes inherited muscle disease', 'Inherited disorders can initially present through hyperCKemia without weakness, so unexplained persistent elevation still warrants evaluation after transient causes are addressed.')])
revise('Initial Rhabdomyolysis Management', others=[
 ('Start bicarbonate-driven urinary alkalinization with fluids titrated mainly to urine pH', 'Bicarbonate may be appropriate for a separate indication, but routine urine alkalinization has not shown sufficient prevention benefit to replace physiology-directed crystalloid and complication monitoring.'),
 ('Start prophylactic continuous renal replacement therapy to clear myoglobin', 'Renal replacement is appropriate for established indications such as refractory hyperkalemia or overload, not routine prophylaxis based on myoglobin or CK burden alone.'),
 ('Use loop-diuretic-driven urine output as the main target before correcting perfusion', 'Diuretics can treat selected volume-overload states, but forcing urine output does not replace restoring appropriate perfusion and can mislead assessment of resuscitation.')])

revise('Rapid Immune Therapy in Severe Exacerbation',
 stem='An adult has been stabilized in monitored care for severe generalized MG deterioration. Which pair consists of established rapid immune-treatment alternatives for this setting?',
 answer='IVIG or plasma exchange', others=[
 ('Azathioprine or mycophenolate', 'Both have steroid-sparing maintenance roles, but their delayed clinical effect prevents them from substituting for rapid rescue during severe exacerbation.'),
 ('Rituximab or elective thymectomy', 'Both can have important disease-modifying roles in selected MG populations, but neither is the standard immediate rescue alternative to IVIG or exchange in this acute setting.'),
 ('Pyridostigmine or amifampridine', 'These alter transmission symptomatically, with amifampridine mainly used in LEMS; they do not constitute the established rapid immune-treatment pair for severe autoimmune MG.')])
next(r for r in rows if r['title'] == 'Normal CK Does Not Exclude Myopathy')['style'] = 'direct'
revise('Risk-Stratified Cancer Screening in Myositis', others=[
 ('Use routine age/sex-based screening without additional myositis-directed assessment', 'Routine screening remains essential but does not cover the additional IMACS recommendations for this patient’s multiple high-risk factors.'),
 ('Use the moderate-risk assessment pathway', 'Moderate-risk pathways apply to a different combination of features; DM, TIF1-gamma and onset after forty already place this patient in the high-risk category.'),
 ('Use serial tumor markers as the primary enhanced-screening approach', 'Selected markers can form part of a broader protocol, but a marker-only strategy cannot replace clinical evaluation and appropriate imaging in high-risk myositis.')])
revise('Antisynthetase Disease Beyond the Muscle', others=[
 ('Measure respiratory pressures and defer parenchymal imaging pending those results', 'Respiratory-muscle assessment can help, but should not delay direct ILD evaluation in a symptomatic high-risk antisynthetase phenotype.'),
 ('Obtain chest radiography and repeat CK before deciding whether HRCT is needed', 'Radiography and CK may be useful context, but can miss lung disease or dissociate from lung activity; persistent dyspnea warrants more sensitive pulmonary assessment.'),
 ('Assess deconditioning with an exercise program before obtaining lung tests', 'Deconditioning can contribute after illness, but significant ILD must be assessed before assigning persistent dyspnea to fitness alone in this syndrome.')])
revise('Anti-MDA5 and Rapidly Progressive ILD', others=[
 ('Begin glucocorticoid monotherapy and add another agent only after prolonged nonresponse', 'Staged monotherapy can fit selected less aggressive disease, but RP-ILD with suspected MDA5 warrants urgent combination treatment under the conditional guideline recommendation.'),
 ('Begin antifibrotic monotherapy with interval outpatient HRCT', 'Antifibrotics have selected fibrosing-ILD roles, but do not substitute for urgent immune and supportive management of this rapidly deteriorating inflammatory syndrome.'),
 ('Begin low-dose mycophenolate monotherapy with gradual outpatient titration', 'Mycophenolate can be useful in IIM-ILD, but delayed-onset low-dose monotherapy does not meet the urgency and combination-treatment needs of this RP-ILD presentation.')])
revise('Initial Immune Treatment and Objective Follow-up', others=[
 ('Azathioprine monotherapy with observation for its delayed effect', 'Azathioprine can provide steroid-sparing benefit, but delayed monotherapy is usually insufficient induction for disabling active muscle disease without a contraindication to glucocorticoids.'),
 ('Scheduled IVIG as the default first treatment for every inflammatory subtype', 'IVIG has important selected roles, including severe or refractory DM, but is not an interchangeable universal first-line regimen for all non-IBM inflammatory myopathies.'),
 ('Rehabilitation and symptomatic analgesia before initiating immune control', 'Rehabilitation and pain care are important adjuncts, but do not replace treatment of confirmed disabling active immune muscle injury.')])
revise('What ProDERM Established', others=[
 ('IVIG was superior to rituximab for the week-16 composite response', 'ProDERM was placebo controlled, so it cannot establish superiority to an active rituximab regimen that was not its randomized comparator.'),
 ('IVIG produced the same randomized benefit in inclusion body myositis', 'The population had adult DM; a different disease phenotype cannot inherit the same trial conclusion without its own evidence.'),
 ('A single IVIG course established durable drug-free remission', 'The randomized phase used repeated four-weekly treatment and measured composite response at sixteen weeks; it did not demonstrate durable remission after one isolated course.')])
revise('Cardiac Risk in a Female DMD Variant Carrier', others=[
 ('Reproductive counseling with cardiac evaluation only if symptoms emerge', 'Counseling is necessary, but symptoms alone can miss early cardiomyopathy in a heterozygous woman; baseline and ongoing organ assessment are appropriate.'),
 ('Annual CK surveillance with cardiac imaging triggered by a rising CK', 'CK can help describe skeletal involvement but cannot reliably gate cardiac risk; heart disease may occur without a parallel skeletal enzyme change.'),
 ('A one-time baseline ECG with no further testing if it is normal', 'An initial ECG is useful, but does not exclude evolving structural disease or remove the need for a longitudinal cardiac assessment plan.')])

revise('FSHD Requires the Right Molecular Test', others=[
 ('DMPK CTG-repeat expansion testing', 'DMPK testing is appropriate for myotonic dystrophy with myotonia and systemic features; the asymmetric facial-scapular distribution instead directs testing toward FSHD.'),
 ('DMD deletion/duplication and sequence analysis', 'Dystrophin testing fits an X-linked dystrophinopathy phenotype, often with substantial CK elevation and a different distribution; it does not resolve the characteristic FSHD repeat mechanism.'),
 ('PABPN1 repeat analysis', 'PABPN1 testing fits late-onset familial ptosis and dysphagia; the facial-scapular phenotype here is more characteristic of FSHD.')])
revise('A Limb-Girdle Pattern Is Not One Genetic Diagnosis', others=[
 ('Start with one recessive-dystrophy gene selected from proximal weakness alone', 'Single-gene testing can be efficient for a distinctive phenotype, but this broad distribution without subtype-specific clues does not identify one recessive cause.'),
 ('Start immune treatment and reserve molecular assessment for treatment failure', 'Inflammatory disease requires supporting context; familial progressive weakness can be inherited, so empirical immune escalation should not delay an appropriate genetic evaluation.'),
 ('Perform biopsy first and assign inheritance from the histologic pattern', 'Biopsy has selected diagnostic value, but similar dystrophic changes occur across genes and do not independently determine a pedigree or inheritance mechanism.')])
revise('DM1: Myotonia Is Only One Part of the Risk', others=[
 ('Grip-relaxation timing and EMG discharge burden', 'These characterize myotonia, but do not adequately assess silent conduction abnormalities, ventilatory reserve or sedative sensitivity before surgery.'),
 ('CK and conventional proximal-muscle EMG', 'These may describe muscle disease but cannot substitute for cardiac and respiratory assessment in molecularly confirmed multisystem DM1.'),
 ('Repeat-expansion size as the principal perioperative risk predictor', 'Repeat size informs the molecular diagnosis and broad counseling, but does not precisely predict individual cardiac, respiratory or anesthetic risk; direct organ assessment is needed.')])
revise('Progressive External Ophthalmoplegia and Tissue Testing', others=[
 ('Repeat the identical blood deletion assay as the sole next investigation', 'Repeat testing can address sample-quality concerns, but a sensitive negative blood assay may reflect tissue distribution or a nuclear cause; repeating it alone may leave the key limitation unresolved.'),
 ('Treat as seronegative MG on the basis of ptosis alone', 'Ptosis occurs in both groups, but fixed progressive ophthalmoplegia with multisystem clues and unrevealing MG evaluation warrants targeted mitochondrial reassessment before immune treatment.'),
 ('Restrict further testing to maternally inherited point mutations in blood', 'Mitochondrial ophthalmoplegia can involve large deletions, multiple deletions or nuclear genes, so limiting testing to one mutation category and specimen is inadequate.')])
revise('Potassium During Familial Hypokalemic Paralysis', others=[
 ('Give intravenous KCl as the initial route despite safe swallowing and stable physiology', 'Intravenous therapy is appropriate for selected severe or unsafe-swallowing cases, but cautious oral dosing avoids unnecessary IV replacement risk in this stable attack.'),
 ('Give a large potassium dose calculated from a total-body depletion formula', 'That framework can apply to genuine depletion, but a classic redistribution attack risks overshoot when the shift reverses; incremental reassessment is preferable.'),
 ('Start acetazolamide as the sole acute rescue', 'Acetazolamide has a genotype-dependent preventive role, but does not replace correction and monitoring of significant potassium abnormalities during an established attack.')])
revise('Thyrotoxic Periodic Paralysis', others=[
 ('Use potassium replacement followed by long-term acetazolamide prophylaxis', 'This transfers a familial-paralysis preventive strategy without treating the thyroid driver; euthyroid control and cautious shift-directed acute management are central in TPP.'),
 ('Use antithyroid therapy alone while observing the severe hypokalemia', 'Thyroid treatment prevents recurrence but takes time; marked hypokalemia and acute weakness also need immediate monitored management according to ECG and clinical severity.'),
 ('Use large rapid potassium replacement as for a comparable depletion syndrome', 'Renal or GI depletion may require substantial replacement, but TPP mainly redistributes potassium and creates a rebound risk with aggressive dosing.')])
revise('Nondystrophic Myotonia and Mexiletine Safety', others=[
 ('CK and liver tests before starting, with cardiac testing only if palpitations develop', 'Laboratory tests may be useful, but asymptomatic cardiac abnormalities or interactions can affect mexiletine safety; baseline cardiac evaluation should not wait for palpitations.'),
 ('Exercise EMG before starting, with ECG only after reaching the maintenance dose', 'Exercise electrophysiology can characterize channelopathy, but does not replace cardiac risk assessment before exposing the patient to an antiarrhythmic drug.'),
 ('Repeat CLCN1 sequencing before starting, with ECG if the variant changes', 'A concordant established genotype does not require repeat sequencing to guide this safety decision; cardiac and electrolyte review directly addresses treatment risk.')])
revise('Glucocorticoid Myopathy Versus Active Myositis', others=[
 ('Relapsing inflammatory myopathy', 'Relapse remains possible and normal CK does not exclude it, but gradual painless weakness with quiet associated disease during high-dose steroids specifically warrants assessment for steroid toxicity.'),
 ('Inclusion body myositis', 'IBM is a relevant alternative in selected nonresponders, but usually has a characteristic chronic selective pattern; the supplied treatment-linked proximal course favors steroid myopathy.'),
 ('Critical illness myopathy', 'CIM is associated with a suitable severe systemic illness/ICU course, which is not supplied here; chronic glucocorticoid exposure offers the more direct explanation.')])
revise('Colchicine Neuromyopathy and Drug Interaction', others=[
 ('Anti-HMGCR immune-mediated necrotizing myopathy', 'IMNM can cause marked proximal weakness and CK elevation, but the new renal/exposure interaction is a stronger immediate explanation; persistent discordant disease may justify immune evaluation.'),
 ('Clarithromycin-triggered autoimmune MG', 'Macrolides can worsen transmission in susceptible patients, but CK elevation, myalgia and sensory findings with colchicine exposure point to toxic neuromyopathy rather than isolated MG.'),
 ('Chronic uremic polyneuropathy', 'Uremic neuropathy may contribute distal sensory disease, but does not account as directly for the abrupt proximal muscle injury after a high-risk colchicine interaction.')])
revise('Checkpoint-Inhibitor Neuromuscular–Cardiac Overlap', others=[
 ('Hold the checkpoint inhibitor and investigate isolated MG before considering muscle or cardiac involvement', 'Holding the drug is appropriate, but CK/troponin abnormalities and the known overlap risk require parallel assessment rather than delaying the other potentially lethal components.'),
 ('Hold the checkpoint inhibitor and investigate isolated myositis before assessing transmission', 'Muscle injury is present, but bulbar/ocular weakness can include MG and carries airway risk; evaluating only myositis can miss a concurrently treatable transmission disorder.'),
 ('Hold the checkpoint inhibitor and defer monitored care until biopsy confirms an immune process', 'Tissue can help clarify diagnosis, but cardiac and respiratory toxicity can deteriorate rapidly; monitored evaluation should precede definitive biopsy confirmation.')])

screen = next(r for r in rows if r['title'] == 'Risk-Stratified Cancer Screening in Myositis')
screen['sections'].append(S('Screening Interval',
 '**High-risk adult IIM warrants basic and enhanced screening at diagnosis, followed by basic screening annually for three years** under IMACS 2023, in addition to routine population programmes.',
 'These recommendations apply within the guideline disease-onset context and do not mean automatic annual whole-body CT indefinitely. Reassess symptoms, baseline results and local cancer epidemiology.'))

def highlight_values(value):
    if isinstance(value, str):
        parts = re.split(r'(==.*?==)', value)
        pattern = r'(?<![\w.])(?:\d+(?:\.\d+)?(?:[–-]\d+(?:\.\d+)?)?\s*(?:g/kg(?:/day)?|mg/kg(?:/day)?|mg/day|mEq/kg|mL/kg(?:/hour)?|mL/hour|%))'
        return ''.join(p if p.startswith('==') else re.sub(pattern, lambda m: '=='+m.group(0)+'==', p) for p in parts)
    if isinstance(value, (list, tuple)):
        return type(value)(highlight_values(v) for v in value)
    return value

for row in rows:
    row['sections'] = highlight_values(row['sections'])
    row['table'] = highlight_values(row['table'])

if __name__ == '__main__':
    coverage = ROOT/'Neurology/10. Neuromuscular Junction Disorders & Muscle Diseases.coverage.json'
    c = json.loads(coverage.read_text(encoding='utf-8'))
    assert len(rows) == sum(s['questions'] for s in c['sections']) == c['plannedQuestions'], 'Chapter incomplete; do not install'
    index = 0
    for section in c['sections']:
        for decision in section['decisions']:
            assert rows[index]['topic'] == section['section']
            rows[index]['coverageDecision'] = decision
            index += 1
    save('Neurology',10,c['chapter'],rows,R,'Original postgraduate synthesis. Source versions and drug-label jurisdictions are specified where relevant. Full Harrison subscription text was not accessed; no independent clinician review is claimed.')
    c.update(status='authored_validated',authoredQuestions=len(rows))
    c['questionDecisions'] = [dict(question=i+1,title=r['title'],decision=r['coverageDecision']) for i,r in enumerate(rows)]
    coverage.write_text(json.dumps(c,ensure_ascii=False,indent=2),encoding='utf-8')
