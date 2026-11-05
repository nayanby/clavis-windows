"""Original Cardiovascular Pharmacology chapter; direct ChatGPT authorship."""
from qbank_authoring import question, ref, finalize
ACS=ref('2025 ACC/AHA Acute Coronary Syndromes Guideline','https://doi.org/10.1016/j.jacc.2024.11.009')
AF=ref('2023 ACC/AHA/ACCP/HRS Atrial Fibrillation Guideline','https://doi.org/10.1161/CIR.0000000000001193')
HF=ref('2022 AHA/ACC/HFSA Heart Failure Guideline','https://doi.org/10.1161/CIR.0000000000001063')
LIPID=ref('2026 ACC/AHA Multisociety Dyslipidemia Guideline','https://doi.org/10.1161/CIR.0000000000001423')
CCD=ref('2023 AHA/ACC Chronic Coronary Disease Guideline','https://doi.org/10.1016/j.jacc.2023.04.003')
HTN=ref('2024 ESC Elevated Blood Pressure and Hypertension Guideline','https://doi.org/10.1093/eurheartj/ehae178')
VA=ref('2022 ESC Ventricular Arrhythmias Guideline','https://doi.org/10.1093/eurheartj/ehac262')
HIT=ref('ASH 2018 Guideline: Heparin-Induced Thrombocytopenia','https://doi.org/10.1182/bloodadvances.2018024489')
TOX=ref('AHA Resuscitation Guidelines: Special Circumstances, Poisoning','https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-and-pediatric-special-circumstances-of-resuscitation/')
rows=[]
def q(*args,**kwargs):rows.append(question(*args,**kwargs))

q('Which oral P2Y12 inhibitor directly and reversibly blocks the receptor without requiring metabolic activation?',
 'Ticagrelor',[
 ('Clopidogrel','Clopidogrel is a prodrug whose active metabolite irreversibly inhibits P2Y12.'),
 ('Prasugrel','Prasugrel is also a prodrug producing irreversible receptor inhibition.'),
 ('Aspirin','Aspirin acts through platelet cyclooxygenase rather than the P2Y12 receptor.')],
 'P2Y12 agents differ in activation and receptor binding',
 '**Ticagrelor is a direct-acting reversible oral P2Y12 antagonist.**',
 ['Clopidogrel and prasugrel require conversion to active metabolites and inhibit irreversibly.', 'Different activation, potency and offset properties influence selection and interruption planning.'],
 '**A pharmacological distinction does not establish universal clinical superiority.**',
 ['Bleeding, dyspnea, bradyarrhythmia, interactions, adherence and the clinical indication affect ticagrelor suitability.', 'Oral anticoagulation or high bleeding risk can change the preferred antiplatelet regimen.'],
 [['Ticagrelor','Direct, reversible P2Y12 inhibition'],['Clopidogrel/prasugrel','Prodrug, irreversible inhibition'],['Aspirin','Irreversible platelet COX inhibition']], [ACS])
q('A patient taking clopidogrel has CYP2C19 loss-of-function alleles. Which pharmacological effect is expected?',
 'Reduced formation of the active metabolite and less platelet inhibition',[
 ('Increased active-metabolite production with obligatory major bleeding','Loss of activating enzyme function reduces rather than increases activation.'),
 ('No possible effect because clopidogrel directly binds P2Y12 unchanged','Clopidogrel requires metabolic activation.'),
 ('Loss of aspirin-mediated COX inhibition','The genotype effect being tested concerns clopidogrel activation, not aspirin\'s separate target.')],
 'Pharmacogenetics can affect clopidogrel response',
 '**CYP2C19 contributes to conversion of clopidogrel into its active metabolite.**',
 ['Loss-of-function variants can reduce antiplatelet effect.', 'The clinical relevance depends on the indication, ischemic risk and treatment context.'],
 '**A treatment change requires choosing an appropriate alternative, not simply multiplying the dose.**',
 ['Ticagrelor bypasses the need for CYP2C19 activation, while prasugrel has different activation and contraindication considerations.', 'Genotype is one contributor alongside adherence, interactions, absorption and other causes of recurrent events.'],
 [['Clopidogrel loss-of-function metabolism','Reduced active drug exposure'],['Ticagrelor','Direct acting'],['Recurrent ischemia','Assess more than genotype alone']], [ACS], 'clinical_scenario')
q('Which P2Y12 inhibitor offers rapidly reversible intravenous platelet inhibition during PCI when oral treatment is not established?',
 'Cangrelor',[
 ('Ticagrelor','Ticagrelor is an oral direct P2Y12 inhibitor rather than the intravenous agent described.'),
 ('Tirofiban','Tirofiban is intravenous but blocks glycoprotein IIb/IIIa rather than P2Y12.'),
 ('Bivalirudin','Bivalirudin is a direct thrombin inhibitor, not a platelet P2Y12 blocker.')],
 'Intravenous antithrombotic drugs have distinct targets',
 '**Cangrelor provides direct reversible P2Y12 inhibition with rapid onset and offset.**',
 ['It has a selected procedural role when an oral P2Y12 inhibitor has not been given or absorption is problematic.', 'Its short persistence requires planning the transition to an appropriate oral agent.'],
 '**Do not equate all intravenous antithrombotics.**',
 ['A platelet receptor blocker and a coagulation enzyme inhibitor address different pathways.', 'Bleeding risk, timing and transition interactions must be managed according to the selected oral drug.'],
 [['Cangrelor','IV P2Y12 antagonist'],['Tirofiban','IV GP IIb/IIIa antagonist'],['Bivalirudin','IV direct thrombin inhibitor']], [ACS])
q('Why does low-dose aspirin inhibit platelet function for substantially longer than its plasma half-life?',
 'It irreversibly acetylates platelet COX-1, and platelets cannot synthesize enough new enzyme to reverse the effect',[
 ('It reversibly blocks P2Y12 for the full platelet lifespan','Aspirin does not act at the P2Y12 receptor.'),
 ('It irreversibly removes circulating fibrinogen','Its antiplatelet action is not fibrinogen depletion.'),
 ('It remains unchanged in plasma for seven to ten days','The prolonged effect reflects irreversible target modification rather than a comparably long plasma residence.')],
 'Irreversible target inhibition outlasts drug exposure',
 '**Aspirin suppresses thromboxane A2 production through irreversible platelet COX-1 acetylation.**',
 ['Anucleate platelets have limited ability to restore the inhibited pathway.', 'Recovery depends substantially on production of new platelets.'],
 '**Separate platelet inhibition from anticoagulation.**',
 ['Aspirin does not replace indicated anticoagulation for AF or mechanical valves.', 'The persistent effect contributes to procedural and bleeding considerations even after dosing stops.'],
 [['Aspirin','COX-1 and thromboxane pathway'],['P2Y12 inhibitors','ADP receptor pathway'],['Anticoagulants','Coagulation enzyme pathways']], [ACS])
