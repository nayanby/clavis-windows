"""Original topic-based Esophageal Disorders chapter."""
from qbank_authoring import question,ref,finalize
GERD=ref('ACG 2022 Diagnosis and Management of GERD Guideline','https://pmc.ncbi.nlm.nih.gov/articles/PMC8754510/')
BE=ref('ACG 2022 Updated Barrett Esophagus Guideline','https://pmc.ncbi.nlm.nih.gov/articles/PMC10259184/')
EOE=ref('ACG 2025 Eosinophilic Esophagitis Guideline','https://doi.org/10.14309/ajg.0000000000003194')
ACH=ref('ASGE 2020 Achalasia Guideline','https://www.asge.org/docs/default-source/guidelines/asge-guideline-on-the-management-of-achalasia-2020-february-gie.pdf')
CC=ref('Chicago Classification Version 4.0 of Esophageal Motility Disorders','https://doi.org/10.1111/nmo.14058')
FOOD=ref('ASGE Management of Ingested Foreign Bodies and Food Impactions','https://doi.org/10.1016/j.gie.2010.11.010')
rows=[]
def q(*args,**kwargs):rows.append(question(*args,**kwargs))

q('A 67-year-old has progressive dysphagia that began with solids and now affects liquids, with weight loss over three months. Which initial investigation is most appropriate?',
 'Upper endoscopy with biopsy of any suspicious lesion',[
 ('High-resolution manometry before excluding structural disease','Manometry defines motor function, but progressive solid-first symptoms and weight loss require structural and malignant assessment.'),
 ('Ambulatory pH monitoring as the first test','Reflux testing does not exclude a malignant narrowing.'),
 ('An empiric PPI trial alone before investigating for several months','Alarm features should not be managed by prolonged empirical treatment alone.')],
 'Progressive mechanical-pattern dysphagia is an alarm syndrome',
 '**Solid-first progression with weight loss raises concern for an obstructing lesion.**',
 ['Cancer, peptic stricture and other structural causes require direct assessment.', 'Liquid involvement late in the course does not convert the history into a primary motility diagnosis.'],
 '**Endoscopy can establish both anatomy and histology.**',
 ['A suspicious lesion needs biopsy and subsequent staging.', 'If initial assessment is negative but suspicion remains, cross-sectional or EUS evaluation may be necessary.'],
 [['Progressive solids then liquids','Structural obstruction concern'],['Solids and liquids from onset','Suggests a motor disorder, not diagnostic alone'],['Weight loss/alarm features','Prompt endoscopic evaluation']], [GERD], 'clinical_scenario')
q('A patient coughs immediately when swallowing, has nasal regurgitation and recurrent aspiration. Which study best evaluates the suspected swallowing-phase disorder?',
 'Videofluoroscopic swallowing assessment',[
 ('Distal esophageal pH monitoring','That does not directly characterize oral and pharyngeal transfer or aspiration.'),
 ('High-resolution esophageal manometry as the sole initial aspiration study','The history localizes the problem primarily to the oropharyngeal phase.'),
 ('A routine abdominal CT','This does not provide dynamic swallowing assessment.')],
 'Localize dysphagia before selecting the test',
 '**Difficulty initiating a swallow, cough and nasal regurgitation favor oropharyngeal dysfunction.**',
 ['Dynamic swallowing assessment can identify aspiration and guide compensatory strategies.', 'Fiberoptic endoscopic evaluation of swallowing is another appropriate method in selected settings.'],
 '**Address airway and nutritional safety.**',
 ['Neurological and structural causes require directed assessment.', 'Do not assume all reported dysphagia arises from the distal esophagus.'],
 [['Oropharyngeal symptoms','Dynamic swallowing evaluation'],['Esophageal bolus hold-up','Structural/motility pathway'],['Aspiration','Safety and nutritional planning']], [ref('UEG/ESNM Clinical Recommendations for Esophageal and Oropharyngeal Dysphagia','https://doi.org/10.1002/ueg2.70062')], 'clinical_scenario')
q('Manometry shows elevated integrated relaxation pressure, absent normal peristalsis and panesophageal pressurization in at least 20% of swallows. Which achalasia subtype is most likely?',
 'Type II achalasia',[
 ('Type I achalasia','Type I has failed peristalsis without the defining panesophageal pressurization.'),
 ('Type III achalasia','Type III has premature/spastic contractions rather than this classic pressurization pattern.'),
 ('Distal esophageal spasm','DES has premature contractions with normal EGJ relaxation, not the described achalasia pattern.')],
 'Subtype the obstructed aperistaltic esophagus',
 '**Panesophageal pressurization distinguishes type II within an achalasia pattern.**',
 ['Type I is the low-pressurization aperistaltic form.', 'Type III includes spastic premature contractions and needs tailored myotomy planning.'],
 '**Interpret manometry after excluding a mechanical obstruction.**',
 ['Endoscopy is important in the achalasia work-up.', 'Supportive barium or FLIP data can clarify an inconclusive study.'],
 [['Type I','Failed peristalsis, little pressurization'],['Type II','Panesophageal pressurization'],['Type III','Spastic/premature contractions']], [ACH,CC])
