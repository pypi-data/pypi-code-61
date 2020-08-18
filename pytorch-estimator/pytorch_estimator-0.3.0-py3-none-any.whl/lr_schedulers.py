from abc import abstractmethod
from typing import List
import torch.optim as optim

from dataclass_serializer import Serializable
from dataclasses import dataclass, field


class LRScheduler(Serializable):
    @abstractmethod
    def __call__(self, params):
        raise NotImplementedError


@dataclass(frozen=True)
class MultiStepLR(LRScheduler):
    milestones: List[int]
    gamma: float
    schedule_on: str = field(
        default="epoch_end",
        metadata={"contract": lambda x: x in ("batch_end", "epoch_end")},
    )

    def __call__(self, params) -> optim.lr_scheduler.MultiStepLR:
        o = optim.lr_scheduler.MultiStepLR(
            params, milestones=self.milestones, gamma=self.gamma
        )
        o.schedule_on = self.schedule_on  # type: ignore
        return o
