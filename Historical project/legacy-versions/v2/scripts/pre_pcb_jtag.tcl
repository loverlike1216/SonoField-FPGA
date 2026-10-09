# Read-only Hardware Manager scan. No programming, processor reset or MMIO.
if {[version -short] ne "2025.2"} {error "Vivado 2025.2 required"}
open_hw_manager
connect_hw_server -url localhost:3121
set targets [get_hw_targets -quiet]
puts "PREFLIGHT_TARGET_COUNT=[llength $targets]"
if {[llength $targets] != 1} {error "Automatic identification requires exactly one cable; do not guess a board"}
set target [lindex $targets 0]
current_hw_target $target
open_hw_target $target
puts "PREFLIGHT_TARGET=$target"
foreach device [get_hw_devices -quiet] {
 puts "PREFLIGHT_DEVICE=$device"
 report_property -all $device
}
report_property -all $target
close_hw_target
disconnect_hw_server
close_hw_manager
exit
