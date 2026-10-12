# L6. 알코올·알데하이드의 산화와 알켄의 입체선택적 합성 (Oxidation Reactions / Synthesis of Alkenes)

<!-- wiki-links:start -->

> **관련 위키 문서** ([[위키 대문]])
> - 반응: [[HWE 반응]], [[SN2 반응]], [[TEMPO 산화]], [[린들라 환원]], [[스원 산화]], [[알코올 산화]], [[에스터 부분 환원]], [[용해 금속 환원]], [[위티그 반응]], [[존스 산화]], [[피닉 산화]]
> - 시약: [[DIBAL-H]], [[DMP]], [[KMnO4]], [[MnO2]], [[NMO]], [[NaClO2]], [[SeO2]], [[TEMPO]], [[TPAP]], [[린들라 촉매]], [[인 일라이드]], [[존스 시약]]
> - 개념: [[금속 수소화물의 반응성]], [[알릴 양이온]], [[알켄의 입체선택적 합성]], [[옥사포스페테인]], [[입체특이성과 입체선택성]]

<!-- wiki-links:end -->

> 이 강의 노트는 **뼈대**다. 강의 순서와 슬라이드 위치만 정리했고, 설명은 링크된 개념 문서에 있다.
>
> 근거 자료: 수정본 슬라이드(L6_CM3121_Oxidation_and_Alkene_synthesis_corrected, 38쪽). "L6c p.N"은 수정본 PDF의 페이지 번호다.[^1]

## 개요

이 강의는 두 부분으로 되어 있다. 앞부분은 oxidation(산화)이다. alcohol을 aldehyde, ketone, 카복실산으로 바꾸는 시약들을 다루는데, 핵심은 "얼마나 세게 산화할 것인가"를 고르는 일이다. 그래서 DMP, Swern, TPAP, MnO₂, TEMPO처럼 aldehyde에서 멈추는 순한 산화제와, Jones 시약처럼 끝까지 밀어붙이는 강한 산화제를 구분한다. 뒷부분은 alkene의 합성이다. 같은 alkene이라도 *E*와 *Z*는 성질이 다른 별개의 화합물이므로, 한 가지 isomer만 골라 만드는 법(Lindlar, Na/NH₃, Wittig, HWE)을 배운다. 이전 강의(L2)에서 C=C를 산화해 끊거나(ozonolysis) 작용기를 붙였다면(epoxidation, dihydroxylation), 이번에는 거꾸로 C=C를 원하는 기하로 만드는 쪽을 다룬다. 강의 도입부에는 L5의 DIBAL-H 환원도 다시 나온다.

## 강의 흐름

### 0. 도입: DIBAL-H는 왜 알데하이드에서 멈추나 (복습) (L6c p.2)
- −70 °C에서 tetrahedral intermediate가 무너지지 않아 ester가 aldehyde에서 멈춘다. 다른 길은 LiAlH₄로 alcohol까지 환원한 뒤 순한 산화로 되돌리는 것(monensin 중간체).
- → [[에스터 부분 환원]], [[DIBAL-H]]

### 1. 알코올 산화의 큰 그림 (L6c p.3–6)

#### 1.1 왜 멘톨 이야기부터 하나 (p.3–5)
- geraniol → geranial(물음표 단계)은 allylic 1차 alcohol을 aldehyde에서 멈춰야 하므로 순한 산화제가 필요하다.
- → [[알코올 산화]], [[촉매 수소화]]

#### 1.2 3차 알코올은 왜 산화되지 않나 (p.6)
- 일반 메커니즘: O–LG 결합 형성 → 염기가 α-H 제거(E2형). 3차 alcohol에는 α-H가 없다.
- → [[알코올 산화]]

### 2. 알코올 → 알데하이드/케톤: 순한 산화제들 (L6c p.7–14)

#### 2.1 Dess–Martin periodinane (DMP): "I–O"가 산화제 (p.7)
- geraniol → geranial 84%. 중성·실온, 민감한 작용기에 강함. I(V) → I(III).
- → [[DMP]]

#### 2.2 Swern 산화 (1976): "S–Cl"이 산화제 (p.8–9)
- DMSO, (COCl)₂, −78 °C; Et₃N. 싸서 대량 규모, 부산물 Me₂S·CO·CO₂·HCl. 3차 OH는 남는다.
- → [[스원 산화]]

#### 2.3 TPAP/NMO (Ley–Griffith 산화): "Ru–O"가 산화제 (p.10)
- TPAP 촉매량 + NMO terminal oxidant(Ru(VII)/Ru(V) 순환).
- → [[TPAP]], [[NMO]]

#### 2.4 이산화망간 (MnO₂): "Mn–O"가 산화제 (p.10)
- 매우 순해서 allylic·benzylic alcohol만 산화한다(retinol → retinal).
- → [[MnO2]]

