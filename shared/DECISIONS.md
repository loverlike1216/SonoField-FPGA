# Current adopted decisions

Earlier core decisions remain valid in their original interface scope; historical board choices do not transfer to AX7020. Original decision bytes are preserved in the fixed BASE archive.

## ADR-035 — VERSION_UPGRADE_APPROVED: AX7020 v5

Decision Type: VERSION_UPGRADE_APPROVED. From:v2 active /v3 paused local history; To:v5. Approved By:User. Source:actual attachment e8213cac-ae60-4eee-bb3e-6461d16eaf66, archived in AI-interaction-memory/codex/instructions/ax7020_v5_safe_organization.md. Explicit user authority supersedes previous no-upgrade/default-v2 execution restrictions. No v4 fabricated. Selective copy, no source redesign; v1/v2 preserved frozen, v3 stays paused. Official documented AX7020 part/clock/DDR are candidate physical-board facts, not old Robei inheritance. Keep referenced history in place; archive indexes/snapshots only. Real evidence: v5/evidence/BASELINE_VALIDATION.md. External ChatGPT decision/review not claimed. Current recording model GPT-6.1 Sol High.


## ADR-036 — AX7020 read-only qualification and original-preserving candidates (2026-10-09)

Version:v5. Stage:AX7020_BOARD_DETECTION_BOM_REVISION_AND_INTEGRATION_PREFLIGHT. Model:GPT-6.1 Sol High (user-declared). Source:actual user attachment4b78522d-e640-448c-8788-c916d293b560, PCBRevision3.0 response and two uploaded photos. Type:USER_AUTHORIZED_EXECUTION_AND_EVIDENCE_CLASSIFICATION; not a ChatGPT decision.

Continue existing architecture and digital gates, permit bounded read-only detection/candidateBOM/schematic preparation, preserve currently running PL/PS/SDimage until physical/configuration/ownership gates are satisfied. ActualJTAG/CLG400/revision confirmed; DDRCwidth only controller configuration,physicalcapacity/grade unknown. Manufacturerreference is not automaticallyRev3matched. No program/init/reset/DDR RAMaccess this iteration.

ADC C-16 is an isolated recommendation only; no approved formal replacement or productionRTLchange. Independent localTXcut/rearm/I²C/AXC count are electrical candidates; manufacturingHOLD. Full digital115test/four-run baselinePASS is simulation,notboardacceptance. Evidence:v5/evidence/board_bringup/20261009/RESULT.md. Open Problems:P-20261008-001,P-20261009-001. Commit:see post-push receipt for this checkpoint; no self-referential hash fabricated.


## ADR-037 — User-authorized v5 workspace migration (2026-10-09)

Type: WORKSPACE_MIGRATION_AUTHORIZED; version v5 unchanged. Source: actual current user instruction plus Phase0–7 document in AI-interaction-memory/codex/instructions/v5_workspace_migration_20261009.md. Preserve original physical sandbox, clone independently, archive fixed Git tracked tree, maintain AX7020-only current implementation and all inherited acceptance. Candidate commits/push/Draft PR authorized. USER_APPROVAL_REQUIRED_FOR_MAIN_MERGE. This is not a ChatGPT Decision or version approval. Candidate workspace `E:\Codex_project\AMD_Sonofield`; permanent path promotion pending user confirmation and successful reviewed merge. BASE `ecd32e76e9b6c08806eae30a3c75a9c3be5e7570`.
