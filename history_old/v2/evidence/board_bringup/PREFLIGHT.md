# Engineering preflight / execution record

Project SONOFIELD_FPGA / SonoField-FPGA; repository https://github.com/loverlike1216/SonoField-FPGA.git.
Workspace E:\Codex_project\AMD-SonoField-FPGA; main; active/highest v2 ACTIVE; v1 FROZEN.
Starting local and fetched origin/main: 1784d7bc0481c3dd8b9b4b639918d43667cb1749.
Chat source SonoField-FPGA; Codex authorized ACTIVE; Work OFF.
PowerShell 7.6.5; Python 3.10.11; Vivado/hw_server 2025.2 available.
Preexisting untracked PCB/V1/project/SonoField-FPGA-v2-Schematic-V1-SingleSheet_backup/ preserved.

Read AGENTS, README, project/version/engineering states, plan, decisions, acceptance,
engineering blockers, chat/interaction indexes, open board problem and board constraints.
AI-work-memory/INDEX.md does not exist. External Chat history remains BLOCKED.
STATE_CONFLICT_DETECTED: general README/plan still name the schematic stage while prior
canonical engineering state records the motion stage. Latest direct user instruction
authorizes board-only identification. DOCUMENTATION_UPDATE_REQUIRED; Work remains OFF.
Open P-20260919-001/002/003 and P-20260925-001 remain; no matching new formal decision imported.
Prior evidence: evidence/engineering/motion/{regression,standalone,validation}; not rerun as hardware proof.
Board sources: 12 files in Zynq7020; full .const read and previous per-image audit reviewed;
annotated board image inspected again. No newly supplied schematic/manual/full chip marking.

## Current execution boundary (direct user instruction)

Read-only Windows USB/COM/network inventory, FTDI enumeration, Vivado target/JTAG identity,
alternative-tool capability checks, B01/B03 reassessment, engineering evidence/state and Git sync.
Follow-up authorizes evidence-based optimization of prior board configuration/code. Change
only identification scripts, part-validation guard and supporting tests/configuration.
No bitstream, download, driver installation/replacement, EEPROM programming, system reset,
boot/jumper changes, unknown GPIO, external load, PCB edit, PS firmware execution or v3.
Normal JTAG discovery is authorized; no system reset/program commands are issued.
Done when evidence is saved, uncertainties separated from facts, checks run, Git synced and probes stopped.
This is a Codex engineering result; independent Chat acceptance remains pending.

## Tool exceptions retained

- Initial inventory invocation used a wrong working-directory-relative path and did not run;
  corrected to ./collect_windows.ps1 before collecting evidence.
- Initial cable-only Vivado run had no local_raw directory and could not write its requested log;
  two subsequent full ID scans have preserved logs. Do not count the initial run as archived raw evidence.
- Robei openFPGALoader --version is unsupported; documented -V returned 0.13.1.
- Win32_SerialPort yielded no rows; PnP and .NET enumerate COM4. Absence in one provider is not no-port proof.
- Vivado .bat emits 'The system cannot find the path specified' before successfully starting
  Vivado 2025.2. Final identity output and normal exit are present; launcher noise is not suppressed.
