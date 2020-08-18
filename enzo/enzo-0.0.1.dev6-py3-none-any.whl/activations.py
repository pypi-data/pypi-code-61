"""Activation functions"""

import numpy as np
from .derivatives import with_derivative
from . import derivatives as ddx


@with_derivative(ddx.ddx_relu)
def relu(rows):
    """Apply max(0, n) to each n in `rows`.

    Parameters
    ----------
    rows : array_like
    """
    rows = np.asarray(rows)
    return rows * (rows > 0)


@with_derivative(ddx.ddx_sigmoid)
def sigmoid(rows):
    """Apply 1 / (1 + e ^ -n) to each n in `rows`.

    Parameters
    ----------
    rows : array_like
    """
    rows = np.asarray(rows)
    return 1 / (1 + np.exp(-rows))


@with_derivative(ddx.ddx_noactivation)
def noactivation(rows):
    """Do nothing, return `rows`."""
    return rows


def _softmax(row):
    raised_to_the_e = np.exp(row)
    return raised_to_the_e / sum(raised_to_the_e)


@with_derivative(ddx.ddx_softmax)
def softmax(rows):
    """Perform softmax scaling for each row in `rows`."""
    rows = np.asarray(rows)
    return np.apply_along_axis(_softmax, arr=rows, axis=1)
