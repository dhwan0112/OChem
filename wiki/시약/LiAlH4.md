---
aliases: [lithium aluminium hydride, LAH, 수소화알루미늄리튬, 리튬 알루미늄 하이드라이드, LiAlH₄]
분류: 시약
강의: [L5, L11, L15]
주제태그: [환원제, 금속-수소화물]
tags: [분류/시약, 범위/Test1, 범위/Test2, 단원/고리화-첨가, 단원/공액-첨가, 단원/환원, 강의/L05, 강의/L11, 강의/L15, 시약유형/환원제, 주제/금속-수소화물]
---
# LiAlH4

> lithium aluminum hydride(LAH). 산, ester, aldehyde, ketone, amide, nitrile, azide, alkyl halide까지 거의 모든 극성 작용기를 환원하는 강한 환원제다. 강한 만큼 chemoselectivity는 낮다.

## 개요

[hydride 시약의 세기](../개념/금속%20수소화물의%20반응성.md)는 LiAlH₄ > LiBH₄ > NaBH₄ > NaBH₃CN 순이고, 강할수록 선택성이 떨어진다. LiAlH₄는 그 맨 위에 있어서 "무엇을 환원하나"보다 "무엇이 살아남나"를 묻는 편이 빠르다. carboxylic acid, ester, aldehyde는 1차 alcohol로, ketone은 2차 alcohol로 환원하고, amide는 amine으로 바꾼다. (출처: L5 p.18, p.23)

LiAlH₄는 너무 반응성이 커서 쓸 수 있는 용매가 탄화수소, ether, 3차 amine으로 제한되며, 보통 diethyl ether, THF, diglyme을 쓴다. 물과 격렬히 반응하므로 후처리(H₂O 또는 H₂O/H₂SO₄)는 별도 단계로 적는다. 슬라이드는 LiAlH₄를 "pyrophoric chemical"로 경고하는데, 다룰 때 조심해야 한다.[^1] (출처: L5 p.21, p.23)

## 무엇을 하나

| 기질 | 생성물 | 비고 |
|---|---|---|
| aldehyde, ester | 1차 alcohol | ester는 RCH₂OH + R′OH 두 alcohol |
| ketone | 2차 alcohol | |
| carboxylic acid | 1차 alcohol | O–H가 먼저 H₂를 내므로 느리지만 충분히 쓰면 92% |
| amide | amine | C=O → CH₂ ([amide 환원](../반응/아마이드%20환원.md)) |
| nitrile, azide | 1차 amine | ([azide·nitrile을 거친 amine 합성](../반응/아자이드·나이트릴을%20거친%20아민%20합성.md)) |
| alkyl halide | alkane | 할로젠 자리에 H |

(출처: L5 p.7–9, p.17, p.23–24)

### carbonyl 환원

- `2,2-dimethylpropanoic acid (CH3)3CCO2H --[(1) LiAlH4, Et2O; (2) H2O/H2SO4]--> neopentyl alcohol (CH3)3CCH2OH (92%)` (L5)
- `RCO2R' --[(1) LiAlH4, Et2O; (2) H2O/H2SO4]--> RCH2OH + R'OH` (L5)

ester를 환원하면 alcohol이 두 개 나온다는 점에 주의하자. acyl 쪽은 RCH₂OH가 되고 alkoxy 쪽은 R′OH로 떨어져 나온다. (출처: L5 p.23)

### 할로젠도 떼어 낸다

LiAlH₄는 carbonyl뿐 아니라 alkyl halide도 환원해 할로젠을 H로 바꾼다.

- `2-bromopentane --[(1) LiAlH4, ether; (2) H2O/H2SO4]--> pentane` (L5)
- `(1-bromoethyl)benzene PhCH(Br)CH3 --[(1) LiAlD4, ether; (2) H2O/H2SO4]--> PhCHDCH3` (L5)

두 번째 예는 왜 굳이 LiAlD₄를 썼을까? D가 정확히 Br이 있던 자리에 들어간 것을 보면, hydride가 C–Br 탄소를 직접 공격해 Br을 밀어낸다는 것을 알 수 있다.[^2] alkyl halide를 환원하는 다른 방법으로는 (a) elimination 후 hydrogenation, (b) alkyl radical을 거치는 방법이 있다. (출처: L5 p.24)

## 원리: amide가 amine이 되는 이유

ester는 [tetrahedral intermediate](../개념/사면체%20중간체.md)에서 OR이 떨어지지만, amide는 금속에 붙은 O가 떨어지고 N이 남아 iminium을 거쳐 다시 환원된다. 이 흐름은 슬라이드에 [borane](보레인.md) 메커니즘으로 그려져 있다(→ [amide 환원](../반응/아마이드%20환원.md)). (출처: L5 p.9, p.28)