#### 2.5 TEMPO 산화: "N–O"가 산화제 (p.11–12)
- TEMPO 1 mol% + NaOCl/KBr. 실제 산화제는 nitrosonium(oxoammonium) cation.
- → [[TEMPO 산화]], [[TEMPO]]

#### 2.6 Cu(I)/TEMPO 호기성 산화 (Stahl oxidation) (p.13)
- (bpy)CuI/TEMPO/NMI, 공기 O₂가 terminal oxidant. C=C 유지.
- → [[TEMPO 산화]]

#### 2.7 여담: 몸 안의 알코올 산화와 "Asian flush" (p.14)
- ADH, ALDH2가 같은 순서로 산화한다. ALDH2*2 변이에서는 두 번째 단계가 병목.
- → [[알코올 산화]]

### 3. 카복실산까지 가는 산화 (L6c p.15–17)

#### 3.1 알데하이드 → 카복실산: Pinnick 산화 (1981) (p.15)
- NaClO₂, NaH₂PO₄. 2-methyl-2-butene은 HOCl scavenger(OH는 3차, Cl은 2차 탄소).
- → [[피닉 산화]], [[NaClO2]]

#### 3.2 1차 알코올 → 카복실산: Jones 산화와 "3 = 1 + 2" (p.16–17)
- Jones(CrO₃/H₂SO₄)는 강산성. 섬세한 기질은 DMP → NaClO₂ 두 단계.
- → [[존스 산화]], [[존스 시약]], [[알코올 산화]]

#### 3.3 한눈에 정리 (요약 슬라이드) (p.17)
- 순한 산화 a–f, aldehyde → 산 g, 1차 alcohol → 산 h, i.
- → [[알코올 산화]]

### 4. 벤질·알릴 C–H 결합의 산화 (L6c p.18)
- KMnO₄는 benzylic CH₃ → CO₂H(saccharin 합성), SeO₂는 allylic CH₃ → CHO(enal, sirenin 합성). SeO₂는 benzylic에는 안 듣는다.
- → [[KMnO4]], [[SeO2]]

### 5. 알켄의 합성: 왜 "한 가지 이성질체"가 중요한가 (L6c p.19–22)
- cracking·dehydrogenation은 혼합물을 준다. E2도 선호만 있고 통제는 없다(*E* 51, *Z* 18, 말단 31).
- → [[알켄의 입체선택적 합성]], [[입체특이성과 입체선택성]]

### 6. 알카인에서 알켄 만들기 (L6c p.23–25)

#### 6.1 Z-알켄: H₂ + Lindlar 촉매 (p.23)
- 피독된 Pd에서 syn 첨가 후 멈춘다(Japanese beetle pheromone, Z만).
- → [[린들라 환원]], [[린들라 촉매]]

#### 6.2 E-알켄: Na, NH₃(l), t-BuOH (p.23–24)
- SET: radical anion → vinyl radical → trans vinyl anion → *E*-alkene.
- → [[용해 금속 환원]]

#### 6.3 예: Lindlar의 선택성 (Org. Lett. 2001) (p.25)
- enyne의 C≡C만 *Z*로 환원하고 기존 *E*-C=C는 그대로 둔다(연습 문제 3).
- → [[린들라 환원]]

### 7. Wittig 반응 (L6c p.26–38)

#### 7.1 일리드란 무엇이고 어떻게 만드나 (p.26)
- PPh₃ + R–X (S<sub>N</sub>2) → phosphonium salt → 염기로 deprotonation.
- → [[인 일라이드]], [[SN2 반응]]

#### 7.2 Wittig 반응: C=O를 C=C로 바꾼다 (p.27–28)
- cyclohexanone + Ph₃P=CH₂ → methylenecyclohexane 86%. BASF vitamin A 합성.
- → [[위티그 반응]]

#### 7.3 안정화 일리드와 비안정화 일리드 (p.29)
- C=O 공액이면 stabilized(Na₂CO₃로 생성), 알킬이면 unstabilized(BuLi 필요).
- → [[인 일라이드]]

#### 7.4 입체선택성: 안정화는 E, 비안정화는 Z (p.30–31)
- → [[위티그 반응]]

#### 7.5 메커니즘: 4원 고리를 거쳐 P=O로 (p.33)
- ylide 공격 → oxaphosphetane → C=C + P=O(구동력).
- → [[위티그 반응]], [[옥사포스페테인]]

#### 7.6 비안정화 일리드는 왜 Z를 주나 (p.34–35)
- 수직 접근 → syn oxaphosphetane → stereospecific syn elimination → *Z*.
- → [[옥사포스페테인]]

#### 7.7 Horner–Wadsworth–Emmons (HWE) 반응 (p.36–37)
- phosphonate carbanion, *E*-선택적, ketone과도 반응, 수용성 phosphate 부산물.
- → [[HWE 반응]]

#### 7.8 요약 (p.38)
- alkyne → alkene: *Z*는 H₂ + Lindlar, *E*는 Na/NH₃. Wittig: *Z*는 unstabilized, *E*는 stabilized 또는 HWE.
- → [[알켄의 입체선택적 합성]]

