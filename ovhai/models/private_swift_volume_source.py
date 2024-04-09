from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..ovhai_types import UNSET, Unset

T = TypeVar("T", bound="PrivateSwiftVolumeSource")


@_attrs_define
class PrivateSwiftVolumeSource:
    """
    Attributes:
        container (str): container (deprecated: use dataStore.container instead) Example: container.
        region (str): OVHcloud Object Storage region (deprecated: use dataStore.alias instead) Example: GRA.
        archive (Union[Unset, str]): name of the archive that needs to be save (deprecated: use dataStore.archive
            instead) Example: archive.tar.
        internal (Union[Unset, bool]): True if data is stored on OVHcloud AI's internal storage (deprecated: use
            dataStore.internal instead)
        prefix (Union[Unset, str]): Only objects matching the prefix are uploaded to the file system (deprecated: use
            dataStore.prefix instead)
    """

    container: str
    region: str
    archive: Union[Unset, str] = UNSET
    internal: Union[Unset, bool] = UNSET
    prefix: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        container = self.container

        region = self.region

        archive = self.archive

        internal = self.internal

        prefix = self.prefix

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "container": container,
                "region": region,
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
        container = d.pop("container")

        region = d.pop("region")

        archive = d.pop("archive", UNSET)

        internal = d.pop("internal", UNSET)

        prefix = d.pop("prefix", UNSET)

        private_swift_volume_source = cls(
            container=container,
            region=region,
            archive=archive,
            internal=internal,
            prefix=prefix,
        )

        private_swift_volume_source.additional_properties = d
        return private_swift_volume_source

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
