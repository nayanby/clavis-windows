from create_luminal_gi_notes import *
PAN=('IAP acute pancreatitis guideline, 2025','https://doi.org/10.1016/j.pan.2025.04.020')
CYST=('Kyoto IPMN guidelines, 2024','https://www.ahpba.org/wp-content/uploads/2025/02/Kyoto-IPMN-Guidelines-2024.pdf')
PNET=('NCI pancreatic neuroendocrine tumors professional summary','https://www.cancer.gov/types/pancreatic/hp/pnet-treatment-pdq')

def colorectal():
 write('GI & pancreas','Colorectal Disorders',[
 S('Bleeding and altered bowel habit',T('Presentation|Important causes / distinction','''Painless large-volume hematochezia|Diverticular bleeding, angioectasia; severe upper GI bleeding can also present this way
 Painful bloody diarrhea|Ischemic/infectious colitis or IBD; assess perfusion and systemic illness
 Iron-deficiency anemia or persistent bowel change|Colorectal malignancy must be excluded; right-sided cancer need not obstruct
 Watery chronic diarrhea with normal-looking colon|Microscopic colitis requires biopsies
 Anorectal bleeding|Hemorrhoids/fissure can coexist with proximal disease; do not stop evaluation solely because hemorrhoids are seen''')),
 S('Diverticular disease and emergencies',T('Condition|Key management','''Uncomplicated diverticulitis|CT when needed to confirm/assess severity; antibiotics are selective in suitable immunocompetent mild cases, not automatically required for everyone
 Complicated diverticulitis|Abscess, perforation, obstruction or fistula: antibiotics and appropriate drainage/surgical assessment
 Sigmoid volvulus|Endoscopic detorsion in appropriate viable bowel; definitive recurrence-prevention plan
 Cecal volvulus|Usually surgical treatment
 Acute colonic pseudo-obstruction|Exclude mechanical block, correct causes; selected neostigmine/decompression with contraindication review
 Ischemic colitis|Support perfusion and assess severity; peritonitis/gangrene requires surgery''')+U('''Avoid colonoscopy during acute suspected perforation or severe diverticular inflammation. Interval assessment depends on recovery, prior colonoscopy and cancer risk.
 Toxic megacolon is systemic toxicity with colonic dilation, not simply a large colon. Avoid precipitating antimotility drugs and obtain urgent specialist review.''')),
 S('Polyps and colorectal cancer',T('Lesion|Cancer relevance','''Conventional adenoma|Risk increases with size, number, villous features and high-grade dysplasia
 Sessile serrated lesion|Often proximal/subtle; important serrated pathway precursor
 Small distal hyperplastic polyp|Different risk from large/proximal serrated lesions
 Lynch syndrome|Mismatch-repair pathway; colorectal/endometrial spectrum, often without profuse polyposis
 FAP|APC-associated adenomatous polyposis; dominant inheritance
 MUTYH-associated polyposis|Usually biallelic/recessive''')+U('''Post-polypectomy surveillance depends on complete removal, histology, size, number, bowel preparation and guideline jurisdiction.
 New colorectal cancer: assess MMR/MSI for hereditary and treatment implications. MSI-high does not automatically mean Lynch syndrome.
 Obstruction, perforation and significant bleeding require urgent management before an elective staging sequence.'''))],[IBD,('NICE colorectal cancer guideline','https://www.nice.org.uk/guidance/ng151/chapter/Recommendations'),('NCI colorectal genetics','https://www.cancer.gov/types/colorectal/hp/colorectal-genetics-pdq')])

