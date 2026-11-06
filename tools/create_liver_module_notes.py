from clinical_note_authoring import *
HB=('AASLD/IDSA chronic HBV treatment guideline update, 2025','https://www.idsociety.org/practice-guideline/hepatitis-b/hepatitis-b/')
HCV=('AASLD/IDSA HCV guidance','https://www.hcvguidelines.org/guidance/patients-with-decompensated-cirrhosis/')
HRS=('ADQI/ICA cirrhosis-associated AKI consensus, 2024','https://pmc.ncbi.nlm.nih.gov/articles/11193657/')
HCC=('AASLD HCC practice guidance and critical updates','https://www.aasld.org/practice-guidelines/management-hepatocellular-carcinoma')
BAV=('Baveno VII portal hypertension consensus','https://doi.org/10.1016/j.jhep.2021.12.022')
AIH=('EASL autoimmune hepatitis guideline, 2025','https://easl.eu/news/easl-cpgs-autoimmune-hepatitis-2025/')

def hepatitis():
 write('Liver','Liver Diseases Hepatitis',[
 S('Interpret liver tests by pattern',T('Pattern|Key distinction','''Hepatocellular|ALT/AST predominant; R ratio ≥5 supports this pattern
 Cholestatic|ALP predominant; R ratio ≤2 supports this pattern; confirm hepatic origin when uncertain
 Mixed|R ratio >2 and <5
 R ratio|(ALT / ALT upper limit) divided by (ALP / ALP upper limit)
 Synthetic dysfunction|INR and albumin, interpreted with vitamin K status, anticoagulants, nutrition and time course''')+U('''Aminotransferases measure injury, not remaining liver function. Falling enzymes with worsening INR/encephalopathy can indicate deterioration.
 Isolated unconjugated bilirubin: consider hemolysis or Gilbert syndrome; cholestasis usually raises conjugated bilirubin.
 AST:ALT ratio alone does not establish alcohol-associated disease.''')),
 S('Viral hepatitis: compare together',T('Virus|Transmission / diagnosis|Important course','''HAV|Fecal–oral; IgM anti-HAV for acute infection|No chronic infection
 HBV|Blood/sexual/perinatal; HBsAg, anti-HBc, anti-HBs and HBV DNA|Can become chronic; immunosuppression can reactivate infection
 HCV|Blood-borne; antibody followed by RNA for active infection|Antibody can persist after cure; reinfection remains possible
 HDV|Requires HBsAg; anti-HDV then appropriate RNA confirmation|Coinfection/superinfection can cause severe disease
 HEV|Usually fecal–oral/zoonotic depending on setting|Severe pregnancy disease in relevant regions; chronic infection possible with immunosuppression''')+U('''Treat chronic HCV with an appropriate direct-acting antiviral regimen; assess cirrhosis, interactions, prior treatment and HBV reactivation risk.
 Avoid HCV protease-inhibitor regimens in decompensated cirrhosis. Cure does not eliminate HCC surveillance needs in cirrhosis.''')),
 S('Autoimmune, metabolic and drug-related hepatitis',T('Disease|Diagnosis clue|Treatment principle','''Autoimmune hepatitis|IgG, autoantibodies and compatible biopsy; exclude alternatives|Corticosteroid-based induction and appropriate steroid-sparing therapy; not antibody positivity alone
 MASLD/MASH|Steatosis with metabolic risk; fibrosis determines prognosis|Weight/metabolic treatment and fibrosis assessment; selected approved liver-directed treatment in eligible disease
 Alcohol-associated hepatitis|Recent jaundice in compatible exposure; exclude infection/obstruction and mimics|Abstinence, nutrition; selected corticosteroid treatment for severe disease with response reassessment
 Wilson disease|Young patient, hepatic/neuro disease or hemolysis|Copper-focused testing; normal ceruloplasmin does not exclude every case
 Hemochromatosis|Transferrin saturation/ferritin and appropriate genetic assessment|Confirm iron overload; ferritin alone is nonspecific
 Drug-induced liver injury|Temporal drug/supplement exposure; hepatocellular/cholestatic/mixed patterns|Stop suspected agent, assess severity and exclude competing causes''')+U('''Severe alcohol-associated hepatitis: assess contraindications and infection before steroids; use Lille response assessment to avoid continuing ineffective treatment.
 AIH treatment withdrawal requires sustained biochemical control and a specialist plan. Do not use budesonide as a routine substitute in cirrhosis.
 FIB-4 and elastography help stratify fibrosis; acute inflammation and other factors can alter measurements.'''))],[HB,HCV,AIH,('EASL–EASD–EASO MASLD guideline, 2024','https://easlcampus.eu/sites/default/files/2024-06/EASL_CPGs_on_MASLD.pdf')])

