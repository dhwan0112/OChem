# L11. 짝지음 첨가 (Conjugate Addition)

> **통독본:** 2026-10-18에 L11 전 범위의 원자·전자 이동, 선택성의 이유, 중간체와 후처리, 문제 적용 설명을 보강했다. 교재 보충은 출처를 구별하며 상세 개념은 연결된 위키에서 함께 읽는다. 뼈대 노트: [L11 뼈대](../L11_Conjugate_Addition.md) · [위키 대문](../../wiki/위키%20대문.md)

> **관련 위키 문서** ([위키 대문](../../wiki/위키%20대문.md))
> - 반응: [SN2 reaction](../../wiki/반응/SN2%20반응.md), [conjugate addition](../../wiki/반응/공액%20첨가.md), [Michael reaction](../../wiki/반응/마이클%20반응.md), [addition-elimination](../../wiki/반응/첨가-제거%20반응.md), [nucleophilic aromatic substitution](../../wiki/반응/친핵성%20방향족%20치환.md), [nucleophilic acyl substitution](../../wiki/반응/친핵성%20아실%20치환.md), [reductive amination](../../wiki/반응/환원성%20아미노화.md)
> - 시약: [LDA](../../wiki/시약/LDA.md), [LiAlH4](../../wiki/시약/LiAlH4.md), [NaBH4](../../wiki/시약/NaBH4.md), [Pd/C](../../wiki/시약/Pd-C.md), [Grignard reagent](../../wiki/시약/그리냐르%20시약.md), [alkoxide base](../../wiki/시약/알콕사이드%20염기.md), [organocuprate](../../wiki/시약/유기구리%20시약.md), [pyrrolidine](../../wiki/시약/피롤리딘.md)
> - 개념: [1,2-addition vs 1,4-addition](../../wiki/개념/1,2-첨가와%201,4-첨가.md), [E1cB elimination](../../wiki/개념/E1cB%20제거.md), [Meisenheimer complex](../../wiki/개념/마이젠하이머%20착물.md), [aromaticity](../../wiki/개념/방향족성.md), [kinetic vs thermodynamic enolate](../../wiki/개념/속도론적%20엔올레이트와%20열역학적%20엔올레이트.md), [kinetic vs thermodynamic control](../../wiki/개념/속도론적%20지배와%20열역학적%20지배.md), [enamine](../../wiki/개념/엔아민.md), [enol and enolate](../../wiki/개념/엔올과%20엔올레이트.md), [iminium ion](../../wiki/개념/이미늄%20이온.md), [imine](../../wiki/개념/이민.md), [electrophile and nucleophile](../../wiki/개념/친전자체와%20친핵체.md), [hard and soft acids and bases (HSAB)](../../wiki/개념/하드-소프트%20산염기.md)

> [Test 2 반응 판정·검산 순서](../../wiki/개념/Test%202%20반응%20판정과%20답안%20검산.md)로 각 단원의 질문을 연결할 수 있다.

## 읽는 순서와 이번 강의의 핵심 질문

L11은 같은 반응식을 여러 이름으로 외우는 강의가 아니라, **전자 부족한 conjugated 계에 무엇이 어디로 붙고, 그 뒤 어떤 작용기가 회복되는가를** 따라가는 강의다. 1–2절에서 기본 전자 이동을 읽고, 3절에서 공격 위치를 고른 뒤, 4–6절에서 donor·acceptor를 만드는 방법을 비교한다. 마지막 7절에서는 leaving group 때문에 첨가가 치환으로 이어지는 경우를 본다. (출처: L11 p.2–24)

| 읽을 부분 | 읽고 나서 설명할 질문 |
|---|---|
| 1절: conjugated system | 왜 보통 alkene과 달리 $\beta$-탄소가 electrophile인가? |
| 2절: amine·organocuprate | 새 결합을 만드는 원자는 무엇이며 전하와 H는 어떻게 정리되는가? |
| 3절: 1,2/1,4 | 작용기·nucleophile·조건을 바꾸면 무엇이 달라지는가? |
| 4절: enolate Michael | 어떤 두 탄소가 연결되며 왜 1,5-dicarbonyl인가? |
| 5절: enamine | N이 전자를 밀어 주는데 왜 새 결합은 C에서 생기는가? |
| 6절: iminium catalysis | donor 활성화와 acceptor 활성화는 어떻게 다른가? |
| 7절: addition–elimination·SNAr | Nu가 붙은 뒤 왜 H를 받지 않고 leaving group이 나가는가? |
| 8절: 적용 순서 | 공격 원자·중간체·후처리를 나누어 답안을 검산할 수 있는가? |

아래의 그림과 반응식은 각 절의 설명에 맞춰 읽는다. 굽은 화살표는 전자쌍, 직선 화살표는 반응 단계, 공명 화살표는 같은 종의 기여 구조 사이 관계를 나타낸다. (출처: L11 p.3–24)

## 개요

conjugate addition(1,4-첨가)는 $\alpha,\beta$-unsaturated carbonyl 화합물의 C=C 이중결합에 nucleophile이 붙는 반응이다.
L1~L2에서 본 alkene은 전자가 풍부해서 electrophile(E+)을 받아들이는 쪽이었다.
<!-- comment: [완료 2026-10-17] 이미지 추가 바람 직후 내용에 알맞게 — enone_resonance.svg 삽입 -->
C=C가 carbonyl 같은 electron-withdrawing group(EWG)과 conjugated system을 이루면, 전자 밀도가 낮아진 alkene의 탄소가 **electrophile로** 반응할 수 있다.

![methyl vinyl ketone의 공명 구조: carbonyl 탄소와 beta 탄소의 electrophilic 성격](../../figures/L11/enone_resonance.svg)

그림: methyl vinyl ketone의 공명 구조. C=O와 C=C의 $\pi$ 전자가 이동하면 양전하가 carbonyl 탄소뿐 아니라 $\beta$-탄소에도 놓일 수 있다. 이 때문에 conjugated alkene의 $\beta$-탄소가 nucleophile의 공격을 받는다. (출처: L11 p.3)

이 강의는 이 "뒤집힌 alkene"이 amine, thiol, cyanide ion, 유기구리 시약, enolate, enamine 같은 nucleophile과 어떻게 반응하는지 다루고,
nucleophile이 carbonyl 탄소를 공격할지(1,2) $\beta$-탄소를 공격할지(1,4)를 무엇이 정하는지 정리한다.
뒤쪽에서는 L7(enolate alkylation), L8(aldol), L10(enol과 enamine)에서 만든 nucleophile들을 다시 꺼내 1,5-dicarbonyl 화합물을 만들고,
키랄 amine 촉매가 만드는 iminium 이온과 nucleophilic aromatic substitution(SNAr)까지 이어간다. SNAr는 conjugate addition 뒤에 $\beta$ -leaving group이 떨어지는 반응으로 보면 이해가 쉽다.

---

## 1. 공액계(conjugated system)란 무엇이고, 왜 $\beta$-탄소가 양전하를 띠나?

> 개념 문서: [conjugate addition](../../wiki/반응/공액%20첨가.md)

 $\alpha,\beta$-unsaturated carbonyl 화합물은 C=C가 C=O와 바로 붙어있는 분자다.
carbonyl 탄소 옆이 $\alpha$-탄소, 그 다음이 $\beta$-탄소다. 슬라이드에 나온 대표 예시는 다음과 같다.

| 종류 | 체계명 | 관용명 | 구조 |
|---|---|---|---|
| $\alpha,\beta$-unsaturated aldehyde(enal) | propenal | acrolein | CH2=CH-CHO |
| $\alpha,\beta$-unsaturated ketone(enone) | but-3-en-2-one | methyl vinyl ketone(MVK) | CH2=CH-CO-CH3 |
| $\alpha,\beta$-unsaturated 산 | propenoic acid | acrylic acid | CH2=CH-COOH |
| $\alpha,\beta$-unsaturated ester | ethyl propenoate | ethyl acrylate | CH2=CH-CO2Et |

이중결합이 carbonyl에서 한 칸 더 떨어진 $\beta,\gamma$-unsaturated ketone(예: CH3CO-CH2-CH=CH2)은 공액계가 아니라서 이 강의의 반응성을 보이지 않는다.

그렇다면 왜 $\beta$-탄소가 nucleophile을 끌어당길까? 공명 구조를 그려보면 답이 나온다.
중성 구조(A)에서 C=O의 $\pi$ 전자를 산소로 밀면 carbonyl 탄소에 양전하가 생기고(B),
이어서 C=C의 $\pi$ 전자를 옮기면 **$\beta$-탄소에 양전하가** 생긴다(C).
즉 $\beta$-탄소와 carbonyl 탄소 둘 다 $\delta^{+}$ 를 띤다.

그래서 일반 alkene은 E+를 공격하지만, 공액계 alkene은 Nu-에게 공격받는다.

![methyl vinyl ketone의 세 공명 구조 A, B, C: beta-탄소에 양전하가 생기는 과정](../../figures/L11/enone_resonance.svg)

그림: methyl vinyl ketone으로 그린 공명 구조 A ↔ B ↔ C. A의 주황 화살표는 C=O의 $\pi$ 전자가 산소로 가는 것을, B의 화살표는 C=C의 $\pi$ 전자가 옆의 C–C 자리로 옮겨 가는 것을 나타낸다. 파란 O⁻는 음전하를 받은 산소, 빨간 +는 양전하가 놓이는 탄소다. B에서는 carbonyl 탄소, C에서는 $\beta$-탄소가 양전하를 띤다. 그래서 nucleophile이 노릴 수 있는 $\delta^{+}$ 자리가 두 곳이 된다.

이 분극은 분광학에서도 보인다.
- IR: 단순 ketone C=O는 1715 cm-1인데 짝지음 C=O는 1675 cm-1다. 공명으로 C=O가 단일결합 성격을 일부 띠어 결합이 약해졌다는 뜻이다(비교: C-O 단일결합 1050 cm-1).
- 13C NMR: $\beta$-탄소는 약 140 ppm에서 나타나 일반 C=C(약 120 ppm)보다 deshielded이다. $\beta$-탄소의 전자 밀도가 낮다는 증거다.

보충: IR에서는 C=C 흡수도 함께 변한다. 고립된 C=C는 약 1650 cm-1에서 약하게 흡수하지만, 짝지음 계에서는 약 1615 cm-1로 내려가고 세기가 커진다. 진동수가 내려간 것은 C=C도 약해졌다는 뜻이고, 세기가 커진 것은 C=O와 짝지으면서 C=C의 쌍극자 모멘트가 커졌다는 뜻이다. 또 13C NMR에서 $\alpha$-탄소는 약 120 ppm 근처에 머문다. 전자가 빠지는 자리는 $\alpha$ 가 아니라 $\beta$ 라는 점이 숫자로도 보인다. (보충 근거: Clayden p.501)

보충: 공명 구조는 "어디가 $\delta^{+}$ 인가"를 보여 줄 뿐이고, 실제 결합이 생기는 단계는 nucleophile의 HOMO에서 받개의 LUMO로 전자가 들어가는 과정이다. acrolein(propenal)의 LUMO는 $\beta$-탄소에서 계수가 가장 크고, carbonyl 탄소에서 두 번째로 크다. 그래서 $\beta$-탄소가 1순위 공격 자리이고, carbonyl 탄소도 경쟁 자리로 남는다. 3절의 1,2/1,4 경쟁은 이 "두 번째로 큰 계수"에서 나온다. (보충 근거: Clayden p.502)

(출처: L11 p.3)

#### 공명식에서 읽어야 할 것과 실제 반응에서 바뀌는 것

공명식을 그릴 때에는 원자나 H를 움직이지 않고 전자만 옮긴다. 따라서 A, B, C는 차례로 생성되는 세 intermediate가 아니라 **같은 분자를 나타내는 기여 구조** 다. C에 $\beta$-탄소의 양전하를 그릴 수 있다는 것은 그 자리가 electrophilic하다는 뜻이지, 용액에 자유로운 $\beta$ -carbocation이 먼저 생긴다는 뜻은 아니다. 실제 nucleophilic addition에서는 Nu와 탄소 사이에 새 결합을 만들면서 conjugated 계의 전자를 O 쪽으로 밀어 octet을 유지한다. (출처: L11 p.3–5)

번호는 두 체계를 구분해서 읽는다. 분자 이름에서 carbonyl 탄소가 C1이면 이웃 탄소가 C2( $\alpha$ ), 다음이 C3( $\beta$ )다. 반면 **1,4-addition의 번호는 O–C–C–C를 세는 번호이므로** O가 1, carbonyl 탄소가 2, $\alpha$-탄소가 3, $\beta$-탄소가 4다. 따라서 “1,4라서 분자 이름의 C4에 붙는다”는 뜻이 아니다. 두 체계에서 실제 공격 원자는 똑같은 $\beta$-탄소다. (출처: L11 p.3,9)

## 2. conjugate addition(Michael addition)의 일반형

> 개념 문서: [conjugate addition](../../wiki/반응/공액%20첨가.md), [keto-enol tautomerization](../../wiki/반응/케토-엔올%20토토머화.md), [organocuprate](../../wiki/시약/유기구리%20시약.md), [Grignard reagent](../../wiki/시약/그리냐르%20시약.md)

conjugate addition은 **Michael addition** 이라고도 부른다. 일반식은 다음과 같다.

$$
\mathrm{CH_2{=}CH{-}CO{-}R(OR)} \xrightarrow[(2)\ \mathrm{HA}]{(1)\ \mathrm{Nu^-}\ (\text{또는}\ \mathrm{H{-}Nu})} \mathrm{Nu{-}CH_2{-}CH_2{-}CO{-}R(OR)}
$$

결과적으로 Nu와 H가 C=C를 가로질러 붙는다. Nu는 $\beta$-탄소에, H는 $\alpha$-탄소에 붙는다. 이 반응에는 세 가지 조건이 있다.
- alkene이 electrophile로 작용한다.
- Nu와 H가 C=C에 첨가된다.
- alkene 옆에 짝지은 EWG(CHO, COR, COOR 등)가 반드시 있어야 한다.

슬라이드가 든 nucleophile은 CN-, RNH2, RSH, R2CuLi, enolate 등이다.

예시 두 개:

$$
\mathrm{(CH_3)_2C{=}CH{-}CO{-}CH_3} \quad \xrightarrow[25\thinspace{}^\circ\mathrm{C},\ 5\ \text{h}]{\mathrm{PhSH}} \mathrm{(CH_3)_2C(SPh){-}CH_2{-}CO{-}CH_3}
$$

mesityl oxide → 4-methyl-4-(phenylthio)pentan-2-one.

(수율 94%)

 thiol의 황은 $\beta$-탄소에 붙는다.

$$
\mathrm{Ph{-}CH{=}CH{-}CO{-}Ph} \quad \xrightarrow[\mathrm{EtOH},\ \mathrm{HOAc}]{\mathrm{CN^-}} \mathrm{Ph{-}CH(CN){-}CH_2{-}CO{-}Ph}
$$

(수율 95%)

 CN이 $\beta$-탄소(Ph가 붙은 탄소)에 붙는다.

![mesityl oxide + PhSH → 4-methyl-4-(phenylthio)pentan-2-one](../../figures/L11/mesityl_oxide_phsh.svg)

그림: S(파랑)가 $\beta$-탄소(빨강)에 붙는다.

![chalcone + CN− → beta-cyano ketone](../../figures/L11/chalcone_cyanide.svg)

그림: CN(파랑)이 $\beta$-탄소(빨강)에 붙는다.

(출처: L11 p.4)

#### 출발물에서 생성물까지 결합을 따라 읽기

받개를 먼저 $\mathrm{C(=O)}{-}C_{\alpha}{-}C_{\beta}$ 순서로 표시하고, Nu에서 실제로 결합할 원자를 고른다. thiophenol에서는 S, cyanide에서는 C, methylamine에서는 N이 그 원자다. 이 원자를 $\beta$-탄소에 붙인 뒤 원래 $\alpha{-}\beta$ 의 이중결합을 단일결합으로 바꾸고, 최종 carbonyl을 회복하면 기본 생성물의 골격을 얻는다. 원래 $\beta$-탄소에 있던 methyl·phenyl 같은 치환기는 그대로 남는다. (출처: L11 p.4–5,9)

중성 nucleophile과 음이온 nucleophile의 첫 intermediate는 전하가 다르다. $\mathrm{CN^-}$ 같은 음이온이 1,4로 붙으면 주개의 음전하가 소비되고 받개 쪽 enolate에 음전하가 남는다. 반면 중성 amine은 비공유 전자쌍을 새 결합에 쓰면서 N이 양전하를 띠고, 받개 O에는 음전하가 생겨 zwitterion이 된다. 따라서 중성 amine의 첨가에 전하 표시를 모두 생략하면 뒤의 proton transfer가 왜 필요한지 설명할 수 없다. (출처: L11 p.5,7,13)

