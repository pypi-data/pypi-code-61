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

import numpy as np

from projectq.ops import Id, X, Y, Z, MatrixGate
from ._kraus_error import KrausError, OperatorClassError

_tol = 1e-10  # tolerance for rounding errors


class MixedUnitaryError(KrausError):
    """
    Class for quantum errors represented by unitary operators
    with given probabilities
    """

    def __init__(self, operators_set, probs, noisy_gates=None, noisy_qubits=None, name=None):

        if name is None:
            name = 'MixedUnitaryError'

        KrausError.__init__(self, operators_set, probs, noisy_gates, noisy_qubits, name)


class PauliError(MixedUnitaryError):
    """
    Pauli error channel (mixed unitary)
    """
    def __init__(self, args, noisy_gates=None, noisy_qubits=None, name='PauliError'):
        """
        Initialize Pauli error channel

        Arguments:
            args: list of tuples
                first element of a tuple is str denoting Pauli operators (Id, X, Y, Z)
                second element of the tuple is probability of corresponding operator
        """

        # convert args in lists of operators and probabilities
        kraus_ops = []
        probs = []

        for op, prob in args:
            if op == 'i' or op == 'I' or op == 'Id' or op == 'id':
                kraus_ops.append(Id)
                probs.append(prob)
            elif op == 'x' or op == 'X':
                kraus_ops.append(X)
                probs.append(prob)
            elif op =='y' or op == 'Y':
                kraus_ops.append(Y)
                probs.append(prob)
            elif op == 'z' or op == 'Z':
                kraus_ops.append(Z)
                probs.append(prob)
            else:
                raise OperatorClassError("Provided operators do not belongs to Pauli operators")

        MixedUnitaryError.__init__(self, kraus_ops, probs,
                                   noisy_gates, noisy_qubits, name)


class DepolarizingError(KrausError):
    """
    Depolarizing channel error class
    """

    def __init__(self, param_dep, noisy_gates=None, noisy_qubits=None, name='depolarizing_channel'):
        """
        Initialize depolarizing error. Error do not change the state with probability 1-p and
        returns completely mixed state with probability p

        Arguments:
            param_dep : float [0, 1]
                depolarization probability
        """

        if param_dep > 1 or param_dep < 0:
            raise OperatorClassError("Wrong value of parameter. p should belongs to interval [0, 1]")

        M0 = Id
        M1 = X
        M2 = Y
        M3 = Z

        p_0 = 1 - 0.75 * param_dep
        p_1 = p_2 = p_3 = param_dep / 4.
        probs = [p_0, p_1, p_2, p_3]

        KrausError.__init__(self,
                            kraus_ops=[M0, M1, M2, M3],
                            probs=probs,
                            noisy_gates=noisy_gates,
                            noisy_qubits=noisy_qubits,
                            name=name)
        self.depolarizing_parameter = param_dep


class PhaseAmplitudeDampingError(KrausError):
    """
    Quantum error as a combination of both phase- and amplitude- damping quantum channels
    """

    def __init__(self,
                 param_ampl,
                 param_phase,
                 ground_state_population=1,
                 noisy_gates=None,
                 noisy_qubits=None,
                 name='PhaseAmplitudeDampingError'):
        """

        Arguments:
            param_ampl: (float)
                amplitude damping parameter
            param_phase: (float)
                phase damping parameter
            ground_state_population:
                population of ground state |0> at equilibrium
        """

        # check input parameters
        if param_ampl < 0:
            raise OperatorClassError("Wrong value of amplitude damping parameter. " 
                                     "({} < 0 )".format(param_ampl))
        if param_phase < 0:
            raise OperatorClassError("Wrong value of phase damping parameter. "
                                     "({} < 0)".format(param_phase))
        if param_phase + param_ampl > 1:
            raise OperatorClassError("Wrong value of phase and amplitude damping parameters. "
                                     "({} + {} > 1)".format(param_phase, param_ampl))
        if ground_state_population > 1 or ground_state_population < 0:
            raise OperatorClassError("Wrong value of ground state population. It should belongs to "
                                     "the interval [0, 1]")

        p0 = np.sqrt(ground_state_population)
        p1 = np.sqrt(1 - ground_state_population)
        param_gen = 1 - param_ampl - param_phase

        # Damping to |0> state operators
        A0 = p0 * np.array([[1, 0], [0, np.sqrt(param_gen)]], dtype=complex)
        A1 = p0 * np.array(([[0, np.sqrt(param_ampl)], [0, 0]]), dtype=complex)
        A2 = p0 * np.array(([[0, 0], [0, np.sqrt(param_phase)]]), dtype=complex)

        # Damping to |1> state operators
        B0 = p1 * np.array([[np.sqrt(param_gen), 0], [0, 1]], dtype=complex)
        B1 = p1 * np.array([[0, 0], [np.sqrt(param_ampl), 0]], dtype=complex)
        B2 = p1 * np.array([[np.sqrt(param_phase), 0], [0, 0]], dtype=complex)

        # select non-zero operators
        kraus_ops_set = [op for op in [A0, A1, A2, B0, B1, B2]
                     if np.linalg.norm(op) > 1e-10]
        canonical_kraus_set = _canonical_kraus(kraus_ops_set)
        # kraus_ops = [MatrixGate(op) for op in [A0, A1, A2, B0, B1, B2]
        #              if np.linalg.norm(op) > 1e-10]

        kraus_ops = [MatrixGate(op) for op in canonical_kraus_set]

        KrausError.__init__(self,
                            kraus_ops=kraus_ops,
                            probs=None,
                            noisy_gates=noisy_gates,
                            noisy_qubits=noisy_qubits,
                            name=name)
        self.param_ampl = param_ampl
        self.param_phase = param_phase
        self.ground_population = ground_state_population


