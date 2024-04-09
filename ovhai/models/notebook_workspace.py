from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..ovhai_types import UNSET, Unset

T = TypeVar("T", bound="NotebookWorkspace")


@_attrs_define
class NotebookWorkspace:
    """
    Attributes:
        storage_free (Union[Unset, int]):
        storage_used (Union[Unset, int]):
    """

    storage_free: Union[Unset, int] = UNSET
    storage_used: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        storage_free = self.storage_free

        storage_used = self.storage_used

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if storage_free is not UNSET:
            field_dict["storageFree"] = storage_free
        if storage_used is not UNSET:
            field_dict["storageUsed"] = storage_used

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        storage_free = d.pop("storageFree", UNSET)

        storage_used = d.pop("storageUsed", UNSET)

        notebook_workspace = cls(
            storage_free=storage_free,
            storage_used=storage_used,
        )

        notebook_workspace.additional_properties = d
        return notebook_workspace

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
