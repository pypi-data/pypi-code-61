# -*- coding: utf-8 -*-
"""Misc utils. Currently largely for assistance testing domain models."""
import copy
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union

from domain_model import DomainModel
import pytest


def copy_dict_with_key_removed(
    the_dict: Dict[Any, Any], key_to_remove: str = None
) -> Dict[Any, Any]:
    new_dict = copy.deepcopy(the_dict)
    if key_to_remove is not None:
        del new_dict[key_to_remove]
    return new_dict


def _init_domain_model(
    model: DomainModel,
    attribute_under_test: Optional[str] = None,
    test_value: Optional[Any] = None,
    additional_kwargs: Optional[Dict[str, Any]] = None,
) -> DomainModel:
    if additional_kwargs is None:
        additional_kwargs = dict()
    if attribute_under_test is not None:
        additional_kwargs[attribute_under_test] = test_value
    domain_model = model(**additional_kwargs)
    return domain_model


def _domain_model_validation_test(
    callable_to_run: Callable[[Any], Any],
    expected_error: Optional[Exception],
    expected_texts_in_error: Optional[Union[List[str], Tuple[str]]],
    autopopulate: bool = False,
) -> None:
    if expected_error is not None:
        with pytest.raises(expected_error) as e:
            callable_to_run(autopopulate=autopopulate)  # type: ignore
        if expected_texts_in_error is not None:
            if not isinstance(expected_texts_in_error, (list, tuple)):
                expected_texts_in_error = [expected_texts_in_error]
            for this_expected_text_in_error in expected_texts_in_error:
                assert this_expected_text_in_error in str(e)
    else:
        callable_to_run(autopopulate=autopopulate)  # type: ignore


def domain_model_validation_test(
    model: DomainModel,
    attribute_under_test: Optional[str] = None,
    test_value: Optional[Any] = None,
    additional_kwargs: Optional[Dict[str, Any]] = None,
    expected_error: Optional[Exception] = None,
    expected_texts_in_error: Optional[Union[List[str], Tuple[str]]] = None,
    autopopulate: bool = False,
) -> None:
    """Help for testing the validate method."""
    domain_model = _init_domain_model(
        model, attribute_under_test, test_value, additional_kwargs
    )
    _domain_model_validation_test(
        domain_model.validate,
        expected_error,
        expected_texts_in_error,
        autopopulate=autopopulate,
    )


def domain_model_validate_internals_test(
    model: DomainModel,
    attribute_under_test: Optional[str] = None,
    test_value: Optional[Any] = None,
    additional_kwargs: Optional[Dict[str, Any]] = None,
    expected_error: Optional[Exception] = None,
    expected_texts_in_error: Optional[Union[List[str], Tuple[str]]] = None,
    autopopulate: bool = False,
) -> None:
    """Help for testing the validate_internals method."""
    domain_model = _init_domain_model(
        model, attribute_under_test, test_value, additional_kwargs
    )
    _domain_model_validation_test(
        domain_model.validate_internals,
        expected_error,
        expected_texts_in_error,
        autopopulate=autopopulate,
    )
