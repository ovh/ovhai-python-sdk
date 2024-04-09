from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.licensing_type import LicensingType
from ..models.product_type import ProductType
from ..ovhai_types import UNSET, Unset

T = TypeVar("T", bound="CreateImage")


@_attrs_define
class CreateImage:
    """
    Attributes:
        id (str): Image ID
        name (str): Image Name
        product (ProductType):
        source (str): Docker image name, including host and port if not Docker Hub, excluding tag
        description (Union[None, Unset, str]): Image description, required for app/job images
        doc_url (Union[None, Unset, str]): Image documentation URL, required for app/job images
        editor_id (Union[None, Unset, str]): Image editor ID, required for and limited to notebook images
        framework_id (Union[None, Unset, str]): Image framework ID, required for and limited to notebook images
        licensing (Union[Unset, LicensingType]):
        logo_url (Union[None, Unset, str]): Image logo URL
    """

    id: str
    name: str
    product: ProductType
    source: str
    description: Union[None, Unset, str] = UNSET
    doc_url: Union[None, Unset, str] = UNSET
    editor_id: Union[None, Unset, str] = UNSET
    framework_id: Union[None, Unset, str] = UNSET
    licensing: Union[Unset, LicensingType] = UNSET
    logo_url: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        product = self.product.value

        source = self.source

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

        licensing: Union[Unset, str] = UNSET
        if not isinstance(self.licensing, Unset):
            licensing = self.licensing.value

        logo_url: Union[None, Unset, str]
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "product": product,
                "source": source,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if doc_url is not UNSET:
            field_dict["docUrl"] = doc_url
        if editor_id is not UNSET:
            field_dict["editorId"] = editor_id
        if framework_id is not UNSET:
            field_dict["frameworkId"] = framework_id
        if licensing is not UNSET:
            field_dict["licensing"] = licensing
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        product = ProductType(d.pop("product"))

        source = d.pop("source")

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

        create_image = cls(
            id=id,
            name=name,
            product=product,
            source=source,
            description=description,
            doc_url=doc_url,
            editor_id=editor_id,
            framework_id=framework_id,
            licensing=licensing,
            logo_url=logo_url,
        )

        create_image.additional_properties = d
        return create_image

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
