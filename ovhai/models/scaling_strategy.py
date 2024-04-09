from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..ovhai_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.automatic_scaling_strategy import AutomaticScalingStrategy
    from ..models.fixed_scaling_strategy import FixedScalingStrategy


T = TypeVar("T", bound="ScalingStrategy")


@_attrs_define
class ScalingStrategy:
    """
    Attributes:
        automatic (Union[Unset, AutomaticScalingStrategy]):
        fixed (Union[Unset, FixedScalingStrategy]):
    """

    automatic: Union[Unset, "AutomaticScalingStrategy"] = UNSET
    fixed: Union[Unset, "FixedScalingStrategy"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        automatic: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.automatic, Unset):
            automatic = self.automatic.to_dict()

        fixed: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fixed, Unset):
            fixed = self.fixed.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if automatic is not UNSET:
            field_dict["automatic"] = automatic
        if fixed is not UNSET:
            field_dict["fixed"] = fixed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.automatic_scaling_strategy import AutomaticScalingStrategy
        from ..models.fixed_scaling_strategy import FixedScalingStrategy

        d = src_dict.copy()
        _automatic = d.pop("automatic", UNSET)
        automatic: Union[Unset, AutomaticScalingStrategy]
        if isinstance(_automatic, Unset):
            automatic = UNSET
        else:
            automatic = AutomaticScalingStrategy.from_dict(_automatic)

        _fixed = d.pop("fixed", UNSET)
        fixed: Union[Unset, FixedScalingStrategy]
        if isinstance(_fixed, Unset):
            fixed = UNSET
        else:
            fixed = FixedScalingStrategy.from_dict(_fixed)

        scaling_strategy = cls(
            automatic=automatic,
            fixed=fixed,
        )

        scaling_strategy.additional_properties = d
        return scaling_strategy

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
