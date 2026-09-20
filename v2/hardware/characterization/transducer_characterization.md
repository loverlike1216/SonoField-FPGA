# Ultrasonic transmitter characterization database — current 10 mm candidate

Current geometry uses the user's 10 mm transmitter image, not the former TCT40-16T electrical assumptions.
Record the actual manufacturer/part alongside batch/sample IDs. Capacitance and allowable drive are unknown;
do not fill them from a 16 mm product sheet. See hardware/transducers/10mm_supplier_reference.md.

Status: no purchased sample has been measured. `transducer_measurements.csv` contains headers only.
Never replace missing measurements with nominal datasheet values. Blank means unknown.

Required fields: CHANNEL_ID, batch, resonant_frequency_hz, capacitance_pf, relative_SPL_db,
phase_offset_deg, polarity, drive_voltage_vpp, temperature_c, remarks. Additional traceability includes
sample_id, instrument, receiver distance/angle, air temperature/RH, waveform, current, timestamp,
body diameter, pin spacing and height. Keep raw scope/CSV files referenced by evidence_path.

## Procedure

1. Assign a permanent sample/batch ID and intended channel ID. Measure body, pins and height with calipers.
2. Measure capacitance with stated meter frequency/voltage (e.g. 1 kHz small signal); measure baseline temperature.
3. Confirm a permissible excitation range for the actual 10 mm part, then use a current-limited single-channel
   driver with the transducer supported. The old 10 Vpp starting proposal is not a rating for this new part.
   Record differential Vpp, including overshoot.
4. Begin at the approved low excitation (10 Vpp only if qualified). Sweep around 40 kHz at low duty for resonance/relative SPL and phase. Record frequency step,
   settling time, geometry and receiver transfer-function limits. Resonance is measured, not assumed.
5. In fixed geometry, compare the sample to a reference transmitter using a TCT40-16R or suitable receiver and
   oscilloscope trigger. Correct for cable/receiver phase. Reverse sample connection as a check, mark effective
   polarity and store raw phase. Keep the electronic correction separately: correction = negative intrinsic error
   modulo 360 degrees in the documented phasor convention. Polarity reversal is 128 phase codes when appropriate.
6. Recheck repeatability without moving the receiver; then deliberately reseat the sample to quantify fixture sensitivity.
7. Progress 10 → 12 → 16 → approximately 20 Vpp only when waveform, supply current, driver/transducer
   temperature and acoustic behaviour remain acceptable. Observe over a recorded thermal dwell, not only a short burst.
8. Stop on new ringing/overshoot, clipping, unstable current, heating trend, odour or output degradation. Establish
   component-specific temperature/current limits from the purchased parts and prototype before continuous operation.
9. Any operation above the characterized range requires a written electrical decision and new measurements.

Relative receiver voltage is not calibrated absolute SPL. Never convert a TCT40-16R reading to pascals without
a receiver calibration. Keep measurement polarity, geometric propagation phase and driver delay distinguishable.
For each run store drive waveform/frequency, air conditions, device temperatures, supply voltage/current, captures
and measurement uncertainties. Recalibrate after replacing a transducer or driver module.