def hbv():
 write('Liver','Hepatitis B Advanced',[
 S('Serology: read the full pattern',T('Pattern|Interpretation','''HBsAg positive|Current infection; persistence ≥6 months supports chronic HBV
 IgM anti-HBc positive|Usually recent infection; can also occur in severe reactivation/flare
 HBsAg negative, anti-HBc positive, anti-HBs positive|Past infection; reactivation risk remains with selected immunosuppression
 Anti-HBs alone|Usually vaccination-related immunity
 Isolated anti-HBc|Past infection with waned anti-HBs, occult infection, window phase or false-positive result; clarify by context
 HBV DNA|Replication measurement; HBeAg-negative disease can still replicate actively''')),
 S('Treatment selection',T('Drug / strategy|Strength|Main limitation','''Tenofovir disoproxil|Potent, high resistance barrier; important pregnancy/perinatal role|Renal/bone monitoring
 Tenofovir alafenamide|Potent with different renal/bone exposure profile|Eligibility depends on disease stage, renal status and local labeling
 Entecavir|Potent oral high-barrier option in suitable patients|Renal dosing; prior lamivudine resistance and HIV status matter
 Pegylated interferon|Finite course in selected compensated patients|Avoid in decompensated cirrhosis and pregnancy; systemic adverse effects''')+U('''Treatment decisions use fibrosis/cirrhosis, HBV DNA, ALT, age, coinfection, family history, extrahepatic disease and transmission risk. Updated 2025 guidance broadens some treatment discussions; one historical DNA/ALT cutoff does not fit every patient.
 Decompensated HBV requires prompt potent antiviral treatment and transplant assessment.
 Viral suppression reduces progression and transmission but does not reliably eliminate cccDNA or abolish HCC risk.''')),
 S('Reactivation and transmission prevention',U('''Before immunosuppression: HBsAg, total anti-HBc and anti-HBs. HBsAg-negative/anti-HBc-positive patients can reactivate, especially with anti-CD20 treatment or transplantation.
 High-risk exposure: prophylactic high-barrier antiviral and continued post-treatment monitoring/duration according to regimen and guideline.
 Pregnancy with high HBV DNA: maternal antiviral prophylaxis in the indicated window plus timely neonatal vaccination and HBIG where indicated; maternal treatment does not replace infant prevention.
 Test for HIV, HCV and HDV as appropriate. Entecavir or tenofovir strategy must account for HIV treatment rather than use inadvertent inadequate HIV monotherapy.
 Do not stop nucleos(t)ide therapy casually: rebound, severe flare and decompensation can occur. Stopping criteria are selective and monitoring-intensive.''')),
 S('Long-term review',U('''Track HBV DNA, ALT, adherence, renal/bone issues and fibrosis/cirrhosis status.
 HCC surveillance remains indicated in cirrhosis and other defined high-risk HBV groups even with viral suppression.
 Persistent low-level DNA, resistance and nonadherence are different problems; confirm adherence and drug history before changing therapy.
 HBeAg seroconversion is not the same as HBsAg loss or complete elimination of infection.'''))],[HB,('EASL HBV guideline, 2025','https://www.hepb.org/assets/Uploads/EASL-guidelines-May-2025.pdf')])

