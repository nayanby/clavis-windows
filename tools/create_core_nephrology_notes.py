from clinical_note_authoring import *
AKI=('KDIGO AKI guidance: published framework and update status','https://kdigo.org/guidelines/acute-kidney-injury/')
CKD=('KDIGO CKD guideline, 2024','https://kdigo.org/guidelines/ckd-evaluation-and-management/')
ANEMIA=('KDIGO anemia in CKD guideline, 2026','https://kdigo.org/wp-content/uploads/2026/01/KDIGO-2026-Anemia-in-CKD-Guideline.pdf')
GN=('KDIGO glomerular disease guidelines and focused updates','https://kdigo.org/guidelines/gd/')
IGA=('KDIGO IgAN/IgAV guideline, 2025','https://doi.org/10.1016/j.kint.2025.04.004')
NA=('European hyponatremia guideline','https://academic.oup.com/ejendo/article/170/3/G1/6668028')
K=('UK Kidney Association hyperkalemia guidance, updated 2026','https://www.ukkidney.org/health-professionals/guidelines/treatment-acute-hyperkalaemia-adults-0')

def aki():
 write('Nephrology','Acute Kidney Injury',[
 S('Diagnosis and staging',T('Stage|Creatinine criterion|Urine output criterion','''AKI definition|Rise ≥0.3 mg/dL in 48 h or ≥1.5× baseline within 7 days|<0.5 mL/kg/h for ≥6 h
 1|1.5–1.9× baseline or ≥0.3 mg/dL rise|<0.5 mL/kg/h for 6–12 h
 2|2.0–2.9× baseline|<0.5 mL/kg/h for ≥12 h
 3|≥3× baseline, creatinine ≥4 mg/dL, or initiation of kidney replacement therapy|<0.3 mL/kg/h for ≥24 h or anuria ≥12 h''')+P('Use the worse qualifying stage. This is the published KDIGO framework; do not present a public-review update draft as a final guideline. Creatinine lags behind injury and is affected by muscle mass/dilution.')),
 S('Localize the cause',T('Category|Examples / clues|Useful assessment','''Hemodynamic|Volume loss, shock, low effective circulation, drug-related pressure effects|Volume/perfusion, cardiac function and medication review
 Tubular injury|Sepsis, ischemia, nephrotoxins, pigment injury|Granular casts and tubular cells; absence does not exclude
 Interstitial|Drug-associated or systemic inflammation|Sterile pyuria/white-cell casts may occur; classic fever–rash–eosinophilia triad often absent
 Glomerular/vascular|GN, vasculitis, TMA, embolic disease|Hematuria/proteinuria, dysmorphic RBCs/casts, serology and selected biopsy
 Obstructive|Prostate, stones, pelvic disease, catheter block|Bladder/catheter check and imaging; early obstruction may lack marked dilation''')),
 S('Investigations that are often overinterpreted',U('''FeNa = (U Na × P creatinine)/(P Na × U creatinine) ×100. A value <1% suggests sodium retention but can occur in intrinsic injury; diuretics and CKD complicate interpretation.
 FeUrea is not a definitive alternative that eliminates all diuretic/sepsis confounding.
 Urine eosinophils neither confirm nor exclude acute interstitial nephritis.
 A bland urine sediment does not exclude serious vascular, obstructive or hemodynamic disease.
 Ultrasound, urine microscopy, protein quantification and selected biopsy answer different questions; order them according to the suspected compartment.''')),
 S('Treatment and follow-up',U('''Correct perfusion/volume with reassessment; avoid repeated fluid boluses when congestion or overload is present.
 Treat sepsis and obstruction, stop avoidable nephrotoxins, review renally cleared drugs and monitor potassium/acid–base status.
 Loop diuretics treat overload; they do not reverse tubular injury. Low-dose dopamine is not kidney-protective treatment.
 Dialysis for refractory life-threatening electrolyte, acid–base, volume or uremic complications; not one creatinine/BUN number alone.
 Rhabdomyolysis: treat cause, fluid strategy and complications; routine bicarbonate/mannitol for everyone is not established.
 After AKI: reassess recovery, albuminuria and CKD risk; a return toward baseline creatinine does not erase future risk.'''))],[AKI])

