from logging import INFO, DEBUG
from .logging import logger
import boto3
import botocore
import time

CAPABILITIES = ["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
DOES_NOT_EXIST_ERROR = "Stack with id {name} does not exist"
NO_UPDATES_ERROR = "No updates are to be performed."
COMPLETE_STATES = [ "CREATE_COMPLETE", "UPDATE_COMPLETE" ]

client_cf = boto3.client("cloudformation")

class Stack:
    def __init__(self, name):
        self.name = name

    def _log(self, level, msg):
        logger.log(level, f"Stack({self.name}): {msg}")

    def peek(self):
        stack = self._get()
        if stack is None:
            return None
        outputs = stack.get("Outputs", list())
        return { x["OutputKey"] : x["OutputValue"] for x in outputs }

    def _get(self):
        transient_log = False
        self._log(DEBUG, "Attempting to fetch the stabilized stack.")
        while True:
            try:
                data = client_cf.describe_stacks(
                    StackName = self.name,
                )["Stacks"][0]
            except botocore.exceptions.ClientError as err:
                if err.response["Error"]["Message"] == DOES_NOT_EXIST_ERROR.format(name = self.name):
                    self._log(DEBUG, "Stack doesn't exist")
                    return None
                raise
            if data["StackStatus"].endswith("_IN_PROGRESS"):
                if not transient_log:
                    self._log(DEBUG, "Stack is in a transient state. We will continue to poll.")
                    transient_log = True
                time.sleep(2)
                continue
            if data["StackStatus"].endswith("_FAILED"):
                raise RuntimeError(f"Stack: {self.name} is stuck in a failure state.")
            return data

    def up(self, template):
        self._log(INFO, "Moving stack into an [UP] state.")
        self._get()
        try:
            client_cf.create_stack(
                StackName = self.name,
                TemplateBody = template,
                Capabilities = CAPABILITIES
            )
            self._log(DEBUG, "Stack creation initiated")
        except client_cf.exceptions.AlreadyExistsException:
            self._log(DEBUG, "Can't create as stack already exists. Attempting to update.")
            try:
                client_cf.update_stack(
                    StackName = self.name,
                    TemplateBody = template,
                    Capabilities = CAPABILITIES
                )
                self._log(DEBUG, "Stack update initiated")
            except botocore.exceptions.ClientError as err:
                if err.response["Error"]["Message"] != NO_UPDATES_ERROR:
                    raise
                self._log(DEBUG, "Stack hasn't changed. Skipping update.")

        data = self._get()
        if data["StackStatus"] not in COMPLETE_STATES:
            raise RuntimeError(f"Stack: {self.name} is in a bad state.")

        outputs = data.get("Outputs", list())
        return { x["OutputKey"] : x["OutputValue"] for x in outputs }

    def down(self):
        self._log(INFO, "Moving stack into a [DOWN] state")
        self._get()
        client_cf.delete_stack(
            StackName = self.name,
        )
        self._get()