"""Original decision-mapped neuro-oncology, pressure and neurogenetic chapter."""
import json
from qbank_json_chapters import question as Q,save,ROOT
R={
 'NICE':('NICE NG99: adult brain tumors and brain metastases','https://www.nice.org.uk/guidance/ng99/chapter/recommendations'),
 'EANO':('EANO adult diffuse glioma guideline, 2021','https://pmc.ncbi.nlm.nih.gov/articles/PMC7904519/'),
 'CAP':('CAP/AANP/AMP/SNO molecular biomarker guideline, 2022','https://pmc.ncbi.nlm.nih.gov/articles/PMC9311267/'),
 'LP':('Consensus guidance for lumbar puncture safety, 2017','https://pmc.ncbi.nlm.nih.gov/articles/PMC5454085/'),
}
def S(h,main,*children):return(h,[(main,list(children))])
rows=[]
def add(*a,**kw):rows.append(Q(*a,**kw))

add('Primary intracranial tumors','Investigation of a Suspected Intracranial Tumor',
 'A stable adult has a new focal seizure and progressive unilateral weakness. CT suggests an intra-axial mass. Which next diagnostic approach is most appropriate?',
 'Contrast-enhanced structural brain MRI with specialist tissue-diagnosis planning',[
 ('Lumbar puncture for cytology before further structural imaging','CSF cytology has selected oncologic roles, but an incompletely assessed mass can create unsafe pressure gradients; define the structural lesion and procedural safety first.'),
 ('MR spectroscopy as a substitute for tissue diagnosis','Spectroscopy can refine selected imaging questions, but metabolic patterns are not sufficiently definitive to replace integrated tissue diagnosis when feasible and clinically appropriate.'),
 ('Interval noncontrast CT after an antiseizure-treatment trial','Seizure treatment is needed, but symptomatic control does not establish the mass etiology or justify delaying definitive structural assessment in progressive focal disease.')],
 [S('Define the Lesion and Its Immediate Consequences','**Standard structural MRI is the initial detailed investigation for suspected glioma when feasible.** NICE specifies T2, FLAIR, diffusion and pre- and post-contrast volumetric T1 sequences.',
    'Assess location, enhancement, diffusion, edema, hydrocephalus and mass effect. Imaging guides the differential, operative planning and the safest tissue approach.',
    'CT remains useful for rapid emergency assessment and selected questions such as hemorrhage or calcification, but is not interchangeable with the complete MRI evaluation.'),
  S('Imaging Does Not Replace Integrated Diagnosis','**Coordinate specialist neurosurgical and neuro-oncology assessment.** Glioma, metastasis, lymphoma, infection and inflammatory lesions can share imaging features.',
    'Advanced perfusion or spectroscopy can help selected uncertainties but should not be presented as histologic or molecular confirmation.',
    'Avoid LP when mass effect or a dangerous intracranial pressure gradient makes it unsafe; removing only a small volume does not remove that risk. Treat seizures and other urgent complications while planning diagnosis. If rapid deterioration occurs, stabilization and urgent structural intervention take priority over an elective sequence; in this stable patient, high-quality imaging supports an informed tissue and treatment decision.')],['NICE','EANO','LP'])

add('Primary intracranial tumors','Integrated Diagnosis of Oligodendroglioma',
 'An adult diffuse glioma has oligodendroglial morphology and an IDH mutation. Which additional finding is required for the integrated diagnosis of oligodendroglioma?',
 'Whole-arm 1p/19q codeletion',[
 ('MGMT promoter methylation','MGMT methylation informs alkylator sensitivity in relevant contexts, but does not define the oligodendroglial lineage or substitute for 1p/19q codeletion.'),
 ('An isolated TERT promoter mutation','TERT mutations are common in oligodendroglioma but also occur in other tumors; they are not sufficient to establish the integrated diagnosis.'),
 ('Homozygous CDKN2A/B deletion','CDKN2A/B deletion has important grading implications in IDH-mutant astrocytoma, but is not the defining additional marker of oligodendroglioma.')],
 [S('Use Molecular Identity Rather Than Morphology Alone','**Oligodendroglioma is defined by an IDH mutation and whole-arm 1p/19q codeletion.** A fried-egg appearance or calcification can suggest the diagnosis but cannot establish it.',
    'Partial chromosomal losses are not equivalent to the defining whole-arm event. An apparently discordant assay result requires neuropathology review and an appropriate confirmatory strategy.',
    'ATRX loss and TP53 abnormalities favor an astrocytic pathway in an IDH-mutant diffuse glioma and influence the testing algorithm.'),
  S('Separate Identity, Grade and Treatment Prediction','**Adult-type diffuse gliomas comprise IDH-mutant astrocytoma, IDH-mutant/1p19q-codeleted oligodendroglioma and IDH-wildtype glioblastoma.** Each combines molecular identity with relevant grading features.',
    'Oligodendrogliomas have CNS WHO grades 2 or 3. An IDH-mutant astrocytoma can be grade 2, 3 or 4; grade alone does not convert one lineage into another.',
    'MGMT methylation and other biomarkers answer different clinical questions. Treatment depends on integrated diagnosis, grade, symptoms, resection and patient factors rather than one microscopic descriptor. Ensure the final report supports multidisciplinary planning, and do not apply a glioblastoma regimen automatically to every infiltrating glioma with an aggressive-looking scan.')],['CAP','EANO'],style='direct')

add('Primary intracranial tumors','Molecular Grade 4 IDH-Mutant Astrocytoma',
 'An IDH-mutant astrocytoma has no sampled necrosis or microvascular proliferation, but validated testing shows homozygous CDKN2A/B deletion. Which integrated grade is appropriate?',
 'Astrocytoma, IDH-mutant, CNS WHO grade 4',[
 ('Astrocytoma, IDH-mutant, CNS WHO grade 2','A low-grade histologic appearance does not override the grade-4 implication of validated homozygous CDKN2A/B deletion in an IDH-mutant astrocytoma.'),
 ('Astrocytoma, IDH-mutant, CNS WHO grade 3','Grade 3 can apply to other IDH-mutant astrocytomas, but this molecular alteration supports grade 4 even without the sampled histologic grade-4 features.'),
 ('Glioblastoma, IDH-wildtype, CNS WHO grade 4','The patient’s tumor is IDH-mutant; assigning grade 4 does not change the molecular identity into IDH-wildtype glioblastoma.')],
 [S('A Molecular Alteration Can Determine Grade','**Homozygous CDKN2A/B deletion is a grade-4 marker in IDH-mutant astrocytoma.** Necrosis or microvascular proliferation can also establish grade 4, but are not required when this defining alteration is present.',
    'Distinguish homozygous deletion from a nonspecific copy-number change or a report that does not establish the relevant alteration. Review technical adequacy and integrated pathology.',
    'This rule should not be transferred uncritically to every tumor class; molecular grading is entity-specific.'),
  S('Preserve the Integrated Name','**The correct name remains astrocytoma, IDH-mutant, grade 4**, rather than the older IDH-mutant glioblastoma terminology.',
    'The distinction matters for prognosis, counseling and clinical-trial interpretation. Similar grade numbers across molecular entities do not imply identical biology or outcomes.',
    'Review surgical sampling, molecular findings and clinical factors in treatment planning. Lack of enhancement or a limited biopsy without necrosis should not falsely reassure clinicians when the validated molecular result changes grade. Conversely, do not infer deletion from a suspicious scan; treatment decisions require the actual pathology evidence and the patient’s condition and preferences.')],['CAP','EANO'],style='direct')

R['MOL23']=('EANO molecular diagnostic tools for WHO 2021 classification, 2023','https://academic.oup.com/neuro-oncology/article/25/10/1731/7189810')

add('Primary intracranial tumors','Molecularly Defined IDH-Wildtype Glioblastoma',
 'A 64-year-old has a diffusely infiltrating astrocytic glioma that is IDH-wildtype and H3-wildtype. The sample lacks necrosis and microvascular proliferation but has validated EGFR amplification. Other molecular entities have been excluded. Which integrated diagnosis is appropriate?',
 'Glioblastoma, IDH-wildtype, CNS WHO grade 4',[
 ('Astrocytoma, IDH-mutant, CNS WHO grade 4','That diagnosis requires an IDH mutation; a high-grade molecular feature does not make an IDH-wildtype tumor IDH-mutant.'),
 ('Oligodendroglioma, IDH-mutant and 1p/19q-codeleted','Oligodendroglioma requires the defining IDH mutation and whole-arm codeletion; EGFR amplification does not substitute for either requirement.'),
 ('Histologic grade 2 astrocytoma without molecular upgrading','The absence of sampled histologic grade-4 features does not override a qualifying molecular glioblastoma feature in the appropriate adult diffuse astrocytic context.')],
 [S('Molecular Findings Can Establish Grade-4 Biology','**Adult IDH-wildtype diffuse astrocytic gliomas can meet glioblastoma criteria through molecular features**, even without sampled necrosis or microvascular proliferation.',
    'Relevant features include EGFR amplification, combined whole-chromosome 7 gain and chromosome 10 loss, or a qualifying TERT promoter mutation in the appropriate diagnostic context.',
    'Confirm the molecular result and exclude alternative entities, particularly in younger patients or unusual locations. IDH-wildtype alone does not make every CNS tumor a glioblastoma.'),
  S('Do Not Confuse a Screening Stain With Complete Molecular Assessment','**Negative IDH1 R132H immunostaining does not exclude every IDH mutation in all settings.** Additional sequencing is selected according to age, histology and the diagnostic algorithm.',
    'Midline or unusual tumors can need H3 and other molecular assessment. DNA methylation profiling can help resolve selected difficult classifications.',
    'Integrate pathology with imaging and clinical information before treatment planning. A small biopsy can underestimate histologic aggressiveness, while molecular findings can clarify it. Conversely, do not apply a molecular rule outside its intended tumor context or use an isolated nonspecific marker to overrule a well-supported alternative entity. The final integrated name should communicate both identity and grade to the treating team.')],['CAP','EANO','MOL23'],style='direct')

add('Primary intracranial tumors','MGMT Promoter Methylation and Alkylator Benefit',
 'An older patient with confirmed IDH-wildtype glioblastoma is not suitable for combined chemoradiation. Which biomarker is particularly useful when weighing temozolomide-based treatment against a radiotherapy-focused approach?',
 'MGMT promoter methylation',[
 ('Whole-arm 1p/19q codeletion','This defines oligodendroglioma in an IDH-mutant context; it is not the main predictive biomarker for alkylator benefit in established IDH-wildtype glioblastoma.'),
 ('ATRX loss','ATRX is useful for lineage assessment in appropriate diffuse gliomas, but does not replace MGMT methylation when evaluating temozolomide sensitivity in this scenario.'),
 ('An isolated TERT promoter mutation','TERT can contribute to integrated tumor classification, but is not the principal marker used for this temozolomide-selection question.')],
 [S('A Predictive Marker Rather Than a Lineage Definition','**MGMT repairs alkylator-induced DNA damage.** Promoter methylation is associated with reduced expression and greater expected benefit from alkylating treatment in relevant glioblastoma settings.',
    'It does not define oligodendroglioma, establish IDH status or replace the integrated diagnosis. A methylated tumor remains the same molecular entity.',
    'The test is especially useful in older or frail patients when a single-modality strategy is being considered. Performance status, goals, comorbidity and treatment tolerance remain essential.'),
  S('Apply the Result Without Overstating Certainty','**Methylated tumors are more likely to benefit from temozolomide**, while hypofractionated radiotherapy is often favored over temozolomide alone in an unmethylated patient unsuitable for combined treatment.',
    'Assays and cutoffs vary, and borderline results need careful laboratory interpretation. Methylation is not a guarantee of response or a complete individual prognosis.',
    'Fit adults can receive combined therapy even when the expected chemotherapy benefit is smaller; do not turn a selection aid for a frail single-modality scenario into a universal rule to omit treatment. Discuss myelosuppression, infection, nausea and monitoring as part of the plan, alongside supportive and palliative care aligned with the patient’s priorities.')],['CAP','EANO'],style='direct')

add('Primary intracranial tumors','Maximal Safe Resection Preserves Function',
 'A suspected diffuse glioma abuts language and motor pathways. The patient is otherwise fit for surgery. Which operative principle best fits guideline-based care?',
 'Aim for maximal safe resection using appropriate functional planning and preserve neurologic function',[
 ('Pursue radiographic complete resection even if a permanent disabling deficit is expected','Greater removal can be valuable, but permanent neurologic disability can impair quality of life and eligibility for further therapy; completeness is not the overriding goal.'),
 ('Avoid any tissue procedure because the tumor touches eloquent pathways','A stereotactic biopsy or function-guided resection can still be appropriate; eloquent location requires individualized planning rather than automatic abandonment of tissue diagnosis.'),
 ('Begin empirical chemoradiation from the MRI appearance without tissue planning','Treatment without tissue is reserved for exceptional circumstances; feasible integrated pathology normally guides therapy and distinguishes important tumor mimics and molecular entities.')],
 [S('Balance Cytoreduction Against Lasting Disability','**Maximal safe resection is an individualized functional goal.** Diffuse infiltration limits the meaning of a radiographic complete resection and surgery is not inherently curative.',
    'Use appropriate mapping, monitoring, tract-oriented planning or awake techniques where suitable and available. Their role is to support a safe strategy, not to guarantee absence of deficits.',
    'If safe resection is not feasible, targeted biopsy can provide the diagnosis needed for subsequent treatment. Patient goals and expected morbidity influence the choice.'),
  S('Plan Diagnosis and Adjuvant Care Together','**Obtain adequate tissue for integrated histologic and molecular assessment.** Sampling quality matters when the lesion is heterogeneous or a small biopsy could miss important features.',
    'Assess early postoperative imaging and neurologic status according to local pathways. New deficits require evaluation for surgical complications rather than being accepted automatically as the price of tumor removal.',
    'Discuss radiotherapy, systemic options and supportive needs after the integrated result. Preserved cognition, communication and mobility can be crucial to completing further therapy. Avoid describing extent-of-resection observational associations as proof that every additional increment of removal improves survival regardless of neurologic cost; the clinical aim combines disease control with meaningful function.')],['EANO','NICE'])

R.update({
 'STUPP':('Radiotherapy with concomitant/adjuvant temozolomide trial, 2005','https://doi.org/10.1056/NEJMoa043330'),
 'VORA':('FDA vorasidenib approval for selected grade 2 IDH-mutant glioma, 2024','https://www.fda.gov/drugs/cancer-approvals/fda-approves-vorasidenib-grade-2-astrocytoma-or-oligodendroglioma-susceptible-idh1-or-idh2-mutation'),
 'VORALABEL':('Vorasidenib prescribing information','https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=31405fee-55b7-4857-987e-2724ee76be84'),
 'MEN':('EANO meningioma guideline, 2021','https://pmc.ncbi.nlm.nih.gov/articles/PMC8563316/'),
 'VS':('EANO vestibular schwannoma guideline, 2020','https://pmc.ncbi.nlm.nih.gov/articles/PMC6954440/'),
})

add('Primary intracranial tumors','Concomitant and Adjuvant Temozolomide',
 'A fit 52-year-old has a newly diagnosed IDH-wildtype glioblastoma after maximal safe resection. Which postoperative framework is standard for a patient suitable for conventional combined treatment?',
 'Focal radiotherapy with concomitant temozolomide followed by adjuvant temozolomide',[
 ('Whole-brain radiotherapy with temozolomide only at recurrence','Conventional newly diagnosed glioblastoma treatment uses focal rather than routine whole-brain irradiation and includes upfront concomitant/adjuvant temozolomide in suitable patients.'),
 ('Temozolomide alone followed by radiotherapy after the sixth cycle','Single-modality approaches can suit selected older or frail patients, but this fit patient is eligible for combined treatment rather than routine radiation deferral.'),
 ('Focal radiotherapy with PCV as the routine glioblastoma regimen','PCV is important in selected other diffuse glioma settings, particularly oligodendroglial treatment pathways, but is not the standard concomitant/adjuvant regimen asked here.')],
 [S('Use the Established Combined Schedule','**The conventional framework combines focal radiation and temozolomide.** The landmark trial used ==60 Gy in 30 fractions== with ==75 mg/m² temozolomide daily== during radiation.',
    'After a treatment break, adjuvant temozolomide is commonly given at ==150–200 mg/m² daily for five days in each 28-day cycle==, for six cycles in the original regimen.',
    'Adapt treatment for performance status, age, marrow and organ function and patient goals. This question does not imply that every older or frail patient should receive a six-week combined course.'),
  S('Monitor Toxicity and Interpret Response Carefully','**Check blood counts and relevant organ function** and provide antiemetic and infection-prevention measures according to the regimen and steroid exposure.',
    'Lymphopenia and opportunistic infection risk are important during combined treatment. New enhancing abnormalities can reflect treatment effect as well as progression and need clinical-imaging correlation.',
    'MGMT methylation informs expected alkylator benefit but does not guarantee response. Discuss supportive, rehabilitative and palliative care alongside tumor-directed treatment. Do not promise that extending adjuvant chemotherapy indefinitely improves survival; duration and later interventions should follow evidence and the individual clinical course rather than assuming more cycles are necessarily better.')],['STUPP','EANO'])

