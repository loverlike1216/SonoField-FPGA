# Procurement categories — quantities are planning inputs, no purchases made

| Item | P0 purpose / quantity | Selection gate |
|---|---|---|
| User-selected 10 mm / 40 kHz transmitter | At least 2 characterization samples first; 128 positions in current full design | Exact part and batch identity, dimensions/impedance/voltage rating |
| TCT40-16R or ultrasonic receiver | 1 minimum | Relative phase fixture; calibration needed for absolute pressure |
| Robei Zynq-7020 | 1 existing target | Complete part/voltage confirmation |
| TC4427A or reviewed equivalent | Prototype gate-driver candidate | Compatible chosen MOSFET topology, supply and load |
| MOSFET / bridge parts | 2 acoustic channels initially | Load measurement, gate charge, deadtime and disable review |
| Current-limited bench supply | 1 | Suitable independent low-voltage driver supply |
| Oscilloscope and differential probing | At least logic + differential load measurement | Bandwidth/grounding appropriate to switching edges |
| Scale and calibration weights | Resolution suitable for initial particle; about 0.1 mg for small targets | Recorded uncertainty and calibration |
| Calipers, temperature probes, LCR meter | Characterization | Instrument settings recorded |
| Adjustable opposed fixture | P0 gap/alignment sweep | Measured transducer dimensions |
| 74AHCT595, clock buffers | P1/P2 candidate only | PCB-A timing and voltage review before procurement freeze |

No final 128-channel MOSFET/BOM release. Avoid purchasing the complete P3 system before P0/P1 evidence.
