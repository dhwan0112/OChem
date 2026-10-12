# L11. 짝지음 첨가 (Conjugate Addition)

<!-- wiki-links:start -->

> **관련 위키 문서** ([[위키 대문]])
> - 반응: [[SN2 반응]], [[공액 첨가]], [[마이클 반응]], [[이미늄 촉매 공액 첨가]], [[첨가-제거 반응]], [[친핵성 방향족 치환]], [[친핵성 아실 치환]], [[환원성 아미노화]]
> - 시약: [[LDA]], [[LiAlH4]], [[NaBH4]], [[Pd-C|Pd/C]], [[그리냐르 시약]], [[알콕사이드 염기]], [[유기구리 시약]], [[피롤리딘]]
> - 개념: [[1,2-첨가와 1,4-첨가]], [[E1cB 제거]], [[마이젠하이머 착물]], [[방향족성]], [[속도론적 엔올레이트와 열역학적 엔올레이트]], [[속도론적 지배와 열역학적 지배]], [[엔아민]], [[엔올과 엔올레이트]], [[이미늄 이온]], [[이민]], [[친전자체와 친핵체]], [[하드-소프트 산염기]]

<!-- wiki-links:end -->

> 이 강의 노트는 **뼈대**다. 강의 순서와 슬라이드 위치만 정리했고, 설명은 링크된 개념 문서에 있다.

## 개요

L1~L2의 알켄은 electrophile을 받는 nucleophile이었다. 이 강의는 C=C 옆에 carbonyl 같은 EWG가 짝지어 붙으면 알켄이 거꾸로 nucleophile을 받는 electrophile이 된다는 데서 출발한다. 먼저 β-탄소가 왜 δ+인지와 conjugate addition의 일반형을 보고, nucleophile이 carbonyl 탄소(1,2)와 β-탄소(1,4) 중 어디를 칠지를 정하는 세 요인(받개의 작용기, nucleophile의 hard/soft, kinetic/thermodynamic 조건)을 정리한다. 이어서 L7·L8·L10에서 만든 enolate와 enamine을 Michael acceptor에 붙여 1,5-dicarbonyl을 만들고, 받개를 iminium ion으로 활성화하는 유기 촉매를 본다. 마지막으로 β-이탈기가 있으면 첨가 뒤 제거가 일어난다는 점을 벤젠 고리로 넓혀 SNAr까지 잇는다.

## 강의 흐름

### 1. conjugated system과 β-탄소의 δ+ (슬라이드 p.3)
- C=O와 짝지은 C=C는 공명으로 carbonyl 탄소와 β-탄소 두 곳이 δ+가 된다. IR(1675 cm⁻¹)과 ¹³C NMR(β-C 약 140 ppm)이 그 증거다. β,γ-불포화 케톤은 해당 없다.
- → [[공액 첨가|conjugate addition]]의 "원리"

### 2. conjugate addition(Michael addition)의 일반형 (슬라이드 p.4)
- Nu는 β-탄소에, H는 α-탄소에 붙는다. 짝지은 EWG가 반드시 필요하다. 예: mesityl oxide + PhSH(94%), chalcone + CN⁻(95%).
- → [[공액 첨가]]

#### 2.1 아민의 첨가 (슬라이드 p.5)
- 1차·2차 아민 → β-아미노 carbonyl. zwitterion → 양성자 이동 → tautomerization의 네 단계, 모두 가역.
- → [[공액 첨가]]의 "메커니즘", [[케토-엔올 토토머화]]

#### 2.2 organocuprate의 첨가 (슬라이드 p.6–7)
- C–Cu는 C–Mg보다 덜 분극되어 soft하므로 β-탄소를 고른다. R₂CuLi는 CuBr + 2 RLi로 만들고, MeMgBr + CuCl(0.01 eq)은 transmetallation으로 촉매적으로 돈다. CuCl이 없으면 1,2.
- → [[유기구리 시약]], [[그리냐르 시약]]

