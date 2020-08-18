#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections.abc import Collection, Container
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Union

from ycontract import ContractError

__all__ = [
    'more_than',
    'less_than',
    'more_than_or_eq',
    'less_than_or_eq',
    'in_range',
    'is_sub',
    'is_type',
    'is_instance',
    'is_in',
    'exists_path',
]


@dataclass
class CondFunction:
    f: Callable[[Any], bool]

    def __or__(self, other):
        return CondFunction(lambda x: self(x).__or__(other(x)))

    def __xor__(self, other):
        return CondFunction(lambda x: self(x).__xor__(other(x)))

    def __and__(self, other):
        return CondFunction(lambda x: self(x).__and__(other(x)))

    def __call__(self, x):
        return self.f(x)  # type: ignore


def not_f(condf: Callable[..., bool]) -> Callable[..., bool]:
    return CondFunction(lambda x: not condf(x))


def _to_native_number(x) -> float:
    if hasattr(x, '__float__'):
        return float(x)
    elif hasattr(x, '__int__'):
        return int(x)
    else:
        raise ContractError(f"{x} is not a number.")


def more_than(more_than_target) -> Callable[[Any], bool]:
    more_than_target = _to_native_number(more_than_target)

    @CondFunction
    def _more_than(x) -> bool:
        return _to_native_number(x) > more_than_target

    return _more_than


is_positive = more_than(0.0)


def less_than(less_than_target) -> Callable[[Any], bool]:
    less_than_target = _to_native_number(less_than_target)

    @CondFunction
    def _less_than(x) -> bool:
        return _to_native_number(x) < less_than_target

    return _less_than


is_negative = less_than(0.0)


def more_than_or_eq(more_than_target) -> Callable[[Any], bool]:
    more_than_target = _to_native_number(more_than_target)

    @CondFunction
    def _more_than_or_eq(x) -> bool:
        return _to_native_number(x) >= more_than_target

    return _more_than_or_eq


def less_than_or_eq(less_than_target) -> Callable[[Any], bool]:
    less_than_target = _to_native_number(less_than_target)

    @CondFunction
    def _less_than_or_eq(x) -> bool:
        return _to_native_number(x) <= less_than_target

    return _less_than_or_eq


def in_range(a, b=None) -> Callable[[Any], bool]:
    if b is None:
        start, until = 0, a
    else:
        start, until = a, b

    @CondFunction
    def _in_range(x) -> bool:
        return start <= x < until

    return _in_range


def is_sub(sup: Collection) -> Callable[[Any], bool]:
    set_sup = set(sup)

    @CondFunction
    def _is_sub(sub: Collection):
        return set(sub) <= set_sup

    return _is_sub


def is_type(type_: Union[type, str]) -> Callable[[Any], bool]:

    @CondFunction
    def _is_type(x) -> bool:
        if isinstance(type_, type):
            return type(x) is type_
        else:
            return x.__class__.__name__ == type_

    return _is_type


def is_instance(type_: Union[type, str]) -> Callable[[Any], bool]:

    @CondFunction
    def _is_instance(x) -> bool:
        if isinstance(type_, type):
            return isinstance(x, type_)
        else:
            bases = {base.__name__ for base in x.__class__.__bases__}
            print(bases)
            return type_ in bases

    return _is_instance


def is_in(c: Container) -> Callable[[Any], bool]:

    @CondFunction
    def _is_in(x) -> bool:
        return x in c

    return _is_in


def exists_path(p: Union[str, Path]) -> bool:
    return Path(p).exists()
