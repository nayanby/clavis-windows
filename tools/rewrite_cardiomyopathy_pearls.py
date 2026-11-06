"""Topic-led Cardiomyopathies Pearls; prose first, tables only for comparisons."""
import json
from lxml import html
from create_qbank_topic_notes import DEST,page

BODY=r'''<nav><strong>Contents</strong><br>
<a href="#assessment">Assessment</a> · <a href="#hcm">Hypertrophic cardiomyopathy</a> · <a href="#dcm">Dilated cardiomyopathy</a> · <a href="#arrhythmogenic">Arrhythmogenic cardiomyopathy</a> · <a href="#restriction">Restrictive disease</a> · <a href="#amyloid">Amyloidosis</a> · <a href="#storage">Storage disorders</a> · <a href="#myocarditis">Myocarditis</a> · <a href="#sarcoid">Cardiac sarcoidosis</a> · <a href="#takotsubo">Takotsubo</a> · <a href="#cmr">Cardiac MRI</a> · <a href="#family">Family screening and exercise</a></nav>

<section id="assessment"><h2>Assessing cardiomyopathy</h2>
<p>Cardiomyopathy is a disorder of heart muscle that is not adequately explained by coronary disease, hypertension, valve disease or congenital heart disease. Assessment has two parts: describe the structural and functional abnormality, then establish its cause.</p>
<ul><li><strong>Hypertrophic cardiomyopathy:</strong> increased ventricular wall thickness without a sufficient loading explanation.</li>
<li><strong>Dilated cardiomyopathy:</strong> left ventricular enlargement with systolic dysfunction.</li>
<li><strong>Non-dilated left ventricular cardiomyopathy:</strong> nonischemic scar or fatty replacement without ventricular enlargement, or otherwise unexplained global systolic dysfunction without scar. Significant myocardial disease can therefore exist in a normal-sized ventricle.</li>
<li><strong>Arrhythmogenic cardiomyopathy:</strong> myocardial disease with a prominent tendency to ventricular arrhythmia; involvement may be right-sided, left-sided or biventricular.</li>
<li><strong>Restrictive cardiomyopathy:</strong> a stiff myocardium limits filling, often with enlarged atria and normal-sized ventricular cavities.</li></ul>
<p>History should cover heart failure, syncope, arrhythmia, alcohol and drug exposure, systemic disease and premature sudden death in the family. ECG, echocardiography and ambulatory rhythm monitoring define the initial abnormalities. Cardiac MRI helps characterize scar, inflammation and infiltration; genetic testing is selected according to the disease and family history.</p></section>

<section id="hcm"><h2>Hypertrophic cardiomyopathy</h2>
<p>Hypertrophic cardiomyopathy causes ventricular thickening, impaired relaxation and a variable tendency to outflow obstruction and arrhythmia. Sarcomeric disease must be distinguished from hypertension, amyloidosis and storage disorders.</p>
<h3>Diagnosis and obstruction</h3>
<p>In adults, unexplained maximal end-diastolic wall thickness of <strong>15 mm or more</strong> usually establishes the morphological diagnosis. Thickness of 13–14 mm can be significant with a convincing family history or pathogenic variant. Children require age- and body-size-adjusted assessment.</p>
<p>Outflow obstruction is dynamic. Systolic anterior motion of the mitral valve narrows the outflow tract and may cause mitral regurgitation. Reduced ventricular filling, reduced afterload and increased contractility can worsen the gradient. Standing and the strain phase of Valsalva usually increase the murmur.</p>
<p>A peak outflow gradient of <strong>30 mmHg or more</strong> defines obstruction. A gradient of <strong>50 mmHg or more</strong>, at rest or with provocation, is important when considering advanced treatment for persistent symptoms. Exercise echocardiography can reveal obstruction that is absent at rest.</p>
<h3>Treating symptoms</h3>
<p>A <strong>nonvasodilating beta blocker</strong> is usually the first treatment for symptomatic obstruction. Verapamil or diltiazem is an alternative when beta blockade is unsuitable or ineffective, but may be unsafe with hypotension, severe resting symptoms or very high gradients. Avoid dehydration and unnecessary drugs that markedly reduce preload or afterload.</p>
<p>Persistent limiting symptoms may require a cardiac myosin inhibitor, disopyramide with appropriate AV nodal blockade, or septal reduction. Myectomy is particularly useful when mitral or papillary muscle abnormalities also require surgical correction. Alcohol septal ablation is an alternative for selected patients with suitable anatomy.</p>
<p>Mavacamten reduces excessive actin–myosin interaction. It requires echocardiographic monitoring and a careful interaction review. Initiation with <strong>EF below 55%</strong> is not recommended; interrupt treatment if <strong>EF falls below 50%</strong> or heart failure develops.</p>
<h3>Preventing sudden death</h3>
<p>Previous cardiac arrest or sustained ventricular arrhythmia generally warrants assessment for a secondary-prevention ICD. Primary prevention considers family history of HCM-related sudden death, suspected arrhythmic syncope, wall thickness of at least 30 mm, an apical aneurysm and EF below 50%. Nonsustained VT and extensive MRI scar provide additional information.</p>
<p><strong>Relieving obstruction does not remove the need to assess arrhythmic risk.</strong> Reassess risk over time. Clinical atrial fibrillation in HCM generally warrants anticoagulation even when an ordinary stroke-risk score is low.</p></section>

<section id="dcm"><h2>Dilated cardiomyopathy</h2>
<p>Dilated cardiomyopathy combines ventricular enlargement with impaired contraction. Genetic susceptibility and acquired injury frequently overlap. Investigate coronary disease, sustained tachyarrhythmia, alcohol, cardiotoxic drugs, inflammation and endocrine or nutritional causes when appropriate.</p>
<p>Treatment includes the foundational drug classes for heart failure with reduced EF: a renin–angiotensin system inhibitor or ARNI, an evidence-based beta blocker, a mineralocorticoid receptor antagonist and an SGLT2 inhibitor, as tolerated. Diuretics relieve congestion. Treat the cause, including alcohol abstinence or control of a persistent tachyarrhythmia. Continue disease-modifying treatment after recovery unless a specialist-directed plan supports withdrawal.</p>
<h3>Inherited disease and arrhythmia</h3>
<p><strong>LMNA-related disease</strong> often produces conduction disease and atrial or ventricular arrhythmias before severe systolic dysfunction. An EF above 35% does not by itself establish low risk. Genotype, nonsustained VT, conduction abnormalities, scar and ventricular function guide ICD assessment.</p>
<p><strong>DSP-related disease</strong> often involves the left ventricle, with subepicardial or ring-like scar and ventricular arrhythmias. Episodes of chest pain and troponin release can resemble myocarditis. Repeated inflammatory episodes, characteristic scar and family history warrant assessment for inherited arrhythmogenic disease.</p>
<h3>Peripartum cardiomyopathy</h3>
<p>Peripartum cardiomyopathy is otherwise unexplained systolic heart failure near the end of pregnancy or postpartum, usually with <strong>EF below 45%</strong>. Ventricular enlargement is not required. Exclude competing causes such as pre-existing cardiomyopathy, ischemia and significant valve disease.</p>
<p>Treatment depends on whether the patient is pregnant or postpartum and whether she is breastfeeding. ACE inhibitors, ARBs and ARNIs are avoided during pregnancy. Severe dysfunction requires assessment for thromboembolism, arrhythmia and advanced heart failure support. Bromocriptine is used in selected protocols, with attention to anticoagulation and its suppression of lactation.</p></section>

<section id="arrhythmogenic"><h2>Arrhythmogenic cardiomyopathy</h2>
<p>Progressive myocardial injury and replacement fibrosis create a substrate for ventricular arrhythmia. Right ventricular disease may produce regional akinesia or dyskinesia, chamber enlargement, reduced function and anterior T-wave inversion. Left-dominant and biventricular forms also occur.</p>
<p>Diagnosis integrates ECG findings, rhythm monitoring, ventricular imaging, family history and genetic results. An isolated ECG change or MRI finding is insufficient. Ventricular ectopy, unexplained syncope or an affected relative should not be dismissed as athletic adaptation.</p>
<p><strong>PKP2</strong> is associated particularly with the right ventricular form; <strong>DSP</strong> commonly causes left ventricular scar disease. High-intensity endurance exercise can accelerate disease expression and increase arrhythmic risk, including in some variant carriers before obvious ventricular dysfunction. Exercise advice and ICD decisions require disease-specific assessment.</p></section>

<section id="restriction"><h2>Restrictive cardiomyopathy and constrictive pericarditis</h2>
<p>Both conditions cause impaired filling, raised venous pressure and congestion. In restrictive cardiomyopathy the limiting tissue is myocardium; in constriction it is the pericardium. Preserved EF can coexist with severe disease in either condition.</p>
<table><thead><tr><th>Finding</th><th>Restrictive cardiomyopathy</th><th>Constrictive pericarditis</th></tr></thead><tbody>
<tr><td>Ventricular interaction during respiration</td><td>LV and RV systolic pressures usually change in the same direction.</td><td>LV and RV systolic pressures change in opposite directions; ventricular interdependence is exaggerated.</td></tr>
<tr><td>Tissue Doppler</td><td>Mitral annular relaxation velocities are usually reduced.</td><td>Medial e′ may be preserved and exceed lateral e′.</td></tr>
<tr><td>Imaging</td><td>May show infiltration, myocardial scar and atrial enlargement.</td><td>Respiratory septal shift; pericardial thickening or calcification may be present.</td></tr>
</tbody></table>
<p>Normal pericardial thickness does not exclude constriction. A dip-and-plateau tracing or similar diastolic pressures alone does not reliably distinguish the two disorders; integrate respiratory hemodynamics with echocardiography and cross-sectional imaging.</p></section>

<section id="amyloid"><h2>Cardiac amyloidosis</h2>
<p>Amyloid deposition thickens and stiffens the ventricular walls. Carpal tunnel syndrome, neuropathy, conduction disease, disproportionate wall thickening and low ECG voltage can support suspicion. Relative apical sparing on strain imaging is helpful but is not diagnostic by itself.</p>
<h3>Establish the amyloid type</h3>
<p>Begin with <strong>serum free light chains, serum immunofixation and urine immunofixation</strong>. Ordinary electrophoresis alone is insufficient to exclude a monoclonal protein.</p>
<p>With an appropriate cardiac phenotype, grade 2–3 myocardial uptake on bone-tracer scintigraphy can establish ATTR without cardiac biopsy only when light-chain disease has been excluded and true myocardial uptake is confirmed, usually with SPECT. A monoclonal abnormality prevents this shortcut: tissue confirmation and reliable amyloid typing may be needed because AL and ATTR require different treatment. Kidney dysfunction also affects free-light-chain interpretation.</p>
<h3>Treatment</h3>
<p><strong>AL amyloidosis</strong> needs urgent hematology-led treatment of the plasma-cell disorder. <strong>ATTR cardiomyopathy</strong> is treated with therapies directed at transthyretin, including stabilizers such as tafamidis or acoramidis, and the silencing therapy vutrisiran where indicated and available. After ATTR is confirmed, genetic testing distinguishes hereditary from wild-type disease.</p></section>

<section id="storage"><h2>Storage disorders and myocardial iron</h2>
<p>Wall thickening accompanied by pre-excitation, conduction disease, skeletal muscle involvement or systemic findings should prompt investigation beyond sarcomeric HCM.</p>
<ul><li><strong>Fabry disease:</strong> GLA-related alpha-galactosidase A deficiency causes substrate accumulation. Neuropathic pain, angiokeratomas, reduced sweating, renal disease and stroke accompany cardiac involvement. Enzyme activity can be normal in affected women, so genetic testing is important. Treatment includes enzyme replacement or a chaperone for an amenable variant.</li>
<li><strong>PRKAG2 syndrome:</strong> abnormal AMP-activated protein kinase signaling causes cardiac glycogen accumulation. Ventricular hypertrophy, pre-excitation and progressive conduction disease are characteristic.</li>
<li><strong>Danon disease:</strong> LAMP2-related lysosomal dysfunction causes an X-linked disorder, often with severe cardiomyopathy, skeletal myopathy, elevated creatine kinase and pre-excitation. Advanced heart failure can develop early.</li></ul>
<p>Iron overload can cause ventricular dysfunction and arrhythmia. Cardiac MRI T2* measures myocardial iron more directly than serum ferritin: at standard 1.5-T imaging, <strong>T2* below 20 ms indicates cardiac iron, and below 10 ms indicates severe overload</strong>. Lower T2* means greater iron deposition. Management requires appropriate iron chelation and cardiac follow-up.</p></section>

<section id="myocarditis"><h2>Myocarditis</h2>
<p>Myocarditis can present with chest pain, heart failure, conduction disease or ventricular arrhythmia. Troponin elevation reflects myocardial injury but does not establish its cause. MRI can demonstrate edema and nonischemic injury; subepicardial inferolateral enhancement is a common pattern.</p>
<p>Stable presentations are assessed with clinical findings, ECG, biomarkers, echocardiography and MRI. Cardiogenic shock, rapidly progressive dysfunction, serious ventricular arrhythmia or advanced AV block requires urgent specialist assessment. Endomyocardial biopsy is important when identifying the inflammatory subtype will change treatment.</p>
<p><strong>Giant-cell myocarditis</strong> is an aggressive disease associated with rapid heart failure, ventricular arrhythmias and conduction abnormalities. Biopsy establishes the diagnosis. Treatment generally requires combined immunosuppression rather than corticosteroids alone, alongside assessment for mechanical circulatory support or transplantation.</p></section>

<section id="sarcoid"><h2>Cardiac sarcoidosis</h2>
<p>Granulomatous inflammation and subsequent fibrosis can affect the conduction system and ventricular myocardium. Unexplained high-grade AV block, ventricular tachycardia or nonischemic ventricular dysfunction may be the first cardiac manifestation, with or without recognized extracardiac sarcoidosis.</p>
<p><strong>MRI and FDG-PET provide complementary information.</strong> Late gadolinium enhancement identifies myocardial injury and scar. Properly prepared FDG-PET helps assess active inflammation. Patchy disease reduces the sensitivity of an unguided myocardial biopsy; a negative result does not exclude cardiac involvement.</p>
<p>Active clinically significant inflammation may require corticosteroids and additional immunosuppression. Arrhythmic risk must be assessed separately: suppression of inflammation does not remove established scar, and an ICD may be preferable to pacing alone when the risk of ventricular arrhythmia is substantial.</p></section>

<section id="takotsubo"><h2>Takotsubo syndrome</h2>
<p>Takotsubo causes transient ventricular dysfunction, often after physical or emotional stress. Apical ballooning is common, but other patterns occur and a stress trigger is not essential. The wall-motion abnormality often extends beyond a single coronary territory.</p>
<p>Initial assessment must address acute coronary syndrome. MRI and subsequent recovery help distinguish Takotsubo from infarction and myocarditis. Despite reversibility, the acute phase can be complicated by arrhythmia, thrombus, pulmonary edema or shock.</p>
<p><strong>Identify the mechanism of shock before choosing treatment.</strong> With dynamic outflow obstruction, positive inotropes can worsen the gradient. Carefully selected fluid may help when filling is inadequate and pulmonary congestion is absent. Shock caused by pump failure, right ventricular involvement or severe mitral regurgitation requires a different approach. Beta blockade is not given indiscriminately during hemodynamic instability.</p></section>

<section id="cmr"><h2>Interpreting cardiac MRI</h2>
<p>Late gadolinium enhancement describes the distribution of myocardial injury. The pattern helps narrow the cause, while scar burden also informs arrhythmic risk.</p>
<table><thead><tr><th>Distribution</th><th>Common association</th></tr></thead><tbody>
<tr><td>Subendocardial or transmural enhancement in a coronary territory</td><td>Ischemic myocardial injury</td></tr>
<tr><td>Midwall septal enhancement</td><td>Nonischemic dilated cardiomyopathy</td></tr>
<tr><td>Subepicardial inferolateral enhancement with edema</td><td>Myocarditis</td></tr>
<tr><td>Patchy basal septal or multifocal nonischemic enhancement</td><td>Cardiac sarcoidosis</td></tr>
<tr><td>Ring-like subepicardial left ventricular scar</td><td>Arrhythmogenic left ventricular disease, including DSP-related disease</td></tr>
<tr><td>Diffuse subendocardial or transmural enhancement with abnormal myocardial nulling</td><td>Amyloidosis</td></tr>
</tbody></table>
<p>These associations are not exclusive. MRI alone cannot reliably type amyloid or replace biopsy when a specific inflammatory diagnosis will alter treatment.</p></section>

<section id="family"><h2>Family screening and exercise</h2>
<p>First-degree relatives need appropriate clinical screening when inherited cardiomyopathy is suspected. A confirmed pathogenic or likely pathogenic familial variant allows targeted cascade testing after genetic counseling. Follow-up depends on age, the disease and whether the relative carries the familial variant.</p>
<p>A <strong>variant of uncertain significance</strong> does not establish a familial diagnosis and should not by itself determine predictive testing or irreversible treatment. Expert family studies may help clarify its significance; clinical surveillance follows the phenotype and family history.</p>
<p>Exercise advice differs by disease. Appropriate activity is encouraged in HCM, with individualized discussion of competitive or high-intensity sport. High-intensity endurance exercise is particularly concerning in arrhythmogenic cardiomyopathy. After myocarditis, persistent ventricular arrhythmia or other evidence of active disease prevents clearance for intensive exercise.</p>
<p>Prominent ventricular trabeculations can occur in healthy athletes. Morphology alone should not establish cardiomyopathy when function, rhythm assessment and family evaluation are reassuring.</p></section>'''


