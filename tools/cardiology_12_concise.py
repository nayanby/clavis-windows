"""Concise, structured explanation overrides following the user's latest preference."""

def B(label,*details):return ('**'+label+'**',list(details))

def apply(rows):
    edits={
    1: dict(sections=[
      ('Atrial Shunt Physiology',[
       B('Pulmonary flow murmur: increased RV stroke volume across a normal pulmonary valve.',
         'The low-pressure atrial jet is usually inaudible; murmur loudness does not measure defect size.'),
       B('Fixed S2 splitting: persistent RV volume loading with buffered respiratory variation.',
         'A large shunt may also produce a tricuspid mid-diastolic flow rumble.')]),
      ('Assessment',[
       B('TTE: define the communication, RV enlargement and pulmonary pressure.',
         'Use TEE for device rims; CMR/CT for uncertain pulmonary veins or chamber measurements.'),
       B('Closure assessment: integrate shunt burden, PVR, anatomy and LV filling pressure.',
         'Atrial arrhythmias may persist after closure; advanced pulmonary vascular disease changes eligibility.')])],
      reasons=[
       'A high-pressure VSD jet can be loud. An uncomplicated ASD has a small atrial pressure gradient; its ejection murmur arises at the pulmonary valve.',
       'Tricuspid regurgitation produces a lower-sternal, usually holosystolic murmur. It does not explain this pulmonary-area midsystolic flow murmur.',
       'RV outflow obstruction can produce an ejection murmur, but Doppler excludes it here; the ASD instead increases pulmonary flow.']),
    2: dict(sections=[
      ('Partial AV Septal Defect',[
       B('Primum communication + abnormal left AV valve + superior QRS axis.',
         'PR prolongation supports conduction involvement but is not diagnostic alone.'),
       B('Common AV junction: partial AVSD has separate valve orifices; complete AVSD adds a ventricular defect and common valve orifice.',
         'Strong association with trisomy 21; define anatomy directly.'),
       B('PFO differs from ASD: overlapping septal flaps form a tunnel without tissue deficiency.',
         'An incidental PFO rarely explains substantial chronic RV volume overload.')]),
      ('Repair and Follow-Up',[
       B('Echocardiography: map AV valves, shunt, LV outflow and pulmonary veins.',
         'Measure PVR invasively when pulmonary vascular disease is suspected.'),
       B('Indicated repair is generally surgical, addressing the septum and left AV valve.',
         'A conventional secundum device does not correct AVSD anatomy.',
         'Follow residual valve regurgitation, shunts, outflow obstruction and conduction disease.')])],
      reasons=[
       'Secundum defects cause RV loading, often with incomplete RBBB/right axis. The superior axis and abnormal left AV valve favor partial AVSD.',
       'Sinus venosus defects commonly accompany anomalous pulmonary venous drainage. They do not explain the characteristic AV-valve and superior-axis combination.',
       'Unroofed coronary sinus may accompany a persistent left SVC. The supplied valve and electrical findings instead support primum anatomy.']),
    3: dict(sections=[
      ('Compliance and Shunt Direction',[
       B('Reduced LV compliance raises LA pressure and increases left-to-right atrial flow.',
         'The defect can remain unchanged; preserved LVEF does not exclude diastolic dysfunction.'),
       B('RV stiffness or rising PVR can reduce or reverse left-to-right flow.')]),
      ('Before Closure',[
       B('Assess BP, volume status, AV-valve disease and LV filling pressure.'),
       B('Treat reversible contributors, then reassess complete closure, fenestration or deferral.'),
       B('Selected balloon occlusion: 2025 Class 2b.',
         'May overestimate the wedge-pressure rise after actual device closure; not a validated pass/fail test.')])],
      orderedSections=['Before Closure'],
      flow=['LV stiffness ↑','LA pressure ↑','Left-to-right shunt ↑','Closure may unmask pulmonary congestion'],
      reasons=[
       'A stiff RV resists filling and tends to reduce left-to-right shunting; the supplied change originates in the LV.',
       'Rising PVR can reduce or reverse flow, but PVR remains low here and left-to-right shunting increases.',
       'Improved LV compliance lowers filling pressure and favors LV filling; it is the opposite of the documented hypertensive change.']),
    4: dict(sections=[
      ('2025 ACC/AHA Closure Criteria',[
       B('Unrepaired ASD: Qp:Qs ≥1.5 + RV dilation + PVR ≤2 Wood units + no significant LV disease.',
         'Symptoms are not required when these favorable criteria are met.',
         'ESC 2020 uses a different low-PVR category (<3 Wood units); do not merge frameworks.')]),
      ('Closure and Follow-Up',[
       B('Confirm anatomy: defect size, rims, adjacent structures and pulmonary veins.'),
       B('Suitable secundum ASD: prefer transcatheter closure.',
         'AVSD/primum or unsuitable anatomy generally requires surgery.'),
       B('After device closure: ESC 2020 specifies antiplatelet therapy for ≥6 months, aspirin ≥75 mg/day.',
         'Individualize for bleeding, allergy and other antithrombotic indications.'),
       B('Image device position, residual shunt and RV remodeling.',
         'Monitor thrombus and atrial arrhythmias; closure does not erase established rhythm substrate.')])],
      orderedSections=['Closure and Follow-Up'],
      reasons=[
       'Observation suits a small shunt without important RV loading. This asymptomatic patient already meets favorable hemodynamic closure criteria.',
       'PAH treatment is used for selected elevated-PVR pathways. PVR 1.6 Wood units does not justify preparatory PAH medication.',
       'Diuretics relieve congestion but do not remove the persistent shunt; they are not definitive treatment for this suitable significant ASD.']),
    5: dict(sections=[
      ('Localize the First Step-Up',[
       B('Lower-SVC oxygen enrichment suggests pulmonary venous entry into the SVC.',
         'Repeat samples and confirm position: streaming or contamination can mislead.',
         'Do not use an enriched lower-SVC sample as pre-shunt mixed venous blood.')]),
      ('Map and Treat the Connection',[
       B('TEE plus CMR/CT: map all pulmonary veins, caval junctions and atrial septum.'),
       B('Quantify Qp/Qs and RV volume burden; the step-up alone does not prove a sinus venosus defect.'),
       B('Significant suitable lesions: surgical repair or selected expert covered-stent correction.',
         'Covered-stent evidence is mainly observational; test-balloon assessment must confirm unobstructed pulmonary venous redirection.',
         'Monitor SVC/pulmonary venous obstruction and residual shunting.')])],
      orderedSections=['Map and Treat the Connection'],
      reasons=[
       'A secundum ASD produces an atrial-level step-up. It does not explain reproducible enrichment in the SVC above the atrium.',
       'VSD flow produces a ventricular-level step-up, downstream of the normal SVC and right atrium.',
       'PDA flow enters the pulmonary artery. It cannot explain the earliest step-up within the SVC.']),
    6: dict(sections=[
      ('Selected Treat-and-Reassess Pathway',[
       B('2025 ASD pathway: initial PVR 5–8 Wood units falling below 5 on PAH therapy may permit closure.',
         'Require significant left-to-right flow, RV dilation and no important LV disease.',
         'Repeat invasive hemodynamics; a lower echo-estimated pressure is insufficient.'),
       B('ACHD/PH team selects complete closure, fenestration or nonclosure.',
         'Selected-responder cohorts do not prove universal reversibility or cure.')]),
      ('Drug Examples and Monitoring',[
       B('Sildenafil: 20 mg orally three times daily.',
         'Do not combine with organic nitrates or riociguat; monitor BP.'),
       B('Macitentan: 10 mg orally daily.',
         'Pregnancy contraindicated; assess contraception, hemoglobin, liver status and fluid retention.'),
       B('Continue PAH surveillance after closure; treatment may still be required.')])],
      flow=['PAH treatment','Repeat PVR and shunt assessment','Expert closure decision','Long-term PAH follow-up'],
      reasons=[
       'PVR ≤2 defines the uncomplicated pathway. Selected treated responders below 5 may still undergo specialist closure assessment.',
       'Closure removes the shunt but may leave pulmonary vascular disease; it does not justify planned withdrawal of PAH therapy.',
       'Elevated baseline PVR alone is not Eisenmenger syndrome. Net left-to-right flow, normal resting saturation and response require separate assessment.']),
    7: dict(sections=[
      ('Why Closure Can Cause Congestion',[
       B('The ASD decompresses a high-pressure LA; complete closure removes this outlet.',
         'Wedge 24 mmHg and LVEDP 26 mmHg indicate significant left-heart filling disease.',
         'Low PVR and preserved LVEF do not establish closure safety.')]),
      ('Management Sequence',[
       B('Optimize BP and volume status; assess ischemia and AV-valve disease.'),
       B('Reassess symptoms and filling pressures with ACHD expertise.'),
       B('Choose complete closure, selected fenestration or nonclosure from the resulting physiology.'),
       B('Balloon occlusion may help selected cases: 2025 Class 2b.',
         'Temporary occlusion may overestimate the post-device wedge rise; combine baseline findings and treatment response.',
         'Follow congestion, residual shunt, RV remodeling and arrhythmia.')])],
      orderedSections=['Management Sequence'],
      reasons=[
       'Complete device closure suits favorable pulmonary and left-heart physiology. Markedly elevated filling pressure creates a pulmonary-congestion hazard here.',
       'Surgery helps unsuitable device anatomy or associated lesions, but a complete patch removes the same LA decompression route.',
       'PAH drugs target precapillary pulmonary vascular disease. High wedge pressure with low PVR instead identifies a left-heart filling problem.']),
    }
    for number,edit in edits.items():
        row=rows[number-1]
        row['sections']=edit['sections']
        row['others']=[(option,reason) for (option,_),reason in zip(row['others'],edit['reasons'])]
        row['explanationStyle']='concise_structured'
        for key in ['orderedSections','flow']:
            if key in edit:row[key]=edit[key]
