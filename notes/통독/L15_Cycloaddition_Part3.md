# L15. 고리화 첨가 반응 3부 (Cycloadditions, part 3)

> **통독본**: 2026-10-12 재구성 직전의 강의별 전체 노트(교과서 보강 포함)를 그대로 보존한 사본이다. 강의 흐름대로 한 번에 읽을 때 쓴다. 이후의 수정과 보충은 개념 문서에만 반영되므로, **최신 내용은 개념 문서**가 기준이다. 뼈대 노트: [L15 뼈대](../L15_Cycloaddition_Part3.md) · [위키 대문](../../wiki/위키%20대문.md)



> **관련 위키 문서** ([위키 대문](../../wiki/위키%20대문.md))
> - 반응: [1,3-dipolar cycloaddition](../../wiki/반응/1,3-쌍극자%20고리화%20첨가.md), [photochemical \[2+2\] cycloaddition](../../wiki/반응/광화학%202+2%20고리화%20첨가.md), [nitrone cycloaddition](../../wiki/반응/나이트론%20고리화%20첨가.md), [nitrile oxide cycloaddition](../../wiki/반응/나이트릴%20옥사이드%20고리화%20첨가.md), [Diels–Alder reaction](../../wiki/반응/딜스-알더%20반응.md), [Staudinger β-lactam synthesis](../../wiki/반응/스타우딩거%20β-락탐%20합성.md), [역 Diels–Alder reaction](../../wiki/반응/역%20딜스-알더%20반응.md), [역전자 요구 Diels–Alder reaction](../../wiki/반응/역전자%20요구%20딜스-알더%20반응.md), [ozonolysis](../../wiki/반응/오존%20분해.md), [ketene 2+2 cycloaddition](../../wiki/반응/케텐%202+2%20고리화%20첨가.md), [click reaction](../../wiki/반응/클릭%20반응.md)
> - 시약: [LiAlH4](../../wiki/시약/LiAlH4.md), [Danishefsky diene](../../wiki/시약/대니셰프스키%20다이엔.md), [ozone](../../wiki/시약/오존.md)
> - 개념: [1,3-dipole](../../wiki/개념/1,3-쌍극자.md), [endo rule](../../wiki/개념/endo%20규칙.md), [Diels–Alder regioselectivity](../../wiki/개념/딜스-알더%20위치선택성.md), [Woodward–Hoffmann rules](../../wiki/개념/우드워드-호프만%20규칙.md), [imine](../../wiki/개념/이민.md), [isocyanate](../../wiki/개념/이소시아네이트.md), [stereospecificity and stereoselectivity](../../wiki/개념/입체특이성과%20입체선택성.md), [suprafacial and antarafacial](../../wiki/개념/초면과%20대면.md), [ketene](../../wiki/개념/케텐.md), [pericyclic reaction](../../wiki/개념/페리고리%20반응.md), [frontier molecular orbital](../../wiki/개념/프런티어%20분자%20오비탈.md)



CM3121 Advanced Organic Chemistry, Dr. Zhu Ye

## 개요

cycloaddition 시리즈의 마지막 편이다. 앞 강의들에서 Diels–Alder 반응과 프런티어 분자 frontier molecular orbital, FMO, Woodward–Hoffmann 규칙을 익혔다면(→ [L13](L13_Cycloaddition_Part1.md)·[L14](L14_Cycloaddition_Part2.md) cycloaddition 1·2부 문서 참고), 이번 강의는 그 규칙의 "예외처럼 보이는 경우"와 "다른 고리 크기"로 시야를 넓힌다. 먼저 원래는 열적으로 금지되어야 할 [2+2] cycloaddition이 ketene과 isocyanate에서는 왜 버젓이 일어나는지 살펴보고, 그 결과물인 β-락탐(β-lactam)이 페니실린과 어떻게 연결되는지 본다. 이어서 1,3-쌍극자(1,3-dipole)가 만드는 5원자 헤테로고리, 그리고 사실은 1,3-쌍극 cycloaddition이 세 번 연달아 일어나는 반응인 ozone ozonolysis를 다룬다. 마지막으로 siloxydiene을 이용한 비대칭 합성과, 살아 있는 세포 안에서 cycloaddition을 일으키는 생체접합 bioconjugate chemistry으로 마무리한다.

## 0. 워밍업: Diels–Alder 생성물은 어떻게 한 번에 맞히나? (Practice)

> 개념 문서: [Diels–Alder regioselectivity](../../wiki/개념/딜스-알더%20위치선택성.md), [endo rule](../../wiki/개념/endo%20규칙.md)

강의는 복습 문제로 시작한다. 1-acetoxy-1,3-butadiene(AcO-CH=CH-CH=CH2, E)과 (E)-crotonaldehyde(OHC-CH=CH-CH3)를 반응시키면 어떤 cyclohexene이 생길까? 경우의 수가 많아 보이지만, 슬라이드는 이것을 세 번의 결정으로 쪼갠다.

첫째는 regioselectivity이다. diene C1에 X형 치환기(OAc)가 있으니 "ortho" 규칙에 따라 diene의 OAc 달린 탄소 바로 옆에 diene오필의 CHO 달린 탄소가 붙는다. 그러면 Me 달린 탄소는 자연스럽게 diene의 반대쪽 끝과 결합한다. 둘째는 stereoselectivity이다. 2차 궤도 상호작용 때문에 CHO가 diene π계 밑으로 들어가는 endo 전이상태가 유리하고, 그 결과 diene C1의 바깥쪽 치환기인 OAc와 CHO가 생성물에서 서로 cis가 된다. 셋째는 stereospecificity이다. diene오필이 E였으므로 CHO와 Me의 trans 관계는 생성물에 그대로 남는다.

그래서 답은 C(OAc)–C(CHO)–C(Me)가 고리에 연달아 놓이고, 고리 이중결합은 diene의 C2=C3 자리에 남으며, OAc/CHO는 cis, CHO/Me는 trans인 화합물이다. 이름으로는 2-acetoxy-6-methylcyclohex-3-ene-1-carbaldehyde이며 라세미체로 얻어진다(슬라이드의 "or its enantiomer").

(출처: L15 p.3)

## 1. 치환기를 C, Z, X로 나누는 이유 (Substituent classifications)

> 개념 문서: [frontier molecular orbital](../../wiki/개념/프런티어%20분자%20오비탈.md), [substituent effect](../../wiki/개념/치환기%20효과.md)

그런데 "X형 치환기"라는 말은 정확히 무엇을 뜻할까? 강의는 치환기를 전자적 성격에 따라 세 부류로 나눈다.

| 기호 | 예 | 전자적 성격 |
|---|---|---|
| C | 비닐(-CH=CH2), phenyl(-Ph) 등 공액 치환기 | π 주개 또는 π 받개, σ 중성 |
| Z | -COR, -CO2Me, -C≡N, -NO2 등 | π 받개이자 σ 받개 |
| Z | -metal (예: -SiMe3, -BR2) | π 받개이지만 σ 주개 |
| X | -OMe, -NMe2 등 | π 주개이지만 σ 받개 |
| X | -CH3 등 | π 주개, σ 중성 |

즉 C는 공액을 늘리는 치환기, Z는 π 전자를 끌어가는 치환기, X는 π 전자를 밀어주는 치환기다. 여기서 눈여겨볼 점은 같은 Z라도 silyl기나 보릴기는 σ 쪽으로는 오히려 전자를 준다는 것, 같은 X라도 OMe는 σ 쪽으로는 전자를 끈다는 것이다. cycloaddition의 반응성과 regioselectivity을 좌우하는 것은 주로 π 효과이므로, 분류도 π 성격을 기준으로 한다.

이어지는 연습 슬라이드(p.5)는 화합물을 점선 양쪽으로 갈라 놓았다. 왼쪽은 2-methyl프로펜, toluene, cyclohexanone의 pyrrolidine enamine(enamine), lithium enolate(-OLi), 2-methoxy-1,3-butadiene, (E)-1,3-pentadiene처럼 X형 치환기를 가진 전자 풍부 화합물이고, 오른쪽은 methyl acrylate, cyclohex-2-enone, benzonitrile처럼 Z형 치환기를 가진 전자 부족 화합물이다.[1]

(출처: L15 p.4–5)

## 14. 열적 [2+2] cycloaddition (Thermal [2+2] cycloadditions)

### 14.1 금지된 반응이 왜 일어나나?

> 개념 문서: [ketene](../../wiki/개념/케텐.md), [isocyanate](../../wiki/개념/이소시아네이트.md)

Woodward–Hoffmann 규칙에 따르면 총 4전자(4n)가 참여하는 [2+2]는 열적으로 금지다. 실제로 ethylene 두 분자를 아무리 가열해도 cyclobutane은 생기지 않는다. 그런데 슬라이드는 가열만으로 4원 고리가 생기는 두 예를 보여 준다. cis-2-butene과 dimethylketene(Me2C=C=O)을 가열하면 cyclobutanone이 생기는데, 두 Me의 cis 관계가 생성물에도 그대로 남는다. 또 alkene R-CH=CH2와 chlorosulfonyl isocyanate(ClSO2-N=C=O, CSI)를 가열하면 N-SO2Cl β-락탐이 생긴다.

두 시약의 공통점은 누적 cumulated double bonds이다. ketene의 중앙 탄소는 sp 혼성이라 C=C π 결합과 C=O π 결합이 서로 직각으로 놓여 있고, isocyanate의 N=C=O도 마찬가지다. 이 "직각으로 꺾인 두 π 결합"이 수수께끼를 푸는 열쇠다.

(출처: L15 p.6)

### 14.2 supra-antara라는 탈출구

