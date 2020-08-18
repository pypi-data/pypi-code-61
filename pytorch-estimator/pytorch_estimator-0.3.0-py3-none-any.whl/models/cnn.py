from copy import copy
import math

import torch.nn as nn
import torch.nn.functional as F
from .. import init
from ..modules import flatten, global_avg_pool


class conv(nn.Module):
    def __init__(
        self,
        in_channels,
        out_channels,
        kernel_size=1,
        stride=1,
        padding=0,
        dilation=1,
        dropout=0,
        bias=True,
        activation="relu",
    ):
        super().__init__()

        self.conv = nn.Conv1d(
            in_channels,
            out_channels,
            kernel_size=kernel_size,
            stride=stride,
            padding=padding,
            dilation=dilation,
            bias=bias,
        )

        self.act = getattr(F, activation, lambda x: x)

        init.glorot_uniform_(self.conv.weight)
        self.dropout = nn.Dropout(dropout)

        if bias:
            nn.init.constant_(self.conv.bias, 0)

    def forward(self, x):

        return self.dropout(self.act(self.conv(x)))


class dense(nn.Module):
    def __init__(self, input_dim, output_dim, bias=True, dropout=0, activation="relu"):
        super().__init__()

        self.dense = nn.Linear(input_dim, output_dim, bias=bias)

        self.act = getattr(F, activation, lambda x: x)

        init.glorot_uniform_(self.dense.weight)
        self.dropout = nn.Dropout(dropout)

        if bias:
            nn.init.constant_(self.dense.bias, 0)

    def forward(self, x):
        return self.dropout(self.act(self.dense(x)))


modules = dict(
    conv=conv,
    flatten=flatten,
    global_avg_pool=global_avg_pool,
    dense=dense,
    output=dense,
)


def _shape_to_input_dim(input_shape):
    if isinstance(input_shape, (list, tuple)):

        if isinstance(input_shape[0], (list, tuple)):
            raise ValueError("not suppots list / tuple inputs")
        return input_shape[0]

    raise ValueError("not supported input types")


class CNN(nn.Module):
    def __init__(self, input_shape, output_shape, **mp):
        super().__init__()
        self.mp = mp
        layers = []
        for i, layer in enumerate(self.mp["layers"]):
            layer = copy(layer)
            kind = layer.pop("layer")

            if i == 0:
                layer["in_channels"] = _shape_to_input_dim(input_shape)

            if kind == "output":
                assert output_shape[0] > 0
                layer["output_dim"] = output_shape[0]

            layers.append(modules[kind](**layer))

        self.seq = nn.Sequential(*layers)

    @property
    def complexity(self) -> float:
        # Approximation of the Rademacher complexity
        return math.sqrt(float(len(self.mp["layers"]) - 1))

    def forward(self, x, *args, **kwargs):
        return self.seq(x)
