# L10. 엔올과 엔아민 (Enols and Enamines)

<!-- wiki-links:start -->

> **관련 위키 문서** ([위키 대문](../wiki/위키%20대문.md))
> - 반응: [aldol reaction](../wiki/반응/알돌%20반응.md), [alpha-halogenation](../wiki/반응/α-할로젠화.md), [Claisen condensation](../wiki/반응/클라이젠%20축합.md), [enolate alkylation](../wiki/반응/엔올레이트%20알킬화.md), [ester hydrolysis](../wiki/반응/에스터%20가수분해.md), [haloform reaction](../wiki/반응/할로폼%20반응.md), [keto-enol tautomerism](../wiki/반응/케토-엔올%20토토머화.md), [proline-catalyzed aldol reaction](../wiki/반응/프롤린%20촉매%20알돌%20반응.md), [reductive amination](../wiki/반응/환원성%20아미노화.md), [SN2 reaction](../wiki/반응/SN2%20반응.md), [Stork enamine reaction](../wiki/반응/스토크%20엔아민%20반응.md)
> - 시약: [LDA](../wiki/시약/LDA.md), [pyrrolidine](../wiki/시약/피롤리딘.md), [silyl enol ether](../wiki/시약/실릴%20엔올%20에터.md)
> - 개념: [carbocation](../wiki/개념/탄소%20양이온.md), [electrophile and nucleophile](../wiki/개념/친전자체와%20친핵체.md), [enamine](../wiki/개념/엔아민.md), [enol and enolate](../wiki/개념/엔올과%20엔올레이트.md), [imine](../wiki/개념/이민.md), [iminium ion](../wiki/개념/이미늄%20이온.md)

<!-- wiki-links:end -->

> 이 강의 노트는 **뼈대**다. 강의 순서와 슬라이드 위치만 정리했고, 설명은 링크된 개념 문서에 있다.

> 강의 흐름대로 길게 읽고 싶으면 **[통독본](통독/L10_Enol_and_Enamine.md)**(재구성 직전의 전체 노트, 소절마다 개념 문서 링크 포함)을 본다.

## 개요

염기로 만든 enolate 이야기의 "중성 버전"이다. 산 조건에서는 enolate 대신 enol이, 2차 amine을 쓰면 enamine이 nucleophile이 된다. 앞부분은 단순 ketone에서 1%도 안 되는 enol이 어떻게 반응을 이끌고(산 촉매 aldol), 왜 1,3-dicarbonyl에서는 enol이 주인공이 되는지(keto-enol tautomerism, K(enol/keto) 표, 비타민 C)를 다룬다. 이어 halogenation으로 enol의 반응성을 확인하고 silyl enol ether로 위치를 고르는 법을 본 뒤, enamine으로 강염기 없이 aldehyde를 alkylate하는 Stork과 2021년 노벨 화학상으로 이어진 proline 촉매 비대칭 aldol로 끝난다.

## 강의 흐름

### 1. 출발점: 염기 조건의 enolate 반응 (슬라이드 p.2)
- $\alpha$-alkylation, aldol, Claisen 세 반응 모두 enolate가 nucleophile이고 새 C–C 결합은 $\alpha$-탄소에서 생긴다.
- → [Claisen condensation](../wiki/반응/클라이젠%20축합.md) (enolate의 네 가지 상대), [enolate alkylation](../wiki/반응/엔올레이트%20알킬화.md), [aldol reaction](../wiki/반응/알돌%20반응.md)

### 2. 산 조건의 aldol reaction: enol이 nucleophile이 되다 (슬라이드 p.3)
- cyclopentanone: 산 촉매 enolization → enol이 protonate된 ketone을 공격 → E1 탈수로 2-cyclopentylidenecyclopentanone(enone)까지 간다.
- → [keto-enol tautomerization](../wiki/반응/케토-엔올%20토토머화.md) (enolization), [aldol reaction](../wiki/반응/알돌%20반응.md) (산 촉매 aldol), [carbocation](../wiki/개념/탄소%20양이온.md)

