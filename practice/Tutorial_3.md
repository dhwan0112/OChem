# Tutorial 3: 엔올레이트의 형성·알킬화·알돌 반응

> 출처: Tutorial_Questions_3.pdf (문제), Tutorial_3_answers.pdf (공식 풀이, 손글씨). CM3121 Advanced Organic Chemistry (Dr. Zhu Ye)

---

## 문제 1

다음 반응의 intermediate와 생성물을 제시하라.

`화합물 1 --[PPh3, NEt3, THF, reflux, 2시간]--> 2`

- 화합물 1: 2-(4-methoxyphenyl)-2-oxoethyl 2-bromoacetate, 즉 4-MeO-C6H4-CO-CH2-O-CO-CH2Br (펜아실 bromoacetate, phenacyl bromoacetate).

### 공식 풀이

1. `1 --[PPh3]--> 4-MeO-C6H4-CO-CH2-O-CO-CH2-P⁺Ph3 Br⁻` (phosphonium 염, phosphonium salt)
2. `--[NEt3, -HBr]--> 4-MeO-C6H4-CO-CH2-O-CO-CH⁻-P⁺Ph3` (ylide, ylide)
3. `--[비티히 반응(Wittig reaction)]--> 2`
- 2: 4-(4-methoxyphenyl)퓨란-2(5H)-온, 즉 5원 락톤 고리 O-CH2-C(Ar)=CH-C(=O) (butenolide, butenolide).

(출처: Tutorial_3_answers p.1)

### 해설

이 문제의 핵심은 왜 약한 염기인 NEt3만으로 ylide가 만들어지고, 왜 그것이 분자 안의 ketone과 반응하여 고리를 닫는가이다.

먼저 PPh3는 좋은 nucleophile이고 C-Br은 ester carbonyl에 이웃한 $\alpha$-할로 ester 탄소이므로 SN2가 특히 빠르다. 그래서 phosphonium 염이 생긴다. 그런데 이 P⁺-CH2 수소는 양전하를 띤 인과 ester carbonyl 양쪽에 이웃해 있다. 즉 deprotonation으로 생긴 탄소 anion이 ester enolate처럼 carbonyl로 비편재화되어 안정화된다(→ [L7](../notes/L07_Enolate_Alkylation.md) enolate 문서 참고). 이런 "안정화된 ylide(stabilized ylide)"는 산성이 충분히 강하므로 BuLi 같은 강염기 없이 NEt3로도 만들어진다.

이제 ylide 탄소는 nucleophile이 되어 같은 분자의 아릴 ketone carbonyl을 공격한다. 고리를 세어 보면 ylide C, ester C(=O), O, CH2, ketone C로 5원 고리이므로 분자 내 반응이 유리하다. 그 뒤 oxaphosphetane을 거쳐 강한 P=O 결합을 가진 Ph3P=O가 빠져나가면서 C=C가 생긴다. 그래서 생성물은 C=C가 락톤 carbonyl과 짝을 이룬 $\alpha,\beta$-unsaturated $\gamma$-락톤, 즉 butenolide이다. 안정화된 ylide는 보통 ketone과 잘 반응하지 않지만, 여기서는 분자 내 반응이고 환류 조건이므로 진행된다.

### 핵심 개념

$\alpha$-할로 ester + PPh3 → phosphonium 염 → (약염기) 안정화 ylide → 분자 내 비티히로 butenolide 형성.

---

## 문제 2

다음 화합물로부터 해당하는 enolate를 제시하라. enolate가 형성되지 않으면 NA라고 답하라.

- (3) `PhCO-CH=CH-CH3` (크로토노페논, (E)-1-phenyl뷰트-2-ene-1-one) `--[LDA]-->`
- (4) `PhCO-CH=CH2` (1-phenyl프로프-2-ene-1-one, phenyl 비닐 ketone) `--[LDA]-->`
- (5) methyl 2-(시아노메틸)benzoate, 즉 benzene 고리 오르토 위치에 CO2Me와 CH2CN `--[LDA]-->`

