"""Source-coverage additions; stable IDs are assigned by the chapter builder."""
from qbank_json_chapters import question as Q

TOPIC = 'Hypertension-mediated organ damage'
REFERENCES = {
    'ESC_EMERGENCY_POSITION': ('ESC Council on Hypertension position document: hypertensive emergencies, 2019',
                               'https://academic.oup.com/ehjcvp/article/5/1/37/5079054'),
    'RETINA_CASE': ('Retinopathy in Malignant Hypertension, NEJM clinical image, 2021',
                    'https://doi.org/10.1056/NEJMicm2109500'),
}

rows = [Q(
    TOPIC, 'Hypertensive Retinopathy: Vascular Sclerosis Versus Acute Injury',
    'An adult with newly recognized BP 224/132 mmHg reports blurred vision. Both fundi show arteriolar narrowing, AV nicking, flame-shaped hemorrhages and cotton-wool spots. The optic discs have sharp margins without swelling. Which Keith–Wagener–Barker grade best describes these findings?',
    'Grade III', [
        ('Grade I', 'Grade I describes mild generalized arteriolar narrowing. It would fit early vascular narrowing without the AV-crossing changes and exudative or hemorrhagic lesions present here.'),
        ('Grade II', 'Grade II adds more definite arteriolar narrowing and AV nicking. Those chronic vascular changes are present, but hemorrhages and cotton-wool spots advance this examination beyond grade II.'),
        ('Grade IV', 'Grade IV includes advanced retinal injury together with optic-disc edema. Severe BP and visual symptoms alone do not establish that grade; the stem explicitly documents sharp, unswollen disc margins.')],
    [
        ('Retinal Findings', [(
            '**Hemorrhages and cotton-wool spots distinguish advanced retinal injury from isolated arteriolar sclerosis.** In the named historical classification, their presence without disc edema is grade III.',
            ['Cotton-wool spots reflect focal ischemic injury in the retinal nerve-fiber layer. Flame-shaped hemorrhages follow the superficial nerve-fiber architecture. Hard exudates reflect leakage with lipid deposition.',
             'AV nicking and increased arteriolar light reflex, including copper or silver wiring, chiefly describe vascular wall changes. They do not by themselves prove an acute hypertensive emergency.'])]),
        ('Clinical Assessment and Management', [(
            '**Severe hypertension with acute retinal injury requires urgent evaluation for hypertensive emergency even without optic-disc edema.** Grade III or IV changes must be interpreted with symptom onset, examination quality and alternative retinal disease.',
            ['Repeat BP promptly with appropriate technique while assessing neurological status, renal function, urine findings, ECG and other clinically indicated evidence of acute injury. Check blood count and hemolysis markers if thrombotic microangiopathy is suspected. Ophthalmic assessment helps document the lesions and exclude competing causes.',
             'If an emergency is confirmed, use a monitored setting and controlled titration rather than an abrupt unmonitored fall. In the absence of a disease-specific exception, the AHA 2025 sequence is to reduce systolic pressure by no more than 25% in the first hour, then below 160/100 mmHg over the next two to six hours, followed by cautious further reduction. Stroke, aortic dissection and pregnancy require their specific pathways.',
             'Optic-disc edema is a descriptive finding; the term papilledema strictly denotes edema from raised intracranial pressure. Neurological symptoms or an atypical ocular pattern need evaluation rather than attribution to BP alone. Retinal vein occlusion, diabetic retinopathy and other disorders may also produce hemorrhages or cotton-wool spots. The grading answer here depends on the explicitly supplied hypertensive pattern, not on assuming every retinal hemorrhage has a hypertensive cause.'])]),
    ], ['ESC2024', 'AHA2025', 'ESC_EMERGENCY_POSITION', 'RETINA_CASE'],
    table=(['Keith–Wagener–Barker grade', 'Defining fundus pattern'], [
        ['I', 'Mild generalized arteriolar narrowing'],
        ['II', 'More definite narrowing and AV nicking'],
        ['III', 'Vascular changes plus hemorrhages, cotton-wool spots and/or exudates'],
        ['IV', 'Grade III changes with optic-disc edema'],
    ]),
)]
