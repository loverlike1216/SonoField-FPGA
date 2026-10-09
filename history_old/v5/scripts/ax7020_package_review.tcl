# Device database review only. No board access or deployment constraints.
create_project -in_memory -part xc7z020clg400-2
report_property [get_parts xc7z020clg400-2]
set stub [open v5/evidence/board_bringup/20261009/local_raw/package_review.v w]
puts $stub "module package_review(input wire a, output wire b); assign b=a; endmodule"
close $stub
read_verilog v5/evidence/board_bringup/20261009/local_raw/package_review.v
synth_design -rtl -top package_review -part xc7z020clg400-2
set out [open v5/evidence/board_bringup/20261009/package_pin_database.csv w]
puts $out "pin,bank,pin_func"
foreach pin {W19 W18 R14 P14 Y17 Y16 W15 V15 Y14 W14 P18 N17 U15 U14 P16 P15 U17 T16 V18 V17 T15 T14 V13 U13 W13 V12 U12 T12 T10 T11 A20 B19 B20 C20 F17 F16 F20 F19 G20 G19 H18 J18 L20 L19 M20 M19 K18 K17 J19 K19 H20 J20 L17 L16 M18 M17 D20 D19 E19 E18 G18 G17 H17 H16 G15 H15 J14 K14} {
 set obj [get_package_pins $pin]
 puts $out "$pin,[get_property BANK $obj],[get_property PIN_FUNC $obj]"
}
close $out
close_project
