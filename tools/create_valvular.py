"""Original Valvular Heart Disease chapter."""
from qbank_authoring import question, ref, finalize
V=ref('2025 ESC/EACTS Guidelines for Valvular Heart Disease','https://doi.org/10.1093/eurheartj/ehaf194')
A=ref('2020 ACC/AHA Guideline for Valvular Heart Disease','https://doi.org/10.1161/CIR.0000000000000923')
IE=ref('2023 ESC Guidelines for Endocarditis','https://doi.org/10.1093/eurheartj/ehad193')
rows=[]
def q(*args,**kwargs):rows.append(question(*args,**kwargs))

q('Which Doppler combination most clearly supports severe high-gradient aortic stenosis when measurements are technically reliable?',
 'Peak velocity 4.4 m/s and mean gradient 46 mm Hg',[
 ('Peak velocity 2.7 m/s and mean gradient 18 mm Hg','These values do not meet severe high-gradient thresholds.'),
 ('Peak velocity 3.2 m/s and mean gradient 25 mm Hg','This is generally a moderate-gradient range rather than unequivocal severe high-gradient AS.'),
 ('Peak velocity 1.8 m/s and mean gradient 8 mm Hg','This low-gradient combination does not establish severe high-gradient disease.')],
 'Recognizing severe high-gradient AS',
 '**A peak velocity at least 4.0 m/s or mean gradient at least 40 mm Hg supports severe high-gradient AS.**',
 ['A valve area at most 1.0 cm² is another important parameter within an integrated assessment.', 'Doppler alignment, flow state and blood pressure affect measured gradients.'],
 '**Resolve discordant findings rather than averaging unrelated numbers.**',
 ['Low-flow severe disease can have a low gradient and needs a separate diagnostic pathway.', 'High flow or technical error can also create misleading severity estimates.'],
 [['High-gradient severe AS','Vmax at least 4.0 m/s or mean gradient at least 40 mm Hg'],['Discordant low-gradient findings','Assess flow and measurement quality'],['Valve area','Integrate with other parameters']], [V,A])
q('The LV outflow tract diameter is underestimated during aortic valve continuity-equation assessment. What is the expected effect on calculated aortic valve area?',
 'The valve area is underestimated, potentially exaggerating stenosis severity',[
 ('The valve area is overestimated because diameter is ignored','LVOT area depends on the square of the measured diameter.'),
 ('There is no effect because only transvalvular velocity is used','The continuity equation also requires LVOT area and velocity-time integral.'),
 ('The error necessarily proves a high-gradient lesion','A calculation error does not establish the independently measured pressure gradient.')],
 'The continuity equation amplifies diameter error',
 '**LVOT cross-sectional area is proportional to the square of its diameter.**',
 ['Underestimating LVOT diameter reduces calculated stroke volume and aortic valve area.', 'An elliptical LVOT and incorrect sampling can contribute to discordance.'],
 '**Check technical quality before diagnosing low-flow severe AS.**',
 ['Review Doppler windows, sample position, valve morphology and blood pressure.', 'A dimensionless index or additional imaging may help when the LVOT measurement is unreliable.'],
 [['Small LVOT diameter measurement','Smaller calculated LVOT area'],['Reduced calculated forward flow','Smaller continuity-equation valve area'],['Clinical consequence','Possible overclassification of stenosis']], [V])
q('A patient has LVEF 28%, aortic valve area 0.8 cm² and mean gradient 24 mm Hg. During low-dose dobutamine, flow rises and the gradient reaches 43 mm Hg while valve area remains 0.8 cm². What is the interpretation?',
 'True severe low-flow, low-gradient AS with reduced EF',[
 ('Pseudo-severe AS because the gradient increased','A fixed small area with rising flow and a severe gradient supports true severe disease.'),
 ('Mild AS because the resting gradient was below 40 mm Hg','Low flow can mask the gradient of a severe fixed obstruction.'),
 ('Pure dynamic LVOT obstruction established by the valve area alone','The reported valve response supports fixed valvular obstruction, not a proven dynamic mechanism.')],
 'Dobutamine can separate fixed obstruction from low-flow incomplete opening',
 '**True severe AS retains a small valve area when flow improves.**',
 ['A rising mean gradient into the severe range strengthens the interpretation.', 'Pseudo-severe disease generally shows a meaningful increase in valve area as flow rises.'],
 '**Use the full stress study and clinical context.**',
 ['When flow does not increase adequately, projected valve area and CT calcium can help resolve uncertainty.', 'Do not withhold evaluation solely because contractile reserve is absent.'],
 [['Fixed small area plus severe stress gradient','True severe AS'],['Area increases above severe range with flow','Suggests pseudo-severe AS'],['Inconclusive flow response','Use additional assessment']], [V,A], 'clinical_scenario')
q('A patient with LVEF 58% has aortic valve area 0.8 cm², mean gradient 29 mm Hg and stroke volume index 29 mL/m² after measurement error and uncontrolled hypertension are excluded. Which phenotype should be assessed?',
 'Paradoxical low-flow, low-gradient AS with preserved EF',[
 ('Normal-flow high-gradient AS','The measured flow is low and the gradient is below the high-gradient range.'),
 ('Reduced-EF classical low-flow AS','The EF is preserved rather than reduced.'),
 ('Severe AS excluded by preserved EF','A normal EF does not guarantee normal stroke volume or exclude severe obstruction.')],
 'EF and forward stroke volume describe different properties',
 '**A small concentrically remodeled LV can eject a normal fraction of a small end-diastolic volume.**',
 ['Stroke volume index at or below about 35 mL/m² defines the conventional low-flow threshold.', 'The diagnosis requires confirming true stenosis severity and excluding technical and loading confounders.'],
 '**Use integrated imaging to resolve the discordance.**',
 ['CT valve calcium and valve morphology can support severe calcific disease.', 'Symptoms must be attributed carefully because HFpEF, lung disease and other conditions can coexist.'],
 [['Preserved EF with low stroke volume','Possible paradoxical low flow'],['Low EF with low flow','Classical low-flow phenotype'],['Discordant measurements','Need severity confirmation']], [V], 'clinical_scenario')
q('Why are sex-specific CT aortic valve calcium thresholds used when evaluating discordant calcific AS?',
 'Women may have severe stenosis with less valve calcium than men',[
 ('Women require a higher calcium burden than men in every diagnostic framework','The usual diagnostic thresholds are lower in women.'),
 ('CT calcium directly measures regurgitant fraction','It quantifies calcific burden, not backward flow.'),
 ('A calcium score alone replaces every clinical and Doppler assessment','Calcium scoring complements an integrated evaluation, especially when findings are discordant.')],
 'Calcium and fibrosis contribute differently to valve obstruction',
 '**The calcium burden associated with severe AS differs by sex.**',
 ['The 2025 ESC integrated assessment uses supportive thresholds above roughly 2000 Agatston units in men and 1200 in women.', 'These thresholds apply to appropriate calcific disease and should not be treated as universal rules for every valve pathology.'],
 '**Use CT to resolve a specific uncertainty.**',
 ['Review age, valve morphology, flow state and echo quality.', 'A result close to a threshold needs interpretation rather than automatic classification.'],
 [['Men','Higher supportive calcium threshold'],['Women','Lower supportive calcium threshold'],['Clinical role','Adjunct for discordant AS assessment']], [V])
