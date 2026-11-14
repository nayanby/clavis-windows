"""Author the first replacement chapter; JSON delivery, no remote generation."""
from pathlib import Path
import json, random, re
from html import escape
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'Qbank Rebuild' / 'Neurology'
ROWS = []
REFS = {
 'exam': ('University of Florida: Neurology examination guidelines and teaching resources', 'https://neurology.ufl.edu/education/clerkship-in-neurology/evaluation-forms/'),
 'local': ('California Northstate University: Neurology Clerkship Handbook 2024–2025, localization appendix', 'https://medicine.cnsu.edu/PDFs/clerkships/Neurology_Clerkship_Handbook_2_24_25.pdf'),
 'language': ('Merck Manual Professional: Aphasia, reviewed 2025', 'https://www.merckmanuals.com/professional/neurologic-disorders/function-and-dysfunction-of-the-cerebral-lobes/aphasia'),
 'eye': ('Austrian Society of Neurology: Manual of the Neurological Examination for Neurologists in Training, 2021', 'https://www.oegn.at/wp-content/uploads/2024/03/Die_Neurologische_Untersuchung_en_April2021.pdf'),
 'gaze': ('MSD Manual Professional: Conjugate Gaze Palsies, reviewed 2025', 'https://www.msdmanuals.com/professional/neurologic-disorders/neuro-ophthalmologic-and-cranial-nerve-disorders/conjugate-gaze-palsies'),
 'ino': ('MSD Manual Professional: Internuclear Ophthalmoplegia, reviewed 2025', 'https://www.msdmanuals.com/professional/neurologic-disorders/neuro-ophthalmologic-and-cranial-nerve-disorders/internuclear-ophthalmoplegia'),
 'weak': ('MSD Manual Professional: Weakness', 'https://www.msdmanuals.com/professional/neurologic-disorders/symptoms-of-neurologic-disorders/weakness'),
 'cord': ('AO Foundation: Patient examination—neurological evaluation', 'https://surgeryreference.aofoundation.org/spine/trauma/occipitocervical/further-reading/patient-examination-neurological-evaluation'),
 'brainstem': ('StatPearls: Lateral Medullary Syndrome', 'https://www.ncbi.nlm.nih.gov/books/NBK551670/'),
 'hemicord': ('StatPearls: Brown-Séquard Syndrome', 'https://www.ncbi.nlm.nih.gov/books/NBK538135/'),
}

def add(section, title, stem, answer, distractors, anatomy, examination, implications, refs, table=None):
    assert len(distractors)==3
    ROWS.append(dict(section=section,title=title,question=stem,answer=answer,distractors=distractors,
                     anatomy=anatomy,examination=examination,implications=implications,refs=refs,table=table))

LANG = (['Syndrome','Fluency','Comprehension','Repetition'],[
 ['Broca','Reduced','Relatively preserved','Impaired'],['Wernicke','Fluent','Impaired','Impaired'],
 ['Conduction','Fluent','Relatively preserved','Disproportionately impaired'],['Transcortical motor','Reduced','Relatively preserved','Preserved'],
 ['Transcortical sensory','Fluent','Impaired','Preserved'],['Global','Reduced','Impaired','Impaired']])
VIS = (['Site','Typical field abnormality','Useful qualification'],[
 ['Optic nerve','Ipsilateral monocular loss','Afferent pupillary defect if asymmetric'],['Central chiasm','Bitemporal loss','Crossing nasal retinal fibers'],
 ['Temporal optic radiation','Contralateral superior quadrantanopia','Meyer loop'],['Parietal optic radiation','Contralateral inferior quadrantanopia','May accompany parietal signs'],
 ['Occipital cortex','Contralateral homonymous hemianopia','Macular sparing is supportive, not obligatory']])

add('Higher cortical functions','Conduction Aphasia',
 'A right-handed man speaks fluently and follows multistep commands. Naming is mildly impaired, but repetition of a short sentence produces repeated phonemic errors despite several attempts at correction. Which syndrome best fits?',
 'Conduction aphasia',[
 ('Wernicke aphasia','Appropriate when fluent paraphasic speech accompanies impaired comprehension; relatively intact multistep comprehension argues against it here.'),
 ('Transcortical sensory aphasia','Fluent speech and poor comprehension occur with preserved repetition, often with echolalia; the repetition deficit here is the opposite pattern.'),
 ('Anomic aphasia','Word-finding difficulty dominates while repetition and comprehension remain relatively preserved; it does not explain this disproportionate repetition failure.')],
 'The dominant perisylvian language network links auditory-language representations to speech production. Injury involving the supramarginal region and dorsal language connections can impair phonological repetition without severely disrupting comprehension; a single arcuate-fasciculus lesion is an oversimplified anatomical model.',
 'Assess spontaneous fluency, naming, comprehension, repetition, reading and writing separately. Phonemic substitutions and repeated self-correction support a phonological production disorder; exclude hearing impairment and dysarthria before interpreting repetition.',
 'Abrupt onset warrants urgent stroke assessment and brain imaging. Speech and language rehabilitation addresses communication deficits. Aphasia syndrome labels describe the examination and do not establish the vascular lesion by themselves.', ['language','local'], LANG)

add('Higher cortical functions','Transcortical Motor Aphasia',
 'After an anterior cerebral watershed infarct, a patient has markedly reduced spontaneous speech. She follows commands and repeats complex sentences accurately. Which language syndrome is most likely?',
 'Transcortical motor aphasia',[
 ('Broca aphasia','Nonfluent speech with relatively preserved comprehension is compatible, but repetition is generally impaired; accurate complex repetition favors a transcortical syndrome.'),
 ('Conduction aphasia','Speech is usually fluent and repetition is disproportionately impaired; both features differ from this examination.'),
 ('Global aphasia','Extensive dominant perisylvian injury impairs fluency, comprehension and repetition; intact comprehension and repetition exclude the classic global pattern.')],
 'Dominant frontal regions outside the core perisylvian language network contribute to speech initiation. Anterior watershed or supplementary motor region injury may reduce propositional output while preserving the circuits needed for repetition.',
 'Distinguish reduced verbal initiation from decreased consciousness, severe depression, abulia and motor speech impairment. Demonstrate comprehension using nonverbal responses, and test repetition beyond automatic greetings or counting.',
 'The preserved repetition separates transcortical motor from classic Broca aphasia. Recovery depends on lesion extent and cause; formal language assessment and rehabilitation are useful even when bedside comprehension appears normal.', ['language','local'], LANG)

