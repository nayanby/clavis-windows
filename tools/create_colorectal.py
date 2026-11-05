"""Original Colorectal Disorders chapter."""
from qbank_authoring import question,ref,finalize
DIV=ref('AGA Medical Management of Colonic Diverticulitis','https://gastro.org/clinical-guidance/medical-management-of-colonic-diverticulitis/')
LG=ref('ACG 2023 Acute Lower GI Bleeding Guideline','https://doi.org/10.14309/ajg.0000000000002130')
SUR=ref('US Multi-Society Task Force 2020 Post-Polypectomy Surveillance','https://www.asge.org/home/resources/publications/guidelines/recommendations-for-follow-up-after-colonoscopy-and-polypectomy-a-consensus-update-by-the-us-multi-society-task-force-on-colorectal-cancer')
SCR=ref('ACG 2021 Colorectal Screening Guideline: official highlights','https://webfiles.gi.org/docs/media/crc_screening_guidelines_2021_release.pdf')
GEN=ref('NCI PDQ: Genetics of Colorectal Cancer','https://www.cancer.gov/types/colorectal/hp/colorectal-genetics-pdq')
VOL=ref('ASCRS 2021 Colonic Volvulus and Acute Colonic Pseudo-Obstruction Guideline','https://pubmed.ncbi.nlm.nih.gov/34016826/')
rows=[]
def q(*args,**kwargs):rows.append(question(*args,**kwargs))

q('A patient has a first episode of left lower quadrant pain, fever and localized tenderness. What investigation can confirm suspected diverticulitis and assess abscess or perforation?',
 'CT of the abdomen and pelvis with an appropriate contrast protocol',[
 ('Immediate screening colonoscopy during the acute inflammatory phase','This is not the preferred initial diagnostic study and can increase procedural difficulty and risk.'),
 ('A stool occult-blood test as a definitive anatomical diagnosis','It cannot establish diverticular inflammation or complications.'),
 ('A normal abdominal radiograph as sufficient exclusion','Plain films do not reliably exclude diverticulitis.')],
 'Confirm the diagnosis and stage the local complication burden',
 '**CT can identify inflammation, collection, obstruction and extraluminal gas.**',
 ['Clinical diagnosis alone can be inaccurate.', 'Imaging need depends on prior confirmed disease and severity, but is particularly helpful in a first or complicated presentation.'],
 '**Use the findings to choose the pathway.**',
 ['Mild uncomplicated disease differs from abscess or generalized peritonitis.', 'Atypical or persistent disease requires reassessment for alternatives including malignancy.'],
 [['CT','Diagnosis and complication assessment'],['Acute colonoscopy','Usually deferred'],['Persistent atypical course','Reconsider cause']], [DIV], 'clinical_scenario')
q('An immunocompetent patient has mild CT-confirmed uncomplicated diverticulitis, no sepsis, no frailty and good oral tolerance. Which antibiotic principle is appropriate?',
 'Antibiotics can be used selectively rather than automatically in every such case',[
 ('Every uncomplicated case requires prolonged IV antibiotics','That is not the current selective approach.'),
 ('No patient with diverticulitis should ever receive antibiotics','Complications, immune suppression and higher-risk presentations change the recommendation.'),
 ('Antibiotics eliminate the need to reassess worsening symptoms','Clinical deterioration still requires evaluation.')],
 'The indication depends on host and disease risk',
 '**Mild uncomplicated disease in a suitable immunocompetent patient can be managed without routine antibiotics.**',
 ['Comorbidity, vomiting, systemic illness and adverse imaging findings can favor treatment.', 'Immunocompromised patients need a different risk assessment.'],
 '**Provide follow-up and clear deterioration advice.**',
 ['New fever, increasing pain or poor intake can indicate failure or complication.', 'Selective prescribing is not a reason to ignore the patient.'],
 [['Suitable mild uncomplicated disease','Selective antibiotics'],['Complicated/systemically ill/high-risk host','Antibiotics usually indicated'],['Worsening course','Reassess']], [DIV], 'clinical_scenario')
