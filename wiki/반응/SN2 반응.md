---
aliases: [SN2, S_N2, SN2 reaction, 이분자 친핵성 치환, bimolecular nucleophilic substitution, 뒤쪽 공격, backside attack]
분류: 반응
강의: [L1, L2, L5, L6, L7, L10, L11, L12]
주제태그: [친핵성-치환, 입체화학]
tags: [분류/반응, 범위/Test1, 범위/Test2, 단원/공액-첨가, 단원/보호기, 단원/산화-알켄-합성, 단원/알켄-첨가, 단원/엔올레이트, 단원/환원, 강의/L01, 강의/L02, 강의/L05, 강의/L06, 강의/L07, 강의/L10, 강의/L11, 강의/L12, 유형/친핵성-치환, 주제/입체화학]
---
# SN2 반응

> nucleophile이 leaving group의 **정반대편에서** 탄소를 공격하고, 그와 동시에 leaving group이 떨어지는 한 단계 치환 반응. 공격받은 탄소의 배치가 **inversion**된다. CM3121에는 SN2를 다루는 단원이 따로 없지만, epoxide ring opening, enolate alkylation, ylide 제조, amine 합성, protecting group 전략 등 거의 모든 단원에 부품처럼 다시 나온다.

## 개요

이 과목은 SN2를 이미 아는 것으로 보고, 다른 반응의 한 단계로 계속 끌어다 쓴다. 그래서 "이 단계가 SN2인가?"를 알아보는 것만으로 stereochemistry(inversion)와 기질 제한(methyl·1차는 좋고 3차는 안 됨)을 곧바로 예측할 수 있다. 이 문서는 과목 곳곳에 흩어진 SN2를 한곳에 모은다. regioselectivity가 뒤집히는 특수한 경우는 [loose SN2 transition state](../개념/느슨한%20SN2%20전이%20상태.md)에서 따로 다룬다. (출처: L1 p.12; L7 p.9–10)

## 원리

- **backside attack과 inversion:** nucleophile은 C–X σ\* orbital과 가장 잘 겹치도록 leaving group의 정반대편(180°)에서 일직선으로 들어온다. 그래서 공격받은 탄소의 configuration이 inversion된다. (출처: L1 p.12)
- **입체 장애가 위치를 정한다:** 양전하가 쌓이지 않는 "순수한" SN2에서는 덜 붐비는 탄소가 공격받는다. 예를 들어 염기성 조건에서 MeO⁻는 epoxide의 1차 탄소만 공격한다. (출처: L2 p.9)
- **기질 제한:** methyl·1차(특히 allylic·benzylic)는 좋고, 2차는 느리며 E2 elimination과 경쟁하고, 3차는 elimination만 일어난다. leaving group으로는 Cl, Br, I, OTs가 쓰인다. (출처: L7 p.9–10)

![Br⁻가 bromonium ion을 반대쪽에서 공격하는 SN2 단계](../../figures/L01/bromonium_step2.svg)

그림: Br⁻(파랑)가 C–Br⁺ 결합(빨강)의 정반대편에서 탄소를 공격한다. 새 C–Br 결합(초록)은 원래 Br의 반대편에 놓이므로 두 Br이 anti가 된다.

## 이 과목에서 SN2가 나오는 곳

| 단원 | nucleophile → electrophile | 무엇을 위한 SN2인가 | 출처 |
|---|---|---|---|
| [halogen addition](할로젠%20첨가.md) | Br⁻ → [bromonium ion](../개념/브로모늄%20이온.md) | anti 첨가의 원인 | L1 p.12; L2 p.10 |
| [halohydrin formation](할로하이드린%20형성.md) → epoxide | alkoxide → 옆 탄소의 C–Br (분자내) | epoxide 고리 닫기 | L1 p.21 |
| [epoxide ring opening](에폭사이드%20고리%20열기.md) (염기) | RO⁻, amine → 덜 치환된 탄소 | *trans* 생성물, 입체 효과로 위치 결정 | L2 p.9–10 |
| [amine synthesis via azide and nitrile](아자이드·나이트릴을%20거친%20아민%20합성.md) | NH₃, N₃⁻, CN⁻ → R–X | C–N 또는 C–C 결합, overalkylation 회피 | L5 p.5–8 |
| [phosphorus ylide](../시약/인%20일라이드.md) 제조 | PPh₃ → 1차·2차 R–X | phosphonium salt → [Wittig reaction](위티그%20반응.md) | L6 p.26 |
| [enolate alkylation](엔올레이트%20알킬화.md) | enolate α-탄소 → R–X | α-C–C 결합 형성 | L7 p.9–10; L10 p.2 |
| [acetoacetic ester synthesis](아세토아세트산%20에스터%20합성.md)·[malonic ester synthesis](말론산%20에스터%20합성.md) | stabilized enolate → R–X | alkyl group 도입 후 [decarboxylation](탈카복실화.md) | L7 p.16–19 |
| [Evans oxazolidinone](../시약/에반스%20옥사졸리디논.md) | chelated Z-enolate → BnBr | 한쪽 면에서만 SN2 → 99:1 dr | L7 p.27–28 |
| [Stork enamine reaction](스토크%20엔아민%20반응.md) | [enamine](../개념/엔아민.md) α-탄소 → R–X | iminium ion 경유 alkylation | L10 p.11 |
| nitro-[Michael reaction](마이클%20반응.md) 후 고리 닫기 | nitronate 탄소 → 같은 분자의 C–I | 분자내 alkylation | L11 p.17; L13 p.6 |
| [silyl ether protecting group](../시약/실릴%20에터%20보호기.md) 예 | lithium acetylide → C–Br | OH를 TBDMS로 막아야 SN2가 된다 | L12 p.5–6 |

