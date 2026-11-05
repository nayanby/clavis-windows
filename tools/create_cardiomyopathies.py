"""Original topic-based Cardiomyopathies chapter."""
from qbank_authoring import question, ref, finalize
H=ref('2024 AHA/ACC Multisociety Hypertrophic Cardiomyopathy Guideline','https://doi.org/10.1016/j.jacc.2024.02.014')
C=ref('2023 ESC Cardiomyopathies Guideline','https://doi.org/10.1093/eurheartj/ehad194')
M=ref('2025 ESC Myocarditis and Pericarditis Guideline','https://doi.org/10.1093/eurheartj/ehaf192')
VA=ref('2022 ESC Ventricular Arrhythmias Guideline','https://doi.org/10.1093/eurheartj/ehac262')
rows=[]
def q(*args,**kwargs):rows.append(question(*args,**kwargs))

q('An adult has unexplained asymmetric LV wall thickness of 18 mm without hypertension, valve obstruction or another sufficient loading cause. Which phenotype should be considered?',
 'Hypertrophic cardiomyopathy',[
 ('Dilated cardiomyopathy defined by wall thickening alone','DCM concerns ventricular dilation and systolic dysfunction, not isolated unexplained hypertrophy.'),
 ('Physiological athlete remodeling proven by thickness alone','Athletic adaptation requires a broader pattern and cannot be assumed from one measurement.'),
 ('Hypertensive heart disease despite the absence of a loading explanation','A sufficient pressure-loading cause has specifically not been found.')],
 'HCM requires hypertrophy unexplained by loading conditions',
 '**Adult wall thickness of at least 15 mm can support HCM when another cause does not explain it.**',
 ['Smaller thresholds may be relevant in relatives or a known genetic context.', 'Phenocopies such as amyloidosis or storage disease must be considered when the clinical pattern suggests them.'],
 '**Establish a phenotype and then investigate its cause.**',
 ['Review family history, ECG, echo morphology and CMR when indicated.', 'Do not equate every thick wall with sarcomeric HCM.'],
 [['Unexplained hypertrophy','Supports HCM assessment'],['Pressure or valve loading','May explain secondary hypertrophy'],['Infiltrative/storage clues','Assess a phenocopy']], [H,C], 'clinical_scenario')
q('A patient with HCM has exertional symptoms and a resting LVOT gradient of 18 mm Hg. What is the appropriate next physiological assessment?',
 'Assess provoked obstruction with maneuvers and, when needed, exercise echocardiography',[
 ('Exclude obstruction permanently because the resting gradient is below 30','Dynamic obstruction can be absent at rest and emerge under physiological stress.'),
 ('Diagnose severe fixed AS from the LVOT gradient alone','An intracavitary dynamic gradient is not the same as a transvalvular aortic gradient.'),
 ('Perform septal reduction without documenting the obstructive mechanism','Intervention requires appropriate clinical and hemodynamic assessment.')],
 'HCM obstruction is dynamic',
 '**A low resting gradient does not exclude important provocable LVOT obstruction.**',
 ['Valsalva and standing can reveal loading-dependent obstruction.', 'Exercise echo is useful in a symptomatic patient when resting and standard provocation do not explain the presentation.'],
 '**Relate the gradient to symptoms and treatment decisions.**',
 ['A rest or provoked gradient of at least 50 mm Hg is an important threshold in symptomatic treatment pathways.', 'Document mitral systolic anterior motion and the site of acceleration to avoid confusing MR or fixed obstruction with LVOT flow.'],
 [['Low resting gradient','Assess provocation if clinically relevant'],['Exercise-induced obstruction','Can explain exertional symptoms'],['At least 50 mm Hg with symptoms','Important treatment-pathway threshold']], [H], 'clinical_scenario')
q('Why does the murmur of dynamic obstructive HCM often increase during the strain phase of Valsalva?',
 'Reduced venous return makes the LV cavity smaller and can worsen dynamic outflow obstruction',[
 ('Increased preload widens the cavity and necessarily raises obstruction','Valsalva strain generally reduces venous return, and a larger cavity usually reduces this dynamic obstruction.'),
 ('The maneuver creates new aortic leaflet calcification','Calcification does not develop within a bedside maneuver.'),
 ('The murmur must be mitral stenosis because it changes with breathing','The described systolic dynamic response does not identify MS.')],
 'Loading changes alter dynamic obstruction',
 '**A smaller cavity can intensify the interaction of the septum and mitral apparatus.**',
 ['Systolic anterior motion can contribute to obstruction and MR.', 'Standing often has a similar preload-reducing effect.'],
 '**Avoid treating the auscultatory response as a stand-alone diagnosis.**',
 ['Echo confirms anatomy and the location and timing of the gradient.', 'Hydration, afterload and contractility influence symptoms and treatment choices.'],
 [['Reduced preload','Often increases dynamic LVOT obstruction'],['Increased preload/afterload','Can reduce the dynamic gradient'],['Definitive assessment','Doppler and structural imaging']], [H])
q('A patient has symptomatic obstructive HCM without hypotension or contraindication to beta blockade. Which drug strategy is generally first line?',
 'A nonvasodilating beta blocker titrated to tolerance and symptom response',[
 ('A potent arterial vasodilator as the universal first choice','Excessive afterload reduction can worsen dynamic obstruction.'),
 ('Digoxin for routine positive inotropy','Increasing contractility can aggravate obstructive physiology.'),
 ('High-dose loop diuresis despite euvolemia','Reducing preload unnecessarily can worsen obstruction.')],
 'Reduce adrenergic drive in obstructive HCM',
 '**Nonvasodilating beta blockade can reduce heart rate and contractility and improve filling time.**',
 ['Symptoms and tolerability guide titration.', 'Verapamil or diltiazem can be alternatives in selected patients when beta blockers are ineffective or not tolerated.'],
 '**The obstructive phenotype changes usual drug instincts.**',
 ['Avoid unnecessary preload or afterload reduction.', 'Persistent limiting symptoms can lead to myosin inhibitor, disopyramide or septal reduction assessment at an experienced center.'],
 [['Initial suitable obstructive HCM','Nonvasodilating beta blocker'],['Persistent symptoms','Assess additional mechanism-directed options'],['Low preload or afterload','Can worsen obstruction']], [H], 'clinical_scenario')
q('Which patient with obstructive HCM raises particular concern about verapamil use?',
 'A patient with hypotension, severe resting symptoms and a very high resting LVOT gradient',[
 ('A stable patient with adequate pressure who cannot tolerate beta blockade','Verapamil can be an option in an appropriately selected stable patient.'),
 ('A patient with mild symptoms and no major conduction disease after suitability assessment','These features do not define the high-risk scenario described.'),
 ('An asymptomatic relative with a normal phenotype as an indication for treatment','There is no indication here, but this does not represent the specific hemodynamic danger of advanced obstruction.')],
 'Negative inotropy does not eliminate vasodilator risk',
 '**Verapamil can lower pressure and worsen instability in a high-gradient compromised patient.**',
 ['The guideline cautions against use with hypotension, severe resting dyspnea or very high gradients.', 'AV conduction and ventricular function are additional safety considerations.'],
 '**Escalate specialized care when physiology is severe.**',
 ['Do not assume a standard outpatient drug sequence is safe in hemodynamic compromise.', 'Assess volume, rhythm and the need for advanced obstruction treatment.'],
 [['Stable suitable patient','May use a non-DHP CCB'],['Hypotension/severe resting compromise','Avoid reflex verapamil'],['Severe refractory obstruction','Expert-center assessment']], [H])
