# CM3121 고급 유기화학 학습 노트

NUS CM3121 Advanced Organic Chemistry(Dr. Zhu Ye) 강의 자료를 바탕으로 만든 한국어 학습 노트다. **설명은 반응·시약·개념별 문서(`wiki/`)에 모여 있고**, 강의 노트(`notes/`)는 강의 순서와 슬라이드 위치를 따라 그 문서들로 안내하는 뼈대다. 나무위키처럼 읽히도록 서술형으로 썼고, 주요 용어는 영어로 적었다. 모든 내용에는 근거 슬라이드가 `(출처: L# p.N)` 형식으로 표기되어 있다. 여기서 p.N은 PDF 페이지 번호이며, 슬라이드에 인쇄된 번호와 1쪽 차이가 날 수 있다.

**어디서부터 읽나**: [위키 대문](wiki/위키%20대문.md)의 "단원별 시작점" 표에서 단원 개관이나 핵심 문서를 연다. 시험 직전에는 [Test 2 범위](wiki/Test%202%20범위.md)를, 강의 순서대로 훑고 싶으면 아래 강의 노트(뼈대)를 본다.

## 옵시디언으로 보기

이 저장소는 그대로 [옵시디언(Obsidian)](https://obsidian.md/) 볼트로 쓸 수 있다.

1. GitHub에서 **Code → Download ZIP**으로 받아 압축을 풀거나 `git clone`한다.
2. 옵시디언에서 **Open folder as vault**로 저장소 폴더(이 README가 있는 폴더)를 연다.
3. 이 README가 목차 역할을 한다. 노트 사이의 교차 참조(예: "→ L9")는 링크라서 클릭하면 이동하고, 그래프 뷰와 백링크에도 나타난다.

모든 링크는 상대 경로 마크다운 링크라서 **GitHub 웹에서도** README → 위키 대문 → 개념 문서 → 옆 개념 문서 순으로 클릭해 이동할 수 있다.

볼트 설정(`.obsidian/`)에는 다크 테마, 상대 경로 마크다운 링크, `tools/` 폴더 숨김이 기본값으로 들어 있다. 기기마다 달라지는 작업 공간 파일(`workspace.json`)은 저장소에 넣지 않는다. 그림(SVG)은 라이트/다크에 맞춘 배경 카드를 가지고 있어서, 옵시디언 테마와 운영체제의 다크/라이트 설정이 서로 달라도 읽힌다.

## 개념 문서: 반응·시약·개념별 위키 (`wiki/`, 본문)

이 노트의 본문이다. 반응, 시약, 개념 하나마다 문서 하나를 두고, 여러 강의에 흩어진 설명(메커니즘, "왜?", 예, 각주, 교과서 보충, 검토 의견, 그림)을 그 문서에 모았다. "브로모늄 이온"이나 "LDA"처럼 필요한 항목만 찾아 읽고, 링크를 따라 옆 문서로 넘어가며 공부할 수 있다. 각 문서는 한 줄 요약, 개요, 메커니즘(원리), 선택성, 예, 흔한 오해, 관련 문서, 출처로 구성되며, 출처 규칙은 강의 노트와 같다.

- [위키 대문](wiki/위키%20대문.md): 단원별 시작점(개관, 핵심 문서)과 분류별 전체 목록
- [Test 1 범위](wiki/Test%201%20범위.md), [Test 2 범위](wiki/Test%202%20범위.md): 시험 범위별 문서 목록. ★는 2025 Test 1 기출 주제다.
- [인명반응 목록](wiki/인명반응%20목록.md): 인명반응, 인명시약, 인명규칙
- 각 강의 노트 맨 위에는 그 강의와 관련된 위키 문서 목록이 있다.

태그는 옵시디언 태그 창이나 검색(`tag:#범위/Test2`)으로 거를 수 있다.

| 태그 | 뜻 |
|---|---|
| `분류/반응`, `분류/시약`, `분류/개념` | 문서 종류 |
| `범위/Test1`, `범위/Test2` | 시험 범위 (L1–L10 / L11–L15) |
| `기출/Test1-2025` | 2025 Test 1에 나온 주제 |
| `인명반응`, `인명시약`, `인명규칙` | 사람 이름이 붙은 항목 |
| `단원/...`, `강의/L##` | 단원과 강의 |
| `유형/...`, `시약유형/...`, `개념유형/...` | 반응 유형(산화, 환원, C–C 결합 형성 등), 시약 유형, 개념 유형 |
| `주제/...` | 문서별 자유 태그 |

태그와 목록 문서는 `python3 tools/build_wiki_index.py`가 자동으로 만든다. 문서를 고친 뒤 다시 실행하면 되고, 깨진 링크도 함께 검사한다.

## 강의 노트 (`notes/`, 뼈대)

강의 순서대로 소절 제목, 핵심 한두 줄, 슬라이드 쪽수, 개념 문서 링크만 담았다. 각 강의의 연습 문제와 해설은 `practice/L##_Exercises.md`에 있다.

| 강의 | 주제 | 시험 범위 |
|---|---|---|
| [L1](notes/L01_Electrophilic_Addition_to_Alkenes_Part1.md) | 알켄의 친전자성 첨가 1 (브로모늄, 에폭시화, HBr, 다이엔) | Test 1 |
| [L2](notes/L02_Electrophilic_Addition_to_Alkenes_Part2.md) | 알켄의 친전자성 첨가 2 (에폭사이드 열기, 다이올, 오존 분해, 수소붕소화) | Test 1 |
| [L3](notes/L03_Electrophilic_Aromatic_Substitution_Part1.md) | 친전자성 방향족 치환 1 (나이트로화, 설폰화, 프리델-크래프츠, 페놀) | Test 1 |
| [L4](notes/L04_Electrophilic_Aromatic_Substitution_Part2.md) | 친전자성 방향족 치환 2 (배향 효과, 치환기 경쟁, NMR) | Test 1 |
| [L5](notes/L05_Reduction.md) | 환원 (아민 합성, 금속 수소화물, 촉매 수소화) | Test 1 |
| [L6](notes/L06_Oxidation_and_Alkene_Synthesis.md) | 산화와 알켄 합성 (알코올 산화, 위티그, HWE), 정정판 슬라이드 기준 | Test 1 |
| [L7](notes/L07_Enolate_Alkylation.md) | 엔올레이트 알킬화 | Test 1 |
| [L8](notes/L08_Aldol_Reactions.md) | 알돌 반응 | Test 1 |
| [L9](notes/L09_Claisen_Condensation.md) | 클라이젠 축합 | Test 1 |
| [L10](notes/L10_Enol_and_Enamine.md) | 엔올과 엔아민 | Test 1 |
| [L11](notes/L11_Conjugate_Addition.md) | 공액 첨가 | Test 2 |
| [L12](notes/L12_Protecting_Groups.md) | 보호기 | Test 2 |
| [L13](notes/L13_Cycloaddition_Part1.md) | 고리화 첨가 1 (딜스-알더 기초, FMO) | Test 2 |
| [L14](notes/L14_Cycloaddition_Part2.md) | 고리화 첨가 2 (위치선택성, 루이스 산 촉매, [2+2] 등) | Test 2 |
| [L15](notes/L15_Cycloaddition_Part3.md) | 고리화 첨가 3 (케텐 [2+2], 1,3-쌍극자 고리화 첨가) | Test 2 |
| [L16](notes/L16_Sigmatropic_Rearrangements.md) | 시그마트로픽 자리옮김 (예습판: Clayden 35장 기반, 슬라이드 공개 후 갱신) | Test 2 |
| [L17](notes/L17_Electrocyclic_Reactions.md) | 전자고리화 반응 (예습판: Clayden 35장 기반, 슬라이드 공개 후 갱신) | Test 2 |

시험 범위는 수정된 일정표(Revised schedule) 기준이다. Test 1은 1–5주차, Test 2는 6–10주차를 다루며 라디칼 화학은 Test 2에서 제외된다.

## 교과서와 강의 대응

노트의 "보충:" 서술은 표준 교재와 대조해 `(보충 근거: Clayden p.N)` 또는 `(보충 근거: Wade p.N)`으로 근거를 단다. 교과서 쪽수는 **책에 인쇄된 쪽수**다(슬라이드 출처의 p.N이 PDF 쪽수인 것과 다르다). PDF로 열 때는 Clayden 2판은 인쇄 쪽 + 27, Wade 8판은 인쇄 쪽 + 38이 PDF 쪽이다.

| 강의 | Clayden 2판 (장, 시작 쪽) | Wade 8판 (장, 시작 쪽) |
|---|---|---|
| L1–L2 알켄 첨가 | 19장 Electrophilic addition to alkenes (p.427) | 8장 Reactions of Alkenes (p.328) |
| L3–L4 방향족 치환 | 21장 Electrophilic aromatic substitution (p.471) | 17장 Reactions of Aromatic Compounds (p.756) |
| L5 환원 | 23장 Chemoselectivity and protecting groups (p.528), 6·10·11장 | 18장 Ketones and Aldehydes (p.816), 19장 Amines (p.879) |
| L6 산화·알켄 합성 | 23장 (p.528), 위티그는 11장 (p.237)과 27장 S, Si, P (p.656) | 11장 Reactions of Alcohols (p.467), 18장 |
| L7 엔올레이트 알킬화 | 25장 Alkylation of enolates (p.584) | 22장 Condensations and Alpha Substitutions (p.1045) |
| L8–L9 알돌·클라이젠 | 26장 Aldol and Claisen reactions (p.614) | 22장 (p.1045) |
| L10 엔올·엔아민 | 20장 Enols and enolates (p.449), 25장 | 22장 (p.1045) |
| L11 공액 첨가 | 22장 Conjugate addition and SNAr (p.498) | 22장, 17장 |
| L12 보호기 | 23장 (p.528) | 24장 Amino Acids, Peptides (p.1155) |
| L13–L15 고리화 첨가 | 34장 Pericyclic reactions 1 (p.877) | 15장 Conjugated Systems, Orbital Symmetry (p.667) |
| Test 2: 시그마트로픽·전자고리화 | 35장 Pericyclic reactions 2 (p.909) | 15장 |

교과서 PDF(`Clayden-...pdf`, `Wade ...pdf`)는 저장소 루트에 있다.

## 연습 문제와 기출 (`practice/`)

- [Test 1 (2025) 문제 및 해설](practice/Test1_2025.md): 출제 경향 분석 포함
- [Tutorial 1](practice/Tutorial_1.md), [Tutorial 2](practice/Tutorial_2.md), [Tutorial 3](practice/Tutorial_3.md): 공식 풀이와 해설
- [Tutorial 4](practice/Tutorial_4.md): 공식 답이 없어 풀이를 제안함 (불확실한 부분 표시)
- [L10 Practice](practice/L10_Practice.md), [L12 Practice](practice/L12_Practice.md)
- 강의별 연습 문제와 해설(노트에서 옮김): [L1](practice/L01_Exercises.md), [L2](practice/L02_Exercises.md), [L3](practice/L03_Exercises.md), [L4](practice/L04_Exercises.md), [L5](practice/L05_Exercises.md), [L6](practice/L06_Exercises.md), [L7](practice/L07_Exercises.md), [L8](practice/L08_Exercises.md), [L9](practice/L09_Exercises.md), [L10](practice/L10_Exercises.md), [L11](practice/L11_Exercises.md), [L12](practice/L12_Exercises.md), [L13](practice/L13_Exercises.md), [L14](practice/L14_Exercises.md), [L15](practice/L15_Exercises.md), [L16](practice/L16_Exercises.md), [L17](practice/L17_Exercises.md). L16–L17은 교과서 기반 자가 점검 문제다.

공식 풀이에 의문이 있는 곳은 답을 바꾸지 않고 "검토 의견:"으로 따로 적었다.

## 그림 (`figures/`, `tools/chemfig.py`)

반응 메커니즘 그림은 [ReShiki](https://reshiki.com/)로 그린다. 그림 하나는 JSON 스펙 하나로 정의되며, 원자 좌표, 결합, 굽은 화살표(전자쌍/전자 하나), 비공유 전자쌍, 색 강조를 담는다. 이를 `tools/chemfig.py`가 ReShiki 네이티브 문서(.rsk)로 만든 뒤 SVG로 렌더링한다.

- SVG는 `prefers-color-scheme`을 따르므로 **다크 모드에서는 밝은 선으로 자동 전환**된다. 배경 카드도 함께 바뀐다(라이트 #ffffff, 다크 #1e1e1e).
- 색 규칙: 파랑은 친핵체(전자 주는 쪽), 빨강은 친전자체(전자 받는 쪽), 주황은 전자 이동 화살표, 회색은 설명이다.

```bash
export RESHIKI=/path/to/reshiki        # ReShiki 실행 파일 (Linux x64 nightly에서 확인)
python3 tools/chemfig.py figures/L01/bromonium_step1.json
```
