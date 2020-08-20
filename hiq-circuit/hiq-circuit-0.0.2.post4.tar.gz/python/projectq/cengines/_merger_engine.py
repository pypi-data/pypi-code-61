#   Copyright 2017 ProjectQ-Framework (www.projectq.ch)
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
from projectq.cengines import BasicEngine
from projectq.ops import Command, MeasureGate
from projectq.types import Qureg


class MergerEngine(BasicEngine):
    """
    MergerEngine is a compiler engine which applies a filter function to all
    incoming commands, joining commands of a certain type and sending on them
    as one resulting command.

    It skips other commands and sends them to the next engine unchanged.
    """
    def __init__(self, cmd_predicate):
        """
        Initialize the CommandFilter.

        Args:
            cmd_predicate (function): Function which, given a command cmd,
                returns True or False.

        Example:
            .. code-block:: python

                def  cmd_filter(cmd):
                    if isinstance(cmd.gate, MeasureGate):
                        return True
                    else:
                        return False
                compiler_engine = CommandFilter(cmd_filter)
                ...
        """
        BasicEngine.__init__(self)
        self._cmd_predicate = cmd_predicate
        self._received_commands = []
        self._merged_ids = set()
        self._merged_ctrl_ids = set()
        self._merged_tags = []

    def receive(self, command_list):
        for cmd in command_list:
            if self._cmd_predicate(cmd):
                self._received_commands.append(cmd)
            else:
                if self._received_commands:
                    self._merge_commands()
                    new_command_list = [Command(engine=self.main_engine, gate=self._received_commands[0].gate,
                                                qubits=(Qureg(list(self._merged_ids)),), controls=list(self._merged_ctrl_ids), tags=self._merged_tags)]
                    self.send(new_command_list)
                    self._received_commands.clear()
                self.send([cmd])

    def _merge_commands(self):
        self._merged_ids.clear()
        self._merged_ctrl_ids.clear()
        self._merged_tags.clear()
        for com in self._received_commands:
            for qr in com.qubits:
                for q in qr:
                    assert q not in self._merged_ids
                    self._merged_ids.add(q)
            for conq in com.control_qubits:
                assert conq not in self._merged_ctrl_ids
                self._merged_ctrl_ids.add(conq)
            for t in com.tags:
                self._merged_tags.append(t)


def is_merge_gate(cmd):
    if isinstance(cmd.gate, MeasureGate):
        return True
    else:
        return False


MeasureMerger = MergerEngine(is_merge_gate)