q('A patient receiving a cardiac myosin inhibitor for obstructive HCM develops persistent LVEF 44%. What is the appropriate treatment principle?',
 'Stop or interrupt the myosin inhibitor according to the treatment protocol and assess systolic dysfunction',[
 ('Increase the inhibitor because reduced EF proves more obstruction','Further suppressing contractility can worsen systolic dysfunction.'),
 ('Ignore EF because myosin inhibition affects only the valve','The drug acts on myocardial contractile function.'),
 ('Add digoxin automatically without reviewing the obstructive physiology','This does not address the drug-related concern and may be inappropriate in obstruction.')],
 'Myosin inhibition requires ventricular-function surveillance',
 '**Reducing excessive contractile force can improve obstruction but can also depress systolic function.**',
 ['The 2024 guideline calls for discontinuing myosin inhibitors with persistent EF below 50%.', 'Use the current agent-specific monitoring and interaction protocol.'],
 '**Investigate other contributors to a new EF decline.**',
 ['Assess ischemia, arrhythmia, infection and disease progression.', 'Provide appropriate systolic-HF treatment when indicated while reassessing the HCM strategy.'],
 [['Desired effect','Reduced excessive contractility and obstruction'],['EF below 50%','Important safety signal'],['Management','Interrupt/reassess according to protocol']], [H], 'clinical_scenario')
q('A patient with obstructive HCM has NYHA III symptoms despite appropriate drug treatment and a provoked gradient of 85 mm Hg. Which next step is appropriate?',
 'Expert-center assessment for septal reduction or another advanced obstruction-directed strategy',[
 ('Septal reduction solely to eliminate every murmur in an asymptomatic person','The intervention is directed at clinically important refractory obstruction, not an auscultatory finding alone.'),
 ('Ignore the gradient because it is provoked rather than resting','Provoked obstruction can be clinically meaningful.'),
 ('Use fibrinolysis to reduce septal thickness','Fibrinolysis does not treat hypertrophied myocardium.')],
 'Refractory symptomatic obstruction can need intervention',
 '**Clinical limitation, documented obstruction and adequate prior therapy are central to selection.**',
 ['Septal myectomy and alcohol septal ablation have different anatomical requirements and trade-offs.', 'Age, comorbidity, mitral anatomy and center expertise influence choice.'],
 '**Treat the complete obstructive apparatus.**',
 ['Associated mitral or papillary abnormalities may favor a surgical strategy.', 'Ablation is not interchangeable with surgery in every anatomy and carries conduction-system risks.'],
 [['Refractory symptoms plus important gradient','Advanced-treatment assessment'],['Complex mitral anatomy','May favor surgical planning'],['Alcohol septal ablation','Requires suitable septal arterial anatomy']], [H], 'clinical_scenario')
q('Which finding is an important sudden-death risk marker in adult HCM?',
 'Massive LV hypertrophy with maximal wall thickness around 30 mm or greater',[
 ('A soft murmur alone','Murmur intensity does not define sudden-death risk.'),
 ('A normal single ambulatory recording as proof of lifetime safety','Intermittent arrhythmia and evolving phenotype limit that conclusion.'),
 ('Mild isolated hypertension without an HCM phenotype','That is not the characteristic HCM marker being assessed.')],
 'HCM risk assessment uses multiple clinical and imaging markers',
 '**Marked hypertrophy is one important marker rather than a complete ICD rule by itself.**',
 ['Prior arrest or sustained VT, likely arrhythmic syncope, family sudden death, apical aneurysm and systolic dysfunction are other major considerations.', 'Nonsustained VT and extensive LGE can add information in shared decisions.'],
 '**Use the applicable guideline framework with individualized counseling.**',
 ['The ACC/AHA marker approach and ESC model-based tools are related but not identical.', 'Discuss competing risks, device complications and preferences.'],
 [['Massive wall thickness','Important risk marker'],['Prior arrest/sustained VT','Secondary-prevention context'],['ICD decision','Integrated assessment']], [H,C])
q('Why is an LV apical aneurysm relevant in HCM?',
 'It can provide a scar-related ventricular arrhythmia substrate and a site for thrombus',[
 ('It guarantees that the underlying disease is coronary infarction rather than HCM','HCM can have an apical aneurysm without a typical epicardial infarct mechanism.'),
 ('It proves that all obstruction has resolved harmlessly','It can identify a higher-risk phenotype rather than benign resolution.'),
 ('It is visible only on a resting ECG','Imaging, especially contrast echo or CMR, defines it.')],
 'The apex can be a clinically important HCM compartment',
 '**Aneurysmal scar can support ventricular re-entry and stasis.**',
 ['CMR helps detect apical morphology and fibrosis when standard echo is limited.', 'Assess for apical thrombus and the broader arrhythmic risk profile.'],
 '**Do not reduce HCM follow-up to a single septal measurement.**',
 ['Apical, midventricular and other patterns require complete ventricular imaging.', 'Device and anticoagulation decisions follow the full clinical findings rather than the aneurysm label alone.'],
 [['Apical aneurysm','Scar and thrombus concerns'],['CMR/contrast echo','Improves apical assessment'],['Management','Integrate arrhythmia and embolic risk']], [H,C])
q('A 42-year-old patient with HCM develops clinical AF but has CHA2DS2-VASc score 0. What is the stroke-prevention principle?',
 'Anticoagulation is recommended irrespective of the usual score, if no contraindication exists',[
 ('No anticoagulation because age is below 65','HCM-associated AF has a distinct risk framework.'),
 ('Aspirin is equivalent because the score is low','Aspirin is not an equivalent substitute for indicated anticoagulation.'),
 ('Anticoagulation is needed only if the LVOT gradient exceeds 100 mm Hg','The indication is not defined by that gradient threshold.')],
 'HCM-associated AF is not governed by a low conventional score alone',
 '**Clinical AF in HCM generally warrants anticoagulation independent of CHA2DS2-VASc.**',
 ['Atrial disease and the HCM substrate increase embolic concern.', 'A DOAC is generally first line when no separate contraindicating valve or other condition exists.'],
 '**Manage rhythm and stroke risk together.**',
 ['AF may be poorly tolerated because atrial contribution to filling is important.', 'A successful rhythm intervention does not automatically eliminate the underlying anticoagulation indication.'],
 [['Clinical AF with HCM','Anticoagulation despite a low conventional score'],['Rate/rhythm treatment','Addresses hemodynamic and symptom burden'],['Stroke prevention','Separate ongoing need']], [H], 'clinical_scenario')
q('A pathogenic sarcomeric variant is identified in a patient with HCM. What is appropriate for first-degree relatives?',
 'Offer genetic counseling and cascade testing, with phenotype surveillance determined by the results and family context',[
 ('Use any variant of uncertain significance as a definitive predictive test','A VUS should not be treated as a proven familial disease-causing variant.'),
 ('Screen relatives only if they develop severe HF','Early phenotype detection and counseling are valuable before advanced symptoms.'),
 ('Assume a normal childhood echo excludes disease permanently','Age-dependent penetrance can require continued surveillance in at-risk relatives.')],
 'Family evaluation depends on a valid causal variant',
 '**Cascade testing is useful when the familial variant is pathogenic or likely pathogenic.**',
 ['A genotype-positive relative may not yet show hypertrophy.', 'Clinical screening intervals depend on age, genotype, symptoms and the family phenotype.'],
 '**Interpret genetics with counseling rather than as an isolated binary report.**',
 ['Reclassification of variants can change advice.', 'A negative test for a well-established familial variant differs from a negative broad panel in a family without an identified cause.'],
 [['Pathogenic familial variant','Useful for cascade testing'],['Variant of uncertain significance','Not a definitive predictive result'],['Genotype-positive/phenotype-negative','Needs appropriate surveillance']], [H,C])