q('A patient with diverticulitis has a drainable 6-cm pericolic abscess and systemic inflammation. What is an appropriate management direction?',
 'Antibiotics plus image-guided drainage when feasible, with surgical assessment',[
 ('Treat like mild uncomplicated disease without considering source control','The abscess makes this a complicated presentation.'),
 ('Perform a routine outpatient surveillance colonoscopy immediately','That does not drain the collection and is not the acute priority.'),
 ('Use fiber alone as definitive treatment of the infected collection','Dietary measures do not provide source control.')],
 'An abscess creates a source-control problem',
 '**A sizable accessible collection often needs drainage in addition to antibiotics.**',
 ['Location, size, stability and local expertise affect the method.', 'Peritonitis or failure can require surgery.'],
 '**Plan later assessment after acute recovery.**',
 ['Evaluate the colon and recurrence strategy according to the case.', 'Do not treat successful drainage as proof that no further diagnostic follow-up is needed.'],
 [['Uncomplicated inflammation','Medical/supportive pathway'],['Large accessible abscess','Antibiotics and drainage'],['Generalized peritonitis/failure','Surgical pathway']], [DIV], 'clinical_scenario')
q('After recovery from an episode of diverticulitis that warrants colon evaluation, when is colonoscopy generally deferred until?',
 'At least about 6-8 weeks and complete clinical resolution, whichever is later',[
 ('The first hours of active severe inflammation as routine screening','Inflammation increases difficulty and potential risk.'),
 ('Exactly ten years regardless of prior examination or cancer concern','The need and timing depend on the clinical episode and prior high-quality evaluation.'),
 ('Only after recurrent perforation','Follow-up can be indicated much earlier.')],
 'Evaluate the colon after the acute tissue state improves',
 '**Delayed examination helps exclude a cancer mimic while reducing acute-procedure risk.**',
 ['A recent high-quality colonoscopy can alter the need.', 'Alarm symptoms may justify an earlier individualized evaluation.'],
 '**Use the actual previous examination and disease severity.**',
 ['Complicated disease deserves particular attention.', 'Do not schedule by a rigid rule without considering recovery.'],
 [['Acute inflammation','Usually defer routine colonoscopy'],['After recovery','Generally 6-8 weeks or later resolution'],['Prior good recent scope','May change follow-up need']], [DIV])
q('A patient has had several uncomplicated diverticulitis episodes. What should guide elective resection discussion?',
 'An individualized assessment of severity, quality of life, complications and preferences rather than episode count alone',[
 ('A mandatory operation after exactly two episodes in every patient','That numerical rule does not reflect individualized modern care.'),
 ('No surgery can ever help if episodes were initially uncomplicated','Selected persistent or recurrent disease can justify discussion.'),
 ('Resection guarantees every future abdominal symptom will disappear','Symptoms and recurrence can persist in some patients.')],
 'Elective surgery is a benefit-risk decision',
 '**The disease course and patient burden matter more than a simple count.**',
 ['Immune status, complications and operative risk are relevant.', 'Confirm that ongoing symptoms are caused by diverticular disease.'],
 '**Explain realistic outcomes.**',
 ['Surgery can reduce recurrence but does not guarantee complete symptom cure.', 'Use shared decisions rather than an automatic threshold.'],
 [['Episode count','One component, not sole rule'],['Quality of life/complications','Major decision factors'],['Counseling','Benefits and limitations']], [DIV])
q('A patient has ongoing hemodynamically significant hematochezia despite initial resuscitation. Which test can rapidly localize active bleeding for possible embolization?',
 'CT angiography',[
 ('A delayed stool FIT as the acute localization test','FIT is not an emergency localization tool.'),
 ('An unprepared screening colonoscopy as the mandatory first study in every unstable case','CTA can be the preferred localization pathway in ongoing significant bleeding.'),
 ('A routine abdominal ultrasound as equivalent arterial bleed mapping','It does not provide the same acute bleeding localization.')],
 'Active significant bleeding can favor a rapid vascular test',
 '**CTA can identify contrast extravasation and guide interventional radiology.**',
 ['Continue resuscitation and consider an upper source when clinically indicated.', 'A positive study can lead promptly to angiographic treatment.'],
 '**Choose the test according to bleeding activity and stability.**',
 ['A stable patient after cessation follows a different pathway.', 'Do not let a diagnostic sequence delay perfusion support.'],
 [['Ongoing significant bleed','CTA localization'],['Positive arterial source','Angiography/embolization assessment'],['Stable ceased bleeding','Prepared diagnostic evaluation']], [LG], 'clinical_scenario')
