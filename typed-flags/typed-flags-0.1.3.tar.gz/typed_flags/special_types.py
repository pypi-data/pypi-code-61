"""Custom types for use with TypedFlags."""
from argparse import Action
from typing import Any

__all__ = ["StoreDictKeyPair"]


class StoreDictKeyPair(Action):
    """Action for parsing dictionaries on the commandline."""

    def __init__(
        self, option_strings: Any, key_type: type, value_type: type, *args: Any, **kwargs: Any
    ):
        self._key_type = key_type
        self._value_type = value_type
        super().__init__(option_strings, *args, **kwargs)

    def __call__(self, parser: Any, namespace: Any, values: Any, option_string: Any = None) -> None:
        my_dict = {}
        for key_value in values:
            key, value = key_value.split("=")
            my_dict[self._key_type(key.strip())] = self._value_type(value.strip())
        setattr(namespace, self.dest, my_dict)
