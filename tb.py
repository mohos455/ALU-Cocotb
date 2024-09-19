# Code your testbench here
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import *
from cocotb.handle import Force , Release , Freeze 


async def try_start_soon(dut) : 
    cocotb.log.info("Inside Try Start_Soon")
    dut.rst_n.value = 1
    dut.A.value = 0
    dut.B.value = 0
    dut.ALU_Sel.value = 0
    await RisingEdge(dut.clk)
    cocotb.log.info(" After Rising start  soon ")
    await FallingEdge(dut.clk)
    cocotb.log.info(" After Falling start  soon ")
    
async def try_start(dut) : 
    dut.rst_n.value = 0
    dut.A.value = 0
    dut.B.value = 0
    dut.ALU_Sel.value = 0
    await RisingEdge(dut.clk)
    cocotb.log.info(" After Rising Start ")
    await FallingEdge(dut.clk)
    cocotb.log.info(" After Falling Start")
    
async def driving_stimilus(dut):
    await FallingEdge(dut.clk)
    dut.rst_n.value = 1
    dut.A.value = 5
    dut.B.value = 20
    dut.ALU_Sel.value = 0
    await RisingEdge(dut.clk)
    await ReadOnly()
    cocotb.log.info(" Output : "+str(dut.ALU_Out.value))
    
@cocotb.test()
async def tb_top(dut):
    cocotb.log.info(" STARTING SIMULATION ")
    CLK = Clock(dut.clk, 10, units="ns")
    dut.rst_n.value = 0
    await cocotb.start(CLK.start())
    await cocotb.start_soon(driving_stimilus(dut))
    cocotb.log.info(" After Driving Stimilus")
