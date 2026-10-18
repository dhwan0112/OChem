# L14. 고리화 첨가 반응 2부 (Cycloadditions, Part 2)

<!-- wiki-links:start -->

> **관련 위키 문서** ([위키 대문](../wiki/위키%20대문.md))
> - 반응: [\[4+3\] cycloaddition](../wiki/반응/4+3%20고리화%20첨가.md), [\[6+4\] cycloaddition](../wiki/반응/6+4%20고리화%20첨가.md), [Diels–Alder reaction](../wiki/반응/딜스-알더%20반응.md), [inverse electron demand Diels–Alder](../wiki/반응/역전자%20요구%20딜스-알더%20반응.md), [photochemical \[2+2\] cycloaddition](../wiki/반응/광화학%202+2%20고리화%20첨가.md)
> - 시약: [Lewis acid catalyst](../wiki/시약/루이스%20산%20촉매.md), [NBS](../wiki/시약/NBS.md)
> - 개념: [allyl cation](../wiki/개념/알릴%20양이온.md), [aromaticity](../wiki/개념/방향족성.md), [cubane](../wiki/개념/큐베인.md), [Diels–Alder regioselectivity](../wiki/개념/딜스-알더%20위치선택성.md), [endo rule](../wiki/개념/endo%20규칙.md), [frontier molecular orbital](../wiki/개념/프런티어%20분자%20오비탈.md), [pericyclic reaction](../wiki/개념/페리고리%20반응.md), [stereospecificity and stereoselectivity](../wiki/개념/입체특이성과%20입체선택성.md), [substituent effect](../wiki/개념/치환기%20효과.md), [suprafacial and antarafacial](../wiki/개념/초면과%20대면.md), [Test 2 reaction checklist](../wiki/개념/Test%202%20반응%20판정과%20답안%20검산.md), [Woodward–Hoffmann rules](../wiki/개념/우드워드-호프만%20규칙.md)

<!-- wiki-links:end -->


> 이 강의 노트는 **뼈대**다. 강의 순서와 슬라이드 위치만 정리했고, 설명은 링크된 개념 문서에 있다.

> 강의 흐름대로 길게 읽고 싶으면 **[통독본](통독/L14_Cycloaddition_Part2.md)**(재구성 직전의 전체 노트, 소절마다 개념 문서 링크 포함)을 본다.

## 개요

L13에서 Diels–Alder 반응이 concerted, stereospecific, endo 선호라는 것을 봤다. L14는 남은 질문, 즉 왜 [4+4]나 열적 [2+2]는 안 되는지, 왜 X-diene + Z-dienophile이 빠른지, 비대칭 성분끼리는 어느 위치 이성질체가 나오는지를 [Woodward–Hoffmann rules](../wiki/개념/우드워드-호프만%20규칙.md)과 [FMO](../wiki/개념/프런티어%20분자%20오비탈.md)로 답한다. 이어 regioselectivity와 endo stereoselectivity를 합쳐 생성물을 예측하고 Lewis acid 촉매를 본다. 같은 논리를 6원 고리 밖으로 넓혀 [6+4], [4+3], 광화학 [2+2]를 다루고, [4+2]와 [2+2]를 모두 쓰는 cubane 합성으로 마무리한다. 핵심 질문은 "허용되는가, 얼마나 빠른가, 어느 방향인가"이다. (출처: L14 p.1–2)

## 강의 흐름

### 1. DA 반응의 최전선 오비탈 다시 보기 (슬라이드 p.3)
- 주된 상호작용은 HOMO(diene)–LUMO(dienophile)이고, 양 끝 위상이 맞는다(butadiene + maleic anhydride).
- → [frontier molecular orbital](../wiki/개념/프런티어%20분자%20오비탈.md)

### 2. Woodward–Hoffmann 규칙 (슬라이드 p.4–7)
- (4q+2)s + (4r)a 성분 수가 홀수면 열적 허용. suprafacial/antarafacial 정의, "허용 ≠ 반드시 일어남".
- 2.1 DA [$\pi4\mathrm{s}$ + $\pi2\mathrm{s}$]: 합 1, 허용(p.6). 2.2 [4+4] [$\pi4\mathrm{s}$ + $\pi4\mathrm{s}$]: 합 0, 열적 금지(p.7).
- → [Woodward–Hoffmann rules](../wiki/개념/우드워드-호프만%20규칙.md), [suprafacial and antarafacial](../wiki/개념/초면과%20대면.md)