q('Tirofiban inhibits which final common pathway of platelet aggregation?',
 'Fibrinogen-mediated cross-linking through glycoprotein IIb/IIIa',[
 ('ADP binding to P2Y12','This is the target of clopidogrel, prasugrel, ticagrelor and cangrelor.'),
 ('Thrombin catalytic activity','That is the target of a direct thrombin inhibitor such as bivalirudin.'),
 ('Vitamin K epoxide reductase','That is the principal target of warfarin.')],
 'GP IIb/IIIa blockade acts at platelet cross-linking',
 '**Activated GP IIb/IIIa permits fibrinogen to bridge adjacent platelets.**',
 ['Blocking the receptor strongly inhibits aggregation downstream of several activation signals.', 'This potency also creates important bleeding and thrombocytopenia risks.'],
 '**Modern use is selective rather than automatic in every ACS patient.**',
 ['Procedural thrombotic complications can create a role for bailout treatment.', 'Check renal dosing and platelet monitoring requirements for the chosen agent.'],
 [['GP IIb/IIIa inhibitor','Blocks fibrinogen cross-linking'],['P2Y12 inhibitor','Blocks ADP signaling'],['Direct thrombin inhibitor','Blocks thrombin activity']], [ACS])
q('A patient with advanced renal dysfunction needs a rapidly adjustable parenteral anticoagulant for an acute coronary procedure. Which feature often favors unfractionated heparin over standard-dose enoxaparin?',
 'Shorter, titratable action and less dependence on renal clearance',[
 ('Complete absence of any bleeding risk','UFH still causes bleeding and requires careful dose and monitoring decisions.'),
 ('No need for antithrombin to exert its effect','UFH works predominantly through antithrombin.'),
 ('A guarantee that HIT cannot occur','UFH can cause immune HIT and has a higher risk than LMWH in many settings.')],
 'Renal function and reversibility influence heparin selection',
 '**UFH can be titrated using an appropriate assay and has a relatively short duration of action.**',
 ['LMWH exposure can accumulate with renal impairment unless dosing is adjusted.', 'Both agents exert anticoagulant activity through antithrombin, with different anti-Xa and anti-IIa profiles.'],
 '**The choice does not remove the need for monitoring and risk assessment.**',
 ['Review bleeding, platelet trends and the procedural anticoagulation target.', 'If HIT is suspected, neither UFH nor LMWH is an acceptable routine substitute for the other.'],
 [['UFH','Short, adjustable, readily reversible profile'],['LMWH','More predictable dosing but important renal considerations'],['Suspected immune HIT','Use an appropriate non-heparin strategy']], [ACS,HIT], 'clinical_scenario')
q('Which statement about protamine reversal is correct?',
 'It neutralizes UFH more completely than the anti-Xa effect of LMWH',[
 ('It completely reverses every DOAC','Protamine does not reverse direct oral anticoagulants.'),
 ('It is vitamin K and restores new factor synthesis','Protamine binds heparin; vitamin K is a different reversal treatment.'),
 ('It has no potential to cause hypotension or serious reactions','Protamine can cause hypotension and important hypersensitivity or pulmonary vascular reactions.')],
 'The reversal drug must match the anticoagulant',
 '**Protamine binds and neutralizes heparin, but LMWH anti-Xa activity is only partially reversed.**',
 ['Dose selection depends on heparin exposure and time since administration.', 'Excess protamine is not harmless and can itself impair coagulation.'],
 '**Reversal includes supportive bleeding management.**',
 ['Assess bleeding location, timing, renal function and the remaining anticoagulant effect.', 'Do not use protamine as a generic antidote for warfarin or a DOAC.'],
 [['UFH','Substantial neutralization with appropriate protamine'],['LMWH','Incomplete anti-Xa reversal'],['Warfarin/DOAC','Different reversal pathway']], [ACS])
q('Seven days after heparin initiation, a patient develops a platelet fall from 240 to 85 ×10^9/L and a new arterial thrombosis. The 4Ts assessment indicates high-probability HIT. What is appropriate while confirmatory testing is arranged?',
 'Stop all heparin exposure and start an appropriate non-heparin anticoagulant',[
 ('Switch UFH to LMWH','HIT antibodies can cross-react with LMWH; it is not a safe routine substitution.'),
 ('Stop anticoagulation entirely because the platelet count is low','HIT is highly prothrombotic and ordinarily requires non-heparin anticoagulation when not contraindicated.'),
 ('Start warfarin alone immediately before platelet recovery','Early warfarin can worsen the prothrombotic imbalance and is avoided until platelet recovery.')],
 'HIT is a thrombotic immune reaction',
 '**A large platelet fall with the typical timing and new thrombosis warrants immediate action when clinical probability is high.**',
 ['Stop heparin infusions, prophylaxis and heparin flushes.', 'Argatroban, bivalirudin or another guideline-supported non-heparin option is selected according to clinical stability, organ function and context.'],
 '**Do not wait for the laboratory result to manage a high-probability dangerous presentation.**',
 ['Obtain appropriate immunologic and functional testing.', 'Avoid premature warfarin and assess for additional thrombosis.'],
 [['High-probability acute HIT','Stop heparin and use non-heparin anticoagulation'],['LMWH substitution','Not a solution'],['Early warfarin before recovery','Avoid']], [HIT], 'clinical_scenario')
q('Why can warfarin initiation transiently increase thrombosis risk in a susceptible patient?',
 'Protein C activity falls before some longer-lived procoagulant factors have sufficiently declined',[
 ('Warfarin directly activates platelets through P2Y12','Warfarin affects vitamin K-dependent protein synthesis, not direct P2Y12 activation.'),
 ('Warfarin instantly destroys all circulating clotting factors','It inhibits production of functional vitamin K-dependent proteins; existing factors decline according to their half-lives.'),
 ('Protein C is a procoagulant factor that rises immediately','Protein C is an anticoagulant protein and can decline early.')],
 'Different protein half-lives shape warfarin initiation',
 '**Warfarin affects both procoagulant factors and natural anticoagulants.**',
 ['Protein C can fall rapidly relative to some procoagulant factors.', 'This contributes to early hypercoagulability and rare skin necrosis, particularly in susceptible settings.'],
 '**Overlap requirements depend on the clinical indication.**',
 ['Acute VTE treatment requires appropriate initial anticoagulant overlap when warfarin is selected.', 'Do not infer that every low-risk AF initiation automatically needs heparin bridging; that is a separate decision.'],
 [['Warfarin target','Vitamin K-dependent protein production'],['Early protein C decline','Potential transient prothrombotic imbalance'],['Acute VTE initiation','Use appropriate anticoagulant overlap']], [HIT,AF])
