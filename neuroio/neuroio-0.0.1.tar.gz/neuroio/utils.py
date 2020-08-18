import functools
from importlib import import_module
from typing import Any, Callable, List, Optional, TypeVar, Union

from neuroio.constants import sentinel


def get_package_version() -> str:
    from neuroio import __version__

    return __version__


def dynamic_import(abs_path: str, attribute: str) -> Any:
    """
    Imports any attribute from the module specified as string dotted path.
    Takes into account current supplied version to the Client instance.

    :param abs_path: dotted path of the module from which to import from
    :param attribute: function, class or any other attr to be imported
    :return: imported attribute
    """
    module_object = import_module(abs_path)
    return getattr(module_object, attribute)


F = TypeVar("F", bound=Callable[..., Any])


def cached_property(f: F) -> property:
    return property(functools.lru_cache()(f))


def process_query_params(params: dict) -> dict:
    for key, item in params.items():
        if isinstance(item, list):
            params[key] = ",".join(map(str, item))
    return params


def request_dict_processing(
    local_items: dict, reserved_names: List[str]
) -> dict:
    return dict(
        filter(
            lambda kwarg: kwarg[1] is not sentinel
            and kwarg[0] not in reserved_names,
            local_items.items(),
        )
    )


def request_query_processing(
    local_items: dict, reserved_names: List[str]
) -> dict:
    return process_query_params(
        request_dict_processing(local_items, reserved_names)
    )
