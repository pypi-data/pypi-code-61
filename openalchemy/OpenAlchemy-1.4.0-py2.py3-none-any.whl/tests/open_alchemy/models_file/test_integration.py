"""Tests for models file."""

import sys

import pytest
from mypy import api

from open_alchemy import models_file

_DOCSTRING = '"""Autogenerated SQLAlchemy models based on OpenAlchemy models."""'
_EXPECTED_TD_BASE = "typing.TypedDict"
if sys.version_info[1] < 8:
    _EXPECTED_TD_BASE = "typing_extensions.TypedDict"
_EXPECTED_MODEL_BASE = "typing.Protocol"
if sys.version_info[1] < 8:
    _EXPECTED_MODEL_BASE = "typing_extensions.Protocol"
_ADDITIONAL_IMPORT = ""
if sys.version_info[1] < 8:
    _ADDITIONAL_IMPORT = """
import typing_extensions"""


@pytest.mark.parametrize(
    "schemas, expected_source",
    [
        (
            [({"properties": {"id": {"type": "integer"}}}, "Model")],
            f'''{_DOCSTRING}
# pylint: disable=no-member,super-init-not-called,unused-argument

import typing

import sqlalchemy{_ADDITIONAL_IMPORT}
from sqlalchemy import orm

from open_alchemy import models


class ModelDict({_EXPECTED_TD_BASE}, total=False):
    """TypedDict for properties that are not required."""

    id: typing.Optional[int]


class TModel({_EXPECTED_MODEL_BASE}):
    """
    SQLAlchemy model protocol.

    Attrs:
        id: The id of the Model.

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: "sqlalchemy.Column[typing.Optional[int]]"

    def __init__(self, id: typing.Optional[int] = None) -> None:
        """
        Construct.

        Args:
            id: The id of the Model.

        """
        ...

    @classmethod
    def from_dict(cls, id: typing.Optional[int] = None) -> "TModel":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: The id of the Model.

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TModel":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> ModelDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


Model: typing.Type[TModel] = models.Model  # type: ignore
''',
        ),
        (
            [
                ({"properties": {"id": {"type": "integer"}}}, "Model1"),
                ({"properties": {"id": {"type": "string"}}}, "Model2"),
            ],
            f'''{_DOCSTRING}
# pylint: disable=no-member,super-init-not-called,unused-argument

import typing

import sqlalchemy{_ADDITIONAL_IMPORT}
from sqlalchemy import orm

from open_alchemy import models


class Model1Dict({_EXPECTED_TD_BASE}, total=False):
    """TypedDict for properties that are not required."""

    id: typing.Optional[int]


class TModel1({_EXPECTED_MODEL_BASE}):
    """
    SQLAlchemy model protocol.

    Attrs:
        id: The id of the Model1.

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: "sqlalchemy.Column[typing.Optional[int]]"

    def __init__(self, id: typing.Optional[int] = None) -> None:
        """
        Construct.

        Args:
            id: The id of the Model1.

        """
        ...

    @classmethod
    def from_dict(cls, id: typing.Optional[int] = None) -> "TModel1":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: The id of the Model1.

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TModel1":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> Model1Dict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


Model1: typing.Type[TModel1] = models.Model1  # type: ignore


class Model2Dict({_EXPECTED_TD_BASE}, total=False):
    """TypedDict for properties that are not required."""

    id: typing.Optional[str]


class TModel2({_EXPECTED_MODEL_BASE}):
    """
    SQLAlchemy model protocol.

    Attrs:
        id: The id of the Model2.

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: "sqlalchemy.Column[typing.Optional[str]]"

    def __init__(self, id: typing.Optional[str] = None) -> None:
        """
        Construct.

        Args:
            id: The id of the Model2.

        """
        ...

    @classmethod
    def from_dict(cls, id: typing.Optional[str] = None) -> "TModel2":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: The id of the Model2.

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TModel2":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> Model2Dict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


Model2: typing.Type[TModel2] = models.Model2  # type: ignore
''',
        ),
    ],
    ids=["single", "multiple"],
)
@pytest.mark.models_file
def test_integration(schemas, expected_source):
    """
    GIVEN schema and name
    WHEN schema is added to the models file and the models file is generated
    THEN the models source code is returned.
    """
    models = models_file.ModelsFile()
    for schema, name in schemas:
        models.add_model(schema=schema, name=name)
    source = models.generate_models()

    assert source == expected_source


