from create_luminal_gi_notes import *
from create_pancreas_colorectal_notes import PAN,CYST,PNET
BLEED=('ACG lower GI bleeding guideline, 2023','https://doi.org/10.14309/ajg.0000000000002130')
UGIB=('ACG upper GI and ulcer bleeding guideline, 2021','https://doi.org/10.14309/ajg.0000000000001245')
NUT=('ESPEN chronic intestinal failure guideline, 2023','https://www.espen.org/files/ESPEN-Guidelines/ESPEN_guideline_on_chronic_intestinal_failure_in_adults.pdf')
GASTRO=('AGA gastroparesis guideline, 2025','https://gastro.org/clinical-guidance/clinical-guidance-on-the-management-of-gastroparesis/')

def bleeding():
 write('GI & pancreas','GI Bleeding Endoscopy',[
 S('Initial assessment: severity before localization',U('''Assess airway risk, circulation, mental state and ongoing blood loss; obtain IV access, CBC/coagulation profile and cross-match.
 Resuscitate before endoscopy. A normal initial hemoglobin does not exclude major acute hemorrhage.
 Restrictive transfusion is appropriate for many stable patients, often Hb ~7 g/dL; active shock, cardiovascular ischemia and other factors change the threshold.
 Hematochezia with shock can be brisk upper GI bleeding. Melena can occasionally arise beyond the stomach/duodenum.''')),
 S('Source-specific management',T('Source / finding|Management principle','''Suspected nonvariceal upper bleeding|Risk stratification; endoscopy generally within 24 hours after resuscitation
 Active ulcer bleeding / visible vessel|Endoscopic hemostasis; epinephrine should not be the sole definitive modality
 Clean-based ulcer|No routine endoscopic hemostasis; treat cause
 Suspected variceal bleeding|Start vasoactive therapy and antibiotic prophylaxis promptly; urgent endoscopy after stabilization
 Unstable ongoing lower GI bleeding|CT angiography to localize; selected embolization
 Stable lower GI bleeding|Prepared colonoscopy when appropriate; urgent <24-hour colonoscopy is not required for every patient
 Suspected small-bowel bleeding|After appropriate upper/lower evaluation, capsule endoscopy or enteroscopy/imaging according to stability and obstruction risk''')),
 S('After hemostasis',U('''High-risk ulcer bleeding: high-dose PPI after endoscopic hemostasis, then the appropriate oral course.
 Test/treat H. pylori and confirm eradication; review NSAIDs and antithrombotics.
 Recurrent ulcer bleeding usually prompts repeat endoscopic treatment; uncontrolled bleeding may need embolization or surgery.
 Aspirin used for secondary cardiovascular prevention should not be withheld unnecessarily; interruption/resumption of anticoagulants or DAPT requires bleeding–thrombosis assessment.
 Do not apply a routine INR correction target to every cirrhotic bleed; INR does not fully measure hemostasis in cirrhosis.''')),
 S('Endoscopy selection and procedure pitfalls',T('Question|Preferred direction','''Obstructive jaundice needing drainage|ERCP is therapeutic; MRCP/EUS can establish anatomy without diagnostic ERCP risk
 Subepithelial lesion / pancreatic lesion|EUS adds wall-layer or tissue assessment
 Suspected perforation|Urgent imaging/surgical assessment; routine insufflation endoscopy can be inappropriate
 Capsule with suspected stricture|Assess retention risk first
 Iron-deficiency anemia|Investigate cause; bidirectional endoscopy in appropriate risk groups; iron replacement does not replace indicated investigation'''))],[UGIB,BLEED,('AGA iron-deficiency anemia evaluation guideline','https://gastro.org/clinical-guidance/gastrointestinal-evaluation-of-iron-deficiency-anemia/')])