## 반응 요약표

| 반응 | 시약/조건 | 생성물 | 선택성·입체화학 | 비고 |
|---|---|---|---|---|
| [[에스터 부분 환원]] | DIBAL-H, hexane, −70 °C; H₃O⁺ | 알데하이드 | – | 사면체 중간체가 저온에서 안정 (p.2) |
| [[DMP]] 산화 | Dess–Martin periodinane, CH₂Cl₂ | 1°→RCHO, 2°→케톤 | C=C 기하 유지 | I(V)→I(III), 중성·온화 (p.7) |
| [[스원 산화\|Swern 산화]] | (COCl)₂, DMSO, DCM, −78 °C; NEt₃ | 1°→RCHO, 2°→케톤 | 3° OH 영향 없음 | 부산물 Me₂S, CO, CO₂, HCl (p.8–9) |
| Ley–Griffith ([[TPAP]]) | TPAP(촉매), NMO(최종 산화제) | 알데하이드/케톤 | – | Ru(VII)/Ru(V) 순환 (p.10) |
| [[MnO2]] 산화 | MnO₂ | 알릴/벤질 C=O | 알릴·벤질 OH만, C=C 유지 | 일반 2° OH는 남음 (p.10) |
| [[TEMPO 산화]] | TEMPO (0.01 equiv), NaOCl, KBr (0.1 equiv), NaHCO₃, CH₂Cl₂–H₂O, 0 °C | RCHO | 1° 알코올 | 활성종은 나이트로소늄 (p.11–12) |
| Stahl 산화 ([[TEMPO 산화]]) | (bpy)CuI 5%, TEMPO 5%, NMI 10%, air/O₂, MeCN, rt | RCHO | 1° 알코올, C=C 무관 | O₂가 최종 산화제 (p.13) |
| [[피닉 산화\|Pinnick 산화]] | NaClO₂, NaH₂PO₄, 2-methyl-2-butene(또는 DMSO) | RCO₂H | – | HOCl 제거제 (p.15) |
| HOCl 제거 ([[피닉 산화]]) | 2-methyl-2-butene + HOCl | 3-chloro-2-methylbutan-2-ol | OH는 3차 C, Cl은 2차 C | Markovnikov형 (p.15) |
| [[존스 산화\|Jones 산화]] | CrO₃, H₂SO₄ (H₂CrO₄) | 1°→RCO₂H | – | 강산성, 민감한 기질에 부적합 (p.16) |
| 2단계 산화 ([[알코올 산화]]) | DMP → NaClO₂ | RCO₂H | – | "3 = 1 + 2" (p.16–17) |
| 벤질 산화 ([[KMnO4]]) | KMnO₄ | ArCO₂H | 벤질 CH₃ | 사카린 합성 (p.18) |
| 알릴 산화 ([[SeO2]]) | SeO₂ | R–CH=C(CH₃)–CHO | 알릴 CH₃; 그림상 R과 trans인 CH₃ | 벤질 CH₃에는 안 됨 (p.18) |
| [[린들라 환원\|Lindlar 수소화]] | H₂, Pd/CaCO₃/Pb(OAc)₂ | Z-알켄 | syn 첨가 → Z | 과잉 환원 없음 (p.23) |
| [[용해 금속 환원]] | Na, NH₃(l), t-BuOH | E-알켄 | trans 비닐 음이온 → E | SET (p.23–24) |
| 일리드 생성 ([[인 일라이드]]) | PPh₃ + RCH₂X (S<sub>N</sub>2); BuLi/PhLi/t-BuOK (안정화형은 Na₂CO₃) | Ph₃P=CHR | 1°/2° 할로젠화물 | (p.26, 29) |
| [[위티그 반응\|Wittig]] (비안정화) | Ph₃P=CHR (R = 알킬) + R′CHO | R–CH=CH–R′ | Z-선택적 | syn 옥사포스페테인 (p.31, 34) |
| [[위티그 반응\|Wittig]] (안정화) | Ph₃P=CHCO₂Et, Ph₃P=CHCHO 등 + RCHO | α,β-불포화 카보닐 | E-선택적 | (p.30) |
| [[HWE 반응\|HWE]] | (EtO)₂P(O)CH₂EWG, NaH/EtO⁻/KHMDS + 알데하이드·케톤 | 알켄 | E-선택적(이치환) | 수용성 포스페이트 부산물 (p.36–37) |

(쪽 번호는 모두 L6c 기준)

## 연습 문제

→ [L6 연습 문제](../practice/L06_Exercises.md)

## 출처

- 슬라이드: L6 수정본(L6c, PDF p.2–38)

[^1]: 수정본에서는 원본 p.34(Stereochemistry 슬라이드)가 p.34와 p.35에 똑같이 두 번 들어가 있다. 그래서 원본 p.35 이후 슬라이드는 수정본에서 번호가 하나씩 밀린다(원본 p.35 = L6c p.36).
