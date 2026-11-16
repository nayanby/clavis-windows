"""New source-gap decisions; retained questions are not duplicated here."""
from qbank_json_chapters import question
REFERENCES={
 'cang':('Cangrelor US prescribing information','https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/204958Orig1s003lbl.pdf'),
 'cpic':('CPIC CYP2C19–clopidogrel guideline, 2022','https://pmc.ncbi.nlm.nih.gov/articles/PMC9287492/'),
 'tiro':('Tirofiban prescribing information','https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=d554acff-22e9-4f28-b826-ee1b91daa2df'),
 'hit':('ASH HIT guideline, 2018','https://pmc.ncbi.nlm.nih.gov/articles/6258919/'),
 'hitguide':('ASH HIT pocket guide','https://www.hematology.org/-/media/hematology/files/education/clinicians/guidelines-quality/documents/ash_vte_hit_pocketguide.pdf'),
 'fonda':('Fondaparinux US prescribing information','https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021345s052lbl.pdf'),
 'api':('Apixaban US prescribing information, 2026','https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/202155s042lbl.pdf'),
 'bleed':('ACC Anticoagulant Bleeding Pathway, 2020','https://doi.org/10.1016/j.jacc.2020.04.053'),
 'dabi':('Idarucizumab prescribing information','https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=c7400f8a-dcf4-a6df-6d07-983081b1bf34'),
 'lmwh':('Enoxaparin prescribing information: reversal','https://www.accessdata.fda.gov/drugsatfda_docs/label/2018/020164s116lbl.pdf'),
 'tests':('ADLM guidance on DOAC testing','https://doi.org/10.1093/jalm/jfaf155'),
 'andex':('FDA safety communication on Andexxa, December 2025','https://www.fda.gov/vaccines-blood-biologics/safety-availability-biologics/update-safety-andexxa')}
rows=[]
def B(t,*c):return(t,list(c))
def Q(title,stem,answer,others,sections,refs,table=None,flow=None):
 r=question('Antithrombotic pharmacology',title,stem,answer,others,sections,refs,table=table)
 r['explanationStyle']='concise_structured'
 if flow:r['flow']=flow
 rows.append(r)

Q('Transition From Intravenous Cangrelor','Cangrelor is being used during PCI. Oral absorption is now reliable, and clopidogrel has been selected for maintenance. Under US labeling, which transition best avoids a gap in P2Y12 inhibition?',
 'Clopidogrel 600 mg immediately after stopping cangrelor',[
 ('Clopidogrel 600 mg one hour before stopping cangrelor','Loading during the infusion can blunt the short-lived active metabolite’s receptor binding; this timing is suitable for ticagrelor, not clopidogrel.'),
 ('Clopidogrel 75 mg immediately after stopping cangrelor','This is the maintenance dose; without the recommended load, onset is too slow for a reliable immediate transition.'),
 ('Clopidogrel 600 mg six hours after stopping cangrelor','The dose is appropriate, but delaying it leaves a vulnerable interval because cangrelor inhibition resolves rapidly.')],
 [('Receptor Competition',[B('**Cangrelor reversibly occupies P2Y12.**','Clopidogrel’s active metabolite is short-lived; administer its load after the infusion ends.')]),
 ('Transition Regimens',[B('**Use the selected oral agent’s specific timing**, then its maintenance regimen.','Confirm absorption and bleeding risk; rapid IV offset makes an unnecessary delay hazardous.')])],['cang'],
 table=(['Agent','Loading dose','Timing'],[['Clopidogrel','600 mg','Immediately after stopping'],['Prasugrel','60 mg','Immediately after stopping'],['Ticagrelor','180 mg','During infusion or immediately after']] ))

Q('CYP2C19 and Clopidogrel Activation','After ACS PCI, a patient taking clopidogrel is found to have CYP2C19 *2/*2. There is no contraindication to a more potent oral P2Y12 inhibitor. Which strategy best follows CPIC guidance?',
 'Use ticagrelor or prasugrel at the appropriate standard regimen',[
 ('Continue clopidogrel 75 mg because platelet lifespan determines efficacy','Irreversible inhibition lasts for the affected platelet’s lifespan, but inadequate prodrug activation leaves more platelets uninhibited in a poor metabolizer.'),
 ('Increase clopidogrel to 150 mg as the preferred genotype-based regimen','Dose escalation is not the preferred CPIC approach for poor metabolizers; alternative agents avoid unreliable CYP2C19-dependent activation.'),
 ('Replace the P2Y12 inhibitor with a higher aspirin maintenance dose','Aspirin targets COX-1 rather than ADP signaling; increasing it does not substitute for effective P2Y12 inhibition after stenting.')],
 [('Phenotype and Consequence',[B('**Two no-function alleles indicate poor metabolism.**','Reduced active metabolite formation increases residual platelet reactivity and post-PCI ischemic risk.')]),
 ('Apply the Result',[B('**Select an alternative after contraindication screening.**','Prasugrel is contraindicated after stroke/TIA; ticagrelor has interaction, bleeding and tolerability considerations.'),B('**Interpret a known genotype separately from a policy of universal testing.**','Genotype does not measure adherence, absorption or every cause of treatment failure.')])],['cpic'])

