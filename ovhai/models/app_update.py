from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..ovhai_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_deployment_strategy import AppDeploymentStrategy


T = TypeVar("T", bound="AppUpdate")


@_attrs_define
class AppUpdate:
    """
    Attributes:
        default_http_port (Union[None, Unset, int]): Number of the port to access
        deployment_strategy (Union[Unset, AppDeploymentStrategy]):
        grpc_port (Union[None, Unset, int]): GRPC Port that we want to expose in case workload HTTP & gRPC servers
            cannot be multiplexed to listen on the same port Example: 8081.
        url (Union[None, Unset, str]): URL of the new Docker image
    """

    default_http_port: Union[None, Unset, int] = UNSET
    deployment_strategy: Union[Unset, "AppDeploymentStrategy"] = UNSET
    grpc_port: Union[None, Unset, int] = UNSET
    url: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        default_http_port: Union[None, Unset, int]
        if isinstance(self.default_http_port, Unset):
            default_http_port = UNSET
        else:
            default_http_port = self.default_http_port

        deployment_strategy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.deployment_strategy, Unset):
            deployment_strategy = self.deployment_strategy.to_dict()

        grpc_port: Union[None, Unset, int]
        if isinstance(self.grpc_port, Unset):
            grpc_port = UNSET
        else:
            grpc_port = self.grpc_port

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_http_port is not UNSET:
            field_dict["defaultHttpPort"] = default_http_port
        if deployment_strategy is not UNSET:
            field_dict["deploymentStrategy"] = deployment_strategy
        if grpc_port is not UNSET:
            field_dict["grpcPort"] = grpc_port
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.app_deployment_strategy import AppDeploymentStrategy

        d = src_dict.copy()

        def _parse_default_http_port(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        default_http_port = _parse_default_http_port(d.pop("defaultHttpPort", UNSET))

        _deployment_strategy = d.pop("deploymentStrategy", UNSET)
        deployment_strategy: Union[Unset, AppDeploymentStrategy]
        if isinstance(_deployment_strategy, Unset):
            deployment_strategy = UNSET
        else:
            deployment_strategy = AppDeploymentStrategy.from_dict(_deployment_strategy)

        def _parse_grpc_port(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        grpc_port = _parse_grpc_port(d.pop("grpcPort", UNSET))

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))

        app_update = cls(
            default_http_port=default_http_port,
            deployment_strategy=deployment_strategy,
            grpc_port=grpc_port,
            url=url,
        )

        app_update.additional_properties = d
        return app_update

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
