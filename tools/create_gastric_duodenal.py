"""Original Gastric and Duodenal Disorders chapter."""
from qbank_authoring import question,ref,finalize
HP=ref('ACG 2024 H. pylori Treatment Guideline Highlights','https://webfiles.gi.org/links/journals/ACG-Hpylori-Guidelines-Highlights-2024-FINAL.pdf')
UG=ref('ACG 2021 Upper GI and Ulcer Bleeding Guideline','https://doi.org/10.14309/ajg.0000000000001245')
AG=ref('AGA 2021 Atrophic Gastritis Clinical Practice Update','https://doi.org/10.1053/j.gastro.2021.06.078')
MAPS=ref('ESGE/EHMSG/ESP MAPS III Guideline (2025)','https://www.esge.com/management-of-epithelial-precancerous-conditions-and-early-neoplasia-of-the-stomach-maps-iii-esge-ehmsg-esp-guideline-update-2025')
GP=ref('AGA 2025 Gastroparesis Guideline','https://gastro.org/clinical-guidance/clinical-guidance-on-the-management-of-gastroparesis/')
Z=ref('NIDDK: Zollinger-Ellison Syndrome','https://www.niddk.nih.gov/health-information/digestive-diseases/zollinger-ellison-syndrome')
rows=[]
def q(*args,**kwargs):rows.append(question(*args,**kwargs))

q('A treatment-naive patient has confirmed H. pylori, unknown antibiotic susceptibility and no relevant contraindication. Under the 2024 ACG approach, which empirical regimen is preferred among these options?',
 'Optimized bismuth quadruple therapy for 14 days',[
 ('Empirical PPI-clarithromycin-amoxicillin triple therapy regardless of resistance','Clarithromycin-based treatment should not be used empirically when susceptibility is unknown in this framework.'),
 ('PPI monotherapy for 14 days','Acid suppression alone does not eradicate the organism.'),
 ('Metronidazole alone for seven days','Single-antibiotic therapy is not an adequate eradication strategy.')],
 'Resistance patterns determine a modern empirical regimen',
 '**Optimized BQT combines acid suppression, bismuth, tetracycline and metronidazole.**',
 ['The ACG preferred duration is 14 days.', 'Pill burden, dosing explanation and adherence are important determinants of success.'],
 '**Plan confirmation of eradication at the time treatment is prescribed.**',
 ['Symptoms do not reliably establish cure.', 'Review previous antibiotic exposure and allergy before selecting alternatives.'],
 [['Optimized BQT','Four-component 14-day regimen'],['Clarithromycin triple','Requires suitable susceptibility context'],['PPI alone','Symptom treatment, not eradication']], [HP], 'clinical_scenario')
q('A urea breath test is negative while a patient is taking a PPI after recent H. pylori treatment. What is the main interpretive concern?',
 'Acid suppression can produce a false-negative result',[
 ('The result definitively proves eradication regardless of medication','Medication suppression can lower test sensitivity.'),
 ('A PPI causes a mandatory false-positive antibody test instead','The relevant problem is false-negative active-infection testing.'),
 ('No preparation is needed for any H. pylori test','Preparation depends on the test and recent medication.')],
 'Testing conditions affect apparent cure',
 '**Hold a PPI or PCAB for about two weeks before an appropriate test of cure when feasible.**',
 ['Antibiotics and bismuth should generally be absent for at least four weeks.', 'Use a safe symptom-bridging strategy if needed.'],
 '**Repeat a potentially suppressed negative test correctly.**',
 ['A breath or suitable stool antigen test assesses current infection.', 'Serology can remain positive after cure and is not the preferred confirmation method.'],
 [['PPI/PCAB exposure','False-negative concern'],['Antibiotic/bismuth exposure','Also suppresses detection'],['Serology','Not a reliable cure test']], [HP], 'clinical_scenario')
q('When should eradication generally be confirmed after H. pylori therapy?',
 'At least four weeks after antibiotics, with appropriate PPI/PCAB withholding before testing',[
 ('The morning after the last antibiotic dose','Suppression can make early testing misleading.'),
 ('Only if pain persists','Asymptomatic persistent infection still matters.'),
 ('By a persistently positive IgG antibody as proof of treatment failure','Antibodies may remain positive after successful eradication.')],
 'Every treated infection needs a cure assessment',
 '**Use a urea breath test, validated stool antigen test or an appropriately indicated biopsy-based method.**',
 ['The minimum post-antibiotic interval is generally four weeks.', 'Withhold PPI/PCAB for about two weeks and bismuth/antibiotics for four weeks.'],
 '**Clinical improvement is not microbiological confirmation.**',
 ['Persistent infection influences ulcer and gastric cancer risk.', 'A failed test should trigger an exposure- and susceptibility-informed rescue strategy.'],
 [['Symptoms improved','Does not prove cure'],['Active-infection test at correct interval','Appropriate confirmation'],['Antibody persistence','Can outlast infection']], [HP])
