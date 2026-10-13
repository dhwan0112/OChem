# L5 연습 문제와 해설

> [L5 환원 강의 노트](../notes/L05_Reduction.md)에서 옮긴 연습 문제와 해설이다. 문제 옆의 p.는 L5 슬라이드 PDF 쪽이다. 개념 설명은 [amine synthesis (overview)](../wiki/개념/아민%20합성%20개관.md), [reductive amination](../wiki/반응/환원성%20아미노화.md), [amide reduction](../wiki/반응/아마이드%20환원.md), [Eschweiler–Clarke reaction](../wiki/반응/에슈바일러-클라크%20반응.md), [metal hydride의 반응성](../wiki/개념/금속%20수소화물의%20반응성.md), [NaBH3CN](../wiki/시약/NaBH3CN.md), [LiBH4](../wiki/시약/LiBH4.md), [LiAlH4](../wiki/시약/LiAlH4.md), [borane](../wiki/시약/보레인.md), [partial reduction of esters](../wiki/반응/에스터%20부분%20환원.md), [Rosenmund reduction](../wiki/반응/로젠문트%20환원.md), [hydrogenolysis](../wiki/반응/수소화분해.md) 문서에 있다.

## 문제

1. (p.13) N-methyl-2-phenylethanamine PhCH<sub>2</sub>CH<sub>2</sub>NHCH<sub>3</sub>를 어떻게 합성하겠는가? 두 가지 이상의 경로를 제시하라.
2. (p.14) 거미 독소 전구체 합성에서 fragment 1의 aldehyde(...CH<sub>2</sub>CHO)와 fragment 2의 1차 amine(H<sub>2</sub>N-CH<sub>2</sub>...)을 NaCNBH<sub>3</sub>(20 °C, 2 h)로 연결하여 2차 amine(48%)을 얻었다. 같은 생성물을 주는 다른 amine/aldehyde 조합을 제안하라. 또 이 연결에 H<sub>2</sub>, Pd/C를 쓰기 어려운 이유는?
3. (p.16) venlafaxine 합성에서 1-[사이아노(4-methoxyphenyl)methyl]cyclohexanol을 H<sub>2</sub>, 5% Rh/Al<sub>2</sub>O<sub>3</sub>로 처리한 생성물(빈 상자 1)과, 이를 HCHO/HCOOH, reflux로 처리한 최종 생성물(빈 상자 2)을 쓰라. H<sub>2</sub>/Pd-C/HCHO 한 단계 경로에서는 어떤 반응들이 연속으로 일어나는가?
4. (p.17) reductive amination에 NaBH<sub>4</sub> 대신 NaBH<sub>3</sub>CN을 쓰는 이유는?
5. (p.25) 3β-acetoxy-steroid-20-온(C3에 acetate ester, C17 측쇄에 methyl ketone C(=O)CH<sub>3</sub>)을 (a) NaBH<sub>4</sub>, (b) LiBH<sub>4</sub>로 처리한 생성물은?
6. (p.26) methoxy aryl기, 고리형 ether, 고리형 enone(C=C-C=O), N-methyl lactam을 가진 다고리 화합물을 LiAlH<sub>4</sub>, THF(70%)로 처리할 때 각 작용기는 어떻게 되는가?
7. (p.29) ethyl 2-(furan-2-일)propanoate를 2-(furan-2-일)propanal(항생제 monensin 합성 intermediate)로 바꾸는 방법을 DIBAL 외에 제시하라.
8. (p.22, p.27) MeO<sub>2</sub>C-CH<sub>2</sub>CH(CH<sub>3</sub>)CH<sub>2</sub>-CO<sub>2</sub>H를 (a) LiBH<sub>4</sub>/EtOH, (b) BH<sub>3</sub>·THF로 각각 처리한 생성물과 그 이유는?

## 정답 및 해설

