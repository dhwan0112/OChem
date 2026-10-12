# L13. 고리화 첨가 반응 1부: Diels–Alder 반응 (Cycloadditions, Part 1)

<!-- wiki-links:start -->

> **관련 위키 문서** ([[위키 대문]])
> - 반응: [[1,3-쌍극자 고리화 첨가]], [[딜스-알더 반응]], [[로빈슨 고리 형성]], [[마이클 반응]], [[역 딜스-알더 반응]]
> - 개념: [[endo 규칙]], [[s-cis 형태]], [[딜스-알더 위치선택성]], [[속도론적 지배와 열역학적 지배]], [[우드워드-호프만 규칙]], [[입체특이성과 입체선택성]], [[초면과 대면]], [[친전자체와 친핵체]], [[페리고리 반응]], [[프런티어 분자 오비탈]]

<!-- wiki-links:end -->

CM3121 Advanced Organic Chemistry, Dr. Zhu Ye

## 개요

지금까지 다룬 반응은 대부분 친핵체가 친전자체를 공격하는 극성 반응이었다. 엔올레이트가 붙고, 이탈기가 떨어지고, 이온성 중간체가 생겼다가 사라지는 식이다(→ 앞선 엔올레이트·Michael 첨가 강의 참고). 이 강의에서는 전혀 다른 방식으로 결합이 생기는 반응군인 고리형 전자 이동 반응(pericyclic reaction)을 처음 다룬다. 그 대표가 Diels–Alder(DA) 반응이다. 다이엔과 알켄을 한 단계로 이어 붙여 6원자 고리를 만들고, 두 탄소–탄소 결합과 최대 네 개의 입체중심을 한 번에 정해 준다. 그래서 합성에서 가장 강력한 고리 형성 반응 가운데 하나로 꼽힌다. 강의는 "무엇이 반응하나 → 어떻게 반응하나 → 무엇이 빠르게 하나 → 입체화학은 어떻게 정해지나 → 왜 그런가(FMO, Woodward–Hoffmann)" 순서로 진행된다.

## 1. 반응은 어떻게 분류되나: 극성, 라디칼, 그리고 pericyclic

결합이 끊어지고 생기는 방식은 몇 가지나 될까? 슬라이드는 세 가지로 나눈다.

첫째는 극성 메커니즘(polar mechanism)이다. 결합이 비대칭으로 끊어지거나(이종 분해 heterolysis) 비대칭으로 생긴다. 한 분자의 전자 풍부 자리(친핵체)가 다른 분자의 전자 부족 자리(친전자체)에 전자쌍을 주고, 그 과정에서 이온성 중간체가 생긴다. 둘째는 라디칼 메커니즘(radical mechanism)이다. 결합이 대칭으로 끊어지거나(동종 분해 homolysis) 생기며, 홀전자를 가진 라디칼 중간체가 반응을 이끈다. 셋째가 이번 강의의 주인공인 pericyclic 메커니즘이다. 전자가 닫힌 고리를 따라 한 바퀴 돌면서 움직이고, 중간체가 전혀 없다. (출처: L13 p.3)

그렇다면 pericyclic 반응은 구체적으로 어떤 모습일까? 네 가지 특징이 있다. TS가 고리 모양이고, 그 고리 안에 라디칼이나 이온 중간체가 없으며, 결합 형성과 절단이 한꺼번에(협동적, concerted) 일어난다. 그 결과 반응이 입체특이적(stereospecific)이거나 입체선택적(stereoselective)이다(또는 둘 다). 자연계에도 이런 반응이 있다. chorismate mutase라는 효소는 chorismate의 Claisen 자리옮김(Claisen rearrangement)을 촉매해 prephenate를 만든다. 효소 활성 자리의 Arg, Glu 같은 잔기가 수소 결합으로 고리형 TS를 붙잡아 안정화한다.[1] (출처: L13 p.4)

Pericyclic 반응은 다시 세 갈래로 나뉜다. 두 조각이 양 끝에서 동시에 이어져 고리가 되는 고리화 첨가(cycloaddition), 한 사슬의 양 끝이 이어지는 전자고리화 반응(electrocyclic reaction), σ 결합 하나가 자리를 옮기는 시그마트로픽 자리옮김(sigmatropic rearrangement)이다. 고리화 첨가에는 다시 Diels–Alder 반응, 1,3-쌍극자 고리화 첨가(1,3-dipolar cycloaddition), 그 밖의 고리화 첨가가 속한다. 이번 강의는 이 가운데 Diels–Alder만 다룬다. (출처: L13 p.5)

## 2. 극성 반응으로도 6원자 고리는 만들 수 있지 않나?

물론 만들 수 있다. 다만 여러 단계를 거쳐야 한다. 슬라이드는 두 가지 예를 보여 준다.

첫 번째 예에서는 2-methylcyclohexane-1,3-dione과 methyl vinyl ketone이 10% NaOH 조건에서 Michael 첨가를 해 1,5-diketone이 된다. 이것을 piperidine 촉매와 함께 가열하면 물이 빠지면서 이중 고리 enone이 닫힌다. EtONa로 가열하면 같은 일을 한 반응기(one-pot)에서 끝낼 수도 있다.[2]

두 번째 예는 I-(CH2)4-CH=CH-CO2Me와 CH3NO2를 Cs2CO3/DMF, 20 °C에서 반응시키는 것이다. 메커니즘을 따라가 보면 다음과 같다.
1. Cs2CO3가 CH3NO2의 α-H를 떼어 nitronate 음이온(친핵체)을 만든다.
2. nitronate가 α,β-불포화 에스터의 β-탄소(친전자체)에 Michael 첨가해 I-(CH2)4-CH(CH2NO2)-CH2CO2Me가 된다.
3. CH2NO2의 α-H가 다시 탈양성자화된다. 이 탄소 음이온이 같은 분자의 C–I 탄소를 SN2로 공격해 고리를 닫는다.

결과물은 2-(2-nitrocyclohexyl)acetic acid methyl ester다(65%).

즉 극성 방식으로 고리를 만들려면 탈양성자화, 첨가, 고리 닫기를 차례로 거쳐야 하고 그때마다 이온성 중간체가 생긴다. 반면 DA 반응은 이 모든 일을 한 단계로 끝낸다. 이 대비가 이 슬라이드의 핵심이다. (출처: L13 p.6)

## 3. Diels–Alder 반응이란 무엇인가

정의 자체는 간단하다. 짝지어진 다이엔(conjugated diene)과 알켄이 반응해 cyclohexene을 만드는 반응이다. 가장 단순한 예는 1,3-butadiene + ethylene → cyclohexene이다. 그런데 조건을 보면 165 °C, 17 h, 900 atm이 필요하다(수율 78%). "가장 단순한 DA"가 결코 "가장 쉬운 DA"는 아니라는 뜻이다. 왜 이렇게 어려운지는 뒤의 속도 부분에서 다룬다.[3] (출처: L13 p.7)

