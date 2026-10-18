# L8. 알돌 반응 (Aldol Reactions)

<!-- wiki-links:start -->

> **관련 위키 문서** ([위키 대문](../wiki/위키%20대문.md))
> - 반응: [aldol reaction](../wiki/반응/알돌%20반응.md), [crossed aldol reaction](../wiki/반응/교차%20알돌%20반응.md), [Henry reaction](../wiki/반응/헨리%20반응.md), [Horner–Wadsworth–Emmons reaction](../wiki/반응/HWE%20반응.md), [intramolecular aldol reaction](../wiki/반응/분자내%20알돌%20반응.md), [Knoevenagel condensation](../wiki/반응/크뇌베나겔%20축합.md), [Michael reaction](../wiki/반응/마이클%20반응.md), [Mukaiyama aldol reaction](../wiki/반응/무카이야마%20알돌%20반응.md), [retro-aldol reaction](../wiki/반응/역알돌%20반응.md)
> - 시약: [alkoxide base](../wiki/시약/알콕사이드%20염기.md), [LDA](../wiki/시약/LDA.md), [silyl enol ether](../wiki/시약/실릴%20엔올%20에터.md), [TiCl4](../wiki/시약/TiCl4.md)
> - 개념: [alpha-hydrogen acidity](../wiki/개념/α-수소의%20산도.md), [carbocation](../wiki/개념/탄소%20양이온.md), [E1cB elimination](../wiki/개념/E1cB%20제거.md), [enol and enolate](../wiki/개념/엔올과%20엔올레이트.md), [enolate chemistry (overview)](../wiki/개념/엔올레이트%20화학%20개관.md), [hard and soft acids and bases (HSAB)](../wiki/개념/하드-소프트%20산염기.md), [kinetic vs thermodynamic control](../wiki/개념/속도론적%20지배와%20열역학적%20지배.md), [kinetic vs thermodynamic enolate](../wiki/개념/속도론적%20엔올레이트와%20열역학적%20엔올레이트.md), [oxaphosphetane](../wiki/개념/옥사포스페테인.md)

<!-- wiki-links:end -->

> 이 강의 노트는 **뼈대**다. 강의 순서와 슬라이드 위치만 정리했고, 설명은 링크된 개념 문서에 있다.

> 강의 흐름대로 길게 읽고 싶으면 **[통독본](통독/L08_Aldol_Reactions.md)**(재구성 직전의 전체 노트, 소절마다 개념 문서 링크 포함)을 본다.

> CM3121 Advanced Organic Chemistry, Dr. Zhu Ye. 참고 교재: Solomons 13판 19장, Clayden 2판 26장. 이 강의 PDF는 34쪽이며 "p."는 PDF 페이지 번호다.

## 개요

aldol reaction은 enolate 또는 enol이 aldehyde나 ketone의 carbonyl 탄소를 공격해 $\beta$-hydroxy carbonyl 화합물을 만드는 반응이다. L7에서 enolate의 상대가 alkyl halide이었다면, 이번에는 carbonyl 화합물로 바꾼 셈이다. 강의는 천연물과 HWE 복습으로 aldol의 의미를 보여 준 뒤, 염기성·산성 조건의 기본 aldol과 그 retro-aldol을 다룬다. 이어 강의의 절반을 crossed aldol을 제어하는 세 가지 방법(lithium enolate, silyl enol ether, 약염기)에 쓰고, intramolecular aldol과 enolate의 세 electrophile 정리로 끝난다. 전체 지도는 [enolate chemistry (overview)](../wiki/개념/엔올레이트%20화학%20개관.md)에 있다.

## 강의 흐름

### 0. 도입: 천연물, polyketide, 그리고 HWE 복습 (p.2–6)
- erythromycin, discodermolide, roflamycoin의 1,3-산소 패턴은 polyketide 생합성("enolate + carbonyl" 반복)의 결과이고, 실험실에서는 aldol로 만든다.
- HWE의 C–C 결합 형성 단계는 aldol addition과 같은 모양이다. 차이는 alkoxide가 인에 붙잡히느냐 양성자를 받느냐다.
- → [천연물과 polyketide, HWE와의 관계](../wiki/반응/알돌%20반응.md), [Horner–Wadsworth–Emmons reaction](../wiki/반응/HWE%20반응.md), [oxaphosphetane](../wiki/개념/옥사포스페테인.md)

### 1. aldol 반응이란: 정의와 강의의 지도 (p.7)
- $\begin{aligned} & \text{enolate}(\text{또는 enol}) + \text{carbonyl} \\ & \rightleftharpoons \beta\ \text{-hydroxy carbonyl} \\ & \longrightarrow \text{탈수} \end{aligned}$. 첫 단계가 가역이다.
- → [aldol reaction](../wiki/반응/알돌%20반응.md)

### 2. 염기성 조건의 aldol reaction

#### 2.1 "aldol"이라는 이름은 어디서 왔나 (p.8)
- $\begin{aligned} & 2\ \mathrm{CH_3CHO} \\ & \xrightarrow[5\,{}^\circ\mathrm{C}]{10\%\ \mathrm{NaOH}} \text{3-hydroxybutanal(50\%)},\ \text{aldehyde} + \text{alcohol} \end{aligned}$.
- → [aldol reaction](../wiki/반응/알돌%20반응.md)

