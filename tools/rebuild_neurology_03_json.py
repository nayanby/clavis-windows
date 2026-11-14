"""Original chapter 3, using current ILAE terminology and explicit treatment context."""
from qbank_json_chapters import question as Q, save
R={
 'DEF':('ILAE practical clinical definition of epilepsy, 2014','https://www.ilae.org/guidelines/definition-and-classification/the-2014-definition-of-epilepsy-a-perspective-for-patients-and-caregivers'),
 'CLASS':('ILAE updated classification of epileptic seizures, 2025','https://www.ilae.org/guidelines/definition-and-classification/updated-classification-of-epileptic-seizures-2025'),
 'DX':('NICE NG217: Diagnosis and assessment of epilepsy','https://www.nice.org.uk/guidance/ng217/chapter/diagnosis-and-assessment-of-epilepsy'),
 'TX':('NICE NG217: Treating epileptic seizures','https://www.nice.org.uk/guidance/ng217/chapter/treating-epileptic-seizures-in-children-young-people-and-adults'),
 'TEMP':('ILAE EpilepsyDiagnosis: Temporal lobe seizures','https://www.epilepsydiagnosis.org/seizure/temporal-overview'),
 'JME':('ILAE EpilepsyDiagnosis: Juvenile myoclonic epilepsy EEG','https://www.epilepsydiagnosis.org/syndrome/jme-eeg'),
 'FIRST':('AAN/AES: Management of an unprovoked first seizure in adults, 2015','https://www.aan.com/Guidelines/Home/GetGuidelineContent/688'),
 'PREG':('AAN/AES/SMFM pregnancy guidance, 2024: official summary','https://www.aan.com/PressRoom/Home/PressRelease/5170'),
 'DRUG':('US Department of Veterans Affairs: Antiseizure Medication Counseling Desk Guide, July 2025','https://www.epilepsy.va.gov/EPILEPSY/Library/PDFs/ECoE_Antiseizure_Medication_Desk_Guide_July2025.pdf'),
 'DRE':('ILAE: Drug-resistant epilepsy and consensus definition','https://www.ilae.org/patient-care/drug-resistant-epilepsy/drug-resistant-epilepsy'),
 'SE':('ILAE definition and classification of status epilepticus, 2015','https://doi.org/10.1111/epi.13121'),
 'ENLS':('Neurocritical Care Society: ENLS Status Epilepticus Protocol, version 6.0','https://www.neurocriticalcare.org/Portals/0/ENLS%205.0/ENLS%206.0/Protocol%20V6_0%20Status%20Epilepticus.pdf'),
 'ESETT':('ESETT randomized trial: age-group analysis and treatment regimens, Lancet 2020','https://pmc.ncbi.nlm.nih.gov/articles/PMC7241415/'),
}
def S(h,main,*children):return(h,[(main,list(children))])
rows=[]
def add(*a,**kw):rows.append(Q(*a,**kw))

add('Definitions and classification','Epilepsy After One Unprovoked Seizure',
 'After one unprovoked seizure, a patient has an established epileptogenic condition with a reliably estimated 10-year recurrence probability of 70%. Which statement best fits the ILAE clinical definition?',
 'Epilepsy can be diagnosed without waiting for a second unprovoked seizure',[
 ('Two unprovoked seizures are required regardless of recurrence probability','Two events more than 24 hours apart remain one diagnostic route, but ILAE also permits one event with a sufficiently high recurrence probability or a defined epilepsy syndrome.'),
 ('A recurrence probability of 70% is insufficient unless both events occur within one week','The high-risk single-seizure route concerns at least 60% over 10 years; it does not require a second event or a one-week interval.'),
 ('A normal routine EEG would negate the high-risk diagnosis','Routine EEG has limited sensitivity. A normal sample does not overrule a reliable causal diagnosis and sufficiently high recurrence estimate.')],
 [S('Clinical Definition','**Epilepsy** may be diagnosed after two unprovoked or reflex seizures more than 24 hours apart, one such seizure with a recurrence risk ==at least 60% over 10 years==, or an epilepsy syndrome.',
    'The single-seizure risk must be supported rather than assumed. A nonspecific imaging abnormality or one risk factor does not automatically demonstrate that the threshold is exceeded.',
    'Acute symptomatic seizures from a transient metabolic or acute cerebral insult are assessed separately from enduring unprovoked-seizure predisposition.'),
  S('Diagnosis and Treatment Are Separate','**Meeting the definition** supports a disease diagnosis but still requires individualized treatment and counseling.',
    'Consider the type and consequences of possible recurrence, medication adverse effects, comorbidities and patient preferences. Explain that diagnostic confidence and exact numerical risk estimation have limits.',
    'Driving advice follows local regulations; also discuss bathing, swimming, heights and seizure first aid. A negative routine EEG does not by itself establish freedom from future risk.')],['DEF','DX'])

add('Definitions and classification','Acute Symptomatic Metabolic Seizure',
 'A patient without previous seizures convulses while serum sodium is 108 mmol/L after acute water intoxication. Imaging is normal and there are no further seizures after monitored correction. How should the event be classified initially?',
 'Acute symptomatic seizure',[
 ('Established generalized epilepsy','A convulsion during a severe acute metabolic derangement does not by itself establish an enduring epilepsy predisposition or a generalized epilepsy syndrome.'),
 ('Drug-resistant epilepsy','Drug resistance requires persistent seizures despite adequate appropriately selected medication trials; no such treatment history or chronic epilepsy is present.'),
 ('Reflex epilepsy','Reflex seizures recur with a specific stimulus such as flickering light or reading, rather than simply occurring during profound acute systemic electrolyte disturbance.')],
 [S('Provoked Versus Unprovoked','**Severe acute hyponatremia** is a plausible proximate cause of an acute symptomatic seizure.',
    'Identify the temporal relationship and exclude additional contributors such as CNS infection, medication toxicity or an acute structural lesion. The word “provoked” should not be applied merely because sleep deprivation occurred; sleep loss alone does not define an acute symptomatic metabolic seizure.',
    'A single acute symptomatic event is not counted as an unprovoked event for the usual two-seizure epilepsy definition.'),
  S('Immediate and Longer-Term Care','**Treat the cause and stop ongoing seizures**, using an appropriate emergency hyponatremia protocol when symptomatic.',
    'Monitor sodium closely and avoid excessive correction because osmotic demyelination risk can follow overcorrection. A rapidly reversing cause and absence of ongoing risk often argue against indefinite antiseizure therapy.',
    'Long-term treatment is individualized if later unprovoked seizures occur, an epileptogenic lesion is found or EEG and clinical findings reveal an independent epilepsy syndrome.')],['DEF','DX'])

add('Definitions and classification','Resolved Epilepsy',
 'Apart from an age-dependent syndrome that has been outgrown, which seizure-free and medication-free combination meets the ILAE operational description of resolved epilepsy?',
 'Seizure-free for 10 years, with no antiseizure medication for the last 5 years',[
 ('Seizure-free for 2 years while continuing medication','Two years can prompt an individualized withdrawal discussion in some patients, but is not the ILAE criterion for resolved epilepsy.'),
 ('Seizure-free for 5 years, with no medication for the last 2 years','This is a substantial remission but does not reach the operational 10-year seizure-free and 5-year medication-free intervals.'),
 ('Seizure-free for 10 years while still taking medication','The usual operational route also requires the most recent 5 years off treatment; controlled epilepsy on medication is not identical to resolved epilepsy.')],
 [S('Operational Meaning','**Resolved epilepsy** is a defined status, not proof that recurrence risk is zero.',
    'ILAE uses ==10 years without seizures and at least the last 5 years without antiseizure medication==, or an age-dependent syndrome in a person now beyond its applicable age.',
    'The term differs from a short remission, successful pharmacological control and a decision that medication withdrawal may be attempted.'),
  S('Withdrawal Counseling','**Stopping medication** requires a separate individualized discussion rather than waiting for a resolved label.',
    'Review seizure type, syndrome, structural lesions, EEG, prior withdrawal attempts, consequences of recurrence and patient priorities. Some syndromes, such as juvenile myoclonic epilepsy, have a substantial relapse tendency after withdrawal.',
    'Taper according to the drug and clinical context, avoiding abrupt cessation especially of benzodiazepines and barbiturates. Explain local driving restrictions during and after withdrawal and what to do if seizures recur.')],['DEF','DX'],style='direct')

add('Definitions and classification','ILAE Seizure Classification Update',
 'Which terminology change specifically belongs to the ILAE 2025 seizure classification rather than the 2017 operational framework?',
 'Use of consciousness, assessed through awareness and responsiveness, as a classifier',[
 ('Introduction of focal aware and focal impaired awareness as the preferred new 2025 labels','Those awareness-based labels belong to the 2017 framework; the 2025 revision uses consciousness assessed through awareness and responsiveness.'),
 ('Division of all seizures solely into motor and nonmotor types','The 2025 revision replaces that dichotomy with observable versus nonobservable manifestations in relevant parts of the classification; it does not make motor status the sole biological class.'),
 ('Removal of an unknown category so every seizure must be assigned focal or generalized','The updated system retains unknown whether focal or generalized, and unclassified; it explicitly allows uncertainty rather than forcing unsupported localization.')],
 [S('Current Framework','**ILAE 2025** retains focal, generalized, unknown whether focal or generalized, and unclassified main classes.',
    'It removes “onset” from the main class names and uses consciousness, incorporating both recall and responsiveness, instead of awareness alone. Historical records and some current guidelines still use 2017 terms.',
    'Chronological description of manifestations is emphasized. Observable manifestations are not limited to convulsive movements; behavioral arrest and impaired consciousness can also be observable.'),
  S('Practical Application','**Assess what was actually observed** rather than infer consciousness from open eyes or attempted interaction.',
    'Ask witnesses about appropriate responses and ask the patient about recall. Aphasia, motor inability and isolated amnesia can complicate interpretation and should be considered before calling a response failure global impaired consciousness.',
    'If the evidence cannot distinguish focal from generalized, retain the appropriate uncertainty category and seek video, EEG and imaging; classification can change as information improves.')],['CLASS'],style='direct')

