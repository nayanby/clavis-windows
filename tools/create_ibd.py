"""Original Inflammatory Bowel Disease chapter."""
from qbank_authoring import question,ref,finalize
B=ref('BSG 2025 Adult IBD Guideline','https://doi.org/10.1136/gutjnl-2024-334395')
U=ref('ECCO 2026 Ulcerative Colitis Medical Treatment Guideline','https://doi.org/10.1093/ecco-jcc/jjag066')
CD=ref('ACG 2025 Crohn Disease Guideline: official update summary','https://gi.org/journals-publications/ebgi/zhai_dalal_sep2025/')
UC=ref('ACG 2025 UC Guideline: official ASUC algorithm','https://webfiles.gi.org/links/virtgrandround/2025ACGVGR34JointRubinAfzali.pdf')
CA=ref('ECCO 2023 IBD and Malignancies Guideline','https://doi.org/10.1093/ecco-jcc/jjac187')
rows=[]
def q(*args,**kwargs):rows.append(question(*args,**kwargs))

q('An untreated patient has continuous superficial inflammation extending proximally from the rectum, with crypt architectural distortion and no small-bowel or perianal disease. Which diagnosis is favored?',
 'Ulcerative colitis',[
 ('Crohn disease solely because crypt distortion is present','Crypt chronicity occurs in IBD generally; the continuous rectal pattern favors UC.'),
 ('Acute self-limited infectious colitis as the only explanation','Chronic architectural change and the distribution support chronic IBD, although infection must be assessed.'),
 ('Microscopic colitis as the best fit for visibly ulcerated continuous disease','Microscopic colitis usually has a different clinical and endoscopic pattern.')],
 'Distribution and depth help classify IBD',
 '**Continuous rectal-to-proximal mucosal disease is characteristic of untreated UC.**',
 ['Crohn can have skip areas and transmural complications.', 'Treatment can alter distribution, so exceptions should not be mistaken for a rigid diagnostic rule.'],
 '**Confirm with a complete clinicopathological assessment.**',
 ['Exclude infection and obtain appropriately mapped biopsies.', 'A single histological feature rarely determines the entire classification.'],
 [['UC','Typically continuous mucosal colitis from rectum'],['Crohn','Discontinuous and potentially transmural'],['Classification','Clinical, endoscopic and histological integration']], [B], 'clinical_scenario')
q('Which feature particularly supports Crohn disease over uncomplicated UC?',
 'A transmural enteric fistula associated with segmental ileal inflammation',[
 ('Rectal bleeding alone','Bleeding occurs in several colonic disorders.'),
 ('Cryptitis alone','Active crypt inflammation is not specific to Crohn.'),
 ('An elevated CRP alone','CRP measures inflammation, not a unique IBD subtype.')],
 'Transmural disease creates distinctive complications',
 '**Crohn inflammation can extend beyond the mucosa and cause fistulas, abscesses and strictures.**',
 ['Small-bowel involvement and perianal disease add support.', 'Granulomas can help when present but are not required.'],
 '**Map disease extent and complication anatomy.**',
 ['Enterography and pelvic imaging are selected according to the presentation.', 'The complication may require drainage or surgery as well as medication.'],
 [['Transmural inflammation','Fistula/abscess risk'],['Mucosal colitis','Typical UC depth'],['Assessment','Extent plus complications']], [B,CD])
q('What is the best interpretation of an elevated fecal calprotectin in a patient with chronic diarrhea?',
 'It supports intestinal inflammation but is not specific for IBD',[
 ('It proves Crohn disease and excludes infection','Infection and other inflammatory lesions can raise the value.'),
 ('It is a direct measure of anxiety-related bowel symptoms','It is a neutrophil-associated inflammatory marker.'),
 ('A normal result excludes every isolated small-bowel phenotype with certainty','Sensitivity depends on disease location and context.')],
 'A biomarker changes probability rather than naming a disease',
 '**Calprotectin is useful in distinguishing inflammatory from many noninflammatory presentations.**',
 ['It also helps monitor known disease.', 'NSAIDs, infection and neoplasia can confound interpretation.'],
 '**Investigate according to pretest probability and alarm features.**',
 ['Endoscopy or enterography may still be needed.', 'Do not escalate immunosuppression from one unexplained number alone.'],
 [['Elevated result','Inflammation more likely'],['Specific diagnosis','Requires further evidence'],['Known IBD','Useful objective monitoring tool']], [B])
q('A patient with established UC develops an acute diarrhea flare after antibiotics. What should be assessed before assuming all worsening is immune activity?',
 'Clostridioides difficile and other relevant enteric infection',[
 ('Only a serum albumin level as an infection exclusion test','Albumin reflects severity and nutrition but does not exclude infection.'),
 ('A positive IBD history as proof that infection cannot coexist','Both can occur together.'),
 ('A normal previous colonoscopy as permanent protection from infection','Past imaging does not remove current infection risk.')],
 'Infection can mimic or aggravate an IBD flare',
 '**Stool testing is important in acute worsening, especially with compatible exposure.**',
 ['The choice of assay and interpretation must distinguish active infection from colonization.', 'Severe disease may require assessment for additional tissue infections.'],
 '**Avoid automatic treatment escalation without reassessment.**',
 ['Correct fluids and electrolytes and evaluate severity.', 'Immune treatment and infection treatment may both be needed in selected cases.'],
 [['Worsening known IBD','Do not assume one mechanism'],['C. difficile risk','Test in the appropriate syndrome'],['Treatment','Severity and cause informed']], [B,UC], 'clinical_scenario')
