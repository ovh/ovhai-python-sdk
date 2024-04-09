from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..ovhai_types import UNSET, Unset

T = TypeVar("T", bound="UpdateFramework")


@_attrs_define
class UpdateFramework:
    """
    Attributes:
        description (Union[None, Unset, str]): Framework description
        doc_url (Union[None, Unset, str]): Framework documentation URL
        logo_url (Union[None, Unset, str]): Framework logo URL
        name (Union[None, Unset, str]): Framework Name
        saved_paths (Union[List[str], None, Unset]): Saved paths
    """

    description: Union[None, Unset, str] = UNSET
    doc_url: Union[None, Unset, str] = UNSET
    logo_url: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    saved_paths: Union[List[str], None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

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

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        saved_paths: Union[List[str], None, Unset]
        if isinstance(self.saved_paths, Unset):
            saved_paths = UNSET
        elif isinstance(self.saved_paths, list):
            saved_paths = self.saved_paths

        else:
            saved_paths = self.saved_paths

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if doc_url is not UNSET:
            field_dict["docUrl"] = doc_url
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if name is not UNSET:
            field_dict["name"] = name
        if saved_paths is not UNSET:
            field_dict["savedPaths"] = saved_paths

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

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

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

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

        update_framework = cls(
            description=description,
            doc_url=doc_url,
            logo_url=logo_url,
            name=name,
            saved_paths=saved_paths,
        )

        update_framework.additional_properties = d
        return update_framework

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