q('Which pattern favors physiological athlete remodeling over pathological HCM in an otherwise uncertain case?',
 'Proportionate chamber enlargement with preserved diastolic function and regression of borderline hypertrophy after detraining',[
 ('Marked asymmetric hypertrophy with abnormal relaxation and relevant family history','These features favor pathological disease.'),
 ('Extensive pathological fibrosis with unexplained exertional syncope','These are concerning findings, not reassuring athletic adaptation.'),
 ('A pathogenic sarcomeric variant as proof of purely physiological remodeling','A valid disease-causing variant supports inherited disease assessment.')],
 'Differentiate adaptation from disease using a pattern',
 '**No single wall-thickness number resolves every athlete-HCM overlap.**',
 ['Chamber size, diastolic function, ECG, family history and CMR contribute.', 'Detraining can provide additional information in selected borderline cases.'],
 '**Avoid both overdiagnosis and false reassurance.**',
 ['Symptoms, arrhythmia and family sudden death warrant careful assessment.', 'Exercise advice should reflect a shared individualized evaluation rather than an automatic blanket restriction.'],
 [['Physiological adaptation','Proportionate remodeling and normal function'],['HCM clues','Asymmetry, fibrosis, family disease or abnormal function'],['Uncertainty','Specialist multimodal assessment']], [H,C])

# Amyloidosis and other cardiomyopathy phenotypes follow.
q('An older patient has HFpEF, increased LV wall thickness, low ECG voltage and bilateral carpal tunnel syndrome. Which disease should be specifically assessed?',
 'Cardiac amyloidosis',[
 ('Uncomplicated essential hypertension as the only possible explanation','The discordance between wall thickness and voltage plus extracardiac clues warrants an infiltrative assessment.'),
 ('Classic dilated cardiomyopathy solely from preserved EF','The phenotype is thick-walled and restrictive rather than defined by dilation.'),
 ('Isolated benign carpal tunnel syndrome with no cardiac relevance','Carpal tunnel disease can precede ATTR cardiomyopathy, although it is not specific alone.')],
 'Look for discordance and extracardiac clues',
 '**Increased wall thickness with unexpectedly low voltage raises suspicion for an infiltrative process.**',
 ['Carpal tunnel syndrome, spinal stenosis, neuropathy and tendon rupture can support an ATTR pattern.', 'AL amyloidosis must also be excluded promptly; clinical clues do not reliably type the protein.'],
 '**Follow a structured amyloid diagnostic pathway.**',
 ['Assess monoclonal proteins and use appropriate cardiac imaging.', 'Low voltage is not obligatory, and its absence does not exclude amyloidosis.'],
 [['Thick wall plus low voltage','Infiltrative clue'],['Carpal tunnel and related features','May support ATTR suspicion'],['Protein typing','Required before disease-specific treatment']], [C], 'clinical_scenario')
q('Relative apical sparing on longitudinal strain imaging suggests cardiac amyloidosis. Which interpretation is most appropriate?',
 'It is a supportive pattern that requires integration with other evidence rather than a definitive typing test',[
 ('It proves ATTR and excludes AL','Strain patterns cannot reliably establish the amyloid protein type.'),
 ('Its absence excludes every form of cardiac amyloidosis','Sensitivity is imperfect and depends on disease stage and population.'),
 ('It establishes a pathogenic TTR variant','Genetic status cannot be inferred from strain imaging.')],
 'Imaging patterns support a hypothesis',
 '**Relative preservation of apical strain can occur in cardiac amyloidosis.**',
 ['The pattern is not unique to the disease.', 'A full echo assessment includes wall thickness, chamber size, filling, atrial function and right-sided findings.'],
 '**Proceed to protein and tissue-specific diagnostic assessment.**',
 ['Monoclonal testing is essential when choosing the subsequent pathway.', 'Use scintigraphy, CMR and biopsy according to the clinical context rather than treating one strain image as a final diagnosis.'],
 [['Apical sparing','Supportive but not definitive'],['AL versus ATTR','Requires protein-specific assessment'],['Normal or atypical strain','Does not independently exclude disease']], [C])
q('A patient has a compatible cardiac amyloid phenotype and grade 3 myocardial uptake on PYP scintigraphy confirmed by SPECT. Serum and urine immunofixation and serum free-light-chain assessment show no clonal abnormality. What diagnosis can generally be made noninvasively?',
 'ATTR cardiac amyloidosis',[
 ('AL cardiac amyloidosis established solely by strong PYP uptake','Strong uptake is not an AL typing criterion; the nonbiopsy ATTR pathway requires exclusion of a clonal process.'),
 ('Hereditary rather than wild-type ATTR without genetic testing','Scintigraphy cannot distinguish hereditary from wild-type ATTR.'),
 ('Amyloidosis excluded because there is no monoclonal protein','Absence of a clonal marker supports the ATTR pathway rather than excluding all amyloid.')],
 'The nonbiopsy ATTR pathway has specific conditions',
 '**Compatible imaging plus grade 2-3 myocardial bone-tracer uptake and no evidence of a clonal dyscrasia can establish ATTR-CM.**',
 ['SPECT helps confirm myocardial rather than blood-pool uptake.', 'The clonal screen includes serum free light chains and serum and urine immunofixation.'],
 '**Complete TTR genetic testing after ATTR is identified.**',
 ['This distinguishes hereditary from wild-type disease and informs relatives.', 'An incomplete monoclonal screen should not be treated as satisfying the nonbiopsy criteria.'],
 [['Strong myocardial uptake with negative clonal testing','Nonbiopsy ATTR diagnosis may be possible'],['Monoclonal abnormality','Requires a different typing assessment'],['TTR genetic testing','Determines hereditary status']], [C], 'clinical_scenario')
q('A patient with suspected cardiac amyloidosis has a monoclonal light-chain abnormality and positive bone-tracer cardiac uptake. What is the safest diagnostic principle?',
 'Obtain specialist assessment and definitive amyloid typing rather than assume the scan proves ATTR',[
 ('Ignore the monoclonal finding because PYP is positive','A clonal process changes the diagnostic pathway and AL remains a concern.'),
 ('Start ATTR therapy as treatment for every amyloid protein','ATTR-directed treatment does not treat AL.'),
 ('A serum protein electrophoresis without immunofixation is sufficient to close the case','A complete clonal assessment and appropriate tissue typing may be necessary.')],
 'A positive scan does not bypass a monoclonal abnormality',
 '**AL can be rapidly progressive and requires urgent recognition.**',
 ['Monoclonal gammopathy can also coexist with ATTR in an older person.', 'Therefore neither the clonal result nor the scan alone establishes the deposited protein.'],
 '**Use biopsy and reliable protein typing when the nonbiopsy ATTR criteria are not met.**',
 ['Mass-spectrometry-based typing is valuable when available.', 'Coordinate cardiology and hematology rather than delaying a potentially time-sensitive AL diagnosis.'],
 [['Positive scan without clonal abnormality','Potential nonbiopsy ATTR pathway'],['Positive scan with clonal abnormality','Definitive typing assessment needed'],['Confirmed AL','Plasma-cell-directed pathway']], [C], 'clinical_scenario')
