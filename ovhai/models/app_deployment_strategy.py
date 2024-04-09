from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..ovhai_types import UNSET, Unset

T = TypeVar("T", bound="AppDeploymentStrategy")


@_attrs_define
class AppDeploymentStrategy:
    """
    Attributes:
        max_surge (Union[None, Unset, str]): specifies the maximum number of replicas that can be created over the
            desired number of Pods Default: '25%'.
        max_unavailable (Union[None, Unset, str]): specifies the maximum number of replicas that can be unavailable
            during the update process Default: '25%'.
        progress_deadline_seconds (Union[None, Unset, int]): specifies the number of seconds you want to wait for your
            Deployment to progress before the system reports back that the Deployment has failed progressing Default: 600.
    """

    max_surge: Union[None, Unset, str] = "25%"
    max_unavailable: Union[None, Unset, str] = "25%"
    progress_deadline_seconds: Union[None, Unset, int] = 600
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_surge: Union[None, Unset, str]
        if isinstance(self.max_surge, Unset):
            max_surge = UNSET
        else:
            max_surge = self.max_surge

        max_unavailable: Union[None, Unset, str]
        if isinstance(self.max_unavailable, Unset):
            max_unavailable = UNSET
        else:
            max_unavailable = self.max_unavailable

        progress_deadline_seconds: Union[None, Unset, int]
        if isinstance(self.progress_deadline_seconds, Unset):
            progress_deadline_seconds = UNSET
        else:
            progress_deadline_seconds = self.progress_deadline_seconds

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_surge is not UNSET:
            field_dict["maxSurge"] = max_surge
        if max_unavailable is not UNSET:
            field_dict["maxUnavailable"] = max_unavailable
        if progress_deadline_seconds is not UNSET:
            field_dict["progressDeadlineSeconds"] = progress_deadline_seconds

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_max_surge(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        max_surge = _parse_max_surge(d.pop("maxSurge", UNSET))

        def _parse_max_unavailable(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        max_unavailable = _parse_max_unavailable(d.pop("maxUnavailable", UNSET))

        def _parse_progress_deadline_seconds(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        progress_deadline_seconds = _parse_progress_deadline_seconds(d.pop("progressDeadlineSeconds", UNSET))

        app_deployment_strategy = cls(
            max_surge=max_surge,
            max_unavailable=max_unavailable,
            progress_deadline_seconds=progress_deadline_seconds,
        )

        app_deployment_strategy.additional_properties = d
        return app_deployment_strategy

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
