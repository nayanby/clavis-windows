"""Original decision-mapped autoimmune and systemic neurology chapter."""
import json
from qbank_json_chapters import question as Q, save, ROOT

R={
 'GRAUS':('Graus et al: clinical approach to autoimmune encephalitis, 2016','https://pmc.ncbi.nlm.nih.gov/articles/PMC5066574/'),
 'CANADA':('Canadian consensus guidelines for adult autoimmune encephalitis, 2024','https://doi.org/10.1017/cjn.2024.16'),
 'ACUTE':('Autoimmune encephalitis best practice: diagnosis and acute management, 2021','https://pmc.ncbi.nlm.nih.gov/articles/PMC8223680/'),
 'PNS':('Updated diagnostic criteria for paraneoplastic neurologic syndromes, 2021','https://pmc.ncbi.nlm.nih.gov/articles/PMC8237398/'),
}
def S(h,main,*children):return(h,[(main,list(children))])
rows=[]
def add(*a,**kw):rows.append(Q(*a,**kw))

add('Recognition and diagnostic testing','Possible Autoimmune Encephalitis Is a Clinical Entry Point',
 'An adult develops new short-term memory impairment and behavioral change over four weeks, followed by unexplained focal seizures. MRI is initially normal. Which interpretation best fits the 2016 clinical framework?',
 'Possible autoimmune encephalitis warrants evaluation if alternative causes are reasonably excluded',[
 ('Definite autoimmune encephalitis is established by the unexplained seizures','Seizures support the possible category in a compatible subacute syndrome, but do not independently establish definite autoimmune encephalitis or exclude infectious and other causes.'),
 ('Autoimmune encephalitis requires a positive neuronal antibody before clinical classification','Antibodies can establish specific syndromes and improve confidence, but the possible category was designed to permit clinical assessment before delayed results are available.'),
 ('Normal MRI places the presentation outside possible autoimmune encephalitis','MRI abnormalities can support the criteria, but new unexplained seizures provide another qualifying feature; a normal scan does not automatically exclude the possible category.')],
 [S('Apply All Parts of the Entry Criteria','**Possible autoimmune encephalitis requires subacute progression over less than three months** of working-memory impairment, altered mental status or psychiatric symptoms.',
    'At least one supporting feature is required: a new focal CNS finding, seizures unexplained by a known seizure disorder, CSF pleocytosis above five cells per cubic millimetre, or MRI features suggesting encephalitis.',
    'Reasonable exclusion of alternative causes is also essential. The criteria are not fulfilled simply because a patient has psychiatric symptoms or responds transiently to steroids.'),
  S('Classification Guides Investigation, Not Automatic Attribution','**The possible category is an entry point rather than proof of a specific antibody-mediated illness.** Obtain a careful trajectory and exposure history, neurologic assessment, appropriate MRI, EEG and CSF studies.',
    'Investigate infection, seizures themselves, toxic or metabolic disturbance and structural or neoplastic causes according to context. Treat urgent threats while diagnostic assessment proceeds.',
    'Higher-confidence syndrome-specific or antibody-negative probable categories have additional requirements. Treatment decisions integrate severity, objective findings and exclusions; neither waiting indefinitely for antibodies nor treating every possible case as definite disease is justified. Serial assessment can clarify an evolving syndrome and reveal an alternative explanation.')],['GRAUS','CANADA','ACUTE'])

add('Recognition and diagnostic testing','Normal Routine Tests Do Not End a Compatible Evaluation',
 'A patient has a convincing evolving encephalitic syndrome with memory loss and new seizures. MRI and initial CSF cell count are normal. What is the most appropriate interpretation?',
 'Continue a phenotype-directed evaluation; normal routine results do not exclude autoimmune encephalitis',[
 ('Use the normal CSF cell count to prioritize a primary psychiatric diagnosis','A primary psychiatric disorder remains a differential, but a normal cell count cannot explain away objective seizures and an evolving cognitive syndrome or exclude autoimmune disease.'),
 ('Use normal MRI to establish a toxic-metabolic encephalopathy','Metabolic and toxic causes need active investigation, but normal structural imaging is not specific for them and does not establish the mechanism.'),
 ('Use normal MRI and CSF to classify antibody-negative probable autoimmune encephalitis','That category requires positive supporting evidence and relevant exclusions; the absence of routine abnormalities neither establishes probable disease nor excludes all autoimmune syndromes.')],
 [S('Sensitivity Varies With Syndrome and Timing','**Autoimmune encephalitis can have normal conventional MRI or little routine CSF inflammation.** Early testing, the underlying antibody syndrome and the sequence of manifestations influence what is detected.',
    'Review the actual MRI sequences and timing and reassess when clinical evolution warrants it. EEG can detect seizures or focal dysfunction even when structural imaging is unrevealing.',
    'A normal result is therefore a limitation to interpret, not permission to ignore the patient’s trajectory. Conversely, nonspecific EEG slowing alone does not prove immune inflammation.'),
  S('Seek Converging Evidence and Revisit Mimics','**Select further tests from the clinical phenotype**, including appropriately interpreted neural antibodies and infectious studies rather than indiscriminate panels detached from the syndrome.',
    'Review medicines, intoxication, metabolic abnormalities, sleep, ongoing seizures and possible malignancy. An alternative cause may coexist with an antibody or mimic one part of the presentation.',
    'Maintain diagnostic confidence proportional to the evidence. Normal routine studies do not mandate immunotherapy, while serious progressive disease may justify treatment after appropriate exclusion work without every test becoming abnormal. Document the unresolved questions, safety monitoring and reassessment plan so that both treatment response and new discordant findings receive critical review.')],['GRAUS','CANADA','ACUTE'])

add('Recognition and diagnostic testing','Choose the Specimen as Carefully as the Antibody',
 'A young adult has an encephalitic syndrome with psychiatric change, seizures and abnormal movements. Serum NMDAR antibody testing is negative. Which testing strategy is most appropriate when lumbar puncture is safe?',
 'Obtain CSF IgG GluN1 testing and interpret paired serum/CSF results with the phenotype',[
 ('Repeat serum testing alone because serum is the most sensitive specimen for NMDAR disease','Serum is more sensitive for some antibodies such as LGI1, but CSF has particular diagnostic importance in NMDAR encephalitis and can be positive when serum is negative.'),
 ('Substitute serum thyroid antibodies as the confirmatory immune marker','Thyroid antibodies can occur incidentally and do not confirm NMDAR disease; a phenotype-compatible neural antibody assay is the relevant targeted investigation.'),
 ('Use a broad serum panel as a substitute for CSF assessment','Serum panels can contribute when selected appropriately, but cannot replace CSF testing in suspected NMDAR encephalitis or the infectious and inflammatory information obtained from CSF.')],
 [S('Sensitivity Is Antigen- and Specimen-Dependent','**Paired serum and CSF neural antibody testing is often useful**, but the most informative specimen differs by target. CSF is particularly important for NMDAR IgG; serum is more sensitive for LGI1 in many settings.',
    'The relevant NMDAR antibody is IgG against the GluN1 subunit. Other immunoglobulin classes or isolated incongruent serum results should not be equated with the established syndrome.',
    'Collect appropriate samples before immunotherapy when feasible, without creating an unsafe treatment delay. IVIG and other therapies can complicate subsequent interpretation.'),
  S('An Assay Result Must Fit the Patient','**Integrate antibody findings with the syndrome, test method and alternative diagnoses.** Tissue-based screening and antigen-specific confirmation can help resolve unexpected or discordant results.',
    'A positive commercial panel is not an independent diagnosis, especially at low pretest probability. Seek expert laboratory review if the phenotype and result conflict.',
    'CSF also supports investigation for infection, inflammation and selected neoplastic mimics. A negative serum result should not end the evaluation of a strongly compatible NMDAR presentation, while a positive serum result without supporting clinical evidence should not trigger automatic long-term immunosuppression. Discuss tumor assessment and treatment through a syndrome-specific pathway once the integrated diagnosis is supported.')],['GRAUS','CANADA','ACUTE','PNS'])

R['MISDX']=('Multicentre study: autoimmune encephalitis misdiagnosis in adults, 2023','https://pubmed.ncbi.nlm.nih.gov/36441519/')
R['NEGATIVE']=('Antibody-negative autoimmune encephalitis: clinical characterization, 2023','https://doi.org/10.1212/NXI.0000000000200170')

add('Recognition and diagnostic testing','A Positive Panel Does Not Establish the Mechanism',
 'A patient with years of nonspecific fatigue and subjective cognitive symptoms has a weak serum CASPR2 result on a commercial panel. Examination, MRI and routine CSF are unrevealing, without seizures or peripheral hyperexcitability. What is the best next step?',
 'Reassess the phenotype and discuss confirmatory testing with the laboratory before immune attribution',[
 ('Begin a rituximab course for antibody-confirmed autoimmune encephalitis','Rituximab can be used in appropriately diagnosed immune disease, but a weak phenotype-incongruent serum result does not establish that diagnosis or justify its risks.'),
 ('Use serial serum antibody titres as the principal measure of disease activity','Titres can contribute in selected established syndromes, but do not determine whether this initial low-probability presentation is autoimmune or validate a discordant assay result.'),
 ('Use a short steroid response as the confirmatory diagnostic test','Steroids may improve energy, pain or other nonspecific symptoms; a subjective response cannot independently confirm neural autoimmunity or resolve an incongruent antibody result.')],
 [S('Pretest Probability Changes the Meaning of Positivity','**Clinical compatibility is essential when interpreting a neural antibody.** Weak isolated serum results can be unrelated to symptoms, especially when broad testing is applied to a low-probability presentation.',
    'CASPR2-associated disease has recognizable central and peripheral phenotypes, including limbic dysfunction, neuromyotonia and Morvan syndrome. Years of nonspecific symptoms without such findings provide weaker support.',
    'Check the actual antigen, specimen, assay and reported level rather than interpreting the word positive as a diagnosis. Laboratory confirmation can include an orthogonal method or referral testing appropriate to the analyte.'),
  S('Reassess Before Escalating Treatment','**Seek an explanation for the patient’s symptoms while reviewing diagnostic confidence.** Sleep disorders, medicines, mood, metabolic disease and other neurologic conditions may warrant targeted assessment.',
    'Do not regard a normal MRI as proof against all autoimmune disease; the concern here is the combined chronic nonspecific phenotype and discordant laboratory evidence.',
    'Record why the result is or is not considered clinically relevant and discuss uncertain findings with the testing service. Avoid using either subjective steroid benefit or repeated panel positivity as a substitute for objective syndrome assessment. A subsequent compatible evolution should prompt reassessment rather than permanent dismissal, while unsupported immunotherapy can expose the patient to harm and delay the correct diagnosis.')],['CANADA','MISDX','GRAUS'])

add('Recognition and diagnostic testing','Exclude Infection Before an Immune Attribution',
 'An adult has fever, confusion, new seizures and temporal-lobe MRI abnormalities. Initial CSF studies and neuronal antibodies are pending. Which diagnostic-treatment approach is most appropriate?',
 'Investigate infectious and immune causes in parallel while promptly covering plausible HSV encephalitis',[
 ('Begin high-dose steroids and defer antiviral treatment until the antibody panel returns','Steroids can be appropriate for supported autoimmune disease, but a delayed antibody result cannot justify withholding time-sensitive therapy for plausible HSV encephalitis.'),
 ('Classify the temporal MRI pattern as autoimmune limbic encephalitis and use IVIG first','Temporal abnormalities can occur with HSV and seizures as well as autoimmunity; the pattern alone does not establish an immune cause or remove the antiviral indication.'),
 ('Wait for a positive CSF pathogen result before starting targeted antimicrobial treatment','Microbiologic confirmation guides definitive care, but suspected HSV encephalitis warrants prompt empiric treatment while testing proceeds rather than waiting for confirmation.')],
 [S('Shared Phenotypes Require Parallel Investigation','**Infectious and autoimmune encephalitis overlap clinically.** Fever, seizures, altered behavior and temporal MRI changes are not unique to either mechanism.',
    'Obtain CSF when safe for cell count, glucose, protein and relevant pathogen studies, including HSV PCR, alongside phenotype-directed neural antibody testing. Review MRI and EEG in context.',
    'Investigate toxic, metabolic, vascular and neoplastic alternatives when the history or findings suggest them. A positive neural antibody would not automatically exclude coincident infection.'),
  S('Time-Sensitive Care Precedes Complete Certainty','**Give appropriate empiric antimicrobial treatment for a plausible infectious encephalitis.** HSV-active intravenous therapy should follow renal-adjusted local protocols, with hydration and kidney monitoring.',
    'An early negative HSV PCR can require repeat testing when suspicion remains high; integrate sample timing, imaging and clinical evolution rather than stopping therapy on one isolated result.',
    'Consider immune treatment after appropriate infectious assessment when the integrated syndrome supports it, without waiting indefinitely for antibody results. A mass-like lesion requiring lymphoma or other tissue diagnosis introduces separate steroid considerations. The key decision is to protect against a treatable infection while building evidence for mechanism, not to force the case into an immune category from one imaging feature.')],['ACUTE','CANADA','GRAUS'])

add('Recognition and diagnostic testing','Probable Antibody-Negative Disease Requires Positive Evidence',
 'An adult has six weeks of progressive cognitive change. Well-characterized neural antibodies are negative in serum and CSF. After excluding defined autoimmune syndromes and reasonable alternatives, which additional combination supports the 2016 probable antibody-negative autoimmune encephalitis category?',
 'MRI suggesting encephalitis plus CSF-restricted oligoclonal bands',[
 ('A normal MRI plus nonspecific EEG slowing','EEG slowing can document cerebral dysfunction, but does not provide one of the required MRI, CSF-inflammatory or biopsy evidence categories for this specific probable classification.'),
 ('CSF pleocytosis plus CSF-restricted oligoclonal bands with normal MRI','Both findings belong to the same CSF evidence category; two CSF markers do not count as two separate categories under this framework.'),
 ('Subjective steroid benefit plus an elevated serum thyroid antibody','Treatment response and thyroid antibodies are not the required objective evidence categories; both can mislead when used to establish neural autoimmunity.')],
 [S('Use the Complete Framework','**The 2016 probable antibody-negative category requires rapid progression within three months**, exclusion of well-defined autoimmune encephalitis syndromes, absence of well-characterized antibodies in serum and CSF, and reasonable exclusion of alternatives.',
    'At least two separate objective categories are needed: MRI abnormalities suggesting encephalitis; CSF pleocytosis, CSF-specific bands or elevated IgG index; or inflammatory brain biopsy excluding another disorder such as tumor.',
    'CSF pleocytosis and oligoclonal bands are grouped together, not counted twice. An inflammatory biopsy is an available evidence category, not a recommendation to biopsy every uncertain case.'),
  S('Negative Antibodies Are Not a Positive Diagnosis','**Seronegativity describes a test result, not an etiology.** A patient may have untested immune disease, an assay limitation or a nonimmune disorder.',
    'Review testing breadth, specimens and timing, especially after treatment. Reconsider infection, seizures, malignancy and other explanations when the trajectory or objective evidence is discordant.',
    'Patients not meeting this probable category can still require specialist assessment; classification limits should not be converted into automatic dismissal or automatic treatment. Document the level of confidence and reassess with clinical evolution. Prolonged immune escalation requires a stronger rationale than a negative panel coupled with nonspecific symptoms or a temporary subjective steroid response.')],['GRAUS','NEGATIVE','CANADA'],style='direct')

add('Recognition and diagnostic testing','Antibody-Independent Definite Limbic Encephalitis',
 'A patient develops memory loss and seizures over six weeks. MRI shows bilateral medial temporal FLAIR abnormalities highly restricted to those regions. EEG shows temporal slowing, and reasonable alternative causes have been excluded. Neural antibodies are negative. Which classification is supported by the 2016 framework?',
 'Definite autoimmune limbic encephalitis can be supported without a detectable antibody',[
 ('Only possible autoimmune encephalitis because antibodies are negative','Possible disease is an entry category, but the complete bilateral limbic clinical/MRI framework with temporal EEG support and exclusions can establish definite autoimmune limbic encephalitis.'),
 ('Probable antibody-negative encephalitis requires brain biopsy in this presentation','The patient fits a defined limbic syndrome; biopsy is not mandatory for that classification and should not be requested merely because antibody tests are negative.'),
 ('A paraneoplastic limbic syndrome is established by the MRI pattern','Cancer-associated disease is an important possibility, but the limbic pattern does not establish a tumor or a paraneoplastic mechanism without the appropriate integrated assessment.')],
 [S('Meet the Defined Limbic Framework','**Definite autoimmune limbic encephalitis can be diagnosed using a compatible subacute syndrome**, bilateral medial temporal T2/FLAIR abnormalities highly restricted to those regions, supporting CSF or EEG evidence, and reasonable exclusion of other causes.',
    'The clinical syndrome develops within less than three months and includes working-memory deficits, seizures or psychiatric symptoms suggesting limbic involvement.',
    'Support consists of CSF pleocytosis above five cells per cubic millimetre or temporal epileptic/slow-wave EEG activity. Both tests do not have to be abnormal when the rest of this framework is met.'),
  S('Bilateral Signal Is Important but Not Self-Sufficient','**HSV infection, seizure-related changes and neoplastic processes can mimic parts of the picture.** The exclusion requirement remains necessary even when the medial temporal pattern is striking.',
    'Unilateral temporal abnormalities alone do not meet this antibody-independent definite framework; such patients can still have antibody-associated disease and need further evaluation.',
    'Test for relevant neural antibodies because they inform mechanism, tumor association and treatment planning even when classification is already supported clinically. Negative tests do not eliminate all cancer risk or replace an appropriate tumor assessment. Conversely, the term limbic encephalitis does not establish that any coincident tumor is causative; correlate the phenotype, antibody and cancer evidence before assigning paraneoplastic certainty.')],['GRAUS','CANADA','PNS'],style='direct')