add('Higher cortical functions','Gerstmann Syndrome',
 'A patient with a small dominant inferior parietal lesion has intact strength and primary sensation. Which additional combination most strongly supports involvement of the angular-gyrus network?',
 'Acalculia, agraphia, finger agnosia and right–left disorientation',[
 ('Alexia, visual anomia, achromatopsia and prosopagnosia','These findings point toward occipitotemporal visual association networks; face recognition often involves right or bilateral ventral temporal regions rather than the classic dominant angular-gyrus tetrad.'),
 ('Constructional apraxia, left neglect, anosognosia and dressing difficulty','These suggest nondominant parietal association dysfunction, particularly spatial attention networks, rather than the dominant symbolic-processing pattern.'),
 ('Abulia, grasp reflex, impaired set shifting and motor impersistence','These favor frontal or frontal-subcortical network dysfunction. Motor impersistence can also accompany right hemispheric disease; the combination is not the angular-gyrus tetrad.')],
 'Gerstmann syndrome describes the association of impaired calculation, writing, finger identification and right–left orientation. The dominant inferior parietal region and its white-matter connections support these learned symbolic operations; the syndrome is not a perfectly specific single-gyrus marker.',
 'Test written calculation, a dictated sentence, identification of named fingers and crossed commands involving right and left. Account for aphasia, education, vision and hand weakness, which can mimic individual components.',
 'A focal cortical constellation strengthens localization beyond isolated arithmetic difficulty. Acute onset requires assessment for ischemia or hemorrhage; progressive dysfunction raises degenerative or structural causes. Do not diagnose the syndrome from acalculia alone.', ['local','exam'])

add('Higher cortical functions','Ideomotor Apraxia',
 'A patient understands a command to demonstrate using a key but produces an incorrect hand posture with either hand. Strength, proprioception and coordination are preserved; actual key use is substantially better. Which deficit is most likely?',
 'Ideomotor apraxia',[
 ('Ideational apraxia','Failure to conceptualize or sequence a multistep activity, such as preparing tea, is more characteristic; this patient mainly cannot translate a familiar gesture into the commanded posture.'),
 ('Limb-kinetic apraxia','Loss of precise independent finger movements is typically evident during actual manipulation as well; substantial improvement with the real object favors ideomotor dysfunction.'),
 ('Optic ataxia','Misreaching toward visual targets from dorsal visual-stream dysfunction is appropriate when visually guided reaching fails; it does not explain a learned symbolic gesture error without a target.')],
 'Praxis requires a stored action representation, transformation into a motor program and intact execution pathways. Dominant parietal-premotor network injury may impair learned gestures in both hands. Callosal disconnection can instead produce predominantly left-hand apraxia.',
 'Ask for gestures to verbal command, imitation, pantomime of tool use and real-object use. Confirm comprehension and exclude weakness, sensory loss, rigidity and cerebellar ataxia. Body-part-as-object errors and spatial or temporal gesture errors are informative.',
 'A command–automatic dissociation supports ideomotor apraxia but is not universal. Occupational therapy evaluates functional consequences. Praxis deficits can accompany stroke or cortical neurodegenerative disease and require interpretation with the rest of the examination.', ['local','exam'])

add('Higher cortical functions','Hemispatial Neglect and Sensory Extinction',
 'Following a right hemispheric stroke, a patient detects a single touch on either hand. With simultaneous bilateral stimulation she reports only the right touch and omits the left half of a cancellation page. What best explains the findings?',
 'Left hemispatial neglect with tactile extinction',[
 ('Left homonymous hemianopia','A retrochiasmal visual deficit can cause missed left visual stimuli, but cannot by itself explain extinction during bilateral tactile stimulation.'),
 ('Left primary somatosensory cortical loss','A primary sensory deficit should affect isolated left stimuli as well; intact single-stimulus detection with competitive suppression is attentional.'),
 ('Left sensory ataxia','Proprioceptive pathway dysfunction causes impaired joint position and visually compensated incoordination, rather than cancellation omissions and bilateral-stimulation extinction.')],
 'Spatial attention depends on distributed frontal, parietal and subcortical networks. Right hemispheric injury commonly causes severe left neglect. Extinction is failure to report a contralesional stimulus specifically when an ipsilesional stimulus competes with it.',
 'Use visual cancellation, line bisection, copying, assessment of personal space and double simultaneous stimulation in more than one modality. Test visual fields and primary sensation separately because neglect and primary deficits can coexist.',
 'Neglect affects safety, mobility, eating and rehabilitation participation. Anosognosia may compound risk. A normal confrontation field examination does not exclude neglect, and a visual field defect does not account for multimodal extinction.', ['local','exam'])

add('Visual pathways and pupils','Meyer Loop Localization',
 'A patient has a congruent right superior quadrantic field defect in both eyes, without an afferent pupillary defect. Which site is most consistent with the field pattern?',
 'Left temporal optic radiation',[
 ('Left parietal optic radiation','Superior optic-radiation fibers in the parietal lobe carry the inferior visual field; their injury more often causes right inferior quadrantanopia.'),
 ('Right temporal optic radiation','Temporal radiation injury affects the opposite superior field; a right lesion would produce a left superior quadrantic defect.'),
 ('Central optic chiasm','Crossing nasal retinal fibers carry temporal fields in both eyes, so a central chiasmal lesion produces a heteronymous bitemporal pattern.')],
 'Inferior retinal fibers represent the superior visual field. After the lateral geniculate body, these fibers sweep anteriorly through the temporal lobe as Meyer loop before reaching the inferior bank of the calcarine cortex.',
 'Map each eye separately to establish a homonymous defect, then use formal perimetry if bedside boundaries are uncertain. Relative afferent pupillary defects are more characteristic of asymmetric retinal or optic-nerve disease, although optic-tract lesions can also cause one.',
 'A quadrantic pattern suggests a pathway segment rather than a unique etiology. Small occipital lesions can mimic optic-radiation defects, so MRI and associated clinical features refine localization; congruity alone should not determine the site.', ['eye','local'], VIS)

add('Visual pathways and pupils','Optic Chiasmal Compression',
 'Progressive visual difficulty is accompanied by a superior bitemporal field defect that respects the vertical meridian. Which structure is most likely being compressed from below?',
 'Central optic chiasm',[
 ('Both optic tracts','Tract lesions each cause contralateral homonymous loss; symmetric selective superior temporal loss is better explained at the crossing chiasmal fibers.'),
 ('Both occipital poles','Occipital-pole injury predominantly affects central vision in homonymous distributions, rather than an early superior bitemporal pattern.'),
 ('Both lateral geniculate bodies','Geniculate lesions cause homonymous defects, sometimes sectoral; they do not preferentially target the crossing nasal retinal fibers.')],
 'Nasal retinal axons cross at the chiasm and carry the temporal visual fields. A sellar mass growing upward can first affect inferior crossing fibers representing the superior temporal quadrants; anatomical variation and tumor geometry modify this classic progression.',
 'Assess visual acuity, color vision, pupils, optic discs and formal fields. Chiasmal compression can cause optic atrophy; normal acuity early in the course does not exclude substantial peripheral field loss.',
 'Dedicated sellar MRI and endocrine evaluation are appropriate when a pituitary-region lesion is suspected. Sudden headache with visual deterioration or ophthalmoplegia raises pituitary apoplexy and requires emergency assessment rather than elective field surveillance.', ['eye','local'], VIS)

