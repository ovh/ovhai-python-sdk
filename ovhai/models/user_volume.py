import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..ovhai_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_store_volume_source import DataStoreVolumeSource
    from ..models.private_swift_volume_source import PrivateSwiftVolumeSource
    from ..models.public_git_volume_source import PublicGitVolumeSource
    from ..models.public_swift_volume_source import PublicSwiftVolumeSource
    from ..models.standalone_volume_source import StandaloneVolumeSource


T = TypeVar("T", bound="UserVolume")


@_attrs_define
class UserVolume:
    """
    Attributes:
        cache (Union[Unset, bool]):
        created_at (Union[Unset, datetime.datetime]):
        data_store (Union[Unset, DataStoreVolumeSource]):
        id (Union[Unset, str]):
        private_swift (Union[Unset, PrivateSwiftVolumeSource]):
        public_git (Union[Unset, PublicGitVolumeSource]):
        public_swift (Union[Unset, PublicSwiftVolumeSource]):
        standalone (Union[Unset, StandaloneVolumeSource]):
        target_data_store (Union[Unset, DataStoreVolumeSource]):
        target_private_swift (Union[Unset, PrivateSwiftVolumeSource]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    cache: Union[Unset, bool] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    data_store: Union[Unset, "DataStoreVolumeSource"] = UNSET
    id: Union[Unset, str] = UNSET
    private_swift: Union[Unset, "PrivateSwiftVolumeSource"] = UNSET
    public_git: Union[Unset, "PublicGitVolumeSource"] = UNSET
    public_swift: Union[Unset, "PublicSwiftVolumeSource"] = UNSET
    standalone: Union[Unset, "StandaloneVolumeSource"] = UNSET
    target_data_store: Union[Unset, "DataStoreVolumeSource"] = UNSET
    target_private_swift: Union[Unset, "PrivateSwiftVolumeSource"] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cache = self.cache

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        data_store: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data_store, Unset):
            data_store = self.data_store.to_dict()

        id = self.id

        private_swift: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.private_swift, Unset):
            private_swift = self.private_swift.to_dict()

        public_git: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.public_git, Unset):
            public_git = self.public_git.to_dict()

        public_swift: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.public_swift, Unset):
            public_swift = self.public_swift.to_dict()

        standalone: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.standalone, Unset):
            standalone = self.standalone.to_dict()

        target_data_store: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.target_data_store, Unset):
            target_data_store = self.target_data_store.to_dict()

        target_private_swift: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.target_private_swift, Unset):
            target_private_swift = self.target_private_swift.to_dict()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cache is not UNSET:
            field_dict["cache"] = cache
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if data_store is not UNSET:
            field_dict["dataStore"] = data_store
        if id is not UNSET:
            field_dict["id"] = id
        if private_swift is not UNSET:
            field_dict["privateSwift"] = private_swift
        if public_git is not UNSET:
            field_dict["publicGit"] = public_git
        if public_swift is not UNSET:
            field_dict["publicSwift"] = public_swift
        if standalone is not UNSET:
            field_dict["standalone"] = standalone
        if target_data_store is not UNSET:
            field_dict["targetDataStore"] = target_data_store
        if target_private_swift is not UNSET:
            field_dict["targetPrivateSwift"] = target_private_swift
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_store_volume_source import DataStoreVolumeSource
        from ..models.private_swift_volume_source import PrivateSwiftVolumeSource
        from ..models.public_git_volume_source import PublicGitVolumeSource
        from ..models.public_swift_volume_source import PublicSwiftVolumeSource
        from ..models.standalone_volume_source import StandaloneVolumeSource

        d = src_dict.copy()
        cache = d.pop("cache", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _data_store = d.pop("dataStore", UNSET)
        data_store: Union[Unset, DataStoreVolumeSource]
        if isinstance(_data_store, Unset):
            data_store = UNSET
        else:
            data_store = DataStoreVolumeSource.from_dict(_data_store)

        id = d.pop("id", UNSET)

        _private_swift = d.pop("privateSwift", UNSET)
        private_swift: Union[Unset, PrivateSwiftVolumeSource]
        if isinstance(_private_swift, Unset):
            private_swift = UNSET
        else:
            private_swift = PrivateSwiftVolumeSource.from_dict(_private_swift)

        _public_git = d.pop("publicGit", UNSET)
        public_git: Union[Unset, PublicGitVolumeSource]
        if isinstance(_public_git, Unset):
            public_git = UNSET
        else:
            public_git = PublicGitVolumeSource.from_dict(_public_git)

        _public_swift = d.pop("publicSwift", UNSET)
        public_swift: Union[Unset, PublicSwiftVolumeSource]
        if isinstance(_public_swift, Unset):
            public_swift = UNSET
        else:
            public_swift = PublicSwiftVolumeSource.from_dict(_public_swift)

        _standalone = d.pop("standalone", UNSET)
        standalone: Union[Unset, StandaloneVolumeSource]
        if isinstance(_standalone, Unset):
            standalone = UNSET
        else:
            standalone = StandaloneVolumeSource.from_dict(_standalone)

        _target_data_store = d.pop("targetDataStore", UNSET)
        target_data_store: Union[Unset, DataStoreVolumeSource]
        if isinstance(_target_data_store, Unset):
            target_data_store = UNSET
        else:
            target_data_store = DataStoreVolumeSource.from_dict(_target_data_store)

        _target_private_swift = d.pop("targetPrivateSwift", UNSET)
        target_private_swift: Union[Unset, PrivateSwiftVolumeSource]
        if isinstance(_target_private_swift, Unset):
            target_private_swift = UNSET
        else:
            target_private_swift = PrivateSwiftVolumeSource.from_dict(_target_private_swift)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        user_volume = cls(
            cache=cache,
            created_at=created_at,
            data_store=data_store,
            id=id,
            private_swift=private_swift,
            public_git=public_git,
            public_swift=public_swift,
            standalone=standalone,
            target_data_store=target_data_store,
            target_private_swift=target_private_swift,
            updated_at=updated_at,
        )

        user_volume.additional_properties = d
        return user_volume

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
