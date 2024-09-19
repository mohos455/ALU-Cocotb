module ALU (
    input logic clk,
    input logic rst_n,
    input [7:0] A,         
    input [7:0] B,        
    input [1:0] ALU_Sel,   
  output logic [8:0] ALU_Out
);

    always_ff @(posedge clk or negedge rst_n)
    begin
        if(~rst_n) begin
            ALU_Out <= 0 ;
        end
        else begin
        case (ALU_Sel)
            2'b00: ALU_Out <= A + B;        // Addition
            2'b01: ALU_Out <= A - B;        // Subtraction
            2'b10: ALU_Out <= A & B;        // AND
            2'b11: ALU_Out <= A | B;        // OR
            default: ALU_Out <= 8'b00000000;    // Default case
        endcase
        
    end
end

endmodule
