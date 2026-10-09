# v5 next-stage execution report — 2026-10-10

Offline candidate: **ACCEPT WITH LIMITATIONS**. Real-board scope: **REVISE**. Whole platform: **REVISE**. The final user/independent review is pending; these are scoped execution conclusions, not physical release certification.

Project SONOFIELD_FPGA, same repository, v5ACTIVE/highestv5, current branch `codex/v5-ad7606c16-nextstage-20261010`, workspace `E:\Codex_project\AMD_Sonofield`. Source implementation6274330f98955fa0d4c4703a90d31bc1421104fb; final audit/tool source `feb97ad5c95088affaf075cb034fe29d4b5aeda0`. Base PR3b08ccf58, main ecd32e76 unchanged. PR1(d7f7b60)→PR2(7dda49f)→PR3(b08ccf5)→new Draft candidate. PR3 contains PR1/2 ancestry. No duplicate cherry-pick, old sandbox access, archive body read, hardware write or main merge. Publication receipt is `shared/next_stage/PUBLICATION_RECEIPT.json` and supplies the actual new PR URL/commit/CI after this evidence seal.

## Decisions and implementation

The actual user explicitly approved AD7606C-16. The matching P-20261008-001 Decision verifies unchanged v5 Problem bodySHA231aa1770662448c8e9f9cd83aa1b309abcbc21790ffd26eb58821ffe33843ab. No external ChatGPT Decision was invented; access remains BLOCKED. This closes device direction, while ordering suffix/native footprint/analog electrical qualification remain HOLD.

New C16 state machine and independent delayed device model isolate device-specific startup/register/readback/timing. CONFIG02=10, allchannel BW07=ff, ranges03..06=11(+/-5VSE), OS08=0, interface21=0, ID2f nibble2. Readback must pass before ready. Default2s startup,4usreset/275ussetup; only simulation startup is accelerated. Actual integration uses nextstage_pl→prepcb supervisor/mailbox→unchanged AXI/motion/phase core with ADC_C16=1. Original B adapter/model/tests/goldens/default parameter remain regression provenance. Eight signed channels,1024frames16KiB, common timestamps and capture ownership/ACK are preserved. CRC-enabled frames are unsupported; unexpected CRC configuration is rejected. ADC-onlybrownout/realPGOOD/analogSNR/anti-alias/externaltiming are NOT_VERIFIED.

Portable C/Python profile and TMP117 adapters check ID/readiness/EEPROMbusy/NACK/sentinel/range/provenance. Three temperature segments and existing speed-of-sound/phase integration are tested synthetically; humidity is diagnostic. Sparse16+16 scans preserve independent RX gauges/coarseTOF requirements and do not claim full128TX electroacoustic calibration. Same runtime editor retains dynamic XYZ/Bezier handles/undo/redo/limits/save-load/upload/start/pause/resume/stop. REAL_BOARD transport is explicitly locked. The16KiB Snapshot class is an ownership reference; existing bounded240byte production RAW protocol is preserved, no deployed DMA claim. At1152008N1,16KiB payload alone needs>=1.422s, while raw800kSPS8ch rate is12.8MB/s; no continuous UART streaming claim.

## Tests and independent evidence