q('A patient has type III achalasia with a long spastic esophageal segment and is suitable for definitive therapy. Which approach particularly allows tailoring a long proximal myotomy?',
 'Peroral endoscopic myotomy',[
 ('Botulinum toxin as the most durable option in every fit patient','Botulinum toxin is usually reserved for selected patients who cannot undergo more durable treatment.'),
 ('Pneumatic dilation as an equally reliable treatment of every long spastic segment','A long spastic component favors a tailored myotomy strategy.'),
 ('Fundoplication alone without disrupting the outflow obstruction','An antireflux wrap alone does not treat achalasia and can worsen obstruction.')],
 'Spastic achalasia requires more than opening the LES alone',
 '**POEM allows a myotomy length adapted to the spastic segment.**',
 ['Tailored surgical myotomy can also be appropriate in expert hands.', 'Types I and II have different comparative treatment considerations.'],
 '**Discuss reflux as part of the treatment trade-off.**',
 ['POEM can increase postprocedure reflux and may require acid treatment and follow-up.', 'Choose based on anatomy, expertise, preferences and comorbidity.'],
 [['Type III','Longer tailored myotomy often favored'],['Types I/II','Several effective definitive options'],['POEM trade-off','Postprocedure reflux concern']], [ACH], 'clinical_scenario')
q('A 74-year-old has an achalasia-like manometric pattern but rapid weight loss, a short symptom history and difficult passage across the EGJ. Initial mucosal biopsies are negative. What is the next priority?',
 'Evaluate for pseudoachalasia with targeted CT and/or EUS assessment',[
 ('Proceed to routine myotomy without further structural assessment','Malignancy-related obstruction must be considered before irreversible therapy.'),
 ('Declare cancer excluded because superficial biopsies were negative','Infiltrative or extrinsic disease may not be captured by routine mucosal biopsies.'),
 ('Use pH testing as the definitive pseudoachalasia exclusion test','Acid exposure does not exclude infiltrative EGJ disease.')],
 'A motor pattern can be secondary to an obstructing process',
 '**Older age, rapid progression and marked weight loss raise suspicion for pseudoachalasia.**',
 ['Gastric cardia or EGJ malignancy can mimic impaired relaxation and aperistalsis.', 'A seemingly normal mucosa does not exclude submucosal infiltration.'],
 '**Resolve the cause before disrupting the LES.**',
 ['Use repeat targeted endoscopy, EUS or cross-sectional imaging according to findings.', 'The treatment of a malignant obstruction differs fundamentally from primary achalasia.'],
 [['Primary achalasia','Neuromuscular outflow disorder'],['Pseudoachalasia','Secondary obstructive/infiltrative process'],['Red flags','Rapid course, weight loss, difficult EGJ passage']], [ACH], 'clinical_scenario')
q('After achalasia treatment, dysphagia returns. Which investigation provides a useful objective assessment of esophageal emptying?',
 'Timed barium esophagram',[
 ('A symptom score alone as a complete anatomical assessment','Symptoms are important but do not quantify retained barium or define the mechanism.'),
 ('A routine stool test','It does not assess esophageal emptying.'),
 ('A fasting serum gastrin level','This does not quantify emptying after achalasia treatment.')],
 'Measure functional emptying after treatment',
 '**A timed barium study quantifies retention at defined intervals.**',
 ['It can identify persistent outflow limitation or poor emptying.', 'Reflux stricture, incomplete myotomy and progressive dilation are different possible causes of recurrence.'],
 '**Select additional tests to identify the cause.**',
 ['Endoscopy, manometry or FLIP may be complementary.', 'Do not assume every recurrent symptom requires repeating the same procedure.'],
 [['Timed barium','Objective emptying'],['Endoscopy','Mucosal and structural causes'],['Manometry/FLIP','Pressure and junction-opening physiology']], [ACH])
