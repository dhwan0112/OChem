---
aliases: [trifluoroacetic acid, 트라이플루오로아세트산, 트리플루오로아세트산, CF3CO2H, CF₃CO₂H]
분류: 시약
강의: [L2, L12]
주제태그: [산, 보호기-제거]
tags: [분류/시약, 범위/Test1, 범위/Test2, 단원/보호기, 단원/알켄-첨가, 강의/L02, 강의/L12, 시약유형/산, 주제/보호기-제거]
---
# TFA

> trifluoroacetic acid(CF₃CO₂H). 휘발성 있는 강한 유기산이다. 이 과목에서는 **alkene의 단계적 수화**와 **[Boc protecting group](Boc%20보호기.md) 제거**에 등장한다.

## 개요

TFA는 acetic acid의 CH₃를 CF₃로 바꾼 산이다. 보충: fluorine 세 개가 전자를 강하게 끌어 짝염기(CF₃CO₂⁻)를 안정화하므로 acetic acid보다 훨씬 강한 산이다(표준 교재 내용)(보충 근거: Clayden p.176). 강산이면서 짝염기가 nucleophile 역할도 할 수 있어, alkene에 "H와 CF₃CO₂"를 더할 수 있다. (출처: L2 p.20)

## 무엇을 하나

| 기질/조건 | 생성물 | 비고 |
|---|---|---|
| alkene + TFA, 그다음 염기/H₂O | alcohol (Markovnikov) | ester를 거치는 [acid-catalyzed hydration](../반응/산%20촉매%20수화.md) |
| Boc–NR₂ + TFA | 유리 amine | 부산물 CO₂ + 아이소뷰텐 |

(출처: L2 p.20, L12 p.8)

## 단계적 수화

산 촉매 수화는 E1 탈수와 평형이라 한쪽으로 몰기 어렵다. TFA를 쓰면 이 문제를 피한다. (출처: L2 p.19–20)

1. TFA가 alkene을 protonation해(δ⁺인 H) 더 안정한 [carbocation](../개념/탄소%20양이온.md)을 만들고, 짝염기가 그 cation을 붙잡아(δ⁻인 O) trifluoroacetate ester가 된다.
2. ester를 염기성 수용액으로 가수분해하면 alcohol과 trifluoroacetate anion이 나온다.

- 예: cyclohexene --[TFA]--> cyclohexyl trifluoroacetate --[염기, H₂O]--> cyclohexane올 (출처: L2 p.20)
- 예: 카바졸 골격의 아이소프로펜일기 **12** --[TFA, DCM]--> 3차 TFA ester **13** --[NH₄OH, MeOH]--> 3차 alcohol **5** (85%, >99.5% ee) (출처: L2 p.21)

## Boc 제거

Boc(*t*-뷰톡시카보닐)는 산으로 벗기며, 대표 시약이 TFA다. 카바메이트가 끊어져 생긴 carbamic acid이 CO₂를 내놓고 유리 amine이 된다. Cbz는 수소화분해, Fmoc는 염기로 벗기므로 서로 [orthogonal protection](../개념/직교%20보호.md)이 된다. Boc가 산에 약한 것은 안정한 *t*-butyl cation을 낼 수 있기 때문이다. (출처: L12 p.8, p.11)

## 흔한 오해

- "TFA로 Boc만 골라 벗길 수 있으니 다른 산 민감 protecting group는 안전하다": acetal이나 silyl ether도 산에 약하므로, 특히 물이 있으면 함께 손상될 수 있다. 산 조건에서는 이들끼리 직교적이지 않다. (출처: L12 흔한 오해, 연습 문제 8)

## 관련 문서

- 반응: [acid-catalyzed hydration](../반응/산%20촉매%20수화.md), [peptide synthesis](../반응/펩타이드%20합성.md)
- 개념: [carbocation](../개념/탄소%20양이온.md), [Markovnikov's rule](../개념/마르코프니코프%20규칙.md), [orthogonal protection](../개념/직교%20보호.md), [protecting group](../개념/보호기.md)
- 시약: [Boc protecting group](Boc%20보호기.md), [Fmoc protecting group](Fmoc%20보호기.md), [Cbz protecting group](Cbz%20보호기.md)

## 출처

- [L2 Electrophilic Addition to Alkenes, Part 2](../../notes/L02_Electrophilic_Addition_to_Alkenes_Part2.md): 슬라이드 L2 p.19–21
- [L12 Protecting Groups](../../notes/L12_Protecting_Groups.md) 6절, 7절, 흔한 오해
