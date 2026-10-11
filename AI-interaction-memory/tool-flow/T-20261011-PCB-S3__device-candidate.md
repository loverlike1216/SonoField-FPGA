# Observable PCB-S3 tool flow

Project SONOFIELD_FPGA; version v5; branch feat/v5-pcb-design; base 23f8d4cedb44536f8c35fd132171868a80f9ded7; thread 01a128e6-4c68-7ba1-aa87-0d9f17c36f8b. Status PARTIAL: significant observable actions/results through candidate validation; later publication is separately recorded. No hidden reasoning or external ChatGPT output.

## Trigger and boundaries

Actual user approved the S3 engineering document and replied “按 S3 文件完整执行，保持 v5、制造/采购/板写/main 合并 HOLD”. Canonical instruction in codex/instructions; actual hash and problem/body/version verification in S3 DECISION_VALIDATION.json. This allows offline device candidate and normal Draft PR6 synchronization. No native EDA client connected; no board or driver operations executed. Original workspace status/HEAD only; private BOM and historical archive bodies not read.

## Tools, observable results, failures

1. PowerShell 7 / Git / gh: current-only preflight, branch/HEAD/remote and public PR chain checked. Base 23f8d4c, sole active v5. Original workspace retained; historical tree identity checked as metadata only. PREFLIGHT.json records observations.
2. EasyEDA skill/API capability inspection: no connected native client; native schematic NOT_CREATED / ERC NOT_RUN. Strict component/pin/net exports plus 27 vector pages and searchable REVIEW.html used as permitted fallback. This is not native CAD or real ERC.
3. Web primary-source lookup and Python source retrieval: current TI/ADI/Microchip/onsemi/Mean Well/Same Sky/GCT/Littelfuse documentation inspected. SOURCE_MANIFEST.json lists URLs, actual retrieval results, hashes and boundaries. First-pass manifest and failed downloads retained. Raw PDFs/text stay in ignored local_raw. S2 open-source experience is background only; no third-party code copied or novelty claimed.
4. Python deterministic candidate generation: inputs.json, power_worst_case.py, build_candidate.py, build_reports.py produce the power calculations, strict 2126 component / 6390 pin exports, 128 TX mappings, 1541 passive positions, connector/geometry tables, RX RC model, drawings and reports. Circuit choices and unresolved assumptions are explicit in reports 03–11.
5. Independent export-level static review_candidate.py: 45 semantic checks PASS; 256 Boolean safety combinations; zero board-local singleton nets. Earlier J11 test misclassified two OPEN_DRAIN I2C contacts as power NC; failed report preserved and classification corrected using approved pinmap. No test/golden/threshold changes.
6. Bundled @oai/artifact-tool / Node: two XLSX workbooks authored, rendered and visually inspected. Python stdlib XLSX XML verification: 249 power + 236 BOM cached formulas, 252 numeric comparisons PASS; no missing formula caches or Excel error cells. This verifies generated artifacts, not a live Excel runtime or physical design.
7. Edge headless with clone-local temporary browser profile: pin-labelled safety SVG rendered and visually inspected. Other generated SVGs follow the same explicit pin/net layout. PNG previews remain local/ignored.
8. Original digital regression: fresh `python -m unittest discover -s v5/tests -v` with clone-local CC/TMP/TEMP/PYTHONPATH; 243 tests PASS. Full 3696-frame × 3 Icarus + 1 XSim regression is inherited S2 evidence and not rerun for this no-digital-change stage. No new synthesis/implementation/hardware evidence claimed.
9. Current structure/inheritance/protected hash/frozen Git metadata checks and hardware models are recorded in FINAL_VERIFICATION.json. S3 static checks were added to existing workspace-integrity CI. Secret/privacy scan runs against explicitly staged current files before publication.
10. State/ADR044/actual-user Decision addendum/CP003 and observable interaction records written. Final normal commit/push/Draft PR6 update, remote/CI verification and main/original-workspace preservation are recorded in PUBLICATION_RECEIPT.json after execution.

## Evidence and result

Canonical artifacts: v5/hardware/pcb/reviews/20261011_s3. Tool evidence: v5/evidence/pcb_s3_20261011. Observable tool event hashes: codex/S-20261011-pcb-s3-001.tools.json.

Candidate asset delivery ACCEPT WITH LIMITATIONS; PCB-S3 / whole platform REVISE. G1 native CAD/independent review, G2 power/fault/thermal, G3 AFE/protection/power-off isolation, G4 actual digital/constraints integration, G5 mechanical/SKU qualification remain. No model self-certification, manufacturing, procurement, board write or main merge.
