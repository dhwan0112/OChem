"""표기 정리와 목록 재생성에서 발견된 실제 회귀 사례."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import build_wiki_index as wiki
from math_notation import inline_greek


class MathNotationTests(unittest.TestCase):
    def test_locant_hyphen_is_not_a_partial_charge(self):
        cases = {
            'δ-H': r'$\delta$-H',
            'γ,δ-unsaturated': r'$\gamma,\delta$-unsaturated',
            'δ+': r'$\delta^{+}$',
            'δ⁻': r'$\delta^{-}$',
            'ψ₂': r'$\psi_{2}$',
            'hν': r'$h\nu$',
        }
        for text, expected in cases.items():
            with self.subTest(text=text):
                self.assertEqual(inline_greek(text), expected)
                self.assertEqual(inline_greek(expected), expected)

    def test_summary_preserves_commands_and_complete_math(self):
        self.assertIn(r'\alpha', wiki.short(r'[$\alpha$-H](target.md) 설명'))
        for length in range(8, 80):
            result = wiki.short('a' * 30 + r' $\alpha,\beta$-unsaturated carbonyl', length)
            self.assertEqual(result.count('$') % 2, 0, result)

    def test_long_reaction_summary_is_meaningful(self):
        equation = r'$\mathrm{CH_3(CH_2)_6CH_2Br} + \mathrm{NH_3} \xrightarrow{\text{long reagent label}} \text{octylamine}$'
        self.assertEqual(wiki.short(equation), '반응식은 본문 참고')

    def test_navigation_retains_backslashes_and_escaped_brackets(self):
        with tempfile.TemporaryDirectory() as folder:
            notes = Path(folder) / 'notes'
            notes.mkdir()
            page = notes / 'L15_Example.md'
            page.write_text('# Example\n' + wiki.START + '\nold\n' + wiki.END + '\n')
            docs = [dict(title='Staudinger β-lactam synthesis', aliases=[],
                         path=str(Path(folder) / 'reaction.md'), category='반응', lectures=[15]),
                    dict(title=r'\[2+2\] cycloaddition', aliases=[],
                         path=str(Path(folder) / 'cycloaddition.md'), category='반응', lectures=[15])]
            with patch.object(wiki, 'NOTES', str(notes)):
                self.assertEqual(wiki.update_lecture_notes(docs), 1)
                result = page.read_text()
                self.assertIn('Staudinger beta-lactam synthesis', result)
                self.assertNotIn(r'$\beta$', result)
                self.assertIn(r'\[2+2\]', result)
                self.assertNotIn(r'\\[2+2\\]', result)
                self.assertFalse(any(ord(c) < 32 and c not in '\n\t\r' for c in result))
                self.assertEqual(wiki.update_lecture_notes(docs), 0)


if __name__ == '__main__':
    unittest.main()
