---
aliases: [endo rule, 엔도 규칙, endo 선택성, endo/exo, 알더 endo 규칙, 2차 오비탈 겹침, secondary orbital overlap]
분류: 개념
강의: [L13, L14, L15]
주제태그: [입체선택성, 딜스-알더, 오비탈]
tags: [분류/개념, 범위/Test2, 인명규칙, 단원/고리화-첨가, 강의/L13, 강의/L14, 강의/L15, 개념유형/선택성, 주제/딜스-알더, 주제/입체선택성]
---
# endo 규칙

> [Diels–Alder reaction](../반응/딜스-알더%20반응.md)에서는 dienophile의 π 치환기(C=O 등)가 diene π계 **아래로 tucked under** endo TS가 endo rule. 이유는 secondary orbital overlap(2차 오비탈 겹침)이다.

## 개요

stereospecificity가 **한 반응물 안**의 치환기끼리의 관계를 정한다면, endo rule은 **두 반응물 사이**의 관계를 정한다. dienophile의 치환기와 diene 사이의 관계는 무엇이 정할까? 예를 들어 cyclopentadiene + maleic anhydride에서는 anhydride 고리가 새 C=C 쪽을 향하는 endo adduct와, CH2 다리 쪽을 향하는 exo adduct가 둘 다 이론적으로 가능하다. 실제로는 **endo adduct만** 생긴다. DA 반응은 보통 endo TS를 거치는 쪽이 우세하며, 이를 endo rule이라고 한다(→ [stereospecificity와 stereoselectivity](입체특이성과%20입체선택성.md)). (출처: L13 p.21)

![cyclopentadiene + maleic anhydride의 endo adduct(생성)과 exo adduct(생성 안 됨)](../../figures/L13/endo_exo.svg)

*그림: 초록색은 DA 반응으로 새로 생긴 σ 결합 두 개, 파란색은 다리 걸친 고리에 남은 C=C, 빨간색은 anhydride의 C=O다. 왼쪽 endo adduct에서는 anhydride 고리가 C=C 쪽(아래)으로 접혀 들어가 있어 C=C와 C=O가 분자의 같은 쪽에 놓이고, 고리 접합 H 두 개는 CH2 다리 쪽(위)을 향한다. 오른쪽 exo adduct는 반대로 anhydride가 CH2 다리 쪽을 향하고 H가 아래를 향한다. 실제로는 endo adduct만 생긴다.*

## 원리

### 기하학적으로 본 endo와 exo

TS에서 평면인 diene과 평면인 dienophile이 평행하게 포개진다. 이때 EWG(예: CHO)가 diene 아래로 들어가면 endo TS, 바깥으로 비켜나 있으면 exo TS다. dienophile에 carbonyl 같은 전자 끄는 π 치환기가 있으면 보통 endo 첨가가 우세하다. 결과적으로 생성물에서는 새 이중 결합과 C=O 기가 분자의 같은 쪽에 놓인다. 다만 이것은 "선호"이지 "법칙"이 아니어서 두 stereoisomer가 섞여 나오는 경우도 많다.[^1] (출처: L13 p.21–22)

### orbital로 본 endo 선호: secondary orbital overlap

그 이유는 secondary orbital overlap이다. endo TS에서는 dienophile의 C=O 기가 diene 바로 아래에 놓여, 결합을 만들지 않는 diene의 "뒤쪽"(C2, C3)과 결합성으로 상호작용한다. 이 추가 안정화 덕분에 endo TS의 에너지가 낮아진다. (출처: L13 p.21)

슬라이드 p.29는 cyclopentadiene dimerization을 예로 이것을 orbital로 그린다. 두 cyclopentadiene이 만나면 endo-dicyclopentadiene이 생기고, 두 alkene이 서로 endo 관계에 놓인다. diene HOMO의 말단(C1, C4)과 dienophile LUMO의 결합성 겹침이 새 σ 결합을 만드는 **1차 상호작용**이다. 그런데 endo TS에서는 그것만이 아니다. dienophile 분자에 남은 π orbital이 diene의 C2, C3 lobe 바로 아래에 놓여 추가로 결합성 겹침을 한다. 이것이 **secondary orbital overlap**이다. 이 겹침은 결합으로 이어지지 않고 TS만 안정화하는 "보너스"이므로, 남은 π계를 diene 아래에 둘 수 있는 endo 경로가 선호된다(→ [frontier molecular orbital](프런티어%20분자%20오비탈.md)).[^2] (출처: L13 p.29)

