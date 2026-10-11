# CM3121 고급 유기화학 학습 노트

NUS CM3121 Advanced Organic Chemistry(Dr. Zhu Ye) 강의 자료를 바탕으로 만든 한국어 학습 노트다. 나무위키처럼 읽히도록 서술형으로 썼으며, 각 문서 끝에 연습 문제와 해설을 붙였다. 모든 소절에는 근거 슬라이드가 `(출처: L# p.N)` 형식으로 표기되어 있다. 여기서 p.N은 PDF 페이지 번호이며, 슬라이드에 인쇄된 번호와 1쪽 차이가 날 수 있다.

## 강의 노트 (`notes/`)

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

시험 범위는 수정된 일정표(Revised schedule) 기준이다. Test 1은 1–5주차, Test 2는 6–10주차를 다루며 라디칼 화학은 Test 2에서 제외된다.

## 연습 문제와 기출 (`practice/`)

- [Test 1 (2025) 문제 및 해설](practice/Test1_2025.md): 출제 경향 분석 포함
- [Tutorial 1](practice/Tutorial_1.md), [Tutorial 2](practice/Tutorial_2.md), [Tutorial 3](practice/Tutorial_3.md): 공식 풀이와 해설
- [Tutorial 4](practice/Tutorial_4.md): 공식 답이 없어 풀이를 제안함 (불확실한 부분 표시)
- [L10 Practice](practice/L10_Practice.md), [L12 Practice](practice/L12_Practice.md)

공식 풀이에 의문이 있는 곳은 답을 바꾸지 않고 "검토 의견:"으로 따로 적었다.

## 그림 (`figures/`, `tools/chemfig.py`)

반응 메커니즘 그림은 [ReShiki](https://reshiki.com/)로 그린다. 그림 하나는 JSON 스펙 하나로 정의되며, 원자 좌표, 결합, 굽은 화살표(전자쌍/전자 하나), 비공유 전자쌍, 색 강조를 담는다. 이를 `tools/chemfig.py`가 ReShiki 네이티브 문서(.rsk)로 만든 뒤 SVG로 렌더링한다.

- SVG는 `prefers-color-scheme`을 따르므로 **다크 모드에서는 밝은 선으로 자동 전환**된다.
- 색 규칙: 파랑은 친핵체(전자 주는 쪽), 빨강은 친전자체(전자 받는 쪽), 주황은 전자 이동 화살표, 회색은 설명이다.

```bash
export RESHIKI=/path/to/reshiki        # ReShiki 실행 파일 (Linux x64 nightly에서 확인)
python3 tools/chemfig.py figures/L01/bromonium_step1.json
```
