# L13. 고리화 첨가 반응 1부: Diels–Alder 반응 (Cycloadditions, Part 1)

<!-- wiki-links:start -->

> **관련 위키 문서** ([위키 대문](../wiki/위키%20대문.md))
> - 반응: [1,3-dipolar cycloaddition](../wiki/반응/1,3-쌍극자%20고리화%20첨가.md), [Diels–Alder reaction](../wiki/반응/딜스-알더%20반응.md), [Michael reaction](../wiki/반응/마이클%20반응.md), [retro-Diels–Alder reaction](../wiki/반응/역%20딜스-알더%20반응.md), [Robinson annulation](../wiki/반응/로빈슨%20고리%20형성.md)
> - 개념: [aromaticity](../wiki/개념/방향족성.md), [Diels–Alder regioselectivity](../wiki/개념/딜스-알더%20위치선택성.md), [electrophile and nucleophile](../wiki/개념/친전자체와%20친핵체.md), [endo rule](../wiki/개념/endo%20규칙.md), [frontier molecular orbital](../wiki/개념/프런티어%20분자%20오비탈.md), [kinetic vs thermodynamic control](../wiki/개념/속도론적%20지배와%20열역학적%20지배.md), [pericyclic reaction](../wiki/개념/페리고리%20반응.md), [s-cis conformation](../wiki/개념/s-cis%20형태.md), [stereospecificity and stereoselectivity](../wiki/개념/입체특이성과%20입체선택성.md), [suprafacial and antarafacial](../wiki/개념/초면과%20대면.md), [Woodward–Hoffmann rules](../wiki/개념/우드워드-호프만%20규칙.md)

<!-- wiki-links:end -->

> 이 강의 노트는 **뼈대**다. 강의 순서와 슬라이드 위치만 정리했고, 설명은 링크된 개념 문서에 있다.

> 강의 흐름대로 길게 읽고 싶으면 **[통독본](통독/L13_Cycloaddition_Part1.md)**(재구성 직전의 전체 노트, 소절마다 개념 문서 링크 포함)을 본다.

CM3121 Advanced Organic Chemistry, Dr. Zhu Ye

## 개요

L13은 polar 반응과 전혀 다른 방식으로 결합이 생기는 [pericyclic reaction](../wiki/개념/페리고리%20반응.md)을 처음 다루고, 그 대표인 [Diels–Alder reaction](../wiki/반응/딜스-알더%20반응.md)을 소개한다. 먼저 반응 메커니즘을 polar·radical·pericyclic으로 나누고, polar 방식으로 6원 고리를 만드는 다단계 경로와 DA의 한 단계 반응을 대비한다. 이어 "무엇이 반응하나 → 어떻게 반응하나 → 무엇이 빠르게 하나 → 입체화학은 어떻게 정해지나 → 왜 그런가" 순서로 정의, 협동 메커니즘과 방향족성 TS, dienophile·diene의 전자 효과와 s-cis 조건, stereospecificity와 endo 규칙을 본다. 마지막에 이 모든 것을 FMO와 Woodward–Hoffmann 규칙으로 설명한다. Regioselectivity는 L14에서 다룬다.

## 강의 흐름

### 1. 반응은 어떻게 분류되나: 극성, radical, 그리고 pericyclic (슬라이드 p.3–5)
- 결합이 바뀌는 방식은 polar, radical, pericyclic 세 가지다. pericyclic 반응은 고리형 TS, intermediate 없음, concerted, stereospecific/stereoselective가 특징이다. chorismate mutase(Claisen rearrangement) 예.
- pericyclic은 cycloaddition, electrocyclic, sigmatropic으로 나뉘고, L13은 Diels–Alder만 다룬다.
- → [pericyclic reaction](../wiki/개념/페리고리%20반응.md)

### 2. 극성 반응으로도 6원자 고리는 만들 수 있지 않나? (슬라이드 p.6)
- Robinson annulation(Michael + aldol)과 nitro-Michael + 분자 내 SN2는 여러 단계와 이온성 intermediate를 거친다. DA는 한 단계로 끝낸다.
- → [Diels–Alder reaction](../wiki/반응/딜스-알더%20반응.md), [Robinson annulation](../wiki/반응/로빈슨%20고리%20형성.md), [Michael reaction](../wiki/반응/마이클%20반응.md)

### 3. Diels–Alder 반응이란 무엇인가 (슬라이드 p.7–9)
- $\text{conjugated diene} + \text{alkene(dienophile)} \longrightarrow \text{cyclohexene}$. butadiene + ethylene은 165 °C, 900 atm이 필요하다. C1–C6, C4–C5 새 $\sigma$ 결합과 C2=C3 새 $\pi$ 결합.
- cyclic diene은 bridged bicyclic(norbornene)을 준다. Diels–Alderase 효소도 있다.
- → [Diels–Alder reaction](../wiki/반응/딜스-알더%20반응.md)