### 3. Keto-enol tautomer (슬라이드 p.4)
- keto형과 enol형은 H 위치가 다른 별개의 화합물(tautomer)이지 공명 구조가 아니다. enolate가 C에서 양성자를 받으면 keto, O에서 받으면 enol.
- → [keto-enol tautomerization](../wiki/반응/케토-엔올%20토토머화.md), [enol and enolate](../wiki/개념/엔올과%20엔올레이트.md)

### 4. 단순 carbonyl 화합물에서 enol이 적은 이유 (슬라이드 p.5)
- acetone 1.5 × 10⁻⁴ %, cyclohexanone 1.2 %. C=O $\pi$(364) > C=C $\pi$(250 kJ/mol).
- → [keto-enol tautomerization](../wiki/반응/케토-엔올%20토토머화.md)

### 5. 1,3-dicarbonyl: enol이 주인공 (슬라이드 p.6)
- pentane-2,4-dione 76 % enol(공액 + 분자 내 수소결합 6원 고리). ¹H NMR에서 enol O–H $\delta$ 15.5. piroxicam, leptospermone.
- → [keto-enol tautomerization](../wiki/반응/케토-엔올%20토토머화.md)

### 6. 치환기에 따른 K(enol/keto) (슬라이드 p.7)
- 끝 alkyl이 커지면 K↑, 가운데 alkyl은 K↓, CF₃·Ph·Cl·CN은 enol↑, $\beta$-keto ester는 keto 우세.
- → [keto-enol tautomerization](../wiki/반응/케토-엔올%20토토머화.md)

### 7. 비타민 C: 몸 속의 안정한 enol (슬라이드 p.8)
- lactone C=O와 공액된 enediol.
- → [keto-enol tautomerization](../wiki/반응/케토-엔올%20토토머화.md)

### 8. 산 조건 halogenation (슬라이드 p.9)
- acetone --[Br₂, HOAc]--> bromoacetone. enol의 C=C가 Br₂를 공격한다. AlCl₃ 촉매에서도 acyl group으로 불활성화된 benzene 고리는 반응하지 않는다. 산 조건은 대개 mono.
- → [$\alpha$-halogenation](../wiki/반응/α-할로젠화.md), [haloform reaction](../wiki/반응/할로폼%20반응.md) (염기 조건과의 대비), [substituent effect](../wiki/개념/치환기%20효과.md)

### 9. Silyl enol ether를 경유한 halogenation (슬라이드 p.10)
- LDA → Me₃SiCl → Br₂로 덜 치환된 $\alpha$-탄소에 Br. silyl group은 "큰 수소".
- → [$\alpha$-halogenation](../wiki/반응/α-할로젠화.md), [silyl enol ether](../wiki/시약/실릴%20엔올%20에터.md), [LDA](../wiki/시약/LDA.md)

### 10. Enamine: 질소가 밀어주는 enol (슬라이드 p.11)
- 2차 amine(pyrrolidine 등) + ketone → enamine. Stork alkylation: $\alpha$-탄소가 R–X를 S<sub>N</sub>2로 공격 → iminium → 가수분해. enol보다 nucleophilic, 다중 alkylation 억제.
- → [enamine](../wiki/개념/엔아민.md), [Stork enamine reaction](../wiki/반응/스토크%20엔아민%20반응.md), [iminium ion](../wiki/개념/이미늄%20이온.md), [imine](../wiki/개념/이민.md), [pyrrolidine](../wiki/시약/피롤리딘.md), [reductive amination](../wiki/반응/환원성%20아미노화.md)

### 11. Enamine으로 aldehyde를 alkylate하기 (슬라이드 p.12)
- 강염기가 없으니 self-condensation이 없다. pentanal + BrCH₂CO₂Et, 2-ethylhexanal + allyl bromide(4차 $\alpha$-탄소).
- → [Stork enamine reaction](../wiki/반응/스토크%20엔아민%20반응.md)

### 12. Enamine과 aldol: proline이라는 작은 촉매 (슬라이드 p.13)
- List–Lerner–Barbas(2000): acetone + ArCHO, L-proline 30 mol% → 68 %, 76 % ee. 지방족 $\alpha$-가지 aldehyde는 >99 % ee.
- → [proline-catalyzed aldol reaction](../wiki/반응/프롤린%20촉매%20알돌%20반응.md)

