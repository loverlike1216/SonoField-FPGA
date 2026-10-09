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
