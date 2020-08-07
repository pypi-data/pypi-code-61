# MIT License
#
# Copyright (C) The Adversarial Robustness Toolbox (ART) Authors 2020
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
This module implements the adversarial patch attack `AdversarialPatch`. This attack generates an adversarial patch that
can be printed into the physical world with a common printer. The patch can be used to fool image classifiers.

| Paper link: https://arxiv.org/abs/1712.09665
"""
from __future__ import absolute_import, division, print_function, unicode_literals

import logging
from typing import Optional, Tuple, Union

import numpy as np

from art.attacks.evasion.adversarial_patch.adversarial_patch_numpy import AdversarialPatchNumpy
from art.attacks.evasion.adversarial_patch.adversarial_patch_tensorflow import AdversarialPatchTensorFlowV2
from art.estimators.estimator import BaseEstimator, NeuralNetworkMixin
from art.estimators.classification.classifier import (
    ClassifierMixin,
    ClassifierNeuralNetwork,
    ClassifierGradients,
)
from art.estimators.classification import TensorFlowV2Classifier
from art.attacks.attack import EvasionAttack

logger = logging.getLogger(__name__)


class AdversarialPatch(EvasionAttack):
    """
    Implementation of the adversarial patch attack.

    | Paper link: https://arxiv.org/abs/1712.09665
    """

    attack_params = EvasionAttack.attack_params + [
        "rotation_max",
        "scale_min",
        "scale_max",
        "learning_rate",
        "max_iter",
        "batch_size",
    ]

    _estimator_requirements = (BaseEstimator, NeuralNetworkMixin, ClassifierMixin)

    def __init__(
        self,
        classifier: Union[ClassifierNeuralNetwork, ClassifierGradients],
        rotation_max: float = 22.5,
        scale_min: float = 0.1,
        scale_max: float = 1.0,
        learning_rate: float = 5.0,
        max_iter: int = 500,
        batch_size: int = 16,
        patch_shape: Optional[Tuple[int, int, int]] = None,
    ):
        """
        Create an instance of the :class:`.AdversarialPatch`.

        :param classifier: A trained classifier.
        :param rotation_max: The maximum rotation applied to random patches. The value is expected to be in the
               range `[0, 180]`.
        :param scale_min: The minimum scaling applied to random patches. The value should be in the range `[0, 1]`,
               but less than `scale_max`.
        :param scale_max: The maximum scaling applied to random patches. The value should be in the range `[0, 1]`, but
               larger than `scale_min.`
        :param learning_rate: The learning rate of the optimization.
        :param max_iter: The number of optimization steps.
        :param batch_size: The size of the training batch.
        :param patch_shape: The shape of the adversarial patch as a tuple of shape (width, height, nb_channels).
                            Currently only supported for `TensorFlowV2Classifier`. For classifiers of other frameworks
                            the `patch_shape` is set to the shape of the image samples.
        """
        super(AdversarialPatch, self).__init__(estimator=classifier)
        if self.estimator.clip_values is None:
            raise ValueError("Adversarial Patch attack requires a classifier with clip_values.")

        self._attack: Union[AdversarialPatchTensorFlowV2, AdversarialPatchNumpy]
        if isinstance(self.estimator, TensorFlowV2Classifier):
            self._attack = AdversarialPatchTensorFlowV2(
                classifier=classifier,
                rotation_max=rotation_max,
                scale_min=scale_min,
                scale_max=scale_max,
                learning_rate=learning_rate,
                max_iter=max_iter,
                batch_size=batch_size,
                patch_shape=patch_shape,
            )
        else:
            self._attack = AdversarialPatchNumpy(
                classifier=classifier,
                rotation_max=rotation_max,
                scale_min=scale_min,
                scale_max=scale_max,
                learning_rate=learning_rate,
                max_iter=max_iter,
                batch_size=batch_size,
            )
        self._check_params()

    def generate(self, x: np.ndarray, y: Optional[np.ndarray] = None, **kwargs) -> np.ndarray:
        """
        Generate adversarial samples and return them in an array.

        :param x: An array with the original inputs. `x` is expected to have spatial dimensions.
        :param y: An array with the original labels to be predicted.
        :return: An array holding the adversarial patch.
        """
        logger.info("Creating adversarial patch.")

        if y is None:
            raise ValueError("Adversarial Patch attack requires target values `y`.")

        if len(x.shape) == 2:
            raise ValueError(
                "Feature vectors detected. The adversarial patch can only be applied to data with spatial "
                "dimensions."
            )

        return self._attack.generate(x=x, y=y, **kwargs)

    def apply_patch(self, x: np.ndarray, scale: float, patch_external: Optional[np.ndarray] = None) -> np.ndarray:
        """
        A function to apply the learned adversarial patch to images.

        :param x: Instances to apply randomly transformed patch.
        :param scale: Scale of the applied patch in relation to the classifier input shape.
        :param patch_external: External patch to apply to images `x`.
        :return: The patched instances.
        """
        return self._attack.apply_patch(x, scale, patch_external=patch_external)

    def set_params(self, **kwargs) -> None:
        self._attack.set_params(**kwargs)

    def _check_params(self) -> None:
        if not isinstance(self._attack.rotation_max, (float, int)):
            raise ValueError("The maximum rotation of the random patches must be of type float.")
        if self._attack.rotation_max < 0 or self._attack.rotation_max > 180.0:
            raise ValueError("The maximum rotation of the random patches must be between 0 and 180 degrees.")

        if not isinstance(self._attack.scale_min, float):
            raise ValueError("The minimum scale of the random patched must be of type float.")
        if self._attack.scale_min < 0 or self._attack.scale_min >= self._attack.scale_max:
            raise ValueError(
                "The minimum scale of the random patched must be greater than 0 and less than the maximum scaling."
            )

        if not isinstance(self._attack.scale_max, float):
            raise ValueError("The maximum scale of the random patched must be of type float.")
        if self._attack.scale_max > 1:
            raise ValueError("The maximum scale of the random patched must not be greater than 1.")

        if not isinstance(self._attack.learning_rate, float):
            raise ValueError("The learning rate must be of type float.")
        if not self._attack.learning_rate > 0.0:
            raise ValueError("The learning rate must be greater than 0.0.")

        if not isinstance(self._attack.max_iter, int):
            raise ValueError("The number of optimization steps must be of type int.")
        if not self._attack.max_iter > 0:
            raise ValueError("The number of optimization steps must be greater than 0.")

        if not isinstance(self._attack.batch_size, int):
            raise ValueError("The batch size must be of type int.")
        if not self._attack.batch_size > 0:
            raise ValueError("The batch size must be greater than 0.")