q('Manometry reports EGJ outflow obstruction with preserved peristalsis. Under Chicago v4.0, what is needed before calling this a clinically relevant obstructive disorder?',
 'Compatible symptoms and supportive evidence of obstruction, such as timed barium with tablet or FLIP',[
 ('A single elevated supine IRP as sufficient proof for myotomy','Position, artifact and secondary causes can produce an isolated elevated value.'),
 ('Normal symptoms as proof that irreversible treatment is required','An incidental manometric pattern is not automatically a clinical disease.'),
 ('A positive reflux symptom questionnaire as the only supporting test','That does not establish EGJ opening obstruction.')],
 'A manometric pattern can be inconclusive clinically',
 '**CCv4.0 requires correlation rather than treating every EGJOO label.**',
 ['Dysphagia or noncardiac chest pain provides the relevant symptom context.', 'Structural lesions, opioid effects and technical factors should be assessed.'],
 '**Seek corroboration before irreversible therapy.**',
 ['A tablet timed barium study and/or FLIP can show impaired emptying or opening.', 'An inconclusive finding may warrant follow-up rather than immediate LES disruption.'],
 [['Manometry alone','May be clinically inconclusive'],['Symptoms plus supportive obstruction','Establishes relevance'],['Treatment','Cause- and evidence-based']], [CC])
q('Manometry shows normal EGJ relaxation and premature distal contractions in at least 20% of swallows, with appropriate symptoms. Which disorder fits?',
 'Distal esophageal spasm',[
 ('Type III achalasia','Achalasia includes impaired EGJ relaxation and absent normal peristalsis.'),
 ('Absent contractility','That has failed contractions rather than premature propagated activity.'),
 ('Hypercontractile esophagus defined only by high amplitude','Hypercontractility concerns vigor, whereas DES concerns premature timing.')],
 'Timing and vigor identify different motor disorders',
 '**Premature contraction is defined by short distal latency in the appropriate contraction.**',
 ['A distal latency below 4.5 seconds is the conventional timing threshold.', 'Normal EGJ relaxation helps distinguish DES from type III achalasia.'],
 '**Exclude secondary and mechanical contributors.**',
 ['Opioid exposure and obstruction can affect patterns.', 'Symptoms and supportive clinical assessment prevent overdiagnosis from isolated manometric findings.'],
 [['DES','Premature timing with normal EGJ relaxation'],['Type III achalasia','Spasm plus impaired relaxation'],['Hypercontractility','Excessive vigor rather than timing alone']], [CC])

# Reflux, Barrett, EoE and complications follow.
q('A patient has typical heartburn and regurgitation without dysphagia, bleeding, weight loss or other alarm features. Under the ACG GERD approach, what is an appropriate initial strategy?',
 'An eight-week once-daily PPI trial before a meal',[
 ('Immediate manometry as the routine first diagnostic step','Manometry is not the usual first test for uncomplicated typical reflux symptoms.'),
 ('Immediate antireflux surgery based on symptoms alone','Objective confirmation and preprocedural assessment are required before an invasive strategy.'),
 ('Empiric antibiotics for presumed esophageal infection','The typical uncomplicated syndrome does not suggest an infectious indication.')],
 'Typical low-risk reflux symptoms permit an empirical first step',
 '**A properly administered PPI trial is reasonable without immediate invasive testing in this setting.**',
 ['Alarm features change the pathway to prompt evaluation.', 'Weight management, meal timing and symptom-specific lifestyle measures complement treatment.'],
 '**Reassess rather than treating the trial as a permanent diagnosis.**',
 ['Persistent or recurrent symptoms can require endoscopy or objective reflux testing.', 'A symptomatic response is useful but not perfectly specific for GERD.'],
 [['Typical symptoms without alarms','Empirical PPI trial'],['Alarm features','Endoscopic evaluation'],['Uncertain persistent symptoms','Objective assessment']], [GERD], 'clinical_scenario')
q('A patient with longstanding reflux now reports new progressive dysphagia. What is the appropriate next step?',
 'Upper endoscopy rather than simply escalating empirical acid suppression',[
 ('A higher PPI dose alone with no structural assessment','New dysphagia can indicate stricture, cancer or another structural process.'),
 ('Reflux symptom scoring as an adequate exclusion of malignancy','A questionnaire cannot exclude an obstructing lesion.'),
 ('Routine manometry before evaluating the mucosa and lumen','Structural disease should be assessed first in this alarm presentation.')],
 'A new alarm symptom changes an established reflux pathway',
 '**Do not assume every new symptom is uncomplicated GERD.**',
 ['Dysphagia, bleeding, weight loss and anemia warrant evaluation.', 'Endoscopy can detect stricture, erosive disease, neoplasia and features suggesting EoE.'],
 '**Use biopsy and further testing according to the finding.**',
 ['A normal-appearing lumen does not eliminate the need for esophageal biopsy when EoE is suspected.', 'Motility assessment follows when structural and inflammatory causes do not explain symptoms.'],
 [['New dysphagia','Endoscopy'],['Persistent typical symptoms alone','Optimize and investigate as appropriate'],['Unexplained after endoscopy','Consider motility pathway']], [GERD], 'clinical_scenario')
