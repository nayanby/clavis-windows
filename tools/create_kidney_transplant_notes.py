"""Author the Kidney Transplantation Pearls chapter, covering its 40 questions."""
import json
from lxml import html
from create_qbank_topic_notes import DEST, page

BODY=r'''<nav><strong>Contents</strong><br>
<a href="#candidate">Transplant preparation</a> · <a href="#compatibility">Compatibility</a> · <a href="#drugs">Immunosuppression</a> · <a href="#tacrolimus">Tacrolimus toxicity</a> · <a href="#dysfunction">Graft dysfunction</a> · <a href="#surgical">Surgical complications</a> · <a href="#rejection">Rejection</a> · <a href="#cmv">CMV</a> · <a href="#bk">BK virus</a> · <a href="#infection">Other infections</a> · <a href="#recurrence">Recurrent disease</a> · <a href="#followup">Long-term care</a> · <a href="#calculations">Calculations</a> · <a href="#pitfalls">Pitfalls</a></nav>

<section id="candidate"><h2>1 Transplant preparation</h2>
<p><strong>Preemptive transplantation means transplantation before maintenance dialysis begins.</strong> It is preferred when feasible in a suitable patient, particularly when a living donor is available. Refer early enough to complete assessment and donor work-up.</p>
<table><thead><tr><th>Finding</th><th>Approach</th></tr></thead><tbody>
<tr><td>Active disseminated tuberculosis, uncontrolled sepsis or another serious active infection</td><td><strong>Defer transplantation and treat the infection.</strong> Immunosuppression can cause rapid progression.</td></tr>
<tr><td>Latent tuberculosis</td><td>Exclude active disease and plan preventive treatment. This differs from active disseminated TB.</td></tr>
<tr><td>Active malignancy</td><td>Usually defer; suitability and timing depend on the cancer, treatment response and recurrence risk.</td></tr>
<tr><td>Older age, diabetes or obesity</td><td>Assess the combined medical and surgical risk. A single label does not automatically exclude transplantation.</td></tr>
<tr><td>Cardiovascular disease or difficulty taking medicines reliably</td><td>Assess and address the problem before listing. Explain the need for lifelong follow-up and immunosuppression.</td></tr>
</tbody></table>
<p>Document the cause of kidney failure, previous transplants, transfusions, pregnancies, infection serology and vaccination history. These affect recurrence risk, antibody testing and infection prevention.</p></section>

<section id="compatibility"><h2>2 Compatibility and antibody testing</h2>
<p><strong>ABO compatibility and HLA compatibility are separate.</strong> An ABO-compatible recipient can still have donor-specific anti-HLA antibodies and develop antibody-mediated rejection.</p>
<table><thead><tr><th>Test or term</th><th>Meaning</th><th>Interpretation</th></tr></thead><tbody>
<tr><td><strong>Donor-specific antibody (DSA)</strong></td><td>Recipient antibody directed against an antigen present in the donor, often an HLA antigen.</td><td>Class II antibodies, including HLA-DQ, can be clinically important.</td></tr>
<tr><td><strong>Single-antigen bead assay</strong></td><td>Detects individual anti-HLA antibody specificities, including low-level antibodies.</td><td>Sensitive antibody identification; the reported fluorescence is not a universal measure of pathogenicity.</td></tr>
<tr><td><strong>Flow cytometry crossmatch</strong></td><td>Detects recipient antibody binding to donor lymphocytes.</td><td>More sensitive than the conventional complement-dependent cytotoxicity crossmatch; interpret with antibody specificity.</td></tr>
<tr><td><strong>Complement-dependent cytotoxicity crossmatch</strong></td><td>Detects donor-cell injury caused by recipient antibody and complement.</td><td>A positive result with relevant DSA indicates substantial risk of immediate antibody-mediated graft injury.</td></tr>
<tr><td><strong>Virtual crossmatch</strong></td><td>Compares known recipient antibody specificities with donor HLA typing.</td><td>Depends on current, reliable antibody results and adequate donor typing.</td></tr>
</tbody></table>
<p><strong>No single fluorescence cutoff defines a safe transplant.</strong> Consider antibody specificity, strength, assay limitations, crossmatch results and the recipient's history together. Incompatible transplantation requires a specialist protocol.</p></section>

<section id="drugs"><h2>3 Immunosuppressive drugs</h2>
<p>A common maintenance regimen combines <strong>tacrolimus, mycophenolate and a corticosteroid</strong>. Induction treatment is given around transplantation; the agent depends on rejection risk and the treatment protocol.</p>
<table><thead><tr><th>Drug or class</th><th>Main action</th><th>Characteristic problems</th></tr></thead><tbody>
<tr><td><strong>Tacrolimus</strong></td><td>Binds FKBP; inhibits calcineurin, reducing NFAT activation and IL-2 transcription.</td><td>Nephrotoxicity, tremor, hyperkalemia, hypomagnesemia, hypertension and diabetes.</td></tr>
<tr><td><strong>Cyclosporine</strong></td><td>Binds cyclophilin; also inhibits calcineurin.</td><td>Nephrotoxicity, hypertension, gingival enlargement, hirsutism and dyslipidemia.</td></tr>
<tr><td><strong>Mycophenolate</strong></td><td>Inhibits inosine monophosphate dehydrogenase, reducing new guanine nucleotide synthesis in lymphocytes.</td><td>Diarrhea, leukopenia and other cytopenias; fetal harm. Requires a planned alternative before pregnancy.</td></tr>
<tr><td><strong>Sirolimus or everolimus</strong></td><td>Inhibit mTOR signaling and lymphocyte proliferation downstream of growth signals.</td><td>Oral ulcers, poor wound healing, dyslipidemia, proteinuria, cytopenias and pneumonitis.</td></tr>
<tr><td><strong>Belatacept</strong></td><td>Binds CD80/86, preventing CD28-mediated T-cell costimulation.</td><td>Post-transplant lymphoproliferative disorder (PTLD), including CNS disease. <strong>Do not use with negative or unknown EBV serostatus.</strong></td></tr>
<tr><td><strong>Corticosteroids</strong></td><td>Suppress multiple inflammatory and immune pathways.</td><td>Infection, hyperglycemia, hypertension, osteoporosis and weight gain.</td></tr>
<tr><td><strong>Basiliximab</strong></td><td>Blocks the IL-2 receptor CD25; used for induction.</td><td>Does not deplete T cells; choice depends on immunological risk.</td></tr>
<tr><td><strong>Antithymocyte globulin (ATG)</strong></td><td>Depletes T cells; used for selected induction and rejection treatment.</td><td>Infusion reactions, cytopenias and opportunistic infection.</td></tr>
</tbody></table>
<p><strong>Tacrolimus and sirolimus both bind FKBP, but inhibit different targets.</strong> Tacrolimus inhibits calcineurin; sirolimus inhibits mTOR. Impaired wound healing and mouth ulcers favor an mTOR inhibitor as the cause.</p></section>

<section id="tacrolimus"><h2>4 Tacrolimus toxicity and interactions</h2>
<p><strong>Rising creatinine with tremor, hypertension, hyperkalemia and a high trough level suggests tacrolimus toxicity.</strong> Acute renal vasoconstriction can reduce graft filtration. Severe neurological toxicity may include seizures or posterior reversible encephalopathy syndrome.</p>
<table><thead><tr><th>Interaction</th><th>Effect on tacrolimus</th></tr></thead><tbody>
<tr><td>Azole antifungals, including <strong>fluconazole</strong>; clarithromycin; ritonavir-containing treatment; diltiazem or verapamil</td><td>Can increase concentrations through CYP3A inhibition. Magnitude varies by drug and patient.</td></tr>
<tr><td>Rifampicin, carbamazepine, phenytoin and St John's wort</td><td>Can lower concentrations through enzyme induction and increase rejection risk.</td></tr>
<tr><td>Starting or stopping an interacting drug</td><td>Recheck levels and adjust dosing; removal of an inhibitor or inducer also changes exposure.</td></tr>
</tbody></table>
<p>Confirm that the sample is a true <strong>pre-dose trough</strong>, review medicines and recent diarrhea, and assess potassium, magnesium and renal function. Reduce or temporarily withhold tacrolimus when indicated, with the transplant team.</p>
<p><strong>A high level does not exclude obstruction, infection or rejection.</strong> Persistent dysfunction after correcting exposure still requires investigation. Target troughs vary with time after transplantation, rejection risk and the accompanying drugs.</p></section>

<section id="dysfunction"><h2>5 Approach to a rise in creatinine</h2>
<ol><li><strong>Confirm the change and assess urgency.</strong> Compare with the established baseline; check urine output, BP, volume status, potassium and acid–base status.</li>
<li><strong>Review reversible causes.</strong> Look for dehydration, sepsis, recent drugs, interactions, missed immunosuppression and an incorrectly timed drug level.</li>
<li><strong>Obtain graft ultrasound with Doppler.</strong> Check perfusion, hydronephrosis and collections. Sudden anuria soon after surgery needs urgent assessment.</li>
<li><strong>Choose targeted tests.</strong> Urinalysis, urine culture and protein quantification; tacrolimus trough; BK PCR, CMV testing and DSA when clinically indicated.</li>
<li><strong>Biopsy persistent unexplained dysfunction.</strong> Histology can separate rejection, viral injury, drug toxicity and recurrent disease.</li></ol>
<p><strong>Do not assume every creatinine rise is rejection.</strong> Increasing immunosuppression without establishing the cause can worsen BK infection. Conversely, a normal ultrasound does not exclude rejection.</p>
<p><strong>Delayed graft function:</strong> commonly defined as dialysis during the first seven days after transplantation. This is an operational definition, not a diagnosis of the cause. Ischemic tubular injury is common, but thrombosis, obstruction and rejection must still be considered.</p></section>

<section id="surgical"><h2>6 Surgical and vascular complications</h2>
<table><thead><tr><th>Presentation</th><th>Likely problem</th><th>Immediate approach</th></tr></thead><tbody>
<tr><td>Sudden oliguria or anuria soon after surgery; absent arterial flow</td><td><strong>Renal artery thrombosis</strong></td><td>Urgent transplant surgical assessment. Rapid restoration of flow may determine graft survival.</td></tr>
<tr><td>Swollen painful graft, hematuria and abrupt dysfunction; abnormal venous flow</td><td><strong>Renal vein thrombosis</strong></td><td>Urgent Doppler and surgical assessment.</td></tr>
<tr><td>Rising creatinine with hydronephrosis and preserved perfusion</td><td><strong>Ureteric obstruction</strong></td><td>Identify and relieve the obstruction promptly; nephrostomy or stenting may be needed.</td></tr>
<tr><td>Perigraft collection with possible ureteric compression or leg swelling</td><td>Lymphocele; also consider urinoma or hematoma</td><td>Define the collection and its effect. Fluid analysis can help identify a urine leak.</td></tr>
<tr><td>Worsening or resistant hypertension, graft bruit, high anastomotic velocity on Doppler</td><td><strong>Transplant renal artery stenosis</strong></td><td>Confirm significant stenosis and assess for intervention when it causes hypertension or graft dysfunction.</td></tr>
</tbody></table>
<p>The transplanted kidney is denervated. <strong>Obstruction may be painless</strong>; absence of colic does not exclude it.</p></section>

<section id="rejection"><h2>7 Recognizing and treating rejection</h2>
<table><thead><tr><th>Type</th><th>Main findings</th><th>Treatment principle</th></tr></thead><tbody>
<tr><td><strong>Hyperacute rejection</strong></td><td>Minutes to hours; preformed antibody activates complement and injures vessels. Immediate nonfunction, a mottled graft and vascular thrombosis are characteristic.</td><td>Emergency transplant assessment; established extensive injury is often irreversible.</td></tr>
<tr><td><strong>T-cell–mediated rejection</strong></td><td>Interstitial inflammation and tubulitis; more severe disease may involve arteries.</td><td>Clinically significant acute rejection is usually treated with corticosteroids. Steroid-resistant or severe disease may require ATG.</td></tr>
<tr><td><strong>Active antibody-mediated rejection</strong></td><td>Compatible tissue injury, evidence of antibody interaction with endothelium and supporting antibody findings. Glomerulitis and peritubular capillaritis are important lesions.</td><td>Specialist treatment often includes plasma exchange, IV immunoglobulin and corticosteroids; additional agents depend on the setting.</td></tr>
<tr><td><strong>Chronic active antibody-mediated rejection</strong></td><td>Chronic injury such as transplant glomerulopathy, with evidence of ongoing antibody-mediated activity.</td><td>Optimize adherence and maintenance treatment and address BP/proteinuria. Treatment benefit is less established than for acute active disease.</td></tr>
</tbody></table>
<p><strong>C4d-negative staining does not exclude antibody-mediated rejection.</strong> Sufficient microvascular inflammation with DSA can meet diagnostic criteria; validated molecular findings may support assessment. Interpret the complete biopsy and antibody results.</p>
<p><strong>Glomerular basement membrane double contours suggest transplant glomerulopathy.</strong> They are not specific for rejection; recurrent glomerular disease and chronic thrombotic microangiopathy must be excluded.</p>
<p>Microvascular inflammation with both negative DSA and negative C4d is a separate pattern requiring investigation; do not automatically call it antibody-mediated rejection. Isolated peritubular capillaritis also needs caution with infection or T-cell rejection. Obtain biopsy before treatment when feasible; urgent circumstances may require treatment without delay.</p></section>

<section id="cmv"><h2>8 Cytomegalovirus</h2>
<p><strong>D+/R− means CMV-positive donor and CMV-negative recipient.</strong> This is the highest-risk pairing for primary donor-derived CMV infection. R+ recipients remain at risk from reactivation or reinfection.</p>
<table><thead><tr><th>Problem</th><th>Approach</th></tr></thead><tbody>
<tr><td>Prevention in a D+/R− kidney recipient</td><td>Prophylaxis, commonly for about six months, or a closely monitored preemptive strategy. Valganciclovir or letermovir may be used for prophylaxis under the transplant protocol.</td></tr>
<tr><td>Fever, leukopenia, diarrhea or suspected organ disease</td><td>Check quantitative CMV DNA. Suspected colitis may require endoscopy and tissue diagnosis; blood PCR alone does not establish tissue invasion.</td></tr>
<tr><td>Nonsevere disease with reliable oral absorption</td><td>Renal-adjusted <strong>valganciclovir</strong> is commonly used.</td></tr>
<tr><td>Severe disease or unreliable oral absorption</td><td><strong>IV ganciclovir</strong>; adjust to kidney function and monitor blood counts and viral load.</td></tr>
</tbody></table>
<p><strong>Letermovir is a prevention drug, not standard treatment for established CMV disease.</strong> Prophylaxis delays or reduces disease; symptoms after it ends still warrant assessment.</p></section>

<section id="bk"><h2>9 BK polyomavirus</h2>
<table><thead><tr><th>Finding</th><th>Action or interpretation</th></tr></thead><tbody>
<tr><td><strong>Routine adult plasma screening</strong></td><td>Monthly through month 9, then every three months through year 2. Increase surveillance after treatment for rejection.</td></tr>
<tr><td>Plasma BK DNA 1,000–10,000 copies/mL</td><td>Confirm persistence, usually within 2–3 weeks. Sustained levels warrant a treatment review.</td></tr>
<tr><td>Persistent DNAemia above 1,000, a level above 10,000, or biopsy-proven nephropathy</td><td><strong>Reduce maintenance immunosuppression stepwise</strong>, balancing rejection risk; follow plasma PCR about every 2–4 weeks.</td></tr>
<tr><td>Viral inclusions in tubular cells with positive SV40 large T-antigen staining</td><td>Supports polyomavirus nephropathy in the appropriate clinical setting.</td></tr>
</tbody></table>
<p>Stable creatinine does not make sustained BK DNAemia harmless. Biopsy is especially useful with graft dysfunction, high immunological risk or uncertainty about rejection. PCR values depend on the assay; follow trends using comparable tests.</p>
<p><strong>BK nephropathy and rejection can both cause interstitial inflammation.</strong> Their treatment may require opposite changes in immunosuppression. There is no established routine antiviral substitute for reducing immunosuppression.</p></section>

<section id="infection"><h2>10 Other infections and PTLD</h2>
<table><thead><tr><th>Clinical clue</th><th>Diagnosis or prevention</th><th>Key point</th></tr></thead><tbody>
<tr><td>Progressive dyspnea, hypoxemia and diffuse pulmonary infiltrates</td><td><strong>Pneumocystis jirovecii</strong></td><td>TMP–SMX prophylaxis reduces risk. Duration varies by protocol; restart or extend after intensified immunosuppression when indicated.</td></tr>
<tr><td>Pulmonary nodules with brain abscesses or ring-enhancing lesions</td><td><strong>Nocardia</strong></td><td>Assess for CNS spread and obtain microbiological confirmation. Treatment depends on severity and susceptibility; disseminated disease often needs combination therapy.</td></tr>
<tr><td>Severe persistent anemia, very low reticulocytes, relatively preserved other cell lines</td><td><strong>Parvovirus B19 pure red-cell aplasia</strong></td><td>Check PCR; antibody responses may be weak. Treatment commonly includes IV immunoglobulin and review of immunosuppression.</td></tr>
<tr><td>Lymphadenopathy, fever, weight loss, extranodal masses or new CNS symptoms</td><td><strong>PTLD</strong></td><td>EBV mismatch, particularly D+/R−, increases risk. Obtain tissue diagnosis; EBV DNA alone does not establish PTLD.</td></tr>
</tbody></table>
<p><strong>PTLD treatment depends on histology and extent.</strong> Carefully reduce immunosuppression when feasible; CD20-positive B-cell disease may require rituximab, with further lymphoma treatment according to response and subtype.</p>
<h3>Timing helps but does not exclude a diagnosis</h3>
<ul><li><strong>First month:</strong> surgical, hospital-acquired and donor-derived infections are prominent.</li>
<li><strong>Months 1–6:</strong> opportunistic infection becomes more important, depending on prophylaxis.</li>
<li><strong>After six months:</strong> community infections predominate in stable recipients. Recent rejection treatment can restore a high opportunistic-infection risk at any time.</li></ul></section>

<section id="recurrence"><h2>11 Recurrent kidney disease</h2>
<table><thead><tr><th>Finding</th><th>Likely cause</th><th>Important distinction</th></tr></thead><tbody>
<tr><td>Heavy proteinuria within hours or days of transplantation; diffuse foot-process effacement</td><td><strong>Recurrent primary FSGS</strong></td><td>A circulating permeability factor is suspected. Early light microscopy may lack established segmental scars.</td></tr>
<tr><td>Previous genetic or secondary FSGS</td><td>Recurrence risk is generally lower than in primary FSGS</td><td>Determine the original disease rather than treating all FSGS as the same recurrence risk.</td></tr>
<tr><td>Graft dysfunction with thrombocytopenia, hemolysis or biopsy thrombotic microangiopathy; prior complement-mediated aHUS</td><td><strong>Recurrent complement-mediated disease</strong></td><td>Risk depends on the complement abnormality. TMA also occurs with rejection and calcineurin-inhibitor toxicity.</td></tr>
</tbody></table>
<p>Recurrent primary FSGS needs prompt transplant assessment; plasma exchange is often used, with additional treatment individualized. <strong>Routine preventive plasma exchange or rituximab before every FSGS transplant is not established.</strong></p>
<p><strong>Eculizumab blocks C5</strong> and can prevent or treat recurrent complement-mediated aHUS in selected recipients. Arrange meningococcal vaccination and antimicrobial prevention as indicated. Vaccination does not eliminate meningococcal risk.</p></section>

<section id="followup"><h2>12 Long-term care</h2>
<table><thead><tr><th>Problem</th><th>What to do</th></tr></thead><tbody>
<tr><td><strong>Skin cancer</strong></td><td>Cutaneous squamous cell carcinoma is markedly increased. Encourage sun protection, self-examination and regular skin assessment; evaluate persistent lesions.</td></tr>
<tr><td><strong>Post-transplant erythrocytosis</strong></td><td>Confirm persistent elevation, commonly Hb above 17 g/dL or hematocrit above 51%. Assess hypoxia, renal artery stenosis and other causes. ACE inhibitor or ARB treatment often lowers Hb; monitor potassium and creatinine.</td></tr>
<tr><td><strong>Vaccination</strong></td><td>Complete needed vaccines before transplantation when possible. Give indicated non-live vaccines after transplantation at appropriate intervals. Generally avoid live vaccines during significant immunosuppression, including live varicella vaccine.</td></tr>
<tr><td>Cardiovascular and metabolic risk</td><td>Monitor BP, glucose, lipids, weight, graft function and proteinuria. Review bone health and age-appropriate cancer screening.</td></tr>
<tr><td>Adherence and pregnancy planning</td><td>Review dosing, access to medicines, interactions and pregnancy intentions. Do not stop or substitute immunosuppressants without a coordinated plan.</td></tr>
</tbody></table>
<p><strong>Recombinant zoster vaccine is non-live.</strong> It differs from live varicella vaccine; recommendations should follow age, clinical setting and local schedules.</p></section>

<section id="calculations"><h2>13 Useful calculations</h2>
<table><thead><tr><th>Calculation</th><th>Worked example</th><th>Interpretation</th></tr></thead><tbody>
<tr><td><strong>Total daily dose</strong> = dose each time × doses per day</td><td>Mycophenolate 1 g twice daily = 2 g/day = <strong>2,000 mg/day</strong>.</td><td>This is an arithmetic example, not a universal prescription. A stated weight of 70 kg does not change this fixed-dose calculation.</td></tr>
<tr><td><strong>Creatinine rise (%)</strong> = 100 × (new − baseline) ÷ baseline</td><td>1.0 → 1.5 mg/dL: 100 × 0.5/1.0 = <strong>50% rise</strong>.</td><td>A substantial rise needs evaluation; do not wait for a particular percentage when other concerning findings are present.</td></tr>
<tr><td><strong>Log decrease</strong> = log10(initial ÷ final)</td><td>BK 40,000 → 4,000: ratio 10; <strong>1 log10 decrease</strong>, equivalent to a 90% fall.</td><td>A 1-log fall is a tenfold reduction. Use the same sample type, units and preferably the same assay.</td></tr>
</tbody></table></section>

<section id="pitfalls"><h2>14 Pitfalls</h2>
<ul><li><strong>ABO compatible does not mean DSA negative.</strong> HLA-DQ antibody can still matter.</li>
<li><strong>EBV-negative or unknown status excludes belatacept use.</strong></li>
<li><strong>Fluconazole can raise tacrolimus concentrations.</strong> Check levels when interacting treatment is started or stopped.</li>
<li><strong>Sudden anuria after surgery needs urgent perfusion and obstruction assessment.</strong> Do not label it delayed graft function without investigating.</li>
<li><strong>Negative C4d does not rule out antibody-mediated rejection.</strong></li>
<li><strong>BK usually calls for less immunosuppression; rejection often calls for more.</strong> Establish the cause of graft dysfunction.</li>
<li><strong>CMV PCR positivity and CMV tissue-invasive disease are different findings.</strong> Investigate the affected organ when indicated.</li>
<li><strong>Early nephrotic proteinuria suggests recurrent primary FSGS.</strong></li>
<li><strong>A persistent unexplained creatinine rise warrants biopsy.</strong> A normal ultrasound does not exclude disease within the graft.</li></ul></section>'''


