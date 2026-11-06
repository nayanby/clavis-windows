"""Persistent attempts never own or erase Qbank bookmarks."""
import json
from pathlib import Path
import sys
import tempfile
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from cnl_desktop import qbank_progress as progress


class ProgressTests(unittest.TestCase):
    def test_pause_submit_retry_and_bookmarks(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);bank='["Cardiology","CAD","Questions"]'
            def update(**payload):return progress.update(root,dict(bank=bank,**payload))
            update(op='bookmark',question='q1',marked=True)
            paused=dict(id='attempt-one',signature='v1:test',answers=[1,None],index=1,status='paused',score=1,total=2)
            update(op='attempt',attempt=paused)
            update(op='bookmark',question='q2',marked=True)
            entry=progress.read(root)['banks'][bank]
            self.assertEqual(entry['bookmarks'],['q1','q2'])
            self.assertEqual(entry['attempt']['answers'],[1,None])
            submitted={**paused,'answers':[1,0],'status':'submitted'}
            self.assertTrue(update(op='attempt',attempt=submitted)['newSubmission'])
            self.assertFalse(update(op='attempt',attempt=submitted)['newSubmission'])
            entry=update(op='retry')['entry']
            self.assertIsNone(entry['attempt']);self.assertEqual(entry['bookmarks'],['q1','q2'])
            update(op='bookmark',question='q1',marked=False)
            self.assertEqual(progress.read(root)['banks'][bank]['bookmarks'],['q2'])
            self.assertFalse((root/'Qbank').exists())

    def test_invalid_attempt_and_corrupt_state_are_not_overwritten(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            payload=dict(bank='bank',op='attempt',attempt=dict(id='one',signature='test',answers=[None],index=0,status='submitted',score=0,total=1))
            with self.assertRaises(ValueError):progress.update(root,payload)
            self.assertFalse(progress._path(root).exists())
            target=progress._path(root);target.parent.mkdir();target.write_text('invalid JSON')
            with self.assertRaises(ValueError):progress.update(root,dict(bank='bank',op='retry'))
            self.assertEqual(target.read_text(),'invalid JSON')

if __name__=='__main__':unittest.main()