def oncology():
 write('GI & pancreas','GI Oncology Hereditary Cancers',[
 S('Tumor biology: classify before treatment',T('Tumor|Important biomarker / distinction','''Colorectal adenocarcinoma|MMR/MSI; metastatic molecular testing including RAS/BRAF and other actionable alterations as indicated
 Gastric/GEJ adenocarcinoma|HER2, MMR/MSI, PD-L1 and other current treatment-relevant targets
 GIST|KIT/DOG1 support diagnosis; KIT/PDGFRA variant predicts drug sensitivity
 Pancreatic cancer|Histology, stage and appropriate germline/somatic assessment
 Neuroendocrine neoplasm|Site, differentiation, grade, function and somatostatin-receptor expression''')+U('''A tumor marker is not a substitute for tissue diagnosis. CEA and CA19-9 can be normal despite cancer or elevated for other reasons.
 Stage determines local versus systemic strategy; resectability includes vascular anatomy and fitness, not diameter alone.
 MMR deficiency can predict immunotherapy benefit in defined settings. It is not always hereditary.''')),
 S('Hereditary syndromes: compare together',T('Syndrome|Gene / pathway|Cancer clues','''Lynch|MLH1, MSH2, MSH6, PMS2; selected EPCAM deletions|Colorectal/endometrial and other cancers; usually no profuse polyposis
 FAP|APC; dominant|Many adenomas, duodenal risk and extracolonic manifestations
 MUTYH-associated polyposis|Biallelic MUTYH; recessive|Adenomatous polyposis; single heterozygous finding is not equivalent
 Peutz–Jeghers|STK11|Hamartomatous polyps, mucocutaneous pigmentation, broad cancer risk
 Hereditary diffuse gastric cancer|CDH1; selected CTNNA1|Diffuse gastric and lobular breast cancer pattern
 Juvenile polyposis|SMAD4/BMPR1A|Hamartomatous juvenile polyps; colorectal/gastric risk''')),
 S('Results that require careful interpretation',U('''MLH1/PMS2 loss: assess sporadic MLH1 silencing and appropriate hereditary evaluation. Colorectal BRAF interpretation should not be transferred indiscriminately to endometrial cancer.
 A tumor-only pathogenic variant can be somatic or germline; confirm inherited risk with appropriate counseling/testing.
 A variant of uncertain significance is not an indication for irreversible preventive surgery by itself.
 PDGFRA D842V GIST is characteristically imatinib resistant; exact variants matter.
 Surveillance intervals and risk-reducing operations are syndrome- and phenotype-specific; do not assign one schedule to all hereditary GI cancers.'''))],[('NCI colorectal genetics professional summary','https://www.cancer.gov/types/colorectal/hp/colorectal-genetics-pdq'),('NCI gastric genetics','https://www.cancer.gov/types/stomach/hp/gastric-genetics-pdq'),('NCI GIST professional summary','https://www.cancer.gov/types/soft-tissue-sarcoma/hp/gist-treatment-pdq')])

