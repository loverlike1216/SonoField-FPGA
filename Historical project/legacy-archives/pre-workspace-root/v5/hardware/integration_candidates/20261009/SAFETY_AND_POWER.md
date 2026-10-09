# Independent array power and shutdown candidate

Status: functional candidate, **electrical freeze HOLD**. Model: GPT-6.1 Sol High, user-declared. Three required boards; no fourth mandatory environment board.

## Power tree

For each side S=UP/DN:

```
S_PWR_IN / S_PWR_GND (physical XT30, independent branch)
  -> branch fuse -> surge network [UNQUALIFIED, SMBJ20A not released]
  -> primary TPS259470L eFuse -> S_VPROT
       -> AP63203 -> S_3V3 (logic, watchdog, safety, monitoring)
       -> AP63200 candidate5.52V -> ADP7118 fixed5V -> S_5V_AFE
       -> additional normally-OFF TX eFuse/load-cut candidate -> S_VDRV ->32 TC4427A ->64TX
```

Central AUX_PWR_IN has its own protected branch and3.3V/5V_ADC conversion. AX7020 uses its own official5V supply. AX7020 J10/J11 power contacts remain NC on the adapter; their GND contacts provide signal references. Independent physical ports are not galvanic isolation. Use source-end star power returns, continuous signal reference and intentional shield termination; signal/analog cable grounds must not become array load returns.

The extra TX switch is a proposed two-part addition, not included in the original three primary eFuses. Local safety must remain powered while TX is cut; putting its only supply after the same enable-controlled switch creates a startup deadlock. Primary branch qualification and TX enable are separate. Additional device cost/board space is pending design review; nothing is purchased.

## Gate-level functional candidate

TC4427A has no EN.595 OE_N makes outputs high impedance, and SRCLR_N clears only the shift stage. Use local OE pullup, local RESET_N pulldown, DATA/driver-input defined pulldowns and translator Ioff/OE qualification. A10kohm driver-input pulldown candidate reduces sensitivity to leakage relative to100kohm; check worst-case input leakage, VOL and added static load for the selected parts. Each of128 driver inputs needs its own bias. Do not infer a disconnected wire is a solid logic level without that bias.

Use local supervisors/window monitors (TPS3808/TPS3700 candidates), TPS3430 external watchdog (never strap WDO to healthy), hardwired normally-closed E-stop and local primary eFuse FLT_N. Exact suffixes, resistor thresholds, watchdog window, power-on delays, supervisor polarity and oscillator tolerance remain to be frozen. TPS259470L provides **FLT_N, not PGOOD**; use separate qualified rail sensing. TMP117/INA226 software readings do not replace hardware shutdown.

The READY/ARMED/TX_SEEN latch candidate can use SN74LVC1G74 with SN74LVC1G08/1G11 AND,1G32 OR and1G04 inversion gates. Functional equations:

```
H = qualified local rails AND watchdog_ok AND estop_ok AND local_fault_clear
REQUEST = NOT(OE_N_from_FPGA)               // cable float -> local pullup ->REQUEST=0
READY.D = READY.Q OR NOT(RESET_N)           // CLK=buffered RCLK, /CLR=H
ARMED.D = READY.Q                           // CLK=new REQUEST rising edge
ARMED./CLR = H AND (NOT(TX_SEEN.Q) OR TX_PGOOD)
TX_SEEN.D = 1                               // CLK=TX_PGOOD rising; /CLR=H AND REQUEST
TX_SWITCH_EN = H AND REQUEST AND ARMED.Q
LOCAL_595_OE_N = NOT(TX_SWITCH_EN AND READY.Q AND TX_PGOOD AND SETTLED)
```

Preset inputs are inactive. Power-on supervisor must hold clears until valid supply. READY is acquired only by an actual RCLK with the shift clear asserted; OE remains disabled during initialization. A new REQUEST edge is required after a fault; held-high request cannot rearm. TX_SEEN prevents automatic restart after a previously valid TX rail drops. REQUEST is not tied to ARMED asynchronous clear, avoiding a direct CLK/clear recovery conflict. Array boards have separate copies of all latches/watchdogs/power switches.

