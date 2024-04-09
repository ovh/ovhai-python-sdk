from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.product_type import ProductType
from ..ovhai_types import UNSET, Unset

T = TypeVar("T", bound="UpdateImage")


@_attrs_define
class UpdateImage:
    """
    Attributes:
        description (Union[None, Unset, str]): Image description
        doc_url (Union[None, Unset, str]): Image documentation URL
        editor_id (Union[None, Unset, str]): Image editor ID, limited to notebook images
        framework_id (Union[None, Unset, str]): Image framework ID, limited to notebook images
        logo_url (Union[None, Unset, str]): Image logo URL
        name (Union[None, Unset, str]): Image Name
        product (Union[Unset, ProductType]):
        source (Union[None, Unset, str]): Docker image name, including host and port if not Docker Hub, excluding tag
    """

    description: Union[None, Unset, str] = UNSET
    doc_url: Union[None, Unset, str] = UNSET
    editor_id: Union[None, Unset, str] = UNSET
    framework_id: Union[None, Unset, str] = UNSET
    logo_url: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    product: Union[Unset, ProductType] = UNSET
    source: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        framework_id: Union[None, Unset, str]
        if isinstance(self.framework_id, Unset):
            framework_id = UNSET
        else:
            framework_id = self.framework_id

        logo_url: Union[None, Unset, str]
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        product: Union[Unset, str] = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.value

        source: Union[None, Unset, str]
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if doc_url is not UNSET:
            field_dict["docUrl"] = doc_url
        if editor_id is not UNSET:
            field_dict["editorId"] = editor_id
        if framework_id is not UNSET:
            field_dict["frameworkId"] = framework_id
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if name is not UNSET:
            field_dict["name"] = name
        if product is not UNSET:
            field_dict["product"] = product
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

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

        def _parse_framework_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        framework_id = _parse_framework_id(d.pop("frameworkId", UNSET))

        def _parse_logo_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        logo_url = _parse_logo_url(d.pop("logoUrl", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        _product = d.pop("product", UNSET)
        product: Union[Unset, ProductType]
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = ProductType(_product)

        def _parse_source(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source = _parse_source(d.pop("source", UNSET))

        update_image = cls(
            description=description,
            doc_url=doc_url,
            editor_id=editor_id,
            framework_id=framework_id,
            logo_url=logo_url,
            name=name,
            product=product,
            source=source,
        )

        update_image.additional_properties = d
        return update_image

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
