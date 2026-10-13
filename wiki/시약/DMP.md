---
aliases: [Dess–Martin periodinane, Dess-Martin periodinane, 데스-마틴 페리오디네인, 데스-마틴 시약, Dess–Martin]
분류: 시약
강의: [L6]
주제태그: [산화제, 초원자가-아이오딘]
tags: [분류/시약, 범위/Test1, 기출/Test1-2025, 인명시약, 단원/산화-알켄-합성, 강의/L06, 시약유형/산화제, 주제/초원자가-아이오딘]
---
# DMP

> Dess–Martin periodinane. 5배위 iodine(V) 시약으로, 1차 alcohol을 aldehyde(산까지 가지 않음), 2차 alcohol을 ketone으로 바꾼다. 중성·실온 근처의 온화한 조건이 장점이다.

## 개요

menthol 경로의 "geraniol → geranial" 물음표(→ [alcohol oxidation](../반응/알코올%20산화.md))에 대한 가장 간단한 답이 DMP다. 1983년 D. B. Dess와 J. C. Martin이 보고했으며, 5배위 iodine(V)(pentacoordinate iodine(V)) 화합물이다. benziodoxolone 골격의 I에 acetate(OAc) 3개가 붙어 있는 구조다. 슬라이드는 이 시약을 핵심 결합에 따라 "I–O" 산화제라 부른다. (출처: L6c p.6–7)

`geraniol --[DMP, CH2Cl2]--> geranial (84%)`

aldehyde에서 정확히 멈추고 C=C의 *E* 기하도 그대로 유지된다. 그렇다면 왜 DMP를 많이 쓸까? 슬라이드는 세 가지 장점을 든다. 첫째, hypervalent iodine(초원자가 iodine) 시약은 독성이 낮고 안전하며 다루기 쉽고 환경 부담이 적다. 둘째, 온도와 pH가 온화하다(실온 근처, 중성). 셋째, 복잡한 기질의 민감한 작용기를 잘 견딘다(tolerance of sensitive functional groups). (출처: L6c p.7)

## 무엇을 하나

| 기질 | 생성물 | 비고 |
|---|---|---|
| 1차 alcohol | aldehyde | 산까지 가지 않음 |
| 2차 alcohol | ketone | |
| 3차 alcohol | 반응 없음 | 떼어 낼 α-H가 없음 |
| C=C | 그대로 | 기하도 유지 |

(출처: L6c p.6–7)

## 메커니즘

메커니즘은 [alcohol oxidation](../반응/알코올%20산화.md)의 일반 뼈대(O–LG 결합 형성 → 염기가 α-H 제거)를 그대로 따른다.

1. ligand exchange: alcohol O가 I(V)를 공격해 OAc 하나를 밀어낸다. 그러면 alkoxy periodinane intermediate와 AcOH가 생긴다. 이 단계가 "O–LG 만들기"에 해당한다.
2. I에 붙은 또 다른 acetate의 carbonyl 산소가 염기 노릇을 하며 분자 내에서 α-H를 떼어 낸다.
3. C=O가 생기면서 I–O 결합이 끊어지고, I(V)는 I(III)(iodinane, OAc 1개)로 환원된다.

전체 부산물은 iodinane과 AcOH 2분자다. (출처: L6c p.7)

## 이웃 시약과 비교

| 시약 | 활성 결합 | 특징 |
|---|---|---|
| **DMP** | I–O | 온화·중성, 비쌈 |
| [Swern](../반응/스원%20산화.md) | S–Cl | 싸서 대량 규모에 적합, −78 °C, 부산물 Me₂S(악취)·CO·CO₂·HCl |
| [TPAP](TPAP.md)/NMO | Ru–O | Ru 촉매량, NMO가 terminal oxidant |
| [MnO2](MnO2.md) | Mn–O | allylic·benzylic alcohol만 |
| [TEMPO](TEMPO.md)/NaOCl | N–O | 값싼 표백제가 terminal oxidant |
| [Jones reagent](존스%20시약.md) | Cr–O | 1차 alcohol을 산까지, 강산성 |

(출처: L6c p.8–11, p.16–17)

## 예

- `geraniol --[DMP, CH2Cl2]--> geranial (84%)` (L6) (출처: L6c p.7)
- "3 = 1 + 2": Boger의 vancomycin 계열 합성 `R–CH2OH --[Dess–Martin]--> R–CHO --[NaClO2]--> R–CO2H` (2단계 77%). 두 번째 단계는 [Pinnick oxidation](../반응/피닉%20산화.md)다(→ [alcohol oxidation](../반응/알코올%20산화.md)). (L6) (출처: L6c p.16–17)

## 흔한 오해

- **"DMP는 1차 alcohol을 산까지 산화한다"**: aldehyde에서 멈춘다. 산이 필요하면 [NaClO2](NaClO2.md)를 이어 쓴다. (출처: L6c p.17)
- **"DMP가 가장 좋으니 늘 DMP를 쓴다"**: 비싸다. 대량 규모에서는 Swern을 쓴다. (출처: L6c p.8)

## 관련 문서

- 반응: [alcohol oxidation](../반응/알코올%20산화.md), [Swern oxidation](../반응/스원%20산화.md), [Pinnick oxidation](../반응/피닉%20산화.md), [partial reduction of esters](../반응/에스터%20부분%20환원.md)
- 비교 시약: [TPAP](TPAP.md), [MnO2](MnO2.md), [TEMPO](TEMPO.md), [Jones reagent](존스%20시약.md), [NaClO2](NaClO2.md)

## 출처

- [L6 산화와 alkene 합성](../../notes/L06_Oxidation_and_Alkene_Synthesis.md) 2절, 3절 (L6c p.6–7, p.16–17)
- [L6 연습 문제](../../practice/L06_Exercises.md) 2번
