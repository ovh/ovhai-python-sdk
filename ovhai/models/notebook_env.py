from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..ovhai_types import UNSET, Unset

T = TypeVar("T", bound="NotebookEnv")


@_attrs_define
class NotebookEnv:
    """
    Attributes:
        editor_id (Union[Unset, str]): Desired editor. Full list by running 'ovhai capabilities editor list' Example:
            jupyterlab.
        framework_id (Union[Unset, str]): Desired framework. Full list by running 'ovhai capabilities framework list'
            Example: conda.
        framework_version (Union[Unset, str]): Desired version. Full list by running 'ovhai capabilities framework get
            <framework_id>' Example: conda-py39-cudaDevel11.8-v22-4.
    """

    editor_id: Union[Unset, str] = UNSET
    framework_id: Union[Unset, str] = UNSET
    framework_version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        editor_id = self.editor_id

        framework_id = self.framework_id

        framework_version = self.framework_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if editor_id is not UNSET:
            field_dict["editorId"] = editor_id
        if framework_id is not UNSET:
            field_dict["frameworkId"] = framework_id
        if framework_version is not UNSET:
            field_dict["frameworkVersion"] = framework_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        editor_id = d.pop("editorId", UNSET)

        framework_id = d.pop("frameworkId", UNSET)

        framework_version = d.pop("frameworkVersion", UNSET)

        notebook_env = cls(
            editor_id=editor_id,
            framework_id=framework_id,
            framework_version=framework_version,
        )

        notebook_env.additional_properties = d
        return notebook_env

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
