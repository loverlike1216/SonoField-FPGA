# Native Vivado package database check only; no hardware manager or programming.
set input [lindex $argv 0]
set output [lindex $argv 1]
create_project -in_memory -part xc7z020clg400-2
link_design -part xc7z020clg400-2
set data [open $input r]
set report [open $output w]
puts $report "package_pin,bank,pin_function"
foreach pin [split [string trim [read $data]] "\n"] {
    set obj [get_package_pins [string trim $pin]]
    if {[llength $obj] != 1} {error "Invalid or ambiguous package pin $pin"}
    puts $report "$pin,[get_property BANK $obj],[get_property PIN_FUNC $obj]"
}
close $data
close $report
puts "HARDWARE_DESIGN_PACKAGE_REVIEW_PASS version=[version -short]"
exit