q('H. pylori persists after an adherent optimized BQT course. The patient has no penicillin allergy and has not received rifabutin. Which empirical rescue option is supported by the 2024 ACG framework?',
 'Rifabutin-based triple therapy with acid suppression and amoxicillin',[
 ('Repeat an identical failed regimen indefinitely without reassessment','Prior regimen quality and failure need review; simply repeating the same course is not the default response.'),
 ('Empirical clarithromycin triple therapy despite unknown susceptibility','Resistance-guided use is important.'),
 ('Amoxicillin alone without effective acid suppression','This is not the supported rifabutin triple regimen.')],
 'Rescue therapy must account for prior treatment',
 '**Rifabutin triple therapy is a supported option after prior optimized BQT in an appropriate patient.**',
 ['Check adherence, actual doses and previous antibiotics.', 'Persistent failure can require susceptibility-directed treatment.'],
 '**Do not treat every rescue episode as a treatment-naive infection.**',
 ['Drug toxicity, availability and local expertise affect selection.', 'Confirm eradication again after the rescue course.'],
 [['Prior optimized BQT failure','Consider suitable rifabutin triple'],['Unknown clarithromycin sensitivity','Avoid blind clarithromycin rescue'],['Repeated failure','Susceptibility-guided assessment']], [HP,ref('US VA 2024 H. pylori Clinical Recommendations','https://www.va.gov/formularyadvisor/DOC_PDF/CRE_H_Pylori_Clinical_Recommendations_Nov_2024.pdf')], 'clinical_scenario')
q('Which condition best supports selecting a clarithromycin-containing H. pylori regimen under current ACG guidance?',
 'Demonstrated clarithromycin susceptibility with an otherwise appropriate regimen',[
 ('Unknown susceptibility and previous macrolide exposure','This increases concern about resistance rather than supporting empirical use.'),
 ('Failure of the same regimen with no new information','Repeating known failure is not an appropriate default.'),
 ('Symptom severity alone regardless of resistance','Symptoms do not predict antibiotic susceptibility.')],
 'Antibiotic selection should be susceptibility informed',
 '**Clarithromycin resistance substantially reduces success of traditional triple therapy.**',
 ['Previous macrolide exposure is relevant.', 'Validated molecular or culture-based information can guide a suitable choice.'],
 '**Distinguish a convenient regimen from a likely effective one.**',
 ['Explain adherence requirements and adverse effects.', 'A cure test remains necessary even when susceptibility is known.'],
 [['Known susceptible strain','May support clarithromycin use'],['Unknown resistance','Prefer an appropriate empirical alternative'],['Cure confirmation','Required after treatment']], [HP])
q('A patient has localized low-grade gastric MALT lymphoma and H. pylori infection, without an immediate need for oncological rescue. What is an important initial treatment?',
 'H. pylori eradication with hematology and endoscopic follow-up',[
 ('PPI alone as definitive lymphoma treatment','The organism must be eradicated when present; acid suppression alone is insufficient.'),
 ('Immediate gastrectomy in every localized case','Many suitable cases can regress after eradication and do not require routine immediate surgery.'),
 ('No follow-up after symptoms improve','Histological lymphoma response can lag and requires structured assessment.')],
 'An antigen-driven lymphoma can regress after removing the stimulus',
 '**H. pylori is a clinically actionable driver in many gastric MALT cases.**',
 ['Stage, histology and molecular features influence response and further treatment.', 'Failure to regress or adverse disease features can require lymphoma-directed therapy.'],
 '**Confirm both infection cure and lymphoma response.**',
 ['The time course of histological regression differs from symptom relief.', 'Coordinate specialist surveillance rather than assuming eradication ends oncological care.'],
 [['H. pylori-positive gastric MALT','Eradication is important'],['Persistent/adverse lymphoma','Assess additional oncological treatment'],['Follow-up','Infection and histological response']], [HP,ref('ESMO Marginal Zone Lymphoma Clinical Practice Guideline','https://doi.org/10.1016/j.annonc.2019.10.010')], 'clinical_scenario')
