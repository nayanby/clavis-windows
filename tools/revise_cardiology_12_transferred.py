"""Audited editorial revisions to two transferred questions; no runtime writes."""
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / 'Qbank Rebuild' / 'Cardiology'
BANK = ROOT / '12. Adult Congenital Heart Diseases.json'
AUDIT = ROOT / 'audit' / 'reviewed-question-revisions.json'
SOURCE = 'https://doi.org/10.1161/CIR.0000000000001402'


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def replace_strings(value, replacements):
    if isinstance(value, str):
        for old, new in replacements.items():
            value = value.replace(old, new)
        return value
    if isinstance(value, list):
        return [replace_strings(v, replacements) for v in value]
    if isinstance(value, dict):
        return {k: replace_strings(v, replacements) for k, v in value.items()}
    return value


REVISIONS = {
    'cardiology-rebuild-03-047': {
        'The valve is suitable for balloon treatment, with no important pulmonary regurgitation or subvalvular obstruction.':
            'The leaflets are thin and mobile, the annulus is normal-sized, and there is no important pulmonary regurgitation or subvalvular obstruction.',
        'Surveillance until severe RV systolic failure develops':
            'Transcatheter pulmonary valve replacement',
        'Symptoms and severe valvular obstruction already support intervention; waiting for advanced ventricular damage is not a necessary prerequisite.':
            'Transcatheter replacement is valuable for selected dysfunctional conduits, bioprostheses and repaired RV outflow tracts. This patient has a native, mobile doming valve that can be opened by balloon commissurotomy; implanting a prosthesis is not the preferred initial treatment.',
    },
    'cardiology-rebuild-03-048': {
        'Defer referral until RVEF falls below thirty-five percent':
            'Repeat CMR and exercise testing in twelve months',
        'Continue surveillance until the patient reports exertional symptoms':
            'Trial heart-failure medication before reconsidering valve referral',
        'Defer referral until RV end-diastolic volume exceeds three times LV volume':
            'Complete electrophysiological risk stratification before valve referral',
        'Refer to an ACHD valve team to assess pulmonary valve replacement despite absent reported symptoms':
            'Assess pulmonary valve replacement through the ACHD valve team',
        'The specified 2025 marker is RVEF at or below 46% as part of the combined framework; waiting for a conventional advanced dysfunction boundary overlooks the existing adverse findings.':
            'Serial imaging and exercise testing are appropriate when findings remain stable and intervention criteria are not met. Here RVESVi 92 mL/m², RVEF 43% and progressive exercise decline already provide three qualifying markers; another annual observation interval should not replace referral now.',
        'Symptom-only surveillance can overlook reduced self-selected activity; objective decline and the supplied RV markers already support replacement assessment in the named repaired-tetralogy framework.':
            'Medication may be needed for coexisting ventricular failure or congestion. It does not correct pulmonary regurgitation, and a mandatory drug trial is not part of the specified valve-replacement pathway. The supplied structural and functional findings warrant valve assessment without that prerequisite.',
        'The named criterion is RV end-diastolic volume at least twice LV volume, not three times; moreover, the other qualifying markers already support assessment without requiring every listed criterion.':
            'Electrophysiological assessment can guide VT ablation and sudden-death prevention in selected repaired-TOF patients and may be coordinated with valve planning. It is not a prerequisite to referring a patient who already meets the hemodynamic replacement framework; electrical and valve evaluation can proceed together.',
    },
}


if __name__ == '__main__':
    bank = json.loads(BANK.read_text(encoding='utf-8'))
    audit = json.loads(AUDIT.read_text(encoding='utf-8'))
    known = {r['questionId']: r for r in audit['revisions']}
    for i, question in enumerate(bank['questions']):
        qid = question['id']
        if qid not in REVISIONS:
            continue
        if qid in known:
            assert digest(question) == known[qid]['revisedSha256']
            continue
        original = copy.deepcopy(question)
        for old in REVISIONS[qid]:
            assert old in json.dumps(original, ensure_ascii=False), (qid, old)
        revised = replace_strings(question, REVISIONS[qid])
        revised['sourceCheckedAt'] = '2026-11-16'
        assert revised['id'] == original['id']
        assert revised['correctIndex'] == original['correctIndex']
        assert revised['topic'] == original['topic']
        bank['questions'][i] = revised
        audit['revisions'].append(dict(
            questionId=qid, status='author_source_checked', reviewedAt='2026-11-16',
            reason='Replace giveaway waiting strategies with competing procedures or assessment sequences, retaining the independently rechecked 2025 guideline answer.',
            originalSha256=digest(original), revisedSha256=digest(revised),
            changedFields=sorted(k for k in revised if revised[k] != original[k]),
            sources=[SOURCE], independentClinicianReview=False))
    for i, question in enumerate(bank['questions']):
        if question['id'] != 'cardiology-rebuild-03-047':
            continue
        old = 'Dysplastic valves, unsuitable anatomy, important regurgitation or failure of catheter treatment can shift the plan toward surgery.'
        if 'Noonan syndrome' in question['explanation']:
            continue
        addition = ' Dysplastic pulmonary valves are associated with Noonan syndrome and may respond less well to balloon dilation than a thin doming valve. A mobile valvar pulmonary ejection click characteristically softens or merges with S1 during inspiration; the murmur and click are distinct sounds, and this finding is not a substitute for Doppler grading.'
        revised = replace_strings(question, {old: old + addition})
        ref = dict(label='Clinical Methods: Ejection Clicks', url='https://www.ncbi.nlm.nih.gov/books/NBK347/')
        revised['references'].append(ref)
        revised['explanation'] += '\n\n' + ref['label'] + ' — ' + ref['url']
        revised['explanationHtml'] = revised['explanationHtml'][:-5] + '<li><a href="' + ref['url'] + '">' + ref['label'] + '</a></li></ul>'
        record = next(r for r in audit['revisions'] if r['questionId'] == question['id'])
        record['revisedSha256'] = digest(revised)
        record['changedFields'] = sorted(set(record['changedFields']) | {'references'})
        record['sources'].append(ref['url'])
        record['reason'] += ' Added Noonan-associated dysplasia and respiratory behavior of a pulmonary ejection click.'
        bank['questions'][i] = revised
    from qbank_json_chapters import validate
    print(json.dumps(validate(bank), indent=2))
    BANK.write_text(json.dumps(bank, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    AUDIT.write_text(json.dumps(audit, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