add('Recognition and diagnostic testing','EEG Supports the Syndrome and Detects Treatable Seizures',
 'A patient with suspected autoimmune encephalitis becomes intermittently unresponsive. EEG shows diffuse slowing but no captured seizure during a short recording. Which next interpretation is most appropriate?',
 'Slowing documents dysfunction but is nonspecific; consider longer monitoring if nonconvulsive seizures remain plausible',[
 ('Diffuse slowing confirms autoimmune inflammation and supports stopping the etiologic workup','Slowing can occur in metabolic, toxic, infectious and other encephalopathies; it supports cerebral dysfunction but cannot establish an autoimmune cause.'),
 ('The short negative seizure recording excludes a seizure contribution to subsequent episodes','A routine recording samples a limited interval; intermittent seizures or status can require repeat or continuous monitoring when the clinical concern persists.'),
 ('The absence of extreme delta brush materially excludes NMDAR encephalitis','Extreme delta brush can support NMDAR disease in the appropriate setting, but is not required and its absence does not exclude the syndrome.')],
 [S('EEG Has Diagnostic and Monitoring Roles','**Use EEG to identify seizures, nonconvulsive status and cerebral dysfunction.** A clinical episode can reflect seizures, movement phenomena, dysautonomia, medicines or the encephalopathy itself.',
    'Correlate observed events with the recording where possible. Continuous or longer monitoring is appropriate when fluctuating awareness or unexplained deterioration creates ongoing concern.',
    'Diffuse slowing is nonspecific; temporal abnormalities can support a limbic syndrome but also occur with infection, structural disease and seizure-related injury.'),
  S('Recognize Patterns Without Making Them a Standalone Diagnosis','**Extreme delta brush is associated with NMDAR encephalitis**, but the EEG must be interpreted alongside the phenotype, CSF and relevant antibody findings.',
    'Superimposed fast activity can also be influenced by medicines. Not every abnormal movement is an electrographic seizure, and not every unusual EEG pattern calls for anesthetic suppression.',
    'Treat confirmed seizures and status promptly while continuing evaluation of the underlying mechanism. A brief study with no seizure does not guarantee that a later event is nonictal. Reassess sedation, metabolic abnormalities and infection when interpreting background changes; objective seizure control and recovery of cognition may follow different time courses, so one should not be used as a simple surrogate for the other.')],['GRAUS','ACUTE','CANADA'])

add('Antibody-associated syndromes','An Evolving NMDAR Syndrome',
 'A previously well young adult develops rapidly progressive behavioral change, markedly reduced speech, seizures, orofacial dyskinesias and episodes of autonomic instability over three weeks. Which antibody-associated syndrome best unifies this evolution?',
 'NMDAR encephalitis',[
 ('LGI1 encephalitis','LGI1 disease often causes limbic memory impairment and focal seizures, including brief faciobrachial events; this prominent speech, dyskinetic and autonomic multisystem evolution is more characteristic of NMDAR disease.'),
 ('CASPR2-associated Morvan syndrome','Morvan syndrome combines peripheral nerve hyperexcitability, marked sleep disturbance and dysautonomia; those features differ from the predominant speech, seizure and orofacial dyskinetic syndrome here.'),
 ('GABA-B receptor encephalitis','GABA-B receptor disease often presents with severe seizures and limbic cognitive dysfunction, frequently with relevant cancer risk; the broader young-adult dyskinetic and autonomic phenotype more strongly suggests NMDAR disease.')],
 [S('Recognize the Multidomain Evolution','**NMDAR encephalitis can evolve across psychiatric, cognitive, speech, seizure, movement and autonomic domains.** Central hypoventilation and reduced consciousness can complicate severe disease.',
    'Symptoms need not begin simultaneously. An initial psychiatric presentation can precede objective neurologic features; a changing trajectory should trigger reassessment.',
    'Orofacial dyskinesias and complex movements are not all seizures. Video-EEG and bedside correlation help avoid both untreated status and unnecessary deep sedation.'),
  S('Confirm and Protect Against Acute Complications','**Obtain CSF IgG directed against GluN1**, with paired serum assessment and exclusion of important infectious and other mimics. MRI may be normal despite severe illness.',
    'Assess for associated tumors using an age- and sex-informed strategy, particularly ovarian teratoma where relevant. Absence of a detected tumor does not exclude the diagnosis.',
    'Treat through specialist immune-therapy and supportive pathways, including seizure care and close respiratory and autonomic monitoring when indicated. Evaluate swallowing, aspiration, thrombosis, nutrition and rehabilitation needs during prolonged illness. Recovery can be slow and uneven; persistent cognitive or behavioral difficulties require follow-up rather than being equated automatically with ongoing active inflammation or irreversible decline.')],['GRAUS','CANADA','ACUTE'])

add('Antibody-associated syndromes','Tumor Assessment Accompanies NMDAR Confirmation',
 'A 24-year-old woman has a compatible encephalitic syndrome and confirmed CSF IgG GluN1 antibodies. Initial abdominal CT is unrevealing. Which next approach is most appropriate?',
 'Arrange targeted pelvic assessment for ovarian teratoma, with further surveillance individualized to risk and course',[
 ('Accept the negative abdominal CT as completion of tumor assessment','A negative initial study does not exclude every ovarian teratoma; targeted pelvic imaging and an appropriate follow-up plan are needed in this risk context.'),
 ('Prioritize chest imaging for thymoma as the characteristic tumor association','Thymoma is relevant to other immune neurologic syndromes, including selected CASPR2-associated disease, but ovarian teratoma is the characteristic targeted concern in this patient.'),
 ('Use serial serum NMDAR titres to decide whether pelvic imaging is necessary','Antibody titres can contribute to selected follow-up questions, but cannot replace tumor imaging or determine whether an ovarian lesion is present.')],
 [S('Target the Search to the Syndrome and Patient','**Ovarian teratoma is an important association in adult women with NMDAR encephalitis.** Tumor prevalence varies with age and sex, so one universal screening scheme is inappropriate.',
    'Use suitable pelvic ultrasound or MRI according to the initial study, local expertise and clinical circumstances. Review whether the ovaries were adequately assessed rather than assuming an abdominal report answers every pelvic question.',
    'A negative initial tumor search is not evidence against a well-supported antibody-confirmed neurologic diagnosis.'),
  S('Combine Tumor and Neurologic Management','**Treat an identified relevant tumor through specialist gynecologic/oncologic care alongside immunotherapy.** Removing a trigger does not eliminate the need for acute neurologic support.',
    'Persistent or relapsing disease should prompt review of tumor assessment, diagnostic confidence and treatment response. Repeat screening is individualized; do not transfer the PNS-Care high-risk-antibody schedule indiscriminately to every NMDAR patient.',
    'Discuss fertility, procedure risks and uncertainty with the patient or appropriate decision-maker. Empirical removal of normal ovaries is not justified merely by a positive antibody. Continue cognitive, psychiatric and functional rehabilitation, because neurologic recovery may lag behind tumor treatment and the disappearance of acute autonomic or seizure complications.')],['CANADA','ACUTE','PNS','GRAUS'])

R.update({
 'FBDS':('Early immunotherapy in 103 patients with faciobrachial dystonic seizures, 2018','https://pubmed.ncbi.nlm.nih.gov/29272336/'),
 'LGI1COHORT':('LGI1 encephalitis multicentre clinical and outcome study, 2021','https://pmc.ncbi.nlm.nih.gov/articles/PMC7846830/'),
 'MORVAN':('Morvan syndrome: clinical and serological observations in 29 cases, 2012','https://pubmed.ncbi.nlm.nih.gov/22473710/'),
 'GABAB':('GABA-B receptor encephalitis: prognostic cohort, 2022','https://pmc.ncbi.nlm.nih.gov/articles/PMC9062096/'),
})

add('Antibody-associated syndromes','Faciobrachial Events Before Memory Decline',
 'A 66-year-old man has dozens of one-second episodes of unilateral facial grimacing with ipsilateral arm posturing each day. Awareness is usually retained. Routine EEG and MRI are normal, and memory is currently preserved. Which approach best addresses the suspected mechanism?',
 'Urgent LGI1-focused assessment and consideration of immunotherapy, alongside seizure care',[
 ('Escalate antiseizure medicines alone until hippocampal MRI abnormalities appear','Antiseizure medicines may help some events, but suspected LGI1-associated FBDS can precede MRI changes and memory decline and often require prompt immune treatment.'),
 ('Treat as a primary paroxysmal movement disorder and review cognition later','Some movement disorders cause brief posturing, but frequent stereotyped face-arm events in an older adult are a characteristic warning phenotype for LGI1 disease.'),
 ('Require an ictal scalp EEG correlate before ordering neural antibody tests','EEG can clarify competing events, but FBDS often lack a clear scalp ictal correlate; a normal routine recording should not block a phenotype-directed evaluation.')],
 [S('Recognize a Time-Sensitive Warning Phenotype','**Faciobrachial dystonic seizures are very brief, frequent stereotyped events** involving the face and arm, sometimes with leg involvement. They are strongly associated with LGI1 autoimmunity.',
    'They can precede obvious amnesia or a broader limbic syndrome. Normal sodium, MRI or routine EEG early in the course does not exclude the association.',
    'Obtain event videos when possible and review semiology carefully. The term dystonic describes the motor appearance and does not mean these should automatically follow a primary movement-disorder pathway.'),
  S('Treat the Immune Process as Well as the Events','**Early specialist immune treatment is important when the integrated diagnosis is supported.** The 103-patient observational study associated prompt FBDS cessation with lower subsequent cognitive impairment.',
    'This is clinically persuasive observational evidence rather than a guarantee that treatment prevents every cognitive deficit. Do not wait for established dementia to act on a well-supported early syndrome.',
    'Use appropriate LGI1 testing and assess competing diagnoses while planning treatment. Antiseizure medicines are adjuncts rather than a substitute for immunotherapy. Follow seizure burden, memory, sodium and function separately; apparent cessation of the visible events does not by itself prove that all limbic dysfunction has resolved.')],['FBDS','CANADA','ACUTE'])

add('Antibody-associated syndromes','Hyponatremia Can Be a Clue Rather Than the Whole Diagnosis',
 'A 71-year-old develops subacute amnesia and focal seizures. Sodium is 126 mmol/L with a euvolemic hypotonic pattern. MRI shows medial temporal signal change and CSF has two leukocytes per cubic millimetre. Which interpretation is most appropriate?',
 'Consider LGI1 encephalitis while investigating and treating the sodium disturbance',[
 ('Assign the entire syndrome to hyponatremic encephalopathy and reassess only after sodium normalizes','Hyponatremia can contribute to seizures and confusion, but the subacute limbic phenotype and focal findings warrant parallel etiologic assessment rather than assuming sodium explains everything.'),
 ('Use the low CSF cell count to prioritize a degenerative memory disorder','LGI1 disease can have little routine CSF inflammation; a subacute seizure-associated limbic syndrome is not well explained by a primary degenerative diagnosis on that basis.'),
 ('Use hyponatremia to establish a small-cell-lung-cancer-associated limbic syndrome','SCLC can cause SIADH and paraneoplastic disease, but low sodium is not specific for cancer; LGI1 is an important competing association requiring targeted testing.')],
 [S('Integrate the Limbic and Systemic Findings','**LGI1 encephalitis commonly affects older adults with memory impairment and focal seizures.** FBDS are particularly helpful when present, but are not required.',
    'Hyponatremia is frequent and can reflect inappropriate antidiuresis. It strengthens suspicion in the appropriate syndrome without identifying the cause by itself.',
    'Routine CSF can be normal or minimally abnormal. Serum testing is often more sensitive for LGI1 than CSF, although paired testing can help the broader assessment.'),
  S('Manage Sodium and Brain Disease Together','**Assess sodium chronicity, symptoms and contributing medicines**, and correct through an appropriate monitored protocol. Overly rapid correction creates a separate neurologic hazard.',
    'Investigate other causes of hypotonic hyponatremia, including endocrine and drug-related causes. Treating the immune disease does not remove the need for safe electrolyte care.',
    'Monitor cognition and seizure control as sodium improves; persistence of limbic deficits should not be dismissed as delayed electrolyte recovery without reassessment. Use immunotherapy when the integrated evidence supports LGI1 disease and assess tumor risk appropriately, recognizing that this association differs from the much stronger SCLC links of selected other neural antibodies.')],['LGI1COHORT','CANADA','ACUTE'])

add('Antibody-associated syndromes','Peripheral Hyperexcitability With Insomnia and Dysautonomia',
 'A man develops severe insomnia, hallucinations, profuse sweating and fluctuating blood pressure. Examination and EMG demonstrate peripheral nerve hyperexcitability with neuromyotonic discharges. Which syndrome best integrates these findings?',
 'CASPR2-associated Morvan syndrome',[
 ('LGI1-associated limbic encephalitis','LGI1 can cause cognitive disturbance and seizures, but the prominent peripheral neuromyotonia with insomnia and autonomic disturbance particularly suggests the Morvan/CASPR2 spectrum.'),
 ('Isolated acquired neuromyotonia','Isolated neuromyotonia explains cramps and continuous muscle activity, but not the full encephalopathic, sleep and autonomic syndrome that defines the broader Morvan phenotype.'),
 ('NMDAR encephalitis','NMDAR disease can cause insomnia, dysautonomia and movements, but EMG-confirmed peripheral neuromyotonia with this combined syndrome more specifically supports Morvan disease.')],
 [S('Recognize Central, Autonomic and Peripheral Involvement','**Morvan syndrome combines encephalopathic or sleep symptoms, dysautonomia and peripheral nerve hyperexcitability.** Severe insomnia, hallucinations, sweating and cardiovascular fluctuations are useful clues.',
    'Neuromyotonia can produce cramps, stiffness and visible myokymia. EMG documents characteristic spontaneous motor activity rather than attributing every movement to a central seizure.',
    'CASPR2 is an important antigenic association; antigen-specific testing is more informative than an undifferentiated VGKC-complex result.'),
  S('Investigate Tumor Association and Treat Both Domains','**Assess for an associated tumor, particularly thymoma**, guided by the phenotype and specialist evaluation. Tumor association is important but not universal.',
    'Use immune treatment when supported, plus symptom-directed therapy for peripheral hyperexcitability and carefully monitored sleep/autonomic complications. Selected membrane-stabilizing medicines can reduce motor symptoms without treating the whole immune process.',
    'Review respiratory function, nutrition and medication adverse effects in severe disease. A patient with isolated neuromyotonia has a different clinical burden from one with Morvan syndrome; documenting the central and autonomic domains guides monitoring and prevents an incomplete symptomatic-only treatment plan. Follow relapse and functional recovery rather than using the antibody result alone as the endpoint.')],['MORVAN','CANADA','PNS'])

add('Antibody-associated syndromes','Seizure-Predominant Limbic Disease and SCLC Risk',
 'A 63-year-old smoker has new recurrent seizures progressing to status epilepticus with subacute memory loss. CSF and serum testing confirm GABA-B receptor antibodies in a compatible syndrome. Which associated malignancy deserves particular attention?',
 'Small-cell lung carcinoma',[
 ('Ovarian teratoma','Teratoma is a characteristic association in the appropriate NMDAR population, but GABA-B receptor encephalitis in an older smoker particularly raises SCLC risk.'),
 ('Thymoma','Thymoma is relevant to selected CASPR2 and other autoimmune neurologic syndromes, but SCLC is the characteristic tumor concern with this GABA-B receptor phenotype.'),
 ('Testicular germ-cell tumor','Germ-cell tumors are important in selected Ma2/KLHL11-associated syndromes, particularly with brainstem or diencephalic features, rather than the leading association here.')],
 [S('A Limbic Syndrome With Prominent Seizures','**GABA-B receptor encephalitis often causes severe seizures with limbic cognitive or behavioral dysfunction.** Status epilepticus can dominate the presentation.',
    'MRI and CSF findings vary, and no single imaging appearance substitutes for clinical and antibody integration. Exclude infection and other seizure-related causes as appropriate.',
    'The association with SCLC is substantial, especially in the relevant age and smoking context, but an initially negative tumor search does not negate the neurologic diagnosis.'),
  S('Coordinate Neurologic and Cancer Care','**Arrange prompt tumor investigation directed toward the chest and the broader clinical context.** Use appropriate imaging and oncologic assessment rather than relying on serum tumor markers alone.',
    'Treat seizures/status and the immune process while evaluating malignancy. When cancer is found, tumor-directed therapy is a central component of the overall plan, not a reason to postpone supportive neurologic care.',
    'Determine repeat screening from the antibody/phenotype risk framework and clinical course. Coexisting antibodies can modify interpretation and prognosis. Counsel that outcome depends on both neurologic injury and tumor factors; control of seizures does not establish cure of the associated cancer or remove the need for cognitive rehabilitation and follow-up.')],['GABAB','PNS','CANADA','ACUTE'])

