from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..ovhai_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gpu_information import GpuInformation
    from ..models.resources_per_unit import ResourcesPerUnit


T = TypeVar("T", bound="Flavor")


@_attrs_define
class Flavor:
    """
    Attributes:
        default (Union[Unset, bool]):
        description (Union[Unset, str]):
        gpu_information (Union[Unset, GpuInformation]):
        id (Union[Unset, str]):
        max_ (Union[Unset, int]):  Example: 4.
        resources_per_unit (Union[Unset, ResourcesPerUnit]):
        type (Union[Unset, str]):
    """

    default: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    gpu_information: Union[Unset, "GpuInformation"] = UNSET
    id: Union[Unset, str] = UNSET
    max_: Union[Unset, int] = UNSET
    resources_per_unit: Union[Unset, "ResourcesPerUnit"] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        default = self.default

        description = self.description

        gpu_information: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gpu_information, Unset):
            gpu_information = self.gpu_information.to_dict()

        id = self.id

        max_ = self.max_

        resources_per_unit: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.resources_per_unit, Unset):
            resources_per_unit = self.resources_per_unit.to_dict()

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default is not UNSET:
            field_dict["default"] = default
        if description is not UNSET:
            field_dict["description"] = description
        if gpu_information is not UNSET:
            field_dict["gpuInformation"] = gpu_information
        if id is not UNSET:
            field_dict["id"] = id
        if max_ is not UNSET:
            field_dict["max"] = max_
        if resources_per_unit is not UNSET:
            field_dict["resourcesPerUnit"] = resources_per_unit
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.gpu_information import GpuInformation
        from ..models.resources_per_unit import ResourcesPerUnit

        d = src_dict.copy()
        default = d.pop("default", UNSET)

        description = d.pop("description", UNSET)

        _gpu_information = d.pop("gpuInformation", UNSET)
        gpu_information: Union[Unset, GpuInformation]
        if isinstance(_gpu_information, Unset):
            gpu_information = UNSET
        else:
            gpu_information = GpuInformation.from_dict(_gpu_information)

        id = d.pop("id", UNSET)

        max_ = d.pop("max", UNSET)

        _resources_per_unit = d.pop("resourcesPerUnit", UNSET)
        resources_per_unit: Union[Unset, ResourcesPerUnit]
        if isinstance(_resources_per_unit, Unset):
            resources_per_unit = UNSET
        else:
            resources_per_unit = ResourcesPerUnit.from_dict(_resources_per_unit)

        type = d.pop("type", UNSET)

        flavor = cls(
            default=default,
            description=description,
            gpu_information=gpu_information,
            id=id,
            max_=max_,
            resources_per_unit=resources_per_unit,
            type=type,
        )

        flavor.additional_properties = d
        return flavor

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
