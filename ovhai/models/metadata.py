from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..ovhai_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links import Links


T = TypeVar("T", bound="Metadata")


@_attrs_define
class Metadata:
    """
    Attributes:
        current_page (Union[Unset, int]):
        links (Union[Unset, Links]):
        page_count (Union[Unset, int]):
        total (Union[Unset, int]):
    """

    current_page: Union[Unset, int] = UNSET
    links: Union[Unset, "Links"] = UNSET
    page_count: Union[Unset, int] = UNSET
    total: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current_page = self.current_page

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        page_count = self.page_count

        total = self.total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_page is not UNSET:
            field_dict["currentPage"] = current_page
        if links is not UNSET:
            field_dict["links"] = links
        if page_count is not UNSET:
            field_dict["pageCount"] = page_count
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.links import Links

        d = src_dict.copy()
        current_page = d.pop("currentPage", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = Links.from_dict(_links)

        page_count = d.pop("pageCount", UNSET)

        total = d.pop("total", UNSET)

        metadata = cls(
            current_page=current_page,
            links=links,
            page_count=page_count,
            total=total,
        )

        metadata.additional_properties = d
        return metadata

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