q('A patient has mildly active ulcerative proctitis confined to the distal rectum. Which induction treatment is generally preferred?',
 'Rectal mesalamine',[
 ('Oral budesonide targeted only to the terminal ileum','That formulation does not target the rectal lesion effectively.'),
 ('Azathioprine as the fastest induction option','Thiopurines are slow acting and not the preferred initial induction for mild proctitis.'),
 ('Routine colectomy before topical treatment','That is not appropriate for the stated mild localized disease.')],
 'Match drug delivery to disease location',
 '**Rectal 5-ASA directly treats the involved mucosa and is effective in mild proctitis.**',
 ['Adherence and patient ability to use the formulation matter.', 'A topical steroid can be an alternative in selected nonresponse or intolerance.'],
 '**Reassess if the disease is more extensive or severe.**',
 ['Do not infer extent from symptoms alone.', 'Persistent symptoms require checking adherence, infection and objective activity.'],
 [['Proctitis','Rectal mesalamine'],['More extensive disease','Oral plus selected rectal strategy'],['Severe disease','Different induction pathway']], [B,U], 'clinical_scenario')
q('A patient with mildly-to-moderately active left-sided UC is starting 5-ASA. Which strategy can be more effective than oral treatment alone?',
 'Combine oral mesalamine with rectal mesalamine',[
 ('Use only an ileal-release formulation designed for ileocecal Crohn','The delivery site is mismatched.'),
 ('Use a thiopurine loading dose as immediate rescue','Thiopurines are not rapid induction agents.'),
 ('Continue systemic corticosteroids indefinitely as the default maintenance','Steroids are not maintenance therapy.')],
 'A topical component can improve distal drug delivery',
 '**Left-sided disease can benefit from both oral and rectal 5-ASA exposure.**',
 ['Formulation and patient acceptance influence effectiveness.', 'Optimize the prescribed regimen before declaring failure in a mild phenotype.'],
 '**Do not delay escalation when activity is genuinely moderate or severe.**',
 ['Persistent bleeding, systemic burden or high-risk features can justify another approach.', 'Assess objective response and steroid-free control.'],
 [['Mild left-sided UC','Oral plus rectal 5-ASA'],['Poor adherence/delivery','Correct implementation'],['High-risk active disease','Consider appropriate advanced pathway']], [B,U], 'clinical_scenario')
q('A patient has moderate-to-severe UC with substantial inflammatory burden. Which current treatment principle is correct?',
 'Appropriate advanced therapy can be selected early rather than requiring failure of every slow conventional drug first',[
 ('Every patient must remain on ineffective 5-ASA for years before a biologic','Mandatory prolonged ineffective step-up can delay disease control.'),
 ('All advanced agents have identical efficacy and safety in every prior-exposure group','Prior treatment and patient factors affect selection.'),
 ('Symptom relief alone is the only treatment target','Objective inflammatory control and steroid-free remission matter.')],
 'Current care is risk and target oriented',
 '**Disease severity, prognosis, prior exposure and preferences guide therapy selection.**',
 ['Biologics and small molecules offer different mechanisms.', 'Safety profile, speed, extraintestinal disease and access influence choice.'],
 '**Define the monitoring plan at initiation.**',
 ['Assess symptoms and objective markers, with endoscopic evaluation when appropriate.', 'Do not confuse a short steroid response with a durable maintenance strategy.'],
 [['Moderate/severe disease','Select an effective appropriate advanced strategy'],['Prior exposure','Changes comparative choices'],['Target','Steroid-free clinical and objective control']], [U,ref('AGA Living Guideline: Moderate-to-Severe UC','https://gastro.org/news/new-guideline-provides-practical-guidance-for-ulcerative-colitis-therapy-selection/')])
q('Which statement about systemic corticosteroids in IBD is correct?',
 'They can induce remission but should not be used as routine long-term maintenance',[
 ('A low continuous dose is the preferred maintenance for every responder','Long-term toxicity and disease-control limitations make this inappropriate.'),
 ('They replace the need for a steroid-sparing plan','Dependence is a reason to reassess maintenance treatment.'),
 ('They provide no important adverse effects if symptoms improve','Infection, bone, metabolic and other risks remain.')],
 'Induction and maintenance are different treatment roles',
 '**Steroids suppress activity quickly but are not a durable disease-maintenance solution.**',
 ['Repeated courses or inability to taper indicate inadequate control.', 'Budesonide also has a limited induction role rather than universal indefinite maintenance.'],
 '**Establish a steroid-sparing strategy.**',
 ['Select therapy according to disease phenotype and risk.', 'Monitor objective activity and treatment toxicity.'],
 [['Steroid induction','Short-term suppression'],['Steroid dependence','Signals a need for plan change'],['Maintenance','Appropriate steroid-sparing therapy']], [B,U,CD])
