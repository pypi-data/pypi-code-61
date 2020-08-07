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
from __future__ import absolute_import, division, print_function, unicode_literals

import pytest
import logging
import numpy as np

from art.defences.preprocessor.inverse_gan import InverseGAN
from art.attacks.evasion import FastGradientMethod

from tests.utils import get_gan_inverse_gan_ft


@pytest.fixture()
def fix_get_mnist_subset(get_mnist_dataset):
    (x_train_mnist, y_train_mnist), (x_test_mnist, y_test_mnist) = get_mnist_dataset
    n_train = 50
    n_test = 50
    yield (x_train_mnist[:n_train], y_train_mnist[:n_train], x_test_mnist[:n_test], y_test_mnist[:n_test])


@pytest.mark.only_with_platform("tensorflow")
def test_inverse_gan(fix_get_mnist_subset, get_image_classifier_list_for_attack):
    (x_train_mnist, y_train_mnist, x_test_mnist, y_test_mnist) = fix_get_mnist_subset

    gan, inverse_gan, sess = get_gan_inverse_gan_ft()
    if gan is None:
        logging.warning("Couldn't perform  this test because no gan is defined for this framework configuration")
        return

    classifier_list = get_image_classifier_list_for_attack(FastGradientMethod)

    if classifier_list is None:
        logging.warning("Couldn't perform  this test because no classifier is defined")
        return

    classifier = classifier_list[0]

    attack = FastGradientMethod(classifier, eps=0.2)
    x_test_adv = attack.generate(x=x_test_mnist)

    inverse_gan = InverseGAN(sess=sess, gan=gan, inverse_gan=inverse_gan)

    x_test_defended = inverse_gan(x_test_adv, maxiter=1)

    np.testing.assert_array_almost_equal(
        float(np.mean(x_test_defended - x_test_adv)), 0.08818667382001877, decimal=0.01,
    )


if __name__ == "__main__":
    pytest.cmdline.main("-q -s {} --mlFramework=tensorflow --durations=0".format(__file__).split(" "))
