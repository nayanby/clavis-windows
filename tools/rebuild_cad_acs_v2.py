"""Complete CAD/ACS revision under the user's postgraduate Qbank quality standard."""
import copy,json,random,re
from pathlib import Path
from html import escape
from qbank_authoring import ROOT,ref

# Every option set is authored as a single clinically comparable group.
# Correct answer comes first here; serialization uses independently shuffled positions.
SETS=[
('Primary PCI','Fibrinolysis followed by transfer','Fibrinolytic-facilitated immediate PCI','Antithrombotic treatment with delayed angiography',
 ['A pharmacoinvasive strategy is appropriate when timely PCI is unavailable, not when wire crossing is expected in 80 minutes.','Facilitated PCI adds fibrinolytic exposure before otherwise timely PCI and is not the recommended default.','Established STEMI requires reperfusion rather than antithrombotic treatment alone.']),
('Urgent angiography for rescue PCI','Repeat the fibrinolytic dose','Routine angiography in 12–24 hours','Antithrombotic treatment with symptom-guided angiography',
 ['Repeat fibrinolysis is inferior to the rescue-PCI pathway when reperfusion has failed.','That timing suits stable successful fibrinolysis, not persistent ischemia with 20% ST resolution.','Persistent pain and failed ST resolution already establish the need for urgent reassessment.']),
('2–24 hours','Within 60 minutes irrespective of reperfusion','24–72 hours','After a predischarge ischemia test',
 ['Immediate rescue angiography is required for failed reperfusion or instability, rather than routinely for this stable successful case.','This delays the recommended pharmacoinvasive assessment.','Successful lysis does not remove the indication for routine early coronary angiography.']),
('Urgent transfer for primary PCI','Full-dose fibrinolysis followed by transfer','Half-dose fibrinolysis followed by transfer','Antithrombotic treatment with deferred angiography',
 ['Previous spontaneous intracranial hemorrhage is a major contraindication to fibrinolysis.','Reducing the dose does not remove this contraindication.','The contraindication to lysis does not justify leaving an early STEMI without an urgent reperfusion strategy.']),
('Not indicated for routine NSTE-ACS reperfusion','Indicated when troponin exceeds five times the URL','Indicated when GRACE score exceeds 140','Indicated for dynamic ST depression despite nitrates',
 ['Troponin elevation establishes injury, not a fibrinolytic indication.','High GRACE risk supports an invasive strategy, not fibrinolysis.','Refractory ischemia supports urgent angiography, not routine NSTE-ACS lysis.']),
('Culprit-vessel PCI during the initial procedure','Complete multivessel PCI during the initial procedure','Nonculprit PCI followed by culprit PCI','Medical stabilization followed by elective multivessel PCI',
 ['Routine immediate multivessel PCI in infarct-related shock can worsen outcomes compared with an initial culprit-only strategy.','Treating nonculprit lesions first leaves the identified acute ischemic driver untreated.','Shock with an amenable culprit lesion requires urgent revascularization rather than elective deferral.']),
('At least 12 months','1 month','3 months','6 months',
 ['A one-month strategy can be appropriate in selected bleeding-risk or monotherapy pathways, not the specified default.','Abbreviated strategies require patient and regimen selection.','Six months may apply in other contexts; it is not the default ACS duration in this low-bleeding-risk setting.']),
('CABG with an internal mammary graft to the LAD','Multivessel PCI with contemporary drug-eluting stents','PCI confined to the LAD','Medical therapy without revascularization despite persistent symptoms',
 ['PCI may be selected when surgery is unsuitable, but diabetes with suitable multivessel disease favors CABG for long-term outcomes.','An LAD-only strategy does not address the full clinically important anatomy.','Persisting symptoms and suitable anatomy justify revascularization assessment; medical therapy remains necessary with either procedure.']),
('Additional evidence of acute myocardial ischemia','An absolute troponin concentration above five times the URL','A new reduction in ejection fraction without an ischemic pattern','A rise in an inflammatory marker accompanying the troponin rise',
 ['A higher concentration does not by itself distinguish infarction from nonischemic injury.','A nonspecific EF decline does not establish the required ischemic mechanism.','Inflammation can accompany myocarditis or systemic illness and is not proof of infarction.']),
('Secondary MI from oxygen supply–demand imbalance','Primary MI from coronary atherothrombosis','Acute nonischemic myocardial injury','Chronic myocardial injury associated with systemic disease',
 ['No acute atherothrombotic mechanism is demonstrated; profound anemia and tachycardia provide a supply–demand trigger.','The ischemic pain and new ST depression distinguish this from injury without ischemic evidence.','A dynamic troponin pattern with an acute presentation argues against chronic stable injury.']),
('Assay-specific baseline and delta thresholds with clinical assessment','One common absolute delta for all high-sensitivity assays','One common percentage delta regardless of baseline concentration','The 99th-percentile concentration alone without serial change',
 ['Assays are not analytically interchangeable; validated pathways use assay-specific cutoffs.','Percentage change is affected by baseline concentration and is not a universal accelerated-pathway rule.','A single abnormal value does not separate chronic injury from an evolving acute process.']),
('V7–V9','V3R–V4R','V1–V2 one interspace higher','V5–V6 repeated at the usual positions',
 ['Right-sided leads assess RV involvement, especially with inferior MI.','High right-precordial placement is useful for other questions such as a Brugada pattern.','Repeating lateral leads does not provide the posterior view required here.']),
('V4R','V7','V9','aVR',
 ['V7 is a posterior lead rather than the principal right-sided RV lead.','V9 evaluates the posterior LV territory.','aVR can inform other ischemic patterns but does not replace right-sided leads for RV infarction.']),
('Acute aortic dissection involving a coronary ostium','Primary inferior coronary thrombosis without aortic disease','Acute pulmonary embolism with RV strain','Acute pericarditis with regional ECG changes',
 ['Inferior STEMI can be secondary to dissection; pulse asymmetry and new aortic regurgitation make isolated thrombosis an inadequate assumption.','PE can cause shock and RV strain but does not explain the aortic-regurgitation/pulse-deficit pattern.','Pericarditis does not account for the combined aortic and vascular findings.']),
('No routine supplemental oxygen','Nasal oxygen targeting saturation of 100%','Face-mask oxygen until troponin peaks','High-flow oxygen until reperfusion',
 ['Hyperoxia is not the treatment goal in normoxemic uncomplicated ACS.','Troponin kinetics do not determine an oxygen requirement.','Reperfusion status alone does not justify high-flow oxygen in a patient at 97%.']),
('Withhold nitrate because the tadalafil interval is under 48 hours','Give sublingual nitrate because blood pressure is normal','Use intravenous nitrate at a reduced initial dose','Give nitrate once 24 hours have elapsed after tadalafil',
 ['A normal initial pressure does not prevent profound hypotension from the interaction.','Changing the route or reducing the dose does not remove the contraindicated interaction.','The usual tadalafil interval is 48 hours; 24 hours applies to sildenafil or vardenafil.']),
('Previous ischemic stroke or TIA','Age 76 years without prior cerebrovascular disease','Body weight 56 kg without prior cerebrovascular disease','Diabetes treated with insulin',
 ['Older age raises bleeding concern and affects selection, but it differs from the specified absolute stroke/TIA contraindication.','Low body weight affects bleeding risk and maintenance dosing, not the same absolute contraindication.','Diabetes increases ischemic risk and does not itself contraindicate prasugrel.']),
('Stop aspirin at 1–4 weeks; continue anticoagulant plus clopidogrel','Stop clopidogrel at 1–4 weeks; continue anticoagulant plus aspirin','Continue triple therapy for 12 months','Stop anticoagulation at 1–4 weeks; continue aspirin plus clopidogrel',
 ['The preferred dual regimen after early triple therapy retains the P2Y12 inhibitor with the indicated anticoagulant.','Prolonged triple therapy exposes the patient to excess bleeding and is not the default.','DAPT does not replace indicated anticoagulation for AF-related embolic risk.']),
('Defer routine loading until coronary anatomy and strategy are established','Load prasugrel before angiography because troponin is elevated','Load ticagrelor before angiography because the procedure is within 24 hours','Load clopidogrel before angiography in every early-invasive patient',
 ['Routine prasugrel pretreatment before defining anatomy is not recommended in this setting.','Early planned angiography is a reason not to apply routine pretreatment, not a reason to mandate it.','Clopidogrel is not exempt from the routine-pretreatment principle; selected delayed-strategy contexts differ.']),
('Radial access','Femoral access','Brachial access','Ulnar access as the default for all patients',
 ['Femoral access remains useful when indicated but has greater access-site bleeding risk in the stated comparison.','Brachial access is not the routine bleeding-minimizing approach.','Ulnar access can be an alternative, but radial is the guideline-preferred standard when feasible.']),
('Intravascular ultrasound','Quantitative coronary angiography alone','Fractional flow reserve alone','Coronary flow reserve alone',
 ['Angiography is a lumen projection and cannot characterize expansion and edges as directly as intravascular imaging.','FFR evaluates pressure-derived physiological significance rather than detailed stent geometry.','CFR assesses flow reserve and does not directly identify stent expansion or edge dissection.']),
('Papillary muscle rupture','Ventricular septal rupture','LV free-wall rupture','Acute ischemic MR from leaflet tethering without rupture',
 ['Septal rupture causes a shunt rather than the flail leaflet described.','Free-wall rupture causes hemopericardium and tamponade, not a flail mitral leaflet.','Ischemic tethering can cause MR, but a new flail leaflet points to rupture of the support apparatus.']),
('Ventricular septal rupture','Papillary muscle rupture','LV free-wall rupture','Acute severe tricuspid regurgitation',
 ['Acute MR explains pulmonary edema but not a ventricular-level oxygen-saturation step-up.','Free-wall rupture causes tamponade rather than an intracardiac left-to-right shunt.','TR causes regurgitant venous findings, not oxygenated LV blood entering the RV.']),
('LV free-wall rupture','Ventricular septal rupture','Papillary muscle rupture','Massive pulmonary embolism',
 ['VSR produces a shunt; it does not directly explain new hemorrhagic pericardial material.','Papillary rupture produces acute MR rather than hemopericardium.','PE can cause PEA but the new tamponade-producing effusion after MI favors rupture.']),
('Narrow-neck communication with a pericardially contained rupture','Broad-neck outpouching lined by thinned myocardial scar','Apical dyskinesia with persistent ST elevation','Mural thrombus over an akinetic ventricular segment',
 ['A broad-neck myocardial scar outpouching more strongly favors a true aneurysm.','Dyskinesia and persistent ST elevation can accompany a true aneurysm and are not specific for pseudoaneurysm.','Thrombus can accompany several ventricular abnormalities; it does not establish contained rupture.']),
('Early infarct-associated pericarditis','Post-cardiac injury syndrome several weeks after MI','Recurrent infarction from acute coronary reocclusion','LV pseudoaneurysm with contained rupture',
 ['The delayed immune-mediated syndrome has a different usual time course.','Recurrent infarction must be considered, but positional pleuritic pain and a rub favor pericarditis.','Pseudoaneurysm is a structural diagnosis and is not established by an isolated early pericardial rub.']),
('Late-gadolinium-enhancement cardiac MRI','Noncontrast transthoracic echo alone','Routine coronary CT angiography','Repeat invasive coronary angiography',
 ['The mass remains equivocal even after contrast echo; repeating a less sensitive approach is not the best next test.','Routine coronary CT targets coronary anatomy rather than offering the preferred tissue characterization for this question.','A coronary angiogram does not resolve the apical tissue-characterization problem.']),
('Complete AV block with a slow broad-QRS escape','Wenckebach block with a narrow QRS after inferior MI','Transient sinus bradycardia responding to atropine','First-degree AV block with a narrow QRS',
 ['This more often reflects AV nodal involvement rather than extensive infranodal necrosis.','A vagally mediated or sinus-node presentation differs from a distal conduction-system escape.','PR prolongation alone is less suggestive of extensive distal injury.']),
('Myocardial injury with nonobstructive coronary arteries','Myocardial infarction proven to arise from plaque rupture','Microvascular angina without myocardial injury','Takotsubo syndrome established by angiography alone',
 ['The 2026 umbrella includes injury; plaque rupture is one potential cause rather than the definition.','Microvascular angina can occur without an acute injury pattern and is not the expansion of MINOCA.','Takotsubo requires compatible imaging and clinical assessment; a nonobstructive angiogram does not establish it.']),
('Conservative inpatient management with monitoring','PCI across the full dissected segment','Immediate CABG for the mid-distal lesion','Fibrinolysis followed by planned angiography',
 ['PCI can propagate intramural hematoma and is reserved for appropriate high-risk or unstable situations.','Stable preserved-flow mid-distal disease does not establish a surgical indication.','Fibrinolysis can worsen dissection-related bleeding and is not appropriate for confirmed SCAD.']),
('Takotsubo syndrome','Anterior MI from an obstructed LAD','Acute myocarditis','Multivessel epicardial coronary spasm',
 ['The absence of a culprit obstruction and dysfunction beyond one territory favor another mechanism.','Myocarditis remains a differential, but the stress-associated characteristic ventricular pattern favors Takotsubo; CMR may help.','Spasm requires its own evidence and is not the best explanation of the supplied characteristic contraction pattern.']),
('Calcium-channel blocker','Beta-1-selective blocker','Ranolazine as sole first-line prevention','Ivabradine as sole first-line prevention',
 ['Beta blockers are not the principal preventive treatment for demonstrated epicardial spasm.','Ranolazine can have other antianginal roles but does not replace a CCB as the mainstay here.','Heart-rate reduction does not directly address the vasospastic mechanism.']),
('Coronary microvascular dysfunction','Flow-limiting focal epicardial stenosis','Primary epicardial coronary spasm','Secondary MI from acute atherothrombosis',
 ['FFR 0.93 argues against a hemodynamically significant focal epicardial stenosis.','Spasm is not established by low CFR and high microvascular resistance alone.','No acute infarction or thrombotic mechanism is supplied.']),
('FFR 0.80; meets the usual ischemic threshold','FFR 0.80; above the usual ischemic threshold','FFR 1.25; meets the usual ischemic threshold','FFR 1.25; indicates absent epicardial pressure loss',
 ['An FFR at or below 0.80 meets the commonly used threshold.','This reverses distal and aortic pressures.','The ratio is distal divided by aortic pressure during adequate hyperemia; reversing it is not valid interpretation.']),
('Resting pressure index; ischemic threshold 0.89 or less','Hyperemic pressure index; ischemic threshold 0.89 or less','Resting pressure index; ischemic threshold 0.80 or less','Hyperemic flow reserve; ischemic threshold 2.0 or less',
 ['iFR is obtained without pharmacological hyperemia.','0.80 is the usual FFR threshold, not the standard iFR threshold.','CFR is a flow-reserve measure and differs from a resting pressure-derived iFR.']),
('Heart Team assessment with CABG favored','Distal left-main PCI as the default irrespective of complexity','PCI confined to non-left-main lesions','Medical treatment alone because LV function is preserved',
 ['PCI can be appropriate in selected left-main anatomy, but high-complexity disease with acceptable surgery risk favors CABG.','Leaving significant left-main disease unaddressed does not solve the prognostic anatomical problem.','Preserved EF does not remove the importance of significant complex left-main disease.']),
('No reduction in the primary composite with an initial invasive strategy during the main follow-up','Reduction in the primary composite supporting routine PCI for every ischemic stress test','Equivalent results establishing medical treatment for significant left-main disease','Superior outcomes supporting PCI for uncontrolled angina without considering anatomy',
 ['The main trial did not show this primary-composite advantage.','Significant left-main disease was excluded; the result cannot be extrapolated to it.','Refractory symptoms and anatomical suitability require separate assessment; this does not describe the trial conclusion.']),
('Relief of angina and improvement in functional status','Prevention of all subsequent plaque-rupture events','Replacement of long-term lipid-lowering therapy','Established survival benefit from PCI in every stable lesion',
 ['Treating a stenosis does not remove systemic plaque vulnerability.','Secondary prevention remains necessary after revascularization.','The survival implication depends on anatomy and clinical context; symptom benefit is the well-established indication here.']),
('Ranolazine','Ivabradine','Higher-dose metoprolol','Long-acting isosorbide mononitrate',
 ['Further heart-rate reduction is unattractive with a resting rate of 52/min.','Additional beta blockade can worsen bradycardia and hypotension.','A nitrate may aggravate the blood-pressure limitation.']),
('Reassess the indication and consider supervised tapering if appropriate','Continue specifically for a proven lifelong mortality benefit in preserved EF','Replace with another beta blocker to secure the same presumed prognostic benefit','Increase the dose solely because the MI occurred previously',
 ['The specified 2023 guideline does not establish that unconditional remote-MI benefit.','Switching agents does not create an outcome indication absent in the clinical setting.','Dose escalation requires a current indication and physiological tolerance.']),
('Add a nonstatin LDL-lowering agent to the tolerated statin','Continue the statin unchanged until LDL-C exceeds 100 mg/dL','Replace the statin with fibrate monotherapy','Replace the statin with omega-3 monotherapy',
 ['The specified 2025 ACS guideline recommends intensification at LDL-C at least 70 mg/dL on maximal tolerated statin.','A fibrate is not an equivalent LDL-driven secondary-prevention strategy.','Omega-3 therapy does not replace indicated LDL lowering.']),
('Clinical follow-up without routine periodic ischemia testing','Annual stress imaging regardless of clinical stability','Annual coronary CT angiography regardless of symptoms','Scheduled invasive angiography to check for progression',
 ['Routine testing without a change in status has not established benefit in this setting.','Routine anatomical surveillance can trigger unnecessary downstream procedures.','Invasive surveillance is not indicated simply because time has elapsed.']),
('Structured cardiac rehabilitation','Unsupervised activity restriction for six months','Symptom-driven exercise advice without a rehabilitation referral','Routine surveillance angiography before starting exercise',
 ['Prolonged unnecessary restriction promotes deconditioning.','Advice alone does not provide the structured exercise, risk-factor and psychosocial components.','Routine angiography is not a prerequisite after an uncomplicated appropriately assessed MI.']),
('Proton-pump inhibitor','H2-receptor blocker as equivalent protection in every high-risk patient','Sucralfate as the preferred antiplatelet gastroprotection','Antacid treatment taken only when dyspepsia occurs',
 ['H2 blockers do not provide the same recommended high-risk gastroprotection strategy.','Sucralfate is not the guideline-preferred substitute for PPI protection in this context.','Bleeding prevention should not wait for dyspeptic symptoms.'])]