반응을 그릴 때는 번호를 붙이면 편하다. 다이엔 탄소를 C1–C4, 알켄 탄소를 C5–C6으로 두면 굽은 화살표 세 개가 고리를 따라 돈다. 화살표 방향은 시계 방향이든 반시계 방향이든 상관없다. 결과는 같아서, 새 σ 결합 C1–C6과 C4–C5가 생기고 다이엔 가운데에 새 π 결합 C2=C3가 남는다. (출처: L13 p.7)

![butadiene과 ethylene의 Diels–Alder 반응: 굽은 화살표 세 개가 고리를 따라 같은 방향으로 돌며 cyclohexene을 만든다](../figures/L13/da_basic.svg)

*그림: 파란색은 다이엔(s-cis)의 두 π 결합, 빨간색은 dienophile(ethylene)의 π 결합, 주황색 굽은 화살표는 전자쌍의 이동, 초록색은 새로 생긴 σ 결합 C1–C6과 C4–C5다. 화살표 셋은 모두 시계 방향으로 돈다. (1) C1=C2 π 전자가 C1–C6 결합이 되고, (2) C5=C6 π 전자가 C4–C5 결합이 되며, (3) C3=C4 π 전자가 C2–C3로 옮겨가 새 π 결합(파란 C2=C3)이 된다. 세 화살표는 한 단계에서 동시에 일어난다.*

용어도 정리해 두자. 다이엔은 C=C 두 개가 단일 결합 하나로 이어진 짝지어진 다이엔이어야 한다. 다이엔과 반응하는 알켄(때로는 알카인)은 다이엔친화체(dienophile)라고 부르고, 생성물은 cyclohexene이다. 예를 들어 2,3-dimethyl-1,3-butadiene과 acrolein(CH2=CH-CHO)은 3,4-dimethylcyclohex-3-ene-1-carbaldehyde를 준다. 다이엔이 고리형이면 어떻게 될까? cyclopentadiene + nitroethylene(CH2=CH-NO2)처럼 다리 걸친 이중 고리(bridged bicyclic)인 5-nitrobicyclo[2.2.1]hept-2-ene(5-nitronorbornene)이 생긴다. (출처: L13 p.8)

이 반응은 실험실만의 것이 아니다. 자연계에는 DA 반응을 촉매하는 효소(Diels–Alderase)도 있다. 슬라이드의 예에서는 긴 사슬 끝의 다이엔과 tetronate 고리의 exo-methylene dienophile이 효소 주머니 안에서 분자 내 [4+2] 고리화 첨가를 해 spiro 구조의 cyclohexene을 만든다(J. Am. Chem. Soc. 2016, 138, 6095). (출처: L13 p.9)

## 4. 어떻게 반응하나: 메커니즘과 전이 상태

DA 반응에는 정말 중간체가 없을까? 그렇다. DA는 pericyclic 반응의 전형으로, 단일 기본 단계(single elementary step)로 끝난다. 전자는 고리를 따라 돌고, 전하가 쌓이지 않으며, 모든 결합 형성과 절단이 동시에 일어난다. butadiene + ethylene을 단계로 풀어 쓰면 다음과 같다. 다만 실제로는 이 네 가지가 따로 일어나지 않고 한순간에 함께 일어난다.
1. 다이엔의 C1=C2 π 전자가 C1–C6 결합을 만든다.
2. 알켄의 C5=C6 π 전자가 C4–C5 결합을 만든다.
3. 다이엔의 C3=C4 π 전자가 C2–C3로 옮겨가 새 π 결합이 된다.
4. 이 모든 변화가 하나의 고리형 TS에서 동시에 일어나 cyclohexene이 된다.

그렇다면 이 반응은 왜 일어날까? 열역학과 속도론 두 측면에서 답할 수 있다. 열역학적으로는 π 결합 두 개를 잃는 대신 더 강한 C–C σ 결합 두 개(C1–C6, C4–C5)를 얻으므로 이득이다.[4] 속도론적으로는 TS에 6개의 π 전자가 고리 모양으로 비편재화되어 있어, 벤젠처럼 방향족성(4n+2)을 띠고 안정화된다. 이른바 "방향족성 전이 상태"다. (출처: L13 p.10)

이 TS가 실제로 어떻게 생겼는지는 계산 연구로 볼 수 있다. butadiene + ethylene의 TS에서 새로 생기는 C···C 거리는 약 2.2 Å(2.217–2.273 Å)으로, 결합이 반쯤 생긴 상태다. 고리 안의 다른 C–C 거리는 약 1.38–1.43 Å로 단일 결합과 이중 결합의 중간이다. 즉 TS에서는 전자가 고르게 퍼져 있어, 말 그대로 "반쯤 벤젠 같은" 고리 상태다. (출처: L13 p.11)

dienophile을 maleic anhydride로 바꾸어도 그림은 같다. butadiene + maleic anhydride는 6π 비편재화 TS를 거쳐 cis-1,2,3,6-tetrahydrophthalic anhydride를 준다. 두 고리 접합 H가 cis다. 오비탈로 보면 두 반응물이 평행한 평면으로 포개지고, 각 성분이 양 끝에서 같은 면을 써서 결합을 만든다. 이것을 초면-초면(suprafacial–suprafacial) 접근이라고 한다. 이 "같은 면" 성질이 뒤에 나올 입체특이성의 뿌리다. (출처: L13 p.12)

이 반응을 Woodward–Hoffmann 언어로 미리 표현하면 이렇다. 다이엔은 4전자 π 성분(π4), dienophile은 2전자 π 성분(π2)이고, 둘 다 초면으로 반응하므로 [π4s + π2s]다. 여기서 성분(component)이란 반응에 한 단위로 참여하는 결합이나 오비탈을 말한다. 다이엔과 dienophile은 각각 하나의 성분이다. 규칙 자체는 6절에서 다룬다(ChemTube3D 애니메이션 참고). (출처: L13 p.13)

## 5. 무엇이 반응을 빠르게 하나

### 5-1. Dienophile: 전자가 부족할수록 좋다

앞에서 butadiene + ethylene이 900 atm까지 필요했던 이유는 무엇일까? 답은 dienophile의 전자적 성질에 있다. 실제로 쓰이는 dienophile에는 대개 전자 끄는 기(EWG)가 붙어 있다. 슬라이드에 나온 예는 NO2, CN, SO2R, COOR, COR, Cl, Ph이고,[5] 대체로 dienophile의 전자가 부족할수록 반응이 빠르다. 숫자로 비교하면 차이가 확연하다.

- butadiene + ethylene --[165 °C, 17 h, 900 atm]--> cyclohexene (78%)
- butadiene + acrolein --[150 °C, 0.5 h]--> cyclohex-3-ene-1-carbaldehyde
- butadiene + CH2=C(COOMe)2 --[25 °C, 24 h]--> dimethyl cyclohex-3-ene-1,1-dicarboxylate (80%)

