from clinical_note_authoring import *
IBD=('BSG inflammatory bowel disease guideline, 2025','https://doi.org/10.1136/gutjnl-2024-334395')
CEL=('ACG celiac disease guideline, 2023','https://doi.org/10.14309/ajg.0000000000002075')
HP=('ACG H. pylori treatment guideline, 2024','https://pubmed.ncbi.nlm.nih.gov/39626064/')
ACH=('ACG achalasia guideline, 2020','https://gi.org/guideline/diagnosis-and-management-of-achalasia/')
EOE=('ACG eosinophilic esophagitis guideline, 2025','https://doi.org/10.14309/AJG.0000000000003194')

def esophagus():
 write('GI & pancreas','Esophageal Disorders',[
 S('Dysphagia: structural versus motor disease',T('Pattern|Likely direction|Test','''Solids first, progressive|Stricture or cancer|Endoscopy with biopsy
 Intermittent solids/food impaction|Ring or eosinophilic esophagitis|Endoscopy; biopsy even when mucosa appears normal if EoE suspected
 Liquids and solids from onset|Motility disorder|Exclude structural disease, then high-resolution manometry
 Difficulty initiating swallow, aspiration/nasal regurgitation|Oropharyngeal disorder|Swallowing/neurological assessment''')+U('''Weight loss, bleeding, anemia, rapidly progressive symptoms and older age increase concern for malignancy.
 Food bolus with inability to manage secretions requires urgent endoscopic assessment. Do not delay complete obstruction for an elective motility work-up.''')),
 S('Achalasia and major motility patterns',T('Pattern|Manometry|Treatment distinction','''Type I achalasia|Elevated IRP, absent peristalsis, no qualifying panesophageal pressurization|Pneumatic dilation, Heller myotomy or POEM in suitable patients
 Type II achalasia|Elevated IRP, absent peristalsis, panesophageal pressurization ≥20%|Often responds well to LES-disrupting treatment
 Type III achalasia|Elevated IRP, ≥20% premature contractions, no normal peristalsis|Tailored long myotomy/POEM especially useful
 Absent contractility|Normal IRP, 100% failed peristalsis|Do not confuse with achalasia; assess systemic disease
 Distal esophageal spasm|Normal IRP, ≥20% premature contractions plus relevant symptoms|Exclude reflux/secondary causes; selected smooth-muscle relaxation or intervention''')+U('''Timed barium esophagram and FLIP support inconclusive cases. IRP cutoffs depend on equipment and position.
 Endoscopy excludes pseudoachalasia. Rapid weight loss in an older patient warrants careful assessment for malignant obstruction.
 Botulinum toxin is mainly for patients unsuitable for durable therapy. POEM can cause reflux.''')),
 S('GERD, Barrett esophagus and EoE',T('Condition|Diagnosis / principle|Treatment','''GERD|Typical symptoms; investigate alarms or refractory disease; reflux monitoring when diagnosis uncertain|Lifestyle measures and appropriately timed PPI; selected antireflux procedures after objective assessment
 Barrett esophagus|Intestinal metaplasia in an appropriate esophageal segment; assess dysplasia carefully|PPI, surveillance by risk; confirmed dysplasia may require endoscopic eradication
 Eosinophilic esophagitis|Esophageal dysfunction + ≥15 eosinophils/high-power field after assessing other causes|PPI, swallowed topical steroid or dietary therapy; dilation for fibrostenosis plus anti-inflammatory treatment''')+U('''A PPI response does not exclude EoE. Symptoms alone do not reliably show histological remission.
 Do not use dilation alone as the anti-inflammatory treatment for EoE.
 Squamous carcinoma and Barrett-associated adenocarcinoma have different risk contexts; tissue establishes the diagnosis.'''))],[ACH,EOE,('ACG GERD guideline, 2022','https://doi.org/10.14309/ajg.0000000000001538')])

