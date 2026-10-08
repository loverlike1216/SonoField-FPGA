# Directory audit — 2026-10-08

PROJECT_ID SONOFIELD_FPGA; main; source `851d1ef747cd95da13e5eb0705b5a7885b68d83c`. User authorizes existing empty v5 for AX7020. No engineering file moved/deleted/renamed during this audit.

A=current management/dependencies; B=selected reusable v2 files (separate VERSION_MIGRATION_PLAN); C=formal history; D=historical reference; E=rebuildable/runtime candidates. Classification alone never authorizes deletion.

| Original path | Class / purpose | Git tracked / inventoried | References | Historical evidence | Action / target | Risk |
|---|---|---|---|---|---|---|
| .git | A / Repository history | 0 / 0 | 0 | False | KEEP / .git | Unmodified |
| .gitattributes | A / Root governance/entry file | 1 / 1 | 0 | False | KEEP_UPDATE_CURRENT_ONLY / .gitattributes | Preserve prior contents through Git/snapshot |
| .gitignore | A / Root governance/entry file | 1 / 1 | 0 | False | KEEP_UPDATE_CURRENT_ONLY / .gitignore | Preserve prior contents through Git/snapshot |
| .venv | A / Existing pinned Python dependencies | 0 / 0 | 0 | False | KEEP / .venv | Required until v5 environment verified |
| .Xil | E / Vivado runtime/cache | 0 / 0 | 0 | False | KEEP_IGNORED / .Xil | May belong to live process; no cleanup |
| AGENTS.md | A / Root governance/entry file | 1 / 1 | 0 | False | KEEP_UPDATE_CURRENT_ONLY / AGENTS.md | Preserve prior contents through Git/snapshot |
| AI-chat-memory | A / External ChatGPT source and access limits | 3 / 3 | 0 | False | KEEP / AI-chat-memory | Do not fabricate history |
| AI-interaction-memory | A / Observable AI/tool provenance | 37 / 37 | 0 | False | KEEP / AI-interaction-memory | Preserve historical payloads |
| AI-problem | A / Original problems and decisions | 11 / 11 | 0 | False | KEEP / AI-problem | Old version provenance retained; no automatic v5 execution |
| BOM | D / User originals, canonical v2 import exists | 1 / 3 | 13 | False | KEEP_IN_PLACE / BOM | Referenced historical source; manufacturer/user assets |
| build | E / Root generated tool products | 0 / 0 | 103 | False | KEEP_IGNORED / build | Need reference/process inspection; no blind removal |
| CHANGELOG.md | A / Root governance/entry file | 1 / 1 | 0 | False | KEEP_UPDATE_CURRENT_ONLY / CHANGELOG.md | Preserve prior contents through Git/snapshot |
| dfx_runtime.txt | E / Untracked Vivado runtime file | 0 / 1 | 0 | False | KEEP_IGNORED / dfx_runtime.txt | Inspect live processes; preserve user/runtime bytes |
| evidence | C / Historical root verification/handoff evidence | 182 / 182 | 116 | True | KEEP_IN_PLACE / evidence | Cross-document references; do not move entire tree |
| parameter_detection | D / Prior real DDR/JTAG evidence and private raw data | 21 / 36 | 22 | True | KEEP_IN_PLACE / parameter_detection | Historical result links and private originals; never v5 hardware facts |
| PCB | D / Historical native schematic, libraries and untracked backup | 67 / 109 | 37 | True | KEEP_IN_PLACE_COPY_REFERENCE / PCB | Old paths used in reports/scripts; no high-risk move |
| README.md | A / Root governance/entry file | 1 / 1 | 0 | False | KEEP_UPDATE_CURRENT_ONLY / README.md | Preserve prior contents through Git/snapshot |
| shared | A / Current state and historical recovery metadata | 24 / 27 | 0 | False | KEEP_UPDATE_CURRENT_ONLY / shared | Prior state snapshot saved before activation |
| v1 | C / Frozen original engineering | 212 / 213 | 39 | True | KEEP_IN_PLACE / v1 | Moving breaks historical paths; no relocation |
| v2 | C / Latest validated digital source and Robei evidence | 2255 / 2756 | 135 | True | KEEP_IN_PLACE_COPY_SELECTED / v2 | Preserve bytes/history and old reproduction paths |
| v3 | C / User-paused incomplete historical draft | 0 / 32 | 3 | True | KEEP_IN_PLACE / v3 | Untracked files registered; not promoted to v5 baseline |
| v5 | A / User-created AX7020 active development destination | 0 / 0 | 0 | False | POPULATE_BY_COPY / v5 | Initially empty; never overwrite user files |
| vivado_pid39068.str | E / Vivado runtime trace | 0 / 1 | 0 | False | KEEP_IGNORED / vivado_pid39068.str | No active process/cache deletion |
| Zynq7020 | D / Old Robei original board documents | 0 / 12 | 46 | True | KEEP_IN_PLACE / Zynq7020 | Old scripts reference root; historical reproduction retained |
| 指南.md | A / Root governance/entry file | 1 / 1 | 0 | False | KEEP_UPDATE_CURRENT_ONLY / 指南.md | Preserve prior contents through Git/snapshot |

## Preservation and current facts

Per-file byte hashes: HISTORICAL_HASHES_BEFORE.json. Private raw paths additionally covered by local_raw/preservation_hashes_before.json, not published. Cache and .venv internals are retained in place, not claimed exhaustively inspected.
Historical versions/root PCB/Zynq7020/parameter_detection/evidence have cross-path references. They stay in place, read-only for normal v5 development; moving them is unnecessary and would risk reproduction. No high-risk movement is proposed in this iteration.
v4 does not exist and will not be fabricated. v3 is untracked paused history, not a validated source. Latest validated functional source is v2 at9936a737c45bf61f1908863a94f6374c6b5c828c, with subsequent detection/docs commits through startingHEAD. No old PASS is inherited as v5 PASS.
Low-risk archival scope after v5 baseline: copy prior root management snapshots and categorized historical indexes into archive; do not relocate referenced native engineering. Runtime/cache files stay ignored; live Vivado is not terminated.
External ChatGPT history capability remains BLOCKED; current source observable Codex record will be PARTIAL. No independent review invented.
