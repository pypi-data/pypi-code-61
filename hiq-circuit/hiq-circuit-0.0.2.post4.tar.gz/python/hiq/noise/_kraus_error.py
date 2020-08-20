import numpy as np
import itertools as it

from projectq.ops import BasicGate, MatrixGate


class OperatorClassError(Exception):
    pass


class KrausError(object):
    """
    Class for CPTP error channels specified by Kraus operators
    """

    _tol = 1e-10  # tolerance for rounding errors

    def __init__(self, kraus_ops, probs=None, noisy_gates=None, noisy_qubits=None, name=None):
        """
        Initialize error channel in terms of Kraus sum representation

        Arguments:
            kraus_ops: list
                should has the form [K_0, K_1, ...] where K_i is Kraus Operators
                belong to BasicGate object;
                or should has the form [[K_0, K_1, ...], ]
            probs: list or None
                is list of floats corresponding to probability of using certain
                Kraus operator during single run of quantum circuit
                has form [p_0, p_1, ...]
                or      [[p_0, p_1, ...], ]
                if probs is None, it will be computed automatically
        """

        # Check that all Kraus operators are belong to BasicGate objects
        if not isinstance(kraus_ops, list):
            raise OperatorClassError("Invalid kraus_ops value. "
                                     "Provide [K_0, ...] or [[K_0, ...], ] form")
        elif all(isinstance(kraus_set, BasicGate) for kraus_set in kraus_ops):
            # convert to format [[K_0, ...], ]
            kraus_ops = [kraus_ops]
        elif not all(isinstance(k, BasicGate) for kraus_set in kraus_ops for k in kraus_set):
            raise OperatorClassError("Elements of kraus_ops should be "
                                     "BasicGate objects.")

        if probs is None:
            # normalize Kraus operators and compute corresponding probabilities
            kraus_ops, probs = self._set_probabilities(kraus_ops)
            # if not self._if_all_cptp(kraus_ops, probs):
            #     raise OperatorClassError("Bug in the code")
        else:
            if all(isinstance(p, float) for p in probs):
                # convert to [[p_0, ...], ] format
                probs = [probs]

            # check the length of probs and kraus_ops
            if len(kraus_ops) != len(probs):
                raise OperatorClassError("kraus_ops and probs have different length")

            # check that every kraus_set and prob_set have the same length
            elif not all(len(kraus_set) == len(prob_set) for
                         kraus_set, prob_set in zip(kraus_ops, probs)):
                raise OperatorClassError("kraus_set should has the same length as "
                                         "corresponding prob_set")
            # check that channel is CPTP
            if not self._if_all_cptp(kraus_ops, probs):
                raise OperatorClassError("Provided Kraus operators do not belong to CPTP set.")

        self._kraus_ops = kraus_ops
        self._probs = probs
        self._noisy_qubits = set()
        self._allqubits = True
        self._noisy_gates = set()
        self._allgates = True
        self.name = name
        self.position = 'after'

        if noisy_gates is not None and len(noisy_gates) > 0:
            self.add_noisy_gates(noisy_gates)
        if noisy_qubits is not None and len(noisy_qubits) > 0:
            self.add_noisy_qubits(noisy_qubits)
        #     self._noisy_qubits = set(noisy_qubits)
        #     self._allqubits = False
        # else:
        #     self._noisy_qubits = set()

    def _if_cptp(self, kraus_set, probs_set):
        """
        Returns True if set of Kraus operators represents Completely Positive
        Trace Preserving channel.

        Arguments:
            kraus_set: list of (matrices | MatrixGate)
                contains Kraus operators of channel
            probs_set: (list | None)
                contains probability of applying certain operator
                during simulation
        """

        # kraus_set = [op.matrix if isinstance(op, MatrixGate) \
        #                      else np.matrix(op) for op in kraus_set]
        kraus_set_matr = [op.matrix for op in kraus_set]

        d = len(kraus_set_matr[0])
        kraus_sum = np.zeros((d, d))
        for ind, op in enumerate(kraus_set_matr):
            op_dagg = np.conjugate(np.transpose(op))

            if probs_set is None:
                kraus_sum = kraus_sum + np.dot(op_dagg, op)
            else:
                kraus_sum = kraus_sum + probs_set[ind] * np.dot(op_dagg, op)

        abs_dif = np.abs(kraus_sum - np.eye(d))
        if np.sum(abs_dif) < self._tol:
            return True
        else:
            return False

    def _if_all_cptp(self, kraus_ops, probs):
        """
        Returns True if all sets of Kraus operators in channel represents
        Completely Positive Trace Preserving channel.

        :param kraus_ops: list
            List of kraus_sets. Has the form [[K_0, K_1, ...], ]
        :param probs: (list | None)
             contains lists of corresponding probabilities of applying
             certain operator during one run of simulation
        """

        if all(self._if_cptp(kraus_set, prob_set) for kraus_set, prob_set
               in zip(kraus_ops, probs)):
            return True
        else:
            return False

    def _set_probabilities(self, kraus_ops):
        """
        Normalizes Kraus Operators and compute corresponding probabilities

        :param:
            kraus_ops: list
                Has the form [[K_0, K_1, ...], ] where K_i is BasicGate object
        :return:
            rescaled_ops: list of MatrixGate objects
                list of normalized Kraus operators
            probabilities: list
                list of probabilities corresponding to Kraus operators
        """

        probabilities = []
        rescaled_ops = []
        for kraus_set in kraus_ops:
            prob_set = []
            rescaled_kraus_set = []
            for op in kraus_set:
                op_mat = op.matrix
                prob = abs(max(np.diag(np.conj(np.transpose(op_mat)).dot(op_mat))))
                if prob > 0:
                    prob_sqrt = np.sqrt(prob)
                    rescaled_op = np.array(op_mat) / prob_sqrt
                    rescaled_kraus_set.append(MatrixGate(rescaled_op))
                    prob_set.append(prob)

            rescaled_ops.append(rescaled_kraus_set)

            # normalize probabilities
            prob_set = list(np.array(prob_set) / np.array(prob_set).sum())
            probabilities.append(prob_set)

        # probabilities = list(np.sqrt(probabilities))

        return rescaled_ops, probabilities

    @property
    def kraus_ops(self):
        return self._kraus_ops

    @property
    def probs(self):
        return self._probs

    @property
    def noisy_qubits(self):
        return self._noisy_qubits

    @property
    def noisy_gates(self):
        return self._noisy_gates

    @property
    def allqubits(self):
        return self._allqubits

    @property
    def allgates(self):
        return self._allgates

    def _expand_noisy_qubits(self, qubit_inds):
        """
        Adds indexes of noisy qubits which are affected by noise error.
        When new qubit is allocated by noise engine, its index will be
        added to noise error.

        qubit_inds: list of ints
            indexes of qubits in quantum register
        """
        if not isinstance(qubit_inds, (int, list, set)):
            raise OperatorClassError("qubit_inds should be int or list")

        elif isinstance(qubit_inds, int):
            qubit_inds = [qubit_inds]

        elif isinstance(qubit_inds, (list, set)):
            if not all(isinstance(elm, int) for elm in qubit_inds):
                raise OperatorClassError("qubit_inds should be list of integers")

        self._noisy_qubits = self._noisy_qubits.union(qubit_inds)

    def add_noisy_qubits(self, qubit_inds):
        """
        Adds indexes of noisy qubits which are affected by noise error.
        After adding noisy_qubits indexes, new allocated qubits will
        not be affected by this noise error.

        qubit_inds: list of ints
            indexes of qubits in quantum register
        """

        self._expand_noisy_qubits(qubit_inds)
        self._allqubits = False

    def set_noisy_qubits(self, qubit_inds):
        """
        Changes indexes of noisy qubits to provided ones.
        After this command new allocated qubits will
        not be affected by this noise error.

        qubit_inds: list of ints
            indexes of qubits in quantum register
        """
        self._noisy_qubits = set()
        self.add_noisy_qubits(qubit_inds)

    def _expand_noisy_gates(self, noisy_gates):
        """
        Expands noisy gates which are affected by noise error.

        Arguments:
            noisy_gates: (BasicGate obj | list of BasicGate obj)
                list of gates that are affected by the qerror
        """

        # check that all gates belongs to BasicGate class
        if not isinstance(noisy_gates, (list, tuple, set)):
            if not isinstance(noisy_gates, BasicGate):
                raise OperatorClassError("Noisy gate should belong to BasicGate class")
            noisy_gates = [noisy_gates]
        elif not all(isinstance(gate, BasicGate) for gate in noisy_gates):
            raise OperatorClassError("Noisy gates should belong to BasicGate class")

        provided_gates = set(noisy_gates)
        self._noisy_gates |= provided_gates

    def add_noisy_gates(self, noisy_gates):
        """
        Adds noisy gates which are affected by noise error, and
        set allgates parameter to False

        Arguments:
            noisy_gates: (BasicGate obj | list of BasicGate obj)
        """
        self._expand_noisy_gates(noisy_gates)
        self._allgates = False

    def set_noisy_gates(self, noisy_gates):
        """
        Changes set of noisy qubits of qerror to noisy_gates

        Arguments:
            noisy_gates: (BasicGate obj | list of BasicGate obj)
        """
        self._noisy_gates = set()
        self.add_noisy_gates(noisy_gates)

    def compose(self, other):
        """
        Composition of two sequential errors.
            Note: order of errors matters.

        :param other: KrausError obj
            Other error channel which is applied after self
        :return: KrausError obj
        """

        # check that other belongs to KrausError class
        if not isinstance(other, KrausError):
            raise OperatorClassError("Other is not a KrausError class object")

        # check that self and other have the same dimensionality
        if len(self.kraus_ops) != len(other.kraus_ops):
            raise OperatorClassError("Quantum errors have different dimensionality")

        # Create list of operators composition
        kraus_ops_compose = []
        probs_compose = []

        for ind in range(len(self.kraus_ops)):

            kraus_set_compose = []
            probs_set_compose = []

            len0 = len(self.kraus_ops[ind])
            len1 = len(other.kraus_ops[ind])
            for ind0, ind1 in it.product(range(len0), range(len1)):
                op_0 = self.kraus_ops[ind][ind0]
                p0 = self.probs[ind][ind0]
                op_1 = other.kraus_ops[ind][ind1]
                p1 = other.probs[ind][ind1]

                # create new operator
                op_compose_matrix = np.dot(op_0.matrix, op_1.matrix)
                op_compose = MatrixGate(op_compose_matrix)
                kraus_set_compose.append(op_compose)

                # compute corresponding probability
                probs_set_compose.append(p0 * p1)

            # append kraus_set and probs_set to list of operators and probabilities
            kraus_ops_compose.append(kraus_set_compose)
            probs_compose.append(probs_set_compose)

        return KrausError(kraus_ops_compose, probs=probs_compose)

    def _tensor_product(self, other, inverse=False):
        """
        Tensor product of two noise channels in form
        self x other if inverse = False or
        other x self if inverse = True

        Note: order of errors matters

        :param other: KrausError obj
            Other error channel which is applied to another qubit
        :return: KrausError obj
        """

        # check that other belongs to KrausError class
        if not isinstance(other, KrausError):
            raise OperatorClassError("Other is not a KrausError class object")

        if not inverse:
            new_kraus_ops = self.kraus_ops + other.kraus_ops
            new_probs = self.probs + other.probs
        else:
            new_kraus_ops = other.kraus_ops + self.kraus_ops
            new_probs = other.probs + self.probs

        new_noisy_gates = self.noisy_gates.union(other.noisy_gates)
        new_noisy_qubits = self.noisy_qubits.union(other.noisy_qubits)

        new_error = KrausError(new_kraus_ops,
                               probs=new_probs,
                               noisy_gates=new_noisy_gates,
                               noisy_qubits=new_noisy_qubits)
        return new_error

    def tensor(self, other):
        """
        Tensor product of two noise channels in form
        self x other

        :param other: KrausError obj
            Other error channel which is applied to another qubit
        :return: KrausError obj
        """
        return self._tensor_product(other)

    def expand(self, other):
        """
        Tensor product of two noise channels in form
        other x self

        :param other: KrausError obj
            Other error channel which is applied to another qubit
        :return: KrausError obj
        """
        return self._tensor_product(other, inverse=True)

    def __str__(self):
        q_indexes = 'ijklmnopqrstu'
        result = ''
        if self.name is not None:
            result += f'{self.name}\n'
        for ind in range(len(self.kraus_ops)):
            result += f'qubit {q_indexes[ind]} : '
            for kraus_op, prob in zip(self.kraus_ops[ind], self.probs[ind]):
                result += f'p={prob} -> {kraus_op}; '
            result += '\n'
        # print noisy gates
        result += 'noisy gates: '
        if len(self.noisy_gates) > 0:
            for gate in self.noisy_gates:
                result += f'{gate}, '
            result += '\n'
        else:
            result += 'all\n'
        # print noisy qubits
        result += 'noisy qubits: '
        if len(self.noisy_qubits) > 0:
            result += str(self.noisy_qubits)
            result += '\n'
        else:
            result += 'all\n'

        return result
