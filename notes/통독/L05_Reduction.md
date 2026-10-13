# L5. 환원 반응 (Reduction reactions)

> **통독본**: 2026-10-12 재구성 직전의 강의별 전체 노트(교과서 보강 포함)를 그대로 보존한 사본이다. 강의 흐름대로 한 번에 읽을 때 쓴다. 이후의 수정과 보충은 개념 문서에만 반영되므로, **최신 내용은 개념 문서**가 기준이다. 뼈대 노트: [L5 뼈대](../L05_Reduction.md) · [위키 대문](../../wiki/위키%20대문.md)



> **관련 위키 문서** ([위키 대문](../../wiki/위키%20대문.md))
> - 반응: [SN2 reaction](../../wiki/반응/SN2%20반응.md), [Rosenmund reduction](../../wiki/반응/로젠문트%20환원.md), [hydrogenolysis](../../wiki/반응/수소화분해.md), [Staudinger reduction](../../wiki/반응/스타우딩거%20환원.md), [amide reduction](../../wiki/반응/아마이드%20환원.md), [amine synthesis via azide and nitrile](../../wiki/반응/아자이드·나이트릴을%20거친%20아민%20합성.md), [Eschweiler–Clarke reaction](../../wiki/반응/에슈바일러-클라크%20반응.md), [partial reduction of esters](../../wiki/반응/에스터%20부분%20환원.md), [catalytic hydrogenation](../../wiki/반응/촉매%20수소화.md), [reductive amination](../../wiki/반응/환원성%20아미노화.md)
> - 시약: [DIBAL-H](../../wiki/시약/DIBAL-H.md), [LiAlH4](../../wiki/시약/LiAlH4.md), [LiBH4](../../wiki/시약/LiBH4.md), [NaBH3CN](../../wiki/시약/NaBH3CN.md), [NaBH4](../../wiki/시약/NaBH4.md), [Pd/C](../../wiki/시약/Pd-C.md), [PtO2](../../wiki/시약/PtO2.md), [benzyl ether protecting group](../../wiki/시약/벤질%20에터%20보호기.md), [borane](../../wiki/시약/보레인.md), [pyrrolidine](../../wiki/시약/피롤리딘.md)
> - 개념: [metal hydride reactivity](../../wiki/개념/금속%20수소화물의%20반응성.md), [tetrahedral intermediate](../../wiki/개념/사면체%20중간체.md), [iminium ion](../../wiki/개념/이미늄%20이온.md), [imine](../../wiki/개념/이민.md), [electrophile and nucleophile](../../wiki/개념/친전자체와%20친핵체.md)



> CM3121 Advanced Organic Chemistry, Dr. Zhu Ye. 출처 표기의 p.는 PDF 페이지 번호다.

## 개요

이 강의는 "분자에 수소를 붙이는 법", 즉 reduction을 다룬다. 출발점은 amine이다. 세로토닌, 니코틴, diazepam처럼 몸과 약에서 중요한 분자 상당수가 질소를 품고 있는데, 정작 amine을 깔끔하게 만드는 일은 생각보다 까다롭다. 그래서 강의는 amine 합성 문제를 실마리 삼아 azide·nitrile·amide·imine을 환원하는 방법으로 넘어가고, 거기서 NaBH<sub>4</sub>, LiBH<sub>4</sub>, LiAlH<sub>4</sub>, BH<sub>3</sub>, DIBAL-H라는 금속 metal hydride 시약 세트를 정리한 뒤, 마지막으로 H<sub>2</sub>와 금속 촉매를 쓰는 촉매 catalytic hydrogenation으로 마무리한다. 핵심 질문은 하나다. "분자 안에 환원될 수 있는 자리가 여러 개일 때, 원하는 곳만 환원하려면 어떤 시약을 골라야 하나?" L1에서 alkene의 hydroboration으로 만났던 BH<sub>3</sub>가 여기서는 carbonyl 환원제로 다시 등장하고, 이후 L7(enolate), L10(enamine/iminium), L12(protecting group)에서도 이 강의의 시약들이 계속 쓰인다.

## 1. amine이란 무엇이고, 왜 만들기 어려운가

> 개념 문서: [amine synthesis (overview)](../../wiki/개념/아민%20합성%20개관.md), [pyrrolidine](../../wiki/시약/피롤리딘.md), [SN2 reaction](../../wiki/반응/SN2%20반응.md), [amine synthesis via azide and nitrile](../../wiki/반응/아자이드·나이트릴을%20거친%20아민%20합성.md), [Staudinger reduction](../../wiki/반응/스타우딩거%20환원.md), [amide reduction](../../wiki/반응/아마이드%20환원.md), [reductive amination](../../wiki/반응/환원성%20아미노화.md), [imine](../../wiki/개념/이민.md), [iminium ion](../../wiki/개념/이미늄%20이온.md), [NaBH3CN](../../wiki/시약/NaBH3CN.md), [Eschweiler–Clarke reaction](../../wiki/반응/에슈바일러-클라크%20반응.md)

### 1-0. 일상 속 질소 화합물

왜 하필 amine부터 시작할까? 슬라이드는 세로토닌과 도파민 이야기로 답한다. 둘 다 neurotransmitter로, 한 신경에서 다음 신경으로 시냅스 간극을 건너 전기 신호를 전달한다. 세로토닌은 뇌와 중추신경계 전반에서 식욕, 수면 주기, 기분, 기억과 학습을 조절한다.[1] 그 밖에도 pyridoxine(비타민 B6), thiamine 염화물(비타민 B1), 니코틴, 니코틴산(나이아신, 비타민 B3), 불안·alcohol 금단·발작 치료제인 Valium, 항히스타민제 chlorpheniramine, 히스타민이 모두 질소 화합물이다. 생선 비린내의 원인 중 하나인 trimethylamine도 여기에 속한다. 즉 질소 화합물은 생화학적 성질의 폭이 매우 넓고, 그래서 amine을 만드는 법은 유기합성의 기본기가 된다.

(출처: L5 p.2-3)

### 1-0-1. amine의 분류와 성질

amine은 N에 붙은 탄소 수에 따라 1차(RNH<sub>2</sub>), 2차(R<sub>2</sub>NH), 3차(R<sub>3</sub>N)로 나뉜다. N에 기가 네 개 붙을 수도 있는데, 이때는 N이 형식 양전하를 띠어야 하므로 4차 quaternary ammonium salt이 된다. 또 alkyl group이 붙은 alkylamine과 아릴기가 붙은 arylamine으로도 나누는데, 화학은 대체로 비슷하지만 차이도 상당하다.

amine의 화학을 한 줄로 요약하면 "N의 비공유 전자쌍"이다. 이 전자쌍 때문에 amine은 염기이자 nucleophile이 된다. 그런데 같은 N을 가진 amide(RCONH<sub>2</sub>)는 사정이 다르다. amide는 수용성 산에 protonate되지 않을 만큼 염기성이 없고, 친핵성도 약하다.[2] 이 차이는 뒤에서 "amide를 환원하면 amine이 된다"는 사실과 맞물려 중요해진다.

고리형 amine도 이름을 익혀 두자. 7원 고리 azepane, 6원 고리 piperidine·piperazine·모폴린(morpholine), 5원 고리 pyrrolidine, 4원 고리 azetidine, 3원 고리 aziridine이다.[3]

(출처: L5 p.4)

### 1-1. S<sub>N</sub>2로 amine 만들기: 왜 생각대로 안 되나

가장 단순한 발상은 NH<sub>3</sub>를 nucleophile로 써서 alkyl halide을 S<sub>N</sub>2로 치환하는 것이다.

`NH3 (대과량) + R-X --> [R-NH3+ X-] --> RNH2 + NH4+ X-`

메커니즘은 이렇다.
1. NH<sub>3</sub>(nucleophile)의 N 비공유 전자쌍이 R-X의 electrophile을 뒤에서 공격하고, C-X 결합이 끊어지면서 C-N 결합이 생긴다. 결과물은 alkyl암모늄염 R-NH<sub>3</sub><sup>+</sup>X<sup>-</sup>다.
2. 옆에 있던 NH<sub>3</sub>가 N-H 양성자를 떼어 가면 중성 RNH<sub>2</sub>와 NH<sub>4</sub><sup>+</sup>X<sup>-</sup>가 남는다.

실제로 2-bromopropanoic acid 1 mol에 NH<sub>3</sub>를 무려 70 mol 넣으면 alanine(암모늄염 형태)을 65-70%로 얻을 수 있다.

`CH3CH(Br)COOH (1 mol) + NH3 (70 mol) --> CH3CH(NH2)COO- NH4+ (알라닌, 65-70%)`

그런데 왜 NH<sub>3</sub>를 그렇게 많이 넣어야 할까? 1-bromooctane에 NH<sub>3</sub>를 2 eq만 넣어 보면 답이 나온다.

`CH3(CH2)6CH2Br + NH3 (2 eq) --> 옥틸아민 (45%) + 다이옥틸아민 (43%) + 트라이옥틸아민 (미량) + 테트라옥틸암모늄 브로마이드 (미량)`

원하는 1차 amine과 거의 같은 양의 2차 amine이 섞여 나온다. 이것이 over-alkylation이다. 원인은 생성물 자체에 있다. 새로 생긴 RNH<sub>2</sub>는 alkyl group의 전자 공여 덕분에 NH<sub>3</sub>보다 오히려 더 좋은 nucleophile라서, 남은 RX를 먼저 낚아채 버린다.[4] 즉 반응이 "한 번만 일어나고 멈추는" 장치가 없다. 그래서 아래의 방법들은 모두 "N을 한 번만 붙이고 나중에 환원으로 amine을 드러내는" 전략으로 이 문제를 피한다.

(출처: L5 p.5-6)

