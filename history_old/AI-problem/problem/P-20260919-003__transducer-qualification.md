---
problem_id: P-20260919-003
project_id: SONOFIELD_FPGA
active_version: v1
current_stage: V1_LAYOUT_AND_GOVERNANCE
status: OPEN
created_at: 2026-09-19T14:44:59.939171+00:00
created_by: Codex
chat_source_name: SonoField-FPGA
problem_hash: 012593556b514870efb68bbfba4a90d619bbfeb56ec8b016d23b82b334dece82
---

# Problem

## Decision Needed
B05/B06: qualify purchased 10 mm batch

## Goal / Current State
Preserve the chosen v1 architecture while closing hardware evidence gaps. Digital validation is available; hardware is not verified.

## Repository Facts
User selected 10 mm nominal body, 12 mm pitch, 128 positions and 90–115 mm face gap. Image gives no exact manufacturer part, continuous voltage rating, capacitance or measured active aperture. No physical levitation test exists.

## Evidence
v1/hardware/transducers/10mm_supplier_reference.md; v1/hardware/characterization/transducer_characterization.md; v1/docs/experiments/bringup.md
Baseline commit: ada1b2062756a2b852ed643a6eaa04fdc746323b. Current paths reflect authorized layout cleanup.

## What Codex Tried
Read supplied board/supplier references, documented contradictions, implemented and cross-validated the digital/model baseline. No physical measurements or guessed constraints were substituted.

## Root Cause Hypotheses
Missing primary hardware evidence, not an observed digital functional defect.

## Candidate Options / Preliminary Assessment
Obtain exact supplier datasheet and characterize samples before driver/PCB freeze. Retain the chosen geometry, use measured mounting offsets. Do not inherit electrical ratings from differently sized parts.
These are Codex proposals, not ChatGPT decisions.

## Constraints / Acceptance Impact
No fabricated pins, ratings, XDC or hardware PASS. Hardware acceptance remains blocked until supported by evidence.

## Questions For ChatGPT
What safe continuous excitation does the exact purchased part support? What measured tolerances and mounting offsets should constrain the carrier?

## User Approval Boundary
Version changes, fundamental scope/architecture changes, spending, fabrication release and public deployment need user approval.

## Delivery
OPEN; not delivered to external ChatGPT by a tool. Chat access is blocked.
