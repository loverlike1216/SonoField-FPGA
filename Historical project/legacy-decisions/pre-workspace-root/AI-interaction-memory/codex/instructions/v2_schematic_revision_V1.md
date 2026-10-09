# ============================================================
# SonoField-FPGA
# v2 / Schematic Revision V1
# 嘉立创EDA专业版正式原理图工程
# Codex Formal Execution Specification
# ============================================================


# 0. USER AUTHORIZATION / PROJECT GATE

PROJECT_ID:
SONOFIELD_FPGA

PROJECT_NAME:
SonoField-FPGA

FORMAL_REPOSITORY:
https://github.com/loverlike1216/SonoField-FPGA

WORKSPACE:
E:\Codex_project\AMD-SonoField-FPGA

CURRENT_BRANCH:
main

ACTIVE_PROJECT_VERSION:
v2

SCHEMATIC_REVISION:
V1

AUTHORIZED_STAGE:
SCHEMATIC_DESIGN_JLCEDA_PRO

PROJECT_EXECUTION:
PROJECT_ACTIVE


IMPORTANT VERSION DISTINCTION:

E:\Codex_project\AMD-SonoField-FPGA\PCB\V1

中的 V1 仅表示：

SCHEMATIC_REVISION_V1

即“第一版原理图工程”。

它绝不表示：
- SonoField-FPGA 项目回退到 v1；
- 开启新的项目 v1；
- 修改根目录历史 v1；
- 替代当前 active version v2。

正式项目版本仍然：

v2

原有项目：

v1/

继续保持 FROZEN / READ-ONLY。

任何：
“继续”
“continue”
“继续开发”
“继续优化”
“继续修复”
“继续测试”

都表示：

CONTINUE_CURRENT_VERSION = v2

不得因此创建 v3。

只有用户明确批准后才允许开启 v3。


# ============================================================
# 1. ABSOLUTE SCOPE
# ============================================================

本 Stage 只允许：

SCHEMATIC ONLY

即：

只设计、生成、审查和完善
嘉立创EDA专业版原理图。

本 Stage 明确禁止：

- PCB Layout
- PCB Placement
- PCB Routing
- Board Outline implementation
- Copper Pour
- Plane Layout
- Via Design
- Differential Pair Routing
- Physical Length Matching
- Impedance Routing
- Gerber
- Drill File
- Pick & Place
- CPL
- Stencil
- Manufacturing Package
- PCB Fabrication Release

不得以任何理由自动进入 PCB 设计。

即使嘉立创EDA专业版自动生成空 PCB 文件，
也不得继续 Placement 或 Routing，
不得把空 PCB 当成本 Stage 成果。

本阶段最终目标为：

SCHEMATIC_DESIGN_READY

不是：

PCB_READY

不是：

FABRICATION_RELEASE

不是：

HARDWARE_VERIFIED


# ============================================================
# 2. MANDATORY DIRECTORY STRUCTURE
# ============================================================

所有本 Stage 工程必须严格保存于：

E:\Codex_project\AMD-SonoField-FPGA\PCB\V1

固定目录：

E:\Codex_project\AMD-SonoField-FPGA\PCB\V1\
│
├── project\
├── log\
└── device\


## 2.1 project

正式嘉立创EDA专业版原理图工程必须保存到：

E:\Codex_project\AMD-SonoField-FPGA\PCB\V1\project

仅保存正式工程内容，例如：

- 嘉立创EDA Professional 原生工程
- 原理图 Sheet
- Hierarchical Sheet
- Project configuration
- project-local schematic library
- 原理图 PDF 导出
- schematic netlist（若原理图工具原生支持且确有用途）
- schematic BOM audit export
- schematic-only interchange file

禁止在 project 内保存：

- 临时截图
- 浏览器下载垃圾文件
- build cache
- 调试日志
- PCB layout
- Gerber
- 自动备份垃圾副本
- 无意义 temp 文件


## 2.2 log

所有日志及工程证据必须保存到：

E:\Codex_project\AMD-SonoField-FPGA\PCB\V1\log

包括：

- preflight
- Related Work 调研
- datasheet review
- ERC
- schematic rule check
- connectivity audit
- net label audit
- BOM audit
- device pin audit
- power review
- timing review
- signal-level review
- calculations
- screenshots
- tool operation record
- review reports
- unresolved issues
- ERC waivers
- final review
- Git synchronization evidence

推荐结构：

log\
├── preflight\
├── research\
├── datasheet\
├── calculations\
├── pin_audit\
├── net_audit\
├── bom_audit\
├── erc\
├── screenshots\
├── review\
└── final\


## 2.3 device

项目使用器件相关资料统一保存到：

E:\Codex_project\AMD-SonoField-FPGA\PCB\V1\device

包括：

- 嘉立创EDA器件库映射
- symbol
- custom symbol
- package association metadata
- provisional footprint metadata
- pin mapping
- LCSC/JLCEDA part mapping
- manufacturer part number
- component parameter record
- datasheet source metadata
- manufacturer source link record
- hash / document revision record

如果 datasheet 存在版权或再分发限制：

不要把受限制 PDF 擅自上传公开 GitHub。

改为保存：

- manufacturer
- document title
- revision
- official source
- access date
- SHA256（若本地合法持有）
- engineering parameters extracted

不得为了“资料完整”违反 License。


# ============================================================
# 3. GITHUB SYNCHRONIZATION
# ============================================================

本 Stage 所有适合版本控制的正式工程内容必须同步至：

loverlike1216/SonoField-FPGA

branch:

main

对应 Repository 相对路径保持：

PCB/V1/project
PCB/V1/log
PCB/V1/device

不得：

- 新建正式 Repository
- 更换 Repository
- force push
- 改 visibility
- 发布 Release
- 删除 Git 历史

Push 前必须检查：

- token
- key
- password
- cookie
- private credential
- personal data
- unauthorized proprietary file
- restricted datasheet
- temporary file


# ============================================================
# 4. PRE-FLIGHT — MUST EXECUTE FIRST
# ============================================================

在修改任何原理图之前，
必须重新读取真实 Repository 当前状态。

不要假设历史 HEAD 仍然是最新 HEAD。

历史已知 validated source checkpoint 曾为：

9c058fe3b02469a6d36a08e3a7cbedd19076e67b

但本次必须重新执行：

git status
git branch
git log
git fetch
git diff
git remote
git ls-remote

确认真实当前状态。


必须读取至少：

README.md

AGENTS.md

shared/PROJECT_STATE.json

shared/CURRENT_PLAN.md

shared/ACCEPTANCE.md

shared/BLOCKERS.md

shared/HANDOFF.md

shared/DECISIONS.md
如果存在

CHANGELOG
或等价文件

AI-chat-memory/INDEX.md

AI-interaction-memory/INDEX.md