R.update({
 'AMPAR':('AMPAR encephalitis: series of 22 patients, 2015','https://pmc.ncbi.nlm.nih.gov/articles/PMC4478035/'),
 'GAD':('Clinical spectrum of high-titre GAD65 antibodies, 2021','https://jnnp.bmj.com/content/92/6/645'),
 'DPPX':('DPPX antibody-associated encephalitis: main syndrome and antibody effects, 2017','https://pmc.ncbi.nlm.nih.gov/articles/PMC5379928/'),
 'IGLON':('Clinical manifestations of anti-IgLON5 disease, 2017','https://pmc.ncbi.nlm.nih.gov/articles/PMC5409845/'),
})

add('Antibody-associated syndromes','AMPAR Disease Needs Tumor and Relapse Assessment',
 'A woman with confirmed AMPAR antibody-associated limbic encephalitis improves after acute immunotherapy. Which follow-up plan is most appropriate?',
 'Complete phenotype-directed tumor assessment and monitor clinically for relapse and residual deficits',[
 ('End tumor assessment because an acute immune response establishes nonparaneoplastic disease','Improvement after immunotherapy does not exclude a cancer trigger; AMPAR disease has important tumor associations that still require evaluation.'),
 ('Use antibody titre normalization as the sole criterion for stopping follow-up','Antibody results can inform selected questions, but do not replace clinical, cognitive and oncologic reassessment or establish that relapse risk has ended.'),
 ('Apply the ovarian-teratoma-focused pathway used for young women with NMDAR disease','Ovarian teratoma is a characteristic NMDAR association; AMPAR evaluation should consider its different tumor spectrum, including lung, breast and thymic tumors.')],
 [S('A Limbic Phenotype With Important Cancer Associations','**AMPAR encephalitis commonly presents with memory and behavioral dysfunction**, sometimes with prominent psychiatric symptoms or seizures. Appropriate neural antibody confirmation must fit the clinical picture.',
    'Reported associated tumors include lung and breast cancers and thymoma. Cohort frequencies are affected by referral and case selection and should not be presented as universal individual probabilities.',
    'Other neural antibodies can coexist and alter the phenotype or prognosis. Assess the whole laboratory profile rather than assuming one surface antibody explains every neurologic feature.'),
  S('Follow Recovery and New Disease Activity Separately','**Relapse can occur after initial improvement**, while some patients have persistent deficits from the first episode. A new change requires assessment for recurrent inflammation and competing causes.',
    'Coordinate cancer investigation and tumor treatment when indicated, alongside neurologic immune therapy and supportive care. A favorable early response does not complete the oncologic evaluation.',
    'Assess memory, mood, seizures and functional recovery at follow-up. Individualize maintenance treatment and surveillance to disease course, risk and treatment adverse effects rather than prescribing a fixed prolonged course to every patient. Distinguish infection, medicine toxicity and ongoing seizures from relapse before increasing immunosuppression; these alternatives can also cause cognitive deterioration after discharge.')],['AMPAR','PNS','CANADA'])

add('Antibody-associated syndromes','GAD65 Results Require Assay and Phenotype Context',
 'A patient with type 1 diabetes and nonspecific dizziness has a low-positive serum GAD65 result. There is no objective stiff-person, cerebellar or epileptic syndrome. Which interpretation is best?',
 'The result may reflect endocrine autoimmunity and does not establish a neurologic GAD65 syndrome',[
 ('The result establishes an autoimmune cerebellar syndrome despite the normal examination','Cerebellar GAD65 disease requires a compatible objective syndrome and integrated testing; nonspecific dizziness with endocrine-associated positivity is insufficient.'),
 ('Any positive serum result justifies a trial of B-cell-depleting treatment','Immune treatment can be considered for supported neurologic disease, but serum positivity alone does not establish an indication or justify treatment risks.'),
 ('A titre threshold from another assay can be applied directly to confirm neurologic disease','Published cutoffs depend on assay method and units; converting a low-positive report into a diagnosis using an unrelated platform threshold is unreliable.')],
 [S('A Broad Antibody Association, Not a Single Diagnosis','**GAD65 antibodies occur in type 1 diabetes and in selected neurologic syndromes**, including stiff-person spectrum, cerebellar ataxia, epilepsy and limbic encephalitis.',
    'Low serum levels lack specificity for neurologic autoimmunity. A high level increases relevance in a compatible syndrome, but is not independently pathognomonic.',
    'The Mayo radioimmunoassay cohort defined high titre as more than 20 nmol/L. This is an assay-specific research/clinical threshold, not a universal cutoff for ELISA or every laboratory.'),
  S('Match Laboratory Evidence to Objective Findings','**Review the clinical phenotype, assay and CSF evidence where appropriate.** Intrathecal antibody production or other supporting findings can increase confidence in selected cases.',
    'Exclude alternative causes of ataxia, seizures or stiffness. Coexisting autoimmune disease can explain why an antibody is present without explaining a new neurologic complaint.',
    'Treatment responsiveness varies across GAD65-associated phenotypes, and chronic epilepsy may not respond like an acute neuronal-surface-antibody syndrome. Set objective goals before immunotherapy and reassess benefit against toxicity. Neither a low titre in isolation nor failure to cross another assay’s threshold should replace specialist evaluation when a convincing objective neurologic syndrome is actually present.')],['GAD','CANADA','MISDX'],style='direct')

add('Antibody-associated syndromes','Diarrhea Before a Hyperexcitable Encephalopathy',
 'An adult develops substantial weight loss and persistent diarrhea, followed by cognitive change, exaggerated startle, tremor and myoclonus. Infection and common metabolic causes are being evaluated. Which neural antibody syndrome best fits?',
 'DPPX antibody-associated encephalitis',[
 ('Glycine-receptor-associated PERM','PERM can produce marked startle, rigidity and brainstem/autonomic dysfunction, but the prominent diarrheal and weight-loss prodrome particularly suggests DPPX-associated disease.'),
 ('CASPR2-associated Morvan syndrome','Morvan disease combines insomnia, dysautonomia and peripheral neuromyotonia; gastrointestinal prodrome followed by predominantly central hyperexcitability is more characteristic of DPPX here.'),
 ('GAD65-associated stiff-person spectrum','Stiff-person disease can cause stimulus-sensitive spasms and stiffness, but this gastrointestinal-cognitive-hyperexcitable sequence is not its typical defining presentation.')],
 [S('Connect Enteric and Central Symptoms','**DPPX is an auxiliary protein associated with Kv4.2 potassium channels.** Antibody-associated disease links gastrointestinal symptoms with cognitive or psychiatric change and CNS hyperexcitability.',
    'Diarrhea and weight loss can precede the neurologic syndrome. Tremor, myoclonus, exaggerated startle and seizures are possible manifestations, with variable tempo.',
    'This combination is a clue for targeted testing, not permission to omit ordinary gastrointestinal, infectious, nutritional or neoplastic evaluation.'),
  S('Confirm the Mechanism and Restore Function','**Use appropriate antibody confirmation within a compatible phenotype**, assessing CSF and imaging according to the wider differential. Review whether apparent jerks are epileptic, myoclonic or stimulus-related.',
    'Provide fluid, electrolyte and nutritional care while specialist immunotherapy is considered. Severe weight loss can materially affect treatment tolerance and rehabilitation.',
    'Reported improvement with immune treatment supports clinical action, but responses and relapse risk vary and evidence largely comes from observational series. Evaluate associated malignancy when indicated by the syndrome and patient context. Follow cognition, startle burden, gait and nutritional recovery separately rather than assuming that resolution of diarrhea proves neurologic remission.')],['DPPX','CANADA','ACUTE'])

add('Antibody-associated syndromes','Sleep-Bulbar Disease Outside a Typical Acute Encephalitis',
 'An older adult has progressive dysphagia, gait instability, nocturnal stridor, obstructive sleep apnea and complex behaviors during both non-REM and REM sleep. Routine MRI is unrevealing. Which diagnosis deserves targeted consideration?',
 'Anti-IgLON5 disease',[
 ('Progressive supranuclear palsy','PSP can cause gait and bulbar dysfunction and has an IgLON5-like mimic, but the complex mixed sleep disorder with stridor should prompt targeted assessment beyond a degenerative label.'),
 ('Multiple system atrophy','MSA can cause stridor, autonomic failure and REM behavior disorder, but the broader mixed non-REM/REM sleep phenotype with bulbar involvement is an important IgLON5 clue.'),
 ('Isolated REM sleep behavior disorder with unrelated dysphagia','Isolated REM behavior disorder can precede a synucleinopathy, but it does not adequately integrate prominent non-REM abnormalities, airway symptoms and progressive bulbar dysfunction.')],
 [S('Recognize the Sleep and Bulbar Combination','**IgLON5 disease can have a chronic progressive course**, with sleep, bulbar, gait, oculomotor or cognitive manifestations. It need not resemble a conventional rapidly evolving limbic encephalitis.',
    'Parasomnias, abnormal non-REM sleep initiation, obstructive apnea and stridor are important clues. A PSP-like presentation can occur, so a familiar movement-disorder phenotype does not end the differential.',
    'Video-polysomnography and targeted antibody testing can help in the appropriate clinical context. Normal routine MRI does not exclude the disease.'),
  S('Airway Safety Is an Immediate Priority','**Assess stridor, sleep-disordered breathing and swallowing promptly.** Respiratory and aspiration risks can be urgent even while the etiologic workup remains incomplete.',
    'Coordinate sleep, respiratory, ENT and neurologic expertise according to the findings, with appropriate ventilation or airway interventions when needed.',
    'Specialist immunotherapy can be considered, but responses are variable and cannot be promised from the antibody result alone. The relationship between autoimmunity and neurodegenerative pathology is complex. Track bulbar, respiratory, sleep and functional outcomes over time; do not use a chronic course to dismiss the immune association or use a positive antibody to assume that established disability will fully reverse.')],['IGLON','CANADA'])

R['HSV']=('IDSA encephalitis guideline: empiric treatment and repeat HSV PCR','https://academic.oup.com/cid/article/47/3/303/313455')
R['UK2026']=('UK joint-society infectious and autoimmune encephalitis guideline, 2026','https://www.journalofinfection.com/article/S0163-4453(26)00199-4/fulltext')

add('Acute treatment and longitudinal care','An Early Negative HSV PCR Does Not Clear the Infection',
 'A patient with fever, seizures and temporal-lobe abnormalities receives intravenous acyclovir. CSF HSV PCR obtained within the first day of neurologic symptoms is negative, but clinical suspicion remains high. Which action is most appropriate?',
 'Continue appropriate acyclovir and arrange repeat CSF HSV PCR with reassessment',[
 ('Stop acyclovir and begin steroid monotherapy for presumed autoimmune disease','Immune disease remains possible, but an early negative PCR does not reliably exclude HSV in a highly compatible syndrome; stopping coverage prematurely can be harmful.'),
 ('Replace intravenous acyclovir with oral valacyclovir while awaiting repeat testing','Oral therapy is useful for other herpes indications but is not the established substitute for intravenous treatment of suspected acute HSV encephalitis.'),
 ('Increase acyclovir above the standard dose because a negative PCR implies resistance','A negative early PCR does not demonstrate antiviral resistance; reassess timing and the differential rather than inferring resistance or increasing exposure without an indication.')],
 [S('Use Timing to Interpret the Negative Result','**An early negative HSV PCR can occur despite infection.** A compatible temporal syndrome warrants repeat sampling and continued treatment while the uncertainty is resolved.',
    'IDSA guidance recommends considering repeat PCR in three to seven days when the syndrome or temporal imaging remains suggestive. Interpret the repeat result alongside clinical evolution and alternative diagnoses.',
    'Neural antibody testing can proceed in parallel, but its pending status should not determine whether a plausible infectious emergency receives treatment.'),
  S('Give the Correct Route and Protect Kidney Function','**The usual adult regimen with normal renal function is acyclovir ==10 mg/kg IV every eight hours==.** Adjust the dose or interval for renal function and use an appropriate weight-based prescribing protocol.',
    'Maintain suitable hydration, monitor renal function and review nephrotoxic medicines. Acyclovir accumulation can itself produce neurotoxicity, particularly with impaired clearance.',
    'Confirmed HSV encephalitis generally requires a prolonged intravenous course, commonly 14–21 days according to immune status, recovery and specialist guidance. This does not mean every initially suspected case needs the full course if a reliable alternative diagnosis is established. Repeat testing and expert reassessment determine when discontinuation is justified; a single early negative test should not be used as automatic clearance for immunosuppression.')],['HSV','UK2026','ACUTE'])

add('Acute treatment and longitudinal care','Do Not Wait Weeks for a Delayed Antibody Panel',
 'A patient has severe, well-supported autoimmune encephalitis after appropriate evaluation of infection and other major mimics. Neural antibody results will take two weeks. No biopsy-sensitive mass lesion is suspected. What is the best treatment approach?',
 'Begin appropriate first-line immunotherapy now with monitoring and ongoing diagnostic reassessment',[
 ('Defer immune therapy until the antibody identifies a molecular target','Antibodies improve classification and guide later choices, but delayed results should not postpone treatment of severe, sufficiently supported disease after appropriate exclusions.'),
 ('Begin azathioprine alone as the acute induction regimen','Azathioprine can be a selected maintenance agent, but its delayed effect is unsuitable as sole immediate therapy for severe acute encephalitis.'),
 ('Use antiseizure therapy alone until repeat MRI documents further injury','Seizure treatment is essential, but does not treat the underlying immune process; waiting for additional structural damage is not a necessary treatment criterion.')],
 [S('Treat on Integrated Evidence','**A compatible syndrome and appropriate exclusion of important mimics can justify acute immunotherapy before antibody results.** Severity, objective findings and the trajectory determine urgency.',
    'Collect relevant serum and CSF samples before treatment where feasible without creating an unsafe delay. Continue to review infection results and emerging discordant findings.',
    'If lymphoma or another biopsy-sensitive mass lesion remains a serious consideration, coordinate tissue strategy before steroids when clinically feasible; this differs from the stated scenario.'),
  S('Use an Acute Rather Than Maintenance Strategy','**First-line options include high-dose corticosteroids, IVIG and plasma exchange.** Severe disease often warrants combination treatment, individualized to contraindications and local expertise.',
    'Monitor glucose, blood pressure, mental state, infection risk and treatment-specific complications. Provide concurrent respiratory, autonomic, seizure and nutritional care as indicated.',
    'Document objective treatment goals, such as consciousness, seizure burden and functional trajectory, rather than relying on subjective improvement alone. Antibody results can later redirect tumor assessment or treatment mechanism. If the patient worsens, reconsider the diagnosis and complications as well as treatment intensity; empiric treatment does not make the original immune attribution immune to revision.')],['CANADA','ACUTE','GRAUS'])

add('Acute treatment and longitudinal care','Select a First-Line Regimen for Severe Disease',
 'Under the 2024 Canadian consensus, which regimen is appropriate initial therapy for severe autoimmune encephalitis when there are no relevant contraindications?',
 'IV methylprednisolone 1 g daily for five days plus IVIG 2 g/kg over two to five days or plasma exchange',[
 ('Oral prednisone 5 mg daily plus a maintenance azathioprine dose','Low-dose prednisone and azathioprine have selected chronic indications, but do not provide the recommended acute induction intensity for severe encephalitis.'),
 ('Rituximab alone followed by reassessment after the induction course','Rituximab is an important second-line option in relevant antibody-mediated disease, but does not replace the recommended rapid first-line strategy in this question.'),
 ('IVIG 0.4 g/kg once followed by monthly maintenance dosing','A single 0.4 g/kg dose is only a fraction of the usual 2 g/kg acute total; maintenance scheduling should not replace completion of appropriate induction therapy.')],
 [S('Use a Defined Acute Course','**The Canadian consensus recommends high-dose steroids with IVIG or plasma exchange for severe disease.** This is consensus-informed practice with limited comparative trial evidence.',
    'Milder presentations can require a different balance, including selected steroid monotherapy with specialist input. Do not transfer one severe-disease regimen to every uncertain encephalopathy.',
    'Consider treatment sequence: plasma exchange can remove recently infused immunoglobulin, so coordinate scheduling when both are used.'),
  S('Match Treatment to the Patient','**Steroids can worsen hyperglycemia, hypertension, psychiatric symptoms and infection.** IVIG requires attention to thrombotic, renal and volume risks.',
    'Plasma exchange requires suitable access and monitoring for hemodynamic instability, electrolyte changes, bleeding and line complications. These risks influence selection rather than establishing a universally superior option.',
    'Assess clinical response and adverse effects during the course, while continuing supportive care. The exact exchange prescription is individualized by the apheresis service. Persistent deficits immediately after induction do not alone establish treatment failure, but severe deterioration or absent meaningful progress warrants timely specialist reassessment rather than indefinite repetition of the same course.')],['CANADA','ACUTE'],table=(['Treatment','Example acute regimen from Canadian consensus','Key monitoring'],[
 ['IV methylprednisolone','==1 g daily for five days==','Glucose, BP, mental state, infection'],
 ['IVIG','==2 g/kg total over two to five days==','Renal function, thrombosis, fluid status'],
 ['Plasma exchange','Five exchanges on alternate days over approximately ten days','Access, BP, calcium/electrolytes, bleeding']]),style='direct')