def rebuild():
    source=next((ROOT/'completed/Cardiology').glob('01.*/*/questions.json'))
    bank=json.loads(source.read_text(encoding='utf-8'));rows=copy.deepcopy(bank['questions']);assert len(rows)==len(SETS)==44
    # Explicit current-reference contexts replace outdated unqualified terminology.
    rows[9]['question']='During major gastrointestinal bleeding, hemoglobin is 5.6 g/dL. Ischemic chest pain, new ST depression and a dynamic troponin rise occur with sustained tachycardia. No acute coronary thrombus is identified. Under the 2026 Fifth Universal Definition, which classification best fits?'
    rows[28]['question']='In the 2026 Fifth Universal Definition of MI, what does the updated term MINOCA denote?'
    rows[33]['question']='An intermediate stable coronary lesion is assessed during adequate hyperemia. Mean distal coronary pressure is 80 mm Hg and mean aortic pressure is 100 mm Hg, with no significant pressure-wire drift. Which result and interpretation are correct?'
    rows[33]['questionStyle']='calculation'
    latest=ref('Fifth Universal Definition of Myocardial Infarction 2026','https://doi.org/10.1016/j.jacc.2026.07.025')
    targets=list(range(4))*11;random.Random(202611069).shuffle(targets)
    for n,(q,record,pos) in enumerate(zip(rows,SETS,targets),1):
        answer,*rest=record;wrong=rest[:3];reasons=rest[3]
        q['options']=[answer,*wrong];q['correctIndex']=0
        d=q['explanationTeaching'];d['otherOptions']=[dict(optionIndex=i+1,explanation=r) for i,r in enumerate(reasons)]
        q['options'][0],q['options'][pos]=q['options'][pos],q['options'][0];q['correctIndex']=pos
        for a in d['otherOptions']:
            if a['optionIndex']==pos:a['optionIndex']=0
        q.update(qualityRevision='master-instructions-v2',sourceCheckedAt='2026-11-06',reviewStatus='author_rebuilt_source_checked',id=f'cardiology-cad-acs-{n:03}')
    for n in [9,10,29]:rows[n-1]['references']=[latest]
    rows[8]['explanationTeaching']['sections'][0]['bullets'][0]['children'].append('The 2026 definition retains the injury-plus-ischemia requirement and emphasizes appropriate sex-specific assay reference limits.')
    d=rows[9]['explanationTeaching'];d['title']='Secondary myocardial infarction from supply–demand imbalance'
    d['sections'][0]['bullets']=[dict(text='**Secondary MI** is the 2026 category for ischemic injury arising from a mechanism other than acute primary coronary atherothrombosis.',children=['Profound anemia lowers oxygen delivery; tachycardia raises demand.','Ischemic pain and new ST depression establish ischemia in addition to acute injury.'])]
    d['sections'][1]['bullets']=[dict(text='**Correct the precipitating physiological disturbance** while assessing whether coronary evaluation is needed.',children=['Control bleeding and manage severe anemia and hemodynamics.','The older term type 2 MI should be identified as legacy terminology when used.'])]
    d['tables']=[dict(title='Mechanism distinction',headers=['Category','Defining feature'],rows=[['Primary MI','Acute atherothrombotic mechanism'],['Secondary MI','Other ischemic supply–demand mechanism'],['Nonischemic injury','Injury without ischemic evidence']])]
    d=rows[28]['explanationTeaching'];d['title']='Updated MINOCA terminology in 2026'
    d['sections'][0]['bullets']=[dict(text='The 2026 definition expands MINOCA to **myocardial injury with nonobstructive coronary arteries**.',children=['It is an umbrella requiring identification of the underlying mechanism.','This differs from the earlier infarction-only expansion of the acronym.'])]
    d['sections'][1]['bullets']=[dict(text='**Do not infer the final etiology from angiography alone.**',children=['CMR can distinguish ischemic injury from myocarditis and Takotsubo patterns.','Selected intracoronary imaging or coronary-function assessment depends on the presentation.'])]
    d['tables']=[dict(title='Terminology',headers=['Context','Meaning'],rows=[['2026 UDMI','Myocardial injury with nonobstructive coronary arteries'],['Earlier usage','Myocardial infarction with nonobstructive coronary arteries']])]
    d=rows[33]['explanationTeaching'];d['sections'][0]['bullets'][0]['children']=['FFR = hyperemic distal pressure / aortic pressure = 80 / 100 = **0.80**.','The usual threshold is **0.80 or less**, interpreted with technical quality, symptoms and anatomy.']
    # Diagnosis precedes treatment, then complications and chronic coronary disease.
    order=[9,10,11,12,13,14,1,2,3,4,5,6,15,16,17,19,7,18,20,21,*range(22,36),8,*range(36,45)]
    assert len(order)==len(set(order))==44
    rows=[rows[i-1] for i in order]
    dest=ROOT/'recreated-v2/Cardiology/01. CAD and ACS';dest.mkdir(parents=True,exist_ok=True)
    refs={}
    for q in rows:
        for r in q['references']:refs[r['url']]=r['label']
        parts=[f'<p><strong>Correct Answer: {chr(65+q["correctIndex"])} — {escape(q["options"][q["correctIndex"]])}</strong></p>']
        def rich(t):return re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',escape(t))
        for sec in q['explanationTeaching']['sections']:
            parts.append('<ul>')
            for b in sec['bullets']:parts.append('<li>'+rich(b['text'])+'<ul>'+''.join('<li>'+rich(t)+'</li>' for t in b['children'])+'</ul></li>')
            parts.append('</ul>')
        # Tables are selected for genuinely comparative objectives.
        if int(q['id'][-3:]) in {2,3,6,8,9,10,16,18,22,23,24,25,28,29,30,33,34,35,36,37,40}:
            for t in q['explanationTeaching']['tables']:
                parts.append('<table><thead><tr>'+''.join('<th>'+rich(x)+'</th>' for x in t['headers'])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+rich(x)+'</td>' for x in row)+'</tr>' for row in t['rows'])+'</tbody></table>')
        parts.append('<h3>Other Options</h3><ul>')
        for a in sorted(q['explanationTeaching']['otherOptions'],key=lambda a:a['optionIndex']):parts.append('<li><strong>'+chr(65+a['optionIndex'])+' — '+escape(q['options'][a['optionIndex']])+':</strong> '+escape(a['explanation'])+'</li>')
        parts.append('</ul>');q['explanationHtml']=''.join(parts)
        q['explanation']=re.sub('<[^>]+>',' ',q['explanationHtml'])
        assert len(set(q['options']))==4 and len(q['explanationTeaching']['otherOptions'])==3
        assert {a['optionIndex'] for a in q['explanationTeaching']['otherOptions']}==set(range(4))-{q['correctIndex']}
    bank.update(questions=rows,qualityRevision='master-instructions-v2',chapterReferences=[dict(label=v,url=k) for k,v in refs.items()],
      referenceLimit='Harrison text was not supplied; no invented edition, chapter or page citations. Current primary guidelines and trial references are provided.')
    css='body{max-width:960px;margin:28px auto;padding:0 24px;color:#222;font:17px/1.45 Georgia}article{padding:24px 0;border-bottom:1px solid #ddd}h2{font:700 20px/1.3 Arial}ol.options{font:16px/1.4 Arial}table{border-collapse:collapse;width:100%;margin:16px 0}td,th{border:1px solid #ccc;padding:8px;text-align:left}th{background:#edf1f7}li{margin:5px 0}'
    html=['<!doctype html><meta charset="utf-8"><title>CAD and ACS revised chapter</title><style>'+css+'</style><h1>Coronary artery disease and acute coronary syndromes</h1><p>44 postgraduate single-best-answer questions. Complete chapter revision.</p>']
    for i,q in enumerate(rows,1):html.append('<article><h2>'+str(i)+'. '+escape(q['question'])+'</h2><ol type="A" class="options">'+''.join('<li>'+escape(x)+'</li>' for x in q['options'])+'</ol>'+q['explanationHtml']+'</article>')
    html.append('<h2>Chapter references</h2><ol>'+''.join('<li>'+escape(v)+' — <a href="'+escape(k)+'">'+escape(k)+'</a></li>' for k,v in refs.items())+'</ol>')
    (dest/'Complete Chapter.html').write_text(''.join(html),encoding='utf-8')
    # The app supplies the answer banner itself. Plain exports and the complete
    # chapter above retain the requested opening without duplicating it onscreen.
    for q in rows:q['explanationHtml']=re.sub(r'^<p><strong>Correct Answer:.*?</strong></p>','',q['explanationHtml'],count=1)
    (dest/'questions.json').write_text(json.dumps(bank,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(dict(chapter='CAD and ACS',questions=len(rows),answerDistribution={chr(65+i):sum(q['correctIndex']==i for q in rows) for i in range(4)},output=str(dest)),indent=2))

if __name__=='__main__':rebuild()
