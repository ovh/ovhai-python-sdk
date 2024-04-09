from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.licensing_type import LicensingType
from ..ovhai_types import UNSET, Unset

T = TypeVar("T", bound="PresetPartner")


@_attrs_define
class PresetPartner:
    """
    Attributes:
        flavor (Union[Unset, str]):
        id (Union[Unset, str]):
        licensing (Union[Unset, LicensingType]):
        name (Union[Unset, str]):
    """

    flavor: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    licensing: Union[Unset, LicensingType] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        flavor = self.flavor

        id = self.id

        licensing: Union[Unset, str] = UNSET
        if not isinstance(self.licensing, Unset):
            licensing = self.licensing.value

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if flavor is not UNSET:
            field_dict["flavor"] = flavor
        if id is not UNSET:
            field_dict["id"] = id
        if licensing is not UNSET:
            field_dict["licensing"] = licensing
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        flavor = d.pop("flavor", UNSET)

        id = d.pop("id", UNSET)

        _licensing = d.pop("licensing", UNSET)
        licensing: Union[Unset, LicensingType]
        if isinstance(_licensing, Unset):
            licensing = UNSET
        else:
            licensing = LicensingType(_licensing)

        name = d.pop("name", UNSET)

        preset_partner = cls(
            flavor=flavor,
            id=id,
            licensing=licensing,
            name=name,
        )

        preset_partner.additional_properties = d
        return preset_partner

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
