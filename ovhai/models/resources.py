from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..ovhai_types import UNSET, Unset

T = TypeVar("T", bound="Resources")


@_attrs_define
class Resources:
    """
    Attributes:
        cpu (Union[Unset, int]): Count of CPU
        ephemeral_storage (Union[Unset, int]): Ephemeral Storage available in the job in bytes Example: 42949672960.
        flavor (Union[Unset, str]): id of the flavor you want to use. Full list by running 'ovhai capabilities flavor
            list' Example: ai1-1-gpu.
        gpu (Union[Unset, int]): Count of GPU
        gpu_brand (Union[None, Unset, str]):  Example: NVIDIA.
        gpu_memory (Union[None, Unset, int]): GPU memory in bytes Example: 34359738368.
        gpu_model (Union[None, Unset, str]):  Example: Tesla-V100S.
        memory (Union[Unset, int]): Memory in bytes Example: 42949672960.
        private_network (Union[Unset, int]): private network bandwidth in bytes/per sec Example: 1500000000.
        public_network (Union[Unset, int]): public network bandwidth in bytes/per sec Example: 1500000000.
    """

    cpu: Union[Unset, int] = UNSET
    ephemeral_storage: Union[Unset, int] = UNSET
    flavor: Union[Unset, str] = UNSET
    gpu: Union[Unset, int] = UNSET
    gpu_brand: Union[None, Unset, str] = UNSET
    gpu_memory: Union[None, Unset, int] = UNSET
    gpu_model: Union[None, Unset, str] = UNSET
    memory: Union[Unset, int] = UNSET
    private_network: Union[Unset, int] = UNSET
    public_network: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cpu = self.cpu

        ephemeral_storage = self.ephemeral_storage

        flavor = self.flavor

        gpu = self.gpu

        gpu_brand: Union[None, Unset, str]
        if isinstance(self.gpu_brand, Unset):
            gpu_brand = UNSET
        else:
            gpu_brand = self.gpu_brand

        gpu_memory: Union[None, Unset, int]
        if isinstance(self.gpu_memory, Unset):
            gpu_memory = UNSET
        else:
            gpu_memory = self.gpu_memory

        gpu_model: Union[None, Unset, str]
        if isinstance(self.gpu_model, Unset):
            gpu_model = UNSET
        else:
            gpu_model = self.gpu_model

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
        if flavor is not UNSET:
            field_dict["flavor"] = flavor
        if gpu is not UNSET:
            field_dict["gpu"] = gpu
        if gpu_brand is not UNSET:
            field_dict["gpuBrand"] = gpu_brand
        if gpu_memory is not UNSET:
            field_dict["gpuMemory"] = gpu_memory
        if gpu_model is not UNSET:
            field_dict["gpuModel"] = gpu_model
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

        flavor = d.pop("flavor", UNSET)

        gpu = d.pop("gpu", UNSET)

        def _parse_gpu_brand(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        gpu_brand = _parse_gpu_brand(d.pop("gpuBrand", UNSET))

        def _parse_gpu_memory(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        gpu_memory = _parse_gpu_memory(d.pop("gpuMemory", UNSET))

        def _parse_gpu_model(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        gpu_model = _parse_gpu_model(d.pop("gpuModel", UNSET))

        memory = d.pop("memory", UNSET)

        private_network = d.pop("privateNetwork", UNSET)

        public_network = d.pop("publicNetwork", UNSET)

        resources = cls(
            cpu=cpu,
            ephemeral_storage=ephemeral_storage,
            flavor=flavor,
            gpu=gpu,
            gpu_brand=gpu_brand,
            gpu_memory=gpu_memory,
            gpu_model=gpu_model,
            memory=memory,
            private_network=private_network,
            public_network=public_network,
        )

        resources.additional_properties = d
        return resources

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
