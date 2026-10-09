# AX7020 documented hardware facts

Manufacturer source: [ALINX AX7020 repository](https://github.com/alinxalinx/AX7020_2023.1/tree/fcf1e4a239b0f47e8ee95dfde7c2eedc5685c327), pinned commit; [manufacturer manual](https://ax7020-20231-v101.readthedocs.io/zh-cn/latest/AX7020UserManual_CN/AX7020UserManual.html). Downloaded schematic/manual hashes are in sources.json; raw third-party documents remain local only.

Documented: XC7Z020-2CLG400I; PL50MHz U18; PS33.333MHz E7; two4Gb x16 DDR3 devices,1GiB/32bit. Official schematic PDF pages4/5/6/8 show PS clock/MIO,DDR pins,PL clock and twoH5TQ4G63AFR-PBC devices. These are manufacturer specifications, not physical measurements.

2026-10-09 actual evidence: user photos confirm AX701020.3.0 / Revision3.0 and CLG400; Vivado JTAG identifies XC7Z020 ID0x23727093 via Digilent JTAG-HS1, FTDI VID0403/PID6014. Existing PL DONE and both CPUs Running/SD boot were preserved. Read-only DDRC_CTRL0x81 shows configured32bit, not physical capacity or stable memory. No COM enumerated with power/JTAG only. Complete speed/temp grade and actual VCCO remain UNKNOWN. See [current results](../../evidence/board_bringup/20261009/RESULT.md).

Public schematicV2.0 is not revision-matched to actualRev3.0. Pinned helloXSA selects MicronMT41J256M16 RE-125 rather than the manual Hynix model; timing equivalence is unconfirmed. No vendor initialization was executed. Reference FCLK0=50MHz does not replace132MHz core target. Real DDR RAM/UART/PS-PL tests NOT_RUN; full PS platform qualification remains open.

Material includes generic Zynq7010/7020 symbols and nonuniform file-name/title-block revision text; match the actual board revision before deployment. Old D9PSK/512MiB information does not apply. Transport profile has no old COM number. PS export/BSP qualification and pin allocation remain future work.


The copied rtl/timing/board_clock_candidate.sv is an inherited, unused33.333MHz reference example, not the AX7020 PL50MHz clock implementation. The current sono_axi_system OOC top takes its internal clock as an input and does not instantiate that MMCM. Native project reload verification checks no MMCME2_BASE cell exists. Do not use the legacy candidate when integrating AX7020; a revision-matched PS/FCLK or50MHz clock-conversion design requires the next board integration contract. The separate rtl/board/sono_board_smoke_pl.sv is verified by offline simulation, not selected as the current synthesis top. Native source membership is explicit18files; all19currentRTLfiles are included in the offline simulator regressions.

Native reload first failed an arbitrary minimum20-file assertion in the new audit helper. Replaced with exact expected source-path set equality and the unused-MMCM check; the original failed native log is retained. Installed board-store warnings concern unavailable unrelated device families; no board preset was selected or claimed qualified.
