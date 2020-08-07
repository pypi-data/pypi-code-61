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
This module implements the adversarial patch attack `DPatch` for object detectors.

| Paper link: https://arxiv.org/abs/1806.02299v4
"""
import logging
import math
import random
from typing import Dict, List, Optional, Tuple

import numpy as np
from tqdm import trange

from art.attacks.attack import EvasionAttack
from art.estimators.estimator import BaseEstimator, LossGradientsMixin
from art.estimators.object_detection.object_detector import ObjectDetectorMixin
from art.utils import Deprecated, deprecated_keyword_arg

logger = logging.getLogger(__name__)


class DPatch(EvasionAttack):
    """
    Implementation of the DPatch attack.

    | Paper link: https://arxiv.org/abs/1806.02299v4
    """

    attack_params = EvasionAttack.attack_params + [
        "patch_shape",
        "learning_rate",
        "max_iter",
        "batch_size",
    ]

    _estimator_requirements = (BaseEstimator, LossGradientsMixin, ObjectDetectorMixin)

    def __init__(
        self,
        estimator: ObjectDetectorMixin,
        patch_shape: Tuple[int, int, int] = (40, 40, 3),
        learning_rate: float = 5.0,
        max_iter: int = 500,
        batch_size: int = 16,
    ):
        """
        Create an instance of the :class:`.DPatch`.

        :param estimator: A trained object detector.
        :param patch_shape: The shape of the adversarial path as a tuple of shape (height, width, nb_channels).
        :param learning_rate: The learning rate of the optimization.
        :param max_iter: The number of optimization steps.
        :param batch_size: The size of the training batch.
        """
        super(DPatch, self).__init__(estimator=estimator)

        self.patch_shape = patch_shape
        self.learning_rate = learning_rate
        self.max_iter = max_iter
        self.batch_size = batch_size
        self._patch = np.ones(shape=patch_shape) * (self.estimator.clip_values[1] + self.estimator.clip_values[0]) / 2.0
        self._check_params()

    def generate(self, x: np.ndarray, y: Optional[np.ndarray] = None, **kwargs) -> np.ndarray:
        """
        Generate DPatch.

        :param x: Sample images.
        :param y: Target labels for object detector.
        :return: Adversarial patch.
        """
        channel_index = 1 if self.estimator.channels_first else x.ndim - 1
        if x.shape[channel_index] != self.patch_shape[channel_index - 1]:
            raise ValueError("The color channel index of the images and the patch have to be identical.")
        if y is not None:
            raise ValueError("The DPatch attack does not use target labels.")
        if x.ndim != 4:
            raise ValueError("The adversarial patch can only be applied to images.")

        for i_step in trange(self.max_iter, desc="DPatch iteration"):
            if i_step == 0 or (i_step + 1) % 100 == 0:
                logger.info("Training Step: %i", i_step + 1)

            patched_images, transforms = self._augment_images_with_patch(
                x, self._patch, random_location=True, channels_first=self.estimator.channels_first
            )
            patch_target: List[Dict[str, np.ndarray]] = list()

            for i_image in range(patched_images.shape[0]):

                i_x_1 = transforms[i_image]["i_x_1"]
                i_x_2 = transforms[i_image]["i_x_2"]
                i_y_1 = transforms[i_image]["i_y_1"]
                i_y_2 = transforms[i_image]["i_y_2"]

                target_dict = dict()
                target_dict["boxes"] = np.asarray([[i_x_1, i_y_1, i_x_2, i_y_2]])
                target_dict["labels"] = np.asarray([1,])
                target_dict["scores"] = np.asarray([1.0,])

                patch_target.append(target_dict)

            num_batches = math.ceil(x.shape[0] / self.batch_size)
            patch_gradients = np.zeros_like(self._patch)

            for i_batch in range(num_batches):
                i_batch_start = i_batch * self.batch_size
                i_batch_end = min((i_batch + 1) * self.batch_size, patched_images.shape[0])

                gradients = self.estimator.loss_gradient(
                    x=patched_images[i_batch_start:i_batch_end], y=patch_target[i_batch_start:i_batch_end],
                )

                for i_image in range(self.batch_size):

                    i_x_1 = transforms[i_batch_start + i_image]["i_x_1"]
                    i_x_2 = transforms[i_batch_start + i_image]["i_x_2"]
                    i_y_1 = transforms[i_batch_start + i_image]["i_y_1"]
                    i_y_2 = transforms[i_batch_start + i_image]["i_y_2"]

                    if self.estimator.channels_first:
                        patch_gradients_i = gradients[i_image, :, i_x_1:i_x_2, i_y_1:i_y_2]
                    else:
                        patch_gradients_i = gradients[i_image, i_x_1:i_x_2, i_y_1:i_y_2, :]

                    patch_gradients += patch_gradients_i

            self._patch -= patch_gradients * self.learning_rate
            self._patch = np.clip(
                self._patch, a_min=self.estimator.clip_values[0], a_max=self.estimator.clip_values[1],
            )

        return self._patch

    @staticmethod
    @deprecated_keyword_arg("channel_index", end_version="1.5.0", replaced_by="channels_first")
    def _augment_images_with_patch(
        x: np.ndarray, patch: np.ndarray, random_location: bool, channels_first: bool, channel_index=Deprecated
    ) -> Tuple[np.ndarray, List[Dict[str, int]]]:
        """
        Augment images with patch.

        :param x: Sample images.
        :param patch: The patch to be applied.
        :param random_location: If True apply patch at randomly shifted locations, otherwise place patch at origin
                                (top-left corner).
        :param channels_first: Set channels first or last.
        :param channel_index: Index of the color channel.
        :type channel_index: `int`
        """
        # Remove in 1.5.0
        if channel_index == 3:
            channels_first = False
        elif channel_index == 1:
            channels_first = True
        elif channel_index is not Deprecated:
            raise ValueError("Not a proper channel_index. Use channels_first.")

        transformations = list()
        x_copy = x.copy()
        patch_copy = patch.copy()

        if channels_first:
            x_copy = np.transpose(x_copy, (0, 2, 3, 1))
            patch_copy = np.transpose(patch_copy, (1, 2, 0))

        for i_image in range(x.shape[0]):

            if random_location:
                i_x_1 = random.randint(0, x_copy.shape[1] - 1 - patch_copy.shape[0])
                i_y_1 = random.randint(0, x_copy.shape[2] - 1 - patch_copy.shape[1])
            else:
                i_x_1 = 0
                i_y_1 = 0

            i_x_2 = i_x_1 + patch_copy.shape[0]
            i_y_2 = i_y_1 + patch_copy.shape[1]

            transformations.append({"i_x_1": i_x_1, "i_y_1": i_y_1, "i_x_2": i_x_2, "i_y_2": i_y_2})

            x_copy[i_image, i_x_1:i_x_2, i_y_1:i_y_2, :] = patch_copy

        if channels_first:
            x_copy = np.transpose(x_copy, (0, 3, 1, 2))

        return x_copy, transformations

    def apply_patch(
        self, x: np.ndarray, patch_external: Optional[np.ndarray] = None, random_location: bool = False,
    ) -> np.ndarray:
        """
        Apply the adversarial patch to images.

        :param x: Images to be patched.
        :param patch_external: External patch to apply to images `x`. If None the attacks patch will be applied.
        :param random_location: True if patch location should be random.
        :return: The patched images.
        """
        if patch_external is not None:
            patch_local = patch_external
        else:
            patch_local = self._patch

        patched_images, _ = self._augment_images_with_patch(
            x=x, patch=patch_local, random_location=random_location, channels_first=self.estimator.channels_first
        )

        return patched_images

    def _check_params(self) -> None:
        if not isinstance(self.patch_shape, tuple):
            raise ValueError("The patch shape must be a tuple of integers.")
        if len(self.patch_shape) != 3:
            raise ValueError("The length of patch shape must be 3.")

        if not isinstance(self.learning_rate, float):
            raise ValueError("The learning rate must be of type float.")
        if not self.learning_rate > 0.0:
            raise ValueError("The learning rate must be greater than 0.0.")

        if not isinstance(self.max_iter, int):
            raise ValueError("The number of optimization steps must be of type int.")
        if not self.max_iter > 0:
            raise ValueError("The number of optimization steps must be greater than 0.")

        if not isinstance(self.batch_size, int):
            raise ValueError("The batch size must be of type int.")
        if not self.batch_size > 0:
            raise ValueError("The batch size must be greater than 0.")
