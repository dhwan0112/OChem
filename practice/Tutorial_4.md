# CM3121 Tutorial 4 — 고리화 첨가 반응(Cycloadditions)

> 범위: L13–L15 cycloaddition(Diels–Alder, 위치·stereoselectivity, Woodward–Hoffmann 규칙, [4+3], 광화학 [2+2], siloxydiene)
> 출처 파일: 문제 `Tutorial_Questions_4.pdf` (2쪽). **공식 답이 제공되지 않았다.** 아래 풀이는 강의 내용을 근거로 한 제안이며, 확신이 낮은 부분은 [불확실]로 표시했다.

---

## 문제 1

cycloaddition 반응(pericyclic reaction) 생성물의 구조를 제안하고, 해당되면 regioselectivity과 stereoselectivity을 설명하라.

`Danishefsky 다이엔 ((E)-1-메톡시-3-(트라이메틸실릴옥시)-1,3-뷰타다이엔, MeO–CH=CH–C(OSiMe3)=CH2) + 메틸 사이클로헥사-1,4-다이엔-1-카복실레이트 (methyl cyclohexa-1,4-diene-1-carboxylate) --> ?`

(출처: Tutorial_Questions_4 p.1)

### 풀이 제안 (공식 답 없음)

**반응하는 C=C:** dienophile의 두 C=C 중 CO2Me와 콘쥬게이션된 C1=C2만 반응한다. 고립된 C4=C5는 반응하지 않는다.

**일차 cycloaddition물(Diels–Alder 생성물):** cis-융합 이환(bicyclo[4.4.0]) 화합물.
- 새 고리: C$\alpha$(CO2Me, 고리 융합 사차 탄소) – CH(OMe) – CH= C(OSiMe3) – CH2 – C$\beta$(H, 고리 융합) – C$\alpha$
- 원래 고리: C$\alpha$ – CH2 – CH=CH – CH2 – C$\beta$ (고립 이중결합 유지)
- naphthalene 번호로 쓰면: 4a-CO2Me, 4-OMe, 2-OSiMe3, $\Delta^{2}$(silyl enol ether), $\Delta^{6}$, 8a-H. 즉 methyl 4-methoxy-2-(trimethylsilyl옥시)-cis-4a,8a-융합 hexahydronaphthalene-4a-carboxylate 형태다.
- 고리 융합: 4a-CO2Me와 8a-H는 cis(→ cis-융합).
- OMe의 상대배치: endo 규칙을 적용하면 OMe는 CO2Me와 cis다. [불확실: 아래 해설 참고]

**산 후처리 시(Danishefsky diene의 일반적 후속 반응, L15 p.26):** silyl enol ether가 가수분해되어 ketone이 되고, $\beta$-OMe가 제거되어 cyclohexenone이 된다.
- 생성물: cis-4a-(methoxycarbonyl)-4a,5,8,8a-tetrahydronaphthalene-2(1H)-온 유형. 즉 C2=O, C3=C4 enone(C4는 4a에 인접), $\Delta^{6}$ alkene, cis-고리 융합.
- 문제는 "cycloaddition 생성물"을 물었으므로 일차 생성물을 답으로 하되, 산 처리 생성물도 함께 알아 두는 것이 좋다.

### 해설

이 문제의 핵심은 왜 특정 방향(위치)과 특정 면(입체)으로만 고리가 닫히느냐이다. 먼저 반응성부터 보자. Danishefsky diene은 OMe와 OSiMe3라는 두 전자주개(X-형 치환기)를 가진 매우 전자가 풍부한 diene이다. 그래서 HOMO가 높다. dienophile 쪽에서는 CO2Me(Z-형 치환기)가 붙은 C=C만 LUMO가 낮다. 즉 HOMO(diene)–LUMO(dienophile) 간격이 작은 쪽, 곧 ester와 콘쥬게이션된 C=C만 반응한다. 고립된 다른 C=C는 구경꾼이다. (→ [L14](../notes/L14_Cycloaddition_Part2.md) p.3, p.10의 FMO·치환기 분류 참고)

