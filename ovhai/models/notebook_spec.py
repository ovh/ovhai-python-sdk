from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..ovhai_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.env import Env
    from ..models.notebook_env import NotebookEnv
    from ..models.notebook_spec_labels_type_0 import NotebookSpecLabelsType0
    from ..models.resources import Resources
    from ..models.volume import Volume


T = TypeVar("T", bound="NotebookSpec")


@_attrs_define
class NotebookSpec:
    """
    Attributes:
        env (Union[Unset, NotebookEnv]):
        env_vars (Union[List['Env'], None, Unset]): Environment variables that will be injected into the notebook
        labels (Union['NotebookSpecLabelsType0', None, Unset]): some label, used to scope tokens, labels prefixed by
            'ovh/' are owned by the platform and overridden Example: {'label': 'some-label'}.
        name (Union[Unset, str]): Notebook name (generated if not provided) Example: jupyterlab-inspiring.
        resources (Union[Unset, Resources]):
        ssh_public_keys (Union[List[str], None, Unset]): SSH Public keys allowed to SSH into the notebook
        timeout_auto_restart (Union[None, Unset, bool]): Auto restart notebook on timeout
        unsecure_http (Union[Unset, bool]): true if notebook api port can be accessed without any authentication token,
            false otherwise
        volumes (Union[List['Volume'], None, Unset]):
    """

    env: Union[Unset, "NotebookEnv"] = UNSET
    env_vars: Union[List["Env"], None, Unset] = UNSET
    labels: Union["NotebookSpecLabelsType0", None, Unset] = UNSET
    name: Union[Unset, str] = UNSET
    resources: Union[Unset, "Resources"] = UNSET
    ssh_public_keys: Union[List[str], None, Unset] = UNSET
    timeout_auto_restart: Union[None, Unset, bool] = UNSET
    unsecure_http: Union[Unset, bool] = UNSET
    volumes: Union[List["Volume"], None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.notebook_spec_labels_type_0 import NotebookSpecLabelsType0

        env: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.env, Unset):
            env = self.env.to_dict()

        env_vars: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.env_vars, Unset):
            env_vars = UNSET
        elif isinstance(self.env_vars, list):
            env_vars = []
            for env_vars_type_0_item_data in self.env_vars:
                env_vars_type_0_item = env_vars_type_0_item_data.to_dict()
                env_vars.append(env_vars_type_0_item)

        else:
            env_vars = self.env_vars

        labels: Union[Dict[str, Any], None, Unset]
        if isinstance(self.labels, Unset):
            labels = UNSET
        elif isinstance(self.labels, NotebookSpecLabelsType0):
            labels = self.labels.to_dict()
        else:
            labels = self.labels

        name = self.name

        resources: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.resources, Unset):
            resources = self.resources.to_dict()

        ssh_public_keys: Union[List[str], None, Unset]
        if isinstance(self.ssh_public_keys, Unset):
            ssh_public_keys = UNSET
        elif isinstance(self.ssh_public_keys, list):
            ssh_public_keys = self.ssh_public_keys

        else:
            ssh_public_keys = self.ssh_public_keys

        timeout_auto_restart: Union[None, Unset, bool]
        if isinstance(self.timeout_auto_restart, Unset):
            timeout_auto_restart = UNSET
        else:
            timeout_auto_restart = self.timeout_auto_restart

        unsecure_http = self.unsecure_http

        volumes: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.volumes, Unset):
            volumes = UNSET
        elif isinstance(self.volumes, list):
            volumes = []
            for volumes_type_0_item_data in self.volumes:
                volumes_type_0_item = volumes_type_0_item_data.to_dict()
                volumes.append(volumes_type_0_item)

        else:
            volumes = self.volumes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if env is not UNSET:
            field_dict["env"] = env
        if env_vars is not UNSET:
            field_dict["envVars"] = env_vars
        if labels is not UNSET:
            field_dict["labels"] = labels
        if name is not UNSET:
            field_dict["name"] = name
        if resources is not UNSET:
            field_dict["resources"] = resources
        if ssh_public_keys is not UNSET:
            field_dict["sshPublicKeys"] = ssh_public_keys
        if timeout_auto_restart is not UNSET:
            field_dict["timeoutAutoRestart"] = timeout_auto_restart
        if unsecure_http is not UNSET:
            field_dict["unsecureHttp"] = unsecure_http
        if volumes is not UNSET:
            field_dict["volumes"] = volumes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.env import Env
        from ..models.notebook_env import NotebookEnv
        from ..models.notebook_spec_labels_type_0 import NotebookSpecLabelsType0
        from ..models.resources import Resources
        from ..models.volume import Volume

        d = src_dict.copy()
        _env = d.pop("env", UNSET)
        env: Union[Unset, NotebookEnv]
        if isinstance(_env, Unset):
            env = UNSET
        else:
            env = NotebookEnv.from_dict(_env)

        def _parse_env_vars(data: object) -> Union[List["Env"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                env_vars_type_0 = []
                _env_vars_type_0 = data
                for env_vars_type_0_item_data in _env_vars_type_0:
                    env_vars_type_0_item = Env.from_dict(env_vars_type_0_item_data)

                    env_vars_type_0.append(env_vars_type_0_item)

                return env_vars_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["Env"], None, Unset], data)

        env_vars = _parse_env_vars(d.pop("envVars", UNSET))

        def _parse_labels(data: object) -> Union["NotebookSpecLabelsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                labels_type_0 = NotebookSpecLabelsType0.from_dict(data)

                return labels_type_0
            except:  # noqa: E722
                pass
            return cast(Union["NotebookSpecLabelsType0", None, Unset], data)

        labels = _parse_labels(d.pop("labels", UNSET))

        name = d.pop("name", UNSET)

        _resources = d.pop("resources", UNSET)
        resources: Union[Unset, Resources]
        if isinstance(_resources, Unset):
            resources = UNSET
        else:
            resources = Resources.from_dict(_resources)

        def _parse_ssh_public_keys(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ssh_public_keys_type_0 = cast(List[str], data)

                return ssh_public_keys_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        ssh_public_keys = _parse_ssh_public_keys(d.pop("sshPublicKeys", UNSET))

        def _parse_timeout_auto_restart(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        timeout_auto_restart = _parse_timeout_auto_restart(d.pop("timeoutAutoRestart", UNSET))

        unsecure_http = d.pop("unsecureHttp", UNSET)

        def _parse_volumes(data: object) -> Union[List["Volume"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                volumes_type_0 = []
                _volumes_type_0 = data
                for volumes_type_0_item_data in _volumes_type_0:
                    volumes_type_0_item = Volume.from_dict(volumes_type_0_item_data)

                    volumes_type_0.append(volumes_type_0_item)

                return volumes_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["Volume"], None, Unset], data)

        volumes = _parse_volumes(d.pop("volumes", UNSET))

        notebook_spec = cls(
            env=env,
            env_vars=env_vars,
            labels=labels,
            name=name,
            resources=resources,
            ssh_public_keys=ssh_public_keys,
            timeout_auto_restart=timeout_auto_restart,
            unsecure_http=unsecure_http,
            volumes=volumes,
        )

        notebook_spec.additional_properties = d
        return notebook_spec

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
