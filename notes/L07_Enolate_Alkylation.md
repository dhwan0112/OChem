# L7. 엔올레이트와 α-알킬화 반응 (Enolates and α-alkylation reactions)

<!-- wiki-links:start -->

> **관련 위키 문서** ([위키 대문](../wiki/위키%20대문.md))
> - 반응: [acetoacetic ester synthesis](../wiki/반응/아세토아세트산%20에스터%20합성.md), [decarboxylation](../wiki/반응/탈카복실화.md), [enolate alkylation](../wiki/반응/엔올레이트%20알킬화.md), [ester hydrolysis](../wiki/반응/에스터%20가수분해.md), [Horner–Wadsworth–Emmons reaction](../wiki/반응/HWE%20반응.md), [keto-enol tautomerism](../wiki/반응/케토-엔올%20토토머화.md), [malonic ester synthesis](../wiki/반응/말론산%20에스터%20합성.md), [SN2 reaction](../wiki/반응/SN2%20반응.md)
> - 시약: [alkoxide base](../wiki/시약/알콕사이드%20염기.md), [Evans oxazolidinone](../wiki/시약/에반스%20옥사졸리디논.md), [LDA](../wiki/시약/LDA.md), [LiBH4](../wiki/시약/LiBH4.md), [phosphorus ylide](../wiki/시약/인%20일라이드.md)
> - 개념: [alpha-hydrogen acidity](../wiki/개념/α-수소의%20산도.md), [chiral auxiliary](../wiki/개념/키랄%20보조기.md), [electrophile and nucleophile](../wiki/개념/친전자체와%20친핵체.md), [enol and enolate](../wiki/개념/엔올과%20엔올레이트.md), [enolate chemistry (overview)](../wiki/개념/엔올레이트%20화학%20개관.md), [hard and soft acids and bases (HSAB)](../wiki/개념/하드-소프트%20산염기.md), [imine](../wiki/개념/이민.md), [ketene](../wiki/개념/케텐.md), [kinetic vs thermodynamic control](../wiki/개념/속도론적%20지배와%20열역학적%20지배.md), [kinetic vs thermodynamic enolate](../wiki/개념/속도론적%20엔올레이트와%20열역학적%20엔올레이트.md)

<!-- wiki-links:end -->

> 이 강의 노트는 **뼈대**다. 강의 순서와 슬라이드 위치만 정리했고, 설명은 링크된 개념 문서에 있다.

> 강의 흐름대로 길게 읽고 싶으면 **[통독본](통독/L07_Enolate_Alkylation.md)**(재구성 직전의 전체 노트, 소절마다 개념 문서 링크 포함)을 본다.

> CM3121 Advanced Organic Chemistry, Dr. Zhu Ye. 참고 교재: Clayden 2판 25장, McMurry 10판 22장.
> 출처 표기의 p.는 PDF 페이지 번호다. 슬라이드 우측 하단에 인쇄된 번호는 PDF 페이지 번호보다 1 크다(예: PDF p.10 = 슬라이드 번호 11).

## 개요

carbonyl 옆 α-탄소의 수소를 염기로 떼어 내면 carbonyl 화합물이 electrophile에서 nucleophile(enolate)로 뒤집힌다. 이 강의는 그 enolate를 alkyl halide과 SN2로 반응시켜 C–C 결합을 만드는 α-alkylation을 다룬다. 먼저 α-H가 얼마나 산성인지와 어떤 염기로 어느 쪽 enolate를 kinetic vs thermodynamic를 정하고, 그다음 alkylation의 실제와 1,3-dicarbonyl을 쓰는 고전적 합성법(acetoacetic ester·malonic ester synthesis)으로 넘어간다. 이어 carbonyl 밖의 enolate류, enolate가 C와 O 중 어디로 반응하는지, 마지막으로 chiral auxiliary를 쓴 asymmetric alkylation으로 끝난다. 전체 지도는 [enolate chemistry (overview)](../wiki/개념/엔올레이트%20화학%20개관.md)에 있다.

## 강의 흐름

