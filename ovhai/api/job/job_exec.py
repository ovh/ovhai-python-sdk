from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...ovhai_types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    command: List[str],
    stderr: Union[Unset, bool] = True,
    stdout: Union[Unset, bool] = True,
    stdin: Union[Unset, bool] = False,
    tty: Union[Unset, bool] = False,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_command = command

    params["command"] = json_command

    params["stderr"] = stderr

    params["stdout"] = stdout

    params["stdin"] = stdin

    params["tty"] = tty

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v1/job/{id}/exec",
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
    command: List[str],
    stderr: Union[Unset, bool] = True,
    stdout: Union[Unset, bool] = True,
    stdin: Union[Unset, bool] = False,
    tty: Union[Unset, bool] = False,
) -> Response[Any]:
    """Execute a command inside the job

    Args:
        id (str):
        command (List[str]): command is the remote command to execute, not executed within a shell
        stderr (Union[Unset, bool]): redirect the standard error stream of the job for this call
            Default: True.
        stdout (Union[Unset, bool]): redirect the standard output stream of the job for this call
            Default: True.
        stdin (Union[Unset, bool]): redirect the standard input stream of the job for this call
            Default: False.
        tty (Union[Unset, bool]): TTY if true indicates that a tty will be allocated for the exec
            call, client need to upgrade to websocket Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        command=command,
        stderr=stderr,
        stdout=stdout,
        stdin=stdin,
        tty=tty,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    command: List[str],
    stderr: Union[Unset, bool] = True,
    stdout: Union[Unset, bool] = True,
    stdin: Union[Unset, bool] = False,
    tty: Union[Unset, bool] = False,
) -> Response[Any]:
    """Execute a command inside the job

    Args:
        id (str):
        command (List[str]): command is the remote command to execute, not executed within a shell
        stderr (Union[Unset, bool]): redirect the standard error stream of the job for this call
            Default: True.
        stdout (Union[Unset, bool]): redirect the standard output stream of the job for this call
            Default: True.
        stdin (Union[Unset, bool]): redirect the standard input stream of the job for this call
            Default: False.
        tty (Union[Unset, bool]): TTY if true indicates that a tty will be allocated for the exec
            call, client need to upgrade to websocket Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        command=command,
        stderr=stderr,
        stdout=stdout,
        stdin=stdin,
        tty=tty,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
