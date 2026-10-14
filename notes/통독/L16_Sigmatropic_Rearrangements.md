# L16. 시그마트로픽 자리옮김 (Sigmatropic rearrangements)

> **통독본**: 2026-10-12 재구성 직전의 강의별 전체 노트(교과서 보강 포함)를 그대로 보존한 사본이다. 강의 흐름대로 한 번에 읽을 때 쓴다. 이후의 수정과 보충은 개념 문서에만 반영되므로, **최신 내용은 개념 문서**가 기준이다. 뼈대 노트: [L16 뼈대](../L16_Sigmatropic_Rearrangements.md) · [위키 대문](../../wiki/위키%20대문.md)



> **관련 위키 문서** ([위키 대문](../../wiki/위키%20대문.md))
> - 반응: [1,5-hydrogen shift](../../wiki/반응/1,5-수소%20이동.md), [sigmatropic rearrangement](../../wiki/반응/시그마트로픽%20자리옮김.md), [Cope rearrangement](../../wiki/반응/코프%20자리옮김.md), [Claisen rearrangement](../../wiki/반응/클라이젠%20자리옮김.md)



> 이 노트는 슬라이드 공개 전에 Clayden 2판 35장과 Wade 8판으로 만든 **예습판**이다. 강의 슬라이드가 나오면 슬라이드 기준으로 다시 정리한다. 슬라이드와 다르면 슬라이드를 따른다.

CM3121 Advanced Organic Chemistry (10/16 강의 예습)

## 개요

[L13](L13_Cycloaddition_Part1.md)에서 pericyclic 반응을 세 갈래로 나눴다. cycloaddition, 전자고리화 반응(electrocyclic reaction), 시그마트로픽 sigmatropic rearrangement이다. L13–L15는 첫 번째 갈래만 다뤘고, 이 노트는 세 번째 갈래를 다룬다. 두 번째 갈래는 [L17](L17_Electrocyclic_Reactions.md)에서 다룬다.

시그마트로픽 자리옮김은 이름 그대로 **σ 결합 하나가 자리를 옮기는** 반응이다. 한쪽에서 σ 결합이 끊어지는 동시에 다른 곳에서 새 σ 결합이 생기고, π 결합들은 그에 맞춰 위치를 바꾼다. cycloaddition처럼 전자가 고리를 따라 돌고, 이온성 intermediate가 없으며, 한 단계로 끝난다. 다른 점은 굽은 화살표 하나가 π 결합이 아니라 **σ 결합에서 출발한다**는 것이다.

이 노트는 다음 질문을 차례로 따라간다. 이름의 숫자 [i,j]는 무엇을 세나? 가장 중요한 [3,3] Claisen, Cope은 왜 *E* alkene을 주나? Woodward–Hoffmann 규칙으로는 어떻게 "허용"을 판정하나? 규칙이 방향을 알려 주지 않는다면 반응은 왜 한쪽으로만 가나? 마지막으로 [2,3] 자리옮김과 수소 이동([1,5]H 등)을 보고, 수소가 몇 칸 옮기느냐에 따라 초면/대면이 어떻게 바뀌는지 정리한다. (출처: Clayden p.909)

## 1. 시그마트로픽 자리옮김이란 무엇인가

> 개념 문서: [sigmatropic rearrangement](../../wiki/반응/시그마트로픽%20자리옮김.md)

### 1.1 세 갈래를 σ 결합 수로 가르기

세 갈래는 반응 전후 **σ 결합 수의 변화(Δσ)**로 깔끔하게 나뉜다.[^1]

| 갈래 | 무슨 일이 일어나나 | Δσ |
|---|---|---|
| cycloaddition | 새 σ 결합 둘이 생긴다(역반응이면 둘이 끊어진다) | ±2 |
| 시그마트로픽 자리옮김 | σ 결합 하나가 생기는 동시에 하나가 끊어진다 | 0 |
| 전자고리화 반응 | 콘쥬게이션 π계 양 끝을 잇는 σ 결합 하나가 생긴다(또는 끊어진다) | ±1 |

Δσ = 0이라는 것은 분자식도 그대로, 결합 개수도 그대로라는 뜻이다. 그래서 시그마트로픽 반응은 늘 **자리옮김(이성질화)**이다. (출처: Clayden p.922)

### 1.2 [i,j] 표기: 옛 결합과 새 결합 사이를 센다

[3,3], [2,3], [1,5] 같은 숫자는 원자 수도 전자 수도 아니고 **옛 σ 결합과 새 σ 결합의 위치 관계**다. 세는 법은 다음과 같다. (출처: Clayden p.910)

1. 끊어지는 옛 σ 결합의 양 끝 원자에 각각 1번을 붙인다.
2. 각 끝에서 사슬을 따라 2, 3, …으로 센다.
3. 새 σ 결합의 양 끝이 몇 번인지 읽는다. 그 두 숫자가 [i,j]다.

예를 들어 allyl 바이닐 ether CH2=CH–O–CH2–CH=CH2에서 끊어지는 것은 O–CH2 결합이다. O 쪽으로 O(1)–CH(2)=CH2(3), C 쪽으로 CH2(1)–CH(2)=CH2(3)이고, 새 결합은 두 3번 탄소 사이에 생기므로 [3,3]이다.

이렇게 세면 **transition state(TS) 고리의 크기 = i + j**라는 편리한 관계가 생긴다. [3,3]은 6원자 고리 TS, [2,3]은 5원자 고리 TS, [1,5]도 6원자 고리 TS를 거친다.[^2] (출처: Clayden p.917, p.919)

### 1.3 cycloaddition의 대괄호와 혼동하지 말 것

cycloaddition의 [4+2]는 두 성분 각각의 **원자 수**를 더하기로 쓴 것이고([L15](L15_Cycloaddition_Part3.md) 15.2절의 [3+2]처럼), 시그마트로픽의 [3,3]은 쉼표로 쓴 **위치 번호**다. 어느 쪽이든 허용 여부는 대괄호 숫자가 아니라 **전자 수와 초면/대면**으로 판정한다(→ 4절). (출처: Clayden p.894, p.910)

## 2. Claisen rearrangement: 처음 발견된 [3,3]

> 개념 문서: [Claisen rearrangement](../../wiki/반응/클라이젠%20자리옮김.md), [acetal formation](../../wiki/반응/아세탈%20형성.md)

### 2.1 방향족 Claisen rearrangement

최초의 시그마트로픽 자리옮김은 allyl 아릴 ether를 용매 없이 가열했을 때 *ortho*-allylphenol이 생긴 반응이다. 이것이 Claisen rearrangement이다.

- 전체: PhO–CH2–CH=CH2 --[가열]--> 2-allylphenol

반응은 두 단계다.

1. **[3,3] 시그마트로픽 단계(페리고리):** O–CH2 σ 결합이 끊어지면서 allyl group의 말단 탄소가 benzene 고리의 *ortho* 탄소와 결합한다. 이 단계의 생성물은 방향족성을 잃은 cyclohexadiene온이다.
2. **양성자 이동(이온성):** *ortho* 탄소의 H가 떨어지고 산소가 양성자를 받아 방향족 phenol로 돌아온다(keto → enol tautomerization). 방향족성 회복이 이 단계의 추진력이다.

(출처: Clayden p.909–910)

![allyl phenyl ether의 [3,3] 단계: 굽은 화살표 세 개가 6원자 고리를 돌아 cyclohexadienone이 된다](../../figures/L16/claisen_aromatic.svg)

