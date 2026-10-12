# L8. 알돌 반응 (Aldol Reactions)

<!-- wiki-links:start -->

> **관련 위키 문서** ([[위키 대문]])
> - 반응: [[교차 알돌 반응]], [[무카이야마 알돌 반응]], [[분자내 알돌 반응]], [[알돌 반응]], [[역알돌 반응]], [[크뇌베나겔 축합]], [[헨리 반응]]
> - 시약: [[LDA]], [[TiCl4]], [[실릴 엔올 에터]], [[알콕사이드 염기]]
> - 개념: [[E1cB 제거]], [[α-수소의 산도]], [[속도론적 엔올레이트와 열역학적 엔올레이트]], [[속도론적 지배와 열역학적 지배]], [[엔올과 엔올레이트]], [[옥사포스페테인]], [[탄소 양이온]]

<!-- wiki-links:end -->

> 이 강의 노트는 **뼈대**다. 강의 순서와 슬라이드 위치만 정리했고, 설명은 링크된 개념 문서에 있다.

> CM3121 Advanced Organic Chemistry, Dr. Zhu Ye. 참고 교재: Solomons 13판 19장, Clayden 2판 26장. 이 강의 PDF는 34쪽이며 "p."는 PDF 페이지 번호다.

## 개요

aldol reaction은 enolate 또는 enol이 알데하이드나 케톤의 카보닐 탄소를 공격해 β-hydroxy carbonyl 화합물을 만드는 반응이다. L7에서 enolate의 상대가 할로젠화 알킬이었다면, 이번에는 카보닐 화합물로 바꾼 셈이다. 강의는 천연물과 HWE 복습으로 aldol의 의미를 보여 준 뒤, 염기성·산성 조건의 기본 aldol과 그 역반응(retro-aldol)을 다룬다. 이어 강의의 절반을 crossed aldol을 제어하는 세 가지 방법(lithium enolate, silyl enol ether, 약염기)에 쓰고, intramolecular aldol과 enolate의 세 electrophile 정리로 끝난다. 전체 지도는 [[엔올레이트 화학 개관]]에 있다.

## 강의 흐름

### 0. 도입: 천연물, 폴리케타이드, 그리고 HWE 복습 (p.2–6)
- erythromycin, discodermolide, roflamycoin의 1,3-산소 패턴은 polyketide 생합성("enolate + 카보닐" 반복)의 결과이고, 실험실에서는 aldol로 만든다.
- HWE의 C–C 결합 형성 단계는 aldol addition과 같은 모양이다. 차이는 alkoxide가 인에 붙잡히느냐 양성자를 받느냐다.
- → [[알돌 반응|천연물과 polyketide, HWE와의 관계]], [[HWE 반응]], [[옥사포스페테인]]

### 1. 알돌 반응이란: 정의와 강의의 지도 (p.7)
- enolate(또는 enol) + 카보닐 ⇌ β-하이드록시 카보닐 → 탈수. 첫 단계가 가역이다.
- → [[알돌 반응]]

### 2. 염기성 조건의 알돌 반응

#### 2.1 "aldol"이라는 이름은 어디서 왔나 (p.8)
- 2 CH₃CHO --[10% NaOH, 5 °C]--> 3-hydroxybutanal(50%), aldehyde + alcohol.
- → [[알돌 반응]]

#### 2.2 메커니즘: 같은 분자가 친핵체도 되고 친전자체도 된다 (p.9)
- 일부 분자만 enolate가 되어 나머지를 공격한다. C=O는 enolate 쪽, OH는 electrophile 쪽에 남는다. 염기는 촉매량.
- → [[알돌 반응]], [[엔올과 엔올레이트]]

#### 2.3 탈수: E1cB (p.10)
- α-H가 먼저 떨어져 enolate가 된 뒤 β-OH가 HO⁻로 떠난다. 원동력은 conjugation.
- → [[E1cB 제거]]

#### 2.4 알돌에서 멈출까, 축합까지 갈까 (p.11)
- 강한 염기, 높은 온도, 긴 시간일수록 탈수 생성물. condensation의 정의.
- → [[알돌 반응]]

### 3. 산성 조건의 알돌 반응

#### 3.1 산에서는 거의 항상 축합까지 간다 (p.12)
- 아세톤 + HCl → 4-methylpent-3-en-2-one, 사이클로펜탄온 + H⁺ → 2-cyclopentylidenecyclopentanone.
- → [[알돌 반응]]

#### 3.2 메커니즘: 엔올레이트 대신 엔올 (p.13)
- 중성 enol이 양성자화된 카보닐을 공격한다. 탈수는 E1(carbocation 경유)로 빠르다.
- → [[알돌 반응]], [[케토-엔올 토토머화]], [[탄소 양이온]]

#### 3.3 손으로 풀어 보기 (p.14)
- 빈 칸 세 개 → [L8 연습 문제](../practice/L08_Exercises.md) 1–3

### 4. 알돌은 거꾸로도 간다: 역알돌 반응 (p.15–16)
- 천연 벤즈알데하이드: cinnamaldehyde --[K₂CO₃, reflux]--> PhCHO + CH₃CHO. conjugate addition → C–C 개열.
- → [[역알돌 반응]]

### 5. 교차 알돌 반응: 문제와 세 가지 해법

#### 5.1 무엇이 문제인가 (p.17)
- 둘 다 enol화되면 4가지 혼합물. 누가 nucleophile인지 강제로 정해야 한다.
- → [[교차 알돌 반응]]

