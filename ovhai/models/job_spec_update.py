from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..ovhai_types import UNSET, Unset

T = TypeVar("T", bound="JobSpecUpdate")


@_attrs_define
class JobSpecUpdate:
    """
    Attributes:
        timeout (Union[None, Unset, int]): Time in second after the job will shutdown automatically Default: 604800.
        timeout_auto_restart (Union[None, Unset, bool]): If set to true, the job will be rescheduled after a timeout
    """

    timeout: Union[None, Unset, int] = 604800
    timeout_auto_restart: Union[None, Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timeout: Union[None, Unset, int]
        if isinstance(self.timeout, Unset):
            timeout = UNSET
        else:
            timeout = self.timeout

        timeout_auto_restart: Union[None, Unset, bool]
        if isinstance(self.timeout_auto_restart, Unset):
            timeout_auto_restart = UNSET
        else:
            timeout_auto_restart = self.timeout_auto_restart

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if timeout_auto_restart is not UNSET:
            field_dict["timeoutAutoRestart"] = timeout_auto_restart

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_timeout(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        timeout = _parse_timeout(d.pop("timeout", UNSET))

        def _parse_timeout_auto_restart(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        timeout_auto_restart = _parse_timeout_auto_restart(d.pop("timeoutAutoRestart", UNSET))

        job_spec_update = cls(
            timeout=timeout,
            timeout_auto_restart=timeout_auto_restart,
        )

        job_spec_update.additional_properties = d
        return job_spec_update

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
