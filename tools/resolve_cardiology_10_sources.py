"""Reframe uncertain version-specific details using independently accessible sources."""
import json
from html import escape
from qbank_json_chapters import ROOT,rich,validate
from redistribute_cardiology_qbank import digest
p=ROOT/'Cardiology/10. Infective Endocarditis.json'
b=json.loads(p.read_text(encoding='utf-8'));assert b['status']!='installed_verified'
byid={q['id']:q for q in b['questions']}
changed=set()
def get(n):
 q=byid[f'cardiology-rebuild-10-{n:03}'];changed.add(q['id']);return q
def section(h,*lines):return dict(heading=h,bullets=[dict(text=t,children=c) for t,c in lines])
summary=dict(label='AHA official endocarditis statement summary, 2026',url='https://professional.heart.org/en/science-news/infective-endocarditis-diagnosis-antibiotic-therapy-and-management/top-things-to-know')
q=get(25)
q['question']='An adult has uncomplicated oral-streptococcal native-valve IE with amoxicillin MIC 1 mg/L and ceftriaxone MIC 0.25 mg/L. Renal toxicity is a concern and ceftriaxone is tolerated. Which strategy follows the SPILF–AEPEI position statement published in 2025?'
q['options'][0]='A full ceftriaxone course with gentamicin required by the amoxicillin result alone'
q['explanationTeaching']['title']='Drug-Specific MICs in Streptococcal Endocarditis'
q['explanationTeaching']['sections']=[
 section('SPILF–AEPEI Regimen Selection',('**Use the MIC of the beta-lactam selected for treatment.**',['Ceftriaxone MIC ≤0.5 mg/L supports monotherapy in this framework despite reduced amoxicillin susceptibility.']),('**Ceftriaxone 2 g IV daily for 4 weeks** for the supplied uncomplicated NVE.',['PVE requires 6 weeks; complications may change the plan.'])),
 section('Why the Framework Matters',('**This position differs from older routine aminoglycoside-combination rules.**',['Gentamicin toxicity should not be incurred solely because another beta-lactam has a higher MIC.']),('**Do not generalize to ceftriaxone-resistant isolates or a 2-week monotherapy course.**',['Assess both susceptibility results, allergy, cultures and anatomy.']))]
for o in q['explanationTeaching']['otherOptions']:
 if o['optionIndex']==0:o['explanation']='Some guideline regimens add gentamicin for reduced beta-lactam susceptibility. SPILF–AEPEI permits an adequate monotherapy course when the selected ceftriaxone itself is susceptible.'
q['references']=[dict(label='SPILF–AEPEI antibiotic therapy position statement, 2025',url='https://doi.org/10.1016/j.idnow.2024.105011')]
q=get(38)
q['question']='After valve surgery during bacterial IE treatment, valve culture is negative but tissue PCR remains positive for the previously identified organism. Blood cultures have cleared, source control is adequate and the patient is improving. Which interpretation best follows the AHA 2026 public summary and the biology of molecular testing?'
q['options']=['Stop antibiotics immediately because the infected valve has been removed','Restart a full course because any positive tissue PCR proves viable infection','Switch antibiotic class because residual tissue DNA proves resistance','Complete an individualized adequate course without restarting solely because tissue PCR is positive']
q['explanationTeaching']['title']='Postoperative Tissue PCR and Antibiotic Duration'
q['explanationTeaching']['sections']=[
 section('DNA Detection Is Not a Viability Test',('**Tissue PCR can remain positive after organisms are no longer viable.**',['Interpret it alongside blood cultures, histology, operative findings and clinical response.']),('**AHA’s public summary states that positive resected-valve tests alone do not alter postoperative duration.**',['Do not infer treatment failure or resistance solely from residual DNA.'])),
 section('Complete an Adequate Episode-Specific Course',('**Review effective treatment already received and residual infection.**',['Metastatic foci, abscess, pathogen and valve setting can require a different completion plan.']),('**Surgical source removal does not justify automatic cessation.**',['Document the treatment endpoint with the Endocarditis Team; a molecular result alone supplies neither a stopping rule nor a new full-course requirement.']))]
q['explanationTeaching']['otherOptions']=[
 dict(optionIndex=0,explanation='Excision provides source control, but the remaining systemic treatment depends on the episode; negative valve culture after antibiotics does not prove completion.'),
 dict(optionIndex=1,explanation='Persistent viable infection can justify prolonged treatment, but PCR detects DNA rather than proving viability; an isolated positive result cannot establish that indication.'),
 dict(optionIndex=2,explanation='A regimen change may be needed with demonstrated resistance or clinical failure; detection of the original organism’s DNA does not provide susceptibility evidence.')]
