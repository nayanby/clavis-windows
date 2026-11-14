"""Original, coverage-mapped CNS infection chapter for postgraduate revision."""
import json
from qbank_json_chapters import question as Q,save,ROOT
R={
 'WHO':('WHO meningitis diagnosis, treatment and care guideline, 2025','https://www.who.int/publications/i/item/9789240108042'),
 'WHOREC':('WHO meningitis guideline recommendations, 2025','https://www.ncbi.nlm.nih.gov/books/NBK614844/'),
 'NICE':('NICE NG240: Bacterial meningitis and meningococcal disease, 2024','https://www.nice.org.uk/guidance/ng240/chapter/Recommendations'),
 'INDIA':('NCDC India: National Treatment Guidelines for Antimicrobial Use in Infectious Disease Syndromes, 2025','https://ncdc.mohfw.gov.in/wp-content/uploads/2025/12/National-Treatment-Guidelines-for-AMU-in-ID-syndromes-2025.pdf'),
 'DEVICE':('IDSA healthcare-associated ventriculitis and meningitis guideline, 2017','https://www.idsociety.org/practice-guideline/healthcare-associated-ventriculitis-and-meningitis/'),
 'MENING':('CDC: Meningococcal disease surveillance and contact prophylaxis','https://www.cdc.gov/surv-manual/php/table-of-contents/chapter-8-meningococcal-disease.html'),
 'MENRES':('CDC: Contact prophylaxis in areas with ciprofloxacin resistance, 2024','https://www.cdc.gov/mmwr/volumes/73/wr/mm7305a2.htm'),
 'TB':('ATS/CDC/IDSA treatment of drug-susceptible tuberculosis guideline','https://www.idsociety.org/practice-guideline/treatment-of-drug-susceptible-tb/'),
 'TBM':('Tuberculous meningitis clinical practice guideline, 2025','https://pmc.ncbi.nlm.nih.gov/articles/PMC12419961/'),
 'CRYPTO':('NIH adult/adolescent HIV opportunistic infections: Cryptococcosis','https://clinicalinfo.hiv.gov/en/guidelines/hiv-clinical-guidelines-adult-and-adolescent-opportunistic-infections/cryptococcosis'),
 'CRGLOBAL':('ECMM/ISHAM/ASM global cryptococcosis guideline, 2024','https://pmc.ncbi.nlm.nih.gov/articles/PMC11526416/'),
 'ENC2026':('EAN/ESCMID infectious encephalitis guideline, 2026','https://doi.org/10.1111/ene.70647'),
 'ENCIDSA':('IDSA encephalitis guideline, 2008','https://academic.oup.com/cid/article/47/3/303/313455'),
 'JE':('CDC: Clinical features and diagnosis of Japanese encephalitis','https://www.cdc.gov/japanese-encephalitis/hcp/clinical-diagnosis/'),
 'JETX':('CDC: Treatment and prevention of Japanese encephalitis','https://www.cdc.gov/japanese-encephalitis/hcp/treatment-prevention/index.html'),
 'WN':('CDC: Clinical signs and symptoms of West Nile virus disease','https://www.cdc.gov/west-nile-virus/hcp/clinical-signs/index.html'),
 'ABSC':('ESCMID brain abscess guideline, 2024','https://doi.org/10.1016/j.cmi.2023.08.016'),
 'NCC':('IDSA/ASTMH neurocysticercosis guideline, 2017/2018','https://www.idsociety.org/practice-guideline/neurocysticercosis/'),
 'TOXO':('NIH adult/adolescent HIV opportunistic infections: Toxoplasma encephalitis','https://clinicalinfo.hiv.gov/en/guidelines/hiv-clinical-guidelines-adult-and-adolescent-opportunistic-infections/toxoplasmosis'),
 'PML':('NIH adult/adolescent HIV opportunistic infections: PML/JC virus','https://clinicalinfo.hiv.gov/en/guidelines/hiv-clinical-guidelines-adult-and-adolescent-opportunistic-infections/progressive'),
 'SYPH':('CDC STI guideline: Neurosyphilis, ocular syphilis and otosyphilis','https://www.cdc.gov/std/treatment-guidelines/neurosyphilis.htm'),
 'PAM':('CDC: Diagnosis and testing for Naegleria fowleri','https://www.cdc.gov/naegleria/hcp/diagnosis-testing/'),
}
def S(h,main,*children):return(h,[(main,list(children))])
rows=[]
def add(*a,**kw):rows.append(Q(*a,**kw))

add('Diagnosis and immediate care','CSF Glucose in Acute Meningitis',
 'A febrile adult with meningism has CSF WBC 1800/µL, predominantly neutrophils, protein 220 mg/dL and glucose 24 mg/dL with simultaneous blood glucose 100 mg/dL. Which interpretation is best?',
 'The pattern strongly supports bacterial meningitis, while microbiological confirmation remains necessary',[
 ('The neutrophil count alone proves a specific bacterial species','A neutrophilic response supports a pyogenic process but does not identify an organism; early viral disease and other conditions can also produce neutrophils.'),
 ('The glucose should be considered normal because the blood value is normal','The paired CSF:blood ratio is 0.24, which is low. A normal blood concentration makes the disproportionately low CSF result more, not less, informative.'),
 ('Low CSF glucose rules out tuberculosis and fungal meningitis','TB and fungal infection can also reduce glucose; tempo, host factors and organism-directed tests distinguish these from acute pyogenic disease.')],
 [S('Pattern Recognition','**Marked pleocytosis, high protein and low CSF glucose** support acute bacterial meningitis in this clinical context.',
    'Use a contemporaneous blood glucose to interpret the ratio; a CSF:blood glucose ratio below about 0.4 is concerning, while the value here is ==24/100 = 0.24==. No single threshold identifies all cases.',
    'Early bacterial infection, immunosuppression or prior treatment can produce atypical counts; a normal-looking component does not independently exclude infection.'),
  S('Differential and Confirmation','**Gram stain, culture and appropriate molecular tests** complement cell count, protein and paired glucose.',
    'TB, cryptococcosis, other fungal infections and malignant meningitis can cause hypoglycorrhachia, often with a different tempo or cellular pattern. Early viral meningitis may initially be neutrophilic.',
    'Obtain blood cultures and initiate time-critical treatment when bacterial disease is suspected. Do not delay effective antibiotics while trying to make every CSF variable fit a textbook pattern.')],['WHOREC','NICE'],table=(['Syndrome','Typical cells','Glucose pattern','Important limitation'],[
 ['Pyogenic meningitis','Usually neutrophils','Often low ratio','Atypical early or treated cases occur'],['Viral meningitis','Usually lymphocytes','Usually preserved','Early neutrophils can occur'],
 ['TB/fungal meningitis','Often lymphocytes','Often low','Host response may be sparse'],['Malignant meningitis','Variable; malignant cells may be found','Can be low','Requires cytology/flow and context']]))

add('Diagnosis and immediate care','When Imaging Should Precede Lumbar Puncture',
 'A patient with suspected meningitis has a new hemiparesis and markedly reduced consciousness. Which diagnostic sequence is most appropriate?',
 'Start urgent treatment after blood sampling and obtain brain imaging before considering LP',[
 ('Perform LP immediately because neck stiffness establishes safety','Meningism identifies a syndrome, not the absence of a dangerous pressure gradient; focal signs and substantially impaired consciousness require assessment before puncture.'),
 ('Obtain imaging first and defer all antimicrobial treatment until CSF is available','Imaging may delay LP, but suspected bacterial meningitis remains time critical; blood cultures and treatment should proceed without waiting for the full diagnostic sequence.'),
 ('Treat a normal CT as a guarantee that LP is safe regardless of subsequent examination','CT does not eliminate every clinical contraindication. Reassess consciousness, focal signs, papilledema, physiology and coagulation before proceeding.')],
 [S('Risk-Based Imaging','**New focal neurological signs or substantially impaired consciousness** raise concern for a mass lesion or dangerous intracranial pressure physiology.',
    'Other relevant indications depend on the guideline and context, including papilledema, certain new seizures or severe immunocompromise. Do not image every uncomplicated meningitis patient reflexively if that merely delays safe LP.',
    'Hemodynamic or respiratory instability, significant bleeding risk and local infection are separate reasons to defer or modify the puncture plan.'),
  S('Treatment During Diagnostic Delay','**Blood cultures and empirical therapy** should be obtained or started promptly while imaging and stabilization proceed.',
    'A scan can detect a mass, hydrocephalus or edema but is not a certificate of safety; the clinical state and the suspected mechanism remain important.',
    'Once contraindications are resolved or excluded, obtain CSF if it will inform care. Antibiotics reduce culture yield but the harm of diagnostic delay should not outweigh the benefit of immediate treatment in a high-risk presentation.')],['WHO','NICE'])

add('Diagnosis and immediate care','Antibiotics Before Delayed LP',
 'A patient has fever, meningism and a purpuric rash with hypotension. LP cannot be performed safely during immediate resuscitation. What should happen to antimicrobial treatment?',
 'Give effective IV antibiotics promptly after blood cultures if these can be obtained without significant delay',[
 ('Wait for shock to resolve and CSF culture to be collected before treating','Resuscitation and antibiotics are simultaneous priorities. Waiting for a safe LP can postpone treatment of rapidly fatal invasive bacterial disease.'),
 ('Use a single oral antibiotic dose until LP becomes feasible','Oral bridging is not adequate initial therapy for shock with suspected meningitis; rapid effective parenteral exposure is required.'),
 ('Withhold antibiotics if a rapid blood test is initially nondiagnostic','A negative early blood result does not safely exclude invasive disease in this syndrome; initial treatment is guided by clinical probability while diagnostic studies continue.')],
 [S('Time-Critical Care','**Suspected invasive meningococcal disease or bacterial meningitis with shock** requires immediate sepsis and neurological care.',
    'Secure airway and circulation as needed, collect blood cultures and other urgent specimens when feasible, and administer an appropriate IV regimen. Do not let a delayed LP, CT or transfer become a reason to withhold therapy.',
    'NICE NG240 uses an aim of antibiotics within one hour of hospital arrival for suspected bacterial meningitis; a crashing patient should not wait for the end of that interval.'),
  S('Diagnostic and Public-Health Follow-Through','**Sampling before treatment is desirable only when safe and prompt**; life-saving treatment takes priority.',
    'Blood culture and blood/CSF molecular testing can still be informative. Record what was given and when, because pretreatment changes culture interpretation.',
    'Use appropriate droplet precautions when meningococcal disease is suspected and arrange public-health notification and contact assessment. A purpuric rash is important but its absence does not exclude meningococcal infection.')],['NICE','MENING'])

add('Diagnosis and immediate care','CSF After Antibiotic Pretreatment',
 'A patient received ceftriaxone before transfer. LP later shows neutrophilic pleocytosis, high protein and low paired glucose ratio, but Gram stain and culture are negative. Which interpretation is most appropriate?',
 'Prior treatment can sterilize culture; bacterial meningitis remains plausible',[
 ('Negative culture after antibiotics excludes bacterial meningitis','Culture sensitivity falls after treatment, so a negative result cannot independently override a compatible syndrome and inflammatory CSF pattern.'),
 ('The CSF should be reclassified as viral solely because no organism grows','Viral disease is a differential, but culture negativity after antibiotics does not establish it, particularly with this biochemical and cellular profile.'),
 ('Antibiotic pretreatment makes every molecular test uninterpretable','PCR and related assays can remain useful after treatment, although timing, organism coverage and assay performance still affect interpretation.')],
 [S('Effect of Pretreatment','**Microbiological yield falls after effective antibiotics**, sometimes rapidly for susceptible organisms.',
    'CSF inflammatory and biochemical abnormalities may persist after culture becomes negative. The clinical timeline, dose, agent and interval before puncture should be documented.',
    'A negative culture therefore does not mean treatment was unnecessary, nor does it supply a new organism diagnosis by itself.'),
  S('Recovering Diagnostic Information','**Use blood cultures and appropriate molecular assays**, together with the full CSF and imaging context.',
    'A multiplex panel covers only its listed pathogens; a negative panel is not a universal exclusion of bacterial, TB or fungal infection. Molecular positivity can also persist and does not always demonstrate viable organisms.',
    'Review response, possible source, resistance risks and alternative diagnoses with infection specialists. De-escalation and duration should follow the best integrated evidence, not a rule that every culture-negative case either stops immediately or receives indefinite broad therapy.')],['WHOREC','NICE'])

add('Diagnosis and immediate care','Timing of Adjunctive Dexamethasone',
 'An adult with strongly suspected community-acquired bacterial meningitis is about to receive the first antibiotic dose. Which dexamethasone strategy is best supported when adjunctive steroids are indicated?',
 'Administer before or with the first antibiotic dose, without delaying antibiotics',[
 ('Wait until antibiotics have been given for several days before starting routinely','The intended benefit concerns the inflammatory response around initial bacterial killing; routine late initiation is not equivalent to the studied early strategy.'),
 ('Give dexamethasone alone while waiting for the bacterial species','Steroids are adjunctive treatment, not an antimicrobial substitute; withholding antibiotics while awaiting species identification is unsafe.'),
 ('Continue steroids for the same duration as antibiotics regardless of the identified cause','Continuation depends on microbiology, CSF and guideline context. A standard short adjunctive course is not automatically extended to every organism or diagnosis.')],
 [S('Early Adjunctive Therapy','**Dexamethasone** is most useful when given immediately before or alongside the first effective antibiotic in an appropriate bacterial-meningitis population.',
    'A common adult regimen is ==10 mg IV every 6 hours for 4 days== when continued for a supported indication, particularly pneumococcal disease. The exact recommendation depends on the guideline, setting and identified organism.',
    'Do not delay the antibiotic to obtain or prepare the steroid; promptly reassess if antibiotics have already begun.'),
  S('Continuation and Limits','**Review the organism and CSF findings** once results become available.',
    'Some frameworks continue for pneumococcus or H. influenzae and stop for other identified causes; benefits and applicability vary across populations. TB meningitis uses a different longer steroid regimen and must not inherit this four-day schedule.',
    'Monitor glucose and other adverse effects. Steroid-associated symptomatic improvement is not proof that infection is controlled, and clinical deterioration still requires investigation for seizures, hydrocephalus, infarction or an untreated pathogen.')],['WHO','NICE'])

