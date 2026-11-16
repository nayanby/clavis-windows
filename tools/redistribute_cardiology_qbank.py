"""Redistribute existing MCQs without changing question content or review status.

The numbered DOCX filenames are authoritative. The archived original banks make
this operation repeatable, including the uninstalled endocarditis/HTN drafts.
"""
import argparse
import collections
import copy
import hashlib
import json
from pathlib import Path
import sys
import time
import zipfile

from qbank_json_chapters import DATA, REPO, validate

ROOT = REPO / 'Qbank Rebuild'
DEST = ROOT / 'Cardiology'
AUDIT = DEST / 'audit'
ARCHIVE = AUDIT / 'pre-redistribution.zip'

# Original chapter -> destination -> original question numbers. All remaining
# questions retain their disease chapter. No MCQ is copied into two chapters.
MOVES = {
    1: {12: [15, 48], 14: [19]},
    2: {13: [8], 14: list(range(9, 17)),
        15: [20, 21, 28, *range(33, 44), 54, 56, 57, 60, 62, 63, 66]},
    3: {12: [47, 48], 13: [17],
        15: [10, 26, 37, 38, *range(50, 56)]},
    4: {15: [10, 11, 12, 13, 14, 16, 17, 18, 20, 21, 22, 23, 24,
              25, 28, 29, 30, 31, 46, 50, 58, 60, 61, 62]},
    5: {14: [3, *range(12, 19), 21, 22], 15: [28, 30, 34],
        10: [48]},
    6: {14: [*range(1, 9), 17, 18, 19, 21, 27, 28],
        15: [11, 12, 20, 37, 38, 43, 46, *range(53, 58), 61, 64]},
    7: {14: [2, 3, 4, 5, 26, 29, 31, 39, 44],
        15: [12, 13, 14, 15, 24, 25, 33, 37, 49, 51, 56]},
    8: {14: [28], 15: [15, 16, 37, 38]},
    9: {13: [42], 14: [2, 34], 15: [9, 10, 20, 21, 22, 53]},
}


def read_json(p):
    return json.loads(p.read_text(encoding='utf-8'))


def write_json(p, value):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def original_banks():
    if ARCHIVE.exists():
        with zipfile.ZipFile(ARCHIVE) as z:
            return [json.loads(z.read(n)) for n in z.namelist()
                    if n.startswith('Chapter_') and n.endswith('.json')
                    and not n.endswith('.coverage.json')]
    return [read_json(p) for p in sorted(DEST.glob('Chapter_*.json'))
            if not p.name.endswith('.coverage.json')]


def build():
    sources = sorted((DATA / 'files/Cardiology').glob('*.docx'),
                     key=lambda p: int(p.name.split('.')[0]))
    assert len(sources) == 15
    originals = original_banks()
    assert len(originals) == 11
    for bank in originals:
        validate(bank)
    original_q = {q['id']: q for b in originals for q in b['questions']}
    assert len(original_q) == sum(len(b['questions']) for b in originals) == 615
    groups = {i: [] for i in range(1, 16)}
    routes = []
    for b in sorted(originals, key=lambda b: b['chapterOrder']):
        old = b['chapterOrder']
        numbered = {int(q['id'].split('-')[-1]): q for q in b['questions']}
        assignments = {}
        for target, numbers in MOVES.get(old, {}).items():
            for n in numbers:
                assert n in numbered and n not in assignments, (old, n)
                assignments[n] = target
        for n, q in numbered.items():
            target = assignments.get(n, old)
            groups[target].append(copy.deepcopy(q))
            routes.append(dict(questionId=q['id'], title=q['explanationTeaching']['title'],
                               fromChapter=old, toChapter=target,
                               originalQuestionSha256=digest(q),
                               release='previously_installed' if old <= 9 else 'draft_not_installed'))
    banks = []
    for i, source in enumerate(sources, 1):
        assert int(source.name.split('.')[0]) == i and groups[i]
        b = {k: copy.deepcopy(v) for k, v in originals[0].items()
             if k not in {'questions', 'validation', 'installedSha256'}}
        qs = groups[i]
        draft = sum(q['id'].startswith(('cardiology-rebuild-10-', 'cardiology-rebuild-11-')) for q in qs)
        b.update(chapterOrder=i, document=source.stem,
                 headingText=source.stem.split('. ', 1)[1], questions=qs,
                 targetQuestions=len(qs), status='redistributed_existing_questions',
                 sourceDocument=source.name,
                 sourceNote='Existing questions redistributed by clinical focus to the canonical files/Cardiology chapters. '
                 'Question content and source-review status are unchanged. This is not a claim of complete source coverage or a deep-dive explanation rewrite.',
                 redistribution=dict(originalIdsPreserved=True, existingQuestions=len(qs),
                     previouslyInstalledQuestions=len(qs)-draft, draftQuestions=draft,
                     coverageStatus='incomplete_requires_chapter_review',
                     explanationStructureStatus='original_explanations_preserved_not_rewritten'))
        banks.append(b)
    after = {q['id']: q for b in banks for q in b['questions']}
    assert set(after) == set(original_q)
    assert all(after[k] == original_q[k] for k in after)
    assert sum(len(b['questions']) for b in banks) == len(after)
    report = dict(status='passed', totalQuestions=len(after), uniqueQuestionIds=len(after),
        questionsLost=0, questionsDuplicated=0, questionContentChanges=0,
        previouslyInstalledQuestions=541, draftQuestionsNotInstalled=74,
        sourceFolder=str(DATA / 'files/Cardiology'),
        chapters=[dict(chapter=b['chapterOrder'], file=b['document']+'.json',
                       **b['redistribution'],
                       answerDistribution=dict(collections.Counter(chr(65+q['correctIndex']) for q in b['questions'])))
                  for b in banks], questionAssignments=routes)
    return banks, report


