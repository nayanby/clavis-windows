"""Lipid pharmacology decisions for the source-matched Chapter 15."""
from qbank_json_chapters import question
REFERENCES={
 'statin':('ACC/AHA Dyslipidemia Guideline, 2026','https://doi.org/10.1016/j.jacc.2025.11.016'),
 'ezet':('Ezetimibe US prescribing information','https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021445s043lbl.pdf'),
 'incl':('Inclisiran US prescribing information, 2026','https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/214012s021lbl.pdf'),
 'clear':('CLEAR Outcomes randomized trial: ACC report','https://www.acc.org/Latest-in-Cardiology/Clinical-Trials/2023/03/01/23/31/clear-outcomes'),
 'bemp':('Bempedoic acid US prescribing information','https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/211616s022s023lbl.pdf'),
 'reduce':('REDUCE-IT randomized trial','https://doi.org/10.1056/NEJMoa1812792'),
 'feno':('Fenofibrate 48/145-mg tablet prescribing information','https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=085109a6-f006-44f0-a170-980d8899a365'),
 'evin':('Evinacumab US prescribing information','https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/761181s002lbl.pdf')}
rows=[]
def B(t,*c):return(t,list(c))
def Q(title,stem,answer,others,sections,refs,table=None,style='clinical_scenario'):
 r=question('Lipid-lowering pharmacology',title,stem,answer,others,sections,refs,table=table,style=style)
 r['explanationStyle']='concise_structured';rows.append(r)

Q('Statin Intensity','Which regimen is classified as high-intensity statin monotherapy, with an expected LDL-C reduction of at least 50%?',
 'Rosuvastatin 20 mg daily',[
 ('Atorvastatin 20 mg daily','This is moderate-intensity treatment, usually lowering LDL-C by 30–49%; atorvastatin 40–80 mg is the high-intensity range.'),
 ('Simvastatin 40 mg daily','This is moderate-intensity therapy; escalation to simvastatin 80 mg is not a preferred way to initiate high-intensity treatment because of myopathy risk.'),
 ('Pravastatin 80 mg daily','Even at this dose pravastatin is classified as moderate intensity; milligram doses cannot be compared directly across statins.')],
 [('Dose-Specific Classification',[B('**Intensity describes expected population-average LDL reduction.**','Assess the achieved response and adherence rather than assuming every patient has the same percentage fall.')]),
 ('Clinical Use',[B('**Choose the maximally tolerated regimen for the patient’s risk and interactions.**','A lower statin dose plus a nonstatin may achieve substantial lowering, but that does not relabel the statin dose itself as high intensity.')])],['statin'],
 table=(['Intensity','Expected reduction','Examples'],[['High','≥50%','Atorvastatin 40–80 mg; rosuvastatin 20–40 mg'],['Moderate','30–49%','Atorvastatin 10–20 mg; rosuvastatin 5–10 mg'],['Low','<30%','Simvastatin 10 mg; pravastatin 10–20 mg']]),style='direct')

Q('Ezetimibe Target','Which molecular target accounts for ezetimibe’s reduction of intestinal cholesterol absorption?',
 'NPC1L1',[
 ('HMG-CoA reductase','Statins inhibit hepatic cholesterol synthesis through this enzyme; ezetimibe instead acts at the intestinal absorption pathway.'),
 ('ATP citrate lyase','Bempedoic acid inhibits this upstream hepatic synthetic enzyme; it does not describe ezetimibe’s intestinal action.'),
 ('PCSK9','PCSK9-directed therapies preserve LDL receptor availability; this differs from blocking cholesterol entry through NPC1L1.')],
 [('Mechanism',[B('**NPC1L1 inhibition reduces uptake of dietary and biliary cholesterol.**','Reduced hepatic cholesterol delivery promotes LDL clearance and complements statin-mediated synthesis inhibition.')]),
 ('Prescribing',[B('**Standard adult dose: 10 mg once daily**, with or without food.'),B('**Use with appropriate background lipid therapy and reassess response.**','Review muscle/liver symptoms and interacting treatments; separate from bile acid sequestrants by the label-recommended interval.')])],['ezet'],style='direct')

