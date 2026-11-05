"""Original Small Intestine and Malabsorption chapter."""
from qbank_authoring import question,ref,finalize
CE=ref('ESsCD 2025 Adult Coeliac Disease Diagnostic Guideline','https://doi.org/10.1002/ueg2.70119')
PARIS=ref('Paris Consensus on Seronegative Coeliac Disease and Non-Coeliac Enteropathies','https://doi.org/10.1136/gutjnl-2021-326645')
SIBO=ref('ACG 2020 Small Intestinal Bacterial Overgrowth Guideline','https://doi.org/10.14309/ajg.0000000000000501')
IF=ref('ESPEN 2023 Chronic Intestinal Failure Guideline','https://academy.espen.org/files/ESPEN-Guidelines/ESPEN_guideline_on_chronic_intestinal_failure_in_adults.pdf')
AMI=ref('WSES 2022 Acute Mesenteric Ischemia Guideline','https://doi.org/10.1186/s13017-022-00443-x')
rows=[]
def q(*args,**kwargs):rows.append(question(*args,**kwargs))

q('An adult with iron deficiency and chronic diarrhea is being screened for celiac disease while eating gluten. Which initial serological approach is appropriate?',
 'IgA anti-tissue-transglutaminase with assessment of total IgA',[
 ('IgA tTG alone interpreted as definitive exclusion even if IgA deficient','IgA deficiency can make an IgA-based screen falsely reassuring.'),
 ('Native antigliadin antibodies as the preferred modern stand-alone test','These are less suitable than current validated serological approaches.'),
 ('HLA-DQ2 positivity alone as proof of disease','The allele is common and not sufficiently specific.')],
 'A valid screen requires the relevant immunoglobulin context',
 '**IgA tTG is a preferred first-line test when total IgA is adequate.**',
 ['Testing should usually occur during gluten exposure.', 'Clinical suspicion and the chosen diagnostic pathway determine whether biopsy is needed.'],
 '**A negative result has conditions.**',
 ['Low IgA, limited gluten intake and selected seronegative disease can change interpretation.', 'Do not diagnose or exclude disease from one decontextualized result.'],
 [['Adequate IgA','IgA tTG-based screen'],['IgA deficiency','Use appropriate IgG testing'],['Gluten avoidance','Can suppress detection']], [CE], 'clinical_scenario')
q('A patient with suspected celiac disease has selective IgA deficiency. Which serological strategy is appropriate?',
 'Use validated IgG-based celiac tests such as IgG anti-TG2 or deamidated gliadin peptide antibodies',[
 ('Repeat only IgA tTG until it becomes positive','The immunoglobulin deficiency limits that strategy.'),
 ('Treat a negative IgA result as sufficient exclusion','It can be falsely negative.'),
 ('Use a food-specific IgE panel as the diagnostic equivalent','IgE allergy testing is not a celiac serological substitute.')],
 'Match the assay to the patient\'s immunoglobulin production',
 '**IgG-based testing is needed when IgA is deficient.**',
 ['Interpret assay performance and the clinical pretest probability.', 'Persistent convincing malabsorption can still justify duodenal biopsies despite negative serology.'],
 '**Do not confuse celiac autoimmunity with wheat allergy.**',
 ['The tests and mechanisms differ.', 'Confirm the diagnosis before committing to a lifelong restrictive diet.'],
 [['IgA deficiency','IgG-based celiac serology'],['Wheat allergy','Different immune diagnostic pathway'],['High clinical suspicion','Consider histological assessment']], [CE], 'clinical_scenario')
q('When duodenal histology is required for suspected celiac disease, which sampling principle is correct?',
 'Obtain multiple well-oriented samples from both the bulb and distal duodenum',[
 ('One distal fragment excludes patchy disease reliably','Limited sampling can miss disease.'),
 ('Biopsy only a normal stomach instead of the duodenum','The relevant small-bowel mucosa must be assessed.'),
 ('Avoid the bulb because celiac involvement cannot occur there','Bulb involvement can be important.')],
 'Celiac histology can be patchy',
 '**Sampling more than one duodenal location improves sensitivity.**',
 ['The 2025 European approach recommends adequate distal samples plus bulb biopsies.', 'Correct orientation helps assess villous architecture.'],
 '**Histology needs clinical and serological context.**',
 ['Villous atrophy and intraepithelial lymphocytes are not uniquely celiac.', 'Infection, immune deficiency and drug injury can mimic the pattern.'],
 [['Bulb plus distal sampling','Addresses patchiness'],['Orientation','Improves architecture assessment'],['Villous atrophy','Requires etiological interpretation']], [CE,PARIS])