add('Bacterial meningitis','Empirical Community-Acquired Meningitis Regimen',
 'A previously healthy 28-year-old has acute bacterial meningitis. Local policy identifies a clinically important risk of cephalosporin-nonsusceptible pneumococci. There are no Listeria risk factors. Which empirical regimen best fits?',
 'Ceftriaxone plus vancomycin',[
 ('Ceftriaxone alone','This may be appropriate where resistant pneumococci are unlikely or after susceptibility is known, but the stated local resistance context calls for additional coverage pending results.'),
 ('Ampicillin plus gentamicin','This is relevant to selected Listeria treatment contexts but does not provide the required empirical coverage for resistant pneumococcus in a healthy young adult.'),
 ('Vancomycin plus metronidazole','The combination targets resistant Gram-positive and anaerobic organisms but lacks the usual reliable third-generation cephalosporin coverage of community meningococcal and other bacterial causes.')],
 [S('Spectrum and Dose','**Ceftriaxone plus vancomycin** is a common empirical approach when resistant pneumococcal meningitis is a concern.',
    'Use meningitis-dose ceftriaxone, commonly ==2 g IV every 12 hours== in adults. Vancomycin is weight- and exposure-guided with renal monitoring; a routine low skin-infection dose is not an adequate assumption.',
    'Cefotaxime is a third-generation alternative. The need for vancomycin depends on epidemiology and policy rather than being identical in every country.'),
  S('Refining Treatment','**Add Listeria-active therapy when host risk requires it**, rather than assuming that a cephalosporin covers that organism.',
    'Obtain cultures and appropriate molecular studies, then narrow to the pathogen and susceptibility profile. Allergy, renal impairment, travel and prior antimicrobial exposure can modify the initial plan.',
    'Treat promptly and give indicated early adjunctive steroids. A broad empirical regimen is a bridge to a specific diagnosis, not a reason to ignore resistance results, toxicity or source-related complications.')],['WHO','INDIA'])

add('Bacterial meningitis','Listeria Coverage in an At-Risk Adult',
 'A 73-year-old receiving chronic immunosuppression has suspected community-acquired bacterial meningitis. Ceftriaxone and vancomycin have been started under local resistance policy. Which additional drug is most appropriate?',
 'Ampicillin',[
 ('Metronidazole','Metronidazole adds anaerobic coverage useful in selected abscess or contiguous-source infections, but it does not provide the needed Listeria coverage.'),
 ('Cefepime','An antipseudomonal cephalosporin can suit healthcare-associated disease, but changing cephalosporins does not reliably cover Listeria.'),
 ('Azithromycin','A macrolide has other respiratory and selected prophylactic roles but is not the standard Listeria-active addition for acute adult meningitis.')],
 [S('Host Risk and Intrinsic Coverage Gap','**Older age and impaired cell-mediated immunity** increase the relevance of Listeria monocytogenes.',
    'Third-generation cephalosporins do not provide dependable Listeria activity. Add ampicillin, commonly ==2 g IV every 4 hours== in an adult with normal renal function, with adjustment when required.',
    'Other important risk contexts include pregnancy and selected immunocompromised states. Age thresholds vary between frameworks, so the stem uses an unequivocally high-risk host.'),
  S('Syndrome and Alternatives','**Listeria can cause meningitis or rhombencephalitis**, sometimes with brainstem or cranial-nerve findings.',
    'A compatible focal brainstem syndrome may warrant MRI and assessment for associated lesions. Blood cultures can be informative even when CSF microscopy is unrevealing.',
    'For a serious immediate beta-lactam allergy, trimethoprim–sulfamethoxazole is an important alternative under specialist guidance. Definitive selection and duration depend on microbiology, complications and host status, and should not simply copy the course for meningococcal disease.')],['WHO','INDIA'])

add('Bacterial meningitis','Definitive Therapy for Listeria Meningitis',
 'CSF culture identifies susceptible Listeria monocytogenes. Which listed drug is the preferred definitive treatment backbone?',
 'High-dose intravenous ampicillin',[
 ('Ceftriaxone','Excellent CSF use against many community bacteria does not overcome Listeria’s intrinsic cephalosporin resistance; continuing it as definitive monotherapy misses the pathogen.'),
 ('Cefepime','Broader Gram-negative activity does not make this cephalosporin a dependable Listeria regimen; antipseudomonal spectrum is not the relevant requirement.'),
 ('Metronidazole','Its anaerobic activity is useful for many pyogenic abscess regimens but does not make it an appropriate Listeria meningitis backbone.')],
 [S('Pathogen-Directed Treatment','**Ampicillin** is a standard definitive agent for susceptible Listeria CNS infection.',
    'A common adult regimen is ==2 g IV every 4 hours== with renal adjustment. Treatment is generally prolonged, often at least 21 days for uncomplicated meningitis and longer for abscess, rhombencephalitis or other complicated infection.',
    'The course is guided by clinical response, host immunity and complications rather than by a single universal stop date.'),
  S('Adjuncts and Alternatives','**Gentamicin is not an automatic requirement for every patient**; potential synergy must be weighed against renal toxicity and the limited certainty of outcome evidence.',
    'Trimethoprim–sulfamethoxazole is an important alternative when ampicillin cannot be used, with CNS-appropriate dosing and blood-count, renal and potassium monitoring.',
    'Review the empirical regimen once the diagnosis is established. Continuing multiple unnecessary antibiotics adds toxicity without repairing an incorrect treatment backbone; inspect for hydrocephalus, focal lesions and other reasons for a slow response.')],['INDIA','NICE'],style='direct')

add('Bacterial meningitis','Pneumococcal Susceptibility-Guided Treatment',
 'A patient is improving on ceftriaxone and vancomycin. CSF grows pneumococcus resistant to penicillin by meningitis breakpoints but fully susceptible to ceftriaxone. Which definitive approach is appropriate?',
 'Continue meningitis-dose ceftriaxone and discontinue unnecessary vancomycin',[
 ('Change to penicillin G solely because the organism is pneumococcus','Species identification is not equivalent to susceptibility. Meningitis-specific penicillin resistance prevents this routine narrowing.'),
 ('Use vancomycin alone because penicillin is resistant','Penicillin resistance does not imply ceftriaxone resistance. Vancomycin monotherapy is not the preferred unnecessary substitute for a proven active beta-lactam with established CNS use.'),
 ('Escalate to meropenem without a new resistance or clinical indication','Meropenem has selected CNS indications, but broadening an improving susceptible infection is not required merely because a different beta-lactam is resistant.')],
 [S('Use CNS Breakpoints','**Meningitis susceptibility criteria** matter because achievable CSF exposure differs from other infection sites.',
    'A pneumococcal isolate can be penicillin resistant yet ceftriaxone susceptible. Review the laboratory’s meningitis interpretation rather than using a nonmeningeal breakpoint or a generic susceptible label.',
    'For a susceptible isolate, adult ceftriaxone ==2 g IV every 12 hours== is a standard regimen; adjust other aspects of care to the organism and response.'),
  S('Duration and Complications','**Uncomplicated pneumococcal meningitis** commonly requires approximately 10–14 days, with the stated guideline and clinical setting governing the final course.',
    'Persistent fever, neurological decline or poor sterilization should prompt reassessment for resistance, abscess, empyema, hydrocephalus, infarction or another source, not automatic extension without explanation.',
    'Hearing assessment and neurological follow-up are important after recovery. Continue or stop dexamethasone according to the relevant early-adjunctive framework rather than continuing steroids for the entire antibiotic course.')],['NICE','INDIA'])

add('Bacterial meningitis','Meningococcal Contact Prophylaxis in Pregnancy',
 'A pregnant adult household contact had direct exposure to a confirmed meningococcal case. She has no cephalosporin allergy. Which prophylaxis is generally preferred among these options?',
 'Ceftriaxone 250 mg intramuscularly once',[
 ('Rifampin 600 mg orally every 12 hours for 2 days','This is an accepted adult prophylaxis regimen in appropriate nonpregnant contacts, but CDC tables do not recommend it in pregnancy; ceftriaxone is preferred here.'),
 ('Ciprofloxacin 500 mg orally once','This can be used for suitable nonpregnant contacts where susceptibility policy allows, but pregnancy and increasing local resistance can make it less appropriate than ceftriaxone.'),
 ('Amoxicillin–clavulanate orally for 5 days','This is not a standard meningococcal carriage-eradication regimen for exposed household contacts, despite usefulness in other respiratory or contiguous infections.')],
 [S('Who Needs Prophylaxis','**Close contacts** include household members and people directly exposed to relevant oral or respiratory secretions.',
    'Give prophylaxis promptly after public-health assessment; vaccination does not replace immediate exposure management. Casual proximity without secretion exposure does not automatically qualify.',
    'For an adult pregnant contact, ==ceftriaxone 250 mg IM once== is a standard preferred option when suitable.'),
  S('Resistance and Drug Selection','**Local ciprofloxacin resistance** changes prophylaxis policy.',
    'Rifampin, ceftriaxone and, where appropriate, ciprofloxacin are established regimens; azithromycin has a role in selected resistance-based public-health strategies. Rifampin can induce drug metabolism and reduce hormonal contraceptive effectiveness.',
    'Chemoprophylaxis treats carriage risk, not an established symptomatic infection. A contact who develops fever, rash or meningitic symptoms requires urgent clinical assessment rather than reassurance from a prophylactic dose.')],['MENING','MENRES'])

add('Bacterial meningitis','Healthcare-Associated Ventriculitis',
 'Fever and neurological deterioration develop after neurosurgery with an external ventricular drain. Healthcare-associated ventriculitis is suspected and local Gram-negative susceptibility permits cefepime. Which empirical regimen best fits?',
 'Vancomycin plus cefepime',[
 ('Vancomycin plus ceftriaxone','This can resemble community meningitis coverage, but ceftriaxone lacks the antipseudomonal activity needed for the healthcare-associated Gram-negative risk described.'),
 ('Ampicillin plus ceftriaxone','This is relevant in selected other bacterial contexts but does not provide the standard resistant staphylococcal and antipseudomonal coverage required here.'),
 ('Metronidazole plus ceftriaxone','This is a common community brain-abscess combination, not adequate empirical coverage for drain-associated resistant staphylococci and Pseudomonas.')],
 [S('Empirical Spectrum','**IDSA healthcare-associated guidance** recommends vancomycin plus an antipseudomonal beta-lactam such as cefepime, ceftazidime or meropenem.',
    'Choice follows the local antibiogram, previous colonization and allergy or organ-function considerations. A common normal-renal adult cefepime regimen is ==2 g IV every 8 hours== for severe CNS infection, with renal adjustment.',
    'Use appropriate vancomycin exposure monitoring. Cefepime accumulation can itself cause encephalopathy or seizures and should be considered during treatment.'),
  S('Microbiology and Hardware','**CSF culture and device assessment** are central; postoperative cell counts alone may be misleading.',
    'Distinguish contamination from a true device-related infection using organism, repeated findings and clinical context. Some organisms require prolonged culture incubation.',
    'Confirmed infected hardware commonly needs removal or exchange coordinated with neurosurgery, with tailored antimicrobial treatment. Intraventricular antibiotics are selected specialist therapy when systemic treatment alone is inadequate, not routine for every positive sample.')],['DEVICE'])

add('Bacterial meningitis','Recurrent Pneumococcal Meningitis and CSF Leakage',
 'A patient has recurrent pneumococcal meningitis after remote skull-base trauma and intermittent unilateral clear rhinorrhea. Which test of the nasal fluid best supports a CSF leak?',
 'Beta-2 transferrin',[
 ('A positive glucose reagent strip','Glucose strips are insufficiently reliable because nasal secretions, blood contamination and infection alter results; they should not establish or exclude a CSF leak.'),
 ('A high total protein concentration alone','Protein can rise in many secretions and inflammatory conditions and is not the specific marker needed to support CSF origin.'),
 ('Routine bacterial culture of the nasal fluid','Colonization may be identified but does not establish that the fluid is CSF or localize a skull-base communication.')],
 [S('Anatomical Predisposition','**A skull-base communication** permits nasopharyngeal organisms to reach the subarachnoid space and can cause recurrent pneumococcal meningitis.',
    'Beta-2 transferrin is a useful specific fluid marker in the appropriate setting; beta-trace protein is another test used by some services. Intermittent leakage can make sampling difficult.',
    'A negative sample obtained when no leak is active does not definitively rule out the suspected anatomical defect.'),
  S('Localizing and Preventing Recurrence','**High-resolution skull-base imaging** and specialist assessment are used to localize the defect and plan repair.',
    'CT and tailored MRI or selected cisternographic techniques answer different anatomical questions; investigation should be coordinated rather than repeating low-specificity bedside tests.',
    'Treat the acute infection promptly and review indicated pneumococcal vaccination and other preventive measures. Vaccination does not replace repair of a demonstrated defect, and indefinite empirical antibiotics are not a substitute for evaluating the anatomical source.')],['WHO','INDIA'])

add('Bacterial meningitis','Terminal Complement Deficiency',
 'A young adult has had three separate episodes of invasive meningococcal disease. Which immune defect deserves particular investigation?',
 'Terminal complement pathway deficiency',[
 ('Selective IgA deficiency alone as the characteristic association','IgA deficiency has important mucosal and autoimmune associations, but recurrent invasive meningococcal disease is particularly linked to terminal complement dysfunction.'),
 ('Chronic granulomatous disease as the typical meningococcal predisposition','CGD predisposes to selected catalase-positive bacterial and fungal infections through phagocyte dysfunction, rather than the characteristic recurrent meningococcal pattern.'),
 ('Isolated T-cell depletion as the most specific explanation','T-cell defects predispose to many opportunistic infections; recurrent Neisseria disease specifically warrants complement-pathway assessment even if other immune testing is considered.')],
 [S('Mechanism','**C5–C9 membrane-attack-complex defects** impair terminal complement-mediated killing and predispose to recurrent Neisseria infection.',
    'Properdin or other alternative-pathway abnormalities can also be relevant. Acquired terminal complement inhibition, such as C5-targeting therapy, creates a related risk.',
    'The association is stronger than a nonspecific statement that every recurrent infection implies the same immune defect.'),
  S('Assessment and Prevention','**Functional complement testing**, including CH50 and alternative-pathway assessment, guides further component studies.',
    'Interpret results with the clinical state and sample handling because consumption or technical problems can lower activity. Review family history and medications, and seek immunology input.',
    'Meningococcal vaccination and an individualized prevention plan are important, but vaccination does not eliminate all risk in complement deficiency or inhibition. Provide urgent fever/sepsis advice and consider specialist-guided antimicrobial prophylaxis according to the precise condition and local policy.')],['MENING'],style='direct')