q['references']=[summary,dict(label='ESC endocarditis guideline, 2023',url='https://doi.org/10.1093/eurheartj/ehad193')]
q=get(37)
for s in q['explanationTeaching']['sections']:
 for line in s['bullets']:
  if 'AHA 2026 credits' in line['text']:
   line['text']='**AHA’s public 2026 summary does not extend postoperative duration solely for positive resected-valve tests.**'
   line['children']=['This differs from the named ESC positive-valve-culture rule; PCR positivity is not proof of viable infection.']
q['references'].append(summary)
# Preserve the gentamicin decision supported in the public summary; avoid treating
# inaccessible correction-dependent wording about rifampin consensus as verified.
q=get(29)
for s in q['explanationTeaching']['sections']:
 for line in s['bullets']:
  if 'AHA 2026 did not' in line['text']:
   line['text']='**AHA’s public 2026 summary advises against gentamicin in staphylococcal PVE.**'
   line['children']=['Rifampin is a separate decision; this stem specifically tests the published ESC timing approach.']
q['references'].append(summary)
q=get(30)
q['options'][0]='Gentamicin risks outweigh potential benefit; assess other adjuncts separately'
for s in q['explanationTeaching']['sections']:
 for line in s['bullets']:
  if 'No AHA writing-group consensus' in line['text']:
   line['text']='**Assess rifampin separately with the Endocarditis Team.**'
for o in q['explanationTeaching']['otherOptions']:
 if o['optionIndex']==3:o['explanation']='Avoiding gentamicin does not itself establish a mandatory replacement adjunct. Rifampin requires separate assessment of guideline framework, interactions, toxicity and the infection.'
q['references'].append(summary)
q=get(65)
for s in q['explanationTeaching']['sections']:
 for line in s['bullets']:
  if 'AHA 2026 also considers' in line['text']:
   line['text']='**Observational studies support considering colon evaluation in E. faecalis IE**, including cases with an identified source.'
   line['children']=['This association does not establish a universal screening mandate for every enterococcal bacteremia; individualize the evaluation.']
q['references']=[r for r in q['references'] if '0000000000001466' not in r['url']]
q['references'].append(dict(label='Multicenter observational study of colorectal disease in E. faecalis IE, 2020',url='https://pubmed.ncbi.nlm.nih.gov/31444092/'))
for qid in changed:
 q=byid[qid];d=q['explanationTeaching'];plain=[d['title'],'Correct answer: '+q['options'][q['correctIndex']]]
 q['references']=list({r['url']:r for r in q['references']}.values())
 html=['<h2>'+escape(d['title'])+'</h2><p><strong>'+escape(plain[1])+'</strong></p>']
 for s in d['sections']:
  html.append('<h3>'+escape(s['heading'])+'</h3><ul>');plain.append(s['heading'])
  for line in s['bullets']:
   html.append('<li>'+rich(line['text']));plain.append(line['text'])
   if line['children']:html.append('<ul>'+''.join('<li>'+rich(c)+'</li>' for c in line['children'])+'</ul>');plain.extend(line['children'])
   html.append('</li>')
  html.append('</ul>')
 assert not d.get('tables')
 html.append('<h3>Other Options</h3><ul>')
 for o in d['otherOptions']:
  t=q['options'][o['optionIndex']]+': '+o['explanation'];plain.append(t);html.append('<li>'+rich(t)+'</li>')
 html.append('</ul><h3>References</h3><ul>')
 for ref in q['references']:
  plain.append(ref['label']+' — '+ref['url']);html.append('<li><a href="'+escape(ref['url'],quote=True)+'">'+escape(ref['label'])+'</a></li>')
 html.append('</ul>');q['explanation']='\n\n'.join(plain);q['explanationHtml']=''.join(html)
# Keep device diagnosis and management together instead of starting with erosion.
transferred=byid['cardiology-rebuild-05-048']
b['questions']=[q for q in b['questions'] if q['id']!=transferred['id']]
at=next(i for i,q in enumerate(b['questions']) if q['id']=='cardiology-rebuild-10-058')
b['questions'].insert(at+1,transferred)
validate(b);p.write_text(json.dumps(b,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
audit=p.parent/'audit/reviewed-question-revisions.json'
d=json.loads(audit.read_text(encoding='utf-8'))
for r in d['revisions']:
 if r['questionId'] in changed:
  r['revisedSha256']=digest(byid[r['questionId']]);r['reason']+=' Reframed against accessible primary guidance; unsupported version-specific detail removed without changing the tested clinical domain.'
audit.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(reframedQuestions=sorted(changed),validation=validate(b))))