q('A patient started a gluten-free diet before testing and now has negative celiac serology. What is the best interpretation?',
 'The negative result may reflect gluten withdrawal and does not reliably exclude celiac disease',[
 ('The diet response alone proves celiac disease','Several conditions can improve with dietary changes.'),
 ('Negative on-diet serology always excludes the diagnosis','Reduced antigen exposure can suppress antibody production.'),
 ('An immediate biopsy after prolonged avoidance must show untreated disease','Histology can also improve.')],
 'Testing after diet change can erase diagnostic evidence',
 '**A gluten-containing diet is usually required for standard diagnostic assessment.**',
 ['Review the original evidence and duration of avoidance.', 'HLA testing can be useful when the diagnosis is uncertain after dietary restriction.'],
 '**Plan any gluten challenge safely and collaboratively.**',
 ['Dose, duration and suitability depend on the patient.', 'Do not impose a lifelong label from symptom response alone.'],
 [['Before gluten withdrawal','Best opportunity for standard tests'],['After withdrawal','Serology and histology may normalize'],['Uncertain diagnosis','HLA and selected challenge assessment']], [CE], 'clinical_scenario')
q('What is the main diagnostic value of absent HLA-DQ2 and DQ8 in an uncertain celiac case?',
 'It makes celiac disease very unlikely',[
 ('It confirms celiac disease','The absence is useful for exclusion, not confirmation.'),
 ('A positive DQ2 result alone is equally definitive for diagnosis','Risk alleles are too common to establish disease by themselves.'),
 ('HLA is a direct measure of current villous healing','It is inherited susceptibility, not disease activity.')],
 'High negative value differs from low positive specificity',
 '**Most celiac disease occurs in a compatible HLA background.**',
 ['Absence is useful when earlier testing was incomplete or performed on a gluten-free diet.', 'Presence indicates susceptibility rather than proof.'],
 '**Use genetic testing to answer a selected uncertainty.**',
 ['Routine testing is not needed in every straightforward serology-histology case.', 'Rare exceptions and laboratory scope should be considered in a strongly discordant case.'],
 [['HLA absent','Celiac very unlikely'],['HLA present','Susceptibility only'],['Activity assessment','Requires other measures']], [CE])
q('Under the 2025 ESsCD diagnostic guideline, which adult may qualify for a carefully selected no-biopsy celiac pathway?',
 'A patient under 45 with IgA anti-TG2 at least 10 times ULN, appropriate confirmation and no reason requiring endoscopy',[
 ('An older patient with weight loss and gastrointestinal bleeding regardless of serology','Alarm features and alternative pathology require endoscopic assessment.'),
 ('A patient with only a weakly positive tTG and no supporting evidence','The high-titer criterion is not met.'),
 ('Any patient who improves after avoiding bread','Symptoms alone are not the no-biopsy criterion.')],
 'Newer adult pathways are conditional and guideline specific',
 '**ESsCD 2025 permits selected high-titer adults under 45 to avoid biopsy after appropriate confirmation and shared decisions.**',
 ['A new sample for repeat high-titer IgA anti-TG2 is conditionally recommended where feasible.', 'The pathway does not replace endoscopy when another clinical indication exists.'],
 '**Do not mix this with older universal-biopsy or different national frameworks.**',
 ['State the guideline when testing a threshold.', 'Accurate lifelong diagnosis matters before dietary commitment and family assessment.'],
 [['Selected young high-titer adult','Conditional no-biopsy option'],['Low titer or discordance','Further diagnostic assessment'],['Alarm features','Endoscopy may still be needed']], [CE])
q('A patient has intensely pruritic grouped vesicles on extensor surfaces and granular IgA deposits at dermal papillae on perilesional biopsy. Which association is most likely?',
 'Dermatitis herpetiformis associated with celiac disease',[
 ('Pemphigus vulgaris with intercellular IgG','That has a different blister level and immunofluorescence pattern.'),
 ('Bullous pemphigoid with linear basement-membrane staining','The linear pattern differs from granular papillary IgA.'),
 ('Simple food urticaria with no enteropathy relevance','The biopsy pattern supports a specific gluten-associated disease.')],
 'A skin phenotype can reveal gluten-related autoimmunity',
 '**Granular IgA in dermal papillae is characteristic of dermatitis herpetiformis.**',
 ['Intestinal disease can be present even without prominent bowel symptoms.', 'Perilesional rather than destroyed blister tissue improves immunofluorescence assessment.'],
 '**Treat the underlying gluten-sensitive disease.**',
 ['A gluten-free diet is central.', 'Dapsone may control skin symptoms in an appropriate monitored plan, with G6PD and toxicity considerations.'],
 [['Dermatitis herpetiformis','Granular papillary IgA'],['Pemphigoid','Linear basement-membrane pattern'],['Care','Skin control plus gluten-disease management']], [CE], 'clinical_scenario')
q('A patient with established celiac disease has persistent symptoms after starting a gluten-free diet. What is an important early step before diagnosing refractory celiac disease?',
 'Review the original diagnosis and assess ongoing gluten exposure with an experienced dietitian',[
 ('Start lymphoma chemotherapy based on symptoms alone','Refractory disease and malignancy require evidence.'),
 ('Assume every symptom means permanent refractory enteropathy','Exposure, IBS, lactose intolerance, SIBO and other causes are more common explanations.'),
 ('Use symptom improvement as the only measure of mucosal recovery','Symptoms and histology can diverge.')],
 'Nonresponse is a problem to investigate, not a final diagnosis',
 '**Inadvertent gluten exposure is an important correctable cause.**',
 ['Confirm the initial serological and histological evidence.', 'Review dietary sources, cross-contamination and associated disorders.'],
 '**Escalate when persistent enteropathy remains unexplained.**',
 ['Repeat biopsies and specialist testing may be needed.', 'Weight loss, anemia or pain can prompt complication assessment.'],
 [['Initial review','Diagnosis and gluten exposure'],['Alternative causes','Investigate by phenotype'],['Persistent villous disease','Specialist refractory-work-up']], [CE,PARIS], 'clinical_scenario')
