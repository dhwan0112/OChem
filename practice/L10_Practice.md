# L10 연습문제: 엔올·엔아민과 β-케토에스터 화학

> 출처: L10_Practice.pdf (문제), Practice_L10_solutions.pdf (공식 풀이). CM3121 Advanced Organic Chemistry (Dr. Zhu Ye)

---

## 문제 1

intermediate와 생성물의 구조를 제시하라 (Propose the structures of the intermediates and the products).

출발물질: N-methyl 비스(3-propanoic acid ethyl) amine, 즉 EtO2C-CH2CH2-N(CH3)-CH2CH2-CO2Et

1. `EtO2C-CH2CH2-N(CH3)-CH2CH2-CO2Et --[EtONa]--> (A)`
2. `(A) --[EtONa, 그다음 알릴 allyl bromide CH2=CHCH2Br]--> (B)`
3. `(B) --[NaOH, H2O, 그다음 NH4Cl로 quench]--> (C)`
4. `(C) --[heat, -CO2]--> (D)`

### 공식 풀이

- (A): ethyl 1-methyl-4-oxopiperidine-3-carboxylate (6원 고리: N-CH2-CH(CO2Et)-C(=O)-CH2-CH2-N). 4번 탄소가 ketone, 3번 탄소에 CO2Et.
- (B): 3번 탄소(두 carbonyl 사이)에 allyl group이 붙은 4급 탄소 화합물. ethyl 3-allyl-1-methyl-4-oxopiperidine-3-carboxylate.
- (C): ester가 carboxylic acid으로 바뀐 3-allyl-1-methyl-4-oxopiperidine-3-carboxylic acid (β-keto acid).
- (D): decarboxylation 생성물 3-allyl-1-methylpiperidine-4-one.

(출처: Practice_L10_solutions p.1)

### 해설

이 문제의 핵심은 왜 아무 탄소도 아닌 바로 그 자리에서 고리가 닫히고, alkylation가 일어나고, CO2가 빠지는가이다. 답은 모두 하나의 원리, 즉 "두 carbonyl 사이 수소의 산성도"로 이어진다.

첫 단계는 Dieckmann condensation, 즉 분자 내 Claisen condensation(intramolecular Claisen condensation)이다(→ [L9](../notes/L09_Claisen_Condensation.md) Claisen 문서 참고). EtONa가 한쪽 ester의 α-CH2를 deprotonate하여 ester enolate를 만들고, 이것이 반대편 ester의 carbonyl을 공격한다. 고리 원자를 세어 보면 α-C, CH2, N, CH2, CH2, C(=O)로 6원 고리가 되므로 thermodynamic으로 유리하다. tetrahedral intermediate에서 EtO⁻가 떨어져 나가면 β-ketoester가 생긴다. 그런데 이 단계는 그 자체로는 평형이 불리할 수도 있다. 그래서 실제 구동력은 생성된 β-ketoester의 C3-H(pKa 약 11)가 EtO⁻에 의해 곧바로 deprotonate되는 마지막 단계에서 나온다. 공식 풀이는 산 처리 후의 중성 형태를 그린 것이다.

두 번째 단계는 β-ketoester의 alkylation, 즉 acetoacetic ester acetoacetic ester synthesis과 같은 논리이다(→ [L7](../notes/L07_Enolate_Alkylation.md) enolate alkylation 문서 참고). C3-H는 ketone과 ester 사이에 끼어 있어 가장 산성이므로 EtONa로 충분히 enolate가 되고, 이 안정화된 enolate가 allyl bromide에 SN2로 공격한다. allyl halide는 SN2에 특히 반응성이 좋은 electrophile이다. 그 결과 C3는 4급 탄소가 된다.