q('When should a conventional once-daily PPI generally be taken to optimize acid suppression?',
 'About 30-60 minutes before a meal, usually breakfast',[
 ('At bedtime regardless of meals as the standard optimal schedule','For conventional PPIs, premeal activation timing is generally more effective.'),
 ('Only after heartburn is already severe each day','A scheduled course is usually intended for the prescribed therapeutic trial.'),
 ('With an antacid two hours after every meal as a required activation step','That is not the usual PPI activation strategy.')],
 'Administration timing can cause apparent treatment failure',
 '**Meal-related proton pump activation helps explain the premeal schedule.**',
 ['Check adherence and timing before labeling symptoms refractory.', 'Formulation-specific exceptions exist, so apply the actual product instructions.'],
 '**Optimize the basics before adding procedures or multiple drugs.**',
 ['Twice-daily treatment, when indicated, is generally timed before breakfast and the evening meal.', 'Symptoms may have a nonreflux cause even with excellent dosing.'],
 [['Conventional daily PPI','Premeal timing'],['Apparent failure','Check adherence and timing'],['Persistent symptoms','Assess mechanism']], [GERD])
q('A patient has persistent reflux-like symptoms, a normal endoscopy and no previous objective evidence of GERD. Which reflux-monitoring strategy best establishes whether pathological reflux is present?',
 'Ambulatory reflux monitoring off PPI therapy',[
 ('Impedance-pH only on twice-daily PPI as the routine first proof of previously unestablished GERD','On-treatment testing addresses residual reflux in a previously proven disease context.'),
 ('Manometry alone as a direct measure of acid exposure','Manometry measures motor physiology, not reflux exposure.'),
 ('A barium swallow alone as definitive proof of pathological acid burden','Observed reflux on a contrast study is not equivalent to ambulatory acid quantification.')],
 'Choose the test condition according to whether GERD is already proven',
 '**Off-treatment monitoring tests the baseline reflux burden.**',
 ['The diagnosis has not been established by severe erosive disease, Barrett or prior reflux testing in this stem.', 'Use a validated protocol and appropriate medication withholding.'],
 '**A negative study can redirect treatment.**',
 ['Functional heartburn and reflux hypersensitivity require different interpretation.', 'Do not move to surgery solely because symptoms persist on a PPI.'],
 [['Unproven GERD','Off-PPI reflux monitoring'],['Proven GERD with residual symptoms','Often on-treatment impedance-pH'],['Manometry','Motor and preprocedural assessment']], [GERD], 'clinical_scenario')
q('A patient has objectively proven GERD but persistent symptoms despite correctly taken twice-daily PPI. Which test can assess ongoing acid and nonacid reflux-symptom relationships?',
 'Impedance-pH monitoring on PPI therapy',[
 ('Repeating only a symptom questionnaire','It cannot establish ongoing reflux mechanisms.'),
 ('A resting ECG as a reflux exposure measurement','An ECG addresses different diagnostic questions.'),
 ('Treating every persistent symptom as proof of acid breakthrough without testing','Residual symptoms can have nonreflux mechanisms.')],
 'Persistent symptoms in proven disease require mechanism assessment',
 '**Impedance detects reflux events beyond acid-only monitoring.**',
 ['On-treatment testing evaluates the residual burden under the regimen.', 'Symptom association can support reflux hypersensitivity or ongoing reflux relevance.'],
 '**Use the result before escalating to an invasive antireflux procedure.**',
 ['Review other causes and assess motility when a procedure is planned.', 'A low acid burden does not by itself prove that every symptom is unrelated to all reflux events.'],
 [['Acid recording','Measures pH exposure'],['Impedance','Detects bolus reflux independent of acidity'],['On therapy','Tests residual mechanism in established GERD']], [GERD], 'clinical_scenario')
q('Under the ACG definition, which finding supports a Barrett esophagus diagnosis?',
 'At least 1 cm of columnar mucosa in the tubular esophagus with intestinal metaplasia on appropriate biopsy',[
 ('An isolated irregular Z line below 1 cm as a mandatory surveillance diagnosis','ACG does not routinely label this finding as Barrett requiring the standard surveillance pathway.'),
 ('Gastric intestinal metaplasia sampled below the GE junction alone','The anatomical location matters.'),
 ('Any reflux symptom without endoscopic or histological confirmation','Symptoms alone do not establish Barrett.')],
 'Barrett diagnosis has anatomical and histological components',
 '**The ACG framework requires intestinal metaplasia in an appropriate esophageal columnar segment.**',
 ['Document landmarks and segment extent carefully.', 'Biopsy sampling quality affects detection.'],
 '**Avoid an unnecessary disease label for a minimal irregular Z line.**',
 ['Diagnostic definitions differ somewhat among guideline systems.', 'Use the named framework consistently when applying surveillance intervals.'],
 [['Columnar esophagus at least 1 cm plus IM','Supports ACG Barrett diagnosis'],['Irregular Z line below 1 cm','Different routine biopsy/surveillance approach'],['Gastric IM','Different anatomical condition']], [BE])
