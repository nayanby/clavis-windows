"""Map all existing Hematology Word material into twelve numbered chapters."""
import argparse
from pathlib import Path
from word_chapter_distribution import run, ROOT, DEFAULT_DATA

SOURCES = [
    'I. Hemat basics.docx', 'II. Hypoproliferative anemia.docx',
    'III. Hemolytic anemia.docx', 'IV. Pancytopenia.docx',
    'V. Plasma cell.docx', 'VI. WBCs.docx',
    'VII. Coagulation disorders.docx', 'VIII. Platelet disorders.docx',
    'IX. Diseases of metabolism.docx', 'X. Quesions.docx', 'XI. VTE detailed.docx',
]
CHAPTERS = [
    ('Approach to Anemia, RBC Indices & Iron Disorders', [
        (1, 0, 289), (0, 54, 85), (0, 113, 145),
        (8, 0, 153), (8, 267, 359), (9, 0, 5), (9, 6, 9)]),
    ('Megaloblastic & Other Macrocytic Anemias', [(1, 289, 428)]),
    ('Hemolytic Anemias & Hemoglobin Disorders', [
        (2, 0, 1260), (8, 153, 267), (9, 9, 13)]),
    ('Bone-Marrow Failure, Aplastic Anemia & MDS', [
        (0, 0, 29), (3, 0, 217), (3, 228, 236),
        (1, 428, 586), (5, 544, 712), (9, 13, 14), (9, 15, 19)]),
    ('Myeloproliferative Neoplasms', [
        (5, 228, 544), (7, 180, 192), (9, 14, 15), (9, 24, 26)]),
    ('Acute Leukemias', [(5, 0, 228), (5, 712, 854)]),
    ('Chronic Lymphoid Leukemias & Related Disorders', [
        (5, 854, 983), (5, 1522, 1574), (0, 85, 113)]),
    ('Lymphomas', [(5, 983, 1495), (5, 1509, 1522), (9, 26, 27)]),
    ('Plasma-Cell Disorders & Amyloidosis', [(4, 0, 559), (9, 27, 29)]),
    ('Platelets, Bleeding Disorders & Coagulation', [
        (7, 0, 142), (7, 159, 180), (7, 197, 1086),
        (6, 0, 264), (6, 274, 560), (9, 29, 35), (9, 36, 37)]),
    ('Thrombosis, Thrombophilia & Anticoagulants', [
        (10, 0, 763), (6, 264, 274), (6, 560, 1182),
        (7, 142, 159), (7, 1086, 1160), (9, 35, 36), (9, 37, 40)]),
    ('Transfusion Medicine, Hematologic Emergencies & Stem-Cell Transplantation', [
        (0, 29, 54), (7, 192, 197), (3, 217, 228),
        (5, 1495, 1509), (5, 1574, 1577),
        (9, 5, 6), (9, 19, 24), (9, 40, 46)]),
]

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=Path, default=DEFAULT_DATA)
    parser.add_argument('--output', type=Path, default=ROOT / 'build/hematology-distributed')
    parser.add_argument('--install', action='store_true')
    args = parser.parse_args()
    run(args.data.resolve(), args.output.resolve(), 'Hematology', SOURCES, CHAPTERS,
        args.install, content_gaps=[
            'Transfusion reactions, compatibility and GVHD have limited standalone source coverage.',
            'No dedicated LGL leukemia discussion beyond the existing classification list.',
        ])
