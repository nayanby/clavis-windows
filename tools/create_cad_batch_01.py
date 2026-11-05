"""Original ChatGPT-authored topic-based CAD/ACS draft batch. No model API calls."""
import json,html,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]/'build/topic-based-qbank-replacement'
ESC={'label':'2023 ESC Guidelines for Acute Coronary Syndromes: reperfusion and invasive management','url':'https://doi.org/10.1093/eurheartj/ehad191'}
ACS={'label':'2025 ACC/AHA/ACEP/NAEMSP/SCAI Acute Coronary Syndromes Guideline','url':'https://www.jacc.org/doi/10.1016/j.jacc.2024.11.009'}
CCD={'label':'2023 AHA/ACC Multisociety Chronic Coronary Disease Guideline','url':'https://www.jacc.org/doi/10.1016/j.jacc.2023.04.003'}
rows=[]
def add(stem,options,answer,title,principle,children,application,application_children,table,wrong,refs,style):
 rows.append(dict(question=stem,options=options,correctIndex=answer,questionStyle=style,explanationTeaching=dict(title=title,sections=[dict(heading='Diagnostic or treatment principle',bullets=[dict(text=principle,children=children)]),dict(heading='Applying the principle',bullets=[dict(text=application,children=application_children)])],tables=[dict(title='Comparison of the relevant strategies',headers=['Situation or strategy','Clinical interpretation'],rows=table)],otherOptions=[dict(optionIndex=i,explanation=text) for i,text in wrong]),references=refs))