def apply(banks, report):
    expected={q['id']:q for b in banks for q in b['questions']}
    for b in banks:
        current=DEST/(b['document']+'.json')
        if current.exists():
            assert all(q['id'] in expected and expected[q['id']]==q for q in read_json(current)['questions']), 'Later chapter edits exist; do not overwrite them with the frozen redistribution'
    AUDIT.mkdir(parents=True, exist_ok=True)
    if not ARCHIVE.exists():
        files = list(DEST.glob('*.json'))
        with zipfile.ZipFile(ARCHIVE, 'x', zipfile.ZIP_DEFLATED) as z:
            for p in files:
                z.writestr(p.name, p.read_bytes())
            z.writestr('progress-before.json', (ROOT/'progress.json').read_bytes())
        with zipfile.ZipFile(ARCHIVE) as z:
            for p in files:
                assert z.read(p.name) == p.read_bytes()
    # Only verified, archived legacy chapter artifacts are removed.
    for p in DEST.glob('Chapter_*.json'):
        assert p.resolve().is_relative_to(DEST.resolve())
        with zipfile.ZipFile(ARCHIVE) as z:
            assert z.read(p.name) == p.read_bytes()
        p.unlink()
    for b in banks:
        write_json(DEST/(b['document']+'.json'), b)
    for p in DEST.glob('*-source-review.json'):
        review = AUDIT/'source-reviews'/p.name
        if review.exists():
            assert review.read_bytes() == p.read_bytes()
        else:
            review.parent.mkdir(parents=True, exist_ok=True)
            review.write_bytes(p.read_bytes())
        p.unlink()
    write_json(AUDIT/'redistribution-report.json', report)
    lines = ['# Cardiology QBank chapter allocation', '',
        'Names and numbers match the 15 DOCX files in `data/files/Cardiology`.', '',
        '615 existing questions are allocated once each. No new questions were generated. '
        'Question IDs, stems, options, answer keys, explanations and references are unchanged.', '',
        '| Chapter | Topic | Existing questions | Draft questions |',
        '|---|---|---:|---:|']
    for b in banks:
        lines.append(f"| {b['chapterOrder']} | {b['headingText']} | {len(b['questions'])} | {b['redistribution']['draftQuestions']} |")
    lines += ['', '## Review and installation status', '',
        'The 541 previously installed questions are released under the matching source chapter names. '
        'The 65 original endocarditis draft questions and 9 hypertension draft questions remain withheld from the app. '
        'Chapter 10 has one previously installed device-infection question in addition to its 65 draft questions. '
        'Chapter 11 contains only drafts, so it has a delivered JSON file but no installed bank.', '',
        'All 15 files contain existing questions, but full chapter coverage is incomplete. '
        'In particular, chapters 12 and 13 contain only 4 and 3 questions respectively. '
        'The original explanations are preserved; a medical deep-dive structure revision has not been performed. '
        'Answer positions are preserved, so the new chapter subsets have uneven answer-letter distributions.', '',
        'The original source-review ledgers describe the old authoring groups, not the redistributed chapter coverage. '
        'Use `audit/redistribution-report.json` for the question-by-question allocation and original content hashes. '
        'The verified original artifacts are retained in `audit/pre-redistribution.zip`.', '',
        'Run `python tools/redistribute_cardiology_qbank.py --verify` to check the delivered files. '
        'The old individual authoring scripts produce the superseded grouping and should not be run directly over this set.', '']
    (DEST/'README.md').write_text('\n'.join(lines), encoding='utf-8')
    plan = read_json(ROOT/'progress.json')
    others = [x for x in plan['chapters'] if x['subject'] != 'Cardiology']
    rows = [dict(subject='Cardiology', chapter=b['chapterOrder'], document=b['document'],
                 file='Cardiology/'+b['document']+'.json', status='redistributed_coverage_incomplete',
                 **b['redistribution']) for b in banks]
    index = next(i for i, x in enumerate(others) if x['subject'] != 'Neurology')
    plan['chapters'] = others[:index] + rows + others[index:]
    plan['cardiologyRedistribution'] = dict(report='Cardiology/audit/redistribution-report.json',
        existingQuestions=615, sourceChapters=15, fullCoverage=False,
        draftQuestionsNotInstalled=74)
    plan['currentChapter'] = 'Cardiology: canonical 15-chapter redistribution; coverage and explanation revision remain'
    write_json(ROOT/'progress.json', plan)


