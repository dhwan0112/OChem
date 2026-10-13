# L5. 환원 반응 (Reduction reactions)

<!-- wiki-links:start -->

> **관련 위키 문서** ([위키 대문](../wiki/위키%20대문.md))
> - 반응: [SN2 반응](../wiki/반응/SN2%20반응.md), [로젠문트 환원](../wiki/반응/로젠문트%20환원.md), [수소화분해](../wiki/반응/수소화분해.md), [스타우딩거 환원](../wiki/반응/스타우딩거%20환원.md), [아마이드 환원](../wiki/반응/아마이드%20환원.md), [아자이드·나이트릴을 거친 아민 합성](../wiki/반응/아자이드·나이트릴을%20거친%20아민%20합성.md), [에슈바일러-클라크 반응](../wiki/반응/에슈바일러-클라크%20반응.md), [에스터 부분 환원](../wiki/반응/에스터%20부분%20환원.md), [촉매 수소화](../wiki/반응/촉매%20수소화.md), [환원성 아미노화](../wiki/반응/환원성%20아미노화.md)
> - 시약: [DIBAL-H](../wiki/시약/DIBAL-H.md), [LiAlH4](../wiki/시약/LiAlH4.md), [LiBH4](../wiki/시약/LiBH4.md), [NaBH3CN](../wiki/시약/NaBH3CN.md), [NaBH4](../wiki/시약/NaBH4.md), [Pd/C](../wiki/시약/Pd-C.md), [PtO2](../wiki/시약/PtO2.md), [벤질 에터 보호기](../wiki/시약/벤질%20에터%20보호기.md), [보레인](../wiki/시약/보레인.md), [피롤리딘](../wiki/시약/피롤리딘.md)
> - 개념: [금속 수소화물의 반응성](../wiki/개념/금속%20수소화물의%20반응성.md), [사면체 중간체](../wiki/개념/사면체%20중간체.md), [아민 합성 개관](../wiki/개념/아민%20합성%20개관.md), [이미늄 이온](../wiki/개념/이미늄%20이온.md), [이민](../wiki/개념/이민.md), [친전자체와 친핵체](../wiki/개념/친전자체와%20친핵체.md)

<!-- wiki-links:end -->

> 이 강의 노트는 **뼈대**다. 강의 순서와 슬라이드 위치만 정리했고, 설명은 링크된 개념 문서에 있다.

> 강의 흐름대로 길게 읽고 싶으면 **[통독본](통독/L05_Reduction.md)**(재구성 직전의 전체 노트, 소절마다 개념 문서 링크 포함)을 본다.
>
> CM3121 Advanced Organic Chemistry, Dr. Zhu Ye. 출처 표기의 p.는 PDF 페이지 번호다.

## 개요

이 강의는 "분자에 수소를 붙이는 법", 즉 reduction(환원)을 다룬다. 출발점은 amine이다. 몸과 약에서 중요한 분자 상당수가 질소를 품고 있는데 amine을 깔끔하게 만드는 일은 까다롭기 때문에, 강의는 아민 합성 문제를 실마리 삼아 azide·nitrile·amide·imine을 환원하는 방법으로 넘어간다. 거기서 NaBH₄, LiBH₄, LiAlH₄, BH₃, DIBAL-H라는 metal hydride 시약 세트를 정리하고, 마지막으로 H₂와 금속 촉매를 쓰는 catalytic hydrogenation으로 마무리한다. 핵심 질문은 "분자 안에 환원될 수 있는 자리가 여러 개일 때, 원하는 곳만 환원하려면 어떤 시약을 골라야 하나?"이다. L1의 hydroboration에서 만난 BH₃가 여기서는 카보닐 환원제로 다시 등장하고, 이후 L7(enolate), L10(enamine/iminium), L12(protecting group)에서도 이 강의의 시약들이 계속 쓰인다.

## 강의 흐름

### 1. 아민이란 무엇이고, 왜 만들기 어려운가 (슬라이드 p.2–16)

#### 1-0. 일상 속 질소 화합물 (p.2–3)
- 세로토닌·도파민 등 neurotransmitter와 비타민·약물 상당수가 질소 화합물이라 amine 합성은 기본기다.
- → [아민 합성 개관](../wiki/개념/아민%20합성%20개관.md)

