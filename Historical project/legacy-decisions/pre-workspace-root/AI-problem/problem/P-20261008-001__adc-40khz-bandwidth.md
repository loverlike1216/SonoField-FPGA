---
problem_id: P-20261008-001
project_id: SONOFIELD_FPGA
active_version: v5
current_stage: AX7020_V5_SAFE_ORGANIZATION_AND_STANDALONE_BASELINE
status: OPEN
created_at: 2026-10-08T11:16:56.427509+00:00
created_by: Codex
model: GPT-6.1 Sol High
chat_source_name: SonoField-FPGA
chat_access: BLOCKED
problem_hash: 231aa1770662448c8e9f9cd83aa1b309abcbc21790ffd26eb58821ffe33843ab
hash_scope: UTF-8 markdown body after front matter, LF newlines
base_commit: 0f42f49443bf001a147b2d58e2ae939bbcac38ce
---

# Problem

## Decision Needed
Whether the retained AD7606B direct-acquisition path can meet40kHz RX amplitude/phase/SNR requirements, or a controlled input-conditioning/ADC selection change needs a later approval. No part substitution is authorized by this review.

## Goal / Current State
Review the2026-10-08 AX7020/NU40C10T BOM only. v5 and its stage stay unchanged.128TX/8RX and stable digital contracts remain intact; physical feedback not verified.

## Repository Facts
New workbook rowB-014 selectsAD7606BBSTZ-RL; interface proposes biased0..5V RX. v5/config/system_baseline.json selects800000SPS,range_v5.0. v5/rtl/acquisition/ad7606b_if.sv init commands0311/0411/0511/0611 explicitly select+/-5V. No analog transfer function exists in the behavioral ADC proof.

## Evidence
ADI AD7606B RevB Table2 page5: analog -3dB full-power bandwidth13.5kHz at+/-5V;22.5kHz at+/-10V. Figures46/47 page25 show internal filter amplitude/phase response.800kSPS is a conversion rate, not40kHz analog passband qualification. Source:https://www.analog.com/media/en/technical-documentation/data-sheets/ad7606b.pdf. Source workbook and SHA256: v5/hardware/bom/submissions/2026-10-08/submission.json. Existing digital baseline dates/results are unchanged; no new hardware result.

## What Codex Tried
Read actual72-row workbook, official data sheet and current ADC initialization. No code, firmware, board settings or PCB changed. No repeated hardware attempts.

## Root Cause Hypotheses
Selection may have conflated sample rate with analog bandwidth. Attenuated40kHz could still be measured if actual signal/noise/headroom permit; this is not evidence of total inability to acquire.

## Candidate Options
A: retain ADC and qualify end-to-end40kHz attenuation, noise floor, amplitude linearity and channel phase at38.5..41.5kHz. Pros: preserves existing interface. Cons: filter attenuation cannot be recovered without SNR/headroom cost. Risk: insufficient RX dynamic range.
B: propose a wider analog-bandwidth simultaneous ADC or coherent analog frequency conversion. Pros: possible useful40kHz passband. Cons: interface/AFE/protocol/validation impact. Risk: unreviewed scope change. No alternative MPN is approved.

## Constraints / Acceptance Impact
Preserve128 coherent8bit channels, calibration separation, atomic phase commit, default-safe outputs, geometry, existing tests and frozen history. No substitute pinout/bitstream. Existing serial behavioral tests do not validate analog bandwidth. Define actual RX amplitude/SNR/phase error requirements and instrument measurements before this path is accepted.

## Codex Preliminary Assessment
HIGH selection risk for direct40kHz acquisition; release HOLD pending qualification. Core architecture remains unchanged.

## Questions For ChatGPT / User
1. What minimum received signal amplitude, calibrated phase error and SNR are required?
2. Does measured RX transfer/noise permit retaining AD7606B?
3. If not, approve a separately scoped ADC/AFE feasibility comparison?

## User Approval Boundary
Current task authorizes review+sync only. Changing core ADC/AFE architecture requires a subsequent explicit decision/approval and regression plan. ChatGPT source SonoField-FPGA is BLOCKED; no external consultation or Decision fabricated.