add('Visual pathways and pupils','Relative Afferent Pupillary Defect',
 'Both pupils constrict when the right eye is illuminated. When the light is swung to the left eye, both pupils partially dilate. There is no anisocoria. Which abnormality best explains this response?',
 'Left optic-nerve afferent dysfunction',[
 ('Left oculomotor parasympathetic dysfunction','An efferent defect weakens left pupillary constriction regardless of which eye is illuminated and commonly causes anisocoria; it does not make both pupils dilate when the left eye receives light.'),
 ('Right optic-nerve afferent dysfunction','With a right afferent deficit, moving the light from left to right would produce relative bilateral dilation; the direction in this stem localizes to the left.'),
 ('Left sympathetic pathway dysfunction','Horner syndrome causes a small pupil with dilation lag, most conspicuous in darkness; the afferent light signal and consensual constriction remain intact.')],
 'The swinging-flashlight test compares afferent input through each retina and optic nerve. Both pretectal systems project bilaterally to Edinger–Westphal nuclei, so reduced input from one eye produces a relative reduction of constriction in both pupils.',
 'Use similar illumination and duration for each eye while the patient fixates at distance. A relative afferent defect implies asymmetric afferent disease; severe retinal disease can also cause it. Symmetric bilateral optic neuropathy may produce no relative defect.',
 'This response is not itself diagnostic of optic neuritis. Correlate with acuity, color desaturation, visual fields and fundus findings. Distinguish a relative afferent defect from physiological anisocoria and pharmacologic or third-nerve pupillary abnormalities.', ['eye','exam'])

add('Ocular motor and cranial nerves','Internuclear Ophthalmoplegia',
 'On right gaze, the left eye adducts slowly and incompletely while the right eye has abducting nystagmus. Left-eye adduction during near convergence is preserved. Where is the lesion?',
 'Left medial longitudinal fasciculus',[
 ('Left oculomotor fascicle','A fascicular third-nerve lesion can impair adduction, but often also affects vertical movements, eyelid elevation or the pupil; preserved convergence with the characteristic disconjugate pattern favors an internuclear lesion.'),
 ('Right abducens nucleus','A right nuclear lesion prevents conjugate right gaze, including right abduction, rather than allowing right abduction with isolated left adduction weakness.'),
 ('Right medial longitudinal fasciculus','A right MLF lesion impairs right-eye adduction on left gaze; laterality is defined by the adducting eye, not the abducting nystagmus.')],
 'The MLF connects abducens internuclear neurons to the contralateral medial-rectus subnucleus. A left MLF lesion interrupts the signal required for left adduction during right horizontal gaze while leaving the right lateral rectus pathway available.',
 'Look for slowed adducting saccades, abducting nystagmus and associated skew deviation. Convergence is often preserved but may be impaired in some internuclear lesions; it is supportive rather than an obligatory diagnostic requirement.',
 'Bilateral disease in a young adult suggests demyelination, whereas unilateral abrupt disease in an older patient suggests ischemia. Myasthenia can mimic the ocular pattern; variable fatigability and lack of a consistent central pattern prompt reconsideration.', ['ino','gaze'])

add('Ocular motor and cranial nerves','One-and-a-Half Syndrome',
 'Neither eye can look left. On attempted right gaze, only the right eye abducts; vertical movements are preserved. Which combination best localizes the lesion?',
 'Left abducens nucleus and left medial longitudinal fasciculus',[
 ('Left abducens nerve and left oculomotor nerve','This produces a left-eye motor deficit but does not explain failure of the right eye to adduct during left gaze; a pontine conjugate-gaze lesion is needed.'),
 ('Right abducens nucleus and right medial longitudinal fasciculus','This produces the mirror-image syndrome: right gaze palsy with only left abduction remaining.'),
 ('Left frontal eye field and right medial longitudinal fasciculus','A left frontal destructive lesion impairs rightward gaze, and a right MLF lesion impairs right adduction; the resulting directional pattern does not match this left gaze palsy.')],
 'A unilateral dorsal pontine lesion can combine an ipsilateral horizontal gaze palsy with an ipsilateral internuclear ophthalmoplegia. In this case, the left abducens nucleus accounts for absent left gaze, and the left MLF prevents left adduction on right gaze.',
 'Only contralateral abduction remains horizontally. An ipsilateral paramedian pontine reticular formation lesion plus MLF injury can produce a similar bedside syndrome; testing vestibularly driven eye movements helps distinguish premotor from nuclear involvement.',
 'Additional ipsilateral lower-motor-neuron facial weakness suggests extension to the facial fascicle, termed eight-and-a-half syndrome. Assess limb, sensory and cerebellar signs and obtain brainstem imaging; the ocular pattern localizes more precisely than nonspecific diplopia.', ['gaze','ino'])

add('Ocular motor and cranial nerves','Frontal Eye Field Localization',
 'A patient develops right hemiparesis and aphasia with a sustained leftward gaze preference. Which destructive lesion most coherently explains all three findings?',
 'Left frontal hemisphere involving the frontal eye field',[
 ('Right pontine horizontal gaze center','A right pontine lesion can drive gaze left and cause left-sided long-tract weakness, but it does not account for dominant cortical aphasia with right hemiparesis.'),
 ('Right frontal hemisphere involving the frontal eye field','A destructive right frontal lesion typically produces a rightward preference and left weakness; the laterality is reversed.'),
 ('Left pontine horizontal gaze center','A destructive left pontine gaze-center lesion impairs leftward gaze and can cause right weakness, but gaze tends away from the lesion and aphasia is not a pontine sign.')],
 'Each frontal eye field promotes contralateral horizontal saccades via contralateral pontine circuits. An acute destructive left hemispheric lesion reduces rightward drive, allowing a leftward preference toward the injured hemisphere.',
 'Distinguish a preference from a complete gaze palsy. In an appropriate patient, preserved vestibularly driven movements support a supranuclear lesion; never perform oculocephalic maneuvers when cervical spine instability is possible.',
 'An irritative frontal seizure often drives the eyes away from the active focus, unlike the usual destructive pattern. Interpret gaze with awareness, motor signs and language; exceptions occur, especially with seizures or extensive posterior-fossa lesions.', ['gaze','local'])

add('Ocular motor and cranial nerves','Abducens Nuclear Versus Nerve Lesions',
 'A small pontine lesion causes failure of both eyes to turn right. Which additional finding most strongly supports right abducens nuclear involvement rather than an isolated right sixth-nerve lesion?',
 'Failure of left-eye adduction during attempted right gaze',[
 ('Horizontal diplopia worse at distance','Typical of lateral-rectus weakness from a sixth-nerve lesion as well; it does not establish injury to the internuclear neurons.'),
 ('Right esotropia in the primary position','An isolated right sixth-nerve palsy can cause esotropia, so this cannot distinguish nuclear from peripheral involvement.'),
 ('Impaired right-eye abduction','Both a nuclear lesion and a sixth-nerve lesion interrupt right lateral-rectus activation; the contralateral medial rectus distinguishes the conjugate-gaze disorder.')],
 'The abducens nucleus contains motor neurons to the ipsilateral lateral rectus and internuclear neurons that cross and ascend in the opposite MLF to the medial rectus. Nuclear injury therefore impairs both eyes during ipsilateral gaze.',
 'An isolated sixth-nerve palsy causes ipsilateral abduction weakness with preserved contralateral adduction. A PPRF lesion can also impair ipsilateral voluntary horizontal gaze; vestibular testing and adjacent findings help refine the distinction.',
 'The facial fascicle loops around the abducens nucleus, so an associated ipsilateral peripheral facial palsy supports a dorsal pontine lesion. An isolated nerve palsy can instead occur along the cisternal, cavernous-sinus or orbital course, including as a false-localizing sign of raised intracranial pressure.', ['gaze','exam'])

