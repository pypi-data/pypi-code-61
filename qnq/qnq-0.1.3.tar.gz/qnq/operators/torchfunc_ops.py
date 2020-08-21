# This script contain implentation of operators.
# Author:
#     Albert Dongz
# History:
#     2020.7.16 First Release
# Dependencies:
#     PyTorch
# Attention:
#     1. Nothing
import torch.nn as nn


class TorchAdd(nn.Module):
    def __init__(self):
        super(TorchAdd, self).__init__()

    def forward(self, x, y):
        return x + y


class TorchMinus(nn.Module):
    def __init__(self):
        super(TorchMinus, self).__init__()

    def forward(self, x, y):
        return x - y


class TorchMatMul(nn.Module):
    def __init__(self):
        super(TorchMatMul, self).__init__()

    def forward(self, x, y):
        return torch.matmul(x, y)


class TorchDotMul(nn.Module):
    def __init__(self):
        super(TorchDotMul, self).__init__()

    def forward(self, x, y):
        return x * y


class TorchDiv(nn.Module):
    def __init__(self):
        super(TorchDiv, self).__init__()

    def forward(self, x, y):
        return x / y


class TorchSin(nn.Module):
    def __init__(self):
        super(TorchSin, self).__init__()

    def forward(self, x):
        return torch.sin(x)


class TorchCos(nn.Module):
    def __init__(self):
        super(TorchCos, self).__init__()

    def forward(self, x):
        return torch.cos(x)


class TorchSoftmax(nn.Module):
    def __init__(self):
        super(TorchSoftmax, self).__init__()

    def forward(self, x):
        return torch.softmax(x)


# global var
TorchFuncTuple = (TorchAdd, TorchMinus, TorchMatMul, TorchDotMul, TorchDiv,
                  TorchSin, TorchCos, TorchSoftmax)