![cyclopentadiene + maleic anhydride의 endo TS와 exo TS 3D 모델](../../figures/L13/da_endo_exo_ts_3d.svg)

*그림: 위가 cyclopentadiene($CH_2$ 다리가 맨 위), 아래가 maleic anhydride, 초록 점선이 생기는 C···C 결합(2.25 Å로 고정)이다. endo TS에서는 anhydride의 C=O 쪽이 diene π 계 밑으로 들어가 secondary orbital overlap을 하고, exo TS에서는 바깥쪽을 향한다. GFN2-xTB로는 endo가 약 2 kcal/mol 낮았다. 보충: xTB 구조는 GFN2-xTB로 계산한 모델이고, TS는 형성·절단 결합 길이를 고정해 최적화한 근사 구조다(진짜 안장점이 아니다).*

### endo는 kinetic product다

보충: endo가 kinetic product라는 증거는 가역적인 DA에서 나온다. cyclopentadiene 대신 furan을 maleic anhydride와 반응시키면 DA가 가역적으로 일어나 thermodynamic control에 이르고, 이때는 exo adduct가 얻어진다. exo가 더 안정한 이유는 다리 걸친 고리에서 anhydride 고리가 원자 하나짜리 다리(O 또는 CH2) 쪽을 향하는 것이 원자 두 개짜리 다리(C=C 쪽) 쪽을 향하는 것보다 steric hindrance가 작기 때문이다. 또 intramolecular DA에서는 두 반응 부위가 이미 묶여 있어 secondary orbital overlap의 도움이 덜 중요해지므로, 사슬이 접히기 편한 쪽을 따라 exo가 나오기도 한다. 즉 endo rule은 intermolecular·비가역 반응에서 가장 믿을 만하다(→ [kinetic control과 thermodynamic control](속도론적%20지배와%20열역학적%20지배.md), [retro-Diels–Alder reaction](../반응/역%20딜스-알더%20반응.md)). (보충 근거: Clayden p.884, 888–889) (출처: L13 p.22)

## 생성물로 옮기는 법

### "in"/"out" 번역 규칙

시험에서 가장 많이 쓰는 번역 규칙이다. diene을 [s-cis conformation](s-cis%20형태.md)으로 그리고 말단 치환기를 "in"/"out"으로 나눈다. (E)-diene이 s-cis conformation을 취하면 C1의 H는 diene "안쪽"을 향하고("in" 치환기), (E) 치환기는 "바깥쪽"을 향한다("out" 치환기). (출처: L14 p.16–17)

| TS | "out" 치환기와 EWG | "in" 치환기와 EWG |
|---|---|---|
| **endo** | **cis** | trans |
| exo | trans | cis |

(E)-1-치환 diene의 치환기는 "out"이므로 **endo 생성물에서 치환기와 EWG가 cis**다. 예를 들어 (E)-1-methoxybuta-1,3-diene + acrolein에서 regioselectivity만으로는 "ortho" 생성물(2-methoxycyclohex-3-ene-1-carbaldehyde)이라는 것까지만 알고, OMe와 CHO가 cis인지 trans인지는 모른다. endo TS에서는 "in" 치환기(H)와 CHO가 trans가 되므로 OMe와 CHO는 cis이고, 주생성물은 cis-2-methoxycyclohex-3-ene-1-carbaldehyde(racemic)다. exo TS였다면 OMe와 CHO는 trans였을 것이다(→ [Diels–Alder regioselectivity](딜스-알더%20위치선택성.md)). (출처: L14 p.16–17)

### 그리는 순서

p.23–24의 문제((E,E)-hexa-2,4-diene + acrolein의 endo 생성물 고르기)에서 슬라이드 p.24의 풀이는 이렇다. carbonyl이 diene 아래로 tucked under endo TS를 거치면 세 H가 한 면에 모이므로, CHO와 두 Me가 모두 cis인 all-cis 생성물이 생긴다. L14 p.17 하단의 "Recall" 예시도 같은 이야기를 한다. (E,E)-hexa-2,4-diene과 acrolein에서도 endo 생성물과 exo 생성물은 CHO가 두 methyl에 대해 어느 쪽을 향하는지로 구분된다. (출처: L13 p.23–24; L14 p.17)