add('Primary intracranial tumors','Vorasidenib in Selected IDH-Mutant Grade 2 Glioma',
 'An adult has a surgically sampled grade 2 IDH-mutant glioma, with residual nonenhancing disease and no prior radiotherapy or chemotherapy. Immediate chemoradiation is not otherwise required. Which targeted option has trial evidence supporting delayed progression and next intervention in a selected population?',
 'Vorasidenib',[
 ('Osimertinib','Osimertinib has CNS activity in selected EGFR-mutant lung cancers, but is not the IDH-targeted option supported for this postoperative grade 2 glioma population.'),
 ('Bevacizumab','Bevacizumab can reduce edema and has selected recurrent-tumor roles, but does not provide the IDH-directed trial evidence or indication described here.'),
 ('Dabrafenib with trametinib','BRAF/MEK inhibition can be relevant to selected BRAF-altered tumors, but an IDH mutation does not establish that target or the treatment indication in this question.')],
 [S('Keep Trial Selection Separate From Broad Glioma Labels','**Vorasidenib inhibits mutant IDH1 and IDH2.** INDIGO studied a selected postoperative grade 2 population with no previous anticancer therapy beyond surgery and without an immediate need for chemoradiation.',
    'It improved progression-free survival and delayed the next intervention compared with placebo. These endpoints should not be restated as proven overall-survival benefit.',
    'The US FDA approved it in 2024 for patients aged 12 years or older with susceptible IDH1/2-mutant grade 2 astrocytoma or oligodendroglioma after surgery. Regulatory availability and local eligibility can differ.'),
  S('Prescribe With Hepatic and Reproductive Safety Monitoring','**The adult dose is ==40 mg orally once daily== under the prescribing information.** Confirm the susceptible mutation and review drug interactions, smoking effects and reproductive precautions.',
    'Check liver tests before treatment, ==every two weeks for the first two months==, then ==monthly for the first two years==, with additional assessment when abnormalities occur.',
    'Hepatotoxicity can require interruption, reduction or discontinuation under label guidance. Do not substitute this strategy for indicated urgent treatment of enhancing, symptomatic or higher-grade disease outside the supported context. Continue MRI and clinical follow-up and use shared decisions about the benefit of delaying other treatment against toxicity and monitoring burden.')],['VORA','VORALABEL','EANO'])

add('Primary intracranial tumors','Observation of an Incidental Meningioma',
 'A small radiologically typical meningioma is found incidentally. The patient has no attributable symptoms, no important mass effect and no documented growth. Which initial approach is most appropriate?',
 'Clinical and MRI surveillance with individualized review of growth and risk',[
 ('Immediate resection to prevent an inevitable malignant transformation','Surgery is appropriate for many symptomatic or growing tumors, but incidental asymptomatic meningiomas do not all require immediate removal or inevitably transform.'),
 ('Immediate stereotactic radiation for every radiologically typical lesion','Radiation is useful in selected cases, but an incidental low-risk presentation can be observed rather than exposed automatically to treatment.'),
 ('Discharge from follow-up because a dural lesion cannot progress','Many tumors remain indolent, but meningiomas can grow or cause symptoms; observation requires a planned surveillance pathway rather than assuming permanent harmlessness.')],
 [S('Separate Incidental Disease From a Treatment Indication','**Observation is a first option for an incidental asymptomatic suspected meningioma.** Consider size, location, edema, growth risk, age, comorbidity and the patient’s priorities.',
    'Cognition and subtle focal symptoms should be assessed rather than assuming that no dramatic deficit means no attributable impact.',
    'A radiologic diagnosis is not a tissue grade. Rapid growth or atypical features should prompt reassessment for a higher-grade lesion or another diagnosis.'),
  S('Intervene When the Balance Changes','**Symptoms, meaningful growth or threatened function can justify intervention.** Surgery provides tissue and decompression; radiosurgery or fractionated radiation can suit selected anatomy and clinical circumstances.',
    'Aim to preserve function, particularly near venous sinuses, cranial nerves or other critical structures. An intentional subtotal approach plus selected radiation may be preferable to a disabling attempt at complete removal.',
    'Define MRI and clinical follow-up with the specialist service and modify it as evidence accumulates. Seizures, visual change or new focal findings warrant reassessment rather than waiting for the next routine scan. Treatment choice should balance disease control against neurological risk rather than treating every imaging discovery or every small size change as an automatic operation.')],['MEN','NICE'])

add('Primary intracranial tumors','Large Vestibular Schwannoma With Brainstem Compression',
 'A patient has a large vestibular schwannoma causing brainstem compression and progressive gait impairment. Which treatment principle is most appropriate?',
 'Surgical decompression assessment, with extent and adjunctive treatment individualized to cranial-nerve preservation',[
 ('Observation as the preferred strategy used for a small asymptomatic schwannoma','Observation can suit small tumors with preserved function, but a large lesion with progressive symptoms and brainstem compression requires active decompression assessment.'),
 ('Single-session radiosurgery as the default substitute for decompression','Radiosurgery is effective for selected smaller tumors, but does not provide immediate decompression and is not the default for this large compressive presentation.'),
 ('Cochlear rehabilitation alone with imaging only if hearing worsens','Hearing rehabilitation is important but does not address brainstem compression or progressive gait dysfunction; the structural treatment decision cannot be gated by hearing change.')],
 [S('Size and Function Change the Management Pathway','**Vestibular schwannoma management considers tumor size, growth, hearing, cranial-nerve function and mass effect.** Observation, radiosurgery and surgery each have appropriate settings.',
    'Small asymptomatic tumors can be observed with imaging and functional assessment. Symptomatic smaller lesions require individualized comparison of growth control, hearing and facial-nerve risks.',
    'Large tumors compressing the brainstem generally require surgical assessment for decompression rather than applying the small-tumor observation pathway.'),
  S('Protect Cranial-Nerve and Brainstem Function','**Plan the surgical extent around safe decompression and function.** Selected subtotal or near-total approaches with subsequent observation or radiation can balance control against morbidity.',
    'Discuss realistic hearing and facial-nerve outcomes rather than promising preservation from one technique. Evaluate hydrocephalus, swallowing and other cranial-nerve effects when indicated.',
    'Continue postoperative imaging and hearing or balance rehabilitation. Young age, bilateral tumors or other syndromic features should raise the possibility of NF2-related schwannomatosis and prompt appropriate counseling. Treatment is not chosen from diameter alone, but progressive compression is a distinct indication that cannot be managed solely with symptomatic vestibular medicines.')],['VS','NICE'])

R.update({
 'PCNSL':('EHA-ESMO primary CNS lymphoma guideline, 2024','https://doi.org/10.1002/hem3.89'),
 'BM':('ASCO-SNO-ASTRO brain metastases guideline, 2022','https://pmc.ncbi.nlm.nih.gov/articles/PMC8917399/'),
 'ASTRO':('ASTRO brain-metastasis radiotherapy guideline, 2022','https://www.astro.org/provider-resources/guidelines/clinical-practice-guidelines/rt-for-brain-metastases'),
})

add('Lymphoma, metastases and oncologic complications','Tissue Diagnosis Before Steroids in Stable Suspected PCNSL',
 'An alert, clinically stable patient has an enhancing deep cerebral lesion suspicious for primary CNS lymphoma. There is no threatening mass effect, and stereotactic biopsy can be arranged promptly. Which approach is most appropriate?',
 'Coordinate biopsy before corticosteroids when clinically feasible',[
 ('Give dexamethasone first and use lesion shrinkage as diagnostic confirmation','Lymphoma can regress after steroids, but this response is not uniquely diagnostic and can reduce subsequent tissue yield; obtain tissue first when the clinical situation permits.'),
 ('Begin glioblastoma chemoradiation from the enhancement pattern','Lymphoma and glioblastoma can overlap radiologically but require different treatment; imaging suspicion does not justify bypassing feasible tissue diagnosis.'),
 ('Perform extensive resection as the default method of confirming a deep lesion','Selected surgical situations differ, but stereotactic biopsy is generally the diagnostic approach for suspected PCNSL; a deep lesion does not require routine radical removal.')],
 [S('Preserve the Diagnostic Target','**Suspected primary CNS lymphoma normally requires histopathologic confirmation.** Corticosteroids can rapidly alter the lesion and compromise diagnostic tissue.',
    'Avoid them before biopsy when clinically possible and coordinate an expedited procedure. This is not a rule to leave an unstable patient with dangerous mass effect untreated.',
    'If deterioration occurs, urgent tissue acquisition before steroids is preferred when feasible; life-preserving stabilization must not be delayed for an elective sequence.'),
  S('Define Extent After Establishing the Diagnosis','**Assess CNS compartments and exclude systemic lymphoma.** Evaluation can include ocular examination, appropriate systemic imaging and safe CSF assessment according to the clinical setting.',
    'CSF or ocular findings can sometimes contribute to diagnosis, but a negative result does not reliably exclude a parenchymal lesion. LP safety still depends on mass effect and other contraindications.',
    'Document prior steroid exposure for the radiology and pathology teams. If tissue is nondiagnostic after treatment, reassess imaging and the safest next sampling strategy rather than assuming the original suspicion was disproved. Preserve the distinction between a radiologically likely diagnosis and a confirmed lymphoma before starting a disease-specific chemotherapy regimen.')],['PCNSL','LP'])

add('Lymphoma, metastases and oncologic complications','High-Dose Methotrexate in Primary CNS Lymphoma',
 'A fit patient has biopsy-confirmed primary CNS diffuse large B-cell lymphoma and adequate renal function. Which induction principle is most appropriate?',
 'Use a specialist high-dose-methotrexate-based CNS-active regimen with planned consolidation',[
 ('Use R-CHOP alone as for a typical systemic nodal DLBCL','R-CHOP is effective in many systemic DLBCL settings but is not adequate stand-alone induction for PCNSL because CNS drug exposure and disease management differ.'),
 ('Use focal temozolomide chemoradiation as for newly diagnosed glioblastoma','That regimen addresses a different tumor biology; PCNSL requires a lymphoma-specific CNS-active induction and consolidation strategy.'),
 ('Use whole-brain radiotherapy alone as the routine preferred induction for a fit patient','Radiation can have selected roles, including consolidation or palliation, but fit patients generally receive methotrexate-based induction rather than routine radiation-only treatment.')],
 [S('Achieve Therapeutic CNS Exposure','**High-dose methotrexate is a central component of PCNSL induction.** EHA-ESMO recommends doses of at least 3 g/m² with an appropriate rapid infusion to achieve sufficient CNS exposure.',
    'Combination choices depend on age, performance status and organ function. MATRix is one option for eligible fit patients and combines methotrexate, cytarabine, rituximab and thiotepa.',
    'Do not apply intensive regimens indiscriminately to frail patients. Rituximab use and the balance of efficacy and toxicity require specialist discussion in this setting.'),
  S('Plan Rescue, Clearance and Consolidation','**Methotrexate requires protocolized hydration, urinary alkalinization, folinic-acid rescue and drug-level monitoring.** Review renal function and interacting medicines before each course.',
    'Delayed clearance or kidney injury needs urgent specialist management; a standard dose cannot be administered safely without the supporting monitoring system.',
    'Responding eligible patients may receive thiotepa-based autologous transplantation or another tailored consolidation strategy. Radiation-related neurotoxicity matters, especially in older adults. Monitor cognitive, ocular and other involved functions and distinguish relapse from treatment toxicity. PCNSL treatment is not simply systemic lymphoma chemotherapy delivered unchanged to a patient with a brain lesion.')],['PCNSL'])

add('Lymphoma, metastases and oncologic complications','Symptomatic Brain Metastasis With Mass Effect',
 'A patient with metastatic solid cancer has a large brain lesion causing progressive weakness and substantial mass effect. A CNS-active systemic drug is available. Which immediate treatment principle is best supported?',
 'Arrange urgent local-treatment assessment, including decompression where appropriate, rather than relying on systemic therapy alone',[
 ('Start the systemic drug and defer local treatment until radiologic progression','Deferral can suit selected asymptomatic targetable disease under close surveillance, but symptomatic mass effect generally requires local-treatment assessment regardless of systemic options.'),
 ('Use dexamethasone alone as definitive treatment if weakness improves','Steroids can reduce edema and bridge treatment, but symptom improvement does not provide durable control of a large compressive metastatic lesion.'),
 ('Use single-fraction radiosurgery as the default for every lesion causing compression','Radiosurgery is effective for selected lesions, but size, edema and the need for prompt decompression can favor surgery or a different radiation strategy.')],
 [S('Symptoms Change the Sequencing','**Symptomatic brain metastases should receive appropriate local therapy regardless of systemic treatment availability.** Neurosurgical and radiation assessment should address mass effect, anatomy and overall prognosis.',
    'Surgery can relieve compression and provide tissue, particularly when diagnosis is uncertain or a large dominant lesion is driving disability.',
    'Steroids may provide temporary edema relief while definitive planning proceeds, but do not replace tumor-directed local treatment.'),
  S('Integrate Local and Systemic Options','**Choose the local approach through multidisciplinary review.** Consider lesion number, total volume, location, extracranial disease control, functional status and patient goals.',
    'A large lesion is not automatically suitable for a single radiosurgery fraction; fractionated stereotactic approaches can be considered when surgery is unsuitable, according to anatomy and specialist planning.',
    'Postoperative radiation is often required for durable local control. Continue appropriate systemic therapy through a coordinated schedule rather than treating local and systemic care as mutually exclusive choices. Discuss supportive and palliative options when the expected burden of intervention exceeds benefit; the existence of multiple metastases alone does not eliminate the need to assess a threatening dominant lesion.')],['BM','ASTRO'])

add('Lymphoma, metastases and oncologic complications','SRS for Limited Small Brain Metastases',
 'A patient with good performance status has three small unresected brain metastases, no significant mass effect and a non-small-cell solid-tumor primary. No indication for tissue acquisition is present. Which radiation approach is generally appropriate?',
 'Stereotactic radiosurgery to the lesions with MRI surveillance',[
 ('Whole-brain radiotherapy as the required first treatment for three lesions','WBRT has selected roles, but SRS alone is recommended for suitable limited unresected metastases and can reduce the cognitive burden associated with broader irradiation.'),
 ('Open resection of all lesions before considering radiation','Surgery is useful for selected symptomatic, large or diagnostically uncertain lesions, but is not routinely required for each small lesion without mass effect.'),
 ('Observation without local therapy because each lesion is small','Deferral can be appropriate with selected CNS-active systemic options and close review, but small size alone does not justify untreated surveillance in the absence of such a plan.')],
 [S('Select SRS From More Than Lesion Count','**SRS alone is a standard option for suitable patients with one to four unresected metastases**, excluding the small-cell setting addressed differently in the guideline evidence.',
    'Size, total tumor volume, location, symptoms and safe dose constraints matter. Trial populations generally involved relatively small lesions; do not extrapolate the count rule to any tumor volume.',
    'Surgery remains useful for a large symptomatic lesion or when diagnosis is needed, even in a patient who will also receive radiosurgery to other sites.'),
  S('Surveillance Is Part of the Strategy','**Local control of treated lesions does not prevent every new intracranial metastasis.** Arrange regular MRI and clinical follow-up with access to salvage treatment.',
    'Discuss radionecrosis, edema and delayed imaging uncertainty, along with the cognitive trade-offs of WBRT. Subsequent lesions may require additional SRS, surgery or a broader radiation strategy.',
    'Coordinate systemic cancer care and patient goals. SRS selection does not mean extracranial prognosis is irrelevant or that local therapy should continue irrespective of declining function. Reassess the whole clinical situation at each treatment decision rather than following a fixed lesion-number algorithm without regard to burden and benefit.')],['BM','ASTRO'])

