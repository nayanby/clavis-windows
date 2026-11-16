"""Cyanotic physiology and evidence-specific Eisenmenger decisions."""
from qbank_json_chapters import question as Q

TOPIC='Eisenmenger syndrome and cyanotic physiology'
REFERENCES={
 'EISEN_IRON':('Prospective iron replacement in cyanotic CHD, Tay et al., 2011','https://pubmed.ncbi.nlm.nih.gov/20580108/'),
 'BREATHE5':('Bosentan in Eisenmenger syndrome: BREATHE-5 randomized trial, 2006','https://pubmed.ncbi.nlm.nih.gov/16801459/'),
 'MAESTRO':('Macitentan in Eisenmenger syndrome: MAESTRO randomized trial, 2019','https://pmc.ncbi.nlm.nih.gov/articles/PMC6314514/'),
 'BOSENTAN_LABEL':('Bosentan FDA prescribing information, revised November 2025','https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/021290s048%2C209279s015lbl.pdf'),
 'EPOPROSTENOL_LABEL':('Epoprostenol prescribing information, DailyMed, 2026','https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=47f64fcd-cbf7-457a-9548-661fb10ff7e0'),
}
def S(h,t,*children):return h,[(t,list(children))]
rows=[]
def add(*args,**kwargs):rows.append(Q(*args,**kwargs))

add(TOPIC,'Eisenmenger Syndrome Within PAH Associated With Congenital Shunts',
 'A 34-year-old with a large unrepaired VSD had pulmonary overcirculation in childhood. Current catheterization shows mean PA pressure 75 mmHg, wedge pressure 10 mmHg, PVR 18 Wood units and Qp/Qs 0.8. Systemic saturation is 82%, with bidirectional flow and no RV outflow obstruction. Which PAH-CHD category best fits?',
 'Eisenmenger syndrome',[
 ('PAH associated with a small coincidental defect','Small defects can coexist with a pulmonary arteriopathy resembling idiopathic PAH, without having caused the vascular disease. This patient instead has a large longstanding shunt, documented earlier overcirculation and subsequent reversal of its net direction.'),
 ('PAH persisting after correction of a congenital defect','PAH may persist or emerge after surgical or catheter correction. That category requires a repaired defect; the supplied VSD remains open and is the route for desaturated systemic flow.'),
 ('PAH with a prevalent systemic-to-pulmonary shunt','That group retains predominant left-to-right flow, generally without resting cyanosis from shunt reversal. The current net Qp/Qs below one and arterial desaturation place this patient in the Eisenmenger group.')],
 [S('Evolution of the Pulmonary Vascular Lesion',
  '**A large congenital systemic-to-pulmonary communication can produce progressive pulmonary vascular remodeling.** As resistance rises, the original flow excess diminishes and eventually becomes bidirectional or predominantly right-to-left.',
  'The low wedge pressure supports a precapillary process rather than isolated pulmonary venous hypertension. The history establishes the causal large shunt; cyanosis alone would not distinguish pulmonary vascular disease from restricted pulmonary flow in another congenital lesion.'),
  S('Implications for Repair and Ongoing Care',
  '**Established Eisenmenger physiology is not an uncomplicated closure indication.** Eliminating the communication can remove a pressure-relief route and precipitate severe right-heart failure.',
  'A fall in pulmonary pressure during treatment does not by itself establish reversibility or justify closure. Expert assessment integrates resistance, flow direction, filling pressures and ventricular function; selected treat-and-repair pathways for other shunt phenotypes must not be transferred automatically.',
  'Management includes ACHD and pulmonary-hypertension expertise, functional assessment, iron and renal monitoring, and evaluation for targeted PAH therapy. Bleeding, arrhythmia, paradoxical embolism and infection can complicate cyanotic disease. Pregnancy counseling is essential because maternal risk is very high. Intravascular procedures require meticulous exclusion of air from lines when right-to-left passage is possible.')],
 ['ESC2020','ACHD2025'],table=(['PAH-CHD group','Distinguishing context'],[
 ['Eisenmenger','Large causal shunt with advanced pulmonary vascular disease and reversal'],
 ['Prevalent systemic-to-pulmonary shunt','Predominantly left-to-right flow remains'],
 ['Small/coincidental defect','Defect insufficient to explain the pulmonary vascular disease'],
 ['After correction','PAH persists or develops after anatomical repair']]))

