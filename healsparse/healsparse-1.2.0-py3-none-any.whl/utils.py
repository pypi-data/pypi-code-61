import numpy as np
import healpy as hp
import warnings
import numbers

WIDE_NBIT = 8
WIDE_MASK = np.uint8


def reduce_array(x, reduction='mean', axis=2):
    """
    Auxiliary method to perform one of the following operations:
    nanmean, nanmax, nanmedian, nanmin, nanstd

    Args:
    ----
    x: `ndarray`
        input array in which to perform the operation
    reduction: `str`
        reduction method. Valid options: mean, median, std, max, min, and, or
        (default: mean).
    axis: `int`
        axis in which to perform the operation (default: 2)

    Returns:
    --------
    out: `ndarray`.
    """
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore', category=RuntimeWarning)
        if reduction == 'mean':
            ret = np.nanmean(x, axis=axis).ravel()
        elif reduction == 'median':
            ret = np.nanmedian(x, axis=axis).ravel()
        elif reduction == 'std':
            ret = np.nanstd(x, axis=axis).ravel()
        elif reduction == 'max':
            ret = np.nanmax(x, axis=axis).ravel()
        elif reduction == 'min':
            ret = np.nanmin(x, axis=axis).ravel()
        elif reduction == 'and':
            # ravel does not yield the same format as wide_mask
            ret = np.bitwise_and.reduce(x, axis=axis).ravel()
        elif reduction == 'or':
            ret = np.bitwise_or.reduce(x, axis=axis).ravel()
        else:
            raise ValueError('Reduction method %s not recognized.' % reduction)

    return ret


def check_sentinel(type, sentinel):
    """
    Check if the sentinel value works for the given dtype.

    Parameters
    ----------
    type: `type`
    sentinel: `int`, `float`, or None

    Returns
    -------
    Default sentinel if input is None.

    Raises
    ------
    ValueError if sentinel is of wrong type
    """

    if issubclass(type, np.floating):
        # If we don't have a sentinel, use hp.UNSEEN
        if sentinel is None:
            return hp.UNSEEN
        # If input is a float, we're okay.  Otherwise, Raise.
        if isinstance(sentinel, numbers.Real) and not is_integer_value(sentinel):
            return sentinel
        else:
            raise ValueError("Sentinel not of floating type")
    elif issubclass(type, np.integer):
        # If we don't have a sentinel, MININT
        if sentinel is None:
            return np.iinfo(type).min
        if is_integer_value(sentinel):
            if (sentinel < np.iinfo(type).min or
                    sentinel > np.iinfo(type).max):
                raise ValueError("Sentinel out of range of type")
            return sentinel
        else:
            raise ValueError("Sentinel not of integer type")


def is_integer_value(value):
    """
    Check if a value is an integer type

    Parameters
    ----------
    value : 'Object`
       A value of any type

    Returns
    -------
    is_integer : `bool`
       `True` if is a numpy or python integer.  False otherwise.
    """
    if isinstance(value, numbers.Integral):
        return True
    else:
        return False


def _get_field_and_bitval(bit):
    """
    Get the associated field and shifted bit value for a wide mask

    Parameters
    ----------
    bit : `int`
       Bit position

    Returns
    -------
    field : `int`
       Field index for the shifted bit
    bitval : `healsparse.WIDE_MASK`
       Shifted bit value in its field
    """

    field = bit // WIDE_NBIT
    bitval = WIDE_MASK(np.left_shift(1, bit - field*WIDE_NBIT))

    return field, bitval


def _compute_bitshift(nside_coarse, nside_fine):
    """
    Compute the nest bit shift between a coarse and fine map.

    Parameters
    ----------
    nside_coarse : `int`
       nside of the coarse map
    nside_fine : `int`
       nside of the fine map

    Returns
    -------
    bit_shift : `int`
       Number of bits to shift to convert nest pixels
    """
    return 2*int(np.round(np.log2(nside_fine / nside_coarse)))
