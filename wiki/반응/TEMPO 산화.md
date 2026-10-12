---
aliases: [TEMPO oxidation, Anelli oxidation, Stahl oxidation, 스탈 산화, Cu/TEMPO 산화]
분류: 반응
태그: [산화, 알코올, 촉매]
강의: [L6]
---
# TEMPO 산화

> 1차 알코올 --[TEMPO(촉매), NaOCl, KBr, NaHCO₃]--> 알데하이드. 실제 산화제는 TEMPO가 산화되어 생긴 **나이트로소늄(옥소암모늄) 양이온 N⁺=O**이고, 표백제나 공기가 최종 산화제다.

## 개요

표백제(NaOCl)는 싸지만 그대로는 선택성이 없다. [[TEMPO]](2,2,6,6-테트라메틸피페리딘 *N*-옥실)를 1 mol%만 끼우면 1차 알코올이 알데하이드에서 깔끔하게 멈춘다. TEMPO는 네 개의 메틸이 N–O• 라디칼을 둘러싸 보호하는 안정한 나이트록실 라디칼이다. 더 나아가 구리와 함께 쓰면 공기 중 O₂를 최종 산화제로 쓸 수도 있다(Stahl 산화). (출처: L6c p.11, p.13)

## 메커니즘 (NaOCl 계)

1. OCl⁻(최종 산화제)가 Br⁻(공촉매)를 OBr⁻로 산화한다.
2. OBr⁻가 TEMPO(또는 하이드록실아민)를 나이트로소늄 양이온 N⁺=O로 산화한다.
3. 염기성 조건의 알콕사이드 RCH₂O⁻가 N⁺를 공격해 부가물(I) N(O⁻)–O–CH₂R이 된다.
4. N의 O⁻가 분자 내에서 α-H를 떼고 N–O(알콕시) 결합이 끊어져 RCHO와 하이드록실아민(TEMPO-H)이 생긴다.
5. 하이드록실아민이 다시 산화되어 순환이 닫힌다.

(출처: L6c p.11–12)

![TEMPO 부가물(I)에서 분자 내 α-H 제거로 알데하이드와 하이드록실아민이 생기는 단계](../../figures/L06/tempo_adduct.svg)

*그림: 4단계. N의 O⁻(파랑)가 α-H(빨강)를 떼고, C–H 전자는 C=O로, N⁺–O 전자는 N으로 돌아간다. [[알코올 산화]] 일반 뼈대에서 "LG = N⁺, 염기 = 분자 내 O⁻"인 경우다.*

## Cu/TEMPO 호기성 산화 (Stahl)

RCH₂OH --[5% (bpy)CuI, 5% TEMPO, 10% NMI, 공기 또는 O₂, MeCN, rt]--> RCHO

촉매 순환은 두 반쪽이다. (1) Cu(I) + TEMPO-H + ½O₂ → Cu(II)–OH + TEMPO•, (2) Cu(II)–OH + TEMPO• + RCH₂OH → RCHO + H₂O + Cu(I) + TEMPO-H. 결국 O₂가 물이 되는 만큼 알코올이 산화된다. (출처: L6c p.13)

## 선택성

- 1차 알코올을 알데하이드에서 멈춘다. 분자 안의 C=C는 그대로 남는다. (출처: L6c p.11, p.13)
- 보충: Stahl 계는 1차 알코올을 2차 알코올보다 훨씬 빠르게 산화하는 것으로 알려져 있다.

## 예

- 1-헵탄올 --[TEMPO, NaOCl, KBr, NaHCO₃, CH₂Cl₂–H₂O, 0 °C]--> 헵탄알
- 신나밀 알코올 PhCH=CHCH₂OH --[같은 조건]--> 신남알데하이드 PhCH=CHCHO (C=C 유지)

(출처: L6c p.11)

## 흔한 오해

- "TEMPO 라디칼이 알코올을 직접 산화한다": 실제 산화제는 나이트로소늄 양이온이다. TEMPO는 촉매이고 NaOCl(또는 O₂)이 최종 산화제다. 보충: 슬라이드가 쓰는 "nitrosonium cation"은 정식으로는 옥소암모늄(oxoammonium) 이온이라 부르는 경우가 많다. (출처: L6c p.12)
- "KBr은 산화제다": Br⁻는 OCl⁻와 TEMPO 사이를 잇는 공촉매다.

## 관련 문서

- 시약: [[TEMPO]], [[DMP]], [[TPAP]]
- 반응: [[알코올 산화]], [[스원 산화]], [[피닉 산화]]

## 출처

- [L6 산화와 알켄 합성](../../notes/L06_Oxidation_and_Alkene_Synthesis.md) 2.5절, 2.6절
