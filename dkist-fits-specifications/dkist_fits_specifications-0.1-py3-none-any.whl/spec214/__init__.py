"""
Functions and schemas relating to specification 214, the level 1 FITS files.

The 214 schemas are more complex than the 122 ones, as they have more uses, and
are tightly coupled to the 122 schemas.
There are three main variants to the 214 schemas:

  * The **raw schemas** as saved in the yaml files. Each 214 raw schema can
    reference a 122 schema, from which it can copy the 'type', 'default_value',
    'values', and 'format' fields for keys. A key can be marked as ``copy:
    True`` to indicate that the schema **and** the value should be the same in
    214 as 122, or it can be marked as ``copy: 'schema'`` to indicate that just
    the schema is the same for that key, but the value will be regenerated.
  * The **full schemas**. The full schemas are processed to merge the values in
    the schema header, and any values from the corresponding 122 schema. These
    schemas contain a lot more fields than the 122 schemas do, as these schemas
    are also used to generate documentation describing the specification.
  * The **validation schema**. These schemas (returned by `.load_spec214`) are
    the equivalent to the schemas returned by `.load_spec122`. They have all
    the extra fields present in the "full" schemas removed.

"""
import copy
from typing import Any, Dict, List, Tuple, Optional, cast
from pathlib import Path

import yamale  # type: ignore
import yaml

from dkist_fits_specifications import spec122, validation_schema
from dkist_fits_specifications.utils import (load_raw_spec,
                                             raw_schema_type_hint,
                                             schema_type_hint,)

__all__ = ['load_raw_spec214', 'load_full_spec214', 'load_spec214']


base_path = Path(__file__).parent / "schemas"

full_schema_214 = yamale.make_schema(Path(__file__).parent / "spec214_full_schema.yml")


def update_with_122(section_122: Optional[str], schema: schema_type_hint) -> schema_type_hint:
    """
    Update the raw spec 214 schemas with information from the 122 schemas.

    Parameters
    ----------
    section_122
        The section in the 122 specifications to update the schema with.
    schema
        The schema to update, should be the body of a unprocessed 214 schema.

    Returns
    -------
    schema
        The updated 214 schema.
    """
    if section_122 is None:
        return schema

    # Update the 214 schema with the data in the corresponding 122 schema
    schema_122 = spec122.load_raw_spec122(section_122)[section_122][1]

    import_keys = {'type', 'default_value', 'values', 'format'}

    for key, key_schema in schema.items():
        # Copy can be "schema" but that's all we care about here
        to_copy = bool(key_schema.get("copy", False))
        key_122 = key_schema.get("rename", key if to_copy else None)

        if key_122:
            if key_122 not in schema_122:
                print(
                    f"{key_122} is not in the 122 schema for {section_122},"
                    " although the 214 section references it."
                )
                continue
            key_schema_122 = schema_122[key_122]
            update_122 = dict(filter(lambda i: i[0] in import_keys,
                                     key_schema_122.items()))
            schema[key] = {**key_schema, **update_122}

    return schema


def update_schema_with_header(raw_schema: Tuple[Dict, schema_type_hint]) -> schema_type_hint:
    """
    Merge the body of a schema with its header.

    Parameters
    ----------
    raw_schema
        The loaded version of a single yaml file.

    Returns
    -------
    schema
        The body of a schema, updated with the header.
    """
    header, raw_schemas = raw_schema
    header = copy.deepcopy(header)["spec214"]

    # Remove the 122 section name
    header.pop("section_122")

    key_schemas = {}
    for key, key_schema in raw_schemas.items():
        updated_schema = {key: {**header, **key_schema}}
        # Expected takes the value of required unless overridden
        updated_schema[key]["expected"] = updated_schema[key].get("expected",
                                                                  updated_schema[key]["required"])
        yamale.validate(full_schema_214, [(updated_schema, None)])
        key_schemas.update(updated_schema)

    return key_schemas


def preprocess_schema(raw_schema: raw_schema_type_hint) -> schema_type_hint:
    """
    Convert the loaded raw schemas to the full 214 schema.

    Parameters
    ----------
    raw_schema
        The loaded version of a single yaml file.

    Returns
    -------
    schema
        The body of a schema, updated with the header and the relevant values
        from the 122 schema where appropriate.
    """
    section_122 = raw_schema[0]["spec214"]["section_122"]

    # Merge in the keys in the header with all the keys
    schema = update_schema_with_header(raw_schema)

    return update_with_122(section_122, schema)


def load_raw_spec214(glob: Optional[str] = None) -> Dict[str, raw_schema_type_hint]:
    """
    Load the raw 214 schemas from the yaml files.

    Parameters
    ----------
    glob
        A pattern to use to match a file, without the ``.yml`` file extension.
        Can be a section name like ``'wcs'``.

    Returns
    -------
    raw_schemas
        The schemas as loaded from the yaml files.
    """
    return load_raw_spec(base_path, glob)


def load_full_spec214(glob: Optional[str] = None) -> Dict[str, schema_type_hint]:
    """
    Return the full loaded schemas for DKIST Specification 214

    Parameters
    ----------
    glob
        A pattern to use to match a file, without the ``.yml`` file extension.
        Can be a section name like ``'wcs'``.

    """

    raw_schemas = load_raw_spec214(glob)

    schemas = {}
    for schema_name, raw_schema in raw_schemas.items():
        schema = preprocess_schema(raw_schema)
        yamale.validate(full_schema_214, [(schema, None)])
        schemas[schema_name] = schema

    return schemas


def load_spec214(glob: Optional[str] = None) -> Dict[str, schema_type_hint]:
    """
    Load the simple schema version of 214 for validation or generation.

    Parameters
    ----------
    glob
        A pattern to use to match a file, without the ``.yml`` file extension.
        Can be a section name like ``'wcs'``.
    """

    full_schemas = load_full_spec214(glob)

    # Extract the keys from the base schema.
    allowed_keys = validation_schema.includes['key'].dict.keys()

    schemas = {}
    for schema_name, full_schema in full_schemas.items():
        schema = {}
        for key, key_schema in full_schema.items():
            filtered_schema = dict(filter(lambda i: i[0] in allowed_keys,
                                          key_schema.items()))
            schema[key] = filtered_schema
        # Validate the schema against the simple schema
        yamale.validate(validation_schema, [(schema, None)])
        schemas[schema_name] = schema

    return schemas
