#   Copyright 2019 <Huawei Technologies Co., Ltd>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from copy import deepcopy

from projectq.ops import Measure, Allocate, AllocateDirty, AllocateQuregGate
from ._kraus_error import KrausError


class NoiseModelError(Exception):
    pass


class NoiseModel(object):
    """
    The general class for noisy gate
    """

    def __init__(self, qerror=None, noisy_gates=None, noisy_qubits=None, name=None):
        """
        Initialize NoiseModel object

        """
        self._noisy_qubits = set()
        self._noisy_gates = set()
        self.errors_list = []

        if all(a is None for a in [qerror, noisy_gates, noisy_qubits, name]):
            pass
        elif qerror is None and not all(a is None for a in [noisy_gates, noisy_qubits, name]):
            raise NoiseModelError("NoiseModel was initialized without qerror. "
                                  "Add qerror to specify NoiseModel.")
        else:
            self.add_qerror(qerror,
                            noisy_gates=noisy_gates,
                            noisy_qubits=noisy_qubits,
                            name=name)

    def add_qerror(self,
                   qerror,
                   noisy_gates=None,
                   noisy_qubits=None,
                   name=None,
                   position='after'):
        """
        Add quantum error to noise model
        """

        if not isinstance(qerror, KrausError):
            raise NoiseModelError("Argument does not belongs to KrausError class")

        qerror = deepcopy(qerror)

        if noisy_gates is not None:
            qerror.add_noisy_gates(noisy_gates)
            if not isinstance(noisy_gates, (list, tuple)):
                noisy_gates = [noisy_gates]
            self._noisy_gates = self._noisy_gates.union(noisy_gates, qerror.noisy_gates)

        if noisy_qubits is not None:
            qerror.add_noisy_qubits(noisy_qubits)
            self._noisy_qubits = self._noisy_qubits.union(noisy_qubits, qerror.noisy_qubits)
        else:
            self._noisy_qubits = self._noisy_qubits.union(qerror.noisy_qubits)

        if name is not None:
            qerror.name = name

        # set position of noisy gates in a quantum circuit
        if position == 'after':
            qerror.position = 'after'
        elif position == 'before':
            qerror.position = 'before'
        else:
            raise NoiseModelError("Position of error is incorrect. "
                                  "Use keywords 'before' or 'after'.")

        self.errors_list.append(qerror)

    def add_measure_qerror(self, qerror, noisy_qubits=None, name=None):
        """
        Add quantum error to measure operations
        """

        self.add_qerror(qerror,
                        noisy_gates=Measure,
                        noisy_qubits=noisy_qubits,
                        name=name,
                        position='before')

    def add_prepare_qerror(self, qerror, noisy_qubits=None, name=None):
        """
        Add quantum error while during preparation of qubit
        (after gate allocate)
        """

        self.add_qerror(qerror,
                        noisy_gates=(Allocate, AllocateQuregGate(), AllocateDirty),
                        noisy_qubits=noisy_qubits,
                        name=name)

    @property
    def noisy_qubits(self):
        noisy_qubits_set = set()
        for qerror in self.errors_list:
            noisy_qubits_set |= qerror.noisy_qubits
        return noisy_qubits_set

    @property
    def noisy_gates(self):
        noisy_gates_set = set()
        for qerror in self.errors_list:
            noisy_gates_set |= qerror.noisy_gates
        return noisy_gates_set

    def __str__(self):
        result = ''
        for ind, q_error in enumerate(self.errors_list):
            result += f'quantum error {ind}:\n'
            result += str(q_error)
            result += '\n'
        return result