def ckd():
 write('Nephrology','Chronic Kidney Disease',[
 S('Classify by cause, GFR and albuminuria',T('Category|Definition','''CKD|Kidney structural/functional abnormality present ≥3 months with health implications
 G1 / G2|eGFR ≥90 / 60–89; require another marker of kidney damage for CKD diagnosis
 G3a / G3b|45–59 / 30–44 mL/min/1.73 m²
 G4 / G5|15–29 / <15
 A1 / A2 / A3|Urine ACR <30 / 30–300 / >300 mg/g''')+U('''One low eGFR does not prove chronicity. Confirm albuminuria and exclude transient exercise, infection or other causes.
 Creatinine–cystatin C assessment can improve estimation when available and clinically important. Indexed eGFR and absolute drug-clearance estimates are not always interchangeable.
 Use validated kidney-failure risk estimates with GFR/ACR and cause for referral and planning.''')),
 S('Slow progression and reduce cardiovascular risk',T('Intervention|Core principle','''BP and RAAS blockade|ACE inhibitor/ARB for appropriate albuminuric disease; monitor BP, K and creatinine; avoid routine dual blockade
 SGLT2 inhibitor|KDIGO supports eligible CKD at eGFR ≥20 with significant albuminuria or HF; additional defined groups also benefit
 Nonsteroidal MRA|Selected type 2 diabetic CKD with persistent albuminuria, adequate eGFR and normal potassium despite standard care
 GLP-1-based therapy|Selected diabetes/obesity and cardiovascular–kidney indications; agent-specific evidence
 Lifestyle / prevention|Smoking cessation, sodium management, activity, appropriate nutrition and lipid prevention''')+U('''An expected early eGFR dip after a kidney-protective drug differs from progressive injury; assess magnitude, trend, volume and symptoms.
 Manage hyperkalemia when feasible rather than automatically discarding every protective medicine.
 Plan around acute illness, fasting and procedures using drug-specific guidance.''')),
 S('Complications: compare treatment goals',T('Complication|Management distinction','''Anemia|Check iron, bleeding, B12/folate and other causes; iron/ESA selected by setting and risk. KDIGO 2026 advises ESA maintenance below Hb 11.5 g/dL rather than normalization.
 CKD mineral/bone disorder|Trend calcium, phosphate and PTH together; avoid reacting to one PTH value alone
 Acidosis|Consider treatment for clinically important acidosis, e.g. HCO₃⁻ <18 mmol/L in adults; monitor fluid/BP/K
 Volume overload|Sodium/diuretic strategy; assess HF and renal cause
 Uremic symptoms|Assess nutrition, cognition, pericarditis and other complications; dialysis decision is clinical''')),
 S('Planning and pitfalls',U('''Discuss transplant, home/in-centre modalities and conservative kidney care according to prognosis and preferences before a crisis.
 Preserve suitable veins and plan access when indicated; eGFR alone does not determine the exact dialysis start date.
 Avoid unnecessary NSAIDs and adjust relevant drug doses; do not deny every beneficial contrast study solely because CKD exists.
 Dietary restrictions should target actual problems; indiscriminate severe protein/potassium restriction can worsen nutrition.
 Small echogenic kidneys support chronic disease but normal-sized kidneys do not exclude CKD.'''))],[CKD,ANEMIA])