def functional():
 write('GI & pancreas','Functional GI Motility',[
 S('Positive diagnosis, with targeted exclusion',T('Condition|Core distinction','''IBS|Recurrent abdominal pain related to defecation and/or altered stool frequency/form; subtype by stool pattern
 Functional dyspepsia|Postprandial fullness/early satiation or epigastric pain/burning without explanatory structural disease
 Functional constipation|Difficult/infrequent defecation without sufficient IBS pain pattern
 Defecatory disorder|Impaired evacuation due to pelvic-floor/coordination dysfunction
 Gastroparesis|Symptoms + objectively delayed gastric emptying without mechanical obstruction''')+U('''Bleeding, anemia, weight loss, nocturnal progressive symptoms, family cancer history or relevant age/risk prompts investigation.
 Use selective celiac/inflammation testing in diarrhea presentations. Functional disease can coexist with organic disease; avoid labeling every recurrent symptom an inflammatory flare.''')),
 S('Treatment grouped by symptom and mechanism',T('Problem|Useful options|Pitfall','''IBS constipation|Soluble fiber, appropriate osmotic laxative; selected secretagogues/other approved agents|Stool frequency improvement does not always relieve pain
 IBS diarrhea|Dietary review, selected antidiarrheal and disease-specific options|Loperamide improves diarrhea more reliably than global pain symptoms
 IBS pain / gut–brain symptoms|Dietitian-led limited low-FODMAP trial with reintroduction, selected neuromodulator and psychological therapy|Avoid indefinite highly restrictive diets
 Defecatory disorder|Anorectal testing when indicated; biofeedback|Repeated laxative escalation alone may fail
 Gastroparesis|Small-particle/modified meals, nutrition support, glycemic review and selected prokinetic/antiemetic|Exclude obstruction and drug-induced delay first''')),
 S('Testing and drug safety',U('''Suspected gastroparesis: use a properly performed four-hour gastric-emptying study rather than a short study; account for medicines and hyperglycemia that alter emptying.
 Metoclopramide: neurological adverse effects/tardive dyskinesia; use within appropriate duration and risk guidance. Domperidone access and cardiac precautions vary by country.
 Opioids can worsen gastric and intestinal motility; they are not routine treatment for functional abdominal pain.
 Refractory symptoms do not automatically justify pyloric intervention; establish the physiological disorder and assess evidence-based options.
 A breath-test result alone does not establish that all symptoms are due to small-intestinal bacterial overgrowth.'''))],[GASTRO,('ACG IBS guideline, 2021','https://doi.org/10.14309/ajg.0000000000001036')])

def infections():
 write('GI & pancreas','GI Infections Tropical',[
 S('Syndrome-based stool evaluation',T('Pattern|Important possibilities|First priorities','''Acute watery diarrhea|Viral disease, toxin-mediated illness, cholera and other enteric pathogens|Oral/IV rehydration by severity; assess outbreak/travel context
 Bloody/inflammatory diarrhea|Shigella, Campylobacter, invasive bacterial infection, amoebiasis, IBD|Targeted stool tests; assess systemic toxicity
 Persistent watery diarrhea|Giardia, Cryptosporidium/Cyclospora and noninfectious causes|Exposure, immune status and targeted antigen/PCR testing
 Antibiotic-associated diarrhea|C. difficile or other causes|Test appropriate symptomatic patients; positive nucleic acid test can reflect colonization''')),
 S('Treatments with an important second step',T('Infection|Treatment principle / trap','''Invasive amoebiasis|Tissue-active nitroimidazole followed by a luminal amoebicide; metronidazole alone does not clear all luminal infection
 Giardia|Appropriate antiprotozoal therapy; assess reinfection and alternative diagnosis if persistent
 Strongyloides|Ivermectin first-line in suitable patients; corticosteroids can precipitate fatal hyperinfection
 C. difficile|Fidaxomicin preferred in many initial/recurrent settings; oral vancomycin acceptable alternative; fulminant disease follows a separate regimen
 Intestinal tuberculosis|Microbiological/histological evaluation and multidrug TB treatment; do not diagnose from IGRA alone
 CMV colitis|Consider in immunocompromised or refractory severe colitis; tissue assessment is often important''')+U('''Strongyloides hyperinfection: urgent treatment, search for disseminated infection and reduce immunosuppression when possible; absence of eosinophilia does not exclude it.
 Assess Loa loa risk before ivermectin when epidemiologically relevant.
 Avoid reflex corticosteroids for presumed IBD before excluding important infections in a compatible exposure setting.''')),
 S('Antibiotic and diagnostic pitfalls',U('''Suspected Shiga-toxin-producing E. coli: avoid unnecessary antibiotics and antimotility drugs because of HUS concern; provide careful supportive management.
 Stool microscopy may not reliably distinguish pathogenic E. histolytica from nonpathogenic lookalikes; use specific testing when available.
 Do not perform C. difficile testing of cure in an asymptomatic patient. Recurrent symptoms need reassessment rather than interpretation of persistent PCR positivity alone.
 Severe dehydration, shock, peritonitis, toxic megacolon or neurological/renal complications require urgent escalation.
 Oral rehydration works through preserved sodium–glucose cotransport; plain water alone may not replace substantial salt loss.'''))],[('CDC Strongyloides clinical care','https://www.cdc.gov/strongyloides/hcp/clinical-care/index.html'),('IDSA/SHEA C. difficile guideline, 2021','https://www.idsociety.org/practice-guideline/clostridioides-difficile-2021-focused-update/'),('Arizona public-health amebiasis guidance','https://www.azdhs.gov/documents/preparedness/epidemiology-disease-control/investigation-manual/disease-protocols/amebiasis.pdf')])

