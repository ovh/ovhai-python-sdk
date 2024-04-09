from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_list import AppList
from ...models.order import Order
from ...ovhai_types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: Union[None, Unset, int] = UNSET,
    size: Union[None, Unset, int] = UNSET,
    order: Union[Unset, Order] = UNSET,
    sort: Union[None, Unset, str] = UNSET,
    updated_after: Union[None, Unset, int] = UNSET,
    updated_before: Union[None, Unset, int] = UNSET,
    status_state: Union[Unset, List[str]] = UNSET,
    read_lock: Union[Unset, bool] = UNSET,
    label_selector: Union[None, Unset, str] = UNSET,
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

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value if order else None

    params["order"] = json_order

    json_sort: Union[None, Unset, str]
    if isinstance(sort, Unset):
        json_sort = UNSET
    else:
        json_sort = sort
    params["sort"] = json_sort

    json_updated_after: Union[None, Unset, int]
    if isinstance(updated_after, Unset):
        json_updated_after = UNSET
    else:
        json_updated_after = updated_after
    params["updatedAfter"] = json_updated_after

    json_updated_before: Union[None, Unset, int]
    if isinstance(updated_before, Unset):
        json_updated_before = UNSET
    else:
        json_updated_before = updated_before
    params["updatedBefore"] = json_updated_before

    json_status_state: Union[Unset, List[str]] = UNSET
    if not isinstance(status_state, Unset):
        json_status_state = status_state

    params["statusState"] = json_status_state

    params["ReadLock"] = read_lock

    json_label_selector: Union[None, Unset, str]
    if isinstance(label_selector, Unset):
        json_label_selector = UNSET
    else:
        json_label_selector = label_selector
    params["labelSelector"] = json_label_selector

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/app",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, AppList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AppList.from_dict(response.json())

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
) -> Response[Union[Any, AppList]]:
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
    order: Union[Unset, Order] = UNSET,
    sort: Union[None, Unset, str] = UNSET,
    updated_after: Union[None, Unset, int] = UNSET,
    updated_before: Union[None, Unset, int] = UNSET,
    status_state: Union[Unset, List[str]] = UNSET,
    read_lock: Union[Unset, bool] = UNSET,
    label_selector: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, AppList]]:
    """Paginated list of apps

    Args:
        page (Union[None, Unset, int]): page index in the result set
        size (Union[None, Unset, int]): page size
        order (Union[Unset, Order]):
        sort (Union[None, Unset, str]): sort the result set with field Example: status.state.
        updated_after (Union[None, Unset, int]): unix timestamp to filter results updated after
        updated_before (Union[None, Unset, int]): unix timestamp to filter results updated before
        status_state (Union[Unset, List[str]]): status to filter
        read_lock (Union[Unset, bool]):
        label_selector (Union[None, Unset, str]): Label selector used to filter (e.g.
            'app_name=kind_of_magic')

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AppList]]
    """

    kwargs = _get_kwargs(
        page=page,
        size=size,
        order=order,
        sort=sort,
        updated_after=updated_after,
        updated_before=updated_before,
        status_state=status_state,
        read_lock=read_lock,
        label_selector=label_selector,
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
    order: Union[Unset, Order] = UNSET,
    sort: Union[None, Unset, str] = UNSET,
    updated_after: Union[None, Unset, int] = UNSET,
    updated_before: Union[None, Unset, int] = UNSET,
    status_state: Union[Unset, List[str]] = UNSET,
    read_lock: Union[Unset, bool] = UNSET,
    label_selector: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, AppList]]:
    """Paginated list of apps

    Args:
        page (Union[None, Unset, int]): page index in the result set
        size (Union[None, Unset, int]): page size
        order (Union[Unset, Order]):
        sort (Union[None, Unset, str]): sort the result set with field Example: status.state.
        updated_after (Union[None, Unset, int]): unix timestamp to filter results updated after
        updated_before (Union[None, Unset, int]): unix timestamp to filter results updated before
        status_state (Union[Unset, List[str]]): status to filter
        read_lock (Union[Unset, bool]):
        label_selector (Union[None, Unset, str]): Label selector used to filter (e.g.
            'app_name=kind_of_magic')

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, AppList]
    """

    return sync_detailed(
        client=client,
        page=page,
        size=size,
        order=order,
        sort=sort,
        updated_after=updated_after,
        updated_before=updated_before,
        status_state=status_state,
        read_lock=read_lock,
        label_selector=label_selector,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[None, Unset, int] = UNSET,
    size: Union[None, Unset, int] = UNSET,
    order: Union[Unset, Order] = UNSET,
    sort: Union[None, Unset, str] = UNSET,
    updated_after: Union[None, Unset, int] = UNSET,
    updated_before: Union[None, Unset, int] = UNSET,
    status_state: Union[Unset, List[str]] = UNSET,
    read_lock: Union[Unset, bool] = UNSET,
    label_selector: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, AppList]]:
    """Paginated list of apps

    Args:
        page (Union[None, Unset, int]): page index in the result set
        size (Union[None, Unset, int]): page size
        order (Union[Unset, Order]):
        sort (Union[None, Unset, str]): sort the result set with field Example: status.state.
        updated_after (Union[None, Unset, int]): unix timestamp to filter results updated after
        updated_before (Union[None, Unset, int]): unix timestamp to filter results updated before
        status_state (Union[Unset, List[str]]): status to filter
        read_lock (Union[Unset, bool]):
        label_selector (Union[None, Unset, str]): Label selector used to filter (e.g.
            'app_name=kind_of_magic')

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AppList]]
    """

    kwargs = _get_kwargs(
        page=page,
        size=size,
        order=order,
        sort=sort,
        updated_after=updated_after,
        updated_before=updated_before,
        status_state=status_state,
        read_lock=read_lock,
        label_selector=label_selector,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[None, Unset, int] = UNSET,
    size: Union[None, Unset, int] = UNSET,
    order: Union[Unset, Order] = UNSET,
    sort: Union[None, Unset, str] = UNSET,
    updated_after: Union[None, Unset, int] = UNSET,
    updated_before: Union[None, Unset, int] = UNSET,
    status_state: Union[Unset, List[str]] = UNSET,
    read_lock: Union[Unset, bool] = UNSET,
    label_selector: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, AppList]]:
    """Paginated list of apps

    Args:
        page (Union[None, Unset, int]): page index in the result set
        size (Union[None, Unset, int]): page size
        order (Union[Unset, Order]):
        sort (Union[None, Unset, str]): sort the result set with field Example: status.state.
        updated_after (Union[None, Unset, int]): unix timestamp to filter results updated after
        updated_before (Union[None, Unset, int]): unix timestamp to filter results updated before
        status_state (Union[Unset, List[str]]): status to filter
        read_lock (Union[Unset, bool]):
        label_selector (Union[None, Unset, str]): Label selector used to filter (e.g.
            'app_name=kind_of_magic')

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, AppList]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            size=size,
            order=order,
            sort=sort,
            updated_after=updated_after,
            updated_before=updated_before,
            status_state=status_state,
            read_lock=read_lock,
            label_selector=label_selector,
        )
    ).parsed
