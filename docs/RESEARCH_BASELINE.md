# Primary reference register (accessed 2026-09-18/19)

| Source | Used for | Limits |
|---|---|---|
| Local Zynq7020/constrain/*.const | User-authoritative board clock and pin candidates | No package/speed/VCCO; malformed entries |
| [Nexperia 74AHC/AHCT595 Rev.9](https://assets.nexperia.com/documents/data-sheet/74AHC_AHCT595.pdf) | Shift/latch/OE semantics and worst-case timing | Must select actual supply/load/temp corner |
| [Microchip TC4427A](https://www.microchip.com/en-us/product/TC4427A) and its linked DS20001423K | Candidate gate-driver role/range | Does not define a complete bridge or TCT40 limits |
| [TCT40 component sheet hosted by SparkFun](https://docs.sparkfun.com/SparkFun_Ultrasonic_Distance_Sensor-Qwiic/assets/component_documentation/TCT40-16-T-R.pdf) | Example nominal transducer specifications | Purchased manufacturer/lot and continuous voltage limit unknown |
| [Bruus radiation-force tutorial](https://orbit.dtu.dk/en/publications/acoustofluidics-7-the-acoustic-radiation-force-on-small-particles/) | Small-particle modeling limitations | Does not justify 50 mg EPS Rayleigh force estimates |

No third-party RTL, geometry model or reference-project source was copied. Local PNG sources include
third-party watermarks; retain locally and do not redistribute automatically. Public dependencies are
installed normally, version-pinned and not vendored. Tool installations are external prerequisites.