*그림: 빨간색은 끊어지는 O–CH2 σ 결합, 초록색은 새로 생긴 C–C σ 결합, 주황색 굽은 화살표는 전자쌍의 이동이다. (1) benzene 고리의 *ipso*=*ortho* π 전자가 *ortho* 탄소와 allyl 말단 탄소 사이의 새 σ 결합이 되고, (2) allyl C=C π 전자가 CH2–CH 사이로 옮겨 새 π 결합이 되며, (3) O–CH2 σ 전자가 C–O 사이로 옮겨 C=O가 된다. 세 화살표는 한 단계에서 동시에 일어난다. 생성물은 방향족성을 잃은 cyclohexadienone이고, 이어지는 이온성 양성자 tautomerization으로 2-allylphenol이 된다. 산소에 붙어 있던 CH2가 아니라 반대쪽 끝 CH2가 고리에 붙는다는 점(inside out)도 그림에서 확인할 수 있다. Clayden p.909의 그림을 따랐다.*

### 2.2 메커니즘의 증거: allyl group이 "뒤집혀" 붙는다

이 메커니즘이 맞다는 것을 어떻게 알까? allyl group이 비대칭이면 산소에 붙어 있던 탄소가 아니라 **반대쪽 끝 탄소**가 고리에 붙는다. Clayden은 프레닐(3-methyl뷰트-2-엔일) ether PhO–CH2–CH=CMe2를 가열하면 2-(1,1-dimethylallyl)phenol, 즉 CMe2가 고리에 붙고 CH=CH2가 남은 생성물이 생긴다는 예를 든다. allyl group이 "안팎이 inside out" 것인데, 이는 산소에서 떨어진 allyl cation이 아무 끝으로나 붙는 단계적 경로로는 설명하기 어렵고 6원자 고리 TS를 거치는 협동 경로로는 자연스럽다. (출처: Clayden p.910)

### 2.3 지방족 Claisen rearrangement

같은 반응은 방향족 고리 없이도 일어난다. 가장 단순한 예는 다음과 같다.

- CH2=CH–O–CH2–CH=CH2 --[가열, [3,3]]--> OHC–CH2–CH2–CH=CH2 (펜트-4-enal)

이를 지방족 Claisen rearrangement, 또는 Claisen-Cope 자리옮김이라고 부른다. 생성물의 공통점은 **γ,δ-unsaturated carbonyl 화합물**이라는 것이다. carbonyl 탄소에서 α, β, γ, δ로 세면 C=C가 γ와 δ 사이에 놓인다. 합성에서 γ,δ-unsaturated carbonyl이 필요하면 Claisen 자리옮김을 떠올리라는 것이 Clayden의 조언이다. (출처: Clayden p.910, p.912)

![allyl vinyl ether의 [3,3] Claisen rearrangement: 굽은 화살표 세 개가 6원자 고리를 돌아 pent-4-enal이 된다](../../figures/L16/claisen_aliphatic.svg)

*그림: 빨간색은 끊어지는 옛 σ 결합(O–CH2), 초록색은 새로 생긴 σ 결합(C–C), 주황색 굽은 화살표는 전자쌍의 이동이다. 화살표 셋은 같은 방향(반시계)으로 돈다. (1) vinyl 쪽 C=C π 전자가 두 말단 탄소 사이의 새 σ 결합이 되고, (2) allyl 쪽 C=C π 전자가 CH2–CH 사이로 옮겨 새 π 결합이 되며, (3) O–CH2 σ 전자가 O–C 사이로 옮겨 C=O가 된다. 생성물을 출발물과 같은 고리 모양으로 그려 두었으므로 어떤 결합이 바뀌었는지 바로 비교할 수 있다. 옛 결합 양 끝을 1로 두고 세면 새 결합 양 끝이 모두 3이라 [3,3]이다. Clayden p.910의 그림을 따랐다.*

### 2.4 allyl 바이닐 ether는 어떻게 만드나

allyl 쪽은 쉽다. allyl alcohol은 안정하고 만들기 쉽다. 문제는 바이닐 쪽이다. "바이닐 alcohol"은 acetaldehyde의 enol이라 병에 담아 둘 수 없다.

해결책은 **acetal 교환**이다. aldehyde의 acetal(예: MeCH(OMe)2)과 allyl alcohol을 산 propanoic acid EtCO2H와 함께 가열한다.

1. **acetal 교환(S<sub>N</sub>1형):** protonate된 OMe가 methanol로 떨어져 oxocarbenium 이온이 생기고, allyl alcohol이 그 자리에 들어간다. methanol은 혼합물에서 가장 휘발성이 커서 증류로 빠져나가며 평형을 오른쪽으로 민다.
2. **제거(E1형):** 남은 OMe가 다시 protonate되어 떨어지고, oxocarbenium 이온에서 α-H가 빠져 바이닐 ether가 된다.
3. **[3,3] 자리옮김:** 가열하면 그 자리에서 Claisen 자리옮김이 일어난다. allyl 바이닐 ether를 따로 분리할 필요가 없다. 조금만 생겨도 곧바로 자리옮김해 빠져나가기 때문이다.

propanoic acid을 쓰는 이유는 끓는점이 높아 혼합물 전체를 높은 온도에서 평형시킬 수 있기 때문이다.[^3] (출처: Clayden p.911)

같은 전략은 다른 carbonyl 화합물에도 통한다. 출발물만 바꾸면 된다. (출처: Clayden p.911–912)

| acetal류 출발물 | [3,3] 생성물 |
|---|---|
| aldehyde의 acetal | γ,δ-unsaturated aldehyde |
| ketone의 acetal | γ,δ-unsaturated ketone |
| orthoester RC(OMe)3 | γ,δ-unsaturated ester |
| orthoamide(예: DMF dimethyl acetal, "amide acetal") | γ,δ-unsaturated amide |

(→ acetal 화학은 [L12](L12_Protecting_Groups.md) protecting group 문서의 acetal 부분 참고)

## 3. 의자형 transition state: 왜 *E* alkene이 생기나

> 개념 문서: [Claisen rearrangement](../../wiki/반응/클라이젠%20자리옮김.md)

### 3.1 6원자 고리 TS는 의자 모양이다

[3,3] 자리옮김의 TS는 cyclohexane처럼 **chair-like**이다. 이 모양에서는 새 σ 결합을 만들 두 p 오비탈이 서로 정면으로 마주 보고, 새 π 결합 두 개를 만들 오비탈들도 처음부터 평행하게 놓인다. 그래서 오비탈 겹침이 좋다. 이 그림은 특정한 프런티어 오비탈을 나타낸 것이 아니라 겹침의 기하만 보여 주는 것이다. (출처: Clayden p.910)

### 3.2 치환기는 적도 자리로 간다

산소 옆 포화 탄소(옛 σ 결합의 탄소 쪽 끝)에 치환기 R이 있으면 새로 생기는 C=C는 **트랜스(*E*)**가 강하게 우세하다. 이유는 [L13](L13_Cycloaddition_Part1.md)에서 본 stereospecificity과 같은 결의 논리다.

1. 의자형 TS에서 R은 cyclohexane 치환기처럼 축(axial) 또는 equatorial 자리에 놓일 수 있다.
2. 적도 자리가 입체적으로 유리하므로 R은 적도 자리를 택한다.
3. R은 그 자리를 유지한 채 생성물로 넘어가고, 적도 R과 사슬의 나머지가 새 C=C의 반대쪽에 놓여 *E* alkene이 된다.

즉 생성물의 트랜스 기하는 **출발물이 택한 형태와 TS에 이미 들어 있다**. intermediate가 없으니 그 사이에 바뀔 틈도 없다. (출처: Clayden p.910–911)

예: MeCH(OMe)2 + CH2=CH–CH(OH)–R --[EtCO2H, 가열]--> OHC–CH2–CH2–CH=CH–R (*E*) (출처: Clayden p.911)

![Claisen rearrangement의 chair형 transition state: R이 equatorial 자리를 택해 새 C=C가 E가 된다](../../figures/L16/claisen_chair_e.svg)