1. **경로 A (amide 환원, p.9)**: `PhCH2COOH --[1. SOCl2; 2. CH3NH2]--> PhCH2CONHCH3 --[1. LiAlH4; 2. H2O]--> PhCH2CH2NHCH3`. amide C=O가 CH<sub>2</sub>가 된다.
   **경로 B (reductive amination, p.10-12)**: `PhCH2CHO + CH3NH2 --[NaBH3CN, 약산성]--> PhCH2CH2NHCH3`. 새 C-N 결합의 탄소 쪽(CH<sub>2</sub>)이 aldehyde에서 온다.
   **경로 C**: 2-phenylethylamine(p.7의 azide 경로)을 formylation(예: HCOOEt)해 N-포밀 amide PhCH<sub>2</sub>CH<sub>2</sub>NHCHO로 만든 뒤 LiAlH<sub>4</sub>로 환원하면 NHCH<sub>3</sub>가 된다.
   함정: PhCH<sub>2</sub>CH<sub>2</sub>Br + CH<sub>3</sub>NH<sub>2</sub> 직접 alkylation은 over-alkylation 위험(p.6)이 있고, Eschweiler–Clarke는 N,N-dimethyl까지 가므로 monomethyl 합성에 맞지 않는다(p.15).

2. 생성물의 2차 amine N 양쪽이 모두 CH<sub>2</sub>이므로, 어느 쪽 C-N 결합이든 reductive amination으로 만들 수 있다. 대안은 **fragment 1 쪽을 1차 amine**(원래 CHO 탄소가 CH<sub>2</sub>NH<sub>2</sub>가 된 ...CH<sub>2</sub>CH<sub>2</sub>NH<sub>2</sub>)으로, **fragment 2 쪽을 aldehyde**(원래 H<sub>2</sub>N-CH<sub>2</sub>-가 OHC-로 바뀐 OHC-CH<sub>2</sub>CH<sub>2</sub>-N(Cbz)...)로 바꾸어 NaCNBH<sub>3</sub>로 연결하는 것이다. 전체 탄소 수는 그대로다.
   H<sub>2</sub>/Pd-C가 어려운 이유: 분자에 OBn(benzyl ether)과 Cbz(benzyloxycarbonyl)가 많아 hydrogenation 조건에서 benzyl group이 떨어져 나갈 수 있다(p.33 "deprotection of benzyl group"). NaCNBH<sub>3</sub>는 이들을 건드리지 않는다.

3. 빈 상자 1: nitrile이 1차 amine으로 수소화된 **1-[2-amino-1-(4-methoxyphenyl)ethyl]cyclohexanol** (4-MeOC<sub>6</sub>H<sub>4</sub>-CH(CH<sub>2</sub>NH<sub>2</sub>)-C(OH)(cyclohexane 고리)), 57%.
   빈 상자 2: Eschweiler–Clarke로 NH<sub>2</sub>가 N(CH<sub>3</sub>)<sub>2</sub>가 된 **venlafaxine** 1-[2-(dimethylamino)-1-(4-methoxyphenyl)ethyl]cyclohexanol (HCl 염, 80%).
   한 단계 경로: (i) C≡N hydrogenation으로 CH<sub>2</sub>NH<sub>2</sub>, (ii) HCHO와 imine 형성 후 H<sub>2</sub>/Pd 환원으로 NHCH<sub>3</sub>, (iii) 다시 HCHO와 iminium 형성 후 환원으로 N(CH<sub>3</sub>)<sub>2</sub>. HCHO 2.2 eq는 methyl group 두 개분이다. (출처: L5 p.15-16)

