---
aliases: [DIBAL, DIBALH, diisobutylaluminium hydride, 다이아이소뷰틸알루미늄 하이드라이드, i-Bu2AlH]
분류: 시약
강의: [L5, L6]
주제태그: [환원제, 금속-수소화물, 알레인]
tags: [분류/시약, 범위/Test1, 기출/Test1-2025, 단원/산화-알켄-합성, 단원/환원, 강의/L05, 강의/L06, 시약유형/환원제, 주제/금속-수소화물, 주제/알레인]
---
# DIBAL-H

> diisobutylaluminum hydride(*i*-Bu₂AlH). ester를 −70 °C에서 환원하면 alcohol까지 가지 않고 **aldehyde에서 멈춘다**.

## 개요

ester를 [LiAlH4](LiAlH4.md)로 환원하면 중간에 aldehyde가 생기지만, aldehyde가 ester보다 반응성이 크니 곧바로 alcohol까지 가 버린다. DIBAL-H는 이 문제를 "aldehyde를 hydride가 다 사라진 뒤에야 꺼내는" 방식으로 푼다. DIBAL-H는 alane(알레인)이고, Al–H–Al 다리 결합을 가진 bridged dimer로 존재한다. 반응 자체의 메커니즘과 다른 길은 [partial reduction of esters](../반응/에스터%20부분%20환원.md) 문서에 있다. (출처: L5 p.29, L6c p.2)

## 무엇을 하나

| 기질 | 조건 | 생성물 |
|---|---|---|
| ester RCO₂Et | DIBAL, hexane, −70 °C; 그 다음 H₃O⁺ | RCHO (R = *n*-C₁₁H₂₃, 88%) |

(출처: L5 p.29)

## 메커니즘 요약

Lewis acid인 Al이 ester carbonyl O에 배위한 뒤 Al–H의 hydride가 분자 내에서 전달되어 [tetrahedral intermediate](../개념/사면체%20중간체.md) R–CH(OEt)–O–Al(*i*-Bu)₂가 생긴다. 이 intermediate가 −70 °C에서 무너지지 않으므로 반응 중에 aldehyde가 없고, H₃O⁺ 후처리에서야 aldehyde가 나온다. (출처: L5 p.29, L6c p.2)

![DIBAL-H에 의한 ester의 aldehyde 환원 종합 메커니즘: Al이 carbonyl O에 배위하고 Al–H의 hydride가 분자 내에서 carbonyl 탄소로 옮겨 가 −70 °C에서 안정한 tetrahedral intermediate가 되며, 산 처리로 aldehyde와 EtOH가 나온다](../../figures/L05/dibal_ester_mech.svg)

그림: 위 줄이 전체 반응이고 아래 줄은 단계별 풀이다(대괄호는 중간체, ⇌는 평형). 1단계(위 줄의 화살표): carbonyl O의 비공유 전자쌍(파랑, Lewis base)이 Al의 빈 p orbital(빨강, Lewis acid)로 들어가 Lewis adduct($\mathrm{O}^+$–$\mathrm{Al}^-$)가 된다. 2단계: Al–H 결합(파랑)의 hydride가 분자 내에서 carbonyl 탄소(빨강)로 옮겨 가고 C=O π 전자는 O로 올라가 tetrahedral intermediate가 된다(새 C–H는 초록). 이 intermediate는 −70 °C에서 무너지지 않으므로 aldehyde가 생기지 않고 두 번째 hydride를 받지도 않는다. 3단계(위쪽 화살표): 반응이 끝난 뒤 $\mathrm{H_3O^+}$ 로 처리하면 intermediate가 가수분해되어 aldehyde와 EtOH가 나온다. R은 $n\text{-}\mathrm{C_{11}H_{23}}$ 이고 알루미늄 부산물은 그리지 않았다. 보충: 슬라이드는 1–2단계까지 그렸고, 3단계 화살표(workup)와 Lewis adduct 단계의 분리는 보충이다. (보충 근거: Clayden p.533)

## 이웃 시약과 비교

- **[NaBH4](NaBH4.md)·[LiBH4](LiBH4.md)·[LiAlH4](LiAlH4.md):** 모두 anion성(nucleophilic) hydride다. DIBAL-H는 중성이고 Al이 Lewis acid라 먼저 산소에 배위한다는 점에서 [borane](보레인.md)과 같은 "특수 시약"으로 분류된다(→ [metal hydride의 반응성](../개념/금속%20수소화물의%20반응성.md)). (출처: L5 p.18)
- **우회로 1(alcohol 경유):** ester --[LiAlH₄]--> 1차 alcohol --[DMP, Swern 등]--> aldehyde. 마지막 단계에는 [DMP](DMP.md)나 [Swern oxidation](../반응/스원%20산화.md)처럼 aldehyde에서 멈추는 산화제를 쓴다. (출처: L6c p.2)
- **우회로 2(acid chloride 경유):** ester → carboxylic acid → acid chloride → H₂, Pd/BaSO₄, quinoline([Rosenmund reduction](../반응/로젠문트%20환원.md)). (출처: L5 p.17, p.33)

## 흔한 오해

- **"DIBAL-H는 언제나 aldehyde에서 멈춘다"**: 저온에서 tetrahedral intermediate가 안정할 때만 그렇다. (출처: L5 p.29)
- **"DIBAL-H가 약해서 멈춘다"**: 약해서가 아니라, aldehyde가 반응 중에 존재하지 않기 때문이다.

## 관련 문서

- 반응: [partial reduction of esters](../반응/에스터%20부분%20환원.md), [Rosenmund reduction](../반응/로젠문트%20환원.md), [alcohol oxidation](../반응/알코올%20산화.md)
- 비교 시약: [LiAlH4](LiAlH4.md), [LiBH4](LiBH4.md), [borane](보레인.md), [DMP](DMP.md)
- 개념: [tetrahedral intermediate](../개념/사면체%20중간체.md), [metal hydride의 반응성](../개념/금속%20수소화물의%20반응성.md)

## 출처

- [L5 환원](../../notes/L05_Reduction.md) 2절 (슬라이드 p.29)
- [L6 산화와 alkene 합성](../../notes/L06_Oxidation_and_Alkene_Synthesis.md) 0절 (L6c p.2)
