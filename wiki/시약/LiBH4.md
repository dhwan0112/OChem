---
aliases: [lithium borohydride, 수소화붕소리튬, 리튬 보로하이드라이드, LiBH₄]
분류: 시약
강의: [L5, L7]
주제태그: [환원제, 금속-수소화물]
tags: [분류/시약, 범위/Test1, 단원/엔올레이트, 단원/환원, 강의/L05, 강의/L07, 시약유형/환원제, 주제/금속-수소화물]
---
# LiBH4

> lithium borohydride. NaBH₄보다 강하고 LiAlH₄보다 온화한 중간 세기 환원제다. carboxylic acid·amide·nitrile이 있어도 **ester와 lactone**만 골라 alcohol로 바꾼다.

## 개요

NaBH₄는 ethyl acetate나 ethyl benzoate 같은 ester를 아주 느리게만 환원하지만, LiBH₄는 쉽게 환원한다(→ [metal hydride의 반응성](../개념/금속%20수소화물의%20반응성.md)). Na⁺를 Li⁺로 바꾸기만 했는데 왜 ester가 환원될까? 보통 Li⁺가 더 강한 Lewis acid로서 carbonyl 산소에 배위해 carbonyl을 활성화하기 때문이라고 설명한다.[^1] 그 결과 LiBH₄는 NaBH₄보다 강하고 LiAlH₄보다는 온화한 중간 세기의 시약이 된다. aldehyde와 ketone은 물론 환원하고, 특히 carboxylic acid·amide·nitrile이 있어도 **ester와 lactone**만 골라 alcohol로 바꾸는 데 쓰인다. (출처: L5 p.21–22)

## 무엇을 하나

| 기질 | 생성물 | 비고 |
|---|---|---|
| aldehyde, ketone | alcohol | |
| ester, lactone | 1차 alcohol(diol) | NaBH₄와의 차이 |
| carboxylic acid | 반응 없음 | deprotonate되어 carboxylate가 됨 |
| amide, nitrile | 반응 없음 | |

(출처: L5 p.17, p.22)

## 선택성

`MeO2C-CH2-CH(CH3)-CH2-CO2H --[LiBH4, EtOH]--> HO-CH2-CH2-CH(CH3)-CH2-CO2H`

ester 쪽만 CH₂OH가 되고 산은 그대로 남는다. 산이 살아남는 이유는 [carbonyl 반응성 서열](../개념/금속%20수소화물의%20반응성.md)(aldehyde > ketone > ester > amide > carboxylate)에서 찾을 수 있다. 산은 hydride 시약과 만나면 deprotonate되어 carboxylate가 되는데, carboxylate는 반응성 서열의 맨 끝이다. (출처: L5 p.18, p.22)

[borane](보레인.md)과는 거울처럼 상보적이다. 같은 기질 MeO₂C–CH₂CH(CH₃)CH₂–CO₂H에 LiBH₄를 쓰면 ester가 환원되고, BH₃를 쓰면 산이 환원된다([L5 연습 문제](../../practice/L05_Exercises.md) 8번). (출처: L5 p.22, p.27)

## 예

- `MeO2C-CH2CH(CH3)CH2-CO2H --[LiBH4, EtOH]--> HOCH2CH2CH(CH3)CH2-CO2H` (ester만 환원) (L5) (출처: L5 p.22)
- 3β-acetoxy steroid-20-온: NaBH₄는 ketone만 환원하고 acetate를 남기지만, LiBH₄는 ketone과 acetate를 모두 환원해 3β-OH가 드러난 diol을 준다([L5 연습 문제](../../practice/L05_Exercises.md) 5번). (L5) (출처: L5 p.25)
- [Evans oxazolidinone](에반스%20옥사졸리디논.md) 제거: alkylate된 N-acyl oxazolidinone을 LiBH₄로 환원하면 chiral 1차 alcohol(2-benzylbutane-1-올)이 나오고 α-stereocenter는 유지된다. (L7) (출처: L7 p.28)

## 이웃 시약과 비교

| 시약 | ketone | ester | amide | carboxylic acid |
|---|---|---|---|---|
| [NaBH4](NaBH4.md) | O | 느림 | X | X |
| **LiBH₄** | O | O | X | X |
| [LiAlH4](LiAlH4.md) | O | O | O | 느림(충분히 쓰면 O) |
| [borane](보레인.md) | 느림 | 느림 | O | O |

(출처: L5 p.17)

## 흔한 오해

- **"BH₃도 LiBH₄처럼 ester를 환원한다"고 생각하기 쉽지만 사실은** 정반대다. LiBH₄는 ester를(산 유지), BH₃는 산과 amide를(ester 유지) 환원한다. (출처: L5 p.22, p.27)
- **"Na⁺/Li⁺ 차이는 사소하다"**: ester를 환원하느냐 마느냐가 갈린다. (출처: L5 p.21)

## 관련 문서

- 반응: [partial reduction of esters](../반응/에스터%20부분%20환원.md), [enolate alkylation](../반응/엔올레이트%20알킬화.md)
- 비교 시약: [NaBH4](NaBH4.md), [LiAlH4](LiAlH4.md), [borane](보레인.md), [DIBAL-H](DIBAL-H.md), [Evans oxazolidinone](에반스%20옥사졸리디논.md)
- 개념: [metal hydride의 반응성](../개념/금속%20수소화물의%20반응성.md), [chiral 보조기](../개념/키랄%20보조기.md)

## 출처

- [L5 환원](../../notes/L05_Reduction.md) 2절 (슬라이드 p.17, p.21–22, p.25, p.27)
- [L5 연습 문제](../../practice/L05_Exercises.md) 5번, 8번
- [L7 enolate alkylation](../../notes/L07_Enolate_Alkylation.md) Evans 보조기 절

[^1]: 이 설명은 슬라이드가 아닌 일반 교재 수준의 보충이다. (보충 근거: Clayden p.530–531) 슬라이드 p.21은 "cation에 따라 반응성 차이가 크다"는 관찰만 제시한다.
