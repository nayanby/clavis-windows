"""Distribute all existing Hepatology Word sections into eleven chapters.

Source ranges refer to complete top-level OOXML body elements. Original prose,
tables and image relationships are preserved; this does not author new material.
"""
import argparse
from pathlib import Path
from word_chapter_distribution import run, ROOT, DEFAULT_DATA

SOURCES = [
    'I. LFT interpretation.docx',
    'II. Hyperbilirubinemia.docx',
    'III. Viral hepatitis.docx',
    'IV. AUD and ALD.docx',
    'V. MASLD, Autoimmune hepatitis & Metabolic Liver Diseases.docx',
    'VI. CLD and cirrhosis.docx',
    'VII. Portal hypertension.docx',
    'VIII. Budd Chiari syndrome.docx',
    'IX. Drug induced liver injury.docx',
    'X. Acute liver failure.docx',
    'XI. Liver abscess.docx',
    'XII. Biliary disease.docx',
    'XIII. Hepatocellular carcinoma.docx',
    'XIV. Liver diseased in pregnancy.docx',
]

CHAPTERS = [
    ('Liver Function Tests, Acute Viral Hepatitis (HAV, HEV) & Acute Liver Failure', [
        (0, 0, 103), (1, 0, 220), (9, 0, 5), (9, 6, 72), (13, 0, 142)]),
    ('Hepatitis B — Serology, Natural History, Treatment & Reactivation', [
        (2, 0, 80), (2, 82, 231)]),
    ('Hepatitis C — Diagnosis, DAAs, Resistance & Special Populations', [
        (2, 231, 481)]),
    ('MASLD, MASH & Alcohol-Associated Liver Disease', [
        (4, 199, 360), (3, 0, 629), (3, 721, 735)]),
    ('Autoimmune Hepatitis, PBC & PSC', [
        (4, 85, 199), (11, 0, 116)]),
    ('Wilson Disease, Hemochromatosis & Alpha-1 Antitrypsin Deficiency', [
        (4, 0, 85), (5, 44, 45), (5, 205, 206)]),
    ('Drug-Induced Liver Injury & Vascular Liver Diseases', [
        (8, 0, 58), (7, 0, 112), (6, 14, 262)]),
    ('Cirrhosis, Portal Hypertension & Variceal Bleeding', [
        (5, 0, 16), (5, 18, 44), (5, 45, 205), (5, 206, 265),
        (5, 273, 321), (5, 373, 401), (5, 436, 450), (5, 464, 537),
        (6, 0, 14), (6, 262, 390), (6, 420, 432), (6, 437, 446),
        (6, 554, 772), (3, 629, 630), (3, 650, 658), (3, 684, 703)]),
    ('Ascites, SBP, HRS-AKI & Hyponatremia', [
        (5, 321, 373), (5, 418, 436),
        (6, 390, 408), (6, 413, 420), (6, 446, 554),
        (3, 630, 650), (3, 664, 684)]),
    ('Hepatic Encephalopathy & Acute-on-Chronic Liver Failure', [
        (5, 401, 418), (5, 16, 18), (9, 5, 6),
        (2, 80, 82), (6, 408, 413), (3, 658, 664)]),
    ('HCC, Cholangiocarcinoma, Other Liver Tumors & Liver Transplantation', [
        (12, 0, 142), (9, 72, 204), (2, 481, 518),
        (5, 265, 273), (5, 450, 464), (6, 432, 437),
        (3, 703, 721), (10, 0, 127)]),
]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=Path, default=DEFAULT_DATA)
    parser.add_argument('--output', type=Path, default=ROOT / 'build/hepatology-distributed')
    parser.add_argument('--install', action='store_true')
    args = parser.parse_args()
    run(args.data.resolve(), args.output.resolve(), 'Hepatology', SOURCES, CHAPTERS,
        args.install, content_gaps=[
            'HAV and HEV are covered within acute liver failure and pregnancy material; no standalone source chapters.',
            'Alpha-1 antitrypsin deficiency has brief etiological and diagnostic source paragraphs only.',
            'ACLF coverage is limited to the existing definitions and disease-specific material.',
        ])
