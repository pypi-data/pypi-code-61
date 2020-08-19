from typing import Any, Dict, Union, cast

import httpx

from ..client import Client
from ..errors import ApiResponseError
from ..models.assay_result_schema import AssayResultSchema
from ..models.assay_run_schema import AssayRunSchema
from ..models.batch_schema import BatchSchema
from ..models.box_schema import BoxSchema
from ..models.not_found_error import NotFoundError
from ..models.plate_schema import PlateSchema
from ..models.request_schema import RequestSchema
from ..models.schema import Schema
from ..models.tag_schema import TagSchema


async def get_location_schema(
    *, client: Client, schema_id: str,
) -> Union[
    Schema, None, NotFoundError,
]:

    """ None """
    url = "{}/location-schemas/{schema_id}".format(client.base_url, schema_id=schema_id,)

    async with httpx.AsyncClient() as _client:
        response = await _client.get(url=url, headers=client.get_headers(),)

    if response.status_code == 200:
        return Schema.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return None
    if response.status_code == 404:
        return NotFoundError.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise ApiResponseError(response=response)


async def get_box_schema(
    *, client: Client, schema_id: str,
) -> Union[
    BoxSchema, None, NotFoundError,
]:

    """ None """
    url = "{}/box-schemas/{schema_id}".format(client.base_url, schema_id=schema_id,)

    async with httpx.AsyncClient() as _client:
        response = await _client.get(url=url, headers=client.get_headers(),)

    if response.status_code == 200:
        return BoxSchema.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return None
    if response.status_code == 404:
        return NotFoundError.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise ApiResponseError(response=response)


async def get_plate_schema(
    *, client: Client, schema_id: str,
) -> Union[
    PlateSchema, None, NotFoundError,
]:

    """ None """
    url = "{}/plate-schemas/{schema_id}".format(client.base_url, schema_id=schema_id,)

    async with httpx.AsyncClient() as _client:
        response = await _client.get(url=url, headers=client.get_headers(),)

    if response.status_code == 200:
        return PlateSchema.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return None
    if response.status_code == 404:
        return NotFoundError.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise ApiResponseError(response=response)


async def get_container_schema(
    *, client: Client, schema_id: str,
) -> Union[
    Schema, None, NotFoundError,
]:

    """ None """
    url = "{}/container-schemas/{schema_id}".format(client.base_url, schema_id=schema_id,)

    async with httpx.AsyncClient() as _client:
        response = await _client.get(url=url, headers=client.get_headers(),)

    if response.status_code == 200:
        return Schema.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return None
    if response.status_code == 404:
        return NotFoundError.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise ApiResponseError(response=response)


async def get_batch_schema(
    *, client: Client, schema_id: str,
) -> Union[
    BatchSchema, None, NotFoundError,
]:

    """ None """
    url = "{}/batch-schemas/{schema_id}".format(client.base_url, schema_id=schema_id,)

    async with httpx.AsyncClient() as _client:
        response = await _client.get(url=url, headers=client.get_headers(),)

    if response.status_code == 200:
        return BatchSchema.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return None
    if response.status_code == 404:
        return NotFoundError.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise ApiResponseError(response=response)


async def get_entity_schema(
    *, client: Client, schema_id: str,
) -> Union[
    TagSchema, None, NotFoundError,
]:

    """ None """
    url = "{}/entity-schemas/{schema_id}".format(client.base_url, schema_id=schema_id,)

    async with httpx.AsyncClient() as _client:
        response = await _client.get(url=url, headers=client.get_headers(),)

    if response.status_code == 200:
        return TagSchema.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return None
    if response.status_code == 404:
        return NotFoundError.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise ApiResponseError(response=response)


async def get_run_schema(
    *, client: Client, schema_id: str,
) -> Union[
    AssayRunSchema, None, NotFoundError,
]:

    """ None """
    url = "{}/assay-run-schemas/{schema_id}".format(client.base_url, schema_id=schema_id,)

    async with httpx.AsyncClient() as _client:
        response = await _client.get(url=url, headers=client.get_headers(),)

    if response.status_code == 200:
        return AssayRunSchema.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return None
    if response.status_code == 404:
        return NotFoundError.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise ApiResponseError(response=response)


async def get_result_schema(
    *, client: Client, schema_id: str,
) -> Union[
    AssayResultSchema, None, NotFoundError,
]:

    """ None """
    url = "{}/assay-result-schemas/{schema_id}".format(client.base_url, schema_id=schema_id,)

    async with httpx.AsyncClient() as _client:
        response = await _client.get(url=url, headers=client.get_headers(),)

    if response.status_code == 200:
        return AssayResultSchema.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return None
    if response.status_code == 404:
        return NotFoundError.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise ApiResponseError(response=response)


async def get_request_schema(
    *, client: Client, schema_id: str,
) -> Union[
    RequestSchema, None, NotFoundError,
]:

    """ None """
    url = "{}/request-schemas/{schema_id}".format(client.base_url, schema_id=schema_id,)

    async with httpx.AsyncClient() as _client:
        response = await _client.get(url=url, headers=client.get_headers(),)

    if response.status_code == 200:
        return RequestSchema.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return None
    if response.status_code == 404:
        return NotFoundError.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise ApiResponseError(response=response)