q('A patient has confirmed severe high-gradient AS with exertional syncope and dyspnea attributable to the valve. What is the appropriate management principle?',
 'Evaluate promptly for aortic valve intervention through a Heart Team',[
 ('Use diuretics alone indefinitely because the EF is normal','A preserved EF does not remove the indication created by symptomatic severe AS.'),
 ('Perform routine exercise testing to reproduce syncope before referral','Exercise testing is not required to provoke symptoms in already symptomatic severe AS.'),
 ('Wait until resting EF falls below 30%','Waiting for advanced ventricular failure delays treatment beyond the usual symptomatic indication.')],
 'Symptoms transform severe AS management',
 '**Symptomatic severe AS generally requires valve intervention when meaningful benefit is expected.**',
 ['Medical therapy cannot remove the fixed valvular obstruction.', 'The treatment method depends on anatomy, age, risk, life expectancy and patient preferences.'],
 '**Confirm that the valve explains the symptoms while avoiding unnecessary delay.**',
 ['Assess coronary disease and other comorbidity as part of procedural planning.', 'Discuss futility when severe competing illness makes meaningful survival or functional benefit unlikely.'],
 [['Symptomatic severe AS','Intervention assessment'],['Asymptomatic severe AS','Risk and early-intervention assessment'],['Medical therapy','Supportive rather than corrective']], [V,A], 'clinical_scenario')
q('A patient reports no symptoms despite severe AS, but a supervised exercise test produces typical exertional dyspnea at a low workload. What is the significance?',
 'The test unmasks symptoms relevant to the valve-intervention decision',[
 ('The patient must still be classified as definitely asymptomatic','Objective exercise-related symptoms can reveal limitation not recognized in ordinary activity.'),
 ('The symptoms prove that AS is mild','Exercise symptoms do not downgrade stenosis severity.'),
 ('Exercise testing should be repeated until the result is negative','Repeating a positive study to obtain reassurance does not address the finding.')],
 'Reported absence of symptoms can reflect activity restriction',
 '**Exercise testing can clarify functional status in selected apparently asymptomatic severe AS.**',
 ['Patients may unconsciously reduce exertion and deny symptoms.', 'Testing requires appropriate supervision and is not used to challenge an already clearly symptomatic unstable patient.'],
 '**Integrate the result into an intervention discussion.**',
 ['Current guidance also allows broader early intervention in selected low-risk asymptomatic severe high-gradient disease.', 'Do not apply an outdated rule that every patient must wait for spontaneous collapse or major EF decline.'],
 [['Apparently asymptomatic severe AS','Selected supervised exercise assessment'],['Symptoms on testing','Clinically meaningful unmasked limitation'],['Clearly symptomatic severe AS','Proceed to intervention evaluation']], [V], 'clinical_scenario')
q('Under the 2025 ESC/EACTS guideline, a 78-year-old patient with severe tricuspid aortic stenosis has suitable transfemoral anatomy and no need for another open operation. Which approach is generally favored?',
 'TAVI, after individualized Heart Team assessment',[
 ('SAVR is mandatory solely because surgical risk is not prohibitive','The current ESC age and anatomy framework does not restrict TAVI to prohibitive surgical risk.'),
 ('Balloon valvuloplasty as a durable equivalent to valve replacement','Balloon treatment is usually a bridge or selected temporary strategy, not equivalent durable replacement.'),
 ('No intervention because age above 75 is an absolute contraindication','Age alone is not an absolute prohibition; expected benefit and suitability matter.')],
 'Age, anatomy and lifetime strategy guide TAVI versus surgery',
 '**The 2025 ESC guideline favors TAVI in suitable patients aged at least 70 with tricuspid AS.**',
 ['Access anatomy, coronary access, valve durability and concomitant disease still influence selection.', 'A younger patient, bicuspid anatomy or a need for aortic surgery may favor a different strategy.'],
 '**Use the guideline as a framework rather than a single-variable command.**',
 ['Discuss preferences, expected recovery and long-term procedural options.', 'Assess whether intervention will deliver meaningful functional and survival benefit.'],
 [['Older suitable tricuspid AS','TAVI generally favored in current ESC framework'],['Need for other open cardiac/aortic surgery','May favor SAVR'],['Lifetime planning','Includes durability and future coronary access']], [V], 'clinical_scenario')
q('Why can TAVI cause new high-grade AV block?',
 'The prosthesis can affect the nearby AV conduction system at the aortic annulus and membranous septum',[
 ('The sinus node lies inside the aortic valve leaflet','The sinus node is not located in the aortic valve.'),
 ('TAVI intentionally ablates the AV node as part of the procedure','Conduction injury is a complication, not the intended procedural target.'),
 ('All post-TAVI bradycardia proves acute coronary stent thrombosis','Conduction injury has its own anatomical mechanism and requires specific assessment.')],
 'Aortic valve anatomy is close to the His-Purkinje system',
 '**Mechanical pressure and local injury can disturb conduction after TAVI.**',
 ['Pre-existing conduction disease and procedural factors influence risk.', 'New LBBB or evolving AV block requires appropriate monitoring and pacing assessment.'],
 '**Do not equate every new conduction change with an immediate permanent-device indication.**',
 ['Persistent high-grade block and the broader risk profile guide decisions.', 'The observation period and device strategy depend on the actual rhythm trajectory and local protocol.'],
 [['Anatomical proximity','Annulus/membranous septum near conduction tissue'],['New high-grade block','Requires urgent pacing assessment'],['New conduction change','Monitor evolution and risk']], [V])
q('A patient with acute severe AR from endocarditis has pulmonary edema and a nondilated LV. Why is the ventricle not markedly enlarged?',
 'The acute volume load raises filling pressure before compensatory chamber remodeling can occur',[
 ('A nondilated LV excludes severe AR','Acute severe regurgitation can occur before dilation.'),
 ('The LV must always dilate within minutes of any regurgitation','Structural adaptation takes time.'),
 ('The regurgitant volume enters only the right ventricle','Aortic regurgitation directly loads the LV in diastole.')],
 'Acute and chronic AR have different pressure-volume responses',
 '**A previously normal LV cannot immediately accommodate a large regurgitant volume at low pressure.**',
 ['Rapidly elevated LV diastolic pressure can produce pulmonary edema and impaired forward output.', 'The classic wide pulse pressure of chronic AR may be absent in acute severe disease.'],
 '**Acute severe AR with hemodynamic compromise is an urgent surgical problem.**',
 ['Treat the cause and stabilize while arranging definitive intervention.', 'A relatively normal chamber size should not provide false reassurance.'],
 [['Acute AR','High filling pressure before dilation'],['Chronic AR','Progressive volume remodeling'],['Compromised acute severe AR','Urgent intervention assessment']], [V,IE], 'clinical_scenario')
