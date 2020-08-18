from typing import Dict
import torch

from .metric import MetricMeter, Average, OutputTransform, MappingTransform

from dataclasses import dataclass


@dataclass(frozen=True)
class Loss(Average):
    """Record loss which is already calculated.
    """

    name = "loss"
    output_transform: OutputTransform = MappingTransform(input_names=["loss"])

    def update(self, state: MetricMeter, outputs: Dict[str, torch.Tensor]):
        (loss,) = self.output_transform.transform(outputs)

        state.total += loss.item()  # type: ignore
        state.count += 1  # type: ignore