#### 2.2 메커니즘: 같은 분자가 nucleophile도 되고 electrophile도 된다 (p.9)
- 일부 분자만 enolate가 되어 나머지를 공격한다. C=O는 enolate 쪽, OH는 electrophile 쪽에 남는다. 염기는 촉매량.
- → [aldol reaction](../wiki/반응/알돌%20반응.md), [enol and enolate](../wiki/개념/엔올과%20엔올레이트.md)

#### 2.3 탈수: E1cB (p.10)
- $\alpha$-H가 먼저 떨어져 enolate가 된 뒤 $\beta$-OH가 HO⁻로 떠난다. 원동력은 conjugation.
- → [E1cB elimination](../wiki/개념/E1cB%20제거.md)

#### 2.4 aldol에서 멈출까, 축합까지 갈까 (p.11)
- 강한 염기, 높은 온도, 긴 시간일수록 탈수 생성물. condensation의 정의.
- → [aldol reaction](../wiki/반응/알돌%20반응.md)

### 3. 산성 조건의 aldol reaction

#### 3.1 산에서는 거의 항상 축합까지 간다 (p.12)
- $\begin{aligned} & \text{acetone} + \mathrm{HCl} \\ & \longrightarrow \text{4-methylpent-3-en-2-one},\ \text{cyclopentanone} + \mathrm{H^+} \\ & \longrightarrow \text{2-cyclopentylidenecyclopentanone} \end{aligned}$.
- → [aldol reaction](../wiki/반응/알돌%20반응.md)

#### 3.2 메커니즘: enolate 대신 enol (p.13)
- 중성 enol이 protonate된 carbonyl을 공격한다. 탈수는 E1(carbocation 경유)로 빠르다.
- → [aldol reaction](../wiki/반응/알돌%20반응.md), [keto-enol tautomerization](../wiki/반응/케토-엔올%20토토머화.md), [carbocation](../wiki/개념/탄소%20양이온.md)

#### 3.3 손으로 풀어 보기 (p.14)
- 빈 칸 세 개 → [L8 연습 문제](../practice/L08_Exercises.md) 1–3

### 4. aldol은 거꾸로도 간다: retro-aldol reaction (p.15–16)
- 천연 benzaldehyde: $\text{cinnamaldehyde} \xrightarrow[\text{reflux}]{\mathrm{K_2CO_3}} \mathrm{PhCHO} + \mathrm{CH_3CHO}$. conjugate addition → C–C 개열.
- → [retro-aldol reaction](../wiki/반응/역알돌%20반응.md)

### 5. 교차 aldol reaction: 문제와 세 가지 해법

#### 5.1 무엇이 문제인가 (p.17)
- 둘 다 enolization되면 4가지 혼합물. 누가 nucleophile인지 강제로 정해야 한다.
- → [crossed aldol reaction](../wiki/반응/교차%20알돌%20반응.md)

#### 5.2 해법 1: lithium enolate를 미리 만든다 (directed aldol) (p.18–21)
- LDA, −78 °C로 ketone/ester를 먼저 전부 enolate로 바꾼 뒤 aldehyde를 넣는다. 비대칭 ketone은 kinetic 쪽. aldehyde enolate는 부적합. retrosynthesis는 C$\alpha$–C$\beta$를 끊는다.
- → [directed aldol](../wiki/반응/교차%20알돌%20반응.md), [LDA](../wiki/시약/LDA.md), [kinetic vs thermodynamic enolate](../wiki/개념/속도론적%20엔올레이트와%20열역학적%20엔올레이트.md)

#### 5.3 해법 2: silyl enol ether와 Mukaiyama aldol (p.22–27)
- silyl enol ether는 안정한 enol 등가체(Si–O 452 > Si–C 318 kJ/mol). TMSCl/Et₃N → thermodynamic(88 : 12), LDA; TMSCl → kinetic(1 : 99). TiCl₄로 aldehyde를 활성화해 aldol, aldehyde끼리도 가능.
- → [silyl enol ether](../wiki/시약/실릴%20엔올%20에터.md), [Mukaiyama aldol reaction](../wiki/반응/무카이야마%20알돌%20반응.md), [TiCl4](../wiki/시약/TiCl4.md)

#### 5.4 해법 3: "약한" 염기로 차이를 이용한다 (p.28–29)
- Case 1(한 짝이 훨씬 산성): 1,3-dicarbonyl(Knoevenagel), nitro메테인(Henry). Case 2(한 짝이 non-enolizable이고 더 친전자적): chalcone, pseudoionone.
- → [crossed aldol reaction](../wiki/반응/교차%20알돌%20반응.md), [Knoevenagel condensation](../wiki/반응/크뇌베나겔%20축합.md), [Henry reaction](../wiki/반응/헨리%20반응.md), [alpha-hydrogen acidity](../wiki/개념/α-수소의%20산도.md)

