from configparser import ConfigParser
from pathlib import Path
from typing import Final, Iterator, Tuple

from ..decorators import intercept_errors, require_bins, run_subprocess
from ..helpers.contexts import push_env
from ..helpers.keywords_to_options import Argument
from ..helpers.params import Profile
from . import SAMLClient


class AwsProfile(SAMLClient):
    resource: str
    debug: bool
    binary: Final[str] = "aws"

    @intercept_errors()
    @run_subprocess
    @require_bins(binary)
    def exec(self, *args: str, **opts: str) -> Iterator[Tuple[Argument, ...]]:
        self.log_subprocess_event(args)
        with push_env("AWS_PROFILE", self.resource):
            yield *args, opts

    def is_setup(self) -> bool:
        return (Path.home() / '.aws' / 'credentials').exists()

    def _ensure_config(self, profile: Profile) -> ConfigParser:
        return ConfigParser()
