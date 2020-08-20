import json
from abc import abstractmethod
from typing import Any, AnyStr, BinaryIO, List, Mapping, Optional, Union

from ..metrics.registry import is_single_value


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
    ) -> List[float]:
        """
        Converts http_body (or files) to something that can be passed into predict()
        """
        array = json.loads(http_body)
        return [float(x) for x in array]

    def post_process(
        self, score: Union[float, List[float]], prediction_id: str
    ) -> Union[AnyStr, Mapping[str, Any]]:
        """
        Any postprocessing of output from predict() into response body
        """
        return {"result": score, "prediction_id": prediction_id}

    @abstractmethod
    def predict(self, features: List[float]) -> Union[float, List[float]]:
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
        processed_sample = self.pre_process(**kwargs)
        prediction = self.predict(features=processed_sample)
        processed_prediction = self.post_process(score=prediction, prediction_id="test_id")
        # Check processed_sample is iterable since we enumerate on it in metric registry
        assert not is_single_value(
            processed_sample
        ), "self.pre_process() should output List[float] or List[List[float]]"
        assert is_single_value(
            processed_prediction
        ), "self.post_process() should output str or Mapping[str, float]"
        # Must assume feature vector is flattened for metrics to work
        if all(is_single_value(f) for f in processed_sample):
            # If features is List[float], then prediction is float (for regression),
            # or Mapping[str, float] (for individual class probability)
            assert is_single_value(
                prediction
            ), "self.predict() should output float or Mapping[str, float]"
        elif all(all(is_single_value(f) for f in s) for s in processed_sample):
            # If features is List[List[float]], then prediction is List[float]
            assert all(
                is_single_value(p) for p in prediction
            ), "self.predict() should output List[float]"
        else:
            raise ValueError("sample features contain mismatched element type")
        return processed_prediction
