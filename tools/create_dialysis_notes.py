"""Author one complete Dialysis and RRT Pearls module without changing its Qbank."""
import json
from lxml import html
from create_qbank_topic_notes import DEST,page

BODY=r'''<nav><strong>Contents</strong><br>
<a href="#timing">Indications and planning</a> · <a href="#modality">Modality</a> · <a href="#transport">Solute and fluid removal</a> · <a href="#dose">CRRT dose</a> · <a href="#adequacy">HD adequacy</a> · <a href="#volume">Ultrafiltration and hypotension</a> · <a href="#emergencies">HD emergencies</a> · <a href="#access">Vascular access</a> · <a href="#citrate">Citrate anticoagulation</a> · <a href="#pd">PD transport</a> · <a href="#peritonitis">PD peritonitis</a> · <a href="#toxins">Dialyzable poisons</a> · <a href="#recovery">Stopping RRT</a> · <a href="#calciphylaxis">Calciphylaxis</a> · <a href="#pitfalls">Pitfalls</a></nav>

<section id="timing"><h2>1 · Dialysis indications and planning</h2>
<p>Start dialysis for complications that cannot be controlled adequately with medical treatment. Assess symptoms, examination, laboratory trends, urine output and fluid balance together.</p>
<table><thead><tr><th>Finding</th><th>Decision</th></tr></thead><tbody>
<tr><td><strong>Persistent dangerous hyperkalemia</strong>, especially ECG changes</td><td>Urgent dialysis when medical treatment is insufficient. Continue calcium for ECG toxicity and potassium-shifting treatment while arranging dialysis.</td></tr>
<tr><td><strong>Refractory pulmonary edema or fluid overload</strong></td><td>Dialysis/ultrafiltration when respiratory or circulatory compromise cannot be controlled medically.</td></tr>
<tr><td><strong>Severe persistent metabolic acidosis</strong></td><td>Assess the cause, response to treatment and clinical severity; no single pH threshold fits every setting.</td></tr>
<tr><td><strong>Uremic pericarditis or encephalopathy</strong></td><td>Supports starting dialysis promptly. A relatively stable creatinine does not make these complications safe to observe.</td></tr>
<tr><td>Selected severe poisoning</td><td>Use toxin-specific indications; the serum creatinine alone does not determine the need.</td></tr>
<tr><td>Progressive CKD with uncontrolled symptoms, malnutrition or volume/BP problems</td><td>Individualize initiation with the patient, after assessing reversible causes and goals of care.</td></tr>
</tbody></table>
<p><strong>Stable CKD G5 with eGFR 8, preserved appetite, controlled volume, potassium and bicarbonate:</strong> continued close monitoring and preparation may be appropriate. Low eGFR alone does not mandate immediate dialysis.</p>
<p><strong>Plan access or preemptive transplantation when eGFR is below about 15–20 mL/min/1.73 m² or the 2-year kidney replacement risk exceeds 40%.</strong> Planning and starting treatment are different decisions.</p>
<p>Similarly, stage 3 AKI without a dialysis indication can be monitored closely. Reassess frequently; this is active surveillance, with dialysis started if complications develop.</p></section>

<section id="modality"><h2>2 · Choosing the modality</h2>
<table><thead><tr><th>Modality</th><th>Useful setting</th><th>Main limitation</th></tr></thead><tbody>
<tr><td><strong>Intermittent hemodialysis (IHD)</strong></td><td>Rapid correction of potassium, acidosis and small-solute accumulation; preferred for many dialyzable poisons.</td><td>Rapid fluid and osmotic changes may be poorly tolerated in severe shock or intracranial hypertension.</td></tr>
<tr><td><strong>Continuous renal replacement therapy (CRRT)</strong></td><td>Gradual fluid/solute control in hemodynamic instability; favored with acute brain injury and raised intracranial pressure.</td><td>Needs prolonged circuit access, monitoring and attention to interruptions, anticoagulation and electrolyte losses.</td></tr>
<tr><td><strong>SLED / prolonged intermittent therapy</strong></td><td>Slower treatment over an extended session; an alternative where expertise and resources permit.</td><td>Still intermittent; tolerance depends on the prescription and patient.</td></tr>
<tr><td><strong>Peritoneal dialysis (PD)</strong></td><td>Home-based maintenance therapy; also used in selected AKI settings.</td><td>Peritoneal transport, abdominal suitability, infection risk and achievable clearance/ultrafiltration matter.</td></tr>
</tbody></table>
<p>Septic shock requiring substantial vasopressor support generally favors CRRT when available. With cerebral edema, slower solute change also reduces the risk of worsening intracranial pressure.</p>
<p><strong>No consistent mortality advantage of CRRT over IHD has been established across all AKI patients.</strong> Select a modality for the physiological problem; reassess as stability changes.</p></section>

<section id="transport"><h2>3 · Solute clearance and fluid removal</h2>
<table><thead><tr><th>Mechanism</th><th>What happens</th><th>Examples</th></tr></thead><tbody>
<tr><td><strong>Diffusion</strong></td><td>Solute moves down its concentration gradient across a membrane.</td><td>Predominant mechanism for urea and potassium removal in conventional HD; <strong>CVVHD</strong>.</td></tr>
<tr><td><strong>Convection</strong></td><td>Dissolved solute is carried with water filtered across the membrane.</td><td><strong>CVVH</strong>; replacement fluid is needed because the filtered volume exceeds the desired net fluid loss.</td></tr>
<tr><td>Diffusion + convection</td><td>Both mechanisms contribute.</td><td><strong>CVVHDF</strong>.</td></tr>
<tr><td><strong>Ultrafiltration</strong></td><td>Water is removed across the membrane under a pressure gradient; PD uses an osmotic gradient.</td><td>Net fluid removal is prescribed separately from solute clearance.</td></tr>
</tbody></table>
<p><strong>Isolated ultrafiltration is not an adequate substitute for HD in hyperkalemia.</strong> It removes plasma water, with some convective solute removal, but little diffusive potassium clearance. A patient with missed HD, pulmonary edema and dangerous hyperkalemia needs a treatment addressing both problems.</p></section>

<section id="dose"><h2>4 · CRRT dose and interruptions</h2>
<p>For small solutes, effluent flow provides an approximate measure of CRRT clearance. It does not equal the net volume being removed from the patient.</p>
<table><thead><tr><th>Measure</th><th>Calculation / interpretation</th></tr></thead><tbody>
<tr><td><strong>Nominal effluent dose</strong></td><td><strong>Total effluent (mL/h) ÷ body weight (kg)</strong>, expressed as mL/kg/h.</td></tr>
<tr><td><strong>Average delivered dose over a day</strong></td><td><strong>Running dose × actual treatment hours ÷ 24</strong>, before any predilution correction.</td></tr>
<tr><td>Usual delivered target in AKI</td><td><strong>20–25 mL/kg/h.</strong> Often prescribe approximately 25–30 to allow for interruptions; check actual delivery.</td></tr>
<tr><td>Predilution replacement</td><td>Dilutes blood entering the filter. The same nominal effluent flow gives <strong>less effective small-solute clearance</strong> than without substantial predilution.</td></tr>
<tr><td>Downtime</td><td>Filter clotting, procedures, access dysfunction and circuit changes reduce delivered treatment.</td></tr>
</tbody></table>
<h3>Worked calculations</h3>
<ul><li><strong>Effluent 2,000 mL/h, weight 80 kg:</strong> 2,000 ÷ 80 = <strong>25 mL/kg/h</strong>.</li>
<li><strong>Effluent 2,400 mL/h, weight 80 kg:</strong> running dose = 30 mL/kg/h. If treatment runs for 18 hours, daily average = 30 × 18/24 = <strong>22.5 mL/kg/h</strong>.</li>
<li><strong>The same prescription running for 12 hours:</strong> daily average = <strong>15 mL/kg/h</strong>. A satisfactory setting on the machine does not prove an adequate daily dose.</li></ul>
<p>Higher routine CRRT intensity has not improved survival compared with standard dosing. Follow potassium, acid–base status, phosphate, fluid balance and drug clearance as well as the effluent number. Marked ongoing solute production or poisoning may need a different prescription.</p></section>

<section id="adequacy"><h2>5 · Hemodialysis adequacy</h2>
<table><thead><tr><th>Measure</th><th>Formula / target</th><th>Important limitation</th></tr></thead><tbody>
<tr><td><strong>Urea reduction ratio (URR)</strong></td><td><strong>100 × (pre-HD urea − post-HD urea) ÷ pre-HD urea</strong></td><td>Use comparable units and correctly timed samples. Does not account fully for rebound or residual kidney function.</td></tr>
<tr><td><strong>Simple Kt/V</strong></td><td><strong>K × t ÷ V</strong>; K = effective urea clearance, t = treatment time, V = urea distribution volume.</td><td>This is a teaching approximation. Clinical single-pool Kt/V uses formal urea kinetic calculations.</td></tr>
<tr><td><strong>Thrice-weekly maintenance HD</strong></td><td>Target <strong>single-pool Kt/V 1.4 per session</strong>; minimum delivered <strong>1.2</strong>.</td><td>Residual kidney function and other treatment schedules require appropriate assessment. Single-pool and equilibrated Kt/V are different measures.</td></tr>
</tbody></table>
<h3>Worked calculations</h3>
<ul><li><strong>Pre-HD urea 100, post-HD urea 30:</strong> URR = 100 × 70/100 = <strong>70%</strong>.</li>
<li><strong>K 200 mL/min, t 240 min, V 40 L:</strong> convert V to 40,000 mL; Kt/V = 200 × 240/40,000 = <strong>1.2</strong>.</li></ul>
<p>Low delivered clearance should prompt review of treatment duration, missed sessions, blood flow, access function, dialyzer performance and sampling. Access recirculation can make a blood sample misleading.</p>
<p><strong>Adequate urea clearance does not establish adequate volume, potassium, nutritional or symptom control.</strong> Review the patient as well as the clearance measure.</p></section>

<section id="volume"><h2>6 · Ultrafiltration and intradialytic hypotension</h2>
<p><strong>Ultrafiltration rate = planned fluid removal (mL) ÷ treatment duration (h) ÷ body weight (kg).</strong></p>
<p><strong>Remove 3.5 L over 4 hours in a 70-kg patient:</strong> 3,500 ÷ 4 ÷ 70 = <strong>12.5 mL/kg/h</strong>. This is a calculation, not proof that the rate is tolerable.</p>
<table><thead><tr><th>Problem</th><th>Response</th></tr></thead><tbody>
<tr><td><strong>Cramps, nausea and BP 80/50 during fluid removal</strong></td><td><strong>Pause ultrafiltration</strong>, assess circulation and treat hypotension; use positioning and an appropriate fluid bolus when indicated.</td></tr>
<tr><td>Repeated episodes</td><td>Review target weight, interdialytic gain, treatment time, cardiac disease, infection, medicines and the dialysis prescription.</td></tr>
<tr><td>High fluid removal requirement</td><td>Consider longer or additional treatments and address sodium/fluid intake. Do not force the entire volume through a poorly tolerated short session.</td></tr>
<tr><td>CRRT fluid prescription</td><td>Separate <strong>machine net fluid removal</strong> from overall patient balance, which also includes infusions, nutrition, urine and other losses.</td></tr>
</tbody></table>
<p>Not every intradialytic BP fall is due to excessive ultrafiltration. Consider bleeding, sepsis, arrhythmia, myocardial ischemia and circuit-related emergencies when the pattern is atypical.</p></section>

<section id="emergencies"><h2>7 · Hemodialysis emergencies</h2>
<table><thead><tr><th>Pattern</th><th>Likely problem</th><th>Immediate priority</th></tr></thead><tbody>
<tr><td>First aggressive HD at very high urea; headache, restlessness, seizures</td><td><strong>Dialysis disequilibrium:</strong> plasma urea falls faster than brain urea, promoting cerebral water entry.</td><td>Stop/reduce treatment as clinically indicated, stabilize the patient and evaluate neurological deterioration urgently. Prevent with a gentler initial prescription.</td></tr>
<tr><td>Sudden dyspnea, chest/back pain, dark circuit blood and falling hemoglobin</td><td><strong>Hemolysis</strong>; consider mechanical obstruction, overheated/hypotonic dialysate or contamination.</td><td><strong>Stop dialysis/blood pump and do not return circuit blood.</strong> Escalate urgently, monitor ECG and potassium, and investigate the circuit/water system.</td></tr>
<tr><td>Acute dyspnea, hypoxemia or neurological deterioration with suspected air entry</td><td>Air embolism</td><td>Stop the pump, clamp/disconnect the unsafe circuit according to protocol, give emergency support and oxygen, and obtain urgent expert help.</td></tr>
<tr><td>Immediate severe wheeze, flushing, angioedema or shock after starting dialysis</td><td>Severe dialyzer/circuit hypersensitivity</td><td>Stop the exposure and treat anaphylaxis promptly. Follow the specific blood-return protocol for a suspected severe dialyzer reaction.</td></tr>
</tbody></table>
<p><strong>Returning hemolyzed circuit blood can deliver a dangerous potassium load.</strong> Do not apply the usual end-of-treatment blood-return routine to this emergency.</p></section>

<section id="access"><h2>8 · Vascular access and its complications</h2>
<table><thead><tr><th>Access / finding</th><th>Interpretation</th><th>Key point</th></tr></thead><tbody>
<tr><td><strong>Native AV fistula</strong></td><td>Suitable long-term option when vessels and expected treatment course are appropriate.</td><td>Usually lower infection risk than a catheter, but maturation can fail and procedures may be needed.</td></tr>
<tr><td><strong>AV graft</strong></td><td>Useful when fistula anatomy/maturation prospects or timing favor a graft.</td><td>Choose access within an individualized kidney replacement plan; a fistula is not best for every patient.</td></tr>
<tr><td><strong>Urgent temporary dialysis catheter</strong></td><td><strong>Right internal jugular</strong> is generally preferred when feasible.</td><td>Use ultrasound guidance and preserve future access sites. Avoid subclavian access when alternatives are appropriate because of central venous stenosis risk.</td></tr>
<tr><td><strong>High venous pressures + prolonged post-needle bleeding + reduced efficiency</strong></td><td><strong>Outflow venous stenosis</strong></td><td>Needs clinical/access assessment; a functioning thrill alone does not exclude a significant lesion.</td></tr>
<tr><td><strong>Cold painful hand; distal perfusion improves with access compression</strong></td><td><strong>Access-associated steal</strong></td><td>Assess urgently for ischemia and tissue threat; distinguish from neuropathy or isolated venous hypertension.</td></tr>
</tbody></table>
<p>Examine the access and assess flow/adequacy trends. Do not treat a stenosis found only on surveillance imaging as automatically requiring intervention without relevant clinical indicators.</p></section>

<section id="citrate"><h2>9 · Regional citrate anticoagulation</h2>
<p>Citrate lowers ionized calcium within the circuit to inhibit coagulation. Systemic calcium replacement and monitoring are required. Citrate that is metabolized provides an alkali load.</p>
<table><thead><tr><th>Finding</th><th>Citrate accumulation</th><th>Metabolized citrate excess</th></tr></thead><tbody>
<tr><td>Mechanism</td><td>Delivery exceeds the ability to metabolize citrate; calcium–citrate complexes accumulate.</td><td>Citrate is metabolized, but the net alkali load is excessive.</td></tr>
<tr><td>Acid–base pattern</td><td>Often <strong>worsening metabolic acidosis</strong>, in the appropriate clinical setting.</td><td><strong>Metabolic alkalosis</strong>.</td></tr>
<tr><td>Calcium pattern</td><td><strong>Rising total/ionized calcium ratio, falling systemic ionized calcium or increasing calcium infusion requirement.</strong></td><td>Ratio usually remains normal; calcium needs do not show the same accumulation pattern.</td></tr>
<tr><td>Response</td><td>Urgently reassess citrate delivery, clearance, tissue perfusion and calcium replacement; reduce/stop citrate or change anticoagulation as needed.</td><td>Adjust citrate/alkali balance and the prescription rather than assuming accumulation.</td></tr>
</tbody></table>
<p><strong>Total calcium ÷ systemic ionized calcium:</strong> use paired values in the <strong>same units</strong>. A rising ratio toward or above <strong>2.5</strong>, with acidosis and escalating calcium needs, supports accumulation.</p>
<p><strong>Total Ca 2.75 mmol/L, ionized Ca 1.00 mmol/L → ratio 2.75.</strong> The ratio is a warning marker, not a direct citrate measurement. Shock, poor perfusion and impaired citrate metabolism increase concern.</p></section>

<section id="pd"><h2>10 · Peritoneal transport and ultrafiltration</h2>
<table><thead><tr><th>Concept</th><th>Meaning</th></tr></thead><tbody>
<tr><td><strong>Solute clearance</strong></td><td>Solutes diffuse between peritoneal capillary blood and dialysate.</td></tr>
<tr><td><strong>Glucose dialysate</strong></td><td>Creates an osmotic gradient for water removal. As glucose is absorbed, the gradient falls during the dwell.</td></tr>
<tr><td><strong>Peritoneal equilibration test (PET)</strong></td><td>Uses standardized dwell measurements, including the <strong>dialysate-to-plasma creatinine ratio</strong>, to assess small-solute transport.</td></tr>
<tr><td>High peritoneal solute transport</td><td>Rapid solute equilibration, but more rapid loss of the glucose gradient; long glucose dwells can give poor ultrafiltration.</td></tr>
<tr><td><strong>Icodextrin</strong></td><td>A glucose polymer useful for sustained ultrafiltration during the <strong>long dwell</strong>, particularly when glucose-dwell ultrafiltration wanes.</td></tr>
</tbody></table>
<p><strong>Icodextrin glucose-meter pitfall:</strong> maltose metabolites can produce falsely high readings with incompatible meters. Use a glucose-specific, icodextrin-compatible method; an erroneous high value can trigger excess insulin and severe hypoglycemia.</p>
<p>For poor volume control, assess intake, residual urine, adherence, catheter function and the prescription before attributing everything to membrane failure.</p></section>

<section id="peritonitis"><h2>11 · PD peritonitis</h2>
<p>Suspect peritonitis with <strong>cloudy effluent or abdominal pain</strong>. Obtain effluent cell count/differential and cultures, and begin empiric treatment promptly after sampling.</p>
<table><thead><tr><th>Decision</th><th>Rule</th></tr></thead><tbody>
<tr><td><strong>Diagnostic criteria</strong></td><td>Usually at least <strong>2 of 3</strong>: compatible clinical features; effluent WBC <strong>&gt;100/µL after ≥2-hour dwell with &gt;50% neutrophils</strong>; positive effluent culture.</td></tr>
<tr><td>Short automated-PD dwell</td><td>The absolute count may remain below 100/µL. A <strong>neutrophil fraction &gt;50%</strong> with compatible symptoms remains strongly concerning.</td></tr>
<tr><td>Empiric antibiotics</td><td>Cover gram-positive and gram-negative organisms according to local resistance patterns. <strong>Intraperitoneal administration is preferred</strong> when appropriate; systemic sepsis also requires prompt systemic management.</td></tr>
<tr><td><strong>Candida / fungal peritonitis</strong></td><td><strong>Prompt catheter removal plus appropriate antifungal therapy.</strong> Antibiotics alone or observation with the infected catheter retained is inadequate.</td></tr>
<tr><td>Failure to improve</td><td>Reassess effluent trends, cultures, antibiotic delivery, resistant organisms and surgical/secondary causes; consider catheter removal when indicated.</td></tr>
</tbody></table>
<p><strong>WBC 240/µL, 80% neutrophils after a 2-hour dwell + pain/cloudy fluid:</strong> diagnostic criteria are met while culture is pending.</p>
<p><strong>Short dwell, WBC 80/µL, 78% neutrophils + pain/cloudy fluid:</strong> do not dismiss peritonitis because the absolute WBC is below 100.</p></section>

<section id="toxins"><h2>12 · Dialyzable poisons</h2>
<p>Low molecular size, limited protein binding and a small volume of distribution generally favor extracorporeal removal. Poisoning severity, tissue distribution and endogenous clearance remain important.</p>
<table><thead><tr><th>Poison</th><th>When dialysis matters</th><th>Important distinction</th></tr></thead><tbody>
<tr><td><strong>Lithium</strong></td><td>Severe neurological toxicity, seizures, dangerous dysrhythmia or significant accumulation with impaired kidney function.</td><td><strong>IHD is preferred</strong> when feasible. Tissue redistribution or ongoing absorption can cause rebound; monitor serial levels after treatment.</td></tr>
<tr><td><strong>Salicylates</strong></td><td>Altered mental status, new oxygen-requiring hypoxemia/pulmonary edema, failed standard treatment or severe acidemia can justify urgent dialysis.</td><td><strong>IHD is preferred</strong>. Continue appropriate bicarbonate/supportive care while arranging treatment; do not wait for one concentration threshold in a deteriorating patient.</td></tr>
</tbody></table>
<p>In salicylate poisoning, loss of compensatory hyperventilation and worsening acidemia increase tissue toxicity. Airway management must preserve the required ventilation; a falling serum concentration alone does not prove clinical recovery.</p></section>

<section id="recovery"><h2>13 · Assessing recovery from dialysis-requiring AKI</h2>
<table><thead><tr><th>Assessment</th><th>Interpretation</th></tr></thead><tbody>
<tr><td><strong>Sustained improvement in urine output</strong></td><td>Supports recovery, especially alongside improving clearance. Diuretic-induced urine output alone does not establish adequate kidney function.</td></tr>
<tr><td>Potassium and acid–base balance</td><td>Must remain acceptable without ongoing extracorporeal correction.</td></tr>
<tr><td>Volume balance</td><td>Kidney function must be sufficient for current intake, losses and fluid-removal needs.</td></tr>
<tr><td>Trial off RRT</td><td>Use a planned interruption with frequent clinical/laboratory reassessment and clear criteria for restarting.</td></tr>
</tbody></table>
<p><strong>A low creatinine while CRRT is running reflects treatment clearance as well as kidney function.</strong> Assess trends after interruption and avoid interpreting the treated concentration as proof of recovery.</p></section>

<section id="calciphylaxis"><h2>14 · Calciphylaxis</h2>
<p><strong>Severe pain followed by retiform purpura, indurated plaques and skin necrosis</strong> in a dialysis patient suggests calcific uremic arteriolopathy. Pain can precede an obvious ulcer.</p>
<table><thead><tr><th>Feature</th><th>Clinical implication</th></tr></thead><tbody>
<tr><td>Small-vessel calcification and thrombosis</td><td>Produces ischemic skin/subcutaneous injury; not simply excess calcium deposited on the skin surface.</td></tr>
<tr><td>Risk factors</td><td>Advanced kidney disease, disordered mineral metabolism, diabetes, obesity, low albumin and warfarin exposure. Normal current calcium/phosphate does not exclude it.</td></tr>
<tr><td>Diagnosis</td><td>Combine the clinical pattern with specialist assessment. Biopsy is selective because of poor healing/infection risk; consider mimics.</td></tr>
<tr><td>Treatment</td><td>Multidisciplinary wound care, analgesia, infection management, nutrition and correction of modifiable factors. Review warfarin, calcium load and phosphate/PTH management.</td></tr>
<tr><td>Sodium thiosulfate</td><td>Used off-label in many centers, but clinical benefit remains uncertain; it is not an established cure.</td></tr>
</tbody></table>
<p>Skin pain and necrosis require prompt assessment. Secondary infection and sepsis are major threats.</p></section>

<section id="pitfalls"><h2>15 · High-yield pitfalls</h2><ul>
<li><strong>eGFR 8 alone does not mean dialysis today;</strong> uremic pericarditis can mean dialysis despite stable creatinine.</li>
<li><strong>CRRT is selected for tolerability and control,</strong> not a proven universal survival advantage.</li>
<li><strong>Effluent dose ≠ net patient fluid removal.</strong> Downtime and predilution reduce effective delivery.</li>
<li><strong>Use matching units in Kt/V and calcium ratios.</strong> Convert 40 L to 40,000 mL when K is in mL/min.</li>
<li><strong>Isolated ultrafiltration does not adequately treat dangerous hyperkalemia.</strong></li>
<li><strong>Hemolysis → stop HD and do not return circuit blood.</strong></li>
<li><strong>High venous pressure + prolonged bleeding suggests outflow stenosis;</strong> a cold painful hand suggests steal.</li>
<li><strong>Acidosis + rising total/ionized calcium ratio + increasing calcium needs suggests citrate accumulation.</strong> Metabolized citrate excess usually causes alkalosis.</li>
<li><strong>Short PD dwell:</strong> a high neutrophil fraction matters even when WBC is below 100/µL.</li>
<li><strong>Fungal PD peritonitis → remove the catheter promptly and treat the fungus.</strong></li>
<li><strong>Icodextrin needs a compatible glucose meter.</strong> A falsely high result can lead to excessive insulin.</li>
<li><strong>Urine output, untreated solute control and fluid balance guide a trial off RRT.</strong></li>
</ul></section>'''