add('Ocular motor and cranial nerves','Trochlear Nerve Palsy',
 'Vertical diplopia is worse while reading and descending stairs. The right eye is hypertropic, with greater deviation on left gaze and right head tilt. Which muscle is weak?',
 'Right superior oblique',[
 ('Right inferior rectus','Weakness can impair depression, especially in abduction; the adducted-eye and ipsilateral-head-tilt pattern favors superior oblique dysfunction.'),
 ('Left superior oblique','A left fourth-nerve palsy gives left hypertropia, typically worse on right gaze and left tilt; it is the mirror pattern.'),
 ('Left superior rectus','Weakness can make the right eye appear hypertropic, but the gaze and tilt pattern here identifies impaired right superior-oblique depression and intorsion.')],
 'The superior oblique intorts the globe and depresses the adducted eye. Trochlear palsy produces vertical or torsional diplopia that is troublesome on downgaze. Patients commonly compensate by tilting the head away from the affected side.',
 'The three-step pattern supports the diagnosis but is imperfect: skew deviation, restrictive orbital disease and longstanding strabismus can mimic it. Look for torsion, an old head tilt in photographs, and measurements in several gaze positions.',
 'The fourth nerve exits dorsally and its fibers cross before exiting, so a trochlear nuclear lesion affects the contralateral superior oblique, whereas a peripheral nerve lesion affects the ipsilateral muscle. Trauma may produce bilateral palsies.', ['eye','exam'])

add('Ocular motor and cranial nerves','Central and Peripheral Facial Weakness',
 'A patient has right lower facial weakness with preserved forehead wrinkling and strong eye closure, accompanied by right arm weakness and an extensor plantar response. Which site is most likely?',
 'Left supranuclear corticobulbar pathway',[
 ('Right facial nerve at the stylomastoid foramen','A peripheral lesion usually weakens the whole ipsilateral face, including forehead and eye closure; it does not produce a right pyramidal limb pattern.'),
 ('Right facial nucleus in the pons','A nuclear lesion gives ipsilateral upper and lower facial weakness and may accompany contralateral limb signs, unlike the same-sided face–arm pattern here.'),
 ('Left facial nucleus in the pons','This would weaken the left whole face, potentially with right long-tract deficits; the facial laterality and forehead sparing do not match.')],
 'Upper facial motor neurons receive substantial bilateral corticobulbar input, whereas the lower face is more strongly driven contralaterally. A left supranuclear lesion therefore usually weakens the right lower face more than the forehead.',
 'Compare eyebrow elevation, tight eye closure, showing teeth and cheek inflation. Forehead sparing is a useful pattern, not an absolute rule: partial peripheral palsy and some central lesions can blur it. Examine limbs and speech before labeling an acute facial palsy.',
 'Same-sided lower facial and limb pyramidal weakness suggests a contralateral hemispheric lesion. Crossed whole-face and limb weakness points to the pons. Sudden onset requires urgent stroke evaluation even when facial weakness is the most obvious complaint.', ['exam','local'])

add('Ocular motor and cranial nerves','Corneal Reflex Localization',
 'Touching the right cornea produces no blink in either eye. Touching the left cornea produces bilateral blinking. Facial movements are symmetric. Which limb of the reflex is most likely impaired?',
 'Right ophthalmic trigeminal afferent',[
 ('Right facial efferent','The right eye would fail to blink regardless of which cornea was stimulated, while the left eye could still blink with right-corneal stimulation.'),
 ('Left ophthalmic trigeminal afferent','This reverses the pattern: left-corneal stimulation would fail to trigger either eye, whereas the right stimulus would produce bilateral blinking.'),
 ('Left facial efferent','The left eye would fail to close after either stimulus; preserved bilateral closure after left stimulation excludes a major left efferent defect.')],
 'Corneal sensation travels through the nasociliary branch of V1 to trigeminal brainstem circuits. Interneurons activate both facial nuclei, and facial nerves close the eyelids through orbicularis oculi. Each stimulus therefore tests one afferent limb and two efferent limbs.',
 'Approach from the side and stimulate the cornea gently with an appropriate fine wisp, avoiding a visually triggered menace response. Contact-lens use, topical anesthesia and corneal disease can reduce sensitivity without a central lesion.',
 'Interpret the direct and consensual responses together. Symmetric voluntary facial movement and bilateral closure from the left stimulus demonstrate functioning facial efferents here. An absent corneal reflex in reduced consciousness needs medication and ocular-surface context.', ['exam','eye'])

add('Ocular motor and cranial nerves','Bulbar and Pseudobulbar Palsy',
 'Progressive dysarthria and dysphagia are associated with a brisk jaw jerk, a slow stiff tongue without atrophy, and involuntary laughing unrelated to mood. Which localization best fits?',
 'Bilateral corticobulbar pathways',[
 ('Bilateral hypoglossal nuclei','Lower-motor-neuron tongue weakness causes wasting and fasciculations; it does not account for a brisk jaw jerk and spastic bulbar pattern.'),
 ('Bilateral vagal motor nuclei','Nucleus ambiguus disease causes flaccid palatal and laryngeal weakness, but does not explain corticobulbar jaw hyperreflexia or a stiff nonatrophic tongue.'),
 ('Bilateral facial nerves','This chiefly affects facial expression and eye closure; it does not explain tongue spasticity, jaw hyperreflexia and swallowing dysfunction together.')],
 'Pseudobulbar palsy reflects bilateral upper-motor-neuron dysfunction affecting bulbar motor control. Speech is often slow and strained, tongue movements are limited without early denervation wasting, and the jaw jerk may be exaggerated.',
 'Contrast bulbar lower-motor-neuron disease, where speech may be nasal or breathy with tongue atrophy and fasciculation. Emotional lability supports a central network disorder but is not specific to one etiology; a normal gag does not establish safe swallowing.',
 'Assess aspiration risk and obtain formal swallowing evaluation when indicated. Causes include bilateral vascular injury, demyelination and motor neuron disease. ALS can combine bulbar and pseudobulbar signs, so mixed findings should not be forced into a single pure category.', ['exam','local'])