add('Semiology and localization','Mesial Temporal Seizure Semiology',
 'A stereotyped episode starts with a rising epigastric sensation and déjà vu, then behavioral arrest and oral automatisms, followed by several minutes of confusion. Which origin is most likely?',
 'Mesial temporal network',[
 ('Occipital visual cortex','Brief elementary visual phenomena in a hemifield more strongly suggest occipital onset; the autonomic-experiential sequence here is more characteristic of mesial temporal involvement.'),
 ('Primary somatosensory cortex','A focal tingling or somatic sensory march would favor parietal onset; it does not best explain this recurrent epigastric–experiential pattern.'),
 ('Lateral temporal auditory cortex','Auditory sounds or distortions are more suggestive of lateral temporal involvement. Spread can produce overlap, but the initial experiential-autonomic symptoms favor mesial networks.')],
 [S('Clinical Sequence','**Mesial temporal seizures** often begin with autonomic, emotional or experiential symptoms before impaired consciousness and automatisms.',
    'A rising epigastric sensation, fear or déjà vu is supportive rather than perfectly specific. A prolonged postictal confusional period is more typical than the abrupt recovery of a brief typical absence.',
    'The initial remembered symptom may reflect propagation rather than the exact microscopic onset, so semiology alone does not establish an operation target.'),
  S('Evaluation and Comparison','**Video-EEG and epilepsy-protocol MRI** integrate semiology with electrical and structural data.',
    'Look for hippocampal sclerosis or another temporal lesion, but recognize that MRI may be normal. Record duration, stereotypy, responsiveness, laterality and the complete chronological sequence.',
    'Insular and frontal seizures can mimic temporal events, particularly after spread. Drug-resistant focal epilepsy warrants specialist presurgical assessment rather than endlessly repeating similar medication trials.')],['TEMP','DX'],table=(['Origin','Common early manifestation'],[
 ['Mesial temporal','Epigastric rising, fear, déjà vu'],['Lateral temporal','Auditory sounds or distortion'],['Frontal','Brief tonic, asymmetric or hypermotor behavior; often nocturnal'],
 ['Parietal','Somatosensory symptoms or body-schema disturbance'],['Occipital','Brief elementary visual phenomena'],['Insular','Throat/laryngeal discomfort, unpleasant somatosensory or autonomic symptoms']]))

add('Semiology and localization','Sleep-Related Hypermotor Epilepsy',
 'An adult has clusters of 20-second stereotyped nocturnal episodes with abrupt asymmetric tonic posturing and hypermotor movements, followed by rapid recovery. Routine scalp EEG is normal. Which diagnosis is favored?',
 'Sleep-related hypermotor epilepsy',[
 ('NREM disorder of arousal','Parasomnias can cause complex sleep behavior, but episodes are often longer, less stereotyped and less tightly clustered; repeated brief identical asymmetric attacks favor epilepsy.'),
 ('REM sleep behavior disorder','Dream enactment is generally linked to REM and may involve dream recall; the described very brief clustered tonic-hypermotor sequence is more typical of sleep-related focal seizures.'),
 ('Nocturnal panic attacks','Panic can wake a patient with autonomic distress, but recurrent highly stereotyped asymmetric motor posturing and very short clustered episodes favor an epileptic mechanism.')],
 [S('Pattern Recognition','**Brief, abrupt and stereotyped clusters** are important clues to sleep-related hypermotor epilepsy.',
    'Frontal networks are common, but temporal, insular or other extra-frontal onset can generate a hypermotor phenotype after propagation. The syndrome name therefore avoids assuming that all such seizures originate in the frontal lobe.',
    'A normal scalp EEG does not exclude focal seizures, especially with deep onset or prominent muscle artifact.'),
  S('Distinguishing Sleep Disorders','**Detailed witness history and home video** are useful before prolonged video-EEG or combined sleep evaluation.',
    'Ask about sleep-stage timing, clustering, duration, reproducibility, injuries, dream recall and childhood parasomnias. NREM parasomnias and epilepsy can coexist.',
    'An apparently dramatic motor episode should not be diagnosed as functional merely because an ictal scalp correlate is absent. Expert interpretation considers the event’s full semiology and the limitations of the recording.')],['DX','CLASS'])

add('Semiology and localization','Insular Seizure Mimicry',
 'A patient repeatedly experiences a sudden choking sensation with unpleasant throat constriction, hypersalivation and spreading painful paresthesia while initially able to report the symptoms. Which origin deserves particular consideration?',
 'Insular cortex',[
 ('Mesial temporal cortex','Autonomic symptoms and later impaired consciousness can resemble temporal seizures, but early laryngeal constriction and unpleasant somatosensory symptoms particularly suggest insular involvement.'),
 ('Occipital cortex','Elementary visual symptoms or a visual-field phenomenon would be more characteristic; the initial laryngeal and painful somatic sequence is not an occipital signature.'),
 ('Supplementary motor area','Brief asymmetric tonic posturing and preserved awareness can occur with SMA seizures, but the dominant laryngeal-viscerosensory onset is more suggestive of insular networks.')],
 [S('Insular Semiology','**Laryngeal discomfort and unpleasant somatic sensations** can occur early in insular seizures.',
    'Awareness or consciousness may initially be preserved. Subsequent spread into temporal or frontal networks can create automatisms, impaired responsiveness or hypermotor behavior, obscuring the origin.',
    'Symptoms are not pathognomonic: gastrointestinal, respiratory, panic and other seizure causes must be considered in context.'),
  S('Localization Limits','**The insula is deep**, so scalp EEG may appear temporal, frontal, diffuse or unrevealing.',
    'Use the chronological history, video-EEG, structural imaging and other concordant data. Selected drug-resistant cases may require stereo-EEG when noninvasive findings suggest a deep or misleadingly localized onset.',
    'Do not infer an insular focus solely from one throat symptom or proceed to invasive testing without a defined presurgical hypothesis. The value is recognizing a plausible temporal or frontal mimic.')],['TEMP','DX'])

add('Semiology and localization','Ictal Dystonic Posturing',
 'During a recorded temporal seizure, the left arm develops sustained dystonic posturing while the right hand shows manual automatisms. Which lateralizing interpretation is most appropriate?',
 'The dystonic arm supports a right hemispheric seizure origin',[
 ('The dystonic arm supports a left hemispheric seizure origin','Ictal upper-limb dystonia usually lateralizes contralaterally, so left dystonia supports right-sided involvement rather than an ipsilateral rule.'),
 ('The automatising hand proves a left hemispheric origin','Manual automatisms often occur ipsilaterally but are less reliable alone; the right automatism does not justify assigning a left origin against the dystonic sign.'),
 ('The combination proves simultaneous independent bilateral seizures','A unilateral seizure can recruit motor networks and produce this asymmetric combination; bilateral independent onset is not established by opposing hand behaviors.')],
 [S('Lateralizing Signs','**Unilateral ictal dystonia** often points to the contralateral hemisphere in temporal-lobe epilepsy.',
    'Ipsilateral manual automatisms may accompany it, making this combination supportive of a right temporal origin. The value is probabilistic, not absolute, because propagation and atypical anatomy can alter expression.',
    'Other useful signs include postictal paresis, postictal language dysfunction and a reliably documented early forced version, interpreted with timing and context.'),
  S('Integration for Surgery','**Concordance matters** more than any single bedside lateralizing sign.',
    'Compare ictal and interictal EEG, MRI, language and memory testing and, when indicated, functional or invasive studies. A late motor sign can reflect spread and may lateralize differently from the actual onset.',
    'Do not make a resection decision from the side of an automatism alone; define the epileptogenic zone and its relationship to essential cortex through a comprehensive presurgical assessment.')],['TEMP','DX'])

add('EEG and event differentiation','Typical Absence EEG',
 'A child has frequent brief behavioral arrests with abrupt recovery and no postictal confusion. Hyperventilation produces the habitual event. Which EEG pattern best supports typical absence seizures?',
 'Generalized approximately 3-Hz spike-and-wave discharges',[
 ('Generalized slow spike-and-wave below 2.5 Hz','This is associated with atypical absences and developmental epileptic encephalopathies such as Lennox–Gastaut, rather than the classic typical absence context.'),
 ('Unilateral anterior temporal rhythmic theta with gradual evolution','An evolving focal temporal ictal pattern supports a focal seizure, which often lasts longer and can have a more prominent postictal period.'),
 ('Generalized paroxysmal fast activity during non-REM sleep','This is a characteristic feature in Lennox–Gastaut syndrome and tonic seizures; it is not the usual EEG correlate of a brief typical absence.')],
 [S('Electroclinical Correlation','**Typical absences** produce abrupt lapses associated with generalized spike-and-wave, classically around ==3 Hz==.',
    'Hyperventilation can activate events and should be performed under an appropriate EEG protocol. Small automatisms may occur during an absence and do not automatically imply temporal-lobe epilepsy.',
    'Brief duration, high daily frequency, rapid recovery and the generalized EEG pattern help distinguish absence from focal impaired-consciousness seizures.'),
  S('Syndrome and Treatment','**Absence seizure type** is not itself the complete epilepsy syndrome.',
    'Assess age, development, myoclonus, generalized tonic-clonic seizures and background EEG. Ethosuximide is suitable for isolated absences; additional seizure types require a broader-spectrum strategy.',
    'Atypical absences often have less abrupt onset and offset, abnormal development or other seizure types, and slower generalized discharges. Treatment and prognosis differ, so the EEG frequency must be interpreted with the clinical setting.')],['TX','JME'])

add('EEG and event differentiation','Normal Routine EEG',
 'A patient has recurrent stereotyped focal sensory events followed by impaired responsiveness. A routine 20-minute EEG is normal. Which interpretation is best?',
 'The normal sample does not exclude epilepsy; further evaluation depends on clinical suspicion',[
 ('The events are established functional seizures','A normal interictal EEG does not diagnose functional seizures; that conclusion requires positive clinical evidence and appropriate evaluation of typical events.'),
 ('The events cannot arise from the cerebral cortex','Scalp EEG can miss small, deep or intermittent cortical discharges, and the absence of abnormalities during a short sample does not exclude a cortical seizure.'),
 ('A normal routine EEG excludes any need for epilepsy-protocol MRI','Structural assessment follows the clinical syndrome and indications, not the presence of interictal spikes alone; focal symptoms may warrant MRI despite a normal EEG.')],
 [S('Test Sensitivity','**Routine EEG is a sample**, often obtained between events, and has limited sensitivity for epilepsy.',
    'Interictal epileptiform discharges support classification and recurrence-risk assessment but must be distinguished from benign variants and artifact. A positive EEG does not replace a compatible event history either.',
    'NICE advises against using EEG to exclude epilepsy; when requested after a first seizure, early recording, ideally within 72 hours, may improve yield.'),
  S('Further Testing','**Sleep-deprived, ambulatory or video-EEG studies** can improve the chance of capturing relevant abnormalities.',
    'Select the study according to event frequency, safety, diagnostic uncertainty and whether a habitual event must be recorded. MRI evaluates structural causes independently of whether EEG is positive.',
    'Always review syncope, migraine, functional events and other mimics using the history, examination and appropriate cardiac or metabolic tests rather than treating EEG as a binary truth test.')],['DX'])

