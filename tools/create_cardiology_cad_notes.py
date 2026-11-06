"""Concise, clinically grouped CAD/ACS notes for the first Cardiology module."""
from create_qbank_topic_notes import page,DEST
BODY='''<nav><strong>Contents</strong> · <a href="#diagnosis">Diagnosis</a> · <a href="#reperfusion">Reperfusion</a> · <a href="#antithrombotics">Antithrombotics</a> · <a href="#drugs">Other drugs</a> · <a href="#complications">Complications</a> · <a href="#chronic">Chronic CAD</a> · <a href="#nonobstructive">Nonobstructive coronaries</a> · <a href="#references">References</a></nav>

<section id="diagnosis"><h2>1 · Diagnosis: ACS and myocardial injury</h2>
<table><thead><tr><th>Diagnosis</th><th>Required distinction</th></tr></thead><tbody>
<tr><td>Myocardial injury</td><td>Troponin above the assay’s 99th percentile. Rise/fall = acute injury; persistent stable elevation = chronic injury.</td></tr>
<tr><td>Myocardial infarction</td><td><strong>Acute injury + evidence of ischemia:</strong> symptoms, ischemic ECG changes, new ischemic wall-motion abnormality/loss of viable myocardium, or coronary thrombus.</td></tr>
<tr><td>Type 1 MI</td><td>Acute atherothrombosis from plaque rupture or erosion.</td></tr>
<tr><td>Type 2 MI</td><td>Oxygen supply–demand mismatch without acute atherothrombosis; ischemia must still be demonstrated.</td></tr>
<tr><td>NSTEMI</td><td>Acute MI without persistent diagnostic ST elevation.</td></tr>
<tr><td>Unstable angina</td><td>Acute ischemia without acute troponin-defined injury.</td></tr>
</tbody></table>
<ul><li><strong>CKD:</strong> elevated troponin alone does not establish NSTEMI. Use serial change and ischemic evidence.</li>
<li><strong>Sepsis:</strong> troponin rise without ischemic evidence is acute myocardial injury, not automatically type 2 MI.</li>
<li><strong>ECG:</strong> obtain promptly and repeat during recurrent symptoms. A nondiagnostic first ECG does not exclude ACS.</li>
<li><strong>Diffuse ST depression + aVR elevation:</strong> widespread subendocardial ischemia; not specific for left-main occlusion.</li>
<li><strong>Inferior MI:</strong> record right-sided leads when RV infarction is suspected. V4R elevation supports RV involvement.</li></ul><p><a href="#r1">[1]</a> <a href="#r2">[2]</a></p></section>

<section id="reperfusion"><h2>2 · Reperfusion and invasive treatment</h2>
<h3>STEMI</h3><table><thead><tr><th>Situation</th><th>Strategy</th></tr></thead><tbody>
<tr><td>Timely primary PCI available</td><td><strong>Primary PCI.</strong> ESC threshold: anticipated diagnosis-to-wire crossing ≤120 minutes.</td></tr>
<tr><td>PCI delay &gt;120 minutes; symptoms &lt;12 hours; no fibrinolysis contraindication</td><td>Immediate fibrinolysis followed by transfer to a PCI centre.</td></tr>
<tr><td>Failed fibrinolysis</td><td><strong>Rescue PCI:</strong> &lt;50% ST resolution at 60–90 minutes, persistent/worsening ischemia, or hemodynamic/electrical instability.</td></tr>
<tr><td>Successful fibrinolysis</td><td>Routine angiography/PCI within <strong>2–24 hours</strong>; do not discharge after apparent reperfusion.</td></tr>
<tr><td>Fibrinolysis contraindicated</td><td>Transfer for PCI; a long transfer time does not make contraindicated fibrinolysis acceptable.</td></tr>
</tbody></table>
<p><strong>Major fibrinolysis contraindications:</strong> previous intracranial hemorrhage, active major bleeding, suspected aortic dissection, and specified recent stroke or major intracranial injury/surgery. Screen the complete contraindication list.</p>
<h3>NSTE-ACS</h3><ul><li><strong>Immediate angiography:</strong> shock, refractory/recurrent ischemia, life-threatening arrhythmia, mechanical complication, or acute heart failure from ongoing ischemia.</li>
<li><strong>Stable high-risk disease:</strong> inpatient invasive treatment; ESC recommends considering angiography within 24 hours, especially with GRACE &gt;140 or other high-risk features.</li>
<li><strong>No fibrinolysis for NSTEMI or unstable angina.</strong></li></ul>
<h3>PCI: procedural choices</h3><ul><li><strong>Radial access:</strong> preferred when feasible; reduces bleeding and vascular complications.</li><li><strong>IVUS/OCT:</strong> intracoronary imaging guides PCI in complex lesions.</li><li><strong>Cardiogenic shock:</strong> emergency culprit-vessel revascularization. Do not routinely perform immediate PCI of all nonculprit lesions.</li></ul><p><a href="#r2">[2]</a> <a href="#r3">[3]</a></p></section>

<section id="antithrombotics"><h2>3 · Antithrombotic treatment</h2>
<h3>Antiplatelets: compare the P2Y₁₂ inhibitors together</h3>
<table><thead><tr><th>Drug</th><th>Main role / distinction</th><th>Important restriction</th></tr></thead><tbody>
<tr><td>Ticagrelor</td><td>Potent, reversible P2Y₁₂ inhibitor; preferred over clopidogrel in appropriate ACS PCI patients.</td><td>Bleeding; dyspnea; bradyarrhythmia risk. Avoid with prior intracranial hemorrhage.</td></tr>
<tr><td>Prasugrel</td><td>Potent, irreversible P2Y₁₂ inhibitor; ACS treated with PCI.</td><td><strong>Contraindicated after stroke/TIA.</strong> Additional caution with age ≥75 or weight &lt;60 kg.</td></tr>
<tr><td>Clopidogrel</td><td>Less potent; usual P2Y₁₂ agent with fibrinolysis or concurrent long-term oral anticoagulation.</td><td>Variable activation and response; drug/genetic factors can reduce effect.</td></tr>
</tbody></table>
<ul><li><strong>DAPT:</strong> aspirin + a P2Y₁₂ inhibitor. Default after ACS: <strong>12 months or longer under the 2025 US default recommendation</strong> when bleeding risk is not high; shorter or modified regimens are selected for bleeding risk.</li>
<li><strong>NSTE-ACS pretreatment:</strong> do not routinely load before anatomy is known when early angiography is planned. The 2025 US guideline permits selected upstream clopidogrel/ticagrelor when angiography will be delayed &gt;24 hours.</li>
<li><strong>AF + ACS PCI:</strong> minimize triple therapy. The 2025 US guideline recommends stopping aspirin at 1–4 weeks, continuing oral anticoagulation + a P2Y₁₂ inhibitor, preferably clopidogrel. ESC commonly uses a shorter default triple-therapy period, adjusted for ischemic risk.</li>
<li><strong>Anticoagulation:</strong> use an ACS/procedure-specific regimen. It does not replace antiplatelet treatment after coronary stenting.</li>
<li><strong>Bleeding prevention:</strong> radial access, renal/weight-adjusted dosing, and a proton-pump inhibitor when gastrointestinal bleeding risk is increased.</li></ul><p><a href="#r2">[2]</a> <a href="#r3">[3]</a></p></section>

<section id="drugs"><h2>4 · Other drugs: purpose and exclusions</h2>
<table><thead><tr><th>Treatment</th><th>Use</th><th>Key exclusion / limitation</th></tr></thead><tbody>
<tr><td>Nitrates</td><td>Relieve ischemic pain; useful with hypertension or pulmonary congestion.</td><td><strong>Avoid in hypotension, preload-dependent RV infarction, or recent PDE5-inhibitor use.</strong> No established mortality benefit.</td></tr>
<tr><td>Beta blockers</td><td>Reduce heart rate and ischemia; particularly relevant with LV dysfunction or another continuing indication.</td><td>Avoid initiation in shock, acute decompensated heart failure or important bradycardia/AV block.</td></tr>
<tr><td>High-intensity statin</td><td>Early secondary prevention after ACS.</td><td>Add nonstatin treatment if LDL remains above the applicable guideline threshold despite maximal tolerated statin.</td></tr>
<tr><td>ACE inhibitor/ARB</td><td>Particularly important after MI with LV dysfunction, heart failure or other indicated high-risk conditions.</td><td>Monitor renal function and potassium.</td></tr>
<tr><td>Mineralocorticoid antagonist</td><td>Selected post-MI patients with LVEF ≤40% and heart failure or diabetes.</td><td>Requires acceptable kidney function and potassium.</td></tr>
<tr><td>Oxygen</td><td>Hypoxemia.</td><td>Not routine when oxygen saturation is normal.</td></tr>
</tbody></table>
<p><strong>Lipids:</strong> ESC very-high-risk goal: LDL &lt;55 mg/dL and ≥50% reduction. US 2025 ACS guidance: add nonstatin at LDL ≥70 mg/dL; addition is also reasonable at 55–69 mg/dL. Ezetimibe and PCSK9-directed therapy are important options.</p>
<p><strong>After discharge:</strong> smoking cessation, cardiac rehabilitation, exercise, BP/diabetes control and treatment adherence. <a href="#r2">[2]</a> <a href="#r4">[4]</a></p></section>

<section id="complications"><h2>5 · MI complications: recognize the pattern</h2>
<table><thead><tr><th>Complication</th><th>Clue</th><th>Key point</th></tr></thead><tbody>
<tr><td>RV infarction</td><td>Inferior MI + hypotension + raised JVP + clear lungs; V4R elevation.</td><td>Urgent reperfusion; avoid preload-reducing drugs. Cautious fluid assessment rather than indiscriminate large boluses.</td></tr>
<tr><td>AV block in inferior MI</td><td>Often AV-nodal block with narrow escape rhythm; commonly RCA involvement.</td><td>May be transient; pacing depends on symptoms and hemodynamic compromise.</td></tr>
<tr><td>Papillary muscle rupture</td><td>Acute pulmonary edema/shock; acute MR, often after inferior MI.</td><td>Posteromedial muscle is vulnerable because of its single arterial supply. Urgent echo and surgical assessment.</td></tr>
<tr><td>Ventricular septal rupture</td><td>New harsh pansystolic murmur at the lower left sternal border, often a thrill; shock.</td><td>Urgent echo and structural/surgical management.</td></tr>
<tr><td>Free-wall rupture</td><td>Sudden collapse/PEA + new pericardial effusion/tamponade.</td><td>Emergency intervention.</td></tr>
<tr><td>True LV aneurysm</td><td>Scarred dyskinetic wall, usually broad neck; persistent ST elevation may occur.</td><td>HF, arrhythmia and thrombus risk; less prone to rupture than pseudoaneurysm.</td></tr>
<tr><td>LV pseudoaneurysm</td><td>Contained rupture; often narrow neck.</td><td>High rupture risk; urgent specialist assessment. Neck shape alone is not definitive.</td></tr>
<tr><td>LV thrombus</td><td>Large anterior/apical MI, severe regional dysfunction.</td><td>Anticoagulation typically about 3 months after MI, with repeat imaging; minimize combined antithrombotic bleeding risk.</td></tr>
<tr><td>Early post-MI pericarditis</td><td>Pleuritic/positional pain, rub; possible diffuse ST changes.</td><td>Differentiate from recurrent ischemia; treatment commonly uses aspirin-based anti-inflammatory therapy.</td></tr>
</tbody></table><p><strong>Timing trap:</strong> rupture often occurs within the first week but is not confined to a fixed day. A murmur may be faint in severe shock. <a href="#r3">[3]</a> <a href="#r5">[5]</a></p></section>

<section id="chronic"><h2>6 · Chronic coronary disease</h2>
<h3>Testing and revascularization</h3><ul><li><strong>Initial testing:</strong> estimate clinical likelihood; choose coronary CT angiography or functional imaging according to likelihood, patient factors and the diagnostic question.</li>
<li><strong>Intermediate stenosis:</strong> coronary physiology can establish significance; standard thresholds are FFR ≤0.80 or iFR ≤0.89.</li>
<li><strong>Revascularization:</strong> persistent limiting angina despite treatment or prognostically important anatomy. CABG is favored in suitable patients with complex left-main/multivessel disease, especially diabetes.</li>
<li><strong>Stable CAD:</strong> inducible ischemia alone does not mean routine PCI improves survival in every patient.</li></ul>
<h3>Antianginal treatment by mechanism</h3><table><thead><tr><th>Pattern</th><th>Treatment emphasis</th></tr></thead><tbody>
<tr><td>Obstructive exertional angina</td><td>Beta blocker or calcium-channel blocker as appropriate; add agents according to heart rate, BP, LV function and symptoms.</td></tr>
<tr><td>Epicardial vasospasm</td><td><strong>Calcium-channel blocker</strong>; nitrates as needed. Avoid beta-blocker monotherapy, especially nonselective agents.</td></tr>
<tr><td>Microvascular dysfunction without spasm</td><td>Risk-factor treatment and mechanism-directed antianginal therapy; beta blockers may help selected patients.</td></tr>
</tbody></table><p><a href="#r4">[4]</a></p></section>

<section id="nonobstructive"><h2>7 · ACS or ischemia with nonobstructive coronaries</h2>
<table><thead><tr><th>Condition</th><th>Key distinction</th><th>Next step / treatment principle</th></tr></thead><tbody>
<tr><td>MINOCA</td><td>MI criteria + no coronary stenosis ≥50%; a working diagnosis.</td><td>Identify the cause. Cardiac MRI helps distinguish infarction, myocarditis and Takotsubo; intracoronary imaging/testing may reveal plaque injury or spasm.</td></tr>
<tr><td>INOCA</td><td>Ischemia with nonobstructive coronary arteries; not necessarily infarction.</td><td>Assess microvascular dysfunction and vasospasm; treat the identified mechanism.</td></tr>
<tr><td>Takotsubo syndrome</td><td>Transient ventricular dysfunction often extending beyond one coronary territory; possible emotional/physical trigger.</td><td>Initially assess as ACS; define ventricular pattern and complications. A trigger is not mandatory.</td></tr>
<tr><td>SCAD</td><td>Coronary dissection/intramural hematoma; consider in young or postpartum patients.</td><td>Usually conservative when stable, distal flow maintained and no ongoing ischemia. High-risk anatomy or instability can require revascularization.</td></tr>
</tbody></table><p><strong>Do not give every MINOCA patient an identical atherothrombotic regimen:</strong> plaque disruption, spasm, dissection and embolism have different treatment requirements. <a href="#r3">[3]</a> <a href="#r4">[4]</a> <a href="#r6">[6]</a></p></section>

<section id="references"><h2>References</h2><ol>
<li><a href="https://doi.org/10.1161/CIR.0000000000000617">Fourth Universal Definition of Myocardial Infarction. 2018.</a></li>
<li><a href="https://doi.org/10.1016/j.jacc.2024.11.009">ACC/AHA/ACEP/NAEMSP/SCAI Guideline for Acute Coronary Syndromes. 2025.</a></li>
<li><a href="https://academic.oup.com/eurheartj/article/44/38/3720/7243210">ESC Guidelines for Acute Coronary Syndromes. 2023.</a></li>
<li><a href="https://doi.org/10.1093/eurheartj/ehae177">ESC Guidelines for Chronic Coronary Syndromes. 2024.</a></li>
<li><a href="https://doi.org/10.1161/CIR.0000000000001092">AHA Scientific Statement: Management of Patients at Risk for and With LV Thrombus. 2022.</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/5957087/">AHA Scientific Statement: Spontaneous Coronary Artery Dissection. 2018.</a></li>
</ol></section>'''

def make():
    from lxml import html
    # Give references stable anchors without changing their numbered list.
    root=html.fragment_fromstring(BODY,create_parent='div')
    for i,node in enumerate(root.xpath('.//section[@id="references"]/ol/li'),1):node.set('id',f'r{i}')
    body=''.join(html.tostring(n,encoding='unicode') for n in root)
    ids=set(root.xpath('.//*[@id]/@id'));assert all(h[1:] in ids for h in root.xpath('.//a[starts-with(@href,"#")]/@href'))
    dest=DEST/'Cardiology/CAD and ACS.html';dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(page('CAD and acute coronary syndromes',body),encoding='utf-8');print(dest)
if __name__=='__main__':make()