add('Acute treatment and longitudinal care','Escalation Timing Depends on Severity and Guideline',
 'A patient with confirmed severe NMDAR encephalitis remains critically ill without improvement nine days after appropriately delivered first-line combination treatment began. Complications and diagnostic mimics have been reassessed. Which approach best reflects the 2024 Canadian consensus?',
 'Consider second-line treatment now, commonly rituximab for this antibody-mediated syndrome',[
 ('Wait for three months before considering second-line immune treatment','Slow recovery is common, but severe disease without improvement warrants earlier escalation assessment; a fixed three-month delay does not reflect this consensus.'),
 ('Repeat first-line courses until the serum antibody becomes negative','Selected additional first-line treatment may be reasonable, but serum negativity is not the required endpoint and indefinite repetition can delay effective escalation.'),
 ('Begin cyclophosphamide because NMDAR disease is primarily an intracellular-antigen syndrome','Cyclophosphamide has selected immune indications, particularly some cell-mediated paraneoplastic disorders; NMDAR is a neuronal-surface-antibody syndrome for which rituximab is generally preferred.')],
 [S('Recognize Guideline-Specific Timing','**The Canadian consensus supports second-line assessment after five to ten days in severe disease that fails to improve or worsens.** For mild or moderate disease it uses a longer two-to-four-week interval.',
    'The 2021 best-practice recommendations describe consideration after two to four weeks without improvement following combined acute therapy. These are not identical time anchors or high-certainty biologic deadlines.',
    'Clinical severity, treatment adequacy, complications and confidence in the diagnosis determine application. Do not interpret slower expected recovery as a reason to ignore ongoing severe disease.'),
  S('Select and Monitor the Second-Line Agent','**Rituximab is commonly preferred for neuronal-surface-antibody disease.** Example regimens include 1 g IV repeated after two weeks or 375 mg per square metre weekly for four weeks.',
    'Assess infection risks, hepatitis B status, blood counts and immunoglobulins and arrange appropriate infusion precautions before treatment. Drug safety and prevention measures require an individualized plan.',
    'Continue tumor assessment and supportive care. Improvement may lag behind B-cell depletion, and refractory disease can require specialist reassessment of mechanism and further options. Evidence for later agents is more limited; do not present emerging rescue treatments as interchangeable standard care or escalate without checking for infection and treatment-related deterioration.')],['CANADA','ACUTE'],style='direct')

R.update({
 'RTX':('Rituxan prescribing information: HBV screening and safety','https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=b172773b-3905-4a1c-ad95-bab4b6126563'),
 'LONG':('AE recommendations for symptomatic and long-term management, 2021','https://jnnp.bmj.com/content/92/8/897'),
 'RECOVERY':('Autoimmune encephalitis: recovery and long-term sequelae, 2025','https://pubmed.ncbi.nlm.nih.gov/39832911/'),
})

add('Acute treatment and longitudinal care','HBsAg Alone Is Not Adequate Before Rituximab',
 'Rituximab is planned for severe antibody-mediated encephalitis. HBsAg is negative, but total anti-HBc is positive. Which approach is most appropriate?',
 'Assess prior HBV infection and arrange an expert reactivation-prevention plan before B-cell depletion',[
 ('Proceed without HBV precautions because HBsAg is negative','An HBsAg-negative, anti-HBc-positive patient can still have HBV reactivation with B-cell depletion; surface-antigen negativity alone does not establish safety.'),
 ('Repeat liver enzymes and proceed if they are normal','Normal enzymes do not exclude prior HBV infection or predict absence of reactivation during rituximab; virologic assessment and prevention planning are still needed.'),
 ('Give an HBV vaccine dose as the sole preventive intervention','Vaccination can prevent new infection in susceptible individuals, but does not eliminate reactivation risk from prior infection identified by anti-HBc positivity.')],
 [S('Screen for Current and Previous Infection','**Rituximab can reactivate HBV even when HBsAg is negative.** Prescribing information requires HBsAg and anti-HBc testing before treatment.',
    'Interpret anti-HBc with the clinical context and additional serology; seek HBV DNA and specialist advice as appropriate. Anti-HBs positivity does not by itself cancel the concern.',
    'Coordinate antiviral prevention and monitoring with clinicians experienced in HBV. For high-risk B-cell-depleting treatment, do not substitute liver-enzyme surveillance alone for an appropriate prevention strategy.'),
  S('Plan Safety Beyond One Screening Test','**Review active infections, blood counts and baseline immunoglobulins**, and assess vaccination and other prevention needs in the context of urgency and prior therapy.',
    'Monitor infusion reactions and later infectious complications. Prolonged steroid combinations can require additional infection prevention based on dose, duration and patient risks.',
    'HBV exposure is not automatically a permanent prohibition against rituximab; it requires a concrete risk-reduction plan. Document who will prescribe and monitor antiviral care and how follow-up continues after immune treatment, because reactivation can be delayed. Balance the neurologic urgency against modifiable infection risks through coordinated specialist decisions rather than overlooking a positive core antibody.')],['RTX','CANADA'])

add('Acute treatment and longitudinal care','Hypoventilation Requires Organ Support During Immune Treatment',
 'A patient with severe NMDAR encephalitis develops fluctuating consciousness, recurrent apnea and marked heart-rate and BP variability. Which immediate care plan is most appropriate?',
 'ICU-level respiratory and hemodynamic support while continuing mechanism-directed treatment',[
 ('Escalate immunotherapy on the ward and await a respiratory response','Immunotherapy treats the underlying disease but cannot be relied on to reverse recurrent apnea immediately; airway and circulatory risks need monitored organ support.'),
 ('Use supplemental oxygen alone and assess ventilation if saturation falls','Oxygen can improve saturation while hypoventilation and hypercapnia persist; recurrent apnea requires direct ventilation assessment and appropriate airway support.'),
 ('Treat all observed movements with escalating anesthetic antiseizure therapy','Confirmed status can require anesthetic treatment, but dyskinesias and autonomic events are not all seizures; EEG correlation helps avoid unnecessary suppression and additional respiratory harm.')],
 [S('Support Physiology While Immune Therapy Takes Effect','**Central hypoventilation and dysautonomia can be life-threatening in NMDAR encephalitis.** Recurrent apnea warrants urgent airway and ventilatory assessment.',
    'Monitor ventilation as well as oxygenation. Heart-rate and BP instability require continuous assessment, attention to provoking factors and appropriately titrated treatment.',
    'Review sedation, medicines, infection and seizures as additional causes of deterioration; do not attribute every new abnormality automatically to autoimmune activity.'),
  S('Prevent Complications of a Prolonged Admission','**Coordinate seizure monitoring, aspiration prevention and nutrition**, with thrombosis prevention, pressure care and safe mobilization when feasible.',
    'Use video-EEG to distinguish seizures from complex dyskinesias when uncertainty changes management. Avoid unnecessary sedative accumulation while controlling dangerous agitation and confirmed status.',
    'Continue immune and tumor-directed care alongside organ support rather than treating these as sequential stages. Communication with family and rehabilitation planning are important during a potentially long recovery. Severe initial illness does not prove irreversible injury, but prolonged immobility, infection and treatment toxicity can add disability if preventive care is neglected. Reassess readiness for weaning and functional participation as consciousness and autonomic stability improve.')],['ACUTE','CANADA','LONG'])

add('Acute treatment and longitudinal care','Tumor Removal and Immunotherapy Are Complementary',
 'A young woman with confirmed NMDAR encephalitis has an ovarian teratoma identified during evaluation. She is receiving first-line immune treatment and supportive care. Which next strategy is most appropriate?',
 'Coordinate timely tumor-directed treatment alongside continued neurologic immune and supportive care',[
 ('Delay tumor treatment until neurologic remission is complete','Stabilization and procedural risk matter, but a relevant tumor can sustain the immune trigger; waiting for complete neurologic recovery can unnecessarily defer an important treatment component.'),
 ('Stop immunotherapy once the teratoma is removed','Resection addresses an associated trigger, but does not instantly terminate established CNS inflammation or replace neurologic treatment and monitoring.'),
 ('Complete a prolonged immunotherapy trial before deciding whether the teratoma is relevant','The characteristic tumor-syndrome association supports prompt specialist coordination rather than treating the identified teratoma as incidental until months of immune therapy have failed.')],
 [S('Address the Trigger and Established Neurologic Disease','**A relevant tumor and the immune response require coordinated treatment.** In NMDAR encephalitis, teratoma assessment and management are part of the disease-specific pathway.',
    'Plan surgery with gynecologic and anesthetic teams, accounting for dysautonomia, ventilation and overall stability. Timely treatment means a coordinated feasible plan, not ignoring procedural risks.',
    'Discuss fertility-preserving options and histologic assessment as appropriate. A detected lesion should receive specialist evaluation rather than an assumed operative approach from the antibody result alone.'),
  S('Continue Care After the Procedure','**Recovery may lag behind tumor treatment.** Continue immune therapy according to severity and response, with respiratory, seizure, nutritional and rehabilitation support.',
    'Do not interpret persisting symptoms immediately after resection as proof of a second tumor or treatment failure. Reassess clinical trajectory and complications systematically.',
    'Follow-up should address cognition, behavior, function and oncologic questions. A relapse or unexpectedly refractory course may warrant renewed tumor review and diagnostic reassessment. This combined strategy differs from simply adding anticancer therapy after neurologic care is finished; both teams need to share the treatment timeline and anticipated complications throughout the acute admission and recovery.')],['CANADA','ACUTE','PNS','LONG'])

add('Acute treatment and longitudinal care','Residual Memory Problems Are Not Automatically Relapse',
 'Six months after LGI1 encephalitis, a patient has stable residual memory difficulty. A week of poor sleep and a sedating medicine is followed by worse attention, without clear new seizures or focal findings. Which next approach is best?',
 'Assess medicines, sleep, seizures and objective change before assigning relapse or escalating immunotherapy',[
 ('Start rituximab immediately because any cognitive worsening establishes relapse','Relapse can warrant immune treatment, but transient worsening has competing causes; objective reassessment is needed before exposing the patient to additional immunosuppression.'),
 ('Use a persistently positive serum antibody as sufficient confirmation of relapse','Antibodies may persist after clinical improvement; positivity alone does not distinguish residual injury, a reversible comorbidity and renewed inflammatory activity.'),
 ('Classify the deficit as fixed and avoid further neurologic evaluation','Persistent sequelae are common, but a new change still merits assessment for seizures, infection, medication effects or genuine recurrent disease rather than automatic dismissal.')],
 [S('Separate Recovery, Fluctuation and New Inflammation','**Cognitive, sleep, mood and seizure problems can persist after autoimmune encephalitis.** Stable residual disability does not necessarily mean ongoing immune activity.',
    'Define the baseline and time course and seek collateral history. Review medicines, sleep, infection, metabolic factors and possible seizures; select EEG, MRI or CSF when the clinical question warrants them.',
    'Use serial objective cognitive and functional assessment where possible. A single symptom report or antibody level cannot independently establish relapse.'),
  S('Individualize Long-Term Immune Treatment','**A convincing clinical relapse with appropriate supporting evidence can justify acute retreatment and maintenance planning.** Recurrent disease differs from a monophasic episode with residual deficits.',
    'Balance relapse risk against infection, hypogammaglobulinemia and other treatment toxicity. There is no universally proven maintenance regimen or duration for every antibody syndrome.',
    'Provide cognitive rehabilitation, mood and sleep treatment, and support for work, driving and daily activities according to function. Continue appropriate cancer follow-up when relevant. Improvement in reversible contributors can reduce disability without immune escalation; persistent objective deterioration after those factors are addressed should prompt renewed assessment rather than an indefinite assumption that recovery alone explains it.')],['LONG','RECOVERY','CANADA'])

R['PNSVALID']=('Clinical evaluation of PNS-Care criteria, 2024','https://pubmed.ncbi.nlm.nih.gov/39321395/')

add('Paraneoplastic neurological syndromes','PNS Certainty Requires Integrated Evidence',
 'A patient with a high-risk neurologic phenotype has a confirmed high-risk neural antibody. Initial cancer investigation is negative. Which principle best reflects the 2021 PNS-Care framework?',
 'Integrate phenotype, antibody, cancer evidence and follow-up rather than declaring definite PNS from the antibody alone',[
 ('A high-risk antibody establishes definite PNS independently of cancer findings','High-risk antibodies strongly guide tumor investigation, but the framework combines clinical, antibody and cancer evidence; antibody positivity alone does not establish definite PNS.'),
 ('Negative initial screening excludes a paraneoplastic mechanism','Neurologic disease can precede detection of cancer, so a negative initial search does not end appropriate high-risk surveillance.'),
 ('Any coincident tumor establishes definite PNS regardless of its type','A coincident tumor can be unrelated; phenotype-antibody-tumor consistency and, in selected discordant cases, antigen expression matter to attribution.')],
 [S('Use the Framework Rather Than One Positive Test','**PNS-Care combines the clinical phenotype, neural antibody risk and evidence of a relevant cancer.** Follow-up can change diagnostic certainty when an initially occult tumor is later detected.',
    'The 2021 score categories are definite at eight or more, probable at six to seven, possible at four to five and non-PNS by this classification at three or less.',
    'These categories standardize certainty rather than replacing clinical judgment. A low score does not itself explain the symptoms or make further investigation unnecessary when suspicion remains.'),
  S('Exclude Competing Cancer-Related Mechanisms','**Direct metastasis, leptomeningeal disease, treatment toxicity, infection and metabolic disturbance must be considered.** Cancer plus neurologic symptoms is not automatically an immune PNS.',
    'Confirm unexpected antibody results with appropriate laboratory methods and correlate their known phenotype and tumor associations.',
    'Plan cancer assessment from the integrated risk profile and revisit it as follow-up accumulates. A new tumor diagnosis can increase certainty, while prolonged negative surveillance can alter the classification. Record the current evidence and uncertainty rather than preserving an initial label indefinitely; clinical care and symptom treatment should continue while the etiologic status is reassessed.')],['PNS','PNSVALID'],style='direct')

add('Paraneoplastic neurological syndromes','Intracellular Antibodies Often Mark a Cellular Immune Process',
 'Which comparison best explains why an anti-Hu syndrome may respond differently to antibody-removal treatment than NMDAR encephalitis?',
 'Hu targets an intracellular antigen and often marks T-cell-associated injury, whereas NMDAR surface antibodies can directly alter receptor function',[
 ('Hu and NMDAR antibodies primarily cause the same reversible surface-receptor internalization','NMDAR antibodies can alter surface receptor availability, but Hu is intracellular and the associated injury is not explained by the same surface-antibody mechanism.'),
 ('Hu is a surface channel antibody while NMDAR is an intracellular marker','This reverses the target locations and would mislead both mechanistic reasoning and expectations for immune treatment.'),
 ('Hu-associated disease is a direct metastatic complication while NMDAR disease is immune-mediated','Hu-associated PNS is immune-mediated despite its cancer association; direct metastatic disease is a separate mechanism that must be excluded.')],
 [S('Antigen Location Informs Mechanism','**Many classical intracellular onconeural antibodies are biomarkers of a predominantly cellular immune response.** They can be highly informative for cancer search without being the sole direct effector of neuronal injury.',
    'Neuronal-surface antibodies, such as NMDAR IgG, can directly disturb synaptic function. Selected syndromes can therefore show substantial recovery when immune activity is controlled.',
    'This distinction is a framework, not a guarantee of response or a rule covering every intracellular antigen; GAD65-associated disease needs its own phenotype-specific interpretation.'),
  S('Set Realistic Treatment Goals','**Tumor-directed treatment is central when a relevant malignancy is present.** Specialist immune treatment may aim to stabilize disease before irreversible neuronal loss accumulates.',
    'Apheresis or IVIG should not be assumed to reverse established anti-Hu neuronal loss as readily as a reversible surface-receptor dysfunction. Conversely, limited expected reversibility does not justify abandoning supportive care.',
    'Assess progression, function and complications and discuss the evidence limits of immune options. Rehabilitation, pain and autonomic care remain important even when complete recovery is unlikely. Do not infer either therapeutic futility or a mandatory drug solely from antibody location; use the clinical syndrome, cancer status and treatment risks.')],['PNS','ACUTE','CANADA'],style='direct')

add('Paraneoplastic neurological syndromes','Anti-Hu Sensory Neuronopathy Directs the Cancer Search',
 'A 68-year-old smoker develops a subacute painful, asymmetric, non-length-dependent sensory syndrome with marked sensory ataxia and reduced sensory nerve action potentials. Anti-Hu is confirmed. Which tumor should be prioritized?',
 'Small-cell lung carcinoma',[
 ('Thymoma','Thymoma is important in selected CASPR2-associated disease and other immune syndromes, but anti-Hu sensory neuronopathy particularly directs attention toward SCLC.'),
 ('Ovarian teratoma','Teratoma is a characteristic NMDAR association in an appropriate population, but is not the leading tumor concern in an older smoker with confirmed anti-Hu neuronopathy.'),
 ('Hodgkin lymphoma','Hodgkin lymphoma is associated with DNER/Tr-related cerebellar disease among other presentations; the antibody and sensory-ganglion phenotype here more strongly favor SCLC.')],
 [S('Recognize a Sensory Ganglion Pattern','**Sensory neuronopathy can be asymmetric and non-length-dependent**, affecting upper limbs or trunk early and producing severe proprioceptive ataxia.',
    'Electrophysiology can show reduced sensory responses without the usual distal gradient. Assess strength and other neurologic domains because anti-Hu disease can be multifocal.',
    'Sjogren disease, selected toxins and other immune or inherited disorders are alternative causes of neuronopathy; the confirmed antibody and clinical risk context refine this case.'),
  S('Search and Follow According to Risk','**Arrange prompt chest-focused and appropriate broader cancer evaluation.** A normal first study does not end the search in a high-risk phenotype-antibody combination.',
    'Coordinate additional imaging and tissue diagnosis with the relevant services; tumor markers alone cannot exclude SCLC. Treat an identified malignancy and consider specialist immune therapy in parallel.',
    'Provide fall prevention, gait aids, neuropathic pain and autonomic assessment where relevant. Established ganglion-cell injury may recover incompletely, so stabilization and preservation of remaining function are meaningful goals. Reassess atypical progression for another process rather than attributing every later symptom to the original neuronopathy.')],['PNS','PNSVALID'])

