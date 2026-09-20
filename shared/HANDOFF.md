# v2 bootstrap handoff

Goal and scope: user-approved full v2 inheritance, now complete; stop for review before deeper calibration work.
Inputs reviewed: formal v2 attachment, all nine BOM sheets, existing v1 implementation and evidence,
shared state/Problems, unchanged Zynq references and actual tool capability catalog.

Changes: v1 freeze commit 6cbf241 with 212-file hash manifest; full v2 copy with historical evidence segregated;
version metadata/audits, sparse-clone reproduction, unchanged BOM and CSV imports, AI checkpoint configuration.
Validated source commit e353c16d35da2b430f46ba5b83a5a9a79dd749b7, pushed and verified. Fresh report/evidence commit is subsequent Git history.

Tests: 19 inherited Python tests, Icarus multi-size/serializer/fault/map tests, Vivado 2025.2 XSim and three
repeat traces, independent waveform reference, model/coordinate exports, nine interaction tests and BOM audit.
Clean sparse clone without v1 and new venv PASS; six model / 19 coordinate CSVs equal. No core test skipped.
Evidence: v2/evidence/validation, model, bootstrap, reproducibility and synthesis_gate.

Failures/limits: expected Vivado target gate BLOCKED_BY_BOARD_FACT; no synthesized or physical result.
Earlier optional XLSX metadata lookup was absent; subsequent complete source-cell audit passed unchanged.
Board facts, physical serializer margin and TX/RX qualification remain open. External ChatGPT BLOCKED,
Codex capture PARTIAL. No background capture hook; next checkpoint saves the final visible response.

Decision boundary: user approved v2, not v3 or fabrication. Old v1 Problems remain provenance records,
not automatically applicable decisions. BOM old version text is superseded by explicit current user instruction.
Next action: review scoped report_v2.md; proposed V2.2 calibration model. Hardware remains NOT_RUN.
Scope result: ACCEPT WITH LIMITATIONS. Full self-calibrating platform not accepted.