## 선택성

거의 다 환원하므로 chemoselectivity를 기대하기 어렵다. 그래도 남는 것은 있다.

- aryl methyl ether, 고리형 ether는 그대로 남는다. lactam·enone을 가진 다고리 화합물에서 lactam은 고리형 amine, enone C=O는 allylic alcohol이 된다. 보충: LiAlH₄는 enone을 주로 1,2-환원하므로 C=C는 남는다(→ [1,2-첨가와 1,4-첨가](../개념/1,2-첨가와%201,4-첨가.md)). ([L5 연습 문제](../../practice/L05_Exercises.md) 6번) (출처: L5 p.26)
- 고립된 C=C는 극성이 없어 환원되지 않는다. alkene은 [catalytic hydrogenation](../반응/촉매%20수소화.md)의 몫이다. (출처: L5 p.30)
- isoxazoline을 LiAlH₄로 환원하면 C=N 환원과 N–O 절단이 함께 일어나 1,3-amino alcohol이 된다. (L15) (출처: L15 p.20)
- sirenin 합성에서는 `LiAlH4, AlCl3`가 CHO와 CO₂Me를 함께 CH₂OH로 환원한다(→ [SeO2](SeO2.md)). (L6) (출처: L6c p.18)

## 이웃 시약과 비교

- **[LiBH4](LiBH4.md):** ester는 환원하지만 산·amide·nitrile은 남긴다. LiAlH₄로는 이런 구분이 안 된다. (출처: L5 p.22)
- **[borane](보레인.md):** 산과 amide를 빠르게, ester·ketone은 느리게 환원한다. amide → amine은 둘 다 되지만 BH₃는 ester를 남긴다. (출처: L5 p.27)
- **[DIBAL-H](DIBAL-H.md):** LiAlH₄는 ester를 alcohol까지 보내지만, DIBAL-H는 −70 °C에서 aldehyde에서 멈춘다. 대안으로 LiAlH₄로 alcohol까지 환원한 뒤 [DMP](DMP.md) 같은 순한 산화제로 aldehyde까지 되돌리는 우회로도 있다(→ [ester 부분 환원](../반응/에스터%20부분%20환원.md)). (출처: L5 p.29, L6c p.2)

## 흔한 오해

- **"amide를 LiAlH₄로 환원하면 alcohol이 된다"고 생각하기 쉽지만 사실은** C=O가 CH₂가 되어 **amine**이 된다. alcohol 두 개가 나오는 것은 ester다. (출처: L5 p.9, p.23)
- **"표에 산이 '느림'이니 산은 환원되지 않는다"**: 산의 O–H가 먼저 hydride 1당량을 H₂로 소모해 느려질 뿐, 시약을 넉넉히 쓰면 환원된다(→ [metal hydride의 반응성](../개념/금속%20수소화물의%20반응성.md)). (출처: L5 p.17, p.23)

## 관련 문서

- 반응: [amide 환원](../반응/아마이드%20환원.md), [azide·nitrile을 거친 amine 합성](../반응/아자이드·나이트릴을%20거친%20아민%20합성.md), [ester 부분 환원](../반응/에스터%20부분%20환원.md)
- 비교 시약: [NaBH4](NaBH4.md), [LiBH4](LiBH4.md), [DIBAL-H](DIBAL-H.md), [borane](보레인.md)
- 개념: [metal hydride의 반응성](../개념/금속%20수소화물의%20반응성.md), [tetrahedral intermediate](../개념/사면체%20중간체.md)

## 출처

- [L5 환원](../../notes/L05_Reduction.md) 1절, 2절 (슬라이드 p.7–9, p.17, p.21, p.23–26)
- [L5 연습 문제](../../practice/L05_Exercises.md) 6번
- [L6 산화와 alkene 합성](../../notes/L06_Oxidation_and_Alkene_Synthesis.md) 0절, 4절
- [L15 cycloaddition 3부](../../notes/L15_Cycloaddition_Part3.md) isoxazoline 절

[^1]: 엄밀히 LiAlH₄는 공기 중에서 저절로 불붙는 전형적인 pyrophoric 물질이라기보다는 물과 반응해 가연성 H₂를 내는 수반응성(water-reactive) 물질로 분류되는 경우가 많다. 슬라이드의 불꽃 표지는 인화성 위험을 뜻한다. 어느 쪽이든 물·습기를 철저히 피해야 한다.
[^2]: 1차·2차 halide의 LiAlH₄ 환원은 주로 S<sub>N</sub>2형 hydride 치환으로 설명된다. 슬라이드가 말한 "alkyl radical 경유" 방법의 대표 시약은 Bu₃SnH/AIBN이다.
