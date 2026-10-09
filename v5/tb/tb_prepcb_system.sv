`timescale 1ns/1ps
// Actual top including supervisor, BRAM mailbox, AXI bridge and preserved core.
module tb_prepcb_system;
 reg clk=0;always #3.787879 clk=~clk;
 reg rst_n=0;reg[15:0] control=0;reg[7:0] health=8'hff;wire[31:0]status;
 reg[31:0]S_AXI_awaddr=0,S_AXI_wdata=0,S_AXI_araddr=0;
 reg S_AXI_awvalid=0,S_AXI_wvalid=0,S_AXI_bready=1,S_AXI_arvalid=0,S_AXI_rready=1;reg[3:0]S_AXI_wstrb=15;
 wire S_AXI_awready,S_AXI_wready,S_AXI_bvalid,S_AXI_arready,S_AXI_rvalid;
 wire[1:0]S_AXI_bresp,S_AXI_rresp;wire[31:0]S_AXI_rdata;
 wire bram_clk,bram_rst,bram_en;wire[3:0]bram_we;wire[31:0]bram_addr,bram_wrdata;reg[31:0]bram_rddata=0;
 wire adc_busy,adc_reset,adc_convst,adc_cs_n,adc_sclk,adc_sdi;wire[3:0]adc_dout;
 wire[1:0]rx_blank;wire[31:0]serial_data;wire shift_clock,latch_clock,output_disable,heartbeat,efuse_up,efuse_dn,irq,configured;
 prepcb_pl dut(.*);
 defparam dut.supervisor.MS_CYCLES=4,dut.supervisor.LONG_PRESS_MS=3,dut.supervisor.DEBOUNCE_MS=2,dut.supervisor.TIMEOUT_MS=10000;
 defparam dut.core.POWER_WAIT_CYCLES=32;
 defparam dut.core.native_system.INTERVAL_CYCLES=8192;
 ad7606b_model adc(.reset(adc_reset),.convst(adc_convst),.cs_n(adc_cs_n),.sclk(adc_sclk),.sdi(adc_sdi),.hold_busy(1'b0),.busy(adc_busy),.dout(adc_dout),.configured(configured));
 reg[31:0]memory[0:129];reg[31:0]words[0:1536001];integer n,loaded=0,acks=0,trace;
 reg[1023:0]previous=0;reg[127:0]previous_mask=0;
 reg expected_fault=0;
 always@(posedge clk)if(bram_en)bram_rddata<=memory[bram_addr/4];
 task ms(input integer count);begin repeat(count*4)@(negedge clk);end endtask
 task write_axi(input[31:0]addr,input[31:0]value);
 begin
  @(negedge clk);S_AXI_awaddr=addr;S_AXI_wdata=value;S_AXI_awvalid=1;S_AXI_wvalid=1;
  fork
   begin wait(S_AXI_awready);@(negedge clk);S_AXI_awvalid=0;end
   begin wait(S_AXI_wready);@(negedge clk);S_AXI_wvalid=0;end
  join
  wait(S_AXI_bvalid);if(S_AXI_bresp)$fatal(1,"AXI write rejected");@(negedge clk);
 end endtask
 always@(posedge clk)begin #1;
  if(rst_n&&dut.core_reset_n)begin
   if((dut.motion_underflow||dut.motion_overflow||dut.motion_invalid||dut.motion_timeout)&&!expected_fault)$fatal(1,"integrated queue fault");
   if((dut.core.native_system.digital.effective!==previous||dut.core.native_system.digital.mask!==previous_mask)&&!dut.core.native_system.digital.commit_ack)$fatal(1,"nonatomic integrated map");
   if(dut.motion_ack_pulse)begin
    if(dut.acknowledged_sequence!=acks||status[31:16]!=acks+1)$fatal(1,"PS/queue ACK conversion");
    for(integer c=0;c<128;c++)begin
     if(dut.core.native_system.digital.bank.active_requested[c]!==words[1+acks*128+c][7:0]||dut.core.native_system.digital.bank.active_calibration[c]!==words[1+acks*128+c][15:8])$fatal(1,"C/mailbox/core map mismatch");
    end
    $fdisplay(trace,"%0d %0256h %032h",acks+1,dut.core.native_system.digital.effective,dut.core.native_system.digital.mask);acks=acks+1;
   end
   previous=dut.core.native_system.digital.effective;previous_mask=dut.core.native_system.digital.mask;
  end else begin previous=0;previous_mask=0;end
 end
 initial begin
  $readmemh("motion_maps.hex",words);n=words[0];if(n<2||n>512)$fatal(1,"bounded integrated input");trace=$fopen("integrated_ack.txt","w");
  ms(3);rst_n=1;ms(5);if(!output_disable||efuse_up||efuse_dn)$fatal(1,"startup not OFF");
  wait(dut.core.native_system.digital.adc_ready);if(!configured)$fatal(1,"ADC logical configuration");
  write_axi(12,40000);write_axi(8,1);write_axi(0,1);
  control[0]=1;ms(10);control[0]=0;ms(4);if(status[3:0]!=3)$fatal(1,"ARM failed");
  control[1]=1;ms(10);control[1]=0;ms(4);if(status[3:0]!=4)$fatal(1,"CAL failed");
  control[3]=1;control[4]=1;ms(3);control[3]=0;ms(3);if(status[3:0]!=6)$fatal(1,"CAL quality failed");
  if(!output_disable||efuse_up||efuse_dn)$fatal(1,"CAL_READY not OFF");
  while(loaded<n)begin
   wait(!dut.mailbox_busy&&dut.buffered_count<4);
   @(negedge clk);for(integer c=0;c<128;c++)memory[c]=words[1+loaded*128+c];memory[128]=loaded+1;memory[129]=(loaded==n-1);
   control[9]=~control[9];loaded=loaded+1;wait(dut.mailbox_busy);wait(!dut.mailbox_busy);
   if(loaded==2)begin
    control[5]=1;ms(2);control[5]=0;control[6]=1;ms(2);control[6]=0;control[8]=1;ms(1);control[8]=0;
   end
  end
  wait(dut.motion_done);ms(2);if(acks!=n)$fatal(1,"Missing integrated ACK");
  health[1]=0;#1;if(!output_disable||efuse_up||efuse_dn)$fatal(1,"subclock health kill");health[1]=1;ms(4);
  if(status[3:0]!=9||!output_disable)$fatal(1,"restored power auto resumed");
  control[2]=1;ms(5);control[2]=0;ms(5);if(status[3:0]!=2||!output_disable)$fatal(1,"manual rearm boundary");
  control[0]=1;ms(10);control[0]=0;ms(4);control[1]=1;ms(10);control[1]=0;ms(4);
  control[3]=1;ms(3);control[3]=0;ms(4);
  if(status[3:0]!=6||dut.buffered_count!=0||dut.frame_valid||status[31:16]!=0||!output_disable)$fatal(1,"stale task resumed across rearm");
  control[5]=1;ms(2);control[5]=0;expected_fault=1;control[8]=1;ms(4);control[8]=0;
  if(status[3:0]!=9||!output_disable||efuse_up||efuse_dn)$fatal(1,"queue underflow not propagated to both-bank kill");
  $fclose(trace);$display("PASS PREPCB SYSTEM C maps BRAM supervisor AXI atomic ACK fault latch manual rearm no stale task frames=%0d",n);$finish;
 end
 initial begin #200000000;$fatal(1,"Integrated timeout");end
endmodule
