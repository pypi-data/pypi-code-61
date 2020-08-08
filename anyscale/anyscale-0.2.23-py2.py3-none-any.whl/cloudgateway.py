import base64
import copy
import json
import logging
import os
import subprocess
import time
from typing import Any, Dict

import click
from ray.autoscaler.node_provider import get_node_provider, NodeProvider

from anyscale.util import send_json_request

logger = logging.getLogger(__name__)

try:
    import requests
except ImportError:
    logger.exception(
        "Couldn't import `requests` library. Try installing it with `pip install requests`."
    )

ClusterName = str
ProviderConfig = Dict[str, Any]
ClusterConfig = Dict[str, Any]
Request = Dict[str, Any]
Response = Dict[str, Any]


class CloudGatewayRunner:
    """Initializes and runs the cloud gateway.

    Args:
        anyscale_address (str): the address to the anyscale end point.
    """

    def __init__(self, anyscale_address: str) -> None:
        self.anyscale_address = anyscale_address
        self.cached_node_providers: Dict[ClusterName, NodeProvider] = {}

    def _get_bootstrapped_config(
        self, provider_config: ProviderConfig, cluster_config: ClusterConfig
    ) -> Any:
        """Receives the cluster config from the server and bootstraps it."""
        node_provider = get_node_provider(
            provider_config, cluster_config["cluster_name"]
        )
        orig_provider_config = copy.deepcopy(cluster_config["provider"])
        cluster_config["provider"] = cluster_config["provider"]["subprovider"]
        bootstrapped_config = node_provider.bootstrap_config(cluster_config)
        bootstrapped_config["provider"] = orig_provider_config
        # Cache the node provider to avoid bootstrapping for every request
        self.cached_node_providers[cluster_config["cluster_name"]] = node_provider
        return bootstrapped_config

    def _process_request(
        self,
        request: Request,
        cluster_name: ClusterName,
        provider_config: ProviderConfig,
    ) -> Response:
        """Receives the request and processes it."""
        # TODO(ameer): make it multithreaded to support simultaneous execution
        provider_request_types = [
            "non_terminated_nodes",
            "is_running",
            "is_terminated",
            "node_tags",
            "external_ip",
            "internal_ip",
            "create_node",
            "set_node_tags",
            "terminate_node",
            "terminate_nodes",
            "cleanup",
        ]
        cmd_runner_request_types = [
            "cmd_runner.run",
            "cmd_runner.run_rsync_up",
            "cmd_runner.run_rsync_down",
            "cmd_runner.remote_shell_command_str",
        ]
        if request["type"] == "bootstrap_config":
            cluster_config = request["args"][0]
            response = self._get_bootstrapped_config(provider_config, cluster_config)
        elif request["type"] in provider_request_types:
            if cluster_name not in self.cached_node_providers:
                self.cached_node_providers[cluster_name] = get_node_provider(
                    provider_config, cluster_name
                )
            response = self._handle_node_provider_requests(
                request, cluster_name, self.cached_node_providers[cluster_name],
            )
        elif request["type"] in cmd_runner_request_types:
            if cluster_name not in self.cached_node_providers:
                self.cached_node_providers[cluster_name] = get_node_provider(
                    provider_config, cluster_name
                )
            response = self._handle_cmd_runner_request(
                request, self.cached_node_providers[cluster_name]
            )
        else:
            logger.error(
                "The cloud gateway does not support request of type: " + request["type"]
            )
            response = None
        response_message = {"data": response, "request_id": request["request_id"]}
        return response_message

    def _handle_cmd_runner_request(
        self, request: Request, node_provider: NodeProvider,
    ) -> Any:
        """Handles command runner requests."""
        response: Any = None
        if request["type"] == "cmd_runner.run":
            cmd_runner_kwargs, cmd, run_args, run_kwargs = request["args"]
            cmd = self._temporary_aws_credentials_if_necessary(cmd)
            cmd_runner = node_provider.get_command_runner(
                **cmd_runner_kwargs, process_runner=subprocess
            )
            try:
                cmd_runner.run(cmd, *run_args, **run_kwargs)
                response = None
            except Exception as e:
                if isinstance(e, click.ClickException):
                    response = {
                        "exception_type": "click.ClickException",
                        "error_str": str(e),
                    }
                elif isinstance(e, subprocess.CalledProcessError):
                    response = {
                        "exception_type": "subprocess.CalledProcessError",
                        "returncode": e.returncode,
                        "cmd": e.cmd,
                    }
                else:
                    response = {"exception_type": "Exception", "error_str": str(e)}
        elif request["type"] == "cmd_runner.run_rsync_up":
            cmd_runner_kwargs, source, target, content, mode = request["args"]
            try:
                # Store file on the gateway node.
                with open(os.path.expanduser(target), "wb") as f:
                    f.write(base64.b64decode(content))
            except PermissionError:
                logger.warning("File already exists.")
            os.chmod(os.path.expanduser(target), mode)
            cmd_runner = node_provider.get_command_runner(
                **cmd_runner_kwargs, process_runner=subprocess
            )
            # Send file from gateway node (local target) to remote target
            cmd_runner.run_rsync_up(os.path.expanduser(target), target)
            response = None
        elif request["type"] == "cmd_runner.run_rsync_down":
            cmd_runner_kwargs, source, target = request["args"]
            cmd_runner = node_provider.get_command_runner(
                **cmd_runner_kwargs, process_runner=subprocess
            )
            # rsync the source file to the the gateway node with file name <source>.
            cmd_runner.run_rsync_down(source, os.path.expanduser(source))
            if not os.path.isfile(os.path.expanduser(source)):
                raise ValueError(
                    "The cloudgateway supports downloading a single file only."
                )
            mode = os.stat(os.path.expanduser(source)).st_mode & 0o777
            try:
                with open(os.path.expanduser(source), "rb") as f:
                    # Decode makes it json dumpable.
                    content = base64.b64encode(f.read()).decode()
                    response = {"content": content, "mode": mode}
            except FileNotFoundError:
                response = {"content": None, "mode": None}
        elif request["type"] == "cmd_runner.remote_shell_command_str":
            cmd_runner_kwargs = request["args"]
            cmd_runner = node_provider.get_command_runner(
                **cmd_runner_kwargs, process_runner=subprocess
            )
            response = cmd_runner.remote_shell_command_str()
        return response

    def _handle_node_provider_requests(
        self, request: Request, cluster_name: ClusterName, node_provider: NodeProvider,
    ) -> Any:
        """Handles node provider requests."""
        response = getattr(node_provider, request["type"])(*request["args"])
        return response

    def _temporary_aws_credentials_if_necessary(self, cmd: str) -> str:
        """The temporary aws credentials if necessary for temporary access to S3."""
        new_cmd = cmd
        # TODO(ameer): This is really ugly
        if "s3:s3.amazonaws.com" in cmd and "RESTIC_PASSWORD=program_the_cloud" in cmd:
            try:
                resp = send_json_request("/api/v2/users/temporary_aws_credentials", {})
                aws_credentials_vars = " ".join(
                    [key + "=" + resp["result"][key] for key in resp["result"]]
                )
            except Exception as e:
                # The snapshot may not exist.
                raise click.ClickException(e)  # type: ignore

            new_cmd = cmd.replace(
                "RESTIC_PASSWORD=program_the_cloud",
                aws_credentials_vars + " RESTIC_PASSWORD=program_the_cloud",
            )

        return new_cmd

    def gateway_run_forever(self) -> None:
        """Long polls anyscale server."""
        # TODO(ameer): make this run in the background,
        # need to fix the autoscaler cleanup function.
        self._run()

    def _run(self) -> None:
        response_message: Dict[str, Any] = {"data": "first_message", "request_id": "0"}
        while 1:
            try:
                request = send_json_request(
                    self.anyscale_address,
                    {"contents": json.dumps(response_message)},
                    method="POST",
                )
            except Exception:
                logger.exception("Could not connect to Anyscale server. Retrying...")
                response_message = {"data": "first_message", "request_id": "0"}
                time.sleep(10)
                continue
            logger.info("Received request: " + str(request["result"]["type"]))
            try:
                response_message = self._process_request(
                    request["result"],
                    request["result"]["cluster_name"],
                    request["result"]["provider_config"],
                )
            except Exception as e:
                # Gateway Error.
                logger.exception(type(e).__name__ + ": " + str(e))
                response_message = {
                    "data": type(e).__name__ + ": " + str(e),
                    "request_id": request["result"]["request_id"],
                }
