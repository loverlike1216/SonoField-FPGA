---
checkpoint_id: CP-20261004-001
project_id: SONOFIELD_FPGA
project_name: SonoField-FPGA
repository: https://github.com/loverlike1216/SonoField-FPGA.git
branch: main
base_commit: 86b56b20433fb3ddc2d35d4101b1bac6ab312cd8
head_commit: 33ed95d159cf19902c8fbcc17dd89540df4fe3ea
active_version: v2
version_status: ACTIVE
current_stage: TIMING_CLOSURE_REAL_BOARD_INTEGRATION_AND_PRE_PCB_INTERFACE_FREEZE
created_at: 2026-10-03T20:45:21.338881+00:00
created_by: Codex
current_model: GPT-6.1 Sol High
checkpoint_reason: DDR read-only evidence reconciliation
source_of_truth: repository
status: VALID
---

# Context Checkpoint — 当前 v2 恢复入口

VALID 表示恢复状态可对账，不代表整个项目通过验收。完整平台 REVISE；PRE_PCB_BOARD_READY=NO。


## 1. Current Identity

Workspace `E:\Codex_project\AMD-SonoField-FPGA`；main/v2，Stage不变。检测来源commit `33ed95d159cf19902c8fbcc17dd89540df4fe3ea` 已核对远端；后续仅checkpoint/delivery metadata commit。数字核心已验证commit `9936a737c45bf61f1908863a94f6374c6b5c828c` 保留。

## 2. Current Goal

Single Robei XC7Z020 controller for coherent acoustic field; physical staged levitation with50mg final measured target

当前子任务只读检测已完成，获取本板匹配PS/DDR配置是下一步。

## 3. Architecture

Host acoustic solver/trajectory -> PS transport (not deployed) -> AXI/native control ->128common-phase channels with separate requested/calibration and atomic maps ->32lane serializer -> qualified drivers/TX. One central8RX AD7606B feedback path; current feedback validation synthetic/RTL only.

## 4. Completed

- {"item": "USB/FTDI interfaces,COM4 and native Vivado two-device JTAG identification", "status": "HARDWARE_VERIFIED", "scope": "Identity only; not PS/PL execution or UART transport"}
- {"item": "Exact part XC7Z020-1CLG400C and N18/33.333MHz fallback", "status": "EXPECTED", "scope": "Part USER_CONFIRMED_PHYSICAL_FACT, clock USER_APPROVED_DOCUMENT_FALLBACK_NOT_MEASURED"}
- {"item": "64connector signal pins legal/unique in confirmed part database and source Excel", "status": "TESTED", "scope": "Document/package only, physical routing/VCCO unknown"}
- {"item": "Queue selector/width/occupancy and scheduler CE changes", "status": "SIMULATED", "scope": "Original/new cycle behavior equivalent in Icarus/XSim; serializer unchanged"}
- {"item": "Current complete digital/motion/calibration/ADC regression", "status": "SIMULATED", "scope": "115Python tests;3Icarus+1XSim×3696frames,canonicalhashes equal"}
- {"item": "sono_axi_system132MHz internalOOC", "status": "SYNTHESIZED", "scope": "Fully placed/routed; WNS+0.082,TNS0,WHS+0.072,THS0;21,475routednets/0errors"}
- {"item": "Separate upper/lower disable adapter", "status": "SIMULATED", "scope": "Independent asynckill plus synchronized fresh-frame release; not integrated physically"}
- {"item": "Clock MMCM candidate", "status": "SYNTHESIZED", "scope": "Vendor standalone,131.998680MHz; final board clock not frozen"}
- {"item": "Offline AXI/host-C protocol", "status": "TESTED", "scope": "No ARM targetELF,real UART or MMIO"}
- {"item": "New sparse checkout at validated source", "status": "TESTED", "scope": "115tests/frozen212files; same machine and existing pinnedvenv"}
- {"item": "D9PSK exact Micron public FBGA decode and part-specification response", "status": "TESTED", "scope": "Manufacturer component mapping MT41K128M16JT-125 IT:K; not board memory configuration"}
- {"item": "Native Vivado2025.2 JTAG reconfirmation and XSDB2025.2 read-only DDRC register capture", "status": "HARDWARE_VERIFIED", "scope": "Identity and reset-state controller MMIO only; no PS/PL functional loop,DDR initialization,memory test or program"}
- {"item": "DDR candidate configuration and public evidence/transcript privacy/integrity", "status": "TESTED", "scope": "512MiB/32bit retained CANDIDATE; safe read scripts and source boundary checked"}

