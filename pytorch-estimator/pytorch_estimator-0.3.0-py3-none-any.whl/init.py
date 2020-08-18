import scipy
import scipy.stats as stats

import numpy as np
import torch


def _assert_version():
    vers = scipy.__version__.split(".")
    assert int(vers[0]) == 1
    assert int(vers[1]) >= 2


_assert_version()

del _assert_version


# Took from keras
def _compute_fans(shape):
    # always channels first fmt in pytorch
    data_format = "channels_first"

    if len(shape) == 2:
        # swapped 0 and 1 as pytorch's weight shape is different with keras.
        fan_in = shape[1]
        fan_out = shape[0]
    elif len(shape) in {3, 4, 5}:
        # Assuming convolution kernels (1D, 2D or 3D).
        # TH kernel shape: (depth, input_depth, ...)
        # TF kernel shape: (..., input_depth, depth)
        if data_format == "channels_first":
            receptive_field_size = np.prod(shape[2:])
            fan_in = shape[1] * receptive_field_size
            fan_out = shape[0] * receptive_field_size
        # elif data_format == 'channels_last':
        #     receptive_field_size = np.prod(shape[:-2])
        #     fan_in = shape[-2] * receptive_field_size
        #     fan_out = shape[-1] * receptive_field_size
        else:
            raise ValueError("Invalid data_format: " + data_format)
    else:
        # No specific assumptions.
        fan_in = np.sqrt(np.prod(shape))
        fan_out = np.sqrt(np.prod(shape))
    return fan_in, fan_out


def valiance_scaling(tensor, scale=1.0, mode="fan_in", distribution="normal"):
    """Keras styled lecun normal with truncnorm distribution.
    https://github.com/keras-team/keras/blob/master/keras/initializers.py#L210
    """
    assert mode in ("fan_in", "fan_out", "fan_avg")
    assert distribution in ("normal", "uniform")

    with torch.no_grad():

        fan_in, fan_out = _compute_fans(tensor.shape)

        if mode == "fan_in":
            scale /= max(1.0, fan_in)
        elif mode == "fan_out":
            scale /= max(1.0, fan_out)
        else:
            scale /= max(1.0, float(fan_in + fan_out) / 2)

        if distribution == "normal":
            rnd = stats.truncnorm.rvs(
                -2, 2, loc=0, scale=np.sqrt(scale), size=tensor.shape
            )
            tensor.data = torch.tensor(rnd.astype("f"), device=tensor.device)
        else:
            limit = np.sqrt(3.0 * scale)
            tensor.uniform_(-limit, limit)

        return tensor


def he_normal_(tensor):
    return valiance_scaling(tensor, scale=2.0, mode="fan_in", distribution="normal")


def lecun_normal_(tensor):
    return valiance_scaling(tensor, scale=1.0, mode="fan_in", distribution="normal")


def lecun_uniform_(tensor):
    return valiance_scaling(tensor, scale=1.0, mode="fan_in", distribution="uniform")


def glorot_normal_(tensor):
    return valiance_scaling(tensor, scale=1.0, mode="fan_avg", distribution="normal")


def glorot_uniform_(tensor):
    return valiance_scaling(tensor, scale=1.0, mode="fan_avg", distribution="uniform")