다음은 regioselectivity이다. diene에서 가장 친핵적인 탄소, 즉 HOMO 계수가 가장 큰 탄소는 어디일까? OMe는 C1에 붙어 있어 C2와 C4로 전자를 밀어 주고, OSiMe3는 C3에 붙어 있어 C4로 전자를 밀어 준다. 그래서 두 전자주개가 모두 C4(말단 CH2)를 가리키며, C4가 압도적으로 가장 친핵적인 끝이 된다. 그런데 dienophile에서 가장 친전자적인 탄소는 CO2Me의 $\beta$-탄소(H가 붙은 C$\beta$)다. 그래서 diene C4–dienophile C$\beta$ 결합이 먼저(비대칭 전이상태에서 더 많이) 형성되고, 남은 C1(OMe)은 C$\alpha$(CO2Me)와 결합한다. 결과를 강의식으로 표현하면 이렇다. C1-치환(OMe)은 "ortho" 생성물(OMe와 CO2Me가 1,2 관계)을, C2-치환(OSiMe3)은 "para" 생성물(OSiMe3와 CO2Me가 1,4 관계)을 준다. 두 규칙이 서로 모순 없이 같은 생성물을 가리키므로 regioselectivity은 매우 높다. (→ [L14](../notes/L14_Cycloaddition_Part2.md) p.11–15 regioselectivity 참고)

이제 stereoselectivity이다. 먼저 고리 융합은 확실하다. 고리형 dienophile에서 고리의 두 CH2(C3, C6)는 C=C의 같은 쪽(cis)에 있다. 그런데 Diels–Alder는 dienophile에 대해 suprafacial(입체특이적)이다. 그래서 이 cis 관계가 그대로 생성물로 옮겨지고, 결국 4a-CO2Me와 8a-H도 cis인 cis-융합 이환 화합물이 된다. 이것은 반응 메커니즘이 강제하는 결과라서 확실하다. (→ [L13](../notes/L13_Cycloaddition_Part1.md) p.19 stereospecificity 참고)

그런데 C4의 OMe 배치는 endo/exo에 따라 달라진다. 강의의 endo 규칙(L13 p.21–24)은 전자끌개가 diene endo에 놓이는 전이상태를 선호한다고 말한다. 이 규칙을 따르면 CO2Me가 endo이고, (E)-diene의 "바깥쪽(out)" 치환기인 OMe는 endo 치환기와 같은 쪽에 놓인다. 그래서 OMe와 CO2Me는 cis가 된다. 그런데 여기서 dienophile은 사치환에 가까운 붐비는 고리형 alkene이다. C$\alpha$ 쪽에는 CO2Me와 고리 CH2가, C$\beta$ 쪽에는 H와 고리 CH2가 경쟁한다. 그래서 입체 효과가 endo 선호를 뒤집을 가능성이 있다. [불확실] 이 문헌 결과를 확인하지 못했으므로 OMe의 상대배치는 "endo 규칙에 따른 예측"으로만 제시한다. 다행히 산 처리로 OMe가 제거되면 이 입체중심은 사라진다. 그래서 산 처리 생성물에서는 cis-고리 융합만 남는다.

마지막으로 Woodward–Hoffmann 관점에서 보면 [$4\pi$s + $2\pi$s]는 (4q+2)s 성분이 dienophile $2\pi$이므로 열적으로 허용된다. 전자 수로 보면 6 = 4n+2이다. (→ [L13](../notes/L13_Cycloaddition_Part1.md) p.33–35 참고)

### 핵심 개념

- 전자가 풍부한 diene(Danishefsky) + 전자 부족 dienophile: 콘쥬게이션된 C=C만 선택적으로 반응한다.
- regioselectivity: 1-치환 diene → "ortho", 2-치환 diene → "para". 두 효과가 일치하면 선택성이 높다.
- 고리형 dienophile은 suprafacial 첨가로 cis-융합 이환 생성물을 준다. 고리 밖 입체중심은 endo 규칙으로 예측한다.
- Danishefsky diene cycloaddition물은 산 처리로 cyclohexenone이 된다(L15 p.26).

