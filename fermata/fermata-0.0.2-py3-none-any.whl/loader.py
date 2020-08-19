import importlib
import typing
import types
from functools import reduce


def import_module(operation_id: str) -> types.ModuleType:
    # if '.' not exists, raise ValueError
    end = operation_id.rindex('.')
    while end > 0:
        try:
            module = importlib.import_module(operation_id[:end])
            return module, operation_id[end + 1:]
        except ImportError:
            # if no module loaded, raise ValueError
            end = operation_id.rindex('.', 0, end)

    raise ValueError(f'operation_id error: "{operation_id}"')


def load(operation_id: str) -> typing.Callable:
    # load module
    mod, obj_path = import_module(operation_id)
    # load func from mod.attr
    return reduce(getattr, obj_path.split('.'), mod)


def preload(operation_ids: typing.Sequence[str]) -> None:
    for op in operation_ids:
        import_module(op)
