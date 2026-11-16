"""Compact four transferred explanations with hash-audited preservation of questions."""
import copy
import json
from html import escape
from revise_cardiology_12_transferred import BANK, AUDIT, digest
from qbank_json_chapters import rich, validate

EDITS = {
 'cardiology-rebuild-01-015': [
  ('Calculation', ['**Fick shunt ratio:** Qp/Qs = (systemic arterial − mixed venous O₂ content)/(pulmonary venous − pulmonary arterial O₂ content).', '**Substitution:** (98 − 68)/(98 − 83) = 30/15 = **2.0**. Pulmonary flow is twice systemic flow.']),
  ('Interpretation and Limitations', ['**Saturation substitution** assumes comparable hemoglobin and negligible dissolved oxygen; high inspired oxygen can invalidate this shortcut.', '**Sampling** requires steady physiology and representative mixed venous blood; incomplete mixing or anomalous venous return can distort the result.', '**Closure assessment** combines shunt size, chamber enlargement, anatomy and PVR. Qp/Qs ≥1.5 supports significance but does not independently establish operability.'])],
 'cardiology-rebuild-01-048': [
  ('What CMR Measures', ['**Phase-contrast flow** quantifies pulmonary and systemic forward flow to calculate Qp/Qs.', '**Volumetric imaging** measures RV size and systolic function without geometric assumptions; anatomical sequences map pulmonary venous connections.']),
  ('Selecting and Interpreting Tests', ['**Technical checks:** measurement planes, velocity encoding, arrhythmia, regurgitation and collateral flow can alter flow estimates.', '**Echocardiography** assesses valves and shunt anatomy; TEE better defines septal rims when device closure is considered.', '**Catheterization** measures pressures and calculates PVR when pulmonary vascular disease or uncertain operability requires invasive clarification. CMR flow alone cannot supply these pressures.'])],
 'cardiology-rebuild-03-047': [
  ('Severity and Anatomy', ['**Severe valvar pulmonary stenosis:** peak velocity >4 m/s or maximum instantaneous Doppler gradient >64 mmHg; mild <3 m/s, moderate 3–4 m/s.', '**This patient:** 4 × 4.5² = 81 mmHg. Doppler instantaneous and catheter peak-to-peak gradients are not interchangeable.', '**Mobile doming leaflets** and a normal annulus favor balloon commissurotomy. Dysplastic valves, including those associated with Noonan syndrome, respond less predictably.']),
  ('Treatment and Follow-up', ['**Balloon valvuloplasty** is preferred for symptomatic moderate/severe valvar obstruction with favorable anatomy in the 2025 ACHD framework.', '**Surgery** suits unsuitable anatomy, substantial regurgitation or failed balloon treatment; choose repair versus replacement individually.', '**Follow-up:** residual gradient, pulmonary regurgitation, RV size/function and exercise response.', '**A pulmonary ejection click** may soften or merge with S1 on inspiration; distinguish this from the murmur.'])],
 'cardiology-rebuild-03-048': [
  ('2025 Pulmonary Valve Replacement Framework', ['**Asymptomatic repaired TOF:** moderate or greater pulmonary valve dysfunction plus at least two adverse markers supports replacement assessment.', '**Qualifying markers:** RVESVi >80 mL/m²; RVEDV ≥2 × LVEDV; RVEF ≤46%; LVEF ≤50%; progressive objective exercise decline.', '**This patient has three:** RVESVi 92 mL/m², RVEF 43% and declining exercise performance. Reported absence of symptoms does not negate objective deterioration.']),
  ('Valve-team Assessment', ['**Define anatomy** and associated lesions; choose surgical or transcatheter replacement according to RVOT suitability and coronary relationships.', '**Assess arrhythmia risk alongside valve planning.** Replacement improves hemodynamics but does not eliminate scar-related ventricular tachycardia.', '**Continue surveillance** of ventricular function, residual valve dysfunction, exercise capacity and rhythm after intervention.'])],
}

def main():
 bank=json.loads(BANK.read_text(encoding='utf-8'))
 audit=json.loads(AUDIT.read_text(encoding='utf-8'))
 for q in bank['questions']:
  if q['id'] not in EDITS or q.get('explanationStyle')=='concise_structured':continue
  old=copy.deepcopy(q)
  if callable(globals().get('EDIT_HOOK')):EDIT_HOOK(q)
  d=q['explanationTeaching']; sections=[]
  html=['<h2>'+escape(d['title'])+'</h2>']; plain=[d['title']]
  answer='Correct answer: '+q['options'][q['correctIndex']]
  html.append('<p><strong>'+escape(answer)+'</strong></p>');plain.append(answer)
  for heading,lines in EDITS[q['id']]:
   sections.append(dict(heading=heading,bullets=[dict(text=s,children=[]) for s in lines]))
   html.append('<h3>'+escape(heading)+'</h3><ul>'+''.join('<li>'+rich(s)+'</li>' for s in lines)+'</ul>')
   plain.extend([heading,*lines])
  # Retain existing comparison tables and individual distractor reasoning.
  for t in d.get('tables',[]):
   html.append('<div class="table-wrap"><table><thead><tr>'+''.join('<th>'+rich(x)+'</th>' for x in t['headers'])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+rich(x)+'</td>' for x in row)+'</tr>' for row in t['rows'])+'</tbody></table></div>')
   plain.extend([' | '.join(t['headers']),*[' | '.join(row) for row in t['rows']]])
  if not q.get('calculation'):
   html.append('<h3>Other Options</h3><ul>')
   for a in d['otherOptions']:
    s=q['options'][a['optionIndex']]+': '+a['explanation'];plain.append(s)
    html.append('<li>'+rich(s)+'</li>')
   html.append('</ul>')
  html.append('<h3>References</h3><ul>')
  for r in q['references']:
   html.append('<li><a href="'+escape(r['url'],quote=True)+'">'+escape(r['label'])+'</a></li>')
   plain.append(r['label']+' — '+r['url'])
  html.append('</ul>');d['sections']=sections
  q.update(explanation='\n\n'.join(plain),explanationHtml=''.join(html),explanationStyle='concise_structured')
  record=next((r for r in audit['revisions'] if r['questionId']==q['id']),None)
  if record is None:
   record=dict(questionId=q['id'],originalSha256=digest(old),changedFields=[],sources=[r['url'] for r in q['references']],status='author_source_checked',independentClinicianReview=False)
   audit['revisions'].append(record)
  record.update(revisedSha256=digest(q),reviewedAt='2026-11-16',reason=record.get('reason','')+' Condensed teaching into structured bullets; stem, options, key and references preserved.')
  record['changedFields']=sorted(set(record['changedFields'])|{k for k in q if q.get(k)!=old.get(k)})
 report=validate(bank)
 BANK.write_text(json.dumps(bank,ensure_ascii=False,indent=2),encoding='utf-8')
 AUDIT.write_text(json.dumps(audit,ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps(report))

if __name__=='__main__':main()