AI-problem/problem/*

AI-problem/decision/*
如果存在

v2/docs/architecture/*

v2/docs/hardware/*

v2/hardware/bom/*

v2/hardware/mechanical/*

v2/hardware/transducers/*

v2/config/*

v2/rtl/*

v2/software/*

v2/tests/*

root:

BOM/
Zynq7020/

并重点读取：

gpio.const
hardware.const
XDC / constraint references
PCB_SOFTWARE_INTERFACE.md
SELF_CALIBRATION.md
report_v2.md
BOM_LOCK.md
最新 validation evidence
最新 reproducibility evidence

记录：

PROJECT_ID
project_name
repository
workspace
branch
active_version
current_stage
current_commit
dirty status
Chat Source
open blockers
open AI problems

将 preflight 结果写入：

PCB\V1\log\preflight\


# ============================================================
# 5. CURRENT REPOSITORY FACTS
# ============================================================

当前已知工程事实包括：

ACTIVE_VERSION:
v2

v1:
FROZEN

已完成的软件/数字阶段：

SELF_CALIBRATION_SOFTWARE_AND_DIGITAL_SYSTEM

当前软件/数字链已经实现并有证据：

- 128 TX control
- requested/calibration phase separation
- atomic phase commit
- finite TX burst
- RX blanking
- 128-TX scan scheduler
- ADC interface
- bounded capture
- host API
- self-calibration
- TOF
- phase
- pose
- geometry
- frequency sweep
- f_work selection
- health
- calibration database
- LUT
- robustness tests

历史验证包括：

- Python tests
- Icarus
- Vivado 2025.2 XSim
- deterministic/reproducibility checks
- fresh clone verification

这些结果是：

DIGITAL / SOFTWARE EVIDENCE

不是：

PHYSICAL HARDWARE EVIDENCE

不得把 digital PASS 解释成：
原理图、电气、PCB 或悬浮已经通过。


# ============================================================
# 6. FACT PRECEDENCE
# ============================================================

事实优先级：

用户当前指令
>
用户批准的正式决策
>
当前真实代码/配置
>
厂家官方 datasheet
>
AMD / Analog Devices / TI 等官方资料
>
真实工具证据
>
shared 当前状态
>
AI-problem formal decision
>
AI-interaction-memory
>
开源参考项目
>
第三方教程
>
模型推断

如果出现冲突：

必须创建：

DECISION_CONFLICT

记录：

Problem
Source A
Source B
Evidence
Impact
Safe Temporary Assumption
Candidate Resolution
User Approval Required

不得静默选择方便实现的一方。


# ============================================================
# 7. RESEARCH BEFORE FINAL SCHEMATIC ARCHITECTURE
# ============================================================

在正式冻结原理图模块划分之前，
先执行一次有边界的 Related Work 调研。

优先研究：

1. AMD / Xilinx Zynq-7000 PCB Design Guide
   重点：
   - SelectIO
   - VCCO
   - bank power
   - decoupling
   - signal integrity
   - return path

2. Analog Devices EVAL-AD7606B-FMCZ
   重点：
   - AD7606B recommended schematic
   - AVCC
   - VDRIVE
   - reference
   - decoupling
   - grounding
   - digital interface

3. Analog Devices CN0148
   重点：
   - simultaneous-sampling ADC
   - analog/digital partition
   - reference distribution
   - grounding/layout philosophy

4. asiermarzo/Ultraino
   重点：
   - modular ultrasonic channel architecture
   - repeated channel organization
   - array control approach
   - driver board partition

5. leastrobino/acoustic-levitation
   重点：
   - FPGA/SoC multi-channel ultrasound
   - ~40 kHz
   - daughterboard architecture
   - channel replication
   - controller/power separation

6. 其他可信 open-source ultrasound / acoustic phased-array PCB
   只用于寻找：
   - channel replication methodology
   - TX power partition
   - connector strategy
   - debug strategy
   - test point organization

调研目的：

学习工程思想。

禁止：

- 整块复制 PCB
- 直接复制原理图
- 换名字照搬
- 删除版权
- 忽略 License
- 因为“开源项目这么做”就跳过 datasheet 检查

每个真正借鉴的重要设计必须写：

PCB\V1\log\research\related_work_review.md

内容：

Source
License
Relevant Circuit / Idea
Why Relevant
What We Adopt
What We Do NOT Adopt
Changes Required for SonoField-FPGA
Risks


# ============================================================
# 8. SYSTEM GEOMETRY BASELINE
# ============================================================

SonoField-FPGA 当前机械/声学基本架构：

双面对置阵列。

UPPER TX ARRAY:

8 × 8

LOWER TX ARRAY:

8 × 8

TOTAL:

128 TX

TX baseline:

TCT40-10T

Pitch:

12 mm
radiating-surface-centre pitch

Nominal array face gap:

100 mm

Allowed mechanical / calibration range:

90–115 mm

Coordinate reference:

RADIATING_SURFACE_CENTER

Origin:

GEOMETRIC_CENTER

Current TX coordinate set approximately:

±42 mm
±30 mm
±18 mm
±6 mm

不得自行改变：

- 128 TX
- 8×8
- 12 mm pitch
- upper/lower opposed architecture


# ============================================================
# 9. RX ARCHITECTURE
# ============================================================

TOTAL RX:

8

UPPER RX:

4

LOWER RX:

4

当前概念坐标：

4 corner RX / bank
约 ±54 mm

最终机械位置允许通过自校准得到真实几何。

ADC CHANNEL ORDER IS FIXED:

ADC0 = UPPER_RX0
ADC1 = UPPER_RX1
ADC2 = UPPER_RX2
ADC3 = UPPER_RX3

ADC4 = LOWER_RX0
ADC5 = LOWER_RX1
ADC6 = LOWER_RX2
ADC7 = LOWER_RX3

不得擅自交换。


# ============================================================
# 10. TCT40-10T/R1 OFFICIAL BASELINE
# ============================================================

当前使用：

Suzhou RuiNing Electronics Co., Ltd.

TCT40-10T/R1

Manufacturer datasheet baseline:

CENTER FREQUENCY:

40 kHz

TX SOUND PRESSURE:

>= 110 dB
at 40 kHz

Reference:

0 dB = 0.02 mPa

Datasheet test geometry shows approximately:

300 mm

RX SENSITIVITY:

>= -70 dB
at 40 kHz

Reference:

0 dB = 1 V/Pa

Equivalent sensitivity:

10^(-70/20) V/Pa
≈ 316 µV/Pa

STATIC CAPACITANCE:

2000 pF ±30%

Engineering range:

1.4 nF – 2.6 nF

DIRECTIVITY:

-6 dB angle = 60°

Treat approximately as:

±30° main useful -6 dB half-angle.

Mechanical drawing:

Body OD:
~9.9 mm

Pin pitch:
5.0 mm

Pin diameter:
~0.7 mm

Body height:
~7 mm

Lead dimensions:
use manufacturer drawing baseline;
batch verify before PCB freeze.

RX datasheet sensitivity test includes approximately:

3.9 kΩ

This is:

DATASHEET_REFERENCE_LOAD

not automatically production AFE load.


# ============================================================
# 11. TRANSDUCER MODEL RULES
# ============================================================

Nominal static capacitance:

2 nF

At 40 kHz:

|Xc| ≈ 1.99 kΩ

BUT:

TCT40 is resonant piezoelectric hardware.

Do not model it as pure C at resonance.

Real equivalent network includes:

C0
Rm
Lm
Cm
resonance
anti-resonance
Q

Therefore:

DO NOT claim exact:
- TX current
- RX amplitude
- acoustic pressure
- levitation force
- phase delay

from C alone.

All relevant locations must retain:

DNP / TUNING / TEST capability.


# ============================================================
# 12. DIRECTIVITY MUST BE INCLUDED IN HARDWARE THINKING
# ============================================================

Because TX and RX both have angular sensitivity:

Path Gain:

G_path =
G_TX(theta_TX)
×
G_RX(theta_RX)

Do not assume:

512 calibration paths
have identical amplitude/SNR.

This is important for:

- corner TX
- far-corner RX
- diagonal paths

Current software already supports:

weak path
missing path
outlier
health weighting

Hardware must preserve dynamic range and not artificially collapse weak-path measurements.


# ============================================================
# 13. ROBEI ZYNQ-7020 BOARD
# ============================================================

Controller board:

Robei 八角板
Zynq-7020 family

Existing project constraint precedence:

N18

33 MHz

Do not silently change this to 33.333 MHz.

Current researched IO facts indicate:

Expansion IO primarily uses:

Bank34 HR
Bank35 HR

Working mapping:

J3 -> mainly Bank34

J6 -> mainly Bank34

J4 -> Bank35

J5 -> mainly Bank35

N20/P20 -> Bank34

Clock-capable pairs found for review include:

U14/U15 -> SRCC_34

U18/U19 -> MRCC_34

H16/H17 -> MRCC_35

N20/P20 -> SRCC_34

These are not automatically final connector assignments.

Must cross-check:

repository board files
constraint files
AMD official package pinout
manufacturer material
physical board if necessary


# ============================================================
# 14. FPGA BLOCKERS
# ============================================================

B01:

Exact Zynq device full ordering code/package/speed grade
remains unresolved unless real evidence closes it.

B03:

Connector numbering / VCCO ambiguity.

Current conflicts historically include:

- pin numbering mismatch
- duplicate entries
- missing entries
- source discrepancies

Important electrical rule:

HEADER 5V != FPGA VCCO

Never infer:

FPGA IO is 5V tolerant.

Actual:

VCCO_34
VCCO_35

must remain:

TBD / VERIFY

unless:

manufacturer schematic
or
physical measurement

confirms them.


# ============================================================
# 15. FPGA_CORE_INTERFACE IS MANDATORY
# ============================================================

Create one dedicated sheet:

FPGA_CORE_INTERFACE

All downstream schematic sheets use logical net names.

Only FPGA_CORE_INTERFACE contains board-specific mapping.

Mapping database must include:

Logical Signal
Connector
Physical Position
Connector Pin Number
Zynq Ball
Bank
Clock-Capable Type
VCCO
IOSTANDARD
Direction
Confidence
Source

If a field is unknown:

TBD

Never invent it.

This design pattern is mandatory because
future B03 correction must not force whole-schematic redesign.


# ============================================================
# 16. NETWORK LABEL GOVERNANCE
# ============================================================

Network names must be treated as formal interfaces.

Priority:

RTL canonical signal name
>
PCB_SOFTWARE_INTERFACE contract
>
schematic alias

Avoid aliases whenever possible.

Never use meaningless names:

NET1
NET2
NEW
TEMP
ABC
IO1

unless auto-generated internal node has no external semantic meaning.


Suggested canonical groups:

SER_DATA[31:0]

SER_SHIFT_CLK

SER_LATCH_CLK

TX_OUTPUT_DISABLE

HW_ENABLE


ADC_CONVST

ADC_BUSY

ADC_RESET

ADC_CS_N

ADC_SCLK

ADC_SDI

ADC_DOUT_A

ADC_DOUT_B

ADC_DOUT_C

ADC_DOUT_D


RX_BLANK_UPPER

RX_BLANK_LOWER


UPPER_RX0
UPPER_RX1
UPPER_RX2
UPPER_RX3

LOWER_RX0
LOWER_RX1
LOWER_RX2
LOWER_RX3


VIN

VDRV

+5V_A

+5V_D

+3V3_LOGIC

VREF_2V5

AGND

DGND

PGND


# ============================================================
# 17. NET LABEL AUDIT
# ============================================================

Create:

NET_LABEL_AUDIT

Check automatically where possible:

- duplicate semantic signal names
- same label / different meaning
- same meaning / different labels
- isolated labels
- accidental net merges
- wrong bus width
- bus breakout mismatch
- wrong direction
- missing hierarchical port
- floating interface
- ADC channel swap
- TX channel duplicate
- TX channel missing
- serializer lane mapping error
- active-low naming inconsistency
- reset polarity mismatch
- blank polarity mismatch
- enable polarity mismatch

Save report:

PCB\V1\log\net_audit\


# ============================================================
# 18. REQUIRED HIGH-LEVEL SCHEMATIC STRUCTURE
# ============================================================

Use hierarchical multi-sheet architecture.

Recommended structure:

00_SYSTEM_OVERVIEW

01_FPGA_CORE_INTERFACE

02_POWER_INPUT_PROTECTION

03_POWER_REGULATION_DISTRIBUTION

04_LOGIC_LEVEL_TRANSLATION

05_TX_SERIAL_CONTROL

06_TX_CLOCK_BUFFERING

07_TX_DRIVER_UPPER_A

08_TX_DRIVER_UPPER_B

09_TX_DRIVER_LOWER_A

10_TX_DRIVER_LOWER_B

11_TX_ARRAY_UPPER

12_TX_ARRAY_LOWER

13_RX_UPPER_INPUT

14_RX_LOWER_INPUT

15_RX_PROTECTION

16_RX_AFE_STAGE1

17_RX_AFE_STAGE2

18_RX_BLANKING_SWITCH

19_ADC_AD7606B

20_REFERENCE_BIAS

21_ENV_SENSOR

22_CONNECTORS

23_TEST_DEBUG

24_POWER_AND_GROUND_NOTES

Allowed to adjust sheet count if it improves clarity.

禁止：

把 128 路全部堆在一张 Sheet。


# ============================================================
# 19. 00_SYSTEM_OVERVIEW REQUIREMENT
# ============================================================

Overview page must visually communicate:

Robei Zynq-7020

→ Level Translation

→ Serializer

→ Clock Buffer

→ TX Drivers

→ Upper / Lower TCT40 arrays


and separately:

RX transducers

→ Protection

→ AFE Stage1

→ AFE Stage2

→ Blanking Switch

→ AD7606B

→ FPGA


Also show:

Power Tree

Ground Domains

Control Signals

Safety Signals

A reviewer must understand the whole system
from this sheet without opening lower-level sheets.


# ============================================================
# 20. SERIALIZER ARCHITECTURE
# ============================================================

Current BOM baseline:

SN74LVC595APWR

approximately:

32 devices

Architecture:

32 serializer lanes

Each lane corresponds to four active TX outputs.

RTL mapping:

lane l

channels:

4*l
4*l+1
4*l+2
4*l+3

Only intended outputs drive TX controls.

Unused 595 outputs:

must not float into driver inputs
and must not accidentally drive channels.

Current digital target:

shift clock approximately:

66 MHz

simulated PL core:

132 MHz

Important:

DIGITAL SIMULATION PASS
!=
PHYSICAL 66 MHz ELECTRICAL PASS


# ============================================================
# 21. B04 SERIALIZER TIMING GATE
# ============================================================

B04 remains open until physical electrical timing is justified.

Create a worst-case timing review covering:

FPGA output
→ translator
→ buffer
→ clock/data interconnect assumptions
→ SN74LVC595

Calculate:

- propagation delay
- setup time
- hold time
- clock-to-Q
- buffer skew
- translator skew
- total skew
- worst-case timing margin

Use:

datasheet MAX / MIN

not only typical.

If 66 MHz margin is insufficient:

DO NOT silently lower frequency.

Record:

DECISION_REQUIRED

with:

Observed Issue
Calculated Margin
Possible Clock Rates
Possible Architectural Alternatives
Impact
Recommendation

Wait for user/ChatGPT decision if architecture changes.


# ============================================================
# 22. LEVEL TRANSLATION
# ============================================================

Current BOM candidate:

SN74AXC8T245PWR

Important:

SN74AXC8T245 is NOT a generic 5 V translator.

Both supplies must comply with actual datasheet limits.

FPGA-side voltage must remain dependent on verified VCCO.

Do not hard-wire assumptions that VCCO is 3.3 V
until board facts are confirmed.

Review:

- power-up behavior
- OE behavior
- direction control
- VCCA
- VCCB
- partial-power-down behavior
- VIH/VIL
- VOH/VOL
- delay
- skew

Fail-safe behavior matters.


# ============================================================
# 23. CLOCK / FANOUT BUFFER
# ============================================================

Current candidate:

SN74LVC244APWR

Review:

- output current
- propagation delay
- channel skew
- capacitive load
- fanout
- 66 MHz edge quality

Provide optional source-series resistors where justified.

Do not hard-code resistor values without SI/timing reasoning.

Allowed:

22R / 33R / 47R candidate
as DNP/TUNING positions

but actual default value must be justified.


# ============================================================
# 24. TX POWER DRIVER
# ============================================================

Current driver:

TC4427AEOA713

Current approximate quantity:

64

Two channels per IC.

TX transducers:

128 × TCT40-10T

VDRV policy:

Initial qualification:

12 V

Expected experimentation:

12–15 V

Project design ceiling:

18 V

Critical rule:

18 V != verified TCT40 continuous safe voltage.

Never label:

TCT40 continuous rating = 18 V

without real qualification.


# ============================================================
# 25. TX DRIVER SCHEMATIC REQUIREMENTS
# ============================================================

Each TX channel design must consider:

- logic input level
- driver supply
- local decoupling
- peak switching current
- power return
- transducer capacitive load
- optional damping
- optional series resistor
- optional snubber
- output test point
- safe reset/off state

TC4427A must receive correct local decoupling
per manufacturer recommendation.

Repeated driver channels must use:

identical topology
identical net naming convention
deterministic annotation


# ============================================================
# 26. TX POWER RETURN
# ============================================================

High-current TX return belongs to:

PGND

Do not allow:

TC4427 switching current
or
TCT40 TX current

to return through:

AFE reference path
ADC analog ground path
VREF return path

Schematic ground-domain intent must make this clear.

Final PCB plane strategy is NOT designed now,
but schematic must not make good PCB impossible.


# ============================================================
# 27. RX PART
# ============================================================

RX:

TCT40-10R1

Quantity:

8

RX negative / shell behavior:

use supplier/manufacturer polarity information
but retain batch verification gate.

RX input should be:

HIGH IMPEDANCE

Do not automatically place 3.9 kΩ load.

The 3.9 kΩ datasheet test resistor is a measurement condition,
not automatically the production optimum.


# ============================================================
# 28. RX FRONT-END ARCHITECTURE
# ============================================================

Preferred high-level chain:

TCT40-10R1

→ protection / damping position

→ AC coupling

→ VREF_2V5 bias

→ OPA4192 Stage 1

→ OPA4192 Stage 2

→ controlled filtering

→ TMUX1574 blanking/switch

→ AD7606B

Exact TMUX placement relative to gain stages
must be determined by:

- overdrive protection
- recovery
- switch signal range
- noise
- phase
- power-off limits

Do not choose position solely for drawing convenience.


# ============================================================
# 29. OPA4192 ARCHITECTURE
# ============================================================

Current BOM:

OPA4192IPWR

approximately:

4 packages

Total amplifiers:

16

RX:

8

Therefore architecture may use:

2 op-amp stages per RX.

Preferred:

moderate gain per stage

rather than:

one extreme-gain stage.


# ============================================================
# 30. RX GAIN OPTIONS
# ============================================================

Current default design concept:

GAIN_LOW:
~11

GAIN_NORMAL:
~22

Also reserve component options:

GAIN_HIGH:
~47

GAIN_XHIGH:
~100

Higher gain modes should initially be:

DNP / TUNING

not necessarily production-populated.

For every gain configuration calculate:

- Rin
- Rf
- tolerance
- DC operating point
- output swing
- input-referred noise estimate
- closed-loop bandwidth
- gain at 40 kHz
- approximate phase at 40 kHz
- expected headroom

Use actual OPA4192 datasheet.

Do not invent GBW/noise values.


# ============================================================
# 31. RX SIGNAL LEVEL SANITY CHECK
# ============================================================

Datasheet gives:

-70 dB re 1 V/Pa

Equivalent approximately:

316 µV/Pa

110 dB SPL corresponds approximately:

6.32 Pa RMS

At that acoustic pressure,
datasheet-order RX signal is around:

2 mV RMS

This is ONLY:

ORDER-OF-MAGNITUDE SANITY CHECK

It must NOT be used as guaranteed system amplitude.

Do not extrapolate precise 100 mm performance by 1/r
and then freeze AFE gain.

Real prototype measurements remain mandatory.


# ============================================================
# 32. RX FILTERING POLICY
# ============================================================

Do NOT default to a high-Q narrow 40 kHz analog bandpass.

Reason:

SonoField needs:

- frequency sweep
- TOF
- phase
- group delay
- amplitude
- envelope

A narrow analog filter can distort:

phase(f)
group delay

Preferred analog front-end:

- overload protection
- DC block
- bias
- moderate gain
- moderate anti-alias filtering

Fine 38–42 kHz discrimination should primarily occur in:

FPGA/software.

Any analog pole must have documented:

fc
gain
phase @ 38k
phase @ 40k
phase @ 42k
group delay
tolerance.


# ============================================================
# 33. RX PROTECTION
# ============================================================

Protection must be designed for:

unknown real TX coupling
ring-down
startup transients
handling
ESD where appropriate

Provide tuneable positions for:

- series resistor
- low-cap clamp
- optional TVS
- RC damping
- optional Schottky clamp
- blanking control

Do not blindly use large-capacitance TVS
on high-impedance RX nodes.

For protection parts check:

- capacitance
- leakage
- clamp voltage
- recovery
- effect on phase
- effect on sensitivity


# ============================================================
# 34. TMUX1574
# ============================================================

Current RX switch candidate:

TMUX1574PWR

Current digital contract:

RX_BLANK_UPPER

RX_BLANK_LOWER

Logical intent:

1 = BLANK

0 = RECEIVE

Verify against actual TMUX truth table.

Required safe behavior:

Reset:
BLANK

FPGA unavailable:
BLANK where hardware permits

Fault:
BLANK

Power-up:
do not expose ADC to uncontrolled transient

Output-disable:
TX off + RX safe


# ============================================================
# 35. AD7606B
# ============================================================

ADC:

AD7606BBSTZ-RL

Current architecture:

8 channels

16 bit

simultaneous sampling

Software mode

Serial interface

4 DOUT

AVCC:

5 V

VDRIVE:

3.3 V
according to current system contract,
but verify actual interface compatibility.

Input range baseline:

±5 V

Current sampling profile:

800 kSPS

Also validated digitally:

400 kSPS option

Do not enable:

CRC
status header
oversampling

unless RTL/software profile is intentionally updated and revalidated.


# ============================================================
# 36. ADC DOUT MAPPING
# ============================================================

Permanent interface:

DOUTA:
V1 / V2

DOUTB:
V3 / V4

DOUTC:
V5 / V6

DOUTD:
V7 / V8

System channel mapping:

V1 = UPPER_RX0
V2 = UPPER_RX1
V3 = UPPER_RX2
V4 = UPPER_RX3

V5 = LOWER_RX0
V6 = LOWER_RX1
V7 = LOWER_RX2
V8 = LOWER_RX3

Cross-check with existing RTL decoder.

No silent swap.


# ============================================================
# 37. AD7606B OFFICIAL REFERENCE DESIGN
# ============================================================

Use Analog Devices:

EVAL-AD7606B-FMCZ

as a primary reference for:

- supply
- reference
- decoupling
- ADC support circuitry
- digital interface conditioning

Also review:

CN0148

for:

- simultaneous-sampling ADC partition
- grounding
- reference distribution
- high-resolution ADC PCB-readiness principles

Do not blindly copy evaluation-board components.

Every adopted element must match:

current AD7606B mode
current voltage
current sampling rate
current reference strategy


# ============================================================
# 38. ADC REFERENCE / BIAS
# ============================================================

Current AFE bias concept:

2.5 V

Current candidate:

REF5025AIDR

Do not assume REF5025 is the ADC reference source
unless current architecture says so.

Distinguish clearly:

AFE_BIAS_REFERENCE

vs

AD7606B_REFERENCE

They must not be conflated accidentally.

Review official AD7606B internal/external reference strategy.

For VREF_2V5:

review:

- load
- output capacitor
- noise
- startup
- buffer requirement
- distribution
- return path


# ============================================================
# 39. ADC INPUT HEADROOM
# ============================================================

Current AFE concept:

2.5 V centred signal

target operating region roughly:

0.25 V to 4.75 V

feeding AD7606B ±5 V range.

This is:

DESIGN TARGET

not measured hardware performance.

Schematic must include test points
to verify:

DC
Vpp
RMS
clipping
settling


# ============================================================
# 40. SHT45
# ============================================================

Current environment sensor:

SHT45-AD1B-R2

Purpose:

record:

temperature
humidity

for calibration metadata.

Do not position conceptually near hot TX drivers.

If sensor is remote:

use explicit connector/interface.

Review:

I2C pull-up voltage
connector
ESD if exposed
supply decoupling


# ============================================================
# 41. POWER ARCHITECTURE
# ============================================================

Create explicit power-tree sheet.

At minimum distinguish:

VIN

VDRV

+5V_A

+5V_D

+3V3_LOGIC

VREF_2V5

AGND

DGND

PGND

Every rail must document:

Source
Consumers
Expected Voltage
Estimated Current if known
Unknown Current if not known
Protection
Bulk Decoupling
Local Decoupling
Test Point
Power-Up Dependency


# ============================================================
# 42. POWER PROTECTION
# ============================================================

Review need for:

- reverse polarity
- fuse
- eFuse
- OVP
- UVLO
- TVS
- inrush
- bulk capacitance
- current limiting

Use existing BOM first.

Do not silently add expensive parts.

If BOM expansion is needed:

classify:

REQUIRED_CHANGE

OPTIONAL_IMPROVEMENT

DNP_TUNING

and report cost/design impact.


# ============================================================
# 43. GROUND STRATEGY
# ============================================================

Schematic intent:

PGND:
TX high-current return

AGND:
RX AFE / reference / ADC analog

DGND:
digital logic

However:

Do not create physically impossible isolated ground islands.

Document intended connection strategy.

Review goal:

TX switching current must not contaminate:

- RX input
- VREF
- ADC analog return

Schematic must contain notes for future PCB designer:

- sensitive return
- high-current return
- common reference
- joining concept

No PCB plane layout is allowed in this Stage.


# ============================================================
# 44. DECOUPLING QUALITY GATE
# ============================================================

For every IC:

verify manufacturer datasheet.

Especially:

AD7606B

OPA4192

REF5025

TMUX1574

SN74LVC595

SN74AXC8T245

SN74LVC244

TC4427A

SHT45

Do not use:

“全部随便放 100nF”

as design methodology.

For each power-sensitive device evaluate:

- 100 nF ceramic
- 1 µF
- 4.7 µF
- 10 µF
- bulk capacitance

according to datasheet and transient demand.

Document reasoning.


# ============================================================
# 45. TEST POINT STRATEGY
# ============================================================

Provide intentional TP nodes.

TX debug:

SER_DATA representative lanes

SER_SHIFT_CLK

SER_LATCH_CLK

TX_OUTPUT_DISABLE

TC4427 input

TC4427 output

VDRV


RX:

raw RX

after protection

after AC coupling

VREF-biased node

AFE Stage1 output

AFE Stage2 output

TMUX output

ADC input


ADC:

CONVST

BUSY

CS

SCLK

SDI

DOUTA
DOUTB
DOUTC
DOUTD


Power:

VIN
VDRV
5VA
5VD
3V3
VREF2V5
AGND
DGND
PGND

Do not place unnecessary high-capacitance test structures
on sensitive nodes.


# ============================================================
# 46. FAIL-SAFE ANALYSIS
# ============================================================

For every critical control:

determine state during:

- FPGA reset
- FPGA unconfigured
- clock loss
- power ramp
- cable disconnected
- translator unpowered
- driver unpowered
- partial power
- software fault

Critical desired behavior:

TX:
OFF

RX:
BLANK / protected

Driver:
DISABLED

No uncontrolled acoustic emission.


# ============================================================
# 47. COMPONENT LIBRARY POLICY
# ============================================================

For 嘉立创EDA专业版:

Prefer exact MPN.

For every critical part verify:

Manufacturer

MPN

Symbol

Pin Number

Pin Name

Package

Power Pins

NC Pins

Exposed Pad

Polarity

Do not trust EDA library blindly.

Datasheet vs library pin audit is mandatory.


# ============================================================
# 48. LCSC / JLCEDA LIBRARY MAPPING
# ============================================================

If exact part exists:

record:

MPN
JLCEDA device name
LCSC C-number

only after verification.

If not verified:

LCSC_ID_UNVERIFIED

Do not invent a C-number.

If custom symbol is required:

create project-specific symbol
inside:

PCB\V1\device

with source and review record.


# ============================================================
# 49. TCT40 LIBRARY / PACKAGE
# ============================================================

For TCT40 schematic symbol:

show:

positive terminal

negative / shell relationship

TX / RX variant clearly.

Provisional mechanical metadata:

Body:
~9.9 mm

Pitch:
5.00 mm

Pin:
~0.7 mm

Possible finished hole candidate:

0.9–1.0 mm

Possible pad candidate:

1.8–2.0 mm

BUT:

these are provisional.

Since this Stage does not produce PCB:

no manufacturing footprint freeze is required.

Mark:

FOOTPRINT_PROVISIONAL

until purchased batch measurement.


# ============================================================
# 50. CHANNEL NAMING
# ============================================================

Use deterministic naming.

UPPER TX:

TX_U00
...
TX_U63

LOWER TX:

TX_L00
...
TX_L63

RX:

RX_U0
RX_U1
RX_U2
RX_U3

RX_L0
RX_L1
RX_L2
RX_L3

Do not rely only on arbitrary reference numbers.


# ============================================================
# 51. COMPLETE CHANNEL MAP
# ============================================================

Generate:

PCB\V1\log\channel_map\TX_CHANNEL_MAP.csv

and documentation copy under v2/docs/hardware if appropriate.

Every TX maps:

Logical TX
→ Coordinate
→ Serializer Lane
→ SN74LVC595 Ref
→ Q Output
→ Buffer/Translator if any
→ TC4427 Ref
→ TC4427 Channel
→ TCT40 Ref
→ Upper/Lower Array


Every RX maps:

Logical RX
→ Coordinate
→ TCT40-R Ref
→ Protection
→ AFE Stage1
→ AFE Stage2
→ TMUX
→ AD7606B Input
→ DOUT Decode
→ Software Channel


# ============================================================
# 52. AUTOMATED CONNECTIVITY CHECK
# ============================================================

Where technically possible,
write scripts/checkers to verify:

128 TX channels exactly once.

8 RX exactly once.

32 serializer lanes.

4 active outputs/lane.

32 × 4 = 128.

64 TC4427A dual channels
= 128 driver channels.

No duplicate TX.

No missing TX.

No RX duplicate.

ADC channel order exact.

No orphan active driver input.

No accidental active unused output.


# ============================================================
# 53. CURRENT BOM
# ============================================================

Canonical BOM must be read from:

v2/hardware/bom/BOM_MASTER.xlsx

or current canonical replacement.

Historical known baseline approximately includes:

128 × TCT40-10T

8 × TCT40-10R1

64 × TC4427A

32 × SN74LVC595A

8 × SN74AXC8T245

SN74LVC244

4 × OPA4192

TMUX1574

1 × AD7606B

REF5025

1 × SHT45

This list is orientation only.

Repository BOM wins.

Do not silently modify approved part family.


# ============================================================
# 54. BOM AUDIT
# ============================================================

Run:

SCHEMATIC_BOM_AUDIT

Compare:

schematic quantities

vs

canonical BOM

Classify discrepancies:

ERROR

REQUIRED_CHANGE

DNP

PROVISIONAL

NOT_INSTALLED

OPTIONAL

Save:

PCB\V1\log\bom_audit\


# ============================================================
# 55. JLCEDA GUI EXECUTION
# ============================================================

If Codex has real GUI / computer-use access:

actually open:

嘉立创EDA专业版

and operate the real application.

Create/open formal project under:

PCB\V1\project

Perform:

- create sheets
- place symbols
- connect nets
- create hierarchical ports
- assign net labels
- annotate
- run real schematic checks
- save native project
- reopen project
- verify persistence

No fake GUI claims.

If GUI cannot be controlled:

return:

JLCEDA_GUI_ACCESS_BLOCKED

Do NOT pretend the project exists.

In that case generate the maximum usable schematic design package:

- full connection matrix
- sheet plan
- netlist specification
- symbol requirements
- component list
- channel map
- power tree
- pin maps
- design calculations
- importable artifacts if officially supported

But do not fabricate proprietary JLCEDA file formats.


# ============================================================
# 56. ERC / SCHEMATIC RULE CHECK
# ============================================================

Run actual 嘉立创EDA schematic ERC.

If the software exposes additional schematic DRC/rule checks,
run them too.

IMPORTANT:

Because no PCB is generated,
do NOT create a PCB merely to obtain “PCB DRC PASS”.

Do not falsely report:

PCB DRC PASS

when no PCB exists.

Check at minimum:

- unconnected required pin
- floating input
- output-output conflict
- power input missing source
- hidden power pins
- supply polarity
- duplicate RefDes
- duplicated labels
- isolated nets
- wrong hierarchy connection
- bus mismatch
- NC misuse
- open collector / open drain pull-up
- active-low correctness


# ============================================================
# 57. ERC WARNING POLICY
# ============================================================

Target:

ERC ERROR = 0

Warnings:

must NOT be globally suppressed.

Every warning classified:

TRUE_ERROR

INTENTIONAL_NC

INTENTIONAL_DNP

TESTPOINT_ONLY

HIERARCHY_EXPECTED

EDA_FALSE_POSITIVE

UNRESOLVED

Create:

PCB\V1\log\erc\SCHEMATIC_ERC_WAIVERS.md

Any unresolved warning affecting function:

Stage result cannot be READY_FOR_REVIEW.


# ============================================================
# 58. HIGH-QUALITY PCB READINESS REVIEW
# ============================================================

ERC=0 is NOT sufficient.

Perform:

PCB_READINESS_SCHEMATIC_REVIEW

Even though no PCB is drawn.

Review schematic from future PCB implementation perspective.

Check:

- power partition
- analog/digital/power boundaries
- return-current feasibility
- decoupling topology
- ADC reference topology
- sensitive AFE path
- high-current TX path
- connector topology
- clock fanout
- serializer source termination provisions
- testability
- debug access
- component placement feasibility
- thermal clustering risks
- channel replication
- future routing feasibility
- excessive fanout
- overconstrained pinout
- connector pin availability
- ground pins in connectors
- supply pins in connectors

Goal:

The schematic should enable a good PCB,
not merely be electrically connected.


# ============================================================
# 59. MODULE QUALITY REVIEW
# ============================================================

Review every module with this template:

Module Name

Purpose

Inputs

Outputs

Supply

Ground Domain

Signal Levels

Current / Load

Power-Up State

Reset State

Fail-Safe State

Protection

Decoupling

Filtering

Timing

DNP/Tuning

Test Points

Datasheet Compliance

Open Risks

Fabrication Dependencies


Mandatory modules:

FPGA_CORE_INTERFACE

POWER_INPUT_PROTECTION

POWER_REGULATION

LEVEL_TRANSLATION

TX_SERIAL_CONTROL

TX_CLOCK_BUFFERING

TX_DRIVER

TX_ARRAY

RX_TRANSDUCER_INPUT

RX_PROTECTION

RX_AFE_STAGE1

RX_AFE_STAGE2

RX_BLANKING

ADC_AD7606B

REFERENCE_BIAS

ENV_SENSOR

CONNECTORS

TEST_DEBUG


# ============================================================
# 60. SCHEMATIC VISUAL QUALITY
# ============================================================

原理图必须专业可读。

Rules:

Signal generally flows:

left → right

Power:

top → down where practical

Ground:

bottom

Avoid:

crossing wires
long spaghetti wires
random labels
dense component piles
hidden signals without documentation

Repeated channels:

use hierarchical repeated structure
or clear replicated blocks.

Every sheet must contain:

Title
Purpose
Major Inputs
Major Outputs
Page relationship


# ============================================================
# 61. CONNECTOR DESIGN
# ============================================================

Connector pages must clearly identify:

Pin Number

Signal

Direction

Voltage Domain

Ground/Power

FPGA Ball if applicable

Bank if applicable

Current confidence

Do not place important interface information
only in a text note separate from actual connector.


# ============================================================
# 62. ROBEI CONNECTOR SAFETY
# ============================================================

Do not freeze uncertain:

J3/J4/J5/J6 digital numbering.

Use confidence field:

CONFIRMED

HIGH_CONFIDENCE

PROVISIONAL

TBD

Any pin affected by B03:

must not be represented as manufacturer-confirmed.


# ============================================================
# 63. PH0 PROTOTYPE SUPPORT
# ============================================================

Even though no PCB is designed,
schematic must support future:

1 TX + 1 RX

and:

1 TX + 4 RX

qualification.

Measurements to support:

RX raw Vpp

RX RMS

noise

SNR

ring-down

recovery

frequency response

phase

group delay

TX output voltage

TX current

VDRV ripple


# ============================================================
# 64. OPEN PHYSICAL GATES
# ============================================================

Do not close these without physical evidence:

TCT40 batch:

- actual C
- resonance
- impedance
- Q
- polarity
- diameter
- pin dimensions
- maximum drive
- thermal behavior

RX:

- raw signal amplitude
- noise
- overload
- ring-down
- recovery
- phase
- group delay

Robei:

- VCCO34
- VCCO35
- connector numbering
- exact FPGA ordering code

Serializer:

- real 66 MHz timing

ADC:

- real source-synchronous DOUT timing

These remain:

FABRICATION_GATES


# ============================================================
# 65. B05 / B06 STATUS
# ============================================================

Manufacturer datasheet now establishes a real TCT40 baseline.

Therefore B06 should no longer be described as:

NO DATASHEET INFORMATION

Instead:

DATASHEET_BASELINE_ESTABLISHED
/
BATCH_QUALIFICATION_PENDING

But do not mark it fully resolved.

B05 physical levitation / force evidence remains open.


# ============================================================
# 66. B07 STATUS
# ============================================================

Real hardware phase references remain unresolved.

Physical calibration requires:

TX phase reference

RX phase/group delay

ADC timing reference

bank-to-bank gauge relationship

Synthetic calibration cannot close B07.


# ============================================================
# 67. SCHEMATIC DOCUMENTATION
# ============================================================

Create/update documentation such as:

v2/docs/hardware/SCHEMATIC_ARCHITECTURE.md

v2/docs/hardware/SCHEMATIC_DESIGN_RULES.md

v2/docs/hardware/SCHEMATIC_CHANNEL_MAP.md

v2/docs/hardware/SCHEMATIC_OPEN_ITEMS.md

v2/docs/hardware/ROBEI_ZYNQ7020_INTERFACE_REVIEW.md

Documents must match actual schematic.

Do not write aspirational features that are not actually connected.


# ============================================================
# 68. DEVICE DOCUMENTATION
# ============================================================

For each critical device,
store a device record under:

PCB\V1\device

Suggested fields:

Manufacturer

MPN

Function

Supply

Logic Level

Key Timing

Package

Symbol Source

JLCEDA Part

LCSC Part

Datasheet Revision

Datasheet Source

Pin Audit Result

Decoupling Requirements

Known Risk

Design Usage


# ============================================================
# 69. DESIGN CALCULATIONS
# ============================================================

Save engineering calculations under:

PCB\V1\log\calculations

At minimum:

- OPA4192 gain
- AFE bandwidth
- filter poles
- reference loading
- TCT40 impedance sanity check
- serializer timing
- logic-level compatibility
- power estimate
- ADC input headroom
- decoupling reasoning

Calculations must show:

equation
input
source
result
assumption
margin


# ============================================================
# 70. SEARCH FOR FAKE COMPLETION
# ============================================================

Before completing:

search:

TODO
FIXME
TBD
placeholder
stub
mock
fake
temporary
unconnected
not connected
DNP
TUNING

Every occurrence must be classified:

EXPECTED_TUNING

INTENTIONAL_DNP

OPEN_BLOCKER

UNRESOLVED_ERROR

TEMPORARY_WORK

No accidental TBD may remain hidden.


# ============================================================
# 71. CROSS-LAYER CONSISTENCY
# ============================================================

Verify:

RTL signal
=
hardware contract signal
=
schematic signal

Check:

clock polarity

reset polarity

blank polarity

OE polarity

serializer bit order

ADC bit order

ADC channel order

TX channel order

upper/lower bank order

If schematic reveals an actual RTL/interface contradiction:

DO NOT silently modify RTL.

Create:

INTERFACE_CONFLICT

and report for decision.


# ============================================================
# 72. SOFTWARE / RTL CHANGE BOUNDARY
# ============================================================

This is a schematic Stage.

Do not add unrelated software features.

Do not refactor RTL.

Software/RTL changes are only allowed if necessary to fix
a confirmed hardware-interface defect.

If change would alter:

protocol
architecture
timing
channel mapping

stop and request decision.


# ============================================================
# 73. PROJECT HYGIENE
# ============================================================

At Stage end check:

Root cleanliness

PCB/V1 structure

No temp files

No duplicate libraries

No duplicate PDFs

No autosave junk

No broken relative paths

No absolute path dependency where avoidable

No credentials

No incompatible binaries

No stale references


# ============================================================
# 74. JLCEDA REOPEN TEST
# ============================================================

After saving:

close project

reopen project from:

E:\Codex_project\AMD-SonoField-FPGA\PCB\V1\project

Verify:

- sheets present
- hierarchy intact
- symbols resolved
- custom devices resolved
- labels intact
- no missing library
- ERC still same result

This is mandatory if real GUI access exists.


# ============================================================
# 75. INDEPENDENT REVIEW PASSES
# ============================================================

Perform separate review passes:

PASS A:
Functional Connectivity

PASS B:
Electrical / Datasheet

PASS C:
Power / Ground

PASS D:
Analog Signal Integrity

PASS E:
Digital Timing / Levels

PASS F:
Safety / Power-Up

PASS G:
PCB-Readiness

PASS H:
BOM / Device Library

PASS I:
Naming / Documentation

A single ERC PASS is not enough.


# ============================================================
# 76. ACCEPTANCE CRITERIA
# ============================================================

Stage may return READY_FOR_REVIEW only if:

1.
Complete multi-sheet schematic exists.

2.
128 TX represented exactly.

3.
8 RX represented exactly.

4.
32 serializer lanes represented.

5.
TX driver mapping complete.

6.
ADC mapping exact.

7.
No unresolved critical connection error.

8.
ERC ERROR = 0.

9.
Every ERC WARNING reviewed.

10.
Net-label audit passes.

11.
BOM audit completes.

12.
Critical library pin audit completes.

13.
Power tree complete.

14.
Decoupling review complete.

15.
Ground intent documented.

16.
Fail-safe states reviewed.

17.
FPGA unknown facts are visible,
not guessed.

18.
B01/B03/B04/B05/B06/B07 are truthfully represented.

19.
No PCB has been generated.

20.
Project successfully saved under:

PCB\V1\project

21.
Logs stored under:

PCB\V1\log

22.
Devices stored under:

PCB\V1\device

23.
Repository synchronized.

24.
v1 frozen project version remains unchanged.

25.
Active version remains v2.


# ============================================================
# 77. FAILURE CONDITIONS
# ============================================================

Return:

BLOCKED

if:

- JLCEDA inaccessible
- required source files corrupt
- critical datasheet unavailable
- connector facts make schematic logically impossible
- exact required library cannot be created
- repository conflict prevents safe work


Return:

REVISE_REQUIRED

if:

- schematic exists but major technical flaw remains
- ERC critical warnings remain
- channel mapping incomplete
- power topology unsafe
- AFE unjustified
- timing calculation fails
- component mismatch exists


# ============================================================
# 78. GITHUB STATE UPDATE
# ============================================================

After actual successful work:

update as appropriate:

shared/PROJECT_STATE.json

shared/CURRENT_PLAN.md

shared/BLOCKERS.md

shared/HANDOFF.md

shared/ACCEPTANCE.md

CHANGELOG

AI-interaction-memory

Do not falsify:

AI-chat-memory synchronized

unless external ChatGPT history was actually imported.


# ============================================================
# 79. GIT COMMIT
# ============================================================

Use meaningful commits.

Example:

v2: schematic - add JLCEDA schematic revision V1

or:

v2: schematic - complete SonoField electrical architecture

Do not use:

update
final
final2
new
fix


# ============================================================
# 80. FINAL CODEX REPORT
# ============================================================

At completion report exactly:

PROJECT_ID

Project Name

Repository

Workspace

Branch

Active Project Version

Schematic Revision

Stage

Starting Commit

Ending Commit

JLCEDA Version

JLCEDA Access Status

Project Path

Log Path

Device Path

Number of Schematic Sheets

Total Components

TX Count

RX Count

Serializer Lane Count

TX Mapping Result

RX Mapping Result

ADC Mapping Result

BOM Audit

Library Pin Audit

ERC Errors

ERC Warnings

Warning Waivers

Net Audit Result

Power Review Result

AFE Review Result

Timing Review Result

PCB-Readiness Review Result

B01 Status

B03 Status

B04 Status

B05 Status

B06 Status

B07 Status

Open TBDs

Open DNPs

Fabrication Gates

Files Created

Files Modified

Evidence Paths

Git Commit

Git Push Verification

Limitations

Next Recommended Stage

Final Codex Status:

READY_FOR_REVIEW
or
BLOCKED
or
REVISE_REQUIRED


# ============================================================
# 81. FINAL STOP RULE
# ============================================================

Once:

- schematic complete
- real checks complete
- logs saved
- documentation synchronized
- GitHub pushed
- READY_FOR_REVIEW reached

STOP.

DO NOT automatically proceed to PCB.

DO NOT perform placement.

DO NOT perform routing.

DO NOT generate Gerber.

The user and ChatGPT must independently review
SCHEMATIC REVISION V1
before any PCB implementation is authorized.


# ============================================================
# 82. QUALITY PRINCIPLE
# ============================================================

The objective is NOT:

“画出一张能连通且 ERC 不报错的原理图。”

The objective is:

“在当前已知器件、软件、RTL、机械与声学约束下，
形成一套具有明确模块边界、正确网络标签、可靠电源体系、
合理模拟数字分区、真实器件依据、充分调试能力和未来 PCB 可实现性的
高质量 SonoField-FPGA 正式原理图。”

Quality priorities:

Correctness
>
Safety
>
Electrical Stability
>
Traceability
>
Testability
>
PCB Readiness
>
Maintainability
>
Visual Cleanliness

Do not trade correctness for apparent completion.

Do not weaken engineering rules for ERC PASS.

Do not guess unresolved physical facts.

Do not claim hardware validation without hardware evidence.