q('A patient taking warfarin develops life-threatening intracranial bleeding with markedly elevated INR. Which regimen provides rapid factor replacement and sustained reversal?',
 'Four-factor prothrombin complex concentrate plus intravenous vitamin K',[
 ('Oral vitamin K alone and observation','Vitamin K alone acts too slowly for immediate reversal of life-threatening hemorrhage.'),
 ('Protamine alone','Protamine neutralizes heparin rather than warfarin.'),
 ('A platelet transfusion as the principal INR-reversal treatment','Platelets do not replace the vitamin K-dependent coagulation factors responsible for the elevated INR.')],
 'Rapid and sustained warfarin reversal require complementary treatments',
 '**Four-factor PCC supplies depleted factors immediately, while vitamin K enables sustained synthesis.**',
 ['The combination addresses both the immediate deficiency and the continuing warfarin effect.', 'Bleeding-site management and urgent specialist care occur simultaneously.'],
 '**Match reversal intensity to bleeding severity and urgency.**',
 ['An asymptomatic high INR is managed differently from intracranial hemorrhage.', 'Assess thrombotic risk and the eventual need and timing of anticoagulation resumption after stabilization.'],
 [['PCC','Rapid factor replacement'],['IV vitamin K','Sustained restoration of synthesis'],['Protamine','Heparin-specific reversal']], [ref('2020 ACC Expert Consensus Decision Pathway: Bleeding in Patients on Oral Anticoagulants','https://doi.org/10.1016/j.jacc.2020.04.053')], 'clinical_scenario')
q('Which specific reversal agent binds dabigatran in a patient with life-threatening bleeding?',
 'Idarucizumab',[
 ('Protamine','Protamine targets heparin rather than dabigatran.'),
 ('Vitamin K','Vitamin K restores warfarin-affected factor synthesis but does not neutralize dabigatran.'),
 ('Aspirin','Aspirin inhibits platelet function and is not an anticoagulant reversal drug.')],
 'Dabigatran has a specific binding reversal agent',
 '**Idarucizumab is an antibody fragment that binds dabigatran with high affinity.**',
 ['It can reverse the direct thrombin inhibitor effect in urgent indicated settings.', 'The indication is clinically important bleeding or an emergency procedure, not a mildly abnormal laboratory number alone.'],
 '**Continue full bleeding and renal assessment.**',
 ['Dabigatran exposure is strongly influenced by kidney function.', 'Rebound anticoagulant activity can occur in selected high-exposure situations, so clinical and laboratory reassessment may be required.'],
 [['Dabigatran','Direct thrombin inhibitor'],['Idarucizumab','Specific dabigatran-binding reversal'],['Vitamin K','Warfarin pathway']], [ref('2020 ACC Oral Anticoagulant Bleeding Management Pathway','https://doi.org/10.1016/j.jacc.2020.04.053')])
q('Which DOAC is most dependent on renal elimination and therefore especially sensitive to substantial renal impairment?',
 'Dabigatran',[
 ('Apixaban','Apixaban has a smaller renal clearance fraction than dabigatran, though renal function still matters.'),
 ('Rivaroxaban','Rivaroxaban has important renal considerations but is less predominantly renally cleared than dabigatran.'),
 ('Edoxaban','Edoxaban also requires renal assessment, but dabigatran has the greatest renal dependence among these choices.')],
 'DOACs are not pharmacokinetically interchangeable',
 '**Dabigatran has a large renal elimination component.**',
 ['Accumulation increases bleeding risk when kidney function declines.', 'Agent-specific labeling determines eligibility and dose adjustment.'],
 '**Use the appropriate renal assessment and reassess during illness.**',
 ['An old stable creatinine does not establish safety during acute kidney injury.', 'Also review age, weight, P-glycoprotein interactions and the clinical indication.'],
 [['Dabigatran','High dependence on renal elimination'],['Apixaban','Lower renal fraction, but still requires assessment'],['All DOACs','Apply agent-specific criteria']], [AF])
q('A patient taking simvastatin develops severe myalgia and dark urine shortly after clarithromycin is started. Which interaction most plausibly contributed?',
 'CYP3A4 inhibition increased simvastatin exposure',[
 ('Clarithromycin induced simvastatin clearance','The relevant interaction is inhibition with increased exposure, not induction.'),
 ('Simvastatin neutralized the antibiotic in the intestine','That does not explain statin-related muscle injury.'),
 ('The combination prevented all hepatic uptake of LDL','LDL uptake does not explain the acute myotoxic interaction.')],
 'Drug interactions can convert a tolerated statin dose into toxic exposure',
 '**Simvastatin is vulnerable to strong CYP3A4 inhibition.**',
 ['Markedly increased exposure can cause myopathy or rhabdomyolysis.', 'Assess CK, kidney function, potassium and clinical severity when dark urine and weakness suggest significant muscle injury.'],
 '**Choose an alternative antibiotic or statin strategy rather than accepting a preventable interaction.**',
 ['Review the full medication list, dose and product contraindications.', 'Persistent weakness and CK elevation after withdrawal may require evaluation for a different process such as immune-mediated necrotizing myopathy.'],
 [['Strong CYP3A4 inhibitor plus simvastatin','Increased exposure and myotoxicity risk'],['Dark urine with weakness','Evaluate rhabdomyolysis'],['Long-term plan','Use a tolerated interaction-aware lipid regimen']], [LIPID], 'clinical_scenario')
q('Ezetimibe lowers LDL cholesterol primarily by inhibiting which target?',
 'The intestinal sterol transporter NPC1L1',[
 ('HMG-CoA reductase','This is the statin target.'),
 ('ATP citrate lyase','This is the target of bempedoic acid.'),
 ('PCSK9 messenger RNA','This is the pathway targeted by inclisiran-mediated silencing.')],
 'Complementary lipid drugs act at different sites',
 '**Ezetimibe reduces intestinal sterol absorption through NPC1L1 inhibition.**',
 ['Reduced hepatic sterol delivery promotes increased LDL receptor activity.', 'It can provide additional LDL reduction when combined with a statin.'],
 '**Mechanistic complementarity supports combination treatment.**',
 ['Select treatment according to risk, LDL reduction required and tolerability.', 'Do not assume identical event evidence or effect size for all nonstatin agents.'],
 [['Ezetimibe','NPC1L1 inhibition'],['Statin','HMG-CoA reductase inhibition'],['Bempedoic acid','ATP citrate lyase inhibition']], [LIPID])
q('How do evolocumab and alirocumab lower LDL-C?',
 'They bind circulating PCSK9 and reduce LDL receptor degradation',[
 ('They inhibit intestinal NPC1L1','That is ezetimibe\'s principal target.'),
 ('They directly inhibit platelet P2Y12 receptors','That is an antiplatelet mechanism, not PCSK9 antibody action.'),
 ('They increase hepatic LDL receptor degradation','They preserve receptor recycling rather than promoting degradation.')],
 'PCSK9 antibodies preserve LDL receptor availability',
 '**Less PCSK9-mediated receptor destruction allows more hepatic LDL clearance.**',
 ['The antibodies act extracellularly on circulating PCSK9.', 'They can produce substantial LDL reduction and have cardiovascular outcomes evidence in appropriate high-risk populations.'],
 '**Apply the treatment to residual risk and LDL needs.**',
 ['Assess adherence, injection feasibility, cost and access.', 'A PCSK9 antibody and inclisiran affect the same overall pathway by different pharmacological methods.'],
 [['PCSK9 monoclonal antibody','Binds circulating protein'],['Inclisiran','Reduces hepatic PCSK9 production'],['LDL receptor consequence','Increased receptor recycling and clearance']], [LIPID])
