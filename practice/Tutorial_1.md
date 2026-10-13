# CM3121 Tutorial 1 — 알켄 친전자성 첨가와 방향족 친전자성 치환

> 범위: L1/L2 alkene electrophilic addition, L3/L4 방향족 친전자성 electrophilic aromatic substitution, EAS
> 출처 파일: 문제 `Tutorial_Questions_1.pdf`, 공식 풀이 `Tutorial_1_solution.pdf` (손글씨 스캔본)

---

## 문제 1

1-hexene(1-hexene, CH2=CH-CH2CH2CH2CH3)을 NaCl 수용액 속에서 Br2와 반응시키면 세 가지 생성물의 혼합물이 얻어진다. 세 생성물의 구조를 쓰고 regioselectivity을 설명하라.

`CH2=CH-(CH2)3CH3 --[Br2, NaCl in water]--> 세 생성물의 혼합물`

### 공식 풀이

- 1단계: alkene + Br2 → 고리형 bromonium bromonium ion + Br⁻.
- 2단계: nucleophile(Nu⁻)가 bromonium 고리의 **더 많이 치환된 탄소(C2)**를 공격하여 고리를 연다. Br은 말단 탄소(C1)에 남는다.
- 세 생성물:
  1. Nu = Br: 1,2-dibromohexane(1,2-dibromohexane), BrCH2-CHBr-C4H9
  2. Nu = Cl: 1-브로모-2-클로로헥세인(1-bromo-2-chlorohexane), BrCH2-CHCl-C4H9
  3. Nu = OH(물): 1-브로모헥산-2-올(1-bromohexan-2-ol), BrCH2-CH(OH)-C4H9
- regioselectivity 설명: bromonium 이온에서 더 많이 치환된 탄소가 δ+ 성격(cation성)을 더 많이 띠므로 nucleophile가 그쪽을 공격한다("more substituted, more positive cation character").

(출처: Tutorial_1_solution p.1)

### 해설

이 문제의 핵심은 왜 Br이 한쪽 끝(C1)에만 붙고 Br, Cl, OH는 모두 안쪽 탄소(C2)에 붙느냐이다. 출발점은 Br2가 alkene의 π 전자를 받아 만드는 bromonium 이온이다. 이 3원자 고리는 대칭이 아니다. C1은 일차 탄소이고 C2는 alkyl group(부틸)가 붙은 이차 탄소이므로, C–Br⁺ 결합 중 C2–Br 쪽이 더 길고 약하며 C2에 양전하가 더 많이 쌓인다. 즉 bromonium 이온은 "C2에 부분 cation을 가진 고리"로 보는 것이 정확하다.

그래서 nucleophile는 C2를 공격한다. 그런데 이 용액에는 nucleophile가 셋이나 있다. Br2가 쪼개지며 생긴 Br⁻, 일부러 넣은 Cl⁻, 그리고 용매인 H2O다. 세 nucleophile가 같은 bromonium 이온을 두고 경쟁하므로 세 생성물이 섞여 나온다. 물은 중성 nucleophile라서 공격한 직후에는 옥소늄(R–OH2⁺)이 되고, 양성자를 잃으면 bromohydrin이 된다. 물은 양이 압도적으로 많아서 실제로는 bromohydrin이 많이 생기는 경우가 흔하다. 다만 공식 풀이는 비율을 따지지 않았다.

어느 nucleophile든 공격은 bromonium의 anti에서 일어난다. 그래서 Br과 Nu는 서로 anti로 첨가된다. 이 기질에서는 C1에 입체중심이 없어서 anti 첨가가 눈에 띄는 입체화학으로 드러나지 않는다. C2는 새 입체중심이지만 평면 alkene의 양면이 똑같이 공격받으므로 라세미체가 된다. 결국 이 문제는 "Markovnikov형 regioselectivity = 양전하가 더 안정한 탄소에 nucleophile가 간다"는 원리를 bromonium 이온에 적용한 사례다. (→ [L1](../notes/L01_Electrophilic_Addition_to_Alkenes_Part1.md) 문서의 bromonium·halohydrin 부분 참고)

