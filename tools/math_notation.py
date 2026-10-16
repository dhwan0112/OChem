"""생성 목록의 그리스 문자 표기를 본문과 같은 inline LaTeX로 유지한다.

파일명, URL, 태그에는 적용하지 않는다. 기존 $…$ / $$…$$와 코드 표기는 보존한다.
"""
import re

GREEK = dict(zip('αβγδΔπσψνω',
                 ('alpha', 'beta', 'gamma', 'delta', 'Delta', 'pi', 'sigma', 'psi', 'nu', 'omega')))
_CHARS = ''.join(GREEK)
_SUB = str.maketrans('₀₁₂₃₄₅₆₇₈₉ₐₑₕᵢⱼₖₗₘₙₒₚᵣₛₜᵤᵥₓ', '0123456789aehijklmnoprstuvx')
TOKEN = re.compile(
    r'10\^\(ΔpKa\)|'
    r'δ<sub>[HC]</sub>|'
    r'Δ\d+(?:\([0-9a-z]+\))?|'
    r'(?:\(4n(?:\+2)?\)|4n(?:\+2)?|[0-9]+|h)?'
    r'[' + _CHARS + r']'
    r'(?:[' + _CHARS + r']|,\s*[' + _CHARS + r'])*'
    r'(?:[₀-₉ₐₑₕᵢⱼₖₗₘₙₒₚᵣₛₜᵤᵥₓ]+|[0-9]+[sa]?)?'
    r'(?:[⁺⁻]|(?<=[δ])[+−]|(?<=δ)-(?![A-Za-z0-9])|\*(?!\*))?')
PROTECTED = re.compile(r'(`+).*?\1|(?<!\\)\$\$.*?(?<!\\)\$\$|(?<!\\)\$[^$]*?(?<!\\)\$', re.S)


def latex_token(token):
    """토큰을 수식으로 바꾼다. 원문에 적힌 전자 수/첨자는 보존한다."""
    if token == '10^(ΔpKa)':
        return r'10^{\Delta pK_{\mathrm{a}}}'
    if re.fullmatch(r'δ<sub>[HC]</sub>', token):
        return r'\delta_{\mathrm{' + token[6] + '}}'
    if re.fullmatch(r'Δ\d+(?:\([0-9a-z]+\))?', token):
        return r'\Delta^{' + token[1:] + '}'
    token = re.sub(r'([₀-₉ₐₑₕᵢⱼₖₗₘₙₒₚᵣₛₜᵤᵥₓ]+)',
                   lambda m: '_{' + m[0].translate(_SUB) + '}', token)
    token = re.sub(r'ψ([0-9]+)', r'ψ_{\1}', token)
    token = re.sub(r'([πσω][0-9]+)([sa])', lambda m: m[1] + r'\mathrm{' + m[2] + '}', token)
    token = token.replace('⁺', '^{+}').replace('⁻', '^{-}')
    token = re.sub(r'δ([+−-])', lambda m: 'δ^{' + ('+' if m[1] == '+' else '-') + '}', token)
    if token.endswith('*'):
        token = token[:-1] + '^{*}'
    return ''.join('\\' + GREEK[c] if c in GREEK else c for c in token)


def inline_greek(text):
    """생성되는 짧은 본문/링크 표시 글자를 정리한다. URL에는 사용하지 않는다."""
    parts = []
    end = 0
    for m in PROTECTED.finditer(text):
        parts.append(TOKEN.sub(lambda t: '$' + latex_token(t[0]) + '$', text[end:m.start()]))
        parts.append(m[0])
        end = m.end()
    parts.append(TOKEN.sub(lambda t: '$' + latex_token(t[0]) + '$', text[end:]))
    return ''.join(parts)


def plain_greek_label(text):
    """서식이 바뀐 제목을 기존 태그 분류표의 이름과 비교한다."""
    reverse = {v: k for k, v in GREEK.items()}
    return re.sub(r'\$\\(' + '|'.join(reverse) + r')\$', lambda m: reverse[m[1]], text)