@pytest.mark.models_file
def test_schema_change():
    """
    GIVEN schema and name
    WHEN schema is added to the models file, changed and then the models file is
        generated
    THEN the change is reflected in the models file.
    """
    schema = {"properties": {}}
    name = "Model"
    models = models_file.ModelsFile()

    models.add_model(schema=schema, name=name)
    schema["properties"]["id"] = {"type": "integer"}
    source = models.generate_models()

    expected_source = f'''{_DOCSTRING}
# pylint: disable=no-member,super-init-not-called,unused-argument

import typing

import sqlalchemy{_ADDITIONAL_IMPORT}
from sqlalchemy import orm

from open_alchemy import models


class ModelDict({_EXPECTED_TD_BASE}, total=False):
    """TypedDict for properties that are not required."""

    id: typing.Optional[int]


class TModel({_EXPECTED_MODEL_BASE}):
    """
    SQLAlchemy model protocol.

    Attrs:
        id: The id of the Model.

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: "sqlalchemy.Column[typing.Optional[int]]"

    def __init__(self, id: typing.Optional[int] = None) -> None:
        """
        Construct.

        Args:
            id: The id of the Model.

        """
        ...

    @classmethod
    def from_dict(cls, id: typing.Optional[int] = None) -> "TModel":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: The id of the Model.

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TModel":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> ModelDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


Model: typing.Type[TModel] = models.Model  # type: ignore
'''
    assert source == expected_source


@pytest.mark.models_file
def test_inheritance(mocked_facades_models):
    """
    GIVEN schema with inheritance and name
    WHEN schema is added to the models file
    THEN the models file is generated with the inheritance.
    """
    schema = {"properties": {"id": {"type": "integer"}}, "x-inherits": "Parent"}
    mocked_facades_models.get_model_schema.return_value = {
        "properties": {"name": {"type": "string"}}
    }
    name = "Model"
    models = models_file.ModelsFile()

    models.add_model(schema=schema, name=name)
    source = models.generate_models()

    expected_source = f'''{_DOCSTRING}
# pylint: disable=no-member,super-init-not-called,unused-argument

import typing

import sqlalchemy{_ADDITIONAL_IMPORT}
from sqlalchemy import orm

from open_alchemy import models


class ModelDict({_EXPECTED_TD_BASE}, total=False):
    """TypedDict for properties that are not required."""

    name: typing.Optional[str]
    id: typing.Optional[int]


class TModel({_EXPECTED_MODEL_BASE}):
    """
    SQLAlchemy model protocol.

    Attrs:
        name: The name of the Model.
        id: The id of the Model.

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    name: "sqlalchemy.Column[typing.Optional[str]]"
    id: "sqlalchemy.Column[typing.Optional[int]]"

    def __init__(
        self, name: typing.Optional[str] = None, id: typing.Optional[int] = None
    ) -> None:
        """
        Construct.

        Args:
            name: The name of the Model.
            id: The id of the Model.

        """
        ...

    @classmethod
    def from_dict(
        cls, name: typing.Optional[str] = None, id: typing.Optional[int] = None
    ) -> "TModel":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            name: The name of the Model.
            id: The id of the Model.

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TModel":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> ModelDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


Model: typing.Type[TModel] = models.Model  # type: ignore
'''
    assert source == expected_source


