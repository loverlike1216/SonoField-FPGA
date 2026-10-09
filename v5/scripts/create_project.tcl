# Reproducible TARGET project. Configuration must come from verified board evidence.
# Usage: vivado -mode batch -source scripts/create_project.tcl -tclargs config/verified_board.tcl
if {[llength $argv] < 1 || [llength $argv] > 3 || ![file exists [lindex $argv 0]]} {
    error "BLOCKING: supply verified board Tcl with PART, PART_SOURCE, CORE_CLOCK_HZ and CLOCK_SOURCE; no guessed defaults"
}
set root [file normalize [file join [file dirname [info script]] ..]]
set configuration [file normalize [lindex $argv 0]]
# Temporary validation configurations also live in this clone's build scratch.
# This preserves the original negative part/provenance checks without loading
# any configuration from another workspace or from the frozen archive.
if {[string first "${root}/config/" $configuration] != 0 && [string first "${root}/build/" $configuration] != 0} {error "Configuration must belong to this v5 clone config or build scratch"}
set run_id [clock seconds]
set report_dir [file normalize [file join $root evidence migration manual_ooc_$run_id]]
set build_dir [file normalize [file join $root build vivado_$run_id]]
if {[llength $argv] >= 2} {set report_dir [file normalize [lindex $argv 1]]}
if {[llength $argv] >= 3} {set build_dir [file normalize [lindex $argv 2]]}
if {[string first "${root}/evidence/" $report_dir] != 0 || [string first "${root}/build/" $build_dir] != 0} {error "Keep all generated files in this v5 clone"}
if {[file exists $report_dir] || [file exists $build_dir]} {error "Use fresh OOC output and build directories; preserve old results"}
source $configuration
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
create_project sonofield_v5 $build_dir -part $PART
set source_list [open [file join $root config ooc_source_list.txt] r]
foreach rel [split [read $source_list] "\n"] {
    set rel [string trim $rel]
    if {$rel eq ""} {continue}
    set source_file [file normalize [file join $root $rel]]
    if {![string match "rtl/*.sv" $rel] || [string first "${root}/rtl/" $source_file] != 0 || ![file exists $source_file]} {error "Invalid v5 source: $rel"}
    add_files $source_file
}
close $source_list
set_property include_dirs [list [file join $root rtl generated]] [current_fileset]
set_property top sono_axi_system [current_fileset]
set_property generic "CLOCK_HZ=$CORE_CLOCK_HZ" [current_fileset]
update_compile_order -fileset sources_1
# Out-of-context synthesis avoids pretending command ports are board GPIO.
synth_design -top sono_axi_system -part $PART -mode out_of_context -generic CLOCK_HZ=$CORE_CLOCK_HZ
read_xdc [file join $root hardware constraints core_ooc.xdc]
file mkdir $report_dir
report_utilization -file [file join $report_dir utilization.rpt]
report_timing_summary -file [file join $report_dir timing_synthesis.rpt]
report_cdc -details -file [file join $report_dir cdc.rpt]
write_checkpoint -force [file join $build_dir synthesized.dcp]
set files_out [open [file join $report_dir loaded_sources.txt] w]
foreach src [get_files -of_objects [get_filesets sources_1]] {puts $files_out [file normalize $src]}
close $files_out
puts "V5_OOC_SYNTHESIS_COMPLETE; no board IO/PS/bitstream proof"
# Implementation and bitstream intentionally require a separate, reviewed board integration stage.