def nutrition():
 write('GI & pancreas','Nutrition Intestinal Failure',[
 S('Choose the route and identify the deficit',T('Situation|Nutrition strategy','''Functional GI tract, inadequate intake|Oral diet/supplementation first; enteral tube feeding when required
 Intestinal failure|IV fluid/nutrient support needed to maintain health because absorption is insufficient
 Short bowel|Requirements depend on remaining anatomy, ileum, colon continuity and adaptation
 High-output stoma/fistula|Replace water, sodium and magnesium; assess obstruction, sepsis, medicines and intake''')+U('''Screen for malnutrition with weight trajectory, intake, muscle/function and disease burden; albumin alone is not a nutrition diagnosis.
 Enteral feeding is preferred when the gut can absorb sufficiently; parenteral nutrition is not inherently wrong when enteral support cannot meet requirements.
 Estimate needs and monitor delivery, tolerance, fluid balance and relevant micronutrients; avoid both underfeeding and overfeeding.''')),
 S('Refeeding syndrome',T('Feature|Action','''Risk|Prolonged poor intake, substantial weight loss, low BMI, alcohol use or depleted electrolytes
 Mechanism|Insulin-mediated intracellular electrolyte shifts after feeding
 Typical abnormalities|Hypophosphatemia, hypokalemia, hypomagnesemia; fluid retention; thiamine deficiency
 Prevention|Thiamine before/with carbohydrate, correct deficits, cautious initial delivery and monitored advancement
 Monitoring|Electrolytes, fluid status, cardiac/respiratory function and glucose''')+U('''A normal prefeeding phosphate does not exclude total-body depletion. Severe electrolyte or organ complications require urgent adjustment of feeding and replacement.
 IV dextrose can trigger refeeding physiology; the risk is not limited to tube or parenteral nutrition.''')),
 S('Short bowel and parenteral nutrition',U('''High-output jejunostomy: use a sodium-containing glucose–saline rehydration plan; unrestricted hypotonic fluid can worsen sodium losses. Selected antimotility and antisecretory drugs reduce output.
 Colon continuity improves fluid/energy salvage but can increase oxalate-stone and D-lactic-acidosis risks in appropriate anatomy.
 Ileal loss causes B12 and bile-acid problems; excessive bile-acid sequestration can worsen fat malabsorption in extensive resection.
 Parenteral nutrition complications: catheter infection/thrombosis, electrolyte/glucose disturbance, micronutrient deficiency/toxicity and intestinal-failure-associated liver disease.
 Long-term care requires intestinal rehabilitation, line-care training, oral/enteral adaptation and selected specialist therapies or transplantation assessment.'''))],[NUT])

