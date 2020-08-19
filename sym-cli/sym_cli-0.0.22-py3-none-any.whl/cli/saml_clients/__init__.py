import re
import sys
from abc import ABC, abstractmethod
from configparser import ConfigParser
from typing import ClassVar, Final, Optional, Type
from urllib.parse import urlsplit

from ..errors import CliError
from ..helpers import segment
from ..helpers.config import SymConfigFile
from ..helpers.params import Profile, get_aws_saml_url, get_profile


class SAMLClient(ABC):
    binary: ClassVar[str]
    resource: str
    debug: bool
    config_file: Final[SymConfigFile]
    _config: Optional[ConfigParser]

    def __init__(self, resource: str, *, debug: bool) -> None:
        self.resource = resource
        self.debug = debug
        self._config = None

    @abstractmethod
    def exec(self, *args: str, **opts: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def _ensure_config(self, profile: Profile) -> ConfigParser:
        raise NotImplementedError

    def ensure_config(self) -> ConfigParser:
        if not self._config:
            config = self._ensure_config(self.get_profile())
            with self.config_file as f:
                config.write(f)
            self.dconfig(config)
            self._config = config
        return self._config

    def subconfig(self, file_name):
        return SymConfigFile(resource=self.resource, file_name=file_name)

    def dprint(self, s: str):
        if self.debug:
            print(f"{s}\n")

    def dconfig(self, config: ConfigParser):
        if self.debug:
            print("Writing config:")
            config.write(sys.stdout)

    def log_subprocess_event(self, command: tuple):
        segment.track("Subprocess Called", binary=command[0])

    def get_profile(self) -> Profile:
        try:
            profile = get_profile(self.resource)
        except KeyError:
            raise CliError(f"Invalid resource: {self.resource}")

        self.dprint(f"Using profile {profile}")
        return profile

    def get_aws_saml_url(self, bare: bool = False) -> str:
        url = get_aws_saml_url(self.resource)
        if bare:
            url = urlsplit(url).path[1:]
        return url

    def get_creds(self):
        output = self.exec("env", capture_output_=True)[-1]
        env_vars = re.findall(r"([\w_]+)=(.+)\n", output)
        return {
            k: v
            for k, v in env_vars
            if k
            in (
                "AWS_REGION",
                "AWS_ACCESS_KEY_ID",
                "AWS_SECRET_ACCESS_KEY",
                "AWS_SESSION_TOKEN",
            )
        }

    def clone(self, *, klass: Type["SAMLClient"] = None, **overrides):
        kwargs = {
            key: overrides.get(key, getattr(self, key)) for key in ["resource", "debug"]
        }
        return (klass or self.__class__)(**kwargs)