q('Barrett biopsies are read as indefinite for dysplasia during active inflammation. What is the appropriate next strategy?',
 'Expert pathology review, optimized acid suppression and repeat endoscopy within about six months',[
 ('Immediate esophagectomy from one indefinite reading','Indefinite is not the same as confirmed invasive cancer or high-grade dysplasia.'),
 ('Ignore the result for five years regardless of inflammation','The uncertainty needs earlier clarification.'),
 ('Ablate all visible tissue without reassessing or sampling','Inflammatory atypia and true dysplasia require reliable classification.')],
 'Inflammation can obscure dysplasia assessment',
 '**Indefinite means the pathological distinction remains uncertain.**',
 ['A second expert GI pathologist should review dysplastic or uncertain findings.', 'Improve acid control before a high-quality repeat examination.'],
 '**Use the repeat diagnosis to determine subsequent care.**',
 ['Persistent indefinite findings need closer surveillance than routine low-risk NDBE.', 'Confirmed dysplasia leads to a different eradication discussion.'],
 [['Inflamed indefinite biopsy','Review and optimize treatment'],['Repeat assessment','Clarifies category'],['Confirmed neoplasia','Eradication/staging pathway']], [BE], 'clinical_scenario')
q('A Barrett segment contains a visible nodule with dysplasia. What should generally precede ablation of the remaining flat Barrett mucosa?',
 'Endoscopic resection of the visible lesion for histological staging',[
 ('Ablation of the nodule without obtaining a staging specimen','This can destroy tissue needed to determine invasion and adverse features.'),
 ('Surveillance only regardless of confirmed high-grade dysplasia','Confirmed advanced neoplasia usually warrants treatment assessment.'),
 ('A PPI response as a substitute for lesion histology','Symptom response does not stage neoplasia.')],
 'Visible neoplasia requires a resection specimen',
 '**Resection establishes depth, differentiation, margins and lymphovascular features.**',
 ['These findings can change whether endoscopic treatment is sufficient.', 'Flat residual Barrett can then be ablated in an appropriate eradication strategy.'],
 '**Choose the resection technique by lesion characteristics.**',
 ['EMR or ESD may be appropriate depending on size, morphology and suspected invasion.', 'Do not apply a single technique without assessing the lesion.'],
 [['Visible lesion','Resect and stage'],['Flat residual dysplastic Barrett','Ablation after appropriate assessment'],['Deep/adverse invasion','Broader oncological pathway']], [BE,ref('ESGE 2023 Barrett Esophagus Guideline','https://www.esge.com/diagnosis-and-management-of-barrett-esophagus')], 'clinical_scenario')
q('Under the updated ACG length-based approach, a high-quality baseline exam confirms nondysplastic Barrett of 2 cm. What is the usual surveillance interval?',
 'Five years',[
 ('Six months','This is unnecessarily short for the stated high-quality nondysplastic short segment.'),
 ('One year','Routine annual surveillance is not the standard interval here.'),
 ('Three years','Three years is the usual ACG interval for a nondysplastic segment at least 3 cm.')],
 'Barrett length modifies nondysplastic surveillance',
 '**Shorter than 3 cm generally receives a five-year interval in the updated ACG framework.**',
 ['Segments at least 3 cm generally receive a three-year interval.', 'The recommendation assumes adequate baseline sampling and no dysplasia.'],
 '**Use the actual risk and examination quality.**',
 ['New alarm symptoms or a concerning lesion warrant earlier evaluation.', 'Indefinite or confirmed dysplasia follows a different schedule.'],
 [['NDBE below 3 cm','Five years'],['NDBE at least 3 cm','Three years'],['Dysplasia/uncertainty','Separate pathway']], [BE])
q('An adult has food impaction, rings and furrows suggesting EoE. What biopsy strategy is recommended by the 2025 ACG guideline?',
 'At least six targeted biopsies from at least two esophageal levels',[
 ('One distal biopsy only','Eosinophilic inflammation is patchy and limited sampling can miss it.'),
 ('Biopsy only the stomach and infer the esophageal diagnosis','The esophageal tissue must be assessed.'),
 ('No biopsies if rings are visible','Endoscopic appearance alone is not the complete clinicopathological diagnosis.')],
 'Patchiness determines sampling strategy',
 '**Adequate multi-level biopsies improve diagnostic sensitivity.**',
 ['Symptoms plus at least 15 eosinophils per high-power field support EoE after assessing alternative contributors.', 'A normal-looking esophagus does not exclude the disease.'],
 '**Document treatment exposure when interpreting histology.**',
 ['Effective PPI or anti-inflammatory therapy can suppress eosinophils.', 'A negative on-treatment biopsy may need context-specific reassessment.'],
 [['Sampling','At least six biopsies, two levels'],['Histology','At least 15 eos/hpf in context'],['Appearance','Supportive rather than sufficient alone']], [EOE], 'clinical_scenario')