q('A stabilized lower-GI-bleeding patient needs inpatient colonoscopy. What does the 2023 ACG guideline generally recommend about timing?',
 'A nonurgent inpatient colonoscopy rather than routine colonoscopy within 24 hours for every patient',[
 ('Every case benefits from urgent colonoscopy before adequate preparation','Important outcome benefit has not been established for a universal urgent approach.'),
 ('Colonoscopy should never be used after hematochezia','It remains an important diagnostic and therapeutic test.'),
 ('No follow-up is needed after stabilization','The source and recurrence risks still need evaluation.')],
 'A rushed procedure is not automatically a better outcome strategy',
 '**The guideline does not require routine urgent colonoscopy for all admitted LGIB.**',
 ['Adequate preparation and clinical stability support a high-quality examination.', 'Ongoing major bleeding may instead require a CTA-led pathway.'],
 '**Do not confuse nonurgent with neglected.**',
 ['Plan source evaluation and appropriate antithrombotic review.', 'Reassess promptly if the bleeding recurs or perfusion worsens.'],
 [['Stabilized inpatient','Nonurgent prepared colonoscopy'],['Ongoing major bleeding','Consider CTA pathway'],['Deterioration','Escalate immediately']], [LG])
q('An older patient develops cramping left-sided pain followed by bloody diarrhea after a hypotensive episode. Imaging shows segmental watershed-region colitis with relative rectal sparing. Which diagnosis is favored?',
 'Ischemic colitis',[
 ('Classic untreated UC solely from bleeding','UC usually has a different continuous rectal pattern and clinical context.'),
 ('Uncomplicated hemorrhoids','They do not explain segmental colitis and abdominal pain.'),
 ('A normal response to hypotension requiring no assessment','Bowel ischemia requires evaluation and risk assessment.')],
 'Reduced perfusion can injure vulnerable colonic regions',
 '**Watershed distribution and an acute low-flow trigger support colon ischemia.**',
 ['The splenic flexure and rectosigmoid junction are classic vulnerable areas.', 'Right-sided disease, severe pain or systemic compromise can indicate a higher-risk course.'],
 '**Assess severity and exclude a transmural complication.**',
 ['Peritonitis or persistent deterioration requires urgent surgical involvement.', 'Support perfusion and evaluate vascular and medication contributors.'],
 [['Ischemic colitis','Segmental perfusion-related injury'],['UC','Typically continuous rectal involvement'],['Severe signs','Assess viability and surgery need']], [ref('ACG Colon Ischemia Guideline','https://doi.org/10.1038/ajg.2014.395')], 'clinical_scenario')
q('A patient with severe AS has recurrent bleeding from colonic angiodysplasia. Which mechanism contributes to Heyde syndrome?',
 'High-shear loss of high-molecular-weight von Willebrand factor multimers',[
 ('A universal inherited factor VIII deficiency','The mechanism is an acquired shear-related hemostatic problem.'),
 ('Warfarin exposure is required for the syndrome','Anticoagulation can worsen bleeding but is not required for the syndrome.'),
 ('AS prevents all gastrointestinal vascular lesions','The association is the opposite.')],
 'A valve lesion can affect systemic hemostasis',
 '**Shear across severe AS can promote cleavage of large vWF multimers.**',
 ['This can impair primary hemostasis in bleeding vascular lesions.', 'Other causes of anemia and bleeding still require assessment.'],
 '**Treat the bleeding and assess the valve indication.**',
 ['Endoscopic and other bleeding therapies may be needed.', 'Valve correction can improve the acquired mechanism in appropriate patients.'],
 [['Severe AS','High shear'],['vWF effect','Loss of large multimers'],['Clinical association','Angiodysplasia-related bleeding']], [ref('2025 ESC/EACTS Valvular Heart Disease Guideline','https://doi.org/10.1093/eurheartj/ehaf194')], 'clinical_scenario')
q('An asymptomatic screening FIT is positive. What is the appropriate next diagnostic test?',
 'Colonoscopy',[
 ('Repeat FIT until a negative sample is obtained','A later negative does not resolve the positive result.'),
 ('Treat empirically for hemorrhoids and cancel evaluation','A benign possible bleeding source does not exclude neoplasia.'),
 ('A routine abdominal radiograph','It does not adequately evaluate colonic mucosal neoplasia.')],
 'A stool-based screen is a two-step strategy when positive',
 '**The diagnostic colonoscopy completes the positive-screen pathway.**',
 ['Colonoscopy can identify cancer and remove precursor lesions.', 'A screening test is not a definitive anatomical diagnosis.'],
 '**Explain follow-through before ordering the screen.**',
 ['Patients should understand that a positive result requires further evaluation.', 'Do not use repeated stool sampling as a substitute.'],
 [['Negative FIT','Continue the screening schedule as appropriate'],['Positive FIT','Diagnostic colonoscopy'],['Symptoms/alarm features','May require a diagnostic pathway directly']], [SCR])
