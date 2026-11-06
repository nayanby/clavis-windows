"""Verify physical General migration, round trips and edit persistence."""
import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch
from group_qbanks_general import organize, study_packs, REPO
from restore_legacy_qbanks import restore


class GeneralTests(unittest.TestCase):
    def test_legacy_restore_preserves_general_and_deduplicates(self):
        with TemporaryDirectory(dir=REPO/'build') as tmp, patch.object(study_packs.paths,'resource_root',return_value=Path(tmp)/'assets'):
            data=Path(tmp)/'data'
            source=Path(tmp)/'saved'
            source.mkdir()
            general=dict(folder='Neurology',document='Epilepsy',headingText='Epilepsy',navigationGroup='general',
                         questions=[dict(question='General',options=['A','B'],correctIndex=0)])
            study=data/'study-data'
            saved=study_packs.upsert_saved_quiz(study,general)
            path=study_packs._quiz_record_path(study,saved)
            raw=path.read_bytes()
            legacy=dict(folder='Neurology',document='II. Seizures',headingText='SEIZURES',headingIndex=3,
                        questions=[dict(question='Legacy',options=['A','B'],correctIndex=1,explanationHtml='<h2>Preserved</h2>')])
            for name in ('original','duplicate'):
                (source/f'{name}.json').write_text(json.dumps(legacy),encoding='utf-8')
            report=restore(source,data,True)
            self.assertEqual(report['banks'],1)
            self.assertEqual(report['duplicateCopiesSkipped'],1)
            self.assertEqual(path.read_bytes(),raw)
            record=study_packs.find_saved_quiz(study,'Neurology','II. Seizures','SEIZURES')
            self.assertEqual(record['questions'],legacy['questions'])
            target=study_packs._quiz_record_path(study,record)
            self.assertEqual(target.parent.name,'01. SEIZURES')
            self.assertEqual(target.parent.parent.name,'02. Seizures')
            self.assertEqual(json.loads((source/'original.json').read_text()),legacy)

    def test_move_edit_and_restart(self):
        with TemporaryDirectory(dir=REPO/'build') as tmp, patch.object(study_packs.paths, 'resource_root', return_value=Path(tmp)/'assets'):
            data = Path(tmp)/'data'
            study = data/'study-data'
            row = dict(folder='Neurology',document='Epilepsy',headingText='Epilepsy',
                       chapterOrder=2,topicOrder=1,questions=[dict(question='Original',options=['A','B','C','D'],
                       correctIndex=2,explanationHtml='<h2>Reason</h2><table><tr><td>Cell</td></tr></table>')])
            original = study_packs.upsert_saved_quiz(study,row)
            other = study_packs.upsert_saved_quiz(study,{**row,'folder':'Other subject'})
            other_path = study_packs._quiz_record_path(study,other)
            other_bytes = other_path.read_bytes()
            report = organize(data,True)
            self.assertEqual(report['modules'],1)
            self.assertEqual(other_path.read_bytes(),other_bytes)
            target = study_packs._quiz_record_path(study,row)
            self.assertEqual(target.relative_to(data/'Qbank').parts[1],'General')
            loaded = study_packs.find_saved_quiz(study,'Neurology','Epilepsy','Epilepsy')
            self.assertEqual(loaded['questions'],original['questions'])
            self.assertEqual(loaded['navigationGroup'],'general')
            # Even an older editor payload lacking metadata must retain its folder.
            row['questions'][0]['question']='Edited'
            edited = study_packs.upsert_saved_quiz(study,row)
            self.assertEqual(edited['navigationGroup'],'general')
            self.assertEqual(len(study_packs._quiz_record_files(study)),2)
            self.assertEqual(study_packs.migrate_saved_quizzes(study),2)
            loaded = study_packs.find_saved_quiz(study,'Neurology','Epilepsy','Epilepsy')
            self.assertEqual(loaded['questions'][0]['question'],'Edited')
            self.assertEqual(loaded['navigationGroup'],'general')
            self.assertEqual(organize(data,True)['modules'],0)
            self.assertEqual(json.loads(target.read_text())['questions'],row['questions'])


if __name__ == '__main__':
    unittest.main()