### 1-1a. azide 이온 alkylation 후 환원

overalkylation을 막으려면 어떻게 해야 할까? 한 가지 답은 nucleophile을 NH<sub>3</sub> 대신 azide 이온 N<sub>3</sub><sup>-</sup>로 바꾸는 것이다. azide 이온은 좋은 nucleophile라 S<sub>N</sub>2가 잘 되지만, 생성물인 alkyl azide R-N<sub>3</sub>는 더 이상 친핵성이 없다. 그래서 반응이 정확히 한 번에서 멈추고, 그다음 환원하면 1차 amine만 얻는다.

`R-X + N3- --[S_N2, -X-]--> R-N3 --[LiAlH4 또는 H2/Pd 또는 PPh3]--> RNH2`

예: `1-브로모-2-페닐에테인 PhCH2CH2Br --[NaN3, EtOH]--> 2-페닐에틸 아자이드 PhCH2CH2N3 --[1. LiAlH4, ether; 2. H2O]--> 2-페닐에틸아민 PhCH2CH2NH2 (89%)`

환원 시약으로 PPh<sub>3</sub>도 쓸 수 있다는 점이 흥미롭다.[5]

(출처: L5 p.7)

### 1-1b. cyanide 이온 alkylation 후 환원

비슷한 발상으로 cyanide 이온을 쓸 수도 있다. 다만 이번에는 탄소 nucleophile이므로, 결과적으로 탄소가 하나 늘어난 1차 amine이 된다는 점이 다르다. CN의 탄소가 그대로 CH<sub>2</sub>NH<sub>2</sub>의 CH<sub>2</sub>가 되기 때문이다.

`RCH2X --[NaCN]--> RCH2C≡N --[1. LiAlH4, ether; 2. H2O 또는 H2/Pd]--> RCH2CH2NH2 (1차 아민)`

(출처: L5 p.8)

### 1-2. amide를 환원해 amine 만들기

앞의 두 방법은 1차 amine만 준다. 2차·3차 amine이 필요하면 어떻게 할까? 여기서 amide가 나선다. amide는 LiAlH<sub>4</sub> 또는 BH<sub>3</sub>로 환원하면 C=O가 통째로 CH<sub>2</sub>가 되어 amine이 된다. amide의 N에 무엇이 붙어 있느냐에 따라 1차, 2차, 3차 amine을 모두 만들 수 있다.

`RCOOH --[1. SOCl2; 2. NH3]--> RCONH2 --[1. LiAlH4, ether; 2. H2O (또는 BH3)]--> RCH2NH2`

예: `벤질아민 PhCH2NH2 --[CH3COCl, base]--> PhCH2NHCOCH3 --[(1) LiAlH4; (2) H2O]--> N-벤질에틸아민 PhCH2NHCH2CH3`

이 두 단계를 합쳐 보면 결국 benzylamine의 N에 ethyl group을 하나 붙인 셈이다. 그런데 왜 ethyl bromide로 직접 alkylate하지 않을까? 직접 alkylation은 1-1에서 본 overalkylation이 일어나지만, acylation은 생성물인 amide가 친핵성이 약하므로(1-0-1) 딱 한 번에서 멈춘다. 즉 "acylation 후 환원"은 깔끔한 N-alkylation의 우회로다.

보충: 왜 ester는 alcohol이 되는데 amide는 amine이 될까? LiAlH<sub>4</sub>의 첫 수소화물이 붙어 tetrahedral intermediate가 생기는 데까지는 둘이 같다. 갈림길은 그다음이다. ester의 intermediate는 alkoxide(OR<sup>-</sup>)를 내보내 aldehyde가 되고, 이것이 다시 환원되어 alcohol이 된다. amide의 intermediate에서는 R<sub>2</sub>N<sup>-</sup>가 너무 나쁜 leaving group라 떨어지지 못하고, 대신 Al에 배위해 이탈 능력이 커진 산소가 떨어지면서 N의 비공유 전자쌍이 C=N<sup>+</sup>를 만든다. 이 iminium 이온이 두 번째 수소화물을 받아 amine이 된다. 2-4의 BH<sub>3</sub> 메커니즘도 같은 줄거리다. (보충 근거: Clayden p.531)

(출처: L5 p.9)

### 1-3. 환원성 아미노화 (Reductive amination)

#### 무엇을 하는 반응인가

amine을 만드는 가장 강력하고 범용적인 방법이 환원성 아미노화다. aldehyde나 ketone에 amine을 섞고 환원제를 넣으면, carbonyl 탄소에 N이 붙은 amine이 생긴다.

- `벤즈알데하이드 PhCHO --[NH3, H2, Ni]--> 벤질아민 PhCH2NH2 (89%)`
- `PhCHO --[(1) CH3CH2NH2; (2) LiBH3CN]--> N-벤질에탄아민 PhCH2NHCH2CH3 (89%)`
- `사이클로헥산온 --[(1) (CH3)2NH; (2) NaBH3CN]--> N,N-다이메틸사이클로헥산아민 (52-54%)`

(출처: L5 p.10)

#### 어떻게 일어나나

그렇다면 환원제는 정확히 무엇을 환원하는 걸까? carbonyl이 아니라 그 사이에 생기는 C=N이다.