q('How do NSAIDs contribute to peptic ulcer formation?',
 'Cyclooxygenase inhibition reduces protective mucosal prostaglandin effects',[
 ('They directly eradicate H. pylori','NSAIDs are not eradication treatment.'),
 ('They uniformly increase mucus and bicarbonate secretion','Prostaglandin suppression reduces important protective mechanisms.'),
 ('They act only by increasing gastrin from a tumor','That is a different hypersecretory mechanism.')],
 'Mucosal defense is as important as acid',
 '**Reduced prostaglandin activity impairs mucus, bicarbonate and mucosal perfusion defenses.**',
 ['Topical injury and other factors also contribute.', 'H. pylori and NSAID exposure can coexist.'],
 '**Reduce risk according to the patient\'s bleeding history and ongoing need.**',
 ['Avoid unnecessary NSAIDs and use appropriate gastroprotection when indicated.', 'Eradication does not eliminate every risk from continued NSAID exposure.'],
 [['NSAID injury','Reduced mucosal defense'],['H. pylori','Separate treatable contributor'],['Prevention','Exposure review and risk-based protection']], [UG,HP])
q('A gastric ulcer is found in an older patient. Why is biopsy and appropriate healing reassessment important?',
 'Gastric malignancy can present as an ulcer and may be missed by limited initial sampling',[
 ('Every gastric ulcer is malignant','Many are benign, but malignancy must be considered.'),
 ('A PPI response definitively excludes cancer','Symptom improvement or partial healing does not replace adequate assessment.'),
 ('Only duodenal ulcers can have complications','Gastric ulcers can bleed, obstruct, perforate or harbor malignancy.')],
 'A gastric ulcer is a lesion requiring an etiological diagnosis',
 '**Endoscopic appearance alone may not reliably exclude malignancy.**',
 ['Obtain adequate biopsies when safe and reassess nonhealing or suspicious lesions.', 'H. pylori and medication exposure should be evaluated.'],
 '**Tailor follow-up to risk and examination quality.**',
 ['Persistent symptoms, weight loss, anemia or incomplete healing strengthen the need for repeat assessment.', 'Do not apply a benign label without considering the sampling and clinical context.'],
 [['Benign ulcer causes','H. pylori, NSAID and others'],['Malignant ulcer','Requires histology and staging'],['Nonhealing lesion','Repeat targeted assessment']], [ref('ASGE: The Role of Endoscopy in Peptic Ulcer Disease','https://doi.org/10.1016/j.gie.2009.11.026')], 'clinical_scenario')
q('A posterior duodenal bulb ulcer causes major arterial bleeding. Which vessel is classically at risk?',
 'Gastroduodenal artery',[
 ('Left gastric artery','This is more associated with the lesser-curvature gastric supply than the classic posterior duodenal relationship.'),
 ('Splenic artery','It is not the usual vessel immediately behind the duodenal bulb.'),
 ('Inferior mesenteric artery','This supplies a different intestinal territory.')],
 'Ulcer anatomy can predict the bleeding source',
 '**The gastroduodenal artery lies close to the posterior duodenal bulb.**',
 ['Erosion can produce brisk hemorrhage.', 'Anterior duodenal ulcers are classically associated with free perforation.'],
 '**Use the anatomical clue within an active resuscitation pathway.**',
 ['Endoscopic hemostasis is attempted when appropriate.', 'Failed control can require angiographic embolization or surgery.'],
 [['Posterior duodenal ulcer','Gastroduodenal bleeding risk'],['Anterior duodenal ulcer','Perforation association'],['Persistent hemorrhage','Escalate source control']], [UG])
q('A patient with longstanding peptic disease has persistent nonbilious vomiting, early satiety and gastric outlet obstruction. Which biochemical pattern is characteristic after substantial gastric losses?',
 'Hypochloremic hypokalemic metabolic alkalosis',[
 ('Hyperchloremic metabolic acidosis as the usual gastric-loss pattern','Loss of gastric acid usually produces alkalosis rather than this pattern.'),
 ('An isolated respiratory alkalosis with no volume effect','Volume and electrolyte depletion are central.'),
 ('Hyperkalemic normal-anion-gap acidosis as the typical result','That does not match the expected acid and potassium losses.')],
 'Gastric acid loss and volume contraction shape the chemistry',
 '**Hydrogen and chloride loss promotes alkalosis.**',
 ['Volume contraction and aldosterone effects can maintain alkalosis and potassium depletion.', 'Severe depletion requires careful replacement.'],
 '**Stabilize before definitive obstruction treatment.**',
 ['Assess decompression, fluids, potassium and the cause of obstruction.', 'Malignancy must be excluded rather than assuming every obstruction is peptic scarring.'],
 [['Gastric acid loss','Alkalosis and chloride depletion'],['Volume contraction','Maintains renal bicarbonate retention'],['Cause assessment','Benign scar versus malignant obstruction']], [ref('ASGE Guideline: Benign and Malignant Gastroduodenal Obstruction','https://doi.org/10.1016/j.gie.2020.07.063')], 'clinical_scenario')
