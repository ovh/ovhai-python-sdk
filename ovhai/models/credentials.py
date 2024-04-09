from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..ovhai_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.git_credentials import GitCredentials
    from ..models.s3_credentials import S3Credentials


T = TypeVar("T", bound="Credentials")


@_attrs_define
class Credentials:
    """
    Attributes:
        git (Union[Unset, GitCredentials]):
        s3 (Union[Unset, S3Credentials]):
    """

    git: Union[Unset, "GitCredentials"] = UNSET
    s3: Union[Unset, "S3Credentials"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        git: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.git, Unset):
            git = self.git.to_dict()

        s3: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.s3, Unset):
            s3 = self.s3.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if git is not UNSET:
            field_dict["git"] = git
        if s3 is not UNSET:
            field_dict["s3"] = s3

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.git_credentials import GitCredentials
        from ..models.s3_credentials import S3Credentials

        d = src_dict.copy()
        _git = d.pop("git", UNSET)
        git: Union[Unset, GitCredentials]
        if isinstance(_git, Unset):
            git = UNSET
        else:
            git = GitCredentials.from_dict(_git)

        _s3 = d.pop("s3", UNSET)
        s3: Union[Unset, S3Credentials]
        if isinstance(_s3, Unset):
            s3 = UNSET
        else:
            s3 = S3Credentials.from_dict(_s3)

        credentials = cls(
            git=git,
            s3=s3,
        )

        credentials.additional_properties = d
        return credentials

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
