---
aliases: [sodium chlorite, 아염소산나트륨, 소듐 클로라이트, Pinnick 시약, NaClO₂]
분류: 시약
강의: [L6]
주제태그: [산화제]
tags: [분류/시약, 범위/Test1, 기출/Test1-2025, 단원/산화-알켄-합성, 강의/L06, 시약유형/산화제]
---
# NaClO2

> sodium chlorite. 약산성 완충제(NaH₂PO₄)와 함께 **aldehyde를 carboxylic acid**으로 바꾼다([Pinnick oxidation](../반응/피닉%20산화.md)). 순하고 싸고 선택적이며, 부산물 HOCl을 잡는 제거제를 꼭 함께 넣는다.

## 개요

aldehyde를 이미 손에 넣었다면 산까지의 마지막 한 걸음을 무엇으로 할까? 슬라이드의 답이 NaClO₂(Pinnick, 1981)다. 특히 [Jones reagent](존스%20시약.md)의 강산성을 견디지 못하는 민감한 기질에서 "순한 산화로 aldehyde까지, 그 다음 NaClO₂로 산까지"라는 2단계 전략의 두 번째 단계를 맡는다. (출처: L6c p.15–16)

## 무엇을 하나

| 기질 | 조건 | 생성물 |
|---|---|---|
| aldehyde RCHO | NaClO₂, NaH₂PO₄, 2-methyl-2-butene(또는 DMSO) | carboxylic acid RCO₂H |

공정 규모 예: TMS 치환 thienothiophene aldehyde --[NaClO₂, NaH₂PO₄, 2-MeTHF/DMSO/H₂O; NaHSO₃ 퀜치]--> carboxylic acid → (KOH, HCl로 desilylation) → PF-07208254. 발열은 투입량과 희석으로 제어한다. (출처: L6c p.15)

## 왜 alkene을 함께 넣나

반응 부산물인 HOCl이 기질이나 생성물과 부반응을 일으킨다. 그래서 HOCl을 먼저 먹어 치울 희생양 alkene(scavenger)을 넣는다. DMSO를 대신 써도 된다.

(CH₃)₂C=CHCH₃ + HOCl → (CH₃)₂C(OH)–CH(Cl)CH₃ (3-chloro-2-methylbutan-2-ol)

OH는 3차 탄소에, Cl은 2차 탄소에 붙는다. Cl이 electrophile로 먼저 붙고, 생긴 chloronium 이온의 더 치환된 탄소를 물이 공격하기 때문이다([Markovnikov형](../개념/마르코프니코프%20규칙.md), → [halohydrin formation](../반응/할로하이드린%20형성.md)). 보충: 표준 메커니즘에서는 chlorous acid HClO₂가 aldehyde에 첨가한 뒤 고리형 transition state로 분해되며 RCO₂H와 HOCl이 생긴다. (출처: L6c p.15)

## 예: "3 = 1 + 2"

Boger의 vancomycin 계열 합성: R–CH₂OH --[Dess–Martin]--> R–CHO --[NaClO₂]--> R–CO₂H(2단계 77%). (1차 alcohol → 산) = (alcohol → aldehyde) + (aldehyde → 산)이다. (출처: L6c p.16–17)

## 이웃 시약과 비교

- **[Jones reagent](존스%20시약.md):** 1차 alcohol을 한 번에 산까지 보내지만 강산성이라 민감한 기질에 부적합하다. (출처: L6c p.16)
- **[DMP](DMP.md)·[TEMPO](TEMPO.md) 등:** aldehyde에서 멈추는 시약이라 NaClO₂와 짝을 이룬다. (출처: L6c p.17)

## 흔한 오해

- "2-methyl-2-butene은 반응물이다": HOCl 제거제다. (출처: L6c p.15)
- "HOCl이 붙을 때 Cl이 3차 탄소로 간다": 반대다. OH가 3차, Cl이 2차 탄소다. (출처: L6c p.15)

## 관련 문서

- 반응: [Pinnick oxidation](../반응/피닉%20산화.md), [alcohol oxidation](../반응/알코올%20산화.md), [halohydrin formation](../반응/할로하이드린%20형성.md)
- 비교 시약: [Jones reagent](존스%20시약.md), [DMP](DMP.md), [TEMPO](TEMPO.md)
- 개념: [Markovnikov's rule](../개념/마르코프니코프%20규칙.md)

## 출처

- [L6 산화와 alkene 합성](../../notes/L06_Oxidation_and_Alkene_Synthesis.md) 3절