q('A hospitalized UC patient has frequent bloody stools, tachycardia and systemic toxicity. What is an appropriate initial ASUC bundle?',
 'IV corticosteroids, fluid/electrolyte care, infection assessment, early limited endoscopy and VTE prophylaxis when appropriate',[
 ('Oral mesalamine alone with no inpatient monitoring','The systemic severe presentation needs a different pathway.'),
 ('Routine full bowel preparation and maximal colonoscopy before stabilization','Limited endoscopic assessment is safer in severe colitis.'),
 ('Azathioprine alone as immediate rescue','Its onset is too slow for the acute emergency.')],
 'ASUC requires coordinated inpatient care',
 '**Assess severity, infection and complications while starting appropriate IV steroid treatment.**',
 ['Early flexible sigmoidoscopy and biopsies can assess activity and CMV.', 'Document stool frequency, bleeding, vital signs and serial CRP.'],
 '**Involve surgery early rather than only after collapse.**',
 ['A rescue or colectomy decision may be needed within days.', 'Correct nutrition and electrolytes without assuming bowel rest alone treats the disease.'],
 [['Initial ASUC','Monitored multidisciplinary bundle'],['Response assessment','Daily clinical and biochemical review'],['Failure/complication','Timely rescue or surgery']], [UC,B], 'clinical_scenario')
q('After three days of appropriate IV steroids for ASUC, a patient still has nine bloody stools daily and CRP 70 mg/L. There is no perforation or uncontrolled sepsis. What is the appropriate direction?',
 'Timely rescue therapy assessment, conventionally infliximab or IV cyclosporine, with surgical involvement',[
 ('Continue the same IV steroids for several more weeks before reviewing response','Delayed ineffective therapy can worsen outcomes.'),
 ('Start azathioprine alone and wait for its full effect','It is too slow for this rescue need.'),
 ('Discharge on antidiarrheals because stool frequency is the only issue','The persistent severe inflammatory pattern is unsafe for that plan.')],
 'Early steroid nonresponse is a decision point',
 '**Persistent high stool frequency and CRP by day three identify a high-risk course.**',
 ['Infliximab or cyclosporine are conventional rescue options in a suitable patient.', 'Newer rescue approaches require specialist selection and do not justify delaying a clear failure decision.'],
 '**Maintain a realistic surgical plan.**',
 ['Contraindications, prior exposure and clinical trajectory influence rescue choice.', 'Deterioration or a complication can move the decision directly to surgery.'],
 [['Day-three inadequate response','Rescue/surgical reassessment'],['Suitable medical rescue','Infliximab or cyclosporine pathway'],['Complication or failure','Do not delay necessary colectomy']], [UC,B], 'clinical_scenario')
q('An ASUC patient develops free intraperitoneal air, peritonitis and hemodynamic deterioration. What is the appropriate action?',
 'Emergency surgical management rather than another prolonged medical rescue trial',[
 ('Start a slow thiopurine induction and observe','Perforation is not a situation for delayed medical induction.'),
 ('Perform routine full colonoscopy with extensive insufflation','This is inappropriate in a perforated unstable colon.'),
 ('Use antidiarrheal therapy as definitive source control','It does not treat perforation and sepsis.')],
 'A structural complication supersedes the routine drug ladder',
 '**Perforation and peritonitis require emergency surgical source control.**',
 ['Resuscitation and antimicrobials proceed in parallel.', 'Severe bleeding and toxic deterioration can also create urgent surgical indications.'],
 '**Do not let repeated rescue attempts postpone a necessary operation.**',
 ['Early surgical involvement improves planning.', 'The exact operation depends on stability and disease context.'],
 [['Uncomplicated steroid failure','Selected rescue options'],['Perforation/peritonitis','Emergency surgery'],['Support','Resuscitation and sepsis care']], [UC,B], 'clinical_scenario')
q('A steroid-refractory UC flare has deep ulcers. Which test best assesses clinically relevant CMV colitis?',
 'Colonic ulcer biopsies with histology and appropriate CMV tissue testing',[
 ('CMV IgG alone as proof of active colitis','IgG commonly reflects prior exposure.'),
 ('A normal peripheral white count as exclusion','The blood count does not exclude tissue infection.'),
 ('An IBD diagnosis as proof CMV cannot coexist','Tissue infection can complicate severe or refractory disease.')],
 'Tissue disease needs tissue assessment',
 '**Severe refractory colitis warrants consideration of CMV.**',
 ['Histology and immunohistochemistry or appropriate tissue assays support interpretation.', 'Viral detection must be related to the clinical and histological disease burden.'],
 '**Coordinate infection and colitis treatment.**',
 ['Selected significant infection may need antiviral therapy.', 'Do not escalate immunosuppression blindly when an untreated tissue infection may be contributing.'],
 [['CMV IgG','Prior exposure marker'],['Ulcer biopsy','Assesses tissue involvement'],['Management','Integrated infection and IBD plan']], [UC,B], 'clinical_scenario')
q('Why is pharmacological VTE prophylaxis generally considered for a hospitalized active-IBD patient despite ordinary disease-related rectal bleeding?',
 'Active IBD and hospitalization increase thrombosis risk, and minor colitis bleeding is not automatically a contraindication',[
 ('IBD protects against venous thrombosis','Inflammation increases rather than eliminates risk.'),
 ('Any visible blood always prohibits every prophylactic dose','Bleeding severity and contraindications require individual assessment.'),
 ('Aspirin is an equivalent universal inpatient VTE strategy','It is not the usual prophylactic anticoagulation substitute in this setting.')],
 'Inflammation creates competing bleeding and clotting concerns',
 '**Assess VTE prevention actively during admission.**',
 ['Immobility and systemic inflammation increase risk.', 'Major active hemorrhage or another genuine contraindication changes the plan.'],
 '**Do not use a blanket rule based on one symptom.**',
 ['Consider severity, platelets, renal function and procedural context.', 'Use mechanical measures when appropriate and reassess as the condition changes.'],
 [['Active hospitalized IBD','Increased VTE risk'],['Ordinary colitis bleeding','Not an automatic exclusion'],['Major contraindication','Individualized prevention plan']], [B,UC])
