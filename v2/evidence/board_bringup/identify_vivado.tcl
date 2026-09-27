# Read-only JTAG discovery: no programming, PS reset, register writes or GPIO.
puts "TOOL_VERSION=[version -short]"
open_hw_manager
connect_hw_server -url localhost:3121
if {[llength $argv] != 1} { error "Supply exact target URL from discover_vivado.tcl; no automatic board selection" }
set targets {}
foreach candidate [get_hw_targets -quiet] {
    if {$candidate eq [lindex $argv 0]} { lappend targets $candidate }
}
if {[llength $targets] != 1} { error "Expected exactly the observed FTDI A target" }
set target [lindex $targets 0]
current_hw_target $target
open_hw_target $target
puts "IDENTIFICATION_DEVICE_COUNT=[llength [get_hw_devices -quiet]]"
foreach device [get_hw_devices -quiet] {
    puts "IDENTIFIED_DEVICE=$device"
    report_property -all $device
}
report_property -all $target
close_hw_target $target
disconnect_hw_server
close_hw_manager
exit
