#!/usr/bin/env python3
"""Conservative Markdown source checks; does not certify a live renderer.

Math must use balanced inline dollars or standalone display delimiters with
blank lines outside the block. Code, comments and math are masked before
checking prose. Semantic heading/figure consistency requires manual review.
"""
import argparse
import json
import re
import subprocess
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote


class GitHubProse(HTMLParser):
    """Keep visible prose, excluding code and GitHub-recognized math."""
    def __init__(self):
        super().__init__()
        self.ignored = 0
        self.parts = []
        self.maths = 0

    def handle_starttag(self, tag, attrs):
        if tag in {'math-renderer', 'code', 'pre'}:
            self.ignored += 1
        if tag == 'math-renderer':
            self.maths += 1

    def handle_endtag(self, tag):
        if tag in {'math-renderer', 'code', 'pre'}:
            self.ignored -= 1

    def handle_data(self, data):
        if not self.ignored:
            self.parts.append(data)


def audit_github(path):
    request = json.dumps(dict(text=path.read_text(encoding='utf-8'), mode='gfm'))
    response = subprocess.run(['gh', 'api', 'markdown', '--input', '-'],
                              input=request, capture_output=True, text=True, check=True)
    parser = GitHubProse()
    parser.feed(response.stdout)
    leftovers = re.findall(r'\$|\\(?:text|mathrm|begin|xrightarrow|mathstrut)\b|\*\*',
                           ''.join(parser.parts))
    findings = []
    if leftovers:
        findings.append(dict(file=str(path), line=0, code='GITHUB_UNRENDERED',
                             detail=f'{len(leftovers)} math/emphasis markers remain in GitHub prose'))
    return parser.maths, findings


