from argparse import ArgumentParser
from components.processors import Big, Little
from gem5.components.cachehierarchies.classic.private_l1_cache_hierarchy import PrivateL1CacheHierarchy
from gem5.components.memory.memory import ChanneledMemory
from gem5.resources.resource import obtain_resource
from gem5.simulate.simulator import Simulator
from m5.objects import DDR4_2400_8x8

# A simple script to test custom processors
# We will run a simple application (riscv-matrix-multiply-run) with two different configurations of an O3 processor

# Steps
    # 1. Go to components/processors.py and update class big(O3CPU) and class LITTLE(O3CPU)
    # 2. Run with `gem5 --outdir=big-proc ./materials/developing-gem5-models/04-cores/cores-complex.py -p big`
    # 3. Run with `gem5 --outdir=little-proc ./materials/developing-gem5-models/04-cores/cores-complex.py -p little`
    # 4. Compare the stats.txt file in /big-proc/ and /little-proc/

# In general run with the following command
    # gem5 [optional: --outdir=<processor-type>-proc] ./materials/developing-gem5-models/04-cores/cores-complex.py -p <processor-type>
    # Note that processor-type should be "big" or "little"

# *** Argument Parsing ***

USAGE = """ A simple script to test custom processors

Example usage:

gem5 --outdir=big-proc ./materials/developing-gem5-models/04-cores/cores-complex.py -p big
"""

parser = ArgumentParser(description=USAGE)

parser.add_argument(
    "-p",
    "--processor",
    type=str,
    help="Type of processor (big or little)",
    required=True,
)

arguments = parser.parse_args()

# *** Setting up the board and running the workload ***

cache_hierarchy = PrivateL1CacheHierarchy(l1d_size="1KiB", l1i_size="1KiB")

memory = ChanneledMemory(
    dram_interface_class=DDR4_2400_8x8,
    num_channels=2,
    interleaving_size=128,
    size="1 GiB",
)

if arguments.processor.lower() == "big":
    processor = Big()
elif arguments.processor.lower() == "little":
    processor = Little()
else:
    print("Error: processor must be named big or little")

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
