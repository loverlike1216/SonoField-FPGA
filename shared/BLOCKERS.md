# Current v5 blockers — 2026-10-09

Only this table is the current blocker authority. Earlier v2/Robei narratives are historical and do not close AX7020 gates. Last verified from repository evidence and this migration:2026-10-09.

| ID | Status / evidence | Owner / next action | Scope |
|---|---|---|---|
| V5-B01 | PARTIALLY_RESOLVED: AX701020.3.0/XC7Z020/CLG400 historical read-only evidence; full grade/VCCO/Rev3 clock/connector match unknown. v5/evidence/board_bringup/20261009/RESULT.md | User/manufacturer: revision-matched facts | Physical |
| V5-B03 | OPEN: running-image ownership, matched PS DDR/preset/XSA/BSP, UART and real PS-PL absent. P-20261009-001 | User/embedded: obtain matched platform and safe ownership; no DDR RAM or board operation during migration | Physical |
| V5-B04 | OPEN: external66MHz min/max/fanout/cable/PVT, ADC/AFE, watchdog/default-off/rearm/surge/thermal. v5/hardware/integration_candidates/20261009/SAFETY_AND_POWER.md | Hardware/reviewer: measured qualification | Electrical |
| V5-B05 | OPEN: NU40C10T batch/continuous drive/phase/amplitude, exact RX MPN, physical trap/particle milestones missing | User/experimental: datasheets/samples and staged measurements | Acoustic |
| V5-BOM_REVIEW | OPEN/HOLD: formal AD7606B bandwidth; C-16 remains unapproved, surge/MPN/native pin-level netlist unresolved. P-20261008-001; v5/hardware/bom/working/2026-10-09/ | Independent reviewer/user: decisions then verification | Electrical |
| NATIVE_SCHEMATIC_ENVIRONMENT | NOT_CREATED / ERC_NOT_RUN / MANUFACTURING_HOLD | CAD owner after board/electrical facts; old PCB/V1 is not a v5 production design | Hardware |
| CHAT_MEMORY_ACCESS_BLOCKED | BLOCKED: no exposed supported external ChatGPT history reader, ID/URL UNKNOWN | User: supported export or connector if needed | Provenance |
| INDEPENDENT_REVIEW_PENDING | OPEN: no external AI/independent human review fabricated; A+B real environments and two simulators are available evidence | User/reviewer: review concrete Draft PR and evidence | Final review |
| MIG-MAIN | PENDING: explicit user approval for main merge and then post-merge fresh remote clone | User/Codex after approval | Migration promotion |

Physical blockers do not prevent digital migration validation. Whole-platform REVISE; candidate scope evaluated separately. No second active BLOCKERS_ENGINEERING table is created.


Current pre-PCB gate detail: v5/docs/pre_pcb/PRE_PCB_OPEN_BLOCKERS.md PC-B01..13
maps the above electrical/physical/provenance/review blockers. OfflineBlocking0
and knownofflineCritical0 apply only to testedofflinecandidate, not wholeplatform.
Final PS address-map defect is resolved; fullboardtiming, ARMtargetbuild and
physicalcutoff remain OPEN. Main and migrationPR1 remain unmerged pending user.


Historical isolation candidate: Gate4 validation/publication in progress; no known fileloss/blob/mode mismatch. Gate7 blocked by pending explicit user main approval. Existing PC-B01..13 and both open v5 Problems unchanged. No new stale BLOCKERS_ENGINEERING authority is created.
