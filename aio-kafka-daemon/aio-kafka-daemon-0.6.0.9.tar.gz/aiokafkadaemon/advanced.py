"""
Main score worker class implementation
"""
import asyncio
import base64
import json
import tempfile

import aiofiles
import aioredis
from yarl import URL

from .errors import AudioUndecodableException
from .worker import Worker


class AdvancedWorker(Worker):
    """
    Worker class runs the main worker for the scoring service
    """

    def __init__(self, testing=False, score_model=None, kafka_opts={}, redis_opts={}):
        """
        Lowering max_poll_interval_ms from 300s to 60s to be more responsive
        to rebalance error, reduce the impact of user timeouts
        """
        super().__init__(
            kafka_broker_addr=kafka_opts.get("broker"),
            kafka_group_id=kafka_opts.get("group_id"),
            consumer_topic=kafka_opts.get("topic"),
            create_consumer=False if testing else True,
            create_producer=False if testing else True,
            sasl_opts=kafka_opts.get("sasl_opts"),
            consumer_opts={"max_poll_interval_ms": 60000},
        )
        self._testing = testing
        self._audio_path = tempfile.mkdtemp()
        self._score_model = score_model
        self._versions = AdvancedWorker.get_worker_version()

        self._redis_opts = redis_opts
        self._redis = None

    async def start(self):
        """
        Add additional start logic for redis
        """
        await super().start()
        if self._redis_opts:
            self._redis = await aioredis.create_redis_pool(self._redis_opts["url"])

    async def stop(self):
        """
        Add additional stop logic for redis
        """
        await super().stop()
        if self._redis is not None:
            self._redis.close()
            await self._redis.wait_closed()

    @staticmethod
    def get_worker_version():
        """
        Parses worker metadada and returns it
        :return:
        """
        with open("metadata.json", "r") as f:
            data = f.read()
            metadata = json.loads(data)
        return metadata

    @staticmethod
    def is_binary_audio(audio):
        try:
            # Let's try forcing decode here to check it's ok
            if str(audio, "utf-8"):
                audio = None
        except UnicodeDecodeError:
            # This is ok
            pass
        return audio

    @staticmethod
    async def read_local(path):
        audio = None
        async with aiofiles.open(path, "rb") as f:
            audio = await f.read()

        return AdvancedWorker.is_binary_audio(audio)

    @staticmethod
    async def read_http_audio(url, session):
        audio = None
        encoded_url = URL(url, encoded=True)
        async with session.get(encoded_url, timeout=5) as response:
            audio = await response.read()

        return AdvancedWorker.is_binary_audio(audio)

    @staticmethod
    async def read_redis_audio(url, redis_client):
        audio = None
        if not redis_client:
            raise Exception("Redis not initiated")

        key = url.split("//")[1]
        audio_base64 = await redis_client.get(key, encoding="utf-8")
        audio = base64.b64decode(audio_base64)
        return AdvancedWorker.is_binary_audio(audio)

    @staticmethod
    async def fetch_and_write(audio_url, session, redis_client, file_path, retry=2):
        # It assumes the checking for allow local was already done.
        # Let's propagate any exception by the main function
        audio = None
        while retry:
            if audio_url.startswith("http"):
                audio = await AdvancedWorker.read_http_audio(audio_url, session)
            elif audio_url.startswith("redis"):
                audio = await AdvancedWorker.read_redis_audio(audio_url, redis_client)
            else:
                audio = await AdvancedWorker.read_local(audio_url)
            if audio:
                break
            await asyncio.sleep(0.5)

            retry -= 1

        if not audio:
            raise AudioUndecodableException()
        async with aiofiles.open(file_path, "wb") as f:
            await f.write(audio)
