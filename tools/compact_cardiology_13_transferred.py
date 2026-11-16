"""Review and compact transferred Chapter 13 items with original-ID/hash audit."""
import compact_cardiology_12_transferred as editor
editor.BANK=editor.BANK.with_name('13. Aortic Diseases and Peripheral Vascular Diseases.json')
editor.EDITS={
 'cardiology-rebuild-02-008':[
  ('Recognize Aortic Coronary Malperfusion',['**Dissection can involve a coronary ostium**, producing ischemic ECG changes or troponin elevation without primary plaque rupture.','**Abrupt maximal pain, pulse asymmetry and new AR** create a high-risk aortic presentation; ECG and chest radiography cannot exclude it.']),
  ('Select Definitive Imaging',['**Urgent CTA of the aorta** is preferred in most stable patients; ECG gating improves proximal-aortic assessment.','**Bedside TEE** is particularly useful when transfer is unsafe; MRI is generally less practical in the acute emergency.','**Resolve the aortic diagnosis before an indiscriminate ACS antithrombotic/fibrinolytic pathway.** Begin monitoring, analgesia and urgent aortic-team coordination.'])],
 'cardiology-rebuild-09-042':[
  ('Definitive Source Control',['**Type A dissection with tamponade requires emergency aortic repair.** Operative tamponade relief occurs with control of the bleeding source.','**Coordinate surgery, anesthesia, blood products and perfusion support.** A separate drainage procedure should not delay a ready aortic team.']),
  ('Rescue Drainage Is Different',['**Controlled minimal pericardial drainage** may bridge otherwise fatal tamponade when immediate surgery is unavailable.','**Remove only enough to restore essential perfusion**, often targeting approximately 90 mmHg systolic pressure in this rescue context.','**Complete decompression may accelerate bleeding.** A temporary pressure improvement neither repairs the aorta nor eliminates recurrent tamponade risk.'])],
 'cardiology-rebuild-03-017':[
  ('Concomitant Aortic Surgery',['**2025 ESC/EACTS:** when aortic valve surgery is indicated and surgical risk is low, consider root/ascending replacement at maximal diameter ≥45 mm.','**The 48 mm ascending aorta crosses that concomitant threshold.** This is not a universal threshold for isolated sporadic aortic surgery.']),
  ('Match the Operation to Anatomy',['**Measure root and tubular ascending aorta separately.** Ascending dilation alone does not prove root disease.','**Choose repair or replacement by segment, valve pathology and durability.** Suitable pliable cusps with root disease may permit valve-sparing surgery at an experienced center.','**Consider etiology, growth, body size and family history.** Continue aortic surveillance after valve or aortic surgery because untreated segments remain at risk.'])]}
def amend(q):
 if q['id']=='cardiology-rebuild-02-008':
  q['options'][0]='Immediate invasive coronary angiography'
  q['options'][1]='Serial high-sensitivity troponin measurements'
  q['options'][2]='D-dimer-based exclusion pathway'
 if q['id']=='cardiology-rebuild-03-017':
  q['options'][3]='Plan combined valve and root replacement'
editor.EDIT_HOOK=amend
if __name__=='__main__':editor.main()