add('CNS tuberculosis','A Negative CSF Molecular Test',
 'A patient has subacute meningitis, low CSF glucose, lymphocytic pleocytosis and imaging compatible with basal meningitis. Initial CSF Xpert MTB/RIF Ultra is negative. Which interpretation is most appropriate?',
 'A negative result cannot exclude TB meningitis when clinical probability remains high',[
 ('The result rules out CNS tuberculosis regardless of sample quality','CSF disease is often paucibacillary and sensitivity is incomplete; volume, processing and disease burden affect yield.'),
 ('The negative result proves that a fungal pathogen is responsible','Fungal meningitis remains a differential, but a negative TB assay does not identify another organism or remove the need for fungal testing.'),
 ('A normal chest radiograph would make TB meningitis impossible','CNS tuberculosis can occur without obvious radiographic pulmonary disease; absence of a chest finding does not overrule a compatible CNS syndrome.')],
 [S('Microbiological Strategy','**CSF molecular testing** can rapidly identify tuberculosis and rifampicin-resistance markers, but is not a perfect rule-out test.',
    'Send an adequate safely obtained volume for appropriate NAAT, mycobacterial culture and other relevant studies, using laboratory processing protocols. Culture is slow but can add diagnostic and susceptibility information.',
    'AFB smear is insensitive. CSF ADA can support selected contexts but lacks sufficient specificity to independently diagnose TB meningitis.'),
  S('Clinical Decision','**Integrate tempo, CSF, imaging, exposure and systemic evidence** while assessing cryptococcal, other fungal, malignant and inflammatory alternatives.',
    'A sufficiently convincing high-risk presentation may require treatment before microbiological confirmation. Diagnostic uncertainty should be documented and reviewed rather than disguised as a definitive positive test.',
    'Repeat or additional sampling and testing from extracranial sites can improve yield when safe and appropriate. Do not delay treatment solely to obtain a perfect sample in a deteriorating patient.')],['TBM','TB'])

add('CNS tuberculosis','Basal Meningitis and Perforator Infarction',
 'An adult with a three-week febrile meningitic illness has basal meningeal enhancement, communicating hydrocephalus and basal ganglia infarcts. Which mechanism best explains the infarcts in suspected TB meningitis?',
 'Inflammatory involvement of perforating arteries traversing basal exudates',[
 ('A primary cardioembolic mechanism established by the infarct location','Cardioembolism is possible in other contexts, but does not best integrate the basal exudates, subacute meningitis and characteristic perforator-territory injury here.'),
 ('Demyelination caused by low CSF glucose','Hypoglycorrhachia supports the meningitic differential but is not itself the mechanism producing focal perforator-territory ischemic infarcts.'),
 ('Pure venous congestion as the required explanation for all basal ganglia lesions','Venous thrombosis can affect deep structures, but requires venous evidence; basal meningeal inflammation commonly injures arterial perforators in TB meningitis.')],
 [S('Vascular Pathophysiology','**Basal inflammatory exudates** can involve adjacent arterial walls and narrow or occlude perforators.',
    'Basal ganglia and internal-capsular infarcts can produce focal deficits, while large-vessel disease may also occur. Infarction can develop despite treatment because organism control and inflammatory injury evolve on different timescales.',
    'Basal enhancement, hydrocephalus and infarcts form a characteristic combination but are not uniquely diagnostic of tuberculosis.'),
  S('Imaging and Monitoring','**MRI with diffusion imaging and appropriate vascular assessment** helps identify ischemia and associated tuberculomas or other complications.',
    'Hydrocephalus results from impaired CSF circulation or absorption and can itself worsen consciousness. Review serial examination rather than attributing every decline to a new infarct.',
    'Treat suspected infection and indicated inflammation while addressing pressure and systemic complications. Antiplatelet adjuncts have been studied, but should not be presented as an established universal replacement for antimicrobials, steroids or necessary CSF diversion.')],['TBM'])

add('CNS tuberculosis','Duration of Adult Drug-Susceptible TB Meningitis Therapy',
 'Under the ATS/CDC/IDSA framework, what is a standard treatment-duration approach for adult TB meningitis caused by susceptible organisms?',
 'Two months of HRZE followed by an additional 7–10 months of HR',[
 ('Two months of HRZE followed by four months of HR','This is the familiar six-month approach for many pulmonary cases, but it is not the usual adult CNS-duration framework in the question.'),
 ('Four months of a rifapentine–moxifloxacin pulmonary regimen without a CNS-specific assessment','Short pulmonary regimens should not be extrapolated automatically to CNS tuberculosis; site-specific evidence and eligibility matter.'),
 ('HRZE for one month followed by H alone for five months','This removes combination protection and adequate duration without support; a single continuation drug promotes treatment failure and resistance.')],
 [S('Regimen Framework','**Isoniazid, rifampicin, pyrazinamide and ethambutol** are used initially, with subsequent isoniazid–rifampicin continuation for a total often ==9–12 months== in adults.',
    'National programmes may choose a defined 12-month approach, while the optimal duration is not established by robust comparative trials. State the framework rather than treating pulmonary duration as universal.',
    'Standard adult daily doses are typically isoniazid about 5 mg/kg, maximum 300 mg, and rifampicin about 10 mg/kg, commonly maximum 600 mg, with weight-band and programme-specific prescribing.'),
  S('Safety and Special Situations','**Susceptibility, absorption and drug interactions** must be reviewed, especially with HIV therapy or unexpected deterioration.',
    'Give pyridoxine when indicated and monitor hepatic toxicity, ethambutol-related visual risk and other regimen adverse effects. Dose adjustment or alternative agents may be required for organ dysfunction.',
    'Pediatric shortened/intensified options and investigational adult high-dose strategies are not interchangeable with this adult standard. Resistant disease needs specialist-designed therapy rather than a simple extension of an ineffective regimen.')],['TB','TBM'],style='direct')

add('CNS tuberculosis','Adjunctive Steroids in TB Meningitis',
 'An HIV-negative adult begins treatment for probable TB meningitis. Which adjunctive strategy matches established guideline practice while recognizing evolving trial evidence?',
 'Add a severity-appropriate corticosteroid course tapered over about 6–8 weeks',[
 ('Use the four-day bacterial-meningitis dexamethasone schedule as an equivalent TB regimen','The inflammatory illness and evidence base differ; a short pyogenic-meningitis adjunctive course is not the established TB taper.'),
 ('Give corticosteroids alone until mycobacterial culture becomes positive','Steroids do not eradicate tuberculosis and may worsen untreated infection; they are adjuncts to appropriate antituberculosis therapy.'),
 ('Continue the initial high steroid dose indefinitely in every patient','Extended exposure adds substantial toxicity. A planned taper and clinical reassessment are integral, with selected inflammatory complications managed individually.')],
 [S('Guideline Position','**Adjunctive dexamethasone or prednisolone** is recommended in established TB meningitis guidance, generally tapered over ==6–8 weeks==.',
    'Initial dexamethasone schedules vary by severity; published adult protocols use weight-based early doses around 0.3–0.4 mg/kg/day before staged reduction. Use a defined protocol rather than improvising a prolonged fixed dose.',
    'The historical evidence supports a mortality benefit in relevant populations; the magnitude and modifiers of benefit remain active research questions.'),
  S('Evidence Qualifications and Monitoring','**HIV status and host biology** affect interpretation of newer trials.',
    'A major HIV-associated trial did not demonstrate a clear overall survival benefit, and genotype-stratified HIV-negative research has added uncertainty about subgroup effects. These findings do not justify routine genotype-based prescribing without an adopted clinical pathway.',
    'Monitor glucose, infection, gastrointestinal and psychiatric effects and reassess clinical deterioration. Steroids should not conceal hydrocephalus, resistant infection or another diagnosis, and successful tapering does not prove microbiological cure.')],['TB','TBM'])

add('CNS tuberculosis','Paradoxical Deterioration During TB Treatment',
 'After initial improvement on appropriate TB meningitis therapy, a patient develops new enhancing tuberculoma-like lesions at week 6. Adherence is verified and initial susceptibility is reassuring. Which explanation should be considered while alternatives are investigated?',
 'A paradoxical inflammatory reaction',[
 ('Drug resistance proven solely by new enhancement','Resistance must be reassessed where indicated, but radiological worsening after an initial response is not itself proof that the organisms are resistant.'),
 ('Isoniazid neurotoxicity as the best explanation for new enhancing mass lesions','Isoniazid toxicity can cause neuropathy or other neurological problems, but it does not usually generate this evolving focal inflammatory lesion pattern.'),
 ('Microbiological cure proven by the inflammatory appearance','A paradoxical hypothesis is not proof of sterilization. Persistent infection, resistance, inadequate exposure and alternative pathogens still require consideration.')],
 [S('Inflammatory Worsening','**A paradoxical reaction** is clinical or radiological worsening attributable to host inflammation after treatment has begun, often following initial improvement.',
    'New or enlarged tuberculomas, worsening meningeal inflammation or hydrocephalus may occur. In HIV, recent ART adds an immune-reconstitution context, but paradoxical reactions also occur without HIV.',
    'The timing and pattern support the hypothesis, but no single scan establishes it with certainty.'),
  S('Exclude Treatable Failure','**Recheck adherence, dose, absorption, susceptibility and the original diagnosis** before assuming a benign treatment response.',
    'Assess urgent complications such as mass effect, seizures, infarction or hydrocephalus. Obtain additional microbiology or tissue when uncertainty and the clinical course justify it.',
    'If a paradoxical process is most likely, effective TB therapy is generally continued while clinically important inflammation is treated under specialist guidance. Neurosurgical intervention may be needed for pressure or a problematic mass; simply stopping all drugs or changing to a resistant regimen from the scan alone is inappropriate.')],['TBM'])

add('CNS tuberculosis','Symptomatic Hydrocephalus in TB Meningitis',
 'A treated TB meningitis patient becomes progressively drowsy. CT shows increasing ventricular size and transependymal flow. Which action is most appropriate?',
 'Urgent neurosurgical assessment for CSF diversion while continuing infection and critical care',[
 ('Increase antituberculosis doses alone and wait for ventricular size to normalize','Effective antimicrobial therapy is essential but may not reverse a dangerous CSF-pressure complication quickly enough; declining consciousness requires direct pressure assessment.'),
 ('Repeat lumbar punctures without assessing obstruction or pressure gradients','Selected CSF drainage approaches have specific indications, but an unassessed obstructive pattern or pressure gradient can make lumbar puncture hazardous.'),
 ('Assume new ventricular enlargement is an expected harmless radiological change','Progressive drowsiness plus ventricular enlargement indicates a potentially life-threatening complication, not an incidental imaging finding.')],
 [S('Mechanism and Recognition','**Hydrocephalus** may reflect basal-exudate impairment of CSF absorption or obstruction of flow.',
    'Reduced consciousness, worsening headache, vomiting or new ocular findings can signal pressure-related deterioration. Also assess seizures, sodium and glucose, infarction and drug effects because several causes can coexist.',
    'Imaging helps define ventricular change, edema and the anatomical pattern but does not replace repeated clinical assessment.'),
  S('Treatment Sequencing','**CSF diversion** may require an external drain, shunt or selected endoscopic procedure according to anatomy and clinical status.',
    'The neurosurgical and infection teams coordinate timing, microbiology and ongoing therapy. Airway support, circulation and temporizing pressure measures are used when needed while definitive care is arranged.',
    'Continue effective antimicrobials and indicated anti-inflammatory treatment; drainage does not eradicate infection. Conversely, a correct antimicrobial regimen is not sufficient justification for delaying urgent intervention in a deteriorating hydrocephalic patient.')],['TBM'])

add('Fungal CNS infection','Diagnosing Cryptococcal Meningitis',
 'An adult with advanced HIV has subacute headache and raised CSF pressure with few CSF leukocytes. Which test is particularly useful for rapidly identifying cryptococcal meningitis?',
 'CSF cryptococcal antigen',[
 ('India-ink microscopy as a sufficiently sensitive rule-out test','India ink can demonstrate encapsulated yeast but is less sensitive, particularly at low burden; a negative result does not safely exclude cryptococcosis.'),
 ('Serum beta-D-glucan as the preferred organism-specific CNS test','Beta-D-glucan is not a substitute for cryptococcal antigen testing and does not identify the organism or establish meningeal involvement.'),
 ('A normal CSF leukocyte count as evidence against infection','Advanced immunosuppression can blunt inflammation; a sparse CSF cellular response does not exclude high-burden cryptococcal disease.')],
 [S('Rapid Identification','**Cryptococcal antigen testing** on CSF is highly useful in a compatible meningeal syndrome.',
    'Obtain opening pressure and fungal culture when LP is safe. Culture documents viable organisms and later helps distinguish relapse from inflammatory deterioration; antigen and culture answer related but different questions.',
    'Serum antigen supports disseminated infection assessment, but a positive result does not remove the need to evaluate CNS involvement when indicated.'),
  S('Host Response and Pitfalls','**Advanced HIV can produce little CSF inflammation**, so a low cell count is not reassuring by itself.',
    'The diagnostic differential includes TB and other subacute meningitides. Consider assay limitations when a strongly suspected high-burden case tests negative, including laboratory assessment for a high-antigen hook effect with dilution when appropriate.',
    'Assess visual symptoms, neurological status and pressure complications promptly. A rapid positive antigen should lead to appropriate induction and pressure management, not fluconazole monotherapy by default in severe CNS disease.')],['CRYPTO','CRGLOBAL'])

