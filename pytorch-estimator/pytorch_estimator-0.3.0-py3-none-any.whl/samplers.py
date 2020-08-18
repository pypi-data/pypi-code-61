from typing import Optional
from dataclass_serializer import Serializable
from dataclasses import dataclass

from torch.utils.data.sampler import (
    Sampler as TorchSampler,
    RandomSampler as TorchRandomSampler,
)


@dataclass(frozen=True)
class Sampler(Serializable):
    def build(self, estimator, X, y=None) -> TorchSampler:
        raise NotImplementedError


class RandomSampler(Sampler):
    replacement: bool = False
    num_samples: Optional[int] = None

    def build(self, estimator, X, y=None) -> TorchRandomSampler:
        return TorchRandomSampler(
            X, replacement=self.replacement, num_samples=self.num_samples
        )