def cirrhosis():
 write('Liver','Cirrhosis',[
 S('Portal hypertension and ascites',T('Finding / test|Interpretation','''Decompensation|Ascites, variceal bleeding or overt encephalopathy mark major disease progression
 SAAG|Serum albumin − ascitic albumin; ≥1.1 g/dL supports portal hypertension
 Ascitic protein|High SAAG with higher protein raises cardiac/outflow causes; interpret full pattern
 New/worsening ascites or hospitalized decompensation|Diagnostic paracentesis when indicated; do not omit infection assessment
 Ascitic PMN ≥250/mm³|Treat spontaneous bacterial peritonitis in an appropriate setting; culture negativity does not exclude''')+U('''Ascites: sodium management, appropriate spironolactone/loop diuretic balance; monitor renal function and electrolytes.
 Large-volume paracentesis: albumin replacement according to volume and risk; assess refractory ascites for TIPS/transplant suitability.
 SBP: prompt appropriate antibiotics, selected albumin and secondary prevention; suspect secondary peritonitis with atypical findings or poor response.''')),
 S('Varices and bleeding',U('''Clinically significant portal hypertension: nonselective beta blocker, often carvedilol in eligible compensated patients, can prevent decompensation; BP and tolerance matter.
 Acute suspected variceal bleeding: resuscitate, start vasoactive therapy and antibiotic prophylaxis, then urgent endoscopic treatment after stabilization.
 Secondary prophylaxis usually combines nonselective beta blockade and band ligation. Selected high-risk acute bleeds require early/pre-emptive TIPS; uncontrolled bleeding needs rescue strategies.
 Do not lower portal pressure with beta blockade at the expense of severe hypotension or HRS-AKI; adjust treatment in unstable decompensation.''')),
 S('Encephalopathy and kidney injury',T('Problem|Key management','''Hepatic encephalopathy|Find precipitant: infection, bleeding, constipation, sedatives, dehydration/electrolytes; lactulose, with rifaximin for appropriate recurrent disease
 Ammonia level|Does not independently diagnose or grade encephalopathy; assess alternative neurological causes
 AKI in cirrhosis|Assess hypovolemia, infection, tubular injury, obstruction and HRS; these can overlap
 HRS-AKI|No mandatory 48-hour albumin trial for every patient under 2024 ADQI/ICA criteria; volume assessment and response to indicated resuscitation matter
 HRS treatment|Vasoconstrictor plus individualized albumin in suitable patients; monitor oxygenation/overload and ischemia; transplant is definitive liver-directed treatment''')),
 S('Prognosis and routine care',U('''MELD-based scores and Child–Pugh describe different aspects of risk; allocation uses current local policy, not an interchangeable historical formula.
 HCC surveillance, vaccinations, nutrition/sarcopenia care, alcohol abstinence and cause-specific treatment remain necessary.
 Avoid routine protein restriction for encephalopathy. Avoid NSAIDs and unnecessary nephrotoxic/sedative drugs.
 INR elevation does not mean the patient is naturally anticoagulated; assess VTE and bleeding risk separately.
 Recurrent decompensation, HRS, refractory ascites or appropriate prognostic severity should prompt transplant evaluation.'''))],[BAV,HRS,HCC])