### 공식 풀이

- 3: $\gamma$-methyl의 H를 떼어 낸 확장 enolate(dienolate). 세 공명 구조를 표시: $\gamma$-탄소 anion PhCO-CH=CH-CH2⁻ ↔ $\alpha$-탄소 anion PhCO-CH⁻-CH=CH2 ↔ 산소 anion PhC(O⁻)=CH-CH=CH2.
- 4: NA. $\alpha$-수소가 sp2 탄소(비닐 C-H)에 있다고 표시.
- 5: CH2CN의 H를 떼어 낸 탄소 anion Ar-CH⁻-CN ↔ keteneimine anion(ketenimine anion) Ar-CH=C=N⁻.

(출처: Tutorial_3_answers p.1)

### 해설

이 문제의 핵심은 "carbonyl 옆에 H가 있다"는 것만으로 enolate가 생기는가, 아니면 그 H를 떼어 냈을 때 생기는 anion이 $\pi$계와 겹쳐 비편재화될 수 있어야 하는가이다. 답은 후자이다(→ [L7](../notes/L07_Enolate_Alkylation.md) enolate 문서 참고).

화합물 3은 carbonyl과 C=C가 짝을 이룬 enone이다. 그런데 $\alpha$-탄소(C2)는 sp2이고 그 H는 $\pi$계와 수직인 $\sigma$ 평면에 놓여 있어서, 떼어 내도 anion이 carbonyl과 짝을 이룰 수 없다. 대신 $\gamma$-methyl의 sp3 C-H는 C=C-C=O $\pi$계와 겹칠 수 있다. 그래서 LDA는 $\gamma$-H를 떼어 내고, 음전하는 $\gamma$-C, $\alpha$-C, O에 걸쳐 비편재화된 확장 enolate(extended enolate, dienolate)가 생긴다. 이것을 vinylogous deprotonation라 한다. 반대쪽은 phenyl이므로 $\alpha$'-수소가 없다.

화합물 4는 같은 enone이지만 $\gamma$-탄소가 없다. 남은 C-H는 모두 sp2 비닐 C-H이고, 이것을 떼어 내면 음전하가 sp2 오비탈에 갇혀 carbonyl로 비편재화되지 않는다. 즉 안정화된 enolate가 생길 수 없으므로 답은 NA이다.

화합물 5에서는 CH2CN의 수소가 benzyl 위치이면서 nitrile의 $\alpha$-위치이다. 그래서 탄소 anion은 C≡N으로 비편재화되어 keteneimine anion 형태가 되고, benzene 고리 쪽으로도 안정화된다. 여기서 "enolate"는 엄밀히는 nitrile 안정화 탄소 anion(nitrile anion)이다. ester의 methyl(OMe)은 산성 H가 아니고, LDA는 부피가 커서 친핵성이 낮으므로 ester carbonyl을 공격하지 않는다.

검토 의견: 공식 답은 옳다. 덧붙이면 화합물 5의 benzyl anion은 고리를 통해 오르토 위치의 ester carbonyl까지 비편재화될 수 있으므로, 공식 풀이에 그려진 두 공명 구조 외에도 고리·ester 산소에 음전하가 놓이는 공명 구조가 있다. 또한 화합물 4는 LDA와 enolate를 만들지는 않지만, 매우 반응성이 큰 Michael 수용체이므로 실제로는 중합이나 amine 첨가 같은 부반응이 일어날 수 있다.

### 핵심 개념

enolate(또는 안정화 탄소 anion)가 되려면 떼어 낼 H가 sp3 탄소에 있고 그 anion이 $\pi$계(C=O, C=C-C=O, C≡N)와 짝을 이룰 수 있어야 한다.

---

## 문제 3

