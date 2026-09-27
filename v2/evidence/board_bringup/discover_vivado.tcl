# Cable enumeration only. Does not open a target or program/reset a device.
puts "TOOL_VERSION=[version -short]"
open_hw_manager
if {[catch {connect_hw_server -url localhost:3121} detail]} {
    puts "CONNECT_FAILED=$detail"
    close_hw_manager
    exit 2
}
set targets [get_hw_targets -quiet]
puts "TARGET_COUNT=[llength $targets]"
foreach target $targets {
    puts "TARGET=$target"
    report_property $target
}
disconnect_hw_server
close_hw_manager
exit