add('Motor system and reflexes','Pyramidal Weakness and Acute Hypotonia',
 'Two hours after a hemispheric infarct, a patient has severe contralateral weakness with reduced tone and depressed tendon reflexes. Which interpretation is most accurate?',
 'An acute upper-motor-neuron lesion can initially be hypotonic and hyporeflexic',[
 ('The findings establish a peripheral motor lesion','Areflexia and hypotonia suggest peripheral disease in many contexts, but immediately after a major central lesion these findings can occur before spasticity develops.'),
 ('A normal plantar response excludes corticospinal injury','The extensor response may be absent early or difficult to elicit; a single plantar examination cannot exclude a central lesion in a coherent acute syndrome.'),
 ('Spasticity must appear before weakness in a central lesion','Weakness may be immediate, while hyperreflexia and velocity-dependent hypertonia evolve later; the chronology in this option is reversed.')],
 'Chronic corticospinal or related descending motor-pathway injury commonly produces loss of dexterity, pyramidal weakness, hyperreflexia and an extensor plantar response. The acute stage may instead show transient flaccidity and depressed reflexes.',
 'Interpret tone and reflexes in relation to onset, distribution, cortical signs and imaging. Compare proximal and distal power, rapid finger movements, pronator drift and plantar responses. Pain, sedation and reduced cooperation can alter apparent strength.',
 'Central localization should not be rejected because the classic spastic pattern has not yet emerged. Serial examination documents evolution; urgent imaging and stroke management depend on the acute syndrome rather than waiting for hyperreflexia.', ['weak','exam'])

add('Motor system and reflexes','MRC Muscle Power Grading',
 'A patient completes the full range of knee extension against gravity but cannot sustain any additional resistance from the examiner. Which MRC grade is most appropriate?',
 'Grade 3',[
 ('Grade 2','Full movement is possible only with gravity eliminated; this patient succeeds against gravity.'),
 ('Grade 4','Movement against gravity and additional resistance is required. The amount of resistance tolerated is reduced compared with normal, but it is more than demonstrated here.'),
 ('Grade 5','Normal power against expected resistance is required; unresisted antigravity movement alone cannot be graded normal.')],
 'The Medical Research Council scale grades observed voluntary strength rather than muscle tone or endurance. Grade 0 is no contraction, 1 a visible or palpable contraction without movement, 2 movement with gravity eliminated, 3 antigravity movement, 4 movement against resistance, and 5 normal strength.',
 'Stabilize the proximal joint, test the intended action through an appropriate range and compare sides. Joint pain, contracture, comprehension and effort affect results; document these limitations rather than assigning an unjustifiably precise neurological grade.',
 'Grade 4 covers a broad range and is relatively examiner dependent. Functional tasks, dynamometry where available and repeated standardized testing improve follow-up. The scale is ordinal: the difference between grades 2 and 3 is not equivalent to that between 4 and 5.', ['weak','exam'], (['Grade','Observed performance'],[['0','No contraction'],['1','Contraction without movement'],['2','Movement with gravity eliminated'],['3','Movement against gravity'],['4','Movement against added resistance'],['5','Normal power']]))

add('Motor system and reflexes','Spasticity Versus Rigidity',
 'During passive elbow movement, resistance increases when the examiner moves the joint rapidly, with a catch followed by release. Which description is most accurate?',
 'Velocity-dependent spasticity',[
 ('Lead-pipe rigidity','Rigidity is relatively independent of movement velocity and persists through the range, often affecting flexors and extensors; it does not produce the characteristic speed-dependent catch.'),
 ('Paratonia','Variable resistance depends on attention and the examiner’s force and may occur with frontal cognitive dysfunction; it is less stereotyped than a reproducible velocity-dependent catch.'),
 ('Fixed contracture','Structural shortening limits passive range even at slow speed; it should not be inferred when the defining feature is a speed-related catch with release.')],
 'Spasticity is a velocity-dependent increase in stretch-reflex resistance within the upper-motor-neuron syndrome. The clasp-knife phenomenon describes a catch followed by reduced resistance; weakness and impaired selective control may be more disabling than tone itself.',
 'Move the relaxed limb at slow and faster speeds, noting joint position, pain, range and distribution. Parkinsonian rigidity is relatively uniform through the range; superimposed tremor can give cogwheeling, and activation of the opposite limb can accentuate it.',
 'Treatment is guided by functional impairment, pain, hygiene and contracture risk, not merely the presence of increased tone. Physical measures and selected focal or systemic therapy require assessment of strength because reducing tone can worsen function in some weak patients.', ['weak','exam'])

add('Motor system and reflexes','Reflex Arcs and Root Localization',
 'Neck pain radiates down the middle finger. Elbow extension and finger extension are weak, and the triceps reflex is reduced. Which root is most likely affected?',
 'C7',[
 ('C6','C6 disease more often affects elbow flexion or wrist extension, the thumb-side sensory territory and biceps or brachioradialis reflexes; the triceps–middle-finger pattern favors C7.'),
 ('C8','C8 disease typically emphasizes finger flexion and ulnar-side hand symptoms; an isolated reduced triceps reflex with elbow-extension weakness is more consistent with C7.'),
 ('T1','T1 contributes strongly to intrinsic hand function and medial forearm sensation; it does not best explain the proximal extensor and triceps-reflex pattern.')],
 'A radicular syndrome combines myotomal weakness, a compatible sensory or pain distribution and a segmentally reduced reflex. C7 commonly contributes to triceps and finger extensors, although individual muscles have overlapping root supply.',
 'Compare muscles supplied by different peripheral nerves but sharing the suspected root. Test wrist flexion and pronation as well as radial-innervated extensors; sensory mapping alone is less reliable because dermatomes overlap.',
 'Biceps and brachioradialis reflexes assess mainly C5–C6, triceps mainly C7, patellar mainly L3–L4 and ankle mainly S1. Progressive weakness or myelopathic signs warrants prompt cervical imaging; a root label should not obscure concomitant cord compression.', ['exam','local'])

add('Sensory pathways and spinal localization','Brown-Séquard Pattern',
 'A right T8 cord hemisection is followed by right leg pyramidal weakness and loss of right leg vibration and position sense. Which additional deficit is expected below the lesion?',
 'Left pain and temperature loss beginning approximately one to two segments lower',[
 ('Right pain and temperature loss throughout the leg','Below the segmental zone, pain and temperature have already crossed and ascend contralaterally; a right hemicord lesion therefore mainly affects left-sided spinothalamic sensation.'),
 ('Left vibration and position loss throughout the leg','Dorsal-column fibers remain uncrossed within the cord and cross in the medulla, so a right cord lesion affects right-sided vibration and joint position.'),
 ('Bilateral sacral sensory loss with preserved leg sensation','A selective saddle pattern suggests conus or cauda equina involvement; it does not follow the tract anatomy of a thoracic hemisection.')],
 'Below a hemicord lesion, the corticospinal tract and dorsal columns produce ipsilateral motor and proprioceptive deficits. Pain-temperature fibers cross through the anterior white commissure after a short segmental course, creating contralateral spinothalamic loss.',
 'At the lesion level, segmental lower-motor-neuron and sensory abnormalities may coexist. The pain-temperature level may be offset by approximately one to two segments and is not a precise ruler for the vertebral lesion level; incomplete syndromes are common.',
 'Urgent spinal MRI is necessary when acute compression is possible. Trauma, tumor, inflammatory lesions and other causes can produce a Brown-Séquard-plus pattern. Document bladder function and sacral examination rather than assuming they are preserved.', ['hemicord','cord'])