These equations are an explicit gate candidate, **not a completed pin-level/electrical schematic**. Validate asynchronous clear recovery/removal, gate hazards, RCLK glitches, qualified TX_PGOOD rising edge, SETTLED implementation, reset pulse width and first enable pulse on physical parts. The logical model abstracts those analog events. The proposed gates and additional power switch require independent review and a driver prototype before claiming fail-safe hardware.

## Fault matrix and limits

| Event | Functional result | Physical evidence |
|---|---|---|
| Only AX7020 powered / only one array powered | Unqualified side OFF | NOT_RUN |
| FPGA not configured / complete control cable removed | Local bias removes REQUEST; watchdog expires; OFF | NOT_RUN |
| Watchdog/estop/primary power fault | Async clear, OE disabled and TX switch OFF | NOT_RUN |
| TX power lost after valid run | ARMED cleared, no automatic restart | NOT_RUN |
| Healthy supply restored while request remains asserted | Remains OFF, new initialization/enable edge needed | NOT_RUN |
| Upper-only fault | Upper OFF; lower behavior independently qualified | NOT_RUN |
| A single DATA conductor opens while heartbeat remains | **Not detected by this architecture**; requires cable/continuity test or approved integrity feedback | NOT_RUN |
| Logic rail collapses while driver rail remains | Bias/power cutoff candidate; driver behavior below operating supply/glitches unresolved | NOT_RUN |

candidate_checks.json contains1024 qualified-input state combinations, fault/rearm cases and independent-side assertions. safety_fault_matrix.json records uncovered effects. These are functional simulation, not measured shutdown latency or a safety certification. Output capacitance can retain energy after a switch opens; discharge, brownout TC4427A behavior and restart must be observed with the oscilloscope.

## Calculations and unresolved protection

TPS25947 ILIM approximately3334/RILIM gives2.02A with1.65kohm, not5.5A. Tolerance/thermal/startup coordination with2A slow fuse and extra TX switch remain open. INA226±81.92mV/20mohm gives±4.096A measured full-scale; shunt loss at2A is0.08W. It would saturate before5.5A if the limit were raised. Retain three current sensors and three local temperature sensors, one per power/thermal board.

ADP7118 is200mA maximum. AP63200 feedback590kohm/100kohm with0.8V reference gives5.52V nominal. Against420mV maximum dropout at200mA, nominal spare headroom is100mV before buck tolerance, ripple, wire drop and LDO accuracy. ADC C-16 AVCC max50mA at1MSPS suggests the ADC alone fits; it does not close total central/array rail budgets. Model ADC LDO nominal loss≈26mW; array AFE/logic loads and junction temperature need complete device/load/stackup data. Do not equate200mA rating with usable thermal headroom in every package.

power_sweep.csv explicitly assumes C=1/2/3nF and V=5/10/12/16V,40kHz,64 outputs. For an ideal single-ended capacitive load I≈NCVf and P≈NCV²f. Example2nF/12V gives61.44mA/0.73728W capacitive charging per array. This excludes motional resonance, quiescent/short-circuit driver losses, ringing, logic/AFE/buck losses and inrush; it is neither a minimum/maximum real board budget nor a NU40C10T capacitance measurement. Actual peak current depends on edge time and driver impedance. No safe supply/fuse/copper/thermal rating is frozen from it.

SMBJ20A32.4V rated clamping exceeds TPS25947 absolute28V. TC4427A recommended supply ends18V; even a candidate TVS below28V does not automatically protect it. Required: actual source surge waveform/impedance/current, TVS dynamic clamp, trace inductance, response, OVLO tolerances and output overshoot. A lower-VRWM TVS, series impedance or surge stopper can be compared after those conditions are specified; no arbitrary replacement or OVLO divider is declared safe. B-0631.37Mohm upper resistor alone is not a protection design.

References: [TPS25947](https://www.ti.com/lit/ds/symlink/tps25947.pdf), [SMBJ20A manufacturer clamp specification](https://www.diodes.com/part/view/SMBJ20A), [INA226](https://www.ti.com/lit/ds/symlink/ina226.pdf), [ADP7118](https://www.analog.com/media/en/technical-documentation/data-sheets/ADP7118.pdf), [TC4427A](https://www.microchip.com/en-us/product/TC4427A), [AP63200 family](https://www.diodes.com/assets/Datasheets/AP63200-AP63201-AP63203-AP63205.pdf). Physical load, temperature, surge and IO backfeed tests: NOT_RUN.
