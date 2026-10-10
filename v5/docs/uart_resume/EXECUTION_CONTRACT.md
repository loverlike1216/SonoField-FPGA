# v5 UART continuation execution contract — 2026-10-10

Goal: resume the user-reported UART-driver blocker, maximize safe offline target
build progress, preserve the running AX7020 program, and synchronize the same
GitHub Draft candidate. Same project, repository, workspace and sole active v5.

Inputs: actual user reports that COM3 is the board USB-UART and J10/J11 have no
external modules. The later user correction says factory files are remote in
provided vendor shares; there is no local recovery copy. Their provenance and
recoverability are unverified. The exact next-stage S0–S7 instruction remains
canonical; continuing is not permission for halt/reset/init/download/boot writes.

Allowed changes: clone-local locked pyserial dependency, read-only OS discovery,
bounded SLCR reads through an owned server with CPUs Running before/after,
additive 2025.2 BSP build tooling and compatibility includes, independent clean
reproduction, current state/evidence/interaction records and ordinary branch
commits/push/updates to Draft PR4. No main merge is authorized.

Preserve: all existing v5 digital core sources, tests, goldens, BOM/evidence,
protocol, 35 dB criteria, signed capture/ACK, independent requested/calibration
fields, atomic maps, common clock, 128TX/8RX, 32 lanes × 4, 50 Hz motion and
geometry. Formal ADC direction remains the actual user-approved AD7606C-16.
Do not read archived source or access the original physical sandbox.

Architecture: existing 2025.2 DDR-disabled logical XSA, installed native SDT and
EmbeddedSW BSP flow, a qualified Cortex-A9 compiler, and the unchanged existing
safe/status PS service. The SDT time compatibility include forwards existing
XTime APIs to xiltimer; it does not invent hardware timing. This application
does not advertise full motion or sensor runtime capability.

Validation: enumerate COM without opening it; preserve raw and redacted board
logs; run original 203 tests with clone-local scratch and actual host GCC; build
real BSP libraries and linked ARM ELF; audit entry/load segments and reject DDR
or malformed candidates; repeat from an independent sparse clone and fresh venv;
verify S0 raw hashes, old sealed evidence, frozen Git metadata and publication.
Do not mistake a tool launcher's exit status alone for a successful artifact.

Evidence: fresh v5/evidence/uart_resume/20261010_01; ignored local_raw/private
logs and all binaries remain local. Publish only reviewed redacted evidence,
checksums, actual source provenance, failures, limitations and observable records.
Same OS/native EDA/toolchain reproduction is the declared independent scope.

Physical gates: exact Rev3 UART DTR/RTS wiring, complete part/VCCO/clock/platform,
known current image and RAM/CPU ownership, validated recovery, independently
disabled outputs, and separate explicit permission for affected board writes.
COM presence, empty headers and remote downloads alone do not close these gates.

Rollback: no board restoration is needed for these read-only observations.
Retain the branch and evidence; use a separate clean checkout of the prior
candidate daa0e82e08d1459206fde50af2186bca879ba24c or a reviewed normal revert.
No reset--hard, blanket clean, old sandbox modification or history rewrite.

Done when: all safe continuation checks have real results and a remote-verified
Draft update; open physical gates are explicit, checkpoint is recoverable and
main remains unchanged. Offline candidate and physical system receive separate
quality conclusions. Independent/user final review remains pending.