add('EEG and event differentiation','Functional Seizures and Video-EEG',
 'Repeated prolonged shaking episodes have variable asynchronous limb movements and fluctuating responsiveness. The patient also has a prior confirmed focal epilepsy diagnosis. What is the best strategy to establish the nature of the new habitual attacks?',
 'Capture representative habitual events on video-EEG with expert electroclinical interpretation',[
 ('Assume all attacks are epileptic because epilepsy was previously confirmed','Epileptic and functional seizures can coexist; a prior epilepsy diagnosis does not classify every later event or justify uncritical treatment escalation.'),
 ('Diagnose functional seizures from one normal interictal EEG','A normal between-event sample is common in epilepsy and does not establish the mechanism of the habitual attack.'),
 ('Use a single prolactin measurement to replace event recording','Prolactin has timing and seizure-type limitations and can be influenced by other events; it cannot reliably replace detailed electroclinical characterization.')],
 [S('Positive Diagnosis','**Functional seizures** should be diagnosed from a coherent positive electroclinical pattern, not simply exclusion or stigma.',
    'Video-EEG recording of a representative habitual event is the reference approach when available. The patient and witness should confirm that the captured episode matches the usual concerning attacks.',
    'Some genuine focal seizures have little or no scalp correlate. Interpretation must account for semiology, recording quality and the expected sensitivity for that suspected seizure type.'),
  S('Coexisting Conditions','**Dual diagnosis** requires distinguishing event types so medication is neither escalated unnecessarily nor withdrawn from untreated epilepsy.',
    'Explain the functional diagnosis clearly and respectfully and arrange appropriate psychological and neurological follow-up. The attacks are involuntary symptoms, not evidence that the patient is fabricating illness.',
    'Medication reduction, if appropriate, should be based on the confirmed epileptic component and carried out with specialist oversight rather than a blanket response to one captured nonepileptic episode.')],['DX'])

add('Epilepsy syndromes','Juvenile Myoclonic Epilepsy',
 'A 19-year-old reports morning arm jerks causing dropped cups for several years and a tonic-clonic seizure after sleep deprivation. Development and examination are normal. Which syndrome is most likely?',
 'Juvenile myoclonic epilepsy',[
 ('Epilepsy with generalized tonic-clonic seizures alone','This syndrome does not include the recurrent myoclonic seizures central to the history; directed questioning about jerks changes the classification.'),
 ('Juvenile absence epilepsy','Absences and generalized tonic-clonic seizures can occur, but prominent habitual morning myoclonus points toward JME rather than an absence-dominant syndrome.'),
 ('Progressive myoclonic epilepsy','Progressive cognitive, cerebellar or neurological decline would suggest this group; normal development and a stable adolescent-onset morning-jerk pattern fit JME.')],
 [S('Syndrome Recognition','**Morning myoclonus** is frequently overlooked until a generalized tonic-clonic seizure prompts assessment.',
    'JME commonly begins in adolescence, with jerks after awakening and sensitivity to sleep deprivation or alcohol. Some patients also have absence seizures.',
    'EEG typically shows generalized spike- or polyspike-wave, often in the 3–5.5-Hz range, with photosensitivity in some patients. A habitual myoclonic jerk may coincide with a generalized polyspike discharge.'),
  S('Treatment Implications','**Choose a broad-spectrum regimen** and address sleep, adherence and alcohol exposure.',
    'Valproate can be highly effective but has major reproductive safety limitations. Levetiracetam is an important alternative; lamotrigine may aggravate myoclonus in some individuals.',
    'Carbamazepine and related narrow-spectrum strategies may worsen generalized myoclonic or absence seizures. Relapse risk after medication withdrawal is substantial, so apparent remission does not automatically imply a short treatment course.')],['JME','TX'])

add('Epilepsy syndromes','Dravet Syndrome',
 'An adult with developmental impairment had prolonged fever-triggered hemiclonic seizures beginning at 6 months, later multiple seizure types, and worsening on carbamazepine. Which genetic mechanism is most characteristic?',
 'SCN1A loss of function',[
 ('SCN1A gain of function as the usual Dravet mechanism','Gain-of-function channel effects occur in other sodium-channel phenotypes, but the classic Dravet mechanism is loss of function with impaired inhibitory interneuron excitability.'),
 ('KCNQ2-related self-limited neonatal epilepsy','This typically begins in the neonatal period and has a different evolution; it does not best fit the prolonged febrile hemiclonic infancy onset and later Dravet trajectory.'),
 ('PRRT2-related self-limited infantile epilepsy','PRRT2 can cause infantile seizures and movement disorders, often with more favorable development; it does not best explain this severe fever-sensitive developmental epileptic encephalopathy.')],
 [S('Genetic and Clinical Pattern','**Dravet syndrome** is commonly associated with pathogenic SCN1A variants causing reduced sodium-channel function.',
    'Onset is usually in infancy with prolonged fever-sensitive seizures, often hemiclonic or generalized. Later myoclonic and other seizure types, developmental slowing and gait or behavioral difficulties may emerge.',
    'A normal early MRI or EEG does not exclude the syndrome. Genetics supports diagnosis but must be interpreted with the phenotype and variant classification.'),
  S('Medication Consequences','**Maintenance sodium-channel blockers** can worsen the typical syndrome and should not be chosen simply because a seizure looks focal.',
    'Valproate and clobazam are commonly used, with syndrome-specific options including stiripentol, pharmaceutical cannabidiol or fenfluramine under specialist care and monitoring.',
    'Provide an individualized rescue plan for prolonged seizures and fever-associated exacerbations. Acute status treatment and lifelong maintenance decisions are related but distinct; an adult diagnosis still matters when childhood records reveal the characteristic course.')],['TX','DRUG'])

add('Epilepsy syndromes','Lennox–Gastaut Syndrome',
 'A young adult with childhood-onset intellectual disability has tonic seizures during sleep, injurious drop attacks and atypical absences. Which EEG combination is most characteristic?',
 'Generalized slow spike-and-wave with sleep-related generalized paroxysmal fast activity',[
 ('Normal background with regular 3-Hz spike-and-wave only during brief absences','This is more typical of a typical absence syndrome; the mixed tonic-drop seizure burden and developmental impairment suggest a different electroclinical disorder.'),
 ('Isolated centrotemporal spikes with otherwise normal development','That pattern supports self-limited epilepsy with centrotemporal spikes in the appropriate childhood context, not the tonic and atypical-absence encephalopathy described.'),
 ('Continuous unilateral temporal slowing without generalized epileptiform activity','Focal slowing indicates local dysfunction but does not supply the characteristic generalized interictal and sleep patterns of Lennox–Gastaut.')],
 [S('Electroclinical Syndrome','**Lennox–Gastaut** combines multiple seizure types, characteristic EEG findings and developmental or cognitive impairment.',
    'Generalized slow spike-and-wave is usually below 2.5 Hz. Generalized paroxysmal fast activity in sleep supports the diagnosis, particularly alongside tonic seizures.',
    'Drop attacks can reflect tonic or atonic events, so the term describes the functional consequence rather than a single seizure mechanism.'),
  S('Therapeutic Planning','**Broad-spectrum and syndrome-specific treatment** is usually needed, with careful attention to sedation and cumulative adverse effects.',
    'Valproate, lamotrigine, clobazam, rufinamide and other approved options may be selected according to the person and jurisdiction. Ketogenic dietary therapy and selected neuromodulation can be considered in specialist care.',
    'Corpus callosotomy may reduce disabling drop attacks in selected drug-resistant cases; it is a palliative disconnection procedure rather than a general cure for all seizure types or developmental impairment.')],['TX','DRUG'])

add('Epilepsy syndromes','Progressive Myoclonic Epilepsy',
 'A 22-year-old labeled as having JME develops worsening stimulus-sensitive action myoclonus, gait ataxia and cognitive decline. Which interpretation is most appropriate?',
 'Reassess for a progressive myoclonic epilepsy',[
 ('The progression is an expected defining feature of uncomplicated JME','JME does not ordinarily produce progressive neurological and cognitive deterioration; the changing phenotype is an important diagnostic warning.'),
 ('The absence of focal weakness excludes a neurological progressive disorder','Progressive myoclonic epilepsies may predominantly affect coordination, movement and cognition rather than cause a focal pyramidal weakness.'),
 ('Generalized polyspikes establish JME regardless of the clinical course','Generalized polyspike discharges are not exclusive to JME; the syndrome must fit age, seizure types, development and longitudinal course.')],
 [S('When to Reclassify','**Progressive ataxia or cognitive decline** is an alert against uncomplicated JME.',
    'The progressive myoclonic epilepsies include several genetic and metabolic disorders, such as Unverricht–Lundborg disease, Lafora disease and some mitochondrial or lysosomal disorders. They vary in age, progression and associated findings.',
    'Action- or stimulus-sensitive myoclonus can become a major disability distinct from the frequency of generalized convulsions.'),
  S('Targeted Evaluation','**Review the original diagnosis** and distinguish disease progression from medication toxicity.',
    'Examine cognition, coordination, vision, hearing and peripheral findings; obtain MRI and electrophysiology as indicated, then select genetic or metabolic tests according to phenotype and family history.',
    'Avoid indiscriminate broad testing without a clinical hypothesis. Genetic counseling is important, and treatment must address the specific disease when possible as well as seizure and myoclonus control. A prior familiar label should not prevent reassessment when its expected course no longer fits.')],['JME','DX'])

