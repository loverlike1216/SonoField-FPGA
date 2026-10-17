`timescale 1ns/1ps
module tb_freshness;
 reg clk=0,rst_n=0,kick=0,qualified=0;always #5 clk=~clk;
 wire fresh;service_freshness #(.TIMEOUT_CYCLES(16))dut(.*);
 initial begin
  repeat(3)@(negedge clk);rst_n=1;
  qualified=1;repeat(3)@(negedge clk);if(fresh)$fatal(1,"flags without completed service kick");
  kick=1;@(negedge clk);if(!fresh)$fatal(1,"qualified kick not accepted");
  qualified=0;#1;if(fresh)$fatal(1,"qualification lost but output remains enabled");
  repeat(2)@(negedge clk);qualified=1;repeat(2)@(negedge clk);
  if(fresh)$fatal(1,"old freshness resurrected after failed sensor transaction");
  kick=0;@(negedge clk);if(!fresh)$fatal(1,"new valid transaction did not recover");
  repeat(17)@(negedge clk);if(fresh)$fatal(1,"stalled PS not timed out");
  kick=1;@(negedge clk);if(!fresh)$fatal(1,"fresh qualified transaction not accepted");
  rst_n=0;#1;if(fresh)$fatal(1,"reset kill not asynchronous");
  $display("PASS freshness flags/defaultoff/kick/timeout/failed-read invalidation");$finish;
 end
 initial begin #10000;$fatal(1,"timeout");end
endmodule
