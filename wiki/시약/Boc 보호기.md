---
aliases: [Boc, t-Boc, tert-butoxycarbonyl, t-뷰톡시카보닐, Boc2O, Boc 무수물, 다이-tert-뷰틸 다이카보네이트]
분류: 시약
강의: [L12]
주제태그: [보호기, 아민, 카바메이트, 산-불안정]
tags: [분류/시약, 범위/Test2, 단원/보호기, 강의/L12, 시약유형/보호기, 주제/산-불안정, 주제/카바메이트]
---
# Boc 보호기

> amine을 t-butyl carbamate(RNH–CO–OC(CH₃)₃)로 가리는 [protecting group](../개념/보호기.md)이다. Boc₂O와 염기로 씌우고, **산**([TFA](TFA.md) 등)으로 벗긴다.

## 개요

amine은 좋은 nucleophile이자 염기라서 electrophile이 있는 반응에 거의 항상 끼어든다. 질소를 carbonyl에 붙여 carbamate로 만들면 비공유 전자쌍이 C=O와 공명해 nucleophilicity와 염기성이 크게 떨어진다(→ [protecting group](../개념/보호기.md) 문서의 "왜 carbamate인가"). Boc는 그중 산으로 벗기는 carbamate이고, [peptide synthesis](../반응/펩타이드%20합성.md)의 N-protecting group 두 가지 중 하나다. (출처: L12 p.5, p.8)

## 도입

Boc는 Boc2O("Boc anhydride", di-tert-butyl dicarbonate, (t-BuOCO)2O)와 염기로 씌운다. 슬라이드의 예는 methionine을 Boc-Met으로 바꾸는 반응이다. amine N이 anhydride의 carbonyl 탄소를 공격하고, [tetrahedral intermediate](../개념/사면체%20중간체.md)에서 t-BuOCO2⁻가 떨어져 나간다.[^1]

`methionine --[Boc2O, base]--> Boc-Met`

(출처: L12 p.10)

보충: 왜 Cbz는 chloroformate로, Boc는 anhydride로 씌울까? Cbz에 해당하는 t-butyl chloroformate(t-BuOCOCl)는 불안정해서 시약으로 다루기 어렵기 때문이다. 그래서 Boc는 "Boc anhydride"인 di-t-butyl dicarbonate를 쓴다. (보충 근거: Clayden p.558, Wade p.1186)

## 메커니즘: 왜 산에 약한가

그렇다면 Boc는 왜 산에서 벗겨질까? 메커니즘을 따라가 보면 답이 보인다.

1. carbamate의 carbonyl O가 H⁺에 의해 protonate된다.
2. t-Bu–O 결합이 끊어지며 **t-butyl cation**이 떨어져 나간다. 이 cation은 3차 [carbocation](../개념/탄소%20양이온.md)이라 비교적 안정하므로 이 SN1형 이탈이 쉽게 일어난다. 남는 것은 carbamic acid RNH-COOH다.
3. t-butyl cation은 β-H를 잃고 isobutene(CH2=C(CH3)2)이 된다.
4. carbamic acid는 양성자가 옮겨 간 zwitterion(O⁻/NH2⁺) 형태를 거쳐 CO2를 내놓고 H2N–R이 된다.

![Boc carbamate의 carbonyl 산소가 protonate되고 t-butyl cation이 떨어져 carbamic acid가 되는 단계](../../figures/L12/boc_cleavage.svg)

그림: 위 1–2단계. 왼쪽: carbonyl 산소(파랑)의 비공유 전자쌍이 H⁺(빨강)를 잡는다(가역). 가운데: t-Bu–O 결합(빨강)의 전자가 O–C 자리로 가서 새 C=O를 만들고, protonate된 C=O⁺H의 π 전자는 산소로 돌아가 OH가 된다. 오른쪽: carbamic acid(초록이 새 C=O)와 3차 t-butyl cation이 생긴다.

![carbamic acid가 zwitterion을 거쳐 CO2와 amine이 되고, t-butyl cation이 H⁺를 잃어 isobutene이 되는 단계](../../figures/L12/boc_decarboxylation.svg)

그림: 위 3–4단계. 윗줄: carbamic acid가 proton transfer로 O⁻/N⁺H2 zwitterion이 된다. O⁻(파랑)의 전자쌍이 내려와 C=O를 만들고, C–N 결합(빨강) 전자가 질소로 가면서 CO2와 H2N–R이 떨어진다. 아랫줄: t-butyl cation의 methyl C–H 결합(파랑) 전자가 cation 탄소 쪽으로 가서 C=C(초록)가 되고 H⁺가 빠져 isobutene이 된다.

