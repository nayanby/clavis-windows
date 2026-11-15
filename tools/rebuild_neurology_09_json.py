"""Original peripheral neuropathy chapter with explicit decision coverage."""
import json
import re
from qbank_json_chapters import question as Q, save, ROOT
R = {
 'DSP': ('AAN/AANEM/AAPMR practice parameter: laboratory and genetic evaluation of DSP, 2009', 'https://pubmed.ncbi.nlm.nih.gov/19056666/'),
 'APPROACH': ('AAPM&R: Peripheral polyneuropathy evaluation and differential diagnosis, updated 2026', 'https://now.aapmr.org/approach-to-peripheral-polyneuropathy-evaluation-and-differential-diagnosis/'),
 'GBS': ('EAN/PNS guideline on diagnosis and treatment of GBS, 2023', 'https://doi.org/10.1111/jns.12594'),
 'CIDP': ('EAN/PNS CIDP guideline, second revision, 2021', 'https://doi.org/10.1111/ene.14959'),
 'PDN': ('AAN painful diabetic polyneuropathy treatment guideline update, 2021/2022', 'https://pubmed.ncbi.nlm.nih.gov/34965987/'),
}
def S(h, main, *children): return (h, [(main, list(children))])
rows = []
def add(*a, **kw): rows.append(Q(*a, **kw))

add('Clinical and electrodiagnostic approach', 'Pattern Recognition Before Etiologic Testing',
 'A patient has eighteen months of symmetric burning and numbness beginning in the toes and advancing to the calves, with reduced ankle reflexes and mild distal weakness. Which pattern best fits?',
 'A length-dependent distal symmetric polyneuropathy', [
 ('A multifocal mononeuropathy pattern', 'Mononeuritis multiplex causes deficits in separate named nerves, often asymmetric or stepwise, rather than a symmetric stocking progression.'),
 ('A sensory neuronopathy pattern', 'A ganglionopathy often has non-length-dependent, asymmetric sensory loss and prominent proprioceptive ataxia; the distal symmetric evolution here suggests a different distribution.'),
 ('An isolated lumbosacral radiculoplexus syndrome', 'Radiculoplexus disease often begins with pain and asymmetric proximal weakness across several root/nerve territories, unlike this slowly length-dependent distal syndrome.')],
 [S('Define the Phenotype', '**Distribution, tempo and fiber involvement** organize neuropathy evaluation. Length-dependent disorders usually affect the longest axons first, producing distal foot symptoms before hand involvement.',
    'Describe sensory modalities, motor weakness, reflexes and autonomic features. Small-fiber pain can precede obvious weakness or large-fiber sensory loss.',
    'Do not equate a stocking pattern with one cause. Diabetes, alcohol/nutritional disease, renal disease, paraproteinemia, drugs and inherited disorders can produce similar distributions.'),
  S('Features That Change the Pathway', '**Rapid progression, marked asymmetry, proximal weakness, substantial motor involvement or systemic illness** warrant an expanded and often expedited evaluation rather than a routine idiopathic-DSP label.',
    'Electrodiagnostics help classify large-fiber disease and identify an axonal, demyelinating or multifocal pattern. A normal routine study does not exclude small-fiber neuropathy.',
    'Use a high-yield initial laboratory strategy and targeted testing guided by the phenotype. Broad indiscriminate antibody/genetic panels can create incidental findings without resolving the clinical problem.')], ['APPROACH','DSP'])

add('Clinical and electrodiagnostic approach', 'Axonal Loss Versus Primary Demyelination',
 'Nerve conduction studies show markedly reduced distal motor and sensory amplitudes with only mild slowing proportional to the low responses. Which interpretation is most appropriate?',
 'Predominantly axonal neuropathy is favored; mild slowing alone does not establish primary demyelination', [
 ('Definite acquired demyelination from any velocity below the reference range', 'Mild slowing can accompany axonal loss, temperature effects or technical factors; acquired demyelination requires specified abnormalities and a compatible clinical setting.'),
 ('An isolated NMJ transmission disorder as the explanation of reduced sensory responses', 'NMJ disorders can affect motor transmission but usually preserve sensory nerve responses; reduced SNAP amplitudes indicate a different or additional process.'),
 ('A pure myopathy as the sufficient explanation of the sensory abnormalities', 'Myopathy can reduce motor output in severe cases, but does not usually cause a generalized sensory nerve-response reduction.')],
 [S('Amplitude and Timing', '**Reduced SNAP and CMAP amplitudes** commonly reflect loss of functioning sensory and motor axons. Demyelination is supported by sufficiently marked slowing, prolonged distal/F-wave latencies, conduction block or temporal dispersion in the appropriate pattern.',
    'Loss of the fastest axons can mildly slow a response without primary myelin disease. Severe axonal loss can also make latency/velocity interpretation unreliable.',
    'Needle EMG can demonstrate denervation and chronic neurogenic remodeling, helping assess distribution, chronicity and severity.'),
  S('Clinical Integration', '**CIDP is not diagnosed from the word slow.** Apply validated multi-nerve criteria, exclude entrapment and technical explanations, and require a compatible clinical syndrome.',
    'Inherited demyelinating disease often has more uniform slowing, while acquired disease may be heterogeneous, but there are exceptions and patterns overlap.',
    'Electrophysiological classification guides the differential and treatment; it does not by itself identify diabetes, vasculitis, a specific antibody or a genetic cause. Repeat a limited early study when the disease evolution or technical quality justifies it.')], ['CIDP','APPROACH'])

add('Clinical and electrodiagnostic approach', 'Technical Pitfalls in Apparent Demyelination',
 'A cold hand has prolonged distal latencies and slow conduction. The proximal response is small after difficult stimulation near an entrapment site. Which next step is best before diagnosing acquired demyelination?',
 'Warm the limb and verify supramaximal stimulation, waveform quality and appropriate segments', [
 ('Count the apparent abnormalities as definite CIDP without technical review', 'Temperature, inadequate stimulation and entrapment can mimic relevant findings; their presence undermines an unqualified demyelinating interpretation.'),
 ('Use an elevated CSF protein to validate any technically uncertain conduction block', 'CSF protein is supportive only in context and cannot turn an unreliable waveform into valid electrodiagnostic evidence.'),
 ('Ignore the low distal response because amplitude never affects interpretation', 'Low CMAP amplitude can reflect axonal loss and alter the reliability of demyelinating criteria; amplitude-dependent rules and exclusions matter.')],
 [S('Ensure a Valid Study', '**Temperature and stimulation quality** directly affect measured conduction. Cold limbs can prolong latencies and slow velocity; submaximal proximal stimulation can falsely resemble conduction block.',
    'Verify electrode placement, distance, waveform morphology and relevant anatomical variants. Temporal dispersion and phase cancellation can reduce proximal amplitude without the same implication as a true focal failure.',
    'Entrapment segments must be interpreted separately; slowing only at a common compression site is not proof of generalized immune demyelination.'),
  S('Avoid Treatment Based on Artifact', '**Apply the criterion’s technical and amplitude qualifications** before counting an abnormality. A multi-nerve clinical/electrophysiological pattern is more informative than one doubtful segment.',
    'Repeat or extend the study when technical uncertainty or early disease limits interpretation. The appropriate response is improved evidence, not automatic immunotherapy.',
    'Clinical weakness, reflex loss, sensory distribution and time course must remain concordant. Subjective improvement after treatment or a modest protein rise does not compensate for an implausible syndrome or invalid testing.')], ['CIDP','APPROACH'])

add('Clinical and electrodiagnostic approach', 'Small-Fiber Neuropathy with Normal Nerve Conduction',
 'A patient has burning feet, allodynia and impaired pin/temperature sensation, with preserved strength, vibration and routine nerve conduction studies. Which investigation most directly assesses structural small-fiber loss?',
 'Skin biopsy with age- and site-adjusted intraepidermal nerve-fiber density', [
 ('Repeat routine motor conduction alone as a sensitive small-fiber assay', 'Routine conduction chiefly assesses large myelinated fibers and can remain normal in pure small-fiber disease; repeating it alone does not directly quantify small-fiber structure.'),
 ('Needle EMG as the primary direct measure of cutaneous sensory fibers', 'Needle EMG assesses motor-unit activity and denervation, not intraepidermal small sensory-fiber density.'),
 ('A normal vibration threshold as proof that neuropathy is absent', 'Vibration predominantly tests large-fiber function; preservation is compatible with a small-fiber syndrome and cannot exclude it.')],
 [S('Fiber-Selective Clinical Pattern', '**Small-fiber neuropathy** affects thinly myelinated Aδ and unmyelinated C fibers, producing burning pain, altered thermal/pin sensation and sometimes autonomic symptoms.',
    'Strength, tendon reflexes and large-fiber sensory modalities may remain relatively preserved early. Normal routine electrodiagnostics therefore do not resolve the question.',
    'Skin biopsy evaluates intraepidermal fiber density using validated age/site reference data. A symptom alone or one unvalidated cutoff is insufficient for a confident etiologic diagnosis.'),
  S('Functional Testing and Etiology', '**Quantitative sensory and autonomic/sudomotor tests** can provide complementary evidence, but some depend on cooperation and none by itself identifies every cause.',
    'Assess glucose dysregulation, B12, paraproteins, medications and phenotype-directed immune, infectious or inherited causes. Testing should be proportional to the presentation.',
    'Treat the cause when found and address neuropathic pain, sleep and function. A reduced fiber count supports small-fiber injury but should not be equated with proof of an autoimmune mechanism or automatic IVIG eligibility.')], ['APPROACH'])

add('Clinical and electrodiagnostic approach', 'Testing a Peripheral Autonomic Syndrome',
 'A patient with neuropathic pain has orthostatic symptoms, altered sweating and bowel dysmotility. Which test strategy best evaluates autonomic involvement?',
 'A standardized autonomic battery assessing cardiovagal, adrenergic and sudomotor function', [
 ('A single seated blood-pressure reading as a complete autonomic evaluation', 'A seated value can miss postural abnormalities and does not assess cardiovagal or sudomotor function.'),
 ('Motor nerve conduction alone as a sufficient autonomic study', 'Routine motor conduction does not directly assess the small autonomic fibers and physiological reflexes involved in this syndrome.'),
 ('Plasma catecholamines alone as a universal etiologic diagnosis', 'Catecholamine measurements can help selected questions but do not replace standardized physiological testing or establish one cause in every autonomic presentation.')],
 [S('Physiological Domains', '**Autonomic testing** may include HR responses to deep breathing/Valsalva, BP responses to Valsalva and tilt/standing, and sudomotor evaluation such as QSART according to the laboratory protocol.',
    'Medication effects, hydration, cardiac rhythm, temperature and patient preparation influence results. A test report must be interpreted with these confounders and validated reference values.',
    'A postural BP fall supports OH but does not independently distinguish dehydration, medication effect and neurogenic failure.'),
  S('Peripheral Versus Broader Autonomic Disease', '**Diabetes, amyloid, immune autonomic disease and other neuropathies** can cause autonomic symptoms. Central autonomic disorders and non-neurological causes remain competing explanations.',
    'Look for rapid progression, weight loss, cardiomyopathy, severe GI dysfunction, urinary retention and other clues that justify targeted evaluation.',
    'Treatment includes cause-directed care and symptom management with attention to supine hypertension, volume status and interacting drugs. Physiological confirmation identifies affected domains rather than automatically assigning an antibody diagnosis.')], ['APPROACH'])

add('Clinical and electrodiagnostic approach', 'High-Yield Laboratory Screening for DSP',
 'Which group contains the high-yield laboratory tests emphasized by the AAN/AANEM/AAPMR practice parameter for otherwise unexplained distal symmetric polyneuropathy?',
 'Glucose assessment, B12 with functional metabolites when appropriate, and serum protein immunofixation', [
 ('An indiscriminate neuronal-antibody panel without metabolic or paraprotein testing', 'Immune testing is selected for compatible phenotypes; it does not replace high-yield screening for glucose, nutritional and monoclonal-protein causes.'),
 ('Routine nerve biopsy before basic laboratory investigation', 'Biopsy has selected roles such as suspected vasculitis or amyloid but is invasive and is not routine initial testing for a typical length-dependent DSP.'),
 ('A broad genetic panel for every adult before phenotype or pedigree review', 'Genetic testing is important with an inherited phenotype, but indiscriminate first-line use can generate uncertain variants and miss common acquired causes.')],
 [S('High-Yield Treatable or Actionable Causes', '**Blood glucose, serum B12 with appropriate metabolites and serum protein immunofixation** are the highest-yield tests identified by the 2009 practice parameter.',
    'Fasting glucose/HbA1c are commonly used; an oral glucose-tolerance test may be considered when routine testing does not establish diabetes and the phenotype suggests dysglycemia.',
    'Methylmalonic acid helps clarify a borderline B12 result, while renal impairment can elevate it independently. Immunofixation can detect small monoclonal proteins not obvious on routine electrophoresis alone.'),
  S('Broader Initial Assessment', '**CBC, renal/hepatic function, electrolytes and targeted additional tests** complement the core evaluation according to the presentation and local protocol.',
    'Review alcohol, drugs, supplements, systemic symptoms and family history before selecting more specialized studies. Asymmetry, rapid progression or marked motor/proximal disease changes the differential.',
    'A monoclonal protein may be incidental, and diabetes may coexist with another neuropathy. Test results require phenotype-based interpretation rather than automatic closure of the diagnostic process.')], ['DSP','APPROACH'], style='direct')

R['GBS10'] = ('International consensus: GBS diagnosis and management in ten steps, 2019', 'https://doi.org/10.1038/s41582-019-0250-9')
R['SID'] = ('SID-GBS randomized placebo-controlled second-IVIG trial, 2021', 'https://pubmed.ncbi.nlm.nih.gov/33743237/')

add('Guillain-Barre syndrome', 'Recognizing the Acute GBS Syndrome',
 'Ten days after diarrhea, an adult develops progressive symmetric leg then arm weakness over five days, distal paresthesias and generalized areflexia. There is no sensory level. Which diagnosis is most likely?',
 'Guillain–Barre syndrome', [
 ('Typical CIDP', 'CIDP can resemble GBS initially, but its usual progression extends beyond eight weeks; this acute postinfectious course favors GBS while longitudinal follow-up remains important.'),
 ('Acute spinal cord compression', 'Cord compression is an urgent mimic, especially with back pain, a sensory level or sphincter/upper motor neuron signs; the generalized areflexic peripheral pattern here is more suggestive of GBS.'),
 ('Myasthenia gravis', 'MG causes fatigable motor weakness, often ocular/bulbar, with preserved sensation and usually preserved reflexes; paresthesias and generalized areflexia favor a polyradiculoneuropathy.')],
 [S('Clinical Diagnosis', '**GBS is an acute immune polyradiculoneuropathy**, usually reaching nadir within four weeks. Progressive bilateral weakness and reduced reflexes are central features of the typical motor-sensory syndrome.',
    'Antecedent respiratory or gastrointestinal infection, pain, cranial involvement and autonomic dysfunction can support the diagnosis. An infection history is not mandatory.',
    'Variants can differ from the classic ascending pattern, and reflexes can occasionally be preserved in selected motor forms. Avoid an absolute rule based on one absent textbook feature.'),
  S('Immediate Evaluation', '**Assess respiratory, bulbar and autonomic function early**, not only limb power. CSF and electrodiagnostics support diagnosis but can be nondiagnostic early.',
    'Cord disease, acute flaccid myelitis, toxic/metabolic paralysis, botulism and NMJ disorders require consideration according to the examination and exposures.',
    'A sensory level, marked persistent asymmetry, substantial pleocytosis or a strongly atypical time course should trigger reassessment. Do not delay indicated treatment in a convincing rapidly progressive syndrome solely while waiting for every supportive test.')], ['GBS','GBS10'])

add('Guillain-Barre syndrome', 'CSF in the First Week of GBS',
 'On day four of progressive areflexic weakness, CSF protein is within the laboratory reference range and the cell count is 2/µL. Which interpretation is best?',
 'A normal early protein does not exclude GBS', [
 ('GBS is excluded until protein becomes elevated', 'Protein elevation may be absent early, and waiting for its appearance can delay time-sensitive clinical management.'),
 ('The low cell count establishes a specific demyelinating GBS subtype', 'A low cell count can support the overall syndrome but does not distinguish AIDP from axonal/nodal forms; electrophysiology and clinical course provide different information.'),
 ('Albuminocytological dissociation is required in every patient before treatment', 'It is a supportive finding, not a prerequisite that must be demonstrated before treating a convincing severe syndrome.')],
 [S('Timing of Albuminocytological Dissociation', '**Elevated CSF protein with few cells** is characteristic but often develops after the first days. A normal protein during week one is therefore compatible with GBS.',
    'Interpret protein using age, laboratory method and the complete differential. An elevated value alone is nonspecific and does not establish the diagnosis.',
    'CSF can be useful for detecting a mimic even when it does not yet provide the expected protein pattern.'),
  S('When Cells Change the Differential', '**Marked pleocytosis, especially above 50 cells/µL**, raises concern for infection, inflammation, malignancy or another diagnosis. Lesser pleocytosis also requires contextual review rather than automatic dismissal.',
    'Consider HIV-related disease, Lyme disease where relevant, infectious radiculitis and other causes according to exposure and immune status.',
    'Continue respiratory/bulbar monitoring and electrodiagnostic evaluation. Repeat testing may be useful when uncertainty persists, but a lumbar puncture result should not override a clearly evolving neurological emergency.')], ['GBS','GBS10'])