q('A patient has mild-to-moderate active Crohn disease limited to the ileum and ascending colon. Which drug has a targeted induction role?',
 'Controlled ileal-release budesonide',[
 ('Rectal mesalamine suppository','This does not deliver treatment to the ileocecal region.'),
 ('Azathioprine as a rapid short-course induction agent','Its onset is too slow for that role.'),
 ('Budesonide indefinitely as mandatory maintenance','The induction indication does not establish long-term maintenance.')],
 'Delivery site determines the usefulness of a locally acting steroid',
 '**Ileal-release budesonide can induce remission in selected ileocecal Crohn.**',
 ['The conventional regimen is 9 mg daily for induction.', 'It is not sufficient for every location or severe high-risk disease.'],
 '**Plan maintenance and objective follow-up separately.**',
 ['Do not continue a steroid simply because it initially worked.', 'Persistent or higher-risk disease can require advanced treatment.'],
 [['Suitable ileocecal CD','Budesonide induction'],['Different location/severe burden','Choose another strategy'],['Long term','Steroid-sparing plan']], [CD,B], 'clinical_scenario')
q('Which statement reflects current management of active luminal Crohn disease?',
 'Oral mesalamine is not a reliable induction or maintenance treatment and should not delay effective therapy',[
 ('Its UC efficacy proves equal efficacy in every Crohn phenotype','The evidence differs between the diseases.'),
 ('Every patient must fail years of mesalamine before a biologic','That is not a modern risk-based requirement.'),
 ('A lack of mesalamine benefit means no medication can work','Other effective mechanisms are available.')],
 'Do not generalize a drug across IBD labels',
 '**5-ASA has an established role in selected UC but not comparable efficacy in active luminal Crohn.**',
 ['Disease location, complication risk and severity determine appropriate treatment.', 'Older low-efficacy habits can create therapeutic delay.'],
 '**Choose an effective steroid-sparing strategy.**',
 ['Assess inflammatory versus fixed structural symptoms.', 'Track objective response rather than relying on a prescription history.'],
 [['UC','Selected 5-ASA role'],['Luminal Crohn','Do not rely on mesalamine'],['Treatment selection','Phenotype and risk based']], [CD,B])
q('A Crohn patient has fever, pain and a 5-cm intra-abdominal abscess. What should generally precede escalation of immunosuppression?',
 'Antibiotics and drainage/source control when feasible',[
 ('Immediate high-dose immunosuppression without source assessment','An undrained abscess can worsen with immunosuppression.'),
 ('Observation alone regardless of sepsis','A sizable infected collection needs active management.'),
 ('Capsule endoscopy as the first drainage strategy','Capsule imaging does not drain an abscess and can be unsafe with associated obstruction.')],
 'Penetrating Crohn can create a septic rather than purely inflammatory problem',
 '**Drainage and antimicrobial treatment address the collection.**',
 ['Percutaneous or surgical control depends on anatomy and stability.', 'The underlying fistulizing disease still needs a subsequent treatment plan.'],
 '**Reassess after control before starting or intensifying advanced therapy.**',
 ['Review residual infection and structural disease.', 'Do not confuse persistent symptoms from an abscess with simple drug-refractory luminal inflammation.'],
 [['Abscess','Control infection and drain when appropriate'],['After source control','Plan Crohn therapy'],['Persistent structural complication','Surgical assessment may be needed']], [CD,B], 'clinical_scenario')
q('A patient has complex perianal Crohn fistulas with an abscess. Which sequence is appropriate?',
 'Define anatomy, drain the abscess and use a seton when indicated before or alongside an effective fistula-directed medical plan',[
 ('Close the external opening immediately without drainage','Trapping infection can worsen sepsis.'),
 ('Start a biologic while ignoring a known undrained collection','Source control is important before immunosuppressive escalation.'),
 ('Treat with mesalamine alone as the standard fistula-healing regimen','This is not an effective strategy for complex fistulizing disease.')],
 'Fistula care combines surgery and medicine',
 '**Pelvic MRI and examination under anesthesia can define the tract and sepsis.**',
 ['A seton maintains drainage in selected complex tracts.', 'Infliximab has important fistula-related evidence, with selection guided by the full context.'],
 '**Healing the skin opening is not the only target.**',
 ['Assess the internal tract and residual abscess.', 'Long-term coordination reduces recurrence and tissue injury.'],
 [['Anatomy','MRI/EUA assessment'],['Sepsis','Drain and maintain drainage'],['Ongoing disease','Effective combined treatment']], [CD,B], 'clinical_scenario')
