"""Original decision-mapped cardiovascular physiology and investigation MCQs."""
import json
from qbank_json_chapters import question as Q, save, ROOT

R={
 'PV':('Klabunde cardiovascular physiology: loading and inotropy in pressure-volume loops','https://cvphysiology.com/cardiac-function/cf025'),
 'COMPLIANCE':('Klabunde cardiovascular physiology: ventricular compliance','https://cvphysiology.com/cardiac-function/cf014'),
 'LOOP':('Klabunde cardiovascular physiology: ventricular pressure-volume relationship','https://cvphysiology.com/cardiac-function/cf024'),
 'ELASTANCE':('Physiological Society: LV volume analysis and contractile state, 2018','https://doi.org/10.1152/advan.00140.2017'),
 'CYCLE':('Fukuta and Little: cardiac cycle and physiological basis of ventricular function','https://pmc.ncbi.nlm.nih.gov/articles/PMC2390899/'),
}
rows=[]
def S(h,main,*children):return h,[(main,list(children))]
def add(*a,**kw):rows.append(Q(*a,**kw))

add('Ventricular mechanics and cardiac cycle','Preload and the Frank–Starling Response',
 'In an idealized LV pressure–volume experiment, end-diastolic volume increases while arterial afterload and contractile state are held constant. Which change is expected?',
 'A wider loop with increased stroke volume along an unchanged end-systolic relationship',[
 ('A wider loop with a steeper end-systolic relationship','A steeper end-systolic pressure–volume relationship indicates increased contractile state, whereas the experiment specifies unchanged contractility despite the larger stroke volume.'),
 ('A narrower loop with increased end-systolic volume','This pattern fits an acute increase in afterload or reduced contractility more closely; an isolated preload increase normally augments stroke volume through length-dependent activation.'),
 ('A leftward shift of the diastolic pressure–volume relationship','An altered diastolic relationship indicates a change in chamber filling properties; increasing filling volume moves the operating point along the existing relationship rather than proving changed compliance.')],
 [S('Distinguish Loading From Contractile State','**Preload is the myocardial stretch before contraction**, commonly approximated by end-diastolic volume in an idealized loop. More filling can increase ejection through the Frank–Starling mechanism.',
    'Stroke volume is end-diastolic minus end-systolic volume and corresponds to loop width. The end-systolic relationship need not become steeper for stroke volume to increase.',
    'End-diastolic pressure is not interchangeable with volume: compliance and external restraint influence the pressure produced by a given volume.'),
  S('Apply the Model With Clinical Qualifications','**A larger stroke volume does not independently demonstrate improved intrinsic contractility.** Compare loading conditions before interpreting serial measurements.',
    'The idealized experiment fixes variables that often change together in patients. A fluid bolus can alter arterial pressure, ventricular interaction and valve regurgitation as well as filling.',
    'Use the model to explain a physiologic response, not to justify fluid administration to every hypotensive patient. Assess congestion, perfusion and the specific cause of instability. Fluid responsiveness describes a potential rise in output with additional preload; it does not establish that fluid is necessary or that its benefits exceed the risk of pulmonary or systemic congestion. A high filling pressure can coexist with poor forward flow and should not be interpreted as evidence that another bolus will help.')],['PV','LOOP'])

add('Ventricular mechanics and cardiac cycle','Afterload Versus Reduced Contractility',
 'At fixed initial LV end-diastolic volume, arterial pressure is abruptly increased. The first pressure–volume loop is taller and narrower, with greater end-systolic volume; its end-systolic point remains on the original end-systolic relationship. Which interpretation is best?',
 'Increased afterload with preserved contractile state',[
 ('Reduced contractility with unchanged afterload','Reduced contractility shifts the end-systolic relationship downward and rightward; the preserved relationship and higher arterial load instead support a loading effect.'),
 ('Increased preload with unchanged afterload','Additional preload increases starting end-diastolic volume and usually broadens the loop under otherwise fixed conditions; the stem fixes initial filling volume and raises arterial pressure.'),
 ('Reduced diastolic compliance with unchanged afterload','Reduced compliance alters the diastolic pressure–volume relationship and filling pressure; it does not explain the stated acute arterial load and preserved end-systolic relationship.')],
 [S('Identify the Variable That Changed','**Afterload is the load opposing myocardial shortening.** In this experiment the ventricle ejects against a higher arterial pressure, leaving more volume at end systole.',
    'With the initial filling volume fixed, a higher residual end-systolic volume means a smaller stroke volume and lower ejection fraction on that beat.',
    'A fall in EF therefore does not by itself prove that intrinsic contractility deteriorated. Clinical afterload also depends on arterial impedance and ventricular geometry, not only a cuff pressure.'),
  S('Use End-Systolic Behavior to Clarify Mechanism','**The end-systolic pressure–volume relationship helps distinguish load change from contractile-state change.** Its slope is often called end-systolic elastance.',
    'Reduced contractile state shifts the relation downward/rightward; increased contractile state generally shifts it upward/leftward. Interpretation ideally uses a family of loops across changing loads.',
    'The relationship is relatively load insensitive within a useful range, not perfectly independent of all physiology. Do not infer a measured elastance from a single routine echo EF. In clinical assessment, combine pressure, chamber size, valve disease and the treatment context. Subsequent beats can develop secondary preload changes as residual volume accumulates, which is why this stem specifies the first beat and fixed initial end-diastolic volume.')],['ELASTANCE','PV'])

add('Ventricular mechanics and cardiac cycle','Ventricular Compliance and Filling Pressure',
 'Two ventricles have the same end-diastolic volume, but one requires a substantially higher end-diastolic pressure. Its end-diastolic pressure–volume curve lies upward and leftward. Which property is reduced?',
 'Diastolic chamber compliance',[
 ('End-systolic elastance','End-systolic elastance describes the systolic pressure–volume relationship and contractile state; this question concerns the pressure required to fill the chamber during diastole.'),
 ('Systemic arterial compliance','Arterial compliance affects the arterial pressure response to ejected volume and contributes to afterload; it is distinct from the ventricular filling relationship shown.'),
 ('Regurgitant orifice area','A smaller regurgitant orifice can alter loading and forward flow, but it is not the chamber property defined by an increased filling pressure at the same volume.')],
 [S('Relate Pressure Change to Volume Change','**Compliance is the change in volume divided by the corresponding change in pressure**, evaluated over the relevant portion of the filling curve. Stiffness is its reciprocal.',
    'A less compliant ventricle develops greater pressure for a comparable volume. Because the diastolic curve is nonlinear, its local slope changes as filling increases.',
    'A high filling pressure is therefore not a direct measurement of an excessive end-diastolic volume. Hypertrophy and fibrosis are potential contributors, while pericardial restraint and ventricular interaction can affect chamber behavior.'),
  S('Keep Relaxation, Compliance and EF Separate','**Active relaxation and passive filling properties are related but different components of diastolic function.** Impaired relaxation affects early filling; chamber stiffness affects the pressure–volume relationship.',
    'Preserved EF describes the proportion of end-diastolic volume ejected and does not establish normal filling pressures or exclude a heart-failure syndrome.',
    'Clinical evaluation requires symptoms, signs and appropriate objective evidence rather than diagnosing HFpEF from one pressure or a normal EF alone. Interpret Doppler findings in their rhythm and loading context and consider external restraint when pressures and volumes appear discordant. Treatment should address the actual cause of congestion and impaired function; the curve alone does not select a drug or establish that more fluid will improve output.')],['COMPLIANCE','CYCLE'])

R.update({
 'VALVES':('Klabunde cardiovascular physiology: isovolumetric contraction','https://cvphysiology.com/heart-disease/hd002b'),
 'DIASTOLE':('British Society of Echocardiography guidance on diastolic function, 2024','https://pmc.ncbi.nlm.nih.gov/articles/PMC11145885/'),
 'RV':('AHA scientific statement: evaluation and management of right-sided heart failure, 2018','https://www.ishlt.org/docs/default-source/standards-guidelines/2018_endorsement_aha_righthfevaluationandmanagement.pdf'),
})

add('Ventricular mechanics and cardiac cycle','Valve Timing and Isovolumetric Relaxation',
 'In the conventional LV pressure–volume model with competent valves, which pressure configuration occurs during isovolumetric relaxation before mitral opening?',
 'Aortic pressure exceeds LV pressure, and LV pressure still exceeds left atrial pressure',[
 ('LV pressure exceeds both aortic and left atrial pressure','This configuration supports aortic ejection after the outflow valve opens, rather than relaxation with the aortic valve already closed.'),
 ('Aortic pressure exceeds LV pressure, and left atrial pressure exceeds LV pressure','Once left atrial pressure exceeds LV pressure and the mitral valve opens, ventricular filling begins; that is beyond the isovolumetric interval.'),
 ('LV pressure exceeds aortic pressure, and left atrial pressure exceeds LV pressure','This is not the normal early-diastolic pressure ordering; aortic pressure is higher than LV pressure during the interval following aortic closure.')],
 [S('Follow the Pressure Crossings','**Isovolumetric relaxation lies between aortic closure and mitral opening in the conventional model.** LV pressure falls while both valves remain closed and volume stays approximately at end-systolic volume.',
    'The aortic-to-LV gradient supports aortic closure. The mitral valve remains closed until declining LV pressure falls below left atrial pressure.',
    'The preceding isovolumetric contraction interval occurs after mitral closure and before aortic opening, with rising rather than falling ventricular pressure.'),
  S('Use the Model Without Confusing Electrical and Mechanical Events','**Valve events follow changing pressure gradients rather than a fixed ECG landmark alone.** The ECG provides timing context but does not directly measure opening pressure.',
    'Important regurgitation disrupts the ideal closed-valve, constant-volume assumptions; a pressure–volume diagram must therefore be interpreted in the context of valve competence.',
    'Relaxation time also depends on loading: a high left atrial pressure can promote earlier mitral opening even when myocardial relaxation is impaired. A short interval does not independently prove normal diastolic function. Distinguish the chamber-level model from the motion of every individual muscle fiber, since constant cavity volume does not require every sarcomere to maintain a fixed length. Clinical Doppler interpretation integrates valve timing, tissue velocities and the pressure context instead of assigning a diagnosis from one interval.')],['VALVES','DIASTOLE'],style='direct',table=(['LV phase','Mitral valve','Aortic valve','Volume behavior'],[
 ['Filling','Open','Closed','Increases'],['Isovolumetric contraction','Closed','Closed','Approximately unchanged'],
 ['Ejection','Closed','Open','Decreases'],['Isovolumetric relaxation','Closed','Closed','Approximately unchanged']]))

add('Ventricular mechanics and cardiac cycle','Tachycardia and Left Ventricular Supply–Demand Balance',
 'A patient with LV hypertrophy and elevated LV filling pressure develops marked tachycardia without a rise in aortic diastolic pressure. Which mechanism most directly worsens subendocardial oxygen supply–demand balance?',
 'Shorter diastolic perfusion time combined with increased myocardial oxygen demand',[
 ('Longer systolic perfusion time combined with reduced oxygen extraction','The left ventricular subendocardium is compressed during systole, and myocardial oxygen extraction is already substantial; tachycardia does not create a favorable longer systolic supply interval.'),
 ('An increased diastolic coronary pressure gradient caused by the higher heart rate','A higher rate does not itself raise aortic diastolic pressure relative to LV filling pressure; the stated unchanged arterial pressure provides no such compensating gradient.'),
 ('Reduced wall stress caused by the shorter ventricular filling interval','Shorter filling may affect volume, but hypertrophy and high filling pressure do not make tachycardia a reliable wall-stress reduction strategy; the major stated problem is less perfusion time with greater demand.')],
 [S('Separate Perfusion Time From Driving Pressure','**Left ventricular subendocardial flow is strongly dependent on diastole** because systolic contraction compresses intramyocardial vessels. A higher heart rate shortens available diastolic time.',
    'A useful simplified driving-pressure estimate is aortic diastolic pressure minus LV end-diastolic pressure. Elevated LV filling pressure reduces that gradient even when systemic arterial pressure appears acceptable.',
    'The estimate is a teaching approximation, not a complete measurement of coronary resistance, phasic flow or microvascular function.'),
  S('Recognize Simultaneous Demand and Filling Effects','**Tachycardia also increases myocardial oxygen demand.** Hypertrophy can increase vulnerability when coronary flow reserve cannot compensate.',
    'Shorter diastole can impair filling, particularly with impaired relaxation or loss of atrial contribution. The result depends on rhythm, rate, loading and the underlying disease.',
    'Evaluate ischemic symptoms in context rather than assuming either fixed epicardial stenosis or a purely rate-related cause. Correct the precipitant and assess hemodynamic stability before choosing rate or rhythm treatment. This mechanism does not mean that every elevated heart rate should be suppressed: compensatory sinus tachycardia during shock may reflect an unmet circulatory need. Clinical action follows the cause and perfusion assessment, while the physiology explains why uncontrolled tachycardia can become harmful in a vulnerable ventricle.')],['CYCLE','RV'])

add('Ventricular mechanics and cardiac cycle','Ventricular Interdependence in Right Ventricular Loading',
 'With severe acute RV pressure loading, echocardiography shows RV dilation, leftward septal displacement and a small LV cavity. LV EF is preserved, but systemic output falls. Which mechanism best explains the LV finding?',
 'Reduced LV filling from impaired RV delivery and mechanical ventricular interaction',[
 ('Primary LV systolic failure demonstrated by the small cavity','A small cavity with preserved fractional emptying does not establish primary LV contractile failure; it can represent underfilling caused by right-sided dysfunction.'),
 ('Reduced systemic afterload causing primary LV volume depletion','Low systemic resistance may occur in other shock states, but does not account for the demonstrated RV pressure loading and leftward septal displacement.'),
 ('Primary mitral inflow obstruction from structural mitral stenosis','Mitral stenosis can impair filling, but would require valve evidence; the acute RV geometry and septal findings directly support ventricular interaction instead.')],
 [S('Recognize Both Serial and Mechanical Coupling','**Reduced RV forward output limits pulmonary venous return to the LV.** In addition, the ventricles share a septum and are constrained within the pericardial space.',
    'RV dilation and altered transseptal forces can distort LV geometry and reduce filling. These mechanisms can coexist rather than representing competing explanations.',
    'A small, apparently vigorous LV is therefore not reassuring proof of adequate systemic flow. EF is a fraction and can remain normal when absolute stroke volume is low.'),
  S('Use Loading Assessment to Guide the Next Decision','**Additional fluid is not automatically beneficial in a dilated, pressure-loaded RV.** Excess filling can aggravate septal displacement and congestion.',
    'Assess systemic pressure, congestion, oxygenation, RV perfusion and the cause of elevated afterload. Acute pulmonary embolism, pulmonary vascular disease and ventilator-related loading require different definitive approaches.',
    'Integrate echo with the clinical and hemodynamic picture rather than treating a single chamber measurement as a complete diagnosis. Pressure and volume loading can produce different timing of septal flattening, and mixed disease can blur that distinction. Reassess after intervention: improved arterial pressure alone does not prove restored forward output, just as a lower pulmonary artery pressure can sometimes reflect a failing RV rather than successful unloading.')],['RV'])

R.update({
 'REGURG':('ASE/SCMR recommendations for native valvular regurgitation, 2017','https://www.asecho.org/wp-content/uploads/2017/04/2017VavularRegurgitationGuideline.pdf'),
 'PULSE':('Klabunde cardiovascular physiology: aortic and arterial pulse pressure','https://cvphysiology.com/blood-pressure/bp003'),
 'RHC':('German Centre for Cardiovascular Research: cardiac catheterization SOP','https://service4studies.dzhk.de/fileadmin/user_upload/DZHK-SOP-K-05-Cardiac_Catheterization_V1.1_EN.pdf'),
})

add('Ventricular mechanics and cardiac cycle','Total Versus Forward Stroke Volume in Mitral Regurgitation',
 'In isolated mitral regurgitation without a shunt or aortic regurgitation, LV end-diastolic volume is 150 mL and end-systolic volume 50 mL. Correctly measured LVOT forward stroke volume is 55 mL. Which interpretation is correct?',
 'LV EF is about 67%, but regurgitant volume is 45 mL per beat',[
 ('LV EF is about 37%, and regurgitant volume is 45 mL per beat','Dividing forward stroke volume by LV end-diastolic volume gives a forward fraction, not the conventional volume-based LV EF; the latter uses total LV stroke volume.'),
 ('LV EF is about 67%, and regurgitant volume is 55 mL per beat','The conventional EF calculation is correct, but 55 mL is the measured forward volume; regurgitant volume is the total 100 mL minus that forward component.'),
 ('LV EF is about 50%, and regurgitant volume is 100 mL per beat','Neither quantity follows the given definitions: EF uses the 100 mL volume difference divided by 150 mL, and not all LV ejection is regurgitant.')],
 [S('Partition the Ejected Volume','**Total LV stroke volume is EDV minus ESV: 150 − 50 = 100 mL.** Conventional EF is 100/150, approximately 67%.',
    'With isolated MR and the stated exclusions, total ejection separates into forward aortic flow and backward mitral flow. Regurgitant volume is 100 − 55 = 45 mL per beat.',
    'Regurgitant fraction is 45/100, or 45%. Keep its denominator distinct from EDV and from forward stroke volume.'),
  S('Interpret a Preserved EF in Context','**A preserved conventional EF does not guarantee adequate forward output in regurgitation.** Some of the ejected blood returns to the atrium rather than reaching the systemic circulation.',
    'Integrate valve anatomy, quantitative measurements, ventricular remodeling, symptoms and other supportive findings. One derived value should not independently determine severity or intervention.',
    'These subtraction methods are sensitive to acquisition errors, especially area measurements, and their assumptions fail when additional regurgitant lesions or shunts are present. Verify that measurements refer to comparable beats and loading conditions. A disagreement between measured flows should prompt review of technique before assigning the difference to disease. The distinction also explains why serial EF changes must be interpreted with the loading and valve context rather than equating an apparently high EF with normal intrinsic myocardial performance.')],['REGURG'])

