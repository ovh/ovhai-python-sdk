import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..ovhai_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contract_terms_of_service import ContractTermsOfService


T = TypeVar("T", bound="Contract")


@_attrs_define
class Contract:
    """
    Attributes:
        created_at (Union[Unset, datetime.datetime]):
        id (Union[Unset, str]):
        signed_at (Union[None, Unset, datetime.datetime]):
        terms_of_service (Union[Unset, ContractTermsOfService]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    signed_at: Union[None, Unset, datetime.datetime] = UNSET
    terms_of_service: Union[Unset, "ContractTermsOfService"] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        id = self.id

        signed_at: Union[None, Unset, str]
        if isinstance(self.signed_at, Unset):
            signed_at = UNSET
        elif isinstance(self.signed_at, datetime.datetime):
            signed_at = self.signed_at.isoformat()
        else:
            signed_at = self.signed_at

        terms_of_service: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.terms_of_service, Unset):
            terms_of_service = self.terms_of_service.to_dict()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if signed_at is not UNSET:
            field_dict["signedAt"] = signed_at
        if terms_of_service is not UNSET:
            field_dict["termsOfService"] = terms_of_service
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.contract_terms_of_service import ContractTermsOfService

        d = src_dict.copy()
        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        id = d.pop("id", UNSET)

        def _parse_signed_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                signed_at_type_0 = isoparse(data)

                return signed_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        signed_at = _parse_signed_at(d.pop("signedAt", UNSET))

        _terms_of_service = d.pop("termsOfService", UNSET)
        terms_of_service: Union[Unset, ContractTermsOfService]
        if isinstance(_terms_of_service, Unset):
            terms_of_service = UNSET
        else:
            terms_of_service = ContractTermsOfService.from_dict(_terms_of_service)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        contract = cls(
            created_at=created_at,
            id=id,
            signed_at=signed_at,
            terms_of_service=terms_of_service,
            updated_at=updated_at,
        )

        contract.additional_properties = d
        return contract

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
