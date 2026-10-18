---
aliases: [Horner–Wadsworth–Emmons reaction, HWE reaction, 호너-워즈워스-에먼스 반응, Horner-Wadsworth-Emmons]
분류: 반응
강의: [L6, L7, L8]
주제태그: [알켄-합성, 올레핀화, 포스포네이트]
tags: [분류/반응, 범위/Test1, 기출/Test1-2025, 인명반응, 단원/산화-알켄-합성, 단원/엔올레이트, 강의/L06, 강의/L07, 강의/L08, 유형/C–C-결합-형성, 유형/친핵성-첨가, 주제/알켄-합성, 주제/올레핀화, 주제/포스포네이트]
---
# HWE 반응

> $\begin{aligned} & \text{phosphonate carbanion}\ \mathrm{(EtO)_2P(O)CH^-{-}EWG} \\ &  + \text{aldehyde·ketone} \\ & \longrightarrow \text{E-alkene} + \text{수용성 phosphate 염} \end{aligned}$. [Wittig reaction](위티그%20반응.md)의 phosphonate 변형이다.

## 개요

stabilized ylide로 *E*-alkene을 만들 수 있다면, 더 좋은 방법이 따로 필요할까? 슬라이드의 답은 Horner–Wadsworth–Emmons(HWE) 반응이다. 1953년 Wittig이 phosphonium ylide로 olefin 합성을 보고했고, 1958년 Horner가 phosphonium 대신 phosphonate로 안정화된 carbanion(phosphonate-stabilized carbanion)을 쓰는 변형을 발표했다. 이후 Wadsworth와 Emmons가 적용 범위를 넓혔다.[^1] (출처: L6c p.36)

## 원리


$$
\begin{aligned}
& (EtO)_2P(O)CH_2C(O)R \\
& \xrightarrow{\text{염기:}\ \mathrm{EtO^-}\ \text{또는}\ \mathrm{NaH}} \\
& \text{phosphonate carbanion}\ (\mathrm{P{=}C},\ \text{탄소 anion},\  \\
& \text{enolate로 쓰는 공명 구조})
\end{aligned}
$$


P와 C=O 사이의 CH₂는 양쪽 기가 음전하를 안정화하므로 산성이 크다. 생긴 carbanion은 enolate 공명 구조로도 그릴 수 있다(→ [enol and enolate](../개념/엔올과%20엔올레이트.md), [alpha-hydrogen acidity](../개념/α-수소의%20산도.md)). 이 carbanion이 carbonyl에 첨가한 뒤 Wittig과 같은 방식으로 4원 고리([oxaphosphetane](../개념/옥사포스페테인.md)형)를 거쳐 phosphate를 내보내며 C=C가 생긴다. (출처: L6c p.36, L8 p.6)

L7의 enolate 복습 슬라이드는 이 phosphonate anion을 stabilized ylide와 같은 부류로 묶는다. $(EtO)_2P(=O)CH_2C(=O)R \xrightarrow{\mathrm{EtO^-}\ \text{또는}\ \mathrm{NaH}}$로 생긴 anion은 P=O 쪽과 C=O 쪽으로 동시에 비편재화된 세 공명 구조를 갖는다.[^2] (출처: L7 p.3)

### 메커니즘 단계와 aldol과의 관계

예: $(EtO)_2P(O)CH_2CO_2Et$ + PhCHO
1. EtO⁻가 P와 C=O 사이의 산성 CH₂ 양성자를 떼어 enolate를 만든다.
2. enolate의 $\alpha$-탄소(nucleophile)가 PhCHO의 carbonyl electrophile을 공격해 alkoxide가 생긴다. 슬라이드에서 박스로 강조된 이 단계가 aldol addition과 같은 모양이다.
3. alkoxide O⁻가 인을 공격해 4원 고리 intermediate([oxaphosphetane](../개념/옥사포스페테인.md)형)를 만든다.
4. C–P, O–P 결합이 재배열되며 $(EtO)_2PO_2^-$가 떨어지고 C=C가 생겨 (*E*)-$EtO_2C$–CH=CH–Ph가 된다.

일반식은 $R^1COR^2 + R^3O_2C\ \mathrm{{-}}\ CH(R^4)\ \mathrm{{-}}\ P(O)(OR^5)_2 \xrightarrow{\mathrm{Base}} R^3O_2C\ \mathrm{{-}}\ C(R^4)\ =\ CR^1R^2\ \text{이다}$. L8이 aldol에 앞서 HWE를 다시 꺼내는 이유가 2단계다. HWE에서는 alkoxide가 인에 붙잡혀 alkene으로 가지만, aldol에서는 alkoxide가 그냥 양성자를 받아 OH로 남는다(→ [aldol reaction](알돌%20반응.md)). (출처: L8 p.5, p.6)

생성물은 이치환 alkene에서 *E*-선택성이 높다. ketone과도 잘 반응한다.[^3] (출처: L6c p.36)

보충: 그럼 stabilized Wittig ylide는 왜 부족할까? 이름 그대로 너무 안정하기 때문이다. Ph₃P=CHCHO 같은 ylide는 물에서 재결정할 수 있을 정도이고, 원료 phosphonium salt보다도 안정하다. 안정한 만큼 반응성이 낮아 ketone처럼 덜 electrophilic한 상대와는 잘 반응하지 않는다. 그래서 같은 *E*-선택적 olefination을 하되, 더 반응성 있는 phosphonate carbanion으로 바꾼 것이 HWE다. (보충 근거: Clayden p.692)