### 4. 어떻게 반응하나: 메커니즘과 transition state (슬라이드 p.10–13)
- 단일 기본 단계의 concerted 반응. 열역학: $\pi$ 두 개 → $\sigma$ 두 개. 속도론: $6\pi$ 방향족성 TS(새 C···C 약 2.2 Å).
- 두 반응물이 suprafacial–suprafacial로 포개지는 [$\pi4\mathrm{s}$ + $\pi2\mathrm{s}$]다.
- → [Diels–Alder reaction](../wiki/반응/딜스-알더%20반응.md), [suprafacial and antarafacial](../wiki/개념/초면과%20대면.md), [aromaticity](../wiki/개념/방향족성.md)

### 5. 무엇이 반응을 빠르게 하나 (슬라이드 p.14–18)
- $\begin{aligned} & 5\text{–}1\ \text{dienophile은}\ \mathrm{EWG}\text{가}\ \text{많을수록}\ \text{빠르다}(\text{ethylene}\ 900\  \\ & \text{atm}) \\ & \longrightarrow \text{acrolein}\ 150\,{}^\circ\mathrm{C} \\ & \longrightarrow \mathrm{CH_2{=}C(CO_2Me)_2\,25^\circ C)(p.14)} \end{aligned}$. → [Diels–Alder reaction](../wiki/반응/딜스-알더%20반응.md)
- 5-2 diene은 EDG가 있을수록 빠르고, s-cis 형태여야 한다(butadiene 약 1%)(p.15). → [s-cis conformation](../wiki/개념/s-cis%20형태.md), [frontier molecular orbital](../wiki/개념/프런티어%20분자%20오비탈.md)
- 5-3 s-cis 고정 diene(cyclopentadiene 등)은 매우 빠르고, s-trans 고정 diene은 반응하지 않는다(p.16). p.17 연습 문제는 연습 문제 1, 2. → [s-cis conformation](../wiki/개념/s-cis%20형태.md)
- 5-4 cyclopentadiene은 상온에서 이량화하고, 가열·증류(retro-DA)로 단량체를 회수한다. hexachlorocyclopentadiene 부가물은 난연제(p.18). → [retro-Diels–Alder reaction](../wiki/반응/역%20딜스-알더%20반응.md)

### 6. 입체화학: 반응물의 모양이 생성물에 어떻게 새겨지나 (슬라이드 p.19–24)
- 6-1 maleate(cis) → cis, fumarate(trans) → trans: stereospecificity(p.19). → [Diels–Alder reaction](../wiki/반응/딜스-알더%20반응.md), [stereospecificity and stereoselectivity](../wiki/개념/입체특이성과%20입체선택성.md)
- 6-2 diene의 "in" 둘·"out" 둘은 1,4-cis, in + out은 trans. alkyne dienophile은 cyclohexa-1,4-diene(p.20). → [Diels–Alder reaction](../wiki/반응/딜스-알더%20반응.md), [s-cis conformation](../wiki/개념/s-cis%20형태.md)
- 6-3 endo 규칙: cyclopentadiene + maleic anhydride는 endo만 secondary orbital overlap. endo는 kinetic 생성물이다. p.23–24 연습은 all-cis 답(연습 문제 3). → [endo rule](../wiki/개념/endo%20규칙.md)

### 7. 왜 그런가: 분자 오비탈로 다시 보기 (슬라이드 p.25–31)
- 7-1 ethylene $\pi$/$\pi^{*}$, butadiene $\psi_{1}$–$\psi_{4}$(HOMO $\psi_{2}$, LUMO $\psi_{3}$)(p.25–26). → [frontier molecular orbital](../wiki/개념/프런티어%20분자%20오비탈.md)
- 7-2 diene HOMO–dienophile LUMO 간격이 작을수록 빠르다(EDG는 HOMO↑, EWG는 LUMO↓)(p.27). → [frontier molecular orbital](../wiki/개념/프런티어%20분자%20오비탈.md)
- 7-3 양 끝 로브가 같은 면에서 만나야 해서 stereospecific하다(p.28). → [suprafacial and antarafacial](../wiki/개념/초면과%20대면.md)
- 7-4 endo-dicyclopentadiene의 secondary orbital overlap(p.29). → [endo rule](../wiki/개념/endo%20규칙.md)
- 7-5 butadiene 두 분자는 [4+2]만 하고 [4+4]는 열적으로 안 된다(p.30). 정리 슬라이드(p.31). → [frontier molecular orbital](../wiki/개념/프런티어%20분자%20오비탈.md), [Diels–Alder reaction](../wiki/반응/딜스-알더%20반응.md)