> 개념 문서: [ketene 2+2 cycloaddition](../../wiki/반응/케텐%202+2%20고리화%20첨가.md), [suprafacial and antarafacial](../../wiki/개념/초면과%20대면.md)

그렇다면 직교하는 π 결합이 어떻게 금지를 피하게 해 줄까? 일반 alkene 두 분자가 같은 suprafacial–suprafacial, supra-supra 접근하면, 한쪽의 HOMO와 다른 쪽의 LUMO가 한쪽 끝에서는 같은 위상으로, 다른 쪽 끝에서는 반대 위상으로 만난다. 결합 하나는 생기는데 다른 하나는 반결합성이 되어 버리는 셈이다. 이론적으로는 한 성분이 반대 면을 쓰는 suprafacial–antarafacial(supra-antara) 배치면 대칭이 맞지만, 평범한 alkene이 그렇게 몸을 비틀어 접근하는 것은 기하적으로 거의 불가능하다. 슬라이드는 supra-supra, supra-antara, antara-antara 세 배치를 나란히 그리고, 이 중 supra-antara에 박스를 쳐 두었다.

ketene은 바로 이 supra-antara를 해낼 수 있다. 삽화(p.7)를 보면 alkene의 HOMO(초록)가 ketene C=O의 LUMO(π*)와 결합하면서, 동시에 중앙 탄소의 직교하는 여분의 p 궤도와도 결합성 상호작용을 할 수 있다. 덕분에 새로 생기는 두 σ 결합이 모두 결합성 겹침으로 만들어지고, ketene이 antarafacial 성분 역할을 하는 [π2s + π2a] 경로가 열적으로 허용된다.[2] 요약 슬라이드가 "특수한 경우: 열적 [2+2] (suprafacial–antarafacial)"이라고 따로 적어 둔 것이 이 이야기다.

보충: 교재는 이 그림을 겹침의 개수로 세어 설명한다. 먼저 한 alkene을 다른 alkene에 대해 90° 돌려 십자로 겹치면, HOMO의 두 로브와 LUMO의 두 로브가 만나는 네 모서리 가운데 두 곳은 결합성, 두 곳은 반결합성이라 알짜 이득이 없다. 여기에 ketene 중앙 탄소의 직교 p 오비탈(C=O π의 일부)을 더하면 alkene HOMO의 두 로브가 모두 이 오비탈과 결합성으로 겹쳐, 결합성 4곳 대 반결합성 2곳이 되어 반응이 가능해진다. alkene 두 개만으로는 이 여분의 오비탈이 없다는 것이 일반 alkene과의 차이다. 게다가 ketene·isocyanate는 친전자성이라 LUMO가 낮아 alkene HOMO와 에너지도 잘 맞는다. (보충 근거: Clayden p.898–899) 시그마트로픽·전자고리화에서 같은 s/a 개념을 σ 결합에 적용하는 방법은 → L16/L17 예습 노트에서 다룬다.

(출처: L15 p.7, p.32)

### 14.3 ketene으로 cyclobutanone 만들기

> 개념 문서: [ketene 2+2 cycloaddition](../../wiki/반응/케텐%202+2%20고리화%20첨가.md), [ketene](../../wiki/개념/케텐.md)

ketene은 불안정해서 병에 담아 두고 쓰기 어렵다. 그래서 보통은 반응 플라스크 안에서 만든다. dichloroacetyl chloride(Cl2CH-COCl)에 Et3N을 넣으면 다음 순서로 dichloroketene(Cl2C=C=O)이 생긴다.

1. Et3N(염기)이 두 Cl과 C=O 때문에 산성이 커진 α-H를 떼어 enolate를 만든다.
2. enolate 산소의 전자쌍이 되돌아오면서 acyl 탄소의 C–Cl 결합이 끊어지고 Cl⁻가 떨어져 나가 ketene이 된다.

![dichloroacetyl chloride와 Et3N에서 dichloroketene이 생기는 E1cB 제거](../../figures/L15/ketene_generation_e1cb.svg)

*그림: dichloroketene이 생기는 E1cB 제거. 1단계에서 파란 Et3N의 비공유 전자쌍이 빨간 α-H를 떼고(첫 화살표), C–H 결합 전자가 C–C 사이로 들어가 C=C를 만들며(둘째), 빨간 C=O의 π 전자는 산소로 올라가 enolate가 된다(셋째). 2단계에서는 파란 O⁻의 전자쌍이 되돌아와 C=O를 다시 만들고, 빨간 C–Cl 결합 전자가 Cl⁻로 떨어져 나간다. 초록 결합이 각 단계에서 새로 생긴 π 결합이다.*

이 ketene을 cyclopentadiene과 만나게 하면 7,7-dichlorobicyclo로[3.2.0]hept-2-en-6-one이 생긴다. 어느 탄소끼리 붙는지는 슬라이드의 힌트 "carbonyl 탄소가 친전자성이다"로 풀린다. 즉 diene의 친핵성 말단 탄소가 ketene의 carbonyl 탄소와 결합하고, ketene의 CCl2 탄소는 그 옆 탄소와 결합한다. 그래서 C=O는 CH2 옆 고리접합 탄소에, CCl2는 남은 C=C 바로 옆(allyl 위치) 고리접합 탄소에 붙고, 두 고리접합 H는 cis가 된다.

흥미로운 점은 cyclopentadiene이 Diels–Alder의 단골 diene인데도 이 경우에는 [2+2]가 [4+2]보다 빠르다는 것이다.

보충: ketene 생성 단계는 염기가 산성 α-H를 먼저 떼고 그다음 Cl⁻이 떨어지는 E1cB 제거다. 생성물의 cis 고리 접합은 cyclopentadiene 고리 안의 cis C=C에서 그대로 stereospecificity. 두 Cl은 보통 최종 목표에 필요 없지만 Zn/HOAc로 아연 enolate를 거쳐 하나씩 H로 바꿀 수 있어서, 반응성 좋은 dichloroketene을 쓰고 나중에 Cl을 지우는 전략이 흔하다. 거꾸로 ketene의 [4+2] 생성물(cyclohexenone 골격)이 필요하면 ketene은 [2+2]를 해 버리므로, nitroalkene처럼 DA 뒤에 ketone으로 바꿀 수 있는 "ketene 등가체"를 dienophile로 쓴다. (보충 근거: Clayden p.899) 역합성에서도 같은 생각을 쓴다. cyclobutanone을 두 방식으로 자를 수 있으면, alkene의 cis/trans로 입체화학을 정할 수 있고 dichloroketene을 쓸 수 있는 쪽을 고른다. (보충 근거: Clayden p.900)

![dichloroketene과 cyclopentadiene의 열적 [2+2] cycloaddition](../../figures/L15/ketene_22_cyclopentadiene.svg)

*그림: 파란색은 cyclopentadiene의 반응하는 C=C(nucleophile 쪽), 빨간색은 ketene의 C=O로, 그 carbonyl 탄소가 친전자성 자리다. 두 화살표는 같은 방향(시계 방향)으로 돈다. 위쪽 화살표는 diene의 C=C 전자가 ketene의 carbonyl 탄소와 결합하는 것을, 아래쪽 화살표는 ketene의 C=C 전자가 diene의 이웃 탄소와 결합하는 것을 나타낸다. 생성물의 초록 결합이 새 σ 결합이며, 쐐기로 그린 두 고리 접합 H는 cis다. C=O는 CH2 옆 접합 탄소에, CCl2는 남은 C=C 옆 접합 탄소에 붙는다.*

(출처: L15 p.8)

### 14.4 β-락탐과 페니실린: 4원 고리가 왜 약이 되나?

> 개념 문서: [Staudinger β-lactam synthesis](../../wiki/반응/스타우딩거%20β-락탐%20합성.md)

β-락탐은 4원 고리 amide로, 페니실린의 핵심 구조다.[3] 페니실린은 β-락탐이 황을 포함한 5원 고리(티아졸리딘)와 융합된 구조이며, 곁사슬 R에 따라 Penicillin V(R = PhOCH2), Penicillin G(R = CH2Ph)로 나뉜다.

그렇다면 이 작은 고리가 어떻게 세균을 죽일까? 세균 세포벽의 peptidoglycan은 peptide 사슬끼리 교차결합되어 튼튼해지는데, 이 교차결합을 만드는 효소가 transpeptidase이고, 효소가 인식하는 부위가 사슬 끝의 D-Ala-D-Ala다. 그런데 페니실린의 β-락탐 부분은 이 D-alanyl-D-alanine과 모양이 닮았다. 그래서 효소는 페니실린을 기질로 착각하고 붙잡는다.

1. 효소 활성부위의 친핵성 O⁻(세린)가 긴장된 β-락탐의 carbonyl 탄소를 공격해 tetrahedral intermediate를 만든다.
2. C–N 결합이 끊어지며 4원 고리가 열리고, 떨어져 나가는 N은 근처의 B–H⁺에서 양성자를 받는다.
3. 결과적으로 효소의 세린이 ester 형태로 acylate된 채 묶여 버린다. 이것이 공유결합 covalent inhibition이다.

고리 긴장이 큰 4원 고리라서 보통의 amide보다 훨씬 쉽게 열린다는 점이 이 메커니즘의 핵심이다.

(출처: L15 p.9–10)

### 14.5 β-락탐을 [2+2]로 자르는 두 가지 방법

> 개념 문서: [Staudinger β-lactam synthesis](../../wiki/반응/스타우딩거%20β-락탐%20합성.md), [isocyanate](../../wiki/개념/이소시아네이트.md)

β-락탐을 합성하려면 어디를 잘라야 할까? 4원 고리를 [2+2]의 생성물로 보면 역합성 절단 방식은 두 가지다. 하나는 β-락탐을 ketene + imine으로 자르는 것(N1–C2와 C3–C4 결합 절단), 다른 하나는 alkene + isocyanate로 자르는 것(N1–C4와 C2–C3 결합 절단)이다. 페니실린과 amoxicillin이 모두 이 고리를 품고 있다.

