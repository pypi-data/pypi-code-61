import json
from typing import Type
from pydantic import BaseSettings, BaseModel
from nats.aio.client import Client as NATS
from stan.aio.client import Client as STAN


class STANPublisherSettings(BaseSettings):
    host: str = "127.0.0.1"
    port: int = 4222
    cluster: str = "test-cluster"
    client: str = "test-publisher"

    class Config:
        env_prefix = "stan_"


class STANPublisher:
    def __init__(
        self,
        host: str = None,
        port: int = None,
        cluster: str = None,
        client: str = None,
        **kwargs,
    ):
        self.__prepare__(host, port, cluster, client, **kwargs)

    def __prepare__(
        self,
        host: str = None,
        port: int = None,
        cluster: str = None,
        client: str = None,
        validator: Type[BaseModel] = STANPublisherSettings,
        **kwargs,
    ):
        options = {
            key: value
            for (key, value) in [
                ("host", host),
                ("port", port),
                ("cluster", cluster),
                ("client", client),
            ]
            if value is not None
        }
        self._settings = validator(**options)
        self.nc = NATS()
        self.sc = STAN()

    async def connect(self):
        """Connect NATS streaming on top of NATS cluster"""
        # TODO: Support specifying NATS servers
        # uri = f"nats://{self._settings.host}:{self._settings.port}"

        # client on top.
        await self.nc.connect([f"nats://{self._settings.host}:{self._settings.port}"])

        # Start session with NATS Streaming cluster.
        await self.sc.connect(
            self._settings.cluster, self._settings.client, nats=self.nc
        )

    async def close(self):
        await self.sc.close()
        await self.nc.close()

    async def publish(self, channel: str, data: bytes):
        """Publish to a channel.

        Arguments:
            channel: The channel to publish to.
            data: The content of the message to publish.
        """
        return await self.sc.publish(channel, data)

    async def publish_str(self, channel: str, data: str, encoding: str = "utf-8"):
        """Publish a string to a channel

        Arguments:
            channel: The channel to publish to.
            data: A string to send as message content.
            encoding: Encoding to use when converting string to bytes.
        """
        return await self.publish(channel, bytes(data, encoding))

    async def publish_json(self, channel: str, data):
        """Publish JSON serializable object.

        Arguments:
            channel: The channel to publish to.
            data: Any JSON serializable object to send as message content.
        """
        return await self.publish_str(channel, json.dumps(data))

    async def publish_pydantic_model(self, channel: str, data: BaseModel):
        """Publish a pydantic model.

        Arguments:
            channel: The channel to publish to.
            data: Any instance of a class that inherits `pydantic.BaseModel`
        """
        return await self.publish_str(channel, data.json())