세 번째 단계에서 NaOH 수용액은 ester를 saponification하여 carboxylate로 바꾸고, NH4Cl로 퀜칭하여 β-keto acid(β-keto acid)을 얻는다. 마지막으로 가열하면 β-keto acid은 6원 고리 transition state(cyclic six-membered transition state)를 거쳐 CO2를 내놓고 enol이 되며, enol은 keto 형태로 tautomerization한다(→ [L10](../notes/L10_Enol_and_Enamine.md) enol 문서 참고). 즉 CO2Et는 "enolate를 만들기 쉽게 해 주는 임시 활성화기"였고, 역할을 마친 뒤 제거되는 것이다. 최종적으로 piperidine-4-one의 3번 위치에 allyl group 하나만 남는다.

검토 의견: 공식 답 자체는 옳다. 다만 (C)는 분자 안에 3차 amine(N-CH3)과 carboxylic acid이 함께 있으므로, 약산인 NH4Cl(pKa 약 9.2)로 퀜칭한 상태에서는 실제로 zwitterion(암모늄 carboxylate) 형태로 존재할 가능성이 높다. 공식 풀이의 중성 COOH 표기는 단순화한 것으로 이해하면 된다. decarboxylation에는 COOH(protonate된 형태)가 필요하며, 강산 대신 NH4Cl을 쓰는 이유는 amine의 과도한 protonation를 피하면서 β-keto acid을 얻기 위한 것으로 해석할 수 있다.

### 핵심 개념

Dieckmann condensation(6원 고리 β-ketoester) → 활성 메틴 alkylation → 비누화 → β-keto acid decarboxylation: acetoacetic ester 합성의 고리판.

---

## 문제 2

다음 화합물의 합성을 제안하라. 출발물질은 연속된 탄소 사슬이 최대 3개인 것만 사용한다 (O, N, H 원자는 세지 않으며, 표적 분자에 남지 않는 시약은 고려하지 않는다).

표적: diethyl 4,5-dioxocyclopentane-1,3-dicarboxylate, 즉 사이클로펜탄-1,2-dione의 3번과 5번 탄소에 각각 CO2Et가 붙은 화합물 (EtO2C-CH 고리 C(=O)-C(=O) 구조, 두 CH(CO2Et) 사이에 CH2 하나).

### 공식 풀이

1. `EtO2C-CH2CH2-Br + CH2(CO2Et)2 --[NaOEt]--> EtO2C-CH2CH2-CH(CO2Et)2` (새 C-C 결합 형성)
2. `--[NaOH, 물; 그다음 HCl]--> HOOC-CH2CH2-CH(COOH)2`
3. `--[가열, -CO2]--> HOOC-CH2CH2CH2-COOH` (glutaric acid, glutaric acid)
4. `--[EtOH, H2SO4]--> EtO2C-CH2CH2CH2-CO2Et` (diethyl glutarate)
5. `디에틸 글루타레이트 + 디에틸 EtO2C-CO2Et --[NaOEt]--> EtO2C-CH(CO-CO2Et)-CH2CH2-CO2Et`
6. `--[NaOEt]--> 표적 화합물` (분자 내 고리화)

(출처: Practice_L10_solutions p.2)

### 해설

이 문제의 핵심은 왜 이렇게 돌아가는 경로를 택해야 하는가이다. 표적의 탄소 골격을 끊어 보면 두 개의 C(=O)-C(=O) 단위는 oxalate(C2)에서, 나머지 CH(CO2Et)-CH2-CH(CO2Et)는 glutarate(C5)에서 온다는 retrosynthesis이 자연스럽다. 그런데 glutaric acid은 탄소가 5개 연속이므로 출발물질로 쓸 수 없다. 그래서 먼저 C3 조각 두 개로 glutaric acid을 "만들어야" 한다.

