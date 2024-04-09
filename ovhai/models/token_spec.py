from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..ovhai_types import UNSET, Unset

T = TypeVar("T", bound="TokenSpec")


@_attrs_define
class TokenSpec:
    """
    Attributes:
        name (str):  Example: app-token.
        role (str):
        label_selector (Union[Unset, str]): Label selector used to filter resource for the token
    """

    name: str
    role: str
    label_selector: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        role = self.role

        label_selector = self.label_selector

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "role": role,
            }
        )
        if label_selector is not UNSET:
            field_dict["labelSelector"] = label_selector

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        role = d.pop("role")

        label_selector = d.pop("labelSelector", UNSET)

        token_spec = cls(
            name=name,
            role=role,
            label_selector=label_selector,
        )

        token_spec.additional_properties = d
        return token_spec

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
