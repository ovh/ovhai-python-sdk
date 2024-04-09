import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.licensing_type import LicensingType
from ..models.product_type import ProductType
from ..ovhai_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.framework import Framework
    from ..models.partner import Partner


T = TypeVar("T", bound="Image")


@_attrs_define
class Image:
    """
    Attributes:
        created_at (Union[Unset, datetime.datetime]):
        description (Union[None, Unset, str]):
        doc_url (Union[None, Unset, str]):
        editor_id (Union[None, Unset, str]):
        framework (Union[Unset, Framework]):
        framework_id (Union[None, Unset, str]):
        id (Union[Unset, str]):
        licensing (Union[Unset, LicensingType]):
        logo_url (Union[None, Unset, str]):
        name (Union[Unset, str]):
        partner (Union[Unset, Partner]):
        partner_id (Union[None, Unset, str]):
        product (Union[Unset, ProductType]):
        source (Union[Unset, str]):
        updated_at (Union[Unset, datetime.datetime]):
        uuid (Union[Unset, str]):
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    description: Union[None, Unset, str] = UNSET
    doc_url: Union[None, Unset, str] = UNSET
    editor_id: Union[None, Unset, str] = UNSET
    framework: Union[Unset, "Framework"] = UNSET
    framework_id: Union[None, Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    licensing: Union[Unset, LicensingType] = UNSET
    logo_url: Union[None, Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    partner: Union[Unset, "Partner"] = UNSET
    partner_id: Union[None, Unset, str] = UNSET
    product: Union[Unset, ProductType] = UNSET
    source: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    uuid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        doc_url: Union[None, Unset, str]
        if isinstance(self.doc_url, Unset):
            doc_url = UNSET
        else:
            doc_url = self.doc_url

        editor_id: Union[None, Unset, str]
        if isinstance(self.editor_id, Unset):
            editor_id = UNSET
        else:
            editor_id = self.editor_id

        framework: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.framework, Unset):
            framework = self.framework.to_dict()

        framework_id: Union[None, Unset, str]
        if isinstance(self.framework_id, Unset):
            framework_id = UNSET
        else:
            framework_id = self.framework_id

        id = self.id

        licensing: Union[Unset, str] = UNSET
        if not isinstance(self.licensing, Unset):
            licensing = self.licensing.value

        logo_url: Union[None, Unset, str]
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        name = self.name

        partner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.partner, Unset):
            partner = self.partner.to_dict()

        partner_id: Union[None, Unset, str]
        if isinstance(self.partner_id, Unset):
            partner_id = UNSET
        else:
            partner_id = self.partner_id

        product: Union[Unset, str] = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.value

        source = self.source

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        uuid = self.uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if doc_url is not UNSET:
            field_dict["docUrl"] = doc_url
        if editor_id is not UNSET:
            field_dict["editorId"] = editor_id
        if framework is not UNSET:
            field_dict["framework"] = framework
        if framework_id is not UNSET:
            field_dict["frameworkId"] = framework_id
        if id is not UNSET:
            field_dict["id"] = id
        if licensing is not UNSET:
            field_dict["licensing"] = licensing
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if name is not UNSET:
            field_dict["name"] = name
        if partner is not UNSET:
            field_dict["partner"] = partner
        if partner_id is not UNSET:
            field_dict["partnerId"] = partner_id
        if product is not UNSET:
            field_dict["product"] = product
        if source is not UNSET:
            field_dict["source"] = source
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.framework import Framework
        from ..models.partner import Partner

        d = src_dict.copy()
        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_doc_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        doc_url = _parse_doc_url(d.pop("docUrl", UNSET))

        def _parse_editor_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        editor_id = _parse_editor_id(d.pop("editorId", UNSET))

        _framework = d.pop("framework", UNSET)
        framework: Union[Unset, Framework]
        if isinstance(_framework, Unset):
            framework = UNSET
        else:
            framework = Framework.from_dict(_framework)

        def _parse_framework_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        framework_id = _parse_framework_id(d.pop("frameworkId", UNSET))

        id = d.pop("id", UNSET)

        _licensing = d.pop("licensing", UNSET)
        licensing: Union[Unset, LicensingType]
        if isinstance(_licensing, Unset):
            licensing = UNSET
        else:
            licensing = LicensingType(_licensing)

        def _parse_logo_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        logo_url = _parse_logo_url(d.pop("logoUrl", UNSET))

        name = d.pop("name", UNSET)

        _partner = d.pop("partner", UNSET)
        partner: Union[Unset, Partner]
        if isinstance(_partner, Unset):
            partner = UNSET
        else:
            partner = Partner.from_dict(_partner)

        def _parse_partner_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        partner_id = _parse_partner_id(d.pop("partnerId", UNSET))

        _product = d.pop("product", UNSET)
        product: Union[Unset, ProductType]
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = ProductType(_product)

        source = d.pop("source", UNSET)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        uuid = d.pop("uuid", UNSET)

        image = cls(
            created_at=created_at,
            description=description,
            doc_url=doc_url,
            editor_id=editor_id,
            framework=framework,
            framework_id=framework_id,
            id=id,
            licensing=licensing,
            logo_url=logo_url,
            name=name,
            partner=partner,
            partner_id=partner_id,
            product=product,
            source=source,
            updated_at=updated_at,
            uuid=uuid,
        )

        image.additional_properties = d
        return image

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
