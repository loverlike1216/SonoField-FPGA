# Inspect a real routed candidate checkpoint without suppressing inherited rules.
if {![string match "2025.2*" [version -short]]} {error "Vivado2025.2 required"}
if {[llength $argv] != 2} {error "Expected routed DCP and fresh review directory"}
set dcp [file normalize [lindex $argv 0]]
set out [file normalize [lindex $argv 1]]
if {[file exists $out]} {error "Fresh review directory required"}
file mkdir $out
open_checkpoint $dcp
set check [get_drc_checks REQP-1839]
set f [open [file join $out bram_rule_properties.txt] w]
puts $f [report_property -return_string $check]
close $f
help report_drc
report_drc -file [file join $out pl_routed_drc_reopened.rpt]
set f [open [file join $out actual_violation_properties.txt] w]
foreach violation [get_drc_violations] {
 puts $f [report_property -return_string $violation]
}
close $f
puts "PREPCB_DRC_REVIEW_COMPLETE_BOARD_RELEASE_STILL_HELD"
