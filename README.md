# SonoField-FPGA — AX7020 v5

PROJECT_ID **SONOFIELD_FPGA** · **v5 ACTIVE** · **ALINX AX7020** · Vivado2025.2. This is a candidate workspace migration in the existing repository. Main merge and permanent workspace promotion require user review. No version upgrade.

Start with [current state](shared/PROJECT_STATE.json), [recovery checkpoint](shared/CONTEXT_CHECKPOINT.md), [runbook](shared/migration/RUNBOOK.md), [migration evidence](shared/migration/PORTABILITY_AND_REGRESSION.md), [acceptance](shared/ACCEPTANCE.md) and [rollback](shared/migration/ROLLBACK_PLAN.md). The sole production implementation is [v5](v5/README.md). Build/tests/imports use v5 only. Frozen history is excluded from everyday work and may be inspected only on explicit history/recovery instructions.

128TX/8RX, opposed8×8 arrays,8bit independent requested/calibration phases, atomic maps, common timebase,32lanes×4used,50Hz motion infrastructure and existing PS/C/AXI interfaces are preserved. TX NU40C10T; RX MPN unknown; formal ADC AD7606BBSTZ-RL. C-16 is an unapproved candidate. Geometry is12mm radiating-face pitch,100mm nominal face gap adjustable90–115mm, geometric-center origin. Upper/lower64TX arrays have independent external power/protection/cutoff; AX7020 handles signals only.

Real digital regression and documented-device OOC evidence are separate from physical acceptance. Historical AX701020.3.0/XC7Z020/CLG400 read-only identification does not prove PS-PL/DDR/UART/ADC/driver/acoustic operation. Whole-platform conclusion remains REVISE; native v5 schematic NOT_CREATED, ERC_NOT_RUN, electrical/manufacturing HOLD.50mg EPS is a future measured milestone. ChatGPT history access BLOCKED; observable current Codex records PARTIAL.