q('Which echocardiographic feature supports severe chronic AR as part of an integrated assessment?',
 'Holodiastolic flow reversal in the descending aorta',[
 ('A small isolated color jet without other findings','Jet appearance alone can underestimate an eccentric lesion and does not establish severe AR.'),
 ('A normal LV size as a mandatory severity criterion','Chronic severe AR often causes LV remodeling; normal size is not a requirement.'),
 ('A mean systolic aortic gradient above 40 mm Hg as the defining AR measure','That is an AS gradient measure rather than a direct AR severity criterion.')],
 'Backward aortic flow can reveal an important regurgitant burden',
 '**Prominent holodiastolic reversal supports significant AR.**',
 ['Regurgitant volume, fraction, vena contracta and ventricular response also contribute.', 'Pressure half-time is affected by compliance and hemodynamics and should not be used as a single isolated severity rule.'],
 '**Quantify and reconcile before making an intervention decision.**',
 ['CMR can help when echo parameters or ventricular measurements are discordant.', 'Symptoms, LV size and function determine timing alongside lesion severity.'],
 [['Holodiastolic reversal','Supports important AR'],['Pressure half-time','Load and compliance dependent'],['CMR','Useful for selected discordant quantification']], [V])
q('Under the 2020 ACC/AHA framework, an asymptomatic patient with confirmed severe chronic AR has LVEF 52% without another cause of dysfunction. What does this indicate?',
 'LV systolic dysfunction that supports aortic valve surgery rather than waiting for symptoms',[
 ('Normal function for severe AR because EF exceeds 40%','The AR intervention threshold is higher than the HFrEF classification boundary.'),
 ('A reason to defer all treatment until EF is below 30%','That would allow substantial potentially irreversible ventricular deterioration.'),
 ('Proof that AR is mild because the patient denies symptoms','Symptom status does not define regurgitation severity.')],
 'Regurgitant lesions use lesion-specific ventricular thresholds',
 '**The 2020 ACC/AHA AR framework treats EF at or below 55% as abnormal in this setting.**',
 ['A ventricle handling chronic regurgitation can have important dysfunction before reaching generic reduced-EF thresholds.', 'LV dimensions and their progression also inform timing.'],
 '**Specify the guideline rather than mixing thresholds.**',
 ['Current ESC criteria incorporate additional ventricular and indexed measurements.', 'Refer to an experienced valve team for an integrated assessment rather than waiting for overt HF.'],
 [['Severe AR with declining function','Intervention trigger'],['No reported symptoms','Does not guarantee preserved ventricular reserve'],['Serial imaging','Tracks function and chamber remodeling']], [A,V], 'clinical_scenario')
q('A patient has abrupt chest pain, acute severe AR and CT evidence of ascending aortic dissection. What is the definitive priority?',
 'Emergency evaluation for surgical repair of the proximal aorta and associated valve pathology',[
 ('Isolated long-term vasodilator therapy with no surgical evaluation','Medical stabilization does not correct acute type A dissection.'),
 ('Fibrinolysis for any associated ischemic ECG changes','Fibrinolysis can be catastrophic in dissection.'),
 ('Elective surveillance because AR can be chronic','The acute dissection presentation requires an emergency pathway.')],
 'Acute AR can be a manifestation of aortic catastrophe',
 '**Proximal dissection can disrupt aortic root and valve support.**',
 ['Coronary compromise, tamponade and malperfusion can coexist.', 'Management requires an aortic surgical team rather than treating the valve finding in isolation.'],
 '**Stabilization should support, not delay, definitive treatment.**',
 ['Tailor hemodynamic treatment to perfusion and the severe regurgitation physiology.', 'Avoid reflex anticoagulant or thrombolytic ACS treatment without recognizing the aortic diagnosis.'],
 [['Type A dissection with AR','Emergency aortic surgical pathway'],['Chronic isolated AR','Different elective assessment'],['ST changes with dissection','May reflect coronary involvement']], [V], 'clinical_scenario')
q('In severe chronic AR, what is the role of treating coexisting hypertension?',
 'Reduce excessive afterload while continuing lesion-specific surveillance and intervention assessment',[
 ('It reliably eliminates the need for surgery once criteria are met','Blood pressure treatment does not repair a severely regurgitant valve.'),
 ('It is always contraindicated because any pressure reduction is harmful','Appropriate hypertension treatment is important; it must be individualized.'),
 ('It allows ventricular dimensions to be ignored indefinitely','Serial ventricular assessment remains essential.')],
 'Medical treatment does not replace correction of a severe valve lesion',
 '**Hypertension adds to the ventricular load in chronic AR.**',
 ['Appropriate antihypertensive treatment can improve loading conditions.', 'Choice depends on symptoms, ventricular function and other indications.'],
 '**Preserve the distinction between supportive therapy and definitive intervention.**',
 ['Track LV function, dimensions and symptoms even when pressure is controlled.', 'Do not defer surgery when an established intervention indication has emerged.'],
 [['Blood pressure treatment','Reduces a modifiable component of afterload'],['Valve intervention','Corrects the regurgitant lesion'],['Follow-up','Tracks ventricular consequences']], [V,A])
q('A symptomatic patient has rheumatic MS with valve area 1.0 cm², commissural fusion, favorable morphology, no LA thrombus and only mild MR. Which intervention is generally preferred?',
 'Percutaneous mitral commissurotomy',[
 ('Mitral TEER','TEER treats regurgitation and can worsen obstruction; it is not the standard MS treatment.'),
 ('TAVI','TAVI is an aortic intervention, not treatment of rheumatic mitral commissural fusion.'),
 ('Medical treatment alone indefinitely despite suitable symptomatic severe disease','Medical therapy can relieve symptoms but does not open fused commissures.')],
 'Favorable rheumatic morphology supports balloon commissurotomy',
 '**Commissural fusion is the structural substrate that balloon treatment can relieve.**',
 ['Suitability includes leaflet and subvalvular anatomy, calcification, MR severity and absence of LA thrombus.', 'An area at or below 1.5 cm² is clinically significant in this context; symptoms and hemodynamics guide intervention.'],
 '**Use detailed echo assessment before selecting the procedure.**',
 ['TOE evaluates thrombus and anatomy when needed.', 'Unfavorable morphology, significant MR or another surgical indication may favor surgery.'],
 [['Favorable rheumatic fusion','Potential commissurotomy candidate'],['More than mild MR or LA thrombus','Important contraindicating features'],['Degenerative calcific MS','Different anatomy and management']], [V], 'clinical_scenario')
q('Which finding is a major contraindication to routine percutaneous balloon commissurotomy for rheumatic MS?',
 'Left atrial thrombus',[
 ('Commissural fusion with favorable leaflet morphology','That is a favorable substrate rather than a contraindication.'),
 ('Valve area 1.0 cm² in a symptomatic patient','Clinically significant symptomatic stenosis supports considering intervention.'),
 ('Mild MR with otherwise suitable anatomy','Mild MR alone is not the same contraindication as more than mild regurgitation.')],
 'Exclude thrombus before manipulating the stenotic mitral valve',
 '**LA thrombus creates an embolic hazard during commissurotomy.**',
 ['TOE is important when assessing the left atrium and appendage.', 'More than mild MR, absent commissural fusion and unfavorable calcification are other important limitations.'],
 '**Treat the contraindication and reassess the overall strategy.**',
 ['Anticoagulation and repeat imaging may change the thrombus finding.', 'Surgery may be needed when the anatomy or associated disease remains unsuitable.'],
 [['LA thrombus','Do not proceed through a routine balloon pathway'],['Favorable fused commissures','Supports balloon effectiveness'],['Significant MR','Risk of worsening regurgitation']], [V])
