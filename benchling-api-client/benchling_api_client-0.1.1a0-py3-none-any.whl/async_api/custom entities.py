from typing import Any, Dict, Union, cast

import httpx

from ..client import Client
from ..errors import ApiResponseError
from ..models.async_task_link import AsyncTaskLink
from ..models.bad_request_error import BadRequestError
from ..models.conflict_error import ConflictError
from ..models.custom_entity_create import CustomEntityCreate
from ..models.custom_entity_patch import CustomEntityPatch
from ..models.custom_entity_response import CustomEntityResponse


async def create_custom_entities(
    *, client: Client, json_body: CustomEntityCreate,
) -> Union[
    CustomEntityResponse, None, ConflictError, BadRequestError,
]:

    """ Create a custom entity """
    url = "{}/custom-entities".format(client.base_url,)

    json_body.to_dict()

    async with httpx.AsyncClient() as _client:
        response = await _client.post(url=url, headers=client.get_headers(), json=json_body,)

    if response.status_code == 201:
        return CustomEntityResponse.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 503:
        return None
    if response.status_code == 409:
        return ConflictError.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return BadRequestError.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise ApiResponseError(response=response)


async def get_custom_entity(
    *, client: Client, custom_entity_id: str,
) -> Union[
    CustomEntityResponse, BadRequestError,
]:

    """ Get a custom entity """
    url = "{}/custom-entities/{custom_entity_id}".format(client.base_url, custom_entity_id=custom_entity_id,)

    async with httpx.AsyncClient() as _client:
        response = await _client.get(url=url, headers=client.get_headers(),)

    if response.status_code == 200:
        return CustomEntityResponse.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return BadRequestError.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise ApiResponseError(response=response)


async def update_custom_entity(
    *, client: Client, custom_entity_id: str, json_body: CustomEntityPatch,
) -> Union[
    CustomEntityResponse, BadRequestError,
]:

    """ Update a custom entity """
    url = "{}/custom-entities/{custom_entity_id}".format(client.base_url, custom_entity_id=custom_entity_id,)

    json_body.to_dict()

    async with httpx.AsyncClient() as _client:
        response = await _client.patch(url=url, headers=client.get_headers(), json=json_body,)

    if response.status_code == 200:
        return CustomEntityResponse.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return BadRequestError.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise ApiResponseError(response=response)


async def bulk_create_custom_entities(
    *, client: Client, json_body: Dict[Any, Any],
) -> Union[
    AsyncTaskLink, BadRequestError,
]:

    """ Bulk Create custom entities """
    url = "{}/custom-entities:bulk-create".format(client.base_url,)

    async with httpx.AsyncClient() as _client:
        response = await _client.post(url=url, headers=client.get_headers(), json=json_body,)

    if response.status_code == 202:
        return AsyncTaskLink.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return BadRequestError.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise ApiResponseError(response=response)
