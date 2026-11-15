# Cardiology QBank chapter allocation

Names and numbers match the 15 DOCX files in `data/files/Cardiology`.

The redistribution allocated 615 existing questions once each, preserving their IDs, stems, options, answer keys, explanations and references. Subsequent hypertension authoring has added 53 questions, bringing the current total to 668.

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
| 11 | Systemic Hypertension and Hypertensive Emergencies | 62 | 62 |
| 12 | Adult Congenital Heart Diseases | 4 | 0 |
| 13 | Aortic Diseases and Peripheral Vascular Diseases | 3 | 0 |
| 14 | Advanced ECG Interpretation and Electrophysiology | 45 | 0 |
| 15 | Cardiovascular Pharmacology Antithrombotic Therapy and Landmark Trials | 93 | 0 |

## Review and installation status

The 541 previously installed questions are released under the matching source chapter names. The 65 original endocarditis draft questions and 62 current hypertension draft questions remain withheld from the app. Chapter 10 has one previously installed device-infection question in addition to its 65 draft questions. Chapter 11 contains only drafts, so it has a delivered JSON file but no installed bank.

Hypertension has all 62 provisionally planned questions drafted: measurement and phenotypes (9), risk-based initiation and targets (6), lifestyle/contributors (4), initial drug selection/adverse effects (8), resistant hypertension (6), secondary causes (11), general emergencies (5), specific emergencies (8) and target trials (5). Its status is `draft_awaiting_final_review`: final chapter-wide source, coverage and editorial review remains required before installation. The current coverage ledger is `audit/chapter-11-coverage.json`; the original nine-question ledger remains archived.

All 15 files contain existing questions, but full chapter coverage is incomplete. In particular, chapters 12 and 13 contain only 4 and 3 questions respectively. The original explanations are preserved; a medical deep-dive structure revision has not been performed. Answer positions are preserved, so the new chapter subsets have uneven answer-letter distributions.

The original source-review ledgers describe the old authoring groups, not the redistributed chapter coverage. Use `audit/redistribution-report.json` for the original question-by-question allocation and content hashes. It is a historical record of the 615-question redistribution, not a current authoring total. The verified original artifacts are retained in `audit/pre-redistribution.zip`.

Run `python tools/redistribute_cardiology_qbank.py --verify` to check the delivered files. The old individual authoring scripts produce the superseded grouping and should not be run directly over this set.
