import re
from datetime import datetime, timedelta
from pathlib import Path
from subprocess import CalledProcessError
from textwrap import dedent
from typing import Sequence

from ..decorators import intercept_errors, run_subprocess
from ..errors import (
    AccessDenied,
    SuppressedError,
    TargetNotConnected,
    WrappedSubprocessError,
)
from ..helpers.boto import send_ssh_key
from ..helpers.config import Config, SymConfigFile
from ..helpers.params import get_ssh_user

MissingPublicKeyPattern = re.compile(r"Permission denied \(.*publickey.*\)")
TargetNotConnectedPattern = re.compile("TargetNotConnected")
AccessDeniedPattern = re.compile("AccessDeniedException")
ConnectionClosedPattern = re.compile(r"Connection to .* closed")

SSHConfigPath = "ssh/config"
SSHKeyPath = "ssh/key"


@intercept_errors()
@run_subprocess
def gen_ssh_key(dest: SymConfigFile):
    with dest.exclusive_create() as f:
        Path(f.name).unlink(missing_ok=True)
        yield "ssh-keygen", {"t": "rsa", "f": f.name, "N": ""}


def ssh_args(client, instance, port) -> tuple:
    return (
        "ssh",
        instance,
        {
            "p": str(port),
            "F": str(client.subconfig(SSHConfigPath)),
            "l": get_ssh_user(),
            "v": client.debug,
        },
    )


@run_subprocess
def _start_background_ssh_session(
    client: "SAMLClient", instance: str, port: int, *command
):
    yield (
        *ssh_args(client, instance, port),
        {"f": True},
        "-o BatchMode=yes",
        *command,
    )


@run_subprocess
def _start_ssh_session(client: "SAMLClient", instance: str, port: int, *command: str):
    yield (*ssh_args(client, instance, port), *command)


def start_ssh_session(
    client: "SAMLClient", instance: str, port: int, command: Sequence[str] = []
):
    ensure_ssh_key(client, instance, port)
    try:
        _start_ssh_session(client, instance, port, *command)
    except CalledProcessError as err:
        if MissingPublicKeyPattern.search(err.stderr):
            Config.touch_instance(instance, error=True)
            raise WrappedSubprocessError(
                err, f"Does the user ({get_ssh_user()}) exist on the instance?"
            ) from err
        # If the ssh key path is cached then this doesn't get intercepted in ensure_ssh_key
        elif TargetNotConnectedPattern.search(err.stderr):
            raise TargetNotConnected() from err
        elif AccessDeniedPattern.search(err.stderr):
            raise AccessDenied() from err
        elif ConnectionClosedPattern.search(err.stderr):
            raise SuppressedError(err, echo=True) from err
        else:
            raise WrappedSubprocessError(
                err, f"Contact your Sym administrator.", report=True
            ) from err
    else:
        Config.touch_instance(instance)


@intercept_errors({TargetNotConnectedPattern: TargetNotConnected}, suppress=True)
def ensure_ssh_key(client, instance: str, port: int):
    ssh_key = client.subconfig(SSHKeyPath)
    ssh_config = client.subconfig(SSHConfigPath)

    # fmt: off
    ssh_config.put(dedent(  # Ensure the SSH Config first, always
        f"""
        Host *
            IdentityFile {str(ssh_key)}
            PreferredAuthentications publickey
            PubkeyAuthentication yes
            StrictHostKeyChecking no
            PasswordAuthentication no
            ChallengeResponseAuthentication no
            GSSAPIAuthentication no
            ProxyCommand sh -c "sym ssh-session {client.resource} --instance %h --port %p"
        """
    ))
    # fmt: on

    instance_config = Config.get_instance(instance)

    if not ssh_key.path.exists():
        gen_ssh_key(ssh_key, capture_output_=True)

    last_connect = instance_config.get("last_connection")
    if last_connect and datetime.now() - last_connect < timedelta(days=1):
        client.dprint(f"Skipping remote SSH key check for {instance}")
        return

    try:
        _start_background_ssh_session(
            client, instance, port, "exit", capture_output_=True
        )
    except CalledProcessError as err:
        if not MissingPublicKeyPattern.search(err.stderr):
            raise
        send_ssh_key(client, instance, ssh_key)
    else:
        return


def start_tunnel(client, instance: str, port: int):
    client.exec(
        "aws",
        "ssm",
        "start-session",
        target=instance,
        document_name="AWS-StartSSHSession",
        parameters=f"portNumber={port}",
    )
