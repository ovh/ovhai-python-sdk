from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..ovhai_types import UNSET, Unset

T = TypeVar("T", bound="CreateImageVersion")


@_attrs_define
class CreateImageVersion:
    """
    Attributes:
        tag (str): Image tag
        editor_version (Union[None, Unset, str]): Editor version (notebook image versions only)
        framework_version (Union[None, Unset, str]): Framework version (notebook image versions only)
    """

    tag: str
    editor_version: Union[None, Unset, str] = UNSET
    framework_version: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tag = self.tag

        editor_version: Union[None, Unset, str]
        if isinstance(self.editor_version, Unset):
            editor_version = UNSET
        else:
            editor_version = self.editor_version

        framework_version: Union[None, Unset, str]
        if isinstance(self.framework_version, Unset):
            framework_version = UNSET
        else:
            framework_version = self.framework_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tag": tag,
            }
        )
        if editor_version is not UNSET:
            field_dict["editorVersion"] = editor_version
        if framework_version is not UNSET:
            field_dict["frameworkVersion"] = framework_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tag = d.pop("tag")

        def _parse_editor_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        editor_version = _parse_editor_version(d.pop("editorVersion", UNSET))

        def _parse_framework_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        framework_version = _parse_framework_version(d.pop("frameworkVersion", UNSET))

        create_image_version = cls(
            tag=tag,
            editor_version=editor_version,
            framework_version=framework_version,
        )

        create_image_version.additional_properties = d
        return create_image_version

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