add('A 58-year-old man presents 90 minutes after the onset of persistent chest pain with diagnostic anterior ST elevation. Primary PCI can achieve infarct-artery wire crossing 80 minutes after STEMI diagnosis. He has no contraindication to fibrinolysis. Which reperfusion strategy is preferred?',
['Immediate fibrinolysis followed by transfer for angiography','Immediate transfer for primary PCI without preceding fibrinolysis','Fibrinolysis immediately before planned PCI to facilitate reperfusion','Anticoagulation with angiography deferred until the following day'],1,
'Timely primary PCI in STEMI',
'**Primary PCI is preferred when PCI-mediated reperfusion can be achieved within the recommended time window.**',
['For this decision, the anticipated interval from STEMI diagnosis to infarct-artery wire crossing is more informative than transfer duration alone.','A predicted 80-minute interval is within the 120-minute threshold used by the ESC reperfusion strategy.'],
'**Eligibility for fibrinolysis does not make it the preferred strategy when timely PCI is available.**',
['The choice balances rapid reperfusion against the risks and limitations of fibrinolysis.','Do not delay reperfusion for nonessential testing once STEMI is established.'],
[['Timely primary PCI available','Proceed directly to primary PCI'],['Timely PCI unavailable, early presentation, no contraindication','Fibrinolysis followed by immediate transfer may be appropriate']],
[(0,'Fibrinolysis is an alternative when timely primary PCI cannot be provided; the stated PCI delay does not meet that condition.'),(2,'Routine fibrinolytic facilitation before otherwise timely primary PCI is not the recommended reperfusion pathway.'),(3,'Deferring angiography leaves an established acute coronary occlusion without prompt reperfusion.')],[ESC],'clinical_scenario')
add('A patient with STEMI receives fibrinolysis because timely primary PCI is unavailable. At 90 minutes, severe chest pain persists and ST elevation has fallen by only 20%. Which strategy is most appropriate?',
['Repeat fibrinolysis and reassess the ECG after another 90 minutes','Continue medical therapy and perform angiography routinely within 24 hours','Immediate angiography with rescue PCI if indicated','Schedule stress imaging before deciding whether angiography is necessary'],2,
'Failed fibrinolysis and rescue PCI',
'**Persistent ischemia with inadequate ST-segment resolution indicates failed reperfusion.**',
['Less than 50% ST-segment resolution at 60-90 minutes is an important failure criterion.','Ongoing pain or hemodynamic/electrical instability increases the urgency of invasive evaluation.'],
'**Rescue PCI is distinct from routine angiography after successful fibrinolysis.**',
['This patient has objective evidence that waiting for the routine post-lysis pathway would be inappropriate.','Treatment aims to establish infarct-artery patency rather than simply suppress symptoms.'],
[['Failed fibrinolysis or ongoing ischemia','Immediate angiography and rescue PCI'],['Successful fibrinolysis and stable course','Early routine angiography through a pharmacoinvasive strategy']],
[(0,'Repeating a fibrinolytic is not the recommended substitute for rescue PCI after failed reperfusion.'),(1,'Routine early angiography applies to successful lysis; persistent pain and poor ST resolution require urgent rescue.'),(3,'Stress testing is inappropriate in ongoing acute infarction with failed reperfusion.')],[ESC],'clinical_scenario')
add('After successful fibrinolysis for STEMI, a stable patient has resolution of pain and 75% ST-segment resolution. Under the ESC pharmacoinvasive strategy, when should routine coronary angiography generally be performed?',
['Within 2-24 hours after the fibrinolytic bolus','Only if recurrent ischemia develops before discharge','Routinely after 72 hours to reduce procedural bleeding','Only after a positive predischarge exercise test'],0,
'Routine angiography after successful fibrinolysis',
'**Successful fibrinolysis is followed by an invasive strategy rather than watchful waiting alone.**',
['Angiography is generally undertaken within 2-24 hours of the fibrinolytic bolus in stable patients.','Transfer to a PCI-capable center should begin promptly, even when the initial response appears favorable.'],
'**Immediate rescue and planned early angiography serve different clinical situations.**',
['Recurrent ischemia, failed ST resolution or instability changes the plan to urgent angiography.','Pain relief alone does not establish that the residual culprit lesion needs no further assessment.'],
[['Successful lysis, stable patient','Routine angiography within 2-24 hours'],['Failed lysis or recurrent ischemia','Immediate invasive evaluation']],
[(1,'An ischemia-only approach omits the routine invasive component of contemporary pharmacoinvasive care.'),(2,'A blanket 72-hour delay is outside the recommended early window in an otherwise suitable stable patient.'),(3,'Exercise testing is not required to justify routine angiography in this setting.')],[ESC],'direct')
add('A 62-year-old man presents two hours after onset of STEMI. Expected time to primary PCI is 170 minutes. He had a spontaneous intracranial hemorrhage three years ago. Which strategy is most appropriate?',
['Administer tenecteplase because the hemorrhage occurred more than one year ago','Use a reduced fibrinolytic dose because PCI is delayed','Withhold reperfusion and treat with antiplatelet therapy alone','Arrange urgent transfer for primary PCI despite the longer delay'],3,
'Fibrinolysis contraindications override the usual delay-based pathway',
'**A previous intracranial hemorrhage is a major contraindication to fibrinolysis.**',
['A remote event does not become acceptable simply because the patient is beyond a fixed one-year interval.','Assess contraindications before applying the usual preference for lysis when PCI will be substantially delayed.'],
'**Delayed PCI remains preferable to contraindicated fibrinolysis.**',
['The patient still requires an urgent reperfusion plan and transfer to a PCI-capable center.','Dose reduction does not remove the underlying intracranial bleeding concern.'],
[['Long PCI delay without a lysis contraindication','Consider the appropriate fibrinolysis-transfer pathway'],['Long PCI delay with prior intracranial hemorrhage','Pursue urgent PCI transfer rather than fibrinolysis']],
[(0,'Previous intracranial hemorrhage is not made safe for lysis by being three years old.'),(1,'Reducing the dose does not convert a contraindicated treatment into an acceptable reperfusion strategy.'),(2,'The contraindication concerns fibrinolysis, not the need for reperfusion by PCI.')],[ESC,ACS],'clinical_scenario')
add('Which statement about fibrinolytic therapy in non-ST-elevation acute coronary syndrome is correct?',
['It is indicated when high-sensitivity troponin is markedly elevated','It is not a routine treatment for NSTE-ACS, even when troponin is elevated','It is preferred if angiography cannot be performed within two hours','It becomes indicated when ST depression persists despite nitrates'],1,
'Fibrinolysis is not a troponin-driven treatment',
'**NSTE-ACS is managed with risk-directed antithrombotic and invasive strategies, not routine fibrinolysis.**',
['Troponin helps identify myocardial injury and risk; its magnitude does not independently create a fibrinolysis indication.','An ECG and the overall clinical picture determine whether an acute coronary occlusion pattern needs emergency reperfusion assessment.'],
'**Do not transfer the STEMI delay algorithm indiscriminately to all acute coronary syndromes.**',
['Persistent or recurrent ischemia may justify urgent angiography.','Urgency of invasive assessment does not mean that fibrinolytic treatment is appropriate.'],
[['STEMI meeting reperfusion criteria','Primary PCI or an appropriate fibrinolytic strategy'],['NSTE-ACS','Risk-based medical and invasive management; no routine fibrinolysis']],
[(0,'Marked troponin elevation can occur in NSTEMI but does not establish an indication for fibrinolysis.'),(2,'A delayed angiography slot is not a reason to apply the STEMI fibrinolysis pathway to NSTE-ACS.'),(3,'Persistent ischemic ST depression supports urgent reassessment and often invasive management rather than fibrinolysis.')],[ESC,ACS],'direct')
add('A patient with acute myocardial infarction has cardiogenic shock and multivessel coronary disease. The culprit artery is clearly identified and can be treated by PCI. What is the recommended initial PCI approach?',
['Treat the culprit and every angiographically significant nonculprit stenosis in the same procedure','Treat the nonculprit left anterior descending artery before the culprit lesion','Delay all coronary intervention until shock has resolved with medical support','Perform culprit-vessel revascularization without routine immediate nonculprit PCI'],3,
'Multivessel disease in infarct-related cardiogenic shock',
'**Emergency culprit-vessel revascularization is central to management.**',
['Re-establishing flow to the infarct-related artery addresses the immediate ischemic driver.','The shock setting differs from uncomplicated multivessel STEMI when planning complete revascularization.'],
'**Routine immediate nonculprit PCI is not recommended in cardiogenic shock.**',
['A blanket same-session multivessel approach increases procedural burden and is not the default strategy.','Nonculprit disease can be reassessed after stabilization; unusual anatomy or an uncertain culprit requires individualized judgment.'],
[['Infarct-related cardiogenic shock with identifiable culprit','Urgent culprit-vessel revascularization'],['Stable multivessel infarction after culprit treatment','Plan suitable complete revascularization according to anatomy and clinical context']],
[(0,'Routine immediate multivessel PCI is not the recommended default in shock; evidence from CULPRIT-SHOCK informs this distinction.'),(1,'An important nonculprit LAD lesion does not replace the identified culprit as the immediate treatment target.'),(2,'Shock is a reason for urgent revascularization rather than waiting for medical treatment to normalize hemodynamics.')],[ACS],'clinical_scenario')
add('For a patient with acute coronary syndrome treated with PCI who has no high bleeding risk and no indication for oral anticoagulation, what is the default duration of dual antiplatelet therapy?',
['One month for all contemporary drug-eluting stents','Three months irrespective of ischemic risk','At least 12 months, with subsequent treatment individualized','Indefinite dual therapy in every patient'],2,
'Default DAPT after acute coronary syndrome',
'**Aspirin plus an oral P2Y12 inhibitor is the default antiplatelet strategy after ACS.**',
['In patients without high bleeding risk, the default duration is at least 12 months.','The ACS presentation matters: do not assume that all PCI indications share the same default duration.'],
'**Default duration is not a substitute for individualized reassessment.**',
['High bleeding risk, oral anticoagulation, adverse events and selected de-escalation strategies may change treatment.','Indefinite DAPT is not automatically required after completing the initial ACS course.'],
[['ACS without high bleeding risk or oral anticoagulation','Default DAPT for at least 12 months'],['High bleeding risk or another competing indication','Individualize duration and antithrombotic regimen']],
[(0,'Very short DAPT is a selected bleeding-reduction strategy rather than the universal default after ACS.'),(1,'Three months ignores the stated low-bleeding-risk ACS context and cannot be applied irrespective of ischemic risk.'),(3,'Extended treatment can be appropriate in selected patients, but indefinite DAPT is not mandatory for everyone.')],[ACS],'direct')
add('A patient with diabetes has symptomatic chronic coronary disease involving three vessels, including the LAD, despite guideline-directed therapy. Both PCI and CABG are technically feasible, and surgical risk is acceptable. Which strategy is generally preferred to improve long-term outcomes?',
['CABG, with a left internal mammary artery graft to the LAD','PCI solely because diabetes increases the risk of surgical wound complications','Medical therapy alone regardless of persistent symptoms or anatomy','PCI to the LAD alone with no consideration of the remaining disease'],0,
'Diabetes and multivessel chronic coronary disease',
'**CABG is generally preferred over PCI in suitable patients with diabetes and multivessel disease involving the LAD.**',
['The decision incorporates long-term outcomes, coronary complexity and the feasibility of durable revascularization.','A left internal mammary artery graft to the LAD is an important component of the recommended surgical approach.'],
'**A Heart Team assessment should individualize the recommendation.**',
['Operative risk, comorbidity, life expectancy, anatomy and patient preferences remain relevant.','The stem explicitly establishes surgical suitability, so a generic objection to surgery should not overturn the preferred approach.'],
[['Diabetes, multivessel disease including LAD, suitable for surgery','CABG generally preferred'],['Prohibitive surgical risk or unsuitable surgical anatomy','Consider individualized alternatives including PCI']],
[(1,'Diabetes-related surgical risks must be assessed, but they do not automatically outweigh the preference for CABG in an otherwise appropriate candidate.'),(2,'Guideline-directed therapy remains essential, but this option disregards persistent symptoms and the stated multivessel revascularization context.'),(3,'An LAD-only approach ignores the need to plan revascularization around the full coronary anatomy and the comparative benefits of CABG.')],[CCD],'clinical_scenario')
def rich(text):return re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',html.escape(text))
def render(q):
 d=q['explanationTeaching'];parts=['<h2>'+rich(d['title'])+'</h2>'];plain=[d['title']]
 for sec in d['sections']:
  parts.append('<h3>'+rich(sec['heading'])+'</h3><ul>');plain.append(sec['heading'])
  for b in sec['bullets']:
   parts.append('<li>'+rich(b['text'])+'<ul>'+''.join('<li>'+rich(t)+'</li>' for t in b['children'])+'</ul></li>');plain.extend([b['text'],*b['children']])
  parts.append('</ul>')
 for t in d['tables']:
  parts.append('<h3>'+rich(t['title'])+'</h3><table><thead><tr>'+''.join('<th>'+rich(h)+'</th>' for h in t['headers'])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+rich(x)+'</td>' for x in row)+'</tr>' for row in t['rows'])+'</tbody></table>');plain.extend([t['title'],*[' | '.join(row) for row in t['rows']]])
 parts.append('<h3>Other Options</h3><ul>')
 for a in d['otherOptions']:parts.append('<li><strong>'+rich(q['options'][a['optionIndex']])+':</strong> '+rich(a['explanation'])+'</li>');plain.append(q['options'][a['optionIndex']]+': '+a['explanation'])
 parts.append('</ul>');q['explanationHtml']=''.join(parts);q['explanation']='\n\n'.join(plain)
