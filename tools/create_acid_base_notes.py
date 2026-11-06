"""Author the acid–base module in the achalasia reference-note layout."""
from pathlib import Path
from create_qbank_topic_notes import page,DEST
BODY='''
<p class="meta">Nephrology → Acid–base disorders · Reference-checked 6 November 2026 · Adult interpretation; formulas are approximate physiological guides.</p>
<p class="key"><strong>Always do three checks:</strong> identify the primary process → test expected compensation → calculate the albumin-corrected anion gap. A normal pH does not exclude a dangerous mixed disorder.</p>
<nav><a href="#approach">Approach</a> · <a href="#formulas">Formulas</a> · <a href="#compensation">Compensation</a> · <a href="#mixed">Mixed disorders</a> · <a href="#urine">Urine indices</a> · <a href="#rta">RTA</a> · <a href="#alkalosis">Alkalosis</a> · <a href="#toxins">Special causes</a> · <a href="#treatment">Treatment</a> · <a href="#examples">Examples</a> · <a href="#pitfalls">Pitfalls</a></nav>

<section id="approach"><h2>1 · Read the blood gas systematically</h2><ol>
<li><strong>Validate the sample:</strong> clinical timing, oxygen/ventilation settings, simultaneous electrolytes, albumin, lactate and ketones when relevant. Investigate an implausible result or major discrepancy between chemistry total CO₂ and calculated gas bicarbonate.</li>
<li><strong>Describe the pH:</strong> arterial pH below 7.35 is acidemia; above 7.45 is alkalemia. Acidosis/alkalosis describe processes, not the final pH.</li>
<li><strong>Identify the dominant change:</strong> low bicarbonate drives metabolic acidosis; high PaCO₂ drives respiratory acidosis. Reverse directions drive alkalosis.</li>
<li><strong>Check compensation:</strong> departure from the expected response indicates an additional process or a changing/non-steady state.</li>
<li><strong>Calculate the gap even when pH is normal:</strong> correct for albumin; investigate an elevated gap rather than attributing everything to ventilation.</li>
<li><strong>Integrate the patient:</strong> medicines, gastrointestinal loss, kidney function, perfusion, infection, nutrition and possible toxins.</li></ol>
<p><strong>Venous gas:</strong> often useful for pH trends in appropriate settings; venous PCO₂ is not interchangeable with PaCO₂ for precise respiratory assessment, and venous PO₂ does not measure arterial oxygenation. <a href="#r1">[1]</a></p></section>

<section id="formulas"><h2>2 · Key formulas</h2><table><thead><tr><th>Calculation</th><th>Formula</th><th>Use / limitation</th></tr></thead><tbody>
<tr><td>Henderson–Hasselbalch</td><td>pH = 6.1 + log₁₀[HCO₃⁻ / (0.03 × PaCO₂)]</td><td>HCO₃⁻ in mmol/L; PaCO₂ in mmHg. Shows the metabolic-to-respiratory ratio.</td></tr>
<tr><td>Anion gap, excluding potassium</td><td>AG = Na⁺ − (Cl⁻ + HCO₃⁻)</td><td>Use the laboratory’s reference range and the same convention throughout.</td></tr>
<tr><td>Albumin-corrected AG</td><td>AGcorr = AG + 2.5 × (4 − albumin in g/dL)</td><td>Low albumin can conceal retained unmeasured anions. Albumin in g/L must first be divided by 10.</td></tr>
<tr><td>Delta ratio</td><td>(AGcorr − normal AG) / (24 − HCO₃⁻)</td><td>Only a heuristic in an established high-gap acidosis; unreliable near a zero denominator or with changing baselines.</td></tr>
<tr><td>Delta-adjusted bicarbonate</td><td>HCO₃⁻ + (AGcorr − normal AG)</td><td>A value well above the expected baseline suggests an additional alkalinizing process; a low value suggests added normal-gap acidosis.</td></tr>
<tr><td>Calculated serum osmolality</td><td>2Na⁺ + glucose/18 + BUN/2.8</td><td>Na in mmol/L; glucose and BUN in mg/dL. With glucose and urea both in mmol/L: 2Na + glucose + urea.</td></tr>
<tr><td>Osmolal gap</td><td>Measured osmolality − calculated osmolality</td><td>Account for ethanol and the laboratory’s formula; a normal result cannot exclude late toxic-alcohol poisoning.</td></tr>
<tr><td>Renal net acid excretion</td><td>NH₄⁺ excretion + titratable acid excretion − HCO₃⁻ excretion</td><td>These are excretion rates, not urine pH or isolated concentrations.</td></tr>
</tbody></table><p>For worked examples below, normal AG is assumed to be 12 mmol/L and baseline HCO₃⁻ 24 mmol/L. These are teaching assumptions, not universal laboratory cutoffs. <a href="#r1">[1]</a> <a href="#r2">[2]</a> <a href="#r3">[3]</a></p></section>

<section id="compensation"><h2>3 · Expected compensation: the essential table</h2><table><thead><tr><th>Primary disorder</th><th>Approximate expected response</th><th>If the measured result differs</th></tr></thead><tbody>
<tr><td>Metabolic acidosis</td><td><strong>Winter: PaCO₂ = 1.5 × HCO₃⁻ + 8 ± 2 mmHg</strong></td><td>Higher PaCO₂ → added respiratory acidosis; lower → added respiratory alkalosis.</td></tr>
<tr><td>Metabolic alkalosis</td><td>PaCO₂ rises roughly 0.6–0.75 mmHg per 1 mmol/L bicarbonate rise above 24; start near PaCO₂ 40.</td><td>A substantially excessive rise suggests added respiratory acidosis. The response is variable; do not treat a predicted point value as exact.</td></tr>
<tr><td>Acute respiratory acidosis</td><td>HCO₃⁻ rises about 1 mmol/L per 10 mmHg PaCO₂ rise above 40.</td><td>Much higher HCO₃⁻ suggests chronic adaptation or metabolic alkalosis; lower suggests added metabolic acidosis.</td></tr>
<tr><td>Chronic respiratory acidosis</td><td>HCO₃⁻ rises about 3.5–4 mmol/L per 10 mmHg PaCO₂ rise.</td><td>Renal adaptation takes several days and depends on kidney function.</td></tr>
<tr><td>Acute respiratory alkalosis</td><td>HCO₃⁻ falls about 2 mmol/L per 10 mmHg PaCO₂ fall below 40.</td><td>An unexpectedly large fall raises added metabolic acidosis or longer duration.</td></tr>
<tr><td>Chronic respiratory alkalosis</td><td>HCO₃⁻ falls about 4–5 mmol/L per 10 mmHg PaCO₂ fall.</td><td>Interpret with duration, renal function and the clinical cause.</td></tr>
</tbody></table><p><strong>Compensation does not overshoot:</strong> a second primary process is the usual explanation for an apparent overcorrection. Acute-on-chronic respiratory disease often falls between simple textbook predictions. <a href="#r1">[1]</a> <a href="#r4">[4]</a></p></section>

<section id="mixed"><h2>4 · Anion-gap and mixed metabolic disorders</h2><h3>High-gap versus normal-gap acidosis</h3>
<table><thead><tr><th>Pattern</th><th>Mechanism / causes</th><th>Discriminating checks</th></tr></thead><tbody>
<tr><td>High AG</td><td>Lactate, ketoacids, advanced kidney failure, methanol/ethylene glycol metabolites, salicylates, D-lactate, 5-oxoproline.</td><td>Measure suspected acids or toxins directly; a gap does not identify the molecule.</td></tr>
<tr><td>Normal AG / hyperchloremic</td><td>Gastrointestinal bicarbonate loss, RTA, chloride-rich fluid, early kidney-related acid retention, acetazolamide/topiramate.</td><td>Potassium, history, kidney function and appropriate urinary ammonium assessment.</td></tr>
</tbody></table><h3>Delta-ratio interpretation</h3><ul>
<li><strong>A disproportionately small gap rise compared with bicarbonate fall</strong> suggests added normal-gap acidosis.</li>
<li><strong>A disproportionately large gap rise</strong> suggests metabolic alkalosis or a raised pre-existing bicarbonate, such as chronic hypercapnia.</li>
<li>Conventional teaching often uses ratios below about 0.8 and above about 2 as flags; intermediate values do not prove a pure disorder. Acid type, urinary anion loss, treatment and baseline variation alter the relationship.</li></ul>
<p class="key"><strong>Example:</strong> vomiting plus ketoacidosis can produce a high anion gap with near-normal or elevated bicarbonate. Identify both processes rather than ruling out ketoacidosis from pH alone.</p><p><a href="#r2">[2]</a> <a href="#r3">[3]</a></p></section>

<section id="urine"><h2>5 · Urine indices: ask whether ammonium excretion is appropriate</h2><table><thead><tr><th>Index</th><th>Calculation / interpretation</th><th>Important limitations</th></tr></thead><tbody>
<tr><td>Urine anion gap</td><td>UAG = (urine Na + urine K) − urine Cl. In suitable normal-gap acidosis, a negative value supports increased NH₄Cl excretion, often with gastrointestinal loss.</td><td>Unmeasured urinary anions, ketoacids, certain drugs, low distal sodium delivery and CKD can undermine inference. A positive UAG is not synonymous with RTA.</td></tr>
<tr><td>Urine osmolal gap</td><td>Measured urine osmolality − [2(U Na + U K) + U urea + U glucose], using mmol/L inputs. Urea nitrogen in mg/dL requires /2.8; glucose in mg/dL /18.</td><td>Other unmeasured osmoles confound the gap. It is an indirect estimate; direct urinary ammonium is preferable when available.</td></tr>
<tr><td>Approximate urine NH₄⁺</td><td>Urine osmolal gap / 2 can estimate ammonium concentration under appropriate assumptions.</td><td>Concentration is not daily excretion; avoid rigid cutoffs across different urine volumes.</td></tr>
<tr><td>Urine pH</td><td>A persistently high value during systemic acidosis can suggest impaired distal acidification.</td><td>Urine pH does not quantify total acid elimination; infection, specimen delay, bicarbonaturia and low distal sodium delivery alter it.</td></tr>
</tbody></table><p><strong>Type 4 RTA trap:</strong> urine may be acidic despite inadequate ammonium excretion. A low urine pH therefore does not exclude this disorder. <a href="#r5">[5]</a></p></section>

<section id="rta"><h2>6 · RTA comparison</h2><table><thead><tr><th>Feature</th><th>Distal/type 1</th><th>Proximal/type 2</th><th>Type 4</th></tr></thead><tbody>
<tr><td>Main defect</td><td>Distal hydrogen-ion secretion</td><td>Reduced proximal bicarbonate reclamation</td><td>Reduced aldosterone effect and impaired ammonium handling; hyperkalemia suppresses ammoniagenesis</td></tr>
<tr><td>Potassium</td><td>Usually low</td><td>Usually low</td><td><strong>High</strong></td></tr>
<tr><td>Urine pH during established acidosis</td><td>Inappropriately high, often &gt;5.5, after excluding confounders</td><td>Can fall below 5.5 after plasma bicarbonate falls beneath the reduced reabsorptive threshold</td><td>Often below 5.5; ammonium excretion remains inadequate</td></tr>
<tr><td>Clues</td><td>Calcium-phosphate stones, nephrocalcinosis, hypocitraturia; Sjögren disease or drug injury</td><td>Fanconi features: normoglycemic glycosuria, phosphate/urate wasting and other proximal losses</td><td>Diabetes, tubulointerstitial disease, RAAS-blocking drugs or impaired aldosterone action</td></tr>
<tr><td>Principles</td><td>Cause-directed care; alkali and potassium/citrate strategy when indicated</td><td>Treat cause, replace associated losses; larger alkali needs can worsen potassium wasting</td><td>Address hyperkalemia and medicines; selected alkali, diuretic or mineralocorticoid strategies according to volume/BP and cause</td></tr>
</tbody></table><p>Do not diagnose RTA from one alkaline urine sample. The diagnosis requires the systemic acid–base pattern and appropriate exclusion of gastrointestinal loss, kidney failure and transient physiological confounders. <a href="#r5">[5]</a> <a href="#r6">[6]</a></p></section>

<section id="alkalosis"><h2>7 · Metabolic alkalosis: urine chloride plus blood pressure</h2><table><thead><tr><th>Pattern</th><th>Examples</th><th>Clinical direction</th></tr></thead><tbody>
<tr><td>Urine chloride &lt;20 mmol/L</td><td>Vomiting/NG loss, remote diuretics, chloride depletion</td><td>Correct cause, potassium and chloride deficit; isotonic saline when volume depleted and clinically appropriate.</td></tr>
<tr><td>Urine chloride ≥20; normal/low BP</td><td>Active diuretics, Bartter/Gitelman-type salt wasting</td><td>Review drugs, repeat when timing matters, assess magnesium and renal salt loss.</td></tr>
<tr><td>Urine chloride ≥20; hypertension</td><td>Mineralocorticoid excess or related sodium-retaining states</td><td>Evaluate renin/aldosterone pathways and mimics; treat the mechanism.</td></tr>
</tbody></table><ul><li><strong>Maintenance:</strong> chloride depletion, potassium depletion, reduced filtration and mineralocorticoid activity can prevent bicarbonate elimination after the initiating event has stopped.</li><li><strong>Paradoxical aciduria:</strong> a volume- and potassium-depleted patient can excrete acidic urine while the blood remains alkalemic.</li><li><strong>Post-hypercapnic alkalosis:</strong> rapid correction of chronic CO₂ retention can leave previously retained bicarbonate behind.</li><li><strong>Acetazolamide:</strong> increases bicarbonate excretion in selected cases; monitor potassium and kidney function. It does not replace correction of the cause, and improved bicarbonate values do not guarantee improved ventilator outcomes.</li></ul><p>Active diuretics can raise urine chloride despite effective volume depletion. Interpret the sample with treatment timing. <a href="#r7">[7]</a></p></section>

<section id="toxins"><h2>8 · Special high-gap causes and mixed patterns</h2><table><thead><tr><th>Condition</th><th>Recognition clue</th><th>Pitfall</th></tr></thead><tbody>
<tr><td>Salicylates</td><td>Respiratory alkalosis plus high-gap metabolic acidosis; tinnitus, tachypnea, neurological symptoms</td><td>Near-normal pH can conceal substantial toxicity. Loss of compensatory ventilation during intubation is dangerous.</td></tr>
<tr><td>Methanol</td><td>Exposure concern, acidosis, visual toxicity</td><td>Osmolal gap can fall as parent alcohol becomes acidic metabolites.</td></tr>
<tr><td>Ethylene glycol</td><td>Acidosis, AKI; possible hypocalcemia or calcium-oxalate crystals</td><td>Absence of crystals or a normal late osmolal gap does not exclude poisoning.</td></tr>
<tr><td>D-lactate</td><td>Short-bowel context with episodic neurological symptoms and acidosis</td><td>Routine lactate assays predominantly measure L-lactate.</td></tr>
<tr><td>5-oxoproline</td><td>Unexplained gap with risk factors such as chronic acetaminophen exposure, malnutrition or serious illness</td><td>A therapeutic acetaminophen concentration does not exclude this pathway.</td></tr>
<tr><td>Sepsis</td><td>Lactate-related acidosis with possible respiratory alkalosis</td><td>Albumin loss, fluids, kidney dysfunction and ventilation can produce several simultaneous effects.</td></tr>
</tbody></table><p>Suspected toxic-alcohol poisoning needs urgent toxicology input; antidote and dialysis decisions use the exposure, clinical severity and agent-specific guidance, not a gap alone. <a href="#r3">[3]</a> <a href="#r8">[8]</a> <a href="#r9">[9]</a></p></section>

<section id="treatment"><h2>9 · Treatment principles and current evidence</h2><ul>
<li><strong>Treat the cause:</strong> restore perfusion, address infection, stop causative exposures and manage kidney/respiratory failure as appropriate. Alkali is not a substitute for cause control.</li>
<li><strong>DKA:</strong> follow a fluid, insulin and potassium protocol. Routine bicarbonate is not recommended; the 2024 consensus considers it for severe acidemia, pH &lt;7.0. Defer insulin and replace potassium if K⁺ is &lt;3.5 mmol/L. Resolution uses plasma ketones &lt;0.6 mmol/L plus venous pH ≥7.3 or bicarbonate ≥18 mmol/L; anion gap alone can mislead after chloride-rich fluids.</li>
<li><strong>CKD:</strong> KDIGO 2024 suggests considering pharmacological treatment, with or without dietary intervention, for clinically important acidosis—for example adult bicarbonate &lt;18 mmol/L. Monitor bicarbonate, potassium, blood pressure and fluid status; this is not a universal mandate to treat every result below 22.</li>
<li><strong>Severe acidemia with AKI:</strong> BICARICU-2 did not show lower 90-day mortality with bicarbonate in its studied ICU population, although fewer patients received kidney replacement therapy. Do not convert this into a mortality claim or a rule for all acidosis.</li>
<li><strong>Kidney replacement therapy:</strong> consider refractory severe acidemia with the whole clinical picture, especially hyperkalemia, overload, uremic complications or selected toxins. There is no single pH threshold that replaces bedside assessment.</li>
<li><strong>Bicarbonate hazards:</strong> sodium/fluid loading, CO₂ generation and electrolyte changes. Adequate ventilation and repeated assessment matter.</li></ul><p><a href="#r10">[10]</a> <a href="#r11">[11]</a> <a href="#r12">[12]</a></p></section>

<section id="examples"><h2>10 · Worked examples</h2>
<h3>A · Low bicarbonate: is ventilation adequate?</h3><p>HCO₃⁻ 12, PaCO₂ 35 mmHg. Winter predicts <strong>26 ±2</strong>. Actual PaCO₂ is higher: <strong>metabolic acidosis plus respiratory acidosis</strong>, not appropriate compensation.</p>
<h3>B · Albumin correction reveals a mixed metabolic disorder</h3><p>Na 140, Cl 100, HCO₃⁻ 24, albumin 2 g/dL. AG = <strong>16</strong>; corrected AG = <strong>21</strong>. Delta-adjusted bicarbonate = 24 + (21 − 12) = <strong>33</strong>. A high-gap process can coexist with metabolic alkalosis or a raised pre-existing bicarbonate. The delta-ratio denominator is zero here: <strong>do not calculate a ratio</strong>.</p>
<h3>C · Added normal-gap acidosis</h3><p>Na 140, Cl 112, HCO₃⁻ 10, albumin 4. AG = <strong>18</strong>; ΔAG = 6, ΔHCO₃⁻ = 14; ratio ≈<strong>0.43</strong>. This supports a high-gap component plus substantial normal-gap acidosis; confirm with history and direct measurements.</p>
<h3>D · Acute versus chronic CO₂ retention</h3><p>At PaCO₂ 60, a simple acute rise predicts HCO₃⁻ near <strong>26</strong>; established chronic adaptation predicts about <strong>31–32</strong>. Duration, renal function and added metabolic disease determine interpretation.</p></section>

<section id="pitfalls"><h2>11 · Final recall and pitfalls</h2><ul>
<li><strong>Normal pH ≠ normal acid–base physiology.</strong> Opposing processes can conceal each other.</li>
<li><strong>Low bicarbonate ≠ automatically metabolic acidosis.</strong> Chronic respiratory alkalosis also lowers bicarbonate.</li>
<li><strong>Correct the gap for albumin.</strong> Avoid switching between potassium-inclusive and potassium-exclusive reference values.</li>
<li><strong>Measure lactate and β-hydroxybutyrate when relevant.</strong> Neither is identified by the anion gap alone.</li>
<li><strong>Urine pH ≠ ammonium excretion.</strong> Type 4 RTA can have acidic urine.</li>
<li><strong>Normal osmolal gap ≠ no toxic alcohol.</strong> Time since exposure changes the pattern.</li>
<li><strong>Stewart perspective:</strong> PaCO₂, strong-ion difference and weak acids help explain chloride-associated acidosis and the alkalinizing effect of low albumin. It complements rather than replaces clinical cause assessment. <a href="#r13">[13]</a></li>
<li><strong>Trend after treatment.</strong> Fluids, insulin, ventilation and dialysis can change the dominant process.</li></ul></section>

<section><h2>References</h2><ol>
<li id="r1"><a href="https://site.thoracic.org/assemblies/cc/clinical-education/interpretation-of-abgs">American Thoracic Society. Interpretation of arterial blood gases.</a></li>
<li id="r2"><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11924111/">Haber et al. Evaluating a low anion gap: a practical approach. Cleveland Clinic Journal of Medicine, 2023.</a></li>
<li id="r3"><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC5260542/">Seifter and Chang. Disorders of acid–base balance: new perspectives. Kidney Diseases, 2017.</a></li>
<li id="r4"><a href="https://www.merckmanuals.com/professional/multimedia/table/primary-changes-and-compensations-in-simple-acid-base-disorders">Merck Manual Professional. Primary changes and compensations in simple acid–base disorders.</a></li>
<li id="r5"><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC5757610/">Berend. Review of the diagnostic evaluation of normal anion gap metabolic acidosis. Kidney Diseases, 2017.</a></li>
<li id="r6"><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8610947/">Giglio et al. Distal renal tubular acidosis: a systematic approach from diagnosis to treatment. Journal of Nephrology, 2021.</a></li>
<li id="r7"><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC10947768/">Do et al. Metabolic alkalosis: pathogenesis, diagnosis, and treatment. AJKD Core Curriculum, 2022.</a></li>
<li id="r8"><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4371029/">American College of Medical Toxicology. Management priorities in salicylate toxicity, 2015.</a></li>
<li id="r9"><a href="https://www.extrip-workgroup.org/recommendations">EXTRIP Workgroup. Agent-specific extracorporeal treatment recommendations.</a></li>
<li id="r10"><a href="https://doi.org/10.2337/dci24-0032">Umpierrez et al. Hyperglycemic crises in adults with diabetes: international consensus report. Diabetes Care, 2024.</a></li>
<li id="r11"><a href="https://kdigo.org/guidelines/ckd-evaluation-and-management/">KDIGO 2024 CKD guideline. Practice points 3.10.1–3.10.2.</a></li>
<li id="r12"><a href="https://doi.org/10.1001/jama.2025.20231">Jung et al. BICARICU-2 randomized clinical trial. JAMA, 2025.</a></li>
<li id="r13"><a href="https://doi.org/10.1152/ajprenal.00475.2007">Kurtz et al. Acid–base analysis: a critique of the Stewart and bicarbonate-centered approaches. American Journal of Physiology–Renal Physiology, 2008.</a></li>
</ol><p class="meta">Educational revision notes. Source-checked author draft; no independent clinician review recorded.</p></section>
'''
def make():
    from compact_acid_base_notes import compact
    dest=DEST/'Nephrology/Acid Base Disorders.html';dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(page('Acid–base disorders · High-yield notes',compact(BODY)),encoding='utf-8');print(dest)
if __name__=='__main__':make()
