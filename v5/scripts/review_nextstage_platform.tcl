# Read-only offline XPR/BD and routed DCP review. Never connects hardware.
if {![string match "2025.2*" [version -short]]} {error "Vivado2025.2 required"}
if {[llength $argv]!=3} {error "Expected XPR, routed DCP, fresh output"}
set xpr [file normalize [lindex $argv 0]]
set root [file normalize [file join [file dirname $xpr] .. ..]]
if {![file exists [file join $root config nextstage_source_list.txt]]} {error "XPR is not in a current v5 build tree"}
set dcp [file normalize [lindex $argv 1]]
set out [file normalize [lindex $argv 2]]
if {[file exists $out]} {error "Fresh review output required"}
file mkdir $out
open_project $xpr
open_bd_design [get_files prepcb_ps.bd]
validate_bd_design
set ps [get_bd_cells ps7]
if {[get_property CONFIG.PCW_UIPARAM_DDR_ENABLE $ps]!=0 || [get_property CONFIG.PCW_NUM_F2P_INTR_INPUTS $ps]!=5} {error "Unexpected platform configuration"}
set f [open [file join $out source_audit.tsv] w]
puts $f "path\tstatus"
foreach src [get_files -all] {
 set normalized [file normalize $src]
 if {![string match "$root/*" $normalized]} {error "Source outside current v5: $normalized"}
 puts $f "$normalized\tCURRENT_V5_ONLY"
}
close $f
set f [open [file join $out ps7_reopened_properties.txt] w]
puts $f [report_property -return_string $ps]
close $f
close_project
open_checkpoint $dcp
report_timing_summary -delay_type min_max -report_unconstrained -file [file join $out timing_reopened.rpt]
report_cdc -file [file join $out cdc_reopened.rpt]
set rule [get_drc_checks REQP-1839]
# Expand reporting, never waive/disable the rule. Default20 messages hide pins.
set_property MAX_MESSAGES 100000 $rule
set f [open [file join $out bram_rule_properties.txt] w]
puts $f [report_property -return_string $rule]
close $f
report_drc -file [file join $out drc_reopened.rpt]
set f [open [file join $out all_drc_violation_properties.txt] w]
foreach v [get_drc_violations] {puts $f [report_property -return_string $v]}
close $f
set f [open [file join $out scope.txt] w]
puts $f "STATUS=REOPENED_OFFLINE_ONLY"
puts $f "DRC_VIOLATIONS=[llength [get_drc_violations]]"
puts $f "C16_NAMED_CELLS=[llength [get_cells -hier -filter {NAME =~ *c16*}]]"
puts $f "PRODUCTION_IO_DELAYS=NOT_QUALIFIED"
puts $f "BOARD_TIMING=HOLD"
close $f
puts "NEXTSTAGE_REOPENED_CURRENT_V5_BOARD_RELEASE_HELD"