### 8. Woodward–Hoffmann 규칙: 허용과 금지를 가르는 계산법 (슬라이드 p.32–36)
- 열적 pericyclic 반응은 (4q+2)s + (4r)a 성분 수가 홀수여야 허용된다. DA [$\pi4\mathrm{s}$ + $\pi2\mathrm{s}$]는 합 1로 허용. "허용"은 가능하다는 뜻일 뿐이다.
- p.36 연습([4+2] 허용, [4+4] 금지)은 연습 문제 7.
- → [Woodward–Hoffmann rules](../wiki/개념/우드워드-호프만%20규칙.md), [suprafacial and antarafacial](../wiki/개념/초면과%20대면.md)

### 9. 보충: regioselectivity("ortho/para" 규칙)
- 슬라이드에는 없다. $\begin{aligned} & \text{1-치환 diene} \\ & \longrightarrow \text{"ortho"},\ \text{2-치환 diene} \\ & \longrightarrow \text{"para"} \end{aligned}$(L14에서 다룸).
- → [Diels–Alder regioselectivity](../wiki/개념/딜스-알더%20위치선택성.md)

## 반응 요약표

| 반응 | 시약/조건 | 생성물 | 입체화학 | 비고 |
|---|---|---|---|---|
| butadiene + ethylene ([DA](../wiki/반응/딜스-알더%20반응.md)) | 165 °C, 17 h, 900 atm | cyclohexene (78%) | – | 활성화되지 않은 dienophile (p.7, 14) |
| 2,3-dimethylbutadiene + acrolein | 열 | 3,4-dimethylcyclohex-3-ene-1-carbaldehyde | 라셈 | (p.8) |
| cyclopentadiene + nitroethylene | 열 | 5-nitronorbornene | endo/exo 가능 | bridged bicyclic (p.8) |
| butadiene + acrolein | 150 °C, 0.5 h | cyclohex-3-ene-1-carbaldehyde | 라셈 | EWG 1개 (p.14) |
| butadiene + CH2=C(CO2Me)2 | 25 °C, 24 h | dimethyl cyclohex-3-ene-1,1-dicarboxylate (80%) | 비카이랄 | EWG 2개 (p.14) |
| butadiene + methyl acrylate | 열 | methyl cyclohex-3-ene-1-carboxylate | 라셈 | [s-cis](../wiki/개념/s-cis%20형태.md)에서만 (p.15) |
| cyclopentadiene + acrolein | 20 °C, 68 h | 5-norbornene-2-carbaldehyde (92%) | endo로 그려짐 | s-cis 고정 (p.16) |
| cyclopentadiene 2분자 | 상온 | endo-dicyclopentadiene | endo | 가열·증류하면 [retro-DA](../wiki/반응/역%20딜스-알더%20반응.md) (p.18, 29) |
| hexachlorocyclopentadiene + maleic anhydride | 열 | 육염소 norbornene 무수물 | cis-무수물 | 난연제 (p.18) |
| butadiene + maleic anhydride | 열 | cis-1,2,3,6-tetrahydrophthalic anhydride | cis | supra–supra (p.12) |
| butadiene + dimethyl maleate / fumarate | 열 | cis- / trans-cyclohex-4-ene-1,2-diester | syn / anti(라셈) | stereospecific (p.19, 28) |
| (E,E)-1,4-diphenylbutadiene + DMAD | 열 | cis-3,6-diphenylcyclohexa-1,4-diene-1,2-diester | 두 Ph cis | out/out (p.20) |
| (E,E)- / (E,Z)-hexa-2,4-diene + DMAD | 열 | 3,6-dimethylcyclohexa-1,4-diene-1,2-diester | syn / anti | (p.20, 28) |
| cyclopentadiene + maleic anhydride | 열 | endo 부가물 | endo만 | [endo rule](../wiki/개념/endo%20규칙.md) (p.21) |
| (E,E)-hexa-2,4-diene + acrolein | 열 | all-cis 2,5-dimethylcyclohex-3-ene-1-carbaldehyde | endo | (p.23–24) |
| butadiene 2분자 | 가열 | 4-vinylcyclohexene ([4+4] 생성물 없음) | – | [Woodward–Hoffmann rules](../wiki/개념/우드워드-호프만%20규칙.md) (p.30, 36) |
| (비교) 2-methylcyclohexane-1,3-dione + MVK | 10% NaOH 후 piperidine/가열, 또는 EtONa/가열 | 이중 고리 enone | 4차 탄소 | [Robinson annulation](../wiki/반응/로빈슨%20고리%20형성.md) (p.6) |
| (비교) I(CH2)4CH=CHCO2Me + CH3NO2 | Cs2CO3, DMF, 20 °C | 2-(2-nitrocyclohexyl)acetic acid methyl ester (65%) | – | nitro-Michael → SN2 (p.6) |

## 연습 문제
→ [L13 연습 문제](../practice/L13_Exercises.md)

## 출처
- 슬라이드: L13 (PDF p.1–36)
