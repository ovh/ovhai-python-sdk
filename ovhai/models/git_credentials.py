from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..ovhai_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.https_basic_auth import HTTPSBasicAuth
    from ..models.ssh_key_pair import SSHKeyPair


T = TypeVar("T", bound="GitCredentials")


@_attrs_define
class GitCredentials:
    """
    Attributes:
        basic_auth (Union[Unset, HTTPSBasicAuth]):
        ssh_keypair (Union[Unset, SSHKeyPair]):
    """

    basic_auth: Union[Unset, "HTTPSBasicAuth"] = UNSET
    ssh_keypair: Union[Unset, "SSHKeyPair"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        basic_auth: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.basic_auth, Unset):
            basic_auth = self.basic_auth.to_dict()

        ssh_keypair: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ssh_keypair, Unset):
            ssh_keypair = self.ssh_keypair.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if basic_auth is not UNSET:
            field_dict["basicAuth"] = basic_auth
        if ssh_keypair is not UNSET:
            field_dict["sshKeypair"] = ssh_keypair

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.https_basic_auth import HTTPSBasicAuth
        from ..models.ssh_key_pair import SSHKeyPair

        d = src_dict.copy()
        _basic_auth = d.pop("basicAuth", UNSET)
        basic_auth: Union[Unset, HTTPSBasicAuth]
        if isinstance(_basic_auth, Unset):
            basic_auth = UNSET
        else:
            basic_auth = HTTPSBasicAuth.from_dict(_basic_auth)

        _ssh_keypair = d.pop("sshKeypair", UNSET)
        ssh_keypair: Union[Unset, SSHKeyPair]
        if isinstance(_ssh_keypair, Unset):
            ssh_keypair = UNSET
        else:
            ssh_keypair = SSHKeyPair.from_dict(_ssh_keypair)

        git_credentials = cls(
            basic_auth=basic_auth,
            ssh_keypair=ssh_keypair,
        )

        git_credentials.additional_properties = d
        return git_credentials

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