### 핵심 개념

- bromonium 이온은 비대칭이며, 더 많이 치환된 탄소가 δ+를 더 크게 띤다.
- 여러 nucleophile(Br⁻, Cl⁻, H2O)가 공존하면 경쟁 생성물이 섞인다.
- nucleophile는 더 치환된 탄소를, anti 방향에서 공격한다(Markovnikov형, anti 첨가).

---

## 문제 2

다음 4단계 변환의 각 생성물 구조를 쓰고 입체화학을 설명하라.

출발물: (E)-2-cyclopentyl뷰트-2-엔((E)-2-cyclopentylbut-2-ene, cyclopentyl–C(CH3)=CH–CH3; 그림상 두 methyl이 같은 쪽에 있다)

`알켄 --[9-BBN, THF]--> ? --[H2O2]--> ? --[TsCl, base]--> ? --[KCN (SN2)]--> ?`

### 공식 풀이

- 1단계(수소붕소화, hydroboration): H–BR2는 Hδ⁻–Bδ⁺로 분극되어 있다. B는 덜 치환된 탄소(CH–CH3 쪽)에 붙고, H는 더 치환된 탄소(cyclopentyl이 붙은 쪽, "more substituted, more positive character")에 붙는다. 수소붕소화는 **syn 첨가**다. 생성물은 라세미(±) alkyl보레인으로 그려져 있다.
- 2단계(H2O2): B가 OH로 바뀌며 입체화학이 유지된다. 생성물은 3-cyclopentylbutane-2-올(3-cyclopentylbutan-2-ol)이며, 라세미(±)이다. 풀이 그림에서는 지그재그 Me–C–C–Me 골격 위에, cyclopentyl 쪽 탄소에 cyclopentyl(hash)과 H(wedge)가, 카비놀 탄소에 H(hash)와 OH(wedge)가 그려져 있다.
- 3단계(TsCl, base): OH가 OTs로 바뀌며 입체화학이 유지된다(±).
- 4단계(KCN, SN2): CN⁻이 OTs의 뒤쪽에서 공격하여 **입체 inversion of stereochemistry**이 일어난다. 생성물은 3-cyclopentyl-2-methyl뷰테인나이트릴(3-cyclopentyl-2-methylbutanenitrile)이다.

(출처: Tutorial_1_solution p.1)

### 해설

이 문제의 핵심은 단계마다 입체중심이 "새로 생기는가, 유지되는가, 뒤집히는가"를 끝까지 추적하는 것이다. 첫 단계부터 보자. 9-BBN의 B–H 결합에서 B는 빈 p 오비탈을 가진 electrophile다. 그래서 B가 alkene π 전자를 받는 순간, alkene의 두 탄소 중 양전하를 더 잘 견디는 탄소(cyclopentyl과 methyl이 붙은 삼치환 탄소)에 δ+가 생긴다. 그런데 이 δ+ 탄소로 넘어오는 것은 B가 아니라 B에 붙어 있던 H(δ⁻)다. 즉 4중심 전이상태에서 B는 덜 치환된 탄소에, H는 더 치환된 탄소에 동시에 붙는다. 게다가 9-BBN은 부피가 커서 입체적으로도 덜 붐비는 탄소를 강하게 선호한다. 그 결과가 "반-Markovnikov(anti-Markovnikov)" regioselectivity이다.

그런데 B와 H가 한 번에, 같은 면에서 들어오므로 첨가는 syn이다. 이 기질은 삼치환 alkene이라서 두 탄소 모두 새 입체중심이 된다. 그래서 두 입체중심의 상대배치는 alkene의 기하(E)와 syn 첨가에 의해 하나로 정해진다. alkene의 위·아래 면은 동등하게 공격받으므로 생성물은 라세미체(±)다. 직접 CIP 순위를 매겨 보면 alcohol은 (2R*,3S*)-3-cyclopentylbutane-2-올, 즉 (2R,3S)/(2S,3R) 쌍이다. 이 표기는 공식 풀이의 wedge/hash 그림에서 이 해설이 직접 계산한 값이며, 풀이에 적혀 있지는 않다.

