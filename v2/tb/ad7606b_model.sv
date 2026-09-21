`timescale 1ns/1ps
// Protocol model derived from AD7606B Rev B, NOT an analog/device qualification.
module ad7606b_model(input wire reset,convst,cs_n,sclk,sdi,hold_busy,
 output reg busy,output reg[3:0] dout,output reg configured);
 reg[127:0] vectors[0:1023];reg[127:0] converted;
 reg[7:0] registers[0:63];reg register_mode;reg[5:0] read_address;
 reg[31:0] words[0:3];reg[15:0] command;
 integer index,fall_count,conversion_count,k;
 real last_fall,last_rise,last_conv;
 initial begin
  $readmemh("adc_vectors.hex",vectors);
  busy=0;dout=0;configured=0;register_mode=0;read_address=0;
  conversion_count=0;index=0;fall_count=0;last_fall=0;last_rise=0;last_conv=-10000;converted=0;
  for(k=0;k<64;k=k+1)registers[k]=0;
 end
 always @(posedge reset)begin
  configured=0;register_mode=0;read_address=0;conversion_count=0;busy=0;last_conv=-10000;
  for(k=0;k<64;k=k+1)registers[k]=0;
 end
 always @(posedge convst)begin
  if(!configured)$fatal(1,"Conversion before ADC configuration");
  if($realtime-last_conv<1249.9)$fatal(1,"CONVST exceeds 800 kSPS");
  last_conv=$realtime;
  #10 busy=1;
  // Alternating min/max conversion times stresses reading across the next conversion.
  if(conversion_count%2==0)#840;else #640;
  if(!hold_busy)begin
   if(!cs_n)$fatal(1,"SPI overlaps BUSY falling data replacement");
   if($realtime-last_rise<25)$fatal(1,"Read completion lacks 25 ns margin");
   converted=vectors[conversion_count%1024];conversion_count=conversion_count+1;busy=0;
  end
 end
 always @(negedge cs_n)begin
  index=0;fall_count=0;command=0;
  for(k=0;k<4;k=k+1)begin
   words[k]=register_mode?(k==0?{8'b0,registers[read_address],16'b0}:32'b0):
       {converted[(2*k)*16+:16],converted[(2*k+1)*16+:16]};
   dout[k]<=#9 words[k][31];
  end
 end
 always @(negedge sclk)if(!cs_n)begin
  if(last_rise!=0&&$realtime-last_rise<15)$fatal(1,"SCLK high too short");
  last_fall=$realtime;fall_count=fall_count+1;command={command[14:0],sdi};
 end
 always @(posedge sclk)if(!cs_n)begin
  if($realtime-last_fall<15)$fatal(1,"SCLK low too short");
  last_rise=$realtime;index=index+1;
  for(k=0;k<4;k=k+1)dout[k]<=#15(index<32?words[k][31-index]:1'b0);
 end
 always @(posedge cs_n)if(fall_count==16)begin
  if(command[15:14]==2'b01)begin read_address=command[13:8];register_mode=1;end
  else if(register_mode&&command[15:14]==0)begin
   if(command[13:8]==0)begin
    register_mode=0;
    configured=(registers[2]==8'h10 && registers[3]==8'h11 && registers[4]==8'h11 && registers[5]==8'h11 && registers[6]==8'h11);
   end else registers[command[13:8]]=command[7:0];
  end
 end
endmodule
