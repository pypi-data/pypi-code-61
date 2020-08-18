"""Test the example package."""

import unittest

from example import is_language


class ExampleTest(unittest.TestCase):
    """Test the example function."""

    def test_returns_true_when_language_match(self) -> None:
        """Test that the function returns True when given text belongs to language selected."""
        self.assertTrue(is_language("I'm the one who knocks!", language="en"))

    def test_returns_false_when_language_does_not_match(self) -> None:
        """Test that the function returns False when given text does not belongs to language selected."""
        self.assertFalse(is_language("I'm the one who knocks!", language="pt"))