R.update({
 'STEROID':('ASCO/SNO endorsement of CNS steroid and anticonvulsant guidance, 2019','https://doi.org/10.1200/JOP.19.00058'),
 'ASM':('SNO/EANO anticonvulsant prophylaxis guideline, 2021','https://pmc.ncbi.nlm.nih.gov/articles/PMC8563323/'),
 'SNOBM':('SNO brain metastasis consensus review, 2022','https://pmc.ncbi.nlm.nih.gov/articles/PMC9527527/'),
})

add('Lymphoma, metastases and oncologic complications','Cognitive Protection During Whole-Brain Radiotherapy',
 'A patient appropriately selected for WBRT has no hippocampal lesions and an expected survival exceeding four months. Which strategy best reduces the treatment-related cognitive burden?',
 'Hippocampal-avoidance WBRT with memantine when technically appropriate',[
 ('Conventional WBRT without cognitive-protection measures because tumor control takes priority','Tumor control remains necessary, but eligible patients can receive evidence-based cognitive protection without treating it as incompatible with the planned radiation.'),
 ('Memantine alone instead of the indicated WBRT course','Memantine can reduce cognitive toxicity in this setting but is not an antitumor replacement for appropriately indicated radiation.'),
 ('Hippocampal avoidance regardless of nearby tumor distribution','Avoidance requires safe anatomy and coverage; lesions involving the hippocampal avoidance region can make this strategy unsuitable.')],
 [S('Select Eligible Patients','**ASCO-SNO-ASTRO recommends memantine and hippocampal avoidance for eligible WBRT recipients** without hippocampal lesions and with expected survival of at least four months.',
    'The radiation team must confirm that target coverage and avoidance constraints are appropriate. Do not infer eligibility solely from the total number of metastases.',
    'These measures mitigate cognitive injury rather than guarantee that memory will remain normal. Tumor, medicines, seizures and other illness can also affect cognition.'),
  S('Maintain the Distinction Between Local Therapy Choices','**First decide whether WBRT is the appropriate strategy.** SRS, surgery, systemic approaches or supportive care may be more suitable in other clinical contexts.',
    'When WBRT is chosen, avoid omitting cognitive protection merely because the patient has metastatic cancer. Conversely, an expected very short survival changes the likely benefit and treatment burden.',
    'Assess baseline cognition, renal function and medicine tolerance when planning memantine and follow the applicable prescribing protocol. Continue MRI and clinical reassessment and provide practical cognitive support. A new cognitive decline after treatment should not automatically be labeled radiation toxicity without evaluating progression, metabolic illness and other reversible contributors.')],['BM','ASTRO'])

add('Lymphoma, metastases and oncologic complications','Selected Asymptomatic Metastases and CNS-Active Therapy',
 'A patient has small asymptomatic brain metastases from EGFR-mutant NSCLC, no threatening mass effect and access to a CNS-active targeted regimen and close MRI surveillance. Which principle is most appropriate?',
 'A multidisciplinary team may select initial CNS-active systemic therapy with a defined surveillance and salvage plan',[
 ('Local treatment can be deferred for every brain metastasis once any systemic drug is available','Deferral depends on tumor-specific evidence, symptoms, anatomy and monitoring; the presence of an arbitrary systemic option does not establish a safe strategy.'),
 ('WBRT must precede every targeted agent even in this selected asymptomatic setting','Local treatment is essential in many cases, but selected molecularly defined asymptomatic disease can be managed initially with an appropriate CNS-active systemic approach.'),
 ('Imaging can be deferred until symptoms develop if the systemic tumor responds','Extracranial response does not guarantee intracranial control; a systemic-first strategy requires planned MRI and access to prompt salvage treatment.')],
 [S('Deferral Is a Selected Strategy','**Certain CNS-active systemic regimens permit consideration of deferred local therapy in asymptomatic disease.** Molecular subtype and direct evidence for the agent matter.',
    'EGFR-mutant NSCLC is an important example. Other tumor types and targets have their own evidence and eligibility; do not generalize one pathway to all cancers.',
    'Symptomatic lesions or threatening mass effect ordinarily require local-treatment assessment regardless of the availability of targeted therapy.'),
  S('Make Surveillance Part of the Treatment Prescription','**Agree the plan among medical oncology, neurosurgery and radiation oncology.** Consider lesion location, volume, likely response, extracranial status and patient priorities.',
    'Specify clinical and MRI review and the trigger for surgery or radiation. New weakness, seizures or pressure symptoms require prompt reassessment rather than waiting for a scheduled scan.',
    'Explain that deferral is not abandonment of local treatment. Resistance or discordant CNS progression can require a change in systemic and local strategy. Drug choice should follow current tumor-specific guidance and availability rather than a fixed historical list; preserve tissue and molecular information needed for that decision and review treatment interactions and toxicity.')],['BM','ASTRO','SNOBM'])

add('Lymphoma, metastases and oncologic complications','Dexamethasone for Symptomatic Vasogenic Edema',
 'A patient with a brain metastasis has headache and mild focal weakness attributable to edema, without impending herniation. Which initial steroid principle is most appropriate?',
 'Use dexamethasone at a symptom-appropriate dose, commonly 4–8 mg/day, with early reassessment and taper planning',[
 ('Give 16 mg/day to every patient irrespective of symptom severity','Higher doses can be needed for severe pressure-related symptoms, but routine high exposure for mild symptoms adds toxicity without a corresponding established benefit.'),
 ('Use physiologic hydrocortisone replacement as the edema regimen','Replacement dosing treats adrenal insufficiency, not the anti-edema effect sought in a symptomatic metastatic lesion.'),
 ('Continue the initial dexamethasone dose until the tumor disappears','Steroids are a temporary supportive treatment; duration should follow symptoms and definitive therapy rather than radiographic disappearance of the entire lesion.')],
 [S('Match Dose to the Clinical Threat','**Dexamethasone provides temporary relief of edema-related neurologic symptoms.** A starting total of ==4–8 mg/day== is commonly appropriate for mild or moderate symptoms.',
    'Marked symptoms, elevated pressure or threatening mass effect may require a higher dose, such as ==16 mg/day==, alongside urgent definitive assessment.',
    'The steroid response does not establish the tumor diagnosis or replace surgery, radiation or systemic cancer treatment. Asymptomatic patients do not automatically need prolonged prophylactic steroids.'),
  S('Reduce Exposure as the Clinical Situation Allows','**Use the lowest effective dose and taper as rapidly as clinically tolerated.** Account for recurrent edema and adrenal suppression after prolonged exposure.',
    'Monitor glucose, infection, mood, sleep, myopathy and gastrointestinal risk. Proximal weakness from steroids can itself reduce mobility and obscure the neurologic assessment.',
    'Coordinate tapering with the treating team and the expected effect of local therapy. Prolonged combined immunosuppression can require infection prevention, including PJP prophylaxis according to risk. Do not abruptly stop a long course or continue it indefinitely because symptoms once improved; both decisions require a current clinical assessment and a documented plan.')],['STEROID','SNOBM'])

add('Lymphoma, metastases and oncologic complications','Seizure Treatment Differs From Routine Prophylaxis',
 'A patient with newly diagnosed brain metastases has never had a seizure and is not undergoing an immediate operation. Which antiseizure approach is most appropriate?',
 'Do not prescribe routine antiseizure prophylaxis solely because metastases are present',[
 ('Start levetiracetam in all patients because it has few enzyme interactions','Levetiracetam is often useful when seizure treatment is indicated, but a favorable interaction profile does not establish benefit from routine prophylaxis in seizure-naive patients.'),
 ('Start valproate to prevent seizures and improve tumor survival','Valproate can treat selected seizure disorders, but routine prophylaxis and an assumed antitumor survival benefit are not supported reasons to prescribe it here.'),
 ('Start phenytoin until the first surveillance MRI documents response','Phenytoin can treat seizures in appropriate settings, but preventive use until imaging response lacks a supported indication and adds interactions and adverse effects.')],
 [S('Separate Two Different Clinical Questions','**Routine prophylaxis is not recommended for seizure-naive patients with newly diagnosed brain tumors.** This differs from treating a patient who has already had a tumor-associated seizure.',
    'A first attributable seizure commonly warrants ongoing antiseizure treatment because a structural epileptogenic lesion is present; select the drug from the patient’s broader clinical context.',
    'The perioperative question has a separate evidence base. SNO/EANO found insufficient evidence to recommend routine perioperative medication to reduce seizures, rather than proving that every individual perioperative course is wrong.'),
  S('Choose Treatment for an Actual Indication','**When medication is needed, review cancer-drug interactions, renal or hepatic function, mood and blood counts.** Non-enzyme-inducing agents are often favored for interaction reasons.',
    'Levetiracetam can affect mood or behavior; valproate can cause thrombocytopenia and hepatic toxicity. Drug tolerability matters in a patient already receiving systemic treatment.',
    'Educate about recognizing seizures and appropriate emergency responses. New episodic symptoms require evaluation rather than retrospective justification of universal prophylaxis. Do not interpret the absence of prophylactic treatment as absence of seizure risk; it reflects the lack of sufficient preventive benefit to outweigh treatment burden in this population.')],['ASM','STEROID'])

R.update({
 'RN':('EANO consensus statement on radiation necrosis, 2026','https://doi.org/10.1093/neuonc/noag153'),
 'IFO':('Ifosfamide prescribing information: CNS toxicity','https://www.dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=91e433a9-6800-43a6-ac13-a49a04a5aecd'),
 'IIH':('IIH consensus guidelines on management, 2018','https://doi.org/10.1136/jnnp-2017-317440'),
 'PAP':('How to diagnose papilloedema, 2026','https://doi.org/10.1136/pn-2025-004784'),
})

add('Lymphoma, metastases and oncologic complications','Radiation Necrosis Versus Tumor Progression',
 'Months after stereotactic radiation, a treated metastasis enlarges with surrounding edema. The patient is stable. Which diagnostic approach is most appropriate before assigning tumor progression?',
 'Integrate treatment timing, serial MRI and selected advanced imaging, with tissue assessment when needed',[
 ('Classify progression from enlargement on one conventional contrast MRI','Growth and enhancement can reflect recurrent tumor, treatment effect or both; one conventional scan is not always sufficient to establish mechanism.'),
 ('Classify radiation necrosis from improvement after dexamethasone','Steroids can reduce edema around viable tumor as well as radiation injury; a response does not uniquely establish necrosis.'),
 ('Use a single perfusion value as definitive proof of pure radiation injury','Perfusion can help estimate the likelihood of recurrence, but overlap, technical variation and mixed pathology prevent a universal single-value diagnosis.')],
 [S('Recognize a Post-Treatment Differential','**New enhancement after radiation is not automatically viable tumor.** Timing, prior dose distribution, clinical course and serial evolution help distinguish progression from injury.',
    'The 2026 EANO consensus supports advanced MRI, particularly perfusion, and amino-acid PET in selected difficult cases. No imaging method perfectly excludes mixed tumor and necrosis.',
    'Review the actual treatment plan and images with neuroradiology and radiation oncology. A label based only on a report phrase can lead to an inappropriate change of cancer therapy.'),
  S('Use the Result to Guide Treatment','**Symptomatic radiation injury may require corticosteroids**, with bevacizumab or surgery considered in selected steroid-dependent, refractory or diagnostically uncertain cases.',
    'Surgery can provide tissue and decompression when feasible, but procedural risk and goals matter. An asymptomatic stable patient can sometimes undergo planned imaging reassessment rather than immediate intervention.',
    'Review bevacizumab-related bleeding, thrombosis and wound-healing concerns before use. Improvement in edema is not proof that all viable tumor is absent. Continue monitoring symptoms, steroid exposure and imaging, and reconsider the diagnosis if the course diverges from the expected response rather than repeatedly treating an unverified mechanism.')],['RN','BM'])

add('Lymphoma, metastases and oncologic complications','Ifosfamide-Associated Encephalopathy',
 'During an ifosfamide-containing regimen, a patient develops acute confusion and somnolence without a new focal deficit. Which response is most appropriate?',
 'Interrupt ifosfamide and urgently assess treatment toxicity and competing metabolic, infectious or neurologic causes',[
 ('Continue the infusion and reassess after the planned chemotherapy cycle','Acute CNS toxicity can be severe; continuing the suspected drug without immediate assessment may increase harm and delays evaluation of competing emergencies.'),
 ('Treat empirically for CNS tumor progression without reviewing the regimen','Progression can enter the differential, but the temporal drug association warrants toxicity assessment rather than automatic attribution to cancer growth.'),
 ('Give methylene blue as diagnostic confirmation and omit further workup if alertness improves','Methylene blue may be considered for selected cases, but response is not a specific diagnostic test and does not remove the need to assess other causes.')],
 [S('Recognize a Potentially Reversible Treatment Complication','**Ifosfamide can cause encephalopathy during or after administration.** Features range from altered attention and behavior to severe reduced consciousness or seizures.',
    'Stop the suspected exposure and assess airway, glucose, electrolytes, renal function, infection and relevant co-medications. Select imaging or EEG according to the examination and course.',
    'Renal dysfunction and other treatment factors can influence risk and clearance. No single bedside feature proves that the drug is the only cause.'),
  S('Provide Support and Review Rescue Options','**Use supportive care and specialist oncology/toxicology input.** Prescribing information allows consideration of methylene blue, but evidence is limited and it is not a substitute for stopping exposure and assessing physiology.',
    'Review contraindications and interactions, including serotonergic drugs and G6PD-related concerns, before any methylene-blue prescription. Apply the relevant institutional regimen rather than treating it as harmless empirical therapy.',
    'Monitor for recovery and seizures, and reconsider alternative explanations if the course is atypical. Decisions about future ifosfamide exposure require risk-benefit review and a prevention plan; recovery from one episode does not guarantee safe rechallenge. Keep other regimen-specific protective measures coordinated with the oncology team rather than stopping every supportive drug indiscriminately.')],['IFO'])

add('Raised pressure, hydrocephalus and low-pressure mimics','Papilledema Assessment Must Include Visual Function',
 'A patient with headache is found to have bilateral optic-disc swelling. Which initial assessment best establishes urgency and helps confirm papilledema?',
 'Expert disc assessment, BP measurement and documented visual acuity, pupils and formal visual fields',[
 ('Use preserved central visual acuity to assign a low-risk follow-up pathway','Acuity can remain preserved while visual fields deteriorate; central acuity alone does not establish low risk or exclude important pressure-related optic-nerve injury.'),
 ('Measure CSF opening pressure immediately before confirming the disc findings','LP has a role after appropriate imaging and safety assessment, but should not precede structural evaluation or substitute for defining the optic-disc and visual status.'),
 ('Use an isolated retinal nerve-fiber-layer thickness measurement to establish the cause','OCT is valuable for documentation and follow-up, but thickness alone does not distinguish every cause of swelling or replace clinical assessment and imaging.')],
 [S('Confirm What the Disc Finding Represents','**Papilledema is optic-disc swelling caused by raised intracranial pressure.** Other disc disorders and pseudopapilledema can look similar and may require experienced ophthalmic review.',
    'Measure BP to identify a hypertensive emergency and examine acuity, pupils, fields and the fundus. Document severity with photographs or OCT when available.',
    'Central acuity can be normal early. Formal fields can reveal important loss that changes urgency even when the patient reports only headache.'),
  S('Investigate the Cause While Protecting Vision','**Arrange urgent brain imaging with venous assessment when raised pressure is suspected.** Exclude a mass, hydrocephalus and cerebral venous thrombosis before assigning an idiopathic label.',
    'After appropriate imaging and exclusion of contraindications, LP measures opening pressure and checks CSF contents. The safest sequence depends on the clinical condition.',
    'Rapid visual deterioration requires urgent specialist treatment planning rather than routine headache follow-up. Continue objective visual monitoring throughout investigation; reducing headache does not establish that the optic nerves are safe. If disc swelling is uncertain, seek expert confirmation rather than either exposing the patient to unnecessary invasive tests or dismissing possible sight-threatening disease.')],['IIH','PAP','LP'])

