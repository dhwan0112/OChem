# L11 §6 iminium catalytic cycle — 2026-10-20

- Added four ReShiki-native JSON/SVG panels: condensation, conjugate addition, pyrrole rearomatization, hydrolysis/catalyst regeneration.
- Source: user-provided cycle and existing L11 p.21 attack structure. Preserved its stereochemical bonds; attached the pyrrolium positive charge to N explicitly.
- Expanded L11 readthrough and iminium catalysis wiki captions. Distinguished the connected cationic adduct from a zwitterion and rearomatization from product release. Condensation/proton transfers/hydrolysis are summarized, not exhaustive elementary mechanisms.
- Removed duplicated attack illustration in the wiki and repaired an existing bold/link delimiter issue.
- Generated with tools/gen_iminium_cycle.py and tools/chemfig.py, ReShiki 0.11.0-nightly.20261013. Generator uses local helpers without importing scripts with generation side effects.
- Visually reviewed all four panels in light/dark browser rendering; corrected two caption/structure spacing issues. Electron-pair dots and curved arrows in the addition panel remain distinct.
- GitHub Markdown API: 332 readthrough + 15 wiki math components; zero exposed delimiters/LaTeX commands in checked text.
- Chromium/MathJax in light/dark: zero math errors, broken images, or equations wider than 820 px.
- Wiki index builder: 181 documents, zero broken links. Pre-existing wiki index modification left unstaged.
- This is standalone browser QA, not live Obsidian-app theme verification.
- Local previews and QA outputs: /home/kim/Documents/OChem-work/ochem-iminium-cycle-20261020/