EWG 하나로 압력 조건이 사라지고, 두 개면 상온에서도 반응한다. 슬라이드 상자에는 이 밖에 1-chlorovinyl acetate(CH2=C(Cl)OAc), crotononitrile(CH3CH=CH-CN), 고리형 불포화 sulfone(2-sulfolene), 1,2-dihydronaphthalene 같은 dienophile도 나온다. (출처: L13 p.14)

### 5-2. 다이엔: 전자가 풍부하고, s-cis여야 한다

다이엔 쪽은 반대다. 전자 주는 기(EDG)가 붙은 전자 풍부 다이엔이 중성이거나 전자가 부족한 다이엔보다 빠르다. 그래서 가장 이상적인 짝은 "EDG-다이엔 + EWG-dienophile"이다. 왜 그런지는 7절의 FMO에서 설명한다.

그런데 다이엔에는 전자 말고도 중요한 조건이 하나 더 있다. 바로 모양이다. butadiene의 C2–C3 단일 결합은 회전할 수 있어서 두 가지 형태를 오간다. 두 C=C가 반대쪽을 향한 s-trans 형태는 더 안정하지만, C1과 C4가 멀리 떨어져 있어 dienophile의 양 끝에 동시에 닿을 수 없다. 두 C=C가 같은 쪽을 향한 s-cis 형태에서만 C1과 C4가 가까워져 반응할 수 있다. 비유하자면 dienophile을 양손으로 잡으려면 두 팔을 같은 방향으로 뻗어야 하는 셈이다. 두 형태는 빠르게 서로 바뀌므로 s-cis 분자가 반응해 없어지면 평형이 다시 채워 준다. 하지만 butadiene은 상온에서 겨우 1%만 s-cis 형태로 존재한다(슬라이드 수치). 예를 들어 butadiene(s-cis) + methyl acrylate는 methyl cyclohex-3-ene-1-carboxylate를 준다. (출처: L13 p.15)

![butadiene의 s-trans와 s-cis 형태: s-cis만 methyl acrylate와 DA 반응을 할 수 있다](../figures/L13/s_cis_s_trans.svg)

*그림: 초록색은 회전하는 C2–C3 단일 결합, 파란색은 다이엔의 π 결합, 빨간색은 dienophile(methyl acrylate)의 π 결합이다. 왼쪽 s-trans는 더 안정하지만 C1과 C4가 멀어 dienophile의 양 끝에 동시에 닿지 못한다. C2–C3 결합이 빠르게 회전해 s-cis가 되면 C1과 C4가 가까워지고, 주황색 굽은 화살표 셋이 그림 1과 같은 방향으로 돌며 고리가 닫힌다.*

### 5-3. 고리형 다이엔: 처음부터 s-cis로 고정된 다이엔

그렇다면 처음부터 s-cis로 묶여 있는 다이엔은 어떨까? 예상대로 반응성이 매우 크다. cyclopentadiene, furan, cyclohexa-1,3-diene, 1,2-dimethylenecyclohexane("exo-methylene" 다이엔)은 고리 때문에 s-cis로 고정되어 있어서 사슬형 다이엔보다 훨씬 반응성이 크다. 예를 들어 cyclopentadiene + acrolein은 20 °C에서 68 h 만에 5-norbornene-2-carbaldehyde를 92%로 준다. 슬라이드에서는 CHO가 CH2 다리의 반대쪽(endo)으로 그려져 있다. 반대로 3-methylenecyclohexene이나, 두 C=C가 서로 다른 고리에 걸쳐 transoid로 고정된 이중 고리 다이엔처럼 s-trans로 묶여 있는 다이엔은 아무리 가열해도 DA 반응을 할 수 없다. s-cis 형태를 취할 수 없는 다이엔은 DA 반응에 참여하지 못한다. (출처: L13 p.16)

p.17의 연습 문제(생성물에서 다이엔과 dienophile 찾기)는 아래 연습 문제 1, 2로 옮겼다. (출처: L13 p.17)

### 5-4. Cyclopentadiene 이야기: DA 반응은 되돌아갈 수도 있다

cyclopentadiene은 반응성이 너무 커서 생기는 문제가 있다. 바로 자기 자신과 반응한다는 것이다. 한 분자는 다이엔, 다른 분자는 dienophile로 DA 반응을 해서, 상온에서는 이량체(dicyclopentadiene)로 존재한다. 그럼 단량체는 어떻게 얻을까? 이량체를 가열해 "분해(crack)"하면 된다. DA 반응은 가역적일 수 있으므로, 가열하면 역 DA(retro-Diels–Alder) 반응이 일어난다. 이때 끓는점이 낮은 단량체(b.p. 42 °C)를 증류로 빼내면 평형이 계속 단량체 쪽으로 밀린다. 이렇게 얻은 단량체는 −20 °C에서 며칠 보관할 수 있지만, 상온에서는 몇 시간 안에 다시 이량화한다.

![dicyclopentadiene의 역 Diels–Alder 반응: 가열하면 cyclopentadiene 두 분자로 갈라진다](../figures/L13/retro_da_dcpd.svg)

*그림: 보충: 슬라이드에는 평형 화살표만 있고 굽은 화살표는 없다. 역 DA는 정방향 DA의 화살표를 거꾸로 돌린 것이므로 여기서 그려 넣었다. 빨간색은 끊어지는 σ 결합(이량화 때 생겼던 C1–C6, C4–C5), 파란색은 다이엔 쪽에 남아 있던 π 결합이다. 주황색 화살표 셋은 (1) C4–C5 σ 전자가 C3=C4 π 결합으로, (2) C2=C3 π 전자가 C1=C2 π 결합으로, (3) C1–C6 σ 전자가 C5=C6 π 결합으로 옮겨가는 과정이다. 초록색은 새로 생긴 π 결합이다. 가운데 꺾인 선은 CH2 다리(C7)다.*

응용 예도 있다. cyclopentadiene을 Cl2로 처리하면 hexachlorocyclopentadiene이 되고, 이것을 maleic anhydride와 DA 반응시키면 염소가 여섯 개 붙은 norbornene 무수물 부가물이 생긴다. 이 화합물은 난연제(flame retardant)로 쓰인다.[6] (출처: L13 p.18)

## 6. 입체화학: 반응물의 모양이 생성물에 어떻게 새겨지나

### 6-1. 이치환 dienophile: cis는 cis로, trans는 trans로

butadiene에 dimethyl maleate(cis)와 dimethyl fumarate(trans)를 각각 반응시키면 결과가 어떻게 다를까? 답은 "원래 배열 그대로"다. cis-dienophile은 cis 생성물을, trans-dienophile은 trans 생성물을 준다.

- butadiene + dimethyl maleate(Z) → cis-dimethyl cyclohex-4-ene-1,2-dicarboxylate(두 CO2Me가 같은 쪽, syn)
- butadiene + dimethyl fumarate(E) → trans-diester(두 CO2Me가 반대쪽, anti, 라셈체)

