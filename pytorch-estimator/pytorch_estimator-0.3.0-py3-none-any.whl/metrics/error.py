from typing import Dict
from dataclasses import dataclass

import math
import torch

from .metric import MetricMeter, Average, OutputTransform, MappingTransform

EPSILON = 1e-10


@dataclass(frozen=True)
class SMAPE(Average):

    name = "smape"
    output_transform: OutputTransform = MappingTransform(  # type: ignore
        input_names=["logits", "targets"]
    )

    def update(self, state: MetricMeter, outputs: Dict[str, torch.Tensor]):
        (logits, targets) = self.output_transform.transform(outputs)

        smape = torch.sum(
            2.0
            * torch.abs(targets - logits)
            / ((torch.abs(targets) + torch.abs(logits)) + EPSILON)
        )

        state.total += smape.item()  # type: ignore
        state.count += logits.shape[0]  # type: ignore


@dataclass(frozen=True)
class MSE(Average):

    name = "mse"
    output_transform: OutputTransform = MappingTransform(  # type: ignore
        input_names=["logits", "targets"]
    )

    def update(self, state: MetricMeter, outputs: Dict[str, torch.Tensor]):
        (logits, targets) = self.output_transform.transform(outputs)

        mse = torch.sum((targets - logits) ** 2)

        state.total += mse.item()  # type: ignore
        state.count += logits.shape[0]  # type: ignore


@dataclass(frozen=True)
class RMSE(MSE):

    name = "rmse"
    output_transform: OutputTransform = MappingTransform(  # type: ignore
        input_names=["logits", "targets"]
    )

    def compute(self, state: MetricMeter):
        return math.sqrt(super().compute(state))  # type: ignore


@dataclass(frozen=True)
class MAE(MSE):

    name = "mae"
    output_transform: OutputTransform = MappingTransform(  # type: ignore
        input_names=["logits", "targets"]
    )

    def update(self, state: MetricMeter, outputs: Dict[str, torch.Tensor]):
        (logits, targets) = self.output_transform.transform(outputs)

        mae = torch.sum(torch.abs(targets - logits))

        state.total += mae.item()  # type: ignore
        state.count += logits.shape[0]  # type: ignore
