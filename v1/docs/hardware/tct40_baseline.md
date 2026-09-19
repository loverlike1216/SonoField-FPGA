# Current transmitter baseline — nominal 10 mm / 40 kHz

The user selected a 10 mm transmitter from a supplied shop image on 2026-09-19. Project identifier:
`TCT40_10MM_CANDIDATE`. Exact manufacturer and part number are unknown; do not call it TCT40-16T.

| Parameter | Current treatment |
|---|---|
| Nominal body diameter / frequency | 10 mm / 40 kHz, user-selected supplier claims |
| Array / pitch | Opposed planar 8x8 + 8x8, 12 mm radiating-center pitch |
| Face gap | Nominal 100 mm, adjustable 90..115 mm, origin centered |
| Body height / pin spacing | Image says 7 mm / 5 mm; measure before footprint selection |
| Active acoustic aperture | Unknown; 10 mm piston is only an explicit modeling approximation |
| Capacitance / impedance | Unknown; old 16 mm 2–2.5 nF figures do not apply automatically |
| Drive voltage rating | Unknown; no continuous-drive rating inferred from another part |
| SPL | Image says >=110 dB with unspecified conditions; not model pressure calibration |
| '+' / shell connection | Image claim; electrical and acoustic verification required |

At the explicitly configured c=343 m/s and f=40 kHz, wavelength is 8.575 mm. The 12 mm pitch is
about 1.40 wavelengths, still larger than lambda/2. Prioritize opposed standing waves and modest trap
movement; do not promise wide-angle alias-free steering.

Voltage progression 10→12→16→~20 Vpp remains only a candidate characterization sequence, conditional
on qualification of this actual part. Do not assert even the first step is safe solely from its diameter.
Differential Vpp, duty cycle, waveform, overshoot, driver temperature and measured batch behaviour must be recorded.
No thermal/current/pressure or mass-support result exists for the new candidate.

See hardware/transducers/10mm_supplier_reference.md for exact image provenance and limits,
hardware/mechanical/radiating_surface_geometry.md for dimensional datums, and
hardware/characterization/transducer_characterization.md for the measurement procedure.