Q('Renal Adjustment of Tirofiban','Tirofiban is selected for a thrombotic complication during PCI. Cockcroft–Gault CrCl is 45 mL/min. Which labeled regimen is appropriate?',
 '25 micrograms/kg bolus, then 0.075 micrograms/kg/min',[
 ('25 micrograms/kg bolus, then 0.15 micrograms/kg/min','The usual infusion is for CrCl above 60 mL/min; impaired clearance here requires halving the maintenance rate.'),
 ('12.5 micrograms/kg bolus, then 0.15 micrograms/kg/min','Renal adjustment changes the infusion, not by halving the bolus while leaving maintenance exposure unadjusted.'),
 ('12.5 micrograms/kg bolus, then 0.075 micrograms/kg/min','The infusion is appropriately reduced, but the labeled 25-microgram/kg loading dose remains unchanged.')],
 [('Dose and Target',[B('**GP IIb/IIIa blockade inhibits fibrinogen-mediated aggregation.**','Give the 25-microgram/kg bolus over 3 minutes; reduce infusion by half when CrCl is ≤60 mL/min.')]),
 ('Safety',[B('**Check platelets, hemoglobin, renal function and bleeding.**','Acute profound thrombocytopenia can occur; renal deterioration increases exposure.'),B('**Use selectively in PCI complications.**','This regimen does not imply routine upstream administration to every ACS patient.')])],['tiro'])

Q('High-Probability HIT With Thrombosis','On day 7 of UFH, platelets fall from 240 to 85 ×10⁹/L and a new proximal DVT is confirmed. There is no convincing alternative cause or active bleeding. What is the best immediate strategy while HIT testing is arranged?',
 'Stop all heparin and start therapeutic nonheparin anticoagulation',[
 ('Switch UFH to therapeutic enoxaparin while awaiting testing','LMWH can cross-react with HIT antibodies; it is not a safe substitute when immune HIT is strongly suspected.'),
 ('Stop UFH and wait for the functional assay before anticoagulating','A high-probability presentation with new thrombosis has substantial immediate risk; delaying alternative anticoagulation leaves thrombin generation untreated.'),
 ('Stop UFH and begin warfarin alone at the usual starting dose','Early protein C depletion can worsen HIT-associated thrombosis; warfarin is deferred until platelet recovery and requires an appropriate transition.')],
 [('Probability',[B('**The 4Ts assess fall, timing, thrombosis and other causes.**','This >50% fall with typical timing and new thrombosis strongly supports immediate action.')]),
 ('Management Sequence',[B('**Remove heparin sources, including flushes**, send an immunoassay and obtain functional confirmation when indicated.'),B('**Choose the alternative by organ function and clinical stability.**','Argatroban or bivalirudin suits many unstable/procedural settings; selected stable patients may receive fondaparinux or a DOAC.')])],['hit'],flow=['High clinical probability','Stop heparin + nonheparin treatment','Immunoassay ± functional confirmation','Reassess with results'])

Q('Warfarin During Acute HIT','A patient with confirmed HIT and thrombosis is receiving argatroban. Platelets remain 62 ×10⁹/L. Long-term warfarin is being considered because of a separate indication. What is the safest transition principle?',
 'Defer warfarin until platelet recovery and overlap with nonheparin therapy',[
 ('Start warfarin now and stop argatroban at the first INR above 2','Platelet recovery is required before starting warfarin; argatroban also elevates INR, so the first combined INR does not prove adequate warfarin effect.'),
 ('Start warfarin now and continue argatroban for 24 hours','Brief overlap neither addresses acute HIT-related protein C depletion nor allows sufficient reduction in long-lived coagulation factors.'),
 ('Replace argatroban with LMWH for five days before warfarin','Heparin products remain inappropriate in acute HIT; the bridging anticoagulant must be nonheparin.')],
 [('Why Delay',[B('**Early protein C depletion may aggravate thrombosis.**','Wait for recovery, usually ≥150 ×10⁹/L, before warfarin initiation.')]),
 ('Transition Safely',[B('**Overlap for ≥5 days and until the intended INR is achieved.**','Argatroban raises INR; use a validated transition protocol with reassessment after its effect clears.'),B('**Do not confuse stopping heparin with stopping anticoagulation.**','HIT is prothrombotic even while platelets are low.')])],['hitguide'])