왜 그럴까? 반응이 협동적이고 초면으로 일어나기 때문이다. dienophile의 두 탄소는 같은 면에서 동시에 결합을 만들고, 그 사이에 C5–C6 결합이 회전할 수 있는 중간체가 없다. 그래서 알켄의 cis/trans 정보가 고리에 그대로 찍힌다. 반응물의 입체화학이 생성물의 입체화학을 결정하므로 이것을 입체특이성(stereospecificity)이라고 한다. (출처: L13 p.19)

![butadiene + dimethyl maleate(cis): 두 CO2Me가 cis인 생성물](../figures/L13/maleate_cis.svg)

![butadiene + dimethyl fumarate(trans): 두 CO2Me가 trans인 생성물](../figures/L13/fumarate_trans.svg)

*그림: 위는 cis-dienophile(dimethyl maleate), 아래는 trans-dienophile(dimethyl fumarate)이다. 파란색은 다이엔의 π 결합, 빨간색은 dienophile의 π 결합, 주황색 굽은 화살표는 전자쌍의 이동(세 화살표가 같은 방향으로 돈다), 초록색은 새 σ 결합이다. 생성물에서 쐐기(wedge)는 지면 앞, 점선 쐐기(hash)는 지면 뒤를 뜻한다. 같은 쪽에 있던 두 CO2Me는 둘 다 쐐기(cis)가 되고, 반대쪽에 있던 두 CO2Me는 쐐기 하나와 점선 하나(trans, 라셈체)가 된다.*

### 6-2. 이치환 다이엔: "in"과 "out"

다이엔 쪽 치환기는 어떻게 될까? s-cis 형태의 다이엔을 그려 보면, 말단 탄소(C1, C4)의 치환기는 고리 안쪽을 향해 서로 마주 보는 "in" 자리와 바깥쪽을 향하는 "out" 자리 가운데 하나에 놓인다. 규칙은 단순하다. "in" 두 개는 생성물에서 1,4-cis가 되고, "out" 두 개도 서로 1,4-cis가 된다. 그러니 "in" 하나와 "out" 하나는 trans가 된다.

예를 들어 (E,E)-1,4-diphenyl-1,3-butadiene은 두 Ph가 모두 "out"이다. 그래서 dimethyl acetylenedicarboxylate(DMAD, MeO2C-C≡C-CO2Me)와 반응하면 두 Ph가 cis인 3,6-diphenylcyclohexa-1,4-diene-1,2-diester가 생긴다. 반면 (E,Z) 다이엔(R 하나는 "in", 하나는 "out")은 두 R이 trans인 생성물을 준다. dienophile이 알카인이면 원래 삼중 결합 자리에 C=C가 하나 남으므로, 생성물은 cyclohexene이 아니라 cyclohexa-1,4-diene이다. (출처: L13 p.20)

### 6-3. Endo 규칙: 두 반응물 사이의 입체선택성

지금까지는 한 반응물 안의 치환기끼리의 관계를 보았다. 그런데 dienophile의 치환기와 다이엔 사이의 관계는 무엇이 정할까? 예를 들어 cyclopentadiene + maleic anhydride에서는 무수물 고리가 새 C=C 쪽을 향하는 endo 부가물과, CH2 다리 쪽을 향하는 exo 부가물이 둘 다 이론적으로 가능하다. 실제로는 endo 부가물만 생긴다. DA 반응은 보통 endo TS를 거치는 쪽이 우세하며, 이를 endo 규칙(endo rule)이라고 한다.

그 이유는 2차 오비탈 겹침(secondary orbital overlap)이다. endo TS에서는 dienophile의 C=O 기가 다이엔 바로 아래에 놓여, 결합을 만들지 않는 다이엔의 "뒤쪽"(C2, C3)과 결합성으로 상호작용한다. 이 추가 안정화 덕분에 endo TS의 에너지가 낮아진다. 결과적으로 생성물에서는 새 이중 결합과 C=O 기가 분자의 같은 쪽에 놓인다. (출처: L13 p.21)

![cyclopentadiene + maleic anhydride의 endo 부가물(생성)과 exo 부가물(생성 안 됨)](../figures/L13/endo_exo.svg)

*그림: 초록색은 DA 반응으로 새로 생긴 σ 결합 두 개, 파란색은 다리 걸친 고리에 남은 C=C, 빨간색은 무수물의 C=O다. 왼쪽 endo 부가물에서는 무수물 고리가 C=C 쪽(아래)으로 접혀 들어가 있어 C=C와 C=O가 분자의 같은 쪽에 놓이고, 고리 접합 H 두 개는 CH2 다리 쪽(위)을 향한다. 오른쪽 exo 부가물은 반대로 무수물이 CH2 다리 쪽을 향하고 H가 아래를 향한다. 실제로는 endo 부가물만 생긴다.*

좀 더 기하학적으로 보면, TS에서 평면인 다이엔과 평면인 dienophile이 평행하게 포개진다. 이때 EWG(예: CHO)가 다이엔 아래로 들어가면 endo TS, 바깥으로 비켜나 있으면 exo TS다. dienophile에 카보닐 같은 전자 끄는 π 치환기가 있으면 보통 endo 첨가가 우세하다. 다만 이것은 "선호"이지 "법칙"이 아니어서 두 입체이성질체가 섞여 나오는 경우도 많다.[7] (출처: L13 p.22)

p.23–24의 연습 문제((E,E)-hexa-2,4-diene + acrolein의 endo 생성물 고르기)는 연습 문제 3으로 옮겼다. 슬라이드 p.24에 풀이가 있다. 카보닐이 다이엔 아래로 들어간(tucked under) endo TS를 거치면 세 H가 한 면에 모이므로, CHO와 두 Me가 모두 cis인 all-cis 생성물이 생긴다. (출처: L13 p.23–24)

## 7. 왜 그런가: 분자 오비탈로 다시 보기

### 7-1. 재료 준비: 알켄과 다이엔의 π 오비탈

앞에서 나온 "왜?"들에 답하려면 오비탈 그림이 필요하다. 먼저 ethylene을 보자. H–C–H 각은 117.8°, C–H는 108 pm, C=C는 133 pm이다. C–C σ 결합은 sp2 오비탈끼리, π 결합은 p 오비탈끼리 겹쳐 생긴다. 두 p 오비탈이 같은 위상으로 합쳐지면 결합성 π 오비탈(전자 2개, HOMO)이 되고, 반대 위상으로 합쳐지면 마디 평면이 하나 있는 반결합성 π* 오비탈(LUMO)이 된다. (출처: L13 p.25)

butadiene은 이 알켄 두 개의 π와 π*를 섞어 만든다고 생각하면 된다. 그러면 에너지 순서대로 ψ1(마디 0개), ψ2(마디 1개), ψ3(마디 2개), ψ4(마디 3개)의 네 MO가 생긴다. 전자 4개는 ψ1과 ψ2에 들어가므로 HOMO는 ψ2, LUMO는 ψ3다. ψ2의 양 끝 로브는 위상이 반대이고, ψ3의 양 끝 로브는 위상이 같다는 점을 기억해 두면 이후 설명이 쉬워진다. (출처: L13 p.26)

