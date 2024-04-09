from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.notebook_framework import NotebookFramework
from ...ovhai_types import UNSET, Response, Unset


def _get_kwargs(
    *,
    compatible_with_editor: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["compatibleWithEditor"] = compatible_with_editor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/capabilities/notebook/framework",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["NotebookFramework"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = NotebookFramework.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["NotebookFramework"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    compatible_with_editor: Union[Unset, str] = UNSET,
) -> Response[List["NotebookFramework"]]:
    """List notebook frameworks for the current region

    Args:
        compatible_with_editor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['NotebookFramework']]
    """

    kwargs = _get_kwargs(
        compatible_with_editor=compatible_with_editor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    compatible_with_editor: Union[Unset, str] = UNSET,
) -> Optional[List["NotebookFramework"]]:
    """List notebook frameworks for the current region

    Args:
        compatible_with_editor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['NotebookFramework']
    """

    return sync_detailed(
        client=client,
        compatible_with_editor=compatible_with_editor,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    compatible_with_editor: Union[Unset, str] = UNSET,
) -> Response[List["NotebookFramework"]]:
    """List notebook frameworks for the current region

    Args:
        compatible_with_editor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['NotebookFramework']]
    """

    kwargs = _get_kwargs(
        compatible_with_editor=compatible_with_editor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    compatible_with_editor: Union[Unset, str] = UNSET,
) -> Optional[List["NotebookFramework"]]:
    """List notebook frameworks for the current region

    Args:
        compatible_with_editor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['NotebookFramework']
    """

    return (
        await asyncio_detailed(
            client=client,
            compatible_with_editor=compatible_with_editor,
        )
    ).parsed