def mixed_reviews():
 write('GI & pancreas','Mixed GI Structured Review',[
 S('Diarrhea and malabsorption: grouped decisions',T('Clue|Think of|Next distinction','''Bloody diarrhea|IBD, infection, ischemia|Severity, stool testing and appropriate endoscopic assessment
 Steatorrhea|Mucosal disease, pancreatic insufficiency, bile-acid depletion|Nutrition, celiac testing, pancreatic/ileal assessment
 Secretory watery diarrhea|Bile-acid diarrhea, medicines, microscopic colitis, selected NETs|Nocturnal/persistent output; targeted testing rather than indiscriminate hormone panels
 Normal-looking colon with chronic watery diarrhea|Microscopic colitis|Biopsy is required
 Short bowel + episodic neurological symptoms|D-lactate|Routine L-lactate assay can be unrevealing''')+P('Use the dedicated Malabsorption, IBD, Infection and Nutrition modules for treatment details.')),
 S('Pain, jaundice and pancreatic disease',T('Pattern|Priority','''Epigastric pain with lipase ≥3× upper limit|Assess acute pancreatitis criteria, organ failure and cause
 Fever + jaundice + biliary obstruction|Antibiotics and timely drainage for cholangitis
 Painless jaundice / weight loss|Assess malignant obstruction; CA19-9 alone is not diagnostic
 Pancreatic cyst|Classify cyst type and high-risk features; do not drain every cyst as a pseudocyst
 Portal-hypertensive bleeding|Resuscitation, vasoactive treatment, antibiotics and endoscopic hemostasis''')),
 S('Tests that are often overinterpreted',U('''Normal AFP does not exclude HCC; elevated AFP does not replace the appropriate imaging/tissue pathway.
 Positive celiac serology, villous atrophy and response to diet are complementary; none should be interpreted without gluten exposure and alternative causes.
 A high gastrin level can reflect PPI use or achlorhydria, not only gastrinoma.
 Fecal calprotectin identifies inflammation, not its exact cause. A normal CT does not exclude every mucosal disorder.
 A pancreatic fluid collection’s contents, maturity and symptoms determine treatment; diameter alone does not.'''))],[IBD,CEL,PAN,HP])
 write('GI & pancreas','Mixed GI Expanded Review',[
 S('Emergency priorities',T('Presentation|Do first|Avoid','''Shock with GI bleeding|Resuscitate and localize by stability/source|Waiting for hemoglobin to fall before treating shock
 Severe colitis with dilation|Assess toxic megacolon and involve surgery|Antimotility drugs and unnecessary full colonoscopy
 Suspected cholangitis|Antibiotics, severity assessment and biliary drainage|Assuming all gallstone pancreatitis requires identical timing of ERCP
 Infected pancreatic necrosis|Antibiotics and multidisciplinary step-up source control|Routine immediate open necrosectomy in every stable patient
 Food obstruction with pooling secretions|Urgent endoscopic assessment|Deferring for elective manometry''')),
 S('Match the treatment to the mechanism',T('Mechanism|Treatment distinction','''Achalasia|Reduce EGJ resistance; type III often needs a longer myotomy
 Eosinophilic esophagitis|Anti-inflammatory treatment plus dilation when needed
 H. pylori|Resistance-aware eradication and test of cure
 Invasive amoebiasis|Tissue treatment followed by luminal eradication
 Pancreatic exocrine insufficiency|Enzymes with meals and nutritional replacement
 Defecatory disorder|Biofeedback rather than laxative escalation alone''')),
 S('Long-term review checklist',U('''After a GI bleed: eradicate H. pylori, review NSAIDs/antithrombotics and complete the source work-up.
 After an IBD flare: establish steroid-free maintenance and objective assessment; do not maintain remission with repeated steroid courses.
 After pancreatitis: address gallstones, alcohol, triglycerides and nutrition; investigate unexplained or recurrent disease.
 In hereditary cancer: confirm the syndrome and variant before family testing or irreversible prevention.
 In intestinal failure: monitor line complications, fluid/electrolytes, micronutrients and liver disease.
 These mixed collections consolidate the same clinical groups; they do not introduce Level 2 modules.'''))],[ACH,EOE,HP,IBD,PAN,NUT])

if __name__=='__main__':bleeding();oncology();functional();infections();nutrition();mixed_reviews()
