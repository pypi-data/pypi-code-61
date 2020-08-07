# MIT License
#
# Copyright (C) The Adversarial Robustness Toolbox (ART) Authors 2018
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
# Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""
This module implements the classifier `EnsembleClassifier` for ensembles of multiple classifiers.
"""
from __future__ import absolute_import, division, print_function, unicode_literals

import logging
from typing import List, Optional, Union, TYPE_CHECKING

import numpy as np

from art.estimators.classification.classifier import ClassifierNeuralNetwork
from art.estimators.estimator import NeuralNetworkMixin
from art.utils import Deprecated, deprecated_keyword_arg

if TYPE_CHECKING:
    from art.config import CLIP_VALUES_TYPE, PREPROCESSING_TYPE
    from art.data_generators import DataGenerator
    from art.defences.preprocessor import Preprocessor
    from art.defences.postprocessor import Postprocessor

logger = logging.getLogger(__name__)


class EnsembleClassifier(ClassifierNeuralNetwork):
    """
    Class allowing to aggregate multiple classifiers as an ensemble. The individual classifiers are expected to be
    trained when the ensemble is created and no training procedures are provided through this class.
    """

    @deprecated_keyword_arg("channel_index", end_version="1.5.0", replaced_by="channels_first")
    def __init__(
        self,
        classifiers: List[ClassifierNeuralNetwork],
        classifier_weights: Union[list, np.ndarray, None] = None,
        channel_index=Deprecated,
        channels_first: bool = False,
        clip_values: Optional["CLIP_VALUES_TYPE"] = None,
        preprocessing_defences: Union["Preprocessor", List["Preprocessor"], None] = None,
        postprocessing_defences: Union["Postprocessor", List["Postprocessor"], None] = None,
        preprocessing: "PREPROCESSING_TYPE" = (0, 1),
    ) -> None:
        """
        Initialize a :class:`.EnsembleClassifier` object. The data range values and colour channel index have to
        be consistent for all the classifiers in the ensemble.

        :param classifiers: List of :class:`.Classifier` instances to be ensembled together.
        :param classifier_weights: List of weights, one scalar per classifier, to assign to their prediction when
               aggregating results. If `None`, all classifiers are assigned the same weight.
        :param channel_index: Index of the axis in data containing the color channels or features.
        :type channel_index: `int`
        :param channels_first: Set channels first or last.
        :param clip_values: Tuple of the form `(min, max)` of floats or `np.ndarray` representing the minimum and
               maximum values allowed for features. If floats are provided, these will be used as the range of all
               features. If arrays are provided, each value will be considered the bound for a feature, thus
               the shape of clip values needs to match the total number of features.
        :param preprocessing_defences: Preprocessing defence(s) to be applied by the classifier. Not applicable
               in this classifier.
        :param postprocessing_defences: Postprocessing defence(s) to be applied by the classifier.
        :param preprocessing: Tuple of the form `(subtractor, divider)` of floats or `np.ndarray` of values to be
               used for data preprocessing. The first value will be subtracted from the input. The input will then
               be divided by the second one. Not applicable in this classifier.
        """
        if preprocessing_defences is not None:
            raise NotImplementedError("Preprocessing is not applicable in this classifier.")

        # Remove in 1.5.0
        if channel_index == 3:
            channels_first = False
        elif channel_index == 1:
            channels_first = True
        elif channel_index is not Deprecated:
            raise ValueError("Not a proper channel_index. Use channels_first.")

        super(EnsembleClassifier, self).__init__(
            clip_values=clip_values,
            channel_index=channel_index,
            channels_first=channels_first,
            preprocessing_defences=preprocessing_defences,
            postprocessing_defences=postprocessing_defences,
            preprocessing=preprocessing,
        )
        self._nb_classifiers = len(classifiers)

        # Assert all classifiers are the right shape(s)
        for classifier in classifiers:
            if not isinstance(classifier, NeuralNetworkMixin):
                raise TypeError("Expected type `Classifier`, found %s instead." % type(classifier))

            if not np.array_equal(self.clip_values, classifier.clip_values):
                raise ValueError(
                    "Incompatible `clip_values` between classifiers in the ensemble. Found %s and %s."
                    % (str(self.clip_values), str(classifier.clip_values))
                )

            if classifier.nb_classes != classifiers[0].nb_classes:
                raise ValueError(
                    "Incompatible output shapes between classifiers in the ensemble. Found %s and %s."
                    % (str(classifier.nb_classes), str(classifiers[0].nb_classes))
                )

            if classifier.input_shape != classifiers[0].input_shape:
                raise ValueError(
                    "Incompatible input shapes between classifiers in the ensemble. Found %s and %s."
                    % (str(classifier.input_shape), str(classifiers[0].input_shape))
                )

        self._input_shape = classifiers[0].input_shape
        self._nb_classes = classifiers[0].nb_classes

        # Set weights for classifiers
        if classifier_weights is None:
            classifier_weights = np.ones(self._nb_classifiers) / self._nb_classifiers
        self._classifier_weights = classifier_weights

        # check for consistent channels_first in ensemble members
        for i_cls, cls in enumerate(classifiers):
            if cls.channels_first != self.channels_first:
                raise ValueError(
                    "The channels_first boolean of classifier {} is {} while this ensemble expects a "
                    "channels_first boolean of {}. The channels_first booleans of all classifiers and the "
                    "ensemble need ot be identical.".format(i_cls, cls.channels_first, self.channels_first)
                )

        self._classifiers = classifiers
        self._learning_phase: Optional[bool] = None

    def predict(self, x: np.ndarray, batch_size: int = 128, raw: bool = False, **kwargs) -> np.ndarray:
        """
        Perform prediction for a batch of inputs. Predictions from classifiers should only be aggregated if they all
        have the same type of output (e.g., probabilities). Otherwise, use `raw=True` to get predictions from all
        models without aggregation. The same option should be used for logits output, as logits are not comparable
        between models and should not be aggregated.

        :param x: Test set.
        :param batch_size: Size of batches.
        :param raw: Return the individual classifier raw outputs (not aggregated).
        :return: Array of predictions of shape `(nb_inputs, nb_classes)`, or of shape
                 `(nb_classifiers, nb_inputs, nb_classes)` if `raw=True`.
        """
        preds = np.array(
            [self._classifier_weights[i] * self._classifiers[i].predict(x) for i in range(self._nb_classifiers)]
        )
        if raw:
            return preds

        # Aggregate predictions only at probabilities level, as logits are not comparable between models
        var_z = np.sum(preds, axis=0)

        # Apply postprocessing
        predictions = self._apply_postprocessing(preds=var_z, fit=False)

        return predictions

    def fit(self, x: np.ndarray, y: np.ndarray, batch_size: int = 128, nb_epochs: int = 20, **kwargs) -> None:
        """
        Fit the classifier on the training set `(x, y)`. This function is not supported for ensembles.

        :param x: Training data.
        :param y: Target values (class labels) one-hot-encoded of shape (nb_samples, nb_classes).
        :param batch_size: Size of batches.
        :param nb_epochs: Number of epochs to use for training.
        :param kwargs: Dictionary of framework-specific arguments.
        :raises `NotImplementedException`: This method is not supported for ensembles.
        """
        raise NotImplementedError

    def fit_generator(self, generator: "DataGenerator", nb_epochs: int = 20, **kwargs) -> None:
        """
        Fit the classifier using the generator that yields batches as specified. This function is not supported for
        ensembles.

        :param generator: Batch generator providing `(x, y)` for each epoch. If the generator can be used for native
                          training in Keras, it will.
        :param nb_epochs: Number of epochs to use for trainings.
        :param kwargs: Dictionary of framework-specific argument.
        :raises `NotImplementedException`: This method is not supported for ensembles.
        """
        raise NotImplementedError

    @property
    def layer_names(self) -> List[str]:
        """
        Return the hidden layers in the model, if applicable. This function is not supported for ensembles.

        :return: The hidden layers in the model, input and output layers excluded.
        :raises `NotImplementedException`: This method is not supported for ensembles.
        """
        raise NotImplementedError

    def get_activations(
        self, x: np.ndarray, layer: Union[int, str], batch_size: int = 128, framework: bool = False
    ) -> np.ndarray:
        """
        Return the output of the specified layer for input `x`. `layer` is specified by layer index (between 0 and
        `nb_layers - 1`) or by name. The number of layers can be determined by counting the results returned by
        calling `layer_names`. This function is not supported for ensembles.

        :param x: Input for computing the activations.
        :param layer: Layer for computing the activations.
        :param batch_size: Size of batches.
        :param framework: If true, return the intermediate tensor representation of the activation.
        :return: The output of `layer`, where the first dimension is the batch size corresponding to `x`.
        :raises `NotImplementedException`: This method is not supported for ensembles.
        """
        raise NotImplementedError

    def class_gradient(
        self, x: np.ndarray, label: Union[int, List[int], None] = None, raw: bool = False, **kwargs
    ) -> np.ndarray:
        """
        Compute per-class derivatives w.r.t. `x`.

        :param x: Sample input with shape as expected by the model.
        :param label: Index of a specific per-class derivative. If `None`, then gradients for all
                      classes will be computed.
        :param raw: Return the individual classifier raw outputs (not aggregated).
        :return: Array of gradients of input features w.r.t. each class in the form
                 `(batch_size, nb_classes, input_shape)` when computing for all classes, otherwise shape becomes
                 `(batch_size, 1, input_shape)` when `label` parameter is specified. If `raw=True`, an additional
                 dimension is added at the beginning of the array, indexing the different classifiers.
        """
        grads = np.array(
            [
                self._classifier_weights[i] * self._classifiers[i].class_gradient(x, label)
                for i in range(self._nb_classifiers)
            ]
        )
        if raw:
            return grads

        return np.sum(grads, axis=0)

    def loss_gradient(self, x: np.ndarray, y: np.ndarray, raw: bool = False, **kwargs) -> np.ndarray:
        """
        Compute the gradient of the loss function w.r.t. `x`.

        :param x: Sample input with shape as expected by the model.
        :param y: Target values (class labels) one-hot-encoded of shape (nb_samples, nb_classes) or indices of shape
                  (nb_samples,).
        :param raw: Return the individual classifier raw outputs (not aggregated).
        :return: Array of gradients of the same shape as `x`. If `raw=True`, shape becomes `[nb_classifiers, x.shape]`.
        """
        grads = np.array(
            [
                self._classifier_weights[i] * self._classifiers[i].loss_gradient(x, y)
                for i in range(self._nb_classifiers)
            ]
        )
        if raw:
            return grads

        return np.sum(grads, axis=0)

    def set_learning_phase(self, train: bool) -> None:
        """
        Set the learning phase for the backend framework.

        :param train: True to set the learning phase to training, False to set it to prediction.
        """
        if self._learning_phase is not None and isinstance(train, bool):
            for classifier in self._classifiers:
                classifier.set_learning_phase(train)
            self._learning_phase = train

    def __repr__(self):
        repr_ = (
            "%s(classifiers=%r, classifier_weights=%r, channel_index=%r, channels_first=%r, clip_values=%r, "
            "preprocessing_defences=%r, postprocessing_defences=%r, preprocessing=%r)"
            % (
                self.__module__ + "." + self.__class__.__name__,
                self._classifiers,
                self._classifier_weights,
                self.channel_index,
                self.channels_first,
                self.clip_values,
                self.preprocessing_defences,
                self.postprocessing_defences,
                self.preprocessing,
            )
        )

        return repr_

    def save(self, filename: str, path: Optional[str] = None) -> None:
        """
        Save a model to file in the format specific to the backend framework. This function is not supported for
        ensembles.

        :param filename: Name of the file where to store the model.
        :param path: Path of the folder where to store the model. If no path is specified, the model will be stored in
                     the default data location of the library `ART_DATA_PATH`.
        :raises `NotImplementedException`: This method is not supported for ensembles.
        """
        raise NotImplementedError
