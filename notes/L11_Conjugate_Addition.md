# L11. 짝지음 첨가 (Conjugate Addition)

<!-- wiki-links:start -->

> **관련 위키 문서** ([위키 대문](../wiki/위키%20대문.md))
> - 반응: [addition-elimination](../wiki/반응/첨가-제거%20반응.md), [conjugate addition](../wiki/반응/공액%20첨가.md), [iminium-catalysed conjugate addition](../wiki/반응/이미늄%20촉매%20공액%20첨가.md), [Michael reaction](../wiki/반응/마이클%20반응.md), [nucleophilic acyl substitution](../wiki/반응/친핵성%20아실%20치환.md), [nucleophilic aromatic substitution](../wiki/반응/친핵성%20방향족%20치환.md), [reductive amination](../wiki/반응/환원성%20아미노화.md), [SN2 reaction](../wiki/반응/SN2%20반응.md)
> - 시약: [alkoxide base](../wiki/시약/알콕사이드%20염기.md), [Grignard reagent](../wiki/시약/그리냐르%20시약.md), [LDA](../wiki/시약/LDA.md), [LiAlH4](../wiki/시약/LiAlH4.md), [NaBH4](../wiki/시약/NaBH4.md), [organocuprate](../wiki/시약/유기구리%20시약.md), [Pd/C](../wiki/시약/Pd-C.md), [pyrrolidine](../wiki/시약/피롤리딘.md)
> - 개념: [1,2-addition vs 1,4-addition](../wiki/개념/1,2-첨가와%201,4-첨가.md), [aromaticity](../wiki/개념/방향족성.md), [E1cB elimination](../wiki/개념/E1cB%20제거.md), [electrophile and nucleophile](../wiki/개념/친전자체와%20친핵체.md), [enamine](../wiki/개념/엔아민.md), [enol and enolate](../wiki/개념/엔올과%20엔올레이트.md), [hard and soft acids and bases (HSAB)](../wiki/개념/하드-소프트%20산염기.md), [imine](../wiki/개념/이민.md), [iminium ion](../wiki/개념/이미늄%20이온.md), [kinetic vs thermodynamic control](../wiki/개념/속도론적%20지배와%20열역학적%20지배.md), [kinetic vs thermodynamic enolate](../wiki/개념/속도론적%20엔올레이트와%20열역학적%20엔올레이트.md), [Meisenheimer complex](../wiki/개념/마이젠하이머%20착물.md)

<!-- wiki-links:end -->

> 이 강의 노트는 **뼈대**다. 강의 순서와 슬라이드 위치만 정리했고, 설명은 링크된 개념 문서에 있다.

> 강의 흐름대로 길게 읽고 싶으면 **[통독본](통독/L11_Conjugate_Addition.md)**(재구성 직전의 전체 노트, 소절마다 개념 문서 링크 포함)을 본다.

## 개요

L1~L2의 alkene은 electrophile을 받는 nucleophile이었다. 이 강의는 C=C 옆에 carbonyl 같은 EWG가 짝지어 붙으면 alkene이 거꾸로 nucleophile을 받는 electrophile이 된다는 데서 출발한다. 먼저 $\beta$-탄소가 왜 $\delta^{+}$인지와 conjugate addition의 일반형을 보고, nucleophile이 carbonyl 탄소(1,2)와 $\beta$-탄소(1,4) 중 어디를 칠지를 정하는 세 요인(받개의 작용기, nucleophile의 hard/soft, kinetic/thermodynamic 조건)을 정리한다. 이어서 L7·L8·L10에서 만든 enolate와 enamine을 Michael acceptor에 붙여 1,5-dicarbonyl을 만들고, 받개를 iminium ion으로 활성화하는 유기 촉매를 본다. 마지막으로 $\beta$-leaving group이 있으면 첨가 뒤 제거가 일어난다는 점을 benzene 고리로 넓혀 SNAr까지 잇는다.

## 강의 흐름