*그림: Clayden처럼 출발물을 chair형 TS와 같은 모양으로 그렸다. 빨간색은 끊어지는 O–C σ 결합, 파란색은 equatorial 자리의 R이고, 같은 탄소의 H는 axial 자리(아래쪽 세로선)에 있다. 주황색 화살표 셋은 지방족 Claisen과 같다. 오른쪽은 원자 배치를 그대로 둔 채 결합만 바꾼 생성물이며, 초록색은 새 C–C σ 결합과 새 C=C다. equatorial R과 사슬의 나머지(CH2 쪽)가 새 C=C의 반대쪽에 놓이므로 *E* alkene이 된다. 보충: R이 axial이었다면 *Z*가 되었을 것이다. 그림을 단순하게 하려고 말단 CH2 두 개는 묶음 라벨(H2C, CH2)로 적었다. Clayden p.911의 그림을 따랐다.*

![hexa-1,5-diene Cope rearrangement의 chair TS와 boat TS 3D 모델](../../figures/L16/cope_chair_boat_ts_3d.svg)

*그림: 두 allyl 조각(위/아래)이 2.00 Å(초록 점선)에서 결합을 주고받는다. chair TS는 두 allyl의 가운데 탄소가 서로 반대쪽으로 꺾이고, boat TS는 같은 쪽으로 꺾여 가려진(eclipsed) 상호작용이 생긴다. GFN2-xTB로 boat가 약 8 kcal/mol 높았다(실험값 약 6 kcal/mol). Claisen rearrangement도 같은 chair TS를 거친다. 보충: xTB 구조는 GFN2-xTB로 계산한 모델이고, TS는 형성·절단 결합 길이를 고정해 최적화한 근사 구조다(진짜 안장점이 아니다).*

## 4. Woodward–Hoffmann 규칙으로 [3,3]을 판정하기

> 개념 문서: [Claisen rearrangement](../../wiki/반응/클라이젠%20자리옮김.md), [sigmatropic rearrangement](../../wiki/반응/시그마트로픽%20자리옮김.md), [Woodward–Hoffmann rules](../../wiki/개념/우드워드-호프만%20규칙.md)

### 4.1 왜 FMO보다 Woodward–Hoffmann인가

cycloaddition은 두 분자가 공간을 사이에 두고 만나므로 한쪽 HOMO와 다른 쪽 LUMO를 겹쳐 보면 됐다([L14](L14_Cycloaddition_Part2.md) 1–2절). 그런데 [3,3] 자리옮김은 한 분자 안에서 일어나고 성분이 **셋**이다. 콘쥬게이션되지 않은 π 결합 두 개, 그리고 그 둘을 잇는 사슬 속 σ 결합 하나다. 이런 경우에는 FMO보다 Woodward–Hoffmann 규칙이 깔끔하다. (출처: Clayden p.912)

규칙은 L13 8절과 같다. **열적 페리고리 반응에서는 (4q+2)s 성분 수와 (4r)a 성분 수의 합이 홀수여야 한다.** (출처: Clayden p.892, p.912)

### 4.2 여섯 단계 절차

Clayden이 cycloaddition에 쓴 절차를 그대로 적용한다. (출처: Clayden p.912–913)

1. 메커니즘을 그린다(allyl 바이닐 ether → γ,δ-unsaturated aldehyde).
2. 성분을 고른다. 메커니즘에 참여하는 결합은 모두 넣고, 나머지는 넣지 않는다. → π2(C=C), σ2(O–C), π2(C=C)
3. 의자형 TS 모양으로 3차원 그림을 그리고 **성분의 끝에만** 오비탈을 그린다.
4. 새 결합이 생길 곳끼리 점선으로 잇는다.
5. 각 성분에 s 또는 a를 붙인다. Clayden의 그림에서는 π2s, σ2a, π2a가 된다.
6. 센다. (4q+2)s는 π2s 하나, (4r)a는 없다. 합 = 1(홀수) → **열적 허용**. π2a와 σ2a는 세는 대상이 아니다.

### 4.3 σ 결합의 s와 a는 어떻게 정하나

π 결합은 쉽다. 두 새 결합이 옛 π 결합의 같은 면에서 생기면 s, 반대 면이면 a다. σ 결합은 "면"이 분명하지 않으므로 다른 기준을 쓴다. sp3 오비탈의 **큰 로브로 반응하면 retention, 작은 로브로 반응하면 inversion**이라고 부르고,

- 양 끝 모두 보존이거나 양 끝 모두 반전이면 **σ2s**
- 한쪽 끝은 보존, 다른 끝은 반전이면 **σ2a**

로 정한다. (출처: Clayden p.913)

### 4.4 점선을 다르게 이어도 결론은 같다

4단계에서 점선 하나를 다르게 이으면 σ 결합이 σ2s로 바뀌는 대신 π 결합 하나가 π2a로 바뀐다. 그래도 (4q+2)s는 여전히 하나뿐이라 합은 1이고, 반응은 여전히 허용이다. 즉 **꼬리표 붙이는 방식은 여러 가지일 수 있지만 셈의 결과(홀짝)는 바뀌지 않는다**. 시험에서 "s/a를 내가 붙인 것과 다르게 붙였는데 틀렸나?"라고 걱정할 필요가 없는 이유다.[^4] (출처: Clayden p.913)

## 5. 방향: 규칙은 "허용"만 말하고 "어느 쪽"은 말하지 않는다

> 개념 문서: [Claisen rearrangement](../../wiki/반응/클라이젠%20자리옮김.md), [sigmatropic rearrangement](../../wiki/반응/시그마트로픽%20자리옮김.md)

### 5.1 Claisen은 왜 늘 carbonyl 쪽으로 가나

오비탈 대칭은 [3,3] 자리옮김이 허용된다는 것만 알려 준다. 정반응이 허용이면 역반응도 허용이다. 그런데 Claisen 자리옮김은 늘 carbonyl 화합물 쪽으로 간다. 왜일까?

[L10](L10_Enol_and_Enamine.md)의 keto-enol 평형을 떠올리면 된다. keto형은 **C=O π + C–C σ**, enol형은 **C=C π + C–O σ** 조합을 가지며, 앞의 조합이 더 안정해서 keto형이 우세하다. allyl 바이닐 ether(C=C + C–O)와 γ,δ-unsaturated carbonyl(C=O + C–C)의 관계가 정확히 이와 같다. **carbonyl 생성이 반응을 오른쪽으로 민다.** (출처: Clayden p.913)

### 5.2 판정 순서 정리

시그마트로픽 반응 문제를 풀 때는 두 질문을 따로 묻는다.

1. **허용되는가?** → Woodward–Hoffmann(또는 FMO)
2. **어느 쪽이 유리한가?** → 열역학(carbonyl 생성, 고리 긴장 해소, 더 치환된 alkene, 콘쥬게이션, anion 안정화 등)

이 구분은 [L13](L13_Cycloaddition_Part1.md) 5-4절의 역 Diels–Alder처럼 cycloaddition에서도 이미 본 것이다. (출처: Clayden p.913, p.923)

## 6. Cope rearrangement

> 개념 문서: [Cope rearrangement](../../wiki/반응/코프%20자리옮김.md), [Ireland–Claisen](../../wiki/반응/클라이젠%20자리옮김.md)

### 6.1 탄소만 있는 [3,3]

고리 TS가 탄소로만 이루어진 [3,3] 자리옮김이 Cope rearrangement이다. 가장 단순한 헥사-1,5-diene은 자리옮김해도 **출발물과 생성물이 같다**. 반응은 일어나지만 눈에 보이는 변화가 없다. 그러니 Cope 자리옮김을 쓸모 있게 만들려면 한쪽으로 미는 힘이 필요하다. (출처: Clayden p.913)

### 6.2 옥시-Cope: OH 하나로 carbonyl을 만들어 민다

3번 탄소에 OH를 달면(헥사-1,5-diene-3-ol) [3,3] 생성물은 **enol**이 되고, enol은 곧바로 aldehyde로 tautomerization한다. 5.1절의 논리로 반응이 한쪽으로 간다.

- CH2=CH–CH(OH)–CH2–CH=CH2 --[가열, [3,3]]--> HO–CH=CH–CH2–CH2–CH=CH2 → OHC–CH2–CH2–CH2–CH=CH2

