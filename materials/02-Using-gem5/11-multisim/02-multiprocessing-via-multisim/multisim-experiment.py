"""
This script is the starting points for the 02-Using-gem5/11-multisim execise
in which the script in "01-multiprocessing-via-script" is converted to use
the MultiSim module.

This script is incomplete and is to be finished by the user.

Usage
-----
# This will run all the simulations in parallel.
gem5 -m gem5.multisim multisim-experiment.py path/to/multisim-experiment.py

"""

from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.cachehierarchies.classic.private_l1_cache_hierarchy import PrivateL1CacheHierarchy
from gem5.components.memory import SingleChannelDDR3_1600
from gem5.components.processors.cpu_types import CPUTypes
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.isas import ISA
from gem5.resources.resource import obtain_resource
from gem5.simulate.simulator import Simulator

import gem5.utils.multisim as multisim

cache_hierarchy = PrivateL1CacheHierarchy(
    l1d_size="TODO",
    l1i_size="TODO",
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

## Add the simulator to multisim here.
