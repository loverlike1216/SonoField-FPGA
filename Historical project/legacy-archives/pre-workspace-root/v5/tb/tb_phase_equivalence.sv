`timescale 1ns/1ps
// Independent arithmetic oracle uses the original carrier-domain formula.
module tb_phase_equivalence;
 `include "registers.svh"
 reg clk=0;always #3.787878788 clk=~clk;
 reg rst_n=0,bus_valid=0,bus_write=0;reg[7:0] bus_address=0;reg[31:0] bus_wdata=0;
 wire[31:0] bus_rdata;wire bus_ready,bus_error;
 sono_digital_system #(.POWER_WAIT_CYCLES(32)) dut(.clk(clk),.rst_n(rst_n),.hardware_enable(1'b0),
 .bus_valid(bus_valid),.bus_write(bus_write),.bus_address(bus_address),.bus_wdata(bus_wdata),
 .bus_rdata(bus_rdata),.bus_ready(bus_ready),.bus_error(bus_error),.adc_busy(1'b0),.adc_dout(4'b0));
 reg[63:0] reference_acc,next_acc;reg[7:0] reference_phase,previous_phase;reg expected_boundary;
 integer checked=0,n;reg[31:0] random_state=32'h7020132;
 always @(posedge clk)begin
  if(!rst_n || !dut.core_rst)begin reference_acc=0;reference_phase=0;previous_phase=0;expected_boundary=0;end
  else begin
   previous_phase=reference_phase;
   next_acc=reference_acc+dut.cfg[REG_FREQUENCY/4];expected_boundary=next_acc>=132000000;
   reference_acc=expected_boundary?next_acc-132000000:next_acc;
   reference_phase=(reference_acc*256)/132000000;
  end
  #0.1;
  if(dut.master_phase!==reference_phase || dut.boundary!==expected_boundary || dut.tick!==(reference_phase!=previous_phase))
   $fatal(1,"phase equivalence cycle=%0d phase=%0d expected=%0d",checked,dut.master_phase,reference_phase);
  checked=checked+1;
 end
 task frequency(input[31:0] value);
  begin @(negedge clk);bus_valid=1;bus_write=1;bus_address=REG_FREQUENCY;bus_wdata=value;
   @(negedge clk);bus_valid=0;bus_write=0;end
 endtask
 initial begin
  repeat(5)@(negedge clk);rst_n=1;repeat(10)@(negedge clk);
  frequency(38500);repeat(132000)@(negedge clk);
  frequency(41500);repeat(132000)@(negedge clk);
  frequency(40000);repeat(132000)@(negedge clk);
  for(n=0;n<1000;n=n+1)begin
   random_state={random_state[30:0],random_state[31]^random_state[21]^random_state[1]^random_state[0]};
   frequency(38500+random_state%3001);repeat(83)@(negedge clk);
  end
  rst_n=0;repeat(5)@(negedge clk);rst_n=1;repeat(5000)@(negedge clk);
  if(bus_error)$fatal(1,"unexpected bus error");
  $display("PASS PHASE_EQUIVALENCE checked=%0d deterministic_seed=0x7020132 latency_change=0",checked);$finish;
 end
endmodule