q('A hemodynamically stable patient with an upper GI bleed has a Glasgow-Blatchford score of 0 and reliable follow-up. What does this score support?',
 'Consideration of outpatient management after appropriate clinical assessment',[
 ('Mandatory ICU admission solely from the score','A score of 0 identifies a very-low-risk group rather than an ICU mandate.'),
 ('No investigation or follow-up is ever needed','Low immediate risk does not eliminate the need to address the cause.'),
 ('Immediate surgery before endoscopy','The risk profile does not justify this routine approach.')],
 'A pre-endoscopic score can identify very-low-risk bleeding',
 '**ACG supports outpatient consideration for very-low-risk patients such as GBS 0-1.**',
 ['Clinical judgment and a safe follow-up plan remain necessary.', 'The score does not identify the bleeding lesion itself.'],
 '**Separate disposition from etiological follow-up.**',
 ['Provide instructions for recurrent bleeding or deterioration.', 'Medication and ulcer-risk review remain important.'],
 [['GBS 0-1','Very-low-risk disposition consideration'],['Instability or adverse features','Resuscitation and admission pathway'],['Follow-up','Cause-directed care']], [UG], 'clinical_scenario')
q('A stable hospitalized patient with nonvariceal upper GI bleeding has no ACS or other reason for a higher individualized threshold. Which hemoglobin threshold reflects the ACG restrictive transfusion recommendation?',
 'About 7 g/dL',[
 ('10 g/dL in every patient','A routine liberal threshold is not the recommendation for the stated population.'),
 ('12 g/dL in every patient','This is substantially more liberal than the guideline approach.'),
 ('Never transfuse if the bleeding is nonvariceal','Transfusion remains necessary when indicated.')],
 'Restrictive transfusion is a default, not a substitute for resuscitation',
 '**The ACG threshold is approximately 7 g/dL in the stated context.**',
 ['Active massive hemorrhage and clinical perfusion require judgment because an early hemoglobin can lag blood loss.', 'ACS and significant cardiovascular circumstances can justify a different individualized strategy.'],
 '**Treat the patient and bleeding source.**',
 ['Monitor hemodynamics and ongoing loss.', 'Avoid applying a stable-patient number rigidly to exsanguinating shock.'],
 [['Stable usual UGIB context','Restrictive threshold around 7'],['Massive ongoing loss','Perfusion-guided resuscitation'],['ACS/selected comorbidity','Individualized threshold']], [UG])
q('After initial resuscitation, when should upper endoscopy generally occur for a hospitalized patient with overt nonvariceal upper GI bleeding?',
 'Within 24 hours of presentation',[
 ('Before any resuscitation regardless of instability','Stabilization and airway/perfusion assessment come first.'),
 ('Routinely after one week in every patient','That delays appropriate diagnosis and hemostasis.'),
 ('Only if a stool occult-blood test becomes positive','Overt bleeding does not require occult testing to justify endoscopy.')],
 'Timely endoscopy follows initial stabilization',
 '**Endoscopy within 24 hours is the general hospitalized UGIB recommendation.**',
 ['The exact urgency depends on ongoing bleeding and stability.', 'Do not substitute a timing target for adequate resuscitation.'],
 '**Use endoscopic findings to guide subsequent risk care.**',
 ['High-risk stigmata can require hemostasis and intensive PPI treatment.', 'A clean base has a different rebleeding risk and management pathway.'],
 [['Initial phase','Resuscitate and assess'],['General endoscopy target','Within 24 hours'],['After endoscopy','Stigma-based treatment']], [UG], 'clinical_scenario')
