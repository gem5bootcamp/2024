"""
This script is the "01-multiprocessing-via-multisim.py" script converted to
use the MultiSim module.

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

multisim.set_num_processes(2)

for data_cache_size in ["8kb","16KB"]:
    for instruction_cache_size in ["8kb","16KB"]:

        cache_hierarchy = PrivateL1CacheHierarchy(
            l1d_size=data_cache_size,
            l1i_size=instruction_cache_size,
        )

        memory = SingleChannelDDR3_1600(size="32MB")

        processor = SimpleProcessor(
            cpu_type=CPUTypes.TIMING,
            isa=ISA.X86,
            num_cores=1
        )

        board = SimpleBoard(
            clk_freq="3GHz",
            processor=processor,
            memory=memory,
            cache_hierarchy=cache_hierarchy,
        )

        board.set_se_binary_workload(
            obtain_resource("x86-matrix-multiply")
        )

        # The key difference: The simulator is object is passed to the
        # MultiSim module via the `add_simulator` function.
        #
        # The `run` function is not called here. Instead it is involved in
        # MultiSim module's execution.
        multisim.add_simulator(
            Simulator(
                board=board,
                # The `id` parameter is used to identify the simulation.
                # Setting this is strongly encouraged.
                # Each output directory will be named after the `id` parameter.
                id=f"process_{data_cache_size}_{instruction_cache_size}"
            )
        )

