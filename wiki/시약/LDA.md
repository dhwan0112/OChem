---
aliases: [lithium diisopropylamide, 리튬 다이아이소프로필아마이드, LiN(i-Pr)2]
분류: 시약
강의: [L7, L8, L10, L11]
주제태그: [염기, 엔올레이트]
tags: [분류/시약, 범위/Test1, 범위/Test2, 기출/Test1-2025, 단원/공액-첨가, 단원/엔올레이트, 강의/L07, 강의/L08, 강의/L10, 강의/L11, 시약유형/염기]
---
# LDA

> lithium diisopropylamide(LiN(*i*-Pr)₂). **세지만 친핵성은 없는(strong, non-nucleophilic)** 염기다. ketone과 ester를 저온에서 정량적, 비가역적으로 [enolate](../개념/엔올과%20엔올레이트.md)로 바꾸고, 덜 치환된 쪽의 [kinetic enolate](../개념/속도론적%20엔올레이트와%20열역학적%20엔올레이트.md)를 준다.

## 개요

enolate를 "조금" 만드는 염기는 많지만, 출발 carbonyl을 **전부** enolate로 바꾸는 염기는 드물다. LDA가 표준이 된 이유는 두 가지다. conjugate acid인 diisopropylamine이 매우 약한 산이어서 평형이 완전히 enolate 쪽으로 가고, 부피 큰 isopropyl group 두 개가 질소를 가려 carbonyl 탄소를 공격하지 못한다. (출처: L7 p.5–6)

## 만드는 법

THF에서 *n*-BuLi와 diisopropylamine을 섞는다.

`n-BuLi + HN(i-Pr)₂ --[THF]--> LiN(i-Pr)₂ + 뷰테인(pKa 50)`

BuLi의 carbanion이 염기로서 N–H의 수소를 떼어 내고, 훨씬 약한 산인 뷰테인이 기체로 빠져나가므로 되돌아가지 않는다. (출처: L7 p.6)

## 원리

### 왜 정량적인가

산-염기 평형은 더 약한 산 쪽으로 기운다([alpha-hydrogen acidity](../개념/α-수소의%20산도.md)).

- ketone(pKa 19) + EtONa ⇌ enolate + EtOH(pKa 16): 왼쪽으로 치우쳐 enolate가 소량뿐이다.
- ketone(pKa 19) + LDA → enolate + HN(*i*-Pr)₂(pKa 36–38)[^1]: 사실상 완전히 오른쪽으로 간다.

ester α-H(pKa ~25)도 LDA로 충분히 떼어진다. (출처: L7 p.4–6, p.13)

### 왜 친핵성이 없나

그렇다면 BuLi를 바로 쓰면 안 될까? BuLi는 친핵성도 강해서 carbonyl 탄소에 첨가해 버린다. LDA는 질소 양옆의 부피 큰 isopropyl group 두 개가 질소를 가려, 작은 양성자는 잘 떼어 내지만 carbonyl 탄소에는 다가가지 못한다. 즉 LDA는 강염기이면서 친핵성이 없는(NOT nucleophilic) 염기다. 같은 부류로 LiTMP(lithium 2,2,6,6-테트라메틸피페리다이드)와 LHMDS(LiN(SiMe₃)₂)가 있다. (출처: L7 p.6)

## 선택성

- **regioselectivity:** −78 °C에서 LDA는 가장 덜 가려진 α-H를 빨리, 비가역적으로 떼어 간다. 그래서 비대칭 ketone에서는 덜 치환된 C=C의 enolate가 생긴다. 2-헵타논은 methyl 쪽만 100 : 0으로 deprotonate된다. (출처: L7 p.8, p.11–12)
- **화학선택성:** 친핵성이 없으므로 carbonyl에 첨가하지 않는다. (출처: L7 p.6)

![2-methylcyclohexanone의 kinetic/thermodynamic enolate](../../figures/L07/kinetic_thermo_enolate.svg)

*그림: 가려지지 않은 C6–H를 LDA가 −78 °C에서 빠르게 떼면 kinetic enolate(C1=C6)가 생긴다. 자세한 설명은 [kinetic vs thermodynamic enolate](../개념/속도론적%20엔올레이트와%20열역학적%20엔올레이트.md)에 있다. (출처: L7 p.11–12)*

## 쓰임

