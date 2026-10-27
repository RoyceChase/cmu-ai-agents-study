import contextlib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/update_bibliography.py"
SPEC = importlib.util.spec_from_file_location("bibliography", SCRIPT)
bib = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(bib)
XML = b'''<feed xmlns="http://www.w3.org/2005/Atom"
 xmlns:arxiv="http://arxiv.org/schemas/atom">
 <entry><id>http://arxiv.org/abs/2302.04761v1</id>
 <title>Example: Tools &amp; Models</title><published>2023-02-09T00:00:00Z</published>
 <author><name>Example Author</name></author>
 <arxiv:primary_category term="cs.CL"/></entry></feed>'''


class BibliographyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.refs = self.root / "references"
        self.refs.mkdir()
        self.pdf = self.refs / "paper with spaces.pdf"
        self.pdf.write_bytes(b"%PDF-fixture")
        self.readme = self.refs / "README.md"
        self.row = "| Paper | [arXiv](https://arxiv.org/abs/2302.04761) | [PDF](<paper with spaces.pdf>) |\n"
        self.readme.write_text(self.row, encoding="utf-8")
        self.output = self.refs / "bibliography.bib"
        self.metadata = bib.parse_metadata(XML)
        self.root_patch = patch.object(bib, "ROOT", self.root)
        self.root_patch.start()
        self.addCleanup(self.root_patch.stop)

    def papers(self):
        return bib.extract_papers(self.readme)

    def test_spaces_percent_encoding_duplicate_rows_and_code_examples(self):
        self.readme.write_text(self.row + self.row.replace("<paper with spaces.pdf>", "paper%20with%20spaces.pdf") + "```markdown\n| [arXiv](https://arxiv.org/abs/9999.99999) |\n```\n", encoding="utf-8")
        self.assertEqual(self.papers(), {"2302.04761": ("2302.04761", self.pdf)})

    def test_missing_pdf_and_ambiguous_pair_fail(self):
        self.pdf.unlink()
        with self.assertRaisesRegex(ValueError, "PDF missing"):
            self.papers()
        self.pdf.touch()
        self.readme.write_text(self.row.replace("| Paper |", "| [Other](https://arxiv.org/abs/2210.03629) |"), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "expected one"):
            self.papers()

    def test_conflicting_versions_fail(self):
        self.readme.write_text(self.row + self.row.replace("2302.04761)", "2302.04761v1)"), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Conflicting"):
            self.papers()

    def test_preserves_key_custom_fields_other_entries_and_is_idempotent(self):
        existing = '% Keep comment\n@misc{mykey, eprint={2302.04761}, note={Nested {custom}, note}}\n\n@book{other, title={Keep me}}\n'
        result = bib.merge_bibliography(existing, self.papers(), self.metadata, self.output)
        self.assertIn('@misc{mykey,', result)
        self.assertIn('note = {Nested {custom}, note}', result)
        self.assertIn('@book{other, title={Keep me}}', result)
        self.assertIn('file = {paper with spaces.pdf}', result)
        self.assertIn(r'Tools \& Models', result)
        self.assertEqual(result, bib.merge_bibliography(result, self.papers(), self.metadata, self.output))

    def test_new_entry_uses_stable_key(self):
        result = bib.merge_bibliography('', self.papers(), self.metadata, self.output)
        self.assertIn('@misc{arxiv230204761,', result)
        self.assertEqual(result, bib.merge_bibliography(result, self.papers(), self.metadata, self.output))

    def test_paper_directory_keeps_pdf_and_notes_together(self):
        folder = self.refs / 'papers/2302.04761-toolformer'
        folder.mkdir(parents=True)
        pdf = folder / 'paper.pdf'
        self.pdf.rename(pdf)
        (folder / 'notes.md').write_text('# Reading notes\n', encoding='utf-8')
        self.readme.write_text(self.row.replace('<paper with spaces.pdf>', 'papers/2302.04761-toolformer/paper.pdf'), encoding='utf-8')
        result = bib.merge_bibliography('', self.papers(), self.metadata, self.output)
        self.assertIn('file = {papers/2302.04761-toolformer/paper.pdf}', result)

    def test_version_and_missing_metadata_rejected(self):
        papers = {'2302.04761': ('2302.04761v2', self.pdf)}
        with self.assertRaisesRegex(ValueError, 'mismatched'):
            bib.merge_bibliography('', papers, self.metadata, self.output)
        with self.assertRaisesRegex(ValueError, 'Missing'):
            bib.merge_bibliography('', self.papers(), {}, self.output)

    def test_duplicate_entries_and_broken_bib_fail(self):
        for existing in ['@misc{a,eprint={2302.04761}}\n@misc{b,eprint={2302.04761}}', '@misc{a,title={unclosed}', '@misc(a,title={unsupported})']:
            with self.assertRaises(ValueError):
                bib.merge_bibliography(existing, self.papers(), self.metadata, self.output)

    def test_cli_dry_run_and_error_do_not_change_output(self):
        self.output.write_text('% original\n', encoding='utf-8')
        before = self.output.read_bytes()
        argv = ['update', '--readme', str(self.readme), '--output', str(self.output), '--dry-run']
        with patch('sys.argv', argv), patch.object(bib, 'fetch_metadata', return_value=XML), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(bib.main(), 0)
        self.assertEqual(self.output.read_bytes(), before)
        with patch('sys.argv', argv[:-1]), patch.object(bib, 'fetch_metadata', return_value=b'<invalid'), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(bib.main(), 1)
        self.assertEqual(self.output.read_bytes(), before)


if __name__ == '__main__':
    unittest.main()