(출처: Clayden p.913–914)

### 6.3 anion 옥시-Cope: KH로 alkoxide를 만들면 훨씬 빨라진다

alcohol을 먼저 염기(KH가 가장 좋다)로 처리해 alkoxide로 만들면 자리옮김이 크게 빨라진다. 왜일까? 생성물이 이번에는 칼륨 enolate인데, enolate는 출발물인 칼륨 alkoxide보다 안정하다. 반응이 진행될수록 O⁻와 새로 생기는 π 결합 사이의 콘쥬게이션이 자라나 TS부터 안정해진다. 산성 후처리로 enolate를 protonate하면 같은 aldehyde가 나온다. Clayden은 중성 반응을 "SLOW", anion 반응을 "FAST"로 표시한다. (출처: Clayden p.914)

![anionic oxy-Cope rearrangement: potassium alkoxide의 [3,3]으로 potassium enolate가 생긴다](../../figures/L16/anionic_oxy_cope.svg)

*그림: 빨간색은 끊어지는 σ 결합(O⁻가 달린 탄소와 이웃 CH2 사이), 초록색은 새로 생긴 C–C σ 결합이다. 화살표 셋은 Claisen과 같은 [3,3] 패턴이다. (1) 왼쪽 C=C π 전자가 두 말단 탄소 사이의 새 σ 결합이 되고, (2) 오른쪽 C=C π 전자가 옆자리로 옮겨 새 π 결합이 되며, (3) 빨간 σ 결합의 전자가 O⁻ 쪽 탄소와 이웃 탄소 사이의 새 π 결합이 된다. 생성물은 O⁻와 콘쥬게이션된 potassium enolate이고, 후처리(H⁺, H2O)로 hex-5-enal이 된다. 중성 OH(느림) 대신 KH로 만든 O⁻(빠름)를 쓰는 이유가 바로 이 enolate의 안정성이다. Clayden p.914의 그림을 따랐다.*

이 방법은 특이한 화합물도 만든다. 4원 고리가 붙은 allyl alcohol을 KH/THF로 처리하면 anion 옥시-Cope로 4원 고리가 8원 고리로 넓어지면서, 원래라면 Bredt 규칙에 걸릴 **bridgehead 위치의 트랜스 이중결합**을 가진 이환 ketone이 생긴다. (출처: Clayden p.914)

### 6.4 아일랜드-Claisen: ester enolate로 산을 만든다

고리 안의 산소 하나와 고리 밖의 산소 하나를 함께 두면 [3,3] 자리옮김이 아주 잘 일어난다. 이를 쉽게 만드는 방법이 **allyl alcohol의 ester를 enolate로 만드는 것**이다.

1. allyl alcohol을 acetyl chloride와 염기로 acetic acid allyl ester로 만든다.
2. LDA로 ester의 lithium enolate를 만든다(→ [L7](L07_Enolate_Alkylation.md) LDA). 필요하면 Me3SiCl로 silyl ketene acetal로 바꾼다.
3. [3,3] 자리옮김으로 γ,δ-unsaturated carboxylic acid의 lithium염(또는 silyl ester)이 생긴다.
4. H⁺/H2O 후처리로 γ,δ-unsaturated carboxylic acid을 얻는다.

R. E. Ireland가 1970년대에 개발해 아일랜드-Claisen 자리옮김이라고 부른다. 치환기가 알맞게 놓이면 단순 Claisen과 같은 이유(의자형 TS, 적도 R)로 *E* 선택성을 보인다. (출처: Clayden p.914)

### 6.5 산소 없이 미는 법: 고리 긴장과 더 치환된 alkene

산소가 전혀 없어도 출발물이 불안정하거나 생성물이 안정하면 Cope 자리옮김을 한쪽으로 몰 수 있다. (출처: Clayden p.915)

- **고리 긴장 해소:** 3원 고리의 약한 σ 결합이 끊어지는 [3,3] 자리옮김은 33 °C, 36시간 만에 정량적(100%)으로 진행한다. 실온보다 조금 높은 온도에서 끝난다는 것은 그만큼 유리하다는 뜻이다.
- **더 치환된 alkene:** exo-methylene(말단 C=CH2) 두 개를 가진 출발물이 [3,3] 자리옮김으로 5원 고리 안의 삼치환 이중결합 두 개를 가진 생성물이 된다.

해조류의 페로몬 이야기도 같은 원리다. 갈조류 암배우자는 cyclopropane 페로몬을 내놓는데, 이 분자는 상온에서 반감기 몇 분으로 [3,3] 자리옮김을 해 cycloheptadiene인 ectocarpene이 되면서 스스로 활성을 잃는다. 3원 고리 긴장 해소가 추진력이다.[^5] (출처: Clayden p.915)

### 6.6 Claisen 다음 Cope: 시트랄의 공업 합성

비타민 A 합성의 핵심 intermediate인 citral은 [3,3] 자리옮김을 **두 번 연달아** 써서 만든다. (출처: Clayden p.915)

1. unsaturated aldehyde와 unsaturated alcohol(프레놀형)이 물을 잃고 enol ether(allyl 바이닐 ether)를 만든다.
2. **Claisen rearrangement:** 가열하면 carbonyl 생성에 힘입어 γ,δ-unsaturated aldehyde가 된다.
3. **Cope rearrangement:** 이 생성물은 다시 1,5-diene 구조를 가지므로 두 번째 [3,3]이 일어난다. 이번에는 C=O와의 콘쥬게이션, 그리고 말단 이중결합 둘이 삼치환 이중결합 둘로 바뀌는 것이 추진력이다.

결과적으로 프레닐기가 분자 한쪽 끝에서 다른 쪽 끝으로 "걸어가며" 두 번 뒤집힌다(2.2절의 inside-out이 두 번 일어난 셈이다).

## 7. 다른 원소가 낀 [3,3] 자리옮김

> 개념 문서: [sigmatropic rearrangement](../../wiki/반응/시그마트로픽%20자리옮김.md)

[3,3] 자리옮김은 탄소와 산소에만 한정되지 않는다. (출처: Clayden p.916–917)

- **피셔 인돌 합성의 핵심 단계:** phenylhydrazine과 ketone이 약산성에서 phenylhydrazone을 만들고, 이것이 enamine tautomer와 평형을 이룬다. enamine은 [3,3] 자리옮김에 딱 맞게 놓여 있다. 끊어지는 σ 결합은 **약한 N–N 결합**이고, π 결합 하나는 benzene 고리의 것이다. 생성물인 불안정한 diimine은 방향족성을 회복하고, 양성자 이동과 C–N 결합 형성·절단(NH3 이탈)을 거쳐 인돌이 된다.
- **크로뮴산 ester의 [3,3] (산화적 자리옮김):** 3차 allyl alcohol을 산성 CrO3로 산화하면 C–H가 없어 직접 산화가 안 된다. 대신 생긴 크로뮴산 ester가 [3,3] 자리옮김으로 allyl계 반대쪽 끝(H가 있는 탄소)으로 옮겨 가고, 거기서 보통의 Cr(VI) 산화가 일어난다. 결과는 enone이다. 예: cyclohexenone --[1. RLi; 2. CrO3, H⁺]--> 3-R-cyclohex-2-enone(carbonyl이 원래 자리에서 allyl계 반대쪽으로 옮겨진다). Cr은 주황색 Cr(VI)에서 Cr(IV)를 거쳐 녹색 Cr(III)로 내려간다(→ [L6](L06_Oxidation_and_Alkene_Synthesis.md) 산화 문서 참고).

## 8. [2,3] 시그마트로픽 자리옮김

> 개념 문서: [2,3-sigmatropic rearrangement](../../wiki/반응/2,3-시그마트로픽%20자리옮김.md), [SeO2](../../wiki/시약/SeO2.md)

### 8.1 5원자 고리 TS에는 "원자에서 출발하는 화살표"가 필요하다

