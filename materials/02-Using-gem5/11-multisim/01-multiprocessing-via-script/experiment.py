"""
This script creates a simple system with a single core
running a matrix multiply workload in SE mode. It takes the L1 data cache size
and the L1 instruction cache size as command line arguments.

The script is run by "run-experiment.sh" which passes various cache size
combinations to the script to spin-up multiple gem5 instances in parallel.

This is used to demonstrate how **NOT** to use gem5. The gem5 MultiSim module
should be used (see "02-multiprocessing-via-multisim").

"""

from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.cachehierarchies.classic.private_l1_cache_hierarchy import PrivateL1CacheHierarchy
from gem5.components.memory import SingleChannelDDR3_1600
from gem5.components.processors.cpu_types import CPUTypes
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.isas import ISA
from gem5.resources.resource import obtain_resource
from gem5.simulate.simulator import Simulator

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("data_cache", type=str, help="The data cache size.")
parser.add_argument("instruction_cache", type=str,
                    help="The instruction cache size.")
args = parser.parse_args()


cache_hierarchy = PrivateL1CacheHierarchy(
    l1d_size=args.data_cache,
    l1i_size=args.instruction_cache
)

memory = SingleChannelDDR3_1600(size="32MB")

processor = SimpleProcessor(cpu_type=CPUTypes.TIMING, isa=ISA.X86, num_cores=1)

board = SimpleBoard(
    clk_freq="3GHz",
    processor=processor,
    memory=memory,
    cache_hierarchy=cache_hierarchy,
)

board.set_se_binary_workload(
    obtain_resource("x86-matrix-multiply")
)


simulator = Simulator(board=board)
simulator.run()