q('A patient with rheumatic MS has a mean mitral gradient that rises substantially during tachycardia without a structural change in valve area. Why?',
 'Shorter diastolic filling time and increased flow rate raise the flow-dependent gradient',[
 ('A tachycardia-induced change permanently halves the anatomical orifice every minute','The immediate gradient change need not represent a new anatomical lesion.'),
 ('Mitral gradients are independent of heart rate and flow','They depend importantly on both.'),
 ('Tachycardia abolishes left atrial pressure','Faster rate can worsen left atrial pressure and pulmonary congestion.')],
 'A transvalvular gradient is a flow-dependent measurement',
 '**Tachycardia reduces time available for transmitral filling.**',
 ['A higher diastolic flow rate across the fixed orifice increases the gradient.', 'Anemia, pregnancy and other high-flow states can also alter hemodynamic measurements.'],
 '**Record the heart rate and clinical state when interpreting an echo.**',
 ['Integrate direct valve area, morphology and pressure consequences.', 'Rate control can improve symptoms but does not reverse the fused valve anatomy.'],
 [['Faster rate','Shorter diastole and higher gradient'],['Higher flow','Higher measured gradient'],['Anatomical severity','Requires integrated assessment']], [V])
q('A patient with known MS has exertional dyspnea disproportionate to resting echo findings. Which test can clarify the hemodynamic burden?',
 'Exercise echocardiography assessing mitral gradient and pulmonary pressure response',[
 ('A resting calcium score as a complete substitute for transmitral assessment','Calcium burden does not directly define exercise-related transmitral hemodynamics.'),
 ('A single normal oxygen saturation as definitive exclusion of a cardiac mechanism','Resting saturation does not exclude exertional left atrial hypertension.'),
 ('Repeated resting EF measurements alone','EF can remain preserved despite important MS-related pressure elevation.')],
 'Resting measurements may understate exertional valve physiology',
 '**Exercise can reveal a pathological rise in transmitral gradient and pulmonary pressure.**',
 ['This is useful when symptoms and resting severity appear discordant.', 'Document workload, heart rate and the relevant Doppler measurements.'],
 '**Use the result to reconcile symptoms rather than relying on one resting number.**',
 ['Evaluate lung disease, deconditioning and other competing causes as appropriate.', 'Intervention decisions require the valve anatomy, symptoms and full hemodynamic context.'],
 [['Resting echo','Baseline valve and chamber assessment'],['Exercise echo','Dynamic burden under flow and rate stress'],['Discordant symptoms','Requires integrated interpretation']], [V], 'clinical_scenario')
q('Why can previously tolerated rheumatic MS become symptomatic during pregnancy?',
 'Increased blood volume and cardiac output raise flow across the fixed mitral orifice',[
 ('Pregnancy immediately removes all commissural fusion','Pregnancy does not mechanically open the stenotic valve.'),
 ('Cardiac output normally falls to half of baseline','The usual pregnancy adaptation includes an increase rather than this fall.'),
 ('The mitral valve becomes functionally irrelevant when EF is normal','MS can cause severe pulmonary congestion despite preserved EF.')],
 'Pregnancy stresses a fixed obstruction',
 '**Higher flow and heart rate can increase the mitral gradient and left atrial pressure.**',
 ['A patient with limited reserve may develop pulmonary congestion as pregnancy progresses.', 'Preconception assessment is preferable when significant MS is known.'],
 '**Use a pregnancy Heart Team for significant symptomatic disease.**',
 ['Rate and volume management and anticoagulation require pregnancy-specific choices.', 'Selected severe refractory cases can require intervention with careful maternal and fetal planning.'],
 [['Fixed stenotic orifice','Limited capacity to accommodate increased flow'],['Pregnancy adaptation','Higher volume, output and rate'],['Planning','Preconception and multidisciplinary review']], [V])

# Mitral regurgitation, right-sided disease, prosthetic valves and endocarditis follow.
q('Which lesion is an example of primary rather than secondary MR?',
 'A flail posterior leaflet caused by degenerative chordal rupture',[
 ('Leaflet tethering from ischemic LV remodeling','This is ventricular secondary MR with altered supporting geometry.'),
 ('Annular dilation from longstanding AF with otherwise near-normal leaflets','This is an atrial secondary MR mechanism.'),
 ('Papillary displacement from a dilated LV without intrinsic leaflet disease','This is another ventricular secondary mechanism.')],
 'Primary MR begins in the valve apparatus',
 '**Degenerative leaflet or chordal pathology is a primary valve lesion.**',
 ['Secondary MR results from altered ventricular or atrial geometry with no primary destructive leaflet lesion.', 'Mixed disease can occur, so the classification should reflect the actual imaging mechanism.'],
 '**Mechanism determines the therapeutic pathway.**',
 ['A repairable degenerative lesion differs from MR that may improve after HF or rhythm treatment.', 'Detailed echo, often including 3D TOE, guides repair planning.'],
 [['Primary MR','Intrinsic leaflet or chordal lesion'],['Ventricular secondary MR','Tethering and altered ventricular geometry'],['Atrial secondary MR','Annular and atrial remodeling']], [V])
q('An asymptomatic patient has severe primary MR, LVEF 58% and LV end-systolic diameter 43 mm. What is the most appropriate interpretation?',
 'LV dysfunction and enlargement have reached important intervention triggers despite the absence of symptoms',[
 ('Function is normal because EF exceeds the HFrEF threshold','Severe MR uses a higher EF threshold; an EF below 60% can indicate impaired function.'),
 ('Surgery should wait until EF is below 30%','This risks allowing irreversible dysfunction.'),
 ('LV dimensions are irrelevant because regurgitation unloads the ventricle','Ventricular dimensions are central to timing decisions.')],
 'An apparently normal EF can conceal dysfunction in MR',
 '**The LV ejects into both the aorta and the low-impedance left atrium.**',
 ['Total EF can remain high even while forward function deteriorates.', 'EF at or below 60% or LVESD at least 40 mm are important conventional severe primary-MR intervention triggers, with indexed measures adding information.'],
 '**Refer before advanced symptomatic ventricular failure.**',
 ['Repair feasibility, operative risk and patient preferences inform the strategy.', 'Serial trends, AF, pulmonary pressure and atrial enlargement also contribute to timing.'],
 [['Severe MR with EF 58%','Not reassuringly normal function'],['LVESD 43 mm','Important enlargement trigger'],['No symptoms','Does not negate ventricular criteria']], [V,A], 'clinical_scenario')
q('A color Doppler MR jet is eccentric and hugs the left atrial wall. Why can jet area underestimate severity?',
 'Wall interaction alters jet appearance, so an integrated quantitative assessment is needed',[
 ('Every eccentric jet is necessarily mild','Eccentric severe regurgitation is common with prolapse or flail lesions.'),
 ('Jet area is always independent of loading and machine settings','Jet appearance depends on hemodynamics and acquisition.'),
 ('A wall-hugging jet excludes a flail leaflet','A flail leaflet can produce a markedly eccentric jet.')],
 'Color jet area is not a stand-alone MR severity measure',
 '**Eccentric wall-adherent jets can appear deceptively small.**',
 ['Assess vena contracta, flow convergence where valid, regurgitant volume and pulmonary venous flow.', 'Geometry and multiple jets can limit a single quantitative method as well.'],
 '**Reconcile valve anatomy with chamber response and flow evidence.**',
 ['Use TOE or CMR when echo assessment remains discordant.', 'Do not make a surgery decision from one color image without an integrated review.'],
 [['Central jet area','Still affected by settings and load'],['Eccentric wall jet','Can underestimate important MR'],['Discordant findings','Use multimodal quantification']], [V])