add('Guillain-Barre syndrome', 'Axonal GBS and Reversible Conduction Failure',
 'A patient with acute pure motor GBS has low motor amplitudes, preserved sensory responses and an early apparent motor block that resolves without temporal dispersion on serial testing. Which mechanism is particularly relevant?',
 'Reversible nodal conduction failure in an AMAN-spectrum process', [
 ('Every early conduction block proves permanent segmental demyelination', 'Nodal dysfunction in axonal-spectrum GBS can cause transient failure; serial recovery without dispersion can distinguish it from a simple assumption of demyelination.'),
 ('AMSAN as established despite preserved sensory studies', 'AMSAN includes sensory axonal involvement; preserved SNAPs and a pure motor presentation more strongly support AMAN, allowing for timing and test limitations.'),
 ('A pure myopathy as the cause of the nerve conduction block', 'Myopathy has a different electrophysiological pattern and does not explain a serially evolving focal nerve-conduction failure in this acute areflexic syndrome.')],
 [S('Electrophysiological Spectrum', '**AIDP** has demyelinating features, while **AMAN** predominantly affects motor axons/nodes and **AMSAN** includes sensory axonal involvement.',
    'Early nodal dysfunction can be reversible and can mimic demyelinating block before the course clarifies. Low CMAP amplitude does not invariably imply irreversible axonal degeneration.',
    'Serial studies can therefore change subtype classification; technical factors and timing must be reviewed.'),
  S('What Subtyping Does and Does Not Determine', '**Treatment is driven by the clinical GBS syndrome and severity**, not by waiting for a stable subtype label. IVIG or plasma exchange can be appropriate across the major forms.',
    'Anti-ganglioside antibodies and antecedent Campylobacter can be associated with axonal forms, but routine antibody testing has limited value in typical motor-sensory GBS.',
    'A sural-sparing sensory pattern can support GBS in context, but is neither obligatory nor uniquely diagnostic. Prognosis depends on clinical severity, respiratory involvement and recovery trajectory as well as electrophysiology.')], ['GBS','GBS10'], table=(['Pattern','Typical emphasis','Qualification'],[
 ['AIDP','Demyelinating abnormalities','Early studies may be equivocal'],['AMAN','Motor axonal/nodal dysfunction; sensory sparing','Reversible failure can mimic block'],['AMSAN','Motor and sensory axonal involvement','Amplitude loss needs timing/technical interpretation']]))

add('Guillain-Barre syndrome', 'Miller Fisher Syndrome',
 'After a respiratory illness, a patient develops ophthalmoplegia, marked gait ataxia and areflexia with little limb weakness. Which antibody is most specifically associated with the suspected syndrome?',
 'Anti-GQ1b IgG', [
 ('Anti-AChR antibodies', 'AChR antibodies support autoimmune MG in a compatible fatigable motor syndrome, but do not explain the classic ophthalmoplegia–ataxia–areflexia combination.'),
 ('Anti-MAG antibodies', 'Anti-MAG is associated with a chronic distal sensory/demyelinating IgM neuropathy, not this acute postinfectious ophthalmoplegic syndrome.'),
 ('Anti-LGI1 antibodies', 'LGI1 antibodies are associated with limbic disease and faciobrachial dystonic seizures, rather than an acute peripheral ophthalmoplegic–ataxic syndrome.')],
 [S('Clinical Triad', '**Miller Fisher syndrome** classically combines ophthalmoplegia, ataxia and areflexia. It lies within the anti-GQ1b-associated GBS spectrum.',
    'Some patients develop overlap with limb, bulbar or respiratory GBS features, so the initially limited syndrome still requires observation.',
    'Anti-GQ1b testing is particularly useful when MFS is suspected, unlike indiscriminate antibody panels in every typical motor-sensory GBS case.'),
  S('Related Syndromes and Management', '**Bickerstaff brainstem encephalitis** shares ophthalmoplegia and ataxia but includes impaired consciousness and/or central signs such as hyperreflexia. Wernicke disease and brainstem lesions are important alternative diagnoses.',
    'Pure uncomplicated MFS often improves with supportive care, and robust evidence that immunotherapy changes its usually favorable course is limited. Overlap with disabling generalized GBS changes the treatment decision.',
    'Monitor swallowing, breathing, autonomic status and progression, and assess structural or nutritional mimics when the phenotype is atypical. Antibody positivity supports the syndrome but is not a substitute for emergency clinical evaluation.')], ['GBS','GBS10'])

add('Guillain-Barre syndrome', 'Pharyngeal–Cervical–Brachial GBS',
 'A patient develops acute bulbar, neck and arm weakness with reduced arm reflexes after an infection. Legs are relatively spared and there is no clear fatigability. Which GBS variant is particularly suggested?',
 'Pharyngeal–cervical–brachial variant', [
 ('Miller Fisher syndrome without overlap', 'MFS is defined by ophthalmoplegia, ataxia and areflexia; predominant oropharyngeal/neck/arm weakness suggests PCB, though overlap can occur.'),
 ('Pure sensory ataxic GBS', 'A sensory ataxic variant is led by sensory/proprioceptive dysfunction rather than this regional motor and bulbar pattern.'),
 ('Paraparetic GBS', 'Paraparetic GBS predominantly affects the legs, the opposite distribution from this neck–bulbar–arm presentation.')],
 [S('Regional Motor Variant', '**PCB GBS** predominantly affects the oropharyngeal, cervical and brachial muscles, with regional hyporeflexia and relative leg sparing. Anti-GT1a antibodies are an important association.',
    'It can be mistaken for MG, botulism, brainstem stroke or a cervical lesion. The time course, reflexes, sensory/autonomic findings and electrodiagnostics help separate these.',
    'MFS/anti-GQ1b-spectrum overlap is possible; a regional label does not guarantee a permanently limited course.'),
  S('Bulbar and Respiratory Safety', '**Severe bulbar weakness can require airway protection** even without profound leg weakness or a low walking score. Monitor cough, secretion handling and respiratory function.',
    'Assess pupils and autonomic symptoms when botulism is plausible, fatigability/NMJ testing for MG, and focal central signs/imaging when brainstem disease is possible.',
    'Use IVIG or plasma exchange when the clinical severity and GBS treatment context justify it. Do not deny urgent treatment or monitored care merely because the patient can still move the legs.')], ['GBS','GBS10'])

add('Guillain-Barre syndrome', 'Respiratory Failure Despite Normal Oxygen Saturation',
 'A patient with GBS has a falling vital capacity of 18 mL/kg, weak cough and bulbar dysfunction, but room-air oxygen saturation is 98%. What is the best next approach?',
 'Escalate to closely monitored respiratory/airway assessment and plan timely ventilatory support', [
 ('Continue ward observation based solely on the normal oxygen saturation', 'Neuromuscular ventilatory failure can precede hypoxemia; saturation is an inadequate stand-alone measure of respiratory reserve.'),
 ('Wait for severe hypercapnia before considering airway intervention', 'Hypercapnia may be a late sign and can make an avoidable urgent airway crisis more likely; serial mechanics and bulbar status should guide earlier planning.'),
 ('Use noninvasive ventilation as an automatic substitute for airway protection despite severe bulbar dysfunction', 'Noninvasive support may be unsuitable when secretion handling and aspiration protection are poor; airway decisions require individualized critical-care assessment.')],
 [S('Serial Respiratory Function', '**Monitor vital capacity, inspiratory/expiratory strength, cough and bulbar function**, with attention to trends. Clinical work of breathing and rapid deterioration can be more important than one measurement.',
    'The classic risk screen is the 20/30/40 rule: VC below 20 mL/kg, maximal inspiratory pressure magnitude below 30 cmH2O or maximal expiratory pressure below 40 cmH2O.',
    'For a negative inspiratory-force reading, less negative values indicate weakness; stating magnitude avoids reversing the sign convention.'),
  S('Airway Timing', '**VC around 15–20 mL/kg or a rapid fall is concerning**, especially with weak cough, bulbar dysfunction or inability to manage secretions. These are warning thresholds, not a substitute for clinical judgement.',
    'Do not wait for desaturation or a dramatic blood-gas abnormality. Arrange ICU-level review and an airway plan before exhaustion or aspiration occurs.',
    'Continue autonomic monitoring and supportive measures; treatment with IVIG or plasma exchange does not immediately remove the need for ventilation. Repeated objective assessment is required through progression and recovery.')], ['GBS','GBS10'])

add('Guillain-Barre syndrome', 'What the Original EGRIS Predicts',
 'Which combination forms the original Erasmus GBS Respiratory Insufficiency Score?',
 'Time from weakness onset to admission, facial/bulbar weakness and admission MRC sum score', [
 ('Age, preceding diarrhea and MRC score to predict later walking outcome', 'Those variables relate to the modified Erasmus outcome-score framework; EGRIS is specifically a respiratory-risk model with different inputs.'),
 ('CSF protein, anti-GQ1b titre and sural amplitude', 'These can be relevant diagnostically in selected contexts, but are not the original EGRIS clinical input set.'),
 ('Oxygen saturation, serum sodium and creatinine alone', 'These values matter clinically but do not constitute the validated original EGRIS prediction model.')],
 [S('Respiratory-Risk Model', '**Original EGRIS estimates early mechanical-ventilation risk** using clinical severity, speed of progression and cranial/bulbar involvement at admission.',
    'The original score ranges from 0 to 7. Shorter onset-to-admission interval, facial/bulbar weakness and a lower MRC sum score increase the score.',
    'MRC sum assesses six bilateral muscle groups, with a maximum of 60. The score is not simply the power of one selected muscle.'),
  S('Use Alongside Bedside Monitoring', '**Prediction supports triage but does not replace serial respiratory examination.** A lower predicted risk cannot overrule a falling VC, poor secretion handling or new bulbar failure.',
    'Updated/internationally evaluated versions exist, so specify the model when quoting an exact probability. Calibration can differ across populations and settings.',
    'Distinguish EGRIS from mEGOS, which addresses functional outcome. Neither tool should be used to withhold indicated immunotherapy or to make an unsupported guarantee of recovery or ventilator independence.')], ['GBS','GBS10'], style='direct')

add('Guillain-Barre syndrome', 'Severe GBS Dysautonomia',
 'A patient with GBS develops marked BP swings and episodes of profound bradycardia during suctioning. Which approach is most appropriate?',
 'Continuous monitored care with readiness to treat arrhythmia and cautious use of short-acting interventions', [
 ('Use a long-acting antihypertensive aggressively for every transient high reading', 'Transient hypertension may alternate with hypotension; long-lasting BP lowering can create prolonged harm if the autonomic state changes.'),
 ('Treat each bradycardic event as evidence that GBS cannot be the diagnosis', 'Severe bradyarrhythmia is a recognized GBS autonomic complication and should trigger safety escalation rather than diagnostic exclusion.'),
 ('Focus only on limb strength because autonomic events do not affect short-term risk', 'Arrhythmias and hemodynamic instability can be life threatening even when limb weakness is not changing.')],
 [S('Autonomic Instability', '**GBS can cause tachy/bradyarrhythmias, labile BP, ileus, urinary retention and sweating abnormalities.** Severe events can be provoked by procedures or airway stimulation.',
    'Continuous ECG and appropriate BP monitoring are important in unstable patients. Review hypoxia, infection, drugs and electrolyte abnormalities as co-contributors.',
    'Prepare appropriate emergency treatment for significant bradycardia; selected severe recurrent cases require specialist pacing consideration.'),
  S('Avoid Overshoot', '**Treat sustained clinically important abnormalities cautiously**, often favoring short-acting titratable agents in an unstable autonomic setting rather than a fixed response to every transient reading.',
    'Maintain appropriate volume status and monitor sodium, bowel/bladder function and temperature. Hyponatremia can reflect SIADH or other mechanisms and needs contextual assessment.',
    'Provide thrombosis prevention, pressure care, analgesia, nutrition and rehabilitation alongside disease-directed treatment. A favorable motor examination does not eliminate autonomic or respiratory risk.')], ['GBS','GBS10'])

add('Guillain-Barre syndrome', 'Choosing Initial GBS Immunotherapy',
 'An adult with GBS cannot walk unaided seven days after weakness onset. There is no major contraindication to either treatment. Which statement best fits EAN/PNS 2023 guidance?',
 'IVIG 0.4 g/kg/day for five days or an appropriate plasma-exchange course are established options', [
 ('Oral prednisone is preferred because all inflammatory neuropathies respond similarly', 'GBS differs from CIDP: corticosteroids do not provide the established benefit of IVIG or plasma exchange and are not preferred GBS treatment.'),
 ('Treatment should wait until two weeks have elapsed from onset', 'The early window is an opportunity for treatment, not a mandatory waiting period; a nonambulant patient at day seven fits the evidence-supported timing.'),
 ('The electrophysiological subtype must be finalized before treatment starts', 'Early subtype classification can change and is not required before treating a convincing disabling clinical GBS syndrome.')],
 [S('Evidence-Supported Options', '**Standard IVIG totals 2 g/kg**, commonly 0.4 g/kg/day for five days. EAN/PNS recommends it within two weeks in patients unable to walk unaided, with good-practice consideration extending to two to four weeks.',
    'Plasma exchange is recommended within four weeks in nonambulant patients, commonly four to five exchanges totaling approximately 12–15 L over one to two weeks in the guideline framework.',
    'Treatment may also be appropriate in an ambulant patient with rapid progression or important bulbar, respiratory or autonomic disease; walking ability is not the only severity measure.'),
  S('Selection and Safety', '**Choose according to contraindications, stability, access and patient factors.** IVIG requires attention to renal, thrombotic, hemolytic and volume risks; exchange requires vascular-access and hemodynamic assessment.',
    'Neither is uniformly superior in every patient. Routine immediate sequential therapy is not recommended, and plasma exchange after IVIG can remove administered immunoglobulin.',
    'Continue serial respiratory/autonomic monitoring, DVT prevention, analgesia and rehabilitation. Immunotherapy is intended to limit immune injury but does not guarantee immediate reversal of weakness.')], ['GBS','GBS10'])

add('Guillain-Barre syndrome', 'Why CIDP Treatment Cannot Simply Be Copied to GBS',
 'Which treatment statement is correct for typical GBS under EAN/PNS 2023 guidance?',
 'Corticosteroids are not recommended as routine disease-modifying GBS treatment', [
 ('Oral steroids have the same established benefit in GBS as in typical CIDP', 'Typical CIDP can respond to corticosteroids, but GBS trials/guidance do not support transferring that treatment effect to the acute syndrome.'),
 ('Plasma exchange followed immediately by IVIG is routinely superior to either alone', 'Routine immediate sequential treatment has not shown the required added benefit and is not recommended as a default strategy.'),
 ('A prolonged steroid taper is required after every standard IVIG course', 'There is no routine GBS steroid-taper requirement after IVIG; such a schedule confuses GBS with other immune neurological conditions.')],
 [S('Disease-Specific Evidence', '**GBS and CIDP share immune peripheral-nerve injury but have different treatment evidence.** EAN/PNS recommends against oral corticosteroids and weakly against IV corticosteroids for GBS.',
    'IVIG or plasma exchange are the established acute disease-directed options when indicated. A label such as inflammatory neuropathy is insufficient to choose treatment.',
    'Routine PE immediately followed by IVIG is not recommended; this should not be confused with individualized reassessment of a later genuine fluctuation or diagnostic change.'),
  S('Follow the Course', '**Continuing weakness soon after treatment does not automatically prove failure.** Nerve injury and recovery kinetics can produce delayed improvement despite an appropriate initial course.',
    'Reassess clinical trajectory, respiratory/autonomic support, complications and competing diagnoses. Progression beyond eight weeks or repeated fluctuations can shift the diagnosis toward acute-onset CIDP.',
    'If the diagnosis changes, longer-term strategies may become appropriate. Document the reasoning rather than adding steroids or repeated IVIG solely because the first response was not immediate.')], ['GBS','CIDP'], style='direct')

add('Guillain-Barre syndrome', 'Poor Prognosis Alone Is Not an Indication for Repeat IVIG',
 'After a standard IVIG course, a patient with severe GBS remains weak and has a poor prognostic score, without a clear improvement-then-deterioration fluctuation. Which strategy is best supported?',
 'Continue intensive supportive care and reassessment rather than routinely giving a second IVIG course solely for the poor prognosis', [
 ('Give a second full course automatically because the prognostic score is high', 'SID-GBS did not show benefit from a routine early second course for poor prognosis and found more serious adverse events.'),
 ('Add oral steroids as the evidence-based rescue for every slow recovery', 'Corticosteroids are not an established GBS rescue simply because recovery is slow; reassess the course and differential instead.'),
 ('Stop respiratory monitoring because immunotherapy has already been completed', 'The need for respiratory and autonomic support persists independently of completion of the five-day treatment course.')],
 [S('SID-GBS Trial', '**The randomized SID-GBS study** tested an early second IVIG course in patients predicted to have a poor outcome. It did not establish clinical benefit and showed an increased serious-adverse-event burden.',
    'EAN/PNS 2023 therefore recommends against a second course based solely on poor prognosis. A high mEGOS is not itself proof of persistent treatable immune activity.',
    'Clinical deterioration can reflect ongoing acute disease, secondary complications, an alternative diagnosis or a true treatment-related fluctuation; these situations must be distinguished.'),
  S('A Different Question: Genuine Fluctuation', '**Improvement/stabilization followed by renewed objective deterioration** may constitute a TRF and can justify individualized retreatment consideration under specialist guidance.',
    'This differs from never improving or simply having a severe baseline deficit. The randomized poor-prognosis result should not be misrepresented as proof that every later immune relapse must go untreated.',
    'Maintain respiratory care, infection/thrombosis prevention, nutrition, rehabilitation and patient communication. Prognostic models inform expectations but do not replace serial clinical decisions.')], ['SID','GBS'])

add('Guillain-Barre syndrome', 'Treatment-Related Fluctuation Versus Acute-Onset CIDP',
 'A patient initially diagnosed with GBS improves after treatment but has further objective deterioration ten weeks after weakness onset. Which diagnostic reassessment is most important?',
 'Consider acute-onset CIDP', [
 ('Classify every deterioration as ordinary monophasic GBS without further review', 'A later deterioration beyond eight weeks is a recognized reason to reconsider the acute monophasic label.'),
 ('Exclude CIDP because the first presentation evolved rapidly', 'A minority of CIDP patients present acutely and initially resemble GBS; later course can reveal the chronic disorder.'),
 ('Diagnose MMN solely from any relapse after IVIG', 'MMN requires an appropriate multifocal motor phenotype and electrophysiological context; relapse timing alone does not establish it.')],
 [S('Longitudinal Diagnostic Boundary', '**Further worsening after eight weeks from onset or at least three TRFs** strongly raises acute-onset CIDP in a patient initially labeled as GBS.',
    'A TRF is renewed deterioration after treatment-associated improvement or stabilization, not simply a slow or incomplete recovery. Document objective strength, disability and timing.',
    'The early presentation can be indistinguishable, so a provisional acute diagnosis requires follow-up rather than permanent diagnostic closure.'),
  S('Treatment Consequences', '**Acute-onset CIDP may require maintenance therapy**, unlike a straightforward monophasic GBS course. Reassess clinical distribution, electrodiagnostics and supportive tests while excluding mimics.',
    'Appropriate retreatment of an early genuine GBS fluctuation is a separate decision from routine second IVIG for poor prognosis alone.',
    'Review infection, critical illness, drug effects and mechanical complications that can also worsen strength. Treatment should follow the best-supported current diagnosis and documented response, not the name attached during the first admission.')], ['GBS','CIDP'])