이 부분이 malonic ester malonic ester synthesis이다(→ [L7](../notes/L07_Enolate_Alkylation.md) enolate alkylation 문서 참고). diethyl 말로네이트의 CH2는 두 ester 사이에 있어 pKa 약 13이므로 NaOEt로 쉽게 enolate가 되고, 이것이 ethyl 3-bromo프로파노에이트의 C-Br에 SN2로 붙는다. 그다음 세 ester를 모두 가수분해하여 트리카복실산으로 만들고, 가열하면 malonic 부분(같은 탄소에 COOH 두 개)만 6원 고리 transition state를 거쳐 CO2 하나를 잃는다. 즉 말로네이트의 탄소 하나는 활성화기로만 쓰이고 사라지며, 결과적으로 CH2-COOH 단위 하나가 늘어난 glutaric acid이 생긴다. 이것을 피셔 ester화(Fischer esterification, EtOH/H2SO4)로 diethyl glutarate로 바꾼다.

이제 고리를 만든다. diethyl oxalate는 α-수소가 없어 스스로 enolate가 될 수 없지만, carbonyl이 매우 친전자적이므로 "받는 쪽" 전용 파트너로 이상적이다. 그래서 교차 Claisen condensation(crossed Claisen condensation)에서 glutarate의 enolate가 oxalate를 공격하여 α-옥살릴 화합물(α-keto ester가 붙은 형태)이 된다(→ [L9](../notes/L09_Claisen_Condensation.md) Claisen 문서 참고). 이어서 glutarate의 반대편 α-탄소가 enolate가 되어 남아 있는 옥살릴 ester carbonyl을 분자 내에서 공격하고(Dieckmann형 고리화), EtO⁻가 빠지면 5원 고리 1,2-dione이 닫힌다. 고리 원자는 α-C, C=O, C=O, α'-C, CH2로 정확히 5개이다.

검토 의견: 공식 경로는 타당하다. 참고로 (1) NaOEt 조건에서 ethyl 3-bromo프로파노에이트는 E2로 ethyl acrylate가 될 수 있는데, 이 경우에도 말로네이트의 Michael addition(→ L11 짝첨가 문서 참고)로 같은 트리에스터가 생기므로 결과는 같다. (2) 표적 화합물은 매우 산성인 C-H(β-dicarbonyl)와 1,2-dione enol을 가지므로 NaOEt 조건에서는 anion으로 존재하며, 중성 화합물을 얻으려면 산 workup가 필요하다. 공식 풀이에는 이 산 처리가 생략되어 있다. (3) 실제로는 5와 6단계를 한 번에(diethyl glutarate + diethyl oxalate + NaOEt) 진행하는 것이 일반적이다.

### 핵심 개념

malonic ester 합성으로 탄소 사슬을 늘리고(C3 + C3 - CO2 = C5), oxalate와의 교차 Claisen + 분자 내 Claisen으로 5원 고리 1,2-dione을 만든다.

---

## 문제 3

다음 반응의 단계별 메커니즘을 제안하라. (힌트: 처음에 enamine이 형성된다.)

`2-(2-옥소에틸)-6-(4-옥소펜틸)피페리딘 --[acid]--> 삼환 생성물`

- 출발물질: 2차 amine(NH) piperidine 고리. C2에 CH2-CHO, C6에 CH2CH2CH2-CO-CH3.
- 생성물: N을 공유하는 tricyclic amine. 원래 piperidine 고리 + ketone 쪽에서 만들어진 새 6원 고리(N에 이웃한 C=C를 가진 enamine) + aldehyde 쪽에서 만들어진 새 6원 고리(OH를 가진 CH).

### 공식 풀이

1. amine N이 ketone carbonyl을 분자 내 공격 → carbinolamine(carbinolamine, N-C(OH)(CH3)) 형성, 6원 고리 생성.
2. OH가 떨어져 나가며(OH⁻로 표시) iminium iminium ion 형성.
3. OH⁻가 methyl group의 H를 떼어 냄 → 고리 바깥 C=CH2 enamine(exocyclic enamine).
4. enamine의 CH2 말단이 aldehyde carbonyl을 공격 → 새 6원 고리, iminium 이온 + alkoxide(O⁻).
5. alkoxide가 iminium 이웃 고리 C-H를 떼어 냄 → 고리 안 C=C enamine + OH, 최종 생성물.

