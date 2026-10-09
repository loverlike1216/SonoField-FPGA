# ADC candidate review — decision required, not a production substitution

2026-10-09; v5; GPT-6.1 Sol High (user-declared). Related OPEN problem: P-20261008-001. Original user workbook and existing AD7606B RTL remain intact. The working workbook recommends **AD7606C-16BSTZ-RL**, pending independent review and user approval.

| Criterion | AD7606B | AD7606C-16 candidate |
|---|---|---|
| Channels/data | 8 simultaneous, 16-bit | 8 simultaneous, 16-bit |
| Maximum sample rate | 800 kSPS/channel | 1 MSPS/channel; retain existing cadence initially |
| Analog bandwidth | ±5V:13.5kHz; ±10V:22.5kHz | normal25kHz; software high bandwidth220kHz/channel |
| 40kHz implication | Frequency beyond stated analog passband; attenuation/phase must be measured | 40kHz inside high-bandwidth passband; not zero phase/error and not guaranteed matching |
| Interface | Current software mode, four DOUT | Software mode required for high bandwidth and four DOUT;32 clocks/8 samples |
| Supply | AVCC5V, VDRIVE1.71–3.6V | AVCC4.75–5.25V; VDRIVE1.71–5.25V; choose qualified3.3V |
| Analog range | Current four registers0x11 select±5V | Same candidate range0x11 in0x03..0x06 |
| Package | LQFP64 | LQFP64, pin compatible; symbols/power straps still require audit |
| Noise/calibration | Existing digital reference only | ADI headline92dB is for±20V differential, not a guaranteed±5V/40kHz result; evaluate appropriate conditions |
| Procurement | Existing recommendation | Manufacturer product page lists production models; live distributor stock/quote NOT_VERIFIED |

Sources: [AD7606B Rev B](https://www.analog.com/media/en/technical-documentation/data-sheets/ad7606b.pdf), [AD7606C-16 Rev A](https://www.analog.com/media/en/technical-documentation/data-sheets/ad7606c-16.pdf), [manufacturer product/ordering](https://www.analog.com/en/products/ad7606c-16.html). Downloaded C-16 document SHA256:51b7051688a3c9ec61f90a01fda77a4ee0373adedacc1c7ea30a3d0e1c8041a5. Manufacturer list price is not a supplier stock or delivered-cost guarantee.

## Candidate initialization and RTL impact

OS[2:0]=111 enters software mode; confirm PAR/SER/BYTE SEL straps against datasheet. Enter register mode by reading CONFIG. Write CONFIG0x02=0x10 (four DOUT, status/CRC disabled); RANGE0x03..0x06=0x11; **BANDWIDTH0x07=0xFF**. Read back all six registers with pipelined response handling, then write0x00 to return to conversion reads. Candidate command ROM is isolated in ad7606c_candidate_rom.sv. It is not instantiated in the existing production interface.

Current ad7606b_if.sv never writes/verifies0x07, so a physical chip swap alone leaves the required high bandwidth disabled. A later approved adapter must extend initialization/readback checks and fail READY on reset/configuration errors. Preserve adc_serial lane mapping,8×16bit frame, common CONVST/timestamp, timeout policy, AXI/register/protocol/calibration contracts. The existing serial engine samples the old DOUT at the launching SCLK rising edge; C-16 also advances DOUT on that edge. This is logical compatibility only. Requalify first-MSB delay, SCLK/CS timing and returned data including translators/cable on hardware.

The independent Python bitstream reference and current adc_serial RTL were checked with256 fixed-seed frames including signed extremes, using Icarus and XSim. Six corrupted-register responses are rejected by the **reference policy**. This does not prove a complete C-16 initialization RTL implementation, actual ADC synchronization, analog frequency response, CRC behavior or real calibration. No CRC/status test is claimed because this candidate keeps them disabled.

AFE still needs measured gain, saturation/recovery,40kHz phase response and antialiasing. High ADC bandwidth can admit more switching noise. Keep47ohm/1nF input RC as a reviewed candidate, assess op-amp stability/cable capacitance and filter folding; do not treat its simple pole as the whole AFE transfer. Recalibrate RX group delay and phase, preserving original requested/calibration separation. Simultaneous sample conversion does not mean identical analog channel delay.

No third ADC is required to resolve the documented bandwidth mismatch while preserving the architecture. AD7606C-18 would alter the16bit format and is unnecessary for this bounded candidate. Independent review NOT_RUN: no supported external ChatGPT reader/reviewer was available, and no self-review is presented as independent approval. Review inputs: this document, adc_candidate.json, candidate_checks.json, both simulator logs and P-20261008-001. Formal selection and electrical freeze remain pending.
