---
problem_id: P-20261008-001
project_id: SONOFIELD_FPGA
active_version: v5
current_stage: NEXTSTAGE_S0_S7_ADC_C16
status: APPROVED_BY_USER
decision_source: User
chat_source_name: SonoField-FPGA
chat_message_id: UNKNOWN
chat_message_time: 2026-10-10 Asia/Shanghai
problem_hash: 231aa1770662448c8e9f9cd83aa1b309abcbc21790ffd26eb58821ffe33843ab
hash_scope: Original problem body after closing frontmatter plus blank line, UTF8 LF
decision_sync_time: 2026-10-10
---

# ADC direction decision

Actual user message: “我已明确批准 AD7606C-16 作为 v5 正式 ADC，请完成相应的技术决策持久化和工程适配。”
Canonical instruction: ../../AI-interaction-memory/codex/instructions/v5_nextstage_20261010.md, D-NEW-01; raw SHA256 2f4390c8e15d1425297c689781956ef3a4056e757bd353c5fa132d8d7683db68.
External ChatGPT access remains BLOCKED. This is a real USER decision, not a fabricated ChatGPT output or independent electrical review.

## Chosen direction

One AD7606C-16BSTZ-RL candidate orderable part, 8 simultaneous channels, 4DOUT, 16bit signed capture, initially800kSPS. Software straps OS111/PAR-SER1, CONFIG0x02=0x10, BANDWIDTH0x07=0xff, +/-5V single-ended0x11 per channel pair, OS0, interfaceCRCoff; all settings read back before ready. Exact order suffix/package and board electrical qualification remain HOLD.

## Rationale / rejected options

Do not continue the B low-bandwidth path as the production selection; preserve it solely as an executable regression reference and provenance. Do not rename its behavioral model or overwrite old test/golden/evidence. Do not infer analog40kHz SNR or phase from sample rate or highBW alone. Reject automatic1MSPS and raw continuous115200 transfer.

## Validation and remaining gates

Verify original problem ID/body hash/version against unchanged problem; separate adapter and independent model with two simulators, target/host C distinction, preservation hashes, full baseline, current production parameter integration, native Vivado, fresh clone. User authorization closes CHIP_DIRECTION_APPROVAL only. ADC/AFE/reference/filter, 40kHz complete-chain measurements, timing/PCB/ERC and independent review remain REVALIDATE_DECISION / OPEN_ELECTRICAL_QUALIFICATION.

## User approval boundary

Reversible v5 software/RTL/BOM/candidate circuit changes are approved. Board reset/halt/init/download/RAM writes require a separate concrete approval after A2 facts; manufacturing, power output and main merge are not approved. No user approval is inferred for those operations.
