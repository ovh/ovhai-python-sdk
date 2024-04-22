import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..ovhai_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_sync import DataSync
    from ..models.info import Info
    from ..models.job_status import JobStatus
    from ..models.notebook_workspace import NotebookWorkspace
    from ..models.volume_status import VolumeStatus


T = TypeVar("T", bound="NotebookStatus")


@_attrs_define
class NotebookStatus:
    """
    Attributes:
        data_sync (Union[Unset, List['DataSync']]):
        duration (Union[Unset, int]):
        grpc_address (Union[Unset, str]):
        info (Union[Unset, Info]):
        info_url (Union[Unset, str]):
        last_job_status (Union[Unset, JobStatus]):
        last_started_at (Union[None, Unset, datetime.datetime]):
        last_stopped_at (Union[None, Unset, datetime.datetime]):
        monitoring_url (Union[None, Unset, str]):
        ssh_url (Union[None, Unset, str]): Return ssh host and user to connect Example:
            ssh://00000000-0000-0000-0000-000000000000@gra.training.ai.cloud.ovh.net.
        state (Union[Unset, str]):
        url (Union[Unset, str]):
        volumes (Union[Unset, List['VolumeStatus']]):
        workspace (Union[Unset, NotebookWorkspace]):
    """

    data_sync: Union[Unset, List["DataSync"]] = UNSET
    duration: Union[Unset, int] = UNSET
    grpc_address: Union[Unset, str] = UNSET
    info: Union[Unset, "Info"] = UNSET
    info_url: Union[Unset, str] = UNSET
    last_job_status: Union[Unset, "JobStatus"] = UNSET
    last_started_at: Union[None, Unset, datetime.datetime] = UNSET
    last_stopped_at: Union[None, Unset, datetime.datetime] = UNSET
    monitoring_url: Union[None, Unset, str] = UNSET
    ssh_url: Union[None, Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    volumes: Union[Unset, List["VolumeStatus"]] = UNSET
    workspace: Union[Unset, "NotebookWorkspace"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_sync: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data_sync, Unset):
            data_sync = []
            for data_sync_item_data in self.data_sync:
                data_sync_item = data_sync_item_data.to_dict()
                data_sync.append(data_sync_item)

        duration = self.duration

        grpc_address = self.grpc_address

        info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.info, Unset):
            info = self.info.to_dict()

        info_url = self.info_url

        last_job_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.last_job_status, Unset):
            last_job_status = self.last_job_status.to_dict()

        last_started_at: Union[None, Unset, str]
        if isinstance(self.last_started_at, Unset):
            last_started_at = UNSET
        elif isinstance(self.last_started_at, datetime.datetime):
            last_started_at = self.last_started_at.isoformat()
        else:
            last_started_at = self.last_started_at

        last_stopped_at: Union[None, Unset, str]
        if isinstance(self.last_stopped_at, Unset):
            last_stopped_at = UNSET
        elif isinstance(self.last_stopped_at, datetime.datetime):
            last_stopped_at = self.last_stopped_at.isoformat()
        else:
            last_stopped_at = self.last_stopped_at

        monitoring_url: Union[None, Unset, str]
        if isinstance(self.monitoring_url, Unset):
            monitoring_url = UNSET
        else:
            monitoring_url = self.monitoring_url

        ssh_url: Union[None, Unset, str]
        if isinstance(self.ssh_url, Unset):
            ssh_url = UNSET
        else:
            ssh_url = self.ssh_url

        state = self.state

        url = self.url

        volumes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.volumes, Unset):
            volumes = []
            for volumes_item_data in self.volumes:
                volumes_item = volumes_item_data.to_dict()
                volumes.append(volumes_item)

        workspace: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.workspace, Unset):
            workspace = self.workspace.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_sync is not UNSET:
            field_dict["dataSync"] = data_sync
        if duration is not UNSET:
            field_dict["duration"] = duration
        if grpc_address is not UNSET:
            field_dict["grpcAddress"] = grpc_address
        if info is not UNSET:
            field_dict["info"] = info
        if info_url is not UNSET:
            field_dict["infoUrl"] = info_url
        if last_job_status is not UNSET:
            field_dict["lastJobStatus"] = last_job_status
        if last_started_at is not UNSET:
            field_dict["lastStartedAt"] = last_started_at
        if last_stopped_at is not UNSET:
            field_dict["lastStoppedAt"] = last_stopped_at
        if monitoring_url is not UNSET:
            field_dict["monitoringUrl"] = monitoring_url
        if ssh_url is not UNSET:
            field_dict["sshUrl"] = ssh_url
        if state is not UNSET:
            field_dict["state"] = state
        if url is not UNSET:
            field_dict["url"] = url
        if volumes is not UNSET:
            field_dict["volumes"] = volumes
        if workspace is not UNSET:
            field_dict["workspace"] = workspace

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_sync import DataSync
        from ..models.info import Info
        from ..models.job_status import JobStatus
        from ..models.notebook_workspace import NotebookWorkspace
        from ..models.volume_status import VolumeStatus

        d = src_dict.copy()
        data_sync = []
        _data_sync = d.pop("dataSync", UNSET)
        for data_sync_item_data in _data_sync or []:
            data_sync_item = DataSync.from_dict(data_sync_item_data)

            data_sync.append(data_sync_item)

        duration = d.pop("duration", UNSET)

        grpc_address = d.pop("grpcAddress", UNSET)

        _info = d.pop("info", UNSET)
        info: Union[Unset, Info]
        if isinstance(_info, Unset):
            info = UNSET
        else:
            info = Info.from_dict(_info)

        info_url = d.pop("infoUrl", UNSET)

        _last_job_status = d.pop("lastJobStatus", UNSET)
        last_job_status: Union[Unset, JobStatus]
        if isinstance(_last_job_status, Unset):
            last_job_status = UNSET
        else:
            last_job_status = JobStatus.from_dict(_last_job_status)

        def _parse_last_started_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_started_at_type_0 = isoparse(data)

                return last_started_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_started_at = _parse_last_started_at(d.pop("lastStartedAt", UNSET))

        def _parse_last_stopped_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_stopped_at_type_0 = isoparse(data)

                return last_stopped_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_stopped_at = _parse_last_stopped_at(d.pop("lastStoppedAt", UNSET))

        def _parse_monitoring_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        monitoring_url = _parse_monitoring_url(d.pop("monitoringUrl", UNSET))

        def _parse_ssh_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ssh_url = _parse_ssh_url(d.pop("sshUrl", UNSET))

        state = d.pop("state", UNSET)

        url = d.pop("url", UNSET)

        volumes = []
        _volumes = d.pop("volumes", UNSET)
        for volumes_item_data in _volumes or []:
            volumes_item = VolumeStatus.from_dict(volumes_item_data)

            volumes.append(volumes_item)

        _workspace = d.pop("workspace", UNSET)
        workspace: Union[Unset, NotebookWorkspace]
        if isinstance(_workspace, Unset):
            workspace = UNSET
        else:
            workspace = NotebookWorkspace.from_dict(_workspace)

        notebook_status = cls(
            data_sync=data_sync,
            duration=duration,
            grpc_address=grpc_address,
            info=info,
            info_url=info_url,
            last_job_status=last_job_status,
            last_started_at=last_started_at,
            last_stopped_at=last_stopped_at,
            monitoring_url=monitoring_url,
            ssh_url=ssh_url,
            state=state,
            url=url,
            volumes=volumes,
            workspace=workspace,
        )

        notebook_status.additional_properties = d
        return notebook_status

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
