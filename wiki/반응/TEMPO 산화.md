---
aliases: [TEMPO oxidation, Anelli oxidation, Stahl oxidation, 스탈 산화, Cu/TEMPO 산화]
분류: 반응
강의: [L6]
주제태그: [산화, 알코올, 촉매]
tags: [분류/반응, 범위/Test1, 단원/산화-알켄-합성, 강의/L06, 유형/산화, 주제/알코올]
---
# TEMPO 산화

> 1차 alcohol --[TEMPO(촉매), NaOCl, KBr, NaHCO₃]--> aldehyde. 실제 산화제는 TEMPO가 산화되어 생긴 **nitrosonium(oxoammonium) cation N⁺=O**이고, 표백제나 공기가 terminal oxidant다.

## 개요

값싼 NaOCl을 산화제로 쓸 수는 없을까? 표백제만으로는 선택성이 없지만, [TEMPO](../시약/TEMPO.md)라는 촉매를 끼우면 aldehyde에서 깔끔하게 멈춘다. TEMPO는 2,2,6,6-tetramethylpiperidine N-oxyl(슬라이드 표기 "tetramethylpiperidine N-oxide")로, 네 개의 methyl이 N–O• radical을 둘러싸 보호하고 있는 안정한 nitroxyl radical이다(m.p. 36–38 °C). 슬라이드는 이 계를 "N–O" 산화제로 부른다. 더 나아가 구리와 함께 쓰면 공기 중 O₂를 terminal oxidant로 쓸 수도 Stahl oxidation. (출처: L6c p.11, p.13)

$$
\mathrm{RCH_2OH} + \mathrm{NaOCl} \xrightarrow[\mathrm{NaHCO_3},\ \mathrm{CH_2Cl_2{-}H_2O},\ 0\thinspace{}^\circ\mathrm{C}]{\mathrm{TEMPO},\ \mathrm{KBr}} \mathrm{RCHO}
$$

(KBr 0.1 mol equiv, TEMPO 0.01 mol equiv)

## 메커니즘 (NaOCl 계)

그런데 TEMPO가 1 mol%만 있어도 반응이 끝까지 가는 이유는 무엇일까? 답은 촉매 순환에 있다. 일종의 산화 릴레이로 보면 된다.

1. OCl⁻(terminal oxidant)가 Br⁻(co-catalyst)를 OBr⁻로 산화하고, 자신은 Cl⁻가 된다.
2. OBr⁻가 TEMPO(또는 hydroxylamine)를 nitrosonium cation(N⁺=O)으로 산화한다.[^1] alcohol을 실제로 산화하는 것은 이 cation이다.
3. 염기성 조건에서 생긴 alkoxide R¹CH₂O⁻가 N⁺를 공격해 intermediate 부가물(I), 즉 N(O⁻)–O–CH₂R¹이 생긴다.
4. N에 붙은 O⁻가 분자 내에서 α-H를 떼어 내고, N–O(alkoxy) 결합이 끊어진다. 그 결과 carbonyl R¹CHO와 hydroxylamine(TEMPO-H, N–OH)이 생긴다.
5. hydroxylamine은 다시 TEMPO를 거쳐 nitrosonium으로 산화되어 순환이 닫힌다.

(출처: L6c p.11–12)

![TEMPO 산화의 intermediate 부가물(I)에서 분자 내 α-H 제거로 aldehyde와 hydroxylamine이 생기는 단계](../../figures/L06/tempo_adduct.svg)

그림: 위 4단계(L6c p.12의 intermediate adduct (I)). N에 붙은 O⁻(파랑)의 lone pair가 같은 분자 안의 α-H(빨강)를 떼어 간다. 그 C–H 결합 전자(파란 결합)는 C–O 사이로 들어가 C=O가 되고, N⁺–O(alkoxy) 결합(빨강) 전자는 N으로 돌아가 N⁺가 중성 N이 된다. 결과는 aldehyde(초록 C=O)와 hydroxylamine(N–OH)이다. [alcohol oxidation](알코올%20산화.md) 일반 메커니즘에서 "LG = N⁺, 염기 = 분자 내 O⁻"인 경우로 보면 된다.