q('Which finding distinguishes type II refractory celiac disease from type I?',
 'An aberrant clonal intraepithelial lymphocyte population',[
 ('Any positive tTG at the first untreated presentation','That does not establish refractory disease or its subtype.'),
 ('A normal polyclonal IEL phenotype as the defining type II feature','Type I retains a more normal IEL phenotype.'),
 ('Lactose intolerance without persistent villous atrophy','That is not the defining refractory-enteropathy substrate.')],
 'IEL phenotype changes prognosis and management',
 '**Type II has an abnormal clonal lymphocyte population and greater lymphoma concern.**',
 ['Diagnosis requires specialist immunophenotypic and molecular interpretation.', 'Ongoing gluten exposure and other enteropathies must be excluded first.'],
 '**Assess for complications rather than treating a label empirically.**',
 ['Enteropathy-associated T-cell lymphoma is an important concern.', 'Nutrition, immunological treatment and oncological surveillance require expertise.'],
 [['Type I','More normal IEL phenotype'],['Type II','Aberrant clonal IELs'],['Clinical consequence','Higher-risk specialist pathway']], [ref('AGA 2022 Refractory Celiac Disease Clinical Practice Update','https://doi.org/10.1053/j.gastro.2022.07.086')])
q('A patient with longstanding celiac disease develops new severe abdominal pain, weight loss and a focal small-bowel mass. Which complication is particularly important to exclude?',
 'Enteropathy-associated T-cell lymphoma',[
 ('Simple dietary nonadherence as the only possible cause','A mass and systemic deterioration require complication assessment.'),
 ('An isolated benign lactose intolerance as the complete explanation','That does not explain a focal mass.'),
 ('A pituitary adenoma as the characteristic intestinal cancer','This is not the relevant association.')],
 'New alarm features change a chronic enteropathy follow-up',
 '**Celiac-associated lymphoproliferative disease is a serious differential.**',
 ['Refractory type II disease raises particular concern.', 'Small-bowel adenocarcinoma is another relevant malignancy.'],
 '**Obtain tissue and staging through a specialist pathway.**',
 ['Cross-sectional enterography and targeted endoscopic assessment can help.', 'Do not attribute new focal disease to the previous diet diagnosis alone.'],
 [['Stable celiac symptoms','Diet and routine assessment'],['New mass/weight loss/pain','Complication investigation'],['EATL','Important lymphoma association']], [CE], 'clinical_scenario')
q('A patient taking olmesartan develops chronic diarrhea and villous atrophy with negative celiac serology and no response to a gluten-free diet. Which cause should be considered?',
 'Olmesartan-associated sprue-like enteropathy',[
 ('Celiac disease proven by villous atrophy alone','Villous atrophy has a differential and the serology, exposure and response are discordant.'),
 ('A positive HLA result as proof that the drug cannot contribute','HLA susceptibility is not causation.'),
 ('An acute norovirus infection as the only explanation of a chronic drug-related pattern','The prolonged course and medication association require assessment.')],
 'Medication review is essential in seronegative villous atrophy',
 '**Olmesartan can cause a celiac-like enteropathy.**',
 ['Clinical and histological improvement after withdrawal supports the relationship.', 'Exclude other causes rather than diagnosing from exposure alone.'],
 '**Avoid an unnecessary lifelong dietary label.**',
 ['Review pathology, immunoglobulins, infections and other drugs.', 'Coordinate a safe antihypertensive alternative.'],
 [['Celiac','Gluten-related immune enteropathy'],['Olmesartan injury','Drug-related mimic'],['Seronegative atrophy','Requires a structured differential']], [PARIS], 'clinical_scenario')
q('A patient has years of migratory arthralgia followed by weight loss and diarrhea. Duodenal biopsies show PAS-positive macrophages and tissue PCR confirms Tropheryma whipplei. What is the diagnosis?',
 'Whipple disease',[
 ('Celiac disease as the specific explanation of PAS-positive macrophages','That is not the typical celiac histological pattern.'),
 ('Disseminated MAC established despite organism-specific PCR for another pathogen','MAC can be a histological mimic, but the specific PCR supports Whipple in this context.'),
 ('Isolated primary lactase deficiency','That does not explain systemic arthralgia and tissue infection.')],
 'An infection can precede bowel symptoms with joint disease',
 '**Classic Whipple disease combines systemic features with small-bowel infection.**',
 ['PAS staining alone is not fully specific.', 'PCR and expert histology help distinguish mimics such as mycobacterial disease.'],
 '**Assess systemic involvement before treatment planning.**',
 ['Neurological or cardiac involvement changes the evaluation.', 'An isolated positive stool PCR can represent carriage and is not equivalent to tissue-confirmed symptomatic disease.'],
 [['Clinical clue','Arthralgia preceding malabsorption'],['Tissue','PAS macrophages plus specific confirmation'],['Assessment','Systemic and neurological involvement']], [ref('Clinical Manifestations, Treatment and Diagnosis of T. whipplei Infection','https://doi.org/10.1128/CMR.00033-16')], 'clinical_scenario')