q('A bleeding ulcer has a nonbleeding visible vessel, Forrest IIa. What is the appropriate endoscopic principle?',
 'Apply endoscopic hemostatic treatment',[
 ('No treatment because bleeding has stopped at that instant','A visible vessel is a high-risk stigma for rebleeding.'),
 ('Treat it like a clean-base Forrest III ulcer','The risk categories differ.'),
 ('Use biopsy alone as definitive vascular hemostasis','Sampling does not provide appropriate hemostatic treatment.')],
 'A visible vessel remains high risk without active spurting',
 '**Forrest IIa warrants endoscopic hemostasis.**',
 ['Mechanical or thermal methods are selected according to lesion and expertise.', 'Active spurting and oozing also require treatment.'],
 '**Follow hemostasis with appropriate acid suppression.**',
 ['Assess H. pylori and NSAID exposure to reduce recurrence.', 'A low-risk clean base does not require the same intervention.'],
 [['Ia/Ib','Active bleeding'],['IIa','Nonbleeding visible vessel; treat'],['III','Clean base; lower rebleeding risk']], [UG])

# Rebleeding, hypersecretion, premalignant disease and gastric motor disorders follow.
q('An actively bleeding ulcer is injected with epinephrine and bleeding slows. What should usually follow?',
 'A definitive additional mechanical or thermal hemostatic method',[
 ('End the procedure because epinephrine alone is sufficient durable treatment','Epinephrine injection should not be the sole hemostatic modality.'),
 ('Give oral antacid only as a substitute for vessel treatment','That does not provide definitive hemostasis.'),
 ('Apply fibrinolysis to expose the vessel','That would promote rather than control bleeding.')],
 'Temporary vasoconstriction and tamponade are not enough',
 '**Epinephrine can improve visualization but monotherapy has a higher rebleeding concern.**',
 ['Combine with an appropriate mechanical or thermal technique.', 'The lesion position and vessel characteristics affect method choice.'],
 '**Continue post-hemostasis risk management.**',
 ['Use appropriate high-dose PPI treatment for a high-risk ulcer.', 'Identify and treat H. pylori and avoid unnecessary ulcerogenic medication.'],
 [['Epinephrine','Adjunctive temporary control'],['Clip/thermal method','Definitive additional hemostasis'],['Afterward','PPI and cause-directed prevention']], [UG], 'clinical_scenario')
q('After successful endoscopic treatment of a high-risk bleeding ulcer, which acid-suppression strategy is recommended initially?',
 'High-dose PPI therapy for about 72 hours using an appropriate continuous or intermittent regimen',[
 ('A single antacid dose as equivalent protection','This is not equivalent to the recommended post-hemostasis acid suppression.'),
 ('No PPI if the visible vessel is no longer bleeding','Rebleeding risk remains after successful local treatment.'),
 ('Antibiotics alone regardless of H. pylori status','Antibiotics do not replace immediate acid suppression.')],
 'Clot stability benefits from effective acid suppression',
 '**High-risk endoscopic stigmata justify intensive initial PPI treatment.**',
 ['ACG accepts appropriate continuous or intermittent high-dose regimens.', 'Subsequent oral treatment depends on risk and ulcer context.'],
 '**Do not use a low-risk clean-base pathway for a treated vessel.**',
 ['Monitor for recurrent bleeding and hemodynamic change.', 'Longer-term healing and risk-factor treatment remain necessary.'],
 [['Treated high-risk ulcer','Initial high-dose PPI'],['Continuous/intermittent','Validated regimens can be used'],['Clean-base ulcer','Different risk-intensity pathway']], [UG])
q('A patient rebleeds after initially successful endoscopic ulcer hemostasis and can undergo another procedure. What is generally the next source-control step?',
 'Repeat endoscopy with further hemostatic treatment',[
 ('Immediate surgery in every patient before reassessment','Repeat endoscopic therapy is generally suggested first when feasible.'),
 ('Only repeat a stool occult-blood test','Overt recurrent bleeding needs active management.'),
 ('Observe without intervention because one treatment has already been attempted','Recurrent bleeding requires reassessment and control.')],
 'Recurrent bleeding does not automatically mean endoscopy has no further role',
 '**Repeat endoscopic treatment can control recurrent ulcer hemorrhage.**',
 ['Newer mechanical approaches may be useful according to the lesion.', 'Resuscitation and airway/perfusion assessment remain immediate priorities.'],
 '**Escalate when endoscopic control fails.**',
 ['Transcatheter arterial embolization is an important next option.', 'Surgery is selected according to failure, availability and the clinical state.'],
 [['First recurrence when feasible','Repeat endoscopic hemostasis'],['Endoscopic failure','Consider arterial embolization'],['Persistent uncontrolled bleeding','Multidisciplinary rescue including surgery']], [UG], 'clinical_scenario')
