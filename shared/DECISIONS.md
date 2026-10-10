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

## ADR-038 — User-authorized additive v5 pre-PCB full-system stages (2026-10-09)

Type: USER_AUTHORIZED_EXECUTION; source actual new user request and exact document
AI-interaction-memory/codex/instructions/v5_prepcb_full_system_20261009.md.
Continue samev5/repository/independent clone, branchfeat/v5-prepcb-full-system
stacked on migration candidate d7f7b60; no new version, no main merge.
Existing validated digital RTL/tests/goldens/thresholds remain protected.
Two Cservice adapter files change only behind explicit SF_PREPCB_EXTENSION;
original expected hashes are retained as source/initialcopy provenance and new
hashes require the independent112-file S0 preservation audit.

Adopt user-defined centralAX7020header-only protectedsingle-source rails,
two independent12V5A candidate arrays, threeTMP117 and optionalSHT45,
bounded phase-aware50Hz runtime paths and sparse geometry calibration with
explicit RX0/RX4 gauges. FormalAD7606BBSTZ-RL and NU40C10T unchanged; RXunknown,
Rev3/power/BSP/electrical/physical gates remain open. Synthetic data cannot
close hardware or fullTXcalibration gates. PCB/manufacturingNOT_RELEASED.

Offline implementations, normaldevelopmentbranch commits/push and review
package are authorized by this actual user instruction. No programming/init/
halt/reset/DDR/boot/CADmanufacturing operation. ExternalChatGPT reading remains
BLOCKED. This record is a user decision, not a fabricated ChatGPT Decision.
Evidence: v5/evidence/pre_pcb_20261009 and docs/pre_pcb contracts. CP005 records
in-progress validation; final acceptance follows actual successful gates.


### ADR-038 execution closure — 2026-10-09

User-authorized existingv5 offlineprePCB stage executed and cross-checked.
No new architectural/version/ADC substitution decision. Final evidence selects
corrected PS6window/5IRQ and actualnewtopchain; CP005 addressclaim superseded
by CP006, immutablehistoricalsnapshot preserved. Deliver candidate with limits,
retain physical/ARM/independentreview/main gates; stop further optimization.
Source: actual instruction + FINAL_VERIFICATION; not a ChatGPT Decision.

## ADR-039 — User-authorized historical path isolation (2026-10-09)

Source: actual current user request and exact Gate0–7 document in AI-interaction-memory/codex/instructions/v5_historical_project_20261009.md. Same repository/version. Authorize one-time bijective path relocation of frozen snapshots and old v2 instruction copies into exact Historical project root, preserving bytes/blob/mode; current v5 and root shared/open Problems/approval provenance remain. Current older BLOCKERS/ACCEPTANCE conflict had already been resolved by PR1/PR2; original stale bodies remain frozen. Branch is created from main then normally fast-forwarded to complete unmerged v5 candidate, with dependencies explicit. Main merge and Gate7 require concrete user approval. No external ChatGPT Decision is claimed. No old board pin/clock/DDR choice transfers. No hardware or ADC change.


## ADR-040 — Actual user-approved v5 ADC direction and next-stage scope (2026-10-10)

Decision Source: User, actual next-stage request plus exact instruction AI-interaction-memory/codex/instructions/v5_nextstage_20261010.md SHA2562f4390c8e15d1425297c689781956ef3a4056e757bd353c5fa132d8d7683db68. Continue v5, same repository/workspace. Formal AD7606C-16 direction APPROVED; order suffix/nativefootprint and electrical/analog qualification HOLD. Corresponding P-20261008-001 decision verifies original v5bodySHA231aa1770662448c8e9f9cd83aa1b309abcbc21790ffd26eb58821ffe33843ab. No ChatGPT decision/review invented.

User authorizes reversible adapters/models/config/C/Python/GUI/BOM/netcontract/offline native builds, read-only OS/board qualification, reviewed normalcommits/push/stackedDraftPR onPR3. Preserve originalBtests/goldens/35dB/core/default behavior and historicalBOM/evidence; active newtopC16. Twoindependentexternal12Varrays, centralAX7020-only protectedsingle-source rails,3TMP117,128TX/8RX,12mmpitch/100mm90–115mmgap,50Hz/commonclock/atomicmaps unchanged. A2 affected boardwrites, importantarchitecture, manufacturing/purchase and mainmerge require their actual approval. Supersedes older pendingC16 direction only, not analog/electrical gates. No new version.

## Engineering finding — P-20261010-001 (2026-10-10)

Full nativeDRC enumerates346REQP-1839BRAM asynchronous control warnings plus1OOCZPS7-1. Exact current/clean routedreport bodies agree. Positive OOCslack and emptyCDC do not close reset or unqualifiedIO risk. ProblembodySHA9cc8f62962b6ed42c4f282cd239303fe01faefb1fd670d9a0fbaef61e7171d3d; OPEN for real independent/user architectural decision. No reset architecture change, waiver or severity reduction. This is a Codex evidence finding, not an approved architectural Decision. Evidence expanded_current2 and clean expanded reports in next_stage/20261010. Preserve async emergencykill and signedcapture/ownership constraints while reviewer selects a validated RAM-facing reset strategy.

2026-10-10 subsequent actual user instruction "我已将jtag插稳" triggered fresh read-only detection: After the actual user reseated JTAG, dedicated localhost3122 XSDB/Vivado2025.2 read-only identification PASS: xc7z020 ID0x23727093; both Cortex-A9 Running before/after; BOOT_MODE0x05, DDRC0x81/0x3e; PL DONE/EOS1, existing image identity UNKNOWN. Sysmon zero/-273.1 values INVALID, no voltage/temperature claim. Original Vivado GUI retained; owned server disconnected/stopped. CP2102N remains Code28/0COM. No halt/reset/init/download/memory/DDR-RAM/GPIO/driver/serial write. Real UART->PS->AXI->PL and A2 write gate remain STOP. This is an observed fact update, not authorization to overwrite the running image.


## ADR-041 — Actual UART continuation facts and offline BSP build (2026-10-10)

Source: actual user reports UART driver installed, board USB-UART COM3, empty
J10/J11, GitHub synchronization requested; later correction says no local
factory/SD recovery files, remote links only. Current OS confirms COM3Code0.
These facts authorize safe continuation and ordinary Draft publication, not
CPU halt/reset/init/programming/RAM/boot writes. Exact Rev3 line control,
platform/image/ownership/recovery/output and operation approval gates remain.

Native installed2025.2SDT/empyro/EmbeddedSW + official hash-pinned ArmGNU13.2
compile the unchanged safe/status service via an additive xiltimer compatibility
include. Independent freshclone203tests+BSP/ELF/OCMaudit PASS. No core interface,
algorithm/ADC/version/platform choice changed; physical matching still HOLD.
Vitis platformAPI missingQEMU and RWX ELF warning preserved. This is a user-fact
record and verified implementation finding, not an external ChatGPT Decision.
Evidence: v5/evidence/uart_resume/20261010_01; CP-20261010-002.