def install(banks):
    """Migrate only the 541 already installed questions; keep 74 drafts withheld."""
    sys.path.insert(0, str(REPO/'src'))
    from cnl_desktop import study_packs
    root = (DATA/'Qbank').resolve()
    study = DATA/'study-data'
    before = {p: p.read_bytes() for p in study_packs._quiz_record_files(study)}
    old = {p: raw for p, raw in before.items() if json.loads(raw).get('folder') == 'Cardiology'}
    released = {q['id']: q for b in banks for q in b['questions']
                if int(q['id'].split('-')[-2]) <= 9}
    actual = {q['id']: q for raw in old.values() for q in json.loads(raw)['questions']}
    assert len(released) == len(actual) == 541 and actual == released
    assert all(p.resolve().is_relative_to(root) for p in old)
    assert not any(p.is_symlink() or p.is_junction() for p in root.rglob('*'))
    backup = DATA/'qbank-reset-backups'/f'cardiology-redistribution-{time.time_ns()}.zip'
    backup.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(backup, 'x', zipfile.ZIP_DEFLATED) as z:
        for p, raw in old.items():
            z.writestr(p.relative_to(root).as_posix(), raw)
    with zipfile.ZipFile(backup) as z:
        assert all(z.read(p.relative_to(root).as_posix()) == raw for p, raw in old.items())
    destinations = {}
    for bank in banks:
        b = copy.deepcopy(bank)
        b['questions'] = [q for q in b['questions'] if q['id'] in released]
        if not b['questions']:
            continue
        b['targetQuestions'] = len(b['questions'])
        b['status'] = 'redistributed_previously_installed_questions'
        # Keep exact source chapter basenames, with an identity digest for the app.
        identity = study_packs._quiz_row_id(b)
        name = hashlib.sha256(identity.encode()).hexdigest()[:20]+'.json'
        dest = root/'Cardiology'/b['document']/'Questions'/name
        assert dest.resolve().is_relative_to(root)
        assert not dest.exists(), dest
        destinations[dest] = b
    try:
        assert all(p.read_bytes() == raw for p, raw in before.items())
        for p, b in destinations.items():
            p.parent.mkdir(parents=True, exist_ok=True)
            write_json(p, b)
        for p in old:
            p.unlink()
        previous_resource = study_packs.paths.resource_root
        try:
            study_packs.paths.resource_root = lambda: DATA.parent/'_internal/assets'
            loaded = study_packs.read_quizzes(study)
        finally:
            study_packs.paths.resource_root = previous_resource
        cardio = [b for b in loaded if b.get('folder') == 'Cardiology']
        assert len(cardio) == len(destinations)
        loaded_qs = {q['id']: q for b in cardio for q in b['questions']}
        assert loaded_qs == released
        assert sum(len(b['questions']) for b in cardio) == 541
        assert all(p.read_bytes() == raw for p, raw in before.items() if p not in old)
    except BaseException:
        for p in destinations:
            p.unlink(missing_ok=True)
        for p, raw in old.items():
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(raw)
        raise
    # Remove only empty legacy directories after successful readback.
    for p in sorted((root/'Cardiology').rglob('*'), key=lambda p: len(p.parts), reverse=True):
        assert p.resolve().is_relative_to(root/'Cardiology')
        if p.is_dir() and not any(p.iterdir()):
            p.rmdir()
    write_json(AUDIT/'installation-report.json', dict(status='passed',
        installedChapters=len(destinations), installedQuestions=541,
        draftQuestionsWithheld=74, otherBanksPreserved=len(before)-len(old),
        backup=str(backup), files=[str(p) for p in destinations],
        note='Chapter 11 has only draft questions and remains uninstalled. All 15 canonical JSON files are delivered in the repository.'))
    plan = read_json(ROOT/'progress.json')
    for row in plan['chapters']:
        if row['subject'] == 'Cardiology':
            row['installedQuestions'] = row['previouslyInstalledQuestions']
            row['draftQuestionsWithheld'] = row['draftQuestions']
            row['runtimeStatus'] = 'installed_redistributed_subset' if row['installedQuestions'] else 'draft_not_installed'
    write_json(ROOT/'progress.json', plan)


