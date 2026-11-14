"""Distribute the eight existing GI Word sources into eleven numbered chapters.

Preserve every original body element once using the shared Word package utility.
"""
import argparse
from pathlib import Path
from word_chapter_distribution import run, ROOT, DEFAULT_DATA

SOURCES = [
    'I. GI anatomy and physiology.docx', 'II. Esophageal disorders.docx',
    'III. Stomach.docx', 'IV. IBD.docx', 'V. Malabsorption syndromes.docx',
    'VI. Pancreas.docx', 'VII. Other intestinal disorders.docx',
    'VIII. Question Based Notes.docx',
]
# End positions are exclusive; the final sectPr is retained as page setup.
# Each tuple is source index, start element, end element.
CHAPTERS = [
    ('Esophageal Disorders & GERD', [
        (1, 0, 294), (1, 320, 430), (0, 38, 49), (0, 109, 145)]),
    ('Gastritis, Peptic Ulcer Disease & H. pylori', [
        (2, 0, 80), (2, 95, 309), (0, 235, 301)]),
    ('Upper & Lower Gastrointestinal Bleeding', [
        (7, 0, 195), (7, 207, 226), (1, 294, 320), (2, 80, 95)]),
    ('Malabsorption, Celiac Disease & Chronic Diarrhea', [
        (4, 0, 150), (4, 165, 222), (0, 346, 537),
        (7, 493, 504), (7, 540, 557), (7, 590, 601)]),
    ('Inflammatory Bowel Disease', [(3, 0, 136)]),
    ('Functional GI & Motility Disorders', [
        (0, 31, 38), (0, 49, 109), (6, 372, 394), (6, 440, 480)]),
    ('Acute & Chronic Pancreatitis', [
        (5, 0, 366), (0, 301, 313), (4, 150, 165)]),
    ('Pancreatic Cystic Lesions & Neoplasms', [(6, 282, 312)]),
    ('Biliary Tract Disorders & Cholangitis', [(0, 313, 319), (7, 432, 442)]),
    ('GI Polyps, NETs & GI Malignancies', [
        (6, 0, 282), (6, 312, 372), (7, 226, 432), (7, 442, 455)]),
    ('GI Endoscopy, Imaging & Miscellaneous Disorders', [
        (0, 0, 31), (0, 145, 235), (0, 319, 346), (6, 394, 440),
        (7, 195, 207), (7, 455, 493), (7, 504, 540),
        (7, 557, 590), (7, 601, 635)]),
]

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=Path, default=DEFAULT_DATA)
    parser.add_argument('--output', type=Path, default=ROOT / 'build/gi-distributed')
    parser.add_argument('--install', action='store_true')
    args = parser.parse_args()
    run(args.data.resolve(), args.output.resolve(), 'GI & pancreas', SOURCES, CHAPTERS,
        args.install, content_gaps=[
            'No dedicated pancreatic cystic-lesion material in the eight sources.',
            'No standalone cholangitis discussion in the eight sources.',
        ])