add(TOPIC,'Compensated Secondary Erythrocytosis in Cyanotic CHD',
 'A stable adult with Eisenmenger syndrome has hemoglobin 22 g/dL, hematocrit 68%, MCV 88 fL and ferritin 70 micrograms/L. Hydration is adequate, and there is no headache, visual disturbance or other hyperviscosity symptom. Which approach to the erythrocytosis is best?',
 'Maintain hydration and monitor without scheduled phlebotomy',[
 ('Perform isovolumic phlebotomy because hematocrit exceeds 65%','Expert isovolumic phlebotomy may be considered for persistent clinically important hyperviscosity after dehydration and iron deficiency are corrected. Exceeding a numerical threshold without symptoms does not supply that indication.'),
 ('Schedule repeated phlebotomy to achieve the hematocrit target used in polycythemia vera','Polycythemia vera is a clonal myeloproliferative disorder with a different thrombotic mechanism and treatment target. Applying its target to adaptive hypoxemic erythrocytosis can impair oxygen delivery and deplete iron.'),
 ('Start aspirin solely to counter the elevated red-cell mass','Antiplatelet therapy has established indications in atherosclerotic disease and selected hematological settings. Cyanotic erythrocytosis alone does not establish benefit, while abnormal hemostasis can increase bleeding risk.')],
 [S('Oxygen Transport and Compensatory Red-Cell Mass',
  '**Chronic arterial desaturation stimulates erythropoiesis.** An increased hemoglobin concentration helps preserve oxygen content when the saturation of each hemoglobin molecule is reduced.',
  'The hemoglobin value therefore requires interpretation with oxygen saturation, symptoms and iron status. A high value in this setting does not by itself establish a myeloproliferative neoplasm or a need to normalize the count.'),
  S('When Symptoms Change the Assessment',
  '**Persistent hyperviscosity is a clinical diagnosis after competing causes are considered.** Review hydration and iron indices before attributing fatigue, headache or dizziness to the hematocrit.',
  'The current ACHD pathway considers phlebotomy for persistent symptoms with hematocrit above 65% despite adequate hydration and iron repletion. If selected, it requires experienced supervision with isovolumic replacement, not repeated unsupervised blood donation.',
  'New severe headache, fever, focal neurological findings or altered consciousness requires urgent evaluation for causes such as stroke or brain abscess. It should not be labeled hyperviscosity from a blood count alone. Follow-up includes symptoms, saturation, full blood count and iron indices. Inappropriate repeated venesection can create iron deficiency even while the absolute hemoglobin remains above the usual laboratory reference interval.')],
 ['ACHD2025','ESC2020'])

add(TOPIC,'Iron Deficiency Despite an Elevated Hemoglobin',
 'A cyanotic adult has increasing fatigue, hemoglobin 19 g/dL, hematocrit 60%, MCV 66 fL, ferritin 7 micrograms/L and transferrin saturation 8%. There is no acute bleeding or hemodynamic deterioration. Which strategy best addresses the laboratory abnormality?',
 'Replace iron with monitored reassessment of blood count and iron indices',[
 ('Withhold iron because the hemoglobin is already above the laboratory reference range','A raised hemoglobin can be an appropriate response to hypoxemia. It does not exclude depleted stores; low ferritin and transferrin saturation provide direct evidence of iron deficiency here.'),
 ('Perform venesection before giving iron to prevent a further hematocrit increase','Venesection may have a narrow role in persistent symptomatic hyperviscosity after other factors are corrected. In this iron-deficient patient it would remove additional iron and red cells rather than address the demonstrated deficiency.'),
 ('Defer iron until a hemoglobinopathy panel explains the microcytosis','Thalassemia is a genuine cause of microcytosis and may coexist. However, the depleted iron indices already justify replacement and assessment of its cause; persistent unexplained microcytosis can subsequently prompt additional testing.')],
 [S('Recognizing Relative Hematological Inadequacy',
  '**Laboratory reference ranges derived from noncyanotic adults can conceal iron deficiency in cyanotic CHD.** Interpret hemoglobin alongside saturation and iron studies rather than using a high hemoglobin to exclude deficiency.',
  'Microcytosis supports the finding but is not a substitute for ferritin and transferrin saturation. Inflammatory states can complicate ferritin interpretation; the very low ferritin in this case is persuasive evidence of depleted stores.'),
  S('Replacement, Evidence and Monitoring',
  '**Correct the deficiency and investigate its source.** Review dietary intake, menstrual or gastrointestinal loss and prior phlebotomy. Route and dose depend on tolerability, severity and the specialist treatment plan.',
  'A small prospective cyanotic-CHD study used oral ferrous fumarate titrated up to 200 mg three times daily for three months. This is the mass of the iron salt, not 200 mg of elemental iron per dose, and is a study protocol rather than a mandatory starting regimen.',
  'That study found improved iron stores, walking performance and reported quality of life; peak oxygen uptake did not significantly improve. Its uncontrolled design and mixed congenital population limit causal and survival claims. Recheck clinical response, hemoglobin and iron indices, and adjust replacement rather than withholding needed iron merely because erythropoiesis may increase. Persistent symptoms after correction require assessment for cardiac, pulmonary vascular and other systemic causes.')],
 ['EISEN_IRON','ESC2020'])