q('A patient with recurrent distal duodenal ulcers and diarrhea has fasting hypergastrinemia. Which additional finding supports Zollinger-Ellison physiology rather than achlorhydric autoimmune gastritis?',
 'Inappropriately high gastrin despite an acidic gastric lumen',[
 ('Markedly high gastric pH with corpus atrophy','That supports a compensatory hypergastrinemia from reduced acid.'),
 ('Hypergastrinemia during PPI treatment as definitive proof by itself','PPI-associated acid suppression can raise gastrin and confound diagnosis.'),
 ('Vitamin B12 deficiency alone as a gastrinoma-specific marker','B12 deficiency can accompany autoimmune atrophic disease.')],
 'Interpret gastrin in relation to acid',
 '**ZES is inappropriate gastrin secretion with acid hypersecretion.**',
 ['High gastrin alone is not diagnostic.', 'PPI use and achlorhydria can cause appropriate compensatory elevation.'],
 '**Use a safe specialist testing plan.**',
 ['Abrupt withdrawal of acid suppression in suspected severe ZES can be dangerous.', 'Confirm biochemistry before tumor-localization assumptions and assess MEN1 when appropriate.'],
 [['ZES','High gastrin with acid secretion'],['Autoimmune atrophy','High gastrin from low acid'],['PPI exposure','Important confounder']], [Z], 'clinical_scenario')
q('Which response is characteristic of a positive secretin stimulation test for gastrinoma in an appropriate diagnostic setting?',
 'A paradoxical rise in serum gastrin',[
 ('A mandatory fall in gastrin to zero','Gastrinoma can respond paradoxically rather than with the normal inhibitory pattern.'),
 ('A rise in insulin as the defining endpoint','The test assesses gastrin response in this context.'),
 ('Immediate eradication of H. pylori','Secretin testing is not antimicrobial treatment.')],
 'A gastrinoma can respond abnormally to secretin',
 '**Provoked gastrin elevation can support ZES when baseline testing is not conclusive.**',
 ['The test must be interpreted with gastric acid status and medication context.', 'Assay and protocol-specific criteria matter.'],
 '**A positive biochemical result precedes localization and staging.**',
 ['Duodenal and pancreatic primary sites are important.', 'Assess MEN1 features such as hyperparathyroidism where relevant.'],
 [['Secretin test','Paradoxical gastrin response'],['Acid context','Needed to interpret hypergastrinemia'],['Next phase','Localization and syndrome assessment']], [Z])
q('A patient has B12 deficiency, anti-intrinsic-factor antibodies, corpus-predominant atrophy and hypergastrinemia. Which mechanism best explains the gastrin elevation?',
 'Loss of acid-producing parietal cells removes normal acid feedback',[
 ('A gastrinoma is proven whenever gastrin is high','Achlorhydric feedback can produce substantial hypergastrinemia without a gastrinoma.'),
 ('Excess parietal-cell acid secretion from an intact corpus','The described corpus atrophy implies loss rather than excess of acid-producing capacity.'),
 ('A primary insulin-secreting tumor','That does not explain the gastric autoimmune pattern.')],
 'Autoimmune gastritis removes both acid and intrinsic-factor capacity',
 '**Parietal-cell destruction can cause hypochlorhydria or achlorhydria and pernicious anemia.**',
 ['Iron deficiency can also be present, sometimes earlier than B12 deficiency.', 'Chronic hypergastrinemia stimulates ECL-cell proliferation.'],
 '**Assess neoplastic risk as well as nutrient replacement.**',
 ['Gastric adenocarcinoma and type 1 gastric NET are relevant risks.', 'Topographical biopsies define distribution and severity.'],
 [['Parietal-cell loss','Low acid and impaired intrinsic factor'],['G-cell response','Compensatory hypergastrinemia'],['Consequences','Nutrient and neoplasia assessment']], [AG], 'clinical_scenario')
q('Under MAPS III, a patient has advanced extensive gastric intestinal metaplasia, OLGIM stage III, after a high-quality examination. What follow-up is generally recommended?',
 'High-quality surveillance endoscopy about every three years',[
 ('No surveillance regardless of extent','Advanced extensive disease has a different risk than limited low-risk antral metaplasia.'),
 ('Weekly endoscopy in every patient','That is not the recommended routine interval.'),
 ('Surveillance only if H. pylori remains positive','Eradication does not eliminate all risk once advanced premalignant change exists.')],
 'Extent and stage refine gastric cancer risk',
 '**Advanced OLGA/OLGIM III-IV or extensive antrum-and-corpus disease supports surveillance.**',
 ['MAPS III generally recommends a three-year interval.', 'Additional family or other risk factors may modify individualized follow-up.'],
 '**Eradicate H. pylori and maintain examination quality.**',
 ['Careful inspection and targeted sampling of lesions are essential.', 'Do not treat a negative infection test as reversal of all premalignant tissue risk.'],
 [['Limited low-risk change','Different surveillance decision'],['Advanced extensive stages','Generally three-year surveillance'],['H. pylori','Treat but continue risk-based assessment']], [MAPS], 'clinical_scenario')
