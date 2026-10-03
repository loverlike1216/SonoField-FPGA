# Package database query only; does not establish PCB wiring or VCCO.
set root [file normalize [file join [file dirname [info script]] ..]]
set out [file join $root evidence pre_pcb_board_ready connector_reference]
file mkdir $out
create_project -in_memory -part xc7z020clg400-1
link_design -part xc7z020clg400-1
set f [open [file join $out package_pins.tsv] w]
puts $f "pin\tpin_func\tbank\tis_bonded\tis_general_purpose\tis_clk_capable"
foreach p [lsort [get_package_pins]] {
 puts $f "$p\t[get_property PIN_FUNC $p]\t[get_property BANK $p]\t[get_property IS_BONDED $p]\t[get_property IS_GENERAL_PURPOSE $p]\t[get_property IS_CLK_CAPABLE $p]"
}
close $f
close_project
exit