| Gate | Measured result | Limit |
|---|---|---|
| Original tests/additions |171 original+32new=203; current final203 and clean203PASS | after-run discovery was199; four contract tests added later and executed separately |
| Full before/after/clean |3696frames×3Icarus+1XSim in each; all canonical trajectory/map/trap/ACK hashes equal | model/RTL evidence, no real particle tracking |
| C/AXI/safety/equivalence | all original gates PASS;35dB thresholds unchanged | lowSNR failed/rejected records retained |
| Temperature |160maps/20480C-Python channel words match | synthetic temperatures |
| Sparse |10fits/5seeds/5starts/384holdouts; maximum translation0.002275190mm, rotation0.003091529deg, holdout10.236393ns | synthetic, not perTX hardware calibration |
| Runtime GUI |5actual callback cases375frames plus3696-frame gate | automation, not a human manual acceptance |
| C16 independent adapter |64signed+32continuous800kSPS frames;5badreadbacks and BUSY/reset/overlap; two tools sameSHA11a9e2c3f9e601b616a7053db0b79efd098730a0fd2a9c76446bd19ba12a9ecb | CRCoff profile; no analog measurements |
| C16 full capture chain |2×1024signedframes, 4BRAMwords/frame, timestamp/burst/ownership/ACK/abort; two tools plus cloneSHAff6001e389b357f4339f5d5133a2afb304329d0a2b050acae433bc856464d4b0 | BRAM reset electrical risk remains |
| C16 integrated top |37maps, both tools ACKSHA84db46a42298ea8f89938a7a23dd7dd60a5eabd44b375d10471f583c84abac8f | actual candidateRTL, no programmed board |
| Host C PING |1000/1000; p50=6us,p95=7.5us,p99=12.501us,max99.3us current fixture | in-process compiledC, never UART/PS/AXI latency |
| Target compile | AMDClang16.0.6 Cortex-A9 ELF32 ARM relocatable object; identicalSHA9c0f09221b1e4a1748875dce96b459f1ab97ddda5780971fca68e488118536ff | not linked BSP application |
| Independent clone | nohardlinks, fresh locked12dependency venv, history worktree absent; full gates+supplements PASS | same Windows/EDA installation |

Current tools: PowerShell7.6.5, Python3.10.11, GCC9.2.0, Icarus12.0devel, Vivado2025.2, Vitis2025.2 launcher. XSDB2025.2 performed the later bounded read-only identification described below. Vitis launcher exit0 contains a traceback; full target application remains BLOCKED. All timing/latency statistics are scoped to their measured environment.

## Native Vivado result and physical risk

Fresh clean native2025.2 BD/XSA/build exits0; actual current and clone XPR/BD/DCP reopening exits0. Explicit23currentv5 sources only;6AXIwindows,5IRQs,3IIC, DDRoff logicalcandidate. Internal132MHz route: WNS+0.038ns/WHS+0.068ns/TNS0/THS0,7480LUT/20223FF/4RAMB36. Current/clean timing, resource and full DRC report bodies are exactly equal, excluding only nonfunctionalDate/Host/Command headers. Candidate partxc7z020clg400-2 is documented-device scope, not measured fullgrade proof.

Production timing is HOLD:161input and148output delays absent, physical pins/VCCO/clock/UART/DDR/preset/IO66MHzPVT/cables unqualified. Full DRC shows346REQP-1839(RAMB36 async control) plus1ZPS7-1(OOC PS). Empty CDC output skips unqualified IO and cannot prove reset/board safety. The346warnings are fully reported, not waived; P-20261010-001 requests independent reset/BRAM architecture review while preserving asynchronous emergency kill. No important architecture change was silently made. Positive slack cannot close that risk.

## Actual hardware and PCB status

After the actual user reseated JTAG, dedicated localhost3122 XSDB/Vivado2025.2 read-only identification PASS: xc7z020 ID0x23727093; both Cortex-A9 Running before/after; BOOT_MODE0x05, DDRC0x81/0x3e; PL DONE/EOS1, existing image identity UNKNOWN. Sysmon zero/-273.1 values INVALID, no voltage/temperature claim. Original Vivado GUI retained; owned server disconnected/stopped. CP2102N remains Code28/0COM. No halt/reset/init/download/memory/DDR-RAM/GPIO/driver/serial write. Real UART->PS->AXI->PL and A2 write gate remain STOP. New current evidence: `jtag_reseated/summary.json`, before/after XSDB logs and Hardware Manager report. Earlier no-JTAG observations remain timestamped failures rather than being rewritten.

Two user vendor images were inspected fully and transcribed/hash-recorded without publishing private originals. NU40C10T family formal; exact T-2/R-2 order codes and continuous drive remain HOLD.40Vp-p is a stated maximum, not a continuous recommendation.9.8±0.5mm body and12mm pitch imply theoretical1.7mm worstbody clearance, unmeasured assembly. User39.68/40/40.32kHz observations remain user preliminary inputs; bench SOP checks generator/scope timebase/trigger/window before resonance or Doppler claims.