q('A symptomatic patient has severe degenerative MR with a highly repairable posterior leaflet prolapse and acceptable surgical risk. Which approach is generally preferred at an experienced center?',
 'Durable surgical mitral valve repair rather than routine replacement',[
 ('Replacement in every patient regardless of repair feasibility','A durable repair is generally preferred when feasible for degenerative MR.'),
 ('TEER in every low-risk patient solely because it is less invasive','TEER has an important role in selected patients but does not universally replace durable surgical repair.'),
 ('No intervention because a prolapse lesion is always benign','Severe symptomatic MR is not benign simply because the cause is degenerative.')],
 'Durability and repair expertise matter',
 '**Repair preserves native tissue and avoids some prosthesis-related burdens.**',
 ['The expected durability must be high; a technically possible but poor repair is not the goal.', 'Valve-center expertise influences the probability of a successful lasting result.'],
 '**Select the intervention around risk and anatomy.**',
 ['TEER may be appropriate when surgery is high risk and anatomy is suitable.', 'Discuss recurrence, residual gradient and the future treatment pathway.'],
 [['Repairable degenerative MR with acceptable risk','Surgical repair generally preferred'],['High surgical risk with suitable anatomy','Consider transcatheter repair'],['Nonrepairable valve','Assess replacement strategy']], [V,A], 'clinical_scenario')
q('A patient has severe ventricular secondary MR during decompensated HFrEF and has not yet received optimized HF therapy. What should generally come first before deciding on a chronic mitral intervention?',
 'Optimize HF treatment and assess CRT when indicated, then reassess residual MR',[
 ('Immediate TEER solely from the initial MR grade in every patient','Secondary MR is load and geometry dependent and may improve with appropriate HF treatment.'),
 ('Assume that the MR can never improve','Reverse remodeling and resynchronization can reduce regurgitation in selected patients.'),
 ('Treat only the valve and discontinue HF medication','The ventricular disease remains central and requires ongoing treatment.')],
 'Treat the ventricular substrate before judging residual secondary MR',
 '**Secondary MR can improve when loading and ventricular geometry improve.**',
 ['Foundational HFrEF treatment and indicated CRT are central.', 'Reassess severity after stabilization rather than using a congestion-amplified grade as the only basis for a permanent decision.'],
 '**Persistent severe MR can still require intervention.**',
 ['Do not use optimization as an excuse for indefinite delay when symptoms and severe regurgitation persist.', 'A Heart Team evaluates anatomy, ventricular size, RV function and advanced-HF alternatives.'],
 [['Before optimization','Treat HF and assess CRT'],['After optimization with severe residual MR','Evaluate selected valve intervention'],['Advanced disease','Consider the complete advanced-HF strategy']], [V], 'clinical_scenario')
q('Which patient profile most closely resembles the conventional COAPT-like population considered for TEER in severe secondary MR after optimized therapy?',
 'Persistent symptoms, LVEF 35%, LVESD 62 mm and pulmonary systolic pressure 55 mm Hg with suitable anatomy',[
 ('LVEF 10%, extreme LV dilation and irreversible severe RV failure','These findings raise major concern about benefit and are outside conventional COAPT-like selection.'),
 ('Mild MR without symptoms or chamber consequences','The trial-based indication concerns important persistent MR in a symptomatic eligible population.'),
 ('Active destructive endocarditis of the mitral valve','This is not the chronic secondary-MR TEER pathway.')],
 'Selection determines the value of a secondary-MR intervention',
 '**Severe MR alone does not establish that every failing ventricle will benefit from TEER.**',
 ['Conventional criteria include EF 20-50%, LVESD at most 70 mm and pulmonary systolic pressure at most 70 mm Hg in an appropriate symptomatic patient.', 'Anatomical feasibility and optimized treatment are essential additional requirements.'],
 '**Interpret thresholds within a modern Heart Team assessment.**',
 ['Contemporary evidence and guidance refine selection beyond a simple checklist.', 'Assess competing disease and goals rather than extrapolating benefit to an irreversibly damaged ventricle.'],
 [['COAPT-like profile','Residual severe symptomatic MR with suitable ventricular and valve features'],['Extreme ventricular/RV disease','Potential futility concern'],['Mild MR','No severe-MR intervention indication']], [A,V])
q('Which Carpentier mechanism best describes ischemic MR caused by systolic leaflet tethering after ventricular remodeling?',
 'Type IIIb restricted systolic leaflet motion',[
 ('Type I normal leaflet motion with isolated annular dilation','Annular dilation can coexist, but the specified tethering mechanism is IIIb.'),
 ('Type II excessive motion from leaflet prolapse','Prolapse is excessive rather than restricted motion.'),
 ('Type IIIa restriction in systole and diastole, classically rheumatic','That differs from predominantly systolic tethering.')],
 'Motion classification helps describe the repair problem',
 '**Type IIIb indicates restricted systolic motion associated with ventricular tethering.**',
 ['Papillary muscle displacement and altered LV geometry pull the leaflets away from effective coaptation.', 'This differs from primary excess leaflet motion or rheumatic restriction throughout the cardiac cycle.'],
 '**A descriptive classification does not replace severity assessment.**',
 ['Quantify MR and evaluate ventricular disease, annulus and subvalvular apparatus.', 'Mechanism helps select medical, surgical or transcatheter strategies.'],
 [['Type I','Normal motion; annular dilation or perforation'],['Type II','Excessive motion'],['Type IIIa/IIIb','Restriction in both phases / systolic restriction']], [V])
q('Why can acute severe MR produce pulmonary edema and shock despite a surprisingly soft systolic murmur?',
 'Rapid LV-LA pressure equalization can reduce the audible gradient while the acute LA pressure rise is severe',[
 ('A soft murmur always excludes severe valve disease','Murmur intensity is not a reliable severity rule in acute hemodynamic collapse.'),
 ('The regurgitant blood never reaches the left atrium','MR directly loads the left atrium.'),
 ('Acute MR immediately creates a large compliant left atrium','A previously normal atrium has not had time for chronic adaptation.')],
 'Acute MR is a pressure emergency',
 '**A noncompliant left atrium cannot accommodate the sudden regurgitant load.**',
 ['Pulmonary venous pressure rises rapidly.', 'Low forward output and pressure equalization can make auscultation less dramatic than the clinical severity.'],
 '**Urgent echocardiography is more important than waiting for a classic loud murmur.**',
 ['Consider chordal or papillary rupture and endocarditis.', 'Stabilization and definitive intervention depend on the cause and hemodynamic compromise.'],
 [['Acute MR','Abrupt LA pressure rise, pulmonary edema'],['Chronic MR','Atrial adaptation may initially buffer pressure'],['Soft murmur with shock','Does not exclude severe MR']], [V], 'clinical_scenario')