(출처: L15 p.11)

첫 번째 방법의 예로, phenoxyacetyl chloride(PhOCH2COCl)를 Et3N으로 처리해 페녹시케텐(PhO-CH=C=O)을 만들고 imine(Ar-N=CH-…, Ar = 4-methoxyphenyl, acetal 측쇄 포함)과 반응시키면 3-페녹시-β-락탐이 92% 수율로 생긴다. regioselectivity은 앞과 같은 논리다. imine의 친핵성 N이 ketene의 친전자성 carbonyl 탄소를 공격해 N–C(=O) 결합을 만들고, ketene의 α-탄소(PhO 달린 탄소)가 imine 탄소와 결합한다. 슬라이드 그림에서 C3의 PhO(점선)와 C4 치환기(쐐기)는 trans로 그려져 있다.[4]

두 번째 방법의 예는 CSI와 2-(chloromethyl)프로펜(CH2=C(CH3)CH2Cl)의 반응이다. alkene의 말단 CH2가 nucleophile로서 CSI의 carbonyl 탄소와 결합하고, 양전하를 더 잘 견디는 3차 탄소가 N과 결합한다. 그래서 N 옆에 Me와 CH2Cl을 가진 4차 탄소가 있는 1-(chlorosulfonyl)-4-(chloromethyl)-4-methyl아제티딘-2-one이 생긴다. N에 붙은 SO2Cl은 다음처럼 떼어 낸다.

1. NaHCO3/H2O로 S–Cl이 가수분해되어 N-SO3H가 된다.
2. O–H 결합의 전자가 S=O 쪽으로 밀리고 N–S 결합이 끊어지면서 SO3가 떨어져 나가고, N은 양성자를 얻어 N-H 락탐(4-(chloromethyl)-4-methyl아제티딘-2-one)이 된다.

보충: 두 방법 모두 N에 치환기가 붙어 있는데, 그 이유는 서로 다르다. ketene + imine에서 N-아릴(4-methoxyphenyl)을 쓰는 것은 N-아릴 imine이 N-H imine보다 안정해서 다루기 쉽기 때문이다. isocyanate + alkene에서 N-SO2Cl을 쓰는 것은 alkene이 그다지 친핵적이지 않으므로 isocyanate를 강한 전자 끄는 기로 활성화해야 하고, 그 기를 반응 뒤 쉽게 떼어 낼 수 있어야 하기 때문이다. CSI는 시판되고 단순 alkene과도 반응한다. 다만 enol ether나 바이닐 sulfide처럼 아주 전자가 풍부한 alkene과는 반응이 협동적이지 않고 자유 회전이 가능한 intermediate를 거치는 단계적 반응으로 바뀌어, alkene의 E/Z 혼합물에서도 trans 생성물만 나온다. 즉 이때는 입체특이적이 아니라 입체선택적이다. (보충 근거: Clayden p.900–901)

![페녹시케텐과 imine의 [2+2] cycloaddition으로 β-락탐이 생기는 과정](../../figures/L15/staudinger_beta_lactam.svg)

*그림: 파란 N은 imine의 친핵성 질소, 빨간색은 ketene의 C=O(친전자성 carbonyl 탄소)다. 두 화살표는 같은 방향(시계 방향)으로 돈다. 아래쪽 화살표는 N의 비공유 전자쌍이 ketene carbonyl 탄소를 공격해 N–C(=O) 결합을 만드는 것을, 위쪽 화살표는 ketene의 C=C 전자가 imine 탄소와 결합하는 것을 나타낸다. 초록 결합이 새로 생긴 두 σ 결합이다. 그림에서는 imine 탄소의 치환기(슬라이드의 O–CH2–다이옥솔레인 곁사슬)를 OR로, 4-methoxyphenyl을 Ar로 줄였고, 생성물의 PhO(점선 쐐기)와 OR(쐐기)는 슬라이드처럼 trans로 그렸다.*

(출처: L15 p.12)

## 15. 1,3-쌍극자와 1,3-쌍극 cycloaddition (1,3-dipoles)

### 15.1 1,3-쌍극자란 무엇인가?

> 개념 문서: [1,3-dipole](../../wiki/개념/1,3-쌍극자.md)

이제 고리 크기를 바꿔 보자. 4원자 diene 대신 3원자짜리 π계가 alkene과 만나면 5원 고리가 생긴다. 이 3원자 성분이 1,3-쌍극자이며, 한쪽 끝은 친전자성, 다른 쪽 끝은 친핵성이라는 이중성을 가진다.

| 이름 | 공명 구조 |
|---|---|
| diazoalkane | ⁺N=N–C⁻R2 ↔ N≡N⁺–C⁻R2 |
| azide* | ⁺N=N–N⁻R ↔ N≡N⁺–N⁻R |
| 니트릴 ylide(nitrile ylide) | RC⁺=N–C⁻R2 ↔ RC≡N⁺–C⁻R2 |
| 니트릴 imine(nitrile imine) | RC⁺=N–N⁻R ↔ RC≡N⁺–N⁻R |
| 니트릴 oxide(nitrile oxide)* | RC⁺=N–O⁻ ↔ RC≡N⁺–O⁻ |
| azomethine ylide | R2C⁺–NR–C⁻R2 ↔ R2C=N⁺R–C⁻R2 |
| nitrone* | R2C⁺–NR–O⁻ ↔ R2C=N⁺R–O⁻ |
| carbonyl oxide* | R2C⁺–O–O⁻ ↔ R2C=O⁺–O⁻ |

(*: 이 강의에서 본격적으로 다루는 것. 슬라이드에서 박스 표시)

니트론을 예로 들어 보자. 니트론은 R(N⁺)(=CH2)–O⁻와 ⁺CH2–NR–O⁻ 두 공명 구조를 오간다. 원자 번호를 O(1), N(2), C(3)로 매기면, N(2)은 이미 4개의 결합을 가진 cation이라 nucleophile이 들어갈 자리가 없지만, C(3)는 두 번째 공명 구조에서 양전하를 띠므로 nucleophile 공격을 받을 수 있다. 반대로 O(1)는 음전하를 가진 친핵성 말단이다.

슬라이드는 "각 화합물의 공액 π계 전자수를 세어 보라"고 묻는다. 답은 모두 4개다. 즉 1,3-쌍극자는 세 원자에 4개의 π 전자가 퍼진, allyl anion과 등전자적인 계다.[5]

(출처: L15 p.13)

### 15.2 [3+2]는 왜 열적으로 잘 되나?

> 개념 문서: [1,3-dipolar cycloaddition](../../wiki/반응/1,3-쌍극자%20고리화%20첨가.md)

1,3-쌍극자 a–b–c(4π)와 dipolarophile d=e(2π)가 만나면 5원자 고리 생성물(cycloadduct)이 생긴다. 이름은 [3+2]지만 전자수로는 4 + 2 = 6, 즉 4n+2이므로 Diels–Alder와 똑같이 열적 supra-supra 경로가 허용된다. 쌍극자가 삼중결합형(a≡b–c)이면 생성물 고리 안에 a=b 이중결합이 하나 남는다.

보충: diene과 1,3-쌍극자의 결정적인 차이는 반응 상대의 폭이다. diene은 친핵성이라 주로 자기 HOMO를 쓰므로 전자 부족 dienophile이 있어야 잘 반응한다. 반면 1,3-쌍극자는 이름 그대로 친핵성 끝과 친전자성 끝을 다 가져서, 상대가 전자 풍부하면 LUMO를, 전자 부족하면 HOMO를 쓴다. 그래서 DA에서는 나쁜 dienophile인 단순 alkene도 좋은 쌍극친화체가 된다. 또 DA의 diene은 s-cis여야 했지만, 니트릴 oxide·azide처럼 직선형인 쌍극자도 cycloaddition을 잘 한다. (보충 근거: Clayden p.901–902)

(출처: L15 p.14)

### 15.3 니트론의 regioselectivity: 누가 HOMO를 쓰나?

> 개념 문서: [nitrone cycloaddition](../../wiki/반응/나이트론%20고리화%20첨가.md)

그런데 니트론은 친전자성과 친핵성을 다 갖고 있으니, alkene의 어느 탄소와 어느 끝이 붙을지는 어떻게 정해질까? 답은 상대 alkene의 성격에 따라 니트론이 역할을 바꾼다는 것이다.

상대가 전자 풍부하거나 단순 alkyl 치환 alkene(R-CH=CH2, EDG)이면, alkene이 HOMO를 쓰고 니트론이 LUMO를 쓴다. 그래서 친핵성 alkene의 말단 CH2가 니트론의 친전자성 탄소를 공격하고, 니트론 O⁻는 치환된 탄소와 결합한다. 생성물은 R이 O 옆 탄소에 있는 5-치환 isoxazolidine이다.

반대로 상대가 전자 부족 alkene(R-CO-CH=CH2, EWG)이면 역할이 뒤바뀐다. 이번에는 니트론이 HOMO, alkene이 LUMO를 쓴다. 니트론의 친핵성 O⁻가 짝지은 첨가처럼 alkene의 친전자성 β-탄소(말단 CH2)를 공격하고, 니트론 탄소는 α-탄소와 결합한다. 그래서 COR이 C4에 있는 4-acyl isoxazolidine이 생긴다.[6]

![니트론과 전자 풍부 alkene의 1,3-쌍극 cycloaddition으로 5-치환 isoxazolidine이 생기는 과정](../../figures/L15/nitrone_cycloaddition.svg)

