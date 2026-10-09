// Isolated configuration ROM only; not instantiated in the production ADC interface.
module ad7606c_candidate_rom(input wire[4:0] index,output reg[15:0] command);
always @* case(index)
5'd0: command=16'h4200;
5'd1: command=16'h0210;
5'd2: command=16'h0311;
5'd3: command=16'h0411;
5'd4: command=16'h0511;
5'd5: command=16'h0611;
5'd6: command=16'h07ff;
5'd7: command=16'h4200;
5'd8: command=16'h4000;
5'd9: command=16'h4300;
5'd10: command=16'h4000;
5'd11: command=16'h4400;
5'd12: command=16'h4000;
5'd13: command=16'h4500;
5'd14: command=16'h4000;
5'd15: command=16'h4600;
5'd16: command=16'h4000;
5'd17: command=16'h4700;
5'd18: command=16'h4000;
5'd19: command=16'h0000;
default: command=16'h0000;
endcase
endmodule
