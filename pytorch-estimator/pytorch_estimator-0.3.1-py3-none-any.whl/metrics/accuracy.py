from typing import Dict
import torch
from dataclasses import dataclass, field

from .metric import MetricMeter, Average, OutputTransform, MappingTransform


@dataclass(frozen=True)
class Accuracy(Average):
    name = "acc"
    output_transform: OutputTransform = MappingTransform(
        input_names=["logits", "targets"]
    )

    def update(self, state: MetricMeter, outputs: Dict[str, torch.Tensor]):

        preds, targets = self.output_transform.transform(outputs)

        indices = torch.argmax(preds, dim=1)
        correct = torch.eq(indices, targets).view(-1)

        state.total += torch.sum(correct).item()  # type: ignore
        state.count += correct.size(0)  # type: ignore


@dataclass(frozen=True)
class TopKAccuracy(Average):
    k: int = field(metadata={"contract": lambda x: x > 0})
    output_transform: OutputTransform = MappingTransform(
        input_names=["logits", "targets"]
    )

    @property
    def name(self) -> str:
        return f"acc@{self.k}"

    def update(self, state: MetricMeter, outputs: Dict[str, torch.Tensor]):
        preds, targets = self.output_transform.transform(outputs)

        sorted_indices = torch.topk(preds, self.k, dim=1)[1]

        expanded_y = targets.view(-1, 1).expand(-1, self.k)

        correct = torch.sum(torch.eq(sorted_indices, expanded_y), dim=1)

        state.total += torch.sum(correct).item()  # type: ignore
        state.count += correct.size(0)  # type: ignore