def gastric():
 write('GI & pancreas','Gastric Duodenal Disorders',[
 S('Dyspepsia and peptic ulcer disease',T('Problem|Key distinction','''Uninvestigated dyspepsia|Assess age, local cancer risk and alarm features; H. pylori test-and-treat or acid suppression in suitable low-risk patients
 Gastric ulcer|Biopsy and follow-up according to lesion/risk; malignancy can mimic a benign ulcer
 Duodenal ulcer|H. pylori and NSAIDs are major causes; routine malignancy risk differs from gastric ulcer
 Recurrent/refractory ulcer|Check adherence, ongoing NSAID/aspirin exposure, persistent H. pylori and uncommon hypersecretory causes
 Bleeding/perforation/obstruction|Complication pathway rather than routine outpatient dyspepsia treatment''')+U('''NSAID injury reflects impaired mucosal protection; PPI reduces acid injury but does not eliminate every bleeding risk.
 Avoid attributing weight loss, persistent vomiting or iron-deficiency anemia to functional dyspepsia without assessment.''')),
 S('H. pylori: treatment and confirmation',T('Decision|High-yield rule','''Initial treatment, susceptibility unknown|ACG 2024 favors optimized bismuth quadruple therapy for 14 days
 Bismuth quadruple components|PPI + bismuth + tetracycline + metronidazole
 Clarithromycin/levofloxacin regimens|Do not use empirically where resistance undermines efficacy; use susceptibility-directed selection
 Test of cure|Urea breath test, stool antigen or indicated biopsy testing ≥4 weeks after antibiotics; withhold PPI/PCAB for 2 weeks where feasible
 Serology|Does not reliably prove active infection or eradication''')+U('''Review previous antibiotic exposure, allergy and adherence before rescue therapy. Rifabutin-based or vonoprazan-based options have defined roles.
 Acute bleeding and suppressive drugs can produce false-negative tests; repeat appropriately when suspicion remains.''')),
 S('Gastric inflammation and hypersecretion',T('Condition|Distinctive finding|Important consequence','''Autoimmune gastritis|Corpus-predominant atrophy; parietal-cell/intrinsic-factor autoimmunity|Iron/B12 deficiency; hypergastrinemia and type 1 gastric NET risk
 H. pylori atrophic gastritis|Chronic inflammation/atrophy and metaplasia|Gastric cancer risk; eradicate infection and assess surveillance indications
 Zollinger–Ellison syndrome|Inappropriate hypergastrinemia with acid hypersecretion|Recurrent ulcers/diarrhea; consider MEN1
 Ménétrier disease|Giant folds with protein loss|Hypoalbuminemia; requires distinction from infiltrative malignancy''')+U('''A high gastrin level alone does not diagnose gastrinoma: PPIs and achlorhydria also raise gastrin. Interpret with gastric acidity and specialist testing.
 Diffuse infiltrative gastric cancer may yield negative superficial biopsies; persistent suspicious wall thickening needs deeper/targeted assessment.
 Gastroparesis requires delayed emptying without mechanical obstruction; symptoms alone are insufficient.'''))],[HP,('NCI gastric cancer professional summary','https://www.cancer.gov/types/stomach/hp/stomach-treatment-pdq')])

def malabsorption():
 write('GI & pancreas','Small Intestine Malabsorption',[
 S('Localize the mechanism',T('Mechanism|Examples|Clues','''Mucosal disease|Celiac disease, tropical sprue, immune-mediated enteropathy|Multiple nutrient deficiencies; biopsy abnormalities
 Maldigestion|Pancreatic exocrine insufficiency|Steatorrhea, weight loss; fecal elastase supports assessment
 Bile-acid depletion/malabsorption|Ileal disease/resection, cholestatic disorders|Watery diarrhea or fat malabsorption depending on extent
 Bacterial overgrowth|Altered anatomy, dysmotility|Bloating, diarrhea, possible B12 deficiency
 Lymphatic disease|Intestinal lymphangiectasia|Protein loss, lymphopenia, edema''')+U('''Assess weight, stool pattern, CBC, iron, B12/folate, albumin and relevant fat-soluble vitamins.
 A watery stool can falsely lower fecal elastase by dilution. A positive breath test requires clinical interpretation; no single test proves every malabsorption syndrome.''')),
 S('Celiac disease: diagnosis before diet',T('Step|Key point','''Initial serology|tTG-IgA plus total IgA while eating gluten
 IgA deficiency|Use appropriate IgG-based tests
 Confirmation in adults|Duodenal biopsies usually required; include bulb and distal duodenum
 HLA-DQ2/DQ8|Absence strongly argues against celiac disease; presence is common and not diagnostic
 Treatment|Strict gluten-free diet, dietitian review and correction of deficiencies''')+U('''Villous atrophy is not specific: consider medicines such as olmesartan, immunodeficiency, Giardia, tropical sprue and other enteropathies.
 Gluten restriction before testing can cause false-negative serology/biopsy. Use a planned specialist approach when diagnosis is uncertain.
 Persistent symptoms: first assess gluten exposure and alternative causes before labeling refractory celiac disease.''')),
 S('High-yield differentials',T('Condition|Distinguishing point','''Tropical sprue|Tropical exposure with diffuse malabsorption; folate/B12 deficiency; exclude celiac and infection
 Whipple disease|Systemic symptoms, arthralgia and intestinal disease; tissue/PCR diagnosis with organism-specific treatment
 Giardia|Water/exposure history; chronic diarrhea and malabsorption; stool antigen/PCR testing
 Ileal disease/resection|B12 and bile-acid problems; extensive loss can worsen fat malabsorption
 Short bowel|Fluid, electrolyte and nutrition needs depend on remaining length, ileum and colon continuity
 Protein-losing enteropathy|Low albumin after excluding hepatic/renal causes; fecal alpha-1-antitrypsin clearance can support diagnosis''')+U('''Iron deficiency often reflects proximal small-bowel disease; B12 absorption depends on intrinsic factor and terminal ileum.
 Refractory celiac disease requires confirmed diagnosis, exclusion of gluten exposure and specialist evaluation for aberrant lymphocytes/lymphoma.
 Treat the cause and replace deficiencies; antidiarrheals alone do not correct malabsorption.'''))],[CEL,('NICE celiac disease guideline','https://www.nice.org.uk/guidance/ng20/chapter/Recommendations')])

