"""Original movement-disorders and ataxias chapter; coverage-driven authoring."""
import json
from qbank_json_chapters import question as Q, save, ROOT
R = {
 'PDCR': ('MDS clinical diagnostic criteria for Parkinson disease, 2015', 'https://escholarship.org/uc/item/1zd719dv'),
 'PDSTAT': ('MDS position on clinical diagnosis of Parkinson disease', 'https://www.movementdisorders.org/MDS/News/Newsroom/Position-Papers/MDS-Position-Diagnosis-of-PD.htm'),
 'AAN': ('AAN guideline: Dopaminergic therapy for motor symptoms in early PD, 2021', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC8672433/'),
 'NICE': ('NICE NG71: Parkinson disease in adults, recommendations', 'https://www.nice.org.uk/guidance/ng71/chapter/Recommendations'),
 'PSP': ('MDS clinical diagnostic criteria for PSP, 2017', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5516529/'),
 'MSA': ('MDS diagnostic criteria for multiple system atrophy, 2022', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9321158/'),
 'TREM': ('MDS consensus classification of tremors, 2018', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6530552/'),
 'ATAX': ('Guidelines on diagnosis and management of progressive ataxias, 2019', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6381619/'),
 'RBD': ('AASM REM sleep behavior disorder management guideline, 2023', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC10071384/'),
 'INFUSE': ('FDA foscarbidopa/foslevodopa subcutaneous infusion label, 2024', 'https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/216962s000lbl.pdf'),
}
def S(h, main, *children): return (h, [(main, list(children))])
rows = []
def add(*a, **kw): rows.append(Q(*a, **kw))

add('Parkinson disease', 'Establishing Motor Parkinsonism',
 'Which examination combination satisfies the MDS motor definition of parkinsonism?',
 'Bradykinesia with rigidity or rest tremor', [
 ('Rest tremor and postural instability without bradykinesia', 'Tremor and imbalance warrant evaluation but do not fulfill the MDS prerequisite without bradykinesia; tremor can arise from several other syndromes.'),
 ('Rigidity and reduced arm swing without bradykinesia', 'Rigidity and reduced arm swing support suspicion, but the formal motor definition still requires bradykinesia rather than these two features alone.'),
 ('Action tremor and impaired tandem gait without bradykinesia', 'Action tremor with tandem difficulty may indicate a tremor/ataxia syndrome and requires a different assessment; it does not establish parkinsonism.')],
 [S('Required Motor Finding', '**Bradykinesia** means slowness with progressive reduction in amplitude or speed, or progressive hesitations/halts, during repetitive movement. Assess finger tapping, hand opening, pronation–supination and foot movements.',
    'The MDS definition requires bradykinesia plus either rigidity or rest tremor. A resting tremor is therefore not mandatory, and a tremor alone is insufficient.',
    'Pain, weakness, apraxia and poor comprehension may slow performance without producing genuine parkinsonian bradykinesia; interpret the pattern rather than speed alone.'),
  S('Syndrome Versus Cause', '**Parkinsonism is a clinical syndrome.** Establishing it does not by itself distinguish Parkinson disease from MSA, PSP, drug-induced disease or other etiologies.',
    'After confirming the motor syndrome, review exclusions, red flags and supportive findings. A sustained clear dopaminergic response and asymmetric onset are useful in context, while early severe autonomic failure, gaze palsy or rapid progression demand reassessment.',
    'Postural instability often develops later in PD and is not part of the required core definition. Early recurrent falls should not be used as a shortcut to uncomplicated PD.')], ['PDCR','PDSTAT'], style='direct')

add('Parkinson disease', 'Exclusion Criteria Versus Red Flags',
 'Which finding is an absolute exclusion for Parkinson disease under the 2015 MDS clinical criteria rather than merely a red flag?',
 'Downward vertical supranuclear gaze palsy', [
 ('Recurrent falls from impaired balance within three years of onset', 'Early recurrent falls are a red flag requiring appropriate counterbalancing support for probable PD; they also raise particular concern for PSP.'),
 ('Severe autonomic failure within the first five years', 'Early severe autonomic failure is a red flag for alternative disease, especially MSA, but is distinguished from an absolute exclusion in the MDS classification.'),
 ('Bilateral symmetric parkinsonism throughout the course', 'Persistent symmetry is a red flag and should prompt review for secondary causes, but the MDS list classifies it differently from a vertical supranuclear gaze palsy.')],
 [S('Three Evidence Categories', '**Absolute exclusions** preclude a PD diagnosis under the specified criteria. Downward vertical supranuclear gaze palsy or selective slowing of downward vertical saccades is one such exclusion.',
    'Other exclusions include unequivocal cerebellar abnormalities, a plausible dopamine-blocker exposure explaining the syndrome, clear cortical sensory/apraxic features, and normal presynaptic dopaminergic functional imaging if that test has been performed.',
    'Clinical interpretation and test quality matter. The criteria are not a substitute for verifying that the apparent sign is genuine and has the stated anatomical meaning.'),
  S('Established and Probable PD', '**Clinically established PD** requires no absolute exclusions, at least two supportive criteria and no red flags. **Clinically probable PD** permits up to two red flags if each is counterbalanced by a supportive feature.',
    'Supportive evidence includes a clear dramatic dopaminergic response, levodopa-induced dyskinesia, limb rest tremor and selected validated olfactory or cardiac sympathetic findings.',
    'Early falls, severe early autonomic failure or rapid progression are clinically important even when not formally absolute exclusions. Their presence should trigger active review of alternative degenerative and secondary causes.')], ['PDCR'], style='direct')

add('Parkinson disease', 'What Dopamine-Transporter Imaging Can Establish',
 'A patient with uncertain tremor has reduced striatal uptake on dopamine-transporter SPECT. Which interpretation is most appropriate?',
 'Presynaptic nigrostriatal dysfunction is supported, but the scan does not reliably distinguish PD from MSA or PSP', [
 ('The scan identifies idiopathic PD with pathological certainty', 'Reduced uptake occurs in several degenerative parkinsonian syndromes; it is not a direct assay of Lewy bodies or a specific pathological diagnosis of PD.'),
 ('The result is the characteristic normal scan expected in pure essential tremor', 'Pure essential tremor generally preserves presynaptic dopaminergic imaging; reduced uptake should prompt assessment for a degenerative dopaminergic deficit or another explanation.'),
 ('The scan measures only postsynaptic dopamine-receptor density', 'Dopamine-transporter SPECT assesses presynaptic transporter binding, unlike imaging methods designed to assess postsynaptic receptor function.')],
 [S('Presynaptic Imaging', '**Dopamine-transporter SPECT** evaluates striatal presynaptic dopaminergic terminal function. It can help when clinical examination cannot confidently separate essential tremor from a parkinsonian syndrome.',
    'Reduced uptake can occur in PD, MSA, PSP and other degenerative parkinsonian disorders. Clinical phenotype and longitudinal observation remain necessary for etiologic classification.',
    'A scan is not routinely required when the clinical diagnosis is clear. Review interfering drugs, acquisition quality and specialist interpretation when results conflict with the examination.'),
  S('Appropriate Differential Use', '**Pure drug-induced parkinsonism and essential tremor** often have preserved presynaptic uptake. An abnormal scan in a dopamine-blocker-exposed patient may suggest unmasked underlying degeneration rather than a purely pharmacological syndrome.',
    'Under the 2015 MDS criteria, normal presynaptic functional imaging, if performed and technically reliable, is an exclusion for clinical PD; this does not mean everyone needs a scan.',
    'The test does not replace MRI for a suspected structural or vascular cause and does not provide a stand-alone explanation for gait disturbance, autonomic failure or cognitive symptoms.')], ['PDCR','NICE'])

R.update({
 'PRKN': ('GeneReviews: PRKN-related early-onset Parkinson disease, updated 2026', 'https://www.ncbi.nlm.nih.gov/books/NBK1478/'),
 'SIN': ('Sinemet immediate-release prescribing information, 2026', 'https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/017555s076lbl.pdf'),
 'RAS': ('Rasagiline prescribing information', 'https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=68cef20f-10c0-475e-af95-b7799355c7e9'),
 'OPI': ('Opicapone prescribing information, 2025', 'https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212489s011lbl.pdf'),
 'LEAP': ('LEAP randomized delayed-start levodopa trial, 2019', 'https://www.nejm.org/doi/10.1056/NEJMoa1809983'),
 'DBS': ('Congress of Neurological Surgeons evidence-based STN versus GPi DBS guideline, 2018', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6636249/'),
})

add('Parkinson disease', 'Early-Onset Recessive Parkinsonism',
 'Two siblings born to unaffected consanguineous parents develop levodopa-responsive parkinsonism in their twenties, with early foot dystonia and treatment-related dyskinesia. Which genetic context best fits?',
 'Biallelic pathogenic PRKN variants', [
 ('A heterozygous pathogenic LRRK2 variant', 'LRRK2 commonly causes dominant, incompletely penetrant PD, often later onset; it is less consistent with this strongly recessive very-early-onset pedigree.'),
 ('An autosomal dominant SNCA multiplication', 'SNCA duplications or triplications can cause dominant parkinsonism, sometimes with prominent cognitive/autonomic disease, but do not best match unaffected consanguineous parents and affected siblings.'),
 ('A heterozygous GBA1 susceptibility variant as a fully penetrant recessive cause', 'GBA1 variants increase PD risk with incomplete penetrance; one variant does not constitute the biallelic recessive mechanism suggested by this pedigree.')],
 [S('Pedigree and Phenotype', '**PRKN-related disease** is an important cause of early-onset recessive parkinsonism. Foot dystonia, a good levodopa response and early motor complications can be prominent.',
    'PINK1 and PARK7 also cause recessive early-onset forms. A phenotype and pedigree guide testing but do not identify a gene with certainty; molecular confirmation is needed.',
    'Testing should detect relevant sequence variants and deletions/duplications where indicated. A single PRKN variant does not automatically establish biallelic disease.'),
  S('Counselling and Management', '**Genetic counselling** should accompany testing and interpretation. For confirmed recessive disease with both parents carrying a pathogenic allele, each full sibling has a 25% probability of being affected at conception.',
    'Dominant genes such as LRRK2 and SNCA and risk-associated genes such as GBA1 have different penetrance and family implications. A risk variant must not be described as a deterministic diagnosis.',
    'Treat motor symptoms according to functional needs while anticipating dyskinesia and fluctuations. Genotype may inform trial eligibility and prognosis, but does not justify claiming an established curative gene-specific therapy.')], ['PRKN'])

add('Parkinson disease', 'Choosing Initial Dopaminergic Treatment',
 'A 72-year-old with newly diagnosed PD has bradykinesia and rigidity interfering with dressing and walking. He has mild orthostatic symptoms and is concerned about hallucinations. Which initial motor treatment is generally preferred?',
 'Low-dose immediate-release carbidopa–levodopa, titrated to benefit', [
 ('Pramipexole as the default because levodopa must be delayed for neuroprotection', 'Dopamine agonists may suit selected younger patients, but older age increases hallucination, sleepiness and behavioral risks; delaying levodopa is not an established neuroprotective strategy.'),
 ('Trihexyphenidyl as the preferred treatment for gait and rigidity at this age', 'Anticholinergics occasionally help tremor in selected younger patients, but cognitive, urinary and autonomic toxicity make them a poor first choice for this older patient.'),
 ('Rasagiline alone irrespective of the functional burden', 'MAO-B monotherapy may suit mild symptoms, but levodopa generally provides greater motor benefit when symptoms significantly affect daily function.')],
 [S('Benefit–Risk Selection', '**Levodopa provides the greatest symptomatic motor benefit** and is the AAN-preferred initial dopaminergic treatment for patients seeking treatment of early motor symptoms. NICE recommends offering it when motor symptoms affect quality of life.',
    'Use immediate-release treatment initially at the lowest effective dose and titrate according to function and adverse effects. Older patients are particularly vulnerable to dopamine-agonist hallucinations, sudden sleep and orthostatic effects.',
    'Discuss nausea, hypotension, hallucinations and later motor complications rather than implying levodopa has no risks.'),
  S('Timing and Disease Modification', '**The LEAP delayed-start trial did not establish a disease-modifying effect** of early levodopa over the studied period. Neither neuroprotection from starting nor protection from delaying treatment should be asserted.',
    'Treatment timing is driven by functional burden, patient priorities and tolerability. Exercise, physiotherapy and occupational strategies accompany medication.',
    'Dyskinesia risk relates to several factors, including age at onset, disease duration and levodopa exposure. Fear of future dyskinesia should not leave a currently disabled patient inadequately treated.')], ['AAN','NICE','LEAP'])

add('Parkinson disease', 'Carbidopa–Levodopa Pharmacology',
 'Why is carbidopa combined with levodopa?',
 'It inhibits peripheral aromatic L-amino-acid decarboxylase, increasing levodopa available to the brain', [
 ('It selectively blocks dopamine receptors in the striatum', 'Striatal dopamine-receptor blockade can worsen parkinsonism; carbidopa instead reduces peripheral conversion of the dopamine precursor.'),
 ('It inhibits central MAO-B as its primary action', 'Central MAO-B inhibition describes rasagiline or selegiline, not the mechanism of carbidopa.'),
 ('It directly stimulates dopamine receptors without metabolic conversion', 'Direct receptor stimulation describes dopamine agonists. Levodopa is a precursor, while carbidopa preserves its availability through peripheral enzyme inhibition.')],
 [S('Peripheral Decarboxylation', '**Carbidopa has little CNS penetration** and inhibits peripheral conversion of levodopa to dopamine. This reduces peripheral adverse effects and the levodopa dose needed for a central effect.',
    'Levodopa crosses the blood–brain barrier and is converted to dopamine within the CNS. Dopamine itself does not cross the barrier effectively.',
    'A common adult immediate-release starting regimen is carbidopa/levodopa 25/100 mg three times daily, adjusted to frailty and response. Approximately 70–100 mg/day of carbidopa is generally needed for effective peripheral enzyme inhibition.'),
  S('Absorption and Safety', '**Large neutral amino acids** can compete with levodopa transport, while delayed gastric emptying can make response unpredictable. Review meal timing and protein redistribution when clinically important fluctuations occur.',
    'Do not advise indiscriminate protein restriction or malnutrition. Taking a dose with a small nonprotein snack can improve nausea when an empty stomach is poorly tolerated.',
    'Monitor postural symptoms, nausea, hallucinations, dyskinesia and wearing-off. Dopamine-blocking antiemetics such as metoclopramide can worsen motor function; choose an appropriate alternative after reviewing cardiac and interaction risks.')], ['SIN','AAN'], style='direct')

add('Parkinson disease', 'Dopamine-Agonist Impulse-Control Disorder',
 'A man taking pramipexole develops compulsive online gambling and uncontrolled spending. Motor symptoms are otherwise stable. What is the best management principle?',
 'Discuss the behavior directly and gradually reduce the dopamine agonist with specialist supervision', [
 ('Increase pramipexole to suppress an assumed nonmotor OFF symptom', 'Agonist-associated impulse-control behavior is a treatment adverse effect; increasing exposure can worsen it rather than treating a dopaminergic deficit.'),
 ('Stop all dopaminergic drugs abruptly without a replacement plan', 'Agonist reduction is appropriate, but abrupt withdrawal can cause a severe withdrawal syndrome and loss of motor control; the transition requires a monitored plan.'),
 ('Continue the agonist unchanged and rely only on financial counselling', 'Practical safeguards and counselling help, but do not adequately address the causal medication exposure when a serious treatment-associated impulse-control disorder is present.')],
 [S('Behavioral Toxicity', '**Dopamine agonists** can cause gambling, hypersexuality, compulsive shopping and binge eating. Ask patients and, with consent, carers directly because embarrassment and poor insight can conceal symptoms.',
    'Risk is not confined to one agonist. Sleepiness, sudden sleep attacks, hallucinations, edema and orthostatic hypotension are additional important effects.',
    'Older age, cognitive impairment, hallucinations or excessive daytime sleepiness may make an agonist a poor initial choice; younger age does not eliminate behavioral risk.'),
  S('Taper and Motor Rebalancing', '**Gradual specialist-guided agonist reduction** is usually the key intervention, with adjustment of levodopa or other therapy to maintain function.',
    'Monitor for dopamine-agonist withdrawal syndrome, which may include anxiety, dysphoria, fatigue, pain and autonomic symptoms and may not respond fully to levodopa substitution.',
    'Use shared decisions, behavioral support and practical protection from financial or interpersonal harm. Counsel about driving if sleep attacks occur and document the treatment–behavior relationship during follow-up.')], ['AAN','NICE'])

add('Parkinson disease', 'Rasagiline and Interacting Analgesics',
 'A patient taking rasagiline needs an analgesic review. Which listed drug is contraindicated with rasagiline because of a serious interaction risk?',
 'Tramadol', [
 ('Paracetamol', 'Paracetamol can be appropriate for nociceptive pain when liver-related dosing limits are respected; it does not have the specific serotonergic opioid interaction of tramadol.'),
 ('Topical diclofenac', 'Topical diclofenac may suit localized musculoskeletal pain, subject to NSAID precautions; it does not share the MAO-inhibitor interaction specified for tramadol.'),
 ('Lidocaine patch', 'A topical lidocaine preparation can help selected localized neuropathic pain and does not share tramadol’s serotonergic interaction mechanism.')],
 [S('Selective MAO-B Inhibition', '**Rasagiline inhibits MAO-B** at recommended doses, reducing dopamine breakdown. It may be used for mild early symptoms or as an adjunct for motor fluctuations.',
    'Usual monotherapy dosing is 1 mg orally daily. Lower dosing is used in specified adjunctive or interaction contexts; with ciprofloxacin or another CYP1A2 inhibitor, the cited label limits dosing to 0.5 mg/day.',
    'Selectivity is dose dependent, so exceeding recommended doses adds risk rather than providing a safe shortcut to greater benefit.'),
  S('Interaction Review', '**Tramadol, meperidine and certain other opioids are contraindicated** because of serotonin-syndrome risk. Dextromethorphan and other MAO inhibitors also require avoidance under the label.',
    'The cited US labeling requires at least fourteen days between stopping rasagiline and initiating specified contraindicated drugs. Antidepressant combinations and washout intervals need drug-specific review; fluoxetine persistence can require a longer interval in the opposite direction.',
    'Fever, agitation, autonomic instability, clonus and hyperreflexia suggest serotonin toxicity. A medication review should include over-the-counter cough remedies as well as prescribed analgesics.')], ['RAS'], style='direct')

add('Parkinson disease', 'COMT Inhibitors as Levodopa Adjuncts',
 'Which COMT-inhibitor comparison is correct for PD motor fluctuations?',
 'Opicapone is a once-daily adjunct; tolcapone requires particular attention to serious hepatotoxicity', [
 ('Entacapone replaces levodopa by directly stimulating dopamine receptors', 'Entacapone prolongs levodopa availability through peripheral COMT inhibition; it is an adjunct rather than a direct dopamine-receptor agonist or levodopa replacement.'),
 ('Tolcapone has no central action and no clinically important liver concern', 'Tolcapone acts centrally and peripherally and carries serious hepatic risk; the absence of such risk cannot be assumed from the shared COMT drug class.'),
 ('Opicapone is routinely taken with every individual levodopa dose', 'Entacapone is commonly paired with individual levodopa doses; opicapone provides prolonged inhibition with once-daily administration.')],
 [S('Prolonging Levodopa Exposure', '**COMT inhibitors reduce levodopa metabolism** and can shorten OFF time when added to carbidopa–levodopa. They do not treat PD effectively as stand-alone replacements for levodopa.',
    'Entacapone is commonly given as 200 mg with each levodopa dose, within the applicable daily maximum. Opicapone is commonly 50 mg once daily at bedtime under the cited US label.',
    'The opicapone label advises no food for one hour before and at least one hour after dosing. Moderate hepatic impairment requires a lower dose and severe impairment should be avoided under that label.'),
  S('Adverse Effects and Selection', '**Dyskinesia can increase** because levodopa exposure rises; reducing the levodopa dose may be necessary. Hallucinations and hypotension can also worsen.',
    'Entacapone can cause diarrhea and benign urine discoloration. Tolcapone has a restricted role because potentially fatal hepatic injury requires careful eligibility, consent and liver monitoring.',
    'Select an adjunct according to OFF burden, dosing convenience, cognitive/psychiatric effects, liver status and access rather than assuming all COMT inhibitors have identical pharmacology or safety.')], ['OPI','NICE'], style='direct')

add('Parkinson disease', 'Predictable End-of-Dose Wearing-Off',
 'A patient taking carbidopa–levodopa every five hours reliably becomes slow and rigid during the last hour before each dose, then improves after the next dose. There is little troublesome dyskinesia. Which strategy best addresses the pattern?',
 'Reduce gaps in levodopa coverage and consider a suitable OFF-reducing adjunct', [
 ('Lower every levodopa dose while keeping the five-hour gaps unchanged', 'Lowering individual doses can help peak-dose dyskinesia, but without improving coverage may worsen predictable end-of-dose loss of benefit.'),
 ('Add amantadine solely because this pattern proves peak-dose dyskinesia', 'Amantadine is useful for dyskinesia in selected patients, but the described slowness before the next dose is an OFF phenomenon rather than excess peak-dose movement.'),
 ('Treat the episodes as established levodopa-resistant gait failure without a diary', 'Levodopa-resistant axial disease is a different problem; the reproducible improvement after each dose supports a medication-state relationship that should be characterized and optimized.')],
 [S('Recognizing the Motor State', '**Wearing-off** is a predictable decline in benefit as a levodopa dose’s effect wanes. A medication and symptom diary helps separate it from delayed ON, unpredictable OFF and dyskinesia.',
    'Options include smaller, more frequent levodopa doses, an appropriate formulation change or addition of a COMT inhibitor, MAO-B inhibitor or selected dopamine agonist.',
    'Review adherence, constipation/gastric emptying and meal-related absorption before attributing every fluctuation to disease progression.'),
  S('Tailoring the Adjunct', '**Cognitive, behavioral and autonomic risks** influence treatment choice. An agonist may be unsuitable with hallucinations, sleep attacks or impulse-control vulnerability.',
    'Adding an exposure-prolonging drug may uncover dyskinesia, requiring levodopa adjustment. Patients need a clear dosing schedule and follow-up rather than several unsupervised simultaneous changes.',
    'Persistent disabling fluctuations despite optimized oral treatment justify evaluation for device-aided therapy or DBS in suitable patients. These options target motor-state variability and do not provide a cure for the underlying disease.')], ['NICE','AAN'])

R.update({
 'PIMA': ('Pimavanserin prescribing information, 2026', 'https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/207318s016lbl.pdf'),
 'CLOZ': ('FDA removal of clozapine REMS with continuing ANC-monitoring advice, 2025', 'https://www.fda.gov/drugs/drug-safety-communications/fda-removes-risk-evaluation-and-mitigation-strategy-rems-program-antipsychotic-drug-clozapine'),
 'MIDO': ('Midodrine summary of product characteristics', 'https://www.medicines.org.uk/emc/product/15179/smpc'),
 'CRISIS': ('German Society of Neurology guideline: akinetic crisis and withdrawal syndromes, 2024', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11447035/'),
})

add('Parkinson disease', 'Peak-Dose Dyskinesia',
 'A levodopa-treated patient develops flowing choreiform movements when mobility is otherwise best, approximately one hour after each dose. There is no confusion. Which strategy most directly addresses this pattern?',
 'Reduce individual levodopa peaks and consider amantadine if troublesome dyskinesia persists', [
 ('Increase each levodopa dose to treat presumed end-of-dose OFF dystonia', 'Painful OFF dystonia occurs during low dopaminergic states, whereas the timing during maximal benefit supports peak-dose dyskinesia that may worsen with larger peaks.'),
 ('Add a COMT inhibitor without reviewing the levodopa dose', 'A COMT inhibitor can reduce OFF time, but can intensify dyskinesia through greater levodopa exposure unless the regimen is adjusted.'),
 ('Use an anticholinergic as the preferred treatment for generalized peak-dose chorea', 'Anticholinergics have a limited role in selected tremor-predominant young patients and dystonia contexts; they are not the preferred treatment for levodopa-induced peak-dose dyskinesia.')],
 [S('Motor-State Classification', '**Peak-dose dyskinesia** commonly consists of choreiform movements during high levodopa effect. Distinguish it from diphasic dyskinesia during rising/falling levels and painful dystonia during OFF periods.',
    'Smaller individual doses with a revised schedule can lower peaks while preserving useful ON time. Review adjuncts that prolong or intensify levodopa exposure.',
    'The aim is functional good ON time, not elimination of every visible movement at the cost of disabling immobility.'),
  S('Amantadine and Escalation', '**Amantadine can reduce troublesome dyskinesia**, with NMDA-receptor antagonism among its relevant actions. Immediate-release regimens often start at 100 mg daily and may increase to 100 mg twice daily when appropriate.',
    'Renal function, age and the specific formulation determine dosing; immediate- and extended-release preparations are not milligram-for-milligram interchangeable. Monitor hallucinations, confusion, edema and livedo reticularis.',
    'If oral optimization fails, consider appropriate DBS or infusion therapy after specialist assessment. Cognitive vulnerability may limit amantadine and also affects eligibility for invasive treatment.')], ['NICE','AAN'])

add('Parkinson disease', 'Freezing of Gait and Medication State',
 'A patient freezes mainly at doorways during the hour before levodopa, but freezing improves after the next dose. Which approach is most appropriate?',
 'Optimize OFF coverage and combine it with cueing-based gait rehabilitation', [
 ('Assume every freezing episode is levodopa resistant and avoid medication review', 'Some freezing becomes levodopa resistant, particularly later axial disease, but the reproducible OFF relationship here supports optimizing dopaminergic coverage.'),
 ('Increase levodopa indefinitely even if freezing later persists during good ON periods', 'ON-state resistant freezing may not improve with further dopaminergic escalation, which can add dyskinesia or hallucinations; reassess phenotype and nonpharmacological strategies.'),
 ('Use DBS solely for levodopa-resistant postural instability without a broader assessment', 'Standard DBS most reliably improves levodopa-responsive motor symptoms and selected tremor; resistant balance and gait failure alone are poor indications.')],
 [S('State-Dependent Gait Failure', '**OFF-related freezing** can improve when levodopa coverage is optimized. Record timing, triggers, turning, dual-task effects and the patient’s ON/OFF response.',
    'Doorways and turning are common triggers. Visual floor markings, rhythmic auditory cues, deliberate weight shifting and physiotherapy can help selected patients.',
    'Assess orthostatic hypotension, neuropathy, vision, cognition, footwear and environmental hazards because gait disability may have several simultaneous causes.'),
  S('Limits of Dopaminergic Escalation', '**Late axial dysfunction may become poorly levodopa responsive.** Persistent freezing or falls during a genuinely good ON state needs a separate assessment rather than automatic repeated dose escalation.',
    'DBS is not a dependable treatment for all balance and speech problems and can sometimes worsen them. Preoperative levodopa response and neuropsychological assessment are therefore essential.',
    'Falls prevention, an appropriate walking aid and home assessment remain important even when medication-state optimization helps. A treatment plan should measure actual walking safety and independence, not only limb motor scores.')], ['NICE','DBS'])

add('Parkinson disease', 'Selecting a DBS Candidate',
 'Which patient is the best candidate for a DBS assessment?',
 'A cognitively intact patient with clear levodopa responsiveness and disabling fluctuations despite optimized therapy', [
 ('A patient with severe dementia and recurrent uncontrolled hallucinations', 'Dementia and unstable psychosis substantially increase surgical and postoperative risk and usually preclude standard DBS selection despite severe motor disability.'),
 ('A patient with early falls, vertical gaze palsy and minimal levodopa response', 'That phenotype suggests atypical parkinsonism such as PSP, in which standard PD DBS generally does not provide the expected benefit.'),
 ('A patient whose main disability is levodopa-resistant speech and postural instability', 'Levodopa-resistant axial deficits are less reliably improved and may worsen after stimulation; they are not a strong stand-alone indication for standard DBS.')],
 [S('What Surgery Can Improve', '**Levodopa-responsive motor symptoms**, motor fluctuations and troublesome dyskinesia are central indications for DBS in appropriately selected PD. Medication-resistant tremor is an important special case that can still respond.',
    'Evaluate the diagnosis, documented medication response, realistic goals, MRI, surgical risk, support and ability to attend programming visits.',
    'A motor challenge is informative but not the sole selection test. Severe disability alone does not establish that the disability is stimulation responsive.'),
  S('Cognitive and Psychiatric Assessment', '**Dementia, uncontrolled psychosis and unstable major psychiatric illness** are major concerns. Formal neuropsychological assessment helps identify vulnerabilities and guide selection.',
    'DBS does not stop neurodegeneration or reliably prevent later cognitive, autonomic and axial complications. Explain the distinction between symptomatic benefit and disease modification.',
    'Postoperative programming and medication adjustment are part of treatment. Device care, battery management and avoidance of abrupt treatment interruptions are important to sustaining benefit safely.')], ['DBS','NICE'])

add('Parkinson disease', 'Choosing STN Versus GPi Stimulation',
 'A suitable PD DBS candidate has troublesome dyskinesia and mild cognitive vulnerability. Medication reduction is not a primary goal. Which target is generally favored for discussion?',
 'Globus pallidus internus', [
 ('Subthalamic nucleus specifically because it has no cognitive trade-off', 'STN can provide strong motor benefit and greater medication reduction, but cognitive and mood concerns can favor GPi when those risks are important.'),
 ('Ventral intermediate thalamus as the preferred target for all fluctuations and dyskinesia', 'VIM stimulation can treat tremor but does not provide the same broad control of bradykinesia, rigidity and motor complications as STN or GPi in this setting.'),
 ('Ablation of both thalami as the usual first choice for this cognitive profile', 'Lesional thalamic procedures have selected tremor indications, but bilateral destructive treatment carries important speech and balance risks and is not the preferred approach to this broader PD problem.')],
 [S('Goal-Directed Target Selection', '**STN and GPi DBS both improve PD motor symptoms** in suitable patients. CNS guidance favors STN when reduction of dopaminergic medication is the principal goal.',
    'When medication reduction is not anticipated and the goal is to reduce ON-medication dyskinesia, GPi can be favored. Concern about cognitive decline or depression also supports considering GPi.',
    'These are evidence-informed tendencies, not a guarantee that one target has no cognitive or psychiatric adverse effects.'),
  S('Individualized Trade-offs', '**Formal cognitive and psychiatric assessment** remains essential before choosing either target. Mild vulnerability and established dementia are different clinical situations; the latter may exclude DBS entirely.',
    'Consider tremor, bradykinesia, gait response, dyskinesia, medication toxicity and the patient’s priorities together. VIM is useful principally for tremor rather than comprehensive PD motor-state control.',
    'Programming, lead placement and postoperative medication management affect outcome substantially. Target choice does not make levodopa-resistant balance, speech or cognitive symptoms predictably responsive.')], ['DBS'])

add('Parkinson disease', 'Persistent Parkinson Disease Psychosis',
 'A patient with PD has distressing persistent visual hallucinations after infection, delirium and vision problems are assessed and unnecessary provoking drugs are reduced. Motor function is fragile. Which option has a specific US indication for PD hallucinations and delusions without dopamine-receptor blockade?',
 'Pimavanserin', [
 ('Risperidone', 'Risperidone can treat psychosis in other settings but its dopamine D2 blockade can substantially worsen parkinsonism, making it poorly suited to this fragile motor state.'),
 ('Olanzapine', 'Olanzapine has antipsychotic efficacy in other disorders but can worsen PD motor function and is not recommended as a routine PD psychosis solution.'),
 ('Haloperidol', 'Haloperidol is a potent dopamine blocker used in selected acute psychiatric contexts; it risks marked motor deterioration in PD and does not match the mechanism requested.')],
 [S('Medication and Medical Review', '**Look for delirium, infection, metabolic disturbance and medication toxicity** before labeling symptoms as chronic PD psychosis. If symptoms are benign and insight is preserved, medication may not always be required.',
    'Simplify provoking medications cautiously with specialist input, balancing hallucination control against immobility. Abrupt removal of all dopaminergic therapy is unsafe.',
    'Treat persistent distress or risk through a shared plan with the patient and carers, and assess cognitive status because it influences treatment and prognosis.'),
  S('Antipsychotic Choices', '**Pimavanserin acts mainly as a 5-HT2A inverse agonist** and has a US indication for hallucinations and delusions associated with PD psychosis. The usual label dose is 34 mg once daily; QT prolongation and CYP3A4 interactions require review.',
    'Low-dose clozapine has strong efficacy evidence but requires blood-count monitoring and attention to orthostasis, myocarditis and other toxicity. The FDA removed the US REMS programme in 2025 while continuing to recommend ANC monitoring according to labeling.',
    'Quetiapine is sometimes used, although efficacy evidence is less robust and sedation/hypotension matter. Local approval and access differ; antipsychotics also carry mortality warnings in older patients with dementia-related psychosis.')], ['PIMA','CLOZ','NICE'])

add('Parkinson disease', 'Neurogenic Orthostatic Hypotension',
 'A patient with PD has symptomatic orthostatic hypotension despite hydration, medication review and compression measures. Which pharmacological plan is appropriate to consider?',
 'Daytime midodrine with supine and standing BP monitoring and avoidance near bedtime', [
 ('Bedtime midodrine as the main dose regardless of supine blood pressure', 'Midodrine can cause substantial supine hypertension; dosing close to lying down increases that risk rather than targeting daytime orthostatic symptoms.'),
 ('Fludrocortisone without monitoring potassium, edema or heart failure', 'Fludrocortisone can be useful in selected patients, but volume expansion can cause hypokalemia, edema and supine hypertension and can aggravate heart failure.'),
 ('Increase a diuretic as the routine treatment for the postural symptoms', 'A diuretic may be needed for another condition, but volume depletion can worsen orthostatic hypotension and should be reviewed rather than reflexively increased.')],
 [S('Identify the Mechanism', '**Neurogenic orthostatic hypotension** reflects impaired autonomic BP compensation. Measure supine and standing BP and HR, and assess dehydration, anemia and medication effects before assuming all postural dizziness is neurogenic.',
    'A fall of at least 20 mmHg systolic or 10 mmHg diastolic within three minutes is the conventional OH threshold. A blunted HR response supports a neurogenic mechanism, interpreted in light of beta-blockers and rhythm disease.',
    'Use fluid/salt measures when safe, slower position changes, abdominal compression and head-up sleeping as appropriate.'),
  S('Pressor Therapy', '**Midodrine is an alpha-1 agonist prodrug.** A common initiation is 2.5 mg two or three times daily, titrated according to symptoms and BP, up to 10 mg three times daily under the cited SmPC.',
    'Take the last dose at least four hours before bedtime and monitor supine hypertension, urinary retention and other adverse effects. Contraindications and renal status require review.',
    'Droxidopa is an alternative where available; fludrocortisone is an off-label volume-expanding option in many settings. Treatment should improve standing function without creating dangerous supine hypertension.')], ['MIDO','NICE'])

add('Parkinson disease', 'REM Sleep Behavior Disorder',
 'A man with PD punches and kicks while apparently acting out dreams. Which investigation best supports definite REM sleep behavior disorder and helps exclude mimics?',
 'Video polysomnography demonstrating REM sleep without normal muscle atonia', [
 ('A daytime routine EEG alone', 'EEG can help when epilepsy is suspected, but a routine waking recording does not demonstrate REM-stage loss of atonia or adequately characterize the nocturnal behavior.'),
 ('Dopamine-transporter SPECT', 'This may show a presynaptic dopaminergic deficit but does not establish the sleep-stage physiology required to confirm RBD.'),
 ('An overnight oxygen-saturation tracing alone', 'Oximetry can suggest sleep-disordered breathing but cannot by itself establish REM atonia loss or distinguish RBD from apnea-related arousals.')],
 [S('Confirmation and Mimics', '**REM sleep behavior disorder** combines dream-enactment behavior with REM sleep without atonia on polysomnography. Consider obstructive sleep apnea, nocturnal seizures and non-REM parasomnias as mimics.',
    'RBD is associated with synucleinopathies including PD, DLB and MSA, but the behavior does not independently distinguish among them or guarantee future conversion in an otherwise isolated case.',
    'Review antidepressants and other potential provoking medications, balancing risks before changing them.'),
  S('Prevent Injury and Treat Symptoms', '**A safer sleep environment is essential**: remove dangerous bedside objects, pad hard surfaces and consider sleeping arrangements when a partner is at risk.',
    'AASM 2023 conditionally supports immediate-release melatonin or clonazepam in appropriate adults. Melatonin commonly starts at 3 mg at bedtime and can be increased; clonazepam often starts at 0.25–0.5 mg at bedtime.',
    'Clonazepam can worsen falls, confusion and sleep-disordered breathing, particularly in older neurodegenerative patients. Choose according to cognitive, respiratory and balance risks; neither treatment is proven to prevent the underlying neurodegenerative process.')], ['RBD'])

add('Parkinson disease', 'Parkinsonism–Hyperpyrexia Syndrome',
 'After emergency surgery, a patient with PD misses levodopa for two days and develops fever, severe rigidity, reduced consciousness, autonomic instability and high CK. Which management principle is most important?',
 'Urgently restore dopaminergic treatment by an appropriate route and provide intensive supportive care', [
 ('Continue the levodopa interruption until all fever has resolved', 'The interruption may be a key trigger; continued withdrawal can prolong the crisis. Investigate infection while restoring appropriate dopaminergic therapy.'),
 ('Give haloperidol as the main treatment for rigidity and altered behavior', 'Dopamine blockade can further worsen the hypodopaminergic state; haloperidol does not correct the underlying mechanism and can aggravate motor deterioration.'),
 ('Treat solely with antipyretics and discharge after the temperature falls', 'Cooling and antipyretics are supportive but do not address the crisis or complications such as rhabdomyolysis, aspiration and renal injury.')],
 [S('Akinetic Crisis', '**Parkinsonism–hyperpyrexia syndrome** can follow abrupt dopaminergic interruption, impaired absorption, intercurrent infection or DBS-related interruption. The presentation resembles neuroleptic malignant syndrome.',
    'Urgently assess CK, renal function, electrolytes, infection and cardiorespiratory status. Sepsis and other causes can coexist and must not be ignored because the drug history is suggestive.',
    'Hospital medication timing and formulation are critical; nil-by-mouth status requires an alternative delivery plan rather than automatic omission.'),
  S('Emergency Management', '**Re-establish dopaminergic therapy promptly**, often with suitable levodopa through a nasogastric tube if swallowing is unsafe and enteral delivery is feasible. Specialist-guided alternatives may be required when the gut cannot be used.',
    'Provide fluids, temperature control, aspiration prevention and monitoring/treatment of rhabdomyolysis, renal injury, thrombosis and autonomic instability. Severe cases require intensive care.',
    'Dantrolene or other adjuncts may be considered in selected cases, but evidence is limited and they do not replace restoration of dopamine treatment and supportive management. Review the medication-system failure to prevent recurrence.')], ['CRISIS'])

add('Parkinson disease', 'Continuous Levodopa Delivery',
 'An adult with levodopa-responsive advanced PD has disabling motor fluctuations despite oral optimization and is being assessed for device-aided treatment. Which statement about foscarbidopa–foslevodopa is accurate?',
 'It provides continuous subcutaneous delivery of levodopa/carbidopa prodrugs through an infusion pump', [
 ('It is a dopamine agonist infusion that requires no levodopa conversion', 'Apomorphine is a dopamine agonist used by injection or infusion; foslevodopa instead is converted to levodopa and remains a levodopa-based strategy.'),
 ('It must be delivered through a surgically placed jejunal tube', 'Levodopa/carbidopa intestinal gel uses an enteral delivery system; the foscarbidopa–foslevodopa product in this question is administered subcutaneously.'),
 ('It is a proven neuroprotective replacement for all oral PD treatment', 'Continuous delivery is intended to improve motor fluctuations; it does not establish disease modification, and selection and supplementary treatment remain individualized.')],
 [S('Prodrug Infusion', '**Foslevodopa and foscarbidopa** are soluble prodrugs converted to levodopa and carbidopa. Continuous subcutaneous infusion aims to reduce variability associated with intermittent oral exposure.',
    'The US FDA approved the combination for motor fluctuations in adults with advanced PD in 2024. Local approval, access and selection rules differ.',
    'Infusion rates are calculated and titrated from prior levodopa exposure under the product-specific protocol; an oral tablet’s milligram dose cannot be directly substituted as a pump rate.'),
  S('Selection and Monitoring', '**Infusion-site reactions and infection**, dyskinesia, hallucinations, orthostatic hypotension and other dopaminergic effects require monitoring. Training, aseptic site care and a backup plan for interruption are essential.',
    'Other device-aided options include apomorphine infusion, intestinal levodopa gel and DBS in eligible patients. Choose according to the dominant problem, cognition, psychiatric status, anatomy, support and preferences.',
    'These treatments most directly address levodopa-responsive motor-state complications. They do not reliably correct levodopa-resistant axial, cognitive or autonomic disability and should be framed with realistic functional goals.')], ['INFUSE','NICE'])

R['CBD'] = ('Armstrong et al. Criteria for clinical diagnosis of corticobasal degeneration, 2013', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3590050/')
R['DIP'] = ('Persistent drug-induced parkinsonism with normal DAT imaging, clinical cohort, 2016', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC4905632/')
R['AMA'] = ('Amantadine immediate-release capsule prescribing information', 'https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=b54064bc-b3e1-4d83-be40-fcaddd2e99d0')
rows[10]['refs'].append('AMA')

add('Atypical and secondary parkinsonism', 'PSP Richardson Syndrome',
 'A 67-year-old has early backward falls, axial rigidity and slow vertical saccades. Voluntary downgaze is restricted but initially improves with the vestibulo-ocular maneuver. Which diagnosis best fits?',
 'Progressive supranuclear palsy, Richardson phenotype', [
 ('Typical Parkinson disease', 'PD can eventually cause falls, but early backward instability and supranuclear vertical gaze dysfunction strongly favor an atypical syndrome rather than typical PD.'),
 ('Multiple system atrophy', 'MSA often has early autonomic failure, cerebellar disease or stridor; the characteristic vertical supranuclear ocular pattern points more strongly toward PSP.'),
 ('Corticobasal syndrome', 'CBS commonly has asymmetric limb apraxia, cortical sensory loss or alien-limb phenomena; the early axial-fall and vertical-gaze combination is more characteristic of PSP-Richardson.')],
 [S('Supranuclear Ocular Dysfunction', '**Vertical supranuclear gaze palsy** reflects impaired voluntary gaze that can initially be overcome by the vestibulo-ocular reflex. This distinguishes supranuclear dysfunction from a purely restrictive or nuclear ocular deficit.',
    'Slow vertical saccades can precede a fixed gaze-range limitation. Test saccades by command rather than relying only on pursuit, and distinguish true slowing from delayed initiation.',
    'Early unprovoked falls and axial akinetic-rigid disease are typical of the Richardson phenotype. The 2017 MDS criteria recognize a wider range of PSP presentations beyond this classic combination.'),
  S('Pathology and Management', '**PSP is a predominantly four-repeat tauopathy.** Midbrain atrophy can support the diagnosis but is not independently pathognomonic.',
    'A levodopa trial may help selected parkinsonian features, especially variant presentations, but response is usually less sustained than in typical PD. DBS is generally not an effective treatment for the broader PSP syndrome.',
    'Prioritize falls prevention, swallowing and aspiration assessment, communication support, nutrition, eye-care strategies and multidisciplinary planning. Prognosis and counselling depend on phenotype and progression; do not assume every patient begins with the classic gaze palsy.')], ['PSP'])

add('Atypical and secondary parkinsonism', 'MDS MSA Criteria: Established Versus Probable',
 'Which statement correctly distinguishes clinically established from clinically probable MSA under the 2022 MDS criteria?',
 'An MSA-compatible MRI marker is required for clinically established disease but is not mandatory for clinically probable disease', [
 ('Both categories require neuropathological confirmation', 'Neuropathology establishes neuropathologically defined MSA; established and probable are clinical diagnostic categories rather than requirements for tissue confirmation.'),
 ('Autonomic dysfunction is unnecessary for clinically established MSA', 'Clinically established MSA requires autonomic failure together with the appropriate poorly levodopa-responsive parkinsonian or cerebellar syndrome and additional criteria.'),
 ('A hot-cross-bun sign alone establishes clinically probable MSA', 'An imaging sign alone does not fulfill the clinical combination, support and exclusion requirements; hot-cross-bun appearances also occur in other disorders.')],
 [S('Clinical Certainty Categories', '**Clinically established MSA** requires autonomic dysfunction plus poorly levodopa-responsive parkinsonism or a qualifying cerebellar syndrome, at least two supportive features, a qualifying MRI marker and absence of exclusions.',
    'Clinically probable MSA requires at least two of autonomic dysfunction, parkinsonism and cerebellar syndrome, plus at least one supportive feature and no exclusion. MRI markers are not mandatory for that category.',
    'Probable disease can therefore include parkinsonism plus cerebellar signs without the autonomic core combination required for established disease.'),
  S('Autonomic Thresholds', '**Unexplained voiding difficulty with a postvoid residual of at least 100 mL**, urge incontinence or neurogenic OH can satisfy specified established-category autonomic features, after excluding alternative explanations.',
    'Neurogenic OH uses a BP fall of at least 20 mmHg systolic, usually with at least 10 mmHg diastolic, and a blunted HR response; the established category uses a three-minute window, while probable criteria allow up to ten minutes.',
    'Prostatic obstruction, diabetic neuropathy, volume depletion and BP-lowering drugs can mimic relevant findings. Apply the full operational definitions rather than counting any urinary complaint or postural symptom as MSA.')], ['MSA'], style='direct', table=(['Feature','Clinically established','Clinically probable'],[
 ['Core syndrome','Autonomic failure + poorly responsive parkinsonism or cerebellar syndrome','At least 2 of autonomic, parkinsonian and cerebellar domains'],['Supportive features','At least 2','At least 1'],['Qualifying MRI marker','Required','Not required'],['Exclusions','Must be absent','Must be absent']]))

add('Atypical and secondary parkinsonism', 'MSA Imaging in Clinical Context',
 'A patient has progressive cerebellar ataxia, neurogenic orthostatic hypotension, urinary retention and pontocerebellar atrophy with a hot-cross-bun appearance. Which interpretation is best?',
 'MSA-C is a strong possibility, but the MRI sign must be interpreted with clinical criteria and competing causes', [
 ('The hot-cross-bun sign proves MSA independently of the clinical syndrome', 'The appearance is associated with MSA-C but can occur in hereditary and other ataxias; it is not a stand-alone pathological diagnosis.'),
 ('A substantial sensory neuronopathy and bilateral vestibular areflexia would exclude all genetic testing', 'That combination should raise RFC1-associated disease/CANVAS and can redirect testing; it does not make inherited late-onset ataxia irrelevant.'),
 ('Levodopa responsiveness at any point rules out MSA with certainty', 'Some patients with MSA have an initial or partial response. The degree, persistence and full diagnostic context matter, rather than any response being categorically exclusionary.')],
 [S('Pontocerebellar and Autonomic Pattern', '**MSA-C** combines a predominant cerebellar syndrome with characteristic autonomic and other features. MRI may show pontine, middle cerebellar peduncle or cerebellar atrophy and a hot-cross-bun pattern.',
    'MSA-P is the parkinsonian-predominant phenotype and can show putaminal atrophy or other qualifying abnormalities. The 2022 criteria specify eligible markers by phenotype.',
    'MSA is an alpha-synucleinopathy characterized pathologically by prominent glial cytoplasmic inclusions; an MRI pattern does not directly demonstrate that pathology.'),
  S('Mimics and Supportive Features', '**Hereditary ataxias, RFC1 disease, immune disease and structural causes** require consideration when the tempo, examination or family history is atypical.',
    'Stridor, early severe postural instability, rapid progression and particular postural deformities can support MSA, while a convincing alternative diagnosis may exclude it.',
    'Monitor swallowing, falls, sleep/respiratory symptoms, urinary retention and supine hypertension. Stridor warrants prompt specialist evaluation because it can have important airway consequences; autonomic and rehabilitation care remain central even when no curative therapy is available.')], ['MSA','ATAX'])

add('Atypical and secondary parkinsonism', 'Corticobasal Syndrome Is Not a Pathological Diagnosis',
 'A patient has markedly asymmetric rigidity, limb apraxia, cortical sensory loss and an alien-limb phenomenon. Which conclusion is most defensible?',
 'The phenotype supports corticobasal syndrome, which can have several underlying pathologies', [
 ('Corticobasal degeneration pathology is proven from the examination alone', 'CBD is one cause of CBS, but Alzheimer pathology, PSP and other degenerative diseases can produce the syndrome; bedside phenotype does not prove one proteinopathy.'),
 ('Typical PD explains the cortical signs without reassessment', 'Apraxia and cortical sensory dysfunction are not usual defining features of uncomplicated PD and should prompt assessment of a cortical degenerative or structural syndrome.'),
 ('MSA is established because asymmetry is its defining cortical feature', 'MSA is primarily identified by autonomic, parkinsonian and cerebellar combinations; alien-limb and cortical sensory/apraxic features favor a different clinical syndrome.')],
 [S('Clinical Phenotype', '**Corticobasal syndrome** typically combines asymmetric extrapyramidal motor dysfunction with cortical signs such as limb apraxia, cortical sensory loss or alien-limb phenomena.',
    'Dystonia and myoclonus may accompany rigidity and bradykinesia. Distinguish true apraxia from inability caused by weakness, sensory loss or poor comprehension.',
    'MRI can show asymmetric cortical atrophy and helps exclude a structural lesion. The pattern is supportive, not a stand-alone tissue diagnosis.'),
  S('Clinicopathological Heterogeneity', '**Corticobasal degeneration is a four-repeat tauopathy**, but a CBS phenotype can also arise from Alzheimer disease, PSP and other pathology.',
    'Clinical and biomarker assessment may refine the likely cause, particularly when Alzheimer-related pathology is suspected, but uncertainty should be stated honestly.',
    'Symptom-directed treatment includes a levodopa trial where appropriate, focal dystonia treatment, occupational/physical therapy and swallowing/communication assessment. Expected levodopa benefit is commonly limited compared with typical PD; management should address cortical disability as well as rigidity.')], ['CBD'])

add('Atypical and secondary parkinsonism', 'Dopamine-Blocker-Associated Parkinsonism',
 'A woman develops bradykinesia and rigidity after several months of metoclopramide. Which initial approach is best?',
 'Review withdrawal or replacement of the dopamine blocker and follow the clinical course for persistence or unmasked degeneration', [
 ('Diagnose idiopathic PD immediately because drug-induced disease cannot cause tremor', 'Drug-induced parkinsonism can include tremor and may be asymmetric; clinical appearance alone cannot dismiss the relevant dopamine-blocker exposure.'),
 ('Increase metoclopramide to overcome a presumed gastrointestinal cause of bradykinesia', 'Metoclopramide blocks dopamine receptors and can cause or worsen the syndrome; increasing it would reinforce the suspected mechanism.'),
 ('Promise complete recovery within 24 hours after the last dose', 'Improvement may take weeks or months, and persistent symptoms can occur with or without an initially abnormal DAT study; a fixed immediate recovery guarantee is unjustified.')],
 [S('Medication-Induced Motor Syndrome', '**Dopamine D2-receptor blockers** such as antipsychotics and metoclopramide are important causes of secondary parkinsonism. Review the complete medication history, including antiemetics.',
    'Bilateral symmetry is common but not obligatory. Tremor or asymmetry does not by itself prove underlying idiopathic PD.',
    'Coordinate stopping, reducing or substituting the offending drug according to its indication. Psychiatric treatment changes need appropriate collaboration rather than an unsupervised abrupt stop.'),
  S('Persistence and Additional Testing', '**A dopamine blocker can unmask pre-existing degeneration.** Persistent or progressive symptoms after withdrawal warrant clinical reassessment and, when uncertainty affects management, consideration of presynaptic dopaminergic imaging.',
    'Pure postsynaptic drug-induced disease often has preserved DAT uptake; reduced uptake can support underlying nigrostriatal degeneration. Normal imaging does not guarantee immediate or complete recovery.',
    'Avoid reflexive long-term anticholinergic treatment in older patients because of cognitive, urinary and ocular toxicity. Treat functional impairment while reassessing the cause and trajectory over time.')], ['DIP','PDCR'])

R.update({
 'ET11': ('AAN evidence-based essential tremor treatment guideline, 2011', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3208950/'),
 'ET26': ('MDS evidence-based review of medical treatments for essential tremor, 2026', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC13067321/'),
 'HOLMES': ('Raina et al. Holmes tremor: lesion localization and treatment in 29 cases, 2016', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC4782118/'),
 'FUNC': ('Prospective validation of laboratory-supported functional tremor criteria, 2016', 'https://pubmed.ncbi.nlm.nih.gov/26879346/'),
 'BOT': ('AAN botulinum neurotoxin guideline update, 2016', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC4862245/'),
 'ACD': ('Indian clinical practice guidance for psychotropic medication emergencies, 2022', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9122152/'),
 'DRD': ('GeneReviews: GCH1-deficient dopa-responsive dystonia', 'https://www.ncbi.nlm.nih.gov/books/NBK1508/'),
})

add('Tremor syndromes', 'Essential Tremor: The 2018 Syndrome Definition',
 'A patient has bilateral upper-limb action tremor for eighteen months without dystonia, parkinsonism or ataxia. Under the 2018 MDS classification, which label is most appropriate at present?',
 'Indeterminate tremor during observation because the three-year duration requirement is not yet met', [
 ('Definite essential tremor solely from bilateral hand involvement', 'Bilateral action tremor is central to ET, but the 2018 syndrome definition also requires at least three years and absence of other defining neurological signs.'),
 ('Essential tremor plus solely because symptoms affect handwriting', 'Functional impact does not itself define ET-plus; that classification concerns additional neurological signs of uncertain significance accompanying an ET phenotype.'),
 ('Dystonic tremor solely because the tremor worsens with action', 'Action-related worsening is not sufficient for dystonia. Look for abnormal patterned postures, a null point or other convincing dystonic features.')],
 [S('Isolated Action-Tremor Syndrome', '**Essential tremor** under the 2018 MDS framework is isolated bilateral upper-limb action tremor lasting at least three years, with or without tremor elsewhere, and without other neurological signs such as dystonia, ataxia or parkinsonism.',
    'An otherwise compatible syndrome of shorter duration is observed as indeterminate tremor. The duration rule is a classification safeguard, not a reason to withhold symptom treatment.',
    'Isolated head or voice tremor is not sufficient for the ET definition. Sudden onset, stepwise progression and clearly task- or position-specific tremor also require a different classification.'),
  S('ET-Plus and Differential Diagnosis', '**ET-plus** describes an ET phenotype with additional signs of uncertain significance, such as questionable dystonia or mild tandem impairment that does not establish another syndrome.',
    'Definite dystonia, cerebellar disease or parkinsonism should instead be classified appropriately rather than absorbed into an unlimited ET-plus category.',
    'Review stimulants, thyroid disease, medications and anxiety-associated enhanced physiological tremor. Alcohol responsiveness and family history can be informative but are neither necessary nor independently diagnostic.')], ['TREM'], style='direct')

add('Tremor syndromes', 'Essential Tremor Treatment with Asthma',
 'A patient with disabling hand essential tremor has active asthma and a resting pulse of 54/min. Which commonly used oral option is most suitable to try at a very low starting dose?',
 'Primidone', [
 ('Propranolol', 'Propranolol is a commonly used ET treatment, but nonselective beta blockade can aggravate asthma and bradycardia, making it a poor choice in this patient.'),
 ('Trihexyphenidyl', 'Trihexyphenidyl may help selected dystonic or parkinsonian tremor, but is not a standard first-line treatment for an isolated ET syndrome and adds anticholinergic toxicity.'),
 ('Levodopa', 'Levodopa treats parkinsonian symptoms when that syndrome is present; isolated ET without bradykinesia or rigidity is not its usual target.')],
 [S('Comorbidity-Guided Selection', '**Primidone and propranolol** are longstanding commonly used ET treatments. Asthma, bradycardia and conduction disease can make propranolol unsuitable.',
    'Primidone is usually started very low, often 12.5–25 mg at bedtime, and increased slowly. Initial nausea, sedation, dizziness and ataxia can be substantial even at low doses.',
    'Propranolol often begins at 10–20 mg once or twice daily and is titrated to response and cardiovascular tolerance; doses and formulations vary. Neither drug is uniformly effective.'),
  S('Evidence and Escalation', '**The 2011 AAN guideline rated both drugs effective**, while the 2026 MDS evidence review judged certainty more cautiously because of trial bias and imprecision. State the framework rather than presenting all evidence ratings as interchangeable.',
    'Topiramate or selected other drugs may be considered when first options fail, with attention to cognition, renal stones, sedation and patient goals.',
    'For medication-refractory disabling tremor, specialist options include individualized botulinum toxin, thalamic DBS or lesion-based procedures in selected patients. Hand weakness, speech/balance effects and procedural risks require counselling; treatment is symptomatic rather than curative.')], ['ET11','ET26'])

add('Tremor syndromes', 'High-Frequency Orthostatic Tremor',
 'An older adult feels markedly unsteady while standing still, improves on sitting or walking, and has subtle rapid leg vibration. Which test most directly confirms the suspected tremor syndrome?',
 'Surface EMG showing coherent rhythmic leg-muscle bursts at 13–18 Hz while standing', [
 ('Dopamine-transporter SPECT showing reduced striatal uptake', 'DAT imaging can support nigrostriatal dysfunction in parkinsonism but does not establish the characteristic electrophysiology of classic orthostatic tremor.'),
 ('Routine nerve conduction studies demonstrating a distal sensory neuropathy', 'Neuropathy can cause sensory imbalance, but routine sensory studies do not demonstrate the stance-induced high-frequency rhythmic motor discharge defining this syndrome.'),
 ('EEG showing an epileptic discharge before every leg movement', 'Time-locked cortical discharges can support cortical myoclonus, a different phenomenon from the highly coherent 13–18-Hz stance-related tremor described.')],
 [S('Stance-Related Oscillation', '**Classic orthostatic tremor** is a high-frequency tremor, usually 13–18 Hz, occurring during weight-bearing stance. It may be felt more easily than seen and often improves with sitting, walking or leaning.',
    'Surface EMG demonstrates rhythmic synchronous/coherent activity across affected muscles during standing. Clinical unsteadiness without physiological confirmation is insufficient for a confident subtype diagnosis.',
    'Lower-frequency stance tremors and orthostatic myoclonus require separate interpretation; not all shaking while standing is classic primary orthostatic tremor.'),
  S('Associated Disease and Treatment', '**Examine for additional neurological signs** before calling the syndrome primary. Cerebellar, parkinsonian or other abnormalities can indicate a combined or secondary syndrome.',
    'Clonazepam or gabapentin may help selected patients, but evidence is limited and sedation or falls can restrict use. A support that transfers weight to the arms can improve standing function.',
    'Assess vestibular, sensory, cardiovascular and musculoskeletal contributors to imbalance. The diagnostic frequency guides classification, while treatment should target actual standing tolerance and safety.')], ['TREM'])

add('Tremor syndromes', 'Holmes Tremor After a Structural Lesion',
 'Months after a midbrain hemorrhage, a patient develops a slow, large-amplitude arm tremor present at rest and intensified by posture and target-directed movement. Which syndrome best fits?',
 'Holmes tremor', [
 ('Isolated essential tremor', 'ET is primarily a bilateral action-tremor syndrome; a delayed unilateral mixed rest–postural–intention tremor after a structural brain lesion suggests Holmes tremor.'),
 ('Typical Parkinson disease tremor', 'PD rest tremor can re-emerge with posture, but the lesion-related delayed onset and prominent low-frequency intention component favor Holmes tremor in this case.'),
 ('Classic orthostatic tremor', 'Classic orthostatic tremor is a very high-frequency leg/trunk phenomenon on standing, unlike this slow arm tremor with rest and intention components.')],
 [S('Mixed Activation Pattern', '**Holmes tremor** is typically a slow tremor, often below 5 Hz, combining rest, postural and intention components. It can emerge after a delay following a structural lesion.',
    'Lesions can affect midbrain, thalamic or cerebellar-connected networks. The term is preferable to assuming every case is confined to the red nucleus.',
    'Associated weakness, ataxia, sensory findings or ocular abnormalities help localize the original injury. MRI evaluates the structural cause and alternative lesions.'),
  S('Treatment Evidence', '**A levodopa trial can be reasonable**, although response is variable. A 2016 series reported benefit in 13 of 24 treated patients, illustrating possible response without proving universal efficacy.',
    'Other medication trials and selected thalamic or other neurosurgical approaches may be considered for severe refractory disease, but evidence is mainly observational and target selection is individualized.',
    'Occupational strategies and rehabilitation help reduce functional consequences. Explain that the mixed tremor reflects network injury and that a drug effective for one component may not abolish the whole syndrome.')], ['HOLMES','TREM'])

add('Tremor syndromes', 'Positive Signs of Functional Tremor',
 'A hand tremor changes frequency to match contralateral paced tapping and markedly diminishes during a distracting task. Which interpretation is best?',
 'Entrainment and distractibility provide positive evidence supporting functional tremor', [
 ('The findings establish deliberate fabrication', 'Functional tremor is not synonymous with malingering; positive inconsistency signs demonstrate altered motor control but do not establish conscious production.'),
 ('Functional tremor requires a normal MRI and a psychiatric diagnosis before it can be recognized', 'Diagnosis rests on positive clinical inconsistency/incongruence signs; neither a normal scan nor a specific psychiatric diagnosis is a prerequisite.'),
 ('Any variability proves that an organic tremor cannot coexist', 'Functional and other neurological disorders can coexist. Positive signs support a functional component but should not erase separately demonstrated disease.')],
 [S('Rule-In Examination', '**Entrainment, distractibility and marked frequency variability** can support functional tremor when demonstrated reproducibly and interpreted together.',
    'Ask the unaffected hand to tap at several rates and observe whether the tremor adopts that rhythm, pauses or changes substantially. Avoid treating a single ambiguous maneuver as absolute proof.',
    'Electrophysiological test batteries can provide laboratory-supported evidence when the bedside diagnosis is uncertain; validation studies support combining signs rather than relying only on exclusion.'),
  S('Explanation and Treatment', '**Explain the diagnosis using the observed positive signs**, emphasizing that the movement is real and that altered control can be potentially retrained.',
    'Offer appropriate movement-focused physiotherapy, occupational support and psychological treatment when indicated by the individual formulation. A psychiatric stressor is not required for diagnosis.',
    'Review coexisting neurological or medication-related tremor. Repeated investigations without a clinical reason can delay treatment, but new objective signs should still receive a proportionate reassessment.')], ['FUNC'])

add('Dystonia', 'Patterned Posture and a Sensory Trick',
 'A woman has recurrent involuntary head turning with an irregular directional tremor. Lightly touching her chin temporarily improves the posture. Which phenomenon best explains the examination?',
 'Cervical dystonia with a sensory trick', [
 ('Essential head tremor without dystonia', 'ET can involve the head, but patterned abnormal turning, directional tremor and improvement with a sensory trick support a dystonic syndrome rather than isolated ET.'),
 ('A suppressible motor tic with a premonitory urge', 'Tics often have an urge and temporary voluntary suppression; a sustained patterned neck posture modified by light touch is more characteristic of dystonia.'),
 ('Spasticity caused by a corticospinal lesion', 'Spasticity is velocity-dependent resistance associated with upper motor neuron dysfunction; it does not ordinarily produce this patterned posture and sensory-trick response.')],
 [S('Motor Phenomenology', '**Dystonia produces sustained or intermittent contractions causing abnormal, often repetitive, patterned movements or postures.** It can be action induced and may include tremor.',
    'A sensory trick, or geste antagoniste, is a light touch or maneuver that reduces the abnormal movement. It is supportive but not required, and should not be mistaken for evidence of a functional disorder.',
    'Dystonic tremor may be irregular, directional and reduced at a null point. Examine for subtle posturing when an apparently isolated head or task-related hand tremor is encountered.'),
  S('Classification and Evaluation', '**Describe distribution, onset and associated features**: focal, segmental, multifocal, generalized or hemidystonia; isolated versus combined neurological syndromes; and task or time dependence.',
    'Drug exposure, young onset, rapid progression, hemidystonia or other neurological signs can prompt targeted imaging, metabolic or genetic evaluation.',
    'Focal cervical disease commonly responds to appropriately targeted botulinum toxin, with rehabilitation and selected oral agents as adjuncts. A phenotype label should guide evaluation without assuming a single genetic or structural cause.')], ['BOT','TREM'])

add('Dystonia', 'Botulinum Toxin for Cervical Dystonia',
 'A patient has painful focal cervical dystonia interfering with work. Which treatment is generally preferred for targeted symptomatic control?',
 'Botulinum neurotoxin injection into appropriately selected overactive muscles', [
 ('Chronic high-dose trihexyphenidyl as the default before local treatment', 'Anticholinergics can help selected dystonia, especially some younger generalized cases, but systemic cognitive and autonomic effects often limit them relative to focal injection treatment.'),
 ('Levodopa as uniformly effective for all adult cervical dystonia', 'A levodopa trial is important in suspected dopa-responsive presentations, but most isolated adult cervical dystonia does not show that characteristic dramatic sustained response.'),
 ('Immediate GPi DBS before an adequate focal treatment trial', 'GPi DBS can help severe medically refractory dystonia, but is generally considered after appropriate less invasive treatment, including optimized focal injections where indicated.')],
 [S('Targeted Neuromuscular Treatment', '**Botulinum neurotoxin** reduces acetylcholine release at the neuromuscular junction and is a standard treatment for focal cervical dystonia. Type A toxins act on SNAP-25; type B acts on synaptobrevin/VAMP.',
    'Select muscles according to the actual dystonic pattern, not simply the direction the head appears to face. EMG or ultrasound guidance can help in appropriate cases.',
    'Dose and distribution are individualized by muscle, severity, prior response and formulation. Units from different toxin products are not directly interchangeable.'),
  S('Adverse Effects and Follow-up', '**Dysphagia and neck weakness** are important local adverse effects, particularly with certain muscle patterns and injection distributions. Counsel about rare distant toxin effects and evaluate breathing or swallowing difficulty promptly.',
    'Benefits are temporary; follow-up and reinjection timing depend on clinical response and product guidance, often around twelve-week intervals rather than a universal identical schedule.',
    'If response is poor, reassess diagnosis, muscle selection, dose, contracture and technique before assuming antibody-mediated resistance. Rehabilitation and pain management complement the injection strategy.')], ['BOT'])

add('Dystonia', 'Acute Dopamine-Blocker-Induced Dystonia',
 'Hours after haloperidol, a young adult develops painful torticollis and sustained upward eye deviation while remaining conscious. There is no generalized clonus or hyperthermia. Which acute treatment is appropriate?',
 'Parenteral benztropine or diphenhydramine, with airway assessment and withdrawal of the provoking drug', [
 ('Propranolol as the preferred immediate reversal treatment', 'Propranolol is used in selected akathisia or tremor contexts, but does not rapidly reverse the cholinergic–dopaminergic imbalance of an acute dystonic reaction.'),
 ('Additional haloperidol to suppress the eye and neck movements', 'Further dopamine blockade can intensify acute dystonia; the temporal relationship and preserved awareness favor a medication reaction requiring reversal.'),
 ('VMAT2 inhibition as the immediate emergency treatment', 'VMAT2 inhibitors can treat tardive dyskinesia or Huntington chorea, but are not the rapid first-line rescue for an acute dystonic reaction.')],
 [S('Acute Extrapyramidal Reaction', '**Acute dystonia** can occur soon after a dopamine blocker, especially in younger patients. Oculogyric crisis, jaw/tongue spasm and torticollis are characteristic presentations.',
    'Assess the airway because laryngeal involvement can be life threatening. Preserve a broad differential if consciousness, systemic features or the movement pattern is atypical.',
    'Review antipsychotics and antiemetics such as metoclopramide. Stop or replace the provoking agent with appropriate clinical coordination.'),
  S('Reversal and Recurrence Prevention', '**Adult rescue options include benztropine 1–2 mg IM/IV or diphenhydramine 25–50 mg IM/IV**, according to availability and local protocol. Improvement is usually rapid, especially intravenously.',
    'A short oral anticholinergic/antihistaminic continuation is often needed because the provoking drug can outlast the rescue dose. Reassess promptly if response is incomplete or symptoms recur.',
    'Benzodiazepines may be adjunctive in selected persistent cases. Distinguish this acute reaction from akathisia, tardive syndromes, seizure, tetany and neuroleptic malignant syndrome, because their treatment priorities differ.')], ['ACD'])

add('Dystonia', 'Dopa-Responsive Dystonia',
 'A girl develops foot inversion and gait difficulty that worsen through the day and improve after sleep. Cognition and sensory examination are preserved. Which therapeutic diagnostic step is most appropriate?',
 'A supervised low-dose levodopa/decarboxylase-inhibitor trial', [
 ('Treat only with botulinum toxin without evaluating a dopamine-synthesis disorder', 'Focal injection may reduce a particular posture, but the childhood onset and diurnal pattern warrant a potentially transformative levodopa trial before limiting treatment to local symptoms.'),
 ('Start a VMAT2 inhibitor to deplete dopamine', 'VMAT2 inhibition can help chorea or tardive dyskinesia, but dopamine depletion is not the appropriate mechanistic approach to suspected dopamine-synthesis deficiency.'),
 ('Proceed directly to GPi DBS without a medication trial', 'DBS may help refractory dystonia, but suspected dopa-responsive disease should first receive a levodopa trial because a low-dose medical response can be dramatic.')],
 [S('Dopamine-Synthesis Defect', '**GCH1-deficient dopa-responsive dystonia** commonly causes childhood lower-limb dystonia, diurnal fluctuation and a marked sustained levodopa response. GCH1 encodes GTP cyclohydrolase 1, important for tetrahydrobiopterin synthesis.',
    'The common form is autosomal dominant with reduced penetrance. Other dopamine-synthesis disorders can produce related or more complex phenotypes, so treatment response alone does not identify the gene.',
    'The presentation may be mistaken for cerebral palsy or a spastic gait disorder. Absence of a family history does not exclude it.'),
  S('Trial and Long-Term Care', '**Start levodopa cautiously with a peripheral decarboxylase inhibitor.** GeneReviews gives an example initiation of 25–50 mg levodopa one to three times daily in children aged six years or older, with slow adjustment.',
    'Many classic GCH1 cases achieve a complete or near-complete sustained response at relatively low doses. Transient initial dyskinesia can occur, while typical PD-like long-term fluctuations are uncommon in the classic phenotype.',
    'Arrange appropriate genetic evaluation and counselling. A negative or incomplete initial trial requires review of dose, duration, adherence and alternative diagnoses rather than an automatic conclusion from a single dose.')], ['DRD'])

R.update({
 'HDGEN': ('GeneReviews: Huntington disease, repeat interpretation and counselling', 'https://www.ncbi.nlm.nih.gov/books/NBK1305/'),
 'HDTX': ('International Huntington disease treatment guidelines, 2019', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6618900/'),
 'TETRA': ('Tetrabenazine US prescribing information', 'https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=49587379-1cc0-48ff-9f2f-517079cf499d'),
 'VAL': ('Valbenazine prescribing information, 2026', 'https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/218390s003lbl.pdf'),
 'WD22': ('AASLD Wilson disease practice guidance, 2022', 'https://doi.org/10.1002/hep.32801'),
 'WD25': ('EASL-ERN Wilson disease clinical practice guidelines, 2025', 'https://easlcampus.eu/sites/default/files/2025-03/EASL-ERN_CPG_on_Wilson%27s_Disease.pdf'),
 'TICDX': ('CDC: Diagnostic criteria for tic disorders', 'https://www.cdc.gov/tourette-syndrome/diagnosis/index.html'),
 'TICTX': ('AAN treatment guideline for Tourette syndrome and chronic tic disorders, 2019', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6537133/'),
 'MYO': ('Levetiracetam in cortical myoclonus: clinical/electrophysiological study, 2005', 'https://pubmed.ncbi.nlm.nih.gov/16078205/'),
 'NEUROPHYS': ('Clinical neurophysiology of functional motor disorders: IFCN handbook, 2024', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC10862411/'),
})

add('Chorea and related disorders', 'Huntington Repeat Ranges',
 'An asymptomatic adult receives a confirmed HTT result of 38 CAG repeats during a formal predictive-testing programme. Which counselling interpretation is most appropriate?',
 'This is a reduced-penetrance disease-associated allele; clinical disease is possible but not inevitable', [
 ('This is a normal stable allele with no transmission implications', 'Normal alleles are generally 26 or fewer repeats; a 38-repeat allele is disease associated and has important personal and reproductive implications.'),
 ('This is an intermediate allele, conventionally 27–35 repeats', 'Intermediate alleles occupy a lower conventional range and mainly raise transmission-instability concerns; 38 falls in the reduced-penetrance disease-associated category.'),
 ('This guarantees a precisely predictable age of symptom onset', 'Repeat length influences risk and onset but cannot provide a precise individual onset date, particularly within the reduced-penetrance range.')],
 [S('Conventional Laboratory Categories', '**HTT CAG expansion** causes autosomal dominant Huntington disease. Conventional ranges are normal at 26 or fewer, intermediate at 27–35, reduced penetrance at 36–39 and full penetrance at 40 or more repeats.',
    'These categories do not replace assay interpretation. Repeat interruptions and technical methods can affect an estimate near a boundary, so discordant clinical and laboratory findings warrant expert review.',
    'Repeat instability and anticipation are particularly associated with paternal transmission; larger expansions can be associated with juvenile presentations.'),
  S('Predictive Testing and Family Care', '**A result is not merely a laboratory fact.** Pre- and post-test genetic counselling, informed consent, psychological support and discussion of reproductive options are essential.',
    'A heterozygous carrier has a 50% chance of transmitting the allele at each conception, while the transmitted repeat length and penetrance may vary.',
    'Clinical evaluation addresses cognition, behavior, mood, motor function and family support. Do not use a CAG count to make an unsupported exact prediction of employment capacity, lifespan or age of onset.')], ['HDGEN'], style='direct', table=(['CAG repeats','Conventional interpretation'],[
 ['≤26','Normal'],['27–35','Intermediate; possible transmission instability'],['36–39','Reduced penetrance'],['≥40','Full-penetrance disease-associated range within a usual lifespan']]))

add('Chorea and related disorders', 'Huntington Chorea with Psychiatric Comorbidity',
 'A patient with Huntington disease has distressing chorea, active psychosis and inadequately treated major depression. Which strategy is most appropriate?',
 'Address psychiatric illness urgently and consider a suitable antipsychotic that may also reduce chorea', [
 ('Start tetrabenazine without first addressing the depression', 'Tetrabenazine is useful for chorea in appropriate patients but is contraindicated with active suicidality or untreated/inadequately treated depression under its US label.'),
 ('Treat chorea with levodopa as the routine first choice in this hyperkinetic presentation', 'Levodopa may have a role in selected rigid juvenile phenotypes but is not the usual treatment for prominent adult chorea and may worsen hyperkinetic or psychotic symptoms.'),
 ('Use an anticholinergic as the preferred treatment for both psychosis and chorea', 'Anticholinergics do not treat psychosis and can worsen cognition; their selected dystonia/tremor uses do not make them appropriate for this combination.')],
 [S('Choose Treatment Around the Whole Syndrome', '**Chorea treatment is indicated when movement impairs function, safety or comfort**, not simply because it is visible. Assess mood, suicidality, psychosis, swallowing and falls before choosing a dopamine-reducing agent.',
    'A suitable second-generation antipsychotic may address psychosis and reduce chorea. Sedation, metabolic effects, QT risk and drug-induced parkinsonism require monitoring.',
    'Active depression and suicide risk need direct treatment and support; medication choice should not focus on the motor examination while ignoring psychiatric danger.'),
  S('VMAT2 Inhibitors', '**Tetrabenazine, deutetrabenazine and valbenazine** reduce vesicular monoamine storage and have chorea indications in relevant jurisdictions. Their doses, interactions and warnings differ.',
    'Tetrabenazine commonly starts at 12.5 mg daily with gradual titration; CYP2D6 testing is required before exceeding 50 mg/day under the cited label. Depression/suicidality, sedation, akathisia and parkinsonism are important risks.',
    'Valbenazine also has a Huntington-related depression/suicidality boxed warning. Symptomatic improvement does not establish disease modification; rehabilitation, nutrition, speech/swallowing care and family support remain necessary.')], ['HDTX','TETRA','VAL'])

add('Chorea and related disorders', 'Tardive Dyskinesia',
 'After years of dopamine-blocking antipsychotic treatment, a patient develops persistent oro-bucco-lingual stereotypies and choreiform limb movements. Which targeted drug class has an established role for troublesome tardive dyskinesia?',
 'VMAT2 inhibitors such as valbenazine or deutetrabenazine', [
 ('Anticholinergics as routine treatment for the oro-lingual dyskinesia', 'Anticholinergics can reverse acute dystonia or help selected drug-induced parkinsonism, but may worsen classical tardive dyskinesia and are not its routine targeted therapy.'),
 ('Higher-dose dopamine blockade solely to mask the movements long term', 'Increasing blockade may transiently mask dyskinesia but adds exposure and adverse effects; it is not a preferred disease-management strategy for persistent troublesome TD.'),
 ('Levodopa as the standard treatment for antipsychotic-related stereotypies', 'Levodopa is used for selected hypodopaminergic motor syndromes and is not a standard treatment for the described tardive hyperkinetic syndrome.')],
 [S('A Delayed Drug-Associated Syndrome', '**Tardive dyskinesia** follows exposure to dopamine-receptor-blocking drugs and may persist after withdrawal. Orofacial stereotypies, chorea and other movement phenotypes can occur.',
    'Differentiate acute dystonia, akathisia, drug-induced parkinsonism, edentulous movements and other causes. A structured scale such as AIMS helps document distribution and change but does not alone establish etiology.',
    'Review whether the provoking drug is still needed and whether a lower-risk alternative is feasible, while avoiding destabilization of the psychiatric illness.'),
  S('Targeted Therapy', '**Valbenazine and deutetrabenazine** have randomized evidence and relevant regulatory approvals for TD. Use product-specific titration and review CYP interactions, QT risk, sedation and parkinsonism.',
    'Valbenazine for TD commonly starts at 40 mg once daily and may increase after one week, with 60 or 80 mg options according to response, tolerability and labeling. Interaction or organ-function restrictions can require lower dosing.',
    'Treatment can improve movement severity but does not guarantee permanent reversal. Coordinate neurological and psychiatric follow-up and assess speech, chewing, swallowing and social function, not only the numerical movement score.')], ['VAL'])

add('Chorea and related disorders', 'Neurological Wilson Disease: Composite Diagnosis',
 'A 22-year-old has dysarthria, dystonia and an irregular proximal action tremor. Liver enzymes are mildly abnormal. Which evaluation is most appropriate?',
 'Slit-lamp examination, ceruloplasmin, basal 24-hour urinary copper and integrated clinical/genetic assessment', [
 ('Exclude Wilson disease from a normal ceruloplasmin alone', 'Ceruloplasmin may be normal in Wilson disease and can vary with inflammation or estrogen exposure; a normal result does not override a compatible phenotype.'),
 ('Diagnose Wilson disease from low total serum copper alone', 'Low total copper can reflect low ceruloplasmin and is not independently diagnostic; serum results require interpretation with other copper studies and clinical findings.'),
 ('Use a wing-beating tremor as a pathognomonic bedside test', 'A proximal wing-beating pattern is a useful clue but is not exclusive to Wilson disease; objective biochemical, ophthalmic and etiologic evaluation is needed.')],
 [S('Recognizing a Treatable Cause', '**Wilson disease is an ATP7B-related recessive disorder of copper handling.** Young-onset mixed movement disorder, dysarthria, psychiatric change or unexplained liver disease should prompt evaluation.',
    'Kayser–Fleischer rings are common in neurological presentations but not universal. Slit-lamp assessment is more appropriate than relying on an unaided bedside inspection.',
    'Brain MRI can show basal-ganglia and brainstem abnormalities, but neither a normal scan nor absence of a famous imaging sign excludes the disease.'),
  S('Copper Tests and Confirmation', '**Ceruloplasmin is often low**, with values below about 14 mg/dL particularly suggestive, but sensitivity and specificity are imperfect. Low values occur in other conditions.',
    'Basal 24-hour urinary copper is commonly above 100 µg/day in symptomatic disease. Lower values do not categorically exclude early disease, while other liver disorders can also increase excretion.',
    'Integrate ophthalmic, neurological, hepatic, biochemical and ATP7B findings, often using a Leipzig-based framework. Liver copper quantification or newer exchangeable-copper tests may help selected unresolved cases according to availability and specialist expertise.')], ['WD22','WD25'])

add('Chorea and related disorders', 'Treating Neurological Wilson Disease',
 'A patient with neurological Wilson disease is starting chelation. Which treatment principle is most appropriate?',
 'Use a specialist-guided start-low, go-slow regimen and monitor neurological status and copper balance', [
 ('Escalate chelation immediately to the maximum dose because neurological worsening cannot occur', 'Early neurological deterioration is recognized with anti-copper therapy, especially chelation, so cautious initiation and close assessment are important.'),
 ('Use zinc alone for every patient regardless of significant liver involvement', 'Zinc may be appropriate in selected neurological or maintenance contexts, but significant hepatic disease generally requires a chelator under current EASL guidance.'),
 ('Stop all copper-directed treatment permanently once neurological symptoms improve', 'Wilson treatment is generally lifelong; stopping can cause serious hepatic or neurological relapse even after apparent improvement.')],
 [S('Copper Removal and Absorption Reduction', '**Penicillamine and trientine are copper chelators**, while zinc induces intestinal metallothionein and reduces copper absorption. Selection depends on neurological and hepatic severity, prior response and tolerability.',
    'EASL-ERN 2025 recommends either zinc or a chelator for a neurological presentation, with start-low, go-slow chelator initiation. Significant liver involvement favors chelation rather than assuming zinc is sufficient.',
    'Adult penicillamine often reaches 750–1500 mg/day in divided doses; gradual initiation is important in neurological disease. Trientine doses depend on the salt/formulation and should not be exchanged milligram for milligram.'),
  S('Monitoring and Safety', '**Neurological deterioration, undertreatment and copper deficiency** must all be considered during follow-up. Use clinical examination, liver tests, blood counts, urinalysis and properly interpreted copper studies.',
    'Penicillamine can cause rash, cytopenias, proteinuria and autoimmune toxicity; pyridoxine supplementation is commonly provided. Zinc is often prescribed as 50 mg elemental zinc three times daily in adults, separated from meals and interacting agents as instructed.',
    'Urinary copper targets differ between initial chelation, maintenance and zinc treatment. Do not apply one universal threshold or interpret copper excretion without knowing the drug, adherence and sampling conditions.')], ['WD22','WD25'])

add('Tics and myoclonus', 'Tourette Syndrome Diagnostic Requirements',
 'A 15-year-old has had several motor tics and a vocal tic intermittently for eighteen months, beginning at age twelve. The motor and vocal tics were not always simultaneous. Drugs and other causes are excluded. Which diagnosis fits best?',
 'Tourette syndrome', [
 ('Persistent motor tic disorder because motor and vocal tics were not simultaneous', 'Tourette criteria do not require simultaneity. Persistent motor-only disorder applies when the required vocal component has not occurred.'),
 ('Provisional tic disorder because tics wax and wane', 'Waxing and waning is common; provisional disorder applies to a shorter duration, not to every fluctuating course lasting more than a year.'),
 ('Persistent vocal tic disorder despite multiple established motor tics', 'A vocal-only persistent disorder does not capture a history meeting both the multiple-motor and vocal components of Tourette syndrome.')],
 [S('Motor, Vocal and Time Criteria', '**Tourette syndrome** requires multiple motor tics and at least one vocal tic at some point in the illness, not necessarily at the same time, with persistence for more than a year since first tic onset and onset before age eighteen.',
    'Symptoms must not be attributable to a substance or another medical disorder. The pattern commonly waxes and wanes, and temporary improvement does not restart the diagnostic clock.',
    'Coprolalia is not required and occurs in only a minority. Common vocal tics include throat clearing, sniffing and simple sounds.'),
  S('Clinical Assessment', '**Premonitory urges and temporary suppressibility** are common but may be difficult for younger children to describe. Distinguish tics from stereotypies, chorea, dystonia, seizures and functional tic-like behaviors.',
    'Assess impairment and comorbid ADHD, OCD, anxiety and mood symptoms. Comorbidity can cause more disability than the tics themselves.',
    'Treatment is selected according to functional burden rather than the diagnostic label alone. Education and watchful waiting can be appropriate when impairment is minimal, while behavioral or pharmacological treatment is available for troublesome symptoms.')], ['TICDX','TICTX'])

add('Tics and myoclonus', 'Choosing Treatment for Troublesome Tics',
 'A teenager with Tourette syndrome has bothersome tics, wants active treatment and can participate in behavioral sessions. There is no urgent injury risk. Which initial option should be offered when available?',
 'Comprehensive behavioral intervention for tics', [
 ('Start haloperidol automatically before discussing behavioral treatment', 'Antipsychotics can reduce severe tics, but their movement, metabolic and other adverse effects make automatic first-line use inappropriate when an evidence-based behavioral option is feasible.'),
 ('Use a VMAT2 inhibitor as a universally established first-line tic therapy', 'VMAT2 drugs have established roles in TD and Huntington chorea, but should not be assumed to have equivalent evidence or a universal first-line indication for Tourette tics.'),
 ('Treat only the visible tics and avoid evaluating ADHD or OCD', 'Comorbid ADHD and OCD commonly drive impairment and affect treatment choice; ignoring them can leave the major disability untreated.')],
 [S('Behavioral Intervention', '**CBIT combines habit-reversal elements, awareness training, competing responses and modification of tic-provoking situations.** AAN guidance supports offering it as an initial option relative to medication when appropriate and available.',
    'It is not an instruction simply to suppress symptoms through willpower. Explain the structured skills-based approach and adapt it to age, motivation and access.',
    'Education and school/work accommodations can reduce stigma and environmental burden alongside active treatment.'),
  S('Medication by Comorbidity and Severity', '**Clonidine or guanfacine** can help selected patients, particularly when ADHD coexists. Monitor sedation, BP and HR; taper rather than stopping an alpha-2 agonist abruptly.',
    'Aripiprazole or other appropriate antipsychotics may be used when benefits justify risks. Monitor weight/metabolic effects, akathisia, other drug-induced movements and relevant cardiac risks.',
    'Assess symptom-related disability periodically because tics often change with age and context. The goal is improved function and well-being rather than a promise of complete permanent tic elimination.')], ['TICTX'])

add('Tics and myoclonus', 'Electrophysiological Evidence of Cortical Myoclonus',
 'A patient has brief stimulus-sensitive distal jerks. EEG–EMG back-averaging shows a contralateral cortical potential preceding the hand-muscle burst by about 20 ms. Which interpretation is best?',
 'The finding supports a cortical generator for the myoclonus', [
 ('It proves a purely spinal generator', 'Spinal myoclonus has different recruitment and physiology; a correctly localized time-locked cortical potential preceding the distal burst supports cortical involvement.'),
 ('It establishes a functional cause from the short latency alone', 'A short corticospinal-compatible latency does not establish a functional cause; functional jerks require their own positive clinical and physiological assessment.'),
 ('It identifies one specific degenerative etiology regardless of the history', 'Cortical myoclonus is a physiological classification shared by several metabolic, epileptic, posthypoxic, toxic and degenerative disorders; etiology needs further evaluation.')],
 [S('Generator Localization', '**Jerk-locked EEG–EMG back-averaging** can reveal a small cortical transient that is difficult to see in the raw EEG. A hand-muscle latency compatible with corticospinal conduction supports cortical myoclonus.',
    'Brief EMG bursts, stimulus sensitivity and giant somatosensory evoked potentials can provide additional support. Giant potentials alone are not disease-specific and should be integrated with the other findings.',
    'Negative myoclonus is a brief interruption of muscle activity rather than a positive contraction; the physiology and causes require appropriate classification.'),
  S('Cause-Directed Treatment', '**Review drugs, renal/hepatic dysfunction, glucose/electrolytes, hypoxic injury and epileptic or degenerative disease.** Treat a reversible cause before merely suppressing the movement.',
    'Levetiracetam, valproate or clonazepam can help selected cortical myoclonus. For example, levetiracetam may start at 250–500 mg twice daily with renal adjustment and titration; monitor mood and sedation.',
    'Valproate requires reproductive and liver-safety assessment, and clonazepam can cause sedation and falls. A drug useful for cortical myoclonus may not help a spinal or subcortical generator, making physiological localization clinically useful.')], ['MYO','NEUROPHYS'])

R.update({
 'STROKE': ('AHA/ASA acute ischemic stroke guideline, 2026', 'https://doi.org/10.1161/STR.0000000000000513'),
 'FRDA': ('GeneReviews: Friedreich ataxia', 'https://www.ncbi.nlm.nih.gov/books/NBK1281/'),
 'OMAV': ('Omaveloxolone US prescribing information, 2026', 'https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/216718s014lbl.pdf'),
 'SCA2': ('GeneReviews: Spinocerebellar ataxia type 2', 'https://www.ncbi.nlm.nih.gov/books/NBK1275/'),
 'FMR': ('GeneReviews: FMR1 disorders', 'https://www.ncbi.nlm.nih.gov/books/NBK1384/'),
 'RFC': ('GeneReviews: RFC1-related disorders, updated 2026', 'https://www.ncbi.nlm.nih.gov/books/NBK564656/'),
 'FGF': ('GeneReviews: GAA-FGF14-related ataxia', 'https://www.ncbi.nlm.nih.gov/books/NBK599589/'),
 'EA1': ('GeneReviews: Episodic ataxia type 1', 'https://www.ncbi.nlm.nih.gov/books/NBK25442/'),
 'EATRIAL': ('Randomized crossover trial of fampridine and acetazolamide in EA2, 2021', 'https://pmc.ncbi.nlm.nih.gov/articles/pmid/34484942/'),
 'PNS': ('Updated diagnostic criteria for paraneoplastic neurological syndromes, 2021', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC8237398/'),
})

add('Cerebellar and inherited ataxias', 'Cerebellar Limb and Gait Localization',
 'A patient has right-sided finger–nose dysmetria, intention tremor and dysdiadochokinesia without weakness or proprioceptive loss. Which localization best fits?',
 'Right cerebellar hemisphere or its functional connections', [
 ('Left cerebellar hemisphere as the obligatory site because all motor pathways cross once', 'Cerebellar limb signs are usually ipsilateral because of the relevant circuit anatomy; a simple single-crossing rule is inappropriate.'),
 ('Right dorsal columns as the primary explanation despite preserved proprioception', 'Sensory ataxia from dorsal-column disease typically includes impaired position sense and greater reliance on vision, which are absent in this focal cerebellar pattern.'),
 ('A purely bilateral vestibular deficit without limb involvement', 'Vestibular loss commonly impairs gaze stability and gait but does not by itself explain unilateral limb dysmetria and dysdiadochokinesia.')],
 [S('Ipsilateral Limb Incoordination', '**Cerebellar hemisphere dysfunction** commonly produces ipsilateral limb dysmetria, decomposition, intention tremor and impaired rapid alternating movement.',
    'Vermian or midline dysfunction more prominently affects truncal control and gait. Ocular findings such as gaze-evoked nystagmus and saccadic dysmetria can support cerebellar-system involvement.',
    'Weakness, sensory loss, pain and apraxia can impair coordination tests, so establish that the abnormality reflects incoordination rather than inability to execute the movement.'),
  S('Localization Does Not Establish Etiology', '**The time course directs the next investigation.** Sudden onset raises vascular or toxic concerns; subacute disease suggests immune, infectious, neoplastic or nutritional causes; chronic progression raises degenerative and inherited possibilities.',
    'MRI evaluates cerebellar, brainstem and connected pathways, while targeted laboratory and genetic studies depend on the phenotype. A normal early scan does not exclude every physiological or metabolic cause.',
    'The localization remains useful for urgent decision-making, but should not lead to an automatic hereditary diagnosis or delay acute stroke evaluation when symptoms began abruptly.')], ['ATAX'], style='clinical_scenario')

add('Cerebellar and inherited ataxias', 'Sensory Versus Vestibular Ataxia',
 'A patient becomes markedly unsteady in darkness, has absent vibration and position sense in the feet and reduced sensory nerve action potentials. Limb coordination improves with visual guidance. Which mechanism best explains the dominant ataxia?',
 'Loss of proprioceptive afferent input', [
 ('Pure cerebellar hemispheric degeneration without sensory involvement', 'Cerebellar ataxia can persist despite visual guidance and does not explain the documented proprioceptive and sensory nerve abnormalities.'),
 ('Isolated bilateral vestibular failure', 'Bilateral vestibular loss can worsen balance in darkness, but usually produces impaired vestibulo-ocular responses and oscillopsia rather than loss of joint-position sense with abnormal sensory potentials.'),
 ('Pure corticospinal tract degeneration', 'Corticospinal dysfunction causes weakness and upper motor neuron signs; it does not by itself account for this visual compensation and sensory-afferent deficit.')],
 [S('Dependence on Vision', '**Sensory ataxia** results from impaired proprioceptive input through peripheral sensory neurons, large fibers or central pathways. Visual guidance partly compensates, so balance worsens when the eyes close.',
    'A positive Romberg sign is not specific for one disease and can also occur with vestibular impairment. Interpret it with sensory testing and ocular/vestibular examination.',
    'Reduced sensory potentials support peripheral sensory involvement; preserved potentials with impaired position sense can suggest a more central pathway lesion, depending on the complete study.'),
  S('Combined Balance-System Disease', '**Bilateral vestibulopathy** produces oscillopsia during head movement and impaired vestibulo-ocular reflexes. Cerebellar disease causes additional ocular and limb signs.',
    'RFC1-related disease can combine all three balance-system impairments, so do not force every patient into one isolated category.',
    'Evaluate treatable causes including nutritional deficiency, toxic exposure, immune sensory neuronopathy and structural cord disease. Rehabilitation should account for sensory substitution, lighting and fall prevention.')], ['ATAX','RFC'], table=(['Dominant mechanism','Discriminating clues'],[
 ['Cerebellar','Dysmetria, dysarthria, cerebellar ocular signs'],['Sensory','Position/vibration loss; visual compensation'],['Bilateral vestibular','Oscillopsia; abnormal head-impulse/VOR testing'],['Combined','Features from more than one system; consider CANVAS/RFC1']]))

add('Cerebellar and inherited ataxias', 'Acute Cerebellar Ataxia Requires Urgent Assessment',
 'A hypertensive adult develops sudden vertigo, severe gait/truncal ataxia and dysarthria. An initial noncontrast CT shows no hemorrhage. Which next approach is most appropriate?',
 'Continue urgent posterior-circulation stroke evaluation with appropriate vascular and posterior-fossa imaging', [
 ('Discharge with a diagnosis of vestibular neuritis because CT is normal', 'A normal early CT does not reliably exclude posterior-fossa ischemia, and dysarthria with severe truncal/gait ataxia is concerning for a central process.'),
 ('Order an outpatient hereditary ataxia panel before further acute imaging', 'Inherited disease usually has a different tempo; genetic testing does not replace time-critical evaluation of abrupt focal neurological dysfunction.'),
 ('Treat only with vestibular suppressants and wait several days for improvement', 'Symptom relief does not exclude stroke. Waiting can miss reperfusion opportunities and evolving posterior-fossa swelling or hydrocephalus.')],
 [S('Posterior Circulation Warning Pattern', '**Sudden severe ataxia with dysarthria** warrants urgent stroke assessment. CT is useful for hemorrhage but is relatively insensitive for early posterior-fossa ischemia.',
    'Use vascular imaging and MRI with diffusion sequences according to the acute pathway and clinical circumstances. Even early diffusion MRI can occasionally be falsely negative in posterior-circulation disease.',
    'Do not delay eligible acute treatment solely to obtain a preferred image. Bedside vestibular algorithms require the correct clinical syndrome and trained examination; they are not a universal substitute for stroke assessment.'),
  S('Deterioration from Cerebellar Infarction', '**Swelling can cause brainstem compression and obstructive hydrocephalus.** New reduced consciousness or worsening cranial-nerve/brainstem findings require urgent repeat assessment and neurosurgical input.',
    'CSF diversion may be needed for obstructive hydrocephalus. Neurological deterioration from swelling or persistent compression can require decompressive suboccipital surgery under current AHA/ASA guidance.',
    'Serial examination, airway protection and appropriate monitored care are essential. An initially small clinical deficit does not guarantee a benign posterior-fossa course.')], ['STROKE'])

add('Cerebellar and inherited ataxias', 'Friedreich Ataxia: Multisystem Recognition',
 'A teenager has progressive gait ataxia, loss of position sense, absent ankle reflexes, extensor plantar responses, pes cavus and hypertrophic cardiomyopathy. Which diagnosis best fits?',
 'Friedreich ataxia', [
 ('Ataxia with vitamin E deficiency as already excluded without testing', 'Vitamin E deficiency can closely mimic Friedreich ataxia and should be tested, but the described multisystem pattern strongly suggests FRDA and requires molecular confirmation.'),
 ('Pure dominant SCA6 without extracerebellar disease', 'SCA6 often presents as a relatively pure later-onset cerebellar syndrome; this adolescent sensory-pyramidal and cardiomyopathic pattern is less typical.'),
 ('RFC1-associated CANVAS as the usual adolescent cardiomyopathy syndrome', 'RFC1 disease commonly presents later with sensory and vestibular involvement and cough; adolescent cardiomyopathy is not its characteristic defining pattern.')],
 [S('Frataxin Deficiency', '**Friedreich ataxia** is usually caused by biallelic intronic GAA expansions in FXN, reducing frataxin and impairing mitochondrial iron–sulfur biology. Less common alleles include sequence variants or deletions.',
    'The classic phenotype combines cerebellar/sensory ataxia, areflexia and pyramidal signs. Retained reflexes and late-onset forms exist, so absence of a single classic sign does not exclude FRDA.',
    'Assess ECG/echocardiography, glucose regulation, scoliosis, foot deformity, hearing, vision and swallowing in addition to motor disability.'),
  S('Therapy and Monitoring', '**Omaveloxolone** has a US indication for FRDA in adults and adolescents aged at least sixteen years. The usual dose is 150 mg orally once daily on an empty stomach under the cited label.',
    'Check ALT, AST, bilirubin, BNP and lipids before and during treatment; review CYP3A interactions and relevant dose adjustments. Benefit does not mean cure or removal of the need for cardiac and metabolic care.',
    'Genetic counselling and multidisciplinary rehabilitation remain central. A recessive pedigree may have no affected parent, and a routine sequencing result does not replace appropriate expansion analysis.')], ['FRDA','OMAV'])

add('Cerebellar and inherited ataxias', 'A Discriminating Clue in Dominant SCA',
 'Several generations have progressive ataxia. Affected members have strikingly slow saccades and peripheral neuropathy. Which common repeat-expansion SCA is particularly suggested?',
 'SCA2', [
 ('SCA6', 'SCA6 commonly produces a relatively pure cerebellar syndrome with nystagmus; marked slow saccades and neuropathy more strongly suggest SCA2, though overlap exists.'),
 ('SCA7', 'SCA7 is especially associated with retinal degeneration and visual loss; slow saccades can occur but are less discriminating than the characteristic retinal phenotype.'),
 ('SCA3', 'SCA3 can combine ataxia, pyramidal/extrapyramidal signs and neuropathy, but exceptionally slow saccades are a particularly useful SCA2 clue; genetic testing is still necessary.')],
 [S('Phenotype-Guided Genetic Testing', '**SCA2 is an ATXN2 CAG-repeat disorder** with autosomal dominant inheritance. Slow saccades, ataxia, dysarthria and neuropathy are useful clinical clues.',
    'Phenotypic overlap is substantial, and some SCA2 cases present with levodopa-responsive parkinsonism. A bedside clue guides testing rather than proving the subtype.',
    'Anticipation can occur in repeat disorders, but family-specific counselling depends on the gene and repeat behavior.'),
  S('Common Comparisons', '**SCA1** often has prominent pyramidal/bulbar involvement; **SCA3** can have mixed pyramidal, extrapyramidal and peripheral features; **SCA6** is often relatively pure cerebellar disease; **SCA7** adds retinal degeneration.',
    'Choose a validated repeat-expansion strategy rather than assuming all common SCAs are excluded by a sequence-only panel. Review exactly which loci and repeat structures the laboratory assesses.',
    'Assess swallowing, mobility, neuropathy, vision and family support according to the phenotype. Subtype identification informs prognosis and family counselling even when treatment remains mainly symptomatic.')], ['SCA2','ATAX'], style='clinical_scenario', table=(['Subtype','Gene','Useful clue'],[
 ['SCA1','ATXN1','Pyramidal/bulbar signs'],['SCA2','ATXN2','Marked slow saccades; neuropathy'],['SCA3','ATXN3','Mixed pyramidal/extrapyramidal/peripheral findings'],['SCA6','CACNA1A','Relatively pure cerebellar phenotype'],['SCA7','ATXN7','Retinal degeneration/visual loss']]))

add('Cerebellar and inherited ataxias', 'Fragile X-Associated Tremor/Ataxia Syndrome',
 'A 69-year-old man has intention tremor, gait ataxia and neuropathy. MRI shows middle cerebellar peduncle white-matter abnormalities. His daughter has premature ovarian insufficiency. Which test is most relevant?',
 'FMR1 CGG-repeat analysis for a premutation', [
 ('HTT CAG-repeat testing as the leading explanation of this phenotype', 'HTT testing is relevant to Huntington phenotypes with chorea and cognitive/behavioral change; the tremor–ataxia plus ovarian family history points toward an FMR1 premutation.'),
 ('FXN expansion analysis as the only appropriate late-onset test', 'FRDA can occasionally be late onset, but this specific family and middle-peduncle pattern favors FXTAS; testing should follow the complete phenotype.'),
 ('A conventional karyotype alone to detect the relevant repeat size', 'A karyotype does not provide the molecular repeat sizing and methylation-related information used to classify FMR1 alleles.')],
 [S('Premutation-Associated Disease', '**FXTAS** most often affects older FMR1 premutation carriers, particularly men, with action/intention tremor, gait ataxia and variable neuropathy, parkinsonism or cognitive/autonomic features.',
    'The premutation range is approximately 55–200 CGG repeats. This differs from the usually methylated full mutation associated with fragile X syndrome.',
    'Middle cerebellar peduncle signal change is a useful imaging clue but is not uniquely diagnostic and is less consistently present in affected women.'),
  S('Family Implications', '**FMR1 premutations also confer risk of fragile X-associated primary ovarian insufficiency** in women. A pedigree may therefore link late-life ataxia with reproductive or neurodevelopmental findings in relatives.',
    'Premutation carriers do not all develop FXTAS; penetrance varies with age, sex and repeat-related factors. Genetic counselling should address transmission patterns and the possibility of expansion through maternal transmission.',
    'Care is mainly supportive and symptom directed, including mobility, cognition, neuropathy and autonomic assessment. Do not equate a carrier result with a guaranteed neurological prognosis.')], ['FMR'])

add('Cerebellar and inherited ataxias', 'RFC1-Related CANVAS',
 'A 62-year-old has slowly progressive ataxia, a sensory neuronopathy, bilateral vestibular hypofunction and a chronic unexplained cough predating imbalance. A sequence-only exome was negative. Which next test is most appropriate?',
 'Targeted testing for biallelic pathogenic RFC1 repeat expansions', [
 ('Exclude an inherited cause because exome sequencing was negative', 'A sequence-only exome can miss intronic repeat expansions; a negative result does not exclude the specific molecular mechanism strongly suggested here.'),
 ('Use a single heterozygous RFC1 expansion as sufficient proof of recessive disease', 'The common RFC1 disease mechanism is biallelic. One detected allele requires assessment of the other allele and the laboratory’s ability to detect relevant repeat configurations.'),
 ('Diagnose MSA solely because ataxia and autonomic symptoms can coexist', 'MSA remains a differential in adult-onset ataxia, but sensory neuronopathy, bilateral vestibular failure and longstanding cough are particularly suggestive of RFC1-related disease.')],
 [S('Three Balance Systems', '**CANVAS** combines cerebellar ataxia, sensory neuropathy/neuronopathy and bilateral vestibular areflexia. RFC1-related disease can also involve only part of this spectrum.',
    'Chronic cough can precede neurological symptoms by years. Vestibular loss causes oscillopsia and impaired vestibulo-ocular responses; sensory neuronopathy can markedly worsen balance in darkness.',
    'Autonomic symptoms may occur and should not automatically redirect the diagnosis to MSA.'),
  S('Testing the Molecular Mechanism', '**Biallelic intronic RFC1 repeat expansions** are a major cause. The common pathogenic motif is AAGGG, but additional pathogenic repeat configurations exist and test coverage matters.',
    'Conventional sequence-based panels or exomes do not reliably exclude the expansion. Use a validated repeat assay and discuss unresolved cases with the laboratory or a neurogenetics service.',
    'Provide gait and vestibular rehabilitation, sensory-compensation advice, swallowing assessment and cough/autonomic care as needed. A recessive adult-onset disorder can occur without an obvious family history.')], ['RFC'])

add('Cerebellar and inherited ataxias', 'FGF14 GAA-Expansion Ataxia',
 'A 65-year-old has gradually progressive gait ataxia with episodic worsening after alcohol or exertion and downbeat nystagmus. Common SCA expansion testing and routine exome sequencing are unrevealing. Which recently recognized cause should be specifically assessed?',
 'GAA-repeat expansion in FGF14, also called SCA27B', [
 ('An HTT expansion as the characteristic cause of downbeat episodic ataxia', 'Huntington disease is primarily a cognitive/behavioral and choreic or rigid syndrome; this late-onset episodic cerebellar pattern more specifically suggests FGF14 expansion disease.'),
 ('A full FMR1 mutation as the usual mechanism of late-onset FXTAS', 'FXTAS usually involves an FMR1 premutation, not the classic full mutation; the episodic/downbeat phenotype here particularly raises FGF14 disease.'),
 ('GCH1 deficiency as excluded or confirmed by the exome without considering the phenotype', 'GCH1-related dopa-responsive dystonia typically presents with dystonia and levodopa responsiveness, not this characteristic late-onset cerebellar syndrome.')],
 [S('Late-Onset Expansion Disorder', '**GAA-FGF14-related ataxia** often causes slowly progressive adult-onset cerebellar gait dysfunction, downbeat nystagmus and episodic exacerbations, sometimes triggered by alcohol or exertion.',
    'It is an autosomal dominant intronic expansion disorder. Expansions above 300 repeats are generally considered fully penetrant; 250–300 repeats have reduced penetrance and require careful clinical and family interpretation.',
    'A routine exome or a historical panel that omitted the expansion does not exclude it. Confirm the laboratory’s repeat-detection method and coverage.'),
  S('Counselling and Symptomatic Care', '**Clinical phenotype and segregation matter**, especially in a reduced-penetrance range. Do not treat every borderline expansion as a complete explanation without considering other causes.',
    'Preliminary studies suggest symptomatic benefit from 4-aminopyridine for selected symptoms, including downbeat nystagmus, but this should not be described as proven disease modification or a universal approved indication.',
    'Review seizure history, renal function and formulation-specific safety before considering an aminopyridine. Rehabilitation, fall prevention and trigger counselling remain important while longer-term therapeutic evidence evolves.')], ['FGF'])

add('Cerebellar and inherited ataxias', 'Episodic Ataxia Type 2',
 'A young adult has recurrent hours-long attacks of vertigo, dysarthria and ataxia, with interictal downbeat nystagmus. Several relatives are affected. Which pairing best fits?',
 'CACNA1A-related EA2 — consider acetazolamide or specialist-guided aminopyridine therapy', [
 ('KCNA1-related EA1 — hours-long attacks with interictal nystagmus are its defining classic pattern', 'Classic EA1 more often has brief seconds-to-minutes attacks and interictal myokymia, although phenotypic variability prevents an absolute duration rule.'),
 ('FXN-related FRDA — acetazolamide is established as corrective therapy for frataxin deficiency', 'FRDA usually produces progressive multisystem disease; acetazolamide is not a corrective therapy for the underlying frataxin defect.'),
 ('PRKN-related parkinsonism — episodic cerebellar attacks are its characteristic presentation', 'PRKN disease primarily produces early-onset parkinsonism and dystonia, not the familial episodic cerebellar/ocular pattern described.')],
 [S('Channelopathy Comparison', '**EA2 is commonly caused by pathogenic CACNA1A variants**, affecting the P/Q-type calcium channel. Longer ataxic attacks and interictal nystagmus are useful clues.',
    'EA1 is commonly KCNA1-related, affecting a potassium channel, and classically combines short attacks with myokymia. Duration and associated signs overlap, so genetic confirmation is important.',
    'CACNA1A also causes familial hemiplegic migraine and SCA6 through different variant mechanisms; the gene name alone does not specify the clinical disorder.'),
  S('Attack Prevention', '**Acetazolamide and prolonged-release fampridine reduced attacks** in a 2021 randomized crossover EA2 study. The tested regimens were acetazolamide 250 mg three times daily and fampridine 10 mg twice daily.',
    'Start and titrate according to the individual rather than assuming the trial dose is universally suitable. Acetazolamide can cause paresthesias, metabolic acidosis, electrolyte disturbance and renal stones; review renal function and contraindications.',
    'Aminopyridines require seizure and renal-risk assessment and may be off label depending on jurisdiction. Trigger management and safety planning are useful alongside medication.')], ['EA1','EATRIAL'])

add('Cerebellar and inherited ataxias', 'Treatable Causes of Progressive Ataxia',
 'A young adult has a Friedreich-like ataxia with sensory loss and areflexia, but FXN testing is negative. Which readily actionable investigation should not be omitted?',
 'Vitamin E assessment interpreted with the lipid profile', [
 ('Assume all Friedreich-like phenotypes are genetically untreatable', 'Several metabolic and nutritional disorders can mimic FRDA, including vitamin E deficiency, so a negative FXN result should not end the reversible-cause evaluation.'),
 ('Exclude nutritional disease because brain MRI is normal', 'Nutritional or metabolic dysfunction can be clinically important before characteristic structural MRI changes appear; imaging does not replace biochemical assessment.'),
 ('Start a gluten-free diet in every patient without diagnostic evaluation', 'Gluten-associated ataxia is a relevant consideration in selected cases, but indiscriminate diet treatment can obscure testing and overlooks alternative actionable causes.')],
 [S('Vitamin E Deficiency as a Mimic', '**Ataxia with vitamin E deficiency** can resemble FRDA and may result from malabsorption or TTPA-related disease. Interpret alpha-tocopherol in relation to lipid status rather than an isolated concentration alone.',
    'Timely replacement can stabilize or improve selected manifestations, especially before advanced irreversible injury. Investigate the underlying cause and monitor response and biochemical levels.',
    'The presence of a hereditary phenotype does not exclude a treatable metabolic disorder.'),
  S('Broader Reversible-Cause Screen', '**B12 and copper deficiency, thyroid disease, alcohol and medications** are important additional causes or contributors. Phenytoin, lithium and sedative toxicity should be considered from the exposure history.',
    'Suspected Wernicke encephalopathy needs prompt parenteral thiamine rather than waiting for a vitamin result. Correct hypoglycemia immediately while arranging thiamine; do not delay lifesaving glucose.',
    'For possible celiac/gluten-related disease, obtain appropriate serology, including total IgA with IgA-based testing, before dietary exclusion when feasible. Immune and nutritional evaluations should be phenotype guided rather than a nonspecific antibody panel replacing clinical reasoning.')], ['ATAX','FRDA'])

add('Cerebellar and inherited ataxias', 'Rapidly Progressive Paraneoplastic Cerebellar Syndrome',
 'A 58-year-old woman develops severe gait and limb ataxia over six weeks. MRI is initially near normal. Anti-Yo/PCA-1 is confirmed with an appropriate assay. Which next priority is most appropriate?',
 'Investigate a compatible underlying malignancy, particularly breast or gynecological cancer, while assessing other causes and treatment', [
 ('Exclude an immune cerebellar syndrome because MRI lacks atrophy', 'Early paraneoplastic cerebellar disease can have little structural MRI change; a normal-appearing scan does not negate the rapidly progressive phenotype.'),
 ('Treat the antibody result as proof of a specific cancer without locating it', 'A high-risk antibody guides cancer evaluation but does not identify a particular tumor or replace appropriate imaging and tissue diagnosis.'),
 ('Limit evaluation to hereditary repeat testing because adult-onset ataxia is usually genetic', 'A six-week severe cerebellar decline is a red flag for acquired disease; inherited testing must not displace the urgent immune, cancer and other acquired-cause workup.')],
 [S('High-Risk Phenotype and Antibody', '**Rapidly progressive cerebellar syndrome** is a high-risk paraneoplastic phenotype in the 2021 criteria. Anti-Yo is strongly associated with breast and gynecological malignancies.',
    'Other associations include DNER/Tr with Hodgkin lymphoma and Hu with small-cell lung cancer, often with additional neurological involvement. These are associations, not a substitute for confirmation.',
    'Verify unexpected results with appropriate methods because commercial panels can produce false positives, particularly when the phenotype is discordant.'),
  S('Evaluation and Management', '**Search for and treat the tumor promptly**, while excluding direct CNS tumor involvement, infection, toxic/metabolic causes and nonparaneoplastic autoimmunity.',
    'For a high-risk phenotype with a high-risk antibody and initially negative cancer screening, the 2021 panel recommends repeat screening every four to six months for two years, individualized to the clinical context.',
    'Immunotherapy may be considered with specialist input, but responses to intracellular-antigen syndromes such as anti-Yo can be limited because neuronal injury may be irreversible. Rehabilitation, swallowing and nutrition care should start alongside the etiologic workup.')], ['PNS','ATAX'])

# Final editorial refinements: replace categorical/giveaway alternatives with real
# competing diagnoses or strategies, preserving the mapped decision sequence.
R['ATAXGEN'] = ('GeneReviews: Hereditary ataxia overview, updated 2026', 'https://www.ncbi.nlm.nih.gov/books/NBK1138/')
R['AVED'] = ('GeneReviews: Ataxia with vitamin E deficiency', 'https://www.ncbi.nlm.nih.gov/books/NBK1241/')
rows[45]['refs'].append('ATAXGEN')
rows[50]['refs'].append('AVED')
rows[50]['sections'][0][1][0][1].append('For confirmed AVED, reported adult replacement regimens use 800–1500 mg/day of oral vitamin E, adjusted to the preparation and biochemical response under specialist supervision. Do not interchange milligrams and international units without accounting for the formulation.')
rows[20]['sections'][1][1][0] = (
 '**Unexplained voiding difficulty with substantial postvoid residual**, urinary urge incontinence or neurogenic OH can supply the autonomic component after alternatives are excluded.',
 ['The 2022 paper lists a residual threshold of at least 100 mL in its summary table but greater than 100 mL in its operational lexicon. A value clearly above 100 mL satisfies both. Clinical interpretation should not hinge on one exactly borderline measurement; assess repeated findings and competing causes.',
  'Neurogenic OH uses a systolic fall of at least 20 mmHg, usually accompanied by a diastolic fall of at least 10 mmHg, with a blunted HR response. Established criteria use three minutes and probable criteria allow up to ten minutes.',
  'A delta-HR/delta-systolic-BP ratio below 0.5 beats/min per mmHg supports the operational neurogenic definition, after accounting for rate-limiting drugs, rhythm disease and other confounders.',
  'Exclude obstruction, diabetic autonomic neuropathy, volume depletion and relevant medications. Clinically established cerebellar disease requires at least two cerebellar features; probable disease can use one. A checklist without these operational qualifications risks overdiagnosis.'])
rows[21]['others'] = [
 ('A dominant spinocerebellar ataxia such as SCA3', 'SCA3 can produce ataxia, autonomic symptoms and overlapping MRI patterns; family history and genetic testing matter, although the described rapidly evolving severe autonomic-pontocerebellar combination strongly supports considering MSA-C.'),
 ('RFC1-related CANVAS', 'RFC1 disease can include ataxia and autonomic symptoms, but a sensory neuronopathy, bilateral vestibular loss and longstanding cough would particularly support it; these should be actively sought rather than inferred from the MRI.'),
 ('Immune-mediated cerebellar ataxia', 'Immune disease can produce acquired ataxia and requires evaluation when the tempo or associated features suggest it, but this combined autonomic and degenerative MRI phenotype particularly raises MSA-C.')]
rows[23]['others'] = [
 ('Diagnose idiopathic PD and start indefinite levodopa without reviewing metoclopramide', 'PD can be unmasked by dopamine blockade, but the relevant medication exposure should first be reviewed; persistence and progression after withdrawal help determine the subsequent workup.'),
 ('Treat the motor syndrome with long-term trihexyphenidyl while maintaining the same antiemetic', 'Anticholinergics may relieve selected drug-induced symptoms, but leaving an avoidable offending exposure unchanged and adding chronic toxicity is less appropriate than reviewing the cause.'),
 ('Obtain DAT imaging before making any medication change', 'DAT imaging can help unresolved cases or suspected unmasked degeneration, but is not usually needed before reviewing an evidently relevant dopamine blocker and a feasible alternative.')]
rows[28]['others'] = [
 ('Essential tremor with ordinary task-related amplitude variation', 'ET amplitude can vary with task and anxiety, but reproducible frequency adoption during contralateral paced tapping together with distraction-related suppression supports a functional component.'),
 ('Dystonic tremor defined solely by irregularity', 'Dystonic tremor can be irregular and task sensitive, but requires an appropriate dystonic phenotype; entrainment and marked distractibility are positive functional signs rather than sufficient evidence of dystonia.'),
 ('Parkinsonian re-emergent tremor', 'Re-emergent tremor returns after adopting a posture and is assessed alongside bradykinesia/rigidity; the specific reproducible entrainment and distractibility here favor a functional explanation.')]
rows[33]['others'] = [
 ('An intermediate allele with transmission instability but not the conventional disease-associated range', 'Intermediate alleles conventionally contain 27–35 repeats; 38 is within the reduced-penetrance disease-associated range and requires different counselling.'),
 ('A full-penetrance allele with the same interpretation as a 45-repeat result', 'Forty or more repeats is the conventional full-penetrance range. A 38-repeat result cannot be assigned the same penetrance expectation.'),
 ('A normal-range allele without a Huntington-related reproductive implication', 'Normal alleles are conventionally 26 or fewer repeats. A 38-repeat allele has both personal risk and reproductive implications that require formal counselling.')]
rows[36]['others'] = [
 ('Serum ceruloplasmin and total copper alone, followed by a decision without further testing', 'These are useful components, but neither normal ceruloplasmin nor low total copper independently rules disease out or in; the young neurological phenotype warrants a composite assessment.'),
 ('Brain MRI and a levodopa-response trial as the principal confirmation tests', 'MRI can support the differential and a levodopa trial may help selected symptoms, but neither confirms ATP7B-related copper disease or replaces copper and ophthalmic evaluation.'),
 ('Liver ultrasound and routine liver enzymes as the principal exclusion tests', 'These assess hepatic structure and injury but may be nonspecific or relatively mild in neurological Wilson disease; they cannot replace specific copper and ophthalmic studies.')]
rows[37]['others'] = [
 ('Begin full-dose penicillamine immediately rather than gradual introduction', 'Penicillamine is a valid chelator, but rapid introduction can increase concern about paradoxical neurological worsening; neurological disease supports cautious escalation and close follow-up.'),
 ('Choose zinc monotherapy without first assessing the severity of hepatic involvement', 'Zinc can be appropriate in selected neurological or maintenance settings, but significant liver disease favors chelation; the hepatic assessment is necessary before choosing it.'),
 ('Switch to dietary copper restriction alone once the first clinical improvement occurs', 'Dietary measures can complement therapy but do not provide adequate ongoing copper control in established Wilson disease; improvement is not a reason to stop effective anti-copper treatment.')]
rows[44]['others'] = [
 ('Ataxia with vitamin E deficiency', 'AVED can closely mimic FRDA and should be tested because it is treatable; the cardiomyopathy and classic sensory-pyramidal combination particularly support FRDA, pending molecular confirmation.'),
 ('SCA6', 'SCA6 often causes relatively pure later-onset cerebellar disease, making adolescent sensory loss, pyramidal signs and cardiomyopathy a less typical fit.'),
 ('RFC1-related CANVAS', 'CANVAS usually presents later with sensory neuronopathy and vestibular impairment, often with cough; adolescent cardiomyopathy is much more suggestive of the FRDA pattern described.')]
rows[47]['others'] = [
 ('FMR1 CGG-repeat analysis', 'FMR1 testing is relevant for late-onset tremor–ataxia, especially with a fragile-X/ovarian family history, but the sensory-neuronopathy, vestibular and cough combination particularly favors RFC1.'),
 ('FGF14 GAA-repeat analysis', 'FGF14 expansions can cause late-onset cerebellar disease, often with episodic exacerbations and downbeat nystagmus; marked sensory neuronopathy and vestibular failure with cough more specifically suggest RFC1.'),
 ('FXN GAA-repeat analysis', 'FRDA can be late onset and combines sensory and cerebellar dysfunction, but the full vestibular–cough CANVAS pattern makes targeted RFC1 testing the stronger next choice.')]
rows[48]['others'] = [
 ('Biallelic RFC1 expansions', 'RFC1 disease is a major late-onset ataxia cause, but prominent sensory neuronopathy, bilateral vestibular impairment and chronic cough would strengthen it; episodic worsening and downbeat nystagmus are useful FGF14 clues.'),
 ('An FMR1 premutation', 'FXTAS can cause late-onset tremor and ataxia, particularly in men, with neuropathy and characteristic family/MRI clues; the described episodic cerebellar/ocular phenotype particularly suggests FGF14 expansion disease.'),
 ('Biallelic FXN expansions', 'Late-onset FRDA is possible, but a sensory-pyramidal syndrome and relevant systemic manifestations would be more supportive than the predominantly episodic/downbeat pattern here.')]
rows[49]['others'] = [
 ('KCNA1-related EA1 — consider a channelopathy-directed preventive regimen', 'EA1 is a genuine competing episodic ataxia, but classically has brief attacks and interictal myokymia; hours-long attacks with interictal downbeat nystagmus favor EA2.'),
 ('CACNA1A CAG-expansion SCA6 — focus on a progressive cerebellar syndrome', 'SCA6 can begin episodically, but usually has later-onset progressive disease; a young adult with recurrent prolonged attacks particularly raises EA2 variant disease rather than the SCA6 repeat mechanism.'),
 ('FGF14 GAA-expansion SCA27B — consider a late-onset episodic/progressive phenotype', 'FGF14 disease can have episodic exacerbations and downbeat nystagmus, but its usual later onset contrasts with the classic younger familial EA2 presentation; molecular testing resolves overlap.')]
rows[50]['others'] = [
 ('FMR1 premutation testing as the most directly actionable first screen', 'FXTAS testing is appropriate in an older tremor–ataxia phenotype or a suggestive family, whereas a young FRDA-like sensory syndrome warrants checking a treatable vitamin E deficiency.'),
 ('Dopamine-transporter SPECT as the principal biochemical investigation', 'DAT imaging is useful in selected uncertain parkinsonism/tremor cases, but does not detect a nutritional cause of sensory-pyramidal ataxia.'),
 ('Serum anti-Yo testing as the leading test without a rapid acquired course', 'Anti-Yo evaluation can be relevant to rapidly progressive paraneoplastic cerebellar disease; the stated young FRDA-like phenotype more directly supports a metabolic/nutritional screen.')]
rows[51]['others'] = [
 ('Repeat MRI only after several months before beginning a tumor search', 'Follow-up MRI may show evolution, but waiting for atrophy can delay investigation of a high-risk antibody and rapidly progressive phenotype that already justify cancer screening.'),
 ('Order a hereditary ataxia panel before considering acquired causes', 'Genetic testing can help unexplained chronic ataxia, but the six-week course and confirmed anti-Yo result prioritize acquired and cancer-associated evaluation.'),
 ('Treat as nonparaneoplastic autoimmune ataxia without malignancy screening', 'Some immune ataxias are nonparaneoplastic, but anti-Yo is a high-risk cancer-associated antibody; immunotherapy should not displace the tumor search.')]

# Apply the requested subtle threshold/dose highlighting only in teaching text.
_highlights = [
 '25/100 mg three times daily', '70–100 mg/day', '0.5 mg/day', '1 mg orally daily',
 'fourteen days', '200 mg with each levodopa dose', '50 mg once daily at bedtime',
 '100 mg twice daily', '100 mg daily', '34 mg once daily', '2.5 mg two or three times daily',
 '10 mg three times daily', 'four hours before bedtime', '3 mg at bedtime',
 '0.25–0.5 mg at bedtime', '13–18 Hz', '12.5–25 mg at bedtime',
 'benztropine 1–2 mg IM/IV', 'diphenhydramine 25–50 mg IM/IV',
 '25–50 mg levodopa one to three times daily', '36–39', '27–35',
 '12.5 mg daily', '50 mg/day', '40 mg once daily', '14 mg/dL', '100 µg/day',
 '750–1500 mg/day', '50 mg elemental zinc three times daily',
 '250–500 mg twice daily', '150 mg orally once daily', '55–200 CGG repeats',
 '250–300 repeats', '250 mg three times daily', '10 mg twice daily', '800–1500 mg/day',
 'every four to six months for two years'
]
def _highlight(text):
    # Longest match first prevents short dose strings from splitting longer ones.
    import re
    return re.sub('|'.join(re.escape(x) for x in sorted(_highlights,key=len,reverse=True)),lambda m:'=='+m.group()+'==',text)
for _row in rows:
    _row['sections'] = [(h,[(_highlight(t),[_highlight(x) for x in children]) for t,children in bullets]) for h,bullets in _row['sections']]

# Save only once all mapped decisions have been completed and reviewed.
if __name__ == '__main__':
    coverage = ROOT/'Neurology/07. Movement Disorders & Cerebellar Ataxias.coverage.json'
    c = json.loads(coverage.read_text(encoding='utf-8'))
    assert len(rows) == sum(s['questions'] for s in c['sections']) == c['plannedQuestions'], 'Incomplete chapter; do not install'
    index = 0
    for section in c['sections']:
        assert len(section['decisions']) == section['questions']
        for decision in section['decisions']:
            assert rows[index]['topic'] == section['section']
            rows[index]['coverageDecision'] = decision
            index += 1
    save('Neurology',7,c['chapter'],rows,R,'Original postgraduate educational synthesis with a documented decision coverage map. Source versions and limitations are stated in explanations. Full Harrison subscription text was not accessed and no independent clinician review is claimed.')
    c.update(status='authored_validated',authoredQuestions=len(rows))
    c['questionDecisions'] = [dict(question=i+1,title=r['title'],decision=r['coverageDecision']) for i,r in enumerate(rows)]
    coverage.write_text(json.dumps(c,ensure_ascii=False,indent=2),encoding='utf-8')