1. amine N(nucleophile)이 carbonyl electrophile을 공격하고 C=O π 결합이 끊어져 O<sup>-</sup>가 된다. 양성자가 옮겨 가면(두 단계) hemiaminal R(R')C(OH)NHR''이 생긴다.
2. OH가 protonate되어 물로 떨어지고(-H<sub>2</sub>O), N의 비공유 전자쌍이 밀고 들어와 C=N을 만든다. 이것이 imine R(R')C=NR''이다. 여기까지는 모두 가역적이다.
3. imine(또는 protonate된 iminium 이온)의 C=N 탄소에 수소화물 [H]가 붙어 2차 amine R(R')CH-NHR''이 된다.

![환원성 아미노화: 1차 amine이 carbonyl을 공격해 헤미아미날과 imine을 거쳐 2차 amine이 되는 과정](../../figures/L05/reductive_amination.svg)

*그림: 왼쪽의 굽은 화살표 둘이 첫 단계다. (1) amine N의 비공유 전자쌍(파랑, nucleophile)이 carbonyl 탄소(빨강, electrophile)를 공격하고, (2) C=O π 전자가 산소로 올라간다. 양성자 이동 두 번(two steps)을 거치면 헤미아미날이 되고(새 C–N 결합은 초록), 물이 빠지면 imine이 된다. 마지막으로 [H]가 C=N 탄소에 붙어 2차 amine이 된다(초록 C–H). 슬라이드처럼 헤미아미날 ⇌ imine은 가역 화살표로 그렸다.*

슬라이드 그림에서는 헤미아미날과 imine이 함께 [H]로 이어져 있지만, 실제로 수소화물을 받는 것은 C=N(imine/iminium) 쪽이다.

amine의 종류에 따라 결과가 한 단계씩 올라간다. NH<sub>3</sub>를 쓰면 1차, 1차 amine을 쓰면 2차, 2차 amine을 쓰면 3차 amine이 된다. 그런데 2차 amine은 N에 H가 하나뿐이라 중성 imine을 만들 수 없다. 그 대신 iminium 이온(R<sub>2</sub>C=N<sup>+</sup>R<sub>2</sub>)을 거쳐 환원된다.[6] (→ [L10](L10_Enol_and_Enamine.md) enol과 enamine 문서의 iminium 이온 참고)

(출처: L5 p.11)

#### NaBH<sub>3</sub>CN을 쓴 예

슬라이드는 NaBH<sub>3</sub>CN, pH 3-4, C<sub>2</sub>H<sub>5</sub>OH 조건[7]의 세 예를 1차·2차·3차 amine 순서로 보여 준다.

- `3-methyl뷰탄알 (CH3)2CHCH2CHO + NH3 --> 3-methyl뷰탄-1-아민 (CH3)2CHCH2CH2NH2 (1차)`
- `사이클로헥실메탄아민 C6H11CH2NH2 + 아세톤 --> N-(사이클로헥실메틸)프로판-2-아민 C6H11CH2NHCH(CH3)2 (2차)`
- `피롤리딘 + 2-methyl프로판알 (CH3)2CHCHO --> 1-아이소뷰틸피롤리딘 (3차)`

역합성할 때 쓸 만한 요령이 하나 있다. 생성물에서 새 C-N 결합의 탄소 쪽을 보면, 그 탄소가 carbonyl에서 왔고 거기엔 반드시 H가 하나 이상 붙어 있다(환원 때 들어온 H). 이 H가 없는 탄소, 예컨대 3차 alkyl group은 환원성 아미노화로 N에 붙일 수 없다.

(출처: L5 p.12)

슬라이드 p.13(PhCH<sub>2</sub>CH<sub>2</sub>NHCH<sub>3</sub> 합성)과 p.14(거미 독소 전구체의 다른 amine/aldehyde 조합)의 연습은 아래 연습 문제 1, 2번으로 옮겼다.

(출처: L5 p.13-14)

### 1-4. Eschweiler–Clarke methylation

N에 methyl group을 두 개 붙이고 싶다면 더 간단한 방법이 있다. 1차 amine을 formaldehyde(HCHO)와 포름산(HCOOH)으로 처리하면 N,N-dimethyl 3차 amine이 된다.

`R-NH2 --[HCHO, HCOOH]--> R-N(CH3)2`

여기서 흥미로운 점은 금속 수소화물이 전혀 없다는 것이다. 그럼 수소화물은 어디서 올까? 슬라이드의 답은 "HCOOH가 수소화물 공급원"이다.

1. RNH<sub>2</sub>가 HCHO와 축합(-H<sub>2</sub>O)하여 imine R-N=CH<sub>2</sub>가 된다.
2. HCOOH가 imine을 protonate해 iminium R-NH<sup>+</sup>=CH<sub>2</sub>와 포름산 이온 HCOO<sup>-</sup>가 생긴다.
3. 포름산 이온의 C-H가 수소화물로 iminium 탄소에 넘어가고, 남은 부분은 CO<sub>2</sub>로 빠져나간다. 결과는 R-NH-CH<sub>3</sub>.
4. 이 2차 amine이 다시 HCHO와 반응(+H<sup>+</sup>, -H<sub>2</sub>O)해 iminium R-N<sup>+</sup>(CH<sub>3</sub>)=CH<sub>2</sub>가 된다.
5. HCOO<sup>-</sup>가 한 번 더 수소화물을 주고 CO<sub>2</sub>가 빠지면 R-N(CH<sub>3</sub>)<sub>2</sub>가 된다.

![포름산 이온의 C–H 수소화물이 iminium 탄소로 옮겨 가고 CO2가 빠지는 Eschweiler–Clarke 핵심 단계](../../figures/L05/eschweiler_hydride.svg)

*그림: 3번 단계(첫 번째 수소화물 전달)다. 포름산 이온의 H–C 결합(파랑)이 수소화물로서 iminium 탄소(빨강)를 공격하고, O<sup>-</sup>의 비공유 전자쌍이 내려와 C=O를 하나 더 만들어 CO<sub>2</sub>가 떨어져 나간다. iminium의 C=N π 전자는 N으로 돌아가 양전하를 없앤다. 새로 생긴 C–H 결합은 초록이다. 5번 단계도 같은 방식이다. 보충: 슬라이드에는 앞의 두 화살표만 있고, C=N π → N 화살표는 전자 수를 맞추려고 덧붙였다.*

그럼 왜 4차 암모늄염까지 가지 않을까? 3차 amine은 N에 H가 없어 HCHO와 iminium을 만들 수 없기 때문이다. 즉 이 반응은 구조적으로 3차 amine에서 멈춘다. 1-1의 직접 alkylation과 정반대의 장점이다. CO<sub>2</sub> 기체가 빠져나가는 것도 반응을 비가역적으로 밀어 준다.

(출처: L5 p.15)

### 1-5. 응용: Venlafaxine 합성

지금까지의 도구가 실제 약 합성에서 어떻게 엮이는지 보자. 벤라팍신은 뇌의 세로토닌과 노르아드레날린 농도를 높이는 것으로 생각되는 항우울제다.

1. **C-C 결합 만들기** (슬라이드 표기: "enolate chemistry"): `4-메톡시페닐아세토나이트릴 --[LDA; 사이클로헥산온]--> 1-[사이아노(4-메톡시페닐)메틸]사이클로헥산올 (83%)`. LDA가 nitrile α-H를 떼고, 생긴 탄소 anion이 ketone C=O에 첨가한다.[8] (→ [L7](L07_Enolate_Alkylation.md) enolate alkylation 문서의 LDA 참고)
2. **nitrile → 1차 amine** (1-1b의 환원): `--[H2, 5% Rh/Al2O3]--> 1-[2-아미노-1-(4-메톡시페닐)에틸]사이클로헥산올 (57%)`.
3. **N,N-dimethyl화** (1-4의 Eschweiler–Clarke): `--[HCHO, HCOOH, reflux]--> 벤라팍신 (80%, HCl 염)`.

그런데 2와 3을 한 번에 할 수는 없을까? 특허 경로[9]가 바로 그것이다. 사이아노 alcohol을 `H2 (12 bar), Pd/C (5%), HCHO (2.2 eq)`로 처리하면 벤라팍신이 94%로 나온다. nitrile 수소화로 생긴 1차 amine이 같은 용기 안의 HCHO와 환원성 아미노화(H<sub>2</sub>/Pd가 환원제)를 두 번 연달아 겪는 것이다. HCHO가 2.2 eq인 이유도 methyl group 두 개를 붙여야 하기 때문이다. 슬라이드의 빈 상자 두 개는 연습 문제 3번으로 옮겼다.

(출처: L5 p.16)

## 2. 금속 수소화물에 의한 환원

> 개념 문서: [metal hydride reactivity](../../wiki/개념/금속%20수소화물의%20반응성.md), [NaBH4](../../wiki/시약/NaBH4.md), [LiBH4](../../wiki/시약/LiBH4.md), [LiAlH4](../../wiki/시약/LiAlH4.md), [borane](../../wiki/시약/보레인.md), [amide reduction](../../wiki/반응/아마이드%20환원.md), [tetrahedral intermediate](../../wiki/개념/사면체%20중간체.md), [partial reduction of esters](../../wiki/반응/에스터%20부분%20환원.md), [DIBAL-H](../../wiki/시약/DIBAL-H.md)

### 2-0. 개요: 어떤 시약이 무엇을 환원하나

분자에 carbonyl이 여럿 있으면 어느 것이 먼저 환원될까? 이 질문에 답하려면 두 가지 서열을 함께 봐야 한다. 하나는 시약의 세기, 다른 하나는 carbonyl의 반응성이다.

시약의 세기는 LiAlH<sub>4</sub> > LiBH<sub>4</sub> > NaBH<sub>4</sub> > NaBH<sub>3</sub>CN 순이고, 강할수록 선택성은 떨어진다. carbonyl 쪽은 aldehyde > ketone > ester > amide > carboxylate 순으로 반응성이 크다. 그래서 약한 시약일수록 왼쪽(반응성 큰 carbonyl)만 건드리고, 강한 시약은 오른쪽까지 다 환원한다. 여기에 BH<sub>3</sub>와 DIBAL이라는 "특수 시약"이 이 단순한 서열을 벗어나는 독특한 선택성을 보인다.

(출처: L5 p.18)

슬라이드 p.17의 반응성 표를 정리하면 다음과 같다(O = 환원됨, 느림 = 느리게 환원, X = 보통 환원 안 됨).

| 시약 | imine | aldehyde | ketone | ester | amide | carboxylic acid |
|---|---|---|---|---|---|---|
| NaCNBH<sub>3</sub> | O | 느림 | 느림 | X | X | X |
| NaBH<sub>4</sub> | O | O | O | 느림 | X | X |
| LiBH<sub>4</sub> | O | O | O | O | X | X |
| LiAlH<sub>4</sub> | O | O | O | O | O | 느림 |
| BH<sub>3</sub> | O | 느림 | 느림 | 느림 | O | O |

생성물은 imine → RCH<sub>2</sub>NHR, aldehyde → RCH<sub>2</sub>OH, ketone → R<sub>2</sub>CHOH, ester → RCH<sub>2</sub>OH, amide → RCH<sub>2</sub>NR<sub>2</sub>, carboxylic acid → RCH<sub>2</sub>OH다. aldehyde 단계에서 멈추고 싶다면 우회로가 필요하다. ester는 alcohol을 거치거나(환원 후 산화) DIBAL을 쓰고, amide는 LiAlH<sub>4</sub>를 0 °C에서 쓰며, carboxylic acid은 acid chloride을 거친다(3-2의 Rosenmund reduction).

표에서 눈여겨볼 줄은 NaCNBH<sub>3</sub>다. imine은 환원하면서 aldehyde·ketone은 느리게만 건드린다. 게다가 pH > 3의 수용액에서도 안정하다. 그래서 환원성 아미노화에 흔히 쓰인다. 슬라이드는 "왜 NaBH<sub>4</sub>는 안 쓰나?"라고 묻는데, 이 질문은 연습 문제 4번으로 옮겼다.

한 가지 짚어 둘 점이 있다. 표에서 LiAlH<sub>4</sub>의 carboxylic acid 칸은 "느림"인데, p.23에서는 LiAlH<sub>4</sub>가 carboxylic acid을 92%로 잘 환원한다. 모순처럼 보이지만, 산의 O-H가 먼저 수소화물과 반응해 H<sub>2</sub>를 내고 carboxylate가 되기 때문에 느려질 뿐이며 충분한 양을 쓰면 환원된다.[10]

(출처: L5 p.17)

### 2-1. NaBH<sub>4</sub>: 가장 흔한 온화한 환원제

#### 무엇을, 어떻게 환원하나

NaBH<sub>4</sub>는 아마 가장 많이 쓰이는 환원제일 것이다. 온화해서 aldehyde와 ketone만 alcohol로 바꾸고, 보통 ethanol이나 methanol에서 시약을 과량 써서 반응시킨다.

- `뷰탄알 CH3CH2CH2CHO --[NaBH4, MeOH]--> 1-뷰탄올 (85%)`
- `뷰탄온 CH3COCH2CH3 --[NaBH4, MeOH]--> 2-뷰탄올 (87%)`

메커니즘의 이름은 "hydride" 첨가다.
1. BH<sub>4</sub><sup>-</sup>의 B-H 결합 전자쌍이 nucleophile로서 carbonyl electrophile을 공격한다. C-H 결합이 생기고 C=O π 결합이 끊어져 alkoxide가 된다.
2. alkoxide O가 용매 EtOH의 H를 받아 alcohol이 되고, 남은 EtO<sup>-</sup>는 BH<sub>3</sub>에 붙어 EtOBH<sub>3</sub><sup>-</sup>가 된다.
3. 그런데 EtOBH<sub>3</sub><sup>-</sup>에는 아직 B-H가 남아 있으니 여전히 환원제다.

![NaBH4의 수소화물이 ketone 탄소를 공격하고 alkoxide가 EtOH에서 양성자를 받는 메커니즘](../../figures/L05/nabh4_ketone.svg)

*그림: 왼쪽은 1번 단계다. BH<sub>4</sub><sup>-</sup>의 B–H 결합(파랑, nucleophile)이 carbonyl 탄소(빨강, electrophile)를 공격하고 C=O π 전자는 산소로 간다. 가운데는 2번 단계다. alkoxide O<sup>-</sup>(파랑)의 비공유 전자쌍이 EtOH의 H(빨강)를 가져가고, H–O 결합 전자는 O에 남아 EtO<sup>-</sup>가 된다. 새 C–H 결합은 초록이다. EtO<sup>-</sup>는 BH<sub>3</sub>와 만나 EtOBH<sub>3</sub><sup>-</sup>가 된다.*

(출처: L5 p.19)

#### 한 분자가 몇 번 일하나, 그리고 왜 EtOH인가

3번 단계에서 짐작할 수 있듯, BH<sub>4</sub><sup>-</sup> 하나는 수소화물 네 개를 모두 쓸 수 있다. 슬라이드의 stoichiometry이 이것을 보여 준다.

`4 R2CO + NaBH4 --> Na[B(OCHR2)4] --[4 H2O]--> NaB(OH)4 + 4 R2CHOH`

그렇다면 용매는 아무 alcohol이나 써도 될까? 그렇지 않다. NaBH<sub>4</sub>는 물에 잘 녹고 물과는 느리게 반응해 H<sub>2</sub>를 내며, 알칼리를 넣으면 이 반응이 더 느려진다. 문제는 methanol이다. methanol과는 빠르게 반응해서 60 °C에서 24분이면 H<sub>2</sub>가 100% 발생하지만, 같은 조건의 ethanol에서는 2%도 안 된다. 즉 methanol은 환원제를 갉아먹는다. 그래서 슬라이드의 결론은 "**EtOH가 MeOH보다 좋은 용매**"다.[11]

실험 사진 예시는 `4-tert-뷰틸사이클로헥산온 --[NaBH4, ethanol]--> 4-tert-뷰틸사이클로헥산올`이며, TLC(S = 출발물, C = co-spot, R = 반응액)로 진행을 확인한다.[12]

(출처: L5 p.20)

#### aldehyde와 ketone을 구별할 수 있을까

NaBH<sub>4</sub>는 aldehyde와 ketone을 둘 다 환원하지만, 속도는 크게 다르다. isopropyl alcohol에서 0 °C의 2차 속도상수는 benzaldehyde가 820 × 10<sup>-4</sup>, acetophenone이 2.05 × 10<sup>-4</sup> M<sup>-1</sup>s<sup>-1</sup>로, 약 400배 차이다. 그러니 ketone이 함께 있어도 aldehyde만 골라 환원할 수 있다.

보충: 이 400배 차이를 교과서는 주로 입체 장애로 설명한다. aldehyde 탄소에는 작은 H가 붙어 있지만 ketone 탄소에는 탄소 치환기가 둘이라, 수소화물이 접근하기 더 어렵다. 같은 맥락에서 NaBH<sub>4</sub>가 물·alcohol에서도 쓸 수 있을 만큼 "약한" 수소화물 공여체인 반면 LiAlH<sub>4</sub>가 물과 격렬히 반응할 만큼 센 이유도 중심 원자에 있다. Al이 B보다 전기 양성적(더 금속적)이라 Al–H의 수소화물을 더 쉽게 내주기 때문이다. (보충 근거: Clayden p.132)

용매를 바꾸면 이 차이가 더 극단적이 된다. 비양성자성 용매 다이글라임(diglyme, CH<sub>3</sub>OCH<sub>2</sub>CH<sub>2</sub>OCH<sub>2</sub>CH<sub>2</sub>OCH<sub>3</sub>)에서는 aldehyde는 환원되지만 ketone(acetone)은 전혀 환원되지 않는다.

같은 페이지에서 두 가지가 더 나온다. 첫째, LiAlH<sub>4</sub>는 너무 반응성이 커서 쓸 수 있는 용매가 탄화수소, ether, 3차 amine으로 제한되며, 보통 diethyl ether, THF, 다이글라임을 쓴다. 둘째, cation이 중요하다. NaBH<sub>4</sub>는 ethyl acetate나 ethyl benzoate 같은 ester를 아주 느리게만 환원하지만, LiBH<sub>4</sub>는 쉽게 환원한다. 이 관찰이 다음 소절로 이어진다.

(출처: L5 p.21)

### 2-2. LiBH<sub>4</sub>: ester는 잡고 산은 놔두는 시약

Na<sup>+</sup>를 Li<sup>+</sup>로 바꾸기만 했는데 왜 ester가 환원될까? 보통 Li<sup>+</sup>가 더 강한 Lewis 산으로서 carbonyl 산소에 배위해 carbonyl을 활성화하기 때문이라고 설명한다.[13] 그 결과 LiBH<sub>4</sub>는 NaBH<sub>4</sub>보다 강하고 LiAlH<sub>4</sub>보다는 온화한 중간 세기의 시약이 된다. aldehyde와 ketone은 물론 환원하고, 특히 carboxylic acid·amide·nitrile이 있어도 **ester와 락톤**만 골라 alcohol로 바꾸는 데 쓰인다.

`MeO2C-CH2-CH(CH3)-CH2-CO2H --[LiBH4, EtOH]--> HO-CH2-CH2-CH(CH3)-CH2-CO2H`

ester 쪽만 CH<sub>2</sub>OH가 되고 산은 그대로 남는다. 산이 살아남는 이유는 2-0의 서열에서 찾을 수 있다. 산은 수소화물 시약과 만나면 deprotonate되어 carboxylate가 되는데, carboxylate는 반응성 서열의 맨 끝이다.

(출처: L5 p.22)

### 2-3. LiAlH<sub>4</sub>: 거의 다 환원하는 강력한 시약

LiAlH<sub>4</sub>는 강한 환원제다. carboxylic acid, ester, aldehyde는 1차 alcohol로, ketone은 2차 alcohol로 환원하고, 1-2에서 봤듯 amide는 amine으로 바꾼다.

- `2,2-다이메틸프로판산 (CH3)3CCO2H --[(1) LiAlH4, Et2O; (2) H2O/H2SO4]--> 네오펜틸 알코올 (CH3)3CCH2OH (92%)`
- `RCO2R' --[(1) LiAlH4, Et2O; (2) H2O/H2SO4]--> RCH2OH + R'OH`

ester를 환원하면 alcohol이 두 개 나온다는 점에 주의하자. acyl 쪽은 RCH<sub>2</sub>OH가 되고 알콕시 쪽은 R'OH로 떨어져 나온다. 슬라이드는 LiAlH<sub>4</sub>를 "pyrophoric chemical"로 경고하는데, 물과 격렬히 반응하므로 다룰 때 조심해야 한다.[14]

(출처: L5 p.23)

#### 할로젠도 떼어 낸다

LiAlH<sub>4</sub>는 carbonyl뿐 아니라 alkyl halide도 환원해 할로젠을 H로 바꾼다.

- `2-브로모펜테인 --[(1) LiAlH4, ether; (2) H2O/H2SO4]--> 펜테인`
- `(1-브로모에틸)벤젠 PhCH(Br)CH3 --[(1) LiAlD4, ether; (2) H2O/H2SO4]--> PhCHDCH3`

두 번째 예는 왜 굳이 LiAlD<sub>4</sub>를 썼을까? D가 정확히 Br이 있던 자리에 들어간 것을 보면, 수소화물이 C-Br 탄소를 직접 공격해 Br을 밀어낸다는 것을 알 수 있다.[15] alkyl halide을 환원하는 다른 방법으로는 (a) 제거 반응 후 수소화, (b) alkyl radical을 거치는 방법이 있다.

(출처: L5 p.24)

슬라이드 p.25(steroid keto-ester의 NaBH<sub>4</sub> vs LiBH<sub>4</sub>)와 p.26(락탐·enone을 가진 화합물의 LiAlH<sub>4</sub> 환원)은 연습 문제 5, 6번으로 옮겼다.

(출처: L5 p.25-26)

### 2-4. Borane (BH<sub>3</sub>): 서열을 거스르는 시약

#### 왜 산은 빠르고 ester는 느릴까

2-0의 서열대로라면 carboxylic acid은 가장 환원하기 어려운 축이다. 그런데 BH<sub>3</sub>는 정반대로 **carboxylic acid을 1차 alcohol로, amide를 amine으로** 빠르게 환원하고, ester와 ketone은 훨씬 느리게 환원한다. 어떻게 이런 일이 가능할까?

비밀은 BH<sub>3</sub>의 성격에 있다. BH<sub>4</sub><sup>-</sup>나 AlH<sub>4</sub><sup>-</sup>는 anion, 즉 친핵적인 수소화물 공여체라서 전자가 부족한(친전자적인) carbonyl을 좋아한다. 반면 BH<sub>3</sub>는 중성이고 B에 빈 p 오비탈이 있는 Lewis 산이다. 그래서 먼저 carbonyl 산소의 전자쌍을 받아들여야 반응이 시작되고, 따라서 전자가 풍부한(Lewis 염기성이 큰) carbonyl을 선호한다. amide와 carboxylate는 Lewis 염기성이 크고, ester와 ketone은 작다. L1에서 BH<sub>3</sub>가 전자가 풍부한 alkene π 결합과 반응했던 것과 같은 논리다. (→ [L1](L01_Electrophilic_Addition_to_Alkenes_Part1.md) alkene electrophilic addition 문서의 수소붕소화 참고)

참고로 BH<sub>3</sub>는 기체라서 실제로는 BH<sub>3</sub>·Et<sub>2</sub>O나 BH<sub>3</sub>·Me<sub>2</sub>S 착물 형태로 쓴다.

- `사이클로뷰테인 위의 CO2H/CO2Me --[BH3]--> CH2OH/CO2Me` (산만 환원)
- `4-옥소-4-페닐뷰탄산 PhCOCH2CH2CO2H --[BH3]--> PhCOCH2CH2CH2OH` (ketone 유지)
- `N,N-다이메틸피발아마이드 (CH3)3CCONMe2 --[BH3, THF]--> (CH3)3CCH2NMe2 (79%)`
- `메틸 1-벤질-5-옥소피롤리딘-3-카복실레이트 --[BH3, THF]--> 메틸 1-벤질피롤리딘-3-카복실레이트` (락탐 C=O → CH<sub>2</sub>, ester 유지)

같은 기질 MeO<sub>2</sub>C-CH<sub>2</sub>CH(CH<sub>3</sub>)CH<sub>2</sub>-CO<sub>2</sub>H에 LiBH<sub>4</sub>를 쓰면 ester가 환원되고(2-2), BH<sub>3</sub>를 쓰면 산이 환원된다. 즉 두 시약은 서로 거울처럼 상보적인 화학선택성을 가진다.

(출처: L5 p.27)

#### amide 환원 메커니즘

N,N-dimethylpivalamide(79%)를 예로 단계를 따라가 보자.

1. amide carbonyl O의 비공유 전자쌍이 BH<sub>3</sub>의 빈 p 오비탈로 들어가 Lewis 산-염기 착물을 만든다. 이때 N의 비공유 전자쌍이 공명으로 밀어 주어 C=N<sup>+</sup> 성격이 생긴다.
2. 붙어 있는 B-H의 수소화물이 분자 내에서 carbonyl 탄소로 옮겨 간다. 그 결과 같은 탄소에 O-BH<sub>2</sub>와 NMe<sub>2</sub>가 붙은 tetrahedral intermediate가 생긴다.
3. tetrahedral intermediate가 무너진다. N의 비공유 전자쌍이 C=N<sup>+</sup>를 만들며 O-BH<sub>2</sub>를 밀어내 iminium 이온이 된다.
4. 또 다른 BH<sub>3</sub>의 수소화물이 iminium 탄소에 붙어 amine-보레인 착물(N-B 결합)이 된다.
5. H<sub>2</sub>O로 퀜치하면 유리 3차 amine RCH<sub>2</sub>NMe<sub>2</sub>가 나온다.

![BH3 amide 환원 1부: O가 BH3에 배위하고 분자 내 수소화물 전달로 tetrahedral intermediate가 생긴다](../../figures/L05/bh3_amide_step1.svg)

*그림: 1-2번 단계. 왼쪽에서 carbonyl O의 비공유 전자쌍(파랑)이 BH<sub>3</sub>의 빈 p 오비탈(빨강 B)로 들어가고, N의 비공유 전자쌍이 C–N 쪽으로 밀어 C=N<sup>+</sup> 성격을 만든다(새 O–B 결합은 초록). 가운데 착물에서는 B–H 결합(파랑)의 수소화물이 C=N<sup>+</sup> 탄소(빨강)로 옮겨 가고, C=N π 전자는 N으로 돌아간다. 그 결과 오른쪽 tetrahedral intermediate(새 C–H는 초록)가 생긴다.*

![BH3 amide 환원 2부: tetrahedral intermediate가 무너져 iminium 이온이 되고 두 번째 수소화물을 받아 amine이 된다](../../figures/L05/bh3_amide_step2.svg)

*그림: 3-5번 단계. 왼쪽에서 N의 비공유 전자쌍(파랑)이 C–N 결합 쪽으로 내려와 C=N<sup>+</sup>를 만들고, 빨간 C–O 결합의 전자는 O로 가서 O–BH<sub>2</sub>가 떨어져 나간다. 가운데에서는 또 하나의 BH<sub>3</sub>의 B–H(파랑)가 iminium 탄소(빨강)에 수소화물을 주고, C=N π 전자는 N을 거쳐 B와 결합해 amine-보레인 착물(초록 N–B)이 된다. 슬라이드는 이 과정을 N 근처에서 고리 모양으로 도는 화살표로 그렸고, 여기서는 C=N 결합에서 B로 가는 화살표 하나로 줄였다. 마지막으로 H<sub>2</sub>O 퀜치로 3차 amine이 나온다.*

3번 단계가 핵심이다. ester라면 tetrahedral intermediate에서 OR이 떨어져 나가지만, amide는 O(붕소에 붙어 좋은 leaving group이 된)가 떨어지고 N이 남는다. 그래서 alcohol이 아니라 amine이 된다.[16]

(출처: L5 p.28)

### 2-5. DIBAL-H: ester를 aldehyde에서 멈추기

ester를 LiAlH<sub>4</sub>로 환원하면 중간에 aldehyde가 생기지만, aldehyde는 ester보다 반응성이 크니 곧바로 alcohol까지 가 버린다. 그럼 aldehyde에서 멈추게 할 방법은 없을까? DIBAL-H(diisobutylaluminium hydride, i-Bu<sub>2</sub>AlH)가 답이다. DIBAL은 alane이며, Al-H-Al 다리 결합을 가진 bridged dimer로 존재한다.

`RCO2Et --[DIBAL, hexane, -70 °C; H3O+]--> RCHO (88%, R = n-C11H23)`

1. Lewis 산성 Al이 ester carbonyl O에 배위하고, Al-H의 수소화물이 carbonyl 탄소로 전달된다.
2. tetrahedral intermediate R-CH(OEt)-O-Al(i-Bu)<sub>2</sub>가 생긴다. 이 intermediate는 -70 °C에서 안정해서 무너지지 않는다. 무너지지 않으니 aldehyde가 생기지 않고, 따라서 두 번째 수소화물을 받을 대상도 없다.
3. 반응이 끝난 뒤 H<sub>3</sub>O<sup>+</sup>로 처리하면 intermediate가 가수분해되어 그제야 aldehyde가 풀려난다.

![DIBAL-H가 ester 산소에 배위한 뒤 수소화물을 전달해 저온에서 안정한 tetrahedral intermediate를 만들고, 산 처리로 aldehyde가 나오는 과정](../../figures/L05/dibal_ester.svg)

*그림: 왼쪽은 Al이 carbonyl O에 배위한 착물이다(O<sup>+</sup>–Al<sup>-</sup>). Al–H 결합(파랑)의 수소화물이 carbonyl 탄소(빨강)로 옮겨 가고, C=O π 전자는 O로 간다. 가운데 tetrahedral intermediate(새 C–H는 초록)는 −70 °C에서 무너지지 않는다. H<sub>3</sub>O<sup>+</sup> 처리 후에야 aldehyde가 나온다.*

즉 aldehyde를 "수소화물이 다 사라진 뒤에야 꺼내는" 전략이다. 저온이 필수인 이유도 여기에 있다. 슬라이드의 질문 "ester를 aldehyde로 바꾸는 다른 방법은?"은 연습 문제 7번으로 옮겼다.

(출처: L5 p.29)

## 3. 촉매 수소화 (Catalytic hydrogenation, H<sub>2</sub>/Metal)

> 개념 문서: [catalytic hydrogenation](../../wiki/반응/촉매%20수소화.md), [Pd/C](../../wiki/시약/Pd-C.md), [PtO2](../../wiki/시약/PtO2.md), [Rosenmund reduction](../../wiki/반응/로젠문트%20환원.md), [hydrogenolysis](../../wiki/반응/수소화분해.md), [benzyl ether protecting group](../../wiki/시약/벤질%20에터%20보호기.md), [reductive amination](../../wiki/반응/환원성%20아미노화.md)

### 3-1. alkene의 수소화

#### 무극성 H<sub>2</sub>가 어떻게 이중결합을 환원하나

금속 수소화물은 극성인 C=O, C=N에는 잘 듣지만 무극성 C=C에는 거의 반응하지 않는다. 그럼 alkene은 어떻게 환원할까? H<sub>2</sub>와 금속 촉매를 쓴다. H<sub>2</sub>는 그 자체로는 무극성이라 반응성이 없지만, 금속 촉매와 함께라면 C=C, C=N, 삼중결합 등을 환원한다.

`4-(4-하이드록시페닐)뷰트-3-ene-2-one --[H2, Pd/C]--> 4-(4-하이드록시페닐)뷰탄-2-온`

이 예에서 C=C만 환원되고 ketone은 남는다는 점을 보자.[17] 금속 수소화물과는 정반대의 선택성이다.

자주 쓰는 촉매는 둘이다. 하나는 Pd/C(팔라듐-탄소, 보통 질량비 5% 또는 10%)로, 녹지 않으므로 여과로 회수해 재사용할 수 있다. 다른 하나는 PtO<sub>2</sub>(Adams catalyst)인데, 실제로 일하는 것은 산화백금이 아니라 수소화 중에 생기는 Pt 금속이다.

(출처: L5 p.30)

#### 왜 syn 첨가인가

수소화는 금속 표면에서 일어난다. 그 모습을 그려 보면 입체화학이 저절로 따라 나온다.

1. H<sub>2</sub>가 촉매 표면에 흡착된다.
2. alkene이 한쪽 면을 표면에 대고 촉매에 배위한다.
3. 표면의 H 두 개가 같은 면에서 차례로 탄소에 옮겨 가고, 알케인이 표면에서 떨어져 나간다.

H가 모두 표면 쪽, 즉 같은 면에서 오니 **syn 첨가**다. 그래서 1,2-dimethylcyclohexene을 수소화하면 cis 생성물이 우세하다.

`1,2-다이메틸사이클로헥센 --[H2, PtO2, AcOH]--> cis-1,2-다이메틸사이클로헥산 (82%) + trans (18%)`

그런데 syn 첨가라면서 왜 trans가 18%나 나올까? 촉매 표면에서 이중결합이 자리를 옮기는(이성질화) 일이 일어나고, 옮겨진 alkene이 수소화되면 trans가 생길 수 있기 때문이라고 설명한다.[18]

방향족 고리도 수소화될 수 있지만, 고리의 안정성 때문에 조건이 세다.
- `에틸 벤조에이트 PhCO2Et --[H2, Ni, 50 °C, 100 atm]--> 에틸 사이클로헥산카복실레이트`
- `페닐아세트산 PhCH2CO2H --[H2, PtO2, AcOH, 25 °C]--> 사이클로헥실아세트산`

(출처: L5 p.31)

### 3-1a. 응용: BASF (-)-멘톨 공정

촉매 수소화가 산업에서 어떻게 쓰이는지 보여 주는 예다.

- `제라니알 (E) --[H2, CO, Rh(CO)2acac, (S,S)-Chiraphos]--> (+)-시트로넬랄`
- `네랄 (Z) --[H2, CO, Rh(CO)2acac, (R,R)-Chiraphos]--> (+)-시트로넬랄`
- `(+)-시트로넬랄 --[Al cat.]--> (-)-아이소풀레골 --[H2, Ni cat.]--> (-)-멘톨`

첫 단계는 비대칭 asymmetric hydrogenation으로, 분자에 있는 세 곳(공액 C=C, 고립된 C=C, CHO) 중 aldehyde와 공액된 C=C만 환원하면서 새 입체중심을 한쪽 거울상으로 만든다. 여기서 재미있는 점은 E 이성질체(제라니알)와 Z 이성질체(네랄)가 같은 (+)-시트로넬랄을 주려면 서로 반대 거울상의 키랄 리간드를 써야 한다는 것이다. 이중결합의 기하가 뒤집혀 있으니 같은 생성물을 얻으려면 촉매의 손잡이도 뒤집어야 하는 셈이다. 마지막 단계는 isopropenyl group의 C=C를 수소화하는 평범한 수소화다.[19]

(출처: L5 p.32)

### 3-2. 다른 작용기의 수소화

#### 무엇이 먼저 수소화되나

여러 작용기가 있을 때 어느 것이 먼저 수소화될까? 슬라이드는 쉬운 것부터 어려운 것까지 이렇게 줄 세운다.

1. RCOCl → RCHO
2. ArNO<sub>2</sub> → ArNH<sub>2</sub>
3. RC≡CR → cis-RCH=CHR
4. R<sub>2</sub>C=NR → R<sub>2</sub>CH-NHR
5. RCH=CHR → RCH<sub>2</sub>CH<sub>2</sub>R
6. RX-CH<sub>2</sub>Ph → RXH + PhCH<sub>3</sub> (X = O, NH; benzyl group 제거)
7. RCN → RCH<sub>2</sub>NH<sub>2</sub>
8. benzene 고리 → cyclohexane 고리

6번은 benzyl protecting group을 떼는 반응으로, protecting group 전략에서 아주 중요하다. (→ [L12](L12_Protecting_Groups.md) protecting group 문서의 Bn, Cbz 참고)

#### acid chloride: Rosenmund reduction

acid chloride이 가장 쉽다는 점을 이용하면, carboxylic acid → acid chloride → aldehyde라는 경로가 생긴다.

`2-나프토일 클로라이드 --[H2, Pd/BaSO4, quinoline]--> 2-나프트알데하이드 (74-81%)`

여기서는 C-Cl 결합만 환원되고, 생긴 aldehyde와 naphthalene 고리는 환원되지 않는다. BaSO<sub>4</sub>는 촉매 담체이고, 퀴놀린은 첨가제다.[20]

#### nitro group과 imine

- `ArNO2 --[H2, Pt 또는 Pd, EtOH (+HOAc)]--> ArNH2` (보통 ~100%)
- imine의 수소화는 곧 환원성 아미노화다. `1-(4-메톡시페닐)프로판-2-one + 메틸 5-(2-아미노-1-하이드록시에틸)-2-하이드록시벤조에이트 --[H+ (이민 형성)]--> 이민 --[H2, Pd/C]--> 2차 아민`. 1-3에서 NaBH<sub>3</sub>CN이 하던 역할을 H<sub>2</sub>/Pd-C가 맡은 것이다.

(출처: L5 p.33)

### 요약

슬라이드의 요약은 네 줄이다. (1) amine의 합성, (2) 환원성 아미노화, (3) 금속 수소화물 환원(일반 시약과 특수 시약 Borane, DIBAL-H), (4) 촉매 수소화.

(출처: L5 p.34)

## 흔한 오해

- **"NH<sub>3</sub>를 RX와 반응시키면 1차 amine이 생긴다"고 생각하기 쉽지만 사실은** 생성 amine이 더 좋은 nucleophile라 2차·3차 amine과 4차 염이 섞인다. NH<sub>3</sub> 2 eq에서는 1차와 2차가 거의 반반이다(p.6). 깔끔한 1차 amine은 azide, nitrile, amide 환원, 환원성 아미노화로 만든다.
- **"amide를 LiAlH<sub>4</sub>로 환원하면 alcohol이 된다"고 생각하기 쉽지만 사실은** C=O가 CH<sub>2</sub>가 되어 **amine**이 된다. alcohol 두 개가 나오는 것은 ester다.
- **"nitrile 환원은 원래 탄소 수의 amine을 준다"고 생각하기 쉽지만 사실은** RX에 CN을 붙이는 순간 탄소가 하나 늘어나므로 RCH<sub>2</sub>X에서 RCH<sub>2</sub>CH<sub>2</sub>NH<sub>2</sub>가 된다.
- **"NaBH<sub>4</sub>로도 환원성 아미노화가 된다"고 생각하기 쉽지만 사실은** NaBH<sub>4</sub>는 imine이 생기기 전에 carbonyl을 alcohol로 먼저 환원해 버린다. NaBH<sub>3</sub>CN은 carbonyl에 느리고 iminium에 빠르며 약산성에서 안정하다.
- **"Eschweiler–Clarke로 N-methyl amine(monomethyl)을 만든다"고 생각하기 쉽지만 사실은** 1차 amine이 N,N-**다이**methyl까지 간다. 대신 4차 염으로는 가지 않는다.
- **"BH<sub>3</sub>도 LiBH<sub>4</sub>처럼 ester를 환원한다"고 생각하기 쉽지만 사실은** 정반대다. LiBH<sub>4</sub>는 ester를(산 유지), BH<sub>3</sub>는 산과 amide를(ester 유지) 환원한다. BH<sub>3</sub>는 Lewis 산이라 Lewis 염기성이 큰 carbonyl을 좋아한다.
- **"NaBH<sub>4</sub>의 용매로는 MeOH가 표준"이라고 생각하기 쉽지만 사실은** MeOH가 NaBH<sub>4</sub>와 빠르게 반응해 H<sub>2</sub>로 날아가므로, 슬라이드는 EtOH를 더 좋은 용매로 꼽는다.
- **"DIBAL-H는 언제나 ester를 aldehyde로 멈춘다"고 생각하기 쉽지만 사실은** 저온(-70 °C)에서 tetrahedral intermediate가 안정할 때만 그렇다. 온도가 오르면 intermediate가 무너져 aldehyde가 생기고, 그것이 다시 환원되어 alcohol이 될 수 있다.
- **"syn 첨가니까 cis만 100% 나온다"고 생각하기 쉽지만 사실은** 1,2-dimethylcyclohexene에서 trans가 18% 나온다(p.31).
- **"Adams 촉매의 활성종은 PtO<sub>2</sub>"라고 생각하기 쉽지만 사실은** 수소화 중에 생기는 Pt 금속이 실제 촉매다.
- **"H<sub>2</sub>/Pd-C는 alkene만 환원하니 안전하다"고 생각하기 쉽지만 사실은** benzyl ether·benzyl amine·Cbz 같은 benzyl group이 함께 끊어질 수 있다(p.33).

## 반응 정리표

| 반응 | 시약/조건 | 생성물 | regioselectivity | 입체화학 | 비고 |
|---|---|---|---|---|---|
| amine 직접 alkylation | NH<sub>3</sub>(대과량) + RX | RNH<sub>2</sub> (+ overalkylation 생성물) | X가 붙은 탄소에 N | S<sub>N</sub>2 (반전) | NH<sub>3</sub> 2 eq이면 1차/2차 혼합 (p.6) |
| azide 경로 | 1) NaN<sub>3</sub>, EtOH 2) LiAlH<sub>4</sub>; H<sub>2</sub>O (또는 H<sub>2</sub>/Pd, PPh<sub>3</sub>) | RNH<sub>2</sub> | X 탄소 | S<sub>N</sub>2 (반전) | 1차 amine만 |
| nitrile 경로 | 1) NaCN 2) LiAlH<sub>4</sub>; H<sub>2</sub>O (또는 H<sub>2</sub>/Pd) | RCH<sub>2</sub>CH<sub>2</sub>NH<sub>2</sub> | - | S<sub>N</sub>2 (반전) | 탄소 1개 증가 |
| amide 환원 | LiAlH<sub>4</sub> 또는 BH<sub>3</sub>; H<sub>2</sub>O | RCH<sub>2</sub>NR'<sub>2</sub> | C=O → CH<sub>2</sub> | - | 1차/2차/3차 amine 모두 |
| 환원성 아미노화 | amine + R<sub>2</sub>C=O, NaBH<sub>3</sub>CN (pH 3-4, EtOH) 또는 H<sub>2</sub>/Ni, H<sub>2</sub>/Pd-C | 한 단계 더 치환된 amine | carbonyl 탄소에 N | 슬라이드에 지정 없음 | imine/iminium 경유 |
| Eschweiler–Clarke | HCHO, HCOOH | RN(CH<sub>3</sub>)<sub>2</sub> | - | - | HCOOH = 수소화물원, -CO<sub>2</sub>; 4차 염 없음 |
| NaBH<sub>4</sub> 환원 | NaBH<sub>4</sub>, EtOH/MeOH | aldehyde → 1차, ketone → 2차 alcohol | aldehyde > ketone (약 400배) | 4-t-Bu-cyclohexanone → 주로 trans (각주 12) | 다이글라임에선 aldehyde만 |
| LiBH<sub>4</sub> 환원 | LiBH<sub>4</sub>, EtOH | ester/락톤 → alcohol | 산, amide, nitrile 유지 | - | NaBH<sub>4</sub>보다 강함 |
| LiAlH<sub>4</sub> 환원 | 1) LiAlH<sub>4</sub>, Et<sub>2</sub>O/THF 2) H<sub>2</sub>O/H<sub>2</sub>SO<sub>4</sub> | 산/ester/aldehyde → 1차, ketone → 2차 alcohol; amide → amine | 거의 비선택적 | - | 물과 격렬 반응 |
| alkyl halide 환원 | LiAlH<sub>4</sub> (또는 LiAlD<sub>4</sub>), ether | R-H (R-D) | 할로젠 자리 | - | D 표지로 위치 확인 |
| 보레인 환원 | BH<sub>3</sub>·THF/Et<sub>2</sub>O/Me<sub>2</sub>S | 산 → 1차 alcohol, amide → amine | ester, ketone 유지 | - | LiBH<sub>4</sub>와 상보적 |
| DIBAL-H | DIBAL, hexane, -70 °C; H<sub>3</sub>O<sup>+</sup> | ester → aldehyde | - | - | 저온에서 tetrahedral intermediate 안정 |
| alkene 수소화 | H<sub>2</sub>, Pd/C 또는 PtO<sub>2</sub> | 알케인 | - | syn 첨가 (cis 우세) | ketone 유지 |
| 방향족 수소화 | H<sub>2</sub>, Ni (50 °C, 100 atm) 또는 PtO<sub>2</sub>/AcOH | cyclohexane 고리 | - | - | 가장 어려운 수소화 |
| 비대칭 수소화 | H<sub>2</sub>, CO, Rh(CO)<sub>2</sub>acac, Chiraphos | (+)-시트로넬랄 | 공액 C=C만 | E는 (S,S), Z는 (R,R) 리간드 | BASF 멘톨 공정 |
| Rosenmund reduction | H<sub>2</sub>, Pd/BaSO<sub>4</sub>, quinoline | RCHO | C-Cl만 | - | aldehyde, 방향족 유지 |
| nitro 환원 | H<sub>2</sub>, Pt 또는 Pd, EtOH (+HOAc) | ArNH<sub>2</sub> | - | - | ~100% |
| benzyl 제거 | H<sub>2</sub>, Pd/C | ROH/RNH<sub>2</sub> + PhCH<sub>3</sub> | benzyl C-X 결합 | - | protecting group 제거 |

