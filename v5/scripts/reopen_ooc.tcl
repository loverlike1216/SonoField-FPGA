# Reopen the candidate's OOC project without hardware or programming operations.
if {[llength $argv] != 2} {error "Supply project.xpr and new report directory"}
set root [file normalize [file join [file dirname [info script]] ..]]
set project [file normalize [lindex $argv 0]]
set report [file normalize [lindex $argv 1]]
if {[string first "${root}/build/" $project] != 0} {error "Project must belong to this v5 build directory"}
if {[string first "${root}/evidence/" $report] != 0} {error "Reports must belong to this v5 evidence directory"}
if {![string match "*2025.2*" [version -short]]} {error "Vivado2025.2 required"}
open_project $project
update_compile_order -fileset sources_1
file mkdir $report
set output [open [file join $report loaded_sources_reopened.txt] w]
set count 0
foreach source [get_files -of_objects [get_filesets sources_1]] {
    set normalized [file normalize $source]
    if {[string first "${root}/rtl/" $normalized] != 0} {error "Foreign reopened source: $normalized"}
    puts $output $normalized
    incr count
}
close $output
puts "V5_OOC_REOPEN_PASS sources=$count part=[get_property PART [current_project]]"
close_project