*그림: 전자 풍부 alkene(파랑, HOMO)과 니트론(빨간 C=N, LUMO)의 경우다. 세 화살표는 모두 같은 방향(시계 방향)으로 돈다. (1) 니트론 O⁻의 비공유 전자쌍(파랑)이 alkene의 치환된 탄소(CHR)와 결합하고, (2) alkene의 π 전자가 말단 CH2에서 니트론의 친전자성 탄소와 결합하며, (3) C=N의 π 전자가 N⁺로 돌아가 N이 중성이 된다. 초록 결합이 새로 생긴 C–O와 C–C 결합이므로 R은 O 옆 탄소(C5)에 놓인다. 전자 부족 alkene에서는 역할이 바뀌어 4-치환 생성물이 된다(본문 참고).*

(출처: L15 p.15)

### 15.4 니트론의 stereoselectivity과 amino alcohol 합성

> 개념 문서: [nitrone cycloaddition](../../wiki/반응/나이트론%20고리화%20첨가.md)

입체화학은 어떨까? Diels–Alder에서는 2차 궤도 상호작용 때문에 endo가 이겼지만, 니트론 cycloaddition에서는 입체 장애가 가장 작은 exo 전이상태가 선호된다. 보충: 왜 endo 규칙이 없을까? endo를 끌어당기던 것은 dienophile의 짝지음 기가 diene "뒤쪽"과 겹치는 2차 상호작용이었는데, 니트론과 단순 alkene에는 쌍극자나 쌍극친화체 뒤쪽에서 겹칠 짝지음 기가 없다. 그래서 입체 장애만 남고, 생성물도 더 안정한 exo가 된다. (보충 근거: Clayden p.902)

고리형 니트론(1-pyrrole린 N-oxide)과 R-CH=CH2를 반응시키면 R이 O 옆 탄소에 exo로 놓인 이환 isoxazolidine이 생긴다. 이것을 Zn/HOAc로 처리하면 약한 N–O 결합이 환원적으로 끊어져, 2-치환 pyrrolidine에 CH2-CH(OH)R가 붙은 1,3-amino alcohol이 된다. 분자 내 버전도 가능하다. 2-allyl-1-pyrrole린 N-oxide는 분자 내 1,3-쌍극 cycloaddition으로 bridged 삼환 isoxazolidine을 만들고, Zn/HOAc로 N–H와 OH를 가진 이환 amino alcohol이 된다. 즉 니트론 cycloaddition은 "1,3-amino alcohol을 입체선택적으로 만드는 도구"로 쓰인다. 보충: 1,3-쌍극 cycloaddition의 가치는 헤테로고리 그 자체보다 그다음 변환에 있다. cycloaddition에서 만든 C–C와 C–O 결합은 남기고, 원래 쌍극자에 있던 약한 N–O 결합만 LiAlH4, Zn/HOAc, H2/Ni 같은 환원제로 끊으면 나머지 골격과 입체화학은 그대로 NH와 OH가 1,3 관계로 드러난다. (보충 근거: Clayden p.902)

니트론 자체는 간단히 만든다. aldehyde RCHO와 N-치환 hydroxylamine RNHOH를 축합시키면(imine 형성과 같은 원리, -H2O) R-CH=N⁺(R)-OH가 되고, 양성자가 빠지면 니트론 R-CH=N⁺(R)-O⁻가 된다(→ imine 형성 메커니즘 문서 참고).

(출처: L15 p.16)

### 15.5 니트릴 oxide는 어떻게 만드나?

> 개념 문서: [nitrile oxide cycloaddition](../../wiki/반응/나이트릴%20옥사이드%20고리화%20첨가.md)

니트릴 oxide도 반응계 안에서 만든다.[7] acetaldehyde를 예로 들면 전체 반응은 MeCHO --[1. H2N-OH; 2. Cl2; 3. NEt3]--> Me-C≡N⁺-O⁻이며, 과정은 다음과 같다.

1. acetaldehyde와 hydroxylamine이 축합해 옥심 MeCH=N-OH가 된다.
2. OH 산소의 비공유 전자쌍이 밀어주는 힘으로 C=N의 탄소가 Cl–Cl을 공격하고(Cl⁻ 이탈), Me-CH(Cl)-N=O⁺H가 된다.
3. C–H 양성자가 빠지면서 C=N이 다시 생겨 hydroxy모일 chloride(hydroximoyl chloride) MeC(Cl)=N-OH가 된다.
4. NEt3가 O–H 양성자를 떼어 MeC(Cl)=N-O⁻를 만든다.
5. 산소 anion의 전자가 N 쪽으로 밀려 들어가며 Cl⁻가 떨어져 나가고 Me-C≡N⁺-O⁻가 완성된다.

보충: 4–5단계는 이어진 굽은 화살표 하나로 그릴 수 없어서 "O–H deprotonation → Cl⁻ 이탈"의 두 단계로 나누어 그린다. 떨어지는 H(O 위)와 Cl(C 위)이 1,3 관계라서 흔한 β-제거가 아니라 γ-제거에 해당한다. 2단계에서 옥심의 탄소가 Cl2를 공격할 수 있는 것은 옥심이 enol과 비슷하게 N–OH 쪽 전자를 밀어 주기 때문이다. (보충 근거: Clayden p.902–903)

![옥심이 Cl2와 반응해 hydroxy모일 chloride가 되는 과정](../../figures/L15/nitrile_oxide_chlorination.svg)

*그림: 2–3단계. 1단계에서 파란 OH 산소의 비공유 전자쌍이 N–O 사이로 밀려 들어가 N=O⁺를 만들고, 그 힘으로 파란 C=N의 π 전자가 빨간 Cl–Cl의 Cl 하나를 공격하며, Cl–Cl 결합 전자는 Cl⁻로 떨어져 나간다. 2단계에서는 C–H 결합 전자가 C–N 사이로 들어가 C=N을 다시 만들고(H⁺ 이탈), 빨간 N=O⁺의 π 전자가 산소로 돌아가 OH가 된다. 초록 결합이 새로 생긴 C–Cl과 C=N이다.*

![hydroxy모일 chloride가 NEt3에 의해 니트릴 oxide가 되는 과정](../../figures/L15/nitrile_oxide_elimination.svg)

*그림: 4–5단계. 1단계에서 파란 NEt3의 전자쌍이 빨간 O–H의 H를 떼고, O–H 결합 전자는 산소에 남아 O⁻가 된다. 2단계는 슬라이드 그림대로 파란 N의 비공유 전자쌍이 C=N 사이로 들어가 C≡N⁺를 만들고, 빨간 C–Cl 결합 전자가 Cl⁻로 떨어져 나간다. O⁻는 그대로 남으므로 생성물은 Me–C≡N⁺–O⁻다. 초록 결합이 새로 생긴 삼중 결합이다.*

(출처: L15 p.17)

### 15.6 니트릴 oxide의 stereospecificity과 regioselectivity

> 개념 문서: [nitrile oxide cycloaddition](../../wiki/반응/나이트릴%20옥사이드%20고리화%20첨가.md)

슬라이드 p.18은 생성물 칸을 비워 둔 퀴즈이고, p.19가 정답이다. 협동적 supra-supra 반응이므로 alkene의 기하는 그대로 보존된다. 그래서 R'-C≡N⁺-O⁻가 (Z)-RCH=CHR와 만나면 4,5-cis-이치환 isoxazoline(4,5-dihydroisoxazole, C3에 R')이, (E)-RCH=CHR와 만나면 4,5-trans-이치환 isoxazoline이 생긴다. alkyne과 만나면 이야기가 조금 달라지는데, 고리에 이중결합이 두 개가 되어 방향족 isoxazole이 된다. 말단 alkyne HC≡C-R에서는 치환된 탄소가 O와 결합하므로 R이 C5(O 옆)에 오는 3,5-이치환 isoxazole이 생긴다.

보충: 이 regioselectivity은 니트론과 같은 논리다. 니트릴 oxide cycloaddition을 주도하는 것은 alkene(또는 alkyne)의 HOMO와 니트릴 oxide의 LUMO다. 친핵성인 말단 CH2(CH) 탄소가 니트릴 oxide의 친전자성 탄소와 결합하므로, 남은 치환된 탄소가 O와 결합해 R이 C5에 놓인다. isoxazole이 특히 안정한 것은 고리의 C=C, C=N π 전자 4개에 O의 비공유 전자쌍 2개가 더해진 6π 방향족 고리이기 때문이다. (보충 근거: Clayden p.903)

![니트릴 oxide와 (Z)-alkene의 1,3-쌍극 cycloaddition으로 cis-isoxazoline이 생기는 과정](../../figures/L15/nitrile_oxide_cycloaddition.svg)

*그림: 니트릴 oxide와 (Z)-alkene의 협동적 [3+2]. 빨간 C≡N⁺이 LUMO 쪽(친전자성 탄소), 파란 C=C와 O⁻가 전자를 주는 쪽이다. 세 화살표는 모두 같은 방향(시계 방향)으로 돈다. (1) O⁻의 비공유 전자쌍이 alkene 오른쪽 탄소와 결합하고, (2) alkene의 π 전자가 니트릴 oxide의 탄소와 결합하며, (3) C≡N의 π 결합 하나가 N⁺로 돌아가 N이 중성이 된다. 초록 결합이 새로 생긴 C–C와 C–O 결합이고, 고리 안에는 C=N이 하나 남는다. alkene에서 같은 쪽에 있던 두 R은 생성물에서도 같은 쪽(둘 다 쐐기)이므로 4,5-cis isoxazoline이 된다.*

(출처: L15 p.18–19)

### 15.7 isoxazoline은 무엇으로 바뀌나?

> 개념 문서: [nitrile oxide cycloaddition](../../wiki/반응/나이트릴%20옥사이드%20고리화%20첨가.md), [aldol reaction](../../wiki/반응/알돌%20반응.md)

