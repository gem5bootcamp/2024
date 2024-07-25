from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.cachehierarchies.classic.private_l1_cache_hierarchy import PrivateL1CacheHierarchy
from gem5.components.memory.single_channel import SingleChannelDDR3_1600
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.components.processors.cpu_types import CPUTypes
from gem5.resources.resource import obtain_resource
from gem5.simulate.simulator import Simulator
from gem5.isas import ISA

""" The purpose of this script is to demonstratea the journey of an instruction
through the gem5 CPU models,.

It can be executed with:

```shell
gdb gem5

# Add breakpoints to for functions in StaticInst object representing the `Add`
# instruction.

# Add breakpoints to the `Add::Add` function.
# This is just the constructor for the `Add` class. It created the `StaticInst`
# object that represents the `Add` instruction.
(gdb) b Add::Add

# Add breakpoints to the `Add::execute` funciton.
# This is function called to execute the `Add` instruction.
(gdb) b Add::execute

# Start execution of gem5
(gdb) run \
    materials/03-Developing-gem5-models/05-modeling-cores/01-inst-trace.py
```
"""

cache_hierarchy = PrivateL1CacheHierarchy(l1d_size="32KiB", l1i_size="32KiB")
memory = SingleChannelDDR3_1600("1GiB")

# By default, use TIMING
# (Change `ATOMIC` to `TIMING` or `O3` to use see the journey
# in a different CPU model).
processor = SimpleProcessor(cpu_type=CPUTypes.TIMING, num_cores=1, isa= ISA.RISCV)

#Add them to the board.
board = SimpleBoard(
    clk_freq="3GHz",
    processor=processor,
    memory=memory,
    cache_hierarchy=cache_hierarchy,
)

binary = obtain_resource("riscv-hello")
board.set_se_binary_workload(binary)

# Setup the Simulator and run the simulation.
simulator = Simulator(board=board)
simulator.run()