q('A Crohn patient has recurrent obstruction from a short fixed fibrotic stricture with little active inflammation. Which management direction is appropriate?',
 'Assess endoscopic dilation or surgery according to anatomy and risk',[
 ('Escalate corticosteroids indefinitely to dissolve mature fibrosis','Medical anti-inflammatory treatment does not reliably reverse fixed fibrosis.'),
 ('Use a capsule without assessing retention risk','A known obstructing stricture creates retention concern.'),
 ('Assume every obstructive symptom proves an active inflammatory flare','The mechanism can be structural.')],
 'Separate inflammatory narrowing from fixed fibrostenosis',
 '**A predominantly fibrotic lesion may require mechanical treatment.**',
 ['Length, accessibility, associated fistula and cancer concern affect choice.', 'Active inflammation can coexist and needs its own treatment.'],
 '**Use imaging and endoscopic context before intervention.**',
 ['Exclude an abscess or a high-risk neoplastic stricture.', 'Plan recurrence prevention and nutritional care afterward.'],
 [['Inflammatory component','May respond to medical treatment'],['Fixed fibrosis','Dilation or surgery assessment'],['Complicated anatomy','Changes suitability']], [CD,B], 'clinical_scenario')

# Advanced therapies, prevention, surveillance and associated disease follow.
q('Which target distinguishes risankizumab from ustekinumab?',
 'Selective IL-23 p19 blockade',[
 ('Shared IL-12/23 p40 blockade','That is ustekinumab\'s target.'),
 ('Alpha4-beta7 integrin blockade','That is vedolizumab\'s target.'),
 ('TNF-alpha neutralization','That is the anti-TNF pathway rather than selective IL-23 p19 blockade.')],
 'Cytokine subunits distinguish related biological pathways',
 '**IL-23 contains p19, whereas p40 is shared with IL-12.**',
 ['Selective p19 agents differ mechanistically from ustekinumab.', 'Mechanism alone does not determine the best agent for every prior-exposure profile.'],
 '**Select therapy using disease and patient factors.**',
 ['Consider efficacy evidence, safety, extraintestinal disease and access.', 'Use the current indication-specific induction and maintenance regimen.'],
 [['Risankizumab','IL-23 p19'],['Ustekinumab','IL-12/23 p40'],['Vedolizumab','Alpha4-beta7']], [U,B])
q('How does vedolizumab reduce intestinal inflammation?',
 'It blocks alpha4-beta7-mediated lymphocyte trafficking to the gut',[
 ('It directly neutralizes TNF-alpha','That is a different biological class.'),
 ('It inhibits JAK1 intracellular signaling','That describes a small-molecule mechanism such as upadacitinib.'),
 ('It blocks the IL-12/23 p40 subunit','That is ustekinumab.')],
 'Trafficking blockade differs from cytokine neutralization',
 '**Vedolizumab targets a gut-homing integrin pathway.**',
 ['Its tissue-selective mechanism can affect the safety and extraintestinal treatment discussion.', 'It is not simply a corticosteroid or a systemic cytokine blocker.'],
 '**Match the mechanism to the full clinical problem.**',
 ['Speed, prior drug failure and extraintestinal manifestations matter.', 'Continue infection and vaccination assessment even for a gut-selective agent.'],
 [['Vedolizumab','Gut lymphocyte trafficking'],['Anti-TNF','Cytokine neutralization'],['JAK inhibitor','Intracellular signaling']], [U,B])
q('Which biological therapy targets the p40 subunit shared by IL-12 and IL-23?',
 'Ustekinumab',[
 ('Risankizumab','It selectively targets IL-23 p19.'),
 ('Vedolizumab','It targets alpha4-beta7 integrin.'),
 ('Infliximab','It targets TNF-alpha.')],
 'A shared subunit creates dual pathway inhibition',
 '**Ustekinumab blocks p40 and therefore affects IL-12 and IL-23 signaling.**',
 ['Selective IL-23 agents target a different subunit.', 'The drug\'s role depends on approved indication and treatment history.'],
 '**Do not infer interchangeability from a related cytokine family.**',
 ['Comparative evidence and prior exposure guide sequencing.', 'Monitor clinical and objective response after initiation.'],
 [['Ustekinumab','p40 shared by IL-12/23'],['P19 agent','Selective IL-23'],['Treatment decision','Evidence and context based']], [U,B])
q('An older smoker with IBD and previous VTE is considering advanced treatment. Which class requires particular discussion of thrombotic and major cardiovascular safety warnings?',
 'JAK inhibitors such as upadacitinib',[
 ('Rectal mesalamine as the class carrying the same systemic boxed warning','That is not the warning framework being tested.'),
 ('Pancreatic enzyme replacement','It is not a JAK-targeted IBD treatment.'),
 ('Oral rehydration solution','It does not carry this class-specific immune-drug warning.')],
 'Drug efficacy must be weighed against the patient\'s risk profile',
 '**FDA class warnings include serious cardiovascular events, malignancy, thrombosis and death.**',
 ['The evidence and magnitude vary with population and agent.', 'Age, smoking, prior thrombosis and cardiovascular risk inform selection.'],
 '**Use shared decisions and current agent-specific eligibility.**',
 ['Compare suitable alternatives rather than treating a warning as a claim that no patient can benefit.', 'Review infection risk, vaccination and laboratory monitoring.'],
 [['JAK pathway','Small-molecule signaling inhibition'],['Higher-risk history','Important benefit-risk discussion'],['Selection','Individualized contemporary guidance']], [ref('FDA: JAK Inhibitor Safety Communication','https://www.fda.gov/safety/medical-product-safety-information/janus-kinase-jak-inhibitors-drug-safety-communication-fda-requires-warnings-about-increased-risk'),U], 'clinical_scenario')