---

## 문제 2

표적 분자 합성에 필요한 반응물과 시약을 제안하고, 해당되면 위치·stereoselectivity을 설명하라.

**(a)** `[A] + [B] --> [C] --> 표적 1`

표적 1: 삼환 $\gamma$-락톤. 두 개의 cyclobutane이 맞붙은 bicyclo[2.2.0]hexane 핵에 cyclohexane이 융합되어 있다.
- 왼쪽 cyclobutane: CH2–CH2와 두 사차 탄소(하나는 CO2Me, 다른 하나는 락톤 C=O를 가짐)
- 가운데 cyclobutane: 위의 두 사차 탄소 + C(CH3)(고리 융합) + C(H)(고리 융합)
- cyclohexane: C(CH3), CH2, CH2, CH2, CH(O–), C(H)
- 락톤: 사차 탄소–C(=O)–O–CH(cyclohexane)–C(H)–사차 탄소 (5원자 고리)
- 입체: CO2Me와 락톤 C=O는 wedge(같은 쪽), CH3와 고리 융합 H는 hash(반대쪽), CH–O 결합은 wedge

**(b)** `[A] + [B] --> [C] --[in situ DA]--> 표적 2`

표적 2: cis-3,4,4a,5,8,8a-hexahydronaphthalene-1(2H)-온(cis-3,4,4a,5,8,8a-hexahydronaphthalen-1(2H)-one). C1=O, 두 고리 융합 H는 cis(둘 다 hash), C5=C6 이중결합은 고리 융합 탄소 C4a에 인접한다.

(출처: Tutorial_Questions_4 p.1)

### 풀이 제안 (공식 답 없음)

**(a)**
- A = dimethyl 사이클로뷰트-1-ene-1,2-다이카복실레이트(dimethyl cyclobut-1-ene-1,2-dicarboxylate)
- B = 3-methylcyclohex-2-ene-1-온(3-methylcyclohex-2-en-1-one)
- `A + B --[hν (광화학 [2+2])]--> C`
- C = 광화학 cycloaddition물(cis-anti-cis 삼환 keto diester). L14 p.28 슬라이드의 예시와 **동일한 반응**이다.
- `C --[NaBH4 (케톤 환원); 이어서 분자 내 락톤화(필요시 산 촉매 또는 가열)]--> 표적 1`

**(b)**
- C = (E)-데카-1,7,9-triene-3-온((E)-deca-1,7,9-trien-3-one, CH2=CH–CO–CH2CH2CH2–CH=CH–CH=CH2). 이 화합물이 분자 내 Diels–Alder(intramolecular Diels–Alder, IMDA)를 일으켜 표적 2가 된다.
- 제안 1(권장): A = (E)-N-methoxy-N-methyl옥타-5,7-dieneamide(Weinreb amide, CH2=CH–CH=CH–(CH2)3–CON(OMe)Me), B = 바이닐마그네슘 bromide(CH2=CHMgBr) → C(바이닐 ketone)가 생기자마자 실온 부근에서 IMDA.
- 제안 2(대안): A = (E)-옥타-5,7-diene알, B = CH2=CHMgBr → allyl alcohol → DMP 산화로 바이닐 ketone을 만들고 in situ IMDA. 이 경우 실제로는 산화 단계가 하나 더 필요하다.
- [불확실] 문제의 상자 배치(A + B → C, C → 표적 사이 화살표에 시약 상자 없음)로 보아 C가 곧 trienone이라고 해석했다. A + B 단계가 출제자가 의도한 반응인지는 확인할 수 없다. 핵심인 "C = trienone, (E)-diene, endo IMDA → cis-융합"은 비교적 확실하다.

### 해설

