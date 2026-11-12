from pathlib import Path
import sys
import unittest
from tempfile import TemporaryDirectory
from unittest.mock import patch
from bs4 import BeautifulSoup

sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'tools'))
import build_site as b

class RendererTests(unittest.TestCase):
    def setUp(self):
        self.docs={'target':{'meta':{'title':'Target note'}}}

    def test_asset_version_is_stable_across_checkout_line_endings(self):
        with TemporaryDirectory() as directory, patch.object(b,'ROOT',Path(directory)):
            stylesheet=Path(directory)/'styles.css'
            stylesheet.write_bytes(b'body {\n  color: #333;\n}\n')
            version=b.asset('styles.css')
            stylesheet.write_bytes(b'body {\r\n  color: #333;\r\n}\r\n')
            self.assertEqual(version,b.asset('styles.css'))
            stylesheet.write_bytes(b'body {\n  color: #444;\n}\n')
            self.assertNotEqual(version,b.asset('styles.css'))

    def test_wrapped_and_code_aliases_are_single_links(self):
        source='[[target|A wrapped\nlabel]] and [[target|`η_f · f_b`]]'
        result=b.wiki_links(source,self.docs)
        html=b.MD.render(result)
        soup=BeautifulSoup(html,'html.parser')
        self.assertEqual([a['href'] for a in soup.find_all('a')],['target.html','target.html'])
        self.assertIn('A wrapped\nlabel',soup.get_text())
        self.assertIsNotNone(soup.find('a').find_next('a').find('code'))

    def test_table_aliases_do_not_split_columns(self):
        source='| Item | Value |\n|---|---|\n| [[target\\|Display]] | 4 |\n'
        soup=BeautifulSoup(b.MD.render(b.wiki_links(source,self.docs)),'html.parser')
        self.assertEqual(len(soup.select('tbody tr td')),2)
        self.assertEqual(soup.select_one('td a').get_text(),'Display')

    def test_code_examples_remain_literal(self):
        source='`[[target]]`\n\n```\n[[target]]\n```\n'
        self.assertEqual(b.wiki_links(source,self.docs),source)

    def test_unknown_links_fail_instead_of_disappearing(self):
        with self.assertRaises(ValueError):b.wiki_links('[[missing]]',self.docs)

    def test_callouts_and_duplicate_headings_keep_text_and_unique_ids(self):
        doc={'body':'# Source title\n\n## Evidence\n\nA finding.\n\n> [!warning] Limited capture.\n> Keep this detail.\n\n## Evidence\n\nAnother finding.'}
        b.render_doc(doc,self.docs)
        soup=BeautifulSoup(doc['html'],'html.parser')
        self.assertEqual([h['id'] for h in soup.find_all('h2')],['evidence','evidence-1'])
        self.assertIn('Limited capture.',soup.get_text())
        self.assertIn('Keep this detail.',soup.get_text())
        self.assertEqual(soup.select_one('.callout-label').text,'Warning')

    def test_raw_html_and_script_links_are_not_executable(self):
        doc={'body':'<script>alert(1)</script>\n\n[bad](javascript:alert(1))'}
        b.render_doc(doc,self.docs)
        soup=BeautifulSoup(doc['html'],'html.parser')
        self.assertIsNone(soup.find('script'))
        self.assertFalse(any(a.get('href','').startswith('javascript:') for a in soup.find_all('a')))

if __name__=='__main__':unittest.main()