add('Raised pressure, hydrocephalus and low-pressure mimics','Venous Imaging Before an Idiopathic Pressure Label',
 'An adult with confirmed papilledema has no mass or hydrocephalus on routine brain MRI. Which additional investigation is important before diagnosing IIH?',
 'MR or CT venography to exclude cerebral venous sinus thrombosis',[
 ('Carotid Doppler ultrasonography as the principal vascular exclusion test','Carotid imaging addresses selected arterial questions, but does not adequately assess dural venous sinus thrombosis causing raised pressure.'),
 ('Repeat routine MRI after a weight-loss trial','Follow-up imaging can be useful later, but weight or demographic features do not justify postponing the initial exclusion of a venous cause.'),
 ('Use transverse-sinus narrowing on routine MRI as proof of idiopathic disease','Sinus narrowing can accompany IIH and requires appropriate interpretation; it is not equivalent to excluding thrombosis or establishing an idiopathic mechanism.')],
 [S('A Normal Structural Scan Is Not the Complete Workup','**Venous sinus thrombosis can produce papilledema and raised CSF pressure without a mass lesion.** A routine MRI report may not answer the venous question.',
    'The IIH consensus pathway calls for CT or MR venography in the urgent investigation, generally within 24 hours. Seek neuroradiology advice when flow artifacts or unusual anatomy make interpretation uncertain.',
    'Assess pregnancy-related, thrombotic, inflammatory and other risks according to context, but absence of a recognized risk factor does not itself exclude thrombosis.'),
  S('Diagnose Idiopathic Disease Only After Relevant Exclusions','**Complete the neurologic, ocular and laboratory assessment** and perform LP when safe to document pressure and normal CSF composition.',
    'Review medicines and systemic conditions associated with secondary pressure elevation. Obesity, pulsatile tinnitus or an empty sella can support suspicion but do not establish idiopathic disease.',
    'Confirmed thrombosis changes management to a disease-specific venous pathway. A negative venogram does not alone diagnose IIH; it removes one important alternative within a broader framework. Continue visual-risk assessment during the investigation and avoid treating apparent headache improvement as evidence that secondary causes have been excluded.')],['IIH','PAP'])

R['IIHWT']=('IIH Weight Trial: bariatric surgery versus community weight management, 2021','https://pubmed.ncbi.nlm.nih.gov/33900360/')
R['WEIGHT']=('IIH weight-management systematic review and practice recommendations, 2023','https://pubmed.ncbi.nlm.nih.gov/37813577/')

add('Raised pressure, hydrocephalus and low-pressure mimics','Opening Pressure Requires Technique and Context',
 'After appropriate normal imaging and venography, a patient with suspected IIH undergoes LP while anxious, sitting and straining. The recorded pressure is 29 cm CSF. Which interpretation is most appropriate?',
 'The measurement is not a reliable standard opening pressure; reassess technique and the full diagnostic evidence',[
 ('The value confirms IIH independently of the examination and CSF contents','An elevated pressure alone does not establish idiopathic disease, especially when technique is nonstandard; visual, imaging, CSF and exclusion findings remain necessary.'),
 ('Apply a fixed correction factor to convert the sitting pressure into a diagnostic lateral-decubitus value','There is no universal arithmetic correction that replaces an appropriately obtained measurement; position and straining can materially affect interpretation.'),
 ('The value excludes IIH because it is below 30 cm CSF','Adult diagnostic thresholds are around 25 cm CSF rather than a universal 30-cm cutoff; the issue here is reliability and integrated interpretation.')],
 [S('Measure Under Appropriate Conditions','**Measure opening pressure in the lateral decubitus position**, with the patient relaxed and legs extended, allowing the manometer level to settle.',
    'Avoid interpreting straining, breath holding or an improperly positioned recording as the standard value. Document technical limitations and relevant sedation or distress.',
    'The 2018 consensus uses an adult cutoff above 25 cm CSF, while diagnostic frameworks often express an elevated threshold at or above 25; borderline values require clinical interpretation rather than false precision.'),
  S('A Number Does Not Replace the Syndrome','**Pressure must be interpreted with papilledema, neurologic findings, imaging and normal CSF composition.** Exclude secondary causes before assigning an idiopathic label.',
    'A single measurement samples a fluctuating physiologic variable. If it conflicts with a convincing syndrome, expert review may support repeat assessment rather than automatic acceptance or exclusion.',
    'Do not perform repeated LP simply to chase a number or use an unsafe procedure when structural contraindications exist. Assess visual risk throughout the workup. The need for urgent vision-protecting treatment is determined by the clinical state, not by waiting for an arbitrarily more dramatic pressure reading.')],['IIH','LP'],style='direct')

add('Raised pressure, hydrocephalus and low-pressure mimics','Medicine-Associated Intracranial Hypertension',
 'A patient develops papilledema and raised CSF pressure after starting doxycycline. Brain imaging and venography exclude structural and thrombotic causes. Which next step is most appropriate?',
 'Review and withdraw the suspected medicine through a coordinated plan while protecting vision and assessing other contributors',[
 ('Retain an idiopathic diagnosis because venography is negative','Negative venography excludes one important mechanism, but does not eliminate medicine-associated or other secondary pressure elevation.'),
 ('Continue doxycycline and treat the pressure without reviewing its indication','Pressure treatment may be necessary, but failure to address a plausible medication trigger can perpetuate the problem when alternatives are available.'),
 ('Use the timing alone as sufficient proof and omit visual follow-up','The temporal relationship supports suspicion but does not prove exclusive causality or remove the need to monitor and protect visual function.')],
 [S('Look Beyond the Usual Demographic Pattern','**Tetracyclines and vitamin A derivatives are important medication associations** with intracranial hypertension. Review prescriptions, supplements and recent changes.',
    'Other medicines and systemic conditions have been reported, but the strength of causal evidence varies. Do not describe every historical association as an equally established cause.',
    'Obesity or a typical demographic profile does not make secondary evaluation unnecessary. A medication-associated syndrome can resemble IIH clinically.'),
  S('Remove Contributors Without Delaying Vision Care','**Discuss cessation or substitution with the treating clinician**, considering the original indication and the seriousness of the neurologic problem.',
    'Document visual acuity, fields and disc status and treat pressure-related visual risk according to severity. Drug withdrawal is not a reason to wait passively when vision is deteriorating.',
    'Continue assessment of other contributors and follow objective improvement. Re-exposure should be considered carefully rather than used as a diagnostic challenge. Explain that a plausible drug association does not guarantee immediate resolution and that persistent symptoms require reassessment for another cause or ongoing pressure injury.')],['IIH','PAP'])

add('Raised pressure, hydrocephalus and low-pressure mimics','Sustained Weight Loss in Typical IIH',
 'A woman with active IIH and BMI 39 has stable mild visual loss under specialist monitoring. Which long-term intervention addresses a central disease-modifying mechanism?',
 'A supported sustained weight-loss strategy, including bariatric assessment when appropriate',[
 ('Repeated therapeutic LP as the long-term disease-modifying intervention','LP can temporarily reduce CSF pressure in selected circumstances, but fluid is replenished and serial punctures are not the preferred sustained disease-modifying strategy.'),
 ('Analgesic escalation as the principal way to reverse the underlying disease','Headache treatment is important, but analgesia does not address the pressure-related disease mechanism and overuse can add another headache problem.'),
 ('Permanent high-dose corticosteroids to maintain pressure remission','Long-term steroids add substantial toxicity and can promote weight gain; they are not the recommended disease-modifying strategy for typical IIH.')],
 [S('Treat Weight as a Supported Medical Intervention','**Sustained weight loss can reduce intracranial pressure in typical obesity-associated IIH.** Discuss structured care without attributing the illness to personal failure.',
    'The IIH Weight Trial enrolled women with active disease and BMI at least 35 and found greater sustained pressure reduction with bariatric surgery than community weight management.',
    'This evidence applies to an eligible selected population, not a mandate for surgery in every patient. Assess comorbidity, nutritional needs, preferences and local eligibility.'),
  S('Weight Management Does Not Replace Immediate Visual Protection','**Continue pressure-lowering and visual-monitoring treatment as indicated.** Rapidly worsening vision requires urgent intervention rather than waiting for weight loss.',
    'Lifestyle, specialist obesity pharmacotherapy and metabolic surgery have different evidence, risks and access; choose an individualized sustainable plan and monitor its effect.',
    'Follow papilledema and fields as well as weight and headache. Weight regain can be associated with recurrence, so long-term support matters. A patient may have persistent migraine-like headache despite pressure improvement; distinguish that symptom burden from active sight-threatening disease rather than escalating pressure procedures solely because pain continues.')],['IIHWT','WEIGHT','IIH'])

add('Raised pressure, hydrocephalus and low-pressure mimics','Acetazolamide for IIH With Mild Visual Loss',
 'A patient with confirmed IIH and mild visual field loss is starting acetazolamide alongside weight management. Which prescribing approach is most appropriate?',
 'Start a tolerated dose, often 250–500 mg twice daily, and titrate with renal and electrolyte safety review',[
 ('Start 4 g/day immediately because every patient requires the trial maximum','The IIH Treatment Trial allowed up to 4 g/day, but tolerability varies; a maximum studied dose is not an obligatory starting dose.'),
 ('Use acetazolamide only as an acute analgesic during headache attacks','Its main role is reducing CSF production and supporting visual outcomes in selected IIH, not as an as-needed acute migraine analgesic.'),
 ('Increase the dose until headache resolves regardless of visual findings or adverse effects','Headache can persist for other reasons and dose-limiting toxicity matters; titration should follow the overall disease and safety assessment, not pain alone.')],
 [S('Use Evidence Within Its Clinical Population','**Acetazolamide inhibits carbonic anhydrase and reduces CSF production.** Trial evidence shows modest visual-field benefit when added to a weight-reduction diet in patients with mild visual loss.',
    'A common starting range is ==250–500 mg twice daily==, increasing as tolerated. The trial maximum was ==4 g/day==, not a required target for all patients.',
    'Severe or rapidly progressive visual decline requires urgent procedural assessment; tablets should not be used to postpone needed vision-protecting intervention.'),
  S('Anticipate Toxicity and Monitor Function','**Discuss paresthesia, fatigue, altered taste and gastrointestinal effects**, as well as metabolic acidosis, electrolyte disturbance and renal stone risk.',
    'Review kidney function, bicarbonate/electrolytes and relevant contraindications or interactions. Pregnancy and reproductive counseling require individualized specialist advice.',
    'Follow formal visual fields and disc findings, not just headache intensity. Adjust or change treatment when intolerance prevents a useful course rather than urging an unsustainable dose. Continue weight management and a separate headache strategy where needed; acetazolamide benefit for vision does not establish it as effective treatment of headache alone.')],['IIH','WEIGHT'])

R['NPH']=('Japanese Society iNPH management guideline, third edition, 2021','https://pmc.ncbi.nlm.nih.gov/articles/PMC7905302/')

add('Raised pressure, hydrocephalus and low-pressure mimics','Rapid Visual Deterioration in IIH',
 'A patient with confirmed IIH has rapidly worsening visual fields and papilledema despite medical therapy. Which next approach is most appropriate?',
 'Urgent specialist assessment for vision-protecting intervention such as CSF diversion or optic nerve sheath fenestration',[
 ('Continue weight loss alone and repeat fields after several months','Weight loss modifies typical IIH over time, but cannot be relied on to protect vision during rapid current deterioration.'),
 ('Increase analgesia and use headache response to decide whether surgery is needed','Headache and visual risk are different outcomes; improvement in pain does not establish that progressive optic-nerve injury has stopped.'),
 ('Schedule serial outpatient LPs as the definitive long-term intervention','Temporary drainage can bridge selected urgent situations, but repeated punctures are not definitive treatment for rapidly threatened vision.')],
 [S('Treat Vision Loss as the Urgent Endpoint','**Declining visual function in IIH requires urgent intervention planning.** Formal fields, acuity and disc findings define the threat more reliably than headache severity alone.',
    'Confirm the trend and coordinate neuro-ophthalmology and neurosurgery promptly. Do not wait for profound central acuity loss before escalating.',
    'A temporizing CSF drainage strategy may be used by specialists while definitive treatment is arranged, with appropriate procedural safety assessment.'),
  S('Individualize the Procedure and Follow-Up','**CSF diversion and optic nerve sheath fenestration have selected roles**, influenced by visual pattern, overall symptoms, local expertise and patient factors.',
    'Shunts can obstruct, become infected or cause overdrainage; fenestration also has procedural risks and does not treat every aspect of the pressure syndrome. Venous stenting is not an automatic replacement based on narrowing alone.',
    'Continue disease modification and objective visual monitoring after intervention. A technically successful procedure does not guarantee recovery of established optic atrophy. Recurrent headache or visual change needs reassessment for active pressure, treatment complications and other mechanisms rather than automatic repetition of the original operation.')],['IIH','PAP'])

add('Raised pressure, hydrocephalus and low-pressure mimics','Persistent Headache After Papilledema Resolves',
 'A patient previously treated for IIH has stable visual fields and resolved papilledema but persistent migraine-like headache with frequent analgesic use. Which approach is most appropriate?',
 'Assess headache phenotype and medication overuse while maintaining appropriate visual surveillance',[
 ('Perform regular therapeutic LP solely to maintain headache relief','LP may provide transient relief but is not recommended as routine headache treatment; repeated procedures can cause harm and do not address medication overuse or migraine mechanisms.'),
 ('Recommend CSF diversion solely because headache persists','Shunting is not generally recommended for headache alone without appropriate reassessment; persistent pain does not prove ongoing sight-threatening pressure elevation.'),
 ('Escalate acetazolamide until pain stops despite stable ocular findings','Acetazolamide is not established as headache-only therapy and dose escalation adds toxicity; the current phenotype requires a separate headache assessment.')],
 [S('Separate Ocular Remission From Symptom Burden','**Headache can persist after the pressure-related ocular disease improves.** Migraine biology, medication overuse and other contributors can coexist with prior IIH.',
    'Review frequency, triggers, positional features and analgesic days. New visual symptoms or an altered pattern warrants renewed assessment rather than assuming every headache is the same.',
    'Continue an appropriate follow-up plan for recurrence risk; resolved papilledema does not mean the patient’s pain is unimportant or that future pressure disease is impossible.'),
  S('Use a Headache-Specific Plan','**Treat the demonstrated headache phenotype**, including medication-overuse management and suitable preventive therapy when indicated.',
    'Choose medicines with attention to weight, mood, cognition, reproductive considerations and existing treatment. Explain that pain relief and visual protection are separate treatment goals.',
    'Serial LP is not routine long-term care, and CSF diversion should not be recommended solely from persistent pain without expert evaluation. If symptoms suggest shunt malfunction or low pressure in a previously operated patient, investigate those possibilities specifically. Objective visual and neurologic reassessment helps avoid both unnecessary pressure procedures and dismissal of a genuine recurrence.')],['IIH'])