q('A patient with an EoE clinicopathological phenotype improves on PPI treatment. Which interpretation is correct?',
 'PPI responsiveness does not exclude EoE under current criteria',[
 ('A PPI response proves the disorder was never EoE','The mandatory PPI-failure requirement has been removed.'),
 ('All PPI responders require an immediate biologic','Response can support continuing an appropriate effective treatment.'),
 ('Symptom response removes any need to assess inflammatory control','Symptoms can improve despite residual histological activity.')],
 'PPI treatment and EoE diagnosis are compatible',
 '**PPIs are a treatment option rather than a compulsory diagnostic exclusion test.**',
 ['They can have acid-related and anti-inflammatory effects.', 'The diagnosis remains based on symptoms, esophageal eosinophilia and exclusion of relevant alternatives.'],
 '**Assess more than symptom relief.**',
 ['Endoscopic and histological response matter in follow-up.', 'Maintenance treatment helps prevent recurrent inflammatory and fibrostenotic disease.'],
 [['PPI response','Does not negate EoE'],['Treatment choice','Diet, PPI, topical steroid or selected escalation'],['Monitoring','Symptoms plus objective disease activity']], [EOE])
q('A patient with EoE has a tight fibrostenotic narrowing and persistent dysphagia. Which strategy addresses both components of disease?',
 'Dilation when indicated together with anti-inflammatory treatment',[
 ('Dilation alone as a cure for the inflammatory disorder','Dilation improves caliber but does not control eosinophilic inflammation.'),
 ('Anti-inflammatory treatment alone as a guarantee that every established tight stricture will promptly open','Fixed fibrosis can need mechanical treatment.'),
 ('Avoiding all treatment because a stricture means the disease is inactive','Fibrostenosis and inflammation can coexist.')],
 'Mechanical narrowing and immune inflammation require complementary care',
 '**Dilation treats the lumen while medication or diet treats disease activity.**',
 ['Use a careful staged approach based on severity and expertise.', 'Topical swallowed steroids, PPI or dietary therapy are selected through shared decisions.'],
 '**Plan maintenance rather than a one-time procedure.**',
 ['Reassess symptoms and objective inflammation.', 'Ongoing uncontrolled disease can lead to recurrent narrowing and impaction.'],
 [['Dilation','Improves caliber'],['Anti-inflammatory therapy','Controls the underlying process'],['Long term','Maintenance and monitoring']], [EOE], 'clinical_scenario')
q('Which cytokine signaling pathway is inhibited by dupilumab in EoE?',
 'IL-4 and IL-13 signaling through blockade of IL-4 receptor alpha',[
 ('IL-1 signaling as its sole receptor target','That is not dupilumab\'s receptor mechanism.'),
 ('Platelet P2Y12 signaling','That is an antiplatelet target.'),
 ('TNF stimulation rather than inhibition','That is unrelated to the drug\'s type-2 inflammatory pathway.')],
 'Type-2 inflammation is a therapeutic target in EoE',
 '**IL-4 receptor alpha blockade affects IL-4 and IL-13 signaling.**',
 ['Dupilumab has a role in selected nonresponsive or step-up EoE care.', 'Atopic comorbidity can influence the overall treatment discussion.'],
 '**Use the current age/weight and indication-specific regimen.**',
 ['Do not assume the same dose across every disease treated with the agent.', 'Continue disease-response monitoring and address coexisting fibrostenosis.'],
 [['Dupilumab','IL-4R-alpha blockade'],['Biological effect','Reduced IL-4/IL-13 signaling'],['EoE role','Selected escalation and phenotype-based care']], [EOE])

# Obstruction, infection, perforation and oncological decisions complete the bank.
q('A patient has an esophageal food bolus impaction and cannot swallow saliva. There are no signs of perforation. What is the appropriate management?',
 'Emergent endoscopic assessment and removal with airway precautions',[
 ('Wait until the next day to see whether complete obstruction resolves','Inability to handle secretions creates aspiration risk and requires emergent care.'),
 ('Obtain a routine barium study before arranging endoscopy','Contrast can delay treatment and complicate aspiration or subsequent visualization.'),
 ('Use repeated drug attempts as a reason to postpone endoscopy indefinitely','A pharmacological trial must not delay definitive care in complete obstruction.')],
 'Complete obstruction is different from a tolerable partial impaction',
 '**Drooling or inability to manage secretions signals an emergency.**',
 ['Assess airway safety and obtain appropriate endoscopic expertise.', 'Suspected perforation changes the imaging and treatment pathway.'],
 '**Investigate the cause after safe relief.**',
 ['EoE, rings, strictures and malignancy can underlie impaction.', 'A successful extraction should not end the diagnostic plan.'],
 [['Complete obstruction','Emergent endoscopy'],['Perforation concern','Urgent imaging and multidisciplinary care'],['After relief','Assess underlying pathology']], [FOOD], 'clinical_scenario')