| 용도 | 예 | 출처 |
|---|---|---|
| [enolate alkylation](../반응/엔올레이트%20알킬화.md) | 2-methylcyclohexanone --[LDA; CH₃I]--> 2,6-dimethylcyclohexanone 56% (2,2-이치환체 6%) | L7 p.10–11 |
| ester alkylation | CH₃CH₂CH₂CO₂Me --[LDA, THF; EtI]--> (CH₃CH₂)₂CHCO₂Me 96% | L7 p.13 |
| [directed aldol](../반응/교차%20알돌%20반응.md) | CH₃COCH₂CH₃ --[LDA, −78 °C; CH₃CHO; H₂O]--> CH₃CH₂COCH₂CH(OH)CH₃ 75% | L8 p.18 |
| kinetic [silyl enol ether](실릴%20엔올%20에터.md) | 2-methylcyclohexanone --[LDA, −78 °C; Me₃SiCl]--> 덜 치환된 enol ether 99 : 1 | L8 p.24 |
| 위치 지정 [α-halogenation](../반응/α-할로젠화.md) | R–CH₂–CO–CH₃ --[LDA; Me₃SiCl; Br₂]--> R–CH₂–CO–CH₂Br | L10 p.10 |
| [asymmetric alkylation](에반스%20옥사졸리디논.md) | N-acyl oxazolidinone --[LDA, −78 °C; BnBr]--> 92%, 99 : 1 dr | L7 p.27 |

슬라이드는 2-methylpropanoic acid methyl과 cyclopentanecarbaldehyde의 LDA enolate를 직접 그려 보라고 한다(→ [L7 연습 문제](../../practice/L07_Exercises.md) 1). (출처: L7 p.7)

## 흔한 오해

- "강염기면 BuLi를 바로 써도 된다": BuLi는 친핵성이 강해 carbonyl에 첨가한다. 그래서 BuLi로 비친핵성인 LDA를 먼저 만든 뒤 쓴다. (출처: L7 p.6)
- "LDA면 어떤 carbonyl이든 directed aldol의 nucleophile로 쓸 수 있다": 슬라이드는 ketone과 ester에 쓰고 aldehyde는 잘 안 된다고 명시한다. aldehyde끼리의 crossed aldol에는 [Mukaiyama aldol reaction](../반응/무카이야마%20알돌%20반응.md)을 쓴다. (출처: L8 p.18, p.26)
- "lithium enolate는 엔알에도 Michael 첨가를 한다": Li⁺가 aldehyde 산소에 배위해 고리형 transition state를 만들어 1,2-첨가(aldol)가 일어난다(72%). (출처: L11 p.16)

## 관련 문서

- 반응: [enolate alkylation](../반응/엔올레이트%20알킬화.md), [crossed aldol reaction](../반응/교차%20알돌%20반응.md), [Mukaiyama aldol reaction](../반응/무카이야마%20알돌%20반응.md), [α-halogenation](../반응/α-할로젠화.md)
- 시약: [alkoxide base](알콕사이드%20염기.md), [silyl enol ether](실릴%20엔올%20에터.md), [Evans oxazolidinone](에반스%20옥사졸리디논.md)
- 개념: [enol and enolate](../개념/엔올과%20엔올레이트.md), [enolate chemistry (overview)](../개념/엔올레이트%20화학%20개관.md), [alpha-hydrogen acidity](../개념/α-수소의%20산도.md), [kinetic vs thermodynamic enolate](../개념/속도론적%20엔올레이트와%20열역학적%20엔올레이트.md)

## 출처

- [L7 enolate와 α-alkylation](../../notes/L07_Enolate_Alkylation.md) I절(p.5–7), II절, VI절
- [L8 aldol reaction](../../notes/L08_Aldol_Reactions.md) 5절
- [L10 enol과 enamine](../../notes/L10_Enol_and_Enamine.md) silyl enol ether halogenation
- [L11 conjugate addition](../../notes/L11_Conjugate_Addition.md) 4절

[^1]: diisopropylamine의 pKa가 L7 p.4의 표에서는 36, p.6의 반응식에서는 38로 서로 다르게 적혀 있다. 둘 다 문헌에서 쓰이는 값(측정 조건에 따라 다름)이며, 어느 값이든 ketone(19)과의 차이가 커서 결론은 같다. 평형 상수는 대략 10^(ΔpKa)로 어림한다. (출처: L7 p.4, p.6)
