---
{
  "checkpoint_id": "CP-20261010-001",
  "project_id": "SONOFIELD_FPGA",
  "repository": "https://github.com/loverlike1216/SonoField-FPGA.git",
  "branch": "codex/v5-ad7606c16-nextstage-20261010",
  "base_commit": "feb97ad5c95088affaf075cb034fe29d4b5aeda0",
  "active_version": "v5",
  "version_status": "ACTIVE",
  "current_stage": "V5_NEXTSTAGE_S7_OFFLINE_COMPLETE_A2_STOP_DRAFT_REVIEW",
  "created_at": "2026-10-09T23:23:52.204934+00:00",
  "checkpoint_reason": "Complete current and independent-clone offline S0-S7 evidence, actual C16 user decision, full DRC risk and A2 STOP ready for Draft review",
  "status": "VALID_CANDIDATE_WITH_LIMITATIONS"
}
---

# Context checkpoint

## Current identity

# SonoField-FPGA v5 current engineering state — 2026-10-10

SONOFIELD_FPGA; same repository; `codex/v5-ad7606c16-nextstage-20261010`; workspace `E:\Codex_project\AMD_Sonofield`; v5ACTIVE/highestv5. Current ADC direction AD7606C-16 is explicitly user-approved, electrical/package/analog release HOLD. CP `CP-20261010-001` records the current candidate, not a main merge or version upgrade. Runtime implementation6274330f, final audit/tool sourcefeb97ad5c95088affaf075cb034fe29d4b5aeda0; PR3baseb08ccf58, main ecd32e76 unchanged.

Offline **ACCEPT WITH LIMITATIONS**, real-board **REVISE**, whole-platform **REVISE**. Full before171/after199(initialdiscovery)+final203/clean203;3696frames×4each with identicalcanonical trajectory/map/trap/ACK;160maps/20480Cwords;10sparsefits/5seeds/5starts/384holdouts;5runtimeGUIcases375frames; new C16adapter/full2048framecapture/37mapintegratedtop two-tool and clonePASS. Original tests/goldens/35dBcriteria/evidence/BOM remain protected. Freshlockedvenv/nohardlinks/history-absentclone passed, with EOL-only checkout failure and exactrawGit-derived correction recorded.

Real Vivado2025.2 C16logicalBD/XSA/OOC/reopening; WNS+.038/WHS+.068ns,7480LUT/20223FF/4BRAM; same fullreport bodies across clone. ProductionIO161in/148outdelays absent. FullDRC346REQP-1839+1ZPS7-1 remains unwaived; new P-20261010-001OPEN. Actual CortexA9portableobjectPASS; VitisBSP-linkedapplicationBLOCKED.

Current20261010HARDWARE_READONLY after actual user reseat: xc7z020ID23727093; CPU0/1Running before/after; BOOT05/DDRC81+3e; DONE/EOS1; currentimageUNKNOWN; sysmonINVALID. OriginalGUI retained, ownedserver stopped, no writes. UARTCP2102NCode28/0COM and A2STOP remain. Evidence jtag_reseated/summary.json.

Seven-sheet80typeworkingBOM and threeboardADC64/connector/net/SVG contracts are proposed; oneADC/3TMP117/upper-lowersymmetry checked. AllpricesUNKNOWN. CentralAX7020protectedsingle-sourcecapacityBLOCKED; twoindependentexternal12Varrays and safety circuits unqualified. NativeEasyEDAunavailable, schematicNOT_CREATED/ERC_NOT_RUN/MANUFACTURING_HOLD. All13PC-Bgates and threeProblems remain scoped open; device direction alone closed. ExternalChatGPTBLOCKED, actualCodexmessages/toolsPARTIAL.

