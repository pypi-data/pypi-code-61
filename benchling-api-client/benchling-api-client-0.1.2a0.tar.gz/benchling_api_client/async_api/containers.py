from typing import Any, Dict, Optional, Union, cast

import httpx

from ..client import Client
from ..errors import ApiResponseError
from ..models.container import Container
from ..models.container_content import ContainerContent
from ..models.not_found_error import NotFoundError
from ..models.sort1 import Sort1


async def get_container(*, client: Client, container_id: str,) -> Container:

    """ get a container by id """
    url = "{}/containers/{container_id}".format(client.base_url, container_id=container_id,)

    async with httpx.AsyncClient() as _client:
        response = await _client.get(url=url, headers=client.get_headers(),)

    if response.status_code == 200:
        return Container.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise ApiResponseError(response=response)


async def list_containers(
    *,
    client: Client,
    page_size: Optional[int] = 50,
    next_token: Optional[str] = None,
    sort: Optional[Sort1] = Sort1.MODIFIED_AT,
    schema_id: Optional[str] = None,
    modified_at: Optional[str] = None,
    name: Optional[str] = None,
    ancestor_storage_id: Optional[str] = None,
    storage_contents_id: Optional[str] = None,
    archive_reason: Optional[str] = None,
    parent_storage_schema_id: Optional[str] = None,
    assay_run_id: Optional[str] = None,
    checkout_status: Optional[str] = None,
) -> Union[
    Container, None, NotFoundError,
]:

    """ get a list of containers """
    url = "{}/containers".format(client.base_url,)

    json_sort = sort.value if sort else None

    params: Dict[str, Any] = {}
    if page_size is not None:
        params["pageSize"] = page_size
    if next_token is not None:
        params["nextToken"] = next_token
    if sort is not None:
        params["sort"] = json_sort
    if schema_id is not None:
        params["schemaId"] = schema_id
    if modified_at is not None:
        params["modifiedAt"] = modified_at
    if name is not None:
        params["name"] = name
    if ancestor_storage_id is not None:
        params["ancestorStorageId"] = ancestor_storage_id
    if storage_contents_id is not None:
        params["storageContentsId"] = storage_contents_id
    if archive_reason is not None:
        params["archiveReason"] = archive_reason
    if parent_storage_schema_id is not None:
        params["parentStorageSchemaId"] = parent_storage_schema_id
    if assay_run_id is not None:
        params["assayRunId"] = assay_run_id
    if checkout_status is not None:
        params["checkoutStatus"] = checkout_status

    async with httpx.AsyncClient() as _client:
        response = await _client.get(url=url, headers=client.get_headers(), params=params,)

    if response.status_code == 200:
        return Container.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return None
    if response.status_code == 404:
        return NotFoundError.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise ApiResponseError(response=response)


async def get_container_content(
    *, client: Client, container_id: str, containable_id: str,
) -> Union[
    ContainerContent, NotFoundError,
]:

    """ Get a container content """
    url = "{}/containers/{container_id}/contents/{containable_id}".format(
        client.base_url, container_id=container_id, containable_id=containable_id,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(url=url, headers=client.get_headers(),)

    if response.status_code == 200:
        return ContainerContent.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 404:
        return NotFoundError.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise ApiResponseError(response=response)


async def delete_container_content(
    *, client: Client, container_id: str, containable_id: str,
) -> Union[
    None, NotFoundError,
]:

    """ Delete a container content """
    url = "{}/containers/{container_id}/contents/{containable_id}".format(
        client.base_url, container_id=container_id, containable_id=containable_id,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.delete(url=url, headers=client.get_headers(),)

    if response.status_code == 200:
        return None
    if response.status_code == 404:
        return NotFoundError.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise ApiResponseError(response=response)


async def update_container_content(
    *, client: Client, container_id: str, containable_id: str, json_body: Dict[Any, Any],
) -> Union[
    ContainerContent, NotFoundError,
]:

    """ Update a container content """
    url = "{}/containers/{container_id}/contents/{containable_id}".format(
        client.base_url, container_id=container_id, containable_id=containable_id,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.patch(url=url, headers=client.get_headers(), json=json_body,)

    if response.status_code == 200:
        return ContainerContent.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 404:
        return NotFoundError.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise ApiResponseError(response=response)
