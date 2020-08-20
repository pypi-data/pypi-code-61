import numpy as np
from scipy.optimize import least_squares
import matplotlib.pyplot as plt

class LinearMitigating(object):
    def __init__(self, operations, noise_engine, main_engine, n_qubits):
        self.operations = operations
        self.engine = main_engine
        self.noise_engine = noise_engine
        self.n_qubits = n_qubits

    def mitigated_measurment(self):
        qreg = self.engine.allocate_qureg(self.n_qubits)

        values_different_noise = []
        c = np.arange(1.0, 9.0, 0.5)
        for i in range(len(c)):
            k = c[i]
            k1 = c[i - 1]
            for error in self.noise_engine.noise_model.errors_list:
                if i != 0:
                    error._probs[0][0] *= k / k1
                    error._probs[0][1] = 1 - error._probs[0][0]
            value = self.operations(qreg, self.n_qubits)
            values_different_noise.append(value)

        for error in self.noise_engine.noise_model.errors_list:
            error._probs[0][0] *= 0
            error._probs[0][1] = 1
        value_true = self.operations(qreg, self.n_qubits)

        def func(params, x=None):
            a = params[0]
            b = params[1]
            if x is None:
                value = a * c + b
                return np.array(values_different_noise) - value
            else:
                return a * x + b

        params = least_squares(func, [1.0, 1.0]).x

        y0 = func(params, 0.0)

        plt.plot([0], value_true, color='blue', marker='o', label='Noise-free')
        plt.plot(c, values_different_noise, color='red', marker='o', linestyle='', label='Noisy')
        plt.plot([0], [y0], color='green', marker='o', linestyle='', label='Mitigated')
        x = np.arange(0.0, c[-1], 0.01)
        plt.plot(x, func(params, x), color='red', linestyle='--', label='Approximation')

        plt.ylabel('Value of observable')
        plt.xlabel("Error rate's coefficient")
        plt.title("Linear extrapolation")
        plt.legend()

        plt.show()

        return y0

class ExponentialMitigating(object):
    def __init__(self, operations, noise_engine, main_engine, n_qubits):
        self.operations = operations
        self.engine = main_engine
        self.noise_engine = noise_engine
        self.n_qubits = n_qubits

    def mitigated_measurment(self):
        qreg = self.engine.allocate_qureg(self.n_qubits)

        values_different_noise = []
        c = np.arange(1.0, 9.0, 0.5)
        for i in range(len(c)):
            k = c[i]
            k1 = c[i - 1]
            for error in self.noise_engine.noise_model.errors_list:
                if i != 0:
                    error._probs[0][0] *= k / k1
                    error._probs[0][1] = 1 - error._probs[0][0]
            value = self.operations(qreg, self.n_qubits)
            values_different_noise.append(value)

        for error in self.noise_engine.noise_model.errors_list:
            error._probs[0][0] *= 0
            error._probs[0][1] = 1
        value_true = self.operations(qreg, self.n_qubits)

        def func(params, x=None):
            a = params[0]
            b = params[1]
            C = params[2]
            if x is None:
                value = a * np.exp(-b * c) + C
                return np.array(values_different_noise) - value
            else:
                return a * np.exp(-b * x) + C

        params = least_squares(func, [1.0, 1.0, 1.0]).x

        y0 = func(params, 0.0)

        plt.plot([0], value_true, color='blue', marker='o', label='Noise-free')
        plt.plot(c, values_different_noise, color='red', marker='o', linestyle='', label='Noisy')
        plt.plot([0], [y0], color='green', marker='o', linestyle='', label='Mitigated')
        x = np.arange(0.0, c[-1], 0.01)
        plt.plot(x, func(params, x), color='red', linestyle='--', label='Approximation')

        plt.ylabel('Value of observable')
        plt.xlabel("Error rate's coefficient")
        plt.title("Exponential extrapolation")
        plt.legend()

        plt.show()

        return y0


class RichardsonMitigating(object):
    def __init__(self, operations, noise_engine, main_engine, n_qubits):
        self.operations = operations
        self.engine = main_engine
        self.noise_engine = noise_engine
        self.n_qubits = n_qubits

    def mitigated_measurment(self):
        qreg = self.engine.allocate_qureg(self.n_qubits)

        values_different_noise = []
        c = np.arange(1.0, 4.0, 1.0)
        for i in range(len(c)):
            k = c[i]
            k1 = c[i - 1]
            for error in self.noise_engine.noise_model.errors_list:
                if i != 0:
                    error._probs[0][0] *= k / k1
                    error._probs[0][1] = 1 - error._probs[0][0]
            value = self.operations(qreg, self.n_qubits)
            values_different_noise.append(value)

        for error in self.noise_engine.noise_model.errors_list:
            error._probs[0][0] *= 0
            error._probs[0][1] = 1
        value_true = self.operations(qreg, self.n_qubits)

        n = len(c)
        sys_matrix = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                sys_matrix[i][j] = c[j] ** i

        b = np.zeros(n)
        b[0] = 1
        gamma = np.linalg.solve(sys_matrix, b)
        y0 = np.sum(gamma * np.flip(np.array(values_different_noise)))

        plt.plot([0], value_true, color='blue', marker='o', label='Noise-free')
        plt.plot(c, values_different_noise, color='red', marker='o', linestyle='', label='Noisy')
        plt.plot([0, c[0]], [y0, values_different_noise[0]], color='red', marker='',
                 linestyle='--')
        x = np.arange(0.0, c[-1], 0.01)
        plt.plot([0], [y0], color='green', marker='o', label='Mitigated')

        plt.ylabel('Value of observable')
        plt.xlabel("Error rate's coefficient")
        plt.title("Richardson extrapolation")
        plt.legend()

        plt.show()

        return y0
