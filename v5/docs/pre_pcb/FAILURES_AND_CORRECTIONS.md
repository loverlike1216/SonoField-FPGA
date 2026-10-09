# Preserved failures and corrections

Raw logs remain immutable under evidence/pre_pcb_20261009; failed directories
are not promoted to successful evidence. No core test/golden/threshold changed.

* Initial BOM reader saw a UTF8 BOM in CSV header; use utf8-sig.
* Initial standalone unit invocation from repo root lacked the v5 package path;
  rerun from v5 with the existing interpreter. Initial stale/future timestamp
  test exposed future acceptance; timestamp is now explicitly checked.
* Host C Werror caught indentation and integer fabs issues; fixed actual source.
* platform_connected1 lacked generated header registration; connected2 rejected
  SystemVerilog module-reference top. Explicit headers and Verilog top fix the
  actual BD build; neither failed run is treated as platform success.
* platform_connected3 had−.217ns WNS and state-dependent asynchronous loading
  inferred latches/gatedclock. Supervisor rewritten to constant fault latch and
  synchronous state. Two simulators and connected4 route now give+.068ns WNS,
  +.070ns WHS,0internalclock/unconstrained errors. External timing holds persist.
* system1 completed10fits then failed on DLL symbol visibility; exported host
  fixture adapters now call the real C functions.
* system2 passed independent20480word comparison then failed GUI/C phase parity:
  GUI inherited40.3kHz historical fixture whereas new C logical fixture uses
  40kHz. New zero-error nominal reference explicitly uses40kHz; original
  calibration file remains unchanged. system3 complete fivecase gate passed.
* system3 exposed Tk after-callback cleanup warnings when successive test roots
  close. Store/cancel the actual callback before destroying the root; verify
  final source independently in the clean checkout.
* New transfer test tried deleting a loaded Windows DLL in TemporaryDirectory;
  build generated DLL under the ignored v5 build scratch instead.
* Standalone all171_final used Windows globalTEMP and correctly failed9 existing
  configuration-path guards. all171_retry1 sets clone-localbuild TMP/TEMP as
  the original baseline runner already does;171tests pass. No guards weakened.

The first automated GUI screen capture was occluded by another window and was
discarded; it is not UI evidence and is not published. Capture only an explicitly
raised application window and visually verify the final generated image.

## Final integration corrections and evidence qualification

* The inherited queue retains STOP until reset. The new wrapper now preserves
  safe internal prefill while physical OE/eFuse remain supervisor dominated;
  STOP/fault resets the core. Queue faults asynchronously inhibit both banks.
  Rearm requires a fresh low-to-high mailbox publication; a held old publication
  cannot restart motion. Full new-top tests verify this in Icarus and XSim.
* top1 printed an ADC-vector file ERROR alongside its PASS marker. It is invalid
  evidence. The runner now supplies an explicitly synthetic zero vector file
  and rejects ERROR/FATAL even when a PASS marker is present. top_final caught
  an XSim declaration-order error; top_verified passes both simulators.
* Vivado bare assign_bd_address returned success with critical warnings and
  only the core mapped. Earlier connected*/platform_final PS address spaces
  are NOT accepted. Six explicit 64KiB windows now have offset/range/unique
  mapping assertions. Read-only PS interrupt-count setting was removed; the
  propagated count is asserted to be five. Explicit BRAM clock metadata and
  exported serializer data strobes remove the IP-interface critical warnings.
  Final clean-clone platform_verified has no critical warning or ERROR.
  Earlier PL-only route reports retain their stated OOC scope.
* A reopened-DCP review helper first queried nonexistent RULE on a violation;
  that attempt failed. The corrected helper saves actual property reports.
  Default DRC reports 22 warnings including a REQP-1839 limit at 20 entries;
  this is a reported subset, not proof that only 20 physical risks exist.
  No rule was waived, disabled, downgraded or used to claim board acceptance.
* Vitis script execution can return OS exit0 despite a Python traceback.
  Actual preflight output is PS_TARGET_BUILD_BLOCKED, with no reviewed target
  BSP/XSA and no ARM compiler on PATH; exit0 is not a target-build success.
* Native PrintWindow captures only the known Tk application client. Final
  clean-clone GUI case3 image was visually inspected; no desktop/sidebar is
  captured or published. Five final cases total375frames; earlier361frame
  results precede corrected nearest-point selection and the explicit3D edit.

Final evidence paths and accepted-source hashes are in FINAL_VERIFICATION.json
and PRE_PCB_COMPLETE_REPORT.md. Failed/raw earlier records are retained.
