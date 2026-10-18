# L6. 알코올·알데하이드의 산화와 알켄의 입체선택적 합성 (Oxidation Reactions / Synthesis of Alkenes)

<!-- wiki-links:start -->

> **관련 위키 문서** ([위키 대문](../wiki/위키%20대문.md))
> - 반응: [alcohol oxidation](../wiki/반응/알코올%20산화.md), [dissolving metal reduction](../wiki/반응/용해%20금속%20환원.md), [Horner–Wadsworth–Emmons reaction](../wiki/반응/HWE%20반응.md), [Jones oxidation](../wiki/반응/존스%20산화.md), [Lindlar reduction](../wiki/반응/린들라%20환원.md), [partial reduction of esters](../wiki/반응/에스터%20부분%20환원.md), [Pinnick oxidation](../wiki/반응/피닉%20산화.md), [SN2 reaction](../wiki/반응/SN2%20반응.md), [Swern oxidation](../wiki/반응/스원%20산화.md), [TEMPO oxidation](../wiki/반응/TEMPO%20산화.md), [Wittig reaction](../wiki/반응/위티그%20반응.md)
> - 시약: [DIBAL-H](../wiki/시약/DIBAL-H.md), [DMP](../wiki/시약/DMP.md), [Jones reagent](../wiki/시약/존스%20시약.md), [KMnO4](../wiki/시약/KMnO4.md), [Lindlar catalyst](../wiki/시약/린들라%20촉매.md), [MnO2](../wiki/시약/MnO2.md), [NaClO2](../wiki/시약/NaClO2.md), [NMO](../wiki/시약/NMO.md), [phosphorus ylide](../wiki/시약/인%20일라이드.md), [SeO2](../wiki/시약/SeO2.md), [TEMPO](../wiki/시약/TEMPO.md), [TPAP](../wiki/시약/TPAP.md)
> - 개념: [allyl cation](../wiki/개념/알릴%20양이온.md), [metal hydride reactivity](../wiki/개념/금속%20수소화물의%20반응성.md), [oxaphosphetane](../wiki/개념/옥사포스페테인.md), [stereoselective alkene synthesis](../wiki/개념/알켄의%20입체선택적%20합성.md), [stereospecificity and stereoselectivity](../wiki/개념/입체특이성과%20입체선택성.md)

<!-- wiki-links:end -->

> 이 강의 노트는 **뼈대**다. 강의 순서와 슬라이드 위치만 정리했고, 설명은 링크된 개념 문서에 있다.

> 강의 흐름대로 길게 읽고 싶으면 **[통독본](통독/L06_Oxidation_and_Alkene_Synthesis.md)**(재구성 직전의 전체 노트, 소절마다 개념 문서 링크 포함)을 본다.
>
> 근거 자료: 수정본 슬라이드(L6_CM3121_Oxidation_and_Alkene_synthesis_corrected, 38쪽). "L6c p.N"은 수정본 PDF의 페이지 번호다.[^1]

## 개요

이 강의는 두 부분으로 되어 있다. 앞부분은 oxidation(산화)이다. alcohol을 aldehyde, ketone, carboxylic acid로 바꾸는 시약들을 다루는데, 핵심은 "얼마나 세게 산화할 것인가"를 고르는 일이다. 그래서 DMP, Swern, TPAP, MnO₂, TEMPO처럼 aldehyde에서 멈추는 순한 산화제와, Jones 시약처럼 끝까지 밀어붙이는 강한 산화제를 구분한다. 뒷부분은 alkene의 합성이다. 같은 alkene이라도 *E*와 *Z*는 성질이 다른 별개의 화합물이므로, 한 가지 isomer만 골라 만드는 법(Lindlar, Na/NH₃, Wittig, HWE)을 배운다. 이전 강의(L2)에서 C=C를 산화해 ozonolysis 작용기를 epoxidation, dihydroxylation, 이번에는 거꾸로 C=C를 원하는 기하로 만드는 쪽을 다룬다. 강의 도입부에는 L5의 DIBAL-H 환원도 다시 나온다.

## 강의 흐름

