import shlex
from configparser import ConfigParser, NoOptionError, NoSectionError
from pathlib import Path
from typing import Final, Iterator, Optional, Tuple

from ..decorators import intercept_errors, require_bins, run_subprocess
from ..errors import UnavailableResourceError
from ..helpers.config import SymConfigFile
from ..helpers.constants import Saml2AwsNoRoles
from ..helpers.contexts import push_env
from ..helpers.keywords_to_options import Argument, Options, keywords_to_options
from ..helpers.params import Profile, get_saml2aws_params
from . import SAMLClient

ErrorPatterns = {Saml2AwsNoRoles: UnavailableResourceError}


class Saml2Aws(SAMLClient):
    __slots__ = ["config_file", "resource", "debug", "_config"]
    binary = "saml2aws"

    resource: str
    debug: bool
    config_file: Final[SymConfigFile]
    _config: Optional[ConfigParser]

    def __init__(self, resource: str, *, debug: bool) -> None:
        super().__init__(resource, debug=debug)
        self.config_file = SymConfigFile(resource=resource, file_name="saml2aws.cfg")

    def is_setup(self) -> bool:
        path = Path.home() / ".saml2aws"
        if not path.exists():
            return False
        config = ConfigParser()
        config.read(path)
        try:
            return bool(config.get("default", "username"))
        except (NoSectionError, NoOptionError):
            return False

    @intercept_errors(ErrorPatterns)
    @run_subprocess
    @require_bins(binary)
    def exec(self, *args: str, **opts: str) -> Iterator[Tuple[Argument, ...]]:
        self.log_subprocess_event(args)
        s2a_options: Options = {
            "verbose": self.debug,
            "config": str(self.config_file),
            "idp_account": "sym",
            "skip-prompt": True,
        }
        config = self.ensure_config()
        # saml2aws exec actually joins all the arguments into a single string and
        # runs it with the shell. So we have to use shlex.join to get around that!
        reparseable = shlex.join(keywords_to_options([*args, opts]))
        with push_env("AWS_REGION", config["sym"]["region"]):
            yield "saml2aws", s2a_options, "login"  # no-op if session active
            yield "saml2aws", s2a_options, "exec", "--", reparseable

    def _ensure_config(self, profile: Profile) -> ConfigParser:
        saml2aws_params = get_saml2aws_params()
        config = ConfigParser()
        config.read_dict(
            {
                "sym": {
                    "url": self.get_aws_saml_url(),
                    "provider": "Okta",
                    "skip_verify": "false",
                    "timeout": "0",
                    "aws_urn": "urn:amazon:webservices",
                    **saml2aws_params,
                    "role_arn": profile.arn,
                    "region": profile.region,
                }
            }
        )
        return config
