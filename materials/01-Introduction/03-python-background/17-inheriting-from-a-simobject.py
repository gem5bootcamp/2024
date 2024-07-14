"""
This script shows how object oriented design principles can be used to extend
a gem5 SimObject for use in simulation.
"""

#It's useful in gem5 to take a SimObject and extend it to add new functionality.
# gem5 should ideally be open for extension but closed for modification.
# Modifying gem5 code directly can be difficult to maintain and can lead to
# merge conflicts when updating to new versions of gem5.

# Below is an example of spcializing a gem5 SimObject to create an abstract
# L1 cache. This can be used as a base class for L1 instruction cache.
# L1 cache and L1 instruction cache.

from m5.objects import Cache
from abc import ABC

class L1Cache(Cache, ABC):
    """Simple L1 Cache with default values"""

    # Here we set/override the default values for the cache.
    assoc = 8
    tag_latency = 1
    data_latency = 1
    response_latency = 1
    mshrs = 16
    tgts_per_mshr = 20
    writeback_clean = True

    def __init__(self):
        super().__init__()

    # We extend the functionality. In this case by adding a method to aid in
    # Adding the cache to a bus and processor.
    # Connecting to the cpu is left unimplemented as it will be different for
    # each type of cache.
    def connectBus(self, bus):
        """Connect this cache to a memory-side bus"""
        self.mem_side = bus.cpu_side_ports

    def connectCPU(self, cpu):
        """Connect this cache's port to a CPU-side port
        This must be defined in a subclass"""
        raise NotImplementedError


class L1ICache(L1Cache):
    """Simple L1 instruction cache with default values"""

    # Set the size
    size = "32kB"

    def __init__(self):
        super().__init__()

    # This is the implementation needed for the L1ICache to connect to the CPU.
    def connectCPU(self, cpu):
        """Connect this cache's port to a CPU icache port"""
        self.cpu_side = cpu.icache_port