q('Under the 2021 ACG framework, at what age can average-risk colorectal cancer screening begin?',
 '45 years',[
 ('30 years for every average-risk adult','This is not the standard average-risk start.'),
 ('60 years regardless of risk','This is later than recommended.'),
 ('Only after anemia develops','Screening precedes symptoms.')],
 'Screening and diagnostic investigation have different triggers',
 '**ACG supports starting average-risk screening at 45.**',
 ['Family history or a hereditary syndrome can require earlier testing.', 'Symptoms or alarm findings need diagnostic assessment at any relevant age.'],
 '**Choose a suitable method and ensure adherence.**',
 ['Colonoscopy and stool-based strategies have different schedules and follow-up needs.', 'A positive noncolonoscopy test usually requires colonoscopy.'],
 [['Average risk','Start at 45 in this framework'],['High familial/genetic risk','Earlier tailored plan'],['Symptoms','Diagnostic rather than screening logic']], [SCR])
q('A patient\'s father had colorectal cancer at 48. Under the ACG family-history approach, when should colonoscopic screening generally begin?',
 'Age 38, ten years before the relative\'s diagnosis',[
 ('Age 45 solely because that is the average-risk start','The earlier family-history rule applies.'),
 ('Age 50 because the patient has no symptoms','Screening does not wait for symptoms.'),
 ('Age 60 after the relative\'s risk has passed','Familial risk is not removed by waiting.')],
 'Use the earlier of age 40 or ten years before the youngest relevant diagnosis',
 '**A first-degree relative diagnosed before 60 supports an earlier colonoscopy pathway.**',
 ['48 minus 10 gives 38, earlier than 40.', 'Multiple affected relatives or a young pedigree can warrant genetic assessment.'],
 '**The subsequent interval depends on the family and examination findings.**',
 ['Do not apply an average-risk stool-only schedule automatically.', 'Confirm the relative\'s actual diagnosis and age where possible.'],
 [['Average-risk start','45'],['Relevant family history','40 or ten years earlier, whichever first'],['This case','38']], [SCR], 'clinical_scenario')
q('At a high-quality colonoscopy, two tubular adenomas measuring 4 and 6 mm are completely removed. There is no high-risk family history or other modifying condition. Under USMSTF 2020, what is the interval?',
 '7-10 years',[
 ('Six months','That is used for selected large piecemeal resections, not these small completely removed adenomas.'),
 ('One year','That is more consistent with very high adenoma counts or other special circumstances.'),
 ('Three years','Advanced findings usually justify the shorter interval, not this low-risk pattern.')],
 'Low-risk adenomas do not need routine short-interval surveillance',
 '**One or two tubular adenomas below 10 mm support a 7-10-year interval in this guideline.**',
 ['The baseline examination and complete removal must be reliable.', 'Hereditary disease, IBD and important family history change the pathway.'],
 '**State the guideline system.**',
 ['European recommendations can return some low-risk patients to routine screening.', 'Do not mix intervals without the associated assumptions.'],
 [['1-2 small tubular adenomas','7-10 years, USMSTF'],['Advanced lesion','Usually shorter'],['Poor quality/incomplete removal','Requires separate planning']], [SUR])
q('A completely removed 14-mm adenoma is found at a high-quality examination. There are no other modifying risks. What is the usual USMSTF surveillance interval?',
 'Three years',[
 ('Ten years as if the examination were normal','Adenoma size at least 10 mm is an advanced feature.'),
 ('Six months in every en-bloc complete removal','That early interval is not required solely by a completely removed 14-mm lesion.'),
 ('No further screening ever','Adenoma removal does not erase future neoplasia risk.')],
 'Size is an advanced-adenoma feature',
 '**An adenoma at least 10 mm generally supports three-year surveillance after complete removal.**',
 ['High-grade dysplasia and other findings can also affect classification.', 'The interval assumes adequate bowel preparation and complete examination.'],
 '**Separate biological risk from local residual-lesion risk.**',
 ['Large piecemeal resection has its own early site-check pathway.', 'Pathology and resection quality should be reconciled before scheduling.'],
 [['At least 10-mm adenoma','Three-year framework'],['Large piecemeal lesion','Early residual-site check'],['Inadequate exam','Different interval decision']], [SUR])