@pytest.mark.models_file
def test_multiple_calls():
    """
    GIVEN schema and name
    WHEN schema is added to the models file twice
    THEN the models file is generated once.
    """
    schema = {"properties": {"id": {"type": "integer"}}}
    name = "Model"
    models = models_file.ModelsFile()

    models.add_model(schema=schema, name=name)
    models.add_model(schema=schema, name=name)
    source = models.generate_models()

    expected_source = f'''{_DOCSTRING}
# pylint: disable=no-member,super-init-not-called,unused-argument

import typing

import sqlalchemy{_ADDITIONAL_IMPORT}
from sqlalchemy import orm

from open_alchemy import models


class ModelDict({_EXPECTED_TD_BASE}, total=False):
    """TypedDict for properties that are not required."""

    id: typing.Optional[int]


class TModel({_EXPECTED_MODEL_BASE}):
    """
    SQLAlchemy model protocol.

    Attrs:
        id: The id of the Model.

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: "sqlalchemy.Column[typing.Optional[int]]"

    def __init__(self, id: typing.Optional[int] = None) -> None:
        """
        Construct.

        Args:
            id: The id of the Model.

        """
        ...

    @classmethod
    def from_dict(cls, id: typing.Optional[int] = None) -> "TModel":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: The id of the Model.

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TModel":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> ModelDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


Model: typing.Type[TModel] = models.Model  # type: ignore
'''
    assert source == expected_source


def _generate_source(schemas, names):
    """Generate the models file source from a schema."""
    models = models_file.ModelsFile()
    for schema, name in zip(schemas, names):
        models.add_model(schema=schema, name=name)
    return models.generate_models()


def _create_source_file(source, tmp_path):
    """Create a file with the source code."""
    directory = tmp_path / "models"
    directory.mkdir()
    source_file = directory / "models.py"
    source_file.write_text(source)
    return source_file


@pytest.mark.parametrize(
    "schemas, names",
    [
        pytest.param(
            [{"properties": {"id": {"type": "integer"}}}], ["Model"], id="simple",
        ),
        pytest.param(
            [
                {"properties": {"id": {"type": "integer"}}},
                {"properties": {"model": {"type": "object", "x-de-$ref": "RefModel"}}},
            ],
            ["RefModel", "Model"],
            id="object",
        ),
    ],
)
@pytest.mark.models_file
@pytest.mark.slow
def test_generate_type_return(tmp_path, schemas, names):
    """
    GIVEN schema
    WHEN the models file is generated and mypy is run over it
    THEN no errors are returned.
    """
    source = _generate_source(schemas, names)
    source_file = _create_source_file(source, tmp_path)

    _, _, returncode = api.run([str(source_file)])

    assert returncode == 0


@pytest.mark.parametrize(
    "schema, mypy_check, expected_out_substr",
    [
        pytest.param(
            {"properties": {"id": {"type": "integer"}}},
            "reveal_type(Model.id)",
            "'sqlalchemy.sql.schema.Column[Union[builtins.int, None]]'",
            id="nullable column",
        ),
        pytest.param(
            {"properties": {"id": {"type": "integer"}}},
            "model = Model()\nreveal_type(model.id)",
            "'Union[builtins.int, None]'",
            id="nullable column instance",
        ),
        pytest.param(
            {"properties": {"id": {"type": "integer", "nullable": False}}},
            "reveal_type(Model.id)",
            "'sqlalchemy.sql.schema.Column[builtins.int*]'",
            id="not nullable column",
        ),
    ],
)
@pytest.mark.models_file
@pytest.mark.slow
def test_generate_type_check(tmp_path, schema, mypy_check, expected_out_substr):
    """
    GIVEN schema, a mypy check and expected mypy output substring
    WHEN the models file is generated and mypy is run over it
    THEN the expected output substring is in the mypy output.
    """
    source = _generate_source([schema], ["Model"]) + f"\n{mypy_check}"
    source_file = _create_source_file(source, tmp_path)

    out, _, _ = api.run([str(source_file)])

    assert expected_out_substr in out