class PhaseDampingError(PhaseAmplitudeDampingError):
    """
    Phase damping error channel
    """

    def __init__(self,
                 param_phase,
                 noisy_gates=None,
                 noisy_qubits=None,
                 name='PhaseDampingError'):
        """
        Arguments:
            param_phase: float
                phase damping parameter
        """

        # check phase damping parameter
        if param_phase < 0:
            raise OperatorClassError("Wrong value of phase damping parameter. "
                                     "({} < 0)".format(param_phase))
        if param_phase > 1:
            raise OperatorClassError("Wrong value of phase and amplitude damping parameters. "
                                     "({}> 1)".format(param_phase))

        PhaseAmplitudeDampingError.__init__(self,
                                            param_ampl=0,
                                            param_phase=param_phase,
                                            ground_state_population=1,
                                            noisy_gates=noisy_gates,
                                            noisy_qubits=noisy_qubits,
                                            name=name)


class AmplitudeDampingError(PhaseAmplitudeDampingError):
    """
    Amplitude damping error channel
    """

    def __init__(self,
                 param_ampl,
                 ground_state_population=1,
                 noisy_gates=None,
                 noisy_qubits=None,
                 name='AmplitudeDampingError'):
        """
        Arguments:
            param_ampl: (float)
                phase damping parameter
            ground_state_population:
                population of ground state |0> at equilibrium
        """

        # check input parameters
        if param_ampl < 0:
            raise OperatorClassError("Wrong value of amplitude damping parameter. "
                                     "({} < 0 )".format(param_ampl))
        if param_ampl > 1:
            raise OperatorClassError("Wrong value of amplitude damping parameter. "
                                     "({} > 1)".format(param_ampl))

        if ground_state_population > 1 or ground_state_population < 0:
            raise OperatorClassError("Wrong value of ground state population. It should belongs to "
                                     "the interval [0, 1]")

        PhaseAmplitudeDampingError.__init__(self,
                                            param_ampl=param_ampl,
                                            param_phase=0,
                                            ground_state_population=ground_state_population,
                                            noisy_gates=noisy_gates,
                                            noisy_qubits=noisy_qubits,
                                            name=name)


def _canonical_kraus(kraus_set):
    """
    Returns canonical set of Kraus operators based on eigen decomposition of
    Choi matrix

    Arguments:
        kraus_set ([ndarray, ...]):list of Kraus operators

    Return:
        new_kraus ([ndarray, ...]): list of canonical Kraus operators
    """

    choi_mat = _kraus_to_choi(kraus_set)
    new_kraus = _choi_to_kraus(choi_mat)
    return new_kraus


def _kraus_to_choi(kraus_set):
    """
    Change representation of quantum channel from set of
    Kraus operators to Choi matrix

    Arguments:
        kraus_set ([ndarray, ...]): list of Kraus operators

    Return:
         choi_mat (ndarray): Choi matrix corresponding to channel
    """

    choi_mat = 0
    for k in kraus_set:
        vec = k.ravel(order='F')
        choi_mat += np.outer(vec, vec.conj())
    return choi_mat


def _choi_to_kraus(choi_mat):
    """
    Changes representation of quantum channel from Choi matrix
    to a set of Kraus operators
    """

    # Compute eigendecompostion of Choi-matrix
    w, v = np.linalg.eigh(choi_mat)
    # Check that eigenvalues are non-negative
    if len(w[w < -_tol]) == 0:
        # Kraus-sum representation
        kraus_set = []
        for val, vec in zip(w, v.T):
            if abs(val) > _tol:
                k = np.sqrt(val) * vec.reshape((2, 2), order='F')
                kraus_set.append(k)
        return kraus_set