Q('Fondaparinux Dose for Acute VTE','A 72-kg adult with acute proximal DVT and CrCl 64 mL/min is selected for fondaparinux. Which initial treatment dose is appropriate?',
 '7.5 mg subcutaneously once daily',[
 ('2.5 mg subcutaneously once daily','This is a prophylactic regimen and is also used in selected ACS settings; it is inadequate for acute DVT treatment at this weight.'),
 ('5 mg subcutaneously once daily','The 5-mg treatment dose applies below 50 kg; this patient belongs to the intermediate weight tier.'),
 ('10 mg subcutaneously once daily','The 10-mg treatment tier is for patients above 100 kg; it would increase exposure unnecessarily here.')],
 [('Weight-Based Treatment',[B('**Fondaparinux activates antithrombin-mediated Xa inhibition.**','It does not directly inhibit thrombin; dosing differs between prophylaxis and established VTE.')]),
 ('Renal and Procedural Limits',[B('**US VTE labeling contraindicates CrCl <30 mL/min.**','Assess bleeding, renal function and procedural plans; protamine does not provide specific reversal.')])],['fonda'],table=(['Weight','Daily treatment dose'],[['<50 kg','5 mg'],['50–100 kg','7.5 mg'],['>100 kg','10 mg']]))

Q('Apixaban: VTE Versus AF Dose Reduction','An 82-year-old, 58-kg patient with CrCl 52 mL/min has a new proximal DVT. There is no active bleeding or interacting drug, and apixaban is selected. Which US-labeled acute VTE regimen applies?',
 '10 mg twice daily for 7 days, then 5 mg twice daily',[
 ('2.5 mg twice daily from the first dose','Age and weight meet AF dose-reduction criteria, but those criteria are not the acute VTE regimen; 2.5 mg is also an extended-prevention dose after initial treatment.'),
 ('5 mg twice daily from the first dose','This is the continuing VTE dose after the initial seven-day higher-intensity phase, not the labeled complete initial regimen.'),
 ('10 mg twice daily for 21 days, then 5 mg twice daily','The apixaban initial phase lasts seven days; the 21-day lead-in belongs to rivaroxaban at a different dose.')],
 [('Indication Determines Regimen',[B('**Do not transfer AF reduction criteria to acute DVT/PE.**','Appropriate initial intensity is essential despite age and low body weight when treatment is selected.')]),
 ('Follow-up',[B('**Reassess bleeding, kidney function and interacting medicines.**','After at least six months, selected patients continuing secondary prevention use 2.5 mg twice daily; duration depends on recurrence and bleeding risks.')])],['api'])

Q('Urgent Reversal of Warfarin','A patient taking warfarin for AF develops an intracerebral hemorrhage with INR 5.8. Resuscitation and specialist care are underway. What is the preferred rapid reversal strategy when available?',
 'Four-factor PCC plus intravenous vitamin K',[
 ('Intravenous vitamin K alone','Vitamin K restores synthesis over hours; it does not supply the immediate clotting-factor replacement needed for critical-site hemorrhage.'),
 ('Fresh frozen plasma plus oral vitamin K as first choice','Plasma is an alternative when PCC is unavailable, but requires more volume and preparation; oral vitamin K is slower than the urgent IV strategy.'),
 ('Four-factor PCC alone without vitamin K','PCC provides immediate factors, but without sustained restoration of synthesis anticoagulation can recur as the infused factors disappear.')],
 [('Rapid and Sustained Reversal',[B('**PCC replaces factors; vitamin K restores synthesis.**','Use protocol-based 4F-PCC dosing by INR and weight, with IV vitamin K, commonly 10 mg for life-threatening VKA bleeding.')]),
 ('Reassessment',[B('**Stop warfarin, control the bleeding source and repeat INR.**','Monitor neurological course and thrombotic complications; later anticoagulation resumption requires individualized risk assessment.')])],['bleed'])

