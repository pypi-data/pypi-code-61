from typing import Literal, Type

from ..helpers.os import has_command
from . import SAMLClient
from .aws_okta import AwsOkta
from .aws_profile import AwsProfile
from .saml2aws import Saml2Aws

SAMLClientName = Literal["auto", "aws-okta", "saml2aws", "aws-profile"]


def choose_saml_client(saml_client_name: SAMLClientName) -> Type[SAMLClient]:
    if saml_client_name == "aws-okta":
        return AwsOkta
    elif saml_client_name == "saml2aws":
        return Saml2Aws
    elif saml_client_name == "aws-profile":
        return AwsProfile
    else:
        for client in [Saml2Aws, AwsOkta, AwsProfile]:
            if has_command(client.binary):
                return client
    return AwsProfile
