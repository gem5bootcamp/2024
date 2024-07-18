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

from gem5.isas import ISA
from gem5.components.processors.base_cpu_core import BaseCPUCore
from gem5.components.processors.base_cpu_processor import BaseCPUProcessor

from m5.objects import RiscvO3CPU
from m5.objects.FuncUnitConfig import *
from m5.objects.BranchPredictor import (
    TournamentBP,
    MultiperspectivePerceptronTAGE64KB,
)


# O3CPUCore extends RiscvO3CPU. RiscvO3CPU is one of gem5's internal models
# the implements an out of order pipeline. Please refer to
#   https://www.gem5.org/documentation/general_docs/cpu_models/O3CPU
# to learn more about O3CPU.


class O3CPUCore(RiscvO3CPU):
    def __init__(self, width, rob_size, num_int_regs, num_fp_regs):
        """
        :param width: sets the width of fetch, decode, raname, issue, wb, and
        commit stages.
        :param rob_size: determine the number of entries in the reorder buffer.
        :param num_int_regs: determines the size of the integer register file.
        :param num_int_regs: determines the size of the vector/floating point
        register file.
        """
        super().__init__()
        self.fetchWidth = width
        self.decodeWidth = width
        self.renameWidth = width
        self.issueWidth = width
        self.wbWidth = width
        self.commitWidth = width

        self.numROBEntries = rob_size

        self.numPhysIntRegs = num_int_regs
        self.numPhysFloatRegs = num_fp_regs

        self.branchPred = TournamentBP()

        self.LQEntries = 128
        self.SQEntries = 128


# Along with BaseCPUCore, CPUStdCore wraps CPUCore to a core compatible
# with gem5's standard library. Please refer to
#   gem5/src/python/gem5/components/processors/base_cpu_core.py
# to learn more about BaseCPUCore.


class O3CPUStdCore(BaseCPUCore):
    def __init__(self, width, rob_size, num_int_regs, num_fp_regs):
        """
        :param width: sets the width of fetch, decode, raname, issue, wb, and
        commit stages.
        :param rob_size: determine the number of entries in the reorder buffer.
        :param num_int_regs: determines the size of the integer register file.
        :param num_int_regs: determines the size of the vector/floating point
        register file.
        """
        core = O3CPUCore(width, rob_size, num_int_regs, num_fp_regs)
        super().__init__(core, ISA.RISCV)


# O3CPU along with BaseCPUProcessor wraps CPUCore to a processor
# compatible with gem5's standard library. Please refer to
#   gem5/src/python/gem5/components/processors/base_cpu_processor.py
# to learn more about BaseCPUProcessor.


class O3CPU(BaseCPUProcessor):
    def __init__(self, width, rob_size, num_int_regs, num_fp_regs):
        """
        :param width: sets the width of fetch, decode, raname, issue, wb, and
        commit stages.
        :param rob_size: determine the number of entries in the reorder buffer.
        :param num_int_regs: determines the size of the integer register file.
        :param num_int_regs: determines the size of the vector/floating point
        register file.
        """
        cores = [O3CPUStdCore(width, rob_size, num_int_regs, num_fp_regs)]
        super().__init__(cores)
        self._width = width
        self._rob_size = rob_size
        self._num_int_regs = num_int_regs
        self._num_fp_regs = num_fp_regs

    def get_area_score(self):
        """
        :returns the area score of a pipeline using its parameters width,
        rob_size, num_int_regs, and num_fp_regs.
        """
        score = (
            self._width
            * (2 * self._rob_size + self._num_int_regs + self._num_fp_regs)
            + 4 * self._width
            + 2 * self._rob_size
            + self._num_int_regs
            + self._num_fp_regs
        )
        return score

# UPDATE FOR STEP 1
# Configure with width=10, rob_size=40, num_int_regs=50, num_fp_regs=50
class Big(O3CPU):
    def __init__(self):
        super().__init__(
            width=10,
            rob_size=40,
            num_int_regs=50,
            num_fp_regs=50,
        )

# UPDATE FOR STEP 1
# Configure with width=2, rob_size=30, num_int_regs=40, num_fp_regs=40
class Little(O3CPU):
    def __init__(self):
        super().__init__(
            width=2,
            rob_size=30,
            num_int_regs=40,
            num_fp_regs=40,
        )
