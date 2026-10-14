---
aliases: [s-cis conformation, s-cis, s-trans, s-시스, cisoid, 다이엔 형태]
분류: 개념
강의: [L13]
주제태그: [형태, 다이엔, 딜스-알더]
tags: [분류/개념, 범위/Test2, 단원/고리화-첨가, 강의/L13, 개념유형/구조-형태, 주제/다이엔, 주제/딜스-알더, 주제/형태]
---
# s-cis 형태

> Diene의 두 C=C가 가운데 단일 결합(C2–C3)을 기준으로 **같은 쪽**을 향한 conformation. [Diels–Alder reaction](../반응/딜스-알더%20반응.md)은 이 conformation의 diene만 할 수 있다.

## 개요

diene에는 전자적 성질 말고도 중요한 조건이 하나 더 있다. 바로 모양이다. butadiene의 C2–C3 단일 결합은 회전할 수 있어서 두 가지 conformation을 오간다("s"는 single bond의 s다). 두 C=C가 반대쪽을 향한 **s-trans** conformation은 더 안정하지만, C1과 C4가 멀리 떨어져 있어 dienophile의 양 끝에 동시에 닿을 수 없다. 두 C=C가 같은 쪽을 향한 **s-cis** conformation에서만 C1과 C4가 가까워져 반응할 수 있다. 비유하자면 dienophile을 양손으로 잡으려면 두 팔을 같은 방향으로 뻗어야 하는 셈이다. (출처: L13 p.15)

## 원리

두 conformation은 빠르게 서로 바뀌므로 s-cis 분자가 반응해 없어지면 평형이 다시 채워 준다. 하지만 butadiene은 상온에서 겨우 **약 1%**만 s-cis conformation으로 존재한다(슬라이드 수치). 반응할 수 있는 conformation의 비율이 반응 속도에 그대로 반영된다. 예를 들어 butadiene(s-cis) + methyl acrylate는 methyl cyclohex-3-ene-1-carboxylate를 준다. (출처: L13 p.15)

보충: s-trans가 더 안정한데도 반응이 되는 것은 C2–C3 회전 장벽이 약 30 kJ/mol로 작아서 s-cis로 넘어가는 일이 상온에서도 빠르기 때문이다. 같은 논리로 치환기가 s-cis를 방해하는지 돕는지가 속도를 바꾼다. (Z,Z)-hexa-2,4-diene처럼 말단 치환기가 "in" 자리에 놓이면 s-cis에서 두 치환기가 부딪혀 butadiene보다 느리고, (E,E)-hexa-2,4-diene("out" 치환기)은 butadiene과 비슷하며, 2,3-dimethylbutadiene처럼 가운데 치환기는 오히려 s-trans를 불안정하게 해서 더 빠르다. (보충 근거: Clayden p.879; Wade p.687) (출처: L13 p.15)

![butadiene의 s-trans와 s-cis conformation: s-cis만 methyl acrylate와 DA 반응을 할 수 있다](../../figures/L13/s_cis_s_trans.svg)

그림: 초록색은 회전하는 C2–C3 단일 결합, 파란색은 diene의 π 결합, 빨간색은 dienophile(methyl acrylate)의 π 결합이다. 왼쪽 s-trans는 더 안정하지만 C1과 C4가 멀어 dienophile의 양 끝에 동시에 닿지 못한다. C2–C3 결합이 빠르게 회전해 s-cis가 되면 C1과 C4가 가까워지고, 주황색 굽은 화살표 셋이 기본 DA 그림(→ [Diels–Alder reaction](../반응/딜스-알더%20반응.md))과 같은 방향으로 돌며 고리가 닫힌다.

## 고정된 diene

그렇다면 처음부터 s-cis로 묶여 있는 diene은 어떨까? 예상대로 반응성이 매우 크다. cyclopentadiene, furan, cyclohexa-1,3-diene, 1,2-dimethylenecyclohexane("exo-methylene" diene)은 고리 때문에 s-cis로 고정되어 있어서 사슬형 diene보다 훨씬 반응성이 크다. 예를 들어 cyclopentadiene + acrolein은 20 °C에서 68 h 만에 5-norbornene-2-carbaldehyde를 92%로 준다. 슬라이드에서는 CHO가 CH2 다리의 endo으로 그려져 있다(→ [endo rule](endo%20규칙.md)). (출처: L13 p.16)