add('Paraneoplastic neurological syndromes','Rapid Cerebellar Decline Can Precede Visible Atrophy',
 'A woman develops severe bilateral gait and limb ataxia over eight weeks. Initial MRI excludes a structural lesion but shows little cerebellar atrophy. Anti-Yo is confirmed. Which cancer assessment is particularly relevant?',
 'Breast and gynecologic malignancy assessment',[
 ('Testicular germ-cell tumor assessment as the characteristic anti-Yo association','Germ-cell tumors are important in selected Ma2 or KLHL11 syndromes, but anti-Yo-associated cerebellar disease classically directs assessment toward breast and gynecologic malignancies.'),
 ('Hodgkin lymphoma assessment as the characteristic anti-Yo association','Hodgkin lymphoma is particularly associated with DNER/Tr cerebellar disease; antibody specificity helps distinguish that search from anti-Yo-associated disease.'),
 ('Thymoma assessment as the characteristic anti-Yo association','Thymoma can accompany other immune neurologic syndromes, but is not the characteristic cancer association that should lead this anti-Yo-directed evaluation.')],
 [S('Use Tempo and Antibody Together','**Rapidly progressive cerebellar syndrome can cause major disability within three months.** Early imaging may lack the atrophy that later accompanies neuronal loss.',
    'Exclude stroke, metastasis, leptomeningeal disease, infection, toxins and metabolic or nutritional causes. A normal structural scan does not by itself establish an immune mechanism.',
    'Confirmed anti-Yo supports a high-risk cancer-associated syndrome, commonly with breast or gynecologic tumors. DNER/Tr points toward a different association, particularly Hodgkin lymphoma.'),
  S('Pursue Tumor Control and Functional Support','**Arrange prompt targeted cancer investigation**, extending the search and surveillance according to phenotype and antibody risk if initial studies are negative.',
    'Coordinate tumor treatment and specialist immune decisions. Established cerebellar neuronal loss can limit reversal, so early stabilization is an important goal.',
    'Assess swallowing, speech, gait safety, vision-related symptoms and daily functioning. Rehabilitation and assistive strategies remain necessary even after cancer treatment succeeds. Avoid promising that tumor removal will promptly restore coordination or waiting for MRI atrophy before taking a severe subacute syndrome seriously; serial clinical function and the etiologic evidence guide urgency.')],['PNS','PNSVALID'])

R.update({
 'KLHL':('KLHL11 encephalitis phenotype and oncologic associations, 2020','https://pmc.ncbi.nlm.nih.gov/articles/PMC7653501/'),
 'SITC':('SITC immune checkpoint inhibitor adverse-event guideline, 2021','https://pmc.ncbi.nlm.nih.gov/articles/PMC8237720/'),
 'ASCO':('ASCO immune-related adverse-event guideline update, 2021','https://doi.org/10.1200/JCO.21.01440'),
})

add('Paraneoplastic neurological syndromes','Rhombencephalitis With Hearing Symptoms',
 'A man develops subacute vertigo, tinnitus, hearing loss, diplopia and ataxia. Testing confirms KLHL11 IgG. Which associated tumor deserves targeted investigation?',
 'Testicular germ-cell tumor, particularly seminoma',[
 ('Small-cell lung carcinoma','SCLC is important in Hu and GABA-B receptor syndromes, but the KLHL11 rhombencephalitic and auditory phenotype particularly points toward a testicular germ-cell source.'),
 ('Hodgkin lymphoma','Hodgkin lymphoma is an important association of DNER/Tr cerebellar disease, but is not the characteristic tumor association of confirmed KLHL11 disease.'),
 ('Thymoma','Thymoma can accompany Morvan/CASPR2 and other immune syndromes, but does not lead the antibody-directed search in this rhombencephalitic presentation.')],
 [S('Recognize a Brainstem-Cerebellar Phenotype','**KLHL11-associated disease often involves brainstem and cerebellar systems**, with ataxia, vertigo and characteristic auditory symptoms in many reported patients.',
    'Ma2-associated disease can overlap anatomically but may also involve limbic or diencephalic systems. Clinical overlap does not make the antibodies interchangeable.',
    'Review MRI, CSF and electrophysiologic or audiologic findings as appropriate, while excluding direct tumor, infection and other structural causes.'),
  S('Investigate the Germ-Cell Association','**Arrange targeted testicular evaluation, including ultrasound when indicated**, with appropriate systemic oncologic assessment. A normal physical examination does not reliably exclude an occult lesion.',
    'Some patients may have a regressed or otherwise difficult-to-detect tumor, so expert interpretation and follow-up can be needed when initial imaging is unrevealing.',
    'Coordinate tumor treatment and specialist immune care without promising reversal of established neuronal injury. Assess swallowing, gait, hearing and communication needs early. Functional recovery can be limited despite control of the tumor, making rehabilitation and preservation of remaining function important outcomes. Confirm unexpected antibody results rather than assigning a testicular cancer solely from an unverified screening panel.')],['KLHL','PNS','PNSVALID'])

add('Paraneoplastic neurological syndromes','Repeat Screening in a High-Risk Combination',
 'A patient has a high-risk neurologic phenotype and a confirmed high-risk antibody. A comprehensive initial tumor search is negative. What repeat-screening schedule does the 2021 PNS consensus recommend for this combination?',
 'Repeat tumor screening every four to six months for two years',[
 ('Repeat tumor screening annually for ten years','Prolonged individualized follow-up can be needed in selected circumstances, but this is not the consensus schedule specified for the stated high-risk combination.'),
 ('Repeat tumor screening once after five years','An isolated late repeat would miss the recommended early surveillance period when a previously occult tumor may become detectable.'),
 ('Repeat screening only after a neurologic relapse','Relapse can prompt reassessment, but high-risk phenotype-antibody combinations warrant planned surveillance even without recurrent neurologic symptoms.')],
 [S('Apply the Schedule to the Right Population','**The 2021 PNS consensus recommends repeat screening every ==four to six months for two years==** after a negative initial investigation in patients with both high-risk phenotypes and high-risk antibodies.',
    'The schedule is risk-stratified. It should not be copied automatically to every isolated low-risk antibody result or every patient with nonspecific neurologic symptoms.',
    'Some additional situations warrant individualized surveillance according to demographic risk, antibody, phenotype and clinical evolution. Document the rationale rather than assuming one schedule is universal.'),
  S('Choose Investigations From the Expected Tumor Spectrum','**Repeat assessment should remain directed by the syndrome and antibody.** Review whether the initial studies adequately evaluated the relevant organs and whether another modality or specialist review is needed.',
    'Do not rely on normal tumor markers alone. Conversely, repeated low-yield whole-body testing without a clinical risk framework can create incidental findings and unnecessary procedures.',
    'Maintain neurologic treatment and rehabilitation while surveillance continues. A newly detected compatible tumor changes diagnostic confidence and treatment planning; a discordant tumor requires careful attribution rather than automatic PNS labeling. At the end of the planned period, reassess the clinical course and evidence instead of promising that no future cancer is possible.')],['PNS'],style='direct')

add('Paraneoplastic neurological syndromes','Cancer Does Not Make Every Neurologic Syndrome Paraneoplastic',
 'A patient with cancer and a prior immune neurologic diagnosis develops new multifocal radicular pain, cranial neuropathies and worsening gait. Which next approach is best?',
 'Reassess for direct cancer involvement, treatment toxicity, infection and metabolic causes before assigning immune relapse',[
 ('Increase immunosuppression because new neurologic symptoms establish PNS progression','An immune relapse is possible, but this pattern also raises direct leptomeningeal involvement and other actionable mechanisms that require targeted assessment.'),
 ('Use a persistent neural antibody as the principal discriminator of immune relapse','An antibody may persist and does not independently distinguish direct cancer spread, treatment injury or infection from renewed immune activity.'),
 ('Attribute the symptoms to chemotherapy and assess response after the next cycle','Treatment toxicity is relevant, but cranial and radicular progression can signal direct malignant or infectious involvement; continuing therapy without evaluation may delay appropriate care.')],
 [S('Reopen the Mechanism When the Pattern Changes','**A cancer patient can have several neurologic mechanisms over time.** Metastasis, leptomeningeal disease, coagulopathy, treatment toxicity, infection and metabolic disturbance can coexist with PNS.',
    'Define the new localization and tempo, review treatments and immune suppression, and select contrast imaging and safe CSF assessment according to the suspected process.',
    'A previous correct immune diagnosis does not guarantee that each later symptom has the same cause. New pain, cranial deficits or systemic features can change the priorities.'),
  S('Target Treatment to the Reassessed Cause','**Coordinate neurologic and oncology review**, using microbiology, cytology or other tests when indicated rather than treating the antibody as the endpoint of investigation.',
    'A negative initial cytology may need optimized repeat sampling when leptomeningeal suspicion remains; infection and bleeding risks influence procedure timing.',
    'Treat urgent threats and provide symptom support while evidence is assembled. Immune escalation can worsen an unrecognized infection and does not adequately treat direct malignant spread. Conversely, finding a treatment-related contributor does not automatically exclude simultaneous immune activity. Document the evidence for each proposed mechanism and reassess response against objective clinical findings.')],['PNS','CANADA','ASCO'])

add('Paraneoplastic neurological syndromes','Encephalitis During Checkpoint Inhibition',
 'A patient receiving a PD-1 inhibitor develops rapidly progressive confusion, seizures and reduced consciousness. MRI excludes metastasis or mass effect; infection remains under investigation. Which immediate strategy is most appropriate?',
 'Hold checkpoint treatment, arrange urgent specialist assessment and cover infection while treating supported severe immune encephalitis',[
 ('Continue checkpoint treatment and await neural antibodies before changing care','A severe suspected neurologic immune toxicity requires urgent assessment and interruption of the suspected trigger; antibody negativity or delay does not make continuation safe.'),
 ('Treat as brain metastasis with radiation despite negative structural assessment','Radiation treats demonstrated oncologic targets; an encephalitic syndrome without a corresponding lesion needs etiologic assessment rather than empirical cranial irradiation.'),
 ('Use antiseizure treatment alone and review at the next oncology visit','Seizure control is necessary, but severe encephalopathy during checkpoint therapy requires immediate evaluation for infection and immune toxicity, not routine delayed review.')],
 [S('Recognize a Treatment-Related Immune Emergency','**Checkpoint inhibitors can trigger encephalitis and other central or peripheral immune syndromes.** The temporal relationship supports suspicion but does not exclude infection or direct cancer involvement.',
    'Hold the agent and coordinate neurology, oncology and infectious assessment. Obtain appropriate MRI, EEG and CSF studies when safe, including relevant pathogen and neural antibody tests.',
    'Provide empiric antiviral treatment until a plausible viral encephalitis is adequately excluded. Stabilize airway, seizures and autonomic function without waiting for every result.'),
  S('Treat Severe Supported Disease and Reassess','**Guidelines support high-dose corticosteroids for severe immune encephalitis**, commonly methylprednisolone ==1 g IV daily for three to five days==, with IVIG or plasma exchange according to severity and response.',
    'A typical IVIG total is ==2 g/kg over five days==. Refractory disease may require further specialist treatment; recommendations and evidence strength vary by clinical setting.',
    'Monitor for infection and steroid complications and assess other immune toxicities. Decisions about permanent discontinuation or later rechallenge require individualized oncology-neurology discussion, especially after severe disease. A confirmed high-risk PNS antibody can indicate an overlapping triggered paraneoplastic process, but absence of antibodies does not exclude checkpoint-associated neurologic toxicity.')],['SITC','ASCO','PNS'])

R.update({
 'SLE':('EULAR SLE recommendations: 2023 update','https://doi.org/10.1136/ard-2023-224762'),
 'APS':('EULAR management of antiphospholipid syndrome, 2019','https://doi.org/10.1136/annrheumdis-2019-215213'),
 'BEHCET':('EULAR Behcet recommendations, 2018','https://doi.org/10.1136/annrheumdis-2018-213225'),
 'BEHCET24':('BAD/BSR Behcet living guideline, 2024','https://cdn.bad.org.uk/uploads/2024/09/10132850/Behcets-guideline.pdf'),
 'PACNS':('ESO guideline on primary CNS angiitis, 2023','https://doi.org/10.1177/23969873231190431'),
})

add('Systemic inflammatory neurological disorders','A Lupus Diagnosis Does Not Determine the Neurologic Mechanism',
 'A patient with SLE develops acute confusion while receiving glucocorticoids. Fever and a recent medication change are reported. Which first approach is most appropriate?',
 'Investigate infection, metabolic and drug-related causes while assessing whether inflammatory or thrombotic lupus disease is supported',[
 ('Escalate glucocorticoids because confusion in established SLE establishes inflammatory NPSLE','Inflammatory neuropsychiatric lupus can need immune treatment, but infection and drug or metabolic effects must be assessed before attributing this presentation to lupus activity.'),
 ('Begin anticoagulation because neuropsychiatric lupus is predominantly an APS manifestation','Thrombotic disease requires its own supporting evidence; confusion alone does not establish APS-related thrombosis or an anticoagulant indication.'),
 ('Attribute the syndrome to steroid psychiatric toxicity from the medication history','Steroids can cause psychiatric effects, but fever and acute confusion require broader assessment; one plausible medicine effect does not exclude infection or another neurologic process.')],
 [S('Establish Attribution Before Selecting Mechanism-Specific Treatment','**Neuropsychiatric symptoms in SLE have a broad differential.** Infection, metabolic derangement, medicines, primary psychiatric disease, vascular events and inflammatory lupus can overlap.',
    'Define the neurologic syndrome and tempo, examine for focal or meningeal findings, and select imaging, EEG and safe CSF studies as indicated. Systemic activity and serology contribute but do not independently prove CNS attribution.',
    'Assess aPL and vascular evidence when thrombosis is suspected rather than assuming every manifestation is inflammatory.'),
  S('Treat the Supported Mechanism','**EULAR distinguishes inflammatory manifestations from atherothrombotic or aPL-related disease.** Severe inflammatory syndromes may require glucocorticoids and potent immunosuppression under specialist care.',
    'Antiplatelet or anticoagulant treatment addresses appropriate thrombotic indications; it is not a substitute for immune treatment of supported inflammatory disease.',
    'Infection may be exacerbated by further immunosuppression, making early recognition particularly important in a febrile treated patient. Mixed mechanisms can require combined plans. Reassess attribution if the course or response diverges from expectations; an established SLE label should guide a careful differential rather than terminate it.')],['SLE','CANADA'])

add('Systemic inflammatory neurological disorders','Secondary Prevention After Arterial Thrombotic APS',
 'A patient has a documented ischemic stroke attributed to definite APS with persistent triple aPL positivity. After acute care, which long-term antithrombotic approach is best supported?',
 'A vitamin K antagonist strategy with intensity individualized to recurrence and bleeding risk',[
 ('Rivaroxaban as the preferred alternative because it avoids INR monitoring','Convenience does not outweigh evidence of increased arterial events in high-risk APS; rivaroxaban should not be used for this triple-positive arterial phenotype.'),
 ('Aspirin alone as the standard replacement for anticoagulation in definite arterial APS','Aspirin has primary and selected secondary prevention roles, but EULAR favors VKA over aspirin alone for definite APS with a first arterial thrombosis.'),
 ('Glucocorticoids alone to suppress the antibody-mediated thrombosis risk','Immune treatment has selected roles in associated inflammatory disease or catastrophic APS, but does not replace indicated long-term antithrombotic therapy after this arterial event.')],
 [S('Choose Therapy for the Thrombotic Phenotype','**Arterial APS and triple positivity represent a high-risk context.** Do not extrapolate DOAC convenience from ordinary atrial fibrillation or venous thrombosis to this population.',
    'EULAR recommends VKA for a first arterial thrombosis, with INR 2–3 or 3–4 selected according to individual bleeding and recurrence risk. VKA at INR 2–3 plus low-dose aspirin may be considered in selected cases.',
    'These are alternative specialist strategies, not a requirement to prescribe the highest intensity to everyone. Review other stroke mechanisms and conventional vascular risks as well.'),
  S('Manage Recurrence and Treatment Safety','**Check adherence, INR control, interactions and competing causes before labeling anticoagulant failure.** Selected recurrent events may prompt a higher target, added low-dose aspirin or LMWH.',
    'Balance bleeding risk, blood pressure, thrombocytopenia, falls and procedural needs. Explain monitoring and interactions and coordinate pregnancy-related planning when relevant.',
    'Persistent laboratory positivity must be interpreted within a valid clinical diagnosis; an isolated antibody does not imply the same treatment. Long-term prevention should address smoking, hypertension, lipids and mobility alongside anticoagulation rather than treating INR control as the entire stroke-prevention programme.')],['APS','SLE'])

