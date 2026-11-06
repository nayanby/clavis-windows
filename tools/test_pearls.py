"""Pearls shelf tests, including containment and deterministic topic order."""
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

REPO=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(REPO/'src'))
from cnl_desktop import pearls, html_transform


class PearlsTests(unittest.TestCase):
    def test_shelf_and_paths(self):
        with TemporaryDirectory(dir=REPO/'build') as temp:
            data=Path(temp);root=data/'Pearls'
            folder=root/'Cardiology';folder.mkdir(parents=True)
            for name in ['02. Heart Failure.docx','01. CAD and ACS.docx','~$Open.docx','ignored.txt']:
                (folder/name).write_bytes(b'not opened by shelf')
            (root/'index.html').write_text('index')
            (root/'Empty').mkdir()
            with patch.object(pearls.study_packs,'read_quizzes',return_value=[]):
                result=pearls.catalog(data)
            self.assertEqual([s['name'] for s in result['subjects']],['Cardiology'])
            topics=result['subjects'][0]['topics']
            self.assertEqual([t['label'] for t in topics],['CAD and ACS','Heart Failure'])
            self.assertIsNotNone(pearls.resolve(root,topics[0]['id']))
            for bad in ['../Cardiology/01. CAD and ACS.docx','Cardiology/~$Open.docx',
                        'Cardiology/ignored.txt',str(folder/'01. CAD and ACS.docx'),'bad\x00.docx','no.docx']:
                self.assertIsNone(pearls.resolve(root,bad),bad)

    def test_html_detection_conversion_and_save(self):
        import io,zipfile
        from docx import Document
        with TemporaryDirectory(dir=REPO/'build') as temp:
            data=Path(temp);root=data/'Pearls';folder=root/'Nephrology';folder.mkdir(parents=True)
            source=folder/'Acid Base.html'
            original=b'<html><body><main><h1>Title</h1><h2>Interpretation</h2><p><strong>Bold</strong> text HCO<sub>3</sub></p><ul><li>First</li></ul><table><tr><th>A</th><th>B</th></tr><tr><td>1</td><td>2</td></tr></table><script>throw new Error()</script></main></body></html>'
            source.write_bytes(original)
            word=source.with_suffix('.docx');word.write_bytes(b'Previous Word version')
            with patch.object(pearls.study_packs,'read_quizzes',return_value=[]):
                topics=pearls.catalog(data)['subjects'][0]['topics']
            self.assertEqual(len(topics),1)
            self.assertEqual(topics[0]['format'],'html')
            self.assertTrue(topics[0]['id'].endswith('.html'))
            converted=pearls.word_document(source)
            document=Document(io.BytesIO(converted))
            self.assertEqual(len(document.tables),1)
            self.assertTrue(any(r.bold for p in document.paragraphs for r in p.runs))
            self.assertNotIn('Title',''.join(p.text for p in document.paragraphs))
            self.assertNotIn('throw new Error',''.join(p.text for p in document.paragraphs))
            self.assertFalse((root/'_backups').exists(),'Opening HTML does not write Word or create a backup')
            self.assertEqual(pearls.save_word(root,'Nephrology/Acid Base.html')['path'],'Nephrology/Acid Base.docx')
            self.assertEqual(word.read_bytes(),converted)
            self.assertEqual(source.read_bytes(),original)
            backup=next((root/'_backups').glob('*.zip'))
            with zipfile.ZipFile(backup) as archive:self.assertEqual(archive.read('Nephrology/Acid Base.docx'),b'Previous Word version')
            with self.assertRaises(ValueError):pearls.save_word(root,'../outside.html')

    def test_general_order_matches_qbank(self):
        with TemporaryDirectory(dir=REPO/'build') as temp:
            data=Path(temp);folder=data/'Pearls/Cardiology';folder.mkdir(parents=True)
            for name in ['Zeta','Alpha']:(folder/f'{name}.docx').write_bytes(b'Word')
            rows=[dict(folder='Cardiology',document='Zeta',headingText='Zeta',chapterOrder=1,navigationGroup='general')]
            with patch.object(pearls.study_packs,'read_quizzes',return_value=rows):
                self.assertEqual(pearls.catalog(data)['subjects'][0]['topics'][0]['label'],'Zeta')

    def test_page_has_navigation(self):
        page=html_transform.transform_html((REPO/'assets/app.html').read_text(encoding='utf-8'))
        self.assertIn('cnlInstallPearls();',page)
        self.assertIn('function cnlPaintPearlsPage()',page)
        self.assertIn("frame.src='/pearls/viewer?'",page)
        self.assertIn('await openPendingDocument(key)',page)
        clone=pearls.viewer_html(page)
        self.assertIn('window.cnlPearlsLibraryBoot = loadServerLibrary()',clone)
        self.assertNotIn('window.cnlPearlsLibraryBoot = loadServerLibrary()',page)
        self.assertIn('cnlReaderBottomPill',clone)
        self.assertIn('cnlOutlineBtn',clone)


if __name__=='__main__':unittest.main()
