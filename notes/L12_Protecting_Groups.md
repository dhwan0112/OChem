# L12. 보호기 (Protecting Groups)

<!-- wiki-links:start -->

> **관련 위키 문서** ([위키 대문](../wiki/위키%20대문.md))
> - 반응: [SN2 반응](../wiki/반응/SN2%20반응.md), [수소화분해](../wiki/반응/수소화분해.md), [아세탈 형성](../wiki/반응/아세탈%20형성.md), [에스터 가수분해](../wiki/반응/에스터%20가수분해.md), [친핵성 아실 치환](../wiki/반응/친핵성%20아실%20치환.md), [펩타이드 합성](../wiki/반응/펩타이드%20합성.md)
> - 시약: [Boc 보호기](../wiki/시약/Boc%20보호기.md), [Cbz 보호기](../wiki/시약/Cbz%20보호기.md), [DCC](../wiki/시약/DCC.md), [Fmoc 보호기](../wiki/시약/Fmoc%20보호기.md), [Pd/C](../wiki/시약/Pd-C.md), [TFA](../wiki/시약/TFA.md), [THP 보호기](../wiki/시약/THP%20보호기.md), [그리냐르 시약](../wiki/시약/그리냐르%20시약.md), [벤질 에터 보호기](../wiki/시약/벤질%20에터%20보호기.md), [실릴 에터 보호기](../wiki/시약/실릴%20에터%20보호기.md)
> - 개념: [E1cB 제거](../wiki/개념/E1cB%20제거.md), [α-수소의 산도](../wiki/개념/α-수소의%20산도.md), [보호기](../wiki/개념/보호기.md), [사면체 중간체](../wiki/개념/사면체%20중간체.md), [직교 보호](../wiki/개념/직교%20보호.md), [탄소 양이온](../wiki/개념/탄소%20양이온.md)

<!-- wiki-links:end -->

> 이 강의 노트는 **뼈대**다. 강의 순서와 슬라이드 위치만 정리했고, 설명은 링크된 개념 문서에 있다.

CM3121 Advanced Organic Chemistry, Dr. Zhu Ye. 참고 교재: Clayden 2판 23장 (Protecting groups).

## 개요

실제 합성 표적에는 반응할 자리가 여럿이라, 원하는 곳만 반응시키려면 방해되는 작용기를 잠시 가려야 한다. 이 강의는 palytoxin이라는 극단적인 예로 protecting group이 왜 필요한지 보여 준 뒤, 언제 쓰는지(덜 반응적인 작용기를 반응시킬 때, 공존할 수 없는 작용기가 있을 때)와 쓰는 법(보호 → 반응 → 탈보호)을 정리한다. 이어 알코올의 silyl ether, 아민의 carbamate(Boc, Cbz, Fmoc), 알데하이드·케톤의 acetal을 차례로 다루며 각 보호기가 왜 그 조건에서만 벗겨지는지를 메커니즘으로 설명한다. carbamate 다음에는 Boc와 Fmoc가 직교하게 쓰이는 펩타이드 합성(SPPS 포함)을 보고, 마지막에 acetal로 앞에서 막혔던 두 Grignard 문제를 푼다.

## 강의 흐름

### 1. 표적 분자: 왜 이런 게 필요할까 (슬라이드 p.2)
- palytoxin: OH 40개, 키랄 중심 64개. 거의 같은 OH 중 하나만 반응시키려면 나머지를 막아야 한다.
- → [protecting group](../wiki/개념/보호기.md)의 "개요"

### 2. 언제 보호기를 쓰는가 (슬라이드 p.3)
- (1) 덜 반응적인 에스터만 반응시킬 때(ethyl acetoacetate + PhMgBr은 케톤을 침, 52%), (2) 공존할 수 없는 작용기가 있을 때("impossible Grignard reagent", 산성 H).
- → [보호기](../wiki/개념/보호기.md)의 "언제 쓰나", [그리냐르 시약](../wiki/시약/그리냐르%20시약.md)

### 3. 보호기는 어떻게 쓰는가 (슬라이드 p.4)
- FG1 보호 → FG2에서 반응 → FG1 탈보호. 조건: 깔끔한 보호·탈보호, 반응 조건에서의 안정성. 강의의 주인공은 silyl ether, carbamate, acetal.
- → [보호기](../wiki/개념/보호기.md)의 "원리"