다음으로 H2O2에 의한 산화가 온다(보통 NaOH와 함께 쓴다. 공식 풀이에는 H2O2만 적혀 있다). 하이드로퍼옥사이드 anion이 B에 붙은 뒤 alkyl group이 B에서 O로 1,2-이동하는데, 이 이동은 C–B 결합이 C–O 결합으로 그대로 바뀌는 과정이다. 그래서 탄소의 배치가 **유지**된다. TsCl 단계도 마찬가지다. O–H가 O–Ts로 바뀔 뿐 탄소–산소 결합은 끊어지지 않는다. 즉 이 단계는 OH를 좋은 leaving group으로 바꾸는 단계일 뿐 입체중심은 건드리지 않는다.

마지막 SN2에서 처음으로 입체중심이 뒤집힌다. CN⁻은 C–OTs 결합의 정반대(180°)에서 들어와 leaving group을 밀어내므로, 카비놀이었던 탄소에서 Walden 반전이 일어난다. cyclopentyl 쪽 탄소는 반응에 참여하지 않으므로 그대로다. 그래서 최종 nitrile의 상대배치는 alcohol과 비교해 한 중심만 뒤집힌 형태다. CIP로 따져 보면 (2S*,3S*)-3-cyclopentyl-2-methyl뷰테인나이트릴이다(역시 이 해설의 계산값). 덧붙이자면 이 탄소는 이차이고 옆에 가지 달린 탄소가 있어서 SN2가 아주 빠르지는 않다. 그래도 문제에서 SN2로 지정했으므로 반전으로 처리하는 것이 맞다. (→ [L2](../notes/L02_Electrophilic_Addition_to_Alkenes_Part2.md) 문서의 수소붕소화·9-BBN 부분 참고)

### 핵심 개념

- 수소붕소화: 반-Markovnikov regioselectivity(B는 덜 치환된 탄소), syn 첨가, 라세미체 생성.
- H2O2/NaOH와 TsCl는 입체 유지, SN2는 입체 반전.
- 다단계 문제에서는 각 단계가 입체중심을 생성·유지·반전하는지 분리해서 추적한다.

---

## 문제 3

다음 3단계 변환의 각 생성물 구조를 쓰라.

출발물: 1-ethylcyclohexene(1-ethylcyclohexene)

`1-에틸사이클로헥센 --[Br2, EtOH]--> ? --[tBuOK (E2)]--> ? --[O3, then Me2S]--> ?`

### 공식 풀이

- 1단계: bromonium 이온을 EtOH가 더 치환된 탄소(C1, ethyl이 붙은 탄소)에서 공격한다. 생성물은 trans-2-브로모-1-에톡시-1-ethylcyclohexane이다(Br과 OEt는 trans).
- 2단계(tBuOK, E2): HBr이 제거되어 3-에톡시-3-ethylcyclohexene(3-ethoxy-3-ethylcyclohexene)이 생긴다. 이중결합은 Br이 있던 탄소와 그 옆 CH2 탄소 사이(사차 탄소에서 먼 쪽)에 생긴다.
- 3단계(ozone분해, ozonolysis, 환원적 후처리): C=C가 끊어져 dialdehyde가 된다. 생성물은 OHC–CH2CH2CH2–C(Et)(OEt)–CHO, 즉 2-에톡시-2-ethylhexane다이알(2-ethoxy-2-ethylhexanedial)이다.

(출처: Tutorial_1_solution p.2)

### 해설

이 문제의 핵심은 왜 E2 제거가 "엉뚱해 보이는" 방향으로 일어나는가이다. 먼저 1단계는 문제 1과 같은 논리다. Br2가 bromonium 이온을 만들고, 용매인 EtOH가 nucleophile로 작용한다. bromonium의 두 탄소 중 C1은 삼차(ethyl과 고리 탄소 둘)이고 C2는 이차다. 그래서 양전하가 더 큰 C1을 EtOH가 공격하고, 그 방향은 Br의 anti이다. 즉 Br(C2)과 OEt(C1)는 고리 위에서 trans가 된다. 이것을 bromoether라 하며, halohydrin 형성의 alcohol 버전이다.