q('Which description best distinguishes inclisiran from a PCSK9 monoclonal antibody?',
 'It uses small interfering RNA to reduce hepatic PCSK9 synthesis',[
 ('It is an oral inhibitor of intestinal cholesterol uptake','That describes neither inclisiran\'s route nor its target.'),
 ('It binds only circulating PCSK9 protein as an antibody','That is the monoclonal antibody strategy, not RNA interference.'),
 ('It acts by direct inhibition of HMG-CoA reductase','That is the statin mechanism.')],
 'Silencing production differs from binding a circulating protein',
 '**Inclisiran directs RNA interference against hepatic PCSK9 messenger RNA.**',
 ['The pharmacological effect permits infrequent maintenance injections after the initial loading schedule.', 'The mechanism is distinct from extracellular protein binding by evolocumab or alirocumab.'],
 '**Separate LDL lowering from demonstrated cardiovascular outcomes.**',
 ['The 2026 guideline describes important LDL-lowering efficacy while cardiovascular outcomes trials are being completed.', 'Do not presume that a similar LDL effect means every clinical endpoint has already been proven for every drug.'],
 [['Inclisiran','PCSK9 synthesis silencing'],['PCSK9 antibodies','Circulating protein binding'],['Evidence assessment','Check lipid and event outcomes separately']], [LIPID])
q('A statin-intolerant patient taking bempedoic acid develops recurrent gout. Which mechanism-related safety issue should be considered?',
 'Bempedoic acid can increase uric acid and gout risk',[
 ('It invariably causes severe hypouricemia','The recognized concern is increased rather than reduced urate.'),
 ('It is a uricosuric substitute for allopurinol','Bempedoic acid is an LDL-lowering drug, not a gout treatment.'),
 ('Gout proves that the drug has no LDL-lowering action','An adverse effect does not negate its separate lipid effect.')],
 'Bempedoic acid has a distinct benefit-risk profile',
 '**ATP citrate lyase inhibition reduces cholesterol synthesis upstream of HMG-CoA reductase.**',
 ['Hepatic activation helps distinguish its muscle exposure from that of statins.', 'Hyperuricemia, gout and tendon-related precautions remain clinically relevant.'],
 '**Choose therapy using the patient\'s comorbidities as well as LDL needs.**',
 ['Review the severity of gout and available lipid-lowering alternatives.', 'Do not interpret statin intolerance as a reason to leave high cardiovascular risk untreated.'],
 [['Bempedoic acid','Oral ATP citrate lyase inhibitor'],['Gout history','Relevant safety consideration'],['Alternative options','Ezetimibe or PCSK9-directed therapy as appropriate']], [LIPID,ref('CLEAR Outcomes: Bempedoic Acid and Cardiovascular Outcomes in Statin-Intolerant Patients','https://doi.org/10.1056/NEJMoa2215024')], 'clinical_scenario')
q('A patient receiving a statin requires a fibrate for a separate severe triglyceride indication. Which choice is generally preferred over gemfibrozil when combination therapy is necessary and renal function permits?',
 'Fenofibrate',[
 ('Gemfibrozil because it has no statin interaction','Gemfibrozil increases exposure to several statins and raises myopathy risk.'),
 ('A second statin added to the first','Combining two statins is not the appropriate strategy for the triglyceride indication.'),
 ('High-dose niacin solely because flushing prevents myopathy','Flushing is not protective, and this rationale is not evidence based.')],
 'Fibrate selection matters when a statin is continued',
 '**Gemfibrozil has more problematic statin interactions than fenofibrate.**',
 ['The combination can increase myopathy and rhabdomyolysis risk.', 'Fenofibrate still requires renal assessment and does not make combination treatment risk free.'],
 '**Confirm why a fibrate is being added.**',
 ['Severe hypertriglyceridemia and pancreatitis risk differ from a routine attempt to raise HDL.', 'Address secondary triglyceride causes, alcohol, glycemic control and diet alongside medication.'],
 [['Gemfibrozil plus statin','Higher interaction concern'],['Fenofibrate when suitable','Usually preferred if a fibrate combination is needed'],['All combinations','Monitor symptoms and renal suitability']], [LIPID], 'clinical_scenario')
q('Which safety signal is relevant when discussing icosapent ethyl with a high-risk patient who has elevated triglycerides despite statin therapy?',
 'An increased risk of atrial fibrillation or flutter and a bleeding signal',[
 ('A complete absence of arrhythmia or bleeding effects','The relevant trial evidence includes these safety considerations.'),
 ('A requirement to replace the statin with the fish-oil product','Icosapent ethyl was studied as an adjunct in a selected statin-treated population.'),
 ('Equivalent cardiovascular benefit from every over-the-counter mixed fish-oil supplement','The evidence cannot be generalized to all formulations or doses.')],
 'Specific formulations have specific outcome evidence',
 '**Icosapent ethyl is a purified EPA preparation with evidence in selected high-risk statin-treated patients.**',
 ['Do not equate it with all mixed EPA/DHA supplements.', 'AF/flutter and bleeding considerations should be included in an individualized discussion.'],
 '**Eligibility and net benefit depend on the patient\'s context.**',
 ['Review triglycerides, cardiovascular risk, concurrent antithrombotics and AF history.', 'Continue foundational lipid and lifestyle treatment.'],
 [['Purified EPA trial regimen','Specific cardiovascular outcomes evidence'],['Mixed supplement products','Not automatically equivalent'],['Safety review','AF/flutter and bleeding']], [LIPID,ref('REDUCE-IT: Cardiovascular Risk Reduction with Icosapent Ethyl','https://doi.org/10.1056/NEJMoa1812792')])
q('A patient develops a persistent dry cough after starting an ACE inhibitor, without angioedema. Which alternative targets the renin-angiotensin pathway while avoiding ACE-mediated bradykinin accumulation?',
 'An angiotensin receptor blocker',[
 ('Another ACE inhibitor as a guaranteed cough-free option','Cough is often a class effect related to ACE inhibition.'),
 ('A beta blocker because it blocks the AT1 receptor','Beta blockers have different targets and do not directly block AT1.'),
 ('A thiazide because it inhibits bradykinin synthesis','Thiazides act on renal sodium transport rather than this mechanism.')],
 'ACE inhibition and AT1 blockade are not identical',
 '**ACE inhibition reduces angiotensin II formation and impairs bradykinin breakdown.**',
 ['Bradykinin-related effects help explain the dry cough.', 'An ARB blocks AT1 signaling without the same ACE-mediated bradykinin effect.'],
 '**Distinguish cough from prior angioedema.**',
 ['Angioedema creates a different safety assessment for future renin-angiotensin treatment.', 'Monitor kidney function and potassium with either ACE inhibitor or ARB treatment.'],
 [['ACE inhibitor','Angiotensin conversion and bradykinin breakdown affected'],['ARB','AT1 receptor blockade'],['Both classes','Renal and potassium monitoring']], [HTN,HF], 'clinical_scenario')