#### 1-0-1. 아민의 분류와 성질 (p.4)
- 1·2·3차 amine과 4차 암모늄염. N의 lone pair 때문에 base·nucleophile이지만 amide는 염기성·친핵성이 약하다. 고리형 amine 이름(azepane~aziridine).
- → [아민 합성 개관](../wiki/개념/아민%20합성%20개관.md), [피롤리딘](../wiki/시약/피롤리딘.md)

#### 1-1. S<sub>N</sub>2로 아민 만들기: 왜 생각대로 안 되나 (p.5–6)
- NH₃ + RX는 생성 amine이 더 좋은 nucleophile이라 over-alkylation이 일어난다(NH₃ 2 eq에서 1차 45%, 2차 43%).
- → [아민 합성 개관](../wiki/개념/아민%20합성%20개관.md), [SN2 반응](../wiki/반응/SN2%20반응.md)

#### 1-1a. 아자이드 이온 알킬화 후 환원 (p.7)
- R–N₃는 더 이상 nucleophile이 아니라 한 번에서 멈추고, LiAlH₄·H₂/Pd·PPh₃로 환원하면 1차 amine.
- → [아자이드·나이트릴을 거친 아민 합성](../wiki/반응/아자이드·나이트릴을%20거친%20아민%20합성.md), [스타우딩거 환원](../wiki/반응/스타우딩거%20환원.md)

#### 1-1b. 시아나이드 이온 알킬화 후 환원 (p.8)
- 탄소가 하나 늘어난 1차 amine RCH₂CH₂NH₂.
- → [아자이드·나이트릴을 거친 아민 합성](../wiki/반응/아자이드·나이트릴을%20거친%20아민%20합성.md)

#### 1-2. 아마이드를 환원해 아민 만들기 (p.9)
- LiAlH₄ 또는 BH₃로 C=O → CH₂. "acylation 후 reduction"은 깔끔한 N-alkylation 우회로.
- → [아마이드 환원](../wiki/반응/아마이드%20환원.md)

#### 1-3. 환원성 아미노화 (p.10–14)
- 카보닐 + amine → imine/iminium → hydride. NaBH₃CN(pH 3–4)이 표준. 새 C–N의 탄소에는 H가 있어야 한다.
- p.13–14 연습은 [L5 연습 문제](../practice/L05_Exercises.md) 1, 2번.
- → [환원성 아미노화](../wiki/반응/환원성%20아미노화.md), [이민](../wiki/개념/이민.md), [이미늄 이온](../wiki/개념/이미늄%20이온.md), [NaBH3CN](../wiki/시약/NaBH3CN.md)

#### 1-4. Eschweiler–Clarke 메틸화 (p.15)
- HCHO + HCOOH로 1차 amine → N,N-다이메틸. HCOO⁻가 hydride 공급원이고 3차에서 멈춘다.
- → [에슈바일러-클라크 반응](../wiki/반응/에슈바일러-클라크%20반응.md)

#### 1-5. 응용: 벤라팍신(Venlafaxine) 합성 (p.16)
- nitrile carbanion 첨가 → nitrile 수소화 → Eschweiler–Clarke. 특허 경로는 H₂/Pd-C/HCHO 한 번에 94%.
- → [아민 합성 개관](../wiki/개념/아민%20합성%20개관.md), [에슈바일러-클라크 반응](../wiki/반응/에슈바일러-클라크%20반응.md)

### 2. 금속 수소화물에 의한 환원 (슬라이드 p.17–29)

#### 2-0. 개요: 어떤 시약이 무엇을 환원하나 (p.17–18)
- 시약 세기 LiAlH₄ > LiBH₄ > NaBH₄ > NaBH₃CN, 카보닐 반응성 aldehyde > ketone > ester > amide > carboxylate. BH₃와 DIBAL은 특수 시약.
- → [금속 수소화물의 반응성](../wiki/개념/금속%20수소화물의%20반응성.md)

#### 2-1. NaBH₄: 가장 흔한 온화한 환원제 (p.19–21)
- aldehyde·ketone → alcohol. BH₄⁻ 하나가 hydride 넷을 쓴다. MeOH보다 EtOH가 좋은 용매. aldehyde가 ketone보다 약 400배 빠르다.
- → [NaBH4](../wiki/시약/NaBH4.md), [금속 수소화물의 반응성](../wiki/개념/금속%20수소화물의%20반응성.md)

