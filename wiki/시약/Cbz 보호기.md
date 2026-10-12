---
aliases: [Cbz, CBz, Z, Z기, benzyloxycarbonyl, 벤질옥시카보닐, 벤질 카바메이트, BnOCOCl, 벤질 클로로포메이트]
분류: 시약
강의: [L12]
주제태그: [보호기, 아민, 카바메이트, 수소화분해]
tags: [분류/시약, 범위/Test2, 단원/보호기, 강의/L12, 시약유형/보호기, 주제/수소화분해, 주제/카바메이트]
---
# Cbz 보호기

> 아민을 benzyl carbamate(RNH–CO–OCH₂Ph)로 가리는 [[보호기|protecting group]]이다. BnOCOCl과 염기로 씌우고, **H₂/Pd hydrogenolysis**(또는 HBr/AcOH)로 벗긴다.

## 개요

carbamate는 질소의 비공유 전자쌍을 C=O와 공명시켜 아민의 친핵성과 염기성을 떨어뜨린다(→ [[보호기]]의 "왜 carbamate인가"). L12가 소개하는 carbamate 세 가지 가운데 Cbz(CBz, Z라고도 쓴다)는 [[Boc 보호기|Boc]]와 함께 "대표 선수"로 나오며, 제거 조건이 수소화라는 점이 특징이다. (출처: L12 p.5, p.8)

## 도입

`RR'NH --[BnOCOCl(benzyl chloroformate), base]--> R'RN-CO-OCH2Ph`

chloroformate(Cl–CO–OR″)로 carbamate를 만드는 일반형의 한 예다. (출처: L12 p.8)

## 제거

Cbz는 H2/Pd [[수소화분해|hydrogenolysis]]로 벗기는 것이 기본이고(→ [[Pd-C|Pd/C]]), 산(HBr/AcOH)으로도 벗길 수 있다. Cbz를 hydrogenolysis하면 benzyl C–O 결합이 끊겨 toluene과 carbamic acid(RNH-COOH)가 생기고, carbamic acid는 스스로 CO2를 내놓으며 유리 아민이 된다.[^1] 이 "carbamic acid → CO2 + 아민" 단계는 Boc, [[Fmoc 보호기|Fmoc]]에서도 똑같이 마지막을 장식한다. (출처: L12 p.5, p.8)

보충: carbamate는 에스터와 아마이드의 "잡종"이지만 화학적 성질은 아마이드에 가깝다. 그래서 Cbz 자체는 묽은 산 수용액과 염기 수용액을 모두 견디고, 약점은 benzyl기 하나뿐이다. HBr/AcOH 조건이 통하는 이유도 benzyl기에 있다. 강산 HBr이 carbonyl 산소를 양성자화하면, 친핵성이 좋은 Br⁻가 **benzyl 탄소를 [[SN2 반응|SN2]]로 공격**해 BnBr을 떼어 내고 carbamic acid가 남는다. benzyl 자리는 SN2가 빠른 자리이기 때문이다. 이 점이 Boc와 대비된다. Boc는 t-butyl기가 SN1으로 떨어지므로 친핵성 짝염기가 필요 없어 "아무 산"이나 되지만, Cbz는 Br⁻처럼 좋은 nucleophile이 있어야 산으로 벗겨진다. (보충 근거: Clayden p.556–558)

## 선택성

- 수소화로 벗겨지므로, 산으로 벗기는 Boc나 염기로 벗기는 Fmoc와는 다른 조건으로 골라낼 수 있다(→ [[직교 보호]]). Cbz는 Boc를 벗기는 TFA 정도의 산에는 견디므로, TFA로 Boc만 벗기고 Cbz를 남길 수 있다(위 보충). (출처: L12 p.5)
- [[벤질 에터 보호기|benzyl ether(OBn)]]도 H₂/Pd/C로 벗겨지므로 Cbz와 benzyl ether는 서로 직교하지 않는다. (출처: L12 p.5)
- SPPS의 N-보호기로는 잘 쓰지 않는다. 이유는 [[펩타이드 합성]]의 SPPS 절에 있다.

## 흔한 오해

- **"Cbz는 산에 절대 안 벗겨진다"고 생각하기 쉽지만 사실은** 슬라이드 표에 HBr/AcOH가 제거 조건으로 적혀 있다. (출처: L12 p.5)
- **"hydrogenolysis면 어떤 benzyl기든 남길 수 있다"고 생각하기 쉽지만 사실은** 같은 분자의 benzyl ether도 함께 끊긴다. (출처: L12 p.5)
- **"Cbz도 HBr/AcOH 같은 산으로 벗겨지니 Boc와 같은 원리"라고 생각하기 쉽지만 사실은** 경로가 다르다. Boc는 t-butyl cation이 SN1으로 떨어지므로 어떤 산이든 되지만, Cbz는 Br⁻가 benzyl 탄소를 SN2로 공격해야 하므로 친핵성 짝염기를 가진 산(HBr)이 필요하다. 그래서 TFA로 Boc만 벗기고 Cbz를 남길 수 있다. (보충 근거: Clayden p.557–558)

## 관련 문서

- 시약: [[Boc 보호기]], [[Fmoc 보호기]], [[Pd-C|Pd/C]], [[벤질 에터 보호기]], [[TFA]]
- 반응: [[수소화분해]], [[촉매 수소화]], [[펩타이드 합성]], [[SN2 반응]]
- 개념: [[보호기]], [[직교 보호]]

## 출처

- [L12 보호기](../../notes/L12_Protecting_Groups.md) 4절, 6절 (L12 p.5, p.8)

[^1]: 보충: Cbz hydrogenolysis의 생성물(toluene, CO2, 아민)은 표준 교재 내용이며 슬라이드에는 조건만 나온다. (보충 근거: Clayden p.557)