# Additional drug safety and electrophysiology items follow.
q('A patient with bilateral severe renal artery stenosis develops a substantial creatinine rise after ACE inhibitor initiation. Which hemodynamic mechanism best explains the change?',
 'Loss of angiotensin II-mediated efferent arteriolar constriction lowers glomerular filtration pressure',[
 ('Preferential constriction of the afferent arteriole by ACE inhibition','ACE inhibition does not principally cause this afferent constrictor mechanism.'),
 ('Direct crystal precipitation in all renal tubules','That is not the usual ACE inhibitor mechanism in renovascular disease.'),
 ('An immediate increase in aldosterone that raises filtration','ACE inhibition reduces the angiotensin-aldosterone pathway rather than stimulating it.')],
 'Filtration may depend on efferent arteriolar tone',
 '**Severe bilateral renovascular disease can make GFR particularly dependent on angiotensin II.**',
 ['Removing efferent constriction reduces intraglomerular pressure.', 'The same concern can arise with stenosis affecting a solitary functioning kidney.'],
 '**Investigate a substantial renal decline rather than attributing every change to a harmless expected effect.**',
 ['Assess volume depletion, NSAIDs, potassium and other causes of kidney injury.', 'Reassess treatment and the renovascular problem with appropriate specialist input.'],
 [['Angiotensin II','Maintains efferent tone'],['ACE inhibition in critical bilateral stenosis','Can markedly lower filtration pressure'],['Small stable change in other settings','Requires different contextual assessment']], [HTN,HF], 'clinical_scenario')
q('A man with HFrEF develops painful gynecomastia on spironolactone. Kidney function and potassium permit continued MRA therapy. Which substitution can reduce this endocrine adverse effect?',
 'Eplerenone',[
 ('A higher spironolactone dose','The endocrine effect can be dose related and is unlikely to improve with dose escalation.'),
 ('Hydrochlorothiazide as an equivalent MRA','A thiazide is not a mineralocorticoid receptor antagonist or an equivalent disease-modifying substitute.'),
 ('Potassium chloride as an aldosterone antagonist','Potassium supplementation does not block the receptor and can increase hyperkalemia risk.')],
 'Receptor selectivity affects endocrine adverse effects',
 '**Eplerenone is more selective for the mineralocorticoid receptor than spironolactone.**',
 ['Spironolactone also interacts with sex-hormone pathways, contributing to gynecomastia and related effects.', 'A switch can preserve the MRA strategy when the main limitation is an endocrine adverse effect.'],
 '**The substitution does not remove renal or potassium precautions.**',
 ['Continue laboratory monitoring and review interacting medication.', 'Eplerenone has important CYP3A interaction considerations.'],
 [['Spironolactone','More endocrine receptor effects'],['Eplerenone','More selective MRA'],['Both','Hyperkalemia and renal monitoring']], [HF], 'clinical_scenario')
q('An older woman develops confusion and sodium 119 mmol/L two weeks after starting chlorthalidone. Which drug effect contributes to this complication?',
 'Impaired urinary dilution from distal convoluted tubule sodium-chloride transport inhibition',[
 ('Selective blockade of collecting-duct vasopressin receptors','That mechanism promotes aquaresis rather than explaining thiazide-associated impaired dilution.'),
 ('Direct sodium loading through a mineralocorticoid effect','Thiazides promote sodium loss rather than sodium loading.'),
 ('Complete preservation of dilution despite reduced solute transport','The distal dilution defect is a central contributor to thiazide-associated hyponatremia.')],
 'Thiazides can cause clinically important hyponatremia',
 '**Thiazide-type diuretics interfere with sodium chloride transport in a key urinary diluting segment.**',
 ['Older age, low body mass, high water intake and interacting drugs can increase susceptibility.', 'Potassium depletion and volume-related vasopressin release may add to the problem.'],
 '**Severe symptomatic hyponatremia needs urgent controlled management.**',
 ['Stop the culprit and assess symptoms, volume and other causes.', 'Avoid an uncontrolled rapid correction; the immediate treatment and monitoring depend on severity and chronicity.'],
 [['Thiazide exposure','Can impair free-water excretion'],['New confusion with severe low sodium','Urgent assessment'],['Future prescribing','Review recurrence risk and alternatives']], [HTN], 'clinical_scenario')
q('Which combination increases concern for furosemide-related ototoxicity?',
 'Rapid high-dose intravenous administration with renal impairment and concomitant aminoglycoside exposure',[
 ('A stable low oral dose without interacting medication','This is not the characteristic high-risk combination.'),
 ('Slow appropriate administration with normal renal function as a unique mandatory trigger','These factors reduce rather than define the recognized risk.'),
 ('Low LDL cholesterol as the principal mechanism','Lipid concentration is not the central determinant of this toxicity.')],
 'Loop diuretic toxicity depends on exposure and co-medication',
 '**Rapid administration, high exposure and other ototoxic drugs increase hearing-related risk.**',
 ['Renal impairment can increase vulnerability.', 'Aminoglycosides add an important interaction concern.'],
 '**Use an appropriate route and administration rate for the formulation and indication.**',
 ['Review renal function, electrolyte response and hearing symptoms.', 'Avoid unnecessary ototoxic combinations while still treating clinically important congestion.'],
 [['Rapid high IV exposure','Greater ototoxicity concern'],['Aminoglycoside co-treatment','Additional risk'],['Renal impairment','Requires particular caution']], [ref('Furosemide injection prescribing information: ototoxicity and interactions','https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8e0bac29-5a8b-4d4e-93b3-2e21eb3b0650')])
q('A patient taking dapagliflozin is scheduled for elective surgery with prolonged fasting. What preoperative medication action is appropriate?',
 'Withhold dapagliflozin for at least three days before the procedure when possible',[
 ('Continue through fasting because a normal glucose excludes ketoacidosis','SGLT2-associated ketoacidosis can occur without marked hyperglycemia.'),
 ('Stop only on arrival in the operating room as sufficient routine preparation','The recommended interruption begins earlier than the procedure itself.'),
 ('Replace it with a second SGLT2 inhibitor during fasting','Switching within the class does not remove the risk.')],
 'SGLT2-related ketosis can be euglycemic',
 '**Surgery and prolonged fasting can increase ketoacidosis risk during SGLT2 inhibition.**',
 ['Dapagliflozin, empagliflozin and canagliflozin generally require at least three days of preoperative interruption.', 'Ertugliflozin generally requires at least four days.'],
 '**Restart only after the relevant risk factors have resolved and intake is adequate.**',
 ['If urgent surgery prevents a planned hold, use appropriate monitoring and clinical assessment rather than assuming no risk.', 'Symptoms compatible with ketoacidosis warrant ketone and acid-base assessment even when glucose is not very high.'],
 [['Dapagliflozin/empagliflozin/canagliflozin','Hold at least three days before planned surgery'],['Ertugliflozin','Hold at least four days'],['Normal glucose','Does not exclude SGLT2-associated ketoacidosis']], [ref('Dapagliflozin prescribing information: temporary interruption for surgery','https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=ef9e9c8c-5460-4193-952a-0c249dd071bd'),ref('2024 ACC/AHA Perioperative Cardiovascular Management Guideline','https://doi.org/10.1016/j.jacc.2024.06.013')], 'clinical_scenario')