def verify(banks, report):
    delivered = [p for p in DEST.glob('*.json') if 'questions' in read_json(p)]
    assert len(delivered) == 15
    expected={q['id']:q for b in banks for q in b['questions']}
    current=[read_json(DEST/(b['document']+'.json')) for b in banks]
    all_questions=[q for b in current for q in b['questions']]
    actual={q['id']:q for q in all_questions}
    assert len(actual)==len(all_questions),'Duplicate question ID across canonical chapters'
    revision_path=AUDIT/'reviewed-question-revisions.json'
    revisions=read_json(revision_path)['revisions'] if revision_path.exists() else []
    revised={r['questionId']:r for r in revisions}
    assert len(revised)==len(revisions),'Duplicate revision entry'
    assert set(revised)<=set(expected),'Revision does not refer to an archived original'
    for k,r in revised.items():
        assert r['status']=='author_source_checked' and r['reason'] and r['sources']
        assert digest(expected[k])==r['originalSha256'],'Revision original digest mismatch'
        assert k in actual and digest(actual[k])==r['revisedSha256'],'Reviewed revision digest mismatch'
        if actual[k]['correctIndex']!=expected[k]['correctIndex']:
            # The original chapter-10 questions were withheld drafts, never part
            # of the original installed 1–9 set. Permit only the explicitly
            # audited reorder used to balance the first full chapter-10 release.
            move=r.get('unpublishedAnswerReorder',{})
            assert k=='cardiology-rebuild-10-001' and move=={'from':0,'to':1,'medicalAnswerUnchanged':True}
            assert expected[k]['options'][expected[k]['correctIndex']]==actual[k]['options'][actual[k]['correctIndex']]
            assert set(expected[k]['options'])==set(actual[k]['options'])
        assert actual[k]['topic']==expected[k]['topic'],'Revision changed chapter topic assignment'
    assert all(actual.get(k)==q or k in revised for k,q in expected.items()),'An original question changed without a reviewed revision or disappeared'
    for original,bank in zip(banks,current):
        assert bank['document']==original['document'] and bank['chapterOrder']==original['chapterOrder']
        assert bank['targetQuestions']==len(bank['questions'])
        assert all(actual[q['id']]==q or q['id'] in revised for q in original['questions'])
        assert {q['id'] for q in original['questions']} <= {q['id'] for q in bank['questions']}
        if any(q['id'] not in expected for q in bank['questions']):
            validate(bank)
    assert read_json(AUDIT/'redistribution-report.json') == report
    installed = read_json(AUDIT/'installation-report.json')
    runtime = [read_json(Path(p)) for p in installed['files']]
    expected = {q['id']: q for b in banks for q in b['questions']
                if int(q['id'].split('-')[-2]) <= 9}
    for number in installed.get('releasedChapterOrders',[]):
        review=read_json(AUDIT/f'chapter-{number:02}-release-review.json')
        released=current[number-1]
        assert review['status']=='passed' and review['installed']
        assert review['reviewedQuestionsSha256']==digest(released['questions'])
        assert released['status']=='installed_verified'
        expected.update({q['id']:q for q in released['questions']})
    actual = {q['id']: q for b in runtime for q in b['questions']}
    installed_count=sum(len(b['questions']) for b in runtime)
    assert actual == expected and installed_count==len(expected)==installed['installedQuestions']
    assert len(runtime)==installed['installedChapters']
    for b in runtime:
        original = banks[b['chapterOrder']-1]
        assert b['document'] == original['document']
        assert b['headingText'] == original['headingText']
        assert b['targetQuestions'] == len(b['questions'])
    print(f'Verified: 15 source-matched JSON files; 615 original IDs retained ({615-len(revised)} questions unchanged, {len(revised)} reviewed revisions); {len(all_questions)} current unique questions; {installed_count} released; {len(all_questions)-installed_count} drafts withheld.')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser()
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--install', action='store_true')
    parser.add_argument('--verify', action='store_true')
    args = parser.parse_args()
    banks, report = build()
    if args.apply:
        apply(banks, report)
    if args.install:
        install(banks)
    if args.verify:
        verify(banks, report)
    if not args.verify:
        print(json.dumps({k:v for k,v in report.items() if k != 'questionAssignments'}, ensure_ascii=False, indent=2))
