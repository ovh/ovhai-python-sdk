from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.terms_of_service_locale import TermsOfServiceLocale


T = TypeVar("T", bound="ContractTermsOfService")


@_attrs_define
class ContractTermsOfService:
    """ """

    additional_properties: Dict[str, "TermsOfServiceLocale"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.terms_of_service_locale import TermsOfServiceLocale

        d = src_dict.copy()
        contract_terms_of_service = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = TermsOfServiceLocale.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        contract_terms_of_service.additional_properties = additional_properties
        return contract_terms_of_service

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "TermsOfServiceLocale":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "TermsOfServiceLocale") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
