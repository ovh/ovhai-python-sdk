import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..ovhai_types import UNSET, Unset

T = TypeVar("T", bound="NotebookBackup")


@_attrs_define
class NotebookBackup:
    """
    Attributes:
        backup_date (Union[Unset, datetime.datetime]):
        comment (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        id (Union[Unset, str]):
        mount_path (Union[Unset, str]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    backup_date: Union[Unset, datetime.datetime] = UNSET
    comment: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    mount_path: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        backup_date: Union[Unset, str] = UNSET
        if not isinstance(self.backup_date, Unset):
            backup_date = self.backup_date.isoformat()

        comment = self.comment

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        id = self.id

        mount_path = self.mount_path

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_date is not UNSET:
            field_dict["backupDate"] = backup_date
        if comment is not UNSET:
            field_dict["comment"] = comment
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if mount_path is not UNSET:
            field_dict["mountPath"] = mount_path
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _backup_date = d.pop("backupDate", UNSET)
        backup_date: Union[Unset, datetime.datetime]
        if isinstance(_backup_date, Unset):
            backup_date = UNSET
        else:
            backup_date = isoparse(_backup_date)

        comment = d.pop("comment", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        id = d.pop("id", UNSET)

        mount_path = d.pop("mountPath", UNSET)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        notebook_backup = cls(
            backup_date=backup_date,
            comment=comment,
            created_at=created_at,
            id=id,
            mount_path=mount_path,
            updated_at=updated_at,
        )

        notebook_backup.additional_properties = d
        return notebook_backup

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