이렇게 만든 isoxazoline은 그 자체보다 "다른 것으로 바뀌는 능력"이 더 쓸모 있다. LiAlH4로 환원하면 C=N이 환원되고 N–O가 끊어져 1,3-amino alcohol R-CH(NH2)-CH2-CH(OH)-R가 된다. 한편 H2/Ni와 물로 처리하면 N–O 결합이 수소화 분해되어 β-hydroxy imine이 되고, 이것이 물에 가수분해되어 β-hydroxy ketone, 즉 aldol 생성물이 된다. 여기서 놀라운 점은 입체정보의 전달이다. cis-isoxazoline은 syn-aldol을, trans-isoxazoline은 anti-aldol을 준다. 즉 alkene의 Z/E 기하가 고리의 cis/trans를 거쳐 aldol의 syn/anti로 이어진다(→ [L8](L08_Aldol_Reactions.md) aldol reaction 문서 참고).

(출처: L15 p.20)

## 16. ozone 분해 (Ozonolysis)

> 개념 문서: [pericyclic reaction](../../wiki/개념/페리고리%20반응.md)

### 16.1 후처리에 따라 무엇이 나오나?

> 개념 문서: [ozonolysis](../../wiki/반응/오존%20분해.md)

ozone은 C=C를 완전히 끊어 carbonyl 화합물로 만든다. 그런데 같은 ozone 처리 뒤에도 두 번째 단계 시약에 따라 생성물이 달라진다. Me2S로 처리하면 aldehyde(이치환 탄소는 ketone)가, H2O2로 처리하면 carboxylic acid이, NaBH4로 처리하면 alcohol이 생긴다.[8]

슬라이드의 예는 norbornene이다. 1. O3, 2. Me2S로 처리하면 C=C가 끊어지며 두 탄소가 모두 CHO가 되고, 남은 골격(다리 CH2 포함)은 5원 고리가 된다. 원래 C=C의 두 탄소가 같은 면 관계를 유지하므로 두 CHO는 cis이다. 즉 생성물은 cis-cyclopentane-1,3-dicarbaldehyde다.

(출처: L15 p.21)

### 16.2 잠깐, 성층권의 ozone

> 개념 문서: [ozone](../../wiki/시약/오존.md)

강의는 여기서 잠시 ozone층 이야기를 한다. 성층권에서는 O2가 자외선에 광분해되어 O 원자가 생기고(느림), O + O2 → O3가 된다. O3는 자외선을 흡수해 다시 O2 + O로 쪼개지고 재결합하기를 빠르게 반복하며 자외선을 열로 바꾼다. O3가 없어지는 것은 O 원자와의 반응이나 염소 같은 미량 기체에 의해서다(느림). 그런데 여러 자유 radical이 ozone을 파괴하면서 ozone 구멍이 생겼고, 지표에 도달하는 자외선이 늘어 건강 문제가 걱정거리가 되었다. 1987년 몬트리올 Montreal Protocol은 CFC(염화불화탄소) 같은 ozone 파괴 물질을 단계적으로 퇴출하기 위해 만들어졌다.

(출처: L15 p.22)

### 16.3 ozone 분해는 사실 1,3-쌍극 cycloaddition 3연타다

> 개념 문서: [1,3-dipolar cycloaddition](../../wiki/반응/1,3-쌍극자%20고리화%20첨가.md), [ozonolysis](../../wiki/반응/오존%20분해.md)

그렇다면 ozone은 어떻게 C=C를 끊을까? 핵심은 carbonyl oxide(R2C=O⁺–O⁻ ↔ R2C⁺–O–O⁻)가 1,3-쌍극자라는 것, 그리고 ozone 자체도 1,3-쌍극자라는 것이다.

1. 1,3-쌍극 cycloaddition: O3가 alkene과 [3+2]로 반응해 1차 ozonide(primary ozonide, O–O–O가 연속된 1,2,3-trioxolane)를 만든다.
2. 역 1,3-쌍극 cycloaddition(retro-[3+2]): 약한 O–O 결합과 C–C 결합이 끊어지며 aldehyde RCHO와 carbonyl oxide RCH=O⁺–O⁻로 쪼개진다.
3. aldehyde가 180° 돌아 반대 방향으로 정렬한다.
4. 다시 1,3-쌍극 cycloaddition: carbonyl oxide가 aldehyde의 C=O와 반응해 1,2,4-trioxolane(2차 ozonide, 슬라이드 명칭 "trioxolane")을 만든다.
5. 환원 후처리: Me2S의 황이 O–O 결합의 산소를 공격하면 고리가 무너지며 DMSO(Me2S⁺–O⁻)와 RCHO 두 분자가 생긴다.

즉 정방향 → 역방향 → 정방향의 cycloaddition이 차례로 일어나는 셈이다.

보충: 각 단계의 "왜?"는 결합 세기로 설명된다. O–O 단일 결합(약 140 kJ/mol)은 앞에서 "약하다"고 했던 N–O 결합(약 180 kJ/mol)보다도 훨씬 약하고, 1차 ozonide에는 이런 O–O 결합이 두 개나 있다. 그래서 만들어지자마자 역 cycloaddition으로 쪼개진다. carbonyl oxide는 왔던 방향 그대로 다시 붙을 수도 있지만, 친핵성 O⁻가 aldehyde의 친전자성 carbonyl 탄소를 공격하는 배향을 훨씬 선호하므로 aldehyde가 180° 돌아 1,2,4-trioxolane이 된다. 이 ozonide도 폭발성이라 분리하지 않고 Me2S나 Ph3P로 바로 분해한다. (보충 근거: Clayden p.906–907)

![ozone과 alkene의 1,3-쌍극 cycloaddition으로 1차 ozonide가 생기는 과정](../../figures/L15/ozonolysis_step1.svg)

*그림: 1단계. 파란 O⁻(ozone의 친핵성 말단)와 파란 C=C, 빨간 말단 O와 O=O 결합(친전자성 말단)이다. 세 화살표는 같은 방향(반시계 방향)으로 돈다. (1) O⁻의 전자쌍이 alkene 왼쪽 탄소와 결합하고, (2) alkene의 π 전자가 오른쪽 말단 O와 결합하며, (3) O=O의 π 전자가 가운데 O⁺로 가서 중성이 된다. 초록 결합이 새로 생긴 두 C–O 결합이고, 결과는 O–O–O가 이어진 1차 ozonide다.*

![1차 ozonide가 역 1,3-쌍극 cycloaddition으로 aldehyde와 carbonyl oxide로 쪼개지는 과정](../../figures/L15/ozonolysis_retro.svg)

*그림: 2단계. 빨간 O–O와 C–C가 끊어지는 결합이다. 세 화살표는 같은 방향(시계 방향)으로 돈다. (1) 약한 O–O 결합 전자가 가운데 O로 가서 O⁻가 되고, (2) C–C 결합 전자가 왼쪽 C=O를 만들어 aldehyde가 되며, (3) 오른쪽 고리 O의 비공유 전자쌍(파랑)이 C=O⁺를 만들어 carbonyl oxide가 된다. 초록 결합이 새로 생긴 두 C=O다. 이어서 aldehyde가 180° 돌아 carbonyl oxide와 다시 [3+2]를 하면 trioxolane이 된다.*

![180° 돌아 정렬한 aldehyde와 carbonyl oxide가 1,3-쌍극 cycloaddition으로 1,2,4-trioxolane을 만드는 과정](../../figures/L15/ozonolysis_recombination.svg)

*그림: 3단계. 180° 돌아 반대 방향으로 정렬한 aldehyde(빨간 C=O)와 carbonyl oxide(파란 O⁻)의 1,3-쌍극 cycloaddition이다. 세 화살표는 같은 방향(반시계 방향)으로 돈다. (1) O⁻의 전자쌍이 aldehyde의 친전자성 carbonyl 탄소와 결합하고, (2) aldehyde C=O의 π 전자가 carbonyl oxide의 탄소와 결합하며, (3) C=O⁺의 π 전자가 O⁺로 돌아가 중성이 된다. 초록 결합이 새로 생긴 두 C–O 결합이고, 결과는 O–O 결합이 하나뿐인 1,2,4-trioxolane(2차 ozonide)이다.*

(출처: L15 p.23)

### 16.4 과산화물은 양날의 검

> 개념 문서: [ozonolysis](../../wiki/반응/오존%20분해.md)

trioxolane처럼 O–O 결합을 가진 과산화물은 폭발성일 수 있으므로 주의해야 한다. 대표적인 예가 triacetone triperoxide(TATP)다.[9] 반면 같은 O–O 결합이 약이 되기도 한다. endoperoxide를 가진 항말라리아제 artemisinin과,[10] trioxolane 고리를 가진 합성 항말라리아 화합물이 그 예다.

(출처: L15 p.24)

## cycloaddition 반응 중간 정리

여기까지 본 cycloaddition을 한데 모으면 [4+2] (Diels–Alder), [6+4] (triene + diene), [4+3] (allyl cation), 광화학 [2+2], 열적 [2+2], [3+2] (1,3-쌍극 cycloaddition)가 있다. 반응이 가능한지는 FMO의 대칭(Woodward–Hoffmann 규칙)이 정하고, regioselectivity은 FMO 계수가 가장 큰 원자끼리 결합한다는 원리로 정해진다. 열적 반응에서는 HOMO–LUMO가, 광화학 반응에서는 슬라이드 표현으로 "LUMO–LUMO"가 기준인데, 이는 빛을 받아 전자 하나가 들어간 원래 LUMO와 바닥상태 상대의 LUMO의 상호작용을 뜻한다. stereoselectivity은 [4+2]에서 2차 궤도 상호작용에 의한 endo 선호, stereospecificity은 각 반응물 내 기하 보존이다.

