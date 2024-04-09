import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..ovhai_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image import Image
    from ..models.image_mirror_status import ImageMirrorStatus


T = TypeVar("T", bound="ImageVersion")


@_attrs_define
class ImageVersion:
    """
    Attributes:
        created_at (Union[Unset, datetime.datetime]):
        default (Union[Unset, bool]):
        editor_version (Union[None, Unset, str]):
        framework_version (Union[None, Unset, str]):
        image (Union[Unset, Image]):
        image_id (Union[None, Unset, str]):
        mirror_status (Union[Unset, ImageMirrorStatus]):
        partner_id (Union[None, Unset, str]):
        published (Union[Unset, bool]):
        published_at (Union[None, Unset, datetime.datetime]):
        size (Union[None, Unset, int]):
        tag (Union[Unset, str]):
        updated_at (Union[Unset, datetime.datetime]):
        uuid (Union[Unset, str]):
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    default: Union[Unset, bool] = UNSET
    editor_version: Union[None, Unset, str] = UNSET
    framework_version: Union[None, Unset, str] = UNSET
    image: Union[Unset, "Image"] = UNSET
    image_id: Union[None, Unset, str] = UNSET
    mirror_status: Union[Unset, "ImageMirrorStatus"] = UNSET
    partner_id: Union[None, Unset, str] = UNSET
    published: Union[Unset, bool] = UNSET
    published_at: Union[None, Unset, datetime.datetime] = UNSET
    size: Union[None, Unset, int] = UNSET
    tag: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    uuid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        default = self.default

        editor_version: Union[None, Unset, str]
        if isinstance(self.editor_version, Unset):
            editor_version = UNSET
        else:
            editor_version = self.editor_version

        framework_version: Union[None, Unset, str]
        if isinstance(self.framework_version, Unset):
            framework_version = UNSET
        else:
            framework_version = self.framework_version

        image: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        image_id: Union[None, Unset, str]
        if isinstance(self.image_id, Unset):
            image_id = UNSET
        else:
            image_id = self.image_id

        mirror_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mirror_status, Unset):
            mirror_status = self.mirror_status.to_dict()

        partner_id: Union[None, Unset, str]
        if isinstance(self.partner_id, Unset):
            partner_id = UNSET
        else:
            partner_id = self.partner_id

        published = self.published

        published_at: Union[None, Unset, str]
        if isinstance(self.published_at, Unset):
            published_at = UNSET
        elif isinstance(self.published_at, datetime.datetime):
            published_at = self.published_at.isoformat()
        else:
            published_at = self.published_at

        size: Union[None, Unset, int]
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        tag = self.tag

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        uuid = self.uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if default is not UNSET:
            field_dict["default"] = default
        if editor_version is not UNSET:
            field_dict["editorVersion"] = editor_version
        if framework_version is not UNSET:
            field_dict["frameworkVersion"] = framework_version
        if image is not UNSET:
            field_dict["image"] = image
        if image_id is not UNSET:
            field_dict["imageId"] = image_id
        if mirror_status is not UNSET:
            field_dict["mirrorStatus"] = mirror_status
        if partner_id is not UNSET:
            field_dict["partnerId"] = partner_id
        if published is not UNSET:
            field_dict["published"] = published
        if published_at is not UNSET:
            field_dict["publishedAt"] = published_at
        if size is not UNSET:
            field_dict["size"] = size
        if tag is not UNSET:
            field_dict["tag"] = tag
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.image import Image
        from ..models.image_mirror_status import ImageMirrorStatus

        d = src_dict.copy()
        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        default = d.pop("default", UNSET)

        def _parse_editor_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        editor_version = _parse_editor_version(d.pop("editorVersion", UNSET))

        def _parse_framework_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        framework_version = _parse_framework_version(d.pop("frameworkVersion", UNSET))

        _image = d.pop("image", UNSET)
        image: Union[Unset, Image]
        if isinstance(_image, Unset):
            image = UNSET
        else:
            image = Image.from_dict(_image)

        def _parse_image_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        image_id = _parse_image_id(d.pop("imageId", UNSET))

        _mirror_status = d.pop("mirrorStatus", UNSET)
        mirror_status: Union[Unset, ImageMirrorStatus]
        if isinstance(_mirror_status, Unset):
            mirror_status = UNSET
        else:
            mirror_status = ImageMirrorStatus.from_dict(_mirror_status)

        def _parse_partner_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        partner_id = _parse_partner_id(d.pop("partnerId", UNSET))

        published = d.pop("published", UNSET)

        def _parse_published_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                published_at_type_0 = isoparse(data)

                return published_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        published_at = _parse_published_at(d.pop("publishedAt", UNSET))

        def _parse_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        size = _parse_size(d.pop("size", UNSET))

        tag = d.pop("tag", UNSET)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        uuid = d.pop("uuid", UNSET)

        image_version = cls(
            created_at=created_at,
            default=default,
            editor_version=editor_version,
            framework_version=framework_version,
            image=image,
            image_id=image_id,
            mirror_status=mirror_status,
            partner_id=partner_id,
            published=published,
            published_at=published_at,
            size=size,
            tag=tag,
            updated_at=updated_at,
            uuid=uuid,
        )

        image_version.additional_properties = d
        return image_version

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