그런데 2단계의 E2에서 쓸 수 있는 β-수소를 찾아보면 선택지가 좁다. Br이 붙은 C2의 이웃은 C1과 C3인데, C1은 OEt와 Et가 붙은 사차 탄소라서 H가 아예 없다. 그래서 제거는 C3의 H와만 일어날 수 있다. 게다가 E2는 H와 Br이 anti-periplanar(cyclohexane에서는 trans-diaxial)여야 한다. C3에는 CH2의 수소 두 개가 있으므로 그중 하나는 항상 Br과 diaxial 배치를 이룰 수 있다. 결과적으로 C2=C3 이중결합이 생기고, 원래의 C1은 allyl 위치의 사차 OEt, Et로 남는다. 새로 번호를 매기면 3-에톡시-3-ethylcyclohexene이다. 부피 큰 tBuOK는 SN2 치환 대신 제거를 하도록 고른 염기다.

마지막 ozone분해에서는 고리 안의 C=C가 끊어지므로 고리가 열려 사슬이 된다. 이중결합의 두 탄소가 각각 CHO가 되고, Me2S는 ozonide를 환원적으로 분해해 산이 아닌 aldehyde에서 멈추게 한다. 즉 고리 탄소 6개가 그대로 사슬 6개가 되어 hexane다이알 골격이 되고, 원래 C1이었던 탄소가 한쪽 CHO의 바로 옆(C2)에서 Et와 OEt를 들고 있다. 이 C2는 입체중심이지만 처음부터 라세미였으므로 최종 생성물도 라세미다. (→ [L1](../notes/L01_Electrophilic_Addition_to_Alkenes_Part1.md) 문서 bromonium 부분, L02 문서 ozone분해 부분 참고)

### 핵심 개념

- Br2/ROH: bromoether 형성(Markovnikov, anti 첨가).
- E2의 regioselectivity은 "anti-periplanar β-H가 어디 있는가"가 결정한다. 사차 탄소 쪽으로는 제거가 불가능하다.
- O3 후 Me2S(환원적 후처리): C=C → 두 개의 C=O. 고리 alkene이면 고리가 열린다.

---

## 문제 4

다음 변환에 필요한 시약을 제시하라(여러 단계일 수 있다).

- 시약 A: cis-2-뷰텐(cis-2-butene) → 2,3-butanediol(그림: HO와 OH, 두 H가 같은 쪽, 두 Me가 같은 쪽 → meso 형)
- 시약 B: trans-2-뷰텐(trans-2-butene) → 같은 diol

`cis-2-butene --[reagents A]--> meso-2,3-butanediol <--[reagents B]-- trans-2-butene`

### 공식 풀이

- ① 시약 A: OsO4, NMO. 고리형 오스메이트 ester를 거치는 **syn 첨가**다. cis alkene의 두 Me는 cis로 남고, 두 OH도 같은 면에 붙는다.
- ② 시약 B: (1) mCPBA(에폭시화, epoxidation)로 trans-2,3-dimethyl옥시레인을 만든다. 두 Me는 trans로 유지된다. (2) H2O/H⁺. protonate된 epoxide를 물이 뒤쪽에서 공격하여 고리가 anti. 생성물을 다시 그리면 목표 diol과 같다.

(출처: Tutorial_1_solution p.2)

### 해설

이 문제의 핵심은 왜 서로 다른 두 alkene에서 같은 diol이 나오느냐이다. 답은 "alkene의 cis/trans"와 "첨가의 syn/anti"이 서로 상쇄되기 때문이다. 목표 화합물은 meso-2,3-butanediol이다. 그림처럼 C2–C3 결합을 eclipsed으로 놓으면 두 OH, 두 H, 두 Me가 각각 같은 쪽에 있어 분자 가운데에 거울면이 생긴다.

먼저 cis-2-뷰텐에서는 syn dihydroxylation가 필요하다. OsO4는 alkene의 한쪽 면에서 [3+2] 방식으로 두 O를 동시에 붙여 고리형 오스메이트 ester를 만든다. 그래서 두 OH는 반드시 같은 면에 놓인다. 원래 cis였던 두 Me도 그대로 같은 쪽이므로 meso가 된다. NMO는 Os(VI)를 Os(VIII)로 재산화하는 공동 산화제다. 그래서 값비싸고 독성이 큰 OsO4를 촉매량만 써도 된다.