q('In mitral valve prolapse, what usually happens to the midsystolic click when a patient stands from a squatting position?',
 'It occurs earlier as LV volume decreases',[
 ('It invariably disappears because the valve becomes anatomically normal','A loading change does not reverse the structural lesion.'),
 ('It occurs later because standing increases LV volume','Standing generally reduces venous return and LV volume compared with squatting.'),
 ('It becomes an opening snap diagnostic of MS','A prolapse click and stenotic opening snap are distinct phenomena.')],
 'Prolapse timing depends on ventricular loading',
 '**A smaller LV volume allows prolapse to occur earlier in systole.**',
 ['Standing or the strain phase of Valsalva can move the click earlier.', 'Squatting increases filling and afterload, typically delaying the click.'],
 '**Use dynamic auscultation as a clue, not as definitive imaging.**',
 ['Echo establishes leaflet anatomy and associated MR.', 'The degree of click movement does not quantify regurgitant burden.'],
 [['Standing or Valsalva strain','Earlier click'],['Squatting','Later click'],['Severity assessment','Requires echocardiography']], [V])
q('A patient with severe TR has a pulsatile liver and hepatic venous systolic flow reversal. Which mechanism explains these findings?',
 'Regurgitant systolic pressure and flow are transmitted into the right atrium and systemic veins',[
 ('A left-to-right shunt through a ventricular septal defect as the obligatory cause','TR can produce these venous findings without a septal defect.'),
 ('Isolated pulmonary venous hypertension from MS','That is a left atrial-pulmonary venous mechanism, not the direct systemic venous systolic signal.'),
 ('Complete absence of right atrial pressure transmission','The findings arise because transmission is prominent.')],
 'Severe TR creates systemic venous congestion',
 '**Systolic backward flow into the RA can propagate to the hepatic veins.**',
 ['Large venous systolic waves and a pulsatile liver support significant TR.', 'Hepatic flow interpretation also depends on rhythm, compliance and acquisition.'],
 '**Assess the consequences as well as the valve.**',
 ['RV function, hepatic and renal impairment and the underlying pulmonary or left-sided disease influence treatment.', 'A normal pulmonary examination does not exclude major right-sided congestion.'],
 [['TR','Systolic RA and systemic venous loading'],['Hepatic systolic reversal','Supports severe regurgitant physiology'],['Clinical impact','Congestion and end-organ dysfunction']], [V], 'clinical_scenario')
q('Severe TR develops after transvenous pacemaker implantation. Imaging shows the ventricular lead restricting a tricuspid leaflet. Which statement is most accurate?',
 'The lead may be directly contributing to the regurgitation and requires multidisciplinary assessment',[
 ('Every postimplant TR is unrelated to the lead','Lead impingement, adhesion or other interaction can be causal.'),
 ('A larger loop diuretic dose mechanically frees the leaflet','Diuresis may relieve congestion but does not necessarily correct lead impingement.'),
 ('Lead extraction is automatically harmless and mandatory in every patient','Extraction can carry substantial risk and may not resolve chronic valve damage.')],
 'Device-associated TR can have a mechanical component',
 '**Direct lead-leaflet interference differs from purely functional annular dilation.**',
 ['3D echo can clarify the interaction.', 'Both mechanisms may coexist with RV or atrial remodeling.'],
 '**Plan the valve and device strategy together.**',
 ['Consider pacing dependence, lead age, extraction risk and surgical or transcatheter options.', 'Do not assume symptomatic improvement with diuresis eliminates the structural problem.'],
 [['Lead impingement','Direct mechanical cause'],['Functional TR','Annular and chamber remodeling'],['Management','Joint valve and device assessment']], [V], 'clinical_scenario')
q('Why should severe symptomatic TR be assessed before advanced RV failure and irreversible hepatic or renal injury develop?',
 'Late end-organ and RV deterioration can increase procedural risk and reduce the likelihood of recovery',[
 ('TR has no clinical importance until cirrhosis is established','Waiting for irreversible damage can miss the beneficial intervention window.'),
 ('A preserved LV EF guarantees a healthy right ventricle','LV EF does not define RV function or systemic venous burden.'),
 ('Diuretics always permanently correct the valve lesion','They treat congestion but do not reliably reverse the structural cause.')],
 'Timing matters in right-sided valve disease',
 '**Assess RV reserve and organ consequences early rather than treating edema alone indefinitely.**',
 ['Current guidance emphasizes disease staging and structured Heart Team evaluation.', 'Surgery or transcatheter treatment may be appropriate in selected patients before severe irreversible dysfunction.'],
 '**An intervention should have a realistic prospect of benefit.**',
 ['Severe pre-capillary pulmonary hypertension or advanced RV failure can change suitability.', 'Risk scores and comprehensive imaging support the decision rather than substituting for clinical judgment.'],
 [['Earlier eligible severe TR','Potential for better recovery'],['Advanced RV/end-organ injury','Higher risk and possible futility'],['Diuretic response','Symptom control, not proof of lesion correction']], [V])
q('A patient with a serotonin-secreting neuroendocrine tumor develops thickened retracted tricuspid leaflets, severe TR and pulmonary valve disease. What is the most likely process?',
 'Carcinoid heart disease',[
 ('Typical degenerative mitral prolapse','The right-sided fibrotic valve pattern with a neuroendocrine syndrome points to a different process.'),
 ('Rheumatic commissural fusion as the only explanation','Rheumatic disease can affect valves but is not the characteristic serotonin-related right-sided plaque process.'),
 ('A mechanical prosthetic thrombosis','No mechanical valve is described.')],
 'Carcinoid mediators can produce right-sided fibrotic valve disease',
 '**Endocardial fibrous plaques restrict leaflet motion, particularly on the right side.**',
 ['TR and pulmonary stenosis or regurgitation can coexist.', 'Left-sided involvement can occur in selected circumstances, so right-sided predominance is not an absolute rule.'],
 '**Coordinate cardiac and tumor-directed treatment.**',
 ['Assess RV function and the severity of hormone exposure.', 'Intervention requires planning for perioperative hemodynamic and carcinoid-related risks.'],
 [['Carcinoid valve pattern','Thickened retracted right-sided leaflets'],['Tricuspid effect','Commonly regurgitation'],['Pulmonary effect','Stenosis and/or regurgitation']], [V], 'clinical_scenario')
q('Which trade-off is central when choosing a mechanical versus bioprosthetic valve?',
 'Mechanical durability is balanced against lifelong VKA anticoagulation, while tissue valves have a structural deterioration risk',[
 ('Mechanical valves never require anticoagulation','Mechanical valves generally require lifelong VKA treatment.'),
 ('Bioprostheses cannot deteriorate','Structural deterioration is an important lifetime consideration.'),
 ('Valve choice depends only on the current hospital stay','Life expectancy, preferences, pregnancy plans and future procedures matter.')],
 'Valve replacement is a lifetime decision',
 '**Durability and anticoagulation burden are competing considerations.**',
 ['Age alone does not capture adherence, bleeding risk, pregnancy plans or patient priorities.', 'A tissue prosthesis can still require anticoagulation for another indication such as AF.'],
 '**Discuss future treatment pathways before the first intervention.**',
 ['Valve-in-valve feasibility, coronary access and prosthesis size may affect later options.', 'Avoid describing a bioprosthesis as a guarantee of no future anticoagulation or repeat procedure.'],
 [['Mechanical valve','Durable, lifelong VKA burden'],['Bioprosthesis','Less valve-specific long-term anticoagulation, deterioration risk'],['Selection','Shared lifetime planning']], [V,A])
