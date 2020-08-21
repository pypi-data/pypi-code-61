import json
from abc import abstractmethod
from typing import Any, AnyStr, BinaryIO, List, Mapping, Optional, Union

from ..metrics.registry import is_single_value

# Predict output can be a str, float, int, or dictionary of class probability
ScoreVector = Union[List[str], List[float], List[int], List[Mapping[str, float]]]


class ExpressConfig:
    log_top_score: bool = True


class BaseModel:
    """
    All Models declared in serve.py should inherit from BaseModel.
    """

    def __init__(self, config: ExpressConfig = ExpressConfig()):
        # self.config contains logging and other settings
        self.config = config

    def pre_process(
        self, http_body: AnyStr, files: Optional[Mapping[str, BinaryIO]] = None
    ) -> List[List[float]]:
        """
        Converts http_body (or files) to something that can be passed into predict()
        """
        samples = json.loads(http_body)
        return [[float(x) for x in s] for s in samples]

    def post_process(
        self, score: ScoreVector, prediction_id: str
    ) -> Union[AnyStr, Mapping[str, Any]]:
        """
        Any postprocessing of output from predict() into response body
        """
        return {"result": score, "prediction_id": prediction_id}

    @abstractmethod
    def predict(self, features: List[List[float]]) -> ScoreVector:
        """
        Generate prediction based on self.model
        """
        raise NotImplementedError

    def validate(self, **kwargs):
        """
        Checks that self.model is initialized.
        Run through all three steps and throws errors if anything is wrong.
        Also does type checking (might move to mypy).
        """
        # Check predict function can be chained
        processed_sample = self.pre_process(**kwargs)
        prediction = self.predict(features=processed_sample)
        processed_prediction = self.post_process(score=prediction, prediction_id="test_id")

        # Check sample features are iterable and flattened for instrumentation
        assert (
            not is_single_value(processed_sample)
            and not any(is_single_value(f) for f in processed_sample)
            and all(all(is_single_value(f) for f in s) for s in processed_sample)
        ), "self.pre_process() should output List[List[float]]"

        # Check predicted scores are iterable
        assert not is_single_value(prediction) and all(is_single_value(p) for p in prediction), (
            "self.predict() should output List[str], List[float], List[int], "
            "or List[Mapping[str, float]]"
        )

        # Check response body is serialisable
        assert is_single_value(
            processed_prediction
        ), "self.post_process() should output str, bytes, or Mapping[str, Any]"

        return processed_prediction