add('Diagnostic evaluation','MRI in New Focal Epilepsy',
 'A 45-year-old has a first unprovoked seizure preceded by a recurrent stereotyped unilateral sensory aura. Emergency CT is normal. Which investigation best evaluates an underlying epileptogenic structural lesion?',
 'Brain MRI using an epilepsy protocol',[
 ('Repeat noncontrast CT alone as the definitive structural assessment','CT is useful acutely for blood and major lesions but may miss cortical dysplasia, small tumors or mesial temporal abnormalities detected by an epilepsy-protocol MRI.'),
 ('Routine EEG alone without structural imaging','EEG assists classification and risk assessment but does not anatomically exclude a focal cortical lesion, even if epileptiform discharges are absent.'),
 ('Serum antiseizure-drug concentrations before any treatment has been given','Drug concentrations are useful for selected treated patients, not for identifying the cause of an untreated first focal seizure.')],
 [S('Structural Assessment','**Epilepsy-protocol MRI** uses sequences and planes tailored to subtle epileptogenic abnormalities.',
    'High-resolution structural imaging can identify hippocampal sclerosis, focal cortical dysplasia, low-grade tumors, vascular malformations or prior injury. An expert neuroradiology review improves interpretation.',
    'A normal emergency CT is not a substitute for this evaluation when focal epilepsy is suspected; CT and MRI answer overlapping but different questions.'),
  S('Integrated Work-Up','**The clinical event, EEG and imaging** must be interpreted together.',
    'Check glucose, electrolytes and provoking factors and obtain ECG when transient loss of consciousness is part of the presentation. Lumbar puncture is selected for suspected infection or inflammation, not performed automatically after every first seizure.',
    'A lesion is not necessarily causal merely because it is present; assess concordance with semiology and EEG. Conversely, an apparently normal MRI does not exclude epilepsy or a surgically relevant focus.')],['DX'])

add('Diagnostic evaluation','Treatment After a First Unprovoked Seizure',
 'An adult asks whether immediate antiseizure treatment after a first unprovoked seizure guarantees a better long-term chance of permanent remission. Which counseling statement is most accurate?',
 'It reduces early recurrence risk but has not shown improved long-term sustained remission',[
 ('It prevents all further seizures if started within 24 hours','Immediate treatment does not guarantee seizure freedom; recurrence depends on the underlying disease, adherence and drug effectiveness.'),
 ('It has no effect on recurrence during the next two years','Trials show an early recurrence reduction with immediate therapy, so lack of proven long-term remission benefit does not mean there is no short-term preventive effect.'),
 ('It is mandatory after every first seizure regardless of cause or patient preference','Acute symptomatic events and unprovoked events differ, and treatment after a first unprovoked event is individualized using risk, consequences and preferences.')],
 [S('Recurrence and Evidence','**First unprovoked-seizure recurrence** is greatest early; the AAN/AES 2015 synthesis estimated approximately ==21–45% within two years==.',
    'Prior brain insult, epileptiform EEG findings, a significant causal imaging abnormality and a nocturnal seizure can increase risk. These factors should not simply be added as if they formed a validated linear risk score.',
    'Immediate medication reduces near-term recurrence but has not demonstrated a corresponding improvement in long-term sustained remission for every first-seizure patient.'),
  S('Individualized Decision','**Balance potential recurrence consequences with medication burden** and the strength of diagnostic evidence.',
    'Discuss occupation, injuries, driving restrictions, pregnancy plans, comorbidity, adverse effects and patient values. A sufficiently high established recurrence risk may also meet the ILAE single-seizure epilepsy definition.',
    'Ensure follow-up and practical safety advice whether or not treatment begins immediately. Uncertainty should be explained rather than converted into either universal medication or universal deferral.')],['FIRST','DEF'],style='direct')

add('Diagnostic evaluation','Postictal Prolactin Limitations',
 'Which statement best describes serum prolactin in the assessment of a suspected seizure?',
 'A timed elevation may support certain epileptic events but cannot reliably distinguish seizure from syncope',[
 ('A normal value excludes an epileptic seizure','Sensitivity is incomplete and depends on event type and timing; many genuine focal or generalized seizures need not produce a diagnostic elevation.'),
 ('An elevated value proves epilepsy rather than convulsive syncope','Syncope can also raise prolactin, so a positive result cannot by itself distinguish these mechanisms of transient loss of consciousness.'),
 ('A sample taken the next morning has the same diagnostic meaning as an early timed sample','The post-event response is transient. Delayed measurements do not carry the same interpretation as an appropriately timed postictal specimen.')],
 [S('What the Test Can Add','**Postictal prolactin** is an adjunct with a narrow evidence base, not a universal event classifier.',
    'Sampling around 10–20 minutes after an appropriate event may help distinguish generalized tonic-clonic or some focal impaired-consciousness seizures from functional episodes. It is less useful for other seizure types and has timing-dependent sensitivity.',
    'A baseline may be influenced by pregnancy, pituitary disease and medications, and elevations are not uniquely epileptic.'),
  S('Preferred Diagnostic Reasoning','**Witness description and electroclinical assessment** remain central.',
    'Evaluate prodrome, posture, triggers, duration, recovery, lateral tongue injury and the full motor sequence. Cardiac syncope can include brief jerks and deserves appropriate ECG or rhythm assessment.',
    'Use video-EEG when recurring events remain uncertain and an appropriate study can capture the habitual spell. Neither a single biomarker nor one dramatic movement should replace a coherent differential diagnosis.')],['DX'],style='direct')

add('Medication selection','Focal Epilepsy and Depressive Comorbidity',
 'An adult with newly diagnosed focal epilepsy also has depression and is particularly concerned about behavioral adverse effects. There is no cardiac disease and slow titration is acceptable. Which option is a reasonable first-line choice?',
 'Lamotrigine',[
 ('Levetiracetam as the only suitable option because it cannot affect behavior','Levetiracetam is also effective first-line therapy, but irritability and behavioral or mood adverse effects matter in this patient; the absolute claim makes it less suitable than the stated alternative.'),
 ('Ethosuximide','Ethosuximide is chiefly an absence-seizure drug and does not provide appropriate focal-seizure monotherapy coverage in this case.'),
 ('Vigabatrin as the preferred initial monotherapy','Vigabatrin has selected indications but irreversible visual-field toxicity and its therapeutic position make it unsuitable as the routine preferred initial focal monotherapy here.')],
 [S('Selection by Seizure and Patient','**Lamotrigine or levetiracetam** are first-line focal monotherapy options in NICE NG217.',
    'Lamotrigine can be attractive when depressive symptoms or behavioral tolerability influence the choice, provided the delay imposed by careful titration is acceptable. It is not universally superior for every individual.',
    'Levetiracetam has few pharmacokinetic interactions and can be introduced more quickly, but behavioral vulnerability deserves explicit counseling and monitoring.'),
  S('Starting Safely','**Slow lamotrigine titration** reduces the risk of serious rash.',
    'In a typical adult taking neither valproate nor enzyme-inducing antiseizure medicines, an initial 25 mg daily for two weeks followed by 50 mg daily for two weeks is a common labeled schedule; subsequent increases follow the applicable product regimen.',
    'Valproate coadministration requires a lower starting schedule. Discuss rash, mucosal lesions or systemic symptoms promptly, and check relevant drug interactions and adherence before any later dose escalation.')],['TX','DRUG'])

add('Medication selection','Ethosuximide for Isolated Absences',
 'A child has typical absence seizures without myoclonus or generalized tonic-clonic seizures, normal development and a typical EEG. Which monotherapy is the preferred initial absence-specific option?',
 'Ethosuximide',[
 ('Lamotrigine','It can treat absences and may be selected when other factors matter, but ethosuximide is the standard initial choice for uncomplicated absence-only disease.'),
 ('Levetiracetam','It may be considered in some absence treatment pathways, particularly with other seizure types, but is not the preferred absence-specific initial choice in this setting.'),
 ('Sodium valproate','Valproate covers absences and generalized convulsions, but broader coverage is not needed here and its systemic and reproductive adverse effects favor ethosuximide for isolated absences.')],
 [S('Mechanism and Indication','**Ethosuximide** reduces low-threshold T-type calcium currents in thalamic networks involved in absence activity.',
    'Its strength is absence seizure control; it does not adequately cover generalized tonic-clonic or focal seizures. Ask specifically about morning jerks and convulsions before choosing absence-only therapy.',
    'NICE NG217 recommends it first-line for absence seizures without other seizure types requiring broader coverage.'),
  S('Administration and Monitoring','**Dose is titrated to response and tolerability**, commonly starting at a low daily dose and increasing gradually under the relevant pediatric or adult regimen.',
    'A usual maintenance range is approximately 20 mg/kg/day in children, individualized by response and labeling. Gastrointestinal upset, fatigue and headache are common; rash and rare hematologic reactions require attention.',
    'If generalized tonic-clonic seizures coexist or emerge, reconsider the syndrome and medication coverage rather than assuming absence control means all seizure risk is treated.')],['TX','DRUG'])

add('Medication selection','Absences With Generalized Tonic-Clonic Seizures',
 'A woman beyond childbearing potential has typical absences and recurrent generalized tonic-clonic seizures. Liver function is normal, and there is no mitochondrial disorder. Which option best covers both seizure types?',
 'Sodium valproate',[
 ('Ethosuximide alone','It treats absences but does not adequately prevent generalized tonic-clonic seizures; the additional seizure type changes the necessary spectrum of coverage.'),
 ('Carbamazepine','It is effective for many focal seizures but may worsen generalized absence and myoclonic seizures, making it a poor match for this generalized syndrome.'),
 ('Gabapentin','Gabapentin has roles in focal epilepsy and neuropathic pain, but is not an appropriate broad-spectrum treatment for this absence–generalized-convulsion combination and may worsen absences.')],
 [S('Broad-Spectrum Therapy','**Valproate** can control absence, myoclonic and generalized tonic-clonic seizures.',
    'Its actions include effects on sodium channels and inhibitory neurotransmission; no single mechanism accounts for all clinical effects. The seizure combination makes an absence-only drug insufficient.',
    'Lamotrigine or levetiracetam may be alternatives in appropriate patients; comparative choice considers seizure mix, response and adverse effects.'),
  S('Safety Determines Suitability','**Reproductive risk** is a major limitation and must not be omitted from a discussion of valproate.',
    'In people who may become pregnant, avoid it when clinically feasible because of major malformation and neurodevelopmental risks, following applicable local regulatory requirements. Rules for initiating treatment also differ across countries and sexes.',
    'Monitor weight, platelets and liver-related risk; recognize pancreatitis and hyperammonemic encephalopathy. Avoid valproate in relevant POLG-related mitochondrial disease and significant hepatic disease. The stem removes key competing safety constraints rather than claiming universal first choice.')],['TX','PREG','DRUG'])

