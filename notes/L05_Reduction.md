# L5. 환원 반응 (Reduction reactions)

<!-- wiki-links:start -->

> **관련 위키 문서** ([위키 대문](../wiki/위키%20대문.md))
> - 반응: [amide reduction](../wiki/반응/아마이드%20환원.md), [amine synthesis via azide and nitrile](../wiki/반응/아자이드·나이트릴을%20거친%20아민%20합성.md), [catalytic hydrogenation](../wiki/반응/촉매%20수소화.md), [Eschweiler–Clarke reaction](../wiki/반응/에슈바일러-클라크%20반응.md), [hydrogenolysis](../wiki/반응/수소화분해.md), [partial reduction of esters](../wiki/반응/에스터%20부분%20환원.md), [reductive amination](../wiki/반응/환원성%20아미노화.md), [Rosenmund reduction](../wiki/반응/로젠문트%20환원.md), [SN2 reaction](../wiki/반응/SN2%20반응.md), [Staudinger reduction](../wiki/반응/스타우딩거%20환원.md)
> - 시약: [benzyl ether protecting group](../wiki/시약/벤질%20에터%20보호기.md), [borane](../wiki/시약/보레인.md), [DIBAL-H](../wiki/시약/DIBAL-H.md), [LiAlH4](../wiki/시약/LiAlH4.md), [LiBH4](../wiki/시약/LiBH4.md), [NaBH3CN](../wiki/시약/NaBH3CN.md), [NaBH4](../wiki/시약/NaBH4.md), [Pd/C](../wiki/시약/Pd-C.md), [PtO2](../wiki/시약/PtO2.md), [pyrrolidine](../wiki/시약/피롤리딘.md)
> - 개념: [amine synthesis (overview)](../wiki/개념/아민%20합성%20개관.md), [electrophile and nucleophile](../wiki/개념/친전자체와%20친핵체.md), [imine](../wiki/개념/이민.md), [iminium ion](../wiki/개념/이미늄%20이온.md), [metal hydride reactivity](../wiki/개념/금속%20수소화물의%20반응성.md), [tetrahedral intermediate](../wiki/개념/사면체%20중간체.md)

<!-- wiki-links:end -->

> 이 강의 노트는 **뼈대**다. 강의 순서와 슬라이드 위치만 정리했고, 설명은 링크된 개념 문서에 있다.

> 강의 흐름대로 길게 읽고 싶으면 **[통독본](통독/L05_Reduction.md)**(재구성 직전의 전체 노트, 소절마다 개념 문서 링크 포함)을 본다.
>
> CM3121 Advanced Organic Chemistry, Dr. Zhu Ye. 출처 표기의 p.는 PDF 페이지 번호다.

## 개요

이 강의는 "분자에 수소를 붙이는 법", 즉 reduction(환원)을 다룬다. 출발점은 amine이다. 몸과 약에서 중요한 분자 상당수가 질소를 품고 있는데 amine을 깔끔하게 만드는 일은 까다롭기 때문에, 강의는 amine 합성 문제를 실마리 삼아 azide·nitrile·amide·imine을 환원하는 방법으로 넘어간다. 거기서 NaBH₄, LiBH₄, LiAlH₄, BH₃, DIBAL-H라는 metal hydride 시약 세트를 정리하고, 마지막으로 H₂와 금속 촉매를 쓰는 catalytic hydrogenation으로 마무리한다. 핵심 질문은 "분자 안에 환원될 수 있는 자리가 여러 개일 때, 원하는 곳만 환원하려면 어떤 시약을 골라야 하나?"이다. L1의 hydroboration에서 만난 BH₃가 여기서는 carbonyl 환원제로 다시 등장하고, 이후 L7(enolate), L10(enamine/iminium), L12(protecting group)에서도 이 강의의 시약들이 계속 쓰인다.

## 강의 흐름

### 1. amine이란 무엇이고, 왜 만들기 어려운가 (슬라이드 p.2–16)

#### 1-0. 일상 속 질소 화합물 (p.2–3)
- serotonin·dopamine 등 neurotransmitter와 vitamin·약물 상당수가 질소 화합물이라 amine 합성은 기본기다.
- → [amine synthesis (overview)](../wiki/개념/아민%20합성%20개관.md)

#### 1-0-1. amine의 분류와 성질 (p.4)
- 1·2·3차 amine과 4차 ammonium salt. N의 lone pair 때문에 base·nucleophile이지만 amide는 염기성·친핵성이 약하다. 고리형 amine 이름(azepane~aziridine).
- → [amine synthesis (overview)](../wiki/개념/아민%20합성%20개관.md), [pyrrolidine](../wiki/시약/피롤리딘.md)