def make():
    doc=html.fragment_fromstring(BODY,create_parent='div')
    ids=doc.xpath('.//section/@id');assert len(ids)==len(set(ids))==12
    assert not doc.xpath('.//h1|.//script|.//iframe')
    assert all(link[1:] in ids for link in doc.xpath('.//nav//a/@href'))
    tables=doc.xpath('.//table');assert len(tables)==2
    for table in tables:
        count=len(table.xpath('./thead/tr/th'))
        assert all(len(row.xpath('./td'))==count for row in table.xpath('./tbody/tr'))
    coverage=['hcm','hcm','hcm','hcm','hcm','hcm','hcm','assessment','dcm','dcm','dcm','arrhythmogenic',
        'arrhythmogenic','restriction','restriction','amyloid','amyloid','amyloid','storage','storage',
        'myocarditis','myocarditis','sarcoid','sarcoid','takotsubo','takotsubo','storage','storage','cmr','family',
        'dcm','arrhythmogenic','family','family','myocarditis','family','assessment']
    assert len(coverage)==37 and all(key in ids for key in coverage)
    target=DEST/'Cardiology/Cardiomyopathies.html';target.parent.mkdir(parents=True,exist_ok=True)
    rendered=page('Cardiomyopathies',BODY).replace('<h1>Cardiomyopathies</h1>','',1)
    rendered=rendered.replace('</style>','table{display:table;width:100%}@media(max-width:650px){table{display:block;overflow-x:auto}}</style>')
    target.write_text(rendered,encoding='utf-8')
    sources=[
      'https://academic.oup.com/eurheartj/article/44/37/3503/7246608',
      'https://www.jacc.org/doi/10.1016/j.jacc.2024.02.014',
      'https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=669c936b-3ee6-4e36-8a22-79dd11b1255b',
      'https://www.jacc.org/doi/10.1016/j.jacc.2022.11.022',
      'https://academic.oup.com/eurheartj/article/46/40/3952/8234483',
      'https://academic.oup.com/eurheartj/article/46/43/4462/8234487',
      'https://www.acc.org/Latest-in-Cardiology/ten-points-to-remember/2024/04/22/13/10/diagnosis-and-management-of-cs',
      'https://www.acc.org/latest-in-cardiology/ten-points-to-remember/2020/03/30/12/17/takotsubo-syndrome',
    ]
    target.with_suffix('.review.json').write_text(json.dumps(dict(module='Cardiomyopathies',status='authored',
      sourceCheckedAt='2026-11-07',independentClinicianReview=False,visibleReferences=False,visibleTitle=False,
      writingStyle='Standalone topic discussion; prose and selective bullets; comparison tables only',
      groups=12,tables=2,questionCoverage={str(i):key for i,key in enumerate(coverage,1)},checkedSources=sources),indent=2),encoding='utf-8')
    manifest=DEST/'authored-notes.json';authored=json.loads(manifest.read_text(encoding='utf-8')) if manifest.exists() else {}
    authored['Cardiology/Cardiomyopathies']=dict(file=str(target),sections=12,tables=2,references=0,
      words=len(doc.text_content().split()),status='authored_source_checked',chapterOrder=6,writingStyle='topic-led')
    manifest.write_text(json.dumps(authored,indent=2),encoding='utf-8')
    print(target);print(f'12 sections; 2 comparison tables; {len(doc.text_content().split())} words; 37 concepts mapped')


if __name__=='__main__':make()
