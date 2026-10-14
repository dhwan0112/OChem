---
aliases: [Cbz, CBz, Z, Z기, benzyloxycarbonyl, 벤질옥시카보닐, 벤질 카바메이트, BnOCOCl, 벤질 클로로포메이트]
분류: 시약
강의: [L12]
주제태그: [보호기, 아민, 카바메이트, 수소화분해]
tags: [분류/시약, 범위/Test2, 단원/보호기, 강의/L12, 시약유형/보호기, 주제/수소화분해, 주제/카바메이트]
---
# Cbz 보호기

> amine을 benzyl carbamate(RNH–CO–OCH₂Ph)로 가리는 [protecting group](../개념/보호기.md)이다. BnOCOCl과 염기로 씌우고, **H₂/Pd hydrogenolysis**(또는 HBr/AcOH)로 벗긴다.

## 개요

carbamate는 질소의 비공유 전자쌍을 C=O와 공명시켜 amine의 nucleophilicity와 염기성을 떨어뜨린다(→ [protecting group](../개념/보호기.md) 문서의 "왜 carbamate인가"). L12가 소개하는 carbamate 세 가지 가운데 Cbz(Z라고도 쓴다)는 [Boc](Boc%20보호기.md)와 함께 "대표 선수"로 나오며, 제거 조건이 수소화라는 점이 특징이다. (출처: L12 p.5, p.8)

## 도입

`RR'NH --[BnOCOCl(benzyl chloroformate), base]--> R'RN-CO-OCH2Ph`

chloroformate(Cl–CO–OR″)로 carbamate를 만드는 일반형의 한 예다. (출처: L12 p.8)

## 제거

Cbz는 H2/Pd [hydrogenolysis](../반응/수소화분해.md)로 벗기는 것이 기본이고(→ [Pd/C](Pd-C.md)), 산(HBr/AcOH)으로도 벗길 수 있다. Cbz를 hydrogenolysis하면 benzyl C–O 결합이 끊겨 toluene과 carbamic acid(RNH-COOH)가 생기고, carbamic acid는 스스로 CO2를 내놓으며 free amine이 된다.[^1] 이 "carbamic acid → CO2 + amine" 단계는 Boc, [Fmoc](Fmoc%20보호기.md)에서도 똑같이 마지막을 장식한다. (출처: L12 p.5, p.8)

![Cbz의 benzyl C–O 결합이 H2/Pd로 끊겨 carbamic acid와 toluene이 되는 hydrogenolysis](../../figures/L12/cbz_hydrogenolysis.svg)

그림: 보충(슬라이드에는 조건만 있다). H₂/Pd 조건에서 benzyl C–O 결합(빨강)이 끊기고, H₂의 수소(초록)가 양쪽 조각에 붙어 carbamic acid와 toluene이 된다. 금속 표면에서 일어나는 반응이라 굽은 화살표는 그리지 않았다. carbamic acid는 저절로 CO₂를 잃고 amine이 된다(이 단계의 화살표는 [Boc](Boc%20보호기.md) 문서의 두 번째 그림 참고). (보충 근거: Clayden p.557)

보충: carbamate는 ester와 amide의 "잡종"이지만 화학적 성질은 amide에 가깝다. 그래서 Cbz 자체는 묽은 산 수용액과 염기 수용액을 모두 견디고, 약점은 benzyl group 하나뿐이다. HBr/AcOH 조건이 통하는 이유도 benzyl group에 있다. 강산 HBr이 carbonyl 산소를 protonate하면, nucleophilicity가 좋은 Br⁻가 **benzyl 탄소를 [SN2](../반응/SN2%20반응.md)로 공격**해 BnBr을 떼어 내고 carbamic acid가 남는다. benzyl 자리는 SN2가 빠른 자리이기 때문이다. 이 점이 Boc와 대비된다. Boc는 t-butyl group이 SN1으로 떨어지므로 nucleophilic한 짝염기가 필요 없어 "아무 산"이나 되지만, Cbz는 Br⁻처럼 좋은 nucleophile이 있어야 산으로 벗겨진다. (보충 근거: Clayden p.556–558)

![protonate된 Cbz의 benzyl 탄소를 Br⁻가 SN2로 공격해 carbamic acid와 benzyl bromide가 되는 단계](../../figures/L12/cbz_hbr.svg)

그림: 보충. HBr이 carbonyl 산소를 protonation한 상태(빨강 O⁺)에서, Br⁻(파랑)의 전자쌍이 benzyl 탄소(빨강)를 CH2–O 결합의 뒤쪽에서 SN2로 공격하고, CH2–O 결합(빨강)의 전자는 산소로 간다. carbamic acid(초록이 새 C=O)와 benzyl bromide(초록이 새 C–Br)가 생긴다. (보충 근거: Clayden p.557)

## 선택성

- 수소화로 벗겨지므로, 산으로 벗기는 Boc나 염기로 벗기는 Fmoc와는 다른 조건으로 골라낼 수 있다(→ [orthogonal protection](../개념/직교%20보호.md)). Cbz는 Boc를 벗기는 TFA 정도의 산에는 견디므로, TFA로 Boc만 벗기고 Cbz를 남길 수 있다(위 보충). (출처: L12 p.5)
- [benzyl ether(OBn)](벤질%20에터%20보호기.md)도 H₂/Pd/C로 벗겨지므로 Cbz와 benzyl ether는 서로 orthogonal하지 않다. (출처: L12 p.5)
- SPPS의 N-protecting group으로는 잘 쓰지 않는다. 이유는 [peptide synthesis](../반응/펩타이드%20합성.md) 문서의 SPPS 절에 있다.

## 흔한 오해

- **"Cbz는 산에 절대 안 벗겨진다"고 생각하기 쉽지만 사실은** 슬라이드 표에 HBr/AcOH가 제거 조건으로 적혀 있다. (출처: L12 p.5)
- **"hydrogenolysis면 어떤 benzyl기든 남길 수 있다"고 생각하기 쉽지만 사실은** 같은 분자의 benzyl ether도 함께 끊긴다. (출처: L12 p.5)
- **"Cbz도 HBr/AcOH 같은 산으로 벗겨지니 Boc와 같은 원리"라고 생각하기 쉽지만 사실은** 경로가 다르다. Boc는 t-butyl cation이 SN1으로 떨어지므로 어떤 산이든 되지만, Cbz는 Br⁻가 benzyl 탄소를 SN2로 공격해야 하므로 nucleophilic한 짝염기를 가진 산(HBr)이 필요하다. 그래서 TFA로 Boc만 벗기고 Cbz를 남길 수 있다. (보충 근거: Clayden p.557–558)

## 관련 문서

- 시약: [Boc protecting group](Boc%20보호기.md), [Fmoc protecting group](Fmoc%20보호기.md), [Pd/C](Pd-C.md), [benzyl ether protecting group](벤질%20에터%20보호기.md), [TFA](TFA.md)
- 반응: [hydrogenolysis](../반응/수소화분해.md), [catalytic hydrogenation](../반응/촉매%20수소화.md), [peptide synthesis](../반응/펩타이드%20합성.md), [SN2 reaction](../반응/SN2%20반응.md)
- 개념: [protecting group](../개념/보호기.md), [orthogonal protection](../개념/직교%20보호.md)

## 출처

- [L12 protecting group](../../notes/L12_Protecting_Groups.md) 4절, 6절 (L12 p.5, p.8)

[^1]: 보충: Cbz hydrogenolysis의 생성물(toluene, CO2, amine)은 표준 교재 내용이며 슬라이드에는 조건만 나온다. (보충 근거: Clayden p.557)