### 0. 복습: 안정화 ylide는 왜 약염기로도 만들어지나? (p.3)
- 음전하가 C=O로 퍼져 enolate와 같은 공명 구조를 가지므로 C–H가 산성이다. HWE phosphonate anion도 같다.
- → [이미 만나 본 enolate](../wiki/개념/엔올과%20엔올레이트.md), [phosphorus ylide](../wiki/시약/인%20일라이드.md), [Horner–Wadsworth–Emmons reaction](../wiki/반응/HWE%20반응.md)

### I. enolate 형성

#### 1.1 α-수소는 얼마나 산성인가? (p.4)
- aldehyde/ketone α-H pKa 약 19–20. α-H만 산성이고 β, γ, δ-H는 아니다. pKa 표.
- → [alpha-hydrogen acidity](../wiki/개념/α-수소의%20산도.md)

#### 1.2 그럼 아무 염기나 써도 되나? (p.5–6)
- NaOEt는 ketone enolate를 소량만(EtOH 16 < ketone 19), LDA는 사실상 전부 만든다.
- → [pKa로 평형 판단](../wiki/개념/α-수소의%20산도.md), [enolate의 구조와 그림](../wiki/개념/엔올과%20엔올레이트.md), [염기 고르기 두 전략](../wiki/반응/엔올레이트%20알킬화.md)

#### 1.3 LDA는 왜 "강하지만 친핵성이 없는" 염기인가? (p.6–7)
- n-BuLi + HN(i-Pr)₂로 만든다. 부피 큰 isopropyl group이 질소를 가려 carbonyl을 공격하지 못한다. LiTMP, LHMDS도 같은 부류.
- → [LDA](../wiki/시약/LDA.md)

#### 1.4 α-탄소가 두 개라면 어느 쪽이 먼저 떨어지나? (p.8)
- kinetic enolate = 빨리 생기는 쪽(덜 치환), thermodynamic enolate = 더 안정한 쪽(더 치환). 2-헵타논 100 : 0, 2-methoxycyclohexanone 85 : 15.
- → [kinetic vs thermodynamic enolate](../wiki/개념/속도론적%20엔올레이트와%20열역학적%20엔올레이트.md)

#### 1.5 에너지 도표로 보면? (p.11–12)
- 2-methylcyclohexanone: C6–H는 TS가 kinetic, C2–H는 생성물이 thermodynamic. LDA/−78 °C는 kinetic.
- → [kinetic vs thermodynamic enolate](../wiki/개념/속도론적%20엔올레이트와%20열역학적%20엔올레이트.md), [kinetic vs thermodynamic control](../wiki/개념/속도론적%20지배와%20열역학적%20지배.md)

### II. α-alkylation 반응

#### 2.1 enolate는 alkyl halide과 어떻게 반응하나? (p.9–10)
- enolate α-탄소가 R–X를 SN2로 공격한다. methyl·1차·allyl·benzyl 좋음, 2차 불량, 3차는 제거.
- → [enolate alkylation](../wiki/반응/엔올레이트%20알킬화.md), [SN2 reaction](../wiki/반응/SN2%20반응.md)

#### 2.2 실제 ketone alkylation는 어떻게 되나? (p.10–12)
- 2-methylcyclohexanone + LDA; CH₃I → 2,6-이치환체 56%(2,2-이치환체 6%). polyalkylation 주의.
- → [enolate alkylation](../wiki/반응/엔올레이트%20알킬화.md)

#### 2.3 ester와 락톤도 될까? (p.13–14)
- butanoic acid methyl + LDA; EtI → 96%. γ-뷰티로락톤 + LDA; MeI → 88%.
- → [enolate alkylation](../wiki/반응/엔올레이트%20알킬화.md)

### III. 1,3-dicarbonyl 화합물

#### 3.0 두 carbonyl 사이의 수소는 왜 훨씬 산성인가? (p.15)
- 음전하가 두 C=O로 퍼져 pKa 9–13. alkoxide로 충분하다. ethyl acetoacetate와 diethyl malonate.
- → [alpha-hydrogen acidity](../wiki/개념/α-수소의%20산도.md), [alkoxide base](../wiki/시약/알콕사이드%20염기.md)