### 3. 치환기의 분류: C, Z, X형 (슬라이드 p.8–9)
- C(conjugation): HOMO↑ LUMO↓, Z(EWG): LUMO 크게↓, X(EDG): HOMO 크게↑.
- → [frontier molecular orbital](../wiki/개념/프런티어%20분자%20오비탈.md), [substituent effect](../wiki/개념/치환기%20효과.md)

### 4. 반응 속도: 왜 X-diene + Z-dienophile이 빠른가 (슬라이드 p.10)
- (a) butadiene + ethylene < (b) + Z-dienophile < (c) X-diene + Z-dienophile. normal electron demand.
- → [frontier molecular orbital](../wiki/개념/프런티어%20분자%20오비탈.md), [inverse electron demand Diels–Alder](../wiki/반응/역전자%20요구%20딜스-알더%20반응.md)

### 5. DA 반응의 regioselectivity (슬라이드 p.11–15)
- dienophile의 electrophilic 위치($\beta$-탄소)가 diene의 nucleophilic 위치와 결합한다.
- 5.1 C2-치환 diene → "pseudo para"(p.12). 5.2 C1-치환 diene → "pseudo ortho", concerted but unsynchronous TS(p.13). 5.3 ortho/para 규칙(p.14). 5.4 실제 선택성 9:1, 6.8:1, 6:1, 10:1(p.15).
- → [Diels–Alder regioselectivity](../wiki/개념/딜스-알더%20위치선택성.md)

### 6. regioselectivity과 stereoselectivity의 결합 (슬라이드 p.16–19)
- (E)-1-methoxybutadiene + acrolein: $\begin{aligned} & \text{"ortho"} + \text{endo}(\mathrm{"out"}\ \text{치환기와}\ \mathrm{EWG}\ \text{cis}) \\ & \longrightarrow \text{cis-2-methoxycyclohex-3-ene-1-carbaldehyde} \end{aligned}$.
- 6.1 (E)-1-acetoxybutadiene + (E)-crotonaldehyde: 3단계(stereospecificity)까지(연습 문제 3).
- → [Diels–Alder regioselectivity](../wiki/개념/딜스-알더%20위치선택성.md), [endo rule](../wiki/개념/endo%20규칙.md)

### 7. DA 반응의 Lewis acid 촉매 (슬라이드 p.20)
- SnCl4 배위로 dienophile LUMO↓(속도), 편극↑(regioselectivity). isoprene + MVK para:meta 71:29 → 93:7.
- → [Diels–Alder regioselectivity](../wiki/개념/딜스-알더%20위치선택성.md), [Lewis acid catalyst](../wiki/시약/루이스%20산%20촉매.md)

### 8. 6원환을 넘어서: [6+4] cycloaddition (슬라이드 p.21)
- supra–supra 열적 cycloaddition은 총 전자 수 4n+2일 때 허용. $\begin{aligned} & \text{tropone} + \text{cyclopentadiene}(\text{"endo" 표기는 문헌과 다름},\  \\ & \text{해당 문서 각주}),\ \text{fulvene} + \text{1-NEt2-diene} \\ & \longrightarrow \text{azulene 골격} \end{aligned}$.
- → [6+4 cycloaddition](../wiki/반응/6+4%20고리화%20첨가.md)

### 9. [4+3] cycloaddition (슬라이드 p.22–23)
- $\begin{aligned} & \text{1,3-dibromoacetone} + \mathrm{Zn} \\ & \longrightarrow \text{oxyallyl}\ \text{cation}(\text{3원자}\ 2\pi) + \text{diene} \\ & \longrightarrow \text{cyclohept-4-enone} \end{aligned}$. 6전자라 허용.
- → [4+3 cycloaddition](../wiki/반응/4+3%20고리화%20첨가.md), [allyl cation](../wiki/개념/알릴%20양이온.md)

### 10. 광화학 [2+2] cycloaddition (슬라이드 p.24–28)
- 10.1 열적 $\pi2\mathrm{s}$ + $\pi2\mathrm{s}$는 금지(p.24–25). 10.2 빛을 받으면 HOMO/HOMO, LUMO/LUMO 모두 결합성이라 허용(p.26).
- 10.3 각 성분 stereospecific, endo 선택성 없음(p.27). 10.4 regioselectivity는 LUMO/LUMO 큰 계수(isobutylene + cyclohexenone)(p.28).
- → [photochemical \[2+2\] cycloaddition](../wiki/반응/광화학%202+2%20고리화%20첨가.md)

### 11. cubane (슬라이드 p.29–30)
- cubane과 octanitrocubane. Eaton & Cole 합성: 자발적 DA endo 이량화 → $h\nu$ 분자 내 [2+2] → Favorskii 고리 축소 두 번.
- → [cubane](../wiki/개념/큐베인.md)