See [final report](../v5/docs/next_stage/FINAL_REPORT.md), [machine verification](../v5/evidence/next_stage/20261010/FINAL_VERIFICATION.json), [open gates](../v5/docs/next_stage/OPEN_GATES.md), [reproduction](../v5/docs/next_stage/REPRODUCE.md). PR1→PR2→PR3→newcandidate; PR3 contains earlier ancestors and all remain unmerged. Publication receipt [shared/next_stage/PUBLICATION_RECEIPT.json](next_stage/PUBLICATION_RECEIPT.json) is authoritative for actual newDraftURL/remotecommit/CI after sealing. Main/user approval and postmerge regression remain deferred.


## Current goal and architecture

Preserve verified128TX/8RX v5 while implementing actualapprovedC16 and offlinepre-PCB chain; active architecture v5/docs/next_stage/ARCHITECTURE_DECISIONS.md. No version upgrade.

## Completed and evidence

[
  "IMPLEMENTED approvedC16adapter/profile/independentmodel/C-Python-TMP117/lockedGUI/BOM/netcontracts",
  "TESTED203current+203clean(original171+32new); all original thresholds preserved",
  "SIMULATED3696x4before/after/clean exactcanonicalhashes and C16full2048framecapture/two-tool37maptop",
  "SYNTHESIZED_OOC_AND_ROUTED native2025.2C16logicalcandidate; clean fullbuild/reopen reports equal; boardtimingHOLD",
  "BUILT actualCortexA9ELF32relocatableobject, not BSPapplication",
  "HARDWARE_READONLY xc7z020ID23727093/CPU0+1Running/BOOT05/DDRC81+3e/DONE+EOS1; no write; UARTCode28/0COM"
]

## Plan position and next actions

# Current plan — v5 next-stage review

S0 COMPLETE: latest PR1/2/3/main reconciled, new branch on PR3,3324S0 hashes; actual user C16 direction/ProblemHash/version persisted. No old sandbox or archive body access.
S1 COMPLETE_READONLY_OS / BOARD_BLOCKED: actual CP2102NCode28/0COM/noJTAG; originalVivadoGUI retained. No target takeover or serial open.
S2 COMPLETE_DIGITAL_CANDIDATE: separate C16 init/readback/timing/model/C/Python/fullcapture/actualtop, two tools and fresh clone. Analog/brownout/CRC-enabled profile NOT_VERIFIED.
S3 COMPLETE_OFFLINE: preserve original core/35dB/goldens/protocol; three-temperature/sparse/dynamicXYZBezierGUI/Cfixture1000PING. Synthetic/hostfixtures labeled, no particle-tracking claim.
S4 COMPLETE_LOGICAL_NATIVE / TARGET_APPLICATION_BLOCKED: native2025.2 BD6windows5IRQs3IIC/DDROFF and PL OOC route/reopen; portableARMobject realcompile. Matched Rev3/XSA/BSP/linker/OCM/UART and346BRAMwarnings/externaltiming remain STOP. P-20261010-001 requires a real independent reset/BRAM decision.
S5 NOT_RUN_A2_STOP: no physical UART/PS/AXI/PL writes without matched platform/currentimage ownership/recovery/isolatedoutputs plus explicit affected-operation approval. No broad prompt authorization substitutes for A2.
S6 COMPLETE_CANDIDATE_CONTRACTS / ELECTRICAL_HOLD: seven-sheet80typeBOM, ADC64/connector/net/SVG contracts/benchSOP/source reviews; no nativeCAD/ERC/manufacturing release.
S7 OFFLINE_COMPLETE: fullbefore/after/clean,final203,newcapture,rawS0/archivemetadata/source/report/tracehashes; preserve failures, privacy scan, currentstate/checkpoint. Next normalpush+stackedDraftPR onPR3 and actualCI/remote receipt. No merge/cancel of PR1/2/3, no forcepush.

After publication, stop optimization and deliver concrete review package. User/independent reviewer closes actual hardware/electrical/BRAM gates. Current entry v5/scripts/run_nextstage.py and docs/next_stage/REPRODUCE.md; outputs/venv inside current clone only. Continue remains v5. Main promotion and fresh remote-main full regression follow explicit candidate approval only.