### 1. conjugated system과 $\beta$-탄소의 $\delta^{+}$ (슬라이드 p.3)
- C=O와 짝지은 C=C는 공명으로 carbonyl 탄소와 $\beta$-탄소 두 곳이 $\delta^{+}$가 된다. IR(1675 cm⁻¹)과 ¹³C NMR($\beta$-C 약 140 ppm)이 그 증거다. $\beta,\gamma$-unsaturated ketone은 해당 없다.
- → [conjugate addition](../wiki/반응/공액%20첨가.md)의 "원리"

### 2. conjugate addition(Michael addition)의 일반형 (슬라이드 p.4)
- Nu는 $\beta$-탄소에, H는 $\alpha$-탄소에 붙는다. 짝지은 EWG가 반드시 필요하다. 예: mesityl oxide + PhSH(94%), chalcone + CN⁻(95%).
- → [conjugate addition](../wiki/반응/공액%20첨가.md)

#### 2.1 amine의 첨가 (슬라이드 p.5)
- 1차·2차 amine → $\beta$-아미노 carbonyl. zwitterion → 양성자 이동 → tautomerization의 네 단계, 모두 가역.
- → [conjugate addition](../wiki/반응/공액%20첨가.md)의 "메커니즘", [keto–enol tautomerization](../wiki/반응/케토-엔올%20토토머화.md)

#### 2.2 organocuprate의 첨가 (슬라이드 p.6–7)
- C–Cu는 C–Mg보다 덜 분극되어 soft하므로 $\beta$-탄소를 고른다. R₂CuLi는 CuBr + 2 RLi로 만들고, MeMgBr + CuCl(0.01 eq)은 transmetallation으로 촉매적으로 돈다. CuCl이 없으면 1,2.
- → [organocuprate](../wiki/시약/유기구리%20시약.md), [Grignard reagent](../wiki/시약/그리냐르%20시약.md)

#### 2.3 연습: cuprate로 무엇을 만들 수 있나 (슬라이드 p.8)
- 생성물에서 $\beta$-치환기 하나를 R₂CuLi의 R로 떼고 $\alpha$–$\beta$에 C=C를 다시 넣으면 출발 enone이 나온다.
- → [organocuprate](../wiki/시약/유기구리%20시약.md)의 "역합성 요령", [연습 문제](../practice/L11_Exercises.md) 문제 1

### 3. 1,2-첨가와 1,4-첨가 (슬라이드 p.9–13)
- 1,2는 allyl alcohol, 1,4는 enol을 거쳐 ketone을 준다. 무엇이 정하는가: 받개의 작용기, nucleophile, 반응 조건.
- → [1,2-addition과 1,4-addition](../wiki/개념/1,2-첨가와%201,4-첨가.md)

#### 3.1 요인 1: 받개의 작용기 (슬라이드 p.10)
- 직접 첨가 비율 acyl chloride > enal > enone > ester > amide. cinnamaldehyde + NaBH₄는 1,2, cyclopentenone + NaBH₄는 1,4 후 1,2.
- → [1,2-addition과 1,4-addition](../wiki/개념/1,2-첨가와%201,4-첨가.md), [NaBH4](../wiki/시약/NaBH4.md), [addition-elimination](../wiki/반응/첨가-제거%20반응.md)(acyl chloride + NH₃)

#### 3.2 요인 2: nucleophile, Grignard vs cuprate (슬라이드 p.11–12)
- hard nucleophile(RMgBr, RLi)은 carbonyl 탄소로(1,2), soft nucleophile(R₂CuLi, RS⁻)은 $\beta$-탄소로(1,4).
- → [HSAB](../wiki/개념/하드-소프트%20산염기.md), [Grignard reagent](../wiki/시약/그리냐르%20시약.md), [organocuprate](../wiki/시약/유기구리%20시약.md)

#### 3.3 요인 3: kinetic vs thermodynamic product (슬라이드 p.13)
- MVK + NaCN/HCN: 5–10 °C에서 cyanohydrin(1,2, kinetic, 가역), 80 °C에서 NC–CH₂CH₂–COCH₃(1,4, thermodynamic). 1,4는 약한 C=C $\pi$를 잃고 C=O를 보존한다.
- → [1,2-addition과 1,4-addition](../wiki/개념/1,2-첨가와%201,4-첨가.md), [kinetic control과 thermodynamic control](../wiki/개념/속도론적%20지배와%20열역학적%20지배.md)