(출처: Practice_L10_solutions p.3)

### 해설

이 문제의 핵심은 왜 2차 amine 하나가 두 개의 carbonyl을 순서대로 엮어 두 개의 고리를 만들 수 있는가이다. 답은 enamine 화학, 즉 "amine이 carbonyl을 enol과 같은 탄소 nucleophile로 바꿔 준다"는 점에 있다(→ [L10](../notes/L10_Enol_and_Enamine.md) enamine 문서 참고).

먼저 산 촉매 아래에서 2차 amine의 N이 ketone carbonyl을 공격한다. 이 공격이 쉬운 이유는 분자 내 반응이고, 만들어지는 고리가 N, C6, CH2, CH2, CH2, C(ketone)의 6원 고리이기 때문이다. 생성된 carbinolamine의 OH는 protonate되어 물로 떠나고, 그 결과 C=N⁺ iminium 이온이 생긴다. 그런데 N이 2차 amine이었으므로 iminium N에는 더 이상 떼어 낼 H가 없다. 그래서 중성으로 돌아가려면 이웃 탄소의 H를 잃어야 하고, 이것이 enamine 형성이다. 공식 풀이는 methyl(CH3) 쪽 H를 떼어 고리 바깥의 C=CH2 enamine을 만든다.

왜 methyl 쪽이어야 하는가? 이 enamine의 CH2 말단이 aldehyde를 공격할 때 생기는 고리를 세어 보면 N, C2(piperidine), CH2, CH(O), CH2(원래 methyl), C(iminium)로 6원 고리가 된다. 즉 원하는 위치에 고리를 닫을 수 있는 enamine은 methyl 쪽 enamine뿐이고, enamine 형성은 가역적이므로 반응은 결국 이 경로로 흘러간다. enamine의 β-탄소는 질소 고립 전자쌍이 밀어 준 전자 밀도로 친핵성을 가지며, aldehyde는 ketone보다 친전자적이므로 이 intramolecular aldol형(aldol-type) 첨가가 잘 일어난다(→ [L8](../notes/L08_Aldol_Reactions.md) aldol 문서 참고). 그 결과 새 iminium 이온과 alkoxide가 생긴다.

마지막으로 iminium 이온은 다시 이웃 탄소의 H를 잃어 enamine이 되는데, 이번에는 원래 ketone 쪽 고리의 CH2에서 H가 빠져 고리 안(endocyclic) C=C가 형성된다. 동시에 alkoxide는 양성자를 받아 OH가 된다. 즉 최종 생성물은 2차 alcohol과 enamine을 가진 삼환 화합물이다. 문제에 수용액 hydrolysis 단계가 주어져 있지 않으므로, 공식 풀이는 iminium을 ketone으로 되돌리지 않고 중성 enamine 형태를 최종 생성물로 그린다.

검토 의견: 공식 풀이의 연결 관계(어떤 결합이 형성되는지)와 생성물은 옳다. 다만 반응 조건이 "acid"인데 메커니즘에서는 OH⁻가 leaving group 및 염기로, O⁻(alkoxide)가 염기로 그려져 있다. 산성 조건에서는 OH가 먼저 protonate되어 H2O로 떠나고, deprotonation는 물이나 짝염기가 담당하며, aldehyde carbonyl은 protonation(또는 공격 직후 양성자 전달)되어 alkoxide 대신 중성 OH가 생긴다고 쓰는 것이 조건에 더 맞는 표기이다. 시험 답안에서는 산 조건에 맞춘 양성자 전달 단계를 쓰는 편이 안전하다.

### 핵심 개념

2차 amine + ketone → iminium → enamine(탄소 nucleophile) → 분자 내 aldehyde 공격(만니히/aldol형) → 다시 enamine. 고리 크기(6원)가 어느 α-탄소가 반응할지를 결정한다.
