import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..ovhai_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contract import Contract


T = TypeVar("T", bound="Partner")


@_attrs_define
class Partner:
    """
    Attributes:
        contract (Union[Unset, Contract]):
        created_at (Union[Unset, datetime.datetime]):
        description (Union[Unset, str]):
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        project_uuid (Union[Unset, str]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    contract: Union[Unset, "Contract"] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    project_uuid: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contract: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contract, Unset):
            contract = self.contract.to_dict()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        description = self.description

        id = self.id

        name = self.name

        project_uuid = self.project_uuid

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contract is not UNSET:
            field_dict["contract"] = contract
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if project_uuid is not UNSET:
            field_dict["projectUuid"] = project_uuid
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.contract import Contract

        d = src_dict.copy()
        _contract = d.pop("contract", UNSET)
        contract: Union[Unset, Contract]
        if isinstance(_contract, Unset):
            contract = UNSET
        else:
            contract = Contract.from_dict(_contract)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        project_uuid = d.pop("projectUuid", UNSET)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        partner = cls(
            contract=contract,
            created_at=created_at,
            description=description,
            id=id,
            name=name,
            project_uuid=project_uuid,
            updated_at=updated_at,
        )

        partner.additional_properties = d
        return partner

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