q('Why is cardiac conduction history relevant before starting ozanimod for UC?',
 'S1P receptor modulation can cause bradycardia or conduction effects, so baseline suitability assessment is needed',[
 ('It acts only within the bowel with no systemic signaling','S1P modulation has systemic physiological effects.'),
 ('It is a direct beta-agonist that guarantees tachycardia','That is not its mechanism.'),
 ('It permanently eliminates every AV block risk','Conduction precautions remain relevant.')],
 'Lymphocyte trafficking treatment can have off-target clinical consequences',
 '**S1P modulation changes lymphocyte egress and has important cardiac precautions.**',
 ['Review ECG, conduction disease and interacting rate-slowing drugs according to the label.', 'Other precautions include infection and selected ophthalmic or hepatic considerations.'],
 '**Apply the agent-specific initiation plan.**',
 ['Dose titration and contraindications are not identical for every S1P drug.', 'A mechanism label does not replace the current prescribing protocol.'],
 [['S1P modulation','Changes lymphocyte circulation'],['Cardiac review','Bradycardia and conduction suitability'],['Initiation','Agent-specific protocol']], [U,B])
q('Before azathioprine is prescribed, which inherited factors can identify patients at increased risk of severe thiopurine myelosuppression?',
 'TPMT and NUDT15 reduced-function status',[
 ('CYP2C19 only as the complete thiopurine safety test','That is not the principal thiopurine toxicity framework.'),
 ('HLA-DQ2 alone','That is a celiac susceptibility marker rather than a thiopurine metabolism test.'),
 ('Factor V Leiden alone','That assesses a thrombophilia, not thiopurine metabolite handling.')],
 'Thiopurine toxicity has important pharmacogenetic contributors',
 '**TPMT and NUDT15 affect the risk from active thiopurine exposure.**',
 ['Dose reduction or an alternative may be needed for reduced activity.', 'NUDT15 is especially relevant in several Asian and other populations.'],
 '**A favorable test does not remove monitoring.**',
 ['Regular CBC and liver tests remain necessary.', 'Pancreatitis, infection and other adverse effects are not excluded by normal genotype or enzyme activity.'],
 [['TPMT/NUDT15','Myelosuppression susceptibility'],['Dose selection','Adjust to activity and guidance'],['CBC/liver monitoring','Still required']], [B])
q('Why is azathioprine alone a poor choice for rapid induction in a severely active IBD flare?',
 'Its clinical onset is delayed, so it does not provide the required immediate anti-inflammatory control',[
 ('It reaches maximal clinical effect within minutes','The onset is much slower.'),
 ('It is an endoscopic mechanical hemostatic drug','That is unrelated to its immune action.'),
 ('A high loading dose safely eliminates all onset delay','Escalating exposure can increase toxicity without solving the acute treatment need.')],
 'A maintenance-capable drug need not be an induction drug',
 '**Thiopurines can have selected maintenance or combination roles but act slowly.**',
 ['An acute flare requires an appropriate induction strategy.', 'The long-term plan depends on disease, prior therapy and safety considerations.'],
 '**Avoid both therapeutic delay and unnecessary toxicity.**',
 ['Check metabolic safety before use.', 'Review whether a thiopurine is the best ongoing option in the patient\'s risk profile.'],
 [['Acute severe flare','Rapid effective induction/rescue'],['Thiopurine','Delayed-onset selected role'],['Loading escalation','Not a substitute for correct timing']], [B,U])
q('A patient is about to start anti-TNF therapy for Crohn disease. Which infection assessment is particularly important beforehand?',
 'Latent TB and hepatitis B assessment, with management of positive findings',[
 ('Only a routine urine dipstick as complete infection screening','That does not address major reactivation risks.'),
 ('Assume normal temperature excludes latent infection','Latent TB and HBV can be asymptomatic.'),
 ('Start therapy first and investigate only after severe infection develops','Preventive assessment is part of safe initiation.')],
 'Immune therapy can reactivate clinically silent infection',
 '**Anti-TNF treatment creates important TB and HBV reactivation concerns.**',
 ['Use history, appropriate tests and imaging according to the guideline and epidemiology.', 'HBV markers need interpretation for current infection, past exposure and immunity.'],
 '**Act on findings rather than merely documenting them.**',
 ['Prophylaxis, treatment or vaccination may be needed.', 'Urgent disease control requires coordinated specialist timing rather than ignoring either risk.'],
 [['TB','Latent/reactivation assessment'],['HBV','Serological status and prevention plan'],['Timing','Coordinate infection and IBD care']], [B], 'clinical_scenario')
q('Which vaccination principle applies before significant immunosuppression for IBD?',
 'Review and update vaccines early; live vaccines generally require appropriate timing before treatment and are avoided during significant immunosuppression',[
 ('All vaccines are live and therefore permanently prohibited','Many vaccines are nonlive and are important in these patients.'),
 ('Vaccination history matters only after an opportunistic infection occurs','Prevention should precede treatment when possible.'),
 ('A live vaccine can always be given on the same day as any biologic without review','Timing and immune status matter.')],
 'Prevention is most effective before immune suppression',
 '**Assess immunity and age-appropriate vaccination at diagnosis and before treatment.**',
 ['Nonlive vaccines can generally be used, though responses may be reduced.', 'Specific live-vaccine waiting periods depend on the drug and guideline.'],
 '**Include household and travel context where relevant.**',
 ['Do not delay every urgent IBD treatment solely to complete a routine schedule without specialist judgment.', 'Record the plan for vaccines that cannot be given immediately.'],
 [['Before treatment','Best opportunity to update immunity'],['Live vaccines','Timing restrictions'],['Nonlive vaccines','Generally usable with appropriate guidance']], [B])
