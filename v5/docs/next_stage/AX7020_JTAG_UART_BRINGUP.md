# AX7020 read-only bring-up and STOP

After the actual user reseated JTAG, dedicated localhost3122 XSDB/Vivado2025.2 read-only identification PASS: xc7z020 ID0x23727093; both Cortex-A9 Running before/after; BOOT_MODE0x05, DDRC0x81/0x3e; PL DONE/EOS1, existing image identity UNKNOWN. Sysmon zero/-273.1 values INVALID, no voltage/temperature claim. Original Vivado GUI retained; owned server disconnected/stopped. CP2102N remains Code28/0COM. No halt/reset/init/download/memory/DDR-RAM/GPIO/driver/serial write. Real UART->PS->AXI->PL and A2 write gate remain STOP.

Current evidence: `../../evidence/next_stage/20261010/jtag_reseated/summary.json` and redacted logs. Previous `windows_readonly.json`/`usb_targeted_recheck.json`/`windows_readonly_after_continue.json` are valid earlier snapshots, now superseded for adapter availability. ID/DONE/EOS do not reveal package/grade or establish current SonoField image deployment.

No serial open, DTR/RTS toggle, driver installation, CPU halt/reset, ps7_init, FPGA programming, RAM download/write, Flash/SD/boot modification or unknown GPIO/power output occurred. S5 real UART->PS->AXI->PL100/1000 runs are NOT_RUN; the compiled C fixture's1000 PINGs are a software substitute only.

Minimum next physical step: user restores a correctly installed official CP2102N VCP driver and confirms a COM device; JTAG adapter/cable is now identified as Digilent JTAG-HS1 with FTDI driverOK. Driver installation is a system change, not included in read-only authorization. Repeat OS enumeration first. Confirm board revision AX701020.3.0, full FPGA grade, header VCCO, PS clock/UART/DDR configuration, current SD image owner and which safe program is running. Generic AX7020_2023.1 documentation is a candidate, not proof for this Rev3.

Only after A2's facts, physically disabled driver rails/isolated expansion outputs, known recovery image, explicit reset/download/volatile-write authorization and a reviewable smoke image exist may a bounded test open UART or modify board state. Start with outputs disabled, handshake/read-only identity and100 iterations; scale to1000 only after stable results. Save raw packets, CRC/replay/disconnect cases, source commit, latency percentiles and board-state restoration. Otherwise STOP board writes while continuing offline gates.

Native Vitis2025.2 preflight returned shell exit0 but its log contains failure and missing BSP/XSA/ARM-GCC context; it is BLOCKED, never TARGET_APPLICATION_BUILD_PASS. AMD Clang16 successfully emits a Cortex-A9 ARMv7 ELF relocatable object for the portable C-16/TMP117 adapter. That is a real target object, not a BSP-linked executable or a program running on PS.

References: [Microsoft Code28](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/cm-prob-failed-install), [official Silicon Labs VCP](https://www.silabs.com/software-and-tools/usb-to-uart-bridge-vcp-drivers), [ALINX reference](https://github.com/alinxalinx/AX7020_2023.1).