add('Ventricular mechanics and cardiac cycle','Arterial Compliance and Pulse Pressure',
 'Two patients have similar stroke volume and heart rate. In an idealized arterial model, one has substantially lower large-artery compliance. Which pressure change is expected?',
 'A larger pulse pressure for the same ejected volume',[
 ('A smaller pulse pressure because arterial storage is reduced','A less compliant artery undergoes a greater pressure rise for a given volume input; reduced storage capacity does not imply a smaller pressure excursion.'),
 ('An unchanged pulse pressure because stroke volume is the same','Stroke volume is one determinant, but compliance also matters; equal stroke volume does not ensure equal pulse pressure in different arterial systems.'),
 ('A larger pulse pressure only if cardiac output also increases','Lower compliance can widen pulse pressure without an increase in stroke volume or heart rate, so a higher cardiac output is not required.')],
 [S('Relate Pulsatile Pressure to Volume Storage','**Pulse pressure is systolic minus diastolic arterial pressure.** In a simplified model, it increases with stroke volume and decreases with arterial compliance.',
    'The approximation pulse pressure ≈ stroke volume/compliance explains why a stiff aorta can generate a wide pressure excursion despite an ordinary ejected volume.',
    'Compliance is pressure dependent; the same artery can become less compliant at a higher operating pressure. Compare measurements under their actual physiologic conditions.'),
  S('Avoid Treating Pulse Pressure as a Direct Flow Measurement','**The real arterial waveform also reflects ejection characteristics and wave reflection.** A peripheral cuff pressure is not interchangeable with a central aortic waveform.',
    'A wide pulse pressure can occur with stiffness, high stroke volume or regurgitant runoff; the pressure difference alone does not identify which mechanism is present.',
    'Likewise, a narrow pulse pressure can suggest reduced ejection but does not quantify output without assumptions about vascular properties. Interpret the finding with examination, perfusion, valve assessment and appropriate imaging. Do not infer that a higher systolic pressure necessarily means better systemic flow, or that lowering pulse pressure is itself a sufficient treatment goal. The simplified model is useful for mechanism questions while clinical decisions require the patient’s overall blood-pressure pattern, disease and treatment indications.')],['PULSE'])

add('Flow, oxygen transport and resistance calculations','Fick Cardiac Output and Unit Conversion',
 'Measured oxygen consumption is 250 mL O2/min. Arterial oxygen content is 20 mL O2/dL and mixed venous content is 15 mL O2/dL. There is no intracardiac shunt. What is cardiac output?',
 '5.0 L/min',[
 ('2.5 L/min','This value does not follow the stated oxygen consumption divided by the measured arteriovenous oxygen content difference with correct conversion from deciliters to liters.'),
 ('10.0 L/min','This value would require a smaller arteriovenous oxygen content difference at the same consumption; it is not obtained from the given 5 mL/dL difference.'),
 ('50.0 L/min','The numerical quotient is 50 dL/min, not 50 L/min; one liter contains ten deciliters.')],
 [S('Apply Conservation of Oxygen','**Cardiac output = oxygen consumption/(arterial oxygen content − mixed venous oxygen content).** The numerator and denominator must use compatible oxygen-volume units.',
    'The content difference is 20 − 15 = 5 mL O2/dL. Dividing 250 mL O2/min by 5 mL O2/dL gives 50 dL blood/min.',
    'Convert 50 dL/min to ==5.0 L/min==. Equivalently, convert the content difference to 50 mL O2/L before dividing.'),
  S('Understand What Makes the Result Valid','**The Fick method relates tissue oxygen uptake to the difference between delivered and returning blood oxygen content.** Direct Fick uses measured oxygen consumption; assumed consumption introduces a separate source of error.',
    'Use representative systemic arterial and mixed venous samples under sufficiently stable conditions. A central venous sample is not automatically identical to a pulmonary arterial mixed venous sample.',
    'Intracardiac shunting requires a more careful separation of pulmonary and systemic flow and appropriate sampling. Saturation difference alone is not the same as content difference unless the hemoglobin and dissolved-oxygen assumptions are addressed. Interpret a calculated output with the measurement quality and clinical state rather than treating the arithmetic as proof that all input values are valid. A normal resting output also does not establish normal filling pressures or adequate exercise reserve.')],['RHC'],style='direct',calculation=True)

R.update({
 'HEMO':('Vanderbilt cardiovascular ICU: hemodynamic parameter formulas','https://www.vumc.org/cvicu/sites/default/files/2020-03/Hemodynamic-Parameters.pdf'),
 'RESISTANCE':('OpenAnesthesia: calculation of pulmonary and systemic vascular resistance','https://www.openanesthesia.org/keywords/calculation-of-pulmonary-and-systemic-vascular-resistance/'),
 'PH':('ESC/ERS pulmonary hypertension guideline, 2022','https://doi.org/10.1183/13993003.00879-2022'),
})

add('Flow, oxygen transport and resistance calculations','Cardiac Index and Body Surface Area',
 'A patient has a measured cardiac output of 4.2 L/min and body surface area of 2.1 m². What is the cardiac index?',
 '2.0 L/min/m²',[
 ('1.0 L/min/m²','This value does not follow dividing the stated cardiac output by the body surface area; both the numerical operation and indexed unit must be preserved.'),
 ('4.2 L/min/m²','The numerical value 4.2 is the unindexed output in liters per minute; reporting it as an index without division does not account for body size.'),
 ('8.8 L/min/m²','Multiplication of output by body surface area gives approximately 8.8 numerically, but indexing requires division rather than multiplication.')],
 [S('Normalize Flow to Body Size','**Cardiac index = cardiac output/body surface area.** Substitute 4.2 L/min divided by 2.1 m² to obtain ==2.0 L/min/m²==.',
    'Keep the indexed unit explicit. Cardiac output and cardiac index are related measurements but are not numerically interchangeable.',
    'The same absolute output can represent a different indexed flow in two patients of different body size.'),
  S('Interpret a Low Index in the Clinical State','**A low index describes reduced indexed flow, not a complete diagnosis of shock.** Assess tissue perfusion, pressure, oxygen transport and the underlying mechanism.',
    'A low value can occur with impaired contractility, inadequate filling, excessive afterload or mechanical obstruction. Treatment selection requires distinguishing these possibilities.',
    'Review the measurement technique and whether the patient was stable during acquisition. An assumed oxygen consumption, an unrepresentative sample or technically inconsistent thermodilution measurements can distort calculated output and therefore its index. Body-surface-area normalization also has limitations at extreme body sizes. Do not use a single index as an automatic trigger for a specific inotrope or fluid bolus. Follow the clinical trajectory and repeat appropriately acquired measurements when the result is discordant with examination, perfusion or other objective findings.')],['HEMO'],style='direct',calculation=True)

add('Flow, oxygen transport and resistance calculations','Systemic Vascular Resistance Calculation',
 'Mean arterial pressure is 80 mmHg, mean right atrial pressure 10 mmHg and cardiac output 5 L/min. What is systemic vascular resistance in dyn·s·cm⁻⁵?',
 '1120 dyn·s·cm⁻⁵',[
 ('1280 dyn·s·cm⁻⁵','This result omits the downstream right atrial pressure by using MAP alone; the correct driving pressure is MAP minus mean right atrial pressure.'),
 ('1440 dyn·s·cm⁻⁵','This result adds right atrial pressure to MAP, whereas resistance uses the pressure drop across the systemic vascular bed.'),
 ('14 dyn·s·cm⁻⁵','Fourteen is the pressure-gradient-to-flow quotient in Wood units, but the requested cgs expression requires multiplication by 80.')],
 [S('Use the Pressure Drop Across the Correct Circuit','**SVR = 80 × (MAP − mean RAP)/CO** when pressures are in mmHg and output is in L/min.',
    'The systemic pressure gradient is 80 − 10 = 70 mmHg. Dividing by 5 L/min gives 14 mmHg·min/L, or 14 Wood units.',
    'Multiplication by 80 gives ==1120 dyn·s·cm⁻⁵==. Omitting RAP becomes particularly misleading when venous pressure is markedly elevated.'),
  S('Understand a Derived Resistance','**SVR is calculated from pressure and flow**, rather than being a direct measure of intrinsic myocardial contractility or a complete description of arterial load.',
    'Arterial pulsatility, compliance and wave reflection also affect ventricular afterload. A single steady-flow resistance cannot capture all of those properties.',
    'Interpret the result with the actual output and perfusion state. Identical MAP values can coexist with different combinations of cardiac output and vascular resistance. Check transducer leveling, the averaging interval and contemporaneous output acquisition when results appear inconsistent. A change in calculated resistance may reflect a change in the numerator, the denominator or both; do not infer vasoconstriction from the ratio without examining its inputs. If using cardiac index instead of output, label the result as an indexed resistance with the appropriate units.')],['RESISTANCE','HEMO'],style='direct',calculation=True)

add('Flow, oxygen transport and resistance calculations','Pulmonary Vascular Resistance Calculation',
 'At right-heart catheterization, mean pulmonary artery pressure is 35 mmHg, PAWP 15 mmHg, mean right atrial pressure 10 mmHg and cardiac output 4 L/min. What is pulmonary vascular resistance?',
 '5.0 Wood units',[
 ('6.25 Wood units','This subtracts right atrial pressure from mean pulmonary artery pressure; pulmonary vascular resistance instead uses PAWP as the downstream pressure estimate.'),
 ('8.75 Wood units','This divides mean pulmonary artery pressure alone by output, giving total pulmonary resistance rather than the transpulmonary-gradient-based PVR.'),
 ('0.25 Wood units','This reverses or otherwise misapplies the gradient-to-flow relationship; the transpulmonary gradient is 20 mmHg and flow is 4 L/min.')],
 [S('Subtract the Pulmonary Downstream Pressure','**PVR = (mean PAP − PAWP)/cardiac output.** The stated transpulmonary gradient is 35 − 15 = 20 mmHg.',
    'Divide 20 mmHg by 4 L/min to obtain ==5.0 Wood units==. If cgs units are requested, multiply by 80 to obtain 400 dyn·s·cm⁻⁵.',
    'Right atrial pressure is not the downstream pressure for this vascular bed. It belongs in the systemic resistance calculation when subtracted from MAP.'),
  S('Verify the Inputs Before Classifying Disease','**An inaccurate wedge or output produces an inaccurate resistance.** Confirm a genuine wedge recording and use an appropriate flow measurement.',
    'A high pulmonary arterial pressure alone does not establish increased pulmonary vascular resistance; high flow and elevated left-sided filling pressure are alternative contributors.',
    'The 2022 ESC/ERS hemodynamic classification integrates mean PAP, PAWP and PVR. A precapillary hemodynamic pattern is not itself a complete etiologic diagnosis of pulmonary arterial hypertension. Interpret values obtained during unstable physiology or major intrathoracic-pressure changes carefully. In shunt disease, pulmonary and systemic flows can differ, so the correct flow for the relevant circuit matters. These considerations make the subtraction and units necessary but not sufficient for a valid clinical conclusion.')],['RESISTANCE','PH'],style='direct',calculation=True)

R.update({
 'OXYGEN':('Physiological Society: pulmonary physiology of exercise, 2023','https://doi.org/10.1152/advan.00067.2023'),
 'VENOUS':('Gutierrez: central and mixed venous oxygen saturation, 2020','https://pmc.ncbi.nlm.nih.gov/articles/PMC7001812/'),
 'SHUNT':('JACC Interventions: catheterization in adults with congenital heart disease, 2022','https://doi.org/10.1016/j.jcin.2021.12.020'),
})

add('Flow, oxygen transport and resistance calculations','Arterial Oxygen Content in Anemia',
 'Hemoglobin is 8 g/dL, arterial oxygen saturation 100% and PaO2 100 mmHg. Using oxygen-binding capacity 1.34 mL/g and dissolved coefficient 0.003 mL/dL/mmHg, what is arterial oxygen content?',
 'Approximately 11.0 mL O2/dL',[
 ('Approximately 8.0 mL O2/dL','Hemoglobin concentration is not itself oxygen content; the oxygen-binding coefficient and saturation must be applied, with the dissolved component added.'),
 ('Approximately 13.4 mL O2/dL','This would fit a different hemoglobin concentration under similar saturation assumptions, not the stated 8 g/dL.'),
 ('Approximately 20.0 mL O2/dL','Near-normal arterial saturation and tension do not guarantee normal oxygen content when hemoglobin concentration is substantially reduced.')],
 [S('Add Bound and Dissolved Oxygen','**CaO2 = 1.34 × Hb × SaO2 + 0.003 × PaO2**, with saturation entered as a fraction and the stated units.',
    'Hemoglobin-bound oxygen is 1.34 × 8 × 1.00 = 10.72 mL/dL. Dissolved oxygen is 0.003 × 100 = 0.30 mL/dL.',
    'Total content is ==11.02 mL O2/dL==, approximately 11.0. Entering saturation as 100 rather than 1.00 produces a hundredfold error in the bound term.'),
  S('Separate Saturation From Delivery','**A normal saturation describes the proportion of available hemoglobin binding sites occupied**, not the total amount of oxygen carried in a given volume of blood.',
    'Anemia can therefore reduce content despite a normal PaO2 and saturation. Increasing inspired oxygen after hemoglobin is saturated mainly affects the smaller dissolved component under ordinary conditions.',
    'Systemic oxygen delivery also depends on cardiac output: multiplying output in L/min by content in mL/dL requires a factor of ten to obtain mL O2/min. These calculations explain physiology but do not independently set a transfusion threshold. Treatment depends on bleeding, ischemia, symptoms, hemodynamics and the relevant clinical evidence. Consider dyshemoglobinemia and the measurement method when pulse oximetry, blood gas values and clinical findings disagree.')],['OXYGEN'],style='direct',calculation=True)

add('Flow, oxygen transport and resistance calculations','Mixed Venous Saturation and Oxygen Extraction',
 'During monitored care, true mixed venous oxygen saturation falls from 72% to 52%. Arterial saturation, hemoglobin and measured cardiac output are unchanged; the patient has developed shivering and fever. Which mechanism best explains the change?',
 'Increased oxygen consumption with greater tissue extraction',[
 ('Reduced arterial oxygen content caused by desaturation','Arterial desaturation lowers delivery and can lower SvO2, but the stem explicitly holds arterial saturation and hemoglobin unchanged.'),
 ('Reduced systemic oxygen delivery caused by lower cardiac output','A falling output can lower SvO2 through increased extraction, but measured output and arterial content are unchanged in this scenario.'),
 ('Impaired tissue oxygen extraction with venous hyperoxia','Impaired extraction can produce a relatively high venous saturation despite tissue dysfunction; it does not explain this falling value during increased metabolic demand.')],
 [S('Interpret the Supply–Demand Balance','**Mixed venous saturation reflects the interaction of oxygen delivery and consumption.** When output and arterial content remain stable, greater consumption lowers returning oxygen content.',
    'Shivering and fever can increase metabolic demand. The stated fall is therefore consistent with greater extraction rather than proving new pump failure.',
    'A low value can also occur with anemia, hypoxemia or reduced output in other settings; those alternatives must be checked rather than inferred from saturation alone.'),
  S('Check the Sample and the Clinical Context','**True mixed venous blood is sampled in the pulmonary artery after venous return has mixed.** Central venous saturation is a related but nonidentical measurement.',
    'Sampling location, catheter position, timing and shunts can affect interpretation. Compare equivalent measurements obtained under stable acquisition conditions.',
    'A high or normal value does not exclude shock, impaired extraction or regional tissue hypoxia. Integrate perfusion findings, lactate trends, hemoglobin, arterial oxygenation and measured flow. Treat the actual contributor rather than pursuing an isolated saturation target with empiric fluid, transfusion or inotrope therapy. When the result conflicts with the patient’s condition, verify sampling and inputs before escalating treatment. Reassessment after controlling shivering can help establish whether the proposed metabolic explanation fits the observed trajectory.')],['VENOUS'])

add('Flow, oxygen transport and resistance calculations','Pulmonary-to-Systemic Flow Ratio',
 'During stable catheterization on room air, systemic arterial saturation is 98%, pulmonary venous saturation 98%, representative pre-shunt mixed venous saturation 68% and pulmonary arterial saturation 83%. Assuming equal hemoglobin and negligible dissolved oxygen, what is Qp/Qs?',
 '2.0',[
 ('0.5','This inverts the ratio and would suggest systemic flow exceeding pulmonary flow, contrary to the stated pulmonary arterial oxygen enrichment.'),
 ('1.0','Equal pulmonary and systemic flow would require equal relevant oxygen content differences, whereas these differences are 30 and 15 saturation points.'),
 ('1.5','This does not follow dividing the systemic arteriovenous difference by the pulmonary venous-to-arterial difference under the stated assumptions.')],
 [S('Apply the Two-Circuit Fick Relationship','**Qp/Qs = (systemic arterial content − mixed venous content)/(pulmonary venous content − pulmonary arterial content).** Oxygen consumption cancels in the ratio.',
    'Under the stated saturation simplification, Qp/Qs = (98 − 68)/(98 − 83) = 30/15 = ==2.0==.',
    'Pulmonary flow is twice systemic flow, consistent with a net left-to-right shunt in this setting. Do not use the enriched pulmonary arterial sample as the pre-shunt mixed venous value.'),
  S('Preserve the Sampling Assumptions','**Use representative samples from the correct locations and a stable physiologic state.** An oximetry run helps identify where a saturation step-up occurs.',
    'The saturation shortcut assumes comparable hemoglobin and insignificant dissolved oxygen. Supplemental high-concentration oxygen can make dissolved oxygen important, requiring content-based calculation.',
    'Pulmonary venous desaturation, streaming, anomalous venous return and bidirectional shunting require careful interpretation. A calculated ratio does not by itself establish operability or identify the defect. Integrate anatomy, chamber loading, pulmonary pressure and resistance with disease-specific recommendations before deciding on closure. A large shunt ratio is not permission to ignore elevated resistance, just as a ratio near one does not exclude a clinically important lesion when competing shunt directions or measurement problems are present.')],['SHUNT'],style='direct',calculation=True)

R.update({
 'RHC2024':('JACC Heart Failure practical guidance for RHC hemodynamic assessment, 2024','https://doi.org/10.1016/j.jchf.2024.03.020'),
 'WEDGE':('Prospective study: role of wedge oxygen saturation during RHC, 2020','https://doi.org/10.1161/CIRCHEARTFAILURE.120.007981'),
 'RHCAHA':('AHA scientific statement: standardization of invasive hemodynamic protocols','https://doi.org/10.1161/HHF.0000000000000088'),
})

