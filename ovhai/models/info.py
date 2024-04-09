from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..ovhai_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.info_arguments import InfoArguments


T = TypeVar("T", bound="Info")


@_attrs_define
class Info:
    """
    Attributes:
        arguments (Union[Unset, InfoArguments]):
        code (Union[Unset, str]):
        message (Union[Unset, str]):
    """

    arguments: Union[Unset, "InfoArguments"] = UNSET
    code: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        arguments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.arguments, Unset):
            arguments = self.arguments.to_dict()

        code = self.code

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if arguments is not UNSET:
            field_dict["arguments"] = arguments
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.info_arguments import InfoArguments

        d = src_dict.copy()
        _arguments = d.pop("arguments", UNSET)
        arguments: Union[Unset, InfoArguments]
        if isinstance(_arguments, Unset):
            arguments = UNSET
        else:
            arguments = InfoArguments.from_dict(_arguments)

        code = d.pop("code", UNSET)

        message = d.pop("message", UNSET)

        info = cls(
            arguments=arguments,
            code=code,
            message=message,
        )

        info.additional_properties = d
        return info

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
