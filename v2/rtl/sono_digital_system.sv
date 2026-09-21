`timescale 1ns/1ps
// Register-bus integration, deliberately independent of PS, pins and a board PLL.
module sono_digital_system #(
 parameter integer CLOCK_HZ=132000000, POWER_WAIT_CYCLES=2*CLOCK_HZ+1
)(input wire clk,rst_n,hardware_enable,
 input wire bus_valid,bus_write,input wire[7:0] bus_address,input wire[31:0] bus_wdata,
 output reg[31:0] bus_rdata,output wire bus_ready,output reg bus_error,
 input wire adc_busy,input wire[3:0] adc_dout,
 output wire adc_reset,adc_convst,adc_cs_n,adc_sclk,adc_sdi,
 output wire[1:0] rx_blank,output wire[31:0] serial_data,
 output wire shift_clock,latch_clock,output wire output_disable,
 output wire[127:0] commanded_waveform,output wire irq);
 `include "registers.svh"
 initial if(CLOCK_HZ!=SYS_CLOCK_HZ)$fatal(1,"Regenerate and validate ADC timing profile for a different system clock");
 reg[31:0] cfg[0:27];reg[2:0] mode;reg software_enable;
 reg start,abort,ack,map_write,map_commit;reg[63:0] time_now;
 (* ASYNC_REG="TRUE" *) reg[1:0] reset_sync,enable_sync;
 wire core_rst=reset_sync[1];
 always @(posedge clk or negedge rst_n)
  if(!rst_n)reset_sync<=0;
  else reset_sync<={reset_sync[0],1'b1};
 always @(posedge clk or negedge rst_n or negedge hardware_enable)
  if(!rst_n||!hardware_enable)enable_sync<=0;
  else enable_sync<={enable_sync[0],1'b1};
 wire adc_ready,adc_error,adc_idle,frame_valid;
 wire[127:0] frame;wire[63:0] frame_timestamp;
 wire sample_request,burst_start,capture_ready,scan_done,scan_error,scan_active;
 wire[6:0] selected_tx;wire[7:0] sequence_number;wire[10:0] frame_count;
 wire[63:0] first_timestamp,burst_timestamp;wire[3:0] scan_state;
 wire[31:0] buffer_data;
 wire burst_active,burst_done,burst_wave;
 wire normal=(mode==MODE_NORMAL_FIELD||mode==MODE_VALIDATE_FIELD);
 wire calibrating=(mode>=MODE_CALIBRATE_GEOMETRY&&mode<=MODE_CALIBRATE_PHASE);
 wire serializer_fault,map_error;
 reg map_fault_latched;
 always @(posedge clk or negedge core_rst)
  if(!core_rst)map_fault_latched<=0;else if(map_error)map_fault_latched<=1;
 wire fault=adc_error||scan_error||bus_error||serializer_fault||map_error||map_fault_latched;
 wire kill=!software_enable||!enable_sync[1]||fault||mode==MODE_SAFE_DISABLED;
 wire cal_abort=abort||kill||!calibrating;
 ad7606b_if #(.CLOCK_HZ(CLOCK_HZ),.POWER_WAIT_CYCLES(POWER_WAIT_CYCLES)) adc(
  .clk(clk),.rst_n(core_rst),.sample_request(sample_request&&!cal_abort),.time_now(time_now),
  .busy_async(adc_busy),.dout(adc_dout),.adc_reset(adc_reset),.convst(adc_convst),
  .cs_n(adc_cs_n),.sclk(adc_sclk),.sdi(adc_sdi),.ready(adc_ready),.error(adc_error),
  .frame_valid(frame_valid),.frame(frame),.frame_timestamp(frame_timestamp),.idle(adc_idle));
 calibration_scheduler #(.DEPTH(SYS_BUFFER_DEPTH)) scheduler(
  .clk(clk),.rst_n(core_rst),.start(start&&calibrating&&!kill),.abort(cal_abort),.ack(ack),
  .adc_ready(adc_ready),.adc_idle(adc_idle),.adc_error(adc_error),.frame_valid(frame_valid),
  .frame(frame),.frame_timestamp(frame_timestamp),.time_now(time_now),
  .sample_period(cfg[REG_SAMPLE_PERIOD/4]),.pre_samples(cfg[REG_PRE_SAMPLES/4]),
  .main_samples(cfg[REG_MAIN_SAMPLES/4]),.tail_samples(cfg[REG_TAIL_SAMPLES/4]),
  .settle_cycles(cfg[REG_SETTLE_CYCLES/4]),.guard_cycles(cfg[REG_GUARD_CYCLES/4]),
  .first_tx(cfg[REG_FIRST_TX/4][6:0]),.scan_count(cfg[REG_SCAN_COUNT/4][7:0]),
  .burst_active(burst_active),.burst_done(burst_done),.read_address(cfg[REG_BUFFER_ADDR/4][11:0]),
  .read_data(buffer_data),.sample_request(sample_request),.burst_start(burst_start),
  .capture_ready(capture_ready),.done(scan_done),.error(scan_error),.selected_tx(selected_tx),
  .capture_sequence(sequence_number),.frame_count(frame_count),.first_timestamp(first_timestamp),
  .burst_timestamp(burst_timestamp),.rx_blank(rx_blank),.active(scan_active),.state_debug(scan_state));
 burst_generator #(.CLOCK_HZ(CLOCK_HZ)) burst(.clk(clk),.rst_n(core_rst),.start(burst_start),
  .abort(cal_abort),.frequency(cfg[REG_FREQUENCY/4]),.cycles(cfg[REG_BURST_CYCLES/4]),
  .start_phase(cfg[REG_START_PHASE/4][7:0]),.active(burst_active),.done(burst_done),.waveform(burst_wave));
 reg[31:0] carrier_acc;reg[7:0] previous_phase;reg boundary;
 wire[32:0] next_acc={1'b0,carrier_acc}+cfg[REG_FREQUENCY/4];
 wire[39:0] phase_scaled={carrier_acc,8'b0};
 wire[7:0] master_phase=phase_scaled/CLOCK_HZ;
 wire tick=master_phase!=previous_phase;
 always @(posedge clk or negedge core_rst)
  if(!core_rst)begin carrier_acc<=0;previous_phase<=0;boundary<=0;end
  else begin
   previous_phase<=master_phase;boundary<=next_acc>=CLOCK_HZ;
   if(next_acc>=CLOCK_HZ)carrier_acc<=next_acc-CLOCK_HZ;else carrier_acc<=next_acc;
  end
 wire write_ready,pending,commit_ack,map_valid;
 wire[1023:0] effective;wire[127:0] mask,normal_wave;
 phase_bank bank(.clk(clk),.rst_n(core_rst),.period_boundary(boundary),
  .write_valid(map_write),.channel_enable(cfg[REG_MAP_DATA/4][16]),
  .write_channel(cfg[REG_MAP_CHANNEL/4][6:0]),.requested_phase(cfg[REG_MAP_DATA/4][7:0]),
  .calibration_phase(cfg[REG_MAP_DATA/4][15:8]),.commit(map_commit),.write_ready(write_ready),
  .pending(pending),.commit_ack(commit_ack),.command_error(map_error),.active_valid(map_valid),
  .effective_phase(effective),.active_mask(mask));
 channel_waveform wave(.master_phase(master_phase),.effective_phase(effective),.active_mask(mask),.waveform(normal_wave));
 assign commanded_waveform=kill?128'b0:(normal?(map_valid?normal_wave:128'b0):
                           (calibrating&&burst_wave?(128'b1<<selected_tx):128'b0));
 wire frame_done,serial_busy;
 serializer serial(.clk(clk),.rst_n(core_rst),.start(tick),.waveform(commanded_waveform),
  .serial_data(serial_data),.shift_clock(shift_clock),.latch_clock(latch_clock),
  .busy(serial_busy),.frame_done(frame_done),.overrun(serializer_fault));
 reg frame_armed,published;reg[63:0] tx_enable_timestamp;
 always @(posedge clk or negedge core_rst)
  if(!core_rst)begin frame_armed<=0;published<=0;tx_enable_timestamp<=0;end
  else begin
   if(tick)frame_armed<=!kill && ((normal&&map_valid)||(calibrating&&burst_active));
   if(kill)published<=0;else if(frame_done)begin
    published<=frame_armed;
    if(frame_armed&&!published&&calibrating)tx_enable_timestamp<=time_now;
   end
  end
 // External hardware kill bypasses synchronizers for immediate disable; release is synchronous.
 assign output_disable=!rst_n||!hardware_enable||kill||!published;
 assign irq=capture_ready||scan_done||fault;
 assign bus_ready=bus_valid;
 integer i;
 always @(posedge clk or negedge core_rst)begin
  if(!core_rst)begin
   mode<=MODE_SAFE_DISABLED;software_enable<=0;start<=0;abort<=0;ack<=0;
   map_write<=0;map_commit<=0;bus_error<=0;time_now<=0;
   for(i=0;i<28;i=i+1)cfg[i]<=0;
   cfg[REG_FREQUENCY/4]<=SYS_CARRIER_HZ;cfg[REG_BURST_CYCLES/4]<=SYS_BURST_CYCLES;
   cfg[REG_FIRST_TX/4]<=64;cfg[REG_SCAN_COUNT/4]<=128;cfg[REG_SAMPLE_PERIOD/4]<=SYS_ADC_PERIOD;
   cfg[REG_PRE_SAMPLES/4]<=SYS_PRE_SAMPLES;cfg[REG_MAIN_SAMPLES/4]<=SYS_MAIN_SAMPLES;cfg[REG_TAIL_SAMPLES/4]<=SYS_TAIL_SAMPLES;
   cfg[REG_SETTLE_CYCLES/4]<=SYS_SETTLE_CYCLES;cfg[REG_GUARD_CYCLES/4]<=SYS_GUARD_CYCLES;
  end else begin
   time_now<=time_now+1;start<=0;abort<=0;ack<=0;map_write<=0;map_commit<=0;
   if(fault)begin software_enable<=0;mode<=MODE_SAFE_DISABLED;end
   if(bus_valid&&bus_write)begin
    if(bus_address[1:0]!=0)bus_error<=1;
    else case(bus_address)
     REG_CONTROL:begin software_enable<=bus_wdata[0];start<=bus_wdata[1];abort<=bus_wdata[2];
      if(bus_wdata[2])begin software_enable<=0;mode<=MODE_SAFE_DISABLED;end end
     REG_MODE:if(!software_enable&&!scan_active&&!capture_ready&&bus_wdata<=5)mode<=bus_wdata[2:0];else bus_error<=1;
     REG_MAP_CHANNEL:if(bus_wdata<128)cfg[REG_MAP_CHANNEL/4]<=bus_wdata;else bus_error<=1;
     REG_MAP_DATA:cfg[REG_MAP_DATA/4]<=bus_wdata;
     REG_MAP_WRITE:map_write<=1;
     REG_MAP_COMMIT:map_commit<=1;
     REG_BUFFER_ADDR:if(bus_wdata<4096)cfg[REG_BUFFER_ADDR/4]<=bus_wdata;else bus_error<=1;
     REG_ACK_CAPTURE:ack<=bus_wdata[0];
     REG_FREQUENCY:if(mode==0&&bus_wdata>=38500&&bus_wdata<=41500)cfg[REG_FREQUENCY/4]<=bus_wdata;else bus_error<=1;
     REG_FIRST_TX:if(mode==0&&bus_wdata<128)cfg[REG_FIRST_TX/4]<=bus_wdata;else bus_error<=1;
     REG_SCAN_COUNT:if(mode==0&&bus_wdata>0&&bus_wdata<=128)cfg[REG_SCAN_COUNT/4]<=bus_wdata;else bus_error<=1;
     REG_SAMPLE_PERIOD:if(mode==0&&bus_wdata>=165&&bus_wdata<=132000)cfg[REG_SAMPLE_PERIOD/4]<=bus_wdata;else bus_error<=1;
     REG_START_PHASE:if(mode==0&&bus_wdata<256)cfg[REG_START_PHASE/4]<=bus_wdata;else bus_error<=1;
     REG_BURST_CYCLES:if(mode==0&&bus_wdata>0&&bus_wdata<=SYS_BUFFER_DEPTH)cfg[REG_BURST_CYCLES/4]<=bus_wdata;else bus_error<=1;
     REG_PRE_SAMPLES,REG_MAIN_SAMPLES,REG_TAIL_SAMPLES:
      if(mode==0&&bus_wdata<=SYS_BUFFER_DEPTH)cfg[bus_address/4]<=bus_wdata;else bus_error<=1;
     REG_SETTLE_CYCLES,REG_GUARD_CYCLES:
      if(mode==0)cfg[bus_address/4]<=bus_wdata;else bus_error<=1;
     default:bus_error<=1;
    endcase
   end
  end
 end
 always @* begin
  bus_rdata=0;
  if(bus_address[1:0]==0)case(bus_address)
   REG_CONTROL:bus_rdata={31'b0,software_enable};
   REG_STATUS:bus_rdata={24'b0,adc_idle,map_valid,fault,scan_done,capture_ready,scan_active,adc_ready,software_enable};
   REG_MODE:bus_rdata={29'b0,mode};
   REG_BUFFER_DATA:bus_rdata=buffer_data;
   REG_FRAME_COUNT:bus_rdata={21'b0,frame_count};
   REG_CAPTURE_TX:bus_rdata={25'b0,selected_tx};
   REG_CAPTURE_SEQ:bus_rdata={24'b0,sequence_number};
   REG_TIMESTAMP_LO:bus_rdata=first_timestamp[31:0];
   REG_TIMESTAMP_HI:bus_rdata=first_timestamp[63:32];
   REG_BURST_TIMESTAMP_LO:bus_rdata=burst_timestamp[31:0];
   REG_BURST_TIMESTAMP_HI:bus_rdata=burst_timestamp[63:32];
   REG_TX_ENABLE_TIMESTAMP_LO:bus_rdata=tx_enable_timestamp[31:0];
   REG_TX_ENABLE_TIMESTAMP_HI:bus_rdata=tx_enable_timestamp[63:32];
   REG_MAP_STATUS:bus_rdata={28'b0,map_valid,commit_ack,pending,write_ready};
   REG_ERROR:bus_rdata={23'b0,scan_state,map_fault_latched,serializer_fault,bus_error,scan_error,adc_error};
   default:if(bus_address/4<28)bus_rdata=cfg[bus_address/4];
  endcase
 end
endmodule