add('Raised pressure, hydrocephalus and low-pressure mimics','Acute Obstructive Hydrocephalus',
 'A patient with a posterior-fossa mass develops vomiting and reduced consciousness. CT shows ventricular enlargement proximal to an obstructed CSF pathway. Which next approach is most appropriate?',
 'Urgent neurosurgical assessment for controlled ventricular CSF diversion and treatment of the obstruction',[
 ('Perform a large-volume lumbar puncture as the initial decompression','A posterior-fossa mass with obstructive pressure gradients can make lumbar drainage dangerous; ventricular and definitive structural treatment require neurosurgical planning.'),
 ('Treat with acetazolamide and arrange elective imaging review','Medical CSF reduction can have selected roles, but does not adequately address acute neurologic deterioration from an obstructed pathway.'),
 ('Begin an outpatient normal-pressure-hydrocephalus tap-test pathway','That evaluation concerns a chronic clinical syndrome after appropriate assessment; it is inappropriate for acute obstructive deterioration with a mass lesion.')],
 [S('Identify the Obstruction and Clinical Threat','**Obstructive hydrocephalus results from impaired passage through a CSF pathway.** Imaging defines the level and accompanying mass effect.',
    'Reduced consciousness, vomiting and progressive neurologic signs require emergency assessment and physiologic stabilization. A chronic ventriculomegaly workup must not replace the acute pathway.',
    'Protect airway and perfusion as needed while urgently involving neurosurgery; do not delay action to obtain every elective diagnostic sequence.'),
  S('Choose Diversion With the Anatomy in Mind','**An external ventricular drain or another appropriate procedure can provide controlled diversion**, with definitive treatment directed at the cause. Endoscopic third ventriculostomy suits selected obstruction patterns, not every hydrocephalus.',
    'Drainage rate and pressure require specialist control because abrupt pressure shifts can be hazardous, particularly with posterior-fossa lesions.',
    'Lumbar puncture is not a safe universal decompression method. Assess infection, hemorrhage and procedural risks and continue monitoring after diversion. Persistent or recurrent deterioration requires review of drain function and the underlying lesion rather than assuming ventricular enlargement alone explains every subsequent problem.')],['LP','NICE'])

add('Raised pressure, hydrocephalus and low-pressure mimics','A Negative Tap Test Does Not End an iNPH Evaluation',
 'An older adult has gait-predominant impairment, urinary urgency and cognitive slowing. MRI shows ventriculomegaly with a DESH pattern. One tap test shows no clear immediate improvement. Which interpretation is most appropriate?',
 'Reassess test quality, timing, comorbidity and the overall syndrome; a negative tap test does not exclude shunt responsiveness',[
 ('Exclude iNPH because the first post-LP assessment is negative','Tap testing has false negatives and response may require appropriately timed objective assessment; one negative observation cannot independently exclude the diagnosis or benefit.'),
 ('Proceed to shunting solely because ventricles are enlarged','Ventriculomegaly can accompany atrophy or other disorders; clinical correlation, differential assessment and procedural risk-benefit review remain necessary.'),
 ('Diagnose Alzheimer disease from cognitive slowing and stop gait assessment','Neurodegeneration can coexist, but the gait-dominant syndrome and imaging warrant integrated assessment rather than assigning all findings to one cognitive diagnosis.')],
 [S('Recognize the Clinical-Imaging Pattern','**iNPH commonly produces gait impairment with cognitive and urinary symptoms**, but the complete triad is neither uniquely diagnostic nor present in every patient.',
    'DESH includes ventriculomegaly with tight high-convexity spaces and relatively enlarged Sylvian fissures. It supports the diagnosis without making other causes irrelevant.',
    'Assess parkinsonism, neuropathy, vascular disease, orthopedic limitations and neurodegeneration because each can alter gait or expected recovery.'),
  S('Interpret Drainage Testing as a Predictor With Limits','**Use objective baseline and post-drainage measures**, including gait timing and suitable delayed reassessment. A limited immediate examination can miss a clinically relevant response.',
    'Specialists may consider repeat or extended assessment when the overall suspicion remains high. Neither a negative test nor a DESH pattern alone resolves every treatment decision.',
    'Discuss shunt risks, comorbidity and realistic domain-specific benefit; gait may improve differently from cognition. Do not promise complete reversal of dementia or treat age alone as a veto. Follow function and complications after any procedure and reassess deterioration for malfunction, overdrainage or a coexisting progressive disorder.')],['NPH'])

R.update({
 'SIH':('Multidisciplinary spontaneous intracranial hypotension guideline, 2023','https://pmc.ncbi.nlm.nih.gov/articles/PMC10511987/'),
 'ACMG':('ACMG/AMP standards for sequence variant interpretation, 2015','https://doi.org/10.1038/gim.2015.30'),
 'VUS':('NHS Genomics Education: variant of uncertain significance','https://www.genomicseducation.hee.nhs.uk/genotes/knowledge-hub/variant-of-uncertain-significance-vus/'),
})

add('Raised pressure, hydrocephalus and low-pressure mimics','Spontaneous Intracranial Hypotension With Normal Opening Pressure',
 'A patient has a new headache that worsens upright and improves recumbent, with supportive brain MRI findings. A previous LP opening pressure was within range. Which interpretation is most appropriate?',
 'A normal opening pressure does not exclude a spinal CSF leak syndrome',[
 ('The pressure excludes SIH and establishes migraine','Migraine can have positional aggravation, but a normal pressure does not exclude SIH; the orthostatic history and imaging require integrated evaluation.'),
 ('Repeat LP is required solely to demonstrate low pressure before further imaging','LP is not recommended merely to confirm SIH because pressure can be normal and the procedure can create another leak; appropriate MRI and specialist review come first.'),
 ('Low-lying cerebellar tonsils establish congenital Chiari disease as the cause','Brain sag from CSF volume loss can mimic tonsillar descent; interpreting that feature without the broader MRI and clinical pattern can lead to inappropriate treatment.')],
 [S('A CSF-Volume Disorder Can Have a Normal Measured Pressure','**SIH usually results from a spinal dural leak or CSF-venous fistula.** The syndrome name does not mean that every patient has a low LP reading.',
    'Orthostatic headache is characteristic, but its timing and prominence can evolve. Associated neck, auditory, vestibular or cognitive symptoms can contribute to recognition.',
    'Brain MRI may show pachymeningeal enhancement, venous engorgement, brain sag or subdural collections; normal MRI does not exclude every case.'),
  S('Investigate Without Creating an Unnecessary Puncture','**First-line imaging generally includes contrast brain MRI and whole-spine MRI.** Spinal imaging can guide the leak pathway but may not localize the exact defect.',
    'Do not perform LP solely to prove low pressure. If CSF sampling is needed for another diagnostic question, discuss its risks and interpret pressure in context.',
    'Assess orthostatic hypotension, postural tachycardia, migraine and other mimics according to symptoms. A strongly suggestive case with normal initial studies warrants expert review rather than automatic dismissal. Significant subdural collections or neurologic decline require urgent specialist assessment, and treating the underlying leak can be central to preventing recurrent complications.')],['SIH'])

add('Raised pressure, hydrocephalus and low-pressure mimics','Blood Patch and Leak Localization',
 'A patient has clinically and radiologically supported SIH without a localized leak. Which initial treatment pathway is generally appropriate?',
 'Offer an early non-targeted epidural blood patch, with specialist localization if response is absent or transient',[
 ('Require invasive myelographic localization before any blood patch','Myelography is important for selected persistent cases and targeted treatment, but an initial non-targeted patch can be offered without first identifying the precise defect.'),
 ('Use repeated diagnostic LPs to remove pressure before patching','Removing CSF does not treat a spinal leak and can worsen the problem; repeated diagnostic punctures are not a therapeutic pathway for supported SIH.'),
 ('Continue indefinite bed rest and caffeine before considering intervention','Conservative measures can be used briefly, but prolonged deferral of an indicated patch can extend disability and does not reliably close a persistent leak.')],
 [S('Treat Early and Assess the Response','**Non-targeted epidural blood patch is a first-line treatment in the consensus pathway.** Short conservative measures should not turn into an indefinite prerequisite for intervention.',
    'An experienced service generally aims for at least 20 mL and up to 40 mL of autologous blood as tolerated, stopping for significant pressure or radicular symptoms. Patient anatomy and procedural safety determine the actual prescription.',
    'Discuss bleeding, infection and neurologic risks and provide post-procedure observations and advice. A temporary response can be useful information without proving permanent leak closure.'),
  S('Localize Persistent Disease to Plan Targeted Care','**CT or digital-subtraction myelography is selected according to the suspected leak type and spine MRI pattern.** CSF-venous fistulas require a different localization strategy from a fast ventral dural leak.',
    'Persistent or recurrent symptoms can lead to another patch or expert localization and targeted patching, surgery or selected embolization rather than endless empirical punctures.',
    'Explain rebound high-pressure headache after treatment; a changed positional pattern should prompt reassessment rather than automatic repetition of the patch. Track function and orthostatic symptoms at follow-up and review alternative diagnoses if the expected response is absent. Treatment success is clinical and mechanistic, not dependent on making every MRI feature normal immediately.')],['SIH'])

add('Neurogenetic syndromes and testing','Choose a Genetic Test From the Clinical Question',
 'An adult with a progressive neurologic syndrome and a suggestive family history requests genetic testing. Which approach is most appropriate before ordering a broad panel?',
 'Define phenotype and pedigree, assess acquired mimics and counsel about scope, limitations and possible results',[
 ('Order the largest available panel and interpret any rare variant as the cause','Broad testing can help selected cases, but rare variants are common and require evidence; panel size does not replace phenotype, inheritance and variant interpretation.'),
 ('Use family history alone to select predictive testing in an unaffected relative first','When feasible an affected proband is usually the informative starting point; predictive testing needs a clear familial target and an appropriate counseling pathway.'),
 ('Assume a negative exome would exclude inherited disease and order it without further discussion','Exome testing has limitations for repeats, structural changes, mosaicism and other mechanisms; consent should address these limits rather than promise exclusion.')],
 [S('Make the Diagnostic Question Explicit','**Phenotype and pedigree determine the most informative assay.** Document onset, progression, neurologic domains and relevant systemic features and consider actionable acquired mimics.',
    'A three-generation family history can suggest inheritance but may be limited by small families, variable expression, reduced penetrance or de novo disease.',
    'Testing may require a targeted variant, repeat assay, copy-number method, panel, exome, genome or mitochondrial strategy rather than one universal platform.'),
  S('Consent Includes Uncertainty and Family Implications','**Discuss pathogenic, negative and uncertain results**, possible secondary findings where relevant, and the practical implications for relatives and reproductive decisions.',
    'Clarify whether testing is diagnostic in an affected person or predictive in someone without symptoms. The counseling and consent requirements differ.',
    'Use an appropriate clinical laboratory and specialist interpretation and explain the possibility of later reanalysis. A result should inform care through established evidence rather than create a diagnosis from a rare sequence change alone. Protect autonomy and confidentiality, and plan how results will be communicated and followed up instead of treating ordering the test as the end of the evaluation.')],['ACMG','VUS'])

add('Neurogenetic syndromes and testing','A VUS Is Not a Confirmed Molecular Diagnosis',
 'A panel identifies a variant of uncertain significance in a gene associated with the patient’s broad neurologic phenotype. Which next action is most appropriate?',
 'Continue clinical evaluation and seek appropriate segregation or reclassification evidence without treating the VUS as causal',[
 ('Use the VUS to initiate irreversible gene-specific treatment','A VUS lacks sufficient evidence for pathogenic attribution and should not independently drive irreversible treatment; management can still follow the demonstrated clinical syndrome.'),
 ('Offer relatives predictive testing as though a pathogenic familial variant were established','Family sampling may help segregation analysis, but predictive clinical interpretation requires more than an uncertain finding and should not label relatives affected or unaffected.'),
 ('Classify the variant as benign because uncertainty means no biological effect','Uncertain is neither pathogenic nor benign; evidence can change the classification and a plan for expert review or reanalysis may be appropriate.')],
 [S('Understand the Classification','**A VUS has insufficient evidence for a pathogenic or benign conclusion.** It is not a partial confirmation of disease and should not be used as the basis of clinical decision-making.',
    'Population frequency, segregation, functional evidence, mechanism and phenotype can contribute to later classification. A plausible gene name alone does not establish causality.',
    'A negative or uncertain panel also does not exclude every inherited mechanism; review whether the relevant variant classes were assessed.'),
  S('Use Family Information for the Right Purpose','**Selected family testing can help resolve uncertainty**, especially when coordinated with the laboratory and genetics service. This is different from treating the VUS as an established predictive marker.',
    'Continue symptom-based care and surveillance justified by the clinical findings or family history, rather than by the uncertain sequence result alone.',
    'Document the interpretation, explain that classification can change and arrange an appropriate recontact or reanalysis process. Avoid providing false reassurance from a benign-sounding uncertain report or imposing major lifestyle and reproductive conclusions from an unsupported causal claim. A later pathogenic reclassification requires renewed phenotype and inheritance review before changing family-specific advice.')],['ACMG','VUS'],style='direct')

R.update({
 'RFC1':('GeneReviews: RFC1-related disorders, updated 2026','https://www.ncbi.nlm.nih.gov/books/NBK564656/'),
 'HD':('GeneReviews: Huntington disease','https://www.ncbi.nlm.nih.gov/books/NBK1305/'),
 'MELAS':('GeneReviews: MELAS','https://www.ncbi.nlm.nih.gov/books/NBK1233/'),
 'MELAS26':('MELAS and stroke-like episode consensus statements, 2026','https://pmc.ncbi.nlm.nih.gov/articles/PMC13090769/'),
})

add('Neurogenetic syndromes and testing','A Negative Exome Does Not Exclude a Repeat Disorder',
 'An adult has progressive ataxia, sensory neuronopathy and bilateral vestibular dysfunction. A standard exome report is negative. Which next testing principle is most appropriate?',
 'Review assay coverage and arrange validated repeat-expansion testing for a compatible disorder such as RFC1-related disease',[
 ('Exclude an inherited cause because coding exome sequencing was negative','Standard exome testing does not reliably detect many noncoding repeat expansions; the phenotype warrants checking which mechanisms were actually assayed.'),
 ('Repeat the same exome analysis without assessing repeat detection capability','Reanalysis can find newly recognized sequence variants, but does not automatically solve a repeat-expansion question outside the assay’s validated scope.'),
 ('Use a single uncertain coding variant to explain the syndrome instead','A VUS cannot replace evidence for the likely mechanism; forcing an uncertain coding result into the diagnosis risks missing a separately testable repeat disorder.')],
 [S('Match the Variant Class to the Assay','**Standard exome sequencing mainly assesses coding sequence and is not a universal repeat-expansion test.** Negative results must be interpreted against validated platform coverage.',
    'RFC1-related disease is an important example of an intronic repeat mechanism. Repeat motif, zygosity and technical limitations influence appropriate testing and interpretation.',
    'Some validated genome or long-read approaches can detect expansions, but do not assume that every commercial genome report has assessed them adequately.'),
  S('Use Phenotype to Choose the Next Step','**Combined cerebellar, sensory and vestibular dysfunction raises RFC1 suspicion**, often with chronic cough, but the spectrum can be incomplete.',
    'Exclude acquired mimics and other inherited ataxias according to context. A negative family history does not exclude a recessive late-onset condition.',
    'Confirm findings through a suitable clinical assay and genetics interpretation before family advice. The correct response to a negative broad test is not indefinite repetition without a mechanistic question; review repeats, copy-number changes, mitochondrial variants, mosaicism and other gaps relevant to the phenotype. A targeted test can be more informative than a larger panel that misses the required variant class.')],['RFC1','ACMG'])

add('Neurogenetic syndromes and testing','Predictive Huntington Testing Requires Voluntary Counseling',
 'An asymptomatic adult whose parent has molecularly confirmed Huntington disease requests testing. Which approach is most appropriate?',
 'Offer voluntary predictive testing through a structured genetics pathway with informed consent and psychological support',[
 ('Order HTT testing automatically because the family history establishes the adult’s preference','A familial risk does not establish consent; predictive testing requires an autonomous decision and discussion of personal and family consequences.'),
 ('Use a routine exome panel as the preferred substitute for an HTT repeat assay','Huntington disease requires an appropriately validated HTT CAG-repeat analysis; a standard sequence panel may not answer that question.'),
 ('Promise that a positive result will determine the exact age of onset','Repeat length influences risk and onset distribution, but cannot provide a precise individual onset date; modifiers and variability must be discussed.')],
 [S('Separate Predictive From Diagnostic Testing','**Testing an unaffected at-risk adult predicts genetic risk rather than explaining current symptoms.** Confirm the family diagnosis and provide a meaningful opportunity to accept or decline testing.',
    'Discuss psychological readiness, confidentiality, reproductive options and implications for relatives. Family pressure is not a substitute for consent.',
    'Asymptomatic minors are generally not tested for an adult-onset condition without childhood medical benefit; a symptomatic child requiring diagnostic evaluation is a different situation.'),
  S('Interpret the Repeat Range Carefully','**HTT alleles with 36–39 CAG repeats have reduced penetrance**, while alleles of 40 or more are generally full-penetrance disease-associated alleles.',
    'Intermediate alleles, commonly 27–35 repeats, do not ordinarily cause the classical disorder in the individual but can have transmission-instability implications. Laboratory methods and repeat interruptions can complicate borderline interpretation.',
    'Do not convert a repeat count into a guaranteed onset year or severity. Arrange results disclosure and follow-up with appropriate support, including mental-health assessment where indicated. Diagnostic certainty and the person’s future support needs are different questions, and a predictive result should not remove access to counseling or the right to make independent life decisions.')],['HD','ACMG'])