#### 2-2. LiBH₄: 에스터는 잡고 산은 놔두는 시약 (p.22)
- Li⁺ 덕분에 ester·lactone을 환원하고, 카복실산은 carboxylate가 되어 남는다.
- → [LiBH4](../wiki/시약/LiBH4.md)

#### 2-3. LiAlH₄: 거의 다 환원하는 강력한 시약 (p.23–26)
- 산·ester·aldehyde·ketone → alcohol, amide → amine, alkyl halide → alkane(LiAlD₄로 직접 치환 확인).
- p.25–26은 [L5 연습 문제](../practice/L05_Exercises.md) 5, 6번.
- → [LiAlH4](../wiki/시약/LiAlH4.md)

#### 2-4. Borane (BH₃): 서열을 거스르는 시약 (p.27–28)
- Lewis acid라 카복실산·amide를 빠르게, ester·ketone은 느리게 환원한다. LiBH₄와 상보적.
- amide 환원 메커니즘: O→B 배위 → tetrahedral intermediate → O–BH₂ 이탈로 iminium → 두 번째 hydride.
- → [보레인](../wiki/시약/보레인.md), [아마이드 환원](../wiki/반응/아마이드%20환원.md), [사면체 중간체](../wiki/개념/사면체%20중간체.md)

#### 2-5. DIBAL-H: 에스터를 알데하이드에서 멈추기 (p.29)
- −70 °C에서 tetrahedral intermediate가 무너지지 않아 aldehyde에서 멈춘다.
- → [에스터 부분 환원](../wiki/반응/에스터%20부분%20환원.md), [DIBAL-H](../wiki/시약/DIBAL-H.md)

### 3. 촉매 수소화 (Catalytic hydrogenation, H₂/Metal) (슬라이드 p.30–34)

#### 3-1. 알켄의 수소화 (p.30–31)
- H₂/Pd-C 또는 PtO₂가 C=C를 환원하고 ketone은 남긴다. 표면에서 syn 첨가(cis 82 : trans 18). 방향족 고리는 센 조건.
- → [촉매 수소화](../wiki/반응/촉매%20수소화.md), [Pd/C](../wiki/시약/Pd-C.md), [PtO2](../wiki/시약/PtO2.md)

#### 3-1a. 응용: BASF (−)-멘톨 공정 (p.32)
- Rh/Chiraphos asymmetric hydrogenation으로 geranial(E)과 neral(Z)이 같은 (+)-citronellal로 수렴한다.
- → [촉매 수소화](../wiki/반응/촉매%20수소화.md)

#### 3-2. 다른 작용기의 수소화 (p.33)
- 쉬운 순서: RCOCl > ArNO₂ > alkyne > imine > alkene > benzyl 제거 > nitrile > 벤젠 고리.
- Rosenmund(H₂, Pd/BaSO₄, quinoline)로 산 염화물 → aldehyde, imine 수소화는 reductive amination.
- → [촉매 수소화](../wiki/반응/촉매%20수소화.md), [로젠문트 환원](../wiki/반응/로젠문트%20환원.md), [수소화분해](../wiki/반응/수소화분해.md), [벤질 에터 보호기](../wiki/시약/벤질%20에터%20보호기.md), [환원성 아미노화](../wiki/반응/환원성%20아미노화.md)

#### 요약 (p.34)
- (1) 아민의 합성, (2) 환원성 아미노화, (3) 금속 수소화물 환원(일반 시약과 특수 시약 Borane, DIBAL-H), (4) 촉매 수소화.

## 반응 요약표

