`timescale 1ns/1ps
// Manufacturer serial-edge/lane model, not an analog ADC model.
module tb_adc_candidate;
reg clk=0;always #3.787879 clk=~clk;
reg rst_n=0,start=0;reg[3:0] dout=0;
wire cs_n,sclk,sdi,busy,done;wire[127:0] received;
reg[127:0] vectors[0:255];reg[31:0] lane[0:3];
integer i,k,bit_index=0;reg[4:0] rom_index=0;wire[15:0] command;
string vector_file;
ad7606c_candidate_rom rom(rom_index,command);
adc_serial dut(.clk(clk),.rst_n(rst_n),.start(start),.bits(6'd32),.command(16'h0000),.dout(dout),.cs_n(cs_n),.sclk(sclk),.sdi(sdi),.busy(busy),.done(done),.received(received));
always @(negedge cs_n)begin
 bit_index=0;
 for(k=0;k<4;k=k+1)begin lane[k]={vectors[i][(2*k)*16+:16],vectors[i][(2*k+1)*16+:16]};dout[k]=lane[k][31];end
end
always @(posedge sclk)if(!cs_n)begin
 bit_index=bit_index+1;
 for(k=0;k<4;k=k+1)if(bit_index<32)dout[k]<=lane[k][31-bit_index];else dout[k]<=0;
end
initial begin
 if(!$value$plusargs("VECTORS=%s",vector_file))vector_file="adc_vectors.mem";
 $readmemh(vector_file,vectors);
 rom_index=6;#1;if(command!==16'h07ff)$fatal(1,"missing high bandwidth write");
 rom_index=17;#1;if(command!==16'h4700)$fatal(1,"missing bandwidth readback");
 repeat(4)@(negedge clk);rst_n=1;
 for(i=0;i<256;i=i+1)begin
  @(negedge clk);start=1;@(negedge clk);start=0;
  wait(done);#1;
  if(received!==vectors[i])$fatal(1,"frame/lane mismatch %0d got=%032h expected=%032h",i,received,vectors[i]);
  @(negedge clk);
 end
 $display("ADC_CANDIDATE_SERIAL_PASS frames=256 signed_edges_and_channel_order_checked");$finish;
end
initial begin #10000000;$fatal(1,"timeout");end
endmodule
