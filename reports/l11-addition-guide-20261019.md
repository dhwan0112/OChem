# L11 1,2/1,4-addition 단계별 비교 보강 — 2026-10-19

## 반영

L11 통독 §3의 기존 비교표 다음과 `wiki/개념/1,2-첨가와 1,4-첨가.md`에 같은 MVK/CN 골격을 사용한 단계별 설명 및 그림 7개를 추가했다.

1. O부터 세는 addition 번호와 IUPAC locant의 구별.
2. 1,2 공격의 두 전자쌍 화살표와 alkoxide.
3. 1,2 alkoxide의 protonation 및 cyanohydrin.
4. 1,4 공격의 세 전자쌍 화살표와 enolate.
5. Enolate의 O-protonation 및 enol.
6. Enol–keto tautomerization 순변환.
7. 원래 carbonyl/β 탄소를 추적하는 최종 생성물 비교.

생성물 판정과 시약·조건으로 선택성을 예측하는 문제를 구분하는 표, 확인 문제 3개와 해설을 덧붙였다. O⁻만 보고 alkoxide와 enolate를 혼동하거나 OH만 보고 1,2로 판단하는 오류를 설명했다. 모든 1,4 반응에서 enol이 분리되어야 한다는 인상을 피하도록 기존 개요도 수정했다. LUMO 계수만으로 β 탄소를 항상 우선 공격한다고 읽히던 기존 문장을 고쳤다.

## 출처와 제작

강의 PDF p.9를 렌더링하고 p.13의 보존 이미지를 열어 원본 구조와 설명을 확인했다. 중간체/전자 이동은 강의의 순변환을 설명하기 위해 분리한 보충 도식이다. Counterion 및 proton donor 잔기는 생략했고, tautomerization 화살표는 직접적인 무촉매 H 이동 elementary step이 아니다.

`tools/gen_l11_addition_guide.py` → `figures/L11/guide_*.json` → `tools/chemfig.py` 및 ReShiki 0.11.0-nightly.20261013 → SVG 7개. 기존 `mvk_cn_12_vs_14.json`의 공격 부분을 재사용하며 intermediate를 연결했다. 기존 그림 파일은 변경하지 않았다.

## 검수

- 7개 SVG XML 파싱 성공; 폭 319–438 px. 기존 0.62 표시 배율, 원자 약 18 px/캡션 약 14.5 px와 light/dark 색을 유지했다.
- 7개 × 양쪽 테마 = 14개 3배 PNG를 시각 검토했다. Cyanide lone pair 두 점과 화살표 머리/원자 라벨의 분리를 확인했다.
- 1,4의 C=C → C–C 화살표가 C–H 선을 지나는 것을 피하도록 곡률을 바꾸었다. 직선상 nitrile 탄소는 C 라벨을 명시하여 새 C–C 결합을 읽기 쉽게 했다.
- 실제 GitHub Markdown API 검사에서 인접한 수식과 대시의 조합으로 파싱되지 않은 구간을 발견해 문장을 수정했다. 최종 검사: L11 수식 326개, 개념 노트 58개; 수식 밖 미처리 LaTeX 후보 0.
- 두 문서의 로컬 Chromium/MathJax dark/light 네 화면: 수식 오류 0, 깨진 이미지 0, 820 px 본문 폭 초과 수식 0.
- `python3 tools/build_wiki_index.py`: 181개 wiki, broken links 0.
- `git diff --check` 통과.

이번 시각 검수는 신규 7개 그림에 한정한다. 실제 Obsidian 앱 내부 화면은 검수하지 않았다. 로컬 증거: `/home/kim/Documents/OChem-work/ochem-l11-addition-guide-20261019/`.