q('A long-term resident of an endemic tropical region develops malabsorption with folate and B12 deficiency. Celiac and parasitic causes are excluded, and the syndrome improves with appropriate antibiotic and folate treatment. Which diagnosis fits?',
 'Tropical sprue',[
 ('Celiac disease established solely by villous blunting','The geographical, exclusion and treatment context supports another enteropathy.'),
 ('Primary pancreatic insufficiency as proof from folate deficiency alone','The pattern suggests a small-intestinal absorptive problem, although pancreatic disease is part of a broad differential.'),
 ('Isolated iron deficiency without enteropathy','Multiple nutrient deficits and diarrhea indicate more extensive malabsorption.')],
 'Tropical sprue is an exclusion-based malabsorptive syndrome',
 '**Folate and B12 deficits can coexist with chronic diarrhea in the appropriate exposure setting.**',
 ['Exclude celiac disease and treatable infections.', 'Histological changes are not uniquely diagnostic.'],
 '**Replace nutrients while addressing the enteropathy.**',
 ['B12 must not be overlooked when folate is given.', 'Failure to respond should prompt reassessment of the diagnosis.'],
 [['Exposure','Endemic tropical residence/travel'],['Deficits','Folate and B12 often important'],['Diagnosis','Exclude competing enteropathies']], [ref('Merck Manual Professional: Tropical Sprue','https://www.merckmanuals.com/professional/gastrointestinal-disorders/malabsorption-syndromes/tropical-sprue')], 'clinical_scenario')
q('A patient has chronic bloating, greasy stools and weight loss after untreated-water exposure. Which stool investigation can directly support giardiasis?',
 'A validated Giardia antigen or molecular assay',[
 ('Fecal occult blood alone','It does not identify Giardia.'),
 ('A negative single routine microscopy sample as definitive exclusion','Intermittent shedding can reduce single-sample sensitivity.'),
 ('Serum tTG as the organism-specific test','That assesses celiac autoimmunity rather than Giardia.')],
 'A small-intestinal infection can mimic noninfectious malabsorption',
 '**Giardia can cause prolonged diarrhea and nutrient malabsorption.**',
 ['Antigen or molecular testing improves practical detection.', 'Repeated microscopy may be used when appropriate.'],
 '**Interpret testing with exposure and immune status.**',
 ['Persistent or recurrent infection can prompt assessment of reinfection or immune deficiency.', 'Avoid assigning celiac disease from nonspecific villous changes without considering infection.'],
 [['Water exposure plus greasy diarrhea','Giardia consideration'],['Antigen/NAAT','Specific detection'],['Persistent disease','Assess cause and susceptibility factors']], [ref('CDC: Clinical Testing and Diagnosis for Giardia Infection','https://www.cdc.gov/giardia/hcp/diagnosis-testing/index.html')], 'clinical_scenario')
q('Using conventional North American breath-test criteria, which hydrogen result supports SIBO in an appropriate symptomatic patient?',
 'A rise of at least 20 ppm above baseline within 90 minutes after the test substrate',[
 ('Any hydrogen value above zero at any time','Normal fermentation produces some gas.'),
 ('A late rise only after clear colonic arrival as proof of small-bowel overgrowth','Colonic fermentation and rapid transit can confound interpretation.'),
 ('A methane-only result interpreted as proof that the organisms are bacteria','Methanogens are archaea and are termed IMO.')],
 'A breath test is an indirect and context-sensitive test',
 '**A conventional early hydrogen rise can support SIBO.**',
 ['Preparation, substrate and transit affect accuracy.', 'Lactulose can be falsely positive with rapid orocecal transit.'],
 '**Do not diagnose from bloating or a number alone.**',
 ['Use predisposing anatomy or dysmotility and the clinical phenotype.', 'A positive test does not remove the need to address the underlying cause.'],
 [['Early hydrogen rise','Supports SIBO in context'],['Methane at least 10 ppm','IMO framework'],['Limitations','Transit and preparation']], [SIBO])
q('A constipated patient has methane levels at least 10 ppm during a suitable breath test. Which terminology is preferred?',
 'Intestinal methanogen overgrowth',[
 ('Hydrogen-positive SIBO by definition','Methane reflects a distinct microbial and testing pattern.'),
 ('A direct diagnosis of pancreatic insufficiency','The gas result does not establish pancreatic function.'),
 ('A positive celiac serology','Breath gas is not celiac autoantibody testing.')],
 'Methanogens are not bacteria',
 '**IMO acknowledges methane-producing archaea and their distribution beyond the small bowel.**',
 ['Methane positivity is associated with constipation.', 'The conventional criterion is at least 10 ppm at an appropriate measured point, not an obligatory rise from baseline.'],
 '**Use a symptom- and cause-aware treatment plan.**',
 ['Review motility and constipation contributors.', 'Do not treat every positive gas trace without clinical context.'],
 [['Hydrogen pattern','SIBO assessment'],['Methane pattern','IMO terminology'],['Clinical association','Constipation phenotype']], [SIBO])

