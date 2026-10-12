---
aliases: [loose SN2 transition state, loose SN2, 느슨한 SN2, 느슨한 S_N2 전이 상태]
분류: 개념
강의: [L1, L2]
주제태그: [전이-상태, 위치선택성]
tags: [분류/개념, 범위/Test1, 단원/알켄-첨가, 강의/L01, 강의/L02, 개념유형/선택성, 주제/위치선택성, 주제/전이-상태]
---
# 느슨한 SN2 전이 상태

> leaving group 쪽 결합이 nucleophile이 들어오기 **전에 먼저 많이 늘어나**, 탄소에 상당한 부분 양전하가 쌓인 SN2 transition state다. 그래서 nucleophile이 덜 붐비는 탄소가 아니라 **더 치환된 탄소**를 공격한다.

## 개요

보통 [[SN2 반응|SN2]]는 입체 장애가 적은 탄소를 고른다. 그런데 비대칭 [[브로모늄 이온|bromonium ion]]이나 양성자화된 epoxide에서는 정반대 결과가 나온다. 예를 들어 `2-methylpropene --[Br₂, MeOH]-->` 반응에서 methanol은 **더 치환된 쪽(3차 탄소)**을 공격해 ether를 만든다. "SN2라면 보통 덜 붐비는 쪽을 공격하지 않나?" 이 모순을 푸는 열쇠가 loose SN2 transition state이고, 강의는 이것을 L1의 핵심 포인트로 꼽는다. (출처: L1 p.22–23)

## 원리

양전하를 띤 3원 고리(bromonium, 양성자화된 epoxide)가 열릴 때는 nucleophile이 들어오기 전에 C–Br⁺ 또는 C–O⁺H 결합이 먼저 상당히 늘어난다. 그러면 탄소 위에 **부분 양전하**가 쌓인다. 이때 3차 탄소 쪽은 alkyl기들이 이 양전하를 안정화해 주므로 Br이 더 많이 떨어져 나간 상태에 도달할 수 있다. nucleophile은 바로 그 탄소를 공격한다. 그래서 regioselectivity를 **입체 효과가 아닌 전자 효과**가 정한다. (출처: L1 p.23)

그래도 SN2는 SN2다. nucleophile은 leaving group의 정반대편에서 들어오므로 공격받은 탄소는 inversion되고, 첨가 전체로는 anti가 된다. (출처: L1 p.12, L2 p.10)

보충: bromonium ion을 "carbocation 옆의 Br이 비공유 전자쌍을 내주어 양전하를 달래 준 구조"로 보면 이 그림이 자연스럽다. 고리가 열리기 시작할 때 carbocation 성격이 더 치환된 탄소에 실린다(→ [[브로모늄 이온]]). (보충 근거: Clayden p.429)

![비대칭 브로모늄 이온을 MeOH가 더 치환된 탄소에서 여는 메커니즘](../../figures/L01/bromonium_meoh.svg)

*그림: C–Br 결합이 늘어나며 3차 탄소에 δ+가 쌓이고, MeOH의 산소(파랑)가 그 3차 탄소를 뒤쪽에서 공격한다. 이어서 양성자를 잃으면 ether가 된다.*

## 예

- `2-methylpropene --[Br₂, MeOH]--> (CH₃)₂C(OMe)CH₂Br`: OMe가 3차 탄소에 붙는다(→ [[할로하이드린 형성]]). (L1, 출처: L1 p.22)
- `2-methylpropene --[Br₂, H₂O]--> (CH₃)₂C(OH)CH₂Br`. (L1, 출처: L1 p.21)
- `1-methylcyclohexene --[NBS, HBr; ROH]-->` OR은 3차 탄소에, Br은 2차 탄소에 anti. regioselective이면서 stereoselective다. (L2, 출처: L2 p.12)
- `2,2-dimethyloxirane --[MeOH, H⁺]--> (CH₃)₂C(OMe)CH₂OH`: 산성 [[에폭사이드 고리 열기]]. 위치를 정하는 것은 전자 효과이며 bromonium ion이 열리는 경우와 똑같다. (L2, 출처: L2 p.8)

![산 촉매 조건에서 양성자화된 에폭사이드를 MeOH가 3차 탄소에서 여는 메커니즘](../../figures/L02/epoxide_acid.svg)

*그림: 양성자화된 산소 쪽 C–O 결합이 늘어나 3차 탄소에 δ+가 쌓이고, MeOH가 그 탄소를 공격한다.*

## 대비: 염기성 epoxide 열기

같은 epoxide를 MeO⁻로 열면 양성자화가 없어 양전하가 쌓이지 않는다. 이때는 **순수 SN2**라 입체 장애가 관건이고, MeO⁻는 1차 탄소를 공격해 (CH₃)₂C(OH)CH₂OMe가 된다. 같은 기질에서 조건만 바꿔 regioselectivity가 뒤집히는 대표적인 시험 대비다. (출처: L2 p.9)

보충: "양전하가 쌓이면 더 치환된 쪽"이라는 규칙은 한쪽이 **3차 탄소**여서 양전하를 확실히 안정화할 때 깔끔하게 맞는다. 일치환 epoxide에서는 산성에서도 1차 탄소 공격이 우세할 수 있다(→ [[에폭사이드 고리 열기]]). (보충 근거: Clayden p.438)

## 흔한 오해

- "SN2이니 덜 붐비는 탄소가 공격받는다": 양전하를 띤 3원 고리에서는 더 치환된 탄소가 공격받는다. 덜 붐비는 쪽 공격은 염기성 epoxide처럼 양전하가 없는 순수 SN2의 이야기다. (출처: L1 p.23, L2 p.9)
- "양전하가 쌓이니 사실상 SN1이다": 자유로운 [[탄소 양이온|carbocation]]이었다면 양쪽 면 공격으로 stereochemistry가 섞였을 것이다. 실제로는 inversion(anti)만 일어난다. (출처: L2 p.10)

## 관련 문서

- 개념: [[브로모늄 이온]], [[탄소 양이온]], [[마르코프니코프 규칙]], [[입체특이성과 입체선택성]]
- 반응: [[할로젠 첨가]], [[할로하이드린 형성]], [[에폭사이드 고리 열기]], [[SN2 반응]]
- 시약: [[NBS]]

## 출처

- [L1 알켄의 친전자성 첨가 1부](../../notes/L01_Electrophilic_Addition_to_Alkenes_Part1.md): 슬라이드 L1 p.21–23
- [L2 알켄의 친전자성 첨가 2부](../../notes/L02_Electrophilic_Addition_to_Alkenes_Part2.md): 슬라이드 L2 p.8–12
