# UART continuation amendment — 2026-10-10

Current result: offline ACCEPT WITH LIMITATIONS; real-board/whole-platform REVISE.
COM3 now Code0 with driver11.6.0.420; pyserial3.5 locked. New read-only SLCR check
kept both CPUs Running, originalVivado retained; no UARTopen/TX/boardwrite.
Actual2025.2nativeSDT/BSP+ArmGNU13.2 linked safe/status ARMELF and OCM audit PASS
in current/newcleanclone;203+203tests PASS. FullELF is not claimed bit-exact;
application .text matches. Vitis platformAPI missingQEMU failure and RWX warning
remain. Prior1160sealedfiles and original criteria preserved.
User correction: recovery files are remote references only, no local verified
backup. Rev3 DTR/RTS A0 and image/platform/recovery/isolation/permission A2 gates
remain open. PC-B08 logicalbuild subgate closed; physical13PC-B scopes/BRAMProblem
and independentreview stay open. Samev5/mainunmerged/Draft4 update authorized.
See v5/docs/uart_resume/RESULT.md, v5/evidence/uart_resume/20261010_01/FINAL_VERIFICATION.json,
CP-20261010-002 and shared/uart_resume/PUBLICATION_RECEIPT.json. Prior snapshots
below retain provenance; this amendment supersedes only their stale current facts.

---

# SonoField-FPGA v5 current engineering state — 2026-10-10

SONOFIELD_FPGA; same repository; `codex/v5-ad7606c16-nextstage-20261010`; workspace `E:\Codex_project\AMD_Sonofield`; v5ACTIVE/highestv5. Current ADC direction AD7606C-16 is explicitly user-approved, electrical/package/analog release HOLD. CP `CP-20261010-001` records the current candidate, not a main merge or version upgrade. Runtime implementation6274330f, final audit/tool sourcefeb97ad5c95088affaf075cb034fe29d4b5aeda0; PR3baseb08ccf58, main ecd32e76 unchanged.

Offline **ACCEPT WITH LIMITATIONS**, real-board **REVISE**, whole-platform **REVISE**. Full before171/after199(initialdiscovery)+final203/clean203;3696frames×4each with identicalcanonical trajectory/map/trap/ACK;160maps/20480Cwords;10sparsefits/5seeds/5starts/384holdouts;5runtimeGUIcases375frames; new C16adapter/full2048framecapture/37mapintegratedtop two-tool and clonePASS. Original tests/goldens/35dBcriteria/evidence/BOM remain protected. Freshlockedvenv/nohardlinks/history-absentclone passed, with EOL-only checkout failure and exactrawGit-derived correction recorded.

Real Vivado2025.2 C16logicalBD/XSA/OOC/reopening; WNS+.038/WHS+.068ns,7480LUT/20223FF/4BRAM; same fullreport bodies across clone. ProductionIO161in/148outdelays absent. FullDRC346REQP-1839+1ZPS7-1 remains unwaived; new P-20261010-001OPEN. Actual CortexA9portableobjectPASS; VitisBSP-linkedapplicationBLOCKED.

After the actual user reseated JTAG, dedicated localhost3122 XSDB/Vivado2025.2 read-only identification PASS: xc7z020 ID0x23727093; both Cortex-A9 Running before/after; BOOT_MODE0x05, DDRC0x81/0x3e; PL DONE/EOS1, existing image identity UNKNOWN. Sysmon zero/-273.1 values INVALID, no voltage/temperature claim. Original Vivado GUI retained; owned server disconnected/stopped. CP2102N remains Code28/0COM. No halt/reset/init/download/memory/DDR-RAM/GPIO/driver/serial write. Real UART->PS->AXI->PL and A2 write gate remain STOP.

Seven-sheet80typeworkingBOM and threeboardADC64/connector/net/SVG contracts are proposed; oneADC/3TMP117/upper-lowersymmetry checked. AllpricesUNKNOWN. CentralAX7020protectedsingle-sourcecapacityBLOCKED; twoindependentexternal12Varrays and safety circuits unqualified. NativeEasyEDAunavailable, schematicNOT_CREATED/ERC_NOT_RUN/MANUFACTURING_HOLD. All13PC-Bgates and threeProblems remain scoped open; device direction alone closed. ExternalChatGPTBLOCKED, actualCodexmessages/toolsPARTIAL.

See [final report](../v5/docs/next_stage/FINAL_REPORT.md), [machine verification](../v5/evidence/next_stage/20261010/FINAL_VERIFICATION.json), [open gates](../v5/docs/next_stage/OPEN_GATES.md), [reproduction](../v5/docs/next_stage/REPRODUCE.md). PR1→PR2→PR3→newcandidate; PR3 contains earlier ancestors and all remain unmerged. Publication receipt [shared/next_stage/PUBLICATION_RECEIPT.json](next_stage/PUBLICATION_RECEIPT.json) is authoritative for actual newDraftURL/remotecommit/CI after sealing. Main/user approval and postmerge regression remain deferred.


Publication milestone: DraftPR4 https://github.com/loverlike1216/SonoField-FPGA/pull/4 is OPEN/Draft onPR3. Evidencecommit24c2056870db092ec1fd4b8d1ac679d6b7bc9d6c remote verified; push+pull_request Ubuntu structural CI PASS. PR1/2/3 and main unchanged/unmerged. Actual containingreceiptcommit resolves through Git; latest CI remains observable in GitHub. Review candidate/BRAMreset/physical gates; no additional runtime optimization or main/board/manufacturing operation. See next_stage/PUBLICATION_RECEIPT.json (under shared).


UART publication milestone: evidence commit d76999c658c32be2ccb1602353054b7bf2c953cd remote verified; DraftPR4 updated and remains OPEN/Draft onPR3. Push+PR Ubuntu structural CI PASS at that commit. Main ecd32e76 unchanged. See shared/uart_resume/PUBLICATION_RECEIPT.json for exact source/CI/rollback/review boundary. A0/A2 and physical gates remain open.
