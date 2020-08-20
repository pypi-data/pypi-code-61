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
"""
get_expectation_value function compatible with hiq-circuit-service backend.

"""

from projectq.cengines import _schedule_small_terms, _schedule_big_terms


def apply_qubit_operator(eng, qubit_operator, qureg):
    """
    Apply a qubit_operator to the current wave function represented
    by the supplied quantum register.

    Args:
        eng (MainEngine): Main compiler engine to run this function on.
        qubit_operator (projectq.ops.QubitOperator): Operator to measure
        qureg (Qureg|list[Qubit]): Quantum register determining the ordering.
            Must contain all allocated qubits.

    Example:
        Apply a qubit_operator to the current wave function.

     .. code-block:: python

        from projectq import MainEngine
        from projectq.backends import SimulatorMPI
        from projectq.cengines import HiQMainEngine, GreedyScheduler
        from projectq.ops import QubitOperator, All, Measure
        from hiq.libs import apply_qubit_operator

        qubit_operator = 0.3 * QubitOperator('X0 X1 X2') + 0.5 * QubitOperator('Y0 Y1 Y2 Y3 Y4') + /
                         QubitOperator('Z0 Z2') + QubitOperator('X0 X3 X4') + QubitOperator('Z1 Z2 Z4')

        # make the compiler and use the SimulatorMPI as a backend
        sim = SimulatorMPI(gate_fusion=True)
        eng = MainEngine(backend=sim, engine_list=[GreedyScheduler()], verbose=True)

        qureg = eng.allocate_qureg(5)
        apply_qubit_operator(eng, qubit_operator, qureg)

        All(Measure) | qureg
        del qureg

    """
    eng.backend._app_qubit_oper(*schedule_terms(eng, qubit_operator, qureg))


def get_expectation_value(eng, qubit_operator, qureg):
    """
    Get the expectation value of qubit_operator with respect to the current wave function
    represented by the supplied quantum register.

    Args:
        eng (MainEngine): Main compiler engine to run this function on.
        qubit_operator (projectq.ops.QubitOperator): Operator to measure
        qureg (Qureg|list[Qubit]): Quantum register determining the ordering.
            Must contain all allocated qubits.

    Returns:
            Expectation value

    Example:
        Get expectation value of Hamiltonian represented by qubit_operator.

     .. code-block:: python

        from projectq import MainEngine
        from projectq.backends import SimulatorMPI
        from projectq.cengines import HiQMainEngine, GreedyScheduler
        from projectq.ops import QubitOperator, All, Measure
        from hiq.libs import get_expectation_value

        qubit_operator = 0.3 * QubitOperator('X0 X1 X2') + 0.5 * QubitOperator('Y0 Y1 Y2 Y3 Y4') + /
                         QubitOperator('Z0 Z2') + QubitOperator('X0 X3 X4') + QubitOperator('Z1 Z2 Z4')

        # make the compiler and use the SimulatorMPI as a backend
        sim = SimulatorMPI(gate_fusion=True)
        eng = MainEngine(backend=sim, engine_list=[GreedyScheduler()], verbose=True)

        qureg = eng.allocate_qureg(5)
        res = get_expectation_value(eng, qubit_operator, qureg)
        print(res)

        All(Measure) | qureg
        del qureg

    """
    expect = 0.0
    expect += eng.backend._get_exp_value(*schedule_terms(eng, qubit_operator, qureg))
    return expect


def schedule_terms(eng, qubit_operator, qureg):
    """
    Split terms into Small and Big terms and calculate a permutation of terms.

    Args:
        eng (MainEngine): Main compiler engine to run this function on.
        qubit_operator (projectq.ops.QubitOperator): Operator to measure
        qureg (Qureg|list[Qubit]): Quantum register determining the ordering.
            Must contain all allocated qubits.

    Returns:
         pairs (list[list]): Qubit pairs to swap
         terms2send (list[tuple]): Array of terms
         coeff2send (list[float]): Array of terms coefficients
         flag (list[int]): Unified schedule for terms and qubit swaps
    """
    simulator = eng.backend
    n_local = len(simulator.get_local_qubits_ids())

    small_terms = []
    big_terms = []

    for t, c in qubit_operator.terms.items():  # splitting terms
        qs = set([g[0] for g in t])
        if len(qs) <= n_local:
            small_terms.append((t, c))
        else:
            big_terms.append((t, c))

    # terms scheduling
    pairs, terms2send, coeff2send, flag, local_qubits, global_qubits = _schedule_small_terms(small_terms, qureg, simulator)

    pairs4big, terms2send4big, coeff2send4big, flag_big = _schedule_big_terms(big_terms, local_qubits, global_qubits, qureg)

    for pair in pairs4big:
        pairs.append(pair)

    for term in terms2send4big:
        terms2send.append(term)

    for c in coeff2send4big:
        coeff2send.append(c)

    for f in flag_big:
        flag.append(f)

    return pairs, terms2send, coeff2send, flag