add('Systemic inflammatory neurological disorders','Parenchymal and Venous Neuro-Behcet Require Different Assessment',
 'A patient with Behcet disease has a subacute brainstem syndrome and MRI evidence of parenchymal inflammation. Infection is reasonably excluded. Which treatment framework is most appropriate?',
 'High-dose glucocorticoids with a steroid-sparing immunosuppressant, with anti-TNF treatment considered for severe or refractory disease',[
 ('Cyclosporine as the preferred steroid-sparing agent because of prior ocular benefit','Cyclosporine can help selected ocular disease, but guidance advises avoiding it in patients with neurologic Behcet involvement because of neurologic risk.'),
 ('Anticoagulation alone using the cerebral venous thrombosis pathway','Venous thrombosis is a distinct neuro-Behcet mechanism; anticoagulation alone does not treat this demonstrated inflammatory parenchymal presentation.'),
 ('Colchicine alone as induction treatment for the brainstem syndrome','Colchicine helps selected mucocutaneous or joint manifestations, but is not adequate induction therapy for significant parenchymal neurologic involvement.')],
 [S('Define the Neurologic Pattern','**Parenchymal neuro-Behcet often involves brainstem or other CNS tissue**, while nonparenchymal disease includes cerebral venous thrombosis and related intracranial-pressure presentations.',
    'Choose MRI, venous imaging and CSF assessment according to the syndrome. Exclude infection and other mimics before attributing an enhancing lesion to Behcet.',
    'Thrombotic and inflammatory manifestations can coexist, so the clinical label does not eliminate the need to identify the current mechanism.'),
  S('Use Immune Treatment for Parenchymal Inflammation','**High-dose glucocorticoids with an agent such as azathioprine are recommended.** Severe disease or inadequate response can warrant anti-TNF therapy through specialist care.',
    'The EULAR example uses IV methylprednisolone 1 g daily for up to seven days, followed by oral prednisone/prednisolone around 1 mg/kg daily and a planned slow taper; tailor the regimen to severity and toxicity.',
    'Avoid cyclosporine in neurologic involvement even if it previously helped another organ. For venous disease, assess systemic vascular involvement and bleeding hazards, including aneurysm considerations, before an individualized antithrombotic plan. Monitor neurologic function, infection and treatment toxicity and coordinate rheumatology-neurology follow-up rather than treating all Behcet manifestations with one organ-independent regimen.')],['BEHCET','BEHCET24'])

add('Systemic inflammatory neurological disorders','Angiographic Beading Is Not Synonymous With CNS Vasculitis',
 'A patient has recurrent thunderclap headaches and multifocal intracranial arterial narrowing. CSF is nearly normal. Which next diagnostic principle is most appropriate before assigning primary CNS angiitis?',
 'Assess reversible vasoconstriction and other mimics using clinical, imaging and CSF evidence',[
 ('Use the angiographic beading as sufficient confirmation of inflammatory vasculitis','Beading can occur in RCVS and other arteriopathies; angiography alone is not specific enough to establish inflammatory CNS angiitis.'),
 ('Use near-normal CSF as definitive exclusion of every vasculitic process','CSF can shift probability and supports the differential, but a near-normal result does not independently exclude every presentation of CNS angiitis.'),
 ('Use an empirical steroid response as the decisive discriminator','Response is nonspecific and steroids are not a diagnostic reference standard; treatment before adequate assessment can obscure alternatives or expose a patient to inappropriate therapy.')],
 [S('Interpret the Vessel Pattern in Context','**Primary CNS angiitis is a diagnosis requiring exclusion of important mimics.** RCVS, atherosclerosis, infection, dissection and other vascular disorders can produce overlapping findings.',
    'Recurrent thunderclap headache and relatively bland CSF particularly raise RCVS. Review postpartum state, vasoactive exposures, systemic clues and the timing of vascular changes.',
    'MRI parenchymal findings, CSF and vascular imaging should be integrated; no single noninvasive test reliably answers every vessel-size phenotype.'),
  S('Escalate Diagnosis Thoughtfully','**Use expert neurologic and neuroradiologic review**, with catheter angiography or targeted biopsy selected according to the suspected pattern and remaining uncertainty.',
    'Small-vessel disease may be below angiographic resolution. Conversely, visible narrowing does not prove inflammation; a negative angiogram and a positive angiogram each have different limitations.',
    'Investigate infectious causes before immunosuppression and assess for systemic vasculitis when indicated. Follow the clinical and imaging evolution, including reversibility when RCVS is plausible. Avoid replacing this etiologic work with a prolonged steroid trial or labeling every multifocal ischemic lesion as PACNS; treatment consequences are substantial and evidence certainty should remain explicit.')],['PACNS'])

R.update({
 'SARCOID':('Neurosarcoidosis Consortium diagnostic consensus, 2018','https://pubmed.ncbi.nlm.nih.gov/30167654/'),
 'NSREVIEW':('Neurosarcoidosis: pathophysiology, diagnosis and treatment, 2021','https://doi.org/10.1212/NXI.0000000000001084'),
 'SJOGREN':('Neurological complications of Sjogren syndrome: diagnosis and management','https://pmc.ncbi.nlm.nih.gov/articles/PMC6322693/'),
 'THYROID':('Brain dysfunction and thyroid antibodies: diagnosis and misdiagnosis, 2021','https://pubmed.ncbi.nlm.nih.gov/34061124/'),
})

add('Systemic inflammatory neurological disorders','A Negative Angiogram Does Not Exclude Small-Vessel PACNS',
 'A patient has progressive cognitive and focal neurologic dysfunction, inflammatory CSF and multifocal enhancing lesions. Catheter angiography is normal. Infection and malignancy remain under assessment. Which next principle is most appropriate?',
 'Consider small-vessel disease and the role of targeted tissue assessment after expert review of mimics',[
 ('Exclude CNS angiitis because catheter angiography is the definitive test for all vessel sizes','Angiography cannot resolve every small-vessel process; a normal result does not exclude small-vessel PACNS when other evidence warrants further evaluation.'),
 ('Diagnose small-vessel PACNS from inflammatory CSF alone','CSF inflammation is nonspecific and occurs with infection, malignancy and other immune disorders; it cannot independently establish angiitis.'),
 ('Begin indefinite immune treatment and use improvement instead of tissue or further exclusion work','Empiric treatment may occasionally be necessary in urgent circumstances, but response is not specific and should not replace a feasible plan to resolve important mimics.')],
 [S('Tests Sample Different Parts of the Disease','**Catheter angiography and biopsy have complementary limitations.** Angiography evaluates visible vessel lumina, while small-vessel inflammation may lie below its resolution.',
    'Biopsy can demonstrate vasculitis or uncover an alternative diagnosis, but a negative specimen does not exclude patchy disease. Target selection and inclusion of relevant tissue influence yield.',
    'MRI, CSF and clinical tempo help choose the next investigation. Vessel-wall imaging can contribute in selected settings but is not an independent universal confirmation test.'),
  S('Seek Diagnostic Confidence Before Prolonged Toxic Therapy','**Review the case in an experienced multidisciplinary setting**, considering targeted biopsy when its expected benefit justifies procedural risk.',
    'Exclude infection, lymphoma and other inflammatory or vascular mimics. Where tissue is planned, discuss prior treatment effects and sampling strategy with the procedural and pathology teams.',
    'Urgent clinical deterioration may require treatment before every uncertainty is settled, but document that rationale and continue diagnostic reassessment. Do not interpret either a negative angiogram or a nondiagnostic biopsy in isolation. The decision to expose a patient to prolonged immunosuppression should reflect converging evidence, response assessed objectively and a continuing search for an alternative when the course is atypical.')],['PACNS'])

add('Systemic inflammatory neurological disorders','Systemic Tissue Can Support Probable Neurosarcoidosis',
 'A patient has basilar meningeal enhancement, multiple cranial neuropathies and mediastinal lymphadenopathy. An accessible lymph node biopsy shows non-necrotizing granulomas; infection and malignant mimics have been reasonably excluded. Which classification is best supported by the 2018 consensus?',
 'Probable neurosarcoidosis in the compatible neurologic setting',[
 ('Definite neurosarcoidosis because extraneural granulomas prove neural infiltration','Extraneural pathology supports systemic sarcoidosis and probable neurologic attribution; definite neurosarcoidosis requires appropriate neural tissue evidence within the consensus framework.'),
 ('Possible neurosarcoidosis only, because a brain biopsy is mandatory for probable disease','Probable disease can be supported by nonneural biopsy in a compatible syndrome with exclusions; neural biopsy is not required merely to reach that category.'),
 ('An incidental systemic granulomatous disorder with no basis for neurologic attribution','Coincidence remains a consideration, but the compatible meningeal/cranial pattern and exclusion work provide a basis for probable attribution rather than automatic separation.')],
 [S('Match Pathology to the Level of Certainty','**Probable neurosarcoidosis combines a compatible neurologic presentation with systemic tissue evidence**, after rigorous exclusion of other causes.',
    'Definite disease requires neural tissue confirmation. Possible disease lacks the pathologic confirmation required for the higher categories while retaining a compatible evaluated syndrome.',
    'Granulomas are not uniquely sarcoid. Tuberculosis, fungi and other causes must be assessed according to exposure, immune status and tissue findings.'),
  S('Choose Tissue and Treatment With Procedural Risk in Mind','**Accessible extraneural tissue can avoid an unnecessary high-risk neural biopsy.** Select lymph node, lung, skin or another target according to the actual disease distribution.',
    'Serum ACE and characteristic MRI enhancement can support suspicion but do not replace tissue or exclude infection and malignancy.',
    'Once supported, treatment intensity follows neurologic severity and organ involvement, commonly using glucocorticoids with steroid-sparing treatment when indicated. Monitor visual, pituitary, meningeal and other involved functions directly. Unexpected progression should reopen the differential rather than trigger automatic immune escalation; a probable classification reflects strong integrated evidence with an acknowledged limitation, not proof that every later symptom is granulomatous infiltration.')],['SARCOID','NSREVIEW'])

add('Systemic inflammatory neurological disorders','Sjogren Ganglionopathy Can Lack Anti-SSA',
 'A patient has severe sensory ataxia with asymmetric, non-length-dependent sensory loss and reduced sensory responses. Dry eyes and mouth are reported, but anti-SSA and anti-SSB are negative. Which next interpretation is most appropriate?',
 'Sjogren-associated ganglionopathy remains possible and warrants objective glandular and neurologic assessment',[
 ('Negative anti-SSA and anti-SSB exclude Sjogren as the cause','Some neurologic Sjogren phenotypes lack these antibodies; seronegativity does not replace objective assessment when the phenotype and sicca history are suggestive.'),
 ('The findings establish a distal length-dependent axonal polyneuropathy','A non-length-dependent, asymmetric sensory pattern with severe proprioceptive ataxia suggests sensory neuronopathy rather than the usual distal gradient.'),
 ('Sicca symptoms alone establish the autoimmune cause of the neuronopathy','Sicca can be medication-related or have other causes; objective glandular assessment and evaluation of competing neuronopathy etiologies are needed.')],
 [S('Identify the Sensory Neuronopathy Pattern','**Sjogren can cause several peripheral neurologic phenotypes**, including small-fiber neuropathy, distal axonal neuropathy, sensory ganglionopathy and vasculitic neuropathy.',
    'Ganglionopathy can affect arms, trunk or proximal areas early and cause marked position-sense loss, pseudoathetosis and sensory ataxia. Motor strength may be relatively preserved.',
    'The phenotype differs from painful small-fiber disease, where routine sensory nerve conduction may remain normal; electrophysiology helps define which fibers and structures are involved.'),
  S('Confirm Systemic Attribution and Exclude Alternatives','**Use objective ocular/salivary assessment and specialist consideration of gland biopsy when appropriate.** Neurologic presentations can occur without the usual serologic markers.',
    'Review paraneoplastic disease, toxins, nutritional causes and other immune or inherited neuronopathies. Sicca symptoms should be assessed rather than assumed to prove the etiology.',
    'Treatment depends on whether the process is ganglionopathic, vasculitic or another phenotype; evidence for many immune regimens is limited. Provide falls prevention, physiotherapy, pain and autonomic care as indicated. A confirmed systemic diagnosis does not eliminate other contributors, and a negative screening antibody should not close a clinically justified evaluation.')],['SJOGREN','PNS'])

add('Systemic inflammatory neurological disorders','Thyroid Antibodies Do Not Confirm Immune Encephalopathy',
 'A patient with insomnia and subjective cognitive symptoms has high anti-TPO antibodies and stable thyroid replacement. MRI, EEG and CSF reveal no supportive CNS abnormalities. Which approach is most appropriate?',
 'Assess objective neurologic dysfunction and alternative causes before assigning steroid-responsive autoimmune encephalopathy',[
 ('Use the anti-TPO level as sufficient confirmation of autoimmune encephalitis','Thyroid antibodies are common in thyroid autoimmunity and can occur in otherwise healthy people; their level does not independently establish CNS immune disease.'),
 ('Use an empirical steroid-related increase in energy as the decisive confirmation','Steroids can produce nonspecific changes in energy and mood; subjective benefit without objective syndrome evidence is not a reliable diagnostic reference standard.'),
 ('Repeat thyroid antibodies until they normalize before reassessing cognition','Antibody normalization is not the neurologic treatment endpoint and repeated titres do not replace evaluation of sleep, medicines, endocrine status and objective cognition.')],
 [S('Separate Thyroid Autoimmunity From CNS Attribution','**Anti-TPO and thyroglobulin antibodies indicate thyroid autoimmunity, not a specific encephalitis mechanism.** Positivity can be incidental to a neurologic or psychiatric complaint.',
    'Assess thyroid hormone status because endocrine dysfunction itself can affect cognition and mood. Euthyroidism does not establish or exclude a separate neurologic disorder.',
    'The historical steroid-responsive encephalopathy label requires careful exclusion and a compatible objective syndrome; it should not be assigned to nonspecific symptoms from the antibody result alone.'),
  S('Use Objective Findings and Reassessment','**Document the cognitive, neurologic and functional changes**, and investigate medicines, sleep, mood, metabolic disease, seizures and other causes according to context.',
    'Normal routine studies do not exclude every autoimmune syndrome, but absent supportive findings combined with a nonspecific phenotype lowers confidence and makes automatic immunotherapy inappropriate.',
    'If a convincing encephalitic syndrome evolves, reassess with appropriate targeted tests rather than relying on thyroid titres. The 144-case referral study found many alternative diagnoses, illustrating the risk of overattribution rather than providing a universal exclusion rule. Treatment should address the demonstrated mechanism and use objective outcomes when an immune trial is justified.')],['THYROID','CANADA','MISDX'])

R.update({
 'SPSDX':('Stiff-person spectrum diagnosis, misdiagnosis and proposed criteria, 2023','https://pubmed.ncbi.nlm.nih.gov/37212351/'),
 'SPSIVIG':('Randomized crossover trial of IVIG in stiff-person syndrome, 2001','https://doi.org/10.1056/NEJMoa01167'),
 'PERM':('Glycine receptor antibodies in PERM and related syndromes, 2014','https://pubmed.ncbi.nlm.nih.gov/24951641/'),
})

add('Immune hyperexcitability and selected systemic mimics','Stiffness With Stimulus-Triggered Spasms',
 'A patient has progressive axial stiffness, lumbar hyperlordosis and painful spasms triggered by unexpected sound or touch. Strength and sensation are otherwise preserved. Which investigation most directly supports the suspected stiff-person physiology?',
 'EMG assessment for continuous motor unit activity and abnormal agonist-antagonist coactivation',[
 ('Routine sensory nerve conduction to identify a distal sensory axonopathy','Sensory conduction helps assess neuropathy, but a distal sensory lesion does not explain the axial stiffness and stimulus-sensitive spasms; targeted muscle electrophysiology is more informative.'),
 ('Repetitive nerve stimulation to demonstrate a postsynaptic decrement','A decrement supports selected neuromuscular-junction disorders with fatigability; it does not directly assess the continuous motor activation of the suspected syndrome.'),
 ('Serum CK measurement to confirm inflammatory muscle injury','CK helps assess myopathy, but stiff-person physiology is not established by an enzyme elevation; the clinical and electrophysiologic activation pattern is the relevant target.')],
 [S('Recognize the Clinical Pattern','**Stiff-person spectrum disease can cause axial or limb stiffness and stimulus-sensitive painful spasms.** Hyperlordosis, exaggerated startle and unexplained falls can support suspicion.',
    'Assess for pyramidal, extrapyramidal, muscle, structural and functional alternatives. The presence of anxiety or fear of falling neither establishes nor excludes the neurologic syndrome.',
    'EMG can demonstrate continuous motor unit activity, including in relevant paraspinal muscles, and abnormal coactivation. Sampling and medicines that suppress activity can influence findings.'),
  S('Combine Physiology and Immune Evidence','**GAD65, glycine-receptor or other antibody findings must fit the phenotype.** A low-positive serum GAD65 result alone is not sufficient confirmation.',
    'Some presentations have additional brainstem or autonomic involvement and require a broader spectrum diagnosis and monitoring. An isolated stiff-limb presentation can differ from classical axial disease.',
    'No single universally accepted criterion set resolves every case. Use specialist clinical and electrophysiologic review before prolonged immunotherapy, especially when findings are discordant. Document objective stiffness, spasm triggers, gait and functional limitations so that treatment response can be distinguished from nonspecific subjective benefit and medication-related sedation.')],['SPSDX','GAD'])

