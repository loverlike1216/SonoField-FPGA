---
problem_id: P-20261010-001
project_id: SONOFIELD_FPGA
active_version: v5
current_stage: NEXTSTAGE_S4_S7
status: OPEN
created_at: 2026-10-10
created_by: Codex
chat_source_name: SonoField-FPGA
problem_hash: 9cc8f62962b6ed42c4f282cd239303fe01faefb1fd670d9a0fbaef61e7171d3d
---

# Decision needed: inherited capture BRAM asynchronous controls

## Goal / current state

Preserve128TX/8RX, signed1024frame capture/timestamps/ACK, fail-closed safety, atomic maps and original tests while closing actual AX7020 implementation risk. C-16 direction is already user-approved; no device redecision is needed. Source implementation commit6274330f98955fa0d4c4703a90d31bc1421104fb. Main and frozen archive unchanged, real board untouched.

## Repository facts and evidence

`v5/rtl/calibration/calibration_scheduler.sv` remains unchanged from the validated baseline. The routed C-16 top at132MHz has WNS+0.038ns/WHS+0.068ns, TNS/THS0 but161inputs/148outputs without qualified external IO delays. `v5/evidence/next_stage/20261010/expanded_current2/drc_reopened.rpt` and `all_drc_violation_properties.txt` show346REQP-1839 warnings plus1ZPS7-1 OOC warning. Rule severity and enabled status unchanged. The default20limit had hidden remaining pins; MAX_MESSAGES=-1 retained truncation, actual explicit100000 exposed346 without CHECK-3. Complete rule properties are saved.

Asynchronously reset address/data/enable registers drive inferred RAMB36E1 controls (frame_count, selected buffer state and data paths). Vivado warns of possible memory/read corruption on asynchronous reset assertion not analyzed by normal STA. Empty CDC output excludes unqualified IO and is not proof of safe asynchronous reset behavior. This is not a new simulator failure and positive OOC slack does not resolve it.

## What Codex tried / limits

Fresh native synthesis/place/route and checkpoint reopening, full property enumeration, explicit reporting-limit investigation, current v5-only source audit and independent clone native rebuild. No waiver, severity downgrade, false path, historical-source read, reset architecture edit, programming or memory write. The offline regression remains separate from release acceptance.

## Candidates / preliminary assessment (Codex, not ChatGPT)

- A: Keep asynchronous emergency output kill, but redesign RAM-facing control/address/data publication with synchronous reset and a qualified restart/ownership boundary. Likely best review direction; latency, recovery behavior, synthesis inference and capture integrity must be verified.
- B: Separate RAM control registers from asynchronously reset state, explicitly disable write/read before reset transitions and restart after synchronized release. Requires proof for assertion, clock-stop, partial capture and ACK ownership; cannot merely suppress warnings.
- C: Accept existing warnings for deployment. Rejected pending independent proof; current evidence cannot justify release.

## Required validation / acceptance impact

Independent electrical/RTL reviewer must select an actionable design and constraints. Preserve original tests/goldens/35dB and add reset-at-every-capture-state, partial-write/clock-stop, ownership/recovery and two-tool tests. Rerun full current baseline, native fullPS/PL route, complete DRC/CDC and external min/max timing after actual Rev3 facts. Do not change criteria to obtain PASS. Hardware/electrical release remains HOLD until closure.

## Questions / approval boundary

Which reset/BRAM isolation architecture is accepted, what safe capture-abort semantics are required, and what independent proof is sufficient? External ChatGPT reader is BLOCKED; user/independent reviewer must provide a real decision. Important reset/interface architecture change and real board writes require their actual approval. No fabricated Decision is created.