[2,3] 자리옮김은 5원자 고리 TS를 거친다(2 + 3 = 5). 그런데 5원자 고리를 따라 굽은 화살표 세 개를 돌리려면 하나는 **결합이 아니라 원자에서** 출발하거나 끝나야 한다. 그 원자가 탄소 anion이면 괜찮다. carbocation이거나, 산화수를 바꾸기 좋아하는 S, Se여도 된다. (출처: Clayden p.917)

### 8.2 benzyl allyl ether의 anion

benzyl allyl ether PhCH2–O–CH2–CH=CH2를 BuLi로 처리하면 benzyl 위치가 deprotonate되어 탄소 anion이 생긴다. 이 anion이 [2,3] 자리옮김을 한다.

- PhCH2–O–CH2CH=CH2 --[1. BuLi; 2. H⁺]--> PhCH(OH)–CH2–CH=CH2

C–O σ 결합을 잃고 C–C σ 결합을 얻는 것은 손해다(C–O가 더 강하다). 그래도 반응이 가는 이유는 출발물의 **탄소 anion보다 생성물의 산소 anion(alkoxide)이 훨씬 안정**하기 때문이다. (출처: Clayden p.917)

![benzyl allyl ether anion의 [2,3] 자리옮김: 5원자 고리를 도는 화살표 셋 가운데 하나가 탄소 anion의 전자쌍에서 출발한다](../../figures/L16/wittig23_benzyl_allyl.svg)

*그림: 파란색은 BuLi로 만든 benzyl 탄소 anion(비공유 전자쌍), 빨간색은 끊어지는 O–CH2 σ 결합, 초록색은 새로 생긴 C–C σ 결합이다. 5원자 고리를 따라 화살표 셋을 돌리려면 하나는 결합이 아니라 원자에서 출발해야 한다. (1) 탄소 anion의 전자쌍이 allyl 말단 탄소와 새 σ 결합을 만들고, (2) C=C π 전자가 CH–CH2 사이로 옮겨 새 π 결합이 되며, (3) O–CH2 σ 전자가 산소로 가서 alkoxide가 된다. 덜 안정한 탄소 anion이 더 안정한 산소 anion으로 바뀌는 것이 추진력이고, H⁺ 후처리로 homoallylic alcohol PhCH(OH)–CH2–CH=CH2가 된다. Clayden p.917의 그림을 따랐다.*

### 8.3 [2,3]에서도 *E* 선택성

5원자 고리라 완전한 의자는 아니지만, 새 π 결합이 될 부분은 의자형에 가까운 배치를 할 수 있다. 치환된 allyl alcohol로 ether를 만들어 두면 치환기 R이 적도 자리를 택해 **새 C=C가 트랜스**가 된다. (출처: Clayden p.917)

- CH2=CH–CH(OH)–R --[NaH, PhCH2Br]--> benzyl ether --[1. BuLi; 2. H⁺]--> PhCH(OH)–CH2–CH=CH–R (*E*)

### 8.4 ω 성분: p 오비탈 하나를 어떻게 세나

[2,3]에는 π 결합, σ 결합, 그리고 **탄소 anion(p 오비탈 하나)**이 참여한다. Woodward–Hoffmann에서 p 오비탈 하나는 ω(오메가) 성분으로 쓴다. 탄소 anion은 전자 2개라 ω2, carbocation은 0개라 ω0이다. 두 새 결합이 p 오비탈의 같은 로브로 생기면 ω2s, 다른 로브로 생기면 ω2a다.

benzyl allyl ether anion의 [2,3]은 **ω2a + σ2s + π2a**로 기술된다. (4q+2)s는 σ2s 하나, (4r)a는 없으므로 합 1, 열적 허용이다. (출처: Clayden p.917–918)

### 8.5 황의 [2,3]: 설펜산 ester와 allyl sulfoxide

S와 Se는 S(II), S(IV), S(VI)처럼 세 산화 상태를 오갈 수 있어서, 화살표가 그 원자에서 출발하고 끝나는 [2,3] 자리옮김을 잘 한다. (출처: Clayden p.918)

1. allyl alcohol + PhSCl(pyridine) → 불안정한 **설펜산 ester** R–CH=CH–CH2–O–SPh
2. 가열하면 [2,3] 자리옮김으로 **allyl sulfoxide**(S=O)가 된다. 황은 S(II)에서 S(IV)로 바뀐다.
3. allyl sulfoxide는 황이 안정화하는 anion을 만들 수 있어 염기 처리 후 RBr로 alkylation할 수 있다.
4. alkylate된 sulfoxide를 methanol 속에서 (MeO)3P와 가열하면 [2,3]이 **거꾸로** 진행해 설펜산 ester가 다시 생긴다. 평형은 sulfoxide 쪽이지만, 황을 좋아하는 (MeO)3P가 설펜산 ester를 붙잡고 methanol이 alkoxide를 바로 protonate해 allyl alcohol로 끌어낸다(부산물 PhSMe, (MeO)3P=O).

이 순환의 쓸모는 **allyl alcohol을 보통은 alkylation할 수 없는 위치에서 alkylation**한다는 데 있다. 동시에 시그마트로픽 반응이 가역적이라는 직접적인 증거이기도 하다. (출처: Clayden p.918)

### 8.6 셀레늄의 [2,3]: SeO2 allyl 산화

[L6](L06_Oxidation_and_Alkene_Synthesis.md)에서 본 SeO2 allyl 산화도 사실은 페리고리 반응 두 번이다. (출처: Clayden p.919)

1. **엔(ene) 반응과 비슷한 [4+2]:** SeO2가 alkene과 반응해 allyl 셀레닌산이 생긴다.
2. **[2,3] 자리옮김:** allyl 셀레닌산은 allyl sulfoxide처럼(C–Se 결합이 더 약해서 더 쉽게) [2,3] 자리옮김을 해 불안정한 Se(II) ester가 되고, 이것이 곧 분해되어 allyl alcohol이 된다.
3. 특히 methyl group의 경우 산화가 더 진행되어 aldehyde(또는 ketone)가 되기도 한다.

결과적으로 allyl 위치의 CH3가 CH2OH나 CH=O로 바뀐다. NBS allyl bromination과 결과는 비슷하지만 메커니즘은 전혀 다르다. 촉매량 SeO2와 t-BuOOH(재산화제)를 함께 쓰면 독성 있고 냄새나는 셀레늄 부산물을 줄일 수 있다.

## 9. [1,5] 시그마트로픽 수소 이동

> 개념 문서: [1,5-hydrogen shift](../../wiki/반응/1,5-수소%20이동.md)

### 9.1 숫자 "1"의 뜻: 같은 원자가 옮겨 간다

[i,j]의 한 숫자가 1이면 옛 σ 결합과 새 σ 결합이 **같은 원자**에 붙어 있다는 뜻이다. 즉 그 원자(또는 기)가 콘쥬게이션계를 따라 이동한다. 옮겨 가는 원자를 밝혀 [1,5]H 이동처럼 쓰기도 한다. [1,5]의 TS도 6원자 고리다(1 + 5 = 6). (출처: Clayden p.919)

대표 예가 치환 cyclopentadiene이다. 5-R-cyclopenta-1,3-diene의 C5–H가 이웃 탄소로 옮겨 간다. 번호를 셀 때는 메커니즘이 실제로 가는 방향, 즉 **5원 고리를 긴 쪽으로** 돌아 세야 1→5 관계가 된다. (출처: Clayden p.919)

![5-R-cyclopentadiene의 [1,5]H 이동: H가 이웃 탄소로 옮겨 가며 1-R 이성질체가 된다](../../figures/L16/h15_shift_cp.svg)

