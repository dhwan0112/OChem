# L17. 전자고리화 반응 (Electrocyclic reactions)

<!-- wiki-links:start -->

> **관련 위키 문서** ([위키 대문](../wiki/위키%20대문.md))
> - 반응: [Cope rearrangement](../wiki/반응/코프%20자리옮김.md), [electrocyclic reaction](../wiki/반응/전자고리화%20반응.md), [Nazarov cyclization](../wiki/반응/나자로프%20고리화.md), [photochemical \[2+2\] cycloaddition](../wiki/반응/광화학%202+2%20고리화%20첨가.md)
> - 개념: [1,3-dipole](../wiki/개념/1,3-쌍극자.md), [allyl cation](../wiki/개념/알릴%20양이온.md), [conrotatory and disrotatory](../wiki/개념/콘로테이션과%20디스로테이션.md), [pericyclic reaction](../wiki/개념/페리고리%20반응.md), [suprafacial and antarafacial](../wiki/개념/초면과%20대면.md), [Woodward–Hoffmann rules](../wiki/개념/우드워드-호프만%20규칙.md)

<!-- wiki-links:end -->

> 이 강의 노트는 **뼈대**다. 강의 순서와 슬라이드 위치만 정리했고, 설명은 링크된 개념 문서에 있다.

> 강의 흐름대로 길게 읽고 싶으면 **[통독본](통독/L17_Electrocyclic_Reactions.md)**(재구성 직전의 전체 노트, 소절마다 개념 문서 링크 포함)을 본다.

> 이 노트는 슬라이드 공개 전에 Clayden 2판 35장과 Wade 8판으로 만든 **예습판**이다. 아래 쪽수는 슬라이드가 아니라 Clayden 인쇄 쪽수다. 강의 슬라이드가 나오면 슬라이드 기준으로 다시 정리한다. 슬라이드와 다르면 슬라이드를 따른다.

CM3121 Advanced Organic Chemistry (10/21 강의 예습)

## 개요

pericyclic reaction 세 갈래 가운데 마지막인 electrocyclic reaction을 다룬다. cycloaddition([L13](L13_Cycloaddition_Part1.md)–[L15](L15_Cycloaddition_Part3.md))이 $\sigma$ 결합 둘을, sigmatropic rearrangement([L16](L16_Sigmatropic_Rearrangements.md))가 $\sigma$ 결합 하나를 옮기는 것과 달리, 한 conjugated $\pi$계의 양 끝을 $\sigma$ 결합 하나로 잇거나 끊는다. 먼저 방향(열역학)과 Woodward–Hoffmann을 가르고, $4\pi$는 antarafacial, $6\pi$는 suprafacial이라는 결론이 conrotation/disrotation이라는 입체화학으로 바뀌는 과정을 본다. HOMO 위상으로 같은 답을 확인하고(보충), 빛을 쬐면 뒤집힌다는 판정표를 정리한 뒤, endiandric acid, Nazarov cyclization과 dienyl anion, 작은 고리 열림, periplanone B 합성으로 응용한다. (출처: Clayden p.922–923)

## 강의 흐름

### 1. 전자고리화 반응이란 무엇인가 (Clayden p.922–923)
- $\Delta\sigma$ = ±1, 한 $\pi$계의 양 끝을 잇거나 끊는다. 방향은 열역학이 정한다(hexatriene은 닫히고 cyclobutene은 열린다).
- → [electrocyclic reaction](../wiki/반응/전자고리화%20반응.md)

### 2. Woodward–Hoffmann 규칙으로 판정하기 (Clayden p.923–924)
- $6\pi$는 $\pi6\mathrm{s}$, $4\pi$는 $\pi4\mathrm{a}$로 그리면 허용 → 모든 electrocyclic reaction은 허용되고, 차이는 입체화학에 나타난다.
- → [electrocyclic reaction](../wiki/반응/전자고리화%20반응.md), [Woodward–Hoffmann rules](../wiki/개념/우드워드-호프만%20규칙.md), [conrotatory and disrotatory](../wiki/개념/콘로테이션과%20디스로테이션.md)