## Active decisions

ADR040 actual user C16 approval; prior valid scope/invariants retained. P-20261010-001 has no Decision yet.

## Blockers / critical risks

# Current unresolved gates and minimal closure

Device-direction approval is CLOSED: user approved C-16. Its analog/electrical qualification remains OPEN. Original PC-B01..13 IDs persist for continuity; current meaning below supersedes the old pre-PCB B-direction condition.

| Gate | Priority / owner | Minimum closure evidence | Current status |
|---|---|---|---|
| NS-UART / JTAG | P1 user + system/board operator | Official CP2102N driver restored, COM enumerated; actual JTAG adapter and existing safe server visible; then read-only identification | BLOCKED Code28, no COM/JTAG; no install/write authorized |
| PC-B01 Rev3 | P0 user/vendor | Exact revision schematic/full part/VCCO/PSclock/UART/DDR and current image ownership | BLOCKED; generic2023.1 candidate only |
| PC-B02 central power | P0 electrical reviewer | Per-rail max/startup/fault budget and header capacity with single protected source/no backfeed | CENTRAL_POWER_BUDGET_BLOCKED |
| PC-B03 transducers | P1 supplier/bench operator | Exact T/R ordering codes, rated continuous/burst excitation, batch dimensions, impedance/current/thermal sweep | Images transcribed; bench NOT_RUN |
| PC-B04 RXAFE | P0 electrical/bench reviewer | Exact RX, AFE/protection/blank/gain/filter/noise/group-delay/40kHz measurements | HOLD |
| PC-B05 C-16 analog | P0 electrical/bench reviewer | Reference/supply/brownout/straps/highBW/anti-alias/phase/SNR and independent review | USER_DIRECTION_APPROVED; ELECTRICAL_HOLD |
| PC-B06 protection | P0 electrical reviewer | TVS/eFuse/fuse/wire/inrush/thermal coordination; NC estop/localwatchdog/coldrearm real cutoff injections | PROPOSED / SIMULATED_ONLY |
| PC-B07 BRAM/external timing | P0 independent RTL/electrical reviewer | Real decision for P-20261010-001; reset-at-capture proof; complete DRC/CDC; production pins/66MHzIOminmax/SI |346 inherited REQP-1839 plus1OOC PS warning; board timing HOLD |
| PC-B08 target application | P1 platform owner | Qualified XSA/BSP/linker/OCM/UART/I2C/IRQ and linked ARM ELF with logged success | Portable Cortex-A9 object PASS; BSP application BLOCKED |
| PC-B09 temperature/acquisition | P1 bench operator | Three timestamped actual sensor readings, ADC waveforms, coarseTOF/phase gauges and air bias | Digital synthetic / host fixture PASS; real NOT_RUN |
| PC-B10 acoustic/fullTX | P1 bench operator |128TX response/polarity/frequency/temperature, field maps and physical particle tests | UNMEASURED |
| PC-B11 nativeCAD/ERC | P1 CAD/electrical reviewer | Connected native EasyEDA project, every symbol/net/passive pin allocated, actual ERC warnings resolved | Network contract only; ERC_NOT_RUN; MANUFACTURING_HOLD |
| PC-B12 review/merge | P1 user + independent reviewer | Review concrete new stacked Draft PR and dependencies; explicit merge approval | PENDING; main untouched |
| PC-B13 externalChat | P2 user/tool environment | Real exported history or supported reader; genuine independent decisions | BLOCKED; no fabricated transcript/decision |

S5 real UART->PS->AXI->PL volatile test is NOT_RUN. A2's board facts, safe isolated outputs, known image/recovery and explicit reset/download/RAM-write approval must all be present before any write. No missing physical gate blocks safe offline implementation, regression, reports or Draft publication.