**(a)** 이 문제의 핵심은 cyclobutane 두 개가 맞붙은 bicyclo[2.2.0]hexane 골격을 어떻게 만드느냐이다. 4원자 고리를 보면 [2+2] cycloaddition을 떠올려야 한다. 가운데 cyclobutane을 [2+2]로 거꾸로 자르면 두 alkene이 나온다. 하나는 왼쪽 cyclobutane에 붙은 C=C(두 사차 탄소 사이), 곧 cyclobutene-1,2-diester다. 다른 하나는 CH3가 붙은 탄소와 H가 붙은 탄소 사이의 C=C, 곧 3-methylcyclohexenone이다. 그런데 표적에는 ketone 대신 락톤의 CH–O가 있다. 그래서 "광화학 [2+2]로 keto diester를 만든 뒤, ketone을 환원해 생긴 OH가 옆의 ester와 락톤을 만든다"는 2단계 경로가 나온다. 실제로 이 [2+2] 반응은 강의 L14 p.28에 그대로 실려 있다.

그렇다면 왜 열이 아니라 빛인가? 두 alkene의 [$2\pi$s + $2\pi$s]는 (4q+2)s 성분이 2개(짝수)라서 열적으로 금지된다. 즉 HOMO–LUMO의 위상이 한쪽 끝에서 어긋난다. 그런데 빛으로 한 enone을 들뜨게 하면 HOMO–HOMO와 LUMO–LUMO 상호작용이 모두 결합성이 되어 suprafacial–suprafacial 경로가 허용된다. (→ [L14](../notes/L14_Cycloaddition_Part2.md) p.25–27 참고) 각 alkene의 기하는 유지된다(입체특이적). 그래서 cyclobutene 쪽의 두 CO2Me는 cis로, cyclohexenone 쪽의 CH3와 H도 cis로 남는다. 두 성분이 서로 마주 보는 방향은 endo 효과가 아니라 입체 장애가 가장 적은 anti으로 정해진다(강의: "no endo selectivity"). 그 결과 diester 쪽 치환기와 CH3/H가 서로 반대쪽에 놓인 cis-anti-cis 배치가 된다. 표적에서 CO2Me·락톤 C=O는 wedge이고 CH3·H는 hash인 것이 바로 이 배치다. regioselectivity은 대칭 diester라서 문제가 되지 않는다. enone 쪽은 C=C의 두 탄소가 각각 diester의 한 탄소와 결합할 뿐이다.

다음은 락톤화다. NaBH4가 ketone을 이차 alcohol로 환원한다. 그런데 락톤이 닫히려면 새 OH가 가까운 쪽 ester(고리 융합 H 쪽 사차 탄소의 CO2Me)와 같은 면에 있어야 한다. 반대 면의 OH로는 5원자 락톤을 만들 수 없다. 오목한 삼환 골격에서 수소화물은 덜 막힌 볼록면, 즉 고리 융합 H 쪽 면에서 들어올 것으로 예상된다. 그러면 OH는 ester와 같은 면에 놓이고, 분자 내 ester 교환(MeOH 이탈)으로 $\gamma$-락톤이 닫힌다. [불확실] 환원의 면 선택성은 정성적 추론이다. 원하지 않는 에피머가 생기면 그 에피머는 락톤화되지 않는다.

**(b)** 이 문제의 핵심은 "in situ DA"라는 힌트가 무엇을 가리키느냐이다. 먼저 표적의 C5=C6 이중결합 위치를 보자. Diels–Alder로 생긴 cyclohexene에서 새 C=C는 언제나 diene의 가운데 두 탄소(C2, C3) 사이에 생긴다. 그런데 표적에서는 C=C가 고리 융합 탄소 C4a 바로 옆에 있다. 그래서 C4a는 diene의 말단 탄소여야 하고, 다른 융합 탄소 C8a는 dienophile 탄소여야 한다. 즉 고리 융합 결합(C4a–C8a) 자체가 DA로 생긴 결합이다. 그런데 두 융합 탄소는 ketone 고리(C1–C4)로도 이미 연결되어 있다. 그래서 이 반응은 diene과 dienophile이 한 분자 안에 있는 분자 내 Diels–Alder(IMDA)여야 한다. 거꾸로 펼치면 dienophile(바이닐 ketone CH2=CH–CO–)와 diene(–CH=CH–CH=CH2)이 (CH2)3 사슬로 이어진 데카-1,7,9-triene-3-one이 C가 된다.

