import asyncio
from inspect import iscoroutinefunction, signature, _empty
from typing import Callable
from types import BuiltinFunctionType, FunctionType

from nats.aio.client import Client as NATS
from stan.aio.client import Client as STAN
from stan.aio.client import Msg as Message
from stan.aio.client import Subscription
from fastapi import FastAPI
from pydantic import BaseSettings, BaseModel, ValidationError


class FastSTANSettings(BaseSettings):
    host: str = "127.0.0.1"
    port: int = 8222
    cluster: str = "test-cluster"
    client: str = "test-client"


class FastSTAN(FastAPI):
    def __init__(self, fastapi_settings: dict = {}, **kwargs):
        self._settings = FastSTANSettings(**kwargs)
        self._fastapi_settings = fastapi_settings
        self.nc = NATS()
        self.sc = STAN()
        self.subscribers: dict = {}
        super().__init__(**fastapi_settings)
        self.__register_events__()
        self.__register_endpoints__()

    @staticmethod
    def __parse_args__(function: Callable, arbitrary_types_allowed: bool = True):
        """Return argument parser for given function."""
        s = signature(function)

        for _, arg in s.parameters.items():
            try:
                is_model = issubclass(arg.annotation, BaseModel)
                is_class = True
            except TypeError:
                is_model = False
                is_class = False

            # Case 1: We got a pydantic model
            if is_model:
                return lambda data: arg.annotation.parse_raw(data)

            # Case 2: We don't have an annotation
            if arg.annotation is _empty:
                return lambda data: data

            # Case 3: It's a function
            if isinstance(arg.annotation, (FunctionType, BuiltinFunctionType)):
                return lambda data: arg.annotation(data)

            # Case 4: It's something else. Let pydantic perform the validation

            class _Model(BaseModel):
                __root__: arg.annotation

                class Config:
                    arbitrary_types_allowed = True

            def parser(data: bytes):
                try:
                    return _Model.parse_raw(data).__root__
                except ValidationError as main_error:
                    try:
                        return _Model(__root__=data).__root__
                    except ValidationError:
                        pass
                    raise main_error

            return parser

    def subscribe(
        self,
        channel: str,
        error_cb: Callable = None,
        arbitrary_types_allowed: bool = True,
        **kwargs,
    ) -> Callable[[None], None]:
        """Register a new subscriber.
        
        Arguments:
            channel: The channel to subscribe to.
            error_cb: The function that handles errors.
            arbitrary_types_allowed: See pydantic `arbitrary_types_allowed` configuration.
            **kwargs: Any valid keyword argument for the stan client `.subscribe()` method.
        """

        def decorator(function: Callable) -> None:
            """Register a new subscriber

            Arguments:
                function: The function that will be used as callback when receiving messages.
            """
            parse = self.__parse_args__(function, arbitrary_types_allowed)

            # Define a function that will register subscriber
            async def register_subscriber() -> None:
                """Define subscription callback and error callback and enable subscription."""
                sc = self.sc

                async def error_callback(error: Exception):
                    """This function will process every error encountered in subscription callback."""
                    nonlocal error_cb

                    # If an error callback was given then use it.
                    if error_cb:
                        wrapper = error_cb(error)
                        if iscoroutinefunction(error_cb):
                            await wrapper
                    # Default behavior is to log error to stdout.
                    else:
                        print(f"ERROR :: {error}")

                # Define the callback function
                async def callback(msg: Message) -> None:
                    """This function will process every message received during subscription."""
                    nonlocal sc
                    nonlocal function

                    # First try to validate the data
                    try:
                        data = parse(msg.data)
                        result = function(data)
                        if iscoroutinefunction(function):
                            await result
                    # Acknowledge even when there is an exception
                    except Exception as error:
                        await sc.ack(msg)
                        # But raise an error to redirect to error callback
                        raise error
                    # Finally send back acknowledgement
                    await sc.ack(msg)

                # Then subscribe to NATS streaming
                sub = await self.sc.subscribe(
                    channel, cb=callback, error_cb=error_callback, **kwargs
                )
                if "subscription" not in self.subscribers[channel]:
                    self.subscribers[channel]["subscription"] = [sub]
                else:
                    self.subscribers[channel]["subscription"].append(sub)

            # Append the function to register subscriber to the list of subscribers.
            # It will be used later when connecting the application to NATS
            if channel not in self.subscribers:
                self.subscribers[channel] = {"register": [register_subscriber]}
            else:
                self.subscribers[channel]["register"].append(register_subscriber)

        # We must return the decorator else python complains but it will never be used
        return decorator

    async def __register_subscriptions__(self):
        for channel, _dict in self.subscribers.items():
            for register in _dict["register"]:
                await register()

    def __register_endpoints__(self):
        """Register HTTP endpoints."""

        @self.get("/healthz", tags=["Monitoring"], summary="Get health")
        def health():
            if self.sc._loop.is_running():
                try:
                    _ = self.sc._conn_id
                except AttributeError:
                    pass
                else:
                    return {"status": "OK"}

        class TestPublish(BaseModel):
            channel: str
            msg: bytes

        @self.post(
            "/test", tags=["Debug"], summary="Publish a message to test a subscriber"
        )
        def publish(body: TestPublish):
            return self.publish(body.channel, body.msg)

    def __register_events__(self):
        """Register startup and shutdown events."""

        @self.on_event("startup")
        async def connect():
            print("Connection to NATS and STAN.")
            await self.start()

        @self.on_event("shutdown")
        async def disconnect():
            await self.stop()

    async def connect(self):
        """Connect NATS streaming on top of NATS cluster"""
        uri = f"nats://{self._settings.host}:{self._settings.port}"

        # client on top.
        await self.nc.connect()

        # Start session with NATS Streaming cluster.
        await self.sc.connect(
            self._settings.cluster, self._settings.client, nats=self.nc
        )

    async def start(self, connect: bool = True):
        if connect:
            await self.connect()
        await self.__register_subscriptions__()

    async def stop(self):
        for channel, _dict in self.subscribers.items():
            for sub in _dict["subscription"]:
                await sub.unsubscribe()
        await self.sc.close()
        await self.nc.close()

    async def publish(self, channel: str, data: bytes):
        """Publish to a channel."""
        return await self.sc.publish(channel, data)
