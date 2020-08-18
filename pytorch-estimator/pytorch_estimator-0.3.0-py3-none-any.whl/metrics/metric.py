from typing import List, Dict, Any, Callable
from abc import abstractmethod
import warnings

import abc
from dataclass_serializer import Serializable
from dataclasses import dataclass


import torch


class OutputTransform(Serializable):
    def transform(self, outputs: Dict[str, torch.Tensor]) -> List[torch.Tensor]:
        pass


@dataclass(frozen=True)
class MappingTransform(OutputTransform):
    input_names: List[str]

    def transform(self, outputs: Dict[str, torch.Tensor]) -> List[torch.Tensor]:
        return [outputs[name] for name in self.input_names]


@dataclass(frozen=True)
class Metric(Serializable):
    """Class to calculate metrics with running statistics.
    """

    def to_meter(self) -> "MetricMeter":
        return MetricMeter(self)

    @abstractmethod
    def update(self, state: "MetricMeter", output: Dict[str, torch.Tensor]):
        pass

    @abstractmethod
    def reset(self, state: "MetricMeter"):
        pass

    @abstractmethod
    def compute(self, state: "MetricMeter"):
        pass


@dataclass(frozen=True)
class Average(Metric):
    def reset(self, state: "MetricMeter"):
        state.count = 0.0  # type: ignore
        state.total = 0.0  # type: ignore

    def compute(self, state: "MetricMeter"):
        return state.total / state.count  # type: ignore


@dataclass(frozen=True)
class EpochMetirc(Metric):
    """For metrics requires all historical samples.
    """

    output_transform: OutputTransform

    @abc.abstractmethod
    def compute_fn(self, logits, targets) -> float:
        raise NotImplementedError

    def update(self, state: "MetricMeter", output: Dict[str, torch.Tensor]):
        logits, targets = self.output_transform.transform(output)
        logits = logits.detach().type_as(state._predictions)  # type: ignore
        targets = targets.detach().type_as(state._targets)  # type: ignore

        state._predictions = torch.cat(  # type: ignore
            [state._predictions, logits], dim=0  # type: ignore
        )
        state._targets = torch.cat(  # type: ignore
            [state._targets, targets], dim=0  # type: ignore
        )

        # Check once the signature and execution of compute_fn
        if state._predictions.shape == logits.shape:  # type: ignore
            try:
                self.compute_fn(
                    state._predictions,  # type: ignore
                    state._targets,  # type: ignore
                )
            except Exception as e:
                warnings.warn(
                    "Probably, there can be a problem with `compute_fn`:\n {}".format(
                        e
                    ),
                    RuntimeWarning,
                )

    def reset(self, state: "MetricMeter"):
        state._predictions = torch.tensor(  # type: ignore
            [], dtype=torch.float32
        )
        state._targets = torch.tensor([], dtype=torch.float32)  # type: ignore

    def compute(self, state: "MetricMeter"):
        return self.compute_fn(state._predictions, state._targets)  # type: ignore


class MetricMeter:
    """ Computes and stores the reduced and current value """

    def __init__(self, metric):
        self.metric = metric
        self.reset()

    @property
    def name(self):
        return self.metric.name

    def reset(self) -> None:
        """ Reset all statistics """
        self.metric.reset(self)

    def update(self, outputs: Dict[str, torch.Tensor]):
        """ Update statistics """
        self.metric.update(self, outputs)

    def compute(self):
        return self.metric.compute(self)


class Metrics:
    """Holds multiple metrics, and execute it as MetricsMeter.
    """

    def __init__(self, meters: List[Metric]):
        self._m = [m.to_meter() for m in meters]

    def reset(self):
        [m.reset() for m in self._m]

    def update(self, outputs: Dict[str, torch.Tensor]):
        """ Update statistics """
        for meter in self._m:
            meter.update(outputs)

    def sync_to(self, log: Dict[str, Any], prefix=""):
        for meter in self._m:
            log[prefix + meter.name] = meter.compute()


@dataclass(frozen=True)
class Record(Average):
    """Record output value of train / validation step
    """

    name: str

    def update(self, state: MetricMeter, outputs: Dict[str, torch.Tensor]):
        state.total += outputs[self.name].item()  # type: ignore
        state.count += 1  # type: ignore