### 7-2. 왜 전자 풍부 다이엔 + 전자 부족 dienophile이 빠른가?

FMO 이론에 따르면 반응은 한쪽의 HOMO에서 다른 쪽의 LUMO로 전자가 흘러가는 상호작용으로 시작되고, 두 오비탈의 에너지가 가까울수록 상호작용이 강하다. DA에서 가능한 짝은 두 가지다. 다이엔 HOMO(ψ2)와 dienophile LUMO(π*)의 짝은 에너지 차이가 작아 겹침이 좋다. 반대로 다이엔 LUMO(ψ3)와 dienophile HOMO(π)의 짝은 에너지 차이가 커서 겹침이 나쁘다. 그래서 주된 상호작용은 앞의 짝이다.

이제 답이 나온다. 다이엔에 EDG를 붙이면 HOMO가 올라가고, dienophile에 EWG를 붙이면 LUMO가 내려간다. 둘 다 HOMO(다이엔)–LUMO(dienophile) 사이 간격을 좁혀 TS를 안정화하므로 반응이 빨라진다. ethylene이 900 atm을 요구했던 것도, acrolein이나 maleic anhydride가 쉽게 반응하는 것도 같은 이유다.[8] (출처: L13 p.27)

### 7-3. 오비탈로 본 입체특이성

입체특이성도 오비탈 그림으로 바로 이해된다. 다이엔 HOMO의 양 끝 로브와 dienophile LUMO의 양 끝 로브는 각각 같은 면에서 만나야 위상이 맞는다. 그래서 두 σ 결합이 한 면에서 동시에 생기고(초면-초면), 치환기의 상대 배열이 보존된다. 슬라이드는 네 가지 경우를 짝지어 보여 준다. (Z)-maleate는 syn, (E)-fumarate는 anti 생성물을 준다. DMAD와 반응할 때 (E,E)-hexa-2,4-diene은 syn(cis-3,6-dimethyl), (E,Z)-hexa-2,4-diene은 anti(trans-3,6-dimethyl) 생성물을 준다. (출처: L13 p.28)

### 7-4. 오비탈로 본 endo 선호

endo 선호는 cyclopentadiene 이량화를 예로 설명한다. 두 cyclopentadiene이 만나면 endo-dicyclopentadiene이 생기고, 두 알켄이 서로 endo 관계에 놓인다. 다이엔 HOMO의 말단(C1, C4)과 dienophile LUMO의 결합성 겹침이 새 σ 결합을 만드는 1차 상호작용이다. 그런데 endo TS에서는 그것만이 아니다. dienophile 분자에 남은 π 오비탈이 다이엔의 C2, C3 로브 바로 아래에 놓여 추가로 결합성 겹침을 한다. 이것이 2차 오비탈 겹침이다. 이 겹침은 결합으로 이어지지 않고 TS만 안정화하는 "보너스"이므로, 남은 π계를 다이엔 아래에 둘 수 있는 endo 경로가 선호된다.[9] (출처: L13 p.29)

### 7-5. 그럼 다이엔 두 개는 왜 [4+4]를 하지 않을까?

butadiene 두 분자를 가열하면 [4+2] 생성물인 4-vinylcyclohexene은 생기지만, [4+4] 생성물인 cycloocta-1,5-diene은 생기지 않는다. 같은 다이엔 두 개인데 왜 한쪽만 될까? 오비탈을 겹쳐 보면 답이 보인다. [4+2]에서는 한 분자의 HOMO(ψ2)와 다른 분자의 LUMO(dienophile 역할을 하는 C=C 부분)의 양 끝이 모두 위상이 맞아 결합성이다. 그런데 [4+4]에서는 HOMO(ψ2)와 다른 분자의 LUMO(ψ3)를 겹치면, 한쪽 끝은 결합성이지만 다른 끝은 위상이 어긋나 반결합성이다. 두 결합을 동시에 만들 수 없으므로 열적으로는 진행되지 않는다. (출처: L13 p.30)

정리 슬라이드는 지금까지의 흐름을 다섯 줄로 요약한다. DA는 다이엔과 알켄이 cyclohexene을 만드는 반응이고, 메커니즘은 협동적이며 고리형 TS를 거친다. 속도는 전자 풍부 다이엔과 전자 부족 dienophile일수록 빠르다. 입체화학은 반응물 안에서는 입체특이성, 두 반응물 사이에서는 입체선택성(endo TS)으로 정해지고, 이는 FMO로 설명된다. Woodward–Hoffmann 규칙으로 반응성을 예측하는 부분은 회색으로 처리되어 있어 다음 강의로 넘어가는 것으로 보인다. (출처: L13 p.31)

## 8. Woodward–Hoffmann 규칙: 허용과 금지를 가르는 계산법

FMO 그림을 매번 그리지 않고도 반응이 허용되는지 판단할 방법은 없을까? 그 답이 Woodward–Hoffmann 규칙이다.[10] (출처: L13 p.32)

규칙은 한 문장이다. 열적(thermal) pericyclic 반응에서는 (4q+2)s 성분의 수와 (4r)a 성분의 수를 합한 값이 홀수여야 한다. 풀어 말하면, 전자 2, 6, 10개를 가진 초면 성분의 수에 전자 0, 4, 8개를 가진 대면 성분의 수를 더해 홀수가 나오면 그 반응은 "허용"된다. 여기서 '허용(allowed)'은 반드시 일어난다는 뜻이 아니라 이론적으로 가능하다는 뜻일 뿐이다. (출처: L13 p.33)

용어도 정리해 두자. 초면(suprafacial) 성분은 양 끝에서 같은 면으로 새 결합을 만드는 성분이고, 대면(antarafacial) 성분은 양 끝에서 서로 반대 면으로 새 결합을 만드는 성분이다. (출처: L13 p.34)

이제 DA에 적용해 보자. DA는 [π4s + π2s]다. (4q+2)s에 해당하는 것은 알켄(π2s) 1개다. (4r)a에 해당하는 성분은 없다. 다이엔 π4는 초면이므로 (4r)s이고, 세는 대상이 아니다. 합이 1, 즉 홀수이므로 허용된 반응이다. 기하학적으로는 앞에서 본 초면-초면 접근 그대로다. (출처: L13 p.35)

p.36의 연습 문제(같은 규칙으로 [4+2]는 허용되고 [4+4]는 금지됨을 보이기)는 연습 문제 7로 옮겼다. (출처: L13 p.36)

## 9. 보충: 위치선택성("ortho/para" 규칙)

