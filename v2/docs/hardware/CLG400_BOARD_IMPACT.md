# CLG400 engineering impact — v2

User photo confirms XC7Z020 and CLG400. Speed/temperature/full ordering code remain UNKNOWN. Candidate part enumeration cannot close B01. No PCB file or production XDC was changed.

Vivado 2025.2 package database has 400 balls and 125 PL user IO: Bank13=25, Bank34=50, Bank35=50. Bank33 is not bonded. AMD UG865 page22 confirms this restriction, partial Bank13 and bonded PS banks. PS bank pins are not interchangeable with PL GPIO.

Complete audit: [CLG400 pin audit](../../evidence/board_transport/CLG400_PIN_AUDIT.md), with 101 primary constraint entries and 346 total source claims. All connector numbers were compared; no conflicting value was chosen arbitrarily. hardware.const precedence remains a source preference, not proof of package legality or physical routing.

A material conflict is HDMI CEC=J5: CLG400 J5 is PS_DDR_BA2_502, not PL. Another picture names J15 (IO_25_35). Do not substitute it without board evidence. J3/J4 numbering, J4 pin1, duplicate J4 pin6 D18/E18, J6 V16, and Y16/V16 discrepancies remain open. No Bank33-based expansion is permitted; Bank13 must be checked ball by ball.

Array connector plans, serializer lanes and ADC returns must use the audited PL subset and independently verified connector routing/VCCO. This does not provide 128 direct GPIO outputs; serialized expansion remains planned. N18 is a bonded Bank34 MRCC, but its electrical standard and actual clock waveform are not verified. ADC/serializer IO standards, bank voltages, trace delay and level compatibility remain B03/B04 gates. COM4 enumeration does not establish PS MIO routing.

[AMD UG865 official source](https://docs.amd.com/v/u/en-US/ug865-Zynq-7000-Pkg-Pinout). This is the task-authorized technical impact record; it does not approve PCB manufacture or a hardware target.
