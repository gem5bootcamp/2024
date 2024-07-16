# Copyright (c) 2022 The Regents of the University of California
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met: redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer;
# redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution;
# neither the name of the copyright holders nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from m5.objects import DDR4_2400_8x8

from gem5.components.memory.memory import ChanneledMemory


# HW3DDR4 models a 1 GiB dual channel DDR4 DRAM memory with a data
# bus clocked at 2400MHz. This model extends ChanneledMemory from gem5's
# standard libary. Please refer to
#     gem5/src/python/gem5/components/memory/memory.py
# for documentation on ChanneledMemory.

# Below is the function signature for the constructor of ChanneledMemory class.
# class ChanneledMemory(AbstractMemorySystem):
#     def __init__(
#         self,
#         dram_interface_class: Type[DRAMInterface],
#         num_channels: Union[int, str],
#         interleaving_size: Union[int, str],
#         size: Optional[str] = None,
#         addr_mapping: Optional[str] = None,
#     )


class HW3DDR4(ChanneledMemory):
    def __init__(self):
        super().__init__(
            dram_interface_class=DDR4_2400_8x8,
            num_channels=2,
            interleaving_size=128,
            size="1 GiB",
        )