q('When assessing suspected atrophic gastritis, why should body and antrum/incisura biopsies be placed in separately labeled containers?',
 'Topographical distribution helps distinguish patterns and stage cancer risk',[
 ('Mixing every specimen always improves anatomical localization','Mixing removes information about where changes arose.'),
 ('Only the duodenum is needed to establish corpus atrophy','The gastric regions must be sampled.'),
 ('A single serum gastrin value replaces all histology','Gastrin does not define the full mucosal distribution or grade.')],
 'Location is diagnostic information',
 '**Corpus-predominant autoimmune disease differs from multifocal H. pylori-related patterns.**',
 ['Distribution and severity inform risk stratification.', 'Target visible lesions in addition to systematic mapping.'],
 '**Preserve the link between specimen and site.**',
 ['At minimum, body and antrum/incisura should be separately identified.', 'Pathology and endoscopy findings should be reconciled.'],
 [['Body sample','Defines oxyntic involvement'],['Antrum/incisura sample','Defines distal distribution'],['Separate labeling','Preserves topographical interpretation']], [AG,MAPS])
q('A patient has chronic nausea, early satiety and vomiting. Mechanical obstruction has been excluded. Which test is preferred to establish delayed gastric emptying?',
 'A standardized four-hour solid-meal gastric emptying study',[
 ('A normal one-hour study as definitive exclusion','Short protocols can miss delayed emptying.'),
 ('Symptoms alone without objective testing','Functional dyspepsia and other disorders can produce overlapping symptoms.'),
 ('A gastric biopsy alone','Histology does not measure emptying function.')],
 'Gastroparesis requires objective delay without mechanical obstruction',
 '**The 2025 AGA guidance favors four-hour over two-hour-or-shorter testing.**',
 ['Use a standardized meal and protocol.', 'Glucose and medications that alter motility can affect the result.'],
 '**Check whether the test conditions represent baseline physiology.**',
 ['Review opioids, GLP-1-related effects and other relevant drugs.', 'A retained meal on one endoscopy is not by itself a complete diagnostic test.'],
 [['Symptoms','Compatible but nonspecific'],['Obstruction exclusion','Essential'],['Four-hour study','Objective emptying assessment']], [GP], 'clinical_scenario')
q('Which drug used for gastroparesis combines prokinetic action with central dopamine-receptor effects and carries a tardive-dyskinesia concern?',
 'Metoclopramide',[
 ('Ondansetron','It treats nausea through 5-HT3 blockade but is not the described dopamine-antagonist prokinetic.'),
 ('Erythromycin','Its prokinetic effect is through motilin-receptor activity.'),
 ('A proton pump inhibitor','Acid suppression does not provide this prokinetic mechanism.')],
 'A prokinetic benefit can carry neurological risk',
 '**Metoclopramide can improve symptoms and emptying in selected gastroparesis.**',
 ['Central dopamine blockade creates movement-disorder risk.', 'Use the lowest appropriate exposure and review duration, renal dosing and other neurological risks.'],
 '**Assess treatment benefit rather than continuing automatically.**',
 ['Discuss warning symptoms and alternatives.', 'Dietary and glycemic strategies remain important.'],
 [['Metoclopramide','Dopamine-related prokinetic and neurological risk'],['Erythromycin','Motilin agonist effect'],['Ondansetron','Antiemetic, not equivalent prokinetic']], [GP])
q('Which dietary strategy is appropriate for many patients with gastroparesis?',
 'Small-particle, low-fat meals adjusted to tolerance and nutritional needs',[
 ('Large high-fat meals as the routine way to accelerate emptying','Fat and large particles can worsen tolerance and delay emptying.'),
 ('Complete prolonged fasting without nutrition planning','Malnutrition must be avoided.'),
 ('An unrestricted high-fiber bulky diet in every patient','Large indigestible particles can be poorly tolerated.')],
 'Meal properties influence gastric handling',
 '**Smaller particles and lower fat can improve tolerance.**',
 ['Use frequent smaller meals when appropriate.', 'Liquid nutrition may be better tolerated in some patients.'],
 '**Protect nutrition and treat the broader cause.**',
 ['Monitor weight, hydration, deficiencies and glycemic control.', 'Severe failure of oral intake can require specialist nutritional support.'],
 [['Small particles','Easier gastric processing'],['Low fat','Often better tolerated'],['Severe limitation','Nutritional escalation assessment']], [GP])