그렇다면 왜 "in situ"인가? 바이닐 ketone은 매우 반응성이 큰 dienophile다. 게다가 분자 내 반응이라 유효 농도가 높아 생성되자마자 고리화가 진행된다. 그래서 C를 분리하지 않고 그 자리에서 DA가 일어난다. 이런 바이닐 ketone은 Weinreb amide에 바이닐 Grignard를 더해 한 번에 만드는 것이 가장 깔끔하다(Weinreb amide는 과첨가 없이 ketone에서 멈춘다). [불확실] Weinreb amide가 강의 범위인지는 확인하지 못했다. 강의 범위로만 풀어야 한다면 제안 2(aldehyde + 바이닐 Grignard → allyl alcohol → DMP oxidation → in situ IMDA)가 대안이다.

마지막으로 입체화학이다. 표적의 두 고리 융합 H는 cis이다. diene이 (E)형이면 사슬(테더)은 diene 말단의 "바깥쪽(out)" 치환기가 된다. 그런데 endo 전이상태에서는 dienophile의 carbonyl(테더에 포함됨)이 diene 아래로 들어간다. 그러면 endo 치환기와 out 치환기는 생성물에서 cis가 된다. 즉 고리 융합 탄소에서 두 고리 사슬이 cis이므로 두 H도 cis, 곧 cis-융합이다. (E)-diene이 exo 경로를 밟으면 trans-융합이 된다. (Z)-diene이라면 반대로 endo → trans, exo → cis가 된다. 그래서 표적(cis)에는 (E)-diene + endo 경로가 강의의 endo 규칙과 가장 잘 맞는다. [불확실] 실제 IMDA는 테더의 형태 제약 때문에 endo 규칙이 약해져 cis/trans 혼합물이 나오는 경우가 많다. ketone이 테더 안에 있는 trienone은 cis-융합을 선호한다는 문헌 경향이 있는 것으로 알고 있지만 확인하지는 못했다. (→ [L13](../notes/L13_Cycloaddition_Part1.md) p.19–24 stereospecificity·endo 규칙, L06 문서의 DMP 부분 참고)

### 핵심 개념

- 4원자 고리 → [2+2] 역합성. alkene + alkene [2+2]는 광화학적으로만 허용되며, endo 선택성 없이 입체 장애 최소 cis-anti-cis을 취한다.
- ketone 환원 후 인접 ester와 분자 내 락톤화하여 $\gamma$-락톤을 만든다.
- 새 C=C의 위치로 DA 결합을 역추적한다. 고리 융합 결합이 DA 결합이면 IMDA다.
- IMDA 입체: (E)-diene + endo → cis-융합, (E)-diene + exo → trans-융합.

---

## 문제 3

다음 반응의 메커니즘을 제안하라(힌트: 핵심 단계는 cycloaddition). regioselectivity을 설명하고, 이 반응이 Woodward–Hoffmann 규칙에 따라 허용되는지 답하라.

`2-브로모-2-methyl-N-R-프로판아마이드 (Me2CBr–CO–NHR) + 트로폰 (tropone, 사이클로헵타-2,4,6-트라이엔-1-one) --[Na2CO3, solvent]--> 2,2-다이메틸-4-R-사이클로헵타[b][1,4]옥사진-3-one 유형 이환 생성물`

생성물 구조: 6원자 1,4-oxazine-3-one 고리(O–CMe2–C(=O)–N(R)–CH–C)가 cycloheptatriene에 융합되어 있다. tropone의 산소가 CMe2에 결합하고, tropone의 C2($\alpha$-탄소)가 N에 결합하며 sp3 CH가 된다. 원래 C=O 탄소는 enol ether 탄소(C=C–O)가 된다.

