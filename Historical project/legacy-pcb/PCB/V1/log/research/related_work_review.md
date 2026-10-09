# Bounded reference review — 2026-09-25

No external schematic, PCB, HDL or source code was copied. Native circuit capture
is derived from this project's interface and the selected manufacturers' pin tables.

| Source / rights | Relevant idea | Adopt | Excluded / adaptation / risk |
|---|---|---|---|
| [AMD UG933 v1.13.1](https://docs.amd.com/v/u/en-US/ug933-Zynq-7000-PCB), manufacturer copyright | Bank supply and return path discipline | Isolated FPGA_CORE_INTERFACE; VIO_REF verified from actual bank before connection | Generic Zynq guidance does not identify Robei connector pins or VCCO. No guessed FPGA schematic |
| [EVAL-AD7606B-FMCZ / UG-1225](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD7606B-FMCZ.html), ADI reference-design terms | Dedicated analog regulator, reference and ADC decoupling | Separate AVCC/VDRIVE, local REGCAP decoupling, explicit reference option | No wholesale FMC connector or evaluation-board power topology copy; use actual v2 four-DOUT contract |
| [CN0148](https://www.analog.com/en/resources/reference-designs/circuits-from-the-lab/cn0148.html), ADI copyright | Channel matching and return-current partition | Matching RX branches and short local decoupling returns | AD7606 is not AD7606B; all actual ADC pins/configuration come from AD7606B Rev B |
| [Ultraino](https://github.com/asiermarzo/Ultraino), MIT repository license | Repeated modular channels and separate acoustic simulator | Consistent channel IDs, replaceable modules, test access | No copied schematic/code, Arduino timing, supply rating or pressure prediction |
| [leastrobino/acoustic-levitation](https://github.com/leastrobino/acoustic-levitation), CERN OHL v1.2 | FPGA signal generation separated from embedded phase computation and daughterboard power | Controller/driver separation and repeated channel organization | Its 88-channel Murata/DE0 implementation does not qualify TCT40, TC4427A or this serializer |

Architecture remains 32 serializer lanes, two 64-TX banks, four RX per bank,
central eight-channel ADC and remote environmental sensor. Electrical timing,
load characterization and the physical connector gates remain independent.

The EDA GUI originally reported 3.2.135. After the user's reopen it reports
3.2.149. Library APIs were exercised in the live native editor; local-file save
uses its normal Save dialog. Direct filesystem API is permission-disabled.
Creating new library symbols through `LIB_Symbol.create('project',...)` returned
undefined; no fabricated symbol file is substituted for that failed operation.