Q('Specific Reversal of Dabigatran','A patient took dabigatran two hours ago and now has uncontrolled life-threatening GI bleeding. A specific reversal agent is available. Which treatment directly neutralizes dabigatran?',
 'Idarucizumab 5 g intravenously',[
 ('Four-factor PCC as the specific binding antidote','PCC supplies coagulation factors and may be used when specific reversal is unavailable, but it does not bind dabigatran directly.'),
 ('Protamine sulfate by recent anticoagulant dose','Protamine reverses UFH and partly reverses LMWH; it does not neutralize the direct thrombin inhibitor dabigatran.'),
 ('Intravenous vitamin K 10 mg','Vitamin K reverses impaired factor synthesis from VKAs; dabigatran directly inhibits thrombin without depleting vitamin K-dependent factors.')],
 [('Antibody Fragment',[B('**Idarucizumab binds dabigatran and its active metabolites.**','The 5-g total is administered as two consecutive 2.5-g IV doses.')]),
 ('After Reversal',[B('**Continue resuscitation and definitive hemostasis.**','Monitor for recurrent bleeding or anticoagulant activity, particularly with renal impairment and redistribution.'),B('**Reassess thrombosis prevention once safe.**','Reversal removes anticoagulant protection but does not correct the underlying thromboembolic indication.')])],['dabi'])

Q('Partial Reversal of Enoxaparin','An adult develops major bleeding four hours after therapeutic enoxaparin. Protamine is being administered under a monitored reversal protocol. Which statement is most accurate?',
 'Protamine only partly neutralizes enoxaparin anti-Xa activity',[
 ('Protamine completely neutralizes enoxaparin at the UFH-equivalent dose','UFH is more fully reversed; residual LMWH anti-Xa activity can persist despite appropriate protamine dosing.'),
 ('Protamine has no anticoagulant reversal effect on enoxaparin','It provides useful partial reversal, including greater neutralization of anti-IIa activity; lack of complete anti-Xa reversal does not mean no effect.'),
 ('A normal aPTT proves complete enoxaparin reversal','aPTT is insufficiently sensitive to therapeutic LMWH activity and cannot establish complete neutralization.')],
 [('Time-Dependent Dosing',[B('**Recent exposure within 8 hours:** labeling uses 1 mg protamine per 1 mg enoxaparin.','Later exposure or repeat treatment uses different dosing; follow monitored protocol and account for renal clearance.')]),
 ('Clinical Limitations',[B('**Maximum anti-Xa neutralization is approximately 60%.**','Control the source, support circulation and reassess bleeding; excess protamine itself can impair coagulation and cause severe reactions.')])],['lmwh'])

Q('Coagulation Tests During Apixaban Exposure','A patient taking apixaban needs urgent surgery. The last-dose time is uncertain, and PT/INR and aPTT are normal. Which interpretation is best?',
 'Relevant apixaban activity may persist; use a calibrated anti-Xa assay if timely',[
 ('Normal INR establishes that the apixaban effect has cleared','INR is standardized for VKAs, not apixaban; poor reagent sensitivity can produce a normal result despite clinically relevant exposure.'),
 ('Normal aPTT alone excludes residual factor Xa inhibition','aPTT is not sufficiently sensitive to apixaban to exclude its effect; normal routine tests cannot establish drug clearance.'),
 ('A thrombin time is the preferred quantitative apixaban test','Thrombin-based assays are useful for dabigatran assessment; apixaban requires a suitable anti-Xa method rather than thrombin time quantification.')],
 [('Test Selection',[B('**Drug-calibrated anti-Xa testing estimates apixaban concentration.**','Interpret the result alongside timing, kidney function and other anticoagulants; routine PT/aPTT cannot safely rule out exposure.')]),
 ('Urgency Matters',[B('**Use the procedure-specific bleeding risk and laboratory turnaround.**','Do not delay emergency resuscitation for a slow assay or treat a concentration as a universal safe threshold for every operation.')])],['tests'])

Q('Factor Xa Reversal and Changing Availability','In a US hospital in 2026, an apixaban-associated life-threatening hemorrhage requires reversal. Andexanet is unavailable after cessation of US commercial sales. Which approach is most appropriate?',
 'Use a protocol-based four-factor PCC strategy with urgent source control',[
 ('Use idarucizumab because both drugs are direct oral anticoagulants','Idarucizumab is specific to dabigatran; membership in the DOAC category does not make antidotes interchangeable.'),
 ('Use protamine because apixaban and heparin inhibit factor Xa','Protamine neutralizes heparin molecules; it does not reverse apixaban simply because both pathways involve Xa inhibition.'),
 ('Use vitamin K because INR may increase during apixaban exposure','A raised INR does not convert apixaban into a VKA mechanism; vitamin K does not correct direct Xa inhibition.')],
 [('Current Context',[B('**Verify jurisdiction and availability.**','FDA reported an unfavorable benefit–risk assessment and US sales ended in December 2025; an older antidote table alone is insufficient.')]),
 ('Emergency Management',[B('**Stop the drug, resuscitate and control bleeding.**','4F-PCC is a nonspecific prohemostatic option, commonly 25–50 units/kg under local protocol; monitor thrombosis and reassess anticoagulation when safe.')])],['andex','bleed'])