add('Medication selection','Lamotrigine During Pregnancy',
 'A woman controlled on lamotrigine has falling trough concentrations and breakthrough focal seizures during the second trimester despite confirmed adherence. Which explanation and response are most appropriate?',
 'Pregnancy can increase clearance; use clinical and concentration-guided dose adjustment with a postpartum plan',[
 ('The fall proves nonadherence despite the history','Gestational pharmacokinetic changes can lower levels substantially, so adherence concerns should be assessed rather than assumed to be the only explanation.'),
 ('Stop lamotrigine abruptly because every antiseizure drug is more dangerous than seizures','Abrupt withdrawal can provoke dangerous seizures; fetal risk and maternal seizure control require an individualized plan rather than sudden cessation.'),
 ('Keep every dose increase unchanged after delivery','Clearance can fall toward baseline postpartum, so an increased pregnancy dose may cause toxicity unless monitored and adjusted after delivery.')],
 [S('Gestational Pharmacokinetics','**Lamotrigine clearance** may rise during pregnancy, reducing exposure despite an unchanged dose.',
    'A preconception concentration associated with good control is a useful individual reference when available. Follow symptoms and appropriately timed concentrations rather than treating a population laboratory range as the sole target.',
    'Levetiracetam exposure can also fall during pregnancy. Changes vary, so monitoring and adjustment should be personalized.'),
  S('Maternal–Fetal Planning','**Maintain control of convulsive seizures** while using the safest effective regimen for the individual.',
    'The AAN/AES/SMFM 2024 guidance supports considering lamotrigine, levetiracetam or oxcarbazepine when appropriate to minimize major malformation risk, and at least 0.4 mg folic acid daily for people treated with ASMs who may become pregnant.',
    'Plan postpartum reassessment because clearance may normalize rapidly and dose-related dizziness, diplopia or ataxia can appear. Do not interpret pregnancy safety as absence of any risk or a reason to change a stable regimen without careful review.')],['PREG','DRUG'])

add('Pharmacology and interactions','Valproate–Lamotrigine Interaction',
 'Why does adding lamotrigine to valproate require a lower starting dose and slower escalation than adding it without valproate?',
 'Valproate inhibits lamotrigine glucuronidation and increases exposure',[
 ('Valproate induces lamotrigine glucuronidation and lowers exposure','That would tend to require higher rather than lower dosing; valproate’s clinically important effect is inhibition of lamotrigine clearance.'),
 ('Lamotrigine immediately prevents valproate absorption','The interaction is mainly metabolic and does not reflect a complete loss of gastrointestinal valproate uptake when the drugs are combined.'),
 ('The combination requires a rapid loading dose to avoid tolerance','Rapid initiation and escalation increase serious rash risk; the combination calls for a cautious schedule, not a loading strategy for routine maintenance therapy.')],
 [S('Pharmacokinetic Mechanism','**Reduced lamotrigine clearance** prolongs its half-life when valproate is present.',
    'Higher exposure and excessive initial dosing or escalation increase the risk of serious cutaneous reactions, including Stevens–Johnson syndrome and toxic epidermal necrolysis. The combination can be useful, but the schedule must reflect the interaction.',
    'For an adult taking valproate, a typical labeled starting schedule is ==25 mg every other day for two weeks==, then 25 mg daily for two weeks, followed by appropriately cautious increases.'),
  S('Other Important Interactions','**Estrogen-containing contraception** can lower lamotrigine concentrations by increasing clearance.',
    'Starting or stopping estrogen, or the hormone-free interval, can alter exposure and require clinical review. Enzyme-inducing antiseizure drugs can also lower lamotrigine levels.',
    'Any significant treatment interruption may require restarting titration according to the product guidance rather than resuming the previous full dose. A rash with mucosal or systemic symptoms warrants urgent assessment.')],['DRUG'],style='direct')

add('Pharmacology and interactions','Carbamazepine Pharmacogenetics',
 'Before starting carbamazepine in a treatment-naive patient whose ancestry has a high prevalence of HLA-B*15:02, which action is most appropriate?',
 'Screen for HLA-B*15:02 and use the result in drug selection',[
 ('Screen for HLA-B*57:01 as the relevant carbamazepine SJS marker','HLA-B*57:01 is a major abacavir hypersensitivity marker; it is not a substitute for the carbamazepine-specific HLA-B*15:02 assessment in this population.'),
 ('Use a normal eosinophil count to rule out future severe cutaneous reactions','Baseline eosinophils cannot exclude genetically associated future SJS/TEN risk; a normal count does not replace appropriate pharmacogenetic screening.'),
 ('Perform only a skin-prick test to establish long-term safety','SJS/TEN is not assessed by routine immediate-type allergy skin testing, and a negative prick test does not establish safe exposure.')],
 [S('Genetic Risk','**HLA-B*15:02** is strongly associated with carbamazepine-related SJS/TEN in genetically at-risk ancestry groups.',
    'Testing is recommended before first exposure when ancestry and local guidance indicate risk. A positive result generally favors an alternative unless a specialist concludes that exceptional benefit outweighs risk.',
    'HLA-A*31:01 is associated with a broader carbamazepine hypersensitivity spectrum in several populations. A negative HLA-B*15:02 test does not eliminate all rash risk.'),
  S('Broader Drug Assessment','**Carbamazepine** is a sodium-channel blocker useful for focal seizures and selected neuralgias.',
    'It can worsen absence or myoclonic generalized epilepsy. Important adverse effects include hyponatremia, dizziness, blood dyscrasias and severe rash; relevant CBC, sodium and hepatic monitoring is individualized.',
    'Enzyme induction can reduce hormonal contraceptive and other drug exposure, and autoinduction changes its own clearance after initiation. Genotype screening addresses one risk, not every pharmacological interaction or contraindication.')],['DRUG'],style='direct')

add('Pharmacology and interactions','Phenytoin Nonlinear Kinetics',
 'A small phenytoin dose increase produces a disproportionate rise in concentration with nystagmus and ataxia. Which mechanism best explains this?',
 'Saturation of capacity-limited hepatic metabolism',[
 ('Dose-independent first-order clearance across the full concentration range','Strict first-order kinetics predicts a more proportional dose–concentration relationship; phenytoin can depart from this as metabolic capacity becomes saturated.'),
 ('Accelerated renal filtration of unchanged phenytoin','Phenytoin is mainly hepatically metabolized, and increased renal elimination would not explain accumulation and toxicity after a small increment.'),
 ('Autoinduction causing an abrupt fall in clearance','Autoinduction typically increases metabolic clearance rather than explains this capacity-limited accumulation; it is a prominent carbamazepine concept, not the main phenytoin mechanism here.')],
 [S('Capacity-Limited Clearance','**Phenytoin metabolism is saturable**, so modest increments near metabolic capacity may produce large concentration increases.',
    'This is commonly described using Michaelis–Menten kinetics; a single fixed half-life becomes misleading as the dose and concentration rise. Adjust maintenance doses cautiously rather than proportionally scaling a high concentration.',
    'Nystagmus, diplopia, dysarthria and gait or limb ataxia suggest toxicity in the appropriate context.'),
  S('Total Versus Free Concentration','**Protein binding** affects interpretation of the usual total concentration range, approximately 10–20 micrograms/mL.',
    'Hypoalbuminemia, renal dysfunction and competing highly protein-bound drugs can increase the active free fraction. A free phenytoin measurement is preferable when binding is substantially abnormal; correction equations are imperfect.',
    'A low total concentration should not trigger automatic dose escalation in a symptomatic hypoalbuminemic patient. Also consider enzyme induction, interactions, formulation changes and enteral-feeding effects when levels change unexpectedly.')],['DRUG'],style='direct')

add('Pharmacology and interactions','Topiramate and Carbonic Anhydrase Inhibition',
 'A patient taking topiramate develops recurrent calcium phosphate stones and a low serum bicarbonate with a normal anion gap. Which drug effect best links these findings?',
 'Carbonic anhydrase inhibition with renal bicarbonate loss',[
 ('Antidiuretic hormone release with water retention','This more directly explains hypotonic hyponatremia with selected drugs such as carbamazepine, not the characteristic acidosis–stone combination.'),
 ('Inhibition of lamotrigine glucuronidation','Valproate has that important interaction; it does not explain topiramate-related renal bicarbonate wasting and stone risk.'),
 ('Increased proximal urate reabsorption as the principal mechanism','Hyperuricemia can contribute to other stone contexts, but the topiramate pattern is linked to carbonic anhydrase inhibition, urinary changes and hypocitraturia.')],
 [S('Renal Effects','**Topiramate** can cause hyperchloremic non-anion-gap metabolic acidosis through carbonic anhydrase inhibition.',
    'Urinary alkalinization and reduced citrate can promote calcium phosphate stones. Baseline and periodic bicarbonate assessment is recommended in labeling, with closer review when symptoms or risks are present.',
    'Other carbonic anhydrase inhibitors or a ketogenic diet may add acidosis or stone risk; hydration counseling and treatment reassessment are important.'),
  S('Other High-Yield Toxicities','**Cognitive slowing, word-finding difficulty and paresthesias** can limit use despite antiseizure or migraine benefit.',
    'Weight loss may occur. Acute myopia with secondary angle-closure glaucoma requires urgent ophthalmic and medication assessment, especially with new painful blurred vision.',
    'Pregnancy exposure carries important fetal risks and jurisdiction-specific prevention requirements. A favorable effect on body weight does not make the drug appropriate when renal, ocular, cognitive or reproductive risks dominate.')],['DRUG'],style='direct')

add('Pharmacology and interactions','Lacosamide and Cardiac Conduction',
 'A patient with focal epilepsy and baseline first-degree AV block is being considered for lacosamide while taking a beta blocker. Which adverse effect deserves particular monitoring?',
 'PR prolongation and worsening atrioventricular conduction',[
 ('Marked QT shortening as the characteristic lacosamide effect','QT shortening is a more relevant caution with agents such as rufinamide or cenobamate; lacosamide’s central labeled conduction concern is PR prolongation.'),
 ('Typical antimuscarinic sinus tachycardia without AV effects','That is not the defining cardiac action of lacosamide and would miss the potential additive conduction effect with the beta blocker.'),
 ('Dose-dependent shortening of the PR interval','The clinically important change is prolongation, potentially progressing to conduction block in susceptible patients, not improved AV conduction.')],
 [S('Mechanism and ECG','**Lacosamide** enhances slow inactivation of voltage-gated sodium channels and is used for focal seizures.',
    'Dose-dependent PR prolongation and AV block can occur. Baseline conduction disease, structural cardiac disease and other conduction-slowing drugs increase the need for caution.',
    'Obtain an ECG before initiation and after titration in relevant at-risk patients. Review symptoms such as syncope, marked dizziness or palpitations promptly.'),
  S('Clinical Selection','**The cardiac history** can change an otherwise reasonable antiseizure choice.',
    'Lacosamide is not automatically prohibited by every mild PR prolongation, but the combination in this stem warrants an individualized risk review and monitoring plan. More advanced block without pacing raises greater concern.',
    'Dizziness, diplopia and ataxia are other common tolerability issues. Renal or hepatic impairment may affect dosing, and IV use requires attention to the product-specific infusion and cardiac monitoring recommendations.')],['DRUG'],style='direct')