#### 3.1 acetoacetic ester 합성: methyl ketone을 어떻게 만드나? (p.16–17)
- NaOEt; R–X → 가수분해 → β-keto산 가열(6원자 고리형 TS, −CO₂) → methyl ketone. R–X에 –CH₂COCH₃를 붙인 효과.
- → [acetoacetic ester synthesis](../wiki/반응/아세토아세트산%20에스터%20합성.md), [decarboxylation](../wiki/반응/탈카복실화.md), [ester hydrolysis](../wiki/반응/에스터%20가수분해.md)

#### 3.2 거꾸로 생각하기: 2-펜타논의 역합성 (p.18)
- C=O 옆 CH₂와 R 사이를 끊는다. R = ethyl → EtBr.
- → [acetoacetic ester synthesis](../wiki/반응/아세토아세트산%20에스터%20합성.md)

#### 3.3 malonic ester 합성: carboxylic acid은? (p.19–20)
- NaOEt; R–X → KOH → H₂SO₄ 환류(−CO₂) → RCH₂COOH. R–X에 –CH₂COOH를 붙인 효과.
- → [malonic ester synthesis](../wiki/반응/말론산%20에스터%20합성.md), [decarboxylation](../wiki/반응/탈카복실화.md)

### IV. 여러 작용기의 enolate

#### 4.1 ketone·aldehyde·ester: 누가 enol화될 수 있나? (p.21)
- α-H가 있으면 된다. 벤조페논, benzaldehyde, pivaldehyde, formaldehyde는 non-enolizable.
- → [enol and enolate](../wiki/개념/엔올과%20엔올레이트.md)

#### 4.2 carbonyl이 아니어도 enolate 같은 것이 생기나? (p.22)
- nitrile, imine(aza-enolate), nitro 화합물. π 결합 하나를 가진 전자 끄는 기 + sp³ C–H.
- → [enol and enolate](../wiki/개념/엔올과%20엔올레이트.md), [imine](../wiki/개념/이민.md), [Henry reaction](../wiki/반응/헨리%20반응.md)

#### 4.3 그런데 왜 acid chloride, carboxylic acid, amide는 안 되나? (p.23)
- acid chloride enolate는 Cl⁻를 잃고 ketene이 된다. carboxylic acid·N–H amide는 O–H/N–H가 먼저 떨어진다.
- → [alpha-hydrogen acidity](../wiki/개념/α-수소의%20산도.md), [ketene](../wiki/개념/케텐.md)

### V. enolate 반응성: C 대 O

#### 5.1 음전하는 O에 많은데 왜 보통 C에서 반응하나? (p.24)
- 전하는 O에, HOMO 계수는 C에 크다. 오비탈 지배 반응은 C, 전하 지배 반응은 O.
- → [hard and soft acids and bases (HSAB)](../wiki/개념/하드-소프트%20산염기.md), [enol and enolate](../wiki/개념/엔올과%20엔올레이트.md)

#### 5.2 무엇이 C냐 O냐를 가르나? (p.25)
- soft(MeI) → C, hard(Me₂SO₄, MeOMs, Me₃O⁺) → O. 큰 cation(Cs > K > Na > Li)은 O 쪽.
- → [hard and soft acids and bases (HSAB)](../wiki/개념/하드-소프트%20산염기.md)

### VI. 비대칭 alkylation 반응

#### 6.1 보통의 alkylation는 왜 라세미체를 주나? (p.26)
- 평면 enolate의 두 면은 동등하다. chiral auxiliary가 한 면을 가리면 diastereomer 비가 치우친다.
- → [chiral auxiliary](../wiki/개념/키랄%20보조기.md)

#### 6.2 Evans oxazolidinone: 어떻게 한쪽 면만 열어 두나? (p.27)
- Li chelate로 Z-enolate 고정, C4 isopropyl이 한 면을 막아 BnBr이 반대 면으로. 92%, 99 : 1 dr.
- → [Evans oxazolidinone](../wiki/시약/에반스%20옥사졸리디논.md)

