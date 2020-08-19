from configparser import ConfigParser, NoOptionError, NoSectionError
from pathlib import Path
from typing import Final, Iterator, Optional, Tuple

import keyring

from ..decorators import intercept_errors, require_bins, run_subprocess
from ..errors import ResourceNotSetup, UnavailableResourceError
from ..helpers.config import SymConfigFile
from ..helpers.constants import AwsOktaNoRoles, AwsOktaNotSetup
from ..helpers.contexts import push_env
from ..helpers.keywords_to_options import Argument
from ..helpers.params import Profile, get_aws_okta_params
from . import SAMLClient

ErrorPatterns = {
    AwsOktaNoRoles: UnavailableResourceError,
    AwsOktaNotSetup: ResourceNotSetup,
}


class AwsOkta(SAMLClient):
    __slots__ = ["config_file", "resource", "debug", "_config"]
    binary = "aws-okta"

    resource: str
    debug: bool
    config_file: Final[SymConfigFile]
    _config: Optional[ConfigParser]

    def __init__(self, resource: str, *, debug: bool) -> None:
        super().__init__(resource, debug=debug)
        self.config_file = SymConfigFile(resource=resource, file_name="aws-okta.cfg")

    def is_setup(self) -> bool:
        try:
            return bool(keyring.get_password("aws-okta-login", "okta-creds"))
        except Exception:
            return False

    @intercept_errors(ErrorPatterns)
    @run_subprocess
    @require_bins(binary)
    def exec(self, *args: str, **opts: str) -> Iterator[Tuple[Argument, ...]]:
        self.log_subprocess_event(args)
        self.ensure_config()
        with push_env("AWS_CONFIG_FILE", str(self.config_file)):
            yield "aws-okta", {"debug": self.debug}, "exec", "sym", "--", *args, opts

    def _ensure_config(self, profile: Profile) -> ConfigParser:
        config = ConfigParser(default_section="okta")
        config.read_dict(
            {
                "okta": get_aws_okta_params(),
                "profile sym": {
                    "aws_saml_url": self.get_aws_saml_url(bare=True),
                    "region": profile.region,
                    "role_arn": profile.arn,
                },
            }
        )
        return config
