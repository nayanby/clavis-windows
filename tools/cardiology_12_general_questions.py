"""General ACHD management with lesion-specific risk."""
from qbank_json_chapters import question as Q
REFERENCES={'PREGNANCY2025':('ESC cardiovascular disease and pregnancy guideline, 2025','https://doi.org/10.1093/eurheartj/ehaf193')}
def S(h,t,*details):return h,[(t,list(details))]
TOPIC='General adult congenital management'
rows=[Q(TOPIC,'Pregnancy Counseling in Eisenmenger Syndrome',
 'A 26-year-old with Eisenmenger syndrome from a large VSD is considering pregnancy. She is in functional class II on PAH treatment and has preserved LV ejection fraction. Which preconception recommendation best reflects her cardiovascular risk?',
 'Advise against pregnancy because of very high risk and arrange multidisciplinary counseling and reliable contraception',[
 ('Consider pregnancy acceptable with routine obstetric follow-up because LV ejection fraction is preserved','Preserved systemic LV function is reassuring in some congenital lesions but does not remove severe pulmonary vascular disease, right-heart risk or cyanotic physiology. This patient needs specialist counseling rather than routine follow-up alone.'),
 ('Delay conception until symptoms improve to functional class I, then classify the pregnancy as low risk','Functional improvement is desirable but does not establish reversal of Eisenmenger physiology. A symptom-class change alone cannot reclassify this pulmonary vascular disorder as a low-risk pregnancy condition.'),
 ('Offer preconception VSD closure to remove the pregnancy risk','Closure is appropriate for selected shunts before irreversible pulmonary vascular disease develops. Established Eisenmenger physiology makes defect closure hazardous; it cannot be offered as a simple method of converting the patient to a safe pregnancy phenotype.')],
 [S('Risk Is Determined by Physiology',
  '**Eisenmenger syndrome remains a very high-risk pregnancy condition despite modest symptoms or preserved LV systolic function.** Pregnancy-related circulatory changes can exceed the reserve of the pulmonary circulation and right ventricle.',
  'Systemic vasodilation may worsen right-to-left shunting, while changes in volume and flow can precipitate right-heart failure. Thromboembolism and paradoxical embolism add risk. Delivery and the postpartum period require particular attention; successful progression through early pregnancy does not establish safety.',
  'The mWHO 2.0 framework places pulmonary arterial hypertension in class IV. Current guidance emphasizes transparent counseling about maternal and fetal risks, respect for patient decisions and involvement of a Pregnancy Heart Team with congenital and pulmonary-hypertension expertise.'),
  S('Contraception and Medication Review',
  '**Discuss effective contraception before an unintended pregnancy occurs.** Choose the method with the patient after reviewing thrombotic risk, bleeding, drug interactions and procedural tolerance.',
  'Estrogen-containing contraception should be avoided in cyanotic ACHD because of thromboembolic risk. Long-acting options can be considered with specialist counseling; the insertion setting may need planning when hemodynamic reserve is limited.',
  'Review PAH drugs before conception. Endothelin receptor antagonists carry fetal risk, and some can reduce hormonal contraceptive effectiveness. Medication adjustment requires specialist oversight rather than abrupt withdrawal of essential treatment.'),
  S('If Pregnancy Occurs',
  '**Arrange prompt expert review and shared decision-making.** Discuss all management options, including termination where appropriate, without delaying care or assuming the patient has chosen an option.',
  'If pregnancy continues, coordinated maternal-fetal, ACHD, pulmonary-hypertension and anesthesia care is required throughout pregnancy and postpartum. The team should plan surveillance, treatment and delivery in an experienced center. The availability of intensive monitoring does not eliminate the underlying risk.')],
 ['ACHD2025','PREGNANCY2025','BOSENTAN_LABEL'])]
