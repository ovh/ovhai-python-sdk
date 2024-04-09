import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.image_mirror_state import ImageMirrorState
from ..ovhai_types import UNSET, Unset

T = TypeVar("T", bound="ImageMirrorStatus")


@_attrs_define
class ImageMirrorStatus:
    """
    Attributes:
        done_at (Union[None, Unset, datetime.datetime]):
        failure_reason (Union[None, Unset, str]):
        last_done_at (Union[None, Unset, datetime.datetime]):
        retries_count (Union[Unset, int]):
        started_at (Union[None, Unset, datetime.datetime]):
        state (Union[Unset, ImageMirrorState]):
    """

    done_at: Union[None, Unset, datetime.datetime] = UNSET
    failure_reason: Union[None, Unset, str] = UNSET
    last_done_at: Union[None, Unset, datetime.datetime] = UNSET
    retries_count: Union[Unset, int] = UNSET
    started_at: Union[None, Unset, datetime.datetime] = UNSET
    state: Union[Unset, ImageMirrorState] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        done_at: Union[None, Unset, str]
        if isinstance(self.done_at, Unset):
            done_at = UNSET
        elif isinstance(self.done_at, datetime.datetime):
            done_at = self.done_at.isoformat()
        else:
            done_at = self.done_at

        failure_reason: Union[None, Unset, str]
        if isinstance(self.failure_reason, Unset):
            failure_reason = UNSET
        else:
            failure_reason = self.failure_reason

        last_done_at: Union[None, Unset, str]
        if isinstance(self.last_done_at, Unset):
            last_done_at = UNSET
        elif isinstance(self.last_done_at, datetime.datetime):
            last_done_at = self.last_done_at.isoformat()
        else:
            last_done_at = self.last_done_at

        retries_count = self.retries_count

        started_at: Union[None, Unset, str]
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if done_at is not UNSET:
            field_dict["doneAt"] = done_at
        if failure_reason is not UNSET:
            field_dict["failureReason"] = failure_reason
        if last_done_at is not UNSET:
            field_dict["lastDoneAt"] = last_done_at
        if retries_count is not UNSET:
            field_dict["retriesCount"] = retries_count
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_done_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                done_at_type_0 = isoparse(data)

                return done_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        done_at = _parse_done_at(d.pop("doneAt", UNSET))

        def _parse_failure_reason(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        failure_reason = _parse_failure_reason(d.pop("failureReason", UNSET))

        def _parse_last_done_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_done_at_type_0 = isoparse(data)

                return last_done_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_done_at = _parse_last_done_at(d.pop("lastDoneAt", UNSET))

        retries_count = d.pop("retriesCount", UNSET)

        def _parse_started_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = isoparse(data)

                return started_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        started_at = _parse_started_at(d.pop("startedAt", UNSET))

        _state = d.pop("state", UNSET)
        state: Union[Unset, ImageMirrorState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = ImageMirrorState(_state)

        image_mirror_status = cls(
            done_at=done_at,
            failure_reason=failure_reason,
            last_done_at=last_done_at,
            retries_count=retries_count,
            started_at=started_at,
            state=state,
        )

        image_mirror_status.additional_properties = d
        return image_mirror_status

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