4. NaBH<sub>4</sub>는 aldehyde/ketone을 빠르게 환원하므로(p.17 표) imine이 생기기 전에 carbonyl을 alcohol로 바꿔 버린다. 또 imine 형성에 필요한 산성 조건에서 분해되어 H<sub>2</sub>를 낸다. NaBH<sub>3</sub>CN은 aldehyde/ketone을 느리게만 환원하고(p.17 표의 "느림") imine은 환원하며, pH > 3 수용액에서도 안정하다(p.17). 그래서 carbonyl, amine, 환원제를 한 용기에 넣어도 된다. 보충: 전자를 끄는 CN기 때문에 B-H의 hydride 공여력이 약해지고, 더 친전자적인 protonation iminium만 빠르게 환원된다. (보충 근거: Clayden p.234)

5. (a) NaBH<sub>4</sub>: ketone만 환원된다. C20이 2차 alcohol CH(OH)CH<sub>3</sub>가 되고 **3β-acetate는 남는다**. NaBH<sub>4</sub>는 ester를 매우 느리게만 환원한다(p.17, p.21).
   (b) LiBH<sub>4</sub>: ketone과 ester가 모두 환원된다(p.22). C20 alcohol과 함께 acetate가 환원되어 **C3의 3β-OH가 드러난 diol**이 되고, acetyl 부분은 ethanol로 떨어져 나간다. 끊어지는 것은 acyl C-O 결합이므로 C3의 β 배향은 유지된다. C20에 새 stereocenter가 생기지만 슬라이드에 배향이 지정되어 있지 않다.

6. LiAlH<sub>4</sub>는 강한 환원제다(p.17). **lactam(고리형 amide)의 C=O는 CH<sub>2</sub>가 되어** N-methyl 고리형 3차 amine이 된다. **enone의 C=O는 2차 alcohol**(allyl alcohol)이 된다. 보충: LiAlH<sub>4</sub>는 enone을 주로 1,2-환원하므로 C=C는 남는다(1,4-첨가와의 비교는 → [1,2-addition vs 1,4-addition](../wiki/개념/1,2-첨가와%201,4-첨가.md)). aryl methyl ether와 고리형 ether는 변하지 않는다. 보충: 3-methoxy, 4,5-에폭시 고리, N-methyl, 6-OH, 7,8-이중결합의 조합은 morphine 계열(morphinan, codeine 유사) 골격에 해당한다. 새 C-OH stereocenter의 배향은 슬라이드에 제시되지 않았다.

7. **alcohol 경유(p.17 "via alcohol")**: `ester --[1. LiAlH4 (또는 LiBH4); 2. H2O]--> 2-(furan-2-일)propane-1-ol --[온화한 산화: Swern, PCC, Dess–Martin 등]--> 2-(furan-2-일)propanal`. 1차 alcohol을 carboxylic acid까지 과산화하지 않는 산화제를 골라야 한다(→ [alcohol oxidation](../wiki/반응/알코올%20산화.md)).
   **acid chloride 경유(p.17, p.33)**: ester 가수분해 → carboxylic acid → SOCl<sub>2</sub> → acid chloride → H<sub>2</sub>, Pd/BaSO<sub>4</sub>, quinoline(Rosenmund) → aldehyde.

8. (a) LiBH<sub>4</sub>: ester만 환원되어 **HOCH<sub>2</sub>CH<sub>2</sub>CH(CH<sub>3</sub>)CH<sub>2</sub>CO<sub>2</sub>H** (5-hydroxy-3-methylpentanoic acid). LiBH<sub>4</sub>는 산 존재하에 ester를 선택 환원한다(p.22). 산은 deprotonate되어 반응성 최하위인 carboxylate(p.18)가 된다.
   (b) BH<sub>3</sub>: 산만 환원되어 **MeO<sub>2</sub>CCH<sub>2</sub>CH(CH<sub>3</sub>)CH<sub>2</sub>CH<sub>2</sub>OH** (methyl 5-hydroxy-3-methylpentanoate). BH<sub>3</sub>는 Lewis 산이라 전자가 풍부한 carboxylic acid/amide를 선택 환원하고, Lewis 염기성이 약한 ester는 느리다(p.27-28).