# Hereditary neoplasia, obstruction and anorectal disease follow.
q('A 30-mm adenoma is removed piecemeal. Under USMSTF 2020, when is the first surveillance examination generally recommended?',
 'About six months',[
 ('Ten years regardless of resection technique','Large piecemeal removal has substantial residual/recurrent lesion risk.'),
 ('Seven to ten years as for two small tubular adenomas','The resection scenario differs.'),
 ('Only after recurrent bleeding','An asymptomatic residual lesion still matters.')],
 'Piecemeal resection creates a local recurrence concern',
 '**A lesion at least 20 mm removed piecemeal needs an early site check.**',
 ['The USMSTF interval is about six months.', 'Subsequent surveillance depends on the early result and protocol.'],
 '**Document the resection and scar carefully.**',
 ['Use appropriate scar inspection and treatment of residual tissue.', 'Do not assume fragmentation prevents every curative endoscopic outcome, but it changes follow-up.'],
 [['Small complete adenoma','Longer interval'],['At least 20-mm piecemeal removal','Six-month site check'],['Residual tissue','Treat and reassess']], [SUR])
q('A young patient has colorectal and endometrial cancers in the family, with tumor mismatch-repair deficiency but not hundreds of polyps. Which hereditary syndrome is most likely?',
 'Lynch syndrome',[
 ('Classic APC-associated FAP','That typically has a marked adenomatous polyposis phenotype.'),
 ('MUTYH-associated polyposis as the only mismatch-repair syndrome','MUTYH is a base-excision-repair pathway with a different inheritance pattern.'),
 ('Peutz-Jeghers syndrome defined by MMR deficiency','That has a different hamartomatous and pigmentation phenotype.')],
 'A hereditary cancer pattern can exist without florid polyposis',
 '**Lynch involves pathogenic mismatch-repair-related alterations, including selected EPCAM-associated mechanisms.**',
 ['Colorectal and endometrial cancer are important spectrum tumors.', 'Tumor MMR testing is a screening step rather than automatic germline confirmation.'],
 '**Distinguish sporadic MMR loss from inherited disease.**',
 ['MLH1 promoter methylation and selected BRAF testing can help in the appropriate tumor pattern.', 'Genetic counseling and germline assessment follow the full results.'],
 [['Lynch','MMR-associated, often no florid polyposis'],['FAP','APC adenomatous polyposis'],['MUTYH','Recessive base-excision-repair polyposis']], [GEN], 'clinical_scenario')
q('A colorectal tumor loses MLH1 and PMS2 staining. Why is MLH1 promoter methylation or appropriate BRAF testing useful?',
 'It can support a sporadic MLH1-silencing pathway rather than assuming every such tumor is Lynch syndrome',[
 ('It directly proves that every relative carries an APC mutation','That is a different gene and syndrome.'),
 ('It replaces all germline counseling regardless of age and pedigree','Strong clinical context can still warrant further assessment.'),
 ('MMR protein loss always establishes inherited disease without additional work-up','Sporadic methylation is an important alternative.')],
 'Tumor phenotype and germline cause are different levels',
 '**MLH1 silencing is a common sporadic explanation for paired MLH1/PMS2 loss.**',
 ['BRAF findings are interpreted in colorectal tumors and in the correct testing context.', 'Not every MMR-loss pattern uses this same reflex sequence.'],
 '**Complete the hereditary assessment when indicated.**',
 ['Age, family history and unusual results matter.', 'Avoid reassuring or labeling a whole family from one incomplete tumor test.'],
 [['Tumor IHC','Identifies loss pattern'],['Methylation/BRAF','Helps assess sporadic mechanism'],['Germline testing','Answers inherited-risk question']], [GEN])