add('Flow, oxygen transport and resistance calculations','Discordant Cardiac Output Measurements',
 'An obese patient undergoing advanced heart-failure assessment has an indirect Fick output substantially higher than reproducible thermodilution measurements. Oxygen consumption was assumed from a formula. No shunt is identified. Which next approach best addresses the discrepancy?',
 'Review both methods and obtain measured oxygen consumption for direct Fick assessment if the discrepancy affects management',[
 ('Accept indirect Fick because its oxygen consumption input is independent of body habitus','Indirect Fick depends on an estimated consumption value that can be inaccurate in an individual patient; its formula-based input is not immune to body-size and metabolic variation.'),
 ('Accept thermodilution because reproducibility establishes absolute accuracy','Reproducibility supports measurement quality but does not eliminate systematic technical error or all physiologic limitations, so meaningful discordance still warrants review.'),
 ('Average the two outputs and use that value for transplant decisions','Averaging different potentially biased methods does not identify the valid estimate; decisions sensitive to output require resolving acquisition and assumption problems.')],
 [S('Distinguish Direct From Indirect Fick','**Direct Fick uses measured oxygen consumption; indirect Fick substitutes an estimate.** An error in assumed consumption is transmitted to the calculated output.',
    'Also review arterial and mixed venous sampling, hemoglobin, oxygen conditions and whether acquisition occurred in a stable state.',
    'A method’s familiar name does not establish that its inputs were directly measured or appropriate for this patient.'),
  S('Review Thermodilution Before Choosing a Result','**Check injection technique and the consistency of repeated curves.** Catheter position, timing, temperature and circulatory abnormalities can affect the measurement.',
    'Intracardiac shunts require special consideration and can invalidate routine thermodilution interpretation. Significant tricuspid regurgitation may also complicate assessment; avoid assuming one method is universally superior in every context.',
    'When a difference will change pulmonary resistance, advanced-therapy eligibility or treatment, resolve it rather than hiding it in an average. State which method supplied the final output and why it was selected. Recalculate derived resistances using the chosen validated flow. Agreement with an expected clinical label is not an adequate reason to prefer a number; use technical evidence and physiologic plausibility, then document residual uncertainty if it cannot be eliminated.')],['RHC2024','RHC'])

add('Right-heart catheterization and pressure waveforms','Pressure Transducer Level and Respiratory Timing',
 'During supine diagnostic RHC, the transducer has been zeroed to air but is positioned well below the mid-thoracic reference level. Which correction is appropriate before interpreting filling pressures?',
 'Relevel the transducer to the appropriate mid-thoracic reference and acquire respiratory-timed tracings',[
 ('Retain the transducer position and subtract right atrial pressure from every recorded pressure','Pressure differences may cancel a shared offset for some calculations, but this does not validate absolute filling pressures or justify retaining an incorrect reference level.'),
 ('Rezero to air without changing the transducer height','Zeroing addresses the atmospheric reference, whereas leveling addresses the hydrostatic relationship to the heart; repeating only the former does not correct the stated height error.'),
 ('Use the monitor’s whole-recording pressure average without releveling','An automated average neither removes hydrostatic offset nor necessarily handles respiration and ectopy appropriately; inspect valid leveled waveforms before interpretation.')],
 [S('Separate Leveling From Zeroing','**Zeroing and leveling are distinct steps.** The supine mid-thoracic reference approximates the left atrial level; a transducer positioned too low overreads pressure.',
    'A transducer positioned too high underreads pressure. Changes in patient position require reassessment of the reference rather than assuming a previously correct setup remains valid.',
    'Record the patient’s position and acquisition method so serial results can be compared meaningfully.'),
  S('Interpret Respiratory Effects Explicitly','**Acquire end-expiratory pressures without a breath-holding or Valsalva maneuver in the usual diagnostic framework.** Inspect the waveform rather than relying solely on a displayed number.',
    'Large respiratory swings, obesity, obstructive lung disease and positive-pressure ventilation require careful interpretation of intrathoracic pressure and the applicable protocol.',
    'Respiratory timing and cardiac-cycle timing address different questions. Mean atrial pressure and an end-diastolic pressure estimate may differ, particularly with large waves or arrhythmia. Document which quantity is reported rather than silently substituting one for another. A technically small pressure error can alter classification near a diagnostic cutoff, so resolve acquisition problems before diagnosing a disease or escalating therapy from an isolated borderline result.')],['RHCAHA','PH'])

add('Right-heart catheterization and pressure waveforms','Confirming a Genuine Pulmonary Arterial Wedge',
 'A purported wedge tracing retains a pulmonary arterial contour. Blood aspirated in that position has saturation 70%, while systemic arterial saturation is 97%. Which next step is most appropriate?',
 'Reassess catheter position and occlusion, obtain a valid wedge tracing and repeat the confirmatory sample',[
 ('Accept the pressure because the balloon is inflated to the expected volume','Expected balloon volume does not establish complete occlusion; the retained PA contour and venous-like saturation suggest an inadequate wedge position.'),
 ('Use pulmonary artery diastolic pressure as an equivalent substitute','PADP may approximate wedge pressure in selected circumstances, but pulmonary vascular disease can separate them; substituting it does not confirm the questioned measurement.'),
 ('Classify pulmonary hypertension using the recorded wedge and calculated PVR','Classification and resistance depend on a valid downstream pressure; using a questionable wedge can misclassify disease and distort treatment decisions.')],
 [S('Combine Waveform and Occlusion Evidence','**A genuine wedge should show an appropriate downstream atrial waveform rather than a retained PA contour.** A confirmatory aspirate should approach systemic arterial saturation when pulmonary oxygenation is normal.',
    'In this normoxemic patient, 70% is inconsistent with the expected arterialized sample and supports further assessment rather than acceptance.',
    'Use the appropriate careful sampling technique. Do not force an injection or aggressively manipulate an inflated balloon to obtain a desired number.'),
  S('Resolve Technical Doubt Before Clinical Classification','**Repeat positioning and review waveform quality, respiratory timing and the sample conditions.** Document uncertainty if a valid wedge cannot be obtained.',
    'Alternative assessment, including LV pressure measurement when justified, may help answer the clinical question, but LVEDP and mean PAWP are not interchangeable in every condition.',
    'Interpret saturation confirmation alongside the full acquisition, especially with hypoxemia or unusual pulmonary venous physiology. A numerical cutoff cannot replace correct technique. Recalculate PVR after establishing the appropriate downstream pressure and output. Avoid labeling a patient with precapillary or postcapillary disease solely because an unreliable number falls on one side of a threshold; the consequences of that error extend to treatment selection and advanced-therapy assessment.')],['WEDGE','RHC2024'])

R.update({
 'JVP':('Merck Manual professional: cardiovascular examination','https://www.merckmanuals.com/en-ca/professional/cardiovascular-disorders/approach-to-the-cardiac-patient/cardiovascular-examination'),
 'VWAVE':('Fuchs et al. limitations of wedge V waves in diagnosing MR, 1982','https://doi.org/10.1016/0002-9149(82)91968-3'),
})

add('Right-heart catheterization and pressure waveforms','Cannon a Waves and Atrioventricular Timing',
 'A patient with complete AV block has intermittent very large right atrial pressure waves aligned with P waves that occur during ventricular systole. Which mechanism explains these waves?',
 'Atrial contraction against a closed tricuspid valve',[
 ('Systolic regurgitant flow through an incompetent tricuspid valve','Tricuspid regurgitation produces prominent systolic v or fused c-v waves; the intermittent P-linked waves during AV dissociation instead identify cannon a waves.'),
 ('Atrial contraction into a persistently stiff but accessible right ventricle','Poor RV compliance can produce prominent a waves on each appropriately timed atrial contraction, whereas the intermittent giant waves here track unfavorable AV timing.'),
 ('Rapid passive right atrial emptying after tricuspid opening','Passive emptying generates the y descent, a fall in pressure after valve opening rather than a large P-linked pressure rise during ventricular systole.')],
 [S('Identify the Event Before Naming the Wave','**The a wave represents atrial contraction.** When contraction occurs against a closed tricuspid valve, a large cannon wave can result.',
    'Complete AV block permits changing atrial–ventricular timing, so giant waves may be intermittent. Other rhythms can also produce unfavorable timing; the wave alone does not establish complete heart block.',
    'Distinguish these waves from consistently prominent a waves caused by resistance to atrial emptying and from systolic regurgitant v waves.'),
  S('Correlate the Pressure Trace With the ECG','**Use simultaneous rhythm and waveform timing**, rather than identifying every tall wave by amplitude alone.',
    'The x descent relates to atrial relaxation and systolic annular motion; the y descent reflects atrial emptying after the tricuspid valve opens.',
    'Assess the patient’s rate, perfusion and rhythm independently of the waveform label. A conduction disorder may require urgent treatment, but a cannon wave is a mechanistic clue rather than a complete management prescription. Catheter motion and artifact should be excluded when a pressure deflection lacks a plausible relationship to the ECG. Document timing and reproducibility so that subsequent clinicians can distinguish a genuine hemodynamic sign from a nonspecific description of prominent venous pulsation.')],['JVP'])

add('Right-heart catheterization and pressure waveforms','Large Wedge v Waves Are Not Specific for Mitral Regurgitation',
 'A technically valid wedge tracing has large systolic v waves. High-quality valve imaging shows only mild MR, and the patient has substantial left atrial stiffness. Which interpretation is most appropriate?',
 'Low left atrial compliance can generate large v waves without severe MR',[
 ('The pressure tracing establishes severe MR despite the imaging findings','Large v waves are compatible with MR, but are not sufficiently specific to override adequate valve assessment; atrial compliance also determines the pressure rise during filling.'),
 ('A large v wave establishes primary pulmonary arterial disease','Primary pulmonary vascular resistance does not directly define the atrial systolic filling wave; the valid wedge and atrial stiffness point to downstream pressure behavior.'),
 ('Large v waves demonstrate vigorous left atrial contraction','Atrial contraction produces the a wave; the v wave reflects atrial filling during ventricular systole rather than active atrial contraction.')],
 [S('Relate Pressure to Atrial Volume Accommodation','**A stiff left atrium can develop a large systolic pressure rise during filling.** Regurgitant inflow is one possible contributor to a large v wave, not its only cause.',
    'Conversely, a compliant enlarged atrium may accommodate substantial regurgitant volume with a less dramatic pressure wave.',
    'The waveform therefore cannot independently grade MR severity. Integrate imaging, anatomy, loading and the quality of the pressure acquisition.'),
  S('Distinguish Mean Atrial Pressure From End-Diastolic Pressure','**Large v waves can raise mean PAWP above an end-diastolic pressure estimate.** Specify which quantity is being interpreted.',
    'Mean PAWP captures the pulmonary venous/atrial pressure burden and is used in PVR calculation; an end-diastolic measurement addresses a different comparison with LVEDP.',
    'Review discordance rather than choosing whichever pressure supports a preferred diagnosis. A valid atrial waveform may contain important physiology even when it does not match a simplistic valve label. If valve imaging is inadequate or acute MR remains clinically plausible, obtain appropriate additional imaging; that is different from declaring severe regurgitation from a tall wave alone. Reassess loading conditions and rhythm when comparing recordings obtained at different times.')],['VWAVE','RHCAHA','REGURG'])

add('Right-heart catheterization and pressure waveforms','Pulmonary Artery Diastolic Pressure Is Not Always Wedge Pressure',
 'A patient with substantial pulmonary vascular disease has pulmonary artery pressure 75/30 mmHg and a technically confirmed mean PAWP of 10 mmHg. Which value should supply the downstream pressure for PVR calculation?',
 'The confirmed mean PAWP of 10 mmHg',[
 ('The pulmonary artery diastolic pressure of 30 mmHg','PADP can approximate wedge pressure under suitable pulmonary vascular conditions, but the approximation fails with a substantial pulmonary vascular gradient as in this patient.'),
 ('The average of PADP and PAWP, 20 mmHg','Averaging measurements of different physiologic compartments does not create a validated downstream pressure and would underestimate the transpulmonary gradient here.'),
 ('The right atrial pressure measured during the same study','RAP is the downstream pressure used for systemic vascular resistance, not the pulmonary venous/left atrial pressure estimate required for PVR.')],
 [S('Keep the Pulmonary Vascular Compartments Distinct','**PADP is measured upstream in the pulmonary artery; PAWP estimates downstream pressure under appropriate occlusion conditions.** They may be close when resistance is low but are not interchangeable.',
    'A substantial separation can occur with pulmonary vascular disease. Using PADP instead of the valid wedge would erase part of the relevant pressure gradient.',
    'PVR uses mean PAP minus mean PAWP divided by the appropriate cardiac output. Do not substitute a systolic or diastolic PA pressure for the mean in that formula.'),
  S('Resolve a Questioned Wedge by Verification','**If a wedge appears implausible, confirm its acquisition rather than automatically replacing it with PADP.** Review contour, respiratory timing, level and occlusion evidence.',
    'This stem explicitly supplies a technically confirmed wedge, so there is no basis for replacing it with a numerically higher pressure simply because pulmonary arterial pressure is high.',
    'The diastolic pulmonary gradient and PVR describe related but different aspects of physiology. Contemporary disease classification should use the specified guideline framework rather than an isolated surrogate. A pressure discrepancy is information to interpret, not an error to eliminate by averaging. Document the original measured values and the reasoning behind derived calculations so that classification and subsequent treatment decisions remain traceable to valid inputs.')],['PH','RHC2024'])

R['CONSTRICT']=('ESC educational review: constrictive pericarditis and restrictive cardiomyopathy','https://www.escardio.org/communities/councils/cardiology-practice/scientific-documents-and-publications/ejournal/volume-15/Constrictive-pericarditis-role-of-echocardiography-and-magnetic-resonance-imaging/')

add('Right-heart catheterization and pressure waveforms','Precapillary Pulmonary Hypertension: Contemporary Thresholds',
 'Which resting hemodynamic combination meets the 2022 ESC/ERS definition of precapillary pulmonary hypertension?',
 'Mean PAP 23 mmHg, PAWP 12 mmHg and PVR 2.5 Wood units',[
 ('Mean PAP 20 mmHg, PAWP 12 mmHg and PVR 2.5 Wood units','The definition requires mean PAP greater than 20, so a value exactly 20 does not meet the resting PH threshold despite the elevated resistance.'),
 ('Mean PAP 23 mmHg, PAWP 17 mmHg and PVR 2.5 Wood units','The wedge is above 15 and therefore indicates a postcapillary component; with PVR above 2 this is a combined pattern rather than purely precapillary PH.'),
 ('Mean PAP 23 mmHg, PAWP 12 mmHg and PVR 2.0 Wood units','The precapillary definition requires PVR greater than 2; with low wedge and PVR at or below 2, elevated mean pressure may represent an unclassified hemodynamic pattern.')],
 [S('Apply All Three Conditions','**The 2022 ESC/ERS resting precapillary definition requires mean PAP above 20 mmHg, PAWP at or below 15 mmHg and PVR above 2 Wood units.** Each boundary matters.',
    'A pressure of 20 is not above 20, and a resistance of 2 is not above 2. The proposed correct combination satisfies all three conditions.',
    'The lower contemporary thresholds should not be replaced by the older mean PAP threshold of 25 or an older PVR threshold when the question explicitly names this framework.'),
  S('Separate a Hemodynamic Pattern From Etiology','**Precapillary PH is not synonymous with group 1 pulmonary arterial hypertension.** Lung disease, chronic thromboembolic disease and other causes require assessment.',
    'Use validated invasive measurements and the clinical investigation pathway to establish the cause. Echo estimates alone do not provide the same three-variable invasive classification.',
    'A revised diagnostic boundary does not mean every patient near the new threshold has established benefit from the same drug regimen used in older trials. Review symptoms, risk factors, imaging and the quality of the wedge and output measurements before treatment decisions. Borderline findings may need further context or reassessment; the classification is a starting point for causal evaluation rather than permission to assign a specific pulmonary vasodilator.')],['PH'],style='direct')

add('Right-heart catheterization and pressure waveforms','Combined Post- and Precapillary Pulmonary Hypertension',
 'A stable patient has mean PAP 32 mmHg, mean PAWP 20 mmHg and cardiac output 4 L/min. The measurements are technically valid. Under 2022 ESC/ERS definitions, which pattern is present?',
 'Combined post- and precapillary pulmonary hypertension',[
 ('Isolated postcapillary pulmonary hypertension','The elevated wedge establishes a postcapillary component, but PVR is (32-20)/4 = 3 WU, exceeding the 2-WU boundary for an isolated postcapillary pattern.'),
 ('Precapillary pulmonary hypertension without a postcapillary component','The wedge is above 15 mmHg, so the case does not meet the low-wedge requirement for a purely precapillary classification.'),
 ('Unclassified pulmonary hypertension with low resistance','That category can apply to elevated mean PAP with PAWP at or below 15 and PVR at or below 2; neither the wedge nor resistance in this patient fits it.')],
 [S('Calculate Resistance Before Assigning the Pattern','**The transpulmonary gradient is 32 − 20 = 12 mmHg and PVR is 12/4 = 3 Wood units.** Mean PAP and PAWP are elevated.',
    'With mean PAP above 20, PAWP above 15 and PVR above 2, the pattern is combined post- and precapillary PH.',
    'If PVR were at or below 2 with the same elevated mean PAP and wedge, the hemodynamic label would be isolated postcapillary PH.'),
  S('Do Not Turn the Label Into an Automatic Drug Choice','**A combined pattern identifies increased resistance in addition to elevated downstream pressure.** It does not itself establish group 1 PAH or an indication for a PAH-specific drug.',
    'Evaluate the left-heart substrate, volume state, valve disease and other contributors. Confirm that pressure and flow values were acquired under comparable stable conditions.',
    'A large v wave, an incorrect wedge or an inaccurate output can alter the derived resistance. Use mean PAWP for the resistance calculation rather than substituting an end-diastolic value without explaining the purpose. Management follows the underlying disease and applicable evidence. Repeating or extending assessment is preferable to treating a technically questionable boundary value as a definitive etiologic diagnosis.')],['PH','RHCAHA'],table=(['Pattern with mean PAP >20 mmHg','PAWP','PVR'],[
 ['Precapillary','≤15 mmHg','>2 WU'],['Isolated postcapillary','>15 mmHg','≤2 WU'],
 ['Combined post- and precapillary','>15 mmHg','>2 WU'],['Unclassified low-resistance pattern','≤15 mmHg','≤2 WU']]))