## 5. Current Plan Position

Internal digital/timing gates retained; read-only parameter inspection complete; board-matched PS/DDR configuration missing, physical integration blocked

## 6. Next Actions

- Obtain matching Robei PS preset/BD/XSA/HDF/ps7_init/reference project or revision-matched DDR schematic in parameter_detection/inputs; do not execute third-party initialization on import
- Crossverify chip count, density,DQ/rank/address wiring and effective PS parameters; preserve512MiB/32bit CANDIDATE until source gate passes
- Obtain bank34/35VCCO,actual connector orientation/continuity and voltage-qualified IO levels
- Obtain PSUARTinstance/MIO/FTDI-BTXRX/DTRRTS and PS referenceclock/reset/matchedpreset
- Construct reviewed XSA/BSP/Cortex-A9targetbuild and safe disabled-output PS/PL/AXI/clock-reset wrapper; reimplement timing
- After platform facts/gates pass: real100→1000PING/PONG,registerreadback,atomicMAPcompletion generation,errors/linkloss/GUI/ILA
- Qualify external min/max timing/load and independent disables; freeze PCB interface, then measured transducer bring-up

## 7. Active Decisions

- {"problem_id": "P-20260929-001", "decision": "USER_APPROVED_FINAL_PRE_PCB_CONTRACT", "source": "Direct user formal attachment6126fbc9", "scope": "Current bounded queue/control timing, exactpart and newreferences; no electrical guess/deployment", "problem_hash": "a84242c69d945dc5989c8b708623657e61fe8eeb4af0782f4474531cfff9972b", "ref": "AI-problem/decision/P-20260929-001__queue-control-timing.md"}
- {"decision": "MODEL_TRANSITION", "source": "Direct user", "scope": "Future GPT-6.1 Sol High provenance; architecture/version/history unchanged"}
- {"decision": "ACTIVE_V2_SINGLE_BOARD_ONLY", "source": "Direct user", "scope": "Current working scope"}

本次用户直接授权DDR事实核验；检测结果不构成ChatGPT Decision。见 shared/DECISIONS.md 2026-10-04记录。

## 8. Blockers / Critical Issues

- B03
- B04
- B05
- B06
- B07
- CHAT_MEMORY_ACCESS_BLOCKED
- PS_TARGET_BUILD
- UART_ROUTE
- BOARD_MATCHED_PS_DDR_CONFIGURATION_OR_MANUFACTURER_TOPOLOGY_MISSING
- DDR_CONTROLLER_OBSERVED_IN_RESET_NO_EFFECTIVE_CONFIGURATION

Critical issues: []

## 9. Latest Validation