q('An immunocompromised patient has odynophagia and endoscopy shows adherent white esophageal plaques. Which initial systemic treatment is most appropriate for likely susceptible Candida esophagitis?',
 'Fluconazole',[
 ('Acyclovir','Acyclovir treats HSV rather than Candida.'),
 ('Ganciclovir','Ganciclovir treats CMV rather than routine susceptible Candida.'),
 ('Topical oral nystatin alone','Esophageal candidiasis requires systemic therapy; oral topical treatment alone is inadequate.')],
 'Esophageal candidiasis requires more than oral topical treatment',
 '**Plaques with an appropriate immune context suggest Candida.**',
 ['Odynophagia may be prominent.', 'Prior azole exposure and nonresponse raise resistance or alternative-diagnosis concerns.'],
 '**Use systemic treatment and reassess response.**',
 ['Persistent symptoms warrant endoscopic/tissue assessment when not already established.', 'Review immune status, interactions and the need to address the underlying predisposition.'],
 [['Candida','White plaques; systemic antifungal'],['HSV','Often discrete ulcers; antiviral pathway'],['CMV','Often larger ulcers; tissue-based diagnosis']], [ref('NIH Adult and Adolescent OI Guidelines: Mucocutaneous Candidiasis','https://clinicalinfo.hiv.gov/en/guidelines/hiv-clinical-guidelines-adult-and-adolescent-opportunistic-infections/candidiasis-mucocutaneous')], 'clinical_scenario')
q('A patient with advanced immunosuppression has large esophageal ulcers. CMV PCR is positive in a sample, but no diagnostic tissue changes have yet been demonstrated. What is the best interpretation?',
 'Compatible end-organ disease generally needs tissue evidence; viral detection alone can reflect shedding',[
 ('Any positive CMV PCR proves invasive esophagitis','Detection without compatible histopathology is not sufficient in every case.'),
 ('A negative Candida culture excludes all infectious esophagitis','Viral and other causes remain possible.'),
 ('Large ulcers prove HSV without further assessment','Appearance can suggest but does not definitively type the pathogen.')],
 'Distinguish viral presence from invasive disease',
 '**CMV esophagitis is assessed through compatible ulcers and biopsy evidence of tissue infection.**',
 ['Inclusion-bearing cells and appropriate tissue testing support the diagnosis.', 'Profound immunosuppression can permit shedding without the same end-organ syndrome.'],
 '**Target treatment to a defensible diagnosis.**',
 ['Ganciclovir-based therapy is different from the HSV or Candida regimen.', 'Assess cytopenias, kidney function and interactions during treatment planning.'],
 [['PCR or culture alone','May detect shedding'],['Compatible ulcers plus tissue infection','Supports invasive CMV'],['Treatment','Pathogen-specific and toxicity-aware']], [ref('NIH Adult and Adolescent OI Guidelines: Cytomegalovirus Disease','https://clinicalinfo.hiv.gov/en/guidelines/hiv-clinical-guidelines-adult-and-adolescent-opportunistic-infections/cytomegalovirus')], 'clinical_scenario')
q('After forceful vomiting, a patient develops severe chest pain, tachycardia and subcutaneous emphysema. Which investigation is appropriate to assess suspected esophageal perforation and mediastinal contamination?',
 'Urgent contrast-enhanced CT with an appropriate CT-esophagography protocol when feasible',[
 ('Routine ambulatory pH monitoring','This does not diagnose an acute leak or contamination.'),
 ('A normal initial chest radiograph as sufficient exclusion','An early radiograph can miss a perforation.'),
 ('Elective manometry before imaging','This delays assessment of a potentially life-threatening structural emergency.')],
 'Boerhaave syndrome is a transmural rupture emergency',
 '**Pain after vomiting with systemic or extraluminal-air signs requires urgent leak assessment.**',
 ['CT defines air, fluid, leak extent and other thoracic pathology.', 'A simple mucosal Mallory-Weiss tear more commonly presents with bleeding rather than mediastinal contamination.'],
 '**Initiate emergency multidisciplinary treatment.**',
 ['Keep the patient nil by mouth, resuscitate and arrange appropriate antimicrobials and source-control assessment.', 'Endoscopic, surgical or selected conservative management depends on location, containment, timing and stability.'],
 [['Boerhaave','Transmural rupture and contamination'],['Mallory-Weiss','Mucosal tear, typically bleeding'],['Definitive plan','Leak anatomy and clinical state']], [ref('WSES Guidelines: Esophageal Emergencies','https://pmc.ncbi.nlm.nih.gov/articles/PMC6544956/')], 'clinical_scenario')