그런데 trans-2-뷰텐에 같은 OsO4를 쓰면 (±)-diol(트레오 쌍)이 나온다. 그래서 trans alkene에는 anti dihydroxylation가 필요하다. mCPBA는 alkene에 O 하나를 syn으로 전달해 epoxide를 만든다. 이때 두 Me는 trans 그대로다. 이어서 산성 수용액에서 epoxide 산소가 protonate되면, 물이 한 탄소를 C–O 결합의 반대편에서 SN2처럼 공격한다. 즉 두 번째 OH는 첫 번째 OH(원래 epoxide 산소)와 반대 면에 붙는다. trans 기하와 anti 첨가가 만나면 "반대의 반대"가 되어 결과는 meso다. 공식 풀이도 고리가 열린 생성물을 회전시켜 목표 구조와 같음을 보였다.

정리하면 cis + syn = meso, trans + anti = meso, cis + anti = (±), trans + syn = (±)이다. 이 네 조합을 외워 두면 dihydroxylation와 bromination 문제를 빠르게 풀 수 있다. (→ [L2](../notes/L02_Electrophilic_Addition_to_Alkenes_Part2.md) 문서의 OsO4·에폭시화 부분 참고)

### 핵심 개념

- OsO4/NMO: syn dihydroxylation(촉매 OsO4 + 공동 산화제 NMO).
- mCPBA 후 H3O⁺: 에폭시화 후 anti 개환 = 전체적으로 anti dihydroxylation.
- stereospecificity: alkene 기하 × 첨가 방향이 생성물의 상대배치를 결정한다.

---

## 문제 5

다음 각 화합물을 (1) Br2/FeBr3, (2) 진한 HNO3/H2SO4와 반응시킬 때 주생성물을 예측하라.

기질: ethylbenzene, chlorobenzene, anisole, PhOMe, acetanilide(PhNHAc), nitrobenzene

### 공식 풀이

| 기질 | Br2/FeBr3 | HNO3/H2SO4 |
|---|---|---|
| ethylbenzene | para-Br, ortho-Br | para-NO2, ortho-NO2 |
| chlorobenzene | para-Br, ortho-Br | para-NO2, ortho-NO2 |
| 아니솔 | para-Br, ortho-Br | para-NO2, ortho-NO2 |
| acetanilide | para-Br, ortho-Br | para-NO2, ortho-NO2 |
| nitrobenzene | meta-Br (1-브로모-3-nitrobenzene) | meta-NO2 (1,3-dinitrobenzene) |

(출처: Tutorial_1_solution p.3)

### 해설

이 문제의 핵심은 치환기가 왜 특정 위치로 electrophile를 보내느냐이다. 판단 기준은 하나다. electrophile가 붙은 뒤 생기는 cation intermediate(arenium 이온, arenium ion 또는 σ-complex)의 양전하가 어디에 놓이는지 보는 것이다. ortho나 para로 공격하면 공명 구조 중 하나에서 양전하가 치환기가 붙은 ipso 위에 놓인다. meta로 공격하면 그런 공명 구조가 없다.

그래서 ipso 탄소의 양전하를 안정화하는 치환기는 o/p 지향기가 된다. ethyl group은 유도 효과와 초공액으로 전자를 주므로 약한 활성화 o/p 지향기다. OMe와 NHAc는 O와 N의 비공유 전자쌍이 ipso cation에 직접 전자를 밀어 넣어 옥소늄/iminium 형태의 공명 구조를 추가로 만든다. 그래서 강한 활성화 o/p 지향기다. NHAc는 N의 전자쌍이 carbonyl과도 공명하므로 NH2보다는 약하다. 그런데 Cl은 독특하다. 전기음성도 때문에 유도 효과로 고리 전체를 비활성화하지만(반응이 benzene보다 느림), 비공유 전자쌍의 공명 기여는 ortho/para intermediate에서만 가능하다. 즉 "비활성화이지만 o/p 지향"이다.