| 반응 | 시약/조건 | 생성물 | 선택성·입체화학 | 비고 |
|---|---|---|---|---|
| 아민 직접 알킬화 ([아민 합성 개관](../wiki/개념/아민%20합성%20개관.md)) | NH₃(대과량) + RX | RNH₂ (+ 과알킬화 생성물) | S<sub>N</sub>2 (반전) | NH₃ 2 eq이면 1차/2차 혼합 (p.6) |
| [아자이드 경로](../wiki/반응/아자이드·나이트릴을%20거친%20아민%20합성.md) | 1) NaN₃, EtOH 2) LiAlH₄; H₂O (또는 H₂/Pd, PPh₃) | RNH₂ | S<sub>N</sub>2 (반전) | 1차 아민만 (p.7) |
| [나이트릴 경로](../wiki/반응/아자이드·나이트릴을%20거친%20아민%20합성.md) | 1) NaCN 2) LiAlH₄; H₂O (또는 H₂/Pd) | RCH₂CH₂NH₂ | S<sub>N</sub>2 (반전) | 탄소 1개 증가 (p.8) |
| [아마이드 환원](../wiki/반응/아마이드%20환원.md) | LiAlH₄ 또는 BH₃; H₂O | RCH₂NR′₂ | C=O → CH₂ | 1·2·3차 아민 모두 (p.9) |
| [환원성 아미노화](../wiki/반응/환원성%20아미노화.md) | 아민 + R₂C=O, NaBH₃CN (pH 3–4, EtOH) 또는 H₂/Ni, H₂/Pd-C | 한 단계 더 치환된 아민 | 카보닐 탄소에 N | imine/iminium 경유 (p.10–12) |
| [Eschweiler–Clarke](../wiki/반응/에슈바일러-클라크%20반응.md) | HCHO, HCOOH | RN(CH₃)₂ | – | HCOOH = hydride원, 4차 염 없음 (p.15) |
| [NaBH4](../wiki/시약/NaBH4.md) 환원 | NaBH₄, EtOH/MeOH | 알데하이드 → 1차, 케톤 → 2차 알코올 | aldehyde > ketone (약 400배) | diglyme에선 알데하이드만 (p.19–21) |
| [LiBH4](../wiki/시약/LiBH4.md) 환원 | LiBH₄, EtOH | 에스터/락톤 → 알코올 | 산, 아마이드, 나이트릴 유지 | (p.22) |
| [LiAlH4](../wiki/시약/LiAlH4.md) 환원 | 1) LiAlH₄, Et₂O/THF 2) H₂O/H₂SO₄ | 알코올; 아마이드 → 아민 | 거의 비선택적 | 물과 격렬 반응 (p.23) |
| 할로젠화 알킬 환원 ([LiAlH4](../wiki/시약/LiAlH4.md)) | LiAlH₄ (또는 LiAlD₄), ether | R–H (R–D) | 할로젠 자리 | D 표지로 위치 확인 (p.24) |
| [보레인](../wiki/시약/보레인.md) 환원 | BH₃·THF/Et₂O/Me₂S | 산 → 1차 알코올, 아마이드 → 아민 | 에스터, 케톤 유지 | LiBH₄와 상보적 (p.27–28) |
| [DIBAL-H](../wiki/반응/에스터%20부분%20환원.md) | DIBAL, hexane, −70 °C; H₃O⁺ | 에스터 → 알데하이드 | – | 저온에서 사면체 중간체 안정 (p.29) |
| 알켄 [수소화](../wiki/반응/촉매%20수소화.md) | H₂, Pd/C 또는 PtO₂ | 알케인 | syn 첨가 (cis 우세) | 케톤 유지 (p.30–31) |
| 방향족 수소화 ([촉매 수소화](../wiki/반응/촉매%20수소화.md)) | H₂, Ni (50 °C, 100 atm) 또는 PtO₂/AcOH | 사이클로헥세인 고리 | – | 가장 어려운 수소화 (p.31) |
| 비대칭 수소화 ([촉매 수소화](../wiki/반응/촉매%20수소화.md)) | H₂, CO, Rh(CO)₂acac, Chiraphos | (+)-시트로넬랄 | 공액 C=C만; E는 (S,S), Z는 (R,R) | BASF 멘톨 공정 (p.32) |
| [Rosenmund](../wiki/반응/로젠문트%20환원.md) | H₂, Pd/BaSO₄, quinoline | RCHO | C–Cl만 | 알데하이드, 방향족 유지 (p.33) |
| 나이트로 환원 ([촉매 수소화](../wiki/반응/촉매%20수소화.md)) | H₂, Pt 또는 Pd, EtOH (+HOAc) | ArNH₂ | – | ~100% (p.33) |
| 벤질 제거 ([수소화분해](../wiki/반응/수소화분해.md)) | H₂, Pd/C | ROH/RNH₂ + PhCH₃ | 벤질 C–X 결합 | 보호기 제거 (p.33) |

## 연습 문제

→ [L5 연습 문제](../practice/L05_Exercises.md)

## 출처

- 슬라이드: L5 (PDF p.2–34)
