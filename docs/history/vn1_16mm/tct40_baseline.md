# TCT40 baseline and limits

Chosen family: TCT40-16T, nominal 40 kHz open-air transmitter, approximately 16 mm diameter, nF-class load.
Purchased batch identity and all actual ratings are unknown. It is not a calibrated omnidirectional source.

The component document hosted by SparkFun lists 40 kHz, transmitter frequency tolerance ±0.5 kHz,
117 dB minimum and 2500 pF ±30% measured at 1 kHz below 1 V. It also lists an ambiguous 80 V maximum
without enough information here to qualify continuous levitation drive. These are reference claims, not
batch acceptance measurements or permission to use 80 V.
[Reference component document](https://docs.sparkfun.com/SparkFun_Ultrasonic_Distance_Sensor-Qwiic/assets/component_documentation/TCT40-16-T-R.pdf).

The user's 2 nF / 110–117 dB class baseline is retained as an assumption range; do not conflate vendors,
distance, waveform, RMS/Vpp, duty cycle or SPL test conditions. Initial differential drive steps are
10,12,16,~20 Vpp conditional on measurements. A symmetric full bridge on a 5 V supply can ideally produce
10 Vpp across its load; supply voltage and transducer Vpp are not interchangeable. Overshoot counts.

At 343 m/s, wavelength is 8.575 mm. A provisional 18 mm pitch is about 2.10 wavelengths, not lambda/2.
Use opposed standing waves and geometric focusing; large-angle grating-lobe-free steering is not a VN1 claim.
The capacitance is only one part of the resonant electromechanical impedance. Sinusoidal reactive-current
estimates cannot establish square-wave switching current, loss or safe bridge component values.

Characterization and conservative bring-up procedures: hardware/characterization/transducer_characterization.md.
