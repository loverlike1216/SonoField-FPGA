# 原厂依据索引

查询日期2026-10-11；完整下载SHA256/URL/状态在SOURCE_FETCH_MANIFEST.json，具体规格的保证/典型区别见ASSUMPTIONS_AND_UNKNOWNS。原始PDF不入Git。数据表正文版本与后附包装更新日期不同，按正文版本记录。

| 原厂文件 | 本轮实际版本、用途和定位 |
|---|---|
|[TPS3851](https://www.ti.com/lit/ds/symlink/tps3851.pdf)|SBVS300B RevB June2025；页3pin，4工作范围，5阈值/POR，6时序，7波形，17eq1/2，23后缀|
|[TC4427A](https://ww1.microchip.com/downloads/en/DeviceDoc/20001423J.pdf)|DS20001423J 2014；页2反相类型，3/4阈值/峰值/热/静态，应用/旁路章节；12V负载需测|
|[SN74LVC595A](https://www.ti.com/lit/ds/symlink/sn74lvc595a.pdf)|SCASE93A RevA October2025；§5.5页6电平/IOZ/Ioff，§5.7页8clock/pulse/setup/hold，应用OE/clear|
|[TPS54202](https://www.ti.com/lit/ds/symlink/tps54202.pdf)|RevC February2026；§5.5页5电气/fsw，§7.2.3页14–17 L/C/FB/电感电流/热；查完整补偿，不套0.6V|
|[TPS2663](https://www.ti.com/lit/ds/symlink/tps2663.pdf)|SLVSE94G RevG June2024；页7限流/2×脉冲/RON，页18eq2浪涌及SOA，页30eq8限流，页31UVLO/OVP梯形，布局/外部RCB FET|
|[AD7606C-16](https://www.analog.com/media/en/technical-documentation/data-sheets/ad7606c-16.pdf)|RevA；页6带宽/量程/供电，页15–17pin，页58/59应用连接，页60layout；REGCAP与REFCAPA/B区别|
|[OPA4192](https://www.ti.com/lit/ds/symlink/opa4192.pdf)|SBOS620E RevE Nov2015；供电/电气/输出摆幅、噪声/容性负载/应用。仅typ GBW/slew例，不作为生产AFE仿真|
|[TMUX1574](https://www.ti.com/lit/ds/symlink/tmux1574.pdf)|RevC；recommended input range、powered-off protection和应用章节，不能让未偏置RX负压任意进单供电开关|
|[REF50](https://www.ti.com/lit/ds/symlink/ref50.pdf)|RevO Oct2025；§6.3/6.5/8.4与outputcap，A/AI等级不同于E等级；原ref5025 symlink404已纠正并保留失败|
|[ADP7118](https://www.analog.com/media/en/technical-documentation/data-sheets/ADP7118.pdf)|RevH；页1–3电流/压差/误差，applications input/outputcap稳定/热；2.2µF与有效容量|
|[INA226](https://www.ti.com/lit/ds/symlink/ina226.pdf)|SBOS547C RevC Aug2026；页5±81.92mV和电气，register shunt scaling/地址/filter章节；20mΩ5A量程冲突|
|[TMP117](https://www.ti.com/lit/ds/symlink/tmp117.pdf)|SNOSD82D RevD Sep2022；electrical/alert/address/应用；仅遥测不作为独立热点比较器替身|
|[SN74AXC8T245](https://www.ti.com/lit/ds/symlink/sn74axc8t245.pdf)|SCES875C RevC Jan2024；§7.3 Ioff/isolating行为，control DIR/OE参考VCCA，应用上电；必须审实际完整电源组合|
|[TCA9548A](https://www.ti.com/lit/ds/symlink/tca9548a.pdf)|SCPS207H RevH Sep2024；reset/地址/总线特性/应用；100kHz/one-hot是当前合约；内RESET恢复实际未接|
|[STUSB4500L](https://www.st.com/resource/en/datasheet/stusb4500l.pdf)|DS13102 Rev6 Feb2022；原厂web实际读取31页，页1/2/4 CC广告/default1.5A3A/PMOS路径/内部regcap；本地HTTP567未下载，不虚构PDF hash|
|[PJ-002BH](https://www.sameskydevices.com/product/resource/pj-002bh.pdf)|原厂Rev1.08 Sep2024；页1 24V/5A/30mΩ/温度，机械中心pin2.5及mating深度9.5mm|
|[GST60A](https://www.meanwell.com/Upload/PDF/GST60A/GST60A-SPEC.PDF) / [GST40A](https://www.meanwell.com/Upload/PDF/GST40A/GST40A-SPEC.PDF)|2026-04-03；电流/工作条件、DCplug optionalP1M/P1L尺寸表；具体插头极性/连续载流需订单/实物核验|
|[Littelfuse SMBJ](https://m.littelfuse.com/~/media/electronics/datasheets/tvs_diodes/littelfuse_tvs_diode_smbj_datasheet.pdf.pdf)|原厂web表读；SMBJ12A19.9V、SMBJ20A32.4V指定脉冲clamp；未据此选定我方TVS/能量|
|[Nexperia AHC/AHCT595](https://assets.nexperia.com/documents/data-sheet/74AHC_AHCT595.pdf)|Rev9 May2025；用于审开源主图器件/3.3V疑点，不替换我方LVC595|

屏蔽功率电感DCR/Isat/Irms、MLCC偏压、保险I²t、MOS SOA实际厂商料未选择，因此曲线/额定UNKNOWN；未把“没有品牌MPN要求”解释成不需要偏压/故障额定证据。所有待定件给出筛选规格和计算边界，而非伪造现货或供货保证。