(출처: L15 p.25)

## 17. siloxydiene과 aminosiloxydiene (Siloxydienes and Aminosiloxydienes)

### 17.1 diene에 siloxy group을 다는 이유

> 개념 문서: [Danishefsky diene](../../wiki/시약/대니셰프스키%20다이엔.md)

Diels–Alder를 빠르게 하려면 diene을 전자 풍부하게 만들면 된다. 그래서 X형 치환기인 siloxy group(-OSiR3), 알콕시기, 아미노기를 붙인 diene들이 개발되었다. ketone 유래 2-siloxydiene CH2=C(OSiR3)-CH=CH2, 1-siloxydiene R3SiO-CH=CH-CH=CH2, Danishefsky diene CH2=C(OSiR3)-CH=CH-OR', Brassard diene CH2=C(OR')-CH=C(OR'')(OSiR3), Rawal diene CH2=C(OSiR3)-CH=CH-NR'2가 그것이다.

이 diene들의 진짜 장점은 생성물을 cyclohexenone으로 바꿀 수 있다는 데 있다. Danishefsky diene을 예로 들면 다음과 같다.

1. Danishefsky diene과 diene오필이 Diels–Alder 반응을 하면 silyl enol ether와 OMe를 가진 cyclohexene이 생긴다.
2. H⁺로 처리하면 silyl enol ether가 ketone으로 가수분해되고, ketone의 β-위치에 있는 OMe가 β-elimination되어 cyclohexenone이 된다.

C1의 OMe와 C3의 OSiR3가 같은 방향으로 regioselectivity을 밀어주므로 선택성도 높다.[11]

(출처: L15 p.26)

### 17.2 키랄 Lewis 산으로 한쪽 거울상만 만들기

> 개념 문서: [비대칭 Diels–Alder reaction](../../wiki/반응/비대칭%20딜스-알더%20반응.md)

Rawal형 aminosiloxydiene(TBSO, N(R1)CO2Me, 1)과 α,β-unsaturated aldehyde(R2, R3, 2, 2.0 당량)를 키랄 Cr(III)-salen 촉매 3(5 mol%), 4Å MS, CH2Cl2 조건에서 반응시키면 고도로 작용기화된 cyclohexene 4가 위치·입체선택적으로 생긴다. 생성물에서 카바메이트 N과 CHO는 이웃 탄소(ortho 관계)에 놓이고, R2와 CHO를 가진 4차 탄소가 생긴다. 촉매 3은 키랄 trans-1,2-diaminocyclohexane 유래 salen–Cr(III) 착물(3a: X = BF4, 3b: X = SbF6)로, aldehyde carbonyl에 배위해 LUMO를 낮추는 동시에 키랄 환경으로 한쪽 면을 가린다.

(출처: L15 p.27)

### 17.3 금속 없이 수소결합만으로: TADDOL

Lewis 산 대신 수소결합으로도 같은 일을 할 수 있을까? TADDOL 7(Ar = 1-naphthyl)이 그 답이다. Rawal형 diene(NMe2, TBSO; 2.0 당량)과 2-치환 acrolein CH2=C(R)CHO를 TADDOL 7(20 mol%), toluene, -80 °C, 2일 조건에서 반응시키고, 이어서 1) LiAlH4, 2) HF로 처리하면 4-R-4-(hydroxymethyl)cyclohex-2-enone이 생긴다. LiAlH4는 CHO를 CH2OH로 환원하고, HF는 TBS silyl enol ether를 ketone으로 바꾸며, 이때 β-위치의 NMe2가 떨어져 나가 enone이 만들어진다.

| R | 수율 (%) | ee (%) |
|---|---|---|
| H | 77 | 73 |
| Me | 83 | 91 |
| Et | 83 | 88 |
| iPr | 81 | 92 |
| PhCH2 | 82 | 89 |
| TBSO(CH2)2 | 80 | 86 |

TADDOL의 두 OH 중 하나는 다른 OH와 분자 내 수소결합을 하고, 남은 OH가 aldehyde carbonyl 산소와 수소결합해 aldehyde를 활성화하면서 키랄 환경을 제공한다.

(출처: L15 p.28)

### 17.4 실전 응용: 타버소닌의 비대칭 합성

이 방법론은 천연물 합성에 바로 쓰였다.

1. 비닐로거스 카바메이트 5(20 mmol)를 NaHMDS, TBSCl(-78 °C, THF)로 처리해 ketone을 silyl enol ether로 바꾸면 aminosiloxydiene 1a가 된다.
2. 1a와 2-ethylacrolein 2a(24 mmol)를 촉매 3b(5 mol%), 4Å MS, CH2Cl2, -40 °C, 2일 조건에서 반응시키면 Et/CHO 4차 탄소를 가진 4aa가 84%, 95% ee로 생긴다.
3. 4aa를 Wittig reaction(n-BuLi, Ph3PMeBr, THF)시켜 CHO를 비닐로 바꾼 6을 얻는다(정제 없이 사용).
4. 여러 단계를 거쳐 (+)-tabersonine(X = H)과 (+)-16-methoxytabersonine(X = OMe)에 도달한다.

(출처: L15 p.29)

## 18. 생체접합 화학 (Bioconjugate Chemistry)

> 개념 문서: [pericyclic reaction](../../wiki/개념/페리고리%20반응.md), [Woodward–Hoffmann rules](../../wiki/개념/우드워드-호프만%20규칙.md)

### 18.1 세포 안에서 cycloaddition을 일으키려면?

> 개념 문서: [click reaction](../../wiki/반응/클릭%20반응.md), [역전자 요구 Diels–Alder reaction](../../wiki/반응/역전자%20요구%20딜스-알더%20반응.md)

cycloaddition을 살아 있는 세포 안에서 일으키려면 무엇이 필요할까? 슬라이드는 네 가지 조건을 든다. 선택성(세포 속 수많은 작용기와는 반응하지 않을 것), 반응속도(낮은 농도에서도 빠를 것), 화학적 안정성, 생체적합성이다.[12]

첫 번째 답은 변형 촉진 azide–alkyne cycloaddition(strain-promoted azide–alkyne cycloaddition, SPAAC)다. azide(1,3-쌍극자)와 cyclooctyne이 [3+2]로 반응해 융합 1,2,3-triazole을 만든다. 8원 고리에 억지로 끼워 넣은 삼중결합의 긴장 덕분에, 세포에 독성이 있는 구리 촉매 없이도 반응이 진행된다.

두 번째 답은 1,2,4,5-tetrazine과 trans-cyclooctene(TCO)의 역전자요구 Diels–Alder(inverse-electron-demand DA) 반응이다. 보통의 DA와 달리 여기서는 diene(tetrazine)이 전자 부족하고, 긴장된 TCO가 HOMO가 높은 diene오필 역할을 한다.

1. tetrazine과 TCO가 [4+2]로 반응해 다리걸친 이환 intermediate를 만든다.
2. 역-DA로 N2가 빠져나간다(비가역적인 추진력).
3. 4,5-dihydropyridazine이 tautomerize해 1,4-dihydropyridazine(N-H)이 된다.

이런 클릭 반응은 약물, 생체분자(peptide, 당), 고분자, 표면 기능화, 첨단 생체재료(hydrogel, 나노입자) 등에 두루 쓰인다.

(출처: L15 p.30)

### 18.2 실제로 어디에 쓰나?

> 개념 문서: [click reaction](../../wiki/반응/클릭%20반응.md)

생체 영상에서는 Ac4ManNAz를 세포에 먹여 대사적 metabolic glycoengineering으로 연골세포 표면 당에 azide를 심고, DBCO-650(cyclooctyne-형광체)으로 Cu-free 클릭 반응을 일으켜 표지한다. 이중 표지도 가능하다. 세포 표면에 cyclopropene 당과 azide 당을 함께 심은 뒤 tetrazine-Cy3(DAinv)와 cyclooctyne-AlexaFluor488(SPAAC)을 동시에 15분 처리하면, 두 반응이 서로 간섭하지 않고 두 당을 각각 다른 색으로 보여 준다.

신약 발견에서는 표적 효소에 alkyne 조각과 azide 조각이 각각 결합한 뒤, 효소 위에서 triazole이 만들어지게 하여 결합력 높은 저해제를 찾는다(in situ 발견). 항암 치료에서는 두 단계 pretargeting이 쓰인다. 친화성 리간드에 약물을 직접 연결하는 대신, TCO를 단 리간드를 먼저 보내 표적에 붙게 하고, 시간이 지난 뒤 tetrazine-약물 소분자를 투여해 표적에서만 결합시킴으로써 독성을 줄인다.

(출처: L15 p.31)

## 최종 정리: cycloaddition란 결국 무엇인가

cycloaddition은 다양한 크기의 고리를 만드는 pericyclic 반응이다. 허용 여부는 FMO와 Woodward–Hoffmann 규칙이 정한다. 열적으로는 총 전자수 4n+2가 허용되고, 열적 [2+2] (suprafacial–antarafacial)는 특수한 경우다. 광화학적으로는 4n(예: [2+2])이 허용된다. 이 반응들은 입체특이적, 입체선택적, 위치선택적이며, Lewis 산이나 수소결합으로 촉매할 수 있고, 작용기화된 고리 구조 합성에서 생체접합까지 폭넓게 응용된다. 참고로 개요 슬라이드(p.2)에는 광화학 [2+2]가 첫 항목으로 올라 있지만, 이 강의 파일에는 그에 대한 별도 상세 슬라이드가 없고 규칙만 p.25와 p.32에 언급된다.

(출처: L15 p.2, p.32)

## 흔한 오해