# Additional malabsorption mechanisms, intestinal failure and ischemia follow.
q('A patient with a surgically created blind small-bowel loop develops steatorrhea, low B12 and relatively preserved or elevated folate. Which mechanism is likely?',
 'Small-intestinal bacterial overgrowth',[
 ('Pure autoimmune intrinsic-factor deficiency as the sole explanation','That explains B12 deficiency but not the blind-loop malabsorption pattern as well.'),
 ('Isolated lactase deficiency','It does not usually cause this steatorrhea and B12 pattern.'),
 ('A congenital glucose-galactose transporter defect newly appearing in old age','The acquired anatomical stasis is the more relevant mechanism.')],
 'Stasis allows excessive microbial activity',
 '**Overgrowth can consume B12 and deconjugate bile acids.**',
 ['Bile acid deconjugation can impair micelle formation and fat absorption.', 'Microbial folate production can preserve or increase folate despite other deficiencies.'],
 '**Treat the predisposition as well as the microbial burden.**',
 ['Review anatomy, motility and nutritional deficits.', 'Repeated antibiotics without addressing the loop or dysmotility can lead to recurrence.'],
 [['Blind loop','Stasis predisposition'],['B12 low/folate relatively high','Compatible microbial effect'],['Steatorrhea','Bile acid deconjugation can contribute']], [SIBO], 'clinical_scenario')
q('In the classical D-xylose absorption test, which pattern favors pancreatic maldigestion over proximal small-bowel mucosal disease?',
 'Steatorrhea with preserved D-xylose absorption when renal function and test conditions are adequate',[
 ('Low urinary recovery as a perfectly specific pancreatic test','Recovery can be affected by mucosal disease, kidney function and other factors.'),
 ('A normal result as proof that all intestinal disease is excluded','The test has limitations and does not exclude every intestinal disorder.'),
 ('A requirement for pancreatic enzymes to digest D-xylose before uptake','D-xylose does not require pancreatic digestion.')],
 'Digestion and mucosal absorption are different steps',
 '**D-xylose can be absorbed without pancreatic enzyme processing.**',
 ['Preserved uptake can coexist with pancreatic fat maldigestion.', 'Mucosal disease may reduce uptake.'],
 '**Recognize that this is a classical physiological test with limited modern use.**',
 ['Renal impairment can reduce urinary recovery independently of absorption.', 'Current work-up often uses more targeted tests and imaging.'],
 [['Pancreatic insufficiency','D-xylose may remain normal'],['Proximal mucosal injury','Can reduce absorption'],['Urine recovery','Also depends on kidney function']], [ref('Merck Manual Professional: Overview of Malabsorption','https://www.merckmanuals.com/professional/gastrointestinal-disorders/malabsorption-syndromes/overview-of-malabsorption')])
q('A patient with chronic watery diarrhea has fecal elastase 70 micrograms/g from a liquid specimen but no established pancreatic disease. What is the appropriate interpretation?',
 'The result may be falsely low from dilution and should be reassessed using an appropriate formed or semisolid sample and clinical context',[
 ('It proves pancreatic insufficiency regardless of specimen quality','Water content can lower the measured concentration.'),
 ('A trial of enzymes alone is a definitive diagnostic test','Treatment response is not a sufficiently reliable stand-alone diagnosis.'),
 ('A normal CT would exclude every degree of pancreatic insufficiency','Function and anatomy are not perfectly interchangeable.')],
 'Specimen consistency matters for an enzyme concentration',
 '**AGA recommends fecal elastase testing on a solid or semisolid stool.**',
 ['Below 100 on an appropriate specimen provides good evidence of EPI.', 'Values 100-200 are indeterminate and require further assessment.'],
 '**Do not label a patient from a diluted sample alone.**',
 ['Assess pancreatic risk, weight, nutrient deficits and other causes of diarrhea.', 'Repeat or pursue additional evaluation according to the full picture.'],
 [['Liquid stool','False-low concentration risk'],['Appropriate sample below 100','Supports EPI'],['100-200','Indeterminate']], [ref('AGA 2023 Exocrine Pancreatic Insufficiency Clinical Practice Update','https://doi.org/10.1053/j.gastro.2023.07.007')], 'clinical_scenario')
q('Which intestinal segment is especially important for intrinsic-factor-bound B12 absorption and bile acid reabsorption?',
 'Terminal ileum',[
 ('Duodenal bulb','The bulb is not the principal site for these specific absorptive processes.'),
 ('Proximal jejunum as the only required site','Many nutrients are absorbed there, but the named processes are terminal-ileal functions.'),
 ('Rectum','The rectum does not replace these ileal functions.')],
 'Anatomical loss predicts the deficiency pattern',
 '**Terminal ileal disease or resection can impair both B12 and bile acid conservation.**',
 ['B12 depletion may emerge after stored reserves decline.', 'Bile acid consequences depend on the extent of loss and the remaining bowel.'],
 '**Plan long-term replacement and monitoring.**',
 ['Assess fat-soluble nutrients, fluid and electrolyte balance when disease is extensive.', 'A normal early B12 value does not guarantee no later deficiency.'],
 [['Terminal ileum','B12-IF and bile acid uptake'],['Limited loss','Can cause bile acid diarrhea'],['Extensive loss','Can deplete the bile acid pool']], [IF])
