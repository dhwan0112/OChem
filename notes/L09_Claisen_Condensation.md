# L9. 클라이젠 축합 (Claisen Condensations)

<!-- wiki-links:start -->

> **관련 위키 문서** ([[위키 대문]])
> - 반응: [[교차 클라이젠 축합]], [[디크만 축합]], [[말론산 에스터 합성]], [[아세토아세트산 에스터 합성]], [[에스터 가수분해]], [[역알돌 반응]], [[친핵성 아실 치환]], [[클라이젠 축합]]
> - 시약: [[알콕사이드 염기]]
> - 개념: [[α-수소의 산도]], [[사면체 중간체]], [[엔올과 엔올레이트]]

<!-- wiki-links:end -->

> 이 강의 노트는 **뼈대**다. 강의 순서와 슬라이드 위치만 정리했고, 설명은 링크된 개념 문서에 있다.

## 개요

enolate의 세 번째 짝, "enolate + ester"를 다룬다. α-alkylation과 aldol에 이어 ester를 상대로 하면 1,3-dicarbonyl(β-keto ester, β-diketone)이 생긴다. 강의는 먼저 Claisen이 nucleophilic acyl substitution이라는 점을 확인하고, 자기 축합의 메커니즘에서 "생성물의 탈양성자화가 원동력"이라는 핵심 원리를 끌어낸다. 이어 같은 원리로 crossed Claisen(엔올화되지 않는 ester를 electrophile로)과 분자 내 Dieckmann condensation을 설명하고, 합성 설계 연습으로 마무리한다.

## 강의 흐름

### 1. Enolate가 할 수 있는 네 가지 일 (슬라이드 p.2, p.14)
- enolate + alkyl halide → α-alkylation, + aldehyde/ketone → aldol, + ester → 1,3-dicarbonyl(Claisen), + enone → Michael. Claisen의 C–C 형성은 가역(⇌)이다.
- → [[클라이젠 축합]], [[엔올레이트 알킬화]], [[알돌 반응]], [[마이클 반응]]

### 2. Claisen 반응은 결국 친핵성 아실 치환이다 (슬라이드 p.3)
- 첨가로 tetrahedral intermediate가 생긴 뒤 EtO⁻가 떨어진다. aldol은 "첨가", Claisen은 "첨가 후 제거".
- → [[친핵성 아실 치환]], [[사면체 중간체]], [[클라이젠 축합]] (C-/O-acylation 보충)

### 3. 자기 축합: ester 두 분자가 하나로 (슬라이드 p.4–7)
- 2 CH₃CO₂Et → ethyl acetoacetate(76%), ethyl pentanoate → 2-propyl-3-oxoheptanoate(77%).
- 원동력은 생성물 β-keto ester(pKa ~9)의 탈양성자화. 그래서 염기 1당량, 같은 alkoxide, α-H 2개 이상, 마지막 산 처리.
- 같은 β-keto ester 음이온이 Claisen에서는 종착점, acetoacetic ester alkylation에서는 출발점(p.7).
- → [[클라이젠 축합]], [[알콕사이드 염기]], [[아세토아세트산 에스터 합성]], [[α-수소의 산도]]

### 4. 교차 Claisen 축합: 짝을 골라 섞기 (슬라이드 p.8–11)
- 한쪽을 엔올화되지 않는 ester로: oxalate > formate > carbonate > (ethyl acetate) > benzoate.
- ester + carbonate/oxalate(p.9), ketone + oxalate/formate(p.10, 더 산성인 ketone이 enolate), benzoate + acetophenone이 aldol이 아니라 Claisen인 이유(p.11).
- → [[교차 클라이젠 축합]], [[말론산 에스터 합성]], [[역알돌 반응]]

### 5. 분자 내 Claisen: Dieckmann 축합 (슬라이드 p.12)
- diester → 고리형 β-keto ester. 고리 크기 = 카보닐 사이 CH₂ 수 + 1(1,6-diester → 5원, 1,7-diester → 6원).
- → [[디크만 축합]]

### 6. 연습: Claisen으로 합성 설계하기 (슬라이드 p.13)
- 1,3-dicarbonyl 사이 C–C를 끊어 "enolate 조각 + ester 조각"으로 나눈다.
- → [[교차 클라이젠 축합]] (합성 설계), [[디크만 축합]], 연습 문제 6, 7번

### 7. 정리 (슬라이드 p.14–15)
- 유형 셋(자기 축합, crossed, Dieckmann), 원리 하나(생성물의 탈양성자화).
- → [[클라이젠 축합]]

## 반응 요약표

| 반응 | 시약/조건 | 생성물 | 비고 |
|---|---|---|---|
| [[클라이젠 축합]] (ethyl acetate) | 2 CH₃CO₂Et, NaOEt; HCl | CH₃COCH₂CO₂Et (76%) | EtOH 증류 제거, 염기 1당량 (p.5) |
| [[클라이젠 축합]] (ethyl pentanoate) | NaOEt; CH₃CO₂H | ethyl 3-oxo-2-propylheptanoate (77%) | C2 라세미 (p.5) |
| [[교차 클라이젠 축합]] (ester + carbonate) | PhCH₂CO₂Et + (EtO)₂CO, NaOEt, EtOH | PhCH(CO₂Et)₂ (86%) | carbonate는 electrophile 전용 (p.9) |
| [[교차 클라이젠 축합]] (ester + oxalate) | CH₃(CH₂)₅CO₂Et + (CO₂Et)₂, EtONa, EtOH | EtO₂C–CO–CH(CO₂Et)–C₅H₁₁ (83%) | oxalate가 가장 반응성 큼 (p.9) |
| [[교차 클라이젠 축합]] (ketone + oxalate) | cyclohexanone, NaOEt; (CO₂Et)₂; H₃O⁺ | 2-(EtO₂C–CO–)cyclohexanone (67%) | ketone이 enolate (p.10) |
| [[교차 클라이젠 축합]] (ketone + formate) | cyclohexanone, HCO₂Et, EtO⁻; HCl/H₂O | 2-(hydroxymethylene)cyclohexanone | enol형으로 분리 (p.10) |
| [[교차 클라이젠 축합]] (ketone + benzoate) | PhCO₂Et + PhCOCH₃, NaOEt; H₃O⁺ | PhCOCH₂COPh | aldol보다 Claisen 우세 (p.11) |
| [[디크만 축합]] | RO₂C(CH₂)₄CO₂R, 1. RO⁻; 2. H⁺ | 2-(RO₂C)cyclopentanone + ROH | 5원 고리 (p.12) |

## 연습 문제

→ [L9 연습 문제](../practice/L09_Exercises.md)

## 출처

- 슬라이드: L9 (PDF p.1–15)
- 이 강의 PDF는 15쪽이며 슬라이드 하단 번호는 9~22번이다(PDF p.2 = 슬라이드 9). 이 노트와 개념 문서의 "p."는 모두 PDF 페이지 번호다. 표지 다음 슬라이드 2~8번은 PDF에 없다. 참고 교재는 Solomons 13판 19장, Clayden 2판 26장. (출처: L9 p.1)
