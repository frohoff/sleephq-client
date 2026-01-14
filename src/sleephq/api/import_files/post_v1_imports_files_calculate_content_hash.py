from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_v1_imports_files_calculate_content_hash_body import PostV1ImportsFilesCalculateContentHashBody
from ...types import Response


def _get_kwargs(
    *,
    body: PostV1ImportsFilesCalculateContentHashBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/imports/files/calculate_content_hash",
    }

    _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostV1ImportsFilesCalculateContentHashBody,
) -> Response[Any]:
    r"""Calculate the content hash of a file when testing your content_hash algorithm.
    Note - do not use this end point to calculate the content in your finished application.
    This end point is only for use when validating your own implementation of the content_hash
    algorithm.
    Excessive use of this end point may result in your account being rate limited.
    The content_hash is a MD5 hash of the file's content and name joined together.
    For example, if the file's name is \"file.txt\" and the file's content is \"Hello, World!\",
    the content_hash would be the MD5 hash of the string \"Hello, World!file.txt\"
    Do not include the file's path when calculating the content hash.

    Args:
        body (PostV1ImportsFilesCalculateContentHashBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostV1ImportsFilesCalculateContentHashBody,
) -> Response[Any]:
    r"""Calculate the content hash of a file when testing your content_hash algorithm.
    Note - do not use this end point to calculate the content in your finished application.
    This end point is only for use when validating your own implementation of the content_hash
    algorithm.
    Excessive use of this end point may result in your account being rate limited.
    The content_hash is a MD5 hash of the file's content and name joined together.
    For example, if the file's name is \"file.txt\" and the file's content is \"Hello, World!\",
    the content_hash would be the MD5 hash of the string \"Hello, World!file.txt\"
    Do not include the file's path when calculating the content hash.

    Args:
        body (PostV1ImportsFilesCalculateContentHashBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