q('A patient with a mechanical mitral valve develops dyspnea, a new high transprosthetic gradient and a subtherapeutic INR. Which evaluation is appropriate?',
 'Urgent multimodality assessment for prosthetic obstruction, including TOE and leaflet-motion imaging as appropriate',[
 ('Assume that every high gradient is normal for a mechanical valve','A new gradient and symptoms require investigation.'),
 ('Use a normal resting ECG to exclude valve thrombosis','An ECG cannot establish leaflet mobility or exclude thrombus.'),
 ('Start a DOAC as a universal treatment without imaging','DOACs are not the standard mechanical-valve anticoagulant, and the obstructive mechanism must be assessed.')],
 'Mechanical prosthetic dysfunction can be urgent',
 '**Thrombosis is important when symptoms, a rising gradient and inadequate anticoagulation coexist.**',
 ['TOE, fluoroscopy and CT can provide complementary information about thrombus and leaflet motion.', 'Compare with baseline prosthetic hemodynamics and consider flow state.'],
 '**Treatment depends on the mechanism and severity.**',
 ['Obstructive thrombosis may require urgent surgery or carefully selected fibrinolysis according to context and expertise.', 'Do not assume that pannus, thrombosis and patient-prosthesis mismatch require identical treatment.'],
 [['New gradient with low INR','Raises thrombosis concern'],['Leaflet-motion imaging','Assesses mechanical restriction'],['Definitive treatment','Mechanism and stability dependent']], [V,A], 'clinical_scenario')
q('Which pattern favors pannus over fresh thrombus as the cause of mechanical prosthetic obstruction?',
 'Slowly progressive obstruction with dense tissue ingrowth despite generally adequate anticoagulation',[
 ('Abrupt symptoms after several weeks of markedly low INR','This pattern more strongly raises concern for thrombus.'),
 ('A mobile low-density mass with recent anticoagulation interruption','This also favors thrombus rather than mature fibrous ingrowth.'),
 ('Immediate normalization after a change in heart rate as proof of pannus','Rate-related gradient change does not establish fixed tissue ingrowth.')],
 'Pannus and thrombus have different biology',
 '**Pannus is fibrous tissue ingrowth that can progressively restrict a prosthesis.**',
 ['Thrombus is more closely associated with inadequate anticoagulation and can develop rapidly.', 'The two can coexist; time course alone is not definitive.'],
 '**Use imaging to guide treatment rather than testing empiric assumptions.**',
 ['CT tissue characterization, TOE and leaflet motion may help.', 'Fibrinolysis does not dissolve mature fibrous pannus as it can thrombus.'],
 [['Pannus','Fibrous tissue, often gradual'],['Thrombus','Clot, often linked to inadequate anticoagulation'],['Mixed obstruction','Possible; requires integrated imaging']], [V])
q('Soon after valve replacement, a patient has a stable higher-than-expected gradient, normal leaflet motion and a prosthetic effective orifice area small relative to body size. What is the likely explanation?',
 'Patient-prosthesis mismatch',[
 ('Acute thrombus proven solely by any elevated gradient','A high gradient with normal motion and a small indexed orifice may reflect mismatch rather than acquired obstruction.'),
 ('Valve endocarditis established without infectious findings','Infection requires its own clinical and imaging evidence.'),
 ('A normal low-flow state as the necessary cause','The stated small indexed effective area is the key mismatch clue.')],
 'A normally functioning prosthesis can be too small for the patient',
 '**Mismatch concerns the effective orifice area relative to body size.**',
 ['The gradient may be high from the initial postoperative baseline.', 'This differs from a new acquired rise caused by thrombosis or structural deterioration.'],
 '**Interpret gradients with flow, valve model and baseline data.**',
 ['Anemia and other high-flow states can also elevate gradients.', 'Planning an appropriate prosthesis and future lifetime options helps reduce severe mismatch risk.'],
 [['Mismatch','Small indexed area with otherwise normal valve function'],['Acquired obstruction','New dysfunction or gradient increase'],['High flow','Can raise gradient without structural obstruction']], [V], 'clinical_scenario')
q('A patient with a prosthetic valve develops anemia, elevated LDH, low haptoglobin and schistocytes. Imaging shows a significant paravalvular leak. What is the likely anemia mechanism?',
 'Mechanical hemolysis caused by high-shear flow through the leak',[
 ('Vitamin B12 deficiency as the obligatory result of a valve leak','A valve leak does not directly establish B12 deficiency.'),
 ('Aplastic marrow failure caused by the prosthesis in every patient','The biochemical and smear pattern supports destruction rather than marrow failure.'),
 ('Iron excess as the cause of schistocyte formation','That is not the principal mechanism here.')],
 'A small high-velocity leak can cause substantial hemolysis',
 '**Turbulent high-shear flow can fragment red blood cells.**',
 ['LDH elevation, low haptoglobin and schistocytes support intravascular hemolysis.', 'Assess bleeding and other anemia causes as well, especially during anticoagulation.'],
 '**Evaluate the cause and clinical impact of the leak.**',
 ['Infection, dehiscence and procedural factors can contribute.', 'Symptomatic HF or clinically significant hemolysis may justify surgical or transcatheter closure in an appropriate patient.'],
 [['Paravalvular high-shear flow','Mechanical RBC fragmentation'],['Hemolysis markers','LDH high, haptoglobin low, schistocytes'],['Intervention assessment','Severity, symptoms, anatomy and infection status']], [V], 'clinical_scenario')
q('A bioprosthetic valve develops new elevated gradients. CT shows hypoattenuated leaflet thickening and reduced leaflet motion without clear calcific destruction. Which mechanism should be considered?',
 'Bioprosthetic leaflet thrombosis',[
 ('Inevitable irreversible calcific degeneration as the only possibility','Thrombotic dysfunction can mimic degeneration and may respond to appropriate treatment.'),
 ('Normal valve motion established despite the CT finding','Reduced motion is specifically described.'),
 ('Patient-prosthesis mismatch proven by a newly acquired leaflet abnormality','Mismatch is generally a size relationship evident from baseline, not a new thrombotic leaflet finding.')],
 'Tissue valves can thrombose as well as degenerate',
 '**Hypoattenuated leaflet thickening with reduced motion raises concern for thrombotic dysfunction.**',
 ['Assess symptoms, gradient change and the clinical context.', 'Subclinical imaging findings and clinically obstructive thrombosis are not identical management problems.'],
 '**Identify the mechanism before planning reintervention.**',
 ['Appropriate anticoagulation can be considered according to severity and the full evaluation.', 'Exclude infection and structural degeneration, which require different treatment pathways.'],
 [['Thrombosis','Leaflet thickening and reduced motion, potentially reversible'],['Structural degeneration','Intrinsic tissue deterioration'],['Mismatch','Small baseline indexed orifice']], [V], 'clinical_scenario')
q('A stable patient has suspected infective endocarditis and has not yet received antibiotics. Which microbiological step is appropriate before treatment?',
 'Obtain multiple properly collected blood-culture sets from separate peripheral samples before starting antibiotics',[
 ('Give antibiotics first and collect one culture after fever resolves','Prior antibiotics can reduce culture yield, and one later sample is inadequate.'),
 ('Wait for a fever spike before collecting any blood','Continuous bacteremia means cultures should not be delayed solely to match a fever peak.'),
 ('Use only a culture from a pre-existing catheter as definitive routine sampling','Separate peripheral sampling helps assess persistent bacteremia and contamination.')],
 'Preserve microbiological yield in suspected endocarditis',
 '**The ESC guideline recommends three blood-culture sets before antibiotics when feasible.**',
 ['Use proper collection technique and adequate blood volume.', 'In a critically unstable patient, obtain cultures promptly but do not create a dangerous treatment delay.'],
 '**Interpret the organism and pattern together with imaging.**',
 ['Repeated growth of a typical organism is different from a single likely contaminant.', 'Communicate suspected endocarditis to the microbiology and clinical team.'],
 [['Before antibiotics in stable suspected IE','Collect appropriate multiple culture sets'],['Hemodynamic/septic instability','Cultures promptly without unsafe treatment delay'],['Negative cultures after prior antibiotics','Reduced yield does not exclude IE']], [IE], 'clinical_scenario')
