# Cardiology QBank chapter allocation

Names and numbers match the 15 DOCX files in `data/files/Cardiology`.

The redistribution allocated 615 existing questions once each, preserving their IDs, stems, options, answer keys, explanations and references at redistribution. Three subsequent reviewed hypertension revisions retain IDs and answer-letter slots; exact original/revised hashes are recorded in `audit/reviewed-question-revisions.json`. Subsequent authoring has added 98 questions (57 hypertension and 41 ACHD), bringing the current total to 713.

| Chapter | Topic | Authored questions | Draft questions |
|---|---|---:|---:|
| 1 | Cardiovascular Physiology Hemodynamics and Investigations | 53 | 0 |
| 2 | Coronary Artery Disease ACS and Myocardial Infarction | 36 | 0 |
| 3 | Valvular Heart Diseases | 54 | 0 |
| 4 | Heart Failure and Cardiogenic Shock | 41 | 0 |
| 5 | Bradyarrhythmias Conduction Disorders and Pacemakers | 36 | 0 |
| 6 | Supraventricular Tachyarrhythmias and Atrial Fibrillation | 37 | 0 |
| 7 | Ventricular Arrhythmias Sudden Cardiac Death and ICD | 37 | 0 |
| 8 | Cardiomyopathies Myocarditis and Genetic Cardiac Diseases | 56 | 0 |
| 9 | Pericardial Diseases and Cardiac Tamponade | 45 | 0 |
| 10 | Infective Endocarditis | 66 | 65 |
| 11 | Systemic Hypertension and Hypertensive Emergencies | 66 | 0 |
| 12 | Adult Congenital Heart Diseases | 45 | 41 |
| 13 | Aortic Diseases and Peripheral Vascular Diseases | 3 | 0 |
| 14 | Advanced ECG Interpretation and Electrophysiology | 45 | 0 |
| 15 | Cardiovascular Pharmacology Antithrombotic Therapy and Landmark Trials | 93 | 0 |

## Review and installation status

The original 541 installed questions remain released under matching source chapter names. The fully reviewed 66-question hypertension chapter is now installed, bringing Cardiology to 607 installed questions. The 65 original endocarditis draft questions and 41 new ACHD questions remain withheld; chapter 10 also contains one previously installed device-infection question.

Hypertension has 66 reviewed questions: measurement and phenotypes (9), risk-based initiation and targets (6), organ injury and arterial stiffness (2), lifestyle/contributors (4), initial drug selection/adverse effects (8), resistant hypertension (6), secondary causes (13), general emergencies (5), specific emergencies (8) and target trials (5). Release review, documented source checks, source coverage and exact app readback passed. The current coverage ledger is `audit/chapter-11-coverage.json`; release evidence is `audit/chapter-11-release-review.json`. Source-access limitations and the absence of independent clinician peer review remain documented.

All 15 files contain existing questions, but full chapter coverage is incomplete. In particular, chapter 12 has 45 questions (4 existing installed questions and 41 new drafts) against a provisional 55-decision coverage plan, while chapter 13 contains only 3 questions. 612 of the 615 redistributed questions remain verbatim; three hypertension questions have reviewed revisions (two distractor improvements and one ABPM explanation expansion). A full medical deep-dive revision of the other chapter explanations remains pending. Original answer positions are preserved, so redistributed subsets have uneven answer-letter distributions; the completed hypertension bank is balanced at A17/B17/C16/D16.

The original source-review ledgers describe the old authoring groups, not the redistributed chapter coverage. Use `audit/redistribution-report.json` for the original question-by-question allocation and content hashes. It is a historical record of the 615-question redistribution, not a current authoring total. The verified original artifacts are retained in `audit/pre-redistribution.zip`.

Run `python tools/redistribute_cardiology_qbank.py --verify` to check the delivered files. The old individual authoring scripts produce the superseded grouping and should not be run directly over this set.

ACHD authoring is in progress in source order. Its authored cases cover the planned atrial, ventricular and ductal shunt decisions, four coarctation decisions and the congenital outflow/valve section, the five planned TOF decisions, five Eisenmenger decisions, two Ebstein decisions, three transposition decisions, Fontan physiology, protein-losing enteropathy, thromboprophylaxis, liver surveillance and arrhythmia-related deterioration and the preserved flow question. The VSD section explicitly distinguishes the uncertain treat-and-repair benefit from the ASD recommendation. The four transferred questions remain verbatim. See `audit/chapter-12-coverage.json` for the provisional 55-decision plan; a draft count is not a completed chapter.
