from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..ovhai_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.preset_resources import PresetResources


T = TypeVar("T", bound="PresetCapabilities")


@_attrs_define
class PresetCapabilities:
    """
    Attributes:
        exec_ (Union[Unset, bool]):
        flavor_types (Union[Unset, List[str]]):
        log (Union[Unset, bool]):
        resources (Union[Unset, PresetResources]):
        ssh (Union[Unset, bool]):
        volume (Union[Unset, bool]):
    """

    exec_: Union[Unset, bool] = UNSET
    flavor_types: Union[Unset, List[str]] = UNSET
    log: Union[Unset, bool] = UNSET
    resources: Union[Unset, "PresetResources"] = UNSET
    ssh: Union[Unset, bool] = UNSET
    volume: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        exec_ = self.exec_

        flavor_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.flavor_types, Unset):
            flavor_types = self.flavor_types

        log = self.log

        resources: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.resources, Unset):
            resources = self.resources.to_dict()

        ssh = self.ssh

        volume = self.volume

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exec_ is not UNSET:
            field_dict["exec"] = exec_
        if flavor_types is not UNSET:
            field_dict["flavorTypes"] = flavor_types
        if log is not UNSET:
            field_dict["log"] = log
        if resources is not UNSET:
            field_dict["resources"] = resources
        if ssh is not UNSET:
            field_dict["ssh"] = ssh
        if volume is not UNSET:
            field_dict["volume"] = volume

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.preset_resources import PresetResources

        d = src_dict.copy()
        exec_ = d.pop("exec", UNSET)

        flavor_types = cast(List[str], d.pop("flavorTypes", UNSET))

        log = d.pop("log", UNSET)

        _resources = d.pop("resources", UNSET)
        resources: Union[Unset, PresetResources]
        if isinstance(_resources, Unset):
            resources = UNSET
        else:
            resources = PresetResources.from_dict(_resources)

        ssh = d.pop("ssh", UNSET)

        volume = d.pop("volume", UNSET)

        preset_capabilities = cls(
            exec_=exec_,
            flavor_types=flavor_types,
            log=log,
            resources=resources,
            ssh=ssh,
            volume=volume,
        )

        preset_capabilities.additional_properties = d
        return preset_capabilities

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
