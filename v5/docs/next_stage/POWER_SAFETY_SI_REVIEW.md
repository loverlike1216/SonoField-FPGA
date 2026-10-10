# Power, cutoff and signal integrity review

| Domain | Normal source / topology | Evidence required / current status |
|---|---|---|
| Upper / Lower | Each independent external12V, protected polarity/TVS/fuse/eFuse, actual rail cutoff, local logic regulator |5A source label is not usable2A eFuse capacity. Ratings, wire/inrush/current-limit selectivity, connector temperature and losses HOLD. |
| Central | AX7020J10/J11 only, one protected source per rail; never parallel headers or backfeed | Rev3 header source capacity unknown; maximum/startup/fault current per load and drop measurements missing. CENTRAL_POWER_BUDGET_BLOCKED. |
| ADC | AVCC4.75..5.25V filtered, VDRIVE3V3 candidate, separate regulator/reference caps | Datasheet50mA AVCC max1MSPS is a component envelope, not entire central budget. VDRIVE/reference/AFE/regulator/startup missing. |
| RXAFE |8 channels protection, blank/bias, gain/filter/reference candidate |40kHz gain/phase/SNR35dB acceptance, alias attenuation and saturation/recovery measurements missing. |
| Safety | NC estop+localwatchdog+thermalcomparator+PGOOD+coldstartrearm -> physicalcutoff and failclosedOE | PL tests are SIMULATED_ONLY. Clock stop, cable/unpowered logic/power loss, fault/rearm are not physically verified. |
| Serializer |32lanes x4used,66MHz candidate, translated and buffered | Rev3VCCO, exact IO/minmaxdelay, connector/cable/fanout/skew/ringing, externalsetup/hold unqualified. OOC timing does not close these. |

`POWER_SENSITIVITY.json` sweeps1/4/16/64 channels,1.76/2.2/2.64nF,6/12V swing at40kHz.64*2.2nF*12^2*40kHz=0.811008W is ideal CV²f charging sensitivity only. It excludes piezo resonance/dissipation/driver losses and is neither measured power nor an upper bound. Do not freeze copper/current rating from it. Populate per-rail steady/startup/peak/fault budget using measured waveforms and original ratings before release.

Inherited SMBJ20A TVS clamping cannot be assumed below the candidate <=23V eFuse absolute limit. Candidate fuse2A and source5A need coordinated fault/inrush review. GPIO OE-high/high-Z does not remove driver power. Unknown components/thresholds remain PART_SELECTION_HOLD with owner independent electrical reviewer/user; no false PASS/ERC/bench result.
