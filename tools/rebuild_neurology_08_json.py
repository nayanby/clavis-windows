"""Original cognitive-disorders chapter with a coverage-driven decision sequence."""
import json
from qbank_json_chapters import question as Q, save, ROOT
R = {
 'DETECT': ('Alzheimer Association DETeCD-ADRD clinical evaluation guideline, specialty summary, 2024/2025', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11772716/'),
 'AD24': ('Alzheimer Association revised diagnosis and staging criteria, 2024', 'https://doi.org/10.1002/alz.13859'),
 'BBM25': ('Alzheimer Association blood-based biomarker clinical practice guideline, 2025', 'https://doi.org/10.1002/alz.70535'),
 'DLB': ('DLB Consortium fourth consensus report, 2017', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5496518/'),
 'FTD': ('International revised behavioral-variant FTD criteria, 2011', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3170532/'),
 'PPA': ('International classification of primary progressive aphasia variants, 2011', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3059138/'),
}
def S(h, main, *children): return (h, [(main, list(children))])
rows = []
def add(*a, **kw): rows.append(Q(*a, **kw))

add('Cognitive syndrome assessment', 'Mild Cognitive Impairment and Independence',
 'A retired accountant reports progressive forgetfulness. Testing confirms an episodic-memory deficit. He still manages medicines, finances and travel independently, using written reminders and taking longer. Which syndrome is best supported?',
 'Mild cognitive impairment', [
 ('Major neurocognitive disorder solely because objective memory impairment is present', 'Objective decline occurs in both MCI and dementia; loss of independence attributable to cognitive impairment is the important additional distinction for a major syndrome.'),
 ('Subjective cognitive decline without objective impairment', 'Subjective decline describes concern without demonstrable objective impairment on appropriate assessment; this patient has a confirmed memory deficit.'),
 ('Delirium as the principal explanation', 'Delirium is typically acute or subacute with fluctuating attention/awareness and an underlying precipitant, unlike the gradually progressive stable-attention presentation described.')],
 [S('Cognition and Everyday Function', '**Mild cognitive impairment** combines concern about decline with objective cognitive impairment while independence in everyday activities is substantially preserved.',
    'Tasks can be slower, less efficient or supported by compensatory strategies. Needing a list is not equivalent to requiring another person to take over finances or medication administration.',
    'A brief screening score is not a universal boundary between MCI and dementia. Education, language, sensory function, premorbid ability and domain profile affect interpretation.'),
  S('Etiology and Follow-up', '**MCI is a syndrome, not a single disease.** Alzheimer pathology, vascular injury, Lewy body disease, mood/sleep conditions, drugs and systemic illness can contribute.',
    'Obtain an informant history when feasible, assess function explicitly and perform a proportionate etiologic evaluation. Serial assessment can distinguish progression, stability and reversible contributors.',
    'Biomarker-confirmed MCI due to AD may be relevant to anti-amyloid eligibility, but an MCI label alone does not establish the pathology or justify every dementia medication. Discuss uncertainty and functional safety without assuming inevitable progression.')], ['DETECT','AD24'])

add('Cognitive syndrome assessment', 'When Cognitive Decline Becomes a Major Syndrome',
 'A woman has progressive memory and executive impairment. Her daughter now manages bills and medication because she repeatedly makes consequential errors. Arthritis limits shopping, but the financial and medication failures are cognitive. Which feature most strongly supports a major neurocognitive syndrome?',
 'Cognitive impairment now interferes with independent everyday function', [
 ('A screening score below one universal cutoff, regardless of baseline or function', 'Screening supports assessment but no single score universally establishes dementia across languages, educational backgrounds and premorbid abilities.'),
 ('Any need for help with shopping, regardless of the reason', 'Physical disability, transport and social circumstances can create dependence without a cognitive major syndrome; the cause of the functional loss must be identified.'),
 ('Memory impairment without evidence about the rest of the clinical course', 'Memory impairment can occur in MCI, depression, delirium or other disorders; functional impact, objective assessment and the overall course determine syndrome severity.')],
 [S('Functional Threshold', '**A major neurocognitive disorder or dementia syndrome** involves acquired cognitive decline severe enough to interfere with independence, not explained exclusively by delirium or another primary mental disorder.',
    'Complex instrumental activities often fail before basic self-care. Ask for concrete examples of errors in finances, medicines, cooking, navigation and communication.',
    'Separate inability caused by cognitive impairment from arthritis, visual loss, poverty, unfamiliar technology or a family member’s longstanding division of tasks.'),
  S('Syndrome and Disease Formulation', '**Determine severity, cognitive–behavioral pattern and likely etiology separately.** A dementia syndrome is not automatically Alzheimer disease and need not begin with amnesia.',
    'Use the patient’s account, an informant history, examination, cognitive testing and appropriate investigations. A discrepancy between history and a brief test can justify formal neuropsychological assessment.',
    'Document current safety needs and decision-making abilities individually. The syndrome label does not imply that every choice or preference is invalid, and support should be proportionate to the affected functions.')], ['DETECT'])

R['DEL'] = ('NICE CG103 delirium guidance, assessment update 2023 and subsequent updates', 'https://www.nice.org.uk/guidance/cg103/chapter/Recommendations')
R['NICE'] = ('NICE NG97 dementia assessment and management recommendations', 'https://www.nice.org.uk/guidance/ng97/chapter/recommendations')

add('Cognitive syndrome assessment', 'Delirium Superimposed on Dementia',
 'A man with stable mild dementia becomes inattentive and intermittently drowsy over two days after admission. He is now disoriented and cannot sustain a simple conversation. Which interpretation and next step are best?',
 'Suspect superimposed delirium and urgently assess precipitating medical and medication factors', [
 ('Attribute the entire change to the expected rate of Alzheimer progression', 'Neurodegenerative decline is usually slower; a two-day change in attention and arousal is a red flag for an acute superimposed process.'),
 ('Diagnose primary major depression from drowsiness alone', 'Depression can affect concentration and motivation, but this acute fluctuating attention/arousal syndrome warrants delirium assessment before a mood-only explanation.'),
 ('Assign a new permanent dementia stage from testing during the acute episode', 'Cognitive scores during delirium may substantially underestimate baseline ability; treat the acute problem and reassess the longer-term syndrome after recovery.')],
 [S('Acute Attention and Awareness Disturbance', '**Delirium** has acute onset and a fluctuating course, with impaired attention and altered awareness/cognition. Hypoactive disease with drowsiness can be missed when there is no agitation.',
    'An established dementia increases vulnerability and does not explain away the new change. Obtain baseline information from family or records and look for pain, infection, hypoxia, dehydration, retention, constipation and drug effects.',
    'NICE recommends a 4AT assessment in the appropriate general hospital/long-term-care setting when delirium indicators occur. In critical care or postoperative recovery, use CAM-ICU or ICDSC as appropriate.'),
  S('Management Priorities', '**Treat the precipitant and provide supportive care**: orientation, glasses/hearing aids, sleep protection, mobility, hydration and appropriate analgesia. Use a calm environment and familiar support where feasible.',
    'Antipsychotics are not a routine cure and can be hazardous, particularly with Lewy body disease or parkinsonism. Reserve medication for an appropriate severe-distress or safety indication after nonpharmacological measures and risk review.',
    'When delirium and dementia are difficult to distinguish, NICE advises managing delirium first. Recovery can be prolonged; reassessment is needed before assigning a durable new cognitive baseline.')], ['DEL','DETECT'])

add('Cognitive syndrome assessment', 'Depression and Cognitive Symptoms Can Coexist',
 'A 68-year-old with depression reports marked forgetfulness. Testing is variable, but an informant describes progressive navigation errors beginning before the mood episode. Which approach is most appropriate?',
 'Treat and assess the depression while continuing an objective cognitive and etiologic evaluation', [
 ('Exclude neurodegeneration because the patient is distressed by the memory problem', 'Concern about deficits is common in depression but can also occur early in neurodegenerative disease; insight and distress are not exclusion tests.'),
 ('Diagnose irreversible dementia from poor effort on one brief test', 'Variable engagement can reflect mood, fatigue, sensory or language issues; one test does not establish irreversible pathology or the cause of impairment.'),
 ('Defer all cognitive follow-up once an antidepressant is prescribed', 'Mood treatment is appropriate, but persistent or progressive objective deficits and informant-reported decline require follow-up even if depression improves.')],
 [S('Overlapping Presentations', '**Depression can impair attention, processing speed, executive function and memory performance**, and can coexist with or precede a neurodegenerative disorder.',
    'A shorthand label of pseudodementia should not imply that all cognitive symptoms are nonorganic or guaranteed to reverse. Assess the time course and objective everyday function.',
    'Ask about sleep, appetite, anhedonia, psychomotor change, medications and suicidal thinking, while obtaining collateral history of navigation, finances, medicines and other complex tasks.'),
  S('Parallel Assessment and Reassessment', '**Treat clinically significant mood illness and evaluate cognition in parallel.** Use an appropriate cognitive assessment, neurological examination, basic laboratory workup and structural imaging when indicated.',
    'Correct sensory barriers and review sedating or anticholinergic drugs before interpreting poor performance. Formal neuropsychological testing may clarify a persistent mismatch between history and screening.',
    'Improvement with mood treatment is informative but not a definitive biomarker. Continued decline, focal cognitive patterns or progressive loss of independence justify reassessment for Alzheimer, vascular, Lewy body and other etiologies.')], ['DETECT','NICE'])

add('Cognitive syndrome assessment', 'A Screening Score Is Not the Whole Diagnosis',
 'A bilingual older adult with hearing impairment scores poorly on an English-language cognitive screen but manages complex activities independently. Which next step is most appropriate?',
 'Reassess with sensory and language accommodations and interpret domain performance against the clinical history', [
 ('Diagnose dementia from the numerical score alone', 'A screening score is affected by language, education and sensory access; it cannot replace objective decline and functional assessment.'),
 ('Exclude cognitive disease because instrumental activities are still independent', 'Preserved independence argues against a major syndrome but does not exclude MCI or an early disease process requiring evaluation.'),
 ('Use amyloid imaging before establishing whether the test result reflects a valid cognitive deficit', 'Biomarkers may answer selected etiologic questions, but the first issue is whether assessment was valid and whether an objective syndrome is present.')],
 [S('Valid Measurement', '**Language, education, premorbid ability, hearing, vision and motor demands** influence cognitive-screen performance. Use validated translated instruments or a suitable interpreter-based strategy and sensory aids where available.',
    'Interpret memory, attention, executive, language and visuospatial findings as a profile. A low total score can conceal a specific barrier or a genuinely focal deficit.',
    'Brief tests identify concern and guide further assessment; they do not alone distinguish all etiologies or define capacity.'),
  S('Clinical Integration', '**Patient and informant histories** establish change from baseline and its effect on daily life. Compare the pattern with occupational and educational background rather than assuming a population cutoff fits every individual.',
    'Formal neuropsychological evaluation is useful when a high premorbid baseline, atypical language profile or confounded screening creates uncertainty. Repeat assessment can document a trajectory.',
    'A negative screen can also miss early focal disease. Persistent informant concern, progressive navigation errors, language change or behavioral deterioration deserves proportionate evaluation even when a brief total score is reassuring.')], ['DETECT'])

add('Cognitive syndrome assessment', 'Initial Investigation of Cognitive Decline',
 'An adult has a newly recognized progressive cognitive–behavioral syndrome. There is no immediate encephalitic or focal emergency. Which initial investigation strategy is most appropriate?',
 'A basic cognitive laboratory panel and structural brain imaging, followed by phenotype-directed specialized tests', [
 ('An indiscriminate neuronal-antibody panel as the only initial investigation', 'Autoimmune testing is important for compatible rapid or inflammatory presentations, but broad low-pretest-probability panels can mislead and do not replace basic assessment.'),
 ('Amyloid PET for every patient before medication, metabolic or structural review', 'Amyloid PET can help selected etiologic or treatment decisions, but should follow clinical formulation and does not replace evaluation of treatable contributors or structural disease.'),
 ('Serial screening scores alone without laboratory or imaging assessment', 'Longitudinal cognition is useful, but cannot reliably detect metabolic, medication-related or structural causes that may alter management.')],
 [S('Tiered Evaluation', '**DETeCD-ADRD recommends a Tier 1 cognitive laboratory panel and structural imaging in almost all appropriately assessed patients.** A practical panel includes CBC, electrolytes/glucose, renal and hepatic function, calcium, TSH and B12, with additional specified components in the guideline.',
    'The guideline’s full Tier 1 panel also includes magnesium, homocysteine, ESR and CRP. Local protocols and individual risks affect testing; abnormalities require clinical interpretation rather than automatic attribution of the entire syndrome.',
    'Brain MRI without contrast is preferred when feasible; CT is an alternative when MRI is unavailable or contraindicated.'),
  S('What Imaging and Targeted Tests Add', '**Structural imaging** assesses atrophy patterns, infarcts, hemorrhagic markers, hydrocephalus, masses and other competing causes. Mild age-associated findings do not necessarily explain severe impairment.',
    'Select HIV/syphilis tests, sleep evaluation, CSF, EEG, autoimmune studies, genetic testing or molecular biomarkers according to phenotype, tempo, exposure and the management question.',
    'An acute/subacute course, seizures, focal findings or rapidly progressive decline requires an expedited pathway rather than a routine chronic-dementia workup. The final formulation should allow mixed contributors rather than forcing one cause from a single abnormal test.')], ['DETECT','NICE'])

R.update({
 'PCA': ('Consensus classification of posterior cortical atrophy, 2017', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5788455/'),
 'GEN': ('NIA Alzheimer disease genetics fact sheet', 'https://www.nia.nih.gov/health/alzheimers-disease-genetics-fact-sheet'),
 'PET': ('Alzheimer Association/SNMMI amyloid and tau PET appropriate-use criteria, 2025', 'https://doi.org/10.1002/alz.14338'),
 'DONE': ('Donepezil prescribing information, updated 2026', 'https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=76bf638e-dbde-418e-8977-1caf009990bc'),
 'MEM': ('Memantine immediate-release prescribing information, 2026', 'https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=f73e0df0-4af4-42f1-bde6-3cccb47ca378'),
 'LEC': ('Lecanemab US prescribing information, July 2026 revision', 'https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/761375s001lbl.pdf'),
 'DON': ('Donanemab US prescribing information, July 2025 dose revision', 'https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/761248s004lbl.pdf'),
})

add('Alzheimer disease', 'A Progressive Amnestic Alzheimer Syndrome',
 'A 74-year-old has three years of insidious progressive forgetting, repetitive questions and impaired retention of newly learned material despite cueing. Later, navigation and complex-task performance decline. There are no early hallucinations, focal strokes or prominent behavioral change. Which clinical syndrome is most likely?',
 'A typical amnestic Alzheimer clinical syndrome', [
 ('Behavioral-variant frontotemporal dementia', 'bvFTD is more often led by early behavioral/social-cognitive change, disinhibition or stereotyped behavior; the dominant progressive storage-type memory pattern is more typical of AD.'),
 ('Dementia with Lewy bodies', 'DLB can impair memory, but early attention/visuoperceptual dysfunction, cognitive fluctuations, formed hallucinations, RBD or parkinsonism would be stronger clues than this predominantly amnestic trajectory.'),
 ('A purely strategic-infarct cognitive syndrome', 'A strategic infarct can impair memory, but often has an abrupt onset or corresponding focal imaging/history; the gradual multidomain evolution here favors an Alzheimer clinical pattern.')],
 [S('Clinical Pattern', '**Typical symptomatic AD often begins with episodic-memory impairment**, particularly inefficient learning and retention, followed by broader language, executive or visuospatial decline.',
    'A storage-type deficit with poor delayed recall and limited cueing benefit is informative, but no single memory pattern proves amyloid and tau pathology.',
    'Collateral history, objective testing and functional assessment establish severity. MRI may show medial temporal and temporoparietal atrophy, but can be nondiagnostic early.'),
  S('Etiologic Confidence', '**A clinical Alzheimer syndrome and biological AD are related but distinct formulations.** Molecular biomarkers can establish AD pathology when clinically appropriate and can alter confidence or treatment eligibility.',
    'Mixed vascular, Lewy body or other pathology is common in older adults. Do not ignore a substantial additional contributor because one feature resembles typical AD.',
    'Assess medications, systemic contributors, mood, sleep, sensory function and safety. Symptomatic therapies and selected anti-amyloid treatments have different eligibility, monitoring and expected benefits; neither a clinical label nor an atrophy pattern alone determines one universal regimen.')], ['DETECT','AD24'])

add('Alzheimer disease', 'Posterior Cortical Atrophy',
 'A 59-year-old has progressive difficulty reading, locating objects and judging spatial relationships despite adequate ocular acuity. Examination shows simultanagnosia and visuoconstructional impairment with relatively preserved early verbal memory. Which syndrome best fits?',
 'Posterior cortical atrophy', [
 ('Semantic-variant primary progressive aphasia', 'Semantic PPA primarily impairs naming and single-word/object meaning with anterior temporal involvement; visual-spatial processing failure is not its defining initial pattern.'),
 ('Typical amnestic MCI', 'MCI can have nonamnestic profiles, but calling this typical amnestic disease misses the dominant progressive posterior visual-cognitive syndrome.'),
 ('A primary ocular disorder as the sufficient explanation', 'Ocular disease must be excluded, but adequate acuity with simultanagnosia and higher-order visuospatial dysfunction indicates a cortical processing problem rather than an acuity-only disorder.')],
 [S('Higher-Order Visual Syndrome', '**Posterior cortical atrophy** is a progressive syndrome dominated by posterior visual and spatial dysfunction. Features can include simultanagnosia, optic ataxia, ocular apraxia, alexia, acalculia and visuoconstructional failure.',
    'Early relative preservation of memory, nonvisual language and behavior can contrast with typical amnestic AD. Visual complaints may initially lead to repeated ophthalmic assessments.',
    'MRI or functional imaging can show occipitoparietal or occipitotemporal involvement, but clinical assessment must exclude a primary ocular, vascular or mass-lesion explanation.'),
  S('Syndrome and Underlying Disease', '**AD is the most common underlying pathology**, but PCA is not synonymous with biomarker-proven AD. Lewy body, corticobasal and other causes can produce related presentations.',
    'Use appropriate molecular testing when the result will resolve etiology or guide therapy. A visual-led syndrome should not be excluded from an AD discussion solely because early memory is relatively preserved.',
    'Address reading, navigation, falls, environmental contrast, occupational needs and driving safety. Treatment eligibility depends on confirmed disease, clinical stage and safety assessment rather than the syndrome name alone.')], ['PCA','AD24'])

add('Alzheimer disease', 'Familial Alzheimer Genes and APOE',
 'A 46-year-old has a progressive Alzheimer-like syndrome, with an affected parent and grandparent at similarly young ages. Which genetic assessment best addresses a possible highly penetrant dominant cause?',
 'Counselled evaluation of APP, PSEN1 and PSEN2', [
 ('APOE genotyping as a stand-alone deterministic diagnostic test', 'APOE modifies susceptibility and anti-amyloid ARIA risk but does not provide the same deterministic familial-cause interpretation as a confirmed pathogenic APP/PSEN variant.'),
 ('HTT testing as the default explanation of every dominant dementia pedigree', 'HTT testing is relevant when the phenotype suggests Huntington disease, such as chorea with cognitive/behavioral change, rather than automatically replacing Alzheimer-gene evaluation.'),
 ('C9orf72 testing as the only relevant gene regardless of the clinical phenotype', 'C9orf72 is important for FTD/ALS pedigrees; the young-onset Alzheimer-like pattern supports considering AD genes while allowing phenotype-directed broader testing.')],
 [S('High-Penetrance Familial Disease', '**Pathogenic variants in APP, PSEN1 or PSEN2** can cause autosomal dominant AD. A young onset and multigenerational pedigree raise suspicion but do not identify the specific gene.',
    'Obtain a detailed pedigree, confirm relatives’ diagnoses when feasible and test an affected person first when possible. Variant classification and phenotype concordance matter.',
    'Predictive testing of an asymptomatic relative requires dedicated genetic counselling and consent rather than casual inclusion in a general laboratory panel.'),
  S('Susceptibility and Treatment Risk', '**APOE ε4 increases AD risk and is associated with greater ARIA risk during anti-amyloid treatment**, particularly in homozygotes. It does not by itself diagnose symptomatic AD or predict an exact onset age.',
    'Emerging descriptions of ε4 homozygosity as a strong biological risk state should not be conflated with every carrier having the same clinical course or with a conventional monogenic pedigree.',
    'Discuss psychological, family and reproductive implications and the purpose of testing. An anti-amyloid safety-genotype result and an etiologic predictive-family test answer different questions.')], ['GEN','LEC'])

add('Alzheimer disease', 'The 2024 Biological Alzheimer Framework',
 'Under the 2024 Alzheimer Association revised criteria, which statement is most accurate?',
 'An abnormal validated Core 1 biomarker can establish biological AD, while clinical impairment is staged separately', [
 ('Biological AD can be diagnosed only after independence is lost', 'The framework permits a biological diagnosis before dementia; functional loss determines clinical stage rather than the first possible presence of AD pathology.'),
 ('A hippocampal atrophy pattern alone is a specific Core 1 amyloid/tau marker', 'Atrophy is a neurodegeneration marker and is not specific enough to substitute for the specified molecular Core 1 evidence.'),
 ('The criteria recommend routine AD biomarker screening for all asymptomatic adults', 'The biological definition does not amount to a general screening recommendation; routine clinical testing of cognitively unimpaired people is not supported outside the specified research context.')],
 [S('Molecular Diagnosis and Clinical Expression', '**Core 1 biomarkers** include validated amyloid PET, specified CSF amyloid/tau measures and sufficiently accurate plasma assays. An abnormal qualifying result can establish AD within the 2024 biological framework.',
    'Clinical stage is assessed independently. Biological disease can be present without objective impairment, with MCI-level impairment or with dementia-level functional loss.',
    'Later-changing Core 2 measures, including tau-related measures in specified contexts, can refine biological staging and prognosis; nonspecific injury markers are not equivalent to AD-specific molecular evidence.'),
  S('Clinical Use and Boundaries', '**A biological definition is not a universal screening or treatment policy.** The criteria do not recommend clinical biomarker testing of cognitively unimpaired individuals outside research in the absence of an applicable clinical indication.',
    'A positive biomarker does not prove that AD is the only cause of symptoms. Vascular injury, Lewy body pathology, depression, drugs and other disease may contribute.',
    'Identify the criteria version and the test’s analytical/clinical validation. Do not apply thresholds from one assay to another or assume every commercial plasma test meets the required accuracy.')], ['AD24','BBM25'], style='direct')

add('Alzheimer disease', 'Interpreting CSF Alzheimer Biomarkers',
 'A specialist evaluates a progressive cognitive syndrome. Which CSF pattern most strongly supports AD pathology when measured by a validated assay?',
 'A reduced Aβ42/Aβ40 ratio with an abnormal phosphorylated-tau/amyloid profile', [
 ('Isolated elevated total tau with a normal amyloid ratio as definitive AD proof', 'Total tau can reflect neuronal injury in several disorders, including rapidly destructive processes; isolated elevation is not specific proof of AD pathology.'),
 ('Normal amyloid measures with isolated CSF protein elevation', 'Protein elevation has a broad differential and is not the characteristic molecular amyloid/tau pattern used to support AD.'),
 ('CSF-restricted oligoclonal bands as the defining Alzheimer biomarker', 'Oligoclonal bands indicate intrathecal immune activity in appropriate contexts and do not replace the AD-specific molecular biomarker framework.')],
 [S('Amyloid and Tau Relationships', '**Aβ42/Aβ40 ratio and validated tau/amyloid ratios** improve interpretation compared with an isolated raw analyte concentration. Reduced soluble amyloid ratio is associated with cerebral amyloid pathology.',
    'Specified CSF ratios are accepted Core 1 measures in the 2024 framework. The exact threshold depends on the assay, laboratory validation and preanalytical handling.',
    'Do not invent one universal numerical cutoff for all platforms or substitute a nonspecific protein/injury measure for an AD-specific result.'),
  S('Limits and Competing Causes', '**Biomarkers complement clinical assessment**, including tempo, cognitive profile, imaging and other CSF findings when indicated. Discordant results deserve review rather than forced interpretation.',
    'A high total tau alone can occur with acute injury or prion disease; pleocytosis, substantial barrier abnormalities or infectious clues require their own evaluation.',
    'A positive AD profile can coexist with other pathology. Before disease-specific treatment, establish clinical stage, capacity for monitoring and the relevant medication safety criteria rather than treating a biomarker as an automatic prescription.')], ['AD24','DETECT'], style='direct')

add('Alzheimer disease', 'Blood Biomarker Triage Versus Confirmation',
 'A plasma AD test is validated in cognitively impaired specialty-clinic patients with 93% sensitivity and 80% specificity against an accepted reference. Which use fits the 2025 Alzheimer Association guideline?',
 'A triage role, with positive results requiring appropriate confirmatory evaluation', [
 ('A stand-alone confirmatory substitute solely because sensitivity exceeds 90%', 'The confirmatory framework requires both sensitivity and specificity of at least 90%; 80% specificity does not meet that stated threshold.'),
 ('Population screening of cognitively unimpaired adults without further assessment', 'The guideline addresses objectively cognitively impaired patients in specialized care, not unrestricted asymptomatic population screening.'),
 ('A definitive explanation for every symptom regardless of pretest probability', 'Positive predictive value depends on prevalence and context, and an AD biomarker cannot exclude coexisting causes of cognitive impairment.')],
 [S('Performance-Based Recommendations', '**The 2025 specialty-care guideline** supports a triage test with at least 90% sensitivity and at least 75% specificity. A positive triage result is followed by an appropriate confirmatory pathway.',
    'For use as a substitute for amyloid PET or CSF testing, the guideline specifies at least 90% sensitivity and at least 90% specificity in the relevant clinical population.',
    'These are clinical performance requirements, not a statement that every p-tau assay or every commercial blood panel meets them.'),
  S('Assay and Population Matter', '**Use a validated assay and interpretation protocol**, including how indeterminate results are handled. Values and cutoffs are platform specific.',
    'Clinical evaluation remains necessary before testing. Renal disease and other comorbidities can affect some plasma measures, and real-world performance may differ from a selected research cohort.',
    'Discuss the result in terms of the management question and pretest probability. A high-quality biomarker can reduce diagnostic uncertainty but does not by itself determine dementia severity, exclude mixed disease or establish treatment safety.')], ['BBM25'], style='direct', table=(['Use in the specified specialty population','Minimum sensitivity','Minimum specificity','Positive result'],[
 ['Triage','90%','75%','Follow with confirmation'],['Confirmatory substitute','90%','90%','Interpret within the full diagnostic evaluation']]))

add('Alzheimer disease', 'When Amyloid PET Can Change Management',
 'A 61-year-old has progressive language-led cognitive impairment with uncertain etiology after specialist assessment and structural imaging. Establishing AD pathology would alter counselling and possible treatment eligibility. Which use of amyloid PET is most appropriate?',
 'Use it to help resolve the clinically consequential etiologic uncertainty', [
 ('Use it only after severe dementia because early symptomatic disease cannot be assessed', 'Amyloid PET can be useful in appropriate early symptomatic or atypical presentations; requiring severe dementia would miss relevant diagnostic and treatment decisions.'),
 ('Use a positive scan to prove that all impairment is caused exclusively by AD', 'Amyloid positivity supports amyloid pathology but does not exclude other contributing disease or establish that every symptom is attributable to it.'),
 ('Repeat it routinely to track every short-term memory fluctuation', 'Amyloid PET is not a routine short-term symptom-monitoring test. Selected treatment protocols may use plaque burden for a defined decision, which is different from repeated scanning for daily fluctuations.')],
 [S('Appropriate-Use Question', '**The 2025 amyloid/tau PET appropriate-use criteria** emphasize a specialist-led clinical question in which molecular clarification can affect diagnosis, counselling or treatment.',
    'Young-onset, atypical or mixed cognitive syndromes and assessment for relevant amyloid-targeting treatment can be appropriate contexts after a clinical evaluation.',
    'A scan is not a replacement for history, cognitive testing, medication review, laboratory workup or structural imaging.'),
  S('Positive and Negative Results', '**A negative amyloid study makes AD amyloid pathology much less likely as the explanation**, while a positive study establishes amyloid burden that must be interpreted with age and phenotype.',
    'Amyloid positivity becomes more common with age and can coexist with Lewy body or vascular disease. Tau imaging and other evidence may answer different staging or causal questions.',
    'Explain potential diagnostic reclassification before testing. The clinical value is resolution of a decision, not the assumption that more imaging is always better or that plaque burden directly measures daily function.')], ['PET','AD24'])

add('Alzheimer disease', 'Starting Donepezil for Symptomatic AD',
 'An adult with mild Alzheimer dementia has no symptomatic bradycardia and wishes to try symptomatic medication. Which donepezil regimen is appropriate?',
 'Start 5 mg once daily and consider 10 mg daily after at least four to six weeks if tolerated', [
 ('Start 10 mg twice daily immediately to obtain a faster cognitive response', 'Rapid high-dose initiation increases cholinergic toxicity and does not match the labeled gradual once-daily titration.'),
 ('Start memantine solely because every mild case requires it before a cholinesterase inhibitor', 'Memantine is mainly used for moderate-to-severe AD or specified intolerance/combination contexts, not as a universal prerequisite in mild disease.'),
 ('Use donepezil as a proven plaque-clearing disease-modifying treatment', 'Donepezil provides symptomatic cholinergic treatment; it is not an amyloid-clearing antibody or a proven cure for the underlying neurodegenerative process.')],
 [S('Symptomatic Cholinergic Therapy', '**Donepezil inhibits acetylcholinesterase** and is an option for symptomatic AD. NICE lists donepezil, galantamine and rivastigmine for mild-to-moderate AD under appropriate conditions.',
    'The usual initiation is ==5 mg once daily==, with an increase to ==10 mg once daily after four to six weeks== if tolerated. Further formulation-specific options are not a reason to bypass initial titration.',
    'Discuss modest average benefit and individual variability. Use functional and caregiver observations alongside cognition to assess whether treatment is worthwhile.'),
  S('Monitoring and Alternatives', '**Nausea, diarrhea, anorexia/weight loss, sleep disturbance and bradycardia** are relevant adverse effects. Review pulse, syncope, conduction disease, interacting rate-slowing drugs and weight.',
    'Rivastigmine patch can help selected patients with oral tolerability or administration difficulties, but patch dosing and titration are product specific and old patches must be removed.',
    'A decline despite treatment does not automatically mean there was no symptomatic benefit; review tolerability, goals and the overall trajectory rather than promising stabilization or stopping solely at a numerical severity boundary.')], ['DONE','NICE'])

add('Alzheimer disease', 'Syncope During Cholinesterase-Inhibitor Treatment',
 'A patient taking donepezil develops recurrent presyncope with pulse 42/min after a dose increase. He also takes a beta-blocker. Which response is most appropriate?',
 'Assess bradyarrhythmia and medication contributions promptly, including withholding or reducing relevant drugs as clinically indicated', [
 ('Escalate donepezil because dizziness proves inadequate cholinergic stimulation', 'Cholinesterase inhibition can increase vagal effects and cause bradycardia or block; further escalation could worsen the suspected adverse effect.'),
 ('Assume all syncope is progression of dementia and omit cardiac assessment', 'Syncope requires a medical evaluation; conduction disease and medication effects can be treatable and should not be attributed to cognitive decline alone.'),
 ('Switch immediately to another cholinesterase inhibitor without considering a class effect', 'A different formulation may improve gastrointestinal tolerability, but bradycardia can be a class-related effect; switching alone does not resolve the cardiac safety question.')],
 [S('Vagotonic Cardiac Effects', '**Cholinesterase inhibitors can slow sinoatrial and AV nodal conduction**, with bradycardia, block and syncope even when prior conduction disease is not documented.',
    'Review ECG, pulse, orthostatic measurements, electrolytes and competing causes according to urgency. Beta-blockers and other rate-slowing agents can increase concern.',
    'Symptomatic severe bradycardia warrants prompt clinical management, not merely a routine cognitive follow-up appointment.'),
  S('Treatment Reassessment', '**Balance symptomatic cognitive benefit against harm.** Holding or reducing a suspected medication and reviewing the full regimen may be appropriate while the cardiac problem is evaluated.',
    'Other cholinergic effects include gastrointestinal symptoms, weight loss, urinary symptoms and sleep disturbance; perioperative interactions with neuromuscular blockers also matter.',
    'If a cholinesterase inhibitor is not tolerated, alternative cognitive treatment depends on diagnosis and severity. Memantine may fit a moderate-to-severe AD context, but it is not an automatic substitute for every mild-stage patient or every non-AD syndrome.')], ['DONE','NICE'])

add('Alzheimer disease', 'Memantine and Severe Renal Impairment',
 'An adult with moderate-to-severe AD is prescribed immediate-release memantine. Cockcroft–Gault creatinine clearance is 22 mL/min. Which target dose matches the US label?',
 '5 mg twice daily', [
 ('10 mg twice daily', 'This is the usual full immediate-release target in patients without the specified severe renal limitation; the label recommends a lower target at clearance 5–29 mL/min.'),
 ('28 mg once daily of the immediate-release formulation', 'Twenty-eight milligrams once daily is associated with a different extended-release regimen; formulation and renal adjustments must not be mixed.'),
 ('20 mg twice daily', 'This exceeds the usual immediate-release labeled target and would add unnecessary exposure, particularly with severe renal impairment.')],
 [S('NMDA-Receptor Modulation', '**Memantine is an uncompetitive NMDA-receptor antagonist** used for symptomatic moderate-to-severe AD. NICE also uses it in specified moderate-stage cholinesterase-intolerance and combination contexts.',
    'Immediate-release treatment usually starts at ==5 mg once daily== and increases in weekly 5-mg steps to a usual maximum of ==10 mg twice daily== when appropriate.',
    'For creatinine clearance ==5–29 mL/min==, the immediate-release target is ==5 mg twice daily==. Use the Cockcroft–Gault-based label instruction rather than assuming every reported eGFR is interchangeable.'),
  S('Tolerability and Prescribing Details', '**Dizziness, confusion, constipation and headache** are relevant adverse effects. Review falls, adherence and whether symptoms reflect the drug or disease.',
    'Urine alkalinization can reduce elimination, and concurrent NMDA antagonists such as amantadine or ketamine require caution. Extended-release products have their own initiation and renal regimen.',
    'The drug is symptomatic rather than a cure and should not be prescribed for every MCI or non-AD cognitive complaint. Assess the underlying diagnosis, stage, function and patient/caregiver goals before and during treatment.')], ['MEM','NICE'], style='direct')

R['CLARITY'] = ('CLARITY AD randomized trial of lecanemab, 2023', 'https://www.nejm.org/doi/10.1056/NEJMoa2212948')
R['TRAIL'] = ('TRAILBLAZER-ALZ 2 randomized trial of donanemab, 2023', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC10352931/')

add('Alzheimer disease', 'Selecting an Early Symptomatic Anti-Amyloid Candidate',
 'Which patient most closely matches the population in whom lecanemab treatment is initiated under the current US label, assuming a complete favorable safety and monitoring assessment?',
 'A patient with MCI due to AD and confirmed amyloid pathology', [
 ('A cognitively unimpaired APOE ε4 carrier without evidence of amyloid pathology', 'Susceptibility genotype alone does not establish the required symptomatic stage or amyloid confirmation; asymptomatic prevention is a different research question.'),
 ('A patient with severe dementia who has never had amyloid confirmation', 'The initiation population is MCI or mild dementia with confirmed amyloid pathology, not unconfirmed advanced dementia.'),
 ('A patient with a typical frontotemporal syndrome and a negative amyloid evaluation', 'A non-AD syndrome without amyloid pathology does not match the disease-specific mechanism or the required confirmation.')],
 [S('Clinical and Biological Eligibility', '**Anti-amyloid treatment initiation requires early symptomatic AD**, specifically MCI or mild dementia in the cited US labels, with amyloid pathology confirmed before treatment.',
    'A clinical memory complaint, susceptibility genotype or atrophy pattern alone is insufficient. Establish the cognitive syndrome, function and disease-specific evidence.',
    'Labels, appropriate-use recommendations, trial enrollment rules and reimbursement policies are different documents and can impose different boundaries.'),
  S('Benefit, Risk and Feasibility', '**Review baseline MRI, hemorrhagic markers, APOE genotype implications, anticoagulants and capacity for repeated monitoring.** Greater cerebral amyloid angiopathy burden or anticoagulant exposure can substantially increase concern; a label warning should not be casually rewritten as an identical universal absolute contraindication.',
    'In CLARITY AD, the 18-month CDR-SB change was 1.21 with lecanemab versus 1.66 with placebo, an absolute between-group difference of 0.45 points. Both groups declined on average.',
    'Discuss modest slowing, ARIA/hemorrhage risk, treatment burden, uncertainty and local availability. Shared decisions should include the patient’s goals and support system rather than portraying eligibility as an obligation to receive treatment.')], ['LEC','CLARITY'])

add('Alzheimer disease', 'Lecanemab Dosing and MRI: July 2026 US Label',
 'Under the July 2026 US lecanemab label, which scheduled MRI surveillance plan accompanies a recent baseline MRI during early treatment?',
 'MRI after months 1, 2, 3 and 6, with additional evaluation for suspected ARIA', [
 ('MRI only when neurological symptoms develop', 'ARIA is often asymptomatic, so scheduled surveillance is required in addition to symptom-triggered evaluation.'),
 ('A single MRI at month 18 before considering maintenance therapy', 'This would miss the early period when ARIA is particularly important; maintenance decisions do not replace early safety surveillance.'),
 ('Annual CT alone in place of MRI surveillance', 'CT does not provide the required sensitivity and sequence-based evaluation for the scheduled ARIA monitoring specified in the label.')],
 [S('Version-Specific Schedule', '**The July 2026 US label specifies MRI after one, two, three and six months**, following a recent baseline MRI. Images should generally be obtained within about one week before the next scheduled dose and reviewed before proceeding.',
    'At the one-month point, the label gives examples of before the third IV dose or fifth subcutaneous dose. Older infusion-number schedules should not be treated as an unchanged universal rule across routes and label versions.',
    'New headache, confusion, visual symptoms, focal deficits, gait difficulty or seizures require prompt clinical assessment and appropriate MRI rather than waiting for the next planned scan.'),
  S('Starting and Maintenance Regimens', '**Starting treatment** is IV 10 mg/kg every two weeks or subcutaneous 500 mg weekly under this specific US revision. The subcutaneous starting dose uses the appropriate autoinjector presentation and instructions.',
    'After eighteen months, treatment may continue at the starting regimen or transition to IV 10 mg/kg every four weeks or subcutaneous 360 mg weekly maintenance. Starting and maintenance subcutaneous doses are different.',
    'Switching route, missed doses and ARIA-related interruptions require the full product-specific protocol. These regimens do not imply identical approval, access or monitoring arrangements in every country.')], ['LEC'], style='direct', table=(['Phase','IV regimen','Subcutaneous regimen, July 2026 US label'],[
 ['Starting','10 mg/kg every 2 weeks','500 mg weekly'],['Maintenance after 18 months','10 mg/kg every 4 weeks','360 mg weekly'],['Early MRI surveillance','Baseline; months 1, 2, 3, 6','Baseline; months 1, 2, 3, 6']]))

add('Alzheimer disease', 'ARIA Can Mimic Ischemic Stroke',
 'A lecanemab-treated patient develops headache, confusion and a focal neurological deficit. MRI demonstrates new vasogenic edema and several new microhemorrhages. Which interpretation is most likely?',
 'Amyloid-related imaging abnormalities with edema and hemorrhagic features', [
 ('Typical AD progression as the sufficient explanation', 'AD progression does not ordinarily cause an abrupt focal deficit with new vasogenic edema and hemorrhagic MRI changes; a treatment complication requires urgent evaluation.'),
 ('An ischemic event proven solely by the focal deficit', 'Focal deficits require a stroke assessment, but ARIA can mimic ischemia. The anti-amyloid exposure and edema/microhemorrhage pattern change the immediate differential and thrombolysis risk assessment.'),
 ('A benign infusion reaction that requires no imaging-based treatment review', 'Infusion reactions can occur, but the demonstrated cerebral edema and new hemorrhagic markers require ARIA-specific severity assessment rather than dismissal as a transient systemic reaction.')],
 [S('Imaging Categories', '**ARIA-E** denotes edema or sulcal effusion, while **ARIA-H** includes microhemorrhages and superficial siderosis. The two can coexist and may be asymptomatic or cause serious neurological illness.',
    'Risk is higher in APOE ε4 homozygotes and with relevant baseline hemorrhagic/CAA markers. Counsel about genotype-related risk and the implications of testing before treatment.',
    'Headache, confusion, visual change, dizziness, gait disturbance, seizures and focal deficits are possible manifestations. Urgent evaluation must also consider true stroke and other causes.'),
  S('Treatment Interruption and Emergency Care', '**Suspend or modify treatment according to symptoms and MRI severity.** The lecanemab label permits continuation in selected mild/asymptomatic circumstances but requires suspension in more severe combinations; the full table guides decisions.',
    'Consider follow-up MRI, seizure assessment and hospital-level care for significant symptoms. Severe inflammatory ARIA may require specialist-directed treatment beyond a simple dose delay.',
    'Before thrombolysis, clinicians must consider whether a stroke-like deficit could be ARIA; fatal hemorrhage has occurred with this drug class. Anticoagulant and antiplatelet decisions require individualized expert review rather than assuming the usual acute-stroke pathway is unaffected.')], ['LEC','DON'])

add('Alzheimer disease', 'Donanemab: Benefit and Current Escalation',
 'Which statement correctly describes the current US donanemab dosing schedule introduced in July 2025?',
 'Monthly IV doses escalate through 350, 700 and 1050 mg, then 1400 mg from the fourth infusion onward', [
 ('Every monthly infusion is 700 mg with no escalation', 'A 700-mg dose appeared in the original regimen, but the updated US schedule uses staged escalation to 1400 mg rather than a fixed 700-mg course.'),
 ('It uses the same weekly subcutaneous starting schedule as lecanemab', 'Donanemab is administered intravenously every four weeks under this label; lecanemab’s product-specific subcutaneous regimen is not interchangeable.'),
 ('Plaque clearance proves that established dementia has been reversed', 'Amyloid reduction and slower clinical decline are not equivalent to reversal or cure; trial participants still declined on average.')],
 [S('Administration and Monitoring', '**The revised US sequence is 350 mg, 700 mg, 1050 mg and then 1400 mg every four weeks**, infused over approximately thirty minutes. Confirm amyloid pathology and obtain a recent baseline MRI.',
    'Scheduled MRI is required before the second, third, fourth and seventh infusions, with additional assessment for symptoms suggestive of ARIA. APOE ε4-related risk and hemorrhagic safety issues require counselling.',
    'The label allows consideration of stopping based on reduction of amyloid plaques to minimal levels on amyloid PET. This is a defined treatment decision, not proof that the underlying clinical syndrome is cured.'),
  S('Trial Interpretation', '**TRAILBLAZER-ALZ 2** showed a 3.25-point between-group difference in iADRS decline at 76 weeks in the low/medium-tau population, reported as 35.1% slowing.',
    'That relative percentage depends on the population, endpoint and follow-up. It should not be used as a direct head-to-head superiority claim against lecanemab or translated into a guaranteed individual benefit.',
    'Both drug and placebo groups declined on average, and ARIA and serious adverse events matter in the benefit–risk decision. Distinguish the original trial regimen from later dose modifications intended to improve tolerability.')], ['DON','TRAIL'], style='direct')

add('Lewy body cognitive disorders', 'Probable Dementia with Lewy Bodies',
 'A patient with dementia has recurrent detailed visual hallucinations and marked fluctuations of attention and alertness. No biomarker study has yet been obtained. Under the 2017 DLB criteria, which category is supported?',
 'Probable DLB on the basis of two core clinical features', [
 ('Possible DLB only, because a dopamine-transporter scan is mandatory', 'Two core clinical features can support probable DLB without an indicative biomarker; DAT imaging is not mandatory in every case.'),
 ('Definite DLB pathology proven by hallucinations alone', 'The clinical criteria establish a probability category, not neuropathological proof; hallucinations also have medication, ophthalmic and other neurological causes.'),
 ('Typical AD as the only diagnosis because memory decline occurred', 'AD and mixed pathology remain possible, but early fluctuations and recurrent formed hallucinations are core DLB features and should not be ignored.')],
 [S('Core Clinical Features', '**DLB requires a dementia syndrome**, often with early attention, executive and visuoperceptual impairment. Prominent amnesia may emerge later and is not required as the first symptom.',
    'The four core features are fluctuating cognition/alertness, recurrent well-formed visual hallucinations, REM sleep behavior disorder and spontaneous parkinsonism.',
    'Probable DLB is supported by two or more core features, or one core feature plus at least one indicative biomarker. Possible DLB can be supported by one core feature alone, or an indicative biomarker without a core feature.'),
  S('Assess Mimics and Co-pathology', '**Exclude delirium and medication effects** when fluctuations or hallucinations arise acutely. RBD history may need polysomnographic confirmation when the account is uncertain.',
    'AD and Lewy body pathology frequently coexist, so an AD biomarker does not automatically invalidate a convincing DLB clinical syndrome.',
    'The diagnosis affects antipsychotic sensitivity, autonomic and sleep assessment, falls and cognitive treatment. Document the exact supporting features rather than treating every hallucinating older patient as DLB.')], ['DLB'])

add('Lewy body cognitive disorders', 'Indicative Versus Supportive DLB Biomarkers',
 'Which finding is an indicative biomarker in the 2017 DLB diagnostic framework?',
 'Polysomnographic confirmation of REM sleep without atonia', [
 ('Occipital hypometabolism with a cingulate-island pattern on FDG-PET', 'This can support DLB, but is classified as a supportive imaging biomarker rather than one of the three indicative biomarkers in the 2017 framework.'),
 ('Relative preservation of medial temporal structures on MRI', 'Relative medial temporal preservation is supportive and can assist the differential with AD, but is not an indicative biomarker by itself.'),
 ('Posterior slow-wave activity with fluctuations on EEG', 'Characteristic EEG slowing is supportive; it does not occupy the same diagnostic biomarker category as PSG-confirmed REM atonia loss.')],
 [S('Three Indicative Tests', '**Reduced striatal DAT uptake, low cardiac MIBG uptake and PSG-confirmed REM sleep without atonia** are the indicative biomarkers listed in the 2017 consensus.',
    'One indicative biomarker with one core feature can support probable DLB. Biomarkers alone without a core feature do not establish probable DLB under that framework.',
    'The test must be valid and clinically concordant. DAT loss can occur in other degenerative parkinsonian syndromes; MIBG interpretation can be confounded by cardiac disease, diabetes and medications.'),
  S('Supportive Evidence and Limits', '**Occipital metabolic change, relative medial temporal preservation and characteristic posterior EEG slowing** add support but do not have identical diagnostic weight.',
    'A normal result on one indirect biomarker does not categorically exclude all Lewy body disease. Reassess phenotype, stage, technical quality and competing pathology.',
    'Newer alpha-synuclein assays are an evolving area; do not retroactively insert every emerging test into the formal 2017 indicative list without identifying a different evidence framework. Clinical diagnosis still requires the syndrome and exclusion of better explanations.')], ['DLB'], style='direct', table=(['2017 category','Examples'],[
 ['Indicative','Reduced DAT uptake; low cardiac MIBG; PSG REM atonia loss'],['Supportive','Relative medial temporal preservation; occipital hypometabolism/cingulate island; characteristic posterior EEG slowing']]))

add('Lewy body cognitive disorders', 'The One-Year Clinical Convention',
 'A patient develops dementia eight months after the onset of spontaneous parkinsonism. Which terminology best fits the conventional DLB-versus-PDD distinction?',
 'Dementia with Lewy bodies', [
 ('Parkinson disease dementia solely because motor symptoms appeared first', 'PDD is conventionally used when dementia develops in well-established PD; a brief motor-first interval within one year is classified as DLB for this distinction.'),
 ('MSA with dementia established by the interval alone', 'The temporal convention separates DLB and PDD labels; it does not establish MSA, which has its own clinical and exclusion criteria.'),
 ('Alzheimer dementia established by any cognitive decline within a year', 'Timing relative to parkinsonism does not identify AD pathology. The full phenotype and relevant biomarkers determine competing or mixed etiologies.')],
 [S('Operational Terminology', '**Use DLB when dementia precedes, accompanies or occurs within one year of parkinsonism onset.** Use PDD when dementia emerges in the context of established PD after a longer motor course.',
    'The rule is an operational clinical/research convention rather than a sharp biological boundary; both lie within the Lewy body disease spectrum.',
    'Establish that the decline meets a dementia-level functional threshold rather than applying the rule to every minor cognitive complaint.'),
  S('Why the Label Is Not the Whole Evaluation', '**Mixed pathology and delirium remain relevant** regardless of terminology. A rapid change should trigger a search for reversible contributors.',
    'Both syndromes require attention to cognition, hallucinations, falls, sleep, autonomic dysfunction, medication burden and caregiver support.',
    'Do not infer a specific individual prognosis from the calendar interval alone. Treatments and adverse-effect susceptibility depend on the actual clinical state, while the one-year convention mainly standardizes classification.')], ['DLB'], style='clinical_scenario')

add('Lewy body cognitive disorders', 'Antipsychotic Sensitivity in DLB',
 'A patient with probable DLB becomes profoundly rigid, somnolent and autonomically unstable after haloperidol for hallucinations. Which interpretation and action are most appropriate?',
 'Suspect a severe neuroleptic-sensitivity reaction and urgently reassess/withdraw the provoking treatment with supportive care', [
 ('Escalate haloperidol because rigidity proves inadequately treated hallucinations', 'Potent dopamine blockade can cause marked deterioration in DLB; increased exposure can worsen the reaction rather than correct the problem.'),
 ('Switch to another potent D2 blocker without a risk assessment', 'Changing within a strongly dopamine-blocking class does not remove the relevant sensitivity and may reproduce serious motor and systemic effects.'),
 ('Attribute the acute deterioration only to inevitable dementia progression', 'An abrupt treatment-linked change with rigidity and autonomic abnormalities requires urgent assessment for a drug reaction, neuroleptic malignant syndrome and other acute causes.')],
 [S('A Clinically Important Susceptibility', '**DLB can produce severe sensitivity to antipsychotics**, especially potent dopamine antagonists. Reactions can include profound sedation, worsening parkinsonism and life-threatening systemic deterioration.',
    'Assess vital signs, hydration, CK, renal function and competing causes such as infection. Severe rigidity, fever or autonomic instability may require hospital-level emergency management.',
    'Review all recent medications and stop or withhold suspected provoking agents through an appropriate clinical plan.'),
  S('Safer Symptom Management', '**Not every hallucination requires an antipsychotic.** Assess distress, danger, visual impairment, delirium, sleep and medication burden and use environmental and caregiver strategies.',
    'Cholinesterase inhibitors can help cognition and sometimes neuropsychiatric symptoms. If psychosis remains severe, specialist discussion may consider cautious options such as low-dose quetiapine or clozapine, recognizing limited DLB-specific evidence and required monitoring.',
    'Pimavanserin has a US PD-psychosis indication, which should not be restated as an unrestricted DLB approval. Antipsychotic mortality warnings and individual cardiac, autonomic and cognitive risks remain relevant.')], ['DLB','NICE'])

add('Lewy body cognitive disorders', 'Cognitive Treatment in Lewy Body Disease',
 'A patient with DLB has cognitive impairment and non-dangerous recurrent hallucinations. Pulse and medication review reveal no contraindication to a cholinesterase inhibitor. Which approach is appropriate?',
 'Consider donepezil or rivastigmine with monitoring, alongside environmental and caregiver measures', [
 ('Use a high-potency antipsychotic as the default cognitive treatment', 'Dopamine blockers do not treat the cognitive syndrome and may cause severe sensitivity; non-dangerous hallucinations do not automatically justify that risk.'),
 ('Use an anticholinergic to improve both memory and hallucinations', 'Anticholinergic burden can worsen cognition, confusion and autonomic problems; it is not a treatment for DLB memory impairment.'),
 ('Assume all AD-labeled cognitive drugs are ineffective in DLB', 'Cholinesterase inhibition has evidence and guideline support in DLB, although indications and product licensing differ by jurisdiction.')],
 [S('Cholinergic Strategy', '**Donepezil or rivastigmine** can improve cognition and global function in appropriate DLB patients; neuropsychiatric benefit may also occur. NICE recommends them in relevant mild/moderate disease contexts.',
    'Start low and titrate, monitoring pulse, syncope, weight, gastrointestinal effects and sleep. DLB-related autonomic dysfunction makes tolerability assessment particularly important.',
    'Rivastigmine has a specific PDD indication in relevant jurisdictions; DLB recommendations and local licensing should be stated separately.'),
  S('Integrated Care', '**Memantine may be considered when cholinesterase inhibitors are unsuitable**, although evidence is less consistent. Drug choice must follow the actual syndrome, severity and tolerability.',
    'Address orthostatic hypotension, sleep-disordered behavior, falls, vision, nutrition and caregiver burden. Avoid adding one drug for each symptom without reviewing cumulative sedation and autonomic effects.',
    'Hallucinations with preserved insight may be managed supportively. A new abrupt deterioration deserves a delirium/medical review rather than automatic escalation of chronic dementia medication.')], ['DLB','NICE'])

add('Frontotemporal and language-led syndromes', 'Behavioral-Variant FTD: Possible and Probable',
 'A 57-year-old develops progressive disinhibition, loss of empathy, compulsive rituals and hyperorality. Daily function declines, and MRI shows frontal/anterior temporal atrophy. Which category best fits the 2011 criteria, after exclusions?',
 'Probable behavioral-variant frontotemporal dementia', [
 ('Possible bvFTD only because imaging cannot contribute to classification', 'Possible disease is clinically defined, but functional decline and compatible imaging support the probable category under the 2011 framework.'),
 ('Definite FTLD pathology established by the MRI alone', 'The imaging pattern supports probable clinical disease; definite pathology requires appropriate pathological or pathogenic-variant evidence rather than MRI alone.'),
 ('Primary depression as established solely because behavior changed before memory', 'Psychiatric disorders are important mimics, but progressive characteristic social-behavioral changes with functional decline and regional atrophy warrant a neurodegenerative evaluation.')],
 [S('Six Discriminating Domains', '**Possible bvFTD requires progressive deterioration and at least three of six domains**: disinhibition, apathy/inertia, loss of sympathy/empathy, perseverative/compulsive behavior, hyperorality/dietary change and a dysexecutive profile with relative memory/visuospatial preservation.',
    'The features should be persistent or recurrent and represent change from baseline. A single episode of socially unusual behavior is insufficient.',
    'Relative memory preservation is a useful pattern, not a guarantee that every bvFTD patient has normal episodic memory.'),
  S('Increasing Diagnostic Confidence', '**Probable bvFTD adds functional decline and compatible frontal/anterior temporal imaging.** Definite FTLD requires appropriate pathology or a known pathogenic mutation with the relevant clinical syndrome.',
    'Exclude better psychiatric, medical or structural explanations and assess AD-related evidence when the phenotype is uncertain. Longitudinal observation can clarify nonprogressive phenocopies.',
    'Management includes safety/financial assessment, structured routines, caregiver support and symptom-directed behavioral treatment. Cholinesterase inhibitors are not routine disease-specific treatment for FTD and may worsen behavior in some patients.')], ['FTD','NICE'])

add('Frontotemporal and language-led syndromes', 'Semantic-Variant Primary Progressive Aphasia',
 'A patient has fluent grammatically organized speech but loses the meaning of familiar words and objects, with severe naming difficulty and relatively preserved repetition. MRI shows anterior temporal atrophy. Which syndrome best fits?',
 'Semantic-variant PPA', [
 ('Logopenic-variant PPA', 'Logopenic disease prominently impairs word retrieval and sentence repetition, with relatively preserved single-word comprehension early, unlike this loss of word/object meaning.'),
 ('Nonfluent/agrammatic PPA', 'Nonfluent disease features agrammatism or effortful apraxic speech rather than fluent output with disproportionate semantic loss.'),
 ('Primary progressive apraxia of speech without aphasia', 'Apraxia of speech primarily disrupts motor planning and sound production; it does not explain loss of word and object meaning.')],
 [S('Semantic Knowledge Loss', '**Semantic-variant PPA** requires impaired confrontation naming and impaired single-word comprehension, supported by features such as object-knowledge loss, surface dyslexia/dysgraphia and preserved repetition or speech production.',
    'Speech can be fluent yet increasingly empty because specific concepts and words lose meaning. Distinguish semantic loss from merely being unable to retrieve a word.',
    'Anterior temporal atrophy, often asymmetric, supports imaging classification. Later disease can involve behavior and broader cognition.'),
  S('Phenotype and Pathology', '**FTLD-TDP pathology is common**, but phenotype does not provide pathological certainty. Etiologic biomarkers or genetic evaluation may be relevant in selected cases.',
    'PPA first requires a progressive language-led syndrome with language as the principal early cause of functional impairment, rather than an aphasia secondary to stroke or a predominantly amnestic disorder.',
    'Speech-language therapy, communication aids and caregiver adaptation are central. Tailor counselling to the preserved abilities and evolving everyday communication needs, not only the variant label.')], ['PPA'], table=(['Variant','Dominant early problem','Typical anatomical emphasis'],[
 ['Semantic','Word/object meaning and naming','Anterior temporal'],['Nonfluent/agrammatic','Grammar or motor speech planning','Left posterior frontal/insular'],['Logopenic','Word retrieval and sentence repetition','Left temporoparietal']]))

add('Frontotemporal and language-led syndromes', 'Nonfluent/Agrammatic PPA',
 'A patient develops effortful halting speech with distorted inconsistent sound errors and simplified, grammatically incorrect sentences. Single-word meaning remains relatively intact. Which variant is most likely?',
 'Nonfluent/agrammatic PPA', [
 ('Semantic-variant PPA', 'Semantic disease is led by impaired word meaning and naming, usually with relatively fluent grammar early; that is different from this motor-speech/agrammatic pattern.'),
 ('Logopenic-variant PPA', 'Logopenic speech can pause for word finding, but usually lacks frank agrammatism and the distorted motor-speech errors that support nonfluent disease.'),
 ('Typical amnestic AD without a language-led syndrome', 'AD can underlie atypical language presentations, but this clinical pattern is a progressive aphasic syndrome and should not be relabeled as typical amnestic disease without evidence.')],
 [S('Grammar and Motor Speech', '**Nonfluent/agrammatic PPA** is characterized by agrammatism or effortful halting speech with apraxia-of-speech features. Complex sentence comprehension may be impaired despite relatively preserved single-word understanding.',
    'Apraxia of speech causes planning/programming errors, often distorted and inconsistent, and differs from dysarthria caused by weakness or execution abnormalities.',
    'A predominantly progressive motor-speech disorder without significant aphasia may be classified separately; not every speech difficulty is PPA.'),
  S('Associated Disease and Care', '**Left posterior frontal and insular abnormalities** support the syndrome. Tau-related FTLD is common, but the clinical phenotype does not prove a single proteinopathy.',
    'Some patients later develop PSP- or corticobasal-spectrum motor features. Examine eye movements, limb praxis, gait and swallowing longitudinally.',
    'Communication strategies, alternative/augmentative systems and speech-language therapy should begin before speech becomes severely limited. Evaluate mood and caregiver needs while preserving the patient’s ability to participate through nonverbal or supported methods.')], ['PPA'])

add('Frontotemporal and language-led syndromes', 'Logopenic PPA and Alzheimer Pathology',
 'A patient has progressive word-finding pauses and poor repetition of sentences, with preserved single-word comprehension and no clear agrammatism or motor-speech distortion. Which syndrome best fits?',
 'Logopenic-variant PPA', [
 ('Semantic-variant PPA', 'Semantic PPA primarily impairs single-word comprehension and semantic knowledge, which are relatively preserved in this presentation.'),
 ('Nonfluent/agrammatic PPA', 'Nonfluent disease is supported by agrammatism or apraxic motor-speech features, neither of which is prominent here.'),
 ('A primary dysarthria without language impairment', 'Dysarthria affects speech execution; it does not explain a language-led combination of word retrieval and sentence repetition deficits.')],
 [S('Phonological Working-Memory Pattern', '**Logopenic PPA** prominently affects word retrieval and phrase/sentence repetition. Phonological errors can occur while articulation, grammar and single-word meaning are relatively preserved early.',
    'Difficulty grows with sentence length and phonological load. Distinguish the pattern from motor speech apraxia and semantic loss.',
    'Left temporoparietal abnormalities support the imaging phenotype, while the overall diagnosis still requires progressive language-led impairment.'),
  S('Etiologic Assessment', '**AD pathology is common in logopenic PPA**, unlike the usual pathology associations of semantic and nonfluent variants, but it is not established solely by the clinical label.',
    'CSF, validated plasma assays or molecular imaging can help when confirmation will change counselling or disease-specific treatment decisions.',
    'Assess clinical stage, functional limitations and treatment safety if anti-amyloid therapy is considered. Atypical phenotype does not make every drug trial result directly transferable; explain evidence limits and provide communication-focused rehabilitation regardless of biomarker testing.')], ['PPA','AD24'])

R['C9'] = ('GeneReviews: C9orf72 frontotemporal dementia and/or ALS', 'https://www.ncbi.nlm.nih.gov/books/NBK268647/')
add('Frontotemporal and language-led syndromes', 'Familial FTD with Motor Neuron Disease',
 'A patient has bvFTD, while several relatives have FTD or ALS. Which genetic mechanism is particularly important to test with a method capable of detecting it?',
 'C9orf72 hexanucleotide repeat expansion', [
 ('An APOE susceptibility allele as sufficient explanation of the FTD–ALS pedigree', 'APOE is relevant to AD susceptibility and treatment risk; it does not establish the common repeat-expansion mechanism linking familial FTD and ALS.'),
 ('An HTT CAG expansion as the characteristic FTD–ALS mechanism', 'HTT causes Huntington disease and can have behavioral presentations, but the FTD–ALS family pattern particularly raises C9orf72.'),
 ('A negative sequence-only panel as definitive exclusion of inherited FTD', 'Sequence-only testing may miss repeat expansions and other variant types; the assay must match the suspected mechanism.')],
 [S('Genetic Heterogeneity', '**C9orf72 repeat expansion** is an important cause of FTD and ALS, which can occur within the same person or family. Psychiatric, behavioral and motor phenotypes vary.',
    'GRN and MAPT are other major familial FTD genes. GRN commonly associates with TDP-43 pathology and can produce asymmetric presentations; MAPT is associated with tau-related disease.',
    'The phenotype is not a one-to-one genotype map, so select testing with a neurogenetics service and appropriate laboratory coverage.'),
  S('Counselling and Test Design', '**A sequence-only panel does not reliably exclude a repeat expansion.** Confirm whether a dedicated C9orf72 assay is included and how technically difficult results are resolved.',
    'Use pretest counselling and, where feasible, test an affected relative first. Explain variable penetrance, age-dependent expression, family implications and limits of prognosis.',
    'A pathogenic result can guide counselling and research eligibility, but is not synonymous with an established gene-specific cure. Predictive testing in an unaffected relative requires a separate informed process.')], ['C9'])

R.update({
 'VAS': ('VASCOG diagnostic criteria for vascular cognitive disorders, 2014', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC4139434/'),
 'VCI24': ('Canadian Stroke Best Practice Recommendations: vascular cognitive impairment, 2024 update', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11772713/'),
 'NPH': ('Japanese Society iNPH management guidelines, third edition, 2021', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC7905302/'),
 'PENS': ('PENS randomized placebo-controlled shunting trial, 2025', 'https://www.nejm.org/doi/10.1056/NEJMoa2503109'),
 'CJD': ('CDC clinical overview and diagnostic criteria for classic CJD', 'https://www.cdc.gov/creutzfeldt-jakob/hcp/clinical-overview/'),
 'AE': ('Graus et al. A clinical approach to autoimmune encephalitis diagnosis, 2016', 'https://doi.org/10.1016/S1474-4422(15)00401-9'),
 'LGI': ('Early immunotherapy in LGI1 faciobrachial dystonic seizures, 103-patient cohort, 2018', 'https://pubmed.ncbi.nlm.nih.gov/29272336/'),
 'WE': ('EFNS Wernicke encephalopathy guideline, 2010', 'https://doi.org/10.1111/j.1468-1331.2010.03153.x'),
 'POINTER': ('US POINTER randomized multidomain lifestyle trial, 2025', 'https://pubmed.ncbi.nlm.nih.gov/40720610/'),
})

add('Vascular cognitive impairment', 'Vascular Cognitive Disease Need Not Be Stepwise',
 'A hypertensive patient develops gradually progressive slowed processing and executive dysfunction with extensive subcortical small-vessel disease. Memory storage is less impaired than planning and set shifting. Which interpretation is best?',
 'Vascular cognitive impairment can fit this gradual dysexecutive presentation', [
 ('Vascular disease is excluded because there was no stepwise decline', 'Stepwise deterioration can follow recurrent strokes, but subcortical small-vessel disease can cause an insidious progressive cognitive course.'),
 ('AD is established because every progressive cognitive syndrome must be amnestic', 'AD can be progressive and atypical, but progression alone is not disease specific; the executive/processing-speed profile and vascular evidence require integrated assessment.'),
 ('The MRI burden establishes severe dementia without functional assessment', 'Imaging supports etiology but does not establish cognitive severity or independence; a major syndrome requires function-related evidence.')],
 [S('Cognitive Profile and Course', '**Vascular cognitive impairment** spans mild to major syndromes and may follow strategic infarction, multiple strokes or diffuse small-vessel injury.',
    'Processing speed, complex attention and executive function are often prominent, although memory, language and visuospatial deficits can occur according to lesion distribution.',
    'A stepwise course is not mandatory. Establish a plausible link between vascular injury and the observed syndrome rather than assuming any white-matter lesion explains all symptoms.'),
  S('Mixed Etiology and Management', '**Vascular and neurodegenerative pathology frequently coexist.** Assess the history, examination, MRI distribution and other etiologic evidence, allowing a mixed formulation when appropriate.',
    'Separate dependence caused by cognitive impairment from hemiparesis, aphasia or sensory disability when assigning severity.',
    'Treat indicated vascular risk factors and support rehabilitation, function and caregiver needs. Cognitive medication decisions depend on the likely etiologies and evidence; a vascular MRI label alone is not a reason to prescribe every AD drug or an antithrombotic.')], ['VAS','VCI24'])

add('Vascular cognitive impairment', 'Microbleed Distribution and Mixed Pathology',
 'An older patient with cognitive decline has strictly lobar cerebral microbleeds and cortical superficial siderosis on susceptibility MRI. Which process is particularly suggested?',
 'Cerebral amyloid angiopathy', [
 ('Deep perforator arteriopathy as the most specific explanation of this distribution', 'Hypertensive arteriopathy more characteristically produces deep microbleeds in basal ganglia, thalamus and brainstem; a strictly lobar/siderosis pattern raises CAA.'),
 ('A normal aging finding that has no treatment implications', 'Lobar hemorrhagic markers can indicate clinically important vessel disease and affect hemorrhage and anti-amyloid risk assessment; they should not be dismissed as inconsequential.'),
 ('A specific proof that all cognitive decline is due exclusively to AD plaques', 'CAA involves vascular amyloid, while cognitive impairment can reflect mixed vascular and parenchymal processes. The MRI pattern does not assign all symptoms to one pathology.')],
 [S('Hemorrhagic Small-Vessel Markers', '**Strictly lobar microbleeds and cortical superficial siderosis** are characteristic clues to CAA, while deep microbleeds more strongly suggest deep perforator arteriopathy.',
    'Distribution is more informative than merely counting any susceptibility focus. Exclude artifacts and alternative causes and apply a validated CAA framework when making a formal probability diagnosis.',
    'CAA and hypertensive arteriopathy can coexist, and a mixed distribution requires a broader interpretation.'),
  S('Clinical Consequences', '**Hemorrhagic markers matter for treatment planning**, including antithrombotic decisions and anti-amyloid ARIA risk. They do not create an identical absolute contraindication for every drug in every setting.',
    'Assess previous hemorrhage, ischemic indications, BP, falls and the complete MRI alongside patient priorities. Specialist review is appropriate for complex competing risks.',
    'A positive AD biomarker does not eliminate vascular contributions. Structural and molecular information answer complementary questions about cognition and treatment safety.')], ['VCI24','LEC'])

add('Vascular cognitive impairment', 'Prevention Is Based on Vascular Indications',
 'A patient has subcortical vascular cognitive impairment and hypertension but no prior ischemic stroke, TIA, atrial fibrillation or other established antithrombotic indication. Which principle is most appropriate?',
 'Optimize vascular risk management without adding an antithrombotic solely because of the cognitive diagnosis', [
 ('Start long-term anticoagulation to treat white-matter hyperintensities alone', 'Anticoagulation treats defined thromboembolic indications, not white-matter lesions or a cognitive label, and can cause significant bleeding harm.'),
 ('Start dual antiplatelet therapy indefinitely for any vascular cognitive syndrome', 'Dual antiplatelets have selected time-limited cerebrovascular/cardiovascular indications; vascular cognitive impairment alone does not justify indefinite dual therapy.'),
 ('Avoid BP treatment because every reduction in pressure worsens cognition', 'BP management is important for vascular health and prevention. Individualize targets and avoid symptomatic hypotension rather than abandoning treatment categorically.')],
 [S('Treat Established Risk and Disease', '**BP, diabetes, lipids, smoking, activity and sleep-related risks** are appropriate targets according to the patient’s vascular indications and tolerability.',
    'Antiplatelets or anticoagulants should follow established stroke/cardiovascular indications. Cognitive impairment and incidental small-vessel MRI changes do not independently establish those indications.',
    'Review adherence and administration support because executive impairment can undermine a sound preventive prescription.'),
  S('Balance Benefit and Harm', '**Avoid symptomatic orthostatic hypotension and overtreatment**, particularly with frailty, autonomic disease or falls. This is individualized risk management rather than a claim that hypertension protects cognition.',
    'A history of lobar hemorrhage or extensive hemorrhagic MRI markers may change antithrombotic risk assessment and warrants careful review when a competing ischemic indication exists.',
    'Exercise, rehabilitation, hearing/vision support and cognitive/environmental strategies can improve function. No preventive intervention guarantees reversal of established vascular injury or eliminates the possibility of mixed neurodegenerative disease.')], ['VCI24','NICE'])

add('Treatable and rapidly progressive disorders', 'Recognizing Idiopathic Normal-Pressure Hydrocephalus',
 'An older adult has a progressive short-stepped broad-based gait, urinary urgency and dysexecutive cognitive impairment. MRI shows ventriculomegaly, enlarged Sylvian fissures and tight high-convexity sulci. Which diagnosis should be specifically evaluated?',
 'Idiopathic normal-pressure hydrocephalus', [
 ('Hydrocephalus ex vacuo as established by ventricular enlargement alone', 'Atrophy can enlarge ventricles, but disproportionate Sylvian enlargement with high-convexity tightness supports a hydrocephalic pattern rather than simple diffuse ex-vacuo enlargement.'),
 ('Typical amnestic AD as the only explanation', 'AD can coexist, but a gait-led syndrome with this CSF-space pattern warrants iNPH assessment rather than an exclusively amnestic attribution.'),
 ('Vascular parkinsonism as proven by a short-stepped gait alone', 'Vascular disease can produce gait/executive impairment, but gait appearance alone does not resolve the differential; the characteristic CSF-space distribution supports iNPH evaluation.')],
 [S('Clinical and Imaging Pattern', '**iNPH is commonly gait led**, with cognitive slowing/executive dysfunction and urinary urgency or incontinence developing in variable combinations. The complete triad is neither necessary at first presentation nor sufficient by itself.',
    'Ventriculomegaly is often quantified by an Evans index at least 0.3, but the overall pattern and alternative explanations matter. DESH denotes disproportionate CSF-space enlargement with tight high-convexity/midline sulci and enlarged Sylvian fissures.',
    'Distinguish idiopathic disease from secondary hydrocephalus after hemorrhage, meningitis or another identified cause.'),
  S('Selection for Further Assessment', '**Exclude important gait, urinary and cognitive mimics** and assess objective baseline performance before CSF-drainage testing or shunt discussion.',
    'The 2021 Japanese framework uses probable-category CSF pressure at or below 200 mmH2O with normal contents plus specified supporting clinical/imaging or drainage-response evidence; the name alone is not a guarantee that every pressure measurement is identical.',
    'Potential benefit must be balanced with shunt risks and coexisting AD/vascular disease. A radiological pattern supports selection but does not promise complete cognitive recovery.')], ['NPH'])

add('Treatable and rapidly progressive disorders', 'Interpreting the CSF Tap Test',
 'A patient with a convincing iNPH phenotype has no clear gait improvement on one assessment soon after a lumbar tap. Which conclusion is most appropriate?',
 'A negative single assessment does not exclude shunt responsiveness; review timing, objective measures and the overall evidence', [
 ('One negative immediate assessment permanently rules out iNPH', 'Tap tests have imperfect sensitivity and delayed improvement may occur; the phenotype and assessment protocol still matter.'),
 ('Ventriculomegaly guarantees a beneficial shunt regardless of testing or comorbidity', 'Ventricular enlargement is not sufficient to guarantee benefit; selection must consider clinical pattern, competing causes and procedural risk.'),
 ('Subjective recall of improvement is preferable to standardized gait measures', 'Patient reports are useful, but objective timed walking and other standardized measures help quantify response and reduce expectation bias.')],
 [S('Objective Drainage Response', '**A large-volume tap commonly removes 30–50 mL of CSF**, with standardized gait measures before and after drainage. Assessment technique and timing are more important than a rigid preference within that volume range.',
    'Use measures such as timed walking, gait velocity or timed up-and-go, and assess delayed change as appropriate. Cognitive/urinary improvement may follow a different time course.',
    'A clear positive response supports selection, while a negative result has insufficient sensitivity to categorically exclude benefit.'),
  S('Further Selection and Trial Evidence', '**Review DESH, the clinical course and alternative causes** and consider specialist-directed repeat or extended drainage assessment when uncertainty remains. These approaches have their own risks and limitations.',
    'The 2025 PENS randomized trial supported gait-velocity improvement at three months in patients selected on the basis of response to CSF drainage.',
    'That evidence does not prove benefit for every tap-negative patient or guarantee cognitive reversal. Counsel about infection, hemorrhage, obstruction and overdrainage/subdural collections, and define realistic functional goals before shunting.')], ['NPH','PENS'])

add('Treatable and rapidly progressive disorders', 'Suspected Sporadic CJD',
 'A patient develops rapidly progressive cognitive decline, ataxia and myoclonus. MRI shows cortical ribboning and caudate/putaminal diffusion abnormalities. Which CSF assay most specifically supports a prion etiology?',
 'Real-time quaking-induced conversion', [
 ('CSF 14-3-3 protein as a prion-specific molecular test', '14-3-3 reflects neuronal injury and can rise in nonprion acute brain disease; it is supportive in context but is not as etiologically specific as RT-QuIC.'),
 ('Total tau alone as definitive CJD confirmation', 'Very high tau can support rapid neuronal injury but is not specific to CJD and cannot independently distinguish all mimics.'),
 ('Oligoclonal bands as the defining prion assay', 'Oligoclonal bands assess intrathecal immune activity and may redirect consideration toward inflammatory disease; they are not a prion-seeding assay.')],
 [S('Prion-Seeding Evidence', '**RT-QuIC detects seeding activity of abnormal prion protein** and has high specificity in the appropriate syndrome. A progressive neuropsychiatric disorder with positive RT-QuIC can support probable sporadic CJD under the CDC framework.',
    'Characteristic MRI includes caudate/putamen high signal or at least two cortical regions among temporal, parietal and occipital areas on DWI/FLAIR in the conventional criteria.',
    'EEG periodic sharp-wave complexes and CSF injury markers can add support but may be absent or nonspecific. A negative test requires interpretation with sampling, subtype and the complete presentation.'),
  S('Do Not Miss Treatable Mimics', '**Autoimmune/infectious encephalitis, seizures, toxic-metabolic disease and malignancy** can cause rapid cognitive decline or diffusion abnormalities. Complete a targeted reversible-cause evaluation.',
    'Definite CJD requires appropriate neuropathological confirmation. Seek specialist/prion surveillance advice for diagnosis, counselling and instrument/tissue precautions when relevant.',
    'Care includes symptom relief, swallowing/nutrition decisions, family support and advance planning. Do not infer a curative treatment from a positive assay or use nonspecific 14-3-3 elevation alone to stop the mimic evaluation.')], ['CJD'])

add('Treatable and rapidly progressive disorders', 'LGI1 Cognitive Disease and Brief Face–Arm Seizures',
 'An older adult develops subacute memory loss, hyponatremia and dozens of very brief unilateral face–arm dystonic events daily. Which antibody-associated disorder is particularly likely?',
 'LGI1-associated autoimmune encephalitis', [
 ('Anti-NMDA-receptor encephalitis', 'NMDA-receptor disease can cause memory, psychiatric and seizure syndromes, often with characteristic movement/autonomic evolution, but this brief faciobrachial phenotype is particularly associated with LGI1.'),
 ('GAD65-associated epilepsy as the most specific explanation', 'GAD65 disease can produce epilepsy and other neurological autoimmunity, but the distinctive frequent face–arm dystonic seizures and hyponatremia point more strongly toward LGI1.'),
 ('Sporadic CJD established from any brief involuntary movement', 'CJD can cause myoclonus and rapid decline, but this stereotyped seizure pattern with hyponatremia raises a treatable antibody-mediated disease that must be assessed.')],
 [S('Faciobrachial Dystonic Seizures', '**FBDS are brief, frequent, stereotyped face–arm events** strongly associated with LGI1 antibodies. They can precede a limbic cognitive syndrome, and a routine scalp EEG may not show a clear correlate for every event.',
    'Hyponatremia and medial temporal abnormalities can support the syndrome, but normal early MRI or routine CSF does not exclude it.',
    'Use antigen-specific testing and interpret serum/CSF results with the phenotype. A nonspecific historical VGKC-complex result is not interchangeable with confirmed LGI1 or CASPR2 antibodies.'),
  S('Time-Sensitive Treatment', '**Early immunotherapy is associated with better seizure control and reduced cognitive progression in cohort evidence.** Antiseizure medication alone may inadequately control FBDS.',
    'Evaluate infection and other causes promptly, then consider specialist-directed corticosteroids, IVIG or plasma exchange according to the presentation and contraindications. Correct sodium carefully and monitor seizures and autonomic/behavioral complications.',
    'The 103-patient study supports early recognition but is not randomized proof of one universally optimal regimen. Follow cognition and relapse risk after acute improvement rather than assuming seizure cessation guarantees complete memory recovery.')], ['LGI','AE'])

add('Treatable and rapidly progressive disorders', 'Possible Autoimmune Encephalitis',
 'Which combination meets the 2016 clinical framework for possible autoimmune encephalitis, after reasonable exclusion of alternatives?',
 'Subacute memory/mental-status or psychiatric change plus at least one qualifying focal, seizure, CSF or MRI feature', [
 ('Years of isolated stable forgetfulness plus an incidental low-titre serum antibody', 'The possible-AE framework requires a compatible subacute clinical syndrome and supporting features; a discordant low-positive antibody does not replace that clinical requirement.'),
 ('Any positive antibody result regardless of symptoms or assay specificity', 'Antibody testing can be misleading when pretest probability is low; interpretation requires phenotype, specimen and assay validation.'),
 ('An amnestic syndrome only after a positive antibody returns', 'The 2016 framework deliberately permits a clinical possible diagnosis before antibody results, allowing timely evaluation and appropriately selected treatment.')],
 [S('Three Required Elements', '**Possible AE requires subacute progression over less than three months** of working-memory deficits, altered mental status or psychiatric symptoms, plus at least one qualifying supporting feature.',
    'Supporting features are a new focal CNS finding, seizures not explained by a previously known seizure disorder, CSF pleocytosis above 5 cells/µL or MRI findings suggestive of encephalitis.',
    'Reasonable exclusion of alternative causes is also required. Possible is a probability level, not proof that every case has an autoimmune etiology.'),
  S('Investigation and Treatment Sequence', '**MRI, EEG and CSF** help assess inflammatory, infectious and seizure-related causes. Send appropriate antibody tests in serum and CSF as indicated by the suspected syndrome.',
    'HSV and other infections require urgent consideration and empiric treatment when indicated; an early negative PCR can be falsely reassuring. Do not let an autoimmune label delay pathogen-directed treatment.',
    'After appropriate exclusion/treatment of infection and other mimics, immunotherapy can be initiated in a strongly supported syndrome without waiting indefinitely for antibody results. Escalation and tumor screening are tailored to phenotype, antibody and response.')], ['AE'], style='direct')

add('Treatable and rapidly progressive disorders', 'Suspected Wernicke Encephalopathy',
 'A malnourished patient with prolonged vomiting has confusion, gaze-evoked nystagmus and gait ataxia. Which immediate treatment principle is appropriate?',
 'Give parenteral thiamine promptly and correct associated metabolic problems', [
 ('Wait for the serum thiamine result before treatment', 'Laboratory confirmation can be delayed or imperfect, while untreated deficiency can cause irreversible injury; a compatible high-risk presentation warrants prompt treatment.'),
 ('Use oral low-dose supplementation as the only acute treatment despite vomiting', 'Oral absorption and intake are unreliable in this setting; suspected acute Wernicke disease requires parenteral treatment rather than a maintenance-only approach.'),
 ('Withhold urgent glucose for hypoglycemia until a thiamine infusion is available', 'Thiamine should be given promptly, ideally before or with carbohydrate when feasible, but lifesaving correction of hypoglycemia must not be delayed.')],
 [S('Clinical Recognition', '**Wernicke encephalopathy** results from thiamine deficiency and can occur with alcohol-associated malnutrition, hyperemesis, bariatric complications and other prolonged nutritional deficits.',
    'The full confusion–ocular–ataxia triad is often absent. In a relevant context, two of dietary deficiency, ocular signs, cerebellar dysfunction and altered mental state/memory support clinical suspicion.',
    'A normal MRI or an incomplete triad does not safely exclude the diagnosis. Delayed treatment can lead to persistent amnestic/Korsakoff deficits.'),
  S('Dose Framework and Support', '**EFNS recommends thiamine 200 mg IV three times daily**, preferably before carbohydrate when feasible, continued according to clinical response. Other national protocols use higher regimens, so identify and follow the applicable protocol.',
    'Do not delay emergency glucose for a hypoglycemic patient; provide thiamine immediately alongside or as soon as available. Check and correct magnesium, which is relevant to thiamine-dependent function.',
    'Treat refeeding risk, electrolyte deficits and the underlying nutritional cause. Monitor response and provide ongoing nutritional rehabilitation rather than assuming a single injection completes treatment.')], ['WE'])

add('Treatable and rapidly progressive disorders', 'Reversible Contributors Are Not Always the Sole Cause',
 'A patient with two years of progressive cognitive decline has low B12 and a substantial anticholinergic medication burden. Which interpretation is most appropriate?',
 'Treat the deficiencies and medication burden while reassessing for coexisting neurodegenerative or vascular disease', [
 ('Promise complete reversal of every cognitive deficit after one B12 injection', 'B12 deficiency is treatable, but recovery depends on duration and competing pathology; the finding does not guarantee that all impairment is attributable or reversible.'),
 ('Ignore the abnormalities once MRI shows hippocampal atrophy', 'Neurodegenerative imaging and treatable contributors can coexist. An atrophy pattern is not a reason to leave B12 deficiency or harmful drug burden untreated.'),
 ('Stop all medicines immediately without reviewing indications or withdrawal risk', 'Medication reduction should be targeted and clinically coordinated; abrupt cessation can cause withdrawal or destabilize another condition.')],
 [S('Contributor Versus Complete Explanation', '**Medication toxicity, B12 deficiency, thyroid dysfunction, sleep disorders and systemic illness** can worsen cognitive performance and daily function.',
    'Assess whether the degree, timing and phenotype plausibly match the abnormality. A common laboratory finding is not automatically the sole cause of a prolonged progressive syndrome.',
    'B12 deficiency can produce neurological disease without a prominent anemia; confirm and treat according to the clinical setting and investigate the cause.'),
  S('Deprescribing and Follow-up', '**Review anticholinergics, sedatives and interacting drugs**, prioritizing agents with weak indications or clear cognitive effects. Use a taper when required and monitor the symptoms for which a medicine was prescribed.',
    'Correct identified nutritional/metabolic abnormalities and reassess cognition and function after an appropriate interval. Persistent decline warrants continued etiologic evaluation.',
    'HIV, syphilis or other infection testing is selected by presentation and risk rather than ordered indiscriminately or categorically omitted. Maintain a mixed-cause formulation when several contributing processes remain supported.')], ['DETECT','NICE'])

add('Behavior, function and prevention', 'Agitation: Treat Distress and Triggers First',
 'A patient with dementia becomes agitated mainly during bathing. Assessment identifies painful shoulder movement and frightening rapid handling; there is no immediate danger. Which initial plan is best?',
 'Treat pain and adapt the care approach and environment before considering an antipsychotic', [
 ('Start a high-dose antipsychotic to suppress every care-related behavior', 'Antipsychotics have stroke, mortality, sedation and movement risks and should not replace correction of an identified distress trigger in a non-dangerous situation.'),
 ('Prescribe a benzodiazepine before every bath without reassessment', 'Benzodiazepines can cause sedation, falls, paradoxical agitation and dependence; they are not a substitute for pain treatment and a less frightening care technique.'),
 ('Use physical restraint as the routine first response', 'Routine restraint can increase fear and harm and does not address pain or communication needs; care should be adapted to the person and the specific safety context.')],
 [S('Identify the Meaning of the Behavior', '**Pain, delirium, constipation, retention, sensory impairment, fear and unmet needs** commonly drive agitation. Obtain a specific description of timing, triggers and consequences.',
    'Use a calm pace, explanation, familiar carers, privacy, sensory support and a tolerable care routine. Evaluate medical causes when behavior changes abruptly.',
    'Nonpharmacological care is active treatment, not simply postponement of medication.'),
  S('Restricted Medication Role', '**Consider an antipsychotic only for an appropriate severe-distress or harm-risk indication**, after reviewing benefits, risks, alternatives and the possibility of DLB/parkinsonian sensitivity.',
    'Use the lowest effective dose for the shortest appropriate period, define a target behavior and reassess regularly. NICE advises at least six-weekly review and stopping if there is no clear ongoing benefit.',
    'Drug approvals differ by jurisdiction and indication; an approval for AD-associated agitation does not make a medicine an unrestricted as-needed sedative for every dementia behavior. Continue pain, environmental and caregiver interventions even if medication becomes necessary.')], ['NICE'])

add('Behavior, function and prevention', 'Capacity and Driving Need Functional Assessment',
 'A patient with mild dementia can explain a proposed treatment and its main consequences but has begun getting lost while driving. Which principle is most appropriate?',
 'Assess treatment-decision capacity and driving safety separately using the relevant functional evidence', [
 ('The dementia diagnosis automatically removes capacity for every decision', 'Capacity is decision specific and can vary with complexity, support and time; a diagnosis alone does not establish global incapacity.'),
 ('A single cognitive-screen cutoff determines both consent capacity and driving fitness universally', 'Screen scores can inform concern, but no universal number resolves all decisions or driving tasks across individuals and jurisdictions.'),
 ('Preserved conversational fluency proves safe driving despite navigation failures', 'Social conversation can remain fluent while visuospatial, executive or navigation skills are impaired; concrete driving concerns require their own assessment.')],
 [S('Supported Decision-Making', '**Assess the particular decision** using understanding, retention, use/weighing of information and communication under the applicable legal framework. Treat delirium and optimize hearing, language and presentation of information.',
    'A patient may retain capacity for a simple treatment while needing support for finances or a more complex choice. Document the assessment rather than substituting a global label.',
    'Respect autonomy and involve family or legally authorized support as appropriate, while distinguishing support from automatic transfer of every decision.'),
  S('Practical Safety', '**Driving requires navigation, attention, judgement, vision and motor function.** Getting lost, crashes, near misses and informant concerns warrant prompt advice and appropriate driving evaluation.',
    'Licensing/reporting obligations are jurisdiction specific and must be checked locally. Avoid presenting a foreign legal rule as universally applicable.',
    'Also review medication administration, cooking, finances, falls and vulnerability to exploitation. Use proportionate supports that preserve participation and reduce concrete risks rather than assuming every activity must stop at diagnosis.')], ['DETECT','NICE'])

add('Behavior, function and prevention', 'Risk Reduction Without Overstating Prevention',
 'An older adult at increased risk of cognitive decline asks what the 2025 US POINTER trial demonstrated. Which answer is most accurate?',
 'A structured multidomain lifestyle intervention improved the global cognitive composite more than a self-guided intervention over two years', [
 ('It proved complete prevention of all future dementia in participants', 'The trial’s reported primary result concerned change in a cognitive composite, not a guarantee that no participant would develop dementia over a lifetime.'),
 ('It established that exercise alone caused the entire observed benefit', 'The intervention combined activity, diet, cognitive/social challenge and health monitoring; the trial did not isolate one component as the sole cause.'),
 ('It showed that vascular-risk management and social engagement are unnecessary', 'Those factors were part of the intervention framework and remain relevant to overall health; the trial does not justify abandoning them.')],
 [S('Randomized Evidence', '**US POINTER enrolled 2111 at-risk older adults** and compared a structured higher-intensity programme with a lower-intensity self-guided programme.',
    'The structured group had a statistically greater rate of improvement in the global cognitive composite, with an adjusted between-group difference of 0.029 SD per year over two years.',
    'Both groups improved on the measured composite. The result does not establish cure, reversal of established dementia or guaranteed lifetime prevention.'),
  S('Clinical Counselling', '**Recommend feasible physical activity, vascular-risk care, a healthy dietary pattern and cognitive/social engagement**, with hearing/vision support and other individual needs addressed.',
    'Adapt recommendations to mobility, frailty, cardiac status and access rather than giving one rigid exercise prescription to every patient.',
    'Avoid claiming that a supplement, commercial brain game or blood biomarker test by itself prevents dementia. Risk modification can be worthwhile despite uncertainty about an individual outcome, and it complements rather than replaces evaluation of new cognitive symptoms.')], ['POINTER'])

R.update({
 'AETX': ('Canadian consensus recommendations for adult autoimmune encephalitis, 2024', 'https://www.cambridge.org/core/journals/canadian-journal-of-neurological-sciences/article/canadian-consensus-guidelines-for-the-diagnosis-and-treatment-of-autoimmune-encephalitis-in-adults/DC88204486B656B85324E93AF2CCCFC7'),
 'RIVA': ('Rivastigmine transdermal prescribing information', 'https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/022083s028lbl.pdf'),
 'CAA': ('Boston CAA criteria version 2.0, MRI-neuropathology diagnostic study, 2022', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9389452/'),
 'CAP': ('NICE NG108: Decision-specific mental capacity assessment in its UK legal context', 'https://www.nice.org.uk/guidance/ng108/chapter/recommendations'),
 'WEUK': ('UK alcohol-treatment guidance: acute hospital Wernicke treatment, 2025', 'https://www.gov.uk/guidance/clinical-guidelines-for-alcohol-treatment/16-alcohol-care-in-acute-hospitals'),
})
rows[24]['refs'].append('RIVA')
rows[24]['sections'][0][1][0][1].append('For the transdermal rivastigmine product, a common labeled initiation is 4.6 mg/24 hours, increasing after at least four weeks if tolerated to 9.5 mg/24 hours. Apply one patch at a time, remove the previous patch and follow restart instructions after an interruption.')
rows[31]['refs'].append('CAA')
rows[31]['sections'][0][1][0][1].append('Boston v2.0 probable CAA requires the appropriate age/presentation and either at least two strictly lobar hemorrhagic lesions or one such lesion plus a qualifying white-matter feature, with no deep hemorrhagic lesion or better alternative cause. The criteria apply to a defined clinical population rather than every incidental susceptibility focus.')
rows[37]['refs'].append('AETX')
rows[37]['sections'][1][1][0][1].append('For severe supported adult AE, Canadian consensus recommends high-dose IV methylprednisolone, for example 1 g daily for five days, combined with IVIG totaling 2 g/kg over two to five days or a suitable plasma-exchange course. Contraindications, infection exclusion and phenotype determine the choice; nonresponse may prompt second-line therapy such as rituximab.')
rows[38]['refs'].append('WEUK')
rows[38]['sections'][1][1][0][1].append('UK acute-hospital alcohol guidance uses IV thiamine 300–500 mg three times daily for three to five days with daily review for suspected/established Wernicke disease. This higher regimen and the older EFNS 200-mg regimen are explicitly different protocol frameworks, not interchangeable claims of one universal dose.')
rows[41]['refs'].append('CAP')

add('Treatable and rapidly progressive disorders', 'NMDAR Encephalitis: A Psychiatric–Neurological Evolution',
 'A 23-year-old woman develops rapidly progressive psychosis, reduced speech, seizures, orofacial dyskinesia and autonomic instability. Infectious evaluation and treatment are proceeding. Which investigation most directly supports the suspected antibody-mediated diagnosis?',
 'CSF IgG antibodies against the GluN1 subunit of the NMDA receptor', [
 ('CSF LGI1-IgG testing as the leading phenotype-specific assay', 'LGI1 disease commonly presents later in life with limbic memory dysfunction, hyponatremia and faciobrachial dystonic seizures; the psychiatric–speech–dyskinesia–autonomic evolution here particularly suggests NMDAR disease.'),
 ('CSF GABA-B-receptor antibodies as the leading phenotype-specific assay', 'GABA-B disease can cause severe seizures and limbic encephalitis, often with a tumor association, but the broader psychiatric, speech and movement evolution here is more characteristic of NMDAR encephalitis.'),
 ('CSF CASPR2-IgG testing as the leading phenotype-specific assay', 'CASPR2 disease can produce limbic symptoms, peripheral hyperexcitability and Morvan features; it is a genuine differential but less characteristic than NMDAR disease for this presentation.')],
 [S('Recognizing the Syndrome', '**Anti-NMDAR encephalitis** can evolve from psychiatric/cognitive symptoms to speech dysfunction, seizures, dyskinesia/rigidity, reduced consciousness and autonomic dysfunction or hypoventilation.',
    'The 2016 probable framework uses rapid onset within three months of at least four of six symptom groups plus abnormal EEG or inflammatory CSF and reasonable exclusion of alternatives; a compatible three-group presentation with a teratoma can also meet that pathway.',
    'Definite antibody-associated disease requires the appropriate clinical context and IgG anti-GluN1 evidence. CSF testing is essential when suspicion is high; a serum-only result should not substitute for a careful evaluation.'),
  S('Treatment and Tumor Assessment', '**Search for an associated tumor, especially ovarian teratoma in the relevant population**, and arrange treatment/removal when indicated. Age and sex influence the screening plan but do not alone confirm or exclude the disease.',
    'After reasonable infection exclusion, prompt first-line immunotherapy commonly combines corticosteroids with IVIG or plasma exchange in severe disease. Rituximab or another second-line strategy may be considered for inadequate response under specialist care.',
    'Seizure, airway, dysautonomia, nutrition and rehabilitation needs can be substantial. Recovery may be prolonged, and early psychiatric symptoms should not prevent neurological reassessment when the syndrome evolves.')], ['AE','AETX'])
# Place the added, coverage-justified item after the general AE criteria question.
rows.insert(38, rows.pop())

# Whole-chapter option review, before final serialization.
rows[10]['others'] = [
 ('A normal amyloid ratio with isolated high total tau', 'This supports neuronal injury but not a specific AD amyloid/tau pattern; acute injury, seizures and prion disease can raise total tau.'),
 ('An isolated low Aβ42 concentration with a preserved Aβ42/Aβ40 ratio', 'An isolated concentration can be affected by production and preanalytical factors; the validated ratio and accompanying tau profile provide more specific interpretation.'),
 ('A normal amyloid ratio with isolated elevation of total CSF protein', 'Barrier dysfunction or other inflammatory/systemic processes can elevate protein; that is not the AD-specific molecular pattern requested.')]
rows[13]['question'] = 'An adult with mild Alzheimer dementia has no symptomatic bradycardia and is to start donepezil. Which regimen matches the standard US labeled initiation and titration?'
rows[13]['others'] = [
 ('Start 5 mg once daily and increase to 10 mg after one week', 'A 10-mg daily target can be appropriate later, but the label requires four to six weeks at 5 mg before that increase to reduce dose-related toxicity.'),
 ('Start 10 mg once daily without a lower-dose lead-in', 'Ten milligrams is a usual maintenance target, but starting there bypasses the labeled 5-mg tolerability period and increases cholinergic adverse effects.'),
 ('Start 5 mg twice daily from the first day', 'The total equals a common later 10-mg daily dose, but does not match once-daily 5-mg initiation and gradual titration.')]
rows[17]['others'] = [
 ('MRI only before the fifth, seventh and fourteenth IV infusions', 'This resembles an earlier infusion-based schedule and omits the additional early assessment and route-independent month-based wording in the specified July 2026 label.'),
 ('MRI at baseline and months three, six and twelve only', 'This schedule provides some surveillance but misses the specified month-one and month-two examinations during the early risk period.'),
 ('MRI at baseline and only when symptoms arise', 'Symptom-triggered scans are necessary, but asymptomatic ARIA is common and the label also requires scheduled early surveillance.')]
rows[19]['others'] = [
 ('Monthly doses of 700 mg for the first three infusions, then 1400 mg', 'This is the earlier trial/original dosing approach; the July 2025 US modification adds a 350-mg first dose and a 1050-mg third dose.'),
 ('Monthly doses of 350 mg and 700 mg, then 1400 mg from infusion three', 'This preserves the early lower doses but skips the specified 1050-mg third infusion, so does not match the current staged schedule.'),
 ('Monthly doses of 350 mg, 700 mg and 1050 mg, then continue 1050 mg', 'This matches the first three steps but not the labeled 1400-mg dose from the fourth infusion onward.')]
rows[23]['others'] = [
 ('A delirium unrelated to medication as the only explanation', 'Intercurrent delirium must be assessed, but the close treatment-linked rigidity and autonomic deterioration strongly raise a neuroleptic reaction; ignoring the exposure would miss a reversible precipitant.'),
 ('An ischemic stroke as established without focal or imaging evidence', 'Stroke can cause acute deterioration and may require evaluation, but generalized rigidity and treatment-linked systemic change are not proof of a focal ischemic event.'),
 ('Ordinary progression of the chronic Lewy body syndrome', 'Chronic progression does not adequately explain an abrupt deterioration after a potent dopamine blocker; urgently evaluate a drug reaction and other acute causes.')]
rows[29]['others'] = [
 ('Pathogenic APP/PSEN variants as the leading mechanism', 'These are important for dominant Alzheimer pedigrees, but a family combining FTD and ALS more specifically raises C9orf72 expansion disease.'),
 ('A GRN pathogenic variant as the most specific FTD–ALS association', 'GRN is a major familial FTD cause and belongs in relevant broader testing, but the FTD–ALS overlap is particularly characteristic of C9orf72.'),
 ('A MAPT pathogenic variant as the most specific FTD–ALS association', 'MAPT causes tau-related familial FTD, sometimes with parkinsonism, but the motor-neuron-disease overlap more strongly supports C9orf72 expansion testing.')]
rows[30]['others'] = [
 ('Vascular disease is unlikely solely because decline was gradual rather than stepwise', 'A stepwise course can follow recurrent strokes, but diffuse subcortical vascular injury may produce gradual executive and processing-speed decline.'),
 ('A pure Alzheimer etiology is established by progression alone', 'AD can progress insidiously, but the executive/processing-speed pattern and extensive vascular injury require integration; progression alone cannot prove a pure AD cause.'),
 ('Major vascular dementia is established by MRI burden alone', 'Imaging supports etiology, but major-versus-mild severity depends on cognitive functional impairment, not lesion burden in isolation.')]
rows[32]['others'] = [
 ('Start aspirin as a specific treatment for the cognitive syndrome', 'Aspirin is appropriate for defined vascular indications, particularly secondary prevention, but the cognitive label alone does not establish a net benefit in this primary-prevention context.'),
 ('Start anticoagulation for the white-matter disease despite no embolic indication', 'Anticoagulation can prevent embolic events in appropriate conditions such as AF, but the scan and cognitive syndrome alone do not establish that indication.'),
 ('Stop antihypertensives to maintain a high BP as the main cognitive treatment', 'Individualized targets and avoidance of orthostatic symptoms are appropriate, but routine withdrawal to maintain hypertension is not a cognitive treatment strategy.')]
rows[35]['others'] = [
 ('CSF 14-3-3 protein', '14-3-3 supports neuronal injury in an appropriate rapid syndrome but can rise in nonprion disease; it is less etiologically specific than RT-QuIC.'),
 ('CSF total tau', 'Marked tau elevation indicates neuronal injury and can add support, but is not a prion-seeding assay and is less specific than RT-QuIC.'),
 ('Serum neurofilament light chain', 'Neurofilament light reflects axonal injury across many conditions; it cannot specifically identify a prion cause of this syndrome.')]
rows[40]['others'] = [
 ('Treat presumed AD alone and defer the contributor review', 'AD can coexist, but treating a suspected primary degeneration does not address a correctable B12 deficit or harmful anticholinergic burden.'),
 ('Attribute the complete two-year syndrome to B12 deficiency and end etiologic follow-up', 'B12 disease can cause cognitive and neurological impairment, but the duration and coexistence of other pathology require reassessment rather than a guaranteed single-cause conclusion.'),
 ('Reduce medicines without treating B12 or investigating its cause', 'Deprescribing is useful, but does not replace correction and etiologic investigation of a documented deficiency that may contribute to neurological injury.')]
rows[41]['others'] = [
 ('Begin an antipsychotic before addressing the painful care trigger', 'Medication may be needed for severe distress or harm risk in selected cases, but the identified pain and handling trigger should be addressed first in this non-dangerous situation.'),
 ('Schedule a benzodiazepine for each bath as the first intervention', 'Short-term sedation has selected uses, but routine pre-bath benzodiazepines add falls/confusion risks while leaving the modifiable distress mechanism untreated.'),
 ('Increase the cholinesterase-inhibitor dose as the immediate solution', 'A cholinesterase inhibitor may have a role in the underlying dementia, but dose escalation is not an immediate treatment for pain and frightening handling during bathing.')]
rows[43]['others'] = [
 ('It demonstrated a lower lifetime incidence of all dementia as its primary endpoint', 'The reported primary endpoint was a global cognitive-composite trajectory over two years, not lifetime dementia incidence.'),
 ('It showed the independent effect of exercise by holding all other components identical', 'The structured intervention was multidomain; the design did not isolate exercise as the sole differing causal component.'),
 ('It established a treatment that reverses established Alzheimer dementia', 'The trial enrolled at-risk older adults and assessed cognitive change; that is distinct from reversing established biomarker-confirmed Alzheimer dementia.')]

# Highlight selected clinically important doses and thresholds in teaching text.
_marks = ['90% sensitivity','75% specificity','90% specificity','5–29 mL/min',
 '4.6 mg/24 hours','9.5 mg/24 hours','10 mg/kg every two weeks','500 mg weekly',
 '360 mg weekly','10 mg/kg every four weeks','350 mg, 700 mg, 1050 mg and then 1400 mg',
 '200 mmH2O','30–50 mL','above 5 cells/µL','200 mg IV three times daily',
 '300–500 mg three times daily','1 g daily for five days','2 g/kg over two to five days',
 '0.029 SD per year','0.45 points','3.25-point','35.1%']
def _mark(text):
    import re
    return re.sub('|'.join(re.escape(x) for x in sorted(_marks,key=len,reverse=True)),lambda m:'=='+m.group()+'==',text)
for _row in rows:
    _row['sections'] = [(h,[(_mark(t),[_mark(x) for x in children]) for t,children in bullets]) for h,bullets in _row['sections']]

# Do not save or install until every mapped question has been completed.
if __name__ == '__main__':
    coverage = ROOT/'Neurology/08. Dementia & Cognitive Disorders.coverage.json'
    c = json.loads(coverage.read_text(encoding='utf-8'))
    assert len(rows) == sum(s['questions'] for s in c['sections']) == c['plannedQuestions'], 'Chapter incomplete; installation prohibited'
    index = 0
    for section in c['sections']:
        assert len(section['decisions']) == section['questions']
        for decision in section['decisions']:
            assert rows[index]['topic'] == section['section']
            rows[index]['coverageDecision'] = decision
            index += 1
    save('Neurology',8,c['chapter'],rows,R,'Original postgraduate educational synthesis with explicit coverage decisions. Criterion versions, drug-label jurisdictions and evidence limitations are stated. Full Harrison subscription text was not accessed. No independent clinician review is claimed.')
    c.update(status='authored_validated',authoredQuestions=len(rows))
    c['questionDecisions'] = [dict(question=i+1,title=r['title'],decision=r['coverageDecision']) for i,r in enumerate(rows)]
    coverage.write_text(json.dumps(c,ensure_ascii=False,indent=2),encoding='utf-8')