#### 2.3 연습: cuprate로 무엇을 만들 수 있나 (슬라이드 p.8)
- 생성물에서 β-치환기 하나를 R₂CuLi의 R로 떼고 α–β에 C=C를 다시 넣으면 출발 enone이 나온다.
- → [[유기구리 시약]]의 "역합성 요령", [연습 문제](../practice/L11_Exercises.md) 문제 1

### 3. 1,2-첨가와 1,4-첨가 (슬라이드 p.9–13)
- 1,2는 알릴 알코올, 1,4는 enol을 거쳐 케톤을 준다. 무엇이 정하는가: 받개의 작용기, nucleophile, 반응 조건.
- → [[1,2-첨가와 1,4-첨가]]

#### 3.1 요인 1: 받개의 작용기 (슬라이드 p.10)
- 직접 첨가 비율 acyl chloride > enal > enone > ester > amide. cinnamaldehyde + NaBH₄는 1,2, cyclopentenone + NaBH₄는 1,4 후 1,2.
- → [[1,2-첨가와 1,4-첨가]], [[NaBH4]], [[첨가-제거 반응]](acyl chloride + NH₃)

#### 3.2 요인 2: nucleophile, Grignard vs cuprate (슬라이드 p.11–12)
- hard nucleophile(RMgBr, RLi)은 carbonyl 탄소로(1,2), soft nucleophile(R₂CuLi, RS⁻)은 β-탄소로(1,4).
- → [[하드-소프트 산염기]], [[그리냐르 시약]], [[유기구리 시약]]

#### 3.3 요인 3: kinetic vs thermodynamic product (슬라이드 p.13)
- MVK + NaCN/HCN: 5–10 °C에서 cyanohydrin(1,2, kinetic, 가역), 80 °C에서 NC–CH₂CH₂–COCH₃(1,4, thermodynamic). 1,4는 약한 C=C π를 잃고 C=O를 보존한다.
- → [[1,2-첨가와 1,4-첨가]], [[속도론적 지배와 열역학적 지배]]

### 4. enolate의 conjugate addition: 1,5-dicarbonyl (슬라이드 p.14–17)
- → [[마이클 반응]]

#### 4.1 기본형 (슬라이드 p.14)
- enolate α-탄소가 Michael acceptor의 β-탄소를 쳐서 새 enolate → 양성자화하면 1,5-dicarbonyl. acrylonitrile도 좋은 받개다.
- → [[마이클 반응]]의 "메커니즘", [[엔올과 엔올레이트]]

#### 4.2 경쟁 반응: conjugate addition vs aldol (슬라이드 p.15)
- aldol(1,2)은 가역이라 결국 conjugate addition으로 모인다. 경향은 R = H < alkyl < OR < NR₂. LDA enolate + 아마이드 받개(60%).
- → [[마이클 반응]]의 "선택성", [[알돌 반응]]

#### 4.3 반대이온과 enolate 종류 (슬라이드 p.16)
- Li⁺ + enal은 고리형 TS로 aldol(72%). t-BuOK는 thermodynamic enolate로 4차 탄소를 만든다(53%).
- → [[마이클 반응]], [[속도론적 엔올레이트와 열역학적 엔올레이트]], [[알콕사이드 염기]]

#### 4.4 안정한 enolate: 1,3-dicarbonyl과 nitroalkane (슬라이드 p.17)
- malonate + ethyl crotonate, PhCH₂NO₂ + cyclohexenone(Al₂O₃, 92%), nitromethane의 conjugate addition 후 분자 내 SN2 고리화(65%).
- → [[마이클 반응]], [[말론산 에스터 합성]], [[α-수소의 산도]]

### 5. enamine: 중성이면서 soft한 nucleophile (슬라이드 p.18–20)

#### 5.1 enamine 복습 (슬라이드 p.18)
- ketone + 2차 아민 → enamine, R–X로 α-alkylation 후 가수분해. iminium과 enamine은 양성자 하나 차이.
- → [[엔아민]], [[스토크 엔아민 반응]], [[이미늄 이온]], [[환원성 아미노화]]

