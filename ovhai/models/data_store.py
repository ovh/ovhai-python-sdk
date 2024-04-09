from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.store_owner import StoreOwner
from ..models.store_type import StoreType
from ..ovhai_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credentials import Credentials


T = TypeVar("T", bound="DataStore")


@_attrs_define
class DataStore:
    """
    Attributes:
        alias (Union[Unset, str]):
        credentials (Union[Unset, Credentials]):
        endpoint (Union[Unset, str]):
        owner (Union[Unset, StoreOwner]):
        type (Union[Unset, StoreType]):
    """

    alias: Union[Unset, str] = UNSET
    credentials: Union[Unset, "Credentials"] = UNSET
    endpoint: Union[Unset, str] = UNSET
    owner: Union[Unset, StoreOwner] = UNSET
    type: Union[Unset, StoreType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alias = self.alias

        credentials: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        endpoint = self.endpoint

        owner: Union[Unset, str] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.value

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alias is not UNSET:
            field_dict["alias"] = alias
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if owner is not UNSET:
            field_dict["owner"] = owner
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.credentials import Credentials

        d = src_dict.copy()
        alias = d.pop("alias", UNSET)

        _credentials = d.pop("credentials", UNSET)
        credentials: Union[Unset, Credentials]
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = Credentials.from_dict(_credentials)

        endpoint = d.pop("endpoint", UNSET)

        _owner = d.pop("owner", UNSET)
        owner: Union[Unset, StoreOwner]
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = StoreOwner(_owner)

        _type = d.pop("type", UNSET)
        type: Union[Unset, StoreType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = StoreType(_type)

        data_store = cls(
            alias=alias,
            credentials=credentials,
            endpoint=endpoint,
            owner=owner,
            type=type,
        )

        data_store.additional_properties = d
        return data_store

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