def glomerular():
 write('Nephrology','Glomerular Diseases',[
 S('Recognize the syndrome',T('Syndrome|Core findings','''Nephritic|Glomerular hematuria, variable proteinuria, reduced GFR, hypertension/edema
 Nephrotic|Heavy proteinuria, hypoalbuminemia and edema; hyperlipidemia/thrombosis risk
 Rapidly progressive GN|Rapid GFR loss with active glomerular injury; urgent serology/biopsy and treatment planning
 Pulmonary–renal|Alveolar hemorrhage + GN; ANCA, anti-GBM and other causes''')),
 S('Nephrotic diseases: compare together',T('Disease|Clues|Treatment distinction','''Minimal-change disease|Often abrupt nephrosis; foot-process effacement; light microscopy relatively bland|Glucocorticoid-responsive in many adults; exclude secondary causes
 FSGS|A lesion pattern, not one disease|Primary, genetic and adaptive forms differ; do not immunosuppress every FSGS lesion
 Membranous nephropathy|PLA2R-related or secondary; subepithelial deposits|Risk-based immunotherapy plus supportive care; assess malignancy/infection/drug/systemic causes as appropriate
 Amyloid|Systemic clues; typed deposits|AL and ATTR/other amyloid require different treatments
 Diabetic kidney disease|Compatible duration/retinopathy/albuminuria pattern|Atypical rapid decline or active sediment can require another diagnosis/biopsy''')),
 S('Nephritic and crescentic diseases',T('Disease|Discriminating findings|Management principle','''IgA nephropathy|Hematuria near mucosal infection; biopsy diagnosis|Supportive kidney protection plus selected disease-targeted treatment under 2025 guidance
 Infection-related GN|Infection context, often low complement|Treat infection; avoid reflex immunosuppression without diagnosis
 Lupus nephritis|Systemic lupus, complements/anti-dsDNA; class/activity on biopsy|Class- and risk-directed induction/maintenance; current combination options differ
 ANCA vasculitis|Pauci-immune injury, MPO/PR3 may be positive|Urgent rituximab/cyclophosphamide-based induction and glucocorticoid strategy; selected plasma exchange, not routine for everyone
 Anti-GBM disease|Linear GBM antibodies/deposits; pulmonary hemorrhage possible|Urgent plasma exchange plus immunosuppression in appropriate patients
 C3/immune-complex MPGN patterns|Complement/immune-complex mechanisms|Investigate infection, monoclonal disease and complement disorders; morphology alone does not define cause''')),
 S('Supportive care and treatment pitfalls',U('''Quantify proteinuria, assess renal function, BP, potassium, albumin and thrombotic/infectious risk. RAAS/SGLT2 treatment depends on eligibility and acute stability.
 Nephrotic thrombosis prophylaxis is individualized; albumin, disease type, bleeding risk and other factors matter.
 Biopsy distinguishes active treatable inflammation from irreversible scarring and identifies the lesion; positive serology does not answer every management question.
 Exclude infection and arrange preventive measures before intensive immunosuppression. Do not delay treatment of life-threatening pulmonary–renal disease while waiting for every nonessential result.
 New targeted therapies require current drug-specific eligibility and safety review; older guideline listings are not proof of current regulatory status.'''))],[GN,IGA,('KDIGO lupus nephritis guideline, 2024','https://kdigo.org/guidelines/lupus-nephritis/'),('KDIGO ANCA vasculitis guideline, 2024','https://kdigo.org/guidelines/anca-associated-vasculitis/')])

def sodium():
 write('Nephrology','Sodium Water Balance',[
 S('Hyponatremia: tonicity first',T('Pattern|Meaning','''Hypotonic hyponatremia|True excess water relative to sodium; evaluate urine osmolality and cause
 Hyperglycemic hyponatremia|Water shift from cells lowers measured Na; correct for glucose using the appropriate approach
 Pseudohyponatremia|Selected indirect-assay artifact with very high lipid/protein; direct measurement clarifies
 Urine osmolality ≤100 mOsm/kg|Appropriate water excretion; consider high water intake/low solute intake
 Concentrated urine|Antidiuretic activity persists; assess volume, medicines, cortisol/thyroid and renal function''')),
 S('Causes and treatment by mechanism',T('Cause|Clues|Treatment direction','''Hypovolemia|GI/renal salt loss; low effective circulation|Restore appropriate volume; anticipate water diuresis and rapid Na rise after reversal
 SIAD physiology|Hypotonicity, concentrated urine, compatible urine sodium; exclude cortisol/thyroid/renal and volume causes|Treat trigger; fluid/solute strategy and selected second-line treatment
 HF/cirrhosis|Water retention with low effective arterial circulation|Treat underlying disease and congestion; do not give indiscriminate saline
 Adrenal insufficiency|Cortisol deficiency, possible hypotension; K depends on primary versus central disease|Prompt glucocorticoid treatment when indicated
 Thiazide/low-solute states|Drug/diet history|Stop cause; closely monitor correction''')),
 S('Severe symptoms and overcorrection',U('''Seizure, coma or severe neurological symptoms from hyponatremia: monitored 3% saline boluses using a validated protocol; 100–150 mL bolus strategies differ by guideline.
 Initial aim is a small rise, roughly 4–6 mmol/L, sufficient to relieve dangerous symptoms—not immediate normalization.
 Limit daily correction; high-risk patients generally should not exceed 8 mmol/L in 24 hours. Risk increases with very low Na, alcohol use, malnutrition, hypokalemia and liver disease.
 Monitor Na and urine output frequently. Reversal of the cause can trigger sudden water diuresis; potassium replacement also raises effective sodium correction.
 Excess correction: urgent specialist-directed desmopressin/free-water relowering strategy when indicated. Formulas do not replace repeated measurement.''')),
 S('Hypernatremia and polyuria',T('Finding|Interpretation / action','''Hypernatremia|Water deficit relative to sodium or sodium gain; assess duration, volume and ongoing losses
 Dilute urine despite hypernatremia|Consider central/nephrogenic diabetes insipidus
 Osmotic diuresis|Glucose, urea or other solute-driven loss
 Water deficit estimate|Total body water × (Na/140 − 1); an estimate, not the complete prescription
 Central DI|Desmopressin when appropriate; prevent treatment-induced hyponatremia
 Nephrogenic DI|Treat cause, reduce solute burden and selected diuretic/amiloride strategies''')+U('''Restore circulation first if shocked, then replace water with a planned rate accounting for chronicity and losses.
 Chronic/unknown-duration hypernatremia is generally corrected gradually; acute sodium loading may require a different approach.
 Formal water-deprivation or copeptin-based testing requires a safe specialist protocol; do not dehydrate an already unstable hypernatremic patient.'''))],[NA,('Society for Endocrinology inpatient cranial DI guidance','https://doi.org/10.1530/EC-18-0154')])