### 2.1 amine의 첨가: 질소 nucleophile은 어떻게 $\beta$-탄소에 붙나?

1차 또는 2차 amine은 $\alpha,\beta$-unsaturated carbonyl 화합물에 첨가해서 **$\beta$ -amino carbonyl 화합물을** 준다.

$$
\mathrm{(CH_3)_2C{=}CH{-}CO{-}CH_3} \xrightarrow{\ \mathrm{MeNH_2},\ \mathrm{H_2O}\ \mathstrut} \mathrm{(CH_3)_2C(NHMe){-}CH_2{-}CO{-}CH_3}
$$

(수율 75%)

![MeNH2가 mesityl oxide의 beta-탄소를 공격해 쌍극성 이온 enolate가 되는 1단계](../../figures/L11/amine_addition.svg)

그림: 아래 1단계를 그린 것이다. 화살표는 셋이다. (1) $MeNH_2$ 질소(파랑, nucleophile)의 비공유 전자쌍이 $\delta^{+}$ 인 $\beta$-탄소(빨간 C=C 쪽)를 공격한다. (2) C=C의 $\pi$ 전자가 carbonyl 쪽 C–C 자리로 밀려 간다. (3) C=O의 $\pi$ 전자가 O에 비공유 전자쌍으로 남아 O⁻(파랑)가 된다. 초록 결합은 새로 생긴 C–N 결합이다. 생성물은 N⁺와 O⁻를 함께 가진 쌍극성 이온이며, 이어서 양성자 이동과 tautomerization이 일어난다(2–4단계).

메커니즘은 네 단계로 나뉜다.
1. **친핵성 공격** : MeNH2 질소의 비공유 전자쌍이 $\delta^{+}$ 인 $\beta$-탄소(electrophile)를 공격한다. 새 C-N 결합이 생기고, C=C의 $\pi$ 전자는 C=O 쪽으로 밀려 산소 anion이 된다. 이렇게 한 분자 안에 ammonium 부분(N⁺)과 enolate 부분(O⁻)이 함께 있는 zwitterion이 생긴다.
2. **양성자 이동** : 암모늄 N-H의 양성자가 산소로 옮겨간다. 중성 amine과 enol이 된다.
3. **tautomerization** : enol이 keto형으로 바뀐다. $\alpha$-탄소에 H가 붙고 C=O가 다시 생긴다.
4. 그 결과 $\beta$ -amino ketone이 남는다.

![amine 첨가 후 zwitterion에서 enol로의 proton transfer](../../figures/L11/amine_proton_transfer.svg)

그림: 2단계. N⁺–H와 O⁻를 가진 zwitterion이 proton transfer를 거쳐 중성 amine과 enol로 바뀐다. 초록 O–H는 이동한 proton의 도착 위치이며, 평형 화살표는 강의의 가역 단계를 따른다. 이 그림은 순변화를 나타내며 직접적인 분자 내 N→O proton 이동을 뜻하지 않는다. (출처: L11 p.5)

![enol에서 beta-amino ketone으로의 tautomerization](../../figures/L11/amine_tautomerization.svg)

그림: 3–4단계. enol의 C=C가 C–C로 바뀌고 C=O가 회복되어 $\beta$ -amino ketone이 된다. 초록 H는 $\alpha$-탄소에 새로 붙은 H이다. 이는 tautomerization의 순변화이며 O–H가 한 번에 C–H로 이동하는 elementary step을 그린 것이 아니다. (출처: L11 p.5)

슬라이드에는 각 단계가 가역(⇌)으로 그려져 있다.[^1]

보충: amine은 중성 nucleophile이므로 따로 산을 넣지 않아도 amine 자신(N–H)이 enolate에 줄 양성자를 공급한다. 이 절의 carbonyl 받개에 대한 conjugate addition은 enolate(또는 enol)를 거치므로, 이 양성자를 공급할 곳이 필요하다. 그래서 conjugate addition은 보통 물이나 alcohol 같은 양성자성 용매에서 하고, alcohol을 nucleophile로 쓸 때는 촉매량의 염기만 있으면 된다(enolate가 물에서 양성자를 받으며 OH-를 다시 내놓는다). 또 1차 amine 생성물은 아직 N–H가 남아 친핵성을 띠므로, 받개가 충분하면 **두 번째 conjugate addition이** 일어날 수 있다(예: MeNH2 + acrylonitrile 2분자). (보충 근거: Clayden p.503, p.510)

(출처: L11 p.5)

#### amine의 전하와 H를 세어 보는 법

첫 공격 전 $\mathrm{MeNH_2}$ 의 N은 C–N 하나와 N–H 둘, 총 세 결합과 전자쌍 하나를 가진다. 새 C–N 결합을 만들면 네 결합이 되어 $\mathrm{N^+}$ 가 된다. 이후 N–H에서 proton을 잃을 때 그 결합의 전자는 N에 남으므로, N은 다시 세 결합과 전자쌍을 가진 중성 amine으로 돌아온다. **전자쌍 화살표는 H⁺의 이동 경로가 아니라 결합 전자의 이동 경로** 라는 점을 이 단계에서 확인할 수 있다. (출처: L11 p.5)

최종 생성물에서는 출발 enone의 $\alpha$-탄소가 CH에서 CH₂로 바뀌고, $\beta$-탄소에는 NHMe가 붙는다. mesityl oxide의 $\beta$-탄소에는 원래 methyl 둘이 있으므로, 그 탄소에 H를 하나 더 붙이는 것이 아니다. “Nu와 H가 C=C를 가로질러 붙는다”는 말을 각 탄소의 원래 치환기와 원자가에 맞춰 적용해야 한다. (출처: L11 p.4–5)

전하의 합도 확인할 수 있다. 중성 amine과 중성 enone에서 출발했다면, 첨가 직후 N⁺와 O⁻를 가진 zwitterion의 총전하는 0이다. 이후 N이 proton을 잃고 O가 proton을 받으면 두 전하가 모두 사라진다. N–H 결합을 끊을 때 전자쌍은 N에 남아야 하므로, proton transfer를 그리면서 H와 전자쌍을 함께 이동시키지 않는다. (출처: L11 p.5; 전하 검산)

### 2.2 유기구리 시약의 첨가: 왜 구리는 $\beta$-탄소를 고르나?

**lithium dialkylcuprate** R2CuLi는 conjugate addition에 쓰는 대표적인 탄소 nucleophile이다. 실제 구조는 tetramer 등으로 더 복잡하다. 그런데 탄소에서 반응하는 Grignard reagent는 carbonyl을 직접 공격하는데, 구리 시약은 왜 $\beta$-탄소로 갈까?

강의는 carbon–metal 결합의 분극 차이로 설명한다. 강의에 제시된 전기음성도는 Cu가 1.9, Mg가 1.3이다. Cu가 Mg보다 전기음성도가 높으므로 C–Cu 결합은 C–Mg 결합보다 탄소 쪽으로 덜 분극된다. 이 비교는 organocopper의 탄소가 Grignard reagent의 탄소보다 carbanion 성격이 작다는 설명으로 이어진다. 즉 유기구리 시약은 Grignard 시약보다 **soft** nucleophile이다. soft nucleophile이 soft electrophilic site( $\beta$-탄소)를 고르는 경향은 3절에서 자세히 다룬다.

**만드는 법** :

$$
\mathrm{CuBr} + 2\ \mathrm{R{-}Li} \xrightarrow[-78\thinspace{}^\circ\mathrm{C}]{\ \mathrm{Et_2O}\ \mathstrut} \mathrm{R_2CuLi} + \mathrm{LiBr}
$$

이렇게 만든 cuprate는 불안정해서 만든 즉시 써야 한다.

![lithium dialkylcuprate의 화학양론적 제조](../../figures/L11/cuprate_preparation.svg)

그림: $2\,\mathrm{RLi}$ 와 $\mathrm{CuBr}$ 에서 $\mathrm{R_2CuLi}$ 를 만드는 제조식이다. 파랑은 R–metal 결합이며, $\mathrm{Li^+}$ 는 cuprate anion의 counterion이다. 그림은 조성과 결합 관계를 나타낸 도식이고 실제 aggregate의 구조나 기하를 확정한 그림은 아니다. 저온에서 만든 뒤 즉시 사용한다는 조건까지 함께 읽는다. (출처: L11 p.6)

여기서 **미리 제조하는 $\mathrm{R_2CuLi}$와** 아래 촉매계의 **계 안에서 생기는 organocopper를** 구분한다. 촉매계의 carbon donor는 $\mathrm{MeMgBr}$ 이고, $\mathrm{CuCl}$ 은 소량으로 재순환한다. 강의의 `"Me–Cu"`는 methyl 전달을 따라가기 위한 단순화된 표기이므로, 이를 그대로 $\mathrm{Me_2CuLi}$ 의 제조식이나 실제 활성종의 완전한 구조로 읽으면 안 된다. (출처: L11 p.6–7)

**구리 촉매를 써서 반응계 in situ 만드는 법** :

$$
\text{isophorone} \xrightarrow[\mathrm{CuCl}\ (0.01\ \text{eq}),\ \mathrm{Et_2O}]{\mathrm{MeMgBr}} \text{3,3,5,5-tetramethylcyclohexanone}
$$

(수율 83%)

![isophorone + MeMgBr/CuCl → 3,3,5,5-tetramethylcyclohexanone](../../figures/L11/isophorone_cuprate.svg)

그림: Cu 촉매로 methyl이 $\beta$-탄소(빨강)에 1,4-첨가한다.

![MeMgBr의 transmetallation과 CuI 재순환](../../figures/L11/cuprate_transmetallation.svg)

그림: 위쪽은 Me–MgBr에서 Me–Cu로 methyl이 넘어가는 transmetallation, 아래쪽은 enone에 methyl을 전달한 뒤 Cu(I)가 재순환하는 흐름이다. 파랑은 methyl–metal 결합, 초록은 CuCl의 투입·재생이다. 이 화살표들은 단계 사이의 물질 흐름이며 전자쌍을 나타내는 굽은 화살표가 아니다. $\mathrm{MgBrCl}$ 과 magnesium enolate는 강의 p.7의 표기를 따른다. (출처: L11 p.7)

**촉매량이라는 말은 methyl까지 촉매량이라는 뜻이 아니다.** carbon donor인 $\mathrm{MeMgBr}$ 의 methyl은 생성물에 들어가지만 Cu(I)는 다시 다음 methyl을 전달하는 데 쓰인다. 따라서 출발 시약, Cu 촉매, 물 후처리를 서로 다른 역할로 구분해서 읽는다. (출처: L11 p.6–7)

이 반응의 메커니즘은 다음과 같다.
1. **금속 transmetallation** : MeMgBr + CuCl → "Me-Cu" + MgBrCl. methyl group이 마그네슘에서 구리로 넘어간다.
2. **conjugate addition** : "Me-Cu"의 methyl이 enone의 $\beta$-탄소(C3)를 공격한다. 마그네슘 enolate(O- MgBr+)가 생기고 CuCl이 다시 나온다.
3. **재순환** : 다시 나온 Cu(I)가 1단계로 돌아간다. 그래서 구리는 촉매량(0.01 eq)만 있으면 된다.
4. **H2O 처리** : enolate가 protonate되고 tautomerize해서 ketone이 된다. 새 methyl이 붙은 C3는 gem-dimethyl 탄소가 된다.

!["Me–Cu"의 methyl이 isophorone의 beta-탄소에 conjugate addition해 마그네슘 enolate가 되는 단계](../../figures/L11/cuprate_addition.svg)

그림: 위 2단계(conjugate addition)를 그린 것이다. 금속 교환으로 생긴 "Me–Cu"의 C–Cu 결합(파랑, nucleophile)이 isophorone의 $\beta$-탄소(C3)를 공격하고, 빨간 C=C의 $\pi$ 전자는 C1–C2 자리로, C=O의 $\pi$ 전자는 산소로 간다. 그 결과 C1=C2 enolate(O⁻ MgBr⁺)가 생기고 CuCl이 다시 나온다. 초록 결합이 새로 붙은 methyl이며, C3는 gem-dimethyl 탄소가 된다.

#### 물 처리와 carbonyl 회복을 따로 보기

![magnesium enolate의 물 후처리와 enol 형성](../../figures/L11/cuprate_enolate_protonation.svg)

그림: 첨가 직후에는 C=O가 아니라 C1=C2와 O⁻를 가진 enolate가 있다. 물 처리 뒤 O가 proton을 받은 enol로 이어지는 순변화를 분리했다. 파란 O⁻와 초록 O–H를 비교하며, $\mathrm{MgBr^+}$ 는 enolate의 counterion이다. 용매·염의 모든 산염기 교환은 생략한 도식이다. (출처: L11 p.7,9)

![enol에서 ketone으로의 회복과 alpha 수소 도입](../../figures/L11/cuprate_keto_recovery.svg)

그림: enol의 C1=C2가 단일결합이 되고 C1=O가 회복된다. 초록 C–H는 $\alpha$-탄소(C2)에 도입된 H, 아래쪽 초록 C–C는 앞 단계에서 $\beta$-탄소(C3)에 만들어진 methyl 결합이다. O–H가 직접 한 번에 C–H로 이동한다는 elementary step이 아니라 tautomerization의 순변화다. (출처: L11 p.7,9)

생성물을 검산할 때는 세 곳을 본다. **C1에서는 C=O가 돌아오고, C2는 CH₂가 되며, C3에는 새 methyl이 남는다.** isophorone의 C3에는 원래 methyl이 있으므로 methyl이 하나 더 붙으면 gem-dimethyl 탄소가 된다. 최종 생성물에서 새 C–C 결합을 carbonyl 탄소에 그리면 1,4 생성물이 아니라 1,2 경로를 그린 셈이다. (출처: L11 p.6–7)

CuCl이 **없으면** MeMgBr이 C=O에 직접 첨가(1,2-첨가)한다.

![같은 isophorone에서 CuCl 유무에 따른 12와 14 첨가의 비교](../../figures/L11/cuprate_12_vs_14_isophorone.svg)

그림: 위는 CuCl 없이 MeMgBr이 carbonyl 탄소를 공격하는 1,2 경로의 후처리 생성물이고, 아래는 CuCl 촉매로 $\beta$-탄소에 methyl이 붙는 1,4 경로다. 위에서는 C=C가 남고 C=O가 alcohol로 바뀌며, 아래에서는 C=C가 사라지고 C=O가 회복된다. 초록은 새 methyl 결합과 후처리로 도입된 O–H 또는 C–H다. 입체배치를 지정하지 않은 연결 구조 비교이며, 83% 수율은 강의의 Cu 촉매 1,4 반응에 해당한다. (출처: L11 p.6–7)

(출처: L11 p.6, p.7)

### 2.3 연습: 유기구리 시약으로 무엇을 만들 수 있나?

슬라이드 p.8은 분자 간(intermolecular) conjugate addition만 써서 네 화합물을 만드는 방법을 묻는다. 거꾸로 생각하는 요령은 이렇다. 생성물 ketone에서 **carbonyl로부터 $\beta$ 위치에 있는 치환기 하나를** R2CuLi에서 온 R로 보고 떼어낸다. 그리고 $\alpha$ -C와 $\beta$ -C 사이에 C=C를 다시 넣으면 출발 enone이 나온다. 문제는 "연습 문제"에 옮겼다.

(출처: L11 p.8)

#### cuprate 역합성은 새 결합을 먼저 찾는다

예를 들어 2-heptanone을 만들려면 carbonyl 탄소를 C2로 두고 사슬의 C3를 $\alpha$ , C4를 $\beta$ 로 표시한다. C4–C5 결합을 새 결합으로 보고 끊으면, 받개는 methyl vinyl ketone이고 전달할 조각은 propyl이다. 이때 이중결합을 되살릴 자리는 **최종 생성물의 C3–C4** , 즉 carbonyl에 인접한 $\alpha{-}\beta$ 결합이다. 끊은 C4–C5 자체를 이중결합으로 바꾸는 것이 아니다. (출처: L11 p.8; 풀이 적용)

이 방법으로 고리형 ketone도 읽는다. 목표물의 $\beta$-탄소에 methyl 둘이 있으면 하나는 출발 enone의 치환기, 다른 하나는 cuprate에서 전달된 methyl로 나눌 수 있다. 반면 $\gamma$-탄소의 치환기를 cuprate에서 넣겠다고 계획하면 공격 위치가 맞지 않는다. 마지막에는 **받개의 탄소 수 + 전달되는 R 한 조각의 탄소 수 = 생성물 탄소 수를** 확인한다. $\mathrm{R_2CuLi}$ 에 R이 둘 적혀 있어도 한 번의 conjugate addition에 R 둘을 같은 탄소에 동시에 붙이지 않는다. (출처: L11 p.6–8)

