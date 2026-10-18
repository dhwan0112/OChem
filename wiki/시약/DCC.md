---
aliases: ["N,N′-dicyclohexylcarbodiimide", DCC, 다이사이클로헥실카보다이이미드, 디사이클로헥실카보디이미드, 카보다이이미드, 커플링제, coupling agent]
분류: 시약
강의: [L12]
주제태그: [커플링제, 아마이드-결합, 펩타이드]
tags: [분류/시약, 범위/Test2, 단원/보호기, 강의/L12, 시약유형/커플링제, 주제/아마이드-결합, 주제/펩타이드]
---
# DCC

> *N*,*N*′-dicyclohexylcarbodiimide(C₆H₁₁–N=C=N–C₆H₁₁). carboxylic acid를 활성화해 amine과 **amide 결합**을 만들게 하는 coupling agent다. 부산물은 dicyclohexylurea(DCU)다.

## 개요

[peptide synthesis](../반응/펩타이드%20합성.md)에서는 CO₂H를 먼저 C(=O)X로 활성화해 electrophilicity를 높인다. 슬라이드는 이 일을 하는 시약을 "coupling reagent"라고만 부르고, L12 연습 문제에서 그 예로 DCC를 쓴다. (출처: L12 p.9, p.12; L12 Practice 문제 3)

보충: carboxylic acid와 amine을 그냥 섞으면 산-염기 반응으로 ammonium carboxylate 염이 먼저 생겨, 실온에서는 amide가 잘 생기지 않는다. 그래서 활성화가 필요하다. (보충 근거: Wade p.983)

## 원리

보충: DCC의 가운데 탄소(N=C=N)가 electrophile이다. carboxylic acid가 이 탄소를 공격해 *O*-acylisourea가 되면, 원래 OH였던 자리가 좋은 leaving group을 가진 활성 ester로 바뀐다. amine이 그 carbonyl 탄소를 공격해 [tetrahedral intermediate](../개념/사면체%20중간체.md)를 거쳐 amide가 되고, DCC 쪽은 DCU로 떨어진다(→ [nucleophilic acyl substitution](../반응/친핵성%20아실%20치환.md)). (보충 근거: Wade p.1187, Clayden p.747) 이 설명은 연습 문제 해설에 있으며 공식 풀이에는 "DCC"라는 시약 이름만 나온다.

## 예

L-phenylalanine과 L-alanine으로 Phe-Ala dipeptide를 만드는 공식 풀이다. (출처: L12 Practice 풀이 p.3)

1. $\mathrm{L{-}Phe} \xrightarrow{\mathrm{Boc_2O}} \mathrm{Boc{-}Phe{-}OH}\ (\text{amine 보호}),$ → [Boc](Boc%20보호기.md))
2. $\begin{aligned} & \mathrm{L{-}Ala} \\ & \xrightarrow[\mathrm{MeOH}]{\mathrm{H^+}} \mathrm{H{-}Ala{-}OMe}\ (\text{carboxylic acid를 methyl ester로 보호}) \end{aligned}$

3. $\mathrm{Boc{-}Phe{-}OH} + \mathrm{H{-}Ala{-}OMe} \xrightarrow{\mathrm{DCC}} \mathrm{Boc{-}Phe{-}Ala{-}OMe}$

4. $\xrightarrow{\mathrm{TFA}} \mathrm{H_2N{-}Phe{-}Ala{-}OMe}$ (→ [TFA](TFA.md))
5. $\xrightarrow{\mathrm{NaOH},\ \text{물}} \mathrm{L{-}Phe{-}L{-}Ala}\ (\text{ester 가수분해})$


보호를 하는 이유는 각 amino acid가 amine(nucleophile)과 carboxylic acid(DCC로 활성화되는 쪽)를 모두 갖기 때문이다. 보호 없이 DCC와 섞으면 Phe-Phe, Ala-Ala, Ala-Phe, Phe-Ala와 oligomer가 무작위로 생긴다. (출처: L12 p.9; L12 Practice 문제 3)

검토 의견: 공식 경로는 표준적이고 옳다. 다만 DCC 활성화 단계와 NaOH saponification 단계에서는 $\alpha$-탄소의 racemization 위험이 있어, 실무에서는 HOBt 같은 첨가제나 온화한 조건(LiOH, 저온)을 함께 쓴다(보충 근거: Clayden p.748). 공식 답은 바꾸지 않는다.

## 흔한 오해

- "DCC가 있으면 보호 없이도 원하는 peptide 하나만 생긴다": DCC는 어느 carboxylic acid든 활성화하므로, 반응해서는 안 되는 NH₂와 CO₂H를 먼저 [protecting group](../개념/보호기.md)으로 가려야 한다. (출처: L12 p.9)
- "DCC는 amine을 활성화한다": 활성화되는 것은 carboxylic acid 쪽이다. amine은 그대로 nucleophile로 공격한다(보충). (보충 근거: Wade p.1187)

## 관련 문서

- 반응: [peptide synthesis](../반응/펩타이드%20합성.md), [nucleophilic acyl substitution](../반응/친핵성%20아실%20치환.md), [ester hydrolysis](../반응/에스터%20가수분해.md)
- 시약: [Boc protecting group](Boc%20보호기.md), [Fmoc protecting group](Fmoc%20보호기.md), [TFA](TFA.md)
- 개념: [protecting group](../개념/보호기.md), [orthogonal protection](../개념/직교%20보호.md), [tetrahedral intermediate](../개념/사면체%20중간체.md)

## 출처

- [L12 연습문제](../../practice/L12_Practice.md) 문제 3
- [L12 protecting group](../../notes/L12_Protecting_Groups.md) 7절
