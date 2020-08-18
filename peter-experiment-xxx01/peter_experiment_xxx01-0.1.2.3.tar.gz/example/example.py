#!/usr/bin/env python

"""This is an example program written in python to show github Actions.

When a pull request is made the workflow defined in .github/workflows/main.yml will be executed, which will check this
file for code style (flake8), typing (mypy) and run the tests in tests/. If any step fails the build is considered
failed and the pull requests cannot be merged.
"""
from typing import Literal

import langdetect

# Just to illustrate some more advanced use of typing
LANGUAGES = Literal['nl', 'hr', 'en', 'fa', 'de', 'bn', 'ml', 'ta', 'lt', 'it', 'ca', 'he', 'no', 'pl', 'tl', 'da',
                    'th', 'ru', 'zh-tw', 'fr', 'ro', 'tr', 'te', 'ar', 'ne', 'es', 'id', 'cs', 'ko', 'sq', 'ja', 'lv',
                    'so', 'hu', 'pt', 'bg', 'uk', 'el', 'fi', 'zh-cn', 'mr', 'ur', 'pa', 'mk', 'vi', 'sw', 'sk', 'sl',
                    'af', 'cy', 'sv', 'gu', 'kn', 'hi', 'et']


def is_language(text: str, language: LANGUAGES = "en") -> bool:
    """Return the language detected in the text.

    For the list of available languages check https://pypi.org/project/langdetect/.

    :param text: the text from which the language should be detected.
    :param language: the language to check if the text belongs to.
    :return the detected language.
    """
    return langdetect.detect(text) == language
