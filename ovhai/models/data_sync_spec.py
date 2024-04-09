from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.data_sync_spec_direction import DataSyncSpecDirection
from ..ovhai_types import UNSET, Unset

T = TypeVar("T", bound="DataSyncSpec")


@_attrs_define
class DataSyncSpec:
    """
    Attributes:
        direction (DataSyncSpecDirection): direction of data synchronisation
        app_id (Union[None, Unset, str]): associated app id if relevant
        job_id (Union[None, Unset, str]): associated job id if relevant
        manual (Union[Unset, bool]): true if the data sync is started by the user
        volume (Union[None, Unset, str]): id of the associated volume
    """

    direction: DataSyncSpecDirection
    app_id: Union[None, Unset, str] = UNSET
    job_id: Union[None, Unset, str] = UNSET
    manual: Union[Unset, bool] = UNSET
    volume: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        direction = self.direction.value

        app_id: Union[None, Unset, str]
        if isinstance(self.app_id, Unset):
            app_id = UNSET
        else:
            app_id = self.app_id

        job_id: Union[None, Unset, str]
        if isinstance(self.job_id, Unset):
            job_id = UNSET
        else:
            job_id = self.job_id

        manual = self.manual

        volume: Union[None, Unset, str]
        if isinstance(self.volume, Unset):
            volume = UNSET
        else:
            volume = self.volume

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "direction": direction,
            }
        )
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if manual is not UNSET:
            field_dict["manual"] = manual
        if volume is not UNSET:
            field_dict["volume"] = volume

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        direction = DataSyncSpecDirection(d.pop("direction"))

        def _parse_app_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        app_id = _parse_app_id(d.pop("appId", UNSET))

        def _parse_job_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        job_id = _parse_job_id(d.pop("jobId", UNSET))

        manual = d.pop("manual", UNSET)

        def _parse_volume(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        volume = _parse_volume(d.pop("volume", UNSET))

        data_sync_spec = cls(
            direction=direction,
            app_id=app_id,
            job_id=job_id,
            manual=manual,
            volume=volume,
        )

        data_sync_spec.additional_properties = d
        return data_sync_spec

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
