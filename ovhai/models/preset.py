from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.preset_type import PresetType
from ..ovhai_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.doc_url import DocURL
    from ..models.preset_capabilities import PresetCapabilities
    from ..models.preset_partner import PresetPartner


T = TypeVar("T", bound="Preset")


@_attrs_define
class Preset:
    """
    Attributes:
        capabilities (Union[Unset, PresetCapabilities]):
        descriptions (Union[Unset, List[str]]):
        doc_url (Union[Unset, List['DocURL']]):
        id (Union[Unset, str]):
        logo_url (Union[Unset, str]):
        name (Union[Unset, str]):
        partner (Union[Unset, PresetPartner]):
        snippet (Union[Unset, str]):
        type (Union[Unset, PresetType]):
    """

    capabilities: Union[Unset, "PresetCapabilities"] = UNSET
    descriptions: Union[Unset, List[str]] = UNSET
    doc_url: Union[Unset, List["DocURL"]] = UNSET
    id: Union[Unset, str] = UNSET
    logo_url: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    partner: Union[Unset, "PresetPartner"] = UNSET
    snippet: Union[Unset, str] = UNSET
    type: Union[Unset, PresetType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        capabilities: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities.to_dict()

        descriptions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.descriptions, Unset):
            descriptions = self.descriptions

        doc_url: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.doc_url, Unset):
            doc_url = []
            for doc_url_item_data in self.doc_url:
                doc_url_item = doc_url_item_data.to_dict()
                doc_url.append(doc_url_item)

        id = self.id

        logo_url = self.logo_url

        name = self.name

        partner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.partner, Unset):
            partner = self.partner.to_dict()

        snippet = self.snippet

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if descriptions is not UNSET:
            field_dict["descriptions"] = descriptions
        if doc_url is not UNSET:
            field_dict["docUrl"] = doc_url
        if id is not UNSET:
            field_dict["id"] = id
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if name is not UNSET:
            field_dict["name"] = name
        if partner is not UNSET:
            field_dict["partner"] = partner
        if snippet is not UNSET:
            field_dict["snippet"] = snippet
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.doc_url import DocURL
        from ..models.preset_capabilities import PresetCapabilities
        from ..models.preset_partner import PresetPartner

        d = src_dict.copy()
        _capabilities = d.pop("capabilities", UNSET)
        capabilities: Union[Unset, PresetCapabilities]
        if isinstance(_capabilities, Unset):
            capabilities = UNSET
        else:
            capabilities = PresetCapabilities.from_dict(_capabilities)

        descriptions = cast(List[str], d.pop("descriptions", UNSET))

        doc_url = []
        _doc_url = d.pop("docUrl", UNSET)
        for doc_url_item_data in _doc_url or []:
            doc_url_item = DocURL.from_dict(doc_url_item_data)

            doc_url.append(doc_url_item)

        id = d.pop("id", UNSET)

        logo_url = d.pop("logoUrl", UNSET)

        name = d.pop("name", UNSET)

        _partner = d.pop("partner", UNSET)
        partner: Union[Unset, PresetPartner]
        if isinstance(_partner, Unset):
            partner = UNSET
        else:
            partner = PresetPartner.from_dict(_partner)

        snippet = d.pop("snippet", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, PresetType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = PresetType(_type)

        preset = cls(
            capabilities=capabilities,
            descriptions=descriptions,
            doc_url=doc_url,
            id=id,
            logo_url=logo_url,
            name=name,
            partner=partner,
            snippet=snippet,
            type=type,
        )

        preset.additional_properties = d
        return preset

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
