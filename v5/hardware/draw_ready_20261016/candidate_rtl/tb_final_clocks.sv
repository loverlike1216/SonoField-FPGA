`timescale 1ns/1ps
module tb_final_clocks;
 reg ref_clk50=0;always #10 ref_clk50=~ref_clk50;
 wire core_clk,tx_clk,locked;draw_ready_clocks dut(.*);
 real lastcore=0,lasttx=0;integer nc=0,nt=0;
 always@(posedge core_clk)if(locked)begin
  if(lastcore&&($realtime-lastcore<7.8075||$realtime-lastcore>7.8175))$fatal(1,"128MHz period %f",$realtime-lastcore);lastcore=$realtime;nc=nc+1;
 end
 always@(posedge tx_clk)if(locked)begin
  if(lasttx&&($realtime-lasttx<3.90125||$realtime-lasttx>3.91125))$fatal(1,"256MHz period %f",$realtime-lasttx);lasttx=$realtime;nt=nt+1;
 end
 initial begin wait(locked);repeat(1000)@(posedge core_clk);if(nt<1998||nt>2002)$fatal(1,"clock ratio");$display("PASS REAL_UNISIM_MMCM125/256MHz period/ratio");$finish;end
 initial begin #200000;$fatal(1,"MMCM did not lock");end
endmodule