q('A patient with acute digoxin poisoning develops a life-threatening ventricular arrhythmia and hyperkalemia. Which specific treatment is indicated?',
 'Digoxin-specific immune Fab',[
 ('Protamine','Protamine neutralizes heparin and does not bind digoxin.'),
 ('Vitamin K','Vitamin K does not reverse cardiac glycoside toxicity.'),
 ('A higher digoxin dose to suppress ectopic automaticity','More digoxin worsens the toxic mechanism.')],
 'Life-threatening cardiac glycoside toxicity has a specific antidote',
 '**Digoxin immune Fab binds free glycoside and reduces its toxic activity.**',
 ['Severe arrhythmia and important hyperkalemia are concerning manifestations in acute poisoning.', 'Toxicity can involve increased automaticity together with AV conduction block.'],
 '**Continue intensive supportive and biochemical monitoring.**',
 ['Potassium can fall after effective reversal, so repeated monitoring is necessary.', 'Routine total digoxin assays after Fab can be misleading because they may measure bound as well as free drug.'],
 [['Severe digoxin toxicity','Give specific immune Fab when indicated'],['After reversal','Monitor potassium and rhythm'],['Post-Fab total drug level','May not reflect active free digoxin']], [TOX], 'clinical_scenario')
q('A patient with a stable warfarin dose starts amiodarone. What change should be anticipated?',
 'An increased anticoagulant effect requiring closer INR monitoring and often a warfarin dose reduction',[
 ('A predictable loss of anticoagulation requiring automatic dose doubling','Amiodarone commonly inhibits warfarin metabolism and raises rather than lowers its effect.'),
 ('No interaction because amiodarone acts only in the heart','Amiodarone has important metabolic and transporter interactions.'),
 ('Protamine should be given prophylactically with each amiodarone dose','Protamine does not reverse warfarin and is not prophylaxis for this interaction.')],
 'Amiodarone interactions can evolve over time',
 '**Inhibition of warfarin metabolism can increase INR and bleeding risk.**',
 ['The magnitude and timing vary, so follow INR rather than assuming one universal final dose.', 'Amiodarone\'s long persistence means interactions may continue after a dose change or discontinuation.'],
 '**Plan monitoring before combining the drugs.**',
 ['Review other interacting medications, diet and renal or hepatic illness.', 'Adjust warfarin according to measured response and the anticoagulation service\'s plan.'],
 [['Amiodarone added','INR may rise'],['Warfarin adjustment','Individualize using closer monitoring'],['Amiodarone stopped','Interaction may persist']], [AF], 'clinical_scenario')
q('A patient on long-term amiodarone develops progressive dyspnea, dry cough and new interstitial pulmonary opacities. Which adverse effect requires assessment?',
 'Amiodarone-related pulmonary toxicity',[
 ('An expected harmless effect that never requires changing treatment','Potential pulmonary toxicity can be serious and requires evaluation.'),
 ('Aspirin-induced platelet inhibition as the direct explanation','That mechanism does not explain this characteristic interstitial lung presentation.'),
 ('A guaranteed bacterial infection solely from the radiograph','Infection is a differential diagnosis, but the drug exposure and pattern require toxicity assessment.')],
 'Amiodarone has important extracardiac toxicity',
 '**New respiratory symptoms on chronic treatment warrant assessment for drug-related lung injury.**',
 ['HF, infection and other lung disease must also be evaluated.', 'Pulmonary toxicity can occur despite a seemingly appropriate daily dose.'],
 '**Review ongoing indication and monitor the broader toxicity profile.**',
 ['Thyroid and liver effects, bradycardia and drug interactions are also relevant.', 'A suspected serious adverse effect requires specialist-guided withdrawal and treatment planning; the long half-life means immediate drug clearance should not be expected.'],
 [['Pulmonary','New cough, dyspnea or interstitial change'],['Thyroid/liver','Periodic and symptom-triggered assessment'],['Electrical','Bradycardia and conduction/QT effects']], [AF], 'clinical_scenario')
q('Why does declining renal function increase concern when a patient is taking sotalol?',
 'Reduced clearance can increase exposure, QT prolongation and torsades risk',[
 ('Sotalol becomes a selective coronary vasodilator in renal failure','Its beta-blocking and repolarization effects do not change into that mechanism.'),
 ('Renal failure completely prevents QT prolongation','Reduced clearance can worsen rather than eliminate QT risk.'),
 ('No dose or interval reassessment is ever required','Renal function is central to safe sotalol dosing and follow-up.')],
 'Sotalol combines beta blockade with repolarization effects',
 '**Renal elimination links kidney function to drug exposure and proarrhythmia.**',
 ['QT prolongation, bradycardia and electrolyte depletion can interact to increase torsades risk.', 'Check potassium and magnesium as well as renal function and ECG findings.'],
 '**Apply the product-specific initiation and adjustment protocol.**',
 ['Acute illness or diuretic changes can alter risk after a previously stable prescription.', 'Avoid combining additional QT-prolonging drugs without a clear monitored plan.'],
 [['Reduced renal clearance','Greater exposure'],['Long QT plus bradycardia or low potassium','Higher torsades concern'],['Monitoring','QT, renal function and electrolytes']], [AF,VA])
q('During exercise, a patient taking flecainide develops more marked QRS widening than at rest. Which property explains this?',
 'Use-dependent sodium-channel blockade that becomes more prominent at faster activation rates',[
 ('Selective If inhibition at the sinus node','That is ivabradine\'s principal mechanism.'),
 ('Pure beta-2 agonism','Flecainide is not a beta-2 agonist.'),
 ('A direct anticoagulant effect on thrombin','Its electrical effects are not caused by anticoagulation.')],
 'Class Ic conduction slowing is rate dependent',
 '**Flecainide dissociates relatively slowly from sodium channels, increasing block during rapid repeated activation.**',
 ['The result can be more ventricular conduction delay and wider QRS complexes at faster rates.', 'This is distinct from a purely AV nodal rate-slowing effect.'],
 '**Assess excessive widening and the structural substrate.**',
 ['Check dose, renal function, interactions and underlying conduction disease.', 'Prior MI or significant ventricular scar remains a major reason to avoid the drug.'],
 [['Faster rate on flecainide','More sodium-channel block and QRS widening'],['Structural scar','Greater proarrhythmic concern'],['Clinical review','ECG and exposure assessment']], [AF,VA], 'clinical_scenario')