### 13. 비대칭 aldol의 촉매 순환 (슬라이드 p.14)
- carbinolamine → iminium → enamine → (carboxylic acid가 aldehyde를 수소결합으로 붙잡은 TS) C–C 형성 → 가수분해, proline 재생.
- → [proline-catalyzed aldol reaction](../wiki/반응/프롤린%20촉매%20알돌%20반응.md), [enamine](../wiki/개념/엔아민.md)

### 14. 정리 (슬라이드 p.15)
- keto와 enol은 tautomer, 1,3-dicarbonyl은 안정한 enol, enol은 halogenation, enamine은 alkylation과 aldol형 반응의 nucleophile. (p.16은 빈 슬라이드)

## 반응 요약표

| 반응 | 시약/조건 | 생성물 | 비고 |
|---|---|---|---|
| [enolate alkylation](../wiki/반응/엔올레이트%20알킬화.md) | enolate + R'CH₂Br | R–CO–CH₂–CH₂R' | S<sub>N</sub>2, 염기 조건 (p.2) |
| [aldol reaction](../wiki/반응/알돌%20반응.md) (enolate) | enolate + R'COR'' | $\beta$-hydroxy carbonyl → enone | 가역 (p.2) |
| [Claisen condensation](../wiki/반응/클라이젠%20축합.md) | enolate + ester(–OEt) | 1,3-dicarbonyl | EtO⁻ 이탈 (p.2) |
| [aldol reaction](../wiki/반응/알돌%20반응.md) (산 촉매) | cyclopentanone, H⁺ | 2-cyclopentylidenecyclopentanone | enol이 nucleophile, E1 탈수 (p.3) |
| [$\alpha$-halogenation](../wiki/반응/α-할로젠화.md) (산 촉매) | Br₂, HOAc | bromoacetone | mono (p.9) |
| [$\alpha$-halogenation](../wiki/반응/α-할로젠화.md) (Lewis acid) | Br₂, 0.75 mol% AlCl₃, Et₂O | 2-bromo-1-phenylpentan-1-one (100 %) | 고리 반응 없음 (p.9) |
| [$\alpha$-halogenation](../wiki/반응/α-할로젠화.md) (silyl enol ether) | 1. LDA 2. Me₃SiCl 3. Br₂ | R–CH₂–CO–CH₂Br | 덜 가려진 $\alpha$-탄소 (p.10) |
| [enamine](../wiki/개념/엔아민.md) 형성 | 2차 amine, cat. H⁺ | enamine | (p.11) |
| [Stork enamine reaction](../wiki/반응/스토크%20엔아민%20반응.md) | 1. R–X 2. H₂O, H⁺ | 2-alkylcyclohexanone | iminium intermediate (p.11) |
| [Stork enamine reaction](../wiki/반응/스토크%20엔아민%20반응.md) (aldehyde) | pentanal, (i-Bu)₂NH/H⁺; BrCH₂CO₂Et; H₂O | ethyl 3-formylhexanoate | self-condensation 없음 (p.12) |
| [Stork enamine reaction](../wiki/반응/스토크%20엔아민%20반응.md) (aldehyde) | 2-ethylhexanal, pyrrolidine/H⁺; allyl bromide; H₂O | 2-allyl-2-ethylhexanal | 4차 $\alpha$-탄소 (p.12) |
| [proline-catalyzed aldol reaction](../wiki/반응/프롤린%20촉매%20알돌%20반응.md) | acetone + RCHO, L-proline 30 mol%, DMSO | CH₃COCH₂CH(OH)R | (R), 76 % ee(4-NO₂C₆H₄) ~ >99 % ee (p.13–14) |

## 연습 문제

→ [L10 연습 문제](../practice/L10_Exercises.md) (강의 노트의 연습 문제와 해설)
→ [L10 연습문제](../practice/L10_Practice.md) (공식 연습문제와 풀이)

## 출처

- 슬라이드: L10 (PDF p.1–16, p.16은 빈 슬라이드)