이 강의 슬라이드에는 위치선택성(regioselectivity)이 나오지 않는다(아마 2부에서 다룰 것이다, → 고리화 첨가 2부 문서 참고). 여기서는 표준 교재의 결론만 짧게 적어 둔다. 비대칭 다이엔과 비대칭 dienophile이 반응할 때, 1-치환 다이엔(예: 1-methoxybutadiene)은 주로 "ortho"(1,2-이치환) 생성물을, 2-치환 다이엔(예: 2-methoxybutadiene)은 주로 "para"(1,4-이치환) 생성물을 준다. 다이엔 HOMO 계수가 가장 큰 말단 탄소가 dienophile LUMO 계수가 가장 큰 탄소(EWG의 β-탄소)와 결합하기 때문이다. (보충 근거: Clayden p.889–891)

## 흔한 오해

- **"butadiene은 그냥 다이엔이니 언제든 반응한다"고 생각하기 쉽지만 사실은** s-cis 형태일 때만 반응하고, 상온에서 s-cis인 분자는 약 1%뿐이다. s-trans로 고정된 다이엔(3-methylenecyclohexene 등)은 아예 반응하지 않고, s-cis로 고정된 cyclopentadiene은 상온에서도 잘 반응한다. (p.15–16)
- **"EWG는 HOMO를 낮추니 dienophile의 HOMO가 중요하다"고 생각하기 쉽지만 사실은** 정상 DA의 핵심 짝은 다이엔 HOMO(ψ2)와 dienophile LUMO(π*)다. EWG는 dienophile의 LUMO를 낮추고 EDG는 다이엔의 HOMO를 올려서 둘 사이 간격을 줄인다. (p.27)
- **"입체특이성과 입체선택성은 같은 말"이라고 생각하기 쉽지만 사실은** 한 반응물 안의 치환기 관계(cis/trans, in/out)는 입체특이적으로 100% 보존되고, 두 반응물 사이의 관계(endo/exo)는 입체선택적이라 혼합물이 생길 수 있다. (p.22, 31)
- **"(E,E)-다이엔의 두 치환기는 E니까 생성물에서 trans일 것"이라고 생각하기 쉽지만 사실은** 두 치환기가 모두 "out"이라서 생성물에서는 1,4-cis다. trans가 되는 것은 (E,Z)-다이엔(in + out)이다. (p.20, 28)
- **"endo는 치환기가 다리(CH2) 아래쪽, 안쪽에 있는 것"이라고 생각하기 쉽지만 사실은** endo는 dienophile의 π 치환기가 다이엔 π계 아래에 놓이는 배향이다. 그래서 norbornene 생성물에서는 치환기가 새 C=C 쪽, 즉 CH2 다리의 반대쪽에 있다. (p.21–22)
- **"2차 오비탈 겹침이 새 결합을 만든다"고 생각하기 쉽지만 사실은** 결합으로 이어지지 않고 endo TS만 안정화하는 속도론적 효과다. (p.21, 29)
- **"π4s도 Woodward–Hoffmann 계산에 넣는다"고 생각하기 쉽지만 사실은** (4q+2)s와 (4r)a만 센다. DA [π4s+π2s]의 합은 1(허용), [π4s+π4s]의 합은 0(금지)이다. 또 '허용'은 일어날 수 있다는 뜻이지 반드시 일어난다는 뜻이 아니다. (p.33–35)
- **"DA로 생긴 고리는 영원하다"고 생각하기 쉽지만 사실은** DA는 가역적일 수 있다. dicyclopentadiene을 가열·증류하면 역 DA로 단량체가 나온다. (p.18)
- **"DA 생성물은 언제나 cyclohexene"이라고 생각하기 쉽지만 사실은** 알카인 dienophile(DMAD 등)을 쓰면 cyclohexa-1,4-diene이 생긴다. (p.20)
- **역합성 요령:** 생성물 고리의 C=C를 C2=C3로 놓고, 그 양옆 탄소 C1, C4에서 다음 결합(C1–C6, C4–C5)을 끊으면 다이엔과 dienophile이 나온다. (p.17)

## 반응 정리표

| 반응 | 시약/조건 | 생성물 | 위치선택성 | 입체화학 | 비고 |
|---|---|---|---|---|---|
| butadiene + ethylene | 165 °C, 17 h, 900 atm | cyclohexene (78%) | 해당 없음 | 해당 없음 | 활성화되지 않은 dienophile이라 가혹한 조건 필요 (p.7, 14) |
| 2,3-dimethylbutadiene + acrolein | 열 | 3,4-dimethylcyclohex-3-ene-1-carbaldehyde | 대칭 다이엔이라 해당 없음 | 새 입체중심 1개(라셈) | (p.8) |
| cyclopentadiene + nitroethylene | 열 | 5-nitronorbornene | 해당 없음 | endo/exo 가능 | 다리 걸친 이중 고리 (p.8) |
| butadiene + acrolein | 150 °C, 0.5 h | cyclohex-3-ene-1-carbaldehyde | 해당 없음 | 라셈 | EWG 1개라 빠름 (p.14) |
| butadiene + CH2=C(CO2Me)2 | 25 °C, 24 h | dimethyl cyclohex-3-ene-1,1-dicarboxylate (80%) | 해당 없음 | 비카이랄 | EWG 2개라 상온에서 반응 (p.14) |
| butadiene + methyl acrylate | 열 | methyl cyclohex-3-ene-1-carboxylate | 해당 없음 | 라셈 | s-cis 형태에서만 반응 (p.15) |
| cyclopentadiene + acrolein | 20 °C, 68 h | 5-norbornene-2-carbaldehyde (92%) | 해당 없음 | endo로 그려짐 | s-cis 고정 다이엔이라 상온 반응 (p.16) |
| cyclopentadiene 2분자 (이량화) | 상온, 몇 시간 | endo-dicyclopentadiene | 해당 없음 | endo | 가열·증류하면 역 DA로 단량체(b.p. 42 °C) 회수 (p.18, 29) |
| hexachlorocyclopentadiene + maleic anhydride | 열 | 육염소 norbornene 무수물 | 해당 없음 | cis-무수물 | 난연제 (p.18) |
| butadiene + maleic anhydride | 열 | cis-1,2,3,6-tetrahydrophthalic anhydride | 해당 없음 | cis(입체특이적) | 6π 방향족성 TS, 초면-초면 (p.12) |
| butadiene + dimethyl maleate (Z) | 열 | cis-cyclohex-4-ene-1,2-diester | 해당 없음 | syn(cis) | 입체특이적 (p.19, 28) |
| butadiene + dimethyl fumarate (E) | 열 | trans-cyclohex-4-ene-1,2-diester | 해당 없음 | anti(trans), 라셈 | 입체특이적 (p.19, 28) |
| (E,E)-1,4-diphenylbutadiene + DMAD | 열 | cis-3,6-diphenylcyclohexa-1,4-diene-1,2-diester | 해당 없음 | 두 Ph cis("out"/"out") | 알카인 dienophile (p.20) |
| (E,Z)-RCH=CH-CH=CHR + DMAD | 열 | trans-3,6-disubstituted cyclohexa-1,4-diene diester | 해당 없음 | 두 R trans("in"/"out") | (p.20, 28) |
| (E,E)-hexa-2,4-diene + DMAD / (E,Z) + DMAD | 열 | 3,6-dimethylcyclohexa-1,4-diene-1,2-diester | 해당 없음 | (E,E)는 syn, (E,Z)는 anti | (p.28) |
| cyclopentadiene + maleic anhydride | 열 | endo 부가물 | 해당 없음 | endo만 생성 | 2차 오비탈 겹침 (p.21) |
| (E,E)-hexa-2,4-diene + acrolein | 열 | all-cis 2,5-dimethylcyclohex-3-ene-1-carbaldehyde | 대칭 다이엔 | endo: CHO와 두 Me 모두 cis | (p.23–24) |
| butadiene 2분자 | 가열 | 4-vinylcyclohexene ([4+2]); cycloocta-1,5-diene([4+4])는 생기지 않음 | 해당 없음 | 해당 없음 | [π4s+π2s]는 허용, [π4s+π4s]는 금지 (p.30, 36) |
| (비교) 2-methylcyclohexane-1,3-dione + MVK | 10% NaOH 후 piperidine/가열(−H2O), 또는 EtONa/가열(one-pot) | 이중 고리 enone | Michael → aldol | 4차 탄소 1개 | 극성 메커니즘 (p.6) |
| (비교) I(CH2)4CH=CHCO2Me + CH3NO2 | Cs2CO3, DMF, 20 °C | 2-(2-nitrocyclohexyl)acetic acid methyl ester (65%) | nitro-Michael → 분자 내 SN2 | 표시 없음 | 극성 메커니즘 (p.6) |