### 0. 도입: DIBAL-H는 왜 aldehyde에서 멈추나 (복습) (L6c p.2)
- −70 °C에서 tetrahedral intermediate가 무너지지 않아 ester가 aldehyde에서 멈춘다. 다른 길은 LiAlH₄로 alcohol까지 환원한 뒤 순한 산화로 되돌리는 것(monensin intermediate).
- → [partial reduction of esters](../wiki/반응/에스터%20부분%20환원.md), [DIBAL-H](../wiki/시약/DIBAL-H.md)

### 1. alcohol 산화의 큰 그림 (L6c p.3–6)

#### 1.1 왜 menthol 이야기부터 하나 (p.3–5)
- $\begin{aligned} & \text{geraniol} \\ & \longrightarrow \\ & \text{geranial}(\text{물음표 단계})\text{은}\  \\ & \begin{gathered}\text{allylic 1차 alcohol을 aldehyde에서 멈춰야 하므로 순한 } \\  \\ & \text{산화제가 필요하다}\end{gathered} \end{aligned}$.
- → [alcohol oxidation](../wiki/반응/알코올%20산화.md), [catalytic hydrogenation](../wiki/반응/촉매%20수소화.md)

#### 1.2 3차 alcohol은 왜 산화되지 않나 (p.6)
- 일반 메커니즘: $\mathrm{O{-}LG}\ \text{결합 형성} \longrightarrow \text{염기가}\ \alpha\ \mathrm{{-}H}\ \text{제거(E2형)}$. 3차 alcohol에는 $\alpha$-H가 없다.
- → [alcohol oxidation](../wiki/반응/알코올%20산화.md)

$\mathrm{\#\#\#}\ 2.\ \text{alcohol} \longrightarrow \text{aldehyde/ketone: 순한 산화제들}$ (L6c p.7–14)

#### 2.1 Dess–Martin periodinane (DMP): "I–O"가 산화제 (p.7)
- geraniol → geranial 84%. 중성·실온, 민감한 작용기에 강함. I(V) → I(III).
- → [DMP](../wiki/시약/DMP.md)

#### 2.2 Swern oxidation (1976): "S–Cl"이 산화제 (p.8–9)
- DMSO, (COCl)₂, −78 °C; Et₃N. 싸서 대량 규모, 부산물 Me₂S·CO·CO₂·HCl. 3차 OH는 남는다.
- → [Swern oxidation](../wiki/반응/스원%20산화.md)

#### 2.3 TPAP/NMO (Ley–Griffith oxidation): "Ru–O"가 산화제 (p.10)
- TPAP 촉매량 + NMO terminal oxidant(Ru(VII)/Ru(V) 순환).
- → [TPAP](../wiki/시약/TPAP.md), [NMO](../wiki/시약/NMO.md)

#### 2.4 manganese dioxide (MnO₂): "Mn–O"가 산화제 (p.10)
- $\begin{aligned} & \text{매우 순해서 allylic·benzylic alcohol만}\  \\ & \text{산화한다}(\text{retinol}) \\ & \longrightarrow \text{retinal)} \end{aligned}$.
- → [MnO2](../wiki/시약/MnO2.md)

#### 2.5 TEMPO oxidation: "N–O"가 산화제 (p.11–12)
- TEMPO 1 mol% + NaOCl/KBr. 실제 산화제는 nitrosonium(oxoammonium) cation.
- → [TEMPO oxidation](../wiki/반응/TEMPO%20산화.md), [TEMPO](../wiki/시약/TEMPO.md)

#### 2.6 Cu(I)/TEMPO 호기성 산화 (Stahl oxidation) (p.13)
- (bpy)CuI/TEMPO/NMI, 공기 O₂가 terminal oxidant. C=C 유지.
- → [TEMPO oxidation](../wiki/반응/TEMPO%20산화.md)

#### 2.7 여담: 몸 안의 alcohol 산화와 "Asian flush" (p.14)
- ADH, ALDH2가 같은 순서로 산화한다. ALDH2*2 변이에서는 두 번째 단계가 병목.
- → [alcohol oxidation](../wiki/반응/알코올%20산화.md)

### 3. carboxylic acid까지 가는 산화 (L6c p.15–17)

