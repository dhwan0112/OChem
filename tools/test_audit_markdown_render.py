"""Regressions for defects observed in the lecture Markdown sources."""
import tempfile
import unittest
from pathlib import Path

from audit_markdown_render import audit, GitHubProse


class MarkdownAuditTests(unittest.TestCase):
    def test_github_prose_excludes_only_code_and_recognized_math(self):
        parser = GitHubProse()
        parser.feed('<p>Text <math-renderer>$x$</math-renderer> $broken$</p>'
                    '<pre><code>** $</code></pre><a href="x">$link$</a>')
        self.assertEqual(parser.maths, 1)
        self.assertEqual(''.join(parser.parts), 'Text  $broken$$link$')

    def codes(self, source):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'L11_example.md'
            path.write_text(source)
            return {item['code'] for item in audit(path)}

    def test_independent_math_and_protected_code(self):
        self.assertEqual(self.codes('Text.\n\n$$\n\\mathrm{CH_3}\n$$\n\n'
                                    '`\\clearpage`\n\n```text\n$ **\n```\n'), set())

    def test_observed_defects(self):
        cases = {
            'INLINE_DISPLAY': 'Text $$x$$\n',
            'DISPLAY_BOUNDARY': 'Text\n$$\nx\n$$\n',
            'UNCLOSED_DISPLAY': '$$\nx\n',
            'UNCLOSED_CODE': '```python\nx\n',
            'PDF_COMMAND': '\\clearpage\n',
            'LOCAL_IMAGE': '![](/home/kim/image.png)\n',
            'EMPTY_ALT': '![](missing.png)\n',
            'MISSING_IMAGE': '![reaction](missing.png)\n',
            'PANDOC_SCRIPT': 'cm^−1^ and pK~a~\n',
            'LATEX_IN_PROSE': '\\mathrm{CH_3}\n',
            'UNMATCHED_DOLLAR': 'Text $x\n',
            'UNBALANCED_BOLD_PARAGRAPH': '**first\n\nsecond**\n',
            'MATH_IN_LINK_LABEL': '[Staudinger $\\beta$-lactam](note.md)\n',
            'MATH_IN_FOOTNOTE': '[^1]: $\\sigma$ complex\n',
            'MULTILINE_INLINE_MATH': '$\\begin{aligned}x\\end{aligned}$\n',
        }
        for code, source in cases.items():
            with self.subTest(code=code):
                self.assertIn(code, self.codes(source))


if __name__ == '__main__':
    unittest.main()
