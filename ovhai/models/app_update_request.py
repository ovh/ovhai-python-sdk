from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..ovhai_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_update import AppUpdate


T = TypeVar("T", bound="AppUpdateRequest")


@_attrs_define
class AppUpdateRequest:
    """
    Attributes:
        app_update (Union[Unset, AppUpdate]):
        id (Union[Unset, str]):
    """

    app_update: Union[Unset, "AppUpdate"] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        app_update: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.app_update, Unset):
            app_update = self.app_update.to_dict()

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_update is not UNSET:
            field_dict["appUpdate"] = app_update
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.app_update import AppUpdate

        d = src_dict.copy()
        _app_update = d.pop("appUpdate", UNSET)
        app_update: Union[Unset, AppUpdate]
        if isinstance(_app_update, Unset):
            app_update = UNSET
        else:
            app_update = AppUpdate.from_dict(_app_update)

        id = d.pop("id", UNSET)

        app_update_request = cls(
            app_update=app_update,
            id=id,
        )

        app_update_request.additional_properties = d
        return app_update_request

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
