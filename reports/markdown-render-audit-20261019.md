# L11–L17 Markdown 렌더링 검수 (2026-10-19)

현재 Git 브랜치의 `notes/통독/L11`부터 `L17`까지 7문서를 검사했다. Dropbox의 E/F 통합본은 이번 수정 대상에 포함하지 않았다.

## 확인한 결함과 수정

- L11 3.2에서 반응 뒤에 붙어 있던 1,2/1,4 표제를 각 반응 앞의 소제목으로 바꿨다. 두 개의 1,2 그림과 캡션은 1,2 소절에 배치했다. 이 구간의 중복 LaTeX 반응식 두 개는 시약·생성물·수율 목록으로 바꿨다.
- L11 3.1의 네 기질 그림도 각각 해당 반응 소제목 아래로 이동했다. 네 그림이 마지막 cyclopentenone 소절에 모여 있던 상태를 해소했다.
- 블록 수식 앞뒤에 빈 줄을 넣고, inline `aligned` 반응식은 독립 블록으로 분리했다. 설명 문장·문제 지시문을 `aligned` 안에 넣은 사례는 일반 본문으로 복원했다.
- 닫히지 않은 강조 표시를 고치고, 괄호·문장부호와 한글 조사가 붙어 GitHub에서 `**`가 노출되던 강조 구간을 정리했다.
- 연속 수식의 경계를 정리했다. 별표는 `\ast`로 표기하여 Markdown 강조 문법과 충돌하지 않게 했다.
- GitHub Markdown API는 링크 글자와 각주 안의 수식을 변환하지 않았다. 해당 위치는 beta, sigma 등의 영어 이름으로 표기했다. 본문의 그리스 문자는 LaTeX를 유지했다. 목록 생성기도 링크 글자에 수식을 재삽입하지 않도록 고쳤다.
- GitHub API가 display math 안의 `\\`, `\,`, `\!`, `\%` 등을 Markdown 이스케이프로 처리하는 사례를 확인했다. 해당 블록의 행 구분에는 MathJax에서 검증한 `\cr`, 간격에는 `\thinspace`와 `\negthinspace`를 사용했다. 수율은 해당 수식에서 percent로 풀어 썼다.

[GitHub 공식 수식 문법](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions)에 따라 display math는 본문과 독립된 블록으로 유지했다. Obsidian과 공유하기 위해 `$$` 구분자를 유지했다.

## 검사 결과

| 검사 | 범위 | 결과 |
|---|---|---|
| 정적 소스 검사 | 통독 7문서 | 지적 항목 0 |
| GitHub 실제 Markdown API | 통독 7문서 전체 원문 | math component 1,254개; 수식 바깥에 남은 `$`, LaTeX 명령, `**` 0 |
| GitHub 반환 HTML + 로컬 MathJax | 7문서 × dark/light = 14개 화면 구성 | 수식 오류 0, 이미지 로딩 실패 0, 820 CSS px 초과 수식 0 |
| 위키 인덱스 생성 | 위키 181문서 | 깨진 링크 0 |
| 도구 회귀 검사 | unittest 7개 메서드, 결함별 subtest 포함 | 통과 |

현재 통독 7문서에서는 PDF 전용 페이지 명령, 절대 로컬 이미지 경로, 빈 이미지 대체 텍스트가 발견되지 않았다. 기반 통합본에 있다는 사실을 현재 파일에도 있다는 뜻으로 취급하지 않았다.

그림의 소절 배치는 제목·대체 텍스트·캡션 목록으로 대조했고 L11의 잘못된 배치를 수정했다. 이번 작업은 모든 그림 내부의 화학 구조와 전자 이동을 새로 검증한 검수가 아니다.

## 재검수와 한계

```bash
python3 tools/audit_markdown_render.py notes/통독 --min-lecture 11 --report /tmp/ochem-markdown-audit.md
python3 tools/audit_markdown_render.py notes/통독 --min-lecture 11 --github
python3 tools/build_wiki_index.py
python3 -m unittest discover -s tools -p 'test_*.py'
git diff --check
```

정적 검수기는 실제 렌더러의 문법 처리를 모두 예측하지 못한다. 이번에는 정적 검사에 더해 `gh api markdown`에 문서 전체를 전달하여 GitHub의 실제 파서 출력을 검사했다. 그 결과의 math component를 로컬 MathJax로 렌더링했으며, 이미지 경로만 로컬 검사용 절대 경로로 치환했다. 이는 GitHub 웹 UI 자체의 브라우저 검사나 실제 Obsidian 앱 검사는 아니다. 모바일 화면도 이번 결과에 포함하지 않는다.
