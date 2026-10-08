# AX7020 v5 safe organization result — 2026-10-08

PROJECT_ID: SONOFIELD_FPGA
project_name: SonoField-FPGA
repository: https://github.com/loverlike1216/SonoField-FPGA.git
workspace_path: E:\Codex_project\AMD-SonoField-FPGA
branch: main
active_version: v5
stage: AX7020_V5_SAFE_ORGANIZATION_AND_STANDALONE_BASELINE
current_model: GPT-6.1 Sol High (user-declared)

## 1. Before / after structure

Before: same Git root; shared activev2/highestv3; v1 frozen,v2 active,v3 paused local untracked,v5 empty; PCB/BOM/Zynq7020/parameter_detection/evidence at original paths; caches/runtime/dependencies local.

After:

```text
AMD-SonoField-FPGA/
  README.md / AGENTS.md / 指南.md / CHANGELOG.md / Git attributes and ignore rules
  shared/                    current v5 state, formal decisions, checkpoints, audit
  AI-chat-memory/            external source BLOCKED
  AI-interaction-memory/     actual observable instructions/messages/tool flow PARTIAL
  AI-problem/                historical provenance, no automatic AX7020 decision
  v5/                        sole active AX7020 implementation
    rtl/ software/ firmware/ tb/ tests/
    config/ simulation/ scripts/ docs/
    hardware/ax7020 constraints pcb bom characterization mechanical transducers
    vivado/ evidence/ build(local-only)
  archive/                   frozen indexes and original governance snapshots
    legacy_versions/ legacy_board/ legacy_pcb/
    historical_evidence/ deprecated_designs/ manifests/
  v1/ v2/ v3/                kept at original paths, historical/frozen/paused
  PCB/ BOM/ Zynq7020/ parameter_detection/ evidence/  referenced history kept
  .git/ .venv/ .Xil/ build/   retained; caches/generated outputs ignored
```

No fabricatedv4; no source/history moves or deletions. Referenced old directories remain in root by the user's permitted safety exception, excluded from normal v5 search/build. Detailed25-entry audit: DIRECTORY_AUDIT.md/.json.

## 2. Copied source count and modules

186 inherited assets:154 COPY_AS_IS,32 COPY_AND_UPDATE. Groups:{"config": 8, "docs": 19, "simulation": 4, "firmware": 4, "hardware": 43, "requirements-board.txt": 1, "requirements-lock.txt": 1, "requirements.txt": 1, "rtl": 21, "scripts": 15, "software": 40, "tb": 18, "tests": 11}. Stable phase/timebase/atomic/safety/serializer, acquisition/calibration/motion/AXI logic, Python solver/controller/UI, C protocol service, all tests/TBs and design reference preserved. RTL count21 includes19SV modules and2generated headers. Three goldenRTL and one unchanged SYNTHETIC calibration record are explicit local inputs. Full per-file source/target/hash: v5/config/inheritance_manifest.json; source plan VERSION_MIGRATION_PLAN.json. New v5 configuration/docs/tools are additional and not included in the186copy count.

## 3. Script/config/path changes

Only v5 functional copies adapted: UI/version metadata,new calibration project_version,local synthetic fixture/default path, golden fixture paths,migration/repository checks,document references,AX7020 fail-closed board profiles and OOC project config. Current COM/physicalPart/PS preset/XSA/BSP/productionXDC are unset; old board clock/pins/DDR/FTDI evidence not promoted. Native top sono_axi_system, documented partxc7z020clg400-2, internal132MHz target; current18synthesisfiles and all19simulationmodules are own v5 paths. Legacy clock candidate is an explicitly unused reference; native check proves zeroMMCMinstances. No production pin constraints or bitstream.

Adapted copied files:

- v5/config/board_smoke_profile.json
- v5/config/board_transport_profile.json
- v5/config/system_baseline.json
- v5/docs/RESEARCH_BASELINE.md
- v5/docs/architecture/SELF_CALIBRATION.md
- v5/docs/architecture/V5_REQUIREMENTS.md
- v5/docs/architecture/digital_interface.md
- v5/docs/dependencies.md
- v5/docs/experiments/bringup.md
- v5/docs/hardware/PCB_SOFTWARE_INTERFACE.md
- v5/docs/hardware/PCB_SOFTWARE_INTERFACE_REQUIREMENTS.md
- v5/docs/hardware/SCHEMATIC_DESIGN_RULES.md
- v5/docs/hardware/SERIALIZER_THROUGHPUT_PROOF.md
- v5/docs/hardware/tct40_baseline.md
- v5/docs/motion/COORDINATE_AND_WORKSPACE.md
- v5/docs/motion/FPGA_MOTION_INTERFACE.md
- v5/docs/motion/INTERACTIVE_CONTROL_ARCHITECTURE.md
- v5/docs/motion/PC_CONTROL_APP.md
- v5/docs/motion/SAFETY_LIMITS.md
- v5/docs/motion/TRAJECTORY_PLANNER.md
- v5/docs/theory/model_and_results.md
- v5/scripts/check_migration.py
- v5/scripts/check_repository.py
- v5/scripts/create_project.tcl
- v5/scripts/pre_pcb_checks.py
- v5/scripts/run_motion_app.ps1
- v5/scripts/timing_equivalence.py
- v5/software/acoustic_model/phase_lut_generator.py
- v5/software/calibration/database.py
- v5/software/calibration/pipeline.py
- v5/software/ui/app.py
- v5/tests/test_motion.py