add('Right-heart catheterization and pressure waveforms','Respiratory Ventricular Discordance in Constriction',
 'A patient with unexplained systemic venous congestion undergoes simultaneous LV and RV pressure recording during spontaneous breathing. With inspiration, RV systolic pressure rises while LV systolic pressure falls. Which diagnosis is most strongly supported by this dynamic finding?',
 'Constrictive pericarditis',[
 ('Restrictive cardiomyopathy','Restriction can produce high filling pressures and a dip-and-plateau contour, but usually preserves concordant respiratory ventricular pressure changes rather than the stated reciprocal behavior.'),
 ('Isolated pulmonary arterial hypertension','Pulmonary vascular disease can elevate RV pressure, but an elevated right-sided pressure alone does not explain the characteristic reciprocal LV/RV respiratory coupling.'),
 ('Severe tricuspid regurgitation','TR can cause venous congestion and large right atrial systolic waves, but does not by itself establish the demonstrated dynamic biventricular pressure discordance.')],
 [S('Use Dynamic Interaction Rather Than a Static Contour Alone','**Constriction exaggerates ventricular interdependence and limits transmission of intrathoracic pressure to the cardiac chambers.** Inspiration favors RV filling at the expense of LV filling.',
    'Simultaneous recordings can therefore show reciprocal respiratory changes in ventricular systolic pressures. Compare equivalent beats and identify the respiratory phase directly.',
    'Equalized diastolic pressures or a dip-and-plateau pattern are less specific and can also occur with restrictive physiology.'),
  S('Integrate Invasive and Imaging Evidence','**Use echo and CT or CMR to evaluate physiology and the pericardium.** A normal pericardial thickness does not exclude constriction.',
    'Respiratory septal shift, tissue-Doppler behavior and hepatic venous flow can contribute to the assessment; no single anatomic or pressure finding should replace the integrated diagnosis.',
    'Rhythm irregularity, loading conditions and ventilation can complicate interpretation, and mixed myocardial–pericardial disease may occur. Establish the cause and whether inflammation or chronic fixed constriction is present before selecting therapy. The diagnostic value here arises from the simultaneous dynamic behavior, not simply the fact that both filling pressures are high. Document acquisition conditions so a later reviewer can verify that apparent discordance was not created by comparing unrelated beats or separate respiratory cycles.')],['CONSTRICT','RHC2024'])

R.update({
 'TEE':('ASE/SCA comprehensive adult TEE examination guideline, 2013','https://www.asecho.org/wp-content/uploads/2025/04/2013_Performing-Comprehensive-TEE.pdf'),
 'DOPPLER':('ASE recommendations for Doppler echocardiographic quantification','https://anesthesia.bidmc.harvard.edu/ADEL/documents/echo/ASE%20Recommendations%20for%20Quantification%20of%20Doppler%20Echo%202001.pdf'),
})

add('Echocardiographic measurements and interpretation','Selecting TEE After a Nondiagnostic Transthoracic Study',
 'A patient with suspected important mitral leaflet pathology has a technically inadequate TTE despite optimization. Detailed leaflet anatomy will change an imminent repair decision. There is no relevant esophageal contraindication. Which next test most directly addresses the question?',
 'Transesophageal echocardiography',[
 ('Repeat an unchanged transthoracic acquisition on the next day','Repeat TTE can help if conditions or technique can improve, but this optimized inadequate study leaves a decision requiring detailed leaflet imaging that TEE can provide.'),
 ('Radionuclide myocardial perfusion imaging','Perfusion imaging assesses ischemia and viability-related questions, but does not provide the required detailed mitral leaflet anatomy for repair planning.'),
 ('Coronary CT angiography','Coronary anatomy may be needed separately before intervention, but a coronary-focused CT does not most directly resolve the stated leaflet-mechanism question.')],
 [S('Match the Test to the Unresolved Anatomy','**TEE can provide high-resolution imaging of posterior cardiac structures and detailed mitral anatomy**, particularly when transthoracic windows are inadequate.',
    'The value lies in answering a management-relevant question, not simply obtaining an additional test. TTE remains the usual initial study for many structural assessments.',
    'Three-dimensional TEE can clarify the affected leaflet segments and mechanism when available and technically adequate.'),
  S('Plan a Safe and Useful Examination','**Assess esophageal history, airway and sedation risks before proceeding.** A technically attractive modality may be unsuitable when procedural risk is unacceptable.',
    'Esophageal obstruction, perforation or other important pathology requires an appropriate alternative assessment and specialist risk evaluation. Monitoring and preparation follow the procedural protocol.',
    'Interpret valve severity under the acquisition’s loading conditions, since sedation and changes in blood pressure can alter regurgitation. TEE anatomy and Doppler findings complement rather than erase a valid earlier assessment. If the study will not change a decision or the question is already answered by adequate TTE, its added invasiveness may not be justified. Explain the specific purpose and use the resulting mechanism assessment to inform the multidisciplinary intervention plan.')],['TEE','REGURG'])

add('Echocardiographic measurements and interpretation','Doppler Peak Instantaneous Pressure Gradient',
 'Continuous-wave Doppler records a peak velocity of 4.0 m/s across a stenotic valve. Proximal velocity is negligible. Using the simplified Bernoulli equation, what is the peak instantaneous pressure gradient?',
 '64 mmHg',[
 ('16 mmHg','Multiplying velocity by four without squaring gives this value; the simplified relationship is four times velocity squared.'),
 ('32 mmHg','This does not follow the stated simplified Bernoulli relationship for a peak velocity of four meters per second.'),
 ('80 mmHg','This value is not obtained by substituting the measured velocity into four times velocity squared.')],
 [S('Square the Velocity Before Multiplication','**Peak instantaneous gradient = 4 × Vmax²**, with velocity in m/s and gradient in mmHg under the usual simplified assumptions.',
    'Substitute 4 × (4.0)² = 4 × 16 = ==64 mmHg==. The velocity must be squared; an error in measured velocity is therefore amplified.',
    'This calculation estimates the pressure difference at the instant of peak velocity, not an average over systole.'),
  S('Keep Different Gradients Distinct','**Mean Doppler gradient is obtained by averaging instantaneous gradients through the ejection period.** It is not four times the square of an arithmetic mean velocity.',
    'A catheter peak-to-peak gradient compares pressure peaks that occur at different times and is not interchangeable with a Doppler peak instantaneous gradient.',
    'The simplified equation neglects proximal velocity; when it is substantial, the fuller velocity-difference relationship may be needed. Doppler alignment matters because an oblique beam underestimates velocity. Pressure recovery, flow state and serial obstructions can also complicate comparison with invasive data. Do not grade a valve or decide on intervention from this isolated arithmetic result: integrate valve area, mean gradient, flow, anatomy and symptoms. State the type of gradient in the report so the number is not later misread as an invasive or mean measurement.')],['DOPPLER'],style='direct',calculation=True)

add('Echocardiographic measurements and interpretation','LVOT Doppler Stroke Volume',
 'LVOT diameter is 2.0 cm and the correctly acquired pulsed-wave LVOT VTI is 20 cm. Assuming a circular LVOT, what is Doppler stroke volume?',
 'Approximately 63 mL',[
 ('Approximately 31 mL','This is half the correct result and does not follow the area calculation using the stated two-centimeter diameter.'),
 ('Approximately 80 mL','Multiplying diameter squared by VTI without the circle-area factor gives 80, but area is πd²/4 rather than diameter squared alone.'),
 ('Approximately 126 mL','This doubles the correct result; the cross-sectional area for a two-centimeter diameter is approximately 3.14 square centimeters.')],
 [S('Multiply Cross-Sectional Area by Flow Distance','**Stroke volume = LVOT area × LVOT VTI.** With a circular assumption, area = πd²/4 = 0.785 × d².',
    'For d = 2.0 cm, area is 0.785 × 4 = 3.14 cm². Multiply by VTI 20 cm to obtain 62.8 cm³, or ==approximately 63 mL==.',
    'VTI is a distance traveled during one beat, not peak velocity and not a minute-volume measurement.'),
  S('Preserve Measurement Consistency','**Use diameter and Doppler sampling that refer to the appropriate corresponding outflow location.** Diameter error is squared in the area calculation.',
    'Sample placement in accelerated flow or Doppler misalignment can bias the result. Irregular rhythm requires appropriate beat selection and averaging rather than mixing incompatible cycles.',
    'Cardiac output would require multiplication by heart rate and conversion from mL to L. This forward outflow measurement is not necessarily total LV ejection when regurgitation is present; aortic regurgitation also separates antegrade systolic flow from net systemic flow. Interpret changes using comparable technique and loading conditions. A plausible numerical result does not validate an inadequately visualized diameter or a poorly acquired envelope, so review the original images when the derived stroke volume conflicts with the clinical picture.')],['REGURG','DOPPLER'],style='direct',calculation=True)

R.update({
 'STRAIN':('ASE/EACVI clinical consensus: clinical applications of strain echocardiography','https://academic.oup.com/ehjcimaging/article/27/3/335/8445935'),
 'DIA2025':('ASE diastolic function and HFpEF diagnostic recommendations, 2025','https://www.asecho.org/wp-content/uploads/2025/07/Left-Ventricular-Diastolic-Function.pdf'),
})

add('Echocardiographic measurements and interpretation','Squared Diameter Error in LVOT Calculations',
 'An LVOT diameter of 2.0 cm is entered as 1.8 cm. All VTIs are unchanged. By approximately what percentage are the calculated LVOT stroke volume and continuity-equation aortic valve area underestimated?',
 '19%',[
 ('10%','Ten percent is the diameter error, but the area term depends on diameter squared, amplifying its effect on calculated flow and valve area.'),
 ('5%','The diameter is ten percent lower, and squaring amplifies rather than halves that error.'),
 ('36%','This exceeds the exact area error for the stated diameters; compare 1.8 squared with 2.0 squared rather than subtracting unrelated squared percentages.')],
 [S('Calculate the Ratio Before the Percentage','**Area is proportional to diameter squared.** The entered-to-true area ratio is 1.8²/2.0² = 3.24/4.00 = 0.81.',
    'Calculated area is therefore 81% of the true value, an ==underestimate of 19%==. At unchanged VTI, LVOT stroke volume has the same proportional error.',
    'Continuity-equation valve area also scales with LVOT area when both relevant VTIs remain unchanged, so its calculated value is underestimated by the same percentage.'),
  S('Review the Source of Discordant Valve Measurements','**A small diameter error can materially change a derived valve area.** The flow velocity and gradient may remain unchanged while the calculated area appears smaller.',
    'Inspect the original diameter, sampling site, geometric assumption and Doppler envelopes before interpreting discordant stenosis severity.',
    'The approximate small-error rule doubles the fractional diameter error, but the exact squared ratio gives 19% rather than 20% here. A noncircular outflow tract introduces another limitation of a single two-dimensional diameter. Do not correct a suspected error by choosing a diameter that produces an expected valve area; reacquire or independently verify the measurement. Clinical decisions integrate symptoms, flow and other valid severity measures, with additional imaging when appropriate. Preserve the raw measurements so a reviewer can distinguish a genuine physiologic discrepancy from a calculation or acquisition problem.')],['REGURG','DOPPLER'],style='direct',calculation=True)

add('Echocardiographic measurements and interpretation','Strain Changes and Loading Conditions',
 'Serial studies show GLS changing from −20% to −16%, while EF remains similar. The second examination was acquired during marked hypertension using different analysis software. Which interpretation is most appropriate?',
 'Longitudinal shortening appears reduced, but loading and technical comparability must be reviewed before attributing it to new myocardial injury',[
 ('Longitudinal shortening has improved because −16 is numerically greater than −20','Less negative longitudinal strain represents a smaller magnitude of shortening, not better shortening; the sign convention must be interpreted correctly.'),
 ('New intrinsic myocardial injury is established despite the changed acquisition conditions','A reduced GLS magnitude can be clinically important, but loading and software differences can affect the result and prevent this unqualified causal conclusion.'),
 ('The GLS change can be disregarded because EF has not changed','Strain may identify dysfunction not apparent from EF, so a stable EF does not justify dismissing the change; the appropriate response is contextual review.')],
 [S('Interpret the Sign and Magnitude','**Longitudinal shortening is conventionally expressed as negative strain.** A change from −20% to −16% is a reduction in absolute shortening magnitude.',
    'EF and GLS describe different aspects of chamber behavior and need not change in parallel. A preserved EF does not establish normal longitudinal mechanics.',
    'Numerical interpretation precedes disease attribution: recognizing a worse value does not establish why it changed.'),
  S('Assess Serial Comparability','**Blood pressure, loading, rhythm, image quality and analysis method can influence strain.** Use comparable acquisition and software where possible.',
    'Review tracking, region-of-interest placement, frame quality and timing before diagnosing progression from a serial difference.',
    'Repeat or corroborate a clinically important finding under appropriate conditions and integrate symptoms, biomarkers and the disease-specific context. Avoid applying a universal diagnostic cutoff to every vendor, age group or clinical indication. A relative change may have a defined role in a particular surveillance protocol, but that protocol’s assumptions and baseline quality remain necessary. This patient’s hypertension and changed software create identifiable alternative explanations that must be addressed before assigning new myocardial injury or changing treatment on the strain value alone.')],['STRAIN'])

add('Echocardiographic measurements and interpretation','A Normal-Appearing E/A Ratio Does Not Exclude Raised Filling Pressure',
 'A symptomatic patient in sinus rhythm has transmitral E/A of 1.1. Mitral annular relaxation velocities are reduced and other measurements raise concern for elevated filling pressure. Which interpretation is most appropriate?',
 'The inflow ratio may be pseudonormal; integrate tissue Doppler and other filling-pressure evidence',[
 ('An E/A ratio near one establishes normal diastolic function','A near-normal ratio can occur when elevated atrial pressure restores early inflow despite impaired relaxation; it cannot independently establish normal function.'),
 ('Reduced annular relaxation velocity alone establishes elevated atrial pressure','A low e′ supports impaired relaxation but does not by itself prove elevated filling pressure; relaxation and pressure assessment must be distinguished.'),
 ('Preserved EF excludes a clinically important filling abnormality','EF describes fractional ejection and does not exclude diastolic dysfunction or elevated filling pressure; the symptom and Doppler findings require assessment.')],
 [S('Understand Pseudonormal Filling','**Transmitral E and A velocities reflect pressure gradients as well as relaxation.** Increased atrial pressure can augment early filling despite impaired myocardial relaxation.',
    'The resulting E/A ratio can resemble a normal pattern. Age, heart rate, atrial function and loading further influence the ratio.',
    'Use a multiparameter assessment rather than assigning normal function from the apparent inflow balance.'),
  S('Separate Relaxation From Pressure Estimation','**Tissue Doppler e′ helps assess relaxation, while E/e′ and other evidence contribute to pressure assessment.** Neither quantity is universally reliable in isolation.',
    'The 2025 ASE update incorporates a structured assessment with complementary measurements and disease-specific considerations. Rhythm, valve disease and technical limitations determine which framework is applicable.',
    'Atrial size can reflect chronic pressure burden but is affected by other conditions and does not establish the pressure at one moment. Pulmonary pressure estimates also require interpretation of the right-heart and pulmonary context. When noninvasive findings remain indeterminate and exertional symptoms persist, further appropriate functional or invasive assessment may be necessary. Diagnose a clinical HFpEF syndrome using the complete evidence, rather than equating either a normal EF or one abnormal Doppler measure with the final diagnosis.')],['DIA2025','DIASTOLE'])

R['RV2025']=('ASE right-heart assessment and pulmonary hypertension guideline, 2025','https://www.asecho.org/wp-content/uploads/2025/03/PIIS0894731725000379.pdf')

add('Echocardiographic measurements and interpretation','Diastolic Assessment in Atrial Fibrillation',
 'A patient with persistent AF has exertional dyspnea and preserved EF. The operator cannot identify a consistent transmitral A wave and obtains variable E velocities across beats. Which approach best reflects the 2025 ASE guidance?',
 'Use the AF-specific multiparameter assessment with representative-cycle averaging',[
 ('Use E/A from the single beat with the clearest late-diastolic deflection','AF lacks organized atrial contraction, so a deflection should not be treated as a reliable sinus-rhythm A wave; selecting one attractive beat also ignores cycle variability.'),
 ('Use one septal E/e′ measurement as the definitive pressure estimate','E/e′ can contribute to an AF-specific assessment, but the guideline does not support a single parameter as a sufficiently reliable stand-alone pressure marker.'),
 ('Use LA enlargement alone as evidence of elevated current filling pressure','AF itself and chronic remodeling can enlarge the atrium; chamber size alone does not determine the current pressure or replace the multiparameter approach.')],
 [S('Use a Framework Appropriate to the Rhythm','**AF alters filling assessment through loss of organized atrial contraction and variable cycle length.** The sinus-rhythm E/A framework cannot simply be applied unchanged.',
    'The 2025 ASE update provides a separate AF pathway and recommends representative measurements across several cycles. No single echo marker supplies a sufficiently strong stand-alone pressure estimate.',
    'Select cycles that reflect the average heart rate rather than extreme intervals that generate misleadingly high or low velocities.'),
  S('Combine Complementary Findings','**The AF pathway integrates inflow, annular and pulmonary-pressure information.** Additional atrial and pulmonary venous findings can help when the initial assessment is unresolved.',
    'Acquire technically valid signals and retain an indeterminate result when information is inadequate rather than forcing a normal or elevated label.',
    'Consider important valve disease and other disease-specific exceptions before applying an algorithm. Even a technically sound pressure estimate is one component of explaining dyspnea; assess ischemic, pulmonary and other causes according to context. If resting results do not explain symptoms, further appropriately selected testing may be needed. Document rhythm, rate and averaging so subsequent studies can be compared meaningfully rather than interpreting beat-selection differences as disease progression.')],['DIA2025'])

add('Echocardiographic measurements and interpretation','TAPSE Does Not Fully Describe Right Ventricular Function',
 'A patient with severe functional TR has TAPSE 2.0 cm but marked RV enlargement, abnormal free-wall strain and impaired fractional area change. Which interpretation is most appropriate?',
 'The apparently preserved TAPSE does not exclude RV dysfunction; integrate the other measures and loading context',[
 ('RV systolic function is normal because TAPSE exceeds 1.7 cm','TAPSE assesses longitudinal annular excursion and may overestimate function in severe TR or altered annular geometry; it cannot negate the other abnormal findings.'),
 ('The strain result must be discarded whenever TAPSE is normal','Strain and annular excursion capture different behavior and have distinct technical limitations; disagreement calls for integrated review, not automatic rejection of strain.'),
 ('RV dysfunction can be established only after an invasive pressure study','Invasive hemodynamics may answer selected questions, but a comprehensive echo can identify RV dysfunction; catheterization is not required solely to recognize these concordant abnormalities.')],
 [S('Recognize What TAPSE Measures','**TAPSE measures longitudinal motion of the lateral tricuspid annulus**, not the entire RV contraction pattern or effective forward output.',
    'A value above 1.7 cm is generally within the normal range, but severe TR, loading and altered annular mechanics can produce misleading preservation.',
    'Check alignment and image quality, then interpret excursion alongside the chamber’s size, shape and other functional measures.'),
  S('Use a Comprehensive Right-Heart Assessment','**Integrate fractional area change, tissue velocities, free-wall strain and three-dimensional measures when feasible.** Each supplies complementary information.',
    'Assess TR severity, pulmonary loading, venous congestion and forward flow. Apparent improvement in a load-sensitive index does not necessarily indicate myocardial recovery.',
    'Use CMR or invasive assessment when a specific unresolved question will alter management, rather than treating a single discordant index as a reason to ignore the remainder of the study. Serial comparisons require similar views, technique and loading. The 2025 ASE guideline emphasizes systematic right-heart evaluation; reporting one normal-looking number without the abnormal context can obscure clinically important maladaptation and delay an appropriate valve or pulmonary vascular assessment.')],['RV2025'])

