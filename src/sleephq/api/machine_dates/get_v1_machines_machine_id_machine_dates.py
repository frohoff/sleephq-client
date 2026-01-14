from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_machine_date_serializer_list import ApiV1MachineDateSerializerList
from ...models.get_v1_machines_machine_id_machine_dates_sort_order import GetV1MachinesMachineIdMachineDatesSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    machine_id: int,
    *,
    sort_order: GetV1MachinesMachineIdMachineDatesSortOrder | Unset = GetV1MachinesMachineIdMachineDatesSortOrder.DESC,
    page: int | Unset = 1,
    per_page: int | Unset = 100,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sort_order"] = json_sort_order

    params["page"] = page

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/machines/{machine_id}/machine_dates".format(
            machine_id=quote(str(machine_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ApiV1MachineDateSerializerList | None:
    if response.status_code == 200:
        response_200 = ApiV1MachineDateSerializerList.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ApiV1MachineDateSerializerList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    machine_id: int,
    *,
    client: AuthenticatedClient | Client,
    sort_order: GetV1MachinesMachineIdMachineDatesSortOrder | Unset = GetV1MachinesMachineIdMachineDatesSortOrder.DESC,
    page: int | Unset = 1,
    per_page: int | Unset = 100,
) -> Response[Any | ApiV1MachineDateSerializerList]:
    """List Machine Dates

    Args:
        machine_id (int):
        sort_order (GetV1MachinesMachineIdMachineDatesSortOrder | Unset):  Default:
            GetV1MachinesMachineIdMachineDatesSortOrder.DESC.
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiV1MachineDateSerializerList]
    """

    kwargs = _get_kwargs(
        machine_id=machine_id,
        sort_order=sort_order,
        page=page,
        per_page=per_page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    machine_id: int,
    *,
    client: AuthenticatedClient | Client,
    sort_order: GetV1MachinesMachineIdMachineDatesSortOrder | Unset = GetV1MachinesMachineIdMachineDatesSortOrder.DESC,
    page: int | Unset = 1,
    per_page: int | Unset = 100,
) -> Any | ApiV1MachineDateSerializerList | None:
    """List Machine Dates

    Args:
        machine_id (int):
        sort_order (GetV1MachinesMachineIdMachineDatesSortOrder | Unset):  Default:
            GetV1MachinesMachineIdMachineDatesSortOrder.DESC.
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiV1MachineDateSerializerList
    """

    return sync_detailed(
        machine_id=machine_id,
        client=client,
        sort_order=sort_order,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    machine_id: int,
    *,
    client: AuthenticatedClient | Client,
    sort_order: GetV1MachinesMachineIdMachineDatesSortOrder | Unset = GetV1MachinesMachineIdMachineDatesSortOrder.DESC,
    page: int | Unset = 1,
    per_page: int | Unset = 100,
) -> Response[Any | ApiV1MachineDateSerializerList]:
    """List Machine Dates

    Args:
        machine_id (int):
        sort_order (GetV1MachinesMachineIdMachineDatesSortOrder | Unset):  Default:
            GetV1MachinesMachineIdMachineDatesSortOrder.DESC.
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiV1MachineDateSerializerList]
    """

    kwargs = _get_kwargs(
        machine_id=machine_id,
        sort_order=sort_order,
        page=page,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    machine_id: int,
    *,
    client: AuthenticatedClient | Client,
    sort_order: GetV1MachinesMachineIdMachineDatesSortOrder | Unset = GetV1MachinesMachineIdMachineDatesSortOrder.DESC,
    page: int | Unset = 1,
    per_page: int | Unset = 100,
) -> Any | ApiV1MachineDateSerializerList | None:
    """List Machine Dates

    Args:
        machine_id (int):
        sort_order (GetV1MachinesMachineIdMachineDatesSortOrder | Unset):  Default:
            GetV1MachinesMachineIdMachineDatesSortOrder.DESC.
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiV1MachineDateSerializerList
    """

    return (
        await asyncio_detailed(
            machine_id=machine_id,
            client=client,
            sort_order=sort_order,
            page=page,
            per_page=per_page,
        )
    ).parsed
