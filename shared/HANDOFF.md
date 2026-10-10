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

# Current v5 handoff

Goal: current user-approvedAD7606C-16 nextstage candidate; samev5/repository and independentnewworkspace. Inputs exactinstruction/userphotos/currentGitPR1/2/3/currentcode/state and officialsources. Changes: separateC16adapter/model/C-Python-TMP117/lockedGUI/BOM/netcontracts; originalcore/defaultB/tests/goldens/criteria preserved. Tests: fullbefore/after/clean3696x4;final203both;new2048capture/37mapC16top/ADCnegative two-tool;160temperaturemaps/10sparsefits/5GUIcases;actualARMobject;native2025.2logicalplatform/reopen/reportmatch. Evidence FINAL_VERIFICATION and TEST_MATRIX in v5/evidence/next_stage/20261010.

Failures: FAILURE_REGISTER preserves model/bench/BD/reportflag/cwdTMP/EOL/DRC/Vitis issues, not discarded. Unresolved:13PC-Bgates and P-20261010-001BRAMresetrisk; realUART/ADC/TMP117/cutoff/acoustics/boardapplication/nativeERC NOT_RUN/BLOCKED. Risks: missingRev3ownership/power/IO/PSDDRfacts and346DRC warnings; offlinepositiveWNS notphysicalproof. Decisions: actualUserC16direction approved, importantresetarchitecture pending independentdecision; ChatGPT readerBLOCKED. Next actualDraftpublicationreceipt, independent/userreview, no mainmerge/hardwarewrite/manufacturing. Resume CP-20261010-001 and FINAL_REPORT, no archivebodyreads or oldsandboxfallback.


Current JTAG update after actual user reseat: After the actual user reseated JTAG, dedicated localhost3122 XSDB/Vivado2025.2 read-only identification PASS: xc7z020 ID0x23727093; both Cortex-A9 Running before/after; BOOT_MODE0x05, DDRC0x81/0x3e; PL DONE/EOS1, existing image identity UNKNOWN. Sysmon zero/-273.1 values INVALID, no voltage/temperature claim. Original Vivado GUI retained; owned server disconnected/stopped. CP2102N remains Code28/0COM. No halt/reset/init/download/memory/DDR-RAM/GPIO/driver/serial write. Real UART->PS->AXI->PL and A2 write gate remain STOP. Evidence: v5/evidence/next_stage/20261010/jtag_reseated/summary.json.


Publication milestone: DraftPR4 https://github.com/loverlike1216/SonoField-FPGA/pull/4 is OPEN/Draft onPR3. Evidencecommit24c2056870db092ec1fd4b8d1ac679d6b7bc9d6c remote verified; push+pull_request Ubuntu structural CI PASS. PR1/2/3 and main unchanged/unmerged. Actual containingreceiptcommit resolves through Git; latest CI remains observable in GitHub. Review candidate/BRAMreset/physical gates; no additional runtime optimization or main/board/manufacturing operation. See next_stage/PUBLICATION_RECEIPT.json (under shared).