add('Immune hyperexcitability and selected systemic mimics','Disabling Stiff-Person Disease Despite Symptomatic Therapy',
 'A patient with well-supported GAD65-associated stiff-person syndrome remains disabled by stiffness and spasms despite tolerated diazepam and baclofen. Which immune treatment has randomized trial evidence in this setting?',
 'Intravenous immunoglobulin',[
 ('Chronic high-dose glucocorticoid monotherapy as the best-established randomized option','Steroids have selected immune indications, but the landmark placebo-controlled stiff-person trial established evidence for IVIG rather than chronic high-dose steroid monotherapy.'),
 ('Cyclophosphamide as the preferred trial-proven initial immune treatment','Cyclophosphamide has selected refractory immune uses, but its toxicity and evidence do not make it the standard initial trial-supported choice in this scenario.'),
 ('Rituximab as a universally effective replacement for symptomatic treatment','Rituximab may help selected refractory patients, but responses are variable and it is not a universally effective substitute for symptomatic therapy or the trial-supported IVIG option asked here.')],
 [S('Combine Symptom Control With an Objective Immune Trial','**Diazepam and baclofen can reduce spasms through inhibitory pathways**, but sedation, falls and weakness can limit escalation. Do not increase them without assessing useful function.',
    'IVIG has placebo-controlled crossover evidence in a small GAD65-positive stiff-person cohort. The study used 2 g/kg per month, divided over two days, for three monthly treatment periods.',
    'In clinical practice the total dose can be divided over additional days according to tolerance and local protocol. Trial benefit does not establish that every stiff-person phenotype will respond.'),
  S('Measure Benefit and Treatment Burden','**Set outcomes for stiffness, spasm frequency, gait and daily function before treatment.** Reassess whether objective benefit persists and whether ongoing maintenance is justified.',
    'Review renal function, thrombosis and fluid risks before IVIG and monitor infusion reactions and other adverse effects. Dose and interval should reflect the individual response and safety profile.',
    'Rehabilitation and trigger management complement treatment. If response is poor, revisit diagnostic confidence, adherence and competing limitations before adding successive immune agents. Avoid abrupt withdrawal of established baclofen or benzodiazepines; a supervised medication plan reduces withdrawal and rebound risk while preserving safe mobility.')],['SPSIVIG','SPSDX','GAD'],style='direct')

add('Immune hyperexcitability and selected systemic mimics','Rigidity With Brainstem and Autonomic Dysfunction',
 'A patient develops subacute generalized rigidity, stimulus-sensitive myoclonus, dysphagia, eye-movement abnormalities and autonomic instability. Which antibody-associated syndrome deserves particular consideration?',
 'Glycine-receptor-associated PERM',[
 ('Classical isolated GAD65 stiff-person syndrome','Classical stiff-person disease explains stiffness and spasms, but prominent brainstem and autonomic involvement with myoclonus suggests the broader PERM phenotype.'),
 ('Isolated acquired neuromyotonia','Neuromyotonia causes peripheral muscle hyperexcitability, but does not adequately integrate central brainstem abnormalities and the full rigidity-myoclonus syndrome.'),
 ('DPPX-associated encephalitis','DPPX can cause startle and central hyperexcitability, especially after diarrhea and weight loss; the brainstem-rigidity-autonomic pattern here particularly raises PERM.')],
 [S('A Severe Stiff-Person Spectrum Phenotype','**Progressive encephalomyelitis with rigidity and myoclonus combines hyperexcitability with additional CNS involvement.** Brainstem, bulbar and autonomic features distinguish it from a limited stiffness syndrome.',
    'Glycine-receptor antibodies are strongly associated, but testing must be interpreted in the clinical context and with appropriate laboratory confirmation.',
    'Evaluate infection, toxins and other mimics, including tetanus where exposure and examination warrant it. The presence of rigidity does not by itself establish an autoimmune cause.'),
  S('Protect Airway and Autonomic Function','**Assess swallowing, ventilation and hemodynamic instability urgently.** Severe disease can require ICU support while diagnostic work and immune treatment proceed.',
    'Specialist treatment may combine symptomatic antispasm measures with corticosteroids, IVIG or plasma exchange, selected by severity and contraindications. Evidence is largely observational and response varies.',
    'Investigate associated malignancy according to the phenotype and antibody context and monitor for treatment complications. Recovery can be meaningful, but immune response is not guaranteed; follow bulbar function, mobility and autonomic stability separately. A patient whose visible spasms improve can still require respiratory or nutritional support, so symptom reduction should not be used alone to justify lower monitoring intensity.')],['PERM','SPSDX','CANADA'])

R.update({
 'SUSAC':('European Susac Consortium diagnostic criteria, 2016','https://pubmed.ncbi.nlm.nih.gov/28103199/'),
 'SUSAC18':('Susac syndrome diagnostic criteria and treatment algorithm, 2018','https://pubmed.ncbi.nlm.nih.gov/29933288/'),
 'PORPH':('AGA clinical practice update: acute hepatic porphyrias, 2023','https://pmc.ncbi.nlm.nih.gov/articles/PMC10335308/'),
 'WILSON':('EASL-ERN clinical practice guideline on Wilson disease, 2025','https://www.journal-of-hepatology.eu/article/S0168-8278(24)02706-5/fulltext'),
})

add('Immune hyperexcitability and selected systemic mimics','A Brain-Eye-Ear Microangiopathy',
 'A young adult has headache, cognitive change and new hearing difficulty. MRI shows central corpus-callosum lesions. Which targeted assessment best evaluates suspected Susac syndrome?',
 'Retinal fluorescein angiography and formal audiometry alongside neurologic MRI review',[
 ('Optic-nerve MRI and visual evoked potentials as the principal ocular assessment','These tests can help optic neuropathy or demyelination, but Susac ocular disease concerns retinal arterioles; retinal vascular imaging is the targeted examination.'),
 ('AQP4-IgG testing as the confirmatory investigation for the callosal lesions','AQP4 testing is appropriate for compatible NMOSD phenotypes, but central callosal lesions with hearing symptoms should prompt retinal and cochlear evaluation rather than an antibody-only attribution.'),
 ('Catheter cerebral angiography as the primary test for retinal and cochlear involvement','Angiography has selected vascular roles, but does not replace targeted retinal fluorescein imaging and audiometry for the small-vessel organ pattern suspected here.')],
 [S('Assess All Three Organ Domains','**Susac syndrome is an immune-mediated microangiopathy involving brain, retina and inner ear.** Encephalopathy, branch retinal artery occlusions and sensorineural hearing loss form the characteristic triad.',
    'The full triad may not be apparent at first presentation. Test apparently asymptomatic organs when the overall pattern is suggestive rather than waiting for major visual or auditory disability.',
    'Central callosal lesions are useful MRI clues; their presence is not by itself a complete diagnosis or a reason to omit competing infectious, vascular and inflammatory assessment.'),
  S('Use Targeted Tests and Protect Function','**Fluorescein angiography can identify retinal artery occlusions or arteriolar wall hyperfluorescence.** Formal audiometry documents the sensorineural hearing pattern and provides a monitoring baseline.',
    'Coordinate neurology, ophthalmology and audiology assessment. The ocular lesion is retinal ischemia rather than the typical optic neuritis of a demyelinating pathway.',
    'Early specialist immune treatment aims to prevent further organ injury, with intensity individualized to severity and course; evidence is largely expert consensus and observational. Monitor cognition, retinal activity and hearing separately, because improvement in one domain does not establish remission in the others. Provide rehabilitation and hearing or visual support for residual impairment.')],['SUSAC','SUSAC18'])

add('Immune hyperexcitability and selected systemic mimics','A Neurovisceral Attack Needs Biochemical Testing',
 'A patient has recurrent severe abdominal pain without a structural explanation, tachycardia, hyponatremia and new motor-predominant weakness. Acute hepatic porphyria is suspected. Which initial test is most appropriate during symptoms?',
 'A random urine sample for ALA, PBG and creatinine before hemin when feasible',[
 ('A genetic panel as the sole initial confirmation of the current attack','Genetic testing helps identify the subtype after biochemical assessment, but a variant alone does not establish that the current symptoms reflect an active neurovisceral attack.'),
 ('Urinary total porphyrins alone without precursor or creatinine measurement','Porphyrin increases can be secondary and nonspecific; the recommended acute evaluation measures ALA and PBG with creatinine normalization.'),
 ('A 24-hour urine collection before any treatment decision','A random sample with appropriate normalization is the recommended initial approach; waiting for a complete collection can unnecessarily delay assessment and treatment of a severe attack.')],
 [S('Recognize Autonomic, Visceral and Neurologic Involvement','**Acute hepatic porphyrias can cause neurovisceral attacks**, with abdominal pain, autonomic disturbance, psychiatric or encephalopathic symptoms and motor neuropathy.',
    'Collect urine ALA, PBG and creatinine during symptoms, preferably before hemin. Creatinine normalization helps interpretation of a dilute sample.',
    'PBG is elevated in the usual acute attacks except ALAD-deficiency porphyria; isolated ALA elevation has a different differential, including lead-related and other metabolic causes. Confirm the biochemical pattern before subtype genetics.'),
  S('Treat Severe Attacks and Remove Triggers','**Hospitalized severe attacks generally warrant IV hemin**, commonly ==3–4 mg/kg daily for four days==, with specialist and product-specific prescribing.',
    'Review porphyrogenic medicines and triggers, provide nutrition and appropriate analgesia, and correct electrolyte abnormalities safely. Carbohydrate support is not an adequate substitute for hemin in a severe neurologic attack.',
    'Assess respiratory muscle function when motor weakness develops and select medicines from an authoritative porphyria safety resource. Arrange long-term specialist care after biochemical confirmation, including recurrence prevention where indicated. Do not attribute all later abdominal or neurologic symptoms to porphyria without reassessment, even after a genetic diagnosis is established.')],['PORPH'])

add('Immune hyperexcitability and selected systemic mimics','Normal Ceruloplasmin Does Not End a Wilson Evaluation',
 'A young adult has new dystonia, tremor, behavioral change and unexplained liver-test abnormalities. Ceruloplasmin is within the laboratory range. Which next approach is most appropriate?',
 'Continue integrated Wilson evaluation with slit-lamp examination, copper studies and further testing as indicated',[
 ('Exclude Wilson disease because ceruloplasmin is normal','Ceruloplasmin is a useful but imperfect marker; a normal result does not exclude Wilson disease when the neurologic and hepatic phenotype is suggestive.'),
 ('Use total serum copper alone as the confirmatory test','Total serum copper is influenced by ceruloplasmin and other factors and cannot independently establish or exclude Wilson disease.'),
 ('Diagnose autoimmune basal-ganglia disease from the movement phenotype','Immune disease can enter the differential, but a young patient with movement, behavioral and hepatic findings requires an appropriate copper-disorder evaluation rather than premature attribution.')],
 [S('Use Converging Evidence','**Wilson disease can combine hepatic, psychiatric and movement manifestations.** Kayser-Fleischer rings, ceruloplasmin, urinary copper and genetic or selected tissue findings contribute to diagnosis.',
    'Ceruloplasmin may be low for reasons other than Wilson disease and may be normal in affected individuals. Interpret the result within the phenotype rather than as a binary screening gate.',
    'Obtain a properly collected basal 24-hour urinary copper and appropriate slit-lamp assessment. Collection problems, liver disease and treatment status can affect copper interpretation.'),
  S('Interpret Thresholds Within the Diagnostic Framework','**Urinary copper above 100 micrograms per 24 hours is a strong clue in symptomatic untreated adults**, but lower values do not exclude every case and an elevated value is not uniquely diagnostic.',
    'Use an established integrated framework, including ATP7B analysis and further specialist testing when results are discordant. Assess hepatic severity and family-screening needs once the diagnosis is supported.',
    'Treatment requires sustained specialist copper-directed management and monitoring; neurologic worsening can occur with treatment initiation and requires careful planning. Do not offer a short empiric chelator trial as a diagnostic substitute. Follow liver function, copper indices and neurologic response together, and explain the importance of adherence and avoiding unsupervised discontinuation.')],['WILSON'])

def revise(title,answer=None,others=None,table=None):
    r=next(r for r in rows if r['title']==title)
    if answer is not None:r['answer']=answer
    if others is not None:r['others']=others
    if table is not None:r['table']=table

revise('Choose the Specimen as Carefully as the Antibody',answer='Obtain CSF IgG GluN1 testing with paired serum/CSF interpretation',others=[
 ('Repeat serum IgG GluN1 testing using another assay before considering CSF','A second assay can resolve an unexpected result, but a strongly compatible NMDAR syndrome warrants CSF testing because serum alone can be negative.'),
 ('Obtain CSF total IgG index and use it as the specific confirmatory test','An IgG index can support intrathecal immune activity, but is not antigen-specific and cannot replace CSF GluN1 IgG testing for this syndrome.'),
 ('Obtain serum IgM and IgA NMDAR antibodies to improve diagnostic sensitivity','Other antibody classes have been reported in different contexts, but the established encephalitis association concerns IgG GluN1; substituting classes can mislead attribution.')])
revise('A Positive Panel Does Not Establish the Mechanism',others=[
 ('Begin a monitored IVIG trial and use objective cognition as its endpoint','An objective treatment trial can be appropriate in sufficiently supported immune disease, but this weak phenotype-incongruent result first requires confirmation and reassessment of alternatives.'),
 ('Repeat serum CASPR2 titres and treat if the result remains positive','Repeat testing may clarify reproducibility, but persistent weak positivity does not independently establish that the symptoms arise from CASPR2 autoimmunity.'),
 ('Obtain FDG-PET as the decisive confirmation of autoimmune encephalitis','PET can contribute in selected unresolved cases, but nonspecific metabolic abnormalities cannot resolve an incongruent antibody result or replace the clinical diagnostic framework.')])
revise('Exclude Infection Before an Immune Attribution',others=[
 ('Begin IVIG while using repeat MRI to determine whether antiviral coverage is needed','IVIG can treat supported immune disease, but repeat imaging cannot safely gate prompt antiviral treatment in a plausible acute HSV presentation.'),
 ('Obtain CSF neural antibodies first and reserve pathogen testing for a negative panel','A sequential antibody-first strategy can delay a time-sensitive infection diagnosis; infection and immune testing should proceed together when both are plausible.'),
 ('Use CSF cell count and protein to choose exclusively between antiviral and immune treatment','Routine CSF findings overlap and do not reliably establish one mechanism; targeted pathogen tests, clinical context and appropriate empiric cover remain necessary.')])
revise('Antibody-Independent Definite Limbic Encephalitis',answer='Definite autoimmune limbic encephalitis',others=[
 ('Possible autoimmune encephalitis only','The possible category is appropriate before higher-certainty criteria are met; the bilateral restricted limbic MRI, temporal EEG support and exclusions permit definite limbic classification here.'),
 ('Probable antibody-negative autoimmune encephalitis','This category addresses cases outside well-defined autoimmune syndromes; the patient already meets the defined antibody-independent definite limbic framework.'),
 ('Definite paraneoplastic limbic encephalitis','A paraneoplastic mechanism requires relevant cancer and integrated PNS evidence; a limbic syndrome does not independently establish that association.')])
revise('EEG Supports the Syndrome and Detects Treatable Seizures',others=[
 ('Attribute the episodes to the encephalopathy and follow with routine EEG at discharge','Encephalopathy can cause fluctuations, but a short recording may miss intermittent seizures; persistent clinical concern warrants timely longer monitoring rather than delayed reassessment.'),
 ('Escalate antiseizure treatment solely to normalize diffuse slowing','Diffuse slowing reflects nonspecific dysfunction and is not itself an ictal target; treatment escalation should address seizures or another defined indication.'),
 ('Use the background slowing as the principal evidence for immune escalation','Slowing can help characterize dysfunction, but infection, medicines and metabolic causes also produce it; immune escalation needs the integrated disease assessment.')])
revise('Tumor Assessment Accompanies NMDAR Confirmation',answer='Obtain targeted pelvic imaging and plan risk-informed follow-up',others=[
 ('Repeat abdominal CT after neurologic recovery before obtaining pelvic imaging','Interval systemic imaging can have a role, but a young woman with confirmed NMDAR disease needs adequate targeted ovarian assessment during the current evaluation.'),
 ('Obtain chest imaging first and reserve ovarian assessment for persistent disease','Chest investigation can be part of a broader search, but the characteristic age/sex-specific ovarian association warrants targeted assessment without waiting for refractory disease.'),
 ('Use whole-body FDG-PET as the definitive exclusion of an ovarian teratoma','PET can assist selected cancer investigations, but cannot be treated as a definitive substitute for appropriate pelvic structural assessment of a suspected teratoma.')])