## 3. 1,2-첨가와 1,4-첨가: nucleophile은 어디를 칠까?

> 개념 문서: [1,2-addition vs 1,4-addition](../../wiki/개념/1,2-첨가와%201,4-첨가.md), [NaBH4](../../wiki/시약/NaBH4.md), [addition-elimination](../../wiki/반응/첨가-제거%20반응.md), [hard and soft acids and bases (HSAB)](../../wiki/개념/하드-소프트%20산염기.md), [Grignard reagent](../../wiki/시약/그리냐르%20시약.md), [organocuprate](../../wiki/시약/유기구리%20시약.md), [kinetic vs thermodynamic control](../../wiki/개념/속도론적%20지배와%20열역학적%20지배.md)

1절에서 봤듯이 $\delta^{+}$ 자리는 두 곳이다. 그래서 nucleophile은 carbonyl 탄소를 직접 공격( **단순 첨가, 1,2-첨가** )하거나 $\beta$-탄소를 공격( **conjugate addition, 1,4-첨가** )할 수 있다.
- 1,2-첨가: protonate하면 C=C가 남은 allyl alcohol 형태(C=C-C(OH)Nu)가 생긴다.
- 1,4-첨가: protonate하면 먼저 **enol형** (Nu-C-C=C-OH)이 생기고, 이것이 tautomerize해서 더 안정한 **keto형** (Nu-C-CH-C=O)이 된다. "1,4"라는 이름은 O=C-C=C의 O를 1번으로 셀 때 Nu와 H가 1번(O)과 4번( $\beta$ -C)에 붙은 것처럼 보이는 데서 왔다.

(출처: L11 p.9)

그러면 어느 쪽으로 갈지는 무엇이 정할까? 슬라이드는 세 가지를 꼽는다. (1) $\alpha,\beta$-unsaturated 계의 작용기, (2) nucleophile, (3) 반응 조건이다.

#### 1,2와 1,4를 생성물에서 구분하기

| 확인할 자리 | carbonyl에 1,2-addition | $\beta$-탄소에 1,4-addition |
|---|---|---|
| 새 Nu–C 결합 | 원래 carbonyl 탄소 | 원래 $\beta$-탄소 |
| 첨가 직후 | alkoxide | enolate |
| ketone 받개의 후처리 생성물 | allylic alcohol | $\beta$-치환 ketone |
| 원래 C=C | 남음 | 단일결합이 됨 |
| 원래 C=O | C–OH가 됨 | 후처리 후 회복됨 |

이 비교표의 alcohol/ketone 비교는 이 강의의 hydride 및 탄소 nucleophile이 enal·enone에 첨가하는 예에 적용한다. amine 같은 중성 nucleophile의 직접 첨가 중간체에는 N의 전하와 뒤따르는 반응도 따로 고려한다. acyl chloride처럼 leaving group이 있는 carbonyl에서는 1,2 공격 뒤 제거가 이어져 amide 같은 acyl 치환 생성물이 나오므로, “1,2면 최종적으로 무조건 alcohol”이라고 적용하지 않는다. 최종 생성물을 정하려면 **첫 공격 위치와 그 뒤 반응을 따로** 읽어야 한다. (출처: L11 p.9–11)

### 3.1 요인 1: $\alpha,\beta$-unsaturated 계의 작용기

carbonyl이 얼마나 반응성이 큰지에 따라 직접 첨가(C=O 공격) 비율이 달라진다. 직접 첨가 비율이 큰 것부터 나열하면 다음과 같다.

**$\alpha,\beta$-unsaturated acyl chloride > enal > enone > $\alpha,\beta$-unsaturated ester > $\alpha,\beta$-unsaturated amide**

공격 위치뿐 아니라 후속 단계까지 비교한다. 화합물 이름은 설명에 두고, 각 반응식은 반응물·화살표·생성물을 한 줄로 연결했다.

#### 1,2: acryloyl chloride의 acyl 치환

$$
\mathrm{CH_2{=}CH{-}COCl}
\xrightarrow{\mathrm{NH_3}}
\mathrm{CH_2{=}CH{-}CONH_2}
$$

acryloyl chloride → acrylamide. C=C는 남고, carbonyl의 Cl이 NH₂로 치환된다.[^2]

![acryloyl chloride + NH3 → acrylamide (1,2)](../../figures/L11/acryloyl_chloride_nh3.svg)

그림: acyl chloride는 C=O(빨강)에서 바로 치환된다.

#### 1,4: methyl acrylate에 ammonia 첨가

$$
\mathrm{CH_2{=}CH{-}CO_2Me}
\xrightarrow{\mathrm{NH_3}}
\mathrm{H_2N{-}CH_2{-}CH_2{-}CO_2Me}
$$

methyl acrylate → methyl 3-aminopropanoate. ester C=O는 남고, C=C에 N과 H가 첨가된다.

![methyl acrylate + NH3 → methyl 3-aminopropanoate (1,4)](../../figures/L11/methyl_acrylate_nh3.svg)

그림: ester에서는 $\beta$-탄소(빨강)로 1,4-첨가한다.

#### 1,2: cinnamaldehyde의 carbonyl 환원

$$
\mathrm{Ph{-}CH{=}CH{-}CHO}
\xrightarrow[\mathrm{EtOH}]{\mathrm{NaBH_4}}
\mathrm{Ph{-}CH{=}CH{-}CH_2OH}
$$

cinnamaldehyde → cinnamyl alcohol(97%). aldehyde C=O가 환원되고 C=C는 남는다.

![cinnamaldehyde → cinnamyl alcohol (1,2)](../../figures/L11/cinnamaldehyde_nabh4.svg)

그림: aldehyde는 C=O(빨강)가 직접 환원된다.

#### 1,4 후 1,2: cyclopentenone의 연속 환원

$$
\text{cyclopentenone}
\xrightarrow[\mathrm{EtOH}]{\mathrm{NaBH_4}}
\text{cyclopentanol}
$$

수율 99%. 먼저 1,4 환원으로 cyclopentanone이 되고, 그 C=O가 다시 1,2 환원된다(→ [L5 환원](L05_Reduction.md)). (출처: L11 p.10)

![cyclopentenone → cyclopentanol (1,4 후 1,2)](../../figures/L11/cyclopentenone_nabh4.svg)

그림: 먼저 1,4로 C=C가, 그다음 C=O가 환원된다.

보충: 이 순서가 "왜" carbonyl의 반응성 순서인지는 L4~L5에서 본 carbonyl 반응성과 같다. ester의 OR, amide의 NR2는 비공유 전자쌍을 C=O로 밀어 넣어 carbonyl 탄소의 $\delta^{+}$ 를 줄인다. 그래서 nucleophile이 C=O로 직접 갈 이유가 약해지고 $\beta$-탄소가 상대적으로 유리해진다. 극단적으로 NaBH4는 ester·amide C=O를 아예 환원하지 못하므로, $\alpha,\beta$-unsaturated ester에는 짝지음 환원만 일어난다. 반대로 enone에서 C=O만 골라 환원하고 싶으면 NaBH4에 CeCl3을 넣는 Luche 환원을 쓴다. (보충 근거: Clayden p.506)

보충: 슬라이드의 세 요인 외에 Clayden은 **$\beta$-탄소의 입체 장애도** 요인으로 꼽는다. $\beta$-탄소가 붐비면 직접(1,2) 첨가 쪽으로, $\beta$-탄소가 드러나 있으면 conjugate addition 쪽으로 기운다. methyl vinyl ketone이나 exo-methylene ketone처럼 $\beta$ 가 CH2인 받개가 가장 반응성 좋은 Michael 받개인 이유다. (보충 근거: Clayden p.510, p.609)

(출처: L11 p.10)

#### 작용기 예시를 비교할 때 고정해야 하는 것

acryloyl chloride와 methyl acrylate는 같은 $\mathrm{CH_2{=}CH{-}CO{-}}$ 부분을 가지지만 carbonyl의 나머지 치환기가 다르다. 전자는 carbonyl이 반응성이 크고 Cl⁻가 떨어질 수 있어 ammonia로 acyl 치환을 한다. 후자는 OR의 전자 주개 효과 때문에 carbonyl 직접 공격의 경쟁이 약해져, 강의 조건에서는 ammonia의 $\beta$ 첨가가 관찰된다. 두 예의 차이는 ammonia 자체가 바뀌어서가 아니다. (출처: L11 p.10)

환원에서는 **한 번의 hydride 전달과 최종 생성물을 구분한다**. cinnamaldehyde의 예는 C=O만 환원되어 C=C가 남는다. cyclopentenone의 예는 1,4 환원으로 ketone이 생긴 뒤 그 C=O가 다시 환원되어 포화 alcohol이 된다. 따라서 최종 cyclopentanol을 보고 “hydride가 한 단계에서 모든 결합을 환원했다”거나, 이 예를 모든 enone의 NaBH₄ 반응에 그대로 적용하면 안 된다. (출처: L11 p.10)

### 3.2 요인 2: nucleophile, Grignard vs 유기구리

같은 2-cyclohexenone에 methyl group을 도입해도 시약에 따라 첨가 위치가 달라진다.

#### 1,2-첨가: Grignard 또는 organolithium

- 시약: CH₃MgBr 또는 CH₃Li, Et₂O; 이어 H₃O⁺ 후처리
- 생성물: **1-methylcyclohex-2-en-1-ol**
- 수율: **95%**

![2-cyclohexenone + MeLi → 1-methylcyclohex-2-en-1-ol (1,2)](../../figures/L11/cyclohexenone_meli.svg)

그림: 단단한 유기금속은 C=O(빨강)에 1,2-첨가한다.

(출처: L11 p.11)

![CH3MgBr의 methyl이 2-cyclohexenone의 carbonyl 탄소를 직접 공격하는 1,2-addition](../../figures/L11/grignard_12_addition.svg)

그림: Grignard 시약의 1,2-addition. C–Mg 결합(파랑)의 전자쌍이 methyl과 함께 carbonyl 탄소로 가고, 빨간 C=O의 $\pi$ 전자는 산소로 간다. 생성물은 C=C가 그대로 남은 magnesium alkoxide(초록이 새 C–C 결합)이고, H₃O⁺ 후처리로 1-methyl-2-cyclohexen-1-ol이 된다. 같은 enone에 R₂CuLi를 쓰면 methyl이 $\beta$-탄소로 간다(→ [organocuprate](../../wiki/시약/유기구리%20시약.md)의 그림). 보충: 슬라이드는 반응식만 보여 주며, 화살표는 표준적인 carbonyl 첨가 메커니즘으로 그렸다. (출처: L11 p.11)

#### 1,4-첨가: organocuprate

- 시약: Me₂CuLi, ether; 이어 H₃O⁺ 후처리
- 생성물: **3-methylcyclohexanone**
- 수율: **97%**

1,2 경로와 달리 methyl은 $\beta$-탄소에 붙는다. 후처리 뒤에는 C=O가 남고 원래 C=C가 단일결합이 된다. (출처: L11 p.11)

왜 이렇게 갈릴까? hard/soft 개념으로 설명한다.
- **hard nucleophile은** hard electrophile인 **carbonyl 탄소와** 반응하는 경향이 있다(1,2-첨가). 전하가 크고 작은 영역에 집중되어 있어 정전기적 인력이 큰 자리를 고른다고 보면 된다.
- **soft nucleophile은** soft electrophile인 **$\beta$-탄소와** 반응하는 경향이 있다(1,4-첨가).

| hard nucleophile | borderline | soft nucleophile |
|---|---|---|
| F-, OH-, RO-, Cl- | N3-, CH-(원문 표기)[^3] | I-, RS-, RSe- |
| H2O, ROH, ROR, RCOR' | RNH2, RR'NH | RSH, RSR', R3P |
| RMgBr, RLi | Br- | alkene, 방향족 고리 |
| | | R2CuLi |

그래서 RMgBr/RLi는 1,2로, R2CuLi와 thiol(RS-, RSH)은 1,4로 간다고 기억하면 된다.

보충: 교재는 이 선택성을 charge control과 orbital control의 상대적인 기여로 설명한다. 음전하가 작은 영역에 집중된 hard nucleophile에서는 양전하가 큰 carbonyl 탄소와의 정전기적 상호작용이 중요하다. 전자구름이 쉽게 분극되는 soft nucleophile에서는 HOMO–LUMO의 겹침이 중요하며, 강의의 conjugated carbonyl에서는 $\beta$-탄소의 큰 LUMO 계수가 1,4 첨가를 설명하는 단서가 된다. 두 효과가 서로 완전히 분리되어 작용한다는 뜻은 아니다. 실제 선택성은 받개의 작용기, 용매, counterion과 가역성까지 함께 고려해야 한다. (보충 근거: Clayden p.507)

(출처: L11 p.12)

#### hard/soft는 선택성을 설명하는 출발점이다

같은 methyl group이라도 $\mathrm{MeMgBr}$ 과 organocuprate에서는 carbon–metal 결합의 성격이 달라진다. Grignard에서 carbonyl 탄소를 공격하면 O⁻를 가진 alkoxide, organocuprate에서 $\beta$-탄소를 공격하면 공액된 enolate가 생긴다. 전자 이동을 그린 뒤 이 두 intermediate가 서로 다른지 확인하면 “탄소 nucleophile은 전부 같은 생성물을 준다”는 혼동을 피할 수 있다. (출처: L11 p.6–7,11–12)

다만 HSAB 표는 모든 조건의 생성물을 단독으로 결정하는 규칙이 아니다. amine은 표의 borderline 칸에 있지만 p.5에서는 분명히 conjugate addition을 한다. cyanide 역시 p.13에서 온도에 따라 두 경로를 보인다. 따라서 답안은 “soft라서 1,4”에서 끝내기보다 **받개의 작용기 → nucleophile의 성격 → 온도·counterion·후처리** 까지 이어서 판단한다. (출처: L11 p.5,10–13)

### 3.3 요인 3: 반응 조건, kinetic vs thermodynamic 생성물

methyl vinyl ketone(MVK)에 cyanide ion을 첨가하는 반응은 온도만 바꿔도 생성물이 달라진다.
cyanohydrin

$$
\mathrm{MVK} \quad \xrightarrow[5\text{–}10\thinspace{}^\circ\mathrm{C}]{\mathrm{NaCN},\ \mathrm{HCN}} \mathrm{(CH_2{=}CH{-}C(OH)(CN){-}CH_3)}
$$

 carbonyl에 직접 첨가한 **1,2 생성물이다**. 이 반응은 가역적이다. 이것이 **kinetic 생성물(kinetic product, P1)이다**.

$$
\mathrm{MVK} \quad \xrightarrow[80\thinspace{}^\circ\mathrm{C}]{\mathrm{NaCN},\ \mathrm{HCN}} \mathrm{NC{-}CH_2CH_2{-}CO{-}CH_3}\ \text{(4-oxopentanenitrile)}
$$

   **1,4 생성물** . 이것이  **thermodynamic 생성물(thermodynamic product, P2)이다**.

![MVK에 대한 cyanide의 1,2- vs 1,4-첨가 (1/2)](../../figures/L11/mvk_cyanide_1.svg)

![MVK에 대한 cyanide의 1,2- vs 1,4-첨가 (2/2)](../../figures/L11/mvk_cyanide_2.svg)

그림: 보충: 저온에서는 빠른 1,2-첨가(cyanohydrin, kinetic product)가, 80 °C에서는 가역적인 1,2-첨가가 되돌아가고 더 안정한 1,4-첨가 생성물(4-oxopentanenitrile, thermodynamic product)이 쌓인다.

![MVK + CN⁻의 1,2-첨가와 1,4-첨가 굽은 화살표](../../figures/L11/mvk_cn_12_vs_14.svg)

그림: 보충: 왼쪽: $CN^-$ (파랑)이 carbonyl C를 직접 공격하고 C=O $\pi$ 전자가 O로 간다(1,2-첨가, 빠르지만 가역). 오른쪽: $CN^-$ 이 $\beta$-탄소(빨강)를 공격하고 C=C $\pi$ 전자가 C–C로, C=O $\pi$ 전자가 O로 밀려 enolate가 된다(1,4-첨가, 더 안정한 생성물).

