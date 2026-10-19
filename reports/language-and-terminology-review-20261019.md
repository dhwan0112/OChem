# L11–L17 한국어 표현·영어 전문용어 정리

검수일: 2026-10-19. 기준 commit: `3d8574f8d572796d5a0971d3707cdaaf64df6a13`.

사용자가 제공한 E/F 기반 71개 후보를 현행본 조사 기준으로 사용했다. 이 71개는 현행 오류 수가 아니며, 오래된 표현을 현행본에서 발견한 것처럼 기록하지 않았다. 이번 작업은 로컬 현행 브랜치의 실제 파일을 대상으로 했다.

## 범위

- 통독본 L11–L17 7개 전체 소스: 수정 전 5,224행. 제목, 본문, 표, 캡션, 각주, 문서 안의 연습문제를 포함한다.
- 관련 `practice/L11_Exercises.md`–`L17_Exercises.md`와 `L12_Practice.md`: 8개.
- 관련 위키 6개: HSAB, Diels–Alder 반응, peptide synthesis, Grignard reagents, Boc, Fmoc. 위키 대문은 기존 스크립트로 재생성했다. 위키 전체 181개에 대한 언어 전수조사는 아니다.
- 통독본의 Markdown 이미지 참조 156곳, 고유 SVG 138개에서 SVG `<text>` 라벨을 추출했다. 7개 SVG에 한국어가 있었으며 색상·설명·보호/제거 등의 라벨이 포함되어 있다. 그림은 이번 commit에서 수정하지 않았다. `<text>`가 아닌 path로 그려진 글자의 OCR이나 모든 기작 그림의 전자쌍·화살표 배치 재검수는 이번 검사의 범위가 아니다.

## 적용한 원칙과 대표 변경

| 문맥 | 변경 |
|---|---|
| L11 HSAB | ‘단단한 유기금속’을 hard organometallic nucleophile로 수정. hard/soft와 strong/weak를 구별하고 polarizability를 명시 |
| L11 resonance | contributor의 +1 formal charge와 실제 분자의 polarization을 구별. Contributor를 연속 intermediate로 읽지 않도록 설명 |
| L11 NMR | deshielding을 전하량의 직접 측정으로 해석하던 단정을 제거 |
| L11 시약 비교 | Grignard reagents vs organocuprates. 촉매 조건에서 생성되는 organocopper species와 preformed organocuprate를 하나로 치환하지 않음 |
| L12 reagent 소모 | Grignard가 ‘파괴된다’를 proton donor와의 acid–base reaction에 의한 소모로 수정 |
| L12 protecting groups | ‘아킬레스건’, ‘특효약’, ‘거울상처럼 보완’ 등의 비유를 제거하거나 조건과 반응성을 명시 |
| L12 carbamate | N lone pair의 delocalization과 nucleophilicity/basicity 감소를 설명. Boc에 해당하는 chloroformate를 Cbz라고 적은 문장 수정 |
| L12 SPPS | 단계별 세척이 가능하다는 장점과 최종 peptide 정제의 필요성을 구분 |
| L13–L14 concerted | 하나의 elementary step과 두 결합의 동일한 형성 정도를 구별. Asynchronous TS 설명 및 캡션 수정 |
| L14 강의 문구 | 실제 L14 PDF의 “Concerted, but unsymmetrical transition state”를 확인. 기존 unsynchronous 표현을 정리 |
| L13–L17 allowed | orbital-symmetry-allowed의 조건을 명시하고 실제 반응 발생·속도를 보장한다는 표현을 제한 |
| L15 FMO | normal-electron-demand Diels–Alder 문맥을 명시. 모든 diene이 같은 전자적 성격을 가진다는 일반화를 제거 |
| L15 nitrone | 제시된 exo 예시를 모든 nitrone 반응의 보편 규칙이나 thermodynamic 안정성으로 확장하지 않도록 수정 |
| L16 atom mapping | ‘안팎이 inside out’을 끊어지는 C–O 결합, 새 C–C 결합의 말단, 이중결합 위치를 따라 읽는 설명으로 교체 |
| 복합어·음차 | diene오필, pyrrole린, methyl프로펜, methyl아제티딘 등의 혼합 표기를 dienophile, pyrroline, methylpropene, methylazetidin 등으로 정리 |

일반 한국어 설명과 원자·결합·양전하·음전하·전자 수·온도·수율 같은 기본어는 유지했다. 같은 면/반대 면을 기계적으로 suprafacial/antarafacial로 바꾸지 않았다. Electron-deficient와 electrophilic, polarization과 polarizability, functional-group protection과 steric shielding을 동의어로 취급하지 않았다. 문서 파일명과 링크 목적지는 유지했다.

예비 목록의 T69에 해당하는 ‘O는 음성(nucleophilic)’ 표현은 현행 `practice/Tutorial_4.md`의 해당 설명과 일치하지 않았다. 현행에는 이미 nucleophilic/electrophilic 문맥과 공식 답안에 대한 검토 의견이 있으므로 과거 표현을 현재 오류로 집계하지 않았다. ‘멀리서 더하기’, ‘C=O가 뜨거울수록’ 같은 과거 제목도 현행에 그대로 남은 오류라고 집계하지 않았다.

## 출처와 검증 범위

문장별 기존 강의·교재 출처는 보존했다. Concerted/asynchronous 구분은 로컬 Clayden 인쇄 p.889–890의 설명과 L14 PDF p.13의 문구를 대조했다. 기존 L11·L12·L16 보충의 source page 정보는 유지했다. 이번 언어 편집을 모든 수율·구조·기작에 대한 새 독립 검증으로 간주하지 않는다.

언어상 모호한 후보를 소스 전체에서 검색하고 주변 문장을 검토했다. ‘한국어 표현에 더 이상 개선점이 없다’는 판정이나 71개 후보가 모두 현행 오류였다는 판정은 하지 않는다.

## 렌더링 및 회귀 검사

- 편집한 본문 21개를 실제 GitHub Markdown API로 파싱: 수식 밖에 노출된 `$`, 주요 LaTeX 명령 및 `**` 없음.
- 파싱 결과를 Chromium/MathJax로 dark/light 각각 렌더링: 42개 화면 조건, 수식 1,551개. MathJax 오류, 깨진 이미지, 820px 본문 폭을 넘는 수식 각각 0개.
- 통독본 정적 Markdown 검사: 발견 항목 0개.
- 관련 기존 테스트 7개 통과. 링크 목록 재생성 후 깨진 링크 0개.
- 언어 편집 중 관련 연습문제·위키에서 발견된 기존 inline `aligned`, 수식과 강조 문법 충돌, 수식이 들어간 링크 라벨·각주의 GitHub 파싱 문제도 수정했다.
- 이 검증은 GitHub 파서 결과를 이용한 로컬 브라우저 렌더링이다. 실제 Obsidian 앱과 GitHub 웹 UI에서 직접 확인한 결과는 아니다.

검사 산출물과 원본 스냅샷은 `/home/kim/Documents/OChem-work/ochem-language-review-20261019/`에 모았다. `github-parser.json`, `browser-qa.json`, `image-language-inventory.json`, `source-invariants.json`, `context-edits.json`, `lexical-edits.json`, 원문 snapshot과 source excerpt를 포함한다.