add('Fungal CNS infection','Cryptococcal Induction in a Resource-Available Setting',
 'A patient with HIV-associated cryptococcal meningitis is treated in a setting able to monitor daily liposomal amphotericin and provide flucytosine. Which induction regimen is preferred by the NIH panel?',
 'Liposomal amphotericin B plus flucytosine for about 2 weeks',[
 ('Fluconazole alone as equivalent preferred induction','Fluconazole alone is less fungicidal and is not the preferred induction when amphotericin and flucytosine can be delivered safely.'),
 ('Liposomal amphotericin B alone as equivalent combination treatment','Amphotericin monotherapy may be necessary in selected circumstances, but omitting flucytosine does not reproduce the preferred combination.'),
 ('Fluconazole plus flucytosine as the preferred regimen despite full amphotericin availability','This can be an alternative when amphotericin cannot be used, but it is not the resource-available preferred induction described.')],
 [S('Preferred Daily Regimen','**Liposomal amphotericin B 3–4 mg/kg IV daily** plus **flucytosine 25 mg/kg orally every 6 hours** is the NIH preferred resource-available induction approach.',
    'A typical initial course is ==2 weeks==, with clinical stability and CSF culture response informing transition or extension. The single-dose resource-limited pathway is a distinct validated regimen, not an arbitrary shortened version.',
    'Monitor renal function, potassium, magnesium and blood counts; flucytosine accumulation increases marrow and other toxicity risk, especially with renal impairment.'),
  S('Consolidation and Maintenance','**Fluconazole follows induction**, commonly 800 mg/day during consolidation in the NIH pathway, followed by lower-dose maintenance when appropriate.',
    'Consolidation is generally at least eight weeks, with subsequent maintenance commonly 200 mg/day for at least a year and until immune-reconstitution and suppression criteria are met.',
    'Adjust drugs for organ function and interactions. Antifungal efficacy does not substitute for therapeutic CSF drainage when pressure is raised, and ART timing requires a separate deliberate plan.')],['CRYPTO'])

add('Fungal CNS infection','Single-Dose Liposomal Amphotericin Pathway',
 'Which regimen reproduces the WHO-supported single-dose liposomal amphotericin induction pathway studied for HIV-associated cryptococcal meningitis?',
 'Liposomal amphotericin B 10 mg/kg once plus 14 days of flucytosine and high-dose fluconazole',[
 ('Liposomal amphotericin B 3 mg/kg once plus the same oral partners','A single 3-mg/kg dose is not the studied 10-mg/kg induction strategy; a daily low-dose regimen and a single high-dose regimen cannot be substituted dose for dose.'),
 ('Liposomal amphotericin B 10 mg/kg once with only 7 days of both oral partners','This truncates the oral treatment that accompanied the validated single-dose regimen; the shorter infusion schedule does not mean all induction drugs stop early.'),
 ('Liposomal amphotericin B 10 mg/kg once with fluconazole alone for 14 days','Omitting flucytosine changes the evidence-based combination and cannot be assumed to preserve the trial’s benefit and noninferiority result.')],
 [S('Validated Combination','**AMBITION** tested liposomal amphotericin B ==10 mg/kg IV on day 1== with flucytosine ==100 mg/kg/day in four doses== and fluconazole ==1200 mg/day== for 14 days.',
    'The strategy reduced infusion burden and has a WHO-supported role, particularly where daily amphotericin delivery is difficult. It is a complete combination protocol, not a single infusion followed by no therapy.',
    'Use the appropriate patient population and drug formulations; liposomal and deoxycholate amphotericin doses are not interchangeable.'),
  S('Monitoring Still Matters','**Fewer infusions do not eliminate toxicity or pressure complications**.',
    'Check renal function, electrolytes, blood counts and oral-drug adherence, and adjust flucytosine or fluconazole for renal impairment according to protocol. Manage opening pressure actively.',
    'Follow with consolidation and maintenance therapy and a planned ART start. Do not transfer this HIV-associated regimen unchanged to every non-HIV host, cryptococcoma or complicated fungal CNS infection without reviewing the relevant guidance.')],['CRYPTO','CRGLOBAL'])

add('Fungal CNS infection','Raised Pressure in Cryptococcal Meningitis',
 'A patient with cryptococcal meningitis has severe headache, blurred vision and opening pressure 38 cm CSF. Imaging and assessment do not reveal a contraindication to lumbar drainage. Which intervention directly addresses the immediate pressure problem?',
 'Therapeutic CSF drainage with repeat pressure-guided LPs as needed',[
 ('Acetazolamide as the routine replacement for CSF drainage','Unlike selected idiopathic intracranial hypertension care, acetazolamide is not established treatment for cryptococcal pressure elevation and can cause harm.'),
 ('Routine mannitol instead of evaluating CSF drainage','Osmotic therapy is not a dependable substitute for the recommended mechanical pressure strategy in this infection-related physiology.'),
 ('High-dose corticosteroids solely to normalize opening pressure','Routine steroids do not replace drainage and have not shown benefit for uncomplicated cryptococcal pressure control; selected severe IRIS is a different indication.')],
 [S('Pressure Target','**Therapeutic LP** is a central component of cryptococcal care when pressure is elevated or clinically symptomatic.',
    'Remove enough CSF to reduce the pressure substantially, commonly by at least 50% if very high or toward ==20 cm CSF or lower==, documenting a closing pressure. Volumes around 20–30 mL are often required but the pressure response governs.',
    'Repeat, often daily during ongoing symptomatic elevation, according to the clinical and guideline pathway. Pressure can remain dangerous even while antifungals are clearing viable yeast.'),
  S('Escalation and Safeguards','**Persistent or recurrent elevation** may require a drain or shunt after specialist review.',
    'Reassess visual function, consciousness and the possibility of obstruction or another lesion. Do not perform an unsafe LP simply because drainage is generally recommended in cryptococcosis.',
    'Continue effective antifungals, but do not wait for culture sterilization to address a pressure-driven threat. The specific role of serial LP in this disease should not be generalized to every mass-associated intracranial-pressure syndrome.')],['CRYPTO','CRGLOBAL'])

add('Fungal CNS infection','ART Timing in CNS Cryptococcosis',
 'A treatment-naive patient with advanced HIV begins antifungal induction for cryptococcal meningitis. Which general ART timing strategy is recommended?',
 'Usually defer ART for approximately 4–6 weeks after antifungal treatment begins',[
 ('Start ART on the same day in every CNS cryptococcal case','Unlike many other HIV-related infections, very early ART in cryptococcal meningitis can increase mortality and is not the usual recommended strategy.'),
 ('Start after 7 days solely because blood cultures are negative','Blood culture clearance alone does not establish CNS fungal control or remove immune-reconstitution risk; meningeal response and the recommended timing framework matter.'),
 ('Delay ART until a full year of antifungal maintenance has been completed','This unnecessarily prolongs severe HIV-related immune dysfunction. The usual delay is measured in weeks, not completion of long-term maintenance.')],
 [S('Trial and Guideline Rationale','**CNS cryptococcosis is an important exception to immediate ART initiation**.',
    'The COAT trial found worse survival with ART at about 1–2 weeks than with later initiation around five weeks. Guidelines generally recommend a start around ==4–6 weeks== after antifungals begin.',
    'A constrained intracranial compartment, organism burden and inflammatory response contribute to the concern; a low initial CD4 count is not a reason to ignore this disease-specific evidence.'),
  S('Preparing for ART','**Achieve clinical stability and assess microbiological response**, including CSF culture where appropriate.',
    'Control raised pressure, ensure effective induction and consolidation, review interactions and adherence, and arrange close follow-up. The exact timing is individualized when the course is complicated.',
    'Do not extrapolate this delay to every opportunistic infection: PML and many other conditions prioritize prompt immune restoration. Conversely, ART-associated deterioration requires evaluation for IRIS, relapse and other causes rather than automatic ART cessation.')],['CRYPTO'])

add('Fungal CNS infection','Cryptococcal Relapse Versus IRIS',
 'After initial improvement and later ART initiation, a patient develops recurrent meningitic symptoms. CSF cryptococcal antigen remains positive. Which study most directly helps distinguish viable-organism relapse from a sterile inflammatory process?',
 'Repeat CSF fungal culture, interpreted with the clinical course',[
 ('Cryptococcal antigen positivity alone','Antigen may persist after successful treatment, so a positive result cannot by itself demonstrate viable yeast or distinguish relapse from IRIS.'),
 ('A persistently positive India-ink preparation alone','Nonviable organisms can remain visible; microscopy without culture does not establish that ongoing viable infection is causing the deterioration.'),
 ('A CD4-count rise alone','Immune recovery supports an IRIS context but does not exclude adherence problems, resistance or culture-positive recurrent infection.')],
 [S('Viability and Inflammation','**Fungal culture** assesses whether viable Cryptococcus persists or has recurred.',
    'A positive antigen test is useful diagnostically at presentation but can remain positive for a prolonged period. Titer changes alone should not drive a relapse diagnosis or an indefinite induction course.',
    'IRIS often follows immune recovery and may have inflammatory CSF with sterile cultures, but there is no single finding that replaces a full reassessment.'),
  S('Management Branches','**Recheck antifungal adherence, dose, interactions and previous sterility**, as well as opening pressure and alternative infections.',
    'Culture-positive relapse may require renewed induction and susceptibility assessment. For an inflammatory syndrome, continue effective antifungal coverage and usually ART while treating pressure and severe inflammation as clinically indicated.',
    'Corticosteroids are reserved for selected severe IRIS after active uncontrolled infection has been carefully considered; routine steroids for every recurrent headache are inappropriate. Pressure-related deterioration can occur independently of both microbiological relapse and IRIS.')],['CRYPTO','CRGLOBAL'])

add('Fungal CNS infection','CNS Aspergillosis',
 'A neutropenic patient with invasive pulmonary aspergillosis develops brain abscess-like lesions and hemorrhagic infarcts. Which agent has the guideline-preferred primary role for CNS aspergillosis?',
 'Voriconazole',[
 ('Fluconazole','Fluconazole is useful for selected yeasts and consolidation in cryptococcosis, but lacks dependable Aspergillus activity; CNS penetration alone is not sufficient.'),
 ('An echinocandin as routine monotherapy','Echinocandins have selected invasive aspergillosis roles, but poor CNS suitability and evidence make them inappropriate as the routine preferred single CNS agent.'),
 ('Liposomal amphotericin B as mandatory first choice over voriconazole','A lipid amphotericin formulation is an alternative when voriconazole cannot be used or fails, but IDSA places voriconazole first for CNS aspergillosis.')],
 [S('Angioinvasive Disease','**Aspergillus can invade vessels**, producing ischemia, hemorrhage and focal abscesses in addition to pulmonary disease.',
    'Integrate host risk, systemic microbiology, MRI and tissue assessment when feasible; a negative serum test does not exclude every focal CNS case. Distinguish mucormycosis because the preferred drug strategy differs.',
    'CNS disease may arise through bloodstream spread or contiguous sinus extension, and surgery is considered in selected accessible or source-related disease.'),
  S('Treatment and Monitoring','**Voriconazole** is guideline-preferred primary therapy for CNS aspergillosis.',
    'A common IV adult loading regimen is ==6 mg/kg every 12 hours for two doses==, then ==4 mg/kg every 12 hours==, with subsequent route and dose guided by clinical status, interactions and therapeutic monitoring.',
    'Monitor hepatic toxicity, visual or neuropsychiatric effects, QT-related risk and substantial CYP interactions. Assess reversal of immune deficits when feasible. Duration is individualized and prolonged, based on immune recovery and clinical/radiological response rather than a short fixed meningitis course.')],['INDIA'])

add('Fungal CNS infection','Rhino-Orbito-Cerebral Mucormycosis',
 'A patient in diabetic ketoacidosis has invasive necrotic sinus disease extending into the orbit and brain. Tissue shows broad pauciseptate hyphae compatible with Mucorales. Which strategy best fits?',
 'Urgent surgical source control plus liposomal amphotericin B and correction of the metabolic predisposition',[
 ('Voriconazole plus delayed surgery after several weeks','Voriconazole is a major Aspergillus drug but is not dependable Mucorales treatment; delay in source control can permit rapid angioinvasive progression.'),
 ('Fluconazole plus surgery as equivalent mould-directed therapy','Fluconazole lacks reliable activity against Mucorales, so surgical treatment does not make the antifungal choice adequate.'),
 ('An echinocandin alone with correction of hyperglycemia','Risk-factor correction is essential but does not replace active systemic therapy and source control; echinocandin monotherapy is not a standard definitive regimen.')],
 [S('Urgent Combined Treatment','**Rhino-orbito-cerebral mucormycosis** requires rapid multidisciplinary treatment because angioinvasion can cause tissue necrosis, thrombosis and extension.',
    'Obtain tissue for diagnosis without avoidable delay in active treatment. Debridement is coordinated with ENT, ophthalmology, neurosurgery and infection specialists according to extent and feasibility.',
    'Correct ketoacidosis, reduce avoidable immunosuppression and review other predisposing conditions while antifungal therapy proceeds.'),
  S('Antifungal Selection','**Liposomal amphotericin B** is a central first-line agent; CNS involvement commonly leads to a recommended dose around ==10 mg/kg/day== in specialist guidelines.',
    'This is higher than the daily cryptococcal regimen and requires close renal, electrolyte and infusion monitoring. Toxicity can necessitate an individualized alternative strategy.',
    'Isavuconazole or an appropriate posaconazole formulation has selected alternative, step-down or salvage roles. Treatment lasts according to source control, immune/metabolic recovery and imaging response; neither a black eschar nor a single histological feature alone defines the full extent of disease.')],['INDIA'])

add('Viral encephalitis','Immediate Treatment of Suspected HSV Encephalitis',
 'An adult has acute fever, behavioral change, aphasia and a focal seizure with temporal-lobe MRI abnormalities. CSF HSV PCR is pending. Which initial antiviral strategy is most appropriate?',
 'Start intravenous aciclovir promptly while diagnostic evaluation continues',[
 ('Use oral valaciclovir as equivalent initial therapy for severe encephalitis','Oral treatment is not the established substitute for initial IV aciclovir in severe suspected HSV encephalitis; absorption and validated CNS exposure matter.'),
 ('Use foscarnet routinely before evidence of aciclovir resistance','Foscarnet has a role in resistant herpesvirus infection but adds toxicity and is not the standard first choice for this presentation.'),
 ('Use ganciclovir as the preferred empirical HSV agent','Ganciclovir is important for CMV-related disease but does not displace aciclovir as the usual immediate HSV encephalitis treatment.')],
 [S('Time-Critical Antiviral Therapy','**Suspected HSV encephalitis** warrants prompt IV aciclovir rather than waiting for definitive PCR.',
    'A standard adult dose with normal renal function is ==10 mg/kg IV every 8 hours==, using the appropriate weight strategy and renal adjustment. Provide adequate hydration and controlled infusion.',
    'MRI temporal or limbic abnormalities and CSF findings support assessment, but early imaging or CSF can be atypical; a single absent classical feature does not justify delay.'),
  S('Duration and Parallel Care','**Confirmed HSV encephalitis** requires a full IV course, at least 14 days in current adult guidance, with longer treatment in selected immunocompromised or poorly responding patients.',
    'Many pathways use 14–21 days; extension and repeat CSF testing depend on the patient and protocol. Do not shorten treatment to the few days used for uncomplicated skin or mucosal herpes.',
    'Control seizures, assess airway and pressure complications, and pursue bacterial, autoimmune and other infectious alternatives when appropriate. A good early antiviral response does not remove the need for neurological rehabilitation and cognitive follow-up.')],['ENC2026','ENCIDSA'])