q('Endoscopic resection of a Barrett-associated lesion shows T1a adenocarcinoma, well differentiated, clear deep margin and no lymphovascular invasion. Which treatment principle is appropriate?',
 'Endoscopic therapy can be curative in an appropriately selected low-risk mucosal cancer, with eradication of remaining Barrett when indicated',[
 ('Every T1a lesion requires neoadjuvant chemoradiation before any local assessment','Low-risk mucosal disease has a different pathway from locally advanced cancer.'),
 ('Ablation alone should replace the resection specimen needed for staging','Resection histology is what establishes the favorable features in this stem.'),
 ('The same local-only rule applies to deep submucosal invasion with lymphovascular disease','Those findings raise nodal risk and change the oncological strategy.')],
 'Depth and adverse histology determine the local-treatment window',
 '**Low-risk T1a Barrett cancer has a low enough nodal risk to permit endoscopic cure in selected patients.**',
 ['Differentiation, lymphovascular invasion and margins matter.', 'T1b disease needs a separate risk assessment rather than automatic extrapolation.'],
 '**Complete eradication and surveillance remain part of care.**',
 ['Residual Barrett may require ablation after visible lesion resection.', 'Continue expert follow-up for recurrent metaplasia or neoplasia.'],
 [['Low-risk T1a','Potential endoscopic curative pathway'],['Deep or adverse invasion','Broader oncological assessment'],['After eradication','Ongoing surveillance']], [BE,ref('ESGE 2023 Barrett Guideline','https://www.esge.com/diagnosis-and-management-of-barrett-esophagus')], 'clinical_scenario')
q('A patient with systemic sclerosis has reflux and dysphagia. Which manometric pattern is characteristic?',
 'Hypotensive LES with weak or absent distal peristalsis',[
 ('Elevated IRP with absent peristalsis as the classic achalasia pattern','That is a different outflow mechanism.'),
 ('Normal relaxation with premature contractions as the defining DES pattern','That describes spasm rather than the typical scleroderma motor deficit.'),
 ('Uniform high-vigor contractions as the obligatory hypercontractile phenotype','The usual systemic-sclerosis pattern is hypomotility.')],
 'Poor clearance and a weak antireflux barrier can coexist',
 '**Systemic sclerosis can impair distal smooth-muscle function and LES tone.**',
 ['This promotes reflux and prolongs contact with refluxate.', 'Stricture and other structural consequences must still be assessed when dysphagia is present.'],
 '**Manage reflux while recognizing limited clearance reserve.**',
 ['Optimize acid control and evaluate complications.', 'Invasive antireflux decisions require careful motility-informed planning.'],
 [['Systemic sclerosis','Low LES pressure and hypomotility'],['Achalasia','Impaired EGJ relaxation'],['DES','Premature contractions with normal relaxation']], [CC,GERD])
q('An older patient regurgitates undigested food, has halitosis and coughs several hours after meals. A cervical pouch is suspected. Which initial imaging study best defines the anatomy?',
 'A contrast swallow study',[
 ('Blind endoscopic passage without first considering the pouch','A pouch can complicate instrumentation and create perforation risk.'),
 ('Ambulatory distal pH monitoring','This does not define a cervical diverticulum.'),
 ('A gastric emptying scan as the primary pouch study','That addresses gastric rather than pharyngoesophageal anatomy.')],
 'Zenker diverticulum can retain food above the esophagus',
 '**A pharyngoesophageal pouch can cause delayed regurgitation, halitosis and aspiration.**',
 ['Contrast imaging demonstrates size, location and the relationship to swallowing.', 'The disorder is related to upper sphincter outflow mechanics.'],
 '**Plan treatment with anatomy and expertise in mind.**',
 ['Endoscopic or surgical approaches address the septum and cricopharyngeal component in selected symptomatic patients.', 'Avoid attributing retained-food regurgitation automatically to uncomplicated GERD.'],
 [['Zenker','Cervical retained-food pouch'],['Achalasia','Distal emptying disorder'],['Initial anatomy','Contrast swallow']], [ref('UEG/ESNM Dysphagia Clinical Recommendations (2025)','https://doi.org/10.1002/ueg2.70062')], 'clinical_scenario')

if __name__=='__main__':
    finalize('GI & pancreas',1,'Esophageal Disorders','gi-esophageal',rows,28)