### 4. 한눈에 보는 보호기 표 (슬라이드 p.5)
- Clayden 23장 표: acetal, trialkylsilyl, THP, benzyl ether, methyl ether, t-Bu ester, Cbz, Boc, Fmoc의 보호 대상·"무엇으로부터"·도입·제거.
- → [보호기](../wiki/개념/보호기.md)의 표, [THP 보호기](../wiki/시약/THP%20보호기.md), [벤질 에터 보호기](../wiki/시약/벤질%20에터%20보호기.md)

### 5. 알코올의 보호기: silyl ether (슬라이드 p.5–7)
- 5-1 종류(TMS, TES, TBS/TBDMS, TIPS, TBDPS), 5-2 도입(R₃SiCl, imidazole), 5-3 acetylide alkylation 예(OH를 먼저 TBDMS로), 5-4 제거(TBAF 또는 H⁺/H₂O, Si–F가 강함), 5-5 상대 안정성(산: TBDPS 최강, 염기: TIPS 최강).
- → [실릴 에터 보호기](../wiki/시약/실릴%20에터%20보호기.md), [SN2 반응](../wiki/반응/SN2%20반응.md)

### 6. 아민의 보호기: carbamate (슬라이드 p.8)
- 6-1 질소 전자쌍이 C=O로 비편재화되어 nucleophile·염기 성질이 약해진다. 6-2 chloroformate(Cbz) 또는 dicarbonate(Boc₂O)와 염기로 씌운다. 6-3 Boc는 산(TFA), Cbz는 H₂/Pd(또는 HBr/AcOH)로 벗긴다. 마지막은 carbamic acid → CO₂ + 아민.
- → [보호기](../wiki/개념/보호기.md)의 "왜 carbamate인가", [Cbz 보호기](../wiki/시약/Cbz%20보호기.md), [Boc 보호기](../wiki/시약/Boc%20보호기.md), [수소화분해](../wiki/반응/수소화분해.md)

### 7. 펩타이드 합성: 보호기의 실전 무대 (슬라이드 p.9–12)

#### 7-1. 무엇이 문제인가 (슬라이드 p.9)
- Leu와 Gly 모두 NH₂와 CO₂H를 가져 보호 없이는 Leu–Leu, Gly–Gly, Gly–Leu가 섞인다.
- → [펩타이드 합성](../wiki/반응/펩타이드%20합성.md)

#### 7-2. 해결 전략 (슬라이드 p.9)
- Leu는 N-보호(PG1) + C(=O)X 활성화, Gly는 C-보호(PG2). PG1과 PG2는 서로 다른 조건에서 벗겨져야 한다(orthogonal).
- → [펩타이드 합성](../wiki/반응/펩타이드%20합성.md)의 "원리", [직교 보호](../wiki/개념/직교%20보호.md), [사면체 중간체](../wiki/개념/사면체%20중간체.md)

#### 7-3. N-Boc: 산으로 벗기는 보호기 (슬라이드 p.10)
- Boc₂O로 도입(methionine → Boc-Met). 산에서 carbonyl O 양성자화 → t-butyl cation(SN1) 이탈 → isobutene + carbamic acid → CO₂ + 아민.
- → [Boc 보호기](../wiki/시약/Boc%20보호기.md), [탄소 양이온](../wiki/개념/탄소%20양이온.md), [TFA](../wiki/시약/TFA.md)

#### 7-4. N-Fmoc: 염기로 벗기는 보호기 (슬라이드 p.11)
- 1차 CH₂라 산에 강하다. fluorene 9번 C–H(pKa 약 25, 14전자 방향족 음이온)가 아민 염기에 떨어지고 E1cB로 dibenzofulvene + carbamate 음이온 → CO₂ + 아민.
- → [Fmoc 보호기](../wiki/시약/Fmoc%20보호기.md), [E1cB 제거](../wiki/개념/E1cB%20제거.md), [방향족성](../wiki/개념/방향족성.md)

#### 7-5. 고체상 펩타이드 합성(SPPS) (슬라이드 p.12)
- 순차적 전략(수지 위에서 탈보호 A와 커플링 B 반복, C→N 방향)과 수렴적 전략(fragment coupling). N-보호기, 곁사슬 보호기, 수지 연결부가 다른 시점에 끊어진다.
- → [펩타이드 합성](../wiki/반응/펩타이드%20합성.md)의 "SPPS", [직교 보호](../wiki/개념/직교%20보호.md), [DCC](../wiki/시약/DCC.md)