add('Viral encephalitis','Early Negative HSV PCR',
 'CSF HSV PCR obtained 18 hours after neurological symptom onset is negative, but the patient has a convincing temporal encephalitic syndrome. What is the best next step?',
 'Continue aciclovir and repeat appropriately timed CSF testing while reassessing alternatives',[
 ('Stop aciclovir solely on the early negative PCR','Early testing can be falsely negative. A high-probability syndrome requires continued coverage and reassessment rather than a single-test exclusion.'),
 ('Replace CSF testing with a positive serum HSV IgG result as definitive proof','Serum IgG usually reflects prior exposure and does not independently establish active HSV infection in the brain.'),
 ('Start immunosuppression without further infectious reassessment because the first PCR is negative','Autoimmune encephalitis is important, but an early negative viral assay does not safely exclude treatable HSV before an immunosuppressive decision.')],
 [S('Timing and False Negatives','**HSV PCR sensitivity depends on illness timing and sample factors**.',
    'An early negative result within the first 72 hours should not overrule a strongly compatible syndrome. Repeat CSF after an appropriate interval while continuing aciclovir; older IDSA guidance specifies repeat testing in 3–7 days in a compatible case.',
    'Current guidance also considers paired CSF/serum intrathecal antibody assessment when testing was delayed or repeated PCR is unrevealing, especially later in the illness.'),
  S('Stopping Criteria Require Context','**Low clinical suspicion plus appropriately timed negative testing** is a different situation from this high-suspicion early sample.',
    'Review MRI, CSF cells, immune status, treatment timing and an established alternative diagnosis. Use the applicable stopping algorithm rather than interpreting any negative PCR as sufficient.',
    'A normal early MRI or few CSF cells can occur. Continue to investigate seizures, structural lesions, autoimmune disease and other pathogens as needed; persistence with the initial hypothesis should remain evidence based, not indefinite by default.')],['ENC2026','ENCIDSA'])

add('Viral encephalitis','Aciclovir-Associated Kidney Injury and Encephalopathy',
 'During IV aciclovir treatment, a patient develops acute kidney injury followed by new hallucinations and myoclonus after earlier neurological improvement. Which possibility requires prompt assessment?',
 'Aciclovir accumulation and neurotoxicity associated with renal dysfunction',[
 ('Virological progression proven by any new neurological symptom','Relapse or progression must be considered, but the drug–renal timeline and prior improvement also strongly suggest toxicity; neurological change is not itself a viral-load measurement.'),
 ('A need to increase the aciclovir dose because kidney injury lowers drug exposure','Reduced renal clearance can increase exposure. Increasing the dose without adjustment can worsen the suspected problem.'),
 ('Post-HSV autoimmune encephalitis as established solely by myoclonus','Autoimmune relapse is a real differential, but requires integrated evaluation; myoclonus during drug accumulation is not sufficient to establish it.')],
 [S('Renal Clearance and Toxicity','**Aciclovir is substantially renally cleared**, and accumulation can cause confusion, hallucinations, tremor or myoclonus.',
    'Crystal-associated nephropathy is promoted by dehydration, rapid infusion and other renal risks. Maintain hydration, infuse according to the product protocol and adjust dose or interval to kidney function.',
    'An initial normal creatinine does not remove the need for serial monitoring during high-dose IV treatment.'),
  S('Distinguishing From Disease','**Review medication, renal trajectory, EEG, imaging and CSF as indicated** rather than assuming every change is viral progression.',
    'Temporarily holding or modifying treatment and specialist assessment may be necessary when toxicity is substantial, while ensuring the infection remains appropriately treated. Severe accumulation may need renal-support measures in selected patients.',
    'Consider other renally cleared neurotoxic drugs and metabolic causes as well. The diagnostic decision balances ongoing HSV risk against preventable drug injury; it is not a blanket instruction to stop antiviral therapy for every symptom.')],['ENC2026','ENCIDSA'])

add('Viral encephalitis','Autoimmune Relapse After HSV Encephalitis',
 'Several weeks after treated HSV encephalitis and initial recovery, a patient develops new psychiatric symptoms, dyskinesias and autonomic instability. Repeat HSV testing is unrevealing. Which process particularly warrants investigation?',
 'Post-HSV autoimmune encephalitis, including NMDA-receptor antibodies',[
 ('HSV replication as the only possible cause of relapse','Viral relapse remains a differential, but a distinct postinfectious autoimmune syndrome is recognized and should not be excluded by the original infectious diagnosis.'),
 ('Postictal confusion alone as a complete explanation for weeks of new symptoms','Seizures can contribute and EEG is useful, but a persistent evolving psychiatric–movement–autonomic syndrome requires broader assessment.'),
 ('An inevitable fixed residual deficit requiring no further work-up','Static residual cognitive injury differs from a new evolving relapse; potentially treatable inflammation should not be dismissed as an unavoidable sequel.')],
 [S('Biphasic Illness','**HSV can trigger neuronal-surface autoimmunity**, sometimes producing a second neurological phase after initial antiviral response.',
    'NMDA-receptor antibodies are important, but other neuronal antibodies can occur. The phenotype may emphasize psychiatric change, movement disorder or cognitive decline rather than recurrence of the original febrile temporal syndrome.',
    'A new phase should prompt evaluation for both recurrent infection and immune-mediated disease, not automatic selection of one from timing alone.'),
  S('Investigation and Treatment','**CSF antibody testing with paired serum where appropriate**, EEG and imaging support assessment after infection and other causes are reviewed.',
    'CSF is particularly important for NMDA-receptor antibody interpretation. A serum-only low-specificity result should not independently establish the diagnosis.',
    'Specialist immunotherapy may be indicated once the evidence supports an autoimmune process and infectious safety has been considered. This is different from routine prophylactic immunosuppression during every acute HSV infection; seizure, autonomic and rehabilitation needs also require active care.')],['ENC2026'])

add('Viral encephalitis','VZV Vasculopathy Without Rash',
 'An immunocompromised adult has multifocal ischemic lesions and a suspected VZV vasculopathy, but no rash and a negative CSF VZV PCR. Which additional test can be especially informative?',
 'Paired CSF and serum assessment for intrathecal anti-VZV IgG synthesis',[
 ('Serum VZV IgG alone','Prior infection or vaccination commonly produces serum IgG. A positive serum result does not establish intrathecal production or a VZV cause of the vascular syndrome.'),
 ('A negative CSF VZV IgM as a definitive exclusion','IgM performance is limited and timing dependent; a negative result does not reliably exclude VZV vasculopathy.'),
 ('Repeating a skin-lesion swab despite the absence of a lesion','Lesion PCR is useful when a lesion exists, but cannot replace a CNS-directed assessment in rashless suspected vasculopathy.')],
 [S('Virological Diagnosis','**VZV vasculopathy can occur without a rash**, and CSF PCR can be negative, particularly later in the course.',
    'Intrathecal anti-VZV IgG synthesis may provide stronger support in that setting. Use paired samples or an appropriate laboratory method to distinguish local production from passive antibody entry.',
    'Neither a vascular beading pattern nor a positive serum antibody is uniquely diagnostic; consider other infectious, inflammatory and noninflammatory arteriopathies.'),
  S('Treatment Context','**IV aciclovir** is commonly used for confirmed or strongly suspected CNS VZV disease with renal-adjusted CNS dosing.',
    'A typical normal-renal adult regimen is 10 mg/kg every 8 hours, often for at least 14 days with duration individualized to immune status and response. Evidence for adjunctive steroids in vasculopathy is less definitive and requires specialist judgment.',
    'Assess ischemic and hemorrhagic complications, vascular imaging and the underlying immunosuppression. A negative early or late PCR should be interpreted with the disease phase rather than treated as a universal exclusion.')],['ENC2026','ENCIDSA'])

add('Viral encephalitis','Japanese Encephalitis Testing',
 'During a rural monsoon-season outbreak, a patient develops febrile encephalitis with parkinsonian features and bilateral thalamic lesions. Which test most directly supports Japanese encephalitis in the appropriate setting?',
 'JEV-specific IgM in CSF using an appropriate assay',[
 ('A single serum JEV IgG result as proof of acute CNS disease','IgG may reflect remote exposure or vaccination. It does not independently establish an acute encephalitic infection.'),
 ('A negative serum viral PCR as a sufficient exclusion','Viremia can be low or transient by neurological presentation, so a negative blood molecular test does not reliably exclude JE.'),
 ('Bilateral thalamic signal change alone as a definitive organism diagnosis','Thalamic involvement is suggestive but also occurs in other infectious, metabolic and vascular disorders; organism-directed testing remains important.')],
 [S('Syndrome and Laboratory Support','**JE** is a flaviviral encephalitis associated with mosquito exposure in relevant regions and seasons.',
    'Thalamic, basal ganglia or brainstem involvement and movement abnormalities may occur. CSF JEV IgM capture testing is a key diagnostic approach, interpreted with epidemiology and timing.',
    'Early tests can be negative, while flavivirus cross-reactivity or recent vaccination can complicate antibody interpretation. Reference confirmation or follow-up samples may be needed.'),
  S('Treatment and Outcomes','**No proven specific antiviral treatment** replaces supportive neurological care.',
    'Manage airway and ventilation, seizures, hydration, pressure complications and systemic instability. Empirical aciclovir may be needed while treatable HSV remains in the differential, but it is not a proven JE-specific therapy.',
    'Survivors may have substantial cognitive, behavioral or motor sequelae and need rehabilitation. Prevention relies on indicated vaccination and mosquito-exposure reduction; a characteristic MRI pattern should not lead to neglect of alternative treatable causes.')],['JE','JETX'])

add('Viral encephalitis','West Nile Acute Flaccid Myelitis',
 'A patient with febrile encephalitis develops asymmetric flaccid weakness, absent reflexes and relatively preserved sensation during the acute illness. CSF shows pleocytosis. Which mechanism particularly fits neuroinvasive West Nile disease?',
 'Anterior-horn motor-neuron injury',[
 ('Typical postinfectious demyelinating Guillain–Barré syndrome','GBS is an important differential, but a concurrent febrile CNS illness, marked asymmetry and CSF pleocytosis favor a poliomyelitis-like anterior-horn syndrome.'),
 ('A purely sensory dorsal-root ganglionopathy','Ganglionopathy would prominently affect sensation and sensory action potentials; the predominantly motor asymmetric areflexic pattern points elsewhere.'),
 ('A length-dependent chronic axonal polyneuropathy','A chronic distal symmetric neuropathy does not explain acute asymmetric paralysis arising with encephalitis.')],
 [S('Motor Phenotype','**West Nile neuroinvasive disease** can cause meningitis, encephalitis or acute flaccid myelitis.',
    'Anterior-horn injury can produce asymmetric weakness and areflexia with limited sensory loss, sometimes with bulbar or respiratory failure. This differs from assuming that every areflexic paralysis is peripheral demyelinating GBS.',
    'Electrodiagnostic and spinal imaging findings can help define the affected motor system and distinguish mimics.'),
  S('Testing and Support','**CSF or serum WNV IgM** is commonly used with appropriate confirmatory interpretation.',
    'Antibodies can persist and flaviviral cross-reactivity can complicate results; test timing and local epidemiology matter. Early neutrophilic CSF does not automatically exclude an arboviral process.',
    'Monitor respiratory function closely and provide supportive care and rehabilitation. No universally effective proven antiviral regimen is established; immunotherapies or antivirals should not be presented as standard cures on the basis of anecdotal reports.')],['WN'])

add('Viral encephalitis','Antemortem Evaluation of Suspected Rabies',
 'A patient with a remote untreated mammalian bite develops episodic pharyngeal spasms, aerophobia and encephalitic symptoms. Which diagnostic approach is most appropriate?',
 'Urgent reference-laboratory testing using multiple appropriate specimens, including saliva and nuchal skin with serum/CSF assessment',[
 ('A single negative saliva sample as a definitive rule-out','Viral shedding can be intermittent, and no single negative specimen reliably substitutes for the coordinated antemortem testing strategy.'),
 ('A positive serum antibody alone as proof of infection regardless of vaccination history','Vaccination or immunoglobulin exposure affects serum interpretation; context and other specimens are necessary to establish the diagnosis.'),
 ('A normal routine CSF profile as sufficient exclusion','Routine CSF cells and chemistry are not a rabies-specific rule-out test; specialized molecular, antigen or antibody assessment is required.')],
 [S('Diagnosis and Clinical Care','**Rabies evaluation requires urgent public-health and reference-laboratory coordination**.',
    'Saliva, nuchal skin containing hair follicles, serum and CSF are used in an appropriate combined testing plan, sometimes with repeated saliva sampling. A paralytic form may lack the classic furious presentation.',
    'Once neurological disease is established, prognosis is extremely poor and no reproducibly effective curative protocol is proven. Provide expert supportive and goals-of-care assessment rather than promising benefit from an experimental coma regimen.'),
  S('Exposure Prevention Is Different','**PEP prevents disease before clinical rabies**, and must not be confused with treating established encephalitis.',
    'After a qualifying exposure, promptly clean the wound and use the locally approved vaccine/immunoglobulin pathway. Under the CDC IM approach for an unvaccinated immunocompetent person, vaccine is given on days 0, 3, 7 and 14 with human RIG 20 IU/kg infiltrated into wounds as appropriate.',
    'Previously vaccinated and immunocompromised patients have different schedules; WHO-approved intradermal pathways also exist. Saliva exposure through broken skin or mucosa requires assessment, while casual contact alone does not automatically require PEP.')],['ENC2026'])