for i,q in enumerate(rows):
 q.update(id=f'cardiology-cad-acs-{i+1:03}',authorship='Original ChatGPT-authored topic-based question; not an authenticated examination PYQ',reviewStatus='draft',sourceCheckedAt='2026-11-05')
 assert len(q['options'])==4 and len(set(q['options']))==4
 assert {a['optionIndex'] for a in q['explanationTeaching']['otherOptions']}==set(range(4))-{q['correctIndex']}
 assert q['references'] and q['explanationTeaching']['tables']
 render(q)
assert [sum(q['correctIndex']==i for q in rows) for i in range(4)]==[2,2,2,2]
out=ROOT/'drafts/Cardiology/01. Coronary Artery Disease and Acute Coronary Syndromes';out.mkdir(parents=True,exist_ok=True)
bank=dict(folder='Cardiology',document='Coronary Artery Disease and Acute Coronary Syndromes',headingText='Coronary Artery Disease and Acute Coronary Syndromes',chapterOrder=1,topicOrder=1,targetQuestions=44,status='draft_in_progress',questions=rows)
p=out/'cad-acs-draft.json';p.write_text(json.dumps(bank,ensure_ascii=False,indent=2),encoding='utf-8')
planpath=ROOT/'topic-map.json';plan=json.loads(planpath.read_text(encoding='utf-8'));plan['status']='draft_generation_started'
for s in plan['subjects']:
 for c in s['chapters']:
  if s['subject']=='Cardiology' and c['chapterOrder']==1:c.update(status='draft_in_progress',draftQuestionCount=len(rows),draftFile=str(p.relative_to(ROOT)))
planpath.write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'chapter':'Cardiology: CAD and ACS','draftQuestions':len(rows),'target':44,'answerDistribution':dict(A=2,B=2,C=2,D=2),'clinical':sum(q['questionStyle']=='clinical_scenario' for q in rows),'direct':sum(q['questionStyle']=='direct' for q in rows),'path':str(p.resolve()),'activeBanksReplaced':0},indent=2))