q('After ileocolonic resection for Crohn disease, what monitoring is generally recommended even if symptoms improve?',
 'Postoperative ileocolonoscopy at about 6-12 months to assess recurrence',[
 ('No monitoring until severe obstructive symptoms recur','Endoscopic recurrence can precede symptoms.'),
 ('A normal early CRP as proof of permanent cure','Surgery does not eliminate all recurrence risk.'),
 ('A one-time stool occult-blood test as an equivalent recurrence assessment','It cannot grade mucosal postoperative disease.')],
 'Postoperative remission is not the same as cure',
 '**Mucosal recurrence can develop before the patient notices symptoms.**',
 ['Ileocolonoscopy allows a postoperative endoscopic score and treatment adjustment.', 'Smoking, penetrating disease and prior surgery can increase risk.'],
 '**Use risk-based preventive therapy and objective follow-up.**',
 ['Do not wait for a new structural complication before acting.', 'Biomarkers are useful complements rather than perfect replacements in every case.'],
 [['Clinical improvement','Does not exclude early recurrence'],['6-12 month scope','Objective postoperative assessment'],['Risk factors','Guide prevention intensity']], [CD,B], 'clinical_scenario')
q('Which lifestyle exposure worsens Crohn disease course and postoperative recurrence risk?',
 'Cigarette smoking',[
 ('Smoking is protective in every IBD subtype and should be prescribed','Any epidemiological UC association does not justify tobacco treatment.'),
 ('Smoking has no relevance after resection','Postoperative recurrence is an important concern.'),
 ('A normal CRP cancels all smoking-associated risk','A current marker does not remove the exposure risk.')],
 'Smoking cessation is disease-modifying care in Crohn',
 '**Smoking is associated with a worse Crohn trajectory.**',
 ['Cessation support should be active rather than a brief warning.', 'Medication and behavioral support can improve success.'],
 '**Do not turn a disease association into harmful advice for UC.**',
 ['Tobacco carries major cancer and cardiovascular harms.', 'Use safer evidence-based IBD treatment rather than recommending smoking.'],
 [['Crohn','Smoking worsens risk'],['After surgery','Recurrence concern persists'],['Care','Structured cessation support']], [CD,B])
q('A patient has extensive UC without PSC. When is the first risk-assessment surveillance colonoscopy generally considered for colitis-associated cancer prevention?',
 'About eight years after onset of colitis symptoms',[
 ('Only at age 75 regardless of disease duration','IBD surveillance differs from a simple age-only population pathway.'),
 ('Only after a cancer symptom appears','Surveillance aims to detect neoplasia before symptoms.'),
 ('Every week from diagnosis in all uncomplicated cases','That is not the routine schedule.')],
 'Duration and extent influence colitis-associated neoplasia risk',
 '**A baseline surveillance assessment around eight years is a conventional framework.**',
 ['PSC changes the start and frequency.', 'Isolated proctitis does not automatically follow the same extensive-colitis risk pathway.'],
 '**Individualize later intervals.**',
 ['Inflammation, dysplasia, strictures and family history affect risk.', 'High-quality examination and disease control are essential.'],
 [['Colonic IBD','Duration-based surveillance assessment'],['PSC','Earlier dedicated pathway'],['Intervals','Risk stratified']], [CA,B])
q('A patient with UC is newly diagnosed with PSC only two years after colitis onset. What cancer-surveillance principle applies?',
 'Begin the PSC-associated annual colonoscopic surveillance pathway without waiting eight years',[
 ('Wait until year eight because PSC does not change risk','PSC is an important high-risk modifier.'),
 ('Stop surveillance if colitis symptoms are mild','Symptom burden does not capture the full neoplasia risk.'),
 ('Use liver enzymes as a substitute for colon examination','They do not detect colonic dysplasia.')],
 'PSC changes the colorectal risk framework',
 '**PSC-associated colitis warrants surveillance from the time the association is recognized.**',
 ['Annual assessment is the conventional high-risk approach.', 'Risk can be important despite limited symptoms.'],
 '**Use high-quality dysplasia detection.**',
 ['Coordinate liver and bowel surveillance as separate needs.', 'Continue control of mucosal inflammation.'],
 [['Colitis without PSC','Usual duration/risk framework'],['PSC-associated colitis','Annual surveillance from diagnosis'],['Mild symptoms','Do not negate risk']], [CA], 'clinical_scenario')
q('A well-demarcated visible dysplastic lesion in colitic mucosa is completely endoscopically resectable, with no dysplasia elsewhere on a high-quality exam. What is an appropriate modern strategy?',
 'Expert endoscopic resection followed by close surveillance in a suitable patient',[
 ('Mandatory colectomy for every visible lesion regardless of resectability','Selected resectable lesions can be managed endoscopically.'),
 ('Ablate without obtaining a histological specimen','Resection and histological assessment are important.'),
 ('Ignore the lesion because inflammation explains every atypical cell','Confirmed dysplasia requires a deliberate plan.')],
 'Visibility and resectability guide dysplasia management',
 '**A discrete completely resectable lesion differs from unresectable or multifocal disease.**',
 ['Expert pathology confirmation and assessment for synchronous dysplasia matter.', 'Invasive features or poor resectability can favor surgery.'],
 '**Surveillance remains necessary after local treatment.**',
 ['The exact interval depends on lesion and patient risk.', 'Discuss colectomy when the broader neoplasia risk cannot be safely controlled endoscopically.'],
 [['Visible resectable lesion','Selected endoscopic approach'],['Unresectable/multifocal high-risk disease','Surgical discussion'],['After resection','Close expert surveillance']], [CA], 'clinical_scenario')
