# Enamine conjugate addition 일반형 — 2026-10-20

사용자 제공 그림의 세 단계를 ReShiki 0.11.0-nightly.20261013과 기존 `tools/chemfig.py`로 다시 작성했다. 생성기는 `tools/gen_enamine_general.py`, 편집 가능한 최종 스펙은 `figures/L11/enamine_general_*.json`이다.

- Enamine formation, conjugate addition, aqueous work-up의 SVG 3개를 L11 통독 §5.2 시작과 enamine wiki에 삽입했다.
- 원본의 일반형 R¹/R²/R³/Z, N lone pair, 네 전자쌍 화살표, iminium N⁺/enolate O⁻, 새 C–C 결합 및 최종 탄소 번호 1–5를 유지했다. 반응 중심 H는 명시했다.
- 중간체의 총전하 0, carbonyl 탄소를 포함한 1,5 관계, NR₂와 R²의 구별, 산성 후처리에서 amine의 protonation 가능성을 캡션에 설명했다.
- 출처는 사용자 제공 그림과 기존 L11 p.18–19 및 Clayden p.608의 저장소 설명이다. 이번 작업에서 교재 PDF를 새로 대조했다고 주장하지 않는다.
- 기존 원자/캡션 크기와 0.62 표시 배율을 유지했다. SVG 폭은 formation 463 px, addition 547 px, work-up 686 px이다.
- 3개 SVG의 dark/light 3배 렌더링 6개를 시각 검토했다. N 전자쌍 화살표를 라벨 바깥으로 휘게 수정하고, iminium 전하와 중간체 H/R 라벨 겹침을 수정했다.
- GitHub Markdown API/로컬 MathJax 검수 중 enamine wiki의 기존 깨진 반응표, 강조 및 각주 수식 문제를 찾아 반응표와 설명문으로 정리했다. 신규 L11 삽입 구간은 파싱 오류가 없었다.
- 최종 검수 결과는 로컬 `github-parser.json`, `browser-qa.json`에 기록했다. 실제 Obsidian 앱 검수는 수행하지 않았다.
- Wiki index: 181개 문서, broken links 0. `git diff --check` 통과.

로컬 증거: `/home/kim/Documents/OChem-work/ochem-enamine-general-20261020/`.
