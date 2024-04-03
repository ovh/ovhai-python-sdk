from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.scaling_resource_type import ScalingResourceType

T = TypeVar("T", bound="AutomaticScalingStrategy")


@_attrs_define
class AutomaticScalingStrategy:
    """
    Attributes:
        average_usage_target (int): The average resource usage threshold that the app upscale or downscale will be
            triggered from (in %)
        replicas_max (int): Maximum number of replicas
        replicas_min (int): Minimum number of replicas
        resource_type (ScalingResourceType):
    """

    average_usage_target: int
    replicas_max: int
    replicas_min: int
    resource_type: ScalingResourceType
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        average_usage_target = self.average_usage_target

        replicas_max = self.replicas_max

        replicas_min = self.replicas_min

        resource_type = self.resource_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "averageUsageTarget": average_usage_target,
                "replicasMax": replicas_max,
                "replicasMin": replicas_min,
                "resourceType": resource_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        average_usage_target = d.pop("averageUsageTarget")

        replicas_max = d.pop("replicasMax")

        replicas_min = d.pop("replicasMin")

        resource_type = ScalingResourceType(d.pop("resourceType"))

        automatic_scaling_strategy = cls(
            average_usage_target=average_usage_target,
            replicas_max=replicas_max,
            replicas_min=replicas_min,
            resource_type=resource_type,
        )

        automatic_scaling_strategy.additional_properties = d
        return automatic_scaling_strategy

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