*그림: 빨간색은 끊어지는 C5–H σ 결합, 초록색은 새로 생긴 C1–H 결합이다. (1) C5–H σ 전자가 H를 이웃 탄소 C1로 데려가 새 C–H 결합이 되고, (2) C1=C2 π 전자가 C2–C3 사이로, (3) C3=C4 π 전자가 C4–C5 사이로 옮겨 간다. 고리를 긴 쪽으로 세면 H(1)에서 C5(1)–C4(2)–C3(3)–C2(4)–C1(5)이라 [1,5]다. H는 고리 평면의 같은 면(윗면)을 따라 미끄러지므로 suprafacial이다. 생성물 1-R 이성질체는 치환기가 이중결합에 붙어 더 안정하고, 같은 이동이 한 번 더 일어나면 2-R 이성질체도 생긴다. Clayden p.919–920의 그림을 따랐다.*

### 9.2 왜 alkylation한 cyclopentadiene으로 DA를 하면 혼합물이 나오나

cyclopentadienyl anion은 방향족이라 쉽게 만들고 alkylate하기도 쉽다. 그러면 "Cp⁻ alkylation → 5-R-cyclopentadiene → DA" 순서로 원하는 이환 화합물을 만들 수 있을 것 같다. 그런데 실제로는 **DA 생성물 세 가지의 혼합물**이 나온다. 왜일까?

5-R 이성질체가 빠른 [1,5]H 이동으로 1-R, 2-R 이성질체와 평형을 이루기 때문이다. 게다가 1-R, 2-R 이성질체는 이중결합에 치환기가 하나 더 붙어 더 안정하므로 혼합물에서 더 많다. 그래서 처음에 의도한 5-R diene의 DA 생성물은 오히려 소량 생성물이 된다. (출처: Clayden p.919–920)

Dreiding(1983)의 분자 내 DA 예가 이를 잘 보여 준다. 단편화 반응으로 만든 치환 cyclopentadiene은 그대로 분자 내 DA를 할 것으로 보였지만, [1,5]H 이동이 더 빨라 이중결합에 치환기가 더 많은 diene으로 먼저 바뀐 뒤 DA를 했다(74%). diene오필에 ester를 콘쥬게이션시켜 DA를 빠르게 하면 대부분이 [1,5]H 이동보다 먼저 DA를 했다(54%, [1,5]H 경유 생성물 39%). 이는 **두 반응의 속도 경쟁**이라는 것을 보여 준다(→ [L13](L13_Cycloaddition_Part1.md) 5-1절, diene오필의 EWG와 속도). (출처: Clayden p.920)

### 9.3 오비탈: FMO로도, Woodward–Hoffmann으로도

[1,5]H 이동은 FMO와 Woodward–Hoffmann 둘 다 쓰기 좋다. diene을 한 성분(HOMO, LUMO 또는 π4), C–H 결합을 다른 성분(LUMO, HOMO 또는 σ2)으로 본다. (출처: Clayden p.920–921)

- **FMO:** diene의 LUMO(ψ3)와 C–H 결합의 HOMO(채워진 σ 오비탈)를 겹친다. H는 구형 1s 오비탈만 가지므로 위상이 문제 되지 않고, ψ3의 양 끝 로브는 위상이 같아서([L13](L13_Cycloaddition_Part1.md) 7-1절) 모든 오비탈이 맞는다. diene HOMO + C–H LUMO 조합으로 봐도 똑같이 성립한다.
- **Woodward–Hoffmann:** diene π4, C–H σ2. H의 1s 오비탈에는 마디가 없으므로 H 쪽 끝은 **언제나 보존**이다. diene 위쪽 로브에 양 끝을 이으면 π4s + σ2s가 되고, (4q+2)s 하나(σ2s), (4r)a 없음 → 합 1, 허용.

두 방법 모두 같은 그림을 준다. H는 평면 cyclopentadiene 고리의 **윗면을 미끄러지듯** 옮겨 간다. 떠난 면과 같은 면으로 돌아오므로 **suprafacial 이동**이다. 고리에서 대면 이동(윗면에서 떠나 아랫면으로 돌아오는 것)은 애초에 불가능하다. (출처: Clayden p.920–921)

### 9.4 사슬형 diene에서도 일어난다

[1,5]H 이동은 cyclopentadiene에만 있는 것이 아니다. (*E*,*Z*)-diene은 *Z* 쪽 말단의 C–H가 diene 반대쪽 끝에 닿을 수 있어 [1,5]H 이동을 꽤 쉽게 하고, 그 결과 diene의 기하와 위치가 바뀐 혼합물이 생긴다. Clayden은 이것을 (*E*,*Z*)-diene을 쓴 DA 예가 드문 이유 가운데 하나로 든다(→ [L13](L13_Cycloaddition_Part1.md) 6-2절 in/out 치환기). (출처: Clayden p.921)

## 10. [1,3]H와 [1,7]H: 사슬 길이가 초면/대면을 바꾼다

> 개념 문서: [1,5-hydrogen shift](../../wiki/반응/1,5-수소%20이동.md), [electrocyclic reaction](../../wiki/반응/전자고리화%20반응.md)

### 10.1 열적 수소 이동 정리

[1,5]H만 초면으로 쉽게 일어나고 [1,3]H와 [1,7]H는 **대면**이어야 한다. Woodward–Hoffmann으로 확인하면 다음과 같다(H 쪽은 언제나 보존이므로 σ2s로 둔다).

| 이동 | 성분 | 초면이면 | 대면이면 | 열적 결론 |
|---|---|---|---|---|
| [1,3]H | π2 + σ2s | π2s + σ2s: (4q+2)s 2개 → 금지 | π2a + σ2s: 1개 → 허용 | 대면만 허용, 그러나 **불가능** |
| [1,5]H | π4 + σ2s | π4s + σ2s: 1개 → 허용 | π4a + σ2s: (4r)a 1개 + σ2s 1개 = 2 → 금지 | **초면, 쉬움** |
| [1,7]H | π6 + σ2s | π6s + σ2s: 2개 → 금지 | π6a + σ2s: 1개 → 허용 | **대면, 가능** |

Clayden의 요약표도 같다. [1,3]H 대면·불가능, [1,5]H 초면·쉬움, [1,7]H 대면·가능. (출처: Clayden p.921)

- **[1,3]H가 불가능한 이유:** 대면이면 허용이지만, 3탄소 사슬은 너무 짧고 단단해서 H가 윗면에서 아랫면으로 손을 뻗을 수 없다. 다행이다. 그렇지 않다면 이중결합이 [1,3]H 이동을 거듭하며 분자 안을 마구 돌아다닐 것이다.
- **[1,7]H가 가능한 이유:** triene 사슬은 충분히 길고 유연해서 H가 윗면에서 떠나 아랫면으로 돌아올 수 있다. 오비탈로 보면 hexatriene LUMO는 마디가 셋이라 양 끝 로브 위상이 반대이고, 그래서 대면 이동에서 겹침이 맞는다.

(출처: Clayden p.921)

### 10.2 광화학 반응에서는 규칙이 뒤집힌다

[L14](L14_Cycloaddition_Part2.md) 10절에서 열적으로 금지인 [2+2]가 빛으로는 허용됐듯이, 광화학 [1,n]H 이동도 열적 규칙과 반대다. Clayden은 단단한 고리 안이라 대면 [1,7]H 이동을 할 수 없는 화합물이 빛을 받으면 **초면**으로 [1,7]H 이동을 하는 예를 든다. (출처: Clayden p.896–897, p.921)

### 10.3 비타민 D: [1,7]H 이동은 빛 없이 일어난다

몸이 비타민 D를 만드는 마지막 단계가 [1,7]H 시그마트로픽 이동이다. 프로비타민 D2가 비타민 D2로 바뀌는 이 단계는 **빛 없이 저절로** 일어나므로 열적 반응이고, 따라서 대면이어야 한다. triene이 충분히 유연하므로 문제없다. 그렇다면 몸은 왜 햇빛이 필요할까? 그 앞 단계, 즉 ergosterol에서 프로비타민 D2를 만드는 고리 열림이 빛으로만 일어나는 **전자고리화 반응**이기 때문이다. 이 이야기는 [L17](L17_Electrocyclic_Reactions.md) 5.2절에서 이어진다.[^6] (출처: Clayden p.921–922; Wade p.693)