## 연습 문제

1. (p.13) N-methyl-2-phenylethanamine PhCH<sub>2</sub>CH<sub>2</sub>NHCH<sub>3</sub>를 어떻게 합성하겠는가? 두 가지 이상의 경로를 제시하라.
2. (p.14) 거미 독소 전구체 합성에서 fragment 1의 aldehyde(...CH<sub>2</sub>CHO)와 fragment 2의 1차 amine(H<sub>2</sub>N-CH<sub>2</sub>...)을 NaCNBH<sub>3</sub>(20 °C, 2 h)로 연결하여 2차 amine(48%)을 얻었다. 같은 생성물을 주는 다른 amine/aldehyde 조합을 제안하라. 또 이 연결에 H<sub>2</sub>, Pd/C를 쓰기 어려운 이유는?
3. (p.16) 벤라팍신 합성에서 1-[사이아노(4-methoxyphenyl)methyl]cyclohexanol을 H<sub>2</sub>, 5% Rh/Al<sub>2</sub>O<sub>3</sub>로 처리한 생성물(빈 상자 1)과, 이를 HCHO/HCOOH, reflux로 처리한 최종 생성물(빈 상자 2)을 쓰라. H<sub>2</sub>/Pd-C/HCHO 한 단계 경로에서는 어떤 반응들이 연속으로 일어나는가?
4. (p.17) 환원성 아미노화에 NaBH<sub>4</sub> 대신 NaBH<sub>3</sub>CN을 쓰는 이유는?
5. (p.25) 3β-acetoxy-steroid-20-온(C3에 acetate ester, C17 측쇄에 methyl ketone C(=O)CH<sub>3</sub>)을 (a) NaBH<sub>4</sub>, (b) LiBH<sub>4</sub>로 처리한 생성물은?
6. (p.26) methoxy 아릴기, 고리형 ether, 고리형 enone(C=C-C=O), N-methyl 락탐을 가진 다고리 화합물을 LiAlH<sub>4</sub>, THF(70%)로 처리할 때 각 작용기는 어떻게 되는가?
7. (p.29) ethyl 2-(퓨란-2-일)propanoate를 2-(퓨란-2-일)propanal(항생제 모넨신 합성 intermediate)로 바꾸는 방법을 DIBAL 외에 제시하라.
8. (p.22, p.27) MeO<sub>2</sub>C-CH<sub>2</sub>CH(CH<sub>3</sub>)CH<sub>2</sub>-CO<sub>2</sub>H를 (a) LiBH<sub>4</sub>/EtOH, (b) BH<sub>3</sub>·THF로 각각 처리한 생성물과 그 이유는?