## 연습 문제

1. (p.17) 다음 생성물을 만드는 Diels–Alder 반응의 다이엔과 dienophile은 무엇인가? 생성물: tricyclo[5.2.1.0^2,6]deca-3,8-diene(dicyclopentadiene). norbornene 골격에 cyclopentene 고리가 융합된 구조다.
2. (p.17) 다음 생성물을 만드는 다이엔과 dienophile은 무엇인가? 생성물: 벤젠 고리(A)–CH2CH2가 있는 고리(B)–고리 C(cyclohexene: C=C가 고리 B와 공유하는 탄소에서 시작)–고리 D(cyclohexane-1,4-dione)가 차례로 융합된 사환 화합물(steroid형 골격, 고리 C의 C=C는 고리 B 쪽 탄소와 그 이웃 CH 사이에 있음).
3. (p.23–24) (E,E)-hexa-2,4-diene + acrolein의 Diels–Alder 반응에서 endo 규칙에 따라 우세한 생성물은 무엇인가? CHO와 두 Me의 상대 배열로 답하라.
4. (p.19, 28) butadiene을 (a) dimethyl maleate, (b) dimethyl fumarate와 반응시킬 때 생기는 생성물의 상대 입체화학을 쓰고, 이유를 설명하라.
5. (p.20, 28) (a) (E,E)-hexa-2,4-diene + DMAD, (b) (E,Z)-hexa-2,4-diene + DMAD의 생성물에서 두 Me의 관계는 무엇인가?
6. (p.14–16, 27) 다음 쌍에서 DA 반응이 더 빠른 쪽을 고르고 FMO로 설명하라. (a) butadiene + ethylene과 butadiene + acrolein (b) 1,3-butadiene + maleic anhydride와 cyclopentadiene + maleic anhydride (c) 3-methylenecyclohexene + maleic anhydride는 반응하는가?
7. (p.30, 36) 초면-초면 접근을 가정하고, Woodward–Hoffmann 규칙과 FMO로 1,3-butadiene이 열적 [4+2]는 하지만 열적 [4+4]는 하지 않는 이유를 설명하라.
8. (p.18) dicyclopentadiene에서 cyclopentadiene 단량체를 얻는 방법과 그 원리를 쓰고, 단량체를 상온에 두면 어떻게 되는지 설명하라.

## 정답 및 해설

1. **다이엔은 cyclopentadiene, dienophile도 cyclopentadiene이다(이량화).** norbornene 부분의 C=C를 C2=C3로 보고 C1–C6, C4–C5 결합을 끊는다. 그러면 한 분자는 다이엔(s-cis 고정 cyclopentadiene)으로, 다른 분자는 C=C 하나만 쓰는 dienophile로 작용한 것이 보인다. 융합된 cyclopentene 고리의 C=C는 dienophile 분자에 남아 있던 이중 결합이다. 이 반응은 endo 선택적이어서 endo-dicyclopentadiene을 준다(p.29). (출처: L13 p.17, 18, 29)

2. **다이엔: 1-vinyl-3,4-dihydronaphthalene(CH2=CH-C1=C2H-CH2CH2- 벤젠 융합). Dienophile: cyclohex-2-ene-1,4-dione.** 새로 생긴 고리 C에서 C=C(고리 B와 공유하는 탄소 = C3, 그 이웃 CH = C2)를 C2=C3로 놓는다. 고리 C의 CH2가 C1, 고리 B/C 접합 CH가 C4가 된다. 그러면 C1–C6, C4–C5가 새 σ 결합이고, C5와 C6은 고리 C/D 접합 탄소다. C5–C6을 다시 이중 결합으로 바꾸면 양쪽에 C=O가 붙은 cyclohex-2-ene-1,4-dione이 dienophile이 되고, 다이엔은 dihydronaphthalene 고리 안의 C=C와 vinyl기가 s-cis로 짝지어진 다이엔이다. 고리 D에 C=O 외에 다른 C=C가 없으므로 p-benzoquinone(이 경우 생성물에 C=C가 하나 더 남음)이 아니라 cyclohexenedione이 맞다. 보충: 두 C=O는 dienophile을 강하게 활성화하는 EWG다. (보충 근거: Clayden p.886–887) (출처: L13 p.17)

3. **CHO와 두 Me가 모두 cis인 all-cis 2,5-dimethylcyclohex-3-ene-1-carbaldehyde(슬라이드의 왼쪽 생성물: Me, CHO, Me가 모두 hash).** (E,E)-다이엔의 두 Me는 "out"이므로 생성물에서 서로 cis다(입체특이성). endo TS에서는 CHO가 다이엔 아래로 들어간다. 그러면 CHO 탄소의 H는 다이엔 말단의 "in" H들과 반대쪽, 즉 Me 쪽과 반대 방향을 향하게 된다. 결과적으로 세 H(C1-H, C2-H, C5-H)가 모두 한 면(wedge)에, CHO와 두 Me가 모두 반대 면에 놓인다(p.24 그림). exo 생성물은 CHO만 반대쪽(wedge)에 있는 오른쪽 구조다. (출처: L13 p.23–24)

