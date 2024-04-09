from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..ovhai_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_quotas_resources import ProjectQuotasResources


T = TypeVar("T", bound="ProjectQuotas")


@_attrs_define
class ProjectQuotas:
    """Gives quotas related to a project in terms of storage and CPU/GPU resources

    Attributes:
        resources (Union[Unset, ProjectQuotasResources]): Project's number of allowed GPU/CPU resources quotas Example:
            {'CPU': 1, 'GPU': 1}.
        storage (Union[Unset, int]): Project's storage quotas (expressed in bits) Example: 10000000000.
    """

    resources: Union[Unset, "ProjectQuotasResources"] = UNSET
    storage: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        resources: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.resources, Unset):
            resources = self.resources.to_dict()

        storage = self.storage

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resources is not UNSET:
            field_dict["resources"] = resources
        if storage is not UNSET:
            field_dict["storage"] = storage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_quotas_resources import ProjectQuotasResources

        d = src_dict.copy()
        _resources = d.pop("resources", UNSET)
        resources: Union[Unset, ProjectQuotasResources]
        if isinstance(_resources, Unset):
            resources = UNSET
        else:
            resources = ProjectQuotasResources.from_dict(_resources)

        storage = d.pop("storage", UNSET)

        project_quotas = cls(
            resources=resources,
            storage=storage,
        )

        project_quotas.additional_properties = d
        return project_quotas

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
