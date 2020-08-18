from typing import List, Optional
from abc import abstractmethod


import torch.nn as nn

from dataclass_serializer import Serializable
from dataclasses import dataclass


class Loss(Serializable):
    @abstractmethod
    def __call__(self) -> nn.Module:
        raise NotImplementedError


@dataclass(frozen=True)
class BinaryCrossEntropy(Loss):
    reduction: str = "mean"
    weight: Optional[List[int]] = None

    def __call__(self) -> nn.Module:
        return nn.BCELoss(weight=self.weight, reduction=self.reduction)


@dataclass(frozen=True)
class BinaryCrossEntropyWithLogits(Loss):
    reduction: str = "mean"
    weight: Optional[List[int]] = None

    def __call__(self) -> nn.Module:
        return nn.BCEWithLogitsLoss(weight=self.weight, reduction=self.reduction)


@dataclass(frozen=True)
class SoftmaxCrossEntropy(Loss):
    reduction: str = "mean"
    weight: Optional[List[int]] = None

    def __call__(self) -> nn.Module:
        return nn.CrossEntropyLoss(weight=self.weight, reduction=self.reduction)


@dataclass(frozen=True)
class MSELoss(Loss):
    reduction: str = "mean"

    def __call__(self) -> nn.Module:
        return nn.MSELoss(reduction=self.reduction)


@dataclass(frozen=True)
class L1Loss(Loss):
    reduction: str = "mean"

    def __call__(self) -> nn.Module:
        return nn.L1Loss(reduction=self.reduction)


@dataclass(frozen=True)
class Noop(Loss):
    def __call__(self) -> nn.Module:
        return nn.Identity()