(출처: Tutorial_Questions_4 p.2)

### 풀이 제안 (공식 답 없음)

**메커니즘:**
1. Na2CO3가 amide N–H를 deprotonate하여 amidate anion Me2CBr–C(O)=N⁻R을 만든다.
2. Br⁻가 이탈하며 **아자-옥시알릴 cation(aza-oxyallyl cation)**이 생긴다. 공명 구조는 [Me2C⁺–C(=O)–N⁻R ↔ Me2C=C(O⁻)–N⁺R…]이며, 전체적으로 중성인 1,3-쌍극자형 화학종이다. 3원자(C–C–N) $\pi$계에 전자 2개가 있고, 중앙 탄소에 O⁻가 붙은 구조로, L14의 옥시알릴 cation의 질소 유사체다.
3. 아자-옥시알릴 cation(3원자, $2\pi$)과 tropone(O=C1–C7=C6–C5=C4–C3=C2의 8원자, $8\pi$)이 cycloaddition한다. CMe2–O(tropone) 결합과 N–C2(tropone) 결합이 생긴다. 이것은 원자 수로 [8+3], 전자 수로 [$8\pi$ + $2\pi$] cycloaddition이다.
4. 그 결과 tropone 쪽 이중결합은 C1=C7, C6=C5, C4=C3로 재배치되고, C2는 sp3(H, N)가 되어 생성물이 된다.

**regioselectivity:** 아자-옥시알릴 cation의 친전자성 말단(삼차 carbocation 성격의 CMe2)이 tropone의 친핵성 carbonyl O과 결합하고, 친핵성 말단(N⁻)이 tropone의 친전자성 탄소(C2)와 결합한다.

**Woodward–Hoffmann:** [$\pi8\mathrm{s}$ + $\pi2\mathrm{s}$]. (4q+2)s 성분이 1개($2\pi$ allyl cation), (4r)s 성분($8\pi$)은 세지 않으므로 합은 1(홀수)이다. 그래서 열적으로 **허용**된다. 총 전자 수 10 = 4n+2(n = 2)로도 같은 결론이다.

[불확실] 이 반응이 완전한 concerted cycloaddition인지, 아니면 tropone O가 먼저 CMe2 cation을 공격하고 이어서 N이 C2에 conjugate addition하는 단계적(stepwise, 이온성) 과정인지는 이 자료만으로 판단할 수 없다. 문제가 "cycloaddition"라고 힌트를 주었으므로 협동 [8+3]으로 답하는 것이 출제 의도에 맞을 것으로 본다. 또한 이런 반응에는 보통 HFIP 같은 극성·비친핵성 용매가 cation 생성을 돕는 용도로 쓰이는 것으로 알려져 있으나, 문제에는 "solvent"로만 적혀 있다.

### 해설

이 문제의 핵심은 생성물의 6원자 고리가 어떤 두 성분의 어떤 원자들로 만들어졌는지 알아내는 것이다. 생성물 고리를 한 바퀴 돌면 O, CMe2, C=O, N, CH, C(enol ether)이다. 이 중 CMe2–C(=O)–N은 amide에서, O–C–CH는 tropone에서 왔다. 그래서 새로 생긴 결합은 O–CMe2와 N–CH, 두 개다. 두 결합이 한 번에 생겨 고리가 닫히므로 cycloaddition으로 볼 수 있다.

그런데 $\alpha$-bromo아마이드 자체는 cycloaddition을 할 수 없다. 그래서 먼저 반응성 intermediate를 만들어야 한다. 염기가 N–H를 떼어 내면 질소 anion이 생기고, 이것이 이웃 탄소의 Br⁻를 밀어내도록 돕는다. 그러면 Me2C carbocation, C–O⁻, N이 하나의 $\pi$계로 이어진 아자-옥시알릴 cation이 된다. 이 화학종은 강의에서 [4+3]에 쓰인 allyl cation과 똑같은 전자 구조를 가진다. 즉 3원자에 $\pi$전자 2개다. (→ [L14](../notes/L14_Cycloaddition_Part2.md) p.23–24 [4+3] 참고) 한쪽 끝(CMe2)은 친전자적이고 다른 끝(N)은 친핵적이라는 점에서 1,3-쌍극자와도 닮았다. (→ [L15](../notes/L15_Cycloaddition_Part3.md) p.13 1,3-쌍극자 참고)

