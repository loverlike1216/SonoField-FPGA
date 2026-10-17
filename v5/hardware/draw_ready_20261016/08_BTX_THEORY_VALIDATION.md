# B-TX理论与工具验证

|方案|历史联合子模型记录（来自上一轮FINAL_REVIEW，非本轮重跑）|本轮采用判断|
|---|---|---|
|A|6PASS/84FAIL|两级LVC延迟/反射不闭合，淘汰|
|B|6PASS/83FAIL/1HOLD|直流端接损耗/参考供电负担，淘汰|
|C|7PASS/81FAIL/2HOLD|被动82Ω及旧主动变体不闭合，淘汰|
|D|5PASS/83FAIL/2HOLD|单纯移相/ODDR路径不闭合，淘汰|
|E|89PASS/1HOLD|研究次选；需额外相移/包装及完全复验，未放行|
|F|89PASS/1HOLD|保留流水思想；本轮重新设计为LVT128/256MHz唯一方案|
|G|90PASS但数字/针位FAIL|占用GND作差分负线，淘汰|

历史来源：../20261016_BTX_MultiSolution_Validation/FINAL_REVIEW.md。原始失败、非收敛、未通过的-1/-2尝试全部保留，不将子模型PASS改写成历史整机PASS。

终版F-LVT90/90联合工况通过。模型为OEM静态I/V、C_comp、封装RLC、有限边沿、两段传输线与厂家传播时延区间；不是完整合规动态IBIS。独立扣除两级器件路径4.8ns、线偏差0.5ns、FPGA差分预算0.5ns、抖动0.4ns；脉宽另扣两级rise/fall差4.4ns及0.4ns抖动。统一TX判据3.2/2.2/5.2/3.2ns没有降低。

最小建立/保持/脉宽/锁存间隔：5.751267/2.634361/5.204939/3.676019ns。最坏脉宽另用10ps/5ps步长复算，差异约0.379ps，保守脉宽5.205ns仍超过5.2ns。另一个细步长corner非收敛被保留MODEL_HOLD，不作为物理失败或PASS；没有声称所有corner完成细步长收敛证明。

实际native21完整PS/PL已综合、布局和布线，器件xc7z020clg400-2；WNS=+0.084ns，WHS=+0.039ns，DRC0。没有生成/下载bitstream。最终TX pad同corner最大路径散布0.165ns，小于0.5ns预算。全部内部端点有约束；异步健康/BUSY仅到明确同步器/故障锁存采用例外，128/256MHz之间没有全域falsepath。ADC输入按真实每16周期采样设置16/15多周期，44ns往返上界。慢控制使用20ns maxdelay，I2C自时钟；report_timing仍会列出无传统output_delay/部分I2Cinput_delay，详见约束覆盖报告，不将其冒充已做板级测量。

独立模拟器对128TX三载波各4096帧全位比较，真实UNISIM双MMCM检查period/2:1比例；安全缺帧、温度freshness、失败后旧健康不复活及生产BRAM前递均实际运行。

原先32并行支路后接大电容导致浪涌，已精简为四组1µF+32×100nF。原缺帧1000cycle保持许可的反例已由核心64cycle缺帧关断和阵列两路独立时钟WD修正。完整模型/日志均见scripts、candidate_rtl、results、logs。

Methodology提示保留：有意的异步故障/关断链有LUTAR警告；毛刺只会撤销许可，释放经过同步/资格检查。复制IOB对象有XDCV advisory，终版34个TX实际pad路径另逐个核对并落在4.5ns路径及0.5ns相对预算内。没有用关闭警告或豁免DRC伪造通过。
