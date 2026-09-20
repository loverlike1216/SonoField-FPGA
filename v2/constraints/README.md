# No board XDC yet

No PACKAGE_PIN or IOSTANDARD is assigned. See ../shared/BLOCKERS.md (relative to v2) B01-B03.
Simulation clocks are explicit mathematical test inputs, not a selected oscillator or PLL configuration.
The project script rejects unverified board configuration; never override DRC to generate a bitstream.