q('Which antiarrhythmic is a class Ib sodium-channel blocker used intravenously in selected ventricular arrhythmia settings?',
 'Lidocaine',[
 ('Flecainide','Flecainide is class Ic with different kinetics and structural-heart-disease restrictions.'),
 ('Sotalol','Sotalol combines beta blockade with class III repolarization effects.'),
 ('Verapamil','Verapamil is a calcium-channel blocker, not class Ib.')],
 'Class Ib differs from other rhythm-drug categories',
 '**Lidocaine has rapid sodium-channel binding kinetics and preferential effects in depolarized ventricular tissue.**',
 ['It has selected uses in ventricular arrhythmias, including an alternative drug role during refractory VF/pulseless VT resuscitation.', 'It is not routine oral maintenance treatment of AF.'],
 '**Use drug treatment within the relevant electrical and clinical pathway.**',
 ['Defibrillation and CPR remain central for shockable arrest.', 'Neurological toxicity and altered clearance in severe illness are important during infusion.'],
 [['Lidocaine','Class Ib'],['Flecainide','Class Ic'],['Sotalol','Beta blockade plus class III']], [VA,TOX])
q('Which beta blocker is particularly useful when very rapid titration and a short offset are needed because it is metabolized by red-cell esterases?',
 'Esmolol',[
 ('Nadolol','Nadolol is long acting and has important renal elimination.'),
 ('Propranolol','Propranolol is not the ultra-short intravenous esterase-metabolized agent described.'),
 ('Bisoprolol','Bisoprolol is a longer-acting oral beta blocker rather than this rapidly reversible infusion option.')],
 'A short half-life can improve controllability',
 '**Esmolol is an intravenous beta-1-selective blocker with rapid metabolism.**',
 ['Its short duration allows close titration when beta blockade is appropriate.', 'Selectivity is dose dependent and does not eliminate bronchospasm or cardiac adverse-effect concerns.'],
 '**Short action does not make beta blockade suitable in every unstable patient.**',
 ['Assess perfusion, ventricular function, AV conduction and the reason for tachycardia.', 'Compensatory tachycardia from shock or major bleeding requires treatment of the cause rather than reflex suppression.'],
 [['Esmolol','Short titratable IV effect'],['Nadolol','Longer duration, renal considerations'],['Any beta blocker','Assess physiology and contraindications']], [AF,HTN])
q('A patient develops ankle edema on amlodipine without weight gain, elevated JVP or pulmonary congestion. Which mechanism best explains this common adverse effect?',
 'Preferential precapillary arteriolar dilation increases capillary hydrostatic pressure',[
 ('Primary severe sodium retention as the obligatory mechanism','Dihydropyridine edema is often a local hemodynamic effect rather than generalized sodium overload.'),
 ('Direct blockade of lymphatic valves in every patient','That is not the principal pharmacological mechanism.'),
 ('Loss of platelet P2Y12 signaling','Amlodipine does not cause edema through an antiplatelet mechanism.')],
 'CCB edema is often a capillary pressure problem',
 '**Arteriolar dilation without matched venous dilation can increase dependent capillary filtration.**',
 ['The edema can occur without the systemic congestion findings of HF.', 'Dose and prolonged upright posture can influence severity.'],
 '**Do not automatically escalate a loop diuretic for every swollen ankle.**',
 ['Assess for cardiac, renal, venous and other causes before attributing the finding to medication.', 'Dose adjustment, switching treatment or a suitable complementary antihypertensive may be considered.'],
 [['Amlodipine-related dependent edema','Precapillary dilation mechanism'],['HF congestion','Often broader fluid-overload findings'],['Management','Assess cause before reflex diuresis']], [HTN], 'clinical_scenario')
q('A patient taking metoprolol develops marked bradycardia and AV block after verapamil is added. What explains the interaction?',
 'Additive suppression of AV conduction and cardiac contractility',[
 ('Mutual cancellation of all cardiac effects','The effects can reinforce one another rather than cancel.'),
 ('Verapamil-induced acceleration of accessory-pathway conduction as the sole explanation','The stated interaction is combined nodal and myocardial depression, not a proven accessory-pathway rhythm.'),
 ('Metoprolol reversal of calcium-channel blockade','A beta blocker is not an antidote to verapamil.')],
 'Two rate-slowing classes can produce excessive nodal suppression',
 '**Beta blockers and non-DHP CCBs can combine to cause bradycardia, AV block and hypotension.**',
 ['Reduced ventricular function increases concern about combined negative inotropy.', 'Dose, age, kidney or liver illness and other rate-slowing drugs can modify susceptibility.'],
 '**Review all medications when new bradycardia appears.**',
 ['Assess symptoms and perfusion, obtain an ECG and provide acute support when needed.', 'Amlodipine has a different nodal profile and should not be conflated with verapamil or diltiazem.'],
 [['Beta blocker plus verapamil/diltiazem','Additive nodal and inotropic suppression'],['Dihydropyridine CCB','Predominantly vascular effect'],['Symptomatic block','Urgent clinical and medication assessment']], [AF,HTN], 'clinical_scenario')
q('A patient on prolonged hydralazine develops arthralgia, fever and positive antihistone antibodies without another clear explanation. Which drug reaction is most likely?',
 'Hydralazine-associated drug-induced lupus',[
 ('A guaranteed IgE-mediated anaphylactic reaction','The chronic systemic and serologic pattern is not the usual acute anaphylaxis presentation.'),
 ('An expected therapeutic response that needs no review','These findings suggest an adverse immune reaction rather than desired blood pressure treatment.'),
 ('Digoxin-related visual toxicity','That drug and characteristic symptom pattern are not described.')],
 'Hydralazine can produce autoimmune adverse effects',
 '**Drug-induced lupus is a recognized complication of hydralazine exposure.**',
 ['Dose, duration and patient susceptibility influence risk.', 'Hydralazine can also cause more serious immune syndromes, including ANCA-associated vasculitis, so renal or pulmonary findings require careful assessment.'],
 '**Evaluate organ involvement and reconsider the culprit medication.**',
 ['Do not rely on one antibody result alone to define the full syndrome.', 'Withdrawal and further treatment depend on clinical severity and the final diagnosis.'],
 [['Drug-induced lupus pattern','Systemic symptoms with compatible exposure and serology'],['Renal/pulmonary injury','Assess alternative or additional immune disease'],['Treatment review','Address the culprit and severity']], [HTN], 'clinical_scenario')