#### 5.2 enamine의 conjugate addition (슬라이드 p.19)
- pyrrolidine·morpholine enamine이 받개의 말단 CH₂에 붙고, 후처리 가수분해로 1,5-dicarbonyl(95%, 75%).
- → [[마이클 반응]]의 "enamine" 절, [연습 문제](../practice/L11_Exercises.md) 문제 6

#### 5.3 합성 응용: dopamine antagonist (슬라이드 p.20)
- ester enolate + acrylonitrile(Triton B) → H₂/Pd/C로 아민, lactam 고리화 → alkylation과 환원.
- → [[마이클 반응]]의 "예", [연습 문제](../practice/L11_Exercises.md) 문제 7

### 6. iminium ion 촉매 (슬라이드 p.21)
- 키랄 imidazolidinone이 enal을 iminium으로 바꿔 받개를 활성화하고, 벤질기가 한쪽 면을 가려 87–97% ee.
- → [[이미늄 촉매 공액 첨가]], [[이미늄 이온]]

### 7. β-이탈기가 있는 conjugate addition과 SNAr (슬라이드 p.22–23)

#### 7.1 첨가-제거 메커니즘 (슬라이드 p.22)
- β-F enone + R₂NH: 첨가로 생긴 enolate가 F⁻를 밀어내 β-아미노 enone. C=C가 다시 생긴다.
- → [[첨가-제거 반응]]

#### 7.2 친핵성 방향족 치환(SNAr) (슬라이드 p.22–23)
- 강한 EWG가 붙은 할로벤젠에서 첨가(느림) → σ complex → 제거. 규칙: F >> Cl ~ Br >> I, 강한 EWG(NO₂ 최강), 이탈기는 EWG의 ortho/para.
- → [[친핵성 방향족 치환|SNAr]], [[마이젠하이머 착물]]

### 8. 요약 (슬라이드 p.24)
- 1,4 vs 1,2 / RMgBr + CuCl(촉매) / enolate·enamine → 1,5-dicarbonyl / iminium 촉매 / β-이탈기 → SNAr. 공통 뼈대: Nu가 β-탄소 공격 → enolate → enol → 케톤.
- → [[공액 첨가]]의 "공통 뼈대"

## 반응 요약표