Rollback before merge: retain the new candidate branch and switch a separate clean checkout to PR3 baseb08ccf58. Never reset/clean the original sandbox. Revert C-16 adaptation only through a reviewed normal revert/decision; it must not silently withdraw the user's formal device choice. Current evidence and all failed logs remain preserved. No board state restoration action was needed because no hardware state was changed. If the user later approves an affected hardware test, its reviewed image must include a separate restore plan. Main merge and postmerge fresh-main regression remain deferred.


## Latest validation

v5/evidence/next_stage/20261010/FINAL_VERIFICATION.json; TEST_MATRIX.csv; native_reproduction.json; SOURCE_REPRODUCTION.json; full before/after/clean logs; no physical result.

## Known limitations

[
  "SameOS/EDA clone only",
  "346REQP-1839+1OOCwarning and161input/148outputexternaldelay gaps",
  "No targetBSPapplication/realUART/ADC/TMP117/acoustic/nativeERC/manufacturing qualification",
  "ExternalChatGPTBLOCKED; independent/userreviewPENDING; mainunmerged"
]

## Do not change

[
  "Frozenarchive blob/mode/path and originalphysicalsandbox; no default historybodyreads",
  "Original171tests/goldens/35dBthresholds/protocol/safety/ownership/invariants",
  "No hardwarewrite/reset/init/programming/unknownIO/driver/boot/mainmerge/forcepush without actual approved gates"
]

## Invariants

[
  "v5only",
  "128TX8RX/32lanesx4",
  "independent8bitrequested/calibration/commonclock/fullatomicmapsACK",
  "50Hz localmotion/40kHz localcarrier",
  "12mmpitch/100mmnominal90-115mmradiatingfacegap/geometriccenter",
  "One8chC16ADC/3TMP117/twoindependentarray12V/centralprotectedAX7020single-source"
]

## Open AI Problems

P-20261008-001, P-20261009-001, P-20261010-001

## Repository delta since CP008

CP008PR3historicalcandidate continues samev5; actualnewuserapprovedC16, additive offlineimplementation and all new evidence, BRAMrisk, no physical closure

## Resume instruction

Read current states/checkpoint then next_stage FINAL_REPORT, FINAL_VERIFICATION, OPEN_GATES and actual publication receipt. Continue v5; do not rerun history moves or board writes. Wholeplatform REVISE; review candidate before any merge.

## Evidence references

v5/evidence/next_stage/20261010
v5/docs/next_stage/FINAL_REPORT.md
v5/docs/next_stage/OPEN_GATES.md
shared/next_stage/PUBLICATION_RECEIPT.json

## State conflicts

Older B-formal/pendingC16 text superseded by actual user direction, not rewritten as history. Historical boardID/OOC evidence not current physical closure. Full DRC expands truncated warnings; no waiver. Newclone EOL failure corrected from own Git blobs; original evidence preserved.

## Provenance and commit resolution

Actual user instruction and matching Decision/ProblemHash
CurrentGit/source/config/S0raw audit
Fresh before/after/clean logs/two simulators/native fullreports
Actual user reseat + current XSDB/Vivado read-only results; earlier OS snapshots superseded for JTAG only
Containing checkpoint/evidence commit resolves through git log; null self-commit is deliberate, never a fabricated future SHA.


Current JTAG update after actual user reseat: After the actual user reseated JTAG, dedicated localhost3122 XSDB/Vivado2025.2 read-only identification PASS: xc7z020 ID0x23727093; both Cortex-A9 Running before/after; BOOT_MODE0x05, DDRC0x81/0x3e; PL DONE/EOS1, existing image identity UNKNOWN. Sysmon zero/-273.1 values INVALID, no voltage/temperature claim. Original Vivado GUI retained; owned server disconnected/stopped. CP2102N remains Code28/0COM. No halt/reset/init/download/memory/DDR-RAM/GPIO/driver/serial write. Real UART->PS->AXI->PL and A2 write gate remain STOP. Evidence: v5/evidence/next_stage/20261010/jtag_reseated/summary.json.