add('Neurogenetic syndromes and testing','Heteroplasmy and Tissue Choice',
 'A patient with multisystem neurologic disease has a maternal family history suggestive of an mtDNA disorder. Blood testing is unrevealing. Which interpretation is most appropriate?',
 'Review the suspected variant, assay sensitivity and tissue-specific heteroplasmy before excluding mitochondrial disease',[
 ('Exclude mitochondrial disease because an mtDNA variant must be equally detectable in all tissues','Heteroplasmy can vary across tissues and over time; a negative blood result does not exclude every mtDNA disorder.'),
 ('Assume every mitochondrial disorder follows maternal inheritance','Many mitochondrial diseases arise from nuclear genes with Mendelian inheritance; maternal transmission applies to mtDNA mechanisms, not the entire category.'),
 ('Use a mildly raised lactate as sufficient molecular confirmation','Lactate can rise with seizures, sampling conditions and systemic illness; it supports selected assessments but does not establish the genetic mechanism.')],
 [S('Distinguish mtDNA From Nuclear Mechanisms','**Mitochondrial disease can result from mtDNA or nuclear variants.** The inheritance pattern, affected systems and assay must be considered together.',
    'Heteroplasmy is the coexistence of different mtDNA populations, with variable proportions between tissues. Threshold effects and tissue energy demand contribute to clinical variability.',
    'The same maternal family can therefore show different severity or organ involvement; a mildly affected relative does not establish a mild prognosis for every family member.'),
  S('Choose the Sample and Interpret a Negative Result','**A blood assay has a defined detection limit and may not represent every affected tissue.** Specialist testing can involve urine epithelial cells or selected other tissue depending on the suspected disorder.',
    'Review whether sequencing, deletion and low-level heteroplasmy detection were appropriate. Invasive biopsy is not automatically the next step if a suitable less invasive molecular strategy is available.',
    'Assess cardiac, endocrine, hearing and other organ involvement where indicated. A normal lactate does not exclude disease and a raised result is not specific. Counseling should address mechanism-dependent inheritance and reproductive uncertainty rather than applying one recurrence percentage to every patient labeled mitochondrial.')],['MELAS','ACMG'])

add('Neurogenetic syndromes and testing','Mitochondrial Stroke-Like Episodes',
 'A young adult with hearing loss, diabetes and a maternal family history develops seizures, headache and evolving cortical deficits. MRI lesions extend across usual arterial territories. Which mechanism deserves particular consideration?',
 'A mitochondrial stroke-like episode such as MELAS',[
 ('An embolic arterial infarct as the only plausible cause','Arterial stroke remains an emergency differential, but evolving nonterritorial cortical lesions with multisystem maternal clues raise a mitochondrial episode rather than an exclusively embolic explanation.'),
 ('A primary demyelinating relapse from the cortical MRI pattern','Inflammatory disease can cause deficits and seizures, but the nonterritorial evolution and systemic inheritance clues require metabolic-genetic assessment.'),
 ('A primary psychiatric episode because deficits fluctuate','Fluctuation can occur in several neurologic disorders; seizures and objective evolving lesions require investigation rather than psychiatric attribution.')],
 [S('Recognize the Clinical-Radiologic Pattern','**MELAS can cause stroke-like episodes with seizures and cortical dysfunction**, often in association with hearing loss, diabetes, myopathy or other mitochondrial features.',
    'Lesions can evolve beyond a single arterial territory. MRI diffusion findings vary, so do not use one ADC rule as an absolute discriminator.',
    'Lactate and targeted molecular testing contribute to assessment, but neither a raised lactate nor maternal history alone establishes the diagnosis.'),
  S('Treat the Episode and Exclude Coincident Emergencies','**Provide urgent seizure assessment and treatment**, supportive metabolic care and specialist mitochondrial input. Monitor glucose, hydration, nutrition and systemic organ function.',
    'Do not assume that a known mitochondrial diagnosis excludes a true arterial stroke or another acute process. Reperfusion decisions require the actual mechanism and standard eligibility assessment.',
    'Evidence for adjunctive metabolic therapies, including arginine strategies, is uncertain and recommendations differ; do not present them as a proven universal substitute for seizure control and supportive care. Review medicine safety, including genotype-specific risks such as valproate in POLG-related disease. Longitudinal cardiac, endocrine, hearing and functional assessment and mechanism-specific counseling remain important after the acute episode.')],['MELAS','MELAS26'])

R.update({
 'CADASIL':('GeneReviews: CADASIL','https://www.ncbi.nlm.nih.gov/books/NBK1500/'),
 'NF1':('ERN GENTURIS NF1 tumor surveillance guideline, 2023','https://pmc.ncbi.nlm.nih.gov/articles/PMC9845795/'),
 'NF2':('GeneReviews: NF2-related schwannomatosis','https://www.ncbi.nlm.nih.gov/books/NBK1201/'),
 'TSC':('GeneReviews: tuberous sclerosis complex','https://www.ncbi.nlm.nih.gov/books/NBK1220/'),
 'TSCKID':('ERKNet/ERA TSC kidney consensus, 2024','https://doi.org/10.1038/s41581-024-00818-0'),
})

add('Neurogenetic syndromes and testing','CADASIL and NOTCH3 Interpretation',
 'A patient has migraine with aura, recurrent subcortical ischemic events and an autosomal-dominant family history. MRI shows extensive white-matter disease including anterior temporal and external-capsule involvement. Which etiologic investigation is most appropriate?',
 'Phenotype-informed NOTCH3 testing with genetic counseling',[
 ('HTT repeat analysis as the principal confirmatory test','HTT testing addresses Huntington disease, usually with a compatible movement and cognitive syndrome; it does not target this inherited small-vessel phenotype.'),
 ('AQP4-IgG testing as the principal confirmatory test','AQP4 testing helps compatible inflammatory opticospinal disease, but does not establish the cause of a dominant subcortical vascular syndrome.'),
 ('Use the MRI distribution alone as definitive confirmation','The pattern supports suspicion but is not uniquely diagnostic; molecular or selected specialist pathologic evidence is needed for a confirmed etiologic attribution.')],
 [S('Recognize an Inherited Small-Vessel Pattern','**CADASIL is associated with pathogenic NOTCH3 variants**, with variable migraine, ischemic, cognitive and psychiatric manifestations.',
    'Anterior temporal and external-capsule white-matter abnormalities are useful clues in the right context, but their absence does not exclude every presentation.',
    'Age-related or acquired vascular disease and other inherited leukoencephalopathies remain competing explanations. Review the pedigree and actual MRI rather than diagnosing from a single report phrase.'),
  S('Interpret the Result and Manage Vascular Risk','**Variant location, mechanism and phenotype influence interpretation.** A NOTCH3 VUS is not equivalent to a confirmed diagnosis; selected unresolved cases can require specialist skin-biopsy assessment.',
    'Control conventional vascular risks, including hypertension and smoking, and individualize secondary prevention according to the patient’s events and bleeding risk.',
    'Do not automatically anticoagulate solely for the genetic diagnosis or assume that ordinary stroke mechanisms cannot coexist. Counsel relatives through an appropriate predictive-testing pathway and explain variable expression. A molecular diagnosis informs risk and family advice but does not predict a precise onset age or guarantee identical severity across affected relatives.')],['CADASIL','ACMG'])

add('Neurogenetic syndromes and testing','A Changing Plexiform Neurofibroma in NF1',
 'An adult with established NF1 develops new persistent nocturnal pain, rapid enlargement and weakness related to a known plexiform neurofibroma. Which approach is most appropriate?',
 'Urgent expert assessment for malignant transformation with targeted imaging and tissue planning as indicated',[
 ('Observe until the next annual visit because plexiform lesions are congenital','Longstanding benign lesions can change; new persistent pain, altered growth and neurologic deficit are warning features requiring prompt assessment.'),
 ('Treat the pain alone and use analgesic response to exclude malignancy','Symptom relief does not establish benign biology; the structural and neurologic changes still require investigation.'),
 ('Resect without imaging or specialist planning because every painful lesion is malignant','These findings warrant urgent evaluation but are not pathologic proof; imaging and sarcoma/NF expertise guide safe sampling and treatment.')],
 [S('Recognize Warning Features','**NF1 increases the risk of malignant peripheral nerve sheath tumors.** Rapid growth, new persistent or nocturnal substantial pain, a hardening lesion and new neurologic deficits are concerning.',
    'A plexiform neurofibroma can cause symptoms without malignancy, so assessment must distinguish benign burden, atypical lesions and malignant change.',
    'Targeted MRI and selected metabolic imaging can guide evaluation and biopsy, but tissue strategy should account for heterogeneous lesions and sampling risk.'),
  S('Use Syndrome-Specific Surveillance','**NF1 care extends beyond counting skin lesions.** Assess neurologic symptoms, BP, pain and other age-appropriate tumor and systemic risks.',
    'Surveillance intensity and imaging are individualized; do not apply indiscriminate frequent brain scans to every asymptomatic adult as a substitute for clinical review.',
    'Refer suspicious change promptly to an experienced NF/sarcoma team. Genetic counseling should address dominant inheritance and variable expression, while symptom and functional management continue during investigation. Do not reassure solely because the lesion was previously labeled benign or attribute a new deficit automatically to ordinary neurofibroma growth.')],['NF1'])

add('Neurogenetic syndromes and testing','NF2-Related Schwannomatosis and Mosaicism',
 'A young adult has multiple schwannomas and meningiomas with a segmental distribution. Blood testing does not identify a pathogenic NF2 variant. Which interpretation is most appropriate?',
 'Mosaic NF2-related schwannomatosis remains possible; specialist testing may include affected tumor tissue',[
 ('The negative blood result excludes NF2-related disease','A mosaic variant may be absent or below detection in blood; clinical findings and appropriately selected tumor testing can remain informative.'),
 ('The absence of a family history establishes a nonhereditary sporadic process','De novo and mosaic disease can occur without an affected parent; family history alone does not exclude a tumor-predisposition syndrome.'),
 ('A single schwannoma specimen automatically establishes constitutional NF2 inheritance','Tumors can contain somatic changes; distinguishing constitutional and mosaic disease requires integrated testing rather than assuming a tumor variant is present in every tissue.')],
 [S('Use the Updated Syndrome Framework','**NF2-related schwannomatosis is characterized particularly by vestibular schwannomas**, with meningiomas and other nervous-system tumors in the spectrum.',
    'Bilateral vestibular schwannomas are a major diagnostic clue. Young patients with apparently isolated tumors can also require risk assessment rather than reassurance based only on limited current manifestations.',
    'Mosaicism can produce asymmetric or segmental disease and reduce the sensitivity of blood-only testing.'),
  S('Test and Counsel According to the Distribution','**Expert review can compare blood and appropriate tumor specimens**, including whether the same pathogenic variant is found in distinct tumors.',
    'A tumor-specific change is not automatically a germline finding. Assay sensitivity, tissue choice and clinical criteria influence the conclusion and recurrence counseling.',
    'Arrange syndrome-appropriate hearing, neurologic, ophthalmic and MRI surveillance and individualized treatment of threatening lesions. Preserve hearing and cranial-nerve function as meaningful goals. Family advice should reflect whether disease is constitutional or mosaic; do not give one recurrence estimate from the clinical label alone or use a negative blood report to stop an otherwise justified evaluation.')],['NF2','VS','ACMG'])

add('Neurogenetic syndromes and testing','Tuberous Sclerosis Needs Multisystem Follow-Up',
 'An adult with tuberous sclerosis has controlled epilepsy and no new neurologic symptoms. Which ongoing care principle is most appropriate?',
 'Continue structured multisystem surveillance, including renal imaging and function assessment',[
 ('Limit follow-up to seizures because other manifestations become irrelevant in adulthood','Renal, pulmonary and other complications can emerge or progress in adults; seizure control does not complete TSC care.'),
 ('Stop renal imaging after one normal ultrasound','TSC renal lesions can develop or change over time; a single reassuring study does not eliminate the need for longitudinal surveillance.'),
 ('Treat all renal angiomyolipomas surgically when first detected','Management depends on growth, size, bleeding risk and symptoms; observation, mTOR-directed therapy and selective intervention have different appropriate settings.')],
 [S('Connect Neurologic and Systemic Disease','**TSC involves TSC1/TSC2-related dysregulation of mTOR signaling**, with variable cerebral, renal, skin, pulmonary and other manifestations.',
    'Seizures, cortical lesions and subependymal tumors are important neurologic features, but stable epilepsy does not establish that the rest of the syndrome is inactive.',
    'Assess new headache, vomiting or focal signs for causes such as an enlarging SEGA and hydrocephalus, rather than assuming every symptom is a seizure consequence.'),
  S('Follow Risk Over the Life Course','**Renal surveillance includes periodic abdominal imaging**, commonly MRI every one to three years, with at least annual BP and kidney-function assessment according to the clinical situation.',
    'Growing angiomyolipomas can require mTOR therapy or other specialist management; acute hemorrhage has a separate urgent pathway. Preserve renal tissue where feasible.',
    'Pulmonary assessment and brain surveillance depend on age, sex, prior lesions and current guidance. Adults with prior SEGA can need continued imaging. Coordinate genetics, neurology and relevant organ specialists and address neuropsychiatric function and quality of life. Do not replace multisystem care with a single scan schedule or apply an intervention threshold without reviewing symptoms and bleeding risk.')],['TSC','TSCKID'])

R.update({
 'VHL':('International VHL surveillance consortium consensus, 2023','https://doi.org/10.1002/cncr.34896'),
 'FABRY':('GeneReviews: Fabry disease','https://www.ncbi.nlm.nih.gov/books/NBK1292/'),
 'FABRYTEST':('Clinical Fabry testing algorithm in males and females, 2020','https://pubmed.ncbi.nlm.nih.gov/32418857/'),
})

add('Neurogenetic syndromes and testing','VHL Surveillance After a CNS Hemangioblastoma',
 'A young adult with confirmed VHL has undergone treatment of a cerebellar hemangioblastoma. Which follow-up principle is most appropriate?',
 'Continue coordinated CNS, retinal, renal, endocrine and other syndrome-directed surveillance',[
 ('Limit follow-up to the operated cerebellar site','Local postoperative review is needed, but VHL predisposes to additional CNS and systemic lesions and requires broader surveillance.'),
 ('Stop screening after complete removal because the inherited risk has been treated','Resection treats the identified lesion rather than the constitutional predisposition; new lesions can arise elsewhere over time.'),
 ('Use annual brain CT as the sole screening test for all VHL manifestations','Brain CT does not adequately survey the retina, kidneys, adrenal system or spinal axis and is not a substitute for a syndrome-specific protocol.')],
 [S('Recognize the Multiorgan Predisposition','**VHL can cause CNS and retinal hemangioblastomas, renal cell carcinoma, pheochromocytoma and pancreatic lesions**, among other manifestations.',
    'A CNS lesion is one component of the syndrome. Its treatment does not remove the risk of another lesion or establish a uniform clinical course for relatives.',
    'Review hearing-related symptoms and other less obvious manifestations through the coordinated service rather than waiting for every lesion to become symptomatic.'),
  S('Use an Age- and Lesion-Informed Protocol','**Surveillance includes brain and spine MRI, retinal assessment, abdominal imaging and biochemical screening for catecholamine-producing tumors**, with intervals tailored to age and existing findings.',
    'The international consensus commonly uses two-yearly CNS and abdominal MRI in relevant age groups, with more frequent targeted review when a lesion or symptom warrants it.',
    'Before procedures, consider whether occult pheochromocytoma requires assessment; an unrecognized catecholamine-secreting lesion can create procedural risk. Provide genetic counseling and targeted family testing after a confirmed pathogenic familial finding. Document who coordinates each surveillance domain so that successful neurosurgical follow-up does not unintentionally leave renal or endocrine disease unmonitored.')],['VHL','ACMG'])