Q('Inclisiran Dosing and Mechanism','An adult selected for inclisiran receives the first 284-mg subcutaneous dose. Which schedule correctly completes the labeled loading and maintenance plan?',
 'Repeat at 3 months, then every 6 months',[
 ('Repeat after 2 weeks, then every 2 weeks','Frequent injections are used for some PCSK9 monoclonal antibody regimens, not inclisiran’s prolonged hepatic RNA-interference schedule.'),
 ('Repeat after 1 month, then monthly','Monthly dosing fits selected other injectable lipid therapies; inclisiran requires a three-month second dose followed by six-month intervals.'),
 ('Repeat after 6 months, then annually','This omits the scheduled three-month dose and uses an unvalidated prolonged maintenance interval rather than the labeled regimen.')],
 [('RNA Interference',[B('**Inclisiran suppresses hepatic PCSK9 production.**','It is an siRNA therapy, whereas evolocumab and alirocumab bind circulating PCSK9 as antibodies.')]),
 ('Outcome Interpretation',[B('**LDL lowering and event reduction are different endpoints.**','The 2026 dyslipidemia guideline describes cardiovascular outcome trials as pending; do not automatically transfer antibody trial results to inclisiran.'),B('**Monitor LDL response and injection tolerance**, and maintain the scheduled follow-up.')])],['incl','statin'])

Q('CLEAR Outcomes','Which conclusion is supported by CLEAR Outcomes in patients unable or unwilling to take statins because of adverse effects?',
 'Bempedoic acid reduced a composite of major cardiovascular events',[
 ('Bempedoic acid established a significant all-cause mortality reduction','The significant primary composite benefit should not be converted into a claim of demonstrated all-cause survival benefit.'),
 ('Bempedoic acid proved superior to high-intensity statins','The randomized comparator was placebo; the trial did not establish superiority to an adequately tolerated high-intensity statin regimen.'),
 ('Bempedoic acid lowered LDL but did not improve the primary clinical endpoint','The primary four-component event endpoint was significantly reduced; this statement incorrectly dismisses the demonstrated clinical benefit.')],
 [('Population and Result',[B('**Statin-intolerant patients at elevated cardiovascular risk** received bempedoic acid or placebo.','The primary composite occurred in 11.7% versus 13.3%; interpret the result in the studied population.')]),
 ('Clinical Translation',[B('**ATP citrate lyase inhibition offers an oral LDL-lowering option.**','Use 180 mg daily when selected; reassess LDL response and other tolerated therapies.'),B('**Review gout, uric acid, tendon symptoms and interactions.**','A favorable composite endpoint does not mean every individual component or subgroup showed a separate significant benefit.')])],['clear','bemp'],style='direct')

Q('Bempedoic Acid–Statin Interaction','Bempedoic acid is being added to tolerated simvastatin therapy. Under US labeling, which simvastatin dose ceiling addresses the interaction?',
 'Avoid simvastatin doses above 20 mg/day',[
 ('Avoid simvastatin doses above 10 mg/day','Some other interacting drugs impose a 10-mg simvastatin ceiling; this is not the bempedoic acid label threshold.'),
 ('Avoid simvastatin doses above 40 mg/day','The 40-mg limit applies to pravastatin with bempedoic acid; the simvastatin threshold is lower.'),
 ('Retain any previously tolerated simvastatin dose','Prior tolerance does not remove the exposure increase introduced by a new interacting drug; the regimen needs review.')],
 [('Exposure and Myopathy',[B('**Bempedoic acid increases exposure to selected statins.**','Avoid simvastatin >20 mg/day and pravastatin >40 mg/day; adjust the combination or choose another LDL-lowering approach.')]),
 ('Monitoring',[B('**Ask about muscle pain, weakness and dark urine**, with CK testing when clinically indicated.'),B('**Bempedoic acid also raises uric acid and can cause tendon injury.**','Its hepatic activation does not eliminate adverse effects or interactions; evaluate the complete medication list.')])],['bemp'])

