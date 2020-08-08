"""Tests coreml.data.sampler.DataSampler"""
# pylint: disable=no-member,invalid-name
import unittest
from torch.utils.data import Dataset
from numpy.testing import assert_array_equal
from coreml.data.vision.image import Image
from coreml.data.transforms import ClassificationAnnotationTransform
from coreml.data.sampler import DataSampler, ClassificationDataSampler


class DummyDataset(Dataset):
    """Defines a dummy dataset for testing"""
    def __init__(self):
        self.len = 10

    def __getitem__(self, index):
        return index

    def __len__(self):
        return self.len


class DummyClassificationDataset(Dataset):
    """Defines a dummy classification dataset for testing"""
    def __init__(self, mode='binary-1'):
        if mode == 'binary-1':
            # first element is label 'b'
            self.labels = [['b'], ['a'], ['a'], ['b'], ['b']]
        elif mode == 'binary-2':
            # first element is label 'a'
            self.labels = [['a'], ['a'], ['a'], ['b'], ['b']]
        else:
            # multi-class
            self.labels = [['c'], ['a'], ['b'], ['a'], ['c']]

        self.items = [Image(
            '', {'classification': label}) for label in self.labels]

    def __getitem__(self, index):
        return index

    def __len__(self):
        return len(self.items)


class DataSamplerTestCase(unittest.TestCase):
    """Class to run tests on DataSampler"""
    @classmethod
    def setUpClass(cls):
        cls.dataset = DummyDataset()

    def test_no_shuffle(self):
        """Test sampling without shuffling"""
        sampler = DataSampler(
            self.dataset, shuffle=False)
        indices = list(sampler)
        true_indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        # without shuffle=True, the ordering should be the default ordering
        self.assertEqual(indices, true_indices)

    def test_with_shuffle(self):
        """Test sampling with shuffling"""
        sampler = DataSampler(
            self.dataset, shuffle=True)
        indices = list(sampler)
        true_indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        # with shuffle=True, the ordering should be different from the
        # default ordering
        self.assertNotEqual(indices, true_indices)


class ClassificationDataSamplerTestCase(unittest.TestCase):
    """Class to run tests on ClassificationDataSampler"""
    @classmethod
    def setUpClass(cls):
        cls.binary_1_dataset = DummyClassificationDataset('binary-1')
        cls.binary_2_dataset = DummyClassificationDataset('binary-2')
        cls.binary_target_transform = ClassificationAnnotationTransform(
            ['b', 'a'])
        cls.multi_dataset = DummyClassificationDataset('multi')
        cls.multi_target_transform = ClassificationAnnotationTransform(
            ['b', 'a', 'c'])

    def test_default_no_shuffle(self):
        """Test sampling without shuffling on mode='default'"""
        sampler = ClassificationDataSampler(
            self.binary_1_dataset, shuffle=False,
            target_transform=self.binary_target_transform, mode='default')
        indices = list(sampler)
        true_indices = [0, 1, 2, 3, 4]

        # without shuffle=True, the ordering should be the default ordering
        self.assertEqual(indices, true_indices)

    def test_default_with_shuffle(self):
        """Test sampling with shuffling on mode='default'"""
        sampler = ClassificationDataSampler(
            self.binary_1_dataset, shuffle=True,
            target_transform=self.binary_target_transform,
            mode='default')
        indices = list(sampler)
        true_indices = [0, 1, 2, 3, 4]

        # with shuffle=True, the ordering should be different from the
        # default ordering
        self.assertNotEqual(indices, true_indices)

    def test_multi_balanced_no_shuffle(self):
        """Test sampling on mode='balanced' for multiclass no shuffle"""
        sampler = ClassificationDataSampler(
            self.multi_dataset, shuffle=False,
            target_transform=self.multi_target_transform,
            mode='balanced')
        indices = list(sampler)
        true_indices = [2, 1, 0]

        # with shuffle=False, the first occurence of each
        # class should be returned
        self.assertEqual(indices, true_indices)

    def test_multi_balanced_with_shuffle(self):
        """Test sampling on mode='balanced' for multiclass with shuffle"""
        sampler = ClassificationDataSampler(
            self.multi_dataset, shuffle=True,
            target_transform=self.multi_target_transform,
            mode='balanced')
        indices = list(sampler)
        for i, index in enumerate(indices):
            if not i % 3:
                target_label = 0
            elif i % 3 == 1:
                target_label = 1
            else:
                target_label = 2

            self.assertEqual(sampler.labels[index], target_label)

    def test_binary_balanced_no_shuffle(self):
        """Test sampling without shuffling on mode='balanced' for binary"""
        sampler = ClassificationDataSampler(
            self.binary_1_dataset, shuffle=False,
            target_transform=self.binary_target_transform,
            mode='balanced')
        indices = list(sampler)
        assert_array_equal(indices, [0, 1, 3, 2])

    def test_binary_1_balanced_shuffle(self):
        """Test sampling with shuffling on mode='balanced' for binary-1"""
        sampler = ClassificationDataSampler(
            self.binary_1_dataset, shuffle=True,
            target_transform=self.binary_target_transform,
            mode='balanced')
        indices = list(sampler)
        for i, index in enumerate(indices):
            if not i % 2:
                target_label = 0
            else:
                target_label = 1

            self.assertEqual(sampler.labels[index], target_label)

    def test_binary_balanced_length(self):
        """Test sampler length with mode='balanced' for binary-1"""
        sampler = ClassificationDataSampler(
            self.binary_1_dataset, shuffle=True,
            target_transform=self.binary_target_transform,
            mode='balanced')
        self.assertEqual(len(sampler), 4)

    def test_binary_2_balanced_shuffle(self):
        """Test sampling with shuffling on mode='balanced' for binary-2"""
        sampler = ClassificationDataSampler(
            self.binary_2_dataset, shuffle=True,
            target_transform=self.binary_target_transform,
            mode='balanced')
        indices = list(sampler)

        for i, index in enumerate(indices):
            if not i % 2:
                target_label = 0
            else:
                target_label = 1

            self.assertEqual(sampler.labels[index], target_label)


if __name__ == "__main__":
    unittest.main()
