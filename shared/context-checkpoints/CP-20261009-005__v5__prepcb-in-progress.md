---
checkpoint_id: CP-20261009-005
project_id: SONOFIELD_FPGA
repository: https://github.com/loverlike1216/SonoField-FPGA.git
branch: feat/v5-prepcb-full-system
base_commit: d7f7b60ae8ed9ed8bdee34c8738ce68aacd81743
head_commit: RESOLVE_CONTAINING_COMMIT_WITH_GIT_LOG
active_version: v5
version_status: ACTIVE
current_stage: V5_PREPCB_S0_S1_CONTRACTS_S2_S6_VALIDATION_RUNNING
created_at: 2026-10-09T07:09:42.963343+00:00
checkpoint_reason: actual pre-PCB user authorization and executable milestones
source_of_truth: repository
status: VALID_IN_PROGRESS
---

# Context checkpoint

Identity and goal: same project/repository/new independent clone; continue v5
pre-PCB S0–S7, no version upgrade. Migration candidate unmerged; current user
supersedes earlier migration-only scope for additive v5 work.

Architecture/invariants:128TX/8RX, commonclock,32×4serializer, separate8bit
phase fields, atomiccomplete128map/50Hz, threeTMP117, two independent arrays,
central power only protectedAX7020headers. Actual contract is
v5/docs/pre_pcb/CENTRAL_ARRAY_HARDWARE_CONTRACT.md.

Completed: S0 reconciliation/attachments/hashlock; S1 candidatepin/BOM/contract;
new51 C/Python tests; two-simulator supervisor/mailbox tests; actual2025.2
PS7/AXI/BRAM/IIC/IRQ connectedBD and logicalXSA; PL OOC routed internal
WNS+.068/WHS+.070. No hardware acceptance. Original full regression is running.

Plan/next: finish full original and new integrated gates, commit stable source,
independent new clone/lockedvenv, then source/evidence/hash/repro review and
normal development push. S7 requires exact remote receipts, no main merge.

Decisions: current actual user authorizes additiveS0–S7; no ADC/platform/version
upgrade. Ordinary DLL/frequency binding errors corrected with failed logs
retained. No ChatGPT decision invented; external reader BLOCKED.

Blockers/limits: PC-B01..13 in PRE_PCB_OPEN_BLOCKERS.md; target ARM/BSP,
real UART/sensors/ADC, complete board timing/DRC/CDC, power/safety/thermal/AFE,
fullTXcalibration, particles and nativeCAD/ERC remain unverified. Whole
platform REVISE; electrical/manufacturing NOT_RELEASED.

Do not change: frozen archive/oldphysicalworkspace, originaltests/goldens/RTL,
thresholds, formalADC. Two optionalCservice adapters are documented and hash
tracked independently. No board programming/init, forcepush or mainmerge.

OpenAIproblems: P-20261008-001 andP-20261009-001 unchanged, actual hashes
verified by routine workspacechecker. Current candidateboard facts remain
unqualified. PreviousCP004 migration facts remain history, not current stage.

Resume: rootREADME/AGENTS/state/CP/plan/decisions/blockers/acceptance, inspect
actual evidence/pre_pcb_20261009 status and Git. Do not re-read old sandbox.
Provenance: actualuserinstruction+twoPNGs, S0protectioninventory, current
source/config, new51testlog, rtl_supervisor1, platform_connected4 rawreports,
liveGitstatus/head/remote. Head is resolved by commit containing this snapshot.