반대로 NO2는 ipso 탄소에 양전하가 오면 N⁺ 바로 옆에 양전하가 붙는 매우 불리한 구조가 된다. 그래서 ortho/para 공격이 특히 억제되고, 상대적으로 덜 나쁜 meta로 반응한다. 비활성화 meta 지향기다. 니트로벤젠의 반응은 매우 느리므로 실제로는 더 강한 조건이 필요하다.

공식 풀이는 o/p 지향기에 대해 ortho와 para를 모두 적었다. 실제로는 대개 para가 주생성물이다. ortho에는 치환기와의 입체 반발이 있기 때문이다. 이 경향은 부피 큰 NHAc나 Cl에서 특히 강하다. 또 아니솔처럼 강하게 활성화된 고리는 Br2와 반응할 때 다중 bromination가 일어나기 쉬우므로 당량 조절이 필요하다. (→ [L3](../notes/L03_Electrophilic_Aromatic_Substitution_Part1.md)/L4 EAS 강의의 치환기 효과 부분 참고)

### 핵심 개념

- o/p 지향: alkyl(약한 활성화), OMe·NHAc(강한 활성화), 할로젠(비활성화이지만 o/p).
- meta 지향: NO2 등 강한 전자끌개(비활성화).
- 근거는 arenium 이온의 양전하가 ipso 탄소에 놓이는 공명 구조의 안정성이다. o/p 중에서는 입체 효과로 para가 보통 우세하다.

---

## 문제 6

반응 생성물을 예측하고 메커니즘을 제시하라. 생성물은 5원자 고리를 포함한다.

`벤젠 + (브로모메틸)사이클로뷰테인(BrCH2–C4H7) --[AlBr3]--> 5원자 고리를 가진 생성물`

### 공식 풀이

- 생성물: cyclopentylbenzene.
- 메커니즘:
  1. BrCH2–cyclobutyl + AlBr3 → ⁺CH2–cyclobutyl(일차 carbocation) + AlBr4⁻
  2. 고리의 C–C 결합이 cation 중심으로 1,2-이동하며 고리가 확장된다 → cyclopentyl cation.
  3. benzene이 cyclopentyl cation을 공격 → arenium 이온 → H⁺ 손실 → cyclopentylbenzene.

(출처: Tutorial_1_solution p.3)

### 해설

이 문제의 핵심은 왜 cyclobutyl메틸기가 그대로 붙지 않고 cyclopentyl기가 붙느냐이다. Friedel–Crafts alkylation에서 electrophile는 carbocation(또는 그에 가까운 halogenationalkyl–AlBr3 착물)이다. carbocation은 더 안정한 형태로 rearrangement될 기회가 있으면 거의 항상 재배열한다. 그런데 여기서 생기는 ⁺CH2–cyclobutyl은 일차 cation이라 매우 불안정하다.

그래서 이웃한 cyclobutane 고리의 C–C σ 결합이 전자쌍을 들고 cation 중심으로 옮겨 간다(1,2-alkyl 이동). 그러면 원래의 CH2가 고리 안으로 편입되어 4원자 고리가 5원자 고리로 넓어지고, 양전하는 이차 cyclopentyl cation로 옮겨 간다. 이 이동은 두 가지 이유로 강하게 유리하다. 하나는 일차 → 이차 cation의 안정화이고, 다른 하나는 고리 변형 ring strain가 큰 cyclobutane(약 26 kcal/mol)이 거의 변형이 없는 cyclopentane(약 6 kcal/mol)으로 바뀌는 것이다. 즉 전하 안정화와 변형 해소가 같은 방향으로 작용한다.