q('Why is oral minoxidil for resistant hypertension often accompanied by a loop diuretic and a beta blocker when appropriate?',
 'It can cause sodium-water retention and reflex sympathetic tachycardia',[
 ('It causes obligatory severe volume depletion and bradycardia','Its compensatory effects are generally in the opposite direction.'),
 ('The combination prevents every case of hypertrichosis','Diuretic and beta-blocker co-treatment addresses hemodynamic effects, not guaranteed prevention of hair growth.'),
 ('Minoxidil is itself a complete beta blocker and loop diuretic','It is a potent arteriolar vasodilator, not a combination of those mechanisms.')],
 'Potent arteriolar dilation triggers compensatory responses',
 '**Reflex sympathetic activity and renal sodium retention can limit a direct vasodilator\'s net effect.**',
 ['Rate control and adequate diuresis may be needed in resistant hypertension.', 'Pericardial effusion and hypertrichosis are additional important minoxidil safety considerations.'],
 '**Reserve the strategy for an appropriately evaluated resistant phenotype.**',
 ['Confirm adherence, out-of-office pressure and secondary causes.', 'Monitor pressure, heart rate, weight and fluid status rather than assuming the added medications eliminate all adverse effects.'],
 [['Minoxidil','Potent arteriolar vasodilation'],['Reflex tachycardia','May require beta blockade'],['Fluid retention','May require loop diuresis']], [HTN])
q('A patient abruptly stops chronic clonidine and develops severe hypertension, tachycardia and agitation. Which mechanism best explains the presentation?',
 'Rebound sympathetic activation after withdrawal of central alpha-2 agonism',[
 ('Persistent irreversible peripheral alpha blockade','Clonidine is a central sympatholytic agonist, not an irreversible peripheral alpha blocker.'),
 ('An anticoagulant rebound caused by loss of vitamin K inhibition','Clonidine does not act through vitamin K.'),
 ('A predictable diuretic withdrawal hyponatremia syndrome','The characteristic problem is sympathetic rebound hypertension, not that electrolyte mechanism.')],
 'Central sympatholytic withdrawal can be dangerous',
 '**Abrupt clonidine cessation can produce a catecholamine-mediated blood pressure surge.**',
 ['Missed doses, vomiting or prescribing interruption can precipitate the syndrome.', 'Concurrent beta blockade complicates withdrawal planning and should be managed carefully.'],
 '**Plan gradual discontinuation with an individualized replacement strategy.**',
 ['Assess the severity of hypertension and possible acute organ injury.', 'Medication reconciliation should identify interrupted treatment rather than labeling the episode unexplained resistant hypertension.'],
 [['Clonidine during treatment','Central sympathetic suppression'],['Abrupt withdrawal','Rebound sympathetic activation'],['Planned discontinuation','Taper with a coordinated medication plan']], [ref('Clonidine hydrochloride prescribing information: withdrawal','https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=a32f4b18-1090-4d79-a56b-39c0cf366bbc&type=display')], 'clinical_scenario')
q('During a prolonged high-dose sodium nitroprusside infusion, a patient develops otherwise unexplained severe lactic acidosis. Which toxicity should be suspected?',
 'Cyanide toxicity impairing cellular oxygen utilization',[
 ('Vitamin K depletion as the immediate mechanism','Nitroprusside toxicity is not primarily vitamin K antagonism.'),
 ('Direct P2Y12 blockade causing intracellular hypoxia','Nitroprusside does not act through P2Y12.'),
 ('A guaranteed harmless lactate rise unrelated to the drug','Severe unexplained lactate elevation during high exposure is a potentially important toxicity signal.')],
 'Nitroprusside can generate toxic metabolites',
 '**Cyanide accumulation can impair oxidative metabolism and produce lactic acidosis.**',
 ['High infusion rates and impaired detoxification increase concern.', 'Thiocyanate accumulation is a related but distinct risk, particularly with prolonged use and renal impairment.'],
 '**Stop and evaluate a suspected toxic infusion promptly.**',
 ['Use an alternative pressure-control strategy and obtain urgent toxicology-guided management.', 'Continuous pressure monitoring and attention to dose and duration are essential even before toxicity develops.'],
 [['Cyanide toxicity','Impaired oxygen utilization and lactic acidosis'],['Thiocyanate accumulation','Particular concern with prolonged exposure and renal dysfunction'],['Nitroprusside use','Titration and close monitoring']], [ref('Sodium nitroprusside prescribing information: cyanide and thiocyanate toxicity','https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=820eadcb-1230-4b17-a652-e69b52b3c12f')], 'clinical_scenario')
q('Why is a daily nitrate-free interval often incorporated into long-acting nitrate treatment for stable angina?',
 'To reduce pharmacological tolerance from continuous nitrate exposure',[
 ('To restore platelet COX-1 synthesis','Nitrate tolerance is not the aspirin platelet-recovery mechanism.'),
 ('To prevent all interactions with PDE5 inhibitors regardless of timing','A planned nitrate-free period does not make unsafe PDE5 overlap automatically acceptable.'),
 ('To guarantee a mortality benefit from nitrate monotherapy','Nitrates are primarily symptom-relieving treatment, not a universal mortality-reducing monotherapy.')],
 'Continuous nitrate exposure can lose antianginal effect',
 '**A planned low-nitrate interval helps limit tolerance.**',
 ['Schedule the regimen around the patient\'s usual symptom pattern.', 'Tolerance mechanisms involve several vascular and neurohormonal adaptations rather than a simple need for ever-higher dosing.'],
 '**Maintain an appropriate overall angina plan.**',
 ['Review rebound symptoms and the need for complementary antianginal treatment.', 'Continue risk reduction and avoid dangerous PDE5 inhibitor overlap.'],
 [['Continuous long-acting exposure','Tolerance can develop'],['Scheduled low-nitrate interval','Helps preserve effect'],['Nitrate role','Symptom control within a broader CAD regimen']], [CCD])
q('A patient taking ranolazine is prescribed clarithromycin. Which prescribing action is appropriate?',
 'Avoid the combination because strong CYP3A inhibition can markedly increase ranolazine exposure and QT risk',[
 ('Double ranolazine because clarithromycin accelerates clearance','Clarithromycin inhibits rather than accelerates CYP3A-mediated clearance.'),
 ('Continue unchanged because ranolazine has no QT effect','Ranolazine can prolong QT, particularly with increased exposure.'),
 ('Add sotalol to prevent the interaction-related QT change','Another QT-prolonging drug can worsen proarrhythmic risk.')],
 'Antianginal hemodynamic neutrality does not mean absence of electrical risk',
 '**Strong CYP3A inhibitors are contraindicated with ranolazine.**',
 ['Ranolazine is mainly metabolized by CYP3A.', 'Moderate inhibitors such as diltiazem require a labeled dose limit rather than being treated as identical to strong inhibitors.'],
 '**Check the whole medication list before adding a common antibiotic.**',
 ['Choose an appropriate alternative and assess QT, renal function and other risk factors.', 'The ability to treat angina with little heart-rate or pressure reduction does not remove interaction precautions.'],
 [['Strong CYP3A inhibition','Avoid ranolazine combination'],['Moderate CYP3A inhibition','Apply labeled dose limits'],['Additional QT risk','Review and minimize contributors']], [ref('Ranolazine prescribing information: CYP3A interactions and QT prolongation','https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=00979fb3-d70f-493d-94ca-2914cbadaa9d')], 'clinical_scenario')

if __name__=='__main__':
    finalize('Cardiology',4,'Cardiovascular Pharmacology','cardiology-pharmacology',rows,40)
