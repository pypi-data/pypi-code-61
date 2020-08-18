from typing import Tuple
from dataclasses import dataclass
from abc import abstractmethod
import torch.optim as optim

from dataclass_serializer import Serializable


class Optimizer(Serializable):
    @abstractmethod
    def __call__(self, params):
        raise NotImplementedError


@dataclass(frozen=True)
class SGD(Optimizer):
    lr: float
    momentum: float = 0.0
    dampening: float = 0.0
    weight_decay: float = 0.0
    nesterov: bool = False

    def __call__(self, params) -> optim.SGD:
        return optim.SGD(
            params,
            lr=self.lr,
            momentum=self.momentum,
            dampening=self.dampening,
            nesterov=self.nesterov,
            weight_decay=self.weight_decay,
        )


@dataclass(frozen=True)
class Adam(Optimizer):
    lr: float = 1e-3
    betas: Tuple[float, float] = (0.9, 0.999)
    eps: float = 1e-8
    weight_decay: float = 0.0
    amsgrad: bool = False

    def __call__(self, params) -> optim.Adam:
        return optim.Adam(
            params,
            lr=self.lr,
            betas=self.betas,
            eps=self.eps,
            amsgrad=self.amsgrad,
            weight_decay=self.weight_decay,
        )