q('Which CMR pattern is characteristic of cardiac amyloidosis?',
 'Diffuse subendocardial or transmural enhancement with abnormal myocardial nulling and increased extracellular volume',[
 ('A single territorial scar matching one coronary artery as the only defining pattern','That pattern more typically supports ischemic infarction.'),
 ('A normal extracellular volume as a mandatory finding','Amyloid expands the interstitial compartment.'),
 ('An isolated aortic flow acceleration as the diagnostic CMR criterion','That describes a different hemodynamic lesion.')],
 'Amyloid deposition expands the myocardial extracellular space',
 '**CMR can show diffuse infiltration rather than a single coronary-territory scar.**',
 ['Abnormal gadolinium kinetics can make normal nulling difficult.', 'Native T1 and extracellular volume mapping add information, subject to technical and renal-context considerations.'],
 '**CMR supports cardiac involvement but does not reliably replace protein typing.**',
 ['AL and ATTR can share imaging features.', 'Combine the result with clonal testing, scintigraphy and selected biopsy.'],
 [['Amyloid','Diffuse enhancement and extracellular expansion'],['Infarction','Subendocardial/transmural coronary-territory pattern'],['Protein type','Requires additional assessment']], [C])
q('Congo-red-positive tissue confirms amyloid. What is the next essential step before disease-specific systemic treatment?',
 'Identify the deposited amyloid protein reliably',[
 ('Assume every deposit is transthyretin','AL and other amyloid types require different treatment.'),
 ('Assume a coincidental monoclonal protein proves the deposit is AL','A circulating clone can coexist with another amyloid type.'),
 ('Treat the stain as proof of a specific TTR mutation','Congo red identifies amyloid, not a mutation.')],
 'Demonstration of amyloid and typing are separate tasks',
 '**Congo red establishes a deposit with amyloid properties but not its precursor protein.**',
 ['Reliable typing prevents directing treatment at the wrong disease.', 'Mass spectrometry or a validated expert laboratory approach can define the protein.'],
 '**Integrate tissue with systemic evaluation.**',
 ['Assess involved organs and the hematologic or genetic context.', 'Do not infer causality from an incidental age-associated monoclonal gammopathy.'],
 [['Congo red','Confirms amyloid deposition'],['Protein typing','Defines AL, ATTR or another type'],['Genetic testing','Defines hereditary status when appropriate']], [C])
q('Tafamidis treats ATTR cardiomyopathy primarily by which mechanism?',
 'Stabilizing the transthyretin tetramer to reduce dissociation',[
 ('Suppressing all plasma cells that produce immunoglobulin light chains','That is an AL-directed therapeutic concept, not tafamidis action.'),
 ('Silencing hepatic TTR messenger RNA','That is the mechanism of a TTR silencer rather than tafamidis.'),
 ('Directly dissolving every existing myocardial deposit immediately','Tafamidis does not provide immediate universal deposit clearance.')],
 'Stabilization targets an early step in ATTR formation',
 '**Tetramer dissociation is an important step toward transthyretin misfolding and deposition.**',
 ['Tafamidis stabilizes the tetramer rather than suppressing TTR production.', 'It is not treatment for immunoglobulin light-chain amyloidosis.'],
 '**Set realistic expectations for disease-modifying treatment.**',
 ['Clinical benefit develops over time and does not replace congestion management.', 'Disease stage, functional status and newer treatment options influence the individualized plan.'],
 [['Tafamidis','TTR stabilization'],['TTR siRNA','Reduced hepatic production'],['AL therapy','Targets the light-chain-producing clone']], [C,ref('ATTR-ACT: Tafamidis Treatment for Patients with Transthyretin Amyloid Cardiomyopathy','https://doi.org/10.1056/NEJMoa1805689')])
q('Which description correctly distinguishes vutrisiran in contemporary ATTR cardiomyopathy treatment?',
 'It is an RNA-interference therapy that reduces hepatic transthyretin production',[
 ('It is a monoclonal antibody against platelet GP IIb/IIIa','That is an antiplatelet target unrelated to vutrisiran.'),
 ('It is a treatment only for AL plasma-cell disease','Its target is transthyretin production, not the light-chain clone.'),
 ('It acts only by stabilizing an existing TTR tetramer','That is the stabilizer mechanism, not RNA silencing.')],
 'ATTR therapy now includes production-silencing approaches',
 '**Vutrisiran uses small interfering RNA to reduce TTR synthesis in the liver.**',
 ['Its adult US indication includes wild-type and hereditary ATTR cardiomyopathy.', 'This is distinct from tafamidis-mediated tetramer stabilization.'],
 '**Use current agent-specific eligibility and monitoring.**',
 ['Reduced TTR transport can lower vitamin A levels, so follow the label\'s supplementation and symptom guidance.', 'Approval in one jurisdiction does not guarantee identical access or reimbursement elsewhere.'],
 [['Vutrisiran','Hepatic TTR production silencing'],['Tafamidis','Tetramer stabilization'],['Correct amyloid type','Essential before therapy selection']], [ref('Amvuttra prescribing information: ATTR cardiomyopathy indication and mechanism','https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=8db0facb-81b6-4006-9239-27dc6409c5d3&type=display')])
q('A patient has LV dilation and EF 28% without sufficient coronary disease, hypertension or valve disease to explain the findings. Which phenotype is present?',
 'Dilated cardiomyopathy',[
 ('HCM defined by any low EF','A low EF alone does not establish a hypertrophic phenotype.'),
 ('Restrictive cardiomyopathy defined only by LV dilation','Restriction concerns abnormal filling physiology and is not defined by this dilation pattern.'),
 ('A final diagnosis of viral disease from echo alone','The phenotype does not establish a specific cause.')],
 'DCM is a phenotype that still needs an etiological assessment',
 '**Ventricular dilation with systolic dysfunction unexplained by sufficient loading or coronary disease defines the DCM pattern.**',
 ['Genetic, toxic, inflammatory, metabolic and rhythm-related causes are possible.', 'A family history can be relevant even when the patient has an apparent acquired trigger.'],
 '**Treat dysfunction while investigating the cause.**',
 ['Use appropriate HF therapy and assess arrhythmic risk.', 'CMR and selected genetic or systemic testing can identify management-relevant substrates.'],
 [['Phenotype','Dilation plus systolic dysfunction'],['Cause','Requires further investigation'],['Treatment','HF care plus etiology-specific management']], [C], 'clinical_scenario')
q('A family has DCM, early AV conduction disease and ventricular arrhythmias that appear before severe EF reduction. Which genetic substrate is particularly important to consider?',
 'LMNA-related cardiomyopathy',[
 ('A negative family screen based only on one normal childhood ECG','Age-dependent disease can be missed by a single early assessment.'),
 ('An isolated P2Y12 receptor polymorphism as the standard explanation','That is not the characteristic conduction-arrhythmia DCM gene association.'),
 ('A purely valvular disorder established by the pedigree','The combined familial electrical and myocardial phenotype suggests a cardiomyopathy substrate.')],
 'Electrical disease can precede advanced ventricular failure',
 '**LMNA cardiomyopathy can combine conduction disease, atrial arrhythmia and ventricular arrhythmic risk.**',
 ['Risk is not captured by EF alone.', 'A gene-specific framework and family phenotype influence device assessment.'],
 '**Use genetic counseling and appropriate family evaluation.**',
 ['Differentiate a pathogenic variant from an uncertain finding.', 'A pacemaker indication may coexist with a need to consider defibrillation capability in the full risk assessment.'],
 [['LMNA phenotype','DCM plus conduction/arrhythmia burden'],['EF alone','May underestimate risk'],['Device planning','Integrate genotype and electrical disease']], [C,VA], 'clinical_scenario')