#### 5.2 해법 1: 리튬 엔올레이트를 미리 만든다 (directed aldol) (p.18–21)
- LDA, −78 °C로 케톤/에스터를 먼저 전부 enolate로 바꾼 뒤 알데하이드를 넣는다. 비대칭 케톤은 kinetic 쪽. 알데하이드 enolate는 부적합. retrosynthesis는 Cα–Cβ를 끊는다.
- → [[교차 알돌 반응|directed aldol]], [[LDA]], [[속도론적 엔올레이트와 열역학적 엔올레이트]]

#### 5.3 해법 2: 실릴 엔올 에터와 Mukaiyama 알돌 (p.22–27)
- silyl enol ether는 안정한 enol 등가체(Si–O 452 > Si–C 318 kJ/mol). TMSCl/Et₃N → thermodynamic(88 : 12), LDA; TMSCl → kinetic(1 : 99). TiCl₄로 알데하이드를 활성화해 aldol, 알데하이드끼리도 가능.
- → [[실릴 엔올 에터]], [[무카이야마 알돌 반응]], [[TiCl4]]

#### 5.4 해법 3: "약한" 염기로 차이를 이용한다 (p.28–29)
- Case 1(한 짝이 훨씬 산성): 1,3-다이카보닐(Knoevenagel), 나이트로메테인(Henry). Case 2(한 짝이 non-enolizable이고 더 친전자적): chalcone, pseudoionone.
- → [[교차 알돌 반응]], [[크뇌베나겔 축합]], [[헨리 반응]], [[α-수소의 산도]]

### 6. 분자내 알돌 반응: 고리 만들기 (p.30–32)
- 다이카보닐 → 5원/6원 고리 enone. 6-oxoheptanal은 C5 enolate가 알데하이드를 공격해 1-acetylcyclopentene(73%).
- lily aldehyde 합성(p.32)은 Case 2 crossed aldol 응용 → [[교차 알돌 반응|lilial]], [L8 연습 문제](../practice/L08_Exercises.md) 8
- → [[분자내 알돌 반응]]

### 7. 엔올레이트가 만나는 세 친전자체 (p.33)
- aldol(알데하이드/케톤 → β-하이드록시 카보닐), Claisen(에스터 → 1,3-다이카보닐), Michael(α,β-불포화 카보닐 → 1,5-다이카보닐).
- → [[엔올레이트 화학 개관]], [[클라이젠 축합]], [[마이클 반응]]

### 8. 정리 (p.34)
- aldol은 염기·산 모두에서, crossed aldol은 세 방법으로 제어, intramolecular aldol로 고리 형성.
- → [[엔올레이트 화학 개관]]

## 반응 요약표

| 반응 | 시약/조건 | 생성물 | 선택성 | 비고 |
|---|---|---|---|---|
| self-[[알돌 반응\|aldol]] (CH₃CHO) | 10% NaOH, H₂O, 5 °C | 3-hydroxybutanal (50%) | 라세미 | 가역 (p.8–9) |
| 염기성 탈수 | NaOH, 더 격렬한 조건 | (E)-2-butenal | α-H 제거, β-OH 이탈 | [[E1cB 제거\|E1cB]] (p.10–11) |
| 산성 aldol condensation | HCl (cat.) / H⁺ | 4-methylpent-3-en-2-one / 2-cyclopentylidenecyclopentanone | — | enol 경유, 탈수 E1 (p.12–13) |
| [[역알돌 반응\|retro-aldol]] | K₂CO₃, reflux | cinnamaldehyde → PhCHO + CH₃CHO | 공액 첨가 후 Cα–Cβ 개열 | (p.16) |
| [[교차 알돌 반응\|directed aldol]] (LDA) | (1) LDA, THF, −78 °C; (2) RCHO; (3) H₂O | β-하이드록시 케톤 (5-hydroxyhexan-3-one, 75%) | 덜 치환된 α-탄소 | 알데하이드 enolate 부적합 (p.18–20) |
| thermodynamic [[실릴 엔올 에터\|silyl enol ether]] | TMSCl, Et₃N (DMF, 130 °C, 66 h) | 더 치환된 TMS enol ether (88 : 12) | 더 치환된 쪽 | 양이온성 TS (p.22–24) |
| kinetic silyl enol ether | (i) LDA, −78 °C; (ii) TMSCl | 덜 치환된 TMS enol ether (99 : 1) | 덜 치환된 쪽 | (p.24) |
| [[무카이야마 알돌 반응\|Mukaiyama aldol]] | silyl enol ether + RCHO, TiCl₄; H₂O | β-하이드록시 카보닐 | enol ether C=C 위치 | Lewis acid 필수 (p.25–27) |
| [[크뇌베나겔 축합\|Knoevenagel]] | CH₂(CO₂Et)₂, R₂NH, HOAc | (CH₃)₂CHCH=C(CO₂Et)₂ (92%) | 산성 CH₂만 | (p.28) |
| [[헨리 반응\|Henry]] | CH₃NO₂, NaOH, MeOH | (E)-PhCH=CHNO₂ (85%) / 1-(nitromethyl)cyclohexanol (70%) | CH₃NO₂만 | (p.28) |
| α-H 없는 알데하이드와 교차 | PhCHO + PhCOCH₃, HO⁻ / geranial + 아세톤, EtONa | (E)-chalcone (85%) / pseudoionone (49%) | 케톤이 nucleophile | (p.29) |
| [[분자내 알돌 반응\|intramolecular aldol]] | HO⁻ 또는 H₂SO₄ | 1-acetylcyclopentene (73%), 1-(2-methylcyclohex-1-enyl)ethanone (85%) | 5/6원 고리, 알데하이드 우선 | (p.30–31) |

## 연습 문제

→ [L8 연습 문제와 해설](../practice/L08_Exercises.md)

## 출처

- 슬라이드: L8 (PDF p.1–34)
