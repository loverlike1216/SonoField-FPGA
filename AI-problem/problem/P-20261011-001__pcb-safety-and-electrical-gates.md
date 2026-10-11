---
problem_id: P-20261011-001
project_id: SONOFIELD_FPGA
active_version: v5
current_stage: PCB_S2_REVIEW
status: OPEN
created_at: 2026-10-11T04:15:29.323861+00:00
created_by: Codex
chat_source_name: SonoField-FPGA
problem_hash: ff10749ee46342eae17ecc5eff632b9131055199be6eb2cfb0583c16d79ec77f
hash_scope: UTF8 LF body after closing frontmatter plus blank line
---

# PCB safety and electrical decisions required

## Decision Needed / Goal
Approve a concrete next-stage design direction that retains v5/AX7020/128TX8RX/C16/12V single-ended/geometry/protocol, implements default-off independent protection and enables honest passive specifications. TPS3851H33EDRBR x2 direction is already user-approved, but functional safety closure is not.

## Current State / Repository Facts
PCB worktree feat/v5-pcb-design based on Draft PR5 head 8c27b5841b5494c3761ab211881a3ea2be63e8c8; original workspace and unmerged main unchanged. Current prepcb_supervisor.sv line29 toggles heartbeat from timer tick independent of state progress. Existing SCHEMATIC_STATUS and ADR042 require independent window watchdog. New TPS3851 is a timeout watchdog; WDO pulses, RESET assertion makes WDO high-Z, below POR outputs undefined. No native schematic/ERC or qualified cutoff latch/FET network exists.

## Evidence
TPS3851 RevB pp5-7,17,23; TPS2663 RevG pp7,18,30; INA226 RevC p5; manufacturer URLs and hashes in v5/hardware/pcb/reviews/20261011_s2 and v5/evidence/pcb_s2_20261011. Current 243 tests and full3696x3Icarus+1XSim/nextstage digital baseline PASS. These prove only their offline scope. Workbook independently counted1205; approved supervisor-only replacement arithmetic1203. Old1.65k is invalid for TPS26631, 20mOhm*5A=100mV exceeds INA22681.92mV; C0/motional load/AFE/VCCO/externalSTA unknown.

## What Codex Tried / New Information
Read actual fixed-commit hardware files for four requested projects plus supplementary HV583 schematic; read primary datasheets, inspect current heartbeat RTL, independently parse workbook, calculate energy/LC/timing/threshold/range corners, cross-check numerical time-domain models. Preserved first fetch/extraction failures. Did not change RTL, lower35dB, invent loads, open archive bodies, operate board or release manufacturing.

## Root Cause Hypotheses
Old BOM contains functions and quantities before actual circuit design. Part-family substitutions do not preserve window/kill behavior. Free-running heartbeat checks clock presence, not useful control progress. Multi-domain fail-off and power/range coordination are unspecified at component level.

## Candidate Options
A (recommended for next-stage review): retain approved TPS3851x2; add independent too-early/window detector, progress-qualified heartbeat, cold-start-off fault latch/manual rearm and physically biased back-to-back cutoff/discharge. Extra device count is TBD until a concrete circuit is reviewed. Preserve required safety criteria.
B: request a different integrated window supervisor and re-review exact replacement; changes explicit approved part, requires user approval. Still needs physical cutoff/latch/discharge.
C: accept timer heartbeat, omit window and connect WDO directly to power enable. Rejected by current evidence and invariants; cannot justify release.
Power A: keep12V single-ended TC4427 with damping footprints; retain60W capacity candidate/40W controlled-current alternative, measure real load and coordinate ILIM/TVS/jack/shunt/SOA. Power B: bridge/differential is comparison only, requires separate architecture authorization.

## Constraints / Acceptance Impact
No v6/core/protocol/geometry change or main merge; no board/image/DDR/Flash/ultrasound operations.35dB and all243original tests/goldens unchanged. S2-C remains BLOCKED and BOM/HW/ERC/manufacturing HOLD while P0s open.

## Questions For User / Main Chat
1. Accept A as the next-stage circuit design scope, including independently qualified window/latch/cutoff and extra components, or request revised integrated supervisor?
2. What allowed heartbeat/startup/stop-to-safe timing applies; may the next-stage task implement progress tokens instead of timer heartbeat while preserving current protocol?
3. Accept measurement-first12V single-ended/60W-capacity direction and revised protection/shunt coordination, plus central5V regulation/CC budget review before freezing RCL?
4. Supply qualified TX/RX/load/VCCO/cable facts and an independent electrical review of the concrete candidate before native schematic/BOM release.

## User Approval Boundary
Existing approval authorizes this review, independent worktree and TPS3851x2 direction only. It does not approve newly proposed safety circuitry/RTL edits, a reduced safety contract, bridge drive, manufacturing, purchasing or hardware writes. External ChatGPT access BLOCKED; no fabricated external Decision. A real new decision must match this ID/body hash/v5.
