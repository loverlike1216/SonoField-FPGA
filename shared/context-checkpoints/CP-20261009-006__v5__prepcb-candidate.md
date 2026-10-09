---
checkpoint_id: CP-20261009-006
project_id: SONOFIELD_FPGA
repository: https://github.com/loverlike1216/SonoField-FPGA.git
branch: feat/v5-prepcb-full-system
base_commit: d7f7b60ae8ed9ed8bdee34c8738ce68aacd81743
head_commit: None
source_commit: a43728870a06949e67b0604f4716f07419b3306c
active_version: v5
version_status: ACTIVE
current_stage: V5_PREPCB_S7_CANDIDATE_USER_REVIEW_PENDING
created_at: 2026-10-09T10:38:08.858692+00:00
created_by: Codex
checkpoint_reason: S0-S7 offline candidate gates complete; independent clone and corrected PS address mapping; final review handoff
source_of_truth: repository
status: VALID_CANDIDATE_WITH_LIMITATIONS
---

# Context Checkpoint

## Current identity and goal
Same SonoField-FPGA repository, v5 ACTIVE; current sandbox AMD_Sonofield.
S7 candidate delivery; review before any formal main promotion/hardware work.
Executable source and containing-checkpoint commit are separate fields above.

## Architecture and evidence
ThreePCB128TX/8RX, centralPS7/AXI/BRAM/IRQ/threeIIC, inheriteddigitalcore,
new failclosed supervisor/mailbox, optionalCcommands, three-temperaturephase
integral, bounded6DoF sparsefit, runtimeuserpathGUI. See hardwarecontract.
Completed/validation fields in JSON and FINAL_VERIFICATION identify actual
171tests, two-clone fullbaseline, two-simulator newtop,375GUIframes,
20480word comparisons and10numericalfits. Hardware Verified: NONE this task.

## Current plan and next action
OfflineBlocking0/knownCritical0; candidate ACCEPT WITH LIMITATIONS only.
PC-B01..13 remain. Wholeplatform REVISE; PCB/manufacturing NOT_RELEASED.
Finish normalbranch publication/CI receipt, then STOP_OPTIMIZATION_AND_DELIVER.
Independent/user review, physicalqualification and approved dependency-ordered
merges remain future work; no automaticmain merge.

## Active decisions / Do Not Change / Invariants
ADR038 is the actualuser existingv5 authorization, not ChatGPT output.
Preserve originalcore/tests/goldens/thresholds, ADCB and NU40C10T, v5 only,
128TX/8RX/32×4/commonclock/atomicmaps/50Hz/3TMP117 and protectedpowerdomains.
Frozenarchive/oldphysicalcopy excluded; no forcepush/deviceoperation/CADrelease.

## Blockers and known limitations
See PRE_PCB_OPEN_BLOCKERS.md: Rev3, pin/power/partqualification, ADC/AFE,
physicalcoarseTOF and channelresponses, hardwarecutoff, ARM/BSP, fullboard
STA/CDC/BRAMasync, acoustics, CAD/ERC and independentreview. ChatGPT BLOCKED.
Open Problems P-20261008-001 and P-20261009-001 unchanged; no fabricated Decision.

## State conflicts / delta from CP005
CP005 and earlier tool exit0 described a validPSBD. Subsequent explicit
addressreview found five unmappedperipherals. Those addressspaces are invalid;
final source assigns/asserts all six windows and fiveIRQs. EarlierPL OOC-only
reports retain that limited scope. Immutable CP005 snapshot is not rewritten.
Final GUI selection/3Ddrag and supervisor/core fault integration are corrected.
Failed logs retained; FINAL_VERIFICATION selects current accepted evidence.

## Resume instruction and provenance
Read root states/version/checkpoint, PRE_PCB_COMPLETE_REPORT, FINAL_VERIFICATION,
currentplan/decisions/blockers/acceptance, currentGit/remote receipt and open
problems. Real source/config, logs, reports and hashes take priority. The
cleanclone uses a separatevenv and nohardlinks but shares localOS/EDA.
Resolve containingcommit with git log -1 --format=%H -- shared/CONTEXT_CHECKPOINT.json.
Never restart from oldchat or read archive by default. User controls finalmerge.
