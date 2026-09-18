# Reproducible TARGET project. Configuration must come from verified board evidence.
# Usage: vivado -mode batch -source scripts/create_project.tcl -tclargs config/verified_board.tcl
if {[llength $argv] != 1 || ![file exists [lindex $argv 0]]} {
    error "BLOCKING: supply verified board Tcl with PART, PART_SOURCE, CORE_CLOCK_HZ and CLOCK_SOURCE; no guessed defaults"
}
set root [file normalize [file join [file dirname [info script]] ..]]
source [lindex $argv 0]
foreach required {PART PART_SOURCE CORE_CLOCK_HZ CLOCK_SOURCE} {
    if {![info exists $required] || [set $required] eq ""} { error "BLOCKING: missing $required" }
}
if {![string match "*2025.2*" [version -short]]} {error "Authoritative tool must be Vivado 2025.2"}
if {[llength [get_parts -quiet $PART]] != 1} {error "Unknown documented FPGA part"}
create_project sonofield_vn1 [file join $root build vivado] -part $PART -force
foreach dir {rtl rtl/timing rtl/phase rtl/output rtl/control} {
    foreach source_file [glob -nocomplain [file join $root $dir *.sv]] {add_files $source_file}
}
set_property top sono_top [current_fileset]
set_property generic "CLOCK_FREQ=$CORE_CLOCK_HZ" [current_fileset]
update_compile_order -fileset sources_1
# Out-of-context synthesis avoids pretending command ports are board GPIO.
synth_design -top sono_top -part $PART -mode out_of_context -generic CLOCK_FREQ=$CORE_CLOCK_HZ
create_clock -name core_clock -period [expr {1.0e9/$CORE_CLOCK_HZ}] [get_ports clk]
file mkdir [file join $root evidence synthesis]
report_utilization -file [file join $root evidence synthesis utilization.rpt]
report_timing_summary -file [file join $root evidence synthesis timing_synthesis.rpt]
write_checkpoint -force [file join $root build vivado synthesized.dcp]
# Implementation and bitstream intentionally require a separate, reviewed board integration stage.