q('Which CMR scar pattern is more typical of nonischemic DCM than a prior territorial MI?',
 'Mid-wall septal late gadolinium enhancement sparing the subendocardium',[
 ('Subendocardial enhancement confined to an epicardial coronary territory','That pattern is characteristic of ischemic injury.'),
 ('A transmural scar matching an occluded coronary artery','This also supports an infarct mechanism.'),
 ('Any absence of enhancement as proof that no cardiomyopathy exists','DCM can exist without visible LGE.')],
 'Scar distribution helps infer mechanism',
 '**Nonischemic fibrosis often does not follow a single coronary territory or begin in the subendocardium.**',
 ['Mid-wall septal LGE is a recognized DCM pattern.', 'Other patterns may suggest inflammatory, genetic or infiltrative disease.'],
 '**CMR contributes to prognosis as well as diagnosis.**',
 ['Fibrosis can be relevant to arrhythmic risk.', 'Interpret the pattern with coronary assessment, clinical history and ventricular function rather than assigning an etiology from one sequence alone.'],
 [['Ischemic scar','Subendocardial or transmural coronary distribution'],['Nonischemic DCM','Often mid-wall pattern'],['No visible LGE','Does not exclude DCM']], [C])
q('A patient with DCM has a pathogenic TTN truncating variant and a history of substantial alcohol exposure. Which interpretation is most appropriate?',
 'A genetic substrate and an acquired exposure can both contribute to the phenotype',[
 ('The alcohol history makes a valid genetic finding irrelevant','Environmental stress and genetic susceptibility can interact.'),
 ('The genetic finding proves that stopping alcohol cannot help','Removing a toxic contributor remains important.'),
 ('Every TTN sequence change is automatically pathogenic','Variant type, location, frequency and expert interpretation matter.')],
 'Genetic and acquired causes are not mutually exclusive',
 '**Cardiomyopathy often reflects susceptibility interacting with physiological or environmental stress.**',
 ['A pathogenic TTN truncation can be relevant in a patient with another plausible trigger.', 'Do not generalize from a carefully classified variant to every TTN finding.'],
 '**Treat the exposure and assess the family.**',
 ['Counsel on alcohol cessation and continue HF treatment.', 'Offer appropriate genetic counseling and cascade evaluation when a disease-causing familial variant is established.'],
 [['Genetic substrate','May confer susceptibility'],['Alcohol or other stressor','Can contribute to expression'],['Management','Address both rather than choosing only one']], [C], 'clinical_scenario')
q('A woman develops new HF with LVEF 30% late in pregnancy, with no previous cardiac disease or alternative sufficient cause. Which diagnosis should be considered?',
 'Peripartum cardiomyopathy',[
 ('Normal pregnancy adaptation regardless of severe systolic dysfunction','Normal pregnancy does not explain an EF of 30% with HF.'),
 ('A diagnosis that requires pre-existing rheumatic MS','Peripartum cardiomyopathy is a myocardial syndrome and does not require MS.'),
 ('Physiological athlete remodeling','This does not fit the pregnancy-associated new systolic HF syndrome.')],
 'Pregnancy-associated HF needs urgent etiological assessment',
 '**Peripartum cardiomyopathy is otherwise unexplained systolic HF arising toward the end of pregnancy or in the following months.**',
 ['EF is generally below 45%; marked LV dilation is not obligatory.', 'Exclude ischemia, valve disease, hypertension-related complications and other causes.'],
 '**Use a pregnancy/postpartum multidisciplinary treatment plan.**',
 ['Some standard HF drugs are inappropriate during pregnancy, while postpartum choices also depend on lactation and clinical status.', 'Recovery varies, and future pregnancy counseling remains important even after improvement.'],
 [['New unexplained low EF near pregnancy','Consider peripartum cardiomyopathy'],['Normal pregnancy dyspnea','Does not explain objective severe dysfunction'],['Treatment','Stage-specific maternal cardiac care']], [C], 'clinical_scenario')
q('A patient with suspected alcohol-related DCM asks whether reducing exposure matters after HF is established. Which advice is appropriate?',
 'Alcohol cessation is important alongside HF treatment and evaluation for other contributors',[
 ('Continue heavy drinking because myocardial recovery is impossible','Recovery can occur in some patients, and ongoing exposure can worsen disease.'),
 ('Use abstinence as a reason to stop all HF treatment immediately','Exposure removal does not replace disease-modifying treatment.'),
 ('Assume the alcohol history excludes every genetic or ischemic cause','More than one contributor can coexist.')],
 'Removing a cardiotoxic exposure can change the trajectory',
 '**Sustained alcohol exposure can contribute to ventricular dysfunction.**',
 ['The causal assessment requires dose and duration history and exclusion of sufficient alternative causes.', 'Support for alcohol-use disorder may be essential for sustained cessation.'],
 '**Reassess ventricular function after treatment without promising a guaranteed recovery.**',
 ['Continue appropriate HF and arrhythmia management.', 'Consider family history and genetic susceptibility when the phenotype or pedigree suggests them.'],
 [['Exposure removal','Important disease-specific intervention'],['HF treatment','Still required'],['Recovery assessment','Serial function and symptoms']], [C], 'clinical_scenario')
q('A patient has persistent rapid atrial tachycardia and otherwise unexplained LV dysfunction. EF improves substantially after effective rhythm control. What does this support?',
 'Arrhythmia-induced cardiomyopathy',[
 ('A fixed irreversible scar as the sole explanation','Marked recovery after arrhythmia suppression supports a reversible rhythm contribution.'),
 ('A reason to ignore recurrent tachycardia in future','Recurrence can lead to renewed dysfunction.'),
 ('Proof that HF medication must be stopped immediately','Recovery does not establish that all relapse-preventing treatment is unnecessary.')],
 'A sustained rhythm burden can impair ventricular function',
 '**Persistent tachycardia or a high arrhythmia burden can cause or worsen cardiomyopathy.**',
 ['Improvement after effective control supports the diagnosis retrospectively.', 'Pre-existing myocardial disease may coexist.'],
 '**Treat the rhythm and continue structured cardiac follow-up.**',
 ['Choose definitive rhythm treatment when appropriate and monitor for recurrence.', 'Reassess EF, symptoms and ongoing HF therapy after stabilization.'],
 [['Before control','Tachycardia plus unexplained dysfunction'],['After control','Recovery supports a rhythm contribution'],['Long term','Prevent and detect recurrence']], [C], 'clinical_scenario')
q('Which DCM presentation should prompt careful family assessment even if the patient initially appears to have an isolated case?',
 'A first-degree relative with unexplained cardiomyopathy or sudden death at a young age',[
 ('A relative with uncomplicated seasonal rhinitis','That is not the relevant cardiac pedigree clue.'),
 ('No information because all DCM is acquired','A substantial genetic component exists in DCM.'),
 ('A normal single ECG in the proband as proof that relatives need no review','The proband already has structural disease, and one ECG does not resolve familial risk.')],
 'A three-generation pedigree can reveal a hidden familial pattern',
 '**Ask about HF, transplants, pacemakers, defibrillators and unexplained early death.**',
 ['Relatives may have been assigned nonspecific labels rather than a cardiomyopathy diagnosis.', 'Age-dependent penetrance can make a family look isolated at first presentation.'],
 '**Use results to guide clinical and genetic screening.**',
 ['Counsel before predictive testing and interpret variants carefully.', 'Family evaluation should be phenotype and gene informed rather than a generic test for everyone without context.'],
 [['Early sudden death or DCM in relatives','Important familial clue'],['Conduction devices in a pedigree','May reveal electrical disease'],['Normal early assessment','May require age-appropriate surveillance']], [C])

