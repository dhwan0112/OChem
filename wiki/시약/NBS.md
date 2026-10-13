---
aliases: [N-bromosuccinimide, N-브로모석신이미드, N-브로모숙신이미드]
분류: 시약
강의: [L2, L14]
주제태그: [브로민화제, 할로젠]
tags: [분류/시약, 범위/Test1, 범위/Test2, 단원/고리화-첨가, 단원/알켄-첨가, 강의/L02, 강의/L14, 시약유형/할로젠화제, 주제/브로민화제, 주제/할로젠]
---
# NBS

> *N*-bromosuccinimide. 이 과목에서는 주로 **Br₂를 조금씩 내놓는 다루기 쉬운 bromine 공급원**으로 쓰여, [bromonium ion](../개념/브로모늄%20이온.md)을 거치는 [bromohydrin·bromoether](../반응/할로하이드린%20형성.md) 합성에 등장한다.

## 개요

Br₂는 휘발성이 크고 다루기 까다롭다. NBS는 succinimide의 N에 Br이 붙은 고체 시약으로, 반응계 안에서 Br₂를 낮은 농도로 계속 만들어 준다. 그래서 반응 자체는 Br₂와 같은 bromonium 이온 경로를 따른다. (출처: L2 p.11)

## 어떻게 Br₂를 내놓나

1. H⁺가 NBS의 carbonyl 산소를 protonation한다.
2. Br⁻가 N–Br의 Br을 공격해 Br₂와 succinimide가 생긴다.
3. 생긴 Br₂가 alkene과 반응하면 HBr이 다시 만들어진다.
4. 그 HBr이 또 NBS에서 Br₂를 풀어낸다.

그래서 처음에 **아주 소량의 HBr만 있으면** 반응이 계속 굴러간다. (출처: L2 p.11)

## 무엇을 하나

| 기질/조건 | 생성물 | 비고 |
|---|---|---|
| alkene + NBS, cat. HBr, H₂O/DMSO | bromohydrin | anti, OH는 더 치환된 탄소에 |
| alkene + NBS, HBr, 그다음 ROH | bromoether | anti, OR은 더 치환된 탄소에 |
| cyclopent-2-enone + NBS | 4-bromocyclopent-2-enone | allyl bromination (cubane 합성 1단계) |

(출처: L2 p.11–12, L14 p.30)

- 예: *trans*-스틸벤 --[NBS, HBr(촉매), H₂O/DMSO]--> bromohydrin(±, anti). 물이 bromonium ion의 반대쪽에서 공격하므로 **stereoselective**이다. (출처: L2 p.11)
- 예: 1-methylcyclohexene --[1. NBS, HBr; 2. alcohol]--> Br은 2차 탄소(CH)에, OR은 methyl이 붙은 3차 탄소에 anti. stereoselective이면서 regioselective이다(→ [halohydrin formation](../반응/할로하이드린%20형성.md)). (출처: L2 p.12)
- 예: 1-methylcyclohexene --[NBS(cat. HBr), H₂O]--> *trans*-2-bromo-1-methylcyclohexanol(±) (→ [L2 연습 문제](../../practice/L02_Exercises.md) 3번)
- 예: cyclohexene --[1. NBS, HBr; 2. HC≡CCH₂OH]--> *trans*-1-bromo-2-(propargyloxy)cyclohexane(±) (출처: L2 p.12)

보충: allyl 위치 bromination는 bromonium 이온이 아니라 radical 연쇄 반응(Wohl–Ziegler reaction)으로 진행한다. 슬라이드에는 반응식만 있고 메커니즘은 나오지 않는다(표준 교재 내용). (보충 근거: Clayden p.573, Wade p.228)

## 흔한 오해

- "NBS는 Br₂와 전혀 다른 메커니즘으로 반응한다": L2에서 NBS는 Br₂ 공급원이고, 반응은 bromonium 이온을 거친다. (출처: L2 p.11)
- "HBr을 당량만큼 넣어야 한다": 촉매량이면 충분하다. Br₂가 alkene과 반응할 때 HBr이 재생되기 때문이다. (출처: L2 p.11)

## 관련 문서

- 반응: [halohydrin formation](../반응/할로하이드린%20형성.md), [halogen addition](../반응/할로젠%20첨가.md)
- 개념: [bromonium ion](../개념/브로모늄%20이온.md), [loose SN2 transition state](../개념/느슨한%20SN2%20전이%20상태.md)

## 출처

- [L2 Electrophilic Addition to Alkenes, Part 2](../../notes/L02_Electrophilic_Addition_to_Alkenes_Part2.md): 슬라이드 L2 p.11–12
- [L14 Cycloaddition, Part 2](../../notes/L14_Cycloaddition_Part2.md) 11절 (cubane 합성)
