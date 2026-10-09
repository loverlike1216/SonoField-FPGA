# Software-to-hardware interface contract (v2)

Status: DIGITAL_INTERFACE_CONTRACT / PCB_PROPOSED. No PCB layout, connector pin allocation,
Gerber, purchasing or manufacturing authorization is issued by this document.
The machine-readable system baseline, hardware_parts and register_map JSON files are authoritative
for the current software profile. User BOM part strings are preserved; component ratings still
require schematic review and batch qualification.

## Functional boundaries and rails

| Boundary | Contract |
|---|---|
| FPGA source | Documented N18/33 MHz precedence; exact part, VCCO and some connector pins remain BLOCKING |
| Simulation PL | 132 MHz synchronous bus/core; no physical MMCM or timing closure claim |
| Serializer | SN74LVC595APWR, 3.3 V logic candidate, 32 independent lanes, one 8-bit IC per lane with only four mapped outputs |
| Translation | SN74AXC8T245PWR; both rails must remain <=3.6 V, never a 5 V translator; FPGA-side rail waits for VCCO proof |
| Clock fanout | SN74LVC244APWR at 3.3 V candidate; skew/load/trace budget must be measured before 66 MHz use |
| TX stage | TC4427AEOA713, user policy VDRV 12 V initially, 12..15 V operating exploration, 18 V project ceiling; no continuous acoustic drive qualification implied |
| RX switch | TMUX1574PWR; two logical bank blank controls, active high at PL; board logic must map 1 to quiet 2.5 V/reference, 0 to RX signal |
| AFE | OPA4192IPWR, 5 V analog supply proposal, REF5025AIDR 2.5 V bias; selectable nominal gain 11 or 22 requires measured transfer, clipping and recovery |
| ADC | AD7606BBSTZ-RL: AVCC5 V, VDRIVE3.3 V, software mode, serial/four DOUT, +/-5 V input profile |
| Environment | SHT45-AD1B-R2, remote from driver heat; PS/host I2C responsibility; this stage accepts timestamped T/RH config input, no real sensor reading is claimed |

The 0..5 V biased AFE signal fits a +/-5 V ADC range, not +/-2.5 V. The ADC's negative half
is intentionally unused by that AFE bias. Nominal ADC voltage = signed_code * 5/32768 V.
Design headroom is initially 0.25..4.75 V at the ADC input; scope measurement, tolerances and
OPA output swing must confirm it. Detect signed-code rail clipping and record peaks/RMS/DC.
ADC clamps are not a substitute for RX protection; TMUX powered-off signal limits must be checked
against actual RX transients. Do not connect either RX bank directly to a transmitter power node.

## Digital signals (logical names, NOT guessed connector pins)

| Signal | Direction relative to PL | Meaning |
|---|---|---|
| adc_convst | out | rising sample edge; 2 core cycles high; 165-cycle period at 800 kSPS |
| adc_busy | in | two-flop synchronized conversion-complete detection; conversion timeout fails closed |
| adc_reset | out | full reset, 4 us high then >=254 us setup after conservative initial power wait |
| adc_cs_n / adc_sclk / adc_sdi | out | SPI framing, 33 MHz SCLK profile, actual configuration/readback required |
| adc_dout[3:0] | in | A/B/C/D, 32-bit transaction, MSB-first; source-synchronous return timing |
| rx_blank[1:0] | out | bit0 upper bank, bit1 lower; 1 blank, reset=11; unblank opposite bank then settle |
| serial_data[31:0] | out | lane l maps RTL channels 4*l..4*l+3; shifts bit3,2,1,0 |
| shift_clock | out | 66 MHz within a four-bit update frame |
| latch_clock | out | common simultaneous output publication; all unused 595 outputs disconnected from drivers |
| output_disable | out | active high; external pull-up / independent hardware interlock required |
| hardware_enable | in | active high permissive; falling edge disables immediately; synchronized release |
| bus_valid/write/address/wdata | in | PL-clock synchronous register interface; no PS pin or AXI assignment |
| bus_ready/rdata/error/irq | out | response, sticky errors, capture-ready/done/fault event |

32 lanes require 32 actual shift registers with four used outputs each, consistent with the supplied
BOM. This is not a 16-lane/8-output timing claim. A future harness/connector design must budget
all signals, grounds and rails. No arbitrary 20-pin allocation is frozen here. Functional board
partition remains FPGA interface, modular TX power, TX carriers and RX/ADC acquisition.

