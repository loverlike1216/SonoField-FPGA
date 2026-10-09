---
problem_id: P-20261009-001
project_id: SONOFIELD_FPGA
active_version: v5
current_stage: AX7020_BOARD_DETECTION_BOM_REVISION_AND_INTEGRATION_PREFLIGHT
status: OPEN
created_at: 2026-10-09T02:16:17.071733+00:00
created_by: Codex
model: GPT-6.1 Sol High
chat_source_name: SonoField-FPGA
chat_access: BLOCKED
problem_hash: e57cb33e5aee67620a115d901196df28d33574756f4029bfbbe03b04e66a40e4
hash_scope: UTF-8 markdown body after front matter, LF newlines
base_commit: 4dc8e765403561e9aff9980a54390cdbb01ea0ed
---

# Problem

## Decision Needed
Qualify the actual AX7020 Revision3.0 PS/DDR/clock platform and safe ownership of the currently running SD image before any volatile PL/PS test. This is a request for evidence and a bounded integration decision, not an alleged ChatGPT decision.

## Goal / Current State
Continue v5 with unchanged128TX/8RX/core protocols. Read-only JTAG succeeded; no program was downloaded. Both Cortex-A9 cores are already running and PL DONE=1. User declared only power/JTAG connected; actual photos and BOOT_MODE show an inserted SD card / SD boot.

## Repository Facts / Evidence
- Baseline source HEAD: 4dc8e765403561e9aff9980a54390cdbb01ea0ed.
- Real chain: ARM DAP0x4BA00477, XC7Z0200x23727093, packageCLG400 photo. PCB AX701020.3.0. Full speed/temp code unknown.
- BOOT_MODE0xF800025C=0x5; DDRC_CTRL0xF8006000=0x81; CTRL_REG1=0x3E. Controller32bit configuration/released reset does not prove1GiB capacity or stable memory.
- Official manual:2×HynixH5TQ4G63AFR-PBC,1GiB/32bit expected. Pinned hello XSA:32bit,15row/10col/3bank,533.333333MHz,MicronMT41J256M16 RE-125 preset. Could be compatible timing selection, but actual revision/components are not matched.
- Downloaded schematicV2.0 versus actualPCBRev3.0. hello XSA2023.1,FCLK0=50MHz,UART1MIO48/49. Core target132MHz unchanged.
- No COM enumerated, UART unplugged. No qualified target ARM compiler/BSP found. Source paths: v5/evidence/board_bringup/20261009/RESULT.md and hardware/integration_candidates/20261009/official_ps_reference.json.

## What Codex Tried
Read pinned manufacturer manual,16-page schematic and helloXSA HWH/ps7_init parameters; Windows enumeration; nativeVivado/XSDB read-only scans. No init/reset/halt/RAMwrite or external hardware operation. No repeated unsafe tests.

## Root Cause Hypotheses
The manufacturer generic preset may intentionally use an equivalent DDR component; the public schematic may cover a preceding board revision. These are hypotheses only. Unknown current image/RAM ownership makes even a volatile test potentially disruptive.

## Candidate Options
A. Obtain manufacturer Revision3.0 schematic/BOM/referencePS project and identify the currently booted image. Highest confidence, no board modification.
B. Manufacturer explicitly confirmsV2.0 design / preset equivalence for AX701020.3.0; compare all critical nets/timing/DDR geometry and then qualify minimal2025.2 platform in a separate bounded test. Must not infer equivalence from product name.
C. Later use a no-DDR/OCM diagnostic if ownership/reset/output boundaries are explicitly qualified; cannot establish DDR capacity and does not bypass preservation of the running image.

## Constraints / Acceptance Impact
No generic ZedBoard/ZC702 preset, guessed grade/XDC, boot/jumper/storage changes, unknownGPIO, permanent writes or fabricated RAM result. Physical board transport/DDR/PSPL remain NOT_RUN; digital simulation PASS remains valid in its own scope. No core/interface/acceptance change is requested.

## Questions For User / Independent Reviewer
1. Which exact Rev3 schematic/referencePS design and physical FPGA grade apply?
2. What is the current SD image, and which RAM/CPU state may be temporarily replaced after preserving it?
3. Which manufacturer-confirmed DDR topology/timings and actual UART connection qualify the first bounded smoke test?

## User Approval Boundary
User/manufacturer must provide missing actual facts and safe current-image ownership. Volatile tests are already conditionally authorized by the current instruction once gates are proven. No additional general permission is needed for read-only investigation or offline preparation. Permanent storage/boot changes and architecture/version changes remain outside scope.

## Codex Preliminary Assessment
PreferA, allowB only with explicit manufacturer evidence. This local assessment is not ChatGPT review. External source SonoField-FPGA is BLOCKED; no Decision file or independent approval fabricated.