# Inflammatory, arrhythmogenic and storage disorders follow.
q('After a viral-like illness, a patient develops chest pain and troponin elevation. CMR shows inferolateral subepicardial LGE and myocardial edema without a matching coronary-territory pattern. Which diagnosis is most likely?',
 'Acute myocarditis',[
 ('A completed transmural LAD infarction','The distribution is nonischemic and does not follow the proposed LAD territory.'),
 ('Chronic amyloid infiltration as the best explanation of acute focal edema','Amyloid has a different typical diffuse infiltrative pattern and clinical trajectory.'),
 ('A pure pericardial effusion with no myocardial involvement','Troponin and myocardial CMR abnormalities establish myocardial involvement.')],
 'CMR can demonstrate nonischemic inflammatory injury',
 '**A subepicardial or mid-wall pattern with edema supports myocarditis in the appropriate syndrome.**',
 ['CMR combines tissue injury and edema measures rather than relying on LGE alone.', 'A preceding infection is a clue, not proof of a specific myocardial pathogen.'],
 '**Risk assessment determines the next steps.**',
 ['Assess ventricular function, arrhythmia and conduction disease.', 'A stable uncomplicated case and fulminant shock require different investigation and support pathways.'],
 [['Myocarditis','Nonischemic injury plus inflammatory/edema evidence'],['Infarction','Usually subendocardial coronary-territory injury'],['Pericarditis alone','No requirement for myocardial tissue injury']], [M], 'clinical_scenario')
q('A patient has rapidly progressive unexplained HF, cardiogenic shock and ventricular arrhythmias with suspected myocarditis. Which diagnostic strategy is most appropriate at an experienced center?',
 'Consider urgent endomyocardial biopsy because identifying a specific inflammatory subtype can change treatment',[
 ('Assume a viral cause from a positive respiratory swab and omit further assessment','A respiratory result does not establish the myocardial mechanism, especially in a high-risk presentation.'),
 ('Require biopsy in every mild self-limited chest-pain case before any care','Biopsy is selective, with the clearest value when the result changes important management.'),
 ('Delay all support until histology is finalized','Shock stabilization must proceed while diagnostic work is arranged.')],
 'High-risk myocarditis can require tissue diagnosis',
 '**Biopsy can identify giant-cell, eosinophilic or other actionable myocarditis subtypes.**',
 ['Fulminant deterioration, serious ventricular arrhythmia or major conduction disease raises the stakes.', 'Sampling limitations and procedural risk require expertise.'],
 '**Diagnostic and stabilization pathways run together.**',
 ['Use appropriate shock support and assess temporary mechanical assistance when needed.', 'Immunosuppression decisions depend on the suspected or demonstrated subtype, not a generic assumption that every myocarditis is the same.'],
 [['Low-risk improving case','Often noninvasive assessment'],['High-risk unstable case','Consider management-changing biopsy'],['Shock','Immediate support while investigating']], [M], 'clinical_scenario')
q('A young adult has rapidly progressive HF, sustained VT and AV block. Biopsy shows extensive myocyte necrosis with multinucleated giant cells and mixed inflammation. Which diagnosis is most likely?',
 'Giant-cell myocarditis',[
 ('Uncomplicated physiological athlete remodeling','Necrotizing inflammation and malignant electrical disease are not physiological adaptation.'),
 ('Wild-type ATTR identified solely by giant cells','ATTR is an amyloid deposition disease, not defined by this inflammatory histology.'),
 ('A fixed congenital ventricular septal defect','That does not explain the biopsy and rapidly progressive inflammatory syndrome.')],
 'Giant-cell myocarditis is a high-risk actionable subtype',
 '**The combination of destructive inflammation, giant cells and severe electrical or pump dysfunction is characteristic.**',
 ['Differentiation from sarcoidosis and other inflammatory disorders requires expert pathology.', 'The course can be aggressive and require advanced HF support.'],
 '**Urgent specialist treatment can include combination immunosuppression and advanced-therapy assessment.**',
 ['Do not apply a routine mild viral-myocarditis observation strategy.', 'Device and transplant decisions depend on arrhythmia, recovery and the broader course.'],
 [['Giant-cell myocarditis','Destructive inflammation with giant cells'],['Cardiac sarcoidosis','Granulomatous disease with a different integrated pattern'],['Management','Urgent subtype-directed and advanced-HF care']], [M], 'clinical_scenario')
q('A patient develops new cardiac dysfunction after a drug hypersensitivity syndrome. There is eosinophilia and biopsy shows eosinophilic myocardial infiltration with injury. Which process is most likely?',
 'Eosinophilic myocarditis',[
 ('Pure coronary atherothrombosis established by eosinophilia','The biopsy and hypersensitivity context indicate a different mechanism.'),
 ('An incidental normal biopsy finding','Eosinophilic infiltration with myocardial injury is pathological.'),
 ('A diagnosis excluded unless EF is preserved','Eosinophilic myocarditis can cause severe systolic dysfunction and fulminant disease.')],
 'Eosinophilic inflammation can be drug related or systemic',
 '**Consider medication reactions, hypereosinophilic disease, vasculitis and parasitic causes.**',
 ['The systemic context helps identify the driver.', 'Thrombus and severe arrhythmia can complicate myocardial injury.'],
 '**Remove a suspected culprit and use cause-specific specialist treatment.**',
 ['Immunosuppression may be appropriate in selected noninfectious disease.', 'Assess for an infectious cause before assuming all eosinophilic disease should receive the same regimen.'],
 [['Drug hypersensitivity','Potential eosinophilic trigger'],['Systemic eosinophilic disorder','Assess extracardiac involvement'],['Myocardial injury','Can be fulminant and thrombogenic']], [M], 'clinical_scenario')
q('A cancer patient receiving an immune checkpoint inhibitor develops troponin elevation, new AV block and proximal weakness. Which concern requires urgent assessment?',
 'Checkpoint inhibitor-associated myocarditis with possible myositis or myasthenic overlap',[
 ('A harmless obligatory effect of effective cancer treatment','This pattern can indicate life-threatening immune toxicity.'),
 ('Only chronic anthracycline remodeling, irrespective of the treatment exposure','The temporal exposure and electrical-muscle syndrome require immune-toxicity assessment.'),
 ('Exclusion of myocardial disease because skeletal muscle symptoms coexist','Overlap syndromes can involve both cardiac and skeletal or neuromuscular disease.')],
 'Checkpoint toxicity can cross organ systems',
 '**New conduction disease and injury markers during checkpoint therapy are high-risk findings.**',
 ['Myositis and myasthenia-like features can coexist and increase clinical urgency.', 'A preserved EF does not exclude important myocarditis or arrhythmic risk.'],
 '**Hold the suspected treatment and mobilize urgent multidisciplinary care.**',
 ['Cardio-oncology, oncology and relevant neurological expertise may be needed.', 'Appropriate early immunosuppression and monitoring depend on the assessment; do not wait for a large EF decline before escalating.'],
 [['Cardiac signs','Troponin and new conduction/arrhythmia findings'],['Overlap signs','Weakness or neuromuscular symptoms'],['Response','Urgent immune-toxicity assessment']], [M], 'clinical_scenario')
