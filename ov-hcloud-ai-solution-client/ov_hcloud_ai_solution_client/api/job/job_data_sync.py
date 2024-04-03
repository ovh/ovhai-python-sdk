from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_sync import DataSync
from ...models.data_sync_spec import DataSyncSpec
from ...types import Response


def _get_kwargs(
    job_id: str,
    *,
    body: DataSyncSpec,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/v1/job/{job_id}/datasync",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[DataSync]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DataSync.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[DataSync]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    job_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DataSyncSpec,
) -> Response[DataSync]:
    """Initiate a Data Synchronization on a running job

    Args:
        job_id (str):
        body (DataSyncSpec):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataSync]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DataSyncSpec,
) -> Optional[DataSync]:
    """Initiate a Data Synchronization on a running job

    Args:
        job_id (str):
        body (DataSyncSpec):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataSync
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DataSyncSpec,
) -> Response[DataSync]:
    """Initiate a Data Synchronization on a running job

    Args:
        job_id (str):
        body (DataSyncSpec):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataSync]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DataSyncSpec,
) -> Optional[DataSync]:
    """Initiate a Data Synchronization on a running job

    Args:
        job_id (str):
        body (DataSyncSpec):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataSync
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
            body=body,
        )
    ).parsed