다음 질문은 tropone이 몇 전자 성분으로 참여하느냐이다. 새 결합이 생기는 두 원자는 O와 C2다. 이 둘을 $\pi$계로 잇는 경로를 따라가면 O=C1, C7=C6, C5=C4, C3=C2를 모두 거친다. 즉 tropone 전체가 8원자 $8\pi$ 성분으로 참여한다. C1과 C2는 원래 $\sigma$결합으로 이웃해 있으므로, 실제로 생기는 고리는 11원자 고리가 아니라 6원자 고리다. 그래서 반응 후 tropone의 이중결합이 한 칸씩 밀려 C1=C7, C6=C5, C4=C3가 되고, C2는 sp3가 된다. 생성물 그림의 cycloheptatriene 이중결합 배치가 바로 이렇다. 강의의 [6+4] (tropone + cyclopentadiene, L14 p.22)에서 tropone이 $6\pi$로 쓰였다면, 여기서는 carbonyl 산소까지 포함한 $8\pi$로 쓰인 셈이다.

regioselectivity은 "친핵 말단과 친전자 말단의 짝맞춤"으로 설명된다. tropone은 C=O가 강하게 분극되어 있어서 방향족 트로필륨 oxide(C7H6⁺–O⁻) 성격이 크다. 그래서 산소는 전자가 풍부한 친핵 말단이고, 양전하는 고리의 C2, C4, C7 등에 퍼져 C2가 친전자 말단이 된다. 그런데 아자-옥시알릴 cation에서는 CMe2가 친전자 말단(삼차 carbocation 성격, LUMO 계수가 큼)이고 N이 친핵 말단이다. 그래서 O(tropone)→CMe2, N→C2(tropone)으로 결합하는 방향이 선택된다. 반대 방향, 즉 CMe2–C2와 N–O 결합은 electrophile끼리, nucleophile끼리 만나야 하므로 불리하다. 이것은 강의의 "FMO 계수가 가장 큰 원자끼리 결합한다"는 원리와 같은 이야기다. (→ [L15](../notes/L15_Cycloaddition_Part3.md) p.25 요약 참고)

마지막으로 Woodward–Hoffmann 판정을 해 보자. 열적 반응에서 "(4q+2)s 성분 수 + (4r)a 성분 수 = 홀수"면 허용된다. 아자-옥시알릴 cation은 $2\pi$ suprafacial 성분이므로 (4q+2)s(q = 0)에 해당해 1개로 센다. tropone은 $8\pi$ suprafacial 성분, 즉 (4r)s라서 세지 않는다. 그래서 합은 1, 홀수이므로 열적으로 허용된다. 간단히 말해 총 10전자(4n+2)의 supra–supra cycloaddition라서 Diels–Alder(6전자)와 같은 부류다. (→ [L14](../notes/L14_Cycloaddition_Part2.md) p.4–6, p.22 Woodward–Hoffmann 참고)

### 핵심 개념

- $\alpha$-할로아마이드 + 염기 → 아자-옥시알릴 cation(3원자 $2\pi$, 옥시알릴 cation의 질소 유사체).
- tropone은 carbonyl 산소를 포함한 $8\pi$ 성분으로 참여할 수 있다 → [8+3] cycloaddition.
- regioselectivity: 친전자 CMe2–친핵 tropone O, 친핵 말단(N)–친전자 tropone C2의 짝맞춤.
- WH: [$\pi8\mathrm{s}$ + $\pi2\mathrm{s}$], 10전자 = 4n+2 → 열적으로 허용된다.