a. (R)-(+)-2-methyl-1-phenylbutane-1-온(PhCO-CH(CH3)CH2CH3, 화합물 6)의 수용성 ethanol 용액을 염기로 처리하면 용액이 점차 광학 활성을 잃는다. ketone을 분리해 보면 racemization되어 있다. 이 변환의 메커니즘을 제안하라.

`6 (R) --[NaOH, EtOH]--> 6 (R) + 6 (S) (50:50)`

b. a의 결과를 바탕으로 다음 반응의 생성물을 예측하라.

`화합물 7 (cis-1-데칼론, cis-octahydronaphthalen-1(2H)-one, C10H16O; 두 고리 접합 H가 같은 쪽 쐐기) --[NaOH, EtOH]--> 8 (C10H16O)`

### 공식 풀이

- a: OH⁻가 sp3 $\alpha$-탄소의 H를 떼어 내어 평면 sp2 enolate 형성. enolate가 EtOH(HOEt)로부터 앞면에서 양성자를 받으면 6 (R), 뒷면에서 받으면 6 (S). 위쪽에 enolate + EtOH ⇌ ketone + EtO⁻ 평형을 별도로 표시.
- b: OH⁻가 carbonyl에 이웃한 고리 접합 H를 떼어 enolate 형성 → HOEt로 protonation → 8 = trans-1-데칼론 (carbonyl 옆 접합 H가 hash, 다른 접합 H는 쐐기). "trans- is more stable"이라고 표기.

(출처: Tutorial_3_answers p.2)

### 해설

이 문제의 핵심은 왜 carbonyl 옆 입체중심은 염기에서 "기억을 잃는가"이다. 답은 enolate가 평면이라는 데 있다(→ [L7](../notes/L07_Enolate_Alkylation.md) enolate 문서, L10 enol·tautomerization 문서 참고).

a에서 $\alpha$-탄소는 원래 sp3 입체중심이다. 그런데 OH⁻(또는 EtO⁻)가 이 $\alpha$-H를 떼어 내면 $\alpha$-탄소는 sp2가 되어 enolate의 평면에 놓인다. 즉 입체 정보가 사라진다. 그 뒤 enolate가 용매 EtOH로부터 양성자를 다시 받을 때, 위쪽 면과 아래쪽 면은 거울상 관계이므로 정확히 같은 확률로 공격받는다. 그래서 R과 S가 1:1로 생기고, 이 과정이 가역적으로 반복되면서 결국 라세미체가 된다.

b는 같은 원리를 고리 화합물에 적용한 것이다. 7에서 carbonyl에 이웃한 고리 접합 탄소(C8a)는 H를 가지므로 enolate가 될 수 있다. 하지만 이번에는 다른 쪽 고리 접합 탄소(C4a)의 입체중심이 그대로 남아 있다. 그래서 두 면의 protonation 생성물은 거울상이 아니라 부분입체 이성질체(diastereomer, cis와 trans)이고, 평형은 50:50이 아니라 더 안정한 쪽으로 기운다. trans-데칼린은 두 고리가 모두 의자 형태이면서 접합 결합이 서로 equatorial 관계로 연결되어 cis보다 고리 간 고우시 상호작용이 적다. 그래서 가역적 enolization의 thermodynamic 결과로 trans-1-데칼론 8이 주생성물이 된다. 분자식이 그대로(C10H16O)인 것도 이것이 이성질화(에피머화, epimerization)임을 알려 준다.

### 핵심 개념

$\alpha$-입체중심은 염기 조건에서 평면 enolate를 거쳐 라세미화(거울상) 또는 에피머화(부분입체: 더 안정한 trans-데칼론으로 수렴)된다.

---

## 문제 4

a. geraniol(9)을 geranylacetone(10)으로 어떻게 바꿀 수 있는가? 한 단계 이상이 필요할 수 있다.

`(CH3)2C=CH-CH2CH2-C(CH3)=CH-CH2OH --[여러 단계]--> (CH3)2C=CH-CH2CH2-C(CH3)=CH-CH2-CH2-CO-CH3`

