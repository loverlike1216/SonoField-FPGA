# Optional C service adaptation

Authorization: actual user 2026-10-09 pre-PCB full-system task, existing v5.
`firmware/ps_service/service.c` and `service.h` receive a conditional include,
conditional extension pointer and conditional default dispatch. Without
`SF_PREPCB_EXTENSION`, all original commands, structures and behavior remain.
With the macro, commands32–43 are negotiated after original nonce/CRC/sequence
handshake. No old register, packet, test, golden or threshold is modified.
The inheritance manifest retains original source and initial-copy hashes; only
the two current expected hashes and adaptation explanations change.

S0 protected byte inventory and `check_prepcb_preservation.py` independently
reject every other original RTL/firmware/software/test/config/golden edit.
The baseline test count now requires at least115 so additive tests are allowed;
all original test bytes and assertions remain protected by that inventory.
This change does not permit a reduced regression or skipped test.

The extension is portable C tested with host GCC; it is not an ARM/BSP build.
`calibration_verified` defaults false. The host fixture sets it only for explicit
synthetic inputs. No UART, GPIO, sensor or calibration is invented by the target
service. Capability bits reflect installed callbacks. Missing callbacks fail
closed. Real sensor callbacks must enforce bounded hardware timeouts and retain
physical timestamps/provenance; the present host fixture is not that adapter.

Transport coordinates are signed nanometres, converted to metres in propagation
and millimetres for motion guards. Nominal acceleration/jerk limits are8mm/s²
and40mm/s³; receiver budgets8.01/41 cover worst-case1nm coordinate quantization:
second difference ≤4×0.5nm×50² per axis; third difference ≤8×0.5nm×50³ per axis.
This budget applies only to the new wire encoding, never original acceptance.

Task capacity512 is negotiated, bounded and intentionally smaller than the
editor planning limit12000. Larger tasks are rejected before transmission; no
truncation. Actual target OCM/linker allocation remains unqualified. The host
fixture performs real C CRC/sequence parsing and20ms logical ticks. RTL replay
uses the disclosed inherited shortened8192-cycle regression interval; production
2640000-cycle cadence remains covered by original tests.