반대로 3-methylenecyclohexene이나, 두 C=C가 서로 다른 고리에 걸쳐 transoid로 고정된 bicyclic diene처럼 s-trans로 묶여 있는 diene은 아무리 가열해도 DA 반응을 할 수 없다. s-cis conformation을 취할 수 없는 diene은 DA 반응에 참여하지 못한다. (출처: L13 p.16)

| 고정 conformation | 예 | DA 반응성 |
|---|---|---|
| s-cis로 고정 | cyclopentadiene, furan, cyclohexa-1,3-diene, 1,2-dimethylenecyclohexane | 매우 큼 |
| s-trans로 고정 | 3-methylenecyclohexene, 두 C=C가 다른 고리에 transoid로 걸친 bicyclic diene | 가열해도 반응하지 않음 |

보충: s-trans 고정 diene이 안 되는 이유는 "두 끝이 멀어서"만이 아니다. DA에서 diene 가운데의 σ 결합(C2–C3)은 생성물의 새 π 결합이 되고, 그 σ 결합의 conformation(s-cis/s-trans)가 그대로 새 C=C의 cis/trans이 된다. s-trans로 반응한다면 6원 고리 안에 trans C=C가 생겨야 하는데, 이것은 불가능한 구조다. (보충 근거: Clayden p.880) (출처: L13 p.16)

s-cis 고정 diene인 cyclopentadiene은 반응성이 너무 커서 상온에서 스스로 dimer를 만든다(→ [retro-Diels–Alder reaction](../반응/역%20딜스-알더%20반응.md)). (출처: L13 p.18)

## 입체화학에서의 쓰임: "in"과 "out"

diene을 s-cis로 그리면 말단 탄소(C1, C4)의 치환기는 고리 안쪽을 향하는 **"in"** 자리와 바깥쪽을 향하는 **"out"** 자리 가운데 하나에 놓인다. (E)-치환기는 "out", (Z)-치환기는 "in"이다. "in" 둘, "out" 둘은 각각 생성물에서 1,4-cis가 되고, "in" 하나와 "out" 하나는 trans가 된다(자세한 예는 [Diels–Alder reaction](../반응/딜스-알더%20반응.md)의 stereospecificity). [endo rule](endo%20규칙.md)을 생성물로 옮길 때도 이 구분이 필요하다. (출처: L13 p.20; L14 p.17)

## 흔한 오해

- **"butadiene은 그냥 diene이니 언제든 반응한다"고 생각하기 쉽지만 사실은** s-cis conformation일 때만 반응하고, 상온에서 s-cis인 분자는 약 1%뿐이다. s-trans로 고정된 diene(3-methylenecyclohexene 등)은 아예 반응하지 않고, s-cis로 고정된 cyclopentadiene은 상온에서도 잘 반응한다. (출처: L13 p.15–16)
- **"s-cis/s-trans는 cis/trans isomer다"라고 생각하기 쉽지만 사실은** 단일 결합 회전으로 바뀌는 **conformation**이지, 이중 결합의 E/Z 같은 configurational isomer가 아니다.

## 관련 문서

- 반응: [Diels–Alder reaction](../반응/딜스-알더%20반응.md), [retro-Diels–Alder reaction](../반응/역%20딜스-알더%20반응.md)
- 개념: [endo rule](endo%20규칙.md), [stereospecificity와 stereoselectivity](입체특이성과%20입체선택성.md), [Diels–Alder regioselectivity](딜스-알더%20위치선택성.md)

## 출처

- [L13 cycloaddition 1부](../../notes/L13_Cycloaddition_Part1.md) 5절, 6절 (p.15–16, p.18, p.20)
- [L14 cycloaddition 2부](../../notes/L14_Cycloaddition_Part2.md) 6절 (p.17)
