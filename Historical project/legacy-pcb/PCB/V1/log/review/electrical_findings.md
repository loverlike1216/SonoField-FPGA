# Electrical findings requiring explicit disposition

These are Codex engineering findings from primary sources, not ChatGPT decisions.

1. **ADP7118ACPZN5.0-R7 package correction**: ADI Rev H p6 specifies six LFCSP
   signal pins and an exposed ground pad. The native library has 1 VOUT, 2 SENSE,
   3 GND, 4 EN, 5 SS, 6 VIN and pad 7 EP. The imported BOM's LFCSP-8 text is wrong.
   Keep the MPN; use its six-lead variant, connect EP to ground, do not ground SS.
2. **TPS259470L variant**: TI SLVSFC9C pp4–6 defines pin3 AUXOFF and pin4 /FLT.
   Generic library aliases PG/AUXOFF and FLT/PGTH must not lead to a wrong circuit.
   AUXOFF is not treated as a complete 3V3/5VA/VDRV power-good supervisor.
3. **SHT45 extra pad**: the native symbol includes pin5. Sensirion SHT4x v7.3
   pp16–17 says the central die pad is not directly connected to a pin and should
   not be soldered. Leave the symbol's pad5 explicitly unconnected; do not ground it.
4. **Serializer hold margin remains open**: at 132 MHz core the next data change
   is 7.576 ns after an ideal shift rising edge. A clock-only LVC244 delay reduces
   hold margin. TI LVC244A max delay is 5.9 ns (-40..85 C), 7.2 ns (-40..125 C),
   at 3.3 V +/-0.3 V. LVC595A requires 1.5 ns hold. Even with identical translator
   paths and zero trace skew, those bounds leave only 0.176 ns or -1.124 ns.
   Translator differential delay, FPGA IO skew and cable delay are still unknown.
   This is a failed worst-case closure argument, not evidence of measured failure.
   Do not change RTL frequency or claim B04 closed without an approved solution.
5. **RX blanking is downstream**: TMUX1574 protects the ADC measurement window,
   not the preceding amplifier from acoustic/electrical overload. PH0 recovery
   measurements and input protection remain necessary.
6. **Clock-loss safety**: output-disable pulls cover reset/disconnection; they do
   not prove immediate shutdown for a stopped, configured FPGA or latched software
   enable. Independent watchdog/power qualification requires a reviewed design.
   Never waive this by interpreting a static driver level as a verified OFF state.
7. **Transducer provenance**: user-supplied TCT40-10T/R1 baseline is design input.
   The exact manufacturer's original datasheet has not been retrieved. No measured
   resonance, capacitance, polarity, continuous voltage or acoustic force is claimed.