def pancreatitis():
 write('GI & pancreas','Acute Chronic Pancreatitis',[
 S('Acute pancreatitis: diagnosis and severity',T('Decision|Criteria / distinction','''Diagnosis|Any 2: typical pain; lipase/amylase ≥3× upper limit; characteristic imaging
 Mild|No organ failure or local/systemic complication
 Moderately severe|Transient organ failure <48 h and/or local/systemic complication without persistent organ failure
 Severe|Persistent organ failure >48 h
 Early collections|Acute peripancreatic fluid collection or acute necrotic collection
 Mature collections, usually after ~4 weeks|Pseudocyst after interstitial disease; walled-off necrosis contains necrotic material''')+U('''Gallstones and alcohol are common causes; assess triglycerides, calcium, medicines and occult obstruction when indicated.
 Lipase magnitude does not grade severity. Routine early CT is unnecessary in an otherwise clear diagnosis; image for uncertainty or failure to improve/complications.''')),
 S('Initial treatment and biliary intervention',U('''Use reassessed, moderate fluid resuscitation, commonly balanced crystalloid; avoid indiscriminate aggressive loading, especially with cardiac/renal disease.
 Analgesia, organ support and early oral feeding as tolerated. If oral feeding is not feasible, enteral feeding is preferred over routine parenteral nutrition; NG and NJ routes have roles.
 No prophylactic antibiotics for sterile necrosis. Treat proven/suspected infection and obtain source control when needed.
 Urgent ERCP for associated cholangitis; not routine early ERCP for every gallstone pancreatitis without cholangitis or persistent obstruction.
 Mild gallstone pancreatitis: cholecystectomy during the same admission when appropriate; severe/complicated disease may require delay.''')),
 S('Necrosis and local complications',T('Problem|Preferred principle','''Infected necrosis|Antibiotics and multidisciplinary step-up drainage/debridement; delay intervention until organized when clinically tolerable
 Asymptomatic sterile collection|Size alone is not a drainage indication
 Symptomatic mature collection|Drain for infection, pain, obstruction or other appropriate indication
 Pseudoaneurysm bleeding|Urgent vascular imaging/interventional control
 Splenic vein thrombosis|Can cause isolated gastric varices; anticoagulation decisions are individualized''')),
 S('Chronic pancreatitis',U('''Chronic inflammation/fibrosis causes pain, ductal changes, exocrine insufficiency and pancreatogenic diabetes.
 Pancreatic enzymes treat exocrine insufficiency and malnutrition; take with meals/snacks. They are not a universal analgesic treatment.
 Stop alcohol/smoking, assess nutrition and fat-soluble vitamins; use structured pain care and selected endoscopic/surgical treatment for obstruction or refractory pain.
 Type 3c diabetes may combine insulin deficiency with impaired glucagon response, increasing hypoglycemia risk.
 A new mass, weight loss or changing pain requires reassessment for cancer rather than attribution to chronic pancreatitis alone.'''))],[PAN,('NICE pancreatitis guideline','https://www.nice.org.uk/guidance/ng104/chapter/recommendations')])

