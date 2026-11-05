"""Author review of distractor plausibility and repeated learning objectives; not independent review."""
import json
from qbank_authoring import ROOT,finalize,question,ref

def review():
    banks={b['chapterOrder']:b for p in (ROOT/'completed/Oncology').glob('*/*/questions.json') for b in [json.loads(p.read_text(encoding='utf-8'))]};edits=[]
    def change(ch,n,needle,choices):
        item=banks[ch]['questions'][n-1];assert needle.casefold() in item['question'].casefold(),(ch,n,needle)
        indices=[i for i in range(4) if i!=item['correctIndex']];assert len(choices)==3
        for i,(option,reason) in zip(indices,choices):item['options'][i]=option
        item['explanationTeaching']['otherOptions']=[dict(optionIndex=i,explanation=r) for i,(_,r) in zip(indices,choices)]
        item['optionReview']='Author-revised distractor plausibility; no independent clinician review';edits.append(item['id'])
    change(1,7,'prefix',[
      ('Pathological stage assigned before any preoperative treatment','The y prefix indicates assessment during or after initial multimodality treatment.'),
      ('Clinical stage after preoperative treatment without a pathological specimen','The p component indicates pathological rather than clinical classification.'),
      ('Recurrent disease classified after a disease-free interval','Recurrence uses a different prefix; yp denotes post-treatment pathological classification.')])
    change(1,9,'most of the day',[
      ('ECOG 1','ECOG 1 permits light or sedentary work; the stem specifies inability to work.'),
      ('ECOG 3','This entails limited self-care and confinement to bed/chair for more than half of waking hours.'),
      ('ECOG 4','This denotes complete disability and inability to perform self-care.')])
    change(1,10,'limited personal',[
      ('ECOG 2','ECOG 2 retains self-care and spends more than half of waking hours out of bed.'),
      ('ECOG 4','This implies complete disability and inability to perform any self-care.'),
      ('ECOG 1','This remains ambulatory with capacity for light work.')])
    change(1,19,'3 years',[
      ('Length-time bias','This concerns preferential detection of more slowly progressive disease rather than advancing diagnosis for the same death date.'),
      ('Overdiagnosis','That means detecting a cancer that would never become clinically important during life; the stem describes earlier recognition of lethal disease.'),
      ('Stage migration','That concerns movement between stage categories after more sensitive staging.')])
    change(1,20,'slow-growing',[
      ('Lead-time bias','That reflects an earlier starting point for measured survival, not preferential detection by growth rate.'),
      ('Verification bias','That arises when application of a reference standard differs between tested groups.'),
      ('Recall bias','That concerns differential recollection of previous exposures.')])
    change(1,23,'RECIST',[
      ('Stable disease','The 32% reduction from baseline meets the target-lesion partial-response threshold.'),
      ('Complete response','Residual target lesions remain; shrinkage alone is not complete disappearance.'),
      ('Progressive disease','There is no qualifying increase, new lesion or other progression in the stem.')])
    change(2,3,'antipseudomonal',[
      ('Ceftriaxone','It does not provide the required reliable antipseudomonal activity.'),
      ('Ertapenem','Unlike selected other carbapenems, ertapenem does not cover Pseudomonas.'),
      ('Cefazolin','Its narrower spectrum is unsuitable as high-risk febrile-neutropenia monotherapy.')])
    change(2,8,'cecum',[
      ('Clostridioides difficile colitis as the single established diagnosis','It remains a differential, but profound neutropenia with cecal-predominant inflammation is characteristic of neutropenic enterocolitis.'),
      ('Uncomplicated appendicitis as a sufficient explanation without broader assessment','Appendicitis is a differential, but the chemotherapy/neutropenia and bowel-wall pattern raise typhlitis.'),
      ('Acute colonic pseudo-obstruction','Distension may occur, but fever and inflammatory cecal wall thickening in this context favor enterocolitis.')])
    change(2,11,'rasburicase',[
      ('Rasburicase inhibits xanthine oxidase, whereas allopurinol directly degrades existing urate','This reverses the mechanisms.'),
      ('Both principally increase renal urate excretion without affecting production or breakdown','Neither is primarily a uricosuric agent.'),
      ('Allopurinol rapidly converts existing urate to allantoin, whereas rasburicase only prevents new urate','Rasburicase converts urate to allantoin; allopurinol prevents new formation.')])
    change(2,12,'G6PD',[
      ('Hydrogen-peroxide generation can cause oxidative hemolysis and methemoglobinemia only when vitamin B12 is low','The relevant vulnerability is G6PD-related antioxidant deficiency, not B12 deficiency.'),
      ('It predictably causes immune heparin-induced thrombocytopenia','Rasburicase toxicity here is oxidative rather than a heparin/PF4 mechanism.'),
      ('It irreversibly blocks xanthine oxidase in erythrocytes','This is not rasburicase’s uricolytic mechanism or the explanation for the contraindication.')])
    change(2,18,'corticosteroid',[
      ('Dexamethasone 4 mg once daily without an initial higher dose','This is below the NICE adult neurological MSCC initial regimen.'),
      ('Dexamethasone 96 mg routinely for every suspected case','Very high routine dosing increases toxicity and is not the NICE default.'),
      ('Prednisolone 5 mg once daily','This is not an equivalent acute MSCC regimen.')])
    change(2,26,'bisphosphonate',[
      ('Cinacalcet as the default treatment for every PTH-suppressed recurrence','Its main role is selected PTH-mediated disease, not routine refractory humoral hypercalcemia.'),
      ('Calcitonin continued indefinitely as the sole antiresorptive plan','Tachyphylaxis limits its sustained effect; it is mainly a short-term bridge.'),
      ('Oral calcium with calcitriol','This can worsen the hypercalcemia rather than provide antiresorptive treatment.')])
    change(3,2,'cavitating',[
      ('Adenocarcinoma','This may cavitate but the central squamous morphology and PTHrP pattern favor squamous carcinoma.'),
      ('Small-cell carcinoma','Its typical morphology and endocrine associations differ from the supplied squamous differentiation.'),
      ('Typical bronchial carcinoid','This has a different neuroendocrine morphology and usual biological behavior.')])
    change(3,3,'nuclear molding',[
      ('Typical carcinoid tumor','This generally has lower proliferation and lacks the supplied high-grade small-cell pattern.'),
      ('Large-cell neuroendocrine carcinoma','This is high grade but has larger-cell cytology rather than the characteristic molding small cells.'),
      ('Poorly differentiated squamous carcinoma','The neuroendocrine-marker and small-cell morphology favor small-cell carcinoma.')])
    change(3,5,'apical',[
      ('Upper brachial plexus C5–C6 involvement alone','The medial-arm/hand pattern favors the lower plexus, and Horner syndrome requires sympathetic involvement.'),
      ('Phrenic-nerve involvement alone','This can affect diaphragmatic function but does not explain the lower-plexus and Horner pattern.'),
      ('Recurrent-laryngeal nerve involvement alone','Hoarseness would be more characteristic; it does not explain these findings.')])
    change(3,22,'DOG1',[
      ('Gastric leiomyosarcoma','Smooth-muscle morphology and markers would be expected; KIT/DOG1 favors GIST in this context.'),
      ('Gastric schwannoma','This usually has a different immunophenotype, including S100/SOX10 lineage support.'),
      ('Poorly differentiated gastric adenocarcinoma','An epithelial phenotype rather than the described stromal pattern would be expected.')])
    change(3,27,'serum-marker',[
      ('Elevated AFP with normal beta-hCG','An unexplained AFP elevation calls pure seminoma into question.'),
      ('Elevated AFP and beta-hCG together','The AFP component suggests a nonseminomatous component or another source.'),
      ('AFP elevation with isolated LDH normalization','Normal LDH does not make AFP production compatible with pure seminoma.')])
    change(3,30,'pathological measure',[
      ('Clark level as the principal modern T-category measurement','Breslow thickness and ulceration are central; Clark level does not replace them.'),
      ('The surface diameter alone','Diameter is clinically useful but is not the principal histological T-category measure.'),
      ('Degree of pigment darkness alone','Pigment intensity does not determine invasion depth or stage.')])
    change(4,1,'cisplatin',[
      ('Inhibition of topoisomerase I with stabilization of a cleavage complex','This is characteristic of camptothecin derivatives such as irinotecan/SN-38.'),
      ('Inhibition of dihydrofolate reductase','This is a major methotrexate mechanism.'),
      ('Stabilization of microtubules against disassembly','This is characteristic of taxanes.')])
    change(4,2,'thymidylate',[
      ('Depletion of guanine nucleotides through IMP dehydrogenase blockade','This is a different nucleotide-pathway target.'),
      ('Failure to regenerate reduced folate through direct DHFR inhibition','That is the defining methotrexate target rather than the FdUMP complex described.'),
      ('Suppression of topoisomerase II-mediated DNA religation','That is a different DNA-damage mechanism.')])
    change(4,6,'doxorubicin',[
      ('Topoisomerase I poisoning without the anthracycline intercalation mechanism','Topoisomerase I is the principal target of irinotecan/SN-38.'),
      ('Selective disruption of mitotic microtubule assembly','This is a vinca-alkaloid mechanism.'),
      ('Inhibition of thymidylate synthase by a fluorinated nucleotide metabolite','This describes an important fluorouracil mechanism.')])
    change(4,7,'bleomycin',[
      ('Inhibition of topoisomerase II as its defining target','That more directly characterizes etoposide and contributes to anthracycline effects.'),
      ('DNA cross-link formation by platinum adducts','This is a platinum mechanism rather than bleomycin strand damage.'),
      ('Inhibition of ribonucleotide reductase as its principal mechanism','This is characteristic of other antimetabolite strategies.')])
    change(4,9,'D842V',[
      ('Imatinib','PDGFRA D842V is characteristically resistant to imatinib.'),
      ('Sunitinib as a reliably matched initial D842V-specific agent','It is not the specifically active established matched choice in this setting.'),
      ('Regorafenib as the preferred D842V-specific first agent','This later-line GIST agent does not replace the specific avapritinib indication.')])
    change(4,13,'CDK4/6',[
      ('Inhibition of cyclin B–CDK1 at the G2-to-M transition','This describes a different cell-cycle control point.'),
      ('Direct polymerization of spindle microtubules during mitosis','This is not the retinoblastoma-linked G1 checkpoint mechanism.'),
      ('Direct blockade of estrogen synthesis through aromatase','Endocrine partners can do this, but CDK4/6 inhibition targets the cell cycle.')])
    change(4,17,'tamoxifen',[
      ('Tamoxifen reduces estrogen synthesis, whereas aromatase inhibitors modulate the receptor','This reverses the two mechanisms.'),
      ('Tamoxifen degrades the estrogen receptor, whereas aromatase inhibitors antagonize progesterone receptors','Fulvestrant is a SERD; aromatase inhibitors suppress synthesis.'),
      ('Tamoxifen suppresses pituitary GnRH receptors, whereas aromatase inhibitors destroy ovarian tissue','Neither is the defining mechanism of these agents.')])
    change(4,21,'abiraterone',[
      ('Androgen-receptor signaling through direct receptor antagonism','This is characteristic of agents such as enzalutamide, not abiraterone’s principal target.'),
      ('Pituitary GnRH-receptor antagonism','This is the mechanism of GnRH antagonists.'),
      ('Conversion of testosterone to dihydrotestosterone through 5-alpha-reductase','This is the target of drugs such as finasteride, not abiraterone.')])
    change(4,29,'UGT1A1',[
      ('Reduced conversion of irinotecan to SN-38 by carboxylesterases','That would not explain greater SN-38 exposure from impaired glucuronidation.'),
      ('Increased SN-38 binding to EGFR','The relevant issue is metabolic clearance, not an EGFR-binding mechanism.'),
      ('Reduced DPD catabolism of fluorouracil generated from irinotecan','Irinotecan is not a fluorouracil prodrug; UGT1A1 handles SN-38 glucuronidation.')])
    change(5,7,'ptosis',[
      ('Isolated checkpoint myositis without assessing cardiac or junctional overlap','Troponin elevation and ptosis require assessment beyond isolated muscle inflammation.'),
      ('Isolated checkpoint myasthenia without cardiac or muscle injury','Elevated CK and troponin raise concern for a broader overlap.'),
      ('Steroid-induced myopathy as the single best explanation','The early ICI timing, CK elevation, ptosis and cardiac marker pattern favor immune overlap.')])
    change(5,12,'hepatitis',[
      ('Infliximab','Although useful for selected colitis, it is generally avoided in immune hepatitis.'),
      ('Vedolizumab as the usual organ-directed hepatic rescue agent','Its gut-selective action makes it a colitis option rather than standard hepatic rescue.'),
      ('Budesonide alone as sufficient rescue for every severe steroid-refractory case','Severe refractory hepatitis may require additional systemic immunosuppression and specialist care.')])
    change(5,19,'hypomagnesemia',[
      ('Predominantly prerenal azotemia without tubular electrolyte loss','Volume loss can coexist, but persistent magnesium wasting suggests tubular injury.'),
      ('Tumor lysis with phosphate release as the primary explanation','The stem’s cisplatin and magnesium-wasting pattern favors drug-related tubular injury.'),
      ('SIADH causing renal magnesium retention','SIADH primarily affects water balance and does not explain this characteristic pattern.')])
    change(5,21,'vincristine',[
      ('Acute cholinergic hypermotility','This generally causes cramps and diarrhea rather than reduced motility.'),
      ('Neutropenic enterocolitis as established by constipation alone','Fever, neutropenia and inflammatory bowel findings would strengthen that diagnosis.'),
      ('Opioid-independent secretory diarrhea','This is the opposite motility and stool pattern.')])
    change(5,22,'salivation',[
      ('Loperamide','It is important in delayed diarrhea but does not specifically reverse the acute cholinergic syndrome.'),
      ('Octreotide','It may be used in selected severe refractory diarrhea, not as the specific acute antimuscarinic.'),
      ('Ondansetron','It targets a different emetic pathway rather than muscarinic cholinergic symptoms.')])
    change(5,25,'overdose',[
      ('Leucovorin','This modulates fluorouracil activity and is not its overdose antidote.'),
      ('Glucarpidase','This enzymatically cleaves methotrexate rather than fluorouracil.'),
      ('Dexrazoxane','This has anthracycline-related indications, not fluoropyrimidine overdose rescue.')])
    change(5,27,'mesna',[
      ('Proximal renal tubular injury with Fanconi syndrome','Mesna does not reliably prevent ifosfamide tubular nephrotoxicity.'),
      ('Acute central neurotoxicity','Mesna does not provide reliable protection against encephalopathy.'),
      ('Dose-limiting marrow suppression','Mesna’s protective action is urothelial rather than hematopoietic.')])
    change(5,31,'VEGF',[
      ('Hypophysitis and central adrenal insufficiency','These are more characteristic immune-checkpoint endocrinopathies.'),
      ('Cold-triggered dysesthesia and cumulative sensory neuropathy','This is more characteristic of oxaliplatin exposure.'),
      ('Cholinergic diarrhea and salivation','This is associated with acute irinotecan effects rather than VEGF vascular inhibition.')])
    change(6,16,'anti-Hu',[
      ('Thymoma','This is more strongly linked to other autoimmune neurological contexts than anti-Hu sensory neuronopathy.'),
      ('Breast carcinoma','This has important paraneoplastic associations, but SCLC is the major anti-Hu concern.'),
      ('Ovarian carcinoma','This is a key concern with anti-Yo cerebellar disease rather than the supplied anti-Hu phenotype.')])
    change(6,17,'anti-Yo',[
      ('Small-cell lung cancer as the principal anti-Hu-associated pattern','SCLC is important with Hu and other antibodies; anti-Yo particularly directs attention to breast and gynecological sites.'),
      ('Testicular germ-cell tumors as the characteristic association','These more often enter other antibody/phenotype associations, including selected Ma2 contexts.'),
      ('Thymoma-associated myasthenia as the expected tumor–phenotype pair','That is a different antibody and neurological syndrome.')])
    change(6,21,'hypoglycemia',[
      ('An insulin-secreting tumor','Endogenous hyperinsulinism should have inappropriately detectable insulin and C-peptide during hypoglycemia.'),
      ('Exogenous insulin exposure','This generally suppresses C-peptide but leaves measurable insulin, with assay-specific caveats.'),
      ('Sulfonylurea-induced insulin secretion','This ordinarily raises endogenous insulin and C-peptide rather than suppressing both.')])
    change(7,9,'emetogenic',[
      ('A 5-HT3 antagonist, dexamethasone and an NK1 antagonist without olanzapine','The updated standard four-drug high-emetic-risk regimen includes olanzapine unless a patient-specific reason changes the plan.'),
      ('A 5-HT3 antagonist and dexamethasone alone','This omits NK1 blockade and olanzapine needed in the standard high-risk regimen.'),
      ('Olanzapine and dexamethasone without 5-HT3 or NK1 blockade','This is not the full recommended prophylactic combination.')])
    change(7,10,'before any drug',[
      ('Acute chemotherapy-induced nausea','This occurs after drug exposure, generally during the first 24 hours.'),
      ('Delayed chemotherapy-induced nausea from the current cycle','The current cycle has not yet been administered.'),
      ('Breakthrough nausea despite prophylaxis during the current administration','This describes nausea despite current-cycle antiemetics rather than a cue-triggered pre-treatment response.')])

    # Replace repeated objectives with distinct, treatment-relevant questions.
    def replace(ch,n,needle,item):
        old=banks[ch]['questions'][n-1];assert needle.casefold() in old['question'].casefold() or old['question']==item['question'],(ch,n)
        banks[ch]['questions'][n-1]=item;edits.append(old['id']+' objective revised')
    replace(4,15,'prognostic',question(
      'Why is dual BRAF and MEK inhibition used rather than BRAF-inhibitor monotherapy in appropriate BRAF V600-mutant melanoma settings?',
      'It provides more complete MAPK-pathway suppression and can delay resistance compared with BRAF blockade alone',[
       ('MEK inhibition converts a BRAF-wild-type tumor into a BRAF V600-mutant tumor','It blocks downstream signaling rather than creating a driver mutation.'),
       ('The combination removes the need to confirm the BRAF alteration','Molecular eligibility remains essential.'),
       ('MEK inhibition works solely by increasing estrogen synthesis','MEK is a kinase in the MAPK pathway, not an endocrine synthesis enzyme.')],
      'Vertical pathway inhibition can improve control','**BRAF and MEK lie at different levels of the MAPK signaling cascade.**',['Combined inhibition has established roles in specific BRAF-mutant settings.','Benefit does not make every BRAF variant or tumor type equivalent.'],'**Confirm the variant and use disease-specific evidence.**',['Monitor class-specific cardiac, ocular, skin and febrile toxicities.','Do not use a melanoma regimen indiscriminately for colorectal cancer.'],[['BRAF','Upstream kinase target'],['MEK','Downstream kinase target'],['Combination','Deeper pathway blockade']],
      [ref('NCI melanoma professional summary','https://www.cancer.gov/types/skin/hp/melanoma-treatment-pdq')]))
    replace(4,25,'progression-free',question(
      'What is the rationale for tissue-agnostic treatment of an advanced solid tumor with a validated NTRK gene fusion under an applicable drug indication?',
      'The oncogenic fusion can provide a predictive target across several anatomical tumor types',[
       ('Any NTRK point mutation is equivalent to a functional NTRK fusion','Alteration type matters; not every variant is an actionable fusion.'),
       ('NTRK staining alone proves every relevant genomic fusion','Screening and confirmatory testing require appropriate validation.'),
       ('A tissue-agnostic indication removes every stage and prior-treatment eligibility condition','The specific drug indication still defines eligibility.')],
      'A shared driver can matter across anatomical sites','**Tissue-agnostic therapy uses a validated molecular feature to select treatment.**',['A functional NTRK fusion is different from nonspecific expression or an unrelated variant.','Assay selection must account for fusion partners and technical limitations.'],'**Confirm the result and current indication.**',['Review drug interactions, CNS disease and resistance where relevant.','Retain the pathological diagnosis and clinical context.'],[['Predictive feature','Validated oncogenic fusion'],['Anatomical site','May span multiple tumor types'],['Eligibility','Drug-specific conditions']],
      [ref('FDA larotrectinib NTRK-fusion solid-tumor approval','https://www.fda.gov/drugs/fda-approves-larotrectinib-solid-tumors-ntrk-gene-fusions')]))
    replace(6,5,'tumor-only',question(
      'A woman has a pathogenic germline BRCA1 variant. Her brother is healthy. Which statement about inheritance is correct?',
      'Men can carry and transmit the familial variant; each child of a heterozygous carrier has a 50% chance of inheriting it',[
       ('Only female relatives can inherit BRCA1 variants','Inheritance is not restricted to women.'),
       ('A healthy man cannot carry a cancer-predisposition variant','Penetrance is incomplete and the tumor spectrum differs by sex and gene.'),
       ('Every child of a carrier must inherit the variant','Autosomal-dominant transmission from a heterozygous parent is typically 50% per child.')],
      'Sex-influenced cancer risk does not mean sex-limited inheritance','**BRCA1/2 predisposition is inherited in an autosomal-dominant manner.**',['Men can be carriers and can transmit the variant.','Risk magnitude and surveillance depend on the gene and individual context.'],'**Offer targeted familial-variant testing through counseling.**',['Do not exclude a paternal family history.','A positive result indicates predisposition rather than certainty of cancer.'],[['Transmission','Either parent'],['Per-child probability','50% from a heterozygous carrier'],['Cancer development','Incomplete penetrance']],
      [ref('NCI BRCA gene changes and cancer risk','https://www.cancer.gov/about-cancer/causes-prevention/genetics/brca-fact-sheet')],style='clinical_scenario'))
    fixes={
      'https://www.cancer.gov/types/kidney/hp/vhl-syndrome-pdq':'https://www.cancer.gov/publications/pdq/information-summaries/genetics/vhl-syndrome-hp-pdq',
      'https://www.cancer.gov/types/stomach/hp/hereditary-diffuse-gastric-cancer-pdq':'https://www.cancer.gov/publications/pdq/information-summaries/genetics/hereditary-diffuse-gastric-cancer-hp-pdq',
      'https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-avapritinib-gastrointestinal-stromal-tumor-rare-mutation':'https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/212035s004lbl.pdf'}
    for bank in banks.values():
        for item in bank['questions']:
            for r in item['references']:r['url']=fixes.get(r['url'],r['url'])
    slugs={1:'principles',2:'emergencies',3:'solid',4:'systemic',5:'toxicity',6:'genetics',7:'supportive'}
    for order,b in sorted(banks.items()):finalize('Oncology',order,b['headingText'],'onco-'+slugs[order],b['questions'],b['targetQuestions'])
    (ROOT/'oncology-author-review.json').write_text(json.dumps(dict(authorReview=True,independentClinicianReview=False,revisedQuestions=len(edits),changes=edits),indent=2),encoding='utf-8')
    print('Author-revised questions:',len(edits))

if __name__=='__main__':review()