왜 그럴까? 에너지 도표로 보면 1,2-첨가의 활성화 에너지(EA1, TS1)가 1,4-첨가(EA2, TS2)보다 낮다. 그래서 저온에서는 빨리 생기는 P1이 쌓인다. 그런데 P2가 에너지상 더 낮다. 두 경로 모두 C-C $\sigma$ 결합 하나를 얻지만, 1,2-첨가는 C=O $\pi$ 결합(약 369 kJ/mol)을 잃고 1,4-첨가는 C=C $\pi$ 결합(약 280 kJ/mol)을 잃는다. 즉 1,4는 더 약한 결합을 희생하고 강한 C=O를 보존하니 더 안정하다. 고온에서는 가역적인 1,2-첨가가 풀렸다가 다시 일어나기를 반복하면서 결국 안정한 P2로 모인다.

보충: 그렇다면 1,2가 "왜" 더 빠를까? $\beta$-탄소도 $\delta^{+}$ 를 띠지만 carbonyl 탄소가 더 큰 양전하를 띠므로, 음전하를 띤 CN-는 정전기적으로 carbonyl 탄소에 더 빨리 끌린다. 그리고 결정적인 차이는 **가역성이다**. cyanohydrin 형성은 가역이라 평형 속에 늘 출발 enone이 조금 남아 있고, 이 enone이 가끔 1,4-첨가를 하면 그 생성물은 (사실상) 되돌아오지 않는다. 그 결과 1,4 생성물이 조금씩 쌓이고, enone–cyanohydrin 평형이 이를 보충하느라 cyanohydrin이 점점 소모된다. 실온에서도 원리상 일어나지만 매우 느리고, 80 °C에서는 몇 시간이면 끝난다. 같은 논리로 더 높은 온도(예: 160 °C)를 쓰는 예도 있다. (보충 근거: Clayden p.504–505)

(출처: L11 p.13)

[원본 자료에서 세부 구조·입체배치 확인: L11_Conjugate addition.pdf p.13](../../figures/L11/source/L11_p13.png)

#### 빠른 생성물과 안정한 생성물은 서로 다른 비교다

kinetic product를 고를 때 비교하는 것은 **출발물에서 각 transition state까지의 장벽이고**, thermodynamic product를 고를 때 비교하는 것은 **생성물끼리의 에너지** 다. 장벽이 낮다고 생성물도 낮은 에너지를 가져야 하는 것은 아니다. MVK/CN 계에서는 낮은 장벽의 1,2 경로가 저온에서 먼저 관찰되지만, carbonyl을 유지하는 1,4 생성물은 더 안정하다. (출처: L11 p.13)

고온에서 cyanohydrin의 CN이 골격 위를 옆으로 이동하는 것은 아니다. 가역적인 1,2 첨가가 되돌아가 출발 enone을 내놓고, 그 enone이 1,4 경로로 반응할 수 있는 것이다. 따라서 **되돌아갈 수 있는 경로와 충분한 반응 시간이** 있어야 생성물 분포가 바뀐다. “저온 = 1,2, 고온 = 1,4”는 이 계의 결과이며, cuprate나 enamine의 모든 반응에 적용하는 온도 법칙이 아니다. (출처: L11 p.13) (보충 근거: Clayden p.504–505)

슬라이드의 결합 에너지 비교는 carbonyl 보존이 유리하다는 정성적 설명이다. 생성물 에너지 차이를 $369-280$ 만으로 정확히 계산한 값이나 실제 activation energy로 취급하지 않는다. 반응 장벽, 결합 에너지, 생성물 안정성은 구분해서 읽는다. (출처: L11 p.13; 도표 해석)

## 4. enolate의 conjugate addition: 1,5-dicarbonyl을 만드는 길

> 개념 문서: [Michael reaction](../../wiki/반응/마이클%20반응.md), [enol and enolate](../../wiki/개념/엔올과%20엔올레이트.md), [aldol reaction](../../wiki/반응/알돌%20반응.md), [kinetic vs thermodynamic enolate](../../wiki/개념/속도론적%20엔올레이트와%20열역학적%20엔올레이트.md), [alkoxide base](../../wiki/시약/알콕사이드%20염기.md), [malonic ester synthesis](../../wiki/반응/말론산%20에스터%20합성.md), [alpha-hydrogen acidity](../../wiki/개념/α-수소의%20산도.md)

### 4.1 기본형

ketone에 염기를 넣어 만든 enolate(→ [L7](L07_Enolate_Alkylation.md) enolate alkylation 문서 참고)는 탄소 nucleophile로서 Michael acceptor의 $\beta$-탄소를 공격한다.

$$
\begin{aligned}\mathrm{R_1COCH_3}&\xrightarrow{\text{base}}\text{enolate}\cr \text{enolate}&\xrightarrow{\mathrm{CH_2{=}CHCOR_2}}\mathrm{R_1COCH_2CH_2CH_2COR_2}\end{aligned}
$$

1. 염기가 $\alpha$ -H를 떼어 enolate를 만든다.
2. enolate의 $\alpha$-탄소(nucleophile)가 Michael 받개의 $\beta$-탄소(electrophile)를 공격해서 새 C-C 결합이 생긴다. 받개 쪽의 $\pi$ 전자는 산소로 밀려 **새 enolate가** 된다.
3. 이 enolate가 protonate되면 **1,5-dicarbonyl 화합물이** 된다.

![enolate의 alpha-탄소가 Michael 받개의 beta-탄소를 공격하는 화살표](../../figures/L11/enolate_michael.svg)

그림: 2단계의 전자 이동만 그렸다(생성물은 연습 문제 4로 남겨 두었다). 화살표는 넷이다. (1) O⁻의 비공유 전자쌍이 내려와 C=O를 다시 만들고, (2) enolate의 C=C $\pi$ 전자(파랑, nucleophile)가 받개의 $\beta$-탄소(빨강, electrophile)와 새 C–C 결합을 만든다. (3) 받개의 C=C $\pi$ 전자는 carbonyl 쪽 C–C 자리로, (4) 받개의 C=O $\pi$ 전자는 산소로 간다.

슬라이드 p.14의 빈칸은 2단계 생성물을 묻는다(연습 문제 참고). 그 밖의 Michael 받개 예시로는 methyl cinnamate(Ph-CH=CH-CO2Me), acrylonitrile(CH2=CH-CN), ethyl vinyl ketone(CH2=CH-CO-CH2CH3)이 있다. nitrile도 EWG라서 받개가 된다.

보충: nitrile 받개가 특히 깔끔한 이유는, nitrile 탄소는 친전자 자리로서 반응성이 낮아 nucleophile이 C≡N에 직접 붙는 경쟁(carbonyl의 1,2-첨가에 해당)이 거의 없기 때문이다. 그러면서도 음전하는 carbonyl처럼 잘 안정화한다. 그래서 acrylonitrile은 enolate에 대해 가장 좋은 Michael 받개 중 하나다. (보충 근거: Clayden p.510)

보충: 역합성에서 거꾸로 쓰는 요령도 기억해 두자. Claisen 축합은 두 carbonyl 사이에 포화 탄소가 하나인 1,3-dicarbonyl을, Michael 첨가는 포화 탄소가 셋인 **1,5-dicarbonyl을** 준다. 표적에 1,5 관계가 보이면 한쪽 carbonyl 기준 $\beta,\gamma$ 결합을 끊어 보자. $\beta$ 쪽 조각은 $\alpha,\beta$-unsaturated 받개, 다른 조각은 enolate(필요하면 ester를 덧붙인 안정한 enolate) 공여체가 된다. (보충 근거: Wade p.1087–1088)

(출처: L11 p.14)

#### donor와 acceptor의 탄소를 서로 다른 이름으로 추적한다

Michael donor는 enolate를 만드는 쪽, acceptor는 conjugated EWG를 가진 쪽이다. donor의 $\alpha$-탄소를 $C_{\mathrm D}$ , acceptor의 $\beta$-탄소를 $C_{\beta,\mathrm A}$ 라고 하면 새 결합은 항상 이 둘 사이에 만든다. acceptor의 $\alpha$-탄소를 donor가 공격하는 것으로 바꾸거나, donor의 O를 새 C–C 결합의 출발 원자로 그리면 다른 연결 구조가 된다. (출처: L11 p.14)

생성물의 1,5 관계는 다음처럼 **carbonyl 탄소도 포함하여** 센다.

$$
\underbrace{\mathrm{C(=O)}}_{1,\ \mathrm{donor}}
{-}\underbrace{\mathrm{C}}_{2,\ \mathrm{donor}\ \alpha}
{-}\underbrace{\mathrm{C}}_{3,\ \mathrm{acceptor}\ \beta}
{-}\underbrace{\mathrm{C}}_{4,\ \mathrm{acceptor}\ \alpha}
{-}\underbrace{\mathrm{C(=O)}}_{5,\ \mathrm{acceptor}}
$$

따라서 두 carbonyl 탄소 **사이에 있는 포화 탄소는 셋이다**. donor의 carbonyl은 enolate가 반응할 때 회복되고, acceptor의 carbonyl은 새 enolate의 protonation·tautomerization으로 회복된다. 두 carbonyl이 같은 시점에 같은 역할을 하는 것이 아님을 그림의 화살표와 연결해서 읽는다. (출처: L11 p.14,24)

### 4.2 경쟁 반응: conjugate addition vs aldol

그런데 enolate는 carbonyl 탄소를 직접 공격할 수도 있다. 그것이 바로 aldol reaction(→ [L8](L08_Aldol_Reactions.md) aldol reaction 문서 참고)이다. enolate와 enone을 섞으면 두 갈래가 생긴다.
- **conjugate addition(촉진해야 할 것)** : 1,5-dicarbonyl로 간다.
- **직접 첨가 = aldol(피해야 할 것)** : alkoxide를 거쳐 $\beta$ -hydroxy carbonyl이 된다(ketone 받개이면 OH 탄소가 3차, aldehyde 받개이면 2차). 이 단원의 경쟁 반응에서 aldol 단계는 **가역적이다**.

aldol이 가역이라는 점이 중요하다. 이 조건에서 aldol이 되었다가 되돌아오면, 상대적으로 되돌아가기 어렵고 thermodynamic으로 유리한 conjugate addition 생성물이 축적될 수 있다(3.3절의 논리와 같다).

보충: 따라서 conjugate addition을 돕는 전략은 모두 "aldol을 더 쉽게 되돌리는" 방향이다. (1) enolate를 더 안정하게 만들면(예: malonic ester처럼 EWG 두 개) aldol 생성물에서 그 안정한 anion이 다시 떨어져 나가기 쉬워지고, 덤으로 aldol 생성물이 더 붐벼서 불안정해진다. (2) 받개를 ester·amide처럼 carbonyl이 덜 electrophilic한 화합물로 고르면 aldol 자체가 덜 일어나고 더 잘 되돌려진다. 4.3절과 4.4절의 예들은 모두 이 두 전략의 응용이다. (보충 근거: Clayden p.605–606)

받개의 carbonyl 치환기 R이 바뀌면 conjugate addition 경향은 다음 순서로 커진다.

**R = H < alkyl < OR < NR2**

이 순서는 3.1절의 표를 뒤집은 것과 같다. 이 비교에서 amide는 carbonyl 직접 첨가의 경쟁이 약해 conjugate addition이 상대적으로 유리하다. 예:

$$
\begin{aligned}\text{cyclohexanone}&\xrightarrow{\mathrm{LDA}}\text{Li enolate}\cr \text{Li enolate}&\xrightarrow{\mathrm{(E){-}CH_3CH{=}CHCONMe_2}}\begin{gathered}\text{2-}(\mathrm{CH(CH_3)CH_2CONMe_2})\cr \text{cyclohexanone}\end{gathered}\end{aligned}
$$

(수율 60%)

![cyclohexanone enolate + (E)-CH3CH=CHCONMe2 → Michael (60%)](../../figures/L11/michael_cyclohexanone_amide.svg)

그림: enolate(파랑)가 $\beta$-탄소(빨강)에 1,4-첨가.

생성물은 cyclohexanone의 $\alpha$-탄소에 amide 받개의 $\beta$-탄소가 붙은 1,5-dicarbonyl이다.

(출처: L11 p.15)

#### aldol과 Michael을 구별하는 실제 결합

두 경로에서 donor의 공격 원자는 같은 $\alpha$-탄소다. **aldol에서는 acceptor의 carbonyl 탄소** , **Michael에서는 acceptor의 $\beta$-탄소가** 상대 원자다. aldol 후처리 생성물에서는 공격받은 acceptor C=O가 OH로 바뀌지만, Michael 후처리 생성물에서는 그 C=O가 남는다. 따라서 “enolate를 썼다”는 사실만으로 Michael이라고 이름 붙이지 않는다. (출처: L11 p.14–16)

강의 p.15의 3차 amide 받개는 N의 전자 주개 효과로 carbonyl 직접 공격이 상대적으로 불리하다. 이때 **carbonyl이 덜 electrophilic하다는 것과 conjugated alkene이 반응하지 않는다는 것은 다르다** . 바로 그 차이가 carbonyl 직접 첨가를 억제하면서 $\beta$ 첨가를 이용하는 설계다. 다만 모든 Michael 반응이 절대 비가역적이라는 뜻은 아니며, 여기서는 경쟁하는 aldol이 되돌아갈 수 있는 조건에서 원하는 생성물이 축적되는 흐름을 읽는다. (출처: L11 p.15) (보충 근거: Clayden p.605–606,610)

### 4.3 counterion과 enolate 종류가 결과를 바꾼다

**이 enal 예에서는 Li⁺ 배위가 1,2(aldol)를 돕는다.**

$$
\begin{aligned}\mathrm{(CH_3)_2CHCO_2Et}&\xrightarrow[{-78}\thinspace ^\circ\mathrm C,\ \mathrm{THF}]{\mathrm{LDA}}\text{Li enolate}\cr \text{Li enolate}&\xrightarrow{\mathrm{(CH_3)_2C{=}CHCHO}}\mathrm{(CH_3)_2C{=}CHCH(OH)C(CH_3)_2CO_2Et}\end{aligned}
$$

(수율 72%)

![ethyl isobutyrate enolate + 3-methylbut-2-enal → 1,2-adduct](../../figures/L11/isobutyrate_12.svg)

그림: 입체 장애가 큰 $\beta$-탄소 대신 C=O에 1,2-첨가한다.

이번에는 enal을 받개로 썼는데 conjugate addition이 아니라 **aldol(1,2) 생성물이** 나왔다. 왜일까? lithium 이온이 aldehyde 산소에 배위하면서 enolate 산소와 함께 고리형 transition state(cyclic transition state)를 만든다. 그래서 enolate 탄소가 바로 옆의 carbonyl 탄소를 공격하게 된다. 게다가 aldehyde는 원래 직접 첨가 비율이 높은 받개다(3.1절).

**thermodynamic enolate로 4차 탄소 만들기.**

$$
\text{2-methylcyclopentanone} \xrightarrow{\substack{\mathrm{CH_2{=}CHCO_2Me}\cr \mathrm{t\negthinspace {-}BuOK}}} \begin{gathered}\text{2-methyl-2-}(\mathrm{CH_2CH_2CO_2Me})\cr \text{cyclopentanone}\end{gathered}
$$

(수율 53%)

![2-methylcyclopentanone + methyl acrylate → Michael (53%)](../../figures/L11/michael_methylcyclopentanone.svg)

그림: 더 치환된 enolate(파랑)가 $\beta$-탄소(빨강)를 공격.

1. t-BuOK는 2-methylcyclopentanone의 양쪽 $\alpha$ -H를 가역적으로 떼어낸다. 그래서 두 enolate가 평형을 이룬다.
2. 평형에서는 더 치환된(C=C에 Me가 붙은) **thermodynamic enolate가** 우세하다(→ [L7](L07_Enolate_Alkylation.md) 문서의 kinetic/thermodynamic enolate 참고).
3. 이 enolate의 Me가 붙은 $\alpha$-탄소가 methyl acrylate의 $\beta$-탄소를 공격해서 4차 탄소가 생긴다. 생긴 ester enolate가 protonate되면 반응이 끝난다.

보충: 위의 두 예를 나란히 놓으면 counterion의 역할이 보인다. Li+는 산소에 강하게 결합해 aldol 생성물(lithium alkoxide)을 안정화하므로, lithium enolate는 열역학 지배가 필요한 conjugate addition에 불리하다. Na+나 K+ enolate는 더 해리되어 있어 aldol이 되돌아가기 쉽고, 그래서 conjugate addition이 유리하다. t-BuOK를 고른 데도 이유가 있다. 부피가 커서 methyl acrylate의 ester carbonyl을 공격하지 않으면서, ketone의 일부를 deprotonation하여 enolate 평형을 형성할 수 있다. 예외적으로 3차 amide 받개는 carbonyl 탄소의 electrophilicity가 낮아 lithium enolate로도 conjugate addition이 된다(4.2절의 LDA 예). (보충 근거: Clayden p.607, p.610)

(출처: L11 p.16)

[원본 자료에서 세부 구조·입체배치 확인: L11_Conjugate addition.pdf p.16](../../figures/L11/source/L11_p16.png)