### 4. enolate의 conjugate addition: 1,5-dicarbonyl (슬라이드 p.14–17)
- → [Michael reaction](../wiki/반응/마이클%20반응.md)

#### 4.1 기본형 (슬라이드 p.14)
- enolate $\alpha$-탄소가 Michael acceptor의 $\beta$-탄소를 쳐서 새 enolate → protonate하면 1,5-dicarbonyl. acrylonitrile도 좋은 받개다.
- → [Michael reaction](../wiki/반응/마이클%20반응.md)의 "메커니즘", [enol and enolate](../wiki/개념/엔올과%20엔올레이트.md)

#### 4.2 경쟁 반응: conjugate addition vs aldol (슬라이드 p.15)
- aldol(1,2)은 가역이라 결국 conjugate addition으로 모인다. 경향은 R = H < alkyl < OR < NR₂. LDA enolate + amide 받개(60%).
- → [Michael reaction](../wiki/반응/마이클%20반응.md)의 "선택성", [aldol reaction](../wiki/반응/알돌%20반응.md)

#### 4.3 counterion과 enolate 종류 (슬라이드 p.16)
- Li⁺ + enal은 고리형 TS로 aldol(72%). t-BuOK는 thermodynamic enolate로 4차 탄소를 만든다(53%).
- → [Michael reaction](../wiki/반응/마이클%20반응.md), [kinetic vs thermodynamic enolate](../wiki/개념/속도론적%20엔올레이트와%20열역학적%20엔올레이트.md), [alkoxide base](../wiki/시약/알콕사이드%20염기.md)

#### 4.4 안정한 enolate: 1,3-dicarbonyl과 nitroalkane (슬라이드 p.17)
- malonate + ethyl crotonate, PhCH₂NO₂ + cyclohexenone(Al₂O₃, 92%), nitromethane의 conjugate addition 후 분자 내 SN2 고리화(65%).
- → [Michael reaction](../wiki/반응/마이클%20반응.md), [malonic ester synthesis](../wiki/반응/말론산%20에스터%20합성.md), [$\alpha$-H acidity](../wiki/개념/α-수소의%20산도.md)

### 5. enamine: 중성이면서 soft한 nucleophile (슬라이드 p.18–20)

#### 5.1 enamine 복습 (슬라이드 p.18)
- ketone + 2차 amine → enamine, R–X로 $\alpha$-alkylation 후 가수분해. iminium과 enamine은 양성자 하나 차이.
- → [enamine](../wiki/개념/엔아민.md), [Stork enamine reaction](../wiki/반응/스토크%20엔아민%20반응.md), [iminium ion](../wiki/개념/이미늄%20이온.md), [reductive amination](../wiki/반응/환원성%20아미노화.md)

#### 5.2 enamine의 conjugate addition (슬라이드 p.19)
- pyrrolidine·morpholine enamine이 받개의 말단 CH₂에 붙고, 후처리 가수분해로 1,5-dicarbonyl(95%, 75%).
- → [Michael reaction](../wiki/반응/마이클%20반응.md)의 "enamine" 절, [연습 문제](../practice/L11_Exercises.md) 문제 6

#### 5.3 합성 응용: dopamine antagonist (슬라이드 p.20)
- ester enolate + acrylonitrile(Triton B) → H₂/Pd/C로 amine, lactam 고리화 → alkylation과 환원.
- → [Michael reaction](../wiki/반응/마이클%20반응.md)의 "예", [연습 문제](../practice/L11_Exercises.md) 문제 7

### 6. iminium ion 촉매 (슬라이드 p.21)
- 키랄 imidazolidinone이 enal을 iminium으로 바꿔 받개를 활성화하고, benzyl group이 한쪽 면을 가려 87–97% ee.
- → [iminium-catalyzed conjugate addition](../wiki/반응/이미늄%20촉매%20공액%20첨가.md), [iminium ion](../wiki/개념/이미늄%20이온.md)

### 7. $\beta$-leaving group이 있는 conjugate addition과 SNAr (슬라이드 p.22–23)