## 11. 한 장 정리: 시그마트로픽 반응의 허용 판정

> 개념 문서: [sigmatropic rearrangement](../../wiki/반응/시그마트로픽%20자리옮김.md)

| 반응 | TS 고리 | Woodward–Hoffmann 기술 | 열적 | 입체화학의 열쇠 |
|---|---|---|---|---|
| [3,3] Claisen·Cope | 6원자(의자형) | π2s + σ2a + π2a (합 1) | 허용 | 적도 R → *E* alkene |
| [2,3] (탄소 anion, S, Se) | 5원자 | ω2a + σ2s + π2a (합 1) | 허용 | 의자형 부분 → *E* alkene |
| [1,5]H | 6원자 | π4s + σ2s (합 1) | 초면 허용 | H는 같은 면으로 |
| [1,3]H | 4원자 | π2a + σ2s (합 1) | 대면만 허용, 기하상 불가 | – |
| [1,7]H | 8원자 | π6a + σ2s (합 1) | 대면 허용, 가능 | 비타민 D |

광화학 조건에서는 초면/대면 결론이 뒤집힌다. (출처: Clayden p.912–913, p.918, p.921)

## 흔한 오해

- "[3,3]은 6전자, [2,3]은 5전자라서 다르다": 대괄호 숫자는 **위치 번호**이고 전자 수가 아니다. [3,3]과 [2,3] 모두 참여 전자는 6개(π2 + σ2 + π2, 또는 ω2 + σ2 + π2)다. 이것은 cycloaddition의 [3+2]가 5전자가 아닌 것과 같은 함정이다([L15](L15_Cycloaddition_Part3.md) 흔한 오해). (출처: Clayden p.910, p.918)
- "Claisen 자리옮김과 Claisen 축합은 같은 반응": 이름만 같다. Claisen condensation([L9](L09_Claisen_Condensation.md))은 ester enolate의 친핵성 acyl 치환으로 β-keto ester를 만드는 극성 반응이고, Claisen 자리옮김은 allyl 바이닐(아릴) ether의 [3,3] 페리고리 반응으로 γ,δ-unsaturated carbonyl을 만든다. (출처: Clayden p.909, p.912)
- "Cope 자리옮김과 Cope 제거는 같은 것": Cope Cope elimination은 3차 amine oxide가 고리형 TS를 거쳐 alkene과 hydroxylamine으로 쪼개지는 **제거 반응**이다. [3,3] 자리옮김인 Cope 자리옮김과 다르다. (출처: Wade p.908; Clayden p.913)
- "Woodward–Hoffmann으로 허용이면 그쪽으로 반응이 간다": 규칙은 정반응과 역반응을 똑같이 허용한다. 방향은 carbonyl 생성, 고리 긴장, anion 안정성 같은 열역학이 정한다. sulfoxide ⇌ 설펜산 ester의 역반응이 실제로 쓰인다는 것이 그 증거다. (출처: Clayden p.913, p.918)
- "σ 결합은 초면/대면을 정할 수 없다": 큰 로브(보존)와 작은 로브(반전)로 정한다. 양 끝이 같으면 s, 다르면 a다. 그리고 꼬리표를 다르게 붙여도 셈의 홀짝은 같다. (출처: Clayden p.913)
- "[1,3]H는 규칙상 금지라서 안 일어난다": 열적 [1,3]H는 **대면으로는 허용**이다. 안 일어나는 이유는 3탄소 사슬이 너무 짧아 기하학적으로 불가능하기 때문이다. [L14](L14_Cycloaddition_Part2.md)의 π2s + π2a [2+2]가 "허용이지만 일어나지 않는" 것과 같은 구조다. (출처: Clayden p.921)
- "[1,5]H 이동은 cyclopentadiene에서만 일어난다": (*E*,*Z*)-diene 같은 사슬형 계에서도 쉽게 일어난다. (출처: Clayden p.921)
- "비타민 D 합성의 [1,7]H 이동에 빛이 필요하다": 빛이 필요한 것은 그 앞의 전자고리화 고리 열림이고, [1,7]H 이동 자체는 열적(대면)이다. (출처: Clayden p.921–922)

## 반응 요약표

| 반응 | 출발물 → 생성물 | 조건 | 추진력 | 입체화학 | 출처 |
|---|---|---|---|---|---|
| 방향족 Claisen | allyl 아릴 ether → *o*-allylphenol | 가열 | 방향족성 tautomerization | allyl group inside-out | Clayden p.909–910 |
| 지방족 Claisen | allyl 바이닐 ether → γ,δ-unsaturated aldehyde | 가열 | C=O 생성 | 의자형 TS, *E* | p.910–911 |
| acetal 교환 + Claisen | allyl alcohol + MeCH(OMe)2 → γ,δ-unsaturated aldehyde | EtCO2H, 가열(MeOH 증류) | 위와 같음 | *E* | p.911 |
| orthoester·orthoamide 변형 | allyl alcohol + RC(OMe)3 또는 DMF dimethyl acetal → γ,δ-unsaturated ester·amide | 산, 가열 | 위와 같음 | – | p.912 |
| Cope(모체) | 헥사-1,5-diene → 자기 자신 | 가열 | 없음(축퇴) | – | p.913 |
| 옥시-Cope | 헥사-1,5-diene-3-ol → 헥스-5-enal | 가열(느림) | enol → C=O | – | p.913–914 |
| anion 옥시-Cope | 같은 alcohol → 칼륨 enolate → aldehyde | KH, 가열; H⁺/H2O | enolate 안정화 | 빠름 | p.914 |
| 아일랜드-Claisen | allyl ester → γ,δ-unsaturated carboxylic acid | LDA(필요하면 Me3SiCl); H⁺/H2O | carboxylate 생성 | *E* | p.914 |
| 긴장 해소 Cope | 3원 고리 포함 1,5-diene → 고리 확장 생성물 | 33 °C, 36 h (100%) | 고리 긴장 해소 | – | p.915 |
| 시트랄 합성 | enol ether → (Claisen) → (Cope) → 시트랄 | 가열 | C=O, 콘쥬게이션, 삼치환 alkene | – | p.915 |
| 피셔 인돌 | phenylhydrazone(enamine형) → diimine → 인돌 | 약산, 가열 | 약한 N–N 절단, 방향족화 | – | p.916 |
| 크로뮴산 ester [3,3] | 3차 allyl alcohol → 자리 옮긴 enone | CrO3, H⁺ | Cr(VI) 산화 | – | p.916–917 |
| [2,3] 탄소 anion | benzyl allyl ether → 호모알릴 alcohol | BuLi; H⁺ | 탄소 anion → alkoxide | *E* | p.917 |
| [2,3] 황 | allyl alcohol → 설펜산 ester → allyl sulfoxide | PhSCl, pyridine | S=O 생성 | – | p.918 |
| 역 [2,3] 황 | alkylate된 allyl sulfoxide → allyl alcohol | (MeO)3P, MeOH | 친황 포획 | – | p.918 |
| SeO2 allyl 산화 | alkene → allyl alcohol / 엔알 | SeO2 (촉매 + t-BuOOH) | [4+2] 후 [2,3] | – | p.919 |
| [1,5]H 이동 | 5-R-cyclopentadiene ⇌ 1-R, 2-R 이성질체 | 빠른 평형(DA보다 빠를 수 있음) | 더 치환된 diene | 초면 | p.919–921 |
| [1,7]H 이동 | 프로비타민 D2 → 비타민 D2 | 열(빛 불필요) | – | 대면 | p.921–922 |

---

## 자가 점검 문제

1. 다음 반응을 [i,j]로 분류하고 TS 고리 크기를 쓰라. (a) 2-allylphenol을 주는 allyl phenyl ether의 첫 단계, (b) BuLi로 만든 benzyl allyl ether anion의 자리옮김, (c) 5-methylcyclopentadiene이 1-methylcyclopentadiene으로 바뀌는 과정, (d) 프로비타민 D2 → 비타민 D2.

