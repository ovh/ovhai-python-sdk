from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..ovhai_types import UNSET, Unset

T = TypeVar("T", bound="CapabilityNotebookEditor")


@_attrs_define
class CapabilityNotebookEditor:
    """
    Attributes:
        description (Union[Unset, str]): Short description of the editor Example: JupyterLab is a web-based interactive
            development environment.
        doc_url (Union[Unset, str]): URL toward editor documentation Example:
            https://jupyterlab.readthedocs.io/en/stable/.
        id (Union[Unset, str]): unique editor id Example: jupyterlab.
        incompatible_with (Union[Unset, List[str]]):
        logo_url (Union[Unset, str]):  url toward the logo that illustrates the editor
        name (Union[Unset, str]): Name of the editor Example: JupyterLab.
        probe_path (Union[Unset, str]):
        version (Union[Unset, str]): Current version of the editor Example: 1.0.
    """

    description: Union[Unset, str] = UNSET
    doc_url: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    incompatible_with: Union[Unset, List[str]] = UNSET
    logo_url: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    probe_path: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        doc_url = self.doc_url

        id = self.id

        incompatible_with: Union[Unset, List[str]] = UNSET
        if not isinstance(self.incompatible_with, Unset):
            incompatible_with = self.incompatible_with

        logo_url = self.logo_url

        name = self.name

        probe_path = self.probe_path

        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if doc_url is not UNSET:
            field_dict["docUrl"] = doc_url
        if id is not UNSET:
            field_dict["id"] = id
        if incompatible_with is not UNSET:
            field_dict["incompatibleWith"] = incompatible_with
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if name is not UNSET:
            field_dict["name"] = name
        if probe_path is not UNSET:
            field_dict["probePath"] = probe_path
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        doc_url = d.pop("docUrl", UNSET)

        id = d.pop("id", UNSET)

        incompatible_with = cast(List[str], d.pop("incompatibleWith", UNSET))

        logo_url = d.pop("logoUrl", UNSET)

        name = d.pop("name", UNSET)

        probe_path = d.pop("probePath", UNSET)

        version = d.pop("version", UNSET)

        capability_notebook_editor = cls(
            description=description,
            doc_url=doc_url,
            id=id,
            incompatible_with=incompatible_with,
            logo_url=logo_url,
            name=name,
            probe_path=probe_path,
            version=version,
        )

        capability_notebook_editor.additional_properties = d
        return capability_notebook_editor

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