q('A patient with a prosthetic valve has persistent bacteremia and clinical suspicion of endocarditis, but transthoracic echo is nondiagnostic. What is the next imaging principle?',
 'Perform TOE and consider complementary CT or metabolic imaging when needed',[
 ('Exclude endocarditis because the initial TTE is negative','Prosthetic shadowing and limited sensitivity can obscure important disease.'),
 ('Repeat only the ECG as a substitute for valve imaging','ECG can reveal complications but does not exclude vegetations or perivalvular infection.'),
 ('Stop assessment because prosthetic valves cannot become infected','Prosthetic valve endocarditis is an important high-risk entity.')],
 'A negative initial echo does not end a high-probability evaluation',
 '**TOE improves assessment of prosthetic and perivalvular structures.**',
 ['Repeat imaging is appropriate when suspicion remains despite a nondiagnostic early study.', 'Cardiac CT and selected FDG-PET/CT or other metabolic imaging add information in prosthetic infection.'],
 '**Use an Endocarditis Team for integrated interpretation.**',
 ['Combine microbiology, clinical signs and multimodality imaging.', 'The timing after implantation and noninfectious inflammatory uptake affect interpretation of metabolic studies.'],
 [['TTE','Initial noninvasive assessment'],['TOE','Detailed valve and perivalvular assessment'],['CT/metabolic imaging','Selected complementary prosthetic-infection evaluation']], [IE], 'clinical_scenario')
q('A patient with aortic valve endocarditis develops new PR prolongation and intermittent AV block. Which complication is especially concerning?',
 'Periannular extension with an aortic root abscess',[
 ('A harmless obligatory antibiotic effect in every case','New conduction disease can signal local infection extension and should not be dismissed.'),
 ('Isolated mitral leaflet prolapse as the explanation','That does not explain the characteristic aortic-annular conduction concern.'),
 ('Resolution of infection proven by slower AV conduction','A conduction change is not evidence of microbiological cure.')],
 'Conduction disease can reveal invasive infection',
 '**The aortic annulus lies close to the AV conduction system.**',
 ['Abscess or periannular extension can disrupt conduction.', 'New AV block is a warning sign requiring urgent reassessment.'],
 '**Escalate imaging and surgical evaluation.**',
 ['TOE and cardiac CT can define local complications.', 'Antibiotics remain essential, but uncontrolled local extension can require urgent surgery.'],
 [['New PR prolongation/AV block in aortic IE','Concern for periannular extension'],['Abscess imaging','Defines invasive local disease'],['Management','Urgent Endocarditis Team and surgical assessment']], [IE], 'clinical_scenario')
q('A patient with active left-sided endocarditis develops acute severe valve regurgitation, refractory pulmonary edema and cardiogenic shock. What is the appropriate surgical timing principle?',
 'Emergency valve-surgical evaluation while antimicrobial and supportive treatment continue',[
 ('Always wait until the full antibiotic course is complete','Severe hemodynamic compromise is an emergency indication and cannot routinely wait weeks.'),
 ('Avoid surgery in every active infection','Active infection is often the reason surgery is required.'),
 ('Use embolic-risk scoring alone and ignore the HF presentation','The immediate indication is severe HF and shock, independent of a vegetation-size-only framework.')],
 'Severe HF is a major endocarditis surgery indication',
 '**Acute valve destruction can make medical stabilization insufficient.**',
 ['Refractory pulmonary edema or shock warrants emergency intervention assessment.', 'Other major surgical indications include uncontrolled infection and prevention of selected embolic events.'],
 '**Coordinate definitive treatment with ongoing infection care.**',
 ['Antibiotic selection and duration remain microbiology guided.', 'Neurological complications and comorbidity can affect operative planning but require an individualized multidisciplinary decision.'],
 [['Refractory edema or shock from valve dysfunction','Emergency surgical pathway'],['Uncontrolled local infection','Urgent surgery assessment'],['Stable uncomplicated infection','Different timing and treatment context']], [IE], 'clinical_scenario')
q('Which patient is in a high-risk group for whom antibiotic prophylaxis is recommended before an invasive dental procedure involving gingival manipulation?',
 'A patient with a prosthetic heart valve',[
 ('A patient with isolated uncomplicated mitral prolapse and no prior IE','This is not the same high-risk prophylaxis category.'),
 ('A patient with essential hypertension alone','Hypertension alone is not an indication for IE prophylaxis.'),
 ('A patient with a normal heart and a remote uncomplicated coronary angiogram','A prior angiogram alone does not create the high-risk valve indication.')],
 'IE prophylaxis is targeted to defined high-risk settings',
 '**A prosthetic valve or previous endocarditis places a patient in a high-risk category.**',
 ['The dental procedure must also be one for which prophylaxis is indicated.', 'Use the appropriate regimen after reviewing allergy and other relevant factors.'],
 '**Daily oral health remains important.**',
 ['Prophylaxis does not replace dental hygiene or treatment of oral infection.', 'Do not broaden the indication to every murmur or cardiovascular diagnosis.'],
 [['Prosthetic valve or previous IE','High-risk cardiac category'],['Appropriate invasive dental procedure','Prophylaxis indicated in high-risk patient'],['Isolated hypertension','No IE prophylaxis indication']], [IE])
q('A patient has strongly suspected culture-negative endocarditis, no prior antibiotics and a history of livestock exposure. Which organism merits targeted serological evaluation?',
 'Coxiella burnetii',[
 ('Typical Staphylococcus aureus as an organism reliably requiring serology instead of cultures','S. aureus usually grows in routine blood cultures; the exposure and culture-negative pattern point elsewhere.'),
 ('A routine skin contaminant as proof that no infection exists','A possible contaminant does not resolve a strong culture-negative IE presentation.'),
 ('Influenza virus as the standard livestock-associated valvular pathogen','That is not the characteristic cause being tested.')],
 'Culture-negative IE requires an exposure-informed work-up',
 '**Coxiella burnetii is an important cause of culture-negative endocarditis.**',
 ['Livestock exposure provides a useful epidemiological clue.', 'Bartonella and other difficult-to-culture organisms are additional considerations depending on exposure and geography.'],
 '**Coordinate targeted serology and molecular testing.**',
 ['Review whether antibiotics preceded sampling and assess noninfectious mimics.', 'A negative routine culture is not a reason to abandon the diagnosis when clinical and imaging evidence remains strong.'],
 [['Coxiella','Livestock-associated culture-negative IE consideration'],['Prior antibiotics','Common reason for reduced culture yield'],['Targeted testing','Serology and selected molecular methods']], [IE], 'clinical_scenario')

if __name__=='__main__':
    finalize('Cardiology',5,'Valvular Heart Disease','cardiology-valvular',rows,44)