## Cu(I)/TEMPO 호기성 산화 (Stahl oxidation)

표백제보다 더 싼 산화제는 공기다. 그렇다면 공기 중의 O₂로 alcohol을 산화할 수 있을까? Stahl oxidation은 TEMPO와 구리를 함께 촉매로 써서 이것을 해낸다.

$$
\mathrm{RCH_2OH} \xrightarrow[\mathrm{NMI},\ \mathrm{MeCN},\ \text{rt}]{\mathrm{(bpy)CuI},\ \mathrm{TEMPO}} \mathrm{RCHO}
$$

(산화제: air 또는 $\mathrm{O_2}$)
($\mathrm{(bpy)CuI}$ 5%, TEMPO 5%, NMI 10%)

(bpy = 2,2′-bipyridine, NMI = N-methylimidazole)

슬라이드의 촉매 순환은 두 반쪽으로 나뉜다.

1. catalyst oxidation(촉매 산화): (bpy)Cu^I–NMI + TEMPO-H + ½ O₂ → (bpy)Cu^II(OH)–NMI + TEMPO•
2. substrate oxidation(기질 산화): Cu^II–OH + TEMPO• + RCH₂OH → RCHO + H₂O + Cu^I + TEMPO-H

결국 O₂가 물이 되면서 그만큼 alcohol이 산화된다. (출처: L6c p.13)

## 선택성

- 1차 alcohol을 aldehyde에서 멈춘다. 분자 안의 C=C는 그대로 남는다. (출처: L6c p.11, p.13)
- Stahl 계의 chemoselectivity 예: 내부 C=C(*E*)를 가진 1차 alcohol이 [(bpy)Cu^I(NMI)]X(X⁻ = Br⁻, OTf⁻, BF₄⁻, PF₆⁻), TEMPO, MeCN, 공기, 22 °C 조건에서 aldehyde가 되고 C=C는 손대지 않는다.[^2] (출처: L6c p.13)

## 예

- $\text{1-heptanol} \xrightarrow[\mathrm{KBr},\ \mathrm{NaHCO_3}]{\mathrm{TEMPO},\ \mathrm{NaOCl}} \text{heptanal}$ ($\mathrm{CH_2Cl_2{-}H_2O}$, 0 °C)

  (L6)
- $\text{cinnamyl alcohol}\ \mathrm{PhCH{=}CHCH_2OH}$ $\xrightarrow{\text{같은 조건}} \text{cinnamaldehyde}\ \mathrm{PhCH{=}CHCHO}$

  (C=C 유지) (L6)

(출처: L6c p.11)

## 흔한 오해

- **"TEMPO radical이 alcohol을 직접 산화한다"고 생각하기 쉽지만**, 사실 실제 산화제는 TEMPO가 산화되어 생긴 nitrosonium(oxoammonium) cation N⁺=O다. TEMPO는 촉매이고, NaOCl(또는 Stahl 계의 O₂)이 terminal oxidant다. (출처: L6c p.12)
- **"KBr은 산화제다"**: Br⁻는 OCl⁻와 TEMPO 사이를 잇는 co-catalyst다. (출처: L6c p.11)

## 관련 문서

- 시약: [TEMPO](../시약/TEMPO.md), [DMP](../시약/DMP.md), [TPAP](../시약/TPAP.md)
- 반응: [alcohol oxidation](알코올%20산화.md), [Swern oxidation](스원%20산화.md), [Pinnick oxidation](피닉%20산화.md)

## 출처

- [L6 산화와 alkene 합성](../../notes/L06_Oxidation_and_Alkene_Synthesis.md) 2절 (L6c p.11–13)

[^1]: 슬라이드는 "nitrosonium cation"이라고 부르지만, 정식으로는 oxoammonium 이온이라고 부르는 경우가 많다. 슬라이드의 TEMPO 이름 "tetramethylpiperidine N-oxide"도 정확히는 2,2,6,6-tetramethylpiperidin-1-oxyl(nitroxyl radical)이다.
[^2]: 보충: Stahl 계는 1차 alcohol을 2차 alcohol보다 훨씬 빠르게 산화하는 것으로 알려져 있다.