add('Neurogenetic syndromes and testing','Do Not Assign Every Adult Ataxia to Inheritance',
 'An adult with a slowly progressive imbalance syndrome has mild sensory abnormalities and no clear family history. Which initial etiologic strategy is most appropriate?',
 'Define cerebellar, sensory and vestibular contributions and assess acquired causes alongside phenotype-directed genetic testing',[
 ('Assign a recessive inherited ataxia from the absence of affected parents','Recessive disease can occur without family history, but that absence is not proof of inheritance and does not exclude nutritional, toxic, immune or other acquired causes.'),
 ('Order RFC1 testing and end the workup regardless of the result','RFC1 is relevant in selected combined phenotypes, but one test does not resolve every adult ataxia or remove the need to evaluate actionable alternatives.'),
 ('Classify all imbalance as cerebellar degeneration from the gait description','Sensory loss, vestibular failure and mixed disorders can resemble cerebellar gait impairment; examination and targeted testing are needed to localize the components.')],
 [S('Phenotype the Imbalance Before Naming the Disease','**Adult ataxia can arise from cerebellar, sensory or vestibular dysfunction**, often in combination. Examine eye movements, coordination, proprioception, reflexes and vestibular function.',
    'Reconstruct tempo, medicines, alcohol and other exposures, nutrition, autoimmune or cancer clues and relevant systemic findings.',
    'A rapid or asymmetric course and new focal findings change urgency and the differential; do not treat every progressive presentation as a routine inherited degeneration.'),
  S('Use Genetic Testing as One Part of the Workup','**RFC1 disease can involve sensory, vestibular and cerebellar systems**, with chronic cough as an additional clue, but incomplete phenotypes and other causes exist.',
    'Select repeat-expansion or sequence-based tests according to the actual phenotype and validated assay scope. A negative pedigree does not exclude recessive, de novo or variably expressed disease.',
    'Investigate treatable acquired alternatives, including relevant nutritional deficiency and immune or toxic disease, without waiting for a broad genetic panel to return. Rehabilitation, falls prevention and symptom care should begin while etiology is clarified. A positive result still needs causal interpretation, and a negative result should trigger review of both assay limitations and the clinical localization rather than an unsupported permanent label.')],['RFC1','ACMG'])

add('Neurogenetic syndromes and testing','Fabry Testing in a Symptomatic Woman',
 'A woman has neuropathic limb pain, early kidney disease, unexplained left-ventricular thickening and a family history suggestive of Fabry disease. Alpha-galactosidase A activity is within range. Which next approach is most appropriate?',
 'Arrange GLA molecular testing with appropriate variant and phenotype interpretation',[
 ('Exclude Fabry disease because normal enzyme activity has the same sensitivity in both sexes','Enzyme activity can be normal in affected heterozygous women, so a normal result does not exclude disease in this compatible phenotype.'),
 ('Use plasma lyso-Gb3 alone as definitive confirmation or exclusion','The biomarker can help assessment, but values can overlap and cannot replace appropriate molecular evaluation, especially in women.'),
 ('Diagnose Fabry from left-ventricular thickening and start treatment without confirmation','Cardiac thickening has multiple causes; disease-specific treatment requires a supported integrated diagnosis rather than one nonspecific organ finding.')],
 [S('Connect the Neurologic and Systemic Clues','**Fabry disease is an X-linked GLA-related alpha-galactosidase A disorder.** Neuropathic pain, autonomic symptoms and renal, cardiac or cerebrovascular disease can coexist.',
    'Angiokeratomas and corneal findings can support suspicion but are not required in every phenotype. Organ-predominant later-onset presentations also occur.',
    'Marked enzyme deficiency is useful in many affected males, but enzyme screening is less sensitive in women because heterozygous expression can be variable.'),
  S('Confirm Before Disease-Specific Treatment','**Molecular testing is central to diagnosis in a symptomatic woman.** Review sequencing and deletion/duplication coverage and interpret any variant against established evidence.',
    'A GLA VUS is not independently diagnostic. Lyso-Gb3 and selected organ or tissue assessment can contribute to resolving uncertainty through specialist review.',
    'Assess renal, cardiac and neurologic burden and discuss enzyme replacement or an appropriate variant-specific chaperone option when indicated. Not every variant is amenable to the same treatment. Arrange family evaluation and genetic counseling without describing women merely as unaffected carriers; some have clinically important disease requiring longitudinal care.')],['FABRY','FABRYTEST','ACMG'])

R.update({
 'ALD':('International adrenoleukodystrophy diagnosis and management recommendations, 2022','https://doi.org/10.1212/WNL.0000000000201374'),
 'ALDGENE':('GeneReviews: X-linked adrenoleukodystrophy','https://www.ncbi.nlm.nih.gov/books/NBK1315/'),
 'PRNP':('GeneReviews: genetic prion disease','https://www.ncbi.nlm.nih.gov/books/NBK1229/'),
 'PRNPCOUNSEL':('HGSA guidelines for PRNP genetic testing','https://www.cjdsupport.org.au/wp-content/uploads/2021/05/2019-PS03_Guidelines-for-PRNP-genetic-testing.pdf'),
})

add('Neurogenetic syndromes and testing','Spastic Paraparesis With Adrenal Clues',
 'A man has slowly progressive spastic paraparesis and urinary symptoms, with weight loss, hyperpigmentation and orthostatic symptoms. Which etiologic assessment is particularly important?',
 'Evaluate ABCD1-related disease with appropriate biochemical/genetic testing and assess adrenal function',[
 ('Assign hereditary spastic paraplegia and defer endocrine testing','HSP can cause chronic pyramidal disease, but the systemic adrenal clues demand evaluation of a potentially treatable hormonal complication and an alternative genetic mechanism.'),
 ('Use a normal brain MRI to exclude adrenoleukodystrophy','Myeloneuropathy and adrenal disease can occur without the cerebral inflammatory phenotype; a normal brain scan does not exclude ABCD1-related disease.'),
 ('Use the plasma VLCFA concentration to predict the future neurologic phenotype','VLCFA testing helps diagnosis in appropriate patients, but its concentration does not reliably predict whether or when cerebral, spinal or adrenal manifestations will occur.')],
 [S('Recognize Distinct but Related Disease Domains','**ABCD1-related disease can cause myeloneuropathy, cerebral inflammatory disease and adrenal insufficiency.** These manifestations need separate assessment rather than one assumed sequence.',
    'Adult men can present with an adrenomyeloneuropathy pattern. Women can also develop clinically significant myelopathy, while adrenal and cerebral involvement are much less common.',
    'Use appropriate VLCFA or C26:0-lysoPC testing and molecular confirmation. Normal conventional VLCFA can occur in women, making molecular evaluation particularly important in that setting.'),
  S('Do Not Miss Adrenal Risk','**Assess morning cortisol and ACTH with endocrine guidance**, and urgently treat suspected adrenal crisis according to standard emergency care rather than waiting for genetic results.',
    'Confirmed men need appropriate adrenal and cerebral surveillance; early cerebral disease has specialist treatment implications distinct from established chronic myelopathy.',
    'Hormone replacement treats adrenal insufficiency but does not reverse the entire neurologic process. Likewise, cerebral-directed interventions are not a proven universal cure for chronic myeloneuropathy. Explain that genotype, family course and VLCFA level do not reliably predict an individual’s phenotype. Coordinate rehabilitation, bladder care and family evaluation alongside surveillance for actionable complications.')],['ALD','ALDGENE'])

add('Neurogenetic syndromes and testing','PRNP Testing and Variant-Specific Counseling',
 'A patient with a compatible rapidly progressive neurologic syndrome is found to have a confirmed pathogenic PRNP variant. An asymptomatic adult relative asks for predictive testing. Which approach is most appropriate?',
 'Offer formal voluntary counseling about the familial variant, penetrance uncertainty and implications before testing',[
 ('Use the affected relative’s positive result as consent to test the entire family','A molecular diagnosis informs family risk but does not establish each relative’s consent; predictive testing remains an individual decision.'),
 ('Promise that the variant determines an exact onset age and clinical subtype','PRNP-associated disease has variant-dependent and individual variability; a positive result cannot provide a precise onset date or guarantee identical manifestations.'),
 ('Use a normal CSF RT-QuIC result in the unaffected relative as a substitute for predictive genetics','CSF prion assays address a different diagnostic question in symptomatic disease and are not a validated replacement for familial predictive PRNP testing.')],
 [S('Separate Current Disease Diagnosis From Future Risk','**Genetic prion disease includes several phenotypes associated with pathogenic PRNP variants.** A molecular finding must be interpreted with the clinical syndrome and variant evidence.',
    'Family history can be absent through reduced penetrance, unrecognized disease or other family circumstances. Do not assume every apparently sporadic presentation lacks a genetic mechanism.',
    'Diagnostic MRI and CSF studies assess symptomatic disease; they are not interchangeable with a predictive molecular result in a well person.'),
  S('Counsel Without Inventing Precision','**Predictive testing requires informed consent and a structured support pathway.** Discuss psychological effects, privacy, family and reproductive implications and the right to decline.',
    'Penetrance estimates vary by variant and can be revised as evidence improves. Avoid applying one universal risk estimate to every PRNP change or interpreting a VUS as a disease-causing familial marker.',
    'Confirm the affected family member’s variant and the laboratory test before predictive testing. Arrange appropriate results disclosure and follow-up and seek specialist prion advice for clinical care and procedure-specific precautions in affected patients. A genetic result does not justify broad social isolation or imply ordinary casual-contact transmission.')],['PRNP','PRNPCOUNSEL','ACMG'])

add('Neurogenetic syndromes and testing','Cascade Testing Starts With the Confirmed Familial Finding',
 'An affected proband has a pathogenic variant that convincingly explains an autosomal-dominant neurologic syndrome. An adult first-degree relative seeks clarification of risk. Which approach is most appropriate?',
 'Offer counseling and targeted testing for the confirmed familial variant, with gene-specific interpretation and follow-up',[
 ('Repeat an unrestricted panel in each relative before checking the known variant','Broader testing can be needed for a different phenotype, but targeted familial testing usually answers this defined risk question more directly and limits incidental uncertainty.'),
 ('Assume that an unaffected examination excludes inheritance of the familial variant','Age-dependent or reduced penetrance can leave a carrier asymptomatic; examination alone is not a substitute for an informed predictive-testing decision.'),
 ('Assume that a negative familial test excludes every future neurologic disorder','A true negative can substantially reduce the risk from that familial mechanism, but does not exclude unrelated acquired disease, other genetic conditions or a different clinical question.')],
 [S('Define What the Family Test Can Answer','**Targeted cascade testing assesses the established familial variant.** Confirm the proband’s report, pathogenic classification, transcript and inheritance mechanism before ordering.',
    'Explain penetrance and variable expression and distinguish inheriting a variant from predicting exact severity or onset. A molecular recurrence risk is not always a disease-expression probability.',
    'An affected relative with a discordant phenotype may need a separate diagnostic evaluation rather than assuming the family variant explains all symptoms.'),
  S('Connect the Result to Actionable Care','**Positive results should lead to gene- and age-specific surveillance or treatment where supported.** Negative results require interpretation against assay sensitivity and whether the family diagnosis is secure.',
    'For minors, testing depends on childhood benefit and syndrome-specific guidance; do not apply the adult-onset predictive-testing approach indiscriminately to actionable pediatric conditions.',
    'Respect confidentiality and the relative’s choice about testing. Provide a clear follow-up and reproductive-counseling route and explain reclassification if future evidence changes the original conclusion. Cascade testing is not simply copying a risk label through a pedigree; it is a family-specific interpretation linked to validated evidence and meaningful clinical decisions.')],['ACMG','VUS','HD'])

def revise(title,answer=None,others=None,table=None):
    r=next(r for r in rows if r['title']==title)
    if answer is not None:r['answer']=answer
    if others is not None:r['others']=others
    if table is not None:r['table']=table

revise('Maximal Safe Resection Preserves Function',others=[
 ('Plan gross-total removal using radiographic margins as the primary stopping criterion','Radiographic extent is important, but infiltrating tumor near eloquent pathways requires functional limits; a permanent disabling deficit can outweigh incremental removal.'),
 ('Choose stereotactic biopsy without assessing function-guided resection feasibility','Biopsy is appropriate when safe resection is unsuitable, but eloquent proximity alone does not decide this without expert functional and anatomic planning.'),
 ('Treat from the imaging diagnosis and reserve biopsy for inadequate response','Rare patients may be treated without tissue, but feasible integrated pathology normally precedes disease-specific therapy and helps exclude mimics.')])
revise('Observation of an Incidental Meningioma',others=[
 ('Offer elective resection now based on the imaging diagnosis','Resection can be appropriate for symptoms, growth or threatened function, but a small asymptomatic lesion without those features can initially be observed.'),
 ('Offer upfront stereotactic radiosurgery to avoid future surgical risk','Radiosurgery can suit selected anatomy and indications, but immediate treatment is not routinely preferable to surveillance for an incidental low-risk lesion.'),
 ('Follow symptoms without scheduled MRI surveillance','Symptoms are important, but a planned observation strategy generally includes imaging to assess growth rather than waiting for a clinical deficit.')])
revise('Large Vestibular Schwannoma With Brainstem Compression',others=[
 ('Use MRI surveillance with vestibular rehabilitation as the initial strategy','Observation and rehabilitation can suit selected small or stable lesions, but progressive gait impairment with brainstem compression needs decompression assessment.'),
 ('Use single-fraction radiosurgery as the initial treatment','Radiosurgery is useful in selected smaller tumors, but a large compressive lesion may require immediate mechanical decompression and a different risk balance.'),
 ('Use fractionated radiation before considering surgical decompression','Fractionation can be selected when surgery is unsuitable, but does not make prior neurosurgical assessment unnecessary in a fit patient with progressive compression.')])
revise('Tissue Diagnosis Before Steroids in Stable Suspected PCNSL',others=[
 ('Give dexamethasone for several days and biopsy the residual enhancing target','Steroids may be necessary for dangerous mass effect, but this stable patient can undergo prompt biopsy first to reduce the risk of losing diagnostic tissue.'),
 ('Obtain CSF cytology first and defer brain biopsy if it is negative','CSF can contribute when safe, but a negative result does not exclude parenchymal lymphoma and should not postpone a feasible diagnostic biopsy.'),
 ('Use open resection to obtain the largest possible specimen','Selected surgical indications differ, but stereotactic biopsy usually provides the diagnostic approach for a deep suspected PCNSL lesion without a need for major decompression.')])
revise('Symptomatic Brain Metastasis With Mass Effect',answer='Arrange urgent local-treatment assessment and appropriate edema support',others=[
 ('Start the CNS-active systemic agent and schedule MRI reassessment first','A systemic-first approach can suit selected asymptomatic lesions, but symptomatic mass effect generally requires prompt local-treatment assessment.'),
 ('Begin dexamethasone and defer the local decision until steroid taper','Steroids bridge edema-related symptoms but do not replace definitive assessment of a large compressive lesion or justify waiting through a taper.'),
 ('Proceed directly to single-fraction SRS without neurosurgical review','SRS can provide local control in suitable lesions, but size and compression can favor surgery or fractionation and warrant multidisciplinary review.')])
revise('SRS for Limited Small Brain Metastases',others=[
 ('Conventional whole-brain radiotherapy as the initial radiation course','WBRT remains appropriate in selected diffuse or otherwise unsuitable disease, but suitable limited small lesions can receive SRS with less broad cognitive exposure.'),
 ('Resection of the largest lesion followed by radiation to the remaining sites','Surgery helps when tissue or decompression is needed, but neither indication is present here and a suitable SRS strategy avoids an unnecessary operation.'),
 ('Systemic therapy alone with MRI follow-up irrespective of tumor target','Selected CNS-active regimens permit deferral, but this requires tumor-specific evidence and a defined plan rather than the lesion count alone.')])