b. ketone 11로부터 천연물 sativene, 12의 합성을 제안하라.

- 11: 각 methyl(angular methyl)이 붙은 고리 접합 탄소 바로 옆에 ketone을 가진 decalone. 다른 고리에 isopropyl group(hash)와 2차 OH(쐐기)가 있고, 반대쪽 고리 접합 H는 쐐기.
- 12 (사티벤): 삼환 골격에 exo-methylene(C=CH2), 각 methyl, isopropyl을 가진 sesquiterpene.

### 공식 풀이

a:
1. `제라니올 --[PBr3]--> 제라닐 브로마이드 (…C(CH3)=CH-CH2Br)`
2. `CH3COCH2CO2Et --[NaOEt]--> 아세토아세테이트 엔올레이트`
3. enolate + 제라닐 bromide → `EtO2C-CH(CH2-geranyl쇄)-CO-CH3` (ethyl 2-제라닐아세토아세테이트)
4. `--[NaOH, H2O]--> 카복실레이트(⁻O2C-CH(R)-COCH3)`
5. `--[HCl]--> β-케토산 HO2C-CH(R)-COCH3`
6. `--[Δ, -CO2]--> 제라닐아세톤 10`

b:
1. `11 --[TsCl, 염기]--> 2차 알코올의 토실레이트(OTs)`
2. `--[NaOEt]--> 케톤의 엔올레이트(각 메틸 반대쪽 α-CH2에서 형성)` → enolate 탄소가 C-OTs 탄소를 분자 내 SN2 공격(곡선 화살표로 표시) → 삼환 ketone
3. `삼환 케톤 --[Ph3P⁺-CH2⁻ (비티히 시약)]--> 사티벤 12`

(출처: Tutorial_3_answers p.2 (a), p.3 (b))

### 해설

이 문제의 핵심은 왜 "CH2COCH3 하나를 붙이는" 일을 acetone이 아니라 acetoacetic ethyl로 하는가, 그리고 b에서 왜 enolate가 고리 하나를 더 만들 수 있는가이다.

a는 전형적인 acetoacetic ester acetoacetic ester synthesis이다(→ [L7](../notes/L07_Enolate_Alkylation.md) enolate alkylation 문서 참고). 먼저 geraniol의 OH는 나쁜 leaving group이므로 PBr3로 bromide로 바꾼다. allyl bromide이므로 SN2 반응성이 좋다. 그런데 acetone을 직접 enolate로 만들면 자기 aldol 축합이나 다중 alkylation이 섞이기 쉽다. 그래서 두 carbonyl 사이 CH2(pKa 약 11)를 가진 ethyl acetoacetate를 쓰면 NaOEt만으로도 깨끗하게 하나의 안정화 enolate가 생기고, 이것이 제라닐 bromide를 SN2로 alkylation한다. 그 뒤 비누화와 산성화로 $\beta$-keto acid을 만들고, 가열하면 6원 고리 transition state로 CO2가 빠져 enol을 거쳐 methyl ketone이 된다. 즉 ester는 활성화기 역할만 하고 사라지며, 결과는 "acetone enolate로 alkylation한 것"과 같다. 탄소 수를 확인하면 제라닐(C10) + CH2COCH3(C3) = C13으로 geranylacetone과 일치한다.

