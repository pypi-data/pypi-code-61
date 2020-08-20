import asyncio
from typing import Callable

from stan.aio.client import Msg as Message

from .utils import run_func
from .publisher import STANPublisher, STANPublisherSettings
from .parser import PydanticParserMixin


class STANSubscriberSettings(STANPublisherSettings):
    client: str = "test-subscriber"


class STANSubscriber(PydanticParserMixin, STANPublisher):
    def __init__(
        self,
        host: str = None,
        port: int = None,
        cluster: str = None,
        client: str = None,
        **kwargs,
    ):
        self.__prepare__(host, port, cluster, client, validator=STANSubscriberSettings)
        self.__factories__ = {}
        self.__subscriptions__ = {}

    def __get_error_callback__(self, error_cb: Callable[[Exception], None] = None):
        """Return a function that can be used as an error callback."""
        if error_cb:
            # Wrap given callback
            async def callback(msg: Message, error: Exception) -> None:
                """Wrapper around user error callback"""
                nonlocal error_cb
                await run_func(error_cb, error)
                await self.sc.ack(msg)

        else:
            # Default callback
            async def callback(msg: Message, error: Exception) -> None:
                """Default error callback"""
                print(f"ERROR :: {error}")
                await self.sc.ack(msg)

        return callback

    def __get_callback__(
        self,
        function: Callable,
        error_cb: Callable,
        arbitrary_types_allowed: bool = True,
    ):
        """Return a function that can be used as a subscription callback."""
        _, _, parser = self.__get_parser__(function, arbitrary_types_allowed)

        if parser:

            async def callback(msg: Message) -> None:
                """This function will process every message received during subscription."""
                nonlocal function
                nonlocal parser
                try:
                    # Validate the data
                    data = parser(msg.data)
                    # Execute the function
                    await run_func(function, data)
                except Exception as error:
                    await error_cb(msg, error)
                else:
                    # Finally send back acknowledgement
                    await self.sc.ack(msg)

        else:

            async def callback(msg: Message):
                await run_func(function)

        # Return the callback function
        return callback

    async def __subscribe__(self, channel: str, callback: Callable, **kwargs):
        """Subscribe to a channel."""
        sub = await self.sc.subscribe(channel, cb=callback, **kwargs,)

        sub_id = id(sub)

        if channel not in self.__subscriptions__:
            self.__subscriptions__[channel] = {sub_id: sub}
        self.__subscriptions__[channel][sub_id] = sub

    def __subscription_factory__(
        self,
        channel: str,
        function: Callable,
        error_cb: Callable,
        arbitrary_types_allowed: bool = True,
        **kwargs,
    ):
        error_callback = self.__get_error_callback__(error_cb)
        callback = self.__get_callback__(function, error_callback)

        # Define a function that will run subscriber
        async def start_subscription() -> None:
            """Start subscription"""
            await self.__subscribe__(channel, callback, **kwargs)

        # Append the function to register subscriber to the list of subscribers.
        # It will be used later when connecting the application to NATS
        if channel not in self.__factories__:
            self.__factories__[channel] = [start_subscription]
        else:
            self.__factories__[channel].append(start_subscription)

        return start_subscription

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
            return self.__subscription_factory__(
                channel, function, error_cb, arbitrary_types_allowed, **kwargs
            )

        # We must return the decorator else python complains but it will never be used
        return decorator

    async def start(self):
        """Start all subscriptions."""
        for channel, subscriptions in self.__factories__.items():
            print(f"Starting subscriptions for channel {channel}")
            for subscription in subscriptions:
                print(f"Enabling subscription {subscription}")
                await subscription()

    async def stop(self):
        """Stop all subcriptions."""
        for channel, subscriptions in self.__subscriptions__.items():
            print(f"Stopping subscriptions for channel {channel}")
            for sub_id in list(subscriptions.keys()):
                print(f"Stopping subscription {sub_id}")
                await subscriptions[sub_id].unsubscribe()
                del subscriptions[sub_id]

    async def run(self):
        """Connect to NATS and STAN and start all subscriptions."""
        await self.connect()
        await self.start()

    def run_forever(self):
        """Connect to NATS and STAN and start all subscriptions.
        This function will never return a value and will run until stopped.
        """
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.run())
        loop.run_forever()