- {"type": "Real Vivado2025.2 routed internalOOC132MHz", "result": "PASS", "evidence": "v2/evidence/pre_pcb_board_ready/timing/core_timing_pass.json", "commit": "9936a737c45bf61f1908863a94f6374c6b5c828c", "wns_ns": 0.082, "tns_ns": 0, "whs_ns": 0.072, "ths_ns": 0, "fully_routed_nets": 21475, "routing_errors": 0, "date": "2026-10-03"}
- {"type": "Full current functional/motion/calibration/ADC dual-simulator gate", "result": "PASS", "evidence": "v2/evidence/pre_pcb_board_ready/regression_release/summary.json", "commit": "9936a737c45bf61f1908863a94f6374c6b5c828c", "python_tests": 115, "frames": 3696, "runs": 4, "date": "2026-10-03"}
- {"type": "Independent golden queue/scheduler,array safety and serializer throughput", "result": "PASS", "evidence": "v2/evidence/pre_pcb_board_ready/independent_checks_complete/summary.json", "commit": "9936a737c45bf61f1908863a94f6374c6b5c828c", "date": "2026-10-03"}
- {"type": "Offline AXI/host C", "result": "PASS", "evidence": "v2/evidence/pre_pcb_board_ready/axi_offline_release/axi_bridge_tests.json", "commit": "9936a737c45bf61f1908863a94f6374c6b5c828c", "date": "2026-10-03"}
- {"type": "Source hashes144motion+11independent/timing snapshot consistency", "result": "PASS", "evidence": "v2/evidence/pre_pcb_board_ready/repository_reconciliation/final_source_audit.json", "commit": "9936a737c45bf61f1908863a94f6374c6b5c828c", "date": "2026-10-03"}
- {"type": "Fresh sparse checkout115tests/frozen212files", "result": "PASS", "evidence": "v2/evidence/pre_pcb_board_ready/repository_reconciliation/fresh_checkout.json", "commit": "9936a737c45bf61f1908863a94f6374c6b5c828c", "classification": "SAME_MACHINE_EXISTING_PINNED_VENV", "date": "2026-10-03"}
- {"type": "Real PS/PL transport / external acoustic operation", "result": "NOT_VERIFIED", "evidence": "v2/evidence/pre_pcb_board_ready/MISSING_PHYSICAL_FACTS.md", "date": "2026-10-03"}
- {"type": "Official Micron public decoder/specification", "result": "COMPONENT_MAPPING_CONFIRMED", "evidence": "parameter_detection/20261004_ddr/micron_fbga_D9PSK.json", "commit": "33ed95d159cf19902c8fbcc17dd89540df4fe3ea", "date": "2026-10-04"}
- {"type": "Real native Vivado JTAG and read-only XSDB DDRC/AP0", "result": "IDENTITY_VERIFIED_RESET_ONLY_CONFIG_NOT_CONFIRMED", "evidence": "parameter_detection/20261004_ddr/ddrc_registers.json", "commit": "33ed95d159cf19902c8fbcc17dd89540df4fe3ea", "date": "2026-10-04"}
- {"type": "Candidate gate,script safety,message integrity,protected source and public privacy audit", "result": "PASS", "evidence": "parameter_detection/20261004_ddr/audit.json", "commit": "33ed95d159cf19902c8fbcc17dd89540df4fe3ea", "date": "2026-10-04"}

## 10. Known Limitations

- OOC ideal inputclock and missing externalIOdelays/PS7; fullboardtimingNOT_VERIFIED
- WNS+0.082ns small margin; integrated clock/PS/IO must reimplement
- Retained DRC/methodology: RAMB36asynccontrol,LUTreset,suboptimalRAM,externaldelays/PS7 andreportlimit; not waived
- COM4 enumerated, PS UART/MIO route unverified; noCOMopen,targetELF,realPING/maps/GUI/ILA
- FT2232H reported USBvariant; custom cable descriptor is not boardidentity
- GPS photo and rawUSB/network identifiers local-only; publicsanitized records
- External ChatGPT history BLOCKED; actual Codex transcripts PARTIAL, independentreviewPENDING
- Fresh sourcecheckout same machine with existingvenv, not secondphysicalmachine
- Two photo-visible2Gb x16 chips imply512MiB arithmetic candidate but do not prove boardDQ/rank wiring or mappedcapacity
- DDRC_CTRL200/CTRL_REG13E are reset values; width00default is not board32bit confirmation; actualDDRclock/voltage unknown
- Scoped search found no matching PSexport/reference; GUI journal examined but no direct activeGUIproject Tcl query
- Core regression and timing were not rerun for this read-only detection; prior source/date preserved

## 11. Do Not Change

- Frozenv1,historicalevidence/checkpoints/modelprovenance
- NativePCB and unverified pins/IOstandards
- Version/repository/corearchitecture without explicitapplicable userauthorization
- Packet/register/128channel/8bit formats,requested/calibration split,atomics,channelordering/cadence/ACK
- Acceptance thresholds; no testskips/falsepath waivers to claim PASS
- No programming,COM,applicationMMIOwrites,DDR RAM testing or externalPCB operation without verified facts and applicable user authorization
- Keep512MiB/32bit CANDIDATE until boardmatched crossverification; do not turn rated800MHz/1.35V into measuredboardfacts
- Current user DDRinspection permits only documented read-only DDRC_CTRL/CTRL_REG1 viaDAP; no init/write/CPUcontrol/DDRaddress access