R.update({
 'CIDPFULL': ('EAN/PNS CIDP guideline full text, 2021', 'https://pure.amsterdamumc.nl/ws/files/157471785/European-academy-of-neurologyperipheral-nerve-society-guideline-on-diagnosis-and-treatment-of-chronic-inflammatory-demy.pdf'),
 'EFG': ('Efgartigimod alfa/hyaluronidase US label, 2026', 'https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/761304s019lbl.pdf'),
 'ADHERE': ('ADHERE randomized-withdrawal CIDP trial, 2024', 'https://pubmed.ncbi.nlm.nih.gov/39304241/'),
 'MMN': ('EFNS/PNS multifocal motor neuropathy guideline, first revision, 2010', 'https://pubmed.ncbi.nlm.nih.gov/21199100/'),
})

add('CIDP, nodopathies and motor neuropathy', 'Typical CIDP: Distribution and Duration',
 'An adult has four months of progressive symmetric proximal and distal weakness, sensory loss in multiple limbs and generalized reduced reflexes. Which syndrome is most strongly suggested?',
 'Typical CIDP', [
 ('A typical length-dependent axonal DSP as the complete explanation', 'DSP commonly emphasizes distal sensory symptoms; substantial proximal and distal motor involvement over months raises an acquired inflammatory demyelinating syndrome.'),
 ('A monophasic GBS course without diagnostic reconsideration', 'Continued progression beyond eight weeks is a reason to reconsider GBS and assess CIDP, even if early disease appeared acute.'),
 ('MMN with pure motor disease', 'MMN usually causes asymmetric weakness in named motor-nerve territories with sensory sparing; generalized symmetric sensorimotor involvement is more compatible with typical CIDP.')],
 [S('Clinical Framework', '**Typical CIDP** usually has progressive or relapsing symmetric proximal and distal weakness, sensory involvement in at least two limbs and reduced/absent reflexes, evolving over at least eight weeks.',
    'A clinically compatible pattern must be supported by appropriate nerve conduction evidence and exclusion of mimics. The time course alone does not establish immune demyelination.',
    'Variants can be distal, multifocal/focal, motor or sensory predominant, but require their own clinical and electrophysiological framework.'),
  S('Confirm Before Committing to Long-Term Therapy', '**Diabetes, inherited neuropathy, paraproteinemia, amyloid, POEMS and structural disease** can resemble parts of the presentation and deserve phenotype-guided assessment.',
    'The 2021 guideline uses CIDP and possible-CIDP certainty categories rather than simply carrying forward all older labels. Supportive tests are interpreted within the specified pathway.',
    'Document objective baseline impairment and disability before treatment. A sustained measurable response supports management decisions but should not be used to bypass valid diagnostic evidence.')], ['CIDP','CIDPFULL'])

add('CIDP, nodopathies and motor neuropathy', 'Key EAN/PNS 2021 Demyelinating Thresholds',
 'Which non-entrapment motor conduction finding meets a key quantitative demyelinating threshold in the 2021 EAN/PNS CIDP framework when present in the required number of nerves?',
 'Motor conduction velocity at least 30% below the lower limit of normal', [
 ('Velocity 10% below the lower limit in one low-amplitude nerve', 'Mild slowing in a severely reduced response can reflect axonal loss or technical effects and does not meet the stated multi-nerve quantitative threshold.'),
 ('Median distal latency prolongation only across a carpal-tunnel segment', 'Entrapment-related slowing must not be counted uncritically as generalized CIDP demyelination; median-wrist abnormalities require the guideline’s exclusion rules.'),
 ('Reduced sensory amplitude alone with otherwise normal motor timing', 'Sensory abnormalities contribute to classification, but isolated low SNAP amplitude is not the specified motor demyelination criterion.')],
 [S('Quantitative Evidence', '**Motor conduction velocity at least 30% below LLN in at least two nerves**, or motor distal latency at least 50% above ULN in at least two eligible nerves, provides important demyelinating evidence under the 2021 framework.',
    'F-wave prolongation thresholds depend on distal CMAP amplitude: at least 20% above ULN in the usual amplitude context, with a larger 50% threshold when distal CMAP is below 80% of LLN.',
    'Apply the full criterion set and technical qualifications rather than diagnosing CIDP from a single summary number.'),
  S('Block, Dispersion and Sensory Studies', '**Conduction block uses at least 30% proximal-to-distal negative-peak CMAP amplitude reduction** with required distal amplitude and nerve-count/other-feature qualifications; tibial block is excluded from this criterion.',
    'Abnormal temporal dispersion has duration-based rules, including a higher tibial threshold. Phase cancellation, low responses, temperature and anatomical variants can confound interpretation.',
    'Typical CIDP also requires sensory conduction abnormalities in the appropriate number of nerves. Clinical compatibility, distribution, supportive data and exclusion of alternative disease remain necessary.')], ['CIDP','CIDPFULL'], style='direct', table=(['Selected 2021 motor feature','Threshold and important context'],[
 ['Distal motor latency','≥50% above ULN in ≥2 eligible nerves; exclude median-wrist entrapment'],['Motor velocity','≥30% below LLN in ≥2 nerves'],['F-wave latency','≥20% above ULN; ≥50% if distal CMAP <80% LLN; required nerve context'],['Motor block','≥30% amplitude reduction; distal CMAP ≥20% LLN; exclude tibial; additional nerve/feature rules apply']]))

add('CIDP, nodopathies and motor neuropathy', 'CSF Protein Does Not Diagnose CIDP',
 'An older adult with a distal axonal diabetic neuropathy has mildly elevated CSF protein and no convincing motor demyelinating criteria. Which interpretation is best?',
 'The protein result alone is insufficient to establish CIDP', [
 ('Any protein above the laboratory range proves inflammatory demyelination', 'Protein can rise with age, diabetes, spinal disease and other processes; it is supportive only within an appropriate diagnostic framework.'),
 ('Subjective fatigue improvement after IVIG would establish CIDP despite discordant objective findings', 'Nonspecific perceived improvement can occur for several reasons. Objective impairment/disability measures and diagnostic concordance are needed.'),
 ('A normal nerve biopsy is mandatory before excluding CIDP', 'Nerve biopsy is not routinely required in typical evaluation and has sensitivity, specificity and morbidity limitations; a normal biopsy would not resolve all cases.')],
 [S('Supportive, Not Stand-Alone', '**CSF protein elevation** can support a clinically/electrophysiologically compatible CIDP diagnosis, particularly in an uncertain pathway, but is nonspecific.',
    'Use age-appropriate interpretation and assess cell count and alternative causes. A modest isolated elevation should not outweigh a discordant phenotype or technically inadequate nerve study.',
    'Marked pleocytosis, systemic red flags or unusual pain/weight loss should prompt a different or expanded evaluation.'),
  S('Objective Treatment Assessment', '**Measure strength and disability before and after therapy**, using suitable tools such as grip strength, MRC sum, INCAT or I-RODS according to the clinical question.',
    'An improvement should be clinically meaningful and reproducible. Reduced pain or fatigue alone does not establish reversal of immune demyelination.',
    'Reconsider diagnosis when repeated adequate first-line treatments fail. Continuing costly or risky immunotherapy on an unsupported label can delay treatment of amyloid, hereditary, paraproteinemic or other neuropathy.')], ['CIDP','CIDPFULL'])

add('CIDP, nodopathies and motor neuropathy', 'Multifocal CIDP Versus MMN',
 'A patient has chronic asymmetric upper-limb weakness, patchy sensory loss and demyelinating abnormalities in multiple named nerves. Which CIDP variant is particularly suggested?',
 'Multifocal CIDP, historically called MADSAM or Lewis–Sumner syndrome', [
 ('MMN as a pure motor syndrome', 'MMN typically lacks objective sensory loss in the affected nerve distributions; sensory involvement supports multifocal CIDP or another sensorimotor disorder.'),
 ('A single ulnar entrapment as the complete diagnosis', 'One entrapment does not explain multiple noncontiguous sensorimotor territories and generalized acquired demyelinating evidence.'),
 ('A typical uniformly symmetric hereditary demyelinating neuropathy', 'Hereditary disease remains a consideration, especially with pressure palsies or a pedigree, but patchy acquired sensorimotor involvement suggests multifocal CIDP in this setting.')],
 [S('Variant Recognition', '**Multifocal CIDP** produces asymmetric sensory and motor deficits, often initially upper-limb predominant. Historical labels include MADSAM and Lewis–Sumner syndrome.',
    'Distal CIDP emphasizes distal weakness/sensory disease; motor and sensory variants have distinct clinical and sensory-study requirements. Do not assume every variant meets the typical symmetric pattern.',
    'Use the 2021 variant-specific electrodiagnostic and supportive criteria rather than assigning a variant from distribution alone.'),
  S('Differential and Treatment', '**MMN, HNPP, vasculitis, plexopathy and paraproteinemic neuropathy** can cause asymmetric or multifocal deficits. Pain, axonal loss, pressure-site history and monoclonal findings can redirect the evaluation.',
    'IVIG or corticosteroids can be appropriate for many CIDP forms, while motor CIDP favors IVIG because steroid worsening can occur. That distinction also matters when MMN is a competing diagnosis.',
    'Document objective sensory and motor findings and track function with treatment. A sensory complaint without objective confirmation should not automatically convert a pure motor syndrome into multifocal CIDP.')], ['CIDP','CIDPFULL','MMN'])

add('CIDP, nodopathies and motor neuropathy', 'Initial Treatment of Typical CIDP',
 'An adult with well-supported typical CIDP has disabling weakness. Which statement best reflects the 2021 EAN/PNS initial-treatment guidance?',
 'IVIG or corticosteroids are recommended first-line options, selected according to phenotype and patient factors', [
 ('Oral steroids are ineffective because they do not treat GBS', 'GBS and CIDP have different treatment evidence; lack of steroid benefit in GBS does not negate their role in typical CIDP.'),
 ('Maintenance subcutaneous immunoglobulin is the routine emergency induction replacement for IVIG', 'SCIG is an established maintenance strategy in appropriate stabilized patients, but is not generally used as the standard rapid induction approach.'),
 ('Plasma exchange is excluded from CIDP therapy', 'Plasma exchange is effective and recommended particularly when IVIG/corticosteroids are ineffective or unsuitable; it is not categorically excluded.')],
 [S('Induction Options', '**IVIG induction commonly totals 2 g/kg over two to five days.** A lack of immediate response after one dose does not necessarily end an adequate trial, but further treatment requires a defined objective assessment plan.',
    'Corticosteroids may be oral or pulsed according to the regimen; no single schedule is established as best. Review diabetes, osteoporosis, infection risk, psychiatric effects and the need for rapid benefit.',
    'IVIG is preferred initially in motor CIDP under the good-practice recommendation, because corticosteroids can worsen selected motor presentations.'),
  S('Response and Escalation', '**Plasma exchange is effective**, especially when first options fail or are unsuitable, but access, hemodynamics and feasibility of maintenance influence use.',
    'Record baseline strength, disability and treatment goals and assess a meaningful objective response. Recheck diagnosis and technical criteria when benefit is absent or inconsistent.',
    'Modern therapies approved after the 2021 guideline expand choices in specified settings, but approval alone does not make every drug interchangeable for induction, maintenance or every CIDP mimic. Discuss evidence, safety and local access.')], ['CIDP','CIDPFULL'])

add('CIDP, nodopathies and motor neuropathy', 'Individualizing Immunoglobulin Maintenance',
 'A patient with IVIG-responsive CIDP has stable strength and function for many months. Which long-term strategy is most appropriate?',
 'Find the lowest effective dose/interval and periodically reassess treatment dependence using objective measures', [
 ('Maintain the induction dose forever without testing whether disease remains active', 'Some patients enter remission or need less treatment; indefinite unchanged high exposure can add cost and adverse effects without demonstrated need.'),
 ('Stop all therapy abruptly without a relapse plan because the patient currently looks well', 'Stability may reflect treatment dependence. A planned reduction with follow-up is safer and more informative than an unmonitored abrupt stop.'),
 ('Judge every dose change only by transient nonspecific fatigue', 'Fatigue matters, but should be interpreted alongside measurable strength/disability rather than being the sole marker of immune relapse.')],
 [S('Dose and Interval', '**A common trial maintenance regimen is IVIG 1 g/kg every three weeks**, but clinical dosing is individualized; lower doses or longer intervals may preserve benefit.',
    'End-of-dose deterioration can justify a different interval or distribution. Document it objectively rather than assuming all daily symptom variation represents inflammatory activity.',
    'Review renal, thrombotic, hemolytic and infusion-related risks and the patient’s administration burden.'),
  S('SCIG and Dependency Review', '**SCIG is a maintenance option** for appropriately stabilized immunoglobulin-responsive CIDP. Product-specific regimens commonly use weekly doses such as 0.2–0.4 g/kg, with individualized adjustment.',
    'SCIG can provide steadier exposure and home administration but causes local reactions and requires training and a feasible support plan.',
    'Periodically reduce the dose, lengthen the interval or trial withdrawal when clinically appropriate, using an agreed objective relapse threshold and rescue plan. This distinguishes ongoing active disease from fixed residual axonal disability.')], ['CIDP','CIDPFULL'])

add('CIDP, nodopathies and motor neuropathy', 'FcRn Blockade and the ADHERE Population',
 'Which statement about efgartigimod in adult CIDP is most accurate?',
 'It blocks FcRn-mediated IgG recycling, and ADHERE demonstrated reduced relapse risk in an enriched randomized-withdrawal responder population', [
 ('It permanently depletes CD20-positive B cells as its principal mechanism', 'CD20 depletion describes agents such as rituximab; efgartigimod acts on the neonatal Fc receptor to lower circulating IgG.'),
 ('ADHERE proved superiority over IVIG in a direct head-to-head randomized trial', 'ADHERE randomized initial responders to continued drug or placebo withdrawal; it was not a direct randomized comparison against IVIG.'),
 ('Approval for CIDP establishes efficacy for every axonal or diabetic neuropathy', 'The indication and trial population concern CIDP, not all neuropathy phenotypes; misdiagnosis is not corrected by choosing a newer immune drug.')],
 [S('Mechanism and Evidence', '**FcRn blockade reduces IgG recycling**, lowering circulating IgG including pathogenic antibodies. Subcutaneous efgartigimod/hyaluronidase has a US adult CIDP indication.',
    'ADHERE first assessed response in an open-label stage and then randomized responders. Continued treatment reduced relapse risk versus placebo, with hazard ratio about 0.394 in the withdrawal phase.',
    'The responder-enriched design supports maintenance of response in that population; it does not establish universal response or superiority to all existing treatments.'),
  S('Formulation and Safety', '**The 2026 US prefilled-syringe CIDP regimen is 1000 mg efgartigimod/10,000 units hyaluronidase subcutaneously weekly.** The vial presentation has a different stated amount, so use the applicable product instructions.',
    'Assess infection and vaccination needs, hypersensitivity and injection-site reactions. Live vaccines are generally not recommended during treatment because of transient IgG reduction and uncertain response.',
    'Do not copy a four-week cyclic generalized-MG regimen into continuous weekly CIDP dosing. Treatment response and infection risk require monitoring, and availability/approval outside the US must be verified locally.')], ['EFG','ADHERE'], style='direct')

add('CIDP, nodopathies and motor neuropathy', 'Autoimmune Nodopathy Is Not Conventional CIDP',
 'A younger patient has severe distal weakness, sensory ataxia and tremor, poor IVIG response and confirmed IgG4 neurofascin-155 antibodies. Which interpretation is most appropriate?',
 'An autoimmune nodopathy requiring disease-specific reassessment rather than automatic conventional-CIDP escalation', [
 ('Typical CIDP is proved by any positive nerve-related antibody', 'The 2021 framework distinguishes nodal/paranodal antibody-associated disease from conventional CIDP because biology, pathology and treatment response can differ.'),
 ('The antibody result guarantees a response to repeated IVIG', 'IgG4 nodopathies can respond poorly to IVIG; a confirmed result can explain the atypical response rather than justify indefinite repetition.'),
 ('A hereditary tremor–ataxia syndrome is established without reviewing immune evidence', 'Inherited disease can mimic features, but a validated phenotype-concordant nodal antibody has specific significance and should prompt targeted immune evaluation.')],
 [S('Nodal/Paranodal Targets', '**NF155, contactin-1 and CASPR1 antibodies** identify important autoimmune nodopathy contexts. Presentations may include marked tremor/ataxia, distal involvement, severe acute disease or other atypical features.',
    'The immunoglobulin subclass and assay validity matter. Confirm an unexpected result in an experienced laboratory rather than interpreting every weak commercial signal as etiologic proof.',
    'These disorders are distinguished from conventional CIDP in the 2021 guideline rather than treated as an interchangeable diagnostic subgroup.'),
  S('Treatment Implications', '**Poor IVIG response is recognized in selected IgG4 disease.** Rituximab or other antibody-directed strategies may be considered by specialists, but evidence is largely observational and does not justify a universal response guarantee.',
    'Review infection, hepatitis B, immunoglobulins and vaccination before B-cell-directed therapy, and monitor objective neurological function.',
    'Reassess disease classification when the phenotype and response are atypical. A nodopathy label does not remove the need to exclude paraproteinemia, hereditary disease or another cause and to verify the antibody result.')], ['CIDP','CIDPFULL'])

