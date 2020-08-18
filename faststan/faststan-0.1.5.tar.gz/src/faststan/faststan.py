from fastapi import status, FastAPI
from fastapi.responses import JSONResponse
from faststan.subscriber import STANSubscriber


class FastSTAN(FastAPI):
    def __init__(self, fastapi_settings: dict = {}, **kwargs):
        super().__init__(**fastapi_settings)
        self.stan = STANSubscriber(**kwargs)
        self.__set_endpoints__()
        self.__register_events__()

    def __set_endpoints__(self):
        """Register endpoints."""

        @self.get(
            path="/info", tags=["Monitoring"], summary="Get basic informations",
        )
        def infos():
            return self.stan._settings.dict()

        @self.get(
            path="/healthz",
            tags=["Monitoring"],
            summary="Get health",
            responses={
                200: {"description": "System is healthy"},
                503: {"description": "System is unhealthy"},
            },
        )
        def health():
            """Get health of system."""
            if self.stan.nc.CONNECTED:
                try:
                    _ = self.stan.sc._client_id
                    return {"status": "ok", "nats": "ok", "stan": "ok"}
                except AttributeError:
                    return JSONResponse(
                        content={"status": "bad", "nats": "ok", "stan": "bad"},
                        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                    )
                    pass
            return JSONResponse(
                content={"status": "bad", "nats": "ok", "stan": "ok"},
                status_code=status.HTTP_200_OK,
            )

    def __register_events__(self):
        """Register startup and shutdown events."""

        @self.on_event("startup")
        async def connect():
            await self.stan.run()

        @self.on_event("shutdown")
        async def disconnect():
            await self.stan.stop()
            await self.stan.close()