- 열적 [2+2]는 모든 alkene에서 안 된다고 생각하기 쉽지만, 사실은 ketene·isocyanate처럼 직교 π 결합을 가진 누적 이중결합 화합물은 supra-antara 경로로 열적 [2+2]를 한다.
- 광화학과 열적 규칙을 헷갈려 "[2+2]는 열적으로 허용"이라고 외우기 쉽지만, 사실은 일반적인 supra-supra [2+2] (4n)는 광화학적으로 허용되고 열적으로는 금지다. 열적 허용은 4n+2다.
- ketene [2+2]의 regioselectivity은 외워야 하는 규칙이라고 생각하기 쉽지만, 사실은 "carbonyl 탄소가 친전자성"이라는 한 가지 원리로 풀린다. 친핵성 원자(alkene의 더 친핵성인 탄소, imine N)가 carbonyl 탄소에 붙는다.
- ketene·isocyanate의 열적 [2+2]는 언제나 협동적이고 입체특이적이라고 생각하기 쉽지만, 사실은 바이닐 sulfide·enol ether처럼 매우 전자 풍부한 alkene과 CSI의 반응은 단계적으로 일어나 E/Z 혼합물에서도 trans 생성물만 준다(입체선택적). (보충 근거: Clayden p.901)
- 단순 alkene은 DA에서 나쁜 dienophile이니 1,3-쌍극 cycloaddition에서도 나쁠 것이라고 생각하기 쉽지만, 사실은 1,3-쌍극자는 HOMO와 LUMO를 상황에 따라 바꿔 쓰므로 단순 alkene도 좋은 쌍극친화체다. (보충 근거: Clayden p.901)
- CSI + 2-치환 alkene에서 N이 덜 치환된 탄소에 붙는다고 생각하기 쉽지만, 사실은 양전하를 더 잘 견디는 더 치환된 탄소가 N과 결합해 N 옆에 4차 탄소가 생긴다.
- [3+2]이니 5전자 반응이라고 생각하기 쉽지만, 사실은 4π + 2π = 6전자이며 그래서 열적으로 허용된다.
- cycloaddition은 다 endo를 선호한다고 생각하기 쉽지만, 사실은 니트론 cycloaddition은 입체 장애가 작은 exo를 선호한다. endo 규칙은 [4+2]의 이야기다.
- 니트론은 항상 같은 방향으로 붙는다고 생각하기 쉽지만, 사실은 EDG alkene과는 5-치환, EWG alkene과는 4-치환 생성물을 준다(슬라이드 기준). 상대에 따라 HOMO/LUMO 역할이 바뀌기 때문이다.
- isoxazole, isoxazoline, isoxazolidine을 같은 것으로 생각하기 쉽지만, 사실은 각각 방향족(니트릴 oxide + alkyne), 이중결합 하나(니트릴 oxide + alkene), 완전 포화(니트론 + alkene)로 다르다.
- isoxazoline을 환원하면 항상 amino alcohol이 된다고 생각하기 쉽지만, 사실은 LiAlH4는 amino alcohol을, H2/Ni + H2O는 질소가 가수분해로 빠진 β-hydroxy ketone(aldol 생성물)을 준다. cis → syn, trans → anti다.
- ozone 분해는 ozone이 한 번 붙고 끝나는 반응이라고 생각하기 쉽지만, 사실은 1,3-쌍극 cycloaddition → 역반응 → 재결합 cycloaddition의 세 단계를 거치며 최종 ozonide는 1,2,4-trioxolane이다.
- H2O2 후처리는 모든 탄소를 carboxylic acid으로 만든다고 생각하기 쉽지만, 사실은 H를 가진(aldehyde가 될) 탄소만 산이 되고 ketone 쪽은 ketone으로 남는다.
- 역전자요구 DA도 보통 DA처럼 diene이 전자 풍부하다고 생각하기 쉽지만, 사실은 diene(tetrazine)이 전자 부족하고 diene오필(TCO)이 전자 풍부/긴장된 쪽이다.

## 반응 정리표

| 반응 | 시약/조건 | 생성물 | regioselectivity | 입체화학 | 비고 |
|---|---|---|---|---|---|
| DA: 1-acetoxybutadiene + (E)-crotonaldehyde | 가열 | 2-acetoxy-6-methylcyclohex-3-ene-1-carbaldehyde | ortho (OAc 옆에 CHO) | OAc/CHO cis(endo), CHO/Me trans(E 보존) | 라세미 (p.3) |
| ketene + alkene [2+2] | heat | cyclobutanone | alkene 친핵성 탄소 → ketene C=O 탄소 | alkene 기하 보존 | supra-antara (p.6–7) |
| Cl2CHCOCl → Cl2C=C=O, + cyclopentadiene | Et3N | 7,7-dichlorobicyclo로[3.2.0]hept-2-en-6-one | C=O가 CH2 옆 접합 탄소, CCl2가 allyl 접합 탄소 | cis 융합 | [2+2] > [4+2] (p.8) |
| ketene + imine (Staudinger) | PhOCH2COCl, Et3N | 3-페녹시 β-락탐 (92%) | imine N → ketene C=O 탄소 | 그림상 3,4-trans | p.12 |
| CSI + CH2=C(Me)CH2Cl | 이후 NaHCO3, H2O | 4-(chloromethyl)-4-methyl아제티딘-2-one | 3차 탄소가 N과 결합 | – | SO3 이탈 (p.12) |
| 니트론 + R-CH=CH2 (EDG) | 열 | 5-치환 isoxazolidine | 니트론 C–CH2, O–CHR | exo TS | 쌍극자 LUMO (p.15–16) |
| 니트론 + CH2=CH-COR (EWG) | 열 | 4-acyl isoxazolidine | O–CH2(β), C–CH(COR) | – | 쌍극자 HOMO (p.15) |
| isoxazolidine N–O 절단 | Zn, HOAc | 1,3-amino alcohol | – | 입체 보존 | p.16 |
| 니트론 제조 | RCHO + RNHOH | 니트론 | – | – | 축합 (p.16) |
| 니트릴 oxide 제조 | 1. NH2OH 2. Cl2 3. NEt3 | R-C≡N⁺-O⁻ | – | – | hydroxy모일 chloride 경유 (p.17) |
| 니트릴 oxide + Z/E alkene | – | isoxazoline | R'는 C3 | Z → cis, E → trans | 입체특이적 (p.19) |
| 니트릴 oxide + 말단 alkyne | – | 3,5-이치환 isoxazole | R이 C5(O 옆) | – | p.19 |
| isoxazoline 환원 | LiAlH4 | 1,3-amino alcohol | – | – | p.20 |
| isoxazoline 환원/가수분해 | H2/Ni, H2O | β-hydroxy ketone | – | cis → syn, trans → anti | aldol 등가체 (p.20) |
| ozone 분해 | 1. O3 2. Me2S | aldehyde/ketone + DMSO | – | 노보넨 → cis-1,3-dialdehyde | p.21, 23 |
| ozone 분해 | 1. O3 2. H2O2 | carboxylic acid | – | – | p.21 |
| ozone 분해 | 1. O3 2. NaBH4 | alcohol | – | – | p.21 |
| Danishefsky diene DA | DA 후 H⁺ | cyclohexenone | OMe/OSiR3 협력 | – | p.26 |
| Rawal형 diene + 엔알 | Cr-salen 3 (5 mol%), 4Å MS, CH2Cl2 | 작용기화 cyclohexene | N과 CHO ortho | 거울상선택적 | p.27, 29 |
| Rawal형 diene + 2-치환 acrolein | TADDOL 7, toluene, -80 °C; LiAlH4; HF | 4,4-이치환 cyclohexenone | – | 73–92% ee | H-결합 촉매 (p.28) |
| SPAAC | azide + cyclooctyne | triazole | – | – | Cu-free (p.30) |
| IEDDA | tetrazine + TCO | dihydropyridazine + N2 | – | – | 역-DA로 N2 방출 (p.30) |

---

## 연습 문제

1. (p.3) 1-acetoxy-1,3-butadiene과 (E)-crotonaldehyde의 Diels–Alder 생성물을 regioselectivity, endo 선택성, stereospecificity 순서로 결정하고 상대 배치를 서술하라.

2. (p.4–5) 다음 화합물을 전자 풍부(X/C형 치환)와 전자 부족(Z형 치환)으로 분류하라: 2-methyl프로펜, methyl acrylate, cyclohexanone pyrrolidine enamine, cyclohex-2-enone, lithium cyclohexeneolate, benzonitrile, 2-methoxy-1,3-butadiene. 또 -SiMe3는 어떤 유형의 치환기인가?

3. (p.6–7, p.32) 일반 alkene 두 분자는 가열해도 [2+2]가 일어나지 않지만 dimethylketene과 cis-2-butene은 가열하면 cyclobutanone을 준다. 그 이유를 궤도 관점에서 설명하고 생성물의 입체화학을 쓰라.

4. (p.8) dichloroacetyl chloride를 cyclopentadiene 존재 하에 Et3N으로 처리하였다. (a) 반응성 intermediate와 그 생성 메커니즘, (b) 최종 생성물과 regioselectivity의 근거를 쓰라.

5. (p.12) 2-(chloromethyl)프로펜과 chlorosulfonyl isocyanate(CSI)를 반응시킨 뒤 NaHCO3 수용액으로 처리하였다. 각 단계의 생성물을 쓰고 regioselectivity을 설명하라.

6. (p.15) N-methyl니트론 CH2=N⁺(Me)–O⁻를 (a) 1-hexene, (b) methyl vinyl ketone(CH2=CH-COCH3)과 반응시킬 때 주생성물 isoxazolidine의 치환 위치를 예측하고, 각각 어느 성분이 HOMO를 사용하는지 쓰라.

