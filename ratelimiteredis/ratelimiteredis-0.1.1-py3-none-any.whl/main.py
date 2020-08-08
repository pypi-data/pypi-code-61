from .redis import RedisInterface
from .utils import calc_ttl, parse_rate


class RateLimit:
    def __init__(self, redis: RedisInterface):
        self.redis = redis.pool
        self.encoding = redis._encoding

    async def _handling(self, rate: str, key: str, value: str) -> dict:
        count, seconds = parse_rate(rate)
        redis_key = f"[{key}][{value}][{count}/{seconds}]"

        current = await self.redis.get(redis_key, encoding=self.encoding)
        if current:
            current = int(current)
            if current >= count:
                return {
                    "ratelimited": True,
                    "data": {
                        "limit": count,
                        "remaining": count - (current if current else 0),
                        "reset": calc_ttl(await self.redis.ttl(redis_key)),
                    },
                }

        value = await self.redis.incr(redis_key)
        if value == 1:
            await self.redis.expire(redis_key, seconds)

        return {
            "ratelimited": False,
            "data": {
                "limit": count,
                "remaining": count - (current if current else 0),
                "reset": calc_ttl(await self.redis.ttl(redis_key)),
            },
        }

    async def set(self, rate: str, key: str, value: str) -> None:
        await self._handling(rate, key, value)

    async def get(self, rate: str, key: str, value: str) -> dict:
        return await self._handling(rate, key, value)