add('Pharmacology and interactions','Levetiracetam Behavioral Adverse Effects',
 'Seizures improve after levetiracetam is started, but the patient develops new severe irritability and aggression. No metabolic, intoxication or postictal explanation is found. Which interpretation is most appropriate?',
 'Levetiracetam-related behavioral toxicity should be considered',[
 ('The symptoms prove that the seizures are functional','Behavioral adverse effects of a medication do not reclassify the original events. Epilepsy and psychiatric symptoms need separate, integrated assessment.'),
 ('The drug cannot be responsible because it has few hepatic interactions','Low pharmacokinetic interaction potential does not imply absence of central behavioral adverse effects; these are separate dimensions of tolerability.'),
 ('The symptoms indicate the expected syndrome of phenytoin cerebellar toxicity','Phenytoin toxicity more characteristically produces nystagmus, ataxia and dysarthria; the timing and behavioral phenotype point to a different drug effect here.')],
 [S('Adverse-Effect Recognition','**Irritability, agitation, aggression or mood change** can occur with levetiracetam.',
    'Assess severity, temporal relationship, prior psychiatric history, sleep and concurrent drugs. Urgent evaluation is appropriate for dangerous behavior, severe depression or suicidal thinking.',
    'Do not dismiss symptoms solely because seizure frequency improved, and do not abruptly stop treatment without a safe alternative when ongoing seizures pose risk.'),
  S('Pharmacology and Adjustment','**SV2A binding** contributes to levetiracetam’s antiseizure action.',
    'It has relatively few hepatic enzyme interactions and is largely renally cleared, so kidney function informs dose adjustment. These features can be useful in polypharmacy but do not remove behavioral or sedating adverse effects.',
    'Dose reduction or transition to another suitable drug can be considered with specialist oversight. The best alternative depends on seizure type, comorbidity and prior response; preserving seizure control and improving psychiatric tolerability are both treatment goals.')],['DRUG'])

add('Drug resistance and advanced treatment','Definition of Drug-Resistant Epilepsy',
 'Which treatment history meets the ILAE definition of drug-resistant epilepsy?',
 'Failure of two tolerated, appropriately selected and adequately used medication schedules to achieve sustained seizure freedom',[
 ('Failure of one drug stopped after two days because of mild nausea','An inadequately tried or intolerable regimen does not establish efficacy failure under the definition, and only one schedule has been attempted.'),
 ('Breakthrough events solely during repeated missed doses of otherwise effective therapy','Nonadherence can cause apparent treatment failure but must be addressed before classifying adequate medication trials as ineffective.'),
 ('Persistent absences during phenytoin and carbamazepine treatment','These are inappropriate choices for an absence syndrome and can worsen it; failure of poorly selected agents does not prove true resistance to appropriate treatment.')],
 [S('Adequacy of Trials','**Drug resistance** requires failure of two tolerated, appropriately chosen and used schedules, alone or in combination.',
    'Confirm the events are epileptic, the seizure or syndrome classification is correct, doses and duration are adequate, and adherence and interactions have been assessed. These checks identify pseudo-resistance.',
    'The definition concerns sustained seizure freedom rather than a modest reduction in frequency. Trial length must be interpreted in relation to the person’s prior interseizure intervals.'),
  S('What the Definition Changes','**Referral to a comprehensive epilepsy service** should occur once resistance is established rather than after years of serial similar drug substitutions.',
    'Evaluation can identify a resectable focus, suitable neuromodulation, dietary options or a corrected diagnosis. Referral is an assessment, not a commitment to an operation.',
    'Continue optimizing safety, comorbidities and medication while evaluation proceeds. A structurally normal MRI does not remove the need for specialist review when focal epilepsy remains drug resistant.')],['DRE'],style='direct')

add('Drug resistance and advanced treatment','Presurgical Evaluation of Temporal Epilepsy',
 'An adult has disabling focal seizures despite two adequate suitable medication trials. MRI shows unilateral hippocampal sclerosis and video-EEG findings are concordant. Which next step is most appropriate?',
 'Comprehensive epilepsy-surgery evaluation',[
 ('Require failure of ten medications before referral','An arbitrary high number prolongs exposure to uncontrolled seizures; two adequate failures meet the usual resistance threshold and justify comprehensive evaluation.'),
 ('Proceed directly to resection without language or memory assessment','Concordance is encouraging but does not replace assessment of cognitive risk, essential cortex and the complete presurgical data.'),
 ('Use vagus nerve stimulation as the obligatory first procedure before considering resection','VNS can be useful when resection is unsuitable, but it is not a mandatory prerequisite to potentially curative surgery for a well-localized resectable temporal focus.')],
 [S('Assessing Candidacy','**Concordant unilateral focal epilepsy** is an important setting in which surgery may offer substantial seizure-control benefit.',
    'Review habitual seizure video-EEG, high-quality MRI, neuropsychology and the relationship to language and memory networks. Some cases need functional imaging, language mapping or invasive monitoring.',
    'The epileptogenic zone is not automatically identical to every MRI abnormality; concordance across independent modalities is central.'),
  S('Benefits and Trade-Offs','**Resection or ablation** is selected according to anatomy, expected efficacy and functional risk.',
    'Dominant temporal procedures can affect verbal memory or language; visual-field and other surgical risks also require counseling. Choice between open surgery, ablation and nonresective options is individualized.',
    'If onset is bilateral, poorly localizable or inseparable from essential cortex, VNS, DBS or responsive neurostimulation may be considered where available. These generally aim for seizure reduction and should not be presented as equivalent cures for every focal epilepsy.')],['DRE','DX'])

add('Drug resistance and advanced treatment','SUDEP Counseling',
 'A patient with frequent nocturnal generalized tonic-clonic seizures asks which modifiable clinical factor is most strongly associated with reducing SUDEP risk. What is the best answer?',
 'Achieving freedom from generalized tonic-clonic seizures',[
 ('Normalizing an interictal EEG despite ongoing convulsions','EEG changes can inform care, but persistent tonic-clonic seizures remain a major risk even if one between-event recording appears normal.'),
 ('Eliminating all subjective auras while nocturnal convulsions continue','Auras may matter for safety and quality of life, but control of the convulsive seizure burden is the stronger established SUDEP-related priority.'),
 ('Using a nighttime alarm device instead of optimizing treatment','Detection technology may support a safety plan, but it does not replace seizure control or have established evidence that every device prevents SUDEP.')],
 [S('Risk Communication','**Generalized tonic-clonic seizure burden** is the strongest established clinical SUDEP risk factor.',
    'Freedom from these seizures is associated with reduced risk. Discuss the risk in clear individualized terms without implying that every person with epilepsy has the same prognosis or that zero risk can be guaranteed.',
    'Poor adherence, nocturnal events and uncontrolled epilepsy require attention as part of an integrated seizure-control strategy.'),
  S('Prevention Plan','**Optimize treatment and adherence**, and assess drug resistance promptly.',
    'Address sleep deprivation, alcohol-related triggers and barriers to taking medication. Explain rescue treatment, seizure first aid and when emergency help is needed, and discuss nighttime supervision or detection options according to the person’s circumstances.',
    'Do not oversell monitoring devices as proven prevention. Shared planning should support autonomy and practical safety rather than create restrictions without explaining their relevance or evidence.')],['DRE','DRUG'])

add('Status epilepticus: recognition','Convulsive Status Time Points',
 'A generalized tonic-clonic seizure has continued for 6 minutes. According to the ILAE operational framework, which interpretation is correct?',
 'The treatment threshold has been exceeded; do not wait for the 30-minute injury-risk time point',[
 ('Status treatment should start only after 30 minutes','Thirty minutes corresponds to an approximate time beyond which long-term injury risk increases in convulsive SE; it is not a safe waiting period before treatment.'),
 ('Status is excluded unless two separate seizures have occurred','One prolonged seizure is sufficient. Recurrent seizures without recovery can also meet the clinical emergency definition.'),
 ('A 6-minute seizure is automatically super-refractory status','Super-refractory refers to persistence or recurrence despite an anesthetic-treatment course, not simply duration beyond the initial treatment threshold.')],
 [S('Operational Thresholds','**Convulsive SE** uses ==t1 approximately 5 minutes== as the time to initiate treatment and ==t2 approximately 30 minutes== as a marker of increasing long-term consequence risk.',
    'These time points differ across seizure types and should not be transferred unchanged to every nonconvulsive syndrome. Recurrent convulsions without return toward baseline are also an emergency.',
    'Treatment responsiveness worsens with delay, so preparation and adequately dosed therapy should proceed promptly.'),
  S('Immediate Parallel Actions','**Airway support, oxygenation, glucose testing and seizure termination** occur in parallel.',
    'Check for hypoglycemia and give dextrose promptly when needed; provide thiamine in an at-risk patient without delaying glucose. Obtain IV or intraosseous access and assess temperature, electrolytes, toxins and medication history.',
    'Do not postpone the first benzodiazepine for CT, EEG or a complete laboratory panel in an actively convulsing patient. Investigate and treat the precipitating cause as seizure control proceeds.')],['SE','ENLS'])

add('Status epilepticus: initial treatment','Adequate Initial Lorazepam Dose',
 'A 70-kg adult has ongoing convulsive status with established IV access. Which initial lorazepam regimen is appropriate?',
 '0.1 mg/kg IV, capped at 4 mg for the initial dose',[
 ('0.01 mg/kg IV, capped at 1 mg','This is commonly too small for established adult convulsive status and risks ineffective treatment followed by delay; use an adequate guideline-based initial dose.'),
 ('4 mg orally as the initial route','Oral delivery is not appropriate during active convulsions because of aspiration and delayed or unreliable absorption; an immediately effective parenteral route is available.'),
 ('0.1 mg/kg as a continuous infusion without an initial bolus','A continuous sedative infusion may be used in later refractory care, but it does not replace the prompt initial benzodiazepine dose in this treatment phase.')],
 [S('Benzodiazepine Therapy','**IV lorazepam** is given at ==0.1 mg/kg, maximum 4 mg per initial dose== in an appropriate protocol.',
    'For this adult, the cap determines the initial dose. A repeat dose may be given after several minutes if seizures persist, following the emergency pathway while preparing a longer-acting IV antiseizure drug.',
    'Underdosing is a common cause of apparent benzodiazepine failure; document dose, route and administration time.'),
  S('Safety Without Delay','**Respiratory and circulatory support** must be ready during treatment.',
    'Monitor oxygenation, ventilation, pressure and cardiac rhythm. Ongoing untreated convulsions also cause major respiratory harm, so fear of sedation should not lead to ineffective microdosing.',
    'If seizures persist after an adequate benzodiazepine, promptly load a suitable second-line agent rather than repeatedly giving small unstructured doses. The team should pursue the cause, including metabolic, infectious, toxic and adherence-related triggers, in parallel.')],['ENLS'])

