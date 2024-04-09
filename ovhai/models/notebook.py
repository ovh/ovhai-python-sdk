import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..ovhai_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notebook_spec import NotebookSpec
    from ..models.notebook_status import NotebookStatus


T = TypeVar("T", bound="Notebook")


@_attrs_define
class Notebook:
    """
    Attributes:
        created_at (Union[Unset, datetime.datetime]):
        id (Union[Unset, str]):
        spec (Union[Unset, NotebookSpec]):
        status (Union[Unset, NotebookStatus]):
        updated_at (Union[Unset, datetime.datetime]):
        user (Union[Unset, str]): Public Cloud project username Example: user.
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    spec: Union[Unset, "NotebookSpec"] = UNSET
    status: Union[Unset, "NotebookStatus"] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    user: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        id = self.id

        spec: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        user = self.user

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if spec is not UNSET:
            field_dict["spec"] = spec
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.notebook_spec import NotebookSpec
        from ..models.notebook_status import NotebookStatus

        d = src_dict.copy()
        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        id = d.pop("id", UNSET)

        _spec = d.pop("spec", UNSET)
        spec: Union[Unset, NotebookSpec]
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = NotebookSpec.from_dict(_spec)

        _status = d.pop("status", UNSET)
        status: Union[Unset, NotebookStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = NotebookStatus.from_dict(_status)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        user = d.pop("user", UNSET)

        notebook = cls(
            created_at=created_at,
            id=id,
            spec=spec,
            status=status,
            updated_at=updated_at,
            user=user,
        )

        notebook.additional_properties = d
        return notebook

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