add('Echocardiographic measurements and interpretation','Estimating RV Systolic Pressure From a TR Jet',
 'A complete, well-aligned TR jet has peak velocity 3.0 m/s. Estimated RAP is 8 mmHg, and there is no pulmonary valve or RV outflow obstruction. What is the estimated pulmonary artery systolic pressure?',
 '44 mmHg',[
 ('36 mmHg','This is the RV-to-RA systolic gradient alone; estimated RAP must be added to obtain RV systolic pressure.'),
 ('28 mmHg','This subtracts RAP from the Doppler gradient, whereas RV systolic pressure is the RV-to-RA gradient plus RAP.'),
 ('72 mmHg','This does not follow the stated TR velocity and RAP using the simplified Bernoulli relationship.')],
 [S('Calculate the Gradient and Add Downstream Pressure','**The TR-derived RV–RA gradient is 4 × velocity².** With velocity 3.0 m/s, the gradient is 4 × 9 = 36 mmHg.',
    'RV systolic pressure is 36 + 8 = ==44 mmHg==. In the absence of an RV outflow or pulmonary valve gradient, this approximates pulmonary artery systolic pressure.',
    'If an outflow obstruction is present, RV systolic pressure cannot simply be relabeled as pulmonary artery systolic pressure.'),
  S('Recognize the Uncertainty in the Estimate','**Both jet measurement and estimated RAP contribute error.** Incomplete envelopes or Doppler misalignment can underestimate velocity, and squaring amplifies velocity error.',
    'RAP estimation from venous imaging also has limitations. Severe TR and altered pressure equilibration may make a simple gradient estimate misleading.',
    'This estimate is not a direct mean pulmonary artery pressure, wedge pressure or pulmonary vascular resistance. It cannot independently classify PH or establish an indication for pulmonary vasodilator therapy. Interpret echo probability with other right-heart signs and the clinical context, obtaining invasive confirmation when it will inform a relevant decision. An absent measurable TR jet does not prove normal pulmonary pressure, just as one elevated estimate does not establish a specific pulmonary vascular diagnosis.')],['RV2025','PH'],style='direct',calculation=True)

R.update({
 'CCS':('ESC chronic coronary syndromes guideline, 2024','https://doi.org/10.1093/eurheartj/ehae177'),
 'CHEST':('AHA/ACC multisociety chest pain guideline, 2021','https://doi.org/10.1016/j.jacc.2021.07.053'),
})

add('Echocardiographic measurements and interpretation','Doppler Alignment Before Assigning Valve Severity',
 'A calcified aortic valve has an unexpectedly low recorded velocity. The initial continuous-wave beam is oblique to the jet, and an alternative acoustic window has not been attempted. Which next step is most appropriate?',
 'Repeat optimized Doppler acquisition from appropriate windows before concluding that obstruction is mild',[
 ('Classify the lesion as mild using the currently recorded peak velocity','A low velocity is informative only when acquisition is adequate; an oblique beam underestimates the component of flow along the beam.'),
 ('Classify the lesion as severe from calcification regardless of hemodynamics','Calcification supports structural disease, but does not independently establish hemodynamic severity; optimize measurements and integrate the full assessment.'),
 ('Use the same oblique velocity to calculate a more precise pressure gradient','Applying the Bernoulli equation cannot correct an underestimated input velocity; mathematical precision does not repair acquisition bias.')],
 [S('Correct Acquisition Before Interpretation','**Doppler measures the velocity component parallel to the ultrasound beam.** Oblique alignment can underestimate peak velocity and its derived gradient.',
    'Interrogate the jet from appropriate acoustic windows and trace a complete, correctly identified envelope. Confirm that the signal is the intended outflow jet rather than another high-velocity flow.',
    'Squaring velocity in the gradient formula amplifies measurement error; calculation is not a substitute for alignment.'),
  S('Investigate Persistent Discordance Systematically','**After obtaining valid signals, integrate valve area, mean gradient, flow and morphology.** A genuinely low-flow state can also produce a low gradient despite important obstruction.',
    'Review LVOT diameter, VTI sampling, blood pressure and rhythm. Additional stress or anatomic imaging may answer a residual question when appropriately indicated.',
    'Do not choose an assumed severity first and then adjust measurements until they fit it. Record which windows supplied the highest reliable signal and why a study remains limited if acquisition is inadequate. Symptoms and ventricular response matter for clinical management, but neither removes the need for technical validity. A repeat optimized examination can be more useful than escalating directly to another modality on the basis of a preventable Doppler error.')],['DOPPLER'])

add('Ischemia testing and coronary physiology','Anatomic Testing for Suspected Stable Coronary Disease',
 'A 48-year-old with stable exertional chest discomfort has a low-to-moderate clinical likelihood of obstructive CAD and no known coronary disease. The immediate question is whether coronary plaque or obstructive anatomy is present. Sinus rhythm, renal function and contrast history favor CT acquisition. Which test most directly answers that question?',
 'Coronary CT angiography',[
 ('Stress echocardiography','Stress echo assesses inducible functional consequences and is useful when ischemia is the principal question, but does not directly map nonobstructive coronary plaque or the coronary lumen.'),
 ('Stress myocardial perfusion imaging','Perfusion testing is appropriate for ischemia assessment, but a normal perfusion result does not provide the requested anatomic exclusion of coronary plaque.'),
 ('Invasive coronary angiography as the initial diagnostic study','Invasive angiography is appropriate for selected high-risk findings or severe refractory symptoms, but the stated stable patient and favorable noninvasive anatomy question support CCTA first.')],
 [S('Distinguish Anatomy From Ischemia','**CCTA evaluates coronary lumen and plaque**, making it useful for excluding obstructive anatomy in appropriately selected patients.',
    'Stress imaging addresses whether a physiologic demand or vasodilator challenge produces evidence of ischemia. The tests answer overlapping but different questions.',
    'The 2024 ESC framework selects tests using clinical likelihood, patient characteristics and the intended management decision rather than one universal test for all chest pain.'),
  S('Select and Interpret the Study in Context','**Image quality depends on rhythm, motion and calcification**, while contrast exposure and patient cooperation affect suitability.',
    'A stenosis seen anatomically does not automatically establish functional significance or a need for revascularization. Selected intermediate findings may need functional assessment.',
    'Likewise, absence of obstructive epicardial disease does not exclude every coronary cause of symptoms, including microvascular or vasomotor disease. Explain the result in relation to the question asked. New unstable symptoms require a different urgent evaluation rather than simply continuing an elective stable-chest-pain pathway. Avoid duplicate testing when a high-quality study has already resolved the relevant question, and use a second modality when a specific unresolved finding will change care.')],['CCS','CHEST'])

add('Ischemia testing and coronary physiology','Exercise ECG With an Uninterpretable Baseline',
 'A patient with stable symptoms needs noninvasive ischemia assessment. The resting ECG shows LBBB, and the patient can exercise adequately. Which principle should guide test selection?',
 'Choose an appropriate imaging-based ischemia test rather than diagnosing ischemia from exercise ST shifts alone',[
 ('Use standard exercise ECG because adequate exercise capacity restores ST specificity','Adequate exercise enables workload assessment, but does not remove the baseline repolarization abnormality that limits ischemic ST interpretation in LBBB.'),
 ('Use a larger ST-depression threshold to make exercise ECG diagnostically reliable','Changing the threshold does not validate routine ischemic ST interpretation in LBBB; choose a suitable alternative rather than inventing a correction.'),
 ('Proceed to invasive angiography solely because LBBB prevents exercise ECG interpretation','LBBB limits this particular test, but does not by itself require invasive angiography; imaging-based noninvasive strategies remain available according to the clinical question.')],
 [S('Separate Exercise Information From ST Interpretation','**An uninterpretable resting ECG limits the use of exercise-induced ST changes for ischemia diagnosis.** LBBB, ventricular pacing and certain other baseline abnormalities require a different diagnostic strategy.',
    'Exercise can still provide information about symptoms, capacity, blood pressure and rhythm. These observations do not make the ST segment a reliable ischemia test.',
    'Choose imaging or anatomic testing according to the intended question, clinical likelihood and local expertise.'),
  S('Account for Modality-Specific Artifacts','**LBBB can also affect imaging interpretation**, including septal perfusion or motion patterns. A test must be selected and interpreted with that context.',
    'Vasodilator perfusion imaging is often useful; stress echo, CMR or anatomic assessment may be appropriate in selected circumstances. Review each option’s limitations rather than treating all imaging as equivalent.',
    'Assess exercise and pharmacologic contraindications before proceeding. The need for a test should arise from its likely effect on diagnosis or management, not merely an abnormal resting ECG. If the chosen study is equivocal, review acquisition and the LBBB-related pattern before escalating to invasive testing. A technically limited test should be reported as such rather than labeled negative simply because the desired diagnostic endpoint could not be interpreted.')],['CHEST','CCS'])

R.update({
 'STRESS2026':('ASNC guideline for SPECT/PET myocardial perfusion stress testing, 2026','https://www.journalofnuclearcardiology.org/article/S1071-3581%2826%2900351-X/fulltext'),
 'SPECT':('EACVI consensus on performance and interpretation of SPECT/SPECT-CT, 2025','https://pmc.ncbi.nlm.nih.gov/articles/PMC12096082/'),
})

add('Ischemia testing and coronary physiology','Pharmacologic Stress When Vasodilators Are Unsuitable',
 'An otherwise stable patient cannot exercise because of orthopedic disability and needs a functional ischemia test. The laboratory has documented a significant contraindication to vasodilator stress because of bronchospastic disease. Echo windows are adequate, with no important arrhythmia, severe hypertension or dynamic LV outflow obstruction. Which strategy is most suitable?',
 'Dobutamine stress echocardiography with appropriate monitoring',[
 ('Adenosine perfusion imaging with the usual infusion','Adenosine is useful when vasodilator stress is appropriate, but the documented bronchospastic contraindication makes it unsuitable in this specific patient.'),
 ('Dipyridamole perfusion imaging as a nonvasodilator alternative','Dipyridamole produces vasodilator stress through endogenous adenosine effects; it is not a way to avoid the stated vasodilator contraindication.'),
 ('Exercise stress echocardiography using a reduced workload','Exercise imaging is useful when sufficient safe exercise is feasible, but orthopedic disability prevents the needed diagnostic exercise challenge here.')],
 [S('Match the Stress Mechanism to the Contraindication','**Dobutamine increases cardiac workload through adrenergic stimulation**, providing a functional alternative when exercise is inadequate and vasodilator stress is unsuitable.',
    'The stem supplies adequate acoustic windows and excludes important competing contraindications. Selection still requires a complete pretest safety assessment.',
    'Do not confuse a different vasodilator agent with a different physiologic stress mechanism.'),
  S('Perform a Monitored Protocol','**Monitor ECG, blood pressure, symptoms and wall motion throughout stress and recovery.** Use a validated laboratory protocol with trained staff and rescue capability.',
    'Review beta blockade and other medicines that can affect target response. Arrhythmias, ischemia, hypotension and obstruction are relevant complications.',
    'Acute bronchospasm, unstable symptoms or another active illness may require postponement of an elective study rather than immediate substitution of a drug. Stable pulmonary disease also does not imply that every vasodilator is universally prohibited; the question specifies an established contraindication. Record whether an adequate diagnostic stress endpoint was reached, because an incomplete study should not be labeled a definitive negative result. Choose another modality if acoustic quality or the actual clinical question makes stress echo unsuitable.')],['STRESS2026','CHEST'])

add('Ischemia testing and coronary physiology','Attenuation Artifact and Balanced Ischemia',
 'SPECT shows a mild inferior defect that disappears on prone and correctly registered attenuation-corrected images, with preserved regional thickening. Which interpretation is most appropriate?',
 'Attenuation artifact is favored over a fixed infarct in that region',[
 ('A transmural inferior infarct is established by the initial fixed defect','A fixed perfusion defect can indicate scar, but its disappearance after artifact-directed correction and preserved thickening argue against assuming a transmural infarct.'),
 ('Reversible inferior ischemia is established by changing patient position','A position-related change tests attenuation; it is not the same as a stress-to-rest reversible defect caused by altered coronary flow.'),
 ('Normal corrected relative perfusion excludes all clinically important multivessel disease','Correction resolves the apparent regional defect, but relative perfusion can miss balanced reductions in multivessel flow and cannot exclude every coronary disease mechanism.')],
 [S('Review the Acquisition Before Assigning Pathology','**Soft-tissue attenuation can create a perfusion defect without corresponding myocardial injury.** Position changes, attenuation correction and gated function help evaluate this possibility.',
    'Check raw projections, motion and registration. A misregistered correction map can introduce rather than eliminate an artifact.',
    'Preserved thickening supports the interpretation here but is not an independent guarantee that every fixed defect is artifactual.'),
  S('Remember the Relative Nature of Conventional Perfusion Images','**Balanced global flow reduction may produce less obvious regional contrast.** A seemingly uniform distribution does not ensure normal absolute flow.',
    'Interpret high-risk symptoms, ECG findings, stress function and other supportive markers together. Quantitative flow assessment with an appropriate modality can answer selected unresolved questions.',
    'Do not send every mild defect directly to invasive angiography without reviewing technical validity, and do not dismiss a clinically high-risk presentation solely because relative images appear uniform. The test report should distinguish attenuation correction from true stress–rest reversibility and state residual limitations. A defensible interpretation explains why the observed pattern favors artifact while preserving the separate question of the patient’s overall coronary risk and need for further investigation.')],['SPECT','CCS'])

add('Ischemia testing and coronary physiology','FFR and iFR Decision Thresholds',
 'During assessment of an intermediate coronary stenosis in a stable patient, which pair matches the 2024 ESC thresholds for hemodynamic significance?',
 'FFR ≤0.80 and iFR ≤0.89',[
 ('FFR ≤0.89 and iFR ≤0.80','This reverses the commonly used thresholds; hyperemic FFR and resting wave-free iFR are distinct indices with different decision boundaries.'),
 ('FFR ≤0.75 and iFR ≤0.89','An FFR boundary near 0.75 has historical diagnostic significance, but the stated contemporary decision threshold is 0.80 rather than 0.75.'),
 ('FFR ≤0.80 and iFR ≤0.95','The FFR threshold fits, but 0.95 is not the iFR significance threshold specified in this guideline.')],
 [S('Distinguish the Two Measurements','**FFR assesses a distal-to-aortic pressure ratio during maximal hyperemia**, whereas iFR assesses a selected resting diastolic period without requiring the same hyperemic challenge.',
    'The stated decision boundaries are ==FFR ≤0.80== and ==iFR ≤0.89==. Equality meets the specified threshold.',
    'These are physiologic assessments of a lesion, not visual percentage-stenosis grades.'),
  S('Use a Threshold Within a Valid Clinical Assessment','**Check pressure equalization, waveform quality and drift**, and ensure an adequate hyperemic response when interpreting FFR.',
    'Serial lesions, diffuse disease, microvascular dysfunction and special hemodynamic contexts can complicate interpretation. Discordant indices require review rather than automatic averaging.',
    'A physiologically significant value contributes to a revascularization decision alongside symptoms, anatomy, medical treatment and procedural considerations. It does not independently prescribe a stent. Conversely, a value above the threshold does not prove that all symptoms are noncoronary: vasomotor or microvascular disease may remain relevant. Document the actual value and acquisition conditions rather than reducing the report to positive or negative, particularly near a boundary where technical error and the broader evidence deserve attention.')],['CCS'],style='direct')

R['CPET']=('AHA clinician guide to cardiopulmonary exercise testing in adults','https://doi.org/10.1161/CIR.0b013e3181e52e69')

add('Ischemia testing and coronary physiology','Microvascular Dysfunction Despite a Nonischemic FFR',
 'A patient has persistent angina without obstructive coronary disease. A technically adequate study shows FFR 0.92, reduced coronary flow reserve and IMR 32 units. Which interpretation best fits?',
 'Coronary microvascular dysfunction without a flow-limiting focal epicardial lesion',[
 ('A focal epicardial stenosis established by the FFR result','An FFR of 0.92 does not meet the usual ≤0.80 threshold for a significant focal lesion; the abnormal microvascular measurements answer a different question.'),
 ('Normal coronary physiology because the FFR is above threshold','FFR does not exclude microvascular dysfunction; reduced flow reserve and elevated IMR remain abnormal despite the absence of a significant focal pressure drop.'),
 ('Epicardial vasospasm established by the elevated IMR','IMR assesses microvascular resistance, whereas epicardial spasm requires an appropriate vasomotor assessment with clinical and electrocardiographic correlation.')],
 [S('Separate Pressure-Limiting Stenosis From Microvascular Function','**A nonischemic FFR does not establish normal microcirculation.** Flow reserve and microvascular resistance provide complementary information.',
    'The 2024 ESC guideline identifies IMR at or above 25 units as increased. The stated value of 32 supports a microvascular abnormality in the technically valid clinical context.',
    'Reduced CFR can also reflect diffuse epicardial disease or altered resting flow; it should not be assigned a cause without the other measurements and anatomy.'),
  S('Use the Endotype to Inform Further Care','**Persistent symptoms with nonobstructive arteries warrant a coherent diagnostic assessment**, rather than dismissal because angiography or FFR lacks a focal target.',
    'Review measurement method, hyperemic response, hemodynamics and competing noncoronary causes. Vasospasm may coexist and requires a distinct assessment.',
    'Treatment should follow the identified mechanism and clinical guidance, including risk-factor management and appropriately selected antianginal therapy. The result does not create a focal lesion for stenting. Explain what each test has excluded and what remains abnormal so the patient understands why a reassuring epicardial pressure ratio does not negate the symptom mechanism. Record raw values and method because flow-reserve boundaries and resistance measures depend on the technique used.')],['CCS'])