4. **(a) cis(syn)-dimethyl cyclohex-4-ene-1,2-dicarboxylate. (b) trans(anti)-diester(라셈).** DA는 협동적인 초면-초면 반응이다. dienophile의 두 탄소가 같은 면에서 동시에 새 σ 결합을 만들고, C–C 회전이 가능한 중간체가 없다. 따라서 Z-알켄의 cis 관계와 E-알켄의 trans 관계가 그대로 고리에 옮겨진다(입체특이성). (출처: L13 p.19, 28)

5. **(a) syn(cis-3,6-dimethyl). (b) anti(trans-3,6-dimethyl).** s-cis 형태에서 (E,E)-다이엔의 두 Me는 모두 "out"이고, out끼리는 생성물에서 1,4-cis다. (E,Z)-다이엔에서는 Me 하나가 "in", 하나가 "out"이므로 trans가 된다. DMAD는 알카인이라 생성물은 cyclohexa-1,4-diene-1,2-dicarboxylate이다. (출처: L13 p.20, 28)

6. **(a) butadiene + acrolein이 훨씬 빠르다**(150 °C, 0.5 h 대 165 °C, 17 h, 900 atm). CHO(EWG)가 dienophile의 LUMO를 낮춰 다이엔 HOMO–dienophile LUMO 에너지 차이가 줄어들기 때문이다. **(b) cyclopentadiene 쪽이 빠르다.** s-cis로 고정되어 있어 반응 가능한 형태가 100%인 반면, butadiene은 상온에서 약 1%만 s-cis다. 보충: cyclopentadiene의 고리 CH2(알킬)는 다이엔 HOMO를 약간 올리는 효과도 있다(보충 근거: Clayden p.886, 890). **(c) 반응하지 않는다.** 3-methylenecyclohexene은 두 C=C가 s-trans로 고정되어 있어 C1과 C4가 가까워질 수 없다. (출처: L13 p.14–16, 27)

7. **Woodward–Hoffmann:** [4+2]는 [π4s + π2s]다. (4q+2)s 성분(π2s)이 1개, (4r)a 성분이 0개로 합이 1(홀수)이므로 열적으로 허용된다. [4+4]는 [π4s + π4s]다. 두 성분 모두 (4r)s라서 세지 않으므로 (4q+2)s는 0개, (4r)a도 0개이고 합이 0(짝수)이다. 따라서 열적으로 금지된다. **FMO:** [4+2]에서는 한 butadiene의 HOMO(ψ2)와 다른 butadiene의 C=C 하나(dienophile 부분)의 LUMO가 겹치며 양 끝이 모두 결합성이므로, 4-vinylcyclohexene이 생긴다. [4+4]에서는 ψ2(HOMO)와 다른 분자의 ψ3(LUMO)의 양 끝 가운데 한쪽은 결합성이지만 다른 쪽은 위상이 맞지 않아 반결합성이다. 따라서 두 σ 결합을 동시에 만들 수 없어 cycloocta-1,5-diene은 열적으로 생기지 않는다. (출처: L13 p.30, 33–36)

8. **dicyclopentadiene을 가열해 분해(crack)하고 증류한다.** 가열하면 역 DA 반응이 일어나 단량체가 생긴다. 끓는점이 낮은 cyclopentadiene(b.p. 42 °C)이 끓는점이 높은 이량체에서 증류되어 빠져나가므로 평형이 단량체 쪽으로 이동한다. 단량체는 −20 °C에서는 며칠 보관할 수 있지만, 상온에서는 몇 시간 안에 DA 이량화(endo)로 다시 dicyclopentadiene이 된다. 그래서 사용 직전에 새로 분해해서 쓴다. (출처: L13 p.18)

## 각주

[1] 보충: Claisen 자리옮김은 [3,3]-시그마트로픽 자리옮김의 한 종류다. p.5의 분류에서 고리화 첨가와는 다른 갈래(시그마트로픽 자리옮김)에 속한다. (보충 근거: Clayden p.909) (출처: L13 p.4–5)

[2] 보충: 첫 번째 예는 Robinson 고리 만들기(Robinson annulation, Michael 첨가 + 분자 내 aldol 축합)이고, 생성물은 Wieland–Miescher ketone으로 알려진 화합물이다(→ 엔올레이트·aldol·Robinson 고리 만들기 관련 강의 참고). (보충 근거: Clayden p.638–639, 845) (출처: L13 p.6)

[3] Diels–Alder 반응은 Otto Diels와 Kurt Alder가 1928년에 처음 보고했고, 두 사람은 이 업적으로 1950년 노벨 화학상을 받았다. (출처: L13 p.7)

[4] 보충: 엄밀히 세면 π 결합 3개가 끊어지고, π 결합 1개(C2=C3)와 σ 결합 2개가 새로 생긴다. 순수하게 보면 π 결합 2개가 σ 결합 2개로 바뀐 셈이다. (보충 근거: Clayden p.878) (출처: L13 p.10)

[5] 보충: Cl과 Ph는 NO2나 C=O만큼 강한 EWG가 아니다. Ph와 Cl은 모두 추가 짝지음(conjugation)을 제공해 dienophile을 활성화하는 치환기로 분류되며, 그 효과도 상대적으로 작다. (보충 근거: Clayden p.880, 890) (출처: L13 p.14)

[6] 보충: 이 부가물은 chlorendic anhydride로 불린다. (출처: L13 p.18)

[7] 보충: endo 생성물은 속도론적(kinetic) 생성물이다. 입체 장애가 적은 exo 생성물이 열역학적으로 더 안정한 경우가 많아서, 고온이나 장시간(역 DA가 가능한 가역 조건)에서는 exo 비율이 늘어날 수 있다. (보충 근거: Clayden p.884) (출처: L13 p.22)

[8] 보충: 이렇게 다이엔 HOMO–dienophile LUMO 상호작용이 지배하는 전형적인 경우를 정상 전자 요구(normal electron demand) DA라고 부른다. (보충 근거: Clayden p.886–887) (출처: L13 p.27)

[9] 슬라이드 p.29의 그림에는 아래쪽(dienophile 역할) cyclopentadiene의 오비탈이 "LUMO of diene"이라고 적혀 있다. 그 분자가 화합물로서 다이엔이라는 뜻으로 읽어야 하며, 반응에서의 역할은 dienophile이다(그 C=C의 LUMO). (출처: L13 p.29)

[10] R. B. Woodward와 R. Hoffmann의 첫 논문 "Stereochemistry of Electrocyclic Reactions"는 1964년 말 JACS에 투고되어 1965년 1월호에 실렸다. 슬라이드에는 Woodward가 편집인 Marshall Gates에게 보낸 편지와 게재 승인서가 실려 있다. 1981년 노벨 화학상은 "화학 반응의 진행에 관해 각자 독립적으로 발전시킨 이론"으로 Kenichi Fukui(FMO 이론)와 Roald Hoffmann이 공동 수상했다. Woodward는 1979년에 세상을 떠나 공동 수상하지 못했다(보충). (보충 근거: Clayden p.892) (출처: L13 p.32)
