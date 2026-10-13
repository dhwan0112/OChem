---
aliases: [Fmoc, 9-fluorenylmethoxycarbonyl, 9-플루오렌일메톡시카보닐, Fmoc-Cl]
분류: 시약
강의: [L12]
주제태그: [보호기, 아민, 카바메이트, 염기-불안정]
tags: [분류/시약, 범위/Test2, 단원/보호기, 강의/L12, 시약유형/보호기, 주제/염기-불안정, 주제/카바메이트]
---
# Fmoc 보호기

> amine을 9-fluorenylmethyl carbamate로 가리는 [protecting group](../개념/보호기.md)이다. Fmoc-Cl과 염기로 씌우고, **amine 염기**로 [E1cB elimination](../개념/E1cB%20제거.md)을 일으켜 벗긴다. 산에는 강하다.

## 개요

Fmoc(9-fluorenylmethoxycarbonyl)의 개성은 [Boc](Boc%20보호기.md)와 정반대라는 데 있다. Boc는 산에 약하고 염기에 강하며, Fmoc는 산에 강하고 염기에 약하다. 이 거울상 관계 덕분에 둘은 [orthogonal protection](../개념/직교%20보호.md)의 토대가 되고, [peptide 합성](../반응/펩타이드%20합성.md)에서 N-protecting group으로 쓰인다. (출처: L12 p.11)

## 도입

`RNH2 --[Fmoc-Cl, base]--> Fmoc-NHR` (출처: L12 p.11)

## 원리: 왜 산에 강한가

carbamate O에 붙은 탄소가 CH2, 즉 1차 탄소이므로 안정한 [carbocation](../개념/탄소%20양이온.md)을 만들 수 없어 SN1이 불가능하다. 그렇다고 SN2가 되느냐 하면, 바로 옆에 덩치 큰 fluorenyl기가 버티고 있어 그것도 안 된다. 산이 Boc를 벗기던 경로가 Fmoc에는 아예 없는 것이다. (출처: L12 p.11)

## 메커니즘: 왜 염기에 약한가

대신 Fmoc에는 다른 약점이 있다. fluorene 9번 위치의 C–H가 pKa 약 25로, 탄소에 붙은 수소치고는 꽤 산성이다. 이 H가 떨어지고 나면 생기는 anion이 14-electron aromatic system을 이루어 안정화되기 때문이다(→ [aromaticity](../개념/방향족성.md), [α-H acidity](../개념/α-수소의%20산도.md)). 그래서 염기를 만나면 다음과 같은 E1cB elimination이 일어난다.

1. amine 염기(:NR3)가 fluorene 9번 C–H를 deprotonation한다(가역).
2. 생긴 fluorenyl anion은 aromaticity로 안정화된다.
3. anion의 전자쌍이 C=C를 만들며 CH2–O 결합을 밀어내고, carbamate anion(RNH-CO2⁻)이 떨어져 나간다. 남은 hydrocarbon은 dibenzofulvene(9-methylenefluorene)이다.
4. carbamate anion이 CO2를 잃고 H2N–R이 된다.

![amine 염기가 Fmoc의 fluorene 9번 C–H를 떼고, anion이 carbamate를 밀어내 dibenzofulvene과 carbamate anion이 되는 E1cB 메커니즘](../../figures/L12/fmoc_removal.svg)

*그림: 윗줄 왼쪽: NR3(파랑)의 비공유 전자쌍이 fluorene 9번 탄소의 H(빨강, pKa 약 25)를 떼고, C–H 결합 전자는 탄소에 남는다(가역). 윗줄 오른쪽: 생긴 fluorenyl anion은 14-electron aromatic system으로 안정화된다. 이 anion의 전자쌍이 C9–CH2 사이에 C=C를 만들고, CH2–O 결합(빨강) 전자가 산소로 떨어져 나간다(E1cB). 아랫줄: dibenzofulvene(초록이 새 C=C)과 carbamate anion이 생기고, carbamate anion의 O⁻가 C=O를 만들며 C–N 결합(빨강)이 끊어져 CO2와 H2N–R이 된다.*

(출처: L12 p.11)

보충: pKa 약 25짜리 C–H를 amine(짝산 pKa 약 10)이 뗀다는 것이 이상해 보일 수 있다. 실제로 평형에서 생기는 aromatic anion은 아주 적은 양뿐이다. 하지만 생기는 족족 곧바로 제거 반응으로 소모되므로, 평형이 계속 오른쪽으로 끌려가 결국 전부 벗겨진다. fluorenyl anion이 aromatic인 이유는 cyclopentadienyl anion과 같다(가운데 5원 고리의 anion이 두 benzene 고리와 함께 14전자 π계를 이룬다). (보충 근거: Clayden p.559)

실제 peptide 합성에서는 piperidine 같은 2차 amine을 주로 쓴다.[^1] 결국 Boc(산에 약하고 염기에 강함)와 Fmoc(산에 강하고 염기에 약함)는 거울상처럼 서로 보완하는 관계이고, 이것이 orthogonal protection 전략의 토대가 된다. (출처: L12 p.11)

## 흔한 오해

- **"Fmoc는 산성 수소를 가지니까 강염기가 있어야 벗겨진다"고 생각하기 쉽지만 사실은** pKa 약 25짜리 C–H라도 amine 염기로 충분하다. deprotonation이 가역이어도 이어지는 E1cB elimination과 decarboxylation이 반응을 끌고 가기 때문이다. (출처: L12 p.11)
- **"Fmoc도 carbamate니까 TFA로 벗긴다"고 생각하기 쉽지만 사실은** 1차 CH2라 SN1, SN2가 모두 막혀 산에 안정하다. (출처: L12 p.11)

## 관련 문서

- 시약: [Boc 보호기](Boc%20보호기.md), [Cbz 보호기](Cbz%20보호기.md)
- 반응: [펩타이드 합성](../반응/펩타이드%20합성.md)
- 개념: [E1cB 제거](../개념/E1cB%20제거.md), [직교 보호](../개념/직교%20보호.md), [보호기](../개념/보호기.md), [방향족성](../개념/방향족성.md), [탄소 양이온](../개념/탄소%20양이온.md), [α-수소의 산도](../개념/α-수소의%20산도.md)

## 출처

- [L12 보호기](../../notes/L12_Protecting_Groups.md) 7절 (L12 p.11)

[^1]: 보충: 슬라이드의 염기는 일반적인 :NR3로 그려져 있다. 실제로 piperidine 같은 2차 amine이 흔히 쓰이고, 이 amine이 생성된 dibenzofulvene을 포획한다는 점은 표준 peptide 화학 내용이다.