## 정답 및 해설

1. **경로 A (amide 환원, p.9)**: `PhCH2COOH --[1. SOCl2; 2. CH3NH2]--> PhCH2CONHCH3 --[1. LiAlH4; 2. H2O]--> PhCH2CH2NHCH3`. amide C=O가 CH<sub>2</sub>가 된다.
   **경로 B (환원성 아미노화, p.10-12)**: `PhCH2CHO + CH3NH2 --[NaBH3CN, 약산성]--> PhCH2CH2NHCH3`. 새 C-N 결합의 탄소 쪽(CH<sub>2</sub>)이 aldehyde에서 온다.
   **경로 C**: 2-phenylethylamine(p.7의 azide 경로)을 포밀화(예: HCOOEt)해 N-포밀 amide PhCH<sub>2</sub>CH<sub>2</sub>NHCHO로 만든 뒤 LiAlH<sub>4</sub>로 환원하면 NHCH<sub>3</sub>가 된다.
   함정: PhCH<sub>2</sub>CH<sub>2</sub>Br + CH<sub>3</sub>NH<sub>2</sub> 직접 alkylation은 overalkylation 위험(p.6)이 있고, Eschweiler–Clarke는 N,N-dimethyl까지 가므로 monomethyl 합성에 맞지 않는다(p.15).