| 반응 | 시약/조건 | 생성물 | 위치선택성 | 비고 |
|---|---|---|---|---|
| 티올 첨가 ([[공액 첨가]]) | mesityl oxide + PhSH, 25 °C | (CH3)2C(SPh)CH2COCH3 (94%) | 1,4 | soft (p.4) |
| 시안화 첨가 ([[공액 첨가]]) | chalcone + ⁻CN, EtOH, HOAc | PhCH(CN)CH2COPh (95%) | 1,4 | 새 입체중심, 라세미(보충) (p.4) |
| 아민 첨가 ([[공액 첨가]]) | mesityl oxide + MeNH2, H2O | (CH3)2C(NHMe)CH2COCH3 (75%) | 1,4 | zwitterion 경유 (p.5) |
| cuprate 제조 ([[유기구리 시약]]) | CuBr + 2 RLi, Et2O, −78 °C | R2CuLi + LiBr | – | 즉시 사용 (p.6) |
| Cu 촉매 Grignard ([[유기구리 시약]]) | isophorone + MeMgBr, CuCl 0.01 eq | 3,3,5,5-tetramethylcyclohexanone (83%) | 1,4 | CuCl 없으면 1,2 (p.6–7) |
| Grignard/RLi ([[그리냐르 시약]]) | 2-cyclohexenone + CH3MgBr 또는 CH3Li; H3O⁺ | 1-methyl-2-cyclohexen-1-ol (95%) | 1,2 | hard (p.11) |
| cuprate ([[유기구리 시약]]) | 2-cyclohexenone + (CH3)2CuLi; H3O⁺ | 3-methylcyclohexanone (97%) | 1,4 | soft (p.11) |
| acyl chloride + NH3 ([[첨가-제거 반응]]) | CH2=CHCOCl + NH3 | CH2=CHCONH2 | 1,2(아실 치환) | (p.10) |
| acrylate + NH3 ([[공액 첨가]]) | CH2=CHCO2Me + NH3 | H2NCH2CH2CO2Me | 1,4 | (p.10) |
| enal 환원 ([[NaBH4]]) | cinnamaldehyde + NaBH4, EtOH | cinnamyl alcohol (97%) | 1,2 | (p.10) |
| 고리 enone 환원 ([[NaBH4]]) | cyclopentenone + NaBH4, EtOH | cyclopentanol (99%) | 1,4 후 1,2 | (p.10) |
| HCN 첨가, 저온 ([[1,2-첨가와 1,4-첨가]]) | MVK + NaCN, HCN, 5–10 °C | cyanohydrin | 1,2 | kinetic, 가역 (p.13) |
| HCN 첨가, 고온 ([[1,2-첨가와 1,4-첨가]]) | MVK + NaCN, HCN, 80 °C | NCCH2CH2COCH3 | 1,4 | thermodynamic (p.13) |
| enolate Michael ([[마이클 반응]]) | cyclohexanone + LDA; (E)-CH3CH=CHCONMe2 | 1,5-ketoamide (60%) | 1,4 | 아마이드 받개 (p.15) |
| Li enolate + enal ([[알돌 반응]]) | ethyl isobutyrate + LDA, −78 °C; (CH3)2C=CHCHO | β-hydroxy ester (72%) | 1,2(aldol) | Li⁺ 배위 (p.16) |
| thermodynamic enolate Michael ([[마이클 반응]]) | 2-methylcyclopentanone + methyl acrylate, t-BuOK | 4차 탄소 생성물 (53%) | 1,4 | (p.16) |
| malonate Michael ([[마이클 반응]]) | CH2(CO2Et)2 + ethyl crotonate, NaOEt | (EtO2C)2CHCH(CH3)CH2CO2Et | 1,4 | 안정한 enolate (p.17) |
| nitroalkane Michael ([[마이클 반응]]) | PhCH2NO2 + 2-cyclohexenone, Al2O3 | 3-(CH(Ph)NO2)cyclohexanone (92%) | 1,4 | (p.17) |
| Michael–분자 내 alkylation ([[마이클 반응]]) | I(CH2)4CH=CHCO2Me + CH3NO2, Cs2CO3, DMF | methyl 2-(2-nitrocyclohexyl)acetate (65%) | 1,4 후 SN2 | (p.17) |
| enamine alkylation ([[스토크 엔아민 반응]]) | cyclohexanone + pyrrolidine; R–X; H3O⁺ | 2-R-cyclohexanone | α | (p.18) |
| enamine Michael ([[마이클 반응]]) | pyrrolidine enamine + CH2=C(SMe)CO2Me; H2O | 1,5-dicarbonyl (95%) | 1,4 | (p.19) |
| enamine Michael ([[마이클 반응]]) | morpholine enamine + CH2=C(SO2Ph)COCH3, SiO2; H2O | 1,5-diketone (75%) | 1,4 | (p.19) |
| iminium 촉매 ([[이미늄 촉매 공액 첨가]]) | enal + pyrrole, imidazolidinone 20 mol% | β-pyrrolyl aldehyde (68–90%) | 1,4 | 87–97% ee, (R) (p.21) |
| β-이탈기 치환 ([[첨가-제거 반응]]) | 2-F-cyclohexenyl methyl ketone + R2NH | β-아미노 enone | β 치환 | (p.22) |
| SNAr ([[친핵성 방향족 치환]]) | o-F-acetophenone + R2NH | o-NR2-acetophenone | ipso | ortho EWG (p.23) |
| SNAr ([[친핵성 방향족 치환]]) | p-Cl-nitrobenzene + HO⁻ | p-nitrophenol | ipso | para EWG (p.23) |

## 연습 문제
→ [L11 연습 문제](../practice/L11_Exercises.md)

## 출처
- 슬라이드: L11 (PDF p.3–24)