## 12. Invariants

- 128channels/8bit;commoncoherent PLphase
- Requested+calibration modulo256 andatomiccomplete-mapcommit
- Safe reset/globaldisable and independentarraydisable integration required
- 38.5..41.5kHz; core132MHz target/current132/66MHz design; inputfallback33.333MHz not measurement; finalboardclock notfrozen
- 10mm body/12mm radiating-center pitch/8×8upper+lower/100mm nominal facegap/90..115mm range/origin geometriccenter

## 13. Open AI Problems

- P-20260919-001
- P-20260919-002
- P-20260919-003
- P-20260925-001
- P-20260927-001

本次未生成新Problem：实际配置来源缺口已明确，普通资料核验无需伪造咨询或Decision。

## 14. Repository Delta Since Previous Checkpoint

Official public Micron lookup D9PSK→MT41K128M16JT-125 IT:K; real XSDBAP0two documented DDRC reads show reset values200/3E; native Vivado reidentifies XC7Z020. No matching boardconfig in scoped search.512MiB/32bit remain candidates. Detection reports/scripts/public logs/config/state/guide/observable records added; coreRTL/software/PCB and historical frozen/checkpoint evidence unchanged.

## 15. Resume Instruction

Read current state/version/checkpoint/plan/decision and parameter_detection/20261004_ddr/RESULT.md. Stay currentv2 singleboard. Inspection finished; acquire actual matched PS/DDR topology/configuration and remaining physicalfacts. No DDR initialization/memory test,download or externalhardware operation at this boundary.

## 16. Evidence References

- v2/evidence/pre_pcb_board_ready/RESULT.md
- v2/evidence/pre_pcb_board_ready/summary.json
- v2/evidence/pre_pcb_board_ready/MISSING_PHYSICAL_FACTS.md
- v2/evidence/pre_pcb_board_ready/board_identity/jtag_identity.json
- v2/evidence/pre_pcb_board_ready/board_identity/windows_inventory.json
- v2/evidence/pre_pcb_board_ready/connector_reference/connector_audit.json
- v2/evidence/pre_pcb_board_ready/timing/strategy3/routed/timing_summary.rpt
- v2/evidence/pre_pcb_board_ready/regression_release/summary.json
- v2/evidence/pre_pcb_board_ready/repository_reconciliation/fresh_checkout.json
- AI-interaction-memory/codex/S-20261003-codex-002.md
- AI-interaction-memory/tool-flow/T-20261003-002__pre-pcb.md
- 指南.md
- parameter_detection/20261004_ddr/RESULT.md
- parameter_detection/20261004_ddr/summary.json
- parameter_detection/20261004_ddr/audit.json
- parameter_detection/20261004_ddr/ddrc_registers.json
- parameter_detection/20261004_ddr/vivado_jtag_sanitized.log
- v2/config/ddr_candidate.json
- AI-interaction-memory/codex/S-20261004-codex-001.md
- AI-interaction-memory/tool-flow/T-20261004-001__ddr-identification.md

## 17. Provenance

- Direct user current formalcontract and personalizedrules
- Current Git source9936a73 and exacttests/timing/identity/sourceaudit above
- shared state/version/decisions/blockers/acceptance
- Direct user DDRphoto/candidate/crossverify instruction; current native Micron/Vivado/XSDB outputs at detection commit33ed95d159cf19902c8fbcc17dd89540df4fe3ea

## State Conflicts

- {"status": "RESOLVED_CURRENT_STATE", "scope": "Previous source/clock/part/timing/current-evidence summaries lag actual current work", "resolution": "Direct user complete-part/new Excel fallback contract and current strategy3/full regression PASS govern; old timing/model evidence remains historical"}

当前DDR_CANDIDATE与复位32bit字段没有冲突：字段是默认值，不能提升本板配置。新只读控制器访问是当前用户明确指令的窄范围，旧记录的应用MMIO/初始化门禁继续有效。