2. 생성물의 2차 amine N 양쪽이 모두 CH<sub>2</sub>이므로, 어느 쪽 C-N 결합이든 환원성 아미노화로 만들 수 있다. 대안은 **fragment 1 쪽을 1차 amine**(원래 CHO 탄소가 CH<sub>2</sub>NH<sub>2</sub>가 된 ...CH<sub>2</sub>CH<sub>2</sub>NH<sub>2</sub>)으로, **fragment 2 쪽을 aldehyde**(원래 H<sub>2</sub>N-CH<sub>2</sub>-가 OHC-로 바뀐 OHC-CH<sub>2</sub>CH<sub>2</sub>-N(Cbz)...)로 바꾸어 NaCNBH<sub>3</sub>로 연결하는 것이다. 전체 탄소 수는 그대로다.
   H<sub>2</sub>/Pd-C가 어려운 이유: 분자에 OBn(benzyl ether)과 Cbz(benzyloxycarbonyl)가 많아 수소화 조건에서 benzyl group이 떨어져 나갈 수 있다(p.33 "deprotection of benzyl group"). NaCNBH<sub>3</sub>는 이들을 건드리지 않는다.

3. 빈 상자 1: nitrile이 1차 amine으로 수소화된 **1-[2-아미노-1-(4-methoxyphenyl)ethyl]cyclohexanol** (4-MeOC<sub>6</sub>H<sub>4</sub>-CH(CH<sub>2</sub>NH<sub>2</sub>)-C(OH)(cyclohexane 고리)), 57%.
   빈 상자 2: Eschweiler–Clarke로 NH<sub>2</sub>가 N(CH<sub>3</sub>)<sub>2</sub>가 된 **벤라팍신** 1-[2-(dimethyl아미노)-1-(4-methoxyphenyl)ethyl]cyclohexanol (HCl 염, 80%).
   한 단계 경로: (i) C≡N 수소화로 CH<sub>2</sub>NH<sub>2</sub>, (ii) HCHO와 imine 형성 후 H<sub>2</sub>/Pd 환원으로 NHCH<sub>3</sub>, (iii) 다시 HCHO와 iminium 형성 후 환원으로 N(CH<sub>3</sub>)<sub>2</sub>. HCHO 2.2 eq는 methyl group 두 개분이다. (출처: L5 p.15-16)