#### 7.1 첨가-제거 메커니즘 (슬라이드 p.22)
- $\beta$-F enone + R₂NH: 첨가로 생긴 enolate가 F⁻를 밀어내 $\beta$-아미노 enone. C=C가 다시 생긴다.
- → [addition-elimination](../wiki/반응/첨가-제거%20반응.md)

#### 7.2 nucleophilic aromatic substitution(SNAr) (슬라이드 p.22–23)
- 강한 EWG가 붙은 halobenzene에서 첨가(느림) → $\sigma$ complex → 제거. 규칙: F >> Cl ~ Br >> I, 강한 EWG(NO₂ 최강), leaving group은 EWG의 ortho/para.
- → [SNAr](../wiki/반응/친핵성%20방향족%20치환.md), [Meisenheimer complex](../wiki/개념/마이젠하이머%20착물.md)

### 8. 요약 (슬라이드 p.24)
- 1,4 vs 1,2 / RMgBr + CuCl(촉매) / enolate·enamine → 1,5-dicarbonyl / iminium 촉매 / $\beta$-leaving group → SNAr. 공통 뼈대: Nu가 $\beta$-탄소 공격 → enolate → enol → ketone.
- → [conjugate addition](../wiki/반응/공액%20첨가.md)의 "공통 뼈대"

## 반응 요약표

