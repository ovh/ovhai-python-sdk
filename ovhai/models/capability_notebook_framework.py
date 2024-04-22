from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..ovhai_types import UNSET, Unset

T = TypeVar("T", bound="CapabilityNotebookFramework")


@_attrs_define
class CapabilityNotebookFramework:
    """
    Attributes:
        description (Union[Unset, str]): Short description of the framework Example: An end-to-end open source machine
            learning platform.
        doc_url (Union[Unset, str]): URL toward frameworks documentation Example: https://www.tensorflow.org/api_docs.
        id (Union[Unset, str]): unique framework id Example: tensorflow.
        logo_url (Union[Unset, str]): url toward the logo to illustrate the framework Example:
            https://storage.gra.cloud.ovh.net/v1/AUTH_00000000000000000000000000000000/logo/tensorflow.svg.
        name (Union[Unset, str]): Name of the base framework Example: Tensorflow.
        saved_paths (Union[Unset, List[str]]): paths that are saved between start & stop of notebooks Example:
            ['/workspace'].
        versions (Union[Unset, List[str]]): Specific version for the framework Example: ['2.4.1-ovh.beta.0'].
    """

    description: Union[Unset, str] = UNSET
    doc_url: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    logo_url: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    saved_paths: Union[Unset, List[str]] = UNSET
    versions: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        doc_url = self.doc_url

        id = self.id

        logo_url = self.logo_url

        name = self.name

        saved_paths: Union[Unset, List[str]] = UNSET
        if not isinstance(self.saved_paths, Unset):
            saved_paths = self.saved_paths

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
        if saved_paths is not UNSET:
            field_dict["savedPaths"] = saved_paths
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

        saved_paths = cast(List[str], d.pop("savedPaths", UNSET))

        versions = cast(List[str], d.pop("versions", UNSET))

        capability_notebook_framework = cls(
            description=description,
            doc_url=doc_url,
            id=id,
            logo_url=logo_url,
            name=name,
            saved_paths=saved_paths,
            versions=versions,
        )

        capability_notebook_framework.additional_properties = d
        return capability_notebook_framework

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