보충: 교재는 이런 문제를 푸는 순서를 다음처럼 제시한다. (보충 근거: Clayden p.885) (출처: L13 p.23–24)

1. 먼저 평면 구조로 mechanism과 후보 생성물을 그리고 이미 아는 stereochemistry(여기서는 out/out → 두 Me cis)을 표시한다.
2. diene을 위에, dienophile을 아래에 겹쳐 그리되 C=O가 diene 밑으로 tucked under 놓는다.
3. 새 stereocenter가 될 탄소에 H를 모두 그려 넣는다.
4. 고리를 펴서 그리면 같은 방향을 향하던 H들이 모두 고리의 한 면에 모인다.
5. 나머지 치환기를 반대 면에 그린다.

이 순서를 따르면 슬라이드 p.24의 all-cis 답이 그대로 나온다.

## 예

- cyclopentadiene + maleic anhydride --[열]--> endo adduct만 (L13) (출처: L13 p.21)
- cyclopentadiene 2분자 --[상온]--> endo-dicyclopentadiene (L13) (출처: L13 p.18, p.29)
- cyclopentadiene + acrolein --[20 °C, 68 h]--> 5-norbornene-2-carbaldehyde (92%, endo로 그려짐) (L13) (출처: L13 p.16)
- (E,E)-hexa-2,4-diene + acrolein --[열]--> **all-cis** 2,5-dimethylcyclohex-3-ene-1-carbaldehyde. 두 Me는 "out"이라 서로 cis(stereospecificity)이고, endo라 CHO도 Me들과 cis다. (L13) (출처: L13 p.23–24)
- (E)-1-methoxybuta-1,3-diene + acrolein --[열]--> *cis*-2-methoxycyclohex-3-ene-1-carbaldehyde(racemic) (L14) (출처: L14 p.16–17)
- (E)-1-acetoxybuta-1,3-diene + (E)-crotonaldehyde: OAc("out")와 CHO가 endo로 cis (L14, L15, → [Diels–Alder regioselectivity](딜스-알더%20위치선택성.md)) (출처: L14 p.18–19; L15 p.3)
- **합성에서의 쓰임:** [cubane](큐베인.md) 합성에서 2-bromocyclopentadienone의 endo dimer는 두 C=C가 가까이 마주 보고 있어 다음 단계의 intramolecular photochemical [2+2]가 가능했다. (L14) (출처: L14 p.30)

## endo rule이 통하지 않는 곳

| 반응 | stereoselectivity |
|---|---|
| [photochemical \[2+2\] cycloaddition](../반응/광화학%202+2%20고리화%20첨가.md) | endo selectivity 없음, steric hindrance 최소 TS |
| [nitrone cycloaddition](../반응/나이트론%20고리화%20첨가.md) | exo 선호 |
| 가역적 DA (furan + maleic anhydride) | thermodynamic control로 더 안정한 exo |
| intramolecular DA | endo·exo 모두 가능, 사슬이 접히기 편한 쪽 |
| [\[6+4\] cycloaddition](../반응/6+4%20고리화%20첨가.md) | 슬라이드는 "endo"로 표시했으나 문헌(Houk 등)은 exo로 부른다. Clayden p.894는 "endo 관계"로 서술해 교재마다 기준이 다르다(검토 의견, 해당 문서 각주) |

(출처: L14 p.21, p.27; L15 p.16) 가역적 DA와 intramolecular DA 두 줄은 위 "endo는 kinetic product다"의 보충 내용이다.

## 흔한 오해

