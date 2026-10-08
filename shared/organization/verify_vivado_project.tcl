# Read-only project/checkpoint reload; no implementation or board access.
if {[llength $argv] != 1} {error {Supply current v5 root}}
set v5 [file normalize [lindex $argv 0]]
if {![string match *2025.2* [version -short]]} {error {Vivado2025.2 required}}
open_project [file join $v5 build vivado sonofield_v5.xpr]
if {[get_property PART [current_project]] ne {xc7z020clg400-2}} {error {Unexpected documented-device target}}
if {[get_property TOP [get_filesets sources_1]] ne {sono_axi_system}} {error {Unexpected top}}
set sources [get_files -of_objects [get_filesets sources_1]]
set n 0
foreach src $sources {
    set p [file normalize $src]
    if {![string match "${v5}/rtl/*" $p] || ![file exists $p]} {error "Foreign/missing source: $p"}
    incr n
}
if {$n < 20} {error {Incomplete RTL source list}}
open_checkpoint [file join $v5 build vivado synthesized.dcp]
set clk [get_clocks core_clock]
if {[llength $clk] != 1} {error {Missing OOC internal clock}}
set period [get_property PERIOD $clk]
if {abs($period-7.575758) > 0.001} {error {Unexpected core clock}}
set constraints [file join $v5 hardware constraints core_ooc.xdc]
set f [open $constraints r];set xdc [read $f];close $f
foreach line [split $xdc "\n"] {
    if {[string match {#*} [string trim $line]]} {continue}
    if {[regexp {PACKAGE_PIN|IOSTANDARD|set_false_path} $line]} {error {Unexpected physical constraints or waiver}}
}
puts "V5_NATIVE_PROJECT_REOPEN_PASS source_files=$n internal_period_ns=$period"
puts {Scope: project/source/internal synthesis checkpoint only. No physical board pins/PS/route/bitstream proof.}
close_project