4. NaBH<sub>4</sub>는 aldehyde/ketone을 빠르게 환원하므로(p.17 표) imine이 생기기 전에 carbonyl을 alcohol로 바꿔 버린다. 또 imine 형성에 필요한 산성 조건에서 분해되어 H<sub>2</sub>를 낸다. NaBH<sub>3</sub>CN은 aldehyde/ketone을 느리게만 환원하고(p.17 표의 "느림") imine은 환원하며, pH > 3 수용액에서도 안정하다(p.17). 그래서 carbonyl, amine, 환원제를 한 용기에 넣어도 된다. 보충: 전자를 끄는 CN기 때문에 B-H의 수소화물 공여력이 약해지고, 더 친전자적인 protonation iminium만 빠르게 환원된다. (보충 근거: Clayden p.234)

5. (a) NaBH<sub>4</sub>: ketone만 환원된다. C20이 2차 alcohol CH(OH)CH<sub>3</sub>가 되고 **3β-acetate는 남는다**. NaBH<sub>4</sub>는 ester를 매우 느리게만 환원한다(p.17, p.21).
   (b) LiBH<sub>4</sub>: ketone과 ester가 모두 환원된다(p.22). C20 alcohol과 함께 acetate가 환원되어 **C3의 3β-OH가 드러난 diol**이 되고, acetyl 부분은 ethanol로 떨어져 나간다. 끊어지는 것은 acyl C-O 결합이므로 C3의 β 배향은 유지된다. C20에 새 입체중심이 생기지만 슬라이드에 배향이 지정되어 있지 않다.