add('Brain abscess and empyema','Diffusion Imaging of a Pyogenic Abscess',
 'A patient with fever and recent dental infection has a smooth ring-enhancing brain lesion. Its central cavity is bright on DWI with low ADC. Which diagnosis is most supported?',
 'Pyogenic brain abscess',[
 ('Necrotic brain metastasis','A necrotic metastasis can ring enhance, but its fluid center more often has facilitated rather than marked restricted diffusion; the infection context strengthens the abscess interpretation.'),
 ('Glioblastoma with central necrosis','Glioblastoma can mimic an abscess, but irregular infiltrative tissue and other imaging findings commonly differ. Central restricted diffusion with this clinical context favors pus, without being absolutely specific.'),
 ('Tumefactive demyelination','An open-ring pattern and other demyelinating features can suggest this alternative; it is less consistent with a purulent cavity pattern and a compatible infectious source.')],
 [S('Imaging Principle','**Viscous cellular pus** commonly restricts water diffusion, producing central DWI hyperintensity with low ADC.',
    'Contrast MRI defines ring enhancement, edema, satellite lesions and complications. Diffusion is highly useful but not perfectly specific: some tumors, granulomatous lesions or treated infections can overlap.',
    'DWI brightness alone can reflect T2 effects, so the ADC map and the location of restriction matter.'),
  S('Microbiology and Safety','**Source investigation and neurosurgical sampling** help establish the organism and guide therapy.',
    'Dental, sinus, ear, bloodstream, endocardial, traumatic and postoperative routes suggest different spectra. Multiple lesions may indicate hematogenous spread, but number alone does not identify the organism.',
    'A space-occupying lesion requires assessment of mass effect and LP safety; CSF sampling is not the preferred way to aspirate an abscess diagnosis. Coordinate urgent therapy with planned tissue or pus collection when feasible, without delaying treatment of severe disease.')],['ABSC','INDIA'])

add('Brain abscess and empyema','Community Brain Abscess Treatment',
 'An immunocompetent adult has a 3.8-cm frontal abscess after sinus infection, with mass effect and a focal deficit. Which empirical antimicrobial combination best covers common streptococci and anaerobes while surgical care is arranged?',
 'Ceftriaxone plus metronidazole',[
 ('Ceftriaxone alone','Ceftriaxone covers many streptococci and relevant bacteria but does not provide the full anaerobic strategy needed for a typical contiguous sinus-source abscess.'),
 ('Vancomycin plus cefepime without anaerobic coverage','This fits many healthcare-associated spectra better, but omits the usual anaerobic component for the stated community contiguous source unless another agent is added.'),
 ('Vancomycin alone','It can cover resistant Gram-positive organisms but does not provide the appropriate mixed bacterial and anaerobic coverage for this source.')],
 [S('Empirical Regimen','**A third-generation cephalosporin plus metronidazole** is a standard community abscess regimen in an appropriate host.',
    'Common adult doses with normal organ function are ==ceftriaxone 2 g IV every 12 hours== and ==metronidazole 500 mg every 8 hours==. Tailor treatment when culture and susceptibility are available.',
    'Postoperative or penetrating-trauma disease often needs resistant staphylococcal and Gram-negative coverage; severe immunocompromise raises additional fungal, Nocardia and other possibilities.'),
  S('Source Control','**The large symptomatic lesion with mass effect needs urgent neurosurgical evaluation**, usually for aspiration or another suitable intervention.',
    'Size is one factor rather than an inflexible universal cut-off; location, accessibility, mass effect, clinical course and organism matter. Treat the sinus or other source as well.',
    'In a stable selected patient, a brief coordinated wait for prompt aspiration can improve microbiological yield, but severe disease should not wait untreated. Decompression, diagnosis and antibiotic choice are parts of the same plan.')],['ABSC','INDIA'])

add('Brain abscess and empyema','Duration and Follow-Up of Brain Abscess Therapy',
 'A pyogenic brain abscess has been aspirated and cultures guide therapy. Which statement best reflects the ESCMID approach to antimicrobial duration for a typical aspirated or medically managed bacterial abscess?',
 'A prolonged course, commonly 6–8 weeks, with clinical and imaging reassessment',[
 ('Stop at seven days if the fever has resolved','Fever resolution does not establish sterilization of a focal intracranial collection; a short systemic-infection course is not sufficient by itself.'),
 ('Use a mandatory early oral switch after 48 hours in every patient','Evidence for a routine early oral switch is limited and does not support an automatic rule regardless of organism, drainage and response.'),
 ('Continue unchanged antibiotics indefinitely until every trace of enhancement disappears','Residual enhancement may lag behind recovery. Imaging must be interpreted with clinical response, abscess size, microbiology and complications rather than using an indefinite single-sign endpoint.')],
 [S('Duration Framework','**ESCMID 2024** generally supports about ==6–8 weeks== of treatment for bacterial abscess managed by aspiration or without excision, with individual exceptions.',
    'The evidence is not equally strong for every surgical and microbiological subgroup. Complete excision or particular organisms can change duration, so the question specifies the common aspirated/medical context.',
    'A confirmed pathogen allows narrowing and avoids unnecessary toxicity from prolonged broad empirical combinations.'),
  S('Assessing Progress','**Serial neurological review and imaging** evaluate cavity size, edema, recurrence and new complications.',
    'Investigate unexpected deterioration promptly for inadequate drainage, resistant or alternative pathogens, rupture into ventricles, hydrocephalus or seizures. Do not wait for a scheduled scan when the patient worsens.',
    'Monitor agent-specific toxicity, including renal, hepatic, blood-count or neurological effects. An oral strategy, if considered in a selected patient, needs reliable absorption, adherence and a specialist-supported regimen rather than extrapolation from a short uncomplicated extracranial infection.')],['ABSC'],style='direct')

add('Brain abscess and empyema','Corticosteroids for Severe Abscess-Related Edema',
 'A patient with a brain abscess develops severe perifocal edema and impending herniation while emergency neurosurgical treatment is arranged. What is the best interpretation of steroid use?',
 'Corticosteroids can be indicated for the severe edema while definitive treatment proceeds',[
 ('Steroids are prohibited in every brain abscess regardless of pressure physiology','The concern about infection does not justify withholding a potentially life-saving anti-edema intervention in the severe setting described.'),
 ('Steroids replace drainage and antimicrobial treatment once edema improves','Symptomatic reduction of edema does not eradicate the collection or remove its cause; definitive source and antimicrobial treatment remain necessary.'),
 ('Every small stable abscess requires the same prolonged high-dose steroid course','Routine exposure in uncomplicated disease is a different question. The severe mass-effect indication does not create a universal steroid prescription.')],
 [S('Defined Indication','**Severe edema or impending herniation** can justify corticosteroids in brain abscess under specialist management.',
    'ESCMID guidance supports this selected use despite limitations in comparative evidence. Dexamethasone dose and duration follow the acute neurocritical situation and should be reassessed frequently.',
    'Do not turn an appropriate rescue indication into indefinite therapy after the pressure threat resolves.'),
  S('Parallel Definitive Care','**Airway, perfusion, neurosurgical source control and effective antimicrobials** proceed together.',
    'Steroids can alter imaging and inflammatory manifestations and carry glucose, infection, psychiatric and other risks. A response does not establish a noninfectious diagnosis.',
    'If the lesion diagnosis is uncertain, remember that lymphoma and other tumors may also improve after steroids, potentially affecting tissue diagnosis. The need to preserve diagnostic yield should be balanced against an immediate herniation threat rather than used as a reason to delay life-saving treatment.')],['ABSC'])

add('Brain abscess and empyema','Subdural Empyema',
 'A patient with sinusitis develops fever, focal seizures and rapidly progressive weakness. MRI shows a crescentic diffusion-restricting extra-axial collection. Which strategy is most appropriate?',
 'Urgent neurosurgical drainage assessment with intravenous antibiotics',[
 ('Treat as an uncomplicated sterile subdural hygroma and observe','A diffusion-restricting collection with fever and rapid neurological deterioration strongly suggests empyema rather than a benign sterile fluid collection.'),
 ('Manage with oral sinusitis antibiotics alone','Intracranial suppuration with neurological compromise requires CNS-appropriate parenteral treatment and source-control assessment, not an uncomplicated sinus regimen.'),
 ('Wait for a repeat scan several weeks later before surgical review','Subdural infection can spread rapidly across the compartment; the current deterioration is already an urgent reason for neurosurgical involvement.')],
 [S('Anatomical Emergency','**Subdural empyema** is purulent infection in the subdural space and can progress quickly.',
    'Sinus or ear disease, trauma and surgery are important contexts. Fever, headache, seizures, meningism or focal deficits may occur; rapid deterioration differentiates the management urgency from many incidental collections.',
    'Contrast MRI with diffusion helps identify the infected extra-axial compartment and associated cerebritis or venous complications.'),
  S('Combined Treatment','**Drainage plus antibiotics** is commonly needed, coordinated with treatment of the contiguous source.',
    'A third-generation cephalosporin plus metronidazole is a common community-source starting framework; add or alter resistant staphylococcal/Gram-negative coverage according to trauma, surgery and local risk. Obtain operative cultures when feasible.',
    'Control seizures and assess mass effect, venous thrombosis and airway needs. LP does not drain the subdural space and may be unsafe with mass effect. Duration and follow-up are individualized with infection and neurosurgical teams rather than copied from uncomplicated meningitis.')],['ABSC','INDIA'])

add('Parasites and other CNS infections','One or Two Viable Parenchymal Cysticerci',
 'A patient with a seizure has two viable parenchymal cysticerci, no raised intracranial pressure and no ocular cyst. Under IDSA/ASTMH guidance, which antiparasitic approach is preferred?',
 'Albendazole monotherapy with indicated adjunctive corticosteroids',[
 ('Albendazole plus praziquantel as the required regimen for every cyst burden','Combination therapy has a specific preferred role when more than two viable parenchymal cysts are present; it is not mandatory for the one-to-two-cyst situation.'),
 ('Praziquantel alone as the preferred initial regimen','Praziquantel has cysticidal activity, but albendazole is the preferred monotherapy under the specified guideline for this burden and setting.'),
 ('Symptomatic therapy alone because viable cysts cannot respond to drugs','Symptomatic-only treatment is appropriate for calcified lesions and selected contraindicated situations, not the usual recommendation for treatable viable cysts without pressure contraindications.')],
 [S('Viability Guides Treatment','**One or two viable parenchymal cysts** are generally treated with albendazole rather than no cysticidal therapy when treatment is safe.',
    'A typical regimen is ==15 mg/kg/day in two divided doses, maximum 1200 mg/day, for 10–14 days==. Begin indicated corticosteroids before antiparasitic therapy to limit treatment-provoked inflammation.',
    'Provide antiseizure medication for patients with seizures and assess drug interactions. The number, stage and compartment of cysts are all relevant.'),
  S('Before and After Treatment','**Exclude ocular involvement and uncontrolled intracranial pressure** before starting cysticidal drugs.',
    'MRI helps define viable or extraparenchymal disease, while noncontrast CT is useful for calcification. Follow-up imaging assesses cyst resolution rather than assuming seizure control proves parasitological cure.',
    'Antiseizure withdrawal is individualized to lesion resolution, seizure history and recurrence risk; residual calcification can sustain an epileptogenic substrate even after viable cysts disappear. Do not copy the treatment course for a ventricular or subarachnoid cyst from this parenchymal regimen.')],['NCC'])

add('Parasites and other CNS infections','Multiple Viable Parenchymal Cysticerci',
 'A patient has six viable parenchymal cysticerci with seizures, but no uncontrolled pressure, hydrocephalus or ocular disease. Which regimen is preferred under IDSA/ASTMH guidance?',
 'Albendazole plus praziquantel with corticosteroids started before cysticidal therapy',[
 ('Albendazole alone as the preferred regimen regardless of cyst number','Albendazole monotherapy is appropriate for one or two viable cysts, but combination treatment is preferred when the viable parenchymal burden exceeds two.'),
 ('Praziquantel alone as equivalent preferred combination treatment','Monotherapy omits the dual regimen supported for this larger viable burden and should not be assumed to have the same cyst-resolution performance.'),
 ('Antiseizure treatment alone despite safely treatable viable disease','Antiseizure drugs control symptoms but do not eradicate viable cysts; symptomatic-only care has a different role for calcified disease or temporary treatment contraindications.')],
 [S('Combination Regimen','**More than two viable parenchymal cysts** are generally treated with albendazole plus praziquantel.',
    'Use albendazole ==15 mg/kg/day==, typically maximum 1200 mg/day, and praziquantel ==50 mg/kg/day== for ==10–14 days== under the guideline pathway. Doses are divided according to the regimen.',
    'Corticosteroids start before cysticidal drugs, and antiseizure treatment is given when seizures have occurred. Check renal/hepatic and interaction considerations appropriate to the chosen drugs.'),
  S('Compartment and Inflammation','**The parenchymal regimen is not universal NCC therapy**.',
    'Ventricular obstruction, diffuse cerebral edema, subarachnoid disease or ocular cysts may require a different sequence, longer treatment or surgery. Killing organisms can acutely worsen inflammation, which is why pressure and location are reviewed first.',
    'Plan follow-up imaging and neurological review. Persistent cysts may need reassessment or retreatment, but an isolated residual calcification is not evidence that another course of cysticidal drugs is necessarily beneficial.')],['NCC'],table=(['NCC pattern','Usual initial framework','Important exception'],[
 ['1–2 viable parenchymal cysts','Albendazole alone','Only when pressure/ocular assessment permits'],['>2 viable parenchymal cysts','Albendazole + praziquantel','Steroids before cysticidal drugs'],
 ['Calcified parenchymal lesions','Symptomatic management','No viable cyst to kill'],['Ventricular obstruction/diffuse edema','Treat complication first','Do not reflexively start parenchymal regimen']]))

add('Parasites and other CNS infections','Calcified Neurocysticercosis',
 'An adult with seizures has only small fully calcified parenchymal lesions on CT, without viable cysts or hydrocephalus. What is the most appropriate treatment principle?',
 'Treat seizures and other symptoms rather than prescribe antiparasitic therapy for the calcifications',[
 ('Give albendazole plus praziquantel until the calcium disappears','Calcifications represent nonviable residues and do not disappear through killing an active parasite; repeated cysticidal treatment adds risk without that target.'),
 ('Give routine prolonged corticosteroids to all patients with calcified lesions','Steroids are not routinely recommended for isolated calcified parenchymal NCC, even though selected inflammatory episodes may require individualized assessment.'),
 ('Require surgical excision of every calcification before antiseizure treatment','Most patients are managed medically. Surgery is reserved for selected refractory focal epilepsy or other specific indications, not every incidental calcification.')],
 [S('Residual Epileptogenic Lesions','**Calcified NCC contains no viable parasite target** for albendazole or praziquantel.',
    'Antiseizure therapy and clinical follow-up address the ongoing problem. Calcification does not mean that seizure risk has disappeared; gliosis and intermittent perilesional inflammation can remain relevant.',
    'MRI can be useful when symptoms suggest edema, another lesion stage or a complication not defined by CT alone.'),
  S('Inflammation and Long-Term Decisions','**Perilesional edema** may recur around calcified lesions, but routine corticosteroid treatment is not a universal answer.',
    'Assess severity and alternative causes and avoid reflexive repeated steroid exposure; abrupt withdrawal may complicate inflammatory dynamics in selected cases. Antiparasitic treatment should not be restarted merely because edema is seen around calcium.',
    'Medication withdrawal depends on seizure control, prior recurrence, EEG and structural risk. Selected drug-resistant focal epilepsy may warrant surgical evaluation, but localization and risk assessment are required rather than removing all visible calcifications.')],['NCC'])