#### 1-1. S<sub>N</sub>2로 amine 만들기: 왜 생각대로 안 되나 (p.5–6)
- NH₃ + RX는 생성 amine이 더 좋은 nucleophile이라 over-alkylation이 일어난다(NH₃ 2 eq에서 1차 45%, 2차 43%).
- → [amine synthesis (overview)](../wiki/개념/아민%20합성%20개관.md), [SN2 reaction](../wiki/반응/SN2%20반응.md)

#### 1-1a. azide 이온 alkylation 후 환원 (p.7)
- R–N₃는 더 이상 nucleophile이 아니라 한 번에서 멈추고, LiAlH₄·H₂/Pd·PPh₃로 환원하면 1차 amine.
- → [amine synthesis via azide and nitrile](../wiki/반응/아자이드·나이트릴을%20거친%20아민%20합성.md), [Staudinger reduction](../wiki/반응/스타우딩거%20환원.md)

#### 1-1b. cyanide 이온 alkylation 후 환원 (p.8)
- 탄소가 하나 늘어난 1차 amine RCH₂CH₂NH₂.
- → [amine synthesis via azide and nitrile](../wiki/반응/아자이드·나이트릴을%20거친%20아민%20합성.md)

#### 1-2. amide를 환원해 amine 만들기 (p.9)
- $\mathrm{LiAlH_4}\ \text{또는}\ \mathrm{BH_3}\text{로}\ \mathrm{C{=}O} \longrightarrow \mathrm{CH_2}$. "acylation 후 reduction"은 깔끔한 N-alkylation 우회로.
- → [amide reduction](../wiki/반응/아마이드%20환원.md)

#### 1-3. reductive amination (p.10–14)
- $\begin{aligned} & \text{carbonyl} + \text{amine} \\ & \longrightarrow \text{imine/iminium} \\ & \longrightarrow \text{hydride} \end{aligned}$. NaBH₃CN(pH 3–4)이 표준. 새 C–N의 탄소에는 H가 있어야 한다.
- p.13–14 연습은 [L5 연습 문제](../practice/L05_Exercises.md) 1, 2번.
- → [reductive amination](../wiki/반응/환원성%20아미노화.md), [imine](../wiki/개념/이민.md), [iminium ion](../wiki/개념/이미늄%20이온.md), [NaBH3CN](../wiki/시약/NaBH3CN.md)

#### 1-4. Eschweiler–Clarke methylation (p.15)
- $\mathrm{HCHO} + \mathrm{HCOOH}\text{로}\ \text{1차 amine} \longrightarrow \text{N,N-dimethyl}$. HCOO⁻가 hydride 공급원이고 3차에서 멈춘다.
- → [Eschweiler–Clarke reaction](../wiki/반응/에슈바일러-클라크%20반응.md)

#### 1-5. 응용: venlafaxine 합성 (p.16)
- $\begin{aligned} & \text{nitrile carbanion 첨가} \\ & \longrightarrow \text{nitrile hydrogenation} \\ & \longrightarrow \text{Eschweiler–Clarke} \end{aligned}$. 특허 경로는 H₂/Pd-C/HCHO 한 번에 94%.
- → [amine synthesis (overview)](../wiki/개념/아민%20합성%20개관.md), [Eschweiler–Clarke reaction](../wiki/반응/에슈바일러-클라크%20반응.md)

### 2. metal hydride에 의한 환원 (슬라이드 p.17–29)

#### 2-0. 개요: 어떤 시약이 무엇을 환원하나 (p.17–18)
- 시약 세기 LiAlH₄ > LiBH₄ > NaBH₄ > NaBH₃CN, carbonyl 반응성 aldehyde > ketone > ester > amide > carboxylate. BH₃와 DIBAL은 특수 시약.
- → [metal hydride의 반응성](../wiki/개념/금속%20수소화물의%20반응성.md)

#### 2-1. NaBH₄: 가장 흔한 온화한 환원제 (p.19–21)
- $\text{aldehyde·ketone} \longrightarrow \text{alcohol}$. BH₄⁻ 하나가 hydride 넷을 쓴다. MeOH보다 EtOH가 좋은 용매. aldehyde가 ketone보다 약 400배 빠르다.
- → [NaBH4](../wiki/시약/NaBH4.md), [metal hydride의 반응성](../wiki/개념/금속%20수소화물의%20반응성.md)

#### 2-2. LiBH₄: ester는 잡고 산은 놔두는 시약 (p.22)
- Li⁺ 덕분에 ester·lactone을 환원하고, carboxylic acid는 carboxylate가 되어 남는다.
- → [LiBH4](../wiki/시약/LiBH4.md)