7. (p.18, 빈칸 문제) R'-C≡N⁺-O⁻와 (a) (Z)-RCH=CHR, (b) (E)-RCH=CHR, (c) 말단 alkyne HC≡C-R 의 생성물을 쓰라. 이어서 (a)의 생성물을 H2/Ni, H2O로 처리하면 무엇이 생기는가? (p.20)

8. (p.21, 23) 노보넨을 1. O3, 2. Me2S로 처리하였다. 생성물을 쓰고, 1차 ozonide에서 최종 생성물까지 거치는 intermediate를 순서대로 나열하라. 2단계 시약을 H2O2로 바꾸면 생성물은?

---

## 정답 및 해설

1. 정답: 2-acetoxy-6-methylcyclohex-3-ene-1-carbaldehyde, OAc/CHO cis, CHO/Me trans (라세미).
   해설: (1) diene C1의 X형 OAc → "ortho" 규칙에 따라 CHO 탄소가 OAc 탄소 옆에 결합(Me 탄소는 diene C4와 결합). (2) endo 전이상태에서 CHO가 diene 아래 위치 → (E)-1-치환 diene의 C1 치환기와 cis. (3) E-diene오필 → CHO와 Me trans 보존. 슬라이드 박스와 일치. (출처: L15 p.3)

2. 정답: 전자 풍부 — 2-methyl프로펜(Me, X), enamine(NR2, X), lithium enolate(O⁻, X), 2-methoxybutadiene(OMe, X). 전자 부족 — methyl acrylate(CO2Me, Z), cyclohexenone(C=O, Z), benzonitrile(CN, Z). -SiMe3는 Z형(π 받개이지만 σ 주개).
   해설: X형은 π 주개, Z형은 π 받개. 슬라이드 p.5의 점선 왼쪽/오른쪽 배치가 이 분류에 해당. (출처: L15 p.4–5)

3. 정답: ketene은 누적 이중결합으로 C=C π와 C=O π가 서로 직교. alkene HOMO가 ketene C=O LUMO와 결합하면서 중앙 탄소의 직교 p 궤도와도 결합할 수 있어, ketene이 antarafacial 성분인 supra-antara [π2s + π2a] 경로가 열적으로 허용된다. 일반 alkene의 supra-supra [2+2]는 4전자(4n)라 열적으로 금지이고, supra-antara는 기하적으로 불가능하다. 생성물은 2,2,3,4-tetramethylcyclobutanone으로, 3,4-dimethyl이 cis(alkene 기하 보존).
   (출처: L15 p.6–7, p.32)

4. 정답: (a) dichloroketene Cl2C=C=O. Et3N이 α-H를 떼어 enolate를 만들고, enolate가 acyl Cl⁻을 내보내 ketene 생성. (b) 7,7-dichlorobicyclo로[3.2.0]hept-2-en-6-one(cis 융합). 친전자성인 ketene carbonyl 탄소에 cyclopentadiene의 말단 탄소가 결합하고, CCl2 탄소가 그 이웃(남은 C=C에 allyl) 탄소와 결합한다. 이 계에서는 [2+2]가 [4+2]보다 빠르다.
   (출처: L15 p.8)

5. 정답: 1단계: 1-(chlorosulfonyl)-4-(chloromethyl)-4-methyl아제티딘-2-one. 2단계: 4-(chloromethyl)-4-methyl아제티딘-2-온(N-H β-락탐).
   해설: alkene의 말단 CH2(친핵성)가 CSI carbonyl 탄소(친전자성)와 결합하고, 더 치환된 탄소(양전하를 더 잘 안정화)가 N과 결합 → N 옆 4차 탄소. NaHCO3/H2O로 S–Cl 가수분해 → N-SO3H → SO3 이탈 → N-H. (출처: L15 p.12)

6. 정답: (a) 5-부틸-2-methylisoxazolidine (부틸이 O 옆 C5). alkene(HOMO)이 니트론(LUMO)과 상호작용; alkene 말단 CH2가 친전자성 니트론 탄소와 결합. (b) 4-acetyl-2-methylisoxazolidine (acetyl이 C4). 니트론(HOMO)의 O⁻가 친전자성 β-탄소(CH2)와 결합; alkene은 LUMO 사용.
   해설: 니트론은 친핵성·친전자성을 겸하므로 상대에 따라 역할이 바뀐다(슬라이드 규칙). (출처: L15 p.15)

7. 정답: (a) 3-R'-4,5-cis-다이R-isoxazoline. (b) 3-R'-4,5-trans-다이R-isoxazoline. (c) 3-R'-5-R isoxazole(방향족, R이 O 옆 C5). (a)를 H2/Ni, H2O로 처리하면 N–O 수소화 분해 → β-hydroxy imine → 가수분해 → R'-CO-CH(R)-CH(OH)-R, syn-aldol 생성물.
   해설: 협동적 supra-supra [3+2]이므로 alkene 기하가 stereospecificity, cis 고리 관계가 syn aldol로 전달된다. trans였다면 anti aldol. (출처: L15 p.18–20)

8. 정답: cis-cyclopentane-1,3-dicarbaldehyde(두 CHO가 같은 면). intermediate: O3 + alkene 1,3-쌍극 cycloaddition → 1차 ozonide(1,2,3-trioxolane) → 역 1,3-쌍극 cycloaddition으로 carbonyl + carbonyl oxide(1,3-쌍극자) → 재배향 후 1,3-쌍극 cycloaddition → 1,2,4-trioxolane(2차 ozonide) → Me2S reduction → dialdehyde + DMSO. H2O2 후처리 시 cis-cyclopentane-1,3-dicarboxylic acid.
   해설: 노보넨의 C=C가 끊어지며 두 탄소가 모두 CHO가 되고, 남은 고리 골격(다리 CH2 포함)이 5원 고리가 된다. 원래 C=C 탄소들이 exo/endo 같은 면 관계를 유지하므로 cis. 노보넨처럼 같은 분자 안에서 두 carbonyl이 생기면 trioxolane도 분자 내에서 형성되지만 최종 결과는 같다. (출처: L15 p.21, 23)

## 각주

[1] 보충: X형 치환기는 HOMO(및 LUMO)를 올려 친핵성을 키우고, Z형 치환기는 LUMO(및 HOMO)를 낮춰 친전자성을 키운다. 그래서 정상 전자요구 Diels–Alder는 "X/C-diene + Z-diene오필" 조합에서 빠르다. (보충 근거: Clayden p.886–887, 890)

[2] 보충: ketene의 중앙 탄소는 치환기가 없는 sp 탄소라 입체 장애가 작아서, alkene이 이렇게 직교 방향으로 접근할 수 있다.

[3] 슬라이드 p.9: Alexander Fleming은 Penicillium 곰팡이 군체 주변에서 포도상구균 군체가 녹아 없어지는 것을 관찰했고(British Journal of Experimental Pathology에 실린 배양 접시 사진), 1945년 노벨 생리의학상을 받았다.

[4] 보충: ketene–imine [2+2] (Staudinger reaction)는 슬라이드에서 협동적 화살표로 그려져 있지만, 실제로는 zwitterion intermediate를 거치는 단계적 경로로 알려져 있다. 슬라이드의 trans 표기는 그림 그대로 옮긴 것이며, 이 조건의 일반적인 cis/trans 경향은 시험 범위 밖으로 보고 따로 단정하지 않는다. 보충: Clayden은 같은 페녹시케텐 + imine 예(92%)를 싣고, 두 성분에 치환기가 하나씩 있으면 서로 피하려고 4원 고리에서 trans로 놓인다고 설명한다. 슬라이드의 trans 그림과 일치한다. (보충 근거: Clayden p.900)

[5] 보충: azide나 니트릴 oxide 같은 삼중결합형 쌍극자는 이와 직교하는 π 결합을 하나 더 가지지만, cycloaddition에 참여하는 π계는 4전자다. (보충 근거: Clayden p.901–902)

[6] 보충: isoxazolidine의 번호는 O1, N2, C3, C4, C5다. 실제 계에서는 치환기에 따라 regioselectivity이 섞여 나오기도 하지만, 시험에서는 슬라이드 규칙(EDG → 5-치환, EWG → 4-치환)을 따르면 된다.

[7] 보충: 니트릴 oxide는 불안정해서 쉽게 이량체화하므로, 보통 반응계 내(in situ)에서 생성하여 곧바로 쌍극친화체와 반응시킨다.

[8] 보충: H2O2 산화 후처리에서 carboxylic acid이 되는 것은 H를 가진(aldehyde가 될) 탄소이며, 이치환 탄소는 ketone으로 남는다. (보충 근거: Clayden p.907)

[9] 슬라이드 p.24: 2017년 University of Bristol의 한 학생이 의도치 않게 약 40 g의 TATP를 만들어 건물 대피와 폭발물 처리반의 통제 폭파가 있었던 사건, 그리고 2021년 싱가포르에서 TATP 폭탄 제조를 탐색한 테러 계획 보도가 소개되어 있다.

[10] 슬라이드 p.24: 아르테미시닌의 발견은 2015년 노벨 생리의학상으로 이어졌다.

[11] 보충: Z-치환 diene오필의 경우 Z는 OMe 달린 탄소의 이웃 탄소에 놓이며(OMe에 대해 ortho, OSiR3에 대해 para), 산 처리 후 4-치환 cyclohex-2-enone이 된다. 또한 Rawal diene은 아미노기가 알콕시기보다 강한 주개라 Danishefsky diene보다 반응성이 높다.

[12] 슬라이드 p.30의 노벨상 메달 아이콘. 보충: 2022년 노벨 화학상은 클릭 화학과 bioorthogonal 화학의 Bertozzi, Meldal, Sharpless에 수여되었다.
