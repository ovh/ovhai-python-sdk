from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.me_token_kind import MeTokenKind
from ..models.role import Role
from ..ovhai_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_quotas import ProjectQuotas


T = TypeVar("T", bound="Me")


@_attrs_define
class Me:
    """
    Attributes:
        name (Union[Unset, str]): Openstack user name Example: user.
        quotas (Union[Unset, ProjectQuotas]): Gives quotas related to a project in terms of storage and CPU/GPU
            resources
        role (Union[Unset, Role]):
        tenant (Union[Unset, str]): Openstack tenant Example: 226611a69e109427083f154c9cc858f58.
        token_kind (Union[Unset, MeTokenKind]): Token kind for current user
        trust_id (Union[Unset, str]): Trust used to access the object storage Example:
            226611a69e109427083f154c9cc858f58.
    """

    name: Union[Unset, str] = UNSET
    quotas: Union[Unset, "ProjectQuotas"] = UNSET
    role: Union[Unset, Role] = UNSET
    tenant: Union[Unset, str] = UNSET
    token_kind: Union[Unset, MeTokenKind] = UNSET
    trust_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        quotas: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.quotas, Unset):
            quotas = self.quotas.to_dict()

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        tenant = self.tenant

        token_kind: Union[Unset, str] = UNSET
        if not isinstance(self.token_kind, Unset):
            token_kind = self.token_kind.value

        trust_id = self.trust_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if quotas is not UNSET:
            field_dict["quotas"] = quotas
        if role is not UNSET:
            field_dict["role"] = role
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if token_kind is not UNSET:
            field_dict["tokenKind"] = token_kind
        if trust_id is not UNSET:
            field_dict["trustId"] = trust_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_quotas import ProjectQuotas

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _quotas = d.pop("quotas", UNSET)
        quotas: Union[Unset, ProjectQuotas]
        if isinstance(_quotas, Unset):
            quotas = UNSET
        else:
            quotas = ProjectQuotas.from_dict(_quotas)

        _role = d.pop("role", UNSET)
        role: Union[Unset, Role]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = Role(_role)

        tenant = d.pop("tenant", UNSET)

        _token_kind = d.pop("tokenKind", UNSET)
        token_kind: Union[Unset, MeTokenKind]
        if isinstance(_token_kind, Unset):
            token_kind = UNSET
        else:
            token_kind = MeTokenKind(_token_kind)

        trust_id = d.pop("trustId", UNSET)

        me = cls(
            name=name,
            quotas=quotas,
            role=role,
            tenant=tenant,
            token_kind=token_kind,
            trust_id=trust_id,
        )

        me.additional_properties = d
        return me

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
