from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...ovhai_types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    page: Union[Unset, int] = UNSET,
    size: Union[Unset, int] = UNSET,
    follow: Union[Unset, bool] = UNSET,
    tail: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["page"] = page

    params["size"] = size

    params["follow"] = follow

    params["tail"] = tail

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v1/job/{id}/log",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
        return None
    if response.status_code == HTTPStatus.NOT_FOUND:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = UNSET,
    size: Union[Unset, int] = UNSET,
    follow: Union[Unset, bool] = UNSET,
    tail: Union[Unset, int] = UNSET,
) -> Response[Any]:
    """Retrieve job logs

    Args:
        id (str):
        page (Union[Unset, int]):
        size (Union[Unset, int]):
        follow (Union[Unset, bool]):
        tail (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        page=page,
        size=size,
        follow=follow,
        tail=tail,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = UNSET,
    size: Union[Unset, int] = UNSET,
    follow: Union[Unset, bool] = UNSET,
    tail: Union[Unset, int] = UNSET,
) -> Response[Any]:
    """Retrieve job logs

    Args:
        id (str):
        page (Union[Unset, int]):
        size (Union[Unset, int]):
        follow (Union[Unset, bool]):
        tail (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        page=page,
        size=size,
        follow=follow,
        tail=tail,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
