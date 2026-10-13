---
aliases: [Pd/C, 팔라듐-탄소, palladium on carbon, H2/Pd-C, 팔라듐 탄소]
분류: 시약
강의: [L3, L5, L11, L12]
주제태그: [환원, 촉매, 수소화, 탈보호]
tags: [분류/시약, 범위/Test1, 범위/Test2, 단원/공액-첨가, 단원/방향족-치환, 단원/보호기, 단원/환원, 강의/L03, 강의/L05, 강의/L11, 강의/L12, 시약유형/촉매, 시약유형/환원제, 주제/수소화, 주제/탈보호]
---
# Pd/C

> 팔라듐을 탄소에 올린 불균일 촉매(보통 질량비 5% 또는 10%). H₂와 함께 C=C, C≡C, C=N, nitro, nitrile을 환원하고 benzyl group(Bn, Cbz)를 끊는다. ketone은 보통 남긴다.

## 개요

금속 수소화물은 극성인 C=O, C=N에는 잘 듣지만 무극성 C=C에는 거의 반응하지 않는다. H₂ 자체도 무극성이라 반응성이 없지만, 금속 촉매 표면에서는 C=C, C=N, 삼중결합 등을 환원한다. Pd/C는 그 대표 촉매로, 녹지 않으므로 여과로 회수해 재사용할 수 있다. 반응 자체는 [catalytic hydrogenation](../반응/촉매%20수소화.md) 문서에 있다. (출처: L5 p.30)

## 무엇을 하나

슬라이드는 쉬운 것부터 어려운 것까지 다음 순서로 줄 세운다. (출처: L5 p.33)

| 순서 | 기질 | 생성물 |
|---|---|---|
| 1 | RCOCl | RCHO (피독 촉매 필요, [Rosenmund reduction](../반응/로젠문트%20환원.md)) |
| 2 | ArNO₂ | ArNH₂ |
| 3 | RC≡CR | *cis*-RCH=CHR (멈추려면 [Lindlar catalyst](린들라%20촉매.md)) |
| 4 | imine R₂C=NR | amine R₂CH–NHR |
| 5 | alkene | 알케인 |
| 6 | RX–CH₂Ph (X = O, NH) | RXH + PhCH₃ (benzyl group 제거) |
| 7 | RCN | RCH₂NH₂ |
| 8 | benzene 고리 | cyclohexane 고리 (센 조건) |

## 원리와 입체화학

H₂가 촉매 표면에 흡착되고, alkene이 한쪽 면을 표면에 대고 배위한 뒤, 표면의 H 두 개가 같은 면에서 차례로 탄소에 옮겨 간다. 그래서 **syn 첨가**다. 예: 1,2-dimethylcyclohexene --[H₂, PtO₂, AcOH]--> *cis* 82% + *trans* 18%. *trans*가 섞이는 것은 보충 설명으로 표면에서의 이중결합 이성질화 때문이라고 한다. (보충 근거: Clayden p.535–536) (출처: L5 p.31)

## 선택성과 예

- **C=C만, ketone은 그대로:** 4-(4-hydroxyphenyl)뷰트-3-엔-2-온 --[H₂, Pd/C]--> 4-(4-hydroxyphenyl)butane-2-온(보충: 이른바 라즈베리 ketone, 보충 근거: Clayden p.536). 금속 수소화물과 정반대의 선택성이다. (출처: L5 p.30)
- **nitro 환원:** nitrobenzene --[H₂, Pd/C]--> aniline. [nitration](../반응/나이트로화.md) 다음 [diazonium salt reactions](../반응/다이아조늄%20염%20반응.md)으로 가는 다리다. (출처: L3 p.13, L5 p.33)
- **imine·nitrile:** 벤라팍신 특허 경로는 사이아노 alcohol을 H₂(12 bar), Pd/C, HCHO(2.2 eq)로 한 번에 처리해 nitrile 환원과 환원성 아미노화 두 번을 연달아 일으킨다(94%). conjugate addition 생성물의 nitrile도 H₂/Pd/C로 1차 amine이 된다. (출처: L5 p.16, L11 p.20)
- **benzyl group 제거(수소화분해):** benzyl ether(OBn)와 [Cbz protecting group](Cbz%20보호기.md)는 H₂, Pd/C로 벗긴다. 보충: Cbz는 toluene과 carbamic acid이 되고, carbamic acid이 CO₂를 잃어 amine이 된다. (보충 근거: Wade p.1171) (출처: L12 p.5, p.8)

## 이웃 촉매와 비교

- **PtO₂(Adams catalyst):** 실제 촉매는 수소화 중 생기는 Pt 금속이다. 방향족 수소화(PtO₂, AcOH)에도 쓴다. (출처: L5 p.30–31)
- **[Lindlar catalyst](린들라%20촉매.md) (Pd/CaCO₃/Pb(OAc)₂):** 피독시켜 alkyne을 *Z*-alkene에서 멈춘다. (출처: L6c p.23)
- **Pd/BaSO₄ + 퀴놀린:** acid chloride을 aldehyde에서 멈추는 [Rosenmund reduction](../반응/로젠문트%20환원.md). (출처: L5 p.33)
- **[NaBH3CN](NaBH3CN.md):** 환원성 아미노화를 할 때 benzyl기를 건드리지 않는다. (출처: L5 p.14)

## 흔한 오해

- "H₂/Pd-C는 alkene만 환원하니 안전하다": benzyl ether, benzyl amine, Cbz가 함께 끊어질 수 있다. 그래서 Cbz와 benzyl ether는 서로 [직교적](../개념/직교%20보호.md)이지 않다. (출처: L5 p.33, L12 p.5)
- "syn 첨가니까 *cis*만 100% 나온다": 1,2-dimethylcyclohexene에서 *trans*가 18% 나온다. (출처: L5 p.31)

## 관련 문서

- 반응: [catalytic hydrogenation](../반응/촉매%20수소화.md), [Lindlar reduction](../반응/린들라%20환원.md), [Rosenmund reduction](../반응/로젠문트%20환원.md), [reductive amination](../반응/환원성%20아미노화.md), [hydrogenolysis](../반응/수소화분해.md)
- 시약: [Lindlar catalyst](린들라%20촉매.md), [Cbz protecting group](Cbz%20보호기.md), [NaBH3CN](NaBH3CN.md), [PtO2](PtO2.md), [benzyl ether protecting group](벤질%20에터%20보호기.md)
- 개념: [protecting group](../개념/보호기.md), [orthogonal protection](../개념/직교%20보호.md)

## 출처

- [L5 환원](../../notes/L05_Reduction.md) 1절, 3절
- [L3 electrophilic aromatic substitution 1부](../../notes/L03_Electrophilic_Aromatic_Substitution_Part1.md) 3절 (슬라이드 p.13)
- [L11 conjugate addition](../../notes/L11_Conjugate_Addition.md) 5절
- [L12 protecting group](../../notes/L12_Protecting_Groups.md) protecting group 표, 카바메이트 절