def make():
    doc=html.fragment_fromstring(BODY,create_parent='div')
    ids=doc.xpath('.//*[@id]/@id');assert len(ids)==len(set(ids))
    assert all(h.startswith('#') and h[1:] in ids for h in doc.xpath('.//a/@href'))
    tables=doc.xpath('.//table')
    for table in tables:
        columns=len(table.xpath('./thead/tr/th'))
        assert columns and all(len(row.xpath('./td'))==columns for row in table.xpath('./tbody/tr'))
    coverage=['timing','timing','timing','timing','timing','modality','modality','transport','transport',
              'dose','dose','adequacy','adequacy','adequacy','volume','volume','emergencies','emergencies',
              'access','access','access','access','citrate','citrate','peritonitis','peritonitis','peritonitis',
              'pd','pd','pd','toxins','toxins','modality','dose','recovery','transport','calciphylaxis']
    assert len(coverage)==37 and all(item in ids for item in coverage)
    assert not doc.xpath('.//script|.//iframe|.//h1')
    destination=DEST/'Nephrology/Dialysis RRT.html'
    document=page('Dialysis and renal replacement therapy',BODY)
    document=document.replace('<h1>Dialysis and renal replacement therapy</h1>','',1)
    document=document.replace('</style>','table{display:table;width:100%}th:first-child,td:first-child{min-width:120px}@media(max-width:650px){table{display:block;overflow-x:auto}}</style>')
    destination.write_text(document,encoding='utf-8')
    sources=[
        'https://kdigo.org/wp-content/uploads/2024/03/KDIGO-2024-CKD-Guideline.pdf',
        'https://kdigo.org/wp-content/uploads/2016/10/KDIGO-2012-AKI-Guideline-English.pdf',
        'https://www.kidney.org/sites/default/files/12-85-0946_ica_crn-pocket-guide_v6_chp_10.pdf',
        'https://www.kidney.org/sites/default/files/2026-07/2019-kdoqi-guideline-vascular-access.pdf',
        'https://www.bcrenal.ca/resource-gallery/Documents/Provincial-Guideline_HD_Complications.pdf',
        'https://pmc.ncbi.nlm.nih.gov/articles/PMC10245563/',
        'https://doi.org/10.1177/08968608221080586',
        'https://www.medicines.org.uk/emc/product/1819/smpc',
        'https://www.extrip-workgroup.org/lithium',
        'https://www.extrip-workgroup.org/salicylates',
        'https://pmc.ncbi.nlm.nih.gov/articles/PMC12683247/',
    ]
    destination.with_suffix('.review.json').write_text(json.dumps(dict(module='Dialysis RRT',status='authored',
        groups=len(doc.xpath('./section')),tables=len(tables),sourceCheckedAt='2026-11-06',
        independentClinicianReview=False,visibleReferences=False,visibleTitle=False,
        questionCoverage={str(i):section for i,section in enumerate(coverage,1)},checkedSources=sources),indent=2),encoding='utf-8')
    manifest=DEST/'authored-notes.json'
    if manifest.is_file():
        authored=json.loads(manifest.read_text(encoding='utf-8'))
        authored['Nephrology/Dialysis RRT']=dict(file=str(destination),sections=len(doc.xpath('./section')),
            tables=len(tables),references=0,words=len(doc.text_content().split()),status='authored_source_checked',chapterOrder=9)
        manifest.write_text(json.dumps(authored,indent=2),encoding='utf-8')
    print(destination)
    print(f'{len(doc.xpath("./section"))} sections; {len(tables)} tables; 37 questions mapped; all anchors and table rows valid')


if __name__=='__main__':make()