add('CIDP, nodopathies and motor neuropathy', 'Multifocal Motor Neuropathy',
 'An adult has slowly progressive asymmetric distal arm weakness in several named nerve territories. Sensation is preserved, there are no definite upper motor neuron signs, and conduction block is demonstrated outside entrapment sites. Which diagnosis best fits?',
 'Multifocal motor neuropathy', [
 ('ALS as established despite the focal motor conduction block', 'ALS is an important motor-only differential, but true non-entrapment conduction block supports a potentially treatable motor neuropathy; assess UMN signs and broader denervation carefully.'),
 ('Multifocal CIDP with documented sensory disease', 'Multifocal CIDP includes sensory involvement, whereas the preserved sensory examination/studies and pure motor pattern favor MMN.'),
 ('A single cervical root lesion as the complete explanation', 'A root lesion does not account for the pattern of multiple named nerve territories with motor block away from entrapment sites; the distribution and electrodiagnostics require broader consideration.')],
 [S('Pure Motor Immune Neuropathy', '**MMN usually causes chronic asymmetric weakness**, often upper-limb and distal predominant, with little or no objective sensory loss in affected territories.',
    'Motor conduction block outside common compression sites is important evidence. Absence of a demonstrable block on a limited study does not resolve every suspected case; examine accessible segments and technical quality.',
    'Anti-GM1 IgM can support the diagnosis but is neither universally present nor sufficient alone. Marked bulbar disease or definite UMN signs should prompt reassessment.'),
  S('Treatable Mimic of Motor Neuron Disease', '**Distinguish MMN from ALS, motor CIDP, root/plexus disease and hereditary motor neuropathy.** Sensory studies and careful motor distribution are particularly useful.',
    'IVIG is the established first-line treatment when disability warrants it. Early recognition can preserve function before substantial irreversible axonal loss.',
    'Corticosteroids and plasma exchange cannot simply be transferred from CIDP therapy and can be ineffective or worsen MMN. Follow strength and practical hand function rather than antibody titres alone.')], ['MMN'])

add('CIDP, nodopathies and motor neuropathy', 'Treating Functionally Significant MMN',
 'A patient with well-supported MMN has disabling hand weakness. Which initial disease-directed treatment is preferred?',
 'IVIG, commonly totaling 2 g/kg over two to five days', [
 ('Oral corticosteroids as the default first-line treatment', 'Steroids are effective in many CIDP contexts but are not standard MMN therapy and can worsen weakness in selected patients.'),
 ('Plasma exchange as the routine preferred induction therapy', 'Exchange is effective in CIDP/GBS but is not an established preferred MMN treatment and can be associated with worsening.'),
 ('Riluzole as treatment of the presumed motor-neuron disease mechanism', 'Riluzole has an ALS role; the supported conduction-block motor neuropathy has a different treatable immune mechanism and should not be managed as ALS by default.')],
 [S('Immunoglobulin Response', '**IVIG is first-line MMN therapy**, with a common induction total of 2 g/kg over two to five days. Use a patient-specific plan that accounts for renal, thrombotic, volume and hemolytic risks.',
    'A meaningful objective improvement in strength/function supports continuing treatment. A fixed denervated muscle may not recover fully even when immune activity is controlled.',
    'Lack of response requires review of diagnosis, exposure and the degree of irreversible axonal damage rather than automatic indefinite high-dose treatment.'),
  S('Maintenance and Monitoring', '**Many responders need maintenance IVIG**, individualized by recurrence and function. Guideline examples include 1 g/kg every two to four weeks or 2 g/kg every one to two months, rather than one mandatory schedule.',
    'Selected patients may use SCIG maintenance under appropriate specialist/product arrangements. Monitor clinical dependence and adverse effects.',
    'Do not use an anti-GM1 titre as the sole dosing target. Rehabilitation, splinting and practical hand support complement immune treatment, while steroid/PE regimens borrowed from other inflammatory neuropathies can be inappropriate.')], ['MMN'])