#### 2-3. LiAlH₄: 거의 다 환원하는 강력한 시약 (p.23–26)
- $\begin{aligned} & \text{산·ester·aldehyde·ketone} \\ & \longrightarrow \text{alcohol},\ \text{amide} \\ & \longrightarrow \text{amine},\ \text{alkyl halide} \\ & \longrightarrow \text{alkane}(\mathrm{LiAlD_4}\text{로}\ \text{직접 치환 확인}) \end{aligned}$.
- p.25–26은 [L5 연습 문제](../practice/L05_Exercises.md) 5, 6번.
- → [LiAlH4](../wiki/시약/LiAlH4.md)

#### 2-4. Borane (BH₃): 서열을 거스르는 시약 (p.27–28)
- Lewis acid라 carboxylic acid·amide를 빠르게, ester·ketone은 느리게 환원한다. LiBH₄와 상보적.
- amide 환원 메커니즘: $\begin{aligned} & \mathrm{O} \\ & \longrightarrow \mathrm{B}\ \text{배위} \\ & \longrightarrow \text{tetrahedral intermediate} \\ & \longrightarrow \mathrm{O{-}BH_2}\ \text{이탈로 iminium} \\ & \longrightarrow \text{두 번째 hydride} \end{aligned}$.
- → [borane](../wiki/시약/보레인.md), [amide reduction](../wiki/반응/아마이드%20환원.md), [tetrahedral intermediate](../wiki/개념/사면체%20중간체.md)

#### 2-5. DIBAL-H: ester를 aldehyde에서 멈추기 (p.29)
- −70 °C에서 tetrahedral intermediate가 무너지지 않아 aldehyde에서 멈춘다.
- → [partial reduction of esters](../wiki/반응/에스터%20부분%20환원.md), [DIBAL-H](../wiki/시약/DIBAL-H.md)

### 3. catalytic hydrogenation (H₂/metal) (슬라이드 p.30–34)

#### 3-1. alkene의 hydrogenation (p.30–31)
- H₂/Pd-C 또는 PtO₂가 C=C를 환원하고 ketone은 남긴다. 표면에서 syn addition(cis 82 : trans 18). aromatic ring은 센 조건.
- → [catalytic hydrogenation](../wiki/반응/촉매%20수소화.md), [Pd/C](../wiki/시약/Pd-C.md), [PtO2](../wiki/시약/PtO2.md)

#### 3-1a. 응용: BASF (−)-menthol 공정 (p.32)
- Rh/Chiraphos asymmetric hydrogenation으로 geranial(E)과 neral(Z)이 같은 (+)-citronellal로 수렴한다.
- → [catalytic hydrogenation](../wiki/반응/촉매%20수소화.md)

#### 3-2. 다른 작용기의 hydrogenation (p.33)
- 쉬운 순서: RCOCl > ArNO₂ > alkyne > imine > alkene > benzyl 제거 > nitrile > benzene 고리.
- $\begin{aligned} & \text{Rosenmund}(\mathrm{H_2},\ \mathrm{Pd/BaSO_4},\ \text{quinoline})\text{로}\ \text{acid chloride} \\ & \longrightarrow \text{aldehyde},\ \text{imine hydrogenation은 reductive amination} \end{aligned}$.
- → [catalytic hydrogenation](../wiki/반응/촉매%20수소화.md), [Rosenmund reduction](../wiki/반응/로젠문트%20환원.md), [hydrogenolysis](../wiki/반응/수소화분해.md), [benzyl ether protecting group](../wiki/시약/벤질%20에터%20보호기.md), [reductive amination](../wiki/반응/환원성%20아미노화.md)

#### 요약 (p.34)
- (1) amine의 합성, (2) reductive amination, (3) metal hydride 환원(일반 시약과 특수 시약 Borane, DIBAL-H), (4) catalytic hydrogenation.

## 반응 요약표