q('Why can a bile acid sequestrant worsen steatorrhea after extensive ileal resection even though it helps some patients after a limited resection?',
 'Extensive loss can deplete the bile acid pool, and further binding reduces bile acids available for fat absorption',[
 ('All post-ileal-resection diarrhea has an identical mechanism','Extent of loss changes the physiology.'),
 ('Sequestrants replace bile acids in micelles','They bind bile acids rather than supply them.'),
 ('Bile acids have no role in fat absorption','They are important for micelle formation.')],
 'Distinguish colonic bile acid irritation from pool depletion',
 '**A limited ileal defect can deliver excess bile acids to the colon and cause watery diarrhea.**',
 ['Binding can help that phenotype.', 'Extensive resection can instead reduce the total pool enough to impair lipid absorption.'],
 '**Match treatment to anatomy and stool phenotype.**',
 ['Assess steatorrhea and fat-soluble nutrient loss.', 'Do not reflexively give the same binder to every short-bowel patient.'],
 [['Limited ileal loss','Colonic bile acid diarrhea'],['Extensive ileal loss','Pool depletion and steatorrhea'],['Sequestrant','Can help one and worsen the other']], [IF])
q('A patient with short bowel, fat malabsorption and a colon in continuity develops recurrent calcium oxalate stones. Which mechanism contributes?',
 'Unabsorbed fatty acids bind calcium, leaving more soluble oxalate available for colonic absorption',[
 ('All luminal oxalate becomes insoluble when fat is unabsorbed','Calcium is diverted away from oxalate binding.'),
 ('The kidney directly synthesizes all oxalate because the ileum is absent','Enhanced intestinal absorption is the central enteric mechanism.'),
 ('Removing the colon increases the same colonic absorption pathway','Colon continuity is important to this mechanism.')],
 'Fat malabsorption changes luminal calcium binding',
 '**Less calcium remains available to precipitate oxalate in the gut.**',
 ['More soluble oxalate can then be absorbed.', 'Dehydration and low urine volume add stone risk.'],
 '**Use an anatomy-aware prevention plan.**',
 ['Fluid, dietary oxalate and appropriate calcium with meals may be considered.', 'Assess nutritional adequacy rather than imposing indiscriminate fat or calcium restriction.'],
 [['Fatty acids','Bind luminal calcium'],['Oxalate','More soluble and absorbable'],['Colon continuity','Supports enteric hyperoxaluria pathway']], [IF], 'clinical_scenario')
q('A short-bowel patient with a colon in continuity develops episodic ataxia and confusion after carbohydrate-rich meals, with metabolic acidosis and a normal routine L-lactate assay. What should be considered?',
 'D-lactic acidosis',[
 ('Exclusion of all lactate-related disease from a normal L-lactate','Routine assays may not detect D-lactate.'),
 ('Isolated respiratory alkalosis','The stated disorder is metabolic acidosis with characteristic neurological episodes.'),
 ('A hypoglycemic episode proven without a low glucose','The short-bowel fermentation pattern suggests another mechanism.')],
 'Unabsorbed carbohydrate can be fermented to an unusual stereoisomer',
 '**D-lactate-producing colonic organisms can generate an absorbed acid load.**',
 ['Neurological features are characteristic.', 'A specific assay may be needed because routine lactate testing targets L-lactate.'],
 '**Treat the episode and reduce the substrate problem.**',
 ['Manage hydration, acidosis and nutrition with specialist input.', 'Dietary carbohydrate adjustment and selected antimicrobial strategies depend on the case.'],
 [['Short bowel plus colon','Fermentation substrate and site'],['Normal L-lactate','Does not exclude D-lactate'],['Symptoms','Episodic neurological dysfunction and acidosis']], [IF], 'clinical_scenario')
q('Which mechanism underlies teduglutide treatment in selected short-bowel syndrome with intestinal failure?',
 'GLP-2 receptor-mediated enhancement of intestinal absorptive adaptation',[
 ('Direct pancreatic lipase replacement','That is pancreatic enzyme therapy, not teduglutide.'),
 ('Bile acid sequestration as its primary effect','That is a different strategy.'),
 ('Inhibition of every intestinal epithelial growth pathway','Teduglutide promotes trophic adaptation rather than generalized growth inhibition.')],
 'An intestinal growth factor can improve fluid and nutrient absorption',
 '**Teduglutide is a GLP-2 analogue used in carefully selected SBS patients.**',
 ['It can reduce dependence on parenteral support.', 'It does not guarantee complete independence in every anatomy.'],
 '**Monitor the consequences of increased absorption and trophic activity.**',
 ['Fluid overload, drug absorption changes and neoplasia-related precautions require attention.', 'Continue an intestinal rehabilitation program rather than treating the injection as a stand-alone cure.'],
 [['GLP-2 analogue','Supports absorptive adaptation'],['Potential benefit','Reduced parenteral requirement'],['Monitoring','Fluid, medication and mucosal safety']], [IF])
