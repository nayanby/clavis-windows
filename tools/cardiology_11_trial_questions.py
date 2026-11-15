"""Treatment-target trial interpretation for hypertension chapter 11."""
from qbank_json_chapters import question as Q

REFERENCES = {
 'SPRINT': ('SPRINT original randomized trial, 2015', 'https://doi.org/10.1056/NEJMoa1511939'),
 'ACCORD_BP': ('ACCORD-BP randomized trial, 2010', 'https://doi.org/10.1056/NEJMoa1001286'),
 'BPROAD': ('BPROAD intensive BP control in type 2 diabetes, online 2024/print 2025', 'https://doi.org/10.1056/NEJMoa2412006'),
 'STEP': ('STEP intensive BP control in older adults, 2021', 'https://doi.org/10.1056/NEJMoa2111437'),
 'HYVET': ('HYVET hypertension treatment at age 80 or older, 2008', 'https://doi.org/10.1056/NEJMoa0801369'),
 'SPRINT_PROTOCOL': ('SPRINT cohort methods and orthostatic outcomes', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC7261502/'),
 'BPROAD_PROTOCOL': ('BPROAD primary rationale and design', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC10755603/'),
}
TOPIC = 'Landmark treatment-target trials'
rows = []


def S(h, t, *children):
    return h, [(t, list(children))]


def add(*args, **kwargs):
    rows.append(Q(*args, **kwargs))


add(TOPIC, 'SPRINT: Eligibility, Benefits and Adverse Effects',
 'Which patient most closely matches the original SPRINT population for intensive versus standard systolic BP targets? All eGFR values are in mL/min/1.73 m².',
 'A 67-year-old with SBP 152 mmHg and eGFR 48, without diabetes or previous stroke', [
 ('A 67-year-old with SBP 152 mmHg, eGFR 48 and type 2 diabetes', 'Diabetes was excluded from SPRINT, even though CKD could otherwise identify increased cardiovascular risk. Diabetes-specific target evidence comes from trials such as ACCORD-BP and BPROAD rather than direct SPRINT enrollment.'),
 ('A 67-year-old with SBP 152 mmHg, eGFR 48 and a previous stroke', 'Previous stroke was a SPRINT exclusion. Secondary cerebrovascular prevention therefore requires its own evidence and current guidance rather than an assertion that this exact phenotype was randomized in SPRINT.'),
 ('A 45-year-old with SBP 152 mmHg and high estimated cardiovascular risk', 'High risk matters, but SPRINT enrolled adults aged at least fifty. Evidence can inform discussion beyond the trial population, but a forty-five-year-old does not match the original age eligibility.')],
 [S('Population and Targets', '**SPRINT enrolled adults aged at least fifty at increased cardiovascular risk, excluding diabetes and previous stroke.** Eligible CKD included eGFR 20–59 mL/min/1.73 m²; other risk routes included clinical/subclinical CVD, Framingham ten-year risk at least 15% or age at least 75.',
    'The comparison was a systolic target below 120 versus below 140 mmHg. Trial targets require interpretation alongside standardized measurement, achieved pressure and monitoring rather than a direct translation to a rushed office reading.',
    'In the original 2015 report, intensive treatment reduced the primary cardiovascular composite with a hazard ratio of 0.75 and all-cause mortality with a hazard ratio of 0.73. These estimates should not be mixed indiscriminately with those in later follow-up reports.'),
  S('Safety and Clinical Application', '**Benefits came with more selected serious adverse events.** Hypotension, syncope, electrolyte abnormalities and acute kidney injury/failure were more frequent; injurious falls were not significantly increased in the original report.',
    'Choose a feasible regimen and monitor symptoms, standing pressure, renal function and electrolytes. A trial-supported lower target is not an instruction to force a particular number despite poor tolerance.',
    'Consider comorbidity, frailty and competing risks when applying evidence. Do not describe all SPRINT measurements as necessarily unattended, or assume that the same numerical target represents identical pressure exposure under every clinic technique. The appropriate examination inference combines the eligible population, cardiovascular benefit and adverse-event profile. It neither proves an identical benefit in excluded diabetes/stroke populations nor supports withholding effective treatment from every patient outside the trial.')], ['SPRINT', 'SPRINT_PROTOCOL', 'AHA2025', 'ESC2024'])

add(TOPIC, 'ACCORD-BP: Primary Composite and Stroke Result',
 'Which statement best describes the principal ACCORD-BP findings in high-risk type 2 diabetes?',
 'The primary cardiovascular composite was not significantly reduced, while stroke was reduced', [
 ('The primary cardiovascular composite was reduced, while stroke was unchanged', 'This reverses the important ACCORD-BP distinction. The principal composite did not meet statistical significance, whereas the prespecified stroke outcome favored intensive treatment.'),
 ('Neither the primary cardiovascular composite nor stroke was reduced significantly', 'It is correct that the primary composite was not significantly reduced, but the stroke result was significant. Calling the trial uniformly negative discards a clinically relevant secondary finding.'),
 ('The primary cardiovascular composite was unchanged, while stroke increased', 'The first component resembles the primary-result interpretation, but the direction of the stroke finding is wrong. Intensive treatment reduced rather than increased the observed stroke outcome.')],
 [S('Trial Design and Results', '**ACCORD-BP compared systolic targets below 120 and below 140 mmHg in 4733 high-risk adults with type 2 diabetes.** Its primary composite comprised nonfatal MI, nonfatal stroke and cardiovascular death.',
    'The primary hazard ratio was 0.88, with a 95% confidence interval of 0.73–1.06 and P=0.20. This did not establish a statistically significant primary-composite benefit.',
    'Stroke was reduced, with a hazard ratio of 0.59 and P=0.01. The finding should be identified as a secondary outcome rather than relabeled as a positive primary endpoint.'),
  S('Interpretation and Current Practice', '**A nonsignificant primary result is not proof that the two strategies are equivalent.** Precision, event rates, power and the full pattern of benefit and harm matter.',
    'Intensive treatment produced more treatment-attributed serious adverse events. Monitor hypotension, electrolyte effects and kidney function when pursuing a lower target rather than considering the pressure number in isolation.',
    'Do not confuse the BP randomization with ACCORD’s separate intensive-glycemia intervention and its safety findings. Equally, do not treat ACCORD-BP as the final word on all diabetic BP targets: BPROAD subsequently supplied a larger diabetes-specific trial with a positive cardiovascular composite. The studies differ in population, size, background care and endpoint composition, including the handling of heart failure. Current recommendations should synthesize that later evidence while accurately preserving what ACCORD itself did and did not demonstrate. This distinction is more useful than memorizing a label of positive or negative without naming the endpoint.')], ['ACCORD_BP', 'BPROAD', 'AHA2025'],style='direct')

add(TOPIC, 'BPROAD: Intensive BP Control in Type 2 Diabetes',
 'Which statement correctly distinguishes BPROAD from an assumption that ACCORD-BP settled the question against intensive BP control in diabetes?',
 'BPROAD demonstrated a significant reduction in its primary cardiovascular composite', [
 ('BPROAD reproduced a nonsignificant primary composite with only a secondary stroke signal', 'That description more closely resembles the commonly tested ACCORD-BP pattern. BPROAD significantly reduced its specified primary cardiovascular composite.'),
 ('BPROAD evaluated adults without diabetes and therefore supplied only indirect evidence', 'This confuses the population with SPRINT. BPROAD specifically enrolled adults with type 2 diabetes and increased cardiovascular risk.'),
 ('The primary benefit occurred without more symptomatic hypotension or hyperkalemia', 'Overall serious adverse-event rates were similar, but symptomatic hypotension and hyperkalemia were more frequent in the intensive group. Comparable overall safety totals should not be substituted for the results of individual adverse-event categories.')],
 [S('Population, Targets and Outcome', '**BPROAD randomized 12821 high-risk adults aged at least fifty with type 2 diabetes in China to systolic targets below 120 or below 140 mmHg.** It excluded eGFR below 30 mL/min/1.73 m². The report appeared online in 2024 and in the 2025 print publication.',
    'The primary composite included nonfatal stroke, nonfatal MI, treatment or hospitalization for heart failure, and cardiovascular death. It should not be casually renamed a three-point MACE endpoint.',
    'The primary hazard ratio was 0.79, with a 95% confidence interval of 0.69–0.90. Intensive treatment therefore demonstrated a significant benefit for this specified composite.'),
  S('Safety and Application', '**Use the trial to support a monitored treatment strategy in a comparable patient.** It does not establish that an identical target has the same balance of benefit and harm in every person with diabetes.',
    'Symptomatic hypotension and hyperkalemia were more frequent with intensive treatment. Review orthostatic symptoms, kidney function, potassium, adherence and the practical burden of additional drugs.',
    'BPROAD and ACCORD-BP differ in size, population, background care and endpoint composition. A positive composite does not prove that every component was independently significantly reduced. Distinguish the assigned target from achieved average pressure. AHA/ACC 2025 recommends a systolic goal below 130 mmHg in diabetes, with encouragement toward below 120 when appropriate to reduce cardiovascular events; monitor tolerance rather than forcing the lower number in every patient. Diabetes-specific evidence now supports benefit beyond a simple reading of the older ACCORD primary result, while preserving individualized care.')], ['BPROAD', 'BPROAD_PROTOCOL', 'ACCORD_BP', 'AHA2025'],style='direct')

add(TOPIC, 'STEP: Intensive Targets in Older Hypertensive Adults',
 'Which population and target comparison correctly describes STEP?',
 'Chinese adults aged 60–80; SBP 110 to below 130 versus 130 to below 150 mmHg', [
 ('Chinese adults aged 60–80; SBP below 120 versus below 140 mmHg', 'The age/location are compatible, but these are the familiar SPRINT/BPROAD target numbers. STEP compared bounded ranges of 110–<130 and 130–<150.'),
 ('Adults aged at least 80; indapamide-based treatment toward below 150/80 versus placebo', 'This describes the central HYVET population and strategy rather than STEP. Age strata and comparator design must be kept separate.'),
 ('Adults aged 40–59; SBP below 130 versus below 160 mmHg', 'Younger adults require their own risk assessment and evidence interpretation. This age range and target pair were not the STEP randomized comparison.')],
 [S('Trial Design and Findings', '**STEP studied 8511 Chinese adults aged sixty to eighty with hypertension.** It compared a systolic target of 110 to below 130 with a standard range of 130 to below 150 mmHg.',
    'Over a median 3.34 years, the broad primary cardiovascular composite occurred in 3.5% versus 4.6%, with a hazard ratio of 0.74. The composite included stroke, ACS, acute decompensated HF, coronary revascularization, AF and cardiovascular death.',
    'The broad composite is not identical to ACCORD-BP’s three-component endpoint or BPROAD’s endpoint. Keep the event definition attached to the effect estimate.'),
  S('Older-Adult Treatment', '**STEP supports more intensive control in selected ambulatory older adults, with attention to tolerability.** Hypotension was more frequent with the intensive strategy.',
    'The trial does not establish a universal target for an eighty-eight-year-old with substantial frailty, symptomatic orthostasis or limited lifespan. Such patients need individualized goals and monitoring of standing pressure and functional outcomes.',
    'Do not infer that age sixty automatically requires permissive hypertension or that all patients above eighty should receive the lower STEP range. A target interval used for randomization is also not a proof that every value below its lower boundary is safe. Review the patient’s clinical profile, measurement method, medication adverse effects and follow-up capacity when selecting a goal. HYVET and SPRINT add different older-adult evidence, but they cannot be combined into one fictional population or one shared target comparison.')], ['STEP', 'HYVET', 'ESC2024'],style='direct')

add(TOPIC, 'HYVET: Treating Selected Adults Aged Eighty or Older',
 'Which interpretation best matches the main HYVET trial?',
 'Selected adults aged at least 80 benefited from indapamide-based treatment toward below 150/80 mmHg', [
 ('Adults aged at least 80 were randomized between systolic targets below 120 and below 140 mmHg', 'That is an intensive-versus-standard target design resembling SPRINT, not HYVET. HYVET compared active indapamide-based treatment with matching placebo toward a 150/80 target.'),
 ('The principal comparison was indapamide alone against perindopril alone', 'Perindopril could be added to the active regimen, with matching placebo in the comparison group. HYVET was not a direct monotherapy ranking trial between those two drugs.'),
 ('The primary stroke endpoint was significantly reduced while all-cause mortality was unchanged', 'The final main report showed a nonsignificant reduction in fatal/nonfatal stroke at P=0.06, but a significant reduction in all-cause mortality. This option reverses the key significance pattern.')],
 [S('Population and Regimen', '**HYVET enrolled selected adults aged at least eighty with sustained systolic BP at least 160 mmHg.** Treatment began with indapamide sustained release 1.5 mg daily, with perindopril 2–4 mg added when required, versus matching placebo.',
    'The target was below 150/80 mmHg. The trial therefore supports treating important hypertension in suitable very old adults; it was not a direct test of an SBP target below 120.',
    'In the final main analysis, fatal or nonfatal stroke was reduced by about 30% with P=0.06, while all-cause mortality fell by about 21% and HF by about 64%, both significantly. Do not substitute interim or per-protocol significance results for the final primary analysis.'),
  S('Clinical Application and Limits', '**Chronological age alone is not a reason to withhold treatment.** The person’s frailty, standing tolerance, comorbidities, functional status and goals determine how closely a trial strategy can be applied.',
    'Monitor sodium, potassium, kidney function and orthostatic symptoms with an indapamide/RAS-blocker regimen. The chosen drugs have real metabolic and hemodynamic effects even when an elderly population benefited on average.',
    'Do not conclude that HYVET forbids a lower tolerated target under newer guidance, or that its results establish safety in every institutionalized or severely frail patient. The comparison was treatment against placebo in a selected population with substantially elevated pressure. Modern target selection draws on additional studies and patient circumstances. Its enduring examination lesson is that effective BP treatment can benefit suitable octogenarians, while the target, endpoint and eligibility details must remain those of the actual trial.')], ['HYVET', 'AHA2025', 'ESC2024'],style='direct')