#### 서로 다른 두 선택성을 구분한다

p.16의 두 예에는 서로 다른 질문이 들어 있다. Li enolate/enal 예의 질문은 **acceptor의 carbonyl과 $\beta$ 중 어디를 공격하느냐** 다. t-BuOK/2-methylcyclopentanone 예의 질문은 **donor의 두 $\alpha$ 위치 중 어느 쪽을 enolate로 사용하느냐** 다. 첫 예의 1,2/1,4 선택성과 둘째 예의 donor regioselectivity를 한 가지 규칙으로 섞으면 안 된다. (출처: L11 p.16)

둘째 예에서 methyl이 붙은 donor $\alpha$-탄소는 처음에는 H 하나와 세 C–C 결합을 가진다. 그 H를 잃고 enolate가 된 뒤 새 C–C 결합을 만들면, H가 사라진 자리에 acceptor 조각이 들어가 **네 탄소와 결합한 quaternary carbon이** 된다. 여기서 “thermodynamic”은 두 donor enolate 사이의 평형을 말한다. p.13의 1,2/1,4 최종 생성물 안정성 비교와는 무엇을 비교하는지가 다르다. (출처: L11 p.13,16)

Li⁺의 효과도 “Li가 보이면 Michael 금지”로 외우지 않는다. 바로 앞 p.15에는 LDA로 만든 Li enolate가 3차 amide 받개에 conjugate addition하는 예가 있다. counterion 효과는 받개 carbonyl의 반응성 및 배위 가능성과 함께 읽어야 한다. (출처: L11 p.15–16)

### 4.4 안정한 enolate: 1,3-dicarbonyl과 nitroalkane

1,3-dicarbonyl에서 얻은 enolate는 음전하를 두 carbonyl에 분산할 수 있다. 이런 안정화된 탄소 nucleophile도 conjugate addition의 donor로 사용한다.

**1,3-dicarbonyl 화합물** :

$$
\mathrm{CH_2(CO_2Et)_2} + \mathrm{CH_3CH{=}CH{-}CO_2Et} \xrightarrow[\mathrm{EtOH},\ \text{reflux}\ 1\ \text{h}]{\mathrm{NaOEt}} \mathrm{(EtO_2C)_2CHCH(CH_3)CH_2CO_2Et}
$$

diethyl malonate enolate가 ethyl crotonate의 $\beta$-탄소(CH3가 붙은 탄소)를 공격한다.

![diethyl malonate + ethyl crotonate → Michael](../../figures/L11/michael_malonate_crotonate.svg)

그림: malonate anion(파랑) → $\beta$-탄소(빨강).

**nitroalkane** : nitro group $\alpha$ -H는 산성이 커서 약한 염기로도 nitronate anion이 생긴다.

$$
\mathrm{PhCH_2NO_2} + \text{2-cyclohexenone} \xrightarrow[0\text{–}25\thinspace{}^\circ\mathrm{C},\ \text{neat}]{\ \mathrm{Al_2O_3}\ \mathstrut} \text{3-}(\mathrm{CH(Ph)NO_2})\text{cyclohexanone}
$$

(수율 92%)

$$
\mathrm{I(CH_2)_4CH{=}CHCO_2Me} + \mathrm{CH_3NO_2} \xrightarrow{\mathrm{Cs_2CO_3}} \begin{gathered}\mathrm{I(CH_2)_4CH(CH_2NO_2)}\cr \mathrm{{-}CH_2CO_2Me}\end{gathered}
$$

DMF, 20 °C. Michael 첨가 뒤의 사슬을 다음 단계에 그대로 이어 쓴다.

$$
\begin{gathered}\mathrm{I(CH_2)_4CH(CH_2NO_2)}\cr \mathrm{{-}CH_2CO_2Me}\end{gathered}\xrightarrow[\text{intramolecular SN2}]{\mathrm{Cs_2CO_3}}\begin{gathered}\text{methyl 2-(2-nitrocyclohexyl)}\cr \text{acetate}\end{gathered}
$$

(수율 65%)
 1. nitromethane의 anion이 enester의 $\beta$-탄소에 conjugate addition한다(분자 간).
 2. 생성물의 CH2NO2는 여전히 산성 $\alpha$ -H를 갖는다. 그래서 다시 deprotonate된 nitronate 탄소가 같은 분자의 C-I를 SN2로 공격해 고리를 닫는다(분자 내 alkylation).
 3. 결과는 NO2와 CH2CO2Me가 이웃한 탄소에 붙은 cyclohexane이다. conjugate addition과 alkylation이 연달아 일어난 셈이다.

![PhCH2NO2 + 2-cyclohexenone → Michael (92%)](../../figures/L11/michael_nitro_cyclohexenone.svg)

그림: nitronate(파랑)가 $\beta$-탄소(빨강)에 첨가.

![Michael 후 분자내 SN2 → methyl 2-(2-nitrocyclohexyl)acetate](../../figures/L11/michael_nitro_cyclization.svg)

그림: Michael 첨가 뒤 nitronate가 C–I를 SN2로 닫아 고리(초록).

보충: nitro group은 pKa 기준으로 carbonyl 두 개에 맞먹는 EWG다(nitroalkane $\alpha$ -H의 pKa 약 10). 그래서 Al2O3, K2CO3, amine 같은 아주 약한 염기로도 nitronate가 생기고, ketone·ester 쪽의 자기 축합 같은 부반응을 피할 수 있다. 또 반응은 **염기 촉매로** 돈다. 첨가 직후 생긴 enolate(conjugate acid pKa 약 20–25)가 nitronate보다 훨씬 강한 염기라서, 다음 nitroalkane 분자에서 양성자를 떼어 새 nucleophile을 만들어 주기 때문이다. 위 고리화 예의 염기는 Cs₂CO₃다. 교재는 큰 Cs⁺가 carbonate ion과 강하게 배위하지 않아 carbonate가 염기로 작용하기 유리한 조건이라고 설명한다. (보충 근거: Clayden p.611–612)

(출처: L11 p.17)

#### 안정화된 anion과 연속 고리화를 읽는 순서

“안정한 enolate”는 반응성이 없다는 뜻이 아니라, 음전하를 여러 EWG에 분산할 수 있다는 뜻이다. malonate는 두 ester 사이의 탄소에서 H를 잃고, nitroalkane은 nitro group 옆 탄소에서 H를 잃어 nitronate가 된다. **nitronate는 carbonyl enolate와 같은 물질은 아니지만** , 탄소에서 결합을 만들 수 있는 안정화된 anion이라는 점에서 같은 Michael donor 전략에 들어간다. (출처: L11 p.17) (보충 근거: Clayden p.605–606,611)

nitromethane의 연속 반응에서는 먼저 분자 사이 Michael addition으로 탄소 사슬을 연결한다. 이어 처음 nitromethane에서 온 탄소가 다시 H를 잃고, 같은 분자 안의 C–I 탄소를 공격한다. 새로 닫힐 고리는 **nitromethane의 탄소 하나 + acceptor의 원래 $\beta$-탄소 하나 + 그 뒤의 CH₂ 넷 = 여섯 원자** 다. ester carbonyl이나 nitro의 N을 고리 원자 수에 포함시키지 않는다. 두 번째 단계는 alkyl iodide의 SN2이므로 C–I 결합이 끊기며 I⁻가 나가고, 첫 단계에서 생긴 C–C 결합은 유지된다. (출처: L11 p.17; 골격 추적)

보충: 여기서는 anion의 **생성 가능성, 염기성, 반응 위치를** 따로 생각해야 한다. 음전하가 EWG에 분산되면 그 anion을 만들기 위한 deprotonation은 쉬워지고, 생성된 anion의 염기성은 낮아진다. 그렇다고 탄소에서 결합을 만드는 능력이 없어지는 것은 아니다. 안정화된 donor를 쓰면 경쟁하는 aldol 첨가가 되돌아가기 쉬워져 Michael 생성물이 축적되는 데 유리할 수 있다. 따라서 “안정한 anion이므로 더 강한 nucleophile”이라고 설명하기보다, **원하는 반응과 경쟁 반응의 상대적인 진행 정도가 달라진다** 고 읽는 편이 정확하다. (보충 근거: Clayden p.605–606,611)

## 5. enamine: 중성이면서 soft nucleophile

> 개념 문서: [enamine](../../wiki/개념/엔아민.md), [Stork enamine reaction](../../wiki/반응/스토크%20엔아민%20반응.md), [iminium ion](../../wiki/개념/이미늄%20이온.md), [reductive amination](../../wiki/반응/환원성%20아미노화.md), [Michael reaction](../../wiki/반응/마이클%20반응.md)

### 5.1 enamine 복습

enamine은 aldehyde나 ketone이 **2차 amine과** 반응해서 생긴다(→ [L10](L10_Enol_and_Enamine.md) enol과 enamine 문서 참고). 자주 쓰는 2차 amine은 pyrrolidine, piperidine, morpholine이다.

$$
\text{cyclohexanone} + \text{pyrrolidine} \xrightarrow{\text{cat.}\ \mathrm{H^+}} \text{1-pyrrolidinylcyclohexene}\ (\text{enamine})
$$

$$
\text{enamine} \xrightarrow{\ 1.\ \mathrm{R{-}X};\ 2.\ \mathrm{H_2O},\ \mathrm{H^+}\ \mathstrut} \text{2-R-cyclohexanone}
$$

![cyclohexanone + pyrrolidine → enamine](../../figures/L10/enamine_cyclohexanone.svg)

그림: 2차 amine N(파랑)이 C=O(빨강)와 축합해 enamine(초록)이 된다.

1. 질소의 비공유 전자쌍이 C=C 쪽으로 밀려서 enamine의 $\beta$-탄소(carbonyl이었던 탄소의 이웃)가 nucleophile이 된다. 이 탄소가 R-X를 SN2로 공격한다.
2. **iminium이** 생긴다. iminium은 $\alpha$ -H를 잃고 enamine과 평형을 이룰 수 있다.
3. 물과 산으로 가수분해하면 ketone이 다시 나오고, $\alpha$-위치에 R이 붙어 있다.

슬라이드는 "Imine and Enamine are tautomers"라고 정리하고[^4], 환원성 amine화(reductive amination)를 떠올려 보라고 한다.

(출처: L11 p.18)

#### enamine의 어느 탄소가 donor인가

enamine을 $\mathrm{R_2N{-}C{=}C}$ 로 적으면 N에서 먼 쪽의 C가 새 결합을 만드는 탄소다. 이 탄소는 **원래 carbonyl 화합물을 기준으로는 $\alpha$-탄소이고**, N을 기준으로 부르는 enamine의 위치 표현에서는 $\beta$-탄소다. 강의마다 부르는 번호가 달라도 같은 원자다. enamine donor의 이 탄소와 Michael acceptor의 $\beta$-탄소를 구분하여 표시한 뒤 새 결합을 잇는다. (출처: L11 p.18–19; L10 p.11)

N의 전자쌍은 C=N⁺를 만들며 전자를 밀어 주고, 실제 새 C–C 결합은 enamine의 C=C 전자가 만든다. 따라서 최종 생성물에 acceptor를 N에 직접 연결하면 이 강의의 carbon addition과 다른 생성물이다. 가수분해에서는 C=N을 거쳐 C=O가 돌아오며 amine이 분리된다. C–C 결합 형성에 관여한 탄소는 가수분해 후에도 같은 자리에 남는다. (출처: L11 p.18–19)

### 5.2 enamine의 conjugate addition

enamine은 전하가 없는 **soft 탄소 nucleophile이다**. 따라서 conjugate addition의 탄소 nucleophile로 사용할 수 있다. 반응 뒤 H2O로 iminium/enamine을 가수분해하면 ketone이 돌아온다.

$$
\begin{gathered}\text{pyrrolidine}\cr \text{enamine}\end{gathered}\xrightarrow[\mathrm{2.\ H_2O}]{\mathrm{1.\ CH_2{=}C(SMe)CO_2Me}}\begin{gathered}\text{2-}(\mathrm{CH_2CH(SMe)CO_2Me})\cr \text{cyclohexanone}\end{gathered}
$$

cyclohexanone 유래 pyrrolidine enamine을 사용한다. 조건: MeCN에서 첨가 후 H₂O 처리. (출처: L11 p.19)

(수율 95%)

$$
\begin{gathered}\text{morpholine}\cr \text{enamine}\end{gathered}\xrightarrow[\mathrm{2.\ H_2O}]{\mathrm{1.\ CH_2{=}C(SO_2Ph)COCH_3}}\begin{gathered}\text{2-}(\mathrm{CH_2CH(SO_2Ph)COCH_3})\cr \text{cyclohexanone}\end{gathered}
$$

cyclohexanone 유래 morpholine enamine을 사용한다. 조건: SiO₂/THF, 0–20 °C, 2 h 반응 후 H₂O 처리. (출처: L11 p.19)

(수율 75%)

![pyrrolidine enamine + CH2=C(SMe)CO2Me → Michael (95%)](../../figures/L11/enamine_michael_sme.svg)

그림: enamine $\beta$ -C(파랑)가 acceptor $\beta$-탄소(빨강)에 첨가한 뒤 가수분해.

![morpholine enamine + CH2=C(SO2Ph)COCH3 → Michael (75%)](../../figures/L11/enamine_michael_so2ph.svg)

그림: morpholine enamine의 탄소가 acceptor의 말단 탄소와 결합하고, 가수분해 후 donor의 ketone이 회복된다.

두 경우 모두 enamine 탄소는 받개의 말단 CH2( $\beta$-탄소)에 붙는다. 생성물은 1,5-dicarbonyl 관계다. 세 번째 예(morpholine enamine + EtO2C-CH=CH-NO2)는 빈칸이라서 연습 문제로 옮겼다.

보충: enamine이 enol보다 나은 이유는 두 가지다. 질소가 산소보다 전자를 더 잘 밀어 주어 친핵성이 크고, 미리 정량적으로 만들어 둘 수 있다. 첨가 직후에는 enolate–iminium 쌍극성 이온이 생기는데, 빠른 양성자 이동으로 더 안정한 "carbonyl + enamine" tautomer가 된다. 이 enamine은 반응이 끝날 때까지 그대로 있다가 산성 수용액 후처리에서 iminium을 거쳐 가수분해되고, 2차 amine은 염산염으로 씻겨 나간다. 그래서 가수분해는 별도 단계라기보다 후처리의 일부다. (보충 근거: Clayden p.608)

(출처: L11 p.19)

![pyrrolidine enamine의 beta-탄소가 methyl 2-(methylthio)acrylate의 말단 CH2를 공격해 iminium–enolate 쌍극성 이온이 되는 단계](../../figures/L11/enamine_conjugate.svg)

그림: [enamine](../../wiki/개념/엔아민.md)의 conjugate addition(cyclohexanone의 pyrrolidine enamine + CH₂=C(SMe)CO₂Me). 질소의 비공유 전자쌍(파랑)이 N–C 결합 쪽으로 밀려 C=N⁺를 만들고, 파란 C=C의 $\pi$ 전자가 받개의 $\beta$-탄소(빨간 C=C의 말단 CH₂)를 공격한다. 받개 쪽에서는 C=C의 $\pi$ 전자가 C–C(O) 자리로, C=O의 $\pi$ 전자가 산소로 간다. 결과는 iminium과 ester enolate가 한 분자에 있는 쌍극성 이온이고(초록이 새 C–C 결합), H₂O 후처리로 1,5-dicarbonyl 화합물이 된다. 보충: 슬라이드는 반응식만 보여 주며, 쌍극성 이온 intermediate는 Clayden의 설명을 따랐다. (출처: L11 p.19) (보충 근거: Clayden p.608)

#### enamine Michael을 끝까지 그리는 순서

p.19의 첫 받개 $\mathrm{CH_2{=}C(SMe)CO_2Me}$ 에서는 CO₂Me에 바로 붙은 탄소가 $\alpha$ , 말단 CH₂가 $\beta$ 다. SMe가 달린 탄소를 새 결합의 위치로 고르는 것이 아니다. donor의 반응 탄소를 말단 CH₂에 붙인 뒤, acceptor 쪽의 원래 $\alpha$-탄소에 H가 들어가면 **donor–CH₂–CH(SMe)–CO₂Me** 연결이 된다. SMe와 ester는 원래 같은 탄소에 연결된 상태를 유지한다. (출처: L11 p.19)

첨가 직후 iminium⁺와 enolate⁻를 그렸다면 아직 후처리 전이다. proton transfer로 받개의 carbonyl이 돌아오고, 가수분해로 donor의 carbonyl도 돌아온 뒤 최종 구조를 읽는다. 그러면 donor ketone–donor $\alpha$ –acceptor $\beta$ –acceptor $\alpha$ –acceptor ester의 1,5 관계를 확인할 수 있다. **물 처리는 새 C–C 결합을 만드는 단계가 아니라 가수분해로 C=O를 회복하는 단계** 다. (출처: L11 p.19) (보충 근거: Clayden p.608)

