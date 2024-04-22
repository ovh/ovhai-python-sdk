import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..ovhai_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_sync import DataSync
    from ..models.info import Info
    from ..models.job_state_history import JobStateHistory
    from ..models.volume_status import VolumeStatus


T = TypeVar("T", bound="JobStatus")


@_attrs_define
class JobStatus:
    """
    Attributes:
        data_sync (Union[Unset, List['DataSync']]):
        duration (Union[Unset, int]): Time since the job is RUNNING in seconds
        exit_code (Union[None, Unset, int]): If job is terminated, return the exit code of the job
        external_ip (Union[None, Unset, str]): Job External IP
        finalized_at (Union[None, Unset, datetime.datetime]):
        grpc_address (Union[Unset, str]): Address to reach when you want to access the Job's gRPC services Example:
            https://00000000-0000-0000-0000-000000000000.job-grpc.gra.ai.cloud.ovh.net.
        history (Union[Unset, List['JobStateHistory']]):
        info (Union[Unset, Info]):
        info_url (Union[Unset, str]): Return the information UI URL about the job Example:
            https://ui.gra.ai.cloud.ovh.net/job/00000000-0000-0000-0000-000000000000.
        initializing_at (Union[None, Unset, datetime.datetime]):
        ip (Union[None, Unset, str]): Job internal IP
        last_transition_date (Union[None, Unset, datetime.datetime]):
        monitoring_url (Union[None, Unset, str]): Return the monitoring/grafana UI URL about the job Example:
            https://monitoring.gra.ai.cloud.ovh.net/d/gpu?var-job=00000000-0000-0000-0000-000000000000&from=0000000000000.
        queued_at (Union[None, Unset, datetime.datetime]):
        ssh_url (Union[None, Unset, str]): Return ssh host and user to connect Example:
            ssh://00000000-0000-0000-0000-000000000000@gra.ai.cloud.ovh.net.
        started_at (Union[None, Unset, datetime.datetime]):
        state (Union[Unset, str]):
        stopped_at (Union[None, Unset, datetime.datetime]):
        timeout_at (Union[None, Unset, datetime.datetime]):
        url (Union[Unset, str]): Job access url Example:
            https://00000000-0000-0000-0000-000000000000.job.gra.ai.cloud.ovh.net.
        volumes (Union[Unset, List['VolumeStatus']]):
    """

    data_sync: Union[Unset, List["DataSync"]] = UNSET
    duration: Union[Unset, int] = UNSET
    exit_code: Union[None, Unset, int] = UNSET
    external_ip: Union[None, Unset, str] = UNSET
    finalized_at: Union[None, Unset, datetime.datetime] = UNSET
    grpc_address: Union[Unset, str] = UNSET
    history: Union[Unset, List["JobStateHistory"]] = UNSET
    info: Union[Unset, "Info"] = UNSET
    info_url: Union[Unset, str] = UNSET
    initializing_at: Union[None, Unset, datetime.datetime] = UNSET
    ip: Union[None, Unset, str] = UNSET
    last_transition_date: Union[None, Unset, datetime.datetime] = UNSET
    monitoring_url: Union[None, Unset, str] = UNSET
    queued_at: Union[None, Unset, datetime.datetime] = UNSET
    ssh_url: Union[None, Unset, str] = UNSET
    started_at: Union[None, Unset, datetime.datetime] = UNSET
    state: Union[Unset, str] = UNSET
    stopped_at: Union[None, Unset, datetime.datetime] = UNSET
    timeout_at: Union[None, Unset, datetime.datetime] = UNSET
    url: Union[Unset, str] = UNSET
    volumes: Union[Unset, List["VolumeStatus"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_sync: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data_sync, Unset):
            data_sync = []
            for data_sync_item_data in self.data_sync:
                data_sync_item = data_sync_item_data.to_dict()
                data_sync.append(data_sync_item)

        duration = self.duration

        exit_code: Union[None, Unset, int]
        if isinstance(self.exit_code, Unset):
            exit_code = UNSET
        else:
            exit_code = self.exit_code

        external_ip: Union[None, Unset, str]
        if isinstance(self.external_ip, Unset):
            external_ip = UNSET
        else:
            external_ip = self.external_ip

        finalized_at: Union[None, Unset, str]
        if isinstance(self.finalized_at, Unset):
            finalized_at = UNSET
        elif isinstance(self.finalized_at, datetime.datetime):
            finalized_at = self.finalized_at.isoformat()
        else:
            finalized_at = self.finalized_at

        grpc_address = self.grpc_address

        history: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.history, Unset):
            history = []
            for history_item_data in self.history:
                history_item = history_item_data.to_dict()
                history.append(history_item)

        info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.info, Unset):
            info = self.info.to_dict()

        info_url = self.info_url

        initializing_at: Union[None, Unset, str]
        if isinstance(self.initializing_at, Unset):
            initializing_at = UNSET
        elif isinstance(self.initializing_at, datetime.datetime):
            initializing_at = self.initializing_at.isoformat()
        else:
            initializing_at = self.initializing_at

        ip: Union[None, Unset, str]
        if isinstance(self.ip, Unset):
            ip = UNSET
        else:
            ip = self.ip

        last_transition_date: Union[None, Unset, str]
        if isinstance(self.last_transition_date, Unset):
            last_transition_date = UNSET
        elif isinstance(self.last_transition_date, datetime.datetime):
            last_transition_date = self.last_transition_date.isoformat()
        else:
            last_transition_date = self.last_transition_date

        monitoring_url: Union[None, Unset, str]
        if isinstance(self.monitoring_url, Unset):
            monitoring_url = UNSET
        else:
            monitoring_url = self.monitoring_url

        queued_at: Union[None, Unset, str]
        if isinstance(self.queued_at, Unset):
            queued_at = UNSET
        elif isinstance(self.queued_at, datetime.datetime):
            queued_at = self.queued_at.isoformat()
        else:
            queued_at = self.queued_at

        ssh_url: Union[None, Unset, str]
        if isinstance(self.ssh_url, Unset):
            ssh_url = UNSET
        else:
            ssh_url = self.ssh_url

        started_at: Union[None, Unset, str]
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        state = self.state

        stopped_at: Union[None, Unset, str]
        if isinstance(self.stopped_at, Unset):
            stopped_at = UNSET
        elif isinstance(self.stopped_at, datetime.datetime):
            stopped_at = self.stopped_at.isoformat()
        else:
            stopped_at = self.stopped_at

        timeout_at: Union[None, Unset, str]
        if isinstance(self.timeout_at, Unset):
            timeout_at = UNSET
        elif isinstance(self.timeout_at, datetime.datetime):
            timeout_at = self.timeout_at.isoformat()
        else:
            timeout_at = self.timeout_at

        url = self.url

        volumes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.volumes, Unset):
            volumes = []
            for volumes_item_data in self.volumes:
                volumes_item = volumes_item_data.to_dict()
                volumes.append(volumes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_sync is not UNSET:
            field_dict["dataSync"] = data_sync
        if duration is not UNSET:
            field_dict["duration"] = duration
        if exit_code is not UNSET:
            field_dict["exitCode"] = exit_code
        if external_ip is not UNSET:
            field_dict["externalIp"] = external_ip
        if finalized_at is not UNSET:
            field_dict["finalizedAt"] = finalized_at
        if grpc_address is not UNSET:
            field_dict["grpcAddress"] = grpc_address
        if history is not UNSET:
            field_dict["history"] = history
        if info is not UNSET:
            field_dict["info"] = info
        if info_url is not UNSET:
            field_dict["infoUrl"] = info_url
        if initializing_at is not UNSET:
            field_dict["initializingAt"] = initializing_at
        if ip is not UNSET:
            field_dict["ip"] = ip
        if last_transition_date is not UNSET:
            field_dict["lastTransitionDate"] = last_transition_date
        if monitoring_url is not UNSET:
            field_dict["monitoringUrl"] = monitoring_url
        if queued_at is not UNSET:
            field_dict["queuedAt"] = queued_at
        if ssh_url is not UNSET:
            field_dict["sshUrl"] = ssh_url
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if state is not UNSET:
            field_dict["state"] = state
        if stopped_at is not UNSET:
            field_dict["stoppedAt"] = stopped_at
        if timeout_at is not UNSET:
            field_dict["timeoutAt"] = timeout_at
        if url is not UNSET:
            field_dict["url"] = url
        if volumes is not UNSET:
            field_dict["volumes"] = volumes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_sync import DataSync
        from ..models.info import Info
        from ..models.job_state_history import JobStateHistory
        from ..models.volume_status import VolumeStatus

        d = src_dict.copy()
        data_sync = []
        _data_sync = d.pop("dataSync", UNSET)
        for data_sync_item_data in _data_sync or []:
            data_sync_item = DataSync.from_dict(data_sync_item_data)

            data_sync.append(data_sync_item)

        duration = d.pop("duration", UNSET)

        def _parse_exit_code(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        exit_code = _parse_exit_code(d.pop("exitCode", UNSET))

        def _parse_external_ip(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_ip = _parse_external_ip(d.pop("externalIp", UNSET))

        def _parse_finalized_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                finalized_at_type_0 = isoparse(data)

                return finalized_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        finalized_at = _parse_finalized_at(d.pop("finalizedAt", UNSET))

        grpc_address = d.pop("grpcAddress", UNSET)

        history = []
        _history = d.pop("history", UNSET)
        for history_item_data in _history or []:
            history_item = JobStateHistory.from_dict(history_item_data)

            history.append(history_item)

        _info = d.pop("info", UNSET)
        info: Union[Unset, Info]
        if isinstance(_info, Unset):
            info = UNSET
        else:
            info = Info.from_dict(_info)

        info_url = d.pop("infoUrl", UNSET)

        def _parse_initializing_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                initializing_at_type_0 = isoparse(data)

                return initializing_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        initializing_at = _parse_initializing_at(d.pop("initializingAt", UNSET))

        def _parse_ip(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ip = _parse_ip(d.pop("ip", UNSET))

        def _parse_last_transition_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_transition_date_type_0 = isoparse(data)

                return last_transition_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_transition_date = _parse_last_transition_date(d.pop("lastTransitionDate", UNSET))

        def _parse_monitoring_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        monitoring_url = _parse_monitoring_url(d.pop("monitoringUrl", UNSET))

        def _parse_queued_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                queued_at_type_0 = isoparse(data)

                return queued_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        queued_at = _parse_queued_at(d.pop("queuedAt", UNSET))

        def _parse_ssh_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ssh_url = _parse_ssh_url(d.pop("sshUrl", UNSET))

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

        state = d.pop("state", UNSET)

        def _parse_stopped_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                stopped_at_type_0 = isoparse(data)

                return stopped_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        stopped_at = _parse_stopped_at(d.pop("stoppedAt", UNSET))

        def _parse_timeout_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                timeout_at_type_0 = isoparse(data)

                return timeout_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        timeout_at = _parse_timeout_at(d.pop("timeoutAt", UNSET))

        url = d.pop("url", UNSET)

        volumes = []
        _volumes = d.pop("volumes", UNSET)
        for volumes_item_data in _volumes or []:
            volumes_item = VolumeStatus.from_dict(volumes_item_data)

            volumes.append(volumes_item)

        job_status = cls(
            data_sync=data_sync,
            duration=duration,
            exit_code=exit_code,
            external_ip=external_ip,
            finalized_at=finalized_at,
            grpc_address=grpc_address,
            history=history,
            info=info,
            info_url=info_url,
            initializing_at=initializing_at,
            ip=ip,
            last_transition_date=last_transition_date,
            monitoring_url=monitoring_url,
            queued_at=queued_at,
            ssh_url=ssh_url,
            started_at=started_at,
            state=state,
            stopped_at=stopped_at,
            timeout_at=timeout_at,
            url=url,
            volumes=volumes,
        )

        job_status.additional_properties = d
        return job_status

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
