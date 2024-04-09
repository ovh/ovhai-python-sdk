from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.image_version_list import ImageVersionList
from ...ovhai_types import Response


def _get_kwargs(
    image_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v1/image/{image_id}/version",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ImageVersionList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ImageVersionList.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ImageVersionList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    image_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, ImageVersionList]]:
    """List partner images version

    Args:
        image_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ImageVersionList]]
    """

    kwargs = _get_kwargs(
        image_id=image_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    image_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, ImageVersionList]]:
    """List partner images version

    Args:
        image_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ImageVersionList]
    """

    return sync_detailed(
        image_id=image_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    image_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, ImageVersionList]]:
    """List partner images version

    Args:
        image_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ImageVersionList]]
    """

    kwargs = _get_kwargs(
        image_id=image_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    image_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, ImageVersionList]]:
    """List partner images version

    Args:
        image_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ImageVersionList]
    """

    return (
        await asyncio_detailed(
            image_id=image_id,
            client=client,
        )
    ).parsed