add('Ischemia testing and coronary physiology','Vasomotor Testing Answers a Different Question From FFR',
 'Recurrent rest angina continues despite nonobstructive angiography and FFR above the ischemic threshold. Episodes suggest a dynamic coronary mechanism. Which specialist investigation most directly evaluates inducible coronary spasm?',
 'Intracoronary acetylcholine provocation with symptom, ECG and angiographic assessment',[
 ('Repeat FFR during adenosine hyperemia','FFR assesses pressure loss across epicardial disease during hyperemia, but does not replace provocation for a suspected dynamic vasospastic mechanism.'),
 ('Repeat resting iFR measurement','A resting pressure ratio can assess an intermediate lesion, but a normal result between episodes cannot exclude inducible coronary spasm.'),
 ('Coronary calcium scoring','Calcium scoring describes calcified plaque burden and risk, but does not test dynamic coronary vasoreactivity or establish the cause of episodic rest angina.')],
 [S('Identify the Vasomotor Endotype','**Acetylcholine testing assesses coronary vasoreactivity in an experienced laboratory.** Interpret reproduction of symptoms and ischemic ECG changes together with the angiographic response.',
    'Epicardial spasm and microvascular spasm are distinct findings; the absence of a large-vessel constriction does not make every provoked ischemic response negative.',
    'A normal fixed-lesion pressure ratio answers a different physiologic question and does not exclude a dynamic disorder.'),
  S('Use a Controlled Specialist Protocol','**Provocation requires appropriate selection, monitoring and reversal capability.** Arrhythmia and sustained spasm are relevant procedural risks.',
    'Document the protocol, observed response and recovery. Do not infer a positive diagnosis from nonspecific discomfort without corroborating findings.',
    'Integrate the result with the spontaneous presentation and other causes of chest pain. Once an endotype is established, treatment can be directed to that mechanism rather than repeated searches for an angiographic stenosis. A negative provocation study must also be interpreted within its technical and clinical limitations. Explain that nonobstructive coronary anatomy and the absence of ischemic FFR are compatible with certain coronary disorders, while avoiding the opposite mistake of labeling all persistent chest pain as coronary spasm without adequate evidence.')],['CCS'])

add('Ischemia testing and coronary physiology','Integrated Interpretation of Cardiopulmonary Exercise Testing',
 'A technically valid CPET shows reduced peak VO2, a high VE/VCO2 slope, preserved breathing reserve and RER 1.15 at peak exercise. Which conclusion is most appropriate?',
 'Exercise capacity is reduced despite substantial effort; circulatory and pulmonary vascular contributors require integrated assessment',[
 ('Low motivation is the most likely explanation for the reduced peak VO2','A peak RER of 1.15 supports substantial metabolic effort, so low motivation cannot be assumed from the low peak VO2 alone.'),
 ('A primary mechanical ventilatory ceiling is established','A preserved breathing reserve argues against a simple mechanical ventilatory ceiling; the remaining pattern requires integration with gas exchange, circulatory response and clinical context.'),
 ('The high VE/VCO2 slope specifically establishes left ventricular systolic failure','Ventilatory inefficiency occurs in several cardiac and pulmonary vascular or lung disorders, so this variable is not specific for LV systolic failure.')],
 [S('Assess Effort Before Interpreting Capacity','**Peak VO2 reflects achieved exercise oxygen uptake**, and interpretation requires the adequacy of effort and the exercise protocol.',
    'RER is VCO2/VO2. The stated 1.15 supports substantial effort, but should be integrated with symptoms, workload and the complete test rather than used as a universal binary validity rule.',
    'Heart-rate targets alone can be misleading with beta blockade, chronotropic dysfunction or pacing.'),
  S('Integrate Ventilation and Circulation','**A high VE/VCO2 slope indicates ventilatory inefficiency**, which is not unique to one disease. Preserved breathing reserve does not exclude every pulmonary abnormality.',
    'Review oxygen saturation, end-tidal gases, oxygen pulse, blood-pressure response, ECG and the trajectory of oxygen uptake relative to work.',
    'The pattern can guide further evaluation for circulatory or pulmonary vascular limitation, while anemia, deconditioning and other contributors remain relevant. Oxygen pulse includes both stroke volume and extraction effects and is not a direct stroke-volume tracing. Use disease-specific prognostic thresholds only within their validated setting; do not apply a transplant criterion to an undiagnosed patient simply because peak VO2 is low. A useful report explains the observed limitation and remaining differential rather than converting one variable into a definitive diagnosis.')],['CPET'])

R.update({
 'SCCT':('SCCT expert consensus on coronary CT angiography, 2021','https://pmc.ncbi.nlm.nih.gov/articles/PMC8713482/'),
 'SCMR':('SCMR standardized CMR interpretation and post-processing, 2020 update','https://pmc.ncbi.nlm.nih.gov/articles/PMC7066763/'),
})

add('CT, CMR and multimodality selection','Coronary Calcium Blooming and Nondiagnostic CT Segments',
 'CCTA shows extensive calcification in a proximal coronary segment. Blooming obscures the residual lumen, and the reader cannot reliably grade stenosis. Which interpretation is most appropriate?',
 'Report the segment as limited or nondiagnostic and select further assessment according to symptoms and clinical risk',[
 ('Report a severe stenosis because calcified plaque fills the apparent lumen','Blooming can exaggerate plaque dimensions and stenosis; an obscured lumen does not justify assigning a precise severe grade without adequate visualization.'),
 ('Report the segment as nonobstructive because calcium is a stable plaque feature','Calcification does not exclude important obstruction, and a nondiagnostic lumen cannot be treated as a negative anatomic result.'),
 ('Repeat the same acquisition without changing technical or patient factors','A repeat may help when a correctable problem exists, but repeating identical conditions does not reliably resolve severe calcium blooming and adds exposure without a defined benefit.')],
 [S('Distinguish Plaque Detection From Lumen Grading','**Calcium blooming can obscure the contrast-filled lumen and overestimate narrowing.** The presence of plaque may be certain while the stenosis grade remains uncertain.',
    'Review reconstruction and image quality, but do not claim precision beyond what the acquisition supports. A nondiagnostic segment is not a normal segment.',
    'Motion, irregular rhythm and other acquisition factors can further limit CCTA; renal and contrast considerations also affect test selection.'),
  S('Choose the Next Test for the Remaining Question','**Further functional or invasive assessment depends on the clinical context.** A patient with high-risk symptoms requires a different response from one with low-risk stable symptoms.',
    'Functional imaging may clarify ischemic significance when anatomic grading is uncertain; invasive angiography may be appropriate when risk or symptoms justify it.',
    'Avoid assuming that every heavily calcified artery needs intervention or that a calcium-rich plaque is harmless. The report should name the affected segment and limitation so that an apparently reassuring overall summary does not hide an unevaluated proximal vessel. New unstable symptoms must be evaluated through an acute pathway rather than managed solely by this elective imaging interpretation.')],['SCCT','CCS'])

add('CT, CMR and multimodality selection','A Zero Calcium Score Does Not Exclude Noncalcified Plaque',
 'A symptomatic 42-year-old has a coronary calcium score of zero. Which conclusion is justified?',
 'No detectable calcified plaque was identified, but noncalcified coronary disease is not excluded',[
 ('Obstructive coronary disease is excluded regardless of symptom characteristics','A zero calcium score lowers probability in appropriate settings but does not exclude noncalcified plaque or every obstructive lesion, particularly in younger symptomatic patients.'),
 ('The symptoms are nonischemic because calcium scoring is a stress test','Calcium scoring measures calcified plaque burden; it does not impose a stress challenge or directly assess myocardial ischemia.'),
 ('Noncalcified plaque is present and explains the symptoms','A zero score does not exclude noncalcified plaque, but it also does not establish its presence or prove that symptoms have a coronary cause.')],
 [S('State What the Test Actually Measures','**A calcium score describes detectable coronary calcification**, not the entire plaque burden or the physiologic consequences of a lesion.',
    'A zero score can be useful risk information, but its meaning depends on age, symptoms and the clinical setting.',
    'Noncalcified plaque may be present before detectable calcification. CCTA and functional studies answer different questions that a calcium scan cannot replace.'),
  S('Use the Result Within the Appropriate Pathway','**Symptoms still require assessment according to their acuity and clinical likelihood.** A low calcium burden should not override a high-risk presentation.',
    'In a stable patient, select further testing only when it addresses a relevant unresolved question. In acute suspected ischemia, follow the appropriate ECG, biomarker and clinical pathway.',
    'Preventive decisions also integrate risk factors and guideline-specific exceptions rather than reducing every choice to one score. Avoid both overclaiming that zero means no disease and overcorrecting by assuming occult plaque must be responsible. Explain the distinction to the patient: the scan is reassuring about the measured burden while leaving selected mechanisms unresolved. Documentation should preserve this qualified interpretation so later clinicians do not read a zero score as a lifetime guarantee against coronary disease or an exclusion test for all chest pain.')],['SCCT','CHEST','CCS'])

add('CT, CMR and multimodality selection','Ischemic Versus Nonischemic Late Gadolinium Enhancement',
 'CMR shows subendocardial LGE extending toward transmural involvement in contiguous segments that match a coronary territory. Which interpretation is most strongly supported?',
 'An ischemic myocardial injury pattern',[
 ('A typical nonischemic midwall fibrosis pattern','Midwall fibrosis often spares the subendocardium and does not necessarily follow one coronary distribution; that differs from the pattern explicitly described.'),
 ('A typical nonischemic subepicardial injury pattern','Subepicardial enhancement can occur in myocarditis and other nonischemic conditions, but the stated subendocardial territorial involvement instead favors ischemic injury.'),
 ('Active edema without evidence of established tissue injury','LGE describes expanded contrast distribution and delayed washout in injured tissue; active edema requires appropriate complementary sequences and is not established by this LGE pattern alone.')],
 [S('Interpret Distribution Before Assigning Etiology','**Ischemic injury typically involves the subendocardium and follows a coronary territory**, with greater transmural extent in more extensive injury.',
    'Nonischemic patterns often involve the midwall or subepicardium and spare the subendocardium, although disease-specific exceptions and mixed patterns exist.',
    'The pattern supports an injury mechanism; it does not by itself identify current coronary anatomy or prove that an acute occlusion is ongoing.'),
  S('Integrate Tissue Characterization With the Clinical Timeline','**LGE is not a stand-alone clock for injury or a direct measure of active inflammation.** Compare edema-sensitive imaging, function and clinical evidence.',
    'Report location, intramural distribution and extent. Distinguish a territorial pattern from diffuse subendocardial involvement in infiltrative or other noncoronary disease.',
    'Viability and potential functional recovery relate to scar extent but should not be reduced to a promise of benefit from revascularization based on one image. Symptoms, coronary anatomy, ischemia and the broader treatment evidence remain relevant. Check image quality, nulling and artifact before labeling enhancement. A technically sound pattern can be highly informative while still requiring correlation to distinguish a prior infarct from a current acute presentation or concurrent nonischemic disease.')],['SCMR'])

R.update({
 'MAPPING':('Expert recommendations: CMR in nonischemic myocardial inflammation, 2018','https://doi.org/10.1016/j.jacc.2018.09.072'),
 'THROMBUS':('AHA scientific statement on LV thrombus, 2022','https://doi.org/10.1161/CIR.0000000000001092'),
 'CMRCHD':('SCMR reporting guideline for congenital heart disease, 2024','https://www.journalofcmr.com/article/S1097-6647%2824%2901089-5/fulltext'),
})

add('CT, CMR and multimodality selection','CMR Mapping Supports Tissue Characterization, Not a Specific Pathogen',
 'A patient with suspected acute myocardial inflammation has elevated myocardial T2 and a nonischemic T1-based abnormality on a technically adequate CMR. Which conclusion is most appropriate?',
 'The combination supports myocardial inflammation in the appropriate clinical context but does not identify its specific cause',[
 ('The findings establish a viral pathogen without further evaluation','Mapping identifies tissue properties rather than a microbial organism; the cause of inflammation requires clinical and sometimes additional etiologic assessment.'),
 ('An elevated T2 measurement alone establishes the complete diagnosis','T2 supports edema, but the contemporary tissue framework integrates complementary T1-based evidence and the clinical presentation rather than using one value in isolation.'),
 ('The findings establish irreversible fibrosis as the only explanation','Edema and other tissue changes can alter mapping values; abnormal mapping does not mean that every affected region represents permanent fibrosis.')],
 [S('Combine Complementary Tissue Markers','**The updated Lake Louise approach combines a T2-based edema marker with a T1-based injury marker.** The latter can include nonischemic LGE, elevated native T1 or increased extracellular volume.',
    'The combination increases confidence in myocardial inflammation when the clinical presentation is appropriate. It does not independently prove a particular pathogen or immune mechanism.',
    'Individual values depend on acquisition and reference standards; a universal millisecond cutoff is inappropriate across different scanners and sequences.'),
  S('Interpret the Scan Within the Clinical Course','**Timing and disease distribution affect sensitivity.** A negative or incomplete tissue study does not resolve every possible inflammatory presentation.',
    'Integrate symptoms, ECG, biomarkers, ventricular function and alternative explanations, including ischemic injury. Biopsy has selected indications when its result can guide urgent management.',
    'Do not prescribe immunosuppression solely because a mapping value is high. Treatment depends on the clinical syndrome, severity and suspected or established cause. Serial imaging may help assess evolution, but changes should be compared using technically consistent acquisition and interpreted with recovery of function and symptoms. A report should distinguish observed edema or injury from an etiologic diagnosis rather than turning a sensitive tissue signal into certainty about the mechanism.')],['MAPPING','SCMR'])

add('CT, CMR and multimodality selection','CMR for Unresolved Left Ventricular Thrombus',
 'After an anterior infarction with apical akinesis, a patient has an equivocal apical mass on TTE. Imaging remains nondiagnostic despite an ultrasound-enhancing agent, and determining whether thrombus is present will change treatment. CMR is feasible. Which next test is most appropriate?',
 'CMR with a protocol designed to assess LV thrombus',[
 ('Routine TEE as the preferred method for every LV apical mass','TEE is valuable for atrial, valvular and selected aortic questions, but does not universally improve LV apical assessment; CMR is specifically useful after unresolved contrast-enhanced TTE.'),
 ('A repeat noncontrast TTE using the same inadequate apical views','Repeat echo can help if acquisition can improve, but unchanged limited views do not address the persistent uncertainty after contrast enhancement.'),
 ('Myocardial perfusion SPECT to establish whether the mass is thrombus','Perfusion imaging can assess ischemia or scar-related questions, but is not the most direct tissue-characterization test for this unresolved LV mass.')],
 [S('Escalate When the Result Changes Management','**The AHA statement identifies CMR as particularly useful when suspected LV thrombus remains unresolved on echo even with an enhancing agent.** Persistent concern despite a negative echo can also justify CMR.',
    'Use appropriate cine and tissue-characterization sequences rather than assuming any generic cardiac MR acquisition answers the thrombus question.',
    'Distinguish thrombus from trabeculation, artifact and other masses using the complete imaging pattern.'),
  S('Separate Diagnosis From the Subsequent Treatment Decision','**Confirming thrombus affects antithrombotic management**, but bleeding risk, concomitant antiplatelet therapy and the clinical setting still matter.',
    'A suspected lesion should be described as uncertain until adequately assessed; an apparently negative limited view should not be treated as definitive exclusion.',
    'Check device, renal and other CMR considerations before selecting the protocol. When CMR is unavailable or unsuitable, discuss an appropriate alternative with imaging specialists rather than repeatedly performing the same nondiagnostic acquisition. Document the question and whether it was resolved. Follow-up imaging must be planned in the context of the treatment course; resolution should be established with an adequate method rather than inferred from symptom improvement alone.')],['THROMBUS','SCMR'])

add('CT, CMR and multimodality selection','CMR Shunt Quantification and Right Ventricular Volumes',
 'An adult with a suspected atrial-level left-to-right shunt has RV enlargement that is difficult to quantify by TTE. The clinical team needs reproducible RV volumes and pulmonary-to-systemic flow assessment. Which examination most directly combines these measurements?',
 'CMR cine ventricular volumetry with appropriately planned phase-contrast flow measurements',[
 ('Coronary calcium scoring with gated CT','Calcium scoring measures calcified coronary plaque and does not provide the required ventricular volumetry and circuit-specific flow quantification.'),
 ('TEE focused on the atrial septum without quantitative flow acquisition','TEE can define septal anatomy, but a focused anatomic study does not provide the same comprehensive RV volume and pulmonary/systemic flow measurements requested here.'),
 ('Myocardial perfusion SPECT with gated EF measurement','Gated perfusion imaging can assess LV function and perfusion, but is not the preferred integrated method for RV volumetry and direct shunt-flow quantification.')],
 [S('Combine Chamber Response With Flow','**Cine CMR quantifies ventricular volumes and EF**, while velocity-encoded phase-contrast imaging measures flow through appropriately selected vessels.',
    'In a simple atrial-level shunt, pulmonary and systemic flow measurements can quantify Qp/Qs, while RV volume documents the chamber consequence.',
    'Index volumes to body size and report the acquisition and contouring convention for meaningful comparison over time.'),
  S('Plan Measurements for the Actual Anatomy','**Flow sites must match the lesion.** A simple main-pulmonary-artery to ascending-aortic comparison is not universally valid for every congenital connection or collateral pathway.',
    'Check velocity encoding, plane alignment, background phase offsets and internal flow consistency. Regurgitation and additional shunts complicate ventricular stroke-volume comparisons.',
    'An elevated Qp/Qs or enlarged RV does not independently establish suitability for closure. Integrate anatomy, symptoms, pulmonary pressures and resistance under disease-specific guidance. CMR does not replace invasive pressure assessment when operability depends on it. A useful report states net forward flows and the assumptions used rather than presenting an unexplained ratio. When different flow or volume estimates disagree, review the anatomy and acquisition before attributing the discrepancy to a new lesion.')],['CMRCHD','SCMR'])

R.update({
 'CIEDCMR':('SCMR consensus on CMR in patients with implanted cardiac devices, 2024','https://events.scmr.org/wp-content/uploads/2024/08/CMR-with-implantable-cardiac-devices.pdf'),
 'GAD':('ACR–NKF consensus on gadolinium contrast in kidney disease','https://pmc.ncbi.nlm.nih.gov/articles/PMC7873723/'),
 'KDIGO':('KDIGO CKD guideline, 2024','https://kdigo.org/wp-content/uploads/2024/03/KDIGO-2024-CKD-Guideline.pdf'),
})