#### 6.3 보조기는 어떻게 떼어 내나? (p.28)
- LiBH₄ → 키랄 1차 alcohol, LiOH/H₂O₂ → 키랄 carboxylic acid. α-입체 중심 유지.
- → [Evans oxazolidinone](../wiki/시약/에반스%20옥사졸리디논.md), [LiBH4](../wiki/시약/LiBH4.md)

### 정리 (p.29)
- 강염기로 α-enolate, 부피 큰 염기로 kinetic enolate, SN2로 alkylation. acetoacetate → –CH₂COCH₃, malonate → –CH₂COOH. carbonyl 밖에서도 enolate류가 생긴다.
- → [enolate chemistry (overview)](../wiki/개념/엔올레이트%20화학%20개관.md)

## 반응 요약표

| 반응 | 시약/조건 | 생성물 | 선택성 | 비고 |
|---|---|---|---|---|
| [LDA](../wiki/시약/LDA.md) 제조 | n-BuLi + HN(i-Pr)₂, THF | LiN(i-Pr)₂ + 뷰테인 | – | 비가역 (p.6) |
| enolate 형성 (정량) | LDA, THF, −78 °C | lithium enolate | 덜 치환된 α-C (kinetic) | (p.5–8) |
| enolate 형성 (소량, 평형) | NaOEt, EtOH | 소듐 enolate 소량 | – | [alpha-hydrogen acidity](../wiki/개념/α-수소의%20산도.md) (p.5) |
| [kinetic vs thermodynamic](../wiki/개념/속도론적%20엔올레이트와%20열역학적%20엔올레이트.md) | LDA, −78 °C | 2-methylcyclohexanone → C1=C6 enolate | 덜 가려진 C6 | (p.11–12) |
| ketone [α-alkylation](../wiki/반응/엔올레이트%20알킬화.md) | 1. LDA 2. CH₃I (또는 BnBr) | 2,6-dimethylcyclohexanone 56% | 덜 치환된 α-C, 라세미 | SN2 규칙 (p.10–11) |
| ester α-alkylation | 1. LDA, THF 2. EtI | 2-ethylbutanoic acid methyl 96% | α-C | (p.13) |
| 락톤 α-alkylation | 1. LDA 2. MeI | α-methyl-γ-뷰티로락톤 88% | α-C | (p.14) |
| [acetoacetic ester synthesis](../wiki/반응/아세토아세트산%20에스터%20합성.md) | 1. NaOEt 2. R–X 3. aq. NaOH 4. H₃O⁺, 가열 | CH₃COCH₂R | 두 C=O 사이 CH₂ | (p.16–18) |
| [malonic ester synthesis](../wiki/반응/말론산%20에스터%20합성.md) | 1. NaOEt 2. R–X 3. KOH 환류 4. H₂SO₄ 환류 | RCH₂COOH | 두 C=O 사이 CH₂ | (p.19–20) |
| β-keto산 [decarboxylation](../wiki/반응/탈카복실화.md) | 가열 | enol → ketone + CO₂ | – | 6원자 고리형 TS (p.16) |
| acid chloride + Et₃N | Cl₂CHCOCl, Et₃N | 다이클로로[ketene](../wiki/개념/케텐.md) | – | (p.23) |
| [C- vs O-alkylation](../wiki/개념/하드-소프트%20산염기.md) | soft: MeI / hard: MeOMs, Me₂SO₄, Me₃O⁺ | ketone (C) / enol ether (O) | C 또는 O | (p.24–25) |
| [Evans asymmetric alkylation](../wiki/시약/에반스%20옥사졸리디논.md) | N-acyl oxazolidinone, LDA, −78 °C; BnBr | α-benzyl 생성물 92% | 99 : 1 dr | (p.27) |
| 보조기 제거 | LiBH₄ / LiOH, H₂O₂ | 키랄 1차 alcohol / 키랄 carboxylic acid | α-입체중심 유지 | (p.28) |

## 연습 문제

→ [L7 연습 문제와 해설](../practice/L07_Exercises.md)

## 출처

- 슬라이드: L7 (PDF p.1–29)