Seven-sheet Excel BOM has80line types; candidate installed units488upper/488lower/83central/13external (includes aggregate assemblies; B-016zeroqty allocation note is excluded). Formula caches, quantities, references and upper/lower symmetry were independently tested; all pricesUNKNOWN. ADC64pins (unusedDOUTE-H NC),80connectorpositions,3TMP117, oneADC, reference/REGCAP/REFCAP, AFE/power/protection/net contracts and SVG overview are candidates. Upper/lower each independent protected external12V; central only single protectedAX7020rail source, no backfeed/parallelheaders. Capacity, TVS/eFuse/fuse/inrush/wire/thermal/MPN/nativepinallocation/SI remain HOLD. The48pointCV²fsensitivity is theoretical, not measured power or an upper bound. No connected nativeEasyEDA; schematicNOT_CREATED/ERC_NOT_RUN/MANUFACTURING_HOLD, no fabricated Gerber/ERC.

## Preservation, failures and reproducibility

S0 audits3324currentfiles;3026original tests/goldens/evidence/BOM files retain rawSHA;3918archiveblob/mode/path metadata remains identical without body reads. Exact six-file parameter/config adaptation hashes are pinned, and reviewed-change keys cannot exempt tests/goldens/thresholds. Original submitted BOM/evidence remain immutable.202currentfunctional/script files match canonicalLF hashes across clone;200matchraw,2newtexttools differ onlyEOL (nextstage_source_list.txt/build_nextstage_bom.mjs). The strict S0 raw check passes in both workspaces.

Fresh clone initially inherited globalcore.autocrlf=true;141unchangedrawfiles differed onlyEOL and strict audit correctly FAILED. Set localfalse and reconstruct exactS0bytes from the clone's own Git objects; no root body copy, no history read, no checker relaxation. Raw failure and materialization receipts are retained. Full clone used627source; later ordinary fast-forward to finaltoolsource adds capturebench/audits/BOMformatting, not runtimeRTL/C/Python behavior. Final203, newcapturechain, strictpreservation/source/native checks validate those supplements. See REPRODUCE.md for repeatable byte policy, fresh output paths and failure handling.

FAILURE_REGISTER.json preserves ADCmodel/bench reset issues, first twoBD wrapper failures, currentrun3 final invalidreportflag, incorrectunitcwd/TMP runs, EOL audit failure, truncatedDRC reporting attempts and Vitis traceback. No failing original assertion,35dBthreshold or golden was removed or weakened. Raw native logs with Windowsidentity are retained locally under ignoredlocal_raw; public copies redact only private identity/path fields and keep raw/public hashes. Generated executables/caches are excluded from Git; public reports/maps/traces remain auditable.

## Review boundary and rollback

All13PC-Bgates remain scoped open with owners/minimumclosure in OPEN_GATES.md; ADC direction alone is closed. NewBRAMProblem isOPEN; externalChatGPTBLOCKED and independentreviewPENDING. Source/contract tests do not qualify analog, electrical or manufacturing release. No fakehardware source, lowerthreshold, historical rewrite, forcepush or directmainmerge.

Before merge, retain the candidate branch and use a separate clean checkout of PR3b08ccf58 for rollback. A reviewed normal revert plus full regression can undo candidate changes; no reset-hard/blanketclean or oldsandbox modification. ADC direction remains user-approved until another actual decision. No hardware restoration was needed because no hardware state was changed. Any future board experiment needs its own approved image/operation/recovery/isolated-output plan. Main merge and fresh remote-main full regression remain deferred to explicit user approval of the concrete PR.

Evidence index: v5/evidence/next_stage/20261010/EVIDENCE_INDEX.md; matrixTEST_MATRIX.csv; machineFINAL_VERIFICATION.json; current checkpointshared/CONTEXT_CHECKPOINT.*. Observable actual Codex messages/tools arePARTIAL with source hashes/cutoff; no hidden reasoning or inaccessible ChatGPT history is recorded.