q('Under the 2025 ESC myocarditis framework, which approach to strenuous exercise after acute myocarditis is most appropriate?',
 'Restrict exercise during active disease and use an individualized remission-based reassessment before return',[
 ('Return as soon as chest pain disappears without rhythm or function assessment','Symptom improvement alone does not establish complete cardiac recovery.'),
 ('Use a fixed calendar date as proof that inflammation and arrhythmic risk have resolved','The disease trajectory and residual findings matter.'),
 ('Prohibit all future physical activity permanently in every recovered patient','A blanket lifelong prohibition is not the individualized approach.')],
 'Return to exercise depends on recovery rather than one symptom or date',
 '**Current guidance emphasizes restriction until clinical remission and individualized reassessment.**',
 ['Ventricular function, injury markers, inflammation and arrhythmia are relevant.', 'Exercise testing and ambulatory ECG can contribute to clearance when appropriate.'],
 '**Discuss the intended intensity and the residual substrate.**',
 ['Competitive or high-intensity activity requires particular attention to risk.', 'Persistent scar or arrhythmia may alter advice even after active inflammation improves.'],
 [['Active myocarditis','Exercise restriction'],['Apparent recovery','Clinical, imaging and rhythm reassessment'],['Return plan','Individualized to risk and activity']], [M])
q('Which protein-system abnormality is commonly implicated in inherited arrhythmogenic cardiomyopathy?',
 'Desmosomal dysfunction affecting cell-to-cell adhesion',[
 ('A primary platelet COX-1 defect','That is not the characteristic cardiomyocyte adhesion substrate.'),
 ('An isolated vitamin K recycling defect','That affects coagulation rather than defining arrhythmogenic cardiomyopathy.'),
 ('A universal acquired TTR deposition process','ATTR is a different infiltrative disease.')],
 'Intercellular coupling contributes to arrhythmogenic disease',
 '**Variants in desmosomal genes can produce myocardial injury, fibrosis and ventricular arrhythmias.**',
 ['Right-dominant, left-dominant and biventricular patterns occur.', 'Not every clinically affected patient has an identified desmosomal variant.'],
 '**The electrical phenotype may precede advanced pump failure.**',
 ['Family assessment, CMR and rhythm evaluation are important.', 'Exercise exposure can influence disease expression and risk.'],
 [['Desmosomes','Cell adhesion and mechanical coupling'],['Disease expression','Scar and ventricular arrhythmia'],['Phenotype range','RV, LV or biventricular']], [C,VA])
q('A patient with arrhythmogenic cardiomyopathy asks about continuing high-intensity endurance competition. Which advice best reflects disease-specific risk?',
 'High-intensity endurance exercise can increase arrhythmic risk and disease expression, so activity needs specialist adjustment',[
 ('Endurance competition is protective regardless of genotype or phenotype','The evidence does not support that reassurance.'),
 ('A normal EF guarantees that exercise cannot trigger arrhythmia','Electrical risk can precede marked systolic dysfunction.'),
 ('Implanting an ICD makes every level of sport risk free','An ICD does not prevent all arrhythmia, injury or disease progression.')],
 'Mechanical stress can modify an inherited arrhythmogenic substrate',
 '**Exercise intensity and duration can influence penetrance and ventricular arrhythmias.**',
 ['Recommendations depend on diagnosis, genotype, symptoms and arrhythmic history.', 'The goal is a safe individualized activity plan, not unnecessary total inactivity.'],
 '**A device is protection against selected events, not permission to ignore triggers.**',
 ['Review the patient\'s sport, environment and preferences.', 'Continue family and longitudinal cardiac assessment.'],
 [['High-intensity endurance exposure','Potential adverse modifier'],['Lower-intensity activity','Individualize with specialist advice'],['ICD','Does not eliminate all sport-related risk']], [C,VA], 'clinical_scenario')
q('A patient has recurrent myocarditis-like chest-pain episodes, ventricular ectopy, subepicardial LV scar and a pathogenic DSP variant. Which interpretation is most appropriate?',
 'A desmoplakin-related arrhythmogenic cardiomyopathy can present with inflammatory hot phases',[
 ('Every episode proves an unrelated new viral infection','A genetic arrhythmogenic substrate can produce recurrent inflammatory presentations.'),
 ('DSP excludes ventricular arrhythmic risk','DSP disease can carry important ventricular arrhythmia risk.'),
 ('Normal RV size excludes all arrhythmogenic cardiomyopathy','Left-dominant forms exist.')],
 'Inflammation and inherited cardiomyopathy can overlap',
 '**DSP-related disease can have a left-dominant scar phenotype with recurrent injury episodes.**',
 ['The phenotype may not resemble classic right-dominant ARVC.', 'Family history and variant classification are important.'],
 '**Assess rhythm risk and relatives as well as the acute chest-pain episode.**',
 ['CMR and ambulatory rhythm data contribute to management.', 'Do not assume an apparent myocarditis label excludes a heritable substrate.'],
 [['DSP cardiomyopathy','Can be LV dominant with inflammatory episodes'],['Classic ARVC image','Does not capture every phenotype'],['Follow-up','Scar, function, arrhythmia and family assessment']], [C,M], 'clinical_scenario')
q('Which approach is most appropriate when diagnosing arrhythmogenic right ventricular cardiomyopathy?',
 'Integrate structural, functional, electrical, tissue and familial evidence rather than rely on one imaging feature',[
 ('Diagnose it from one borderline RV dimension alone','RV dimensions vary with body size and training, and one borderline value lacks specificity.'),
 ('Exclude it whenever a single ECG is normal','Early or intermittent disease may not produce a diagnostic resting ECG.'),
 ('Treat all RV-origin PVCs as proof of ARVC','Idiopathic RV outflow ectopy can occur without cardiomyopathy.')],
 'ARVC diagnosis requires a convergent pattern',
 '**Multiple independent domains improve specificity.**',
 ['Regional dysfunction, ventricular size, ECG changes, arrhythmia morphology and family/genetic findings contribute.', 'CMR interpretation requires care to avoid overcalling normal variation.'],
 '**Differentiate a disease substrate from an isolated rhythm focus.**',
 ['Atypical morphology, syncope or family sudden death warrants more detailed assessment.', 'Repeat evaluation can be appropriate when an early phenotype remains uncertain.'],
 [['Single borderline finding','Insufficient alone'],['Convergent domains','Supports a disease diagnosis'],['Isolated typical RVOT ectopy','May be idiopathic']], [C,VA])
