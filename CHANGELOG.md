# Changelog

## v2 — team handoff checkpoint (2026-09-29)

- Fresh GitHub clone + independent venv: supported full-history v2 sparse setup passes 112 Python tests and AXI Icarus/XSim checks. Full-checkout frozen-v1 audit has 135 CRLF/LF-only mismatches; failure evidence is retained and the guide documents the supported route.
- Added root 指南.md with progress, resolved/open issues, ownership proposals, portable Windows setup,
  exact-commit validation copies, evidence interpretation and gated next development steps.
- Linked the guide from README and clarified current stage/authorization in AGENTS.
- Annotated progress checkpoint tag `v2-board-transport-offline-20260929`; no Release or version upgrade.
- Functional source/RTL and frozen v1 remain unchanged; handoff checks are recorded under
  evidence/engineering/handoff_20260929. Local-only board originals and existing schematic backup
  remain explicitly outside the Git delivery.

## v2 — board transport and PS/PL offline preflight (2026-09-27)

- Persisted photo-confirmed XC7Z020/CLG400 while keeping speed/temperature/full ordering code unknown.
- Audited 101 primary constraints and 346 total claims against Vivado CLG400 balls and AMD UG865;
  retained connector conflicts and found CEC=J5 is PS DDR. No production XDC or PCB change.
- Added gated SerialBoardTransport, generated binary protocol constants, host-tested C PS service,
  and AXI4-Lite/native bridge with real-system tests under Icarus and Vivado 2025.2 XSim.
- Python suite:112 tests passed. Live COM4 remains unopened and map/motion capability stays disabled.
- Fixed calibration buffer RAM inference with an equivalent synchronous write process. All three
  CLG400 candidates synthesize to 8681 LUT,17996 registers,4 BRAM; 132 MHz core timing fails
  (-8.128/-4.995/-3.609 ns). P-20260927-001 requests a timing-closure decision.
- Evidence and final regression/reproduction status: v2/evidence/board_transport/RESULT.md.
  No download, external output, release, deployment or v3; independent review remains pending.

## v2 — board-only identification (2026-09-27)

- Windows/D2XX confirmed FT2232H 0403:6010 with interfaces A/B and COM4 on B.
- Vivado 2025.2 read ARM DAP 0x4BA00477 and xc7z020 0x23727093 twice.
- Archived filtered evidence and local-only raw device inventory; no programming or driver changes.
- Added exact-part/silicon validation before target project creation and seven offline gate tests.
- B01 remains blocked on package/speed; B03 remains blocked on VCCO/connectors/PS wiring.
  No PCB/RTL or frozen v1 changes; BoardTransport hardware execution remains disabled.

## v2 — interactive motion digital stage (2026-09-27)

- Added a local simulation UI, bounded quintic/planar trajectory planning, calibrated
  LEVITATION_TRAP_V1 inspection and explicit operator-confirmation/STOP states.
- Reused the existing Controller, calibrated model and phase engine; added a complete-map
  stream API, clocked ring buffer and integrated motion wrapper with atomic ACK validation.
- Full 3696-frame GUI demonstration matched across three Icarus runs and Vivado 2025.2 XSim.
  Production 50 Hz cadence and failure injection passed both tools; final Python suite has 90 tests.
- Preserved failed tool evidence and fixed XSim declaration/launcher compatibility, latched
  STOP recovery, Windows DPI screenshot bounds and existing adjacent problem-digest auditing.
- Frozen v1 and all PCB source files remain unchanged. No physical motion, board deployment,
  independent acceptance, release or v3 is claimed. Engineering evidence is under evidence/engineering/motion.
- Applied 2026-09-27-r1 ownership rules; Work remains OFF. The current user explicitly authorized
  the six stage docs and observable interaction checkpoint as task-specific exceptions.

## v1 — observable interaction memory

- Added real local Codex transcript capture, session/tool register, index and checkpoint instructions.
- Added privacy filters, source matching, repeat sync and hash integrity tests. No hidden reasoning exported.
- External ChatGPT remains BLOCKED; Codex source coverage is explicitly PARTIAL.

## v1 — layout and governance

- User authorized same-version local/GitHub organization and removal of obsolete version records.
- Consolidated runnable code, dependencies, scripts, docs, hardware and fresh evidence under v1/.
- Root holds shared state, version gate, ChatGPT source records and evidence-backed Problem records.
- Chat source SonoField-FPGA recorded with BLOCKED access; no imported messages or invented decisions.
- Path-dependent tools and run guide updated. Existing Git history retained.
- Full local and clean-checkout Python/Icarus/XSim gates PASS; six model and 19 coordinate/phase CSVs identical.
- 12 board source files and RTL/TB/tests unchanged; obsolete current-tree records and old clone caches removed.

## v1 — established functional baseline

- Shared 40 kHz phase reference, requested/calibration separation, atomic map updates and safety gating.
- 128 positions, 10 mm nominal diameter, 12 mm face-center pitch, 100 mm nominal face gap, 90–115 mm travel.
- Python reference model and Icarus/Vivado XSim cross-validation; hardware gates remain open.

## v2 — authorized bootstrap

- Freeze v1 intact; copy the complete project into v2, including independently archived historical evidence.
- Import user BOM unchanged with all sheets as CSV; current version governed by explicit v2 approval.
- Add frozen-parent/standalone checks and version-aware interaction metadata. Fresh verification recorded in v2.
- Calibration/ADC/PCB implementation remains subsequent work.


## 2026-09-21 — v2 software/digital self-calibration

Added four-lane AD7606B startup/readback/acquisition, 128-TX scanning, bounded host-ACK buffer,
calibration/field modes and runtime frequency, standalone Python raw-to-LUT calibration, source
configuration and hardware interface contract. Added 25 Python tests and CAL-TB01..15, exact
ADC roundtrip and deterministic/noise evidence. Frozen v1 unchanged. No PCB or hardware claim.

## 2026-09-24 — v2 software/digital delivery

- Corrected stale serializer permission on abort/re-enable; uploaded computed common frequency with LUT.
- Added per-path quality/report output and final 45-test full gate.
- Fresh clone/new locked venv without v1 passed all Python/Icarus/XSim/audit/model/coordinate checks.
- Preserved initial newline-hash audit failure; source evidence now uses explicit canonical LF text.
- Verified renamed workspace, updated operational paths and session-scoped transcript relocation check.
- Source 9c058fe3b02469a6d36a08e3a7cbedd19076e67b pushed; no frozen v1/PCB/hardware-result changes.

## 2026-09-26 — v2 schematic V1 draft
- Captured128TX/8RX, serializer/level translation, ADC/AFE and three power domains in native EasyEDA.
- Consolidated83modules into one named, partitioned sheet; exported vector PDF/SVG and corrected ADC label alignment.
- Native3992-pin and independent1338-pin mapping audits pass;212 frozen v1 files unchanged. ERC45warnings retained and classified.
- Electrical release remains REVISE; no PCB or hardware result. Persisted pwsh preference and observable interaction checkpoint.