add('Parasites and other CNS infections','Raised Pressure Before Cysticidal Therapy',
 'A patient with NCC has a ventricular cyst, obstructive hydrocephalus and declining consciousness. Which management sequence is most appropriate?',
 'Address hydrocephalus and obtain urgent specialist surgical assessment before cysticidal treatment',[
 ('Start albendazole immediately and expect obstruction to resolve before inflammation develops','Cysticidal therapy can intensify inflammation and worsen an already dangerous obstruction; immediate drug killing is not the first priority here.'),
 ('Use the two-week parenchymal combination regimen without reviewing cyst location','Ventricular disease has different anatomical and surgical considerations; the standard viable parenchymal course cannot be copied blindly.'),
 ('Treat only seizures because ventricular cysts never require mechanical intervention','Seizure control does not relieve obstructed CSF flow; endoscopic removal or CSF diversion may be necessary depending on anatomy and feasibility.')],
 [S('Stabilize the Neurological Complication','**Cysticidal therapy is rarely the immediate emergency in NCC**, whereas pressure-related deterioration can be.',
    'Assess airway, perfusion, imaging and herniation risk urgently. A mobile or obstructing ventricular cyst may be suitable for endoscopic removal; CSF diversion is selected according to the situation.',
    'Diffuse cerebral edema also requires pressure and anti-inflammatory management before considering antiparasitic treatment.'),
  S('Why Sequence Matters','**Parasite death releases inflammatory stimuli**, which can worsen edema or CSF obstruction.',
    'Specialist teams determine whether and when antiparasitic treatment is needed after surgery or stabilization. Avoid preoperative cysticidal treatment when it could make a removable ventricular cyst inflamed or adherent.',
    'Subarachnoid disease may need prolonged therapy and inflammation control, unlike a simple two-week parenchymal course. The aim is safe control of the full disease compartment, not simply the fastest administration of an anthelminthic.')],['NCC'])

add('Parasites and other CNS infections','Ocular Cysticercosis Before Antiparasitic Treatment',
 'Before starting albendazole for confirmed NCC, which associated finding particularly requires ophthalmic assessment because drug-induced inflammation could threaten vision?',
 'An intraocular cysticercus',[
 ('A subcutaneous cysticercal nodule without ocular involvement','This can support systemic infection but does not carry the same immediate intraocular inflammatory hazard that changes the treatment sequence.'),
 ('An intestinal adult Taenia carrier state as proof of an ocular contraindication','Tapeworm carriage has important treatment and transmission implications but does not itself establish an intraocular cyst or the associated visual risk.'),
 ('A remote fully calcified muscle lesion alone','Calcified peripheral disease can indicate past infection but does not demonstrate a viable eye lesion that might inflame during CNS cysticidal therapy.')],
 [S('Pretreatment Eye Examination','**Funduscopic examination** is recommended before antiparasitic therapy for NCC to identify possible ocular involvement.',
    'An intraocular cyst may need surgical ophthalmic management before systemic cysticidal treatment because treatment-provoked inflammation can damage vision. Further ocular imaging is selected when examination or symptoms warrant it.',
    'Ask about visual loss, floaters and ocular symptoms, but absence of symptoms does not replace the recommended assessment.'),
  S('Other Essential Preparation','**Review cyst stage, compartment and intracranial pressure** along with the eye findings.',
    'Start indicated corticosteroids before cysticidal drugs and manage seizures appropriately. Antiparasitic treatment of viable parenchymal disease is different from symptomatic care of calcifications or urgent management of ventricular obstruction.',
    'For prolonged albendazole courses, monitor relevant blood counts and hepatic effects. Consider exposure, household transmission and tapeworm-carrier assessment according to the setting, but do not confuse acquisition of eggs causing cysticercosis with eating a cyst-containing meat product causing intestinal taeniasis.')],['NCC'],style='direct')

add('Parasites and other CNS infections','Presumptive Toxoplasma Encephalitis and Biopsy',
 'An adult with HIV, CD4 35/µL and positive Toxoplasma IgG has multiple compatible ring-enhancing brain lesions. Appropriate anti-Toxoplasma therapy is started. There is no clinical improvement by day 14 despite verified treatment. What is the best next step?',
 'Reassess the diagnosis and strongly consider brain biopsy',[
 ('Continue unchanged empirical treatment for months before considering alternatives','Most responding cases improve clinically within approximately 10–14 days; persistent nonresponse requires evaluation rather than indefinite assumption of the same cause.'),
 ('Diagnose primary CNS lymphoma solely because treatment has failed','Lymphoma is important but is not proven by failure alone; tissue or other directed assessment is needed, and other infections or treatment problems remain possible.'),
 ('Use improvement after corticosteroids as specific proof of toxoplasmosis','Steroids can improve edema from several lesions, including lymphoma; that response does not reliably identify the organism and can affect biopsy yield.')],
 [S('Empirical-Treatment Context','**Advanced HIV with a compatible multifocal lesion pattern** commonly justifies presumptive treatment when the overall evidence supports toxoplasmosis.',
    'A supported regimen is TMP–SMX at ==TMP 5 mg/kg plus SMX 25 mg/kg twice daily==, IV or orally as appropriate. Pyrimethamine–sulfadiazine with leucovorin is another established regimen.',
    'Acute therapy is generally at least six weeks, longer for extensive or incompletely responding disease, followed by suppressive treatment until immune-reconstitution criteria are met.'),
  S('Response Is Diagnostic Evidence','**Deterioration during the first week or lack of improvement by 10–14 days** warrants reassessment and often biopsy consideration.',
    'Review adherence, dose, absorption, interactions and the differential, including CNS lymphoma, TB, fungal disease and other causes. Earlier biopsy may be appropriate if initial findings are atypical.',
    'Reserve steroids for clinically significant mass effect or other specific indications rather than routine use. Maintain seizure treatment if needed and plan ART and toxicity monitoring through the HIV/infection team.')],['TOXO'])

add('Parasites and other CNS infections','Progressive Multifocal Leukoencephalopathy',
 'A patient with advanced HIV develops subacute progressive focal deficits. MRI shows asymmetric subcortical white-matter lesions involving U-fibers, with little mass effect and no prominent ring enhancement. Which test is most directly supportive of the suspected diagnosis?',
 'CSF JC-virus PCR in the appropriate clinical and imaging context',[
 ('Serum JC-virus antibody as proof of active brain infection','Prior exposure is common; a positive serum antibody does not establish active PML or distinguish asymptomatic infection from CNS disease.'),
 ('CSF Toxoplasma IgG as the defining test for this white-matter syndrome','Toxoplasma exposure and encephalitis need a different diagnostic framework, usually with focal mass lesions; that antibody does not establish PML.'),
 ('A normal CT as a sufficient exclusion of PML','MRI is more sensitive for the typical white-matter changes; normal or subtle CT findings do not exclude the suspected progressive demyelinating infection.')],
 [S('Clinical and Imaging Pattern','**PML is JC-virus-associated demyelinating disease**, usually in an immunocompromised setting.',
    'Subacute asymmetric deficits and multifocal white-matter lesions with limited mass effect are characteristic. Inflammatory PML or PML-IRIS can enhance and swell, so absence of enhancement is not an absolute requirement.',
    'CSF PCR supports diagnosis, but sensitivity can be lower with immune restoration or low viral burden; a negative result may require repeat sensitive testing or selected biopsy when suspicion persists.'),
  S('Immune Restoration','**Prompt effective ART** is the principal treatment approach in HIV-associated PML.',
    'No specific antiviral drug has consistently demonstrated curative benefit. Review the cause of immunosuppression in non-HIV cases and consider its reversal where feasible.',
    'Monitor for IRIS and its complications; steroids are considered for selected clinically important inflammatory edema rather than given routinely to every PML case. This prompt-ART strategy contrasts with the usual deliberate delay in CNS cryptococcosis.')],['PML'])

add('Parasites and other CNS infections','Neurosyphilis Treatment and CSF Interpretation',
 'An adult has compatible neurological findings and laboratory-supported neurosyphilis. Which regimen is recommended by the CDC as the preferred treatment?',
 'Aqueous crystalline penicillin G 18–24 million units/day IV for 10–14 days',[
 ('Benzathine penicillin G 2.4 million units IM weekly for three doses as the sole CNS regimen','This treats selected non-neurosyphilis stages but does not provide the standard adequate CNS regimen for established neurosyphilis.'),
 ('A single 2.4-million-unit IM benzathine penicillin dose','This is used for selected early syphilis without CNS disease; it is not sufficient for the neurological infection described.'),
 ('Oral doxycycline for seven days as equivalent preferred therapy','A short oral course is not the CDC preferred CNS treatment and should not be substituted for a proven parenteral neurosyphilis regimen.')],
 [S('Recommended Regimen','**Aqueous crystalline penicillin G** is given as ==3–4 million units IV every 4 hours== or continuous infusion, totaling 18–24 million units daily for 10–14 days.',
    'Selected alternative regimens require specialist review of allergy, adherence and evidence. Procaine penicillin plus probenecid is a specific alternative when reliable administration is feasible, not the same as benzathine penicillin.',
    'Ocular and otic syphilis can require the neurosyphilis treatment approach even when routine CSF findings are normal.'),
  S('Diagnostic and Follow-Up Principles','**CSF-VDRL is specific but insensitive** in the correct uncontaminated clinical setting.',
    'A negative result does not exclude every compatible case; interpret CSF cells/protein and treponemal studies with serum serology and the examination. Positive treponemal tests can persist and are not a simple cure marker.',
    'Follow clinical and quantitative nontreponemal responses and assess HIV. A transient Jarisch–Herxheimer reaction differs from penicillin allergy; long-term neurological recovery depends on the type and duration of injury as well as microbiological treatment.')],['SYPH'],style='direct')

add('Parasites and other CNS infections','Primary Amebic Meningoencephalitis',
 'A previously healthy swimmer develops rapidly fulminant meningitis after warm freshwater entered the nose. CSF is neutrophilic and routine bacterial studies are unrevealing. Which pathogen deserves urgent targeted testing?',
 'Naegleria fowleri',[
 ('Acanthamoeba species','These more often cause granulomatous amebic encephalitis with a slower focal course, frequently in an immunocompromised host, rather than the classic rapidly fulminant post-freshwater syndrome.'),
 ('Balamuthia mandrillaris','Balamuthia can cause severe granulomatous encephalitis in several host groups, but the acute nasal freshwater-associated presentation particularly suggests Naegleria.'),
 ('Angiostrongylus cantonensis','This typically causes eosinophilic meningitis after ingestion-related exposure; the tempo, route and neutrophilic syndrome here fit a different organism.')],
 [S('Route and Clinical Course','**Naegleria enters through the nose** and can cause rapidly progressive primary amebic meningoencephalitis.',
    'Warm freshwater exposure or unsafe nasal irrigation is relevant. Drinking water alone is not the same route, and the common term brain-eating amoeba should not replace precise clinical reasoning.',
    'CSF can resemble bacterial meningitis; request urgent specialized examination and PCR rather than waiting for routine culture to identify the organism.'),
  S('Emergency Laboratory and Treatment Coordination','**Fresh CSF microscopy and reference testing** may demonstrate trophozoites or pathogen DNA.',
    'Coordinate specimen handling with the laboratory and urgent public-health or reference experts. Do not let routine specimen assumptions destroy the chance of recognizing motile organisms or obtaining suitable molecular material.',
    'Treatment is expert-directed and usually combines active agents such as an amphotericin formulation and other drugs, with intensive management of cerebral edema; evidence is limited and prognosis is very poor. A fixed drug-only promise of cure would overstate the evidence.')],['PAM'])

add('Parasites and other CNS infections','Eosinophilic Meningitis',
 'After travel in an endemic region and consumption of raw snails, a patient develops severe headache with CSF eosinophilic pleocytosis. Which cause is most strongly suggested?',
 'Angiostrongylus cantonensis',[
 ('Gnathostoma spinigerum','Gnathostomiasis also causes eosinophilic neurological disease, often after raw freshwater fish or other hosts, with migratory or hemorrhagic features; the snail exposure particularly favors Angiostrongylus.'),
 ('Taenia solium','NCC can cause varied neurological syndromes, but ingestion of eggs and its cystic or meningeal patterns differ; raw snail exposure with eosinophilic meningitis points more specifically elsewhere.'),
 ('Naegleria fowleri','Naegleria is associated with nasal warm-freshwater entry and fulminant neutrophilic meningoencephalitis, not this characteristic ingestion-related eosinophilic syndrome.')],
 [S('Syndromic Definition','**CSF eosinophilia** is commonly defined using about 10 eosinophils/µL or at least 10% of CSF leukocytes, with interpretation of laboratory method and context.',
    'A. cantonensis is an important cause after exposure to infected snails, slugs, contaminated produce or relevant paratenic hosts. A convincing exposure history can guide early testing even before eosinophilia becomes prominent.',
    'The differential includes other helminths, selected fungal infections, drug reactions, malignancy and foreign material; eosinophils do not identify the parasite alone.'),
  S('Confirmation and Treatment Context','**Reference molecular or serological testing** is selected with local expertise and availability.',
    'Manage pain and intracranial pressure and consider a specialist corticosteroid-based approach for significant neuroangiostrongyliasis. Anthelminthic use, timing and co-treatment depend on the setting and evidence; it should not be presented as an unqualified parasite-killing emergency in every case.',
    'Assess neurological progression and alternative diagnoses, particularly when the course, exposure or imaging is atypical. Food and produce safety counseling prevents recurrence but does not replace evaluation of the current meningitis.')],['WHO'])

