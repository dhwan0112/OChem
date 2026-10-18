---
aliases: [N-methylmorpholine N-oxide, N-메틸모폴린 N-옥사이드, NMMO, 공산화제, co-oxidant, terminal oxidant]
분류: 시약
강의: [L2, L6]
주제태그: [산화제, 공산화제, 촉매-재생]
tags: [분류/시약, 범위/Test1, 기출/Test1-2025, 단원/산화-알켄-합성, 단원/알켄-첨가, 강의/L02, 강의/L06, 시약유형/산화제, 주제/공산화제, 주제/촉매-재생]
---
# NMO

> *N*-methyl모폴린 *N*-oxide. 스스로 기질을 산화하기보다는 **값비싼 금속 산화제를 촉매량만 쓰도록 금속을 다시 산화해 주는 공산화제(최종 산화제)**다. [OsO₄](OsO4.md) dihydroxylation과 [TPAP](TPAP.md) 산화에 짝으로 붙는다.

## 개요

OsO₄는 비싸고 독성이 강하다. 그래서 실제로는 OsO₄를 촉매량만 넣고, 반응 뒤 환원된 오스뮴을 NMO가 다시 산화해 촉매를 돌린다. TPAP(Pr₄N⁺ RuO₄⁻)도 같은 방식으로, 촉매량만 넣고 실제 산화 당량은 NMO가 댄다. 즉 NMO를 보면 "금속 산화제가 촉매로 돌고 있구나"라고 읽으면 된다. (출처: L2 p.14, L6c p.10)

## 원리

| 짝 | 금속이 하는 일 | NMO가 하는 일 | 출처 |
|---|---|---|---|
| cat. OsO₄ / NMO | $\text{alkene에 두 O를 syn으로 붙이고}\ \mathrm{Os(VIII)} \longrightarrow \mathrm{Os(VI)}$ | Os(VI)를 Os(VIII)로 재산화 | L2 p.14 |
| cat. TPAP / NMO (Ley–Griffith) | $\text{alcohol을 산화하고}\ \mathrm{Ru(VII)} \longrightarrow \mathrm{Ru(V)}$ | Ru(V)를 Ru(VII)로 재산화, 자신은 *N*-methyl모폴린이 됨 | L6c p.10 |

보충: NMO는 N–O 결합의 산소 하나를 금속에 넘겨주고 3차 amine(*N*-methyl모폴린)으로 환원된다. 촉매량 OsO₄ + NMO 조합은 흔히 Upjohn 조건이라 부른다. (보충 근거: Clayden p.442, p.545)

## 예

- $\begin{aligned} & \mathrm{R{-}CH_2{-}CH{=}C(CH_3)_2} \\ & \xrightarrow{\text{cat.}\ \mathrm{OsO_4},\ \mathrm{NMO},\ \mathrm{H_2O/}\ \mathit{t}\ \mathrm{{-}BuOH}} \mathrm{R{-}CH_2{-}CH(OH){-}C(OH)(CH_3)_2} \end{aligned}$ (출처: L2 p.14)
- $\alpha\ \text{-hydroxy}\ \text{ester}(\text{2차 alcohol}) \xrightarrow{\mathrm{TPAP(cat.)},\ \mathrm{NMO}} \alpha\ \text{-keto ester}\ (93\%)$ (출처: L6c p.10)
- 바레니클린 intermediate: $\begin{aligned} & \text{노보넨형}\ \mathrm{C{=}C} \\ & \xrightarrow{\text{cat.}\ \mathrm{OsO_4},\ \mathrm{NMO},\ 85\%} \text{exo-*cis*-diol} \\ & \xrightarrow{\mathrm{NaIO_4}} \text{dialdehyde} \end{aligned}$ (→ [periodate cleavage](../반응/과아이오딘산%20절단.md)) (출처: Tutorial 2 문제 3)

## 시험에서

- Tutorial 1 문제 4와 Test 1(2025) 문제 3은 *cis*-1,2-diol을 만드는 시약으로 OsO₄/NMO를 요구한다. (출처: Tutorial 1 문제 4, Test 1 문제 3)
- 검토 의견: Test 1 문제 3의 공식 답은 "OsO₄, then H₂O"다. 개념은 맞지만 출제 근거 쪽도 OsO₄/NMO를 쓰므로, 답안에는 "cat. OsO₄, NMO"로 쓰는 편이 안전하다. 공식 답 자체는 그대로 둔다. (보충 근거: Clayden p.442)

## 흔한 오해

- "NMO가 alkene에 OH를 붙인다": 두 O를 붙이는 것은 OsO₄다. NMO는 환원된 Os를 되돌릴 뿐이다. 그래서 입체화학(syn)도 OsO₄의 고리형 오스메이트 ester가 정한다(→ [dihydroxylation](../반응/다이하이드록실화.md)). (출처: L2 p.14)
- "TPAP 산화에서 TPAP가 화학량론적 산화제다": TPAP는 촉매량이고, 산화 당량은 NMO가 댄다. (출처: L6c p.10)

## 관련 문서

- 반응: [dihydroxylation](../반응/다이하이드록실화.md), [alcohol oxidation](../반응/알코올%20산화.md), [periodate cleavage](../반응/과아이오딘산%20절단.md)
- 시약: [OsO4](OsO4.md), [TPAP](TPAP.md), [NaIO4](NaIO4.md), [KMnO4](KMnO4.md)

## 출처

- [L2 Electrophilic Addition to Alkenes, Part 2](../../notes/L02_Electrophilic_Addition_to_Alkenes_Part2.md): 슬라이드 L2 p.14
- [L6 Oxidation and Alkene Synthesis](../../notes/L06_Oxidation_and_Alkene_Synthesis.md) 2절
- [Tutorial 1](../../practice/Tutorial_1.md) 문제 4, [Tutorial 2](../../practice/Tutorial_2.md) 문제 3
- [Test 1 (2025)](../../practice/Test1_2025.md) 문제 3
