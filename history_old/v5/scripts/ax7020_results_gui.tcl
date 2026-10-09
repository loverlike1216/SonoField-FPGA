# User requested a visible results page. Read-only Hardware Manager; leave it open.
open_hw_manager
connect_hw_server -url localhost:3121
set targets [get_hw_targets]
if {[llength $targets] != 1} {error "Select the correct target; no automatic ambiguous access"}
current_hw_target [lindex $targets 0]
open_hw_target
puts "===== SONOFIELD v5 AX7020 READ-ONLY RESULTS ====="
foreach dev [get_hw_devices] {
    puts "ACTUAL DEVICE: [get_property PART $dev], IDCODE: 0x[get_property IDCODE_HEX $dev]"
    if {[get_property PART $dev] eq "xc7z020"} {
        current_hw_device $dev
        refresh_hw_device -update_hw_probes false $dev
        puts "ACTUAL PL DONE: [get_property REGISTER.CONFIG_STATUS.BIT14_DONE_PIN $dev]"
    }
}
puts "XSDB read-only result: both Cortex-A9 cores Running; BOOT_MODE=0x5; DDRC_CTRL=0x81."
puts "USER/PHOTO: AX701020.3.0 / PCB Revision3.0; CLG400 marking; exact speed/temp grade not confirmed."
puts "NO BITSTREAM / CPU RESET / RAM WRITE / FLASH / SD WRITE PERFORMED."
puts "UART: no COM enumerated (user connected power/JTAG only). VCCO not physically measured."
puts "DIGITAL BASELINE PASS is simulation only. Native PCB ERC / board PS-PL loop NOT_RUN."
puts "Evidence: v5/evidence/board_bringup/20261009/RESULT.md"
puts "===== Preserve running image; electrical/manufacturing HOLD ====="
