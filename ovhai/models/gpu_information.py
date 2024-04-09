from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..ovhai_types import UNSET, Unset

T = TypeVar("T", bound="GpuInformation")


@_attrs_define
class GpuInformation:
    """
    Attributes:
        gpu_brand (Union[None, Unset, str]):
        gpu_memory (Union[None, Unset, int]):
        gpu_model (Union[None, Unset, str]):
    """

    gpu_brand: Union[None, Unset, str] = UNSET
    gpu_memory: Union[None, Unset, int] = UNSET
    gpu_model: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gpu_brand is not UNSET:
            field_dict["gpuBrand"] = gpu_brand
        if gpu_memory is not UNSET:
            field_dict["gpuMemory"] = gpu_memory
        if gpu_model is not UNSET:
            field_dict["gpuModel"] = gpu_model

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

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

        gpu_information = cls(
            gpu_brand=gpu_brand,
            gpu_memory=gpu_memory,
            gpu_model=gpu_model,
        )

        gpu_information.additional_properties = d
        return gpu_information

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