q('Which extraintestinal manifestation often parallels intestinal inflammatory activity?',
 'Erythema nodosum',[
 ('Ankylosing spondylitis as an obligatorily parallel manifestation','Axial disease often runs independently of bowel activity.'),
 ('PSC as a condition that reliably resolves with every colitis remission','PSC commonly has an independent course.'),
 ('A fixed cataract as an inflammatory activity biomarker','That is not a direct parallel activity marker.')],
 'Some extraintestinal disease tracks bowel inflammation',
 '**Erythema nodosum often improves when intestinal activity is controlled.**',
 ['Certain peripheral arthritis patterns can also parallel activity.', 'Not every extraintestinal manifestation follows this relationship.'],
 '**Treat the manifestation and the underlying disease.**',
 ['Exclude infection and other causes of tender nodules when appropriate.', 'Persistent or severe manifestations can need specialty care.'],
 [['Often parallel','Erythema nodosum'],['Often independent','Axial spondyloarthritis, PSC'],['Treatment','Organ-specific and bowel-directed assessment']], [B])
q('An IBD patient has inflammatory back pain and sacroiliitis despite sustained bowel remission. Which interpretation is correct?',
 'Axial spondyloarthritis can follow a course independent of intestinal activity',[
 ('Bowel remission excludes inflammatory axial disease','The courses can be discordant.'),
 ('All back pain must be caused by active colitis','Mechanical and other causes also need assessment.'),
 ('A gut-selective drug is guaranteed to control every axial manifestation','Mechanism and organ-specific evidence affect selection.')],
 'A quiet bowel does not guarantee a quiet joint',
 '**Axial inflammation can persist independently.**',
 ['Coordinate rheumatological and IBD assessment.', 'Drug choice may need to cover both compartments.'],
 '**Avoid treating only the bowel biomarker.**',
 ['Assess symptoms, function and appropriate imaging.', 'NSAID use requires a balanced individualized discussion rather than an automatic unmonitored course.'],
 [['Intestinal activity','May be in remission'],['Axial activity','Can remain active'],['Therapy','Choose with both organs in mind']], [B], 'clinical_scenario')
q('After an ileal pouch-anal anastomosis for UC, a patient develops increased stool frequency, urgency and endoscopic pouch inflammation. Which is a usual initial treatment for an uncomplicated first episode of pouchitis?',
 'A short appropriate antibiotic course such as ciprofloxacin or metronidazole',[
 ('Immediate permanent pouch removal in every first episode','Many initial episodes respond to medical treatment.'),
 ('Mesalamine suppositories as an equivalent treatment for every pouch syndrome','Cuffitis and pouchitis are different compartments and need assessment.'),
 ('Ignore the endoscopic inflammation because high stool frequency is always normal','A change from baseline with inflammation warrants treatment.')],
 'A pouch has its own inflammatory differential',
 '**Intermittent pouchitis commonly responds to antibiotics.**',
 ['Assess infection, cuffitis, mechanical problems and Crohn-like pouch disease when features are atypical.', 'Chronic antibiotic-dependent or refractory disease has a different pathway.'],
 '**Do not assume colectomy eliminates all future inflammatory care.**',
 ['Reassess symptoms and objective findings.', 'Advanced therapy can be needed in selected chronic cases.'],
 [['Initial uncomplicated pouchitis','Antibiotic course'],['Cuffitis','Rectal cuff-focused disease'],['Chronic refractory pattern','Specialist escalation']], [ref('AGA 2024 Pouchitis and Inflammatory Pouch Disorders Guideline','https://pmc.ncbi.nlm.nih.gov/articles/PMC11163976/')], 'clinical_scenario')
q('A woman with IBD is planning pregnancy. Which medication specifically requires preconception discontinuation because of teratogenic risk?',
 'Methotrexate',[
 ('Mesalamine as a universal teratogen requiring withdrawal in every patient','It is commonly continued when appropriate; formulation and individual factors are reviewed.'),
 ('Every anti-TNF regardless of relapse risk','Effective biological therapy can often be continued under a pregnancy plan.'),
 ('All maintenance treatment without distinction','Active disease itself can harm pregnancy outcomes.')],
 'Pregnancy planning requires medication-specific decisions',
 '**Methotrexate is contraindicated in pregnancy and requires a planned washout before conception.**',
 ['Use current drug and guideline advice for the interval.', 'Other small molecules also have important pregnancy restrictions.'],
 '**Preserve remission with suitable treatment.**',
 ['Do not stop effective maintenance indiscriminately.', 'Coordinate gastroenterology, obstetric and medication counseling before conception when possible.'],
 [['Methotrexate','Stop before pregnancy under a planned protocol'],['Appropriate maintenance','Can protect remission'],['Active disease','Important maternal and fetal risk']], [B], 'clinical_scenario')

if __name__=='__main__':
    finalize('GI & pancreas',4,'Inflammatory Bowel Disease','gi-ibd',rows,36)
