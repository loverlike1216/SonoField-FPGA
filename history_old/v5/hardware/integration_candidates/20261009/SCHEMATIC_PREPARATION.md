# Three-board candidate design package

Status: offline preparation only; native EasyEDA project/interface unavailable this run; ERC NOT_RUN. No native schematic, PCB or Gerber is fabricated. The two arrays can share one logical design with different side/channel assembly identifiers. Manufacturing HOLD.

Central modules: AX7020 J10/J11 signal-only adapter; UP/DN distribution and clock branching; one8channel simultaneous ADC and software straps; ADC reference/REGCAP/input protection; AUX protected power; three independent I²C domain buffering candidates; INA226/TMP117; E-stop/status test points. AX7020 power pins NC, actual board grounds retained. 80-pin connector candidate CSV has package pin,bank,direction,canonical net,source and qualification state. It is not an XDC or approved cable pinout.

Array modules: independent XT30/protection/local power;16 independent595 lanes;32 dual TC4427A;64 NU40C10T;4 RX;2 OPA4192;TMUX1574 blank/reference;local REF5025;external watchdog/rail qualification/rearm/TX cutoff;RX shielded cable;temperature/current monitoring. TX IDs UPPER_TX_00..63 and LOWER_TX_00..63. ADC channels0..3 map UPPER_RX_00..03,4..7 LOWER_RX_00..03. Transducer positions are radiating-face centers; TX x/y=-42,-30,-18,-6,6,18,30,42mm; z=±gap/2. RX four corners(±54,±54)mm; upper normal−Z, lower+Z. Hole/pin/body tolerances remain sample-dependent.

## Canonical logical connectivity

| Network | Origin → destination | State |
|---|---|---|
| TX_DATA_UP[15:0]/TX_DATA_DN[15:0] | PL→central→16 DS per side→595 Q0..Q3→drivers→64TX | Core mapping preserved; cable physical assignment candidate |
| UP/DN_SRCLK, RCLK | PL→central→local4+4 clock fanout→595 groups | External min/max timing open |
| UP/DN_OE_N,RESET_N | PL→qualified local safety→595 OE/SRCLR | Local default-off bias mandatory; clear+latch sequence |
| UP/DN_RX_BLANK,HEARTBEAT,SYNC | PL→local analog switch/watchdog/sync | New sync/heartbeat board wiring candidate; no core protocol rewrite |
| UP/DN_PGOOD,FAULT_N | Local monitored rails/fault→qualified return→PL | FLT_N is not a substitute forPGOOD |
| ADC_CONVST,SCLK,CS_N,SDI,RESET | PL→central ADC | Common conversion start; mode/readback candidate |
| ADC_BUSY,DOUT[3:0] | ADC→PL | FourDOUT/8×16bit; actual return timing unverified |
| MON_I2C_SCL/SDA | PL open drain or PS EMIO via two PL pins→buffered monitoring bus | No push-pull AXC use; actual controller adaptation not implemented |
| ESTOP_OK | Hardwired NC fail-safe status→PL | Monitoring does not replace direct power/enable interlock |
| RX_UP[0:3],RX_DN[0:3] | Local AFE→fourshielded pairs/side→ADC ch0..7 | Not Ethernet; connector keying and shield grounding open |
| UP_PWR_IN,DN_PWR_IN,AUX_PWR_IN | Independent protected external branches | No array power through FPGA connector |

## Candidate direction grouping and I²C

Each array has21 nonclock outputs and2 returned status signals after allocating SRCLK/RCLK directly to the clock fanout. AXC8T245 has two4bit DIR groups, so6 output groups+1 input group require **four chips per array**. Candidate groups: DATA0..15 in four groups; OE_N,RESET_N,BLANK,HB in group5;SYNC in group6 with unused inputs safely biased;PGOOD/FAULT in return group7;group8 spare. Central twoAXC can provide twooutput groups for5ADC controls and twoinput groups for5ADC signals+ESTOP; I²C separate. Same nominal3.3V does not eliminate powered-off isolation; cancellation needs Ioff/sequence/signal integrity evidence.

Use one INA226/TMP117 per board for power/thermal visibility. Proposed7bit addresses: centralINA0x40(A1=GND,A0=GND),UP0x41(A1=GND,A0=VS),DN0x44(A1=VS,A0=GND); TMP central0x48(ADD0=GND),UP0x49(V+),DN0x4B(SCL). Verify straps against exact manufacturer revision and native netlist. Separate pullups on each powered segment;4.7kohm is a candidate, determine Rmin from sink current and Rmax from bus capacitance/rise-time. Three central TCA4307 open-drain isolation candidates separate AX/main and both array domains; verify power-off behavior, stuck-bus handling, EN bias and address visibility. PS MIO I²C pins are not assumed accessible through J10/J11; EMIO/controller is future board adaptation. SHT45 remote board is optional DNP.

## ADC/reference and component audit

ADP7118ACPZN5.0-R7 isCP-6-3/LFCSP6:1VOUT,2SENSE/ADJ,3GND,4EN,5SS,6VIN; EP=GND. VOUT/VIN each needs datasheet-compatible capacitors; sense to5V output, SS not grounded. Text package correction is complete; native symbol/land/Pin1/thermal pad audit not performed.

ADC REGCAP pins36/39 each have a separate1µF toAGND; REFCAPA/B44/45 common reference capacitor10µF toREFGND,REFIN/REFOUT10µF separately. Check C-16 exact pin map/reference mode and supply bypass against RevA before implementation. RX_REF2V5 is an AFE bias, not an interchangeable ADC reference. Composite RC/reference rows are design groups with0procurement quantity; passives remain in actual aggregate rows and cannot be double-counted. Every final passive still needs reference designator/tolerance/voltage/MPN assignment.

Package row audit CSV distinguishes exact manufacturer package matches, unresolved suffix/MPN, passive/composite/mechanical entries, and unavailable EDA-library validation. A nominal package name is not a successful CAD land-pattern check. RX part,NU40C10T supplier datasheet, eFuse surge circuit, rail supervisors/watchdog/gates, connector models/polarity and thermal/stackup remain open.

## Required native design work

Open/create the actual v5 EasyEDA project and connect the documented bridge. Build central+common-array candidate sheets, use visible module boundaries/names, standard orientations/readable labels and hierarchical side names. Generate netlist/BOM from those symbols, compare to candidate signal and quantity tables, run real ERC and review every warning. No old PCB/V1 file is an authoritative v5 native schematic. Native creation waits for a connected tool/project and the missing electrical facts; logical preparation is available now.