add('CT, CMR and multimodality selection','CMR With a Non-MR-Conditional Cardiac Device',
 'CMR could resolve a management-relevant tissue question in a patient with a non-MR-conditional pacemaker system. Which approach best reflects contemporary specialist guidance?',
 'Assess the complete device system and consider protocolized imaging at an experienced center with electrophysiology support',[
 ('Exclude CMR solely because the system lacks an MR-conditional label','The label affects risk assessment, but selected nonconditional systems can undergo MRI under specialized protocols; it is not a universal prohibition.'),
 ('Proceed with a routine scan because the pacemaker generator was recently implanted','A recent generator does not establish whole-system conditionality or safe scanning; leads, dependence, programming and other factors require review.'),
 ('Replace the tissue question with coronary CT because any cardiac CT is diagnostically equivalent','CT can answer selected anatomic questions, but it is not automatically equivalent to the requested CMR tissue assessment; an alternative must answer the actual clinical question.')],
 [S('Assess the Whole System and Clinical Benefit','**Device safety depends on the generator, leads and their combination**, not the generator label alone. Review dependence, battery status, lead integrity and abandoned or other higher-risk leads.',
    'The 2024 SCMR consensus supports selected nonconditional-device imaging within an appropriate specialist pathway, usually at 1.5 T.',
    'Consider whether artifact will still permit the intended diagnosis. A safely acquired but uninterpretable study may not provide the expected benefit.'),
  S('Use a Complete Safety Protocol','**Coordinate pre- and post-scan interrogation, appropriate programming and continuous monitoring.** Trained staff, emergency capability and device-specific planning are essential.',
    'Follow the relevant consent process and local protocol. Do not generalize evidence from selected systems to every lead configuration or perform an improvised routine scan.',
    'If the required expertise or protocol is unavailable, discuss referral or another modality that can resolve the question. The choice balances diagnostic benefit, procedural risk and alternative information. Record why CMR is needed and how its safety and expected image quality were assessed. Device conditionality is a technical classification, not a guarantee that a particular scan is appropriate or an automatic reason to abandon a potentially useful investigation.')],['CIEDCMR'])

add('CT, CMR and multimodality selection','Gadolinium Selection in Advanced Kidney Disease',
 'A patient with stable eGFR 24 mL/min/1.73 m² needs management-relevant contrast-enhanced CMR. Noncontrast alternatives will not answer the question. Which strategy best reflects ACR–NKF guidance?',
 'Consider an appropriate group II agent at the lowest diagnostic dose after individualized benefit–risk assessment',[
 ('Cancel every gadolinium-enhanced examination whenever eGFR is below 30','Advanced kidney disease requires agent-specific assessment, but the very low NSF risk of group II agents does not support a blanket prohibition on clinically necessary examinations.'),
 ('Use any available gadolinium agent because all groups have equivalent NSF risk','NSF risk differs by agent group; avoiding higher-risk agents is a meaningful part of selecting contrast for advanced kidney disease.'),
 ('Initiate hemodialysis solely to permit the planned group II contrast dose','ACR–NKF guidance does not recommend starting or altering dialysis solely because a group II agent is administered; that would introduce an unnecessary intervention.')],
 [S('Use Agent-Specific Rather Than Blanket Risk Assessment','**Group II gadolinium agents have a very low documented NSF risk even in advanced kidney disease.** Weigh that risk against the harm of withholding a necessary diagnostic examination.',
    'Use an appropriate agent and the lowest dose that provides the diagnostic information. Determine whether the patient has stable CKD or acute kidney injury and review recent exposures.',
    'KDIGO 2024 similarly favors lower-risk ACR agent groups when gadolinium is required below a GFR of 30; selection follows the current product and institutional policy.'),
  S('Keep Contrast Types and Procedures Distinct','**Gadolinium safety is not the same question as iodinated CT contrast safety.** Do not transfer a rule between them without evaluating its evidence.',
    'Explain the reason contrast is needed and document alternatives. Renal disease does not remove the need for an adequate imaging protocol or informed discussion.',
    'Dialysis should not be started or changed solely for the stated group II exposure. Conversely, low NSF risk does not justify unnecessary contrast or disregard of hypersensitivity and other patient factors. Reassess the clinical question if a noncontrast sequence can genuinely provide the needed answer. The goal is a useful diagnostic study with an appropriate agent, rather than either indiscriminate administration or automatic refusal based on a single eGFR threshold.')],['GAD','KDIGO'])

R.update({
 'MI2026':('Joint ESC/ACC/AHA/WHF Fifth Universal Definition of MI, 2026','https://doi.org/10.1093/eurheartj/ehag101'),
 'HF':('ESC acute and chronic heart failure guideline, 2021','https://doi.org/10.1093/eurheartj/ehab368'),
 'AECG':('ISHNE–HRS ambulatory ECG monitoring consensus, 2017','https://www.hrsonline.org/wp-content/uploads/2025/02/2017-ISHNE-HRS-Ambulatory-ECG.pdf'),
})

add('Biomarkers, monitoring and integrated investigation strategy','Acute Myocardial Injury Is Not Automatically Infarction',
 'During an acute systemic illness, high-sensitivity troponin rises and falls with values above the assay’s sex-specific 99th percentile. No ischemic symptoms, new ischemic ECG changes or imaging evidence of ischemic injury have been established. Which conclusion is justified now?',
 'Acute myocardial injury is present; myocardial infarction requires additional etiologic assessment and supporting evidence',[
 ('An acute myocardial infarction is established by the troponin kinetics alone','Dynamic troponin elevation establishes acute injury, but does not independently establish infarction; investigate the mechanism and evidence supporting ischemia or acute coronary pathology.'),
 ('Chronic myocardial injury is established because systemic illness is present','Chronic injury describes persistently elevated values without the relevant acute change; the stated rise and fall instead supports an acute injury pattern.'),
 ('A normal coronary circulation can be assumed because there are no ischemic symptoms','Absent symptoms do not prove normal coronaries or exclude silent ischemia; the current evidence requires assessment rather than an unqualified exclusion.')],
 [S('Separate the Biomarker Pattern From the Final Diagnosis','**The 2026 Fifth Universal Definition identifies acute injury by a rise and/or fall with at least one troponin value above the sex-specific 99th percentile.** This establishes injury, not its cause.',
    'MI requires additional evidence supporting acute ischemia or acute coronary pathology. Review symptoms, ECG and appropriate cardiac or coronary imaging according to the presentation.',
    'The 2026 classification updates earlier terminology; do not automatically convert every illness-associated elevation into an infarction subtype.'),
  S('Investigate the Clinical Mechanism','**Treat instability and evaluate the trigger while clarifying the cardiac findings.** Systemic illness and coronary pathology can coexist.',
    'Interpret serial measurements with the assay and sampling interval. An elevated biomarker is clinically meaningful even when an infarction diagnosis is not yet established.',
    'Do not prescribe an acute coronary antithrombotic regimen solely from this label without evaluating benefit, bleeding risk and the actual syndrome. Conversely, do not dismiss a concerning presentation as nonspecific because another illness is present. The appropriate next investigation depends on the evolving evidence. Document the supported finding and unresolved mechanism rather than replacing uncertainty with a more specific diagnosis than the data justify.')],['MI2026'])

add('Biomarkers, monitoring and integrated investigation strategy','Natriuretic Peptides in Obesity and Atrial Fibrillation',
 'An obese patient has persistent exertional dyspnea and clinical concern for HFpEF despite a relatively low natriuretic peptide value. Which interpretation is most appropriate?',
 'Obesity can lower peptide concentrations; persistent clinical suspicion warrants integrated assessment',[
 ('The low value excludes HFpEF regardless of body habitus','Low peptides can help exclude HF in appropriate settings, but obesity can suppress values and HFpEF may remain plausible when clinical evidence is compelling.'),
 ('Any elevation would specifically establish HFpEF as the cause of dyspnea','AF, kidney dysfunction, age and other cardiac or pulmonary conditions can elevate peptides; an elevated value is not specific for this syndrome.'),
 ('Renal dysfunction generally lowers peptide values in the same way as obesity','Kidney dysfunction commonly increases natriuretic peptide concentrations rather than producing the same suppressive effect described for obesity.')],
 [S('Interpret the Concentration in Its Setting','**Obesity can reduce natriuretic peptide concentrations**, while AF, increasing age and kidney dysfunction can raise them.',
    'The same numerical result therefore has different implications across clinical settings. Acute and nonacute diagnostic pathways also use different interpretation frameworks.',
    'Use the actual assay and clinical purpose rather than transferring a threshold between BNP, NT-proBNP and unrelated settings.'),
  S('Integrate Symptoms With Objective Assessment','**A peptide result is one component of evaluating suspected heart failure.** Assess congestion, ventricular and valve structure, diastolic findings and competing explanations for dyspnea.',
    'If resting results remain inconclusive in a patient with exertional symptoms, appropriately selected exercise or invasive assessment may resolve the question.',
    'Avoid both overdiagnosis from an isolated elevated value and premature exclusion from a low value in a context that reduces sensitivity. Follow changes using a comparable assay and interpret them alongside treatment, renal status and rhythm. A biomarker trend does not independently establish the correct diuretic dose or explain every symptom. The final diagnosis should reconcile the clinical presentation with the objective findings rather than allow one laboratory result to override the rest of the evidence.')],['HF','DIA2025'])

add('Biomarkers, monitoring and integrated investigation strategy','Ambulatory Monitoring Duration Should Match Symptom Frequency',
 'A stable patient has brief palpitations every two to three weeks. Baseline ECG is nondiagnostic, and there is no high-risk feature requiring admission. Which initial ambulatory strategy offers the best chance of symptom–rhythm correlation?',
 'An external loop or suitable extended monitor covering several weeks',[
 ('A single 24-hour Holter as a definitive exclusion test','A short Holter is useful for daily symptoms, but an uneventful day does not exclude an intermittent arrhythmia occurring every several weeks.'),
 ('A repeat resting ECG at the next routine appointment','A resting ECG may capture a persistent rhythm abnormality, but has a low chance of recording the brief infrequent symptomatic event described.'),
 ('An implantable loop recorder before trying an appropriate external strategy','An implantable recorder is useful for selected very infrequent or unresolved events, especially syncope contexts, but is more invasive than the suitable several-week external approach here.')],
 [S('Plan for the Expected Event Interval','**Less frequent symptoms require longer monitoring to improve capture.** A 24–48-hour Holter is best suited to events occurring daily or nearly daily.',
    'An external loop recorder or other suitable extended device can cover the interval expected for these palpitations. Choose activation and automatic-detection capability that fit the event.',
    'An implantable recorder has a role when the expected interval or previous nondiagnostic evaluation justifies it; it is not the automatic first choice for every palpitation.'),
  S('Seek Correlation Rather Than Incidental Findings Alone','**Record symptom timing and compare it with the actual rhythm.** A detected arrhythmia is not necessarily the cause of an unrelated symptom.',
    'Normal rhythm during the representative symptom can also be useful evidence. A recording without the typical event has a different meaning from one that captures it.',
    'Review device adherence, signal quality and whether episodes are too brief for manual activation. Syncope, exertional events, significant structural disease or other high-risk features may change the urgency and setting. The stem excludes those concerns to focus on duration selection. Explain the recording plan and follow-up so the patient knows how to mark symptoms and how significant findings will be reviewed, rather than treating monitor placement as a completed diagnostic evaluation.')],['AECG'])

add('Biomarkers, monitoring and integrated investigation strategy','Exercise Hemodynamics for Unexplained Exertional Dyspnea',
 'A patient has persistent exertional dyspnea, preserved EF and nondiagnostic resting evaluation. At specialist RHC, resting PAWP is 11 mmHg. During technically valid supine exercise, PAWP reaches 31 mmHg with an abnormally steep PAWP/output relationship. Which interpretation is most appropriate?',
 'An abnormal exercise rise in left-sided filling pressure can explain symptoms despite normal resting pressure',[
 ('The normal resting wedge excludes a cardiac filling-pressure limitation','Resting pressure may be normal in exertional disease; a valid abnormal exercise response provides information unavailable from the resting measurement.'),
 ('The exercise wedge establishes isolated precapillary pulmonary vascular disease','An elevated exercise wedge points to a downstream filling-pressure contribution rather than establishing an isolated low-wedge pulmonary vascular mechanism.'),
 ('Any rise in wedge with exercise is physiologic, so the result is nondiagnostic','Some pressure rise is physiologic, but its magnitude, workload and relationship to output matter; the stated marked response is not dismissed merely because it occurred during exercise.')],
 [S('Test the Physiology During the Symptom State','**Exercise hemodynamics can reveal a filling-pressure abnormality absent at rest.** A normal resting wedge is not proof of normal exercise reserve.',
    'A supine exercise PAWP above 25 mmHg is a commonly used abnormal threshold in the cited framework; a PAWP/CO slope above 2 mmHg/L/min also supports an abnormal response.',
    'Position, workload and acquisition protocol matter. Do not apply a supine threshold uncritically to an upright study.'),
  S('Verify the Dynamic Measurements','**Obtain matched pressure and flow measurements across exercise stages**, with attention to respiratory effects, level and signal quality.',
    'Integrate the response with symptoms, cardiac structure and competing pulmonary or systemic causes. A pressure abnormality does not automatically identify every contributor to dyspnea.',
    'Exercise RHC is most useful when a specific unresolved question will change diagnosis or management after an appropriate noninvasive evaluation. It is not needed for every patient with breathlessness. Report the protocol and the pressure–flow relationship rather than a solitary peak number without context. Review whether the observed exercise reproduced the usual symptoms and whether technical limitations could have distorted the measurement before making a definitive clinical classification.')],['RHCAHA','PH','DIA2025'])

add('Biomarkers, monitoring and integrated investigation strategy','Invasive Coronary Assessment When It Can Change Management',
 'A patient has disabling low-workload angina despite appropriate antianginal therapy and high-risk noninvasive findings. The patient is a potential revascularization candidate. Which next approach is most appropriate?',
 'Invasive coronary angiography with physiologic assessment of relevant intermediate lesions when needed',[
 ('Repeat the same adequate noninvasive study before discussing angiography','Repetition may help a technically inadequate or changed clinical situation, but the stated high-risk evidence and refractory symptoms already justify assessment that can guide treatment.'),
 ('Use coronary calcium scoring to decide whether symptoms warrant further evaluation','Calcium scoring cannot resolve the already established high-risk symptomatic question or define a revascularization strategy.'),
 ('Continue serial resting troponin testing as the principal investigation of stable symptoms','Troponin is central to suspected acute injury, but repeated resting values do not define coronary anatomy or address this refractory stable-angina decision.')],
 [S('Connect the Investigation to a Potential Action','**The 2024 ESC guideline supports invasive angiography for severe refractory symptoms or high-risk disease assessment.** This patient also has a plausible treatment decision that the anatomy can inform.',
    'Intermediate lesions may require FFR or iFR rather than visual grading alone. Complex anatomy may require multidisciplinary planning.',
    'New instability would require an acute assessment pathway instead of treating the situation as routine elective testing.'),
  S('Weigh Benefit Against Procedure Burden','**Review renal function, bleeding risk, vascular access and the patient’s goals.** An invasive result is useful when it can change care in a way that offers meaningful benefit.',
    'Severe frailty, limited life expectancy or inability to pursue a resulting treatment can change the balance; a high-risk test label is not a substitute for individualized assessment.',
    'Explain that angiography does not itself commit the patient to an immediate intervention. Anatomy, physiologic significance, symptom burden and the broader evidence determine the next decision. Avoid duplicate tests that do not resolve a new question, while retaining medical therapy and risk-factor treatment throughout the diagnostic process. Document the intended decision before testing so the result can be interpreted against a clear purpose rather than becoming an isolated procedural finding.')],['CCS'])

add('Biomarkers, monitoring and integrated investigation strategy','Resolving Discordant Anatomy and Physiology',
 'CCTA suggests an intermediate stenosis, while a subsequent technically limited stress study is reported as showing no ischemia. Symptoms remain convincing. Which next approach is most appropriate?',
 'Review both studies’ technical validity and use a targeted additional assessment if the unresolved result will change care',[
 ('Treat the limited stress result as definitive exclusion of coronary disease','An inadequate stress acquisition may not answer the ischemia question, and a negative label should not erase the stated limitation or the anatomic finding.'),
 ('Proceed directly to stenting based on the CCTA percentage estimate','An intermediate anatomic stenosis does not independently prove functional significance; a revascularization decision requires the relevant clinical and physiologic context.'),
 ('Repeat every available cardiac imaging modality to establish agreement','Broad untargeted duplication increases burden without necessarily resolving the actual uncertainty; select the test that addresses the specific remaining question.')],
 [S('Check Whether the Tests Answered the Same Question','**Anatomic narrowing and inducible ischemia are related but nonidentical findings.** Some apparent discordance is expected, especially for intermediate lesions.',
    'Review motion, calcification, stress adequacy, artifact and the actual territory assessed. A limited negative examination is different from an adequate negative one.',
    'Do not select the result that merely matches the initial expectation; establish which information is technically dependable.'),
  S('Choose the Smallest Investigation That Resolves the Clinical Decision','**A complementary functional or invasive physiologic assessment may clarify an important intermediate lesion.** The appropriate choice depends on symptoms, risk and what the result would change.',
    'If obstructive disease does not explain the presentation, consider microvascular or vasomotor disease and noncoronary causes rather than repeatedly chasing the same anatomic target.',
    'Explain residual uncertainty and the plan to the patient. A coherent diagnostic sequence can stop once the relevant decision is adequately supported; agreement among every modality is not a requirement. Conversely, persistent high-risk clinical evidence deserves reassessment when a test was incapable of excluding the proposed mechanism. Preserve the limitations and source measurements in the record so later decisions do not rely on an oversimplified positive or negative summary.')],['CCS','CHEST'])

def revise(number, *, answer=None, others=None):
    r=rows[number-1]
    if answer is not None:r['answer']=answer
    if others is not None:r['others']=others

revise(3,others=[
 ('End-systolic elastance','End-systolic elastance characterizes systolic pressure–volume behavior and contractile state; the stated curve is an end-diastolic filling relationship.'),
 ('Effective arterial elastance','Effective arterial elastance summarizes aspects of arterial load, usually from end-systolic pressure relative to stroke volume, rather than the ventricular diastolic filling curve.'),
 ('End-diastolic chamber stiffness','Stiffness is the reciprocal of compliance; higher pressure for the same volume indicates increased rather than reduced stiffness.')])
revise(16,answer='Review acquisition and, if needed, measure oxygen consumption for direct Fick',others=[
 ('Recalculate indirect Fick with a different estimated-consumption equation','Alternative prediction equations can change the estimate but do not establish the true individual consumption; important discordance may require direct measurement and technical review.'),
 ('Repeat thermodilution until a value matches the indirect Fick result','Repeating valid acquisitions may help, but selecting only a matching value introduces bias; reproducibility and curve quality should guide acceptance rather than agreement with a preferred result.'),
 ('Use the mean of the two reported outputs for derived resistance','Averaging potentially biased methods does not identify a valid flow and can produce an unjustified resistance estimate when the discrepancy affects a major decision.')])
revise(25,others=[
 ('Ultrasound-enhanced transthoracic imaging focused on LV cavity definition','An enhancing agent can improve endocardial border definition and selected Doppler signals, but does not necessarily overcome the inadequate detailed leaflet imaging needed for repair planning.'),
 ('CMR focused on regurgitant volume and ventricular remodeling','CMR can quantify regurgitation and chamber response, but TEE most directly supplies the detailed leaflet mechanism requested for an imminent repair decision.'),
 ('Cardiac CT focused on mitral annular geometry and calcification','CT is useful for annular anatomy and procedural planning, but the immediate question of detailed leaflet pathology after inadequate TTE is most directly addressed by TEE.')])
