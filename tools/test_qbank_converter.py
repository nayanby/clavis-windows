"""Native selection, output layout, overwrite backup, and General save compatibility."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from cnl_desktop.qbank_converter import QbankConverter
from cnl_desktop import study_packs
from readable_general_qbanks import migrate


QUESTION = {'question': 'Which option?', 'options': ['Alpha', 'Beta'], 'correctIndex': 1,
    'explanation': 'Reason', 'explanationHtml': '<h2>Reason</h2><table><tr><td><b>Beta</b></td></tr></table>'}


class Window:
    def __init__(self, files): self.files = files
    def create_file_dialog(self, kind, **kwargs):
        assert kwargs['allow_multiple']
        return self.files


class ConversionTests(unittest.TestCase):
    def test_multiple_files_and_backup(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            one = root / 'Acid Base.html'; two = root / 'Heart Failure.htm'
            one.write_text('<meta charset=utf-8><p>β</p>', encoding='utf-8')
            two.write_text('<p>Two</p>', encoding='utf-8')
            api = QbankConverter(); api._window = Window([str(one), str(two)])
            selected = api.choose_qbank_html()['files']
            self.assertEqual(len(selected), 2)
            self.assertIn('β', selected[0]['html'])
            for entry in selected:
                saved = api.save_qbank_json(entry['token'], [QUESTION])
                self.assertNotIn('error', saved)
                source = root / entry['name']
                target = source.parent / source.stem / (source.stem + '.json')
                self.assertEqual(Path(saved['path']), target)
                self.assertEqual(json.loads(target.read_text(encoding='utf-8'))['questions'], [QUESTION])
                self.assertTrue(source.exists())
                self.assertIn('error', api.save_qbank_json(entry['token'], [QUESTION]))
            target = root / 'Acid Base' / 'Acid Base.json'
            old = target.read_bytes()
            selected = api.choose_qbank_html()['files']
            saved = api.save_qbank_json(selected[0]['token'], [{**QUESTION, 'question': 'Changed?'}])
            self.assertNotIn('error', saved)
            self.assertEqual(Path(saved['backup']).read_bytes(), old)
            self.assertEqual(one.read_text(encoding='utf-8'), '<meta charset=utf-8><p>β</p>')
            self.assertIn('error', api.save_qbank_json('../outside', [QUESTION]))

    def test_cancel_empty_and_errors(self):
        api = QbankConverter(); api._window = Window(None)
        self.assertEqual(api.choose_qbank_html(), {'files': []})
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / 'Empty.html'; source.write_text('<p>Notes</p>')
            api._window = Window([str(source), str(source.with_suffix('.missing'))])
            rows = api.choose_qbank_html()['files']
            self.assertIn('error', rows[1])
            self.assertIn('error', api.save_qbank_json(rows[0]['token'], []))
            self.assertFalse((source.parent / source.stem).exists())

    def test_general_migration_and_edit_preserve_path(self):
        with tempfile.TemporaryDirectory() as directory:
            data = Path(directory); root = data / 'Qbank'; root.mkdir()
            row = {'folder': 'Cardiology', 'document': 'CAD and ACS', 'headingText': 'CAD and ACS',
                'headingIndex': 0, 'chapterOrder': 3, 'navigationGroup': 'general', 'questions': [QUESTION], 'madeAt': 1}
            source = root / 'Cardiology/General/03. CAD and ACS/01. CAD and ACS/hash.json'
            source.parent.mkdir(parents=True); source.write_text(json.dumps(row))
            original = source.read_bytes()
            legacy = root / 'Cardiology/01. Legacy/01. Heading/legacy.json'
            legacy.parent.mkdir(parents=True); legacy.write_text(json.dumps({**row, 'document': 'Legacy', 'headingText': 'Heading', 'navigationGroup': ''}))
            report = migrate(root, apply=True)
            self.assertEqual(report['files'], 1)
            target = source.parent.parent / 'CAD and ACS.json'
            self.assertEqual(target.read_bytes(), original)
            self.assertTrue(legacy.exists())
            self.assertFalse(source.parent.exists())
            self.assertEqual(migrate(root)['files'], 0)
            rows = study_packs._read_quiz_records(data / 'study-data')
            general = next(r for r in rows if r.get('navigationGroup') == 'general')
            self.assertEqual(general['chapterOrder'], 3)
            study_packs.migrate_saved_quizzes(data / 'study-data')
            self.assertEqual(json.loads(target.read_text())['chapterOrder'], 3)
            study_packs.upsert_saved_quiz(data / 'study-data', {**general, 'questions': [{**QUESTION, 'question': 'Edited?'}]})
            self.assertEqual(list(target.parent.glob('*.json')), [target])
            self.assertEqual(json.loads(target.read_text())['questions'][0]['question'], 'Edited?')


if __name__ == '__main__': unittest.main()