add('Status epilepticus: initial treatment','Intramuscular Midazolam Without IV Access',
 'A 75-kg adult is actively convulsing in the prehospital setting and IV access is not available. Which treatment is most appropriate now?',
 'Midazolam 10 mg intramuscularly',[
 ('Delay benzodiazepine until intravenous lorazepam can be obtained','A rapidly available non-IV benzodiazepine avoids treatment delay; waiting for a difficult IV can worsen seizure duration and responsiveness.'),
 ('Lorazepam 4 mg intramuscularly as the preferred rapid IM option','IM midazolam has more reliable rapid absorption for this emergency pathway; the established non-IV evidence does not simply substitute the IV lorazepam drug via any route.'),
 ('Diazepam 10 mg intramuscularly as the preferred rapid IM option','IM diazepam absorption is less reliable for rapid seizure termination. Rectal or IV diazepam has different practical roles, but midazolam is preferred for the specified IM approach.')],
 [S('Route Matters','**IM midazolam** is an effective early option when IV access is not established.',
    'A commonly used adult regimen is ==10 mg IM for weight above 40 kg==. Buccal or intranasal midazolam can also be used under an appropriate dose-specific protocol.',
    'RAMPART supported the practical effectiveness of prompt IM midazolam compared with IV lorazepam in prehospital convulsive status, partly by avoiding access delays.'),
  S('What Follows','**Continue resuscitation and obtain access** while reassessing whether convulsions stop.',
    'Maintain airway positioning and ventilation support, check glucose and prepare second-line therapy if needed. A non-IV first dose is the beginning of a coordinated pathway, not a reason to omit subsequent monitoring.',
    'Record any doses already given by family or emergency services to avoid inadvertent excessive repeat sedation. Seizure termination, respiratory assessment and cause identification remain the main immediate goals.')],['ENLS'])

add('Status epilepticus: established status','ESETT Second-Line Therapy',
 'Convulsive status persists after an adequate benzodiazepine. Which statement best reflects ESETT when choosing levetiracetam, fosphenytoin or valproate?',
 'The three regimens had similar overall efficacy; choose using patient-specific risks',[
 ('Levetiracetam was conclusively superior to both alternatives','ESETT did not establish superiority of levetiracetam; convenience and tolerability may favor it in some patients without proving greater average efficacy.'),
 ('Fosphenytoin was effective only in patients with normal structural MRI','MRI normality was not the defining basis for effectiveness; the emergency choice concerns suitable dosing, contraindications and the clinical situation.'),
 ('Valproate must be used first even in major hepatic or relevant mitochondrial disease','Valproate has important hepatic and POLG-related contraindications; similar trial efficacy cannot override a specific serious drug risk.')],
 [S('Trial Regimens','**ESETT** compared IV levetiracetam, fosphenytoin and valproate after benzodiazepine-refractory convulsive status.',
    'The studied loads were levetiracetam ==60 mg/kg, maximum 4500 mg==; fosphenytoin ==20 mg PE/kg, maximum 1500 mg PE==; and valproate ==40 mg/kg, maximum 3000 mg==, infused over 10 minutes in the trial.',
    'Approximately half responded under the trial endpoint, without a clear overall winner. Do not generalize an apparent numerical difference into proven superiority.'),
  S('Patient-Specific Choice','**Comorbidity and contraindications** determine which suitable agent to use promptly.',
    'Consider cardiac conduction and hypotension risk for fosphenytoin, hepatic or mitochondrial risks and reproductive context for valproate, and renal or behavioral history for levetiracetam.',
    'Maintenance adjustment differs from the initial emergency load. Persistent seizures despite an adequate benzodiazepine and second-line agent require refractory-status escalation and EEG-guided care, rather than prolonged indecision between trial-equivalent options.')],['ESETT','ENLS'])

add('Status epilepticus: established status','Fosphenytoin Units and Infusion Safety',
 'When ordering an IV fosphenytoin load for convulsive status, which prescription convention reduces a major dosing error?',
 'Express the dose and rate in phenytoin equivalents, with ECG and BP monitoring',[
 ('Use milligrams of fosphenytoin salt interchangeably with milligrams PE','The quantities are not interchangeable; ignoring the PE convention can produce a dosing error even though the drug is converted to phenytoin.'),
 ('Infuse the full load as an unrestricted rapid IV push','Fosphenytoin still has cardiovascular rate limits; a prodrug formulation does not remove the need for controlled administration and monitoring.'),
 ('Use oral maintenance phenytoin without a loading strategy for ongoing status','Maintenance absorption and timing do not provide the immediate exposure needed to treat continuing convulsive status; an emergency loading regimen is required.')],
 [S('Prescription and Dose','**Phenytoin equivalents (PE)** standardize fosphenytoin dosing to the active phenytoin amount.',
    'An emergency load is commonly ==20 mg PE/kg== under the relevant protocol. ESETT capped it at 1500 mg PE; other institutional or product regimens must be distinguished rather than assumed identical.',
    'The adult IV rate must not exceed the product-recommended maximum, commonly ==150 mg PE/min==, and may need to be slower in an at-risk patient.'),
  S('Monitoring and Comparison','**ECG, blood pressure and respiratory monitoring** are required during and after administration.',
    'Fosphenytoin generally causes less local tissue injury than alkaline IV phenytoin, but hypotension and arrhythmia remain possible. Significant conduction disease may favor a different second-line agent.',
    'After control, plan maintenance, consider drug interactions and interpret total versus free phenytoin levels appropriately. Distinguish an emergency loading dose, infusion rate and daily maintenance dose in every order.')],['ESETT','ENLS'],style='direct')

add('Status epilepticus: refractory status','Escalation After Two Treatment Stages',
 'Convulsive seizures continue after adequate IV lorazepam and an appropriate full IV second-line load. Which next strategy is most appropriate?',
 'Escalate to refractory-status care with airway management, continuous EEG and an anesthetic infusion as indicated',[
 ('Wait for a day before adding therapy because two agents have been given','Failure of the initial adequate stages establishes a time-critical refractory problem; untreated ongoing convulsions should not be observed for an arbitrary 24 hours.'),
 ('Use an oral third drug as the only immediate intervention','Oral therapy may contribute later but cannot be relied on as sole rapid treatment of ongoing refractory convulsive status with uncertain absorption and airway risk.'),
 ('Use neuromuscular paralysis alone as evidence of seizure control','Paralysis stops visible muscle activity without treating cortical seizures. Without EEG, ongoing electrical status can be concealed rather than terminated.')],
 [S('Refractory Definition','**Refractory status** persists despite an adequate benzodiazepine and a suitable adequately dosed second-line antiseizure agent.',
    'Early expert neurocritical involvement is necessary. Secure ventilation and hemodynamics and initiate continuous EEG when available; absence of visible movement after intubation or paralysis does not prove electrical seizure termination.',
    'Anesthetic options include midazolam or propofol, with other agents selected according to response, physiology and institutional expertise.'),
  S('Beyond Seizure Suppression','**Treat the precipitating disorder** while titrating the anesthetic to EEG and clinical goals.',
    'Maintain an appropriate longer-acting antiseizure regimen and investigate infection, toxic-metabolic causes, acute lesions and autoimmune disease when indicated. Deep sedation creates risks including hypotension and infection.',
    'Anesthetic dose and target are individualized; burst suppression is not a universal outcome-proven target for every patient. Prolonged or high-dose propofol requires attention to infusion-syndrome risk and systemic monitoring.')],['ENLS'])

add('Status epilepticus: EEG-guided care','Persistent Coma After Convulsive Seizures',
 'Generalized convulsions stop after treatment, but the patient remains unexpectedly unresponsive with intermittent eyelid twitching. CT and glucose do not explain the state. Which investigation is most important now?',
 'Urgent continuous EEG',[
 ('A repeat routine EEG the next week as an outpatient','Possible ongoing nonconvulsive status is an acute diagnosis; a deferred short recording cannot resolve the current unexplained coma or guide urgent treatment.'),
 ('Serum prolactin alone to establish termination','Prolactin does not reliably determine whether cortical electrical seizures are continuing and is especially limited after prolonged or repeated seizures.'),
 ('A normal oxygen saturation as sufficient confirmation of recovery','Adequate oxygenation is necessary but does not establish electrical seizure control; nonconvulsive status can persist despite acceptable respiratory measurements.')],
 [S('Electroclinical Dissociation','**Convulsive status can evolve into nonconvulsive status**, particularly after medication suppresses obvious movements.',
    'Persistent altered consciousness may also reflect the postictal state, sedative exposure, metabolic abnormalities or the underlying brain lesion. EEG helps distinguish these possibilities instead of assuming that every prolonged recovery is postictal.',
    'Subtle eyelid, facial or ocular movements are clues but are neither required nor sufficient for diagnosis.'),
  S('Interpretation and Treatment','**Continuous recording** can capture intermittent seizures and guide treatment response.',
    'Interpret rhythmic or periodic patterns using accepted electroclinical criteria, evolution, frequency and context. Not every periodic discharge warrants maximal anesthetic suppression, and treatment response must include clinical interpretation where possible.',
    'If an anesthetic or paralytic is used, ongoing EEG is particularly important. Continue airway, circulation and cause-directed care while assessment proceeds rather than postponing all treatment until a perfect recording is available.')],['ENLS'])

