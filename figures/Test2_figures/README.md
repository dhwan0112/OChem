# CM3121 Test 2 그림 모음 (L11–L16)

Test 2 범위(L11–L16)의 개념 그림(SVG)과 오비탈 애니메이션(GIF)을 주제별로 정리한 모음이다. SVG는 대부분 컬러판과 흑백판(`_bw`)이 한 쌍이며, 컬러판은 [STYLE.md](../STYLE.md) 색 규칙(HOMO·nucleophile 파랑, LUMO·electrophile 빨강, 전자 이동 주황, 새 결합 초록)을 따른다. `index.html`을 브라우저로 열면 전체를 한 화면에서 볼 수 있다.

## 01. L11 conjugate addition

| 파일 | 형식 | 내용 | 출처 |
|---|---|---|---|
| `L11_01_enamine_conjugate_addition_p19.svg` | SVG (컬러만) | pyrrolidine enamine + methyl 2-(methylthio)acrylate → zwitterion → H₂O → 1,5-dicarbonyl (95%) | L11 p.19; Clayden p.608 |
| `L11_02_enamine_conjugate_addition_general.svg` | SVG (컬러만) | 일반형 3단계: enamine 생성 → conjugate addition → 가수분해, 1–5 번호 | L11 p.14, 18–19 |
| `L11_03_iminium_catalysis_cycle.svg` | SVG (컬러만) | imidazolidinone 촉매 순환 4단계, (R)-생성물 | L11 p.21 |

## 02. Cycloaddition (L13–L15)

| 파일 | 형식 | 내용 | 출처 |
|---|---|---|---|
| `CY_01_DA_mechanism` | SVG 컬러/흑백 | Diels–Alder 곡선 화살표, cyclic TS, cyclohexene | L13 p.10, 19, 33–35 |
| `CY_02_FMO_allowed_vs_forbidden` | SVG 컬러/흑백 | 열적 [4+2] 허용, 열적 [2+2] 금지, 광화학 [2+2] 허용의 로브 비교 | L13 p.27–30; L14 p.24–26 |
| `CY_03_DA_orbitals.gif` | GIF | DA를 오비탈로: 양 끝 A+A, π4s + π2s, 결합 형성 | L13 p.10; L14 p.6 |
| `CY_04_EZ_diene_DA_3D.gif` | GIF | (E,Z)-diene + DMAD: inside는 위, outside는 아래 → trans | L13 p.20; Clayden p.885–886 |
| `CY_05_antarafacial_reach_2plus2.gif` | GIF | π2s + π2a: 반대 면 로브로 닿는 원리와 성분의 비틀림 | L14 p.5 |
| `CY_06_ketene_vs_alkene_2plus2.gif` | GIF | 평범한 alkene은 교차해도 상쇄, ketene은 직교 C=O π*로 순 결합 → cyclobutanone | L15 p.6–7; Clayden p.898–899 |
| `CY_07_ketene_crossed_topview` | SVG 컬러/흑백 | 위 GIF의 정지 화면 요약(위에서 본 교차 배치, 결합 4 대 반결합 2) | L15 p.6–8; Clayden p.898–899 |

## 03. Woodward–Hoffmann (세 종류 pericyclic 공통)

| 파일 | 형식 | 내용 | 출처 |
|---|---|---|---|
| `WH_01_phase_basics` | SVG 컬러/흑백 | 위상(부호) 일치, supra와 antara가 부호를 뒤집는 방식 | L13 p.27–29; L14 p.5 |
| `WH_02_MO_ladders` | SVG 컬러/흑백 | ethylene, allyl, butadiene, hexatriene MO와 양 끝 대칭 S/A | L13 p.27; L14 p.23 |
| `WH_03_SA_matching` | SVG 컬러/흑백 | S/A로 supra·antara 판정 6예 (cycloaddition 3 + sigmatropic 3) | L14 p.6, 24–25; L15 p.6–8; L16 p.21–24 |
| `WH_04_notation_table` | SVG 컬러/흑백 | π2s 같은 표기 읽는 법, 전자 수별 (4q+2)/(4r) 분류표 | L14 p.4–6; L15 p.13 |
| `WH_05_counting_rule` | SVG 컬러/흑백 | 카운팅 2×2 표와 4단계 절차 | L13 p.33–34; L14 p.4–6 |
| `WH_06_counting_examples` | SVG 컬러/흑백 | 6예의 면 그림과 장부 (DA, [2+2], ketene, [1,5]-H, [1,3]-H, [3,3]) | L14–L16 |
| `WH_07_examples_table` | SVG 컬러/흑백 | 14예 카운팅 표 (cycloaddition 7, sigmatropic 5, electrocyclic 2) | L14–L16; Clayden p.918, 922–924 |

## 04. Sigmatropic (L16)

| 파일 | 형식 | 내용 | 출처 |
|---|---|---|---|
| `SG_01_1-7H_shift_antarafacial.gif` | GIF | 열적 [1,7]-H 이동: triene이 나선으로 비틀려 σ2s + π6a | L16 p.21–24 |

## 추천 순서

1. W–H 기초: `WH_01` → `WH_02` → `WH_03` → `WH_04` → `WH_05` → `WH_06` → `WH_07`
2. 비틀 필요가 없는 경우: `CY_01` → `CY_02` → `CY_03`
3. 비틀어야 하는 경우: `CY_05` → `CY_06` → `CY_07` (cycloaddition), `SG_01` (sigmatropic)
4. 입체화학: `CY_04`

## 주의

- 대문자 S/A(양 끝 대칭)는 설명용 표기이고 강의 표기가 아니다. 답안에는 소문자 s/a와 (4q+2)/(4r) 카운팅을 쓴다.
- GIF의 분자 기하는 결합 길이만 맞춘 도식이다. 로브 크기는 Hückel 계수를 반영한 것도 있고 위상만 보인 것도 있다(각 그림 하단 설명 참고).
- L11 그림 세 장은 초기에 만든 것이라 흑백판이 없고 색 규칙이 뒤의 그림과 조금 다르다.
- tropone + cyclopentadiene [6+4]의 endo 표기는 슬라이드와 문헌이 엇갈린다(통독본 L14 각주 [5]). 이 모음에는 그림이 없다.
