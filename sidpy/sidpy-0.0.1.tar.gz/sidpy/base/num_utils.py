# -*- coding: utf-8 -*-
"""
Utilities that assist in writing scientific data to HDF5 files

Created on Thu Sep  7 21:14:25 2017

@author: Suhas Somnath, Chris Smith
"""

from __future__ import division, print_function, unicode_literals, absolute_import
import sys
from itertools import groupby
import numpy as np

if sys.version_info.major == 3:
    from collections.abc import Iterable
    unicode = str
    xrange = range
else:
    from collections import Iterable

__all__ = ['get_slope', 'to_ranges', 'contains_integers', 'integers_to_slices',
           'get_exponent']


def get_slope(values, tol=1E-3):
    """
    Attempts to get the slope of the provided values. This function will be handy
    for checking if a dimension has been varied linearly or not.
    If the values vary non-linearly, a ValueError will be raised

    Parameters
    ----------
    values : array-like
        List of numbers
    tol : float, optional. Default = 1E-3
        Tolerance in the variation of the slopes.
    Returns
    -------
    float
        Slope of the line
    """
    if not isinstance(tol, float):
        raise TypeError('tol should be a float << 1')
    step_size = np.unique(np.diff(values))
    if len(step_size) > 1:
        # often we end up here. In most cases,
        step_avg = step_size.max()
        step_size -= step_avg
        var = np.mean(np.abs(step_size))
        if var / step_avg < tol:
            step_size = [step_avg]
        else:
            # Non-linear dimension! - see notes above
            raise ValueError('Provided values cannot be expressed as a linear trend')
    return step_size[0]


def to_ranges(iterable):
    """
    Converts a sequence of iterables to range tuples

    From https://stackoverflow.com/questions/4628333/converting-a-list-of-integers-into-range-in-python

    Credits: @juanchopanza and @luca

    Parameters
    ----------
    iterable : collections.Iterable object
        iterable object like a list

    Returns
    -------
    iterable : generator object
        Cast to list or similar to use
    """
    iterable = sorted(set(iterable))
    for key, group in groupby(enumerate(iterable), lambda t: t[1] - t[0]):
        group = list(group)
        if sys.version_info.major == 3:
            yield range(group[0][1], group[-1][1]+1)
        else:
            yield xrange(group[0][1], group[-1][1]+1)


def contains_integers(iter_int, min_val=None):
    """
    Checks if the provided object is iterable (list, tuple etc.) and contains integers optionally greater than equal to
    the provided min_val

    Parameters
    ----------
    iter_int : :class:`collections.Iterable`
        Iterable (e.g. list, tuple, etc.) of integers
    min_val : int, optional, default = None
        The value above which each element of iterable must possess. By default, this is ignored.

    Returns
    -------
    bool
        Whether or not the provided object is an iterable of integers
    """
    if not isinstance(iter_int, Iterable):
        raise TypeError('iter_int should be an Iterable')
    if len(iter_int) == 0:
        return False

    if min_val is not None:
        if not isinstance(min_val, (int, float)):
            raise TypeError('min_val should be an integer. Provided object was of type: {}'.format(type(min_val)))
        if min_val % 1 != 0:
            raise ValueError('min_val should be an integer')

    try:
        if min_val is not None:
            return np.all([x % 1 == 0 and x >= min_val for x in iter_int])
        else:
            return np.all([x % 1 == 0 for x in iter_int])
    except TypeError:
        return False


def integers_to_slices(int_array):
    """
    Converts a sequence of iterables to a list of slice objects denoting sequences of consecutive numbers

    Parameters
    ----------
    int_array : :class:`collections.Iterable`
        iterable object like a :class:`list` or :class:`numpy.ndarray`

    Returns
    -------
    sequences : list
        List of :class:`slice` objects each denoting sequences of consecutive numbers
    """
    if not contains_integers(int_array):
        raise ValueError('Expected a list, tuple, or numpy array of integers')

    def integers_to_consecutive_sections(integer_array):
        """
        Converts a sequence of iterables to tuples with start and stop bounds

        @author: @juanchopanza and @luca from stackoverflow

        Parameters
        ----------
        integer_array : :class:`collections.Iterable`
            iterable object like a :class:`list`

        Returns
        -------
        iterable : :class:`generator`
            Cast to list or similar to use

        Note
        ----
        From https://stackoverflow.com/questions/4628333/converting-a-list-of-integers-into-range-in-python
        """
        integer_array = sorted(set(integer_array))
        for key, group in groupby(enumerate(integer_array),
                                  lambda t: t[1] - t[0]):
            group = list(group)
            yield group[0][1], group[-1][1]

    sequences = [slice(item[0], item[1] + 1) for item in integers_to_consecutive_sections(int_array)]
    return sequences


def get_exponent(vector):
    """
    Gets the scale / exponent for a sequence of numbers. This is particularly useful when wanting to scale a vector
    for the purposes of plotting

    Parameters
    ----------
    vector : array-like
        Array of numbers

    Returns
    -------
    exponent : int
        Scale / exponent for the given vector
    """
    if not isinstance(vector, np.ndarray):
        raise TypeError('vector should be of type numpy.ndarray. Provided object of type: {}'.format(type(vector)))
    if np.max(np.abs(vector)) == np.max(vector):
        exponent = np.log10(np.max(vector))
    else:
        # negative values
        exponent = np.log10(np.max(np.abs(vector)))
    return int(np.floor(exponent))