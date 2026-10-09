---
problem_id: P-20260919-002
project_id: SONOFIELD_FPGA
active_version: v1
current_stage: V1_LAYOUT_AND_GOVERNANCE
status: OPEN
created_at: 2026-09-19T14:44:59.938171+00:00
created_by: Codex
chat_source_name: SonoField-FPGA
problem_hash: a43d10626a92859139b1cfb1e6336939c87f24dbfc379ef40433c8ac5514f295
---

# Problem

## Decision Needed
B04: select electrically feasible output expansion

## Goal / Current State
Preserve the chosen v1 architecture while closing hardware evidence gaps. Digital validation is available; hardware is not verified.

## Repository Facts
Candidate 32 lanes with four used outputs each is simulated at 132 MHz core / 66 MHz shift clock. 128 arbitrary 8-bit phases require 10.24 MHz state refresh. Digital PASS does not establish component timing, loading or PLL feasibility.

## Evidence
v1/docs/hardware/interface.md; v1/rtl/output/serializer.sv; v1/tb/tb_serializer_fault.sv; v1/evidence/validation/summary.json
Baseline commit: ada1b2062756a2b852ed643a6eaa04fdc746323b. Current paths reflect authorized layout cleanup.

## What Codex Tried
Read supplied board/supplier references, documented contradictions, implemented and cross-validated the digital/model baseline. No physical measurements or guessed constraints were substituted.

## Root Cause Hypotheses
Missing primary hardware evidence, not an observed digital functional defect.

## Candidate Options / Preliminary Assessment
Qualify the current candidate against worst-case timing, voltage/fanout/routing and verified board clock generation; compare another output expander if it cannot satisfy timing. Added component cost or fundamental architecture changes need user approval.
These are Codex proposals, not ChatGPT decisions.

## Constraints / Acceptance Impact
No fabricated pins, ratings, XDC or hardware PASS. Hardware acceptance remains blocked until supported by evidence.

## Questions For ChatGPT
Is the candidate electrically achievable with documented margins? What interface must be measured before PCB freeze?

## User Approval Boundary
Version changes, fundamental scope/architecture changes, spending, fabrication release and public deployment need user approval.

## Delivery
OPEN; not delivered to external ChatGPT by a tool. Chat access is blocked.