ADC channel order is permanent: ADC0..3 UPPER_RX0..3; ADC4..7 LOWER_RX0..3. In four-lane mode,
DOUTA V1/V2, B V3/V4, C V5/V6, D V7/V8. Positions are radiating-face centres at the defined corner
coordinates; carrier PCB thickness is not a geometric calibration parameter.

## AD7606B startup and frame contract

Strap PAR/SER SEL=1 and OS[2:0]=111 for software mode. Ensure STBY/WR and reference selection
match the final schematic. RTL waits >2 s after its reset release before the full ADC reset;
power-good must precede PL reset release. It then asserts reset 4 us, waits 254 us, enters register
mode with 0x4200, writes CONFIG 0x0210 and ranges 0x0311/0x0411/0x0511/0x0611, reads back CONFIG
and all four range registers with two-frame reads, and writes 0x0000 to exit register mode.
No oversampling, CRC or status header is enabled. These additions change framing and require a
new verified profile, not an unchecked flag change. Tests shorten only the initial two-second wait.

CS falling presents the first MSB; AD7606B advances later bits after SCLK rising. The FPGA captures
the preceding stable bit on the core edge launching that rising edge. 32 cycles at 33 MHz take
about 0.97 us. Reads extend across the next conversion. The behavioral model checks 650/850 ns
alternating BUSY completion, 9 ns CS-to-data and 15 ns SCLK-to-data, and >=25 ns before the next
BUSY falling edge. This is chip-level behavioral evidence, NOT return-flight/setup/hold closure
through a translator, cable and PCB. Use lower sampling rate if measured timing requires it.

No external DOUT synchronizer may be inserted casually; independently synchronizing bits would
corrupt the serial timing model. Real XDC must constrain input/output paths from the verified FPGA
part/IO rail and actual board delays. Such XDC and synthesis are blocked on board facts.

## Register and capture protocol

See generated REGISTER_MAP in docs/architecture and config/register_map.json for byte addresses.
CONTROL bit0=software enable, bit1=start pulse, bit2=abort and force SAFE. MODE 0..5 follows the
architecture document. Parameters write only while SAFE; frequency 38500..41500 Hz, scan 1..128,
first TX0..127, sampling period >=165 cycles. Invalid writes latch a fault. Recovery is reset.
STATUS bits 0 enabled,1 ADCready,2 scanactive,3 capture-ready,4 done,5 fault,6 mapvalid,7 ADCidle.
ERROR bits0 ADC,1 scan,2 bus,3 serializer,4 map; bits5..8 scheduler state.

Each capture holds 1..1024 frames, eight signed int16 channels per frame. Host writes BUFFER_ADDR
as a 32-bit word offset, waits one PL clock, reads BUFFER_DATA. Words 0..3 hold ADC0/1,2/3,4/5,6/7
in little-endian order. First timestamp and period reconstruct every conversion index. Burst and
TX-enable timestamps distinguish request, acquisition and serialized publication. ACK_CAPTURE bit0
releases ownership. Read/drain metadata before ACK. No full DMA/DDR path is claimed.

Map writes use MAP_CHANNEL, MAP_DATA [7:0] requested, [15:8] calibration, [16] enable, MAP_WRITE.
Write all 128 unique channels then MAP_COMMIT. MAP_STATUS bits0 write-ready,1 pending,2 commit-ack
(one cycle),3 valid. Host polls pending/valid; it need not catch the one-cycle acknowledgement.
Never clear previous calibration as an implicit side effect of updating requested phase.

## Before physical use

Measure RX-chain complex gain/group delay and one phase reference in EACH directional bank;
otherwise cross-bank absolute phase remains unknown. Measure TX polarity, resonance, capacitance,
AFE saturation/recovery, driver waveform/current/temperature and serializer timing. Record raw
ADC data with actual firmware/source hash, sample-clock measurement and timing metadata.
Qualify PH0/PH1 before full power: physical acceptance still needs scope traces and measured
particle mass/dimensions/environment. No software plot supplies those observations.

Primary references: [AD7606B](https://www.analog.com/media/en/technical-documentation/data-sheets/ad7606b.pdf),
[SN74LVC595A](https://www.ti.com/product/SN74LVC595A),
[SN74AXC8T245](https://www.ti.com/product/SN74AXC8T245),
[TMUX1574](https://www.ti.com/product/TMUX1574),
[SHT45](https://sensirion.com/products/catalog/SHT45).
