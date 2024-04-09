from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..ovhai_types import UNSET, Unset

T = TypeVar("T", bound="UpdateImageVersion")


@_attrs_define
class UpdateImageVersion:
    """
    Attributes:
        default (Union[None, Unset, bool]): Set as true for marking the version as image default (notebook image
            versions only)
        editor_version (Union[None, Unset, str]): Editor version (notebook image versions only)
        framework_version (Union[None, Unset, str]): Framework version (notebook image versions only)
        published (Union[None, Unset, bool]): Version publishing
    """

    default: Union[None, Unset, bool] = UNSET
    editor_version: Union[None, Unset, str] = UNSET
    framework_version: Union[None, Unset, str] = UNSET
    published: Union[None, Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        default: Union[None, Unset, bool]
        if isinstance(self.default, Unset):
            default = UNSET
        else:
            default = self.default

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

        published: Union[None, Unset, bool]
        if isinstance(self.published, Unset):
            published = UNSET
        else:
            published = self.published

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default is not UNSET:
            field_dict["default"] = default
        if editor_version is not UNSET:
            field_dict["editorVersion"] = editor_version
        if framework_version is not UNSET:
            field_dict["frameworkVersion"] = framework_version
        if published is not UNSET:
            field_dict["published"] = published

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_default(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        default = _parse_default(d.pop("default", UNSET))

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

        def _parse_published(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        published = _parse_published(d.pop("published", UNSET))

        update_image_version = cls(
            default=default,
            editor_version=editor_version,
            framework_version=framework_version,
            published=published,
        )

        update_image_version.additional_properties = d
        return update_image_version

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
