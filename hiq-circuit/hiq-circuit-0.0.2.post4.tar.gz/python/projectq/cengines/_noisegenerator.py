
"""
Contains Noise generator engine
"""

import random
import numpy as np
from projectq.cengines import BasicEngine
from projectq.ops import (AllocateDirtyQubitGate,
                          AllocateQubitGate,
                          ClassicalInstructionGate,
                          Command,
                          MeasureGate,
                          DeallocateQubitGate,
                          AllocateQuregGate)

from copy import deepcopy


class NoiseEngine(BasicEngine):
    """
    Noise generator engine is a compiler engine which replaces logic gates
    according to noise model
    """

    def __init__(self, noise_model, rnd_seed=None):
        """
        Initialize a NoiseEngine object

        :param
            noise_model: str
                specific noise model.
        """

        # Check that noise_model is "correct"
        # some code here

        noise_model = deepcopy(noise_model)

        BasicEngine.__init__(self)
        self.noise_model = noise_model
        if rnd_seed is None:
            self.rnd_seed = random.randint(0, 4294967295)


    def _update_noisy_qubits(self, cmd, noise_model):
        """
        Appends indexes of new allocated qubits to noise model
        if some error acts on all qubits in the circuit.

        Arguments:
            cmd: Command class object
            noise_model: NoiseModel object
        """
        gate = cmd.gate
        qubit_inds = set(q.id for q in cmd.qubits[0])
        control_inds = set(q.id for q in cmd.control_qubits)
        all_qubit_inds = qubit_inds.union(control_inds)

        if isinstance(gate, (AllocateQubitGate, AllocateDirtyQubitGate, AllocateQuregGate)):
            # Append new qubit index to NoiseModel obj
            for qerror in self.noise_model.errors_list:
                if qerror.allqubits:
                    qerror._expand_noisy_qubits(all_qubit_inds)

    def _update_noisy_gates(self, cmd, noise_model):
        """
        Appends gates to the set of noisy gates if
        some quantum error acts on all quantum gates

        Arguments:
            cmd: Command class object
            noise_model: NoiseModel object
        """
        gate = cmd.gate

        if not isinstance(gate, ClassicalInstructionGate):
            # Append new gate to NoiseModel obj
            for qerror in self.noise_model.errors_list:
                if qerror.allgates:
                    qerror._expand_noisy_gates(gate)


    def _is_noisy(self, cmd, noise_obj):
        """
        Returns True if engine should add noise instance after the command

        Arguments:
            cmd: Command class object
            noise_obj: NoiseModel object or KrausError object
        """

        gate = cmd.gate
        qubit_inds = set(q.id for q in cmd.qubits[0])
        control_inds = set(q.id for q in cmd.control_qubits)
        all_qubit_inds = qubit_inds.union(control_inds)

        noisy_qubits = noise_obj.noisy_qubits
        noisy_gates = noise_obj.noisy_gates
        noisy_elements = noisy_gates | noisy_qubits # union of all noisy qubits and gates

        if isinstance(gate, ClassicalInstructionGate):
            # Rules for ClassicalInstructionGate
            if all_qubit_inds <= noisy_qubits and gate in noisy_gates:
                return True

        # elif not bool(noisy_elements):
        elif not bool(noisy_elements):
            # when noisy all_qubit_inds and gates are not specified we consider all of them as pure
            return False

        elif all_qubit_inds <= noisy_qubits:
            # if all_qubit_inds are in noisy qubits
            if not bool(noisy_gates):
                return True
            elif gate in noisy_gates:
                return True
            else:
                return False
        else:
            return False

    def _add_noisy_gate(self, cmd, noise_model):
        """
        Sends command with additional noise to the next engine

        Note: in current version all Kraus operators consider
        to be acting on single qubit. So every kraus_set in kraus_ops
        acts on its own qubit.


        :param
            cmd: Command obj
                contains gate and qubits it acts on
            noise_model: NoiseModel obj
                noise model in main engine
        """

        qubits = [q for qreg in cmd.qubits for q in qreg]
        controls = cmd.control_qubits
        gate_qubits = controls + qubits

        # initialize lists for qerrors before and after gate
        cmd_before_gate = []
        cmd_after_gate = []

        for qerror in noise_model.errors_list:

            # if particular error affects the command, add noise
            if self._is_noisy(cmd, qerror):

                if len(gate_qubits) == len(qerror.kraus_ops):
                    kraus_ops = self._generate_error_instance(qerror)
                    new_cmd = self._generate_command(kraus_ops, gate_qubits, self.next_engine)
                    if qerror.position == 'before':
                        cmd_before_gate += new_cmd
                    elif qerror.position == 'after':
                        cmd_after_gate += new_cmd

                elif len(qerror.kraus_ops) == 1:
                    for qubit in gate_qubits:
                        kraus_ops = self._generate_error_instance(qerror)
                        new_cmd = self._generate_command(kraus_ops, qubit, self.next_engine)
                        if qerror.position == 'before':
                            cmd_before_gate += new_cmd
                        elif qerror.position == 'after':
                            cmd_after_gate += new_cmd

        self.send(cmd_before_gate + [cmd] + cmd_after_gate)

    def _generate_command(self, kraus_ops, qubits, engine):
        """
        Helper function to generate a list of commands consisting of the gate and
        the qubits being acted upon.

        Returns: list
            List of Command objects containing the gate and the qubits.
        """

        if not isinstance(qubits, list):
            qubits = [qubits]

        cmd_list = []

        for kraus_op, qubit in zip(kraus_ops, qubits):
            qubit = kraus_op.make_tuple_of_qureg(qubit)
            cmd_list.append(Command(engine, kraus_op, qubit))

        return cmd_list

    def _generate_error_instance(self, qerror):
        """
        Randomly chooses one Gate from KrausError obj

        Arguments:
            qerror: KrausError obj

        Return:
            kraus_intanse: MatrixGate obj
        """
        # choose one of Kraus Operators randomly
        # np.random.seed(self.rnd_seed)
        kraus_instance = []
        for kraus_set, prob_set in zip(qerror.kraus_ops, qerror.probs):
            kraus_set_len = len(kraus_set)
            kraus_op_ind = np.random.choice(kraus_set_len, p=prob_set)
            kraus_op = kraus_set[kraus_op_ind]
            kraus_instance.append(kraus_op)

        return kraus_instance


    def receive(self, command_list):
        """
        Receives a command list and if command contains noisy gate and qubits,
        it adds Kraus operator according to the current noise model.
        All other commands are sent to next engine.

        :param command_list: list of Commands class objects
        """

        for cmd in command_list:
            # update set of noisy qubits
            self._update_noisy_qubits(cmd, self.noise_model)

            # update set of noisy gates
            if cmd.gate not in self.noise_model.noisy_gates:
                self._update_noisy_gates(cmd, self.noise_model)

            if isinstance(cmd.gate, DeallocateQubitGate):
                # Measure qubit in order to do factorisation
                # of state before deallocation
                qubits = cmd.qubits
                cmd_measure = Command(self.next_engine, MeasureGate(), qubits)
                self.send([cmd_measure])

            # Check that noise model affects the command
            if self._is_noisy(cmd, self.noise_model):
                self._add_noisy_gate(cmd, self.noise_model)
            # if command is noiseless, send it to the next engine
            else:
                self.send([cmd])
