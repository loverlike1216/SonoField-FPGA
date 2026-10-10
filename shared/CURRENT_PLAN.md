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

# Current plan — v5 next-stage review

S0 COMPLETE: latest PR1/2/3/main reconciled, new branch on PR3,3324S0 hashes; actual user C16 direction/ProblemHash/version persisted. No old sandbox or archive body access.
S1 COMPLETE_HARDWARE_READONLY / UART_BLOCKED: After the actual user reseated JTAG, dedicated localhost3122 XSDB/Vivado2025.2 read-only identification PASS: xc7z020 ID0x23727093; both Cortex-A9 Running before/after; BOOT_MODE0x05, DDRC0x81/0x3e; PL DONE/EOS1, existing image identity UNKNOWN. Sysmon zero/-273.1 values INVALID, no voltage/temperature claim. Original Vivado GUI retained; owned server disconnected/stopped. CP2102N remains Code28/0COM. No halt/reset/init/download/memory/DDR-RAM/GPIO/driver/serial write. Real UART->PS->AXI->PL and A2 write gate remain STOP.
S2 COMPLETE_DIGITAL_CANDIDATE: separate C16 init/readback/timing/model/C/Python/fullcapture/actualtop, two tools and fresh clone. Analog/brownout/CRC-enabled profile NOT_VERIFIED.
S3 COMPLETE_OFFLINE: preserve original core/35dB/goldens/protocol; three-temperature/sparse/dynamicXYZBezierGUI/Cfixture1000PING. Synthetic/hostfixtures labeled, no particle-tracking claim.
S4 COMPLETE_LOGICAL_NATIVE / TARGET_APPLICATION_BLOCKED: native2025.2 BD6windows5IRQs3IIC/DDROFF and PL OOC route/reopen; portableARMobject realcompile. Matched Rev3/XSA/BSP/linker/OCM/UART and346BRAMwarnings/externaltiming remain STOP. P-20261010-001 requires a real independent reset/BRAM decision.
S5 NOT_RUN_A2_STOP: no physical UART/PS/AXI/PL writes without matched platform/currentimage ownership/recovery/isolatedoutputs plus explicit affected-operation approval. No broad prompt authorization substitutes for A2.
S6 COMPLETE_CANDIDATE_CONTRACTS / ELECTRICAL_HOLD: seven-sheet80typeBOM, ADC64/connector/net/SVG contracts/benchSOP/source reviews; no nativeCAD/ERC/manufacturing release.
S7 OFFLINE_COMPLETE: fullbefore/after/clean,final203,newcapture,rawS0/archivemetadata/source/report/tracehashes; preserve failures, privacy scan, currentstate/checkpoint. Next normalpush+stackedDraftPR onPR3 and actualCI/remote receipt. No merge/cancel of PR1/2/3, no forcepush.

After publication, stop optimization and deliver concrete review package. User/independent reviewer closes actual hardware/electrical/BRAM gates. Current entry v5/scripts/run_nextstage.py and docs/next_stage/REPRODUCE.md; outputs/venv inside current clone only. Continue remains v5. Main promotion and fresh remote-main full regression follow explicit candidate approval only.


Publication milestone: DraftPR4 https://github.com/loverlike1216/SonoField-FPGA/pull/4 is OPEN/Draft onPR3. Evidencecommit24c2056870db092ec1fd4b8d1ac679d6b7bc9d6c remote verified; push+pull_request Ubuntu structural CI PASS. PR1/2/3 and main unchanged/unmerged. Actual containingreceiptcommit resolves through Git; latest CI remains observable in GitHub. Review candidate/BRAMreset/physical gates; no additional runtime optimization or main/board/manufacturing operation. See next_stage/PUBLICATION_RECEIPT.json (under shared).


UART publication milestone: evidence commit d76999c658c32be2ccb1602353054b7bf2c953cd remote verified; DraftPR4 updated and remains OPEN/Draft onPR3. Push+PR Ubuntu structural CI PASS at that commit. Main ecd32e76 unchanged. See shared/uart_resume/PUBLICATION_RECEIPT.json for exact source/CI/rollback/review boundary. A0/A2 and physical gates remain open.