### 5.3 합성 응용: dopamine 길항제

conjugate addition은 의약품 합성에도 쓰인다. 슬라이드의 예는 dopamine antagonist인 1-propyl-3-(2,5-dimethoxyphenyl)piperidine의 합성이다.[^5]

$$
\begin{aligned}\mathrm{ArCH_2CO_2Et}&\xrightarrow[\text{Triton B}]{\mathrm{CH_2{=}CHCN}}\boxed{\text{빈칸 1}}\cr \boxed{\text{빈칸 1}}&\xrightarrow{\mathrm{H_2/Pd/C}}\boxed{\text{빈칸 2}}\cr \boxed{\text{빈칸 2}}&\xrightarrow{\text{alkylation, reduction}}\text{생성물}\end{aligned}
$$

여기서 Ar은 2,5-dimethoxyphenyl이다.

Triton B는 수산화 benzyltrimethylammonium이고, ester $\alpha$ -H를 떼는 염기 역할을 한다. 빈칸은 연습 문제로 옮겼다.

보충: Triton B 같은 4차 암모늄 수산화물을 쓰는 이유는, 유기 cation 덕분에 수산화 이온이 유기 용매에 녹기 때문이다. Clayden은 같은 경로를 "enolate의 acrylonitrile conjugate addition → nitrile의 1차 amine 환원 → (저절로 일어나는) lactam 고리화 → alkylation과 amide 환원"으로 소개한다. 즉 H2/Pd/C 단계 뒤의 lactam 형성은 따로 시약이 필요 없는 자발적 반응이다. (보충 근거: Clayden p.612)

(출처: L11 p.20)

#### 합성 경로에서 탄소 사슬과 고리 크기 추적하기

보충: Ar을 2,5-dimethoxyphenyl로 두면 첫 Michael 생성물은 $\mathrm{Ar{-}CH(CO_2Et){-}CH_2{-}CH_2{-}CN}$ 이다. 출발 ester의 $\alpha$-탄소와 acrylonitrile의 말단 탄소 사이에 결합이 생긴 것이며, CN은 제거되지 않고 사슬 끝에 남는다. nitrile 환원 뒤에는 **CN의 탄소가 CH₂가 되고 N이 NH₂가 되므로** , $\mathrm{Ar{-}CH(CO_2Et){-}CH_2{-}CH_2{-}CH_2NH_2}$ 가 된다. 환원을 탄소 하나를 추가하는 반응으로 그리지 않는다. (출처: L11 p.20) (보충 근거: Clayden p.612)

보충: 그 NH₂가 같은 분자의 ester carbonyl을 공격하면, N–CH₂–CH₂–CH₂–CH(Ar)–C(=O)의 여섯 원자로 lactam 고리가 닫히고 ester의 EtO 부분은 ethanol로 빠진다. 마지막 amide 환원은 고리의 C=O를 CH₂로 바꾸며, N-propyl alkylation은 고리 N의 치환기를 정한다. **고리 골격을 만드는 단계, N 치환기를 넣는 단계, carbonyl을 없애는 단계를 구분** 하면 긴 합성식도 한 번에 외울 필요가 없다. (출처: L11 p.20) (보충 근거: Clayden p.612)

## 6. iminium 이온 촉매: 받개를 더 강한 electrophile로 바꾸기

> 개념 문서: [iminium-catalysed conjugate addition](../../wiki/반응/이미늄%20촉매%20공액%20첨가.md), [iminium ion](../../wiki/개념/이미늄%20이온.md)

지금까지는 nucleophile을 바꿔서 conjugate addition을 조절했다. 그러면 받개 쪽을 강화할 수는 없을까? enal을 2차 amine 촉매와 축합해 **iminium 이온으로** 바꾸면 된다. iminium 이온은 중성 carbonyl 화합물보다 더 친전자적이다. 양전하를 띤 C=N+가 C=O보다 전자를 더 세게 끌기 때문이다.

슬라이드의 반응: enal H-CO-CH=CH-R1과 pyrrole 유도체(R2, R3 치환, N-P)에 키랄 imidazolidinone 촉매(5-benzyl-2,2,3-trimethylimidazolidin-4-one, 20 mol%)를 넣으면 $\beta$-위치에 pyrrole C2가 붙은 aldehyde가 생긴다. 수율 68–90%, 87–97% ee, 12개 예시. R1은 방향족/지방족, R2·R3는 지방족, P = H, Me, allyl이다.[^6]

crotonaldehyde(CH3CH=CH-CHO)와 N-methylpyrrole로 메커니즘을 보면 다음과 같다.
1. **iminium 형성** : 촉매의 2차 amine(N-H)이 crotonaldehyde와 축합해서 $\alpha,\beta$-unsaturated iminium 이온이 된다.
2. **입체선택적 conjugate addition** : N-methylpyrrole의 C2(nucleophile, 전자 공여성이 있는 방향족 $\pi$ 계)가 iminium의 $\beta$-탄소(electrophile)를 공격한다. 이때 촉매의 benzyl group이 한쪽 면을 가리고 있다. 그래서 pyrrole은 **benzyl group을 피해 반대쪽(아래쪽) 면에서** 접근한다. 생성물은 촉매 쪽 enamine과 pyrrolium cation(방향족성이 깨진 상태)이다.
3. **재방향족화** : pyrrolium에서 H+가 빠지면서 pyrrole의 방향족성이 회복된다.
4. **가수분해** : iminium/enamine 부분이 가수분해되어 (R)-3-(1-methylpyrrol-2-yl)butanal이 나오고, 촉매가 재생된다.

즉 촉매가 받개를 활성화하고 동시에 면 선택성까지 정한다.

(출처: L11 p.21)

![N-methylpyrrole의 C2가 iminium ion의 beta-탄소를 benzyl group 반대쪽 면에서 공격하는 단계](../../figures/L11/iminium_attack.svg)

그림: 2단계(입체선택적 conjugate addition). 왼쪽 위는 촉매와 crotonaldehyde가 만든 iminium ion이다(빨간 C=N⁺와 C=C가 받개). 아래의 N-methylpyrrole(파랑)에서 질소 전자쌍이 고리로 밀려 들어가고, 고리 C=C 전자가 옮겨 가며, 파란 C2=C3의 $\pi$ 전자가 iminium의 $\beta$-탄소를 공격한다. 동시에 받개의 C=C 전자는 C–C(=N⁺) 자리로, C=N⁺의 $\pi$ 전자는 질소로 간다. 오른쪽 생성물은 촉매 쪽 enamine과 pyrrolium cation이며, 새 C–C 결합(초록 점선 쐐기)은 슬라이드처럼 benzyl group(굵은 쐐기)를 피한 아래쪽 면 공격의 결과다. 이후 H⁺가 빠져 재방향족화하고 가수분해되면 (R)-aldehyde가 나온다. (출처: L11 p.21)

[원본 자료에서 세부 구조·입체배치 확인: L11_Conjugate addition.pdf p.21](../../figures/L11/source/L11_p21.png)

#### enamine activation과 iminium activation을 나란히 읽기

| 확인 항목 | enamine donor activation | iminium acceptor activation |
|---|---|---|
| amine이 먼저 결합하는 상대 | donor aldehyde/ketone | acceptor enal |
| 반응에서 커지는 성질 | 탄소의 nucleophilicity | conjugated 계의 electrophilicity |
| 새 결합을 만드는 탄소 | 원래 donor의 $\alpha$-탄소 | acceptor의 $\beta$-탄소가 공격받음 |
| 후처리 | donor C=O 회복 | acceptor C=O 회복 및 촉매 재생 |

p.21에서는 pyrrole의 **C2와** enal의 **$\beta$-탄소를** 연결한다. pyrrole의 N은 고리 전자를 밀어 주지만 새 결합이 생기는 원자는 고리 C2다. 첨가로 aromaticity가 잠시 깨진 뒤 C2의 H⁺가 빠지면서 pyrrole이 다시 aromatic해진다. 그 뒤 aldehyde를 회복해야 최종 생성물이므로, 촉매와의 C–N 결합이 남은 중간체에서 답안을 끝내지 않는다. (출처: L11 p.18–21)

면 선택성과 regioselectivity도 나누어 읽는다. $\beta$ 공격은 **어느 원자를 고르느냐** , benzyl group 반대면의 접근은 **어느 면에서 접근하느냐의** 문제다. 그림의 “아래쪽”은 해당 배치에서의 표현이지 종이를 돌려도 아래에서 공격한다는 뜻이 아니다. 같은 촉매 그림을 기준으로 두 면을 구분하고, 제시된 crotonaldehyde 예의 (R) 배치를 확인한다. 다른 기질까지 (R)이라고 자동 지정하지 않는다. (출처: L11 p.21)

수율과 ee는 다른 수치다. 수율 68–90%는 얻은 생성물의 양, ee 87–97%는 생성물 enantiomer 조성의 치우침을 나타낸다. ee를 major enantiomer의 백분율로 그대로 쓰지 않는다. (출처: L11 p.21; 수치 구분)

ee의 의미를 수치로 확인해 보면, 두 enantiomer만 있다고 할 때 ee 87%는 major 93.5%, minor 6.5%에 해당한다. 둘의 합은 100%이고 차이가 87%이기 때문이다. 이 조성은 수율과 별개다. 수율이 높아도 두 enantiomer가 비슷하게 생기면 ee는 낮을 수 있다. (출처: L11 p.21; ee 정의에 따른 계산 예)

## 7. $\beta$ -leaving group이 있는 conjugate addition과 SNAr

> 개념 문서: [addition-elimination](../../wiki/반응/첨가-제거%20반응.md), [SNAr](../../wiki/반응/친핵성%20방향족%20치환.md), [Meisenheimer complex](../../wiki/개념/마이젠하이머%20착물.md)

### 7.1 첨가-제거 메커니즘

 $\beta$-탄소에 leaving group(예: F)가 붙어 있으면 어떻게 될까? conjugate addition으로 생긴 enolate가 그냥 protonate되지 않는다. 대신 전자를 되밀어 leaving group을 내보낸다. 결과적으로 $\beta$ -leaving group이 nucleophile로 **치환** 된다.

$$
\begin{aligned}
& \text{1-(2-fluorocyclohex-1-enyl)ethanone} + \mathrm{R_2NH} \cr
& \qquad \longrightarrow \text{1-(2-}\mathrm{NR_2}\text{-cyclohex-1-enyl)ethanone}
\end{aligned}
$$

1. **addition** : R2NH의 질소가 F가 붙은 $\beta$-탄소를 공격한다. C=C의 $\pi$ 전자는 산소로 가서 enolate가 된다. 이때 $\beta$-탄소는 sp3가 되고 N과 F가 함께 붙어 있다.[^7]
2. **elimination** : enolate 산소의 전자가 되돌아와 C=O를 다시 만든다. 동시에 $\alpha$ = $\beta$ 이중결합이 재생되면서 F-가 떨어진다.
3. 결과는 $\beta$-아미노 enone이다. C=C가 다시 생겼다는 점이 단순 conjugate addition과 다르다.

![R2NH가 F가 붙은 beta-탄소에 첨가한 뒤 F⁻가 떨어지는 첨가-제거 메커니즘](../../figures/L11/addition_elimination.svg)

그림: 왼쪽(첨가): $R_2NH$ 의 질소(파랑) 비공유 전자쌍이 F가 붙은 $\beta$-탄소를 공격하고, 빨간 C=C의 $\pi$ 전자는 C–C(O) 자리로, C=O의 $\pi$ 전자는 산소로 간다. 가운데 intermediate에서 $\beta$-탄소는 sp3이고 N과 F가 함께 붙어 있다(초록이 새 C–N 결합, 질소는 슬라이드처럼 양성자를 잃은 $R_2N$ 으로 그렸다[^7]). 오른쪽(제거): O⁻ 전자쌍이 C=O를 다시 만들고, enolate의 C=C 전자가 고리 안 C=C로 옮겨 가며, C–F 결합(빨강) 전자가 F⁻로 떨어진다.

(출처: L11 p.22)

#### 첨가 후 protonation과 제거의 갈림길

보통의 conjugate addition에서는 $\beta$ 에 Nu가 붙고 $\alpha$ 에 H가 들어가 포화 carbonyl이 된다. 반면 $\beta$-탄소에 F 같은 leaving group이 있으면 첨가 intermediate에서 **Nu와 F가 일시적으로 같은 탄소에 공존한다**. 그 뒤 전자가 되돌아오며 C=C가 회복되고 F⁻가 나가므로, 전체 결과는 Nu/H의 첨가가 아니라 F/Nu의 치환이다. (출처: L11 p.22)

전자쌍을 추적할 때 새 C–N 결합은 유지하고 C–F 결합만 끊는다. N에 붙어 있던 H는 별도의 proton transfer로 정리해야 하며, 중성 $\mathrm{R_2NH}$ 가 붙은 직후 N을 아무 전하 없이 네 결합으로 그리지 않는다. 강의 그림이 proton transfer를 생략한 $\mathrm{R_2N}$ 형태를 썼다는 점과, 실제로 첫 첨가 직후의 전하 수지는 구분한다. (출처: L11 p.22; 전하 검산)

### 7.2 nucleophilic aromatic substitution(SNAr)

같은 논리를 benzene 고리에 적용하면 **nucleophilic aromatic substitution(SNAr)이** 된다. L3~L4의 electrophilic aromatic substitution(SEAr)에서는 방향족 고리가 nucleophile였다. 그런데 강한 EWG가 붙으면 고리가 전자 부족해져 반대로 nucleophile의 공격을 받는다.

보충: 그렇다면 보통의 bromobenzene은 왜 HO-와 치환하지 않을까? SN2는 nucleophile이 C–Br 결합 뒤쪽에서 일직선으로 들어와야 하는데, sp2 탄소의 C–Br 결합은 고리 평면 안에 있어서 뒤쪽이 곧 고리 안쪽이다. nucleophile이 고리 속으로 들어가 탄소를 뒤집을 수는 없으므로 **sp2 탄소에서는 SN2가 일어나지 않는다** . SN1도 불리하다. 생길 아릴 cation의 빈 오비탈이 p가 아니라 고리 밖을 향한 sp2 오비탈이라 안정화를 받지 못하기 때문이다. 그래서 halobenzene의 치환에는 첨가-제거라는 별도의 경로가 필요하고, 이 단원의 addition–elimination 경로는 첨가로 생긴 음전하를 받아 줄 EWG가 있을 때 유리해진다. (보충 근거: Clayden p.514–515)

$$
\begin{aligned}
& \mathrm{Ar(EWG){-}X} + \mathrm{Nu^-} \cr
& \longrightarrow [\sigma\ \text{complex}] \cr
& \longrightarrow \mathrm{Ar(EWG){-}Nu} + \mathrm{X^-}
\end{aligned}
$$

1. **첨가** : Nu-가 X가 붙은 ipso 탄소를 공격한다. 그 탄소는 sp3가 되고, 음전하는 고리 전체(그리고 EWG)로 퍼진 anion성 **$\sigma$ complex에** 놓인다.[^8]
2. **제거** : X-가 떨어지면서 방향족성이 회복된다.

**SNAr의 세 가지 규칙은** 다음과 같다.
1. **leaving group 순서는 F >> Cl ~ Br >> I다** (o-nitrohalobenzene 기준). 슬라이드는 "F가 가장 좋은 leaving group"라고 표현한다. SN2와 순서가 정반대인 점이 핵심이다.[^9]
2. **강한 EWG가 필요하다** . 상대 속도(k_rel)는 NO2 = 1, SO2Me = 1/18, CN = 1/32, COMe = 1/80이다. nitro group이 가장 강하다.
3. **leaving group은 EWG의 ortho 또는 para 위치에 있어야 한다** . 그래야 첨가 단계에서 생긴 음전하가 공명으로 EWG(C=O 산소나 NO2 산소)까지 퍼질 수 있다. meta 위치에서는 음전하가 EWG가 붙은 탄소로 가지 못한다.

보충: 규칙 1의 크기를 숫자로 보면, 2-halonitrobenzene에서 F 화합물은 Cl·Br 화합물보다 약  $10^2$ – $10^3$ 배 빠르고 I 화합물은 더 느리다. 규칙 3의 근거도 실험으로 확인된다. cyclohexadienyl anion(SNAr intermediate의 모형)의 13C NMR에서 공격 자리 기준 ortho·para 탄소는 benzene(약 130 ppm)보다 훨씬 고장(약 76–78 ppm)으로, meta 탄소는 거의 그대로(약 132 ppm) 나타난다. 음전하가 사실상 ortho·para에만 놓인다는 뜻이다. 그래서 한 분자에 Cl이 둘 있어도 NO2의 ortho에 있는 Cl만 치환되고 meta의 Cl은 남는다. 참고로 규칙 1의 F 효과는 공명이 아니라 **유발 효과** (C–F 결합의 분극)이고, NO2의 효과는 주로 **공명이다**. (보충 근거: Clayden p.517–518)

