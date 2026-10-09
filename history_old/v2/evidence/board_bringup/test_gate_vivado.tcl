# Offline authoritative-tool rejection tests. No hardware manager or project.
set here [file dirname [file normalize [info script]]]
set script [file normalize [file join $here ../../scripts/create_project.tcl]]
file mkdir [file join $here local_raw]
foreach {candidate expected} {
    xc7z020 {full documented}
    xc7z010clg400-1 {full documented}
    xc7z020clg400-* {full documented}
    xc7z020unknown-1 {Unknown or non-exact}
} {
    set config [file join $here local_raw invalid_test_fixture.tcl]
    set f [open $config w]
    puts $f [list set PART $candidate]
    puts $f {set PART_SOURCE {negative test fixture, not board facts}}
    puts $f {set CORE_CLOCK_HZ 132000000}
    puts $f {set CLOCK_SOURCE {negative test fixture}}
    close $f
    set argv [list $config]
    set code [catch {source $script} result]
    if {$code != 1 || [string first $expected $result] < 0} {
        error "FAIL: $candidate unexpected outcome: $result"
    }
    puts "PASS REJECT $candidate : $result"
}
puts "PASS VIVADO_BOARD_GATE 4 cases; no project created"
exit