R.update({
 'ADA26': ('ADA Standards of Care: neuropathy and foot care, 2026', 'https://doi.org/10.2337/dc26-S012'),
 'DLR': ('Cochrane review: Immunotherapy for diabetic amyotrophy, 2017', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6483238/'),
 'B12': ('NICE NG239: B12 deficiency diagnosis and treatment, 2024', 'https://www.nice.org.uk/guidance/ng239/chapter/Recommendations'),
 'B6': ('Medsafe vitamin B6 and peripheral neuropathy safety update, 2025', 'https://www.medsafe.govt.nz/profs/PUArticles/June2025/Vitamin-B6-and-peripheral-neuropathy.html'),
 'DULO': ('Duloxetine prescribing information', 'https://www.dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=b6040e79-0bbd-41a3-ba86-2a360a41864c'),
 'PREG': ('Pregabalin prescribing information', 'https://www.dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=ebe34db4-816d-4f0a-adbb-826693662754'),
 'CIPN': ('ASCO chemotherapy-induced neuropathy guideline update, 2020', 'https://doi.org/10.1200/JCO.20.01399'),
})

add('Common acquired and toxic neuropathies', 'Diabetes Does Not Explain Every Neuropathy',
 'A patient with diabetes develops rapidly progressive proximal and distal weakness over three months, with substantial non-entrapment demyelinating abnormalities. Which approach is best?',
 'Investigate a superimposed disorder such as CIDP rather than attributing all findings to routine diabetic DSP', [
 ('Diagnose ordinary diabetic DSP from diabetes alone', 'Typical diabetic DSP is usually length-dependent and sensory predominant; rapid marked proximal motor dysfunction and strong demyelinating evidence deserve another evaluation.'),
 ('Diagnose CIDP solely because diabetes and weakness coexist', 'CIDP remains a possibility, but diabetes can complicate electrophysiology and CSF interpretation; the full clinical/technical criteria and mimics still require review.'),
 ('Treat only neuropathic pain and defer assessment of the motor progression', 'Pain treatment can help symptoms but does not address potentially treatable progressive weakness or establish its cause.')],
 [S('Typical Diabetic Pattern', '**Diabetic distal symmetric polyneuropathy** commonly begins with distal sensory symptoms and signs, followed later by motor impairment. Assess pain/temperature and vibration/reflexes, together with protective sensation and foot risk.',
    'Rapid progression, marked asymmetry, proximal weakness or substantial motor-predominant disease are reasons for neuromuscular assessment rather than automatic attribution to diabetes.',
    'A diabetic patient can have B12 deficiency, entrapment, CIDP, amyloid or another neuropathy at the same time.'),
  S('Prevention and Interpretation', '**Optimize individualized glycemic and vascular risk management**, provide foot surveillance and address smoking, footwear and ulcer prevention. Benefit from glycemic control is strongest for prevention in type 1 diabetes and more modest for slowing type 2 disease.',
    'Review metformin-associated B12 deficiency when appropriate. A mildly elevated protein or modest slowing alone should not lead to CIDP overdiagnosis.',
    'Treatment should follow the best-supported phenotype and etiology. Correcting diabetes control does not promise reversal of established axonal loss, while a second treatable process should not be missed.')], ['ADA26','CIDP'])

add('Common acquired and toxic neuropathies', 'Diabetic Lumbosacral Radiculoplexus Neuropathy',
 'An adult with type 2 diabetes develops severe unilateral thigh/hip pain, weight loss and subsequent patchy proximal weakness and atrophy. EMG involves several roots and peripheral nerves. Imaging excludes a compressive mass. Which diagnosis best fits?',
 'Diabetic lumbosacral radiculoplexus neuropathy', [
 ('A single femoral mononeuropathy', 'Femoral disease can cause knee-extension weakness and sensory change, but the multi-root/multi-nerve distribution and painful proximal syndrome extend beyond a single nerve.'),
 ('Typical painless length-dependent diabetic DSP', 'DSP usually begins distally and symmetrically; severe asymmetric proximal pain followed by patchy weakness is a different diabetic neuropathy pattern.'),
 ('Typical CIDP as established from diabetes and proximal weakness alone', 'CIDP often has a more symmetric acquired demyelinating pattern; painful asymmetric radiculoplexus axonal disease requires a different evaluation and evidence framework.')],
 [S('Pain Followed by Weakness', '**Diabetic radiculoplexus neuropathy**, often called diabetic amyotrophy, can begin with focal severe pain and evolve into weakness across several nerve/root territories, sometimes spreading to the other side.',
    'Weight loss is common. The presentation may occur despite relatively acceptable current glycemic control and is not simply the severe end of routine DSP.',
    'Exclude neoplastic/infiltrative plexopathy, structural root disease, hematoma and systemic vasculitis when the history or examination suggests them.'),
  S('Recovery and Treatment Evidence', '**Analgesia, rehabilitation, nutritional support and diabetes care** are central. Recovery can take months or longer and may remain incomplete.',
    'Microvasculitic ischemic injury has a biological role, but high-quality randomized evidence supporting a routine immunotherapy regimen is insufficient. The Cochrane review did not establish a positive or negative treatment effect from available randomized data.',
    'Selected severe cases may receive specialist-directed immune treatment, but it should not be presented as universally proven. Define the goals and uncertainty and monitor objective strength, pain and function.')], ['DLR','ADA26'])

add('Common acquired and toxic neuropathies', 'Pain Treatment with Coexisting Depression',
 'An adult with painful diabetic neuropathy and major depression has normal renal and hepatic function. A single medicine addressing both conditions is preferred. Which option best fits that goal?',
 'Duloxetine', [
 ('Pregabalin', 'Pregabalin can reduce neuropathic pain and help sleep, but is not an antidepressant treatment for major depression; edema, weight gain and sedation may also matter.'),
 ('Gabapentin', 'Gabapentin can help neuropathic pain, with renal adjustment and sedation monitoring, but does not provide established major-depression treatment.'),
 ('Topical capsaicin', 'Capsaicin can help selected localized neuropathic pain with limited systemic exposure, but does not treat the coexisting depressive illness.')],
 [S('Choose by Comorbidity', '**SNRIs, gabapentinoids, TCAs and selected sodium-channel blockers** have guideline-supported roles in painful diabetic neuropathy. Similar average efficacy means comorbidity and adverse effects often determine the best initial choice.',
    'Duloxetine can address pain and depression. A lower lead-in such as 30 mg daily may improve tolerability, with 60 mg once daily a usual diabetic-pain target.',
    'Review nausea, BP, serotonergic interactions, withdrawal and hepatic risk. Avoid or use an alternative in the label-specified severe renal/hepatic settings rather than applying this normal-organ-function example indiscriminately.'),
  S('Alternatives and Follow-up', '**Pregabalin and gabapentin require renal dose adjustment** and can cause sedation, edema and falls. A common pregabalin initiation in adequate renal function is 150 mg/day divided, with product/indication-specific titration.',
    'TCAs may be limited by anticholinergic, orthostatic and cardiac effects. Topical options can suit focal symptoms or systemic-drug intolerance.',
    'Assess sleep, function and meaningful pain reduction rather than demanding complete analgesia. Switch class or consider a rational combination after an adequate tolerated trial; AAN advises against routine opioid treatment for PDN.')], ['PDN','DULO','PREG'])

add('Common acquired and toxic neuropathies', 'B12 Myeloneuropathy and Functional Markers',
 'A patient taking metformin has paresthesias, loss of position sense, absent ankle reflexes and extensor plantar responses. Serum B12 is indeterminate. Which test can clarify functional deficiency, interpreted with renal function?',
 'Methylmalonic acid', [
 ('Serum folate alone', 'Folate evaluates a related nutritional issue but does not specifically establish functional B12 deficiency and cannot explain away a compatible B12 neurological syndrome.'),
 ('Serum creatine kinase as the primary confirmation test', 'CK assesses muscle injury and does not directly test the B12-dependent metabolic pathway involved in this myeloneuropathic presentation.'),
 ('HbA1c as sufficient proof that all neurological findings are diabetic', 'Glycemic status matters, but posterior-column/pyramidal findings and an indeterminate B12 level require assessment of an additional treatable deficiency.')],
 [S('Combined Central and Peripheral Injury', '**B12 deficiency can cause neuropathy and subacute combined cord dysfunction**, producing mixed areflexic sensory and pyramidal findings. Neurological disease can occur without macrocytosis or anemia.',
    'Metformin, malabsorption, autoimmune gastritis, dietary deficiency and nitrous oxide exposure are relevant contexts. Nitrous oxide can inactivate B12 function even when a measured concentration is not frankly low.',
    'MMA supports functional deficiency when the initial B12 test is indeterminate, but renal impairment can independently elevate it.'),
  S('Treat Without Avoidable Delay', '**Do not delay replacement in a strongly suspected neurological syndrome** while waiting for all confirmation. Choose intramuscular or high-dose oral treatment according to cause, neurological severity, absorption and applicable guidance.',
    'NICE recommends at least 1 mg/day when oral replacement is used for malabsorption; severe neurological disease commonly warrants parenteral treatment and close response review.',
    'Investigate the cause and arrange ongoing therapy when required. Folate alone can improve hematological abnormalities while leaving B12-related neurological injury unaddressed, and recovery may be incomplete after prolonged deficiency.')], ['B12','ADA26'])

add('Common acquired and toxic neuropathies', 'Pyridoxine Excess',
 'A patient develops sensory ataxia and distal paresthesias while taking several over-the-counter multivitamin and magnesium preparations. Which supplement exposure should be specifically reviewed?',
 'Total vitamin B6 intake across all products', [
 ('Vitamin B12 as the typical dose-dependent sensory neurotoxin in ordinary supplementation', 'B12 deficiency is a neurological concern, but routine B12 replacement is not the classic supplement-related sensory-neuropathy mechanism described here.'),
 ('Thiamine as the common cause of a supplement-induced sensory neuronopathy', 'Thiamine deficiency can cause neurological injury; the recognized chronic supplement toxicity concern in this pattern is pyridoxine exposure.'),
 ('Folate as the direct explanation of all ataxia regardless of B6 exposure', 'Folate assessment may be relevant nutritionally, but does not replace review of B6-containing products and other sensory-neuropathy causes.')],
 [S('Hidden Cumulative Exposure', '**Vitamin B6 excess can cause sensory neuropathy or neuronopathy.** Products marketed for magnesium, zinc, stress or general nutrition may all contain B6, creating unrecognized cumulative intake.',
    'Ask for labels and actual daily doses rather than the product category alone. Pyridoxine, pyridoxal and pyridoxamine-related naming can obscure the same nutrient exposure.',
    'Regulatory safety reports include cases at lower doses or with multiple products; do not claim a single universally safe threshold for every individual and duration.'),
  S('Evaluation and Management', '**Stop unnecessary excess exposure and investigate competing causes.** A measured level can support exposure assessment but does not by itself prove every symptom is attributable to B6.',
    'Recovery can be slow and incomplete. Follow sensory function, gait safety and objective findings, and provide rehabilitation/support while monitoring the course.',
    'B6 deficiency also has clinical contexts, including selected drug-related needs, so treatment is not indiscriminate avoidance of the nutrient. Use indicated physiological supplementation rather than assuming all high-dose vitamins are harmless.')], ['B6','APPROACH'])

add('Common acquired and toxic neuropathies', 'Chemotherapy-Induced Sensory Neuropathy',
 'A patient receiving oxaliplatin develops distal sensory symptoms and cold-triggered dysesthesias that later persist between cycles. Which management principle is most appropriate?',
 'Assess functional toxicity with oncology and consider treatment modification rather than only adding analgesics', [
 ('Continue the same neurotoxic exposure regardless of functional deterioration', 'Cancer control matters, but intolerable neuropathy or functional impairment requires discussion of delay, dose reduction, substitution or stopping according to the oncological setting.'),
 ('Use routine prophylactic high-dose B6 as a proven prevention strategy', 'No such universal prevention benefit is established, and B6 excess can itself cause neuropathy.'),
 ('Diagnose CIDP solely because symptoms persist after an infusion', 'Persistence is compatible with toxic axonal/sensory injury; CIDP requires its own clinical/electrophysiological evidence.')],
 [S('Exposure and Pattern', '**Oxaliplatin can cause acute cold-triggered symptoms and cumulative sensory neuropathy.** Platinum agents, taxanes and vinca alkaloids have important but differing neurotoxicity patterns.',
    'Symptoms can continue or worsen after exposure ends in selected drug contexts, so the absence of a current infusion does not automatically exclude toxicity.',
    'Review diabetes, B12, alcohol, other neurotoxic drugs and baseline neuropathy, since combined contributors influence severity.'),
  S('Treatment Decisions', '**Discuss chemotherapy modification for intolerable symptoms or functional impairment** rather than masking progressive injury. Decisions depend on cancer benefit, alternatives and patient priorities.',
    'ASCO 2020 supports duloxetine for established painful CIPN, with limited average benefit; a common approach is 30 mg daily for one week then 60 mg daily if suitable.',
    'Rehabilitation, fall prevention and hand/foot safety are important. Antioxidants, vitamins or other drugs should not be presented as universally proven prevention, and analgesia does not reverse the toxic injury itself.')], ['CIPN'])

add('Common acquired and toxic neuropathies', 'Neuropathy in Advanced Kidney Disease',
 'An adult with advanced chronic kidney disease develops symmetric distal sensory loss, areflexia and later distal weakness with an axonal electrophysiological pattern. Which interpretation is most appropriate?',
 'Uremic neuropathy is plausible, while other common and treatable causes still require review', [
 ('Renal disease proves that no other neuropathy can coexist', 'Diabetes, B12 deficiency, drugs, entrapment and immune or paraprotein disease can coexist with kidney failure and may alter treatment.'),
 ('Any mild conduction slowing establishes CIDP in this setting', 'Axonal loss and other confounders can cause modest slowing; CIDP still requires a compatible pattern and validated criteria.'),
 ('A pure myopathy explains the sensory nerve abnormalities', 'Uremic myopathy can coexist, but a sensory axonal nerve-response pattern is not explained by muscle disease alone.')],
 [S('Length-Dependent Axonal Pattern', '**Uremic neuropathy** commonly causes a distal symmetric sensorimotor axonal syndrome, often with sensory symptoms and reduced reflexes before substantial weakness.',
    'Severity relates to the renal and metabolic context rather than one universal creatinine cutoff. Electrodiagnostics quantify the peripheral pattern and identify atypical features.',
    'Rapid progression, marked asymmetry or proximal weakness should trigger assessment of another process.'),
  S('Renal and Neurological Management', '**Optimize renal replacement and metabolic care** with nephrology, while assessing nutrition, diabetes control and medication exposure. Transplantation or improved clearance can improve selected patients, but advanced axonal loss may persist.',
    'Adjust gabapentinoids and other renally cleared pain medicines; accumulation can cause sedation, myoclonus or encephalopathy that complicates the neurological picture.',
    'Provide foot care, rehabilitation and fall prevention. The renal diagnosis should guide safe prescribing without becoming a reason to omit a focused evaluation for another treatable neuropathy.')], ['APPROACH','DSP'])

add('Common acquired and toxic neuropathies', 'Alcohol-Associated Neuropathy',
 'A person with prolonged heavy alcohol exposure has painful length-dependent sensory loss and areflexia. Which care plan is most appropriate?',
 'Address alcohol exposure, nutrition and vitamin deficiencies while evaluating other contributors and providing symptom/functional care', [
 ('Treat with a vitamin preparation while leaving alcohol-related risk and nutrition unaddressed', 'Replacement may be necessary but is not a substitute for exposure management, adequate nutrition and assessment of other causes.'),
 ('Assume thiamine deficiency is the only possible mechanism in every case', 'Direct alcohol-related toxicity and multiple nutritional/systemic factors can contribute; the mechanism should not be reduced to one deficiency in every patient.'),
 ('Start immune therapy solely from the history of burning pain', 'Painful axonal neuropathy is not proof of immune demyelination; IVIG requires an appropriate evidence-supported indication.')],
 [S('Multiple Contributors', '**Alcohol-associated neuropathy** is often length dependent and painful, with axonal sensory greater than motor involvement. Nutritional deficiencies and liver/metabolic disease may coexist.',
    'Assess intake, weight loss, thiamine/B12 and other clinically relevant nutritional risks, medications and glucose/paraprotein causes. A known exposure does not eliminate the broader differential.',
    'A rapidly evolving motor syndrome or central signs should prompt reassessment rather than automatic attribution to chronic alcohol use.'),
  S('Recovery and Support', '**Reduce or stop harmful exposure through a supported treatment plan**, with assessment and prevention of alcohol withdrawal when relevant. Provide nutritional rehabilitation and indicated vitamin replacement.',
    'Suspected Wernicke disease needs prompt parenteral thiamine and medical care; routine oral maintenance is not equivalent to treating that acute syndrome.',
    'Pain management, rehabilitation, footwear and injury prevention improve function while nerves recover. Improvement can be slow and incomplete, and high-dose mixed supplements should be reviewed to avoid additional B6 toxicity.')], ['APPROACH','B12','B6'])

R.update({
 'VASC': ('Peripheral Nerve Society guideline on nonsystemic vasculitic neuropathy, 2010', 'https://doi.org/10.1111/j.1529-8027.2010.00281.x'),
 'LEP': ('WHO management of leprosy reactions and prevention of disabilities, 2020', 'https://www.who.int/publications/i/item/9789290227595'),
 'LEPUK': ('UKHSA memorandum on leprosy, 2023', 'https://www.gov.uk/government/publications/leprosy-memorandum/memorandum-on-leprosy-2023'),
 'AMYL': ('ACC expert consensus on cardiac amyloidosis, 2023: monoclonal screening and tissue typing', 'https://www.jacc.org/doi/10.1016/j.jacc.2022.11.022'),
})

add('Systemic, infectious and paraproteinemic neuropathies', 'Vasculitic Mononeuritis Multiplex',
 'A patient develops a painful left foot drop followed three weeks later by right ulnar sensory loss and weakness. Studies show multifocal axonal loss. No systemic diagnosis is established after initial assessment. Which investigation is most useful for establishing suspected nonsystemic vasculitic neuropathy?',
 'Biopsy of a clinically and electrophysiologically affected sensory nerve, with adjacent muscle when appropriate', [
 ('Lumbar puncture for an isolated increase in CSF protein', 'CSF can support inflammatory polyradiculoneuropathy, but increased protein is nonspecific and cannot demonstrate vessel-wall injury causing multifocal axonal ischemia.'),
 ('Skin punch biopsy for intraepidermal nerve-fiber density', 'This test documents small-fiber loss when appropriate; routine fiber-density sampling does not establish the vascular pathology needed in this multifocal motor-sensory syndrome.'),
 ('Repeat nerve conduction studies to demonstrate demyelinating conduction block', 'Serial studies can resolve evolving electrodiagnostic uncertainty, but seeking a demyelinating marker would not establish suspected vasculitis in this painful multifocal axonal presentation.')],
 [S('Ischemic Injury to Individual Nerves', '**Vasculitic neuropathy** often evolves through painful, asymmetric deficits in successive nerve territories. Confluent disease may eventually resemble a polyneuropathy, so the early history matters.',
    'Examine for skin, renal, pulmonary and constitutional disease. Targeted evaluation includes urinalysis, renal function, inflammatory markers and context-directed ANCA, connective-tissue, complement, cryoglobulin and infection testing.',
    'Neither a negative ANCA result nor a normal inflammatory marker excludes nonsystemic nerve vasculitis. Conversely, an antibody alone does not establish the mechanism of nerve injury.'),
  S('Tissue Selection and Treatment Implications', '**Select an affected accessible sensory nerve**, avoiding a completely destroyed territory. Combined nerve-muscle sampling can improve the opportunity to find patchy vascular lesions when anatomically suitable.',
    'Definite histologic vasculitis requires vascular inflammation with evidence of vessel damage; sparse perivascular cells alone are insufficient. Sampling sensitivity is imperfect, and a negative biopsy must be interpreted with the phenotype and systemic evaluation.',
    'If vasculitis is already proven in another relevant tissue, nerve biopsy may be unnecessary. Rapidly progressive deficits need specialist-directed treatment; glucocorticoids and additional immunosuppression are chosen according to severity, systemic subtype and infection risks, rather than copying a CIDP regimen.')], ['VASC','APPROACH'])

add('Systemic, infectious and paraproteinemic neuropathies', 'Leprosy Reaction With New Nerve Dysfunction',
 'Six weeks after starting appropriate multidrug therapy for borderline leprosy, a patient develops swelling of existing plaques, a tender enlarged ulnar nerve and new finger-abduction weakness. There are no generalized tender nodules. What is the best next management?',
 'Urgently assess nerve function and treat a type 1 reaction with systemic corticosteroids while continuing multidrug therapy', [
 ('Replace multidrug therapy with a second-line antimicrobial regimen for presumed resistance', 'Resistance or relapse needs appropriate evidence and specialist investigation; acute inflammation of existing lesions with neuritis during treatment is characteristic of a reaction, not sufficient proof of antimicrobial failure.'),
 ('Continue multidrug therapy with analgesia and defer anti-inflammatory therapy until the course ends', 'Analgesia may relieve discomfort, but recent motor loss indicates threatened nerve function and requires prompt reaction treatment rather than waiting for antimicrobial completion.'),
 ('Use thalidomide as the principal treatment for erythema nodosum leprosum', 'Thalidomide can be used under strict specialist and pregnancy-prevention controls for selected type 2 reactions, but this plaque-based reversal reaction with neuritis requires a different treatment approach.')],
 [S('Recognize the Reaction Pattern', '**Type 1 or reversal reactions** occur especially in borderline disease, with inflammation of existing lesions and potentially severe neuritis. They can appear before, during or after antimicrobial treatment.',
    'Type 2 reactions, or erythema nodosum leprosum, more often produce crops of tender nodules with systemic inflammation in multibacillary disease. The distinction guides therapy, but new nerve dysfunction is urgent in either setting.',
    'Document sensory testing and voluntary muscle strength at baseline and serially. Nerve pain can be absent despite functional deterioration; tenderness alone is not an adequate monitoring measure.'),
  S('Preserve Function During Treatment', '**Continue the indicated multidrug course** while treating the immune reaction. Recent neuritis with weakness generally warrants systemic prednisolone under a leprosy service, followed by a response-guided taper.',
    'A commonly used adult initial dose is approximately 40–60 mg/day, adjusted for weight, severity and local protocol. Courses often require months; a brief analgesic-style steroid burst is inadequate for significant nerve injury.',
    'Assess infection, glucose and steroid adverse-effect risks; provide rest or splinting during acute neuritis, subsequent rehabilitation, protective footwear and care of insensitive skin. Recheck function during taper because recurrent inflammation may require reassessment and adjustment.')], ['LEP','LEPUK'])

add('Systemic, infectious and paraproteinemic neuropathies', 'Typing Suspected Amyloid Neuropathy',
 'A patient has progressive painful axonal neuropathy, orthostatic hypotension, nephrotic-range proteinuria and a small IgG-lambda monoclonal protein. Fat-pad sampling shows Congo-red-positive material. Which step is most appropriate before choosing disease-directed treatment?',
 'Type the deposited amyloid using a validated method, preferably mass spectrometry, with hematologic assessment', [
 ('Classify the deposits as AL solely because a monoclonal protein is present', 'A monoclonal gammopathy increases concern for AL but can coexist with ATTR or another amyloid type; treatment requires establishing the actual deposited precursor.'),
 ('Use technetium-PYP scintigraphy alone to determine whether the neuropathy is caused by AL', 'Bone-avid scintigraphy has a defined role in ATTR cardiac assessment after appropriate exclusion of AL; it does not type peripheral-nerve deposits or establish AL neuropathy.'),
 ('Use TTR sequencing alone to assign the precursor in the Congo-red-positive tissue', 'Sequencing is important when hereditary ATTR is suspected, but finding a variant does not by itself prove that these deposits contain TTR rather than immunoglobulin light chains.')],
 [S('Detect the Clone and Identify the Deposit', '**Amyloid neuropathy** may combine painful sensory loss, progressive weakness and disproportionate autonomic dysfunction. Proteinuria, cardiomyopathy, weight loss and carpal tunnel disease strengthen suspicion but do not identify the precursor.',
    'Screen with serum free light chains and both serum and urine immunofixation. Routine protein electrophoresis alone can miss a small pathogenic clone. Renal impairment changes light-chain concentrations and ratio interpretation.',
    'Congo red demonstrates amyloid but does not distinguish AL from ATTR. Validated tissue typing, preferably proteomic mass spectrometry where available, prevents potentially harmful treatment based on an incidental monoclonal gammopathy.'),
  S('Interpret Negative and Positive Tests', '**A negative fat-pad sample does not exclude amyloidosis**; persistent suspicion may require another appropriate tissue site, balancing yield and procedural risk.',
    'Assess cardiac and renal involvement promptly because these influence prognosis and treatment tolerance. A PYP scan cannot replace tissue typing in a patient with a monoclonal protein and suspected cardiac amyloid.',
    'Confirmed AL requires urgent hematology-led plasma-cell-directed care; ATTR requires TTR-focused evaluation and treatment. Support autonomic symptoms, nutrition and neuropathic pain while preserving blood pressure and avoiding unnecessary neurotoxic exposures.')], ['AMYL','APPROACH'])

R.update({
 'ATTR': ('GeneReviews: hereditary transthyretin amyloidosis, updated 2024', 'https://www.ncbi.nlm.nih.gov/books/NBK1194/'),
 'ATTRCON': ('Expert consensus to improve diagnosis of ATTR amyloidosis with polyneuropathy, 2021', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC8179912/'),
 'EPL': ('US WAINUA/eplontersen prescribing information, revised 2026', 'https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/217388s005lbl.pdf'),
 'POEMS': ('Comprehensive diagnosis and management of POEMS syndrome, 2022', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9624442/'),
 'POEMS26': ('POEMS syndrome: 2026 update on diagnosis, risk stratification and management', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC13540325/'),
 'MAG': ('Anti-MAG neuropathy: where do we stand? 2023', 'https://doi.org/10.1002/mus.27954'),
 'RIMAG': ('Placebo-controlled rituximab trial in IgM anti-MAG neuropathy, 2013', 'https://pubmed.ncbi.nlm.nih.gov/23667063/'),
})

add('Systemic, infectious and paraproteinemic neuropathies', 'Hereditary Transthyretin Amyloid Red Flags',
 'A 58-year-old has progressive axonal sensorimotor neuropathy, orthostatic hypotension, alternating diarrhea and constipation, bilateral carpal tunnel operations years earlier and unexplained ventricular wall thickening. There is no known family history. Which investigation most directly addresses the suspected hereditary cause?',
 'TTR sequencing with genetic counseling and appropriate evaluation for typed amyloid deposition', [
 ('PMP22 copy-number testing as the initial molecular test', 'PMP22 testing is appropriate for typical CMT1A or recurrent pressure palsies, but neither usually explains the autonomic, gastrointestinal and infiltrative cardiac combination.'),
 ('A paraneoplastic neuronal antibody panel as the initial etiologic test', 'A subacute sensory neuronopathy with non-length-dependent loss can justify paraneoplastic evaluation; this progressive multisystem amyloid pattern more directly warrants TTR investigation.'),
 ('Repeat CIDP antibody testing followed by another empiric IVIG course', 'Immune testing can be useful in a compatible acquired demyelinating phenotype, but progressive axonal disease with amyloid red flags requires reassessment before additional immune therapy.')],
 [S('A Multisystem Pattern', '**ATTRv neuropathy** can begin with small-fiber and autonomic symptoms before obvious large-fiber weakness. Carpal tunnel syndrome may precede generalized disease by years.',
    'Cardiac infiltration, weight loss and gastrointestinal or erectile dysfunction strengthen suspicion. None is specific alone, and diabetes or an incidental entrapment must not end the investigation when progression is disproportionate.',
    'Apparent demyelinating features can lead to a CIDP label, particularly with severe axonal loss. Revisit the diagnosis when the clinical pattern or response to immune treatment is discordant.'),
  S('Molecular Confirmation and Family Care', '**A pathogenic TTR variant** supports hereditary disease in the appropriate phenotype. Interpret variants of uncertain significance carefully and use tissue confirmation with validated precursor typing when required by the diagnostic context.',
    'Absence of a known family history does not exclude autosomal dominant disease because onset, penetrance and recognition vary. Offer counseling before predictive testing of relatives.',
    'Evaluate cardiac, renal, nutritional, autonomic and ocular involvement. Distinguish hereditary ATTR from wild-type ATTR and AL; a cardiac imaging result alone does not establish the cause of every neuropathy. Early specialist assessment matters because disease-modifying treatment aims to limit further injury, while established deficits may persist.')], ['ATTR','ATTRCON','AMYL'])

add('Systemic, infectious and paraproteinemic neuropathies', 'TTR Silencing for Amyloid Polyneuropathy',
 'Which agent is a TTR-directed antisense oligonucleotide with a 2026 US-labeled indication for adult hereditary ATTR polyneuropathy and a subcutaneous once-monthly regimen?',
 'Eplontersen', [
 ('Patisiran', 'Patisiran also treats hereditary ATTR polyneuropathy, but uses RNA interference and intravenous administration rather than the antisense, monthly subcutaneous regimen specified.'),
 ('Vutrisiran', 'Vutrisiran is a subcutaneous TTR silencer used for ATTR disease, but is an siRNA agent with a different dosing interval, not this antisense formulation.'),
 ('Tafamidis', 'Tafamidis stabilizes the TTR tetramer rather than lowering hepatic production through antisense action; indication and formulation differ by jurisdiction, including US cardiomyopathy labeling.')],
 [S('Reduce the Precursor or Stabilize It', '**TTR gene silencers** lower hepatic production of transthyretin, including variant and wild-type protein. Antisense oligonucleotides and siRNA reach this goal through different molecular machinery.',
    'Stabilizers instead reduce tetramer dissociation. These are disease-modifying strategies, distinct from analgesics or drugs treating orthostatic hypotension; symptom relief does not demonstrate control of deposition.',
    'Do not extrapolate a cardiomyopathy indication to polyneuropathy, or a regional approval to worldwide availability. Selection also considers phenotype, organ involvement, stage, access and the specific product label.'),
  S('Eplontersen Regimen and Monitoring', '**The 2026 US WAINUA regimen is ==45 mg subcutaneously once monthly==** for adults with hereditary ATTR polyneuropathy. It is not a weight-based intravenous infusion.',
    'Reduced circulating TTR lowers serum vitamin A. Supplement at the recommended daily allowance; high doses should not be used merely to normalize a serum concentration affected by transport-protein reduction.',
    'Refer patients with possible vitamin-A-deficiency ocular symptoms, such as night blindness, for ophthalmologic assessment. Continue objective neurologic, functional and multisystem follow-up; treatment cannot be assumed to reverse established axonal loss. Check the current product-specific instructions rather than transferring safety schedules or administration rules between different TTR drugs.')], ['EPL','ATTR'], style='direct')

add('Systemic, infectious and paraproteinemic neuropathies', 'POEMS Diagnostic Requirements',
 'A patient has a progressive demyelinating polyneuropathy, an IgA-lambda plasma-cell clone, a sclerotic bone lesion and peripheral edema. Which statement best applies the POEMS diagnostic framework?',
 'Both mandatory criteria, at least one other major criterion and at least one minor criterion are present', [
 ('All five features represented by the acronym must be present', 'The acronym describes a syndrome, but the formal framework does not require all five named features; specific mandatory, other-major and minor requirements determine diagnosis.'),
 ('The monoclonal protein and edema suffice even without polyneuropathy', 'A plasma-cell disorder with volume overload has several causes; neuropathy is one of the two mandatory criteria in the standard POEMS framework.'),
 ('The sclerotic lesion is a minor criterion and requires Castleman disease as an additional mandatory feature', 'A sclerotic bone lesion is an other-major criterion; Castleman disease is another possible major feature, not a universal additional requirement.')],
 [S('Apply Criteria Rather Than the Acronym', '**Both mandatory findings** are polyneuropathy, usually with conduction slowing, and a monoclonal plasma-cell disorder, typically lambda restricted.',
    'At least one other major finding and one minor finding are also required. A small clone can be clinically important; the amount of monoclonal protein does not reliably measure the systemic syndrome.',
    'Neuropathy may be misclassified as CIDP. Edema, thrombocytosis, skin change or a sclerotic lesion should trigger a broader search rather than indefinite escalation of immune therapy.'),
  S('Investigations and Treatment Direction', '**VEGF supports diagnosis and follow-up**, but serum and plasma values differ and cutoffs are assay dependent. Interpret elevations alongside the phenotype and exclude alternative contributors.',
    'Assess marrow, skeletal lesions, volume overload, endocrine function, eye grounds and cardiopulmonary involvement. Isolated common diabetes or thyroid disease does not satisfy the endocrinopathy criterion by itself.',
    'Treatment targets the plasma-cell process: a suitable isolated lesion may receive radiotherapy, whereas disseminated disease requires systemic specialist therapy, sometimes including autologous transplantation. IVIG-based CIDP treatment does not address the underlying clone.')], ['POEMS','POEMS26'],
 table=(['Category','Required findings'],[
 ['Mandatory: both','Polyneuropathy; monoclonal plasma-cell disorder'],
 ['Other major: at least one','Sclerotic bone lesion; Castleman disease; elevated VEGF'],
 ['Minor: at least one','Organomegaly; extravascular volume overload; qualifying endocrinopathy; skin changes; papilledema; thrombocytosis/polycythemia']]))

add('Systemic, infectious and paraproteinemic neuropathies', 'IgM Anti-MAG Distal Neuropathy',
 'A 69-year-old has years of slowly progressive distal sensory loss, gait ataxia and hand tremor, with little proximal weakness. Nerve studies show disproportionate distal motor latency prolongation; immunofixation identifies IgM-kappa and anti-MAG antibodies are strongly positive. Which diagnosis best fits?',
 'IgM anti-MAG-associated distal demyelinating neuropathy', [
 ('Typical CIDP', 'Typical CIDP usually combines proximal and distal weakness with sensory involvement; this slowly distal sensory-ataxic phenotype and strong anti-MAG association identify a distinct paraproteinemic disorder.'),
 ('POEMS syndrome', 'POEMS can cause demyelinating neuropathy, but usually involves a lambda plasma-cell process plus its required systemic criteria; IgM anti-MAG with this distal pattern favors another entity.'),
 ('AL amyloid neuropathy', 'AL often produces painful axonal and autonomic neuropathy with organ disease; a strongly anti-MAG-associated distal demyelinating pattern is a different mechanism despite both involving a monoclonal protein.')],
 [S('Recognize the Distal Phenotype', '**Anti-MAG neuropathy** is commonly associated with an IgM monoclonal gammopathy and a slowly progressive distal sensory-predominant syndrome. Sensory ataxia and tremor can be prominent before major weakness.',
    'Electrodiagnostics often show marked distal slowing, reflecting distal myelin dysfunction. A low antibody result without a compatible phenotype is less persuasive than a strong result in this characteristic clinical setting.',
    'Evaluate the hematologic clone and consider an underlying lymphoproliferative disorder. A small clone may still produce a pathogenic antibody; absence of overt malignancy does not establish that the neuropathy is unrelated.'),
  S('Treatment Evidence and Follow-up', '**Treat disability and progression rather than the antibody number alone.** Stable mild disease may be monitored with functional measures, rehabilitation and fall prevention.',
    'Progressive disabling disease warrants joint neurology-hematology consideration of clone-directed therapy. Rituximab is used in selected patients, but the randomized trials did not meet their primary endpoints; it should not be described as uniformly proven to reverse this disease.',
    'IVIG may provide limited or transient benefit in some patients, but the durable response expected in typical CIDP cannot be assumed. Assess gait, hand function and patient-centered disability over an appropriate interval; changes in IgM or antibody titers alone are insufficient proof of clinical improvement.')], ['MAG','RIMAG','CIDP'])

R.update({
 'CMT': ('GeneReviews: Charcot-Marie-Tooth hereditary neuropathy overview', 'https://www.ncbi.nlm.nih.gov/books/NBK1358/'),
 'HNPP': ('GeneReviews: hereditary neuropathy with liability to pressure palsies', 'https://www.ncbi.nlm.nih.gov/books/NBK1392/'),
 'CMTX': ('GeneReviews: GJB1 disorders and CMT1X', 'https://www.ncbi.nlm.nih.gov/books/NBK1374/'),
 'REFSUM': ('GeneReviews: adult Refsum disease', 'https://www.ncbi.nlm.nih.gov/books/NBK1353/'),
 'REFSUM26': ('Global DARE committee guidance on diagnosis and metabolic management of adult Refsum disease, 2026', 'https://doi.org/10.1002/jimd.70201'),
})

add('Hereditary neuropathies', 'CMT1A and PMP22 Copy Number',
 'A 24-year-old has slowly progressive distal leg wasting, pes cavus and absent ankle reflexes since adolescence. His father has similar feet. Motor conduction velocities are diffusely and relatively uniformly reduced without convincing multifocal block. Which molecular abnormality is most likely?',
 'PMP22 duplication', [
 ('PMP22 deletion', 'A deletion usually causes HNPP, characterized by recurrent pressure-related focal palsies and entrapment susceptibility rather than this classic steadily progressive CMT1A phenotype.'),
 ('GJB1 pathogenic variant', 'GJB1 causes X-linked CMT with variable conduction slowing; direct father-to-son transmission, as described here, does not fit X-linked inheritance.'),
 ('MFN2 pathogenic variant', 'MFN2 is an important cause of axonal CMT2, where reduced amplitudes predominate and motor velocities are usually more preserved than in this uniform demyelinating pattern.')],
 [S('Inherited Versus Acquired Demyelination', '**CMT1A** commonly causes a symmetric distal motor-sensory neuropathy with foot deformity, slowly progressive weakness and longstanding areflexia. Hand weakness can develop later.',
    'Relatively uniform slowing favors an inherited myelin disorder, whereas multifocal block or marked temporal dispersion can support acquired disease in the proper setting. These are pattern clues, not absolute exclusions.',
    'Family history may be absent because of a new variant, subtle manifestations or limited information. Ask about high arches, ankle instability, orthoses and unexplained gait problems in relatives.'),
  S('Testing and Functional Care', '**PMP22 copy-number analysis** is an appropriate early genetic test in a classic CMT phenotype; ensure that a sequencing panel actually includes deletion/duplication detection.',
    'If negative, phenotype- and inheritance-directed testing or a suitably designed multigene panel follows. A variant of uncertain significance should not be treated as a confirmed diagnosis.',
    'Provide genetic counseling, physiotherapy, ankle-foot orthoses and assessment of orthopedic deformity, pain and occupational needs. Avoid empiric long-term immune therapy merely because velocities are slow. Review potentially neurotoxic drugs and functional decline; a new abrupt asymmetric deficit still warrants assessment for a superimposed cause.')], ['CMT','CIDP'])

add('Hereditary neuropathies', 'Hereditary Liability to Pressure Palsies',
 'A 29-year-old has recovered from wrist drop after sleeping on an arm and foot drop after prolonged leg crossing. Studies show disproportionate slowing at several entrapment sites, including asymptomatic nerves. His mother reports similar episodes. Which test is most appropriate initially?',
 'PMP22 deletion/duplication analysis', [
 ('GJB1 sequence analysis alone', 'GJB1 testing is appropriate in an X-linked CMT pattern, but recurrent pressure-triggered focal palsies with multifocal entrapment abnormalities more strongly suggest a PMP22 dosage disorder.'),
 ('TTR sequencing alone', 'TTR testing addresses suspected hereditary amyloid neuropathy, especially autonomic and multisystem disease, rather than recurrent recoverable pressure palsies in this family.'),
 ('Serum anti-GM1 IgM as the principal confirmatory test', 'Anti-GM1 can support MMN in a compatible progressive pure motor syndrome; it does not establish the inherited sensory-motor pressure susceptibility seen here.')],
 [S('Recognize a Dosage Disorder', '**HNPP** commonly results from a PMP22 deletion; some affected individuals have a pathogenic sequence variant. The phenotype is recurrent focal neuropathy at pressure-prone sites, sometimes with residual weakness or a mild background polyneuropathy.',
    'Episodes can be painless and recovery can be substantial, but complete recovery is not guaranteed. An isolated common entrapment is not sufficient to diagnose a hereditary syndrome.',
    'Electrodiagnostics may reveal abnormalities outside the currently symptomatic nerve. Interpret diffuse mild slowing and focal entrapment together with the history rather than equating multiple slow segments with CIDP.'),
  S('Prevent Further Nerve Injury', '**Reduce prolonged compression and repetitive mechanical stress** through positioning, protective padding and occupational adjustments. Avoid sustained leg crossing, prolonged elbow pressure and poorly positioned immobilization.',
    'Use temporary splints or ankle-foot orthoses, rehabilitation and symptom-directed pain treatment as needed. Counsel surgical and anesthesia teams about careful positioning and pressure protection.',
    'Most families show autosomal dominant inheritance, so counseling includes a 50% transmission probability for an affected heterozygous parent. Test relatives through an informed genetic pathway. New persistent deficits still need examination for structural compression or another treatable process; an inherited predisposition does not make every subsequent symptom attributable to HNPP.')], ['HNPP','CMT'])

add('Hereditary neuropathies', 'GJB1-Related X-Linked CMT',
 'A man with molecularly confirmed GJB1-related CMT asks about transmission to his children. His partner does not carry the familial variant. Which counseling statement is correct?',
 'All daughters inherit his GJB1 variant; none of his sons inherit it from him', [
 ('Each son and daughter has a 50% chance of inheriting his variant', 'That pattern applies to a heterozygous mother with an X-linked variant or to an autosomal dominant variant, not transmission of an affected father’s X chromosome.'),
 ('All sons inherit his variant and daughters do not', 'A father transmits his Y chromosome to sons and his X chromosome to daughters; this proposed pattern reverses X-linked transmission.'),
 ('Daughters inherit the variant only if their mother also carries it', 'The paternal X chromosome reaches every daughter irrespective of the mother’s genotype; two affected alleles are not required for a daughter to inherit or manifest this disorder.')],
 [S('Inheritance and Variable Expression', '**GJB1 encodes connexin 32** and causes X-linked CMT1X. Affected males are often more severely involved, but heterozygous females may have clinically important neuropathy.',
    'There is no father-to-son transmission of the paternal X-linked variant. A heterozygous woman has a 50% chance of transmitting the variant to each child, with severity varying by sex and other factors.',
    'A negative family history does not rule out the diagnosis. Mildly affected female relatives, new variants and incomplete pedigree information can obscure the pattern.'),
  S('Clinical Interpretation and Counseling', '**Intermediate or variable conduction slowing** can occur; do not restrict inherited neuropathy to the uniform demyelination pattern of CMT1A. Clinical course, pedigree and molecular evidence must agree.',
    'Some GJB1 variants are associated with transient central neurologic episodes and white-matter abnormalities. An acute episode still requires urgent assessment for vascular, infectious or metabolic causes rather than automatic genetic attribution.',
    'Offer formal genetic counseling, targeted testing for the established familial variant and individualized reproductive discussion. Provide rehabilitation, orthoses and orthopedic or occupational support according to function. Molecular confirmation informs relatives and avoids unnecessary immune treatment, but does not predict the precise severity in every child.')], ['CMTX','CMT'], style='direct')

add('Hereditary neuropathies', 'Treatable Adult Refsum Disease',
 'A young adult with progressive neuropathy and ataxia reports longstanding night blindness and loss of smell. Examination shows ichthyosis and retinal pigmentary degeneration. Plasma phytanic acid is markedly elevated. Which long-term management principle is most appropriate?',
 'Restrict dietary phytanic acid with specialist support while maintaining adequate energy intake and avoiding fasting', [
 ('Use a phytanic-acid-restricted diet combined with prolonged fasting to accelerate weight loss', 'Restriction is appropriate, but fasting mobilizes stored phytanic acid during lipolysis and can precipitate deterioration; adequate energy intake is essential.'),
 ('Use high-dose pyridoxine as the main disease-modifying treatment', 'Pyridoxine has roles in selected deficiencies and metabolic disorders, but does not correct the phytanic-acid pathway here; excess itself can cause sensory neuropathy.'),
 ('Use routine chronic IVIG as the principal treatment for the neuropathy', 'IVIG treats selected immune neuropathies, whereas this retinal, olfactory and biochemical pattern identifies a metabolic accumulation disorder requiring substrate-directed management.')],
 [S('Identify a Metabolic Neuropathy', '**Adult Refsum disease** is a peroxisomal disorder of phytanic-acid handling, usually due to biallelic PHYH variants and less often PEX7 variants. It is distinct from the older infantile Refsum terminology within the Zellweger spectrum.',
    'Retinitis pigmentosa, anosmia, neuropathy, ataxia, hearing impairment and ichthyosis occur in varying combinations. Cardiac conduction disease or arrhythmia can be dangerous and requires assessment.',
    'Measure plasma phytanic acid and pursue molecular confirmation through a metabolic service. Dietary exposure influences levels; interpret results with the phenotype and specialist laboratory advice.'),
  S('Prevent Catabolism and Reduce Exposure', '**Specialist dietary therapy** reduces phytanic-acid intake while preserving sufficient calories and nutritional adequacy. Avoid prolonged fasting and rapid weight loss, including around illness or procedures.',
    'Acute metabolic deterioration can require therapeutic plasma exchange together with nutritional measures; this is a specialist intervention, not a substitute for sustained dietary management.',
    'Follow phytanic acid, nutritional status, neurologic function, hearing, vision and cardiac involvement. Neuropathy and systemic features may improve or stabilize, while established retinal injury may persist. The 2026 metabolic guidance acknowledges limited disease-specific evidence for some emergency nutrition practices; do not present extrapolated protocols as randomized-trial-proven cures.')], ['REFSUM','REFSUM26','B6'])

R.update({
 'CTS': ('AAOS management of carpal tunnel syndrome guideline, 2024', 'https://www.aaos.org/globalassets/quality-and-practice-resources/carpal-tunnel/carpal-tunnel-2024/cts-cpg.pdf'),
 'CTSREL': ('Academy of Medical Royal Colleges: carpal tunnel release, reviewed 2024', 'https://ebi.aomrc.org.uk/interventions/carpal-tunnel-syndrome-release/'),
 'ULNAR': ('AAPM&R: ulnar mononeuropathy at the elbow', 'https://now.aapmr.org/ulnar-nerve-mononeuropathy-at-the-elbow-2/'),
 'RADIAL': ('AAPM&R: radial nerve mononeuropathy', 'https://now.aapmr.org/radial-nerve-mononeuropathy-2/'),
 'FIBULAR': ('AAPM&R: knee neuropathies', 'https://now.aapmr.org/knee-neuropathies/'),
 'NA': ('AAPM&R: immune-mediated brachial plexopathy', 'https://now.aapmr.org/immune-mediated-brachial-plexopathy/'),
 'NAPNS': ('Orphanet: neuralgic amyotrophy', 'https://www.orpha.net/en/disease/detail/2901'),
})

add('Focal neuropathies and plexopathies', 'Severe Carpal Tunnel Syndrome',
 'A patient with confirmed median neuropathy at the wrist has persistent numbness despite a neutral night splint, progressive thenar weakness and active denervation in abductor pollicis brevis. Which next step best addresses the risk of further nerve injury?',
 'Refer for carpal tunnel decompression assessment', [
 ('Repeat local corticosteroid injections as the definitive long-term strategy', 'Injection can help short-term symptoms in selected patients, but is not a durable solution for progressive motor deficit and denervation in severe compression.'),
 ('Continue splinting alone for another six months before referral', 'Neutral splinting is reasonable for mild or moderate intermittent symptoms, but further delay is less suitable when objective motor deterioration suggests significant nerve injury.'),
 ('Use a neuropathic analgesic as the principal treatment and reassess only if pain increases', 'Analgesics can reduce discomfort but do not decompress the median nerve; motor and sensory progression, rather than pain intensity alone, determine concern.')],
 [S('Assess Severity Beyond Nocturnal Tingling', '**Median compression at the wrist** commonly causes nocturnal paresthesia in the radial digits and may progress to persistent sensory loss and thenar weakness. Sensation over the thenar eminence can be spared because the palmar cutaneous branch travels outside the tunnel.',
    'Objective weakness, atrophy or denervation indicates a different risk from intermittent paresthesia alone. Evaluate alternative or coexisting root, plexus and generalized nerve disease when the distribution is atypical.',
    'A validated clinical approach can diagnose many typical cases. Electrodiagnostics are particularly helpful for severity, uncertainty and competing pathology; they are not a universal prerequisite for every clinical diagnosis.'),
  S('Match Treatment to Nerve Injury', '**Early surgical assessment is appropriate for severe or progressive deficit**, with shared discussion of decompression, risks and realistic recovery. Longstanding axonal loss can limit motor recovery even after successful release.',
    'For milder disease, neutral night positioning and selected injection can reduce symptoms. The AAOS 2024 guideline distinguishes short-term injection benefit from lack of sustained long-term improvement.',
    'Address contributing conditions and functional demands without promising that metabolic correction alone resolves established mechanical compression. Monitor sensation, thenar strength and daily function, not just pain. Explain that decompression prevents ongoing pressure but does not guarantee immediate reversal of every deficit.')], ['CTS','CTSREL'])

add('Focal neuropathies and plexopathies', 'When an Ulnar Label Is Too Narrow',
 'A patient has weak finger abduction and numbness of the little finger. Which additional finding most strongly argues for a C8–T1/root or lower-plexus process rather than an isolated ulnar lesion?',
 'Weak median-innervated thenar abduction together with medial forearm sensory loss', [
 ('Weak first dorsal interosseous with little-finger numbness', 'Both are within the ulnar distribution and are compatible with an ulnar mononeuropathy; they do not independently show involvement beyond that nerve.'),
 ('Weak flexor carpi ulnaris with weak ulnar-innervated finger flexors', 'A sufficiently proximal ulnar lesion can involve these forearm muscles, so their weakness does not by itself require a root or plexus lesion.'),
 ('Reduced dorsal ulnar hand sensation with weak interossei', 'This combination can occur in an ulnar lesion proximal to the dorsal cutaneous branch and helps distinguish elbow-region disease from some wrist lesions.')],
 [S('Test Muscles Outside the Suspected Nerve', '**Root and plexus lesions cross named-nerve boundaries.** Abductor pollicis brevis is median innervated, while the medial forearm is supplied by the medial antebrachial cutaneous nerve rather than the ulnar nerve.',
    'Map objective weakness, sensory loss and reflexes rather than relying on a patient’s broad description of tingling. Coexisting median and ulnar entrapments can still complicate interpretation.',
    'An ulnar lesion at the wrist often spares dorsal ulnar sensation and forearm muscles. Elbow lesions can affect those territories, depending on level, severity and fascicular involvement.'),
  S('Resolve the Level With Targeted Testing', '**Electrodiagnostics should sample ulnar and non-ulnar C8–T1 muscles**, relevant sensory responses and, when appropriate, paraspinal muscles. Isolated abnormalities at a common entrapment site should not override a broader clinical pattern.',
    'Root lesions are generally proximal to the sensory ganglion and preserve distal SNAPs; plexus lesions can reduce them. Technical factors and coexisting neuropathy can obscure this distinction, and an early study can be nondiagnostic.',
    'Use cervical or plexus imaging when indicated by localization, progression, severe pain, trauma, cancer risk or other concerning features. Persistent progressive weakness should not be managed indefinitely as an uncomplicated elbow entrapment without reassessment.')], ['ULNAR','APPROACH'])

add('Focal neuropathies and plexopathies', 'Posterior Interosseous Localization',
 'A patient cannot extend the fingers at the metacarpophalangeal joints or extend the thumb. Wrist extension is retained but deviates radially. Triceps strength and first dorsal web-space sensation are normal. Which localization best fits?',
 'Posterior interosseous nerve', [
 ('Radial nerve at the spiral groove', 'A spiral-groove lesion can spare triceps but commonly weakens wrist extension more broadly and may impair superficial radial sensation; the preserved radial wrist extension and sensory sparing favor a more distal motor branch.'),
 ('Superficial radial sensory nerve', 'This branch causes sensory symptoms over the dorsoradial hand without finger-extensor paralysis, so it cannot account for the objective motor deficit.'),
 ('C7 nerve root', 'A C7 lesion can affect extensors but often also involves nonradial C7 muscles, reflexes or root-related pain; the selective distal radial motor pattern is more consistent with PIN disease.')],
 [S('Interpret Preserved Wrist Extension', '**The posterior interosseous nerve** supplies most finger and thumb extensors but no cutaneous sensory territory. Extensor carpi radialis longus receives a more proximal branch and can preserve wrist extension.',
    'Loss of ulnar-directed wrist-extensor force can cause radial deviation during extension. Evaluate true metacarpophalangeal extension rather than assuming preserved interphalangeal extension excludes extensor weakness.',
    'The superficially adjacent radial sensory branch has a different functional role. A normal sensory examination helps localization but does not exclude a motor neuropathy.'),
  S('Find the Cause and Protect Function', '**Consider focal compression, a structural lesion or inflammatory fascicular injury**, guided by onset, pain and examination. Electrodiagnostics define distribution and axonal involvement; ultrasound or MRI can identify a mass or focal constriction when suspected.',
    'A painful radial-tunnel syndrome without objective motor deficit should not be equated with a clear PIN palsy. Tendon rupture and mechanical finger problems also deserve consideration when the examination is inconsistent.',
    'Use splinting and hand therapy to maintain function and range while investigating the cause. Progressive deficit, a compressive mass, trauma or failure to recover warrants specialist reassessment; an anatomic label alone does not determine whether observation or decompression is appropriate.')], ['RADIAL','APPROACH'])

R['MERALGIA'] = ('AAOS OrthoInfo: meralgia paresthetica', 'https://www.orthoinfo.org/diseases--conditions/burning-thigh-pain-meralgia-paresthetica/')

add('Focal neuropathies and plexopathies', 'Protecting Gait in Fibular Compression Palsy',
 'After prolonged squatting, a patient develops a painless foot drop. Examination and studies localize a common fibular compression neuropathy at the fibular head, without trauma, a mass or progressive deterioration. Which initial plan is best?',
 'Remove pressure, provide an ankle-foot orthosis and rehabilitation, and arrange reassessment of recovery', [
 ('Use observation alone without gait support until dorsiflexion returns', 'Some compression lesions recover with time, but unprotected foot drop increases falls and contracture risk; gait support and rehabilitation address immediate functional consequences.'),
 ('Proceed directly to surgical exploration despite no structural lesion or progressive deficit', 'Exploration is appropriate in selected traumatic, structural, progressive or nonrecovering cases; it is not automatically the first step for a stable pressure palsy without those features.'),
 ('Begin systemic corticosteroids as the principal treatment of the compression', 'Steroids have roles in selected inflammatory disorders, but do not replace pressure relief and functional protection in a localized mechanical compression palsy.')],
 [S('Reduce Pressure and Prevent Secondary Injury', '**Common fibular neuropathy at the fibular head** is vulnerable to external pressure, prolonged squatting, immobilization and marked weight loss. Management depends on both cause and severity, not the foot-drop label alone.',
    'Check for trauma, a compressive cyst or mass, severe pain and progressive deficits. A broader distribution of weakness, upper motor neuron signs or sphincter symptoms requires reconsideration of the localization.',
    'An ankle-foot orthosis improves toe clearance and gait safety. Maintain passive ankle range, especially dorsiflexion, and use graded rehabilitation to prevent shortening and compensatory injury.'),
  S('Follow the Trajectory', '**Serial examination and appropriately timed electrodiagnostics** help assess axonal injury and reinnervation. Very early tests may not fully show denervation, and recovery time varies with the injury mechanism.',
    'Relieve ongoing external compression and review positioning, braces and habitual leg crossing. Address nutritional or systemic contributors when relevant rather than assuming all risk is mechanical.',
    'Persistent severe weakness, absent expected recovery, a structural lesion or new deterioration warrants specialist reassessment and possible surgical evaluation. Do not promise a fixed recovery interval or defer a concerning mass because the first impression was a benign posture-related palsy.')], ['FIBULAR','APPROACH'])

add('Focal neuropathies and plexopathies', 'Meralgia Paresthetica and Motor Red Flags',
 'An obese patient wearing a tight work belt develops burning and numbness confined to the anterolateral thigh. Strength and knee reflexes are normal. Which new finding would most strongly require a diagnosis beyond isolated meralgia paresthetica?',
 'Objective knee-extension weakness with a reduced patellar reflex', [
 ('Symptoms worsening with a tight belt', 'External compression near the inguinal ligament is a common provoking factor in lateral femoral cutaneous neuropathy and supports, rather than challenges, the proposed localization.'),
 ('A small patch of reduced pin sensation over the lateral thigh', 'A focal sensory deficit in the lateral femoral cutaneous distribution is compatible with meralgia paresthetica and does not imply motor nerve or root involvement.'),
 ('Burning pain without symptoms below the knee', 'Localized burning in this sensory territory can occur in meralgia; absence of distal leg symptoms does not establish a broader femoral or root lesion.')],
 [S('A Pure Sensory Nerve', '**The lateral femoral cutaneous nerve** supplies sensation over a variable anterolateral thigh territory and has no motor function. Compression commonly occurs near the inguinal ligament.',
    'Obesity, pregnancy, tight garments and local procedures can predispose. A typical history and examination often establish the working diagnosis without extensive testing.',
    'Quadriceps weakness or a depressed knee reflex suggests femoral neuropathy, an upper lumbar root/plexus process or another additional lesion. Back pain, widespread deficits or systemic warning features also change the investigation pathway.'),
  S('Conservative Care and Selective Testing', '**Reduce external pressure** by modifying belts or clothing and addressing contributing factors. Offer symptom-directed treatment while monitoring the distribution and neurologic examination.',
    'Electrodiagnostics or imaging are reserved for diagnostic uncertainty, atypical findings or suspected structural disease. Technical difficulty recording this sensory response, especially in obesity, means an absent result is not diagnostic in isolation.',
    'A selected local anesthetic block can help diagnosis or symptom control. Persistent disabling symptoms may merit specialist interventions, but invasive treatment is not required for every presentation. Reassess new weakness rather than attributing it to pain from a nerve that carries no motor fibers.')], ['MERALGIA','APPROACH'])

add('Focal neuropathies and plexopathies', 'Neuralgic Amyotrophy',
 'A patient develops abrupt severe shoulder pain without trauma. Ten days later the pain eases, but scapular winging and patchy weakness of shoulder external rotation appear. Passive shoulder movement is preserved, and the weakness does not fit one root. Which diagnosis best fits?',
 'Neuralgic amyotrophy', [
 ('Cervical radiculopathy', 'A root lesion can cause shoulder pain and weakness, but a consistent myotomal pattern, reflex changes or neck-related provocation would be more expected than this patchy sequential pain-then-paresis syndrome.'),
 ('Rotator cuff tear', 'Cuff disease can impair shoulder elevation or rotation and may follow trauma, but does not explain neurogenic scapular winging and weakness distributed across separate nerve territories.'),
 ('Compressive upper-trunk plexopathy', 'A structural plexus lesion can cause similar weakness and requires exclusion when indicated; the abrupt severe pain followed by patchy paresis without trauma more strongly suggests neuralgic amyotrophy.')],
 [S('Pain Followed by Patchy Paresis', '**Neuralgic amyotrophy** often begins with intense shoulder or upper-arm pain, followed over days to weeks by weakness in a multifocal nerve distribution. Long thoracic and suprascapular involvement can produce winging and external-rotation weakness.',
    'The syndrome can involve selected fascicles or individual nerves rather than the entire plexus. Sensory symptoms are variable, and a painless presentation is possible but less typical.',
    'Ask about prior attacks, family history, recent illness and procedures. A temporal association with a potential trigger does not by itself establish causation.'),
  S('Exclude Structural Disease and Support Recovery', '**Targeted electrodiagnostics and imaging** help confirm distribution and exclude cervical, shoulder or plexus pathology. A very early EMG may precede demonstrable denervation and should not overrule a compelling evolving examination.',
    'Treat acute pain and provide rehabilitation tailored to weakness, scapular mechanics and endurance. Avoid excessive loading of denervated muscles; recovery may take months to years and can be incomplete.',
    'Early corticosteroids are sometimes considered for acute pain, but controlled evidence for long-term neurologic recovery is limited. Do not promise that steroids or IVIG restore strength. Progressive or persistent focal deficits may require specialist imaging for constrictions and reconsideration of structural intervention in selected cases.')], ['NA','NAPNS','APPROACH'])

# Final editorial replacements keep alternatives clinically credible and remove
# giveaway qualifiers from the initial draft. Match by title to prevent drift.
def revise(title, *, stem=None, answer=None, others=None):
    matches = [r for r in rows if r['title'] == title]
    assert len(matches) == 1, title
    r = matches[0]
    if stem is not None: r['question'] = stem
    if answer is not None: r['answer'] = answer
    if others is not None: r['others'] = others

revise('Axonal Loss Versus Primary Demyelination',
 answer='Predominantly axonal polyneuropathy', others=[
 ('Acquired segmental demyelinating polyneuropathy', 'Acquired demyelination requires sufficiently marked timing abnormalities, block or dispersion in the appropriate pattern; mild slowing proportional to low amplitudes is less persuasive.'),
 ('Inherited uniform demyelinating polyneuropathy', 'CMT1A commonly produces relatively uniform substantial slowing with a compatible longstanding phenotype; the dominant amplitude loss described here instead favors axonal injury.'),
 ('Multifocal demyelinating motor neuropathy', 'MMN produces a compatible asymmetric motor syndrome with motor conduction block and sensory sparing; reduced sensory amplitudes and this generalized pattern argue against it.')])
revise('Technical Pitfalls in Apparent Demyelination', others=[
 ('Extend the study to additional motor nerves before repeating the affected segment', 'Sampling additional nerves can establish distribution, but does not correct the cold limb or unreliable stimulation in the segment currently being interpreted.'),
 ('Obtain CSF protein and cell count before revisiting the waveform', 'CSF is useful in selected inflammatory-neuropathy evaluations, but cannot validate a technically uncertain block; basic recording problems should first be corrected.'),
 ('Obtain nerve ultrasound to assess focal enlargement before repeating the recording', 'Ultrasound can reveal entrapment or enlargement, but is complementary and does not replace a technically valid conduction study when classifying apparent demyelination.')])
revise('Small-Fiber Neuropathy with Normal Nerve Conduction', others=[
 ('Quantitative thermal sensory threshold testing', 'Thermal thresholds assess small-fiber function but depend on cooperation and central processing; they do not directly quantify structural intraepidermal nerve loss.'),
 ('Quantitative sudomotor axon reflex testing', 'QSART evaluates postganglionic sudomotor function and can support autonomic small-fiber involvement; it is a functional test rather than a measure of cutaneous fiber density.'),
 ('Sural nerve biopsy with myelinated fiber morphometry', 'Selected nerve biopsy can investigate vasculitis, amyloid or other pathology, but is invasive and not the preferred direct structural test for this pure cutaneous small-fiber presentation.')])
revise('Testing a Peripheral Autonomic Syndrome', others=[
 ('Head-up tilt with beat-to-beat blood-pressure monitoring alone', 'Tilt testing helps characterize orthostatic hemodynamics but does not fully evaluate cardiovagal and sudomotor domains in this multisystem presentation.'),
 ('Heart-rate variability during deep breathing alone', 'Deep breathing assesses cardiovagal reflex function, but does not characterize adrenergic blood-pressure control or postganglionic sudomotor function.'),
 ('Quantitative sudomotor axon reflex testing alone', 'QSART assesses a relevant sudomotor domain; the orthostatic and other symptoms require a broader battery rather than sweat testing alone.')])
revise('High-Yield Laboratory Screening for DSP', others=[
 ('ANA, ANCA, complement and cryoglobulins', 'These are valuable when vasculitic or connective-tissue features are present, but have lower first-line yield than glucose, B12/metabolites and immunofixation in otherwise unexplained typical DSP.'),
 ('HIV serology, hepatitis C serology and region-directed Lyme testing', 'Infectious testing is selected by exposure, geography and phenotype; this is not the high-yield core group specified by the cited DSP practice parameter.'),
 ('Urinary porphyrin precursors, lead and arsenic assays', 'These investigate compatible toxic or porphyric presentations, especially with exposure or systemic clues, rather than forming the recommended core screen for typical unexplained DSP.')])
revise('CSF in the First Week of GBS',
 stem='Which CSF result on day four is compatible with typical GBS and is least concerning for an alternative inflammatory or infectious diagnosis?',
 answer='Protein within the laboratory reference range; 2 leukocytes/µL', others=[
 ('Protein within the laboratory reference range; 120 leukocytes/µL', 'A normal protein can occur early, but marked pleocytosis is atypical and requires investigation for infectious, inflammatory or malignant mimics.'),
 ('Elevated protein; 90 leukocytes/µL with neutrophil predominance', 'Raised protein does not compensate for substantial neutrophilic pleocytosis; infection and other alternative diagnoses need urgent contextual evaluation.'),
 ('Elevated protein; 150 leukocytes/µL with low CSF glucose', 'Low glucose with marked pleocytosis suggests processes such as infection or meningeal malignancy rather than uncomplicated albuminocytological dissociation.')])
revise('Axonal GBS and Reversible Conduction Failure', others=[
 ('Segmental demyelination with remyelinating recovery in AIDP', 'AIDP can produce block, but recovery without development of temporal dispersion in a pure motor pattern raises reversible nodal failure rather than simply assuming segmental demyelination.'),
 ('Motor and sensory axonal degeneration in AMSAN', 'AMSAN includes sensory involvement and axonal degeneration generally recovers through slower repair; preserved SNAPs and rapidly reversible motor failure favor an AMAN-spectrum nodal process.'),
 ('Fixed distal motor axonal degeneration in AMAN', 'AMAN can cause irreversible axonal degeneration, but resolution of apparent block without dispersion points to a reversible functional component rather than established fixed axon loss alone.')])
revise('Miller Fisher Syndrome', others=[
 ('Anti-GM1 IgG', 'GM1 antibodies are associated with selected motor axonal GBS phenotypes; GQ1b is the more characteristic association for acute ophthalmoplegia, ataxia and areflexia.'),
 ('Anti-GT1a IgG', 'GT1a antibodies are associated especially with pharyngeal-cervical-brachial disease and can cross-react with GQ1b; the classic Miller Fisher phenotype is most specifically linked to GQ1b.'),
 ('Anti-MAG IgM', 'MAG antibodies occur with a chronic distal demyelinating sensory-ataxic paraproteinemic neuropathy, rather than this acute ophthalmoplegic postinfectious syndrome.')])
revise('Respiratory Failure Despite Normal Oxygen Saturation', others=[
 ('Provide low-flow oxygen and repeat respiratory mechanics after the next routine ward round', 'Oxygen can treat hypoxemia but not neuromuscular hypoventilation or secretion failure; the described progression requires urgent monitored respiratory assessment.'),
 ('Use a trial of noninvasive ventilation on the ward as the initial airway strategy', 'Noninvasive support can help selected respiratory disorders, but severe bulbar dysfunction and weak secretion clearance in progressive GBS make delayed definitive airway planning hazardous.'),
 ('Transfer for monitoring but use serial pulse oximetry as the main trigger for intubation', 'Transfer is appropriate, but oxygen saturation can remain reassuring despite declining ventilatory reserve; mechanics, trajectory and airway protection must guide timing.')])
revise('Severe GBS Dysautonomia', others=[
 ('Start a scheduled long-acting antihypertensive to suppress the BP peaks', 'Fixed sustained BP lowering may be appropriate in stable chronic hypertension, but alternating severe hypotension makes overshoot a concern in acute GBS dysautonomia.'),
 ('Give a beta-blocker to control tachycardic periods and reassess bradycardia afterward', 'Rate control can be appropriate in selected sustained tachyarrhythmias, but intermittent profound vagal bradycardia requires close monitoring and makes empiric beta-blockade a poor default.'),
 ('Use intermittent ward ECG and treat symptomatic bradycardia when it recurs', 'Intermittent checks may suit stable patients, but can miss sudden severe arrhythmia in this unstable autonomic presentation; continuous monitored care is needed.')])
revise('Choosing Initial GBS Immunotherapy',
 answer='IVIG 0.4 g/kg/day for five days or plasma exchange over an appropriate four-to-five-exchange course', others=[
 ('IVIG 0.4 g/kg/day for five days followed immediately by a scheduled plasma-exchange course', 'Each modality is established individually, but routine sequential treatment adds no established benefit; exchange after IVIG can also remove administered immunoglobulin.'),
 ('Oral prednisolone induction followed by a response-guided taper', 'A steroid-based strategy is a legitimate option in typical CIDP, but trial evidence does not establish it as disease-modifying treatment for GBS.'),
 ('Subcutaneous immunoglobulin maintenance dosing as initial induction', 'SCIG is useful for maintenance in appropriately stabilized CIDP, but is not an established substitute for the acute IVIG or exchange regimen in disabling GBS.')])
revise('Poor Prognosis Alone Is Not an Indication for Repeat IVIG',
 answer='Continue supportive care with serial reassessment of trajectory and complications', others=[
 ('Give a second full IVIG course based on the poor prognostic score', 'This is the strategy tested by SID-GBS without demonstrated benefit and with more serious adverse events; poor prognosis alone is not a retreatment indication.'),
 ('Start plasma exchange immediately as a scheduled rescue after the IVIG course', 'Exchange is an established initial option, but routine early switching after IVIG for poor prognosis has no established added benefit and may remove infused immunoglobulin.'),
 ('Begin corticosteroid induction followed by maintenance for presumed ongoing inflammation', 'Maintenance steroids can be appropriate after a substantiated CIDP diagnosis, but severe early GBS with slow recovery does not establish that chronic inflammatory disorder.')])
revise('Treatment-Related Fluctuation Versus Acute-Onset CIDP', others=[
 ('A GBS treatment-related fluctuation within the usual acute window', 'An early improvement-then-worsening episode can be GBS-TRF; renewed deterioration after eight weeks instead particularly raises acute-onset CIDP.'),
 ('A new recurrent GBS episode after complete recovery', 'Recurrent GBS involves a distinct new episode after an appropriate interval and recovery context; continuing fluctuations in this early longitudinal course more strongly suggest acute-onset CIDP.'),
 ('Critical illness polyneuropathy as the primary longitudinal explanation', 'Critical illness can cause additional weakness in a suitable ICU/sepsis context, but that context is not supplied and does not account as directly for the described treatment-associated recurrent course.')])

revise('Why CIDP Treatment Cannot Simply Be Copied to GBS',
 stem='Which approach lacks an established routine disease-modifying role in typical GBS under EAN/PNS 2023 guidance?',
 answer='Corticosteroid induction', others=[
 ('A standard five-day IVIG course', 'IVIG is established for appropriately selected disabling GBS, particularly within the guideline-supported early treatment window; it differs from corticosteroid therapy in its evidence base.'),
 ('A standard plasma-exchange course', 'Exchange is an established acute GBS option when indicated and feasible; it is not necessary to add steroids to make this treatment effective.'),
 ('A choice between IVIG and exchange guided by patient factors', 'Selecting one established therapy according to renal, thrombotic, access and hemodynamic considerations is appropriate; the two options are not routinely combined.')])
revise('Typical CIDP: Distribution and Duration', others=[
 ('Length-dependent axonal polyneuropathy', 'Axonal DSP more commonly emphasizes distal sensory loss and later distal weakness; substantial proximal and distal motor disease over months warrants evaluation for CIDP.'),
 ('Hereditary demyelinating neuropathy', 'Inherited disease can cause slowing and areflexia, but often has a longstanding distal phenotype, deformity or pedigree rather than the supplied acquired proximal-distal course.'),
 ('Multifocal motor neuropathy', 'MMN typically produces asymmetric named-nerve motor deficits with sensory sparing, rather than symmetric proximal-distal sensorimotor involvement.')])
revise('Key EAN/PNS 2021 Demyelinating Thresholds',
 stem='For the motor conduction-velocity criterion in EAN/PNS 2021 CIDP guidance, what reduction below the lower limit of normal is required in at least two eligible nerves?',
 answer='At least 30%', others=[
 ('At least 10%', 'This degree of slowing can occur with axonal loss or technical factors and does not reach the guideline motor velocity criterion, even when more than one nerve is measured.'),
 ('At least 20%', 'Twenty percent is relevant to selected F-wave latency rules above the upper limit, not the required reduction in motor conduction velocity below its lower limit.'),
 ('At least 50%', 'Fifty percent appears in distal latency and amplitude-qualified F-wave rules; requiring this much velocity reduction would miss patients who meet the actual velocity criterion.')])
revise('CSF Protein Does Not Diagnose CIDP',
 answer='Review phenotype and conduction quality before assigning immune demyelination', others=[
 ('Begin an IVIG trial and use change in fatigue as the principal diagnostic endpoint', 'An objective monitored treatment trial can support a defined possible-CIDP pathway, but fatigue alone is nonspecific and insufficient with this discordant axonal phenotype.'),
 ('Use proximal nerve enlargement on ultrasound as a replacement for motor conduction evidence', 'Ultrasound can provide supportive data in selected uncertain cases, but does not independently establish CIDP or negate a discordant clinical/electrophysiological pattern.'),
 ('Perform sural biopsy as the next routine confirmation of CIDP', 'Biopsy has a selected role for uncertainty or suspected mimics, but its limitations and morbidity make it unsuitable as routine confirmation of an isolated mild protein increase.')])
revise('Multifocal CIDP Versus MMN', others=[
 ('Multifocal motor neuropathy', 'MMN is an important competing acquired multifocal disorder, but objective sensory loss in affected nerve distributions argues for a sensorimotor process such as multifocal CIDP.'),
 ('Distal CIDP', 'Distal CIDP emphasizes distal weakness and sensory loss with a different distribution; patchy asymmetric involvement of several named upper-limb nerves more specifically suggests multifocal CIDP.'),
 ('Sensory-predominant CIDP', 'Sensory-predominant CIDP emphasizes sensory impairment with its own clinical framework; substantial asymmetric motor deficits make multifocal sensorimotor disease the better fit.')])
revise('Initial Treatment of Typical CIDP', others=[
 ('SCIG maintenance dosing as the standard initial induction strategy', 'SCIG is established for maintenance in stabilized immunoglobulin-responsive CIDP; IVIG or corticosteroids are the recommended usual induction options.'),
 ('Azathioprine monotherapy as the preferred rapid induction strategy', 'A steroid-sparing immunosuppressant may be considered in selected long-term management, but lacks the established rapid induction role of the recommended first-line options.'),
 ('Rituximab as the preferred induction for antibody-unselected typical CIDP', 'B-cell-directed therapy may be considered in selected refractory or antibody-defined disorders; it does not replace the guideline first-line options for routine typical CIDP.')])
revise('Individualizing Immunoglobulin Maintenance', others=[
 ('Continue the present full dose indefinitely because remission cannot be assessed clinically', 'An effective dose may need continuation if reduction causes objective relapse, but the guideline supports periodic assessment for lower requirements or remission in stable patients.'),
 ('Stop immunoglobulin immediately and assess only if marked weakness recurs', 'A supervised withdrawal can be appropriate in selected stable patients, but needs agreed objective monitoring and a rescue plan rather than waiting for substantial disability.'),
 ('Replace IVIG with chronic corticosteroids before attempting any immunoglobulin reduction', 'Steroids are useful in CIDP, but an automatic switch adds different toxicity and is not necessary merely to test dependence in a stable IVIG responder.')])
revise('FcRn Blockade and the ADHERE Population',
 answer='FcRn blockade; relapse prevention tested in a responder-enriched randomized-withdrawal phase', others=[
 ('CD20 blockade; relapse prevention tested in a responder-enriched randomized-withdrawal phase', 'CD20 depletion describes agents such as rituximab, whereas efgartigimod blocks FcRn-mediated IgG recycling; the ADHERE design does not change that mechanism.'),
 ('FcRn blockade; superiority to IVIG tested in a head-to-head induction trial', 'The mechanism is correct, but ADHERE randomized initial responders to continued treatment or placebo withdrawal rather than directly comparing IVIG induction.'),
 ('Complement C5 blockade; superiority to IVIG tested in a head-to-head induction trial', 'C5 inhibition is a different immune strategy, and the stated active-comparator design does not describe ADHERE; neither part identifies this CIDP evidence correctly.')])
revise('Autoimmune Nodopathy Is Not Conventional CIDP',
 answer='Autoimmune nodopathy', others=[
 ('Typical CIDP', 'The phenotype can resemble CIDP, but a validated NF155-associated syndrome is categorized as autoimmune nodopathy in the 2021 framework, with distinct treatment-response implications.'),
 ('IgM anti-MAG neuropathy', 'Anti-MAG disease may cause tremor and sensory ataxia, but typically has a chronic distal IgM-associated pattern and a different antigen association from confirmed IgG4 NF155 disease.'),
 ('POEMS neuropathy', 'POEMS can be severe and demyelinating, but requires a plasma-cell disorder and the defined additional criteria; this antibody and phenotype instead support nodopathy.')])
revise('Multifocal Motor Neuropathy', others=[
 ('Lower-motor-neuron-predominant motor neuron disease', 'Motor neuron disease can cause asymmetric motor deficits without sensory loss, but convincing non-entrapment motor block supports MMN and warrants evaluation for a treatable immune neuropathy.'),
 ('Multifocal CIDP', 'Multifocal CIDP is a close acquired demyelinating alternative, but usually has objective sensory involvement; a pure motor named-nerve pattern favors MMN.'),
 ('Motor-predominant CIDP', 'Motor CIDP can spare clinical sensation, but often has a more generalized pattern; asymmetric distal named-nerve weakness with block is particularly characteristic of MMN.')])
revise('Diabetes Does Not Explain Every Neuropathy',
 answer='Evaluate for superimposed CIDP using the full clinical and electrodiagnostic framework', others=[
 ('Classify the progression as diabetic distal symmetric polyneuropathy', 'Typical diabetic DSP can cause slowing and distal weakness, but rapid substantial proximal-distal progression with qualifying non-entrapment demyelination requires another explanation.'),
 ('Classify the progression as diabetic lumbosacral radiculoplexus neuropathy', 'Radiculoplexus disease often starts with severe asymmetric hip/thigh pain and patchy axonal weakness; the supplied generalized demyelinating pattern suggests a different superimposed process.'),
 ('Classify the progression as treatment-induced neuropathy of diabetes', 'Treatment-induced disease follows rapid glycemic improvement and emphasizes acute pain/autonomic symptoms; that temporal context is absent and marked demyelinating motor progression is discordant.')])
revise('B12 Myeloneuropathy and Functional Markers',
 stem='A metformin-treated patient has paresthesias, loss of position sense, absent ankle reflexes and extensor plantar responses. B12 is indeterminate and renal function is normal. Which biochemical test most specifically supports functional B12 deficiency?', others=[
 ('Plasma homocysteine', 'Homocysteine can rise with B12 deficiency but also folate deficiency and other factors, making it less specific than MMA in the stated normal renal context.'),
 ('Serum folate', 'Folate measurement addresses a related nutritional deficiency, but does not confirm intracellular B12 dysfunction and cannot explain away this possible myeloneuropathy.'),
 ('Repeat full blood count and mean corpuscular volume', 'Macrocytosis can support a megaloblastic process, but neurological B12 deficiency may occur without anemia or an elevated MCV; a normal count cannot resolve the indeterminate B12 result.')])
revise('Pyridoxine Excess',
 answer='Vitamin B6 exposure', others=[
 ('Vitamin B12 exposure', 'B12 deficiency can cause ataxic myeloneuropathy and is worth evaluating, but ordinary B12 supplementation is not the characteristic supplement-associated sensory neurotoxicity in this setting.'),
 ('Thiamine exposure', 'Thiamine deficiency can produce neuropathy in malnutrition, but supplemental thiamine is not the usual explanation for a dose-related sensory toxic syndrome from stacked preparations.'),
 ('Vitamin E exposure', 'Vitamin E deficiency can cause ataxia and neuropathy in a suitable malabsorptive or genetic context; the exposure concern with overlapping multivitamin and magnesium products is especially B6.')])
revise('Chemotherapy-Induced Sensory Neuropathy',
 stem='During oxaliplatin treatment, cold-triggered dysesthesias evolve into persistent distal numbness that impairs fastening buttons and causes near-falls. What is the best next management step?',
 answer='Review neurotoxicity severity with oncology and consider a dose delay, reduction, substitution or cessation', others=[
 ('Add duloxetine and continue the current oxaliplatin schedule without a toxicity review', 'Duloxetine has evidence for painful established CIPN, but analgesia does not address progressive functional impairment or determine whether neurotoxic exposure should continue unchanged.'),
 ('Continue the current schedule and reassess only after chemotherapy completion', 'Monitoring may suffice for mild transient symptoms, but progressive functional loss warrants timely oncology review rather than waiting until cumulative injury is complete.'),
 ('Start IVIG for presumed chemotherapy-triggered CIDP', 'Immune neuropathy may occur in specific contexts, but this characteristic cumulative oxaliplatin sensory syndrome does not establish acquired demyelination or justify IVIG.')])
revise('Neuropathy in Advanced Kidney Disease',
 answer='Uremic distal sensorimotor polyneuropathy', others=[
 ('Typical CIDP', 'CIDP requires a compatible proximal-distal clinical pattern and qualifying demyelination; advanced renal disease with this predominantly axonal distal pattern does not establish it.'),
 ('Dialysis-related amyloid carpal tunnel syndrome', 'Dialysis-associated amyloid can cause focal median compression, but that does not explain the generalized length-dependent motor-sensory axonal pattern.'),
 ('Renal osteodystrophy-associated proximal myopathy', 'Renal bone/mineral disorders can contribute to proximal muscle dysfunction, but do not sufficiently explain distal sensory loss, areflexia and axonal nerve abnormalities.')])
revise('Alcohol-Associated Neuropathy',
 answer='Supported alcohol cessation, nutritional assessment and replacement, rehabilitation and symptom care', others=[
 ('Thiamine replacement and pain treatment as the complete plan', 'Thiamine is important when deficiency is suspected, but a plan omitting alcohol treatment, broader nutritional assessment and functional protection leaves major contributors unaddressed.'),
 ('IVIG induction followed by strength-guided maintenance', 'This is appropriate for selected immune neuropathies, but exposure-associated length-dependent axonal disease needs etiologic assessment rather than automatic immunotherapy.'),
 ('Neuropathic analgesia with reassurance that no additional etiologic assessment is needed', 'Analgesia is useful, but diabetes, B12 deficiency, paraproteins and other causes may coexist; a known alcohol exposure should not close the diagnostic evaluation.')])

revise('POEMS Diagnostic Requirements',
 stem='In a patient with polyneuropathy and a monoclonal plasma-cell disorder, which additional combination satisfies the standard POEMS framework?',
 answer='At least one other major criterion and at least one minor criterion', others=[
 ('At least two minor criteria without another major criterion', 'Multiple minor manifestations can raise suspicion, but the standard framework still requires another major criterion such as a sclerotic lesion, Castleman disease or elevated VEGF.'),
 ('At least one other major criterion without a minor criterion', 'Another major finding strengthens the diagnosis, but the standard combination also requires at least one qualifying minor manifestation.'),
 ('At least three minor criteria, with or without another major criterion', 'Counting minor findings cannot replace the defined major requirement; the framework is categorical rather than an interchangeable total-points score.')])
revise('Treatable Adult Refsum Disease', others=[
 ('Restrict dietary phytanic acid while using rapid weight reduction to lower total body stores', 'Reducing dietary exposure is correct, but rapid weight loss mobilizes stored phytanic acid and can worsen disease; energy adequacy and avoidance of catabolism are essential.'),
 ('Use repeated plasma exchange alone as long-term treatment with an unrestricted diet', 'Exchange can be important in acute metabolic deterioration, but cannot replace sustained dietary control and adequate nutrition in long-term management.'),
 ('Use dietary restriction alone and allow fasting during intercurrent illness', 'Restriction is a foundation of care, but illness-associated catabolism and fasting can mobilize phytanic acid; an individualized emergency nutrition plan is needed.')])
revise('Protecting Gait in Fibular Compression Palsy', others=[
 ('Provide an ankle-foot orthosis and schedule immediate decompression', 'An orthosis is appropriate, but stable posture-related palsy without a structural lesion or deterioration does not automatically require immediate decompression; follow trajectory and severity.'),
 ('Provide gait training and defer orthotic support until recovery has plateaued', 'Training is useful, but an orthosis can immediately improve toe clearance and reduce falls while recovery is evolving; waiting for plateau leaves avoidable functional risk.'),
 ('Provide a corticosteroid course and reassess before arranging rehabilitation', 'Steroids are used for selected inflammatory disorders, but evidence does not establish them as the primary treatment for uncomplicated mechanical fibular compression; pressure relief and functional support should begin promptly.')])

def highlight_values(value):
    if isinstance(value, str):
        parts = re.split(r'(==.*?==)', value)
        pattern = r'(?<![\w.])(?:\d+(?:\.\d+)?(?:[–-]\d+(?:\.\d+)?)?\s*(?:g/kg(?:/day)?|mg/day|mg/kg|mL/kg|cells/µL|mmHg|%))'
        return ''.join(p if p.startswith('==') else re.sub(pattern, lambda m: '=='+m.group(0)+'==', p) for p in parts)
    if isinstance(value, (list, tuple)):
        return type(value)(highlight_values(v) for v in value)
    return value

for row in rows:
    row['sections'] = highlight_values(row['sections'])
    row['table'] = highlight_values(row['table'])

# Serialize only the completed chapter, never a partial draft.
if __name__ == '__main__':
    coverage = ROOT/'Neurology/09. Peripheral Neuropathies & Polyradiculoneuropathies.coverage.json'
    c = json.loads(coverage.read_text(encoding='utf-8'))
    assert len(rows) == sum(s['questions'] for s in c['sections']) == c['plannedQuestions'], 'Chapter incomplete; do not install'
    index = 0
    for section in c['sections']:
        assert len(section['decisions']) == section['questions']
        for decision in section['decisions']:
            assert rows[index]['topic'] == section['section']
            rows[index]['coverageDecision'] = decision
            index += 1
    save('Neurology',9,c['chapter'],rows,R,'Original postgraduate educational synthesis with mapped decisions. Source versions, drug-label jurisdictions and evidence limits are stated. Full Harrison subscription text was not accessed; no independent clinician review is claimed.')
    c.update(status='authored_validated',authoredQuestions=len(rows))
    c['questionDecisions'] = [dict(question=i+1,title=r['title'],decision=r['coverageDecision']) for i,r in enumerate(rows)]
    coverage.write_text(json.dumps(c,ensure_ascii=False,indent=2),encoding='utf-8')