add(TOPIC,'Interpreting Eisenmenger Endothelin-Antagonist Trials',
 'Which statement correctly distinguishes randomized endothelin-receptor-antagonist evidence in Eisenmenger syndrome?',
 'BREATHE-5 improved pulmonary vascular resistance without worsening systemic oxygen saturation',[
 ('MAESTRO met its primary endpoint by improving six-minute walk distance over placebo','MAESTRO studied macitentan in a broader Eisenmenger population, but did not show superiority for the primary six-minute walk endpoint. Exploratory biomarker and hemodynamic signals cannot be relabeled as a positive primary endpoint.'),
 ('BREATHE-5 established bosentan superiority over sildenafil in a direct randomized comparison','BREATHE-5 compared bosentan with placebo. It did not randomize patients between an endothelin antagonist and a PDE5 inhibitor, so it cannot establish comparative superiority between those drug classes.'),
 ('MAESTRO demonstrated lower mortality as its primary treatment effect','MAESTRO assessed exercise capacity over 16 weeks, not a primary mortality endpoint. A short-term functional trial does not establish a survival benefit simply because its drug is used in PAH.')],
 [S('Population and Endpoint Matter',
  '**BREATHE-5 enrolled 54 WHO functional class III patients and compared bosentan with placebo for 16 weeks.** Oxygen saturation was the primary safety endpoint and pulmonary vascular resistance the primary efficacy endpoint.',
  'The trial also found a favorable walking-distance effect. It supported treatment without the feared deterioration in systemic oxygenation; it was not a head-to-head trial or a mortality trial.',
  'MAESTRO enrolled 226 patients, included a more heterogeneous population and permitted selected background PAH treatment. Its negative primary exercise endpoint must remain explicit despite exploratory findings. Different populations and trial conduct prevent a simple indirect ranking of the two agents.'),
  S('Applying Treatment and Monitoring',
  '**Bosentan blocks both ETA and ETB receptors.** For an adult weighing more than 40 kg, the labeled oral regimen starts at 62.5 mg twice daily and increases after four weeks to 125 mg twice daily if appropriate.',
  'Obtain aminotransferases before treatment and monthly thereafter; monitor hemoglobin, fluid retention and interactions. Pregnancy is contraindicated. Effective contraception is required during treatment and for one month after stopping, and bosentan can reduce hormonal contraceptive effectiveness.',
  'Therapy is selected and escalated by congenital and PAH specialists according to symptoms, functional assessment and response. ERA and PDE5-inhibitor strategies should not be judged from a false claim that every ERA trial was positive.'),
  S('Escalation Beyond Oral Monotherapy',
  '**Persistent limitation or deterioration requires reassessment and specialist escalation.** A PDE5 inhibitor is another initial option, and an ERA/PDE5-inhibitor combination may be selected according to the clinical response. Adult sildenafil commonly starts at 20 mg orally three times daily; organic nitrates and riociguat must not be coadministered.',
  'Prostacyclin-pathway treatment may be considered when oral therapy is ineffective or poorly tolerated. For selected advanced disease, continuous IV epoprostenol is an expert-center option. The labeled initial infusion is 2 ng/kg/min, with initial increments of 2 ng/kg/min at intervals of at least 15 minutes according to tolerance; this is a monitored initiation regimen, not a fixed maintenance dose or an automatic prescription for all Eisenmenger patients.',
  'Monitor systemic pressure, oxygenation, symptoms and fluid status. Flushing, headache, jaw pain, diarrhea and hypotension can limit titration. Interruption of a continuous epoprostenol infusion can cause dangerous rebound pulmonary hypertension; infusion access, backup delivery and infection prevention require explicit planning. Right-to-left shunting adds the need for meticulous exclusion of air from lines.',
  'Evidence from other PAH phenotypes must not be treated as proof of the same benefit in Eisenmenger syndrome. Clinical deterioration also warrants assessment of arrhythmia, infection, iron deficiency, thromboembolism and ventricular function rather than dose escalation without reassessment.')],
 ['BREATHE5','MAESTRO','BOSENTAN_LABEL','ACHD2025','SILDENAFIL_LABEL','EPOPROSTENOL_LABEL'],style='direct',
 table=(['Trial','Treatment / primary outcome interpretation'],[
 ['BREATHE-5, 16 weeks','Bosentan: PVR benefit; systemic saturation safety preserved'],
 ['MAESTRO, 16 weeks','Macitentan: primary 6-minute walk superiority not demonstrated']]))