(출처: 표의 각 행)

## 예

- $\text{cyclopentene oxide} \xrightarrow{\mathrm{Me_2NH}} \text{trans-2-(dimethylamino)cyclopentanol}\ \mathrm{(\pm )}$

  backside attack이므로 *trans*. (출처: L2 p.10)
- $\mathrm{PhCH_2CH_2Br} \xrightarrow[\mathrm{EtOH}]{\mathrm{NaN_3}} \mathrm{PhCH_2CH_2N_3} \xrightarrow{1.\ \mathrm{LiAlH_4};\ 2.\ \mathrm{H_2O}} \mathrm{PhCH_2CH_2NH_2}\ (89\unicode{x25})$

  (출처: L5 p.7)
- $\mathrm{CH_3CH(OTBDMS)(CH_2)_3Br} \xrightarrow{\mathrm{HC{\equiv}CLi}} \mathrm{CH_3CH(OTBDMS)(CH_2)_3C{\equiv}CH}$

  (출처: L12 p.5–6)
- 연습 문제에서는 alcohol → OTs(retention) → KCN(SN2, inversion)처럼 stereocenter를 추적하는 문제로 나온다. (출처: Tutorial 1 문제 2)

## 흔한 오해

- "SN2이면 항상 덜 치환된 탄소가 공격받는다": protonated epoxide나 비대칭 bromonium ion처럼 양전하를 띤 3원 고리는 C–X 결합이 먼저 늘어나 **더 치환된** 탄소가 공격받는다. 그래도 inversion은 그대로다(→ [loose SN2 transition state](../개념/느슨한%20SN2%20전이%20상태.md)). (출처: L1 p.22–23; L2 p.8)
- "alkyl halide이면 무엇이든 alkylate된다": 2차는 E2와 경쟁해 수율이 나쁘고 3차는 elimination만 일어난다. 그래서 [Wittig reaction](위티그%20반응.md) retrosynthesis에서도 ylide 쪽은 SN2가 잘 되는 1차 halide에서 오도록 끊는 편이 유리하다. (출처: L7 p.10; L6 p.26)
- "leaving group 능력은 어디서나 I > Br > Cl > F": [nucleophilic aromatic substitution](친핵성%20방향족%20치환.md)에서는 슬라이드가 F를 가장 좋은 leaving group으로 꼽아, SN2와 순서가 정반대다. (출처: L11 p.22–23) 보충: F의 이탈 능력이 좋아서가 아니라, 느린 단계가 첨가이고 전기음성도가 큰 F가 ipso 탄소를 활성화하기 Clayden. (보충 근거: Clayden p.518)

참고로 Fmoc protecting group이 산에 강한 이유도 SN2로 설명된다. carbamate O에 붙은 CH₂는 1차라 SN1이 안 되고, 옆의 부피 큰 fluorenyl기 때문에 SN2도 막혀 있다(→ [Fmoc protecting group](../시약/Fmoc%20보호기.md)). (출처: L12 p.11)

## 관련 문서

- 반응: [epoxide ring opening](에폭사이드%20고리%20열기.md), [halogen addition](할로젠%20첨가.md), [enolate alkylation](엔올레이트%20알킬화.md), [amine synthesis via azide and nitrile](아자이드·나이트릴을%20거친%20아민%20합성.md), [Wittig reaction](위티그%20반응.md), [Stork enamine reaction](스토크%20엔아민%20반응.md), [nucleophilic aromatic substitution](친핵성%20방향족%20치환.md)
- 시약: [phosphorus ylide](../시약/인%20일라이드.md), [Evans oxazolidinone](../시약/에반스%20옥사졸리디논.md), [silyl ether protecting group](../시약/실릴%20에터%20보호기.md)
- 개념: [loose SN2 transition state](../개념/느슨한%20SN2%20전이%20상태.md), [electrophile and nucleophile](../개념/친전자체와%20친핵체.md), [stereospecificity and stereoselectivity](../개념/입체특이성과%20입체선택성.md), [bromonium ion](../개념/브로모늄%20이온.md)

## 출처

- [L1 Electrophilic Addition to Alkenes, Part 1](../../notes/L01_Electrophilic_Addition_to_Alkenes_Part1.md): 슬라이드 L1 p.12, p.21–23
- [L2 Electrophilic Addition to Alkenes, Part 2](../../notes/L02_Electrophilic_Addition_to_Alkenes_Part2.md): 슬라이드 L2 p.8–10
- [L5 Reduction](../../notes/L05_Reduction.md) 1절
- [L6 Oxidation and Alkene Synthesis](../../notes/L06_Oxidation_and_Alkene_Synthesis.md) 7절
- [L7 Enolate Alkylation](../../notes/L07_Enolate_Alkylation.md) II절, III절, VI절
- [L10 Enol and Enamine](../../notes/L10_Enol_and_Enamine.md) 본문 (p.2, p.11)
- [L11 Conjugate Addition](../../notes/L11_Conjugate_Addition.md) (p.17, p.22–23)
- [L12 Protecting Groups](../../notes/L12_Protecting_Groups.md) 5절, Fmoc
- [Tutorial 1](../../practice/Tutorial_1.md) 문제 2
