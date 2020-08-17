import asyncio
from inspect import iscoroutinefunction, signature, _empty
from typing import Callable

from nats.aio.client import Client as NATS
from stan.aio.client import Client as STAN
from stan.aio.client import Msg as Message
from pydantic import BaseSettings, BaseModel, ValidationError


class FastSTANSettings(BaseSettings):
    host: str = "127.0.0.1"
    port: int = 8222
    cluster: str = "test-cluster"
    client: str = "test-client"


class FastSTAN:
    def __init__(self, **kwargs):
        self.settings = FastSTANSettings(**kwargs)
        self.nc = NATS()
        self.sc = STAN()
        self.subscribers: List[Callable] = []

    @staticmethod
    def __parse_args__(function: Callable, arbitrary_types_allowed: bool = True):
        """Return argument parser for given function."""
        s = signature(function)

        for _, arg in s.parameters.items():
            try:
                is_model = issubclass(arg.annotation, BaseModel)
            except TypeError:
                is_model = False
            # Case 1: We got a pydantic model
            if is_model:
                parser = lambda data: arg.annotation.parse_raw(data)
            # Case 2: We got an annotation that is not a pydantic model
            elif arg.annotation is not _empty:

                class _Model(BaseModel):
                    __root__: arg.annotation

                    class Config:
                        arbitrary_types_allowed = True

                parser = lambda data: _Model.parse_raw(data).__root__
            # Case 3: No annotation available
            else:
                parser = lambda data: data
            # TODO: Support dependencies as arguments
            break
        return parser

    def subscribe(
        self,
        topic: str,
        error_cb: Callable = None,
        arbitrary_types_allowed: bool = True,
    ) -> Callable[[None], None]:
        """Decorator factory to add subscription.
        
        Arguments:
            topic: The topic to subscribe to
        """

        def decorator(function: Callable) -> None:
            """Decorator to add subscription.

            Arguments:
                function: The function that will be used as callback when receiving messages
            """
            parse = self.__parse_args__(function, arbitrary_types_allowed)

            # Define a function that will register subscriber
            async def register_subscriber() -> None:
                """Define callback and enable subscription."""
                sc = self.sc

                async def error_callback(error):
                    nonlocal sc
                    if error_cb:
                        wrapper = error_cb(error)
                    if iscoroutinefunction(error_cb):
                        await wrapper

                # Define the callback function
                async def callback(msg: Message) -> None:
                    """Subscription callback"""
                    nonlocal sc

                    # First try to validate the data
                    try:
                        data = parse(msg.data)
                        result = function(data)
                        if iscoroutinefunction(function):
                            await result
                    except Exception as error:
                        await sc.ack(msg)
                        raise error
                    # Finally send back acknowledgement
                    else:
                        await sc.ack(msg)

                # Then subscribe to NATS streaming
                sub = await self.sc.subscribe(
                    topic, cb=callback, error_cb=error_callback
                )

            # Append the function to register subscriber to the list of subscribers.
            # It will be used later when connecting the application to NATS
            self.subscribers.append(register_subscriber)

        # We must return the decorator else python complains but it will never be used
        return decorator

    async def __register__(self):
        for future_subscription in self.subscribers:
            await future_subscription()

    async def __connect__(self):
        """Connect NATS streaming on top of NATS cluster"""
        uri = f"nats://{self.settings.host}:{self.settings.port}"

        # client on top.
        await self.nc.connect()

        # Start session with NATS Streaming cluster.
        await self.sc.connect(self.settings.cluster, self.settings.client, nats=self.nc)

    async def run(self):
        await self.__connect__()
        await self.__register__()

    def run_forever(self, loop=None):
        """Run the application forever."""
        if loop is None:
            loop = asyncio.get_event_loop()
        loop.run_until_complete(self.run())
        self.sc._loop.run_forever()
