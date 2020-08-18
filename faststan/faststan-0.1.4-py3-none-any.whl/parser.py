from inspect import signature, _empty
from typing import Callable, Generic, TypeVar, Any
from types import BuiltinFunctionType, FunctionType

from pydantic import BaseModel, ValidationError


T = TypeVar("T")


class PydanticParserMixin(Generic[T]):
    @staticmethod
    def __get_parser__(
        function: Callable[[T], None], arbitrary_types_allowed: bool = True
    ) -> Callable[[bytes], Any]:
        """Return argument parser for given function."""
        s = signature(function)

        try:
            name, param = list(s.parameters.items())[0]
        except IndexError:
            return None, None, None

        annotation = param.annotation
        try:
            is_model = issubclass(annotation, BaseModel)
        except TypeError:
            is_model = False

        # Case 1: We got a pydantic model
        if is_model:

            def parser(data: bytes) -> T:
                return annotation.parse_raw(data)

        # Case 2: We don't have an annotation
        elif annotation is _empty:

            def parser(data: bytes) -> bytes:
                return data

        # Case 3: It's a function
        # NOTE: This branch fu**s all types in the function...
        #       We should not accept functions in the first place!
        # PROPOSAL: Instead we could give a function in the decorator.
        elif isinstance(annotation, (FunctionType, BuiltinFunctionType)):

            def parser(data: bytes) -> T:
                return annotation(data)

        # Case 4: It's something else. Let pydantic perform the validation
        else:

            class _Model(BaseModel):
                __root__: annotation

                class Config:
                    arbitrary_types_allowed = True

            def parser(data: bytes) -> T:
                try:
                    return _Model.parse_raw(data).__root__
                except ValidationError as main_error:
                    try:
                        return _Model(__root__=data).__root__
                    except ValidationError:
                        pass
                    raise main_error

        return name, annotation, parser