q('Hundreds of colorectal adenomas develop in a teenager with an autosomal-dominant family history. Which gene is most characteristic?',
 'APC',[
 ('MUTYH as the usual dominant classic syndrome','MUTYH-associated polyposis is generally recessive.'),
 ('MLH1 as the defining cause of hundreds of adenomas','Lynch has a different typical phenotype.'),
 ('STK11 as the standard adenomatous-polyposis gene','STK11 is associated with Peutz-Jeghers hamartomatous polyposis.')],
 'Classic FAP is an inherited adenomatous field defect',
 '**APC pathogenic variants can produce numerous colorectal adenomas and very high untreated cancer risk.**',
 ['Attenuated phenotypes also exist.', 'Upper-GI and extracolonic manifestations matter.'],
 '**Use genetic and surgical prevention planning.**',
 ['Endoscopic burden, age and phenotype guide intervention.', 'Family cascade assessment can identify at-risk relatives early.'],
 [['APC','Classic/attenuated FAP'],['MUTYH','Usually recessive polyposis'],['STK11','Hamartomatous Peutz-Jeghers syndrome']], [GEN], 'clinical_scenario')
q('Which inheritance pattern is characteristic of MUTYH-associated polyposis?',
 'Autosomal recessive disease from biallelic pathogenic variants',[
 ('Obligatory X-linked recessive inheritance','MUTYH is not an X-linked syndrome.'),
 ('Autosomal dominant APC disease by definition','APC and MUTYH are different pathways.'),
 ('Mitochondrial maternal inheritance','That is not the characteristic inheritance.')],
 'A polyposis pedigree may lack vertical transmission',
 '**Affected siblings can occur with clinically unaffected parents in recessive disease.**',
 ['The adenoma burden can overlap attenuated FAP.', 'A single variant has a different risk interpretation from biallelic disease.'],
 '**Counsel using the actual genotype.**',
 ['Sibling and reproductive implications differ from a dominant syndrome.', 'Surveillance depends on the confirmed risk category and phenotype.'],
 [['Biallelic MUTYH','Recessive polyposis'],['APC','Dominant polyposis'],['Family assessment','Genotype-informed counseling']], [GEN])
q('A flat proximal colonic lesion has a mucus cap and serrated crypt architecture with basal distortion. Which precursor is most likely?',
 'Sessile serrated lesion',[
 ('A conventional pedunculated tubular adenoma as the best morphology match','The flat mucus-capped proximal and serrated crypt pattern points elsewhere.'),
 ('An inflammatory pseudopolyp as the defining molecular precursor','That is a different lesion type.'),
 ('A juvenile hamartomatous polyp as the typical serrated pattern','It has different architecture.')],
 'Not all colorectal precursors follow the conventional adenoma pathway',
 '**Sessile serrated lesions can be subtle and proximal.**',
 ['A mucus cap can make detection difficult.', 'The serrated pathway can involve BRAF and epigenetic changes.'],
 '**Complete detection and removal matter.**',
 ['Size, dysplasia, number and resection quality guide surveillance.', 'Do not classify every serrated lesion as a harmless distal hyperplastic polyp.'],
 [['Sessile serrated lesion','Flat, often proximal, distorted serrated crypts'],['Conventional adenoma','Different dysplastic architecture'],['Follow-up','Lesion-specific risk factors']], [SUR,GEN])
q('An older patient has iron-deficiency anemia, fatigue and occult blood loss without early obstructive symptoms. Which colonic location is a classic concern?',
 'Right colon',[
 ('The rectum as the only site capable of occult bleeding','Any lesion can bleed, but this pattern is classically associated with proximal cancer.'),
 ('No colorectal lesion because obstruction is absent','Proximal tumors can grow before causing obstruction.'),
 ('Only uncomplicated hemorrhoids regardless of age','Iron deficiency requires appropriate investigation rather than attribution.')],
 'Presentation varies with anatomy',
 '**A wider proximal lumen can permit tumor growth before obstruction.**',
 ['Chronic occult loss can dominate the presentation.', 'Left-sided lesions more often cause altered bowel habit or narrowing, though patterns overlap.'],
 '**Investigate iron deficiency rather than relying on stereotyped symptoms.**',
 ['Complete appropriate gastrointestinal evaluation.', 'A negative symptom history does not replace cancer assessment.'],
 [['Right-sided cancer','Occult loss/anemia often prominent'],['Left-sided lesion','Narrowing symptoms can be earlier'],['Iron deficiency','Needs a cause']], [ref('NCI PDQ: Colon Cancer Treatment','https://www.cancer.gov/types/colorectal/hp/colon-treatment-pdq')], 'clinical_scenario')