add('Sensory pathways and spinal localization','Anterior Cord Syndrome',
 'After thoracoabdominal aortic surgery, a patient develops acute paraplegia, urinary retention and loss of pinprick below T10. Toe position sense and vibration are relatively preserved. Which cord syndrome is most likely?',
 'Anterior cord syndrome',[
 ('Posterior cord syndrome','This primarily compromises vibration, position sense and sensory balance, while relatively sparing pain-temperature and motor tracts; the modality pattern here is reversed.'),
 ('Central cord syndrome','A cervical central cord syndrome classically causes greater arm than leg weakness, sometimes with sacral sparing; isolated postoperative thoracic paraplegia with dorsal-column preservation fits anterior cord dysfunction.'),
 ('Brown-Séquard syndrome','A hemicord pattern is asymmetric, with ipsilateral motor/proprioceptive and contralateral pain-temperature abnormalities; this patient has bilateral motor and spinothalamic loss.')],
 'Anterior cord dysfunction involves corticospinal and anterolateral pathways while relatively sparing dorsal columns. Anterior spinal arterial compromise is an important cause, particularly after aortic procedures; the clinical syndrome does not prove a particular artery is occluded.',
 'Early flaccidity and areflexia can reflect spinal shock. Assess a sensory level, sacral sensation, sphincters and evolution of plantar responses. Relative dorsal-column preservation is a classical clue but may be incomplete in real infarction.',
 'Acute postoperative myelopathy needs emergency evaluation to exclude compressive hematoma and identify perfusion-related injury. MRI can initially be nondiagnostic in cord ischemia; persistent clinical suspicion warrants specialist-directed reassessment rather than dismissal after an early normal scan.', ['cord','local'])

add('Sensory pathways and spinal localization','Syringomyelic Dissociated Sensory Loss',
 'A patient has bilateral loss of pain and temperature over the shoulders and upper arms, preserved vibration, and wasting of intrinsic hand muscles. Which structure is affected earliest in the classic sensory pattern?',
 'Crossing spinothalamic fibers in the anterior white commissure',[
 ('Bilateral dorsal columns','These carry vibration and joint position, which remain preserved; their dysfunction produces sensory ataxia rather than selective pain-temperature loss.'),
 ('Bilateral lateral spinothalamic tracts','Established lateral tract injury produces contralateral pain-temperature loss below the lesion, rather than the initial suspended segmental pattern from central crossing-fiber injury.'),
 ('Bilateral dorsal root ganglia','Ganglionopathy commonly affects several sensory modalities and may be patchy or non-length-dependent; it does not selectively explain central cord hand wasting and cape-like pain-temperature loss.')],
 'A central cervical cavity can damage decussating pain-temperature fibers before reaching the dorsal columns. This produces suspended, dissociated sensory loss in involved segments. Extension into anterior horns accounts for segmental hand wasting and weakness.',
 'Examine pain-temperature and vibration-position separately; a cotton-wool screen alone can miss the dissociation. Map the upper and lower boundaries and look for long-tract leg signs, scoliosis and craniovertebral-junction features.',
 'MRI defines the cavity and associated causes, including Chiari malformation, tumor or prior trauma. Classic bilateral cape distribution is helpful but neither universal nor necessary; eccentric cavities can cause asymmetric symptoms and more complex cord syndromes.', ['cord','local'])

add('Sensory pathways and spinal localization','Sensory Ataxia and Romberg Testing',
 'A patient stands steadily with feet together and eyes open but sways markedly after eye closure. Toe position sense is impaired; heel–shin performance improves while watching the leg. Which mechanism best explains the imbalance?',
 'Loss of proprioceptive input',[
 ('Cerebellar hemispheric incoordination','Dysmetria typically persists with visual guidance; closing the eyes may worsen any imbalance, but striking visual compensation with impaired position sense favors sensory ataxia.'),
 ('Cerebellar vermian dysfunction','Truncal ataxia is usually evident even with eyes open; it does not account for the measured proprioceptive deficit and visual compensation.'),
 ('Frontal gait initiation failure','Difficulty initiating steps, short steps and impaired postural control suggest frontal gait dysfunction; the eye-closure dependence and position loss require a sensory explanation.')],
 'Balance integrates vision, vestibular signals and proprioception. When proprioception is impaired, vision can compensate until the eyes close. A positive Romberg sign therefore tests dependence on visual input rather than directly diagnosing cerebellar disease.',
 'Guard the patient against falling. A meaningful positive test requires relative stability with eyes open and clear deterioration with eye closure. Vestibular dysfunction can also produce a positive Romberg response; the abnormal joint-position examination identifies the sensory component here.',
 'Localize further using reflexes, sensory distribution and central signs: large-fiber neuropathy, sensory neuronopathy and dorsal-column disease are major possibilities. A stamping gait and pseudoathetosis support deafferentation, whereas nystagmus and dysarthria suggest additional cerebellar or vestibular involvement.', ['exam','local'])

add('Sensory pathways and spinal localization','Cortical Sensory Dysfunction',
 'With eyes closed, a patient detects touch, pinprick and finger movement normally but cannot identify a key placed in the right hand or a number traced on that palm. Language and attention are intact. Which site is most likely?',
 'Left parietal sensory association cortex',[
 ('Right parietal sensory association cortex','Cortical sensory processing is predominantly contralateral; a right lesion would more directly impair left-hand stereognosis and graphesthesia.'),
 ('Right median nerve','A median neuropathy causes abnormalities in its peripheral sensory distribution and cannot selectively abolish whole-hand object recognition with intact primary modalities.'),
 ('Left dorsal columns in the cervical cord','A left dorsal-column lesion affects ipsilateral proprioception and vibration, especially on the left, rather than isolated right cortical discrimination with normal position sense.')],
 'Stereognosis integrates shape, texture and spatial information to identify an object by touch. Graphesthesia identifies traced symbols. Impairment despite intact primary sensation supports contralateral parietal cortical or related network dysfunction.',
 'First ensure adequate touch and position input, preserved cognition, comprehension and familiarity with the object or symbol. Compare hands and include sensory extinction and two-point discrimination when useful; poor performance without these prerequisites is not reliably cortical.',
 'Differentiate astereognosis from failure to name a recognized object because of aphasia. Ask the patient to match or demonstrate the object’s use when language is uncertain. Cortical sensory signs can accompany a small parietal infarct even without obvious weakness.', ['exam','local'])

