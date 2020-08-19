import os
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Any, Final, Iterator, Literal, MutableMapping, TypedDict, cast

import immutables
import yaml
from portalocker import Lock
from portalocker.constants import LOCK_EX, LOCK_NB, LOCK_SH
from portalocker.exceptions import AlreadyLocked

from .io import TruncatingStringIO

ConfigKey = Literal["org", "email"]


def sym_config_file(file_name: str) -> Path:
    try:
        xdg_config_home = Path(os.environ["XDG_CONFIG_HOME"])
    except KeyError:
        xdg_config_home = Path.home() / ".config"
    sym_config_home = xdg_config_home / "sym"
    return sym_config_home / file_name


class SymConfigFile:
    def __init__(self, *, file_name: str, **dependencies):
        path = Path()
        for k, v in sorted(dependencies.items()):
            path = path / k / str(v)
        self.path = sym_config_file(path / file_name)

        self.read_lock = Lock(str(self.path), mode="r", flags=LOCK_SH | LOCK_NB)
        self.write_lock = Lock(
            str(self.path), mode="w+", flags=LOCK_EX | LOCK_NB, fail_when_locked=True
        )

    def __enter__(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        try:
            # acquire read lock, hold across context
            self.value = self.read_lock.acquire().read()
        except FileNotFoundError:
            self.value = None
        self.file = TruncatingStringIO(initial_value=self.value)
        return self.file

    def __exit__(self, type, value, traceback):
        self.read_lock.release()  # release read lock
        if value:
            return
        if self.file.tell() == 0:
            return
        if self.value != (value := self.file.getvalue()):
            with self.exclusive_access() as f:
                f.write(value)

    def __str__(self):
        return str(self.path)

    def put(self, s: str):
        with self as f:
            f.write(s)

    @contextmanager
    def exclusive_access(self):
        try:
            with self.write_lock as f:  # acquire write lock
                yield f
        except AlreadyLocked:  # another thread is writing same value
            with NamedTemporaryFile(mode="w") as f:  # throw away the input
                yield f

    @contextmanager
    def exclusive_create(self):
        with self.exclusive_access() as f:
            if f.buffer.peek():
                raise AlreadyLocked()
            yield f


class ServerConfigSchema(TypedDict):
    last_connection: datetime


class ConfigSchema(TypedDict, total=False):
    org: str
    email: str
    default_resource: str
    servers: MutableMapping[str, ServerConfigSchema]


class Config(MutableMapping[ConfigKey, Any]):
    __slots__ = ["file", "config"]

    file: Final[SymConfigFile]
    config: Final[ConfigSchema]

    def __init__(self) -> None:
        self.file = SymConfigFile(file_name="config.yml")
        with self.file as f:
            config = cast(ConfigSchema, yaml.safe_load(stream=f) or {})
        self.config = config

    def __flush(self) -> None:
        with self.file as f:
            yaml.safe_dump(self.config, stream=f)

    def __getitem__(self, key: ConfigKey) -> Any:
        item = self.config[key]
        if isinstance(item, dict):
            return immutables.Map(item)
        return item

    def __delitem__(self, key: ConfigKey) -> None:
        del self.config[key]
        self.__flush()

    def __setitem__(self, key: ConfigKey, value: Any) -> None:
        if isinstance(value, immutables.Map):
            value = dict(value)
        self.config[key] = value
        self.__flush()

    def __iter__(self) -> Iterator[ConfigKey]:
        return cast(Iterator[ConfigKey], iter(self.config))

    def __len__(self) -> int:
        return len(self.config)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.path})"

    @classmethod
    def reset(cls):
        setattr(cls, "__instance", cls())

    @classmethod
    def instance(cls) -> "Config":
        if not hasattr(cls, "__instance"):
            cls.reset()
        return getattr(cls, "__instance")

    @classmethod
    def get_org(cls) -> str:
        return cls.instance()["org"]

    @classmethod
    def get_email(cls) -> str:
        return cls.instance()["email"]

    @classmethod
    def get_servers(cls) -> str:
        return cls.instance().get("servers", immutables.Map())

    @classmethod
    def get_instance(cls, instance: str) -> str:
        return cls.get_servers().get(instance, ServerConfigSchema())

    @classmethod
    def touch_instance(cls, instance: str, error: bool = False):
        instance_config = cls.get_instance(instance)
        instance_config["last_connection"] = None if error else datetime.now()
        cls.instance()["servers"] = cls.get_servers().set(instance, instance_config)