### 3. conrotatory과 disrotatory (Clayden p.924–925)
- $\begin{aligned} & \text{열적}\ 6\pi\ (\text{octatriene}) \\ & \longrightarrow \text{cis-dimethyl)는 disrotatory},\ \text{열적}\ 4\pi\ (\text{cis-dimethylcyclobutene}) \\ & \longrightarrow (\mathit{E}\ ,\ \mathit{Z})\text{-diene)는}\ \text{conrotatory} \end{aligned}$. 회전 방향(시계/반시계)으로 센다.
- → [conrotatory and disrotatory](../wiki/개념/콘로테이션과%20디스로테이션.md)

### 4. HOMO 대칭으로 다시 보기 (보충: Wade p.671–672, p.694–698)
- HOMO 양 끝 위상이 반대면 con, 같으면 dis. 빛을 받으면 HOMO*가 한 단계 위로 바뀌어 뒤집힌다.
- → [conrotatory and disrotatory](../wiki/개념/콘로테이션과%20디스로테이션.md), [frontier molecular orbital](../wiki/개념/프런티어%20분자%20오비탈.md)

### 5. 광화학 전자고리화 반응: 규칙이 뒤집힌다 (Clayden p.921–922, p.926–927; Wade p.693)
- 판정표 "4n·열·con". 비타민 D: ergosterol의 $6\pi$ 고리 열림은 광화학 conrotation으로만 가능하고, 다음 단계는 열적 [1,7]H.
- → [conrotatory and disrotatory](../wiki/개념/콘로테이션과%20디스로테이션.md), [electrocyclic reaction](../wiki/반응/전자고리화%20반응.md), [1,5-hydrogen shift](../wiki/반응/1,5-수소%20이동.md)

### 6. 자연 속 전자고리화 반응: endiandric acid (Clayden p.925–926)
- $8\pi$ con → $6\pi$ dis → 분자 내 Diels–Alder가 효소 없이 연달아 일어나 라세미 천연물이 된다.
- → [electrocyclic reaction](../wiki/반응/전자고리화%20반응.md), [Diels–Alder reaction](../wiki/반응/딜스-알더%20반응.md)

### 7. cation과 anion의 전자고리화 반응 (Clayden p.927–928)
- Nazarov: pentadienyl cation($4\pi$)은 열적 con, 빛 dis. cyclooctadienyl anion($6\pi$)은 dis로 cis-bicyclo[3.3.0]; 기하가 불가능하면 허용 반응도 막힌다.
- → [Nazarov cyclization](../wiki/반응/나자로프%20고리화.md), [electrocyclic reaction](../wiki/반응/전자고리화%20반응.md)

### 8. 작은 고리는 전자고리화로 열린다 (Clayden p.928–929)
- $\text{cyclopropyl cation} \longrightarrow \text{allyl}\ \text{cation}(2\pi\ \text{dis 고리 열림})$. ester 치환 aziridine → azomethine ylide($4\pi$ con), [3+2]로 포획해 cis → 2,5-trans 확인.
- → [electrocyclic reaction](../wiki/반응/전자고리화%20반응.md), [allyl cation](../wiki/개념/알릴%20양이온.md), [1,3-dipolar cycloaddition](../wiki/반응/1,3-쌍극자%20고리화%20첨가.md)

### 9. 페리고리 반응만으로 만든 페로몬: 페리플라논 B (Clayden p.929–930)
- 광화학 [2+2] → vinyl Grignard → anionic oxy-Cope → $4\pi$ 고리 열림. 반대쪽 끝에 치환기가 없어 con/dis를 구별할 수 없다.
- → [electrocyclic reaction](../wiki/반응/전자고리화%20반응.md), [photochemical \[2+2\] cycloaddition](../wiki/반응/광화학%202+2%20고리화%20첨가.md), [Cope rearrangement](../wiki/반응/코프%20자리옮김.md)

