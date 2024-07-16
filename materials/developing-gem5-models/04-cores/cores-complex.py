from gem5.resources.resource import obtain_resource
from gem5.simulate.simulator import Simulator
from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.cachehierarchies.classic.private_l1_cache_hierarchy import PrivateL1CacheHierarchy
# from gem5.components.cachehierarchies.ruby.mesi_two_level_cache_hierarchy import MESITwoLevelCacheHierarchy
from gem5.components.memory.single_channel import SingleChannelDDR3_1600, SingleChannelDDR4_2400
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.components.processors.cpu_types import CPUTypes
from gem5.isas import ISA

from components.memories import HW3DDR4
# from components.cache_hierarchies import HW3MESICache
from components.processors import big, LITTLE
from components.boards import HW3RISCVBoard

from m5.objects import DDR4_2400_8x8
from gem5.components.memory.memory import ChanneledMemory

# Run with the following command
    # gem5 ./materials/developing-gem5-models/04-cores/cores-complex.py

# A simple script to test custom processors
# We will run a simple application (riscv-matrix-multiply-run) with two different configurations of an O3 processor

cache_hierarchy = PrivateL1CacheHierarchy(l1d_size="1KiB", l1i_size="1KiB") # Was 32
# cache_hierarchy = HW3MESICache()
# cache_hierarchy=MESITwoLevelCacheHierarchy(
#     l1d_size="16kB",
#     l1d_assoc=8,
#     l1i_size="16kB",
#     l1i_assoc=8,
#     l2_size="256kB",
#     l2_assoc=16,
#     num_l2_banks=1,
# )
#

memory = ChanneledMemory(
    dram_interface_class=DDR4_2400_8x8,
    num_channels=2,
    interleaving_size=128,
    size="1 GiB",
)

# Comment out the processor you don't want to use and
# Uncomment the one you do want to use

processor = big()
# processor = LITTLE()

board = SimpleBoard(
    clk_freq="2GHz",
    processor=processor,
    memory=memory,
    cache_hierarchy=cache_hierarchy
)

# Resources can be found at https://resources.gem5.org/
# https://resources.gem5.org/resources/riscv-getting-started-benchmark-suite?version=1.0.0

workload = obtain_resource("riscv-matrix-multiply-run")
board.set_workload(workload)
simulator = Simulator(board=board)
simulator.run()
print(f"Ran a total of {simulator.get_current_tick() / 1e12} simulated seconds")
