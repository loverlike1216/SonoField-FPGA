# AX7020 v5 execution contract — 2026-10-09

Project SONOFIELD_FPGA; main; v5 unchanged; recording model GPT-6.1 Sol High (user-declared). User source: attachment 4b78522d-e640-448c-8788-c916d293b560.

Goal: identify the connected AX7020, qualify board configuration, preserve the digital baseline, revise a separate BOM working copy and prepare three-board schematics.

Scope: read-only Windows/Vivado/XSDB identification; manufacturer source/configuration extraction; isolated ADC/safety/interface candidates and verification; workbook corrections; normal GitHub sync. No fabricated ERC, physical measurement or independent reviewer result.

Invariants: 128 TX, 8 RX, 32 lanes/four used outputs, 8-bit coherent phase, independent requested/calibration phases, atomic commit, existing register/protocol/motion contracts. NU40C10T transmitter; RX MPN unresolved. 12 mm radiating-center pitch; 100 mm face gap adjustable 90–115 mm; center origin. Central/upper/lower required boards; remote environment optional. Each array has its own physical protected power input; AX7020 supplies no array power.

Do not change: frozen versions, user originals, validated core RTL or test thresholds. Do not create v6, program permanent storage, change drivers/boot switches or drive unknown GPIO.

Hardware gates: A reads only; B needs qualified part/clock/reset/safe IO; C additionally needs matched PS DDR/clock configuration and demonstrably unoccupied RAM; D follows real UART/AXI integration. User reports only power/JTAG connected. Photo shows SD position/card, and scan shows DONE=1 plus both CPUs Running. These are affirmative reasons to preserve the current image and not write unknown RAM. No unqualified B/C/D test will run.

Inputs: current repository/checkpoint/decisions/evidence; original 72-row submitted workbook and companion document; Revision 3.0 photos; pinned ALINX manual/schematic/XSA; primary component datasheets.

Validation: repeat full 115-test/3696-frame×4 baseline including Icarus/XSim/AXI/safety/equivalence; separate candidate checks; original source hashes; complete connector budget and package-pin database check; workbook recalculation/visual/error check. Synthesis/routing only required for actual PS/PL implementation changes; isolated reference candidates are not a deployed board platform.

Rollback: remove only this iteration's added candidates/working copy with normal reviewed Git revert; preserve raw failed evidence and originals. Done when all safely executable checks have outcomes, nine BOM findings have dispositions, current evidence/state are checkpointed and remote commit verified. Manufacturing/electrical freeze stays HOLD pending real hardware and independent review.
