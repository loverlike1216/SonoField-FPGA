# AX7020 documented hardware facts

Manufacturer source: [ALINX AX7020 repository](https://github.com/alinxalinx/AX7020_2023.1/tree/fcf1e4a239b0f47e8ee95dfde7c2eedc5685c327), pinned commit; [manufacturer manual](https://ax7020-20231-v101.readthedocs.io/zh-cn/latest/AX7020UserManual_CN/AX7020UserManual.html). Downloaded schematic/manual hashes are in sources.json; raw third-party documents remain local only.

Documented: XC7Z020-2CLG400I; PL50MHz U18; PS33.333MHz E7; two4Gb x16 DDR3 devices,1GiB/32bit. Official schematic PDF pages4/5/6/8 show PS clock/MIO,DDR pins,PL clock and twoH5TQ4G63AFR-PBC devices. These are manufacturer specifications, not physical measurements. No current board/revision/JTAG/DDR/UART runtime test occurred.

Material includes generic Zynq7010/7020 symbols and nonuniform file-name/title-block revision text; match the actual board revision before deployment. Old D9PSK/512MiB information does not apply. Transport profile has no old COM number. PS export/BSP qualification and pin allocation remain future work.