q('A 35-year-old has uninvestigated dyspepsia without alarm features or increased gastric-cancer risk. Which initial strategy is generally appropriate?',
 'Noninvasive H. pylori testing and treatment if positive',[
 ('Immediate gastrectomy for every dyspeptic patient','There is no indication for that approach.'),
 ('Empirical antibiotics without documenting infection','Testing guides an eradication indication and avoids unnecessary treatment.'),
 ('Assume functional dyspepsia without assessing relevant causes','A structured initial assessment is appropriate.')],
 'Use a risk-based dyspepsia pathway',
 '**In a younger low-risk patient, test-and-treat is an appropriate initial approach.**',
 ['Older age, concerning features or a high-risk background can favor endoscopy.', 'Thresholds and risk assessment depend on the named guideline and local cancer epidemiology.'],
 '**Follow the result and clinical response.**',
 ['Confirm eradication if treated.', 'Persistent symptoms can lead to acid treatment and further evaluation rather than repeated blind antibiotics.'],
 [['Younger low-risk dyspepsia','H. pylori test-and-treat'],['Higher-risk presentation','Consider endoscopy'],['Persistent symptoms','Reassess and tailor care']], [HP,ref('ACG/CAG Dyspepsia Guideline','https://doi.org/10.1038/ajg.2017.154')], 'clinical_scenario')
q('A patient has giant gastric body folds, foveolar hyperplasia, low albumin and edema due to gastric protein loss. Which disease is most likely?',
 'Menetrier disease',[
 ('Zollinger-Ellison syndrome','It can cause large folds but typically through acid-secretory/glandular changes rather than this protein-losing foveolar pattern.'),
 ('Autoimmune atrophic gastritis','That produces oxyntic atrophy rather than the classic hypertrophic protein-losing pattern.'),
 ('Uncomplicated H. pylori dyspepsia without hypertrophic disease','That does not fully explain the characteristic morphology and protein loss.')],
 'Giant folds require a histological differential',
 '**Menetrier disease features foveolar hyperplasia and protein-losing gastropathy.**',
 ['The body/fundus pattern and relative antral sparing can help.', 'Adequate tissue is needed because superficial sampling may be insufficient.'],
 '**Exclude mimics and assess nutritional consequences.**',
 ['Lymphoma, infiltrative cancer and hypersecretory states can also enlarge folds.', 'Specialist treatment depends on severity and the confirmed diagnosis.'],
 [['Menetrier','Foveolar hyperplasia and protein loss'],['ZES','Hypersecretory glandular pattern'],['Infiltrative neoplasia','Requires adequate tissue exclusion']], [ref('Fiske et al.: Efficacy of Cetuximab in Menetrier Disease, clinical phenotype and trial','https://pmc.ncbi.nlm.nih.gov/articles/PMC3638759/')], 'clinical_scenario')
q('A gastric subepithelial spindle-cell tumor is positive for KIT and DOG1. Which diagnosis is most likely?',
 'Gastrointestinal stromal tumor',[
 ('Leiomyoma as the best fit for KIT/DOG1 positivity','Smooth-muscle markers rather than this classic pattern would support leiomyoma.'),
 ('Gastric schwannoma as the best fit','Schwannoma is usually characterized by neural markers such as S100/SOX10 rather than the typical GIST profile.'),
 ('Adenocarcinoma','An epithelial cancer has different morphology and marker context.')],
 'A subepithelial mass needs mesenchymal typing',
 '**KIT and DOG1 support GIST in the appropriate morphological context.**',
 ['Some GISTs are KIT negative, so no single stain is an absolute exclusion rule.', 'Molecular testing can guide targeted treatment.'],
 '**Risk assessment uses more than the diagnostic marker.**',
 ['Size, mitotic activity, site and rupture are important.', 'Biopsy and resection planning should minimize avoidable tumor disruption.'],
 [['GIST','KIT/DOG1-associated mesenchymal tumor'],['Leiomyoma','Smooth-muscle phenotype'],['Schwannoma','Neural marker phenotype']], [ref('NCI PDQ: Gastrointestinal Stromal Tumors Treatment','https://www.cancer.gov/types/soft-tissue-sarcoma/hp/gist-treatment-pdq')], 'clinical_scenario')

if __name__=='__main__':
    finalize('GI & pancreas',2,'Gastric and Duodenal Disorders','gi-gastric-duodenal',rows,28)
