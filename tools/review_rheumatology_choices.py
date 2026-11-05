"""Apply explicit distractor revisions to authored banks before mapping/installing.

This is an author plausibility pass, not independent clinical review. Run after
chapter creation; finalization preserves IDs, answer balance and rich-text output.
"""
import json
from qbank_authoring import ROOT,finalize

def review():
    banks={b['chapterOrder']:b for p in (ROOT/'completed/Rheumatology').glob('*/*/questions.json') for b in [json.loads(p.read_text(encoding='utf-8'))]}
    edits=[]
    def change(ch,n,answer,choices,stem=None):
        item=banks[ch]['questions'][n-1];correct=item['correctIndex']
        item['options'][correct]=answer
        indices=[i for i in range(4) if i!=correct]
        for i,(option,rationale) in zip(indices,choices):item['options'][i]=option
        assert len(choices)==3
        item['explanationTeaching']['otherOptions']=[dict(optionIndex=i,explanation=rationale) for i,(_,rationale) in zip(indices,choices)]
        if stem:item['question']=stem
        item['optionReview']='Author-revised distractor plausibility; no independent clinical review'
        edits.append(dict(chapter=ch,question=n,id=item['id']))

    change(1,8,'Septic arthritis',[
      ('Rheumatoid monoarticular flare','A flare is possible, but fever and acute monoarthritis during biologic therapy require urgent exclusion of infection.'),
      ('Acute CPP crystal arthritis','CPPD can cause fever and a hot knee, but aspiration must also assess infection.'),
      ('Acute gout','Gout is a differential; finding crystals would still not completely exclude infection.')],
      'A patient with controlled RA develops an acutely hot swollen knee and fever while taking a biologic. Which diagnosis is the most urgent to exclude by arthrocentesis?')
    change(1,9,'Cervical instability with spinal cord compression',[
      ('Median nerve entrapment at the wrist','This can cause hand symptoms but does not explain brisk reflexes and possible myelopathy.'),
      ('Cervical radiculopathy without cord involvement','Radiculopathy can cause focal symptoms, but upper motor neuron signs raise concern for cord involvement.'),
      ('Length-dependent peripheral polyneuropathy','This generally causes distal sensory loss and reduced rather than brisk reflexes.')])
    change(1,11,'High-resolution chest CT together with pulmonary function assessment',[
      ('Chest radiography alone','A normal radiograph does not exclude clinically important interstitial disease.'),
      ('CT pulmonary angiography as the sole routine ILD assessment','It can answer an embolic question but does not replace the dedicated structural/functional ILD approach.'),
      ('Surgical lung biopsy before HRCT','Biopsy is not the universal first investigation for a compatible ILD presentation.')])
    change(1,12,'Rheumatoid vasculitis with mononeuritis multiplex',[
      ('Lumbar radiculopathy','This can cause foot drop but does not unify the palpable purpura and systemic syndrome.'),
      ('Diabetic length-dependent polyneuropathy','This usually has a different distribution and does not explain the vasculitic skin lesions.'),
      ('Common peroneal entrapment neuropathy','This can cause focal foot drop but does not explain systemic and cutaneous vascular findings.')])
    change(1,13,'Methotrexate',[
      ('Hydroxychloroquine','This can suit selected low-activity disease but is not usually the anchor for moderate-to-high activity.'),
      ('Sulfasalazine','This is a conventional alternative in appropriate patients, but methotrexate is the usual anchor in the stated suitable patient.'),
      ('Leflunomide','This is an effective alternative when methotrexate is unsuitable rather than the usual default anchor in this stem.')])
    change(1,19,'Major cardiovascular, malignancy and thrombotic safety concerns',[
      ('Retinal toxicity as the main history-specific risk','This is a hydroxychloroquine-associated issue and does not explain why prior MI, smoking and DVT matter for tofacitinib.'),
      ('Drug-induced lupus as the main history-specific risk','This is not the principal concern prompted by these cardiovascular and thrombotic factors.'),
      ('Calcineurin-mediated nephrotoxicity','Tofacitinib is a JAK inhibitor, not a calcineurin inhibitor.')])
    change(1,22,'Rituximab',[
      ('Abatacept','It is a non-TNF RA option, but the prior rituximab-responsive lymphoproliferative disorder gives a specific reason to favor rituximab.'),
      ('Tocilizumab','It can treat RA but is not the agent conditionally favored for this particular prior malignancy context.'),
      ('Adalimumab','A TNF inhibitor is not the guideline-preferred agent in the stated lymphoproliferative setting.')])
    change(1,23,'A suitable non-TNF strategy such as abatacept',[
      ('Infliximab-based escalation','TNF blockade is disfavored in advanced symptomatic heart failure.'),
      ('Etanercept-based escalation','The heart-failure concern also affects this TNF strategy.'),
      ('Adalimumab-based escalation','The guideline favors a suitable non-TNF option rather than this TNF inhibitor in NYHA III/IV disease.')])
    change(1,28,'Methotrexate toxicity from the co-trimoxazole interaction',[
      ('Felty syndrome','RA-associated neutropenia is a differential, but the acute mucositis/pancytopenia after a recognized interaction favors drug toxicity.'),
      ('New myelodysplastic neoplasm','This can cause cytopenias, but the timing and mucosal injury make an interaction-related toxicity more likely.'),
      ('An isolated viral marrow-suppression syndrome','Possible in context, but the documented interacting exposure provides the more direct explanation.')],
      'A patient on methotrexate develops mouth ulcers, bruising and pancytopenia after starting trimethoprim-sulfamethoxazole. What is the most likely cause?')
    change(1,30,'Antiviral prophylaxis with an appropriate HBV monitoring plan',[
      ('HBV DNA and ALT surveillance alone without prophylaxis','Monitoring alone is insufficient for the usual anti-CD20 high-risk strategy in an anti-HBc-positive patient.'),
      ('A hepatitis B vaccine booster without antiviral prophylaxis','Vaccination does not prevent reactivation of existing prior infection under B-cell depletion.'),
      ('HBsAg surveillance alone until clinical hepatitis occurs','This can detect the complication late and does not provide the recommended prevention.')])
    change(1,32,'Continue methotrexate and withhold adalimumab for a dosing interval, restarting after adequate healing and no infection',[
      ('Withhold methotrexate and continue adalimumab through arthroplasty','This reverses the usual ACR/AAHKS strategy.'),
      ('Continue both on their usual schedule through arthroplasty','The biologic is generally withheld around this elective procedure.'),
      ('Withhold both for six months before and after surgery','This unnecessarily prolongs interruption and flare risk beyond the guideline approach.')])
    change(1,33,'Methotrexate, sulfasalazine and hydroxychloroquine',[
      ('Methotrexate, leflunomide and hydroxychloroquine','These are conventional agents but not the standard named triple-therapy combination.'),
      ('Methotrexate, sulfasalazine and azathioprine','This is not the conventional triple-therapy combination.'),
      ('Leflunomide, sulfasalazine and hydroxychloroquine','This omits methotrexate from the standard named strategy.')])
    change(2,15,'Sulfasalazine',[
      ('Hydroxychloroquine','It is not the usual evidence-based conventional option for peripheral SpA synovitis.'),
      ('Azathioprine','It can treat associated bowel disease in selected contexts but is not the usual conventional arthritis choice here.'),
      ('Methotrexate specifically as a proven axial treatment','Methotrexate can have peripheral roles in selected phenotypes, but efficacy for isolated axial disease is not established.')])
    change(3,23,'Basic calcium phosphate-associated Milwaukee shoulder syndrome',[
      ('CPP crystal arthropathy','CPPD can affect the shoulder, but the destructive cuff-tear/large low-cell effusion phenotype is particularly characteristic of Milwaukee shoulder.'),
      ('Chronic tophaceous gout','Gout is a differential, but would require appropriate urate-deposition evidence.'),
      ('Neuropathic shoulder arthropathy','This is an important destructive mimic; neurological findings such as a syrinx would support it.')])
    change(4,6,'DAT positivity without demonstrated active hemolysis',[
      ('Active warm autoimmune hemolytic anemia','A positive DAT alone is insufficient without evidence of ongoing red-cell destruction.'),
      ('Thrombotic microangiopathic hemolytic anemia','The stem provides no schistocytic hemolysis and DAT positivity does not define TMA.'),
      ('Pure red-cell aplasia','The stated normal hemoglobin and isolated DAT do not support this diagnosis.')])
    change(4,8,'Investigate and treat possible infection while assessing other pulmonary causes',[
      ('Treat acute lupus pneumonitis without microbiological assessment','Lupus pneumonitis can resemble infection, but focal consolidation during immunosuppression requires prompt infection assessment.'),
      ('Treat diffuse alveolar hemorrhage as established without checking hemoglobin or further assessment','The stem does not establish the hemorrhagic syndrome.'),
      ('Treat pulmonary embolism as established without further assessment','Embolism can be a differential, but is not proven by the given presentation.')])
    change(4,19,'Glucocorticoids plus mycophenolate plus belimumab',[
      ('Glucocorticoids plus azathioprine plus hydroxychloroquine','This is not an ACR initial triple-immunosuppressive regimen for active proliferative nephritis.'),
      ('Glucocorticoids plus mycophenolate plus anifrolumab','Anifrolumab does not have the same established severe active nephritis role as belimumab in this guideline.'),
      ('Glucocorticoids plus methotrexate plus belimumab','Methotrexate does not replace the renal induction backbone in this regimen.')])
    change(4,35,'A vitamin K antagonist with target INR 2–3',[
      ('A vitamin K antagonist with target INR 1.5–2','This is below the usual target for venous APS secondary prevention.'),
      ('Aspirin alone','This does not provide adequate usual secondary prevention after unprovoked venous APS thrombosis.'),
      ('Rivaroxaban as the default choice regardless of antibody risk profile','High-risk APS has evidence favoring VKA over routine DOAC substitution.')])
    change(4,44,'ADAMTS13 activity with inhibitor/antibody assessment',[
      ('Lupus anticoagulant testing alone','This evaluates an APS-associated mechanism but does not identify severe ADAMTS13 deficiency.'),
      ('Complement C3/C4 alone','Complement results cannot independently identify immune TTP.'),
      ('Direct antiglobulin testing alone','DAT helps assess immune red-cell injury rather than the defining TTP mechanism.')])
    change(5,4,'Interstitial lung disease',[
      ('Pulmonary arterial hypertension as the dominant antibody-specific association','PAH can occur, but anti-topoisomerase I particularly highlights ILD risk.'),
      ('Scleroderma renal crisis as the dominant antibody-specific association','Anti-RNA polymerase III is the more characteristic renal-crisis association.'),
      ('Inflammatory necrotizing myopathy as the defining association','Anti-SRP/HMGCR are more specific to that myopathy phenotype.')])
    change(5,20,'Finger-flexor and quadriceps weakness',[
      ('Symmetric shoulder/hip weakness with heliotrope rash','This more strongly supports dermatomyositis.'),
      ('Fatigable ocular and bulbar weakness with preserved sensation','This favors a neuromuscular-junction disorder.'),
      ('Distal sensory loss with areflexia and little selective quadriceps involvement','This favors peripheral neuropathy rather than the characteristic IBM pattern.')])
    change(5,31,'Intravenous immunoglobulin',[
      ('Hydroxychloroquine alone','It may help skin disease but is not equivalent to the phase 3 evidence for active muscle disease.'),
      ('Etanercept','It does not have the same randomized DM efficacy evidence.'),
      ('Abatacept as the agent established by ProDERM','ProDERM studied IVIG, not abatacept.')])
    change(5,38,'Pulmonary arterial hypertension',[
      ('Isolated asymptomatic bronchiolitis as the principal mortality complication','Airway disease can occur, but PAH is a major recognized severe MCTD complication.'),
      ('Recurrent pulmonary embolism as an inevitable RNP-specific complication','Thromboembolism is a differential, not an inevitable antibody-defined complication.'),
      ('Primary pulmonary alveolar proteinosis as the characteristic vascular complication','This is a different alveolar process, not the characteristic MCTD vascular risk.')])
    change(6,4,'Minor labial salivary gland biopsy with expert histology',[
      ('Repeat isolated anti-SSB testing as an equivalent classification substitute','Isolated anti-SSB does not replace the anti-SSA or biopsy criterion.'),
      ('Salivary ultrasound as an automatically sufficient 2016 scored item','Ultrasound can support assessment, but is not itself a scored item in that framework.'),
      ('Repeated ANA titers as definitive proof','ANA is not sufficiently specific and does not show the glandular histology.')])
    change(6,9,'Sensory neuronopathy/ganglionopathy',[
      ('Length-dependent axonal polyneuropathy','This often starts distally in the feet; sensory ganglionopathy may produce disproportionate ataxia and non-length-dependent deficits.'),
      ('Small-fiber neuropathy','This typically emphasizes pain and autonomic symptoms rather than marked proprioceptive ataxia.'),
      ('Inflammatory myopathy','Muscle weakness does not explain the primary position-sense deficit.')])
    change(6,10,'Interstitial lung disease',[
      ('Pulmonary arterial hypertension','It is a differential for low DLCO, but basal crackles raise concern for parenchymal disease.'),
      ('Isolated upper-airway dryness','This can cause cough but not the full crackles/gas-transfer pattern.'),
      ('Asthma alone','An obstructive/variable airway phenotype would be needed and does not best explain these findings.')])
    change(6,12,'Pilocarpine',[
      ('Hydroxychloroquine','It is not a direct muscarinic secretagogue and does not reliably reverse dryness.'),
      ('Rituximab','It is a B-cell-directed agent, not a direct secretagogue for routine sicca symptoms.'),
      ('Oxybutynin','Its antimuscarinic action can worsen dryness.')])
    change(6,24,'Hypophysitis with pituitary deficiencies and/or diabetes insipidus',[
      ('A nonfunctioning pituitary adenoma as the defining IgG4 lesion','Adenoma is a structural differential but is not the characteristic inflammatory manifestation.'),
      ('Primary autoimmune thyroiditis as the only endocrine manifestation','Thyroid disease can overlap but does not exhaust IgG4 endocrine involvement.'),
      ('Primary hyperparathyroidism as the characteristic mechanism','This is a different endocrine process, not the characteristic IgG4 pituitary phenotype.')])
    change(7,5,'Aortic aneurysm or stenotic disease at involved sites',[
      ('Only recurrent superficial temporal tenderness without structural vascular risk','GCA can cause extracranial damage even when cranial symptoms settle.'),
      ('Only lower-limb deep venous thrombosis as the defining damage pattern','The defining large-vessel damage is arterial, not this isolated venous pattern.'),
      ('Only transient vasospasm without any aneurysm or stenosis risk','Established arterial structural complications can occur.')])
    change(7,17,'High-quality PR3-ANCA and MPO-ANCA antigen-specific assays',[
      ('Indirect immunofluorescence alone without antigen-specific assessment','A fluorescence pattern without antigen specificity is less informative than the current preferred high-quality assays.'),
      ('ANA and extractable nuclear antigen testing as the primary AAV panel','These investigate other connective-tissue diseases rather than the characteristic AAV antigens.'),
      ('Anti-GBM antibody alone','This assesses a key pulmonary-renal differential, but does not replace PR3/MPO testing for suspected GPA/MPA.')])
    change(7,19,'Glucocorticoids with rituximab or cyclophosphamide',[
      ('Glucocorticoids with azathioprine alone','Azathioprine is more commonly a maintenance agent and is not the standard organ-threatening induction backbone.'),
      ('Glucocorticoids with methotrexate despite rapidly progressive GN','Methotrexate is not suitable for this severe renal induction setting.'),
      ('Glucocorticoids with hydroxychloroquine','This does not adequately treat severe necrotizing AAV.')])
    change(7,39,'Pulmonary artery aneurysm and bleeding risk',[
      ('Only a conventional lower-limb embolic source assessment','The DVT is already known; hemoptysis in Behcet specifically requires pulmonary arterial lesion assessment.'),
      ('Only thrombophilia gene testing','This does not resolve the urgent hemorrhagic vascular risk.'),
      ('Only serial D-dimer measurements','D-dimer cannot exclude a pulmonary arterial aneurysm or establish anticoagulation safety.')])
    change(7,43,'Infective endocarditis-associated immune phenomena',[
      ('Primary AAV as proven by ANCA positivity','Endocarditis can produce ANCA and glomerular immune injury; infection must be excluded.'),
      ('A simple drug rash as the whole explanation','This does not explain fever, murmur, complement consumption and GN.'),
      ('Isolated noninflammatory valve degeneration','This does not explain the systemic febrile immune-complex syndrome.')])
    change(8,7,'Macrophage activation syndrome',[
      ('An uncomplicated Still flare','Falling counts/fibrinogen and progressive organ injury suggest MAS rather than an ordinary flare.'),
      ('Isolated methotrexate marrow toxicity','This can cause cytopenias but does not best unify the rapidly evolving ferritin/coagulation/hepatic pattern.'),
      ('Autoimmune hemolytic anemia alone','This does not explain the complete coagulopathic multiorgan deterioration.')])
    change(8,11,'Hemophagocytic lymphohistiocytosis',[
      ('Sepsis without associated hyperinflammatory syndrome','Sepsis is a major differential and may coexist, but the whole pattern requires active HLH assessment.'),
      ('Acute leukemia as the only explanation before further assessment','Malignancy may trigger HLH, so marrow investigation does not replace syndrome recognition.'),
      ('Isolated acute viral hepatitis','This can raise ferritin, but does not best explain the full splenic/cytopenic/coagulopathic syndrome.')])
    change(9,3,'EBUS-guided thoracic nodal sampling',[
      ('Mediastinoscopy as the routine first step','EBUS is generally favored as the less invasive initial thoracic node approach when tissue is required.'),
      ('Surgical lung biopsy as the routine first step','This usually adds unnecessary invasiveness when informative nodes are accessible.'),
      ('Unguided endomyocardial biopsy','This is not the first tissue target for this thoracic nodal presentation.')])
    change(9,10,'Sarcoidosis-associated pulmonary hypertension',[
      ('Progressive pulmonary fibrosis alone','Fibrosis is a differential, but the disproportionate symptoms and syncope require vascular assessment.'),
      ('Airway obstruction alone','This may contribute to dyspnea but does not best explain the disproportionate DLCO/syncope pattern.'),
      ('Deconditioning as the complete diagnosis without testing','This should not be assumed in the presence of pulmonary vascular warning findings.')])
    change(9,16,'Uveitis',[
      ('Dry-eye-related superficial irritation alone','This does not encompass the deeper inflammatory visual threat of uveitis.'),
      ('Steroid-induced cataract as the direct granulomatous lesion','Cataract can be treatment-related but is not the direct inflammatory lesion asked about.'),
      ('Refractive presbyopia','This is age-related optical change rather than sarcoid inflammation.')])
    change(9,17,'Cardiac sarcoidosis',[
      ('Vasovagal syncope','New high-grade AV block is not explained by an uncomplicated vasovagal event.'),
      ('Medication-related AV block as established without exposure review','This is a differential, but sarcoidosis makes myocardial involvement a major urgent concern.'),
      ('Degenerative conduction disease as certain at age 46','It is possible but should not close the assessment for an inflammatory cardiac cause.')])
    change(9,23,'Methotrexate',[
      ('Hydroxychloroquine','It has selected skin/calcium roles but is not an equivalent preferred pulmonary steroid-sparing drug.'),
      ('Etanercept','It does not have the same effective sarcoid treatment evidence as the relevant conventional or monoclonal TNF strategies.'),
      ('Colchicine','It is not an equivalent pulmonary disease-modifying strategy.')])
    change(10,6,'Terminal complement pathway deficiency',[
      ('Early classical pathway deficiency such as C2','This usually lowers CH50 with preserved AH50.'),
      ('Alternative pathway factor B deficiency','This usually lowers AH50 with preserved CH50.'),
      ('Properdin deficiency','This is an alternative-pathway defect and does not usually abolish classical functional activity in the same pattern.')])
    change(10,11,'Neutrophil dihydrorhodamine oxidative-burst assay',[
      ('Neutrophil CD18 flow cytometry','This assesses an adhesion defect rather than the suspected oxidative killing defect.'),
      ('CH50 and AH50','These assess complement function rather than oxidative burst.'),
      ('Quantitative immunoglobulins and vaccine response','These assess antibody deficiency, not the defining CGD defect.')])
    change(10,19,'G6PD assessment',[
      ('TPMT activity alone','This is relevant to thiopurine metabolism, not the key dapsone oxidant-toxicity screen.'),
      ('HLA-B*58:01 typing alone','This is an allopurinol hypersensitivity association.'),
      ('NUDT15 genotyping alone','This helps thiopurine dosing, not the defining dapsone safety assessment.')])
    change(10,20,'A pre-existing demyelinating disorder such as multiple sclerosis',[
      ('A remote uncomplicated Bell palsy','This is not the same TNF-associated central demyelinating concern.'),
      ('Stable length-dependent diabetic neuropathy','This is a different neurological mechanism and not the defining class warning.'),
      ('Migraine without focal neurological deficit','This does not carry the same demyelination-related treatment concern.')])
    change(10,21,'Histoplasma capsulatum',[
      ('Aspergillus fumigatus','It is an opportunistic mold differential, but Histoplasma is a classic endemic granulomatous concern in this TNF/exposure setting.'),
      ('Candida albicans','This can cause invasive disease in selected settings but is not the characteristic endemic fungal exposure association.'),
      ('Pneumocystis jirovecii','It is another immunocompromised-host pulmonary pathogen but does not best match the endemic disseminated granulomatous clue.')])
    change(10,22,'Mucocutaneous Candida infection',[
      ('Recurrent meningococcal disease from terminal complement impairment','This is the classic susceptibility of a different pathway.'),
      ('Enteroviral disease from profound antibody deficiency','This is more characteristic of humoral immune failure.'),
      ('Disseminated histoplasmosis from granuloma impairment','This is a particularly important TNF-blockade association rather than the defining IL-17 mucosal defense pattern.')])
    change(10,24,'Herpes zoster',[
      ('Primary measles as the principal latent-virus reactivation','Measles is not the characteristic latent reactivation risk.'),
      ('HPV warts as the sole principal vaccine-preventable reactivation issue','HPV prevention matters in broader care, but zoster is the characteristic JAK-associated concern asked about.'),
      ('Hepatitis A reactivation','Hepatitis A does not establish the chronic latent infection pattern assumed here.')])
    for order,bank in banks.items():
        finalize('Rheumatology',order,bank['headingText'],bank['questions'][0]['id'].rsplit('-',1)[0],bank['questions'],bank['targetQuestions'])
    (ROOT/'rheumatology-option-review.json').write_text(json.dumps(dict(revisedQuestions=len(edits),edits=edits,independentClinicalReview=False),indent=2),encoding='utf-8')
    print(json.dumps(dict(revisedQuestions=len(edits),questions=328)))

if __name__=='__main__':review()