def biliary():
 write('Liver','Biliary',[
 S('Gallstone disease: localize the complication',T('Condition|Clues|Management','''Biliary colic|Episodic pain without sustained inflammation|Elective definitive management when indicated
 Acute cholecystitis|Persistent RUQ pain, tenderness and inflammatory findings|Antibiotics/source assessment; early cholecystectomy in suitable patients
 Choledocholithiasis|Duct stone/obstruction; may cause cholestasis|MRCP/EUS for appropriate intermediate-risk diagnosis; ERCP for therapeutic clearance
 Acute cholangitis|Infected obstructed biliary tree; fever/jaundice may be incomplete|Antibiotics, resuscitation and severity-dependent timely drainage
 Gallstone pancreatitis|Pancreatic inflammation|Urgent ERCP for cholangitis; not routine for all uncomplicated cases''')),
 S('PBC, PSC and IgG4 disease',T('Feature|PBC|PSC','''Main site|Small intrahepatic ducts|Intra/extrahepatic ducts; small-duct variant exists
 Typical test|Cholestasis + AMA or PBC-specific antibodies|MRCP stricturing pattern; assess relevant strictures
 Associations|Other autoimmune disease|IBD; cholangiocarcinoma/gallbladder and colorectal cancer risk
 Treatment|UDCA first-line; selected additional current therapies for inadequate response|Treat complications/strictures and assess transplant indications; no universal curative drug
 Biopsy|Selected uncertain/overlap cases|Needed in selected small-duct or overlap presentations''')+U('''Pruritus severity is not proportional to bilirubin. Use stepwise symptom treatment and assess bone/fat-soluble-vitamin issues when indicated.
 Obeticholic acid was withdrawn from the US PBC market in 2025; do not present it as a universal current second-line standard. Newer options and local approvals require current guidance.
 IgG4-related cholangitis can mimic PSC or cancer; integrate pancreas/other organs, serology, imaging and tissue. IgG4 elevation alone is not diagnostic.''')),
 S('Strictures and malignancy',U('''A new relevant stricture in PSC requires assessment for cholangiocarcinoma; CA19-9 can rise with cholangitis and does not prove cancer.
 MRCP maps ducts noninvasively; ERCP provides drainage and selected sampling but carries pancreatitis/infection risk.
 Painless progressive jaundice, weight loss or a suspicious hilar/distal lesion needs malignancy evaluation.
 A negative brush cytology result does not reliably exclude every biliary malignancy.
 Secondary sclerosing causes include ischemic, infectious and procedural injury; not every beaded duct is primary PSC.'''))],[('AASLD PSC/cholangiocarcinoma guidance','https://www.aasld.org/practice-guidelines/primary-sclerosing-cholangitis-and-cholangiocarcinoma'),('AASLD PBC medication guideline announcement, 2026','https://www.aasld.org/aasld-and-aga-offer-first-medication-focused-guideline-treating-pbc'),('NICE gallstone disease guideline','https://www.nice.org.uk/guidance/cg188/chapter/Recommendations')])

def alf():
 write('Liver','Acute Liver Failure Transplantation',[
 S('Define the syndrome',T('Condition|Distinction','''Acute liver failure|Acute liver disease, usually <26 weeks, with INR ≥1.5 and encephalopathy in a patient without pre-existing cirrhosis
 Acute liver injury|Acute injury/coagulopathy without the defining encephalopathy
 Acute-on-chronic liver failure|Acute deterioration of chronic liver disease with organ failure; definitions differ across societies
 Prognosis|Etiology, encephalopathy, organ failure, lactate/INR and trajectory; no single enzyme level establishes recovery''')),
 S('Identify treatable causes immediately',T('Cause|Priority','''Acetaminophen|Prompt N-acetylcysteine when suspected; do not delay for a late low level if the clinical history suggests toxicity
 Viral hepatitis|Appropriate HAV/HBV/HEV and other testing; antiviral treatment in defined causes/settings
 Ischemic injury|Restore circulation and oxygen delivery; investigate shock/cardiac disease
 Autoimmune hepatitis|Urgent specialist assessment; immunosuppression in selected patients without delaying transplant decisions
 Wilson disease|Hemolysis and characteristic biochemical pattern may be clues; urgent transplant assessment
 Pregnancy-related disease|Obstetric/hepatology emergency; delivery and organ support when indicated
 Vascular/drug/toxin causes|Doppler/appropriate imaging; complete drug/supplement history and cause-specific treatment''')),
 S('ICU priorities',U('''Early transfer/discussion with a transplant centre; do not wait for advanced coma or all listing criteria.
 Protect the airway in advanced encephalopathy; prevent/treat hypoglycemia, infection, AKI, electrolyte abnormalities and circulatory failure.
 Cerebral edema risk: monitor neurological status, avoid hypoxemia/hypotension, and use specialist osmotic/renal support strategies when indicated.
 Do not routinely correct INR solely to normalize the number in a nonbleeding patient; this can obscure prognosis and add volume. Procedures/bleeding need individualized hemostatic care.
 N-acetylcysteine also has selected non-acetaminophen ALF roles, especially early presentations; it is not a substitute for transplant assessment.''')),
 S('Transplant selection and follow-up',U('''King’s College and other prognostic models support decisions but do not replace trajectory and specialist judgment; criteria differ for acetaminophen and non-acetaminophen causes.
 Assess contraindications, reversible organ injury, psychosocial factors and urgency through the transplant team.
 Post-transplant: rejection, infection, drug toxicity, vascular/biliary complications and recurrence of disease have different diagnostic pathways.
 Calcineurin inhibitors can cause renal/metabolic toxicity; drug levels and interactions matter. A rising liver test is not automatically rejection.
 Severe encephalopathy, rising lactate, progressive INR or multiorgan failure despite falling AST/ALT signals danger, not biochemical recovery.'''))],[('AASLD acute liver failure overview, 2025','https://www.aasld.org/liver-fellow-network/core-series/back-basics/defining-and-managing-acute-liver-failure'),('AASLD acute-on-chronic liver failure guidance','https://www.aasld.org/practice-guidelines/acute-chronic-liver-failure-and-management')])