R.update({
 'ASPER':('IDSA aspergillosis guideline: CNS therapy, 2016','https://www.idsociety.org/practice-guideline/aspergillosis/'),
 'MUCOR':('ECMM/MSG global mucormycosis guideline, 2019','https://pmc.ncbi.nlm.nih.gov/articles/PMC8559573/'),
 'AMBITION':('AMBITION randomized trial: single-dose liposomal amphotericin for cryptococcal meningitis, 2022','https://doi.org/10.1056/NEJMoa2111904'),
 'COAT':('COAT randomized trial: ART timing after cryptococcal meningitis, 2014','https://doi.org/10.1056/NEJMoa1312884'),
 'TBHIV':('Adjunctive dexamethasone for TB meningitis in HIV-positive adults, randomized trial, 2023','https://doi.org/10.1056/NEJMoa2216218'),
 'TBGEN':('Genotype-stratified adjunctive dexamethasone in HIV-negative TB meningitis, phase 3 trial, 2025/2026','https://www.nature.com/articles/s41591-025-04138-z'),
 'VZV':('UCSF Infectious Diseases Management Program: VZV CNS infection testing','https://idmp.ucsf.edu/content/vzv-cns-infection-testing'),
 'POSTHSV':('Armangue et al.: Autoimmune encephalitis after HSV encephalitis, prospective observational study, 2018','https://pmc.ncbi.nlm.nih.gov/articles/pmid/30049614/'),
 'RABTEST':('CDC: Rabies antemortem specimen collection','https://www.cdc.gov/rabies/hcp/suspected-human-rabies/index.html'),
 'RABPEP':('CDC: Rabies post-exposure prophylaxis guidance','https://www.cdc.gov/rabies/hcp/clinical-care/post-exposure-prophylaxis.html'),
 'ANGIO':('CDC: Rat lungworm clinical testing and diagnosis','https://www.cdc.gov/angiostrongylus/hcp/diagnosis-testing/'),
 'LEAK':('ARUP Consult: CSF leak testing and beta-2 transferrin','https://arupconsult.com/content/csf-leak-beta-2-transferrin'),
 'COMP':('CDC: Meningococcal disease in complement inhibitor recipients','https://www.cdc.gov/meningococcal/hcp/clinical-guidance/complement-inhibitor.html'),
})
for n,key in {12:'LEAK',13:'COMP',17:'TBHIV',22:'AMBITION',24:'COAT',26:'ASPER',27:'MUCOR',31:'POSTHSV',32:'VZV',35:'RABTEST',50:'ANGIO'}.items():rows[n-1]['refs'].append(key)
rows[16]['refs'].append('TBGEN');rows[34]['refs'].append('RABPEP')
R['ENC2026']=(R['ENC2026'][0],'https://pmc.ncbi.nlm.nih.gov/articles/PMC13650609/')

# Use realistic alternatives and specify the exact decision instead of relying on giveaways.
rows[2]['others'][1]=('Perform LP after initial fluids and wait for its Gram stain to choose the first antibiotic','Obtaining CSF before treatment is useful in a safe stable patient, but shock makes LP unsuitable now and waiting for the result would delay time-critical treatment.')
rows[6]['others']=[
 ('Trimethoprim–sulfamethoxazole','This is an important Listeria-active alternative when a serious beta-lactam allergy or another constraint prevents ampicillin use; it is not the usual preferred addition in the uncomplicated prescribing situation given.'),
 ('Gentamicin alone','Gentamicin may be used as a selected adjunct, with renal-risk consideration, but it does not replace a reliable CNS-active Listeria treatment backbone.'),
 ('Metronidazole','Metronidazole adds anaerobic coverage for selected abscess sources; it does not close the Listeria gap left by the cephalosporin-containing regimen.')]
rows[7]['others']=[
 ('Ceftriaxone','It is useful for many bacterial meningitides but does not provide reliable Listeria activity; the organism-specific spectrum overrides familiarity with its CNS use.'),
 ('Trimethoprim–sulfamethoxazole','This is a recognized alternative, especially with serious beta-lactam allergy, but ampicillin remains the standard preferred backbone when it is suitable.'),
 ('Meropenem','It has Listeria activity and selected alternative roles, but a broad carbapenem is not the routine preferred definitive replacement for suitable high-dose ampicillin in a susceptible infection.')]
rows[15]['others'][2]=('A six-month BPaLM regimen used for selected drug-resistant pulmonary tuberculosis','BPaLM addresses a different resistance and eligibility setting. It is not the standard adult drug-susceptible TB meningitis regimen and CNS eligibility cannot be assumed from pulmonary evidence.')
rows[16]['others'][1]=('Defer any adjunctive steroid until mycobacterial culture confirmation','Guideline treatment commonly includes probable clinically diagnosed TB meningitis; waiting weeks for culture can postpone an indicated adjunct in a serious high-probability illness.')
rows[16]['others'][2]=('Use a one-week oral prednisone taper as the standard adjunct','Short tapers are used in other inflammatory conditions, but do not reproduce the severity-based six-to-eight-week TB meningitis regimens supporting established practice.')
rows[17]['others'][2]=('A newly acquired fungal abscess as the most likely explanation without further supporting evidence','A second pathogen is a genuine differential, especially with immunosuppression, but the initial response and subsequent tuberculoma-like evolution favor consideration of a paradoxical reaction while microbiology and host risks are reassessed.')
rows[18]['others'][2]=('Escalate corticosteroids alone and defer CSF intervention while waiting for a response','Inflammation may contribute, but declining consciousness with progressive hydrocephalus can require direct urgent pressure relief; a steroid trial alone should not postpone neurosurgical assessment.')
rows[19]['others'][2]=('CSF fungal culture as the only rapid test','Culture is essential for viability and follow-up but takes longer than antigen detection; it complements rather than replaces a rapid antigen assay in the initial evaluation.')
rows[23]['others'][2]=('Wait until the entire eight-week consolidation phase is complete before considering ART','That adds delay beyond the usual four-to-six-week start window and is not a universal prerequisite. CNS response and stability guide an appropriate planned start.')
rows[29]['question']='During IV aciclovir treatment, a patient develops acute kidney injury followed by hallucinations and myoclonus after earlier neurological improvement. Which explanation is most strongly suggested by this sequence?'
rows[29]['others']=[
 ('Aciclovir-resistant HSV progression','Resistance can matter particularly in selected immunocompromised hosts, but the initial response followed by kidney injury and new compatible symptoms makes drug accumulation a more immediate explanation to evaluate.'),
 ('Postinfectious autoimmune encephalitis','This is a real cause of neurological relapse after HSV, but a close relationship to renal dysfunction during active aciclovir dosing favors toxicity in this particular sequence.'),
 ('Nonconvulsive status epilepticus as the established cause','EEG may be required because seizures can coexist, but the clinical sequence alone does not establish status and does strongly raise the recognized renal drug-accumulation problem.')]
rows[30]['question']='Several weeks after completed HSV encephalitis treatment and initial recovery, a patient off aciclovir with stable kidney function develops new psychiatric symptoms, dyskinesias and autonomic instability. Repeat HSV testing is unrevealing. Which process particularly warrants investigation?'
rows[30]['others'][2]=('Persistent aciclovir neurotoxicity as the leading explanation','Drug accumulation is important during treatment, especially with renal impairment, but the patient is now off the drug with stable kidney function and a new delayed autoimmune-type syndrome.')
rows[31]['others'][2]=('Serum VZV PCR as a sufficient replacement for CNS-directed antibody testing','Blood PCR can support disseminated infection in selected cases, but it does not reliably exclude localized or later CNS vasculopathy and cannot replace assessment of intrathecal evidence.')
rows[32]['others'][2]=('CSF JEV PCR as a sufficiently sensitive first rule-out test','A positive molecular result can be helpful, but viral RNA detection is often insensitive by the neurological phase; the appropriate IgM approach is generally more useful for routine confirmation.')
rows[33]['others'][1]=('Botulism','Botulism can cause motor weakness with preserved sensation, but typically has a descending cranial-autonomic syndrome without inflammatory encephalitis or this CSF response.')
rows[33]['others'][2]=('Acute transverse myelitis','Early spinal shock can reduce reflexes, but a sensory level and cord-pattern dysfunction are more typical; the asymmetric predominantly motor phenotype during neuroinvasive WNV suggests anterior-horn injury.')
rows[37]['others'][2]=('Continue the full antibiotic combination until all residual enhancement disappears','Some radiological changes lag behind microbiological and clinical improvement. Duration must incorporate cavity evolution, response and source control rather than require disappearance of every enhancing trace.')
rows[38]['others'][0]=('Avoid corticosteroids to preserve diagnostic yield despite impending herniation','Diagnostic yield and antimicrobial concerns matter, but severe edema or impending herniation is a guideline-supported reason for selected steroid use while definitive care proceeds.')
rows[38]['others'][2]=('Use a prolonged high-dose course for every abscess with any surrounding edema','Imaging edema alone does not establish the same rescue indication as severe symptoms or impending herniation; routine prolonged exposure adds toxicity without an established universal benefit.')
rows[40]['others'][2]=('Antiseizure therapy alone with imaging reassessment','Symptomatic-only therapy fits calcified disease or selected situations where cysticidal treatment is unsafe; the stated safely treatable viable cysts support albendazole under the specified guideline.')
rows[43]['others'][2]=('Treat seizures and monitor ventricular size without immediate surgical review','Seizure control is important but does not directly relieve obstructed CSF flow; declining consciousness already warrants urgent assessment for removal or diversion.')
rows[45]['others'][0]=('Complete the full six-week empirical course before reassessing the cause','A full treatment course is appropriate for a responding confirmed or supported case, but absence of expected improvement by day 14 warrants earlier reassessment and possible biopsy.')
rows[46]['others']=[
 ('Serum JC-virus antibody','Prior exposure is common; antibody positivity is not proof of active demyelinating brain infection and cannot replace appropriate CSF testing.'),
 ('Plasma JC-virus PCR','A positive result can support concern in selected settings, but sensitivity for CNS PML is limited and blood detection does not replace the better-localized CSF assessment.'),
 ('Urine JC-virus PCR','Urinary shedding can occur without PML. It does not establish that JC virus is causing the patient’s progressive white-matter disease.')]
rows[47]['others'][2]=('Doxycycline 100 mg orally twice daily for 14 days','This is used as an alternative in selected early syphilis without CNS disease, but does not constitute the CDC preferred neurosyphilis treatment regimen.')
rows[20]['sections'][1][1][0][1].append('Maintenance discontinuation generally requires at least one year of antifungal treatment, absence of symptoms, CD4 count at least 100/µL and suppressed HIV RNA on effective ART; review the current pathway and restart suppression if immune criteria are lost.')
rows[45]['sections'][0][1][0][1].append('After a response, TMP–SMX maintenance is commonly one double-strength tablet twice daily. Secondary suppression can generally stop after successful acute therapy, no TE symptoms and CD4 above 200/µL for more than six months on ART; restart if CD4 falls below 200.')
rows[48]['sections'][1][1][0][1].append('Current expert multidrug approaches may include conventional amphotericin B, miltefosine, an azole, azithromycin and rifampin, with route, dose and adjuncts coordinated urgently from the latest specialist protocol; these are limited-evidence rescue regimens, not a reliably curative standard.')
R['PAMTX']=('CDC: Clinical care of Naegleria fowleri infection, current multidrug guidance','https://www.cdc.gov/naegleria/hcp/clinical-care/')
rows[48]['refs'].append('PAMTX')
rows[37]['answer']='A prolonged intravenous course, commonly 6–8 weeks, with clinical and imaging reassessment'
for index in [21,23,25]:rows[index]['style']='direct'
rows[23]['question']='In treatment-naive HIV-associated cryptococcal meningitis, which general ART timing strategy is recommended?'
rows[25]['question']='Under IDSA guidance, which listed agent has the preferred primary role for treatment of CNS aspergillosis?'
R['TBGEN']=('Genotype-stratified adjunctive dexamethasone in HIV-negative TB meningitis, randomized phase 3 trial, 2026','https://pmc.ncbi.nlm.nih.gov/articles/PMC13004695/')
rows[28]['sections'][1][1][0][1].append('The 2026 EAN/ESCMID low-suspicion stopping framework requires an appropriately timed negative HSV PCR after 72 hours, normal CSF white cells unless another diagnosis explains them, and no temporal MRI abnormality. High clinical suspicion is not cleared by that early negative sample.')

rows[26]['table']=(['CNS fungal disease','Typical preferred initial approach','Key distinction'],[
 ['Cryptococcal meningitis','Amphotericin-based induction + flucytosine in a specified regimen','Actively manage CSF pressure'],
 ['CNS aspergillosis','Voriconazole; loading 6 mg/kg IV q12h twice, then commonly 4 mg/kg q12h','Angioinvasive infarcts or abscesses'],
 ['CNS mucormycosis','Liposomal amphotericin B, often 10 mg/kg/day, plus source control','Voriconazole does not reliably cover Mucorales']])
rows[46]['table']=(['Process in advanced HIV','Typical imaging clue','Important qualification'],[
 ['PML','Asymmetric white-matter/U-fiber lesions; usually little mass effect','IRIS may enhance and swell'],
 ['Toxoplasma encephalitis','Often multiple enhancing mass lesions','Number and location are not completely specific'],
 ['Primary CNS lymphoma','Enhancing lesion(s), often with deep/periventricular involvement','Steroids can temporarily improve imaging and affect biopsy']])

if __name__=='__main__':
    coverage=ROOT/'Neurology/05. Central Nervous System Infections.coverage.json'
    c=json.loads(coverage.read_text(encoding='utf-8'))
    assert len(rows)==sum(s['questions'] for s in c['sections'])==50
    index=0
    for section in c['sections']:
        assert len(section['decisions'])==section['questions']
        for decision in section['decisions']:
            assert rows[index]['topic']==section['section'],(index,rows[index]['topic'])
            rows[index]['coverageDecision']=decision;index+=1
    save('Neurology',5,'05. Central Nervous System Infections',rows,R,
      'Original postgraduate teaching synthesis with a documented 50-decision coverage map. Decision-sensitive content checked against WHO meningitis guidance 2025, NICE, NCDC India 2025, EAN/ESCMID encephalitis 2026, IDSA/ASTMH, ESCMID brain abscess guidance and current NIH/CDC resources. Resistance patterns, resource availability and host populations modify recommendations and are stated where relevant. Full Harrison’s subscription text was not accessed. No independent clinician validation is claimed.')
    c['status']='authored_validated';c['authoredQuestions']=len(rows)
    c['questionDecisions']=[dict(question=i+1,title=r['title'],decision=r['coverageDecision']) for i,r in enumerate(rows)]
    coverage.write_text(json.dumps(c,ensure_ascii=False,indent=2),encoding='utf-8')