예시는 다음과 같다.

$$
\text{2-fluoroacetophenone} + \mathrm{R_2NH} \xrightarrow[\text{elimination}]{\text{addition}} \text{2-}(\mathrm{NR_2})\text{acetophenone}
$$

 acetyl group의 ortho 위치 F가 치환된다. 7.1절의 cyclohexene 예와 메커니즘이 같다. 음전하가 acetyl 산소로 가서 enolate가 된다.

$$
\text{4-chloronitrobenzene} + \mathrm{HO^-} \xrightarrow[\text{elimination}]{\text{addition}} \text{4-nitrophenol}
$$

 para 위치의 Cl이 치환되고, 음전하는 NO2 산소까지 퍼진다.[^10]

![4-chloronitrobenzene + HO− → 4-nitrophenol (SNAr)](../../figures/L11/snar_chloronitrobenzene.svg)

그림: para $NO_2$ 가 음전하를 받아 주므로 Cl(빨강)이 OH(초록)로 치환된다.

(출처: L11 p.22, p.23)

![HO⁻가 4-chloronitrobenzene의 ipso 탄소를 공격해 음전하가 NO₂ 산소에 놓인 sigma complex가 되는 addition 단계](../../figures/L11/snar_addition.svg)

그림: SNAr의 addition 단계(4-chloronitrobenzene + HO⁻). HO⁻(파랑)의 비공유 전자쌍이 Cl이 붙은 ipso 탄소를 공격하고, 빨간 C=C의 $\pi$ 전자는 옆 C–C 자리로, 그다음 고리 C=C의 $\pi$ 전자는 C–N 자리로, N=O의 $\pi$ 전자는 산소로 차례로 밀려난다(주황 화살표 네 개). 오른쪽 $\sigma$ complex(Meisenheimer complex)에서 ipso 탄소는 sp³이고 HO와 Cl을 함께 가지며(초록이 새 C–O 결합), 음전하는 NO₂의 두 산소에 놓인 nitronate 형태다. (출처: L11 p.23)

![sigma complex에서 Cl⁻가 떨어지며 4-nitrophenol이 되는 elimination 단계](../../figures/L11/snar_elimination.svg)

그림: SNAr의 elimination 단계. NO₂의 O⁻(파랑) 전자쌍이 N=O를 다시 만들고, C=N의 $\pi$ 전자는 고리 C–C 자리로, 고리 아래쪽 C=C의 $\pi$ 전자는 ipso 탄소 쪽 C–C 자리로 옮겨 가며, C–Cl 결합(빨강)의 전자가 Cl⁻로 떨어진다. 결과는 aromaticity가 회복된 4-nitrophenol이다. 슬라이드는 이 단계의 화살표 중 O⁻ → N, 고리 안 하나, C–Cl → Cl만 그렸고, 그림은 같은 전자 흐름을 고리를 따라 끝까지 이어 그린 것이다. (출처: L11 p.23)

NO₂에 음전하를 표시한 그림에서는 원래 nitro group의 전하도 함께 센다. 중성 nitro group의 기여 구조는 N⁺와 O⁻ 하나를 가지므로 합이 0이다. addition intermediate를 N⁺와 O⁻ 둘로 나타낸 구조에서는 그 부분의 합이 −1이다. 따라서 “두 산소에 음전하가 있다”는 설명을 분자 전체가 −2라는 뜻으로 읽으면 안 된다. 출발 nucleophile이 HO⁻라면 중성 aryl halide와 합친 전체 전하도 −1로 유지되어야 한다. (출처: L11 p.23; 전하 검산)

#### SNAr에서 공격 자리와 EWG의 상대 위치 찾기

먼저 X가 붙은 **ipso 탄소를** 고정하고, 그 자리를 1번으로 둔다. addition intermediate의 음전하를 고리를 따라 그리면 2·4·6번, 즉 ipso 기준 ortho·para 위치로 분산시킬 수 있다. EWG가 그 자리에서 음전하를 더 받아 줄 때 addition intermediate가 안정해진다. 따라서 NO₂가 X의 ortho/para인지 보는 것이며, 단순히 “benzene에 NO₂가 있다”는 확인만으로 충분하지 않다. (출처: L11 p.23)

| 구분 | SEAr | 이 단원의 addition–elimination SNAr |
|---|---|---|
| 고리의 역할 | nucleophile | electrophile |
| 고리를 공격하는 종 | electrophile | nucleophile |
| 첫 첨가 intermediate | cation성 | anion성 |
| aromaticity 회복 시 나가는 종 | 보통 H⁺ | X⁻ |
| 이 강의에서 강조하는 활성화 | 전자를 주는 고리의 반응성 | ortho/para EWG의 음전하 안정화 |

F가 반응을 빠르게 한다는 설명은 이 활성화된 SNAr의 **느린 addition 단계에** 관한 것이다. “C–F 결합이 가장 약해서 F⁻가 쉽게 나간다”는 설명과는 반대다. 최종 치환 위치를 표시한 뒤에는 X가 Nu로 바뀌었는지, EWG는 그대로 남았는지, 고리가 다시 aromatic한지 확인한다. 염기성 조건의 nitrophenol/phenoxide 구분은 마지막 protonation 상태의 문제이며 새 C–O 결합이 생긴 위치를 바꾸지 않는다. (출처: L11 p.22–23)

## 8. 요약

> 개념 문서: [conjugate addition](../../wiki/반응/공액%20첨가.md)

- 친핵성 conjugate addition: 1,4 vs 1,2 첨가
- 유기구리 시약의 첨가: RMgBr + CuCl(촉매량)
- enolate와 enamine의 첨가: 1,5-dicarbonyl 생성물
- iminium 이온 촉매
- $\beta$ -leaving group이 있을 때의 conjugate addition → SNAr

공통 뼈대는 이렇다. Nu-가 $\beta$-탄소를 공격하면 enolate가 생긴다(공명으로 $\alpha$-탄소 anion과 같다). 이것이 H+를 받으면 enol이 되고, tautomerize하면 ketone이 된다.

(출처: L11 p.24)

---

#### 처음 보는 반응식을 읽는 순서

받개를 찾은 다음 carbonyl 또는 EWG를 기준으로 $\alpha$ 와 $\beta$ 를 먼저 표시한다. 이어 시약에서 **실제로 전달되는 원자 또는 탄소 조각을** 고른다. amine이면 N, organocuprate이면 R의 탄소, enolate/enamine이면 donor carbonyl의 $\alpha$-탄소다. 그다음 1,2/1,4와 첨가/치환을 고르고, 마지막으로 proton transfer·가수분해·추가 환원을 적용한다. (출처: L11 p.4–24)

| 답안에서 확인할 질문 | 확인 이유 |
|---|---|
| donor와 acceptor의 어느 원자가 연결되었나? | 1,2/1,4 및 donor 위치 오류 방지 |
| 중간체의 O와 N 전하가 맞나? | alkoxide·enolate·zwitterion·iminium 구분 |
| 최종 C=C와 C=O 중 무엇이 남았나? | 단순 첨가·conjugate addition·치환 구분 |
| H₂O/H₃O⁺ 뒤 carbonyl이 회복되었나? | enamine/iminium 중간체를 최종 답으로 쓰는 오류 방지 |
| 탄소 수와 고리 원자 수가 맞나? | Michael 연결·nitrile 환원·연속 고리화 검산 |

특히 **조건이 달라진 이유를 한 문장으로 설명** 해 본다. “Cu를 넣어 전달되는 탄소의 반응 성격이 달라졌다”, “가역적인 1,2 경로에서 출발물이 회복될 시간이 생겼다”, “donor enolate의 평형이 더 치환된 쪽을 선택했다”, “EWG가 addition intermediate의 음전하를 받아 준다”처럼 실제로 바뀐 대상을 말할 수 있어야 한다. 이 네 설명은 서로 다른 문제를 다루므로 하나의 “더 안정하다”로 뭉뚱그리지 않는다. (출처: L11 p.6–7,13,16,23)

## 흔한 오해

- **"Grignard 시약도 C=C에 붙는 탄소 nucleophile이므로 enone에 1,4로 간다"고 생각하기 쉽지만, 사실은** RMgBr과 RLi는 hard nucleophile이므로 주로 C=O에 1,2-첨가한다(2-cyclohexenone + MeMgBr → 1-methyl-2-cyclohexen-1-ol, 95%). 1,4로 보내려면 R2CuLi를 쓰거나 CuCl을 촉매량 넣어야 한다. (L11 p.7, p.11)
- **"CuCl을 당량만큼 넣어야 한다"고 생각하기 쉽지만, 사실은** Cu(I)가 conjugate addition 뒤에 재생되므로 0.01 eq면 충분하다. (L11 p.7)
- **"1,2 생성물은 덜 안정하니 아예 안 생긴다"고 생각하기 쉽지만, 사실은** cyanide ion 첨가에서는 저온에서 1,2(cyanohydrin)가 더 빨리 생기는 kinetic 생성물이다. 고온에서 가역 반응이 평형에 이르러야 1,4 생성물이 주로 남는다. (L11 p.13)
- **"1,4-첨가는 Nu와 H가 1번과 4번 원자에 붙어 enol로 끝난다"고 생각하기 쉽지만, 사실은** enol은 intermediate일 뿐이고 곧 tautomerize해서 최종적으로는 C=C에 Nu와 H가 붙은 포화 ketone이 된다. (L11 p.9)
- **"NaBH4는 enone의 C=O만 환원한다"고 생각하기 쉽지만, 사실은** cyclopentenone은 NaBH4/EtOH로 1,4 후 1,2가 일어나 cyclopentanol까지 간다. 반면 cinnamaldehyde는 1,2만 일어나 allyl alcohol에서 멈춘다. (L11 p.10)
- **"lithium enolate + enal이면 Michael addition"라고 생각하기 쉽지만, 사실은** Li+가 aldehyde 산소에 배위해서 고리형 transition state를 만들기 때문에 aldol(1,2) 생성물이 나온다(72%). conjugate addition을 원하면 amide·ester처럼 덜 친전자적인 받개나 안정한 enolate, enamine을 쓴다. (L11 p.15, p.16)
- **"SNAr에서도 I가 가장 좋은 leaving group"라고 생각하기 쉽지만, 사실은** SNAr에서는 F >> Cl ~ Br >> I다. 속도를 결정하는 것은 C-X 결합이 끊기는 단계가 아니라 첨가 단계다. (L11 p.23)
- **"EWG만 있으면 위치에 상관없이 SNAr가 된다"고 생각하기 쉽지만, 사실은** leaving group이 EWG의 ortho/para에 있어야 음전하가 EWG로 비편재화된다. (L11 p.23)
- **"짝지음 alkene은 electrophile이 되었으니 Br2 같은 electrophile와는 반응하지 않는다"고 생각하기 쉽지만, 사실은** $\alpha,\beta$-unsaturated carbonyl 화합물도 Br2 첨가는 (더 느리게나마) 한다. EWG는 alkene의 친핵성을 줄일 뿐 없애지 않는다. alkene과 방향족 고리의 기본 성격은 여전히 nucleophile이고, 이 강의는 예외적으로 electrophile처럼 구는 경우를 다룬다. (보충 근거: Clayden p.499, p.526)
- **"lithium enolate도 염기 조건이니 Michael 첨가에 그냥 쓰면 된다"고 생각하기 쉽지만, 사실은** Li+가 alkoxide 산소를 강하게 붙잡아 aldol 생성물을 안정화하므로 열역학 지배가 필요한 conjugate addition에는 불리하다. Na/K enolate(예: t-BuOK), 안정화된 enolate나 enamine을 사용하는 전략이 있다. 예외는 carbonyl 직접 첨가가 상대적으로 불리한 3차 amide 받개다. (보충 근거: Clayden p.607, p.610)
- **"amine은 borderline nucleophile이므로 1,4를 안 한다"고 생각하기 쉽지만, 사실은** 슬라이드 예시처럼 1차·2차 amine은 enone과 acrylate에 1,4로 첨가해서 $\beta$ -amino carbonyl을 준다. (L11 p.5, p.10)

---

## 반응 정리표

<!-- Wide source table reformatted as entries for reading; all cells retained. -->

### thiol 첨가

- 시약/조건: mesityl oxide + PhSH, 25 °C, 5 h
- 생성물: (CH3)2C(SPh)CH2COCH3 (94%)
- regioselectivity: 1,4
- 입체화학: 해당 없음
- 비고: soft nucleophile (p.4)

### 시안화 첨가

- 시약/조건: chalcone + -CN, EtOH, HOAc
- 생성물: PhCH(CN)CH2COPh (95%)
- regioselectivity: 1,4
- 입체화학: 새 입체중심, 라세미(보충)
- 비고: (p.4)

### amine 첨가

- 시약/조건: mesityl oxide + MeNH2, H2O
- 생성물: (CH3)2C(NHMe)CH2COCH3 (75%)
- regioselectivity: 1,4
- 입체화학: 해당 없음
- 비고: zwitterion → enol → ketone (p.5)

### cuprate 제조

- 시약/조건: CuBr + 2 RLi, Et2O, -78 °C
- 생성물: R2CuLi + LiBr
- regioselectivity: –
- 입체화학: –
- 비고: 불안정, 즉시 사용 (p.6)

### Cu catalyst Grignard addition

- 시약/조건: isophorone + MeMgBr, CuCl 0.01 eq, Et2O
- 생성물: 3,3,5,5-tetramethylcyclohexanone (83%)
- regioselectivity: 1,4
- 입체화학: 해당 없음
- 비고: 금속 교환, Cu 재순환. CuCl 없으면 1,2 (p.6–7)

### Grignard/organolithium

- 시약/조건: 2-cyclohexenone + CH3MgBr 또는 CH3Li; H3O+
- 생성물: 1-methylcyclohex-2-en-1-ol (95%)
- regioselectivity: 1,2
- 입체화학: –
- 비고: hard nucleophile (p.11)

### cuprate

- 시약/조건: 2-cyclohexenone + (CH3)2CuLi; H3O+
- 생성물: 3-methylcyclohexanone (97%)
- regioselectivity: 1,4
- 입체화학: –
- 비고: soft nucleophile (p.11)

### acyl chloride + NH3

- 시약/조건: CH2=CHCOCl + NH3
- 생성물: CH2=CHCONH2
- regioselectivity: 1,2(acyl 치환)
- 입체화학: –
- 비고: (p.10)

### acrylate + NH3

- 시약/조건: CH2=CHCO2Me + NH3
- 생성물: H2NCH2CH2CO2Me
- regioselectivity: 1,4
- 입체화학: –
- 비고: (p.10)

### enal 환원

- 시약/조건: cinnamaldehyde + NaBH4, EtOH
- 생성물: cinnamyl alcohol (97%)
- regioselectivity: 1,2
- 입체화학: –
- 비고: (p.10)

### 고리 enone 환원

- 시약/조건: cyclopentenone + NaBH4, EtOH
- 생성물: cyclopentanol (99%)
- regioselectivity: 1,4 후 1,2
- 입체화학: –
- 비고: (p.10)

### HCN addition(저온)

- 시약/조건: MVK + NaCN, HCN, 5–10 °C
- 생성물: cyanohydrin
- regioselectivity: 1,2
- 입체화학: –
- 비고: kinetic, 가역 (p.13)

### HCN addition(고온)

- 시약/조건: MVK + NaCN, HCN, 80 °C
- 생성물: NCCH2CH2COCH3
- regioselectivity: 1,4
- 입체화학: –
- 비고: thermodynamic (p.13)

### enolate Michael

- 시약/조건: cyclohexanone + LDA; (E)-CH3CH=CHCONMe2
- 생성물: 1,5-ketoamide (60%)
- regioselectivity: 1,4
- 입체화학: 표시 없음
- 비고: amide 받개 (p.15)

### lithium enolate + enal

- 시약/조건: ethyl isobutyrate + LDA, -78 °C, THF; (CH3)2C=CHCHO
- 생성물: $\beta$ -hydroxy ester (72%)
- regioselectivity: 1,2(aldol)
- 입체화학: –
- 비고: Li+ 배위, 고리형 TS (p.16)

### thermodynamic enolate Michael

