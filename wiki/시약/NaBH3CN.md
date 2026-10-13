---
aliases: [sodium cyanoborohydride, NaCNBH3, 사이아노수소화붕소나트륨, 소듐 사이아노보로하이드라이드, NaBH₃CN]
분류: 시약
강의: [L5]
주제태그: [환원제, 금속-수소화물, 환원성-아미노화]
tags: [분류/시약, 범위/Test1, 기출/Test1-2025, 단원/환원, 강의/L05, 시약유형/환원제, 주제/금속-수소화물, 주제/환원성-아미노화]
---
# NaBH3CN

> sodium cyanoborohydride. aldehyde·ketone은 느리게만 건드리고 imine(iminium)은 환원하며 약산성에서도 버틴다. 그래서 [reductive amination](../반응/환원성%20아미노화.md)의 표준 시약이다.

## 개요

hydride 시약 가운데 가장 약하다(LiAlH₄ > LiBH₄ > NaBH₄ > NaBH₃CN). 약하다는 것이 오히려 장점이다. carbonyl, amine, 환원제를 한 용기에 넣어도 carbonyl이 먼저 alcohol로 환원되지 않고, 생긴 imine·iminium만 골라 amine으로 바꾸기 때문이다. 슬라이드 표에는 NaCNBH₃로 적혀 있는데 같은 시약이다. 리튬염 LiBH₃CN도 같은 용도로 나온다. (출처: L5 p.10, p.17–18)

## 무엇을 하나

| 기질 | 생성물 | 비고 |
|---|---|---|
| imine·[iminium](../개념/이미늄%20이온.md) | amine | 빠름 |
| aldehyde·ketone | alcohol | 느림 |
| ester, amide, carboxylic acid | 반응 없음 | |

pH > 3의 수용액에서도 안정하다는 점이 NaBH₄와의 결정적 차이다. (출처: L5 p.17)

## 원리: 왜 iminium만 골라 환원하나

reductive amination에서 실제로 hydride를 받는 것은 carbonyl이 아니라 그 사이에 생기는 C=N이다. amine이 carbonyl에 붙어 hemiaminal이 되고, 물이 빠져 imine(2차 amine이면 iminium)이 된 뒤 hydride가 C=N 탄소에 붙는다(메커니즘과 그림은 [reductive amination](../반응/환원성%20아미노화.md)). 보충: CN기가 전자를 끌어 B–H의 hydride 공여력이 약해지므로, 더 electrophilic한 protonation된 iminium만 빠르게 환원된다. (보충 근거: Clayden p.234) (출처: L5 p.11, p.17)

## 예

슬라이드 조건은 NaBH₃CN, pH 3–4, EtOH다.[^1]

- `3-methylbutanal + NH3 --[NaBH3CN]--> 3-methylbutane-1-amine` (1차)
- `cyclohexylmethanamine + acetone --[NaBH3CN]--> N-(cyclohexylmethyl)propane-2-amine` (2차)
- `pyrrolidine + 2-methylpropanal --[NaBH3CN]--> 1-isobutylpyrrolidine` (3차)
- `cyclohexanone --[(1) (CH3)2NH; (2) NaBH3CN]--> N,N-dimethylcyclohexanamine (52-54%)`
- 거미 독소 전구체: aldehyde 조각과 1차 amine 조각을 NaCNBH₃(20 °C, 2 h)로 이어 2차 amine(48%)을 얻는다([L5 연습 문제](../../practice/L05_Exercises.md) 2번).

(L5) (출처: L5 p.10, p.12, p.14)

## 이웃 시약과 비교

- **[NaBH4](NaBH4.md):** carbonyl을 빠르게 환원하므로 imine이 생기기 전에 alcohol을 만들어 버리고, imine 형성에 필요한 산성 조건에서 분해된다. (출처: L5 p.17)
- **H₂/[Pd/C](Pd-C.md):** 같은 일을 할 수 있지만 benzyl ether나 Cbz 같은 benzyl기를 함께 끊을 수 있다(→ [hydrogenolysis](../반응/수소화분해.md)). 거미 독소 전구체 합성에서 NaCNBH₃를 쓴 이유다. (출처: L5 p.14, p.33)
- **HCOOH([Eschweiler–Clarke 반응](../반응/에슈바일러-클라크%20반응.md)):** N,N-dimethylation 전용. metal hydride 없이 formate ion이 hydride를 준다. (출처: L5 p.15)

## 흔한 오해

- **"NaBH₄로 바꿔도 된다"**: 위 이유로 안 된다. one-pot reductive amination의 핵심은 carbonyl에 느린 시약이다. (출처: L5 p.17)
- **"약한 시약이니 산성일수록 좋다"**: 아래 각주의 검토 의견 참고. 원리는 "약산성에서 iminium을 선택적으로 환원한다"이다.

## 관련 문서

- 반응: [reductive amination](../반응/환원성%20아미노화.md), [Eschweiler–Clarke 반응](../반응/에슈바일러-클라크%20반응.md), [hydrogenolysis](../반응/수소화분해.md)
- 비교 시약: [NaBH4](NaBH4.md), [Pd/C](Pd-C.md)
- 개념: [iminium ion](../개념/이미늄%20이온.md), [metal hydride의 반응성](../개념/금속%20수소화물의%20반응성.md), [imine](../개념/이민.md), [amine 합성 개관](../개념/아민%20합성%20개관.md)

## 출처

- [L5 환원](../../notes/L05_Reduction.md) 1절, 2절 (슬라이드 p.10–12, p.14, p.17)
- [L5 연습 문제](../../practice/L05_Exercises.md) 2번, 4번

[^1]: 검토 의견: 흔히 인용되는 Borch 조건은 pH 6–7 부근이며, pH 3–4처럼 더 산성이면 NaBH₃CN이 aldehyde·ketone도 상당히 환원하기 시작한다고 알려져 있다(보충 근거: Clayden p.234–235, pH 6 조건 부분만). 시험에서는 슬라이드 값(pH 3–4)을 따른다(→ [reductive amination](../반응/환원성%20아미노화.md)).
