from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_image_version import CreateImageVersion
from ...models.image_version import ImageVersion
from ...ovhai_types import Response


def _get_kwargs(
    image_id: str,
    *,
    body: CreateImageVersion,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/v1/image/{image_id}/version",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ImageVersion]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ImageVersion.from_dict(response.json())

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
) -> Response[Union[Any, ImageVersion]]:
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
    body: CreateImageVersion,
) -> Response[Union[Any, ImageVersion]]:
    """Create partner image version and start its mirroring

    Args:
        image_id (str):
        body (CreateImageVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ImageVersion]]
    """

    kwargs = _get_kwargs(
        image_id=image_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    image_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateImageVersion,
) -> Optional[Union[Any, ImageVersion]]:
    """Create partner image version and start its mirroring

    Args:
        image_id (str):
        body (CreateImageVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ImageVersion]
    """

    return sync_detailed(
        image_id=image_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    image_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateImageVersion,
) -> Response[Union[Any, ImageVersion]]:
    """Create partner image version and start its mirroring

    Args:
        image_id (str):
        body (CreateImageVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ImageVersion]]
    """

    kwargs = _get_kwargs(
        image_id=image_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    image_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateImageVersion,
) -> Optional[Union[Any, ImageVersion]]:
    """Create partner image version and start its mirroring

    Args:
        image_id (str):
        body (CreateImageVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ImageVersion]
    """

    return (
        await asyncio_detailed(
            image_id=image_id,
            client=client,
            body=body,
        )
    ).parsed