def audit(path):
    source = path.read_text(encoding='utf-8')
    findings = []

    def flag(code, offset, detail):
        findings.append(dict(file=str(path), line=source.count('\n', 0, offset)+1,
                             code=code, detail=detail))

    def mask(match):
        return ''.join('\n' if c == '\n' else ' ' for c in match[0])

    text = re.sub(r'<!--[\s\S]*?-->', mask, source)
    lines = text.splitlines(keepends=True)
    fence = None
    display = False
    offset = 0
    masked = []
    for n, line in enumerate(lines):
        stripped = line.strip()
        opening = re.match(r'^(`{3,}|~{3,})', stripped)
        if fence:
            if re.fullmatch(re.escape(fence[0])+r'{'+str(len(fence))+r',}', stripped):
                fence = None
            masked.append(re.sub(r'[^\n]', ' ', line))
        elif opening and not display:
            fence = opening[1]
            masked.append(re.sub(r'[^\n]', ' ', line))
        elif stripped == '$$':
            neighbor = n+1 if display else n-1
            if 0 <= neighbor < len(lines) and lines[neighbor].strip():
                flag('DISPLAY_BOUNDARY', offset, 'Blank line required outside display block')
            display = not display
            masked.append(re.sub(r'[^\n]', ' ', line))
        elif display:
            masked.append(re.sub(r'[^\n]', ' ', line))
        else:
            if '$$' in line:
                flag('INLINE_DISPLAY', offset, 'Display delimiters must occupy their own lines')
            masked.append(line)
        offset += len(line)
    if fence:
        flag('UNCLOSED_CODE', len(source), 'Unclosed code fence')
    if display:
        flag('UNCLOSED_DISPLAY', len(source), 'Unclosed display math')
    text = ''.join(masked)
    text = re.sub(r'(`+)[^\n]*?\1', mask, text)
    for match in re.finditer(r'\[([^\]\n]*\$[^\]\n]*)\]\(', text):
        flag('MATH_IN_LINK_LABEL', match.start(), 'GitHub leaves link-label math unrendered')
    for match in re.finditer(r'^\[\^[^\]]+\]:[^\n]*\$', text, re.M):
        flag('MATH_IN_FOOTNOTE', match.start(), 'GitHub leaves footnote math unrendered')
    for match in re.finditer(r'(?<!\$)\$\\begin\{(?:aligned|gathered)\}', text):
        flag('MULTILINE_INLINE_MATH', match.start(), 'Use an independent display block')
    for match in re.finditer(r'!\[([^\]]*)\]\(([^\n]+?)\)', text):
        alt, destination = match.groups()
        if not alt.strip():
            flag('EMPTY_ALT', match.start(), 'Image has no alternative text')
        destination = destination.strip('<>')
        if destination.startswith(('/home/', '/Users/')):
            flag('LOCAL_IMAGE', match.start(), destination)
        elif not re.match(r'[a-zA-Z]+:|#', destination):
            target = path.parent / unquote(destination.split('#')[0])
            if not target.exists():
                flag('MISSING_IMAGE', match.start(), destination)
    # Preserve offsets while excluding destinations, then inline math.
    text = re.sub(r'(?<=\]\()([^\n]*?)(?=\))', mask, text)
    text = re.sub(r'(?<!\\)\$(?!\$)[^$\n]+?(?<!\\)\$', mask, text)
    patterns = {
        'UNMATCHED_DOLLAR': r'(?<!\\)\$',
        'PDF_COMMAND': r'\\(?:clearpage|newpage)\b',
        'LATEX_IN_PROSE': r'\\(?:text|mathrm|xrightarrow|mathstrut|begin|end|alpha|beta|gamma|pi|sigma)\b',
        'PANDOC_SCRIPT': r'\^[^\s^]+\^|(?<!~)~[^\s~]+~(?!~)',
        'INVALID_CHARACTER': r'\ufffd|[\u200b\u200c\u200d\ufeff]',
    }
    for code, pattern in patterns.items():
        for match in re.finditer(pattern, text):
            flag(code, match.start(), match[0])
    if len(re.findall(r'(?<!\\)\*\*', text)) % 2:
        flag('UNBALANCED_BOLD', 0, 'Odd number of bold markers outside code/math')
    offset = 0
    for paragraph in re.split(r'(\n\s*\n)', text):
        if len(re.findall(r'(?<!\\)\*\*', paragraph)) % 2:
            flag('UNBALANCED_BOLD_PARAGRAPH', offset, 'Bold cannot cross paragraph boundaries')
        offset += len(paragraph)
    return findings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', type=Path)
    parser.add_argument('--min-lecture', type=int, default=11)
    parser.add_argument('--report', type=Path)
    parser.add_argument('--json', type=Path)
    parser.add_argument('--github', action='store_true',
                        help='Also send each document to GitHub Markdown API (requires authenticated gh)')
    args = parser.parse_args()
    if not args.root.exists():
        parser.error(f'Path does not exist: {args.root}')
    files = [args.root] if args.root.is_file() else sorted(args.root.rglob('*.md'))
    files = [p for p in files if (m := re.match(r'L(\d+)', p.name)) and int(m[1]) >= args.min_lecture]
    if not files:
        parser.error('No lecture Markdown files matched the requested range')
    findings = [item for p in files for item in audit(p)]
    maths = 0
    if args.github:
        try:
            for path in files:
                count, extra = audit_github(path)
                maths += count
                findings.extend(extra)
        except (OSError, subprocess.CalledProcessError) as error:
            parser.error(f'GitHub Markdown API failed: {error}')
    report = '# Markdown source audit\n\n'
    report += f'Files: {len(files)}; findings: {len(findings)}\n\n'
    if args.github:
        report += f'GitHub parser: {maths} math components recognized.\n\n'
    report += '| File | Line | Code | Detail |\n|---|---:|---|---|\n'
    for item in findings:
        report += '| {file} | {line} | {code} | {detail} |\n'.format(**{k:str(v).replace('|', '\\|') for k,v in item.items()})
    report += '\nSource checks do not certify GitHub/Obsidian rendering or heading/figure semantics.\n'
    print(report, end='')
    if args.report:
        args.report.write_text(report)
    if args.json:
        args.json.write_text(json.dumps(dict(files=[str(p) for p in files], findings=findings), ensure_ascii=False, indent=2))
    return bool(findings)


if __name__ == '__main__':
    raise SystemExit(main())