q('A rectal adenocarcinoma has been biopsied and distant staging is being arranged. Which study is central to local pelvic staging and circumferential resection-margin assessment?',
 'High-resolution pelvic MRI',[
 ('A routine chest radiograph as the complete local staging test','It does not map the rectal tumor and mesorectal fascia.'),
 ('A stool FIT as a T-stage measurement','FIT is not an anatomical staging test.'),
 ('A normal serum CEA as proof of early local stage','CEA cannot define local extent.')],
 'Rectal treatment depends on local anatomical risk',
 '**MRI defines tumor relation to the mesorectal fascia and other pelvic structures.**',
 ['Depth, nodes and extramural vascular features influence planning.', 'Selected early lesions may also benefit from endorectal ultrasound assessment.'],
 '**Separate local and distant staging.**',
 ['CT-based systemic staging answers a different question.', 'Use a multidisciplinary strategy rather than treating the rectum like every colon segment.'],
 [['Pelvic MRI','Local rectal anatomical staging'],['Systemic CT','Distant spread assessment'],['CEA','Adjunct marker, not anatomical stage']], [ref('NCI PDQ: Rectal Cancer Treatment','https://www.cancer.gov/types/colorectal/hp/rectal-treatment-pdq')], 'clinical_scenario')
q('A metastatic colorectal cancer has an activating RAS mutation. What does this generally imply for cetuximab-based EGFR blockade?',
 'It predicts lack of benefit from standard anti-EGFR treatment in that molecular context',[
 ('It guarantees exceptional anti-EGFR response','Constitutive downstream signaling is a resistance mechanism.'),
 ('It is the same as dMMR and proves identical immunotherapy sensitivity','RAS and mismatch repair are different biomarkers.'),
 ('It eliminates the need for any further treatment selection','Other effective systemic strategies may remain.')],
 'A downstream driver can bypass receptor blockade',
 '**Activating KRAS or NRAS can maintain signaling despite EGFR inhibition.**',
 ['Extended RAS testing is part of treatment selection.', 'Tumor sidedness, BRAF and other markers also influence care.'],
 '**Do not use one biomarker as the entire oncology plan.**',
 ['Choose an appropriate regimen through current oncological guidance.', 'New mutation-specific combinations have their own evidence and do not erase the standard resistance principle.'],
 [['RAS wild type','One prerequisite for selected anti-EGFR use'],['RAS activated','Standard EGFR blockade resistance'],['Other markers','Add treatment-selection information']], [ref('NCI PDQ: Colon Cancer Treatment, molecular therapy selection','https://www.cancer.gov/types/colorectal/hp/colon-treatment-pdq')])
q('A stable patient has sigmoid volvulus without peritonitis, perforation or ischemic bowel signs. What is the usual initial intervention?',
 'Endoscopic detorsion and decompression, followed by definitive recurrence-prevention planning',[
 ('Blind oral cathartics as definitive treatment of a closed loop','This does not safely relieve the torsion.'),
 ('Observation alone until the bowel becomes ischemic','Delay can be dangerous.'),
 ('Treat every uncomplicated case exactly like cecal volvulus without considering endoscopic decompression','The two locations have different usual initial strategies.')],
 'A viable sigmoid volvulus can often be decompressed endoscopically',
 '**Confirm there is no clinical indication for immediate surgery.**',
 ['Assess mucosal viability during decompression.', 'Recurrence is common without a definitive plan.'],
 '**Decompression is not always the final treatment.**',
 ['Elective or same-admission resection assessment depends on the patient.', 'Ischemia, perforation or failed decompression requires surgery.'],
 [['Viable uncomplicated sigmoid volvulus','Endoscopic decompression'],['Ischemia/perforation','Emergency surgery'],['After success','Recurrence-prevention planning']], [VOL], 'clinical_scenario')
q('A patient has cecal volvulus causing obstruction. Which treatment direction is generally preferred?',
 'Surgical management rather than routine colonoscopic detorsion',[
 ('Use sigmoid-volvulus endoscopic success assumptions without qualification','Cecal volvulus has a different anatomy and lower reliability of endoscopic reduction.'),
 ('High-dose antidiarrheals as definitive treatment','They do not correct torsion.'),
 ('Wait indefinitely because the cecum cannot become ischemic','Closed-loop ischemia is a major concern.')],
 'Location changes the volvulus pathway',
 '**Cecal volvulus usually requires an operation.**',
 ['Bowel viability and patient state determine the surgical procedure.', 'Perforation or ischemia increases urgency.'],
 '**Do not treat all colonic dilation as pseudo-obstruction.**',
 ['A mechanical twist is different from Ogilvie syndrome.', 'Imaging helps define the mechanism before a pharmacological decompression attempt.'],
 [['Sigmoid volvulus','Often initial endoscopic reduction if viable'],['Cecal volvulus','Usually surgical pathway'],['Pseudo-obstruction','No mechanical twist']], [VOL], 'clinical_scenario')