def ibd():
 write('GI & pancreas','Inflammatory Bowel Disease',[
 S('Ulcerative colitis versus Crohn disease',T('Feature|Ulcerative colitis|Crohn disease','''Distribution|Colon; usually continuous from rectum|Any GI segment; skip lesions
 Depth|Predominantly mucosal|Transmural
 Complications|Severe bleeding, toxic megacolon; colorectal cancer risk|Stricture, fistula, abscess; malnutrition
 Histology|Chronic colitis pattern; no diagnostic granuloma requirement|Noncaseating granulomas support diagnosis but are often absent
 Surgery|Colectomy removes colonic disease|Resection is not curative; recurrence common''')+U('''Exclude infection, especially C. difficile, during flares. Ileocolonoscopy with segmental biopsies establishes extent; small-bowel imaging assesses Crohn disease.
 Fecal calprotectin helps assess intestinal inflammation but is not specific for IBD. Symptoms and CRP alone can miss active disease.''')),
 S('Treatment classes: induction versus maintenance',T('Class|Role|Major trap','''5-ASA|Mild–moderate UC; topical treatment important in distal disease|Not a reliable general treatment for luminal Crohn disease
 Corticosteroids|Induction of remission in selected active disease|Not maintenance treatment
 Thiopurine / methotrexate|Selected steroid-sparing maintenance roles; methotrexate not interchangeable across UC/CD|Slow onset, marrow/hepatic toxicity; assess appropriate pharmacogenetic/infection risks
 Anti-TNF|Moderate–severe disease and selected fistulizing Crohn disease|TB/HBV screening; assess infection and immunogenic loss of response
 Vedolizumab|Gut-selective integrin blockade|Not an immediate rescue for every unstable severe flare
 IL-12/23 or IL-23-directed therapy|Defined UC/CD indications|Agent and disease indications differ
 JAK inhibitors / S1P modulators|Selected moderate–severe disease|Infection, thrombotic/cardiovascular or conduction risks depend on class/agent''')+U('''Select therapy by severity, location, prior exposure, complications and comorbidity; an obligatory prolonged step-up sequence is not appropriate for every high-risk patient.
 Aim for sustained steroid-free control and objective improvement; persistent symptoms can also reflect infection, stricture, bile-acid diarrhea or IBS overlap.''')),
 S('Acute severe UC and complications',U('''Acute severe UC: ≥6 bloody stools/day plus systemic toxicity; admit, assess infection, give IV corticosteroids and VTE prophylaxis unless contraindicated.
 Review response early, commonly by day 3. Steroid-refractory disease requires rescue infliximab/ciclosporin in appropriate patients or surgery; do not delay colectomy for deterioration, perforation, uncontrolled hemorrhage or toxic megacolon.
 Avoid antidiarrheals/opioids and full colonoscopy in a dangerously dilated inflamed colon; use appropriate limited assessment.
 Crohn abscess: antibiotics and drainage/source control; do not intensify immunosuppression while uncontrolled sepsis persists.
 Smoking worsens Crohn disease. PSC changes colorectal surveillance risk; colectomy does not cure PSC.''')),
 S('Surveillance and extraintestinal disease',U('''Colorectal surveillance depends on duration, extent, inflammatory burden, PSC and previous dysplasia; use high-quality surveillance techniques.
 Peripheral arthritis may track bowel activity; axial disease can follow a separate course.
 Red painful eye with photophobia requires urgent assessment for uveitis.
 Before advanced therapy: infection screening, vaccination review, cancer risk and pregnancy planning; do not stop effective treatment reflexively in pregnancy without assessing relapse risk.'''))],[IBD,('ACG UC guideline, 2025','https://doi.org/10.14309/ajg.0000000000003463')])

if __name__=='__main__':esophagus();gastric();malabsorption();ibd()
