---
checkpoint_id: "CP-20261010-002"
project_id: "SONOFIELD_FPGA"
project_name: "SonoField-FPGA"
repository: "https://github.com/loverlike1216/SonoField-FPGA.git"
branch: "codex/v5-ad7606c16-nextstage-20261010"
base_commit: "7d4dd090aac29331166d72aa50d2a0c5a6068101"
head_commit: null
active_version: "v5"
version_status: "ACTIVE"
current_stage: "V5_UART_RESUME_OFFLINE_BSP_BUILT_A0_A2_STOP_DRAFT_REVIEW"
created_at: "2026-10-10T05:36:22.595758+00:00"
created_by: "Codex"
checkpoint_reason: "Actual user UART-driver continuation, corrected recovery fact, new read-only SLCR evidence, native BSP-linked ARM service and independent clean reproduction"
source_of_truth: "repository"
status: "VALID_CANDIDATE_WITH_LIMITATIONS"
---

# Context Checkpoint CP-20261010-002

PROJECT_ID SONOFIELD_FPGA; SonoField-FPGA; same official repository;
workspace E:\Codex_project\AMD_Sonofield; branch codex/v5-ad7606c16-nextstage-20261010; v5 ACTIVE.
Base/tool source 7d4dd090aac29331166d72aa50d2a0c5a6068101; containing HEAD resolves with
`git log -1 --format=%H -- shared/CONTEXT_CHECKPOINT.json`.
Created 2026-10-10T05:36:22.595758+00:00; source_of_truth repository; status VALID_CANDIDATE_WITH_LIMITATIONS.

## Current goal and architecture
Continue v5 UART recovery and safe offline native build, synchronize Draft4.
Existing128TX/8RX/commonclock/atomicmaps/50Hz/geometry/user-approvedC16 architecture
is unchanged. New2025.2SDT time compatibility include forwards to xiltimer.
Only the existing safe/status service was linked; no full deployed motion/sensor
runtime, matched physical platform or board permission is inferred.

## Completed and latest validation
203current +203independent freshclone tests PASS; actual2025.2SDT/BSP/linkedARM
ELF PASS both; OCMaudit/3negativecases PASS; application .text hashes match.
FullELF/BSP are path-dependent, not declared bit-exact. COM3Code0/driver11.6.0.420
and pyserial3.5 confirmed. New XSDB SLCR read-only snapshot has both CPUs Running
before/after; no UARTopen/TX/FIFO/RAM/write/halt/reset/init/download. Original
Vivado retained, ownedserver stopped. Prior1160sealed evidence and S0/frozen
metadata retain hashes; prior3696x4 simulations were not rerun this round.
Evidence: v5/evidence/uart_resume/20261010_01; result and reproduction: v5/docs/uart_resume.

## Plan position and next actions
S1 UARTdriver subgate closed; A0 line-control fact gate remains open. S4 logical
BSP/ELF subgate closed through installed2025.2nativeCLI; Vitis platformAPI still
fails missingZynqQEMU. S5 realcontrol remains NOT_RUN. S7 new evidence prepared
for existingDraftPR4. Next: actual remote receipt, user/independent review,
Rev3 documents/recovery/image ownership; no main or board write without approval.

## Decisions and open problems
ADR040 user-approvedC16 unchanged; ADR041 records actual driver/site/recovery
facts and safe offline continuation. P-20261008-001/P-20261009-001/P-20261010-001
remain indexed; BRAMreset architecture has no new independent approved decision.
ExternalChatGPT reader BLOCKED; no invented decision or transcript.

## Blockers, limitations and quality
All13physical/electricalPC-B scopes remain OPEN. PC-B08 linked-candidate subgate
closed only. Rev3 DTR/RTS/PS/pins/VCCO/clock/currentimage/RAMowner/recovery unknown;
remote hardware share lists V2.0 schematic, not matchedRev3 proof. NativeERC and
manufacturing HOLD. BRAM346warnings/externalIOtiming unchanged. ELF RWX warning
retained. Offline ACCEPT WITH LIMITATIONS; realboard/wholeplatform REVISE;
independent/user final review PENDING.

## Do Not Change and invariants
Original sandbox and frozen archives; original tests/goldens/BOM/evidence/35dB
criteria, protocol/capture/ACK/atomicmaps/separate8bitphases/commonclock,
128TX8RX/32x4/50Hz/12mmpitch/100mmnominal90-115mmfacegap/centerorigin.
No version upgrade, historybodyread, forcepush, mainmerge, boardwrite, unknownIO
or manufacturing. Default-off output safety remains mandatory.

## State conflicts and delta
Earlier Code28/0COM and noBSPapplication snapshots remain immutable historical
evidence; current observations supersede their current-state wording. Earlier
user 'original files available' is corrected by later 'no local files': remote
references exist, usable recovery backup NOT_VERIFIED. No scope expansion.

## Resume instruction, evidence and provenance
Read README/AGENTS, PROJECT_STATE, VERSION_STATE, this checkpoint, CURRENT_PLAN,
DECISIONS/BLOCKERS/ACCEPTANCE, uart_resume RESULT/FINAL_VERIFICATION and actual
publication receipt, then Git/PR latest state. JSON companion holds machine refs.
Observable user/tool records are PARTIAL with cutoff and hashes. Base facts come
from actual source/build/OS/XSDB/clone checks, not inferred ChatGPT history.
