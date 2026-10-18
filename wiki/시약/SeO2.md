---
aliases: [selenium dioxide, 이산화셀레늄, SeO₂, Riley 산화]
분류: 시약
강의: [L6, L16]
주제태그: [산화제, 알릴-산화]
tags: [분류/시약, 범위/Test1, 범위/Test2, 단원/산화-알켄-합성, 단원/시그마트로픽-전자고리화, 강의/L06, 강의/L16, 시약유형/산화제, 주제/알릴-산화]
---
# SeO2

> selenium dioxide. allyl methyl기(C=C 옆의 CH₃)를 산화해 **enal**($\alpha,\beta$-unsaturated aldehyde)을 만든다. benzyl methyl group에는 듣지 않는다.

## 개요

allyl 위치의 C–H는 benzyl 위치처럼 공명으로 안정화되는 특별한 자리라, 산소가 없어도 산화할 수 있다. SeO₂는 이 allyl C–H를 골라 CHO까지 산화한다. 이 강의에서는 결과만 다루고, 메커니즘은 [pericyclic 반응](../개념/페리고리%20반응.md) 단원으로 미룬다. (출처: L6c p.18)

## 무엇을 하나

| 기질 | 생성물 | 비고 |
|---|---|---|
| allyl methyl R–CH=C(CH₃)₂ | R–CH=C(CH₃)–CHO | 그림상 R과 *trans*인 CH₃가 산화됨 |
| benzyl methyl Ar–CH₃ | 반응 없음 | [KMnO4](KMnO4.md)와의 차이 |

(출처: L6c p.18)

## 선택성

말단 isopropylidene =C(CH₃)₂에는 methyl이 두 개 있다. 슬라이드 그림에서는 R과 *trans* 위치에 있는 methyl이 CHO가 된다. 보충: 이 *E* 선택성은 표준 Riley oxidation와도 맞는다. (보충 근거: Clayden p.919) (출처: L6c p.18)

## 메커니즘: pericyclic 반응 두 번

L6에서 미뤄 둔 메커니즘은 L16(교재 보충, Clayden 기반)에서 나온다. SeO₂ allyl 산화는 사실 pericyclic 반응 두 번이다. (출처: Clayden p.919)

1. **ene reaction:** SeO₂가 alkene과 반응해 allyl seleninic acid가 생긴다.
2. **[2,3] rearrangement:** allyl seleninic acid는 allyl sulfoxide처럼(C–Se 결합이 더 약해서 더 쉽게) [2,3] sigmatropic rearrangement를 해 불안정한 Se(II) ester가 되고, 이것이 곧 분해되어 allylic alcohol이 된다(→ [2,3-sigmatropic rearrangement](../반응/2,3-시그마트로픽%20자리옮김.md)).
3. 특히 methyl group은 산화가 더 진행되어 aldehyde(또는 ketone)가 되기도 한다.

결과적으로 allyl 위치의 CH₃가 CH₂OH나 CH=O로 바뀐다. NBS allyl bromination과 결과는 비슷하지만 메커니즘은 전혀 다르다. 촉매량 SeO₂와 t-BuOOH(재산화제)를 함께 쓰면 독성 있고 냄새나는 selenium 부산물을 줄일 수 있다. (출처: Clayden p.919)

## 예: 시레닌 합성

천연물 sirenin 합성에서 `1. SeO₂; 2. LiAlH₄, AlCl₃` 순서로, 말단 isopropylidene의 allyl methyl을 CHO로 바꾼 뒤 CHO와 CO₂Me를 모두 CH₂OH로 환원해 diol을 얻는다. 두 번째 단계는 [LiAlH4](LiAlH4.md)가 aldehyde와 ester를 함께 환원하는 예이기도 하다. (출처: L6c p.18)

## 이웃 시약과 비교

- **[KMnO4](KMnO4.md):** $\text{benzyl}\ \mathrm{CH_3} \longrightarrow \mathrm{CO_2H}$. SeO₂는 allyl CH₃ → CHO. (출처: L6c p.18)
- **[MnO2](MnO2.md):** 이미 있는 allyl **OH**를 C=O로 바꾼다. SeO₂는 산소가 없는 allyl **CH₃**에서 출발한다. (출처: L6c p.10, p.18)

## 흔한 오해

- "SeO₂도 benzyl methyl을 산화한다": 듣지 않는다. (출처: L6c p.18)
- "SeO₂는 allyl methyl을 산까지 산화한다": 슬라이드의 생성물은 enal(CHO)이다.


## 그림으로 확인하기

![selenium ene](../../figures/L16/selenium_ene.svg)

![selenium 23](../../figures/L16/selenium_23.svg)

그림: propene 모형으로 ene와 뒤의 [2,3]을 나누었다. 주황은 전자쌍 이동, 초록은 새 결합이다. [2,3] 뒤 selenium ester의 hydrolysis가 allylic alcohol을 준다. (원본 대조: L16_Sigmatropic rearrangements.pdf p.20)

[원본 자료에서 세부 구조·입체배치 확인: L16_Sigmatropic rearrangements.pdf p.20](../../figures/L16/source/L16_p20.png)

## 관련 문서

- 비교 시약: [KMnO4](KMnO4.md), [MnO2](MnO2.md), [LiAlH4](LiAlH4.md)
- 반응: [2,3-sigmatropic rearrangement](../반응/2,3-시그마트로픽%20자리옮김.md)
- 개념: [pericyclic 반응](../개념/페리고리%20반응.md)

## 출처

- [L6 산화와 alkene 합성](../../notes/L06_Oxidation_and_Alkene_Synthesis.md) 4절
- [L16 sigmatropic rearrangement](../../notes/통독/L16_Sigmatropic_Rearrangements.md) (교재 보충, Clayden p.919 기반)