6. LiAlH<sub>4</sub>는 강한 환원제다(p.17). **락탐(고리형 amide)의 C=O는 CH<sub>2</sub>가 되어** N-methyl 고리형 3차 amine이 된다. **enone의 C=O는 2차 alcohol**(allyl alcohol)이 된다. 보충: LiAlH<sub>4</sub>는 enone을 주로 1,2-환원하므로 C=C는 남는다(1,4-첨가와의 비교는 → L11 conjugate addition 문서 참고). 아릴 methyl ether와 고리형 ether는 변하지 않는다. 보충: 3-methoxy, 4,5-에폭시 고리, N-methyl, 6-OH, 7,8-이중결합의 조합은 모르핀 계열(morphinan, 코데인 유사) 골격에 해당한다. 새 C-OH 입체중심의 배향은 슬라이드에 제시되지 않았다.

7. **alcohol 경유(p.17 "via alcohol")**: `에스터 --[1. LiAlH4 (또는 LiBH4); 2. H2O]--> 2-(퓨란-2-일)프로판-1-ol --[온화한 산화: Swern, PCC, Dess–Martin 등]--> 2-(퓨란-2-일)프로판알`. 1차 alcohol을 carboxylic acid까지 과산화하지 않는 산화제를 골라야 한다(→ [L6](L06_Oxidation_and_Alkene_Synthesis.md) 산화 문서 참고).
   **acid chloride 경유(p.17, p.33)**: ester 가수분해 → carboxylic acid → SOCl<sub>2</sub> → acid chloride → H<sub>2</sub>, Pd/BaSO<sub>4</sub>, Rosenmund → aldehyde.

8. (a) LiBH<sub>4</sub>: ester만 환원되어 **HOCH<sub>2</sub>CH<sub>2</sub>CH(CH<sub>3</sub>)CH<sub>2</sub>CO<sub>2</sub>H** (5-hydroxy-3-methylpentanoic acid). LiBH<sub>4</sub>는 산 존재하에 ester를 선택 환원한다(p.22). 산은 deprotonate되어 반응성 최하위인 carboxylate(p.18)가 된다.
   (b) BH<sub>3</sub>: 산만 환원되어 **MeO<sub>2</sub>CCH<sub>2</sub>CH(CH<sub>3</sub>)CH<sub>2</sub>CH<sub>2</sub>OH** (methyl 5-hydroxy-3-methylpentanoate). BH<sub>3</sub>는 Lewis 산이라 전자가 풍부한 carboxylic acid/amide를 선택 환원하고, Lewis 염기성이 약한 ester는 느리다(p.27-28).

## 각주

[1] 슬라이드는 May, *Molecules That Amaze Us*(CRC Press)를 인용해 "세로토닌이 도파민과 함께 인류 진화와 과학·예술·문화 발전의 원동력이었다고까지 주장할 수 있다"는 다소 과감한 문장을 소개한다. 경쟁심과 남보다 앞서려는 욕구에도 관여할 수 있다고 한다. (출처: L5 p.2)

[2] amide N의 비공유 전자쌍은 C=O와 공명하며 비편재화되어 있어서, 양성자나 electrophile에 내줄 여유가 적다. amide가 protonation될 때도 N이 아니라 O에서 일어난다.

[3] 슬라이드에는 아제티딘이 "Azeditine"으로, 모폴린이 "Morph oline"으로 표기되어 있는데 오타다. 바른 이름은 azetidine, morpholine이다. (출처: L5 p.4)

[4] alkyl group의 유발 효과(전자 공여)로 N이 더 전자가 풍부해지기 때문이다. 2차 amine부터는 입체 장애도 커지므로 3차, 4차로 갈수록 생성량이 줄어 p.6처럼 "미량"이 된다.

[5] PPh<sub>3</sub>를 쓰는 환원은 Staudinger 환원이라 부른다. azide와 PPh<sub>3</sub>가 N<sub>2</sub>를 내놓고 iminophosphorane(R-N=PPh<sub>3</sub>)을 만든 뒤, 물로 가수분해해야 RNH<sub>2</sub>와 Ph<sub>3</sub>P=O가 된다. 슬라이드에는 이 가수분해 단계가 생략되어 있다.

[6] iminium에 α-H가 있으면 H를 잃고 enamine이 될 수도 있다. 환원성 아미노화 조건에서는 환원제가 iminium을 바로 잡아챈다.

[7] 슬라이드는 NaBH<sub>3</sub>CN reaction 조건을 pH 3-4로 적고 있다. 다만 흔히 인용되는 Borch 조건은 pH 6-7 부근이며, pH 3-4처럼 더 산성이면 NaBH<sub>3</sub>CN이 aldehyde·ketone도 상당히 환원하기 시작한다고 알려져 있다. 시험에서는 슬라이드 값을 따르되, "약산성에서 iminium을 선택적으로 환원한다"는 원리를 기억하는 것이 핵심이다.

[8] 슬라이드는 "enolate chemistry"라고 적지만, 엄밀히는 nitrile α-H를 뗀 nitrile 안정화 탄소 anion(enolate 유사체)이다. anion 전하가 C≡N 쪽으로 비편재화되어 안정해지는 원리는 enolate와 같다.

[9] Burgos et al. 2008 (US Patent). (출처: L5 p.16)

[10] 이 때문에 LiAlH<sub>4</sub>로 carboxylic acid을 환원할 때는 첫 수소화물 1당량이 H<sub>2</sub> 발생에 소모된다는 점을 감안해 시약을 넉넉히 쓴다.

[11] p.20-21의 교재 발췌는 H. C. Brown 연구진의 논문들을 인용한다. Brown은 붕소 화합물(보레인 등)을 유기합성에 도입한 공로로 1979년 노벨 화학상을 받았다.

[12] 슬라이드에는 생성물의 입체화학이 그려져 있지 않다. 표준 교재에 따르면 작은 수소화물이 주로 축 axial에서 공격하므로 OH가 에쿼토리얼인 trans-4-tert-butylcyclohexanol이 주생성물이다.

[13] 이 설명은 슬라이드가 아닌 일반 교재 수준의 보충이다. (보충 근거: Clayden p.530–531) 슬라이드 p.21은 "cation에 따라 반응성 차이가 크다"는 관찰만 제시한다.

[14] 엄밀히 LiAlH<sub>4</sub>는 공기 중에서 저절로 불붙는 전형적인 pyrophoric 물질이라기보다는 물과 반응해 가연성 H<sub>2</sub>를 내는 water-reactive 물질로 분류되는 경우가 많다. 슬라이드의 불꽃 표지는 인화성 위험을 뜻한다. 어느 쪽이든 물·습기를 철저히 피해야 한다.

[15] 1차·2차 halide의 LiAlH<sub>4</sub> 환원은 주로 S<sub>N</sub>2형 수소화물 치환으로 설명된다. 슬라이드가 말한 "alkyl radical 경유" 방법의 대표 시약은 Bu<sub>3</sub>SnH/AIBN이다.

[16] carboxylic acid의 경우에는 먼저 산의 O-H가 BH<sub>3</sub>와 반응해 H<sub>2</sub>를 내고 acyl옥시보레인(RCO<sub>2</sub>BR<sub>2</sub>)이 되며, 이것이 환원되어 최종적으로 1차 alcohol이 된다. 보충: 이 붕소 ester(triacylborate)가 보통 ester보다 훨씬 빨리 환원되는 이유는, carbonyl 옆 산소의 비공유 전자쌍이 C=O뿐 아니라 B의 빈 p 오비탈과도 나눠 쓰여 carbonyl을 덜 안정화하기 때문이다. acid anhydride이 ester보다 반응성이 큰 것과 같은 원리다. 반대로 acid chloride·ester는 전자가 부족한 carbonyl이라 BH<sub>3</sub>가 거의 건드리지 않거나 느리게만 환원한다. (보충 근거: Clayden p.531–532)

[17] 생성물 4-(4-hydroxyphenyl)butane-2-one은 라즈베리 향의 주성분으로 알려진 "라즈베리 ketone"이다.

[18] 이 이성질화 설명은 표준 교재의 보충 내용이다. (보충 근거: Clayden p.536) 슬라이드는 82:18이라는 결과와 "cis가 우세하다"는 점만 제시한다.

[19] (+)-시트로넬랄은 (R)-시트로넬랄이다. Al catalyst 단계는 분자 내 carbonyl-엔(carbonyl-ene) 고리화로, aldehyde와 삼치환 alkene이 반응해 고리를 닫는다.

[20] 보충: 퀴놀린은 Pd 촉매를 일부러 부분 피독시켜(활성을 낮춰) 생성된 aldehyde가 더 환원되지 않게 하는 역할을 한다. 담체를 탄소 대신 BaSO<sub>4</sub>(또는 CaCO<sub>3</sub>)로 쓰는 것도 같은 목적이다. 생성물이 촉매 표면에서 빨리 떨어져 나가게 해 과잉 환원을 줄인다. 6강의 Lindlar catalyst(Pd/CaCO<sub>3</sub>/Pb)도 같은 발상이다. (보충 근거: Clayden p.537–538)