Additional current tools: scripts/run_baseline.py/.ps1,check_structure.py,config/board_facts.json,ax7020_ooc.tcl,inheritance_manifest.json,hardware/constraints/core_ooc.xdc. Reuse completeness checks never open old worktrees. Shared organization scripts are archival/validation audit tools, not runtime dependencies.

## 4. Archive and retained files

Archive:15 exact original governance snapshots plus categorized frozen indexes/manifests. No old-version/PCB/raw board tree moved. All3343inventoried historical non-cache files preserve byte hashes.605untracked originals have a verified private ZIP under shared/organization/local_raw; backup receipt includes SHA256 and restore instructions. No blanket staging/private raw document publication. Caches/.venv remain, not falsely claimed fully inspected. Recovery commit:4cd42172dbbb1b4a2fc45d8f0d33d28f2efcc0fe.

Kept in place:v1/v2/v3,PCB(includinguntrackedbackup),BOM,Zynq7020,parameter_detection,root evidence,.venv/.Xil/build/runtime files. Reason: existing historical imports/scripts/reports/source references and untracked user assets. Further high-risk relocation would require a separate explicit plan/approval; none is necessary for this usable v5 result.

## 5. Real before/after/standalone comparison

Three complete orchestrators PASS. Each:115Python tests,3696motionframes×4(3Icarus+1XSim),waveform/model oracle/calibration/ADC/Cprotocol/AXI/safety/golden cycle-equivalence. Source hashes, motion hashes, waveformTB15, ADC roundtrip and repeated calibration numerical artifact hashes match across allthree. Rawcalibration.json changes onlygit_commit(base vs recovery); every other field is exactly equal, original rawhashes/expectedcommits retained in baseline/CALIBRATION_PROVENANCE_DIFF.json. No rawJSON byteidentity acrossdifferentprovenance claimed. Standalone parent has no oldversions/shared/archive; same external interpreter/dependencies/tools reused, not a second computer or fresh dependency install. Evidence:v5/evidence/BASELINE_VALIDATION.md and baseline/COMPARISON.json.

Vivado2025.2 OOC synthesis executed:7219LUT,17918FF,4RAMB36; pre-route WNS+0.994ns/WHS+0.157ns. Native project/checkpoint reopen PASS,18own sources,7.576ns restoredclock,unusedlegacyMMCMcheckPASS. Boundary2324no-input-delay/256no-output-delay warnings retained; full-board route/IO/PS/bitstream/hardware NOT_RUN. No clock/pin/falsepath invented.

Failures retained: first baseline omittedmotion_gate.py; second missingexplicitfixture(72tests,FAIL); first native audit had an erroneousminimum20module assertion. Ordinary dependency and audit-rule corrections recorded in DEPENDENCY_RCA.md, no assertions/functional threshold weakened. User-home prefixes in3failure logs sanitized for current public files; exact raw copies retained privately. No failure deleted.

## 6. Git and synchronization

Same main branch and requested remote, no new repository/tag/release/forcepush/history rewrite. Pre-archive recovery commit above is real. Final current state/evidence/checkpoint use subsequent normal commits; exact pushed delivery HEAD and remote equality are in GIT_SYNC.json and the final user response. Historical trees unchanged. Existing untrackedv3 andPCBbackup intentionally remain local; ignored/private/generated data is not claimed mirrored to publicGitHub.

## 7. Remaining risks

AX7020 actual board/revision/VCCO/full ordering-code match,matchingPS DDR/clock/preset/XSA/BSP,productionIO/externaltiming,realhost-boardtransport,safety/driver/ADC/transducer characterization and staged measured levitation remain unverified. Manufacturer reference is not physical measurement. ExistingBOM/circuit design inputs are not AX7020 electrical release. Inherited design docs retain older stage narratives; current implementation status comes from current source/state/evidence and docs/README.md. ExternalChatGPT history/review BLOCKED; Codex transcriptPARTIAL, no inventedreview/history.

## 8. Continuation readiness

YES for v5 digital/software work and board-integration planning, with v5/README.md and root指南.md providing portable commands/tools/output/pass criteria/troubleshooting. NO physical deployment until qualified platform/IO/PS inputs and a reviewed integration contract. Current shared state/plan/decisions/blockers/acceptance and reconciledContextCheckpoint identify the next step; do not restart old versions or createanother version oncontinue.

## 9. Scoped Quality Gate

ACCEPT WITH LIMITATIONS for directory organization and available digital/tool baseline, contingent on final normal remote verification. Whole physical platform is not accepted. The user's core target/interfaces/algorithms/acceptance remain continuous, all history preserved.