### 6. intramolecular aldol reaction: 고리 만들기 (p.30–32)
- $\text{dicarbonyl} \longrightarrow \text{5원/6원 고리 enone}$. 6-oxoheptanal은 C5 enolate가 aldehyde를 공격해 1-acetylcyclopentene(73%).
- lily aldehyde 합성(p.32)은 Case 2 crossed aldol 응용 → [lilial](../wiki/반응/교차%20알돌%20반응.md), [L8 연습 문제](../practice/L08_Exercises.md) 8
- → [intramolecular aldol reaction](../wiki/반응/분자내%20알돌%20반응.md)

### 7. enolate가 만나는 세 electrophile (p.33)
- $\begin{aligned} & \text{aldol}(\text{aldehyde/ketone}) \\ & \longrightarrow \beta\ \text{-hydroxy carbonyl)},\ \text{Claisen}(\text{ester}) \\ & \longrightarrow \text{1,3-dicarbonyl)},\ \text{Michael}(\alpha,\beta\ \text{-unsaturated carbonyl}) \\ & \longrightarrow \text{1,5-dicarbonyl)} \end{aligned}$.
- → [enolate chemistry (overview)](../wiki/개념/엔올레이트%20화학%20개관.md), [Claisen condensation](../wiki/반응/클라이젠%20축합.md), [Michael reaction](../wiki/반응/마이클%20반응.md)

### 8. 정리 (p.34)
- aldol은 염기·산 모두에서, crossed aldol은 세 방법으로 제어, intramolecular aldol로 고리 형성.
- → [enolate chemistry (overview)](../wiki/개념/엔올레이트%20화학%20개관.md)

## 반응 요약표

| 반응 | 시약/조건 | 생성물 | 선택성 | 비고 |
|---|---|---|---|---|
| self-[aldol](../wiki/반응/알돌%20반응.md) (CH₃CHO) | 10% NaOH, H₂O, 5 °C | 3-hydroxybutanal (50%) | 라세미 | 가역 (p.8–9) |
| 염기성 탈수 | NaOH, 더 격렬한 조건 | (E)-2-butenal | $\alpha$-H 제거, $\beta$-OH 이탈 | [E1cB](../wiki/개념/E1cB%20제거.md) (p.10–11) |
| 산성 aldol condensation | HCl (cat.) / H⁺ | 4-methylpent-3-en-2-one / 2-cyclopentylidenecyclopentanone | — | enol 경유, 탈수 E1 (p.12–13) |
| [retro-aldol](../wiki/반응/역알돌%20반응.md) | K₂CO₃, reflux | $\text{cinnamaldehyde} \longrightarrow \mathrm{PhCHO} + \mathrm{CH_3CHO}$ | conjugate addition 후 C$\alpha$–C$\beta$ 개열 | (p.16) |
| [directed aldol](../wiki/반응/교차%20알돌%20반응.md) (LDA) | (1) LDA, THF, −78 °C; (2) RCHO; (3) H₂O | $\beta$-hydroxy ketone (5-hydroxyhexan-3-one, 75%) | 덜 치환된 $\alpha$-탄소 | aldehyde enolate 부적합 (p.18–20) |
| thermodynamic [silyl enol ether](../wiki/시약/실릴%20엔올%20에터.md) | TMSCl, Et₃N (DMF, 130 °C, 66 h) | 더 치환된 TMS enol ether (88 : 12) | 더 치환된 쪽 | cation성 TS (p.22–24) |
| kinetic silyl enol ether | (i) LDA, −78 °C; (ii) TMSCl | 덜 치환된 TMS enol ether (99 : 1) | 덜 치환된 쪽 | (p.24) |
| [Mukaiyama aldol](../wiki/반응/무카이야마%20알돌%20반응.md) | silyl enol ether + RCHO, TiCl₄; H₂O | $\beta$-hydroxy carbonyl | enol ether C=C 위치 | Lewis acid 필수 (p.25–27) |
| [Knoevenagel](../wiki/반응/크뇌베나겔%20축합.md) | CH₂(CO₂Et)₂, R₂NH, HOAc | (CH₃)₂CHCH=C(CO₂Et)₂ (92%) | 산성 CH₂만 | (p.28) |
| [Henry](../wiki/반응/헨리%20반응.md) | CH₃NO₂, NaOH, MeOH | (E)-PhCH=CHNO₂ (85%) / 1-(nitromethyl)cyclohexanol (70%) | CH₃NO₂만 | (p.28) |
| $\alpha$-H 없는 aldehyde와 교차 | PhCHO + PhCOCH₃, HO⁻ / geranial + acetone, EtONa | (E)-chalcone (85%) / pseudoionone (49%) | ketone이 nucleophile | (p.29) |
| [intramolecular aldol](../wiki/반응/분자내%20알돌%20반응.md) | HO⁻ 또는 H₂SO₄ | 1-acetylcyclopentene (73%), 1-(2-methylcyclohex-1-enyl)ethanone (85%) | 5/6원 고리, aldehyde 우선 | (p.30–31) |

## 연습 문제

→ [L8 연습 문제와 해설](../practice/L08_Exercises.md)

## 출처

- 슬라이드: L8 (PDF p.1–34)
