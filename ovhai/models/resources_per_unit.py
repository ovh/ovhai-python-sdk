from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..ovhai_types import UNSET, Unset

T = TypeVar("T", bound="ResourcesPerUnit")


@_attrs_define
class ResourcesPerUnit:
    """
    Attributes:
        cpu (Union[Unset, int]): Amount of CPU per flavor Example: 13.
        ephemeral_storage (Union[Unset, int]): Ephemeral Storage available in the job in bytes Example: 42949672960.
        memory (Union[Unset, int]): Memory in bytes Example: 42949672960.
        private_network (Union[Unset, int]): private network bandwidth in bytes/per sec Example: 1500000000.
        public_network (Union[Unset, int]): public network bandwidth in bytes/per sec Example: 1500000000.
    """

    cpu: Union[Unset, int] = UNSET
    ephemeral_storage: Union[Unset, int] = UNSET
    memory: Union[Unset, int] = UNSET
    private_network: Union[Unset, int] = UNSET
    public_network: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cpu = self.cpu

        ephemeral_storage = self.ephemeral_storage

        memory = self.memory

        private_network = self.private_network

        public_network = self.public_network

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpu is not UNSET:
            field_dict["cpu"] = cpu
        if ephemeral_storage is not UNSET:
            field_dict["ephemeralStorage"] = ephemeral_storage
        if memory is not UNSET:
            field_dict["memory"] = memory
        if private_network is not UNSET:
            field_dict["privateNetwork"] = private_network
        if public_network is not UNSET:
            field_dict["publicNetwork"] = public_network

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cpu = d.pop("cpu", UNSET)

        ephemeral_storage = d.pop("ephemeralStorage", UNSET)

        memory = d.pop("memory", UNSET)

        private_network = d.pop("privateNetwork", UNSET)

        public_network = d.pop("publicNetwork", UNSET)

        resources_per_unit = cls(
            cpu=cpu,
            ephemeral_storage=ephemeral_storage,
            memory=memory,
            private_network=private_network,
            public_network=public_network,
        )

        resources_per_unit.additional_properties = d
        return resources_per_unit

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