q('Stool sodium is 30 mmol/L and potassium 40 mmol/L. Using 290 minus 2 × (Na + K), what is the stool osmotic gap?',
 '150 mOsm/kg',[
 ('70 mOsm/kg','This is the sum of electrolytes, not the calculated gap.'),
 ('140 mOsm/kg','This is the estimated electrolyte contribution before subtraction.'),
 ('290 mOsm/kg','This omits the electrolyte contribution.')],
 'Estimate the contribution from unmeasured osmoles',
 '**The gap is 290 - 2 × 70 = 150.**',
 ['A high gap supports an osmotic component in the appropriate clinical context.', 'Use fresh properly handled stool electrolytes and do not substitute a misleading measured stool osmolality blindly.'],
 '**The calculation supports, rather than replaces, etiological assessment.**',
 ['Poorly absorbed sugars or laxatives can create an osmotic pattern.', 'Mixed mechanisms and fasting responses require clinical interpretation.'],
 [['Electrolyte sum','70'],['Twice the sum','140'],['Osmotic gap','150']], [ref('Merck Manual Professional: Diarrhea','https://www.merckmanuals.com/professional/gastrointestinal-disorders/symptoms-of-gastrointestinal-disorders/diarrhea')])
q('A patient has edema and severe hypoalbuminemia without sufficient liver disease, renal protein loss or poor intake. Which test can support gastrointestinal protein loss?',
 'Fecal alpha-1-antitrypsin clearance',[
 ('Serum amylase as a direct enteric protein-loss measurement','It does not quantify gastrointestinal protein loss.'),
 ('A normal urine protein as proof that no protein loss exists anywhere','It excludes one route, not the gastrointestinal route.'),
 ('Fecal elastase as an equivalent protein-leak test','Elastase assesses pancreatic enzyme output rather than enteric protein leakage.')],
 'Protein loss can occur across the gastrointestinal tract',
 '**Alpha-1-antitrypsin clearance is useful because the protein resists much intestinal degradation.**',
 ['Interpret with stool volume and serum concentration.', 'Bleeding and gastric acidity can affect selected situations and test interpretation.'],
 '**A positive result does not identify the cause.**',
 ['Consider mucosal disease, lymphatic obstruction and elevated venous pressure.', 'Use imaging, endoscopy and cardiac assessment according to the phenotype.'],
 [['Clearance test','Supports enteric protein loss'],['Etiology','Requires further investigation'],['Differential','Mucosal, lymphatic and hemodynamic causes']], [IF], 'clinical_scenario')
q('A patient has protein-losing enteropathy, lymphopenia and low immunoglobulins. Biopsy shows dilated intestinal lymphatics. Which diagnosis is most likely?',
 'Intestinal lymphangiectasia',[
 ('Isolated pancreatic lipase deficiency','It does not explain lymphatic dilation and lymphocyte loss.'),
 ('Pernicious anemia as the full mechanism','That concerns intrinsic factor and B12, not lymph leakage.'),
 ('A normal physiological response to high dietary protein','The findings are pathological.')],
 'Lymph leakage removes more than albumin',
 '**Loss of intestinal lymph can reduce albumin, lymphocytes and immunoglobulins.**',
 ['Primary disease and secondary lymphatic obstruction are possible.', 'Elevated venous pressure can impair lymph drainage.'],
 '**Identify the driver before assigning an idiopathic label.**',
 ['Assess cardiac, malignant and other obstructive causes.', 'Nutrition and selected low-long-chain-fat/MCT strategies require specialist planning.'],
 [['Lymphatic leakage','Protein and immune-cell loss'],['Biopsy','Dilated lacteals/lymphatics'],['Assessment','Primary versus secondary cause']], [IF], 'clinical_scenario')
q('A patient has recurrent sinopulmonary infections, low IgG and IgA, chronic diarrhea and villous atrophy with sparse plasma cells. Which diagnosis should be considered?',
 'CVID-associated enteropathy',[
 ('Celiac disease proven by a negative IgA tTG','Low IgA makes serology less reliable and the immune phenotype needs assessment.'),
 ('A normal immune state because intestinal symptoms are present','Enteropathy can be part of a primary immune deficiency.'),
 ('Olmesartan injury established without any drug exposure','A medication cause requires an appropriate exposure history.')],
 'Villous atrophy can arise in an immune-deficiency phenotype',
 '**CVID can cause inflammatory or infectious intestinal disease.**',
 ['Reduced plasma cells can be supportive but are not an absolute required finding.', 'Exclude Giardia and other infections before assigning noninfectious CVID enteropathy.'],
 '**Use immunological and gastrointestinal expertise together.**',
 ['Standard celiac antibodies can be difficult to interpret.', 'Treatment depends on infection, inflammation, nutrition and the broader immune diagnosis.'],
 [['CVID clues','Low immunoglobulins and recurrent infection'],['Histology','May show sparse plasma cells and villous injury'],['Work-up','Exclude infection and other enteropathies']], [PARIS,ref('International Consensus Document: CVID Disorders','https://pmc.ncbi.nlm.nih.gov/articles/PMC4869529/')], 'clinical_scenario')