def make():
    doc=html.fragment_fromstring(BODY,create_parent='div')
    ids=doc.xpath('.//*[@id]/@id')
    assert len(ids)==len(set(ids))
    assert all(h.startswith('#') and h[1:] in ids for h in doc.xpath('.//a/@href'))
    tables=doc.xpath('.//table')
    for table in tables:
        count=len(table.xpath('./thead/tr/th'))
        assert count and all(len(row.xpath('./td'))==count for row in table.xpath('./tbody/tr'))
    coverage=['candidate','candidate','compatibility','compatibility','compatibility','drugs','drugs','drugs','drugs','drugs',
        'tacrolimus','tacrolimus','rejection','rejection','rejection','rejection','rejection','cmv','cmv','bk','bk','bk',
        'infection','infection','infection','infection','surgical','surgical','dysfunction','surgical','recurrence','recurrence',
        'followup','followup','followup','calculations','calculations','calculations','rejection','dysfunction']
    assert len(coverage)==40 and all(key in ids for key in coverage)
    assert not doc.xpath('.//script|.//iframe|.//h1')
    destination=DEST/'Nephrology/Kidney Transplantation.html'
    destination.parent.mkdir(parents=True,exist_ok=True)
    document=page('Kidney transplantation',BODY).replace('<h1>Kidney transplantation</h1>','',1)
    document=document.replace('</style>','table{display:table;width:100%}th:first-child,td:first-child{min-width:120px}@media(max-width:650px){table{display:block;overflow-x:auto}}</style>')
    destination.write_text(document,encoding='utf-8')
    sources=[
        'https://kdigo.org/guidelines/transplant-candidate/',
        'https://kdigo.org/wp-content/uploads/2026/04/KDIGO-2020-Transplant-Candidate-Guideline.pdf',
        'https://kdigo.org/wp-content/uploads/2017/02/KDIGO-2009-Transplant-Recipient-Guideline-English.pdf',
        'https://banfffoundation.org/central-repository-for-banff-classification-resources-3/',
        'https://pmc.ncbi.nlm.nih.gov/articles/PMC9292213/',
        'https://doi.org/10.1097/TP.0000000000003095',
        'https://pmc.ncbi.nlm.nih.gov/articles/PMC11335089/',
        'https://bts.org.uk/uk-guideline-on-management-of-bk-polyomavirus-bkpyv-infection-and-disease-following-kidney-transplantation/',
        'https://pmc.ncbi.nlm.nih.gov/articles/PMC12180710/',
        'https://packageinserts.bms.com/pi/pi_nulojix.pdf',
        'https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=7f667de1-9dfa-4bd6-8ba0-15ee2d78873b&type=display',
        'https://cdsco.gov.in/opencms/resources/UploadCDSCOWeb/2018/UploadPrescribingInfo/6Mycophanolate%20Mofetil.pdf',
        'https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=3e7aa7ef-665f-4dd4-a14b-b90949bb646f',
        'https://www.transplant.bc.ca/Documents/Statistics/Clinical%20Guidelines%20for%20Kidney%20Transplantation.pdf',
        'https://www.cdc.gov/vaccines/hcp/imz-best-practices/altered-immunocompetence.html',
        'https://www.cdc.gov/meningococcal/risk-factors/receiving-complement-inhibitors.html',
    ]
    review=dict(module='Kidney Transplantation',status='authored',groups=len(doc.xpath('./section')),
        tables=len(tables),sourceCheckedAt='2026-11-06',independentClinicianReview=False,
        visibleReferences=False,visibleTitle=False,
        questionCoverage={str(i):key for i,key in enumerate(coverage,1)},checkedSources=sources)
    destination.with_suffix('.review.json').write_text(json.dumps(review,indent=2),encoding='utf-8')
    manifest=DEST/'authored-notes.json'
    authored=json.loads(manifest.read_text(encoding='utf-8')) if manifest.is_file() else {}
    authored['Nephrology/Kidney Transplantation']=dict(file=str(destination),sections=review['groups'],tables=len(tables),
        references=0,words=len(doc.text_content().split()),status='authored_source_checked',chapterOrder=10)
    manifest.write_text(json.dumps(authored,indent=2),encoding='utf-8')
    print(destination)
    print(f'{review["groups"]} sections; {len(tables)} tables; {len(doc.text_content().split())} words; 40 questions mapped')


if __name__=='__main__':make()