$$
\begin{aligned}
& \mathrm{\#\#\#\#}\ 3.1\ \text{aldehyde} \\
& \longrightarrow \text{carboxylic acid: Pinnick oxidation}\ (1981)\ \mathrm{(p.15)}
\end{aligned}
$$
- NaClO₂, NaH₂PO₄. 2-methyl-2-butene은 HOCl scavenger(OH는 3차, Cl은 2차 탄소).
- → [Pinnick oxidation](../wiki/반응/피닉%20산화.md), [NaClO2](../wiki/시약/NaClO2.md)

$$
\begin{aligned}
& \mathrm{\#\#\#\#}\ 3.2\ \text{1차 alcohol} \\
& \longrightarrow \text{carboxylic acid: Jones 산화와}\ \mathrm{"3}\ =\ 1 + \mathrm{2"\,(p.16{-}17)}
\end{aligned}
$$
- Jones(CrO₃/H₂SO₄)는 강산성. $\text{섬세한 기질은}\ \mathrm{DMP} \longrightarrow \mathrm{NaClO_2}\ \text{두 단계}$.
- → [Jones oxidation](../wiki/반응/존스%20산화.md), [Jones reagent](../wiki/시약/존스%20시약.md), [alcohol oxidation](../wiki/반응/알코올%20산화.md)

#### 3.3 한눈에 정리 (요약 슬라이드) (p.17)
- $\begin{aligned} & \text{순한 산화}\ \mathrm{a{-}f},\ \text{aldehyde} \\ & \longrightarrow \text{산}\ \mathrm{g},\ \text{1차 alcohol} \\ & \longrightarrow \text{산 h},\ \mathrm{i} \end{aligned}$.
- → [alcohol oxidation](../wiki/반응/알코올%20산화.md)

### 4. benzyl·allyl C–H 결합의 산화 (L6c p.18)
- $\begin{aligned} & \mathrm{KMnO_4}\text{는}\ \text{benzylic}\ \mathrm{CH_3} \\ & \longrightarrow \mathrm{CO_2H}(\text{saccharin 합성}),\ \mathrm{SeO_2}\text{는}\ \text{allylic}\ \mathrm{CH_3} \\ & \longrightarrow \mathrm{CHO}(\text{enal},\ \text{sirenin 합성}) \end{aligned}$. SeO₂는 benzylic에는 안 듣는다.
- → [KMnO4](../wiki/시약/KMnO4.md), [SeO2](../wiki/시약/SeO2.md)

### 5. alkene의 합성: 왜 "한 가지 isomer"가 중요한가 (L6c p.19–22)
- cracking·dehydrogenation은 혼합물을 준다. E2도 선호만 있고 통제는 없다(*E* 51, *Z* 18, 말단 31).
- → [stereoselective alkene synthesis](../wiki/개념/알켄의%20입체선택적%20합성.md), [stereospecificity와 stereoselectivity](../wiki/개념/입체특이성과%20입체선택성.md)

### 6. alkyne에서 alkene 만들기 (L6c p.23–25)

#### 6.1 Z-alkene: H₂ + Lindlar catalyst (p.23)
- 피독된 Pd에서 syn 첨가 후 멈춘다(Japanese beetle pheromone, Z만).
- → [Lindlar reduction](../wiki/반응/린들라%20환원.md), [Lindlar catalyst](../wiki/시약/린들라%20촉매.md)

#### 6.2 E-alkene: Na, NH₃(l), t-BuOH (p.23–24)
- SET: $\begin{aligned} & \text{radical anion} \\ & \longrightarrow \text{vinyl radical} \\ & \longrightarrow \text{trans vinyl anion} \\ & \longrightarrow \mathit{E}\ \text{-alkene} \end{aligned}$.
- → [dissolving metal reduction](../wiki/반응/용해%20금속%20환원.md)

#### 6.3 예: Lindlar의 선택성 (Org. Lett. 2001) (p.25)
- enyne의 C≡C만 *Z*로 환원하고 기존 *E*-C=C는 그대로 둔다(연습 문제 3).
- → [Lindlar reduction](../wiki/반응/린들라%20환원.md)

### 7. Wittig reaction (L6c p.26–38)

#### 7.1 ylide란 무엇이고 어떻게 만드나 (p.26)
- $\begin{aligned} & \mathrm{PPh_3} + \mathrm{R{-}X\,(S<sub>N</sub>2)} \\ & \longrightarrow \text{phosphonium salt} \\ & \longrightarrow \text{염기로 deprotonation} \end{aligned}$.
- → [phosphorus ylide](../wiki/시약/인%20일라이드.md), [SN2 reaction](../wiki/반응/SN2%20반응.md)

#### 7.2 Wittig reaction: C=O를 C=C로 바꾼다 (p.27–28)
- $\text{cyclohexanone} + \mathrm{Ph_3P{=}CH_2} \longrightarrow \text{methylenecyclohexane}\ 86\%$. BASF vitamin A 합성.
- → [Wittig reaction](../wiki/반응/위티그%20반응.md)

#### 7.3 안정화 ylide와 비안정화 ylide (p.29)
- C=O 공액이면 stabilized(Na₂CO₃로 생성), alkyl이면 unstabilized(BuLi 필요).
- → [phosphorus ylide](../wiki/시약/인%20일라이드.md)

#### 7.4 stereoselectivity: 안정화는 E, 비안정화는 Z (p.30–31)
- → [Wittig reaction](../wiki/반응/위티그%20반응.md)

#### 7.5 메커니즘: 4원 고리를 거쳐 P=O로 (p.33)
- $\begin{aligned} & \text{ylide 공격} \\ & \longrightarrow \text{oxaphosphetane} \\ & \longrightarrow \mathrm{C{=}C} + \mathrm{P{=}O(}\text{구동력)} \end{aligned}$.
- → [Wittig reaction](../wiki/반응/위티그%20반응.md), [oxaphosphetane](../wiki/개념/옥사포스페테인.md)

#### 7.6 비안정화 ylide는 왜 Z를 주나 (p.34–35)
- 수직 접근 → syn oxaphosphetane → stereospecific syn elimination → *Z*.
- → [oxaphosphetane](../wiki/개념/옥사포스페테인.md)

#### 7.7 Horner–Wadsworth–Emmons (HWE) 반응 (p.36–37)
- phosphonate carbanion, *E*-선택적, ketone과도 반응, 수용성 phosphate 부산물.
- → [Horner–Wadsworth–Emmons reaction](../wiki/반응/HWE%20반응.md)

#### 7.8 요약 (p.38)
- $\text{alkyne} \longrightarrow \text{alkene:}\ \mathit{Z}\ \text{는}\ \mathrm{H_2} + \text{Lindlar},\ \mathit{E}\ \text{는}\ \mathrm{Na/NH_3}$. Wittig: *Z*는 unstabilized, *E*는 stabilized 또는 HWE.
- → [stereoselective alkene synthesis](../wiki/개념/알켄의%20입체선택적%20합성.md)

## 반응 요약표

| 반응 | 시약/조건 | 생성물 | 선택성·stereochemistry | 비고 |
|---|---|---|---|---|
| [partial reduction of esters](../wiki/반응/에스터%20부분%20환원.md) | DIBAL-H, hexane, −70 °C; H₃O⁺ | aldehyde | – | tetrahedral intermediate가 저온에서 안정 (p.2) |
| [DMP](../wiki/시약/DMP.md) 산화 | Dess–Martin periodinane, CH₂Cl₂ | $\begin{aligned} & \mathrm{1^\circ } \\ & \longrightarrow \mathrm{RCHO},\ \mathrm{2^\circ } \\ & \longrightarrow \text{ketone} \end{aligned}$ | C=C 기하 유지 | I(V)→I(III), 중성·온화 (p.7) |
| [Swern oxidation](../wiki/반응/스원%20산화.md) | (COCl)₂, DMSO, DCM, −78 °C; NEt₃ | $\begin{aligned} & \mathrm{1^\circ } \\ & \longrightarrow \mathrm{RCHO},\ \mathrm{2^\circ } \\ & \longrightarrow \text{ketone} \end{aligned}$ | 3° OH 영향 없음 | 부산물 Me₂S, CO, CO₂, HCl (p.8–9) |
| Ley–Griffith ([TPAP](../wiki/시약/TPAP.md)) | TPAP(촉매), NMO(최종 산화제) | aldehyde/ketone | – | Ru(VII)/Ru(V) 순환 (p.10) |
| [MnO2](../wiki/시약/MnO2.md) 산화 | MnO₂ | allyl/benzyl C=O | allyl·benzyl OH만, C=C 유지 | 일반 2° OH는 남음 (p.10) |
| [TEMPO oxidation](../wiki/반응/TEMPO%20산화.md) | TEMPO (0.01 equiv), NaOCl, KBr (0.1 equiv), NaHCO₃, CH₂Cl₂–H₂O, 0 °C | RCHO | 1° alcohol | 활성종은 nitrosonium (p.11–12) |
| Stahl oxidation ([TEMPO oxidation](../wiki/반응/TEMPO%20산화.md)) | (bpy)CuI 5%, TEMPO 5%, NMI 10%, air/O₂, MeCN, rt | RCHO | 1° alcohol, C=C 무관 | O₂가 최종 산화제 (p.13) |
| [Pinnick oxidation](../wiki/반응/피닉%20산화.md) | NaClO₂, NaH₂PO₄, 2-methyl-2-butene(또는 DMSO) | RCO₂H | – | HOCl 제거제 (p.15) |
| HOCl 제거 ([Pinnick oxidation](../wiki/반응/피닉%20산화.md)) | 2-methyl-2-butene + HOCl | 3-chloro-2-methylbutan-2-ol | OH는 3차 C, Cl은 2차 C | Markovnikov형 (p.15) |
| [Jones oxidation](../wiki/반응/존스%20산화.md) | CrO₃, H₂SO₄ (H₂CrO₄) | 1°→RCO₂H | – | 강산성, 민감한 기질에 부적합 (p.16) |
| 2단계 산화 ([alcohol oxidation](../wiki/반응/알코올%20산화.md)) | DMP → NaClO₂ | RCO₂H | – | "3 = 1 + 2" (p.16–17) |
| benzyl 산화 ([KMnO4](../wiki/시약/KMnO4.md)) | KMnO₄ | ArCO₂H | benzyl CH₃ | saccharin 합성 (p.18) |
| allyl 산화 ([SeO2](../wiki/시약/SeO2.md)) | SeO₂ | R–CH=C(CH₃)–CHO | allyl CH₃; 그림상 R과 trans인 CH₃ | benzyl CH₃에는 안 됨 (p.18) |
| [Lindlar hydrogenation](../wiki/반응/린들라%20환원.md) | H₂, Pd/CaCO₃/Pb(OAc)₂ | Z-alkene | syn 첨가 → Z | 과잉 환원 없음 (p.23) |
| [dissolving metal reduction](../wiki/반응/용해%20금속%20환원.md) | Na, NH₃(l), t-BuOH | E-alkene | trans vinyl anion → E | SET (p.23–24) |
| ylide 생성 ([phosphorus ylide](../wiki/시약/인%20일라이드.md)) | PPh₃ + RCH₂X (S<sub>N</sub>2); BuLi/PhLi/t-BuOK (안정화형은 Na₂CO₃) | Ph₃P=CHR | 1°/2° halide | (p.26, 29) |
| [Wittig](../wiki/반응/위티그%20반응.md) (비안정화) | Ph₃P=CHR (R = alkyl) + R′CHO | R–CH=CH–R′ | Z-선택적 | syn oxaphosphetane (p.31, 34) |
| [Wittig](../wiki/반응/위티그%20반응.md) (안정화) | Ph₃P=CHCO₂Et, Ph₃P=CHCHO 등 + RCHO | $\alpha,\beta$-unsaturated carbonyl | E-선택적 | (p.30) |
| [HWE](../wiki/반응/HWE%20반응.md) | (EtO)₂P(O)CH₂EWG, NaH/EtO⁻/KHMDS + aldehyde·ketone | alkene | E-선택적(이치환) | 수용성 phosphate 부산물 (p.36–37) |

(쪽 번호는 모두 L6c 기준)

## 연습 문제

→ [L6 연습 문제](../practice/L06_Exercises.md)

## 출처

- 슬라이드: L6 수정본(L6c, PDF p.2–38)

[^1]: 수정본에서는 원본 p.34(Stereochemistry 슬라이드)가 p.34와 p.35에 똑같이 두 번 들어가 있다. 그래서 원본 p.35 이후 슬라이드는 수정본에서 번호가 하나씩 밀린다(원본 p.35 = L6c p.36).