2. (*E*)-뷰트-2-엔일 phenyl ether PhO–CH2–CH=CH–CH3를 가열했다. [3,3] 단계 직후의 intermediate와 최종 생성물을 쓰고, methyl group이 어느 탄소에 놓이는지 설명하라.

3. 펜트-1-ene-3-ol CH2=CH–CH(OH)–CH2CH3를 (a) MeCH(OMe)2, (b) MeC(OMe)3와 각각 propanoic acid 촉매로 가열했다. 각 생성물의 구조와 이중결합의 기하를 쓰고, 기하가 그렇게 정해지는 이유를 설명하라.

4. 헥사-1,5-diene-3-ol을 그냥 가열할 때와 KH로 먼저 처리한 뒤 가열할 때를 비교하라. 두 경우의 [3,3] 직후 생성물, 최종 생성물(후처리 포함), 속도 차이의 이유를 쓰라.

5. (a) [1,5]H 이동을 π4 + σ2로 놓고 Woodward–Hoffmann 셈을 해서 초면 이동이 열적으로 허용됨을 보이라. (b) 같은 방식으로 열적 [1,3]H 이동이 어떤 조건에서 허용되는지 구하고, 그런데도 실제로 일어나지 않는 이유를 쓰라.

6. 5-benzylcyclopentadiene을 만든 뒤 바로 DMAD(MeO2C–C≡C–CO2Me)와 반응시켰더니 DA 생성물 세 가지가 섞여 나왔다. 이유를 설명하고, 의도한 생성물이 주생성물이 되지 않는 이유도 쓰라.

---

## 해설

1. (a) [3,3], 6원자 고리 TS. 옛 O–CH2 결합 양 끝을 1로 두면 새 C–C 결합은 고리의 *ortho* 탄소(3)와 allyl 말단 탄소(3) 사이에 생긴다. (b) [2,3], 5원자 고리 TS. 탄소 anion(2번)과 allyl 말단(3번)이 이어진다. (c) [1,5]H, 6원자 고리 TS. 같은 H가 옛 결합과 새 결합의 한쪽 끝(1)이고, 고리를 긴 쪽으로 돌아 5번 탄소에 붙는다(여러 번 일어나면 2-methyl 이성질체도 생긴다). (d) [1,7]H, 8원자 고리 TS, 열적 대면 이동. (출처: Clayden p.909–910, p.917, p.919, p.921)

2. [3,3] 직후에는 방향족성을 잃은 6-치환 cyclohexa-2,4-diene온이 생기고, tautomerization으로 2-(뷰트-3-ene-2-일)phenol *o*-C6H4(OH)–CH(CH3)–CH=CH2가 된다. allyl group이 inside-out으로 붙으므로 산소에 붙어 있던 CH2가 아니라 반대쪽 끝, 즉 CH3가 달린 탄소가 고리와 결합한다. 그래서 methyl은 고리에 붙은 탄소에 놓이고 말단 바이닐기가 남는다. (출처: Clayden p.909–910의 프레닐 예를 바꿈)

3. (a) acetal 교환으로 CH2=CH–O–CH(Et)–CH=CH2가 생기고, [3,3] 자리옮김으로 (*E*)-헵트-4-enal OHC–CH2–CH2–CH=CH–CH2CH3이 된다. (b) orthoester에서는 MeO–C(=CH2)–O–CH(Et)–CH=CH2(ketene acetal)를 거쳐 methyl (*E*)-헵트-4-엔오에이트 MeO2C–CH2–CH2–CH=CH–Et가 된다. 두 경우 모두 의자형 TS에서 Et가 적도 자리를 택하고 그 배치가 그대로 새 C=C로 넘어가므로 *E*가 우세하다. 추진력은 C=O 생성이다. (출처: Clayden p.910–912)

4. 중성: [3,3] 직후 enol HO–CH=CH–CH2–CH2–CH=CH2가 생기고 tautomerization으로 헥스-5-enal이 된다. 느리다. KH 처리: alkoxide가 [3,3]을 해서 칼륨 enolate가 생기고, H⁺/H2O 후처리로 같은 헥스-5-enal이 된다. enolate가 alkoxide보다 안정하고, TS에서부터 O⁻와 새 π 결합의 콘쥬게이션이 자라므로 훨씬 빠르다. (출처: Clayden p.913–914)

5. (a) diene 윗면 로브에 양 끝을 이으면 π4s, H는 1s 오비탈이라 언제나 보존이므로 C–H는 σ2s. (4q+2)s = 1(σ2s), (4r)a = 0 → 합 1(홀수), 허용. (b) [1,3]H는 π2 + σ2s. 초면(π2s)이면 (4q+2)s가 2개라 금지, 대면(π2a)이면 σ2s 하나뿐이라 합 1, 허용. 즉 대면이면 허용이지만 3탄소 사슬이 짧고 단단해 H가 반대 면으로 갈 수 없어 실제로는 불가능하다. (출처: Clayden p.920–921)

6. 5-benzyl 이성질체는 빠른 초면 [1,5]H 이동으로 1-benzyl, 2-benzyl 이성질체와 평형을 이룬다. 세 diene이 모두 DMAD와 DA를 하므로 생성물이 셋이다. 1-, 2-치환 이성질체는 이중결합에 치환기가 붙어 더 안정하므로 혼합물 속에 더 많고, 그래서 5-치환 diene에서 나온 의도한 생성물은 오히려 소량이 된다. DA를 [1,5]H 이동보다 빠르게 만들면(더 반응성 큰 diene오필) 이 경쟁을 줄일 수 있다. (출처: Clayden p.919–920)

## 각주

[^1]: Clayden은 이 구분을 35장 전자고리화 반응 절의 상자로 정리한다. cycloaddition과 그 역반응을 한데 묶어 Δσ = ±2로 쓰는 식이다. (출처: Clayden p.922)
[^2]: [1,3]H 이동은 4원자, [1,7]H 이동은 8원자 고리 TS를 거치는 셈이다. 이 크기 차이가 10절의 "초면이냐 대면이냐, 그리고 기하학적으로 가능하냐"를 가른다. (출처: Clayden p.917, p.921)
[^3]: Clayden은 이 acetal 교환에서 첫 methanol은 S<sub>N</sub>1, 두 번째는 E1로 떨어진다고 강조하고 "acetal에서는 절대 S<sub>N</sub>2 메커니즘을 쓰지 말라"고 덧붙인다. protonate된 OR이나 OH가 떨어지는 단계가 acetal 화학의 중심이다. (출처: Clayden p.911)
[^4]: Clayden은 [3,3] 자리옮김을 FMO로 다루는 방법이 궁금하면 Ian Fleming의 *Frontier Orbitals and Organic Chemical Reactions*(2판, 2009)를 보라고 하고, [1,5] 자리옮김에서는 FMO 접근도 함께 쓴다. (출처: Clayden p.913)
[^5]: 1995년에 발표된 결과로, 그전까지 페로몬으로 알려졌던 엑토카펜이 사실은 비활성이고 진짜 페로몬은 cyclopropane 화합물이라는 것이 밝혀졌다. 스스로 몇 분 만에 꺼지는 신호라서 바닷물을 쓸모없는 페로몬으로 채우지 않고 정확한 순간만 allyl 수 있다. (출처: Clayden p.915)
[^6]: Clayden은 ergosterol → 프로비타민 D2 → 비타민 D2(D2 계열)로, Wade는 7-dehydrocholesterol → 프로비타민 D3(D3 계열)로 설명한다. 출발 sterol과 곁사슬이 다를 뿐, "햇빛이 필요한 페리고리 고리 열림"이라는 핵심은 같다. Wade는 햇빛을 덜 받는 추운 지방 아이들의 rickets을 예로 든다. (출처: Clayden p.921–922; Wade p.693)