즉 Boc가 산에 약한 진짜 이유는 "안정한 3차 carbocation을 내놓을 수 있다"는 데 있다. 부산물이 CO2와 isobutene이라는 기체라서 반응이 한 방향으로 깔끔하게 진행된다는 점도 장점이다.[^2] (출처: L12 p.10)

보충: 반대로 Boc는 왜 염기에 강할까? carbonyl이 t-butyl group에 가려져 OH⁻조차 공격하지 못하기 때문이다. 그리고 산 쪽은 3 M HCl 정도의 묽은 산 수용액으로도 벗겨지며, 이 조건에서는 peptide 결합이나 methyl ester가 가수분해되지 않는다. 고체상 합성에서는 TFA로 짧게 처리해 벗긴다. (보충 근거: Clayden p.558–559, Wade p.1187)

## 선택성

- 염기에는 안정하다. 그래서 염기로 벗기는 [Fmoc](Fmoc%20보호기.md)와 거울상처럼 짝을 이루어 [orthogonal protection](../개념/직교%20보호.md)의 토대가 된다. (출처: L12 p.11)
- 산에 약한 acetal, silyl ether, THP, t-Bu ester와는 산 조건에서 orthogonal하지 않는다. TFA로 Boc를 벗기면 이들도 손상될 위험이 있다. 반면 [Cbz](Cbz%20보호기.md)는 TFA에 견딘다. (출처: L12 p.5)
- t-butyl ester(carboxylic acid protecting group)의 산 절단도 같은 원리(t-butyl cation 경유)다. (출처: L12 p.5)

## 예

- methionine `--[Boc₂O, base]-->` Boc-Met. (L12) (출처: L12 p.10)
- Boc–Phe–Ala–OMe `--[TFA]-->` H₂N–Phe–Ala–OMe. methyl ester와 amide는 TFA에 견딘다. (L12 Practice) (출처: L12 연습 풀이 p.3)

![Boc₂O에 의한 amine 보호](../../figures/L12/boc2o_protection.svg)

그림: 보충: amine N(파랑)의 전자쌍이 $Boc_2O$의 carbonyl C(빨강)를 공격하고 C=O π 전자가 O로 가서 tetrahedral intermediate가 된다. 이어서 $tBuOCO_2^-$가 떨어지고, 이것이 $CO_2$와 $tBuO^-$로 분해되어 반응을 끌어당긴다.

![methionine + Boc2O → Boc-Met](../../figures/L12/boc_methionine.svg)

그림: $NH_2$(파랑)가 Boc의 C=O(빨강)를 공격해 carbamate(초록)가 된다.

## 흔한 오해

- **"Boc와 Fmoc는 같은 carbamate니까 같은 조건에서 벗겨진다"고 생각하기 쉽지만 사실은** 정반대다. Boc는 안정한 t-butyl cation을 낼 수 있어 산에 약하고, Fmoc는 1차 CH2라 SN1/SN2가 막혀 산에 강한 대신 9번 C–H가 산성이라 염기에 약하다. 둘은 서로 orthogonal하다. (출처: L12 p.10–11)
- **"Boc 제거는 SN2다"라고 생각하기 쉽지만 사실은** 3차 탄소라 뒤쪽 공격이 아니라 t-butyl cation이 떨어지는 SN1형이다. (출처: L12 p.10)

## 관련 문서

- 시약: [Fmoc protecting group](Fmoc%20보호기.md), [Cbz protecting group](Cbz%20보호기.md), [TFA](TFA.md), [DCC](DCC.md)
- 반응: [peptide synthesis](../반응/펩타이드%20합성.md)
- 개념: [protecting group](../개념/보호기.md), [orthogonal protection](../개념/직교%20보호.md), [carbocation](../개념/탄소%20양이온.md), [tetrahedral intermediate](../개념/사면체%20중간체.md)

## 출처

- [L12 protecting group](../../notes/L12_Protecting_Groups.md) 6절, 7절 (L12 p.5, p.8, p.10)
- [L12 연습문제](../../practice/L12_Practice.md) 문제 3

[^1]: 보충: 이탈한 t-BuOCO2⁻는 CO2와 t-BuO⁻로 분해된다. 슬라이드에는 Boc2O와 염기라는 조건과 생성물만 나온다.
[^2]: 보충: 기체 부산물이 반응을 정방향으로 밀어 준다는 해석은 교재 수준의 보충이다.
