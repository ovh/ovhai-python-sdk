from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..ovhai_types import UNSET, Unset

T = TypeVar("T", bound="DataStoreVolumeSource")


@_attrs_define
class DataStoreVolumeSource:
    """
    Attributes:
        alias (str): Data store alias Example: GRA.
        container (str):  Example: container.
        archive (Union[Unset, str]): name of the archive that needs to be save Example: archive.tar.
        internal (Union[Unset, bool]): True if data is stored on OVHcloud AI's internal storage
        prefix (Union[Unset, str]): Only objects matching the prefix are uploaded to the file system
    """

    alias: str
    container: str
    archive: Union[Unset, str] = UNSET
    internal: Union[Unset, bool] = UNSET
    prefix: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alias = self.alias

        container = self.container

        archive = self.archive

        internal = self.internal

        prefix = self.prefix

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alias": alias,
                "container": container,
            }
        )
        if archive is not UNSET:
            field_dict["archive"] = archive
        if internal is not UNSET:
            field_dict["internal"] = internal
        if prefix is not UNSET:
            field_dict["prefix"] = prefix

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        alias = d.pop("alias")

        container = d.pop("container")

        archive = d.pop("archive", UNSET)

        internal = d.pop("internal", UNSET)

        prefix = d.pop("prefix", UNSET)

        data_store_volume_source = cls(
            alias=alias,
            container=container,
            archive=archive,
            internal=internal,
            prefix=prefix,
        )

        data_store_volume_source.additional_properties = d
        return data_store_volume_source

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