| 반응 | 시약/조건 | 생성물 | 선택성·stereochemistry | 비고 |
|---|---|---|---|---|
| amine 직접 alkylation ([amine synthesis (overview)](../wiki/개념/아민%20합성%20개관.md)) | NH₃(대과량) + RX | RNH₂ (+ over-alkylation 생성물) | S<sub>N</sub>2 (inversion) | NH₃ 2 eq이면 1차/2차 혼합 (p.6) |
| [azide 경로](../wiki/반응/아자이드·나이트릴을%20거친%20아민%20합성.md) | 1) NaN₃, EtOH 2) LiAlH₄; H₂O (또는 H₂/Pd, PPh₃) | RNH₂ | S<sub>N</sub>2 (inversion) | 1차 amine만 (p.7) |
| [nitrile 경로](../wiki/반응/아자이드·나이트릴을%20거친%20아민%20합성.md) | 1) NaCN 2) LiAlH₄; H₂O (또는 H₂/Pd) | RCH₂CH₂NH₂ | S<sub>N</sub>2 (inversion) | 탄소 1개 증가 (p.8) |
| [amide reduction](../wiki/반응/아마이드%20환원.md) | LiAlH₄ 또는 BH₃; H₂O | RCH₂NR′₂ | $\mathrm{C{=}O} \longrightarrow \mathrm{CH_2}$ | 1·2·3차 amine 모두 (p.9) |
| [reductive amination](../wiki/반응/환원성%20아미노화.md) | amine + R₂C=O, NaBH₃CN (pH 3–4, EtOH) 또는 H₂/Ni, H₂/Pd-C | 한 단계 더 치환된 amine | carbonyl 탄소에 N | imine/iminium 경유 (p.10–12) |
| [Eschweiler–Clarke](../wiki/반응/에슈바일러-클라크%20반응.md) | HCHO, HCOOH | RN(CH₃)₂ | – | HCOOH = hydride원, quaternary salt 없음 (p.15) |
| [NaBH4](../wiki/시약/NaBH4.md) 환원 | NaBH₄, EtOH/MeOH | $\begin{aligned} & \text{aldehyde} \\ & \longrightarrow \text{1차},\ \text{ketone} \\ & \longrightarrow \text{2차 alcohol} \end{aligned}$ | aldehyde > ketone (약 400배) | diglyme에선 aldehyde만 (p.19–21) |
| [LiBH4](../wiki/시약/LiBH4.md) 환원 | LiBH₄, EtOH | $\text{ester/lactone} \longrightarrow \text{alcohol}$ | 산, amide, nitrile 유지 | (p.22) |
| [LiAlH4](../wiki/시약/LiAlH4.md) 환원 | 1) LiAlH₄, Et₂O/THF 2) H₂O/H₂SO₄ | $\text{alcohol};\ \text{amide} \longrightarrow \text{amine}$ | 거의 비선택적 | 물과 격렬 반응 (p.23) |
| alkyl halide 환원 ([LiAlH4](../wiki/시약/LiAlH4.md)) | LiAlH₄ (또는 LiAlD₄), ether | R–H (R–D) | 할로젠 자리 | D 표지로 위치 확인 (p.24) |
| [borane](../wiki/시약/보레인.md) 환원 | BH₃·THF/Et₂O/Me₂S | $\begin{aligned} & \text{산} \\ & \longrightarrow \text{1차 alcohol},\ \text{amide} \\ & \longrightarrow \text{amine} \end{aligned}$ | ester, ketone 유지 | LiBH₄와 상보적 (p.27–28) |
| [DIBAL-H](../wiki/반응/에스터%20부분%20환원.md) | DIBAL, hexane, −70 °C; H₃O⁺ | $\text{ester} \longrightarrow \text{aldehyde}$ | – | 저온에서 tetrahedral intermediate 안정 (p.29) |
| alkene [hydrogenation](../wiki/반응/촉매%20수소화.md) | H₂, Pd/C 또는 PtO₂ | alkane | syn addition (cis 우세) | ketone 유지 (p.30–31) |
| aromatic hydrogenation ([catalytic hydrogenation](../wiki/반응/촉매%20수소화.md)) | H₂, Ni (50 °C, 100 atm) 또는 PtO₂/AcOH | cyclohexane 고리 | – | 가장 어려운 hydrogenation (p.31) |
| asymmetric hydrogenation ([catalytic hydrogenation](../wiki/반응/촉매%20수소화.md)) | H₂, CO, Rh(CO)₂acac, Chiraphos | (+)-citronellal | conjugated C=C만; E는 (S,S), Z는 (R,R) | BASF menthol 공정 (p.32) |
| [Rosenmund](../wiki/반응/로젠문트%20환원.md) | H₂, Pd/BaSO₄, quinoline | RCHO | C–Cl만 | aldehyde, 방향족 유지 (p.33) |
| nitro 환원 ([catalytic hydrogenation](../wiki/반응/촉매%20수소화.md)) | H₂, Pt 또는 Pd, EtOH (+HOAc) | ArNH₂ | – | ~100% (p.33) |
| benzyl 제거 ([hydrogenolysis](../wiki/반응/수소화분해.md)) | H₂, Pd/C | ROH/RNH₂ + PhCH₃ | benzyl C–X 결합 | protecting group 제거 (p.33) |

## 연습 문제

→ [L5 연습 문제](../practice/L05_Exercises.md)

## 출처

- 슬라이드: L5 (PDF p.2–34)