### 8. 알데하이드·케톤의 보호기: acetal (슬라이드 p.13–14)

#### 8-1. 씌우기와 벗기기 (슬라이드 p.13)
- ethylene glycol + p-TsOH ⇌ 1,3-dioxolane + H₂O. 물을 빼면 보호, 물과 산을 넣으면 탈보호. 염기·nucleophile에 안정, 산에 불안정.
- → [아세탈 형성](../wiki/반응/아세탈%20형성.md)

#### 8-2. 2절의 두 문제, 이렇게 푼다 (슬라이드 p.14, p.3)
- 예제 1: 케톤을 acetal로 가린 뒤 PhMgBr 2당량 → CH₃COCH₂C(OH)Ph₂. 예제 2: acetal 보호 → Grignard 생성 → HCO₂Et(2차 알코올) → 탈보호로 6-hydroxyundecane-2,10-dione.
- → [아세탈 형성](../wiki/반응/아세탈%20형성.md)의 "예", [그리냐르 시약](../wiki/시약/그리냐르%20시약.md)

### 9. 더 찾아보려면, 그리고 요약 (슬라이드 p.15–16)
- SynArchive 데이터베이스, 두 작용기를 한 고리로 묶는 보호(acetonide, oxazolidinone 등). 요약: 알코올은 silyl ether, 아민은 carbamate, 알데하이드·케톤은 acetal.
- → [보호기](../wiki/개념/보호기.md)의 "더 찾아보려면", "요약"

## 반응 요약표

| 보호 대상 | 보호기 | 도입 조건 | 안정한 조건 | 제거 조건 | 비고 |
|---|---|---|---|---|---|
| 알코올 | [silyl ether](../wiki/시약/실릴%20에터%20보호기.md) (TMS, TES, TBS/TBDMS, TIPS, TBDPS) | R3SiCl, imidazole | nucleophile, C/N 염기 | TBAF (nBu4NF) 또는 H⁺/H2O | 산 안정성: TMS < TES < TBS < TIPS < TBDPS; 염기: TMS < TES < TBS ~ TBDPS < TIPS |
| 알코올 | [THP](../wiki/시약/THP%20보호기.md) | dihydropyran + 산 | 강염기 | H⁺, H2O | THP 자체도 acetal |
| 알코올 | [benzyl ether (OBn)](../wiki/시약/벤질%20에터%20보호기.md) | NaH, BnBr | 거의 모든 조건 | H2, Pd/C 또는 HBr | 강의에서는 부차적(회색 표시) |
| phenol | methyl ether (ArOMe) | NaH, MeI 또는 (MeO)2SO2 | 염기 | BBr3, HBr, HI, Me3SiI | |
| 카복실산 | t-butyl ester | isobutene, H⁺ | nucleophile | 강산 | 산 절단은 t-Bu cation 경유(Boc와 같은 원리) |
| 아민 | [Boc](../wiki/시약/Boc%20보호기.md) (t-BuOCO) | Boc2O, 염기 | electrophile, 염기, 수소화 | 산 (TFA; H⁺, H2O) | 부산물 CO2 + isobutene |
| 아민 | [Cbz](../wiki/시약/Cbz%20보호기.md) (Z, BnOCO) | BnOCOCl, 염기 | electrophile | H2, Pd 또는 HBr/AcOH | 부산물 toluene + CO2 |
| 아민 | [Fmoc](../wiki/시약/Fmoc%20보호기.md) | Fmoc-Cl, 염기 | electrophile, 산 | 아민 염기 (E1cB) | 부산물 dibenzofulvene + CO2; Boc와 직교 |
| 알데하이드, 케톤 | [acetal (1,3-dioxolane)](../wiki/반응/아세탈%20형성.md) | HOCH2CH2OH, p-TsOH (물 제거) | 염기, nucleophile | H2O, p-TsOH | 가역 평형 |

직교성 요약은 [직교 보호](../wiki/개념/직교%20보호.md)에 있다.

## 연습 문제
→ [L12 연습 문제](../practice/L12_Exercises.md) (노트 자체 문제와 해설), [L12 연습문제](../practice/L12_Practice.md) (공식 연습문제 풀이)

## 출처
- 슬라이드: L12 (PDF p.2–16)