add('Brainstem and cerebellar localization','Lateral Medullary Syndrome',
 'Sudden vertigo, hoarseness and dysphagia accompany right facial pain-temperature loss, left body pain-temperature loss, right ptosis and miosis, and right limb ataxia. Where is the lesion?',
 'Right lateral medulla',[
 ('Right medial medulla','Medial medullary injury classically combines contralateral weakness and dorsal-column modality loss with ipsilateral tongue weakness; nucleus-ambiguus and crossed pain-temperature findings favor the lateral region.'),
 ('Right lateral caudal pons','Lateral pontine disease can cause crossed sensory findings and ataxia, but prominent ipsilateral whole-face weakness or auditory involvement is more typical than the nucleus-ambiguus dysphagia–hoarseness pattern.'),
 ('Left lateral medulla','This would reverse the facial sensory, Horner and cerebellar laterality; the ipsilateral cranial and cerebellar findings identify the right side.')],
 'The pattern combines spinal trigeminal tract/nucleus involvement, contralateral spinothalamic dysfunction, descending sympathetic injury, inferior cerebellar pathway dysfunction and nucleus ambiguus involvement. Vertebral or PICA territory ischemia is a common cause.',
 'Examine voice, palate, cough and swallowing, not just limb power. Classic lateral medullary lesions may spare corticospinal pathways, so preserved strength does not imply a benign vestibular disorder. Horner syndrome may be subtle.',
 'Urgent stroke evaluation and brainstem-sensitive imaging are required. Assess swallowing before oral intake because aspiration can be clinically important. AICA-territory lateral pontine disease is more strongly associated with facial paralysis and auditory symptoms, though vascular syndromes overlap.', ['brainstem','local'])

add('Brainstem and cerebellar localization','Medial Medullary Syndrome',
 'A patient has left hemiparesis, impaired left vibration and joint position sense, and a tongue that deviates right on protrusion. Facial strength is preserved. Which site best explains the findings?',
 'Right medial medulla',[
 ('Right lateral medulla','Lateral medullary injury typically gives crossed pain-temperature loss, dysphagia, Horner syndrome and ataxia; the pyramidal–medial lemniscal–hypoglossal combination is medial.'),
 ('Left medial medulla','This would produce right body deficits and left hypoglossal weakness, reversing the stated laterality.'),
 ('Right posterior limb of the internal capsule','A capsular lesion can cause left sensorimotor deficits but does not produce right lower-motor-neuron tongue weakness from hypoglossal involvement.')],
 'A medial medullary lesion can involve the pyramid before corticospinal decussation, the medial lemniscus after sensory decussation, and ipsilateral hypoglossal fascicles. This creates contralateral weakness and proprioceptive loss with ipsilateral tongue weakness.',
 'The tongue deviates toward its weak side when protruded in a lower-motor-neuron lesion; atrophy and fasciculations may appear later. Compare facial movement and pain-temperature sensation to determine whether adjacent structures are involved.',
 'The classic triad may be incomplete. Arterial supply includes anterior spinal and vertebral paramedian branches, with anatomical variability. MRI and vascular investigation determine cause; syndrome recognition supports localization but should not delay acute stroke care.', ['local','exam'])

add('Brainstem and cerebellar localization','Cerebellar Hemisphere Localization',
 'A patient has right-sided finger–nose dysmetria, intention tremor and dysdiadochokinesia. Joint position sense and strength are normal, and visual guidance does not correct the errors. Which region is most likely affected?',
 'Right cerebellar hemisphere',[
 ('Left cerebellar hemisphere','Cerebellar limb signs are usually ipsilateral because of the organization and crossings of input and output pathways; this would more directly affect the left limbs.'),
 ('Right dorsal columns','Deafferentation can produce incoordination, but position sense is impaired and visual guidance helps; both discriminators are absent here.'),
 ('Left primary motor cortex','A motor cortical lesion can impair dexterity, but weakness, pyramidal signs and slowed movements are more expected than an isolated ipsilateral cerebellar constellation.')],
 'Cerebellar hemispheres regulate timing, scaling and error correction of ipsilateral limb movements. Dysmetria is inaccurate movement amplitude; intention tremor increases near a target, and dysdiadochokinesia reflects irregular rapid alternating movements.',
 'Test finger–nose, heel–shin, rapid alternating movement and rebound carefully, accounting for weakness, pain and visual impairment. Vermian disease produces more axial and gait dysfunction, while vestibulocerebellar disease emphasizes balance and ocular findings.',
 'Acute cerebellar signs warrant urgent posterior-fossa evaluation. Headache, vomiting, declining consciousness or cranial nerve signs may indicate mass effect or hydrocephalus. Apparent limb ataxia alone does not determine whether the cause is infarction, hemorrhage, tumor, inflammation or toxicity.', ['exam','local'])

add('Peripheral localization','Common Fibular Neuropathy Versus L5 Radiculopathy',
 'Foot drop follows prolonged leg crossing. Dorsiflexion and eversion are weak, but inversion and hip abduction are preserved. Sensation is reduced over the dorsum of the foot. Which site is most likely?',
 'Common fibular nerve at the fibular neck',[
 ('L5 nerve root','L5 radiculopathy can cause foot drop, but often also weakens tibialis posterior inversion and gluteus medius hip abduction, which use different nerves and are spared here.'),
 ('Sciatic nerve in the thigh','A substantial sciatic lesion commonly affects tibial-division actions or plantar sensation as well; the selective fibular pattern and compression history favor the fibular neck.'),
 ('Deep fibular nerve at the ankle','A distal deep branch lesion affects short toe extensors or first-web-space sensation, while sparing ankle dorsiflexors whose branches arise proximally and sparing superficial-branch eversion.')],
 'The common fibular nerve is vulnerable where it winds around the fibular neck. Its deep branch supplies dorsiflexors and its superficial branch supplies evertors. Tibialis posterior inverts through the tibial nerve, providing an L5 action outside the fibular territory.',
 'Test dorsiflexion, toe extension, eversion, inversion, plantar flexion and hip abduction. Sensory borders overlap and may be incomplete. A reduced fibular motor response or conduction block across the fibular head helps establish peripheral localization.',
 'Needle EMG sampling of nonfibular L5 muscles and paraspinals helps assess radiculopathy; normal distal sensory responses favor a preganglionic root lesion but are not an absolute rule. Remove pressure and assess orthotic needs; progressive or unexplained deficits require further investigation.', ['local','exam'])

add('Peripheral localization','Preganglionic Versus Postganglionic Sensory Lesions',
 'A patient has C8–T1-distribution weakness and numbness. Ulnar and medial antebrachial cutaneous sensory nerve action potentials are reduced, while sampled cervical paraspinal muscles are normal. Which localization is favored?',
 'Lower-trunk brachial plexopathy',[
 ('C8–T1 radiculopathy','A typical root lesion proximal to the dorsal-root ganglion preserves distal sensory action potentials. Paraspinal denervation would support a root lesion, although a normal sample does not exclude it.'),
 ('Ulnar neuropathy at the elbow','This can reduce ulnar responses and weaken ulnar muscles, but does not account for medial antebrachial cutaneous abnormalities, which arise through a separate terminal nerve.'),
 ('Cervical anterior horn disease','A pure anterior horn process is motor and preserves sensory action potentials; reduced responses in two sensory nerves point to a postganglionic sensory-motor lesion.')],
 'The sensory neuron cell body lies in the dorsal-root ganglion. Lesions proximal to it usually leave the distal sensory axon and recorded SNAP intact; plexus or peripheral nerve lesions are postganglionic and can reduce distal sensory responses.',
 'Use a pattern across several nerves and muscles rather than one low amplitude. Age, temperature, technical factors and coexisting neuropathy can reduce responses. A normal paraspinal sample has limited sensitivity and does not independently exclude radiculopathy.',
 'Lower-trunk disease affects C8–T1 fibers distributed through more than one terminal nerve. Pain, Horner syndrome or a mass warrants targeted evaluation of the plexus and thoracic inlet. Electrodiagnosis establishes physiological distribution; imaging and clinical context establish the cause.', ['local','exam'])

