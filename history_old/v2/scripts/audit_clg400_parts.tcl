# Diagnostic only: enumerating candidates does not identify the physical speed grade.
set root [file normalize [file join [file dirname [info script]] ..]]
set out [file join $root evidence board_transport]
file mkdir $out
if {[version -short] ne "2025.2"} {error "Vivado 2025.2 required"}
set parts [lsort [get_parts -quiet -filter {DEVICE == xc7z020 && PACKAGE == clg400}]]
if {![llength $parts]} {error "No installed XC7Z020 CLG400 candidates"}
set f [open [file join $out clg400_parts.tsv] w]
puts $f "part\tdevice\tpackage\tspeed"
foreach p $parts {
    puts $f "$p\t[get_property DEVICE $p]\t[get_property PACKAGE $p]\t[get_property SPEED $p]"
}
close $f
puts "CANDIDATE_ANALYSIS_ONLY parts=$parts"
create_project -in_memory -part [lindex $parts 0]
link_design -part [lindex $parts 0]
report_property -all [get_package_pins N18]
set f [open [file join $out clg400_package_pins.tsv] w]
puts $f "pin\tpin_func\tbank\tis_bonded\tis_general_purpose\tis_clk_capable"
foreach p [lsort [get_package_pins]] {
    puts $f "$p\t[get_property PIN_FUNC $p]\t[get_property BANK $p]\t[get_property IS_BONDED $p]\t[get_property IS_GENERAL_PURPOSE $p]\t[get_property IS_CLK_CAPABLE $p]"
}
close $f
close_project
exit