### 10. 세 갈래 총정리 (Clayden p.922–925, p.927)
- cycloaddition·sigmatropic·electrocyclic의 $\Delta\sigma$, 판정 도구, 열적 허용 모양, 빛의 효과, 입체화학의 열쇠 비교표.
- → [electrocyclic reaction](../wiki/반응/전자고리화%20반응.md), [pericyclic reaction](../wiki/개념/페리고리%20반응.md)

## 반응 요약표

| 반응 | 출발물 → 생성물 | 조건 | $\pi$ 전자 | 회전 | 문서 |
|---|---|---|---|---|---|
| hexatriene 고리 닫힘 | $\longrightarrow \text{cyclohexa-1,3-diene}$ | 500 °C | 6 | dis | [electrocyclic reaction](../wiki/반응/전자고리화%20반응.md) |
| cyclobutene 고리 열림 | $\longrightarrow \text{buta-1,3-diene}$ | 200 °C | 4 | con | [electrocyclic reaction](../wiki/반응/전자고리화%20반응.md) |
| octatriene | $(2\ \mathit{E}\ \mathrm{,4}\ \mathit{Z}\ \mathrm{,6}\ \mathit{E})\text{-octatriene} \longrightarrow \text{5,6-dimethylcyclohexadiene}$ | 열 / $h\nu$ | 6 | dis(cis) / con(trans) | [conrotatory and disrotatory](../wiki/개념/콘로테이션과%20디스로테이션.md) |
| dimethylcyclobutene 열림 | $\text{cis-3,4-dimethylcyclobutene} \longrightarrow (\mathit{E}\ ,\ \mathit{Z})\text{-hexa-2,4-diene}$ | 가열 | 4 | con | [conrotatory and disrotatory](../wiki/개념/콘로테이션과%20디스로테이션.md) |
| 비타민 D (1단계) | ergosterol → 프로비타민 D2 | 햇빛 | 6 | con | [electrocyclic reaction](../wiki/반응/전자고리화%20반응.md) |
| endiandric acid | polyene → D/E → A | 열 | 8 → 6 | con → dis | [electrocyclic reaction](../wiki/반응/전자고리화%20반응.md) |
| Nazarov | $\text{divinyl ketone} \longrightarrow \text{cyclopentenone}$ | H3PO4, AcOH / $h\nu$ | 4 | con(trans) / dis(cis) | [Nazarov cyclization](../wiki/반응/나자로프%20고리화.md) |
| dienyl anion | $\text{cyclooctadiene} \longrightarrow \text{cis-bicyclo[3.3.0]octene}$ | BuLi; 0 °C; H⁺ | 6 | dis | [electrocyclic reaction](../wiki/반응/전자고리화%20반응.md) |
| cyclopropyl cation | $\text{cyclopropyl chloride} \longrightarrow \text{allyl acetate}$ | KOAc, AcOH | 2 | dis(열림) | [electrocyclic reaction](../wiki/반응/전자고리화%20반응.md) |
| aziridine 열림 + [3+2] | aziridine → azomethine ylide → dihydropyrrole | 가열, dipolarophile | 4 | con | [electrocyclic reaction](../wiki/반응/전자고리화%20반응.md) |
| periplanone B 고리 열림 | $\text{cyclobutene 융합 10원 고리} \longrightarrow \text{12원 고리 diene}$ | 175 °C; $h\nu$ | 4 | con(구별 불가) | [electrocyclic reaction](../wiki/반응/전자고리화%20반응.md) |

(출처: Clayden p.922–930)

## 연습 문제
→ [L17 연습 문제](../practice/L17_Exercises.md)

## 출처
- 슬라이드: L17 (아직 공개 전. 이 뼈대는 Clayden 2판 35장 p.922–930, Wade 8판 p.671–698 기반)