- 시약/조건: 2-methylcyclopentanone + methyl acrylate, t-BuOK
- 생성물: 2-Me-2-(CH2CH2CO2Me)cyclopentanone (53%)
- regioselectivity: 1,4
- 입체화학: 4차 탄소
- 비고: 더 치환된 쪽에서 반응 (p.16)

### malonic ester Michael

- 시약/조건: CH2(CO2Et)2 + ethyl crotonate, NaOEt, EtOH, reflux
- 생성물: (EtO2C)2CHCH(CH3)CH2CO2Et
- regioselectivity: 1,4
- 입체화학: –
- 비고: 안정한 enolate (p.17)

### nitroalkane Michael

- 시약/조건: PhCH2NO2 + 2-cyclohexenone, Al2O3, neat
- 생성물: 3-(CH(Ph)NO2)cyclohexanone (92%)
- regioselectivity: 1,4
- 입체화학: –
- 비고: (p.17)

### Michael-분자 내 alkylation

- 시약/조건: I(CH2)4CH=CHCO2Me + CH3NO2, Cs2CO3, DMF
- 생성물: methyl 2-(2-nitrocyclohexyl)acetate (65%)
- regioselectivity: 1,4 후 SN2 고리화
- 입체화학: 표시 없음
- 비고: (p.17)

### enamine alkylation

- 시약/조건: cyclohexanone + pyrrolidine(cat. H+); R-X; H2O, H+
- 생성물: 2-R-cyclohexanone
- regioselectivity: $\alpha$ -alkylation
- 입체화학: –
- 비고: (p.18)

### enamine Michael

- 시약/조건: pyrrolidine enamine + CH2=C(SMe)CO2Me, MeCN; H2O
- 생성물: 1,5-dicarbonyl (95%)
- regioselectivity: 1,4
- 입체화학: –
- 비고: (p.19)

### enamine Michael

- 시약/조건: morpholine enamine + CH2=C(SO2Ph)COCH3, SiO2, THF; H2O
- 생성물: 1,5-diketone (75%)
- regioselectivity: 1,4
- 입체화학: –
- 비고: (p.19)

### iminium 촉매

- 시약/조건: enal + pyrrole, imidazolidinone 20 mol%
- 생성물: $\beta$ -pyrrole릴 aldehyde (68–90%)
- regioselectivity: 1,4
- 입체화학: 87–97% ee, crotonaldehyde 예에서 (R)
- 비고: benzyl group 반대면 공격 (p.21)

### $\beta$ -leaving group 치환

- 시약/조건: 2-F-cyclohexenyl methyl ketone + R2NH
- 생성물: $\beta$-아미노 enone
- regioselectivity: $\beta$-위치 치환
- 입체화학: –
- 비고: 첨가-제거 (p.22)

### SNAr

- 시약/조건: o-F-acetophenone + R2NH
- 생성물: o-NR2-acetophenone
- regioselectivity: ipso 치환
- 입체화학: –
- 비고: ortho EWG (p.23)

### SNAr

- 시약/조건: p-Cl-nitrobenzene + HO-
- 생성물: p-nitrophenol
- regioselectivity: ipso 치환
- 입체화학: –
- 비고: para EWG (p.23)

---

## 연습 문제

**문제 1** (p.8) 분자 간 유기구리 conjugate addition만 써서 다음 화합물을 만드는 방법(출발 enone + cuprate)을 제시하라.
(a) 2-heptanone CH3CH2CH2CH2CH2COCH3
(b) 3,3-dimethylcyclohexanone
(c) 3-ethyl-4-tert-butylcyclohexanone
(d) 4a-vinyl-octahydronaphthalene-2(1H)-온(고리 접합 탄소에 CH=CH2가 있고, 그 탄소가 C=O의 $\beta$ 위치인 데칼론)

**문제 2** (p.11) 2-cyclohexenone을 (i) CH3MgBr로 처리한 뒤 H3O+로, (ii) (CH3)2CuLi로 처리한 뒤 H3O+로 처리했을 때의 주생성물을 각각 쓰고, 차이를 hard/soft 개념으로 설명하라.

**문제 3** (p.13) methyl vinyl ketone에 NaCN/HCN을 5–10 °C와 80 °C에서 반응시켰을 때의 생성물을 쓰고, 어느 쪽이 kinetic·thermodynamic 생성물인지 결합 에너지로 설명하라.

**문제 4** (p.14 빈칸) ketone R1COCH3의 enolate가 Michael 받개 CH2=CH-COR2에 첨가할 때, 빈칸에 들어갈 intermediate와 protonation 후 최종 생성물을 쓰라.

**문제 5** (p.16) 2-methylcyclopentanone과 methyl acrylate를 t-BuOK로 반응시키면 새 결합이 C2(methyl이 붙은 탄소)에 생긴다. 이유를 설명하라.

**문제 6** (p.19 빈칸) cyclohexanone의 morpholine enamine과 ethyl (E)-3-nitroacrylate(EtO2C-CH=CH-NO2)를 반응시킨 뒤 H2O로 처리했을 때의 생성물을 예측하라.

**문제 7** (p.20 빈칸) ethyl 2-(2,5-dimethoxyphenyl)acetate에서 1-propyl-3-(2,5-dimethoxyphenyl)piperidine까지 가는 경로에서 (i) acrylonitrile/Triton B 처리 생성물, (ii) H2/Pd/C 처리 생성물(과 그 뒤 일어나는 일)을 쓰고, (iii) 마지막 "alkylation and reduction" 단계를 설명하라.

**문제 8** (p.23) 4-chloronitrobenzene은 HO-와 SNAr로 쉽게 반응하지만 3-chloronitrobenzene은 그렇지 않다. 이유를 설명하고, leaving group 반응성 순서가 SN2와 다른 이유도 쓰라.

---

## 정답 및 해설

**문제 1**
- (a) **methyl vinyl ketone(CH2=CH-CO-CH3) + (CH3CH2CH2)2CuLi** . MVK의 $\beta$-탄소(말단 CH2)에 propyl이 붙으면 Pr-CH2-CH2-CO-CH3 = CH3(CH2)4COCH3가 된다. 거꾸로 CH3CH=CH-COCH3 + Et2CuLi로 하면 가지 달린 CH3CH(Et)CH2COCH3가 나오므로 틀린 답이다.
- (b) **3-methyl-2-cyclohexenone + (CH3)2CuLi** . 이미 Me가 있는 $\beta$-탄소(C3)에 Me가 하나 더 붙어 gem-dimethyl이 된다(isophorone → 3,3,5,5-tetramethylcyclohexanone 예시와 같은 원리, p.6–7).
- (c) **4-tert-butyl-2-cyclohexenone + (CH3CH2)2CuLi** . ethyl이 C3( $\beta$ )에 있으므로 ethyl이 nucleophile이어야 한다. tBu는 C4( $\gamma$ )에 있으니 출발물에 이미 있어야 한다. 3-ethylcyclohexenone + tBu2CuLi로는 tBu가 C3에 붙으므로 안 된다. 보충: 일반적으로 cuprate는 tBu 반대면으로 주로 들어가서 trans 이성질체가 우세하지만, 슬라이드는 입체화학을 묻지 않는다.
- (d) **$\Delta^{1(8a)}$-옥탈론(4,4a,5,6,7,8-hexahydronaphthalen-2(3H)-one, 고리 접합 탄소가 $\beta$-탄소인 이고리 enone) + (CH2=CH)2CuLi** . vinyl기가 고리 접합 $\beta$-탄소에 붙어 4차 탄소가 생긴다. vinyl cuprate도 R2CuLi의 일종이다.
(근거: L11 p.6–8, p.11)

**문제 2**
(i) 1-methylcyclohex-2-en-1-ol(1,2-첨가, 95%). (ii) 3-methylcyclohexanone(1,4-첨가, 97%). C-Mg 결합은 분극이 커서 탄소가 hard nucleophile이 되고, hard electrophilic site인 carbonyl 탄소를 공격한다. Cu(1.9)는 Mg(1.3)보다 전기음성도가 커서 C-Cu 결합의 분극이 작다. 그래서 cuprate는 soft nucleophile로서 $\beta$-탄소를 공격한다. (근거: L11 p.6, p.11, p.12)

**문제 3**
5–10 °C에서는 cyanohydrin CH2=CH-C(OH)(CN)CH3(1,2, kinetic 생성물 P1, 가역)이 생긴다. 80 °C에서는 NC-CH2CH2-CO-CH3(1,4, thermodynamic 생성물 P2)이 생긴다. 1,2-첨가의 활성화 에너지가 더 낮아 저온에서 빨리 생긴다. 하지만 1,2는 C=O $\pi$ (약 369 kJ/mol)를 잃고 1,4는 더 약한 C=C $\pi$ (약 280 kJ/mol)를 잃으므로(둘 다 C-C $\sigma$ 를 얻음), 1,4 생성물이 더 안정하다. 고온에서는 1,2-첨가가 되돌려지므로 평형이 안정한 P2 쪽으로 이동한다. (근거: L11 p.13)

**문제 4**
enolate의 $\alpha$-탄소가 받개의 $\beta$-탄소를 공격하면 새 enolate intermediate R1-CO-CH2-CH2-CH=C(O-)-R2가 생긴다. 이것이 protonation(그리고 tautomerization)되면 **1,5-dicarbonyl 화합물 R1-CO-CH2CH2CH2-CO-R2가** 된다. (근거: L11 p.14, p.24 요약 "1,5-dicarbonyl products")

**문제 5**
t-BuOK 조건에서는 deprotonation이 가역적이라서 두 enolate가 평형을 이룬다. 평형에서는 C=C가 더 많이 치환된 thermodynamic enolate(C1=C2, C2에 Me)가 우세하다. 그래서 C2가 methyl acrylate의 $\beta$-탄소를 공격해 4차 탄소를 가진 methyl 3-(1-methyl-2-oxocyclopentyl)propanoate(53%)가 생긴다. (근거: L11 p.16)

**문제 6**
**ethyl 3-nitro-2-(2-oxocyclohexyl)propanoate** , 즉 (2-oxocyclohexyl)-CH(CO2Et)-CH2NO2다. 받개에는 EWG가 두 개 있다. nitro group이 ester보다 훨씬 강한 EWG이므로 nitro group을 기준으로 한 $\beta$-탄소, 즉 CO2Et가 붙은 탄소가 공격을 받는다. 그러면 음전하는 nitronate로 안정화된다. 그 뒤 H2O 처리로 iminium이 가수분해되어 ketone이 돌아온다. 보충: 슬라이드에는 이 칸의 답이 없다. 위 답은 "더 강한 EWG가 regioselectivity를 정한다"는 원리(Clayden 2판 25장)에 따른 예측이다(보충 근거: Clayden p.611). (근거: L11 p.19, p.23의 EWG 세기 순서 NO2 > ... > COMe)
**문제 7**
- (i) ester $\alpha$ -H가 deprotonate되고, 그 enolate가 acrylonitrile의 $\beta$-탄소에 conjugate addition한다. 생성물은 **ethyl 4-cyano-2-(2,5-dimethoxyphenyl)butanoate** , Ar-CH(CO2Et)-CH2CH2-CN이다.
- (ii) H2/Pd/C로 nitrile이 1차 amine으로 환원되어 Ar-CH(CO2Et)-CH2CH2CH2-NH2가 된다. 이 amine이 같은 분자의 ester를 분자 내에서 공격해서(EtOH가 빠짐) 6원자 lactam **3-(2,5-dimethoxyphenyl)piperidin-2-one이** 생긴다. 보충: 슬라이드 빈칸에 lactam까지 그려져 있는지는 확인할 수 없다. 하지만 최종 생성물의 고리가 N-CH2-CH2-CH2-CH(Ar)-CH2 구조이므로, lactam C=O 탄소가 최종 생성물에서 N 옆 CH2가 된다는 것과 일치한다. Clayden도 같은 경로에서 이 lactam 고리화가 저절로 일어난다고 설명한다(보충 근거: Clayden p.612).
- (iii) lactam 질소를 propyl group으로 alkylation(N-propyl)하고, amide C=O를 CH2로 환원(보충: 보통 LiAlH4 사용, 보충 근거: Clayden p.236)하면 1-propyl-3-(2,5-dimethoxyphenyl)piperidine이 된다.
(근거: L11 p.20)

**문제 8**
4-chloronitrobenzene에서는 HO-가 C-Cl 탄소에 첨가할 때 생긴 음전하가 공명으로 NO2가 붙은 탄소, 나아가 nitro group 산소까지 퍼진다. 그래서 $\sigma$ 착물이 안정화된다. meta 이성질체에서는 음전하가 NO2가 붙은 탄소에 오지 않아 이런 안정화가 없다. 그래서 leaving group은 EWG의 ortho/para에 있어야 한다. leaving group 순서가 F >> Cl ~ Br >> I인 것은 SNAr의 속도 결정 단계가 C-X가 끊기는 단계가 아니라 첫 번째 첨가 단계이기 때문이다. 전기음성도가 가장 큰 F가 ipso 탄소를 가장 강하게 $\delta^{+}$ 로 만들고 anion성 intermediate를 안정화하므로 첨가가 가장 빠르다(보충, Clayden 22장) (보충 근거: Clayden p.518). (근거: L11 p.22, p.23)

---

## 각주

[^1]: 보충: amine의 conjugate addition은 가역적이다. amine은 carbonyl에 1,2로도 첨가할 수 있지만 그 생성물(hemiaminal)은 쉽게 되돌아간다. 그래서 결국 안정한 1,4 생성물이 쌓인다. 3.3절의 kinetic/thermodynamic 논리와 같은 구도다. (보충 근거: Clayden p.582)

[^2]: 엄밀히 말하면 이 반응은 C=O에 1,2로 첨가한 뒤 Cl-가 떨어지는 친핵성 acyl 치환(첨가-제거)이다. 슬라이드는 첫 공격 위치를 기준으로 "1,2"라고 분류했다.

[^3]: 슬라이드 표의 경계 칸에 "CH-"라고 적혀 있는데, 무엇을 뜻하는지 슬라이드만으로는 분명하지 않다. CN-의 오타일 가능성이 있다. 다만 일반적인 HSAB 표에서 CN-는 보통 soft base로 분류된다. 실제로 p.13에서 CN-는 조건에 따라 1,2와 1,4를 모두 보인다. 보충: 슬라이드 표는 Clayden 22장의 표와 칸 배치가 같은데, Clayden 표의 경계 칸에는 "N3–, CN–"가 적혀 있다. 따라서 "CH-"는 CN-의 오타로 보는 것이 자연스럽고, 이 강의의 맥락에서는 CN-를 경계 nucleophile로 읽으면 된다(p.13의 이중적 거동과도 맞는다). 또 Clayden 표는 hard 칸에 NH3와 SO4^2-를 더 싣고 있다. (보충 근거: Clayden p.507)

[^4]: 엄밀하게는 슬라이드 그림에 있는 것은 2차 amine 유래의 **iminium 이온과** enamine이다. 둘은 양성자 하나를 주고받는 deprotonation/protonation 관계다. 중성 imine-enamine tautomer 관계는 1차 amine에서 생기는 N-H imine에 해당한다(→ [L10](L10_Enol_and_Enamine.md) 문서 참고).

[^5]: 슬라이드에 따르면 dopamine 길항제는 조현병, 양극성 장애, 자극제 유발 정신병 치료에 쓰여 왔다.

[^6]: 보충: 이 반응은 MacMillan의 organocatalysis 연구로 알려진 imidazolidinone 촉매 계열이다. MacMillan은 비대칭 유기 촉매 개발 공로로 2021년 노벨 화학상(List와 공동)을 받았다. 슬라이드에는 노벨상 언급이 없다.

[^7]: 슬라이드 intermediate에는 질소가 "R2N"으로 그려져 있다. 하지만 중성 R2NH가 첨가한 직후의 질소는 R2NH+(양전하)이고, 이후 양성자를 잃어 R2N이 된다.

[^8]: 보충: 이 anion성 sigma 착물은 흔히 마이젠하이머 Meisenheimer complex이라 부른다.

[^9]: 보충: F-가 이탈 능력 자체가 뛰어나서가 아니다. 느린 단계가 첨가이기 때문에 전기음성도가 큰 F가 ipso 탄소를 활성화하고 anion intermediate를 안정화해서 전체 속도를 높인다(Clayden 22장) (보충 근거: Clayden p.518). 슬라이드의 "F is the best leaving group"은 "SNAr 속도가 가장 빠른 할로젠"으로 읽는 것이 정확하다.

[^10]: 슬라이드 생성물은 4-nitrophenol(HO-Ar)로 그려져 있다. 엄밀히는 염기성 조건에서 산성인 nitrophenol(pKa 약 7)이 deprotonate되어 phenoxide로 존재하고, 산 처리 후 phenol이 얻어진다(보충). (보충 근거: Clayden p.176)