add(TOPIC,'Antithrombotic Decisions in Eisenmenger Syndrome',
 'An adult with Eisenmenger syndrome is in sinus rhythm, has no prior venous thromboembolism, no intracardiac thrombus and no mechanical valve. There have been intermittent minor hemoptysis episodes. Which long-term antithrombotic strategy is most appropriate solely for the Eisenmenger diagnosis?',
 'Do not prescribe routine oral anticoagulation; reassess if a separate indication develops',[
 ('Start a vitamin K antagonist to prevent pulmonary vascular thrombosis','A vitamin K antagonist may be appropriate for a separate established indication after individualized assessment. Eisenmenger physiology alone has not shown a preventive survival benefit sufficient to offset its bleeding risk.'),
 ('Start a direct oral anticoagulant because it avoids INR monitoring','Convenience does not create an anticoagulation indication. A DOAC requires an appropriate thromboembolic indication, consideration of the congenital phenotype, renal function and bleeding risk; none is established by the supplied history alone.'),
 ('Use aspirin as a lower-intensity substitute for preventive anticoagulation','Aspirin has distinct arterial indications but is not a proven substitute for routine thromboprophylaxis in cyanotic CHD. It can also worsen bleeding, including in a patient with hemoptysis.')],
 [S('Simultaneous Thrombotic and Hemorrhagic Risk',
  '**Cyanotic CHD can produce both thrombosis and bleeding.** Altered platelet number or function and coagulation abnormalities coexist with vascular dilation, stasis and possible thrombus formation.',
  'An elevated hematocrit does not mean that all clinical risk is thrombotic or that antithrombotic treatment will improve outcomes. The presence, location and likely age of any detected thrombus matter; organized in-situ pulmonary arterial thrombus is not automatically equivalent to a new embolic event.'),
  S('Separate Indications and Bleeding Assessment',
  '**Current ACHD guidance advises against routine oral anticoagulation for Eisenmenger syndrome alone.** Reconsider treatment if atrial arrhythmia, documented thromboembolism, a mechanical prosthesis or another independent indication appears.',
  'Even with an indication, review bleeding history, platelet count, renal and hepatic function, concurrent drugs and the proposed agent with experienced clinicians. A mechanical valve has a specific vitamin K antagonist requirement; one should not substitute a DOAC merely to simplify follow-up.',
  'Active significant hemoptysis requires urgent clinical assessment and stabilization, with investigation of its cause and specialist decisions about antithrombotic interruption or reversal when relevant. Recurrent minor bleeding also deserves evaluation. If warfarin is used, a markedly high hematocrit requires the laboratory to consider citrate adjustment for coagulation sampling, because standard sampling can distort results. The decision is driven by the actual competing risks rather than a universal procoagulant label.')],
 ['ACHD2025','ESC2020'])
