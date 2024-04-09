from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..ovhai_types import UNSET, Unset

T = TypeVar("T", bound="Framework")


@_attrs_define
class Framework:
    """
    Attributes:
        description (Union[Unset, str]):
        doc_url (Union[None, Unset, str]):
        id (Union[Unset, str]):
        logo_url (Union[None, Unset, str]):
        name (Union[Unset, str]):
        partner_id (Union[Unset, str]):
        saved_paths (Union[Unset, List[str]]):
    """

    description: Union[Unset, str] = UNSET
    doc_url: Union[None, Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    logo_url: Union[None, Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    partner_id: Union[Unset, str] = UNSET
    saved_paths: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        doc_url: Union[None, Unset, str]
        if isinstance(self.doc_url, Unset):
            doc_url = UNSET
        else:
            doc_url = self.doc_url

        id = self.id

        logo_url: Union[None, Unset, str]
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        name = self.name

        partner_id = self.partner_id

        saved_paths: Union[Unset, List[str]] = UNSET
        if not isinstance(self.saved_paths, Unset):
            saved_paths = self.saved_paths

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if doc_url is not UNSET:
            field_dict["docUrl"] = doc_url
        if id is not UNSET:
            field_dict["id"] = id
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if name is not UNSET:
            field_dict["name"] = name
        if partner_id is not UNSET:
            field_dict["partnerId"] = partner_id
        if saved_paths is not UNSET:
            field_dict["savedPaths"] = saved_paths

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        def _parse_doc_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        doc_url = _parse_doc_url(d.pop("docUrl", UNSET))

        id = d.pop("id", UNSET)

        def _parse_logo_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        logo_url = _parse_logo_url(d.pop("logoUrl", UNSET))

        name = d.pop("name", UNSET)

        partner_id = d.pop("partnerId", UNSET)

        saved_paths = cast(List[str], d.pop("savedPaths", UNSET))

        framework = cls(
            description=description,
            doc_url=doc_url,
            id=id,
            logo_url=logo_url,
            name=name,
            partner_id=partner_id,
            saved_paths=saved_paths,
        )

        framework.additional_properties = d
        return framework

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
