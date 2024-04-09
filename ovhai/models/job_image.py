from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..ovhai_types import UNSET, Unset

T = TypeVar("T", bound="JobImage")


@_attrs_define
class JobImage:
    """
    Attributes:
        description (Union[Unset, str]):
        doc_url (Union[Unset, str]):
        id (Union[Unset, str]):
        logo_url (Union[Unset, str]):
        name (Union[Unset, str]):
        versions (Union[Unset, List[str]]):
    """

    description: Union[Unset, str] = UNSET
    doc_url: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    logo_url: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    versions: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        doc_url = self.doc_url

        id = self.id

        logo_url = self.logo_url

        name = self.name

        versions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.versions, Unset):
            versions = self.versions

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
        if versions is not UNSET:
            field_dict["versions"] = versions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        doc_url = d.pop("docUrl", UNSET)

        id = d.pop("id", UNSET)

        logo_url = d.pop("logoUrl", UNSET)

        name = d.pop("name", UNSET)

        versions = cast(List[str], d.pop("versions", UNSET))

        job_image = cls(
            description=description,
            doc_url=doc_url,
            id=id,
            logo_url=logo_url,
            name=name,
            versions=versions,
        )

        job_image.additional_properties = d
        return job_image

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
