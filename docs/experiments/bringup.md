# Physical bring-up and evidence gates

All stages below are NOT VALIDATED. Digital tests do not count as hardware evidence.

| Stage | Required experiment | Evidence / exit gate |
|---|---|---|
| PH0 | Single TCT40 characterization and driver electrical checks | Batch, frequency response, polarity, differential Vpp/current/temperature, scope captures |
| PH1 / P0 | Two opposed emitters on adjustable fixture | Relative phase, centerline pressure scan, gap and alignment sweep |
| PH2 | Initial stable lightweight EPS particle | Measured mass/dimensions, duration, voltage/current, photo/video and environment |
| PH3 / P1 | 4x4 upper + 4x4 lower | All 32 calibrated identities, stable light-particle trap and replacement/recalibration procedure |
| PH4 / P2 | 6x6 + 6x6 | 72-channel geometry and phase validation; demonstration reliability |
| PH5 | Approximately 5,10,25,50 mg, sequentially | Separate weighed objects; dimensions/density; failed trials retained |
| PH6 | Vertical node translation | Measured displacement trajectory, phase command log, retained trapping |
| PH7 | Small-range XY motion | Measured displacement, stability and failure envelope |
| PH8 / P3 | Optional 8x8 + 8x8 | Only when measured force/control limitation justifies 128 emitters |

Before PH0, verify oscillator/part/VCCO and interlock wiring; scope two digital channels with drivers unpowered.
Verify 0/90/180 degrees, reset, hardware inhibit and a phase commit with the physical serializer output.
Then power only one current-limited driver channel. Measure differential waveform, overshoot, ringing,
current and thermal drift. Initial voltage escalation follows the characterization document; never jump to a vendor maximum.

P0 spacing is an adjustable experimental variable; wavelength/2 node spacing is a starting physical expectation,
not a guaranteed optimum fixture gap. Confirm emitter acoustic polarity at a fixed receiver location first.
Scan pressure along the axis with consistent probe geometry. Try a tiny measured EPS object before 5 mg.
Keep airflow, hands, nearby reflectors and acoustic exposure controlled. Use a power-off setup procedure and
avoid handling live switching connections. No exposure level is certified by this simulation.

Every milestone records timestamp, board/driver revision, sample and channel IDs, calibration revision,
object mass/scale uncertainty, diameter/shape, derived density, array coordinates/normals, air temperature/RH,
frequency, drive Vpp, supply current, driver/transducer temperatures, scope files and photo/video.
Use headers in hardware/characterization/; do not populate measured fields with model values.

After 2–3 unsuccessful attempts with unchanged configuration: stop changing counts/voltage. Collect evidence,
compare baseline, check resonance/polarity/phase/gap/alignment/consistency/loading/driver clipping/airflow and
particle dimensions/density. Record cause, alternatives and recommendation in shared/HANDOFF.md.
Only increase emitters or voltage after acoustic strength is identified as the likely limiting factor.