q('A 45-year-old patient has unexplained high-grade AV block, ventricular ectopy and bilateral hilar adenopathy. Which myocardial disease is particularly important to assess?',
 'Cardiac sarcoidosis',[
 ('Age-related degenerative conduction disease as the only explanation','The age and systemic granulomatous clues warrant a broader assessment.'),
 ('An isolated concealed accessory pathway','That does not explain AV block and systemic adenopathy.'),
 ('Pure calcific AS without imaging evidence','The combined electrical and systemic presentation suggests another substrate.')],
 'Conduction disease can be a presentation of cardiac sarcoid',
 '**Granulomatous inflammation and scar can involve the basal septum and conduction system.**',
 ['VT, ventricular dysfunction and otherwise unexplained AV block are important clues.', 'Extracardiac disease can provide a safer diagnostic tissue target.'],
 '**Assess inflammation, scar and arrhythmic risk together.**',
 ['CMR and FDG-PET provide complementary information.', 'A need for pacing can coexist with ventricular arrhythmic risk that affects device planning.'],
 [['Unexplained AV block at a young age','Consider inflammatory/infiltrative disease'],['Hilar adenopathy','Supports systemic sarcoid assessment'],['Cardiac evaluation','CMR, PET and rhythm-risk review']], [ref('AHA Scientific Statement: Diagnosis and Management of Cardiac Sarcoidosis (2024)','https://doi.org/10.1161/CIR.0000000000001240'),C], 'clinical_scenario')
q('In suspected cardiac sarcoidosis, what is the main complementary role of properly prepared FDG-PET when CMR has shown scar?',
 'Assess metabolically active inflammation that may guide treatment and response assessment',[
 ('Determine a precise LVOT gradient by Doppler','PET does not perform Doppler gradient measurement.'),
 ('Prove that every LGE region contains active inflammation','LGE can reflect scar and does not necessarily indicate current activity.'),
 ('Replace preparation because normal myocardial glucose uptake is always absent','Physiological myocardial uptake must be suppressed to improve interpretation.')],
 'Scar and activity are related but different questions',
 '**FDG uptake can identify active inflammatory metabolism, while CMR characterizes injury and fibrosis.**',
 ['Appropriate dietary preparation and fasting reduce misleading physiological myocardial uptake.', 'Neither test should be interpreted without the clinical and systemic context.'],
 '**Use activity information as part of a treatment decision.**',
 ['Active inflammation may support immunosuppressive management in a clinically significant phenotype.', 'Residual scar can continue to confer arrhythmic risk even when inflammatory activity falls.'],
 [['CMR LGE','Myocardial injury/scar characterization'],['FDG-PET','Inflammatory activity assessment'],['After activity improves','Scar-related risk can persist']], [ref('AHA Scientific Statement: Cardiac Sarcoidosis (2024)','https://doi.org/10.1161/CIR.0000000000001240')])
q('A man has LV hypertrophy, neuropathic pain, angiokeratomas, proteinuria and low native myocardial T1. Which diagnosis is most likely?',
 'Fabry disease',[
 ('ATTR amyloidosis','Amyloid usually expands extracellular volume and increases rather than characteristically lowers native T1.'),
 ('Uncomplicated sarcomeric HCM','The multisystem storage clues and low T1 require a phenocopy assessment.'),
 ('Hypertension alone','Hypertension does not explain the characteristic skin, nerve and renal findings.')],
 'A hypertrophic phenotype can reflect intracellular storage',
 '**Fabry disease results from deficient alpha-galactosidase A activity associated with GLA variants.**',
 ['Cardiac hypertrophy can coexist with renal, neurological and skin manifestations.', 'Low native T1 supports lipid storage, although fibrosis can alter local values.'],
 '**Confirm the diagnosis with appropriate sex-specific testing and genetics.**',
 ['Enzyme activity is useful in males; females can have nondiagnostic activity and need genetic assessment.', 'Specific treatment depends on disease status and, for chaperone therapy, variant amenability.'],
 [['Fabry','Intracellular storage, often low native T1'],['Amyloid','Extracellular infiltration, often high T1/ECV'],['Sarcomeric HCM','Different etiological pathway']], [C], 'clinical_scenario')
q('A patient with transfusion-related iron overload develops cardiac dysfunction. Which CMR measure is specifically useful for quantifying myocardial iron?',
 'Myocardial T2-star',[
 ('Aortic valve calcium score','That quantifies valve calcium, not myocardial iron.'),
 ('The LVOT pressure gradient alone','A pressure gradient does not measure myocardial iron content.'),
 ('A single EF measurement as a direct iron concentration','EF is a functional consequence and can remain preserved before major dysfunction.')],
 'Iron changes magnetic relaxation properties',
 '**Myocardial iron shortens T2-star, making the measurement useful for burden and treatment monitoring.**',
 ['Lower values indicate greater iron loading within the validated acquisition framework.', 'Serum ferritin and liver iron do not always predict cardiac iron accurately.'],
 '**Identify a treatable cause before advanced dysfunction.**',
 ['Coordinate chelation and hematological treatment with cardiac monitoring.', 'Follow rhythm, function and iron measures rather than relying on one systemic biomarker.'],
 [['T2-star CMR','Myocardial iron assessment'],['Ferritin','Systemic marker with limitations'],['EF','Functional consequence, not direct tissue iron']], [C], 'clinical_scenario')
q('Prominent LV trabeculations are found incidentally in an asymptomatic person with normal function and no family disease. What is the most appropriate interpretation?',
 'Morphology alone does not establish a pathological cardiomyopathy or an anticoagulation indication',[
 ('Every high trabeculation ratio mandates anticoagulation','Thromboembolic treatment needs clinical indications rather than morphology alone.'),
 ('The image proves inevitable progressive HF','Prognosis depends on function, arrhythmia, family context and associated disease.'),
 ('All prominent trabeculation is impossible in healthy adaptation','Hypertrabeculation can occur in physiological or transient settings.')],
 'Hypertrabeculation is a phenotype requiring context',
 '**An imaging ratio alone can overdiagnose disease.**',
 ['Assess ventricular function, scar, arrhythmia, symptoms and family history.', 'Pregnancy and athletic remodeling can alter trabecular appearance.'],
 '**Base treatment on the actual clinical problems.**',
 ['HF, AF, ventricular thrombus or a genetic cardiomyopathy may create specific indications.', 'Avoid a lifelong disease label from an incidental morphological finding without supporting evidence.'],
 [['Trabecular morphology alone','Insufficient for a disease or treatment mandate'],['Dysfunction/scar/arrhythmia','Adds pathological significance'],['Anticoagulation','Requires an appropriate indication']], [C])
q('Simultaneous ventricular pressure recordings show concordant LV and RV systolic pressure changes with respiration in a patient with restrictive filling. Which process does this favor over classic constrictive pericarditis?',
 'Restrictive myocardial disease',[
 ('Classic constriction with marked ventricular interdependence','Classic constriction more characteristically produces respiratory discordance of LV and RV systolic pressure.'),
 ('Atrial flutter as a complete structural diagnosis','An atrial rhythm alone does not explain this differential hemodynamic pattern.'),
 ('Severe AS established by respiratory concordance','Respiratory ventricular concordance is not an AS diagnostic criterion.')],
 'Restriction and constriction can share filling abnormalities but differ in coupling',
 '**Respiratory systolic concordance favors a myocardial restrictive process, whereas discordance supports constriction.**',
 ['Equalized diastolic pressures or a dip-and-plateau pattern alone are less specific.', 'Interpret measurements with correct technique and the patient\'s volume and respiratory state.'],
 '**Integrate invasive findings with tissue and pericardial imaging.**',
 ['Echo tissue velocities, septal motion, CMR and CT can resolve the differential.', 'Mixed myocardial and pericardial disease can occur, particularly after radiation or surgery.'],
 [['Restriction','Respiratory systolic concordance'],['Constrictive pericarditis','Respiratory LV/RV systolic discordance'],['Shared findings','Rapid early filling does not distinguish alone']], [C])

if __name__=='__main__':
    finalize('Cardiology',6,'Cardiomyopathies','cardiology-cardiomyopathies',rows,44)