add('Status epilepticus: cause-specific treatment','Eclampsia-Associated Seizures',
 'At 34 weeks of pregnancy, a woman with severe hypertension and headache develops a generalized convulsion. Eclampsia is the leading diagnosis. Which drug is preferred for seizure treatment and recurrence prevention?',
 'Magnesium sulfate',[
 ('Phenytoin as the preferred specific eclampsia regimen','Phenytoin is used in some other seizure emergencies but is less effective than magnesium for eclamptic seizure prevention and is not the preferred specific regimen.'),
 ('Diazepam infusion as a routine replacement for magnesium','A benzodiazepine may be needed for persistent seizures or rescue, but it is not the preferred disease-specific treatment replacing magnesium in eclampsia.'),
 ('Levetiracetam monotherapy before any magnesium assessment','Levetiracetam can be useful when epilepsy or another cause is present or magnesium cannot be used, but it is not the standard preferred initial eclampsia-specific therapy.')],
 [S('Specific Anticonvulsant Regimen','**Magnesium sulfate** is first-line treatment for eclamptic seizures and prevention of recurrence.',
    'A commonly used IV regimen is ==4 g over 5–15 minutes, then 1 g/hour== under an obstetric protocol. Protocols differ, and maintenance commonly continues for 24 hours after the last seizure, with delivery timing also considered.',
    'Recurrent seizures may require an additional magnesium dose and reassessment; prolonged refractory convulsions still require airway support and additional rescue treatment.'),
  S('Monitoring and Definitive Care','**Respiratory rate, tendon reflexes and urine output** guide toxicity surveillance, with magnesium levels when clinically indicated.',
    'Renal impairment increases toxicity risk. Stop the infusion and treat clinically significant toxicity, commonly with IV calcium gluconate according to emergency protocol.',
    'Control severe pressure and arrange urgent obstetric management after maternal stabilization. Consider PRES and alternative intracranial causes, especially with focal signs, atypical timing or failure to improve; magnesium does not replace imaging when those features demand it.')],['ENLS'])

add('Status epilepticus: cause-specific treatment','Isoniazid-Induced Refractory Seizures',
 'After a suspected large isoniazid ingestion, a patient develops recurrent seizures and severe metabolic acidosis despite benzodiazepine treatment. Which antidote is required urgently?',
 'Pyridoxine',[
 ('Thiamine','Thiamine is important in deficiency and selected toxic-metabolic settings but does not reverse the pyridoxal-phosphate-related GABA deficiency caused by isoniazid.'),
 ('Folinic acid','Folinic acid has roles in selected antifolate or toxic-alcohol treatment contexts; it is not the specific replacement for isoniazid-related pyridoxine depletion.'),
 ('Hydroxocobalamin','Hydroxocobalamin is a cyanide antidote and does not correct the isoniazid mechanism, although both poisonings can produce severe acidosis and neurological collapse.')],
 [S('Toxic Mechanism','**Isoniazid** disrupts pyridoxine-dependent synthesis of the inhibitory transmitter GABA.',
    'The resulting seizures may resist standard drugs unless the cofactor deficiency is corrected. Marked lactic acidosis can accompany prolonged convulsions and poisoning.',
    'Pyridoxine is given in addition to airway care, benzodiazepines and correction of metabolic complications, not after exhausting every conventional antiseizure drug.'),
  S('Antidote Dosing','**Known ingestion** is treated with IV pyridoxine on a gram-for-gram basis matching the isoniazid amount under a toxicology protocol.',
    'When the dose is unknown, a commonly used initial adult dose is ==5 g IV==, with further dosing guided by seizure control and expert advice. Exact administration rate follows the acute poisoning protocol and clinical stability.',
    'Contact a poison service and verify availability early because high-dose supply may be limited. Assess coingestants, electrolytes, acid–base status and organ function; persistent severe toxicity may need further specialist-directed supportive or extracorporeal measures.')],['ENLS'])

R.update({
 'DRAVET':('Dravet Syndrome Foundation: diagnosis and treatment resources','https://dravetfoundation.org/hcp-resources/diagnosis-and-treatment/'),
 'LGS':('ILAE EpilepsyDiagnosis: Lennox–Gastaut EEG','https://www.epilepsydiagnosis.org/syndrome/lgs-eeg.html'),
 'PME':('ILAE variable-age epilepsy syndrome definitions, 2022','https://doi.org/10.1111/epi.17240'),
 'PRL':('AAN: Serum prolactin in diagnosing epileptic seizures, 2005','https://pubmed.ncbi.nlm.nih.gov/16157897/'),
 'LTG':('FDA Lamictal prescribing information, 2025','https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/020241s068s069%2C020764s061s062%2C022251s032s033lbl.pdf'),
 'CBZ':('DailyMed: carbamazepine prescribing information and HLA-B*15:02 warning','https://dailymed-beta.nlm.nih.gov/dailymed/drugInfo.cfm?setid=87d343a8-84d5-4cdd-b0a0-629311b51f11'),
 'PHT':('DailyMed: phenytoin prescribing information','https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=3bc82d23-3950-f181-e063-6394a90ad565'),
 'TPM':('DailyMed: topiramate prescribing information','https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=e4886adf-199d-4b19-a4ef-75f8f94cb54e'),
 'LCM':('DailyMed: lacosamide prescribing information','https://www.dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=d823fbfa-8ff5-4ef8-84ce-fbe916d4e430'),
 'LEV':('DailyMed: levetiracetam prescribing information','https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=7696961e-dfff-422a-b72f-e31ceeac10af'),
 'SURG':('ILAE consensus on timing of epilepsy surgery referral, 2022','https://pmc.ncbi.nlm.nih.gov/articles/PMC9562030/'),
 'SUDEP':('AES position statement on SUDEP counseling, 2019','https://www.ilae.org/files/ilaeGuideline/AES_SUDEP_Position_Statement_2019.pdf'),
 'RAMPART':('RAMPART: Intramuscular versus Intravenous Therapy for Prehospital Status Epilepticus, 2012','https://doi.org/10.1056/NEJMoa1107494'),
 'OBS':('NICE NG133: Hypertension in pregnancy, recommendations','https://www.nice.org.uk/guidance/ng133/chapter/recommendations'),
 'INH':('DailyMed: isoniazid prescribing information, overdose and pyridoxine','https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=0013c0c8-513a-48f3-a918-5bc1750c96a7'),
})
for n,key in {13:'DRAVET',14:'LGS',15:'PME',18:'PRL',19:'LTG',23:'LTG',24:'CBZ',25:'PHT',26:'TPM',27:'LCM',28:'LEV',30:'SURG',31:'SUDEP',34:'RAMPART',39:'OBS',40:'INH'}.items():rows[n-1]['refs'].append(key)
rows[34]['table']=(['ESETT agent','Studied IV load','Trial maximum'],[
 ['Levetiracetam','60 mg/kg','4500 mg'],['Fosphenytoin','20 mg PE/kg','1500 mg PE'],['Valproate','40 mg/kg','3000 mg']])
rows[13]['table']=(['Feature','Typical absence syndrome','Lennox–Gastaut'],[
 ['Absence pattern','Abrupt, brief; rapid recovery','Often atypical; other seizure types'],['Interictal EEG','Generalized around 3-Hz spike-wave','Generalized slow spike-wave <2.5 Hz'],
 ['Sleep EEG clue','No required tonic GPFA pattern','Generalized paroxysmal fast activity'],['Development','Usually normal at onset','Developmental/cognitive impairment common']])

# Keep each alternative within the clinical decision and remove treatment ambiguity.
rows[18]['question']='An adult with newly diagnosed focal epilepsy has depression and previously developed severe aggression on levetiracetam prescribed elsewhere. Slow titration is acceptable. Under NICE NG217, which listed option is the preferred remaining first-line monotherapy?'
rows[18]['others']=[
 ('Levetiracetam','This is normally a first-line focal option, but the documented prior severe behavioral reaction makes rechallenge less suitable than the other recommended first-line drug.'),
 ('Carbamazepine','It is effective for focal seizures, but NICE places it among subsequent monotherapy options after unsuccessful first-line choices; lamotrigine remains an untried first-line option here.'),
 ('Lacosamide','It is useful for focal epilepsy, but NICE positions monotherapy later in the sequence. The patient has not yet tried the remaining recommended first-line choice, lamotrigine.')]
rows[20]['question']='Which listed drug has broad-spectrum activity covering both typical absences and generalized tonic-clonic seizures, unlike an absence-specific drug or predominantly focal-seizure alternatives?'
rows[20]['style']='direct'
rows[23]['others']=[
 ('HLA-B*57:01 testing','This is important before abacavir in its relevant clinical context, but it does not substitute for HLA-B*15:02 screening before carbamazepine in an at-risk ancestry group.'),
 ('CYP2C9 genotyping as the only required cutaneous-risk test','CYP2C9 affects phenytoin metabolism and dosing; it is not the principal marker for carbamazepine-associated SJS/TEN risk tested in this question.'),
 ('HLA-A*31:01 testing instead of HLA-B*15:02 testing','HLA-A*31:01 has a real association with broader carbamazepine hypersensitivity, but it does not replace the HLA-B*15:02 assessment for the high-prevalence ancestry and SJS/TEN context specified.')]
rows[26]['others']=[
 ('QT prolongation with torsades de pointes as the characteristic effect','That pattern is important with several other medication classes, but lacosamide’s labeled dose-related conduction issue centers on the PR interval and AV conduction.'),
 ('QT shortening as the characteristic ECG effect','Short-QT concerns are more relevant to antiseizure agents such as rufinamide or cenobamate; they do not identify the major lacosamide warning in this case.'),
 ('Coronary vasospasm as the characteristic dose-related cardiac toxicity','Vasospastic ischemia has other drug causes, but it is not the characteristic lacosamide mechanism amplified by baseline AV delay and a conduction-slowing beta blocker.')]
rows[27]['others']=[
 ('Postictal psychosis as the primary explanation','Postictal psychosis usually has a temporal relationship to a seizure cluster, often with a lucid interval and psychotic features. New sustained irritability after drug initiation without that sequence favors medication toxicity.'),
 ('An ictal behavioral manifestation recurring throughout the day','Ictal behavior is usually episodic and stereotyped with a corresponding event pattern; a persistent new behavioral change after starting medication warrants a drug adverse-effect assessment.'),
 ('A newly progressive frontal-lobe disorder as the leading explanation','Frontal disease can alter behavior, but the close medication relationship and absence of other supporting progression make a recognized drug adverse effect the more immediate hypothesis to evaluate.')]

if __name__=='__main__':
    assert len(rows)==40,len(rows)
    save('Neurology',3,'03. Epilepsy & Status Epilepticus',rows,R,
      'Original postgraduate teaching synthesis. Current seizure terminology checked against ILAE 2025; diagnostic and treatment pathways checked against NICE NG217, AAN/AES guidance, official drug information and ENLS/ESETT. Regulatory requirements differ by jurisdiction, especially reproductive precautions. Full Harrison’s subscription text was not accessed. Source checking is not independent clinician validation.')