q('A hospitalized patient has acute colonic pseudo-obstruction without mechanical obstruction or ischemia and has failed appropriate supportive measures. There is no contraindication. Which monitored treatment is appropriate?',
 'Neostigmine with cardiac monitoring and resuscitation readiness',[
 ('Neostigmine without excluding mechanical obstruction','That is an essential safety distinction.'),
 ('Loperamide as the principal decompressive drug','It can worsen hypomotility.'),
 ('Oral barium as a treatment to force the colon open','It is not a therapeutic decompression strategy.')],
 'Pseudo-obstruction is a motor failure rather than a mechanical blockage',
 '**Acetylcholinesterase inhibition can stimulate colonic motility.**',
 ['Bradycardia and other contraindications require careful assessment.', 'Endoscopic decompression is an option when drug treatment is unsuitable or unsuccessful.'],
 '**Continue correcting precipitating factors.**',
 ['Review opioids, electrolytes, mobility and acute illness.', 'Peritonitis, ischemia or perforation changes the need to emergency surgery.'],
 [['Supportive care fails','Consider monitored neostigmine'],['Contraindication/failure','Endoscopic decompression assessment'],['Complication','Surgical pathway']], [VOL], 'clinical_scenario')
q('A patient has persistent bleeding and prolapsing grade II internal hemorrhoids despite fiber and bowel-habit treatment. Which office procedure is commonly appropriate?',
 'Rubber band ligation',[
 ('Banding a painful thrombosed external hemorrhoid as the same procedure','External thrombosis is a different anatomical and treatment problem.'),
 ('Routine colectomy','This is not indicated for internal hemorrhoids.'),
 ('Permanent topical steroid use as definitive correction of prolapse','Long-term topical steroids do not correct the prolapse and can damage local skin.')],
 'Internal hemorrhoid anatomy permits office treatment',
 '**Band ligation can treat selected bleeding or prolapsing internal hemorrhoids.**',
 ['Assess grade, symptoms and contraindications.', 'Place treatment according to appropriate anatomy to avoid severe pain.'],
 '**Do not attribute all bleeding to hemorrhoids without assessment.**',
 ['Age, anemia, change in habit and screening status can require colon evaluation.', 'Continue fiber and reduced straining after the procedure.'],
 [['Internal grade II disease','Often office-treatment suitable'],['External thrombosis','Different pathway'],['Bleeding evaluation','Consider other causes']], [ref('AGA: Diagnosis and Treatment of Hemorrhoids','https://gastro.org/clinical-guidance/diagnosis-and-treatment-of-hemorrhoids/')], 'clinical_scenario')
q('A patient has a typical chronic posterior anal fissure with painful defecation and sphincter hypertonia. Which topical treatment can promote healing with fewer headaches than nitrates?',
 'A topical calcium channel blocker such as diltiazem',[
 ('An oral stimulant laxative as a direct sphincter-relaxing substitute','Stool management helps but does not reproduce the topical smooth-muscle action.'),
 ('A prolonged high-potency topical steroid as the primary fissure-healing treatment','That is not the recommended chemical sphincter-relaxation strategy.'),
 ('An antidiarrheal to harden stools in every patient','Hard stools can worsen injury.')],
 'Reduce sphincter pressure and stool trauma',
 '**Topical CCBs have efficacy comparable to nitrates with a favorable headache profile.**',
 ['Fiber, hydration and stool-softening strategies support healing.', 'Botulinum toxin or surgery may be considered after failure in an appropriate patient.'],
 '**Atypical fissures need broader investigation.**',
 ['Lateral or multiple lesions can suggest Crohn, infection or neoplasia.', 'Sphincterotomy decisions require continence-risk assessment.'],
 [['Typical chronic fissure','Topical relaxation plus bowel care'],['CCB versus nitrate','Similar efficacy, fewer headaches'],['Atypical lesion','Investigate another cause']], [ref('ASCRS 2023 Anal Fissure Guideline','https://fascrs.org/ascrs/media/files/Education/2023-Anal-Fissures-CPG.pdf')], 'clinical_scenario')

if __name__=='__main__':
    finalize('GI & pancreas',5,'Colorectal Disorders','gi-colorectal',rows,28)
