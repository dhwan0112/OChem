# L12 연습 문제와 해설

> [L12 protecting group](../notes/L12_Protecting_Groups.md) 강의 노트에 있던 연습 문제와 해설을 그대로 옮겼다. 공식 연습문제(슬라이드 PDF)의 풀이는 [L12 연습문제](L12_Practice.md)에 따로 있다. 관련 개념: [acetal formation](../wiki/반응/아세탈%20형성.md)(문제 1, 2), [silyl ether protecting group](../wiki/시약/실릴%20에터%20보호기.md)(문제 3, 4), [Boc protecting group](../wiki/시약/Boc%20보호기.md)(문제 5), [Fmoc protecting group](../wiki/시약/Fmoc%20보호기.md)(문제 6), [peptide synthesis](../wiki/반응/펩타이드%20합성.md)(문제 7), [orthogonal protection](../wiki/개념/직교%20보호.md)(문제 8).

## 연습 문제

1. ethyl acetoacetate(CH3COCH2CO2Et)에 PhMgBr을 직접 가하면 어떤 생성물이 주로 생기는가? CH3COCH2C(OH)Ph2를 얻으려면 어떤 순서로 반응시켜야 하는가? (p.3, p.14)
2. CH3CO(CH2)3Br과 ethyl 포메이트로부터 6-hydroxyundecane-2,10-dione을 합성하는 경로를 시약과 함께 쓰고, 보호 없이 Grignard 시약을 만들 수 없는 이유를 설명하라. (p.3, p.14)
3. CH3CH(OH)CH2CH2CH2Br을 lithium acetylide와 반응시켜 CH3CH(OH)(CH2)3C≡CH를 얻으려 한다. 필요한 보호/탈보호 단계와 시약을 쓰고, 보호가 필요한 이유를 설명하라. (p.6)
4. 한 분자에 TES 에테르와 TBDPS 에테르가 있다. 묽은 산 조건에서 어느 쪽이 먼저 제거되는가? 또 TBS와 TIPS를 염기 조건에서 비교하면? (p.7)
5. 산 조건에서 Boc-NHR이 탈보호되는 메커니즘을 단계별로 쓰고, 부산물 두 가지를 쓰라. (p.10)
6. Fmoc 카바메이트가 산에는 안정하고 amine 염기에는 불안정한 이유를 구조와 메커니즘으로 설명하라. (p.11)
7. p.9의 dipeptide 합성에서 Leu와 Gly를 보호 없이 커플링시키면 어떤 문제가 생기는가? N-protecting group은 염기로, C-protecting group은 산으로 제거되어야 한다면 각각 어떤 protecting group이 적합한가? (p.9, p.11, p.5)
8. amine이 Boc로, alcohol이 TBS로, ketone이 acetal로 보호된 분자가 있다. (a) TBAF, (b) TFA, (c) piperidine 처리 시 각각 어느 protecting group이 제거되는가(주된 반응 기준)? (p.5, p.6, p.8, p.13)

## 정답 및 해설

1. 직접 반응시키면 더 친전자성인 ketone이 공격받아 CH3C(OH)(Ph)CH2CO2Et가 생성된다(슬라이드상 52%). 원하는 생성물을 얻으려면 (i) HOCH2CH2OH, H+로 ketone을 acetal로 보호하고, (ii) PhMgBr 2당량을 가한다. ester에 첫 번째 첨가 후 EtO-가 이탈해 ketone이 되고, 두 번째 첨가로 3차 alkoxide가 된다. (iii) H+, H2O로 protonation와 acetal 가수분해를 함께 진행하면 CH3COCH2C(OH)Ph2가 된다. (출처: L12 p.3, p.14)

2. (i) HOCH2CH2OH, H+ 촉매로 ketone을 acetal로 바꾼다. (ii) Mg, Et2O로 Grignard 시약을 만든다. (iii) HCO2Et에 Grignard 2당량: 첫 번째 첨가 후 EtO- 이탈로 aldehyde, 두 번째 첨가로 2차 alkoxide. (iv) H+, H2O로 alcohol을 만들면서 두 acetal을 동시에 벗기면 (CH3CO(CH2)3)2CHOH. 보호하지 않으면 생성되는 C–MgBr(nucleophile)이 다른 분자의 ketone(electrophile)을 공격하므로 Grignard 시약이 존재할 수 없다("impossible Grignard reagent"). (출처: L12 p.3, p.14)

3. (i) t-BuMe2SiCl, imidazole로 OH를 OTBDMS로 바꾼다. (ii) HC≡CLi로 C–Br에서 SN2 치환하여 CH3CH(OTBDMS)(CH2)3C≡CH. (iii) TBAF(또는 H+/H2O)로 탈보호하여 CH3CH(OH)(CH2)3C≡CH. 이유: lithium acetylide는 강염기라 보호되지 않은 OH(alkyne보다 훨씬 산성)를 deprotonate하며 소모되어 alkylation가 일어나지 않는다. (출처: L12 p.6)

4. 산 안정성은 TES (64) << TBDPS (5,000,000)이므로 TES가 먼저 제거된다. 염기 조건에서는 TBS (20,000) < TIPS (100,000)이므로 TIPS가 더 안정하다. (출처: L12 p.7)

5. (1) carbonyl O가 protonate된다. (2) t-Bu–O 결합이 끊어지며 t-butyl cation이 이탈하고 carbamic acid RNHCOOH가 생긴다. (3) t-butyl cation이 H+를 잃고 isobutene이 된다. (4) carbamic acid이 decarboxylate되어 RNH2 + CO2가 된다. 부산물은 CO2와 isobutene(2-methyl프로펜). (출처: L12 p.10)

6. 산 안정성: 카바메이트 O에 붙은 탄소가 1차 CH2라 안정한 carbocation이 생기지 않아 SN1이 불가능하고, 옆의 부피 큰 fluorenyl기 때문에 SN2도 불가능하다. 즉 Boc와 달리 산에서 C–O가 끊어질 경로가 없다. 염기 불안정성: fluorene 9번 C–H는 pKa 약 25로 비교적 산성인데, deprotonation로 생기는 anion이 14전자 방향족계로 안정하기 때문이다. amine 염기가 이 H를 떼면 anion이 CH2–O 결합을 밀어내며 dibenzofulvene과 카바메이트 anion을 E1cB, 카바메이트 anion은 CO2를 잃고 amine이 된다. (출처: L12 p.11)

7. 두 amino acid 모두 NH2(nucleophile)와 CO2H를 가지므로 보호 없이 활성화·커플링하면 Leu–Leu, Gly–Gly, Gly–Leu 등 여러 dipeptide와 올리고머가 섞여 생긴다. N-protecting group을 염기로 벗기려면 Fmoc가 적합하다(amine 염기로 제거, 산에 안정). C-protecting group을 산으로 벗기려면 t-butyl ester가 적합하다(isobutene/H+로 도입, 강산으로 제거). 이 조합은 서로 직교적이어서 각 말단을 골라서 드러낼 수 있다. (출처: L12 p.5, p.9, p.11)

8. (a) TBAF: F-가 Si를 공격하여 TBS만 제거된다(Boc, acetal은 F-에 안정). (b) TFA: Boc가 제거된다. 다만 acetal과 TBS도 산에 불안정하므로 특히 물이 있으면 함께 손상될 위험이 있다. Boc/acetal/TBS는 산 조건에서 서로 직교적이지 않다. (c) piperidine(amine 염기): Boc, TBS, acetal 모두 염기에 안정하므로 제거되는 protecting group이 없다(piperidine은 Fmoc 제거용). (출처: L12 p.5, p.6, p.8, p.11, p.13)