- **"endo는 치환기가 다리(CH2) 아래쪽, 안쪽에 있는 것"이라고 생각하기 쉽지만 사실은** endo는 dienophile의 π 치환기가 diene π계 아래에 놓이는 배향이다. 그래서 norbornene 생성물에서는 치환기가 새 C=C 쪽, 즉 CH2 다리의 반대쪽에 있다. (출처: L13 p.21–22)
- **"secondary orbital overlap이 새 결합을 만든다"고 생각하기 쉽지만 사실은** 결합으로 이어지지 않고 endo TS만 안정화하는 kinetic effect다. (출처: L13 p.21, p.29)
- **"endo = 치환기끼리 cis"라고 외우기 쉽지만 사실은** endo TS에서 cis가 되는 것은 diene의 **"out" 치환기**와 EWG다. "in" 치환기는 EWG와 trans가 된다. (E)-1-치환 diene에서는 치환기가 "out"이므로 endo 생성물에서 치환기와 EWG가 cis다. (출처: L14 p.17)
- **"endo는 100% 보존되는 stereospecificity"라고 생각하기 쉽지만 사실은** stereoselectivity라 혼합물이 생길 수 있다. (출처: L13 p.22, p.31)
- **"endo는 언제나 thermodynamic으로도 유리하다"고 생각하기 쉽지만 사실은** endo는 대개 덜 안정한 kinetic product다. 가역 조건(furan + maleic anhydride)에서는 더 안정한 exo가 얻어진다. (보충 근거: Clayden p.884)
- **"cycloaddition은 다 endo를 선호한다"고 생각하기 쉽지만 사실은** endo rule은 [4+2]의 이야기다. photochemical [2+2]에는 endo selectivity이 없고, nitrone cycloaddition은 exo를 선호한다. (출처: L14 p.27; L15 p.16)

## 관련 문서

- 반응: [Diels–Alder reaction](../반응/딜스-알더%20반응.md), [retro-Diels–Alder reaction](../반응/역%20딜스-알더%20반응.md), [photochemical \[2+2\] cycloaddition](../반응/광화학%202+2%20고리화%20첨가.md), [nitrone cycloaddition](../반응/나이트론%20고리화%20첨가.md), [\[6+4\] cycloaddition](../반응/6+4%20고리화%20첨가.md)
- 개념: [frontier molecular orbital](프런티어%20분자%20오비탈.md), [s-cis conformation](s-cis%20형태.md), [Diels–Alder regioselectivity](딜스-알더%20위치선택성.md), [stereospecificity와 stereoselectivity](입체특이성과%20입체선택성.md), [kinetic control과 thermodynamic control](속도론적%20지배와%20열역학적%20지배.md), [cubane](큐베인.md)
- 시약: [Lewis acid catalyst](../시약/루이스%20산%20촉매.md)

## 출처

- [L13 cycloaddition 1부](../../notes/L13_Cycloaddition_Part1.md) 6절, 7절 (p.16, p.18, p.21–24, p.29)
- [L14 cycloaddition 2부](../../notes/L14_Cycloaddition_Part2.md) 6절, 10절, 11절 (p.16–17, p.27, p.30)
- [L15 cycloaddition 3부](../../notes/L15_Cycloaddition_Part3.md) 0절, 15절 (p.3, p.16)

[^1]: 보충: endo 생성물은 kinetic product다. steric hindrance가 적은 exo 생성물이 thermodynamic으로 더 안정한 경우가 많아서, 고온이나 장시간(retro-DA가 가능한 가역 조건)에서는 exo 비율이 늘어날 수 있다. (보충 근거: Clayden p.884) (출처: L13 p.22) 또 [Lewis acid catalyst](../시약/루이스%20산%20촉매.md)는 일반적으로 endo selectivity도 높이는 것으로 알려져 있다. 다만 Clayden은 Lewis acid가 dienophile LUMO를 더 낮춰 반응을 빠르게 하고 LUMO 계수 차이를 키워 regioselectivity를 높인다는 점만 설명하며(보충 근거: Clayden p.891), endo selectivity 향상은 이 교재에서 확인되지 않는다. L14 슬라이드의 예도 regioselectivity만 보여 준다. (출처: L14 p.20)
[^2]: 슬라이드 p.29의 그림에는 아래쪽(dienophile 역할) cyclopentadiene의 orbital이 "LUMO of diene"이라고 적혀 있다. 그 분자가 화합물로서 diene이라는 뜻으로 읽어야 하며, 반응에서의 역할은 dienophile이다(그 C=C의 LUMO). (출처: L13 p.29)
