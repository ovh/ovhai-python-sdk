from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.notebook import Notebook
from ...ovhai_types import Response


def _get_kwargs(
    id: str,
    backup_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/v1/notebook/{id}/backup/{backup_id}/fork",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Notebook]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Notebook.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.PAYMENT_REQUIRED:
        response_402 = cast(Any, None)
        return response_402
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, Notebook]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    backup_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, Notebook]]:
    """Create notebook from existing backup

    Args:
        id (str):
        backup_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Notebook]]
    """

    kwargs = _get_kwargs(
        id=id,
        backup_id=backup_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    backup_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, Notebook]]:
    """Create notebook from existing backup

    Args:
        id (str):
        backup_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Notebook]
    """

    return sync_detailed(
        id=id,
        backup_id=backup_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    backup_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, Notebook]]:
    """Create notebook from existing backup

    Args:
        id (str):
        backup_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Notebook]]
    """

    kwargs = _get_kwargs(
        id=id,
        backup_id=backup_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    backup_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, Notebook]]:
    """Create notebook from existing backup

    Args:
        id (str):
        backup_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Notebook]
    """

    return (
        await asyncio_detailed(
            id=id,
            backup_id=backup_id,
            client=client,
        )
    ).parsed
