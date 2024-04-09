from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.token_list import TokenList
from ...ovhai_types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: Union[None, Unset, int] = UNSET,
    size: Union[None, Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_page: Union[None, Unset, int]
    if isinstance(page, Unset):
        json_page = UNSET
    else:
        json_page = page
    params["page"] = json_page

    json_size: Union[None, Unset, int]
    if isinstance(size, Unset):
        json_size = UNSET
    else:
        json_size = size
    params["size"] = json_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/token",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[TokenList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TokenList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[TokenList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[None, Unset, int] = UNSET,
    size: Union[None, Unset, int] = UNSET,
) -> Response[TokenList]:
    """Paginated list of AI access tokens

    Args:
        page (Union[None, Unset, int]): page index in the result set
        size (Union[None, Unset, int]): page size

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TokenList]
    """

    kwargs = _get_kwargs(
        page=page,
        size=size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[None, Unset, int] = UNSET,
    size: Union[None, Unset, int] = UNSET,
) -> Optional[TokenList]:
    """Paginated list of AI access tokens

    Args:
        page (Union[None, Unset, int]): page index in the result set
        size (Union[None, Unset, int]): page size

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TokenList
    """

    return sync_detailed(
        client=client,
        page=page,
        size=size,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[None, Unset, int] = UNSET,
    size: Union[None, Unset, int] = UNSET,
) -> Response[TokenList]:
    """Paginated list of AI access tokens

    Args:
        page (Union[None, Unset, int]): page index in the result set
        size (Union[None, Unset, int]): page size

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TokenList]
    """

    kwargs = _get_kwargs(
        page=page,
        size=size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[None, Unset, int] = UNSET,
    size: Union[None, Unset, int] = UNSET,
) -> Optional[TokenList]:
    """Paginated list of AI access tokens

    Args:
        page (Union[None, Unset, int]): page index in the result set
        size (Union[None, Unset, int]): page size

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TokenList
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            size=size,
        )
    ).parsed