def potassium():
 write('Nephrology','Potassium Disorders',[
 S('Hyperkalemia: protect, shift, remove',T('Step|Treatment role|Pitfall','''Confirm and monitor|ECG, repeat nonhemolyzed sample when appropriate; assess renal function/drugs|Do not delay treatment of convincing severe toxicity while waiting for repeat sampling
 Protect myocardium|IV calcium for indicated ECG toxicity/severe presentation|Does not lower serum potassium
 Shift into cells|Insulin–glucose; nebulized beta₂ agonist as adjunct|Transient effect; monitor glucose after insulin and repeat K
 Remove potassium|Dialysis, appropriate binders or renal excretion strategies|Shifting alone leaves total-body potassium unchanged
 Correct cause|AKI, drugs, acidosis, tissue breakdown or impaired aldosterone effect|Rebound can occur after temporary improvement''')+U('''A normal ECG does not exclude dangerous hyperkalemia. Calcium formulation, access and dose must follow the emergency protocol.
 Insulin can cause delayed hypoglycemia, especially with kidney disease; planned serial glucose checks are essential.
 Sodium bicarbonate is not a reliable universal stand-alone hyperkalemia treatment; consider the acid–base setting.
 Severe/refractory hyperkalemia with poor renal clearance may require urgent dialysis.''')),
 S('Find the mechanism',T('Mechanism|Examples','''Reduced renal excretion|AKI/CKD, hypoaldosteronism, RAAS inhibitors, MRAs, trimethoprim and selected other drugs
 Cell release / shift out|Rhabdomyolysis, tumor lysis, insulin deficiency, selected acidoses
 Pseudohyperkalemia|Hemolysis, difficult sampling, marked thrombocytosis/leukocytosis in relevant assays
 Persistent hyperkalemic normal-gap acidosis|Consider type 4 RTA; urine pH may still be low''')),
 S('Hypokalemia: distinguish loss from redistribution',T('Pattern|Likely direction','''Low urine potassium during hypokalemia|Appropriate renal conservation; consider GI loss, low intake or redistribution
 Renal potassium loss|Diuretics, mineralocorticoid excess, tubular disease, magnesium deficiency
 Hypokalemic metabolic alkalosis|Vomiting/diuretics or salt-wasting/mineralocorticoid disorders; use urine chloride and BP
 Hypokalemic normal-gap acidosis|Diarrhea or distal/proximal RTA
 Rapid weakness with redistribution|Insulin/beta-agonist effect or periodic paralysis; total-body deficit may be limited''')+U('''Urine potassium indices depend on intake, urine concentration and renal function; do not use one threshold without its units/context.
 Hypomagnesemia causes refractory renal K wasting; replace magnesium when deficient.
 ECG may show flattened T waves, ST depression and U waves; weakness and arrhythmia risk determine urgency.''')),
 S('Replacement and long-term prevention',U('''Oral potassium is preferred when safe; IV replacement for severe/symptomatic disease, ECG changes or inability to use the gut, with access/rate-specific monitoring.
 Do not give potassium as an IV push. Adjust for renal function and repeated levels.
 Redistribution syndromes can rebound into hyperkalemia when the shift reverses; avoid assuming every low value represents a large total-body deficit.
 Review drugs, constipation, diet and potassium binders in chronic hyperkalemia; preserve indicated kidney/cardiac protective treatment when safely possible.
 Dialysis and insulin change serum K rapidly; monitor for rebound and associated glucose/electrolyte complications.'''))],[K,('Resuscitation Council UK special circumstances, 2025','https://www.resus.org.uk/professional-library/2025-resuscitation-guidelines/special-circumstances-guidelines')])

if __name__=='__main__':aki();ckd();glomerular();sodium();potassium()
