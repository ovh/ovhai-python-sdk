from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..ovhai_types import UNSET, Unset

T = TypeVar("T", bound="CreateFramework")


@_attrs_define
class CreateFramework:
    """
    Attributes:
        description (str): Framework description
        id (str): Framework ID
        name (str): Framework Name
        doc_url (Union[None, Unset, str]): Framework documentation URL
        logo_url (Union[None, Unset, str]): Framework logo URL
        saved_paths (Union[List[str], None, Unset]): Saved paths
    """

    description: str
    id: str
    name: str
    doc_url: Union[None, Unset, str] = UNSET
    logo_url: Union[None, Unset, str] = UNSET
    saved_paths: Union[List[str], None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        id = self.id

        name = self.name

        doc_url: Union[None, Unset, str]
        if isinstance(self.doc_url, Unset):
            doc_url = UNSET
        else:
            doc_url = self.doc_url

        logo_url: Union[None, Unset, str]
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        saved_paths: Union[List[str], None, Unset]
        if isinstance(self.saved_paths, Unset):
            saved_paths = UNSET
        elif isinstance(self.saved_paths, list):
            saved_paths = self.saved_paths

        else:
            saved_paths = self.saved_paths

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "id": id,
                "name": name,
            }
        )
        if doc_url is not UNSET:
            field_dict["docUrl"] = doc_url
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if saved_paths is not UNSET:
            field_dict["savedPaths"] = saved_paths

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description")

        id = d.pop("id")

        name = d.pop("name")

        def _parse_doc_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        doc_url = _parse_doc_url(d.pop("docUrl", UNSET))

        def _parse_logo_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        logo_url = _parse_logo_url(d.pop("logoUrl", UNSET))

        def _parse_saved_paths(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                saved_paths_type_0 = cast(List[str], data)

                return saved_paths_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        saved_paths = _parse_saved_paths(d.pop("savedPaths", UNSET))

        create_framework = cls(
            description=description,
            id=id,
            name=name,
            doc_url=doc_url,
            logo_url=logo_url,
            saved_paths=saved_paths,
        )

        create_framework.additional_properties = d
        return create_framework

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
