import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..ovhai_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.info import Info
    from ..models.volume import Volume
    from ..models.volume_status import VolumeStatus


T = TypeVar("T", bound="DataSyncProgress")


@_attrs_define
class DataSyncProgress:
    """
    Attributes:
        app_volume (Union[Unset, Volume]):
        completed (Union[Unset, int]):
        created_at (Union[Unset, datetime.datetime]):
        data_sync_id (Union[Unset, str]):
        deleted (Union[Unset, int]):
        direction (Union[Unset, str]):
        eta (Union[Unset, int]): ETA in second. Deprecated
        failed (Union[Unset, int]):
        id (Union[Unset, str]):
        info (Union[Unset, str]):  Example: container@GRA.
        job_volume (Union[Unset, Volume]):
        notebook_volume (Union[Unset, Volume]):
        processed (Union[Unset, int]):
        reason (Union[Unset, Info]):
        shutdown (Union[None, Unset, str]):
        skipped (Union[Unset, int]):
        state (Union[Unset, str]):
        total (Union[Unset, int]):
        transferred_bytes (Union[Unset, int]):
        updated_at (Union[Unset, datetime.datetime]):
        volume_status (Union[Unset, VolumeStatus]):
    """

    app_volume: Union[Unset, "Volume"] = UNSET
    completed: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    data_sync_id: Union[Unset, str] = UNSET
    deleted: Union[Unset, int] = UNSET
    direction: Union[Unset, str] = UNSET
    eta: Union[Unset, int] = UNSET
    failed: Union[Unset, int] = UNSET
    id: Union[Unset, str] = UNSET
    info: Union[Unset, str] = UNSET
    job_volume: Union[Unset, "Volume"] = UNSET
    notebook_volume: Union[Unset, "Volume"] = UNSET
    processed: Union[Unset, int] = UNSET
    reason: Union[Unset, "Info"] = UNSET
    shutdown: Union[None, Unset, str] = UNSET
    skipped: Union[Unset, int] = UNSET
    state: Union[Unset, str] = UNSET
    total: Union[Unset, int] = UNSET
    transferred_bytes: Union[Unset, int] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    volume_status: Union[Unset, "VolumeStatus"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        app_volume: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.app_volume, Unset):
            app_volume = self.app_volume.to_dict()

        completed = self.completed

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        data_sync_id = self.data_sync_id

        deleted = self.deleted

        direction = self.direction

        eta = self.eta

        failed = self.failed

        id = self.id

        info = self.info

        job_volume: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.job_volume, Unset):
            job_volume = self.job_volume.to_dict()

        notebook_volume: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notebook_volume, Unset):
            notebook_volume = self.notebook_volume.to_dict()

        processed = self.processed

        reason: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.to_dict()

        shutdown: Union[None, Unset, str]
        if isinstance(self.shutdown, Unset):
            shutdown = UNSET
        else:
            shutdown = self.shutdown

        skipped = self.skipped

        state = self.state

        total = self.total

        transferred_bytes = self.transferred_bytes

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        volume_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.volume_status, Unset):
            volume_status = self.volume_status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_volume is not UNSET:
            field_dict["appVolume"] = app_volume
        if completed is not UNSET:
            field_dict["completed"] = completed
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if data_sync_id is not UNSET:
            field_dict["dataSyncId"] = data_sync_id
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if direction is not UNSET:
            field_dict["direction"] = direction
        if eta is not UNSET:
            field_dict["eta"] = eta
        if failed is not UNSET:
            field_dict["failed"] = failed
        if id is not UNSET:
            field_dict["id"] = id
        if info is not UNSET:
            field_dict["info"] = info
        if job_volume is not UNSET:
            field_dict["jobVolume"] = job_volume
        if notebook_volume is not UNSET:
            field_dict["notebookVolume"] = notebook_volume
        if processed is not UNSET:
            field_dict["processed"] = processed
        if reason is not UNSET:
            field_dict["reason"] = reason
        if shutdown is not UNSET:
            field_dict["shutdown"] = shutdown
        if skipped is not UNSET:
            field_dict["skipped"] = skipped
        if state is not UNSET:
            field_dict["state"] = state
        if total is not UNSET:
            field_dict["total"] = total
        if transferred_bytes is not UNSET:
            field_dict["transferredBytes"] = transferred_bytes
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if volume_status is not UNSET:
            field_dict["volumeStatus"] = volume_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.info import Info
        from ..models.volume import Volume
        from ..models.volume_status import VolumeStatus

        d = src_dict.copy()
        _app_volume = d.pop("appVolume", UNSET)
        app_volume: Union[Unset, Volume]
        if isinstance(_app_volume, Unset):
            app_volume = UNSET
        else:
            if _app_volume is not None:
                app_volume = Volume.from_dict(_app_volume)
            else:
                app_volume = None

        completed = d.pop("completed", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        data_sync_id = d.pop("dataSyncId", UNSET)

        deleted = d.pop("deleted", UNSET)

        direction = d.pop("direction", UNSET)

        eta = d.pop("eta", UNSET)

        failed = d.pop("failed", UNSET)

        id = d.pop("id", UNSET)

        info = d.pop("info", UNSET)

        _job_volume = d.pop("jobVolume", UNSET)
        job_volume: Union[Unset, Volume]
        if isinstance(_job_volume, Unset):
            job_volume = UNSET
        else:
            if _job_volume is not None:
                job_volume = Volume.from_dict(_job_volume)
            else:
                job_volume = None

        _notebook_volume = d.pop("notebookVolume", UNSET)
        notebook_volume: Union[Unset, Volume]
        if isinstance(_notebook_volume, Unset):
            notebook_volume = UNSET
        else:
            if _notebook_volume is not None:
                notebook_volume = Volume.from_dict(_notebook_volume)
            else:
                notebook_volume = None

        processed = d.pop("processed", UNSET)

        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, Info]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = Info.from_dict(_reason)

        def _parse_shutdown(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        shutdown = _parse_shutdown(d.pop("shutdown", UNSET))

        skipped = d.pop("skipped", UNSET)

        state = d.pop("state", UNSET)

        total = d.pop("total", UNSET)

        transferred_bytes = d.pop("transferredBytes", UNSET)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        _volume_status = d.pop("volumeStatus", UNSET)
        volume_status: Union[Unset, VolumeStatus]
        if isinstance(_volume_status, Unset):
            volume_status = UNSET
        else:
            volume_status = VolumeStatus.from_dict(_volume_status)

        data_sync_progress = cls(
            app_volume=app_volume,
            completed=completed,
            created_at=created_at,
            data_sync_id=data_sync_id,
            deleted=deleted,
            direction=direction,
            eta=eta,
            failed=failed,
            id=id,
            info=info,
            job_volume=job_volume,
            notebook_volume=notebook_volume,
            processed=processed,
            reason=reason,
            shutdown=shutdown,
            skipped=skipped,
            state=state,
            total=total,
            transferred_bytes=transferred_bytes,
            updated_at=updated_at,
            volume_status=volume_status,
        )

        data_sync_progress.additional_properties = d
        return data_sync_progress

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