| 반응 | 시약/조건 | 생성물 | regioselectivity | 비고 |
|---|---|---|---|---|
| thiol 첨가 ([conjugate addition](../wiki/반응/공액%20첨가.md)) | mesityl oxide + PhSH, 25 °C | (CH3)2C(SPh)CH2COCH3 (94%) | 1,4 | soft (p.4) |
| 시안화 첨가 ([conjugate addition](../wiki/반응/공액%20첨가.md)) | chalcone + ⁻CN, EtOH, HOAc | PhCH(CN)CH2COPh (95%) | 1,4 | 새 입체중심, 라세미(보충) (p.4) |
| amine 첨가 ([conjugate addition](../wiki/반응/공액%20첨가.md)) | mesityl oxide + MeNH2, H2O | (CH3)2C(NHMe)CH2COCH3 (75%) | 1,4 | zwitterion 경유 (p.5) |
| cuprate 제조 ([organocuprate](../wiki/시약/유기구리%20시약.md)) | CuBr + 2 RLi, Et2O, −78 °C | R2CuLi + LiBr | – | 즉시 사용 (p.6) |
| Cu catalyst Grignard ([organocuprate](../wiki/시약/유기구리%20시약.md)) | isophorone + MeMgBr, CuCl 0.01 eq | 3,3,5,5-tetramethylcyclohexanone (83%) | 1,4 | CuCl 없으면 1,2 (p.6–7) |
| Grignard/RLi ([Grignard reagent](../wiki/시약/그리냐르%20시약.md)) | 2-cyclohexenone + CH3MgBr 또는 CH3Li; H3O⁺ | 1-methyl-2-cyclohexen-1-ol (95%) | 1,2 | hard (p.11) |
| cuprate ([organocuprate](../wiki/시약/유기구리%20시약.md)) | 2-cyclohexenone + (CH3)2CuLi; H3O⁺ | 3-methylcyclohexanone (97%) | 1,4 | soft (p.11) |
| acyl chloride + NH3 ([addition-elimination](../wiki/반응/첨가-제거%20반응.md)) | CH2=CHCOCl + NH3 | CH2=CHCONH2 | 1,2(acyl 치환) | (p.10) |
| acrylate + NH3 ([conjugate addition](../wiki/반응/공액%20첨가.md)) | CH2=CHCO2Me + NH3 | H2NCH2CH2CO2Me | 1,4 | (p.10) |
| enal 환원 ([NaBH4](../wiki/시약/NaBH4.md)) | cinnamaldehyde + NaBH4, EtOH | cinnamyl alcohol (97%) | 1,2 | (p.10) |
| 고리 enone 환원 ([NaBH4](../wiki/시약/NaBH4.md)) | cyclopentenone + NaBH4, EtOH | cyclopentanol (99%) | 1,4 후 1,2 | (p.10) |
| HCN addition, 저온 ([1,2-addition과 1,4-addition](../wiki/개념/1,2-첨가와%201,4-첨가.md)) | MVK + NaCN, HCN, 5–10 °C | cyanohydrin | 1,2 | kinetic, 가역 (p.13) |
| HCN addition, 고온 ([1,2-addition과 1,4-addition](../wiki/개념/1,2-첨가와%201,4-첨가.md)) | MVK + NaCN, HCN, 80 °C | NCCH2CH2COCH3 | 1,4 | thermodynamic (p.13) |
| enolate Michael ([Michael reaction](../wiki/반응/마이클%20반응.md)) | cyclohexanone + LDA; (E)-CH3CH=CHCONMe2 | 1,5-ketoamide (60%) | 1,4 | amide 받개 (p.15) |
| Li enolate + enal ([aldol reaction](../wiki/반응/알돌%20반응.md)) | ethyl isobutyrate + LDA, −78 °C; (CH3)2C=CHCHO | $\beta$-hydroxy ester (72%) | 1,2(aldol) | Li⁺ 배위 (p.16) |
| thermodynamic enolate Michael ([Michael reaction](../wiki/반응/마이클%20반응.md)) | 2-methylcyclopentanone + methyl acrylate, t-BuOK | 4차 탄소 생성물 (53%) | 1,4 | (p.16) |
| malonate Michael ([Michael reaction](../wiki/반응/마이클%20반응.md)) | CH2(CO2Et)2 + ethyl crotonate, NaOEt | (EtO2C)2CHCH(CH3)CH2CO2Et | 1,4 | 안정한 enolate (p.17) |
| nitroalkane Michael ([Michael reaction](../wiki/반응/마이클%20반응.md)) | PhCH2NO2 + 2-cyclohexenone, Al2O3 | 3-(CH(Ph)NO2)cyclohexanone (92%) | 1,4 | (p.17) |
| Michael–분자 내 alkylation ([Michael reaction](../wiki/반응/마이클%20반응.md)) | I(CH2)4CH=CHCO2Me + CH3NO2, Cs2CO3, DMF | methyl 2-(2-nitrocyclohexyl)acetate (65%) | 1,4 후 SN2 | (p.17) |
| enamine alkylation ([Stork enamine reaction](../wiki/반응/스토크%20엔아민%20반응.md)) | cyclohexanone + pyrrolidine; R–X; H3O⁺ | 2-R-cyclohexanone | $\alpha$ | (p.18) |
| enamine Michael ([Michael reaction](../wiki/반응/마이클%20반응.md)) | pyrrolidine enamine + CH2=C(SMe)CO2Me; H2O | 1,5-dicarbonyl (95%) | 1,4 | (p.19) |
| enamine Michael ([Michael reaction](../wiki/반응/마이클%20반응.md)) | morpholine enamine + CH2=C(SO2Ph)COCH3, SiO2; H2O | 1,5-diketone (75%) | 1,4 | (p.19) |
| iminium 촉매 ([iminium-catalyzed conjugate addition](../wiki/반응/이미늄%20촉매%20공액%20첨가.md)) | enal + pyrrole, imidazolidinone 20 mol% | $\beta$-pyrrolyl aldehyde (68–90%) | 1,4 | 87–97% ee, (R) (p.21) |
| $\beta$-leaving group 치환 ([addition-elimination](../wiki/반응/첨가-제거%20반응.md)) | 2-F-cyclohexenyl methyl ketone + R2NH | $\beta$-아미노 enone | $\beta$ 치환 | (p.22) |
| SNAr ([nucleophilic aromatic substitution](../wiki/반응/친핵성%20방향족%20치환.md)) | o-F-acetophenone + R2NH | o-NR2-acetophenone | ipso | ortho EWG (p.23) |
| SNAr ([nucleophilic aromatic substitution](../wiki/반응/친핵성%20방향족%20치환.md)) | p-Cl-nitrobenzene + HO⁻ | p-nitrophenol | ipso | para EWG (p.23) |

## 연습 문제
→ [L11 연습 문제](../practice/L11_Exercises.md)

## 출처
- 슬라이드: L11 (PDF p.3–24)