### 12. 요약 (슬라이드 p.31)
- DA: 빠름(HOMO–LUMO 간격), stereospecific, stereoselective(endo), regioselective(ortho/para). 다양한 cycloaddition: 열적 [6+4], [4+3], 광화학 [2+2] (열적 [2+2] cumulene은 회색 처리, L15에서).
- → [Diels–Alder reaction](../wiki/반응/딜스-알더%20반응.md), [pericyclic reaction](../wiki/개념/페리고리%20반응.md)

## 반응 요약표

| 반응 | 시약/조건 | 생성물 | regioselectivity | 입체화학 | 비고 |
|---|---|---|---|---|---|
| butadiene 이량화 [4+2] | 가열 | 4-vinylcyclohexene | – | – | $\pi4\mathrm{s}$+$\pi2\mathrm{s}$, 허용 (p.7) |
| butadiene [4+4] | 가열 | (cycloocta-1,5-diene 생성 안 됨) | – | – | [열적 금지](../wiki/개념/우드워드-호프만%20규칙.md) (p.7) |
| 2-methoxybutadiene + acrylonitrile | DA | 4-methoxycyclohex-3-ene-1-carbonitrile | pseudo para | – | (p.11–12) |
| 4-methylpenta-1,3-diene + methyl acrylate | DA | methyl 2,2-dimethylcyclohex-3-ene-1-carboxylate | pseudo ortho | – | 비대칭 협동 TS (p.13) |
| (E)-penta-1,3-diene + CH2=CHW | W=CN 100 °C / W=COOR 200 °C | 1,2-이치환 cyclohexene | ortho:meta = 9:1 / 6.8:1 | – | (p.15) |
| 2-X-butadiene + methyl acrylate | – | 1,4-이치환 cyclohexene | para:meta = 6:1 (Me), 10:1 (OMe) | – | (p.15) |
| (E)-1-methoxybutadiene + acrolein | DA | cis-2-methoxycyclohex-3-ene-1-carbaldehyde | ortho | [endo](../wiki/개념/endo%20규칙.md) → OMe/CHO cis | 라세미 (p.16–17) |
| (E)-1-acetoxybutadiene + (E)-crotonaldehyde | DA | 6-formyl-5-methylcyclohex-2-en-1-yl acetate | ortho (OAc/CHO) | OAc/CHO cis, CHO/Me trans | 라세미 (p.18–19) |
| isoprene + methyl vinyl ketone | toluene 120 °C / SnCl4·5H2O 0 °C | 1-(4-methylcyclohex-3-en-1-yl)ethanone | para:meta = 71:29 / 93:7 | – | [Lewis acid](../wiki/시약/루이스%20산%20촉매.md) (p.20) |
| tropone + cyclopentadiene | [6+4 cycloaddition](../wiki/반응/6+4%20고리화%20첨가.md), 열 | 다리걸친 이환 ketone | – | 슬라이드 "endo" | $10\pi$ (p.21) |
| 6,6-dimethylfulvene + 1-NEt2-butadiene | [6+4] 후 −HNEt2 | dimethyl azulene형 골격 | CMe2–C4 | – | (p.21) |
| 1,3-dibromoacetone + Zn + diene | Zn | cyclohept-4-en-1-one | – | – | [4+3 cycloaddition](../wiki/반응/4+3%20고리화%20첨가.md) (p.22–23) |
| ethylene + maleic anhydride | 가열 ✗ / $h\nu$ ✓ | cyclobutane-1,2-dicarboxylic anhydride | – | supra–supra | [광화학 2+2](../wiki/반응/광화학%202+2%20고리화%20첨가.md) (p.24) |
| dimethyl 1,2-cyclobutenedicarboxylate + 3-methylcyclohex-2-enone | $h\nu$ | 4-4-6 삼환 diester ketone | – | 각 성분 stereospecific, anti | (p.27) |
| isobutylene + cyclohex-2-enone | $h\nu$ | 7,7-dimethylbicyclo[4.2.0]octan-2-one | CMe2–C$\beta$ | cis 융합으로 그림 | LUMO/LUMO (p.28) |
| cubane 합성 핵심 단계 | HNEt2 → 자발적 DA; $h\nu$ | $\text{endo 이량체} \longrightarrow \text{새장 diketone}$ | – | endo | [cubane](../wiki/개념/큐베인.md) (p.30) |

## 연습 문제
→ [L14 연습 문제](../practice/L14_Exercises.md)

## 출처
- 슬라이드: L14 (PDF p.1–31)
