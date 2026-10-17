---
checkpoint_id: CP-20261017-GUIDEFORMAT
project_id: SONOFIELD_FPGA
repository: https://github.com/loverlike1216/SonoField-FPGA.git
branch: codex/v5-hardware-design-20261011
base_commit: 62330fb35022421c0560b3bede8803c53b30b02d
head_commit: UNKNOWN_SELF_REFERENTIAL_USE_GIT_RESOLVER
active_version: v5
current_stage: V5_THEORY_DRAW_READY_AWAIT_INDEPENDENT_REVIEW
created_at: 2026-10-17T18:00:51.519478+00:00
status: VALID_THEORY_CANDIDATE_REVIEW_PENDING
---

# Context checkpoint

## 1. Current Identity
SONOFIELD_FPGA; E:/Codex_project/AMD_Sonofield; codex/v5-hardware-design-20261011; active v5. Entry HEAD 62330fb35022421c0560b3bede8803c53b30b02d. Resolve checkpoint commit with `git log -1 --format=%H -- shared/CONTEXT_CHECKPOINT.json`.

## 2. Current Goal
User-requested re-expression of the existing connection guide is complete. Engineering remains at independent Review; no automatic CAD/PCB.

## 3. Architecture
Unchanged user-authorized final theory contract: XC7Z020-2CLG400I; 128/256MHz F-LVT; 128TX/8RX; three independent12V inputs, 10V TX; C16 eightDOUT8MHz400kSPS. Architecture reference: v5/hardware/draw_ready_20261016/00_FINAL_THEORY_DECISION.md.

## 4. Completed
Documented 982 template devices on13pages; verified expanded1611devices/5205pins/1259passives/1088nets, 80+128contacts, 13booklets. TESTED with two Python versions and8negative mutations. Earlier simulation/route evidence remains scoped as recorded in the previous checkpoint; no new physical validation.

## 5. Current Plan Position
Guide conversion complete. Same stage: V5_THEORY_DRAW_READY_AWAIT_INDEPENDENT_REVIEW.

## 6. Next Actions
Independent Review of theory/design package; guide may now be read per page. Stop before CAD/PCB unless a new user instruction authorizes that stage.

## 7. Active Decisions
["User20261016autonomousv5theory/necessaryRTL-XDC/samebranchpublication", "UserdevicecorrectionXC7Z020-2CLG400I", "F-LVT128/256MHz;ADC8MHz400kSPS;3x12V10VTX"]
No new architecture or ChatGPT decision was created by formatting documents.

## 8. Blockers / Critical Issues
No document-equivalence blocker. Original source-freeze CI FAIL remains; independent engineering Review, physical/SSO/PDN/ERC/runtime qualification remain open. No automatic main promotion.

## 9. Latest Validation
v5/hardware/draw_ready_20261016/guide_by_page_20261017/results/CONSISTENCY.json: PASS, zero connection differences, 8/8invalid documents rejected. Logs include Python3.12.14 and3.10.11 actual executions. Earlier native21/functional evidence remains referenced in JSON.

## 10. Known Limitations
["Originalfrozen_parenthashFAILretained", "FullIBIS/SSO/PDNnotqualified", "NoCAD/ERC/physical/deployment", "ChatGPTreadsendBLOCKED"]

## 11. Do Not Change
["NoV6", "NoHistoricalprojectbodyreads/changes", "NoS3/S4/nativeEDAmodifications", "NoMainmerge/hardwarewrites/fabrication/procurement"]
Original02guide, BOM and formalRTL/XDC were not modified by this task.

## 12. Invariants
["128TX8RX", "8bitrequested/calibrationseparate", "atomiccompletemapcommit", "40kHz256phases50Hzmotion", "UCC27624andSN74LVC595A", "threeindependent12V/fixed10VTX", "2x20+2x32physicalpincontracts"]

## 13. Open AI Problems
["P-20261016-001"]
No new architecture problem; external ChatGPT review not fabricated.

## 14. Repository Delta Since Previous Checkpoint
Only added detailed guide, page booklets, independent checks/logs and project/interaction recovery metadata. Historical project bodies untouched; existing BOM/PCB/untracked raw evidence retained.

## 15. Resume Instruction
Read current shared state, then v5/hardware/draw_ready_20261016/guide_by_page_20261017/README.md and original v5/hardware/draw_ready_20261016/FINAL_REVIEW.md. Preserve review/physical boundaries; do not restart optimization or drawing automatically.

## 16. Evidence References
v5/hardware/draw_ready_20261016/guide_by_page_20261017/14_GUIDE_CONSISTENCY_REPORT.md; scripts/check_guide_consistency.py; results/CONSISTENCY.json; logs/check_guide_consistency.log; logs/check_guide_consistency_python310.log; original theory evidence remains in JSON.

## 17. Provenance
Actual originalMarkdown and8hashed source files, current Git entry HEAD, original CSV and saved pin database, newlyparsed finalMarkdown, actualtwoPython executions andnegative mutation checks. Document PASS does not certify hardware.
