`timescale 1ns/1ps
module tb_calibration;
 `include "registers.svh"
 reg clk=0;always #3.787878788 clk=~clk;
 reg rst_n=0,hardware_enable=0,bus_valid=0,bus_write=0;
 reg[7:0] bus_address=0;reg[31:0] bus_wdata=0;
 wire[31:0] bus_rdata;wire bus_ready,bus_error;
 wire adc_reset,convst,cs_n,sclk,sdi,busy;wire[3:0] dout;reg hold_busy=0;
 wire[1:0] blank;wire[31:0] serial;wire shift,latch,oe,irq,configured;
 wire[127:0] wave;
 sono_digital_system #(.POWER_WAIT_CYCLES(32)) dut(.clk(clk),.rst_n(rst_n),.hardware_enable(hardware_enable),
  .bus_valid(bus_valid),.bus_write(bus_write),.bus_address(bus_address),.bus_wdata(bus_wdata),
  .bus_rdata(bus_rdata),.bus_ready(bus_ready),.bus_error(bus_error),.adc_busy(busy),.adc_dout(dout),
  .adc_reset(adc_reset),.adc_convst(convst),.adc_cs_n(cs_n),.adc_sclk(sclk),.adc_sdi(sdi),
  .rx_blank(blank),.serial_data(serial),.shift_clock(shift),.latch_clock(latch),.output_disable(oe),
  .commanded_waveform(wave),.irq(irq));
 ad7606b_model adc(.reset(adc_reset),.convst(convst),.cs_n(cs_n),.sclk(sclk),.sdi(sdi),
  .hold_busy(hold_busy),.busy(busy),.dout(dout),.configured(configured));
 task write_reg(input[7:0] address,input[31:0] data);
  begin @(negedge clk);bus_valid=1;bus_write=1;bus_address=address;bus_wdata=data;
   @(negedge clk);bus_valid=0;bus_write=0;end
 endtask
 integer n,j,k,fd,seen,burst_ticks,scan_seen;
 reg[63:0] previous_stamp;
 reg[127:0] expected;
 reg[31:0] before_word;
 reg checking=0;
 reg[16:0] calibrated_map[0:127];
 reg[31:0] calibrated_frequency[0:0];
 reg[63:0] normal_period_start;
 initial begin #20000000;$fatal(1,"CAL timeout");end
 always @(posedge clk)if(rst_n&&checking)begin
  if(dut.fault)$fatal(1,"Unexpected integrated fault %h",dut.bus_rdata);
  if(dut.calibrating && wave!=0 && wave!=(128'b1<<dut.selected_tx))$fatal(1,"More than selected TX driven");
  if(dut.calibrating && !dut.burst_active && !oe)$fatal(1,"Stale output permit outside calibration burst");
  if(dut.scan_state>=1&&dut.scan_state<=3 && blank!=(dut.selected_tx>=64?2'b10:2'b01))$fatal(1,"Wrong RX blank direction");
  if(dut.burst_active)burst_ticks=burst_ticks+1;
  if(dut.frame_valid)begin
   if(dut.frame!==adc.vectors[seen%1024])$fatal(1,"ADC ordering/data mismatch frame %0d",seen);
   if(seen>0 && dut.sequence_number==0 && dut.frame_count>0 && dut.frame_timestamp-previous_stamp!=dut.cfg[REG_SAMPLE_PERIOD/4])
    $fatal(1,"Nonuniform conversion timestamps");
   previous_stamp=dut.frame_timestamp;seen=seen+1;
  end
 end
 initial begin
  seen=0;burst_ticks=0;previous_stamp=0;
  $readmemh("calibration_map.hex",calibrated_map);
  $readmemh("calibration_frequency.hex",calibrated_frequency);
  repeat(5)@(negedge clk);
  if(oe!==1||wave!==0)$fatal(1,"Reset not safe");
  rst_n=1;hardware_enable=1;
  wait(dut.adc_ready);if(!configured)$fatal(1,"Configuration not verified");
  $display("PASS CAL-TB13 safe OE during reset and verified ADC configuration");checking=1;
  write_reg(REG_SCAN_COUNT,1);write_reg(REG_SETTLE_CYCLES,20);write_reg(REG_GUARD_CYCLES,20);
  write_reg(REG_MODE,MODE_CALIBRATE_GEOMETRY);write_reg(REG_CONTROL,3);
  wait(dut.capture_ready);@(negedge clk);
  if(dut.frame_count!=1024||dut.selected_tx!=64||seen!=1024)$fatal(1,"Full capture size/order");
  if(burst_ticks!=52800)$fatal(1,"Burst cycle count %0d",burst_ticks);
  if(dut.burst_timestamp-dut.first_timestamp!=32*165)$fatal(1,"Pretrigger timestamp");
  $display("PASS CAL-TB01 burst length / frequency; CAL-TB07 BUSY timing; CAL-TB08 frame capture; CAL-TB09 8-channel ordering");
  fd=$fopen("adc_roundtrip.hex","w");
  for(n=0;n<1024;n=n+1)begin
   expected=adc.vectors[n];
   for(j=0;j<4;j=j+1)begin
    write_reg(REG_BUFFER_ADDR,n*4+j);@(negedge clk);bus_address=REG_BUFFER_DATA;#1;
    if(bus_rdata!==expected[j*32+:32])$fatal(1,"Host readback frame %0d word %0d",n,j);
    $fdisplay(fd,"%08x",bus_rdata);
   end
  end
  $fclose(fd);
  before_word=dut.scheduler.memory[0][31:0];repeat(500)@(negedge clk);
  if(!dut.capture_ready||dut.scheduler.memory[0][31:0]!==before_word||seen!=1024)$fatal(1,"Overwrite before ACK");
  $display("PASS CAL-TB10 capture-buffer boundaries and backpressure; CAL-TB15 injected-vector exact comparison");
  write_reg(REG_ACK_CAPTURE,1);wait(dut.scan_done);write_reg(REG_CONTROL,4);repeat(5)@(negedge clk);
  // All 128 TX selections, each opposing four RX; shorter legal one-cycle captures.
  write_reg(REG_BURST_CYCLES,1);write_reg(REG_PRE_SAMPLES,2);write_reg(REG_MAIN_SAMPLES,24);
  write_reg(REG_FREQUENCY,41500);
  write_reg(REG_TAIL_SAMPLES,6);write_reg(REG_SCAN_COUNT,128);
  write_reg(REG_MODE,MODE_CALIBRATE_PHASE);write_reg(REG_CONTROL,3);
  for(n=0;n<128;n=n+1)begin
   wait(dut.capture_ready);@(negedge clk);
   if(dut.selected_tx!=((64+n)%128)||dut.sequence_number!=n||dut.frame_count!=32)$fatal(1,"Scan ordering %0d",n);
   write_reg(REG_ACK_CAPTURE,1);wait(!dut.capture_ready);
  end
  wait(dut.scan_done);
  $display("PASS CAL-TB02 single TX; CAL-TB03 64-channel scan order; CAL-TB04 lower-to-upper; CAL-TB05 upper-to-lower; CAL-TB06 RX blank state");
  write_reg(REG_CONTROL,4);repeat(5)@(negedge clk);
  // Lower acquisition rate is runtime configurable while safe.
  write_reg(REG_SAMPLE_PERIOD,330);write_reg(REG_SCAN_COUNT,1);
  write_reg(REG_FREQUENCY,38500);
  write_reg(REG_MODE,MODE_CHARACTERIZE_TX);write_reg(REG_CONTROL,3);
  wait(dut.capture_ready);write_reg(REG_ACK_CAPTURE,1);wait(dut.scan_done);
  $display("PASS CAL-TB14 frequency sweep 38500/40000/41500 Hz and 400/800 kSPS");
  write_reg(REG_CONTROL,4);repeat(5)@(negedge clk);
  write_reg(REG_FREQUENCY,calibrated_frequency[0]);
  for(k=0;k<128;k=k+1)begin
   write_reg(REG_MAP_CHANNEL,k);write_reg(REG_MAP_DATA,calibrated_map[k]);write_reg(REG_MAP_WRITE,1);
  end
  write_reg(REG_MAP_COMMIT,1);wait(dut.commit_ack);
  if(!dut.map_valid)$fatal(1,"Map not active");
  for(k=0;k<128;k=k+1)
   if(dut.effective[k*8+:8]!==((calibrated_map[k][7:0]+calibrated_map[k][15:8])&8'hff))$fatal(1,"Calibrated phase sum %0d",k);
  write_reg(REG_MODE,MODE_NORMAL_FIELD);write_reg(REG_CONTROL,1);wait(!oe);
  @(posedge dut.boundary);normal_period_start=dut.time_now;
  @(posedge dut.boundary);
  if(dut.time_now-normal_period_start<SYS_CLOCK_HZ/calibrated_frequency[0] ||
     dut.time_now-normal_period_start>SYS_CLOCK_HZ/calibrated_frequency[0]+1)$fatal(1,"Computed f_work not applied to field engine");
  repeat(5000)@(negedge clk);
  $display("PASS CAL-TB12 return to normal field with Python calibrated atomic phase map");
  hardware_enable=0;#1;if(!oe)$fatal(1,"Hardware kill not asynchronous");
  hardware_enable=1;write_reg(REG_CONTROL,4);
  write_reg(REG_MODE,MODE_CALIBRATE_GEOMETRY);write_reg(REG_CONTROL,3);
  wait(dut.burst_active);write_reg(REG_CONTROL,4);repeat(5)@(negedge clk);
  if(!oe||dut.burst_active||blank!=3)$fatal(1,"Abort not safe");
  $display("PASS CAL-TB11 abort during calibration and asynchronous hardware kill");
  checking=0;
  // Outstanding conversion drains; a missing BUSY completion then fails closed.
  wait(dut.adc_idle);hold_busy=1;
  write_reg(REG_MODE,MODE_CALIBRATE_GEOMETRY);write_reg(REG_CONTROL,3);
  wait(dut.adc_error);repeat(5)@(negedge clk);
  if(!oe||dut.mode!=0)$fatal(1,"ADC timeout not safe");
  $display("PASS additional ADC timeout and safe mode");
  write_reg(REG_FREQUENCY,99999);repeat(3)@(negedge clk);
  if(!bus_error||!oe)$fatal(1,"Invalid control not rejected");
  $display("PASS additional invalid register configuration fails closed");
  $display("PASS calibration digital system");$finish;
 end
endmodule
