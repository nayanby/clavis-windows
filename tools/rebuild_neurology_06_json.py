"""Original demyelinating disorders chapter; incremental draft, not yet installed."""
import json
from qbank_json_chapters import question as Q, save, ROOT

R = {
 'MC24': ('Montalban et al. Diagnosis of multiple sclerosis: 2024 revisions of the McDonald criteria. Lancet Neurology, 2025', 'https://cdn.sebia.com/wp-content/uploads/Montalban-2025.pdf'),
 'NEMOS1': ('NEMOS revised NMOSD recommendations, Part I: diagnosis and differential diagnosis, 2023', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC10267280/'),
 'MOG23': ('International MOGAD Panel proposed diagnostic criteria, 2023', 'https://pubmed.ncbi.nlm.nih.gov/36706773/'),
}

def S(h, main, *children): return (h, [(main, list(children))])
rows = []
def add(*a, **kw): rows.append(Q(*a, **kw))

add('MS diagnosis and classification', 'A Typical Clinically Isolated Syndrome',
 'A 27-year-old develops painful monocular visual loss over two days. Examination shows impaired colour vision and a relative afferent pupillary defect; orbital MRI demonstrates a short enhancing optic-nerve lesion. Which classification is most appropriate before the remaining diagnostic evaluation?',
 'A typical clinically isolated demyelinating syndrome requiring etiologic evaluation', [
 ('Radiologically isolated syndrome without a clinical attack', 'Radiologically isolated presentations have incidentally detected characteristic lesions without a corresponding clinical attack; this patient has objective symptomatic optic-nerve dysfunction.'),
 ('Primary progressive MS established by this single episode', 'Progressive-onset disease requires sustained progression over at least twelve months, not a subacute focal attack evolving over two days.'),
 ('A nonspecific neurological presentation without objective localization', 'Nonspecific sensory complaints or fatigue may lack objective localization, whereas the pupillary, colour-vision and MRI findings here localize a genuine optic neuropathy.')],
 [S('Clinical Pattern', '**A clinically isolated syndrome** is a first clinical episode compatible with inflammatory CNS demyelination; the label describes the presentation rather than establishing its final cause.',
    'Typical presentations include unilateral optic neuritis, a focal brainstem syndrome and partial myelitis. Symptoms generally persist at least 24 hours and should not be better explained by fever, infection or another disorder.',
    'The objective examination and anatomically concordant imaging make this presentation substantially more specific than fatigue, headache or brief nonlocalizing paresthesias.'),
  S('Etiologic Evaluation', '**MS, MOGAD and AQP4-positive NMOSD** are distinct potential causes of inflammatory optic neuritis. MRI of brain and spinal cord, CSF where indicated and phenotype-directed serum antibody testing refine the diagnosis.',
    'Severe bilateral involvement, marked disc swelling, chiasmal involvement, longitudinally extensive disease or poor recovery should prompt particular attention to alternatives. None of these patterns is independently diagnostic.',
    'Under the 2024 McDonald revisions, the optic nerve can contribute to dissemination in space, but a single optic-nerve attack does not by itself fulfill every requirement for MS. Apply the appropriate pathway only after excluding a better explanation.')], ['MC24','NEMOS1','MOG23'])

add('MS diagnosis and classification', 'MRI Lesion Morphology in Suspected MS',
 'A 59-year-old with hypertension and migraine has several punctate deep-white-matter lesions. Which additional MRI finding would most specifically strengthen suspicion for MS?',
 'Ovoid periventricular lesions oriented perpendicular to the ventricular surface', [
 ('Small rounded deep-white-matter lesions separated from the cortex', 'These lesions commonly accompany migraine or vascular disease; their presence without characteristic morphology or distribution does not provide strong MS-specific evidence.'),
 ('Symmetric confluent periventricular signal with lacunes and microbleeds', 'Confluent white-matter disease with lacunes and microbleeds often supports small-vessel injury, particularly in an older hypertensive patient, although coexistence remains possible.'),
 ('A solitary tiny subcortical focus without ventricular or cortical contact', 'A nonspecific isolated subcortical focus is common in several conditions and should not be mislabeled as a periventricular or juxtacortical MS lesion.')],
 [S('Anatomical Specificity', '**Dawson-finger morphology** reflects lesions extending along periventricular medullary veins. Ovoid lesions perpendicular to the ventricles, callosal involvement and characteristic cortical/juxtacortical disease strengthen the imaging pattern.',
    'A periventricular lesion must contact the ventricle; a juxtacortical lesion must abut cortex without intervening normal white matter. Merely being near either structure is insufficient.',
    'Lesion count alone cannot convert an atypical vascular pattern into MS. Consider size, shape, orientation, anatomical distribution and clinical concordance.'),
  S('Avoiding Misdiagnosis', '**Migraine and cerebral small-vessel disease** are frequent sources of nonspecific MRI abnormalities, particularly when the clinical presentation does not resemble an inflammatory attack.',
    'In patients aged 50 years or older or with vascular risk factors, the 2024 recommendations strongly favour additional specificity evidence, such as characteristic spinal cord lesions, positive CSF or an appropriate central vein sign assessment.',
    'A typical-looking individual lesion is supportive rather than independently conclusive. Review the whole scan, clinical history and alternative explanations before applying a diagnostic algorithm.')], ['MC24'], style='clinical_scenario')

add('MS diagnosis and classification', 'Dissemination in Space: The 2024 Framework',
 'Which anatomical region was added as a fifth location for dissemination in space in the 2024 McDonald revisions published in 2025?',
 'Optic nerve', [
 ('Cortical or juxtacortical region', 'Cortical and juxtacortical lesions already belonged to the spatial framework and together form one region rather than two independent locations.'),
 ('Infratentorial region', 'Brainstem and cerebellar lesions were already represented by the infratentorial region in earlier McDonald criteria; this was not the newly added location.'),
 ('Spinal cord', 'Spinal cord lesions have long contributed to dissemination in space and remain relevant to both relapsing and progressive-onset diagnostic pathways.')],
 [S('Five Anatomical Regions', '**The optic nerve** joins periventricular, cortical/juxtacortical, infratentorial and spinal cord regions in the 2024 revisions. The revision year and publication year differ: the position paper appeared in 2025.',
    'Evidence of optic-nerve involvement can be established through appropriate optic-nerve MRI, optical coherence tomography or visual evoked potentials under specified technical and exclusion requirements.',
    'An abnormal test caused by glaucoma, retinal disease or another optic neuropathy cannot simply be counted as MS-related optic-nerve involvement.'),
  S('Applying the Framework', '**Dissemination in space** concerns characteristic lesions in distinct CNS locations, not the number of separate lesions within one location.',
    'Two spinal cord lesions do not automatically become two of the five anatomical regions. A special progressive-onset pathway separately recognizes multiple cord lesions in the correct clinical setting.',
    'Dissemination in time, positive CSF and newer MRI biomarkers have pathway-specific roles. The presence of lesions in two regions alone should not be presented as a universal sufficient criterion. In a typical clinical presentation, four or five involved regions have a distinct updated pathway.')], ['MC24'], style='direct', table=(['Region','Example of relevant involvement'],[
 ['Periventricular','Characteristic lesion contacting a lateral ventricle'],['Cortical/juxtacortical','Cortical lesion or lesion directly abutting cortex'],['Infratentorial','Characteristic brainstem or cerebellar lesion'],['Spinal cord','Characteristic inflammatory cord lesion'],['Optic nerve','Qualified MRI, OCT or VEP evidence after excluding alternatives']]))

add('MS diagnosis and classification', 'CSF Biomarkers in the Updated MS Criteria',
 'In an appropriate suspected-MS presentation, which statement about the 2024 McDonald revisions is accurate?',
 'Validated evidence of intrathecal kappa free-light-chain synthesis can serve as an alternative to CSF-restricted oligoclonal bands', [
 ('The serum oligoclonal-band pattern alone establishes positive CSF', 'CSF-restricted bands require comparison with serum; a serum pattern alone cannot demonstrate an intrathecal immune response or satisfy the intended CSF evidence.'),
 ('An elevated total CSF protein can replace oligoclonal bands', 'Total protein elevation is nonspecific and occurs in many inflammatory, infectious and structural disorders; it is not the proposed alternative marker of intrathecal immunoglobulin synthesis.'),
 ('A positive CSF marker independently establishes MS without clinical or imaging context', 'CSF immune markers support a specified diagnostic pathway but are not disease-specific; infections and other inflammatory disorders can also produce intrathecal immunoglobulin synthesis.')],
 [S('Intrathecal Immunoglobulin Synthesis', '**CSF-restricted oligoclonal bands** indicate immunoglobulin production within the CNS when interpreted with paired serum. The 2024 framework also accepts appropriately assessed kappa free-light chains as an alternative marker.',
    'Use a validated laboratory approach reflecting intrathecal synthesis rather than treating an unadjusted serum concentration or an isolated absolute CSF value as interchangeable with a validated index.',
    'The kappa free-light-chain index incorporates CSF and serum measurements and the albumin quotient to account for barrier-related transfer. Assay methods, thresholds and local validation matter.'),
  S('Diagnostic Limits', '**Positive CSF is supportive, not pathognomonic.** Interpret the result alongside a compatible syndrome, characteristic lesions and exclusion of a better explanation.',
    'Marked pleocytosis, very high protein, pronounced hypoglycorrhachia or a clinical infectious syndrome should redirect the differential rather than being dismissed because oligoclonal bands are present.',
    'Absence of oligoclonal bands does not categorically exclude MS, but an atypical presentation with negative CSF deserves careful reassessment. The updated framework offers several evidence combinations; not every pathway requires the same test.')], ['MC24'], style='direct')

add('MS diagnosis and classification', 'Four-Region Disease in a Typical Presentation',
 'A 29-year-old has an objectively documented partial myelitis. MRI shows characteristic lesions in periventricular, cortical/juxtacortical, infratentorial and spinal cord regions. No better explanation is found. Under the 2024 McDonald revisions, which conclusion is best?',
 'The four-region pathway can establish MS without additional evidence of dissemination in time', [
 ('A second clinical attack is necessary before MS can be diagnosed', 'A second attack can establish temporal dissemination, but modern criteria permit diagnosis before it; the updated four-region pathway specifically removes that universal requirement.'),
 ('Positive CSF oligoclonal bands are required despite the four-region pattern', 'Positive CSF supports several diagnostic pathways, especially when fewer regions are involved, but is not mandatory in this specific typical four-region presentation.'),
 ('The optic nerve must be involved before any updated diagnostic pathway applies', 'The optic nerve is an additional eligible region, not an obligatory site. Four characteristic regions can be involved without optic-nerve disease.')],
 [S('Updated Diagnostic Pathway', '**A typical clinical presentation with characteristic lesions in at least four of the five regions** can meet the 2024 MS diagnostic framework without further temporal or CSF requirements, provided a better explanation has been excluded.',
    'This is a substantive change from a simplistic rule that every patient must demonstrate dissemination in both space and time. The diagnostic pathway depends on presentation and the amount and type of evidence.',
    'Count cortical and juxtacortical involvement together as one region. Multiple lesions within the same region do not multiply the anatomical count.'),
  S('Limits of Application', '**A highly characteristic pattern is essential.** The pathway does not validate four vaguely abnormal scan areas in a patient with an unrelated syndrome.',
    'NMOSD, MOGAD, vascular disease, infection and other inflammatory disorders require consideration when the phenotype or MRI raises concern. Positive imaging criteria are never permission to ignore a better diagnosis.',
    'CSF remains useful for atypical features or diagnostic uncertainty even when not formally required by this pathway. A diagnostic rule and a complete clinical evaluation serve related but different purposes.')], ['MC24'])

add('MS diagnosis and classification', 'MRI Dissemination in Time',
 'Which MRI result demonstrates dissemination in time in an appropriate suspected-MS presentation?',
 'A new characteristic T2 lesion on follow-up compared with the baseline scan', [
 ('Two characteristic T2 lesions in different regions on the same noncontrast scan', 'Different locations can establish spatial dissemination, but without enhancement information or interval change they do not independently demonstrate that lesions formed at different times.'),
 ('An unchanged single T2 lesion on two scans six months apart', 'Persistence of the same lesion can confirm a stable abnormality, but stability supplies no evidence of a new inflammatory event or temporal dissemination.'),
 ('Several simultaneously enhancing lesions without nonenhancing lesions or a prior comparison', 'Several enhancing lesions can reflect one inflammatory episode. Simultaneous enhancement alone does not establish that lesions arose in separate periods.')],
 [S('Temporal Evidence', '**A new T2 lesion or a new gadolinium-enhancing lesion on follow-up MRI** can demonstrate dissemination in time when compared with an appropriate reference scan.',
    'Simultaneous characteristic enhancing and nonenhancing lesions on a single scan can also support temporal dissemination, reflecting lesions of different inflammatory ages.',
    'A subsequent clinical attack can supply temporal evidence. A fixed arbitrary waiting interval is not required merely to allow the calendar to advance; the relevant feature is convincing new disease activity.'),
  S('Technical Interpretation', '**Comparable acquisition and careful lesion review** help prevent a lesion previously missed because of slice thickness, field strength or positioning from being called genuinely new.',
    'Enhancement is a transient marker of blood-brain barrier disruption, not a permanent property of every MS plaque. Absence of enhancement does not establish absence of MS.',
    'The 2024 framework does not require dissemination in time in every diagnostic pathway. Positive CSF or selected MRI biomarkers may provide alternative evidence under specified conditions; these alternatives do not redefine what temporal dissemination means.')], ['MC24'], style='direct')

add('MS diagnosis and classification', 'The Central Vein Sign in Adults',
 'An adult with a typical demyelinating syndrome has characteristic lesions in two eligible CNS regions. Susceptibility MRI shows a central vein in 7 of 14 assessable white-matter lesions. What is the best interpretation under the 2024 revisions?',
 'The adult select-6 central-vein criterion is met and can support diagnosis through the relevant pathway', [
 ('The criterion fails because more than 90% of lesions must contain a vein', 'An exceptionally high proportion may be convincing, but the adult select-6 approach does not require a universal 90% threshold when six or more qualifying lesions are demonstrated.'),
 ('A central vein in any single lesion is sufficient for the select-6 criterion', 'An isolated vein-positive lesion is insufficiently specific for the named select-6 method; veins can be visible in lesions outside MS as well.'),
 ('The result substitutes for the requirement to exclude a better diagnosis', 'The central vein sign increases specificity in a defined diagnostic framework, but it cannot override a better vascular, inflammatory or infectious explanation for the presentation.')],
 [S('Susceptibility-Based Biomarker', '**The central vein sign** identifies the perivenular organization of many MS lesions using appropriately acquired susceptibility-sensitive MRI sequences.',
    'For an adult with at least ten assessable white-matter lesions, six or more qualifying vein-positive lesions meet the select-6 approach. Seven of fourteen therefore satisfies the relevant numeric requirement in this stem.',
    'In a typical clinical presentation with dissemination in space, a positive select-6 assessment can provide sufficient additional evidence under the 2024 framework. The sign is useful but is not a compulsory test for every patient.'),
  S('Interpretive Limits', '**Acquisition quality and lesion eligibility** matter. A vein passing beside a lesion is not necessarily the central vein sign, and artifact can degrade assessment.',
    'Pediatric interpretation requires separate caution; the original panel gives age-specific guidance rather than assuming all adult performance estimates transfer unchanged.',
    'The central vein sign may help distinguish MS from migraine-related or vascular white-matter abnormalities, but its value depends on a compatible overall lesion pattern. A negative study does not categorically exclude demyelinating disease.')], ['MC24'])

add('MS diagnosis and classification', 'Paramagnetic Rim Lesions in Single-Region Disease',
 'An adult has a typical demyelinating attack with characteristic lesions confined to one eligible CNS region. Susceptibility imaging identifies a definite paramagnetic rim lesion. Which additional finding supports a single-region diagnostic pathway in the 2024 revisions, assuming alternatives are excluded?',
 'CSF-restricted oligoclonal bands', [
 ('A higher total lesion count within that same region without other evidence', 'More lesions in one location may increase suspicion, but lesion burden alone does not provide the stipulated CSF or temporal evidence for this single-region paramagnetic-rim pathway.'),
 ('A mildly elevated erythrocyte sedimentation rate', 'An inflammatory blood marker may be relevant to systemic differentials, but it neither establishes intrathecal synthesis nor substitutes for the diagnostic evidence required here.'),
 ('A normal visual evoked-potential study', 'A normal VEP may be useful when evaluating optic pathways, but it does not create an additional region or provide positive CSF or temporal evidence.')],
 [S('Chronic Active Lesion Biology', '**A paramagnetic rim lesion** has a susceptibility rim associated with iron-containing inflammatory cells at the edge of a chronic active plaque. It increases diagnostic specificity in an appropriate setting.',
    'For a typical clinical presentation with lesions in only one anatomical region, at least one qualifying rim lesion plus positive CSF or dissemination in time can support the updated diagnostic pathway.',
    'The CSF result in this stem supplies intrathecal immune evidence. It is the combination of findings, rather than a rim lesion alone, that is being tested.'),
  S('Specificity and Availability', '**PRLs and the central vein sign are different biomarkers.** A vein reflects perivenular lesion architecture; a rim reflects chronic peripheral inflammatory activity.',
    'Neither finding is mandatory for every MS diagnosis. Appropriate sequences, expert interpretation and differentiation from mimics or susceptibility artifacts are needed.',
    'A negative rim assessment does not exclude MS, and rim-positive lesions are not a direct indication for a particular drug. Treatment choice still depends on phenotype, disease activity, prognosis, comorbidities and patient priorities.')], ['MC24'])

R.update({
 'PHENO': ('Lublin et al. Defining the clinical course of MS: the 2013 revisions, published 2014', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC4117366/'),
 'NICE': ('NICE NG220: Multiple sclerosis in adults, relapse recognition and treatment', 'https://www.nice.org.uk/guidance/ng220/chapter/Recommendations'),
 'RELAPSE': ('Expert recommendations for diagnosis and treatment of MS relapses, 2022', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC8780774/'),
 'OCR': ('Ocrevus intravenous prescribing information, revised May 2026', 'https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/761053s038lbl.pdf'),
})

add('MS diagnosis and classification', 'Progressive-Onset MS: The Unified Framework',
 'A 46-year-old has 18 months of objectively documented progressive spastic paraparesis without attacks. MRI shows two characteristic, noncompressive spinal cord lesions; CSF has restricted oligoclonal bands. After exclusion of structural, metabolic, infectious and alternative inflammatory causes, which interpretation best fits the 2024 framework?',
 'The progressive-onset pathway can be met by the prolonged progression, two characteristic cord lesions and positive CSF', [
 ('A superimposed clinical relapse must occur before progressive MS can be diagnosed', 'A relapse would establish inflammatory activity but is not necessary for a primary progressive presentation; progression from onset is the defining clinical trajectory.'),
 ('The two spinal cord lesions count as four separate anatomical regions', 'The cord is ordinarily one anatomical region. The updated progressive-onset pathway has a specific allowance for two cord lesions, not a general multiplication of region counts.'),
 ('Positive CSF establishes progressive MS even if MRI instead shows compressive myelopathy', 'Intrathecal immunoglobulin synthesis is not disease-specific; a demonstrably compressive explanation must be addressed rather than overridden by positive oligoclonal bands.')],
 [S('Progression from Onset', '**At least twelve months of clinical progression** is required in the progressive-onset framework. Objective serial assessment and a credible history help distinguish sustained progression from incomplete recovery after an attack.',
    'The 2024 revisions use a unified diagnostic framework for relapsing and progressive presentations. In progressive-onset disease, two or more characteristic cord lesions can provide the relevant dissemination-in-space evidence.',
    'Positive CSF supplies an additional supporting element in the case described. Two cord lesions alone should not be taught as universally sufficient for a progressive diagnosis.'),
  S('Excluding Progressive Myelopathy Mimics', '**Cervical or thoracic compression, dural arteriovenous fistula, B12 or copper deficiency and infections** may produce a progressive cord syndrome. MRI morphology and targeted laboratory evaluation remain crucial.',
    'A longitudinally extensive central cord lesion, prominent cord swelling, severe pain, systemic disease or an atypical CSF profile should broaden the differential.',
    'Do not simply transplant older primary-progressive criteria into an unqualified question about current criteria. The version and population must be stated, particularly when discussing the updated allowance for multiple cord lesions.')], ['MC24'])

add('MS diagnosis and classification', 'Specificity in Older Patients with Vascular Risk',
 'A 63-year-old with diabetes and hypertension has an uncertain sensory history and several white-matter lesions. Which approach best reflects the additional specificity advice in the 2024 McDonald revisions?',
 'Seek supporting evidence such as characteristic cord lesions, positive CSF or a qualifying central vein sign before attributing the findings to MS', [
 ('Diagnose MS from the number of deep-white-matter lesions alone', 'Lesion count is useful only after morphology and location are appropriately classified; vascular lesions can be numerous without representing inflammatory demyelination.'),
 ('Exclude MS on age alone and perform no further evaluation', 'Older onset is less common and increases the risk of mimics, but age does not categorically exclude MS when characteristic clinical and paraclinical evidence is present.'),
 ('Use a nonspecific elevation of serum inflammatory markers to establish MS', 'Blood inflammatory markers can guide systemic differential diagnoses, but do not establish CNS demyelination or provide the specific supporting evidence suggested here.')],
 [S('Why Additional Evidence Matters', '**Age of 50 years or older and vascular comorbidity** increase the chance that MRI abnormalities have a non-MS explanation. The updated panel strongly recommends additional diagnostic specificity in these settings.',
    'Examples include characteristic spinal cord lesions, evidence of intrathecal immune activity and an appropriately assessed central vein sign. The choice of tests depends on the presentation and available expertise.',
    'Atypical symptoms and nonspecific scans require reassessment even when one ancillary test is positive; test interpretation depends on the prior clinical probability.'),
  S('Pattern-Based Differential Diagnosis', '**Small-vessel disease** commonly produces deep white-matter abnormalities, lacunes and microbleeds. Characteristic callosal, juxtacortical or short-segment cord involvement may favour demyelination but still requires integrated interpretation.',
    'Ask whether symptoms localize to a CNS lesion and represent an inflammatory attack or progression, rather than assuming that any sensory complaint is a demyelinating event.',
    'Avoid using an empiric steroid response as a diagnostic shortcut. Several alternative inflammatory disorders respond to steroids, and fluctuating symptoms can improve for unrelated reasons.')], ['MC24'])

add('MS diagnosis and classification', 'Incidental Demyelinating-Pattern MRI Findings',
 'A 32-year-old without a prior demyelinating attack has incidentally detected, convincingly MS-typical lesions in periventricular and infratentorial regions. CSF shows restricted oligoclonal bands, and a careful evaluation excludes better explanations. What is the best statement about the 2024 revisions?',
 'This combination can meet an updated MS diagnostic pathway despite the absence of a prior clinical attack', [
 ('The absence of symptoms prohibits an MS diagnosis under every updated pathway', 'That reflects an overly restrictive interpretation of earlier clinical frameworks; the updated criteria include selected radiologically isolated presentations with additional qualifying evidence.'),
 ('Any incidental white-matter lesion is sufficient regardless of its morphology or CSF', 'Incidental lesions are common and often nonspecific. The updated pathway requires a characteristic distribution and additional evidence, with alternative causes excluded.'),
 ('The diagnosis necessarily mandates the same drug for every asymptomatic individual', 'Diagnostic classification and treatment selection are separate decisions. Benefits, risks, disease burden, prognostic markers and patient preferences affect whether and how therapy is offered.')],
 [S('From RIS to a Biological Diagnostic Framework', '**Selected radiologically isolated presentations** can fulfill the 2024 MS framework. In the described case, typical lesions in at least two anatomical locations and positive CSF provide the relevant evidence combination.',
    'Dissemination in time or a qualifying central vein sign can provide alternative additional evidence in specified pathways. A nonspecific incidental MRI does not become diagnostic merely because the patient is young.',
    'Confirm that imaging genuinely resembles inflammatory demyelination and that the history does not reveal an overlooked clinical event.'),
  S('Counselling and Surveillance', '**Risk assessment remains individualized.** Cord lesions, inflammatory MRI activity, intrathecal immune markers and longitudinal change inform discussion of future clinical disease.',
    'Discuss diagnostic uncertainty, surveillance and the evidence for treatment rather than equating a revised label with an automatic uniform prescription.',
    'An asymptomatic person with typical lesions may warrant specialist review and a planned clinical/MRI follow-up strategy. New symptoms require prompt evaluation, while vascular or migraine-associated lesions should be managed according to their actual cause.')], ['MC24'])

add('MS diagnosis and classification', 'Activity and Progression Are Separate Descriptors',
 'A patient with established secondary progressive MS has no relapses or new MRI lesions during the last year but shows sustained worsening of walking independent of attacks. Which descriptor best summarizes that interval?',
 'Not active, with progression', [
 ('Active, without progression', 'A new relapse or new inflammatory MRI lesion would support activity without progression if sustained disability did not worsen; neither condition describes this interval.'),
 ('Active, with progression', 'This descriptor requires evidence of both inflammatory activity and disability progression in the stated period; progressive walking decline alone does not supply MRI or relapse activity.'),
 ('Not active, without progression', 'This describes an interval without new inflammatory events and without sustained worsening; the objectively worsening walking performance excludes the second component here.')],
 [S('Two Clinical Axes', '**Activity** is assessed through clinical relapses and MRI evidence such as gadolinium-enhancing or new/enlarging T2 lesions. **Progression** describes sustained worsening of disability over time in a progressive course.',
    'Specify the assessment interval. A patient can be not active during one year and active during another; these are longitudinal descriptors rather than permanent labels.',
    'The patient has documented worsening without an observed inflammatory event, making not active with progression the appropriate descriptor for the stated year.'),
  S('Clinical Interpretation', '**Absence of new conventional MRI lesions does not prove biological inactivity in every compartment.** Clinical progression can continue despite apparent suppression of focal inflammatory activity.',
    'Before attributing slower walking to progression, assess infection, pain, spasticity, deconditioning, medication effects and orthopedic disease. Serial objective functional measures improve reliability.',
    'These descriptors help frame prognosis and treatment discussions but do not alone identify one optimal therapy. Age, disease duration, prior activity, safety and evidence in the relevant population remain important.')], ['PHENO'], style='clinical_scenario', table=(['During a defined interval','New relapse/MRI activity','Sustained progression'],[
 ['Active, with progression','Present','Present'],['Active, without progression','Present','Absent'],['Not active, with progression','Absent','Present'],['Not active, without progression','Absent','Absent']]))

add('MS relapse treatment', 'Infection-Associated Pseudorelapse',
 'A woman with MS develops worsening of her old leg weakness during a febrile urinary infection. There are no new focal findings, and function returns to baseline after the fever resolves. Which initial strategy is most appropriate?',
 'Treat the infection and reassess neurological function before labeling the episode a new relapse', [
 ('Give high-dose methylprednisolone immediately for every recurrence of old weakness', 'High-dose steroids are appropriate for selected true inflammatory relapses, but can worsen infection and are not the initial response to fever-linked transient recurrence of old symptoms.'),
 ('Escalate disease-modifying therapy solely because weakness increased during fever', 'DMT escalation may follow confirmed breakthrough inflammatory disease; a reversible temperature-related episode alone does not establish treatment failure.'),
 ('Start plasma exchange for presumed steroid-refractory inflammation', 'Plasma exchange is a rescue treatment for severe inflammatory attacks in an appropriate setting, not for symptoms resolving with treatment of an infectious trigger.')],
 [S('Temperature-Sensitive Conduction', '**Pseudorelapse** is worsening of previous neurological deficits from a systemic trigger without a new inflammatory lesion. Fever and heat can impair conduction through previously demyelinated pathways.',
    'Urinary and respiratory infections, heat exposure and other physiological stressors are common precipitants. The temporal link to fever and recovery after its resolution strongly support this interpretation.',
    'A true relapse can coexist with infection. Persisting new objective deficits after treatment require reassessment rather than automatic dismissal as pseudorelapse.'),
  S('Assessment and Treatment', '**Exclude infection and other causes** before diagnosing relapse. Review the duration, pattern, examination findings, medications and metabolic status; obtain targeted tests when indicated.',
    'A relapse generally involves new or worsened neurological symptoms lasting more than 24 hours without fever or infection after a period of stability, with the complete context guiding diagnosis.',
    'Treat the trigger and support mobility, hydration and bladder care. Steroids can accelerate recovery from an inflammatory relapse but do not treat a urinary infection or establish that the symptoms represent new MS activity.')], ['NICE','RELAPSE'])

add('MS relapse treatment', 'High-Dose Methylprednisolone for a Disabling Relapse',
 'After infection is excluded, an adult with MS has a functionally disabling relapse suitable for outpatient oral treatment. Which regimen matches NICE NG220?',
 'Oral methylprednisolone 500 mg daily for five days', [
 ('Oral prednisolone 10 mg daily for five days', 'A low oral steroid dose may be used for other inflammatory conditions, but does not provide the high-dose regimen recommended for treating an MS relapse.'),
 ('Intravenous methylprednisolone 1 g once, followed by no further doses', 'A 1-g dose forms part of a recognized IV pulse course, generally for three to five days; a single isolated dose is not the regimen requested here.'),
 ('Oral methylprednisolone 16 mg daily for four weeks', 'A prolonged low-dose course is not equivalent to an evidence-based high-dose pulse and exposes the patient to sustained steroid toxicity without matching the recommended relapse regimen.')],
 [S('Regimen and Route', '**NICE recommends oral methylprednisolone 0.5 g daily for five days** for an MS relapse selected for treatment. The dose is intentionally much higher than routine low-dose steroid prescriptions.',
    'An alternative is ==IV methylprednisolone 1 g daily for three to five days== when oral treatment has failed or is not tolerated, or when severe disease or monitoring needs warrant admission.',
    'Not every mild sensory relapse needs steroids. Consider functional impact, expected recovery, patient preference and comorbidity before prescribing.'),
  S('Benefits and Monitoring', '**Steroids accelerate recovery** but do not replace long-term disease-modifying treatment or reliably prevent subsequent disability from the episode.',
    'Discuss insomnia, mood change, dyspepsia, hyperglycemia and infection risk. Diabetes, severe psychiatric history and other comorbidities may alter the monitoring setting.',
    'A routine prolonged oral taper is generally unnecessary after a short high-dose course for a typical MS relapse. Reevaluate persistent severe deficits for rescue therapy and reconsider mimics if the course is atypical.')], ['NICE','RELAPSE'], style='direct')

add('MS relapse treatment', 'Rescue Therapy for a Severe Steroid-Refractory Attack',
 'A patient with an established inflammatory demyelinating disorder remains unable to stand after a severe acute myelitis despite IV methylprednisolone 1 g daily for five days. Infection and compression have been excluded. Which rescue treatment has the best-established role?',
 'Therapeutic plasma exchange', [
 ('Begin glatiramer acetate as the sole acute rescue treatment', 'Glatiramer acetate is a preventive MS therapy; its onset and mechanism do not provide rapid rescue of a severe steroid-refractory cord attack.'),
 ('Use dalfampridine as the sole treatment for the inflammatory lesion', 'Dalfampridine can improve walking performance in selected patients but is symptomatic therapy; it does not remove the acute inflammatory process causing severe myelitis.'),
 ('Continue a low-dose oral steroid course for several months before considering rescue', 'An extended low-dose course may have roles in selected other inflammatory diseases, but delaying effective rescue after a severe steroid-refractory attack risks persistent disability.')],
 [S('Apheresis as Acute Rescue', '**Plasma exchange** is an established second-line option for severe acute CNS inflammatory demyelinating attacks that respond inadequately to high-dose corticosteroids.',
    'A common course is five to seven exchanges, often on alternate days, with exact volume and scheduling determined by the apheresis service and clinical response. Earlier rescue is generally preferable to prolonged delay in a devastating attack.',
    'The evidence and rationale concern acute inflammatory attacks. Plasma exchange is not a routine treatment for chronic noninflammatory progressive MS disability.'),
  S('Monitoring and Reassessment', '**Vascular access, blood pressure, electrolytes and coagulation** require monitoring. Citrate-associated hypocalcemia, infection, bleeding and hemodynamic complications must be anticipated.',
    'The attack phenotype should also prompt appropriate AQP4-IgG and MOG-IgG evaluation when not already established; these diagnoses affect long-term prevention and the urgency of attack rescue.',
    'After stabilization, review the preventive regimen separately. A long-term DMT may reduce future attacks, but starting it is not equivalent to rescuing the current severe neurological deficit.')], ['RELAPSE'])

R.update({
 'MENACT': ('MENACTRIMS consensus recommendations, 2023 revision, published 2024', 'https://menactrims.org/wp-content/uploads/2024/11/Menactrims-2023-guidelines.pdf'),
 'ORATORIO': ('ORATORIO randomized trial: Ocrelizumab versus placebo in primary progressive MS, 2017', 'https://www.nejm.org/doi/10.1056/NEJMoa1606468'),
 'NAT': ('Tysabri current US prescribing information', 'https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=c5fdde91-1989-4dd2-9129-4f3323ea2962'),
 'NATEMA': ('EMA recommendations to minimize natalizumab PML risk', 'https://www.ema.europa.eu/mt/news/ema-confirms-recommendations-minimise-risk-brain-infection-pml-tysabri'),
 'FING': ('Gilenya prescribing information, updated 2025', 'https://www.dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=cc9e1c8c-0e2b-44e2-878b-27057f786be9'),
 'TERI': ('Aubagio prescribing information, 2026', 'https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/202992s018lbl.pdf'),
 'DMF': ('Tecfidera prescribing information, updated June 2025', 'https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=665d7e74-036c-5f68-5b67-ab84b9b49151'),
 'CLAD': ('Mavenclad prescribing information, May 2026', 'https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/022561s013lbl.pdf'),
})

add('MS disease-modifying therapy', 'Escalation for Highly Active Relapsing MS',
 'Despite good adherence to interferon beta, a 30-year-old has two disabling relapses and several new enhancing lesions over twelve months. Which treatment strategy is most appropriate to discuss?',
 'Switch to a suitable high-efficacy DMT after individualized safety and reproductive assessment', [
 ('Continue the same regimen solely because adherence is good', 'Good adherence excludes one common reason for apparent failure, but it does not negate recurrent objective inflammatory activity that supports treatment reassessment.'),
 ('Use intermittent high-dose steroids as the sole long-term preventive strategy', 'Steroids can speed recovery from individual attacks but are not a substitute for an effective disease-modifying strategy against recurrent inflammatory disease.'),
 ('Replace all preventive treatment with rehabilitation alone', 'Rehabilitation addresses disability and remains valuable alongside medication, but does not provide comparable control of ongoing focal inflammatory MS activity.')],
 [S('Breakthrough Disease', '**Repeated disabling relapses with new enhancing lesions despite an adequate adherent trial** indicate substantial breakthrough inflammatory disease. A higher-efficacy strategy should be considered rather than accepting repeated preventable injury.',
    'Suitable options may include an anti-CD20 agent, natalizumab or selected immune-reconstitution therapies, depending on prior treatment, JCV status, comorbidities, infection risk, reproductive plans and local access.',
    'No single high-efficacy agent is uniformly best. Discuss expected benefit, monitoring burden, serious adverse effects and patient preferences.'),
  S('Safe Transition', '**Confirm the diagnosis and the treatment exposure** before calling the regimen ineffective. Check adherence, duration sufficient for effect and whether events are true relapses rather than pseudorelapses.',
    'Obtain drug-specific screening, update appropriate vaccinations and plan the transition to avoid both excessive overlapping immunosuppression and unnecessary untreated intervals.',
    'Relapse rescue and rehabilitation remain separate immediate needs. Long-term response is assessed through clinical activity, MRI activity, disability trajectory and safety rather than symptoms alone.')], ['MENACT'])

add('MS disease-modifying therapy', 'Ocrelizumab in Primary Progressive MS',
 'Which agent demonstrated reduced confirmed disability progression versus placebo in the ORATORIO trial of primary progressive MS?',
 'Ocrelizumab', [
 ('Natalizumab', 'Natalizumab is a high-efficacy therapy for relapsing MS, but the placebo-controlled PPMS result named in the stem was established with ocrelizumab.'),
 ('Glatiramer acetate', 'Glatiramer acetate is used for relapsing disease; it is not the agent that produced the positive ORATORIO confirmed-disability-progression result in PPMS.'),
 ('Dimethyl fumarate', 'Dimethyl fumarate is an oral relapsing-MS therapy and requires lymphocyte monitoring; it does not supply the PPMS trial evidence requested here.')],
 [S('Trial Evidence', '**ORATORIO** randomized patients with PPMS to ocrelizumab or placebo. Twelve-week confirmed disability progression occurred in ==32.9% versus 39.3%==, with hazard ratio ==0.76==.',
    'The benefit represents slowing of progression, not reversal or a cure. The trial predominantly informs a selected population, including adults aged 18–55 years with EDSS 3.0–6.5 and specified disease-duration limits.',
    'Extrapolation to substantially older patients with advanced, longstanding noninflammatory disability requires particular caution. Local eligibility and reimbursement rules can be narrower than a general regulatory indication.'),
  S('Treatment and Safety', '**Ocrelizumab is a CD20-directed B-cell-depleting antibody.** The adult IV course starts with 300 mg, followed by another 300 mg two weeks later; subsequent doses are 600 mg every six months.',
    'Before treatment, assess HBV status, immunoglobulins, liver tests, active infection and vaccination needs. Premedication and infusion monitoring reduce and detect infusion reactions.',
    'Monitor infection burden and immunoglobulin decline over time. A separate subcutaneous formulation has its own dose and administration instructions; its milligram dose must not be substituted into the IV regimen.')], ['ORATORIO','OCR'], style='direct')

add('MS disease-modifying therapy', 'Resolved Hepatitis B Before Anti-CD20 Therapy',
 'Before ocrelizumab, a patient is HBsAg negative, anti-HBc positive and anti-HBs positive, with undetectable HBV DNA. Which next step is best?',
 'Obtain hepatology/infectious-disease input and plan HBV-reactivation prevention before B-cell depletion', [
 ('Treat the negative HBsAg as proof that reactivation is impossible', 'Resolved HBV can reactivate during anti-CD20 therapy because immune control is impaired; HBsAg negativity does not eliminate that biologic risk.'),
 ('Give an HBV vaccine booster as the only reactivation-prevention measure', 'Vaccination prevents acquisition in susceptible individuals but does not eradicate persistent intrahepatic HBV or replace reactivation prevention in an anti-HBc-positive patient.'),
 ('Exclude ocrelizumab permanently in every anti-HBc-positive patient', 'Active HBV infection is a contraindication, while resolved infection can often be managed with expert-guided prophylaxis and monitoring rather than a universal permanent prohibition.')],
 [S('Reactivation Risk', '**Anti-HBc positivity** identifies previous or current exposure. A patient with resolved infection may retain replication-competent HBV despite negative HBsAg and undetectable circulating DNA.',
    'Anti-CD20 therapy is a high-risk setting for reactivation. Arrange specialist-guided antiviral prophylaxis, commonly with a high-barrier agent such as entecavir or tenofovir, and an appropriate monitoring/duration plan.',
    'Check HBsAg, anti-HBc and anti-HBs rather than relying on a single screening result. Active infection requires evaluation and treatment before an ocrelizumab decision.'),
  S('Other Pretreatment Measures', '**Quantitative immunoglobulins, liver tests and infection review** are part of ocrelizumab preparation. Delay infusion during an active infection and consider the consequences of recurrent serious infections or sustained hypogammaglobulinemia.',
    'The US IV label advises live vaccines at least four weeks before initiation and nonlive vaccines, when possible, at least two weeks before. Avoid live vaccines during treatment and until B-cell repletion.',
    'Vaccine responses may be attenuated after B-cell depletion. Preventive planning should therefore precede therapy when clinical urgency allows.')], ['OCR','MENACT'])

add('MS disease-modifying therapy', 'Natalizumab-Associated PML Risk',
 'Which natalizumab-treated patient has the greatest established PML risk among the following profiles?',
 'Anti-JCV-antibody positive after more than two years of treatment, with prior immunosuppressant exposure', [
 ('Anti-JCV-antibody negative after six months, without prior immunosuppression', 'This is a substantially lower-risk profile, although false-negative testing and later seroconversion mean that risk is not literally zero.'),
 ('Anti-JCV-antibody positive after six months, without prior immunosuppression', 'JCV positivity increases concern, but shorter exposure and no prior immunosuppression generally carry lower risk than the combined high-risk profile.'),
 ('Anti-JCV-antibody negative after three years, without prior immunosuppression', 'Longer exposure is relevant, but current antibody negativity without prior immunosuppression is lower risk than the combination of JCV positivity, long exposure and prior immunosuppression.')],
 [S('Risk Stratification', '**Anti-JCV antibody positivity, longer exposure—especially beyond two years—and prior immunosuppressant use** are the established major risk factors for natalizumab-associated progressive multifocal leukoencephalopathy.',
    'In antibody-positive patients without prior immunosuppressant exposure, the antibody index further informs risk; an index above 1.5 after more than two years is a particularly concerning category.',
    'The index is not a test for active PML and does not replace clinical or MRI assessment. Antibody-negative patients require reassessment because seroconversion occurs.'),
  S('Monitoring and Management', '**New subacute cognitive, language, visual or motor deficits** require prompt evaluation for PML rather than automatic steroid treatment for presumed MS relapse.',
    'Withhold natalizumab when PML is suspected and obtain appropriate brain MRI and CSF JCV PCR. Early negative PCR may require repeat sensitive testing when suspicion remains high.',
    'Natalizumab blocks alpha-4-integrin-mediated leukocyte trafficking; the usual IV regimen is 300 mg every four weeks. Extended-interval approaches can reduce risk in selected settings but do not abolish it, and a transition plan must account for recurrent MS activity.')], ['NAT','NATEMA'])

add('MS disease-modifying therapy', 'Disease Reactivation After Fingolimod Withdrawal',
 'A patient planning a change from fingolimod asks whether treatment can simply be stopped for several months before the next DMT. Which counselling point is most appropriate?',
 'Plan a monitored transition because severe disease reactivation can follow fingolimod discontinuation', [
 ('A prolonged untreated interval is needed for every patient regardless of disease activity', 'Some transitions need safety-related spacing, but a universal long untreated period disregards the recognized risk of severe disease reactivation after fingolimod withdrawal.'),
 ('Rebound can be excluded if the lymphocyte count remains low', 'Persistent peripheral lymphopenia does not reliably exclude inflammatory reactivation; circulating cell counts alone cannot guarantee protection during the transition.'),
 ('Stopping fingolimod requires no follow-up if the last MRI was stable', 'A stable pretreatment or on-treatment scan does not eliminate withdrawal-related risk. New symptoms and interval imaging may be needed during a planned switch.')],
 [S('Withdrawal-Related Disease Activity', '**Severe worsening after stopping fingolimod** is a recognized safety concern. Reported events usually occur within twelve weeks, although later events up to twenty-four weeks have been described.',
    'Fingolimod functionally modulates S1P receptors and retains lymphocytes in lymphoid tissue. Its immunologic effects and the risks of the next drug both influence transition timing.',
    'Discuss the reason for stopping, current activity, pregnancy plans, infection risk and the proposed next therapy. No one washout duration is optimal for every clinical situation.'),
  S('Practical Transition', '**Avoid an unnecessary untreated gap**, while considering additive immunosuppression, unresolved infection and drug-specific requirements.',
    'Arrange a clinical plan for new neurological symptoms and consider an MRI reference around the switch. Severe deterioration requires prompt examination and differentiation of relapse, infection and other causes.',
    'Restarting after a sufficiently long interruption may require repeat first-dose cardiac monitoring according to the label. A supervised transition is therefore more than simply writing a new prescription.')], ['FING','MENACT'])

add('MS disease-modifying therapy', 'Fingolimod Initiation and Monitoring',
 'Which initiation plan is appropriate for an otherwise eligible adult starting fingolimod?',
 'Baseline ECG and eye assessment, with at least six hours of first-dose pulse and blood-pressure monitoring', [
 ('Observe only for an immediate injection-site reaction', 'Injection reactions matter for injectable agents, whereas fingolimod is oral and its early safety concern includes bradycardia and atrioventricular conduction effects.'),
 ('Monitor only liver enzymes and omit cardiac assessment', 'Liver testing is important, but does not address the potentially significant first-dose reduction in heart rate or conduction abnormalities.'),
 ('Use JCV antibody index as the sole pre-treatment safety assessment', 'JCV index is central to natalizumab risk stratification, but it does not replace cardiac, ophthalmic, infectious or laboratory assessment before fingolimod.')],
 [S('Cardiac Effects', '**Fingolimod can cause first-dose bradycardia and AV block.** Obtain an ECG before dosing and at the end of observation, with hourly pulse and blood-pressure measurement for at least six hours.',
    'Observation must be extended when specified abnormalities occur, including a low rate at six hours, a nadir at the observation endpoint or new significant AV block. Selected higher-risk patients require overnight monitoring.',
    'Review recent cardiovascular events, significant conduction disease, QT prolongation and interacting rate-slowing drugs. Some findings are contraindications rather than indications merely to observe longer.'),
  S('Ophthalmic and Other Safety', '**Macular edema** requires baseline fundus/macular evaluation and reassessment around three to four months, as well as evaluation for visual symptoms. Diabetes and uveitis increase risk.',
    'Check CBC, liver tests, VZV immunity and infection history; vaccinate susceptible patients before treatment using the label-specified interval. Monitor for skin malignancy and other recognized complications.',
    'The usual adult dose is 0.5 mg orally daily. Other S1P modulators have distinct titration and initiation requirements; fingolimod rules should not be generalized to every agent.')], ['FING'], style='direct')

add('MS disease-modifying therapy', 'Accelerated Teriflunomide Elimination',
 'A woman taking teriflunomide plans pregnancy. Which regimen is an established accelerated elimination procedure?',
 'Cholestyramine 8 g every eight hours for eleven days', [
 ('Activated charcoal 50 g once as a single dose', 'Activated charcoal is an accepted elimination agent, but the labeled regimen is repeated 50-g doses every twelve hours for eleven days, not a single dose.'),
 ('Stop the drug for one week and assume clearance is complete', 'Teriflunomide persists through enterohepatic recycling; without accelerated elimination, reaching the target concentration commonly takes months and can take up to two years.'),
 ('Use a proton-pump inhibitor daily for eleven days', 'A proton-pump inhibitor treats acid-related disease but does not provide the binding/elimination effect of cholestyramine or activated charcoal for teriflunomide.')],
 [S('Prolonged Persistence', '**Teriflunomide inhibits dihydroorotate dehydrogenase**, reducing de novo pyrimidine synthesis in activated lymphocytes. Its long persistence and embryo-fetal risk make reproductive planning essential.',
    'The labeled accelerated procedure is ==cholestyramine 8 g every eight hours for eleven days==; 4 g three times daily may be used if 8 g is poorly tolerated. An alternative is ==activated charcoal 50 g every twelve hours for eleven days==.',
    'The target plasma concentration is ==below 0.02 mg/L==. Confirm adequate elimination using the applicable label and laboratory protocol before attempting conception.'),
  S('Counselling and Monitoring', '**Effective contraception** is required until the relevant elimination criteria are met. If pregnancy occurs, stop the drug and arrange prompt specialist assessment and accelerated elimination.',
    'Without accelerated elimination, the average time to reach the low target level is about eight months and may extend to two years. A short calendar washout is therefore unreliable.',
    'Hepatotoxicity, hypertension, neuropathy and cytopenias are other important safety issues. Elimination may permit disease activity to return, so coordinate an alternative MS management plan rather than leaving prevention unaddressed.')], ['TERI'], style='direct')

add('MS disease-modifying therapy', 'Persistent Lymphopenia with Dimethyl Fumarate',
 'A patient on dimethyl fumarate has an absolute lymphocyte count of 0.4 × 10^9/L on repeated tests over seven months. There are no neurological symptoms. What is the best response under US prescribing guidance?',
 'Consider interrupting treatment and follow lymphocyte recovery while planning alternative disease control', [
 ('Continue unchanged because only neutrophil counts affect opportunistic infection risk', 'Lymphocyte depletion is directly relevant to dimethyl-fumarate-associated opportunistic infection and PML risk; a normal neutrophil count does not remove that concern.'),
 ('Diagnose PML from the lymphocyte count alone and begin PML treatment', 'Lymphopenia is a risk marker, not proof of active PML. New compatible neurological findings require targeted MRI and virological assessment.'),
 ('Increase the dose to overcome a presumed inadequate immune effect', 'Persistent severe lymphopenia is a safety signal, not evidence of underdosing; increasing exposure would not address the clinical problem.')],
 [S('Threshold and Action', '**Persistent severe lymphopenia** requires active review. US labeling advises considering interruption if lymphocytes remain ==below 0.5 × 10^9/L for more than six months==.',
    'Obtain a CBC including lymphocytes before treatment, at six months and every six to twelve months thereafter under the US label, or more frequently according to clinical risk and local recommendations.',
    'Continue monitoring after discontinuation until recovery. Recovery may be delayed after prolonged severe lymphopenia, which affects the timing and safety of a subsequent immunotherapy.'),
  S('Drug Effects and Infection Risk', '**Dimethyl fumarate** has immunomodulatory and antioxidant-pathway effects, including Nrf2 activation; its full therapeutic mechanism is not completely defined. Flushing and gastrointestinal symptoms are common tolerability problems.',
    'The usual initiation is 120 mg twice daily for seven days, then 240 mg twice daily. Liver injury, herpes zoster and other opportunistic infections are important additional concerns.',
    'PML can present with progressive cognitive, visual or focal motor deficits. Withhold treatment and investigate promptly if such symptoms arise; do not assume every new deficit in a treated patient is an MS relapse.')], ['DMF'])

add('MS disease-modifying therapy', 'Cladribine Reproductive Precautions: A Versioned Label Question',
 'Under the May 2026 US Mavenclad label, which contraception advice applies after the last dose in each annual treatment course?',
 'Six months for females and fourteen weeks for males of reproductive potential', [
 ('Fourteen weeks for females and six months for males', 'These intervals reverse the sex-specific recommendations in the May 2026 US label; the longer six-month requirement applies to females.'),
 ('Contraception is needed only during the days tablets are taken', 'The genotoxic and embryo-fetal risk extends beyond the short tablet-dosing windows, so contraception must continue for the specified post-course interval.'),
 ('One week after either sex completes the course', 'A one-week interval is substantially shorter than the current labeled reproductive precautions and does not provide the requested risk mitigation.')],
 [S('Sex-Specific Current US Label', '**The May 2026 US label specifies six months for females and fourteen weeks for males** after the last dose in each treatment course. Explicitly identify the label version because older sources may list six months for both.',
    'Exclude pregnancy before each annual course. Cladribine is contraindicated during pregnancy, and effective contraception is required during dosing as well as for the relevant period afterward.',
    'Use the current jurisdiction-specific label for contraceptive counselling. The May 2026 US label reports no clinically significant pharmacokinetic interaction with a studied combined oral contraceptive; older added-barrier wording should not be presented as a current universal US requirement.'),
  S('Immune-Reconstitution Treatment', '**Cladribine is a purine nucleoside analogue** producing prolonged lymphocyte depletion. The approved cumulative oral course is 3.5 mg/kg over two years, divided into two yearly treatment courses with short dosing cycles.',
    'Screen for HIV, active tuberculosis, hepatitis and other relevant infection; assess malignancy and lymphocyte counts before treatment. Complete indicated live vaccines at least four to six weeks before dosing and avoid them while immune suppression persists.',
    'Herpes zoster risk rises with lymphopenia; antiviral prophylaxis is recommended when lymphocytes are below 200/µL. Current US guidance also recommends recombinant zoster vaccination for VZV-seropositive patients before or during treatment.')], ['CLAD'], style='direct')

add('MS disease-modifying therapy', 'Interferon Beta and Glatiramer Acetate',
 'A patient with relapsing MS has troublesome flu-like symptoms and transaminase elevations on an injectable DMT. Which drug is most consistent with this adverse-effect pattern?',
 'Interferon beta', [
 ('Glatiramer acetate', 'Glatiramer commonly causes injection-site reactions and can cause transient post-injection flushing, chest tightness or dyspnea; the flu-like and liver-test pattern is more characteristic of interferon beta.'),
 ('Natalizumab', 'Natalizumab can cause infusion reactions and liver injury, but is distinguished by alpha-4-integrin blockade and PML risk rather than the classic interferon-associated flu-like syndrome.'),
 ('Ocrelizumab', 'Ocrelizumab is a B-cell-depleting antibody with infusion reactions and infection-related monitoring; the stereotyped chronic injectable flu-like syndrome points more strongly to interferon beta.')],
 [S('Comparative Mechanisms and Tolerability', '**Interferon beta** alters immune signalling and leukocyte trafficking. Flu-like symptoms, injection reactions, cytopenias and liver-enzyme abnormalities are important adverse effects; monitor CBC and liver tests.',
    'Dose titration, timing and an antipyretic may improve flu-like symptoms in suitable patients. Persistent significant liver abnormalities require clinical evaluation rather than simply masking symptoms.',
    'Preparations have different doses and schedules. The drug family should not be treated as a single interchangeable syringe prescription.'),
  S('Glatiramer Acetate and Shared Decisions', '**Glatiramer acetate** is a synthetic polypeptide mixture with immunomodulatory effects. Common adult regimens are 20 mg subcutaneously daily or 40 mg subcutaneously three times weekly at least 48 hours apart.',
    'Injection-site reactions and lipoatrophy can occur. A transient immediate post-injection syndrome is recognized, but suspected anaphylaxis requires emergency care and must not be dismissed as a benign expected reaction.',
    'These agents have long safety experience and may suit selected patients, including some reproductive planning contexts. Their generally lower efficacy compared with several modern agents matters when disease is highly active; treatment must balance efficacy, safety and preferences.')], ['MENACT'])

# Individual editorial refinements after source checks.
R['HBV'] = ('AASLD hepatitis B guidance: prophylaxis during anti-CD20 therapy', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5975958/')
R['GLAT'] = ('FDA boxed warning for glatiramer-associated anaphylaxis, January 2025', 'https://www.fda.gov/drugs/drug-safety-communications/fda-adds-boxed-warning-about-rare-serious-allergic-reaction-called-anaphylaxis-multiple-sclerosis')
rows[17]['refs'].append('HBV')
rows[24]['refs'].append('GLAT')
rows[15]['others'] = [
 ('Switch to another platform injectable as the default response to this level of activity', 'A lateral switch between platform therapies can suit intolerance or a less active course, but repeated disabling attacks and enhancing lesions favour consideration of higher efficacy.'),
 ('Continue the present DMT with surveillance because the attacks recovered fully', 'Continued surveillance can suit an isolated uncertain event, but recovery does not negate repeated objective inflammatory injury despite adequate adherent treatment.'),
 ('Treat each attack with a steroid pulse while deferring DMT reassessment', 'Steroid pulses have an acute recovery role; repeated disabling attacks despite prevention require reassessment of disease control rather than rescue treatment alone.')]
rows[14]['others'] = [
 ('Repeat high-dose methylprednisolone alone while deferring apheresis', 'A further pulse may be considered after a partial response in selected cases, but a severe persistently disabling attack after adequate steroids warrants prompt consideration of plasma exchange.'),
 ('Use IV immunoglobulin as the preferred routine rescue for steroid-refractory MS myelitis', 'IVIG has established uses in other immune neurological diseases and selected demyelinating contexts, but plasma exchange has the better-established rescue role for this severe steroid-refractory MS-type attack.'),
 ('Begin cyclophosphamide as the preferred rescue before trying apheresis', 'Cyclophosphamide may be considered in exceptional fulminant refractory disease, but its toxicity and weaker evidence make it less appropriate before established apheresis rescue.')]

R.update({
 'NEMOS2': ('NEMOS revised NMOSD recommendations, Part II: attack therapy and long-term management, 2023', 'https://doi.org/10.1007/s00415-023-11910-z'),
 'MENING': ('CDC clinical guidance: meningococcal risk during complement-inhibitor therapy', 'https://www.cdc.gov/meningococcal/hcp/clinical-guidance/complement-inhibitor.html'),
})

add('Neuromyelitis optica spectrum disorder', 'AQP4-Positive NMOSD: Diagnostic Requirements',
 'A woman has a first episode of severe optic neuritis. Serum AQP4-IgG is convincingly positive by a validated cell-based assay. Appropriate evaluation excludes alternative causes. Which interpretation best follows the international NMOSD criteria?',
 'One compatible core clinical characteristic with AQP4-IgG positivity can establish NMOSD', [
 ('Both optic neuritis and transverse myelitis must already have occurred', 'The historic opticospinal requirement is too restrictive for AQP4-positive disease; a single qualifying core syndrome can establish the current diagnosis when alternatives are excluded.'),
 ('A second clinical attack is required to demonstrate dissemination in time', 'Dissemination in time is not required in AQP4-positive NMOSD; waiting for another attack can delay effective prevention of potentially irreversible disability.'),
 ('Four characteristic MS anatomical regions must be involved', 'The five-region McDonald framework applies to MS and should not be substituted for the distinct antibody-associated NMOSD diagnostic framework.')],
 [S('Antibody-Defined Astrocytopathy', '**AQP4-IgG-positive NMOSD** is primarily an autoimmune astrocytopathy, with secondary inflammatory demyelination and tissue injury. A validated serum cell-based assay is preferred for antibody testing.',
    'At least one of six core clinical characteristics is required: optic neuritis, acute myelitis, area postrema syndrome, another acute brainstem syndrome, a qualifying diencephalic syndrome or a qualifying cerebral syndrome.',
    'The diencephalic and cerebral categories require appropriate NMOSD-typical MRI abnormalities. A positive antibody without a compatible core clinical syndrome should not alone be equated with definite symptomatic NMOSD.'),
  S('Clinical Consequences', '**Exclude a better explanation** and verify unexpected low-level or assay-discordant results. Serum is generally the preferred specimen; indiscriminate use of less specific assays can mislead.',
    'A first attack can leave major disability, and AQP4-positive disease has substantial relapse risk. After acute treatment, discuss long-term attack prevention rather than waiting for a second event merely to satisfy a nonexistent temporal rule.',
    'MS therapies cannot be assumed effective for NMOSD. Treatment targets and safety preparation differ substantially, making etiologic classification clinically important.')], ['NEMOS1','NEMOS2'])

add('Neuromyelitis optica spectrum disorder', 'Seronegative NMOSD Requires More Evidence',
 'An AQP4-IgG-negative patient has optic neuritis and acute myelitis during one attack. Which additional feature is especially relevant to meeting the stricter seronegative NMOSD criteria?',
 'An acute cord lesion extending over at least three contiguous vertebral segments, with the other required clinical/MRI and exclusion criteria satisfied', [
 ('CSF oligoclonal bands alone, regardless of the MRI phenotype', 'Oligoclonal bands can occur in several disorders and do not replace the syndrome-specific MRI requirements for AQP4-negative NMOSD; persistent bands may instead strengthen consideration of MS.'),
 ('Two attacks of isolated optic neuritis without a second core syndrome', 'Repeated attacks of the same syndrome supply time separation but not the required dissemination in space across core characteristics for the seronegative NMOSD framework.'),
 ('A positive serum MOG-IgG result that meets MOGAD criteria, retained under the same NMOSD label', 'When a compatible presentation meets MOGAD criteria, MOGAD is the preferred distinct etiologic diagnosis rather than treating it as simply AQP4-negative NMOSD.')],
 [S('Stricter Clinical and Imaging Rules', '**AQP4-negative or unknown-status NMOSD** requires at least two different core characteristics occurring in one or more attacks. At least one must be optic neuritis, acute myelitis with LETM, or area postrema syndrome.',
    'Dissemination in space is required, but the two syndromes need not occur at separate times. A single simultaneous opticospinal attack can therefore provide the necessary clinical distribution.',
    'Additional syndrome-specific MRI requirements must be met. Myelitis requires a longitudinally extensive lesion of at least three contiguous vertebral segments, or an appropriate long segment of focal cord atrophy with a compatible previous episode.'),
  S('Avoiding an Overinclusive Label', '**Negative AQP4 testing does not automatically establish seronegative NMOSD.** Consider timing, treatment exposure, assay quality and repeat testing when appropriate.',
    'Evaluate serum MOG-IgG using a cell-based assay when the phenotype suggests MOGAD. Also consider MS, sarcoidosis, infection, vascular myelopathy and systemic inflammatory disease.',
    'The full optic-nerve, brainstem and cerebral MRI requirements depend on the corresponding syndrome. A vague clinical history plus nonspecific white-matter lesions is insufficient for this higher-specificity framework.')], ['NEMOS1'])

add('Neuromyelitis optica spectrum disorder', 'Area Postrema Syndrome',
 'A woman has five days of otherwise unexplained intractable vomiting and hiccups. MRI shows a focal dorsal medullary lesion near the fourth ventricle. Which diagnosis should be specifically investigated?',
 'AQP4-IgG-associated NMOSD presenting with area postrema syndrome', [
 ('A vestibular migraine episode', 'Vestibular migraine can cause episodic vertigo and nausea, but persistent hiccups with a dorsal medullary lesion is a more specific clue to area postrema involvement.'),
 ('A peripheral acute vestibular neuritis', 'Vestibular neuritis causes a peripheral vestibular syndrome with vertigo and nystagmus, not a focal dorsal medullary lesion or a characteristic prolonged hiccup syndrome.'),
 ('A typical gastrointestinal dysmotility syndrome', 'Gastrointestinal disease can cause prolonged vomiting and should be assessed, but does not explain the anatomically concordant dorsal medullary lesion in this presentation.')],
 [S('Anatomical Localization', '**The area postrema** lies in the dorsal medulla adjacent to the fourth ventricle and participates in emetic responses. Its involvement can produce otherwise unexplained nausea, vomiting or hiccups.',
    'Area postrema syndrome is one of the six NMOSD core characteristics and may precede optic neuritis or myelitis. Send serum AQP4-IgG by a validated cell-based assay in the appropriate clinical context.',
    'When MRI does not show acute area postrema involvement, NEMOS specifies persistence for at least 48 hours; a shorter syndrome can qualify when the characteristic acute dorsal brainstem lesion is demonstrated.'),
  S('Differential and Treatment', '**Exclude gastrointestinal, metabolic, toxic and structural explanations.** The lesion and phenotype support a central process but are not independently antibody proof.',
    'A suspected inflammatory NMOSD attack warrants urgent specialist assessment and treatment, usually high-dose IV methylprednisolone with early apheresis for severe or inadequately responsive disease.',
    'Antiemetics, hydration and electrolyte correction provide supportive care but do not replace treatment of the underlying inflammatory attack. Recognizing this syndrome early can prevent misclassification as an isolated gastrointestinal illness.')], ['NEMOS1','NEMOS2'])

add('Neuromyelitis optica spectrum disorder', 'Comparing Inflammatory Myelitis Patterns',
 'An adult with severe acute myelitis has a centrally located lesion spanning six vertebral segments with marked cord swelling. Which interpretation is most appropriate?',
 'The pattern should prompt AQP4-IgG and MOG-IgG evaluation rather than being assumed to represent typical MS myelitis', [
 ('The lesion length alone definitively establishes AQP4-positive NMOSD', 'LETM is characteristic of NMOSD but also occurs in MOGAD, sarcoidosis and other inflammatory, infectious or vascular disorders; serology and the complete evaluation remain necessary.'),
 ('The pattern is the usual short peripheral cord lesion of MS', 'Typical MS cord lesions are commonly short and peripheral on axial imaging; a swollen central six-segment lesion is an important reason to reconsider that assumption.'),
 ('Longitudinally extensive disease excludes MOGAD', 'MOG-associated myelitis can be longitudinally extensive and may involve central gray matter or the conus; lesion length does not exclude that diagnosis.')],
 [S('Longitudinal and Axial Distribution', '**LETM** conventionally spans at least three contiguous vertebral segments. Central extensive involvement with swelling is a red flag against automatically classifying an attack as typical MS myelitis.',
    'AQP4-associated disease can be severe with central cord involvement. MOGAD often involves gray matter and may show an axial H-sign or conus involvement; MS more often produces short peripheral lesions.',
    'These are tendencies, not absolute boundaries. Early scans, late scans and treatment can alter the apparent length, and AQP4-positive attacks can occasionally have short lesions.'),
  S('Etiologic Workup', '**Exclude compression and vascular disease urgently**, then integrate MRI, CSF, serum cell-based antibody assays and targeted systemic/infectious investigations.',
    'A cord lesion alone cannot identify one antibody. Optic-nerve phenotype, area postrema symptoms, brain MRI and attack history help refine the differential.',
    'Treat a disabling inflammatory attack promptly while completing the etiologic evaluation. The long-term preventive strategy differs across MS, AQP4-positive NMOSD and MOGAD.')], ['NEMOS1'], table=(['Disorder','Common cord pattern','Important qualification'],[
 ['MS','Short, often peripheral lesions','Atypical patterns require reassessment'],['AQP4-NMOSD','Often central LETM with swelling','Short lesions can occur'],['MOGAD','Gray-matter H-sign; conus or LETM possible','No single MRI sign proves the antibody etiology']]))

add('Neuromyelitis optica spectrum disorder', 'Early Apheresis in a Severe NMOSD Attack',
 'An AQP4-positive woman presents with rapidly worsening paraplegia from myelitis. After the first days of IV methylprednisolone there is no meaningful improvement. Which management sequence is preferred?',
 'Add early plasma exchange or immunoadsorption rather than waiting through a prolonged oral steroid course', [
 ('Defer apheresis until an oral taper has been completed over several months', 'An oral taper can help bridge prevention after acute treatment, but completing it before rescue would delay time-sensitive treatment of severe ongoing attack-related disability.'),
 ('Start satralizumab alone and wait for its preventive effect to rescue the current paralysis', 'Satralizumab can prevent attacks in appropriate AQP4-positive disease, but its preventive role does not replace rapid rescue of a devastating acute attack.'),
 ('Use a rehabilitation programme as the only next intervention', 'Rehabilitation is essential after stabilization, but does not rapidly remove circulating inflammatory mediators or replace escalation of inadequately controlled acute inflammation.')],
 [S('Attack-Related Disability', '**NMOSD disability is predominantly attack related**, so timely suppression of severe inflammation is especially important. Give IV methylprednisolone, commonly 1 g daily for three to five days, and assess response early.',
    'NEMOS recommends early apheresis when the response is insufficient during the first days. In selected severe attacks or a history of poor steroid response, first-line or concomitant apheresis may be appropriate.',
    'Plasma exchange and immunoadsorption are both options where available. Common courses use approximately five exchanges, with additional sessions based on response and service protocol.'),
  S('After Rescue', '**An individualized oral steroid taper and attack-preventive therapy** may reduce early recurrence while the preventive treatment becomes effective. This differs from the usual short-pulse approach to a typical MS relapse.',
    'Monitor apheresis access, blood pressure, calcium, fibrinogen and infection risk. Coordinate antibody sampling before plasma exchange when feasible without delaying treatment.',
    'Bladder care, thrombosis prevention, skin protection and rehabilitation accompany disease-directed therapy. They should proceed alongside treatment rather than being treated as substitutes for it.')], ['NEMOS2'])

add('Neuromyelitis optica spectrum disorder', 'Targets of NMOSD Preventive Biologics',
 'Which pairing correctly identifies the target of a biologic used to prevent attacks in AQP4-IgG-positive NMOSD?',
 'Inebilizumab — CD19', [
 ('Eculizumab — IL-6 receptor', 'Eculizumab inhibits complement protein C5. IL-6-receptor blockade instead describes satralizumab or tocilizumab.'),
 ('Satralizumab — CD20', 'Satralizumab blocks the IL-6 receptor; CD20 depletion is the mechanism of rituximab and several MS B-cell therapies.'),
 ('Rituximab — complement C5', 'Rituximab targets CD20-positive B cells. C5 inhibition is the mechanism of eculizumab and ravulizumab.')],
 [S('Mechanistic Selection', '**Inebilizumab targets CD19**, depleting a broad B-lineage population. Eculizumab and ravulizumab inhibit C5, while satralizumab inhibits IL-6 receptor signalling.',
    'Rituximab targets CD20 and has substantial NMOSD experience; approval status differs by jurisdiction. Availability and regulatory status should not be inferred from approval for another autoimmune disease.',
    'These preventive treatments have differing onset, route, dosing and monitoring requirements. There is no universally proven best agent from a direct head-to-head randomized comparison of all options.'),
  S('Drug-Specific Preparation', '**Complement inhibition requires meningococcal risk mitigation.** B-cell-directed therapy requires HBV screening, immunoglobulin assessment and vaccination planning; IL-6 blockade requires attention to infection, neutrophils and liver tests.',
    'Examples of maintenance schedules include inebilizumab 300 mg IV on days 1 and 15 followed by six-monthly dosing, and satralizumab 120 mg subcutaneously at weeks 0, 2 and 4, then every four weeks, for eligible patients under the applicable label.',
    'Select therapy according to attack severity, relapse history, comorbidity, reproductive plans and access. Do not extrapolate AQP4-positive randomized evidence indiscriminately to double-seronegative disease or MOGAD.')], ['NEMOS2'], style='direct', table=(['Target','Examples','Prominent safety issue'],[
 ['C5','Eculizumab; ravulizumab','Meningococcal infection despite vaccination'],['CD19','Inebilizumab','Infection, HBV reactivation, low immunoglobulins'],['IL-6 receptor','Satralizumab; tocilizumab','Infection, liver-test and neutrophil abnormalities'],['CD20','Rituximab','HBV reactivation and hypogammaglobulinemia']]))

add('Neuromyelitis optica spectrum disorder', 'Meningococcal Prevention Before C5 Inhibition',
 'A patient is to begin eculizumab for AQP4-positive NMOSD. Which preventive strategy is appropriate?',
 'Provide MenACWY and MenB vaccination, ideally at least two weeks before treatment, with antimicrobial planning if treatment cannot wait', [
 ('Give MenACWY alone and regard all meningococcal risk as eliminated', 'MenACWY does not cover serogroup B, and even complete vaccination does not eliminate meningococcal risk during terminal complement blockade.'),
 ('Give MenB alone and omit clinical infection counselling', 'MenB alone leaves other relevant serogroups unaddressed, and breakthrough disease remains possible; patients need prompt-action counselling even after both vaccine types.'),
 ('Rely on pneumococcal vaccination as the specific meningococcal protection', 'Pneumococcal vaccination may be otherwise indicated but does not replace meningococcal vaccination or other risk mitigation for C5-inhibitor-associated susceptibility.')],
 [S('Complement-Dependent Bacterial Defence', '**C5 inhibition markedly increases meningococcal disease risk.** CDC recommends both MenACWY and MenB vaccination, ideally completed or updated at least two weeks before the first complement-inhibitor dose.',
    'If urgent therapy cannot safely wait, follow the product label and specialist antimicrobial prophylaxis plan. Vaccination and antibiotics reduce risk but cannot guarantee prevention.',
    'Maintain recommended boosters while risk persists. Under current CDC guidance, MenACWY boosters are generally every five years; MenB boosters are given one year after the primary series and then every two to three years.'),
  S('Breakthrough Infection', '**Fever, headache, neck stiffness, rash or an acute systemic illness require immediate assessment**, even in a vaccinated patient receiving prophylaxis.',
    'Some cases involve nongroupable meningococci that are less commonly invasive in people with intact complement activity. A reassuring vaccine history must not delay evaluation or empiric treatment.',
    'Balance prevention timing with the neurological risk of delayed NMOSD therapy. A coordinated vaccination, antimicrobial and emergency-access plan supports timely treatment of both risks.')], ['MENING','NEMOS2'])

add('Neuromyelitis optica spectrum disorder', 'MS Therapies Are Not Interchangeable with NMOSD Prevention',
 'A woman labeled as having MS has severe recurrent opticospinal attacks despite interferon beta. A validated serum assay is now clearly AQP4-IgG positive and the clinical criteria support NMOSD. What is the best treatment implication?',
 'Reclassify the disease and replace interferon beta with an appropriate NMOSD attack-prevention strategy', [
 ('Increase interferon beta because it is the standard preventive agent for AQP4-positive disease', 'Interferon beta is an MS therapy and can be ineffective or associated with worsening in NMOSD; escalating it does not address the revised etiology.'),
 ('Switch to fingolimod as the preferred disease-specific NMOSD agent', 'Fingolimod treats relapsing MS but has been associated with severe NMOSD worsening and should not be selected as NMOSD prevention.'),
 ('Switch to natalizumab because leukocyte-trafficking blockade is established NMOSD prevention', 'Natalizumab has not provided reliable NMOSD control and can be associated with worsening; efficacy in MS does not establish efficacy in AQP4-associated astrocytopathy.')],
 [S('Etiology Determines Prevention', '**AQP4-positive NMOSD and MS are distinct diseases.** Interferon beta, fingolimod and natalizumab should not be substituted for NMOSD-specific preventive therapy.',
    'AQP4-associated attacks can cause severe visual and spinal disability. After acute treatment, prevention commonly uses appropriate C5 inhibition, CD19-directed therapy, IL-6-receptor blockade or other established immunosuppression according to access and patient factors.',
    'Rituximab, mycophenolate and azathioprine also have roles in selected settings, but onset, evidence, monitoring and approval status differ.'),
  S('Revisiting a Prior MS Diagnosis', '**Recurrent severe optic neuritis, LETM, area postrema symptoms or poor recovery** should prompt diagnostic reassessment rather than repeatedly labeling the course as unusually aggressive MS.',
    'Confirm assay quality and clinical concordance, especially when a result conflicts with a strongly typical MS phenotype. Antibody interpretation must remain integrated with imaging and examination.',
    'The transition should be coordinated to control active inflammation and prevent further attacks without unnecessary overlapping toxicity. Avoid treating a diagnostic label as fixed when new reliable evidence changes the underlying disease classification.')], ['NEMOS1','NEMOS2'])

R.update({
 'MOGFULL': ('International MOGAD Panel proposed criteria: full position paper, 2023', 'https://bcneuro.ca/wp-content/uploads/2026/04/Diagnosis-of-myelin-oligodendrocyte-glycoprotien-antibody-associated-Disease-International-MOGAD-Panel-Proposed-criteria.pdf'),
 'MOGST': ('Trewin et al. MOGAD corticosteroid dose and taper duration, multicentre cohort, 2024', 'https://jnnp.bmj.com/content/early/2024/05/16/jnnp-2024-333463?versioned=true'),
 'MOGIVIG': ('Chen et al. Maintenance IVIG in adult MOGAD, retrospective cohort, 2022', 'https://jamanetwork.com/journals/jamaneurology/fullarticle/2790493'),
 'METEOR': ('Phase III METEOROID MOGAD results: investigator conference abstract, 2026', 'https://www.neurology.org/doi/abs/10.1212/WNL.0000000000217915'),
 'MOGFDA': ('FDA orphan indication database: satralizumab for MOGAD, checked November 2026', 'https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=824521'),
 'MOGFILING': ('Sponsor announcement of MOGAD priority review, September 2026', 'https://www.roche.com/media/releases/med-cor-2026-09-10'),
})

add('MOG antibody-associated disease', 'Interpreting Low-Positive MOG-IgG',
 'A serum fixed cell-based assay reports MOG-IgG at 1:20 in a patient evaluated after optic neuritis. Under the 2023 international criteria, what additional evidence is needed to support MOGAD?',
 'Negative AQP4-IgG, at least one specified supporting clinical/MRI feature, and exclusion of a better diagnosis', [
 ('Treat the low-positive result as sufficient irrespective of the clinical phenotype', 'Low-positive results have lower predictive value and require additional phenotype support; indiscriminate testing can generate misleading positives in patients with another disease.'),
 ('Require the serum titre to exceed 1:100 in every patient', 'A fixed-assay titre of at least 1:100 is clear positive, but the criteria allow low-positive cases when the required additional supporting and exclusion conditions are satisfied.'),
 ('Require CSF-restricted oligoclonal bands as the defining additional test', 'Oligoclonal bands are neither required nor defining for MOGAD. They may occur, but persistent intrathecal bands with an MS-typical pattern should prompt careful differential review.')],
 [S('Assay-Dependent Categories', '**MOG-IgG should be measured with a validated cell-based assay.** For fixed assays, clear positivity is a titre of at least 1:100; titres of at least 1:10 but below 1:100 are classified as low positive.',
    'Live-assay cutoffs are assay specific. Do not transfer a fixed-assay dilution threshold uncritically to every live-cell method or flow-cytometry result.',
    'A low-positive or untitered-positive serum result requires AQP4-IgG negativity and at least one specified supporting clinical or MRI feature, in addition to a core demyelinating event and exclusion of a better explanation.'),
  S('Clinical Specificity', '**Supporting optic-neuritis features** include bilateral simultaneous involvement, prominent disc edema, longitudinally extensive optic-nerve disease and perineural enhancement, as specified in the criteria.',
    'A clear-positive result in a compatible core event does not require the same extra supporting-feature step, but exclusion of a better diagnosis remains necessary.',
    'Avoid routine broad MOG screening in a strongly typical MS phenotype. Pretest probability affects positive predictive value, and a low titre cannot override a more convincing alternative diagnosis.')], ['MOGFULL'], style='direct')

add('MOG antibody-associated disease', 'The MOG-Associated Optic-Neuritis Phenotype',
 'A young adult develops bilateral painful visual loss with marked optic-disc edema. MRI shows long anterior optic-nerve lesions and perineural enhancement. Which antibody-associated diagnosis is most strongly suggested?',
 'MOG antibody-associated disease', [
 ('AQP4-IgG-positive NMOSD', 'AQP4 disease can cause severe bilateral optic neuritis, but posterior/chiasmal involvement and poor recovery are common concerns; marked disc swelling with anterior perineural involvement more strongly suggests MOGAD.'),
 ('Typical MS-associated optic neuritis', 'MS optic neuritis is commonly unilateral with a shorter optic-nerve lesion and less prominent disc swelling; bilateral extensive perineural disease is an important reason to test for alternatives.'),
 ('Nonarteritic anterior ischemic optic neuropathy', 'Ischemic optic neuropathy can produce disc swelling, usually with sudden painless visual loss and a different risk profile; the painful bilateral inflammatory MRI pattern is less typical.')],
 [S('Anatomical Pattern', '**MOG-associated optic neuritis** commonly produces prominent disc edema, bilateral involvement and long anterior optic-nerve lesions. Perineural or optic-nerve-sheath enhancement is a useful supporting clue.',
    'The pattern is suggestive rather than pathognomonic. Orbital inflammation, sarcoidosis, infection and other causes of optic perineuritis may also enhance around the nerve.',
    'Send serum MOG-IgG with a validated cell-based assay and interpret the result using the 2023 criteria. Consider AQP4-IgG testing because the differential affects prognosis and prevention.'),
  S('Recovery and Attack Treatment', '**Visual loss can be severe at nadir despite substantial steroid responsiveness.** Recurrent attacks may still cause cumulative retinal/optic-nerve injury, so good recovery from one event does not make recurrence harmless.',
    'Acute treatment usually uses high-dose IV methylprednisolone, with early consideration of plasma exchange or IVIG for severe or inadequately responsive attacks according to specialist assessment.',
    'A slower individualized steroid taper is often considered because early recurrence during withdrawal is recognized. Relapse prevention decisions depend on the disease course and attack consequences, not MRI morphology alone.')], ['MOGFULL','MOGST'])

add('MOG antibody-associated disease', 'Conus Involvement and the H-Sign',
 'An adult with acute urinary retention and paraparesis has conus involvement and central gray-matter T2 hyperintensity forming an axial H-sign. Which diagnosis should be specifically considered?',
 'MOG antibody-associated myelitis', [
 ('Typical MS myelitis as the presumptive diagnosis without antibody testing', 'MS often produces short peripheral cord lesions; prominent gray-matter H-sign and conus involvement should trigger consideration of MOGAD and other causes rather than an automatic MS label.'),
 ('Spinal dural arteriovenous fistula as proven by the H-sign', 'A dural fistula can involve the conus and produce sphincter dysfunction, but an H-sign does not prove it; course, perimedullary vessels and vascular imaging determine that diagnosis.'),
 ('AQP4-positive myelitis as excluded because the lesion is central', 'Central cord involvement is also common in AQP4 disease. The MOG-suggestive pattern does not exclude NMOSD, and both antibody etiologies may require investigation.')],
 [S('Gray-Matter Predominance', '**The H-sign** represents preferential involvement of central gray matter on axial spinal MRI. Conus disease and prominent sphincter symptoms are additional clues to MOG-associated myelitis.',
    'MOGAD may cause longitudinally extensive or shorter cord lesions. Lesion length alone cannot distinguish it from AQP4-associated myelitis or other inflammatory disease.',
    'Obtain serum MOG-IgG using a cell-based assay and assess AQP4-IgG where appropriate. A supportive MRI sign is interpreted within the complete diagnostic framework.'),
  S('Competing Causes', '**Cord infarction, viral anterior-horn disease and vascular congestion** can also affect central gray matter. Hyperacute onset, diffusion restriction, systemic infection or abnormal perimedullary vessels can redirect evaluation.',
    'Urgently exclude compression. Review the tempo, CSF, contrast pattern and entire neuraxis rather than treating one axial image as etiologically definitive.',
    'For an inflammatory attack, prompt high-dose steroids and appropriately timed rescue treatment aim to limit disability. Bladder drainage, bowel care and rehabilitation are important concurrent measures because sphincter deficits may persist despite motor recovery.')], ['MOGFULL','NEMOS1'])

add('MOG antibody-associated disease', 'Cortical Encephalitis with Seizures',
 'A young adult has headache, focal seizures and a unilateral cortical FLAIR-hyperintense lesion with leptomeningeal enhancement. Infectious encephalitis is being urgently evaluated. Which immune demyelinating disorder can produce this phenotype?',
 'MOG antibody-associated cortical encephalitis', [
 ('A typical chronic MS plaque without cortical inflammation', 'MS can be associated with seizures and cortical lesions, but the acute cortical encephalitis phenotype with headache and meningeal enhancement warrants specific consideration of MOGAD and other mimics.'),
 ('A purely peripheral antibody-mediated neuropathy', 'Peripheral neuropathies can produce weakness and sensory deficits but do not explain cortical MRI inflammation and focal seizures localized to the cerebral cortex.'),
 ('A noninflammatory postictal change established without further workup', 'Postictal MRI abnormalities are a genuine differential, but their possibility does not establish the cause; inflammatory or infectious disease can provoke both seizures and cortical signal change.')],
 [S('FLAMES Phenotype', '**MOG-associated cortical encephalitis**, often called FLAMES, can feature seizures, headache, cortical FLAIR hyperintensity and sometimes overlying leptomeningeal enhancement. Unilateral cortical involvement is characteristic but not obligatory.',
    'It is included among the core clinical events in the 2023 MOGAD criteria. Confirm serum MOG-IgG with a suitable cell-based assay and apply additional support requirements for low-positive results.',
    'CSF may be inflammatory, and fever can occur. These features do not safely separate immune disease from infection at presentation.'),
  S('Time-Critical Differential', '**HSV and other infectious encephalitides must be considered urgently.** Obtain appropriate CSF, MRI and EEG, and start empiric pathogen-directed treatment when clinically indicated rather than waiting for antibody results.',
    'Other alternatives include autoimmune encephalitis, vasculitis, neoplasm and seizure-related reversible MRI abnormalities. Evolution on follow-up and the full laboratory evaluation help distinguish them.',
    'Treat seizures and the underlying cause concurrently. Once infection is appropriately addressed and MOGAD is supported, corticosteroids are commonly effective; severe or refractory disease may require specialist escalation.')], ['MOGFULL'])

add('MOG antibody-associated disease', 'ADEM Requires an Encephalopathic Presentation',
 'A child develops acute multifocal neurological deficits and behavioral change not explained by fever, sedation or a postictal state. MRI shows large poorly marginated bilateral white-matter lesions with deep-gray involvement. Which syndrome best fits?',
 'Acute disseminated encephalomyelitis', [
 ('A typical isolated first MS optic-neuritis attack', 'A focal optic-neuritis attack does not account for unexplained encephalopathy and diffuse multifocal brain lesions; that combination is more consistent with ADEM.'),
 ('Radiologically isolated syndrome', 'Radiologically isolated presentations lack a corresponding clinical demyelinating event, whereas this child has both multifocal deficits and encephalopathy.'),
 ('A monophasic course proven by the initial MRI alone', 'ADEM is often monophasic, but an initial scan cannot prove the future course; follow-up is needed and relapsing MOGAD or another diagnosis may emerge.')],
 [S('Clinical Syndrome', '**ADEM** is an acute polyfocal inflammatory demyelinating presentation with encephalopathy not otherwise explained. The pediatric consensus phenotype is especially relevant because MOGAD is common among children with this presentation.',
    'MRI often shows large, bilateral, poorly demarcated white-matter abnormalities, sometimes involving basal ganglia or thalami. The pattern differs from the more sharply defined typical MS lesion distribution.',
    'Encephalopathy distinguishes ADEM from many otherwise similar multifocal demyelinating attacks. Altered behavior or consciousness must be evaluated for infection, metabolic disturbance, medication effects and seizures.'),
  S('Etiology and Follow-up', '**ADEM is a syndrome, not an antibody diagnosis.** Test serum MOG-IgG where appropriate; positivity can identify MOGAD, but ADEM can also occur without MOG-IgG.',
    'Do not apply the MS diagnostic algorithm uncritically to an ADEM presentation. Clinical evolution, follow-up MRI and antibody interpretation help distinguish monophasic ADEM from a relapsing disorder.',
    'Acute treatment commonly uses IV methylprednisolone with an individualized taper; severe refractory disease may require IVIG or plasma exchange. Follow-up includes motor, visual, behavioral and cognitive assessment even when gross neurological recovery is good.')], ['MOGFULL','MC24'])

add('MOG antibody-associated disease', 'Acute MOGAD and Steroid Tapering',
 'A patient with confirmed MOGAD improves rapidly after IV methylprednisolone for severe optic neuritis. Which subsequent principle is most appropriate?',
 'Individualize a slower oral taper because early relapse during rapid steroid withdrawal is recognized', [
 ('Use the short-pulse MS strategy as mandatory for every MOGAD attack', 'A short pulse without a taper may suit many MS relapses, but MOGAD has recognized steroid-dependent early recurrence and requires a separate individualized discussion.'),
 ('Continue high-dose prednisone indefinitely regardless of toxicity', 'Prolonged steroids may suppress attacks but expose patients to infection, osteoporosis, metabolic and adrenal complications; indefinite high-dose therapy is not a universal strategy.'),
 ('Start a standard MS platform DMT as proven MOGAD relapse prevention', 'Interferon beta and glatiramer are MS therapies with no comparable established preventive efficacy in MOGAD; etiologic classification changes the maintenance discussion.')],
 [S('Attack Treatment', '**High-dose corticosteroids** are commonly used for acute MOGAD, often IV methylprednisolone 1 g daily for three to five days in adults. Treat severe attacks promptly rather than waiting for antibody titres to fall.',
    'For severe or inadequately responsive disease, consider early plasma exchange or IVIG according to the attack, prior response and available expertise.',
    'The post-pulse taper is often slower than for a typical MS relapse. Balance early recurrence risk against diabetes, infection, psychiatric effects, bone health and other steroid toxicity.'),
  S('Evidence and Limits', '**A 2024 multicentre observational cohort** associated prednisone at least 12.5 mg/day in adults for at least three months from onset with longer time to first relapse. This is not a randomized mandate for every patient.',
    'The optimum taper remains uncertain and patient dependent. A history of recurrence during withdrawal, severe residual deficits or recurrent attacks can favour a steroid-sparing prevention discussion.',
    'Monitor blood pressure, glucose, infection, ocular and bone health during prolonged therapy, and account for adrenal suppression when tapering. A first event does not automatically require lifelong immunotherapy because MOGAD can remain monophasic.')], ['MOGST','MOGFULL'])

add('MOG antibody-associated disease', 'Maintenance IVIG and Evolving MOGAD Evidence',
 'An adult with relapsing MOGAD is considering maintenance IVIG. Which interpretation of the evidence is most accurate?',
 'Adult cohort data support an association with fewer relapses, but do not prove randomized superiority over every alternative', [
 ('The 2022 IVIG cohort proves that every patient must receive lifelong therapy after one attack', 'The study was observational and did not establish either universal treatment after one attack or a mandatory lifelong duration; monophasic disease remains possible.'),
 ('Successful AQP4-positive NMOSD trials automatically establish equal efficacy in MOGAD', 'The diseases differ biologically and clinically; efficacy and approval in AQP4-positive NMOSD cannot simply be transferred to MOGAD.'),
 ('No randomized MOGAD prevention data had been reported by November 2026', 'That overlooks the 2026 METEOROID randomized satralizumab results; new trial evidence must be distinguished from the older observational IVIG literature and from regulatory approval.')],
 [S('Observational IVIG Evidence', '**A 2022 retrospective adult cohort** found lower relapse activity during maintenance IVIG. Doses of at least 1 g/kg every four weeks were associated with fewer breakthrough relapses than lower or less frequent dosing.',
    'Treatment selection, concomitant therapy and other confounding limit causal inference. This is supportive evidence rather than a randomized head-to-head proof that IVIG is always best.',
    'Discuss infusion burden, thrombosis, hemolysis, renal risk, headache and aseptic meningitis. Individualize the dose, interval and duration according to response and tolerability.'),
  S('Current Evidence Versus Approval', '**METEOROID reported positive randomized satralizumab results in 2026**, including a reported 68% reduction in relapse risk versus placebo. The conference and sponsor-reported results are a different evidence category from the IVIG cohort.',
    'As checked in November 2026, the FDA orphan indication record did not list MOGAD approval; a September sponsor announcement described priority review with a January 2027 decision target. Priority review is not approval.',
    'Choose prevention for a relapsing or high-consequence course through specialist shared decision-making. Do not present an emerging trial, a different disease indication or an observational association as interchangeable evidence.')], ['MOGIVIG','METEOR','MOGFDA','MOGFILING'])

R.update({
 'OPEN': ('Masdeu et al. Open-ring imaging sign in atypical brain demyelination, 2000', 'https://pubmed.ncbi.nlm.nih.gov/10751251/'),
 'BALO': ('Clinical and radiologic features, pathology and treatment of Balo concentric sclerosis, 2021 cohort', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC8362356/'),
 'BAC': ('Baclofen tablets prescribing information', 'https://dailymed.nlm.nih.gov/dailymed/getFile.cfm?setid=f4e8cbc5-b1f2-4331-a267-d5bd90bcde8a&type=pdf'),
 'DAL': ('Ampyra dalfampridine extended-release prescribing information', 'https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=974fb2af-7012-4989-b330-e44a31c9c3e5'),
})

add('Other demyelinating presentations and symptoms', 'An Open-Ring Tumefactive Lesion',
 'A 31-year-old has subacute hemiparesis and a 3-cm white-matter lesion with incomplete ring enhancement open toward the cortex. Which interpretation is best?',
 'Tumefactive demyelination is strongly suggested, while neoplasm and infection still require assessment', [
 ('A pyogenic abscess is definitively established by the incomplete ring', 'An abscess can enhance in a ring, often with central diffusion restriction, but an open ring toward gray matter is a recognized clue favouring demyelination rather than proof of abscess.'),
 ('Primary CNS lymphoma is excluded because demyelination is possible', 'Lymphoma can mimic inflammatory disease and can transiently improve with steroids. A suggestive imaging sign cannot safely exclude malignancy when the overall course remains concerning.'),
 ('Glioblastoma is the only plausible cause of any lesion larger than 2 cm', 'High-grade glioma is a genuine competing diagnosis, but inflammatory demyelination can also produce large mass-like lesions; size alone is not etiologically specific.')],
 [S('Tumefactive Demyelination', '**A large inflammatory demyelinating lesion**, often larger than 2 cm, may resemble a tumor clinically and radiologically. An incomplete ring with the opening toward cortex or gray matter is a useful supporting sign.',
    'The enhancing edge generally reflects the active inflammatory margin. Edema and mass effect can occur, so their presence does not automatically establish neoplasm.',
    'Assess the rest of the brain and cord for characteristic lesions and review the clinical tempo, immune status, diffusion pattern, perfusion and other sequences.'),
  S('Diagnostic Strategy', '**An open ring is supportive rather than absolute proof.** Differential diagnoses include glioma, lymphoma, metastasis, abscess and other inflammatory lesions.',
    'CSF and serum studies can help when safe and clinically indicated. If uncertainty persists or the course is atypical, multidisciplinary review and biopsy may be necessary.',
    'Steroids can improve demyelination but also temporarily alter lymphoma and reduce biopsy yield. Coordinate treatment and tissue decisions when malignancy is a serious possibility; improvement alone is not an adequate diagnostic test.')], ['OPEN','BALO'])

add('Other demyelinating presentations and symptoms', 'Concentric Demyelination',
 'MRI shows a mass-like cerebral lesion with alternating concentric bands of differing T2 signal and ring-like enhancement. Which pathological pattern best corresponds?',
 'Alternating layers of demyelinated and relatively preserved myelin in a Balo-type lesion', [
 ('Uniform liquefactive necrosis within a pyogenic abscess cavity', 'An abscess typically has a cavity with pus and characteristic diffusion behavior; alternating concentric myelin preservation and loss is a different pathological organization.'),
 ('A homogeneous sheet of malignant lymphocytes as a defining feature of this MRI pattern', 'Primary CNS lymphoma is a serious differential for some mass-like lesions, but concentric alternating myelin bands correspond more specifically to a Balo-type demyelinating pattern.'),
 ('A completed arterial-territory infarct established by concentric rings alone', 'Ischemia is assessed through onset, vascular distribution and diffusion evolution. Concentric ring architecture is not itself proof of an arterial-territory infarct.')],
 [S('Radiological–Pathological Correlation', '**Balo concentric sclerosis** describes a striking pattern of alternating concentric demyelinated and relatively myelin-preserved layers. MRI can demonstrate corresponding concentric bands on T2 and postcontrast sequences.',
    'Lesions may evolve over serial imaging and can have peripheral diffusion restriction. The pattern is informative, but the complete clinical and imaging context remains necessary.',
    'Some patients have other MS-typical lesions or later meet MS criteria; others have a monophasic course. A single concentric lesion does not by itself determine the entire long-term disease trajectory.'),
  S('Treatment and Prognosis', '**High-dose corticosteroids** are commonly used for an acute symptomatic inflammatory lesion. Severe steroid-refractory disease may require plasma exchange or other specialist-directed rescue.',
    'Evidence largely comes from cohorts and case series rather than a dedicated large randomized Balo treatment trial. The syndrome should not be presented as uniformly fatal or as requiring the same lifelong regimen in every case.',
    'Biopsy can be appropriate if tumor, infection or another diagnosis remains unresolved. Subsequent prevention depends on attack history, associated lesions, diagnostic classification and the balance of benefit and treatment risk.')], ['BALO'], style='direct')

add('Other demyelinating presentations and symptoms', 'Goal-Directed Treatment of MS Spasticity',
 'A patient with MS has painful generalized leg spasms despite treatment of constipation and a urinary infection. Physiotherapy is ongoing, and the agreed goal is less nocturnal pain. Which oral drug is a usual first-line option?',
 'Baclofen', [
 ('Dalfampridine', 'Dalfampridine may improve walking speed in selected patients, but it is not the usual first-line antispastic drug for painful generalized spasms.'),
 ('Amantadine', 'Amantadine is sometimes considered for MS fatigue after individualized assessment, but does not provide the standard first-line pharmacological approach to painful generalized spasticity.'),
 ('Carbamazepine', 'Carbamazepine is useful for trigeminal neuralgia and some paroxysmal tonic symptoms; persistent generalized spasticity is more commonly approached with baclofen and physical measures.')],
 [S('Treat the Trigger and Define the Goal', '**Spasticity can worsen with infection, constipation, urinary retention, pain or poor positioning.** Address these first and use stretching, positioning and physiotherapy alongside medication.',
    'Some patients rely on increased tone for standing or transfers. Reducing tone may unmask weakness, so agree on a functional or comfort goal and reassess the actual outcome.',
    'NICE considers oral baclofen a first-line option for MS spasticity with specific treatment goals. It acts mainly through GABA-B receptors.'),
  S('Dosing and Escalation', '**Start low and titrate to benefit and tolerability.** A common adult initiation is 5 mg three times daily, with gradual increases; the cited oral tablet label gives a maximum of 80 mg/day.',
    'Sedation, dizziness and weakness may limit dosing. Renal clearance makes accumulation and neurotoxicity important in kidney impairment; use additional caution and dose adjustment or an alternative when appropriate.',
    'Do not stop established baclofen abruptly because withdrawal can be dangerous. If oral treatment fails, specialist options include other oral agents, focal botulinum toxin for a suitable distribution or intrathecal baclofen for severe refractory generalized spasticity.')], ['NICE','BAC'])

add('Other demyelinating presentations and symptoms', 'Dalfampridine: Renal and Seizure Safety',
 'An adult with MS and walking impairment asks about dalfampridine. Estimated creatinine clearance is 44 mL/min. Which decision best follows the US extended-release product label?',
 'Do not prescribe because creatinine clearance at or below 50 mL/min is a contraindication', [
 ('Prescribe 10 mg twice daily because renal function does not affect exposure', 'Dalfampridine is eliminated mainly through the kidneys; impaired clearance raises exposure and seizure risk, which is why the contraindication matters.'),
 ('Split the extended-release tablet to create an approved reduced dose', 'The extended-release tablet must be swallowed whole. Splitting changes delivery and does not provide a validated labeled regimen for moderate renal impairment.'),
 ('Use it specifically to reduce the frequency of inflammatory relapses', 'Dalfampridine is a symptomatic walking treatment, not a disease-modifying agent that prevents new inflammatory attacks or replaces an MS DMT.')],
 [S('Mechanism and Indication', '**Dalfampridine, also called prolonged-release fampridine,** blocks potassium channels and can improve conduction in demyelinated axons. It can improve walking performance in a subset of patients.',
    'The US extended-release dose is ==10 mg twice daily, approximately twelve hours apart==. Higher doses do not add established benefit and increase adverse effects, particularly seizures.',
    'Assess meaningful functional response rather than continuing solely because the drug has been started. It does not treat an acute relapse or prevent disease progression.'),
  S('Contraindications and Monitoring', '**A history of seizure or creatinine clearance at or below 50 mL/min is a contraindication.** Estimate clearance before prescribing and monitor renal function during use.',
    'Even mild impairment, with clearance 51–80 mL/min, can produce higher exposure and requires careful benefit-risk assessment. Do not substitute a normal-looking serum creatinine for an actual clearance estimate.',
    'Swallow tablets whole, do not double a missed dose and avoid duplicate 4-aminopyridine products. If a seizure occurs, permanently discontinue according to the label. The patient in the stem is below the renal safety threshold.')], ['DAL'])

# Final chapter-level editorial review.
rows[26]['table'] = (['Core syndrome','Additional MRI pattern for seronegative/unknown-status assessment'], [
 ['Optic neuritis','Normal/nonspecific brain MRI OR optic-nerve lesion involving at least half its length or the chiasm'],
 ['Acute myelitis','Cord lesion spanning at least 3 contiguous vertebral segments; or corresponding long focal atrophy after a compatible prior attack'],
 ['Area postrema syndrome','Dorsal medullary/area postrema lesion'],
 ['Other brainstem syndrome','Periependymal brainstem lesion near the fourth ventricle'],
 ['Diencephalic syndrome','Typical periependymal third-ventricular or hypothalamic/thalamic lesion'],
 ['Cerebral syndrome','Typical extensive periependymal, long callosal/corticospinal or large confluent white-matter lesion; interpret with the full syndrome']])
rows[35]['others'] = [
 ('Typical MS-associated partial myelitis', 'MS remains a differential, but commonly causes short peripheral cord lesions; conus and gray-matter-predominant disease should specifically prompt MOG testing rather than a presumptive MS label.'),
 ('Spinal dural arteriovenous fistula', 'A fistula can cause conus-related sphincter dysfunction and central edema, especially with a progressive course and perimedullary vessels; it must be assessed, but this acute H-sign phenotype also specifically suggests MOG myelitis.'),
 ('Acute spinal cord infarction', 'Cord infarction can involve gray matter and cause acute sphincter deficits, especially with hyperacute onset and diffusion restriction; the tempo and vascular evaluation distinguish it from inflammatory MOG myelitis.')]
rows[36]['others'] = [
 ('Anti-NMDA-receptor encephalitis', 'This can cause seizures and behavioral, movement or autonomic abnormalities, but an isolated unilateral cortical FLAIR-inflammatory phenotype is particularly recognized in MOG-associated cortical encephalitis.'),
 ('LGI1-antibody encephalitis', 'LGI1 disease commonly affects older adults with amnesia, faciobrachial dystonic seizures and sometimes hyponatremia; medial temporal disease is more typical than the unilateral cortical MOG phenotype described.'),
 ('A noninflammatory seizure-related cortical MRI abnormality', 'Postictal changes can resemble cortical inflammation and remain a genuine differential, but should not be assumed when an inflammatory encephalitis may be causing the seizures.')]
rows[37]['question'] = 'A child develops acute multifocal neurological deficits and behavioral change not explained by fever, sedation or a postictal state. MRI shows large poorly marginated bilateral white-matter lesions with deep-gray involvement and no hemorrhage. Which syndrome best fits?'
rows[37]['others'] = [
 ('A first MS attack with multifocal deficits', 'MS can produce multifocal deficits, but prominent unexplained encephalopathy and large poorly defined lesions in a child favour an ADEM syndrome rather than a typical first MS attack.'),
 ('Autoimmune limbic encephalitis', 'Limbic encephalitis can cause behavioral change and seizures, but classically involves memory and medial temporal structures rather than this diffuse demyelinating white-matter phenotype.'),
 ('Acute hemorrhagic leukoencephalitis', 'This fulminant inflammatory disorder includes prominent hemorrhagic necrosis and often rapid severe deterioration; the absence of hemorrhage and the stated phenotype favour conventional ADEM.')]

# The complete chapter is saved only when every mapped decision has been authored.
if __name__ == '__main__':
    coverage = ROOT / 'Neurology/06. Multiple Sclerosis & Other CNS Demyelinating Disorders.coverage.json'
    c = json.loads(coverage.read_text(encoding='utf-8'))
    assert len(rows) == sum(s['questions'] for s in c['sections']) == c['plannedQuestions'], 'Draft incomplete; installation prohibited'
    index = 0
    for section in c['sections']:
        assert len(section['decisions']) == section['questions']
        for decision in section['decisions']:
            assert rows[index]['topic'] == section['section']
            rows[index]['coverageDecision'] = decision
            index += 1
    save('Neurology', 6, c['chapter'], rows, R,
         'Original postgraduate teaching synthesis with an explicit coverage map. Full Harrison subscription text was not accessed. No independent clinician review is claimed. Guideline versions and evidence limitations are stated within explanations.')
    c['status'] = 'authored_validated'
    c['authoredQuestions'] = len(rows)
    c['questionDecisions'] = [dict(question=i+1, title=r['title'], decision=r['coverageDecision']) for i,r in enumerate(rows)]
    coverage.write_text(json.dumps(c, ensure_ascii=False, indent=2), encoding='utf-8')