## 선택성

- 이치환 alkene에서 ***E*-선택성**이 높다. (출처: L6c p.36)
- 실험실에서 HWE를 좋아하는 이유 하나는 부산물인 diethyl phosphate 염이 물에 녹아, 분리가 까다로운 Ph₃P=O보다 훨씬 쉽게 씻겨 나간다는 점이다. (출처: L6c p.37)

## 예

- $\begin{aligned} & \text{2,2-dimethylcyclopentanone} + (EtO)_2P(O)CH_2CO_2Et \\ & \xrightarrow{\mathrm{NaH}} \text{ethyl (2,2-dimethylcyclopentylidene)acetate} \end{aligned}$. 그림에서 CO₂Et는 gem-dimethyl 반대쪽으로 그려져 있다. (L6) (출처: L6c p.37)
- 슬라이드에는 빈칸이 있는 HWE 예가 두 개 더 있다. 하나는 KHMDS를 쓴 분자 간 반응이고, 다른 하나는 NaH/THF를 쓴 분자 내 반응($\beta$-lactam 기질 → 6원 고리가 닫힌 1-carbacephem 골격, 85%)이다([L6 연습 문제](../../practice/L06_Exercises.md) 6번). (L6) (출처: L6c p.37)

![2,2-dimethylcyclopentanone + (EtO)2P(O)CH2CO2Et → ethyl (2,2-dimethylcyclopentylidene)acetate](../../figures/L06/hwe_dimethylcyclopentanone.svg)

그림: phosphonate anion(파랑)이 C=O(빨강)와 새 C=C(초록)를 만든다.

![2,2-dimethylcyclopentanone + (EtO)2P(O)CH2CO2Et → ethyl (2,2-dimethylcyclopentylidene)acetate HWE 종합 메커니즘](../../figures/L06/hwe_dimethylcyclopentanone_mech.svg)

그림: 보충: 위 줄은 전체 반응이고, 아래 두 줄은 단계별 메커니즘이다(평형 화살표 ⇌로 연결, 단계 구성은 위 4단계 목록, 곧 L8 슬라이드의 메커니즘을 따랐다). 1단계: $\mathrm{NaH}$의 $\mathrm{H^-}$(base)가 P와 C=O 사이 CH$_2$의 H(빨강, acid)를 떼어 phosphonate carbanion과 $\mathrm{H_2}$가 된다. 2단계: carbanion(파랑, nucleophile)이 ketone의 C=O 탄소(빨강, electrophile)를 공격해 alkoxide가 된다. 3단계: alkoxide의 O$^-$가 P를 공격해 4원 고리 oxaphosphetane형 intermediate가 된다. 4단계: C–P와 C–O 결합이 끊어지며 C=C(초록)와 $(\mathrm{EtO})_2\mathrm{PO_2^-}$가 생긴다. 4단계의 화살표는 그림 맨 아래 줄 오른쪽 intermediate에 그렸고, 맨 위 줄의 생성물 옆 $\mathrm{Na^+}$는 반대 이온이다.

## 흔한 오해

- **"HWE도 Wittig처럼 Ph₃P=O가 나온다"**: P에 phenyl이 아니라 ethoxy가 붙어 있어 수용성 phosphate 염이 나온다. (출처: L6c p.37)
- **"*Z*-alkene이 필요할 때도 HWE"**: 슬라이드 요약에서 *Z*는 unstabilized Wittig ylide, *E*는 stabilized ylide 또는 HWE다(→ [stereoselective alkene synthesis](../개념/알켄의%20입체선택적%20합성.md)). (출처: L6c p.38)

## 관련 문서

- 반응: [Wittig reaction](위티그%20반응.md), [Lindlar reduction](린들라%20환원.md), [dissolving metal reduction](용해%20금속%20환원.md), [aldol reaction](알돌%20반응.md)
- 시약: [phosphorus ylide](../시약/인%20일라이드.md)
- 개념: [stereoselective alkene synthesis](../개념/알켄의%20입체선택적%20합성.md), [enol and enolate](../개념/엔올과%20엔올레이트.md), [alpha-hydrogen acidity](../개념/α-수소의%20산도.md), [stereospecificity와 stereoselectivity](../개념/입체특이성과%20입체선택성.md), [oxaphosphetane](../개념/옥사포스페테인.md)

## 출처

- [L6 산화와 alkene 합성](../../notes/L06_Oxidation_and_Alkene_Synthesis.md) 7절 (L6c p.36–38)
- [L7 enolate alkylation](../../notes/L07_Enolate_Alkylation.md) (p.3)
- [L8 aldol reaction](../../notes/L08_Aldol_Reactions.md) (p.5–6)
- [L6 연습 문제](../../practice/L06_Exercises.md) 6번

[^1]: 보충: Wadsworth와 Emmons의 논문은 1961년에 나왔다.
[^2]: 슬라이드는 HWE anion도 "stabilized ylide"라고 부르지만, 엄밀히 말하면 인 원자에 양전하가 없으므로 ylide라기보다 phosphonate-stabilized carbanion이다. (출처: L7 p.3)
[^3]: 보충: phosphonate carbanion은 stabilized phosphonium ylide보다 nucleophilicity가 커서 ketone과도 잘 반응한다(Clayden 27장). (보충 근거: Clayden p.628, p.692)