def rich(s):
    return re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',escape(s))

def build():
    assert len(ROWS)==30, len(ROWS)
    direct={3:'Which combination constitutes the classic Gerstmann syndrome?',
      12:'Which finding distinguishes a right abducens nuclear lesion from an isolated right sixth-nerve lesion?',
      16:'Spastic bulbar weakness, a brisk jaw jerk and a slow nonatrophic tongue most strongly indicate dysfunction at which level?',
      19:'Which form of increased muscle tone is characterized by a velocity-dependent catch during passive movement?',
      27:'Which site most commonly causes isolated right-sided limb dysmetria, intention tremor and dysdiadochokinesia with intact proprioception?'}
    positions=[i%4 for i in range(30)]
    random.Random(20261115).shuffle(positions)
    questions=[]
    for n,(r,pos) in enumerate(zip(ROWS,positions),1):
        if n in direct:r['question']=direct[n]
        options=[r['answer']]+[o for o,_ in r['distractors']]
        options[0],options[pos]=options[pos],options[0]
        rationales={o:why for o,why in r['distractors']}
        sections=[('Anatomical Basis',r['anatomy']),('Examination and Differentiation',r['examination']),('Clinical Implications',r['implications'])]
        html=['<h2>'+escape(r['title'])+'</h2>', '<p><strong>Correct answer: '+chr(65+pos)+' — '+escape(r['answer'])+'</strong></p>']
        teaching=[]
        for heading,body in sections:
            sentences=re.split(r'(?<=[.!?])\s+(?=[A-Z])',body)
            html.append('<h3>'+heading+'</h3><ul><li>'+rich(sentences[0]))
            if len(sentences)>1:html.append('<ul>'+''.join('<li>'+rich(t)+'</li>' for t in sentences[1:])+'</ul>')
            html.append('</li></ul>')
            teaching.append(dict(heading=heading,bullets=[dict(text=sentences[0],children=sentences[1:])]))
        tables=[]
        if r['table']:
            headers,rows=r['table'];tables=[dict(headers=headers,rows=rows)]
            html.append('<div class="table-wrap"><table><thead><tr>'+''.join('<th>'+escape(x)+'</th>' for x in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+escape(x)+'</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table></div>')
        other=[dict(optionIndex=i,explanation=rationales[o]) for i,o in enumerate(options) if i!=pos]
        html.append('<h3>Other Options</h3><ul>'+''.join('<li><strong>'+chr(65+a['optionIndex'])+' — '+escape(options[a['optionIndex']])+':</strong> '+rich(a['explanation'])+'</li>' for a in other)+'</ul>')
        refs=[dict(label=REFS[k][0],url=REFS[k][1]) for k in r['refs']]
        html.append('<h3>References</h3><ul>'+''.join('<li><a href="'+ref['url']+'">'+escape(ref['label'])+'</a></li>' for ref in refs)+'</ul>')
        plain='\n\n'.join([r['title'],'Correct answer: '+r['answer'],*[h+'\n'+b for h,b in sections],*['Other option — '+o+': '+why for o,why in r['distractors']]])
        if tables:plain+='\n\n'+' | '.join(tables[0]['headers'])+'\n'+'\n'.join(' | '.join(row) for row in tables[0]['rows'])
        plain+='\n\nReferences\n'+'\n'.join(x['label']+' — '+x['url'] for x in refs)
        questions.append(dict(id=f'neuro-rebuild-01-{n:03}',topic=r['section'],question=r['question'],options=options,correctIndex=pos,
          explanation=plain,explanationHtml=''.join(html),explanationTeaching=dict(title=r['title'],sections=teaching,tables=tables,otherOptions=other),references=refs,
          sourceCheckedAt='2026-11-15',reviewStatus='source_checked_not_independently_clinician_reviewed',
          questionStyle='direct' if n in direct else 'clinical_scenario'))
    bank=dict(schemaVersion=1,folder='Neurology',subject='Neurology',chapterOrder=1,topicOrder=1,headingIndex=0,
      document='01. Neuroanatomy, Clinical Localization & Neurological Examination',
      headingText='Neuroanatomy, Clinical Localization & Neurological Examination',targetQuestions=30,status='chapter_authored',
      authorship='Original educational MCQs; not authenticated NEET-SS past questions',
      sourceNote='Original postgraduate teaching synthesis. Accessible examination manuals and specialty references were checked for anatomical and bedside distinctions. Harrison’s is a requested conceptual standard; its full subscription text was not accessed or claimed as verified. No independent clinician review is recorded.',
      explanationCss='body{font:17px Arial,Helvetica,sans-serif;color:#252525}p{margin:0 0 8px}h2{font-size:18px;color:#6F3D5D;background:#E7E1E4;margin:4px 0 8px;padding:7px}h3{font-size:17px;color:#233D6B;border-bottom:1px solid #bbc4d3;margin:4px 0 8px}strong{color:#233D6B;font-size:17px}li{margin:3px 0}li li{margin:2.83px 0}.table-wrap{overflow-x:auto}table{border-collapse:collapse;font-size:17px;width:100%}th,td{border:1px solid #c9c9c9;padding:6px;text-align:left}th{background:#6F3D5D;color:white}tr:nth-child(even){background:#f7f5f6}mark{background:#FFF2B3}',questions=questions)
    OUT.mkdir(parents=True,exist_ok=True)
    dest=OUT/'01. Neuroanatomy, Clinical Localization & Neurological Examination.json'
    dest.write_text(json.dumps(bank,ensure_ascii=False,indent=2),encoding='utf-8')
    distribution=Counter(q['correctIndex'] for q in questions)
    assert sorted(distribution.values())==[7,7,8,8]
    assert len({q['question'] for q in questions})==30
    for q in questions:
        assert len(q['options'])==len(set(q['options']))==4
        assert {a['optionIndex'] for a in q['explanationTeaching']['otherOptions']}==set(range(4))-{q['correctIndex']}
        assert len(q['explanation'].split())>=180,(q['id'],len(q['explanation'].split()))
    print(json.dumps(dict(file=str(dest),questions=30,answers={chr(65+i):distribution[i] for i in range(4)},minimumExplanationWords=min(len(q['explanation'].split()) for q in questions)),indent=2))

if __name__=='__main__':build()