def pancreas():
 write('GI & pancreas','Pancreas',[
 S('Autoimmune pancreatitis: compare both types',T('Feature|Type 1|Type 2','''Disease association|IgG4-related systemic disease|Duct-centric pancreatitis; association with IBD
 Histology|Lymphoplasmacytic sclerosing pattern|Granulocytic epithelial lesions
 Serum IgG4|May be elevated; normal does not exclude|Often normal
 Other organs / relapse|Biliary, salivary, renal and other lesions; relapse more common|Systemic IgG4 features uncommon; relapse less common''')+U('''Imaging, tissue, serology and other-organ findings establish the diagnosis together.
 Do not use an empirical steroid trial to bypass assessment of a potentially malignant pancreatic mass. IgG4 elevation alone is not diagnostic.''')),
 S('Pancreatic cysts: classify before surveillance',T('Lesion|Clue|Risk / action','''Pseudocyst|Previous pancreatitis; no epithelial lining|Do not assume every cyst in a patient with pain is a pseudocyst
 Serous cystic neoplasm|Microcystic pattern, possible central scar|Usually low malignant potential; intervene for appropriate symptoms/uncertainty
 Mucinous cystic neoplasm|Usually body/tail in women; no typical duct communication|Premalignant; risk assessment by size, features and surgical fitness
 IPMN|Main/branch duct involvement; mucinous ductal lesion|Main-duct disease and high-risk features increase concern
 Solid-pseudopapillary neoplasm|Often young women; mixed solid/cystic lesion|Surgical evaluation''')+U('''High-risk IPMN features include obstructive jaundice from a head lesion, enhancing mural nodule/solid component, marked main-duct dilation and suspicious/positive cytology.
 Worrisome findings trigger further evaluation, often EUS; they do not all mandate immediate surgery.
 Cyst-fluid CEA supports mucinous classification but does not independently diagnose malignancy. Surveillance depends on lesion risk, age, comorbidity and ability to undergo treatment.''')),
 S('Pancreatic adenocarcinoma',U('''Head lesions often cause painless jaundice; body/tail tumors may present with weight loss/back pain without jaundice.
 Pancreas-protocol imaging assesses vascular involvement and metastases; tissue is required before most nonsurgical systemic treatment plans.
 CA19-9 is not a screening or exclusion test: it may rise with cholestasis and remain low in nonsecretors.
 Resectable, borderline-resectable, locally advanced and metastatic disease require different strategies. Obstruction, pain, nutrition and thrombosis need concurrent treatment.
 Differentiate autoimmune pancreatitis, chronic pancreatitis and other tumors through a structured specialist assessment.'''))],[CYST,('NCI pancreatic cancer professional summary','https://www.cancer.gov/types/pancreatic/hp/pancreatic-treatment-pdq'),('European IgG4-related digestive disease guideline','https://doi.org/10.1177/2050640620934911')])

def nets():
 write('GI & pancreas','Gastrointestinal Neuroendocrine Tumors',[
 S('Classify the tumor on separate axes',T('Axis|Meaning','''Site|Gastric, small-bowel, appendiceal, rectal or pancreatic origin affects staging and treatment
 Differentiation|Well-differentiated NET versus poorly differentiated neuroendocrine carcinoma
 Grade|Proliferation using site-appropriate mitotic count/Ki-67; grade 3 NET is not synonymous with NEC
 Function|Clinical hormone syndrome; staining alone does not establish a functional tumor
 Stage / receptor expression|Anatomical spread and somatostatin-receptor status guide treatment''')),
 S('Hormone syndromes',T('Syndrome|Key clue / confirmation','''Carcinoid syndrome|Flushing, secretory diarrhea, possible right-sided valve disease; appropriate 5-HIAA testing and confounder review
 Insulinoma|Hypoglycemia with inappropriate endogenous insulin/C-peptide; critical sample and exclusion of drug causes
 Gastrinoma|Acid hypersecretion, ulcers/diarrhea; interpret gastrin with gastric pH and PPI exposure
 VIPoma|Large-volume watery diarrhea, hypokalemia and dehydration
 Glucagonoma|Diabetes, weight loss, necrolytic migratory erythema and thrombosis risk''')+U('''Chromogranin A is nonspecific and can rise with PPIs and renal dysfunction; it does not establish the diagnosis.
 Classic midgut carcinoid syndrome often accompanies hepatic metastases; anatomic exceptions occur.''')),
 S('Staging and treatment',U('''Use cross-sectional imaging, tissue classification and selected somatostatin-receptor imaging; FDG imaging may add information in more aggressive disease.
 Surgery for appropriate localized disease; somatostatin analogues for hormone control and selected tumor-control settings.
 PRRT requires suitable receptor-positive disease and clinical eligibility. Targeted drugs, liver-directed treatment or chemotherapy depend on site, grade and progression.
 Poorly differentiated NEC follows a different systemic-treatment pathway from a low-grade NET.
 Severe secretory syndromes require fluid/electrolyte support while the tumor is treated; anticipate peri-procedural hormone complications.'''))],[PNET,('NCI GI carcinoid tumor professional summary','https://www.cancer.gov/types/gi-carcinoid-tumors/hp/gi-carcinoid-treatment-pdq')])

if __name__=='__main__':colorectal();pancreatitis();pancreas();nets()