revise('Cognitive Protection During Whole-Brain Radiotherapy',others=[
 ('Conventional WBRT with memantine, without hippocampal avoidance','Memantine provides cognitive protection, but an eligible patient can gain the additional benefit of hippocampal avoidance when coverage constraints permit it.'),
 ('Hippocampal-avoidance WBRT without memantine','Avoidance helps reduce cognitive burden, but the guideline recommends combining it with memantine in eligible WBRT recipients rather than omitting the medication component.'),
 ('Conventional WBRT with cognitive rehabilitation after treatment','Rehabilitation can help residual deficits, but does not replace available preventive measures when the patient is eligible for them.')])
revise('Dexamethasone for Symptomatic Vasogenic Edema',answer='Start dexamethasone 4–8 mg/day and reassess for taper',others=[
 ('Start dexamethasone 16 mg/day and maintain it through all cancer treatment','Higher doses can suit severe pressure-related symptoms, but mild deficits without impending herniation support lower exposure and active reassessment.'),
 ('Use physiologic hydrocortisone replacement and reassess symptoms','Replacement is appropriate for adrenal insufficiency but is not the recommended anti-edema regimen for this metastatic presentation.'),
 ('Use a brief fixed dexamethasone course and stop without symptom review','A short course can be appropriate, but taper and cessation should account for clinical response, definitive treatment and prior exposure rather than a fixed unreviewed schedule.')])
revise('Integrated Diagnosis of Oligodendroglioma',table=(['Adult diffuse entity','Defining molecular framework','CNS WHO grades'],[
 ['Astrocytoma, IDH-mutant','IDH mutation; astrocytic integrated lineage','2, 3 or 4'],
 ['Oligodendroglioma','IDH mutation plus whole-arm 1p/19q codeletion','2 or 3'],
 ['Glioblastoma, IDH-wildtype','Appropriate adult diffuse astrocytic context, IDH/H3-wildtype and qualifying histologic or molecular features','4']]))
revise('Concomitant and Adjuvant Temozolomide',table=(['Phase','Conventional regimen','Qualification'],[
 ['Radiation','==60 Gy in 30 fractions==','Focal treatment in suitable fit adults'],
 ['Concomitant temozolomide','==75 mg/m² daily== during radiation','Monitor counts and infection risk'],
 ['Adjuvant temozolomide','==150–200 mg/m² daily for five days every 28 days==','Six cycles in the original regimen; individualize treatment']]))
R['INDIGO']=('INDIGO randomized trial, 2023','https://doi.org/10.1056/NEJMoa2304194')
R['MBSAFETY']=('FDA methylene-blue prescribing information: G6PD and serotonergic risks','https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/204630Orig1s023lbl.pdf')
next(r for r in rows if r['title']=='Vorasidenib in Selected IDH-Mutant Grade 2 Glioma')['refs'].append('INDIGO')
next(r for r in rows if r['title']=='Ifosfamide-Associated Encephalopathy')['refs'].append('MBSAFETY')

revise('Papilledema Assessment Must Include Visual Function',others=[
 ('Document acuity and headache severity and use those to determine follow-up urgency','Acuity and pain matter, but visual-field loss can precede central acuity loss; formal fields and expert disc assessment are needed to judge visual threat.'),
 ('Obtain OCT and use nerve-fiber thickness as the main measure of current visual function','OCT helps document swelling and later atrophy, but is not a substitute for visual-field testing or a complete ophthalmic assessment.'),
 ('Arrange LP manometry before ophthalmic characterization of the disc swelling','LP can be appropriate after imaging and safety assessment, but does not replace confirming papilledema and documenting the visual baseline.')])
revise('Venous Imaging Before an Idiopathic Pressure Label',others=[
 ('Intracranial arterial MR angiography to exclude an arterial stenosis syndrome','Arterial imaging can answer selected stroke questions, but does not adequately replace venography when excluding a pressure-producing venous sinus thrombosis.'),
 ('Repeat contrast brain MRI without dedicated venous assessment','Reviewing structural imaging can clarify lesions, but a routine scan may not adequately assess the venous sinuses and does not replace the specified vascular exclusion.'),
 ('Catheter venography with manometry as the routine first venous investigation','Invasive venous studies have selected roles, including procedural planning, but MR or CT venography is the appropriate initial exclusion test in this presentation.')])
revise('Acetazolamide for IIH With Mild Visual Loss',answer='Start 250–500 mg twice daily and titrate to response and tolerability',others=[
 ('Start 2 g twice daily and reduce only after visual remission','Four grams daily was a trial maximum, but starting immediately at that dose can be poorly tolerated and is not necessary for every patient.'),
 ('Use 250 mg intermittently for severe headache days','Acetazolamide is used as sustained pressure-lowering treatment when indicated, not as an as-needed acute headache analgesic.'),
 ('Keep 250 mg twice daily fixed irrespective of visual course','A low starting dose can suit some patients, but titration or a change of strategy must reflect visual response and toxicity rather than an unreviewed fixed prescription.')])
revise('Rapid Visual Deterioration in IIH',answer='Arrange urgent vision-protecting procedural assessment',others=[
 ('Increase acetazolamide and review fields at the next routine clinic','Dose adjustment can help stable disease, but rapid field deterioration requires urgent intervention planning and should not await routine reassessment.'),
 ('Expedite weight-loss treatment as the sole next intervention','Weight loss is disease-modifying, but its time course cannot protect currently deteriorating vision without an acute vision-preserving plan.'),
 ('Use repeated outpatient LPs as the definitive strategy','Specialist drainage can bridge urgent care, but serial outpatient punctures do not replace a definitive intervention assessment for rapidly threatened vision.')])
revise('A Negative Tap Test Does Not End an iNPH Evaluation',others=[
 ('Treat the negative immediate test as sufficient to stop the shunt workup','A negative test can lower confidence, but false negatives and delayed responses occur; the gait phenotype, DESH pattern and assessment quality warrant integrated review.'),
 ('Proceed directly to shunting without assessing competing gait disorders','The pattern can support a shunt decision in selected patients, but comorbidity and procedural risk still require assessment rather than relying on ventriculomegaly alone.'),
 ('Repeat the LP solely to document a higher opening pressure','iNPH assessment is not a search for a high pressure threshold; objective response, clinical pattern and imaging are the relevant questions.')])
revise('Blood Patch and Leak Localization',others=[
 ('Perform myelography first and patch only after a precise defect is seen','Myelography is valuable for targeted treatment of selected persistent leaks, but early non-targeted EBP does not require prior exact localization.'),
 ('Use prolonged conservative care before referring for an epidural procedure','Brief conservative measures can be appropriate, but prolonged delay can extend disability when an early patch is indicated for supported SIH.'),
 ('Proceed directly to surgical exploration using the clinical headache pattern','Surgery can close a localized lesion, but needs appropriate localization and planning; headache phenotype alone does not identify a safe operative target.')])
revise('Choose a Genetic Test From the Clinical Question',others=[
 ('Order a broad panel first and defer detailed pedigree review until results return','A broad panel can help, but phenotype and pedigree inform assay choice, variant interpretation and consent before testing rather than only after an uncertain result.'),
 ('Test an unaffected relative first because this avoids ambiguity from advanced disease','Testing an affected proband is usually more informative for establishing the familial mechanism; unaffected predictive testing requires its own clear question and counseling.'),
 ('Choose exome sequencing first and treat all repeat disorders as covered','Exome can be appropriate for selected phenotypes, but standard analysis does not reliably assess many expansions; assay coverage must match the suspected mechanism.')])
revise('A VUS Is Not a Confirmed Molecular Diagnosis',others=[
 ('Use the VUS to select disease-specific surveillance independent of the phenotype','Surveillance may be justified by clinical or family findings, but an uncertain variant alone should not be treated as the established causal basis for management.'),
 ('Offer predictive testing to relatives using the VUS as the familial risk marker','Family testing can help segregation and reclassification, but is not equivalent to predictive testing of an established pathogenic familial variant.'),
 ('Close the molecular evaluation because the gene on the report fits broadly','A plausible gene is not sufficient; evidence may be needed for reclassification, and other mechanisms or diagnoses can still require assessment.')])
revise('Spontaneous Intracranial Hypotension With Normal Opening Pressure',table=(['Syndrome','Key clinical clue','Pressure/test interpretation','Safety or management distinction'],[
 ['IIH','Papilledema with appropriate pressure syndrome','Elevated properly measured pressure plus normal CSF and exclusions','Assess venous causes and protect vision'],
 ['Acute obstruction','Deterioration with obstructed ventricular pathway','Structural imaging defines dangerous gradients','Urgent specialist diversion; LP can be unsafe'],
 ['iNPH','Gait-predominant chronic syndrome and compatible ventriculomegaly','Tap response can help; a negative test is not absolute exclusion','Assess comorbidity and realistic shunt benefit'],
 ['SIH','Orthostatic headache with compatible imaging or leak evidence','Normal LP pressure does not exclude disease','Avoid LP solely for confirmation; consider early EBP']]))

revise('Heteroplasmy and Tissue Choice',others=[
 ('Repeat the same blood assay and treat a second negative result as exclusion','Repeat testing can resolve a technical problem, but does not remove tissue-dependent heteroplasmy or detection-limit concerns when suspicion remains strong.'),
 ('Use muscle biopsy as the obligatory next step for every negative blood test','Biopsy can help selected cases, but urine or another appropriate less-invasive molecular strategy may answer the question before an invasive procedure.'),
 ('Use the lactate concentration as the principal confirmatory test','Lactate contributes to a metabolic assessment but is nonspecific and cannot independently establish or exclude a mitochondrial genetic mechanism.')])
revise('Mitochondrial Stroke-Like Episodes',others=[
 ('Recurrent embolic arterial ischemia','Embolic stroke remains an urgent alternative, but evolving nonterritorial cortical lesions with hearing, endocrine and maternal-history clues favor a mitochondrial mechanism here.'),
 ('Autoimmune cortical encephalitis','Immune cortical disease can cause seizures and deficits, but the multisystem maternal pattern and nonterritorial evolution make a mitochondrial episode particularly relevant.'),
 ('Cerebral venous thrombosis','Venous disease can produce headache, seizures and nonarterial lesions and requires imaging when suspected, but the inherited multisystem context particularly supports the proposed mitochondrial diagnosis.')])
revise('CADASIL and NOTCH3 Interpretation',others=[
 ('HTRA1-focused testing as the leading single-gene investigation','HTRA1 disorders can cause inherited small-vessel disease, but the dominant migraine/stroke pedigree and anterior temporal pattern particularly support NOTCH3 assessment first.'),
 ('COL4A1/COL4A2-focused testing as the leading investigation','These disorders can cause inherited vascular disease, often with hemorrhagic, structural or systemic clues; the pattern described more strongly supports CADASIL.'),
 ('CSF oligoclonal bands as the principal etiologic confirmation','CSF testing can investigate a competing inflammatory diagnosis, but does not confirm this inherited vascular mechanism or replace appropriately selected molecular testing.')])
revise('A Changing Plexiform Neurofibroma in NF1',others=[
 ('Optimize neuropathic analgesia and reassess at the routine surveillance visit','Analgesia is useful, but rapid growth, persistent nocturnal pain and weakness are warning signs requiring expedited tumor assessment rather than routine follow-up.'),
 ('Arrange a pain-service procedure before reassessing the lesion structurally','Pain intervention can help selected benign disease, but should not precede investigation of concerning growth and neurologic change that may alter the diagnosis.'),
 ('Begin a benign-plexiform-tumor treatment pathway before evaluating transformation','Benign plexiform lesions have their own treatments, but new red flags require assessment for atypical or malignant change before assuming the previous biology remains unchanged.')])
revise('Fabry Testing in a Symptomatic Woman',others=[
 ('Repeat enzyme activity alone and stop evaluation if it remains normal','Repeat activity can clarify an assay concern, but normal enzyme results still do not reliably exclude Fabry in a woman with a compatible phenotype.'),
 ('Use plasma lyso-Gb3 as the sole next diagnostic gate','Lyso-Gb3 can support assessment, but a normal or overlapping value cannot replace appropriate GLA analysis in this setting.'),
 ('Start enzyme replacement and use organ response as the diagnostic test','Disease-specific therapy can be indicated after a supported diagnosis, but a treatment-response trial is not an appropriate substitute for confirmation and variant interpretation.')])
revise('Spastic Paraparesis With Adrenal Clues',others=[
 ('Prioritize an HSP panel and postpone endocrine testing until genetic results return','HSP testing may be relevant later, but possible adrenal insufficiency is actionable now and should be assessed alongside ABCD1-related disease.'),
 ('Prioritize inflammatory myelopathy testing and use a steroid response to determine etiology','Inflammation is a differential, but the chronic myeloneuropathy with adrenal clues requires a specific metabolic-genetic and endocrine evaluation rather than a response-based diagnosis.'),
 ('Obtain brain MRI and investigate ABCD1 only if cerebral white-matter lesions are found','Brain MRI is important for cerebral surveillance, but myeloneuropathy and adrenal disease can exist without cerebral lesions and still justify diagnostic testing.')])
revise('Cascade Testing Starts With the Confirmed Familial Finding',others=[
 ('Order a broad neurologic panel rather than targeted familial testing','A broad panel can suit a distinct unresolved phenotype, but the established familial variant usually permits a more direct and interpretable predictive test.'),
 ('Use periodic neurologic examination as a substitute for offering predictive testing','Clinical surveillance can be chosen by someone declining testing, but an unaffected examination does not determine genotype in an age-dependent disorder.'),
 ('Test only relatives who already have a characteristic symptom','Diagnostic testing is appropriate for symptomatic relatives, but informed adult predictive testing can be offered before symptoms when the familial mechanism is established.')])
revise('Heteroplasmy and Tissue Choice',table=(['Mechanism','Useful testing principle','Important limit'],[
 ['Sequence variant','Validated gene/panel/exome/genome assessment','A negative result depends on coverage and variant classes'],
 ['Repeat expansion','Expansion-specific assay or validated repeat-capable platform','Standard exome may miss noncoding repeats'],
 ['Mosaicism','Appropriate sensitive blood and selected tissue analysis','Blood can be negative despite affected tissue'],
 ['mtDNA heteroplasmy','Variant- and tissue-appropriate testing','Blood level may not represent other tissues'],
 ['Established familial pathogenic variant','Targeted testing with counseling','Penetrance and phenotype may remain variable']]))
R['MEMANTINE']=('RTOG 0614 randomized memantine trial, 2013','https://pmc.ncbi.nlm.nih.gov/articles/PMC3779047/')
mem=next(r for r in rows if r['title']=='Cognitive Protection During Whole-Brain Radiotherapy')
mem['refs'].append('MEMANTINE')
mem['sections'].append(S('Memantine Trial Regimen','**RTOG 0614 began treatment within three days of starting WBRT**, with escalation to ==20 mg/day== and continuation for ==24 weeks==.',
 'Use a gradual titration and adjust for renal function and tolerability under the applicable prescribing protocol. This is cognitive protection, not tumor therapy.'))

if __name__=='__main__':
    coverage=ROOT/'Neurology/13. Neuro-oncology, Intracranial Hypertension & Neurogenetic Disorders.coverage.json'
    c=json.loads(coverage.read_text(encoding='utf-8'))
    assert len(rows)==c['plannedQuestions']==sum(s['questions'] for s in c['sections']),'Incomplete chapter; do not install'
    index=0
    for section in c['sections']:
        for decision in section['decisions']:
            assert rows[index]['topic']==section['section']
            rows[index]['coverageDecision']=decision
            index+=1
    save('Neurology',13,c['chapter'],rows,R,'Original source-based postgraduate synthesis; full Harrison subscription text not accessed; independent clinician review not claimed.')
    c.update(status='authored_validated',authoredQuestions=len(rows))
    c['questionDecisions']=[dict(question=i+1,title=r['title'],decision=r['coverageDecision']) for i,r in enumerate(rows)]
    coverage.write_text(json.dumps(c,ensure_ascii=False,indent=2),encoding='utf-8')