q('A patient with AF suddenly develops severe abdominal pain that is initially disproportionate to examination findings. Which diagnosis requires urgent exclusion?',
 'Acute embolic mesenteric ischemia',[
 ('Uncomplicated IBS solely because the early abdomen is soft','A soft early examination does not exclude intestinal ischemia.'),
 ('Chronic stable malabsorption as the only explanation','The abrupt severe vascular-risk presentation is different.'),
 ('Acute ischemia excluded by an initially normal lactate','Lactate can be normal early.')],
 'Early ischemia can precede peritonitis',
 '**An embolic source and abrupt pain are important clues.**',
 ['Progression can lead to transmural necrosis.', 'No single routine laboratory test safely excludes early AMI.'],
 '**Obtain urgent CTA and surgical/vascular assessment.**',
 ['Do not wait for lactate to rise or the abdomen to become rigid.', 'Resuscitation and definitive perfusion/source-control planning proceed together.'],
 [['Early AMI','Severe pain with limited examination findings'],['Later necrosis','Peritonitis may develop'],['Diagnosis','Urgent vascular imaging']], [AMI], 'clinical_scenario')
q('A patient in prolonged shock on vasopressors develops suspected bowel ischemia without a major mesenteric arterial occlusion. Which mechanism is possible?',
 'Nonocclusive mesenteric ischemia from low flow and vasoconstriction',[
 ('A patent proximal artery excludes all ischemia','Microcirculatory hypoperfusion can occur without an occlusive clot.'),
 ('A mandatory large embolus despite no occlusion','The syndrome can be nonocclusive.'),
 ('A benign medication effect that never needs bowel assessment','NOMI can be lethal.')],
 'Intestinal perfusion can fail without a blocked main artery',
 '**Low output and intense splanchnic vasoconstriction can reduce tissue flow.**',
 ['Critically ill patients may have muted or nonspecific symptoms.', 'Feed intolerance, distension, acidosis and organ deterioration can be clues.'],
 '**Correct perfusion and assess bowel viability urgently.**',
 ['Treat the shock driver and reassess vasoconstrictor burden while preserving systemic perfusion.', 'Necrotic bowel requires source control; selected vascular treatments depend on the case.'],
 [['Occlusive AMI','Arterial or venous obstruction'],['NOMI','Low flow/vasoconstriction without major occlusion'],['Management','Perfusion plus viability assessment']], [AMI], 'clinical_scenario')
q('An older patient with diffuse atherosclerosis has reproducible postprandial abdominal pain, food avoidance and weight loss. Which diagnosis is most likely?',
 'Chronic mesenteric ischemia',[
 ('Classic isolated lactose intolerance as the best explanation of vascular food fear','The atherosclerotic pattern and weight loss warrant vascular assessment.'),
 ('Acute appendicitis with a stable months-long meal relation','That does not fit the chronology.'),
 ('Asymptomatic celiac seropositivity as a definitive diagnosis without testing','The clinical vascular syndrome needs assessment.')],
 'Postprandial demand can expose inadequate mesenteric flow reserve',
 '**Meal-related pain and food fear are characteristic clues.**',
 ['Atherosclerotic stenoses are a common cause.', 'Anatomical stenosis alone is not sufficient without a compatible clinical assessment.'],
 '**Use mesenteric vascular imaging and specialist review.**',
 ['Exclude important gastrointestinal mimics.', 'Revascularization can be appropriate for symptomatic confirmed disease; diet avoidance alone does not solve the perfusion problem.'],
 [['Clinical triad','Postprandial pain, food fear, weight loss'],['Vascular imaging','Defines stenotic disease'],['Treatment','Cause and revascularization assessment']], [AMI], 'clinical_scenario')
q('A patient with suspected acute mesenteric ischemia now has generalized peritonitis. What is the appropriate operative principle?',
 'Immediate surgical exploration and viability/source-control assessment without delaying for nonessential testing',[
 ('Wait for serial lactate values to prove necrosis','Peritonitis already indicates a dangerous advanced process.'),
 ('Continue outpatient observation because the pain has become more localized','Peritoneal signs require emergency care.'),
 ('Use capsule endoscopy as the first emergency viability test','That is inappropriate in suspected necrosis and possible obstruction.')],
 'Peritonitis changes the urgency',
 '**Advanced intestinal ischemia with peritoneal signs mandates surgery without delay.**',
 ['Resuscitation, antimicrobials and perfusion planning occur in parallel.', 'The operation assesses viable bowel and the need for revascularization or resection.'],
 '**Preserve bowel when safely possible.**',
 ['A second-look strategy can help in selected uncertain viability.', 'Early CTA is important before this stage, but should not become a reason to postpone necessary emergency surgery.'],
 [['Suspected early AMI','Urgent CTA'],['Generalized peritonitis','Emergency operation'],['Viability uncertainty','Selected second-look planning']], [AMI], 'clinical_scenario')

if __name__=='__main__':
    finalize('GI & pancreas',3,'Small Intestine and Malabsorption','gi-small-intestine',rows,32)