b는 분자 내 enolate alkylation(intramolecular enolate alkylation)이다(→ [L7](../notes/L07_Enolate_Alkylation.md) enolate alkylation 문서 참고). 먼저 2차 OH를 TsCl로 tosylate로 바꿔 좋은 leaving group으로 만든다. 그런데 ketone의 한쪽 $\alpha$-탄소는 각 methyl이 붙은 4급 탄소여서 H가 없다. 그래서 NaOEt는 반대쪽 $\alpha$-CH2에서만 enolate를 만들 수 있고, 반응 위치가 자동으로 정해진다. 이 enolate 탄소가 데칼린 골격을 가로질러 C-OTs 탄소 뒷면을 공격하면(SN2, 입체 반전) 새 C-C 결합이 생겨 삼환 ketone이 된다. SN2는 leaving group 정반대편에서의 공격을 요구하므로, 이 고리화가 가능한 것은 11의 OH(따라서 OTs)의 입체 배치가 enolate 탄소가 뒷면에서 닿을 수 있도록 미리 설계되어 있기 때문이다. 마지막으로 남은 ketone을 비티히 반응(Ph3P=CH2)으로 C=CH2로 바꾸면 사티벤의 exo-methylene이 완성된다.

검토 의견: 공식 답은 옳다. a에서 덧붙이면, allyl alcohol에 PBr3를 쓰면 일부 allyl 자리옮김(SN2') 생성물이나 이중결합 기하 이성질화가 생길 수 있고, HCl 산성화·가열 단계에서는 삼치환 alkene이 산에 민감할 수 있으므로 온화한 조건이 필요하다. 이는 답의 타당성을 바꾸지 않는 실험적 주의점이다.

### 핵심 개념

a: acetoacetic ester 합성 = 안정화 enolate alkylation + 비누화 + decarboxylation으로 "R-CH2COCH3" 도입. b: tosylate를 leaving group으로 한 분자 내 enolate SN2 고리화 + 비티히 methylene화.

---

## 문제 5

다음 변환의 시약 또는 생성물을 제시하라.

a. `화합물 13 --[1. LDA; 2. 아크롤레인(acrolein, CH2=CH-CHO); 3. HCl 수용액]--> 14`

- 13: (S)-헵트-6-ene-2-일 acetate, 즉 CH3CO-O-CH(CH3)-CH2CH2CH2-CH=CH2 (그림의 쐐기 표기 기준으로 S 배열).

b. `사이클로헥산온(15) --[?]--> 16`

- 16: 2-(1-hydroxy-3-phenylpropyl)-2-methylcyclohexane-1-one, 즉 C2가 CH3와 CH(OH)-CH2CH2-Ph를 가진 4급 탄소.

### 공식 풀이

a:
1. `13 --[LDA]--> 아세테이트 에스터 엔올레이트 (⁻CH2-CO-OR ↔ CH2=C(O⁻)-OR)`
2. `--[아크롤레인, Aldol]--> CH2=CH-CH(O⁻)-CH2-CO-OR` (alkoxide)
3. `--[HCl]--> CH2=CH-CH(OH)-CH2-CO-OR` ($\beta$-hydroxy ester)
4. `--[H⁺]--> 14 = CH2=CH-CH=CH-CO-OR` (펜타-2,4-dienoic acid ester, 탈수 생성물)
(R = (S)-헵트-6-ene-2-일, 입체중심 유지)

b:
1. `15 --[LDA]--> 사이클로헥산온 엔올레이트`
2. `--[MeI]--> 2-methyl사이클로헥산온`
3. `--[Me3SiCl, Et3N]--> 1-트리메틸실릴옥시-2-methyl사이클로헥센` (더 치환된 C1=C2 silyl enol 에테르, silyl enol ether)
4. `--[i) PhCH2CH2CHO, TiCl4; ii) H2O]--> 16`

(출처: Tutorial_3_answers p.3)

### 해설

이 문제의 핵심은 어떤 enolate(또는 enol 등가체)를 어떤 조건으로 만들어야 원하는 탄소에서 aldol이 일어나는가이다.

a에서 LDA는 강하고 부피가 큰 비친핵성 염기이다. 그래서 ester carbonyl을 공격하지 않고 acetyl의 CH3에서만 H를 떼어 lithium ester enolate를 정량적으로 만든다(→ [L7](../notes/L07_Enolate_Alkylation.md) enolate 문서 참고). 반대쪽 alcohol 부분의 CH(CH3)는 산소에 붙은 탄소여서 carbonyl의 $\alpha$-위치가 아니므로 반응하지 않고, 따라서 그 입체중심도 그대로 유지된다. 그다음 acrolein을 넣으면 lithium enolate는 aldehyde carbonyl에 1,2-첨가하는 aldol 반응을 한다(→ [L8](../notes/L08_Aldol_Reactions.md) aldol 문서 참고). acrolein은 Michael 수용체이기도 하지만, lithium enolate와 반응성이 큰 aldehyde carbonyl의 조합에서는 저온 1,2-첨가가 우세하다. 그 결과 allyl형 2차 alkoxide가 생기고, HCl 수용액이 이것을 protonation한다. 공식 풀이는 여기서 산 촉매 탈수까지 진행되어, C=C가 ester와 짝을 이루고 원래 비닐기와도 짝을 이루는 dienoic acid ester 14가 생긴다고 본다. 탈수의 구동력은 짝을 이룬 dienoate의 안정성이다.

검토 의견: 공식 풀이는 14를 탈수 생성물 CH2=CH-CH=CH-CO2R로 제시하며, 이 문서에서도 그대로 공식 답으로 둔다. 다만 3단계 조건은 단지 "HCl 수용액"(일반적인 산성 후처리)이므로, 실제로는 $\beta$-hydroxy ester CH2=CH-CH(OH)-CH2-CO2R가 분리될 가능성이 높다. ester aldol 생성물은 ketone aldol 생성물에 비해 $\alpha$-H 산성도가 낮아 E1cB 탈수가 잘 일어나지 않으며, 산 촉매 탈수(allyl cation 경유 E1)는 보통 가열이나 더 강한 조건이 필요하다. 시험에서 공식 답에 맞추려면 "산 처리로 탈수되어 짝 디엔 ester 형성"을 쓰되, 탈수 전의 $\beta$-hydroxy ester를 intermediate로 함께 보여 주는 것이 안전하다.

b의 출발점은 역합성이다. 16은 C2가 4급 탄소이고 그 위에 CH3와 aldol 생성물 CH(OH)CH2CH2Ph가 있다. 그래서 C2에 methyl을 먼저 넣고, 그다음 같은 C2에서 aldol을 일으켜야 한다. 먼저 LDA/MeI로 enolate alkylation을 하여 2-methylcyclohexanone을 만든다. 그런데 2-methylcyclohexanone을 다시 LDA로 처리하면, LDA는 부피가 크므로 덜 치환된 C6에서 H를 떼어 내는 kinetic enolate를 만든다. 이것은 원하는 위치가 아니다. 그래서 Me3SiCl/Et3N 조건을 쓴다. 이 조건은 약염기·평형 조건이므로 더 치환되어 thermodynamic으로 안정한 C1=C2 silyl enol thermodynamic silyl enol ether를 준다(→ [L7](../notes/L07_Enolate_Alkylation.md) kinetic/thermodynamic enolate 문서 참고). silyl enol 에테르는 그 자체로는 친핵성이 약하지만, Lewis acid TiCl4가 aldehyde를 활성화하면 C2가 aldehyde를 공격하는 Mukaiyama aldol reaction이 일어난다(→ [L8](../notes/L08_Aldol_Reactions.md) aldol 문서 참고). 마지막으로 물 처리로 silyl group과 티타늄이 떨어지면 $\beta$-hydroxy ketone 16이 얻어진다. 즉 "thermodynamic enol 등가체를 silyl enol 에테르로 붙잡아 두고 Lewis acid으로 반응시키는" 것이 위치 선택성의 열쇠이다.

### 핵심 개념

a: LDA로 ester enolate → aldehyde에 1,2-aldol(공식 답은 이후 탈수까지). b: alkylation 후 thermodynamic silyl enol 에테르로 더 치환된 위치를 고정 → TiCl4 Mukaiyama aldol로 4급 탄소 형성.
