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
# Exact documented part required; physical revision is a separate gate.
if {![regexp {^xc7z020[a-z0-9]+-[123][a-z0-9]*$} $PART]} {
    error "BLOCKING: full documented xc7z020 package/speed part required; JTAG family alone is insufficient"
}
set resolved_parts [get_parts -quiet $PART]
if {[llength $resolved_parts] != 1 || [lindex $resolved_parts 0] ne $PART} {
    error "Unknown or non-exact documented FPGA part"
}
create_project sonofield_v5 [file join $root build vivado] -part $PART -force
foreach dir {rtl rtl/timing rtl/phase rtl/output rtl/control rtl/acquisition rtl/calibration rtl/motion} {
    foreach source_file [glob -nocomplain [file join $root $dir *.sv]] {add_files $source_file}
}
set_property include_dirs [list [file join $root rtl generated]] [current_fileset]
set_property top sono_axi_system [current_fileset]
set_property generic "CLOCK_HZ=$CORE_CLOCK_HZ" [current_fileset]
update_compile_order -fileset sources_1
# Out-of-context synthesis avoids pretending command ports are board GPIO.
synth_design -top sono_axi_system -part $PART -mode out_of_context -generic CLOCK_HZ=$CORE_CLOCK_HZ
read_xdc [file join $root hardware constraints core_ooc.xdc]
file mkdir [file join $root evidence synthesis]
report_utilization -file [file join $root evidence synthesis utilization.rpt]
report_timing_summary -file [file join $root evidence synthesis timing_synthesis.rpt]
report_cdc -details -file [file join $root evidence synthesis cdc.rpt]
write_checkpoint -force [file join $root build vivado synthesized.dcp]
set files_out [open [file join $root evidence synthesis loaded_sources.txt] w]
foreach src [get_files -of_objects [get_filesets sources_1]] {puts $files_out [file normalize $src]}
close $files_out
puts "V5_OOC_SYNTHESIS_COMPLETE; no board IO/PS/bitstream proof"
# Implementation and bitstream intentionally require a separate, reviewed board integration stage.