def tumors():
 write('Liver','HCC Liver Tumors',[
 S('Surveillance and diagnosis',U('''Surveillance: cirrhosis and selected high-risk chronic HBV groups; ultrasound with AFP every 6 months under AASLD guidance, with alternative imaging strategies when ultrasound is inadequate.
 A suspicious lesion requires appropriate multiphasic CT/MRI. Validated imaging criteria can establish HCC without biopsy only in the appropriate at-risk population.
 Arterial enhancement alone is insufficient; size and the complete enhancement pattern matter. Indeterminate or non-HCC patterns need further evaluation.
 Normal AFP does not exclude HCC. An elevated AFP alone does not establish diagnosis.''')),
 S('Stage the tumor and the liver',T('Dimension|Why it matters','''Tumor burden|Size, number, vascular invasion and metastases determine available local/systemic options
 Liver reserve|Portal hypertension, bilirubin, decompensation and functional reserve constrain treatment
 Performance status|Affects expected benefit and tolerance
 Transplant criteria|Conventional Milan: single ≤5 cm or up to 3 each ≤3 cm, without macrovascular invasion/extrahepatic spread; accepted expansions/downstaging depend on policy''')),
 S('Treatment grouped by setting',T('Setting|Options / limitation','''Localized, preserved reserve|Resection or ablation in suitable anatomy; portal hypertension and remnant liver matter
 Early HCC with cirrhosis and transplant eligibility|Transplant treats tumor and liver disease; bridging/downstaging when appropriate
 Liver-confined unresectable disease|Selected transarterial/locoregional approaches; not suitable for every decompensated patient
 Advanced/unresectable disease|Current immunotherapy-based and targeted systemic options selected by liver reserve, bleeding risk and contraindications
 Anti-VEGF-containing treatment|Assess variceal/other bleeding risk before treatment''')+U('''Do not extrapolate one preferred regimen to every Child–Pugh class or transplant recipient.
 Tumor progression and liver decompensation can occur independently; monitor both.
 Post-treatment viable enhancing tumor matters; size change alone can misrepresent response after locoregional therapy.''')),
 S('Other focal liver lesions',T('Lesion|Typical distinction','''Hemangioma|Characteristic peripheral nodular enhancement with progressive fill-in; avoid unnecessary biopsy of a characteristic vascular lesion
 Focal nodular hyperplasia|Characteristic imaging; usually benign without routine resection
 Hepatocellular adenoma|Hormone/metabolic context; bleeding/malignant risk depends on size, sex and subtype
 Cholangiocarcinoma|Biliary malignancy; imaging/tissue and resectability pathway differs from HCC
 Metastases|Primary-tumor context; not every lesion in cirrhosis is HCC'''))],[HCC,('NCI liver cancer professional summary','https://www.cancer.gov/types/liver/hp/adult-liver-treatment-pdq')])

if __name__=='__main__':hepatitis();hbv();cirrhosis();biliary();alf();tumors()