revise(47,others=[
 ('TEE directed toward the LV apex','TEE is valuable for many embolic-source questions, but its geometry can limit apical assessment; CMR is particularly useful after the stated unresolved enhanced TTE.'),
 ('A repeat ultrasound-enhanced TTE using the same apical acquisition','A targeted repeat can help when technique can improve, but contrast has already failed to resolve this mass; repeating an unchanged inadequate acquisition is less informative than feasible CMR.'),
 ('A coronary-focused CT angiogram without a delayed mass-characterization protocol','CT can assess thrombus with an appropriate protocol when needed, but a coronary-focused acquisition may not resolve the mass and is less directly supported here than CMR.')])
revise(48,answer='Cine CMR volumetry with anatomy-specific phase-contrast flow assessment',others=[
 ('Three-dimensional TTE ventricular volumetry with repeat Doppler flow estimates','Three-dimensional echo can improve RV measurement when image quality is adequate, but the stated difficult transthoracic quantification favors CMR for reproducible volumes and integrated flows.'),
 ('TEE septal imaging with a contrast shunt study','TEE can define the septal defect and contrast passage, but that primarily anatomic assessment does not replace the requested comprehensive RV volumes and quantitative pulmonary/systemic flows.'),
 ('Right-heart catheterization with an oximetry run','Catheterization can quantify shunting and is important for pressure or resistance questions, but does not directly provide the reproducible RV volumetry requested alongside flow assessment.')])
R['SCCT2026']=('SCCT interpretation and reporting of CCTA, 2026 update','https://doi.org/10.1016/j.jcct.2026.08.014')
rows[42]['refs'].append('SCCT2026')
rows[8]['table']=(['Variable','Relationship','Units to preserve'],[
 ['Cardiac output','Oxygen consumption / arteriovenous content difference','mL O2/min divided by mL O2/L gives L/min'],
 ['Cardiac index','CO / body surface area','L/min/m²'],
 ['SVR','80 × (MAP − RAP) / CO','dyn·s·cm⁻⁵'],
 ['PVR','(mean PAP − mean PAWP) / CO','Wood units'],
 ['Oxygen delivery','CO × arterial O2 content × 10','mL O2/min when CO in L/min and content in mL/dL']])
rows[18]['table']=(['Wave or descent','Principal event','Useful distinction'],[
 ['a wave','Atrial contraction','Prominent with resistance to atrial emptying'],
 ['Cannon a wave','Atrial contraction against closed tricuspid valve','Correlate with AV timing'],
 ['v wave','Atrial filling during ventricular systole','Large with TR on right side; left-sided size also depends on compliance'],
 ['x descent','Atrial relaxation and systolic annular displacement','Interpret in rhythm and disease context'],
 ['y descent','Emptying after AV valve opening','Rapid early ventricular filling']])
rows[24]['table']=(['Modality','Particularly useful question','Important limitation'],[
 ['TTE','Initial valve and chamber evaluation','Acoustic windows may be inadequate'],
 ['TEE','Detailed mitral mechanism and procedural anatomy','Esophageal and sedation risks'],
 ['CMR','Regurgitant flow and ventricular volumes','Safety, artifact and acquisition feasibility'],
 ['Cardiac CT','Annular geometry and calcification','Contrast, radiation and motion considerations']])
rows[38]['table']=(['Index','Acquisition framework','2024 ESC significance threshold'],[
 ['FFR','Pressure ratio during maximal hyperemia','≤0.80'],
 ['iFR','Resting wave-free diastolic pressure ratio','≤0.89'],
 ['IMR','Microvascular resistance assessment','≥25 units supports microvascular dysfunction']])
rows[44]['table']=(['LGE distribution','Interpretive direction','Qualification'],[
 ['Territorial subendocardial ± transmural','Ischemic injury pattern','Does not establish ongoing acute occlusion'],
 ['Midwall or subepicardial, nonterritorial','Nonischemic injury pattern','Not a pathogen-specific diagnosis'],
 ['Diffuse/global subendocardial','Consider infiltrative and other noncoronary causes','Do not assume a single coronary infarct'],
 ['No LGE','No detected focal enhancement','Does not exclude every myocardial disease']])

revise(29,answer='Reduced shortening magnitude requiring review of loading and method comparability',others=[
 ('Improved longitudinal shortening with stable global chamber emptying','A change from −20 to −16 is less negative and therefore represents reduced shortening magnitude; the numerical sign should not be mistaken for improvement.'),
 ('New intrinsic systolic dysfunction requiring treatment escalation from this comparison','The change may be important, but hypertension and changed software are material alternative explanations; confirm comparability before attributing it to intrinsic deterioration.'),
 ('Measurement variation that can be set aside because EF is stable','Stable EF does not invalidate a strain change, which can reveal different functional information; review acquisition and context rather than dismissing it.')])
revise(30,answer='Possible pseudonormal inflow requiring integrated pressure assessment',others=[
 ('Normal relaxation with a high-normal filling pressure','Reduced annular relaxation velocities contradict an assumption of normal relaxation; the near-one inflow ratio can be restored by increased atrial pressure.'),
 ('Impaired relaxation with normal filling pressure established by E/A','Impaired relaxation can coexist with normal pressure, but E/A alone cannot establish that pressure is normal when complementary findings raise concern.'),
 ('Restrictive filling established by the near-one E/A ratio','A near-one ratio is not itself the characteristic restrictive inflow pattern; the correct interpretation is integrated assessment for possible pseudonormalization.')])
revise(31,answer='An AF-specific multiparameter assessment using representative cycles',others=[
 ('The sinus-rhythm E/A pathway using the clearest apparent late filling wave','AF lacks organized atrial contraction, so selecting a late deflection does not restore the validity of a sinus-rhythm E/A classification.'),
 ('A single-cycle septal E/e′ classification at the longest RR interval','E/e′ may contribute, but one selected extreme interval can misrepresent the usual state; the guideline uses a multiparameter representative-cycle approach.'),
 ('A chronic-pressure classification based principally on LA volume','Atrial enlargement may reflect AF and remodeling as well as pressure burden, so it cannot independently establish the current filling pressure in this patient.')])
revise(32,answer='Integrated evidence of RV dysfunction despite preserved annular excursion',others=[
 ('Preserved global RV function with isolated regional strain abnormalities','TAPSE samples annular motion rather than global function; abnormal FAC and marked remodeling prevent concluding that global performance is preserved from this value.'),
 ('Technical strain error as the preferred explanation for all discordance','Tracking error should be checked, but independent abnormal FAC and RV remodeling support a real problem; a normal-looking TAPSE does not make strain error the preferred global explanation.'),
 ('Indeterminate RV function until invasive pressures have been measured','Pressures may clarify loading, but echo can identify dysfunction through multiple valid measures; invasive assessment is not required merely to recognize this pattern.')])
revise(34,answer='Reacquire aligned Doppler signals from appropriate acoustic windows',others=[
 ('Repeat the Bernoulli calculation using the existing peak velocity','The calculation cannot correct an oblique velocity input and will preserve its underestimation; fix acquisition before using a derived gradient.'),
 ('Use valve calcification as the principal severity measure on the current study','Morphology is useful, but the stated correctable Doppler limitation should be resolved before replacing hemodynamic assessment with an anatomic impression.'),
 ('Classify a low-flow low-gradient syndrome from the current velocity','Low-flow disease is a real cause of low gradients, but cannot be established from a known misaligned signal without valid flow and severity assessment.')])
revise(36,answer='An appropriate imaging-based test that accounts for the LBBB pattern',others=[
 ('Exercise ECG with ischemia classified from a larger ST-depression threshold','Increasing the cutoff does not validate diagnostic ST interpretation in LBBB; exercise capacity can still be assessed, but ischemia requires a suitable alternative.'),
 ('Exercise ECG interpreted primarily from recovery-phase ST changes','Recovery-phase analysis does not remove the underlying repolarization limitation of LBBB; this approach cannot substitute for appropriate ischemia testing.'),
 ('Invasive angiography as the default replacement for an uninterpretable ECG','Angiography is appropriate with relevant risk or symptoms, but LBBB alone does not eliminate noninvasive imaging choices or mandate an invasive test.')])
revise(38,answer='An attenuation-related apparent defect rather than established inferior scar',others=[
 ('A fixed inferior scar with preserved surrounding wall motion','A small scar can coexist with motion, but disappearance of the defect with position and adequate attenuation correction specifically favors artifact in this region.'),
 ('Inferior inducible ischemia demonstrated by correction of the defect','Inducible ischemia requires the appropriate stress-rest physiologic comparison; a position- or correction-related change addresses attenuation rather than reversibility.'),
 ('Motion-related reconstruction artifact as the established explanation','Motion is a possible perfusion-imaging problem, but the stem describes correction methods and a pattern supporting attenuation; no motion evidence is provided.')])
revise(40,answer='A microvascular abnormality without a significant focal epicardial pressure drop',others=[
 ('A focal epicardial pressure-limiting lesion despite preserved hyperemic FFR','FFR 0.92 is not in the usual significant range; reduced CFR and IMR 32 instead support microvascular involvement without proving a focal target.'),
 ('Elevated resting flow as the sole explanation for reduced flow reserve','High resting flow can reduce CFR, but does not adequately account for the independently elevated IMR, which supports an abnormal microvascular resistance component.'),
 ('Isolated epicardial vasospasm established by the flow-reserve result','Spasm can coexist, but CFR and IMR are not a provocation test; establishing a vasospastic mechanism requires the appropriate separate assessment.')])

revise(43,answer='Report the unresolved lumen and select risk-appropriate further assessment',others=[
 ('Report severe stenosis from the apparent calcium-encroached lumen','When the lumen cannot be graded reliably, blooming may exaggerate narrowing; the stated technical limitation prevents a defensible precise severe classification.'),
 ('Report nonobstructive disease using only the assessable adjacent segments','Adjacent normal segments do not exclude obstruction within the obscured proximal segment; report the limitation rather than generalizing a negative finding.'),
 ('Repeat CCTA with the same acquisition before considering another modality','A repeat should address a correctable factor or a defined reconstruction opportunity; repeating identical conditions is not a reliable solution for the stated calcium limitation.')])
revise(44,answer='No detectable calcified plaque; noncalcified disease remains possible',others=[
 ('Low total plaque burden sufficient to exclude obstructive disease','A zero calcium score is reassuring in suitable contexts, but it does not measure all plaque and cannot independently exclude a noncalcified obstructive lesion in this symptomatic patient.'),
 ('Low coronary risk sufficient to classify the symptoms as nonischemic','Risk assessment is not the same as ischemia diagnosis; the score does not replace evaluation of symptom characteristics and the appropriate clinical pathway.'),
 ('Evidence favoring microvascular angina over noncalcified epicardial disease','A calcium score does not distinguish these mechanisms; neither microvascular angina nor noncalcified plaque is established by a zero result.')])
revise(46,answer='CMR evidence supporting inflammation without an established specific cause',others=[
 ('Viral myocarditis established by combined mapping abnormalities','The combination supports an inflammatory injury pattern, but mapping does not identify a viral organism or exclude other inflammatory causes.'),
 ('Irreversible fibrosis established by the elevated T1-based measure','T1-based abnormalities reflect tissue changes that can include edema and extracellular expansion; the result does not establish that all affected tissue is irreversible fibrosis.'),
 ('An ischemic injury pattern established by elevated T2','T2 supports increased tissue water, not a coronary distribution; the provided nonischemic T1-based pattern requires the stated inflammatory-context interpretation.')])
revise(49,answer='Specialist whole-system assessment for a protocolized CMR examination',others=[
 ('Defer the scan until routine generator replacement establishes conditionality','Replacing a generator does not necessarily make the lead–generator system MR conditional and may not address the current diagnostic need; assess the actual system now.'),
 ('Perform the scan under the generator’s MR-conditional instructions','The stem specifies a nonconditional system, so instructions for a different conditional configuration cannot replace the appropriate specialist protocol.'),
 ('Substitute an anatomic CT examination before assessing CMR feasibility','CT may answer selected questions, but the unresolved issue is tissue characterization; choose an alternative only if it can answer that question rather than bypassing a feasible specialist assessment.')])
revise(50,answer='An appropriate group II agent at the lowest diagnostic dose after review',others=[
 ('A noncontrast CMR examination even though it leaves the clinical question unresolved','Noncontrast imaging is useful when adequate, but the stem establishes that it will not answer the management-relevant question; low eGFR alone does not justify automatic diagnostic compromise.'),
 ('A higher-NSF-risk agent at a fraction of its usual diagnostic dose','Choosing an agent with higher established risk is not preferable to an appropriate group II agent, and an inadequate dose may sacrifice the required diagnostic information.'),
 ('A group II agent after starting temporary dialysis for contrast clearance','Group II use does not justify initiating dialysis solely for that exposure; assess benefit and risk without adding an unnecessary invasive therapy.')])
revise(51,answer='Acute myocardial injury requiring further assessment of cause and ischemic evidence',others=[
 ('Acute myocardial infarction established by the troponin rise and fall','The kinetics establish acute injury, but infarction requires additional evidence; the current presentation has not yet supplied the necessary etiologic support.'),
 ('Chronic myocardial injury with an incidental short-term fluctuation','The stem supplies an acute rise and fall rather than a stable chronic pattern, so chronic injury is not the best supported current classification.'),
 ('An analytical false-positive troponin result as the preferred explanation','Assay interference can be investigated when results are discordant, but there is no specific interference evidence here; systemic illness can cause genuine acute injury.')])
revise(53,answer='Several-week external loop or suitable extended ECG monitoring',others=[
 ('A 24–48-hour Holter as the initial recording strategy','Short monitoring suits daily events, but is less likely to capture symptoms separated by two to three weeks than an appropriate extended external recording.'),
 ('A patient-triggered brief ECG recording arranged only at office visits','Recording during symptoms is valuable, but office timing is unlikely to coincide with these brief infrequent episodes; a wearable extended strategy better covers the expected interval.'),
 ('An implantable loop recorder as the initial monitoring strategy','An implantable recorder may be useful for very infrequent or unresolved events, but is more invasive than a suitable external several-week strategy in this stable low-risk presentation.')])

revise(5,answer='Shorter diastolic perfusion time with increased oxygen demand',others=[
 ('A reduced diastolic driving pressure caused by a rise in aortic pressure','A rise in aortic diastolic pressure would tend to increase the simplified driving gradient if LVEDP were unchanged; no arterial rise is supplied here.'),
 ('Reduced myocardial extraction compensating for increased metabolic demand','Increased demand requires more supply or extraction, not a reduction in extraction as a protective response; the myocardium already extracts a substantial fraction of delivered oxygen.'),
 ('Longer systolic ejection providing additional subendocardial perfusion','LV systolic compression limits subendocardial flow; increased rate does not improve supply by creating a longer favorable systolic perfusion interval.')])
revise(6,answer='LV underfilling from reduced RV delivery and septal/pericardial interaction',others=[
 ('New primary LV contractile failure as the principal cause of low output','Primary LV dysfunction can lower output, but the small preserved-EF chamber with acute RV dilation and septal shift points to reduced filling rather than demonstrating intrinsic LV failure.'),
 ('Predominantly systemic vasodilation with an incidental RV abnormality','Vasodilation can lower systemic pressure, but does not explain the stated RV pressure loading, septal displacement and LV underfilling as directly as ventricular interaction.'),
 ('Isolated reduced venous return without mechanical ventricular interaction','Reduced RV forward delivery is relevant, but leftward septal displacement also provides evidence of mechanical interaction; omitting that component does not fully explain the findings.')])
revise(54,answer='An exertional left-sided filling-pressure abnormality despite normal resting pressure',others=[
 ('Normal exercise adaptation established by a normal resting wedge','A normal resting value cannot establish a normal exercise response; the marked validated pressure rise and abnormal pressure–flow relationship provide contrary evidence.'),
 ('Isolated precapillary exercise PH without a downstream-pressure contribution','The markedly elevated exercise wedge demonstrates a downstream contribution; an isolated precapillary label cannot account for that finding.'),
 ('A primary mechanical ventilatory limit established by the pressure response','Mechanical ventilatory limitation requires relevant respiratory evidence; the recorded abnormal wedge response instead supplies a cardiac filling-pressure mechanism.')])
revise(55,answer='Invasive angiography with selective lesion physiology when needed',others=[
 ('Repeat the same adequate functional study to confirm persistence of ischemia','Repetition can be useful with changed or uncertain findings, but the adequate high-risk study and refractory symptoms already support invasive assessment that can guide treatment.'),
 ('CCTA as a mandatory additional step before considering angiography','CCTA is useful in appropriate anatomic diagnostic pathways, but is not a mandatory extra step when severe refractory symptoms and high-risk evidence justify invasive assessment.'),
 ('Further observation without anatomic assessment while continuing the current regimen','Medical treatment continues, but disabling symptoms despite appropriate therapy and potential revascularization benefit justify defining anatomy rather than indefinitely observing the unchanged regimen.')])
revise(56,answer='Review technical validity and target the unresolved management-relevant question',others=[
 ('Defer further coronary assessment on the basis of the negative stress summary','A high-quality negative study may support deferral in some settings, but this study is explicitly limited and does not reliably resolve convincing persistent symptoms.'),
 ('Refer directly for lesion intervention using the CT percentage alone','An intermediate CT stenosis may need functional clarification; intervention should not follow automatically from visual anatomy without the appropriate clinical and physiologic assessment.'),
 ('Repeat the limited stress protocol unchanged before reviewing the CT images','A repeat may help when a limitation can be corrected, but technical review should first establish the unresolved question and whether a revised or alternative study will answer it.')])

if __name__=='__main__':
    coverage=ROOT/'Cardiology/01. Cardiovascular Physiology, Hemodynamics & Investigations.coverage.json'
    c=json.loads(coverage.read_text(encoding='utf-8'))
    assert len(rows)==c['plannedQuestions']==sum(s['questions'] for s in c['sections']),'Incomplete chapter; do not install'
    index=0
    for section in c['sections']:
        for decision in section['decisions']:
            assert rows[index]['topic']==section['section']
            rows[index]['coverageDecision']=decision
            index+=1
    save('Cardiology',1,c['chapter'],rows,R,'Original educational synthesis; full Harrison subscription text not accessed; independent clinician review not claimed.')
    c.update(status='authored_validated',authoredQuestions=len(rows))
    c['questionDecisions']=[dict(question=i+1,title=r['title'],decision=r['coverageDecision']) for i,r in enumerate(rows)]
    coverage.write_text(json.dumps(c,ensure_ascii=False,indent=2),encoding='utf-8')
