"""Concise postgraduate notes: standard terminology, formulas and discriminating facts."""
import lxml.html as H

BODY='''<nav><strong>Contents</strong> · <a href="#interpret">Interpretation</a> · <a href="#metabolic-acidosis">Metabolic acidosis</a> · <a href="#rta">RTA</a> · <a href="#alkalosis">Metabolic alkalosis</a> · <a href="#respiratory">Respiratory disorders</a> · <a href="#mixed">Mixed disorders</a> · <a href="#treatment">Treatment</a> · <a href="#references">References</a></nav>

<section id="interpret"><h2>1 · Acid–base interpretation</h2>
<ol><li><strong>pH:</strong> &lt;7.35 = acidemia; &gt;7.45 = alkalemia.</li>
<li><strong>Primary change:</strong> HCO₃⁻ ↓ = metabolic acidosis; HCO₃⁻ ↑ = metabolic alkalosis; PaCO₂ ↑ = respiratory acidosis; PaCO₂ ↓ = respiratory alkalosis.</li>
<li><strong>Compensation:</strong> compare measured values with the expected response.</li>
<li><strong>Anion gap:</strong> calculate and correct for albumin.</li>
<li><strong>Mixed disorder:</strong> check compensation and the relationship between the gap rise and bicarbonate fall.</li></ol>
<p class="key"><strong>Normal pH does not exclude a mixed disorder. Low HCO₃⁻ may reflect metabolic acidosis or compensation for respiratory alkalosis.</strong></p>
<p>pH = 6.1 + log₁₀[HCO₃⁻ / (0.03 × PaCO₂)]. HCO₃⁻: mmol/L; PaCO₂: mmHg. <a href="#r1">[1]</a></p></section>

<section id="metabolic-acidosis"><h2>2 · Metabolic acidosis</h2>
<h3>Formulas</h3><table><thead><tr><th>Calculation</th><th>Formula</th></tr></thead><tbody>
<tr><td>Expected PaCO₂: Winter’s formula</td><td><strong>1.5 × HCO₃⁻ + 8 ± 2</strong></td></tr>
<tr><td>Anion gap, excluding potassium</td><td><strong>AG = Na − Cl − HCO₃⁻</strong></td></tr>
<tr><td>Albumin correction</td><td><strong>AGcorr = AG + 2.5 × (4 − albumin in g/dL)</strong></td></tr>
<tr><td>Calculated serum osmolality</td><td>2Na + glucose/18 + BUN/2.8; glucose and BUN in mg/dL. With glucose and urea in mmol/L: 2Na + glucose + urea.</td></tr>
<tr><td>Osmolal gap</td><td>Measured − calculated osmolality; account for ethanol.</td></tr>
</tbody></table>
<p><strong>Measured PaCO₂ above Winter’s range:</strong> additional respiratory acidosis. <strong>Below range:</strong> additional respiratory alkalosis.</p>
<h3>Causes</h3><table><thead><tr><th>High anion gap</th><th>Normal anion gap</th></tr></thead><tbody>
<tr><td>Lactic acidosis; ketoacidosis; advanced kidney failure; methanol; ethylene glycol; salicylates; D-lactate; 5-oxoproline.</td><td>Diarrhea and other intestinal bicarbonate losses; renal tubular acidosis; chloride-rich fluids; early kidney-related acid retention; acetazolamide/topiramate.</td></tr>
</tbody></table>
<h3>Distinctive causes</h3><table><thead><tr><th>Cause</th><th>Key clue / trap</th></tr></thead><tbody>
<tr><td>Salicylates</td><td><strong>Respiratory alkalosis + high-gap acidosis.</strong> Tinnitus and tachypnea. Near-normal pH can mask toxicity; loss of hyperventilation during intubation can worsen acidemia.</td></tr>
<tr><td>Methanol</td><td>Visual toxicity. A normal late osmolal gap does not exclude poisoning.</td></tr>
<tr><td>Ethylene glycol</td><td>AKI, possible hypocalcemia and calcium-oxalate crystals. Absence of crystals does not exclude poisoning.</td></tr>
<tr><td>D-lactate</td><td>Short bowel + episodic neurological symptoms. Routine lactate assays mainly measure L-lactate.</td></tr>
<tr><td>5-oxoproline</td><td>Chronic acetaminophen exposure, malnutrition or serious illness; acetaminophen concentration may be therapeutic.</td></tr>
</tbody></table>
<p><strong>Gap traps:</strong> hypoalbuminemia masks a high AG; toxic-alcohol osmolal gaps fall as acidic metabolites accumulate. Measure suspected lactate, ketones or toxins directly. <a href="#r2">[2]</a> <a href="#r3">[3]</a> <a href="#r8">[8]</a> <a href="#r9">[9]</a></p></section>

<section id="rta"><h2>3 · Normal-gap acidosis: urine tests and RTA</h2>
<h3>Urinary ammonium assessment</h3><table><thead><tr><th>Test</th><th>Interpretation</th></tr></thead><tbody>
<tr><td>Urine anion gap<br>UAG = U Na + U K − U Cl</td><td>Negative UAG supports increased NH₄Cl excretion, often with diarrhea. A positive UAG is not diagnostic of RTA.</td></tr>
<tr><td>Urine osmolal gap<br>Measured − [2(U Na + U K) + U urea + U glucose]</td><td>Use mmol/L. Gap/2 roughly estimates urine NH₄⁺ concentration when other unmeasured osmoles are absent. Direct NH₄⁺ measurement is preferable.</td></tr>
<tr><td>Net acid excretion</td><td>NH₄⁺ + titratable acid − HCO₃⁻ excretion; use excretion rates, not urine pH.</td></tr>
</tbody></table>
<p><strong>UAG limitations:</strong> urinary ketoanions or drug anions, low distal sodium delivery, and CKD. <strong>Urine pH limitations:</strong> urinary infection, delayed processing and bicarbonaturia.</p>
<h3>RTA comparison</h3><table><thead><tr><th>Feature</th><th>Type 1: distal</th><th>Type 2: proximal</th><th>Type 4</th></tr></thead><tbody>
<tr><td>Defect</td><td>Distal H⁺ secretion</td><td>Proximal HCO₃⁻ reabsorption</td><td>Reduced aldosterone effect; reduced NH₄⁺ excretion</td></tr>
<tr><td>Potassium</td><td>Usually low</td><td>Usually low</td><td><strong>High</strong></td></tr>
<tr><td>Urine pH during acidosis</td><td>Usually &gt;5.5</td><td>Can fall &lt;5.5 once plasma HCO₃⁻ is below the reduced reabsorptive threshold</td><td>Often &lt;5.5</td></tr>
<tr><td>Clues</td><td>Calcium-phosphate stones, nephrocalcinosis, low urine citrate; Sjögren disease</td><td>Fanconi syndrome: glycosuria despite normal blood glucose, phosphate and urate wasting</td><td>Diabetes, tubulointerstitial disease, RAAS-blocking drugs</td></tr>
<tr><td>Treatment</td><td>Alkali; potassium/citrate replacement when indicated</td><td>Replace alkali and associated losses; monitor potassium wasting</td><td>Correct hyperkalemia; review drugs; selected alkali, diuretic or mineralocorticoid treatment</td></tr>
</tbody></table><p class="key"><strong>Acidic urine does not exclude type 4 RTA:</strong> urine pH measures free H⁺, not total ammonium excretion. <a href="#r5">[5]</a> <a href="#r6">[6]</a></p></section>

<section id="alkalosis"><h2>4 · Metabolic alkalosis</h2>
<p><strong>Expected PaCO₂:</strong> approximately 40 + (0.6–0.75) × (HCO₃⁻ − 24). Compensation is variable. <a href="#r4">[4]</a></p>
<table><thead><tr><th>Urine chloride / BP</th><th>Likely causes</th><th>Treatment direction</th></tr></thead><tbody>
<tr><td>U Cl &lt;20 mmol/L</td><td>Vomiting, gastric suction, remote diuretic use</td><td>Replace chloride and potassium; saline if volume depleted and appropriate.</td></tr>
<tr><td>U Cl ≥20; normal/low BP</td><td>Active diuretics, Bartter/Gitelman syndromes</td><td>Review diuretics; assess renal salt loss and magnesium.</td></tr>
<tr><td>U Cl ≥20; hypertension</td><td>Mineralocorticoid excess or related sodium-retaining states</td><td>Evaluate renin/aldosterone and treat the cause.</td></tr>
</tbody></table>
<ul><li><strong>Persistence:</strong> chloride depletion, hypokalemia, reduced GFR and mineralocorticoid activity limit bicarbonate excretion.</li>
<li><strong>Active diuretics:</strong> urine chloride may be high despite volume depletion.</li>
<li><strong>Paradoxical aciduria:</strong> acidic urine despite metabolic alkalosis in severe volume/potassium depletion.</li>
<li><strong>Post-hypercapnic alkalosis:</strong> rapid correction of chronic CO₂ retention leaves retained bicarbonate.</li>
<li><strong>Acetazolamide:</strong> promotes bicarbonate loss; monitor potassium and renal function. A lower bicarbonate does not establish improved ventilator outcomes.</li></ul><p><a href="#r7">[7]</a></p></section>

<section id="respiratory"><h2>5 · Respiratory acidosis and alkalosis</h2>
<p>Starting values for these estimates: <strong>PaCO₂ 40 mmHg; HCO₃⁻ 24 mmol/L.</strong></p>
<table><thead><tr><th>Disorder</th><th>Expected HCO₃⁻ change per 10 mmHg PaCO₂ change</th></tr></thead><tbody>
<tr><td>Acute respiratory acidosis</td><td><strong>↑ 1 mmol/L</strong> per PaCO₂ ↑ 10</td></tr>
<tr><td>Chronic respiratory acidosis</td><td><strong>↑ 3.5–4 mmol/L</strong> per PaCO₂ ↑ 10</td></tr>
<tr><td>Acute respiratory alkalosis</td><td><strong>↓ 2 mmol/L</strong> per PaCO₂ ↓ 10</td></tr>
<tr><td>Chronic respiratory alkalosis</td><td><strong>↓ 4–5 mmol/L</strong> per PaCO₂ ↓ 10</td></tr>
</tbody></table>
<p><strong>At PaCO₂ 60:</strong> expected HCO₃⁻ ≈26 in acute respiratory acidosis; ≈31–32 in chronic respiratory acidosis.</p>
<p><strong>Mixed disorder:</strong> HCO₃⁻ below the expected range suggests additional metabolic acidosis; above it suggests additional metabolic alkalosis, after allowing for duration of the respiratory disorder. <a href="#r1">[1]</a> <a href="#r4">[4]</a></p></section>

<section id="mixed"><h2>6 · Mixed disorders</h2>
<table><thead><tr><th>Calculation</th><th>Formula</th></tr></thead><tbody>
<tr><td>Delta ratio</td><td><strong>(AGcorr − normal AG) / (24 − HCO₃⁻)</strong></td></tr>
<tr><td>Delta-adjusted bicarbonate</td><td><strong>HCO₃⁻ + (AGcorr − normal AG)</strong></td></tr>
</tbody></table>
<ul><li><strong>Small AG rise relative to HCO₃⁻ fall:</strong> additional normal-gap acidosis.</li>
<li><strong>Large AG rise relative to HCO₃⁻ fall:</strong> additional metabolic alkalosis or raised baseline bicarbonate from chronic hypercapnia.</li>
<li>Ratios &lt;~0.8 or &gt;~2 are clues, not diagnostic cutoffs. Do not calculate the ratio when its denominator is zero or near zero.</li></ul>
<h3>Worked examples</h3><table><thead><tr><th>Results</th><th>Calculation</th><th>Conclusion</th></tr></thead><tbody>
<tr><td>HCO₃⁻ 12; PaCO₂ 35</td><td>Winter: 26 ±2</td><td>Metabolic + respiratory acidosis</td></tr>
<tr><td>Na 140; Cl 112; HCO₃⁻ 10; albumin 4 g/dL</td><td>AG 18; delta ratio = 6/14 ≈0.43</td><td>High-gap + normal-gap acidosis</td></tr>
<tr><td>Na 140; Cl 100; HCO₃⁻ 24; albumin 2 g/dL</td><td>AG 16; AGcorr 21; adjusted HCO₃⁻ 33</td><td>High-gap process with metabolic alkalosis or elevated baseline bicarbonate; delta ratio undefined</td></tr>
</tbody></table><p>Examples assume normal AG 12 and baseline HCO₃⁻ 24 mmol/L; substitute the laboratory range and known patient baseline. <a href="#r2">[2]</a> <a href="#r3">[3]</a></p></section>

<section id="treatment"><h2>7 · Treatment essentials</h2>
<ul><li><strong>Metabolic acidosis:</strong> correct the cause. Bicarbonate does not replace treatment of shock, infection, ketoacidosis or poisoning.</li>
<li><strong>DKA:</strong> fluids, insulin and potassium. If K⁺ &lt;3.5 mmol/L, replace potassium and defer insulin. Bicarbonate is not routine; consider at pH &lt;7.0 under the 2024 consensus. Resolution: ketones &lt;0.6 mmol/L plus pH ≥7.3 or HCO₃⁻ ≥18 mmol/L. The anion gap alone is unreliable after hyperchloremic acidosis develops. <a href="#r10">[10]</a></li>
<li><strong>CKD:</strong> KDIGO 2024 suggests considering treatment for clinically important acidosis, e.g. HCO₃⁻ &lt;18 mmol/L in adults. Monitor bicarbonate, potassium, BP and fluid status. <a href="#r11">[11]</a></li>
<li><strong>Severe acidemia + AKI:</strong> BICARICU-2 showed no 90-day mortality benefit from bicarbonate; kidney replacement therapy use was lower. <a href="#r12">[12]</a></li>
<li><strong>Dialysis:</strong> refractory severe acidemia, especially with hyperkalemia, overload, uremic complications or dialyzable toxins. A single pH cutoff is insufficient.</li>
<li><strong>Bicarbonate adverse effects:</strong> sodium/fluid loading, CO₂ generation and electrolyte changes.</li></ul>
<p><strong>Stewart approach:</strong> PaCO₂, strong-ion difference and weak acids describe acid–base balance. Extra chloride can lower pH; low albumin can raise it. <a href="#r13">[13]</a></p></section>'''

def compact(original):
    root=H.fragment_fromstring(original,create_parent='div')
    refs=root.xpath('./section[not(@id)]')[-1];refs.set('id','references')
    return BODY+H.tostring(refs,encoding='unicode')