Q('REDUCE-IT and Formulation-Specific Evidence','A statin-treated patient with established ASCVD and triglycerides 220 mg/dL asks whether any fish-oil supplement reproduces REDUCE-IT. Which response best reflects the trial?',
 'Benefit was demonstrated with prescription icosapent ethyl 2 g twice daily',[
 ('Equivalent triglyceride lowering proves equivalent cardiovascular benefit','A surrogate change does not establish matching clinical outcomes across different formulations or mechanisms.'),
 ('The trial tested an over-the-counter mixed EPA/DHA preparation','REDUCE-IT used a defined prescription purified EPA formulation; variable supplement content cannot be treated as the tested intervention.'),
 ('The trial enrolled only patients with triglycerides above 1,000 mg/dL','The study addressed residual cardiovascular risk with moderate triglyceride elevation in statin-treated high-risk patients, not exclusively severe chylomicronemia.')],
 [('Evidence',[B('**REDUCE-IT tested 4 g/day of icosapent ethyl.**','The primary event rate was 17.2% versus 22.0% over median 4.9 years; eligibility and background statin treatment matter.')]),
 ('Risk–Benefit Discussion',[B('**Review AF and bleeding risks**, particularly with concomitant antithrombotics.'),B('**Do not substitute a generic fish-oil claim for trial evidence.**','Treat secondary causes of triglyceride elevation and continue indicated LDL-lowering therapy.')])],['reduce'])

Q('Fenofibrate in Moderate Renal Impairment','A patient with persistent severe hypertriglyceridemia and eGFR 42 mL/min/1.73 m² is selected for a US fenofibrate tablet product available as 48 and 145 mg. Which starting regimen follows that product’s labeling?',
 '48 mg once daily, with renal and triglyceride reassessment',[
 ('145 mg once daily without a renal adjustment','This is a full-strength regimen; the specified product starts at 48 mg in eGFR 30 to <60 and increases only after reassessment.'),
 ('145 mg twice daily with the two main meals','Doubling the full tablet dose is not a labeled renal-adjustment strategy and increases toxicity risk.'),
 ('Avoid any fenofibrate solely because eGFR is below 60','Severe renal impairment precludes treatment, but this moderate range permits a reduced product-specific starting dose with monitoring.')],
 [('Formulation Matters',[B('**Fenofibrate products are not all dose-interchangeable.**','For this 48/145-mg product, eGFR 30 to <60 requires a 48-mg start; eGFR <30 is contraindicated.')]),
 ('Safety',[B('**Monitor renal function, liver injury and muscle symptoms.**','Statin coadministration, renal impairment and hypothyroidism increase myopathy risk.'),B('**Treat secondary causes and diet alongside medication.**','Triglyceride lowering is not by itself proof of reduced ASCVD events or a measured pancreatitis-outcome benefit.')])],['feno'])

Q('Evinacumab in Homozygous FH','Which injectable therapy targets ANGPTL3 and can lower LDL-C independently of residual LDL-receptor function in homozygous familial hypercholesterolemia?',
 'Evinacumab',[
 ('Evolocumab','This antibody targets PCSK9; its LDL-lowering effect depends on increasing functioning LDL receptors, limiting response in receptor-null disease.'),
 ('Inclisiran','This siRNA reduces hepatic PCSK9 production; it is not ANGPTL3 inhibition and likewise acts through the LDL-receptor pathway.'),
 ('Alirocumab','This is another PCSK9 antibody, not the receptor-independent ANGPTL3-directed treatment asked about.')],
 [('Distinct Target',[B('**ANGPTL3 inhibition alters lipoprotein metabolism beyond PCSK9.**','This provides a specialist option in HoFH, including patients with very limited LDL-receptor activity.')]),
 ('Administration and Limits',[B('**15 mg/kg IV over 60 minutes every 4 weeks** is the labeled regimen.'),B('**Use as an adjunct to the overall HoFH treatment plan.**','Monitor infusion/hypersensitivity reactions and pregnancy-related precautions; LDL reduction should not be misrepresented as a dedicated cardiovascular mortality trial result.')])],['evin'],style='direct')