revise('Faciobrachial Events Before Memory Decline',others=[
 ('Optimize antiseizure treatment first and defer immune therapy until cognitive impairment appears','Antiseizure drugs may help events, but observational evidence supports treating the immune process early rather than waiting for memory decline in a supported LGI1 phenotype.'),
 ('Obtain prolonged video-EEG before beginning the neural antibody investigation','Video-EEG can characterize events, but a clear scalp correlate may be absent in FBDS; antibody and specialist immune evaluation should proceed rather than depend on EEG capture.'),
 ('Use interval MRI to confirm hippocampal injury before considering immune treatment','MRI follow-up can be useful, but a normal early scan does not exclude LGI1-associated FBDS or justify waiting for structural injury before assessment and treatment.')])
revise('Hyponatremia Can Be a Clue Rather Than the Whole Diagnosis',others=[
 ('Correct sodium first and defer neural antibody testing until cognition is reassessed','Electrolyte care is essential, but the focal seizures and limbic pattern warrant parallel etiologic testing rather than waiting to see whether sodium explains everything.'),
 ('Prioritize GABA-B receptor encephalitis because hyponatremia specifically identifies SCLC','GABA-B disease and SCLC can cause this combination, but sodium is nonspecific; the older-adult limbic syndrome also strongly warrants LGI1 assessment.'),
 ('Prioritize a degenerative memory disorder with superimposed metabolic seizures','A degenerative disorder can coexist with metabolic illness, but the subacute limbic course and focal seizures require evaluation for a treatable inflammatory syndrome.')])
revise('AMPAR Disease Needs Tumor and Relapse Assessment',others=[
 ('Repeat cancer imaging only if a clinical relapse occurs','Relapse should prompt reassessment, but the important tumor association warrants completing an adequate initial investigation rather than making cancer evaluation dependent on recurrence.'),
 ('Schedule prolonged maintenance therapy using antibody titres as the main endpoint','Maintenance can be appropriate in selected courses, but requires clinical risk-benefit assessment; titres alone do not establish the need, duration or remission.'),
 ('Limit tumor imaging to the pelvis and follow the NMDAR teratoma pathway','Pelvic evaluation may be relevant in a broader search, but AMPAR disease has a different tumor spectrum, including breast, lung and thymic tumors that must inform assessment.')])
revise('GAD65 Results Require Assay and Phenotype Context',others=[
 ('Use repeat serum titre progression as the main criterion for neurologic attribution','Serial titres can contribute in established disease, but changing levels alone do not identify a neurologic syndrome when objective clinical findings are absent.'),
 ('Use CSF oligoclonal bands as sufficient confirmation of GAD65-mediated disease','Bands can support CNS immune activity in an appropriate setting, but are not GAD65-specific and cannot establish the mechanism without a compatible syndrome.'),
 ('Apply a published high-titre cutoff directly after changing its numerical units','Thresholds depend on assay calibration and methodology, not just arithmetic unit conversion; an unrelated platform cutoff cannot independently confirm neurologic GAD65 autoimmunity.')])

revise('An Evolving NMDAR Syndrome',table=(['Antibody','High-yield phenotype','Important association or test clue'],[
 ['NMDAR','Psychiatric/speech change, seizures, dyskinesias, dysautonomia','CSF IgG GluN1; ovarian teratoma in relevant patients'],
 ['LGI1','Limbic amnesia, focal seizures, FBDS','Hyponatremia; routine CSF may be bland'],
 ['CASPR2','Limbic disease or peripheral hyperexcitability/Morvan','Insomnia and dysautonomia; selected thymoma association'],
 ['GABA-B receptor','Seizure-predominant limbic disease, possible status','Important SCLC association'],
 ['AMPAR','Limbic cognitive/psychiatric syndrome','Lung, breast and thymic tumors; relapse can occur']]))
revise('Probable Antibody-Negative Disease Requires Positive Evidence',table=(['Objective evidence category','Qualifying findings','Counting rule'],[
 ['MRI','Abnormalities suggesting autoimmune encephalitis','One category'],
 ['CSF','Pleocytosis, CSF-specific bands or elevated IgG index','Multiple CSF markers still count as one category'],
 ['Brain biopsy','Inflammatory infiltrates with another disorder excluded','One category; not mandatory in every case'],
 ['Required total','At least two categories plus the remaining clinical/exclusion criteria','Negative antibodies alone do not qualify']]))

revise('Select a First-Line Regimen for Severe Disease',answer='Pulse IV methylprednisolone plus IVIG or plasma exchange',others=[
 ('Pulse IV methylprednisolone alone as the planned complete induction course','Steroid monotherapy can be considered in selected mild or moderate disease, but the Canadian consensus recommends combination first-line therapy for severe disease.'),
 ('IV rituximab as the sole initial induction treatment','Rituximab is a preferred second-line option for many surface-antibody syndromes, but does not replace the rapid first-line combination recommended in this scenario.'),
 ('Oral prednisone with azathioprine as the initial induction combination','Oral steroid and azathioprine combinations can have maintenance roles, but delayed-onset azathioprine does not supply the acute severe-disease induction effect sought here.')])
revise('Escalation Timing Depends on Severity and Guideline',others=[
 ('Continue first-line treatment and defer the second-line decision until week four','A two-to-four-week interval appears in other guidance or less severe settings, but this question specifies the Canadian severe-disease recommendation supporting assessment at five to ten days.'),
 ('Repeat IVIG and make escalation dependent on a falling serum antibody titre','Additional first-line treatment can be selected, but a titre fall is not a prerequisite for escalation when a severe, well-supported syndrome fails to improve.'),
 ('Prefer cyclophosphamide as the next agent for this surface-antibody syndrome','Cyclophosphamide has selected refractory or cell-mediated immune indications, but rituximab is generally preferred for NMDAR disease in the cited consensus.')])
revise('HBsAg Alone Is Not Adequate Before Rituximab',others=[
 ('Proceed with rituximab and monitor liver enzymes without a virologic prevention plan','Liver monitoring is useful, but negative HBsAg does not remove reactivation risk from prior infection and enzyme surveillance alone is inadequate high-risk planning.'),
 ('Defer rituximab until anti-HBc becomes negative on repeat serology','Anti-HBc can remain positive after prior infection; waiting for seroreversion is not the appropriate safety endpoint when expert antiviral prevention can enable necessary treatment.'),
 ('Give a hepatitis B vaccine booster and proceed without further HBV assessment','Vaccination protects susceptible patients from new infection but does not eliminate latent-virus reactivation risk in someone with evidence of previous infection.')])
revise('Tumor Removal and Immunotherapy Are Complementary',others=[
 ('Complete the second-line immune induction course before surgical assessment','Neurologic stabilization and anesthetic risk must be considered, but a relevant tumor warrants coordinated timely surgical assessment rather than automatic deferral until immune induction ends.'),
 ('Resect the tumor and pause further immune treatment pending postoperative recovery','A procedure may require adjustments, but resection does not promptly extinguish established CNS inflammation or justify an automatic prolonged interruption of neurologic therapy.'),
 ('Continue immune therapy and use serial tumor imaging to decide on later resection','Surveillance suits selected incidental lesions, but a relevant identified teratoma in confirmed NMDAR disease needs timely specialist tumor management rather than observation by default.')])
revise('Residual Memory Problems Are Not Automatically Relapse',others=[
 ('Give another acute IVIG course and interpret improvement as confirmation of relapse','A supported relapse may require treatment, but nonspecific improvement cannot establish the cause; medicines, sleep and seizures should first be assessed in this scenario.'),
 ('Measure serum antibody titre and escalate if it remains positive','Persistent antibodies can accompany recovery or residual injury, so positivity alone cannot distinguish relapse from the reversible contributors described.'),
 ('Continue the current medicines and monitor cognition at the next routine annual visit','Longitudinal follow-up is useful, but a new change with identifiable medicine and sleep factors deserves timely reassessment rather than passive annual observation.')])
revise('Rapid Cerebellar Decline Can Precede Visible Atrophy',others=[
 ('Thoracic assessment for SCLC as the leading antibody-directed search','SCLC is a major concern with Hu and selected other antibodies, but anti-Yo in this woman particularly directs attention to breast and gynecologic malignancies.'),
 ('Lymphoma-focused assessment as the leading antibody-directed search','Hodgkin lymphoma is particularly linked to DNER/Tr cerebellar disease; anti-Yo supports a different initial targeted tumor emphasis.'),
 ('Thymic assessment as the leading antibody-directed search','Thymoma is important in selected CASPR2 and other immune syndromes, but is not the characteristic anti-Yo association guiding this case.')])
revise('Repeat Screening in a High-Risk Combination',others=[
 ('Repeat tumor screening every four to six months for one year','This uses the appropriate interval but truncates the two-year surveillance period recommended for the stated high-risk phenotype-antibody combination.'),
 ('Repeat tumor screening every twelve months for two years','Annual assessment is used in some different follow-up frameworks, but the 2021 PNS consensus specifies a shorter four-to-six-month interval for this combination.'),
 ('Repeat tumor screening every four to six months for five years','Longer individualized surveillance may be justified in selected cases, but five years is not the specified standard duration of this 2021 recommendation.')])
revise('Encephalitis During Checkpoint Inhibition',answer='Hold the checkpoint inhibitor and urgently evaluate infection and immune toxicity with appropriate treatment',others=[
 ('Hold the checkpoint inhibitor and defer immune treatment until neural antibodies return','Holding treatment is appropriate, but negative or delayed antibodies do not exclude immune toxicity; severe supported disease requires timely therapy after appropriate infectious assessment.'),
 ('Continue the checkpoint inhibitor while treating seizures and possible infection','Seizure and infection care are needed, but a suspected severe neurologic immune toxicity also requires interruption of the potential trigger and specialist reassessment.'),
 ('Hold the checkpoint inhibitor and begin steroids without pathogen evaluation or antiviral cover','Immune treatment can be urgent, but infection can mimic this presentation; appropriate pathogen investigation and empiric coverage should accompany care when infection remains plausible.')])
revise('Intracellular Antibodies Often Mark a Cellular Immune Process',table=(['Feature','Classical intracellular onconeural syndromes','Neuronal-surface-antibody syndromes'],[
 ['Examples','Hu, Yo, Ma2','NMDAR, LGI1, CASPR2'],
 ['Mechanistic framework','Often predominantly cellular injury; antibody is an important marker','Antibody-mediated disruption of accessible targets can be important'],
 ['Cancer interpretation','Many have high cancer association; target-specific search','Cancer risk varies considerably by antibody and patient'],
 ['Treatment implication','Tumor control is central; established neuronal loss may limit reversal','Immune therapy can reverse dysfunction, but recovery is not guaranteed']]))

revise('A Lupus Diagnosis Does Not Determine the Neurologic Mechanism',answer='Evaluate competing causes and assess inflammatory versus thrombotic lupus attribution',others=[
 ('Give pulse glucocorticoids and use the response to establish inflammatory attribution','Pulse therapy can be appropriate for supported severe inflammatory NPSLE, but fever and medicine changes require assessment of competing causes rather than a response-based diagnosis.'),
 ('Begin anticoagulation after a positive aPL screen without documenting thrombosis','aPL can inform risk and selected prevention strategies, but a positive screen alone does not establish that confusion is thrombotic or justify therapeutic anticoagulation.'),
 ('Reduce the steroid dose and defer further CNS investigation pending improvement','Steroid toxicity is plausible, but modifying treatment alone can delay diagnosis of infection, seizures or another cause of acute confusion.')])
revise('Secondary Prevention After Arterial Thrombotic APS',others=[
 ('Rivaroxaban-based anticoagulation with standard vascular risk reduction','DOACs are appropriate in many other thromboembolic settings, but triple-positive arterial APS has an unfavorable evidence base and should receive a VKA-oriented strategy.'),
 ('Dual antiplatelet therapy as the long-term substitute for VKA','Antiplatelet strategies have selected stroke indications, but do not replace guideline-preferred VKA treatment for definite arterial thrombotic APS in this scenario.'),
 ('Low-dose aspirin with hydroxychloroquine as the complete secondary-prevention plan','These agents can have roles in SLE or selected primary prevention contexts, but are not sufficient replacement for indicated anticoagulation after this definite APS arterial event.')])
revise('Angiographic Beading Is Not Synonymous With CNS Vasculitis',others=[
 ('Prioritize PACNS induction treatment on the angiographic pattern','Immune induction is appropriate for sufficiently supported PACNS, but recurrent thunderclap headaches and bland CSF require careful RCVS and other mimic assessment before that attribution.'),
 ('Use vessel-wall MRI as the sole definitive test distinguishing RCVS from PACNS','Vessel-wall MRI can contribute in selected cases, but is not sufficiently definitive in isolation to replace integrated clinical, CSF and vascular assessment.'),
 ('Use a short steroid trial before pursuing additional vascular evaluation','A response trial can be misleading and does not reliably distinguish the mechanisms; adequate etiologic assessment is preferable before exposing a suspected RCVS patient to steroids.')])
revise('A Negative Angiogram Does Not Exclude Small-Vessel PACNS',others=[
 ('Repeat luminal angiography as the only remaining confirmation strategy','Repeat angiography can answer technical or evolving vascular questions, but small-vessel disease may remain invisible and requires a broader diagnostic strategy.'),
 ('Use the CSF inflammatory pattern as sufficient evidence for induction therapy','Inflammatory CSF can support suspicion, but is not specific and cannot resolve infection, lymphoma and other important mimics in this case.'),
 ('Use steroid responsiveness instead of tissue assessment to confirm the cause','Urgent empiric therapy may sometimes be necessary, but improvement is nonspecific and cannot replace a feasible diagnostic plan or exclude a steroid-sensitive mimic.')])
revise('Systemic Tissue Can Support Probable Neurosarcoidosis',answer='Probable neurosarcoidosis',others=[
 ('Definite neurosarcoidosis','Definite classification requires neural tissue evidence in the appropriate framework; this biopsy establishes systemic rather than direct neural pathology.'),
 ('Possible neurosarcoidosis only','Possible disease lacks the tissue support needed for higher certainty; the compatible syndrome and systemic pathology support probable disease after appropriate exclusions.'),
 ('Isolated neurosarcoidosis','The demonstrated systemic tissue involvement makes an isolated neural-disease designation unsuitable; that term is not a replacement for the certainty category asked here.')],table=(['Consensus category','Tissue evidence','Shared requirement'],[
 ['Possible','No pathologic confirmation','Compatible neurologic assessment and reasonable exclusion of alternatives'],
 ['Probable','Nonneural tissue supports systemic sarcoidosis','Compatible neurologic assessment and reasonable exclusion of alternatives'],
 ['Definite','Neural tissue supports sarcoidosis','Compatible neurologic assessment and reasonable exclusion of alternatives']]))
revise('Disabling Stiff-Person Disease Despite Symptomatic Therapy',others=[
 ('Rituximab','Selected refractory patients may receive rituximab, but the landmark positive placebo-controlled crossover evidence for the scenario concerns IVIG; benefit cannot be assumed for every agent.'),
 ('Cyclophosphamide','Cyclophosphamide may be considered in selected refractory immune disease, but it does not share the positive randomized evidence asked about here and has substantial toxicity.'),
 ('Mycophenolate mofetil','Mycophenolate can have selected maintenance roles in immune neurologic disease, but it is not the acute treatment with the positive randomized stiff-person trial evidence.')])
revise('A Neurovisceral Attack Needs Biochemical Testing',others=[
 ('A panel of acute-porphyria genes before precursor testing','Genetics can identify a subtype after biochemical assessment, but a pathogenic variant does not independently establish that the current symptoms are an active attack.'),
 ('Random urinary total porphyrins as the screening assay','Porphyrin elevations can be secondary and nonspecific; ALA and PBG with creatinine normalization directly assess the acute precursor pattern.'),
 ('A 24-hour urine porphyrin fractionation as the first test','Fractionation can help later subtype assessment, but a timely random precursor sample is preferable initially and avoids delaying severe-attack care.')])
revise('Normal Ceruloplasmin Does Not End a Wilson Evaluation',others=[
 ('Repeat ceruloplasmin alone before deciding whether copper studies are needed','Repeat testing can clarify a questionable result, but normal ceruloplasmin does not justify deferring an integrated evaluation of this suggestive hepatic-neurologic phenotype.'),
 ('Use total serum copper as the sole next discriminator','Total copper is affected by ceruloplasmin and other factors and cannot independently establish or exclude Wilson disease; integrated testing is required.'),
 ('Use basal-ganglia MRI findings as the confirmatory investigation','MRI can support the neurologic assessment, but its patterns are not uniquely Wilson disease and do not replace ocular, biochemical and selected genetic evidence.')])

if __name__=='__main__':
    coverage=ROOT/'Neurology/12. Autoimmune, Paraneoplastic & Systemic Neurological Disorders.coverage.json'
    c=json.loads(coverage.read_text(encoding='utf-8'))
    assert len(rows)==c['plannedQuestions']==sum(s['questions'] for s in c['sections']),'Incomplete chapter; do not install'
    index=0
    for section in c['sections']:
        for decision in section['decisions']:
            assert rows[index]['topic']==section['section']
            rows[index]['coverageDecision']=decision
            index+=1
    save('Neurology',12,c['chapter'],rows,R,'Original source-based postgraduate synthesis; full Harrison subscription text not accessed and independent clinician review not claimed.')
    c.update(status='authored_validated',authoredQuestions=len(rows))
    c['questionDecisions']=[dict(question=i+1,title=r['title'],decision=r['coverageDecision']) for i,r in enumerate(rows)]
    coverage.write_text(json.dumps(c,ensure_ascii=False,indent=2),encoding='utf-8')