이후는 일반적인 EAS다. benzene의 π 전자가 cyclopentyl cation을 공격해 arenium 이온을 만들고, AlBr4⁻(또는 Br⁻)가 H⁺를 떼어 내 방향족성이 회복된다. 한 가지 덧붙이면, 공식 풀이는 편의상 자유 일차 cation을 그렸다. 실제로 자유 일차 cation은 거의 생기지 않으며, C–Br–AlBr3 착물의 이온화와 alkyl 이동이 동시에(협동적으로) 일어난다고 보는 것이 더 정확하다. cyclopentylbenzene은 같다. 이 재배열 문제 때문에 다음 문제 7에서는 alkylation 대신 acylation를 쓴다. (→ [L3](../notes/L03_Electrophilic_Aromatic_Substitution_Part1.md) EAS 강의의 Friedel–Crafts alkylation·재배열 부분 참고)

### 핵심 개념

- Friedel–Crafts alkylation는 carbocation 재배열을 동반한다.
- 고리 ring expansion: cyclobutyl카비닐 cation → cyclopentyl cation(전하 안정화 + 변형 해소).
- 일차 halogenationalkyl로는 원하는 일차 alkylbenzene을 직접 얻기 어렵다.

---

## 문제 7

benzene에서 (cyclobutyl메틸)benzene((cyclobutylmethyl)benzene, Ph–CH2–C4H7)을 합성하는 계획을 제시하라.

`벤젠 --[여러 단계]--> Ph–CH2–사이클로뷰틸`

### 공식 풀이

1. `사이클로뷰테인카복실산 --[SOCl2, DMF]--> 사이클로뷰테인카보닐 클로라이드`
2. `벤젠 + 사이클로뷰테인카보닐 클로라이드 --[AlCl3]--> 사이클로뷰틸 페닐 케톤 (Ph–CO–C4H7)` (Friedel–Crafts acylation)
3. `Ph–CO–C4H7 --[Zn/Hg, HCl]--> Ph–CH2–C4H7` (Clemmensen reduction)

(출처: Tutorial_1_solution p.3)

### 해설

이 문제의 핵심은 문제 6의 재배열 함정을 어떻게 피하느냐이다. 목표물은 benzene 고리와 cyclobutane 사이에 CH2가 하나 낀 구조다. 직관적으로는 BrCH2–cyclobutyl로 바로 alkylate하면 될 것 같다. 그런데 문제 6에서 보았듯이 이 electrophile는 고리 확장을 일으켜 cyclopentylbenzene을 준다. 그래서 carbocation을 거치지 않는 electrophile가 필요하다.

그 답이 Friedel–Crafts acylation다. acid chloride이 AlCl3와 만나면 acylium 이온(acylium ion, R–C≡O⁺)이 생긴다. 이 이온은 산소의 비공유 전자쌍이 양전하를 공명으로 안정화하므로 재배열하지 않는다. 그래서 cyclobutyl 고리가 손상되지 않은 채 C=O 탄소가 benzene에 붙는다. 게다가 생성된 아릴 ketone은 carbonyl이 고리를 비활성화하므로 다중 acylation도 일어나지 않는다. 이것도 alkylation보다 나은 점이다. acid chloride은 carboxylic acid을 SOCl2(촉매 DMF, Vilsmeier형 활성화)로 처리해 만든다.

마지막으로 C=O를 CH2로 완전히 환원해야 한다. Clemmensen reduction(Zn(Hg), 진한 HCl)은 아릴 ketone을 methyl렌으로 바꾸는 표준 방법이다. 즉 "acylation + carbonyl 완전 환원" 조합은 일차 alkylbenzene을 재배열 없이 만드는 정석 전략이다. 덧붙이면, 산성에 약한 기질에는 Wolff–Kishner reduction(H2NNH2, KOH, 가열)을 쓰거나, benzyl 위치 ketone이므로 H2/Pd-C 수소화분해를 대안으로 쓸 수 있다. (→ [L3](../notes/L03_Electrophilic_Aromatic_Substitution_Part1.md) EAS 강의의 Friedel–Crafts acylation·Clemmensen 부분 참고)

### 핵심 개념

- acylium 이온은 재배열하지 않는다. 그래서 acylation + 환원으로 재배열 없는 alkylbenzene을 얻는다.
- acylation 생성물은 비활성화되어 다중 치환이 억제된다.
- C=O → CH2: Clemmensen(Zn/Hg, HCl) 또는 Wolff–Kishner(N2H4, KOH).
